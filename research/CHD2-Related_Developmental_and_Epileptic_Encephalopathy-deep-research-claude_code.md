---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8
cached: false
start_time: '2026-07-22T16:40:20.622838'
end_time: '2026-07-22T16:51:06.106748'
duration_seconds: 645.48
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: CHD2-Related Developmental and Epileptic Encephalopathy
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
  - claude-opus-4-8
  web_search_requests: 27
  num_turns: 42
  total_cost_usd: 4.509883749999999
  session_id: e25f4fd6-4f3a-4824-91a7-b741d8d1d2ed
  stop_reason: end_turn
citation_count: 28
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CHD2-Related Developmental and Epileptic Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CHD2-Related Developmental and Epileptic Encephalopathy** covering all of the
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

# CHD2-Related Developmental and Epileptic Encephalopathy — Comprehensive Research Report

**Prepared:** 2026-07-22 · **Target KB:** dismech `kb/disorders/` · **Category:** Mendelian

---

## Evidence provenance and verification status

Every PMID below is tagged with its verification status in this session. Only **✅ VERIFIED** identifiers were confirmed against a live PubMed/publisher record during this research pass. Items marked **⚠️ UNVERIFIED PMID** have a confirmed title/journal/year/DOI but the numeric PMID was *not* independently resolved — run `just fetch-reference` on these before using them as evidence, per the project's anti-hallucination SOP. Suggested ontology terms are **candidates requiring OAK verification** (`just validate-terms-file`); HPO in particular has renamed several seizure-semiology terms in recent releases, so labels must be checked rather than trusted.

---

## 1. Disease Information

### Overview

CHD2-related developmental and epileptic encephalopathy (CHD2-DEE) is an autosomal dominant, almost always de novo, neurodevelopmental disorder caused by heterozygous loss-of-function variants in *CHD2*, which encodes chromodomain helicase DNA-binding protein 2 — an ATP-dependent chromatin remodeler. The disorder sits at the intersection of three clinical worlds: it is a **developmental and epileptic encephalopathy**, an **intellectual disability / autism syndrome**, and a **photosensitive generalized epilepsy**. Its most distinctive clinical signature is an unusually intense, sometimes self-induced, sensitivity to flickering light superimposed on a myoclonic-predominant, drug-resistant generalized epilepsy.

The canonical presentation is a child with normal or mildly delayed early development who, typically in the second or third year of life, develops an explosive onset of multiple daily myoclonic and absence seizures, followed by developmental plateau or frank regression and long-term intellectual disability. The phenotypic range is however much broader than the original DEE description, extending from mild intellectual disability with well-controlled epilepsy to, at the far end, adult-onset non-syndromic pharmacoresistant epilepsy.

Importantly, the disorder is now best conceptualized not as a single syndrome but as a **spectrum of CHD2-related neurodevelopmental disorders**, of which DEE94 is the severe pole. GeneReviews explicitly frames the entity this way ("CHD2-Related Neurodevelopmental Disorders"), and ClinGen's Epilepsy Gene Curation Expert Panel curated the gene-disease relationship against the broad entity "complex neurodevelopmental disorder" rather than a narrow DEE label.

### Key identifiers

| Resource | Identifier | Notes |
|---|---|---|
| OMIM (phenotype) | **615369** — Developmental and Epileptic Encephalopathy 94 (DEE94) | Formerly "Epileptic encephalopathy, childhood-onset" (EEOC) |
| OMIM (gene) | **602119** — CHD2 | 15q26.1 |
| MONDO | **MONDO:0014150** — developmental and epileptic encephalopathy 94 | Confirmed via OLS4 query; synonym "CHD2 myoclonic encephalopathy" |
| MedGen | **C3809278** / CUI concept ID 815608 | |
| GARD | 13197 | |
| HGNC | **hgnc:1917** (dismech lowercase convention) | *CHD2* |
| UniProt | **O14647** | CHD2_HUMAN |
| Ensembl | ENSG00000173575 | |
| NCBI Gene | 1106 | |
| RefSeq transcript | **NM_001271.4** | Canonical transcript used in ClinVar submissions |
| ClinGen gene-disease validity | **Definitive**, AD, "complex neurodevelopmental disorder" (MONDO:0100038), Epilepsy GCEP, report date 2022-07-14 | Citable as `CGGV:` structured source |
| ClinGen dosage | **HI score 3** (sufficient evidence for haploinsufficiency); **TS score 0** (no evidence for triplosensitivity), 2019-10-23 | Citable as `CGDS:HGNC_1917` |
| ICD-11 | 8A61.Z / 8A6Z (developmental and epileptic encephalopathy, unspecified) — no CHD2-specific code | |
| ICD-10 | G40.4 (other generalized epilepsy and epileptic syndromes) — no specific code | |
| Orphanet | No dedicated CHD2 ORPHA code; MalaCards maps to ORPHA:1942 / ORPHA:2382 (broad DEE groupings) — **verify before citing** | |

> **Note on the triplosensitivity score.** The ClinGen TS score of 0 predates the 2024 *CHASERR* discovery. There is now direct human evidence that **increased** CHD2 dosage is also pathogenic (see §4), so the TS=0 assertion should be treated as historically accurate but biologically superseded. This is a good candidate for a `discussions` entry with `kind: KNOWLEDGE_GAP`.

### Synonyms and alternative names

- CHD2 myoclonic encephalopathy (MedlinePlus / MONDO synonym)
- Developmental and epileptic encephalopathy 94; DEE94
- Epileptic encephalopathy, childhood-onset (EEOC) — legacy OMIM title
- CHD2-related neurodevelopmental disorders (GeneReviews preferred, broader)
- CHD2-related epilepsy
- CHD2 encephalopathy
- Childhood-onset epileptic encephalopathy with CHD2 mutation
- Myoclonic encephalopathy, CHD2-related

### Information provenance

Knowledge of this disorder derives predominantly from **aggregated, disease-level resources**: multicenter genetic-epilepsy cohorts, systematic literature pooling, and curated databases (ClinVar, ClinGen, OMIM, GeneReviews). The largest single evidence base is a 2025 pooled analysis of **236 individuals** assembled from 74 published articles plus the PERC (Pediatric Epilepsy Research Consortium) Genetics registry (PMID:40934838 ✅). There is *also* a genuine individual-patient/EHR layer: the Coalition to Cure CHD2 has run a digital natural-history study (62 participants, CLIRINX platform), a RARE-X caregiver-reported registry, and a **Ciitizen** medical-record aggregation project that codes real patient records into HPO terms for computational analysis (PMID:39391213 ✅). For dismech purposes, most evidence items will carry `evidence_source: HUMAN_CLINICAL`, with a substantial `MODEL_ORGANISM` and `IN_VITRO` layer for mechanism.

---

## 2. Etiology

### Primary causal factor

CHD2-DEE is a **monogenic, chromatin-mediated developmental disorder**. The proximate cause is heterozygous loss of function of *CHD2*, producing haploinsufficiency of the CHD2 chromatin remodeler in the developing brain. There is no environmental cause, no infectious contribution, and no established multifactorial component to disease *occurrence*.

GeneReviews states the mechanism plainly: *"CHD2-related neurodevelopmental disorders result from haploinsufficiency of CHD2."* The variant-class distribution supports this — *"The overwhelming majority of CHD2 pathogenic variants lead to either truncation of the protein or loss of gene expression by whole-gene deletion."* A 2018 mechanistic review quantified the same point in an early cohort: *"The vast majority (83%, 33/40) of patients carry truncating CHD2 variants, suggesting that the pathogenic mechanism that underpins CHD2-associated epilepsy is haploinsufficiency."*

### Genetic risk factors

**Causal variants.** De novo heterozygous LoF variants in *CHD2* — nonsense, frameshift, canonical splice-site, and whole-gene/multi-exon deletions — are causal, not merely risk-conferring. In the 2025 pooled cohort, **95% (170/179)** of variants with parental testing were confirmed de novo (PMID:40934838 ✅). De Maria et al. found **72.5%** of patients carried truncating variants (Am J Med Genet A 2022;188(2):522–533, DOI:10.1002/ajmg.a.62548 ⚠️ UNVERIFIED PMID).

**Susceptibility (non-DEE) role.** This is a mechanistically important nuance for the KB: *CHD2* variation is *also* a **quantitative risk factor for photosensitivity** in epilepsy generally, not only a cause of DEE. Galizia et al. compared 580 individuals with photosensitive seizures and/or an abnormal photoparoxysmal EEG response against 34,427 population controls and found *"unique CHD2 variation was over-represented in cases overall (P = 2.17 × 10⁻⁵)"*, with 11 unique variants in cases versus 128 in the much larger control set (PMID:25783594 ✅). Within syndromes, the enrichment concentrated in **eyelid myoclonia with absences (EMA)**: *"there was over-representation of unique CHD2 variants (3/36 cases) in the archetypal photosensitive epilepsy syndrome, eyelid myoclonia with absences (P = 3.50 × 10⁻⁴)."* This makes *CHD2* one of the few genes with an established **endophenotype-level** genetic contribution to photosensitivity — a strong candidate for a dismech `relationship_type: SUSCEPTIBILITY` gene annotation alongside the causal one.

**Modifier genes.** No validated human modifier loci have been reported. However, **genetic background is a powerful modifier in mouse**, which is mechanistically suggestive: in a *Chd2* frameshift-truncation model, *"no phenotypes were observed on the pure C57BL/6J background,"* whereas *"crossing these mice onto the 129X1/SvJ genetic background gradually uncovered neurodevelopmental phenotypes"* (Mavashov et al., Epilepsia 2026, DOI:10.1002/epi.70073 ⚠️ UNVERIFIED PMID; and bioRxiv 2025.03.18.643778). This is a defensible basis for a `HUMAN_MODEL_MISMATCH` discussion entry: strain-dependent penetrance in mouse implies unidentified human modifiers, but none are mapped.

**The CHASERR locus as a second genetic etiology.** See §4 — de novo deletion of the adjacent lncRNA gene *CHASERR* causes a **distinct, more severe** disorder by the opposite dosage mechanism.

### Environmental risk factors

None are established for disease *causation*. Advanced paternal age is a general risk factor for de novo mutation across the genome and is a plausible but **unquantified-for-CHD2** contributor; do not assert it without a CHD2-specific source.

### Environmental *precipitants* (distinct from risk factors)

This is where CHD2 is unusual and where dismech should be careful to separate "what causes the disease" from "what triggers the seizures":

1. **Photic stimulation** — the dominant, near-defining trigger. Flickering light, television, sunlight through trees, video screens. GeneReviews: *"Clinical photosensitivity (i.e., seizures triggered by photic stimulation) is a distinguishing feature reported in a total of 80% (20/25) of individuals where it was specifically queried."* The pooled analysis reports **59% (80/136)** (PMID:40934838 ✅), and the adult cohort **64%** (PMID:39601014 ✅).
2. **Self-induction** — a striking behavioral feature where affected children deliberately seek out flicker. Thomas et al.: of 10 patients, *"7 exhibited exquisite clinical photosensitivity; 6 self-induced with the television"* (PMID:25672921 ✅). This is a *behavioral phenotype that is simultaneously a seizure trigger* — a genuine feedback loop worth modeling explicitly as a pathophysiology node.
3. **Fever** — **37% (33/90)** fever-sensitive in the pooled cohort (PMID:40934838 ✅). Suls et al. specifically titled the phenotype a *"fever-sensitive myoclonic epileptic encephalopathy sharing features with Dravet syndrome"* (PMID:24207121 ✅). Note the discrepancy with GeneReviews, which observes that *"febrile seizures, which are characteristic of Dravet syndrome, have only been reported in 11 individuals with CHD2 variants"* — i.e. fever *sensitivity* of established seizures is common, but classic febrile seizures as a presenting event are not. Curate these as two distinct claims.

### Protective factors

No genetic or environmental protective factors are established. The only actionable "protective" intervention is **avoidance of photic triggers** — GeneReviews advises to *"Avoid flickering lights that may provoke seizures."* This is best modeled as a treatment/management action (`MAXO`-annotated behavioral intervention), not a protective factor in the etiologic sense.

### Gene–environment interactions

The single well-supported GxE interaction is **CHD2 genotype × photic environment**. The interaction is dose-graded rather than binary: complete LoF produces DEE with exquisite photosensitivity, while rarer/milder *CHD2* variation raises photosensitivity risk in otherwise typical epilepsies (PMID:25783594 ✅). Critically, the interaction is **conserved across species** — zebrafish *chd2* knockdown *"markedly enhanced mild innate zebrafish larval photosensitivity"* (PMID:25783594 ✅), providing model-organism corroboration of a human GxE effect. That cross-species conservation is unusually strong evidence for a genuine mechanistic interaction rather than an ascertainment artifact.

A second, weaker interaction is **genotype × febrile illness** (37% fever sensitivity), analogous to but milder than the SCN1A/Dravet paradigm.

---

## 3. Phenotypes

### Frequency data — the two principal cohorts

Two independent aggregations give slightly different denominators. Both should be curated, with `population` distinguishing them.

| Phenotype | GeneReviews | Puri 2025 pooled (n=236) | Suggested HPO (verify) |
|---|---|---|---|
| Seizures (any) | 96% (109/113) | ~100% (ascertainment) | HP:0001250 Seizure |
| Developmental delay | 95% (81/85) combined DD/ID | 88% (156/177) | HP:0001263 Global developmental delay |
| Intellectual disability | (within the 95%) | 86% (121/141) | HP:0001249 Intellectual disability |
| Autism / autistic features | 56% (39/70) | 45% (68/150) | HP:0000717 Autism / HP:0000729 Autistic behavior |
| Photosensitivity (clinical) | 80% (20/25) when queried | 59% (80/136) | *see note below* |
| Fever sensitivity | — | 37% (33/90) | HP:0002373 Febrile seizure (approximate) |
| Epileptiform EEG abnormality | — | 88% (122/138) | HP:0002353 EEG abnormality |
| Abnormal MRI | — | 19% | HP:0002500 / HP:0012443 (verify) |
| Male sex | — | 53% (108/205) | — |
| De novo origin | "almost all" | 95% (170/179) | — |

> **HPO caution on photosensitivity.** I could not verify a specific HPO ID for "photosensitive seizure" or "photoparoxysmal EEG response" in this session, and I will not guess one — HPO has multiple similarly-named terms in the seizure-precipitant and EEG-abnormality branches. Look these up with `runoak -i sqlite:obo:hp search "photo"` before curating. This is the single highest-risk term in the entry precisely because it is the disease's most characteristic feature.

### Seizure semiology (the core phenotype cluster)

**Onset.** GeneReviews: *"Seizure onset is typically between ages six months and four years"* with **median onset at 30 months**. Thomas et al. report a **mean of 26 months** across 10 patients (PMID:25672921 ✅). The pooled analysis found a far wider true range: *"Seizure onset ranged from 1 day to 22 years"* (PMID:40934838 ✅), and Chen et al. observed onset from *"3 months to 10 years 5 months"* across 17 patients (PMID:31677157 ✅).

**Onset character.** Distinctively abrupt. GeneReviews: onset is *"explosive in many children, characterized by multiple daily myoclonic and absence seizures."* This "explosive" quality — going from no seizures to many daily seizures over days to weeks — is a useful discriminator in the differential.

**Seizure types**, in rough order of characteristic-ness:

- **Myoclonic seizures** — the signature type; present in **all 10** of Thomas et al.'s patients (PMID:25672921 ✅). HP:0002123 Generalized myoclonic seizure (verify label).
- **Atypical absence / absence seizures** — HP:0007270 Atypical absence seizure; HP:0011147 Typical absence seizure (verify).
- **Myoclonic-atonic seizures** and **drop attacks** — GeneReviews lists *"drop attacks, myoclonus"* and a distinctive *"atonic-myoclonic-absence"* composite seizure. HP:0032794 Myoclonic-atonic seizure (verify).
- **Atonic seizures** — HP:0010819 Atonic seizure.
- **Generalized tonic-clonic / bilateral tonic-clonic** — HP:0002069 (label recently changed to "Bilateral tonic-clonic seizure" — verify).
- **Eyelid myoclonia with absences** — in roughly 10% per the Epilepsiome summary; *CHD2* is *"the first identified cause of the archetypal generalized photosensitive epilepsy syndrome, eyelid myoclonia with absences"* (PMID:25783594 ✅).
- **Focal seizures** — a minority; De Maria et al. found generalized types accounted for **75.5%** of all epilepsies, implying ~25% with focal features (DOI:10.1002/ajmg.a.62548 ⚠️).
- **Epileptic spasms** — rare; 2/17 in Chen et al. (PMID:31677157 ✅). HP:0011097 Epileptic spasm.
- **Status epilepticus** — reported, frequency not well quantified. HP:0002133 Status epilepticus.

**Multiplicity.** *"More than half of affected individuals have multiple seizure types, with a predominance of myoclonic-atonic, myoclonic, and absence seizures."* Evolution to multiple refractory types over months is characteristic and is part of what qualifies the disorder as an epileptic *encephalopathy*.

### Cognitive, developmental, and behavioral phenotypes

**Intellectual disability severity distribution.** GeneReviews: *"intellectual disability ranges from mild (in 7/15 individuals) to severe (8/15 individuals)"* — roughly bimodal, split evenly. The Epilepsiome breakdown gives approximately 30% mild, 25% moderate, 15% severe-profound.

**Regression.** Developmental regression coinciding with seizure onset is a defining feature of the DEE framing (OMIM: *"Affected individuals have cognitive regression and impaired intellectual development"*). Pre-seizure development is inconsistently reported — GeneReviews notes psychomotor development prior to seizures *"can be delayed…but is often not reported and this feature requires further evaluation."* This is an honest, citable **knowledge gap** worth capturing as a `discussions` entry: whether CHD2 encephalopathy is truly seizure-driven regression or an underlying developmental trajectory unmasked by seizure onset is unresolved.

**Language.** Prominent language impairment is repeatedly emphasized, including as a relatively isolated feature in milder presentations (De Maria et al. ⚠️). HP:0000750 Delayed speech and language development; HP:0001344 Absent speech.

**Behavioral and psychiatric.** GeneReviews: *"Challenging behaviors, most often aggression, have been described,"* plus ADHD, anxiety, and rarely psychosis or schizophrenia. The adult cohort is far more granular and more sobering (PMID:39601014 ✅): behavioral issues in **100%**, internalizing features such as anxiety in **71%**, **self-injurious behaviors in 50%**, ASD diagnosed in **71%**.

Candidate HPO terms: HP:0000718 Aggressive behavior; HP:0100716 Self-injurious behavior; HP:0000739 Anxiety; HP:0007018 ADHD; HP:0000717 Autism; HP:0002360 Sleep disturbance.

### Motor, gait, and systemic phenotypes

The adult study identified a cluster that is under-recognized in pediatric reports: *"seizure severity is associated with worse comorbidities such as maladaptive behaviors, gait, gastrointestinal, sleep, and abnormal pain responsiveness"* (PMID:39601014 ✅). Only **43% could ambulate independently** in adulthood. Abnormal pain responsiveness is a notable and easily missed feature.

Cerebellar signs appear in some series — one imaging study reported inferior vermis hypoplasia (7/10) and mild cerebellar atrophy (4/10), suggesting ataxia may be under-reported.

### Dysmorphism and growth

CHD2 haploinsufficiency is characteristically **non-dysmorphic** — GeneReviews describes a *"brain-restricted phenotype."* This is diagnostically useful and is the sharpest clinical discriminator from *CHASERR* deletion, which produces *"shared facial dysmorphisms"* (NEJM 2024). Absence of dysmorphism is worth curating explicitly as a negative finding.

### Progression, severity, and quality-of-life impact

- **Progression:** Seizures are generally most severe in early childhood, but do not reliably remit — **79% of adults still have ongoing seizures** (PMID:39601014 ✅). Some individuals show progressive brain atrophy: *"MRI has shown atrophy that tends to be more posterior and can be progressive,"* with 3 of 4 individuals having sequential imaging showing progressive atrophy.
- **A progressive myoclonic epilepsy mimic:** CHD2-DEE can phenocopy PME — worsening myoclonus, cognitive decline, and ataxia — and has been formally reported as such (Chityala et al., *Epileptic Disorders*, DOI:10.1002/epd2.70196 ⚠️ UNVERIFIED PMID). This matters clinically because it can send workups down an expensive PME/storage-disease path.
- **Quality of life:** No disease-specific validated QoL instrument exists. The Coalition to Cure CHD2 collects HRQoL questionnaires via RARE-X (PMID:39391213 ✅). Caregiver-prioritized burdens, from a 75-participant community poll, ranked in order: **seizure control > behavior > regression > intellectual disability > phenotypic severity > medication side effects > speech**. That ranking is genuinely useful for a KB — it is patient-derived rather than clinician-assumed.

---

## 4. Genetic / Molecular Information

### Causal gene

***CHD2*** (chromodomain helicase DNA-binding protein 2), **15q26.1**, hgnc:1917, OMIM *602119, UniProt O14647, canonical transcript NM_001271.4. The protein is ~1,828 aa (~211 kDa).

### Constraint

*CHD2* is among the most LoF-intolerant genes in the genome: **pLI = 1**, **LOEUF ≈ 0.07–0.17** (gnomAD). This is exactly the constraint profile expected of a haploinsufficient dominant developmental gene and provides strong supporting evidence (ACMG PVS1 applicability) for truncating-variant interpretation.

### Variant spectrum

**Detection rates by method** (GeneReviews): sequence analysis detects **93% (129/139)** of pathogenic variants; chromosomal microarray detects **7% (10/139)** — i.e. whole-gene and multi-exon deletions are a small but non-trivial slice, meaning a negative gene panel does not fully exclude the diagnosis.

**Variant classes:**
- **Truncating (nonsense, frameshift):** the majority — 72.5% (De Maria ⚠️), 83% in an earlier 40-patient series.
- **Splice-site:** canonical and, increasingly, deep-intronic (e.g. ClinVar RCV003740922, c.4593-14A>G).
- **Missense:** a minority, and mechanistically informative — they *"cluster in the functional domains"* and disrupt DNA binding or chromatin remodeling capacity. Missense variants outside functional domains are frequently VUS; an "interdomain" missense variant was associated with the unusual adult-onset pharmacoresistant epilepsy presentation (De Maria ⚠️).
- **Whole-gene deletions / CNVs:** ~7%.
- **Synonymous variants:** numerous benign/likely-benign ClinVar entries exist (e.g. c.3036T>C p.Ser1012=, c.4260A>G p.Ser1420=, c.2098A>C p.Arg700=) — a reminder that ClinVar *CHD2* records include many non-pathogenic classifications.

**Origin:** Overwhelmingly **germline de novo** (95%, 170/179). Somatic *CHD2* mutation occurs in cancers (notably CLL) but is **mechanistically and clinically unrelated** to the neurodevelopmental disorder; do not conflate them in the KB.

**Functional consequence:** **Loss of function.** GeneReviews: *"Loss-of-function predominates; no gain-of-function mechanisms reported"* for germline disease. No dominant-negative mechanism has been established.

### The CHASERR locus — bidirectional dosage sensitivity

This is the most important recent development in CHD2 genetics and deserves a dedicated section in any KB entry.

***CHASERR*** (CHD2 Adjacent, Suppressive Regulatory RNA; OMIM *620993) is a conserved long noncoding RNA gene transcribed immediately upstream of *CHD2* that acts as a **negative cis-regulator** of *CHD2* expression. In mouse, *"Chaserr inhibits expression of Chd2 in cis and is required for postnatal mouse development"* (Rom et al., Nat Commun 2019, DOI:10.1038/s41467-019-13075-8 ⚠️ UNVERIFIED PMID).

In 2024, three unrelated children were reported with **de novo deletions of the CHASERR promoter and first three exons** that spared *CHD2* and its promoter entirely. They had *"severe encephalopathy, shared facial dysmorphisms, cortical atrophy, and cerebral hypomyelination — a phenotype that is distinct from the phenotypes of patients with CHD2 haploinsufficiency."* Mechanistically, *"The CHASERR deletion results in increased CHD2 protein abundance in patient-derived cell lines and increased expression of the CHD2 transcript in cis"* (NEJM 2024;DOI:10.1056/NEJMoa2400718; the medRxiv preprint is PMID:38496558 ✅ — the NEJM PMID was not resolved ⚠️).

The authors' conclusion is the headline: *"these findings indicate that CHD2 has bidirectional dosage sensitivity in human disease."* This is also **the first demonstration that haploinsufficiency of a lncRNA causes a Mendelian disease**. OMIM has assigned the resulting phenotype its own entry: **#621012, NEDFSAB** (neurodevelopmental disorder with dysmorphic facies, absent speech and ambulation, and brain abnormalities).

**KB implication:** *CHD2* too little → DEE94, non-dysmorphic, brain-restricted. *CHD2* too much (via CHASERR loss) → NEDFSAB, dysmorphic, hypomyelinating, more severe. These are two distinct dismech entries linked by an inverse-dosage relationship — an excellent candidate for a `Grouping` with `grouping_basis: SHARED_GENE_FAMILY` / `SHARED_MECHANISM`, or for a mechanistic hypothesis capturing the dosage-window model.

### Epigenetic information

CHD2 *is* an epigenetic regulator, and its loss leaves a measurable epigenomic fingerprint. **A validated DNA methylation episignature exists for CHD2 haploinsufficiency**: *"CHD2 haploinsufficiency is one of several genetic conditions with a distinct episignature"* (PMID:39391213 ✅). GeneReviews confirms clinical utility — DNA methylation episignatures *"can help resolve variants of uncertain significance in CHD2."* A refinement of the CHD2 episignature specifically in genetically unsolved DEEs has been published (medRxiv 2023.10.11.23296741).

This is functionally significant: the episignature is simultaneously (a) a diagnostic test, (b) a functional-evidence source for ACMG variant classification, and (c) *"a strong biomarker candidate"* for future clinical trials (PMID:39391213 ✅).

### Chromosomal abnormalities

15q26.1 deletions encompassing *CHD2* — ranging from intragenic multi-exon deletions to larger contiguous-gene deletions — account for ~7% of cases and are detected by CMA. Larger 15q26 deletions may add non-neurological features from neighboring genes.

---

## 5. Environmental Information

- **Environmental factors:** None causally implicated. No toxin, radiation, pollutant, or occupational exposure is associated with *CHD2* de novo mutation beyond generic de novo mutational processes.
- **Lifestyle factors:** Not applicable to causation. Relevant only to seizure management (sleep deprivation and screen/flicker exposure as generic and CHD2-specific precipitants respectively).
- **Infectious agents:** None. Febrile illness acts as a **non-specific seizure precipitant** (37% fever sensitivity), not as an etiologic agent — any pathogen producing fever can do this. Curate as a precipitant, never as an infectious cause.

**The one environmental exposure that genuinely matters** is photic: television, video screens, sunlight flicker, strobe lighting. It is a seizure trigger of unusual potency in this disorder and the target of the only broadly applicable non-pharmacologic intervention.

---

## 6. Mechanism / Pathophysiology

### Protein architecture

CHD2 contains, N→C: **tandem chromodomains**, an **SNF2-family ATPase/helicase domain**, and a C-terminal **DNA-binding domain**. Notably, *"The N-terminal chromodomains serve an autoinhibitory function, while deletion of this region increases both DNA-binding and ATPase activities."* Additionally, *"The C-terminus of CHD2 also associates with a poly ADP-ribose (PAR) binding domain that is involved in DNA damage repair"* — implying a secondary genome-maintenance role distinct from its transcriptional one.

### Core molecular function

CHD2 is an ATP-dependent chromatin remodeler that *"use[s] the energy from ATP hydrolysis to remodel chromatin into periodic nucleosome arrays."* Its most mechanistically specific activity is **histone variant deposition**: *"CHD2 interacts with H3.3, a histone variant incorporated into the nucleosome at transcriptionally active genes,"* and *"the chromodomain of CHD2 facilitates H3.3 incorporation into the nucleosome, poising genes necessary for differentiation for expression."*

This gives a clean, causally-legible mechanism: **CHD2 pre-loads differentiation genes with H3.3-containing nucleosomes so they are poised to fire at the right developmental moment.** Halve the CHD2 and you do not abolish those genes — you **mistime** them. That framing explains why the disorder is developmental-window-dependent rather than a simple constitutive deficiency.

### Recruitment and interaction partners

CHD2 does not choose its own targets; it is recruited by cell-type-specific transcription factors:
- **NKX2-1** in interneuron lineages — *"CHD2 ChIP-qPCR revealed an overlap with NKX2-1 binding at three candidate genes important for interneuron development."* CHD2 is itself an NKX2-1 direct target, and the two *"could coregulate cIN gene expression by cobinding shared genomic regulatory regions"* (Meganathan et al., PNAS 2017, DOI:10.1073/pnas.1712365115 ⚠️; and Sci Rep 2022, PMID:36115870 ✅).
- **REST (RE1-silencing transcription factor)** in progenitors — *"candidate ChIP-seq revealed CHD2 binding at REST,"* and loss of CHD2 reduces REST expression. Since REST is the master repressor keeping neuronal genes off in non-neuronal and progenitor cells, this is a plausible upstream node for premature neuronal differentiation.

### The causal chain (upstream → downstream)

**Node 1 — MOLECULAR: CHD2 haploinsufficiency.** De novo truncating variant / whole-gene deletion → ~50% reduction in functional CHD2 protein. `biological_scale: MOLECULAR`.

**Node 2 — MOLECULAR: Impaired H3.3 deposition and defective chromatin remodeling at differentiation loci.** Reduced ATP-dependent nucleosome remodeling; loss of poising at developmental genes. GO:0043044 ATP-dependent chromatin remodeling; GO:0043486 histone exchange (verify).

**Node 3 — CELLULAR: Loss of neural progenitor self-renewal / premature neuronal differentiation.** *"Chd2 is predominantly expressed in Pax6+ radial glia in the VZ/SVZ from E12–E18"*; *"Chd2 knockdown promotes premature neuronal differentiation during embryonic mouse cortical development due to a decrease in Pax6+ neural progenitor cells and an increase in Tbr2+ intermediate progenitor cells."* The interpretation: *"Chd2 deficiency suppresses the self-renewal capacity of the radial glia and instead promotes premature neuronal differentiation."* Cell types: CL:0000681 radial glial cell; CL:0000031 neuroblast.

**Node 4 — CELLULAR: Deficient cortical GABAergic interneuron generation and maturation.** This is likely the key seizure-relevant node. *"CHD2 gene expression levels gradually increase during the differentiation of human embryonic stem cells (hESCs) to cortical interneurons,"* and *"CRISPR-Cas9 mediated biallelic knockout of CHD2 resulted in fewer TUBB3+ neurons with shorter neurites."* GeneReviews: *"Complete CHD2 loss in a human stem cell model resulted in defects in the development of inhibitory interneurons and altered expression of genes important in neurotransmission."* Impaired interneuron differentiation is described as a *"well established… pathogenic mechanism in epilepsy."* Cell types: CL:0000617 GABAergic neuron; CL:0011005 GABAergic interneuron (verify).

**Node 5 — CELLULAR/TISSUE: Reduced neuron number and altered excitatory/inhibitory balance.** *"A heterozygous Chd2 loss mouse showed deficits in neuronal development including reduced number of both excitatory and inhibitory neurons and severe impairments in long-term memory"* (Kim et al., Neuron 2018;100:1180–1193.e6 ⚠️ UNVERIFIED PMID). *"Loss of a single Chd2 copy leads to deficits in neuron proliferation and a shift in neuronal excitability."*

**Node 6 — TISSUE: Cortical network hyperexcitability with altered background oscillations.** Mouse ECoG shows *"a global reduction in the total power of background activity"* plus *"increased susceptibility to seizures induced by acute administration of 4-aminopyridine"* (Mavashov et al. ⚠️). Notably, the background-EEG change is a *state* abnormality independent of ictal events — a candidate translational biomarker.

**Node 7 — ORGANISM: Photosensitive, myoclonic-predominant generalized epilepsy + developmental encephalopathy.** Seizures, regression, ID, ASD.

**A parallel/feedback loop worth modeling separately:** Node 4/6 (cortical hyperexcitability with occipital-predominant photic drive) → photosensitivity → **self-induction behavior** → increased seizure burden → further encephalopathy. The self-induction arm is behavioral, not purely neurophysiological, and is unusual enough to merit its own node.

### Suggested GO terms (verify all with OAK)

Biological process: GO:0006338 chromatin remodeling; GO:0043044 ATP-dependent chromatin remodeling; GO:0006325 chromatin organization; GO:0034728 nucleosome organization; GO:0006357 regulation of transcription by RNA polymerase II; GO:0030182 neuron differentiation; GO:0050767 regulation of neurogenesis; GO:0021895 cerebral cortex neuron differentiation; GO:0007399 nervous system development; GO:0006281 DNA repair (for the PAR-binding arm).
Molecular function: GO:0004386 helicase activity; GO:0003682 chromatin binding; GO:0016887 ATP hydrolysis activity; GO:0140658 ATP-dependent chromatin remodeler activity (verify).
Cellular component: GO:0005634 nucleus; GO:0000785 chromatin.

### Other mechanism domains

- **Metabolic changes:** None established. No metabolic biomarker, no storage material, no enzyme deficiency. This is a *negative* finding worth recording because it is what distinguishes CHD2 from the true progressive myoclonic epilepsies it can mimic.
- **Immune involvement:** None established.
- **Tissue damage mechanisms:** Progressive posterior-predominant cerebral atrophy is documented, but its driver — seizure-related excitotoxic injury versus a primary progressive neurodevelopmental/degenerative process — is **unresolved**. Another good `KNOWLEDGE_GAP` entry.
- **Protein dysfunction:** Loss of function via truncation/degradation or, for missense variants in functional domains, impaired DNA binding and remodeling. No aggregation, no misfolding pathology.
- **Single-cell / cell-type specificity:** An important, explicitly-flagged gap — CHD2 is expressed in **oligodendrocytes** *"almost to the same extent as neurons, but…did not study this cell type in their mouse model"* (PMID:39391213 ✅). Given that *CHASERR* deletion (excess CHD2) produces **cerebral hypomyelination**, an oligodendrocyte arm of CHD2 biology is strongly suspected and essentially unexplored. CL:0000128 oligodendrocyte.

---

## 7. Anatomical Structures Affected

**Organ level.** The phenotype is **brain-restricted** — GeneReviews emphasizes that affected individuals show a *"brain-restricted phenotype,"* implying *"a unique role for CHD2"* in human brain despite ubiquitous expression. No primary cardiac, renal, hepatic, or skeletal involvement. Body system: nervous system only. Secondary involvement is downstream of neurological disability — gastrointestinal dysfunction (constipation, feeding difficulty) and sleep disturbance, both prominent in adults (PMID:39601014 ✅), and injury risk from drop attacks.

**Anatomical sites (UBERON candidates, verify):**
- UBERON:0000955 brain — primary
- UBERON:0000956 cerebral cortex — the principal site of dysgenesis and hyperexcitability
- Occipital/posterior cortex — implicated by both the posterior-predominant atrophy pattern and by photosensitivity physiology (visual cortex as the photic entry point). *"Atrophy that tends to be more posterior and can be progressive."* UBERON:0016530 occipital cortex (verify).
- UBERON:0002037 cerebellum, UBERON:0004720 cerebellar vermis — inferior vermis hypoplasia 7/10 and mild cerebellar atrophy 4/10 in one imaging series
- UBERON:0002421 hippocampal formation — hippocampal signal alterations 4/10, volume loss 2/10; memory deficits in mouse
- Ventricular/subventricular zone — the developmental site of the progenitor defect (verify the correct UBERON ID)
- Medial ganglionic eminence — origin of the NKX2-1⁺ interneurons most affected (verify)

**Lateralization:** Bilateral and generally symmetric. Generalized epilepsy with bilateral EEG discharges; atrophy is diffuse-to-posterior rather than focal or asymmetric.

**Cell populations (CL candidates, verify):** CL:0000617 GABAergic neuron and CL:0011005 GABAergic interneuron (primary); CL:0000681 radial glial cell (developmental origin); CL:0000679 glutamatergic neuron and CL:0000598 pyramidal neuron (also reduced in number); CL:0000031 neuroblast; CL:0000128 oligodendrocyte (suspected, understudied).

**Subcellular:** GO:0005634 nucleus; GO:0000785 chromatin. Interestingly, Xenopus work found CHD2 *"localizes to microtubules of the mitotic spindle"* (PMID:39391213 ✅) — a non-canonical localization that, if confirmed, could link CHD2 to progenitor division mechanics rather than transcription alone.

---

## 8. Temporal Development

**Onset.** Typical seizure onset **6 months to 4 years**, median **30 months** (GeneReviews), mean **26 months** (PMID:25672921 ✅). Full observed range **1 day to 22 years** (PMID:40934838 ✅). Onset pattern is characteristically **acute to subacute and "explosive"** — multiple daily seizures appearing over a short interval — rather than insidious. Developmental delay may precede seizures but is inconsistently documented.

**Stages (a reasonable natural-history model, not a formal staging system — none exists):**
1. **Pre-seizure (birth–~2y):** normal to mildly delayed development.
2. **Explosive onset / encephalopathic phase (~1–4y):** abrupt multiple daily myoclonic and absence seizures; developmental plateau or regression; photosensitivity emerges; self-induction may begin.
3. **Established refractory phase (childhood):** multiple seizure types, drug resistance, ID consolidates, ASD and behavioral features become prominent.
4. **Adult phase:** seizures persist in **79%**; photosensitivity persists in **64%**; behavioral and psychiatric burden dominates; ambulation independent in only **43%** (PMID:39601014 ✅).

**Progression rate and course.** Variable; broadly **chronic and lifelong** with an early-childhood peak in seizure burden. The course is *not* classically progressive-degenerative, but progressive posterior atrophy in a subset and PME-mimicking trajectories in others mean "stable after early childhood" would be an overstatement. Curate as chronic with variable progression rather than as a single course descriptor.

**Remission.** Uncommon and treatment-mediated when it occurs. GeneReviews: *"Only 13 of 33 affected individuals have been reported to be seizure free on ASM treatment for two to five years"* (≈39%). Spontaneous remission is not established.

**Critical periods.** Two matter therapeutically. (1) The **prenatal/early-postnatal progenitor window** (mouse E12–E18 equivalent), when CHD2 governs radial glial self-renewal and interneuron specification — likely already passed by the time of diagnosis, which is a hard constraint on any restorative therapy. (2) The **early-childhood seizure-onset window**, when seizure control might plausibly protect development. Whether intervening in window 2 alters cognitive outcome is unknown and is arguably the central open clinical question in the disease.

---

## 9. Inheritance and Population

**Prevalence.** *"The prevalence of CHD2-related neurodevelopmental disorders is not known"* (GeneReviews) — this should be recorded as `prevalence_class: NOT_YET_DOCUMENTED` or `UNKNOWN` rather than fabricated. Available proxies (all diagnostic yields, **not** population prevalence — do not convert them):
- **1.2%** of epileptic encephalopathies in the original targeted-resequencing cohort (PMID:23708187 ✅).
- **~1%** of individuals in DEE cohorts carry a *CHD2* variant (GeneReviews).
- **0.25%** of individuals in broad comprehensive-testing cohorts.
- *CHD2* was the **fourth most highly implicated gene** in one neurodevelopmental-disorder-plus-epilepsy cohort.

A defensible order-of-magnitude inference — clearly flagged as inference, not data — is a birth prevalence in the low single digits per 100,000, but I would not curate a number without a primary source.

**Inheritance.** **Autosomal dominant**, de novo in ~95%. GeneReviews: *"CHD2-related neurodevelopmental disorders are autosomal dominant disorders typically caused by a de novo pathogenic variant."*

Suggested `Inheritance` block: HP:0000006 Autosomal dominant inheritance. This is **not** a digenic/oligogenic disorder.

**Penetrance.** *"Penetrance for CHD2-related neurodevelopmental disorders is unknown but assumed to be complete."* Caveat: *"a small number of instances"* of inheritance from **mildly affected parents** are documented — so either penetrance is incomplete or expressivity is wide enough that mild carriers go unrecognized. Both readings are live.

**Expressivity.** Markedly **variable** — from severe DEE with profound ID to adult-onset non-syndromic epilepsy with preserved cognition. De Maria et al. describe *"a wide spectrum of conditions"* (⚠️).

**Genetic anticipation.** Not applicable — not a repeat-expansion disorder.

**Germline mosaicism.** Documented. GeneReviews: *"Presumed parental germline mosaicism was reported in a family with unaffected parents and sib recurrence."* This is the basis for counseling that recurrence risk after a de novo case is *"slightly greater than that of the general population."*

**Recurrence risk.** ~1% or slightly higher for siblings when the variant is confirmed de novo in the proband (germline mosaicism); **50%** per pregnancy if a parent carries the variant.

**Founder effects / carrier frequency / consanguinity.** None, none, and no role respectively — a dominant de novo disorder in a gene under maximal LoF constraint (pLI=1) will not accumulate carriers or founder haplotypes.

**Demographics.** No ethnic or geographic predilection reported. Cohorts span Europe, North America, China, and Australia. Sex ratio approximately equal with a slight male excess: **53% male (108/205)** (PMID:40934838 ✅) — consistent with chance and with the general male excess in ascertained neurodevelopmental cohorts; do not over-interpret. Age distribution is lifelong from early childhood; the adult population is real but historically under-described (PMID:39601014 ✅).

---

## 10. Diagnostics

### Genetic testing — the definitive route

GeneReviews: *"The diagnosis of a CHD2-related neurodevelopmental disorder is established in a proband with suggestive findings and a heterozygous pathogenic variant in CHD2 identified by molecular genetic testing."*

**Recommended approach.** *"An epilepsy or intellectual disability multigene panel that includes CHD2 and other genes of interest…is most likely to identify the genetic cause."* Exome sequencing is advantaged because it *"includes genes recently identified as causing intellectual disability whereas some multigene panels may not."*

| Method | Yield / role |
|---|---|
| Multigene epilepsy/ID panel | First-line; must include CHD2 and CNV calling |
| Exome sequencing (WES) | Broad, catches newly-described genes |
| Genome sequencing (WGS) | Best for deep-intronic splice variants, structural variants, and — critically — **CHASERR-locus deletions, which panels and exomes will miss entirely** |
| Chromosomal microarray | **7% (10/139)** of pathogenic variants; detects whole-gene/multi-exon deletions |
| Single-gene sequencing | Only for targeted familial variant testing |
| Karyotype / FISH | Not indicated |
| mtDNA / repeat expansion testing | Not indicated |

> **A practical warning worth curating:** if a child has the classic CHD2 clinical picture but panel/exome is negative, escalate to **genome sequencing** rather than stopping. The *CHASERR* phenotype is caused by a non-coding deletion adjacent to *CHD2* that standard coding-focused pipelines will not report.

### Omics-based diagnostics

**DNA methylation episignature** is the standout, and is clinically actionable today: a validated CHD2 episignature *"can help resolve variants of uncertain significance in CHD2"* (GeneReviews; PMID:39391213 ✅). It functions as orthogonal functional evidence for ACMG classification (PS3-type) and can also *exclude* a provisional diagnosis when negative. Transcriptomics, proteomics, and metabolomics have **no established diagnostic role**.

### Electrophysiology

**EEG** is the key functional test. Epileptiform abnormalities in **88% (122/138)** (PMID:40934838 ✅). Characteristic findings:
- **Generalized spike-wave** discharges (GeneReviews).
- **Photoparoxysmal response (PPR)** on intermittent photic stimulation — but here is an important and clinically counterintuitive point: GeneReviews notes that a PPR *"has only been recorded in two affected individuals,"* despite clinical photosensitivity in ~60–80%. **Clinical photosensitivity in CHD2 markedly exceeds laboratory-demonstrable photoparoxysmal response.** Do not use a negative IPS study to exclude photosensitivity or to lift precautions. Curate these as two distinct phenotypes with very different frequencies.
- Background slowing and, in mouse, reduced total background power — a candidate quantitative biomarker.

Other electrophysiology (EMG, nerve conduction, ECG) has no established role.

### Neuroimaging

**MRI is normal in the majority** — abnormal in only **19%** (PMID:40934838 ✅); one series found no abnormality in 14 of 17. When abnormal: cerebral atrophy (posterior-predominant, sometimes progressive on serial imaging — 3 of 4 with sequential studies), hippocampal signal change (4/10) with volume loss (2/10), inferior vermis hypoplasia (7/10), mild cerebellar atrophy (4/10). PET, CT, and ultrasound have no specific role.

### Laboratory tests and biomarkers

**There is no diagnostic blood, urine, or CSF biomarker.** No enzyme assay, no metabolite. Routine metabolic workup is normal — which is itself diagnostically useful when excluding PME/storage disease. Biopsy and histopathology have **no role**; there is no characteristic pathology.

### Clinical criteria and differential diagnosis

No consensus clinical diagnostic criteria exist — diagnosis is genetic. GeneReviews notes the differential must consider *"all genes known to be associated with epileptic encephalopathy (~90 have been identified)."*

Key differentials:
- **Dravet syndrome (SCN1A)** — the closest mimic; Suls et al. framed CHD2 as *"sharing features with Dravet syndrome."* Discriminators: CHD2 has later onset (median 30 mo vs. <12 mo), true febrile seizures are uncommon, and photosensitivity/self-induction is far more prominent.
- **Myoclonic-atonic epilepsy (Doose syndrome)** — overlapping semiology; genetic testing distinguishes.
- **Lennox-Gastaut syndrome** — CHD2 variants are found in LGS cohorts.
- **Eyelid myoclonia with absences (Jeavons syndrome)** — CHD2 is the first identified genetic cause (PMID:25783594 ✅).
- **Progressive myoclonic epilepsies** (Unverricht-Lundborg, Lafora, NCL, MERRF) — CHD2 can phenocopy PME (DOI:10.1002/epd2.70196 ⚠️); normal metabolic/storage workup and absence of a defining biopsy finding point away from true PME.
- **Other chromatin-remodeler NDDs** — CHD8 (autism/macrocephaly), CHD7 (CHARGE), CHD1/CHD3/CHD4.
- **CHASERR-deletion disorder (NEDFSAB, OMIM #621012)** — dysmorphic, hypomyelinating, more severe.

### Screening

There is **no newborn screening, no carrier screening, and no population screening** for CHD2 — appropriately, given a de novo dominant disorder with no presymptomatic intervention. Cascade testing in families is limited to confirming de novo status in parents (which informs recurrence risk) and testing at-risk relatives when a parent is found to carry the variant.

---

## 11. Outcome / Prognosis

**Survival and mortality.** No published disease-specific survival curve, life-expectancy figure, or mortality rate. Adults into their mid-forties are reported (age range 18–45, median 21 in the adult cohort, PMID:39601014 ✅), so the condition is compatible with survival into at least middle adulthood. **SUDEP risk should be presumed elevated** given refractory generalized epilepsy with tonic-clonic seizures, but I found **no CHD2-specific SUDEP data** — do not assert a rate.

**Seizure outcome.** Poor. GeneReviews: *"Most individuals remain refractory to treatment and require multiple anti-seizure medications. Only 13 of 33 affected individuals have been reported to be seizure free on ASM treatment for two to five years"* (≈39%). In adulthood, **79% still have ongoing seizures** (PMID:39601014 ✅).

**Cognitive and functional outcome.** Intellectual disability in ~86–95%, ranging mild to severe with a roughly even split at the extremes. In adults: independent ambulation in only **43%**; ASD in **71%**; behavioral issues in **100%**; self-injury in **50%**; anxiety/internalizing features in **71%** (PMID:39601014 ✅). Independent living is not the expected outcome.

**Complications.** Injury from drop attacks and myoclonic-atonic seizures; status epilepticus; aspiration and feeding difficulty; gastrointestinal dysmotility/constipation; sleep disturbance; ASM adverse effects (a top-seven caregiver concern); self-injurious behavior; caregiver burden.

**Recovery potential.** Developmental regression is generally **not recovered**. There is no evidence that seizure control reverses established cognitive impairment, though the possibility that early control protects trajectory remains an open and important question.

**Prognostic factors.** The single most useful published prognostic signal comes from the adult cohort: *"seizure severity is associated with worse comorbidities such as maladaptive behaviors, gait, gastrointestinal, sleep, and abnormal pain responsiveness"* (PMID:39601014 ✅). A relative genotype-phenotype association has been suggested — the Chinese cohort reported that *"The phenotypes, especially seizure control and fever sensitivity, and genotypes had a relative association"* — but no robust, replicated genotype-based prognostic rule exists. Earlier onset and truncating variants trend toward greater severity, and interdomain missense variants toward milder/later-onset presentations, but these are trends, not predictors.

**Prognostic biomarkers.** None validated. Quantitative background-EEG measures are the most promising candidate, supported by both the mouse background-power finding and the human EEG abnormality rate.

---

## 12. Treatment

### The honest headline

**There is no disease-specific or targeted therapy, and no evidence-based ASM algorithm.** GeneReviews: *"At this time, no specific guidelines regarding choice of specific anti-seizure medications exist, as the best regimen for CHD2-related neurodevelopmental disorders is not yet established."* The Epilepsiome concurs: *"Thus far, there is no specific recommended treatment regimen for patients with CHD2 mutations."* And the 2024 roadmap: *"there are currently no targeted therapies available for CHD2-related disorders"* (PMID:39391213 ✅).

I searched specifically for CHD2 ASM-response cohort data and **did not find a published head-to-head comparison**. This absence should be curated as an explicit knowledge gap rather than papered over with generalized-epilepsy inferences.

### Pharmacotherapy — practice-based, not evidence-based

Treatment follows generalized/myoclonic-epilepsy principles: broad-spectrum agents (valproate, levetiracetam, clobazam, lamotrigine with caution, topiramate, zonisamide, ethosuximide for absences, clonazepam for myoclonus). **Sodium-channel blockers (carbamazepine, oxcarbazepine, phenytoin, lamotrigine in some patients) can aggravate myoclonic and absence seizures in generalized epilepsies** — a standard and important caution, but note that I found **no CHD2-specific aggravation data**, so this should be curated as general myoclonic-epilepsy practice rather than a CHD2-specific claim.

Suggested annotation pattern:
```yaml
treatment_term:
  preferred_term: Pharmacotherapy
  term: {id: NCIT:C15986, label: Pharmacotherapy}
  therapeutic_agent:
  - preferred_term: valproic acid
    term: {id: CHEBI:39867, label: valproic acid}   # verify with OAK
```
CHEBI candidates requiring verification: valproic acid, levetiracetam, clobazam, clonazepam, lamotrigine, topiramate, ethosuximide, zonisamide, cannabidiol, fenfluramine. **Per prior project experience, prefer CHEBI over NCIT for `therapeutic_agent` — NCIT drug terms frequently fail dynamic-enum validation.**

**Pharmacogenomics:** No CHD2-specific pharmacogenomic guidance exists. Standard CPIC guidance (e.g. HLA-B*15:02 and carbamazepine) applies as it would to any patient.

**Ketogenic diet:** Reported ineffective in the small number tried — *"Ketogenic diet was not effective in three affected individuals"* (GeneReviews). n=3 is very weak evidence; curate the number, not a conclusion. MAXO:0000088 dietary intervention.

**Fenfluramine:** I searched specifically and found **no CHD2 case series**. It is used in Dravet and LGS and is mentioned in the roadmap as an example of successful drug repurposing in a related disorder, but there is no CHD2 evidence. Do not curate it as a CHD2 treatment.

### Non-pharmacologic and supportive management

- **Photic-trigger avoidance** — the only CHD2-specific intervention with a clear rationale. GeneReviews: counsel that *"exposure to intensely flickering lights may provoke seizures including eyelid myoclonias, absence seizures, and generalized tonic-clonic seizures."* Practically: blue/Z1 tinted lenses, screen management, avoidance of strobe environments, and — given self-induction — behavioral strategies to interrupt the seeking behavior.
- **Early intervention and education** — ages 0–3 early intervention; 3–5 developmental preschool; ongoing special education, speech, occupational, and physical therapy. MAXO:0000011 physical therapy; speech therapy term (verify).
- **Behavioral intervention** — *"Children may qualify for and benefit from interventions used in treatment of autism spectrum disorder, including applied behavior analysis (ABA)."*
- **Genetic counseling** — MAXO:0000079 genetic counseling.
- **Supportive care** — MAXO:0000950 supportive care.
- **Surgery/VNS** — no CHD2-specific data; resective surgery is not rational for a generalized genetic epilepsy. VNS/corpus callosotomy for drop attacks would follow generic drug-resistant-generalized-epilepsy practice.

### Advanced therapeutics in development

This is the most dynamic part of the field (all from PMID:39391213 ✅ unless noted):

- **CHD2-upregulating ASOs — the lead strategy.** *"One of the most promising approaches for CHD2-RD is using antisense oligonucleotides…to increase CHD2 expression to overcome haploinsufficiency."*
- **CHASERR-targeting ASOs — the most elegant strategy.** Because CHASERR is a negative cis-regulator, knocking it down *raises* CHD2: in mice, *"targeting Chaserr…leads to an increase of CHD2 messenger RNA."* The 2024 human CHASERR-deletion data both validate the target and **define its therapeutic window** — too much CHD2 causes a *worse* disease. Any CHASERR-directed therapy must therefore titrate into a narrow dosage band, which is a real and specific development risk. A practical obstacle: *"CHASERR was presented to the n-Lorem Foundation but was not accepted due in part to the lack of a pharmacodynamic biomarker."*
- **Fusion-transcript induction** — a newer approach reported to upregulate haploinsufficient CHD2 (bioRxiv 2025.05.28.656657).
- **miRNA modulation**, **stop-codon read-through** (nonsense variants only), and **targeted drug repurposing screens** in animal models, *"currently underway."*
- **Gene replacement is largely off the table:** AAV vectors cannot carry the >5 kb CHD2 coding sequence, and *"the cis-acting feedback loop between CHD and CHASERR would likely introduce additional challenges."*

**Delivery constraint:** all candidates must *"cross the blood–brain barrier or be injected directly into the cerebrospinal fluid"* — i.e. intrathecal ASO delivery on the nusinersen/tofersen model.

If the KB entry uses the `antisense_oligonucleotide_therapy` module, note that the CHD2 approach is a **fourth mechanism class not currently in that module** — neither RNase H knockdown of a pathogenic transcript, nor splice modulation, nor steric translation blockade, but **upregulation of a haploinsufficient gene via knockdown of its cis-repressive lncRNA**. That is a genuine gap in the existing module and worth flagging.

**Clinical trials:** I found **no registered interventional trial for a CHD2-targeted therapy**. Do not populate `clinical_trials` with an NCT unless one is verified on ClinicalTrials.gov at curation time.

---

## 13. Prevention

**Primary prevention:** Not possible. De novo mutations in a constrained gene are not preventable by any known modifiable exposure.

**Secondary prevention:** Early genetic diagnosis is the actionable lever. Rapid panel/exome testing in early-onset DEE enables trigger counseling, avoidance of aggravating ASMs, early developmental intervention, accurate recurrence counseling, and research/trial eligibility. There is no population screening program and none is warranted.

**Tertiary prevention (preventing complications) — the substantive category here:**
- **Photic-trigger avoidance** to reduce seizure burden.
- **Injury prevention** — protective headgear for drop attacks; supervision.
- **Avoiding seizure-aggravating ASMs.**
- **Seizure action plans and rescue medication** for status epilepticus.
- **Proactive management** of the adult-emergent comorbidity cluster — gait, GI, sleep, behavior, pain responsiveness (PMID:39601014 ✅). The adult data argue for surveillance of these domains rather than reactive management.

**Genetic counseling and reproductive prevention.** Counseling should cover: ~95% de novo origin; ~1% or slightly higher sibling recurrence risk from germline mosaicism; 50% transmission risk if a parent carries the variant; testing of both parents to establish de novo status. **Prenatal diagnosis and preimplantation genetic testing are technically available** once the familial variant is known — most relevant for the germline-mosaicism scenario and for affected/mildly-affected parents.

**Immunization:** No disease-specific vaccine strategy. Routine childhood immunization should proceed normally; given 37% fever sensitivity, prophylactic antipyretics around vaccination are a reasonable practice-level consideration (extrapolated from Dravet practice — **not CHD2-evidenced**, so flag as such).

**Public health / environmental interventions:** Broad flicker-safety standards for broadcast and gaming content (the "Pokémon shock" regulatory lineage) benefit photosensitive individuals generally, including CHD2 patients. This is a real but non-specific intervention.

---

## 14. Other Species / Natural Disease

**Taxonomy of orthologs:**
| Species | NCBI Taxon | Gene | Notes |
|---|---|---|---|
| *Homo sapiens* | NCBITaxon:9606 | *CHD2* (NCBI Gene 1106) | |
| *Mus musculus* | NCBITaxon:10090 | *Chd2* | Principal model |
| *Danio rerio* | NCBITaxon:7955 | *chd2* | Photosensitivity model |
| *Xenopus tropicalis/laevis* | NCBITaxon:8364 / 8355 | *chd2* | Spindle-localization finding |
| *Drosophila melanogaster* | NCBITaxon:7227 | *kis* (kismet, related CHD) | Distant ortholog |

**Naturally occurring disease in other species:** **None reported.** I found no OMIA entry, no veterinary case series, and no naturally occurring CHD2-related epilepsy in companion animals or wildlife. All animal disease is experimentally induced. Record this as a clear negative.

**Breed (VBO):** Not applicable — no breed-associated natural disease.

**Comparative biology.** CHD2 is deeply conserved across vertebrates in both sequence and function, and — importantly — the *photosensitivity phenotype itself* is conserved: *chd2* knockdown *"markedly enhanced mild innate zebrafish larval photosensitivity"* (PMID:25783594 ✅). Conservation of a *specific, unusual clinical feature* across ~400 million years of divergence is strong evidence that the human photosensitivity is a direct consequence of CHD2 loss rather than a downstream epiphenomenon. The *Chaserr* lncRNA is likewise conserved and functionally equivalent in mouse.

**Zoonotic potential / cross-species transmission:** Not applicable — a germline genetic disorder.

---

## 15. Model Organisms

### Zebrafish (*Danio rerio*, NCBITaxon:7955)

The best model for the **seizure and photosensitivity** phenotypes. Suls et al. established it alongside the human genetics: *"They knocked down chd2 in zebrafish, and chd2-knockdown larvae exhibited altered locomotor activity, with field-potential recordings revealing epileptiform discharges similar to seizures in affected persons"* (PMID:24207121 ✅). Galizia et al. extended it to the defining feature: *"Knockdown of chd2 in zebrafish with targeted morpholino results in larvae displaying seizure-like behavior and photosensitivity, recapitulating the phenotype seen in humans"* (PMID:25783594 ✅). Morphant larvae also show *"pericardial edema, microcephaly, body curvature, absent swim bladder, stunted growth, and epileptiform discharges"* (Baraban lab, UCSF).

**Recapitulation:** Excellent for seizures and photosensitivity — arguably the only model that captures the disease's signature feature. **Limitations:** morpholino knockdown carries well-known off-target and toxicity concerns; some phenotypes (edema, curvature) are non-specific morphant artifacts; larval models cannot address cognition, ASD-like behavior, or long-term progression. Primary application: **high-throughput drug repurposing screens**.

### Mouse (*Mus musculus*, NCBITaxon:10090)

The best model for **development, circuits, and cognition**; the weakest for seizures.

- **Kim et al. (Neuron 2018;100:1180–1193.e6 ⚠️ UNVERIFIED PMID)** — "Chd2 Is Necessary for Neural Circuit Development and Long-Term Memory." *Chd2* haploinsufficiency *"compromises cortical development, synaptic function, and memory in mice"*; heterozygotes show *"reduced number of both excitatory and inhibitory neurons and severe impairments in long-term memory."*
- **Mavashov et al. (Epilepsia 2026, DOI:10.1002/epi.70073 ⚠️; bioRxiv 2025.03.18.643778)** — a frameshift-truncation model. *"Heterozygous and homozygous Chd2 mutant mice demonstrate reduced CHD2 expression, alteration in background electrocorticographic (ECoG) oscillations, behavioral deficits, and an increased susceptibility to seizures."* Specifically: a *"global reduction in the total power of background activity"* and increased susceptibility to 4-aminopyridine-induced seizures; on the 129X1/SvJ background, motor deficits including clasping and rotarod impairment, and growth retardation in homozygotes.
- **C-terminal deletion model:** *"Mice with homozygous deletions of the C-terminus of Chd2 exhibit perinatal lethality."* Heterozygotes show systemic abnormalities but *"no neurological defects were reported."*
- **Chaserr knockout mouse (Ulitsky lab):** elevated Chd2; *"early lethality"* — validating the dosage-window concern for CHD2-raising therapy.
- **Uncoupling study (Mol Psychiatry 2026, DOI:10.1038/s41380-026-03539-x ⚠️)** — "Uncoupling memory impairments from autism-associated behaviors in Chd2 deficient mice," suggesting the cognitive and social phenotypes are mechanistically dissociable.

**The central mouse limitation — and this is important enough to curate as a formal `HUMAN_MODEL_MISMATCH`:** *"No CHD2 mouse model exhibits spontaneous seizures,"* and models *"did not appear to have a 50% CHD2 protein reduction"* (PMID:39391213 ✅). The Ulitsky model showed *"unusual EEG activity, but also did not have clinical seizures."* So the field's best mechanistic model does not reproduce the disease's cardinal clinical feature, while the model that does reproduce it (zebrafish larvae) cannot address the developmental and cognitive core. Any mouse-derived efficacy claim about seizure control must be treated as extrapolation.

### *Xenopus*

Willsey lab work found *"a stronger phenotype seen in morpholinos than in CRISPR editing"* and, notably, that CHD2 *"localizes to microtubules of the mitotic spindle"* — a non-chromatin localization with implications for progenitor division.

### Human iPSC, hESC, and organoid models

The most human-relevant system, and the source of the interneuron mechanism.
- hESC-derived cortical interneuron differentiation identified *CHD2* as an NKX2-1 target and showed *"CHD2 deficiency impaired cIN development and altered later cIN function"* (PNAS 2017, DOI:10.1073/pnas.1712365115 ⚠️; Sci Rep 2022, PMID:36115870 ✅).
- *"CRISPR-Cas9 mediated biallelic knockout of CHD2 resulted in fewer TUBB3+ neurons with shorter neurites."*
- *"Several induced CHD2 pluripotent stem cells (iPSC) in both human and CRISPR cells induced around the world,"* with an NIH grant supporting expansion into **cortical organoids** (PMID:39391213 ✅).
- Patient-derived iPSCs from *CHASERR*-deletion individuals showed increased CHD2 protein, confirming the cis-repression mechanism in human cells (NEJM 2024).

**Limitations:** iPSC/organoid systems model early development, not mature circuits or seizures; **and a specific technical caveat flagged in the roadmap — "CHD2 is lowly expressed in certain cell types,"** producing *"irregular results including CHD2+/– models that do not appear to achieve 50% protein reduction."* Protein quantification is a genuine unsolved methods problem in this field.

**Model databases:** MGI (mouse), ZFIN (zebrafish — Suls et al. is indexed as ZDB-PUB-131218-5), Xenbase, IMSR/IMPC/KOMP, Alliance of Genome Resources, Cellosaurus.

---

## Curator notes for the dismech entry

A few things I'd flag before this gets turned into YAML, since some of them are the kind of thing that quietly breaks validation or, worse, quietly encodes something wrong:

**Verify before citing.** Seven references here have confirmed titles/journals/DOIs but PMIDs I could not resolve in this session: De Maria 2022 (AJMG A), Kim 2018 (Neuron), Meganathan 2017 (PNAS), Rom 2019 (Nat Commun), the CHASERR NEJM paper, Chityala (Epileptic Disorders), and Mavashov (Epilepsia). Run `just fetch-reference` on each and confirm the snippet is an exact substring before use. The verified set — 23708187, 24207121, 25783594, 25672921, 31677157, 40934838, 39601014, 39391213, 36115870, 38496558 — is safe to build the backbone on.

**The riskiest ontology term is the most important one.** Photosensitivity is this disease's signature, and I deliberately did not guess an HPO ID for it. Look it up properly. Same for "eyelid myoclonia," "myoclonic-atonic seizure," and the photoparoxysmal-EEG term — HPO has renamed several seizure-semiology terms recently and stale memory is exactly how a bad `term.label` sneaks past.

**Two frequencies for the same phenotype, and that's correct.** GeneReviews says 80% photosensitivity (20/25, when specifically asked); the pooled analysis says 59% (80/136). These aren't in conflict — they're different ascertainment. Curate both with distinct `population` values rather than picking a winner.

**Don't collapse "photosensitive" and "photoparoxysmal response."** Clinical photosensitivity runs 59–80%; a recorded PPR on EEG has been documented in a handful of patients. Two phenotypes, wildly different frequencies, opposite clinical implications for whether a normal IPS study means anything.

**The CHASERR story wants its own entry.** Too little CHD2 gives you DEE94; too much gives you NEDFSAB (OMIM #621012) — dysmorphic, hypomyelinating, more severe. Same gene, opposite direction, different disease. That's a separate dismech entry plus a grouping, and it also means the existing ClinGen TS=0 dosage call is historically true but biologically stale. Worth a `discussions` note rather than silently inheriting the old score.

**Three honest knowledge gaps worth encoding rather than smoothing over:** (1) no CHD2-specific ASM comparative data exists, so any treatment ranking is borrowed from generalized-epilepsy practice; (2) whether the progressive posterior atrophy is seizure-driven injury or primary neurodegeneration is unresolved; (3) the mouse models don't seize, which is a textbook `HUMAN_MODEL_MISMATCH` — the model that captures the mechanism can't show you the disease, and the model that shows you the disease can't tell you the mechanism.

**Sources:**
- [GeneReviews: CHD2-Related Neurodevelopmental Disorders](https://www.ncbi.nlm.nih.gov/books/NBK333201/)
- [OMIM #615369 DEE94](https://omim.org/entry/615369) · [OMIM *602119 CHD2](https://omim.org/entry/602119) · [OMIM *620993 CHASERR](https://www.omim.org/entry/620993) · [OMIM #621012 NEDFSAB](https://omim.org/entry/621012)
- [Carvill 2013, Nat Genet (PMID:23708187)](https://pubmed.ncbi.nlm.nih.gov/23708187/)
- [Suls 2013, AJHG (PMID:24207121)](https://pubmed.ncbi.nlm.nih.gov/24207121/)
- [Galizia 2015, Brain (PMID:25783594)](https://pubmed.ncbi.nlm.nih.gov/25783594/)
- [Thomas 2015, Neurology (PMID:25672921)](https://www.neurology.org/doi/10.1212/WNL.0000000000001305)
- [Chen 2020, DMCN (PMID:31677157)](https://pubmed.ncbi.nlm.nih.gov/31677157/)
- [Puri 2025, Seizure (PMID:40934838)](https://pubmed.ncbi.nlm.nih.gov/40934838/)
- [Adult Phenotype of CHD2-Associated Disorders (PMID:39601014)](https://pubmed.ncbi.nlm.nih.gov/39601014/)
- [Prince 2024, roadmap to cure CHD2-RD (PMID:39391213)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11465304/)
- [Meganathan 2022, Sci Rep (PMID:36115870)](https://pubmed.ncbi.nlm.nih.gov/36115870/) · [Meganathan 2017, PNAS](https://www.pnas.org/doi/10.1073/pnas.1712365115)
- [Wilson 2018, Front Mol Neurosci — chromatin remodelers in epilepsy](https://www.frontiersin.org/journals/molecular-neuroscience/articles/10.3389/fnmol.2018.00208/full)
- [CHASERR deletion, NEJM 2024](https://www.nejm.org/doi/full/10.1056/NEJMoa2400718) · [preprint PMID:38496558](https://pubmed.ncbi.nlm.nih.gov/38496558/)
- [Rom 2019, Nat Commun — Chaserr regulates Chd2](https://www.nature.com/articles/s41467-019-13075-8)
- [Kim 2018, Neuron — Chd2 and long-term memory](https://www.cell.com/neuron/fulltext/S0896-6273(18)31045-6)
- [Mavashov, Epilepsia 2026](https://onlinelibrary.wiley.com/doi/10.1002/epi.70073) · [bioRxiv preprint](https://www.biorxiv.org/content/10.1101/2025.03.18.643778v1.full)
- [De Maria 2022, Am J Med Genet A](https://onlinelibrary.wiley.com/doi/10.1002/ajmg.a.62548)
- [Chityala, Epileptic Disorders — PME mimic](https://onlinelibrary.wiley.com/doi/10.1002/epd2.70196)
- [ClinGen CHD2 gene curation](https://search.clinicalgenome.org/kb/genes/HGNC:1917) · [ClinGen CHD2 dosage](https://search.clinicalgenome.org/kb/gene-dosage/CHD2)
- [Epilepsiome: CHD2 — what you need to know (2023)](https://epilepsygenetics.blog/the-epilepsiome/chd2-this-is-what-you-need-to-know-2023/)
- [MedlinePlus: CHD2 myoclonic encephalopathy](https://medlineplus.gov/genetics/condition/chd2-myoclonic-encephalopathy/)