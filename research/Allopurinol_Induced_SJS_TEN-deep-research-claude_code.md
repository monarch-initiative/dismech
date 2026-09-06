---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-09-01T08:15:33.916362'
end_time: '2026-09-01T08:32:25.938902'
duration_seconds: 1012.02
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Allopurinol-Induced Stevens-Johnson Syndrome/Toxic Epidermal Necrolysis
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
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-5[1m]
  web_search_requests: 6
  num_turns: 68
  total_cost_usd: 7.009300999999999
  session_id: 44de43a8-574c-450e-9aa7-434c8596e374
  stop_reason: end_turn
  permission_denials: 3
  denied_tools:
  - Bash
  assistant_text_blocks: 1
citation_count: 49
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Allopurinol-Induced Stevens-Johnson Syndrome/Toxic Epidermal Necrolysis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Allopurinol-Induced Stevens-Johnson Syndrome/Toxic Epidermal Necrolysis** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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

# Allopurinol-Induced Stevens–Johnson Syndrome / Toxic Epidermal Necrolysis
### A comprehensive research report for knowledge-base curation

**Compiled:** 2026-09-01 · **Target concept:** allopurinol-induced SJS/TEN (a drug-specific severe cutaneous adverse reaction, SCAR) · **Evidence base:** primary literature via PubMed/E-utilities, ontology lookups via EBI OLS4, trial records via ClinicalTrials.gov API.

> **Framing note up front, because it shapes everything below.** This is not a Mendelian disease with a lesion you can point at in a gene. It's a *drug toxicity* — a pharmacological accident that only happens when a particular small molecule meets a particular immune receptor in a particular person. Think of it less like a broken enzyme and more like a lock that opens for the wrong key: allopurinol's metabolite slips into the groove of an HLA molecule it was never meant to touch, and the T-cell system reads the result as "infected self." Everything downstream — the blisters, the sloughing skin, the mortality — follows from that one molecular mis-recognition.

---

## 1. Disease Information

### 1.1 Overview

Allopurinol-induced SJS/TEN is a **delayed (Type IVc), HLA class I–restricted, CD8+ T-cell–mediated severe cutaneous adverse reaction** in which allopurinol (or, more precisely, its active metabolite **oxypurinol**) triggers widespread keratinocyte death, epidermal detachment, and mucosal erosion. It sits on a severity spectrum defined by body-surface-area (BSA) detachment:

| Entity | Epidermal detachment | Mucosal involvement |
|---|---|---|
| SJS | < 10% BSA | ≥ 2 sites, typical |
| SJS/TEN overlap | 10–30% BSA | ≥ 2 sites, typical |
| TEN | > 30% BSA | ≥ 2 sites, typical |

This BSA-based consensus classification is the Bastuji-Garin scheme (PMID:8420497).

Allopurinol also causes two *sibling* SCAR phenotypes that share the same HLA restriction and the same culprit metabolite but differ in clinical expression: **DRESS/DIHS** (drug reaction with eosinophilia and systemic symptoms) and the older umbrella term **allopurinol hypersensitivity syndrome (AHS)**. Most genetic-association literature reports the pooled endpoint "allopurinol-SCAR" (SJS/TEN + DRESS), which is a real limitation when curating SJS/TEN specifically — flag it in every evidence item drawn from those studies.

**Why allopurinol matters disproportionately:** it is the single most common culprit drug for SJS/TEN in Europe and Israel.

> "Allopurinol was the drug most frequently associated with SJS or TEN, with 66 exposed patients (17.4%) and 28 exposed control subjects (1.9%) (adjusted odds ratio = 18, 95% confidence interval: 11-32)."
> — Halevy et al., EuroSCAR Study Group, *J Am Acad Dermatol* 2008 (**PMID:17919772**)

### 1.2 Key identifiers

| Resource | Identifier | Label / note |
|---|---|---|
| MONDO | `MONDO:0018229` | Stevens-Johnson syndrome |
| MONDO | `MONDO:0019810` | toxic epidermal necrolysis |
| MONDO | `MONDO:0044739` | Stevens-Johnson syndrome/toxic epidermal necrolysis overlap syndrome |
| MONDO | `MONDO:0018890` | Lyell syndrome |
| MONDO | `MONDO:0005594` | severe cutaneous adverse reaction (parent grouping) |
| MeSH | `D013262` | Stevens-Johnson Syndrome — **note:** this single descriptor absorbs "Toxic Epidermal Necrolysis", "Lyell's Syndrome", "Drug-Induced Stevens-Johnson Syndrome", and "Stevens-Johnson Syndrome Toxic Epidermal Necrolysis Spectrum" as entry terms |
| ICD-10 | `L51.1` / `L51.2` / `L51.3` | SJS / TEN / SJS-TEN overlap |
| ICD-10 (external cause) | `T50.4` | poisoning by/adverse effect of drugs affecting uric acid metabolism |
| ICD-11 MMS | `EB13.0` / `EB13.1` / `EB13.2` | SJS / TEN / overlap; block EB13 "Stevens-Johnson syndrome or toxic epidermal necrolysis". Drug-induced variants also code under `EH63` |
| NCIT | `NCIT:C79777` | Toxic Epidermal Necrolysis |
| NCIT (CTCAE) | `NCIT:C143880`, `C146148` (Gr 4), `C146579` (Gr 5) | Toxic Epidermal Necrolysis, CTCAE grading |
| Orphanet | `ORPHA:95455` | Stevens-Johnson syndrome/toxic epidermal necrolysis spectrum — **verify before binding**; the Orphanet portal blocked automated retrieval during this research, so this code is from secondary sources |
| PharmGKB / CPIC | HLA-B*58:01 – allopurinol | Level 1A pharmacogenomic association |

**⚠️ Curation decision flagged:** *there is no MONDO term for "allopurinol-induced SJS/TEN."* No `MONDO:*` concept encodes the drug-specific entity. Options: (a) curate as a drug-toxicity Disease entry anchored to `MONDO:0018229` and/or `MONDO:0019810` via `mappings.mondo_mappings` with `mapping_predicate: skos:narrowMatch`; (b) curate the general SJS/TEN entity and carry allopurinol as an `environmental[]` / exposure-linked mechanism. Option (a) is more consistent with how dismech treats drug-toxicity entries (the "side effect as mechanism" module family), but the call belongs in the design register.

### 1.3 Synonyms and alternative names

- Allopurinol hypersensitivity syndrome (AHS) — **broader**; includes DRESS and non-SCAR rashes
- Allopurinol-induced SCAR / allopurinol-SCAR — **broader**; pooled SJS/TEN + DRESS endpoint used in most genetics papers
- Allopurinol-induced epidermal necrolysis (EN) — the RegiSCAR-preferred umbrella for SJS + overlap + TEN
- Allopurinol-induced Lyell syndrome (chiefly for the TEN pole)
- Drug-induced Stevens-Johnson syndrome (MeSH entry term)

### 1.4 Data provenance — patient-level vs aggregated

Both, and the distinction matters for evidence grading:

- **Individual-patient (EHR/registry-derived):** the RegiSCAR and EuroSCAR case–control networks; the Taiwan Allopurinol-SCAR Consortium prospective cohort (PMID:26399967); Vanderbilt BioVU–linked SJS/TEN Survivor Study (PMID:41160012); Ontario ICES administrative-claims cohort (PMID:35644439); Taiwan NHIRD (PMID:39969876); Danish national registries (PMID:42467870).
- **Aggregated disease-level:** CPIC/PharmGKB guideline annotations, Orphanet, MeSH/ICD, and pooled meta-analyses of HLA association.
- **Mechanistic:** ex vivo patient PBMC and blister-cell work — individual-patient biospecimens, small n (typically 5–25 cases per study).

---

## 2. Etiology

### 2.1 Primary causal factors

The disease is **obligately two-hit**: it requires (i) exposure to allopurinol and accumulation of oxypurinol, and (ii) a permissive HLA class I background — plus, almost always, (iii) a naive T-cell repertoire containing clonotypes capable of reading the drug–HLA complex.

**Necessary exposure:** allopurinol (CHEBI:40279), a xanthine oxidase inhibitor used for gout, hyperuricemia, tumor lysis prophylaxis, and (often inappropriately) asymptomatic hyperuricemia. Allopurinol is rapidly converted in vivo to **oxypurinol** (CHEBI:748196; also indexed as alloxanthine, CHEBI:28315), which has a long half-life and is **renally cleared** — the pivot on which most of the risk architecture turns.

**Dose- and time-dependence** (unusual for a Type B idiosyncratic reaction, and one of the most curation-relevant facts here):

> "Daily doses equal to or greater than 200 mg were associated with a higher risk (adjusted odds ratio = 36, 95% confidence interval: 17-76) than lower doses (adjusted odds ratio = 3.0, 95% confidence interval: 1.1-8.4). The risk was restricted to short-term use (<or=8 weeks)."
> — Halevy et al. 2008 (**PMID:17919772**)

> "Despite the prevailing dogma that Type B adverse drug reactions are dose independent, allopurinol hypersensitivity is primarily driven by oxypurinol-specific T cell response in a dose-dependent manner, particular in the presence of HLA-B*58:01 allele."
> — Yun et al., *Clin Exp Allergy* 2013 (**PMID:24152157**)

### 2.2 Genetic risk factors

#### HLA-B*58:01 — the dominant locus

Discovered in Han Chinese in a candidate-SNP screen that landed squarely in the MHC:

> "The HLA-B*5801 allele was present in all (100%) 51 patients with allopurinol-SCAR, but only in 20 (15%) of 135 tolerant patients [odds ratio 580.3 (95% confidence interval, 34.4-9780.9); corrected P value = 4.7 x 10(-24)]"
> — Hung et al., *PNAS* 2005 (**PMID:15743917**)

The same paper notes the risk allele sits on an extended haplotype: "HLA alleles A*3303, Cw*0302, and DRB1*0301 were in linkage disequilibrium and formed an extended haplotype with HLA-B*5801" — relevant because tag-SNP proxies (e.g. rs3131003, rs9263726, PSORS1C1) are used in some screening programs and are LD-based, not causal (PMID:41846573).

Effect size is **strongly ancestry-dependent** and weaker outside East Asia. A second, independent, Taiwanese cohort estimate:

> "HLA-B*58:01 was strongly associated with allopurinol-SCAR (p<0.001, OR (95% CI) 109 (25 to 481))"
> — Chung et al., *Ann Rheum Dis* 2015 (**PMID:25115449**)

And a modern range across phenotype severity:

> "Individuals who carry the human leukocyte antigen (HLA)-B*58:01 allotype are at higher risk of experiencing a hypersensitivity reaction (odds ratios ranging from 5.62 to 580.3 for mild to severe reactions, respectively)."
> — Mifsud et al., *Allergy* 2023 (**PMID:37452515**)

#### HLA-A*34:02 — a newly identified second independent locus (2025)

This is the most important recent genetic development, and it directly undercuts single-allele screening in admixed populations:

> "Two HLA class I alleles were found to be independently associated with increased risk of allopurinol-induced SCAR: HLA-B*58:01 (OR, 28.0 [95% CI, 8.6-100.6]) and HLA-A*34:02 (OR, 20.6 [95% CI, 3.3-131.1]). No HLA class II alleles meeting the Bonferroni-corrected P < .05 level of significance were identified."
> — Campbell et al., *JAMA Dermatol* 2025 (**PMID:41160012**; preprint **PMID:40475155**)

> "the allele was absent in more than one-third of the patient cohort and is therefore an incomplete indicator of risk"
> — same source

Caveats to record with this finding: n = 16 cases, primarily self-identified Black race, single-center, HLA imputed from genotyping array in controls. Treat `HLA-A*34:02` as `SUSCEPTIBILITY`, not `CAUSATIVE`, and mark the evidence `directness: DIRECT` but note the small cohort.

#### Other reported HLA associations (weaker / not replicated)

- `HLA-DR9`, `HLA-DR14` in allopurinol hypersensitivity arising in hematologic malignancy (Korean cohort, PMID:24858023) — class II, unreplicated.
- In a Turkish DRESS cohort, `HLA-B*58:01` co-occurred with other risk alleles in multiple-drug-hypersensitivity syndrome (PMID:42014364).

#### Penetrance is low — this is the single most misused number in the field

Carrying HLA-B*58:01 is **necessary-ish but nowhere near sufficient**. Population frequencies (see §9) put carriers at 10–20% of Han Chinese, while allopurinol-SCAR incidence is ~0.3%/year of treated patients. The allele is a permissive background, not a determinant.

### 2.3 Environmental / clinical (non-genetic) risk factors

| Factor | Effect | Evidence |
|---|---|---|
| **Renal impairment / CKD** | OR 8.0 (3.9–17) for allopurinol-SCAR; drives oxypurinol accumulation and delayed clearance | PMID:25115449 |
| **Starting dose > 100 mg/day in CKD** | RR 2.25 (1.50–3.37); 0.40% vs 0.18% at 180 days | PMID:35644439 |
| **Daily dose ≥ 200 mg** | aOR 36 (17–76) vs aOR 3.0 (1.1–8.4) below | PMID:17919772 |
| **First 8 weeks of therapy** | Risk essentially confined to this window | PMID:17919772 |
| **Advanced age** | SCORTEN component (> 40 y); most cohorts are 60s–70s | PMID:10951229; PMID:41160012 (mean 61.1 y) |
| **Concurrent thiazide diuretics** | Long-standing clinical suspicion; **not supported** by EuroSCAR — "The use of comedications did not increase the risk" | PMID:17919772 (negative finding — curate as `REFUTE`) |
| **Prescribing for asymptomatic hyperuricemia** | Exposure without benefit; a health-systems risk multiplier rather than a biological one | ACR guideline conditionally recommends *against* ULT for asymptomatic hyperuricemia, PMID:32390306 |

The Ontario CKD result is the cleanest actionable statement in the whole risk literature:

> "Older patients with CKD who started allopurinol at >100 mg/d versus ≤100 mg/d were twice as likely to visit a hospital with a severe cutaneous reaction in the next 180 days."
> — Bathini et al., *Am J Kidney Dis* 2022 (**PMID:35644439**)

### 2.4 Protective factors

- **Non-carriage of HLA-B*58:01** — the dominant protective state, but explicitly incomplete (PMID:41160012).
- **Low starting dose with slow titration** (≤100 mg/day, lower in CKD), strongly recommended by ACR 2020 (PMID:32390306). Mechanistically coherent: the T-cell response is oxypurinol-concentration-dependent (PMID:24152157).
- **Substituting a structurally unrelated xanthine oxidase inhibitor.** Febuxostat does not cross-react with oxypurinol-specific T cells:
  > "Oxypurinol induced T-cell response in a concentration- and time-dependent manner, whereas allopurinol or febuxostat did not. T cells from patients with allopurinol-SCAR showed no crossreactivity with febuxostat."
  > — Chung et al., *J Invest Dermatol* 2015 (**PMID:25946710**)
- **Prospective HLA-B*58:01 screening** — demonstrated preventive effect (see §13).
- No **genetic protective variant** has been characterized. Not applicable / no data.

### 2.5 Gene–environment interaction

This disease *is* a gene–environment interaction; the two axes are not separable. Three interacting dimensions are documented:

1. **HLA genotype × drug concentration.** "TCL induction data show that both the presence of HLA-B*58:01 allele and high concentration of drug are important for the generation of drug-specific T cells… functional avidity of ALP/OXP-TCL is dependent on both the induction dose and HLA-B*58:01 status." (PMID:24152157)
2. **HLA genotype × renal function.** Impaired eGFR → oxypurinol accumulation → higher effective drug concentration at the HLA groove. "Poor renal function was significantly associated with the delayed clearance of plasma oxypurinol, and increased the risk of allopurinol-SCAR" (PMID:25115449). This is a *pharmacokinetic* GxE, not a pharmacodynamic one.
3. **HLA genotype × TCR repertoire.** Even among carriers, the responding clonotypes are private — see §6.

---

## 3. Phenotypes

### 3.1 Prodromal / constitutional

| Phenotype | HP term | Onset | Frequency | Notes |
|---|---|---|---|---|
| Fever | `HP:0001945` Fever | 1–3 d before skin lesions | Very frequent (~85–95%) | SCORTEN uses tachycardia, not fever |
| Malaise / influenza-like prodrome | `HP:0033834` (Malaise) — verify | Prodromal | Frequent | |
| Painful skin / burning eyes | `HP:0025280` (Pain) + `HP:0000613` (Photophobia) | Prodromal | Frequent | Skin *pain out of proportion to visible lesion* is the classic early red flag |

### 3.2 Cutaneous — the defining phenotypes

| Phenotype | HP term | Severity | Course | Frequency |
|---|---|---|---|---|
| **Skin detachment** (epidermal detachment / sloughing) | `HP:0032156` **Skin detachment** | Defines the SJS↔TEN axis | Rapidly progressive over 2–5 d, then re-epithelializes | 100% (definitional) |
| Cutaneous bullae / blistering | `HP:0008066` Abnormal blistering of the skin; `HP:0200037` Skin vesicle | Moderate–severe | Progressive then resolving | Very frequent |
| Skin erosion | `HP:0200041` **Skin erosion** | Severe | Acute, self-limited | Very frequent |
| Erythroderma / dusky macules with atypical targets | `HP:0001019` Erythroderma | Variable | Acute | Very frequent |
| Positive Nikolsky sign | **No HP term identified** — free-text `preferred_term`, no `term:` binding | Sign, not symptom | Acute phase | Frequent |

> ⚠️ **Ontology gap.** OLS4 returned no HP term for "Nikolsky sign." Per the dismech term contract, leave `term:` absent rather than binding a near-miss; *no term beats a bad one*.

### 3.3 Mucosal

| Phenotype | HP term | Frequency |
|---|---|---|
| Oral mucosal blisters/erosions | `HP:0200097` **Oral mucosal blisters** | ~90%+ |
| Conjunctivitis / ocular surface erosion | `HP:0000509` Conjunctivitis (verify) | ~60–80% acute |
| Genital / urethral erosion | free-text; consider `HP:0000130` Abnormality of the female genitalia — poor fit, likely leave unbound | Frequent |
| Tracheobronchial epithelial sloughing | free-text | Uncommon but prognostically severe |

At least two mucosal sites are required by the consensus definition (PMID:8420497).

### 3.4 Systemic / laboratory

| Phenotype | HP / LOINC | Note |
|---|---|---|
| Elevated serum urea (> 10 mmol/L) | `HP:0003138` Increased blood urea nitrogen; LOINC 3094-0 | SCORTEN component |
| Hyperglycemia (> 14 mmol/L) | `HP:0003074` Hyperglycemia; LOINC 2345-7 | SCORTEN component |
| Serum bicarbonate < 20 mmol/L | `HP:0002913`-adjacent; LOINC 1963-8 | SCORTEN component |
| Tachycardia > 120 bpm | `HP:0001649` Tachycardia | SCORTEN component |
| Eosinophilia | `HP:0001880` Eosinophilia | More characteristic of the DRESS sibling phenotype than of SJS/TEN |
| Elevated transaminases / drug-induced liver injury | `HP:0002910` Elevated hepatic transaminase | Common in allopurinol-SCAR broadly |
| Acute kidney injury | `HP:0001919` Acute kidney injury | Both a risk factor *and* a consequence — model both directions |
| Electrolyte disturbance | `HP:0003111` Abnormal blood ion concentration | 81.7% in a 213-patient SJS/TEN series (PMID:31898979) |

### 3.5 Onset timing, severity, and course

- **Latency:** typically **2–8 weeks** after allopurinol initiation; EuroSCAR restricts the risk window to ≤8 weeks (PMID:17919772). This is *longer* than the ~1-week latency typical of antiseizure-drug SJS/TEN and is a useful discriminator for ALDEN causality scoring.
- **Onset pattern:** acute, but with a subacute prodrome.
- **Severity:** severe by definition; graded by SCORTEN (§10) and BSA.
- **Progression:** rapidly progressive over days, then plateau, then re-epithelialization over ~2–3 weeks. Self-limited *if* the drug is withdrawn — but re-exposure can be worse and is potentially fatal.
- **Duration:** the acute episode is self-limited; the sequelae are lifelong (§11).

### 3.6 Quality-of-life impact

Acute phase: intensive/burn-unit-level care, severe pain, inability to eat or open eyes. Survivor phase carries substantial and durable burden — chronic ocular surface disease (dry eye, symblepharon, corneal opacification, blindness), cutaneous dyspigmentation and scarring, nail dystrophy, genital adhesions, chronic pruritus, and post-traumatic stress. Disease-specific QoL instrument data (EQ-5D / SF-36 / DLQI) for **allopurinol-specific** SJS/TEN was **not identified** in this search; general SJS/TEN survivor QoL literature exists but was not retrieved in a form suitable for quoting. **Gap — flag as `KNOWLEDGE_GAP`.**

---

## 4. Genetic / Molecular Information

### 4.1 There are no causal genes in the Mendelian sense

This is a pharmacogenomic susceptibility trait, not a monogenic disease. **No pathogenic variants, no ACMG/AMP classification, no gnomAD pathogenic allele frequency, no somatic/germline distinction, no chromosomal abnormality.** All of these template sub-items are **not applicable**.

What exists instead is an **HLA allelic risk architecture**: common, functionally normal MHC alleles that happen to have a peptide-binding groove chemistry permissive to oxypurinol.

### 4.2 Susceptibility loci

| Gene | HGNC | Allele | Role | Evidence |
|---|---|---|---|---|
| **HLA-B** | `hgnc:4932` | `HLA-B*58:01` | Principal susceptibility allele; restricts oxypurinol presentation | PMID:15743917, PMID:24591375, PMID:25115449, PMID:41160012 |
| **HLA-A** | `hgnc:4931` | `HLA-A*34:02` | Second independent susceptibility allele (US, admixed) | PMID:41160012 |
| **HLA-A / HLA-C / HLA-DRB1** | — | `A*33:03`, `Cw*03:02`, `DRB1*03:01` | Extended-haplotype LD partners of B*58:01 — **not independently causal** | PMID:15743917 |
| *(tag SNP)* | — | `rs3131003` | Moderate LD proxy for HLA-B*58:01, used in Korean risk prioritization | PMID:41846573 |
| *(tag SNP)* | — | `rs9263726` (PSORS1C1) | Reported proxy in gout cohorts | secondary source; verify before curating |

**Curation note on relationship types:** use `relationship_type: SUSCEPTIBILITY` for all of these. None is `CAUSATIVE`. `Inheritance`: this is not an inherited disease — but the *susceptibility* is inherited codominantly as an HLA allele. If an `inheritance:` block is added at all, `HP:0010982` (Polygenic inheritance) is a poor fit; a free-text description of HLA-allelic susceptibility with no `term:` binding is the honest choice.

### 4.3 Genes central to the effector mechanism (not risk genes)

These belong in `pathophysiology` nodes, **not** in `genetic:`:

| Gene | HGNC | Role |
|---|---|---|
| `GNLY` (granulysin) | `hgnc:4414` | Dominant cytotoxic effector in blister fluid |
| `ANXA1` (annexin A1) | `hgnc:533` | Monocyte-derived necroptosis trigger |
| `FPR1` | `hgnc:3826` | Annexin A1 receptor on keratinocytes |
| `RIPK1` | `hgnc:10019` | Necrosome |
| `RIPK3` | `hgnc:10021` | Necrosome, phosphorylates MLKL |
| `MLKL` | `hgnc:26617` | Pore-forming executioner of necroptosis |
| `FASLG` | `hgnc:11936` | Fas-ligand apoptosis arm |
| `PRF1` / `GZMB` | `hgnc:9360` / `hgnc:4709` | Perforin/granzyme cytotoxicity |
| `TNF` | `hgnc:11892` | Etanercept's target; elevated in lesional skin |
| `CXCL10` | `hgnc:10637` | Macrophage-derived CTL chemoattractant (shown in ICI-SJS/TEN — *not yet demonstrated for allopurinol*) |
| `XDH` (xanthine dehydrogenase/oxidase) | `hgnc:12805` | Allopurinol's *therapeutic* target — irrelevant to the toxicity mechanism, which is the whole point |

That last row deserves emphasis for the causal graph: **the toxicity has nothing to do with the drug's intended pharmacology.** Xanthine oxidase inhibition and HLA-B*58:01 binding are two entirely separate molecular events that happen to involve the same molecule. This is why febuxostat — same target, different scaffold — is safe in these patients.

### 4.4 Modifier genes, epigenetics, chromosomal abnormalities

- **Modifier genes:** none characterized. The functional modifier is the *TCR repertoire*, which is somatically generated rather than germline-encoded (§6).
- **Epigenetics:** no DNA-methylation or histone-modification data specific to allopurinol-SJS/TEN was identified. **Not available.**
- **Chromosomal abnormalities:** not applicable.

---

## 5. Environmental Information

- **The obligate environmental factor is a drug exposure.** Model as an `environmental[]` entry with `influences_mechanisms` and `environmental_effect: TRIGGERS`. ECTO has exposure-to-chemical patterns; a specific "exposure to allopurinol" term was not confirmed in this search — check `cache/ecto/terms.csv` and run `just environmental-term-audit` before assuming a gap. If unbound, record the search in `review_notes:` per the `check-environmental-evidence` waiver convention.
- **Modifying environmental/clinical exposures:** renal impairment (from any cause), high initiation dose, concurrent illness. Diuretic co-medication was *tested and not supported* (PMID:17919772).
- **Lifestyle factors:** no independent effect established. Gout's own lifestyle determinants (alcohol, purine-rich diet, obesity) act only by increasing the probability of allopurinol prescription — an indirect, non-mechanistic path. Do not draw a causal edge.
- **Infectious agents:** **not applicable** to the allopurinol-induced form. (Contrast: *Mycoplasma pneumoniae* causes a distinct mucocutaneous entity, MIRM, which is a differential — see §10.) Herpesvirus reactivation (HHV-6, EBV, CMV) is a feature of **DRESS**, not of SJS/TEN, and should not be imported into this entry.

---

## 6. Mechanism / Pathophysiology

### 6.1 The causal chain, step by step

> Read this as a relay race where each runner hands off to the next. Steps 1–5 are the *sensitization/recognition* leg; steps 6–10 are the *execution* leg; step 11 is what you see at the bedside.

1. **Allopurinol is ingested and rapidly metabolized to oxypurinol** by xanthine oxidase. Oxypurinol has a long half-life and is renally cleared. → *leads to* a systemic oxypurinol burden proportional to dose and inversely proportional to eGFR. *(Demonstrated: PMID:24152157, PMID:25115449.)*

2. **Renal impairment or high dosing raises the steady-state oxypurinol concentration.** → *results in* sufficient local drug concentration at the antigen-presenting cell surface to occupy HLA grooves. *(Demonstrated in humans: "Poor renal function was significantly associated with the delayed clearance of plasma oxypurinol, and increased the risk of allopurinol-SCAR (p<0.001, OR (95% CI) 8.0 (3.9 to 17))" — PMID:25115449.)*

3. **Oxypurinol binds non-covalently and reversibly into the peptide-binding groove of HLA-B\*58:01.** This is the **p-i (pharmacological interaction with immune receptors)** mechanism — no hapten, no covalent adduct, no antigen processing required. → *leads to* an altered peptide/HLA surface.

   > "ALP/OXP-specific T cells reacted immediately to the addition of the drugs and bypassed intracellular Ag processing, which is consistent with the 'pharmacological interaction with immune receptors' (p-i) concept."
   > — Yun et al., *J Immunol* 2014 (**PMID:24591375**)

   > "this response supported the pharmacological interaction with immune receptors (p-i) concept by showcasing (i) the labile metabolite interaction with peptide/HLA complexes, (ii) immunogenic complex formation at the cell surface, and (iii) lack of requirement for antigen processing to elicit drug-induced T cell responsiveness."
   > — Mifsud et al., *Allergy* 2023 (**PMID:37452515**)

4. **BRANCH — a partly complementary "altered peptide repertoire" mechanism.** Structural work shows the drug can also *enable* self-peptides that would otherwise not bind at all:

   > "a Lamin A/C peptide KAGQVVTI which is unable to bind HLA-B*58:01 on its own, is enabled to form a stable peptide-HLA complex only in the presence of allopurinol. Crystal structure analysis reveal that allopurinol non-covalently facilitated KAGQVVTI to adopt an unusual binding conformation, whereby the C-terminal isoleucine does not engage as a PΩ that typically fit deeply in the binding F-pocket."
   > — Huan et al., *Sci Rep* 2023 (**PMID:37296297**)

   The authors extend this to viral peptide (EBNA3B) presentation and propose the result is **anti-self reactivity**: "aberrant loading of unconventional peptides in the presence of allopurinol or oxypurinol may be able to trigger anti-self reactions that can lead to Stevens-Johnson syndrome/toxic epidermal necrolysis." *(Structural/in vitro — mark `evidence_source: IN_VITRO`, and note the two branches are not mutually exclusive; the field has not settled which dominates in vivo. Good candidate for a `mechanistic_hypotheses` group with `status: EMERGING`.)*

5. **Drug-modified pHLA complexes are read by CD8+ T cells bearing specific, private, oligoclonal αβTCRs.** → *results in* immediate T-cell activation without a processing delay.

   > "Preferential TCR-V-β usage and clonal expansion of specific CDR3 (third complementarity-determining region) were found in the blister cells from skin lesions (n=8) and oxypurinol-activated T-cell cultures (n=4) from patients with allopurinol-SCAR."
   > — Chung et al., *J Invest Dermatol* 2015 (**PMID:25946710**)

   > "Examination of paired OXP-induced αβTCR repertoires highlighted an oligoclonal and private clonotypic profile in both resolved ALP-induced SJS/TEN cases and drug-naïve healthy donors."
   > — Mifsud et al. 2023 (**PMID:37452515**)

   Note the striking implication of that last clause: **drug-naive healthy donors already carry the responsive clonotypes.** The repertoire is not the bottleneck; the drug concentration and the HLA are.

6. **Activated drug-specific CD8+ CTLs (and NK/NKT cells) traffic to skin and mucosa** and accumulate in the subepidermal blister space. → *leads to* a local cytotoxic milieu.

7. **CTL/NK degranulation releases granulysin as the dominant soluble killer.** → *results in* keratinocyte death **without requiring cell–cell contact**, which is what makes the damage *disseminated* rather than focal.

   > "Granulysin concentrations in the blister fluids were two to four orders of magnitude higher than perforin, granzyme B or soluble Fas ligand concentrations, and depleting granulysin reduced the cytotoxicity. Granulysin in the blister fluids was a 15-kDa secretory form, and injection of it into mouse skin resulted in features mimicking SJS-TEN."
   > — Chung et al., *Nat Med* 2008 (**PMID:19029983**)

8. **BRANCH — a parallel monocyte-driven necroptosis arm.** Drug-exposed monocytes secrete annexin A1, which engages FPR1 on keratinocytes:

   > "Mass spectrometric analysis identified annexin A1 as a key mediator of keratinocyte death; depletion of annexin A1 by a specific antibody diminished supernatant cytotoxicity. The necroptosis-mediating complex of RIP1 and RIP3 was indispensable for SJS/TEN supernatant-induced keratinocyte death, and SJS/TEN keratinocytes expressed abundant formyl peptide receptor 1 (FPR1), the receptor for annexin A1, whereas control keratinocytes did not."
   > — Saito et al., *Sci Transl Med* 2014 (**PMID:25031270**)

   → *leads to* RIPK1/RIPK3 necrosome assembly, MLKL phosphorylation, membrane rupture. **Note:** this work used SJS/TEN broadly, not allopurinol specifically — grade accordingly and say so in the `explanation`.

9. **Auxiliary arms:** Fas/FasL-mediated apoptosis, perforin/granzyme B, and TNF-α. TNF-α is the arm with the strongest therapeutic validation (§12). Macrophage-derived CXCL10 recruiting CXCR3+ CTLs has been demonstrated in **immune-checkpoint-inhibitor**-induced SJS/TEN (PMID:39737932) — mechanistically attractive, but **not yet shown for allopurinol**. Curate as `KNOWLEDGE_GAP` or `mechanistic_hypotheses`, not as established.

10. **Massive keratinocyte apoptosis + necroptosis → full-thickness epidermal necrosis** → *results in* loss of dermal–epidermal adhesion, sub-epidermal cleavage, Nikolsky-positive sloughing.

11. **Loss of the epidermal barrier → the clinical syndrome:** fluid and electrolyte loss, thermoregulatory failure, protein catabolism, and a wide-open portal for sepsis — which is what actually kills most patients.

12. **Feedback loop worth modeling explicitly:** sustained oxypurinol levels after drug withdrawal keep feeding step 3. "Sustained high levels of oxypurinol after allopurinol withdrawal correlated with the poor prognosis of allopurinol-SCAR." (PMID:25115449). This is the mechanistic rationale for the (unproven) proposal to actively enhance oxypurinol clearance — the same paper: "An early intervention to increase the clearance of plasma oxypurinol may improve the prognosis of allopurinol-SCAR."

### 6.2 Suggested GO / CL / UBERON terms for pathophysiology nodes

| Node concept | GO / CL / UBERON |
|---|---|
| Antigen presentation via MHC class I | `GO:0019885` antigen processing and presentation of endogenous peptide antigen via MHC class I — *use with care; the p-i mechanism explicitly **bypasses** processing.* Consider leaving unbound or using a peptide-antigen-binding term instead |
| T cell receptor signaling | `GO:0050852` T cell receptor signaling pathway |
| T-cell-mediated cytotoxicity | `GO:0001913` T cell mediated cytotoxicity; `GO:0001916` positive regulation of T cell mediated cytotoxicity |
| Keratinocyte apoptosis | `GO:0097283` **keratinocyte apoptotic process**; `GO:1902174` positive regulation of keratinocyte apoptotic process |
| Necroptosis | `GO:0070266` **necroptotic process**; `GO:0060545` positive regulation of necroptotic process; `GO:1901026` ripoptosome assembly involved in necroptotic process |
| CD8+ cytotoxic T cell | `CL:0000794` CD8-positive, alpha-beta cytotoxic T cell |
| Keratinocyte | `CL:0000312` keratinocyte; `CL:4052061` epidermal keratinocyte; `CL:0002187` basal cell of epidermis |
| Monocyte / macrophage | `CL:0000576` monocyte; `CL:0000235` macrophage (verify) |
| NK cell | `CL:0000623` natural killer cell (verify) |
| Epidermis | `UBERON:0001003` skin epidermis; `UBERON:0002025` stratum basale of epidermis |

### 6.3 Molecular profiling

- **Transcriptomics:** the granulysin discovery came from gene-expression profiling of blister cells (PMID:19029983). scRNA-seq of SJS/TEN lesional skin exists for **ICI-induced** (PMID:39737932) and **PD-1-inhibitor-induced** (PMID:41418419) disease. **No published single-cell atlas of allopurinol-specific SJS/TEN lesions was identified.** Genuine, curatable gap.
- **Proteomics:** mass spectrometry of PBMC supernatant identified annexin A1 (PMID:25031270).
- **Immune repertoire sequencing:** next-generation TCR sequencing of blister cells and drug-stimulated cultures (PMID:25946710); paired single-cell αβTCR sequencing (PMID:37452515).
- **Structural biology:** X-ray crystallography of allopurinol/oxypurinol–HLA-B*58:01–peptide ternary complexes (PMID:37296297). Also in silico docking showing oxypurinol binds the HLA-B*58:01 groove with higher affinity than allopurinol (PMID:24591375, `evidence_source: COMPUTATIONAL`).
- **Metabolomics / lipidomics:** none identified. **Not available.**
- **Functional genomics screens (CRISPR/RNAi):** none identified for this disease. **Not available.**

---

## 7. Anatomical Structures Affected

### Organ level
- **Primary:** skin (`UBERON:0002097` skin of body) and stratified squamous mucosae — oral (`UBERON:0000165` mouth), ocular surface / conjunctiva (`UBERON:0001811` conjunctiva), genital, anal, and in severe cases tracheobronchial and esophageal epithelium.
- **Secondary:** kidney (AKI, both risk factor and complication), liver (transaminitis), lung (bronchiolitis obliterans, ARDS), bone marrow (cytopenias), cardiovascular system (long-term — see §11).
- **Body systems:** integumentary (primary), immune (driver), ocular/visual, gastrointestinal, respiratory, renal, cardiovascular.

### Tissue and cell level
- **Tissue:** stratified squamous epithelium — full-thickness epidermal necrosis with a **sparse** dermal inflammatory infiltrate. The mismatch between the tiny number of infiltrating cells and the enormous amount of dead epidermis is precisely what the soluble-mediator model (granulysin, annexin A1) was invented to explain.
- **Cells targeted:** keratinocytes (`CL:0000312`; `CL:4052061` epidermal keratinocyte; `CL:0002187` basal cell of epidermis).
- **Cells driving:** CD8+ cytotoxic T cells (`CL:0000794`), NK cells, NKT cells, monocytes/macrophages.

### Subcellular level
- **Plasma membrane** (`GO:0005886`) — where the drug–pHLA complex forms, where FPR1 sits, and where phospho-MLKL executes.
- **Endoplasmic reticulum** (`GO:0005783`) — conventional peptide loading; *notably bypassed* in the p-i model.
- **Cytosol** (`GO:0005829`) — necrosome assembly.
- **Mitochondrion** (`GO:0005739`) — intrinsic apoptotic arm.

### Localization and laterality
- **Bilateral and symmetric**, characteristically starting on the face and upper trunk and spreading centrifugally. Palms and soles are frequently involved; the scalp is typically spared. Lesions are **not** dermatomal or unilateral — asymmetry should prompt reconsidering the diagnosis.

---

## 8. Temporal Development

- **Age of onset:** adult to geriatric, tracking the age distribution of gout and CKD. Mean 61.1 y (SD 12.6) in the US SCAR cohort (PMID:41160012); median 76 y in the Ontario CKD allopurinol-initiator cohort (PMID:35644439). Pediatric cases are exceptional.
- **Onset pattern:** subacute prodrome (1–3 d) → acute explosive cutaneous phase.
- **Latency from drug start:** typically 2–8 weeks; EuroSCAR found risk "restricted to short-term use (≤8 weeks)" (PMID:17919772). Longer than for antiseizure drugs.
- **Stages:**
  1. *Prodromal* — fever, malaise, skin pain, ocular grittiness.
  2. *Acute/progressive* — 2–5 days of expanding erythema, blistering, detachment. Maximal BSA usually by day 5–7.
  3. *Plateau/nadir* — sepsis and multi-organ risk peak.
  4. *Re-epithelialization* — median 14–19 days depending on treatment (PMID:29400697).
  5. *Chronic sequelae* — lifelong (§11).
- **Progression rate:** rapid (days).
- **Course:** monophasic and self-limited **if the drug is stopped**; not relapsing-remitting. Recurrence requires re-exposure — and is typically more severe.
- **Remission:** treatment-independent resolution follows drug withdrawal; no spontaneous remission while the drug continues. Because oxypurinol clearance is slow in CKD, "withdrawal" is not instantaneous at the tissue level (PMID:25115449).
- **Critical intervention window:** the earliest possible drug withdrawal. Every hour of continued exposure is more antigen. Beyond that, the therapeutic window for immunomodulation is the first few days of the acute phase.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

**Denominators worth keeping straight** — SJS/TEN overall vs. allopurinol-attributable vs. per-initiator risk:

| Measure | Estimate | Source |
|---|---|---|
| SJS/TEN incidence, general population | ~1–2 per million per year (classical estimate); a contemporary Danish 90-day background risk of **0.17 per 100,000 individuals (95% CI 0.16–0.18)** | PMID:42467870 |
| Allopurinol share of all SJS/TEN in Europe/Israel | **17.4%** of cases (66/379) — the single most common culprit | PMID:17919772 |
| Allopurinol-SCAR incidence in treated Taiwanese patients | **0.30% per year (95% CI 0.28–0.31%)** — i.e. ~300 per 100,000 treated patients per year | PMID:26399967 |
| Severe cutaneous reaction within 180 d, older CKD patients starting > 100 mg/d | **0.40%** (vs 0.18% at ≤100 mg/d) | PMID:35644439 |
| SCAR cases avoidable by HLA screening (Thai model) | 1.554 SJS/TEN cases and 0.140 deaths per 1,000 patients tested | PMID:40829930 |

> **Note the two-orders-of-magnitude gap** between the general-population SJS/TEN rate and the rate among allopurinol initiators. That gap *is* the drug effect.

### 9.2 Inheritance

- **Inheritance pattern:** not a heritable disease. The **susceptibility allele** HLA-B*58:01 is inherited codominantly at the HLA-B locus. Most reported cases are heterozygous — in Thai patients, "96.7% of patients with allopurinol-induced cutaneous adverse drug reactions were found to be heterozygous for HLA-B*58:01." Do **not** bind an HPO mode-of-inheritance term to this entry.
- **Penetrance:** very low and jointly conditioned on drug exposure, dose, and renal function. Carriers who never take allopurinol never manifest.
- **Expressivity:** highly variable — the *same* allele and the *same* drug yield mild rash, DRESS, SJS, or TEN in different people. What determines which is not known. **Genuine `KNOWLEDGE_GAP`.**
- **Anticipation, germline mosaicism, consanguinity:** **not applicable.**
- **Carrier frequency:** see allele frequencies below — but "carrier" is a misnomer here; these are common functional HLA alleles, not recessive disease alleles.

### 9.3 Population demographics and geography

**HLA-B*58:01 allele/carrier frequency by ancestry** (figures are a synthesis across sources; the authoritative consolidated dataset is Zhou et al. 2021, which pooled HLA genotypes from 3.5–6.4 million individuals across up to 74 countries, **PMID:32535895**):

| Population | Approximate frequency |
|---|---|
| Han Chinese | ~10–20% |
| Thai | ~6–8% (up to ~9%) |
| Korean | ~6–12% |
| Indonesian | ~11% |
| African American / Black | ~3–6% |
| European / White | ~1–2% (< 0.5% in Belgium and Ireland to ~2% in Italy) |

> "We find major ethnogeographic differences in risk allele prevalence, which translated into pronounced differences in the number of patients needed to test to prevent one case of severe hypersensitivity reactions between countries and populations… Testing of HLA-B*58:01 is more likely to be cost-effective throughout Africa and Asia compared with Europe and the Americas."
> — Zhou et al., *Clin Pharmacol Ther* 2021 (**PMID:32535895**)

**Ancestry-dependence of the association strength** is separate from allele frequency and is the more important curation point. HLA-B*58:01 accounts for essentially **100% of cases in Han Chinese** but only **~55–64% in Northern and Southern European** cohorts, and was **absent in more than one third** of a US cohort of predominantly self-identified Black patients (PMID:41160012). The Portuguese cohort study (PMID:23600531) confirmed a real but weaker association in a European population.

**Sex ratio:** roughly balanced. US SCAR cohort: 9 female (56.25%) / 7 male (43.75%) (PMID:41160012). Taiwan SJS/TEN survivor cohort: ~50.7% female (PMID:39969876). No convincing sex effect.

**Age distribution:** concentrated in the 6th–8th decades, following gout/CKD prescribing.

---

## 10. Diagnostics

### 10.1 Clinical diagnosis is primary

There is **no confirmatory acute-phase test**. Diagnosis rests on: recent drug exposure with compatible latency + prodrome + painful dusky erythema evolving to blistering and detachment + ≥2 mucosal sites + positive Nikolsky sign + compatible histology.

### 10.2 Histopathology / biopsy

- **Frozen section or punch biopsy** of lesional skin: full-thickness epidermal necrosis, subepidermal detachment, sparse lymphocytic infiltrate, apoptotic/necrotic keratinocytes at all epidermal levels. This is the key rule-out for staphylococcal scalded skin syndrome (which cleaves at the granular layer, not the DEJ).
- **Direct immunofluorescence:** negative — used to exclude autoimmune blistering disease (pemphigus, bullous pemphigoid, linear IgA).
- Full-thickness epidermal necrosis on biopsy was the entry criterion in the PD-1-inhibitor SJS/TEN series (PMID:41418419).

### 10.3 Laboratory tests and biomarkers

| Test | LOINC (verify before binding) | Purpose |
|---|---|---|
| Serum urea / BUN | 3094-0 | SCORTEN |
| Serum glucose | 2345-7 | SCORTEN |
| Serum bicarbonate | 1963-8 | SCORTEN |
| Serum creatinine / eGFR | 2160-0 / 33914-3 | Risk + prognosis; drives oxypurinol clearance |
| CBC with differential | 57021-8 | Eosinophilia (DRESS), cytopenias |
| ALT / AST | 1742-6 / 1920-8 | Organ involvement |
| **Plasma oxypurinol** | no standard LOINC identified | **Research/prognostic** — sustained high levels post-withdrawal predict poor outcome (PMID:25115449). Not routinely available |
| **Plasma / blister granulysin** | no standard LOINC identified | **Research/prognostic** — elevated levels linked to mortality in allopurinol-SJS/TEN (PMID:25115449); also proposed as an early rapid diagnostic |

> "the increased plasma levels of oxypurinol and granulysin linked to the high mortality of allopurinol-SJS/TEN (p<0.01), and strongly associated with prolonged cutaneous reactions in allopurinol-DRESS (p<0.05)"
> — Chung et al. 2015 (**PMID:25115449**)

These two are the closest thing this disease has to a **disease-specific prognostic biomarker pair**, and they are attractive `biochemical:` entries with `BiomarkerReadout` links to the oxypurinol-accumulation and granulysin-cytotoxicity pathophysiology nodes.

### 10.4 Genetic testing

- **Single-allele targeted testing** is the standard: `HLA-B*58:01` genotyping, pre-prescription. Widely available (real-time PCR, LAMP — PMID:23066948; single-tube duplex real-time PCR — PMID:26652271; SSO/SSP typing).
- **HLA imputation from genotyping arrays** is used in biobank research (PMID:41160012) but is not a clinical test.
- **WGS/WES, gene panels, CMA, karyotype, FISH, mtDNA, repeat-expansion testing:** **not applicable.**
- **After the fact**, HLA typing has *diagnostic* value too: in the Turkish DRESS cohort, HLA genotyping was used alongside patch testing and the lymphocyte transformation test to attribute causality among multiple candidate drugs (PMID:42014364).
- **Emerging caveat:** because HLA-B*58:01 is absent in > ⅓ of US allopurinol-SCAR cases and HLA-A*34:02 is independently associated, the authors argue for broader panels — "These findings underscore the need to conduct population-based studies that both reproduce known and uncover novel HLA associations to reduce harm through contributions to screening, risk stratification, and diagnosis" (PMID:41160012).

### 10.5 Ex vivo / delayed drug-allergy testing

- **Lymphocyte transformation test (LTT)** with **oxypurinol** — critically, LTT with the *parent* drug is far less sensitive. "Allopurinol allergic patients are primarily sensitized to oxypurinol in a dose-dependent manner… OXP-TCLs do not recognize allopurinol and vice versa." (PMID:24152157). *Practical implication: an LTT run with allopurinol alone can produce a false negative.* This is an excellent, concrete, curatable diagnostic pitfall.
- **Patch testing** — used in the DRESS setting; low sensitivity, and contraindicated as *provocation* in SJS/TEN survivors.
- **Drug provocation/rechallenge is absolutely contraindicated** in SJS/TEN.

### 10.6 Severity scoring and causality assessment

- **SCORTEN** — seven independent mortality predictors, developed and validated in 165 + 75 patients:
  > "We identified seven independent risk factors for death and constituted the toxic epidermal necrolysis-specific severity-of-illness score: age above 40 y, malignancy, tachycardia above 120 per min, initial percentage of epidermal detachment above 10%, serum urea above 10 mmol per liter, serum glucose above 14 mmol per liter, and bicarbonate below 20 mmol per liter. For each toxic epidermal necrolysis-specific severity-of-illness score point the odds ratio was 3.45 (confidence interval 2.26-5.25)."
  > — Bastuji-Garin et al., *J Invest Dermatol* 2000 (**PMID:10951229**)
  Calibration was excellent in the derivation setting: "excellent agreement between expected (19.6%) and actual (20%) mortality; discrimination was also excellent with a receiver operating characteristic area of 82%."
- **ALDEN (ALgorithm of Drug causality for Epidermal Necrolysis)** — Sassolas et al. 2010 (**PMID:20375998**). The standard causality instrument; used to nominate allopurinol as the culprit when several drugs are in play.
- **RegiSCAR score** — for DRESS specifically, not SJS/TEN (PMID:42499701, PMID:42014364).

### 10.7 Differential diagnosis

| Condition | Distinguishing features |
|---|---|
| Staphylococcal scalded skin syndrome | Subcorneal (granular-layer) split, no mucosal erosion, children, toxin-mediated |
| Generalized bullous fixed drug eruption | Well-demarcated recurrent plaques at fixed sites, minimal mucosal/systemic involvement, better prognosis |
| Acute generalized exanthematous pustulosis (AGEP) | Sterile pustules on edematous erythema, faster onset, neutrophilia |
| DRESS | Facial edema, eosinophilia, lymphadenopathy, visceral involvement, later onset — but **same drug, same allele** |
| Erythema multiforme major | True target lesions, acral distribution, HSV-associated, better prognosis |
| *Mycoplasma*-induced rash and mucositis (MIRM) | Predominantly mucosal, minimal skin, younger patients, infectious trigger |
| Paraneoplastic pemphigus, acute GVHD, autoimmune bullous disease | DIF-positive / clinical context |

### 10.8 Screening in asymptomatic individuals

The screening question here is **pharmacogenomic pre-prescription genotyping**, not disease screening. See §13.

---

## 11. Outcome / Prognosis

### 11.1 Mortality

- **General SJS/TEN:** mortality historically ~30% for TEN (PMID:10951229); modern SJS/TEN cohorts report lower figures with specialist care — 3.8% observed vs 8.6% SCORTEN-predicted in a 213-patient Chinese series (PMID:31898979). One-year mortality of 17% among Danish antiseizure-drug-associated SJS/TEN cases (PMID:42467870).
- **Allopurinol-specific:** allopurinol-SCAR carries a *worse* prognosis than SCAR from many other culprits, and the driver is renal.
  > "Impaired renal function and increased plasma levels of oxypurinol and granulysin correlated with the poor prognosis of allopurinol-SCAR."
  > — Chung et al. 2015 (**PMID:25115449**)
  > "Patients with allopurinol-induced SCARs with renal impairment have significantly higher risk of mortality."
  > — Wang, Dao & Chung, *Curr Opin Allergy Clin Immunol* 2016 (**PMID:27362322**)
- A precise allopurinol-SJS/TEN-specific case-fatality rate from a large modern cohort was **not identified** in this search. Curate the general SJS/TEN figures and the allopurinol-specific *direction* of effect, and flag the exact number as a gap.

### 11.2 Morbidity, complications, and disability

**Acute complications** (from a 213-case SJS/TEN series, PMID:31898979):

| Complication | Frequency |
|---|---|
| Electrolyte disturbance | 174/213 (81.7%) |
| Drug-induced liver injury | 64/213 (30.0%) |
| Infection | 53/213 (24.9%) — respiratory 10.3%, wound 5.2% |
| Fasting glucose > 10 mmol/L | 33/213 (15.5%) |

Sepsis from the denuded skin is the leading proximate cause of death. Other acute complications: hypovolemia, AKI, ARDS/bronchiolitis obliterans, GI hemorrhage (18.2% under corticosteroids vs 2.6% under etanercept, PMID:29400697), thermoregulatory failure, protein-losing catabolic state.

**Chronic sequelae** — this is a disease that does not stop when the skin heals:
- **Ocular:** chronic dry eye, symblepharon, trichiasis, limbal stem cell deficiency, corneal neovascularization and opacification, blindness. The most common and most disabling long-term sequela.
- **Cutaneous:** dyspigmentation, scarring, nail dystrophy/anonychia, chronic pruritus, alopecia.
- **Mucosal:** oral synechiae, esophageal strictures, vaginal/urethral stenosis, phimosis.
- **Pulmonary:** obstructive disease, bronchiolitis obliterans.
- **Cardiovascular — recently quantified and previously underappreciated:**
  > "compared with non-SJS/TEN participants, patients with SJS/TEN had higher risks of cardiovascular morbidity (CVA: HR, 1.65 [95% CI, 1.57-1.72] … IHD: HR, 1.58 [95% CI, 1.51-1.65] …) and death due to cardiovascular disease (CVA: HR, 1.69; 95% CI, 1.46-1.96; IHD: HR, 1.55; 95% CI, 1.32-1.82). The increased cardiovascular mortality risks peaked at 1 year after SJS/TEN and persisted for 4 to 7 years."
  > — Chiu & Chiu, *JAMA Dermatol* 2025 (**PMID:39969876**) — n = 10,571 (CVA cohort) / 11,084 (IHD cohort) SJS/TEN survivors, Taiwan NHIRD 1998–2021
- **Psychological:** PTSD, depression, anxiety — well described in survivor cohorts.
- **Iatrogenic:** lifelong avoidance of allopurinol *and* uncertainty about related urate-lowering options; loss of a first-line gout therapy in someone who often has CKD and few alternatives.

### 11.3 Prognostic factors

- **SCORTEN** (age, malignancy, tachycardia, BSA, urea, glucose, bicarbonate) — PMID:10951229.
- **Renal function / eGFR** — allopurinol-specific, and the strongest disease-specific modifier (PMID:25115449).
- **Plasma oxypurinol level and its trajectory after withdrawal** (PMID:25115449).
- **Plasma granulysin level** (PMID:25115449).
- **Speed of culprit-drug withdrawal.**
- **ICU admission at diagnosis** predicts higher long-term cardiovascular mortality (PMID:39969876).

---

## 12. Treatment

### 12.1 The one intervention everyone agrees on

**Immediate and permanent withdrawal of allopurinol**, plus lifelong documented avoidance. Everything else is contested.

- NCIT: `NCIT:C15747` **Supportive Care**; `NCIT:C49236` Therapeutic Procedure
- Therapeutic modality: `BEHAVIORAL` is a poor fit; this is really "drug discontinuation," for which no clean NCIT clinical-action term was identified. Consider a free-text `preferred_term` with no `term:` binding.

### 12.2 Supportive care — the backbone

Wound care, fluid/electrolyte resuscitation, nutritional support, analgesia, temperature control, infection surveillance (without prophylactic systemic antibiotics), airway assessment, **early ophthalmology involvement** (amniotic membrane transplantation for the ocular surface), urology/gynecology for genital care. Management in a burn unit or specialized SCAR center where available.

> "There is currently no evidence-based treatment outside of aggressive supportive care"
> — Justice, Mukherjee, Martin-Pozo & Phillips, *Allergol Int* 2025 (**PMID:40473510**)

That sentence, from a 2025 review by the group running the definitive trial, is the honest summary of the field and should be quoted directly in the entry.

### 12.3 TNF-α blockade (etanercept) — the strongest positive RCT evidence

Randomized trial, n = 96 SJS/TEN patients, etanercept vs corticosteroids (NCT01276314):

> "Etanercept improved clinical outcomes in patients with SJS-TEN. Etanercept decreased the SCORTEN-based predicted mortality rate (predicted and observed rates, 17.7% and 8.3%, respectively). Compared with corticosteroids, etanercept further reduced the skin-healing time in moderate-to-severe SJS-TEN patients (median time for skin healing was 14 and 19 days for etanercept and corticosteroids, respectively; P = 0.010), with a lower incidence of gastrointestinal hemorrhage in all SJS-TEN patients (2.6% for etanercept and 18.2% for corticosteroids; P = 0.03)."
> — Wang et al., *J Clin Invest* 2018 (**PMID:29400697**)

Mechanistic corroboration in the same trial: "etanercept decreased the TNF-α and granulysin secretions in blister fluids and plasma (45.7%-62.5% decrease after treatment; all P < 0.05) and increased the Treg population (2-fold percentage increase after treatment; P = 0.002)." That is a rare instance of a trial validating the mechanism it targets — good material for a `treatments.target_mechanisms` link with its own evidence.

- Annotation: `treatment_term` `NCIT:C15986` Pharmacotherapy; `therapeutic_agent` `NCIT:C2381` **Etanercept**; `therapeutic_modality: MONOCLONAL_ANTIBODY` — *strictly*, etanercept is a soluble receptor–Fc fusion protein, not a monoclonal antibody. `PROTEIN_REPLACEMENT` is also wrong. **`OTHER` is the honest value**; flag this as a modality-enum gap.
- Supporting data in adjacent settings: TNF blockade in ICI-induced SJS/TEN "showed a significantly rapid recovery and no recurrence of SCAR with continuous ICI therapy" (PMID:39737932); etanercept + corticosteroid combination in PD-1-inhibitor SJS/TEN gave re-epithelialization in 5.75 ± 1.48 days (n = 5, PMID:41418419). Both are **non-allopurinol** contexts — grade accordingly.

### 12.4 Ciclosporin

Widely used, mechanistically plausible (calcineurin inhibition blocks CTL activation), supported by cohort studies and meta-analyses suggesting a mortality benefit — but **no adequately powered RCT**. `therapeutic_agent`: `CHEBI:4031` cyclosporin A / `CHEBI:748220` cyclosporine; `therapeutic_modality: SMALL_MOLECULE`; `treatment_term` `NCIT:C15986`.

### 12.5 Systemic corticosteroids

The historical default, and still the comparator arm in the etanercept trial. Associated there with slower healing and markedly more GI hemorrhage (18.2% vs 2.6%; PMID:29400697). Evidence remains "a subject of ongoing debate, with inconsistent evidence regarding their efficacy" (PMID:40909037). `NCIT:C2322` Corticosteroid as `therapeutic_agent`.

### 12.6 IVIG and plasmapheresis

A large Japanese administrative-database comparison of second-line therapy after corticosteroid failure (1,215 screened; 53 plasmapheresis-first vs 213 IVIG-first) found **no significant difference in inpatient mortality** between the two (PMID:36884227). IVIG's Fas-blockade rationale has not translated into consistent survival benefit.
- `NCIT:C121331` Intravenous Immunoglobulin Therapy; `NCIT:C15304` Plasmapheresis.

### 12.7 The definitive trial: NATIENS

| Field | Value |
|---|---|
| Registry ID | **NCT02987257** |
| Title | NATIENS: Optimal Management and Mechanisms of SJS/TEN (North American Therapeutics in Epidermal Necrolysis Syndrome) |
| Phase | `PHASE_III` |
| Status | `COMPLETED` (registry-recorded; start 2023-03-21, completion 2025-10-31) |
| Arms | Etanercept 50 mg SC on day 1 and day 4 **vs** harmonized supportive care |
| Primary outcome | Time to complete re-epithelialization |
| Design | Multicenter, double-blind, randomized |

> ⚠️ **Read this one carefully before curating.** The ClinicalTrials.gov record returns an **enrollment count of 2** alongside status `COMPLETED`. That is almost certainly a study that closed with minimal accrual rather than a completed 100+ patient trial, but I did not find a published results paper to confirm either reading. **Do not** curate NATIENS as having answered the question. Record `status: COMPLETED`, `phase: PHASE_III`, and put the accrual caveat in `notes:`.

### 12.8 Experimental / emerging

- **JAK inhibitors** (tofacitinib and others) — case reports and small series; rationale is IFN-γ/JAK-STAT blockade. No controlled data identified.
- **Necroptosis inhibition** (RIPK1/RIPK3/MLKL) — "Inhibition of necroptosis completely prevented SJS/TEN-like responses in a mouse model of SJS/TEN" (PMID:25031270). Preclinical only; `evidence_source: MODEL_ORGANISM`.
- **Granulysin neutralization** — direct target validation exists (depletion reduced cytotoxicity, PMID:19029983); no clinical agent.
- **Accelerated oxypurinol clearance** (hemodialysis/hemoperfusion) — proposed but untested: "An early intervention to increase the clearance of plasma oxypurinol may improve the prognosis of allopurinol-SCAR" (PMID:25115449). This is an **allopurinol-specific** therapeutic hypothesis with no other analogue in SCAR, and worth curating as such.

### 12.9 Pharmacogenomics — replacing the drug

- **HLA-B*58:01–positive patients should not receive allopurinol.** CPIC assigns a Level 1A recommendation; the 2015 update confirmed the 2013 recommendations stand:
  > "We reviewed the recent literature and concluded that none of the evidence would change the therapeutic recommendations in the original guideline; therefore, the original publication remains clinically current."
  > — Saito et al., *Clin Pharmacol Ther* 2016 (**PMID:26094938**)
- **Febuxostat** (`CHEBI:31596`) is the principal substitute — structurally unrelated, and immunologically non-cross-reactive (PMID:25946710). Its own cardiovascular safety signal (CARES trial) is a separate consideration.
- **Probenecid** (uricosuric) — the Thai cost-effectiveness model found HLA screening cost-effective *only* if probenecid was the alternative (PMID:40829930).
- **Desensitization** protocols exist for *mild* allopurinol rash but are **contraindicated after SJS/TEN**.

### 12.10 Treatment algorithm (synthesis)

1. Recognize; stop allopurinol immediately; stop all other non-essential drugs (ALDEN to assign causality).
2. Assess BSA detachment; calculate SCORTEN; check eGFR and, if available, plasma oxypurinol.
3. Transfer to burn unit / specialist center. Institute aggressive supportive care.
4. Early ophthalmology, urology/gynecology, ENT/pulmonology consultation.
5. Consider systemic immunomodulation — etanercept has the best randomized evidence (PMID:29400697); ciclosporin is a reasonable alternative; corticosteroids carry a GI bleeding penalty; IVIG/plasmapheresis show no clear benefit over one another.
6. On recovery: document allergy in every record system; HLA-B*58:01 typing (for the patient *and* consider family cascade testing given the shared haplotype); switch to febuxostat or a uricosuric; long-term ophthalmologic follow-up; recognize the elevated cardiovascular risk in survivorship care.

---

## 13. Prevention

### 13.1 Primary prevention — this is where the wins are

**(a) Don't prescribe allopurinol when it isn't indicated.** ACR 2020 conditionally recommends *against* urate-lowering therapy for asymptomatic hyperuricemia. Every avoided prescription is an avoided exposure.

**(b) Start low, go slow.** ACR 2020 strongly recommends:
> "using a low starting dose of allopurinol (≤100 mg/day, and lower in CKD) or febuxostat (<40 mg/day); and a treat-to-target management strategy with ULT dose titration guided by serial serum urate (SU) measurements, with an SU target of <6 mg/dl."
> — FitzGerald et al., *Arthritis Rheumatol* 2020 (**PMID:32390306**)

Note that the same guideline still names allopurinol "the preferred first-line ULT, including for those with moderate-to-severe chronic kidney disease (CKD; stage >3)" — the low-dose-start recommendation is what makes that safe.

**(c) Pre-prescription HLA-B\*58:01 genotyping.** The strongest prevention evidence in the entire report:

> "Participants who tested positive for HLA-B*58:01 (19.6%, n=571) were advised to avoid allopurinol… SCARs did not develop in any of the participants receiving allopurinol who screened negative for HLA-B*58:01. By contrast, seven cases of SCARs were expected, based on the estimated historical incidence of allopurinol induced SCARs nationwide (0.30% per year, 95% confidence interval 0.28% to 0.31%; P=0.0026…)"
> — Ko et al., *BMJ* 2015 (**PMID:26399967**), 2,910 participants, 15 Taiwanese medical centres

`NCIT:C92803` Genetic Screening; `NCIT:C200724` Cascade Testing.

### 13.2 Who should be screened — and the economics

- **CPIC:** if HLA-B*58:01 genotype is known and positive, allopurinol is contraindicated (PMID:26094938). CPIC does not mandate universal testing.
- **ACR 2020:** conditionally recommends HLA-B*58:01 testing **before allopurinol** in patients of **Southeast Asian descent and African American** patients (PMID:32390306).
- **Cost-effectiveness varies sharply by country and by what the alternative drug is:**
  > "Testing of HLA-B*58:01 is more likely to be cost-effective throughout Africa and Asia compared with Europe and the Americas." — Zhou et al. 2021 (**PMID:32535895**)
  > "HLA-B*58:01 testing was not cost-effective before allopurinol initiation in Thai patients with gout at the current price of 1,000 THB per test. However, HLA-B*58:01 testing would be cost-effective if only probenecid was the alternative treatment for patients with positive HLA-B*58:01 results." — Dilokthornsakul et al., *ACR Open Rheumatol* 2025 (**PMID:40829930**), ICER 1,093,068 THB/QALY ≈ $31,404/QALY

  This is a nice illustration that a screening program's value depends less on the test than on how good the second-line drug is.

### 13.3 The implementation gap

Recommended ≠ done. A VA study of clinical decision support:
> "The percentage of Asian or African American/Black patients who had HLA-B*58:01 testing before or during the month allopurinol was prescribed increased from 8.8% in October 2022 to 35.5% in December 2023 at the dashboard + BPA site and from 2.1% to 4.5% at the dashboard only site (P < .0001 for difference in difference)."
> — Fadairo-Azinge et al., *Arthritis Care Res* 2026 (**PMID:41664544**)

Baseline testing rates of 2–9% in a guideline-eligible population, rising only to ~35% with an active alert. National implementation programs exist (e.g. Singapore — PMID:39405418).

### 13.4 Secondary and tertiary prevention

- **Secondary (early detection):** patient counseling to stop the drug and seek care at the first rash — especially in the first 8 weeks; clinician education on the skin-pain-out-of-proportion red flag.
- **Tertiary (preventing complications in those affected):** early transfer to specialist care; aggressive ocular surface management to prevent blindness; sepsis surveillance; permanent allergy documentation; **cardiovascular risk-factor management in survivors**, given HR ~1.6 for CVA and IHD persisting 4–7 years (PMID:39969876).

### 13.5 Genetic counseling, immunization, public health

- **Genetic counseling:** relevant in a narrow sense. HLA-B*58:01 is inherited; first-degree relatives of a case have elevated carriage probability, and cascade testing before *their* allopurinol prescription is defensible. This is pharmacogenomic counseling, not reproductive counseling.
- **Immunization:** **not applicable.**
- **Public health / environmental interventions:** regulatory labeling (HLA-B*58:01 appears in Korean drug labels and, less consistently, US labels — PMID:41846573); pharmacovigilance; national genotype-guided prescribing programs.

---

## 14. Other Species / Natural Disease

### 14.1 Is there a natural animal counterpart?

**Not for allopurinol-induced SJS/TEN specifically.** But TEN as a drug-hypersensitivity phenotype does occur naturally in companion animals:

> "Cutaneous drug allergies in veterinary medicine can have a variety of clinical manifestations, ranging from pruritus to often fatal toxic epidermal necrolysis… There are multiple theories that attempt to explain how drug allergies occur… These include the (pro)-hapten hypothesis, the Danger Theory, the pi concept, and the viral reactivation theory."
> — Voie, Campbell & Lavergne, *J Vet Intern Med* 2012 (**PMID:22519673**)

Note that the p-i concept — the exact mechanism at work in allopurinol-SJS/TEN — is already part of the veterinary conceptual framework. But **no HLA-B*58:01 orthologue exists**: MHC class I alleles are not conserved across species at allelic resolution, and the dog leukocyte antigen (DLA) and feline leukocyte antigen (FLA) systems have their own architectures. There is no reported drug–MHC association in animals analogous to HLA-B*58:01/allopurinol.

- Species: `NCBITaxon:9615` *Canis lupus familiaris* (dog); `NCBITaxon:9685` *Felis catus* (cat) — for TEN generally, not for this drug.
- MONDO carries `MONDO:1013225` **toxic epidermal necrolysis, non-human animal**.
- Breed (VBO): no breed predisposition to drug-induced TEN identified. **Not applicable.**

### 14.2 Allopurinol in veterinary medicine

Allopurinol is used long-term in dogs, chiefly for **canine leishmaniosis** and for urate urolithiasis in Dalmatians. Adverse effects reported are predominantly **xanthine urolithiasis** (an on-target pharmacological effect, not an immune one), not epidermal necrolysis (e.g. PMID:20178476, PMID:10622623). **The immune-mediated SCAR phenotype does not appear to be a recognized entity in dogs on allopurinol** — a striking negative that fits the HLA-restriction model, since dogs have no HLA-B*58:01.

### 14.3 Comparative biology and evolutionary conservation

- **Conserved:** the *effector* machinery — granulysin has no direct mouse orthologue (mice use NK-lysin), but perforin/granzyme, Fas/FasL, and the RIPK1/RIPK3/MLKL necroptosis axis are broadly conserved across mammals.
- **Not conserved:** the *initiating* recognition event. HLA allelic specificity is human-specific by definition. This is the central translational barrier for the disease and the reason animal modeling is so limited (§15).
- **Zoonotic potential / cross-species transmission:** **not applicable.**

---

## 15. Model Organisms

> **Bottom line first:** this disease is exceptionally hard to model, because the initiating lesion is an interaction between a specific human MHC allele and a specific small molecule. You can model the *dying* (steps 6–11 of §6.1) reasonably well. You cannot easily model the *recognizing* (steps 3–5).

### 15.1 Human ex vivo systems — the workhorse, and effectively the primary model

These are **not** animal models and belong in `experimental_models:` as NAMs:

| System | What it models | `relationship` | Fidelity | Key limitation |
|---|---|---|---|---|
| Patient PBMC + oxypurinol (LTT / drug-specific T-cell lines) | Drug-specific CD8 activation, p-i kinetics, dose-dependence | `RECAPITULATES` | HIGH | Ex vivo; uses resolved cases, not active disease |
| Patient blister-fluid cells | Effector cell composition, granulysin content, TCR clonotypes | `MEASURES` | HIGH | Descriptive; single time point |
| Patient-derived keratinocyte cultures ± SJS/TEN PBMC supernatant | Keratinocyte necroptosis, annexin A1/FPR1 dependence | `RECAPITULATES` | MODERATE | Not allopurinol-specific in the source study |
| HLA-B*58:01-transfected APC lines + oxypurinol | HLA restriction, requirement (or not) for processing | `RECAPITULATES` | MODERATE | Cell-line context, supraphysiological drug concentrations |
| Recombinant HLA-B*58:01 crystallography | Drug–groove binding, altered peptide repertoire | `MEASURES` | HIGH | Static structure; no cellular context |

Notable design feature of the Mifsud study: it drew T-cell lines from **drug-naive healthy donors** as well as resolved cases (PMID:37452515) — a clean way to separate "the repertoire exists" from "the repertoire was expanded by disease."

### 15.2 Animal models

- **Mouse granulysin injection model** — recombinant 15-kDa secretory granulysin injected intradermally: "injection of it into mouse skin resulted in features mimicking SJS-TEN" (PMID:19029983). Models the *effector* step only. `relationship: PARTIALLY_RECAPITULATES`, `fidelity: MODERATE`, `limitations`: no drug, no HLA, no T cell — this is a pure downstream-mediator model.
- **Mouse SJS/TEN necroptosis model** — used to show that "Inhibition of necroptosis completely prevented SJS/TEN-like responses in a mouse model of SJS/TEN" (PMID:25031270). Same caveat: effector-arm only.
- **HLA-B\*58:01 transgenic mouse:** **no such model was identified in this search.** Repeated targeted PubMed queries for HLA-B*58:01 transgenic/humanized mice returned nothing. (For contrast, HLA-B*57:01 transgenic mice exist for abacavir hypersensitivity, which is the obvious template.) **This is the single largest model-system gap for this disease and a strong candidate for a `HUMAN_MODEL_MISMATCH` discussion entry**, since it means every mechanistic claim about the initiating recognition event rests on human ex vivo work alone.

### 15.3 Model limitations, stated plainly

1. **No animal expresses HLA-B*58:01 naturally.** The initiating event is unmodellable without transgenesis.
2. **Murine xanthine oxidase metabolism differs**, so oxypurinol exposure is not equivalent.
3. **Granulysin has no direct mouse orthologue**, so the dominant human effector cannot be studied in a wild-type mouse.
4. **Keratinocyte death models (granulysin injection, necroptosis inhibition) reproduce the lesion without reproducing its cause** — useful for therapeutics aimed at steps 6–11, useless for prevention.
5. **No organoid or skin-on-chip model of SJS/TEN was identified.** Given that this disease is fundamentally an immune–epithelial interface problem, a co-culture immunocompetent skin construct with HLA-B*58:01-matched donor cells is the obvious missing NAM.

### 15.4 Resources

- MGI, IMPC, IMSR for the necroptosis-pathway alleles (*Ripk1*, *Ripk3*, *Mlkl*, *Fasl*) — all exist and are well characterized, but for necroptosis biology generally, not for this disease.
- Cellosaurus / ATCC for HLA-typed B-lymphoblastoid lines used as APCs.
- The **NATIENS** (NCT02987257) biorepository and the **SJS/TEN Survivor Study** (PMID:41160012) are the two most important *human* sample resources.

---

## Appendix A — Curation-ready ontology suggestions

| dismech slot | Suggested binding | Confidence |
|---|---|---|
| `disease_term` | `MONDO:0018229` SJS **or** `MONDO:0019810` TEN — needs a lump/split decision; no drug-specific MONDO term exists | ⚠️ decision required |
| `mappings.mondo_mappings` | `MONDO:0005594` severe cutaneous adverse reaction, `skos:broadMatch`; `MONDO:0044739` overlap, `skos:relatedMatch` | high |
| `genetic[].gene_term` | `hgnc:4932` HLA-B; `hgnc:4931` HLA-A | high |
| `pathophysiology` cell types | `CL:0000794` CD8+ αβ cytotoxic T cell; `CL:0000312` keratinocyte; `CL:4052061` epidermal keratinocyte; `CL:0002187` basal cell of epidermis | high |
| `pathophysiology` processes | `GO:0050852`; `GO:0001913`; `GO:0097283`; `GO:0070266`; `GO:1902174`; `GO:0060545` | high |
| Anatomy | `UBERON:0001003` skin epidermis; `UBERON:0002025` stratum basale of epidermis | high |
| Phenotypes | `HP:0032156` Skin detachment; `HP:0200041` Skin erosion; `HP:0200097` Oral mucosal blisters; `HP:0008066` Abnormal blistering of the skin; `HP:0001019` Erythroderma; `HP:0001945` Fever | high |
| Chemical entities | `CHEBI:40279` allopurinol; `CHEBI:748196` oxypurinol (syn. `CHEBI:28315` alloxanthine); `CHEBI:31596` febuxostat; `CHEBI:4031` cyclosporin A | high |
| Treatments | `NCIT:C15747` Supportive Care; `NCIT:C15986` Pharmacotherapy + `NCIT:C2381` Etanercept; `NCIT:C121331` IVIG Therapy; `NCIT:C15304` Plasmapheresis; `NCIT:C92803` Genetic Screening; `NCIT:C2322` Corticosteroid | high |
| **Do not bind** | Nikolsky sign (no HP term); "epigenetic clock"-style composite indices (n/a); an HPO inheritance term (this is not a heritable disease) | — |

### Module conformance candidates

Check `just list-modules` before creating anything new, but these look like natural conformance targets:
- A **treatment-toxicity / "side effect as mechanism"** module — this entry is a textbook member of that family.
- A **T-cell-mediated cytotoxicity** or **adaptive immune effector** module, if one exists.
- A **necroptosis / regulated cell death** module for steps 8–10.
- **Not** an infection or autoimmunity module — the trigger is exogenous and pharmacological, and it resolves on withdrawal.

---

## Appendix B — Explicit gaps (candidate `discussions` with `kind: KNOWLEDGE_GAP` or `HUMAN_MODEL_MISMATCH`)

1. **No HLA-B*58:01 transgenic animal model exists.** Every claim about the initiating drug–HLA–TCR event rests on human ex vivo data. → `HUMAN_MODEL_MISMATCH`.
2. **Why the same allele + same drug yields SJS/TEN in one carrier and DRESS in another is unknown.** Variable expressivity with no explanation.
3. **No allopurinol-specific case-fatality rate** from a large modern cohort was identified; existing figures are for SJS/TEN pooled across culprits.
4. **The p-i mechanism vs. the altered-peptide-repertoire mechanism** are both supported and not reconciled. → `mechanistic_hypotheses` with two groups, `status: EMERGING` for the altered-repertoire model (PMID:37296297).
5. **Macrophage-derived CXCL10** is established in ICI-induced SJS/TEN but untested in allopurinol-induced disease (PMID:39737932).
6. **The annexin A1–FPR1 necroptosis arm** (PMID:25031270) was demonstrated in SJS/TEN generally, not in allopurinol-specific cases.
7. **Enhanced oxypurinol clearance as therapy** is a stated hypothesis with no trial (PMID:25115449).
8. **HLA-A*34:02** rests on 16 cases from a single center (PMID:41160012) and needs replication.
9. **No QoL instrument data specific to allopurinol-induced SJS/TEN.**
10. **NATIENS results are unpublished** and the registry enrollment figure suggests the trial may not have accrued.
11. **No single-cell atlas of allopurinol-induced SJS/TEN lesional skin.**

---

## Sources

**Primary literature (PubMed)**
- Hung SI et al. HLA-B*5801 allele as a genetic marker for severe cutaneous adverse reactions caused by allopurinol. *PNAS* 2005;102(11):4134-9. [PMID:15743917](https://pubmed.ncbi.nlm.nih.gov/15743917/) · doi:10.1073/pnas.0409500102
- Halevy S et al. Allopurinol is the most common cause of Stevens-Johnson syndrome and toxic epidermal necrolysis in Europe and Israel. *J Am Acad Dermatol* 2008;58(1):25-32. [PMID:17919772](https://pubmed.ncbi.nlm.nih.gov/17919772/)
- Chung WH et al. Granulysin is a key mediator for disseminated keratinocyte death in Stevens-Johnson syndrome and toxic epidermal necrolysis. *Nat Med* 2008;14(12):1343-50. [PMID:19029983](https://pubmed.ncbi.nlm.nih.gov/19029983/)
- Bastuji-Garin S et al. SCORTEN: a severity-of-illness score for toxic epidermal necrolysis. *J Invest Dermatol* 2000;115(2):149-53. [PMID:10951229](https://pubmed.ncbi.nlm.nih.gov/10951229/)
- Bastuji-Garin S et al. Clinical classification of cases of toxic epidermal necrolysis, Stevens-Johnson syndrome, and erythema multiforme. [PMID:8420497](https://pubmed.ncbi.nlm.nih.gov/8420497/)
- Sassolas B et al. ALDEN, an algorithm for assessment of drug causality in Stevens-Johnson syndrome and toxic epidermal necrolysis. [PMID:20375998](https://pubmed.ncbi.nlm.nih.gov/20375998/)
- Yun J et al. Allopurinol hypersensitivity is primarily mediated by dose-dependent oxypurinol-specific T cell response. *Clin Exp Allergy* 2013;43(11):1246-55. [PMID:24152157](https://pubmed.ncbi.nlm.nih.gov/24152157/)
- Yun J et al. Oxypurinol directly and immediately activates the drug-specific T cells via the preferential use of HLA-B*58:01. *J Immunol* 2014;192(7):2984-93. [PMID:24591375](https://pubmed.ncbi.nlm.nih.gov/24591375/)
- Saito N et al. An annexin A1-FPR1 interaction contributes to necroptosis of keratinocytes in severe cutaneous adverse drug reactions. *Sci Transl Med* 2014;6(245):245ra95. [PMID:25031270](https://pubmed.ncbi.nlm.nih.gov/25031270/)
- Chung WH et al. Insights into the poor prognosis of allopurinol-induced severe cutaneous adverse reactions. *Ann Rheum Dis* 2015;74(12):2157-64. [PMID:25115449](https://pubmed.ncbi.nlm.nih.gov/25115449/)
- Chung WH et al. Oxypurinol-specific T cells possess preferential TCR clonotypes and express granulysin in allopurinol-induced severe cutaneous adverse reactions. *J Invest Dermatol* 2015;135(9):2237-48. [PMID:25946710](https://pubmed.ncbi.nlm.nih.gov/25946710/)
- Lin CH et al. Immunologic basis for allopurinol-induced severe cutaneous adverse reactions. *J Allergy Clin Immunol* 2015;135(4):1063-1065.e5. [PMID:25458913](https://pubmed.ncbi.nlm.nih.gov/25458913/)
- Ko TM et al. Use of HLA-B*58:01 genotyping to prevent allopurinol induced severe cutaneous adverse reactions in Taiwan. *BMJ* 2015;351:h4848. [PMID:26399967](https://pubmed.ncbi.nlm.nih.gov/26399967/)
- Saito Y et al. CPIC guidelines for HLA-B genotype and allopurinol dosing: 2015 update. *Clin Pharmacol Ther* 2016;99(1):36-7. [PMID:26094938](https://pubmed.ncbi.nlm.nih.gov/26094938/)
- Wang CW, Dao RL, Chung WH. Immunopathogenesis and risk factors for allopurinol severe cutaneous adverse reactions. *Curr Opin Allergy Clin Immunol* 2016;16(4):339-45. [PMID:27362322](https://pubmed.ncbi.nlm.nih.gov/27362322/)
- Wang CW et al. Randomized, controlled trial of TNF-α antagonist in CTL-mediated severe cutaneous adverse reactions. *J Clin Invest* 2018;128(3):985-996. [PMID:29400697](https://pubmed.ncbi.nlm.nih.gov/29400697/)
- Yang L et al. Retrospective study of 213 cases of Stevens-Johnson syndrome and toxic epidermal necrolysis from China. *Burns* 2020;46(4):959-969. [PMID:31898979](https://pubmed.ncbi.nlm.nih.gov/31898979/)
- FitzGerald JD et al. 2020 American College of Rheumatology Guideline for the Management of Gout. *Arthritis Rheumatol* 2020;72(6):879-895. [PMID:32390306](https://pubmed.ncbi.nlm.nih.gov/32390306/)
- Zhou Y et al. Global frequencies of clinically important HLA alleles and their implications for the cost-effectiveness of preemptive pharmacogenetic testing. *Clin Pharmacol Ther* 2021;109(1):160-174. [PMID:32535895](https://pubmed.ncbi.nlm.nih.gov/32535895/)
- Bathini L et al. Initiation dose of allopurinol and the risk of severe cutaneous reactions in older adults with CKD. *Am J Kidney Dis* 2022;80(6):730-739. [PMID:35644439](https://pubmed.ncbi.nlm.nih.gov/35644439/)
- Miyamoto Y et al. Evaluation of plasmapheresis vs immunoglobulin as first treatment after ineffective systemic corticosteroid therapy for patients with SJS/TEN. *JAMA Dermatol* 2023;159(5):481-487. [PMID:36884227](https://pubmed.ncbi.nlm.nih.gov/36884227/)
- Huan X et al. Allopurinol non-covalently facilitates binding of unconventional peptides to HLA-B*58:01. *Sci Rep* 2023;13(1):9373. [PMID:37296297](https://pubmed.ncbi.nlm.nih.gov/37296297/)
- Mifsud NA et al. The allopurinol metabolite, oxypurinol, drives oligoclonal expansions of drug-reactive T cells in resolved hypersensitivity cases and drug-naïve healthy donors. *Allergy* 2023;78(11):2980-2993. [PMID:37452515](https://pubmed.ncbi.nlm.nih.gov/37452515/)
- Chen CB et al. Immune checkpoint inhibitor-induced severe epidermal necrolysis mediated by macrophage-derived CXCL10 and abated by TNF blockade. *Nat Commun* 2024;15(1):10733. [PMID:39737932](https://pubmed.ncbi.nlm.nih.gov/39737932/)
- Chiu HY, Chiu YM. Risk of cardiovascular morbidity and mortality in Stevens-Johnson syndrome/toxic epidermal necrolysis survivors. *JAMA Dermatol* 2025;161(4):391-398. [PMID:39969876](https://pubmed.ncbi.nlm.nih.gov/39969876/)
- Justice J, Mukherjee E, Martin-Pozo M, Phillips E. Updates in the pathogenesis of SJS/TEN. *Allergol Int* 2025;74(3):361-371. [PMID:40473510](https://pubmed.ncbi.nlm.nih.gov/40473510/)
- Dilokthornsakul P et al. An updated economic evaluation of HLA-B*58:01 genotype testing in gouty patients for preventing severe allopurinol hypersensitivity in Thailand. *ACR Open Rheumatol* 2025;7(8):e70093. [PMID:40829930](https://pubmed.ncbi.nlm.nih.gov/40829930/)
- Campbell CN, Krantz MS, Yu A, Phillips EJ; SJS/TEN Survivor Study Collaborators. HLA-B*58:01 and risk of allopurinol-induced severe cutaneous adverse reactions in the US. *JAMA Dermatol* 2025;161(12):1258-1263. [PMID:41160012](https://pubmed.ncbi.nlm.nih.gov/41160012/) (preprint [PMID:40475155](https://pubmed.ncbi.nlm.nih.gov/40475155/))
- Xiong H, Shen Z. Increased TNF-α in SJS/TEN induced by PD-1 inhibitors supports the combination therapy of etanercept and systemic corticosteroids. *Mol Immunol* 2026;189:174-180. [PMID:41418419](https://pubmed.ncbi.nlm.nih.gov/41418419/)
- Fadairo-Azinge A et al. Effect of implementing a dashboard with or without a best practice alert on HLA-B*58:01 testing rates among allopurinol users at VA medical centers. *Arthritis Care Res* 2026;78(9):1265-1269. [PMID:41664544](https://pubmed.ncbi.nlm.nih.gov/41664544/)
- Lee HK et al. Application of risk priority number of failure mode and effects analysis to drug-variant pairs for severe cutaneous adverse reactions in Korean and American populations. *Pharmacogenet Genomics* 2026;36(4):125-133. [PMID:41846573](https://pubmed.ncbi.nlm.nih.gov/41846573/)
- Ünal D et al. Utility of patch testing, LTT, and HLA genotyping in identifying culprit drugs and diagnosing multiple drug hypersensitivity in definite DRESS. *Clin Transl Allergy* 2026;16(4):e70172. [PMID:42014364](https://pubmed.ncbi.nlm.nih.gov/42014364/)
- Heerfordt IM et al. Risk of Stevens-Johnson syndrome and toxic epidermal necrolysis after initiation of antiseizure medication: a Danish nationwide cohort study. *Neurology* 2026;107(3):e218355. [PMID:42467870](https://pubmed.ncbi.nlm.nih.gov/42467870/)
- Voie KL, Campbell KL, Lavergne SN. Drug hypersensitivity reactions targeting the skin in dogs and cats. *J Vet Intern Med* 2012;26(4):863-74. [PMID:22519673](https://pubmed.ncbi.nlm.nih.gov/22519673/)
- Gonçalo M et al. HLA-B*58:01 is a risk factor for allopurinol-induced DRESS and SJS/TEN in a Portuguese population. *Br J Dermatol* 2013. [PMID:23600531](https://pubmed.ncbi.nlm.nih.gov/23600531/)
- Jung JW et al. HLA-DR9 and DR14 are associated with the allopurinol-induced hypersensitivity in hematologic malignancy. *Tohoku J Exp Med* 2014. [PMID:24858023](https://pubmed.ncbi.nlm.nih.gov/24858023/)
- Chua HM et al. Implementation of HLA-related genotype-guided prescribing in Singapore. *Am J Health Syst Pharm* 2025;82(5):e285-e293. [PMID:39405418](https://pubmed.ncbi.nlm.nih.gov/39405418/)

**Databases and registries**
- [ClinicalTrials.gov NCT02987257 — NATIENS](https://clinicaltrials.gov/study/NCT02987257) · [NCT01276314 — etanercept RCT](https://clinicaltrials.gov/study/NCT01276314)
- [EBI Ontology Lookup Service (OLS4)](https://www.ebi.ac.uk/ols4) — MONDO, HP, GO, CL, UBERON, CHEBI, NCIT term verification
- [HGNC REST API](https://rest.genenames.org) — gene identifier verification
- [NCBI MeSH — D013262](https://www.ncbi.nlm.nih.gov/mesh/68013262)
- [PharmGKB / CPIC allopurinol guideline](https://cpicpgx.org/guidelines/guideline-for-allopurinol-and-hla-b/)
- [ICD-11 MMS EB13 block](https://www.findacode.com/icd-11/block-195467267.html)
- [Orphanet — SJS/TEN spectrum (ORPHA:95455)](https://www.orpha.net/en/disease/detail/95455) — *code from secondary sources; portal blocked automated retrieval, verify before binding*
- [DermNet NZ — SJS/TEN](https://dermnetnz.org/topics/stevens-johnson-syndrome-toxic-epidermal-necrolysis)
- [Mayo Clinic Laboratories — HLA-B*5801 genotype test](https://www.mayocliniclabs.com/test-catalog/overview/610055/hla-b-5801-genotype-allopurinol-hypersensitivity-varies) · [ARUP Consult — HLA-B*58:01 genotyping](https://arupconsult.com/ati/hla-b5801-genotyping)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 45 |
| Resolved | 45 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 12 |
| Quoted claims found in source | 9 |
| Quoted claims **not** found in source | 3 |
| References weighed for topical relevance | 45 |
| On topic | 35 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:24152157` *(abstract only)*: "TCL induction data show that both the presence of HLA-B*58:01 allele and high concentration of drug are important for the generation of drug-specific T cells… functional avidity of ALP/OXP-TCL is dependent on both the induction dose and HLA-B*58:01 status."
  - closest text in source: "TCL induction data show that both the presence of HLA-B*58:01 allele and high concentration of drug are important for the generation of drug-specific T cells"
- `PMID:17919772` *(abstract only)*: "restricted to short-term use (≤8 weeks)"
  - closest text in source: "The risk was restricted to short-term use (<or=8 weeks)"
- `PMID:24152157` *(abstract only)*: "Allopurinol allergic patients are primarily sensitized to oxypurinol in a dose-dependent manner… OXP-TCLs do not recognize allopurinol and vice versa."
  - closest text in source: "RESULTS: Allopurinol allergic patients are primarily sensitized to oxypurinol in a dose-dependent manner"
