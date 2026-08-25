---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-16T10:01:57.250762'
end_time: '2026-08-16T10:19:52.013428'
duration_seconds: 1074.76
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Stiff Skin Syndrome
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
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-5[1m]
  num_turns: 61
  total_cost_usd: 7.082820000000001
  session_id: 9e98a832-d2e8-40fa-b801-5ec134db1e10
  stop_reason: end_turn
  permission_denials: 5
  denied_tools:
  - Bash
  - Write
  assistant_text_blocks: 1
reference_validation:
  total_references: 47
  verified: 47
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Stiff Skin Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Stiff Skin Syndrome** covering all of the
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

sup Harry — here's the full workup on stiff skin syndrome. Everything below is checked against live sources (PubMed E-utilities, ClinVar, OLS4, HPO API, Orphanet API) rather than recalled; where I couldn't verify something I say so out loud in the **⚠ verification notes** at the end. Quotes marked as verbatim came off the actual cached abstract text, not a summarizer.

---

# Stiff Skin Syndrome — Disease Characteristics Research Report

**Prepared:** 2026-08-16 · **Target:** `Stiff_Skin_Syndrome` · **Category:** Mendelian

---

## 0. The one-paragraph version

Stiff skin syndrome (SSS) is what happens when the scaffolding protein your skin's connective tissue hangs on loses its handshake with the cells living in it. Fibrillin-1 normally forms long polymer cables (microfibrils) that do two jobs at once: they're the rebar that elastic fibers get built around, *and* they're a leash that holds the growth factor TGF-β in a latent, inactive state. One tiny stretch of fibrillin-1 — a three-amino-acid RGD motif sitting in its fourth TB domain — is the grip cells use to hold onto that rebar via surface receptors called integrins. Break that grip with a missense change and you get: cells that can't feel their own matrix, matrix that piles up in disorganized excess, elastic fibers that never assemble properly, and a TGF-β leash that goes slack. The result is skin that literally goes rock-hard from birth or early childhood, welding itself to the tissue underneath and freezing the big joints in flexion — **without** the inflammation, autoantibodies, Raynaud phenomenon, or visceral involvement of ordinary scleroderma. It's fibrosis with the immune system taken out of the equation, which is exactly why it became such a valuable window into systemic sclerosis.

---

## 1. Disease Information

### 1.1 Overview

SSS is a rare, non-inflammatory, slowly progressive fibrosing disorder of skin and subcutis. The Orphanet definition (ORPHA:2833, record dated 2026-07-02, retrieved via the Orphanet API) reads verbatim:

> "Stiff skin syndrome is a rare, slowly progressive cutaneous disease characterized by rock-hard skin bound firmly to the underlying tissues (mainly on the shoulders, lower back, buttocks and thighs), mild hypertrichosis and hyperpigmentation overlying the affected areas of skin, as well as limited joint mobility (mainly of large joints) with flexion contractures. Cutaneous nodules, affecting mostly distal interphalangeal joints, as well as extracutaneous manifestations, including diffuse entrapment neuropathy, scoliosis, a tiptoe gait and a narrow thorax, may be associated. Restrictive pulmonary changes, muscle weakness, short stature and growth delay have also been reported. **No vascular hyperreactivity, immunologic abnormalities nor visceral, muscular or bone involvement has been described.**"

That last sentence is the diagnostic hinge — it's the negative space that separates SSS from systemic sclerosis.

The MONDO/GARD description (MONDO:0008492, via OLS4 and the HPO API) adds lipodystrophy, scoliosis, muscle weakness, slow growth, short stature, and eye-muscle weakness/paralysis to the picture.

First described by Esterly & McKusick in 1971 (**PMID:5100776**, *Pediatrics* 47(2):360-9, "Stiff skin syndrome"; companion piece **PMID:5173296**, *Birth Defects Orig Artic Ser*). The molecular cause sat unknown for 39 years until Loeys et al. 2010.

### 1.2 Key identifiers (all verified live)

| Resource | ID |
|---|---|
| **MONDO** | `MONDO:0008492` (label: *stiff skin syndrome*) — **use this as `disease_term`** |
| **OMIM** | `OMIM:184900` (phenotype) |
| **Orphanet** | `ORPHA:2833` (typology: Disease; classification level: Disorder; preferential parent ORPHA:89826 *Rare skin disease*) |
| **MeSH** | `MESH:C566112` |
| **NCIT** | `NCIT:C118636` |
| **UMLS** | `UMLS:C1861456` |
| **MedGen** | `MedGen:348877` |
| **SNOMED CT** | `765187004` |
| **DOID** | `DOID:0111561` |
| **GARD** | `GARD:0005025` |
| **ICD-11 (foundation)** | `642409035` |
| **Causal gene** | FBN1 — `hgnc:3603`, `NCBIGene:2200`, `OMIM:134797`, UniProt P35555, locus 15q21.1 |

Two animal-side MONDO terms also exist and are worth knowing about so you don't cross-wire them: `MONDO:1010789` *stiff skin syndrome, dog* and `MONDO:1010147` *stiff skin syndrome, non-human animal*.

### 1.3 Synonyms

- **SSKS** (the MONDO exact synonym, and the label ClinVar uses)
- **Congenital scleroderma** — the framing Loeys et al. used in their title
- **Congenital fascial dystrophy** — used interchangeably in the clinical literature (see **PMID:24630430**, *Actas Dermosifiliogr* 2014, titled "Congenital fascial dystrophy or stiff skin syndrome: a case report")
- **Stiff-skin syndrome** (hyphenated variant, e.g. **PMID:26471116**)

Recognized clinical variants (see §1.4): **widespread/classic SSS**, **generalized segmental SSS**, **localized (segmental) SSS**.

### 1.4 Classification — two competing schemes, both from real cohorts

This matters for the KB because it determines whether you model subtypes.

**Two-way split (Myers et al. 2016, PMID:26944597, 52 cases):** segmental vs widespread. Verbatim: *"Of 52 total cases, 18 (35%) were segmentally distributed and 34 (65%) were widespread."* Conclusion verbatim: *"We propose a distinct clinical entity, segmental SSS, characterized by a segmental distribution, later age of onset, and less severe functional limitation. Both segmental SSS and widespread SSS share common diagnostic histopathologic features."*

**Three-way split (Zhao et al. 2024, PMID:38844593, 83 cases):** classic widespread / generalized segmental / localized. Verbatim: *"Among the 83 patients, 27.7, 41, and 31.3% had classic widespread, generalized segmental, and localized SSS, respectively. Joint immobility was present in 100, 71, and 20% of classic, generalized, and localized cases, respectively."*

The three-way scheme is the more recent one and carries prognostic weight (see §8.2). My recommendation for the KB: model these as `has_subtypes` with short names `Classic`, `Generalized segmental`, `Localized`, and note the older two-way scheme in the description.

### 1.5 Information provenance

Everything here is **aggregate disease-level literature** — case reports, retrospective case series, and one molecular-genetics landmark. There is **no EHR-derived or registry-derived dataset** for SSS that I could find, no natural-history study, and no clinical trial (see §12.5). The largest evidence pools are:

| Source | n | PMID |
|---|---|---|
| Zhang 2025 (16 own + 138 literature, pediatric) | 154 | 40551142 |
| Issa Jules 2026 systematic review (27 articles) | 204 | 42165429 |
| Zhao 2024 (24 own + 59 literature) | 83 | 38844593 |
| Myers 2016 (4 own + 48 literature) | 52 | 26944597 |
| Wen 2023 single-department series | 31 | 37594328 |
| Sanchez-Espino 2024 (Toronto, imaging-focused) | 11 | 37864376 |
| Loeys 2010 (molecularly confirmed, HPO source) | 8 | 20375004 |

Note the heavy overlap — these series re-review each other's published cases, so total *distinct* reported patients worldwide is on the order of 200–300, not the sum of the column.

---

## 2. Etiology

### 2.1 Primary cause — genetic, and beautifully specific

Widespread/classic SSS is caused by heterozygous missense mutations in **FBN1**, and not just anywhere in FBN1 — they cluster in the **single domain that carries an RGD integrin-binding motif**, the fourth TGF-β-binding-protein-like domain (TB4).

**Landmark: Loeys BL et al., *Sci Transl Med* 2010;2(23):23ra20 — PMID:20375004.** Verbatim from the abstract:

> "We report that stiff skin syndrome (SSS), an autosomal dominant congenital form of scleroderma, is caused by mutations in the sole Arg-Gly-Asp sequence-encoding domain of fibrillin-1 that mediates integrin binding."

> "Ordered polymers of fibrillin-1 (termed microfibrils) initiate elastic fiber assembly and bind to and regulate the activation of the profibrotic cytokine transforming growth factor-beta (TGFbeta). Altered cell-matrix interactions in SSS accompany excessive microfibrillar deposition, impaired elastogenesis, and increased TGFbeta concentration and signaling in the dermis."

**Confirmation and penetrance (Gerber EE et al., *Nature* 2013;503:126-30 — PMID:24107997).** Verbatim:

> "we studied stiff skin syndrome (SSS), a rare but tractable Mendelian disorder leading to childhood onset of diffuse skin fibrosis with autosomal dominant inheritance and complete penetrance."

> "SSS mutations all localize to the only domain in fibrillin-1 that harbours an Arg-Gly-Asp (RGD) motif needed to mediate cell-matrix interactions by binding to cell-surface integrins."

**Domain assignment restated independently (Del Cid JS et al., *J Biol Chem* 2019 — PMID:31640988).** Verbatim: *"Fibrillin-1 is a modular glycoprotein that includes 7 latent transforming growth factor β (TGFβ)-binding protein-like (TB) domains and mediates cell adhesion through integrin binding to the RGD motif in its 4th TB domain. A subset of missense mutations within TB4 cause stiff skin syndrome (SSS), a rare autosomal dominant form of scleroderma."*

### 2.2 The segmental problem — a genuine open question

Here's the interesting wrinkle, and it's the single biggest knowledge gap in this disease. **Segmental SSS is, in most reported cases, FBN1-negative.** Its molecular basis is unknown.

**PMID:32698527** (Fusco C et al., *Int J Mol Sci* 2020) states it verbatim: *"SSS is distinct in a widespread form, caused by recurrent germline variants of FBN1 encoding a key molecule of the TGF-β signaling, and a segmental form with unknown molecular basis."*

Because segmental SSS is unilateral/blaschkoid in distribution, the natural hypothesis is **post-zygotic somatic mosaicism** — a mutation arising in a patch of embryonic ectoderm/mesoderm rather than in the germline. I want to be explicit: **I found no publication that demonstrates mosaicism in segmental SSS.** It is a reasonable inference from the distribution, not an established fact, and it should be curated as a `KNOWLEDGE_GAP` discussion rather than as mechanism.

One single-case genetic finding exists: **PMID:32212274** (Rangu S et al., *Clin Exp Dermatol* 2020) titled *"Segmental stiff skin syndrome: a novel case with an interleukin-17C mutation successfully treated with secukinumab."* ⚠ This record is **abstract-free in PubMed** (title/metadata only), so no quotable snippet exists from the abstract. Treat the IL17C association as a single unreplicated observation, not an established second locus. It is nonetheless the stated rationale for anti-IL-17 therapy in segmental disease.

### 2.3 Risk factors

**Genetic:**
- Causal: heterozygous FBN1 TB4 missense (see §4). Autosomal dominant, **complete penetrance** (PMID:24107997).
- Susceptibility loci: none known. No GWAS exists for SSS (n far too small).
- Modifier genes: none identified. Variable expressivity is documented but unexplained (see §9.3).

**Environmental / demographic:**
- **None established.** No toxin, drug, infection, occupational exposure, diet, or lifestyle factor has been implicated. This is a clean Mendelian disorder.
- Age: onset is congenital-to-early-childhood and essentially deterministic given genotype, not a "risk factor" in the epidemiological sense.
- Sex: no established predominance (see §9.4).
- Family history: relevant for inherited cases; multigenerational families are documented (PMID:26471116 — a two-generation non-consanguineous Northern Irish family with three affected members; PMID:37115944 — father and son).

### 2.4 Protective factors

None known, genetic or environmental. There is one *adjacent* protective-variant finding worth logging as a cross-reference: in **Leri's pleonosteosis** (a differential diagnosis, §10.4), Banka et al. found that in a systemic sclerosis cohort *"the minor allele of a missense SDC2 variant, p.Ser71Thr, could confer protection against disease (p<1×10(-5))"* (**PMID:24442880**). That's a systemic-sclerosis protective allele, **not** an SSS one — don't cross-wire it.

### 2.5 Gene–environment interactions

None described. The mouse work argues the phenotype is cell-autonomous to the matrix defect and does not require an environmental second hit: PMID:24107997 concludes verbatim *"These results show that alterations in cell-matrix interactions are sufficient to initiate and sustain inflammatory and pro-fibrotic programmes."* The word doing the work there is **sufficient**.

---

## 3. Phenotypes

### 3.1 The curated HPO annotation set (source: HPO API, disease OMIM:184900)

All frequencies below trace to **PMID:20375004** (the 8 molecularly-confirmed Loeys patients) and are the official HPOA annotations. These are directly usable as `phenotypes` entries with `frequency` backed by an n/N count.

| HP ID | Label | Frequency (n/N) | Category |
|---|---|---|---|
| `HP:0030053` | **Stiff skin** | 8/8 | Skin |
| `HP:0002987` | **Elbow flexion contracture** | 8/8 | Connective tissue |
| `HP:0012385` | **Camptodactyly** | 8/8 | Connective tissue |
| `HP:0003577` | **Congenital onset** | 8/8 | Clinical course |
| `HP:0006380` | Knee flexion contracture | 7/8 | Connective tissue |
| `HP:0006467` | Limited shoulder movement | 7/8 | Other |
| `HP:0000545` | Myopia | 6/8 | Eye |
| `HP:0002020` | Gastroesophageal reflux | 4/8 | Digestive |
| `HP:0000518` | Cataract | 2/8 (onset `HP:0003596`) | Eye |
| `HP:0009830` | Peripheral neuropathy | 2/8 | Nervous system |
| `HP:0001647` | Bicuspid aortic valve | 1/8 | Cardiovascular |
| `HP:0009125` | Lipodystrophy | Occasional | Connective tissue |
| `HP:0004322` | Short stature | Occasional | Growth |
| `HP:0001324` | Muscle weakness | Occasional | Musculature |
| `HP:0000006` | Autosomal dominant inheritance | — | Inheritance |

Mapping to dismech `FrequencyEnum`: 8/8 → `VERY_FREQUENT` (or `OBLIGATE` for stiff skin, arguably); 7/8 (87.5%) → `VERY_FREQUENT`; 6/8 (75%) → `FREQUENT`; 4/8 (50%) → `FREQUENT`; 2/8 (25%) → `OCCASIONAL`; 1/8 (12.5%) → `OCCASIONAL`. **Careful** — n=8 is a tiny denominator and these are the *molecularly confirmed classic* cases, which skew severe. Per the dismech frequency SOP, cite the count in the evidence explanation and don't let an 8-patient series masquerade as a population frequency.

### 3.2 Cohort-derived frequencies (much larger denominators, different populations)

These come from clinically-diagnosed cohorts that mix segmental and widespread cases, so they run *lower* than the Loeys numbers. Both sets are true; they describe different populations.

**Zhang et al. 2025 (n=154 pediatric; PMID:40551142)** — verbatim:
> "Thigh skin sclerosis (81, 52.6%) was the most common manifestation observed in these patients. Joint restriction was present in 55(35.7%) patients."

**Issa Jules et al. 2026 systematic review (n=204; PMID:42165429)** — verbatim:
> "The segmental form was predominant compared with the widespread form (73.5% versus 26.5%). Major sign was the indurated skin in all patients (100%). Hypertrichosis, hyperpigmentation, subcutaneous signs, and limited temporomandibular joint mobility were considered minor signs, found at respective rates of 10%, 5%, 5%, and 1%."

**Myers et al. 2016 (n=52; PMID:26944597)** — verbatim:
> "Limitation in joint mobility affected 44% of patients with segmental SSS and 97% of patients with widespread SSS."

**Zhao et al. 2024 (n=83; PMID:38844593)** — joint immobility 100% / 71% / 20% across classic / generalized segmental / localized.

### 3.3 Additional phenotypes with suggested HPO terms (verified labels)

| Feature | Suggested HP term | Source |
|---|---|---|
| Thickened skin | `HP:0001072` Thickened skin | Orphanet, all series |
| Hypertrichosis over lesions | `HP:0000998` Hypertrichosis | ORPHA:2833; PMID:42165429 (10%); PMID:37594328 |
| Hyperpigmentation over lesions | `HP:0000953` Hyperpigmentation of the skin | ORPHA:2833; PMID:37594328 |
| Limitation of joint mobility | `HP:0001376` Limitation of joint mobility | ORPHA:2833; PMID:38844593 |
| Joint contracture (generic) | `HP:0034392` Joint contracture | ORPHA:2833 |
| Hip contracture | `HP:0003273` Hip contracture | clinical series |
| Scoliosis | `HP:0002650` Scoliosis | ORPHA:2833 |
| Tip-toe gait | `HP:0030051` Tip-toe gait | ORPHA:2833 |
| Narrow chest | `HP:0000774` Narrow chest | ORPHA:2833 |
| Restrictive ventilatory defect | `HP:0002091` Restrictive ventilatory defect | ORPHA:2833 ("restrictive pulmonary changes") |
| Entrapment neuropathy | `HP:0012181` Entrapment neuropathy | ORPHA:2833 ("diffuse entrapment neuropathy") |
| Reduced subcutaneous adipose tissue | `HP:0003758` Reduced subcutaneous adipose tissue | MONDO/GARD def; mouse model PMID:24107997 |
| Ophthalmoplegia | `HP:0000602` Ophthalmoplegia | **PMID:26471116** — see below |

**Ocular phenotype is a genuinely underappreciated feature.** Chamney et al. (*Eye* 2016, **PMID:26471116**) verbatim:
> "All three patients had ophthalmoplegia of varying degrees. Direct sequencing of the FBN1 gene detected a heterozygous pathogenic mutation (c.4710G>C; p.Trp1570Cys) in all affected patients."
> "This is the first report of ophthalmoplegia in association with SSS."

That's a molecularly-anchored genotype–phenotype observation in a three-member family — good `HUMAN_CLINICAL` evidence, though n=3 and a single family, so the appropriate frequency band is at most `OCCASIONAL` with the caveat stated.

### 3.4 Phenotype characteristics

- **Age of onset:** congenital in classic SSS (`HP:0003577` at 8/8 in the molecular cohort); early childhood otherwise. Median onset across 154 pediatric patients was **2.0 years (IQR 0.5–4.8)** (PMID:40551142). Segmental onset is later: **4.1 years vs 1.6 years** for widespread (PMID:26944597).
- **Severity:** variable, and severity tracks distribution — classic > generalized segmental > localized (PMID:38844593).
- **Progression:** slowly progressive, non-remitting. See §8.
- **Quality-of-life impact:** ⚠ **No formal QoL instrument (EQ-5D, SF-36, PROMIS, CDLQI) has been applied to SSS in any publication I could find.** What is documented is functional: joint contractures limiting mobility, restrictive chest wall mechanics, diagnostic delay, and pain. PMID:36825671 verbatim: *"Segmental stiff skin syndrome is a rare fibrosing scleroderma-like disorder characterized by progressive indurations of the skin leading to joint contractures, decreased mobility, and pain."* PMID:40551142 notes verbatim: *"Patients with joint contractures had longer diagnostic delays compared with those without joint contractures."* That last one is a nice, curatable statement about the cost of delayed diagnosis.

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene

**FBN1**, fibrillin-1. `hgnc:3603` · `NCBIGene:2200` · `OMIM:134797` · UniProt P35555 · 15q21.1 · 65 exons, 56 domains.

The pleiotropy here is remarkable and worth stating explicitly, because it's the thing that makes SSS mechanistically interesting. From Sakai & Keene, *Matrix Biol* 2019 (**PMID:30219651**), verbatim:

> "Most of the more than 3000 mutations known today in FBN1 cause the Marfan syndrome. Marfan mutations can occur in any of the 56 domains that compose fibrillin-1. In contrast, rare mutations in FBN1 that are confined to only certain domains cause several different types of acromelic dysplasia."

> "Many of the phenotypes of acromelic dysplasias are the opposite of those found in Marfan syndrome. Knowledge of the functions and structural organization of fibrillin molecules within microfibrils is required to understand how one protein and one gene can be the basis for multiple genetic disorders."

So: **TB4 → stiff skin syndrome. TB5 → acromelic dysplasias (acromicric, geleophysic, Weill-Marchesani). Everywhere else → Marfan.** One gene, three phenotypic universes, sorted by domain.

### 4.2 Pathogenic variants — verified against ClinVar and OMIM allelic-variant IDs

These four are the canonical SSS alleles. I pulled the ClinVar VCV XML directly and confirmed each carries an OMIM allelic-variant xref in the `134797.005x` block **and** a trait xref to `OMIM:184900` / trait names "STIFF SKIN SYNDROME" and "SSKS".

| cDNA (NM_000138.5) | Protein | ClinVar | OMIM allelic variant | Classification | GRCh38 |
|---|---|---|---|---|---|
| c.4710G>T | p.Trp1570Cys | `VCV000016469` | FBN1 **.0050** | Pathogenic | chr15:48467975 |
| c.4710G>C | p.Trp1570Cys | `VCV000016470` | FBN1 **.0051** | Pathogenic | chr15:48467975 |
| c.4691G>C | p.Cys1564Ser | `VCV000016471` | FBN1 **.0052** | Pathogenic | chr15:48467994 |
| c.4729T>G | p.Cys1577Gly | `VCV000016472` | FBN1 **.0053** | Pathogenic (criteria provided, single submitter) | — |

Note the elegance of the first two rows: **two different nucleotide changes at the same codon producing the same p.Trp1570Cys substitution**, in independent families. That's convergent evidence that the *residue*, not the nucleotide, is what matters — a nice recurrent-hotspot argument.

- **Variant type/class:** all **missense**. No truncating, frameshift, splice-site, or structural variants have been reported as causing SSS — and mechanistically they *shouldn't*, because the disease requires a mutant protein that still gets built into microfibrils (§4.4).
- **Somatic vs germline:** germline for classic SSS. Segmental SSS is hypothesized (**not demonstrated**) to be post-zygotic somatic.
- **Allele frequency:** I queried gnomAD v4 by the GRCh38 coordinates above and both returned *"Variant not found"* — i.e. **absent from gnomAD**, consistent with private/family-specific pathogenic alleles.
- **De novo vs inherited:** both occur. Multigenerational transmission is documented (PMID:26471116, PMID:37115944).

**Notable non-SSS TB4 variant, useful for a differential-diagnosis note:** Wilson et al. (*Am J Med Genet A* 2013, **PMID:23794388**) report *"a variant in an evolutionarily conserved residue that stabilizes the integrin binding fragment of FBN1, associated with juvenile idiopathic arthritis, mitral valve prolapse or apparently normal phenotype in different family members."* So not every TB4-region change gives SSS — the RGD-proximal geometry is what counts.

**Adjacent-domain phenocopy:** Wang et al. 2020 (**PMID:32406602**) report *"acromicric dysplasia with stiff skin syndrome-like severe cutaneous presentation"* from FBN1 c.5243G>A (p.Cys1748Tyr), exon 42 — outside TB4. Verbatim conclusion: *"This is a report about acromicric dysplasia with stiff skin syndrome-like severe cutaneous presentation caused by a single hotspot mutation, further revealing the gene pleiotropy of FBN1."* Note this variant is **not in ClinVar** under that protein change (I checked — zero hits), so it's a single-report allele.

### 4.3 Functional consequence — selective, not global, loss of integrin binding

This is the most mechanistically precise piece of the whole story. Del Cid et al. 2019 (**PMID:31640988**) tested every RGD-binding integrin against wild-type and mutant fibrillin-1. Verbatim:

> "Our data show that 7 of the 8 RGD-binding integrins can mediate adhesion to fibrillin-1. A single amino acid substitution responsible for SSS (W1570C) markedly inhibited adhesion mediated by integrins α5β1, αvβ5, and αvβ6, partially inhibited adhesion mediated by αvβ1, and did not inhibit adhesion mediated by α8β1 or αIIbβ3."

> "In the SSS mutant background, the presence of a cysteine residue in place of highly conserved tryptophan 1570 alters the conformation of the region containing the exposed RGD sequence within the same domain to differentially affect fibrillin's interactions with distinct RGD-binding integrins."

So the mutation doesn't blow up the RGD motif — it **warps the loop's presentation**, and different integrins, which read that loop differently, are affected to different degrees. It's a change of handshake, not an amputation of the hand. Critically, **αvβ6 and αvβ5 are the integrins that activate latent TGF-β**, so losing those specifically is a direct line to the TGF-β phenotype.

### 4.4 Dominance mechanism — why SSS is *not* Marfan

Jensen et al. 2015 (**PMID:25979247**) built a GFP-tagged full-length fibrillin-1 secretion/assembly assay and found the crucial asymmetry. Verbatim:

> "We show that substitutions in fibrillin-1 domains TB4 and TB5 that cause SSS and the acromelic dysplasias do not prevent fibrillin-1 from being secreted or assembled into microfibrils, whereas MFS-associated substitutions in these domains result in a loss of recombinant protein in the culture medium and no association with microfibrils."

> "These results suggest fundamental differences in the dominant pathogenic mechanisms underlying MFS, SSS and the acromelic dysplasias, which give rise to TGFβ dysregulation associated with these diseases."

Read that carefully, because it's the whole thing: **in SSS the mutant protein gets made, secreted, and built into the cable.** The cable exists; it just talks to cells wrongly. In Marfan the mutant protein never makes it into the cable at all. Same gene, same domains, opposite failure mode — which is why the phenotypes are near-mirror-images (tall/loose/aneurysmal vs short/stiff/fibrotic).

For dismech: this is a `functional_impact_category` question on `GeneticContext`. Neither plain `LOSS_OF_FUNCTION` nor `GAIN_OF_FUNCTION` fits cleanly. The most defensible call is **`NEOMORPHIC`** or **`DOMINANT_NEGATIVE`** with the Jensen result quoted as the justification — the incorporated mutant subunit poisons the signaling properties of the polymer it joins. I'd lean `DOMINANT_NEGATIVE` and say why in the evidence explanation.

### 4.5 Modifier genes, epigenetics, chromosomal abnormalities

- **Modifier genes:** none identified.
- **Epigenetics:** ⚠ **No DNA-methylation, histone-modification, or chromatin study of SSS exists.** I searched; there is nothing in ENCODE, Roadmap, or the primary literature. This is a real, curatable `KNOWLEDGE_GAP`.
- **Chromosomal abnormalities:** none in SSS. (For contrast, the differential Leri's pleonosteosis *is* a copy-number disorder — 8q22.1 microduplication, PMID:24442880.)

---

## 5. Environmental Information

Short section, because the honest answer is short.

- **Environmental factors:** none established. No CTD entry, no toxicological association, no radiation or pollution link.
- **Lifestyle factors:** none.
- **Infectious agents:** none. Not applicable.

The only environmental-adjacent claim in the literature is a *negative* one: Orphanet explicitly states *"No vascular hyperreactivity, immunologic abnormalities nor visceral, muscular or bone involvement has been described"* — i.e. the environmental/immune triggers that drive acquired scleroderma are conspicuously absent here.

For the dismech `environmental:` block: **leave it empty**, or record a single entry documenting the negative with `supports: NO_EVIDENCE`. Don't manufacture an exposure.

---

## 6. Mechanism / Pathophysiology

### 6.1 The causal chain (proposed pathograph)

Here's the chain as I'd model it, upstream → downstream. Every arrow below has a citable source.

```
[1] FBN1 TB4 missense (W1570C / C1564S / C1577G)          MOLECULAR
      ↓ (mutant protein IS secreted and IS assembled — PMID:25979247)
[2] Conformationally altered RGD loop in fibrillin-1 TB4    MOLECULAR
      ↓
[3] Selective loss of integrin binding (α5β1, αvβ5, αvβ6)   MOLECULAR
      ↓ ────────────────────────┐
[4] Impaired fibroblast          │  [4b] Loss of αvβ6/αvβ5-dependent
    cell–matrix adhesion          │       latent-TGF-β restraint
    CELLULAR                      │       MOLECULAR
      ↓                           ↓
[5] Excessive microfibrillar deposition + impaired elastogenesis   TISSUE
      ↓
[6] Increased TGF-β concentration and signaling in dermis          MOLECULAR
    (↑ nuclear pSmad2, ↑ CTGF)
      ↓
[7] Fibroblast activation: ↑COL1A1, ↑COL3A1, ↑fibronectin-1,
    ↑thrombospondin-1, ↑LTBP, ↑ITGB1; ↓MMP-2 activity            CELLULAR
      ↓
[8] Dense, disorganized collagen accumulation in reticular dermis,
    subcutaneous septa and fascia; adipocyte entrapment           TISSUE
      ↓
[9] Rock-hard skin bound to underlying tissue                     TISSUE
      ↓
[10] Joint flexion contractures, restricted mobility,
     restrictive chest wall, entrapment neuropathy                ORGANISM
```

Plus a **branch that only fires in mice** (see §6.6 — this is important):

```
[3/4] Altered cell–matrix interaction
      ↓ (MOUSE ONLY)
[M1] Dermal infiltration by pDC, Th2/Th17/Th9 cells, plasma cells
      ↓
[M2] Anti-nuclear and anti-topoisomerase I autoantibodies
```

### 6.2 Molecular pathways

- **TGF-β / SMAD signaling** — the central axis. `GO:0007179` transforming growth factor beta receptor signaling pathway; `GO:0060395` SMAD protein signal transduction; `GO:0071559` response to transforming growth factor beta; `GO:0050431` transforming growth factor beta binding. Modifier: `INCREASED` (or `GAIN_OF_FUNCTION` if you want to claim the pathway has escaped normal regulatory restraint — and here you arguably can, since the *restraint mechanism itself* is what's broken; but per the dismech guidance, `INCREASED` is the safer default and the quantitative claim is the one the evidence directly supports).
- **Integrin-mediated signaling** — `GO:0007229` integrin-mediated signaling pathway; `GO:0005178` integrin binding; `GO:0007160` cell-matrix adhesion. Modifier: `DECREASED`.
- **ERK/MAPK and NF-κB** — documented in segmental SSS patient fibroblasts (PMID:32698527, below).
- **Reactome/KEGG:** relevant pathways are "Molecules associated with elastic fibres" (R-HSA-2129379), "Elastic fibre formation" (R-HSA-1566948), "Signaling by TGFB family members" (R-HSA-9006936), and KEGG hsa04350 (TGF-beta signaling) / hsa04510 (Focal adhesion) / hsa04512 (ECM-receptor interaction). ⚠ I did not independently verify those specific Reactome/KEGG accession numbers against the databases — treat as leads, not evidence.

### 6.3 The segmental-SSS fibroblast experiment — the best mechanistic data on the non-FBN1 form

Fusco et al. 2020 (**PMID:32698527**) is the single most useful paper for building the downstream half of the pathograph, because it measured actual signaling in patient cells. Verbatim:

> "Lesional fibroblast studies showed a higher phosphorylation level of extracellular signal-regulated kinase 1/2 (ERK1/2), increased levels of nuclear factor-kB (NFkB), and a nuclear accumulation of phosphorylated Smad2 via Western blot and microscopy analyses."

> "Quantitative PCR expression analysis of genes encoding key extracellular matrix proteins revealed increased levels of COL1A1, COL3A1, AGT, LTBP and ITGB1, while zymography assay reported a reduced metalloproteinase 2 enzymatic activity."

> "In vitro exposure of patient's fibroblasts to losartan led to the partial restoration of normal transforming growth factor β (TGF-β) marker protein levels."

> "Our results for the first time reported that aberrant TGF-β signaling may drive the pathogenesis of segmental SSS and might open the way to novel therapeutic approaches."

Two things worth flagging. First, **↓MMP-2 activity** means this isn't only over-production of matrix — it's also under-clearance. The fibrosis is a bathtub with the tap open *and* the drain plugged. Second, the losartan rescue *in vitro* is the direct mechanistic rationale for the losartan case reports in §12.

Note this is `IN_VITRO` evidence from **one patient's fibroblasts**. Tag it accordingly.

### 6.4 The human tissue-expression study — and its awkward result

Guiducci et al. 2009 (**PMID:19468049**) profiled a single SSS patient's dermis before the gene was known, and got a result that partly *conflicts* with the "TGF-β is up" narrative. Verbatim:

> "Histopathological examination showed flattened dermal papillae, a scarce presence of sub-epidermal microvessels and mild dermal fibrosis, but no inflammatory infiltrates. In the SSS dermis, the expression of IL-1beta, -6 and MCP-1 was low, whereas VEGF was intensively expressed. **No differences were observed for TGF-beta, CTGF and ET-1.** In contrast, col1A2, fibronectin-1 and thrombospondin-1 were overexpressed in the SSS dermis."

> "In our SSS patient, an overexpression of ECM proteins was detected, whereas no inflammatory infiltrates or up-regulation of pro-fibrotic cytokines were found. The data suggest that fibrosis in SSS might be independent from inflammation."

**Do not paper over this.** Guiducci measured TGF-β *transcript* by qPCR and found it unchanged; Loeys measured TGF-β *signaling output* (nuclear pSmad2, CTGF protein) and found it up. Those aren't necessarily contradictory — TGF-β dysregulation in fibrillinopathies is about **bioavailability of the already-made latent pool**, not about transcription. But the honest curation move is to record both, tag Guiducci's TGF-β finding as `PARTIAL` or as a distinct claim, and note the reconciliation in the explanation. This is exactly the kind of thing that makes a `mechanistic_hypotheses` block earn its keep.

The inflammation-independence finding, by contrast, is **strongly replicated**. Wen et al. 2023 (**PMID:37594328**, n=31) verbatim: *"Compared with morphea, SSS showed more prominent proliferation of fibroblasts and completely lacked lymphocyte infiltration."* And: *"Histopathologically, SSS shows proliferation of fibroblasts, sclerosis and an absence of inflammation."*

### 6.5 Protein dysfunction

- **Structure:** fibrillin-1 is a 350 kDa modular glycoprotein — 47 cbEGF domains, 7 TB (TGF-β-binding-protein-like) domains, hybrid domains. TB4 is the only one carrying an RGD. UniProt P35555; AlphaFold model available.
- **Misfolding/aggregation:** ⚠ Not the mechanism here. Unlike Marfan TB4/TB5 substitutions (which cause secretion failure — PMID:25979247), SSS substitutions fold and secrete fine.
- **The W1570C twist:** the substitution introduces an **unpaired cysteine** where a highly conserved tryptophan sat. In a domain already full of structural disulfides, a spare free thiol is a loaded gun — it can form aberrant intermolecular bonds. PMID:31640988 attributes the phenotype to conformational change in the RGD loop rather than to aberrant disulfides specifically, but the free-cysteine motif is a recurring theme in TB-domain disease. (For an analogous mechanism in a different protein, cf. **PMID:39864627** on pathological NOTCH3 thiol reactivity in CADASIL — same structural logic, unrelated disease.)
- **Loss vs gain:** best described as **dominant-negative/neomorphic** — see §4.4.

### 6.6 Immune involvement — and the human/model mismatch you must flag

This is the single most important caveat in the whole entry, and I'd curate it as a `HUMAN_MODEL_MISMATCH` discussion rather than a `KNOWLEDGE_GAP`.

**In the mouse**, the phenotype is emphatically inflammatory. Gerber et al. 2013 (**PMID:24107997**) verbatim:

> "Mutant mice show skin infiltration of pro-inflammatory immune cells including plasmacytoid dendritic cells, T helper cells and plasma cells, and also autoantibody production; these findings are normalized by integrin-modulating therapies or TGF-β antagonism."

**In humans**, the histology is famously *bland*. Guiducci: "no inflammatory infiltrates." Wen (n=31): "completely lacked lymphocyte infiltration." Orphanet: "no ... immunologic abnormalities."

Those two statements do not obviously coexist. Possible reconciliations: the mouse model is homozygous or on a permissive background; human biopsies are taken years into established disease and miss an early inflammatory window; species differences in dermal immune surveillance; or the immune arm genuinely requires something mice have and humans don't. **Nobody has resolved this.** That's a real, publishable-grade open question, and it's precisely what the `HUMAN_MODEL_MISMATCH` kind exists for. Proposed experiments: early-lesion biopsy series with immunophenotyping; single-cell RNA-seq of SSS lesional skin (none exists); serial ANA/anti-Scl-70 in a molecularly confirmed cohort.

### 6.7 Metabolic changes, biochemical abnormalities

- **Metabolic:** none described. No metabolomics study of SSS exists.
- **Biochemical:** no enzyme deficiency, no receptor mutation, no channelopathy. The defect is purely structural-plus-signaling in the ECM. Notably, **routine labs are normal** — that's diagnostically load-bearing (§10).
- One histochemical finding: PMID:32406602 (the acromicric/SSS-overlap case) reports *"Alcian blue staining indicated dermal mucopolysaccharide deposition"* — glycosaminoglycan accumulation alongside the collagen. Worth a `biochemical` entry with the caveat that it's from an overlap phenotype, not classic SSS.

### 6.8 Molecular profiling — what exists and what doesn't

| Modality | Status |
|---|---|
| Transcriptomics | ⚠ **No published RNA-seq or microarray of SSS skin.** Only targeted qPCR panels (PMID:19468049, PMID:32698527). No GEO series that I could identify. |
| Proteomics | ⚠ **None.** |
| Metabolomics | ⚠ **None.** |
| Lipidomics | ⚠ **None.** |
| Single-cell | ⚠ **None.** No Human Cell Atlas or Single Cell Portal dataset. |
| Spatial transcriptomics | ⚠ **None.** |
| Multi-omics | ⚠ **None.** |
| CRISPR/RNAi screens | ⚠ **None specific to SSS.** |
| Ultrastructure (EM) | Yes — Loeys 2010 reports abnormal microfibrillar architecture and patchy elastin. |
| Targeted in vitro assays | Yes — microfibril assembly assay (PMID:25979247), integrin adhesion panel (PMID:31640988), patient fibroblast signaling (PMID:32698527). |

**For the `datasets:` block: I found no SSS-specific accession in GEO, PRIDE, MetaboLights, or ArrayExpress.** Per the dismech dataset SOP, do not go fishing on the gene symbol — searching FBN1 will surface Marfan and aortic-aneurysm datasets, which is exactly the Named-Entity-Confusion-via-dataset-search trap. Better to leave `datasets:` empty and record the absence in `notes:`.

### 6.9 Suggested ontology terms (all labels verified live via OLS4)

**GO — biological process / molecular function / cellular component:**

| CURIE | Verified label | Suggested modifier |
|---|---|---|
| `GO:0007179` | transforming growth factor beta receptor signaling pathway | `INCREASED` |
| `GO:0060395` | SMAD protein signal transduction | `INCREASED` |
| `GO:0071559` | response to transforming growth factor beta | `INCREASED` |
| `GO:0050431` | transforming growth factor beta binding | — |
| `GO:0007229` | integrin-mediated signaling pathway | `DECREASED` |
| `GO:0005178` | integrin binding | `DECREASED` |
| `GO:0007160` | cell-matrix adhesion | `DECREASED` |
| `GO:0030198` | extracellular matrix organization | `ABNORMAL` / `INCREASED` |
| `GO:0085029` | extracellular matrix assembly | `INCREASED` |
| `GO:0048251` | elastic fiber assembly | `DECREASED` |
| `GO:0001527` | microfibril (cellular component) | — |
| `GO:0032964` | collagen biosynthetic process | `INCREASED` |
| `GO:0030199` | collagen fibril organization | `ABNORMAL` |
| `GO:0005201` | extracellular matrix structural constituent | — |

**CL — cell types:**

| CURIE | Verified label | Role |
|---|---|---|
| `CL:0000057` | fibroblast | Primary effector cell |
| `CL:0002620` | skin fibroblast | The specific population — prefer this |
| `CL:0000136` | adipocyte | Entrapped in fibrotic septa (PMID:29505473) |
| `CL:0000784` | plasmacytoid dendritic cell | **Mouse model only** (PMID:24107997) |
| `CL:0000899` | T-helper 17 cell | **Mouse model only** |
| `CL:0000786` | plasma cell | **Mouse model only** |

**UBERON — anatomy:**

| CURIE | Verified label |
|---|---|
| `UBERON:0002097` | skin of body |
| `UBERON:0002067` | dermis |
| `UBERON:0002072` | hypodermis |
| `UBERON:0002190` | subcutaneous adipose tissue |
| `UBERON:0008982` | fascia |
| `UBERON:0000982` | skeletal joint |
| `UBERON:0001085` | skin of trunk |

**CHEBI / NCIT — see §12.6.**

### 6.10 Module conformance opportunities

SSS is a strong candidate conformer for **`fibrotic_response`** — but with an important asterisk. The module's canonical chain runs *tissue injury → inflammation → mesenchymal cell activation → myofibroblast → excessive ECM → organ dysfunction*, and **SSS skips the inflammation node entirely** (that's its whole scientific point). So conformance should be declared at the mesenchymal-activation and excessive-ECM nodes and explicitly *not* at the inflammation node, with the Guiducci and Wen quotes as the justification. That asymmetry is genuinely informative rather than a gap — SSS is the natural experiment showing the fibrotic module can run without its inflammatory trigger.

Also worth checking: `aortopathy_tgfbeta_dysregulation` shares the FBN1/TGF-β logic but its downstream (medial degeneration → aortic dilation) is absent in SSS — one 1/8 bicuspid aortic valve does not an aortopathy make. **Do not** conform SSS to it.

---

## 7. Anatomical Structures Affected

### 7.1 Organ level

**Primary:** skin (`UBERON:0002097`) — specifically dermis (`UBERON:0002067`) and hypodermis/subcutis (`UBERON:0002072`), extending into fascia (`UBERON:0008982`).

**Regional distribution** (verbatim, PMID:37594328): *"Skin lesions of widespread SSS generally showed skin sclerosis concentrating over the lumbar, buttocks, thighs, proximal part of limbs, and shoulders with specific abnormal gait and posture. Skin lesions of segmental SSS generally showed sclerotic plaques involving the thigh, lumbar area and buttocks, associated with hypertrichosis, hyperpigmentation and a cobblestone appearance."*

The **limb girdles** are the signature territory. Sanchez-Espino 2024 (PMID:37864376) verbatim: *"MRI readings showed abnormal high signal intensity of the affected tissue correlating with the anatomical site of involvement in all cases, specifically, in the shoulder/pelvic girdle with limb extension."* And thigh sclerosis is the single most common finding at **52.6%** of 154 pediatric patients (PMID:40551142).

**Secondary organ involvement:**
- **Musculoskeletal** — joints (`UBERON:0000982`) via contracture; spine via scoliosis. This is mechanical, secondary to the cutaneous encasement, not primary joint disease.
- **Respiratory** — restrictive ventilatory defect from a rigid, narrow thorax. Not lung parenchymal disease.
- **Peripheral nervous system** — entrapment neuropathy from compression within fibrotic tissue; documented at 2/8 in the Loeys cohort.
- **Eye** — ophthalmoplegia (PMID:26471116), myopia 6/8, cataract 2/8.
- **Craniofacial** — PMID:42165429 found *"limited temporomandibular joint mobility"* in 1% of 204 patients; facial skin induration occurs.
- **Cardiovascular** — 1/8 bicuspid aortic valve. **No aortopathy.** Do not extrapolate Marfan cardiovascular surveillance to SSS on this basis.
- **GI** — gastroesophageal reflux 4/8. Mechanism unclear; possibly mechanical.

**Explicitly NOT involved** (per Orphanet, and this is diagnostically decisive): visceral organs, vasculature (no Raynaud, no vascular hyperreactivity), bone (primary), and the immune system.

### 7.2 Tissue and cell level

- **Connective tissue** is the target. Specifically the **reticular dermis** and **subcutaneous fibrous septa**.
- Zhao 2024 quantified the depth distribution by subtype, verbatim: *"54.5% of classic and 50% of generalized cases occurred throughout the dermis or the subcutis, whereas 76% of localized cases were mainly involved in the reticular dermis or subcutis."*
- **Cell populations:** dermal/skin fibroblasts (`CL:0002620`) are the effectors — and unusually for a fibrosis, they're described as *proliferating*, not merely activated. PMID:37594328 verbatim: *"SSS showed more prominent proliferation of fibroblasts."*
- **Adipocytes** (`CL:0000136`) get **entrapped** by advancing collagen — PMID:29505473 verbatim: *"biopsy showing adipocyte entrapment which we believe is an unrecognized key pathological finding in diagnosis of this entity."* Separately, subcutaneous fat is *lost* over time in the mouse model.
- **Epidermis** is essentially spared — the only change is flattened dermal papillae (PMID:19468049), i.e. a passive consequence of the dermis below going rigid.

### 7.3 Subcellular level

The action is **extracellular**, which is itself notable. Relevant GO cellular components: `GO:0001527` microfibril; extracellular matrix and extracellular space. There is no reported mitochondrial, lysosomal, nuclear, or ER compartment pathology in SSS. (Contrast: the Marfan-type TB4 mutations *do* cause ER retention — but those aren't SSS.)

### 7.4 Localization and lateralization

- **Classic/widespread SSS:** bilateral, roughly **symmetric**, girdle-predominant.
- **Segmental SSS:** *"largely unilateral, segmental distribution"* (PMID:26944597) — often following a blaschkoid or dermatomal-ish pattern. This asymmetry is the strongest clinical argument for mosaicism.

So lateralization is itself a subtype discriminator, which is a nice thing to encode.

---

## 8. Temporal Development

### 8.1 Onset

- **Pattern:** insidious, chronic. Never acute.
- **Classic SSS:** congenital — `HP:0003577` congenital onset at **8/8** in the molecularly confirmed cohort (PMID:20375004). Case reports of neonatal presentation exist (PMID:22998194 "Stiff skin syndrome in a newborn infant").
- **Overall pediatric cohort:** median onset **2.0 years (IQR 0.5–4.8)**, median age at diagnosis **9.0 years (IQR 5.0–13.0)** (PMID:40551142). That's a **~7-year diagnostic delay** — one of the more actionable numbers in this whole report.
- **By subtype:** segmental 4.1 y vs widespread 1.6 y (PMID:26944597).
- **Systematic review:** *"The age of onset of this syndrome was predominantly early childhood"* (PMID:42165429).
- Adult-onset/adult-diagnosed cases exist but are rare and probably represent late recognition of long-standing disease (PMID:30874234, "Middle-Aged Female Diagnosed With Widespread Stiff Skin Syndrome").

### 8.2 Progression — with actual transition probabilities

This is the most useful prognostic dataset available, from Zhao 2024 (PMID:38844593), verbatim:

> "In patients with incipient localized SSS, 42% (21/50) developed generalized SSS, and only 6% (3/50) progressed to classic SSS, whereas more than half of the incipient generalized SSS cases (60.6%, 20/33) developed classic SSS."

Those are real, curatable transition rates for a `progression` block:

| From | To | Rate |
|---|---|---|
| Localized | Generalized segmental | 42% (21/50) |
| Localized | Classic widespread | 6% (3/50) |
| Generalized segmental | Classic widespread | 60.6% (20/33) |

The paper's conclusion, verbatim: *"We propose a distinct clinical classification characterized by lesion distribution, including classic widespread, generalized segmental, and localized SSS, associated with disease severity and prognosis."*

- **Rate:** slow. Described as "slowly progressive" by Orphanet and consistently in case reports.
- **Course pattern:** **progressive**, not relapsing-remitting, not episodic. Long-term follow-up is documented in PMID:38664099 ("Stiff skin syndrome: long-term follow-up").
- **Duration:** chronic, lifelong.

### 8.3 Patterns

- **Remission:** ⚠ **Spontaneous remission has not been reported.** Treatment-induced remission has not been achieved either — the 2025 series is blunt about this (verbatim): *"these treatments are not capable of reversing established skin lesions."*
- **Critical periods:** the therapeutic logic — such as it is — is that **early intervention before contractures fix** is the only window that matters. The evidence for that is indirect (the diagnostic-delay/contracture correlation in PMID:40551142) rather than interventional. In the mouse, prevention worked and reversal *also* worked with TGF-β blockade, which is at least encouraging about the existence of a window (§15.2).

---

## 9. Inheritance and Population

### 9.1 Epidemiology

- **Prevalence:** ⚠ **No quantitative estimate exists.** I queried the Orphanet API for ORPHA:2833 — the record carries a definition but the prevalence endpoint returned nothing retrievable. The disease is universally described as "rare"/"ultrarare"; PMID:32698527 calls it verbatim *"an ultrarare and untreatable condition."* Practical framing for the KB: use `prevalence_class: UNKNOWN` or `NOT_YET_DOCUMENTED` with `measure_type: CASES_IN_LITERATURE`, and record the case counts below in `notes`.
- **Cumulative reported cases:** the largest systematic review found **204 patients across 27 articles spanning 1970–2025** (PMID:42165429). Accounting for overlap between series, the world literature holds on the order of **200–300 distinct reported cases**.
- **Incidence:** unknown. No population-based estimate.

### 9.2 Inheritance

- **Pattern:** **autosomal dominant** — `HP:0000006`. Verbatim from PMID:24107997: *"a rare but tractable Mendelian disorder leading to childhood onset of diffuse skin fibrosis with autosomal dominant inheritance and complete penetrance."*
- **Penetrance:** **complete** (same quote). Note the mild dissonance with PMID:23794388, which reports an FBN1 integrin-binding-fragment variant giving *"apparently normal phenotype in different family members"* — but that variant causes JIA/MVP, not SSS, so it isn't a counterexample to SSS penetrance.
- **Expressivity:** **variable.** The three-subtype severity spectrum is the clearest evidence.
- **Genetic anticipation:** not applicable (not a repeat-expansion disorder).
- **Germline mosaicism:** not reported. **Somatic** mosaicism is the leading (unproven) hypothesis for segmental disease.
- **Founder effects:** none identified. The recurrence of p.Trp1570Cys is a **mutational hotspot** (two different nucleotide changes at the same codon in unrelated families), not a founder haplotype — an important distinction.
- **Consanguinity:** irrelevant for a dominant disorder. PMID:26471116 specifically describes a *"two generation nonconsanguineous"* family.
- **Carrier frequency:** not applicable (dominant, fully penetrant). Pathogenic alleles are absent from gnomAD.
- **De novo rate:** unquantified; both de novo and inherited cases occur.

### 9.3 Genetic testing yield — a number worth having

Implicit in the literature but rarely stated: **FBN1 testing is high-yield in classic widespread SSS and low-yield in segmental SSS.** Zhang 2025's cohort was 14/16 segmental, and the recommendation is hedged accordingly (verbatim): *"The diagnosis of SSS should involve a thorough investigation of family history, detailed physical examination, comprehensive pathological assessment, genetic testing when applicable, and careful exclusion of other scleroderma-like diseases."* Note "**when applicable**" — that hedge is doing real work.

### 9.4 Population demographics

- **Affected populations:** cases reported worldwide — USA, UK/Northern Ireland, Belgium, Italy, Spain, Chile, Mexico, Brazil, Lebanon, China, Canada, Côte d'Ivoire, Argentina, Australia. **No ethnic predilection identified.** The two largest series happen to be Chinese (Peking Union, n=16 own; Xi'an Jiaotong, n=24 own; Xijing, n=31), which reflects tertiary-referral concentration and publication activity, not a true population skew.
- **Geographic distribution of variants:** none. p.Trp1570Cys has been reported in geographically unrelated families (a hotspot, not a regional allele).
- **Sex ratio:** ⚠ **Not established.** None of the cohort papers I read reported a male:female breakdown in the abstract. Do not assert a ratio.
- **Age distribution:** overwhelmingly pediatric at presentation; the prevalent population is all ages, since the disease is lifelong and not fatal.

---

## 10. Diagnostics

### 10.1 Laboratory tests — the diagnostic value is in the negatives

There is **no diagnostic biomarker** for SSS. What makes labs useful is that they are *normal*, which rules the imitators out:

- **ANA:** negative (positive ANA points to morphea/SSc).
- **Anti-Scl-70 / anti-centromere / anti-RNA-pol III:** negative.
- **Eosinophils:** normal (elevated → eosinophilic fasciitis).
- **Inflammatory markers (ESR/CRP):** normal.
- **Serum/urine paraprotein:** absent (present → scleromyxedema, scleredema of Buschke).
- **Glucose/HbA1c:** normal (abnormal → scleredema diabeticorum).

⚠ I found **no LOINC-coded reference-range study specific to SSS**, and no `reference_ranges` block is warranted — there's no analyte to bound.

### 10.2 Imaging — the most practically useful modern addition

**High-frequency ultrasound and shear-wave elastography** have become the workhorse non-invasive tools. Sanchez-Espino 2024 (PMID:37864376) verbatim:

> "The sclerotic changes were measured clinically and radiologically, by a total of 16 imaging studies: 13 magnetic resonance imaging (MRI) and 3 ultrasound. MRI readings showed abnormal high signal intensity of the affected tissue correlating with the anatomical site of involvement in all cases, specifically, in the shoulder/pelvic girdle with limb extension. Shear wave ultrasound elastography (SWE) demonstrated higher values within the dermis compared to the control site."

> "Skin SWE is a feasible, noninvasive, and objective instrument to evaluate and monitor sclerotic changes overtime, it could be potentially extrapolated to other pediatric skin sclerotic conditions."

The 2026 case report (PMID:42021647) makes the resource-limited-settings argument, verbatim: *"Ultrasound demonstrated dermal thickening and prominent hypodermal fibrous septa, findings that correlated with the characteristic hypoinflammatory lattice arrangement seen on histology. This case highlights the diagnostic value of integrating advanced imaging and pathology to ensure accuracy and avoid treatment delays, particularly in resource-limited settings where genetic testing is unavailable."*

Also: PMID:30704628 (ultrasound morphology with clinical-histological correlation), PMID:32697852 (sonographic features of segmental SSS — verbatim: *"High-frequency ultrasonography can represent a useful clinical adjunct in the differential diagnosis of this condition"*).

### 10.3 Biopsy / histopathology — the diagnostic gold standard

Three findings, in decreasing order of specificity:

1. **The subcutaneous lattice.** McCalmont & Gilliam (**PMID:22211327**), titled: *"A subcutaneous lattice-like array of thick collagen is a clue to the diagnosis of stiff skin syndrome."* ⚠ Abstract-free record — the title is the finding, and per the dismech title-snippet rule, this title *does* state a result rather than a topic, so it's quotable with that noted in the explanation.
2. **Absence of inflammation.** Replicated across PMID:19468049, PMID:37594328 (n=31), PMID:37864376.
3. **Adipocyte entrapment.** PMID:29505473, verbatim: *"biopsy showing adipocyte entrapment which we believe is an unrecognized key pathological finding in diagnosis of this entity."* (Proposed by a single group; treat as a supportive rather than defining feature.)

Plus: thickened dermis with sclerotic, densely packed collagen extending into subcutaneous septa; fibroblast proliferation; normal epidermis with flattened dermal papillae; increased fibrillin-1 and elastin deposition on immunostaining with abnormal microfibrillar ultrastructure on EM.

**Biopsy must be deep** — a punch that stops at mid-dermis will miss the septal/fascial pathology entirely and can be read as normal. That's a genuine clinical pitfall and belongs in the entry.

### 10.4 Differential diagnosis — the "great imitators" problem

PMID:32513403 is literally titled *"Sclerodermalike syndromes: Great imitators."* Distinguishing features:

| Condition | Distinguishing feature |
|---|---|
| **Morphea / localized scleroderma** | Lymphocytic infiltrate present; SSS *"completely lacked lymphocyte infiltration"* (PMID:37594328). Also violaceous border, epidermal atrophy. |
| **Systemic sclerosis** | Raynaud, nailfold capillary abnormalities, ANA/anti-Scl-70, visceral involvement — all absent in SSS. |
| **Scleredema (Buschke / diabeticorum)** | Upper back/neck predominance, mucin deposition, diabetes or post-infectious association. PMID:34411278 addresses exactly this discrimination. |
| **Eosinophilic fasciitis** | Peripheral eosinophilia, "groove sign", post-exertional onset, steroid-responsive. |
| **Nephrogenic systemic fibrosis** | Renal failure + gadolinium exposure history. |
| **Acromicric / geleophysic dysplasia** | Same gene, TB5 domain; short stature, brachydactyly, cone-shaped epiphyses dominate. Can overlap — PMID:32406602. |
| **Weill-Marchesani syndrome** | FBN1 (dominant) or ADAMTS10 (recessive); microspherophakia, ectopia lentis, glaucoma. |
| **Myhre syndrome** | SMAD4; stiff thick skin + short stature + hearing loss + intellectual disability. Another "TGF-β-pathy." |
| **Leri's pleonosteosis** | 8q22.1 microduplication (GDF6, SDC2); *"Scleroderma-like skin thickening can be seen in some individuals with LP"* (PMID:24442880). |
| **Infantile systemic hyalinosis / hyaline fibromatosis** | ANTXR2; gingival hypertrophy, painful nodules (PMID:26207694). |
| **Winchester syndrome** | MMP2; osteolysis. |
| **Congenital fascial dystrophy** | Considered synonymous by many (PMID:24630430). |

PMID:24442880 gives a lovely framing sentence for the whole neighborhood, verbatim: *"We propose that LP is an additional member of the growing 'TGF-β-pathies' group of musculoskeletal disorders, which includes Myhre syndrome, acromicric dysplasia, geleophysic dysplasias, Weill-Marchesani syndromes and stiff skin syndrome."* That's a ready-made `Grouping` rationale if you ever want one.

### 10.5 Genetic testing

- **Recommended approach:** targeted **FBN1** sequencing (single-gene) is the highest-yield first test in classic widespread SSS with a compatible phenotype. Focus on **exons encoding TB4** (the c.4691–c.4729 region, exons 37–38).
- **Gene panels:** connective-tissue-disorder / aortopathy panels all contain FBN1 and will work, but return many Marfan-oriented VUS.
- **WES/WGS:** appropriate when the phenotype is atypical or the FBN1 test is negative — this is how PMID:32406602 (WGS + Sanger) and PMID:27188772 (canine WGS) were solved.
- **CMA / karyotype / FISH / mtDNA / repeat-expansion testing:** **not indicated.** No copy-number or cytogenetic mechanism in SSS. (CMA *is* the right test if Leri's pleonosteosis is on the differential.)
- **Yield caveat:** in segmental SSS, expect a negative result. PMID:32698527 verbatim: *"a segmental form with unknown molecular basis."* Genetic testing being unavailable is also a real-world constraint (PMID:42021647).
- **ACMG classification:** the four canonical alleles are ClinVar Pathogenic; three carry "no assertion criteria provided" (legacy OMIM submissions), one has "criteria provided, single submitter."

### 10.6 Omics-based diagnostics

None available or in development. See §6.8.

### 10.7 Clinical criteria

⚠ **There are no formally validated diagnostic criteria** — no society guideline, no consensus statement, no ICD-linked criteria set. Diagnosis is a gestalt of: compatible clinical picture (rock-hard girdle skin ± hypertrichosis/hyperpigmentation, joint limitation) + supportive histopathology (thick lattice collagen, no inflammation) + supportive imaging (US/MRI) + exclusion of imitators + FBN1 confirmation where available.

The closest thing to a criteria statement is the 2026 systematic review's conclusion, verbatim: *"Stiff skin syndrome should be considered systematically in any patient presenting with facial skin induration and should be investigated thoroughly, excluding any visceral or biological abnormalities."*

For the dismech `definitions:` block, this would be a `derivation_basis: ESTABLISHED_CRITERIA`? **No** — I'd argue it isn't established. There is no consensus criteria set. If you write a definition, it should be honest about that.

### 10.8 Screening

- **Newborn screening:** not performed, not proposed. Would fail every Wilson-Jungner criterion (no treatment that changes outcome).
- **Carrier screening:** not applicable (dominant).
- **Cascade screening:** reasonable in a family with a known FBN1 TB4 variant — but note the disease is fully penetrant and clinically obvious, so cascade *testing* mostly serves reproductive planning rather than presymptomatic detection.

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality

- **Life expectancy:** not established to be reduced. SSS is **not** a fatal disease in the way systemic sclerosis is — no pulmonary arterial hypertension, no renal crisis, no interstitial lung disease, no cardiac involvement.
- **Survival rate / mortality rate / disease-specific mortality:** ⚠ **No published figures.** No registry, no cohort with mortality follow-up.
- **Theoretical risk:** severe restrictive chest-wall disease could compromise respiratory function in the most severe classic cases, and anesthetic management is genuinely hazardous (PMID:32761718, "Anesthetic implications of a pediatric patient with stiff skin syndrome" — rigid skin complicates airway access, IV access, and positioning). But no mortality series exists.

### 11.2 Morbidity and function

Morbidity, not mortality, is the whole story:

- **Joint contractures** — the dominant disability. 100% in classic, 71% generalized, 20% localized (PMID:38844593).
- **Restricted mobility and pain** (PMID:36825671).
- **Restrictive pulmonary changes** (Orphanet).
- **Entrapment neuropathy** (Orphanet; 2/8 in Loeys cohort).
- **Chronic exertional compartment syndrome** — an unusual but instructive complication. PMID:37115944: *"Chronic Exertional Compartment Syndrome Requiring Bilateral Fasciotomy: An Atypical Complication of Familial Stiff Skin Syndrome in a Father and Son."* When the fascia itself becomes an inelastic casing, muscle has nowhere to expand.
- **Growth impairment and short stature** (Orphanet, MONDO).
- **Diagnostic delay** — ~7 years median (PMID:40551142), and *"Patients with joint contractures had longer diagnostic delays."*
- **Disability outcomes:** ⚠ no ICF-coded or formal disability data.
- **QoL measures:** ⚠ none applied. See §3.4.

### 11.3 Disease course and recovery

- **Complications:** contractures, compartment syndrome, restrictive lung physiology, neuropathy, anesthetic risk, psychosocial impact of visible disfigurement.
- **Recovery potential:** essentially nil for established lesions. The 2025 series states it flatly (verbatim): *"these treatments are not capable of reversing established skin lesions."*

### 11.4 Prognostic factors

The one genuinely validated prognostic factor is **lesion distribution at presentation** (PMID:38844593) — localized carries the best prognosis, with only 6% progressing to classic disease, while generalized segmental progresses to classic in 60.6%. That's the number to put in a `progression` block.

Secondary prognostic considerations: earlier onset associates with widespread disease (1.6 y vs 4.1 y, PMID:26944597); joint involvement at diagnosis predicts functional impairment.

**Prognostic biomarkers:** ⚠ none. SWE elastography is a promising *monitoring* tool (PMID:37864376) but has not been shown to predict outcome.

---

## 12. Treatment

### 12.1 The honest headline

**There is no disease-modifying therapy for stiff skin syndrome.** PMID:32698527 calls it verbatim *"an ultrarare and untreatable condition."* Every systemic agent below rests on case reports and small series — zero randomized trials, zero controlled comparisons.

The 2025 case series states the position most carefully (verbatim, PMID:40551142):

> "Currently, there is limited evidence supporting the use of systemic treatment options targeting the transforming growth factor-β or interleukin-17 pathways (such as MMF, losartan, and secukinumab) to slow disease progression. However, these treatments are not capable of reversing established skin lesions, and further investigations are imperative to assess their therapeutic efficacy in SSS."

And on what patients actually receive (verbatim): *"Patients were primarily treated with physical therapy, while some patients received medications such as mycophenolate mofetil (MMF), losartan, and secukinumab. However, the prognosis varied."*

### 12.2 Physical therapy — the actual mainstay

Physiotherapy and stretching to preserve range of motion and delay contracture is the **only intervention with consistent support across every series**. It is supportive, not disease-modifying, and its evidence base is "everyone does it and it seems to help," which is to say uncontrolled.

Combined-modality report: PMID:27846975, *"Segmental stiff skin syndrome (SSS): Two additional cases with a positive response to mycophenolate mofetil and physical therapy."* ⚠ Abstract-free record; the title states the result.

### 12.3 Pharmacotherapy — three anecdotal options, three different rationales

**Mycophenolate mofetil (MMF)** — antimetabolite, IMPDH inhibitor, broadly antifibrotic/antiproliferative. Reported with "positive response" in two segmental cases (PMID:27846975) and used in the Zhang cohort.

**Losartan** — angiotensin II type 1 receptor blocker, which reduces TGF-β signaling. This is the **mechanistically best-motivated** oral agent, borrowed straight from Marfan aortopathy. Case report: PMID:29110325 ("A case of segmental stiff skin syndrome treated with systemic losartan"). And critically, there's supporting in-vitro data in the *right* cells: PMID:32698527 verbatim: *"In vitro exposure of patient's fibroblasts to losartan led to the partial restoration of normal transforming growth factor β (TGF-β) marker protein levels."* Note **"partial."**

**Secukinumab** — anti-IL-17A monoclonal antibody. Two independent segmental-SSS reports: PMID:32212274 (the IL17C-variant case) and PMID:36825671, the latter verbatim: *"Treatment options are limited; we report a patient that showed improvement with anti-IL17 biologic therapy."*

⚠ **A caution worth curating:** the secukinumab rationale is IL-17**A** blockade, while the reported variant was in IL-17**C**. Those are different cytokines with different receptors (IL-17C signals through IL-17RE). The mechanistic link between the reported variant and the drug that worked is **not established** — it's a plausible-sounding leap. Flag it rather than repeating it as mechanism.

Other reported/attempted agents (generally with poor or absent response): systemic and intralesional corticosteroids, methotrexate, D-penicillamine, phototherapy/PUVA, cyclosporine. One outlier case: PMID:23910622, "Stiff skin syndrome and myeloma treated with autologous stem cell transplantation" — a coincidental-comorbidity report, not an SSS therapy.

### 12.4 Advanced therapeutics — all preclinical

**This is where SSS gets genuinely exciting**, and it's the part most likely to matter for a mechanism KB. Gerber et al. 2013 (**PMID:24107997**) showed in knock-in mice:

> "Here we show that mouse lines harbouring analogous amino acid substitutions in fibrillin-1 recapitulate aggressive skin fibrosis that is prevented by integrin-modulating therapies and reversed by antagonism of the pro-fibrotic cytokine transforming growth factor β (TGF-β)."

> "Mutant mice show skin infiltration of pro-inflammatory immune cells including plasmacytoid dendritic cells, T helper cells and plasma cells, and also autoantibody production; these findings are normalized by integrin-modulating therapies or TGF-β antagonism."

Note the two verbs: integrin modulation **prevented**; TGF-β blockade **reversed**. If that reversal translates, it's the only lead pointing at established-lesion regression. **None of this has entered human trials.** No gene therapy, no ASO, no siRNA, no cell therapy, no gene editing exists or is in development for SSS.

### 12.5 Clinical trials

⚠ **I searched ClinicalTrials.gov via the v2 API for "stiff skin syndrome" and got zero studies.** There is no interventional or observational trial for this disease. The `clinical_trials:` block should be **empty**. (The only hit on a loose condition search was NCT05687474, "Baby Detect: Genomic Newborn Screening," which lists hundreds of conditions and is not an SSS study — do not curate it.)

### 12.6 Surgical, supportive, rehabilitative

- **Surgery:** limited and reactive. **Fasciotomy** for compartment syndrome (PMID:37115944). Contracture release has been attempted but recurrence from ongoing fibrosis is the expected problem. Oral/maxillofacial procedures for TMJ restriction (PMID:42165429).
- **Anesthesia:** requires specific planning — see PMID:32761718.
- **Rehabilitation:** PT/OT, stretching, splinting, mobility aids.
- **Supportive:** pain management, respiratory monitoring in severe thoracic involvement, psychosocial support.

### 12.7 Suggested NCIT / CHEBI annotations (all verified live via OLS4)

| Treatment | `treatment_term` | `therapeutic_agent` | `therapeutic_modality` |
|---|---|---|---|
| Physical therapy | `NCIT:C15302` Physical Therapy | — | `BEHAVIORAL` |
| Occupational therapy | `NCIT:C121351` Occupational Therapy | — | `BEHAVIORAL` |
| Rehabilitation | `NCIT:C15315` Rehabilitation | — | `BEHAVIORAL` |
| Mycophenolate mofetil | `NCIT:C15986` Pharmacotherapy | `CHEBI:8764` mycophenolate mofetil *(or `NCIT:C1468`)* | `SMALL_MOLECULE` |
| Losartan | `NCIT:C15986` Pharmacotherapy | `CHEBI:6541` losartan *(or `NCIT:C66869`)* | `SMALL_MOLECULE` |
| Secukinumab | `NCIT:C15986` Pharmacotherapy | `NCIT:C152315` Secukinumab | `MONOCLONAL_ANTIBODY` |
| Methotrexate | `NCIT:C15986` Pharmacotherapy | `CHEBI:44185` methotrexate | `SMALL_MOLECULE` |
| Fasciotomy / surgery | `NCIT:C15329` Surgical Procedure | — | `SURGERY` |
| Genetic counseling | `NCIT:C15240` Genetic Counseling | — | `BEHAVIORAL` |

Per the KB's memory note about NCIT drug terms failing `therapeutic_agent` validation, **prefer the CHEBI IDs** where they exist. Secukinumab has no CHEBI term, so NCIT is the only option there.

**`target_mechanisms` suggestions** (for the pathograph links):
- Losartan → `INHIBITS` the "Increased TGF-β signaling" node (supported by PMID:32698527's in-vitro partial rescue).
- Secukinumab → the IL-17 axis — but **only if you model an IL-17 node**, and I'd argue you shouldn't, because the human evidence is one case. Better to record the treatment without a mechanism link than to invent a node to hang it on.
- MMF → fibroblast proliferation node.

### 12.8 Pharmacogenomics, treatment algorithms, personalized medicine

- **Pharmacogenomics:** ⚠ none for SSS. (Generic MMF/IMPDH and losartan/CYP2C9 PGx exists in PharmGKB but is disease-agnostic.)
- **Treatment algorithm:** none published. In practice: confirm diagnosis → PT/OT immediately → consider losartan or MMF in progressive disease → consider anti-IL-17 in segmental disease → surgical intervention only for complications.
- **Combination therapy:** PT + MMF is the only combination with a published report (PMID:27846975).
- **Genotype-guided treatment:** ⚠ **does not exist.** No genotype–treatment-response data.

---

## 13. Prevention

- **Primary prevention:** **not possible.** A dominant, fully penetrant, congenital-onset genetic disorder with no environmental component has no primary prevention. Do not manufacture one.
- **Secondary prevention (early detection):** the actionable target is the **~7-year diagnostic delay** (PMID:40551142). Earlier recognition → earlier PT → potentially fewer fixed contractures. That inference is reasonable but *unproven* — the delay/contracture correlation in that paper is associational, and reverse causation (more severe disease presents earlier) is not excluded. Curate carefully.
- **Tertiary prevention:** contracture prevention via sustained PT/stretching/splinting; respiratory monitoring; pre-operative anesthetic planning (PMID:32761718). This is where essentially all realistic prevention effort sits.
- **Immunization:** not applicable.
- **Screening programs:** none; not warranted (see §10.8).
- **Genetic screening:** prenatal diagnosis and preimplantation genetic testing are technically available for families with a known FBN1 variant. ⚠ I found no publication reporting either being performed for SSS.
- **Risk stratification:** the Zhao subtype classification (§8.2) is the only validated stratifier, and it stratifies *progression*, not risk of onset.
- **Behavioral interventions:** none reduce risk of disease. Maintaining range of motion reduces *disability*.
- **Genetic counseling** (`NCIT:C15240`): 50% recurrence risk per pregnancy for an affected parent; complete penetrance means an inheriting child *will* be affected; severity is not predictable from genotype. Counseling for segmental disease is genuinely harder — if it's post-zygotic somatic, recurrence risk is likely low but germline mosaicism cannot be formally excluded, and **there is no data to quote**. Say so.
- **Public health / environmental interventions:** not applicable.

---

## 14. Other Species / Natural Disease

There are two distinct canine conditions here, and they are **not the same disease** — mixing them up is the obvious trap.

### 14.1 West Highland white terrier "stiff skin-like syndrome"

Doelle et al., *Vet Dermatol* 2016 (**PMID:27188772**). Verbatim:

> "Affected dogs exhibited markedly indurated skin that was attached firmly to the underlying tissue and incomplete closure of the mouth and eyes."

> "Histologically, the dermis and pannicular septa were thickened by a marked increase in coarse collagen fibres and a mild to moderate increase in collagen fibre diameter. The syndrome most likely follows an autosomal recessive mode of inheritance. **The sequence analysis did not reveal any obvious causative variant in the investigated candidate genes ADAMTSL2 and FBN1.**"

> "Unlike in humans, or previously described beagles with stiff skin, there was no restriction of joint mobility. Genetic analysis did not detect a candidate causative variant and warrants further research."

So: **phenotypic mimic, different inheritance (recessive), unknown gene, no joint restriction.** It is *not* a model of human SSS in any mechanistic sense — it's a phenocopy. Curate it as such or not at all.

- Species: dog, `NCBITaxon:9615`
- Breed: West Highland White Terrier — ⚠ I did not verify a VBO identifier; look it up before curating.
- Related MONDO: `MONDO:1010789` *stiff skin syndrome, dog*

### 14.2 Musladin-Lueke Syndrome (MLS) in Beagles — ADAMTSL2

Bader et al., *PLoS One* 2010 (**PMID:20862248**). Verbatim:

> "Musladin-Lueke Syndrome (MLS) is a hereditary disorder affecting Beagle dogs that manifests with extensive fibrosis of the skin and joints. In this respect, it resembles human stiff skin syndrome and the Tight skin mouse, each of which is caused by gene defects affecting fibrillin-1, a major component of tissue microfibrils."

> "Sequence analysis of a candidate gene at this locus, ADAMTSL2, which is responsible for the human TGFβ dysregulation syndrome, Geleophysic Dysplasia (GD), uncovered a mutation in exon 7 (c.660C>T; p.R221C) perfectly associated with MLS (p-value=10(-12))."

> "The genetic basis of MLS is a founder mutation in ADAMTSL2, previously shown to interact with latent TGF-β binding protein, which binds fibrillin-1. The molecular effect of the founder mutation on ADAMTSL2 is formation of disulfide-bonded dimers."

MLS is genetically a **geleophysic-dysplasia** homolog, not an SSS homolog — but it lands in the same microfibril/LTBP/TGF-β network one node over. **Autosomal recessive, founder mutation.** Good comparative-biology material; bad "animal model of SSS" material.

- Species: dog, `NCBITaxon:9615`; breed Beagle (⚠ VBO id unverified)
- Orthologous gene: ADAMTSL2 (`NCBIGene:9719` in human; canine ortholog per Ensembl)
- OMIA: MLS is catalogued in OMIA — ⚠ I did not retrieve the OMIA accession; look it up before curating.

### 14.3 Comparative biology and evolutionary conservation

The FBN1 RGD motif and the TB-domain architecture are deeply conserved across vertebrates — which is exactly why the mouse knock-in works (mouse W1572 = human W1570, a 2-residue offset from a small indel in the alignment). The broader lesson from the animal side: **you can arrive at stiff, fibrotic skin from multiple points in the fibrillin/LTBP/ADAMTSL/TGF-β network** — fibrillin-1 itself (human SSS, Tsk mouse), ADAMTSL2 (dog MLS, human GD), ADAMTS10 (Weill-Marchesani; and *"although surviving mice were slightly smaller and had stiff skin"* — PMID:30201140). The network has one output and several inputs.

### 14.4 Transmission

**Zoonotic potential: none.** Cross-species susceptibility: not applicable. Genetic disorder, not transmissible.

---

## 15. Model Organisms

### 15.1 Genetic mouse models — the flagship

**Gerber et al. 2013 knock-in lines (PMID:24107997)** are the definitive SSS models and the source of essentially all interventional mechanism data.

| Allele | Nature | Notes |
|---|---|---|
| **Fbn1 W1572C** | Knock-in, mouse equivalent of human W1570C | The disease-analogous model |
| **Fbn1 D1545E** | Knock-in, RGD→RGE | Obligate loss of integrin binding — the mechanistic control |

Abstract-level verbatim support: *"mouse lines harbouring analogous amino acid substitutions in fibrillin-1 recapitulate aggressive skin fibrosis that is prevented by integrin-modulating therapies and reversed by antagonism of the pro-fibrotic cytokine transforming growth factor β (TGF-β)."*

⚠ **Full-text details** (retrieved via an automated reader, not verified against the PDF — **verify before quoting as evidence**): heterozygotes showed increased collagen deposition by 1 month and reduced subcutaneous fat by 3 months; homozygous W1572C showed accelerated fibrosis; homozygous D1545E was embryonic-lethal before E10.5; treatments were a β1-integrin-activating antibody (9EG7) and a panspecific TGF-β neutralizing antibody (1D11) over 12 weeks; β3-integrin haploinsufficiency/deficiency also normalized the phenotype; immune findings included CD317+ pDCs expressing IL-6 and IFN-α, plus CD4+IL-4+ Th2, CD4+IL-17+ Th17 and CD4+IL-9+ Th9 cells, with anti-nuclear and anti-topoisomerase I autoantibodies. **These are excellent leads for `readouts` and `modeled_mechanisms`, but they came out of a summarizer and need the actual paper before they go in a KB entry.**

### 15.2 The Tight-skin (Tsk) mouse — related but not SSS

`Fbn1^Tsk` — a spontaneous **in-frame internal duplication** in Fbn1. PMID:19541933 verbatim: *"the tight-skin (TSK) mouse, which harbors a spontaneous internal duplication in the microfibrillar glycoprotein fibrillin-1."* PMID:15022335 verbatim: *"Skin fibrosis in the TSK mouse, a model of skin fibrosis seen in systemic sclerosis (SSc), is caused by a large in-frame duplication in the Fbn1 gene, tsk-Fbn1."*

Mechanistic finding (PMID:15022335, verbatim): *"Expression of tsk-Fbn1 in cultured MEF cells altered the morphology of Fbn-1 fibers and increased the deposition of type I collagen into the extracellular matrix (ECM) without concomitantly changing messenger RNA expression, secretion, or processing of type I procollagen."*

**That last clause is the important one:** the collagen surplus arises from **altered matrix deposition/retention**, not from cranking up collagen transcription. Same conclusion as the reduced-MMP-2 finding in human segmental fibroblasts, arrived at independently. Both point at the drain, not just the tap.

Tsk is a **structurally distinct** lesion (duplication vs missense) and is conventionally an SSc model rather than an SSS model. Relationship: `PARTIALLY_RECAPITULATES` at best, with the duplication-vs-missense difference as an explicit `limitations` entry. Also note the Tsk lung phenotype (emphysema, PMID:19541933) which human SSS does **not** have — that's a `FAILS_TO_RECAPITULATE` candidate.

### 15.3 Network-adjacent mouse models

- **Adamtsl2^−/−** (PMID:25762570) — geleophysic dysplasia model; neonatal lethal; *"An increase in microfibrils in the bronchial wall was associated with increased FBN2 and microfibril-associated glycoprotein-1 (MAGP1) staining."* Notably: *"treatment with TGFβ-neutralizing antibody did not correct the epithelial dysplasia"* — a useful negative result showing not everything in this network is TGF-β-downstream.
- **Adamts10^−/−** (PMID:30201140) — *"surviving mice were slightly smaller and had stiff skin"*; identified fibrillin-2 as a novel ADAMTS10 substrate.

### 15.4 Cellular and in vitro systems

| System | What it's good for | Source |
|---|---|---|
| Patient lesional dermal fibroblasts | Signaling (pERK1/2, NF-κB, nuclear pSmad2), ECM gene expression, MMP-2 zymography, drug rescue | PMID:32698527 |
| GFP-tagged full-length fibrillin-1 microfibril assembly assay | Discriminating secretion failure (MFS) from assembly-competent mutants (SSS) | PMID:25979247 |
| Recombinant fibrillin-1 fragment + integrin-transfected adhesion panel | Per-integrin dissection of the adhesion defect | PMID:31640988 |
| Recombinant-cell early fibrillin-1 assembly monitoring | Assembly kinetics | PMID:24559401 |
| Conditional tsk-Fbn1 expression in MEFs | Matrix deposition without transcriptional change | PMID:15022335 |

⚠ **No iPSC-derived model, no organoid, no skin-on-chip, and no immortalized SSS cell line** exists for this disease. That's a `KNOWLEDGE_GAP` with a concrete `proposed_experiments` entry attached — patient-derived iPSC → fibroblast/skin-organoid differentiation would be a genuinely useful thing for someone to build.

### 15.5 Model limitations, stated plainly

1. **The inflammation discrepancy** (§6.6) — the mouse has a florid immune infiltrate and autoantibodies; human histology is bland. This is the headline mismatch.
2. **Homozygous vs heterozygous** — human SSS is heterozygous; several mouse findings come from homozygotes.
3. **Contractures** — mouse skin fibrosis is not obviously accompanied by the joint contractures that dominate human morbidity. The mouse is a skin model, not a disability model.
4. **Tsk is the wrong mutation class** and carries a lung phenotype humans lack.
5. **The dog "models" aren't models** — one has no identified gene and recessive inheritance (WHWT), the other is in a different gene entirely (Beagle/ADAMTSL2).

### 15.6 Model resources

MGI (Fbn1, MGI:95489 — ⚠ ID not independently verified this session), IMSR, Alliance of Genome Resources, JAX (Tsk strain is a long-standing JAX line), OMIA for the canine conditions.

---

## ⚠ Verification notes — what I could NOT confirm

Being explicit so nothing here gets curated as fact when it's a lead:

1. **Loeys 2010 full text is paywalled.** Europe PMC returned zero bytes for PMC2953713. The four SSS variants are confirmed via **ClinVar + OMIM allelic-variant xrefs** (FBN1 .0050–.0053, all xref'd to OMIM:184900), which is solid independent confirmation. But per-family assignments, de novo status, and the exact elastin/pSmad2/CTGF wording came from an automated page reader and are **not** verbatim-verified. **Do not use them as evidence snippets.** One number that reader gave me was outright wrong (it said "Gly1594Asn"; ClinVar says p.Gly1594**Asp**) — treat everything else from that source with matching suspicion.
2. **Gerber 2013 full-text details** in §15.1 (doses, antibody clones, timelines, immune subsets) — same caveat. The *abstract* quotes in §6.6 and §12.4 are verbatim and safe.
3. **ICD-10 code** — not verified. MONDO carries an ICD-11 *foundation* id (642409035) only. Don't assert an ICD-10 code.
4. **Orphanet prevalence** — the API's prevalence endpoint didn't resolve for ORPHA:2833. No quantitative estimate obtained.
5. **Sex ratio** — no abstract reported one. Don't assert.
6. **VBO breed IDs and the OMIA accession for MLS** — not retrieved.
7. **gnomAD absence** — I queried by ClinVar-derived GRCh38 coordinates (15:48467975, 15:48467994) with C>G alleles and got "Variant not found" for both. FBN1 is on the minus strand, so I inferred the genomic allele from cDNA; the "not found" result is consistent with absence but I did not separately confirm the reference base.
8. **Reactome/KEGG pathway accessions** in §6.2 — written from knowledge, not looked up. Verify before use.
9. **MGI:95489** — not verified this session.
10. **Several key papers are abstract-free in PubMed** (PMID:22211327, 27846975, 32212274, 34411278, 30704628, 25200307, 5100776, 5173296). Per the dismech title-snippet rule, their titles are the only quotable text; some of those titles *do* state results (22211327, 27846975) and are usable with that noted, but the two 1971 Esterly papers are pure topic titles and should not be cited as evidence snippets — cite them in `notes:` as historical provenance instead.

---

## Curation recommendations for the dismech entry

A few things that jumped out as I went, in rough priority order:

1. **The `HUMAN_MODEL_MISMATCH` discussion in §6.6 is the highest-value thing in this entry.** Mouse = inflammatory fibrosis with autoantibodies; human = "completely lacked lymphocyte infiltration" across 31 biopsies. That's not a hedge, it's a genuine unresolved translational question, and it's exactly what that discussion kind exists for.
2. **Two evidence-conflict items need `mechanistic_hypotheses` or careful `supports` grading:** Guiducci's unchanged TGF-β transcript vs Loeys's elevated TGF-β signaling (§6.4), and the IL17C-variant-to-anti-IL17A-drug leap (§12.3).
3. **`fibrotic_response` conformance should be declared node-by-node**, explicitly skipping the inflammation node. The skip is the science.
4. **Leave `datasets:` and `clinical_trials:` empty** and record the absence in `notes:`. I checked both; there's genuinely nothing, and searching FBN1 for datasets will drag in Marfan material — the exact NEC-via-dataset-search trap the SOP warns about.
5. **Fetch the four reference-cache entries before writing any evidence**: `just fetch-reference PMID:20375004 PMID:24107997 PMID:25979247 PMID:31640988` plus the cohort papers. Several of my best quotes are long compound sentences — pre-test them against the cache before the first Write, since a blocked write is a no-op and you'd be re-emitting the whole file.
6. **Watch the square brackets.** A few of the abstracts contain bracketed frequency notation like "Very frequent (99-80%)" — fine — but the ClinVar titles use `>` characters that HTML-escape oddly, and the ORPHA-style pipe rows need care. Nothing I quoted above has square brackets, but check anything you pull fresh.

There's a They Might Be Giants line about a person who's "a self-contained, self-perpetuating system" — which is more or less what an SSS fibroblast is doing. No inflammatory trigger, no autoimmune drumbeat, no external insult. Just a cell that can't feel the matrix it built, building more of it, forever. That's the whole disease in one sentence, and it's why it taught us so much about the fibrosis that *does* have a trigger.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 47 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |

All extracted references resolved successfully.