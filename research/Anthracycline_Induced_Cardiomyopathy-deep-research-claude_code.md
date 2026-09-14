---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-09-01T12:09:33.736706'
end_time: '2026-09-01T12:24:20.696101'
duration_seconds: 886.96
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Anthracycline-Induced Cardiomyopathy
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
  web_search_requests: 10
  num_turns: 88
  total_cost_usd: 6.826602999999997
  session_id: 8539d77b-24ba-4cc5-83e1-56537057707f
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 1
citation_count: 12
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Anthracycline-Induced Cardiomyopathy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Anthracycline-Induced Cardiomyopathy** covering all of the
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

# Anthracycline-Induced Cardiomyopathy — Comprehensive Research Report

**Prepared:** 2026-09-01 · **Target MONDO:** `MONDO:0022653` (*cardiomyopathy due to anthracyclines*) · **Category:** Complex / acquired drug-toxicity cardiomyopathy

> **Read-me first — a framing note that matters for KB modeling.** This is not a Mendelian disease with a causal gene. It is an *exposure-initiated* cardiomyopathy: the drug is the cause, and the genome is a set of dials on how hard the drug lands. Every "genetic" section below therefore describes **susceptibility modifiers**, not causal variants, and the etiologic root node of the pathograph should be the anthracycline exposure itself. Modeling this the other way round (gene → disease) inverts the whole mechanism.

---

## 1. Disease Information

### 1.1 Overview

Anthracycline-induced cardiomyopathy (AIC) is an acquired, dose-dependent cardiomyopathy caused by exposure to anthracycline chemotherapeutics — doxorubicin, daunorubicin, epirubicin, idarubicin — and the structurally related anthraquinone mitoxantrone. It presents as progressive left ventricular systolic dysfunction that may remain asymptomatic (detectable only by imaging or biomarkers) or progress to overt dilated-phenotype heart failure. It is the archetypal "side effect as mechanism" entity in cardio-oncology.

The clinical importance is not marginal. Anthracyclines remain first-line for lymphomas, acute leukaemias, breast cancer, and soft-tissue sarcomas six decades after their introduction:

> "Since their introduction in the 1960s, anthracyclines have been a significant breakthrough in oncology... Although new-generation targeted drugs and cellular therapies are revolutionizing contemporary oncology, anthracyclines remain the cornerstone of treatment for lymphomas, acute leukemias, and soft tissue sarcomas. However, their clinical application is limited by a dose-dependent cardiotoxicity that can reduce cardiac performance and eventually lead to overt heart failure."
> — Camilli et al., *JACC CardioOncology* 2024 (**PMID:39479333**), state-of-the-art review

### 1.2 Identifiers

| Resource | Identifier | Label |
|---|---|---|
| MONDO | `MONDO:0022653` | cardiomyopathy due to anthracyclines *(verified via OLS4)* |
| SNOMED CT | `880042006` | Dilated cardiomyopathy caused by anthracycline (disorder) |
| UMLS / MedGen | `C5437452` | Dilated cardiomyopathy caused by anthracycline |
| MONDO parent | `MONDO:0004994` | cardiomyopathy |
| SNOMED parent | `72972005` | Dilated cardiomyopathy caused by drug (disorder) |
| ICD-10-CM | `I42.7` | Cardiomyopathy due to drug and external agent (+ `T45.1X5A` adverse effect of antineoplastic drugs) |
| ICD-11 | `BC43.4` / `BC43` region (cardiomyopathy due to drug) with external-cause extension |
| MeSH | `D066126` (Cardiotoxicity); `D004317` (Doxorubicin); `D002311` (Cardiomyopathies) |
| OMIM | **Not applicable** — no Mendelian OMIM entry; this is an acquired toxicity |
| Orphanet | **No dedicated ORPHA disorder code**; check `ORPHA:` structured cache before asserting one |

*Modeling note:* ICD-10/ICD-11 assignments above are the conventional coding practice and should be confirmed against a coding authority before being committed as `mappings` — they are the weakest-verified identifiers in this table.

### 1.3 Synonyms and alternative names

- Anthracycline cardiotoxicity (ACT); anthracycline-induced cardiotoxicity (AIC)
- Doxorubicin-induced cardiomyopathy (DIC); doxorubicin cardiotoxicity
- Adriamycin cardiomyopathy (historic trade-name usage)
- Chemotherapy-induced cardiomyopathy (broader; not synonymous — includes trastuzumab, VEGF-inhibitor, and proteasome-inhibitor toxicity)
- Cancer therapy-related cardiac dysfunction (CTRCD) — the **umbrella** term adopted by ESC/IC-OS, of which AIC is one cause. Do not treat CTRCD and AIC as exact matches; `skos:broadMatch` is the honest relation.

### 1.4 Data provenance character

Evidence is drawn from **both** aggregated disease-level resources and individual-patient sources, and the two disagree systematically:

- **Prospective single-institution cohorts with protocolized echo** (e.g., Cardinale 2015, n=2,625) capture asymptomatic dysfunction and yield ~9% incidence.
- **Retrospective trial re-analysis** (Swain 2003) and **survivorship registries** (Childhood Cancer Survivor Study, DCOG-LATER, St Jude Lifetime) capture symptomatic/late events at long latency.
- **EHR/registry disproportionality data** (VigiBase) capture reported adverse events, heavily under-ascertained for asymptomatic disease.

Incidence figures are therefore not comparable across sources without knowing the case definition. This is the single most important caveat for any epidemiology annotation in this entry.

---

## 2. Etiology

### 2.1 Primary causal factor

**Exposure to an anthracycline or anthraquinone antineoplastic agent.** The relationship is dose-dependent and, in its established form, largely irreversible at the level of cardiomyocyte loss.

Suggested ECTO/CHEBI grounding for the exposure node:

| Agent | CHEBI | Status |
|---|---|---|
| doxorubicin | `CHEBI:28748` | verified (label: *doxorubicin*) |
| daunorubicin | `CHEBI:41977` | verified |
| epirubicin | `CHEBI:47898` | verified — **canonical label is `4'-epidoxorubicin`**, use `preferred_term: epirubicin` |
| idarubicin | `CHEBI:42068` | verified |
| mitoxantrone | `CHEBI:50729` | verified |

### 2.2 Dose as the dominant risk factor

Swain's re-analysis of three prospective phase III trials remains the reference dose-response curve in adults:

> "Analysis indicated that an estimated cumulative 26% of patients would experience doxorubicin-related CHF at a cumulative dose of 550 mg/m(2)."
> — Swain SM et al., *Cancer* 2003;97(11):2869-79 (**PMID:12767102**)

and, crucially, that the older 7%-at-550-mg/m² figure was an underestimate:

> "Doxorubicin-related CHF occurs with greater frequency and at a lower cumulative dose than previously reported. These findings further indicate that LVEF is not an accurate predictor of CHF in patients who receive doxorubicin." *(ibid.)*

In childhood cancer survivors the dose-response begins far lower than the traditional "safe threshold" implied:

> "A dose-dependent association was observed between cumulative anthracycline exposure and cardiomyopathy risk (0 mg/m(2): reference; 1 to 100 mg/m(2): odds ratio [OR], 1.65; 101 to 150 mg/m(2): OR, 3.85; 151 to 200 mg/m(2): OR, 3.69; 201 to 250 mg/m(2): OR, 7.23; 251 to 300 mg/m(2): OR, 23.47; > 300 mg/m(2): OR, 27.59; P(trend) < .001)."
> — Blanco JG et al., *J Clin Oncol* 2012 (**PMID:22124095**)

**Agent-specific dose equivalence** was re-derived from 28,423 pooled survivors, overturning the hematologic-toxicity-based conversion factors that treatment protocols had used:

> "Relative to doxorubicin, the equivalence ratios were 0.6 (95% CI, 0.4-1.0) for daunorubicin, 0.8 (95% CI, 0.5-2.8) for epirubicin, and 10.5 (95% CI, 6.2-19.1) for mitoxantrone."
> — Feijen EAM et al., *JAMA Oncol* 2019;5(6):864-871 (**PMID:30703192**)

> "the current hematologic-based doxorubicin dose equivalency of mitoxantrone (4:1) appeared to significantly underestimate the association of mitoxantrone with long-term cardiomyopathy risk." *(ibid.)*

This is a high-value, under-modeled fact: **mitoxantrone is roughly 10× doxorubicin for late cardiomyopathy, not 4×.**

### 2.3 Non-genetic (clinical/environmental) risk factors

Assembled from the HFA-ICOS baseline risk proforma and its validation, the ESC 2022 guideline, and the JACC state-of-the-art review:

- **Cumulative anthracycline dose** (dominant, continuous)
- **Prior anthracycline or other cardiotoxic cancer therapy**
- **Mediastinal/chest radiotherapy**, especially ≥15 Gy cardiac dose — Mulrooney reports cardiac radiation ≥1500 cGy "increased the relative hazard of congestive heart failure, myocardial infarction, pericardial disease, and valvular abnormalities by twofold to sixfold" (**PMID:19996459**)
- **Concurrent HER2-targeted therapy (trastuzumab)** — sequential/concurrent exposure is synergistic
- **Age at exposure** — bimodal: very young children and older adults. Swain: "Age appeared to be an important risk factor for doxorubicin-related CHF after a cumulative dose of 400 mg/m(2), with older patients (age > 65 years) showing a greater incidence of CHF compared with younger patients" (**PMID:12767102**)
- **Female sex** — higher risk in paediatric cohorts; also the group with greater dexrazoxane benefit (Lipshultz 2010)
- **Pre-existing cardiovascular disease, reduced baseline LVEF, hypertension, diabetes, obesity, chronic kidney disease**
- **Elevated baseline cardiac biomarkers (troponin, natriuretic peptides)**
- **Smoking, sedentary behaviour** (HFA-ICOS lifestyle domain)
- **Bolus vs. prolonged-infusion administration** — bolus schedules deliver higher peak myocardial concentration and carry higher risk

**Baseline risk stratification is now validated.** In the CARDIOTOX registry (NCT02039622), n=1,066:

> "According to the HFA-ICOS criteria, 571 patients (53.6%) were classified as low risk, 333 (31.2%) as moderate risk, 152 (14.3%) as high risk, and 10 (0.9%) as very high risk... Incidence rates of symptomatic or moderate to severe symptomatic CTRCD and all-cause mortality significantly increased with HFA-ICOS score [hazard ratio 28.74, 95% confidence interval (CI) 9.33-88.5; P < .001...]"
> — Rivero-Santana B et al., *Eur Heart J* 2025;46(3):273-284 (**PMID:39106857**)

### 2.4 Protective factors

**Genetic protective alleles.** The variant alleles of the carbonyl-reductase SNPs behave protectively at low-to-moderate dose:

> "Among individuals carrying the variant A allele (CBR1:GA/AA and/or CBR3:GA/AA), exposure to low- to moderate-dose anthracyclines (1 to 250 mg/m(2)) did not increase the risk of cardiomyopathy."
> — Blanco 2012 (**PMID:22124095**)

Similarly for *CELF4*: "among patients with the A allele, cardiomyopathy was infrequent and not dose related" (**PMID:26811534**).

**Pharmacological/behavioural protection** — see §12–13. Briefly: dexrazoxane, liposomal formulation, statins, ACE inhibitors/ARBs, and (emerging) SGLT2 inhibitors.

### 2.5 Gene–environment interaction

This disease is the textbook GxE case, and the *CELF4* finding was explicitly framed that way — the SNP showed **no marginal association**, only an interaction with dose:

> "No SNP was marginally associated with cardiomyopathy. However, SNP rs1786814 on the CELF4 gene passed the significance cutoff for gene-environment interaction (Pge = 1.14 × 10(-5))... among those exposed to greater than 300 mg/m(2) of anthracyclines, the rs1786814 GG genotype conferred a 10.2-fold (95% CI, 3.8- to 27.3-fold; P < .001) increased risk of cardiomyopathy compared with those who had GA/AA genotypes and anthracycline exposure of 300 mg/m(2) or less."
> — Wang X et al., *J Clin Oncol* 2016 (**PMID:26811534**)

Modeling implication: a genotype node with no edge to the exposure node misrepresents this. The correct pathograph shape is exposure → mechanism, with genotype as a modifier edge onto the exposure→mechanism link, not a parallel initiating cause.

---

## 3. Phenotypes

### 3.1 Cardiac structural and functional phenotypes

| Phenotype | HP term | Type | Notes |
|---|---|---|---|
| Dilated cardiomyopathy | `HP:0001644` *Dilated cardiomyopathy* ✓cached | Structural | The established late phenotype |
| Cardiomyopathy (generic) | `HP:0001638` *Cardiomyopathy* ✓ | Structural | Parent term |
| Reduced left ventricular ejection fraction | `HP:0012664` *Reduced left ventricular ejection fraction* ✓ | Functional/imaging | The defining CTRCD criterion |
| Congestive heart failure | `HP:0001635` *Congestive heart failure* ✓ | Clinical syndrome | Symptomatic endpoint |
| Restrictive cardiomyopathy | `HP:0001723` *Restrictive cardiomyopathy* ✓ | Structural | Paediatric survivors, late; less common |
| Myocardial fibrosis | `HP:0001685` *Myocardial fibrosis* ✓ | Histopathological | Detected by CMR LGE/ECV and biopsy |
| Left ventricular hypertrophy (inadequate wall growth in children) | `HP:0001712` ✓ | Structural | In paediatric survivors the lesion is often *failure of wall thickness to grow*, i.e. reduced LV wall thickness — verify a better HP term before binding |
| Cardiogenic shock | `HP:0030149` ✓ | Severe/late | "very severe" CTRCD |
| Sudden cardiac death | `HP:0001645` ✓ | Terminal event | Late survivorship |

### 3.2 Arrhythmic and electrophysiological phenotypes

| Phenotype | HP term |
|---|---|
| Arrhythmia | `HP:0011675` ✓ |
| Sinus tachycardia | `HP:0011703` ✓ |
| Supraventricular tachycardia | `HP:0004755` ✓ |
| Atrial fibrillation | `HP:0005110` ✓ |
| Atrial flutter | `HP:0004749` ✓ |
| Ventricular tachycardia | `HP:0004756` ✓ |
| Ventricular arrhythmia | `HP:0004308` ✓ |
| Prolonged QT interval | `HP:0001657` ✓ |
| Abnormal EKG | `HP:0003115` ✓ — non-specific ST/T changes and reduced QRS voltage are classic acute findings |

### 3.3 Symptoms and signs of heart failure

| Phenotype | HP term |
|---|---|
| Dyspnea | `HP:0002094` ✓ |
| Exertional dyspnea | `HP:0002875` ✓ |
| Orthopnea | `HP:0012764` ✓ |
| Fatigue | `HP:0012378` ✓ |
| Asthenia | `HP:0025406` ✓ |
| Palpitations | `HP:0001962` ✓ |
| Syncope | `HP:0001279` ✓ |
| Peripheral edema | `HP:0012398` ✓ |
| Elevated jugular venous pressure | `HP:0030848` ✓ |
| Hepatomegaly | `HP:0002240` ✓ |
| Ascites | `HP:0001541` ✓ |
| Pleural effusion | `HP:0002202` ✓ |
| Pericardial effusion | `HP:0001698` ✓ (acute pericarditis-myocarditis syndrome) |

### 3.4 Laboratory abnormalities

| Phenotype | HP term | LOINC |
|---|---|---|
| Increased circulating troponin I concentration | `HP:0410173` ✓ | LOINC `10839-9` (Troponin I, serum) |
| Increased circulating troponin T concentration | `HP:0410174` ✓ | LOINC `67151-1` (hs-cTnT) |
| Increased circulating brain natriuretic peptide concentration | `HP:0033534` ✓ | LOINC `33762-6` (NT-proBNP); `30934-4` (BNP) |

*LOINC codes above are the conventional ones and should be confirmed before binding — they were not machine-verified in this pass.*

### 3.5 Onset, severity, progression, frequency

**Three classical temporal forms** (a taxonomy that Cardinale's data partly dismantled — see §8):

| Form | Timing | Character | Frequency |
|---|---|---|---|
| Acute | Within days of infusion | Transient arrhythmia, ECG changes, rarely myopericarditis | <1%; usually reversible |
| Early-onset chronic | <1 year after therapy | Progressive LV dysfunction, often asymptomatic at detection | The bulk of cases |
| Late-onset chronic | >1 year, up to decades | Dilated/restrictive cardiomyopathy in survivors | Cumulative incidence rises to 30 years |

**Frequency of asymptomatic vs symptomatic disease**, from the RARG GWAS background:

> "Anthracyclines are used in over 50% of childhood cancer treatment protocols, but their clinical usefulness is limited by anthracycline-induced cardiotoxicity (ACT) manifesting as asymptomatic cardiac dysfunction and congestive heart failure in up to 57% and 16% of patients, respectively."
> — Aminkeng F et al., *Nat Genet* 2015 (**PMID:26237429**)

**Severity grading — ESC 2022 CTRCD.** These are the operative severity categories and should be modeled as a `stages`/severity axis rather than as separate phenotypes:

*Asymptomatic:*
- **Mild:** "LVEF ≥50% and decline in GLS >15% and/or new rise in cardiac biomarkers"
- **Moderate:** "new decrease in LVEF by 10% to a LVEF of 40% to 49%"
- **Severe:** "new decrease in LVEF to <40%"

*Symptomatic:*
- **Mild:** "mild HF symptoms, no intensification of therapy required"
- **Moderate:** "required intensification of diuretic agents and HF therapy"
- **Severe:** "hospitalization for HF"
- **Very severe:** "HF requiring inotropic or mechanical support and consideration of transplantation"

— as summarized in Camilli et al. 2024 (**PMID:39479333**), from Lyon AR et al., *Eur Heart J* 2022;43(41):4229-4361 (**PMID:36017568**)

### 3.6 Quality of life

No AIC-specific QoL instrument exists. Reported impacts, per phenotype:
- **Symptomatic HF** — measured with KCCQ, MLHFQ, and generic EQ-5D/SF-36; scores track NYHA class rather than aetiology.
- **Asymptomatic dysfunction** — by definition no direct QoL decrement, but drives lifelong surveillance burden, insurance/employment consequences, and anxiety in survivors.
- **Treatment truncation** — an under-measured harm: cardiotoxicity that forces early discontinuation of curative-intent chemotherapy imposes oncologic as well as cardiac cost.
- Childhood cancer survivors carry the burden across decades; CCSS data (**PMID:19996459**) show cumulative cardiac incidence still climbing 30 years out.

---

## 4. Genetic / Molecular Information

**There are no causal genes.** Everything in this section is susceptibility, modifier, or pharmacogenomic. Model with `relationship_type: SUSCEPTIBILITY` or `MODIFIER`, never `CAUSATIVE`.

### 4.1 Susceptibility loci — replicated

| Gene | HGNC (verified via HGNC REST) | Variant | Effect | Evidence |
|---|---|---|---|---|
| **RARG** | `hgnc:9866` | rs2229774 (p.Ser427Leu), nonsynonymous | ~4.7× increased risk; derepresses *TOP2B* | **PMID:26237429**, **PMID:34525346** |
| **CBR3** | `hgnc:1549` | V244M (rs1056892), G allele | Homozygous G → risk at low/moderate dose | **PMID:22124095** |
| **CBR1** | `hgnc:1548` | 1096G>A | Variant A allele protective at low dose | **PMID:22124095** |
| **CELF4** | `hgnc:14015` | rs1786814, GG genotype | 10.2× risk at >300 mg/m²; GxE only | **PMID:26811534** |
| **TTN** | `hgnc:12403` | Truncating variants (TTNtv) | 7.5% of CCM cases vs 1.1% TCGA | **PMID:30987448** |
| **RAC2** | `hgnc:9802` | — | Functionally validated as modulating DIC susceptibility | *JACC CardioOncol* 2024 functional-validation study (verify PMID before citing) |
| **SLC28A3** | `hgnc:16484` | rs7853758 | Protective in CPNDS candidate-gene work | Verify PMID before binding |
| **UGT1A6** | `hgnc:12538` | *4 allele | Risk-increasing | Verify PMID before binding |
| **HAS3** | `hgnc:4820` | rs2232228 | Modifies risk at high dose | Verify PMID before binding |

**The RARG result is the mechanistically deepest**, because the variant was traced to the same effector as the core mechanism:

> "We identified a nonsynonymous variant (rs2229774, p.Ser427Leu) in RARG highly associated with ACT (P = 5.9 × 10(-8), odds ratio (95% confidence interval) = 4.7 (2.7-8.3)). This variant alters RARG function, leading to derepression of the key ACT genetic determinant Top2b, and provides new insight into the pathophysiology of this severe adverse drug reaction."
> — Aminkeng 2015 (**PMID:26237429**)

and was then confirmed in patient-derived cells with a candidate therapy attached:

> "We determine that the mechanism of this RARG variant effect is mediated via suppression of topoisomerase 2β (TOP2B) expression and activation of the cardioprotective extracellular regulated kinase (ERK) pathway. We use patient-specific hiPSC-CMs as a drug discovery platform, determining that the RARG agonist CD1530 attenuates DIC"
> — Magdy T et al., *Cell Stem Cell* 2021;28(12):2076-2089 (**PMID:34525346**)

### 4.2 The rare-variant / latent-cardiomyopathy hypothesis

Garcia-Pavia's finding reframes a fraction of AIC as **unmasked latent inherited cardiomyopathy**:

> "Titin-truncating variants (TTNtvs) predominated, occurring in 7.5% of patients with CCM versus 1.1% of The Cancer Genome Atlas participants (P=7.36e-08), 0.7% of healthy volunteers (P=3.42e-06), and 0.6% of the reference population (P=5.87e-14). Adult patients who had CCM with TTNtvs experienced more heart failure and atrial fibrillation (P=0.003) and impaired myocardial recovery (P=0.03) than those without."
> — Garcia-Pavia P et al., *Circulation* 2019 (**PMID:30987448**)

> "Consistent with human data, anthracycline-treated TTNtv mice and isolated TTNtv cardiomyocytes showed sustained contractile dysfunction unlike wild-type (P=0.0004 and P<0.002, respectively)." *(ibid.)*

Other sarcomeric/cytoskeletal genes on the sequenced panel — *MYH7* (`hgnc:7577`), *LMNA* (`hgnc:6636`), *BAG3* (`hgnc:939`) — are plausible in the same frame but individually underpowered.

### 4.3 Variant classification, frequency, origin

- **Classification:** These are **risk alleles**, not ACMG pathogenic variants. `rs2229774`, `rs1786814`, `CBR3 V244M` are common polymorphisms and would be classified benign/VUS by ACMG criteria for Mendelian disease — that framework simply does not apply. *TTNtv*s are the exception: individually they may be classified pathogenic/likely pathogenic for DCM in ClinVar, and here act as a susceptibility background.
- **Allele frequency:** All the GWAS/candidate SNPs above are common (MAF typically >5%) in gnomAD; *TTNtv* carrier frequency in unselected populations is ~0.5–1.1% per the comparison cohorts above.
- **Origin:** Germline. Somatic variation is not implicated.
- **Functional consequence:** *RARG* p.Ser427Leu — loss of repressive function on *TOP2B* (a de-repression, i.e. functionally hypomorphic for the receptor, hypermorphic for the target). *CBR1/CBR3* — altered enzyme activity changing the rate of anthracycline → alcohol-metabolite conversion. *CELF4* — altered *TNNT2* splicing regulation. *TTNtv* — haploinsufficiency/poison-peptide effect on sarcomere reserve.

### 4.4 The *CELF4* → *TNNT2* splicing mechanism

Unusually for a GWAS hit, a splicing mechanism was proposed and partly tested in human hearts:

> "CUG-BP and ETR-3-like factor proteins control developmentally regulated splicing of TNNT2, the gene that encodes for cardiac troponin T (cTnT), a biomarker of myocardial injury. Coexistence of more than one cTnT variant results in a temporally split myofilament response to calcium, which causes decreased contractility. Analysis of TNNT2 splicing variants in healthy human hearts suggested an association between the rs1786814 GG genotype and coexistence of more than one TNNT2 splicing variant (90.5% GG v 41.7% GA/AA; P = .005)."
> — Wang 2016 (**PMID:26811534**) — *TNNT2* = `hgnc:11949` ✓cached

### 4.5 Epigenetic information

- **Nrf2 (`NFE2L2`, `HGNC:7782`) → HMOX1 (`HGNC:5013`) transcriptional axis** is a demonstrated *transcriptional*, not strictly epigenetic, driver of iron liberation (Fang 2019, below).
- **Circulating miRNAs** are the most active current biomarker/epigenetic-regulation area; a 2024 state-of-the-art review catalogues candidates: "circulating miRNAs exhibit resistance to degradation and offer a direct pathomechanistic link" — Boen HM et al., *JACC CardioOncol* 2024;6(2):183-199 (**PMID:38774014**). Frequently reported candidates include miR-1, miR-34a, miR-208a/b, miR-133b, miR-146a; none is clinically validated.
- **TOP2B–SMYD1 interaction:** a 2026 report describes TOP2B binding SMYD1, a muscle-restricted histone methyltransferase whose mutations independently cause human cardiomyopathy — a genuinely epigenetic arm of the mechanism (Wang Q et al., *Cancer Res Commun* 2026, **PMID:42102394**). New and unreplicated; treat as `EMERGING`.
- DNA methylation and histone-modification profiling in AIC is exploratory; no ENCODE/Roadmap-level resource is disease-specific.

### 4.6 Chromosomal abnormalities

**Not applicable.** No aneuploidy, translocation, or CNV association is established for AIC.

---

## 5. Environmental Information

### 5.1 The exposure itself

This is the etiologic root. Model as an `environmental[]` entry with `influences_mechanisms` and `environmental_effect: TRIGGERS`, targeting the systemic-exposure pathophysiology node.

- **Route:** intravenous (bolus or continuous infusion). Infusion duration is a modifiable determinant of peak myocardial concentration.
- **Dose metric:** cumulative mg/m² doxorubicin-equivalent, with the Feijen equivalence ratios (**PMID:30703192**) as the conversion.
- **ECTO:** Search ECTO for an anthracycline/doxorubicin exposure term before binding. If none exists at adequate specificity, follow the repository's "no term beats a bad one" rule — leave `term:` off, keep the free-text `preferred_term`, and record the search in `notes:`. Do **not** stretch a generic "exposure to drug" term.

### 5.2 Co-exposures that modify risk

- **Thoracic/mediastinal ionizing radiation** — additive to synergistic (Mulrooney, **PMID:19996459**)
- **Trastuzumab and other HER2-targeted agents** — sequential exposure amplifies dysfunction; the mechanistic rationale is loss of the NRG1/ERBB2 cardiomyocyte repair pathway *while* anthracycline damage is accruing
- **Cyclophosphamide, taxanes** — commonly co-administered; taxanes alter doxorubicin pharmacokinetics
- **Mitoxantrone** used in multiple sclerosis — a non-oncologic exposure route that is easy to miss

### 5.3 Lifestyle factors

- Sedentary behaviour, obesity, smoking, hypertension, diabetes — all in the HFA-ICOS proforma
- **Exercise during and after treatment** is under investigation as protective; evidence is mechanistically attractive and clinically not yet definitive

### 5.4 Infectious agents

**Not applicable.** No infectious aetiology.

---

## 6. Mechanism / Pathophysiology

### 6.1 The causal chain — ordered

Present in this order in the pathograph. Every step names what it causes next; inference is flagged.

1. **Intravenous anthracycline administration** *leads to* **systemic anthracycline exposure and myocardial drug accumulation**. Cardiomyocytes are particularly exposed because doxorubicin concentrates in mitochondria, of which cardiac muscle has an unusually high fraction by volume. *(Demonstrated — Ichikawa, **PMID:24382354**)*

2. **Myocardial drug accumulation** *branches* into three coupled arms:

   **Arm A — the topoisomerase-IIβ arm (the dominant, best-evidenced initiating lesion).**

   2A. Doxorubicin intercalates into cardiomyocyte DNA and forms a **ternary Top2β–DNA–drug cleavage complex**. TOP2A, the antitumour target, is not expressed in terminally differentiated cardiomyocytes; TOP2B is, throughout the cell cycle including in quiescent cells. *(Demonstrated)*

   2A.1 The trapped complex *results in* **DNA double-strand breaks** (`GO:0006302` *double-strand break repair* ✓cached, as the countervailing process).

   2A.2 Top2β-dependent transcriptome remodelling *leads to* **defective mitochondrial biogenesis** — specifically, downregulation of PGC-1α (*PPARGC1A*) and PGC-1β and their downstream oxidative-phosphorylation programme.

   2A.3 Defective mitochondrial biogenesis *results in* **reactive oxygen species formation**, which feeds Arm B.

   > "Here we show that cardiomyocyte-specific deletion of Top2b (encoding topoisomerase-IIβ) protects cardiomyocytes from doxorubicin-induced DNA double-strand breaks and transcriptome changes that are responsible for defective mitochondrial biogenesis and ROS formation. Furthermore, cardiomyocyte-specific deletion of Top2b protects mice from the development of doxorubicin-induced progressive heart failure, suggesting that doxorubicin-induced cardiotoxicity is mediated by topoisomerase-IIβ in cardiomyocytes."
   > — Zhang S et al., *Nat Med* 2012;18(11):1639-42 (**PMID:23104132**) · `evidence_source: MODEL_ORGANISM`

   **Arm B — the iron / redox / ferroptosis arm.**

   2B. Doxorubicin **concentrates inside mitochondria** and chelates iron; simultaneously, Nrf2-mediated upregulation of heme oxygenase-1 degrades heme and *results in* **systemic non-heme iron release**.

   > "Administering DOX to mice induced cardiomyopathy with a rapid, systemic accumulation of nonheme iron via heme degradation by Nrf2-mediated up-regulation of Hmox1, which effect was abolished in Nrf2-deficent mice. Conversely, zinc protoporphyrin IX, an Hmox1 antagonist, protected the DOX-treated mice, suggesting free iron released on heme degradation is necessary and sufficient to induce cardiac injury."
   > — Fang X et al., *PNAS* 2019 (**PMID:30692261**) · `evidence_source: MODEL_ORGANISM`

   2B.1 **Mitochondrial iron accumulation** *leads to* Fenton-chemistry ROS generation and **lipid peroxidation of mitochondrial membranes**.

   > "Given that ferroptosis is driven by damage to lipid membranes, we further investigated and found that excess free iron accumulated in mitochondria and caused lipid peroxidation on its membrane. Mitochondria-targeted antioxidant MitoTEMPO significantly rescued DOX cardiomyopathy, supporting oxidative damage of mitochondria as a major mechanism in ferroptosis-induced heart damage." *(ibid.)*

   2B.2 Concurrent **GPX4 downregulation** removes the enzymatic brake on lipid peroxidation, *resulting in* **mitochondria-dependent ferroptosis** (`GO:0097707` *ferroptosis* ✓cached).

   > "we show that DOX downregulated glutathione peroxidase 4 (GPx4) and induced excessive lipid peroxidation through DOX-Fe2+ complex in mitochondria, leading to mitochondria-dependent ferroptosis; we also show that mitochondria-dependent ferroptosis is a major cause of DOX cardiotoxicity."
   > — Tadokoro T et al., *JCI Insight* 2020 (**PMID:32376803**) · `evidence_source: MODEL_ORGANISM`

   2B.3 The human-tissue anchor for this arm — the one observation that is not model-organism-only:

   > "hearts from patients with doxorubicin-induced cardiomyopathy had markedly higher mitochondrial iron levels than hearts from patients with other types of cardiomyopathies or normal cardiac function."
   > — Ichikawa Y et al., *J Clin Invest* 2014;124(2):617-30 (**PMID:24382354**) · `evidence_source: HUMAN_CLINICAL`

   **Arm C — the metabolite arm.**

   2C. Cytosolic carbonyl reductases CBR1/CBR3 reduce doxorubicin to **doxorubicinol**, a C-13 alcohol metabolite that is a poor antitumour agent but a potent inhibitor of cardiac ion pumps (SERCA2a/`ATP2A2` `HGNC:812`, Na⁺/K⁺-ATPase) and of mitochondrial F₀F₁-ATPase. *(Mechanism inferred from enzymology and the CBR1/CBR3 genetic association; the direct in vivo human causal step is not demonstrated.)*

3. **Convergence.** ROS, DNA damage, mitochondrial failure, and ion-pump inhibition converge on **cardiomyocyte energetic failure and impaired excitation–contraction coupling** (`GO:0060048` *cardiac muscle contraction* ✓, `GO:0034614` *cellular response to reactive oxygen species* ✓).

4. **Sarcomeric and cytoskeletal disruption** — myofibrillar loss and sarcomere disarray (`GO:0045214` *sarcomere organization* ✓). Titin haploinsufficiency amplifies this step, which is why *TTNtv* carriers show "sustained contractile dysfunction" (**PMID:30987448**).

5. **Regulated cardiomyocyte death** — ferroptosis is now argued to be the *predominant* form, with apoptosis (`GO:0006915` ✓), necroptosis, and dysregulated autophagy (`GO:0006914` ✓) contributing. Because adult cardiomyocytes are terminally differentiated, this loss is *irreversible* — the defining reason the disease progresses.

6. **Cardiomyocyte loss** *leads to* **compensatory hypertrophy of surviving myocytes, cardiac fibroblast activation, and replacement fibrosis** (`HP:0001685`; `CL:0002548` *fibroblast of cardiac tissue* ✓).

7. **Fibrosis + myocyte loss** *result in* **adverse LV remodelling — chamber dilatation, wall thinning, and falling ejection fraction**. This is the point where the disease becomes detectable by GLS, then by LVEF.

8. **Adverse remodelling** *leads to* **clinical heart failure**, arrhythmia, and, at the extreme, cardiogenic shock and death.

9. **Branch — the surveillance/reversibility branch.** Between steps 6 and 8 there is a therapeutic window in which neurohormonal blockade produces substantial functional recovery (see §11). Beyond it, recovery falls off sharply. This branch is what makes early detection a mechanistic, not merely a logistic, question.

### 6.2 Molecular pathways

- **DNA topoisomerase type II activity** — `GO:0003918` *DNA topoisomerase type II (double strand cut, ATP-hydrolyzing) activity* *(verified via OLS4)*; the relevant enzyme is TOP2B (`hgnc:11990`, verified)
- **DNA damage response / DSB repair** — `GO:0006302` ✓; ATM–p53 signalling downstream
- **PGC-1α/β mitochondrial biogenesis programme** — via *PPARGC1A/B*; KEGG `hsa04714`, Reactome R-HSA-1592230
- **Nrf2–ARE antioxidant response** — *NFE2L2* (`HGNC:7782`) → *HMOX1* (`HGNC:5013`); paradoxically injurious here because HMOX1 induction liberates free iron
- **Ferroptosis pathway** — GPX4 (`HGNC:4556`), ACSL4, system x_c⁻; KEGG `hsa04216`
- **Iron homeostasis** — ABCB8 (`HGNC:49`) mitochondrial iron export; note **`GO:0055072` is obsolete** — use `GO:0006879` *intracellular iron ion homeostasis* *(verified via OLS4)*
- **Retinoic-acid receptor signalling** — RARG (`hgnc:9866`) → *TOP2B* transcriptional repression
- **ERK/MAPK** — cardioprotective; suppressed in RARG-variant cardiomyocytes (**PMID:34525346**)
- **Neuregulin-1/ERBB2 cardiomyocyte survival** — the pathway trastuzumab blocks, explaining anthracycline–trastuzumab synergy
- **NLRP3 inflammasome / IL-1β** — sterile inflammation amplifying injury; increasingly reported, not yet definitive

### 6.3 Cellular processes

| Process | GO term | Status |
|---|---|---|
| Ferroptosis | `GO:0097707` ✓cached | Now argued dominant |
| Apoptotic process | `GO:0006915` ✓ | Established, `modifier: INCREASED` |
| Autophagy | `GO:0006914` ✓ | Dysregulated (both blocked flux and excess initiation reported) |
| Response to oxidative stress | `GO:0006979` ✓ | Established |
| Cellular response to reactive oxygen species | `GO:0034614` ✓ | Established |
| Mitochondrion organization | `GO:0007005` ✓ | `modifier: DECREASED` (biogenesis defect) |
| Double-strand break repair | `GO:0006302` ✓ | Overwhelmed |
| Cellular senescence | `GO:0090398` ✓ | Reported in cardiac fibroblasts and endothelium |
| Sarcomere organization | `GO:0045214` ✓ | `modifier: DECREASED` |
| Cardiac muscle contraction | `GO:0060048` ✓ | `modifier: DECREASED` |
| Intracellular iron ion homeostasis | `GO:0006879` (verified) | `modifier: DECREASED` / disrupted |

### 6.4 Protein dysfunction

- **TOP2B** — not misfolded; *trapped* as a covalent cleavage complex on DNA. This is a poisoned-enzyme mechanism, closer to a gain of toxic function than to loss of function, and should be modeled with `Descriptor.modifier` on the process rather than `functional_impact_category` (no host variant is required).
- **GPX4** — downregulated protein abundance, loss of peroxidase activity
- **SERCA2a (*ATP2A2*)** — inhibited by doxorubicinol; impaired calcium reuptake
- **Titin** — truncated in the *TTNtv* subgroup, reducing sarcomeric reserve
- **Mitochondrial complexes I/III** — sites of doxorubicin one-electron redox cycling generating superoxide
- **ABCB8** — capacity-limited mitochondrial iron export; overexpression is protective in mice

### 6.5 Metabolic changes

- Shift away from fatty-acid β-oxidation toward glycolysis (the fetal metabolic programme of failing myocardium)
- Reduced oxidative phosphorylation capacity and ATP output
- Depleted reduced glutathione; NADPH consumption by redox cycling
- Accumulation of oxidized phospholipid species (the ferroptosis lipidomic signature — hydroperoxy-PE species)
- Cardiac creatine/phosphocreatine depletion

### 6.6 Immune system involvement

Sterile inflammation rather than autoimmunity. DAMPs released from dying cardiomyocytes activate resident and recruited macrophages (`CL:0000763` *myeloid cell* ✓, or a cardiac macrophage term); NLRP3-inflammasome activation and IL-1β/IL-6 elevation are reported. No autoantibody or immunodeficiency component. This is a secondary amplifier, not an initiator — place it downstream in the pathograph.

### 6.7 Tissue damage mechanisms

Oxidative stress, iron-catalysed lipid peroxidation, DNA double-strand breakage, mitochondrial permeability transition, myocyte necrosis/ferroptosis, and replacement fibrosis. Ischaemia is *not* a primary mechanism — coronary arteries are typically spared, which distinguishes AIC from ischaemic cardiomyopathy at biopsy and on CMR.

### 6.8 Molecular profiling

- **Transcriptomics:** anthracyclines produce a *shared* cardiomyocyte gene-expression response across TOP2-inhibiting agents, suggesting a common transcriptional signature rather than agent-specific programmes (see PMC10927150 / the associated bioRxiv preprint; verify the published PMID before citing). GEO holds multiple hiPSC-CM doxorubicin exposure series — search `doxorubicin cardiomyocyte` in GEO and triage for relevance before recording any `datasets:` accession (**relevance triage is mandatory; resolution is not relevance**).
- **Proteomics:** PRIDE/ProteomeXchange hold doxorubicin-treated cardiomyocyte and murine heart datasets; no consensus signature.
- **Metabolomics/lipidomics:** oxidized phosphatidylethanolamine species are the mechanistically anchored lipidomic readout (LIPID MAPS); acylcarnitine accumulation reflects the β-oxidation block.
- **Single-cell:** cardiac macrophage, fibroblast, and endothelial responses have been profiled in murine DIC; human single-cell AIC data are sparse.
- **Functional genomics:** hiPSC-CM CRISPR and pharmacogenomic screens (Burridge/Magdy programme) are the productive platform; DepMap is not informative for a non-cancer cardiac phenotype.

---

## 7. Anatomical Structures Affected

### 7.1 Organ level

- **Primary:** heart — `UBERON:0000948` *heart* ✓cached
- **Predominant chamber:** left ventricle — `UBERON:0002084` *heart left ventricle* ✓; myocardium `UBERON:0002349` ✓; left ventricle myocardium `UBERON:0006566` ✓
- **Right ventricle:** involved, and increasingly recognized as an early site; historically under-imaged
- **Secondary organ involvement (all consequences of heart failure, not direct toxicity):** lungs (congestion, pleural effusion), liver (congestive hepatopathy), kidneys (cardiorenal syndrome), skeletal muscle (deconditioning)
- **Body systems:** cardiovascular (primary); respiratory, hepatic, renal (secondary)

### 7.2 Tissue and cell level

| Structure | Term |
|---|---|
| Cardiac muscle tissue | `UBERON:0001133` ✓ |
| Cardiac muscle cell (the primary target) | `CL:0000746` *cardiac muscle cell* ✓ |
| Cardiac fibroblast (fibrotic response) | `CL:0002548` *fibroblast of cardiac tissue* ✓ |
| Endothelial cell (microvascular injury) | `CL:0000115` *endothelial cell* ✓ |
| Endocardial cell | `CL:0002350` ✓ |
| Myeloid cell / cardiac macrophage | `CL:0000763` ✓ |
| Vascular smooth muscle cell | `CL:0000359` ✓ |

Cardiac progenitor/stem cell depletion is a proposed additional mechanism, particularly relevant to the paediatric phenotype where the heart still needs to grow. Treat as `EMERGING`.

### 7.3 Subcellular level (GO Cellular Component)

- **Mitochondrion** (`GO:0005739`) — the central compartment: drug concentration, iron accumulation, lipid peroxidation, biogenesis failure
- **Nucleus** (`GO:0005634`) — TOP2B cleavage complexes, DNA DSBs
- **Sarcomere** (`GO:0030017`) / **myofibril** (`GO:0030016`) — structural disarray
- **Sarcoplasmic reticulum** (`GO:0016529`) — SERCA2a inhibition, calcium mishandling
- **Mitochondrial inner membrane** (`GO:0005743`) — site of lipid peroxidation and ETC redox cycling

*These GO CC IDs are the standard ones but were not machine-verified in this pass; confirm before binding.*

### 7.4 Localization and laterality

**Global and biventricular**, not regional. This is diagnostically important: a *regional* wall-motion abnormality argues for coronary disease rather than AIC. On CMR, diffuse extracellular volume expansion without an infarct-pattern late-gadolinium-enhancement territory is the expected picture.

---

## 8. Temporal Development

### 8.1 Onset

- **Age:** any — from infancy (paediatric oncology) to the ninth decade. Bimodal risk peaks in very young children and adults >65.
- **Pattern:** predominantly **insidious and asymptomatic at onset**. Acute onset (arrhythmia, myopericarditis within days) is rare.

### 8.2 The timing revision — the single most consequential recent finding

The classical acute / early-chronic / late-chronic trichotomy is substantially wrong about *when* the injury declares itself. In the largest prospective protocolized-echo cohort (n=2,625, median follow-up 5.2 years):

> "The overall incidence of cardiotoxicity was 9% (n=226). The median time elapsed between the end of chemotherapy and cardiotoxicity development was 3.5 (quartile 1 to quartile 3, 3-6) months. In 98% of cases (n=221), cardiotoxicity occurred within the first year."
> — Cardinale D et al., *Circulation* 2015;131(22):1981-8 (**PMID:25948538**)

> "Three types of anthracycline-induced cardiotoxicities are currently recognized: acute, early-onset chronic, and late-onset chronic. However, data supporting this classification are lacking." *(ibid.)*

The reconciliation with survivorship data is that **"late-onset" cardiomyopathy is largely early subclinical injury that was never looked for**, plus the additional stress of somatic growth and ageing on a depleted myocyte pool. Both facts are true and belong in the entry: injury is early, *manifestation* can be decades later.

### 8.3 Progression and stages

Map to the ESC CTRCD severity ladder (§3.5) as `stages`:
1. **Subclinical injury** — troponin rise, GLS decline >15% relative, LVEF preserved ≥50%
2. **Mild asymptomatic CTRCD** — as above, formally graded
3. **Moderate asymptomatic CTRCD** — LVEF 40–49%
4. **Severe asymptomatic CTRCD** — LVEF <40%
5. **Symptomatic HF** — mild → moderate → severe (hospitalization) → very severe (inotropes/MCS/transplant)

**Rate:** variable. Most decline occurs within 12 months of the last dose; thereafter slow progression or plateau, with a second late slope in long-term survivors.

**Course:** progressive rather than relapsing–remitting; the paediatric course can be biphasic (early dysfunction, apparent stabilization, late deterioration around growth spurts and pregnancy).

**Duration:** chronic and lifelong once established.

### 8.4 Remission and recovery

**Treatment-induced, and steeply time-dependent.** Cardinale's recovery data are the key numbers:

> "Twenty-five (11%) patients had full recovery, and 160 (71%) patients had partial recovery."
> — **PMID:25948538**

> "Most cardiotoxicity after anthracycline-containing therapy occurs within the first year and is associated with anthracycline dose and LVEF at the end of treatment. Early detection and prompt therapy of cardiotoxicity appear crucial for substantial recovery of cardiac function." *(ibid.)*

Spontaneous remission without therapy is uncommon.

### 8.5 Critical periods

- **During and immediately after chemotherapy** — the window for primary prevention (dexrazoxane, liposomal formulation, statin, ACEi/ARB)
- **First 12 months post-treatment** — the window where nearly all incident dysfunction appears and where prompt HF therapy yields recovery
- **Adolescent growth spurt** and **pregnancy** in childhood-cancer survivors — periods of increased haemodynamic demand that unmask latent dysfunction

---

## 9. Inheritance and Population

### 9.1 Epidemiology

**There is no single prevalence figure, and reporting one without its case definition is misleading.** Anchor points:

| Population / definition | Figure | Source |
|---|---|---|
| Prospective cohort, LVEF decline >10 points to <50%, adults | **9%** overall incidence | Cardinale 2015, **PMID:25948538** |
| Doxorubicin 550 mg/m², clinical CHF, adults | **26%** estimated cumulative | Swain 2003, **PMID:12767102** |
| Doxorubicin 400 mg/m², clinical CHF, adults | ~5% (widely cited from the same dataset) | Swain 2003 |
| Childhood cancer protocols, asymptomatic dysfunction | **up to 57%** | Aminkeng 2015, **PMID:26237429** |
| Childhood cancer protocols, congestive heart failure | **up to 16%** | Aminkeng 2015, **PMID:26237429** |
| Meta-analysis, LVEF decline at median 9 y | **6%** overt, **18%** subclinical | cited in Camilli 2024, **PMID:39479333** |
| CCSS survivors vs siblings, CHF | **HR 5.9 (95% CI 3.4–9.6)** | Mulrooney 2009, **PMID:19996459** |
| CARDIOTOX registry, any CTRCD incl. mild asymptomatic | **67.3%** (n=718/1066) | Rivero-Santana 2025, **PMID:39106857** |

That last row deserves emphasis — under the ESC 2022 definition, which counts a >15% relative GLS decline as mild CTRCD, two-thirds of anthracycline-treated patients meet criteria. The definition, not the biology, moved. Any `prevalence` record here **must** carry `measure_type` and a `notes:` line naming the case definition, or it will be uninterpretable.

Suggested structured record shape:

```yaml
prevalence:
- population: Adults receiving anthracycline-containing chemotherapy (prospective cohort, Italy)
  measure_type: PERIOD_PREVALENCE
  prevalence_class: COMMON
  rate_per_100000: 9000.0
  notes: >-
    9% incidence of LVEF decline >10 absolute points to <50% over median 5.2 years;
    98% of events within the first year. Not comparable with ESC-2022 CTRCD rates,
    which include mild asymptomatic GLS-defined cases.
```

### 9.2 Inheritance

**Not a heritable disease.** Do not populate `inheritance:` with a Mendelian mode. If an inheritance block is used at all, `HP:0010982` *Polygenic inheritance* with `relationship_type: SUSCEPTIBILITY` gene typing is the only defensible framing, and even that is a stretch — the susceptibility architecture is a handful of common variants plus a rare-variant tail, acting only in the presence of exposure.

- **Penetrance / expressivity / anticipation / mosaicism / founder effects / consanguinity / carrier frequency:** **Not applicable.**
- The one partial exception is the *TTNtv* subgroup, where a genuinely inherited, autosomal-dominant DCM predisposition is unmasked by exposure. Model that as a `MODIFIER`/`SUSCEPTIBILITY` genetic entry with a `discussions` note, not as an inheritance mode for AIC.

### 9.3 Population demographics

- **Affected populations:** anyone exposed. Ancestry-specific risk-allele frequencies differ (the RARG GWAS replicated in both European and non-European cohorts — 96 European and 80 non-European replication patients), but population-level differences in AIC risk are driven mainly by differences in treatment protocols and access to surveillance.
- **Geographic distribution:** worldwide, tracking anthracycline use. No endemic pattern.
- **Sex ratio:** In paediatric cohorts, female sex is a risk factor and girls derive greater dexrazoxane benefit (**PMID:20850381**). In the adult CARDIOTOX validation cohort, 81.9% were women — but that reflects the breast-cancer-heavy case mix, not a sex-specific susceptibility. Do not read a sex ratio out of a cohort's cancer distribution.
- **Age distribution:** bimodal risk (young children, adults ≥65); the CARDIOTOX cohort mean age was 54 ± 14 years with 24.5% ≥65.

---

## 10. Diagnostics

### 10.1 Imaging — the diagnostic backbone

| Modality | Role | NCIT |
|---|---|---|
| **Transthoracic echocardiography with 3D LVEF and GLS** | First-line, serial | Search NCIT for *Echocardiography*; not verified this pass |
| **Global longitudinal strain (GLS)** | Earliest routine functional marker; >15% *relative* decline defines mild CTRCD | — |
| **Cardiac MRI** | Reference standard for LVEF; T1 mapping/ECV quantifies diffuse fibrosis and oedema; used when echo is non-diagnostic | — |
| **MUGA / radionuclide ventriculography** | Historic; reproducible LVEF, but radiation and no strain — largely superseded | — |
| **CT** | Only for coronary exclusion | — |

The **SUCCOUR** trial tested whether GLS should *drive* therapy rather than merely detect injury:

> "In this international, multicenter, prospective, randomized controlled trial, 331 anthracycline-treated patients with another heart failure risk factor were randomly allocated to CPT initiation guided by either ≥12% relative reduction in GLS (n = 166) or >10% absolute reduction of LVEF (n = 165)."
> — Thavendiranathan P et al., *J Am Coll Cardiol* 2021;77(4):392-401 (**PMID:33220426**); 3-year follow-up: Negishi T et al., *JACC Cardiovasc Imaging* 2023 (**PMID:36435732**)

### 10.2 Biomarkers

- **Cardiac troponin I / T (including high-sensitivity assays)** — the earliest signal of injury and the best-validated risk stratifier:

  > "TnI release pattern after high-dose chemotherapy identifies patients at different risks of cardiac events in the 3 years thereafter."
  > — Cardinale D et al., *Circulation* 2004;109(22):2749-54 (**PMID:15148277**)

  > "In the TnI-/- group, no significant reduction in ejection fraction was observed during the follow-up, and there was a very low incidence of cardiac events (1%). In contrast, a greater incidence of cardiac events occurred in TnI-positive patients, particularly in the TnI(+/+) group (84% versus 37% in the TnI+/- group; P<0.001)." *(ibid.)*

  Note the study's threshold was ≥0.08 ng/mL on a contemporary-generation assay — **do not carry that cut-point forward to a high-sensitivity assay.**

- **Natriuretic peptides (BNP, NT-proBNP)** — ESC recommends baseline measurement if they are to be used in follow-up.
- **Circulating miRNAs** — investigational; reviewed in **PMID:38774014**. Not clinically actionable.
- **Emerging plasma panels** in childhood survivors — Leerink JM et al., *J Am Heart Assoc* 2022 (**PMID:35861824**).

### 10.3 Electrophysiology

12-lead ECG at baseline and during surveillance: sinus tachycardia, non-specific ST/T changes, reduced QRS voltage, QTc prolongation, and (late) conduction disease. ECG is neither sensitive nor specific for AIC and is used for arrhythmia detection and as a red flag, not for diagnosis.

### 10.4 Biopsy and pathology

- **Endomyocardial biopsy** — `NCIT:C51674` *Endomyocardial Biopsy* ✓cached. Historically the gold standard, using the **Billingham grading scale** (0 to 3, scoring myofibrillar loss, cytoplasmic vacuolization of cardiomyocytes, and myocyte necrosis on electron microscopy). Now rarely performed: it is invasive, samples the right ventricle, and has been displaced by strain and CMR. Retain it as a differential-diagnosis tool when myocarditis or infiltrative disease is in play.
- **Characteristic histopathology:** myocyte vacuolization ("adria cells"), myofibrillar dropout, interstitial and perivascular fibrosis, absence of significant inflammatory infiltrate (which is what distinguishes it from myocarditis), and on EM, distended sarcoplasmic reticulum and swollen mitochondria.

### 10.5 Genetic testing

- **No diagnostic genetic test exists for AIC.** Genotype is not part of any guideline diagnostic pathway.
- **Cardiomyopathy gene panel** has an emerging *risk-stratification* role, given the *TTNtv* finding (**PMID:30987448**). ClinGen-curated DCM panels (*TTN*, *LMNA*, *MYH7*, *BAG3*, *RBM20*, *FLNC*, *DSP*, etc.) are the relevant gene set. This is not yet standard of care; frame it as a `discussions` / `KNOWLEDGE_GAP` item.
- **Pharmacogenomic genotyping** (*RARG*, *CBR3*, *SLC28A3*, *UGT1A6*) — CPNDS has proposed clinical recommendations; **not** in CPIC guidelines and **not** in the FDA Table of Pharmacogenomic Biomarkers as of this writing. Check PharmGKB for current level-of-evidence assignments before asserting clinical actionability.
- WGS/WES, CMA, karyotyping, FISH, mtDNA testing, repeat-expansion testing: **not applicable.**

### 10.6 Clinical criteria

**ESC 2022 / IC-OS CTRCD definitions** (§3.5) are the operative diagnostic criteria (**PMID:36017568**). ASCO's 2017 survivorship guideline (**PMID:27918725**) covers monitoring in adult survivors.

### 10.7 Differential diagnosis

| Alternative | Distinguishing features |
|---|---|
| **Ischaemic cardiomyopathy** | Regional wall-motion abnormality; subendocardial/transmural LGE in a coronary territory; obstructive CAD on angiography. AIC is global. |
| **Trastuzumab-mediated cardiac dysfunction** | Typically reversible on drug cessation, non-dose-dependent, no myocyte necrosis. Distinguishing the two in a patient who got both is often impossible and is a genuine knowledge gap. |
| **Immune checkpoint inhibitor myocarditis** | Fulminant course, marked troponin elevation, lymphocytic infiltrate on biopsy, conduction disease. |
| **Familial/genetic DCM** | Family history, earlier onset relative to exposure, causative variant. Note the overlap: *TTNtv* carriers sit in both categories. |
| **Peripartum cardiomyopathy** | Temporal relation to pregnancy; a real confounder in young survivors. |
| **Radiation-induced heart disease** | Pericardial constriction, valvular thickening, coronary ostial disease, conduction disease. Frequently *co-occurs* rather than being an alternative. |
| **Cardiac amyloidosis / infiltrative disease** | Increased wall thickness with low voltage, apical-sparing strain pattern, characteristic CMR. |
| **Takotsubo / stress cardiomyopathy** | Apical ballooning, rapid recovery. |
| **Sepsis- or thyrotoxicosis-related cardiomyopathy** | Reversible, systemic trigger identifiable. |

### 10.8 Screening

- **Baseline risk assessment before the first dose** — HFA-ICOS proforma (validated: **PMID:39106857**). Baseline echo with GLS plus troponin and natriuretic peptide in anyone who will be followed with them.
- **On-treatment surveillance** — frequency by risk tier; high/very-high risk patients get echo/biomarkers before alternate cycles and at cumulative-dose milestones.
- **Post-treatment** — echo at end of therapy and at 12 months is the highest-yield schedule, since 98% of events fall in the first year (**PMID:25948538**).
- **Long-term survivorship** — lifelong periodic echo per Children's Oncology Group / IGHG survivorship guidelines, risk-stratified on cumulative dose and chest radiation.
- **Cascade/carrier screening:** not applicable, except that a *TTNtv* found incidentally has family implications.

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality

- AIC is a leading non-cancer cause of death in long-term cancer survivors. Historical series of established, untreated anthracycline cardiomyopathy reported ~50% 2-year mortality — a figure that predates modern HF therapy and should be cited as historical, not current.
- CCSS: survivors were "significantly more likely than siblings to report congestive heart failure (hazard ratio (HR) 5.9, 95% confidence interval 3.4 to 9.6; P<0.001)" and "The cumulative incidence of adverse cardiac outcomes in cancer survivors continued to increase up to 30 years after diagnosis" (**PMID:19996459**).
- CARDIOTOX: "A total of 197 patients (18.4%) died" over median 54.8 months, with mortality rising steeply across HFA-ICOS strata (HR 7.43 for very high risk) (**PMID:39106857**).

### 11.2 Recovery potential — the most actionable prognostic fact

Recovery is common **if therapy starts early**, and this is the central argument for surveillance: 11% full and 71% partial recovery when HF therapy was initiated at detection (**PMID:25948538**). Recovery probability falls sharply with time from LVEF decline to treatment initiation.

*Modeling note:* this makes "time from detection to therapy" a legitimate prognostic factor node, not merely a process metric.

### 11.3 Morbidity, disability, quality of life

Chronic heart failure with its full functional burden: exercise limitation, recurrent hospitalization, polypharmacy, device therapy, and — in the paediatric survivor population — a decades-long trajectory interacting with growth, pregnancy, and other late effects. QoL measured with generic instruments (EQ-5D, SF-36, PROMIS) and HF-specific tools (KCCQ, MLHFQ); no AIC-specific instrument.

### 11.4 Complications

Progressive HF; atrial and ventricular arrhythmia; thromboembolism from a dilated, poorly contracting ventricle; secondary mitral regurgitation; pulmonary hypertension; cardiorenal syndrome; sudden cardiac death; and — the oncologic complication that is easy to overlook — **curtailment of curative cancer therapy**.

### 11.5 Prognostic factors and biomarkers

- Cumulative anthracycline dose (dose-equivalent adjusted)
- **End-of-chemotherapy LVEF** — "end-chemotherapy LVEF (hazard ratio, 1.37; 95% confidence interval, 1.33-1.42 for each percent unit decrement) and cumulative doxorubicin dose (hazard ratio, 1.09; 95% confidence interval, 1.04-1.15 for each 50 mg/m(2) increment) were independent correlates of cardiotoxicity" (**PMID:25948538**)
- Troponin release pattern — persistent elevation (TnI+/+) carries an 84% cardiac-event rate (**PMID:15148277**)
- Baseline HFA-ICOS risk category (**PMID:39106857**)
- Time from LVEF decline to HF therapy initiation
- Concomitant chest radiotherapy
- Age, sex, pre-existing cardiovascular disease
- **Genotype:** *TTNtv* carriers show "impaired myocardial recovery (P=0.03)" (**PMID:30987448**) — a genotype→prognosis edge worth modeling explicitly
- CMR ECV / late gadolinium enhancement burden (emerging)

---

## 12. Treatment

### 12.1 Established heart-failure pharmacotherapy (treatment of established AIC)

Guideline-directed medical therapy for HFrEF applies without modification. All are `treatment_term: NCIT:C15986` *Pharmacotherapy* ✓cached, with `therapeutic_agent` carrying the drug and `therapeutic_modality: SMALL_MOLECULE` (or `MONOCLONAL_ANTIBODY` where relevant).

| Class | Example agent | CHEBI | Verified? |
|---|---|---|---|
| ACE inhibitor | enalapril | `CHEBI:4784` | ✓cached |
| ARB | candesartan | `CHEBI:3347` | verified via OLS4 |
| Beta blocker (non-selective, antioxidant) | carvedilol | `CHEBI:3441` | ✓cached |
| MRA | spironolactone | `CHEBI:9241` | ✓cached |
| SGLT2 inhibitor | empagliflozin / dapagliflozin | `CHEBI:82720` / `CHEBI:85078` | ✓cached |
| ARNI | sacubitril/valsartan | look up before binding | not verified |
| Loop diuretic | furosemide | look up before binding | not verified |

### 12.2 Primary prevention — cardioprotective strategies

**Dexrazoxane** — the only agent licensed specifically for this indication. `CHEBI:50223` (label *(+)-dexrazoxane*, verified) / `NCIT:C1333` *Dexrazoxane* (verified). Mechanism: EDTA-analogue iron chelation plus catalytic-cycle inhibition of TOP2B — note that both arms of the core mechanism are addressed, which is why it works.

Cochrane, 13 RCTs, 2,521 participants:

> "In adults, moderate-quality evidence showed that there was less clinical heart failure with the use of dexrazoxane (risk ratio (RR) 0.22, 95% confidence interval (CI) 0.11 to 0.43; 7 studies, 1221 adults). In children, we identified no difference in clinical heart failure risk between treatment groups (RR 0.20, 95% CI 0.01 to 4.19; 3 studies, 885 children; low-quality evidence)."
> — de Baat EC et al., *Cochrane Database Syst Rev* 2022;9:CD014638 (**PMID:36162822**)

> "Overall survival (OS) was reported in adults and overall mortality in children. The meta-analyses of both outcomes showed no difference between treatment groups (hazard ratio (HR) 1.04, 95% 0.88 to 1.23; 4 studies; moderate-quality evidence...)" *(ibid.)* — i.e., **the historical concern that dexrazoxane blunts antitumour efficacy is not supported.**

Long-term paediatric follow-up:

> "Dexrazoxane provides long-term cardioprotection without compromising oncological efficacy in doxorubicin-treated children with high-risk ALL. Dexrazoxane exerts greater long-term cardioprotective effects in girls than in boys."
> — Lipshultz SE et al., *Lancet Oncol* 2010;11(10):950-61 (**PMID:20850381**)

Regulatory label restricts use to metastatic breast cancer beyond 300 mg/m² cumulative doxorubicin, which is narrower than the evidence supports — a live practice/label mismatch worth recording in `notes:`.

**Liposomal doxorubicin** — reformulation reduces myocardial delivery while preserving tumour delivery via the EPR effect. "In five trials comparing liposomal doxorubicin (LD) with conventional doxorubicin, LD reduced the risk of clinical heart failure (OR 0.18, 0.08–0.38) and subclinical heart failure (RR 0.31, 0.20–0.48)" (meta-analysis; verify the PMID for the specific systematic review before citing — candidates surfaced include **PMID:41084073**). Formally recommended by ESC for CTRCD prevention (**PMID:36017568**).

**Statins.** STOP-CA is the strongest randomized evidence:

> "The incidence of the primary end point was 9% (13/150) in the atorvastatin group and 22% (33/150) in the placebo group (P = .002). The odds of a 10% or greater decline in LVEF to a final value of less than 55% after anthracycline treatment was almost 3 times greater for participants randomized to placebo compared with those randomized to atorvastatin (odds ratio, 2.9; 95% CI, 1.4-6.4)."
> — Neilan TG et al., *JAMA* 2023;330(6):528-536 (**PMID:37552303**) · NCT02943590

> "There were 13 adjudicated heart failure events (4%) over 24 months of follow-up. There was no difference in the rates of incident heart failure between study groups (3% with atorvastatin, 6% with placebo; P = .26)." *(ibid.)*

That second quote is the honest limitation and should be curated alongside the first: the trial moved an imaging endpoint, not a clinical heart-failure endpoint. Curate as `SUPPORT` with `directness: INDIRECT` for any claim about preventing heart failure.

**Neurohormonal prophylaxis.** PRADA:

> "The overall decline in LVEF was 2.6 (95% CI 1.5, 3.8) percentage points in the placebo group and 0.8 (95% CI −0.4, 1.9) in the candesartan group in the intention-to-treat analysis (P-value for between-group difference: 0.026). No effect of metoprolol on the overall decline in LVEF was observed."
> — Gulati G et al., *Eur Heart J* 2016;37(21):1671-80 (**PMID:26903532**) · a 2.6-point vs 0.8-point difference is real but small; do not over-claim it.

**Administration-schedule modification** — prolonged infusion rather than bolus; dose capping.

**SGLT2 inhibitors — emerging.** EMPACARD-PILOT (**PMID:39237985**) and the PROTECT trial (dapagliflozin; registered 2024-03-19) are the active programme; observational data suggest benefit. Curate as `EMERGING` with a `discussions` knowledge-gap entry, not as established therapy.

### 12.3 Advanced and device therapy

- **Cardiac resynchronization therapy** — `NCIT:C80436` ✓cached — for eligible patients with wide QRS
- **ICD** for primary/secondary arrhythmic prevention
- **Mechanical circulatory support (LVAD)** as bridge or destination
- **Heart transplantation** — `NCIT:C15246` *Heart Transplantation* ✓cached — feasible in cancer survivors with adequate oncologic remission duration; AIC is a recognized transplant indication
- **Gene, cell, RNA-based, and targeted therapies:** none approved. Investigational: TOP2B antisense oligonucleotide (ASO-18) reported cardioprotective versus dexrazoxane in a mouse AIC model (**PMID:42102394** — 2026, preclinical, unreplicated); RARG agonist CD1530 (**PMID:34525346** — hiPSC-CM and mouse); ferroptosis inhibitors (ferrostatin-1, MitoTEMPO) preclinical only.

### 12.4 Supportive and rehabilitative

- Sodium and fluid management, symptom-directed diuresis — `NCIT:C15747` *Supportive Care* ✓cached
- **Cardiac rehabilitation / structured exercise training** — increasingly recommended both during and after therapy; `therapeutic_modality: BEHAVIORAL`
- Cardiovascular risk-factor management (BP, lipids, glycaemia, smoking cessation)

### 12.5 Pharmacogenomics

No CPIC guideline and no FDA pharmacogenomic labelling for anthracyclines as of this writing. CPNDS has published *RARG*/*SLC28A3*/*UGT1A6* recommendations. Verify current PharmGKB level-of-evidence assignments before asserting any actionable genotype-guided recommendation — this is exactly the kind of claim that ages badly.

### 12.6 Treatment algorithm

1. Baseline HFA-ICOS risk stratification + echo with GLS + troponin/NP
2. Risk-adapted primary prevention: dexrazoxane and/or liposomal formulation and/or dose capping for high/very-high risk; consider statin
3. On-treatment surveillance at risk-adapted intervals
4. On detection of CTRCD: grade by ESC criteria; start ACEi/ARB + beta blocker (carvedilol) promptly; do not wait for symptoms
5. Multidisciplinary cardio-oncology decision on continuing versus modifying versus stopping anthracycline — a genuine risk-benefit trade, since stopping curative chemotherapy has its own mortality
6. Escalate to full GDMT (add MRA, SGLT2i, ARNI) for established HFrEF
7. Device therapy, MCS, transplant for refractory disease
8. Lifelong survivorship surveillance

---

## 13. Prevention

### 13.1 Primary prevention (preventing the cardiomyopathy)

- **Avoid the exposure where an equally effective non-anthracycline regimen exists** — the only fully effective prevention, and increasingly available in breast cancer
- **Cumulative dose limitation**, using cardiotoxicity-calibrated equivalence ratios (**PMID:30703192**) rather than hematologic-toxicity ratios
- **Dexrazoxane** in high-risk patients (**PMID:36162822**, **PMID:20850381**)
- **Liposomal formulation** (ESC-recommended)
- **Prolonged infusion** rather than bolus
- **Atorvastatin 40 mg daily for 12 months** in lymphoma patients (**PMID:37552303**)
- **Candesartan** during adjuvant therapy (**PMID:26903532**)
- **Pre-treatment cardiovascular risk-factor optimization** — BP, lipids, glycaemia, weight, smoking
- **Minimize concurrent cardiac radiation dose** — modern conformal/proton techniques

### 13.2 Secondary prevention (early detection, treat before symptoms)

This is where the field's leverage is. The evidence chain — troponin identifies subclinical injury (**PMID:15148277**) → GLS identifies functional decline before LVEF (**PMID:33220426**) → early HF therapy yields 82% partial-or-full recovery (**PMID:25948538**) — is the strongest argument in cardio-oncology and should be modeled as an explicit causal chain in the entry, not as three unrelated diagnostic facts.

### 13.3 Tertiary prevention

Full GDMT, arrhythmia management, anticoagulation where indicated, cardiac rehabilitation, avoidance of further cardiotoxic exposure (including re-challenge and additional chest radiation), pregnancy counselling in female survivors, and lifelong surveillance.

### 13.4 Risk stratification

The HFA-ICOS baseline proforma is the validated instrument (**PMID:39106857**), available as a calculator. Genotype is not yet part of any validated risk model — an explicit knowledge gap.

### 13.5 Immunization, genetic counselling, public health

- **Immunization:** not applicable to AIC as such; routine vaccination is standard supportive care for immunosuppressed oncology patients.
- **Genetic counselling:** not routine. Becomes relevant only when a *TTNtv* or other DCM-associated variant is identified, at which point cascade testing of relatives follows standard inherited-cardiomyopathy practice.
- **Public health / environmental interventions:** not applicable — the exposure is a prescribed therapeutic, so the "environmental intervention" is prescribing policy and formulary choice.

---

## 14. Other Species / Natural Disease

### 14.1 Taxonomy

| Species | NCBI Taxon | Relevance |
|---|---|---|
| *Homo sapiens* | `NCBITaxon:9606` | Primary |
| *Canis lupus familiaris* | `NCBITaxon:9615` | **Naturally occurring** — dogs treated for lymphoma/sarcoma develop AIC |
| *Felis catus* | `NCBITaxon:9685` | Occasional veterinary oncology use |
| *Mus musculus* | `NCBITaxon:10090` | Principal experimental model |
| *Rattus norvegicus* | `NCBITaxon:10116` | Chronic-dosing model |
| *Danio rerio* | `NCBITaxon:7955` | Screening model |
| *Oryctolagus cuniculus* | `NCBITaxon:9986` | Classic chronic cardiomyopathy model |

*Taxon IDs above are the standard ones; verify against the `cache/ncbitaxon` cache before binding.*

### 14.2 Natural disease in other species

This is genuinely a naturally occurring veterinary disease, not merely an induced model — dogs receiving anthracycline chemotherapy for canine multicentric lymphoma develop the same entity:

> "An 8-year-old, castrated, mixed-breed dog was diagnosed with multicentric lymphoma and received multi-agent chemotherapy... After third-line chemotherapy with epirubicin, the patient was diagnosed with dilated cardiomyopathy. The total cumulative doses of doxorubicin, mitoxantrone, and epirubicin were 125, 8, and 125 mg/m2, respectively."
> — Tagawa M et al., *Open Vet J* 2021;11(1):6-10 (**PMID:33898277**) · `evidence_source: MODEL_ORGANISM` (per repository convention, veterinary observations grade as MODEL_ORGANISM)

> "Further studies are required to establish prevention and management strategies for dogs receiving potentially cardiotoxic therapies, such as anthracyclines." *(ibid.)*

**Veterinary relevance is real and practical:** canine lymphoma is one of the most common canine malignancies, doxorubicin is standard of care, and dose limits (~180–240 mg/m² cumulative in dogs) are set by cardiotoxicity. Doberman Pinschers and other breeds with a genetic DCM predisposition are considered higher risk — a natural analogue of the human *TTNtv* finding. Check **VBO** for breed identifiers if breed-specific curation is wanted; check **OMIA** for canine DCM entries.

### 14.3 Comparative biology

- **Conservation:** *TOP2B*, *GPX4*, *ABCB8*, and the mitochondrial biogenesis machinery are broadly conserved across mammals; the core mechanism is not human-specific.
- **Orthologues:** mouse *Top2b*, *Gpx4*, *Abcb8*, *Rarg*, *Cbr1*/*Cbr3*, *Celf4*, *Ttn* — all have one-to-one human orthologues (Alliance of Genome Resources / HomoloGene).
- **Comparative pathology:** the murine and canine lesions both show myocyte vacuolization, myofibrillar loss, and interstitial fibrosis — the same Billingham-type picture as human biopsies.
- **Difference to flag:** rodent hearts have a much higher basal heart rate and different calcium-handling kinetics, so contractile-phenotype timing does not translate directly.

### 14.4 Transmission

**Not applicable** — no zoonotic or cross-species transmission. Cross-species *susceptibility* to the same drug is universal among mammals.

---

## 15. Model Organisms

### 15.1 In vivo models

| Model | Design | Fidelity | Limitations |
|---|---|---|---|
| **Acute high-dose murine DIC** (single 15–20 mg/kg i.p. doxorubicin) | Rapid LV dysfunction over 5–14 days | `PARTIALLY_RECAPITULATES` | Supraclinical dose; substantial systemic toxicity and weight loss confound the cardiac phenotype; does not model the chronic human course |
| **Chronic low-dose murine DIC** (repeated 3–5 mg/kg weekly, cumulative ~20–25 mg/kg) | Progressive dilated phenotype over weeks | `RECAPITULATES` — closest to human | Long, expensive; strain-dependent (C57BL/6 relatively resistant vs. BALB/c) |
| **Cardiomyocyte-specific *Top2b* knockout** (`Top2b^fl/fl`; Myh6-Cre) | The mechanistic proof model | `RESCUES` the phenotype | A loss-of-target model, not a disease model; tells you the target, not the natural history — **PMID:23104132** |
| **ABCB8-overexpressing transgenic mouse** | Mitochondrial iron export | `RESCUES` — **PMID:24382354** | Overexpression is supraphysiological |
| ***Gpx4* Tg and heterodeletion mice** | Bidirectional ferroptosis test | `RESCUES` / worsens respectively — **PMID:32376803** | Same caveat |
| ***Ripk3^−/−*, *Mlkl^−/−*, *Fadd^−/−Mlkl^−/−* mice** | Apoptosis/necroptosis-defective backgrounds, isolating ferroptosis | `RECAPITULATES` ferroptotic death — **PMID:30692261** | Compound knockouts have their own baseline phenotypes |
| ***Nrf2*-deficient mice** | Tests the HMOX1/iron arm | `FAILS_TO_RECAPITULATE` (protected) — **PMID:30692261** | Nrf2 loss has broad pleiotropic effects |
| ***TTNtv* rat/mouse + anthracycline** | Genotype × exposure interaction | `RECAPITULATES` the human genotype effect — **PMID:30987448** | — |
| **Rabbit chronic model** | Weekly doxorubicin, classic CHF model | `RECAPITULATES` | Cost; limited genetic tools |
| **Zebrafish** | Larval and adult doxorubicin exposure | `PARTIALLY_RECAPITULATES` | Cardiomyocytes regenerate in zebrafish — which is precisely the property human hearts lack, so translational validity for the *irreversibility* of the human disease is poor. This is a **`HUMAN_MODEL_MISMATCH`**, not just a limitation |
| **Naturally occurring canine AIC** | Client-owned dogs on anthracycline chemotherapy | `RECAPITULATES` — spontaneous, outbred, clinically monitored — **PMID:33898277** | Case-series level evidence; no controlled dosing |

### 15.2 In vitro / non-animal models (NAMs)

**Patient-specific hiPSC-derived cardiomyocytes are the standout platform**, because they reproduce individual susceptibility, not just the class effect:

> "hiPSC-CMs derived from individuals with breast cancer who experienced DIC were consistently more sensitive to doxorubicin toxicity than hiPSC-CMs from patients who did not experience DIC, with decreased cell viability, impaired mitochondrial and metabolic function, impaired calcium handling, decreased antioxidant pathway activity, and increased reactive oxygen species production."
> — Burridge PW et al., *Nat Med* 2016;22(5):547-56 (**PMID:27089514**) · `evidence_source: IN_VITRO`

> "Taken together, our data indicate that hiPSC-CMs are a suitable platform to identify and characterize the genetic basis and molecular mechanisms of DIC." *(ibid.)*

And they function as a drug-discovery platform for genotype-matched cardioprotection (**PMID:34525346**, CD1530 for *RARG* carriers).

Other in vitro systems:
- **Neonatal rat ventricular myocytes (NRVM)** — the historical workhorse; immature and proliferative, poor fidelity for a terminally differentiated phenotype
- **H9c2 rat cardiomyoblast line** — convenient, low fidelity; not a cardiomyocyte
- **AC16 human cardiomyocyte line** — immortalized, limited fidelity
- **Engineered heart tissue / cardiac organoids and organ-chips** — force-generating 3D constructs with better maturation; the direction of travel for NAM-based cardiotoxicity screening
- **Isolated adult cardiomyocytes and ex vivo Langendorff-perfused hearts** — good for acute contractile and calcium readouts

### 15.3 Model characteristics — what is and is not captured

**Recapitulated well:** myocyte vacuolization and myofibrillar loss; LV systolic dysfunction; mitochondrial iron accumulation; ferroptotic death; TOP2B dependence; genotype-specific susceptibility (hiPSC-CM).

**Not captured:**
- The **decades-long latency** of human late-onset disease — no model runs that long
- **Cumulative-dose scaling** — murine mg/kg regimens do not map cleanly onto human mg/m² cumulative exposure
- **Co-exposure complexity** — real patients get radiation, trastuzumab, taxanes, and cyclophosphamide
- **Comorbidity background** — models are young, healthy, and inbred; patients are older with hypertension, diabetes, and CKD
- **hiPSC-CM maturity** — these cells are fetal-like in metabolism, sarcomere organization, and electrophysiology, which limits inference about a terminally differentiated adult myocyte. Model this explicitly as a `HUMAN_MODEL_MISMATCH` discussion rather than burying it in `limitations` prose.

### 15.4 Resources

MGI, RGD, ZFIN, Alliance of Genome Resources, IMPC/KOMP (for *Top2b*, *Gpx4*, *Abcb8*, *Rarg* alleles), IMSR/JAX for strain availability, Cellosaurus for H9c2/AC16, and the Stanford Cardiovascular Institute and Northwestern Center for Pharmacogenomics hiPSC-CM biobanks.

---

## Knowledge Gaps and Open Questions

Worth curating as `discussions` entries with `kind: KNOWLEDGE_GAP` or `HUMAN_MODEL_MISMATCH`:

1. **Are the ESC-2022 mild-CTRCD cases the same disease as clinical AIC?** Two-thirds of treated patients now meet criteria (**PMID:39106857**). Whether GLS-defined mild dysfunction predicts clinical heart failure, or is a reversible physiological perturbation, is unresolved — and it determines whether a very large number of people should be treated.
2. **Statins move imaging endpoints but not heart-failure endpoints.** STOP-CA was explicit: "There was no difference in the rates of incident heart failure between study groups" (**PMID:37552303**). Whether the surrogate translates is untested.
3. **Should genotype enter clinical risk models?** *TTNtv* has a strong effect and no place in any guideline pathway.
4. **Distinguishing anthracycline from trastuzumab injury** in patients who received both is currently impossible clinically, and blurs the aetiology of a large fraction of breast-cancer CTRCD.
5. **Why is dexrazoxane's label narrower than its evidence?** Cochrane finds RR 0.22 for clinical HF in adults with no survival penalty (**PMID:36162822**), yet approval is restricted to metastatic breast cancer beyond 300 mg/m².
6. **Ferroptosis inhibition has never been tested in humans**, despite being the mechanism with the strongest recent preclinical support and a human-tissue anchor (**PMID:24382354**).
7. **hiPSC-CM immaturity** as a translational limit on the entire pharmacogenomic-screening programme (`HUMAN_MODEL_MISMATCH`).
8. **Zebrafish cardiac regeneration** makes that model structurally unable to test the property that defines the human disease (`HUMAN_MODEL_MISMATCH`).
9. **SGLT2 inhibitors** — mechanistically attractive, observationally supported, awaiting PROTECT and its siblings.

---

## Verification Status of Identifiers in This Report

Because a plausible-but-wrong CURIE passes most automated checks, here is what was actually verified in this pass:

**Machine-verified against the local term caches (`cache/*/terms.csv`):** all HP terms in §3; `CL:0000746`, `CL:0002548`, `CL:0000115`, `CL:0002350`, `CL:0000763`, `CL:0000359`; `UBERON:0000948`, `UBERON:0001133`, `UBERON:0002084`, `UBERON:0002349`, `UBERON:0006566`; `GO:0006302`, `GO:0006914`, `GO:0006915`, `GO:0006979`, `GO:0007005`, `GO:0034614`, `GO:0045214`, `GO:0060048`, `GO:0090398`, `GO:0097707`; `CHEBI:28748`, `CHEBI:41977`, `CHEBI:42068`, `CHEBI:3441`, `CHEBI:4784`, `CHEBI:9241`, `CHEBI:39548`, `CHEBI:82720`, `CHEBI:85078`, `CHEBI:18248`, `CHEBI:29033`; `NCIT:C15632`, `NCIT:C15986`, `NCIT:C15747`, `NCIT:C15246`, `NCIT:C51674`, `NCIT:C80436`, `NCIT:C456`; `hgnc:12403`, `hgnc:11949`, `hgnc:9802`, `hgnc:7577`, `hgnc:6636`, `hgnc:939`, `hgnc:11180`, `hgnc:1516`, `hgnc:2874`, `hgnc:7876`, `hgnc:10484`, `hgnc:4886`.

**Verified live via OLS4 or the HGNC REST API:** `MONDO:0022653`; `CHEBI:47898`, `CHEBI:50223`, `CHEBI:50729`, `CHEBI:3347`; `NCIT:C1333`; `GO:0003918`, `GO:0006879`; `HGNC:11990` (TOP2B), `HGNC:9866` (RARG), `HGNC:1548` (CBR1), `HGNC:1549` (CBR3), `HGNC:14015` (CELF4), `HGNC:4556` (GPX4), `HGNC:49` (ABCB8), `HGNC:16484` (SLC28A3), `HGNC:12538` (UGT1A6), `HGNC:4820` (HAS3), `HGNC:7782` (NFE2L2), `HGNC:5013` (HMOX1), `HGNC:812` (ATP2A2), `HGNC:11989` (TOP2A).

**Explicitly flagged as NOT verified in this pass — look them up before binding:** all ICD-10/ICD-11 codes; all LOINC codes; all GO Cellular Component IDs in §7.3; all NCBITaxon IDs in §14.1; the NCIT terms for echocardiography, CMR, and MUGA; ECTO exposure terms.

**One obsolescence caught:** `GO:0055072` is recorded in the local cache as **obsolete iron ion homeostasis**. Use `GO:0006879` *intracellular iron ion homeostasis* instead.

**Two PMIDs cited from search-engine summaries only, not fetched abstracts** — verify before use as evidence: the *JACC CardioOncology* 2024 functional-validation study naming *RAC2*, and the liposomal-doxorubicin systematic review (**PMID:41084073** is the likely match). The `SLC28A3`, `UGT1A6`, and `HAS3` associations in §4.1 are reported without a fetched primary citation and need one.

---

## Key References

| PMID | Citation | Role |
|---|---|---|
| 23104132 | Zhang S et al. *Nat Med* 2012;18(11):1639-42 | TOP2B is the mechanistic target |
| 24382354 | Ichikawa Y et al. *J Clin Invest* 2014;124(2):617-30 | Mitochondrial iron; human tissue anchor |
| 30692261 | Fang X et al. *PNAS* 2019 | Ferroptosis; Nrf2–HMOX1 iron release |
| 32376803 | Tadokoro T et al. *JCI Insight* 2020 | GPX4 and mitochondria-dependent ferroptosis |
| 26237429 | Aminkeng F et al. *Nat Genet* 2015;47(9):1079-84 | RARG rs2229774 GWAS |
| 34525346 | Magdy T et al. *Cell Stem Cell* 2021;28(12):2076-2089 | RARG mechanism + CD1530 |
| 26811534 | Wang X et al. *J Clin Oncol* 2016 | CELF4 gene–environment interaction |
| 22124095 | Blanco JG et al. *J Clin Oncol* 2012 | CBR1/CBR3; low-dose risk |
| 30987448 | Garcia-Pavia P et al. *Circulation* 2019 | TTN truncating variants |
| 27089514 | Burridge PW et al. *Nat Med* 2016;22(5):547-56 | Patient-specific hiPSC-CM platform |
| 12767102 | Swain SM et al. *Cancer* 2003;97(11):2869-79 | Adult dose–response |
| 30703192 | Feijen EAM et al. *JAMA Oncol* 2019;5(6):864-871 | Cardiotoxicity dose-equivalence ratios |
| 25948538 | Cardinale D et al. *Circulation* 2015;131(22):1981-8 | Timing, incidence, recovery |
| 15148277 | Cardinale D et al. *Circulation* 2004;109(22):2749-54 | Troponin risk stratification |
| 19996459 | Mulrooney DA et al. *BMJ* 2009;339:b4606 | CCSS long-term cardiac outcomes |
| 36017568 | Lyon AR et al. *Eur Heart J* 2022;43(41):4229-4361 | ESC 2022 cardio-oncology guideline |
| 39106857 | Rivero-Santana B et al. *Eur Heart J* 2025;46(3):273-284 | HFA-ICOS risk score validation |
| 27918725 | Armenian SH et al. *J Clin Oncol* 2017 | ASCO survivorship guideline |
| 36162822 | de Baat EC et al. *Cochrane Database Syst Rev* 2022;9:CD014638 | Dexrazoxane meta-analysis |
| 20850381 | Lipshultz SE et al. *Lancet Oncol* 2010;11(10):950-61 | Dexrazoxane long-term paediatric |
| 37552303 | Neilan TG et al. *JAMA* 2023;330(6):528-536 | STOP-CA atorvastatin RCT |
| 26903532 | Gulati G et al. *Eur Heart J* 2016;37(21):1671-80 | PRADA candesartan/metoprolol |
| 33220426 | Thavendiranathan P et al. *J Am Coll Cardiol* 2021;77(4):392-401 | SUCCOUR GLS-guided therapy |
| 36435732 | Negishi T et al. *JACC Cardiovasc Imaging* 2023 | SUCCOUR 3-year results |
| 39479333 | Camilli M et al. *JACC CardioOncol* 2024;6(5):655-677 | State-of-the-art review |
| 38774014 | Boen HM et al. *JACC CardioOncol* 2024;6(2):183-199 | Circulating miRNA biomarkers |
| 33898277 | Tagawa M et al. *Open Vet J* 2021;11(1):6-10 | Naturally occurring canine AIC |
| 42102394 | Wang Q et al. *Cancer Res Commun* 2026 | TOP2B–SMYD1; ASO-18 (preclinical, new) |
| 39237985 | EMPACARD-PILOT | SGLT2 inhibitor pilot |

**Sources (web):**
- [ESC 2022 Guidelines on cardio-oncology — European Heart Journal](https://academic.oup.com/eurheartj/article/43/41/4229/6673995)
- [Anthracycline Cardiotoxicity in Adult Cancer Patients — JACC: CardioOncology (PMC11520218)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11520218/)
- [STOP-CA Randomized Clinical Trial — JAMA](https://jamanetwork.com/journals/jama/fullarticle/2807988)
- [HFA-ICOS risk score validation — PubMed](https://pubmed.ncbi.nlm.nih.gov/39106857/)
- [Cardiotoxicity of doxorubicin is mediated through mitochondrial iron accumulation — JCI](https://www.jci.org/articles/view/72931)
- [Identification of the molecular basis of doxorubicin-induced cardiotoxicity — Nature Medicine](https://www.nature.com/articles/nm.2919)
- [A coding variant in RARG confers susceptibility — Nature Genetics](https://www.nature.com/articles/ng.3374)
- [Genetics of Anthracycline-Associated Cardiotoxicity — Frontiers in Cardiovascular Medicine](https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2022.867873/full)
- [Novel Mechanism of and Therapeutic Approach for Anthracycline-Induced Cardiotoxicity — Cancer Research Communications](https://aacrjournals.org/cancerrescommun/article/6/6/1261/785472/Novel-Mechanism-of-and-Therapeutic-Approach-for)
- [Efficacy and cardiovascular safety of liposomal doxorubicin — Cardio-Oncology](https://link.springer.com/article/10.1186/s40959-025-00375-w)
- [PROTECT trial (dapagliflozin) rationale and design — Cardio-Oncology](https://pmc.ncbi.nlm.nih.gov/articles/PMC12400668/)
- [MONDO:0022653 — EBI OLS4](https://www.ebi.ac.uk/ols4/api/v2/entities?search=anthracycline%20cardiomyopathy)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 36 |
| Resolved | 36 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 9 |
| Quoted claims found in source | 8 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 36 |
| On topic | 29 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:41084073` *(abstract only)*: "In five trials comparing liposomal doxorubicin (LD) with conventional doxorubicin, LD reduced the risk of clinical heart failure (OR 0.18, 0.08–0.38) and subclinical heart failure (RR 0.31, 0.20–0.48)"
  - closest text in source: "Nine studies compared LD with conventional doxorubicin and three with epirubicin"
