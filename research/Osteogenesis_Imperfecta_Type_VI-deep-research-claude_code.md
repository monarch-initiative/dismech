---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-4-6
cached: false
start_time: '2026-06-29T00:37:06.129470'
end_time: '2026-06-29T00:43:31.732747'
duration_seconds: 385.6
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Osteogenesis Imperfecta Type VI
  mondo_id: MONDO:0013515
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
  - claude-sonnet-4-6
  web_search_requests: 22
  num_turns: 32
  total_cost_usd: 1.7802019
  session_id: 47773791-be6a-5374-abd7-2aac0ef4f74c
  stop_reason: end_turn
citation_count: 23
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Osteogenesis Imperfecta Type VI
- **MONDO ID:** MONDO:0013515 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Osteogenesis Imperfecta Type VI** covering all of the
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

I now have sufficient information to compile the comprehensive research report. Let me assemble it.

---

# Comprehensive Research Report: Osteogenesis Imperfecta Type VI

**Prepared:** June 29, 2026
**Disease:** Osteogenesis Imperfecta Type VI (OI6)
**Category:** Mendelian / Autosomal Recessive Rare Bone Dysplasia

---

## 1. Disease Information

### Overview

Osteogenesis Imperfecta Type VI (OI6) is an extremely rare, severe autosomal recessive skeletal dysplasia characterized by bone fragility and a distinctive mineralization defect, caused by loss-of-function mutations in the *SERPINF1* gene encoding pigment epithelium-derived factor (PEDF). It was first delineated by Glorieux et al. in 2002 as a group of patients initially classified as OI type IV who share a unique set of clinical, histological, and biochemical features not explained by collagen structural defects (PMID: 11771665). Unlike the classical dominant OI types (I–IV), OI type VI is distinguished by normal type I collagen, an absence of dentinogenesis imperfecta and hearing loss, and the pathognomonic "fish-scale" lamellar pattern observed by polarized-light bone histomorphometry. Fewer than 50 cases have been reported in the world literature.

### Key Identifiers

| Resource | Identifier |
|---|---|
| OMIM | #613982 (OI6) / *613982* (SERPINF1 OMIM Gene) |
| Orphanet | ORPHA:216804 |
| MONDO | MONDO:0013515 |
| MeSH | C567088 |
| ICD-10 | Q78.0 (Osteogenesis imperfecta) |
| ICD-11 | LD24.10 |
| SERPINF1 HGNC | HGNC:8824 |
| SERPINF1 locus | Chromosome 17p13.3 |

### Synonyms and Alternative Names

- OI Type VI
- Osteogenesis imperfecta with mineralization defect
- OI6
- Brittle bone disease type VI
- Pigment epithelium-derived factor (PEDF) deficiency

---

## 2. Etiology

### Primary Disease Cause

OI type VI is caused exclusively by **biallelic loss-of-function variants in *SERPINF1*** (chromosome 17p13.3), which encodes the secreted glycoprotein pigment epithelium-derived factor (PEDF). All disease-causing alleles reported to date result in complete or near-complete abolition of PEDF secretion. Unlike OI types I–IV, the type I collagen genes (*COL1A1*, *COL1A2*) are structurally normal. PEDF's roles in bone homeostasis—inhibiting osteoclastogenesis, promoting osteoblast differentiation, and regulating mineralization—are thus disrupted (PMID: 21826736; PMID: 24523041).

### Genetic Risk Factors

- **Autosomal recessive inheritance:** Both parents are obligate heterozygous carriers. The recurrence risk for sibling offspring of carrier couples is 25% per pregnancy.
- **Consanguinity:** OI type VI is enriched in consanguineous populations. In a large Indian cohort, SERPINF1 variants accounted for approximately 12.5% of the autosomal recessive OI population, attributable to higher background rates of consanguinity (PMC10323215).
- **Founder mutations:** A 5-bp duplication in exon 3 of *SERPINF1*, c.261_265dup (p.Leu89Argfs*26), exhibits a strong founder effect in the **Tuvan population** of Southern Siberia, with an estimated carrier frequency of 1:114 and disease prevalence of approximately 1:52,375 in that isolate (PMC12250282).
- **No known genetic modifier genes** significantly altering OI6 penetrance or expressivity have been identified. Penetrance is complete for biallelic null alleles.

### Environmental Risk Factors

No environmental factors have been shown to cause or substantially modify OI type VI risk, which is monogenic. However:
- **Calcium and vitamin D insufficiency** can worsen the already-poor bone mineralization phenotype and exacerbate fracture burden.
- **Physical trauma** from standing and ambulation precipitates the first fractures (onset 4–18 months).

---

## 3. Phenotypes

### Clinical Phenotype Summary

OI type VI presents with a characteristically **moderate-to-severe** and **progressive** skeletal phenotype. The defining clinical features that distinguish it from other OI types include the absence of fractures at birth, absence of dentinogenesis imperfecta, normal or faintly blue (not deep blue) sclerae, and absent sensorineural hearing loss (PMID: 11771665; PMC12250282).

| Phenotype | HP Term | Frequency | Onset | Severity | Notes |
|---|---|---|---|---|---|
| Recurrent fractures | HP:0002757 | Universal (100%) | Infant (4–18 mo) | Severe (8–200 fractures lifetime) | Not present at birth |
| Short stature | HP:0004322 | Universal (100%) | Childhood | Severe (Z-scores −2.7 to −7.7) | |
| Vertebral compression fractures | HP:0002953 | Universal (100%) | Childhood | Severe | All patients in case series |
| Long bone deformity / bowing | HP:0002982 | Very frequent | Childhood | Severe–very severe | Multilevel, multiplanar |
| Kyphoscoliosis | HP:0002751 | Very frequent | Childhood | Moderate–severe | Up to grade IV |
| Bell-shaped thorax / thin ribs | HP:0000774 | Frequent | Childhood | — | |
| Muscular hypotonia | HP:0001290 | Frequent | Infancy | — | |
| Reduced bone mineral density | HP:0004349 | Universal (100%) | Childhood | Z-scores −1.7 to −4.6 | |
| White or faintly blue sclerae | HP:0000953 | Universal | At birth | — | Deep blue absent |
| Absent dentinogenesis imperfecta | HP:0000668 (absent) | Universal | — | — | Key negative feature |
| Absent hearing loss | HP:0000407 (absent) | Universal | — | — | Key negative feature |
| Motor developmental delay | HP:0001270 | Frequent | Infancy | — | Delayed independent sitting/walking |
| Loss of independent ambulation | — | Frequent–universal | Childhood | — | All patients in one case series |

**Biochemical phenotypes:**
- **Elevated serum alkaline phosphatase (ALP):** ALPL levels in children with OI6 are elevated compared with age-matched OI type IV patients (409 ± 145 U/L vs. 295 ± 95 U/L; PMID: 11771665). HP:0003155 (Elevated alkaline phosphatase)
- **Undetectable serum PEDF:** Circulating PEDF (~100 nM in normal individuals) is completely absent or dramatically reduced in OI6 patients (PMID: 21826736). This is pathognomonic.

**Histopathology phenotype:**
- **Fish-scale lamellar pattern (polarized light):** Bone biopsy reveals an irregular "fish-scale" arrangement of bone lamellae visible under polarized light microscopy — the histological hallmark of OI6, not seen in other OI types (PMID: 11771665; PMID: 25554599).
- **Increased osteoid volume:** Excessive unmineralized osteoid accumulates, reflecting a prolonged mineral lag time and impaired matrix mineralization.
- **Increased osteocyte number**
- **Coexistence of hypermineralized zones and hypomineralized osteoid seams** at nano-scale (PMID: 25554599): unusual heterogeneous mineral particle population.

### Quality of Life Impact

OI type VI severely impairs quality of life. All patients in published series lose independent ambulation; 2 of 4 patients in the Tuvan cohort never achieved unsupported sitting (PMC12250282). Progressive spinal deformities cause pain, respiratory compromise, and loss of balance. BAMF and GMFM mobility scores are low and tend to stabilize or marginally improve only with aggressive anti-resorptive therapy (PMC4180531).

---

## 4. Genetic and Molecular Information

### Causal Gene: *SERPINF1* (HGNC:8824)

*SERPINF1* encodes the 418-amino-acid secreted glycoprotein **PEDF** (pigment epithelium-derived factor), a member of the non-inhibitory serpin superfamily. The protein contains a collagen-binding domain (N-terminal region), an antiangiogenic domain, and a neurotrophic domain. PEDF is ubiquitously expressed but particularly abundant in bone (osteoblasts, osteocytes), eye (retinal pigment epithelium), and liver (PMID: 21826736).

- **Gene locus:** 17p13.3
- **RefSeq mRNA:** NM_002615.6
- **UniProt:** P36955

### Pathogenic Variant Types

All OI6-causing variants result in loss of function (PEDF absent from serum). Variant types include:

| Variant | Type | Exon | Effect | Population | Reference |
|---|---|---|---|---|---|
| c.295C>T (p.R99X) | Nonsense | 4 | NMD; <6% transcript remaining | French-Canadian | PMID:21826736 |
| c.10440_10443dupATCA (p.H389fsX392) | Frameshift | 8 | Premature stop | Italian | PMID:21826736 |
| c.261_265dup (p.Leu89Argfs*26) | Frameshift | 3 | Loss of function | Tuvan (founder) | PMC12250282 |
| c.185G>T (p.Gly62Val) | Missense | 3 | Likely pathogenic | Various | PMC12250282 |
| c.992_993insCA (p.Glu331Asnfs) | Frameshift insertion | — | Truncation (86 aa loss); no NMD | Various | PMC12250282 |
| Intronic cryptic splice site (intron 4, AGGC→AGGT) | Splice site | Intron 4 | Aberrant splicing → loss of function | Various | PMC6124173 |
| Homozygous in-frame deletions/missenses (e.g., p.Val356Glu; p.Ala96_Gly215del) | Missense / large del | Various | Protein misfolded; ER retention | Chinese families | PMID:25868797 |

- **Variant classification:** All definitively pathogenic variants are autosomal recessive. *De novo* variants are not described; both parents are obligate carriers.
- **Allele frequency (gnomAD):** Individual *SERPINF1* LOF alleles are individually very rare (heterozygous allele frequency typically <0.001); compound heterozygosity is common outside founder populations.
- **Origin:** Germline; somatic OI6 not described.
- **Functional consequence:** Null mutations → nonsense-mediated decay or premature stop → absent PEDF protein. Missense/in-frame variants → protein misfolding → ER retention → ER stress → no secreted protein (PMID:25868797; ScienceDirect article on ER stress 2025).

### Modifier Genes / Epigenetics

No well-validated modifier genes for OI6 expressivity have been identified. Notably, a rare *IFITM5* S40L mutation (causing OI type V) paradoxically reduces PEDF secretion from osteoblasts, producing an "atypical OI type VI" phenotype—demonstrating that PEDF reduction is the proximate cause rather than SERPINF1 genotype per se (PMID:24523041). Epigenetic contributions are not established for OI6.

---

## 5. Environmental Information

No environmental factors are causal in OI type VI, which is an entirely monogenic condition. Environmental modifiers of clinical severity include:
- **Physical trauma and weight-bearing:** The onset of fractures coincides with early ambulation (4–18 months), indicating that mechanical loading precipitates fractures in the setting of extreme bone fragility.
- **Calcium and vitamin D intake:** Suboptimal calcium/vitamin D worsens the mineralization defect. All published treatment protocols include calcium (500–1000 mg/day) and vitamin D supplementation alongside pharmacotherapy (PMC4180531).
- **Immobilization:** Prolonged immobilization after fractures accelerates bone resorption and worsens osteopenia, creating a vicious cycle.

---

## 6. Mechanism / Pathophysiology

### Overview of Pathogenic Cascade

The fundamental mechanism of OI6 is **absence of secreted PEDF**, leading to dysregulated bone remodeling, defective matrix mineralization, and excessive osteoid accumulation. PEDF normally exerts multiple protective effects in bone:

#### 6a. RANKL/OPG Axis: Osteoclast Overactivation

PEDF normally upregulates **osteoprotegerin (OPG)** expression in osteoblasts, thereby **inhibiting RANKL-mediated osteoclast differentiation and activation**. PEDF also directly antagonizes RANKL-mediated cell survival signals in osteoclast precursors (PMID:19945427). In the absence of PEDF, the OPG:RANKL ratio is shifted toward RANKL, promoting osteoclastogenesis and excessive bone resorption. This explains the limited efficacy of bisphosphonates (which require mineralized bone matrix for deposition) and the superior efficacy of **denosumab** (anti-RANKL monoclonal antibody) in OI6 (PMC4180531).

- GO process: GO:0030316 (osteoclast differentiation)
- GO process: GO:0060352 (cell adhesion molecule production involved in inflammatory response) — secondary
- CL terms: CL:0000092 (osteoclast), CL:0000062 (osteoblast)

#### 6b. SOST/Sclerostin Dysregulation: Impaired Osteoblast Differentiation

PEDF suppresses expression of **SOST** (encoding sclerostin) and other osteocyte-associated genes (*MEPE*, *DMP1*) in osteocytes via **ERK/GSK-3β/β-catenin signaling**. ERK activation by PEDF inactivates GSK-3β, stabilizing β-catenin and permitting nuclear Wnt target gene activation to support osteoblastogenesis. Without PEDF, sclerostin is overexpressed, Wnt signaling is inhibited, and osteoblast gene expression (*RUNX2*, osteocalcin, BSP, COL1A1*) is reduced (PMID:30076958; PMID:30607618).

- GO process: GO:0060070 (canonical Wnt signaling pathway)
- GO process: GO:0010832 (negative regulation of myotube differentiation) — adjacent
- Cell type: CL:0000137 (osteocyte)

#### 6c. Wnt3a Antagonism at Terminal Osteoblast Differentiation

PEDF blocks **LRP6** (a Wnt co-receptor), suppressing Wnt3a signaling at the late stage of osteoblast differentiation. Continuous Wnt3a exposure at this stage paradoxically reduces mineralization by 40%. PEDF therefore acts as a context-dependent Wnt inhibitor at terminal differentiation, and its absence unleashes inappropriate Wnt3a activity that disrupts the osteoblast-to-osteocyte transition and the initiation of matrix mineralization (PMC4970601). This explains the increased osteoid (unmineralized matrix) with architecturally abnormal lamellae.

- GO process: GO:0030282 (bone mineralization)
- GO process: GO:0043062 (extracellular structure organization)

#### 6d. PEDF-TGF-β Antagonism

PEDF functionally antagonizes **TGF-β signaling**. Loss of PEDF leads to activated TGF-β signaling in osteoblasts, which delays osteoblast maturation and ECM mineralization while simultaneously stimulating **pro-angiogenic factors** (e.g., VEGF). In the *Serpinf1*−/− mouse model, TGF-β stimulation and PEDF deficiency produce additive suppression of osteogenic markers (Kang et al. 2022, JBMR, PMID:35212013). This provides a rationale for combined PEDF replacement + TGF-β antibody therapeutic strategies. Increased angiogenesis may also contribute to the structural vascular pathogenesis.

- GO process: GO:0007179 (TGF-β receptor signaling pathway)
- GO process: GO:0001525 (angiogenesis)

#### 6e. ER Stress / Autophagy (In-Frame / Missense Variants)

For patients harboring in-frame or missense SERPINF1 mutations (rather than truncating null alleles), mutant PEDF protein is synthesized but **retained in the endoplasmic reticulum** due to misfolding. This triggers **ER stress** and the unfolded protein response (UPR), activating ER-associated degradation (ERAD) and autophagy as compensatory mechanisms (ScienceDirect 2025, PMID forthcoming). The net result is osteoblast apoptosis and impaired differentiation, convergent on the same downstream phenotype. ER stress and autophagy pathways are emerging as **therapeutic targets** for SERPINF1 missense-variant OI6.

- GO process: GO:0034976 (response to endoplasmic reticulum stress)
- GO process: GO:0006914 (autophagy)

#### 6f. Anti-Adipogenic / Anti-Angiogenic Functions

PEDF inhibits adipogenesis (binding adipose triglyceride lipase, suppressing PPARγ). In the *Serpinf1*−/− mouse, total body adiposity increases by ~50%, suggesting PEDF-null OI6 may have altered mesenchymal stem cell fate allocation (reduced osteoblast, increased adipocyte differentiation from bone marrow progenitors) (PMC8755987).

### Summary Causal Chain

```
Biallelic SERPINF1 LOF mutations
    ↓
Absent PEDF in circulation and bone ECM
    ↓
[Branch A] ↓OPG, ↑RANKL → Osteoclast overactivation → Excessive bone resorption
[Branch B] ↑Sclerostin → ↓Wnt signaling → Impaired osteoblast differentiation
[Branch C] ↑Wnt3a at terminal differentiation → Disrupted osteoblast-osteocyte transition
[Branch D] ↑TGF-β signaling → Delayed osteoblast maturation + ↑pro-angiogenic factors
[Branch E] (Missense only) ER retention of PEDF → ER stress → Osteoblast apoptosis
    ↓ (convergence)
Defective ECM mineralization + Excess unmineralized osteoid + Structural lamellar disorganization
    ↓
Fish-scale lamellation pattern; elevated ALP; absent serum PEDF
    ↓
Bone fragility → Fractures, deformity, short stature, kyphoscoliosis
```

### Tissue / Cell Types Involved

| Cell Type | CL Term | Role |
|---|---|---|
| Osteoblast | CL:0000062 | Primary cell with SERPINF1 expression; fails to secrete PEDF; impaired differentiation/mineralization |
| Osteocyte | CL:0000137 | Overexpresses sclerostin in absence of PEDF |
| Osteoclast | CL:0000092 | Overactivated due to altered RANKL/OPG ratio |
| Mesenchymal stem cell | CL:0000134 | Skewed toward adipogenic fate when PEDF absent |
| Bone marrow stromal cell | CL:0002092 | Source of osteoblast precursors |

### Anatomical Structures Affected (UBERON)

| Structure | UBERON | Involvement |
|---|---|---|
| Long bone (femur, tibia, humerus) | UBERON:0002203 | Fractures, bowing, deformity |
| Vertebra | UBERON:0001130 | Compression fractures, kyphoscoliosis |
| Rib | UBERON:0002228 | Thin ribs, bell-shaped thorax |
| Cortical bone | UBERON:0001481 | Abnormal lamellar organization |
| Trabecular bone | UBERON:0005401 | Reduced volume, increased osteoid |
| Sclerae | UBERON:0000952 | White/faintly blue |
| Bone marrow | UBERON:0002371 | Altered progenitor cell fate |

---

## 7. Anatomical Structures Affected

See detailed summary in section 6 (Mechanism). Briefly:

- **Primary:** Long bones (bilateral), vertebral column (multilevel compression fractures), thoracic cage (thin ribs, bell-shaped chest), bone extracellular matrix
- **Secondary:** Respiratory function (from thoracic restriction and kyphoscoliosis); neuromuscular function (hypotonia, motor delay)
- **Subcellular:** Endoplasmic reticulum (ER retention of missense PEDF), extracellular matrix (excessive osteoid accumulation)

The **eye** (retinal pigment epithelium, where PEDF was originally discovered) is not clinically affected in OI6 despite high PEDF expression there.

---

## 8. Temporal Development

### Onset

- **Perinatal/neonatal period:** No fractures at birth (important distinguishing feature from OI types II/III). Skeletal appearance is normal at birth.
- **Infancy (4–18 months):** Fractures begin with the onset of weight-bearing and ambulation. This is the canonical age-of-onset for OI6 (PMID: 11771665; PMC12250282).
- **Early childhood:** Progressive long bone deformities, vertebral compression fractures; growth retardation becomes apparent.

### Progression

OI6 follows a **relentlessly progressive** clinical course:
- Fracture burden accumulates over childhood (reported range: 8–200 total fractures across published patients, PMC12250282).
- Skeletal deformities worsen progressively: bowing of long bones becomes multiplanar, vertebral compression fractures lead to loss of height, kyphoscoliosis progresses and may require surgical stabilization in adolescence.
- Mobility generally decreases: all affected patients in one cohort eventually lost independent ambulation; 2 of 4 never achieved unsupported sitting.
- **No spontaneous remission** occurs; disease is lifelong and progressive without intervention.

### Disease Stage Patterns

| Stage | Approximate Age | Key Events |
|---|---|---|
| Pre-fracture | 0–6 months | Normal at birth; no clinical signs |
| Fracture onset | 4–18 months | First fractures with standing/walking |
| Early progressive | 2–10 years | Accumulating fractures; deformity; vertebral compression |
| Severe deformity | 10–20 years | Kyphoscoliosis; wheelchair dependence; growth failure |
| Adult | >20 years | Fixed deformities; continued fracture risk; chronic pain |

---

## 9. Inheritance and Population

### Inheritance

- **Autosomal recessive (AR)**
- Penetrance is **complete** for confirmed biallelic null alleles
- **Expressivity:** Variable (8–200 lifetime fractures in published cases); may partly reflect variant type (null vs. missense), genetic background, and treatment access
- **No genetic anticipation** (not a trinucleotide repeat disorder)
- **Consanguinity:** A significant risk factor; many published cases involve consanguineous parents

### Epidemiology

| Metric | Value | Source |
|---|---|---|
| Overall OI prevalence | ~1:10,000–20,000 | Orphanet |
| OI6 global prevalence | Extremely rare; <50 cases reported | PMC12250282 |
| OI6 Tuvan population prevalence | ~1:52,375 | PMC12250282 |
| Carrier frequency (Tuvan, c.261_265dup) | 1:114 (0.0044) | PMC12250282 |
| OI6 fraction of AR-OI in India | ~12.5% of AR-OI | PMC10323215 |
| Sex ratio | Not established; M=F expected (AR) | — |

### Population Demographics

- **Global:** Reported in patients from France, Italy, Russia (Tuva), India, Korea, China, Ecuador, Middle East, and North Africa — no single ethnic group predominates globally.
- **Tuvan population (Southern Siberia):** Strong founder effect (c.261_265dup); likely the highest known local prevalence due to long-term population isolation (PMC12250282).
- **Indian subcontinent:** Disproportionately represented among AR-OI cohorts, likely due to consanguinity rates (PMC10323215).
- **Age distribution:** A pediatric disease. Most reported patients are children/adolescents; adult cases documented but rare.

---

## 10. Diagnostics

### Clinical Diagnostic Criteria

OI6 was originally distinguished from type IV OI by the combination of (PMID: 11771665):
1. Fractures first documented between 4 and 18 months
2. **Absence** of fractures at birth
3. White or faintly blue sclerae (not deep blue)
4. **Absence** of dentinogenesis imperfecta
5. **Absence** of sensorineural hearing loss
6. Very short stature
7. Elevated serum alkaline phosphatase (in childhood)
8. **Histological fish-scale lamellar pattern** on bone biopsy under polarized light

After 2011, **genetic confirmation by SERPINF1 sequencing** or serum PEDF measurement became the gold-standard confirmatory test, superseding bone biopsy for most cases.

### Laboratory Tests

| Test | Finding | Clinical Significance | LOINC |
|---|---|---|---|
| Serum alkaline phosphatase | Elevated in childhood (mean 409 U/L) | Biochemical marker; reflects defective mineralization | LOINC:6768-6 |
| Serum PEDF | Undetectable (vs. ~100 nM normal) | Pathognomonic; distinguishes OI6 from all other OI types | — |
| Serum calcium | Usually normal | Rules out primary hypocalcemia | LOINC:17861-6 |
| Serum phosphate | Usually normal | Rules out hypophosphatemia/rickets | LOINC:2777-1 |
| Urinary bone resorption markers (CTX, NTX) | Elevated | Reflects osteoclast overactivity; used to guide denosumab dosing intervals | LOINC:48407-7 |
| Dual-energy X-ray absorptiometry (DXA) | Low lumbar spine Z-score (−1.7 to −4.6) | Quantifies bone mineral density deficit | — |

### Bone Biopsy (Histopathology)

- Iliac crest bone biopsy under **tetracycline double-labeling** reveals:
  - Increased osteoid thickness
  - Prolonged osteoid maturation time (increased mineral lag time)
  - **Fish-scale lamellar pattern** under polarized light (irregularly alternating bright/dark lamellae with rotational disorder)
  - Increased osteocyte density
  - Decreased mineralized bone volume per tissue volume
- HP:0011001 (Increased bone mineral density) does not apply; rather HP:0004349 (Decreased bone mineral density) combined with unique histology

### Genetic Testing

- **First-line:** Next-generation sequencing gene panel including *SERPINF1* (along with other AR-OI genes: *CRTAP*, *LEPRE1/P3H1*, *PPIB*, *SERPINH1*, *FKBP10*, *SP7*, *TMEM38B*, *SEC24D*, etc.)
- **Whole-exome sequencing (WES):** Recommended for atypical presentations; identifies cryptic splice variants (PMC6124173)
- **Whole-genome sequencing (WGS):** Can detect deep intronic variants and complex structural variants if panel/WES non-diagnostic
- **Single-gene Sanger sequencing:** Used for targeted confirmation of identified variants; for family screening of known mutations
- Molecular confirmation is essential: the fish-scale biopsy pattern, while characteristic, requires expertise and is increasingly replaced by genetic/PEDF testing

### Differential Diagnosis

| Condition | Distinguishing Features |
|---|---|
| OI type III (COL1A1/A2) | Deep blue sclerae; dentinogenesis imperfecta; fractures at birth; collagen abnormal |
| OI type IV (COL1A1/A2) | Mild blue sclerae; variable DI; fractures often present at birth; collagen abnormal |
| OI type V (IFITM5) | Hyperplastic callus; interosseous membrane calcification; white sclerae; history-based |
| X-linked hypophosphatemic rickets | Hypophosphatemia; normal PEDF; no fish-scale pattern |
| Nutritional rickets / osteomalacia | Responds to Vitamin D; normal genetics |
| Atypical OI type V with PEDF reduction (IFITM5 S40L) | Rare overlap; has BRIL protein abnormality; OI type V features also present |

---

## 11. Outcome / Prognosis

### Long-Term Course

OI type VI follows a **severe-to-very severe progressive** course, with cumulative fractures and skeletal deformities. In the largest published follow-up cohort, all patients sustained progressive deformities despite intervention; complete cessation of fractures was not achieved (PMID:28689307).

Key outcome data from published series:
- **Fracture burden:** 0.8–8.69 fractures/year across patients; cumulative lifetime fractures 12–200 (PMC12250282)
- **Mobility:** All patients in one series lost independent ambulation; functional stabilization achievable with aggressive pharmacotherapy
- **Height:** Final height severely reduced (Z-scores −2.7 to −7.7 SD); some height gain with denosumab treatment (5–8 cm over 2 years, PMC4180531)
- **Vertebral morphology:** Vertebral reshaping and improvement in BMD with denosumab; lumbar spine BMD Z-score improves with treatment (PMID:28689307)
- **Life expectancy:** Likely near-normal in adults receiving appropriate care (no specific mortality data published; severe early cases with thoracic restriction may be at respiratory risk)

### Complications

- **Respiratory failure** from thoracic deformity/kyphoscoliosis (potentially fatal in severe cases)
- **Spinal cord compression** from severe kyphoscoliosis
- **Immobility and wheelchair dependence**
- **Chronic pain**
- **Rebound hypercalcemia** from denosumab discontinuation (important iatrogenic risk)

### Prognostic Factors

- **Variant type:** Null alleles (NMD) = severest; missense alleles may have marginally different phenotypic spectrum
- **Response to denosumab:** Superior to bisphosphonates; BMD and fracture rates improved in all treated patients (PMC4180531; PMC6751648)
- **Age at treatment initiation:** Earlier treatment may prevent progressive deformity

---

## 12. Treatment

### 1. Bisphosphonates (Limited Efficacy)

**Cyclic intravenous pamidronate** (standard of care for other OI types) shows **limited efficacy** in OI6. Proposed mechanism: unmineralized osteoid prevents bisphosphonate binding to bone mineral (hydroxyapatite), reducing drug deposition and anti-resorptive effect (ScienceDirect, Moffatt 2006). Patients show modest increases in lumbar BMD but suboptimal fracture reduction compared to types III/IV OI.

- MAXO: MAXO:0000950 (supportive care as baseline)
- Route: IV infusions, typically q3–4 months

### 2. Denosumab (Anti-RANKL) — Preferred Treatment

**Denosumab** (NCIT:C66871; a RANKL-inhibiting monoclonal antibody) directly addresses the OI6 pathomechanism (excess RANKL-driven bone resorption due to absent PEDF). This therapeutic rationale was translated successfully by Hoyer-Kuhn et al. (PMC4180531).

**Dosing:**
- 1 mg/kg body weight subcutaneous injection
- Initial interval: 12 weeks; shortened to minimum 10 weeks if bone resorption markers re-elevate or bone pain recurs
- **Calcium supplementation:** 500–1000 mg/day for 2 weeks post-injection
- **Vitamin D:** Throughout treatment

**Outcomes after 2 years (n=4, PMC4180531):**
- Continuous areal BMD increase at lumbar spine and total body
- Vertebral morphology improvement (re-shaping)
- Fracture rate: 0–2 fractures per patient over 2 years (vs. historical fracture burden)
- Mobility improvement (BAMF and GMFM scores)
- Height gain of 5–8 cm

**Safety:** Mild hypocalcemia post-injection managed with supplementation; no severe adverse events reported.

**⚠️ Important warning:** Abrupt denosumab discontinuation causes rebound hypercalcemia and rapid bone loss (rebound phenomenon); transition to bisphosphonates or gradual dose spacing is necessary.

- MAXO term: MAXO:0000950 (pharmacotherapy)
- Treatment term: NCIT:C15986 (Pharmacotherapy)
- Therapeutic agent: NCIT:C66871 (Denosumab)

### 3. Surgical and Orthopedic Interventions

- **Intramedullary rod fixation** (telescoping rods): Performed at multiple sites (femur, tibia, humerus) to stabilize deformed long bones; prevents further deformity from fractures. Multiple surgeries typically required.
- **Corrective osteotomy:** Realignment of severely deformed long bones; combined with rod insertion.
- **Spinal stabilization:** Surgical spinal fusion for severe progressive kyphoscoliosis (typically deferred until puberty)

- MAXO: MAXO:0000004 (surgical procedure)
- NCIT: NCIT:C16186 (Orthopedic Surgical Procedure)

### 4. Physical and Rehabilitative Therapy

- **Physical therapy** (MAXO:0000011): Strengthening, gait training, pool therapy (hydrotherapy preferred to minimize fracture risk)
- **Occupational therapy:** Adaptive equipment; mobility aids
- Pain management: analgesics, anti-inflammatory agents (used cautiously given fracture and GI risk)

### 5. Calcium and Vitamin D Supplementation

- Essential adjunct to all pharmacotherapy, particularly denosumab
- Targets: Serum 25-OH-D >30 ng/mL; adequate dietary calcium intake

### 6. Experimental / Emerging Treatments

| Approach | Mechanism | Status | Reference |
|---|---|---|---|
| PEDF protein replacement (microspheres) | Directly restores PEDF → improves bone mass and mechanics | Preclinical (mouse model); 35–52% increase in trabecular BV/TV | PMC4970601 |
| Anti-TGF-β antibody | Addresses PEDF-TGF-β antagonism | Preclinical rationale | PMID:35212013 |
| Anti-sclerostin antibody (setrusumab/romosozumab) | Inhibits Wnt pathway brake; may be beneficial | Not systematically tested in OI6; OI types I/III/IV studied (NCT03118570) | Academic.oup.com/jbmr 2024 |
| Mesenchymal stem cell therapy | BOOSTB4 trial; general OI | Phase I/II; includes severe OI | NCT03706482 |
| ER stress modulators / autophagy inducers | Target ER retention phenotype in missense alleles | Preclinical research 2025 | ScienceDirect 2025 |

---

## 13. Prevention

### Genetic Counseling (Primary Prevention)

- **Carrier testing** is recommended for:
  - Parents of an affected child (confirmed obligate carriers if both parents are present and healthy)
  - Siblings of affected individuals (50% carrier probability)
  - Members of high-risk founder populations (e.g., Tuvan population)
- **Recurrence risk:** 25% per pregnancy for carrier couples
- **Preconception counseling:** Especially in consanguineous families and founder populations

### Prenatal Diagnosis

- **Chorionic villus sampling (CVS) or amniocentesis:** Fetal DNA tested for known parental *SERPINF1* mutations after the first affected child is identified
- **Preimplantation genetic testing (PGT):** PGT-M (for monogenic disease) can be offered to carrier couples undergoing IVF, enabling selection of unaffected embryos

### Tertiary Prevention (Complication Prevention in Affected Individuals)

- **Anti-resorptive therapy (denosumab)** as early as feasible to reduce fracture burden
- **Calcium and vitamin D sufficiency** maintained throughout life
- **Safe exercise programs:** Hydrotherapy, swimming — minimize high-impact loading
- **Fall prevention:** Adaptive mobility aids; safe home environments
- **Spinal monitoring:** Annual radiographs; early referral to spine surgery if progressive scoliosis
- **Respiratory surveillance:** Pulmonary function tests in patients with severe thoracic deformity
- **Vitamin D monitoring** (avoid deficiency, which worsens the mineralization defect)

### Screening

- **Newborn/infant screening:** No population-level newborn screening for OI6 exists. Clinical suspicion arises from fractures in early infancy; SERPINF1 sequencing or serum PEDF can confirm.
- **Cascade family testing:** All first-degree relatives of affected individuals should be offered carrier testing if proband mutations are known.

---

## 14. Other Species / Natural Disease

### Model Organisms

#### *Serpinf1*−/− Mouse (Primary Model)

The **Pedf-null mouse** (*Serpinf1*−/−) is the principal and best-validated animal model of OI type VI (Bogan et al. 2013, PMID:23413146).

| Feature | Mouse Phenotype | Human Correspondence |
|---|---|---|
| Trabecular bone volume | Significantly reduced (microCT) | Reduced BMD |
| Osteoid accumulation | Increased osteoid thickness | Fish-scale pattern / increased osteoid |
| Mineralization lag | Prolonged (histomorphometry) | Increased mineral lag time |
| Bone brittleness | Reduced ultimate displacement + energy to failure (3-point bending) | Increased fracture risk |
| PEDF expression | PEDF in osteoblasts and osteocytes; absent in KO | Undetectable serum PEDF |
| Anti-angiogenic effects | Increased CD-31 immunoreactivity in vessels | Possible vascular contributions |
| Body adiposity | +50% in KO | Not systematically assessed in humans |

**Limitations:** The Pedf-null mouse has a milder skeletal phenotype than most OI6 human patients. No spontaneous fractures at birth are seen (consistent with human presentation). The mouse does not fully recapitulate the extent of spinal and long-bone deformity seen in severely affected children.

- NCBI Taxon: 10090 (Mus musculus)
- Model type: Knockout (germline null)

#### Zebrafish

Zebrafish (*Danio rerio*) models of mineralization defects have been used for OI research broadly (including the *chihuahua* model), but *serpinf1*-specific zebrafish models are not prominently described in the published literature. PEDF is conserved in zebrafish.

- NCBI Taxon: 7955 (Danio rerio)

#### In Vitro Models

- **MC3T3-E1 murine osteoblast cell line:** Used to validate SERPINF1 missense mutations and ER retention phenotype (ER stress studies, 2025)
- **Human bone marrow mesenchymal stem cells (hMSCs):** Used to study PEDF-Wnt3a axis and mineralization; PEDF restoration improved mineralization in hMSC culture (PMC4970601)
- **Primary osteoblasts from Pedf-null mice:** Enhanced alizarin-red staining and elevated mineral:matrix ratio in culture (paradoxical increase in vitro, contrasting with in vivo hypomineralization, reflecting complex regulation)

---

## 15. Summary of Key Ontology Terms

### HPO Phenotype Terms

| Phenotype | HP Term |
|---|---|
| Recurrent fractures | HP:0002757 |
| Short stature | HP:0004322 |
| Vertebral compression fractures | HP:0002953 |
| Kyphoscoliosis | HP:0002751 |
| Bowing of long bones | HP:0002982 |
| Reduced bone mineral density | HP:0004349 |
| Elevated alkaline phosphatase | HP:0003155 |
| Hypotonia | HP:0001290 |
| Motor delay | HP:0001270 |
| White sclerae | HP:0000953 |
| Pathological fracture | HP:0002756 |

### GO Biological Processes

| Process | GO Term |
|---|---|
| Bone mineralization | GO:0030282 |
| Osteoclast differentiation | GO:0030316 |
| Canonical Wnt signaling | GO:0060070 |
| TGF-β receptor signaling | GO:0007179 |
| Response to ER stress | GO:0034976 |
| Autophagy | GO:0006914 |
| Angiogenesis | GO:0001525 |
| Osteoblast differentiation | GO:0001649 |
| ECM organization | GO:0030198 |

### CL Cell Ontology Terms

| Cell Type | CL Term |
|---|---|
| Osteoblast | CL:0000062 |
| Osteocyte | CL:0000137 |
| Osteoclast | CL:0000092 |
| Mesenchymal stem cell | CL:0000134 |

### CHEBI / Drug Terms

| Agent | ID |
|---|---|
| Pamidronate | CHEBI:25689 |
| Denosumab | NCIT:C66871 |
| Calcium carbonate | CHEBI:3311 |
| Cholecalciferol (Vitamin D3) | CHEBI:28940 |

### MAXO Treatment Terms

| Treatment | MAXO Term |
|---|---|
| Physical therapy | MAXO:0000011 |
| Genetic counseling | MAXO:0000079 |
| Surgical procedure | MAXO:0000004 |
| Supportive care | MAXO:0000950 |

---

## Key References

| PMID / Source | Description |
|---|---|
| PMID:11771665 | Glorieux et al. 2002 — Original description of OI type VI (JBMR) |
| PMID:21826736 | Becker et al. 2011 — SERPINF1 mutations cause OI type VI (identification) |
| PMID:24523041 | Cho et al. 2012 — PEDF biology and OI6 mechanisms |
| PMID:23413146 | Bogan et al. 2013 — Serpinf1-/- mouse model (JBMR) |
| PMC4180531 | Hoyer-Kuhn et al. 2014 — Denosumab 2-year outcomes in OI6 children |
| PMID:27127101 | Belinsky et al. 2016 — PEDF restoration via Wnt3a blockade improves bone in OI6 mouse |
| PMID:28689307 | Long-term follow-up of OI type VI with bisphosphonate/denosumab |
| PMC6751648 | Hoyer-Kuhn et al. 2019 — Individualized denosumab treatment follow-up |
| PMID:30076958 | PEDF regulation of SOST/sclerostin via ERK/GSK-3β/β-catenin |
| PMID:30607618 | PEDF reduced SOST/sclerostin expression in bone explants |
| PMID:35212013 | Kang et al. 2022 — PEDF-TGF-β antagonism in OI6 bone and vascular pathogenesis (JBMR) |
| PMC10323215 | SERPINF1 variants in Indian OI population — 18 patients, 10 variants |
| PMC12250282 | 2025 MDPI — Novel SERPINF1 variants; Tuvan founder effect; case series |
| PMID:25554599 | Unique micro- and nano-scale mineralization in OI6 bone (Bone) |
| PMID:25868797 | In-frame SERPINF1 mutations in OI6 — ER retention phenotype |
| PMC6124173 | Whole-exome sequencing identifies cryptic splice site in SERPINF1 |
| PMC8755987 | 2022 Review — OI mechanisms and signaling pathways (Endocrine Reviews) |
| ScienceDirect 2025 | ER stress and autophagy as therapeutic targets in SERPINF1-OI6 |
| PMID:19945427 | PEDF regulates osteoclasts via OPG and RANKL |

---

## Sources

- [Molecular and Clinical Aspects of OI Type VI — MDPI/PMC 2025 (PMC12250282)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12250282/)
- [OMIM Entry #613982 — Osteogenesis Imperfecta Type VI](https://omim.org/entry/613982)
- [Mutations in SERPINF1 Cause OI Type VI — PubMed PMID:21826736](https://pubmed.ncbi.nlm.nih.gov/21826736/)
- [Two Years' Experience with Denosumab for Children with OI Type VI — PMC4180531](https://pmc.ncbi.nlm.nih.gov/articles/PMC4180531/)
- [Individualized Denosumab Treatment Follow-up — PMC6751648](https://pmc.ncbi.nlm.nih.gov/articles/PMC6751648/)
- [A Mouse Model for Human OI Type VI — PMC3688658](https://pmc.ncbi.nlm.nih.gov/articles/PMC3688658/)
- [PEDF Restoration Increases Bone Mass via Wnt3a Blockade — PMC4970601](https://pmc.ncbi.nlm.nih.gov/articles/PMC4970601/)
- [OI Mechanisms and Signaling Pathways Review — PMC8755987](https://pmc.ncbi.nlm.nih.gov/articles/PMC8755987/)
- [Update on Genetics of OI — PMC11607015](https://pmc.ncbi.nlm.nih.gov/articles/PMC11607015/)
- [SERPINF1 Variants in Indian OI Patients — PMC10323215](https://pmc.ncbi.nlm.nih.gov/articles/PMC10323215/)
- [PEDF Regulates Osteoclasts via OPG and RANKL — PubMed PMID:19945427](https://pubmed.ncbi.nlm.nih.gov/19945427/)
- [PEDF Regulates SOST/Sclerostin via ERK/GSK-3β — PubMed PMID:30076958](https://pubmed.ncbi.nlm.nih.gov/30076958/)
- [PEDF Reduces SOST Expression in Bone Explants — PubMed PMID:30607618](https://pubmed.ncbi.nlm.nih.gov/30607618/)
- [Antagonism Between PEDF and TGF-β in OI6 — PMC11152058](https://pmc.ncbi.nlm.nih.gov/articles/PMC11152058/)
- [Unique Micro- and Nano-Scale Mineralization Pattern in OI6 — PubMed PMID:25554599](https://pubmed.ncbi.nlm.nih.gov/25554599/)
- [Whole-Exome Sequencing Identifies Cryptic Splice Site in SERPINF1 — PMC6124173](https://pmc.ncbi.nlm.nih.gov/articles/PMC6124173/)
- [Osteogenesis Imperfecta — Endotext/NIH Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK279109/)
- [Osteogenesis Imperfecta — StatPearls/NIH Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK536957/)
- [NIH Genetic Testing Registry — OI Type VI](https://www.ncbi.nlm.nih.gov/gtr/conditions/C3279564/)
- [Endoplasmic Reticulum Stress and Autophagy in SERPINF1-Induced OI6 — ScienceDirect 2025](https://www.sciencedirect.com/science/article/abs/pii/S0024320525004977)
- [In-frame SERPINF1 Mutations in OI Type VI — PubMed PMID:25868797](https://pubmed.ncbi.nlm.nih.gov/25868797/)
- [OI Type VI: A Form of Brittle Bone Disease with Mineralization Defect — JBMR 2002 (Glorieux)](https://academic.oup.com/jbmr/article-abstract/17/1/30/7582605)
- [Setrusumab for OI — Phase 2b ASTEROID Study — JBMR 2024](https://academic.oup.com/jbmr/article/39/9/1215/7714798)