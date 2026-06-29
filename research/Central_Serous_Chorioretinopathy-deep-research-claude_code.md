---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-4-6
cached: false
start_time: '2026-06-25T12:07:39.438823'
end_time: '2026-06-25T12:17:28.082107'
duration_seconds: 588.64
template_file: templates\disease_pathophysiology_research.md
template_variables:
  disease_name: Central Serous Chorioretinopathy
  mondo_id: ''
  category: Complex
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
  - claude-sonnet-4-6
  num_turns: 5
  total_cost_usd: 1.2503657
  session_id: 10bb6955-7a19-477c-9e2e-781da3ee768b
  stop_reason: end_turn
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Central Serous Chorioretinopathy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Central Serous Chorioretinopathy** covering all of the
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

Here is the comprehensive research report on **Central Serous Chorioretinopathy (CSCR)**:

---

# CSCR Research Report

> **Important:** All PMIDs below are from training knowledge and must be verified with `just fetch-reference PMID:XXXXX` before writing any snippet into the YAML. Priority fetch list is at the end.

---

## 1. Disease Information

| Field | Value |
|---|---|
| MONDO | MONDO:0018616 |
| ORPHA | ORPHA:443079 |
| ICD-10 | H35.7 |
| ICD-11 | 9B75.2 |
| MeSH | D056833 |
| UMLS | C0730328 |
| OMIM | No single entry — complex/multifactorial, no classic Mendelian form |
| MedDRA | 10086644 |

**Synonyms:** Central serous retinopathy (CSR), CSCR, CSC, central serous chorioretinitis (historical), idiopathic central serous chorioretinopathy.

CSCR is classified by Orphanet as a rare choroidal disorder, but is actually the **fourth most common retinal disorder** in adults after AMD, diabetic retinopathy, and branch retinal vein occlusion — particularly prevalent in young to middle-aged males.

---

## 2. Etiology & Risk Factors

### Genetic Risk Factors (GWAS findings)

| Gene/Locus | Variant | OR | PMID |
|---|---|---|---|
| **CFH** (1q32) | rs800292 (I62V) | ~1.6–1.8 | PMID:25939894 |
| **CFH** (1q32) | rs1061170 (Y402H) | ~1.4 | PMID:25939894 |
| **ARMS2/HTRA1** (10q26) | rs10490924 | ~1.4 | PMID:29515099 |
| **NR3C2** (4q31.1) | regulatory variant | — | PMID:34385711 |
| **KCNJ13** (2q37) | regulatory variant | — | PMID:34385711 |
| **GATA5** (18q11.2) | rs6141806 | — | PMID:31712692 |

Key point: CFH and ARMS2/HTRA1 are the **same loci** associated with AMD — CSCR and AMD share genetic architecture at Bruch membrane/choroidal vascular vulnerability genes.

### Environmental Risk Factors

- **Corticosteroids (strongest modifiable risk):** ~10–40× increased risk; all routes (systemic > intranasal > inhaled > topical skin > epidural). Even brief high-dose burst courses are sufficient. PMID:25654734 (pharmacoepidemiology), PMID:17702499 (review).
- **Psychosocial stress / Type A personality:** Chronic HPA axis activation → elevated cortisol → MR activation. PMID:15897545.
- **Obstructive sleep apnea:** OR ~2–4; intermittent hypoxia + cortisol dysregulation. PMID:23736878.
- **Pregnancy:** Third trimester; elevated placental CRH and cortisol. Usually resolves postpartum. PMID:8778938.
- **H. pylori:** Multiple case-control studies show association; eradication may help but data conflicting. Controversial.
- **Endogenous Cushing syndrome:** CSCR can be the presenting feature — check cortisol in severe/bilateral cases.

### Mineralocorticoid Receptor Pathway (detailed mechanism)

In choroidal endothelial cells, **11β-HSD2 expression is low**, so cortisol is not inactivated locally and freely activates **NR3C2** (mineralocorticoid receptor):
1. MR nuclear translocation → upregulates **VEGF-A** → VEGFR2 phosphorylation of VE-cadherin → junction opening → hyperpermeability
2. Upregulates **AQP1** (aquaporin-1) → increased transendothelial water flux
3. Upregulates **SERPINE1** (PAI-1) → fibrin deposition in choroid
4. Downregulates tight junction proteins (occludin, claudin-5)

Seminal mechanistic paper: PMID:22446627 (Zhao et al. 2012, *J Clin Invest* — mineralocorticoid receptor in rat and human chorioretinopathy).

---

## 3. Phenotypes (with HPO terms and frequencies)

| Phenotype | HPO Term | Frequency | Clinical Details |
|---|---|---|---|
| Visual impairment / blurred central vision | HP:0000505 | VERY_FREQUENT (>90%) | VA 20/20 to 20/200; often mild in acute |
| Metamorphopsia | HP:0012508 | FREQUENT (60–80%) | Wavy/distorted lines; Amsler grid test |
| Micropsia | HP:0012508 (best fit) / HP:0000505 | FREQUENT (50–70%) | Objects appear smaller; photoreceptor displacement |
| Relative central scotoma | HP:0000575 | FREQUENT (60–80%) | Relative, not absolute |
| Reduced contrast sensitivity | HP:0007663 | FREQUENT (60–80%) | Often disproportionate to Snellen acuity |
| Hypermetropic shift | HP:0000540 | FREQUENT (>70%) | 0.5–2.0 diopters; retinal elevation shortens focal length |
| Dyschromatopsia / color vision deficit | HP:0000551 | OCCASIONAL (30–50%) | Blue-yellow axis; Farnsworth-Munsell testing |
| Photopsia | HP:0030786 | OCCASIONAL (20–40%) | Brief flashes; mechanical photoreceptor stimulation |
| Nyctalopia / impaired dark adaptation | HP:0000662 | OCCASIONAL (20–40%) | Especially in chronic CSCR with rod involvement |
| Abnormal multifocal ERG | HP:0000580 | FREQUENT in chronic | Reduced macular responses; central P1 amplitude |

**Note on micropsia:** Orphanet explicitly lists micropsia as a CSCR symptom (ORPHA:443079 definition). HPO:HP:0012508 (Metamorphopsia) is the closest; add preferred_term "Micropsia" with a note. Consider also HP:0012508 with a modifier.

**Subtype-specific notes:**
- **Acute CSCR:** Acute monocular onset; VA often 20/30–20/60; spontaneous improvement expected
- **Chronic CSCR:** Bilateral in ~40%; "descending RPE tracks" (gravity-dependent atrophy); cystoid macular degeneration; subretinal fibrin/precipitates; choroidal neovascularization

---

## 4. Genetics / Molecular (detailed)

### CFH polymorphisms
- **rs800292 (I62V):** Risk allele reduces CFH's C3b binding and factor I cofactor activity → less complement regulation at choroidal Bruch membrane → C5a-mediated mast cell degranulation → histamine → permeability increase
- **rs1061170 (Y402H):** Reduces CFH binding to heparan sulfate in choroid → impaired local complement regulation

### Key GWAS papers
1. **PMID:25939894** — Schellevis 2015, *J Med Genet*: First CSCR GWAS (170 cases); CFH rs800292 genome-wide significant (OR 1.59)
2. **PMID:29515099** — Schellevis 2018, *Ophthalmology*: Expanded GWAS (~750 cases); confirmed CFH + new hit ARMS2/HTRA1 (rs10490924, OR 1.38)
3. **PMID:31712692** — Hosoda 2020, Japanese GWAS: GATA5 locus; pachychoroid disease spectrum
4. **PMID:34385711** — Large European meta-GWAS (>4,200 cases): confirmed CFH, ARMS2/HTRA1; novel hits NR3C2, KCNJ13 (**verify this PMID**)

### NR3C2 variants
GWAS signal is regulatory (non-coding). Rare gain-of-function NR3C2 coding variants reported in familial CSCR cases. Supports constitutive MR hyperactivity as genetic risk mechanism.

### KCNJ13
Encodes Kir7.1 inwardly rectifying potassium channel in RPE basolateral membrane. Coding mutations cause Leber congenital amaurosis (monogenic). GWAS variants in CSCR suggest subtler RPE ion transport dysregulation.

### No monogenic/Mendelian form established. No CNV/chromosomal abnormalities implicated.

---

## 5. Pathophysiology (Detailed Causal Chain)

### Node 1: Choroidal Hyperpermeability and Pachychoroid Phenotype
**Cell type:** CL:0000115 (endothelial cell; preferred_term "choroidal endothelial cell")
**Biological processes:**
- GO:0043117 (positive regulation of vascular permeability) — INCREASED
- GO:0042921 (glucocorticoid receptor signaling pathway)
- GO:0045944 (positive regulation of transcription by RNA polymerase II) — MR-mediated

**Pachychoroid structural predisposition:**
- Dilated outer choroidal vessels (Haller layer "pachyvessels" >200 μm on EDI-OCT)
- Compressed inner choroidal layers (Sattler layer, choriocapillaris)
- Mean subfoveal choroidal thickness (SFCT) ~450–500 μm in CSCR vs ~280 μm controls

**Mechanism:** Cortisol → NR3C2 activation → VEGF-A ↑ + AQP1 ↑ + tight junction proteins ↓ → choroidal vascular hyperpermeability. CFH deficiency → complement C3b on choroidal endothelium → C5a → mast cell histamine → amplified permeability.

→ **downstream:** Retinal Pigment Epithelium Dysfunction

### Node 2: Retinal Pigment Epithelium Dysfunction
**Cell type:** CL:0002586 (retinal pigment epithelial cell)
**Biological processes:**
- GO:0006811 (monoatomic ion transport) — DECREASED (Na⁺/K⁺-ATPase failure)
- GO:0070588 (calcium ion transmembrane transport) — disrupted
- GO:0045087 (innate immune response) — complement deposition on RPE basal surface

**Key events:**
- Hydrostatic pressure from hyperpermeant choriocapillaris → RPE tight junction disruption (occludin, ZO-1, claudin-19 ↓)
- Focal RPE detachments → serous pigment epithelial detachments (PEDs)
- SERPINE1 (PAI-1) upregulation → fibrin deposition in sub-RPE space
- Chronic: diffuse RPE atrophy, "descending tracks" on FA

→ **downstream:** Subretinal Fluid Accumulation and Macular Detachment

### Node 3: Subretinal Fluid Accumulation and Photoreceptor Damage
**Cell types:**
- CL:0000210 (photoreceptor cell)
- CL:0000573 (retinal cone cell) — most metabolically vulnerable; foveal cones first affected
- CL:0000604 (retinal rod cell) — impaired dark adaptation in chronic

**Biological processes:**
- GO:0007601 (visual perception) — DECREASED
- GO:0007602 (phototransduction) — DECREASED
- GO:0006915 (apoptotic process) — INCREASED in chronic disease (photoreceptor death)
- GO:0001525 (angiogenesis) — INCREASED in CNV complication

**Key events:**
- Neurosensory retinal detachment → photoreceptor outer segment disruption
- Ellipsoid zone (EZ) disruption on OCT = marker of photoreceptor outer segment integrity loss
- Outer nuclear layer (ONL) thinning on OCT = photoreceptor cell body loss
- In acute: reversible upon SRF resolution
- In chronic: irreversible photoreceptor loss, permanent VA reduction

### Node 4 (Complication): Choroidal Neovascularization
- Chronic RPE atrophy + Bruch membrane damage → VEGF-A ↑ → angiogenesis
- Type 1 (sub-RPE) CNV develops in ~5–10% chronic CSCR over 5 years
- Evolution to pachychoroid neovasculopathy spectrum

---

## 6. Diagnostics

### OCT (primary diagnostic tool)
- Subfoveal fluid (SRF): hyporeflective space under neurosensory retina
- Pigment epithelial detachments (PEDs): dome-shaped RPE elevation
- Ellipsoid zone (EZ) disruption: photoreceptor outer segment loss
- Outer nuclear layer (ONL) thinning: photoreceptor cell loss
- SFCT measurement: >300–350 μm indicates pachychoroid

### Fluorescein Angiography (FA)
- "Smoke-stack" pattern (~10–20%): single leakage point with upward mushroom-cloud expansion
- "Ink-blot" pattern (~80%): gradually expanding spot of hyperfluorescence
- "Descending RPE tracks" in chronic: gravity-dependent RPE decompensation

### Indocyanine Green Angiography (ICGA)
- Early: choroidal hyperpermeability zones
- Late: persistent hyperfluorescence of dilated pachyvessels
- Essential for: treatment planning (PDT spot targeting), distinguishing CNV from pure CSCR

### OCT-Angiography (OCT-A)
- Choriocapillaris flow deficits under SRF area
- CNV detection (type 1 sub-RPE flow signal)
- No dye required

### Enhanced Depth Imaging OCT (EDI-OCT)
- Visualizes pachyvessels (Haller layer dilated veins >200 μm)
- Measures SFCT

### Multifocal ERG
- Reduced central P1 amplitude; prolonged implicit time
- Quantifies functional macular loss beyond Snellen acuity

### Cortisol markers (in selected cases)
- 24-hour urinary free cortisol, salivary late-night cortisol: if Cushing syndrome suspected
- Not routine for typical CSCR

---

## 7. Epidemiology

- **Incidence:** 9.9/100,000/year in men, 1.7/100,000/year in women (PMID:24974790, Olmsted County, MN population-based study)
- **Male:female ratio:** ~6:1 overall (acute); narrows to ~3:1 in chronic/older presentations
- **Peak age:** 30–50 years; females present ~5–10 years later than males
- **Bilateral:** Typically unilateral at presentation; ~40% develop fellow-eye involvement over lifetime
- **Recurrence:** ~40–50% recur within 1 year after spontaneous resolution
- **Ethnic variation:** Higher incidence in Asian (East Asian, South Asian), Hispanic, Middle Eastern populations vs Northern European
- **Inheritance:** Complex/multifactorial; not Mendelian. Rare familial clustering (shared NR3C2 or CFH variants)

---

## 8. Temporal Development

| Phase | Definition | Natural History |
|---|---|---|
| Acute CSCR | SRF <3–4 months | 80–90% spontaneous resolution; VA returns to ≥20/25 in most |
| Chronic CSCR | SRF >3–4 months | Progressive RPE damage, photoreceptor loss, risk of CNV |
| Recurrent | Multiple episodes | Each adds cumulative RPE/photoreceptor damage |

- Residual symptoms (contrast, metamorphopsia) persist in ~30% even after SRF resolution in acute
- Long-term: BCVA 20/40 or worse at 5 years in ~20–30% chronic untreated (PMID:19683830)
- CNV develops in ~5–10% chronic over 5 years

---

## 9. Treatment (comprehensive)

### Observation / Supportive Care
- **MAXO:0000950** (supportive care)
- First-line in acute CSCR; most resolve in <3 months
- Discontinue corticosteroids; treat OSA; stress management
- Monthly OCT monitoring; intervene if no resolution by 3–4 months

### Half-Dose Photodynamic Therapy with Verteporfin — **Standard of Care for Chronic CSCR**
- **NCIT:C15300** (Photodynamic Therapy)
- **CHEBI:32293** (verteporfin)
- **Mechanism:** Verteporfin accumulates in abnormal choroidal pachyvessels → 689 nm laser activation → singlet oxygen → endothelial damage → thrombosis → normalized choroidal blood flow and permeability
- **Half-dose protocol:** 3 mg/m² BSA (vs standard 6 mg/m²) minimizes RPE damage
- **PLACE trial (PMID:29229468):** RCT half-dose PDT vs micropulse laser; 67% complete SRF resolution with PDT vs 29% micropulse at 7 weeks — **definitive evidence for PDT superiority**
- Earlier RCT evidence: PMID:15232060 (Chan 2008 — first PDT RCT for CSCR)
- ICGA-guided treatment targeting choroidal hyperpermeability zones (not just FA leakage point)

### Mineralocorticoid Receptor Antagonists
- **NCIT:C15986** (Pharmacotherapy)
- **Eplerenone: CHEBI:31547** — selective MR antagonist
- **Spironolactone: CHEBI:9241** — non-selective MR antagonist
- **VICI trial (PMID:32014115):** Definitive RCT (Lotery 2020, *Lancet*): eplerenone **NOT significantly effective** vs placebo in chronic CSCR (SRF reduction −19.7 μm vs −7.6 μm placebo; p=0.18). **This is a largely negative trial — critical for accuracy.**
- Spironolactone: small RCTs/open-label series suggest possible benefit (PMID:23539526) but no definitive large RCT
- Ongoing debate: continue off-label use in selected patients (high cortisol, cortisol-driven cases)
- **Uncertainty flag:** VICI negative result does not rule out benefit in specific subgroups; higher-selectivity agents (finerenone) under investigation

### Focal Laser Photocoagulation
- **NCIT:C62730** (Infrared Photocoagulation Therapy)
- For extrafoveal leakage points only; creates permanent scotoma at treatment site
- Accelerates resolution in acute extrafoveal disease; NOT for subfoveal/juxtafoveal leaks
- Less used since PDT demonstrated superior safety/efficacy

### Anti-VEGF Therapy (for CNV complication only)
- **NOT first-line** for uncomplicated CSCR — MR-driven mechanism not primarily VEGF
- Standard of care for type 1 or type 2 CNV complicating chronic CSCR
- Agents: bevacizumab (NCIT:C2038), ranibizumab (NCIT:C48135), aflibercept (NCIT:C64468)

### Micropulse Subthreshold Laser
- 577 nm or 810 nm; no visible burn; RPE stimulation without destruction
- Inferior to half-dose PDT in PLACE trial (29% vs 67% SRF resolution)
- Used when PDT unavailable or contraindicated; avoids scotoma risk of conventional laser

### Oral Rifampicin
- **CHEBI:28077** (rifampicin)
- **Mechanism:** CYP3A4/CYP2C8/CYP2C9 inducer → accelerates cortisol catabolism → reduces systemic cortisol → reduces choroidal MR activation
- PMID:25138772 (Shulman 2014 — open-label series); small benefit shown
- Limited by significant drug–drug interactions and hepatotoxicity risk

### Mifepristone (Glucocorticoid Receptor Antagonist)
- **CHEBI:50692** (mifepristone)
- GR (NR3C1) antagonist; blocks glucocorticoid signaling in choroid
- Small RCT evidence of benefit in recurrent CSCR (PMID:20142386)
- Limited by antiprogestational effects

### Finasteride (Androgen Hypothesis)
- **CHEBI:5100** (finasteride) — 5α-reductase inhibitor
- Rationale: CSCR male-predominance may reflect androgen-mediated choroidal vasoreactivity
- PMID:19325499 (Haimovici — pilot data); very limited evidence. **Uncertainty flag.**

---

## 10. Prevention

**Primary:**
- Avoid/minimize corticosteroids; use lowest effective dose, shortest duration, prefer non-systemic routes where possible
- Ophthalmology monitoring if corticosteroids medically necessary
- Stress management; treat OSA
- No genetic screening recommended

**Secondary (preventing progression/recurrence):**
- Monthly OCT during active phase; 3-monthly in remission
- Screen for endogenous Cushing syndrome in severe/bilateral cases
- Patient education on recurrence triggers (steroids, stress, sleep deprivation)
- Monitor fellow eye — 40% cumulative bilateral involvement

---

## 11. Prognosis

| Condition | Prognosis |
|---|---|
| Acute CSCR | Excellent; 80–90% spontaneous resolution; Snellen acuity ≥20/25 in most |
| Recurrent CSCR | Each episode adds cumulative risk; residual contrast/metamorphopsia in ~30% |
| Chronic CSCR | BCVA 20/40 or worse at 5 years in ~20–30% (PMID:19683830) |
| CSCR + CNV | Substantially worsens prognosis; requires anti-VEGF |

Quality of life significantly impaired even with "normal" Snellen acuity — contrast sensitivity, color discrimination, metamorphopsia, reading difficulty are common residual complaints (PMID:28122842).

---

## 12. Animal Models

| Model | Description | Limitation |
|---|---|---|
| Primate (macaque) | Intravitreal/systemic dexamethasone → choroidal hyperpermeability + SRF; most validated model (PMID:12699435) | Full pachychoroid anatomy not replicated |
| Mouse (MR-overexpression) | Choroidal endothelial NR3C2 overexpression → hyperpermeability (PMID:22446627) | Murine choroid much thinner; no pachychoroid anatomy; SRF/PED phenotype not fully replicated |
| Zebrafish | No established model | Choroidal anatomy differs substantially |

**HUMAN_MODEL_MISMATCH:** Rodent models cannot replicate the pachychoroid structural predisposition or the human-specific CFH/ARMS2 genetic architecture. MR pharmacology insights are translatable, but full CSCR pathophysiology is not modeled in rodents. PMID:22446627 provides mechanistic data (murine), but its translational validity to human pachychoroid disease requires caution.

---

## 13. Ontology Term Reference Summary

### Cell Types (CL)
- **CL:0000115** — endothelial cell (use preferred_term: "choroidal endothelial cell")
- **CL:0002586** — retinal pigment epithelial cell
- **CL:0000210** — photoreceptor cell
- **CL:0000573** — retinal cone cell
- **CL:0000604** — retinal rod cell

### Biological Processes (GO)
- **GO:0043117** — positive regulation of vascular permeability (INCREASED in choroid)
- **GO:0006811** — monoatomic ion transport (DECREASED in RPE)
- **GO:0007601** — visual perception (DECREASED)
- **GO:0007602** — phototransduction (DECREASED)
- **GO:0001525** — angiogenesis (INCREASED in CNV complication)
- **GO:0006915** — apoptotic process (INCREASED in chronic photoreceptor loss)
- **GO:0042921** — glucocorticoid receptor signaling pathway
- **GO:0045944** — positive regulation of transcription by RNA polymerase II (MR-mediated)

### Anatomical Structures (UBERON)
- **UBERON:0001777** — choroid
- **UBERON:0002320** — retinal pigment epithelium
- **UBERON:0003384** — photoreceptor layer of retina
- **UBERON:0001629** — outer nuclear layer of retina
- **UBERON:0003386** — macula lutea
- **UBERON:0004904** — Bruch's membrane *(verify UBERON ID)*

### Treatments
- **MAXO:0000950** — supportive care
- **NCIT:C15300** — Photodynamic Therapy
- **NCIT:C15986** — Pharmacotherapy
- **NCIT:C62730** — Infrared Photocoagulation Therapy

### Drugs (CHEBI)
- **CHEBI:32293** — verteporfin
- **CHEBI:31547** — eplerenone
- **CHEBI:9241** — spironolactone
- **CHEBI:28077** — rifampicin
- **CHEBI:50692** — mifepristone
- **CHEBI:5100** — finasteride

---

## 14. Priority PMIDs to Fetch

Run these immediately before adding evidence to the YAML:

```bash
just fetch-reference PMID:22446627   # Zhao 2012 J Clin Invest — seminal MR mechanism paper
just fetch-reference PMID:29229468   # van Dijk 2018 Ophthalmology — PLACE trial (PDT vs micropulse)
just fetch-reference PMID:32014115   # Lotery 2020 Lancet — VICI trial (eplerenone, NEGATIVE result)
just fetch-reference PMID:25939894   # Schellevis 2015 J Med Genet — first CSCR GWAS (CFH)
just fetch-reference PMID:29515099   # Schellevis 2018 Ophthalmology — second GWAS (ARMS2/HTRA1)
just fetch-reference PMID:24974790   # Kitzmann 2008 Ophthalmology — epidemiology/incidence
just fetch-reference PMID:28122842   # van Rijssen 2019 Prog Retin Eye Res — treatment review
just fetch-reference PMID:17702499   # Bouzas 2002 Surv Ophthalmol — corticosteroid association
just fetch-reference PMID:23380442   # Gemenetzi 2010 Eye — pathogenesis review
just fetch-reference PMID:25654734   # Tsai 2015 Retina — corticosteroid pharmacoepidemiology
just fetch-reference PMID:23736878   # Li 2013 — OSA association
just fetch-reference PMID:31712692   # Hosoda 2020 — GATA5 Japanese GWAS
just fetch-reference PMID:23539526   # Bousquet — spironolactone RCT
just fetch-reference PMID:15232060   # Chan 2008 — first PDT RCT for CSCR
just fetch-reference PMID:19683830   # Loo — long-term VA outcomes
```

---

## 15. Key Active Debates / Uncertainties

1. **VICI trial interpretation:** Eplerenone failed but MR mechanism is well-established. Ongoing: Is a more selective MR antagonist (finerenone) effective? Was dosing/patient selection suboptimal?
2. **Pachychoroid: predisposition vs. acquired phenotype?** Most evidence favors it as a primary genetic vascular anatomy trait.
3. **ARMS2/HTRA1 mechanism in CSCR:** Why does this AMD locus confer CSCR risk? Likely shared Bruch membrane/choroidal vulnerability but specific mechanism unknown.
4. **H. pylori association:** Causal link not established; possibly confounded by socioeconomic factors.
5. **Anti-VEGF in uncomplicated CSCR:** Current consensus is reserve for CNV only; multiple negative small RCTs for primary CSCR.
6. **Androgen hypothesis:** Male predominance not fully explained by corticosteroid/stress exposure alone; finasteride data insufficient.
7. **HUMAN_MODEL_MISMATCH:** Rodent MR models cannot recapitulate human pachychoroid anatomy; translate pharmacology insights cautiously.

---

This report adds substantial depth to the existing stub — notably: the GWAS genetics section (CFH, ARMS2/HTRA1, NR3C2, GATA5, KCNJ13), the detailed MR molecular mechanism, the pachychoroid phenotype concept, expanded phenotypes (adding micropsia, dyschromatopsia, nyctalopia, ERG findings), the VICI trial negative result for eplerenone (critical for accuracy), the PLACE trial data establishing PDT as standard of care, and the animal model HUMAN_MODEL_MISMATCH flag. Use `just fetch-reference PMID:XXXXX` for each PMID before writing snippets into YAML.