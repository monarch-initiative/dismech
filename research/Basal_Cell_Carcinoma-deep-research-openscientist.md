---
provider: openscientist
model: openscientist-autonomous
cached: false
end_time: '2026-05-06T00:20:20.473762+00:00'
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Basal Cell Carcinoma
  mondo_id: ''
  category: ''
citation_count: 70
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Basal Cell Carcinoma
- **MONDO ID:**  (if available)
- **Category:**

## Research Objectives

Please provide a comprehensive research report on **Basal Cell Carcinoma** covering all of the
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

# Comprehensive Disease Characterization: Basal Cell Carcinoma

## Summary

**Basal cell carcinoma (BCC)** is the most common human malignancy worldwide, accounting for approximately 80% of all keratinocyte cancers. Driven in nearly all cases by constitutive activation of the **Hedgehog (HH) signaling pathway** — primarily through loss-of-function mutations in *PTCH1* (~73% of cases) or gain-of-function mutations in *SMO* (~10–20%) — BCC arises from the interplay between chronic ultraviolet radiation (UVR) exposure, genetic susceptibility in pigmentation-related genes (*MC1R*, *ASIP*, *TYR*, *OCA2*, *IRF4*, *SLC45A2*), and epigenomic reprogramming. The global incidence is rising steadily, with an estimated annual percentage change (EAPC) of 1.94% from 1990 to 2021, and the age-standardized incidence rate in adults >=65 years reached 371.97 per 100,000 in 2021 ([PMID: 39966563](https://pubmed.ncbi.nlm.nih.gov/39966563/); [PMID: 40397469](https://pubmed.ncbi.nlm.nih.gov/40397469/)).

Treatment follows a tiered approach stratified by disease stage and risk: surgical excision including **Mohs micrographic surgery** (5-year recurrence rate 3.8%) remains the standard for most cases; **Hedgehog pathway inhibitors** (vismodegib and sonidegib, with overall response rates of 65–89%) serve as first-line systemic therapy for locally advanced disease; and **cemiplimab** (anti-PD-1 immunotherapy) provides durable responses for patients who progress on or are intolerant to HH inhibitors. Though typically indolent with >95% cure rates when detected early, locally advanced BCC (5-year disease-specific survival 79%) and rare metastatic BCC (5-year disease-specific survival 30%) remain significant clinical challenges ([PMID: 41039887](https://pubmed.ncbi.nlm.nih.gov/41039887/)).

Prevention centers on UV photoprotection (sunscreen, protective clothing, UV avoidance), early detection through dermoscopy and clinical screening, and heightened surveillance for high-risk populations including immunosuppressed patients, those with hereditary syndromes (Gorlin syndrome, xeroderma pigmentosum), and individuals with fair skin and extensive sun exposure history. The rising global incidence underscores the importance of public health education and primary prevention strategies.

---

## 1. Disease Information

### Overview

Basal cell carcinoma is a malignant neoplasm arising from basal cells of the epidermis and hair follicle structures. It is the single most common cancer in humans, particularly prevalent among fair-skinned populations. BCC is characterized by slow growth, local invasiveness, and an extremely low rate of metastasis (<0.1%), yet untreated lesions can cause significant tissue destruction and functional impairment ([PMID: 31585338](https://pubmed.ncbi.nlm.nih.gov/31585338/); [PMID: 41515948](https://pubmed.ncbi.nlm.nih.gov/41515948/)).

As noted in a comprehensive epidemiological review: *"Basal cell carcinomas (BCC) are the most common, comprising 80% of keratinocyte cancers, but have a very low rate of metastases and low mortality"* ([PMID: 31585338](https://pubmed.ncbi.nlm.nih.gov/31585338/)).

### Key Identifiers

| Database | Identifier |
|----------|-----------|
| **MONDO** | MONDO:0004972 |
| **OMIM** | 605462 (BCC1); 613294 (BCC, susceptibility to) |
| **ICD-10** | C44 (Other malignant neoplasms of skin) |
| **ICD-11** | 2C32.0 (Basal cell carcinoma of skin) |
| **MeSH** | D002280 (Carcinoma, Basal Cell) |
| **Orphanet** | ORPHA:48 (Basal cell carcinoma) |
| **SNOMED CT** | 254701007 (Basal cell carcinoma of skin) |

### Synonyms and Alternative Names

- Basal cell epithelioma
- Basalioma
- Rodent ulcer
- BCC
- Basaloid carcinoma
- Jacob's ulcer

### Information Sources

This report synthesizes information from aggregated disease-level resources (OMIM, Orphanet, GWAS Catalog, COSMIC, GBD), clinical trial data, population-based registries (SEER, Danish national databases), and primary literature (100 papers reviewed from PubMed).

---

## 2. Etiology

### Disease Causal Factors

BCC is a multifactorial disease resulting from the convergence of **genetic**, **environmental**, and **epigenetic** factors. The central molecular driver is constitutive activation of the Hedgehog signaling pathway:

*"Basal cell carcinoma (BCC) is driven in nearly all cases by mutations that constitutively activate upstream Hedgehog (HH) signaling, either through loss-of-function mutations in PTCH1 or gain-of-function mutations in SMO"* ([PMID: 41240053](https://pubmed.ncbi.nlm.nih.gov/41240053/)).

The disease represents a complex interplay: *"BCC is a complex disease, in which the interplay between UVR, phenotype (UVR-sensitive) and genotype (somatic mutations and germline mutations/polymorphisms) fulfils a key role in the aetiopathogenesis"* ([PMID: 28220485](https://pubmed.ncbi.nlm.nih.gov/28220485/)).

### Risk Factors

#### Genetic Risk Factors

- **PTCH1 mutations (9q22.32)**: Loss-of-function mutations in the Hedgehog receptor PTCH1 are found in ~73% of sporadic BCCs (OMIM: 601309). These are predominantly somatic, though germline mutations cause Gorlin syndrome.
- **SMO mutations (7q32.1)**: Gain-of-function mutations in the Smoothened receptor occur in ~10–20% of cases (OMIM: 601500).
- **TP53 mutations**: Found in approximately 50% of BCCs, typically UV-signature C>T transitions.
- **Pigmentation gene variants** (GWAS-identified susceptibility loci):
  - *MC1R* (rs1805007, Arg151Cys) — strongest association with BCC risk; OR = 1.55 (95% CI: 1.45–1.66; P = 4.3 x 10^-17) ([PMID: 21700618](https://pubmed.ncbi.nlm.nih.gov/21700618/))
  - *ASIP/RALY* — associated with agouti signaling and melanogenesis
  - *IRF4* — interferon regulatory factor 4
  - *OCA2* — oculocutaneous albinism type 2
  - *SLC45A2* — solute carrier family 45 member 2
  - *TYR* — tyrosinase
- **Novel susceptibility loci**: 6p25 near *EXOC2* (rs12210050; OR = 1.24, P = 9.9 x 10^-10) and 13q32 near *UBAC2* (rs7335046; OR = 1.26, P = 2.9 x 10^-8) ([PMID: 21700618](https://pubmed.ncbi.nlm.nih.gov/21700618/))

Six pigmentation loci overlap between BCC, SCC, and melanoma: *ASIP/RALY*, *IRF4*, *MC1R*, *OCA2*, *SLC45A2*, and *TYR* ([PMID: 30908599](https://pubmed.ncbi.nlm.nih.gov/30908599/)).

#### Environmental Risk Factors

- **Ultraviolet radiation (UVR)**: The dominant environmental risk factor. *"Chronic ultraviolet radiation (UVR), the dominant risk factor, induces DNA damage and inflammation that dysregulate epigenetic enzymes (e.g., DNMTs, HDACs)"* ([PMID: 42074595](https://pubmed.ncbi.nlm.nih.gov/42074595/)). Both UVA and UVB contribute to BCC through direct DNA damage (cyclobutane pyrimidine dimers) and indirect oxidative stress.
- **Immunosuppression**: Solid organ transplant recipients have markedly increased risk; SIR for skin cancer post-HSCT was 7.21 (95% CI: 3.98–13.08), with allogeneic HSCT SIR of 10.18 ([PMID: 38987869](https://pubmed.ncbi.nlm.nih.gov/38987869/)).
- **Fair skin/Fitzpatrick type I-II**: UV-sensitive phenotype strongly predisposes.
- **Age**: Incidence increases markedly with age; median age at diagnosis ~67–72 years.
- **Sex**: Males are affected more frequently than females.
- **Family history**: First-degree relatives with BCC confer increased risk.
- **Ionizing radiation exposure**: History of radiation therapy.
- **Arsenic exposure**: Environmental or occupational arsenic.
- **Certain medications**: Hydrochlorothiazide, statins, ACE inhibitors, and omeprazole have been associated with increased BCC risk ([PMID: 38282244](https://pubmed.ncbi.nlm.nih.gov/38282244/)).
- **Burns/scars**: Burn scars are recognized risk factors for skin cancer (Marjolin's ulcer) ([PMID: 42023819](https://pubmed.ncbi.nlm.nih.gov/42023819/)).

#### Hereditary Syndromes

- **Gorlin syndrome (Basal cell nevus syndrome, BCNS)**: Autosomal dominant, caused by germline heterozygous mutations in *PTCH1*, *SUFU*, *SMO*, or *PTCH2*. *"Gorlin-Goltz syndrome... is a rare, inherited, autosomal dominant genodermatoses, with variable expression and complete penetrance, characterized by the occurrence of multiple basal cell carcinomas (BCCs) at a young age, palmoplantar pits, keratocystic odontogenic tumors, intracranial ectopic calcifications, facial dysmorphism, and ocular and skeletal anomalies"* ([PMID: 41884741](https://pubmed.ncbi.nlm.nih.gov/41884741/)).
- **Xeroderma pigmentosum (XP)**: Defective nucleotide excision repair leads to extreme UV sensitivity and markedly elevated skin cancer risk ([PMID: 37964400](https://pubmed.ncbi.nlm.nih.gov/37964400/)).

### Protective Factors

#### Genetic Protective Factors

- **MC1R wild-type alleles**: Associated with darker pigmentation and reduced BCC risk.
- **CTSS (Cathepsin S)**: Mendelian randomization identified CTSS as significantly associated with decreased BCC risk ([PMID: 39702585](https://pubmed.ncbi.nlm.nih.gov/39702585/)).
- **Darker skin pigmentation genes**: Higher melanin content provides natural UV protection.

#### Environmental Protective Factors

- **Sunscreen use**: Higher SPF use 15 years prior was associated with reduced BCC risk (P = 0.04) ([PMID: 38282244](https://pubmed.ncbi.nlm.nih.gov/38282244/)).
- **Coffee consumption**: Higher coffee intake was inversely associated with BCC ([PMID: 38282244](https://pubmed.ncbi.nlm.nih.gov/38282244/)).
- **Relaxation activities/stress reduction**: Associated with reduced risk ([PMID: 38282244](https://pubmed.ncbi.nlm.nih.gov/38282244/)).
- **Photoprotective clothing**: Consistent textile sun protection.
- **DNA repair enzymes (topical)**: Topical photolyase with UV filters reduced new BCC incidence by 56% in XP patients ([PMID: 25408650](https://pubmed.ncbi.nlm.nih.gov/25408650/)).

### Gene-Environment Interactions

The interaction between UV exposure and genetic susceptibility is central to BCC pathogenesis. Individuals with *MC1R* variants (red hair, fair skin) who have chronic UV exposure show multiplicative risk increases. UV radiation induces characteristic C>T and CC>TT transitions ("UV signature mutations") in *PTCH1* and *TP53*, linking environmental exposure directly to the genetic driver events. Additionally, chronic UVR dysregulates epigenetic enzymes including DNMTs and HDACs, creating epigenomic reprogramming that contributes to carcinogenesis ([PMID: 42074595](https://pubmed.ncbi.nlm.nih.gov/42074595/)).

---

## 3. Phenotypes

### Clinical Subtypes and Presentations

| Subtype | Frequency | Clinical Features | HPO Term |
|---------|-----------|-------------------|----------|
| **Nodular BCC** | ~60–80% | Pearly, translucent papule/nodule with telangiectasias; may ulcerate centrally | HP:0002671 |
| **Superficial BCC** | ~10–30% | Erythematous, scaly patch or plaque; flat surface with multiple small erosions | HP:0002671 |
| **Infiltrative/morpheaform (sclerodermiform) BCC** | ~5–10% | Scar-like, ill-defined, indurated plaque; white/ivory color | HP:0002671 |
| **Basosquamous (metatypical) BCC** | ~1–2% | Features of both BCC and SCC; more aggressive behavior | HP:0002671 |

**Relevant HPO Terms:**
- HP:0002671 — Basal cell carcinoma
- HP:0008069 — Neoplasm of the skin
- HP:0001000 — Abnormality of skin pigmentation
- HP:0007565 — Multiple basal cell carcinomas (Gorlin syndrome)

### Phenotype Characteristics

- **Age of onset**: Predominantly adult-onset (median ~67–72 years); younger onset in Gorlin syndrome and XP. Outdoor workers develop BCC at older ages than indoor workers ([PMID: 28207005](https://pubmed.ncbi.nlm.nih.gov/28207005/)).
- **Severity**: Variable; ranges from indolent superficial lesions to locally destructive advanced tumors. Sclerodermiform BCCs are diagnosed on average 3.52 years later than non-aggressive subtypes ([PMID: 29723362](https://pubmed.ncbi.nlm.nih.gov/29723362/)).
- **Progression**: Typically slow-growing (months to years); infiltrative subtypes progress more rapidly.
- **Location**: ~75% occur on the head and neck; nose is the most common site (42.9%), followed by cheek (14.3%) and upper lip (11.9%) ([PMID: 40370729](https://pubmed.ncbi.nlm.nih.gov/40370729/)).
- **Frequency**: The most common human cancer; lifetime risk 33–39% for men and 23–28% for women in white populations ([PMID: 35942364](https://pubmed.ncbi.nlm.nih.gov/35942364/)).

### Dermoscopic Features by Subtype

- **Superficial BCC**: Brown globules, shiny white-red structureless areas, flat surface, multiple small erosions ([PMID: 41685950](https://pubmed.ncbi.nlm.nih.gov/41685950/); [PMID: 26921200](https://pubmed.ncbi.nlm.nih.gov/26921200/))
- **Nodular BCC**: Blue structures, arborizing telangiectasias, ulceration, large tumor islands ([PMID: 41685950](https://pubmed.ncbi.nlm.nih.gov/41685950/))
- **Infiltrative BCC**: White porcelain areas, lack of pigmentation, elongated hyporeflective tumor strands ("shoal of fish" pattern on LC-OCT) ([PMID: 41685950](https://pubmed.ncbi.nlm.nih.gov/41685950/); [PMID: 34047380](https://pubmed.ncbi.nlm.nih.gov/34047380/))

### Quality of Life Impact

BCC can significantly impact quality of life, particularly when located in cosmetically sensitive areas (face, nose, periorbital region). Surgical treatment may result in scarring, disfigurement, and functional impairment. Advanced BCC treatment with HH inhibitors causes substantial side effects including muscle spasms, alopecia, and dysgeusia that affect daily functioning. Superficial BCCs and small nodular BCCs on the trunk have relatively minimal QOL impact.

---

## 4. Genetic/Molecular Information

### Causal Genes

| Gene | OMIM | HGNC | Role | Mutation Frequency |
|------|------|------|------|--------------------|
| **PTCH1** | 601309 | HGNC:9585 | Tumor suppressor; HH pathway receptor | ~73% of sporadic BCCs |
| **SMO** | 601500 | HGNC:11119 | Proto-oncogene; HH signal transducer | ~10–20% of sporadic BCCs |
| **TP53** | 191170 | HGNC:11998 | Tumor suppressor; genome guardian | ~50% of sporadic BCCs |
| **SUFU** | 607035 | HGNC:16466 | Negative regulator of HH pathway | Germline in some Gorlin cases |
| **PTCH2** | 603673 | HGNC:9586 | HH pathway receptor paralog | Germline in rare Gorlin cases |

*"It occurs due to a defective hedgehog cell signaling pathway, caused by heterozygous germ-line mutations in either Patched 1 (PTCH1), Suppressor of fused (SUFU), Smoothened (SMO), or Patched 2 (PTCH2) genes, leading to tumorigenesis and various developmental anomalies"* ([PMID: 41884741](https://pubmed.ncbi.nlm.nih.gov/41884741/)).

### Pathogenic Variants

- **PTCH1**: Loss-of-function mutations include nonsense, frameshift, splice-site, and missense variants. UV-signature C>T transitions are common in sporadic BCC. Somatic loss of heterozygosity (LOH) at 9q22 is frequent. In Gorlin syndrome, germline heterozygous mutations with second-hit somatic inactivation follow the Knudson two-hit model. Specific variants such as PTCH1 c.3499G>A (p.G1167R) promote proliferation and may confer resistance to vismodegib ([PMID: 37552752](https://pubmed.ncbi.nlm.nih.gov/37552752/)).
- **SMO**: Gain-of-function mutations (e.g., SMO c.2081C>G, p.P694R) constitutively activate HH signaling independent of ligand. SMO mutations are also the most common mechanism of acquired resistance to HH inhibitors ([PMID: 40522768](https://pubmed.ncbi.nlm.nih.gov/40522768/); [PMID: 37552752](https://pubmed.ncbi.nlm.nih.gov/37552752/)).
- **TP53**: UV-signature mutations, primarily somatic.
- **Classification**: Most PTCH1 mutations in sporadic BCC are somatic. Germline PTCH1 mutations in Gorlin syndrome are classified as pathogenic per ACMG/AMP guidelines in ClinVar. SMO activating variants are primarily somatic (COSMIC).

### Modifier Genes

- **MC1R**: Red hair color variants modify BCC susceptibility independent of UV response.
- **MDM2 SNP309G**: Functional polymorphism that elevates MDM2 levels, decreasing p53 activity and potentially modifying tumor phenotype ([PMID: 28925402](https://pubmed.ncbi.nlm.nih.gov/28925402/)).
- **AKT1**: Activation is obligatory for spontaneous BCC tumor growth in murine models ([PMID: 27388747](https://pubmed.ncbi.nlm.nih.gov/27388747/)).

### Epigenetic Information

Epigenetic dysregulation plays a significant role in BCC pathogenesis. Chronic UV exposure dysregulates DNA methyltransferases (DNMTs) and histone deacetylases (HDACs), creating an altered epigenomic landscape that promotes tumorigenesis ([PMID: 42074595](https://pubmed.ncbi.nlm.nih.gov/42074595/)). Key epigenetic features include:

- **DNA methylation**: Promoter hypermethylation of tumor suppressor genes
- **Histone modifications**: Altered histone acetylation patterns
- **Non-coding RNAs**: Dysregulation of long non-coding RNAs (lncRNAs), circular RNAs, and miRNAs ([PMID: 33242578](https://pubmed.ncbi.nlm.nih.gov/33242578/))
- **Chromatin remodeling**: UV-induced changes in chromatin accessibility

### Chromosomal Abnormalities

- **Loss of heterozygosity (LOH) at 9q22**: The most common chromosomal alteration, encompassing the *PTCH1* locus.
- **Additional LOH regions**: 1q, 2q, 9p, and 17p (TP53 locus).
- **Copy number alterations**: Gains at 6p and losses at 9q are recurrent.

---

## 5. Environmental Information

### Environmental Factors

- **Ultraviolet radiation**: The primary etiological agent. UVR is the dominant risk factor, recognized as a Group 1 carcinogen (IARC). Both acute intermittent (sunburn) and chronic cumulative exposure contribute. *"Ultraviolet (UV) radiation is the primary risk factor for the development of both melanocytic and nonmelanocytic skin cancer"* ([PMID: 41495244](https://pubmed.ncbi.nlm.nih.gov/41495244/)).
- **Ionizing radiation**: Therapeutic radiation exposure increases BCC risk in the irradiated field.
- **Arsenic**: Environmental contamination (drinking water) and occupational exposure.
- **Coal tar and petroleum products**: Occupational carcinogens.
- **Psoralen + UVA (PUVA)**: Phototherapy treatment for psoriasis increases risk.

### Lifestyle Factors

- **Outdoor occupation**: Outdoor workers are more likely to develop nodular BCC, but BCC onset is actually older in outdoor workers than indoor workers, suggesting other factors contribute to early-onset BCC ([PMID: 28207005](https://pubmed.ncbi.nlm.nih.gov/28207005/)).
- **Indoor tanning**: Artificial UV exposure significantly increases risk.
- **Sunscreen use**: Regular high-SPF sunscreen use is protective ([PMID: 38282244](https://pubmed.ncbi.nlm.nih.gov/38282244/)).
- **Diet**: Higher linolenic acid intake associated with BCC; higher coffee consumption protective ([PMID: 38282244](https://pubmed.ncbi.nlm.nih.gov/38282244/)).

### Infectious Agents

- BCC is not directly caused by infectious agents in most cases.
- **Human papillomavirus (HPV)**: Some studies suggest a possible cofactor role, though evidence is limited for BCC specifically. HPV has a clearer role in SCC pathogenesis.

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways

#### Hedgehog (HH) Signaling Pathway — The Central Driver

The Hedgehog pathway is the principal oncogenic driver in BCC. In normal physiology, the transmembrane receptor PTCH1 inhibits the signal transducer SMO. Binding of HH ligands (SHH, IHH, DHH) to PTCH1 relieves this inhibition, allowing SMO activation and subsequent nuclear translocation of GLI transcription factors (GLI1, GLI2, GLI3), which activate target gene expression.

**Causal chain in BCC:**
```
UV Radiation --> PTCH1 Loss-of-Function Mutation (or SMO Gain-of-Function)
    --> Constitutive SMO Activation
    --> GLI1/GLI2 Nuclear Translocation
    --> Transcription of Target Genes (CCND1, MYC, BCL2, PTCH1, GLI1)
    --> Proliferation UP, Apoptosis DOWN, Stem Cell Self-Renewal UP
    --> BCC Formation
```

**GO terms:** GO:0007224 (smoothened signaling pathway), GO:0061371 (determination of heart left/right asymmetry — embryonic HH function)

#### Wnt/Beta-Catenin Pathway

Concomitant Wnt pathway activation is required for BCC initiation. Studies demonstrate that BCC formation requires *"reprogramming of interfollicular epidermal cells to an embryonic hair follicle progenitor-like fate, with concomitant Wnt pathway activation"* ([PMID: 23196843](https://pubmed.ncbi.nlm.nih.gov/23196843/)).

**GO term:** GO:0016055 (Wnt signaling pathway)

#### p53 Pathway

TP53 mutations occur in ~50% of BCCs, contributing to impaired DNA damage response and apoptosis evasion. MDM2 overexpression further attenuates p53 activity in some cases.

**GO term:** GO:0006915 (apoptotic process)

#### PI3K/AKT/mTOR Pathway

AKT1 activation has been shown to be obligatory for spontaneous BCC tumor growth in murine models mimicking Gorlin syndrome ([PMID: 27388747](https://pubmed.ncbi.nlm.nih.gov/27388747/)).

**GO term:** GO:0043491 (protein kinase B signaling)

### Cellular Processes

- **Aberrant proliferation**: Constitutive HH signaling drives uncontrolled basal cell division (GO:0008283, cell proliferation)
- **Apoptosis resistance**: BCL2 upregulation through GLI-mediated transcription (GO:0043066, negative regulation of apoptotic process)
- **Stem cell reprogramming**: Interfollicular epidermal cells are reprogrammed to embryonic hair follicle progenitor-like cells ([PMID: 23196843](https://pubmed.ncbi.nlm.nih.gov/23196843/)) (GO:0048863, stem cell differentiation)
- **DNA damage and repair failure**: UV-induced CPDs and 6-4PPs, impaired nucleotide excision repair (GO:0006289, nucleotide-excision repair)
- **Epigenomic reprogramming**: UV-induced dysregulation of DNMTs and HDACs ([PMID: 42074595](https://pubmed.ncbi.nlm.nih.gov/42074595/))

### Cell of Origin

BCC originates from **interfollicular epidermal progenitor cells** and **hair follicle stem cells**. Lineage-tracing studies show that BCC-initiating cells are reprogrammed to hair follicle progenitor-like fate. BCC patches are more frequent, larger, and more invasive near hair follicles (HFs), and proliferation of basal epidermal cells within 60 micrometers of HF openings is elevated upon UV exposure ([PMID: 32492418](https://pubmed.ncbi.nlm.nih.gov/32492418/)). *LGR5*-expressing hair follicle stem cells and their progeny contribute to tumor development ([PMID: 28070642](https://pubmed.ncbi.nlm.nih.gov/28070642/); [PMID: 22945646](https://pubmed.ncbi.nlm.nih.gov/22945646/)).

**Cell Ontology terms:** CL:0000312 (keratinocyte), CL:0002559 (hair follicle cell), CL:0000646 (basal cell)

### Immune System Involvement

BCC is characterized by **low immunogenicity**, which contributes to immune evasion. Key features include:

- **PD-L1 expression**: Present in tumor cells and microenvironment, enabling immune checkpoint evasion
- **Tumor-infiltrating lymphocytes (TILs)**: Generally sparse in BCC compared to SCC
- **Regulatory T cells (Tregs)**: Enriched in the tumor microenvironment
- **Tumor-associated macrophages (TAMs)**: CD68+ and CD163+ macrophages in the BCC microenvironment; single-cell atlases link macrophages and CD8+ T cells to BCC biology ([PMID: 36451860](https://pubmed.ncbi.nlm.nih.gov/36451860/))
- **Myeloid-derived suppressor cells (MDSCs)**: Contribute to immunosuppressive milieu ([PMID: 39404378](https://pubmed.ncbi.nlm.nih.gov/39404378/))

### Stromal Microenvironment

The BCC stroma plays a critical role in disease behavior. Alcian blue (AB)-positive stroma — indicating mucin-rich, desmoplastic extracellular matrix remodeling — has been identified as a candidate biomarker for HH inhibitor resistance, with multivariable hazard ratio = 23.8 (95% CI: 4.02–141.3; P < 0.001) for shorter progression-free survival ([PMID: 41543881](https://pubmed.ncbi.nlm.nih.gov/41543881/)).

### Potential Prognostic Biomarkers

- **SOX2**: Expression levels as potential prognostic biomarker
- **Matrix metalloproteinases (MMPs)**: Emerging as prognostic indicators and therapeutic targets ([PMID: 39697716](https://pubmed.ncbi.nlm.nih.gov/39697716/))
- **ASIP (Agouti signaling protein)**: Mendelian randomization confirmed association with increased BCC and melanoma risk ([PMID: 39702585](https://pubmed.ncbi.nlm.nih.gov/39702585/))

---

## 7. Anatomical Structures Affected

### Organ Level

- **Primary organ**: Skin (UBERON:0002097)
- **Body system**: Integumentary system
- **Secondary involvement**: In advanced/metastatic disease — regional lymph nodes, lung, bone, liver (rare)

### Tissue and Cell Level

- **Tissue types**: Epidermis (UBERON:0001003), dermis (UBERON:0002067)
- **Specific cell populations**:
  - Basal keratinocytes (CL:0000312)
  - Hair follicle stem cells (CL:0002559)
  - Interfollicular epidermal progenitors (CL:0000646)
  - LGR5+ hair follicle stem cells
  - LGR6+ stem cells ([PMID: 28070642](https://pubmed.ncbi.nlm.nih.gov/28070642/))

### Subcellular Level

- **Nucleus**: Site of GLI transcription factor activity; DNA damage accumulation (GO:0005634)
- **Primary cilium**: Essential organelle for HH signal transduction (GO:0005929)
- **Cell membrane**: PTCH1/SMO receptor complex (GO:0005886)
- **Cytoplasm**: SMO trafficking and SUFU-GLI complex (GO:0005737)

### Localization

- **Head and neck**: ~75% of all BCCs (UBERON:0000974, neck; UBERON:0000033, head)
  - Nose: Most common site (~43%) (UBERON:0000004)
  - Cheek (~14%) (UBERON:0001567)
  - Periorbital region
  - Ears (including external auditory canal) ([PMID: 39979629](https://pubmed.ncbi.nlm.nih.gov/39979629/))
- **Trunk**: More common in indoor workers, suggesting non-UV etiological factors ([PMID: 28207005](https://pubmed.ncbi.nlm.nih.gov/28207005/))
- **Extremities**: Less common
- **Lateralization**: No consistent lateralization; distribution follows sun-exposed surfaces

---

## 8. Temporal Development

### Onset

- **Typical age of onset**: Adult to geriatric (median ~67–72 years); incidence increases sharply with age
- **Early onset**: In Gorlin syndrome (childhood/adolescence) and xeroderma pigmentosum
- **Onset pattern**: Insidious/chronic; typically grows slowly over months to years
- **Trend**: Increasing incidence in younger age groups noted ([PMID: 39422527](https://pubmed.ncbi.nlm.nih.gov/39422527/))

### Progression

- **Disease stages** (EADO staging for advanced BCC):
  - Stage I: Superficial, small, low-risk
  - Stage II: Larger, higher-risk subtypes
  - Stage III: Locally advanced (laBCC) — significant tissue invasion
  - Stage IV: Metastatic (mBCC) — extremely rare (<0.1%)

- **Progression rate**: Generally slow; infiltrative/sclerodermiform subtypes may progress more rapidly and invade deeper structures.
- **Disease course**: Progressive if untreated; does not spontaneously resolve in most cases. Chronic lifelong surveillance needed due to recurrence risk and risk of new primary tumors.
- **Advanced disease characteristics**: Median size of laBCC was 73 mm (IQR 110; range 15–400 mm), with 71% measuring 5 cm or larger; 59% showed infiltration beyond subcutaneous fat; 12% had bone infiltration ([PMID: 41039887](https://pubmed.ncbi.nlm.nih.gov/41039887/)).

### Patterns

- **Recurrence**: 44% of laBCC experienced local recurrence after resection. Median time to metastasis was 33 months ([PMID: 41039887](https://pubmed.ncbi.nlm.nih.gov/41039887/)).
- **Multiple primaries**: Patients with one BCC have ~50% chance of developing another within 5 years. Risk prediction scores can identify individuals at risk of multiple keratinocyte cancers, with top percentile DRS associated with up to 13-fold risk increase ([PMID: 33420020](https://pubmed.ncbi.nlm.nih.gov/33420020/)).
- **Critical periods**: Cumulative childhood UV exposure is a critical window; photoprotection in early life significantly reduces lifetime BCC risk.

---

## 9. Inheritance and Population

### Epidemiology

| Metric | Value | Source |
|--------|-------|--------|
| **Global incidence (>=65 years)** | 371.97 per 100,000 (95% UI: 310.75–439.58) in 2021 | [PMID: 40397469](https://pubmed.ncbi.nlm.nih.gov/40397469/) |
| **ASIR trend** | EAPC = 1.94% (1990–2021) | [PMID: 39966563](https://pubmed.ncbi.nlm.nih.gov/39966563/) |
| **Denmark BCC incidence** | 252 to 338 per 100,000 (2007–2021), age-adjusted | [PMID: 39708578](https://pubmed.ncbi.nlm.nih.gov/39708578/) |
| **Lifetime risk (white population)** | Men: 33–39%; Women: 23–28% | [PMID: 35942364](https://pubmed.ncbi.nlm.nih.gov/35942364/) |
| **Proportion of keratinocyte cancers** | ~80% | [PMID: 31585338](https://pubmed.ncbi.nlm.nih.gov/31585338/) |

### Genetic Etiology

- **Sporadic BCC**: Multifactorial/polygenic inheritance with strong environmental contribution
- **Gorlin syndrome**: Autosomal dominant, complete penetrance, variable expressivity ([PMID: 41884741](https://pubmed.ncbi.nlm.nih.gov/41884741/))
- **Polygenic risk scores**: PRS associated with ~3-fold increases in BCC risk; BCC genetic susceptibility also accelerates skin aging by 0.88 years perceived age increase per genetic risk score unit ([PMID: 31419349](https://pubmed.ncbi.nlm.nih.gov/31419349/); [PMID: 30908599](https://pubmed.ncbi.nlm.nih.gov/30908599/))

### Population Demographics

- **Most affected populations**: Fair-skinned Caucasians (Fitzpatrick skin types I–II); particularly prevalent in Australia, Northern Europe, and North America
- **Sex ratio**: Male predominance; males > females (~1.5:1 to 2:1)
- **Ethnic variation**: Significantly lower incidence in people of color; in non-white SOTRs, BCC occurs in 46.9% of skin cancer cases ([PMID: 37788820](https://pubmed.ncbi.nlm.nih.gov/37788820/))
- **Geographic distribution**: Higher incidence at lower latitudes (greater UV exposure); highest rates in Australia; burden disproportionately higher in countries with higher sociodemographic index ([PMID: 40397469](https://pubmed.ncbi.nlm.nih.gov/40397469/))
- **Age distribution**: Sharply increasing incidence after age 50; global burden greatest in adults >=65 years; population growth is the primary driver of increasing burden ([PMID: 40397469](https://pubmed.ncbi.nlm.nih.gov/40397469/))

---

## 10. Diagnostics

### Clinical Examination and Dermoscopy

- **Clinical diagnosis**: Based on characteristic morphology — pearly, translucent papule/nodule with telangiectasias on sun-exposed skin
- **Dermoscopy**: Essential tool for BCC diagnosis. Sensitivity 97.1% (95% CI: 91.80–99.40) and specificity 78.95% (95% CI: 54.43–93.95) for BCC detection using reflectance confocal microscopy ([PMID: 30987174](https://pubmed.ncbi.nlm.nih.gov/30987174/)). Integration of dermoscopy and RCM improves diagnostic accuracy, with AUC reaching 0.899 for superficial BCC ([PMID: 41685950](https://pubmed.ncbi.nlm.nih.gov/41685950/)).

### Imaging Studies

- **Line-field confocal OCT (LC-OCT)**: Overall BCC subtype agreement with histology was 90.4% (95% CI: 79.0–96.8) ([PMID: 34047380](https://pubmed.ncbi.nlm.nih.gov/34047380/))
- **Reflectance confocal microscopy (RCM)**: Non-invasive in vivo imaging with high sensitivity for BCC detection
- **Hyperspectral imaging (HSI)**: Emerging computer-aided detection method ([PMID: 38067338](https://pubmed.ncbi.nlm.nih.gov/38067338/))
- **CT/MRI**: For advanced BCC to assess extent of invasion, perineural spread, or metastasis

### Biopsy and Histopathology

- **Biopsy**: Mandatory for histological confirmation, especially in ambiguous lesions and high-risk areas ([PMID: 31288208](https://pubmed.ncbi.nlm.nih.gov/31288208/))
- **Histopathological features**: Basaloid cell nests with peripheral palisading, retraction artifact (clefting), mucinous stroma
- **Immunohistochemistry**: BerEP4 positive, BCL2 positive, CK5/6 positive; helps differentiate from SCC and trichoepithelioma
- **Subtyping**: Critical for treatment planning — nodular, superficial, infiltrative/morpheaform, basosquamous

### Genetic Testing

- **Gorlin syndrome**: Panel testing for *PTCH1*, *PTCH2*, *SMO*, and *SUFU* recommended for patients presenting with multiple BCCs at young age or syndromic features ([PMID: 39581763](https://pubmed.ncbi.nlm.nih.gov/39581763/))
- **Sporadic BCC**: Genetic testing not routinely performed; molecular profiling may guide therapy in advanced cases resistant to HH inhibitors
- **Tumor molecular profiling**: Useful for identifying resistance mechanisms (SMO mutations, GLI amplification) in HHI-resistant cases ([PMID: 41515948](https://pubmed.ncbi.nlm.nih.gov/41515948/); [PMID: 40522768](https://pubmed.ncbi.nlm.nih.gov/40522768/))

### Artificial Intelligence

AI-based diagnostic tools are being developed for BCC detection in dermoscopy, OCT, and RCM images, showing promising results for automated detection and classification ([PMID: 36785993](https://pubmed.ncbi.nlm.nih.gov/36785993/); [PMID: 40370729](https://pubmed.ncbi.nlm.nih.gov/40370729/)).

### Differential Diagnosis

| Condition | Distinguishing Features |
|-----------|------------------------|
| Squamous cell carcinoma | Keratinization, more infiltrative, higher metastatic potential |
| Trichoepithelioma | Benign; LGR6+ stromal cells present (absent in BCC) |
| Melanoma (amelanotic) | S100/Melan-A positive; lacks palisading |
| Sebaceous hyperplasia | Central umbilication, yellowish color |
| Dermatofibroma | Firm papule, dimple sign |
| Merkel cell carcinoma | Rapidly growing, violaceous nodule |

### Screening

- **Full-body skin examination**: Recommended for high-risk individuals (fair skin, history of skin cancer, immunosuppression)
- **SCREEN clinic model**: Integrated skin cancer screening in transplant clinics identifies at-risk patients ([PMID: 27663613](https://pubmed.ncbi.nlm.nih.gov/27663613/))
- **No population-wide newborn or genetic screening** for sporadic BCC

---

## 11. Outcome/Prognosis

### Survival and Mortality

| Stage | 5-Year Disease-Specific Survival | Source |
|-------|----------------------------------|--------|
| **Early/localized BCC** | >95–99% | Multiple sources |
| **Locally advanced BCC** | 79% | [PMID: 41039887](https://pubmed.ncbi.nlm.nih.gov/41039887/) |
| **Metastatic BCC** | 30% | [PMID: 41039887](https://pubmed.ncbi.nlm.nih.gov/41039887/) |

- **Mortality**: Very low overall; death is uncommon and decreasing due to earlier diagnosis ([PMID: 35942364](https://pubmed.ncbi.nlm.nih.gov/35942364/)). In one 32-year single-center study, 12% of patients with laBCC died of their disease ([PMID: 41039887](https://pubmed.ncbi.nlm.nih.gov/41039887/)).

### Morbidity

- **Local tissue destruction**: Untreated BCC can cause significant cosmetic and functional impairment
- **Treatment morbidity**: Surgical scarring, HHI side effects (muscle spasms, alopecia, dysgeusia)
- **Multiple BCCs**: Patients are at substantial risk of developing subsequent primary BCCs; high DRSA scores associated with earlier diagnosis by up to 14 years and more recurrent forms ([PMID: 33420020](https://pubmed.ncbi.nlm.nih.gov/33420020/))

### Prognostic Factors

- **Tumor subtype**: Infiltrative/morpheaform and basosquamous subtypes carry higher recurrence and metastatic risk
- **Tumor size**: Larger tumors have worse outcomes
- **Location**: Head/neck tumors, particularly periorbital and nasal, carry higher surgical complexity
- **Perineural/perivascular invasion**: Associated with higher recurrence and metastatic risk
- **Immunosuppression status**: Transplant recipients have higher recurrence and more aggressive disease
- **Alcian blue-positive stroma**: Candidate biomarker for HHI resistance (HR = 23.8) ([PMID: 41543881](https://pubmed.ncbi.nlm.nih.gov/41543881/))
- **ECOG performance status**: Significant predictor of overall survival in vismodegib-treated patients ([PMID: 41053641](https://pubmed.ncbi.nlm.nih.gov/41053641/))

---

## 12. Treatment

### Surgical Treatment (MAXO:0000004 — surgical procedure)

#### Mohs Micrographic Surgery (Gold Standard for High-Risk BCC)
- **5-year recurrence rate**: 3.8% overall (95% CI: 2.8–5.0); 3.1% for primary BCC; 5.3% for recurrent BCC — from a Danish nationwide cohort of 2,203 patients ([PMID: 39791512](https://pubmed.ncbi.nlm.nih.gov/39791512/))
- **Cure rates**: Up to 99–100% reported ([PMID: 40167057](https://pubmed.ncbi.nlm.nih.gov/40167057/))
- **Indications**: High-risk BCC, recurrent BCC, cosmetically sensitive areas

#### Standard Surgical Excision
- First-line for most "easy-to-treat" BCCs
- Complete excision with histologically confirmed margins
- **MAXO:0000601** — wide excision

#### Other Destructive Techniques
- **Electrodesiccation and curettage**: For low-risk, superficial BCC
- **Cryotherapy**: For low-risk superficial BCC
- **Laser ablation**: Select superficial cases

### Pharmacotherapy

#### Hedgehog Pathway Inhibitors (MAXO:0001298 — targeted therapy)

| Drug | Indication | ORR | CR | Key Side Effects |
|------|-----------|-----|-----|-----------------|
| **Vismodegib** | laBCC, mBCC | 65% (real-world) | 28% | Muscle spasms, alopecia, dysgeusia |
| **Sonidegib** | laBCC | 89% (real-world) | 37% | Muscle spasms, alopecia, dysgeusia |

*"Updated evidence confirms Hedgehog pathway inhibitors (HHIs) as the standard first-line therapy for advanced BCC, while programmed death-1 (PD-1) blockade with cemiplimab has established durable responses after HHI failure"* ([PMID: 41703999](https://pubmed.ncbi.nlm.nih.gov/41703999/)).

Vismodegib median PFS was 15.1 months and median OS was 37.5 months in a facial laBCC cohort ([PMID: 41053641](https://pubmed.ncbi.nlm.nih.gov/41053641/)). Sonidegib showed superior real-world efficacy compared to pivotal trial data (ORR 89% vs. 60.6%) ([PMID: 40834113](https://pubmed.ncbi.nlm.nih.gov/40834113/)). Sequential HHI therapy (switching from vismodegib to sonidegib) achieved ORR of 71% with CR of 43% ([PMID: 40834113](https://pubmed.ncbi.nlm.nih.gov/40834113/)).

**Resistance mechanisms**: Mutations in SMO (drug-binding site alterations), GLI2 amplification, activation of alternative pathways (PI3K/AKT). SMO c.2081C>G (p.P694R) may confer resistance to vismodegib but sensitivity to downstream inhibitor GANT61 ([PMID: 37552752](https://pubmed.ncbi.nlm.nih.gov/37552752/)).

#### Immunotherapy (MAXO:0000750 — immunotherapy)

- **Cemiplimab (anti-PD-1)**: FDA-approved for patients with laBCC or mBCC who have progressed on or are intolerant to HHI therapy. *"Cemiplimab is the first immune checkpoint inhibitor (ICI) approved by the Food and Drug Administration for refractory BCC, marking a major breakthrough in BCC immunotherapy"* ([PMID: 39697716](https://pubmed.ncbi.nlm.nih.gov/39697716/)). Response rate ~21% in mBCC, with durable disease control ([PMID: 40432222](https://pubmed.ncbi.nlm.nih.gov/40432222/)).
- **Combination therapy**: Cemiplimab + vismodegib shows promise — a case report demonstrated pathologic complete response with combination neoadjuvant therapy ([PMID: 39949752](https://pubmed.ncbi.nlm.nih.gov/39949752/)).

#### Topical Therapies (MAXO:0001058 — topical medication)

*"For the treatment of superficial BCC, complete clearance rates ranged from 90 to 93% for 5% 5-fluorouracil (5-FU) and 71 to 76% for imiquimod (IMQ)"* ([PMID: 36169917](https://pubmed.ncbi.nlm.nih.gov/36169917/)).

| Agent | Indication | Clearance Rate |
|-------|-----------|---------------|
| **5-Fluorouracil 5%** | Superficial BCC | 90–93% |
| **Imiquimod 5%** | Superficial BCC | 71–76% |
| **Imiquimod 5%** | Giant superficial BCC | Effective (case series) |

#### Photodynamic Therapy (MAXO:0000940)

Effective for superficial BCC and thin nodular BCC. PDT combined with Mohs surgery may offer advantages for non-aggressive laBCC subtypes ([PMID: 40449860](https://pubmed.ncbi.nlm.nih.gov/40449860/)).

#### Radiation Therapy (MAXO:0000014 — radiation therapy)

- **Superficial radiation therapy (SRT)**: IGSRT showed 2-year freedom from recurrence of 99.23% across all NMSC types; BCC recurrence 1.1% ([PMID: 39777366](https://pubmed.ncbi.nlm.nih.gov/39777366/))
- **Surface mold brachytherapy**: Effective alternative for inoperable patients ([PMID: 39719956](https://pubmed.ncbi.nlm.nih.gov/39719956/))
- Valid alternative to surgery for facial BCC in elderly patients ([PMID: 31288208](https://pubmed.ncbi.nlm.nih.gov/31288208/))

### Neoadjuvant Approaches

HHI neoadjuvant therapy before surgery is emerging as a strategy to reduce tumor burden before definitive excision, particularly in cosmetically sensitive areas ([PMID: 40043261](https://pubmed.ncbi.nlm.nih.gov/40043261/); [PMID: 40559089](https://pubmed.ncbi.nlm.nih.gov/40559089/)).

### Treatment Algorithm

```
BCC Diagnosis
|-- Low-risk / "Easy-to-treat"
|   |-- Superficial --> Topical (5-FU, imiquimod), PDT, or surgery
|   +-- Nodular --> Surgical excision +/- Mohs
|-- High-risk / "Difficult-to-treat"
|   |-- Recurrent / cosmetically sensitive --> Mohs micrographic surgery
|   +-- Locally advanced (laBCC)
|       |-- Resectable --> Neoadjuvant HHI --> Surgery
|       +-- Unresectable --> HHI (vismodegib/sonidegib)
|           |-- Response --> Continue / Surgery
|           +-- Progression/Intolerance --> Cemiplimab (anti-PD-1)
|               +-- Progression --> Clinical trials / Combination therapy
+-- Metastatic (mBCC) --> HHI --> Cemiplimab --> Clinical trials
```

---

## 13. Prevention

### Primary Prevention

- **UV avoidance**: Limiting sun exposure, especially during peak hours (10 AM–4 PM)
- **Sunscreen**: Regular use of broad-spectrum SPF 30+ sunscreen; higher SPF use associated with reduced risk ([PMID: 38282244](https://pubmed.ncbi.nlm.nih.gov/38282244/))
- **Protective clothing**: Hats, long sleeves, UV-protective textiles; particularly important in resource-limited settings ([PMID: 38672604](https://pubmed.ncbi.nlm.nih.gov/38672604/))
- **Avoidance of indoor tanning**: Critical public health measure
- **Topical DNA repair enzymes**: Photolyase-containing sunscreens reduced BCC incidence by 56% in XP patients ([PMID: 25408650](https://pubmed.ncbi.nlm.nih.gov/25408650/))
- **Public health education**: Skin Cancer Awareness Month (May) shows seasonal increases in search interest; targeted campaigns needed for communities of color ([PMID: 38643380](https://pubmed.ncbi.nlm.nih.gov/38643380/); [PMID: 24485530](https://pubmed.ncbi.nlm.nih.gov/24485530/))

**MAXO:0000150** — sun protective behavior counseling

### Secondary Prevention

- **Full-body skin examination**: Regular dermatological screening for high-risk individuals
- **Dermoscopy-assisted screening**: Improves accuracy of BCC subtype identification, particularly for superficial BCC ([PMID: 26921200](https://pubmed.ncbi.nlm.nih.gov/26921200/))
- **Integrated transplant screening clinics**: SCREEN clinic model for organ transplant recipients ([PMID: 27663613](https://pubmed.ncbi.nlm.nih.gov/27663613/))
- **Disease risk scores**: Polygenic risk scores can identify high-risk individuals and predict when they are likely to develop skin cancer, with high scores associated with earlier diagnosis by up to 14 years ([PMID: 33420020](https://pubmed.ncbi.nlm.nih.gov/33420020/))

### Tertiary Prevention

- **Long-term follow-up**: Recommended for all patients with BCC, especially high-risk subtypes
- **Surveillance protocols**: Close monitoring for Gorlin syndrome patients to diagnose and treat BCCs at early stage ([PMID: 31288208](https://pubmed.ncbi.nlm.nih.gov/31288208/))
- **Immunosuppression management**: Switching from calcineurin inhibitors to mTOR inhibitors in transplant recipients may reduce NMSC incidence ([PMID: 37887285](https://pubmed.ncbi.nlm.nih.gov/37887285/))

### Genetic Counseling

- Recommended for patients with multiple BCCs at young age or features suggesting Gorlin syndrome
- Family screening for *PTCH1* mutations in confirmed Gorlin kindreds
- Prenatal testing available for known pathogenic variants

---

## 14. Other Species / Natural Disease

### Taxonomy of Affected Species

BCC and BCC-like tumors have been documented in several species:

- **Mus musculus** (mouse; NCBI Taxon: 10090): Primary model organism for BCC research
- **Rattus norvegicus** (rat; NCBI Taxon: 10116): Less commonly used
- **Felis catus** (domestic cat): Rare spontaneous BCC reported
- **Canis lupus familiaris** (domestic dog): Rare basal cell tumors (generally more benign than human BCC)
- **Equus caballus** (horse): Occasionally reported

### Orthologous Genes

| Human Gene | Mouse Ortholog | NCBI Gene ID (Mouse) |
|-----------|---------------|----------------------|
| *PTCH1* | *Ptch1* | 19206 |
| *SMO* | *Smo* | 319757 |
| *SUFU* | *Sufu* | 24069 |
| *GLI1* | *Gli1* | 14632 |
| *GLI2* | *Gli2* | 14633 |

### Comparative Biology

The Hedgehog signaling pathway is highly conserved across vertebrates. Ptch1+/- heterozygous knockout mice develop mandibular cysts that histologically resemble keratocystic odontogenic tumors of Gorlin syndrome, with parakeratotic stratified squamous epithelium and keratinized contents ([PMID: 12542834](https://pubmed.ncbi.nlm.nih.gov/12542834/)). The conservation of HH pathway components across species validates the use of animal models for studying BCC biology and testing therapeutics.

---

## 15. Model Organisms

### Mouse Models

#### Ptch1+/- Heterozygous Knockout Mouse
- **Type**: Genetically engineered (knockout)
- **Background**: Mimics Gorlin syndrome with heterozygous Ptch1 inactivation
- **Phenotype recapitulation**: Develops medulloblastoma, rhabdomyosarcoma, and mandibular cysts; BCC development requires additional stimuli (UV or chemical carcinogenesis)
- **Mandibular cysts**: Found in 25.4% of Ptch1+/- mice, lined by thin parakeratotic squamous epithelium resembling keratocystic odontogenic tumors of Gorlin syndrome ([PMID: 12542834](https://pubmed.ncbi.nlm.nih.gov/12542834/))

#### SKH1-Ptch1+/- Mouse (UV-Inducible BCC Model)
- **Type**: Conditional/hairless variant
- **Features**: AKT1 activation is obligatory for spontaneous BCC growth; vismodegib can ablate tumors but they recur upon drug discontinuation ([PMID: 27388747](https://pubmed.ncbi.nlm.nih.gov/27388747/))

#### Ptch(flox/flox)CD4Cre+/- Mouse
- **Type**: Conditional knockout
- **Key finding**: Biallelic loss of Ptch in CD4+ cells does not suffice for BCC formation alone; a second stimulus (DMBA/TPA) is required. BCCs originate from rare Ptch-deficient stem cell-like cells expressing CD4 ([PMID: 24662765](https://pubmed.ncbi.nlm.nih.gov/24662765/))

#### UV-Inducible Murine BCC Model (Multicolor Lineage Tracing)
- **Key finding**: BCC patches are more frequent, larger, and more invasive near hair follicles. Chronic UV irradiation promotes proliferation of basal epidermal cells within 60 micrometers of HF openings ([PMID: 32492418](https://pubmed.ncbi.nlm.nih.gov/32492418/))

### Model Limitations

- Mouse skin differs from human skin in thickness, hair cycling, and immune composition
- Ptch1+/- mice more commonly develop medulloblastoma than BCC without additional stimuli
- UV-induced murine BCCs may not fully recapitulate the mutational spectrum of human BCCs
- Drug metabolism differences between mice and humans affect pharmacokinetic modeling
- Immune microenvironment differs between species

### Model Resources

- **Mouse Genome Informatics (MGI)**: Comprehensive Ptch1 allele database
- **International Mouse Phenotyping Consortium (IMPC)**: Ptch1 knockout phenotyping data
- **Jackson Laboratory (JAX)**: Repository for BCC-relevant mouse strains
- **IMSR (International Mouse Strain Resource)**: Strain availability database

---

## Key Findings — Detailed Evidence

### Finding 1: BCC is the Most Common Human Malignancy Driven by Hedgehog Pathway Dysregulation

BCC accounts for approximately 80% of all keratinocyte cancers and is the single most common cancer in fair-skinned populations. The disease is driven in virtually all cases by constitutive activation of the Hedgehog signaling pathway, predominantly through loss-of-function mutations in *PTCH1* or gain-of-function mutations in *SMO*. The global burden is substantial and rising — the age-standardized incidence rate in adults >=65 was 371.97 per 100,000 (95% UI: 310.75–439.58) in 2021, with an EAPC of 1.94% from 1990 to 2021. In Denmark alone, 183,338 first-time BCC cases were recorded from 2007 to 2021, with age-adjusted incidence rising from 252 to 338 per 100,000.

### Finding 2: Gorlin Syndrome Demonstrates Germline Hedgehog Pathway Mutations Cause Hereditary BCC

Gorlin-Goltz syndrome (BCNS) provides the genetic proof-of-concept that Hedgehog pathway mutations are causal for BCC. This autosomal dominant syndrome with complete penetrance and variable expression is caused by heterozygous germline mutations in *PTCH1*, *SUFU*, *SMO*, or *PTCH2*. Affected individuals develop multiple BCCs at a young age alongside palmoplantar pits, keratocystic odontogenic tumors, intracranial calcifications, and skeletal anomalies. Patients with SHH-subgroup medulloblastoma should undergo routine genetic testing for Gorlin-associated mutations, as early identification changes management — notably, whole craniospinal irradiation should be avoided due to risk of radiation-induced BCCs ([PMID: 32930885](https://pubmed.ncbi.nlm.nih.gov/32930885/)).

### Finding 3: Comprehensive Treatment Paradigm — Surgery, HH Inhibitors, Immunotherapy, and Topical Therapies

The treatment landscape for BCC is well-defined and expanding. Mohs micrographic surgery remains the gold standard for high-risk BCC with a 5-year recurrence rate of 3.8% (nationwide Danish cohort). For locally advanced disease, HH inhibitors provide high response rates — vismodegib ORR 65% with 28% CR; sonidegib ORR 89% with 37% CR in real-world settings. Cemiplimab has emerged as a transformative option after HHI failure, providing durable responses. Topical therapies (5-FU 90–93% clearance; imiquimod 71–76% clearance) remain effective for superficial BCC.

### Finding 4: UV Radiation is the Dominant Environmental Risk Factor Through DNA Damage and Epigenomic Reprogramming

Ultraviolet radiation is the primary environmental driver of BCC through a dual mechanism of direct DNA damage (UV-signature mutations in *PTCH1*, *TP53*) and chronic dysregulation of epigenetic machinery (DNMTs, HDACs). The interplay between UVR, UV-sensitive phenotype, and genotype is central to BCC etiopathogenesis. Immunosuppression dramatically amplifies risk — stem cell transplant recipients have a 7.21-fold increased skin cancer risk. GWAS have identified multiple susceptibility loci in pigmentation genes that modify UV sensitivity and BCC risk.

---

## Mechanistic Model

The pathogenesis of BCC can be understood as a multi-step process with converging genetic and environmental inputs:

```
INITIATION
===========
  Chronic UV Exposure (UVB > UVA)
      |
      v
  DNA Damage: CPDs, 6-4PPs, oxidative lesions
      |
      +---> UV-signature mutations (C>T, CC>TT)
      |         |
      |         +---> PTCH1 loss-of-function (~73%)
      |         +---> TP53 inactivation (~50%)
      |         +---> SMO gain-of-function (~10-20%)
      |
      +---> Epigenomic Reprogramming
                |
                +---> DNMT/HDAC dysregulation
                +---> Promoter methylation changes
                +---> ncRNA dysregulation

PROMOTION
==========
  Constitutive HH Pathway Activation
      |
      v
  SMO Activation --> GLI1/GLI2 Nuclear Translocation
      |
      +---> Target gene transcription: CCND1, MYC, BCL2
      +---> Wnt pathway co-activation (required)
      +---> Stem cell reprogramming to HF progenitor fate
      |
  AKT/PI3K Pathway Activation (required for growth)
      |
      v
  Cell Proliferation UP + Apoptosis DOWN

PROGRESSION
============
  Clonal Expansion from Hair Follicle-Proximal Stem Cells
      |
      +---> Nodular BCC (most common)
      +---> Superficial BCC
      +---> Infiltrative/Morpheaform BCC (desmoplastic stroma)
      +---> Basosquamous BCC (mixed differentiation)
      |
  Immune Evasion (PD-L1, Tregs, TAMs, low TILs)
      |
      v
  Locally Advanced BCC (rare: Metastatic BCC)
```

---

## Evidence Base

### Landmark References

| PMID | Title/Topic | Key Contribution |
|------|------------|-----------------|
| [41240053](https://pubmed.ncbi.nlm.nih.gov/41240053/) | BCC precursor lesion | Established that nearly all BCCs are driven by HH pathway mutations |
| [28220485](https://pubmed.ncbi.nlm.nih.gov/28220485/) | Epidemiology review | Confirmed BCC as most common cancer in white-skinned individuals |
| [41884741](https://pubmed.ncbi.nlm.nih.gov/41884741/) | Gorlin-Goltz syndrome genetics | Comprehensive description of BCNS genetics and features |
| [41703999](https://pubmed.ncbi.nlm.nih.gov/41703999/) | Evolving BCC treatment paradigms | Established current HHI to PD-1 treatment algorithm |
| [39791512](https://pubmed.ncbi.nlm.nih.gov/39791512/) | Mohs surgery nationwide cohort | Definitive recurrence data from Danish national registry |
| [42074595](https://pubmed.ncbi.nlm.nih.gov/42074595/) | Epigenetic landscape of NMSC | Linked UV to epigenomic reprogramming via DNMT/HDAC dysregulation |
| [40397469](https://pubmed.ncbi.nlm.nih.gov/40397469/) | Burden of skin cancer in older adults | Comprehensive global burden data and projections to 2050 |
| [36169917](https://pubmed.ncbi.nlm.nih.gov/36169917/) | Topical treatment advances | Clearance rates for 5-FU and imiquimod in superficial BCC |
| [38987869](https://pubmed.ncbi.nlm.nih.gov/38987869/) | Skin cancer post-HSCT meta-analysis | Quantified immunosuppression as risk factor (SIR = 7.21) |
| [41543881](https://pubmed.ncbi.nlm.nih.gov/41543881/) | AB-positive stroma and HHI resistance | Novel prognostic biomarker for HHI treatment outcome |
| [23196843](https://pubmed.ncbi.nlm.nih.gov/23196843/) | Stem cell reprogramming in BCC | Established Wnt co-activation and HF progenitor reprogramming |
| [32492418](https://pubmed.ncbi.nlm.nih.gov/32492418/) | UV and hair follicle-proximal carcinogenesis | BCC preferentially initiates near hair follicles |
| [21700618](https://pubmed.ncbi.nlm.nih.gov/21700618/) | GWAS for BCC and SCC | Identified MC1R, 6p25, and 13q32 susceptibility loci |
| [31288208](https://pubmed.ncbi.nlm.nih.gov/31288208/) | European BCC guidelines | Consensus diagnostic and treatment recommendations |
| [33420020](https://pubmed.ncbi.nlm.nih.gov/33420020/) | Disease risk scores for skin cancers | PRS predict BCC risk and timing of onset |

---

## Limitations and Knowledge Gaps

1. **Incomplete epidemiological data**: BCC is often not reported to cancer registries, making true global incidence difficult to ascertain. The GBD data may underestimate the burden.

2. **Limited data in non-white populations**: Most BCC research focuses on Caucasian populations. Characterization in people of color, where BCC presents differently and may be diagnosed later, remains insufficient ([PMID: 37788820](https://pubmed.ncbi.nlm.nih.gov/37788820/); [PMID: 24485530](https://pubmed.ncbi.nlm.nih.gov/24485530/)).

3. **Biomarker validation**: Promising biomarkers such as AB-positive stroma, SOX2, and MMPs require prospective validation in larger cohorts.

4. **HHI resistance mechanisms**: While SMO mutations are the best-characterized resistance mechanism, the full landscape of resistance pathways (including non-HH pathway activation) remains incompletely understood.

5. **Optimal combination therapy**: The sequencing and combination of HH inhibitors with immunotherapy is being explored but lacks phase III trial data.

6. **Prevention in high-risk populations**: Optimal prevention strategies for transplant recipients and Gorlin syndrome patients need further refinement.

7. **Epigenetic mechanisms**: While UV-induced epigenomic reprogramming is established, specific therapeutic targeting of epigenetic alterations in BCC remains in preclinical stages.

8. **Single-cell and spatial profiling**: The cellular heterogeneity of BCC and its microenvironment, particularly regarding therapy resistance, requires further characterization with modern single-cell and spatial transcriptomic approaches.

---

## Proposed Follow-up Experiments/Actions

1. **Prospective biomarker validation study**: Validate AB-positive stroma as a predictive biomarker for HHI resistance in a multicenter prospective cohort, potentially enabling treatment stratification before initiating systemic therapy.

2. **Combination therapy clinical trials**: Design randomized trials of cemiplimab + vismodegib/sonidegib versus sequential therapy for laBCC to determine optimal treatment strategy for advanced disease.

3. **Single-cell atlas of BCC subtypes**: Comprehensive single-cell RNA-seq profiling of nodular, superficial, infiltrative, and basosquamous BCC subtypes to characterize cellular heterogeneity, immune microenvironment, and identify subtype-specific therapeutic vulnerabilities.

4. **Epigenetic therapeutic targeting**: Preclinical and early-phase clinical studies of DNMT inhibitors and HDAC inhibitors in BCC, particularly in combination with HHI therapy to address resistance.

5. **Polygenic risk score implementation study**: Clinical validation trial evaluating whether incorporation of BCC PRS into primary care screening protocols improves early detection rates and reduces advanced-stage presentation.

6. **Non-white population epidemiology**: Large prospective cohort studies of BCC incidence, characteristics, and outcomes in diverse populations to address existing data gaps.

7. **CRISPR functional genomics**: Systematic CRISPR screens in BCC cell lines and organoids to identify synthetic lethal interactions with HH pathway activation, potentially revealing new therapeutic targets for HHI-resistant disease.

8. **Liquid biopsy development**: Development and validation of circulating tumor DNA (ctDNA) assays for monitoring treatment response and detecting early recurrence in advanced BCC.

---

## Ontology Summary

### Key Ontology Terms for Knowledge Base Entry

| Category | Term | ID |
|----------|------|----|
| **Disease** | Basal cell carcinoma | MONDO:0004972 |
| **Phenotype** | Basal cell carcinoma | HP:0002671 |
| **Phenotype** | Multiple basal cell carcinomas | HP:0007565 |
| **Gene** | PTCH1 | HGNC:9585 |
| **Gene** | SMO | HGNC:11119 |
| **Gene** | TP53 | HGNC:11998 |
| **Gene** | MC1R | HGNC:6929 |
| **Gene** | SUFU | HGNC:16466 |
| **Biological Process** | Smoothened signaling pathway | GO:0007224 |
| **Biological Process** | Wnt signaling pathway | GO:0016055 |
| **Biological Process** | Apoptotic process | GO:0006915 |
| **Biological Process** | Cell proliferation | GO:0008283 |
| **Cellular Component** | Primary cilium | GO:0005929 |
| **Cell Type** | Keratinocyte | CL:0000312 |
| **Cell Type** | Basal cell of epidermis | CL:0000646 |
| **Cell Type** | Hair follicle cell | CL:0002559 |
| **Anatomy** | Skin of body | UBERON:0002097 |
| **Anatomy** | Epidermis | UBERON:0001003 |
| **Anatomy** | External nose | UBERON:0000004 |
| **Anatomy** | Head | UBERON:0000033 |
| **Chemical** | Vismodegib | CHEBI:66903 |
| **Chemical** | 5-Fluorouracil | CHEBI:46345 |
| **Treatment** | Surgical procedure | MAXO:0000004 |
| **Treatment** | Targeted therapy | MAXO:0001298 |
| **Treatment** | Immunotherapy | MAXO:0000750 |
| **Treatment** | Radiation therapy | MAXO:0000014 |
| **Treatment** | Sun protective counseling | MAXO:0000150 |

---

*Report generated: 2026-05-05 | Based on systematic review of 100 primary literature sources | All citations verified against PubMed abstracts*
