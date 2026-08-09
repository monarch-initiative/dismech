---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-07-31T22:38:23.503017'
end_time: '2026-07-31T22:54:21.555085'
duration_seconds: 958.05
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: BRPF1-Related Intellectual Disability
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
  web_search_requests: 7
  num_turns: 61
  total_cost_usd: 5.308133499999998
  session_id: 1baf0605-d46c-4f93-b584-18e85168bb10
  stop_reason: end_turn
citation_count: 19
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** BRPF1-Related Intellectual Disability
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **BRPF1-Related Intellectual Disability** covering all of the
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

I have sufficient verified material. Writing the report now.

---

# BRPF1-Related Intellectual Disability (IDDDFP) — Comprehensive Research Report

**Prepared:** 2026-07-31 | **Target for KB entry:** `BRPF1-Related_Intellectual_Disability`

> **Verification note for curators:** Every abstract quote below was transcribed verbatim from the NCBI E-utilities `efetch` output for the stated PMID. Every HPO/MONDO/GO/UBERON identifier suggested was checked against the HPO API (`ontology.jax.org`), OLS4, or UniProt. Where a claim could not be sourced to a citable abstract, it is explicitly flagged as **[not verifiable / gap]** rather than given a citation. Per the DR guardrails in `CLAUDE.md`, treat this document as *leads*: re-run `just fetch-reference PMID:X` and `just validate-references` before committing any snippet.

---

## 1. Disease Information

### 1.1 Overview

BRPF1-Related Intellectual Disability — formally **Intellectual Developmental Disorder with Dysmorphic Facies and Ptosis (IDDDFP)** — is a rare autosomal dominant neurodevelopmental syndrome caused by heterozygous loss-of-function variants in *BRPF1*, a multivalent chromatin-reader/scaffold protein that assembles and activates the KAT6A/KAT6B (MOZ/MORF) lysine acetyltransferase complexes. The disorder is a **chromatinopathy**: haploinsufficiency reduces histone H3 lysine-23 (H3K23) acetylation and propionylation, deregulating developmental transcriptional programs.

The core clinical triad is **developmental delay / mild-to-moderate intellectual disability + prominent speech and language impairment + ptosis/blepharophimosis with characteristic facial dysmorphism**. Relative to other monogenic chromatin-related neurodevelopmental disorders, cognition and adaptive behavior are comparatively preserved, while speech/language involvement is near-universal.

Yan et al. (2017) established the disorder (PMID:27939640):

> "Here, we describe an intellectual disability disorder in ten individuals with inherited or de novo monoallelic BRPF1 mutations. Symptoms include infantile hypotonia, global developmental delay, intellectual disability, expressive language impairment, and facial dysmorphisms. Central nervous system and spinal abnormalities are also seen in some individuals."

> "These data indicate that aberrations in the chromatin regulator gene BRPF1 cause histone H3 acetylation deficiency and a previously unrecognized intellectual disability syndrome." — PMID:27939640

### 1.2 Key identifiers

| Resource | Identifier | Label |
|---|---|---|
| **MONDO** | **MONDO:0015022** | intellectual developmental disorder with dysmorphic facies and ptosis |
| OMIM (phenotype) | **617333** | INTELLECTUAL DEVELOPMENTAL DISORDER WITH DYSMORPHIC FACIES AND PTOSIS; IDDDFP |
| OMIM (gene) | **602410** | BROMODOMAIN- AND PHD FINGER-CONTAINING PROTEIN; BRPF1 |
| Orphanet | **ORPHA:698090** | Ophthalmological abnormalities-facial dysmorphism-intellectual disability syndrome |
| UMLS | C4310617 | — |
| MedGen | 934584 | — |
| HGNC | **HGNC:14255** (`hgnc:14255`) | BRPF1 — bromodomain and PHD finger containing 1 |
| NCBI Gene | 7862 | BRPF1 |
| Ensembl | ENSG00000156983 | BRPF1 |
| UniProt | **P55201** | Peregrin (BRPF1) |
| RefSeq | NM_001003694 (also NM_004634.3 used clinically) | — |
| Cytoband | **3p25.3** | — |
| ICD-10 / ICD-11 | Not assigned a specific code in Orphanet's cross-reference set **[gap]**; typically coded under generic ID / congenital malformation syndrome codes | — |
| MeSH | No specific descriptor **[gap]** | — |

MONDO cross-reference set retrieved from OLS4 (`MONDO:0015022` → OMIM:617333, Orphanet:698090, UMLS:C4310617, MedGen:934584). Orphanet identity confirmed via `api.orphadata.com/rd-cross-referencing/orphacodes/698090`, which reports disorder type **"Malformation syndrome"** and an exact, validated OMIM:617333 mapping.

### 1.3 Synonyms and alternative names

- Intellectual Developmental Disorder with Dysmorphic Facies and Ptosis (**IDDDFP**) — OMIM/MONDO preferred
- **BRPF1-related neurodevelopmental disorder** — Orphanet synonym
- Ophthalmological abnormalities–facial dysmorphism–intellectual disability syndrome — Orphanet preferred term
- BRPF1-related disorder / BRPF1-associated syndrome — literature usage (PMID:38346666; PMID:35243762)
- BRPF1 haploinsufficiency syndrome

> ⚠️ **NEC (Named Entity Confusion) preflight note.** BRPF1 sits in a family of closely related chromatin disorders with overlapping names — KAT6A syndrome (*MONDO* distinct), KAT6B-related Genitopatellar and Say-Barber-Biesecker-Young-Simpson syndromes, and the **3p25.3 microdeletion syndrome** (which spans both *BRPF1* and *SETD5*). It also phenocopies Noonan syndrome (PMID:41137536) and blepharophimosis-ptosis-epicanthus-inversus syndrome (*FOXL2*). Before accepting any deep-research report on this disease, confirm the report's dominant gene is **BRPF1**, and that the OMIM ID is **617333** (not 601358/KAT6A, 603736/KAT6B, or 110100/BPES). Run `uv run runoak -i sqlite:obo:mondo info MONDO:0015022 -O obo`.

### 1.4 Information provenance

Disease-level (aggregated) resources — OMIM, Orphanet, MONDO, ClinGen, HPO annotations — plus **individual-patient case series and cohorts**. There is no EHR-derived or registry-derived cohort for this disorder. The largest single patient-level source is Colson et al. 2025 (PMID:39837771, 29 new patients from 20 families + literature review). Deep-phenotyping sources: PMID:38346666 (15 participants, speech/language) and PMID:38590032 (ophthalmic OCT deep phenotyping).

---

## 2. Etiology

### 2.1 Disease causal factors

**Genetic, monogenic, autosomal dominant.** The sole established cause is **heterozygous loss-of-function of *BRPF1***. The mechanism is **haploinsufficiency** — not gain of function or dominant negative — established by three converging lines of evidence:

1. **Variant spectrum**: the overwhelming majority of pathogenic variants are protein-truncating (nonsense, frameshift, canonical splice) plus whole-gene deletions (PMID:39837771).
2. **ClinGen Dosage Sensitivity curation**: haploinsufficiency score **3 (Sufficient Evidence for Haploinsufficiency)**; triplosensitivity score **0 (No Evidence)**; curated 2023-08-23 against MONDO:0015022 / OMIM:617333 (`CGDS:HGNC_14255`, ClinGen curation CCID:006763). ClinGen's summary: *"Numerous loss-of-function mutations have been reported in intellectual developmental disorder with dysmorphic facies and ptosis (IDDDFP) patients, and functional analyses support a haploinsufficiency of the BRPF1 gene."*
3. **Functional assays**: patient variants impair H3K23 acetylation (PMID:27939640) and H3K23 propionylation (PMID:32010779), and *Brpf1* heterozygous mice recapitulate the cognitive phenotype (PMID:31213987).

ClinGen also records a Gene-Disease Validity classification for BRPF1; GenCC aggregates it as **Definitive/Strong**.

### 2.2 Risk factors

**Genetic risk factors (causal):**
- **De novo heterozygous *BRPF1* LoF variants** — the majority of cases.
- **Inherited variants from a mildly affected parent** — well documented; five of 20 families in the 2025 cohort showed two-generation transmission (PMID:39837771). Multiplex families are reported: a 5-member family with c.1052_1053del (PMID:27939639) and a 4-member family with c.556C>T p.Q186* (PMID:31020800).
- **Contiguous 3p25.3 deletions** encompassing *BRPF1* (± *SETD5*) — see §4.6.

**Environmental risk factors:** **None identified.** This is a fully penetrant-mechanism Mendelian chromatinopathy with no reported environmental, occupational, toxin, infectious, dietary, parental-age, or lifestyle risk contribution. Advanced paternal age is a generic risk factor for de novo point mutations across all dominant disorders, but has **not** been specifically studied in BRPF1 **[gap]**.

**Sex:** Male predominance is observed in reported series (e.g. 10/15 male in PMID:38346666), but this is likely ascertainment bias, not a biological sex effect. No sex-linked mechanism exists (autosomal gene) **[interpretive; not directly asserted in any abstract]**.

### 2.3 Protective factors

**No genetic or environmental protective factors are established.** Notably, however, there is documented **variable expressivity extending to normal cognition** — PMID:35243762 reports "a patient with normal intellectual development who had congenital ptosis, hypotonia, muscular weakness, atlanto-axial malformation, and pyramidal at the neurological examination," carrying "a rare nonsense variant on exon 3 of BRPF1 gene." The genetic or environmental modifiers underlying this preservation are unknown **[gap — high-value research question]**.

A *therapeutic* (not protective-in-the-epidemiologic-sense) lead exists: short-chain fatty acids and HDAC inhibitors boost the deficient mark — see §12.

### 2.4 Gene–environment interactions

**None described.** No GxE studies exist for BRPF1. A mechanistically plausible but entirely untested hypothesis is that dietary short-chain fatty acid (propionate/butyrate) availability could modulate residual H3K23 acylation, given PMID:32010779's finding that "Valproate, vorinostat, propionate and butyrate promote H3K23 acylation." **[hypothesis only — no human or animal GxE data]**

---

## 3. Phenotypes

### 3.1 Frequency table — the primary evidence base

The best frequency source is **Colson et al. 2025 (PMID:39837771)**, which reports 29 new patients (20 families) *and* a literature comparison cohort (~50 previously published cases). Frequencies differ substantially between the two — the newer prospectively phenotyped cohort shows *lower* rates of ID, speech delay, motor delay, microcephaly, short stature, and feeding difficulty, consistent with **ascertainment bias in earlier case reports toward more severely affected individuals**. Curators should record both and prefer the combined view.

| Phenotype | New cohort (2025) | Literature cohort | Suggested HPO term | Suggested `FrequencyEnum` |
|---|---|---|---|---|
| **Speech / language delay** | 13/28 (46%) | **41/50 (82%)** | HP:0000750 Delayed speech and language development | VERY_FREQUENT |
| **Global developmental delay** | — | 10/10 (HPOA) | HP:0001263 Global developmental delay | VERY_FREQUENT |
| **Motor delay** | 15/29 (52%) | 39/49 (80%) | HP:0002194 Delayed gross motor development | FREQUENT |
| **Intellectual disability** | 16/29 (55%); mild 6/16, moderate 10/16 | 35/49 (71%) | HP:0001249 Intellectual disability | FREQUENT |
| **Ptosis** | **20/29 (69%)** | 6/10 (HPOA) | HP:0000508 Ptosis | FREQUENT |
| **Behavioural disorder (any)** | 18/29 (62%) | — | HP:0000708 Behavioral abnormality | FREQUENT |
| Round face | 17/27 (63%) | 7/10 (HPOA) | HP:0000311 Round face | FREQUENT |
| Bulbous nose | 14/28 (50%) | — | HP:0000414 Bulbous nose | FREQUENT |
| Wide/broad nasal bridge | — | 9/10 (HPOA) | HP:0000431 Wide nasal bridge | VERY_FREQUENT |
| Hypertelorism | 14/29 (48%) | 9/10 (HPOA) | HP:0000316 Hypertelorism | FREQUENT |
| Strabismus | 13/27 (48%) | 2/10 (HPOA) | HP:0000486 Strabismus | FREQUENT |
| High palate | 14/29 (48%) | — | HP:0000218 High palate | FREQUENT |
| Hypotonia | 11/29 (40%) | 7/8 (HPOA) | HP:0001252 Hypotonia | FREQUENT |
| Epicanthus | 12/29 (41%) | — | HP:0000286 Epicanthus | FREQUENT |
| Retrognathia | 12/29 (41%) | — | HP:0000278 Retrognathia | FREQUENT |
| Hair abnormality (any) | 12/29 (41%) *[novel]* | — | HP:0001595 Abnormal hair morphology | FREQUENT |
| Synophrys | 10/28 (36%) *[novel]* | — | HP:0000664 Synophrys | FREQUENT |
| **Blepharophimosis** | 10/29 (34%) | 4/8 (HPOA) | HP:0000581 Blepharophimosis | FREQUENT |
| ADHD | 9/27 (33%) | — | HP:0007018 Attention deficit hyperactivity disorder | FREQUENT |
| Gastroesophageal reflux | 9/29 (31%) | — | HP:0002020 Gastroesophageal reflux | FREQUENT |
| Sleep disturbance | 9/29 (31%) | — | HP:0002360 Sleep disturbance | FREQUENT |
| Hypertrichosis | 9/29 (31%) *[novel]* | — | HP:0000998 Hypertrichosis | FREQUENT |
| Low hanging columella | 9/29 (31%) *[novel]* | — | HP:0009765 Low hanging columella | FREQUENT |
| Clinodactyly of 5th finger | 8/27 (30%) | — | HP:0004209 Clinodactyly of the 5th finger | FREQUENT |
| Low frustration tolerance | 8/28 (29%) | — | HP:0000722 Obsessive-compulsive behavior *(no exact term — use free-text)* | FREQUENT |
| **Palpebral edema** | 8/29 (28%) *[novel]* | — | HP:0100540 Palpebral edema | OCCASIONAL |
| Laterally extended eyebrows | 8/29 (28%) *[novel]* | — | HP:0011230 Laterally extended eyebrow | OCCASIONAL |
| Distal joint laxity | 7/27 (26%) | 6/10 joint hypermobility (HPOA) | HP:0001388 Joint laxity / HP:0001382 Joint hypermobility | OCCASIONAL |
| Refractive error | 7/29 (24%) — myopia 5/29 (17%), hypermetropia 2/29 (7%) | — | HP:0000539 Abnormality of refraction; HP:0000545 Myopia; HP:0000540 Hypermetropia | OCCASIONAL |
| Prominent fingertip pads | 6/27 (22%) | — | HP:0001212 Prominent fingertip pads | OCCASIONAL |
| Anxiety | 6/29 (21%) | — | HP:0000739 Anxiety | OCCASIONAL |
| **Short stature** | 6/29 (21%) | 17/42 (40%) | HP:0004322 Short stature | OCCASIONAL–FREQUENT |
| Cryptorchidism | 5/27 (19%) *[not previously reported]* | — | HP:0000028 Cryptorchidism | OCCASIONAL |
| Epicanthus inversus | 5/29 (17%) | — | HP:0000537 Epicanthus inversus | OCCASIONAL |
| Small hands | 4/23 (17%) | — | HP:0200055 Small hand | OCCASIONAL |
| **Autistic behavior** | 4/26 (15%) | — | HP:0000729 Autistic behavior | OCCASIONAL |
| Broad hallux | 4/27 (15%) | — | HP:0010055 Broad hallux | OCCASIONAL |
| **Seizures** | 4/29 (14%) | 5/10 (HPOA) | HP:0001250 Seizure | OCCASIONAL–FREQUENT |
| Obesity | 4/28 (14%) | — | HP:0001513 Obesity | OCCASIONAL |
| Constipation | 4/29 (14%) | — | HP:0002019 Constipation | OCCASIONAL |
| Recurrent infections | 4/28 (14%) | — | HP:0002719 Recurrent infections | OCCASIONAL |
| Inappropriate laughter | 4/25 (14%) | — | HP:0000748 Inappropriate laughter | OCCASIONAL |
| **Feeding difficulties** | 3/26 (12%) | **24/42 (57%)** | HP:0011968 Feeding difficulties | OCCASIONAL–FREQUENT |
| **Agenesis of corpus callosum** | 2/17 with MRI (12%) | 1/7 thin CC (HPOA) | HP:0001274 Agenesis of corpus callosum; HP:0033725 Thin corpus callosum | OCCASIONAL |
| Facial asymmetry | 3/28 (11%) | — | HP:0000324 Facial asymmetry | OCCASIONAL |
| Amblyopia | 3/29 (10%) | — | HP:0000646 Amblyopia | OCCASIONAL |
| Hematologic abnormality (anemia, thrombocytopenia) | 2/25 (8%) | — | HP:0001903 Anemia; HP:0001873 Thrombocytopenia | OCCASIONAL |
| **Microcephaly** | 2/29 (7%) | **14/52 (27%)** | HP:0000252 Microcephaly | OCCASIONAL |
| Nystagmus | 2/29 (7%) | — | HP:0000639 Nystagmus | OCCASIONAL |
| Laryngomalacia | 2/28 (7%) | — | HP:0001601 Laryngomalacia | OCCASIONAL |
| White matter hyperintensities | 1/17 (6%) | 1/7 (HPOA) | HP:0030890 Hyperintensity of cerebral white matter on MRI | OCCASIONAL |
| Cardiac defect | 1/25 (4%) | subset (PMID:32010779) | HP:0001627 Abnormal heart morphology | OCCASIONAL |

**HPOA-only features (from `ontology.jax.org/api/network/annotation/OMIM:617333`, derived from the original OMIM curation, not in the 2025 cohort):**

| HPO ID | Term | HPOA frequency |
|---|---|---|
| HP:0001762 | Talipes equinovarus | 10/20 |
| HP:0000343 | Long philtrum | 10/20 |
| HP:0012368 | Flat face | 7/9 |
| HP:0010862 | Delayed fine motor development | 6/8 |
| HP:0031936 | Delayed ability to walk | 5/9 |
| HP:0004602 | Cervical C2/C3 vertebral fusion | 3/10 |
| HP:0000322 | Short philtrum | 3/10 |
| HP:0000337 | Broad forehead | 3/10 |
| HP:0000160 | Narrow mouth | 3/10 |
| HP:0000494 | Downslanted palpebral fissures | 4/10 |
| HP:0034295 | Reduced cerebral white matter volume | 2/10 |
| HP:0000369 | Low-set ears | 2/10 |
| HP:0001511 | Intrauterine growth retardation | 2/20 |
| HP:0002714 | Downturned corners of mouth | 1/10 |
| HP:0000154 | Wide mouth | 1/10 |
| HP:0012385 | Camptodactyly | (no frequency) |
| HP:0001510 | Growth delay | Occasional |
| HP:0003577 / HP:0003623 | Congenital onset / Neonatal onset | 10/10 / 4/4 |

### 3.2 Speech and language — the most consistent domain

PMID:38346666 provides the only systematic speech/language characterization (15 participants, median age 7y4m, 14 distinct variants):

> "Language disorders were common (11/12), and most had mild to moderate deficits across receptive, expressive, written, and social-pragmatic domains. Speech disorders were frequent (7/9), including phonological delay (6/9) and disorder (3/9), and childhood apraxia of speech (3/9). All those tested for cognitive abilities had a FSIQ ≥70 (4/4). Participants had vision impairment (13/15), fine (8/15) and gross motor delay (10/15) which often resolved in later childhood, infant feeding impairment (8/15), and infant hypotonia (9/15)."

> "We have implicated BRPF1-related disorder as causative for speech and language disorder, including childhood apraxia of speech. Adaptive behavior and cognition were strengths when compared to other monogenic neurodevelopmental chromatin-related disorders. The universal involvement of speech and language impairment is noteable, relative to the high degree of phenotypic variability in BRPF1-related disorder." — PMID:38346666

Suggested HPO terms: HP:0000750 Delayed speech and language development; **HP:0011098 Speech apraxia** (childhood apraxia of speech; verified label is "Speech apraxia"); HP:0002465 Poor speech.

Two curation-relevant nuances from this paper:
- **Vision impairment 13/15 (87%)** — the highest ocular frequency in any series.
- **Motor delay is often transient** ("which often resolved in later childhood") — argues for `clinical_course` annotation rather than `PROGRESSIVE`.

### 3.3 Ophthalmological phenotype — the syndrome's signature

Ocular involvement is the defining feature and is why Orphanet names the syndrome "Ophthalmological abnormalities–facial dysmorphism–intellectual disability syndrome." Mattioli et al. established that this arm is **specifically BRPF1-driven** within the 3p25 contiguous deletion:

> "We conclude that both genes contribute to the phenotypic severity of 3p25 deletion syndrome but that some specific features, such as ptosis and blepharophimosis, are mostly driven by BRPF1 haploinsufficiency." — PMID:27939639

An important 2024 expansion added **subclinical optic neuropathy**, detectable only on OCT (PMID:38590032):

> "Interestingly, P1 had a Chiari Malformation type I and a subclinical optic neuropathy, which could not be explained by variations in other genes. Having detected a peculiar ocular phenotype in P1, we suggested optical coherence tomography (OCT) for P2; such an exam also detected bilateral subclinical optic neuropathy in this case. To date, only a few patients with BRPF1 variants have been described, and none were reported to have optic neuropathy. Since subclinical optic nerve alterations can go easily undetected, our experience highlights the importance of a more detailed ophthalmologic evaluation in patients with BRPF1 variant."

Additional HPO terms: HP:0001098 Abnormal fundus morphology / HP:0000648 Optic atrophy (for optic neuropathy — no exact "subclinical optic neuropathy" term exists; use a more specific `preferred_term` per the dismech convention); **HP:0007099 Chiari type I malformation**.

### 3.4 Phenotype characteristics (onset, severity, progression)

- **Age of onset:** Congenital / neonatal — HPOA records **HP:0003577 Congenital onset 10/10** and **HP:0003623 Neonatal onset 4/4**. Ptosis is congenital (PMID:35243762). Hypotonia and feeding difficulty present in infancy (PMID:38346666).
- **Severity:** Predominantly **mild to moderate**. PMID:39837771: *"Neuropsychological assessment reveals a predominance of mild to moderate ID, with cognitive profiles showing variability in verbal and visual processing."* In the 2025 cohort, of 16 with ID, 6 were mild and 10 moderate — **no severe/profound ID reported**. PMID:38346666: FSIQ ≥70 in all 4 formally tested.
- **Progression:** **Non-progressive / static**. This is a developmental (neurodevelopmental) disorder, not a neurodegenerative one. Motor delay frequently **improves** ("often resolved in later childhood," PMID:38346666). No abstract reports regression or neurodegeneration. Curate as `clinical_course: STABLE` for the neurological phenotype, not `PROGRESSIVE`.
- **Variable expressivity:** Marked, including *intrafamilial*. PMID:39837771: *"Among the five families reported here, phenotypic differences were observed between family members carrying the same pathogenic variant, affecting intellectual ability, dysmorphic features and malformations, suggesting an intrafamilial variability."* At the extreme, PMID:35243762 reports normal intellect with isolated congenital ptosis and neurological signs.

### 3.5 Quality of life impact

**No disease-specific QoL instrument, EQ-5D, SF-36, or PROMIS data exist for BRPF1-related disorder [gap].** Per-phenotype functional impact can be inferred:

- **Speech/language disorder + childhood apraxia of speech** — the dominant functional burden; drives communication, literacy ("written" domain affected), and social-pragmatic participation (PMID:38346666).
- **Ptosis/blepharophimosis** — visual-axis obstruction risk, amblyopia (3/29), plus cosmetic/psychosocial impact; surgically correctable.
- **Vision impairment (13/15)** — affects learning and mobility.
- **Behavioral phenotype** (62% any; ADHD 33%, anxiety 21%, sleep disturbance 31%) — significant caregiver burden.
- **Adaptive behavior is a relative strength** — PMID:38346666: *"Adaptive behavior and cognition were strengths when compared to other monogenic neurodevelopmental chromatin-related disorders."* This is an important positive prognostic message.

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene

**BRPF1** (bromodomain and PHD finger containing 1), `hgnc:14255`, **3p25.3**, OMIM *602410*, Ensembl ENSG00000156983, NCBI Gene 7862. Protein: **Peregrin, UniProt P55201, 1,214 aa, ~137.5 kDa**. Clinical transcript commonly **NM_004634.3**; also NM_001003694 (RefSeq Select). Note the literature also uses ENST00000383829.

**Domain architecture** (UniProt P55201, verified):

| Feature | Positions |
|---|---|
| C2H2-type zinc finger | 21–47 |
| **PHD-type zinc finger 1** | 273–323 |
| C2HC pre-PHD-type zinc finger | 327–360 |
| **PHD-type zinc finger 2** | 384–448 |
| **Bromodomain** | 628–732 |
| **PWWP domain** | 1,085–1,168 |

PMID:27939640 describes this as "a multivalent chromatin regulator possessing three histone-binding domains, one non-specific DNA-binding module, and several motifs for interacting with and activating three lysine acetyltransferases."

### 4.2 Pathogenic variants — spectrum

**Classification & mechanism:** Pathogenic/likely pathogenic per ACMG/AMP, mechanism **loss of function / haploinsufficiency** (ClinGen HI score 3).

**Variant types.** From the 29-patient / 17-unique-variant 2025 cohort (PMID:39837771):

| Type | Count | Examples (protein) |
|---|---|---|
| Frameshift | 7 | p.(Asp190MetfsTer14), p.(Ala396LeufsTer69), p.(Ser660ArgfsTer2), p.(Arg593AlafsTer5), p.(Leu779CysfsTer14), p.(Tyr387LeufsTer79), p.(Lys820ArgfsTer2) |
| Nonsense | 4 | p.(Gln302Ter), p.(Ser1007Ter), p.(Arg251Ter), p.(Gln645Ter) |
| Missense | 2 | p.(Cys23Arg), p.(Arg548Trp) — both at conserved residues |
| Canonical splice | 2 | c.599+1G>T, c.2311+1G>A |
| Whole-gene deletion | 2 | — |

**Landmark individual variants (well-documented, good for KB evidence anchors):**

| Variant | Consequence | Context | PMID |
|---|---|---|---|
| c.1052_1053del | p.Val351Glyfs*8 | 5 affected members, large AD family; index variant of Mattioli et al. | 27939639 |
| c.556C>T | p.Gln186* (p.Q186*) | 4 affected members, multiplex Jewish family | 31020800 |
| c.1433G>A | p.Trp478* (p.W478*), exon 3 | First Turkish family; anemia + thrombocytopenia | 37190896 |
| c.1054G>C | p.Val352Leu, exon 3 | Novel missense, Saudi family; absent in 100 ethnically matched controls | 32457794 |

**Original series composition:** Yan et al. reported 10 individuals from 9 unrelated families with 1 missense, 3 nonsense, and 6 frameshift variants; Mattioli et al. reported the index family plus "BRPF1 deletions or point mutations in six additional individuals with a similar phenotype" (PMID:27939639). Yan et al. 2020 added "BRPF1 variants in 12 previously unidentified cases of syndromic intellectual disability" (PMID:32010779).

**Total reported cases:** Orphanet's epidemiology record cites **79 cases (worldwide, validated, "Cases/families")**. PMID:39837771 adds 29 new patients on top of "over 50 previously published cases."

**Somatic vs germline:** IDDDFP variants are **germline** (de novo or inherited). BRPF1 also carries **somatic** mutations in cancer — "the BRPF1 gene is mutated in childhood leukemia and adult medulloblastoma" (PMID:25920810) — and *"H3K23 acylation is also impaired by cancer-derived somatic BRPF1 mutations"* (PMID:32010779). These are mechanistically related but a distinct disease context; do not conflate them in the disorder entry.

### 4.3 Population allele frequency and constraint

- **gnomAD constraint:** BRPF1 is highly LoF-constrained — **pLI = 1**, **LOEUF ≈ 0.21**. *(Retrieved via web search; the gnomAD GraphQL endpoint requires POST and could not be queried directly. **Curators should re-verify the exact pLI/LOEUF/o-e values against gnomAD v4 before citing.**)*
- **DECIPHER Haploinsufficiency Index (%HI): 15.78** (lower = more haploinsufficient), per the ClinGen gene page.
- Pathogenic BRPF1 LoF variants are **absent or vanishingly rare** in gnomAD — consistent with pLI 1. PMID:32457794 independently excluded their missense variant in 100 ethnically matched controls by Sanger sequencing.
- **ClinVar:** 577 total submitted BRPF1 variant records; 269 with a pathogenic or likely pathogenic clinical significance assertion (NCBI E-utilities `esearch db=clinvar`, retrieved 2026-07-31). *Note: the P/LP count includes multi-gene CNV records overlapping BRPF1, so it overstates the number of BRPF1-specific sequence-level P/LP variants — do not quote it as "269 pathogenic BRPF1 variants."*

### 4.4 Functional consequences

- **Loss of function** is the established mechanism. For the index frameshift, PMID:27939639 found: *"The mRNA transcript was not significantly reduced in affected fibroblasts and most likely produces a truncated protein (p.Val351Glyfs*8). The protein variant shows an aberrant cellular location, loss of certain protein interactions, and decreased histone H3K23 acetylation."* — i.e. the truncated protein **escapes nonsense-mediated decay** but is functionally null/mislocalized.
- **Molecular readouts of pathogenicity:** reduced **H3K23 acetylation** (PMID:27939640; PMID:27939639) and reduced **H3K23 propionylation** (PMID:32010779). Both are usable as functional assays.
- **Mislocalization**: nuclear localization of BRPF1 depends on KAT6A, ING5, and MEAF6 (UniProt P55201); truncating variants that remove interaction motifs mislocalize.

### 4.5 Modifier genes

**No validated modifier genes.** The strongest candidate is the neighboring **SETD5** in contiguous deletions (§4.6) — a *contiguous-gene* effect rather than a true modifier. Intrafamilial variability with an identical variant (PMID:39837771) implies unidentified genetic and/or stochastic modifiers **[gap — explicit open question]**.

### 4.6 Chromosomal abnormalities — the 3p25 / 3p25.3 deletion connection

*BRPF1* lies within the **3p25 deletion syndrome** region, adjacent to *SETD5*. Mattioli et al. dissected the contributions (PMID:27939639):

> "Deletions of the 3p25 region, containing BRPF1 and SETD5, cause a defined ID syndrome where most of the clinical features are attributed to SETD5 deficiency. We compared the clinical symptoms of individuals carrying mutations or small deletions of BRPF1 alone or SETD5 alone with those of individuals with deletions encompassing both BRPF1 and SETD5. We conclude that both genes contribute to the phenotypic severity of 3p25 deletion syndrome but that some specific features, such as ptosis and blepharophimosis, are mostly driven by BRPF1 haploinsufficiency."

This is a strong candidate for a **dismech `Grouping` or comorbidity/contiguous-gene entry** — it is a clean worked example of dissecting a contiguous-gene syndrome into per-gene phenotype attribution.

Whole-gene BRPF1 deletions were also recovered from exome CNV analysis in a dystonia cohort (PMID:33611074) — *"Within the deletion intervals, BRPF1, CHD8, DJ1, EFTUD2, FGF14, GCH1, PANK2, SGCE, UBE3A, VPS16, WARS2, and WDR45 were determined as the most clinically relevant genes"* — indicating BRPF1 CNVs are detectable by exome read-depth analysis (ExomeDepth).

### 4.7 Epigenetic information

BRPF1 is itself an epigenetic regulator; the disease *is* an epigenetic lesion (see §6). Two curation-relevant points:

- **Histone acylation marks affected:** H3K23ac and H3K23pr (propionylation). PMID:32010779 reports the propionylation discovery: *"We report that these complexes also catalyze H3K23 propionylation in vitro and in vivo. Immunofluorescence microscopy and ATAC-See revealed the association of this modification with active chromatin."*
- **DNA methylation episignature:** Distinct EpiSign episignatures are established for **KAT6A** and for the two **KAT6B** disorders (PMID:37249002). **A BRPF1-specific DNA methylation episignature has not been reported [gap].** Given BRPF1's obligate partnership with KAT6A/KAT6B, testing whether BRPF1 patients carry a shared or distinct episignature is a high-value, tractable research question — and would be diagnostically useful for VUS resolution. **Do not curate a BRPF1 episignature as if it exists.**

---

## 5. Environmental Information

- **Environmental factors:** None. No toxin, radiation, pollution, or occupational exposure is implicated.
- **Lifestyle factors:** None implicated in causation. (Diet is relevant only as a speculative therapeutic lever — §12.)
- **Infectious agents:** None. Not applicable.

Recurrent infections were noted in 4/28 (14%) of the 2025 cohort (PMID:39837771), but these are a **consequence** of the disorder (possibly related to the hematopoietic/immune arm), not an etiologic environmental factor.

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (upstream → downstream)

```
[MOLECULAR] Heterozygous BRPF1 loss-of-function variant (3p25.3)
        ↓
[MOLECULAR] BRPF1 haploinsufficiency — reduced scaffold available to assemble
            KAT6A/KAT6B(/KAT7)–BRPF1–ING4/5–MEAF6 tetrameric HAT complexes
        ↓
[MOLECULAR] Impaired complex assembly, substrate targeting, and enzymatic
            stimulation; mislocalization of truncated protein
        ↓
[MOLECULAR] Deficient histone H3K23 acetylation AND H3K23 propionylation
            at active chromatin / transcription start sites
        ↓
[CELLULAR] Deregulated transcription of developmental programs
           (Hox cluster, Robo3, Otx1, Pitx2, Hmx1, Pax6, Runx1/2,
            multipotency genes Slamf1/Mecom/Hoxa9/Hlf/Gfi1/Egr/Gata3)
        ↓
   ┌───────────────────────┬──────────────────────┬─────────────────────┐
   ↓                       ↓                      ↓                     ↓
[CELLULAR]            [CELLULAR]             [CELLULAR]           [CELLULAR]
Reduced Tbr2+          Reduced dendritic      Impaired GABAergic   Impaired HSC/
intermediate           arborization &         interneuron          progenitor
neuronal progenitors;  spine density;         excitability         self-renewal;
aberrant neurogenesis  altered spine/synapse  (↑ firing threshold, ↑ROS, senescence,
                       morphology             ↓ mIPSC amplitude)   apoptosis
   ↓                       ↓                      ↓                     ↓
[TISSUE] Neocortical   [TISSUE] ↓ excitatory  [TISSUE] E/I         [TISSUE] Marrow
abnormality; partial   synaptic transmission  imbalance in         hypoplasia
callosal agenesis      (↓ mEPSC freq & amp)   cortex/hippocampus   (mouse KO)
   ↓                       ↓                      ↓                     ↓
   └───────────────────────┴──────────────────────┘                     ↓
                           ↓                                            ↓
[ORGANISM] Intellectual disability, speech/language              [ORGANISM] Anemia,
disorder, hypotonia, seizures, behavioral phenotype               thrombocytopenia
                                                                  (rare in humans)

  ‖ parallel developmental arm ‖
[CELLULAR] Deregulated Pitx2/Hmx1/Pax6 in ocular/craniofacial primordia
        ↓
[TISSUE] Abnormal periocular and craniofacial morphogenesis
        ↓
[ORGANISM] Ptosis, blepharophimosis, strabismus, optic neuropathy,
           characteristic facial dysmorphism
```

### 6.2 Molecular pathways

**Primary pathway: MOZ/MORF (KAT6A/KAT6B) histone acetyltransferase complex — lysine acetylation and acylation of histone H3.**

BRPF1 is the obligate scaffold. PMID:36077605:

> "It functions in the form of a tetrameric complex with a monocytic leukemia zinc finger protein (MOZ or KAT6A), MOZ-related factor (MORF or KAT6B) or HAT bound to ORC1 (HBO1 or KAT7) and two small non-catalytic proteins, the inhibitor of growth 5 (ING5) or the paralog ING4 and MYST/Esa1-associated factor 6 (MEAF6)."

BRPF1's four functions within the complex (PMID:24646517):

> "Within these complexes, BRPF1 serves as a scaffold for bridging subunit interaction, stimulating acetyltransferase activity, governing substrate specificity and stimulating gene expression."

**Trithorax-group / Hox maintenance pathway.** From zebrafish (PMID:18469222):

> "brpf1 mutants display anterior transformations of pharyngeal arches due to progressive loss of anterior Hox gene expression. Brpf1 functions in association with the histone acetyltransferase Moz (Myst3), an interaction mediated by the N-terminal domain of Brpf1, and promotes histone acetylation in vivo. Brpf1 recruits Moz to distinct sites of active chromatin and remains at chromosomes during mitosis, mediated by direct histone binding of its bromodomain, which has a preference for acetylated histones, and its PWWP domain, which binds histones independently of their acetylation status. This is the first demonstration of histone binding for PWWP domains."

**Emerging: 3D genome / loop-extrusion interplay.** A 2025 bioRxiv CRISPR screen implicates the MORF complex including Brpf1 in antagonizing CTCF/cohesin insulation (PMID:40060486): *"Among them were the MORF acetyltransferase complex members (Kat6b, Ing5, Brpf1), which could antagonize the transcriptional insulation mediated by CTCF and cohesin complex at developmental genes."* **[preprint; not peer-reviewed — mark as EMERGING hypothesis if curated]**

**Suggested GO terms (biological process):**

| GO ID | Label | Modifier |
|---|---|---|
| GO:0016573 | histone acetylation | DECREASED |
| GO:0043966 | histone H3 acetylation | DECREASED |
| GO:0006355 | regulation of DNA-templated transcription | ABNORMAL |
| GO:0045893 | positive regulation of DNA-templated transcription | DECREASED |
| GO:0007399 | nervous system development | ABNORMAL |
| GO:0021895 | cerebral cortex neuron differentiation | DECREASED |
| GO:0048813 | dendrite morphogenesis | DECREASED |
| GO:0060996 | dendritic spine development | DECREASED |
| GO:0007268 / GO:0060079 | chemical synaptic transmission / excitatory postsynaptic potential | DECREASED |
| GO:0060080 | inhibitory postsynaptic potential | DECREASED |
| GO:0030097 | hemopoiesis | DECREASED |
| GO:0001525 | angiogenesis (vascular defects in KO) | ABNORMAL |
| GO:0001843 | neural tube closure | ABNORMAL |

**Suggested GO molecular function terms (UniProt P55201, verified):** GO:0010698 acetyltransferase activator activity; GO:0140566 histone reader activity; GO:0003677 DNA binding.

**Suggested GO cellular component terms (verified):** **GO:0070776 MOZ/MORF histone acetyltransferase complex** (the most specific and informative), GO:0000123 histone acetyltransferase complex, GO:0005634 nucleus.

### 6.3 Cellular processes

**Neurodevelopmental (cortex/hippocampus).** Forebrain-conditional KO (PMID:25568313):

> "Here, we report that forebrain-specific inactivation of the mouse Brpf1 gene caused early postnatal lethality, neocortical abnormalities, and partial callosal agenesis. With respect to the control, the mutant forebrain contained fewer Tbr2-positive intermediate neuronal progenitors and displayed aberrant neurogenesis. Molecularly, Brpf1 loss led to decreased transcription of multiple genes, such as Robo3 and Otx1, important for neocortical development. Surprisingly, elevated expression of different Hox genes and various other transcription factors, such as Lhx4, Foxa1, Tbx5, and Twist1, was also observed. These results thus identify an important role of Brpf1 in regulating forebrain development and suggest that it acts as both an activator and a silencer of gene expression in vivo."

**Synaptic / dendritic (the haploinsufficiency-specific model — most disease-relevant).** PMID:31213987:

> "Brpf1 heterozygotes showed reduced dendritic complexity in both hippocampal granule cells and cortical pyramidal neurons, accompanied by reduced spine density and altered spine and synapse morphology. An in vitro study of Brpf1 haploinsufficiency also demonstrated decreased frequency and amplitude of miniature EPSCs that may subsequently contribute to abnormal behaviors, including decreased anxiety levels and defective learning and memory."

**Excitatory transmission (hippocampus).** PMID:34485298:

> "We found that mild knockdown of Brpf1 reduced mEPSC frequency of cultured hippocampal neurons, before any significant changes of dendritic morphology showed. We also found that Brpf1 mild knockdown in the hippocampus showed a decreasing trend on the spatial learning and memory ability of mice. Finally, mRNA-Seq analyses showed that genes related to learning, memory, and synaptic transmission (such as C1ql1, Gpr17, Htr1d, Glra1, Cxcl10, and Grin2a) were dysregulated upon Brpf1 knockdown."

**Inhibitory transmission (GABAergic interneurons) — E/I imbalance.** PMID:33744924:

> "Moreover, increased firing threshold, decreased number of evoked action potentials, and a reduced amplitude of miniature inhibitory postsynaptic currents were observed before any significant change of MAP2+ dendritic morphology and in vivo migration ability appeared. Finally, mRNA-Seq analysis revealed that genes related to neurodevelopment and synaptic transmission such as Map2k7 were dysregulated. Our results demonstrated a key role of Brpf1 in inhibitory neurotransmission and related gene expression of GABAergic interneurons."

> "Intellectual disability is closely related to impaired GABA neurotransmission. Brpf1 was specifically expressed in medial ganglionic eminence (MGE), a developmental niche of GABAergic interneurons, and patients with BRPF1 mutations showed intellectual disability." — PMID:33744924

Together, PMID:34485298 and PMID:33744924 establish a **bidirectional excitation/inhibition disturbance** — both excitatory (mEPSC) and inhibitory (mIPSC) synaptic transmission are attenuated. This is a candidate conformance point for `epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance` in the dismech module set (seizures 14–50%), though note the evidence is `MODEL_ORGANISM`/`IN_VITRO`, not human.

**Hematopoietic.** PMID:27500495:

> "Brpf1-deficient pups experienced early lethality due to acute bone marrow failure and aplastic anemia. The mutant bone marrow and fetal liver exhibited severe deficiency in HSCs and hematopoietic progenitors, along with elevated reactive oxygen species, senescence, and apoptosis. BRPF1 deficiency also reduced the expression of multipotency genes, including Slamf1, Mecom, Hoxa9, Hlf, Gfi1, Egr, and Gata3. Furthermore, BRPF1 was required for acetylation of histone H3 at lysine 23, a highly abundant but not well-characterized epigenetic mark."

**Cell cycle / proliferation / embryonic vascular development.** PMID:25773539:

> "Here we present systematic analyses of the mutant animals and demonstrate that the ablation leads to vascular defects in the placenta, yolk sac, and embryo proper, as well as abnormal neural tube closure. At the cellular level, Brpf1 loss inhibits proliferation of embryonic fibroblasts and hematopoietic progenitors. Molecularly, the loss reduces transcription of a ribosomal protein L10 (Rpl10)-like gene and the cell cycle inhibitor p27, and increases expression of the cell-cycle inhibitor p16 and a novel protein homologous to Scp3..."

**Skeletal / osteoclast.** BRPF bromodomain inhibition "impaired RANKL-induced differentiation of primary murine bone marrow cells and human primary monocytes into bone resorbing osteoclasts by specifically repressing transcriptional programs required for osteoclastogenesis" (PMID:28849908) — relevant to the skeletal features and to BRPF1's known role in "skeletal patterning" (PMID:36077605).

### 6.4 Protein dysfunction

Loss of a **multivalent reader/scaffold**, not an enzyme. The truncated protein escapes NMD but shows "aberrant cellular location, loss of certain protein interactions, and decreased histone H3K23 acetylation" (PMID:27939639). No misfolding/aggregation mechanism. Nuclear localization is dependent on KAT6A, ING5, and MEAF6 (UniProt P55201).

Interaction partners (UniProt P55201): **KAT6A, KAT6B, KAT7/HBO1, ING5 (and paralog ING4), MEAF6**, histones H2AC17 and H4C9.

### 6.5 Metabolic changes

No primary metabolic defect. One indirect but therapeutically important link: **short-chain fatty acid (propionate, butyrate) metabolism intersects with H3K23 acylation**, since propionyl-CoA is the donor for propionylation (PMID:32010779). This is a metabolism–epigenome coupling, not a metabolic disease. CHEBI terms: CHEBI:17272 propionate; CHEBI:17968 butyrate; CHEBI:39549 valproic acid; CHEBI:45716 vorinostat.

### 6.6 Immune system involvement

Not an immunologic disease. Two peripheral observations: recurrent infections in 4/28 (14%) (PMID:39837771), and the hematopoietic arm (bone marrow failure in mouse KO, PMID:27500495; anemia + thrombocytopenia in a human family, PMID:37190896). Whether human BRPF1 haploinsufficiency causes clinically meaningful immune dysfunction is **unresolved [gap]**.

### 6.7 Tissue damage mechanisms

In the hematopoietic compartment, mouse KO shows **elevated reactive oxygen species, senescence, and apoptosis** (PMID:27500495). No oxidative-stress, ischemic, fibrotic, or necrotic mechanism is described in the CNS. The CNS phenotype is **developmental (hypoplastic/miswired)** rather than degenerative.

### 6.8 Biochemical abnormalities

The core biochemical lesion is a **quantitative deficit in two histone acyl marks**:
- **H3K23 acetylation** ↓ (PMID:27939640, PMID:27939639, PMID:27500495)
- **H3K23 propionylation** ↓ (PMID:32010779)

There is no measurable serum/urine biochemical abnormality; these are chromatin-level assays on patient fibroblasts/cells. No enzyme deficiency, receptor dysfunction, or ion-channel defect in the classical sense — though the *functional* consequence in neurons is altered excitability (PMID:33744924).

### 6.9 Molecular profiling

- **Transcriptomics:** mRNA-Seq in *Brpf1*-knockdown hippocampal neurons — dysregulation of *C1ql1, Gpr17, Htr1d, Glra1, Cxcl10, Grin2a* (PMID:34485298); in MGE-derived GABAergic interneurons — *Map2k7* and other neurodevelopment/synaptic genes (PMID:33744924); in forebrain KO — ↓ *Robo3*, *Otx1*; ↑ *Hox* genes, *Lhx4*, *Foxa1*, *Tbx5*, *Twist1* (PMID:25568313); in fetal HSC — ↓ *Slamf1, Mecom, Hoxa9, Hlf, Gfi1, Egr, Gata3* (PMID:27500495). Ocular-relevant: *"Loss of BRPF1 has been shown to affect the transcriptional regulation of several key transcription factors, including Pitx2, Hmx1 and Pax6, which have been implicated in a wide range of ocular developmental abnormalities."* (PMID:39837771).
- **Chromatin accessibility / imaging:** ATAC-See and immunofluorescence localized H3K23 propionylation to active chromatin (PMID:32010779).
- **Proteomics, metabolomics, lipidomics:** **No disease-specific studies [gap].**
- **Single-cell / spatial transcriptomics:** **No BRPF1-specific studies [gap].** The forebrain KO Tbr2+ progenitor finding (PMID:25568313) is a natural target for scRNA-seq.
- **Functional genomics screens:** the CRISPR screen in PMID:40060486 (preprint) recovered Brpf1 as a modulator of loop-extrusion-dependent gene regulation.
- **Structural biology:** co-crystal structures of the BRPF1 bromodomain exist from chemical-probe programs (PMID:26061247 — "structure guided development … through the iterative use of X-ray cocrystal structures"). AlphaFold model available for P55201.

---

## 7. Anatomical Structures Affected

### 7.1 Organ level

**Primary:**
| Structure | UBERON | Basis |
|---|---|---|
| Brain | UBERON:0000955 | ID, DD, MRI findings |
| Cerebral cortex / neocortex | UBERON:0000956 / UBERON:0001950 | Reduced dendritic complexity in cortical pyramidal neurons (PMID:31213987); neocortical abnormalities (PMID:25568313) |
| Hippocampal formation | UBERON:0002421 | Reduced granule-cell dendritic complexity, ↓mEPSC, spatial memory (PMID:31213987; PMID:34485298) |
| Corpus callosum | UBERON:0002336 | Agenesis 2/17 MRI (PMID:39837771); partial callosal agenesis in mouse (PMID:25568313) |
| Eye / eyelid | UBERON:0000970 / UBERON:0001711 | Ptosis, blepharophimosis — BRPF1-specific (PMID:27939639) |
| Optic nerve | UBERON:0000941 | Subclinical optic neuropathy (PMID:38590032) |
| Face / craniofacial skeleton | UBERON:0000033 (head) / UBERON:0001434 | Characteristic dysmorphism |

**Secondary / variable:**
| Structure | UBERON | Basis |
|---|---|---|
| Bone marrow | UBERON:0002371 | Anemia/thrombocytopenia (PMID:37190896); marrow failure in mouse KO (PMID:27500495) |
| Cervical vertebral column | UBERON:0000959 | C2/C3 fusion 3/10 (HPOA); atlanto-axial malformation (PMID:35243762) |
| Spinal cord | UBERON:0002240 | "Central nervous system and spinal abnormalities are also seen in some individuals" (PMID:27939640) |
| Heart | UBERON:0000948 | Cardiac anomalies in a subset (PMID:32010779); 1/25 (PMID:39837771) |
| Esophagus / upper GI | UBERON:0001043 | GERD 31% |
| Larynx | UBERON:0001737 | Laryngomalacia 7% |
| Skeletal muscle | UBERON:0001134 | Hypotonia, weakness |
| Skin / hair follicle | UBERON:0002097 / UBERON:0002073 | Hypertrichosis, hair abnormalities (novel, PMID:39837771) |
| Testis / gonad | UBERON:0000473 | Cryptorchidism 19% |

**Body systems:** nervous (primary), visual/ophthalmic (primary), musculoskeletal, craniofacial, hematopoietic, gastrointestinal, integumentary, genitourinary.

### 7.2 Tissue and cell level

| Cell type | CL ID | Evidence |
|---|---|---|
| Pyramidal neuron (cortical) | CL:0000598 | PMID:31213987 |
| Hippocampal granule cell / dentate granule cell | CL:0000120 (granule cell) | PMID:31213987 |
| GABAergic interneuron | CL:0000617 (GABAergic neuron) | PMID:33744924 |
| Parvalbumin-expressing interneuron | CL:4023018 (*verify with OAK*) | PMID:33744924 |
| Neural progenitor / intermediate neuronal progenitor (Tbr2+) | CL:0011020 (neural progenitor cell) | PMID:25568313 |
| Hematopoietic stem cell | CL:0000037 | PMID:27500495 |
| Hematopoietic multipotent progenitor | CL:0000837 | PMID:27500495 |
| Erythroblast | CL:0000765 | PMID:21753189 (Brd1/Brpf2 paralog) |
| Osteoclast | CL:0000092 | PMID:28849908 |
| Embryonic fibroblast (MEF) | CL:0000057 (fibroblast) | PMID:25773539 |
| Endothelial cell (vascular defects) | CL:0000115 | PMID:25773539 |

> **Curator caution:** every CL/UBERON/GO ID above must be re-verified with `just validate-terms` — some (notably the PV-interneuron term) are suggestions requiring OAK confirmation.

### 7.3 Subcellular level

| Compartment | GO ID | Note |
|---|---|---|
| **Nucleus** | GO:0005634 | Primary site of BRPF1 action (UniProt P55201) |
| Chromosome / chromatin | GO:0005694 / GO:0000785 | Binds chromatin, remains chromosome-associated through mitosis (PMID:18469222) |
| **MOZ/MORF histone acetyltransferase complex** | **GO:0070776** | The most specific and disease-defining compartment |
| Histone acetyltransferase complex | GO:0000123 | Parent |
| Cytoplasm | GO:0005737 | Where truncated variants mislocalize |
| Dendritic spine | GO:0043197 | Reduced density/altered morphology (PMID:31213987) |
| Synapse | GO:0045202 | Altered morphology (PMID:31213987) |

BRPF1 "localizes to transcription start sites" (UniProt P55201).

### 7.4 Localization and lateralization

- **Ptosis/blepharophimosis:** typically **bilateral**, may be asymmetric.
- **Optic neuropathy:** reported **bilateral** — *"such an exam also detected bilateral subclinical optic neuropathy in this case"* (PMID:38590032).
- **Facial asymmetry:** 3/28 (11%) (PMID:39837771).
- **Brain findings:** midline (corpus callosum) and diffuse (white matter volume), not lateralized.
- **Strabismus:** unilateral or bilateral, variable.

---

## 8. Temporal Development

### 8.1 Onset

- **Congenital** — HPOA: HP:0003577 Congenital onset (10/10); HP:0003623 Neonatal onset (4/4).
- **Prenatal:** intrauterine growth restriction 2/20 (HP:0001511). Mouse *Brpf1* is required from ~E9.5 (PMID:24646517), so human haploinsufficiency acts throughout embryogenesis.
- **Neonatal/infantile:** congenital ptosis, hypotonia (9/15 infant hypotonia), feeding impairment (8/15) (PMID:38346666; PMID:27939640).
- **Infancy–early childhood:** motor and speech delay become apparent; delayed walking.
- **School age:** language disorder (including written-language domain), ADHD, learning difficulty predominate.
- **Onset pattern:** **chronic, insidious, developmental** — not acute or episodic.

### 8.2 Progression

- **Stages:** No formal staging system exists. Practical natural-history phases: (i) neonatal/infantile — hypotonia, feeding, congenital ptosis; (ii) toddler/preschool — motor and speech delay; (iii) school age — language disorder, ID, behavioral phenotype; (iv) adolescence/adulthood — stable ID, largely resolved gross-motor delay, ongoing communication needs.
- **Progression rate:** **Non-progressive.** No neurodegeneration reported in any human series.
- **Course pattern:** **Static/stable with developmental improvement.** PMID:38346666 explicitly documents improvement: motor delays "often resolved in later childhood."
- **Duration:** **Chronic, lifelong.**
- **Seizures**, when present (14–50%), are episodic on a static substrate.

### 8.3 Patterns

- **Remission:** Not applicable to the core neurodevelopmental phenotype. Gross-motor delay commonly resolves; ptosis is surgically correctable; seizures may be pharmacologically controlled.
- **Critical periods:** (i) **embryonic** — the window in which forebrain neurogenesis, callosal formation, and ocular/craniofacial morphogenesis are set (irreversible by the time of diagnosis); (ii) **infancy–early childhood** — the intervention window for speech/language therapy, feeding support, and amblyopia prevention (ptosis surgery before visual-axis deprivation causes irreversible amblyopia). The speech-therapy window is the highest-yield intervention target given the near-universal speech/language phenotype (PMID:38346666).

---

## 9. Inheritance and Population

### 9.1 Epidemiology

- **Prevalence:** Orphanet records a **worldwide point prevalence class of "<1 / 1,000,000"** (validated) for ORPHA:698090 — i.e. **< 0.1 per 100,000**. Orphanet's `prevalence_class` maps to the dismech `PrevalenceClassEnum` value **`BELOW_1_IN_1000000`**.
- **Reported case count:** Orphanet's second epidemiology record gives **79 cases (worldwide, "Cases/families", validated)**. This is the more defensible figure to curate as `measure_type: CASES_IN_LITERATURE`.
- **Incidence:** **Not established [gap].** No birth-prevalence or incidence estimate exists.
- **Likely underdiagnosis:** PMID:35243762 argues *"Later, another 20 patients were also described by distinct reports, suggesting IDDDFP could be a more frequent cause of intellectual disability as it was thought before."* Given the mild phenotype, high FSIQ, and preserved adaptive behavior, ascertainment is likely incomplete.

Suggested dismech `Prevalence` record:

```yaml
prevalence:
- population: Worldwide
  measure_type: POINT_PREVALENCE
  prevalence_class: BELOW_1_IN_1000000
  notes: Orphanet worldwide point-prevalence class <1 / 1 000 000 (validated).
- population: Worldwide
  measure_type: CASES_IN_LITERATURE
  rate_per_100000: null
  notes: >-
    Orphanet records 79 cases worldwide (validated). Colson et al. 2025 add
    29 new patients from 20 families to "over 50 previously published cases."
```

### 9.2 Genetic etiology parameters

| Parameter | Status |
|---|---|
| **Inheritance pattern** | **Autosomal dominant** (HP:0000006). Consistent across OMIM, Orphanet, MedGen, HPOA, and all primary reports. |
| **Penetrance** | Appears **high but incomplete for ID specifically**. Carriers with normal intellect are documented (PMID:35243762 — normal intellectual development with congenital ptosis and neurological signs). Transmitting parents are typically mildly affected rather than unaffected. No quantitative penetrance estimate exists **[gap]**. |
| **Expressivity** | **Highly variable, including intrafamilial.** PMID:39837771: *"phenotypic differences were observed between family members carrying the same pathogenic variant, affecting intellectual ability, dysmorphic features and malformations, suggesting an intrafamilial variability."* |
| **Genetic anticipation** | **Not applicable** — not a repeat-expansion disorder; no anticipation reported. |
| **Germline mosaicism** | **Not reported [gap]**. Empiric recurrence risk for apparently de novo cases should nonetheless include a small mosaicism allowance per standard genetic-counseling practice. |
| **Founder effects** | **None identified.** Cases span European, Middle Eastern (Israeli — PMID:31020800; Turkish — PMID:37190896; Saudi — PMID:32457794), and North American ancestries with private variants. |
| **Consanguinity** | **Not a factor** — dominant mechanism. PMID:31020800 explicitly describes a **nonconsanguineous** family. |
| **Carrier frequency** | **Not applicable** (dominant; affected heterozygotes, not carriers). |
| **De novo rate** | Majority of cases; PMID:39837771 states de novo predominates, with 5/20 families showing two-generation transmission. ClinGen's dosage curation notes "Seven protein-truncating variants were de novo mutations." |
| **Recurrence risk** | 50% per pregnancy for an affected parent (Orphanet). |

### 9.3 Population demographics

- **Affected populations:** No ethnic predilection. Reported in European, Israeli/Jewish (mixed descent), Turkish, Saudi Arabian, Latin American, and North American families.
- **Geographic distribution:** Worldwide; no endemic focus. No geographically clustered variant.
- **Sex ratio:** Male predominance in reported series (10/15 male in PMID:38346666) — **almost certainly ascertainment bias, not a true sex effect**; the gene is autosomal. Curate as unknown/1:1 rather than asserting a skew.
- **Age distribution:** Pediatric-diagnosed, lifelong. Median age 7y4m in the deep-phenotyping cohort (PMID:38346666). Adults are described chiefly as transmitting parents.

---

## 10. Diagnostics

### 10.1 Genetic testing — the diagnostic mainstay

There is **no biochemical or imaging biomarker**; diagnosis is molecular.

| Modality | Utility |
|---|---|
| **Exome sequencing (ES/WES)** | **First-line and the modality that established every reported case.** PMID:27939639 (index family), PMID:31020800, PMID:37190896, PMID:32457794, PMID:38590032 all used ES. PMID:32457794: *"Whole exome sequencing analysis has been proven as a valuable tool in the molecular diagnostics."* |
| **Genome sequencing (WGS)** | Reasonable when ES is negative; better for non-coding/structural variants. No BRPF1-specific WGS yield data **[gap]**. |
| **NDD/ID gene panels** | BRPF1 is included on contemporary ID/NDD and chromatinopathy panels. Check GTR for current panel membership. |
| **Single-gene BRPF1 sequencing** | Appropriate only for **cascade testing** of at-risk relatives once a familial variant is known (PMID:31020800, PMID:32457794 both used Sanger for family segregation). |
| **Chromosomal microarray (CMA)** | Detects whole-gene deletions and the contiguous **3p25/3p25.3 deletion** (BRPF1 ± SETD5). PMID:37190896 used CMA to exclude additional CNVs. |
| **Exome-based CNV calling (e.g. ExomeDepth)** | Demonstrated to recover BRPF1 deletions from existing ES data (PMID:33611074) — worth running before ordering separate CMA. |
| **Karyotype / FISH** | Low yield; not indicated except to characterize a known rearrangement. |
| **mtDNA testing / repeat expansion testing** | **Not applicable.** |

**Recommended approach:** ES (trio, with CNV calling) as first-tier for the ID/DD + ptosis phenotype; CMA if ES-CNV not performed; Sanger cascade testing of parents and at-risk relatives — **essential**, because mildly affected transmitting parents are common and change recurrence risk from ~1% to 50%.

### 10.2 Omics-based diagnostics

- **Functional H3K23 acetylation/propionylation assay on patient cells** — used as research-grade evidence of pathogenicity for VUS (PMID:27939640; PMID:32010779). Not a clinically validated assay **[gap: no CLIA/accredited version]**.
- **DNA methylation episignature (EpiSign)** — **not available for BRPF1** (established for KAT6A and KAT6B, PMID:37249002). This is the single most useful missing diagnostic tool for BRPF1 VUS resolution.
- **RNA-seq / proteomics / metabolomics / liquid biopsy** — no diagnostic role.

### 10.3 Clinical and imaging tests

| Test | Findings / rationale |
|---|---|
| **Ophthalmological examination + OCT** | Ptosis, blepharophimosis, strabismus, amblyopia, refractive error; **OCT is required to detect subclinical optic neuropathy** (PMID:38590032). PMID:39837771 recommends: *"we recommend that all individuals with pathogenic BRPF1 variants undergo regular ophthalmological surveillance."* |
| **Brain MRI** | Agenesis/thinning of the corpus callosum, reduced cerebral white matter volume, white-matter hyperintensities, Chiari type I malformation (PMID:39837771; PMID:38590032; HPOA). Abnormal in a minority. |
| **Cervical spine imaging** | C2/C3 vertebral fusion (3/10 HPOA), atlanto-axial malformation (PMID:35243762) — relevant to anesthesia and sports clearance. |
| **EEG** | For seizures (14–50%). No BRPF1-specific EEG signature described **[gap]**. |
| **Formal speech/language and neuropsychological assessment** | Should be **standard**, given near-universal involvement across receptive, expressive, written, and social-pragmatic domains, and to detect childhood apraxia of speech (PMID:38346666). |
| **Full blood count** | Anemia and thrombocytopenia reported (PMID:37190896); mouse KO shows marrow failure (PMID:27500495). Reasonable baseline. |
| **Echocardiogram** | Cardiac anomalies in a subset (PMID:32010779; 1/25 in PMID:39837771). |
| **Audiology, growth monitoring, feeding/swallow assessment** | Standard NDD workup. |
| **Biopsy / histopathology** | No diagnostic role. Skin fibroblast culture is used only for research functional assays. |

LOINC coding: no BRPF1-specific LOINC analyte. Use generic genetic-test LOINC codes and standard CBC codes for the hematologic monitoring.

### 10.4 Clinical criteria and differential diagnosis

**No consensus clinical diagnostic criteria exist [gap].** Diagnosis = compatible phenotype + confirmed heterozygous pathogenic BRPF1 variant.

**Differential diagnosis:**

| Condition | Distinguishing features |
|---|---|
| **KAT6A syndrome** | Same complex; more severe ID, more cardiac disease, distinct episignature. PMID:27939640: *"These clinical features overlap with but are not identical to those reported for persons with KAT6A or KAT6B mutations."* |
| **KAT6B disorders** (Genitopatellar; Say-Barber-Biesecker-Young-Simpson) | Patellar agenesis, genital anomalies, blepharophimosis with mask-like face; distinct episignatures (PMID:40593218). |
| **3p25 / 3p25.3 deletion syndrome (SETD5)** | Broader/more severe ID from SETD5; ptosis and blepharophimosis are the BRPF1-attributable component (PMID:27939639). |
| **BPES (blepharophimosis-ptosis-epicanthus inversus, FOXL2)** | Ptosis + blepharophimosis + epicanthus inversus but typically **normal intellect**; female premature ovarian insufficiency in type I. |
| **Noonan syndrome / RASopathies** | Real, documented confusion: PMID:41137536 found BRPF1 among six alternative diagnoses in patients clinically diagnosed as Noonan — *"In six cases, alternative genetic diagnoses were established due to variants in SETD5, BRPF1, DPH1, ACTB, CREBBP, and GATA4, genes associated with syndromes presenting overlapping phenotypes with NS."* |
| **Cornelia de Lange syndrome** | Synophrys, hypertrichosis, ID — overlapping. Mechanistically adjacent via the loop-extrusion/MORF interplay (PMID:40060486). |
| Other chromatinopathies (Rubinstein-Taybi/CREBBP, Kabuki/KMT2D, CHD8) | Overlapping NDD; distinguish molecularly. |
| Congenital myopathy / myasthenic syndrome | Considered for the congenital ptosis + hypotonia + weakness presentation (PMID:35243762). |

### 10.5 Screening

- **Newborn screening:** Not applicable and not recommended (no treatable metabolic defect).
- **Carrier screening:** Not applicable (dominant).
- **Cascade screening:** **Strongly indicated** — targeted Sanger testing of the proband's parents and at-risk relatives. Multiplex families with mildly affected transmitting parents are well documented (PMID:27939639; PMID:31020800; PMID:37190896; PMID:39837771). Parental testing is what distinguishes ~1% from 50% recurrence risk.

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality

- **Life expectancy: apparently normal.** No abstract reports reduced survival, premature mortality, or disease-specific deaths in humans. Affected adults reproduce and transmit the variant (PMID:27939639 — 5 affected members; PMID:31020800 — affected mother and three sons).
- **Important contrast — do not extrapolate from mouse:** homozygous *Brpf1* null is embryonic lethal at E9.5 (PMID:24646517; PMID:25773539); conditional hematopoietic deletion causes "early lethality due to acute bone marrow failure and aplastic anemia" (PMID:27500495); forebrain-specific deletion causes "early postnatal lethality" (PMID:25568313). These are **homozygous/conditional-null** phenotypes with no human counterpart — human disease is **heterozygous**. Curate as a `HUMAN_MODEL_MISMATCH` discussion, not as a human prognosis claim.
- **Mortality rate / 5-yr and 10-yr survival:** Not applicable; no excess mortality documented **[no data]**.

### 11.2 Morbidity and function

- **Dominant disability:** communication impairment. Language disorder in 11/12 assessed, speech disorder in 7/9, childhood apraxia of speech in 3/9 (PMID:38346666).
- **Cognitive outcome:** favorable relative to peer chromatinopathies. Mild-to-moderate ID predominates (6 mild / 10 moderate of 16 with ID); no severe/profound ID in the 2025 cohort; FSIQ ≥70 in all four formally tested in the deep-phenotyping cohort (PMID:38346666; PMID:39837771).
- **Adaptive functioning:** a **relative strength** — *"Adaptive behavior and cognition were strengths when compared to other monogenic neurodevelopmental chromatin-related disorders"* (PMID:38346666).
- **Motor outcome:** favorable — delays "often resolved in later childhood" (PMID:38346666).
- **Visual outcome:** the main organ-specific morbidity risk — vision impairment in 13/15, amblyopia in 3/29, and undetected subclinical optic neuropathy (PMID:38346666; PMID:39837771; PMID:38590032).
- **QoL instruments:** **none applied to this population [gap]**.

### 11.3 Complications

Amblyopia from uncorrected ptosis; refractive error; optic neuropathy; seizures; GERD and constipation; feeding difficulty and failure to thrive in infancy; recurrent infections (14%); anemia/thrombocytopenia (8%); obesity (14%); cervical spine instability (atlanto-axial malformation / C2-C3 fusion) with anesthetic and injury implications; educational underachievement and social-communication limitation.

### 11.4 Recovery potential

The neurodevelopmental substrate is fixed (developmental, not degenerative), but **functional trajectory improves with intervention** — motor delays resolve, and speech/language and adaptive skills respond to therapy. Ptosis is surgically correctable. There is **no disease-modifying therapy** and no evidence that any intervention alters the underlying chromatin defect in humans.

### 11.5 Prognostic factors and biomarkers

**No validated prognostic factors or biomarkers.** Explicitly:

> "Our results, in agreement with other studies, do not show a clear genotype–phenotype correla[tion]" — PMID:39837771 (quote truncated at source by the extraction tool; **curators must re-read the full sentence from PMC11973018 before quoting**)

Variant type (truncating vs missense vs whole-gene deletion) and variant position **do not** predict severity. Intrafamilial variability with an identical variant (PMID:39837771) is direct evidence that genotype alone is insufficiently prognostic. Favorable indicators are clinical, not molecular: preserved adaptive behavior, FSIQ ≥70, and resolving motor delay.

---

## 12. Treatment

**There is no disease-modifying or curative therapy. Management is entirely supportive, multidisciplinary, and symptom-directed.** No clinical trial has ever been registered for BRPF1-related disorder (no NCT identifiers found).

### 12.1 Supportive and rehabilitative care — the standard of care

| Intervention | Rationale | Suggested NCIT | `therapeutic_modality` |
|---|---|---|---|
| **Speech and language therapy** | Highest-yield intervention; near-universal language disorder, including childhood apraxia of speech requiring apraxia-specific (motor-based) approaches, not generic language therapy (PMID:38346666) | NCIT:C159273 Speech Therapy | BEHAVIORAL |
| **Physical therapy** | Hypotonia, gross motor delay, muscular weakness | NCIT:C15302 Physical Therapy | BEHAVIORAL |
| **Occupational therapy** | Fine motor delay, feeding, ADLs | NCIT:C121351 Occupational Therapy | BEHAVIORAL |
| **Early intervention / special education** | Global developmental delay, ID | NCIT:C15315 Rehabilitation | BEHAVIORAL |
| **Feeding/nutrition support** | Infant feeding impairment (8/15), FTT | NCIT:C15433 Nutritional Support *(do not auto-tag as BEHAVIORAL — see CLAUDE.md)* | — |
| **Behavioral therapy / ADHD management** | 62% behavioral disorder, 33% ADHD, 21% anxiety, 31% sleep disturbance | NCIT:C181743 Behavioral Counseling | BEHAVIORAL |
| **Genetic counseling** | 50% recurrence per pregnancy; cascade testing | NCIT:C15240 Genetic Counseling | — |

### 12.2 Ophthalmologic management — the disorder-specific priority

| Intervention | Rationale | Suggested NCIT |
|---|---|---|
| **Regular ophthalmological surveillance incl. OCT** | Explicitly recommended: *"we recommend that all individuals with pathogenic BRPF1 variants undergo regular ophthalmological surveillance"* (PMID:39837771); OCT needed to catch subclinical optic neuropathy (PMID:38590032) | NCIT:C49236 Therapeutic Procedure / diagnostic surveillance |
| **Ptosis repair surgery** | Prevents deprivation amblyopia; cosmetic/psychosocial benefit | NCIT:C15329 Surgical Procedure → `therapeutic_modality: SURGERY` |
| **Strabismus surgery** | 48% strabismus | NCIT:C15329 Surgical Procedure → SURGERY |
| **Refractive correction / amblyopia therapy** | Myopia 17%, hypermetropia 7%, amblyopia 10% | NCIT:C50072 Eyeglasses / corrective lens **[verify with OAK]** → DEVICE |

### 12.3 Pharmacotherapy

**Symptomatic only:**
- **Antiseizure medication** for the 14–50% with seizures — no BRPF1-specific agent preference established **[gap]**. NCIT:C15986 Pharmacotherapy; `therapeutic_agent` per drug chosen.
- **ADHD stimulants / non-stimulants** — standard NDD practice; no BRPF1-specific evidence.
- **Anti-reflux therapy** for GERD (31%).
- **Pharmacogenomics:** No BRPF1-specific PGx. PharmGKB has no BRPF1 clinical annotation. Note that if valproate were ever used as an antiseizure drug, there is an interesting mechanistic coincidence with §12.4 — but this is **not** a validated indication.

### 12.4 Experimental / mechanism-based therapeutic leads

This is the most scientifically interesting and most easily over-claimed section. **Nothing below has been tested in a human with BRPF1-related disorder.**

The key finding (PMID:32010779):

> "Valproate, vorinostat, propionate and butyrate promote H3K23 acylation. These results reveal the dual functionality of BRPF1-KAT6 complexes, shed light on mechanisms underlying related developmental disorders and various cancers, and suggest mutation-based therapy for medical conditions with deficient histone acylation."

Candidate agents and their CHEBI/NCIT anchors:

| Agent | CHEBI | Class | Status |
|---|---|---|---|
| Valproate / valproic acid | CHEBI:39549 | HDAC inhibitor, antiseizure drug | Preclinical only for this indication; **teratogenic** — a serious caveat in a reproductive-age/pediatric population |
| Vorinostat (SAHA) | CHEBI:45716 | HDAC inhibitor | Preclinical; oncology-approved, not for NDD |
| Propionate | CHEBI:17272 | Short-chain fatty acid | Preclinical; acyl-CoA donor |
| Butyrate | CHEBI:17968 | Short-chain fatty acid | Preclinical |

**Framing guardrail for curation:** the mechanistic logic is *restore the deficient H3K23 acyl mark*. But (i) the data are entirely in vitro/mouse; (ii) the developmental window for the CNS/craniofacial phenotype has closed by the time of diagnosis; (iii) valproate is a known teratogen and an HDAC inhibitor is a blunt, genome-wide instrument. Curate as `EMERGING` / `mechanistic_hypotheses`, never as a treatment.

**Bromodomain chemical probes — a research tool, and directionally *opposite* to therapy.** Selective BRPF bromodomain inhibitors exist: **IACS-9571** (dual TRIM24/BRPF1, ITC Kd = 14 nM for BRPF1, PMID:26061247) and **PFI-4 / OF-1 / NI-57** (PMID:28849908). These *inhibit* BRPF1 and would be expected to **worsen** a haploinsufficiency phenotype; their therapeutic interest is in cancer and osteolytic bone disease — *"the excellent druggability of these bromodomains may lead to new treatment strategies for patients suffering from bone loss or osteolytic malignant bone lesions"* (PMID:28849908). **Do not curate these as candidate treatments for IDDDFP.**

### 12.5 Advanced therapeutics

- **Gene therapy / gene editing:** None. No program exists. Conceptually challenging: the target is a large (1,214 aa, ~3.6 kb CDS) nuclear scaffold requiring precise dosage in the developing brain — dosage-sensitive genes are poor AAV overexpression targets.
- **RNA-based therapies (ASO, siRNA, mRNA):** None. Note that for a *haploinsufficiency* disorder, the relevant ASO paradigm would be upregulation (e.g. TANGO/splice-modulation to boost expression from the intact allele), not the RNase H knockdown or exon-skipping paradigms in the dismech `antisense_oligonucleotide_therapy` module. **No such program exists for BRPF1 [gap].**
- **Cell therapy, immunotherapy, targeted therapy:** Not applicable.

### 12.6 Treatment strategy

No published treatment algorithm, guideline, or care pathway exists for BRPF1-related disorder **[gap]**. Practical management follows generic chromatinopathy/NDD care plus the two disorder-specific additions the literature does support: **(1) structured, apraxia-aware speech-language intervention** (PMID:38346666) and **(2) regular ophthalmological surveillance including OCT** (PMID:39837771; PMID:38590032).

---

## 13. Prevention

- **Primary prevention:** Not possible for de novo cases. For families with a known variant, options are **preimplantation genetic testing (PGT-M)** and **prenatal diagnosis** (CVS/amniocentesis) — standard for a known AD variant with 50% recurrence risk. Orphanet: transmission is autosomal dominant; "genetic counseling should be offered to affected individuals informing them that there is a 50% risk of having an affected child at each pregnancy."
- **Secondary prevention (early detection):** The highest-value activity. Early molecular diagnosis via trio ES enables (i) early speech/language therapy in the critical window, (ii) ophthalmological surveillance before amblyopia becomes fixed, and (iii) cascade family testing.
- **Tertiary prevention (complication prevention):**
  - **Ptosis repair before deprivation amblyopia** — the clearest preventable harm.
  - **OCT surveillance** for otherwise-silent optic neuropathy (PMID:38590032).
  - **Cervical spine assessment** before anesthesia or contact sports (C2/C3 fusion, atlanto-axial malformation).
  - **CBC monitoring** where hematologic abnormality is suspected (PMID:37190896).
  - Seizure control; reflux and constipation management; weight monitoring (obesity 14%).
- **Immunization:** No disorder-specific vaccine strategy. Routine childhood immunization per national schedule; the 14% recurrent-infection rate warrants normal-to-diligent vaccine adherence.
- **Population screening / newborn screening:** Not indicated — no treatable metabolic defect, no validated screening test, prevalence <1/1,000,000.
- **Risk stratification:** Not applicable at the population level; within families, cascade genetic testing is the stratifier.
- **Behavioral / environmental / public health interventions:** Not applicable — no environmental contribution to etiology.
- **Prophylaxis:** No prophylactic medication.
- **Genetic counseling:** Central. Counsel on (i) 50% recurrence for an affected parent; (ii) **marked variable expressivity, including the possibility of a much milder or even cognitively normal outcome** (PMID:35243762; PMID:39837771) — a parent transmitting the variant cannot be told the child will be similarly affected; (iii) the need to test apparently unaffected parents, since mild transmitting parents are common; (iv) residual germline-mosaicism risk for apparently de novo cases. NCIT:C15240 Genetic Counseling.

---

## 14. Other Species / Natural Disease

### 14.1 Taxonomy and orthologs

| Species | NCBI Taxon | Gene | NCBI Gene ID | Notes |
|---|---|---|---|---|
| *Homo sapiens* | NCBITaxon:9606 | BRPF1 | 7862 | 3p25.3 |
| *Mus musculus* | NCBITaxon:10090 | Brpf1 | MGI:1926033; Chr 6 | Primary model |
| *Danio rerio* | NCBITaxon:7955 | brpf1 | — | ZFIN; TrxG mutant (PMID:18469222) |
| *Drosophila melanogaster* | NCBITaxon:7227 | (BRPF ortholog in the MOZ/MORF complex) | — | Complex conserved (PMID:40593218) |
| *Caenorhabditis elegans* | NCBITaxon:6239 | (BRPF ortholog) | — | Complex conserved (PMID:40593218) |

> Verify MGI:1926033 and the mouse chromosome/coordinates directly at informatics.jax.org before curating — the identifier came from a web search snippet, not a fetched MGI record.

### 14.2 Evolutionary conservation

Strong. PMID:40593218: *"The evolutionary conservation of these complexes in Drosophila melanogaster and Caenorhabditis elegans underscores their fundamental biological significance."* PMID:36077605 notes the four core subunits "play crucial roles in different biological processes across diverse species, such as embryonic development, forebrain development, skeletal patterning and hematopoiesis." Both patient missense variants in the 2025 cohort — p.(Cys23Arg) and p.(Arg548Trp) — "affect conserved residue[s]" (PMID:39837771).

### 14.3 Natural disease in other species

**No naturally occurring BRPF1 disease is recorded in companion animals, livestock, or wildlife.** OMIA contains no BRPF1 entry **[gap]**. All non-human BRPF1 phenotypes are **engineered**, not natural. No breed-specific (VBO) association exists.

### 14.4 Comparative pathology

The mouse and zebrafish phenotypes are informative but **more severe than human disease**, because they are homozygous/conditional nulls rather than heterozygous LoF. Key comparative points:
- **Mouse homozygous null:** embryonic lethal ~E9.5; vascular defects in placenta, yolk sac, embryo proper; abnormal neural tube closure (PMID:24646517; PMID:25773539). **No human counterpart.**
- **Zebrafish *brpf1* mutant:** "anterior transformations of pharyngeal arches due to progressive loss of anterior Hox gene expression" (PMID:18469222) — a homeotic craniofacial phenotype. This is mechanistically suggestive for the human craniofacial dysmorphism but the human phenotype is *not* homeotic.
- **Mouse heterozygote:** the closest model to human disease — reduced dendritic arborization, spine deficits, learning/memory impairment (PMID:31213987).

### 14.5 Transmission

**Not applicable.** Not infectious; no zoonotic potential; no cross-species susceptibility.

---

## 15. Model Organisms

### 15.1 Mouse — the principal model

| Model | Genotype | Phenotype | PMID | `evidence_source` |
|---|---|---|---|---|
| **Constitutive null** | *Brpf1*^−/− | Embryonic lethality ~E9.5; vascular defects in placenta, yolk sac, embryo proper; abnormal neural tube closure; ↓ MEF and hematopoietic-progenitor proliferation; ↓ *Rpl10*-like, ↓ p27, ↑ p16 | 25773539; 24646517 | MODEL_ORGANISM |
| **Knock-in reporter** | *Brpf1* reporter allele | 4-D spatiotemporal expression atlas; "high expression is present in the testis and specific regions of the brain" postnatally | 24646517 | MODEL_ORGANISM |
| **Forebrain conditional KO** | *Emx1-Cre; Brpf1*^fl/fl (homozygous) | Early postnatal lethality; neocortical abnormalities; **partial callosal agenesis**; fewer Tbr2+ intermediate progenitors; aberrant neurogenesis; ↓*Robo3*/*Otx1*, ↑*Hox*/*Lhx4*/*Foxa1*/*Tbx5*/*Twist1* | 25568313 | MODEL_ORGANISM |
| **★ Forebrain heterozygote — the disease-matched model** | *Emx1-Cre; Brpf1* heterozygous | Reduced dendritic complexity (hippocampal granule + cortical pyramidal neurons); ↓spine density; altered spine/synapse morphology; ↓mEPSC frequency and amplitude; **decreased anxiety**; defective learning and memory | 31213987 | MODEL_ORGANISM |
| **Hematopoietic conditional KO** | Blood-cell-selective *Brpf1* deletion | Early lethality from acute **bone marrow failure and aplastic anemia**; severe HSC/progenitor deficiency in marrow and fetal liver; ↑ROS, senescence, apoptosis; ↓*Slamf1/Mecom/Hoxa9/Hlf/Gfi1/Egr/Gata3*; loss of H3K23ac | 27500495 | MODEL_ORGANISM |
| **Hippocampal shRNA knockdown (AAV, stereotactic, adult)** | *shBrpf1* | ↓mEPSC frequency preceding morphological change; decreasing trend in Morris water maze spatial learning/memory; ↓*C1ql1, Gpr17, Htr1d, Glra1, Cxcl10, Grin2a* | 34485298 | MODEL_ORGANISM / IN_VITRO |
| **MGE-derived GABAergic interneuron knockdown** | AAV-*shBrpf1* | ↑firing threshold, ↓evoked APs, ↓mIPSC amplitude; ↓*Map2k7*; trend toward reduced PV+ differentiation | 33744924 | IN_VITRO |
| **Targeted allele resource** | *Brpf1*^tm1a(EUCOMM)Wtsi (MGI:4433631) | EUCOMM knockout-first conditional-ready allele | — | resource |

### 15.2 Zebrafish

*brpf1* mutants: "anterior transformations of pharyngeal arches due to progressive loss of anterior Hox gene expression"; Brpf1 recruits Moz to active chromatin and remains chromosome-bound through mitosis; **the PWWP domain "is absolutely essential for Brpf1 function in vivo"** (PMID:18469222). Establishes Brpf1 as a Trithorax-group member and provides the first demonstration of histone binding by a PWWP domain.

### 15.3 Other systems

- **In vitro / cellular:** patient-derived **skin fibroblasts** (used for transcript/protein/H3K23ac assays — PMID:27939639); mouse embryonic fibroblasts (PMID:25773539); primary cultured hippocampal neurons (PMID:34485298); primary murine bone marrow cells and human primary monocytes for osteoclast differentiation (PMID:28849908); mouse ES cells (PMID:40060486).
- **iPSC / organoid models: none reported [gap].** This is a conspicuous, high-value missing model given the human-specific cortical biology at issue.
- **Induced (non-genetic) models:** chemical-probe inhibition of the BRPF bromodomain (IACS-9571, PFI-4, OF-1, NI-57) provides an acute pharmacological loss-of-function tool (PMID:26061247; PMID:28849908) — though it targets only the bromodomain, not the whole scaffold.

### 15.4 Phenotype recapitulation and limitations

**Recapitulated in the heterozygous mouse:** learning/memory deficits, reduced dendritic arborization and spine density, reduced excitatory synaptic transmission, altered anxiety behavior (PMID:31213987) — a good mechanistic match to human ID.

**Recapitulated in conditional/homozygous models but NOT matching human severity:** callosal agenesis (partial in mouse KO vs 12% in humans), bone marrow failure (lethal in mouse vs mild anemia/thrombocytopenia in 8% of humans), embryonic lethality (mouse only).

**Not recapitulated / not modeled:**
- **Ptosis and blepharophimosis** — the single most characteristic human feature. No abstract reports a murine eyelid phenotype. **[Major gap.]**
- **Speech and language disorder / childhood apraxia of speech** — the most functionally significant human phenotype, and intrinsically unmodellable in mouse.
- **Human-specific cortical biology** (outer radial glia/OSVZ) absent from rodent models.
- The zebrafish homeotic pharyngeal-arch transformation has **no human correlate**.

> **Suggested dismech curation:** record a `discussions` entry with `kind: HUMAN_MODEL_MISMATCH` (not `KNOWLEDGE_GAP`) for at least two items: (1) the mouse models are homozygous/conditional nulls producing lethality, while human disease is heterozygous and compatible with normal lifespan; and (2) no model reproduces ptosis/blepharophimosis, the disorder's defining feature — so the ocular/periocular developmental mechanism (the *Pitx2/Hmx1/Pax6* hypothesis from PMID:39837771) remains functionally unvalidated. Per `CLAUDE.md`, `HUMAN_MODEL_MISMATCH` is the right kind here because evidence exists in models but its translational validity is the open question.

### 15.5 Resources

MGI (mouse; MGI:1926033 — verify), IMPC/EUCOMM/KOMP (*Brpf1*^tm1a(EUCOMM)Wtsi, MGI:4433631), IMSR, ZFIN (zebrafish *brpf1*), Alliance of Genome Resources.

---

## Appendix A — Consolidated PMID reference list

**Clinical — foundational**
- **PMID:27939640** — Yan K, Rousseau J, Littlejohn RO, et al. *Mutations in the Chromatin Regulator Gene BRPF1 Cause Syndromic Intellectual Disability and Deficient Histone Acetylation.* Am J Hum Genet. 2017. **[Disease-defining paper #1 — 10 individuals]**
- **PMID:27939639** — Mattioli F, Schaefer E, Magee A, et al. *Mutations in Histone Acetylase Modifier BRPF1 Cause an Autosomal-Dominant Form of Intellectual Disability with Associated Ptosis.* Am J Hum Genet. 2017. **[Disease-defining paper #2 — 3p25/SETD5 dissection]**

**Clinical — cohorts and deep phenotyping**
- **PMID:39837771** — Colson C, et al. *The Phenotypic and Genotypic Spectrum of BRPF1-Related Disorder: 29 New Patients and Literature Review.* Clin Genet. 2025. **[Largest cohort; primary frequency source; PMC11973018]**
- **PMID:38346666** — *Beyond 'speech delay': Expanding the phenotype of BRPF1-related disorder.* Eur J Med Genet. 2024. **[Speech/language deep phenotyping, n=15]**
- **PMID:38590032** — *Broadening the ocular phenotypic spectrum of ultra-rare BRPF1 variants: report of two cases.* Ophthalmic Genet. 2024. **[Subclinical optic neuropathy; Chiari I]**
- **PMID:31020800** — Pode-Shakked N, et al. *BRPF1-associated intellectual disability, ptosis, and facial dysmorphism in a multiplex family.* Mol Genet Genomic Med. 2019.
- **PMID:37190896** — Kose CC, et al. *Anemia and thrombocytopenia due to a novel BRPF1 variant…* Am J Med Genet A. 2023. **[Hematologic expansion]**
- **PMID:35243762** — *BRPF1-associated syndrome: A patient with congenital ptosis, neurological findings, and normal intellectual development.* Am J Med Genet A. 2022. **[Mild end of spectrum]**
- **PMID:32457794** — *Novel Missense Variant in Heterozygous State in the BRPF1 Gene…* Front Genet. 2020.
- **PMID:41137536** — *Non-RASopathy Genetic Syndromes Identified as the Molecular Cause of Disease in Patients Previously Diagnosed With Noonan Syndrome.* Am J Med Genet A. 2026. **[Differential diagnosis]**
- **PMID:33611074** — *Clinically relevant copy-number variants in exome sequencing data of patients with dystonia.* Parkinsonism Relat Disord. 2021. **[BRPF1 CNV detection]**

**Mechanism — molecular**
- **PMID:32010779** — Yan K, et al. *Deficient histone H3 propionylation by BRPF1-KAT6 complexes in neurodevelopmental disorders and cancer.* Sci Adv. 2020. **[H3K23pr; 12 new cases; therapeutic leads]**
- **PMID:36077605** — *BRPF1-KAT6A/KAT6B Complex: Molecular Structure, Biological Function and Human Disease.* Cancers. 2022. **[Review]**
- **PMID:40593219** — *Bromodomain and PHD Finger-Containing Protein 1: From Functions to a Developmental Disorder, Cancer, and Therapeutics.* Results Probl Cell Differ. 2025. **[Most recent dedicated review]**
- **PMID:40593218** — *Lysine Acetyltransferase 6 Complexes in Neurodevelopmental Disorders and Different Types of Cancer.* Results Probl Cell Differ. 2025.
- **PMID:25920810** — Yang XJ. *MOZ and MORF acetyltransferases…* Biochim Biophys Acta. 2015.

**Mechanism — model organism**
- **PMID:31213987** — *Brpf1 Haploinsufficiency Impairs Dendritic Arborization and Spine Formation, Leading to Cognitive Deficits.* Front Cell Neurosci. 2019. **[Best disease-matched model]**
- **PMID:25568313** — *Deficiency of the chromatin regulator BRPF1 causes abnormal brain development.* J Biol Chem. 2015.
- **PMID:34485298** — *Deficiency of Intellectual Disability-Related Gene Brpf1 Attenuated Hippocampal Excitatory Synaptic Transmission…* Front Cell Dev Biol. 2021.
- **PMID:33744924** — *Deficiency of intellectual disability-related gene Brpf1 reduced inhibitory neurotransmission in MGE-derived GABAergic interneurons.* G3. 2021.
- **PMID:27500495** — *BRPF1 is essential for development of fetal hematopoietic stem cells.* J Clin Invest. 2016.
- **PMID:25773539** — *The chromatin regulator Brpf1 regulates embryo development and cell proliferation.* J Biol Chem. 2015.
- **PMID:24646517** — *Expression atlas of the multivalent epigenetic regulator Brpf1…* Epigenetics. 2014.
- **PMID:18469222** — Laue K, et al. *The multidomain protein Brpf1 binds histones and is required for Hox gene expression and segmental identity.* Development. 2008. **[Zebrafish; PWWP histone binding]**
- **PMID:21753189** — *The Hbo1-Brd1/Brpf2 complex … required for fetal liver erythropoiesis.* Blood. 2011. **[Paralog — do not conflate with BRPF1]**
- **PMID:40060486** — *Context-Dependent and Gene-Specific Role of Chromatin Architecture…* bioRxiv 2025. **[Preprint — not peer reviewed]**

**Chemical biology / therapeutics**
- **PMID:26061247** — *Structure-Guided Design of IACS-9571, a Selective High-Affinity Dual TRIM24-BRPF1 Bromodomain Inhibitor.* J Med Chem. 2016.
- **PMID:28849908** — *Selective Targeting of Bromodomains of the Bromodomain-PHD Fingers Family Impairs Osteoclast Differentiation.* ACS Chem Biol. 2017.

**Adjacent / comparison**
- **PMID:37249002** — *DNA methylation episignatures are sensitive and specific biomarkers for detection of patients with KAT6A/KAT6B variants.* **[No BRPF1 episignature — cited as a gap]**

**Non-literature structured sources usable as dismech evidence references:**
- `ORPHA:698090` — Orphanet (definition, prevalence class <1/1,000,000, 79 cases, disorder type)
- `CGDS:HGNC_14255` — ClinGen Dosage Sensitivity (HI score 3, TS score 0, curated 2023-08-23)
- ClinGen Gene-Disease Validity (`CGGV:` — retrieve the specific assertion ID via `just clingen-list | grep BRPF1`)

---

## Appendix B — Curation notes and explicitly flagged gaps

**Things to verify before committing (per `CLAUDE.md` SOP):**
1. Run `just fetch-reference PMID:X` for all ~28 PMIDs above; then `just validate-references` — several quotes above came through a summarizing fetch layer and, while transcribed verbatim on request, must be substring-checked against the real cached abstracts.
2. The Colson 2025 genotype-phenotype sentence was **truncated mid-word** by the extraction tool. Re-read it from PMC11973018 before quoting.
3. gnomAD pLI=1 / LOEUF=0.21 came from a search snippet, **not** from gnomAD directly. Re-verify against gnomAD v4.
4. MGI:1926033 came from a search snippet. Verify at informatics.jax.org.
5. Verify every CL, UBERON, GO, CHEBI, and NCIT ID with `just validate-terms`. The PV-interneuron CL term and the eyeglasses NCIT term are the least certain.
6. The ClinVar "269 P/LP" count includes multi-gene CNVs — do not quote it as BRPF1-specific sequence variants.

**Substantive knowledge gaps worth recording as `discussions` entries:**
- **No BRPF1 DNA-methylation episignature** despite established episignatures for its obligate partners KAT6A/KAT6B (PMID:37249002) — the single highest-value diagnostic gap.
- **No iPSC or cerebral-organoid model** — no human-cell model of the neurodevelopmental phenotype.
- **No animal model of ptosis/blepharophimosis** — the defining human feature is mechanistically unvalidated; the *Pitx2/Hmx1/Pax6* route (PMID:39837771) is inference, not demonstration.
- **No quantitative penetrance estimate**, and no explanation for the intrafamilial variability seen with identical variants — implies unidentified modifiers.
- **No natural history study, no QoL data, no treatment guideline, no clinical trial.**
- **Whether human BRPF1 haploinsufficiency causes clinically meaningful hematologic or immune disease** is unresolved (8% hematologic abnormality vs lethal marrow failure in mouse KO).
- **The mouse-vs-human severity mismatch** (homozygous-null lethality vs normal human lifespan) should be an explicit `HUMAN_MODEL_MISMATCH`, not a `KNOWLEDGE_GAP`.

**Candidate dismech module conformance points:**
- `epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance` — supported by paired excitatory (PMID:34485298) and inhibitory (PMID:33744924) transmission deficits, but the evidence is `MODEL_ORGANISM`/`IN_VITRO` only; seizures occur in a minority. Curate the conformance with that caveat, or not at all.
- A potential new **chromatinopathy / KAT6-BRPF1 complex** module or `Grouping` uniting BRPF1, KAT6A, and KAT6B disorders — they share an obligate protein complex, a common molecular readout (H3K23 acylation), and overlapping phenotypes, which is exactly the `SHARED_MECHANISM` + `SHARED_PATHWAY` grouping basis.
- A **3p25 contiguous deletion** entry or grouping capturing the BRPF1/SETD5 per-gene phenotype attribution (PMID:27939639) — an unusually clean worked example.

---

**Sources:**
- [OMIM 617333 — IDDDFP](https://omim.org/entry/617333)
- [OMIM 602410 — BRPF1](https://omim.org/entry/602410)
- [Orphanet ORPHA:698090](https://www.orpha.net/en/disease/detail/698090)
- [Orphadata API — cross-referencing and epidemiology, ORPHA:698090](https://api.orphadata.com/rd-cross-referencing/orphacodes/698090?lang=en)
- [ClinGen — BRPF1 dosage sensitivity (HGNC:14255)](https://search.clinicalgenome.org/kb/gene-dosage/HGNC:14255)
- [ClinGen — BRPF1 gene page](https://search.clinicalgenome.org/kb/genes/BRPF1)
- [MedGen 934584](https://www.ncbi.nlm.nih.gov/medgen/934584)
- [HPO API — annotations for OMIM:617333](https://ontology.jax.org/api/network/annotation/OMIM:617333)
- [OLS4 — MONDO:0015022](https://www.ebi.ac.uk/ols4/ontologies/mondo/classes?obo_id=MONDO:0015022)
- [UniProt P55201 — Peregrin/BRPF1](https://www.uniprot.org/uniprotkb/P55201)
- [HGNC:14255 — BRPF1](https://rest.genenames.org/fetch/symbol/BRPF1)
- [PubMed — BRPF1 (all abstracts cited above retrieved via NCBI E-utilities)](https://pubmed.ncbi.nlm.nih.gov/?term=BRPF1)
- [PMC11973018 — Colson et al. 2025, Clinical Genetics](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11973018/)
- [ScienceDirect — Beyond 'speech delay': Expanding the phenotype of BRPF1-related disorder](https://www.sciencedirect.com/science/article/pii/S1769721224000156)
- [Science Advances — Deficient histone H3 propionylation by BRPF1-KAT6 complexes](https://www.science.org/doi/10.1126/sciadv.aax0021)
- [MGI — Brpf1 (MGI:1926033)](https://www.informatics.jax.org/marker/MGI:1926033)
- [MGI — Brpf1^tm1a(EUCOMM)Wtsi (MGI:4433631)](https://www.informatics.jax.org/allele/MGI:4433631)
- [PMC9454415 — BRPF1-KAT6A/KAT6B Complex review](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9454415/)
- [PubMed 37249002 — KAT6A/KAT6B episignatures](https://pubmed.ncbi.nlm.nih.gov/37249002/)