---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-01T07:10:37.979392'
end_time: '2026-08-01T07:28:29.091479'
duration_seconds: 1071.11
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Bachmann-Bupp Syndrome
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
  - claude-opus-5[1m]
  web_search_requests: 8
  num_turns: 77
  total_cost_usd: 6.106121000000002
  session_id: dffc7e17-41dd-47c8-a30e-f5363daff7f0
  stop_reason: end_turn
citation_count: 38
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bachmann-Bupp Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Bachmann-Bupp Syndrome** covering all of the
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

# Comprehensive Research Report: Bachmann–Bupp Syndrome (BABS)

**Prepared:** 2026-08-01 · **Target for KB entry:** `kb/disorders/Bachmann-Bupp_Syndrome.yaml` · **Category:** Mendelian (autosomal dominant, de novo gain-of-function)

> **Scope note / NEC preflight.** This report was anchored on the MONDO/OMIM/gene triple before any content was gathered: **MONDO:0033642** ← xref **OMIM:619075** ← causal gene **ODC1 (HGNC:8109, 2p25.1)**. All primary literature cited below names ODC1 as the causal gene, consistent with the MONDO record. There is an eponym-collision risk class here (multiple "Bachmann" eponyms exist in medicine — e.g., Bachmann's bundle in cardiac conduction), so every citation was checked to be about the ODC1 polyaminopathy specifically. No Named Entity Confusion was detected.

---

## 1. Disease Information

### 1.1 Overview

Bachmann–Bupp syndrome (BABS) is an **ultra-rare autosomal dominant neurodevelopmental disorder caused by *de novo* gain-of-function variants in the 3′ end of *ODC1***, the gene encoding ornithine decarboxylase (ODC), the first and rate-limiting enzyme of polyamine biosynthesis. It is one of five recognized **"polyaminopathies."**

The canonical clinical triad is **global developmental delay + hypotonia + a distinctive non-congenital alopecia** (hair present at birth, then shed in large clumps within the first weeks of life), usually with **macrocephaly/macrosomia**, dysmorphic facies, and nonspecific brain MRI abnormalities.

> "Bachmann-Bupp syndrome (BABS) is a neurodevelopmental disorder characterized by developmental delay, hypotonia, and varying forms of non-congenital alopecia. The condition is caused by 3'-end mutations of the ornithine decarboxylase 1 (ODC1) gene, which produce carboxy (C)-terminally truncated variants of ODC, a pyridoxal 5'-phosphate-dependent enzyme. C-terminal truncation of ODC prevents its ubiquitin-independent proteasomal degradation and leads to cellular accumulation of ODC enzyme that remains catalytically active."
> — Bachmann & Bupp, *Dev Med Child Neurol* 2024 (**PMID:37469105**)

BABS is of outsized translational significance because it is **the first polyaminopathy with a viable targeted treatment**: the ODC suicide inhibitor **eflornithine (α-difluoromethylornithine, DFMO)**, repurposed from oncology/trypanosomiasis, moved from disease description (2018) to first patient dosed in **16 months** (**PMID:40167220**).

### 1.2 Key identifiers

| Resource | Identifier |
|---|---|
| **MONDO** | **MONDO:0033642** — "neurodevelopmental disorder with alopecia and brain abnormalities" |
| **OMIM (phenotype)** | **619075** — BACHMANN-BUPP SYNDROME; BABS |
| **OMIM (gene)** | **165640** — ORNITHINE DECARBOXYLASE 1; ODC1 |
| **Orphanet** | **ORPHA:544488** |
| **MedGen** | **C5436741** / UID 1775930 |
| **UMLS** | C5436741 |
| **GARD** | 0017987 |
| **SNOMED CT** | 1222658006 |
| **ICD-10** | **E72.4** (disorders of ornithine metabolism) — via Orphanet mapping |
| **ICD-11** | Not established in retrieved sources; likely maps under 5C50.Cx (disorders of ornithine metabolism) — *verify before asserting* |
| **MeSH** | No dedicated MeSH descriptor found; indexed via *Ornithine Decarboxylase* (D009952) + *Alopecia* + *Neurodevelopmental Disorders* |
| **Gene** | ODC1 — **HGNC:8109**, NCBI Gene **4953**, Ensembl ENSG00000115758, UniProt **P11926** |

### 1.3 Synonyms

- **Bachmann–Bupp syndrome (BABS)** — the eponymic/clinical name in wide use
- **Neurodevelopmental disorder with alopecia and brain abnormalities (NEDABA)** — the MONDO/OMIM/MedGen preferred label
- ***ODC1*-related neurodevelopmental disorder** — GeneReviews dyadic name
- **Global developmental delay–alopecia–macrocephaly–facial dysmorphism–structural brain anomalies syndrome** — Orphanet label
- Gene aliases in NCBI: ODC, **BABS**, **NEDBA**, **NEDBIA**

### 1.4 Provenance of information

Essentially **all knowledge is derived from individual patient reports and small case series**, not from EHR-scale or registry-scale aggregation. The aggregating structures are:
- **GeneReviews** chapter (Bupp, VanSickle, Bachmann; **PMID:36007106**, NBK583220)
- The **International Center for Polyamine Disorders (ICPD)** — a Corewell Health / Michigan State University collaboration with the Snyder-Robinson Foundation, which performs "comprehensive data generation and local as well as remote sample collection from patients with known or suspected polyamine disorders around the world" (**PMID:37092498**)
- A 2026 systematic narrative review of all five polyaminopathies (**PMID:41410504**)

There is **no EHR-derived cohort, no ICEES/COHD comorbidity signal, and no population registry** for BABS.

---

## 2. Etiology

### 2.1 Primary cause

**Heterozygous, almost always *de novo*, gain-of-function variants clustered in the 3′ end of *ODC1*** — specifically in **exon 12** or the **intron 11 splice sites immediately preceding it** — that remove or disrupt the C-terminal ~37-residue degradation domain (amino acids ~425–461) of the 461-aa ODC protein.

Because these variants fall in the **last exon**, the transcripts **escape nonsense-mediated decay**; a truncated but **catalytically fully active** ODC protein is produced that can no longer be degraded by the antizyme/26S-proteasome route. The result is **massive cellular accumulation of active ODC** and **putrescine overproduction**.

> "We hypothesized that this new mutation (c.1342 A>T) leads to a C-terminal truncation variant of the ODC protein that is resistant to normal proteasomal degradation, leading to putrescine accumulation in cells."
> — Schultz et al., *Biochem J* 2019 (**PMID:31249027**)

This is a **true molecular gain of function** (protein stabilization → enzyme over-accumulation), **not** haploinsufficiency. Critically, *ODC1* **loss-of-function** produces a **mechanistically opposite and phenotypically distinct** picture (see §4.4).

### 2.2 Genetic risk factors

- **Causal variants:** see §4.2. All reported pathogenic variants are 3′-end truncating/splice variants.
- **Susceptibility loci / modifier genes:** **None identified.** No GWAS, no reported modifiers.
- **Parental age:** Not studied. A paternal-age effect is plausible for a *de novo* dominant condition but **has not been demonstrated** for BABS.
- **Family history:** Essentially absent — all molecularly tested probands to date have *de novo* variants.

### 2.3 Environmental risk factors

**None known.** BABS is a monogenic Mendelian disorder with no established environmental contribution to occurrence. Polyhydramnios (58–80% of pregnancies) is a **consequence**, not a cause.

One *theoretical, unproven* environmental modifier exists on the **downstream** side: dietary and gut-microbial polyamines contribute meaningfully to the body polyamine pool, and Rodan et al. explicitly proposed them as therapeutic levers:

> "Therapies aimed at reducing putrescine levels, including ODC1 inhibitors, dietary interventions, and antibiotics to reduce polyamine production by gastrointestinal flora could be considered as disease-modifying therapies."
> — Rodan et al., *Am J Med Genet A* 2018 (**PMID:30475435**)

This makes **dietary polyamine load and gut flora composition** biologically plausible severity modifiers, but **no human data support this in BABS**.

### 2.4 Protective factors

- **Genetic protective factors:** none identified.
- **Environmental protective factors:** none validated. Polyamine-restricted diets are listed by GeneReviews under "therapies under investigation," not as established protection.

### 2.5 Gene–environment interactions

No documented GxE interaction. The single actionable "interaction" is **pharmacological**: the disease phenotype is at least partly reversible by pharmacologic ODC inhibition (eflornithine), demonstrating that the phenotype depends on **ongoing** polyamine flux rather than solely on fixed developmental damage — a point strongly supported by both the human treatment response (**PMID:34282722**) and the K6/ODC mouse (**PMID:8618048**, see §15).

---

## 3. Phenotypes

### 3.1 Frequency table — GeneReviews cohort (n=9 published individuals; primary source)

| Feature | Frequency | Suggested HPO term |
|---|---|---|
| Alopecia (non-congenital, clumped shedding) | **9/9 (100%)** | HP:0001596 Alopecia; HP:0002293 Alopecia of scalp |
| Dysmorphic features | **9/9 (100%)** | HP:0001999 Abnormal facial shape |
| Developmental delay | **8/8 (100%)** | HP:0001263 Global developmental delay |
| Hypotonia | **8/8 (100%)** | HP:0001290 Generalized hypotonia |
| Macrocephaly | **6/9 (66%)** | HP:0000256 Macrocephaly |
| Polyhydramnios (pregnancy history) | **5/9 (55.5%)** | HP:0001561 Polyhydramnios |
| Skin findings (keratosis pilaris / follicular cysts) | **4/8 (50%)** | HP:0032152 Keratosis pilaris; HP:0025249 Follicular cyst *(verify)* |
| Macrosomia in infancy | **2/5 (40%)** | HP:0001520 Large for gestational age |
| Constipation | **3/8 (37.5%)** | HP:0002019 Constipation |
| Seizures | **1/8 (12.5%)** | HP:0001250 Seizure |

*Source: GeneReviews Table 2 (**PMID:36007106**, NBK583220).*

### 3.2 Frequency table — 2026 systematic review (n=12 published BABS cases)

| Feature | Reported | HPO |
|---|---|---|
| Hair abnormalities / alopecia | **12/12 (100%)** | HP:0001596 |
| Brain MRI abnormalities | **12/12 (100%)** | HP:0012443 Abnormal brain morphology |
| Hypotonia | 11/12 | HP:0001290 |
| Global developmental delay | 11/12 | HP:0001263 |
| Dysmorphic features | 10/12 (83.3%) | HP:0001999 |
| Macrocephaly | **9/12 (75%)** | HP:0000256 |
| Prenatal polyhydramnios | 7/12 (58.3%) | HP:0001561 |
| Skin abnormalities (incl. follicular cysts) | 6/12 (50%) | HP:0011368 Abnormal epidermis morphology |
| Behavioral (ADHD/ASD) | 4/12 (33.3%) | HP:0007018 / HP:0000717 |
| Epilepsy | **1/12 (8.3%)** | HP:0001250 |

*Source: VanSickle et al., *Am J Med Genet A* 2026 (**PMID:41410504**, PMC13270430, DOI 10.1002/ajmga.70029).*

> ⚠️ **Verification flag:** the extracted percentages in this table were internally inconsistent for GDD (listed as "11/12 | 83.3%", where 11/12 = 91.7%). **Re-verify the exact n/N against the published Table before committing frequencies from this source to the KB.** The GeneReviews table (§3.1) is the safer primary frequency source.

### 3.3 HPO disease-annotation set (HPOA, OMIM:619075) — with explicit n/N and onset

| HPO ID | Term | Frequency | Onset |
|---|---|---|---|
| HP:0002223 | Absent eyebrow | **5/5** | — |
| HP:0000653 | Sparse eyelashes | 4/4 | — |
| HP:0001263 | Global developmental delay | 4/4 | — |
| HP:0000316 | Hypertelorism | 4/4 | — |
| HP:0000348 | High forehead | 4/4 | — |
| HP:0001561 | Polyhydramnios | 4/5 | Prenatal |
| HP:0000750 | Delayed speech and language development | 3/3 | — |
| HP:0031936 | Delayed ability to walk | 3/3 | — |
| HP:0001290 | Generalized hypotonia | 3/3 | — |
| HP:0012520 | Dilation of Virchow-Robin spaces | 3/4 | — |
| HP:0007018 | Attention deficit hyperactivity disorder | 2/3 | — |
| HP:0000028 | Cryptorchidism | 2/3 | — |
| HP:0001558 | Decreased fetal movement | 2/5 | Prenatal |
| HP:0001792 | Small nail | 2/4 | — |
| HP:0000508 | Ptosis | 2/4 | — |
| HP:0000490 | Deeply set eye | 2/4 | — |
| HP:0002209 | Sparse scalp hair | 1/4 | — |
| HP:0000256 | Macrocephaly | 1/1 | — |
| HP:0004488 | Macrocephaly at birth | 1/4 | Prenatal |
| HP:0001520 | Large for gestational age | 1/4 | Birth |
| HP:0001319 | Neonatal hypotonia | 1/1 | Neonatal |
| HP:0002061 | Lower limb spasticity | 1/1 | — |
| HP:0008872 | Feeding difficulties in infancy | 1/1 | Neonatal |
| HP:0000407 | Sensorineural hearing impairment | 1/1 | — |
| HP:0000378 | Cupped ear | 1/1 | — |
| HP:0000218 | High palate | 1/1 | — |
| HP:0002904 | Hyperbilirubinemia | 1/1 | Neonatal |
| HP:0001943 | Hypoglycemia | 1/1 | Neonatal |
| HP:0007109 | Periventricular cysts | 1/1; 1/4 | Neonatal; — |
| HP:0002195 | Dysgenesis of the cerebellar vermis | 1/4 | — |
| HP:0032471 | Focal polymicrogyria | 1/4 | — |
| HP:0002514 | Cerebral calcification | 1/4 | — |
| HP:0032152 | Keratosis pilaris | 1/4 | — |
| HP:0000958 | Dry skin | 1/4 | — |
| HP:0004209 | Clinodactyly of the 5th finger | 1/4 | — |
| HP:0000581 | Blepharophimosis | 1/4 | — |
| HP:0000494 | Downslanted palpebral fissures | 1/4 | — |
| HP:0000219 | Thin upper lip vermilion | 1/4 | — |
| HP:0000718 | Aggressive behavior | 1/3 | — |

*Source: HPO annotation network, ontology.jax.org (OMIM:619075).*

Orphanet-sourced HPOA bands (via Monarch, MONDO:0033642) additionally list as **Frequent (HP:0040282)**: HP:0000400 Macrotia, HP:0001488 Bilateral ptosis, HP:0030890 Hyperintensity of cerebral white matter on MRI; and as **Occasional (HP:0040283)**: HP:0000023 Inguinal hernia, HP:0000278 Retrognathia, HP:0001257 Spasticity, HP:0002465 Poor speech.

### 3.4 Per-phenotype characterization

**Alopecia (the pathognomonic sign) — HP:0001596 / HP:0002293**
- *Type:* physical/ectodermal manifestation
- *Onset:* **non-congenital, first weeks of life.** GeneReviews: hair "is sometimes sparse and sometimes has atypical color" at birth, then lost "in large clumps" within weeks. Eyebrows and eyelashes are typically congenitally absent/sparse (HP:0002223, HP:0000653).
- *Severity/progression:* variable; often near-total scalp alopecia. **Reversible on eflornithine.**
- *Frequency:* 100%
- *QoL impact:* cosmetic and psychosocial; hair regrowth is consistently reported by families as one of the most visible and valued treatment effects.

**Global developmental delay / intellectual disability — HP:0001263, HP:0001249**
- *Onset:* infancy
- *Severity:* "moderate to severe range" (GeneReviews). Independent walking achieved between **17 months and 4 years**; **three reported individuals remained nonverbal** at last report. A 12-year-old (Patient 10) had "moderate developmental delay and intellectual disability, with the ability to read and write" (**PMID:37092498**) — demonstrating real variable expressivity.
- *Progression:* static/non-degenerative; improvement documented with treatment.
- *QoL impact:* the dominant driver of lifelong disability, caregiver burden, and educational need.

**Hypotonia — HP:0001290 / HP:0001319**
- *Onset:* neonatal/infantile; *Frequency:* ~92–100%; *Progression:* generally static, improves with therapy and with DFMO.
- One patient developed **proximal myopathy confirmed on EMG** with progressive weakness and wheelchair use for distance (**PMID:37092498**) — HP:0003701 Proximal muscle weakness.

**Macrocephaly / overgrowth — HP:0000256, HP:0001520**
- *Onset:* prenatal to infantile; the index patient had macrosomia and macrocephaly (**PMID:30239107**); Patient 10 had OFC >99th centile (38 cm) at birth.
- *Frequency:* 66–75%. Absolute **or relative** macrocephaly (Rodan et al.).
- Overgrowth may give way to obesity risk in later childhood (GeneReviews lists caloric management).

**Brain MRI abnormalities — HP:0012443**
- *Frequency:* abnormal in essentially all imaged patients, but **without a consistent pattern**.
> "Every patient had a brain MRI performed at some time point, and neuroimaging abnormalities are common, but not with a particular pattern or recurrence of findings." — VanSickle et al. 2021 (**PMID:34477286**)
- Reported findings: white matter signal abnormality (HP:0002500 / HP:0030890), **prominent Virchow-Robin/perivascular spaces (HP:0012520)**, periventricular and germinal-matrix cysts (HP:0007109), porencephalic cysts (HP:0002132), corpus callosum abnormalities incl. hypoplasia of the mid-body (HP:0002079), ventriculomegaly (HP:0002119), cerebellar vermis dysgenesis (HP:0002195), focal polymicrogyria (HP:0032471), cerebral calcification (HP:0002514), hypoplastic optic chiasm, hippocampal volume loss.

**Seizures/epilepsy — HP:0001250**
- *Rare* (1/12, 8.3%) but can be **severe and late-onset**. The oldest reported patient (male, 23 y) developed **absence seizures at age 14**, evolving to "multiple seizure types but atypical absence, atonic, and generalized tonic–clonic," **refractory to ketogenic diet** and multiple ASMs (**PMID:34477286**). This was the first epilepsy report in BABS.
- Contrast: epilepsy is far more prominent in Snyder-Robinson syndrome (~63%), which is a useful discriminator (**PMID:41410504**).

**Behavioral phenotypes**
- ADHD (HP:0007018, 2/3 in HPOA), autism spectrum disorder (HP:0000717), aggression (HP:0000718). Aggregate ADHD/ASD ~33%.

**Dermatologic (beyond alopecia)**
- **Follicular cysts** (~50% with skin findings), keratosis pilaris (HP:0032152), dry skin (HP:0000958), hypoplastic/small nails (HP:0001792). Follicular cysts directly phenocopy the K6/ODC mouse.
> "In both patients, treatment with difluoromethylornithine has resulted in improved dermatologic signs, including regrowth of eyebrow and scalp hair and cessation of recurrent follicular cyst development." — Afrin et al., *Pediatr Dermatol* 2023 (**PMID:36443247**)

**Feeding / GI**
- Feeding difficulties in infancy (HP:0008872), aspiration (HP:0002835), constipation (HP:0002019, 37.5%). NG/G-tube may be required.

**Sensory**
- Sensorineural hearing loss (HP:0000407) — present in index patient; refractive error and strabismus (HP:0000486) warrant annual ophthalmology.

**Prenatal**
- Polyhydramnios (HP:0001561) 55–80%, decreased fetal movement (HP:0001558), prenatal ventriculomegaly/cerebral cysts, and — in one 2026 report — **macrocephaly plus ventricular septal defect (HP:0001629)** detected on second-trimester ultrasound (**PMID:41931584**).

**Genitourinary/skeletal**
- Cryptorchidism (HP:0000028, 2/3), inguinal hernia (HP:0000023), fifth-finger clinodactyly (HP:0004209), joint hypermobility (HP:0001382).

### 3.5 Quality of life

**No BABS-specific QoL instrument data (EQ-5D, PROMIS, SF-36, PedsQL) exist in the literature.** QoL statements are qualitative and family-reported. Reported functionally meaningful post-treatment gains in the index patient — self-feeding with a spoon, sitting unsupported, walker use — are the closest available surrogates for QoL benefit (**PMID:34282722**, **PMID:37469105**). *This is a genuine evidence gap.*

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene

| Attribute | Value |
|---|---|
| Symbol / name | **ODC1** / ornithine decarboxylase 1 |
| HGNC | **hgnc:8109** |
| NCBI Gene | 4953 |
| OMIM gene | 165640 |
| Locus | **2p25.1** |
| Genomic span (GRCh38.p14) | chr2:10,439,968–10,448,327 (minus strand) |
| Exons | **13** |
| Canonical transcript / protein | **NM_002539.3 / NP_002530.1** (461 aa) |
| Other RefSeqs | NM_001287188.2, NM_001287189.2, NM_001287190.2 |
| UniProt | **P11926** |
| EC | **4.1.1.17** |
| Cofactor | **pyridoxal 5′-phosphate** (CHEBI:18405); binding at residues 200, 237, 274–277, 389 |
| Quaternary structure | **Homodimer**; both monomers contribute residues to each of two active sites |
| Expression | Broad; highest in testis (RPKM 67.6) and bone marrow (54.4); strongly elevated in proliferating fetal brain ventricular zone |

### 4.2 Pathogenic variants (compiled from all sources)

All are **heterozygous, *de novo*, germline**, and all cluster in **exon 12 / intron 11** of NM_002539.3 — the 3′ region encoding the C-terminal degron.

| # | cDNA (NM_002539.3) | Protein (NP_002530.1) | Type | ClinVar | Source |
|---|---|---|---|---|---|
| 1 | **c.1342A>T** | **p.(Lys448Ter)** | nonsense | VCV000983289, Pathogenic | Bupp 2018 index case (**PMID:30239107**) |
| 2 | **c.1241+1G>T** (IVS11+1G>T) | splice donor loss | splice | VCV000983285, Pathogenic | Rodan 2018 (**PMID:30475435**) |
| 3 | **c.1240_1241dupTG** | **p.(Trp414Cysfs\*17)** | frameshift | VCV000983286, Pathogenic | Rodan 2018 |
| 4 | **c.1255C>T** | **p.(Gln419Ter)** | nonsense | VCV000983287, Pathogenic | Rodan 2018 |
| 5 | **c.1242_1263del22** (NC_000002.12:g.10440850_10440871del) | p.(Trp414Ter) *as reported* | deletion | VCV000983288, Pathogenic | Rodan 2018 |
| 6 | **c.1242-2A>G** (IVS11-2A>G) | splice acceptor loss | splice | VCV001074405, Pathogenic (multiple submitters, no conflicts) | **Recurrent — ≥3 individuals**; VanSickle 2021 (**PMID:34477286**), Michael 2023 (**PMID:37092498**) |
| 7 | **c.1313_1316delCTGT** | p.(438Rfs\*9) *as reported* | frameshift | — | VanSickle 2021 Patient 7 |
| 8 | **c.1252C>T** | **p.(Gln418Ter)** | nonsense | — | VanSickle 2021 Patient 9 |
| 9 | **c.1307_1311delinsT** | **p.(Thr436Ilefs\*11)** | indel/frameshift | — | Michael 2023 Patient 11 |
| — | c.1217A>T | p.(Tyr406Phe) | missense | **VUS** | Bupp 2025 (**PMID:40167220**) — *functionally excluded*, see below |

> ⚠️ **Nomenclature verification flags for the curator:**
> 1. One secondary source rendered the index variant as "c.1342A>G (p.Lys448\*)". The **primary paper and ClinVar both say c.1342A>T** — use **c.1342A>T**.
> 2. Variants #5 and #7 have protein annotations that are inconsistent with their cDNA positions as extracted (`c.1242_1263del22 → p.Trp414*` and `c.1313_1316del → p.438Rfs*9`). Re-derive or re-verify from the source tables before committing HGVS protein strings.
> 3. `c.1242-2A>G` is the single **recurrent** variant and is the most likely candidate for a "hotspot" claim.

**The instructive negative — functional testing overrides sequence intuition.** Bupp et al. 2025 report a patient with the missense VUS **c.1217A>T (p.Tyr406Phe)** and an atypical presentation whose **ODC enzyme activity was "not greater than unaffected control patients' samples,"** arguing against pathogenicity. This establishes that **the biochemical assay, not the variant location alone, adjudicates BABS** (**PMID:40167220**).

### 4.3 Variant classification, allele frequency, origin

- **ACMG/AMP classification:** BABS variants are classified Pathogenic. Note that **PVS1 (null variant) is NOT the operative criterion** here — the mechanism is gain-of-function via stabilization, so PS3 (functional evidence: elevated ODC protein/activity/putrescine), PS2 (*de novo* with confirmed parentage), PM1 (mutational hotspot in the C-terminal degron), and PP4 (highly specific phenotype) carry the weight. **Applying PVS1 to an *ODC1* 3′-truncating variant would be a mechanistic error.**
- **Allele frequency:** All reported BABS variants are **absent from gnomAD/1000 Genomes/TOPMed** (private *de novo* events). **gnomAD constraint metrics (pLI, LOEUF, missense Z) for ODC1 could not be retrieved programmatically for this report and should be looked up directly before being asserted.** Note that constraint metrics are of *limited interpretive value* here, since the disease mechanism is last-exon NMD-escaping GoF rather than haploinsufficiency.
- **Germline vs somatic:** BABS variants are **germline** (*de novo*). Separately, **somatic** *ODC1* alterations occur in sporadic tumors (colorectal, gastric, skin, breast, prostate, neuroblastoma) and are **not** heritable and **not** BABS (GeneReviews).
- **Functional consequence:** **Gain of function via loss of degradation.** The truncated enzyme retains full catalytic activity; steady-state protein level rises dramatically.

### 4.4 Allelic disorders — the loss-of-function arm

*ODC1* **loss-of-function** is mechanistically opposite and phenotypically distinct. Prokop et al. characterized **p.Gly84Arg (NC_000002.12:g.10444500C>T, rs138359527, NP_002530.1:p.Gly84Arg)**:

> "A functional enzyme assay…showed a 2.5-fold reduction of enzyme activity because of the variant."
> "The variant was found at the highest allele frequency within South Asian individuals (0.8%, specifically Gujarati Indians in Houston, TX (1.5%) and Punjabi in Lahore, Pakistan (1%)."
> — Prokop et al., *Genes* 2021 (**PMID:33806076**)

Overall gnomAD frequency 0.23%; TOPMed 0.18%; ~3-fold enrichment in Geno2MP, associated with intellectual disability and seizures. The authors propose a **bidirectional model**:

> "…suggesting gain-of-function variants with neural over-proliferation and loss-of-function variants with neural depletion."

This is an important framing for the KB: *ODC1* dosage is bidirectionally constrained in brain development.

### 4.5 Modifier genes

**None validated.** Mechanistically plausible but untested candidates within the pathway: **OAZ1/OAZ2/OAZ3** (antizymes — the very machinery the truncation escapes), **AZIN1** (antizyme inhibitor), **AMD1**, **SRM**, **SMS**, **SAT1** (catabolic acetylation/export), and the polyamine transport system.

### 4.6 Epigenetics

- **No BABS-specific DNA methylation episignature** has been published. (A DNA-methylation episignature screen would be a natural, tractable study.)
- Indirect but relevant: polyamines are decarboxylated-SAM donors and chromatin-associated polycations; the K6/ODC mouse literature shows elevated polyamines "**alter chromatin remodeling and cell signaling leading to metabolic reprogramming**" (**PMID:41925768**).
- **Regulatory (eQTL) variation at *ODC1* is extensive:** Prokop et al. identified **900 variants associated with *ODC1* expression across 1,414,872 bases** around the locus, including rs2302615 (muscle, p=9.4×10⁻⁷) and rs77575195 (tibial nerve, p=8.3×10⁻⁹), "suggesting a high selection on ODC1 expression levels throughout human evolution" (**PMID:33806076**).

### 4.7 Chromosomal abnormalities

**None reported.** BABS is not caused by CNVs, translocations, or aneuploidy. GeneReviews explicitly states gene-targeted deletion/duplication analysis is **"not required"** given the gain-of-function mechanism — an intragenic deletion would not produce BABS.

---

## 5. Environmental Information

- **Environmental factors:** **Not applicable.** No toxin, radiation, pollutant, or occupational exposure is implicated in BABS causation.
- **Lifestyle factors:** Not applicable to causation. Post-diagnosis, **caloric management** matters for the overgrowth/obesity trajectory, and **dietary polyamine restriction** is an investigational (unproven) adjunct.
- **Infectious agents:** **Not applicable.** No infectious trigger. (Note the ironic pharmacological link in the other direction: eflornithine's original indication is *Trypanosoma brucei gambiense* African sleeping sickness, where trypanosomal ODC's stability — it lacks the antizyme system, **PMID:7730330** — is the drug's selectivity basis.)

---

## 6. Mechanism / Pathophysiology

### 6.1 The causal chain (upstream → downstream)

```
[MOLECULAR — trigger]
de novo heterozygous 3'-end ODC1 variant (exon 12 / intron 11 splice site)
        ↓  (last-exon location → escapes nonsense-mediated decay)
[MOLECULAR]
Production of C-terminally truncated ODC protein lacking the 37-residue
degradation domain (aa ~425–461), but retaining full catalytic activity
        ↓
[MOLECULAR]
Loss of antizyme-stimulated, ubiquitin-INDEPENDENT 26S proteasomal
degradation of ODC  (GO:0010499)
        ↓
[MOLECULAR]
Cellular accumulation of enzymatically active ODC protein
(12–17× normal activity in dermal fibroblasts; 125–137× in RBCs)
        ↓
[MOLECULAR / metabolic]
Excess flux: L-ornithine → putrescine  (GO:0009446 putrescine biosynthetic process;
GO:0004586 ornithine decarboxylase activity)
→ putrescine accumulation; compensatory SAT1 acetylation and cellular export
→ elevated plasma N-acetylputrescine and acisoga
        ↓
[CELLULAR]
Polyamine-driven dysregulation of cell proliferation and differentiation
   ├── neural progenitor over-proliferation / disturbed neurodevelopment
   └── hair follicle outer root sheath keratinocyte dysfunction
        ↓
[TISSUE]
   ├── Abnormal cortical/white-matter architecture, perivascular space dilation,
   │   periventricular cysts, callosal dysgenesis
   ├── Hair follicle failure → anagen disruption → clumped hair shedding;
   │   follicular cyst formation
   └── Somatic overgrowth / macrocephaly
        ↓
[ORGANISM]
Global developmental delay, ID, hypotonia, alopecia, dysmorphism,
± epilepsy, ± behavioral phenotypes
```

**Therapeutic interruption point:** eflornithine irreversibly inhibits the accumulated ODC enzyme at the *first* metabolic node, collapsing putrescine production and normalizing downstream metabolites — with demonstrable reversal of hair, tone, developmental, and even white-matter MRI phenotypes.

### 6.2 Molecular pathway detail

**Polyamine biosynthesis (KEGG hsa00330 arginine & proline metabolism; Reactome "Metabolism of polyamines" R-HSA-351202):**

```
L-arginine → L-ornithine (ARG1/ARG2; also LACC1 from L-citrulline)
L-ornithine --[ODC1, PLP-dependent, EC 4.1.1.17]--> putrescine + CO2   ← RATE-LIMITING; the BABS lesion
putrescine + dcSAM --[SRM]--> spermidine
spermidine + dcSAM --[SMS]--> spermine
(catabolic arm: SAT1 acetylation → PAOX/SMOX back-conversion or export)
(spermidine → hypusination of eIF5A via DHPS + DOHH)
```

**The degradation circuit that BABS breaks** (this is the mechanistic heart of the disease and is supported by classic, well-quotable primary literature):

> "Ornithine decarboxylase (ODC) was converted from a protein with a short intracellular half-life in mammalian cells to a stable protein by truncating 37 residues at its carboxyl terminus. Cells expressing wild-type protein lost ODC activity with a half-life of approximately 1 hour. Cells expressing the truncated protein, however, retained full activity for at least 4 hours…Thus, a carboxyl-terminal domain is responsible for the rapid intracellular degradation of murine ODC."
> — Ghoda et al., *Science* 1989 (**PMID:2928784**)

> "…purified 26S proteasome complex, but not the 20S proteasome, catalyses ODC degradation in the absence of ubiquitin. These results strongly suggest that the 26S proteasome, widely viewed as specific for ubiquitin-conjugated proteins, is the main enzyme responsible for ODC degradation."
> — Murakami et al., *Nature* 1992 (**PMID:1334232**)

And the mapping onto BABS:

> "Antizyme binds to transient ODC monomer, which results in the exposure of the ODC carboxy (C)-terminal tail that is subsequently recognized by the 26S proteasome for degradation…the final 37 amino-acid residues of the ODC carboxy (C)-terminal tail constitute an ODC destabilization domain that is required for antizyme-stimulated ODC degradation…If absent/deleted, enzymatically active ODC protein is not properly degraded and consequently accumulates in cells."
> — Bachmann & Bupp 2024 (**PMID:37469105**)

**Note the elegance for KB modeling:** the 1989 Ghoda experiment is, in effect, an *in vitro* pre-enactment of the human BABS allele — the same 37-residue truncation, three decades earlier.

### 6.3 Cellular processes

| Process | GO term | Direction | Evidence |
|---|---|---|---|
| Ornithine decarboxylase activity | **GO:0004586** | INCREASED | PMID:31249027 |
| Putrescine biosynthetic process | **GO:0009446** | INCREASED | PMID:30239107, 31249027 |
| Polyamine biosynthetic process | GO:0006596 *(verify label)* | INCREASED | PMID:37469105 |
| Proteasomal ubiquitin-independent protein catabolic process | **GO:0010499** | DECREASED | PMID:1334232, 2928784 |
| Positive regulation of cell population proliferation | GO:0008284 | INCREASED | PMID:33806076 |
| Nervous system development / neurogenesis | GO:0007399 / GO:0022008 | ABNORMAL | PMID:33806076 |
| Hair follicle development / hair cycle | GO:0001942 / GO:0042633 | ABNORMAL | PMID:8618048, 7671221 |
| Protein stabilization | GO:0050821 | INCREASED (pathological) | PMID:2928784 |

### 6.4 Protein dysfunction

The wild-type ODC monomer is 461 aa; the functional enzyme is an obligate **homodimer** with two shared active sites (UniProt P11926). BABS variants truncate at residues ~406–448, i.e., **after the catalytic core but within the C-terminal degron**, which is exactly why the protein is simultaneously **stable and active** — the worst combination. Prokop et al. note the C-terminus is under strong evolutionary conservation, including a predicted S-farnesylation site at C454, "the most conserved site of all C-terminal amino acids" (**PMID:33806076**).

This is neither misfolding nor aggregation nor loss of catalysis — it is **loss of a degradation signal**, a comparatively uncommon disease mechanism worth flagging as such in the KB.

### 6.5 Metabolic changes

Measured in patients:
- **RBC ODC enzyme activity: 125–137× control**
- **Primary dermal fibroblast ODC activity: 12–17× control**
- **Putrescine (CHEBI:17148): markedly elevated** in fibroblasts and RBCs
- **Plasma N-acetylputrescine: >97.5th percentile** (Z-score vs 866-child reference cohort)
- **Acisoga [N-(3-acetamidopropyl)pyrrolidin-2-one]: >97.5th percentile**
- **Ornithine (CHEBI:15729) and N-acetylarginine: BELOW the 2.5th percentile** at therapy start — consistent with substrate drawdown by the hyperactive enzyme; both **normalized on eflornithine** (**PMID:34282722**)
- **Spermidine (CHEBI:16610) and spermine (CHEBI:15746): "otherwise normal polyamine levels"** in plasma clinical metabolomics (**PMID:30475435**) — an important specificity point: **the biochemical signature is putrescine/N-acetylputrescine-selective, not a global polyamine elevation.**

> "Plasma clinical metabolomics analysis demonstrates elevation of N-acetylputrescine, the acetylated form of putrescine, with otherwise normal polyamine levels." — Rodan et al. 2018 (**PMID:30475435**)

> "…we detected exceptionally high ODC enzyme activity in both primary dermal fibroblasts (12-17-fold of controls) and red blood cells (RBCs) (125-137-fold of controls), using a specific 14C radioactive ODC activity assay." — Schultz et al. 2019 (**PMID:31249027**)

### 6.6 Immune system involvement

**Not a primary feature of BABS.** No immunodeficiency or autoimmunity reported. However, ODC1/polyamine metabolism is deeply embedded in myeloid immunometabolism — LACC1 converts L-citrulline to L-ornithine and "serv[es] as a bridge between proinflammatory nitric oxide synthase (NOS2) and polyamine immunometabolism," with LACC1 phenotypes requiring downstream ODC1 (**PMID:35978195**); and AhR-driven Odc1 transcription suppresses macrophage pyroptosis via spermine-mediated NLRP3 inhibition (**PMID:39113799**). These make **immune phenotyping of BABS patients a reasonable unexplored question**, but there is currently **no evidence of clinical immune dysfunction** — do not assert one.

### 6.7 Tissue damage mechanisms

BABS is a **developmental/dysregulation** disorder rather than a degeneration/necrosis disorder. There is no evidence for oxidative stress, ischemia, fibrosis, or necrosis as primary mechanisms. The tissue-level abnormalities are **maldevelopmental** (cortical architecture, white matter myelination, follicular structure) and — critically — **at least partly reversible**, which argues against fixed structural destruction:

> "Repeat MRI…demonstrated normalization of the cerebral white matter signal with decrease in volume…resolution of all previously noted cysts." — Rajasekaran et al. 2021 (**PMID:34282722**)

### 6.8 Molecular profiling

- **Transcriptomics:** Prokop et al. mined fetal-brain RNA-seq and cerebral organoid data; *ODC1* expression is "markedly elevat[ed] correlating to early development, while neurons/glia progenitors are still proliferating and maturing," and elevated in ventricular zones and in **SOX-marker-positive pluripotent/immature cells** (**PMID:33806076**). No BABS *patient* transcriptome has been published.
- **Proteomics:** No BABS proteomic dataset. Patient-level protein data are targeted Western blots of ODC (**PMID:30239107**, **PMID:31249027**).
- **Metabolomics:** The best-developed omic layer. Untargeted UPLC-MS clinical metabolomics with Z-scores against an **866-child reference cohort** is the established diagnostic/monitoring modality (**PMID:34282722**). Dansyl-chloride derivatization HPLC is the improved reference method for polyamine quantitation (**PMID:40382146**); the RP-HPLC + ¹⁴C-ornithine ODC activity protocol is published in detail (**PMID:40382142**).
- **Lipidomics:** none.
- **Single-cell / spatial:** none in BABS patients. Cerebral organoid single-cell data inform the neural-progenitor hypothesis (**PMID:33806076**).
- **Functional genomics screens:** No BABS-specific CRISPR/RNAi screen. Extensive ODC1 dependency data exist in DepMap for cancer contexts (not disease-relevant here).

### 6.9 Cell types and anatomical processes — suggested ontology bindings

| Entity | Term | Note |
|---|---|---|
| Outer root sheath cell | **CL:0002561** | The K6/ODC transgene's target cell; direct mouse-human correspondence |
| Keratinocyte | CL:0000312 | |
| Neural progenitor cell | **CL:0011020** | *verify canonical label casing* |
| Radial glial cell | CL:0000681 | Ventricular zone |
| Fibroblast (skin) | CL:0002620 | The accessible patient biopsy cell for ODC assay |
| Erythrocyte | CL:0000232 | The accessible patient blood cell for ODC activity/putrescine |
| Hair follicle | **UBERON:0002073** | |
| Hair follicle bulge | UBERON:0005975 | Stem cell niche implicated in K6/ODC |
| Cerebral white matter | UBERON:0002316 | |
| Corpus callosum | UBERON:0002336 | |
| Lateral ventricle | UBERON:0002285 | |
| Cerebellar vermis | UBERON:0004720 | |

---

## 7. Anatomical Structures Affected

### 7.1 Organ level

**Primary:**
- **Central nervous system** (UBERON:0001017) — the dominant burden: cerebral cortex (UBERON:0000956), cerebral white matter (UBERON:0002316), corpus callosum (UBERON:0002336), periventricular/germinal matrix regions, lateral ventricles (UBERON:0002285), cerebellar vermis (UBERON:0004720), hippocampus (UBERON:0002421), optic chiasm (UBERON:0000959)
- **Skin and appendages** (UBERON:0002097) — hair follicle (UBERON:0002073), scalp (UBERON:0000403), eyebrow (UBERON:0001710), eyelash (UBERON:0001711), nail (UBERON:0001705)

**Secondary / systemic:**
- **Musculoskeletal** — generalized hypotonia; one case with proximal myopathy and heel/ankle contractures
- **Craniofacial skeleton** — macrocephaly, high forehead, high palate, retrognathia, cupped/large ears
- **Gastrointestinal** — feeding difficulty, aspiration, constipation
- **Special senses** — cochlea/inner ear (sensorineural hearing loss), eye (ptosis, blepharophimosis, refractive error, strabismus)
- **Genitourinary** — cryptorchidism (testis, UBERON:0000473)
- **Cardiovascular** — one prenatal case with ventricular septal defect (**PMID:41931584**); the index patient had a cutaneous vascular malformation (**PMID:30239107**). *Not established as a recurrent feature.*
- **Hepatic** — hepatic calcifications in one case (**PMID:37092498**); isolated finding

**Body systems:** nervous, integumentary, musculoskeletal, digestive, sensory; cardiovascular and hepatobiliary only anecdotally.

### 7.2 Tissue and cell level

- **Hair follicle epithelium**, specifically **outer root sheath keratinocytes (CL:0002561)** — the cell type in which the K6 promoter drove ODC in the transgenic mouse that phenocopies BABS skin/hair
- **Neural progenitor cells (CL:0011020)** / radial glia (CL:0000681) of the ventricular and subventricular zones
- **Oligodendrocytes / myelinating glia** — implicated by the white-matter signal abnormalities and their normalization on treatment
- **Dermal fibroblasts (CL:0002620)** and **erythrocytes (CL:0000232)** — biochemically abnormal and diagnostically accessible

### 7.3 Subcellular level

- **Cytosol (GO:0005829)** — ODC is a cytosolic enzyme; this is where the pathological accumulation occurs
- **Proteasome complex (GO:0000502)**, specifically the **26S proteasome** — the machinery whose substrate recognition is evaded
- **Nucleus (GO:0005634)** — polyamines are chromatin-associated polycations

### 7.4 Localization / lateralization

Brain findings are predominantly **bilateral** (bilateral paraventricular cysts, bilateral perivascular space dilation, diffuse white matter change), though asymmetric/unilateral lesions occur (right subependymal cyst; focal polymicrogyria; porencephalic cyst). Alopecia is **diffuse/generalized** with occasional preserved tufts — e.g., "scalp alopecia outside of tuft of long and coarse hair on central posterior scalp" (**PMID:37092498**).

---

## 8. Temporal Development

### 8.1 Onset

- **Prenatal:** polyhydramnios (55–80%), decreased fetal movement, and — in the 2026 report — second-trimester macrocephaly and VSD detectable by ultrasound (**PMID:41931584**). Prenatal ventriculomegaly and cerebral cysts have been detected (**PMID:37092498**).
- **Birth:** macrosomia/large for gestational age, macrocephaly at birth, hair present (may be sparse or atypically colored), congenitally absent/sparse eyebrows and eyelashes.
- **Neonatal:** hypotonia, feeding difficulty, hypoglycemia, hyperbilirubinemia; respiratory distress with NICU stay in one case.
- **First weeks of life:** the **defining event** — hair loss in large clumps (HP:0003623 Neonatal onset / HP:0011463 Childhood onset for later features).
- **Infancy onward:** developmental delay becomes evident.
- **Adolescence/adulthood:** late-onset epilepsy possible (age 14 in the one reported case).

**Onset pattern:** **congenital/insidious**, not acute. Suggested HPO onset term: **HP:0003577 Congenital onset** for the syndrome; **HP:0003623 Neonatal onset** for the alopecia.

### 8.2 Progression

- **Stages:** no formal staging system exists.
- **Progression rate:** the neurodevelopmental phenotype is **static-with-slow-acquisition**, not neurodegenerative. Skills are gained slowly (walking 17 months–4 years) rather than lost. One patient showed **progressive** motor decline with myopathy and loss of ambulation over 12 years, indicating that a subset may have a progressive motor course (**PMID:37092498**).
- **Course pattern:** chronic, lifelong, generally non-progressive on the cognitive axis; **epilepsy, when present, can be progressive and refractory**.
- **Duration:** lifelong.

### 8.3 Patterns

- **Remission:** no spontaneous remission. **Treatment-induced improvement is well documented** — hair regrowth by 1–2 months of eflornithine, motor gains by 4 months, MRI normalization by ~6 months, sustained at >3 years (**PMID:34282722**, **PMID:37469105**).
- **Critical periods:** This is the most clinically consequential open question. The mouse data are unusually informative here:

> "The ODC inhibitor 2-difluoromethylornithine could prevent hair loss and partially normalize skin histology if administered **before** the onset of ODC overexpression. 2-Difluoromethylornithine could **also reactivate hair growth in animals with complete hair loss.**"
> — Soler et al., *J Invest Dermatol* 1996 (**PMID:8618048**)

That is: for the follicular phenotype, both prevention *and* rescue are achievable. Whether the same holds for the **neurodevelopmental** phenotype — and whether there is a closing window for cortical/white-matter benefit — is **unknown and is the central natural-history question for the field**. The prenatal-diagnosis capability now demonstrated (**PMID:41931584**) makes very-early or even prenatal intervention a live question.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

- **Prevalence: UNKNOWN.** GeneReviews: *"The prevalence of Bachmann-Bupp syndrome is unknown."*
- **Cumulative reported cases (a moving target — cite the year):**

| Source (year) | Published cases | Known worldwide |
|---|---|---|
| GeneReviews (2022) | **9** | +3 unreported known to authors |
| Wikipedia / secondary (Nov 2022) | — | "<30 individuals" |
| Bachmann & Bupp, DMCN (2024) | **11** | <30 |
| Bupp et al., AJMG-C (2025) | **11** | 11 + 6 unreported = **17** |
| VanSickle et al., AJMG-A (**2026**) | **12** | **18, spanning eight countries** |

- **Best current statement:** ~12 published cases; ~18–20 known worldwide across ≥8 countries as of 2026. Suggested `prevalence_class`: **BELOW_1_IN_1000000** with `measure_type: CASES_IN_LITERATURE` and `prevalence_class: NOT_YET_DOCUMENTED` as an alternative honest encoding.
- **Incidence:** not estimable.
- **Ascertainment caveat:** BABS is diagnosable only by sequencing, and the phenotype (DD + alopecia) is distinctive enough that it is likely **under**-ascertained rather than over-ascertained. Expect the count to rise with exome/genome uptake.

### 9.2 Inheritance genetics

- **Pattern:** **Autosomal dominant (HP:0000006)**, essentially always **de novo**.
> "All probands reported to date with BABS whose parents have also undergone molecular genetic testing have the disorder as the result of a de novo ODC1 pathogenic variant." — GeneReviews (**PMID:36007106**)
- **Penetrance:** Believed **complete (100%)** — but note this is inferred from a tiny, ascertainment-biased *de novo* case series with no transmitted families; **treat "100% penetrance" as provisional**.
- **Expressivity:** **Variable** — spanning nonverbal severe ID to a 12-year-old who reads and writes; epilepsy in only ~8%; macrocephaly in only 66–75%.
- **Genetic anticipation:** **Not applicable** (not a repeat expansion).
- **Germline mosaicism:** Not documented, but assumed possible; drives the recurrence-risk counseling figure.
- **Recurrence risk:**
  - Parents test negative → **~1% sibling recurrence risk** (germline mosaicism allowance)
  - A parent carries the variant → **50%**
  - Offspring of an affected individual → **50%** (no reported reproduction to date)
- **Founder effects:** **None.** All variants are private *de novo* events; the only recurrence (c.1242-2A>G in ≥3 individuals) reflects a **mutational hotspot at a canonical splice acceptor**, not a shared haplotype.
- **Consanguinity:** **No role** — dominant *de novo* mechanism.
- **Carrier frequency:** **Not applicable.**

### 9.3 Population demographics

- **Ethnic/ancestry predilection:** **None known.** Cases span **eight countries** (**PMID:41410504**), including the US, EU, and a Chinese prenatal case (**PMID:41931584**). The index case was described as Caucasian; no ancestry enrichment has been reported.
- **Geographic distribution:** worldwide, no clustering. Apparent geographic distribution reflects **where genomic sequencing and the ICPD network reach**, not true biology.
- **Sex ratio:** Reported cases include both sexes (the index case and several others are female; the 23-year-old epilepsy case is male; HPOA lists cryptorchidism in 2/3 males). **No sex bias is established; the sample is far too small to estimate a ratio.** Do not assert one.
- **Age distribution:** reported ages at description range from **prenatal/12 months to 23 years**. No adult natural-history data beyond age 23.

---

## 10. Diagnostics

### 10.1 Suggestive clinical findings (GeneReviews)

Consider BABS in an individual with:
1. **"An unusual pattern of noncongenital alopecia due to sudden-onset hair loss shortly after birth"** — the single most specific pointer
2. Developmental delay, typically **moderate to severe**
3. Hypotonia
4. Supportive: **"metabolomic profile showing abnormal polyamine pathway metabolites, including increased N-acetylputrescine"**

### 10.2 Establishing the diagnosis

Requires **all three** of: consistent clinical/laboratory findings + a heterozygous pathogenic/likely pathogenic *ODC1* variant + abnormal polyamine-pathway metabolomics. *"Heterozygous pathogenic variants in ODC1 that cause BABS are typically gain-of-function variants."*

### 10.3 Genetic testing

| Modality | Utility in BABS | Notes |
|---|---|---|
| **Exome sequencing (ES)** | **High — the historical diagnostic route** | All index cases found by WES (**PMID:30239107**, **PMID:34282722**) |
| **Genome sequencing (GS)** | High | Better for the intron-11 splice variants |
| **Single-gene *ODC1* sequencing** | **100% detection (9/9)** per GeneReviews Table 1 | Appropriate when the alopecia+DD gestalt is recognized |
| **Multigene panel** | Useful if *ODC1* is on the ID/alopecia panel | Confirm gene content before ordering |
| **Deletion/duplication analysis** | **NOT required** | GoF mechanism; CNVs do not cause BABS |
| **Chromosomal microarray** | Low yield for BABS (may be done as first-tier DD workup) | Normal in BABS |
| **Karyotype / FISH** | **Not indicated** | |
| **mtDNA testing** | **Not indicated** | |
| **Repeat expansion testing** | **Not indicated** | |

Reference sequence for reporting: **NM_002539.3 / NP_002530.1**.

### 10.4 Biochemical / omics diagnostics — the BABS-distinctive layer

BABS is one of the few neurodevelopmental disorders with a **directly measurable, treatment-responsive enzymatic biomarker**. Three assays:

1. **Plasma untargeted clinical metabolomics** (UPLC-MS) with Z-scores vs a pediatric reference cohort (n=866). Signature: **↑ N-acetylputrescine**, **↑ acisoga**, **↓ ornithine**, **↓ N-acetylarginine** — with *normal* spermidine/spermine. Suitable for **both diagnosis and treatment monitoring** (**PMID:34282722**).
2. **ODC enzyme activity assay** — ¹⁴C-ornithine radioassay on **red blood cells** (125–137× control) or **primary dermal fibroblasts** (12–17× control). Detailed protocol published (**PMID:40382142**). **This is the assay that adjudicates VUSs** (**PMID:40167220**).
3. **Polyamine quantitation by RP-HPLC** with dansyl chloride derivatization (**PMID:40382146**).

Also: **Western blot for ODC protein** in RBCs/fibroblasts (elevated).

Sample collection, shipment, consent, and biobanking protocols for international polyaminopathy patients are published (**PMID:40382145**) and coordinated through the **ICPD**.

### 10.5 Imaging, electrophysiology, other clinical tests

- **Brain MRI** — abnormal in nearly all; no pathognomonic pattern. Findings listed in §3.4. MRI also serves as a **treatment-response readout** (white matter normalization, cyst resolution).
- **Prenatal ultrasound** — polyhydramnios, macrocephaly, ventriculomegaly, cerebral cysts, VSD; can prompt prenatal diagnosis (**PMID:41931584**).
- **EEG** — indicated only if seizures are suspected.
- **EMG/NCS** — one patient's proximal myopathy was identified by EMG (**PMID:37092498**).
- **Audiology** (sensorineural hearing loss) and **ophthalmology** (refractive error, strabismus, ptosis) — annually.
- **Skin biopsy** — for fibroblast culture (research/functional assay), not for histopathology per se. No diagnostic histopathologic signature has been defined; follicular cysts are the notable dermatopathologic finding.
- **Echocardiogram** — only if a cardiac anomaly is suspected; not routine.

### 10.6 Differential diagnosis (GeneReviews Table 3)

| Gene | Disorder | Distinguishing from BABS |
|---|---|---|
| ***LSS*** | *LSS*-related neurodevelopmental disorder | **Alopecia is CONGENITAL** (BABS alopecia is post-natal onset) |
| ***CHD3*** | Snijders Blok-Campeau syndrome | Ventriculomegaly, joint laxity, different dysmorphic gestalt; no clumped hair loss |
| ***DCAF17*** | Woodhouse-Sakati syndrome | Hypogonadism, diabetes mellitus; later onset |
| ***PAK1*** | IDDMSSD | Ataxia; no consistent hair/skin abnormality |
| ***PTEN*** | Cowden syndrome | Facial trichilemmomas, cancer predisposition |
| Multiple | Ectodermal dysplasias | **Congenital** alopecia; dental anomalies (BABS is **not** associated with dental issues) |

Also worth listing: **other polyaminopathies** — Snyder-Robinson syndrome (*SMS*, X-linked, ~63% epilepsy, no alopecia), Faundes-Banka syndrome (*EIF5A*), DHPS deficiency, DOHH disorder. Per the 2026 review, **macrocephaly + non-congenital alopecia is what separates BABS from the other four**:

> "The majority of patients (9/12, 75%) also presented with macrocephaly, which would be considered a distinctive feature of BABS, as this was not reported in any patients with DHPS deficiency, FABAS, or DOHH disorder." (**PMID:41410504**)

### 10.7 Screening of asymptomatic individuals

- **Newborn screening:** BABS is **not** on any NBS panel. It is, however, an intriguing theoretical candidate given (a) a measurable metabolite in blood and (b) an available treatment with a possible early-intervention window — **but no NBS pilot exists and this should be framed as a hypothesis, not a recommendation.**
- **Carrier screening:** not applicable (de novo dominant).
- **Cascade screening:** not applicable in practice; parental testing is done to establish *de novo* status and refine recurrence risk.

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality

- **No BABS-specific mortality data, survival curves, or life-expectancy estimates exist.** The oldest reported patient is **23 years**. No deaths have been reported in the published series. **Do not assert a life expectancy.**
- Mortality risk, where present, would be expected to derive from **aspiration/feeding complications** and **refractory epilepsy**, not from a disease-intrinsic lethal process.

### 11.2 Morbidity and function

- **Dominant morbidity:** moderate-to-severe intellectual disability, motor delay/hypotonia, communication impairment (three individuals nonverbal at last report), feeding difficulty, and — in one long-followed patient — loss of independent ambulation.
- **Functional range is wide:** from nonverbal and wheelchair-dependent to literate with moderate ID.
- **Disability outcomes:** lifelong need for special education, PT/OT/SLP, and in some cases assistive mobility and enteral feeding.
- **No validated QoL instrument data.** (ICF-based functional characterization has not been done.)

### 11.3 Complications

Aspiration and recurrent respiratory events; refractory epilepsy (rare but severe); constipation; obesity secondary to overgrowth; recurrent follicular cysts requiring dermatologic/surgical drainage; refractive error/strabismus; sensorineural hearing loss; contractures/orthopedic sequelae of hypotonia and immobility.

### 11.4 Cancer risk — an unresolved, important question

*ODC1* is a canonical **c-Myc target and proto-oncogenic driver**; K6/ODC mice develop **spontaneous skin tumors** (**PMID:7671221**) and are so tumor-prone they are used as a **carcinogen-detection bioassay** (**PMID:10906419**). Somatic *ODC1*/polyamine dysregulation is pervasive in human cancer.

Rodan et al. therefore raised surveillance explicitly:
> "As the ODC1 gene has been implicated in neoplasia, cancer surveillance may be important in this disorder." (**PMID:30475435**)

**However:** **no malignancy has been reported in any individual with BABS to date**, GeneReviews' surveillance table does **not** include cancer screening, and the 2025 treatment review documents **no cancer-monitoring protocol**. With ~18 patients and a maximum reported age of 23, the cohort is far too small and young to detect an elevated cancer risk.

**Recommended KB framing:** encode this as an **open mechanistic hypothesis / knowledge gap** (`kind: KNOWLEDGE_GAP`, or `HUMAN_MODEL_MISMATCH` — strong mouse tumor phenotype, no human confirmation), **not** as an asserted phenotype. Note the pleasing irony that the treatment (DFMO) is itself an established **chemopreventive** agent (colorectal adenoma prevention, **NCT00118365**), so treated patients may be incidentally protected.

### 11.5 Recovery potential and prognostic factors

- **Recovery potential is genuinely favorable on treatment** and this is the single most important prognostic modifier known:
> "She demonstrated remarkable improvement in both neurological symptoms and cortical architecture. She gained fine motor skills with the capacity to feed herself and sit with support." (**PMID:34282722**)
> "Treated patients have consistently shown improvement in muscle tone, developmental milestones, and hair regrowth." (**PMID:40167220**)
- **Prognostic factors (all inferred, none validated):** age at treatment initiation; presence of refractory epilepsy; severity of baseline structural brain abnormality; feeding/aspiration status.
- **Prognostic biomarkers:** N-acetylputrescine Z-score and RBC ODC activity are **pharmacodynamic** markers with demonstrated normalization on therapy; whether they **predict** developmental outcome is untested.

---

## 12. Treatment

### 12.1 Targeted therapy — eflornithine (DFMO): the flagship

| Attribute | Detail |
|---|---|
| **Agent** | Eflornithine / α-difluoromethylornithine (DFMO); brand **Iwilfin®** (oral, FDA-approved Dec 2023 for high-risk neuroblastoma maintenance) |
| **CHEBI** | **CHEBI:41948** (eflornithine); CHEBI:749357 (hydrochloride) |
| **NCIT** | **NCIT:C226** Eflornithine; NCIT:C1579 Eflornithine Hydrochloride |
| **Mechanism** | *"DFMO is a specific, mechanism-based irreversible (suicide) inhibitor of ODC"* (**PMID:37469105**). Directly inhibits the accumulated pathological enzyme. |
| **Therapeutic modality** | `SMALL_MOLECULE` |
| **treatment_term** | NCIT:C15986 Pharmacotherapy, with `therapeutic_agent` = CHEBI:41948 |
| **target_mechanisms** | `INHIBITS` the ODC-accumulation / putrescine-overproduction node — a textbook drug-target pattern |
| **Route/formulation** | Oral. Solution (Orbus Therapeutics) and powder (ScinoPharm Taiwan) supplied for clinical use |
| **Dosing (BABS protocol)** | *"Patients begin at a dose of 500 mg/m²/BID for 3 months, increase to 750 mg/m²/BID for another 3 months, and then finally increase to 1000 mg/m²/BID indefinitely"* (**PMID:40167220**) — modeled on pediatric neuroblastoma dosing |
| **Regulatory status for BABS** | **Not FDA-approved for BABS.** Five US patients treated under **FDA-approved single-patient Investigational New Drug (IND)** protocols; ≥1 patient treated off-label outside the US. Earlier reports describe compassionate-use approval. |
| **Number treated** | 6 as of the 2025 report (5 US IND + 1 ex-US); DMCN 2024 reported 4 US + 1 EU |
| **Pharmacology** | Rapid renal clearance necessitates sustained high dosing; pediatric range 1.0–6.0 g/m²/day |
| **Safety** | *"DFMO has extraordinary safety and a specific long-term dosing strategy in children with neuroblastoma even if administered daily for several years."* No adverse effects reported in the treated BABS patients. **Known class effects to monitor (from oncology/trypanosomiasis use): reversible ototoxicity/hearing loss, myelosuppression, GI upset, and — for topical use — skin irritation.** Ototoxicity monitoring is especially relevant given baseline SNHL risk in BABS. |

**Documented outcomes (index patient, Rajasekaran 2021 / Bachmann 2024):**

| Domain | Timeline & outcome |
|---|---|
| Eyebrows | Regrowth at **1 month** |
| Scalp hair | Diffuse regrowth in normal pattern at **2 months** |
| Motor | Self-feeding with spoon (with assistance) and unassisted sitting at **4 months**; later walker use |
| Neuroimaging | *"normalization of the cerebral white matter signal with decrease in volume…resolution of all previously noted cysts"* at ~6 months |
| Metabolites | N-acetylputrescine and acisoga normalized at initiation and stayed reduced; ornithine and N-acetylarginine rose into normal range |
| Skin | *"follicular cysts have not recurred for either patient"* (**PMID:37469105**, **PMID:36443247**) |
| Durability | *"just over 3 years into treatment and on maintenance dosing, the patient continues to show significant clinical improvement."* |

> "This work highlights the strategy of repurposing drugs to treat a rare disease." — Rajasekaran et al. 2021 (**PMID:34282722**)

**Caveats to encode honestly:** all outcome data are **uncontrolled single-arm case reports (n≤6)** with no blinding, no comparator, and no pre-specified endpoints. Developmental gains in a young child on intensified therapy services are confounded. The MRI and metabolite changes are the most objective evidence. **There is no randomized or controlled trial of DFMO in BABS**, and none is registered on ClinicalTrials.gov (searches for BABS/ODC1/polyaminopathy return only oncology and chemoprevention DFMO trials: **NCT00118365**, **NCT00086736**, **NCT03536728**).

### 12.2 Other pharmacotherapy / investigational

- **Other ODC inhibitors and DFMO analogs** — listed by GeneReviews as under investigation.
- **Polyamine transport inhibitors** — e.g., **AMXT 1501**, studied with DFMO in oncology (**NCT03536728**); mechanistically rational for BABS (blocking uptake of dietary/microbial polyamines that could bypass ODC inhibition) but **untested in BABS**.
- **Polyamine-restricted diet** — investigational (GeneReviews).
- **Gut-flora-directed antibiotics to reduce luminal polyamine production** — proposed by Rodan et al. (**PMID:30475435**); **never tested**.
- **Anti-seizure medications** — standard; note one reported case refractory to multiple agents *and* the ketogenic diet.

### 12.3 Advanced therapeutics

- **Gene therapy / gene editing:** none developed. Conceptually, BABS is an *allele-selective knockdown* target (ASO or siRNA against the mutant allele) rather than a gene-replacement target — the pathology is a toxic stabilized protein, not absent protein. **No such program exists.** Note the KB's `antisense_oligonucleotide_therapy` module RNase-H-knockdown paradigm would be the natural conceptual fit if one were ever developed.
- **Cell therapy, RNA therapy, immunotherapy:** none; not applicable.
- **Pharmacogenomics:** no PharmGKB/CPIC guidance for eflornithine relevant to BABS.

### 12.4 Supportive, rehabilitative, and surgical management (GeneReviews Table 5)

| Manifestation | Intervention | NCIT suggestion |
|---|---|---|
| Developmental delay / ID | Early intervention (0–3), developmental preschool (3–5), IEP, ABA and behavioral interventions | NCIT:C15315 Rehabilitation |
| Motor delay / hypotonia | Physical therapy; occupational therapy | NCIT:C15302 Physical Therapy; NCIT:C121351 Occupational Therapy |
| Speech delay / nonverbal | Speech-language pathology, AAC | NCIT:C159273 Speech Therapy |
| Feeding difficulties | Feeding therapy; NG/G-tube if needed | NCIT:C15433 Nutritional Support |
| Obesity / overgrowth | Nutritional intervention, caloric restriction | NCIT:C15447 Dietary Intervention |
| Constipation | Stool softeners, prokinetics, laxatives | NCIT:C15986 Pharmacotherapy |
| Epilepsy | Standard ASMs (one case refractory) | NCIT:C15986 Pharmacotherapy |
| Refractive error / strabismus | Standard ophthalmologic care | NCIT:C49236 Therapeutic Procedure |
| Hearing loss | Audiologic management / amplification | NCIT:C49236 |
| Follicular cysts | Dermatologic treatment, surgical drainage | NCIT:C15329 Surgical Procedure |
| Family support | Social work | NCIT:C15747 Supportive Care |
| Reproductive counseling | Genetic counseling | NCIT:C15240 Genetic Counseling |

### 12.5 Surveillance (GeneReviews Table 6)

| Item | Frequency |
|---|---|
| Growth parameters | Each visit |
| Nutritional status / safety of oral intake | Each visit |
| Constipation assessment | Each visit |
| Mobility & self-help skills (OT/PT) | Each visit |
| Developmental progress / educational needs | Each visit |
| Behavioral assessment (ASD, attention, aggression) | Annually |
| Ophthalmology | Annually or as indicated |
| Audiology | Annually or as indicated |
| Complete skin examination for follicular cysts | At least annually |
| Seizure assessment | As clinically indicated |
| Family/social work support needs | Each visit |

*Notably absent from GeneReviews surveillance: cancer screening (see §11.4).*

### 12.6 Treatment strategy

No formal algorithm exists. In practice:
1. Confirm diagnosis (variant + metabolomics + ODC activity — the latter is decisive for VUSs).
2. Institute full multidisciplinary supportive/rehabilitative care immediately.
3. Refer to the **ICPD** for biochemical characterization and biobanking.
4. Pursue eflornithine via single-patient IND (US) or off-label pathway; escalate 500 → 750 → 1000 mg/m² BID.
5. Monitor pharmacodynamically (N-acetylputrescine Z-score, RBC ODC activity) and clinically (hair, tone, milestones, MRI); monitor for DFMO class toxicity including audiometry and CBC.

**Personalized-medicine framing:** BABS is a genuine *N-of-1-to-N-of-6 precision medicine* exemplar — genotype-directed, biomarker-monitored, mechanism-matched.

---

## 13. Prevention

### 13.1 Primary prevention

**Not possible.** BABS arises from *de novo* germline variants with no known modifiable determinant. There is no vaccination, no risk-factor modification, and no environmental lever.

### 13.2 Secondary prevention (early detection)

- **Genomic:** early ES/GS in an infant with the DD + post-natal clumped alopecia gestalt is the practical early-detection route.
- **Biochemical:** plasma N-acetixputrescine on clinical metabolomics can flag the diagnosis; **hypothetically** a newborn-screening analyte, but **no NBS program or pilot exists** — this is speculation, not policy.
- **Prenatal:** the 2026 report demonstrates that second-trimester ultrasound findings (macrocephaly, VSD) can trigger prenatal molecular diagnosis (**PMID:41931584**), and polyhydramnios/ventriculomegaly/cerebral cysts are recurrent prenatal signals.
- **Rationale for early detection is unusually strong here** because a mechanism-matched treatment exists and mouse data show pre-onset DFMO **prevents** the follicular phenotype (**PMID:8618048**).

### 13.3 Tertiary prevention

This is where the actionable prevention lives: eflornithine to prevent progression/persistence of alopecia, hypotonia, follicular cysts, and possibly white-matter injury; aspiration precautions and feeding management; seizure control; caloric management to prevent obesity; annual skin/eye/ear surveillance.

### 13.4 Genetic screening and counseling

- **Genetic counseling (NCIT:C15240)** is indicated for every family: confirm *de novo* status by parental testing; counsel **~1% sibling recurrence** if parents are negative (germline mosaicism), **50%** if a parent carries the variant, **50%** for offspring of an affected individual.
- **Prenatal diagnosis and preimplantation genetic testing (PGT-M)** are technically available once the familial variant is known: *"Given this risk, prenatal and preimplantation genetic testing may be considered."* (GeneReviews)
- **Carrier screening / population genetic screening:** not applicable.

### 13.5 Immunization, public health, environmental interventions, prophylaxis

- **Immunization:** routine childhood immunizations only; no disease-specific vaccine strategy. No contraindication known.
- **Public health / environmental interventions:** **not applicable.**
- **Prophylaxis:** no antimicrobial or other prophylaxis indicated. (Prophylactic *antibiotics to suppress gut polyamine production* is a mechanistic proposal, not a recommendation.)

---

## 14. Other Species / Natural Disease

### 14.1 Taxonomy and orthology

| Species | NCBI Taxon | Gene | Notes |
|---|---|---|---|
| *Homo sapiens* | NCBITaxon:9606 | *ODC1* (Gene 4953) | The disease species |
| *Mus musculus* | NCBITaxon:10090 | *Odc1* | The workhorse model; MGI ID **MGI:97402** — *verify* |
| *Rattus norvegicus* | NCBITaxon:10116 | *Odc1* | Antizyme biology largely worked out in rat systems |
| *Danio rerio* | NCBITaxon:7955 | *odc1* | Used for other polyaminopathies (DHPS zebrafish model, **PMID:39297975**/PMC11429087); **no BABS zebrafish model published** |
| *Trypanosoma brucei* | NCBITaxon:5691 | *ODC* | Pharmacologically pivotal — trypanosomal ODC lacks the antizyme degradation system and is thus constitutively stable, the basis for DFMO's selectivity (**PMID:7730330**) |

The C-terminal degron is **highly evolutionarily conserved** — the predicted farnesylation site C454 is conserved in 215/220 sequences analyzed (**PMID:33806076**).

### 14.2 Natural disease in other species

**None reported.** There is **no OMIA entry for a naturally occurring ODC1 disorder** in companion animals, livestock, or wildlife found in this search. BABS-equivalent disease in animals exists only as **engineered** models. Veterinary relevance: **nil**.

### 14.3 Comparative biology

The comparative story is unusually clean and is the strongest cross-species evidence in the file:
- The **K6/ODC transgenic mouse** (constitutive ODC in hair-follicle outer root sheath keratinocytes near the bulge stem cell niche) develops **alopecia, dermal follicular cysts, excessive skin wrinkling, and enhanced nail growth** — i.e., the *exact* dermatologic tetrad of BABS, including the follicular cysts and nail changes.
- Bupp et al. framed the index human case explicitly against this:
> "This is the first human case confirming similar symptoms observed in a transgenic ODC1 mouse model first described over 20 years ago." (**PMID:30239107**)
- **Evolutionary conservation of the mechanism** is complete: the 37-residue C-terminal degron, antizyme-stimulated ubiquitin-independent 26S degradation, and DFMO sensitivity are all conserved mouse↔human.
- **Divergence:** *Trypanosoma brucei* lacks antizyme-mediated ODC degradation entirely, which is why DFMO is a trypanocide — a natural "phenocopy" of the BABS lesion at the organismal level.

### 14.4 Transmission

**Not applicable.** BABS has no zoonotic potential and no cross-species transmissibility.

---

## 15. Model Organisms

### 15.1 The K6/ODC transgenic mouse — the phenocopy model

**Construct:** bovine keratin 6 promoter driving a mutated ODC transgene in **outer root sheath keratinocytes (CL:0002561)** of the hair follicle near the bulge stem cell niche. Model type: **mammalian, transgenic (gain-of-function overexpression)**.

**Phenotype recapitulation — excellent for the ectodermal arm:**
> "Effects observed include development of dermal follicular cysts, excessive skin wrinkling, enhanced nail growth, alopecia, and spontaneous tumor development. These results indicate that up-regulation of polyamine biosynthesis can profoundly disturb skin homeostasis and alter susceptibility to neoplastic development."
> — Megosh et al., *Cancer Res* 1995 (**PMID:7671221**)

> "These transgenic mice have a normal first hair cycle, but lose their hair completely beginning 2-3 wk after birth… The ODC inhibitor 2-difluoromethylornithine could prevent hair loss and partially normalize skin histology if administered before the onset of ODC overexpression. 2-Difluoromethylornithine could also reactivate hair growth in animals with complete hair loss. Our results suggest that ODC is an important regulatory gene for the mouse hair follicle."
> — Soler et al., *J Invest Dermatol* 1996 (**PMID:8618048**)

Note the striking temporal parallel: mice have a **normal first hair cycle then lose hair at 2–3 weeks**; BABS infants have **hair at birth then shed it in clumps within weeks**.

**Putrescine — not spermidine/spermine — is the effector**, matching the human metabolomic signature:
> "The regulatory polyamine in this model appears to be putrescine, the immediate product of ornithine decarboxylase."
> — Peralta Soler et al., *Cancer Res* 1998 (**PMID:9563478**)

**Model limitations:** (a) expression is **skin/follicle-restricted (K6 promoter)**, so the model does **not** recapitulate the neurodevelopmental, macrocephaly, hypotonia, or brain-imaging phenotypes — the dominant human morbidity; (b) it is an **overexpression** model, not a knock-in of the human degron truncation, so the stoichiometry and cell-type distribution differ; (c) the **tumor phenotype is prominent in mice but has not been observed in humans with BABS**, a genuine human-model mismatch that should be recorded as such rather than translated forward.

**Applications:** hair-cycle biology; DFMO prevention-vs-rescue timing (directly informs the human critical-period question); skin carcinogenesis; and — as a 30-year retrospective published in 2026 — mechanisms of polyamine-promoted tumorigenesis including stem-cell recruitment, chromatin remodeling, metabolic reprogramming, angiogenesis, and immune modulation (**PMID:41925768**). Also validated as a sensitive carcinogen-identification bioassay (**PMID:10906419**).

### 15.2 The *Odc1* knockout mouse — the loss-of-function arm

> "Embryonic day E3.5 ODC-deficient embryos were capable of uterine implantation and induced maternal decidualization yet failed to develop substantially thereafter… loss of ODC does not affect cell growth per se but rather is required for survival of the pluripotent cells of the inner cell mass. Therefore, ODC plays an essential role in murine development."
> — Pendeville et al., *Mol Cell Biol* 2001 (**PMID:11533243**)

**Odc1^-/-^ is embryonic lethal (peri-implantation); Odc1^+/-^ heterozygotes are "viable, normal, and fertile."** This is directly relevant: it shows that (a) *ODC1* haploinsufficiency does not produce BABS, reinforcing that BABS is GoF; and (b) complete ODC ablation is not survivable — which sets a theoretical floor on how aggressively ODC can be inhibited therapeutically (though DFMO's clinical safety record indicates a wide window).

### 15.3 Cellular and in vitro models

- **Patient-derived primary dermal fibroblasts** — the best-characterized BABS cell model. Show 12–17× ODC activity, elevated ODC protein and putrescine; **DFMO exposure "reduced the ODC activity and putrescine to levels observed in controls without adversely affecting cell morphology or inducing cell death"** (**PMID:31249027**). This is the *in vitro* proof-of-concept that directly justified the human trial-of-one — an exemplary bench-to-bedside chain.
- **Patient RBCs** — 125–137× ODC activity; a non-invasive biomarker source.
- **Cerebral organoids** (not patient-derived) — used to link *ODC1* expression to neural progenitor proliferation (**PMID:33806076**).
- **The 1989 Ghoda C-terminal truncation construct** (**PMID:2928784**) is, retrospectively, the founding *in vitro* model of the BABS lesion.

### 15.4 Models that do NOT exist (gaps)

- **No knock-in mouse carrying a human BABS *ODC1* C-terminal truncation allele** — this is the most conspicuous missing model, and the only one that could address the neurodevelopmental phenotype and treatment-window question.
- **No BABS zebrafish model** (in contrast to DHPS deficiency, which has one).
- **No patient-derived iPSC or iPSC-derived neuron/organoid model.**
- **No conditional/neural-specific ODC overexpression model.**
- **No MorPhiC ODC1 null-allele dataset** identified.

### 15.5 Model resources

MGI (mouse), IMPC/KOMP (for *Odc1* alleles), Alliance of Genome Resources, ZFIN, IMSR/JAX for strain availability. The **ICPD** (Corewell Health / Michigan State University / Snyder-Robinson Foundation) is the primary human-sample and biobanking resource (**PMID:37092498**, **PMID:40382145**).

---

## Curation Notes: Evidence Classification and Verification Flags

### Evidence-source tagging for KB items

| Source type | PMIDs |
|---|---|
| **HUMAN_CLINICAL** | 30239107, 30475435, 34477286, 34282722, 36443247, 37092498, 36007106, 37469105, 40167220, 41410504, 41931584 |
| **IN_VITRO** | 31249027, 2928784, 1334232, 40382142, 40382146 |
| **MODEL_ORGANISM** | 7671221, 8618048, 9563478, 11533243, 10906419, 9688139, 7730330, 41925768 |
| **COMPUTATIONAL** | 33806076 (molecular dynamics, eQTL mining, organoid RNA-seq reanalysis — mixed; split evidence items by claim) |
| **OTHER** | 36007106 (GeneReviews — expert consensus review) |

> **Do not let model-organism evidence stand alone for human phenotypes.** The K6/ODC skin-tumor phenotype in particular must **not** be carried into the human entry as a phenotype; encode it as a `HUMAN_MODEL_MISMATCH` discussion.

### Items requiring verification before commit

1. **`c.1342A>T` vs `c.1342A>G`** for the index variant — use **A>T** (primary source + ClinVar VCV000983289).
2. **Protein HGVS for `c.1242_1263del22` and `c.1313_1316delCTGT`** — the extracted protein annotations do not reconcile with the cDNA positions. Re-derive from the source tables.
3. **VanSickle 2026 frequency percentages** — internally inconsistent as extracted (11/12 rendered as 83.3%). Prefer GeneReviews Table 2 as the frequency source; re-verify the 2026 table directly.
4. **gnomAD constraint metrics for ODC1** — not retrieved; look up directly if needed (and note their limited relevance to a last-exon GoF mechanism).
5. **ICD-11 code** — not confirmed; do not assert.
6. **MGI:97402** for mouse *Odc1* — not verified in this session.
7. **HP:0025249 "Follicular cyst"** — term ID not verified via OAK; run `just validate-terms` before commit.
8. **CL:0011020 label casing** — OLS returned "Neural progenitor cell"; confirm canonical label with OAK.
9. **Sex ratio** — do not assert; the sample is too small.
10. **Cancer risk** — encode as knowledge gap, not phenotype.

### Suggested module conformance

BABS does not map cleanly onto an existing `kb/modules/` entry. The closest conceptual neighbors are `metabolic_intoxication_decompensation` (an enzymatic block in intermediary metabolism) — but BABS is a **chronic overproduction**, not an episodic catabolic-stress decompensation, so **conformance would be a poor fit**. Consider instead that BABS, Snyder-Robinson syndrome, Faundes-Banka syndrome, DHPS deficiency, and DOHH disorder together justify **a new `polyamine_pathway_dysregulation` module** and/or a **`Polyaminopathies` Grouping** (`grouping_basis: SHARED_PATHWAY`, with a `NECESSARY` `HAS_BIOLOGICAL_PROCESS` criterion on polyamine metabolic process) — the 2026 systematic review (**PMID:41410504**) is purpose-built as the curated rationale for exactly such a grouping.

---

## Sources

**Primary literature (PubMed):**
- Bupp CP et al. *Am J Med Genet A* 2018 — [PMID:30239107](https://pubmed.ncbi.nlm.nih.gov/30239107/)
- Rodan LH et al. *Am J Med Genet A* 2018 — [PMID:30475435](https://pubmed.ncbi.nlm.nih.gov/30475435/)
- Schultz CR et al. *Biochem J* 2019 — [PMID:31249027](https://pubmed.ncbi.nlm.nih.gov/31249027/)
- Prokop JW et al. *Genes (Basel)* 2021 — [PMID:33806076](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8064465/)
- Rajasekaran S et al. *eLife* 2021 — [PMID:34282722](https://elifesciences.org/articles/67097)
- VanSickle EA et al. *Am J Med Genet A* 2021 — [PMID:34477286](https://pmc.ncbi.nlm.nih.gov/articles/PMC9292803/) (correction: [PMID:37078542](https://pubmed.ncbi.nlm.nih.gov/37078542/))
- Bupp C, VanSickle E, Bachmann AS. *GeneReviews* 2022 — [PMID:36007106 / NBK583220](https://www.ncbi.nlm.nih.gov/books/NBK583220/)
- Afrin A et al. *Pediatr Dermatol* 2023 — [PMID:36443247](https://onlinelibrary.wiley.com/doi/full/10.1111/pde.15187)
- Michael J et al. *Med Sci (Basel)* 2023 — [PMID:37092498](https://pmc.ncbi.nlm.nih.gov/articles/PMC10123676/)
- Bachmann AS, Bupp CP. *Dev Med Child Neurol* 2024 — [PMID:37469105](https://pmc.ncbi.nlm.nih.gov/articles/PMC10796844/)
- Wu B et al. *Int J Mol Sci* 2024 — [PMID:38928047](https://pubmed.ncbi.nlm.nih.gov/38928047/)
- Bupp CP et al. *Am J Med Genet C* 2025 — [PMID:40167220](https://pmc.ncbi.nlm.nih.gov/articles/PMC12353620/)
- Schultz CR et al. *Methods Enzymol* 2025 — [PMID:40382142](https://pubmed.ncbi.nlm.nih.gov/40382142/)
- VanSickle EA et al. *Methods Enzymol* 2025 — [PMID:40382145](https://pubmed.ncbi.nlm.nih.gov/40382145/)
- Nwafor A et al. *Methods Enzymol* 2025 — [PMID:40382146](https://pubmed.ncbi.nlm.nih.gov/40382146/)
- VanSickle EA et al. *Am J Med Genet A* 2026 — [PMID:41410504](https://pmc.ncbi.nlm.nih.gov/articles/PMC13270430/)
- Li R et al. *Prenat Diagn* 2026 — [PMID:41931584](https://obgyn.onlinelibrary.wiley.com/doi/10.1002/pd.70147)
- Gilmour SK et al. *Amino Acids* 2026 — [PMID:41925768](https://pubmed.ncbi.nlm.nih.gov/41925768/)

**Mechanism / model organism:**
- Ghoda L et al. *Science* 1989 — [PMID:2928784](https://pubmed.ncbi.nlm.nih.gov/2928784/)
- Murakami Y et al. *Nature* 1992 — [PMID:1334232](https://pubmed.ncbi.nlm.nih.gov/1334232/)
- Megosh L et al. *Cancer Res* 1995 — [PMID:7671221](https://pubmed.ncbi.nlm.nih.gov/7671221/)
- Hua SB et al. *J Biol Chem* 1995 — [PMID:7730330](https://pubmed.ncbi.nlm.nih.gov/7730330/)
- Soler AP et al. *J Invest Dermatol* 1996 — [PMID:8618048](https://pubmed.ncbi.nlm.nih.gov/8618048/)
- Peralta Soler A et al. *Cancer Res* 1998 — [PMID:9563478](https://pubmed.ncbi.nlm.nih.gov/9563478/)
- Chen Y et al. *Toxicol Lett* 2000 — [PMID:10906419](https://pubmed.ncbi.nlm.nih.gov/10906419/)
- Pendeville H et al. *Mol Cell Biol* 2001 — [PMID:11533243](https://pubmed.ncbi.nlm.nih.gov/11533243/)
- Wei Z et al. *Nature* 2022 (LACC1–NOS2–ODC1) — [PMID:35978195](https://pubmed.ncbi.nlm.nih.gov/35978195/)

**Databases:**
- [OMIM 619075 / 165640](https://omim.org/entry/619075) · [MONDO:0033642 (Monarch)](https://api.monarchinitiative.org/v3/api/entity/MONDO:0033642) · [MedGen C5436741](https://www.ncbi.nlm.nih.gov/medgen/1775930) · [Orphanet 544488](https://www.orpha.net/en/disease/detail/544488) · [NCBI Gene 4953 (ODC1)](https://www.ncbi.nlm.nih.gov/gene/4953) · [UniProt P11926](https://rest.uniprot.org/uniprotkb/P11926) · [HPO annotations, OMIM:619075](https://ontology.jax.org/api/network/annotation/OMIM:619075) · ClinVar VCV000983285–983289, VCV001074405 · [NORD](https://rarediseases.org/rare-diseases/bachmann-bupp-syndrome/) · [Wikipedia](https://en.wikipedia.org/wiki/Bachmann%E2%80%93Bupp_syndrome) · [ClinicalTrials.gov](https://clinicaltrials.gov/) (NCT00118365, NCT00086736, NCT03536728 — DFMO oncology/chemoprevention only; **no BABS trial registered**)

*PubMed metadata and abstracts in this report were retrieved via NCBI E-utilities and PubMed Central; DOIs are listed where retrieved.*