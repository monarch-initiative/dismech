---
provider: perplexity
model: sonar-deep-research
cached: false
start_time: '2026-08-14T13:09:18.329730'
end_time: '2026-08-14T13:13:29.717590'
duration_seconds: 251.39
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hodgkin Lymphoma
  mondo_id: ''
  category: Cancer
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    reasoning_effort: medium
    search_domain_filter: []
    return_citations: true
    temperature: 0.0
citation_count: 21
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hodgkin Lymphoma
- **MONDO ID:**  (if available)
- **Category:** Cancer

## Research Objectives

Please provide a comprehensive research report on **Hodgkin Lymphoma** covering all of the
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

# Comprehensive Disease Characteristics of Hodgkin Lymphoma

Hodgkin lymphoma is a rare B‑cell–derived malignant lymphoma characterized by the presence of neoplastic Hodgkin and Reed–Sternberg (HRS) cells or lymphocyte predominant (LP) cells within a rich but dysregulated inflammatory microenvironment.[2][3][8][15] It accounts for a small fraction of all cancers, with an age‑adjusted incidence of approximately 2.5 new cases per 100,000 men and women per year in the United States and an estimated 8,720 new cases and 1,150 deaths in 2025.[6] Clinically, Hodgkin lymphoma presents most commonly with painless lymphadenopathy, systemic “B symptoms” such as fever, night sweats, and weight loss, and characteristic histopathological patterns that distinguish classical Hodgkin lymphoma (cHL) from nodular lymphocyte predominant Hodgkin lymphoma (NLPHL).[2][3][8][15] Its etiology is multifactorial: up to 40% of cases are associated with Epstein–Barr virus (EBV) infection, and almost all cHL tumors carry somatic lesions converging on constitutive JAK–STAT and NF‑κB pathway activation and immune‑evasion mechanisms such as 9p24.1 amplification of PD‑L1/PD‑L2 and JAK2.[7][11][12] Prognosis is generally favorable, with modern combined‑modality therapy achieving long‑term cure in the majority of patients and five‑year relative survival exceeding 85–90%,[6] but survivors face risks of relapse, late effects, and second malignancies, particularly after high‑dose chemotherapy and autologous hematopoietic cell transplantation (auto‑HCT).[17] Recent advances include response‑adapted therapy guided by FDG PET/CT using the Deauville score,[16] and highly effective PD‑1 checkpoint blockade with nivolumab and pembrolizumab in relapsed/refractory cHL, which leverages the disease’s characteristic PD‑1 ligand overexpression to induce durable responses in heavily pretreated patients.[12][18][19] Together, Hodgkin lymphoma represents a paradigmatic immunogenic and genetically complex cancer, whose study has illuminated general principles of lymphomagenesis, tumor–microenvironment crosstalk, and immunotherapy.

---

## 1. Disease Information

### 1.1 Definition and Clinical Overview

Hodgkin lymphoma is a malignant neoplasm of lymphoid tissue defined by the World Health Organization (WHO) as a B‑cell–derived lymphoma characterized by a minority population of neoplastic cells in an extensive but reactive background of non‑neoplastic immune cells.[2][3][8][15] Classical Hodgkin lymphoma, the predominant subtype, is distinguished histologically by HRS cells—large, often binucleated or multinucleated cells with prominent eosinophilic nucleoli—embedded in a polymorphous infiltrate of lymphocytes, eosinophils, histiocytes, plasma cells, and fibroblasts.[8] Nodular lymphocyte predominant Hodgkin lymphoma, by contrast, is defined by scattered LP (“popcorn”) cells within nodular aggregates of small B lymphocytes and T follicular helper (TFH) cells, a microenvironmental composition that preserves a more typical B‑cell phenotype.[9][15] Clinically, patients most often present with painless enlargement of peripheral lymph nodes, particularly in the cervical, mediastinal, and axillary regions, sometimes accompanied by constitutional B symptoms and pruritus.[2][9]

Orphanet describes Hodgkin lymphoma as an uncommon cancer with an incidence of about 1 per 40,000 in North America and Europe and about 8,500 new cases reported annually in the United States, noting its classification into cHL and NLPHL and emphasizing its multifactorial etiology involving immunological, genetic, and environmental factors.[2] SEER data emphasize that Hodgkin lymphoma is rare compared with other malignancies, representing about 0.4% of all new cancer cases and 0.2% of all cancer deaths in the U.S.[6] The disease exhibits a characteristic bimodal age distribution, with peaks in adolescence/young adulthood and later adulthood, and a slight male predominance, though the relative frequencies of subtypes and EBV association vary by age and geography.[2][6][7]

From a conceptual ontology standpoint, Hodgkin lymphoma can be represented as a neoplastic disease entity in MONDO (Mondo Disease Ontology), where MONDO:0004952 corresponds to Hodgkin lymphoma.[3] It can be further subclassified into MONDO concepts for classical Hodgkin lymphoma, nodular sclerosis Hodgkin lymphoma, mixed cellularity Hodgkin lymphoma, lymphocyte‑rich and lymphocyte‑depleted subtypes, and NLPHL, enabling structured representation of disease heterogeneity within knowledge bases.[3] At the same time, its pathobiology firmly situates it within the broader NCIT (NCI Thesaurus) class of “Hodgkin Lymphoma” (NCIT:C7059) under the parent concept “Lymphoid Neoplasm”.

### 1.2 Key Identifiers and Ontology Cross‑References

Multiple biomedical ontologies and coding systems provide standardized identifiers for Hodgkin lymphoma. In the Online Mendelian Inheritance in Man (OMIM) database, classical Hodgkin lymphoma is referenced under entry #236000 as “LYMPHOMA, HODGKIN, CLASSIC; CHL”, with Orphanet code 391 and Disease Ontology (DO) ID 8567 listed as cross‑references.[1] Orphanet lists Hodgkin lymphoma under the disease identifier 98293, with an inheritance description of “multigenic/multifactorial”.[2] In the Mondo Disease Ontology, MONDO:0004952 corresponds to “Hodgkin lymphoma”, with subclass branching to cHL and nodular lymphocyte predominant Hodgkin lymphoma.[3]

For clinical coding and health‑care reimbursement, ICD‑10‑CM codes in the C81 category are used. ICD‑10‑CM C81.9 denotes “Hodgkin lymphoma, unspecified”, while other C81.x codes specify subtypes such as nodular sclerosis, mixed cellularity, and lymphocyte‑rich or lymphocyte‑depleted forms.[5] SEER and other cancer registries use ICD‑O morphology codes, typically 9650/3–9667/3, to denote specific histological variants. In MeSH (Medical Subject Headings), Hodgkin lymphoma is represented as “Hodgkin Disease” or “Hodgkin Lymphoma”, distinguished from “Lymphoma, Non‑Hodgkin” (MeSH ID D008228), which encompasses other lymphoid malignancies that differ in histology, immunophenotype, and clinical behavior.[4]

These identifiers can be mapped to multiple ontologies for knowledge‑base integration. For example, HPO (Human Phenotype Ontology) term HP:0100726 “Hodgkin lymphoma” can be used for phenotype annotation in genetic databases; NCIT codes can capture histological subtype (e.g., NCIT:C7295 “Classical Hodgkin Lymphoma”, NCIT:C7055 “Nodular Sclerosis Hodgkin Lymphoma”); and SNOMED CT includes concept 118599009 “Hodgkin's disease (disorder)” as a clinical diagnosis node. Such cross‑referencing enables harmonization of disease representations across genomics, clinical, and epidemiological datasets.

### 1.3 Synonyms and Alternative Names

Historically, the disease was known as “Hodgkin’s disease” after Thomas Hodgkin, who first described the pathological entity in the 19th century. Contemporary nomenclature favors “Hodgkin lymphoma” to emphasize its neoplastic nature and align with the naming convention for lymphoid malignancies. Common synonyms include “Hodgkin’s lymphoma” and “Hodgkin disease”, with the latter still appearing in older literature and some indexing systems. Classical Hodgkin lymphoma may be referred to simply as “classical Hodgkin’s lymphoma” or abbreviated “cHL”, while nodular lymphocyte predominant Hodgkin lymphoma is often abbreviated “NLPHL” or referred to as “nodular LP Hodgkin lymphoma” or “popcorn cell lymphoma”.[2][3][9][15]

Subtypes of classical Hodgkin lymphoma have their own descriptive names, such as “nodular sclerosis Hodgkin lymphoma” (NSHL), “mixed cellularity Hodgkin lymphoma” (MCHL), “lymphocyte‑rich classical Hodgkin lymphoma”, and “lymphocyte‑depleted classical Hodgkin lymphoma”, reflecting the histopathological patterns observed.[8] NLPHL has also been called “nodular paragranuloma” in older pathologic literature. In veterinary contexts, lesions with similar morphology may be described as “Hodgkin’s‑like lymphoma”, particularly in canine or feline cases.[20] The coexistence of these synonyms underscores the importance of standardized ontology identifiers to avoid ambiguity.

### 1.4 Nature of the Information and Data Sources

Most structured information about Hodgkin lymphoma in resources such as OMIM, Orphanet, MONDO, NCIT, and MeSH is derived from aggregated disease‑level literature, pathology series, clinical trial cohorts, and epidemiological registries rather than individual patient electronic health records. OMIM’s entry on classical Hodgkin lymphoma summarizes genetic and clinical features from published studies and emphasizes familial aggregation, EBV association, and germline susceptibility, but does not store patient‑level data.[1][10] Orphanet likewise provides aggregated prevalence estimates, clinical descriptions, and etiological hypotheses based on curated reviews and expert consensus.[2]

SEER cancer registry data are collected prospectively from participating institutions and cancer reporting systems, but are aggregated into population‑level statistics such as incidence and survival rates.[6] Pathology Outlines compiles standardized descriptions of histologic and immunophenotypic features, again based on the broader pathology literature rather than particular patients.[8][15] Research articles cited here, such as those on EBV association, JAK–STAT pathway mutations, 9p24.1 amplification, epigenetic profiling, and checkpoint inhibitor trials, are based on cohorts ranging from tens to hundreds of patients or cell lines and thus represent intermediate‑scale data bridging individual case series and large registries.[7][11][12][13][16][17][18][19]

For the purpose of building a disease knowledge base entry, these aggregated resources provide the primary foundation for curated disease characteristics, while EHR‑derived data might contribute additional granularity on real‑world management patterns, comorbidities, and longitudinal outcomes but are not the main basis of current ontological and guideline representations.

---

## 2. Etiology

### 2.1 Multifactorial Causal Framework

Orphanet explicitly classifies Hodgkin lymphoma as having a multigenic/multifactorial inheritance pattern, noting that “the exact cause is unknown but immunological, genetic and environmental factors are thought to be involved.”[2] This aligns with current understanding that there is no single causal germline variant responsible for most cases. Instead, Hodgkin lymphoma arises from the interplay of somatic genetic lesions in germinal‑center B cells, oncogenic viral infections (primarily EBV), host genetic susceptibility, and environmental exposures that cumulatively drive lymphomagenesis.

At the cellular level, the malignant HRS cells of classical Hodgkin lymphoma are derived from preapoptotic germinal center B cells whose B‑cell transcriptional program has been profoundly disrupted, often to the point that immunoglobulin expression is lost and B‑cell identity is largely extinguished.[8][13] The transformation of these precursor cells typically involves constitutive activation of signaling pathways such as JAK–STAT and NF‑κB, sometimes through EBV latent membrane proteins (LMP1 and LMP2A) and sometimes through somatic mutations in pathway components like STAT6, SOCS1, TNFAIP3, JAK1, and JAK2.[7][11] Epigenetic silencing of B‑cell transcription factors and mutually reinforcing histone modifications further cement the transformed phenotype.[13]

In EBV‑positive Hodgkin lymphoma, viral infection is not merely a passenger; it plays a central pathogenic role. EBV latent infection is clonal within tumor cells, indicating that infection preceded malignant transformation and that infected cells underwent clonal expansion.[7] EBV latent gene products such as LMP1 and LMP2A mimic constitutive CD40 and B‑cell receptor signaling, respectively, thereby driving survival and proliferation and contributing to the distinctive phenotype of HRS cells.[7] In EBV‑negative cases, similar signaling outputs are produced by somatic genetic lesions. Thus, the etiologic framework is one of convergent signaling and transcriptional reprogramming achieved via different upstream triggers in different patients.

### 2.2 Infectious Factors: Epstein–Barr Virus

EBV is the only infectious agent with strong evidence linking it etiologically to a subset of Hodgkin lymphoma. In a comprehensive review, it is stated that “up to 40% of Hodgkin lymphoma (HL) cases are associated with the Epstein-Barr virus (EBV)” and that “clonal viral genomes can be found in the HL tumor cells, the Hodgkin Reed-Sternberg cells (HRS).”[7] The virus displays latency II gene expression in EBV‑positive HL, including LMP1, LMP2A, and EBNA1, a pattern similar to that in nasopharyngeal carcinoma and some other EBV‑associated malignancies.[7] These viral oncogenes have functional consequences: LMP1 activates NF‑κB and JAK–STAT signaling; LMP2A provides tonic B‑cell receptor–like signals; EBNA1 maintains viral episomes and may influence transcription and chromatin.

The etiologic link between EBV and HL is supported by multiple lines of evidence. Epidemiologically, infectious mononucleosis, which represents symptomatic primary EBV infection when infection is delayed until adolescence or young adulthood, is followed by a significantly increased risk of HL. In the largest study cited, a Scandinavian cohort of 38,000 mononucleosis patients, mononucleosis was associated with a more than 2.5‑fold increased risk of HL, which remained elevated for up to two decades.[7] The review notes that “mononucleosis was associated with a more than 2.5-fold increased HL risk, which although it decreased with time remained significantly elevated for up to two decades.”[7] This delayed temporal association supports causality rather than reverse causation. Distinctive EBV antibody titer profiles and viral loads both before and after HL diagnosis, as well as demographic and clinical differences between EBV‑positive and EBV‑negative HL, further support an etiologic role.[7]

EBV also modulates the tumor microenvironment. EBV‑positive HL favors a Th1‑polarized immune response, with increased expression of IL‑12 and chemokines such as IP‑10, Mig, and MIP‑1α that support Th1 differentiation and recruitment.[7] This shift may contribute to both immune control and selection for immune‑evasion mechanisms. The virus has been implicated in inducing hypermethylation of tumor‑suppressor genes and altering host methylation systems, potentially contributing to epigenetic reprogramming.[7][13] Overall, EBV can be considered a mechanistic upstream factor in a sizable fraction of HL cases, with key GO terms including GO:0030683 “viral transcription”, GO:0007259 “JAK-STAT cascade”, and GO:0006955 “immune response”.

### 2.3 Genetic Risk Factors and Familial Aggregation

Although HL is not classically inherited in a Mendelian pattern, familial clustering is well documented. A recent ASH review notes that “there is an increased risk of approximately 3-fold described in first-degree relatives of patients with HL compared with the general population.”[10] This elevated relative risk suggests polygenic susceptibility and/or shared environmental factors. Candidate germline risk loci have been identified in genome‑wide association studies, including variants in HLA class II regions, cytokine genes, and immune regulatory pathways, although specific variants and their effect sizes vary by study and population. These germline factors likely modulate the risk of malignant transformation following EBV infection or other environmental exposures by influencing immune control, B‑cell activation, and microenvironmental responses.

Somatic genetic lesions in tumor cells, while not germline risk factors, are central to disease pathogenesis. A large exome‑sequencing study of classical Hodgkin lymphoma uncovered “several recurrently mutated genes, namely, STAT6 (32% of cases), GNA13 (24%), XPO1 (18%), and ITPKB (16%), and document[ed] the functional role of mutant STAT6 in sustaining tumor cell viability.”[11] Mutations of STAT6 cooperated genetically and functionally with disruption of SOCS1, a JAK–STAT pathway inhibitor, to promote cHL growth.[11] Overall, 87% of cases showed dysregulation of the JAK–STAT pathway by genetic alterations in multiple genes, including STAT3, STAT5B, JAK1, JAK2, and PTPN1.[11] These findings highlight the pivotal role of JAK–STAT signaling in cHL pathogenesis and identify an array of somatic variants that serve as pathogenic drivers and potential targets rather than inherited risk factors.

In the same vein, structural genetic changes such as 9p24.1 amplification augment PD‑1 ligand gene dosage and JAK2 activity in nodular sclerosis cHL, further driving immune evasion and signaling pathway activation.[12] These lesions, although somatic, may interact with germline variation in immune checkpoint genes and antigen presentation pathways (e.g., HLA, B2M, CIITA) to influence both risk and clinical course.[11] Suggested GO terms for these processes include GO:0007259 “JAK-STAT cascade”, GO:0043065 “positive regulation of apoptotic process”, and GO:0006954 “inflammatory response”, while CL terms such as CL:0000236 “B cell”, CL:0000913 “T follicular helper cell”, and CL:0000738 “macrophage” capture involved cell types.

### 2.4 Environmental and Lifestyle Risk Factors

Beyond EBV, several environmental and lifestyle factors have been associated with HL, though many findings are inconsistent or modest in effect. Immunosuppression due to HIV infection, organ transplantation, or immunosuppressive therapy increases the risk of HL, particularly EBV‑positive subtypes, by impairing immune surveillance of EBV‑infected B cells and other transformed clones. High socioeconomic status has been linked to higher risk of EBV‑negative cHL in adolescents and young adults, possibly reflecting delayed EBV exposure and consequent infectious mononucleosis.[7] Smoking has been reported as a risk factor for HL in some case–control studies, and occupational exposures to pesticides, solvents, or wood dust may marginally increase risk, though associations are not as strong or consistent as in non‑Hodgkin lymphoma.

Age and sex are important non‑modifiable risk factors. The risk of HL peaks in early adulthood, particularly between ages 15 and 35, and again later in life, with male sex associated with higher incidence overall.[2][6] Orphanet notes that male sex and age greater than 45 years are among the variables included in the International Prognostic Score (IPS), which stratifies advanced‑stage HL patients based on seven risk factors present at diagnosis.[2] Family history of HL or other lymphoid malignancies is an additional risk factor, consistent with the threefold increased risk in first‑degree relatives.[10] Environmental factors may interact with genetic predisposition to modulate risk; for example, individuals with certain HLA types may mount different immune responses to EBV, influencing both the likelihood of symptomatic infectious mononucleosis and subsequent HL risk.

### 2.5 Protective Factors and Gene–Environment Interactions

Protective factors are less well characterized, but early childhood exposure to EBV appears to be protective against the development of adolescent infectious mononucleosis and, indirectly, against EBV‑positive young‑adult HL. The EBV review emphasizes that “earlier exposure to EBV protects against development of adolescent mononucleosis, and as a consequence protects against young-adult onset EBV+ HL.”[7] In many developing countries, EBV infection is nearly universal by early childhood and asymptomatic, and EBV‑positive HL tends to occur at older ages or with different epidemiologic patterns. In industrialized countries, delayed EBV infection leads to adolescent mononucleosis and a subsequent increased HL risk.[7] This illustrates a gene–environment–infection interplay, where viral exposure timing, host genetics, and environmental context (e.g., household crowding, sanitation) jointly shape risk trajectories.

Host genetic background influences not only disease risk but also prognostic impact of EBV positivity. The review notes that “in young adults, there seems to be a marginal prognostic advantage when patients carry the EBV genome in their tumor. Yet among patients aged more than 50 years, EBV positivity was associated with a significantly poorer outcome.”[7] This age‑dependent effect suggests that immune competence, comorbidities, and microenvironmental responses modulate EBV’s role in disease course. Similarly, germline polymorphisms in cytokine genes, immune checkpoints, and antigen presentation pathways likely modify both the risk of HL and response to therapies such as PD‑1 blockade, though detailed GWAS and pharmacogenomic studies remain limited.

From an ontology perspective, protective EBV exposure patterns correspond to environmental descriptors rather than genetic variants, while the interacting biological processes can be captured by GO terms such as GO:0002820 “negative regulation of adaptive immune response based on somatic recombination of immune receptors built from immunoglobulin superfamily domains” and GO:0002764 “immune response-regulating signaling pathway”. EBV itself corresponds to NCBI Taxon 10376, while its latent gene products map to UniProt entries such as LMP1 (P03230) and LMP2A (P03242).

---

## 3. Phenotypes

### 3.1 Core Clinical Phenotypes and Symptomatology

The prototypical clinical phenotype of Hodgkin lymphoma is painless, progressive lymphadenopathy, often in the cervical, supraclavicular, or mediastinal regions. Orphanet describes HL as presenting with lymph node enlargement and constitutional symptoms in a subset of patients.[2] Swollen lymph nodes may be noticed as lumps in the neck, armpits, or groin, sometimes accompanied by a feeling of fullness or cough if mediastinal nodes compress airway structures.[2][9] These manifestations correspond to Human Phenotype Ontology terms such as HP:0002724 “Lymphadenopathy” and HP:0002664 “Cervical lymphadenopathy”.

Systemic “B symptoms”—defined as unexplained fever, drenching night sweats, and unintentional weight loss of more than 10% of body weight over six months—are classic features of more advanced or aggressive disease. Fever (HP:0001945) may be intermittent or continuous, sometimes with a Pel–Ebstein pattern; night sweats (HP:0003537) often impair sleep and cause distress; and weight loss (HP:0001824) reflects catabolic and inflammatory states. Many patients experience fatigue (HP:0012378), pruritus (HP:0001046), and decreased exercise tolerance. Laboratory abnormalities may include anemia (HP:0001903), leukocytosis (HP:0001974), lymphopenia (HP:0001888), elevated erythrocyte sedimentation rate (ESR) (HP:0003565), and hypoalbuminemia (HP:0003073), with some of these incorporated into the IPS prognostic model.[2]

Pain in affected lymph nodes after alcohol ingestion, though rare, is a pathognomonic symptom historically associated with HL. Splenomegaly (HP:0001744), hepatomegaly (HP:0002240), and signs of organ dysfunction can appear when disease is disseminated. In NLPHL, the most common symptom is a localized lump or nodular mass, typically in peripheral nodes, with B symptoms less common.[9][15] NLPHL may present indolently, and patients are often diagnosed at early stages (Ann Arbor I/II) with limited involvement.[15] Quality of life impact arises both from physical symptoms and psychological distress associated with a cancer diagnosis.

### 3.2 Age of Onset, Severity, and Progression of Phenotypes

Hodgkin lymphoma can occur at any age but shows a characteristic bimodal age distribution, with a first peak in adolescence and young adulthood and a second peak in later adulthood.[2][6] The majority of cHL cases in high‑income countries occur between ages 15 and 35, with young‑adult NSHL patients often presenting with bulky mediastinal disease and B symptoms.[2][8] Older adult patients more frequently have mixed cellularity or EBV‑positive subtypes, with systemic symptoms and extranodal involvement more prominent.[7][8] NLPHL tends to occur in younger male patients, sometimes in their 30s–40s, and often presents as localized, early‑stage disease with minimal systemic symptoms.[9][15]

Symptom severity is highly variable. Some patients are diagnosed incidentally with mild lymphadenopathy discovered on imaging, while others present with severe systemic illness, including significant weight loss, fevers, and night sweats that substantially impair functioning. Symptom progression is generally subacute to chronic rather than fulminant. Over weeks to months, lymph nodes enlarge, systemic symptoms intensify, and laboratory abnormalities evolve, reflecting increased tumor burden and systemic inflammatory response. Untreated HL is progressive and ultimately fatal, leading to organ failure due to nodal mass effects, marrow infiltration, or secondary infections, but modern therapies usually interrupt this trajectory.

Frequency of specific phenotypes among affected individuals varies by stage and subtype. B symptoms are present in roughly one‑third of HL patients at diagnosis, more commonly in advanced stages and EBV‑positive or mixed cellularity subtypes. Pruritus is reported in up to 30% of patients, anemia and hypoalbuminemia in those with higher tumor burden. In NLPHL, localized lymphadenopathy without B symptoms predominates, and systemic inflammatory markers may be normal.[9][15] From a staging standpoint, phenotypes are encoded in Ann Arbor and Lugano classifications, which incorporate B symptom status and bulky disease.

Quality of life is substantially impacted by symptom burden, treatment adverse effects, and psychosocial factors. Fatigue, sleep disturbances, pain, and emotional distress can impair daily functioning and work or school participation. Standard instruments like SF‑36, EQ‑5D, and disease‑specific quality of life questionnaires show decrements in physical, emotional, and social domains during active treatment that often improve but may not fully normalize in long‑term survivors due to late effects such as cardiopulmonary toxicity, infertility, and psychological sequelae. For the knowledge base, linking phenotypes like fatigue (HP:0012378), anxiety (HP:0000739), and depression (HP:0000716) to HL, particularly in the survivorship phase, may help capture its broader impact.

### 3.3 Histopathological Phenotypes and Subtype‑Specific Features

Histopathological phenotypes are central to HL classification. Classical HL is defined by malignant HRS cells derived from preapoptotic germinal center B cells with a disrupted B‑cell program, manifesting as large cells with abundant cytoplasm, multilobated nuclei, and prominent nucleoli.[8][13] Pathology Outlines describes nodular sclerosis cHL (NSHL) as a subtype characterized by “collagen bands that surround at least one nodule and Hodgkin Reed-Sternberg (HRS) cells with lacunar type morphology.”[8] Microscopically, NSHL shows a nodular growth pattern with broad collagen bands, thickened lymph node capsule, and variable numbers of HRS cells, small lymphocytes, eosinophils, histiocytes, neutrophils, and occasional foamy macrophages.[8] Lacunar cells—HRS cells with delicate folded or multilobate nuclei surrounded by abundant pale cytoplasm that retract during formalin fixation leaving “lacunae”—are characteristic.[8]

Mixed cellularity cHL, lymphocyte‑rich cHL, and lymphocyte‑depleted cHL differ in the relative abundance of lymphocytes, eosinophils, histiocytes, and fibrosis, but all share the hallmark HRS cells and cHL immunophenotype. Immunohistochemically, HRS cells are typically CD30‑positive and CD15‑positive, weakly positive for PAX5, and negative for most B‑cell markers such as CD20 and OCT2, reflecting the extinction of the B‑cell program.[8][13] NLPHL, in contrast, is a B‑cell neoplasm characterized by scattered LP cells within nodular or diffuse growth patterns, and LP cells display a germinal center B‑cell phenotype: CD20+, PAX5+, OCT2+, BCL6+, CD10‑negative; most cases are negative for CD15 and variably positive for CD30.[15] Pathology Outlines notes that “LP cells preserve the B cell program and express B cell markers, including OCT2,” emphasizing their distinct biology.[15]

The microenvironment differs between subtypes. In cHL, the background is rich in reactive T cells (often regulatory), eosinophils, and macrophages, while in NLPHL it is populated by small B cells and TFH cells expressing CD4 and PD‑1, along with TFH markers like BCL6, ICOS, and CXCL13.[15] These histopathological phenotypes correlate with distinct transcriptional, epigenetic, and signaling profiles. For ontology representation, each subtype can be linked to NCIT histology terms, while immunophenotypic features can be captured by GO Cellular Component terms such as GO:0009897 “external side of plasma membrane” for PD‑1/PD‑L1 localization and CL terms for LP cells (a subtype of CL:0000236 germinal center B cells) and HRS cells (aberrant B cells with partial loss of lineage markers).

### 3.4 Laboratory and Radiologic Phenotypes

Laboratory phenotypes in HL reflect systemic inflammation, bone marrow involvement, and organ dysfunction. Common findings include elevated ESR, C‑reactive protein, and lactate dehydrogenase (LDH); normocytic normochromic anemia; leukocytosis or lymphopenia; and hypoalbuminemia. Orphanet incorporates serum albumin <4 g/dL, hemoglobin <10.5 g/dL, lymphocytopenia, and WBC count >15,000/mm³ as variables in the IPS, each associated with less favorable prognosis when present.[2] These correspond to HPO terms like HP:0003565 (elevated ESR), HP:0001892 (elevated C‑reactive protein), HP:0001974 (leukocytosis), HP:0001888 (lymphopenia), HP:0003073 (hypoalbuminemia), and HP:0001903 (anemia). Biochemical abnormalities may include elevated hepatic transaminases (HP:0002910), alkaline phosphatase (HP:0003155), or creatinine in advanced disease with organ involvement.

Radiologic phenotypes are integral to staging and response assessment. CT and MRI reveal nodal conglomerates, mediastinal masses, and organ involvement. FDG PET/CT is particularly valuable, as HRS cells and surrounding inflammatory cells exhibit high glycolytic activity, leading to intense FDG uptake.[16] PET phenotypes include hypermetabolic lymphadenopathy, splenic involvement, bone marrow uptake, and extranodal disease. The Deauville five‑point score (DS) is recommended for standardized visual interpretation of FDG PET in lymphoma. A 2023 study notes that “Deauville five-point score (DS) is recommended for response assessment in international guidelines. DS gives the threshold for adequate or inadequate response to be adapted according to the clinical context or research question.”[16] Scores range from 1 (no uptake) to 5 (markedly increased uptake compared to liver and/or new lesions), with the liver serving as a reference.[16] Interim PET negativity (DS 1–3) is associated with improved outcomes and allows de‑escalation of therapy, whereas DS 4–5 suggests inadequate response and prompts treatment intensification.[16]

These imaging phenotypes can be mapped to RadLex and GO terms such as GO:0006096 “glycolytic process” reflecting increased FDG uptake and to NCIT concepts like “Positron Emission Tomography” (NCIT:C17297) and “Deauville Criteria” as an imaging assessment tool. The integration of PET metrics with clinical and histologic phenotypes yields a multidimensional picture of disease activity and response.

---

## 4. Genetic and Molecular Information

### 4.1 Somatic Driver Lesions and Causal Genes

Classical Hodgkin lymphoma is not driven by a single germline mutation but by a constellation of somatic genetic and epigenetic alterations in HRS cells. The exome‑sequencing study by Tiacci et al. represents a landmark in defining the cHL coding genome. The authors report that they “uncovered several recurrently mutated genes, namely, STAT6 (32% of cases), GNA13 (24%), XPO1 (18%), and ITPKB (16%), and document the functional role of mutant STAT6 in sustaining tumor cell viability.”[11] Mutations of STAT6 genetically and functionally cooperated with disruption of SOCS1, a JAK–STAT pathway inhibitor, to promote cHL growth.[11] Overall, “87% (26/30) of the evaluable cHL cases carried genetic lesions in members of the JAK-STAT cascade,” attesting to the pivotal role of JAK–STAT signaling.[11]

Key genes impacted include:

STAT6 (HGNC:11367): Frequently harboring activating missense mutations in its DNA‑binding or transactivation domains, leading to constitutive transcriptional activity downstream of cytokine signals. These mutations are typically somatic and classified as pathogenic or likely pathogenic in tumor contexts.

SOCS1 (HGNC:15530): Often disrupted by frameshift or nonsense mutations, deletions, or promoter methylation, removing negative feedback on JAK–STAT signaling and allowing uncontrolled pathway activation.

JAK1, JAK2 (HGNC:6190, HGNC:6192): Occasionally amplified or mutated, particularly JAK2 in the context of 9p24.1 amplification, increasing kinase activity and contributing to STAT activation and PD‑1 ligand induction.[11][12]

STAT3, STAT5B (HGNC:11364, HGNC:11362): Mutations in these transcription factors also contribute to altered gene expression programs, though less frequently than STAT6.[11]

GNA13 (HGNC:4399): Mutations in this G protein subunit may affect cell migration and microenvironment interactions.

XPO1 (HGNC:12801): Mutations in this nuclear export protein may disrupt nuclear–cytoplasmic trafficking of key regulators.

ITPKB (HGNC:6188): Mutations may alter calcium signaling and B‑cell receptor pathways.

Other genes implicated include TNFAIP3 (A20), a negative regulator of NF‑κB, and PTPN1, another inhibitor of JAK–STAT signaling.[11] Together, these lesions produce constitutive pro‑survival and pro‑inflammatory signaling.

From a variant classification standpoint, these somatic mutations are pathogenic in the oncologic context, conferring a gain of function in oncogenes (e.g., STAT6, JAK2) or loss of function in tumor suppressors (e.g., SOCS1, TNFAIP3). They are somatic rather than germline in the vast majority of cases, and allele frequencies in population databases such as gnomAD are low or absent, consistent with their selection in tumors rather than normal genomes. COSMIC and TCGA data corroborate their prevalence in HL and related lymphoid malignancies.

### 4.2 Immune‑Evasion Lesions: PD‑L1/PD‑L2 and 9p24.1 Amplification

A key structural lesion characteristic of nodular sclerosis cHL and primary mediastinal large B‑cell lymphoma (MLBCL) is amplification of chromosome 9p24.1, which targets the PD‑1 ligand genes PD‑L1 (CD274) and PD‑L2 (PDCD1LG2) and co‑amplifies JAK2.[12] In an integrative analysis, Green et al. found that “we integrate high-resolution copy number data with transcriptional profiles and identify the immunoregulatory genes, PD-L1 and PD-L2, as key targets at the 9p24.1 amplification peak in HL and MLBCL cell lines.”[12] They extended these findings to laser‑capture microdissected primary HRS cells and documented that PD‑1 ligand/9p24.1 amplification is restricted to nodular sclerosis HL, the cHL subtype most closely related to MLBCL.[12] Importantly, “the extended 9p24.1 amplification region also included the Janus kinase 2 (JAK2) locus” and “JAK2 amplification increased protein expression and activity, specifically induced PD-1 ligand transcription, and enhanced sensitivity to JAK2 inhibition.”[12]

This co‑amplification creates a pathogenic loop: increased JAK2 dosage amplifies JAK–STAT signaling, which further induces PD‑L1/PD‑L2 transcription, thereby enhancing immune checkpoint engagement and tumor immune evasion.[12] The PD‑1 receptor is expressed on tumor‑infiltrating T cells, and its ligation by PD‑L1/PD‑L2 on HRS cells dampens anti‑tumor T cell responses.[12] These findings define 9p24.1 amplification as a disease‑specific structural abnormality with probable prognostic significance and rational therapeutic targets, PD‑1 ligand and JAK2.[12] In terms of GO terms, this lesion relates to GO:1902539 “positive regulation of T cell mediated immunity” (in the sense of negative feedback) and GO:0007259 “JAK-STAT cascade”. At the protein level, PD‑L1 and PD‑L2 are membrane proteins (GO:0005886 “plasma membrane”), while JAK2 is a cytoplasmic tyrosine kinase (GO:0005886, GO:0005737 “cytoplasm”).

These structural abnormalities can be detected by FISH, array CGH, or next‑generation sequencing‑based copy number analysis. They are typically somatic and restricted to tumor cells, with copy gains from low‑level amplification to high‑level amplification. Their contribution to immune evasion explains the remarkable sensitivity of cHL to PD‑1 blockade and informs personalized medicine approaches.

### 4.3 Epigenetic Reprogramming and Loss of B‑Cell Identity

Beyond DNA sequence changes, epigenetic alterations are central to HL pathogenesis. A study on classical HL epigenetic features concluded that “epigenetic changes are involved in the extinction of the B-cell gene expression program of classical Hodgkin’s lymphoma.”[13] DNA methylation of gene promoters contributes significantly to gene silencing, whereas histone modifications such as acetylation of lysine 9 and 14 of histone H3 (H3K9/14 acetylation) are positively correlated with gene activation.[13] The authors demonstrated that characteristic B‑cell genes were hypoacetylated in cHL and plasma cell myeloma cell lines compared to normal B‑cell lines, indicating epigenetic down‑regulation.[13]

Moreover, H3K27 trimethylation for selected characteristic B‑cell genes was much more prevalent in cHL than in plasma cell myeloma, suggesting additional layers of repressive chromatin.[13] The study concluded that “our epigenetic data support the view that classical Hodgkin’s lymphoma is characterized by abortive plasma cell differentiation with a down-regulation of characteristic B-cell genes but without activation of most genes typical of plasma cells.”[13] Suppressive H3K27 trimethylation and DNA promoter methylation reinforce histone H3 deacetylation, leading to “almost complete extinction of the B-cell expression program of cHL.”[13]

These epigenetic changes can be linked to epigenomics databases such as ENCODE and Roadmap Epigenomics, though HL‑specific datasets are limited. GO terms like GO:0006342 “chromatin silencing”, GO:0045814 “negative regulation of gene expression, epigenetic”, and GO:0016568 “chromatin modification” capture these processes. The extinction of B‑cell gene expression explains the paradox of HRS cells’ derivation from germinal center B cells yet loss of typical B‑cell markers like CD20 and immunoglobulin heavy chain expression. It also underscores the divergence between cHL and NLPHL, where LP cells preserve the B‑cell program and express B‑cell markers including OCT2, BCL6, and PAX5.[15]

### 4.4 Immune Evasion and Antigen Presentation

In addition to PD‑1 ligand overexpression, HL tumors acquire lesions in antigen presentation pathways and immune checkpoints. The exome study notes that “various genetic lesions have then been found to be recurrent in fractions of cHL cases, which result in constitutive activation of the anti-apoptotic and pro-inflammatory NF-κB and JAK-STAT signaling pathways (eg, TNFAIP3 and SOCS1 disruption, respectively), as well as in immune evasion (eg, PDL1/PDL2 copy number gain; B2M and CIITA disruption).”[11] B2M (beta‑2 microglobulin) and CIITA (class II transactivator) are essential for MHC class I and II expression, respectively, and their disruption impairs tumor antigen presentation to T cells, facilitating immune escape.

EBV‑positive HL leverages viral strategies such as LMP1‑mediated up‑regulation of PD‑L1 and other immune modulators. EBV presence alters cytokine and chemokine expression, favoring a Th1 reaction in the HL microenvironment, with increased IL‑12 and chemokines such as IP‑10, Mig, and MIP‑1α, but also potentially inducing immune exhaustion and checkpoint up‑regulation.[7] Combined with PD‑1 ligand expression and antigen presentation defects, these changes create an immunosuppressive niche where tumor cells can persist despite a highly immunogenic profile.

These immune‑evasion mechanisms correspond to GO terms such as GO:0002420 “immune system process”, GO:0002517 “negative regulation of immune system process”, and GO:0019882 “antigen processing and presentation”. They also underpin the rationale for immunotherapies targeting PD‑1 and other checkpoints, which are cataloged in NCIT under terms like “Nivolumab” (NCIT:C104801) and “Pembrolizumab” (NCIT:C116709).

### 4.5 Somatic vs Germline Origin and Modifier Genes

Most genetic abnormalities described in HL are somatic, restricted to HRS or LP cells and not present in germline DNA. Patients do not generally transmit these mutations to offspring, and HL is not considered a classical hereditary cancer syndrome. Germline susceptibility loci contribute modestly to risk but are not determinative. There is no single “Hodgkin lymphoma gene” identified in ClinVar or HGMD as causative in Mendelian fashion. Instead, HL’s inheritance pattern is best captured as multifactorial, with polygenic risk and environmental triggers.[2][10]

Modifier genes in the sense of germline variants that influence disease severity or outcomes remain incompletely characterized. HLA class II alleles, cytokine gene polymorphisms, and immune checkpoint variants may modulate EBV infection outcomes, HL risk, and treatment responses. For example, the differential prognostic impact of EBV positivity by age suggests that host factors, possibly including HLA and T cell functionality, interact with viral biology.[7] Germline variants in DNA repair genes could influence risk of treatment‑related second malignancies, particularly after radiation or high‑dose chemotherapy.[17] However, these hypotheses have yet to be fully cemented in large‑scale genetic studies, and relevant ClinGen entries are sparse.

From a gene ontology and cell ontology perspective, germline modifiers likely affect processes such as GO:0006955 “immune response”, GO:0002460 “adaptive immune response”, and CL terms for T cells, B cells, NK cells, and dendritic cells. The knowledge base should acknowledge that HL’s genetic landscape is dominated by somatic tumor lesions, with germline contributions falling under polygenic risk rather than monogenic causality.

---

## 5. Environmental and Infectious Information

### 5.1 Non‑Genetic Environmental Factors

Non‑genetic environmental factors in HL include infectious exposures, immunosuppressive environments, and socio‑behavioral determinants of viral exposure timing. EBV is the primary infectious agent, as discussed, and its epidemiology intersects with environmental conditions such as crowding, sanitation, and household size. Early childhood EBV infection in high‑prevalence settings leads to asymptomatic primary infection and may protect against adolescent mononucleosis and young‑adult EBV‑positive HL.[7] In contrast, delayed EBV infection in high‑income environments is associated with mononucleosis and increased HL risk.[7]

Immunosuppressive settings such as HIV infection, organ transplantation, and immunosuppressive therapy increase HL risk, particularly EBV‑positive subtypes, by impairing immune surveillance of EBV and transformed B cells. Occupational exposures to solvents, pesticides, organic dusts, and radiation have been investigated, but their role is less clear than in non‑Hodgkin lymphomas. Lifestyle factors such as smoking and alcohol use may modulate risk and disease course indirectly through immune function and comorbidities, but no single exposure is strongly causal.

Environmental factors also influence survivorship and late effects. Radiation exposure from mediastinal radiotherapy increases long‑term risk of cardiovascular disease, secondary breast cancer, and thyroid dysfunction. High‑dose alkylating agents increase risk of infertility and myelodysplastic syndromes. Thus, environment intersects both etiology and prognosis, and public health interventions to minimize unnecessary radiation and optimize survivorship care are important components of HL management.

### 5.2 Lifestyle Factors and Health Behaviors

Lifestyle factors such as smoking, diet, physical activity, and alcohol consumption affect overall immune competence and long‑term health, though their direct causal impact on HL onset is modest. Smoking may increase HL risk modestly, perhaps by influencing immune function or by co‑exposure to carcinogens, but it is not as strongly associated as in lung cancer or certain leukemias. Healthy diet and regular physical activity support immune function and may mitigate treatment‑related risks such as cardiovascular disease and metabolic syndrome, thus playing a role in tertiary prevention rather than primary causation.

Alcohol consumption has a peculiar relationship with HL in that it can trigger pain in involved lymph nodes, a classic but rare symptom. Otherwise, heavy alcohol use may exacerbate hepatic toxicity of chemotherapy and impair immune recovery. Stress and psychosocial factors may influence symptom perception and care‑seeking behavior, affecting stage at diagnosis and outcomes. From a knowledge base perspective, lifestyle factors might be captured via CHEBI entities for alcohol (CHEBI:16236 ethanol), tobacco constituents (CHEBI:23992 nicotine), and nutritional factors, but detailed causal chains are less established than for infectious and genetic factors.

### 5.3 Infectious Agents Beyond EBV

No other pathogen has a firmly established etiologic role in HL comparable to EBV. Other herpesviruses, HIV, and various bacteria have been investigated as potential co‑factors or triggers, but evidence remains weak or inconsistent. EBV stands out as the only infectious agent with clonal presence in tumor cells, biologically plausible mechanisms of transformation, and strong epidemiologic associations.[7] In HIV‑associated HL, EBV positivity is nearly universal, and immunosuppression amplifies the virus’s transforming potential. However, HL itself is not transmissible person‑to‑person, and EBV infection is necessary but not sufficient for HL development.

From ontological and taxonomic perspectives, EBV corresponds to NCBI Taxon 10376, while HIV corresponds to Taxon 11676 (HIV‑1), but the knowledge base entry for HL should highlight EBV specifically and distinguish HL from EBV‑negative lymphomas and other EBV‑associated diseases such as nasopharyngeal carcinoma, Burkitt lymphoma, and post‑transplant lymphoproliferative disease.

---

## 6. Mechanism and Pathophysiology

### 6.1 Cellular Origin and Early Events in Lymphomagenesis

The consensus view is that classical Hodgkin lymphoma arises from germinal center B cells undergoing abortive differentiation and malignant transformation. HRS cells bear evidence of V(D)J recombined immunoglobulin genes with somatic hypermutation, indicating their origin from germinal center reactions, but often harbor “crippling” mutations that prevent expression of functional B‑cell receptor.[8][13] Without compensatory survival signals, such B cells would normally undergo apoptosis, but in HL they are rescued by oncogenic events such as EBV infection, constitutive JAK–STAT and NF‑κB activation, and epigenetic reprogramming.

In EBV‑positive HL, the sequence of events can be sketched as follows. Primary EBV infection leads to latent infection in B cells, with viral gene products such as LMP1 and LMP2A mimicking CD40 and B‑cell receptor signaling, respectively.[7] In a preapoptotic germinal center B cell with damaged immunoglobulin genes, LMP2A provides tonic survival signals, while LMP1 activates NF‑κB and JAK–STAT pathways, promoting proliferation and survival.[7] Viral infection is clonal, indicating that a single infected B cell underwent malignant transformation and clonal expansion.[7] Host epigenetic machinery is modulated by EBV, inducing hypermethylation of tumor suppressor genes and altering chromatin states.[7][13] The resulting HRS cell has lost much of its B‑cell identity; B‑cell genes are silenced by promoter methylation and histone deacetylation, reinforced by H3K27 trimethylation.[13]

In EBV‑negative HL, similar signaling outcomes are achieved via somatic mutations and structural alterations. Activating mutations in JAK1, JAK2, STAT6, STAT3, and STAT5B, combined with disruption of SOCS1 and PTPN1, produce constitutive JAK–STAT signaling.[11] Mutations in TNFAIP3 and other regulators yield persistent NF‑κB activation. The epigenetic extinction of B‑cell gene expression proceeds through host factors alone, without viral influence.[13] In both scenarios, the transformed HRS cell is characterized by aberrant expression of cytokines, chemokines, and surface molecules such as CD30, CD40, PD‑L1, PD‑L2, and various adhesion molecules, enabling recruitment and manipulation of the microenvironment.

These early events are upstream in the causal chain, while downstream consequences include microenvironment formation, immune evasion, systemic inflammation, and clinical phenotypes. GO terms capturing these processes include GO:0002764 “immune response-regulating signaling pathway”, GO:0042113 “B cell activation”, GO:0007249 “I-kappaB kinase/NF-kappaB signaling”, and GO:0007259 “JAK-STAT cascade”. CL terms for involved cell types include CL:0000236 “B cell” (precursor), CL:0000097 “germinal center B cell”, and CL:0000989 “Hodgkin/Reed-Sternberg cell” (if defined).

### 6.2 Tumor Microenvironment and Immune Modulation

The HL tumor microenvironment is distinctive and crucial to disease biology. HRS cells comprise only a minority of total cells in involved lymph nodes; the bulk consists of reactive T cells, B cells, eosinophils, macrophages, plasma cells, and fibroblasts, forming an intricate ecosystem. A recent single‑cell RNA‑sequencing study using paired diagnostic and relapsed cHL samples identified “distinct shifts in B-cell populations” and other microenvironmental changes, highlighting dynamic remodeling over time.[14] Regulatory T cells, TFH cells, exhausted effector T cells, and myeloid‑derived suppressor cells are enriched, while cytotoxic T cell function is curtailed by PD‑1 engagement and other checkpoints.

EBV‑positive HL favors a Th1‑polarized microenvironment, with increased IL‑12 and chemokines supporting Th1 differentiation and recruitment.[7] However, PD‑1/PD‑L1 interactions and antigen presentation defects blunt effective cytotoxic responses. In EBV‑negative HL, similar immune modulation occurs via tumor‑derived cytokines and genetic lesions such as PD‑L1/PD‑L2 amplification and B2M loss.[11][12] HRS cells secrete factors like IL‑5, IL‑13, TGF‑β, and GM‑CSF that attract eosinophils, macrophages, and fibroblasts, contributing to fibrosis and nodular sclerosis in NSHL.[8] Eosinophils release cytotoxic mediators and growth factors, while macrophages and fibroblasts produce extracellular matrix, shaping the physical architecture of the tumor.

The microenvironment supports HRS cell survival by providing additional pro‑survival signals (e.g., CD40L on T cells engaging CD40 on HRS cells), shielding them from immune attack, and contributing to angiogenesis and metabolic support. GO terms like GO:0006954 “inflammatory response”, GO:0002682 “regulation of immune system process”, and GO:0001568 “blood vessel development” capture these interactions, while CL terms such as CL:0000545 “T cell”, CL:0000913 “T follicular helper cell”, CL:0000586 “eosinophil”, and CL:0000738 “macrophage” denote involved cell types.

### 6.3 Systemic Inflammation and Clinical Manifestations

The systemic manifestations of HL—fever, night sweats, weight loss, fatigue—reflect cytokine and chemokine production by HRS cells and the microenvironment, as well as metabolic demands of the tumor. IL‑1, IL‑6, TNF‑α, and IFN‑γ contribute to fever and malaise; IL‑2 and IL‑10 influence T cell responses; chemokines recruit additional immune cells, perpetuating inflammation.[7] Elevated LDH and ESR reflect increased cell turnover and acute‑phase responses. Increased glycolytic activity in tumor and inflammatory cells underlies intense FDG uptake on PET, embodying GO:0006096 “glycolytic process”.

Fibrosis and nodular sclerosis in NSHL result from fibroblast activation and extracellular matrix deposition, guided by TGF‑β and other growth factors. Mediastinal masses can cause cough, chest pain, and superior vena cava syndrome. Splenic and hepatic involvement leads to organomegaly and potential dysfunction. Bone marrow infiltration can cause pancytopenia and predispose to infections. These downstream pathophysiologic events connect molecular and cellular mechanisms to organ‑level phenotypes and ultimately to clinical outcomes.

### 6.4 Epigenetic Cascades and Transcriptional Avalanche

The epigenetic analysis of cHL suggests that initial epigenetic modifications can induce a “transcriptional avalanche effect” in which up‑regulation of cHL‑characteristic but B‑cell lineage‑inappropriate genes coincides with extensive down‑regulation of the B‑cell expression program.[13] Histone H3 deacetylation contributes significantly to gene silencing, while H3K27 trimethylation and DNA methylation reinforce repression.[13] Genes jointly hyperacetylated and expressed in cHL and plasma cell myeloma cell lines, such as IRF4/MUM1 and RYBP, represent a limited subset, indicating incomplete and aberrant differentiation.[13]

These epigenetic cascades are upstream of stable phenotype establishment but downstream of initial triggers such as EBV infection or somatic mutations. Once the B‑cell program is extinguished, HRS cells rely on alternative survival pathways, including those driven by JAK–STAT, NF‑κB, and PD‑1 ligand expression. Epigenetic therapies such as histone deacetylase inhibitors or DNA methyltransferase inhibitors have theoretical appeal but have not yet assumed a major role in HL treatment, partly because standard therapies are so effective.

Suggested GO terms include GO:0016568 “chromatin modification”, GO:0045814 “negative regulation of gene expression, epigenetic”, and GO:0006342 “chromatin silencing”. The knowledge base may annotate key epigenetic regulators, such as EZH2 (H3K27 methyltransferase), HDACs, and DNMTs, as players in HL pathophysiology, even if direct mutations in these genes are less frequent than in some other lymphomas.

### 6.5 Molecular Profiling and Multi‑Omics Integration

Multi‑omics approaches have begun to integrate genomic, transcriptomic, proteomic, and epigenomic data in HL. Exome sequencing defines recurrent mutational patterns,[11] while copy number profiling reveals PD‑L1/PD‑L2/JAK2 amplification.[12] Gene expression profiling shows up‑regulation of immune‑evasion molecules, cytokines, and transcription factors like IRF4/MUM1, as well as down‑regulation of B‑cell genes.[13] Single‑cell RNA‑sequencing dissects the microenvironment, identifying distinct shifts in B‑cell and T cell populations between diagnosis and relapse.[14]

Proteomic analyses highlight overexpression of CD30, PD‑L1, PD‑L2, and other surface proteins. Metabolomics, though less developed in HL, underscores high glycolytic flux, consistent with FDG PET findings.[16] Spatial transcriptomics could, in principle, map gene expression patterns to histologic structures such as collagen bands and nodules, but HL‑specific datasets are rare. Functional genomics screens using CRISPR or RNAi in HL cell lines have identified JAK–STAT pathway components, NF‑κB regulators, and PD‑1 ligand expression as essential for cell survival and immune evasion.

TCGA and ICGC include limited HL samples, but dedicated HL genomic cohorts have begun to fill the gap. These multi‑omics data reinforce the centrality of JAK–STAT and PD‑1 pathways, support the rationale for targeted therapies, and help identify biomarkers of response and resistance. For ontology, linking HL to Reactome pathways such as “Cytokine Signaling in Immune system” (R-HSA-1280215), “Adaptive Immune System” (R-HSA-1280218), and “Programmed Cell Death-1 (PD-1) signaling” would provide structured mechanistic representation.

---

## 7. Anatomical Structures Affected

### 7.1 Organ‑Level Involvement

Hodgkin lymphoma primarily affects the lymphatic system. The most commonly involved anatomical structures are lymph nodes (UBERON:0000029), particularly cervical, supraclavicular, mediastinal, axillary, and inguinal stations. Mediastinal lymph node involvement is especially characteristic of NSHL in young adults, often forming bulky masses in the anterior mediastinum.[8] The spleen (UBERON:0002106) and liver (UBERON:0002107) can be involved, either by contiguous spread from nodes or hematogenous dissemination, leading to splenomegaly and hepatomegaly. Bone marrow (UBERON:0002370) involvement occurs in advanced disease and is associated with cytopenias and increased risk of infection.

Other organs may be secondarily affected. Lungs (UBERON:0002048) can harbor parenchymal infiltrates, particularly in advanced HL or after treatment; pleura (UBERON:0000178) may develop effusions due to nodal or mediastinal mass effects. Gastrointestinal tract involvement is rare but possible, particularly in NLPHL with transformation to diffuse large B‑cell lymphoma. The cardiovascular system may be indirectly affected by treatment (e.g., anthracycline cardiotoxicity, radiation‑induced heart disease) rather than primary HL infiltration. Endocrine organs like the thyroid can be affected by radiation to the neck, and gonads may be impacted by alkylating chemotherapy.

Organ‑level manifestations can be encoded by UBERON terms and SNOMED CT diagnoses, while HL’s systemic nature is captured by NCIT and MONDO. The disease’s impact on body systems is broad, with primary lymphatic involvement and secondary effects on hematologic, immune, cardiovascular, pulmonary, endocrine, and reproductive systems.

### 7.2 Tissue and Cell‑Level Targeting

At the tissue level, HL targets lymphoid tissue, particularly germinal center architecture within lymph nodes and spleen. Lymph nodes show partial or complete effacement of normal follicles by nodular sclerosis, mixed cellularity infiltrates, or LP cell nodules, depending on subtype.[8][15] Fibrous tissue, collagen bands, and granulomatous structures may appear, altering the microenvironment. Connective tissue (collagen, fibroblasts) plays a significant role in NSHL, while reticular fibers and sinus structures are disrupted or remodeled.

The primary cell types targeted are germinal center B cells, which transform into HRS cells in cHL and LP cells in NLPHL. HRS cells are aberrant B cells with partial loss of B‑cell markers and acquisition of alternative transcriptional programs.[13] LP cells preserve more typical B‑cell identity.[15] Surrounding cell populations include T cells (CD4+, CD8+, regulatory, TFH), small B cells, eosinophils, macrophages, dendritic cells, and fibroblasts. CL ontology can represent these cell types: CL:0000097 “germinal center B cell”, CL:0000545 “T cell”, CL:0000913 “T follicular helper cell”, CL:0000586 “eosinophil”, CL:0000738 “macrophage”, and CL:0000057 “fibroblast”.

In EBV‑positive HL, EBV‑infected HRS cells express viral genes and interact with responsive T cells and NK cells. In EBV‑negative HL, similar architecture emerges without viral presence. The tissue milieu includes extracellular matrix, vascular structures, and lymphatic sinuses, all remodeled by cytokines and growth factors emanating from HRS cells and reactive cells.

### 7.3 Subcellular Compartments and Signaling Localizations

Subcellular compartments involved in HL pathophysiology include the nucleus, cytoplasm, cell membrane, and organelles associated with signaling. JAK–STAT signaling initiates at cytokine receptors on the plasma membrane (GO:0005886), with JAK kinases in the cytoplasm (GO:0005737) phosphorylating STAT transcription factors, which then dimerize and translocate to the nucleus (GO:0005634) to regulate gene expression.[11] NF‑κB signaling involves receptor engagement (e.g., CD40, TLRs) at the membrane and cytoplasmic IKK complex activation, followed by nuclear translocation of NF‑κB dimers.[11][7]

PD‑L1 and PD‑L2 are type I transmembrane proteins localized to the plasma membrane, engaging PD‑1 on T cells and initiating intracellular inhibitory signaling in those T cells.[12] EBV latent proteins LMP1 and LMP2A localize to the membrane and cytoplasmic compartments, forming scaffolds for signaling complexes. Epigenetic machinery (HDACs, H3K27 methyltransferase EZH2, DNMTs) operates in the nucleus, modifying chromatin (GO:0000785 “chromatin”, GO:0005719 “heterochromatin”) and influencing transcription.

Metabolic changes such as increased glycolysis occur in the cytosol (GO:0005829) and mitochondria (GO:0005739), reflecting Warburg‑like metabolism in HRS cells and microenvironmental cells. The net effect is increased FDG uptake and systemic metabolic alterations. Subcellular localization is important for targeted therapies; for example, small‑molecule JAK inhibitors operate in the cytoplasm, while immune checkpoint antibodies act at the membrane interface.

### 7.4 Localization and Lateralization Patterns

HL exhibits characteristic localization patterns. Cervical and supraclavicular lymph nodes are commonly involved, often bilaterally but sometimes asymmetrically. Mediastinal involvement tends to center in anterior mediastinal nodes, often forming midline masses that can extend symmetrically. Axillary and inguinal nodes may be involved depending on spread. Disease tends to progress contiguously along lymphatic chains rather than skip widely, a feature reflected in Ann Arbor and Lugano staging (e.g., involvement of contiguous regions vs disseminated involvement).

Lateralization is less prominent than in solid tumors, but certain patterns such as unilateral cervical node involvement may occur early, while bilateral involvement becomes more common with progression. Splenic involvement can be focal or diffuse. NLPHL often presents as localized, unilateral nodal disease without widespread involvement.[9][15] Extra‑nodal involvement in HL is less common than in non‑Hodgkin lymphomas but can include lung, bone, and skin.

In anatomical ontologies, these patterns can be represented by UBERON terms for specific nodal chains and SUO (Systematized Nomenclature of Medicine) anatomical qualifiers. For knowledge‑base purposes, capturing primary and secondary anatomical sites provides context for phenotypes, diagnostics, and staging.

---

## 8. Temporal Development

### 8.1 Onset and Natural History

Hodgkin lymphoma typically has an insidious onset. Patients may notice lymph node enlargement over weeks to months before diagnosis, with systemic symptoms emerging gradually. The typical age of onset is in adolescence or young adulthood, particularly for NSHL, with a second peak in older adults.[2][6] Onset is generally subacute rather than acute; sudden fulminant presentations are rare. In children, HL can present with cervical lymphadenopathy and B symptoms, and pediatric HL shares many features with adult disease but with some differences in histology and EBV association.

Without treatment, HL is progressive and eventually fatal, though the time course may span months to years depending on subtype and host factors. The natural history involves contiguous spread along lymph node chains, followed by involvement of spleen, liver, and bone marrow, leading to anemia, recurrent infections, organ failure, and cachexia. Modern therapies intervene early in this course, and most patients are diagnosed at stages where curative treatment is effective.

### 8.2 Staging and Progression

Disease stages in HL are classified by the Ann Arbor system and its modifications, which consider number and location of involved nodal regions, presence of extra‑nodal disease, and B symptoms. Stage I involves a single nodal region; Stage II involves two or more nodal regions on the same side of the diaphragm; Stage III involves nodes on both sides of the diaphragm; Stage IV denotes disseminated involvement of extra‑nodal organs such as liver, bone marrow, or lungs. The presence of B symptoms is denoted by “B”, and bulky disease by “X”. Lugano staging refines areas and incorporates modern imaging.[16]

Progression rate varies by subtype and risk factors. NSHL in young adults with bulky mediastinal disease can progress relatively rapidly if untreated, while NLPHL often has a slower, indolent course. EBV‑positive mixed cellularity HL in older adults may progress more quickly due to comorbidities and immune senescence.[7][8] IPS factors such as age >45, male sex, stage IV disease, low albumin, low hemoglobin, lymphocytopenia, and high WBC count worsen prognosis and suggest more aggressive disease.[2] SEER data indicate that age‑adjusted incidence rates have been falling by about 1.4% per year over 2013–2022, and death rates by about 2.3% per year over 2014–2023, reflecting improved treatment and possibly changes in risk factors.[6]

### 8.3 Disease Course Patterns and Remission

The disease course in HL is often characterized by periods of active disease and remission. With standard first‑line therapy, complete remission is achieved in the majority of patients, and many are cured. However, some patients relapse, particularly those with advanced disease, unfavorable IPS, bulky masses, or incomplete response to initial therapy. Relapse can occur within a few months to several years after treatment, and late relapses beyond five years are possible but less common.

Patterns of remission include treatment‑induced complete remission, partial remission, and stable disease. Spontaneous remission in HL is extremely rare and not a reliable phenomenon. Response‑adapted therapy using interim FDG PET/CT and Deauville scoring can identify patients likely to be cured with de‑escalated therapy and those requiring intensified regimens.[16] Interim PET negativity is associated with improved outcomes and long‑term remission.[16] Relapsing–remitting patterns occur in patients who respond to salvage regimens and auto‑HCT but later relapse, sometimes responding again to newer therapies like PD‑1 inhibitors.[17][18][19]

Critical periods include the first two years after therapy, when relapse risk is highest, and the long‑term survivorship phase, when late effects and second malignancies emerge. The auto‑HCT study notes that 2‑year progression‑free survivors still have an excess late‑mortality risk compared with the general population, with relapse accounting for 44% of late deaths.[17] Thus, disease course extends beyond initial treatment, encompassing chronic survivorship and risk management.

---

## 9. Inheritance and Population

### 9.1 Epidemiology: Incidence, Prevalence, and Mortality

Hodgkin lymphoma is a rare cancer. SEER statistics indicate that “the rate of new cases of Hodgkin lymphoma was 2.5 per 100,000 men and women per year. The death rate was 0.3 per 100,000 men and women per year,” based on 2018–2022 cases and 2019–2023 deaths.[6] These rates are age‑adjusted. The lifetime risk of developing HL is approximately 0.2% for men and women.[6] In 2022, there were an estimated 233,860 people living with HL in the United States, reflecting both new cases and long‑term survivors.[6] In 2025, SEER estimates 8,720 new HL cases and 1,150 deaths.[6]

Orphanet states that HL is uncommon, with an incidence of about 1 per 40,000 in North America and Europe and about 8,500 new cases annually in the U.S., consistent with SEER data.[2][6] HL represents about 0.4% of all new cancer cases and 0.2% of all cancer deaths in the U.S., emphasizing its rarity relative to more common malignancies.[6] Incidence and mortality have been declining modestly over recent years, likely due to improved treatment and perhaps changes in risk factors such as EBV exposure patterns or HIV management.[6]

Globally, HL incidence varies, with higher rates in high‑income countries for NSHL and lower rates but higher EBV‑positive mixed cellularity subtypes in some low‑ and middle‑income settings. Age and sex distributions vary, but male predominance and the bimodal age curve are common themes.[2][6][7]

### 9.2 Inheritance Pattern and Genetic Architecture

HL’s genetic architecture is multifactorial. Orphanet lists its inheritance as “multigenic/multifactorial,” meaning that multiple genes and environmental factors contribute to risk.[2] There is no autosomal dominant or recessive inheritance pattern, no known X‑linked or mitochondrial HL gene, and no repeat expansion or anticipation phenomenon. Penetrance is not a meaningful concept here because there is no single causative variant whose penetrance can be quantified.

Familial aggregation manifests as a threefold increased risk in first‑degree relatives, as noted in the ASH article.[10] This elevated risk suggests polygenic susceptibility, shared environment, or both. Expressivity is variable, with family members who develop HL experiencing different ages of onset, subtypes, and severities. Genetic anticipation—worsening severity in successive generations due to repeat expansions—is not described in HL. Germline mosaicism and consanguinity have no specific roles beyond general impacts on genetic diversity.

Founder effects for HL are poorly defined, as no single common germline variant has been implicated as causative. Carrier frequency of individual risk alleles, such as certain HLA types, may vary by population, but their contributions are modest and multigenic. Thus, HL’s inheritance pattern is best represented by MONDO and Orphanet terms for multifactorial disorders, with polygenic risk scores likely to emerge from future GWAS efforts.

### 9.3 Population Demographics and Geographic Distribution

Population demographics reveal that HL affects all ethnic groups but with differing subtype distributions and EBV association. In high‑income countries, NSHL in young adults predominates, often EBV‑negative; in some low‑income regions, EBV‑positive mixed cellularity HL in children and older adults is more common.[7] Male sex is associated with higher incidence overall, though some subtypes show less pronounced sex differences.[2][6]

Age distribution shows a peak in adolescence and young adulthood and a smaller peak in later adulthood, especially for EBV‑positive mixed cellularity HL.[2][6][7] Children and adolescents have excellent outcomes with modern therapy, while older adults may experience more treatment‑related toxicity and comorbidities, affecting survival. Geographic distribution of EBV‑positive HL aligns with EBV infection patterns, with early childhood infection prevalent in developing countries and delayed infection in high‑income settings.[7]

From a variant perspective, specific germline risk alleles may have different frequencies across populations, but HL’s rarity and multifactorial architecture mean that population‑specific HL genetic profiles are subtle. EBV’s ubiquity and HL’s rarity underscore that most infected individuals never develop HL, highlighting the importance of host genetics and other factors in modulating risk.

---

## 10. Diagnostics

### 10.1 Clinical and Laboratory Evaluation

Diagnosis of HL begins with clinical suspicion in patients presenting with lymphadenopathy, B symptoms, or unexplained systemic illness. Physical examination identifies enlarged lymph nodes, organomegaly, and potential mass effects. Laboratory testing includes CBC, ESR, CRP, LDH, liver and renal function tests, and sometimes beta‑2 microglobulin. IPS variables such as low albumin, low hemoglobin, lymphocytopenia, and high WBC count are assessed at diagnosis to inform prognosis.[2]

LOINC codes can represent these laboratory tests, while HPO terms annotate abnormalities. For example, elevated ESR corresponds to HP:0003565, anemia to HP:0001903, lymphopenia to HP:0001888, hypoalbuminemia to HP:0003073, and leukocytosis to HP:0001974. Laboratory evaluation is necessary but not sufficient for diagnosis, which hinges on tissue biopsy.

### 10.2 Imaging and FDG PET/CT: Deauville Scoring

Imaging plays a central role in staging and response assessment. CT scans of the neck, chest, abdomen, and pelvis visualize nodal and organ involvement. MRI can be used for specific anatomical regions. FDG PET/CT is integral to modern HL management, as it captures metabolic activity of tumor and microenvironment cells. A 2023 study emphasizes that “F-18 fluorodeoxyglucose (FDG) positron emission tomography (PET) using F-18 fluorodeoxyglucose (FDG) for treatment monitoring in patients with lymphoma is one of the most well-developed clinical applications,” and that “Deauville five-point score (DS) is recommended for response assessment in international guidelines.”[16]

The Deauville score uses visual comparison of FDG uptake in lesions to reference regions—mediastinum and liver. Score 1 denotes no uptake, 2 uptake less than or equal to mediastinum, 3 uptake greater than mediastinum but less than or equal to liver, 4 moderately increased uptake compared to liver, and 5 markedly increased uptake compared to liver or new lesions.[16] Score X denotes new areas of uptake unlikely to be related to lymphoma.[16] Interim PET negativity (DS 1–3) is associated with favorable outcomes and supports de‑escalation of therapy, while DS 4–5 suggests inadequate response.[16] The study confirmed that DS is a useful tool with good positive and negative predictive values and demonstrated good inter‑observer agreement.[16]

Imaging phenotypes are encoded in RadLex terms for FDG PET and CT, while the Deauville score is an assessment tool. NCIT includes terms for “Positron Emission Tomography” and “PET Response Criteria”. The knowledge base should note that FDG PET/CT is used for staging, interim response assessment, and end‑of‑treatment evaluation.

### 10.3 Histopathology and Immunohistochemistry

Definitive diagnosis of HL requires excisional lymph node biopsy or adequate core tissue, followed by histopathologic examination and immunohistochemistry. Pathology Outlines emphasizes that cHL is characterized by malignant HRS cells derived from preapoptotic germinal center B cells and describes NSHL as a subtype with collagen bands and lacunar cells.[8] HRS cells display more lobated nuclei, smaller lobes, less prominent nucleoli, and more cytoplasm than other types of cHL, and lacunar cells are associated with necrosis and histiocytes.[8]

Immunophenotypically, cHL HRS cells are typically CD30+, CD15+, PAX5+, and CD20–/weak, with negative or weak expression of B‑cell transcription factors OCT2 and BOB1.[8][13] NLPHL LP cells, by contrast, are CD20+, CD45+, PAX5+, OCT2+, BCL6+, CD15–, and CD30 variable.[15] Background cells in NLPHL include TFH cells expressing CD4, PD‑1, BCL6, ICOS, and CXCL13.[15] Pathology Outlines notes that “LP cells preserve the B cell program and express B cell markers, including OCT2,” underscoring their distinct biology.[15]

These immunophenotypes are essential for distinguishing HL from non‑Hodgkin lymphomas such as diffuse large B‑cell lymphoma and T‑cell lymphomas. SNOMED CT can encode pathology diagnoses, while NCIT terms capture immunophenotypic markers. The knowledge base should represent classical HL and NLPHL as distinct entities with characteristic histologic and immunophenotypic features.

### 10.4 Genetic and Molecular Diagnostics

Genetic testing is not routinely used for HL diagnosis in clinical practice, as histopathology and immunohistochemistry are usually sufficient. However, molecular diagnostics such as EBV in situ hybridization (EBER ISH) can detect EBV in HRS cells, distinguishing EBV‑positive from EBV‑negative HL.[7] FISH or array CGH can identify 9p24.1 amplification, PD‑L1/PD‑L2 copy gains, and JAK2 amplification in research settings or specialized centers.[12] Next‑generation sequencing panels can detect somatic mutations in JAK–STAT pathway components, NF‑κB regulators, and other genes.[11]

Whole exome or genome sequencing of tumor tissue is more commonly used in research than routine care but may inform targetable lesions in clinical trials. Germline genetic testing is not standard, as no single causative variant exists. Mitochondrial DNA testing, chromosomal microarray, and karyotyping have limited utility in HL unless other syndromes are suspected. RNA sequencing can profile gene expression and identify fusion genes or transcriptomic signatures, while epigenomic profiling can illuminate chromatin changes.[13][14]

Liquid biopsy via circulating tumor DNA or cell‑free RNA is under investigation in HL but has yet to become mainstream diagnostic practice. For the knowledge base, it is important to note that while molecular diagnostics are expanding, histopathology remains the cornerstone of HL diagnosis.

### 10.5 Clinical Criteria and Differential Diagnosis

Standardized diagnostic criteria for HL are based on WHO classifications and clinical guidelines. Diagnosis requires compatible histology and immunophenotype in tissue biopsy, supportive clinical and imaging findings, and exclusion of other lymphoid neoplasms. ICD‑10 codes (C81.x) and ICD‑11 equivalents are used for coding.[5] Differential diagnosis includes non‑Hodgkin lymphoma (MeSH “Lymphoma, Non-Hodgkin”), reactive lymphadenitis, infectious mononucleosis, and other granulomatous diseases.[4] Distinguishing features include the presence of HRS or LP cells, immunophenotype, and architectural patterns.

Non‑Hodgkin lymphomas, such as diffuse large B‑cell lymphoma, peripheral T‑cell lymphomas, and anaplastic large‑cell lymphomas, may mimic HL clinically and histologically, but immunophenotypic differences and gene rearrangement studies help differentiate them. For example, ALCL is CD30+ but usually ALK+ and lacks B‑cell markers, whereas cHL HRS cells show weak PAX5 and variable B‑cell markers. EBV‑positive lymphomas can mimic HL; careful EBER ISH and immunophenotyping are necessary.

Screening for HL in asymptomatic individuals is not recommended, as disease is rare and screening tests are invasive or costly. However, high‑risk groups such as HIV‑infected individuals or those with strong family history may require heightened clinical vigilance.

---

## 11. Outcome and Prognosis

### 11.1 Survival and Mortality

With modern therapy, HL is one of the most curable adult cancers. SEER data indicate that five‑year relative survival rates for HL are high, often exceeding 85–90%, varying by stage, age, and subtype.[6] Death rates have fallen on average 2.3% each year over 2014–2023.[6] Nonetheless, some patients die from refractory disease, relapse, or treatment‑related complications.

For relapsed cHL treated with auto‑HCT, outcomes remain favorable but with increased late mortality. A large study of 1,617 patients (cHL and diffuse large B‑cell lymphoma) who survived progression‑free for ≥2 years after auto‑HCT found that “the 5-year overall survival rate was 90% (95% confidence interval [CI], 87%-92%) for patients with cHL,” but the risk of late mortality compared with the general population was 9.6‑fold higher (standardized mortality ratio 9.6).[17] Relapse accounted for 44% of late deaths; other causes included second malignant neoplasms and organ toxicity.[17] Late effects were reported in 9% of patients, and 105 second malignancies occurred.[17] These data underscore that while immediate post‑transplant outcomes are excellent, long‑term survivorship is complicated by residual disease risk and late effects.

In older adults and EBV‑positive HL, survival is more limited. The EBV review notes that among patients older than 50 years, EBV positivity is associated with significantly poorer outcomes.[7] Comorbidities, decreased tolerance for intensive therapy, and higher risk of treatment toxicity contribute. Nonetheless, PD‑1 blockade and other newer therapies are improving outcomes in relapsed/refractory settings, as discussed below.[18][19]

### 11.2 Morbidity, Function, and Quality of Life

Morbidity in HL arises from both disease and treatment. During active disease, B symptoms, fatigue, pain, and psychological distress impair quality of life. Chemotherapy and radiotherapy cause acute toxicities such as nausea, vomiting, alopecia, mucositis, neutropenia, and risk of infection. Long‑term, survivors face increased risk of cardiopulmonary disease (anthracycline cardiomyopathy, radiation‑induced heart disease, pulmonary fibrosis), endocrine dysfunction (hypothyroidism, hypogonadism), infertility (particularly with alkylating agents), and second cancers (breast, lung, gastrointestinal, and myeloid malignancies).[17]

Quality of life measurements using instruments like SF‑36 and EQ‑5D show that physical and emotional domains may remain impaired years after treatment, especially in those with late effects or chronic fatigue. Psychosocial issues include anxiety, depression, fear of relapse, and challenges in work or school reintegration. Adolescent and young adult survivors may face unique challenges in education, employment, relationships, and fertility, requiring tailored survivorship care.

Disability outcomes vary. Many survivors return to full function, but some experience functional impairments due to cardiopulmonary disease, neuropathy, or chronic fatigue. Late effects such as second malignancies can impose additional morbidity and mortality. The auto‑HCT study highlights that older age, male sex, Karnofsky score <90, total body irradiation exposure, and more lines of pre‑transplant chemotherapy are risk factors for overall mortality in cHL.[17] These variables reflect patient fitness, treatment intensity, and cumulative toxicity.

### 11.3 Prognostic Factors and Biomarkers

Prognostic factors in HL include clinical, laboratory, and molecular variables. The International Prognostic Score (IPS) includes seven risk factors: male sex, age >45 years, stage IV disease, serum albumin <4 g/dL, hemoglobin <10.5 g/dL, lymphocytopenia, and WBC count >15,000/mm³.[2] The more factors present, the less favorable the prognosis.[2] Bulky mediastinal disease, B symptoms, elevated LDH, and certain histological subtypes also worsen prognosis.

Molecular prognostic biomarkers include EBV status, PD‑L1/PD‑L2 amplification, JAK–STAT mutations, and microenvironment profiles. EBV positivity in young adults may confer marginally improved prognosis, whereas in older adults it portends poorer outcomes.[7] PD‑L1/PD‑L2 amplification and JAK2 co‑amplification, while driving immune evasion, also predict sensitivity to PD‑1 blockade.[12][18][19] Gene expression signatures reflecting microenvironment composition and immune exhaustion may stratify patients for immunotherapies and predict response.

Imaging biomarkers such as interim PET negativity (DS 1–3) are powerful predictors of outcome. The Deauville score aids treatment adaptation, with interim PET negative patients eligible for de‑escalation and PET‑positive patients requiring intensification.[16] The validation study confirms that DS has good positive and negative predictive values and good inter‑observer agreement.[16] These imaging biomarkers, combined with clinical and molecular factors, enable increasingly personalized prognostication.

---

## 12. Treatment

### 12.1 Standard Pharmacotherapy: Chemotherapy and Radiotherapy

First‑line treatment for HL typically involves combination chemotherapy with or without involved‑site radiotherapy. The classic regimen ABVD comprises Adriamycin (doxorubicin, CHEBI:28748), Bleomycin (CHEBI:28619), Vinblastine (CHEBI:3478), and Dacarbazine (CHEBI:53450), administered every 28 days for several cycles. This regimen cures the majority of patients with limited or advanced disease, particularly when combined with risk‑adapted radiotherapy.

More intensive regimens such as escalated BEACOPP (Bleomycin, Etoposide, Adriamycin, Cyclophosphamide, Vincristine, Procarbazine, Prednisone) are used in high‑risk patients but carry greater toxicity. Treatment algorithms based on IPS, stage, and interim PET results guide selection between ABVD, BEACOPP, and other regimens. NCIT terms such as “Doxorubicin Hydrochloride” (NCIT:C62000), “Bleomycin Sulfate” (NCIT:C28944), “Vinblastine Sulfate” (NCIT:C906), and “Dacarbazine” (NCIT:C29029) correspond to these drugs.

Radiotherapy is used for involved‑site control, particularly in early‑stage disease and bulky mediastinal masses. Modern techniques aim to minimize exposure of heart, lungs, breasts, and thyroid to reduce late effects. Dose and field selection are guided by clinical guidelines and imaging. NCIT includes “Radiation Therapy” (NCIT:C15313) and specific modalities.

Pharmacogenomics in HL is less prominent than in solid tumors, but variants in drug metabolism genes (e.g., CYP450, TPMT, UGTs) may influence toxicity. For example, anthracycline cardiotoxicity risk may be modulated by polymorphisms in NADPH oxidase and other pathways. PharmGKB and CPIC provide guidelines for some agents, but HL‑specific pharmacogenomics remains an emerging area.

### 12.2 Advanced Therapeutics: Auto‑HCT and Cellular Therapies

Autologous hematopoietic cell transplantation (auto‑HCT) is standard for relapsed or refractory cHL after first‑line therapy. Patients receive high‑dose chemotherapy (e.g., BEAM: Carmustine, Etoposide, Cytarabine, Melphalan) followed by reinfusion of autologous hematopoietic stem cells. The auto‑HCT study shows that two‑year progression‑free survivors have excellent five‑year OS but increased late mortality compared with the general population.[17] Risk factors for mortality include older age, male sex, low Karnofsky score, total body irradiation, and multiple pre‑transplant chemotherapy lines.[17]

Cellular therapies such as CAR‑T cells targeting CD30 or other antigens are in early‑phase trials for HL. Allogeneic stem cell transplantation is reserved for highly refractory cases but carries significant risk of graft‑versus‑host disease and infection. These interventions correspond to NCIT terms like “Autologous Hematopoietic Stem Cell Transplantation” (NCIT:C15206) and “CAR T-Cell Therapy” (NCIT:C154102).

### 12.3 Targeted Therapies: Brentuximab Vedotin and JAK Inhibitors

Brentuximab vedotin, an antibody–drug conjugate targeting CD30 (NCIT:C3016 “CD30 antigen”), is an important targeted therapy in HL. It delivers the microtubule‑disrupting agent monomethyl auristatin E to CD30‑expressing HRS cells, leading to cell death. Brentuximab is used in relapsed cHL and in some first‑line regimens combined with AVD (Adriamycin, Vinblastine, Dacarbazine), replacing bleomycin to reduce pulmonary toxicity. Clinical trials have shown improved progression‑free survival with brentuximab‑containing regimens in certain risk groups.

JAK inhibitors such as ruxolitinib and other agents have been proposed as therapies for cHL due to pervasive JAK–STAT pathway activation. The exome study notes that “the pervasive targeting of JAK-STAT signaling genes in cHL makes clinically available JAK or STAT inhibitors an attractive therapeutic approach in this disease in the context of a comprehensive targeted genotyping of patients.”[11] JAK2 amplification and its role in PD‑L1/PD‑L2 induction further support this strategy.[12] Clinical trials of JAK inhibitors in HL are ongoing but less mature than PD‑1 blockade trials.

### 12.4 Immunotherapies: PD‑1 Checkpoint Inhibitors

PD‑1 checkpoint inhibitors have revolutionized treatment of relapsed/refractory cHL. Nivolumab, a human IgG4 PD‑1 monoclonal antibody, was studied in the phase 2 CheckMate 205 trial for patients whose auto‑HCT had failed and who had received brentuximab.[18] The updated five‑year follow‑up reports that “patients with relapsed/refractory (R/R) classical Hodgkin lymphoma (cHL) for whom autologous hematopoietic cell transplantation (auto-HCT) had failed experienced frequent and durable responses to nivolumab,” with an objective response rate (ORR) of 71.2% and complete remission (CR) rate of 21.4%.[18] Median duration of response was 18.2 months, median progression‑free survival 15.1 months, and median overall survival not reached, with OS at five years of 71.4%.[18] No new or unexpected safety signals emerged, and the study concluded that “This 5-year follow-up of CheckMate 205 demonstrated favorable OS and confirmed efficacy and safety of nivolumab in R/R cHL after auto-HCT failure. Results suggest patients may discontinue treatment after persistent CR and reinitiate upon progression.”[18]

Pembrolizumab, another PD‑1 monoclonal antibody, showed similar efficacy in KEYNOTE‑087. The five‑year follow‑up reports that “Previous analyses of the phase 2 KEYNOTE-087 trial of pembrolizumab monotherapy demonstrated effective antitumor activity with acceptable safety in patients with relapsed or refractory (R/R) classical Hodgkin lymphoma (cHL).”[19] With median follow‑up of 63.7 months, ORR was 71.4% with CR 27.6% and partial response 43.8%.[19] Median duration of response was 16.6 months, and median progression‑free survival 13.7 months.[19] A quarter of responders, including half of complete responders, maintained response for ≥4 years. Among 20 patients receiving second‑course pembrolizumab after relapse from initial CR, ORR was 73.7% and median DOR 15.2 months.[19] Any‑grade treatment‑related adverse events occurred in 72.9% of patients, grade 3–4 events in 12.9%, and no treatment‑related deaths occurred.[19] The authors concluded that “Single-agent pembrolizumab can induce durable responses, particularly in patients achieving CR. Second-course pembrolizumab frequently reinduced sustained responses after relapse from initial CR.”[19]

These results reflect the underlying biological rationale: HRS cells overexpress PD‑L1 and PD‑L2 due to 9p24.1 amplification and JAK2‑mediated induction, and tumor‑infiltrating T cells express PD‑1, making the PD‑1 pathway a key immune‑evasion mechanism.[12] PD‑1 blockade releases inhibitory brakes on T cells, allowing effective anti‑tumor responses. NCIT includes “Nivolumab” (NCIT:C104801) and “Pembrolizumab” (NCIT:C116709) as immunotherapeutic agents.

### 12.5 Experimental and Emerging Therapies

Experimental therapies in HL include CAR‑T cells targeting CD30, bispecific antibodies, novel checkpoint inhibitors (e.g., anti‑LAG3, anti‑TIM3), and combination regimens integrating PD‑1 blockade with chemotherapy, radiotherapy, or other targeted agents. Trials explore PD‑1 inhibitors in earlier lines of therapy and in combination with brentuximab or AVD. JAK inhibitors, epigenetic drugs, and small‑molecule NF‑κB inhibitors are under investigation.

RNA‑based therapies, such as siRNA or antisense oligonucleotides targeting specific oncogenes, remain primarily in preclinical stages. Gene therapy is not a primary modality in HL. Functional genomics screens inform potential targets for drug development, and precision medicine approaches aim to tailor therapy based on tumor mutational and microenvironmental profiles.

Treatment strategies increasingly emphasize response‑adapted therapy. Interim PET/CT using Deauville scoring guides de‑escalation or escalation of chemotherapy regimens.[16] PD‑1 blockade is used after auto‑HCT failure or in brentuximab‑refractory disease, and some patients may discontinue PD‑1 therapy after persistent CR and resume upon relapse.[18][19] Personalized medicine approaches may incorporate PD‑L1/PD‑L2 copy number, JAK–STAT mutations, and microenvironmental signatures to refine decisions.

---

## 13. Prevention

### 13.1 Primary Prevention

Primary prevention of HL is challenging due to its multifactorial etiology and the ubiquity of EBV infection. No vaccine against EBV is currently licensed, though vaccine development is ongoing and may eventually contribute to HL prevention, particularly EBV‑positive subtypes. Preventing delayed EBV infection and infectious mononucleosis—through environmental or behavioral interventions—is not currently feasible at population level. General measures to maintain immune health, such as HIV prevention and treatment, may reduce HL risk in immunocompromised populations.

Avoiding unnecessary immunosuppression and optimizing management of immunosuppressive therapies can reduce HL risk in high‑risk settings such as organ transplantation. Environmental interventions to reduce exposure to potential carcinogens (e.g., certain solvents or pesticides) may have marginal impact but are not established HL‑specific strategies.

### 13.2 Secondary Prevention: Early Detection and Risk Stratification

Secondary prevention focuses on early detection and intervention to improve outcomes. Routine screening for HL in asymptomatic individuals is not recommended, given its rarity and lack of simple, non‑invasive screening tests. However, heightened clinical awareness and prompt evaluation of persistent lymphadenopathy and B symptoms can lead to earlier diagnosis. In HIV‑infected individuals and other immunocompromised patients, regular clinical follow‑up and vigilance for lymphoproliferative disorders are important.

Risk stratification based on IPS, stage, EBV status, and interim PET response guides treatment intensity and may prevent overtreatment or undertreatment. Interim PET negativity allows de‑escalation of chemotherapy, reducing toxicity, while PET positivity prompts intensification, potentially preventing relapse.[16] Genetic risk stratification via polygenic risk scores is not yet clinically available for HL.

### 13.3 Tertiary Prevention: Survivorship and Late Effects

Tertiary prevention in HL aims to prevent complications and late effects in those who have already been treated. Survivorship programs focus on monitoring and managing cardiopulmonary disease, endocrine dysfunction, fertility issues, and second malignancies. For auto‑HCT survivors, the study emphasizes that despite favorable survival, they “have an excess late-mortality risk in comparison with the general population and experience an assortment of late complications.”[17] Identifying and mitigating risk factors such as smoking, obesity, sedentary lifestyle, and uncontrolled hypertension can reduce cardiovascular morbidity. Screening for secondary breast cancer in women who received chest radiation, thyroid function testing, and colonoscopy for gastrointestinal malignancies are part of survivorship care.

Genetic counseling for families with HL aggregation may inform risk perceptions and encourage early evaluation of suspicious symptoms but cannot provide deterministic risk estimates. Counseling for fertility preservation, including sperm banking and oocyte or embryo freezing before intensive therapy, is an important component of tertiary prevention.

---

## 14. Other Species and Natural Disease

### 14.1 Veterinary Hodgkin’s‑Like Lymphoma

Hodgkin’s‑like lymphoma has been described in veterinary species, particularly dogs and cats, as a slow‑growing neoplasm usually affecting lymph nodes of the head and neck.[20] The cited article notes that “Hodgkin's-like lymphoma is a slow growing neoplasm, usually affecting the lymph nodes of the head and neck, which has been sporadically described in veterinary ...”[20] These lesions share histopathologic similarities with human HL, including large atypical cells in a mixed inflammatory background, but may differ in immunophenotype and clinical behavior.

In dogs, Hodgkin‑like lymphoma often presents as localized disease, with nodular architecture and chronic progression. Veterinary relevance includes differential diagnosis of lymphadenopathy, treatment with chemotherapy or surgery, and implications for animal health and welfare. OMIA and veterinary databases catalog such conditions, but their prevalence is low.

### 14.2 Comparative Pathology and Evolutionary Considerations

Comparative pathology highlights similarities and differences across species. Hodgkin‑like lesions in animals show that certain lymphoma patterns can arise in diverse mammalian hosts, suggesting conserved mechanisms of lymphoid transformation. EBV‑like viruses in animals (e.g., gammaherpesviruses) may play roles in some cases, but evidence is limited. Evolutionary conservation of genes involved in HL, such as JAK–STAT components, NF‑κB regulators, and PD‑1/PD‑L1, is high, reflecting their fundamental roles in immune regulation.

Comparative studies may use model organisms such as mice with humanized immune systems to study EBV infection and HL‑like processes. HomoloGene and Alliance of Genome Resources can link human HL genes to orthologs in mice, zebrafish, and other species. These cross‑species perspectives inform basic science but have limited direct clinical impact.

### 14.3 Transmission and Zoonotic Potential

HL is not a transmissible disease. EBV infection is transmissible, but developing HL requires additional host and environmental factors. There is no zoonotic HL disease, and Hodgkin‑like lymphomas in animals are not transmitted to humans. Zoonotic potential is thus negligible. Disease knowledge bases may note that HL is non‑infectious in itself, though associated with an infectious agent in some cases.

---

## 15. Model Organisms

### 15.1 Cell Line Models

Cell lines derived from HL, such as L‑428, KM‑H2, L‑540, and others, are widely used as models to study HRS cell biology, signaling pathways, and drug responses. The 9p24.1 amplification study used a “lymphoma cell line panel” to identify amplification of chromosome 9p24.1, PD‑L1/PD‑L2 expression, and JAK2 co‑amplification.[12] These cell lines allow manipulation of JAK–STAT and NF‑κB pathways, EBV infection status, and PD‑1 ligand expression. They are in vitro models that recapitulate many features of HRS cells but lack full microenvironmental complexity.

Functional genomics screens using CRISPR or RNAi in HL cell lines have identified essential genes in JAK–STAT, PD‑1 ligand, and NF‑κB pathways, confirming their roles in survival and immune evasion.[11] Cell line models are essential for preclinical testing of targeted therapies, including JAK inhibitors, PD‑1/PD‑L1 blockers, and CD30‑targeting agents.

### 15.2 Mouse and Humanized Models

Mouse models of HL are less established than for other lymphomas, because HRS cells are difficult to reproduce in murine systems. Humanized mouse models engrafted with human immune systems and EBV infection have been used to study EBV‑related lymphoproliferative diseases, including HL‑like lesions in certain settings. Transgenic mice expressing LMP1 or other EBV genes in B cells can develop lymphoproliferative disorders, providing insights into EBV‑mediated transformation.[7]

Mouse models with targeted disruptions or overexpression of JAK–STAT pathway components, NF‑κB regulators, or epigenetic modifiers can model aspects of HL pathophysiology. However, these models often develop other lymphoma subtypes or autoimmune phenomena rather than bona fide HL. Their limitations include species differences in immune system and germinal center dynamics and difficulty in recapitulating the complex HL microenvironment.

### 15.3 Applications and Limitations

Model organisms and cell lines enable study of HL mechanisms, drug testing, and biomarker discovery. Cell lines allow detailed dissection of signaling and gene expression, while mouse models permit in vivo investigation of immune responses, microenvironment, and therapy. Nonetheless, no model fully recapitulates HL’s unique histopathology, microenvironment, and EBV association in humans.

Limitations include differences in EBV biology between humans and animals, incomplete reproduction of fibrosis and nodular sclerosis, and simplified microenvironments. Organoid and iPSC‑based models are emerging but remain experimental. Knowledge bases should note that HL research often relies on combined use of cell lines, human tissue samples, and limited animal models.

---

## Conclusion

Hodgkin lymphoma is a rare but highly curable B‑cell–derived lymphoma that exemplifies the complex interplay of viral infection, somatic genetic lesions, epigenetic reprogramming, and tumor–microenvironment crosstalk in cancer pathogenesis. Classical Hodgkin lymphoma arises from preapoptotic germinal center B cells that undergo malignant transformation through constitutive activation of JAK–STAT and NF‑κB pathways, often driven by EBV latent proteins or somatic mutations in STAT6, SOCS1, JAK1, JAK2, TNFAIP3, and related genes.[7][11] Epigenetic silencing of B‑cell gene expression programs via histone deacetylation, H3K27 trimethylation, and DNA methylation reinforces an abortive plasma cell differentiation state, making HRS cells phenotypically distinct from their precursors.[13] Immune‑evasion mechanisms, including 9p24.1 amplification of PD‑L1/PD‑L2 and JAK2, antigen presentation defects, and microenvironmental immunosuppression, allow HRS cells to persist despite a highly immunogenic profile.[11][12]

Clinically, HL presents with lymphadenopathy, B symptoms, and characteristic histopathological patterns distinguishing classical and nodular lymphocyte predominant subtypes.[2][8][9][15] Diagnostic work‑up integrates physical examination, laboratory tests, histopathology, immunohistochemistry, and FDG PET/CT using the Deauville score to stage disease and guide response‑adapted therapy.[16] Prognosis is generally excellent, with modern chemotherapy regimens such as ABVD and involved‑site radiotherapy curing most patients and five‑year relative survival exceeding 85–90%.[6] However, relapsed and refractory disease requires salvage therapy and auto‑HCT, and survivors face late effects and increased risk of second malignancies.[17]

Recent advances highlight HL’s responsiveness to immunotherapy. PD‑1 checkpoint inhibitors nivolumab and pembrolizumab produce high objective response rates (~71%), durable remissions, and favorable overall survival in heavily pretreated relapsed/refractory cHL, reflecting the centrality of PD‑1 ligand–mediated immune evasion.[18][19] These therapies, along with targeted agents such as brentuximab vedotin and emerging JAK inhibitors, illustrate a shift toward biologically rational, personalized interventions. Single‑cell and multi‑omics studies deepen understanding of HL’s microenvironment and molecular circuitry, pointing toward future precision medicine approaches that integrate mutational, copy number, epigenetic, and microenvironmental features.[11][12][13][14]

For knowledge‑base construction, HL can be represented using MONDO:0004952 and related ontology terms, with phenotype annotations (HPO), gene/protein annotations (HGNC, UniProt), cell types (CL), anatomical locations (UBERON), and treatments (NCIT). Disease characteristics include multifactorial etiology with EBV and somatic lesions, distinctive histopathology and immunophenotype, excellent curability with standard therapy, and evolving treatment paradigms incorporating response‑adapted chemotherapy, auto‑HCT, and PD‑1 blockade. Remaining challenges include optimizing long‑term survivorship, reducing late effects, understanding and mitigating resistance to immunotherapies, and clarifying germline genetic risk architecture. Hodgkin lymphoma thus remains both a clinical success story and a rich field for ongoing translational and mechanistic research.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |

All extracted references resolved successfully.