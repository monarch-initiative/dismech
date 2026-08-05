---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-4-6
cached: false
start_time: '2026-06-29T19:47:13.293259'
end_time: '2026-06-29T19:53:53.757155'
duration_seconds: 400.46
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Trichothiodystrophy
  mondo_id: MONDO:0018053
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
  web_search_requests: 16
  num_turns: 23
  total_cost_usd: 1.4142999
  session_id: 47773791-be6a-5374-abd7-2aac0ef4f74c
  stop_reason: end_turn
citation_count: 20
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Trichothiodystrophy
- **MONDO ID:** MONDO:0018053 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Trichothiodystrophy** covering all of the
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

I now have comprehensive data to write the full report. Let me compile it.

---

# Trichothiodystrophy (TTD): Comprehensive Disease Research Report

**Report Date:** June 29, 2026
**Target Disease:** Trichothiodystrophy
**MONDO ID:** MONDO:0018053
**Disease Category:** Mendelian / Rare Autosomal Recessive Neuroectodermal Disorder

---

## 1. Disease Information

### Overview

Trichothiodystrophy (TTD) is a rare, autosomal recessive (and rarely X-linked) multisystem neuroectodermal disorder defined by the hallmark finding of sulfur-deficient, brittle hair with reduced cysteine-rich matrix protein content. The name derives from the Greek *trichos* (hair), *thio* (sulfur), and *dystrophy* (abnormal development). TTD encompasses a phenotypic spectrum ranging from mild isolated hair and skin involvement to a severe multisystem syndrome affecting neurological development, growth, immunity, fertility, and multiple organ systems.

The disorder was first described in 1974 by Price et al. (PMID: 4460955) and has since been recognized as a disorder at the intersection of DNA repair and transcriptional regulation. A landmark systematic review of 112 published cases (PMID: 18603627) characterized the full clinical spectrum, establishing phenotype frequencies used throughout the literature.

A critical and clinically important distinction: unlike xeroderma pigmentosum (XP), which shares causal genes with TTD, patients with TTD do **not** have an elevated predisposition to skin cancer, despite harboring defects in nucleotide excision repair (NER).

### Key Identifiers

| Identifier | Value |
|---|---|
| OMIM | #601675 (TTD1, photosensitive); #616390 (TTD2, photosensitive); #616395 (TTD3, photosensitive); #234050 (TTD4, non-photosensitive); additional entries for TTD5–TTD7 |
| Orphanet | ORPHA:33364 |
| MONDO | MONDO:0018053 |
| ICD-10 | Q84.1 (congenital morphological disturbances of hair) / L67.8 |
| MeSH | D015649 |
| OMIA | N/A (no well-characterized natural animal disease) |

### Common Synonyms and Alternative Names

- PIBIDS syndrome (Photosensitivity, Ichthyosis, Brittle hair, Intellectual impairment, Decreased fertility, Short stature) — the photosensitive form
- IBIDS syndrome (non-photosensitive form with ichthyosis)
- BIDS syndrome (non-photosensitive without ichthyosis)
- Tay syndrome
- Sulfur-deficient brittle hair syndrome
- Pollitt syndrome
- PIBI(D)S
- TTD-A, TTD-B, TTD-C, TTD-NPS (genotype-based subtypes)

---

## 2. Etiology

### Causal Factors

TTD is a genetically heterogeneous disorder caused by biallelic loss-of-function variants (or hemizygous X-linked variants) in genes encoding components of the general transcription/DNA repair machinery. Disease-causing mutations impair either the TFIIH transcription/repair complex, other transcription factors (TFIIE), tRNA aminoacyl synthetases, or RNA-splicing factors. The unifying molecular pathology is a quantitative or qualitative reduction in transcriptional fidelity and/or proteostasis.

### Risk Factors

**Genetic risk factors (causal variants)**

TTD is classified into photosensitive (PS-TTD) and non-photosensitive (NPS-TTD) forms based on whether the causal gene participates in NER:

*Photosensitive TTD (~50% of all TTD cases):*
- **ERCC2 (XPD; HGNC:3434):** Most common cause; mutations account for ~29% of all TTD cases. Encodes the XPD subunit of TFIIH, a 5'→3' helicase. Missense variants predominantly affecting COOH-terminal region (e.g., R722W, R658C, A725P) are characteristic. Point mutations at positions distinct from XP hotspots distinguish TTD from XP-D. OMIM #601675 (TTD1).
- **ERCC3 (XPB; HGNC:3435):** Very rare (~2% of cases); encodes the XPB subunit of TFIIH, a 3'→5' helicase. OMIM #616390 (TTD2).
- **GTF2H5 (TTDA; HGNC:30811):** Encodes the smallest TFIIH subunit (p8/TTDA), ~2% of cases. Loss-of-function mutations cause complete NER deficiency in vitro. OMIM #616395 (TTD3).

*Non-photosensitive TTD (~50% of all TTD cases):*
- **MPLKIP (TTDN1; HGNC:25985):** Encodes M-phase-specific PLK1-interacting protein; functions in RNA splicing and mitosis; accounts for <20% of NPS-TTD. OMIM #234050 (TTD4).
- **GTF2E2 (TFIIEβ; HGNC:4655):** Encodes the β subunit of TFIIE; mutations destabilize the TFIIE complex; confirmed in multiple NPS-TTD cases (PMID: 26996949). OMIM #615919 (TTD5).
- **RNF113A (HGNC:21178):** X-linked; encodes an E3 ubiquitin ligase and spliceosome component; X-linked dominant in females, hemizygous males affected. OMIM #300953 (TTD6).
- **AARS1 (HGNC:20):** Encodes alanyl-tRNA synthetase 1; compound heterozygous missense variants cause NPS-TTD with protein instability and reduced aminoacylation activity (PMID: 33909043).
- **MARS1 (HGNC:6898):** Encodes methionyl-tRNA synthetase 1; homozygous missense variants (e.g., V401M) reduce protein stability to ~30% of control (PMID: 33909043).
- **CARS1 (HGNC:1493):** Encodes cysteinyl-tRNA synthetase 1; biallelic variants cause NPS-TTD (PMID: 30824121).
- **TARS1 (HGNC:11578):** Encodes threonyl-tRNA synthetase 1; recently implicated in NPS-TTD.

**Approximately 37% of TTD cases with confirmed DNA repair defects remain genetically uncharacterized** (PMID: 18603627), suggesting additional causal loci remain to be identified.

**Environmental risk factors**

- **Consanguinity:** Reported in 17% of cases in the systematic review (PMID: 18603627), substantially elevating risk for biallelic mutations in autosomal recessive forms.
- No specific exogenous environmental risk factors are established. The disease is purely genetic in etiology.
- UV exposure is a precipitating trigger for photosensitivity symptoms (sunburn, erythema) in PS-TTD but is not causative.

### Protective Factors

No established genetic or environmental protective factors are known. Avoidance of UV exposure reduces severity of cutaneous manifestations in PS-TTD.

### Gene-Environment Interactions

In photosensitive TTD, UV radiation interacts with the NER repair deficit to produce exaggerated erythema and acute photosensitivity. Crucially, despite NER deficiency, the pro-oncogenic consequences of unrepaired UV photoproducts that cause skin cancer in XP patients do **not** occur in TTD (PMID: 10667598). This paradox is hypothesized to reflect the anti-tumorigenic properties of TTD mutations in melanocytic cells through cell cycle and transcriptional effects distinct from simple repair-deficiency (PMID: 40918647, 2025).

---

## 3. Phenotypes

The following frequencies are derived from the systematic review of 112 published cases (PMID: 18603627).

### Hair and Nail Features (Defining Characteristics)

| Phenotype | Frequency | HPO Term |
|---|---|---|
| Brittle hair / hair shaft abnormalities | 96% | HP:0008070 |
| "Tiger tail" banding on polarized microscopy | 73% | HP:0002217 |
| Decreased hair sulfur/cystine content | 71% | HP:0002223 |
| Sparse hair / hypotrichosis | 48% | HP:0008070 |
| Alopecia | 39% | HP:0001596 |
| Nail onychodystrophy | 37% | HP:0001甲 / HP:0003821 |

**Character of hair findings:** Hair is short, fragile, and breaks at irregular intervals. Scanning electron microscopy and transmission electron microscopy reveal abnormal cuticular scale structure. Light microscopy shows trichorrhexis nodosa-like fractures. Polarized light microscopy reveals alternating bright and dark "tiger tail" bands, reflecting uneven distribution of cysteine-rich matrix proteins—a pathognomonic finding. Amino acid analysis demonstrates approximately 50% reduction in cysteine content compared to controls.

**HPO:** Brittle hair = HP:0008070; Tiger tail banding = HP:0002217; Sparse hair = HP:0001070.

### Neurological Phenotypes

| Phenotype | Frequency | HPO Term |
|---|---|---|
| Developmental delay / intellectual disability | 86% | HP:0001263 |
| Microcephaly | 50% | HP:0000252 |
| Hypomyelination / dysmyelination | ~40% (MRI data) | HP:0003429 |
| Abnormal gait / ataxia | 26% | HP:0002355 |
| Seizures | 6% | HP:0001250 |
| Sensorineural hearing loss | 4% | HP:0000407 |

**Onset:** Developmental delays present in infancy; MRI abnormalities (dysmyelination, white matter signal changes, cerebellar atrophy, dilated ventricles) detectable in early childhood. Hypomyelination reflects impaired thyroid hormone receptor (TR) stabilization in the brain due to reduced TFIIH levels (PMID: 17952069).

**Severity:** Intellectual disability ranges from mild to severe; progressive dysmyelination may worsen over first decade.

### Growth Features

| Phenotype | Frequency | HPO Term |
|---|---|---|
| Short stature | 73% | HP:0004322 |
| Intrauterine growth restriction (IUGR) | 21% | HP:0001511 |
| Low birth weight (<2500g) | 37% | HP:0001518 |

**Progression:** Growth deficiency is typically present from birth and persists. Nutritional support is often required (PMID: 25396826 — growth and nutrition in TTD children).

### Skin Phenotypes

| Phenotype | Frequency | HPO Term |
|---|---|---|
| Ichthyosis | 65% | HP:0008064 |
| Collodion membrane at birth | 26% | HP:0001360 |
| Photosensitivity | 42% | HP:0000992 |

**Character:** Ichthyosis is typically lamellar or congenital ichthyosiform erythroderma in type. Photosensitivity in PS-TTD manifests as acute exaggerated sunburning without skin cancer. Collodion membrane at birth (tight, shiny, film-like encasement) is a significant neonatal manifestation requiring intensive care.

### Ocular Features

| Phenotype | Frequency | HPO Term |
|---|---|---|
| Any ocular abnormality | 51% | — |
| Cataracts | 29% (total); 7% congenital | HP:0000518 |
| Other (nystagmus, strabismus) | Variable | HP:0000639, HP:0000486 |

### Systemic / Other Features

| Phenotype | Frequency | HPO Term |
|---|---|---|
| Recurrent infections | 46% | HP:0002718 |
| Facial dysmorphism | 66% | HP:0001999 |
| Abnormal birth characteristics | 55% | — |
| Maternal pregnancy complications (preeclampsia, HELLP) | 28% | — |
| Gonadal dysgenesis / hypogonadism | 14% | HP:0000144 |
| Beta-thalassemia / anemia | Rare; ~10 cases | HP:0001878 |

**Pregnancy complications:** Mothers carrying TTD-affected fetuses have elevated rates of HELLP syndrome and preeclampsia (28% in the systematic review), possibly related to placental TFIIH dysfunction.

**Beta-thalassemia connection:** A subset of TTD patients (mostly ERCC2-mutant) have beta-thalassemia. Seminal work (PMID: 11734544) demonstrated that mutant TFIIH fails to adequately transcribe the beta-globin gene during terminal erythroid differentiation (a high-demand transcriptional context), directly implicating transcriptional insufficiency in this phenotype.

### Progeroid Features

TTD mouse models and some human patients exhibit segmental progeroid features including early cataracts, osteoporosis, and reduced bone stem cells, suggesting accelerated aging in some tissues. This is consistent with the role of TFIIH in maintaining transcriptional fidelity needed for tissue homeostasis (PMID: 21357150).

---

## 4. Genetic / Molecular Information

### Causal Genes (Summary Table)

| Gene | HGNC ID | Protein | TTD Type | OMIM Disease |
|---|---|---|---|---|
| ERCC2 (XPD) | HGNC:3434 | XPD helicase (TFIIH) | PS-TTD (TTD1) | #601675 |
| ERCC3 (XPB) | HGNC:3435 | XPB helicase (TFIIH) | PS-TTD (TTD2) | #616390 |
| GTF2H5 (TTDA) | HGNC:30811 | p8/TTDA (TFIIH) | PS-TTD (TTD3) | #616395 |
| MPLKIP (TTDN1) | HGNC:25985 | M-phase PLK1-interacting protein | NPS-TTD (TTD4) | #234050 |
| GTF2E2 | HGNC:4655 | TFIIEβ | NPS-TTD (TTD5) | #615919 |
| RNF113A | HGNC:21178 | E3 ubiquitin ligase / spliceosome | NPS-TTD (TTD6; X-linked) | #300953 |
| AARS1 | HGNC:20 | Alanyl-tRNA synthetase 1 | NPS-TTD | — |
| MARS1 | HGNC:6898 | Methionyl-tRNA synthetase 1 | NPS-TTD | — |
| CARS1 | HGNC:1493 | Cysteinyl-tRNA synthetase 1 | NPS-TTD | — |
| TARS1 | HGNC:11578 | Threonyl-tRNA synthetase 1 | NPS-TTD | — |

### Pathogenic Variants

- **ERCC2:** Missense mutations are by far the most common. Hotspot positions include: R722W (c.2164C>T), A725P (c.2173G>C), R658C (c.1972C>T), R112H (c.335G>A). Importantly, TTD-causing mutations in ERCC2 predominantly occur at positions distinct from XP-D mutations, with XP mutations clustering near positions Arg683, while TTD mutations cluster in both NH2- and COOH-terminal regions (PMID: 9182770). All are germline, autosomal recessive (homozygous or compound heterozygous).
- **GTF2H5:** Loss-of-function; includes nonsense and splice-site variants. Homozygous knockout in mice is embryonic lethal (PMID: 23630104).
- **AARS1 / MARS1 / CARS1 / TARS1:** Missense variants reducing protein stability and aminoacylation enzyme activity (PMID: 33909043).

**Key phenotype–genotype correlations:**
- Mutations in the NH2-terminal region of XPD → greater UV sensitivity than COOH-terminal mutations
- Gene dosage (total residual TFIIH) appears to correlate with clinical severity more than the site of mutation alone (ScienceDirect; Chip et al.)
- All TTD mutations lead to reduced cellular TFIIH concentration (up to 70% below normal), suggesting destabilization of the complex rather than simple loss-of-one-subunit function (PMID: 12393803)

### Modifier Genes

No well-established modifiers. However, the genetic background modulates phenotype severity in mouse models.

### Chromosomal Abnormalities

None documented for TTD; all cases arise from point mutations or small indels.

---

## 5. Environmental Information

### Environmental Factors

- **Ultraviolet radiation:** In PS-TTD, UV exposure triggers acute photosensitivity. Patients sunburn severely but do not develop squamous or basal cell carcinoma.
- No specific chemical, occupational, infectious, or dietary environmental triggers have been identified as contributing to disease development.

### Lifestyle Factors

- Sun avoidance is critical for PS-TTD patients; failure to protect skin leads to acute and cumulative UV damage.
- No smoking, alcohol, or diet associations are established.

### Infectious Agents

No infectious agents cause or trigger TTD. However, TTD patients have high susceptibility to **recurrent infections** (46% of cases), particularly respiratory infections and sepsis, which are the leading cause of death in children (13/20 deaths in the systematic review were infection-related; PMID: 18603627).

---

## 6. Mechanism / Pathophysiology

### Core Molecular Mechanism: TFIIH Complex Dysfunction

The central mechanistic thread in photosensitive TTD is destabilization and reduced cellular concentration of the **TFIIH** transcription/repair complex. TFIIH is a 10-subunit complex organized in two subcomplexes:
- **Core complex** (7 subunits): XPB (ERCC3), XPD (ERCC2), p62 (GTF2H1), p52 (GTF2H4), p44 (GTF2H2), p34 (GTF2H3), TTDA (GTF2H5)
- **CAK (CDK-activating kinase) module** (3 subunits): CDK7, cyclin H, MAT1

TFIIH serves dual functions:
1. **Basal transcription (RNA Pol II initiation):** Opens the promoter DNA via XPB helicase activity; phosphorylates RNA Pol II CTD via CDK7
2. **Nucleotide excision repair (NER):** Unwinds DNA around bulky adducts (UV photoproducts, cisplatin adducts) via XPB and XPD helicases to enable lesion excision

In TTD, mutations in ERCC2, ERCC3, or GTF2H5 cause the mutant subunit to destabilize the entire TFIIH complex, reducing its intracellular concentration by up to 70% (PMID: 12393803). This "TFIIH insufficiency" impairs **both** NER (causing photosensitivity) **and** basal transcription (causing developmental abnormalities). The transcriptional impairment is particularly manifest during high-demand transcriptional states—terminal differentiation events in hair, skin, brain myelin, and erythroid cells.

**Key evidence (PMID: 12820975):** TTD-causing XPD mutations confer significant in vitro basal transcription defects, while XP-causing mutations in the same gene largely spare transcriptional function. This distinction explains why TTD has developmental/transcriptional phenotypes while XP has predominantly cancer-predisposition phenotypes.

### Pathway 1: Hair and Skin Abnormalities (Cysteine-Rich Protein Transcription Failure)

During terminal differentiation of hair matrix cells, the gene family encoding cysteine-rich matrix proteins (UHAs/KAPs — keratin-associated proteins) is among the last and most highly transcribed. When TFIIH levels are insufficient, transcription of these high-sulfur protein genes fails preferentially in the final burst of differentiation, leading to:
- Reduced incorporation of cysteine-rich proteins into the hair cortex
- Reduced disulfide bonding → brittle, fragile hair
- Similarly reduced cysteine-rich proteins in nails → onychodystrophy
- Reduced barrier function in skin → ichthyosis

The hair defect is not caused by a primary structural protein mutation but by a **transcriptional insufficiency** in a gene expression program requiring near-maximal TFIIH activity.

**Biological processes (GO):** GO:0006351 (transcription, DNA-templated), GO:0045087 (innate immune response), GO:0006366 (transcription by RNA polymerase II)
**Cell types (CL):** CL:0002559 (hair follicle matrix cell), CL:0000312 (keratinocyte)

### Pathway 2: Neurological Abnormalities (Thyroid Hormone Receptor Coactivation)

TFIIH is required as a co-activator for thyroid hormone receptors (TR) at target gene promoters in the developing brain (PMID: 17952069). Studies in *XpdTTD* mice showed:
- Spatial and selective deregulation of thyroid hormone-responsive gene expression in the brain
- TFIIH is required to stabilize TR-DNA binding at responsive elements
- Reduced expression of myelin basic protein (MBP) and other myelination genes (thyroid hormone targets) → hypomyelination/dysmyelination
- Cerebellar development disrupted → ataxia

This explains the cardinal neurological triad: intellectual disability, microcephaly, and dysmyelination.

**Biological processes (GO):** GO:0006357 (regulation of transcription by RNA polymerase II), GO:0022008 (myelination), GO:0007399 (nervous system development)
**Cell types (CL):** CL:0000128 (oligodendrocyte), CL:0000540 (neuron)

### Pathway 3: Beta-Thalassemia via Transcriptional Insufficiency

The HBB (beta-globin) gene requires very high transcriptional rates during terminal erythroid differentiation. TFIIH mutations impair this high-demand transcription, reducing beta-globin production and causing beta-thalassemia trait or mild beta-thalassemia (PMID: 11734544).

**Cell types (CL):** CL:0000765 (erythroblast), CL:0000232 (erythrocyte)

### Pathway 4: Ribosomal Dysfunction (Common Pathomechanism Across All TTD Forms)

A unifying 2023 study (PMC: 10377840) demonstrated that disrupting TTDN1 (MPLKIP) or RNF113A—which are spliceosome components rather than TFIIH components—produces a converging downstream pathology:
- **Reduced UBF** (upstream binding factor, the master RNA Pol I transcription activator) at the mRNA level
- **Impaired RNA Pol I transcription** → reduced 47S pre-rRNA synthesis
- **Disrupted rRNA processing** → reduced 18S rRNA → fewer small ribosomal subunits
- **Elevated translational error rate** → misfolded protein accumulation
- **Proteostasis collapse** → carbonylated protein accumulation, loss of protein quality control

The authors propose that **ribosomal dysfunction** represents a "common underlying pathomechanism of TTD" that explains neurodevelopmental phenotypes across genetically heterogeneous TTD forms. This unified model connects TFIIH-dependent (NPS and PS) and non-TFIIH-dependent (NPS) TTD through a convergent effect on translational fidelity.

**Biological processes (GO):** GO:0042254 (ribosome biogenesis), GO:0006364 (rRNA processing), GO:0006412 (translation), GO:0006986 (response to unfolded protein)

### Pathway 5: tRNA Synthetase Deficiency and Protein Synthesis Errors

AARS1, MARS1, CARS1, and TARS1 mutations cause loss of aminoacyl-tRNA synthetase activity, directly reducing the fidelity and rate of protein translation (PMID: 33909043). Specifically in TTD:
- Reduced aminoacylation → reduced tRNA charging → mistranslation
- During high-demand protein synthesis states (hair matrix, myelin synthesis), translational errors produce unstable or misfolded structural proteins
- This mechanism converges with the ribosomal dysfunction model: both impair proteostasis during differentiation

### Summary of Mechanistic Causal Chain

```
Germline mutations in ERCC2/ERCC3/GTF2H5
    ↓
Destabilization of TFIIH complex (↓ 70% intracellular levels)
    ↓
Impaired NER ──→ UV photosensitivity (PS-TTD)
    ↓
Impaired RNA Pol II transcription at high-demand loci
    ├─→ KAP gene transcription failure → brittle sulfur-poor hair + ichthyosis
    ├─→ TR-coactivation failure → dysmyelination + intellectual disability
    └─→ HBB transcription failure → beta-thalassemia

Mutations in MPLKIP/RNF113A (splicing)
    ↓
Ribosomal biogenesis disruption (↓ UBF, ↓ 18S rRNA)
    ↓
Reduced translational fidelity → proteostasis collapse → multisystem failure

Mutations in AARS1/MARS1/CARS1/TARS1 (aminoacyl-tRNA synthetases)
    ↓
Reduced tRNA aminoacylation → mistranslation → misfolded proteins in differentiation
    ↓
Brittle hair + neurodevelopmental disease (same convergent phenotype)
```

**Upstream molecular defects:** TFIIH destabilization (or spliceosome/ribosome disruption)
**Downstream cellular consequences:** Transcriptional insufficiency → developmental phenotypes; NER deficiency → UV sensitivity

---

## 7. Anatomical Structures Affected

### Organ Level

| System | Manifestation |
|---|---|
| Skin/integument (primary) | Ichthyosis, photosensitivity, collodion membrane |
| Hair/nail (primary) | Brittle sulfur-deficient hair, onychodystrophy |
| Central nervous system (primary) | Dysmyelination, microcephaly, intellectual disability, cerebellar atrophy |
| Eyes | Cataracts, strabismus, nystagmus |
| Growth system / skeleton | Short stature, IUGR, bone density reduction |
| Hematopoietic (secondary) | Beta-thalassemia, anemia |
| Immune system | Susceptibility to infections (functional immunodeficiency mechanisms unclear) |
| Gonads (secondary) | Hypogonadism, decreased fertility |

**UBERON terms:** UBERON:0000414 (mucosa), UBERON:0002097 (skin of body), UBERON:0000955 (brain), UBERON:0000473 (testis), UBERON:0001638 (vein of retina).

### Tissue and Cell Level

- **Epidermis / stratum corneum:** Impaired terminal differentiation
- **Hair follicle matrix cells (CL:0002559):** Failure of KAP gene transcription
- **Oligodendrocytes (CL:0000128):** Impaired myelination via TR-coactivation failure
- **Erythroid precursors (CL:0000765):** Impaired beta-globin transcription
- **Lens epithelium:** Cataract formation mechanism unclear; possibly transcriptional defect

### Subcellular Level

- **Nucleus:** NER deficiency → persistent UV photoproducts; reduced TFIIH concentrations affect RNA Pol II promoter opening
- **Ribosome (GO:0005840):** Reduced 40S ribosomal subunit availability
- **Nucleolus (GO:0005730):** Impaired rRNA synthesis

---

## 8. Temporal Development

### Onset

- **Prenatal:** Many manifestations present in utero; IUGR (21%), collodion membrane at birth (26%), maternal pregnancy complications (28%). Amniotic fluid may show elevated AFP due to skin barrier disruption.
- **Neonatal:** Collodion membrane, low birth weight, early infections, feeding difficulties.
- **Infancy/Early Childhood:** Brittle hair, ichthyosis, developmental delay apparent; recurrent infections, cataracts, hearing evaluation needed.
- **Later Childhood:** Short stature, intellectual disability defined; neurological features (ataxia, spasticity) may progress.

**HPO onset category:** HP:0003623 (neonatal onset) for most manifestations; HP:0003577 (congenital onset) for structural features.

### Progression

- **Disease course:** Non-episodic, chronic, largely non-progressive neurological phenotype; ichthyosis and hair features persist throughout life.
- **Infections:** Episodic, with high early-life mortality risk. 13 of 19 deaths in the systematic review were infection-related; all but one death occurred under age 10.
- **Neurological:** Dysmyelination is present early; may improve partially in some patients as myelination continues through childhood.
- **Progeroid features:** Some older patients and mouse models demonstrate segmental premature aging (reduced bone density, cataracts).

### Prognosis

- **Mortality:** Substantially elevated in childhood; at age 3 years, 10.7% probability of reported death; by age 9 years, 21.3% (PMID: 18603627). Mortality rate approximately 20-fold higher than US population in children ≤10 years.
- **Median age at death:** 3 years in severe cases; all but one deceased patient in the systematic review died under age 10.
- **Cause of death:** Predominantly infections (pneumonia, sepsis)—13 of 19 deaths in the systematic review were infection-related.
- **Survival to adulthood:** Possible in milder forms; one patient in the systematic review was aged 47 years. However, reliable data on adult natural history is limited.

---

## 9. Inheritance and Population

### Epidemiology

- **Prevalence/Incidence:** Approximately **1 in 1,000,000 live births** in Western countries (some estimates range 1.2/million to 1/million). Approximately 100 cases reported worldwide as of 2024, making it an ultra-rare disease.
- **Gender:** Approximately equal sex distribution (51% male, 49% female in systematic review; PMID: 18603627).
- **Geographic distribution:** Cases reported worldwide; no specific geographic clustering except where consanguinity rates are elevated. In the systematic review, Italy (23%), USA (16%), and UK (16%) contributed the most cases, likely reflecting reporting bias.

### Inheritance Pattern

- **Autosomal recessive** for the vast majority of forms (ERCC2, ERCC3, GTF2H5, MPLKIP, GTF2E2, AARS1, MARS1, CARS1, TARS1 — biallelic mutations required).
- **X-linked** for RNF113A-associated TTD; hemizygous males affected; carrier females may have mild or no features.
- **Penetrance:** Complete for classic multisystem forms; some genotype-specific variable expressivity exists.
- **Expressivity:** Highly variable—same mutation can produce mild hair-only disease or severe multisystem disease. Gene dosage (total residual TFIIH) appears to determine severity more than specific mutation location.
- **Consanguinity:** Present in 17% of reported cases (PMID: 18603627).

### Carrier Frequency

Not well established. Given an incidence of ~1/million, the Hardy-Weinberg estimated carrier frequency is approximately 1/500 for the most common causal allele, but direct population surveys are lacking.

---

## 10. Diagnostics

### Clinical/Hair Diagnostic Tests

**Hair polarized light microscopy:**
- The pathognomonic "tiger tail" banding pattern on polarized light microscopy is present in ~73% of cases (PMID: 18603627).
- Alternating birefringent (bright) and non-birefringent (dark) bands reflect alternating zones of high and low sulfur-protein content.
- This is the first-line and most practical diagnostic test.
- **HPO:** HP:0002217 (abnormal hair shaft banding under polarized microscopy)

**Hair amino acid analysis:**
- Cystine/cysteine content approximately 50% of normal in affected hair.
- Semiquantitative methods using sodium azide-dependent oxidation to cysteic acid have been validated (PMID: 15232704).

**Scanning and transmission electron microscopy:**
- Abnormal cuticle morphology; longitudinal ridging; cuticular ruptures.
- Used primarily in research/reference settings.

**UV sensitivity testing (unscheduled DNA synthesis, UDS):**
- For PS-TTD: Reduced post-UV UDS in fibroblasts demonstrates NER deficiency.
- Not routinely available; performed in specialist NER research laboratories.

**Hair ultrastructure analysis:**
- 2023 study (PMC:10575343) described distinct ultrastructural features of TTD hair shafts distinguishable from other brittle hair disorders.

### Biochemical Tests

- **Complete blood count:** Anemia with target cells when beta-thalassemia coexists.
- **Hemoglobin electrophoresis:** Elevated HbA2 in beta-thalassemia-associated TTD.
- **LOINC:** No LOINC code specifically for TTD hair cystine—general amino acid analysis panels apply.

### Neuroimaging

- **Brain MRI:** Demonstrates hypomyelination (periventricular and subcortical white matter T2 changes), cerebellar atrophy, dilated ventricles. Essential for neurological assessment.
- **Pattern:** TTD is listed as a cause of leukodystrophy/hypomyelinating leukodystrophy; a 2025 case series documented ERCC2 variants as "uncommon contributors to progressive hypomyelinating leukodystrophy" (PMID: 39976384).

### Genetic Testing

**Recommended approach:**
- **NGS-based multi-gene panel** testing covering ERCC2, ERCC3, GTF2H5, MPLKIP, GTF2E2, RNF113A, AARS1, MARS1, CARS1, TARS1 — available through clinical laboratories (GTR: condition C1955934).
- **Comprehensive TTD panel** (GTR test ID 560930) covers major photosensitive and non-photosensitive genes.
- **Whole exome sequencing (WES):** Appropriate first-tier test in cases where clinical features are present but diagnosis unclear; cost-effective for genetically heterogeneous conditions.
- **Whole genome sequencing (WGS):** May be warranted in WES-negative cases to identify deep intronic or structural variants.
- **Sanger sequencing:** For confirmation of identified variants and familial testing.

**Prenatal diagnosis:**
- Available via chorionic villus sampling or amniocentesis once familial mutations are identified.
- Preimplantation genetic diagnosis (PGD) is theoretically available.

### Dermoscopy

- **Polarized transilluminating dermoscopy** has been validated for detecting tiger tail banding in scalp hair in vivo (IJDVL, 2023), allowing non-invasive point-of-care diagnosis.

### Differential Diagnosis

| Condition | Key Distinguishing Feature |
|---|---|
| Xeroderma pigmentosum (XP-D) | Skin cancer predisposition; mutations at different XPD positions; no brittle hair |
| Menkes disease | X-linked recessive; copper metabolism defect; pili torti pattern |
| Netherton syndrome | SPINK5 mutations; trichorrhexis invaginata ("bamboo" hair); ichthyosis linearis circumflexa |
| Argininosuccinic aciduria | Argininosuccinate lyase deficiency; trichorrhexis nodosa; hyperammonemia |
| Biotin-responsive basal ganglia disease | Biotin metabolism; different hair type; treatable |

---

## 11. Outcome / Prognosis

### Survival

- **Early childhood mortality:** ~20-fold elevated vs. US population in children ≤10 years (PMID: 18603627).
- **Probability of death by age 3:** 10.7%; by age 9: 21.3%.
- **Cause:** Predominantly recurrent and severe infections (pneumonia, sepsis).
- **Adult survival:** Possible; the systematic review identified patients up to age 47 years in the mild end of the spectrum.

### Morbidity

- Severe intellectual disability and neurological impairment in most affected individuals significantly impair quality of life and require intensive multidisciplinary support.
- Recurrent infections necessitate prompt antibiotic therapy and prophylactic measures.
- Ichthyosis management is lifelong but improves with emollient therapy.
- Short stature and growth failure may benefit from nutritional intervention (PMID: 25396826).

### Prognostic Factors

- Severity of intellectual disability and neurological involvement is a key prognostic factor.
- Early infection events and sepsis carry the highest mortality risk in early childhood.
- Patients with milder phenotypes (hair only, mild developmental delay) can achieve reasonable quality of life into adulthood.
- Beta-thalassemia, when present, typically manifests as trait or mild disease and rarely requires transfusion.

---

## 12. Treatment

### Current Management Approach

TTD has no curative treatment. Management is **multidisciplinary and symptom-directed.** As stated in NORD resources: "TTD may be adequately managed through topical agents, sun protection measures, use of visual aids, nutritional and growth support, and occupational therapy."

### Pharmacotherapy

**Ichthyosis:**
- **Emollient therapy:** First-line; extensive topical moisturizers (urea-containing creams, petrolatum, ceramide-based emollients) to reduce scale and improve skin barrier. Applied multiple times daily.
  - **MAXO:** MAXO:0000950 (supportive care)
  - **NCIT:** NCIT:C15986 (Pharmacotherapy)
- **Keratolytics:** Lactic acid, urea, salicylic acid formulations.
- **Retinoids:** Systemic retinoids (acitretin, isotretinoin) used in severe congenital ichthyosiform erythroderma; use must be balanced against growth effects.
- **Dupilumab (IL-4Rα antagonist):** A 2021 case report (ResearchGate/Pediatric Dermatology) described **successful treatment of TTD ichthyosis with dupilumab** in a child. A 2024 case series from Pediatric Dermatology further documented dupilumab benefit for ichthyosis in TTD (Ovid/Pediatric Dermatology, 2024). This represents a potentially important advance, as Th2 cytokine signaling contributes to the barrier defect in TTD-associated ichthyosis.
  - **NCIT:** NCIT:C65216 (Dupilumab) / CHEBI:172716
  - **Therapeutic modality:** MONOCLONAL_ANTIBODY

**Photosensitivity (PS-TTD):**
- **Broad-spectrum high-SPF sunscreen** (SPF ≥50): Essential in PS-TTD.
- **Protective clothing and UV-blocking eyewear.**
- **Vitamin D supplementation:** Required when sun avoidance is strict (HP:0100512 vitamin D deficiency risk).
  - **MAXO:** MAXO:0000950 (supportive care), MAXO:0000088 (dietary intervention)

**Infection management:**
- Prophylactic antibiotics (e.g., co-trimoxazole) considered for recurrent bacterial infections.
- Prompt empirical antibiotic therapy for febrile illness.
- Immunization according to schedule (standard vaccines); no live vaccines if immunocompromise is confirmed.
  - **MAXO:** MAXO:0001017 (vaccination), MAXO:0000950 (supportive care)

**Cataracts:**
- Surgical removal followed by optical correction (glasses or contact lenses).
  - **MAXO:** MAXO:0000004 (surgical procedure)

**Anemia / beta-thalassemia:**
- Monitoring of hemoglobin; iron supplementation if deficient; transfusion in severe anemia.

### Rehabilitative and Supportive Care

- **Early intervention programs** for developmental delay.
- **Special education** for intellectual disability.
- **Physical therapy** for ataxia and motor deficits. (**MAXO:** MAXO:0000011)
- **Occupational therapy** for activities of daily living.
- **Speech therapy** for communication difficulties.
- **Hearing aids** for sensorineural hearing loss.
- **Nutritional support:** Nasogastric or gastrostomy feeding in severe cases with growth failure (PMID: 25396826).

### Experimental and Emerging Therapies

No disease-modifying therapies currently approved. Research directions include:
- **TFIIH stabilization strategies:** Molecular chaperones or small molecules that could stabilize mutant TFIIH complexes (preclinical).
- **Ribosome biogenesis modulation:** Targeting the ribosomal dysfunction arm.
- **Thyroid hormone supplementation:** Small study in TTD mice showed partial correction of myelin abnormalities with T3; no human trials reported.
- **Gene therapy:** Theoretical; ERCC2 gene delivery. No clinical trials active as of 2026.

### No active clinical trials

As of the report date, no interventional clinical trials registered on ClinicalTrials.gov specifically for TTD disease modification were identified. Families are encouraged to consult NCI's Gene Review resources and connect with TTD patient registries.

---

## 13. Prevention

### Primary Prevention

- **Genetic counseling** for families with known TTD mutations; risk is 25% per pregnancy for biallelic autosomal recessive forms.
  - **MAXO:** MAXO:0000079 (genetic counseling)
- **Carrier testing** for at-risk relatives once proband mutations identified.
- **Preimplantation genetic diagnosis (PGD)** for couples who are known carriers.

### Secondary Prevention (Early Detection)

- **Newborn screening:** TTD is not included in standard newborn screening panels in any country. Screening via hair amino acid analysis or molecular testing would be feasible in high-risk families.
- **Prenatal diagnosis:** Available via CVS or amniocentesis when familial mutations are known.
- **Cascade family screening** after proband identification.

### Tertiary Prevention (Preventing Complications)

- **Infection prevention:** Careful vaccination schedule; antibiotic prophylaxis; parental education on early infection recognition.
- **Sun protection education:** Comprehensive UV protection protocols for PS-TTD families.
- **Ophthalmology surveillance:** Annual slit-lamp examination for cataracts.
- **Audiology surveillance:** Annual hearing assessment.
- **Nutritional monitoring:** Regular growth charts; dietetic input.

---

## 14. Other Species / Natural Disease

### Animal Models

TTD does not appear to occur naturally in any non-human species at a population level.

**Mouse models (primary research models):**

1. **XpdTTD/R722W knock-in mice** (De Boer et al., 1998): The most-used mouse model; introduced the human R722W XPD mutation into the murine *Ercc2* locus by gene-cDNA fusion targeting. These mice recapitulate many TTD features:
   - Brittle sulfur-deficient hair
   - Developmental delay and reduced body weight
   - Cachexia and short lifespan
   - Segmental progeroid phenotype (bone density loss, cataracts, immune changes)
   - Dysmyelination (brain MRI and histopathology)
   - Thyroid hormone target gene dysregulation in brain (PMID: 17952069)

2. **XpdTTD/†XPCS compound heterozygous mice**: Viable compound heterozygotes allowing study of allele combinations (PMID: 17183058).

3. **XpdTTD/XpdTTD mice with XPA-null background**: Dramatically accelerated aging phenotype; demonstrates additive NER deficiency effects.

4. **TTDA (Gtf2h5) knockout mice**: Embryonic lethal when homozygous null; heterozygous mice show intermediate phenotypes, confirming TTDA is essential for viability (PMID: 23630104).

**Model limitations:**
- Murine hair is structurally different from human hair; not all hair manifestations translate
- Mouse lifespan differences limit studying adult/aging TTD phenotypes
- The progeroid features in mice may overstate the premature aging component relative to human TTD
- Lissencephalic mouse brain differs from human cortical organization, potentially limiting neurological translational validity (HUMAN_MODEL_MISMATCH concern)

**Drosophila models:**
- XPD (*Haywire*) mutant *Drosophila* have been used to study cell-cycle coordination and XPD's non-repair functions (PMC:4283652).

**Evolutionary conservation:**
- XPD/ERCC2 is conserved from yeast (*Rad3* in *S. cerevisiae*) to humans.
- NER pathway is evolutionarily ancient; core mechanisms conserved across eukaryotes.
- *C. elegans* GTF-2H5/TTDA ortholog (PMID: 34873349) is non-essential for transcription but indispensable for NER, offering a simplified model organism for dissecting these functions.

---

## Key Primary Literature Citations

| PMID | Reference Description |
|---|---|
| PMID:18603627 | Faghri et al. systematic review of 112 TTD cases; phenotype frequencies |
| PMID:17952069 | Neurological defects in TTD reveal TFIIH coactivator function of thyroid hormone (Nature Neuroscience) |
| PMID:11734544 | TFIIH mutations cause beta-thalassemia in TTD patients |
| PMID:10667598 | Cancer-free phenotype in TTD unrelated to repair defect |
| PMID:33909043 | AARS1 and MARS1 protein instability causes NPS-TTD |
| PMID:26996949 | GTF2E2 mutations destabilize TFIIE in NPS-TTD |
| PMID:12820975 | TTD XPD mutations cause transcription defects; XP mutations do not |
| PMID:9182770 | XP and TTD associated with different XPD mutations (PNAS 1997) |
| PMID:15232704 | Quantification of cysteine in TTD hair/nails |
| PMID:30824121 | CARS1 (cysteinyl-tRNA synthetase) mutations cause NPS-TTD |
| PMID:39976384 | ERCC2 variants as uncommon cause of hypomyelinating leukodystrophy (2025) |
| PMC:10377840 | Ribosomal dysfunction as common pathomechanism in TTD (Cells 2023) |
| PMID:21730288 | Slowly progressing NER in TTD-A fibroblasts |
| PMID:25396826 | Growth and nutrition in children with TTD |
| PMID:23630104 | TTDA disruption causes complete NER deficiency and embryonic lethality |
| PMID:40918647 | Anti-tumorigenic properties of TTD mutations in melanocytic cells (2025) |

---

## Summary Table: Key Facts for Knowledge Base Entry

| Category | Key Facts |
|---|---|
| MONDO | MONDO:0018053 |
| OMIM | #601675 (TTD1/PS), #616390 (TTD2/PS), #616395 (TTD3/PS), #234050 (TTD4/NPS) |
| Inheritance | Autosomal recessive (most); X-linked (RNF113A) |
| Incidence | ~1/1,000,000 live births |
| Causal genes | ERCC2, ERCC3, GTF2H5, MPLKIP, GTF2E2, RNF113A, AARS1, MARS1, CARS1, TARS1 |
| Pathomechanism | TFIIH insufficiency → transcription + NER deficiency; ribosomal dysfunction |
| Hallmark feature | Brittle sulfur-deficient hair with tiger-tail polarized microscopy banding |
| Photosensitivity | ~50% of cases (PS-TTD); NO cancer predisposition |
| Mortality | 20-fold elevated in children; median age at death 3 years; primarily infections |
| Key treatment | Supportive; emollients, sun protection, infection management; dupilumab (emerging) |
| No cancer predisposition | Critical clinical distinction from XP |

---

Sources:
- [OMIM #601675 — TTD1, Photosensitive](https://omim.org/entry/601675)
- [OMIM #234050 — TTD4, Nonphotosensitive](https://omim.org/entry/234050)
- [OMIM #616390 — TTD2, Photosensitive](https://omim.org/entry/616390)
- [OMIM #616395 — TTD3, Photosensitive](https://omim.org/entry/616395)
- [PMC3459585 — Systematic review of 112 TTD cases](https://pmc.ncbi.nlm.nih.gov/articles/PMC3459585/)
- [PMC10377840 — Ribosomal dysfunction as common pathomechanism in TTD (2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10377840/)
- [PMC11840839 — ERCC2 variants and hypomyelinating leukodystrophy (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11840839/)
- [NCBI Bookshelf NBK6285 — TTD: crosstalk between DNA repair and transcription](https://www.ncbi.nlm.nih.gov/books/NBK6285/)
- [MedlinePlus Genetics — Trichothiodystrophy](https://medlineplus.gov/genetics/condition/trichothiodystrophy/)
- [DermNet NZ — Trichothiodystrophy](https://dermnetnz.org/topics/trichothiodystrophy)
- [NORD — Trichothiodystrophy / IBIDS syndrome](https://rarediseases.org/rare-diseases/ichthyosis-trichothiodystrophy/)
- [GARD — Trichothiodystrophy](https://rarediseases.info.nih.gov/diseases/12109/trichothiodystrophy)
- [GTR — Trichothiodystrophy genetic testing](https://www.ncbi.nlm.nih.gov/gtr/conditions/C1955934/)
- [PNAS — XP and TTD associated with different XPD mutations](https://www.pnas.org/doi/10.1073/pnas.94.16.8658)
- [HMG — AARS1/MARS1 mutations cause TTD](https://academic.oup.com/hmg/article/30/18/1711/6256034)
- [PMC10630875 — MPLKIP maintains DBR1 for lariat debranching (2023)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10630875/)
- [PMC10575343 — Distinct ultrastructural features of TTD hair shafts (2023)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10575343/)
- [Nature Neuroscience — TFIIH coactivator function and TTD neurological defects](https://www.nature.com/articles/nn1990)
- [Cancer Research — Cancer-free phenotype in TTD](https://aacrjournals.org/cancerres/article/60/2/431/506734/)
- [PMC4176511 — Growth and nutrition in TTD children](https://pmc.ncbi.nlm.nih.gov/articles/PMC4176511/)