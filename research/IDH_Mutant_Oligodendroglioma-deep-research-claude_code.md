---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-13T16:27:47.816254'
end_time: '2026-08-13T16:38:16.569895'
duration_seconds: 628.75
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: IDH-Mutant and 1p/19q-Codeleted Oligodendroglioma
  mondo_id: ''
  category: ''
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
  web_search_requests: 17
  num_turns: 18
  total_cost_usd: 3.317425
  session_id: f8f5dbc2-2a92-4911-9cd1-126ee4abb6e0
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 48
reference_validation:
  total_references: 35
  verified: 19
  not_found: 0
  unverifiable: 16
  confabulation_rate: 0.0
  quotes_checked: 0
  quotes_valid: 0
  quotes_not_checkable: 1
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** IDH-Mutant and 1p/19q-Codeleted Oligodendroglioma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **IDH-Mutant and 1p/19q-Codeleted Oligodendroglioma** covering all of the
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

# IDH-Mutant and 1p/19q-Codeleted Oligodendroglioma — Research Report

*Prepared as a curation input for a dismech `Disease` entry. Compiled 2026-08-13.*

---

## ⚠️ Read this before you copy anything into YAML

Everything below is a **lead**, not ground truth. Two specific hazards:

1. **PMIDs.** IDs I pulled directly out of live search results this session are marked ✅. Everything marked ⚠ came out of my head and *must* be resolved with `just fetch-reference PMID:XXXX` before it lands in an evidence block. A real-but-wrong PMID is the nastiest failure mode there is — it sails through existence checks and quietly attributes a claim to a stranger.
2. **Ontology IDs.** Per the repo's own scar tissue, I am not going to guess CURIEs and let them look authoritative. Terms below are given **label-first**, with a candidate ID only where I'm genuinely confident, and everything gets a `runoak` verification note. Treat the labels as the payload and the numbers as a hint.

Direct quotes are given only where I actually retrieved the text; otherwise I paraphrase and say so. Think of this like a tissue sample — useful, but you still stain it yourself before signing the report.

---

## 1. Disease Information

### Overview

Oligodendroglioma, IDH-mutant and 1p/19q-codeleted is an **adult-type diffuse glioma** — one of exactly three such entities in the 2021 WHO Classification of CNS Tumours (CNS5), alongside astrocytoma IDH-mutant and glioblastoma IDH-wildtype. It is a diffusely infiltrating, slow-growing glial tumour of the cerebral hemispheres, with a strong appetite for the **frontal lobe** and a habit of creeping up into the cortex rather than staying politely in white matter.

The defining move of CNS5 is that this is no longer a *histological* diagnosis with molecular garnish. It is a **molecularly defined entity**: you cannot call something an oligodendroglioma in 2026 without both an IDH1/IDH2 mutation **and** whole-arm codeletion of 1p and 19q. A tumour that looks like a textbook fried-egg oligodendroglioma down the microscope but lacks codeletion is something else entirely. This is the single most important framing fact for the whole entry — the name now points at a genotype, and the histology is a supporting witness.

It is graded **CNS WHO grade 2 or grade 3** (there is no grade 4 oligodendroglioma in CNS5). The word "anaplastic" is retired as a name; grade 3 is just grade 3.

### Key identifiers

| System | Value | Confidence |
|---|---|---|
| ICD-O-3 morphology | **9450/3** (grade 2), **9451/3** (grade 3) | High — these are the CNS5 codes |
| ICD-10 | C71.x (malignant neoplasm of brain, by lobe); D43.x if behaviour uncertain | High |
| ICD-11 | 2A00 series (gliomas of brain); exact stem code ⚠ verify | Low |
| MeSH | **D009837** "Oligodendroglioma" | Medium-high ⚠ verify |
| MONDO | **⚠ Do not guess.** Look up "oligodendroglioma" and the CNS5-era "oligodendroglioma, IDH-mutant and 1p/19q codeleted" child term with `runoak -i sqlite:obo:mondo search "oligodendroglioma"`. Check obsoletion against **live OLS**, not the local sqlite build — the local one lags. | — |
| Orphanet | An ORPHA code exists for oligodendroglioma / anaplastic oligodendroglioma ⚠ verify via `just fetch-reference ORPHA:<code>` | Low |
| OMIM | No Mendelian entry for this tumour type. **OMIM 137800 (GLIOMA SUSCEPTIBILITY 1)** is the closest germline-susceptibility handle ⚠ verify | Low |
| NCIT | NCIT has both "Oligodendroglioma" and "Anaplastic Oligodendroglioma" concepts ⚠ look up with `runoak -i sqlite:obo:ncit` | — |

### Synonyms and historical names

- Oligodendroglioma, IDH-mutant and 1p/19q-codeleted (**current WHO name**)
- Anaplastic oligodendroglioma, IDH-mutant and 1p/19q-codeleted (**grade 3, WHO 2016 name — now discouraged as a name, retained only as a descriptor**)
- Oligodendroglioma NOS (used only when molecular testing is unavailable/inconclusive)
- Oligoastrocytoma / anaplastic oligoastrocytoma — **abolished**. This is worth a `notes` line: the old "mixed glioma" bucket dissolved once molecular testing showed nearly every one of them was really an oligodendroglioma *or* an astrocytoma. Diagnoses of "oligoastrocytoma" in pre-2016 literature must be re-read with that in mind, and this is a live source of miscoding in legacy cohorts.
- "1p/19q-codeleted glioma", "codeleted oligodendroglial tumour" (informal)

**NEC risk flag for this entry:** moderate-to-high. Not because of an eponym, but because of the *name-vs-entity drift* above — much of the classic literature ("anaplastic oligodendroglioma", "oligoastrocytoma", "low-grade glioma") describes cohorts that were assembled on histology and only retrospectively genotyped. Any DR report on this disease needs checking not for "did it find the wrong gene" but for "did it silently blend codeleted and non-codeleted cases". Run `just preflight-dr` and expect it may `SKIP` (this is a somatic cancer, so MONDO may not record a single causal gene) — the manual read is the one that matters here.

### Data provenance

Both. Disease-level aggregation (CBTRUS, SEER, Orphanet, WHO) plus a very unusual amount of **individual-patient long-term trial data** — RTOG 9402 and EORTC 26951 followed codeleted patients for two decades, which is rare enough in oncology to be worth citing on its own.

---

## 2. Etiology

### Primary causal factors

This is a **somatic, acquired** neoplasm. There is no meaningful inherited-Mendelian pathway to it. The causal chain, in order of events as best reconstructed from sequencing:

1. **IDH1 or IDH2 mutation** — the founding event, present in essentially 100% of cases by definition. Predominantly **IDH1 p.R132H**, with IDH1 R132C/R132G/R132S/R132L and IDH2 R172K/R172M/R172W/R172G making up the remainder. Notably, **non-canonical (non-R132H) IDH1 mutations and IDH2 mutations are enriched in oligodendroglioma relative to IDH-mutant astrocytoma** — a practical point, because the standard R132H immunostain misses them and you need sequencing.
2. **Whole-arm 1p/19q codeletion**, via an unbalanced translocation (below).
3. **TERT promoter hotspot mutation** (C228T or C250T) — near-universal in adults.
4. **CIC** (19q13.2) and/or **FUBP1** (1p31.1) inactivation — the "second hit" on the retained arms.
5. Variable later hits: **NOTCH1, TCF12, PIK3CA, PIK3R1, ZBTB20, ARID1A, SETD2, CDKN2A/B** (the last being a progression event).

Two things this tumour conspicuously **lacks**, and their absence is diagnostically load-bearing: **ATRX loss** and **TP53 mutation**. Those two define the *astrocytoma* branch of IDH-mutant glioma. IDH-mutant gliomas fork early into "codeletion + TERT" vs "ATRX + TP53", and the two roads essentially never meet.

### The 1p/19q codeletion mechanism (this is the fun part)

It is **not** two independent deletions. It's a single event: a **balanced whole-arm translocation t(1;19)(q10;p10)** creating two derivative chromosomes — one made of 1q+19p, the other of 1p+19q — followed by **loss of the der(1p;19q)**, leaving der(1;19)(q10;p10) behind.

> "A balanced whole-arm translocation between chromosomes 1 and 19 forms 2 derivative chromosomes, one composed of 1q and 19p, the other of 1p and 19q… the 1p–19q derivative is lost but the 1q–19p derivative is maintained throughout cell replication." — retrieved summary of Jenkins et al., *J Neuropathol Exp Neurol* 2006 ✅ **PMID:17021403**

Think of it as a bad cell division rather than two separate mutations — one clumsy shuffle of the deck, and two whole arms walk out the door together. This is why the codeletion is *whole-arm* and why partial 1p or 19q loss (common in astrocytomas and glioblastoma) does **not** count and must not be miscalled as codeletion. That distinction is a genuine diagnostic pitfall and belongs in the entry's `notes`.

### Genetic risk factors (germline)

The standout is **rs55705857**, a low-frequency non-coding SNP at **8q24.21**, near/within **CCDC26**:

> "The SNP rs55705857 confers a 6-fold greater risk of IDH-mutant glioma, and a 9-fold risk for oligodendroglioma with 1p19q codeletion, representing one of the highest reported inherited genetic associations with cancer." — retrieved from *Neuro-Oncology* review "Deciphering gliomagenesis from genome-wide association studies" (2023) ⚠ verify PMID

That is an extraordinary effect size for a GWAS hit — most common-variant associations are odds ratios of 1.1–1.3, and this one is functioning more like a low-penetrance Mendelian allele. And unusually, there's mechanistic follow-through: Yanchus et al., *Science* 2022, "A noncoding single-nucleotide polymorphism at 8q24 drives IDH1-mutant glioma formation" ⚠ verify PMID — showing the variant acts through an enhancer regulating **MYC** in a brain-lineage-specific way. This is a **strong candidate for a curated `genetic:` entry with `relationship_type: SUSCEPTIBILITY`** and probably the single most citable germline finding for the entry.

Other loci: **5p15.33 (TERT)**, **11q23 (PHLDB1)**, **20q13.33 (RTEL1)**, **9p21.3 (CDKN2B-AS1)**, **7p11.2 (EGFR)**, **17p13.1 (TP53)**. The IDH-mutant/non-GBM gliomas cluster preferentially on CCDC26, PHLDB1 and TP53-region variants; EGFR/TERT variants skew toward GBM. A 2023 Australian GWAS additionally reported a **stronger female risk association at 8q24.21** ⚠ verify PMID (PMC10326491) — interesting because the tumour is otherwise male-predominant, so the sex effect runs against the epidemiologic grain and deserves a hedged `notes` line rather than a confident claim.

**Familial/syndromic:** Rare families with clustering of IDH-mutant glioma exist; germline **POT1**, **TP53** (Li-Fraumeni), and mismatch-repair syndromes raise glioma risk broadly but are **not** specifically enriched for the codeleted phenotype. Do not curate Li-Fraumeni as a risk factor for *this* entity without a codeletion-specific source.

### Environmental risk factors

Thin, and honesty about that thinness is the correct curation posture.

- **Ionizing radiation to the head** — the only firmly established exogenous cause of glioma generally (therapeutic cranial RT, atomic-bomb survivor cohorts). Whether it specifically induces *codeleted* tumours is not established; radiation-associated gliomas are more often IDH-wildtype and high-grade. **Curate as a risk factor for glioma with an explicit scope caveat.** ECTO has exposure-to-ionizing-radiation terms suitable for `influences_mechanisms` with `environmental_effect: PREDISPOSES` — but given the codeletion-specificity gap, `MODULATES` or simply an unqualified note may be more defensible. (Repo guidance: `TRIGGERS`/`EXACERBATES` count toward compliance scoring, so don't reach for them on a contested claim.)
- **Mobile phones / RF-EMF** — repeatedly studied, no consistent association. Worth an explicit `supports: NO_EVIDENCE` or `REFUTE` evidence item if a good source is available; a well-curated negative is more useful here than silence.
- **Occupational/chemical exposures** (pesticides, petrochemicals, formaldehyde, vinyl chloride) — inconsistent, mostly null, small studies.
- **Head trauma, diet, smoking, alcohol** — no established association with glioma.

### Protective factors

One genuinely robust and genuinely weird finding: **atopy and allergic disease are inversely associated with glioma risk**. History of asthma, eczema, hay fever, and higher serum IgE all associate with reduced glioma risk across many studies. The mechanistic story — that a hair-trigger immune system is better at clearing nascent transformed glial cells, or that IL-4/IgE signalling is anti-tumorigenic — is unproven, but the epidemiology is consistent enough that it belongs in the entry.

- Also reported: history of **varicella-zoster/chickenpox infection** and VZV IgG positivity, inversely associated with glioma. ⚠ Verify with a recent pooled-analysis source before curating; this is a real literature but the effect sizes wobble.

Genetic protective factors: none established beyond the protective alleles at the risk loci above (i.e. the reference allele of rs55705857).

### Gene–environment interactions

Sparse. Some work on **immune/atopy genotype × allergy phenotype** interactions in glioma risk, and on DNA-repair genotype × radiation exposure. Nothing I would curate as a structured interaction claim without a specific, verified source. **Flag as a genuine `KNOWLEDGE_GAP` discussion** rather than leaving it blank — "we looked and it isn't there" is content.

---

## 3. Phenotypes

The clinical presentation is essentially "a slow-growing mass in the frontal cortex," and the seizure phenotype dominates. Oligodendrogliomas are the **most epileptogenic** of the diffuse gliomas — cortical location plus slow growth is exactly the recipe for building an irritable epileptic focus rather than crushing tissue outright.

| Phenotype | HPO label to look up | Frequency | Notes |
|---|---|---|---|
| **Seizure** (usually focal onset ± bilateral tonic-clonic) | Seizure (HP:0001250, high confidence); consider Focal-onset seizure | **VERY_FREQUENT** — presenting symptom in roughly 60–90% | The signature finding. Often the *only* symptom for years. |
| Headache | Headache (HP:0002315, high confidence) | FREQUENT | |
| Focal neurological deficit (hemiparesis, sensory loss) | Hemiparesis; Focal neurological deficit ⚠ | OCCASIONAL–FREQUENT | Depends on location |
| Personality/behavioural change, executive dysfunction | Personality changes; Frontal lobe dysfunction ⚠ | FREQUENT | Frontal predilection makes this common and frequently under-recognised |
| Cognitive impairment | Cognitive impairment ⚠ | FREQUENT | Both tumour- and treatment-related |
| Aphasia / language disturbance | Aphasia ⚠ | OCCASIONAL | Left frontal/temporal |
| Nausea and vomiting, papilledema (raised ICP) | Papilledema ⚠ | OCCASIONAL | Later/larger tumours |
| Visual field defect | Visual field defect ⚠ | OCCASIONAL | Temporal/occipital extension |
| Intratumoral haemorrhage | Intracranial hemorrhage ⚠ | RARE-OCCASIONAL | Oligodendrogliomas have a delicate chicken-wire vasculature and bleed a bit more than other low-grade gliomas |
| Hydrocephalus | Hydrocephalus ⚠ | RARE | With ventricular/leptomeningeal involvement |

**⚠ Frequency-band discipline:** per repo policy, each `frequency:` value makes its own quantitative claim and needs its own snippet. The seizure figure is well supported by multiple series (the "~80% of oligodendroglioma patients present with seizures" statement is standard in reviews) — but *find the sentence with the number in it* rather than mapping a review's adjective. For every other row above, **omit `frequency:` unless you have a cohort figure.** The band is not free.

### Phenotype characteristics

- **Age of onset:** adult, median **~45 years at diagnosis** (CBTRUS, all grades) ✅ **PMID:41092086**. Peak 35–55. Paediatric cases exist but are rare and molecularly distinct (see §4, TERT).
- **Severity:** variable; many patients are neurologically intact at diagnosis and remain so for years on antiseizure medication alone.
- **Progression:** **slowly progressive**, punctuated. `clinical_course: PROGRESSIVE`; the seizure phenotype itself is often `RECURRENT`/episodic. A long indolent plateau followed by malignant progression is the characteristic shape.
- **Quality of life:** the dominant long-term QoL drivers are (a) **seizure control**, (b) **neurocognitive decline** — which in long survivors is substantially *treatment*-attributable (cranial radiotherapy, PCV), not just tumour-attributable, and (c) **employment and driving loss** from epilepsy. This is a rare tumour where patients live long enough for late radiation neurotoxicity to become the main quality-of-life story, which is precisely the tension the IDH-inhibitor era is trying to resolve. Instruments in use: EORTC QLQ-C30 + QLQ-BN20, MMSE, and in INDIGO specifically, seizure and neurocognitive endpoints were exploratory outcomes ✅ **PMID:41175888**.

---

## 4. Genetic / Molecular Information

### Causal genes and lesions

| Gene / lesion | Locus | Frequency | Type | Consequence |
|---|---|---|---|---|
| **IDH1** (`hgnc:5382` ⚠ verify) | 2q34 | ~90% of IDH-mutant cases; R132H is ~90% of those in gliomas overall, **less dominant in oligodendroglioma** | Somatic heterozygous missense, arginine at the isocitrate-binding site | **NEOMORPHIC** — the textbook case. Loses normal isocitrate→α-KG activity, gains α-KG→**D-(R)-2-hydroxyglutarate** activity |
| **IDH2** (`hgnc:5383` ⚠) | 15q26.1 | ~5–10%; R172K/M/W/G | Somatic heterozygous missense | Same neomorphic gain |
| **1p/19q codeletion** | der(1;19)(q10;p10) | 100% by definition | Whole-arm unbalanced translocation | Loss of one copy each of 1p and 19q |
| **TERT promoter** | 5p15.33, C228T / C250T | **~98–99% in adults** | Somatic promoter point mutation creating an ETS binding site | **GAIN_OF_FUNCTION** — telomerase reactivation |
| **CIC** (`hgnc:` ⚠) | **19q13.2** | ~50–70% | Truncating and missense; on the *retained* 19q | **LOSS_OF_FUNCTION** tumour suppressor |
| **FUBP1** | **1p31.1** | ~15–30% | Mostly truncating; on the *retained* 1p | **LOSS_OF_FUNCTION** |
| **NOTCH1** | 9q34.3 | ~15–30% | Mixed | LOF in this context |
| **TCF12** | 15q21 | ~7% | Mixed | LOF |
| **PIK3CA / PIK3R1** | 3q26 / 5q13 | ~10–20% combined | Missense hotspot | PI3K activation |
| **CDKN2A/B** | 9p21.3 | ~10% overall, rising with grade (~11% in grade 3) | **Homozygous deletion** | LOF; adverse prognosis |
| **ZBTB20, ARID1A, SETD2** | various | low | Mixed | LOF |

The CIC/FUBP1 geography is elegant and worth stating explicitly in the pathophysiology prose: the codeletion removes *one* copy of 1p and 19q, and then point mutations knock out **CIC on the surviving 19q** and **FUBP1 on the surviving 1p**. It's Knudson's two-hit hypothesis executed with a chromosome-scale first hit — the translocation halves the dosage of two whole arms, and the second hits then only have to find one target apiece.

> "With the exception of a single case, all CIC mutations occurred in tumors with combined 1p/19q losses." — retrieved summary, Sahm et al., *Acta Neuropathol* 2012 ⚠ verify PMID

Key primary sources:
- **Bettegowda et al., "Mutations in CIC and FUBP1 contribute to human oligodendroglioma," *Science* 2011** ✅ **PMID:21817013** — the discovery paper.
- **Yip et al., "Concurrent CIC mutations, IDH mutations, and 1p/19q loss distinguish oligodendrogliomas from other cancers," *J Pathol* 2012** ✅ **PMID:22072542**.
- **Chan et al., "Loss of CIC and FUBP1 expressions are potential markers of shorter time to recurrence in oligodendroglial tumors," *Hum Pathol* 2014** ✅ **PMID:24030748** — prognostic angle.
- **Eckel-Passow et al., "Glioma groups based on 1p/19q, IDH, and TERT promoter mutations in tumors," *NEJM* 2015** ⚠ verify PMID — the "triple-positive" group framing.
- **TCGA Research Network, "Comprehensive, integrative genomic analysis of diffuse lower-grade gliomas," *NEJM* 2015** ⚠ verify PMID — the canonical genomic landscape.

### Variant classification, origin, allele frequency

- **Origin: somatic**, essentially without exception. This should be explicit in `GeneticContext.variant_origin` — germline IDH1 R132H does not exist as a viable constitutional state (Ollier/Maffucci disease involves somatic **mosaic** IDH1/IDH2 mutation, which is a genuinely interesting adjacent entity but a different disease).
- **Zygosity: heterozygous** — and this is mechanistically required, not incidental. The neomorphic reaction consumes α-KG produced by the *wild-type* subunit; the mutant enzyme works as a heterodimer with WT. Homozygous IDH1 mutation is selected against. Curate `zygosity: HETEROZYGOUS` with that as the rationale.
- **`functional_impact_category`:** use **`NEOMORPHIC`** for IDH1/IDH2 (not GAIN_OF_FUNCTION — the enzyme acquires a *new reaction*, which is exactly what the neomorphic category exists for), **`LOSS_OF_FUNCTION`** for CIC/FUBP1/NOTCH1/CDKN2A, **`GAIN_OF_FUNCTION`** for TERT promoter and PIK3CA hotspots.
- **Population allele frequency:** not applicable (somatic). gnomAD is the wrong database here. For **rs55705857**, gnomAD *is* appropriate — minor allele frequency is low (~2–5% in European ancestry, near-absent in African ancestry populations), which partly explains the ancestry skew in incidence.
- ClinVar/COSMIC: IDH1 R132H is COSMIC's most-catalogued glioma variant; ClinVar has somatic-oncogenicity classifications now (ClinGen/CGC/VICC oncogenicity framework rather than ACMG/AMP germline criteria — **use the right framework name in the entry**, it's a common miscitation).

### Epigenetics — the actual engine

IDH-mutant gliomas are the defining example of a **metabolic mutation causing a global epigenetic reprogramming event**, and this is where the pathophysiology graph should spend its detail budget:

- **G-CIMP** (glioma CpG island methylator phenotype), Noushmehr et al., *Cancer Cell* 2010 ⚠ verify PMID.
- **Turcan et al., "IDH1 mutation is sufficient to establish the glioma hypermethylator phenotype," *Nature* 2012** ⚠ verify PMID — the causality demonstration, and a strong `IN_VITRO`/`evidence_source` item.
- **Flavahan et al., "Insulator dysfunction and oncogene activation in IDH mutant gliomas," *Nature* 2016** ⚠ verify PMID — hypermethylation of CTCF binding sites → loss of insulation → an enhancer illegitimately activates **PDGFRA**. This is a beautiful, concrete, curatable mechanism node.
- **Histone hypermethylation** — elevated H3K9me3, H3K27me3, H3K4me3 from KDM inhibition. Note the twist: **loss of H3K27me3 is frequent in IDH1-R132H tumours but not in non-canonical IDH1/2-mutant codeleted oligodendroglioma** (Japanese cohort study, PMC8138926 ⚠ verify PMID) — a nice detail for a `distinguishing_features` note, and a caution against over-generalising "IDH-mutant = uniform epigenome."
- **Oligodendroglioma-specific methylation classes** exist in the DKFZ brain-tumour methylation classifier (`O IDH`), and methylation profiling is now a diagnostic modality in its own right (§10).

### Chromosomal abnormalities

- **1p/19q whole-arm codeletion** — definitional (see §2).
- **CDKN2A/B homozygous deletion (9p21.3)** — progression event, adverse prognosis. Frequency reaching ~11% in grade 3 ⚠ verify. Appay et al., *Neuro Oncol* 2019 ✅ **PMID:31832685** ("CDKN2A homozygous deletion is a strong adverse prognosis factor in diffuse malignant IDH-mutant gliomas").
  - **Important curation caveat:** cIMPACT-NOW/CNS5 use CDKN2A/B homozygous deletion to upgrade **IDH-mutant astrocytoma to grade 4**. It is **not** a formal grading criterion in oligodendroglioma (which caps at grade 3), even though it carries adverse prognostic weight there. Do not let a DR report blur those two.
- Recurrent secondary imbalances: loss of 4, 9p, 15q; gain of 7, 11q. Less stereotyped than in glioblastoma.

---

## 5. Environmental Information

- **Environmental factors:** ionizing radiation (established for glioma broadly; codeletion-specificity unproven). No established chemical/toxin cause. CTD will return low-quality co-mention associations here — treat with suspicion.
- **Lifestyle factors:** none established. Some reports of an inverse association with higher BMI/height patterns exist but are inconsistent and I would not curate them.
- **Infectious agents:** **none.** Explicitly not a viral tumour — do not conform this entry to `viral_oncogenesis`. CMV in glioma has been proposed repeatedly and repeatedly failed replication; if you curate it at all, curate it as `supports: REFUTE` or `NO_EVIDENCE` with a source. The atopy/varicella *protective* associations (§2) are the only immune-environment signals with legs.

---

## 6. Mechanism / Pathophysiology

Here's the causal chain, laid out the way a dismech pathograph wants it. I've suggested a `biological_scale` for each node.

### The spine of the cascade

**Node 1 — IDH1/IDH2 neomorphic mutation** (`MOLECULAR`)
Heterozygous R132/R172 substitution in the isocitrate-binding pocket. Loses isocitrate→α-KG; gains NADPH-dependent α-KG→**D-2-hydroxyglutarate**.
- GO: *isocitrate dehydrogenase (NADP+) activity* — GO:0004450 (medium-high confidence, verify); *tricarboxylic acid cycle*.
- `modifier: NEOMORPHIC` is not a ModifierEnum value — put NEOMORPHIC on `GeneticContext.functional_impact_category`, and use `modifier: DECREASED` on the isocitrate-dehydrogenase-activity descriptor. The gained activity is best modelled as a **separate node/molecular function** rather than trying to jam both into one modifier. (This is exactly the "single-value discipline" split the repo asks for.)

**Node 2 — D-2-hydroxyglutarate accumulation** (`MOLECULAR` / arguably `ORGANISM` since it's measurable in tumour tissue at millimolar levels)
> "…mutations at this position alter the activity of the IDH1 enzyme, which converts α-ketoglutarate to R-2-hydroxyglutarate, leading to the accumulation of R-2HG at millimolar levels in tumors." — retrieved summary
- CHEBI: *(R)-2-hydroxyglutarate* / *D-2-hydroxyglutaric acid* ⚠ look up; *2-oxoglutarate* CHEBI:16810 (high confidence).
- Sources: **Dang et al., *Nature* 2009** ⚠ verify PMID (the discovery that mutant IDH1 produces 2-HG).

**Node 3 — Competitive inhibition of α-KG-dependent dioxygenases** (`MOLECULAR`)
2-HG is a structural mimic of α-KG and jams the active site of >60 enzymes: **TET1/2/3** (5mC→5hmC), the **JmjC-domain histone demethylases (KDM)**, **prolyl hydroxylases**, **ALKBH/FTO**, **collagen prolyl-4-hydroxylase**.
> "2-HG is a competitive inhibitor of multiple α-KG-dependent dioxygenases, including histone demethylases and the TET family of 5-methylcytosine (5mC) hydroxylases. 2-HG occupies the same space as α-KG does in the active site of histone demethylases." — retrieved summary of **Xu et al., *Cancer Cell* 2011** ⚠ verify PMID
- The metaphor that actually helps here: 2-HG is a key that fits every lock in a whole family of enzymes and turns none of them. One metabolic typo, and sixty different maintenance crews are locked out of the building at once.

**Node 4a — DNA hypermethylation / G-CIMP** (`MOLECULAR`→`CELLULAR`)
TET inhibition → failure to demethylate → CpG island methylator phenotype.
- GO: *DNA methylation*; *negative regulation of transcription by RNA polymerase II*.

**Node 4b — Histone hypermethylation** (`MOLECULAR`)
KDM inhibition → elevated H3K9me3/H3K27me3/H3K4me3 → repressive chromatin.
- GO: *histone modification*, *chromatin organization*.

**Node 5 — CTCF insulator dysfunction and aberrant enhancer–oncogene contact** (`MOLECULAR`)
Methylation of CTCF sites → loss of topological insulation → enhancer hijack, e.g. **PDGFRA** activation (Flavahan 2016 ⚠).

**Node 6 — Block of glial differentiation / expansion of a stem-like compartment** (`CELLULAR`)
The epigenetic freeze locks cells in a progenitor-like state.
- CL: *oligodendrocyte precursor cell*, *neural stem cell*, *oligodendrocyte*, *astrocyte* — all ⚠ verify IDs.
- GO: *oligodendrocyte differentiation*, *glial cell development*, *stem cell population maintenance*.

**Node 7 — CIC loss → derepression of ETV1/4/5 → RTK/RAS/MAPK output** (`MOLECULAR`→`CELLULAR`)
This is the codeletion-specific arm and the reason this entry is *not* just "IDH-mutant glioma."
> "The best-characterized CIC targets in mammalian cells are the oncogenic transcription factors ETV1, ETV4, and ETV5… CIC functions to transduce receptor tyrosine kinase (RTK) signalling into gene expression changes through a mechanism termed default repression, wherein CIC is bound to target gene promoters or enhancers and inhibits transcription in the absence of signal." — retrieved summary, *Exp Mol Med* 2020 review ⚠ verify PMID
> "In patient-derived oligodendroglioma cells, CIC re-expression or ETV5 blockade decreases lineage bias, proliferation, self-renewal, and tumorigenicity." — retrieved summary ⚠ verify PMID
- CIC is a **default repressor** — normally sitting on ETV promoters with the brake on, released only when RTK/RAS signalling says so. Delete CIC and you've cut the brake cable; the ETV factors run continuously regardless of upstream signal. This maps cleanly onto the existing **`sustaining_proliferative_signaling`** module and, in its adaptor-proximal reading, onto **`rtk_grb2_signaling_adaptation`**.
- GO: *negative regulation of transcription by RNA polymerase II*, *Ras protein signal transduction*, *ERK1 and ERK2 cascade*.

**Node 8 — FUBP1 loss → dysregulated MYC and RNA metabolism** (`MOLECULAR`)
FUBP1 binds the FUSE element upstream of **MYC** and regulates its transcription; it also has roles in splicing and RNA binding. Its loss in oligodendroglioma is less mechanistically nailed-down than CIC's — worth a **`KNOWLEDGE_GAP` discussion**, honestly, rather than an overconfident causal edge.

**Node 9 — TERT promoter mutation → telomerase reactivation → replicative immortality** (`MOLECULAR`→`CELLULAR`)
C228T/C250T create de novo **ETS/GABP** binding motifs upstream of TERT; GABPA/B recruitment reactivates transcription of an otherwise-silenced telomerase.
- GO: *telomere maintenance*, *telomerase activity*.
- **Direct conformance target: `enabling_replicative_immortality#Telomere Maintenance Reactivation`.** This is a textbook fit.

**Node 10 — Cell cycle / checkpoint escape** (`CELLULAR`)
CDKN2A/B homozygous deletion (in a minority, enriched at grade 3) → loss of p16INK4a → CDK4/6-cyclin D unrestrained → RB phosphorylation → S-phase entry.
- **Conformance targets: `evading_growth_suppressors#Loss of Cell-Cycle Checkpoint Control`**, and this is also the mechanistic rationale linking to **`cdk46_inhibitor_resistance`**'s dependency node (CDK4/6 inhibitors are under investigation here).
- Note the counter-current: the same senescence machinery makes **`senescence_tumor_suppression`** relevant as the *protective* arm in low-grade disease.

**Node 11 — Immune quiescence / "cold" microenvironment** (`TISSUE`)
D-2-HG is not just an epigenetic agent — it's exported and taken up by immune cells.
> "(R)-2-hydroxyglutarate drives immune quiescence in the tumor microenvironment of IDH-mutant gliomas" — **Bunse et al., *Nat Med* 2018** ⚠ verify PMID (PMC6448779 ✅ retrieved)
- Mechanism: 2-HG taken up by T cells → inhibits **ATP-dependent T-cell receptor signalling / NFAT activation**, suppresses polyamine metabolism → reduced T-cell proliferation and IFN-γ. Separately, 2-HG dampens microglial activation via **FTO/NF-κB** (*Front Oncol* 2025 ⚠) and drives DNA hypermethylation at microglial lineage enhancers (bioRxiv 2024 — **preprint, flag as such**).
- CL: *microglial cell*, *CD8-positive alpha-beta T cell*, *macrophage*.
- This is the mechanistic explanation for why checkpoint blockade has underperformed in IDH-mutant glioma, and it's a good candidate for a *contrasting* note against the `immune_checkpoint_blockade` module rather than a conformance to it.

**Node 12 — Diffuse infiltration and secondary structures of Scherer** (`TISSUE`)
Perineuronal satellitosis, subpial and perivascular accumulation — the tumour uses existing brain architecture as scaffolding. This is why gross total resection is anatomically impossible and why "cure" isn't the operative concept.
- UBERON: *cerebral cortex*, *white matter of cerebral hemisphere*, *frontal cortex*.

**Node 13 — Cortical irritation → epileptogenesis** (`TISSUE`→`ORGANISM`)
Peritumoral glutamate excess (glioma cells export glutamate via system xc−), altered GABAergic inhibition, peritumoral acidosis and altered chloride homeostasis → excitation/inhibition imbalance.
- **Conformance target: `epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance`.** Strong fit and probably an under-exploited one for glioma entries generally.

**Node 14 — Malignant progression** (`TISSUE`)
Acquisition of CDKN2A/B loss, increased mitotic activity, microvascular proliferation, necrosis → grade 3 behaviour → mass effect and neurological decline.

### The tumour's own developmental hierarchy (single-cell)

The most important piece of modern biology for this entry:

> "…human oligodendrogliomas contain cancer cells specialized into two types of glia, as well as a rare subpopulation of cells that are undifferentiated and display a gene expression program characteristic of neural stem cells… cells displaying proliferation signatures highly enriched in this rare subpopulation, consistent with a cancer stem cell model." — **Tirosh et al., *Nature* 2016** ✅ **PMID:27806376** (4,347 single cells from six IDH-mutant tumours)

Curate this as a distinct pathophysiology node — **a stem-like NSC-programme subpopulation that does the proliferating, with astrocyte-like and oligodendrocyte-like differentiated progeny** — with `evidence_source: IN_VITRO` (or a mix; the profiling is on human tumour tissue with functional follow-up in lines). It reframes the tumour from "a lump of one cell type" to "a small, badly-behaved developmental tree," and it directly explains why cytoreduction alone doesn't cure.

### Metabolic and other omics layers

- **Metabolomics:** the killer signature is **D-2-HG at millimolar concentration**, detectable *in vivo* by MR spectroscopy (§10). Also: NAD+ dependency (IDH-mutant cells are sensitive to NAMPT inhibition), altered glutamate/glutamine handling, reduced NADPH and heightened oxidative-stress vulnerability. MetaboLights/Metabolomics Workbench will have glioma 2-HG datasets.
- **Transcriptomics:** TCGA LGG (`tcga:LGG`) is the reference cohort; GEO holds the Tirosh single-cell data — **Single Cell Portal study SCP12, "Oligodendroglioma intra-tumor heterogeneity"** ✅ retrieved, a strong candidate for a `datasets:` record (run `just verify-datasets` regardless).
- **Proteomics:** CPTAC has glioma proteogenomics; less oligodendroglioma-specific depth.
- **Functional genomics:** DepMap has few true 1p/19q-codeleted models (see §15 — this is the field's central practical bottleneck).
- **DNA repair:** IDH mutation induces a **homologous-recombination defect ("BRCAness")** via 2-HG inhibition of KDM4A/B, creating PARP-inhibitor sensitivity — a real, actively-trialled vulnerability. **Conformance candidate: `dna_repair_synthetic_lethality#PARP and Platinum Synthetic Lethality`.** Interestingly, there's a counter-finding that IDH1-R132H *upregulates* the DNA damage response and can act tumour-suppressively (Núñez et al., *Sci Transl Med* 2019 ⚠ verify PMID) — genuinely contested, and a good candidate for two curated `mechanistic_hypotheses` rather than one flattened claim.

---

## 7. Anatomical Structures Affected

**Organ level**
- Primary: **brain**, specifically the **cerebral hemispheres** (UBERON: *brain* UBERON:0000955 — high confidence; *cerebral hemisphere*, *telencephalon* ⚠ verify).
- **Frontal lobe is the strong favourite** (roughly half of cases), then temporal, parietal, occipital. Posterior fossa, brainstem, and spinal cord locations are rare and should raise doubt about the diagnosis.
- Body system: **nervous system** only. This tumour does not metastasise outside the CNS in any meaningful way (extraneural spread is a vanishing case-report phenomenon).
- Secondary involvement: leptomeninges (rare, late), ventricular system → hydrocephalus (rare).

**Tissue and cell level**
- Tissue: **cerebral cortex** and **subcortical white matter** together — the cortical–subcortical straddle is characteristic and radiologically useful (§10).
- Cell of origin: contested but most evidence points to the **oligodendrocyte precursor cell (OPC)** / **NG2 glia** lineage, or a **neural stem cell** in the subventricular zone acquiring an OPC-like programme. The single-cell hierarchy work (Tirosh) supports an NSC-like apex with OPC/astrocyte-like differentiation. **Curate this as a hypothesis with `mechanistic_hypotheses`, not as settled fact.**
- CL terms to look up: *oligodendrocyte precursor cell*, *oligodendrocyte* (CL:0000128, high confidence), *neural stem cell*, *astrocyte*, *microglial cell*, *neuron* (for satellitosis).

**Subcellular level**
- **Mitochondrion** (IDH2 is mitochondrial; GO:0005739) and **cytosol** (IDH1 is cytosolic/peroxisomal; GO:0005829, GO:0005777) — a nice detail, because the same neomorphic chemistry happens in two different compartments depending on which gene is hit.
- **Nucleus / chromatin** (GO:0000785 chromatin) — where the actual damage lands.
- **Telomere** (GO:0000781 chromosomal telomeric region) ⚠.

**Localization**
- **Unilateral** at presentation in the great majority; supratentorial; often crossing into the corpus callosum with progression. Bilateral/butterfly presentation is uncommon and more suggestive of glioblastoma.
- UBERON: *frontal cortex*, *temporal lobe*, *corpus callosum*, *white matter* — all ⚠ verify.

---

## 8. Temporal Development

**Onset**
- Adult, median **~45 years** ✅ **PMID:41092086**. Younger than IDH-wildtype glioblastoma (median ~65) and slightly older than IDH-mutant astrocytoma.
- Pattern: **insidious**. The tumour has usually been growing for years by the time it announces itself — often with a single seizure in a person who is otherwise entirely well. Volumetric studies of untreated low-grade glioma show slow, roughly linear diameter growth (~4 mm/year) during the indolent phase.
- Paediatric/teenage cases occur but are molecularly distinct: **TERT promoter mutation is typically absent** in teenage-onset codeleted oligodendroglioma (0/5 cases vs 87/88 adult cases in TCGA) — retrieved from *Acta Neuropathol Commun* 2018, PMC6145350 ⚠ verify PMID. Excellent candidate for a `has_subtypes` entry or at minimum a `distinguishing_features` note.

**Progression**
- Stages: (i) occult/indolent growth; (ii) symptomatic grade 2 disease; (iii) grade 3 progression; (iv) treatment-refractory disease. Note there is **no formal AJCC/TNM stage** for CNS tumours — grading substitutes for staging, which is a modelling detail worth capturing so nobody goes looking for a stage field.
- Rate: **slow**, the slowest of the adult diffuse gliomas. Median overall survival in codeleted patients receiving RT+PCV is on the order of **14 years** (§11).
- Course: **progressive with a long plateau**. Not relapsing-remitting. Malignant transformation is the rule if the patient lives long enough — the question is *when*, not *whether*.
- Duration: **chronic, lifelong**, essentially never self-limited and essentially never cured. This is the framing that makes it, functionally, a chronic disease of young adults that happens to be a cancer.

**Patterns**
- Spontaneous remission: does not occur.
- Treatment-induced response: yes — and slowly. Radiographic response to PCV or temozolomide can continue to deepen for **months to years** after treatment ends, which is unusual in oncology and matters for response assessment (RANO-LGG accounts for it).
- **Critical intervention windows:** (a) at diagnosis — extent of resection matters, and there is evidence that early maximal safe resection improves outcome; (b) the **watch-and-wait vs early-treatment decision** in asymptomatic, fully-resected young patients — historically a genuine equipoise, now being renegotiated by vorasidenib; (c) before malignant transformation — the entire logic of the IDH-inhibitor era is that intervening during the indolent phase might delay the point of no return, and might also let you defer cranial radiotherapy and its late cognitive cost.

---

## 9. Inheritance and Population

**Epidemiology**
- **Incidence: 0.29 per 100,000 population per year** for IDH-mutant & 1p/19q-codeleted oligodendroglioma, all grades (CBTRUS 2018–2022) ✅ **PMID:41092086**. For a dismech `Prevalence` record: `measure_type: ANNUAL_INCIDENCE`, `rate_per_100000: 0.29`, `population: United States`, `prevalence_class: BAND_1_9_PER_1000000` ⚠ (0.29/100,000 = 2.9 per million, so that band is right, but sanity-check the enum boundary yourself).
- Oligodendrogliomas make up roughly **1–2% of all primary brain tumours** and ~5% of gliomas — considerably less than older histology-based series claimed, because the molecular definition pruned the category hard.
- Prevalence is higher than incidence would suggest *relative to other gliomas*, because survival is long — a slow-burning tumour accumulates prevalent cases. Explicit point-prevalence figures are scarce; **flag as a gap** rather than back-calculating one.
- **Sex ratio:** male predominance, **43.9% female** ✅ **PMID:41092086** — so roughly **1.3:1 M:F**.
- **Ancestry/ethnicity:** **75.4% non-Hispanic White** ✅ **PMID:41092086**. Incidence is markedly lower in Black and Asian populations. The rs55705857 allele-frequency gradient (§4) is a plausible partial explanation — a rare case where a GWAS variant may actually account for some of an observed incidence disparity, though ascertainment differences absolutely also contribute and the entry should say so.
- **Age distribution:** median 45 at diagnosis; broad 20–70 range; uncommon under 20 and over 75.
- **Geographic:** no strong endemic pattern beyond what ancestry composition and diagnostic-access differences predict.

**Inheritance**
- **Not inherited.** Somatic. Inheritance pattern for the tumour itself: **not applicable** — do not populate an `inheritance:` block with a Mendelian mode.
- The germline **susceptibility** story (rs55705857 etc.) is real but polygenic/low-penetrance. If you want to model it, the right HPO anchor is **Polygenic inheritance (HP:0010982)** with `relationship_type: SUSCEPTIBILITY` on the gene entries — but honestly, for a somatic cancer I'd model the risk allele in `genetic:` and leave `inheritance:` empty rather than force it.
- Penetrance, expressivity, anticipation, germline mosaicism, founder effects, carrier frequency, consanguinity: **all not applicable.** Say so explicitly — an empty field reads as "not yet curated," whereas an explicit N/A is information.

---

## 10. Diagnostics

### Imaging

- **MRI** is the workhorse. The classic triad, and it's genuinely useful:
  > "Lack of T2-FLAIR mismatch, cortical-subcortical involvement in frontal lobe and presence of calcification raises the possibility of an oligodendroglioma." — retrieved
  - **Absence of the T2-FLAIR mismatch sign.** The mismatch sign (bright on T2, dark centrally on FLAIR) is a near-specific marker for IDH-mutant, **1p/19q-INTACT** astrocytoma. Its *absence* in an IDH-mutant tumour therefore argues toward oligodendroglioma. This is a lovely example of a diagnostically useful negative — but note it's a rule-*in* for astrocytoma, not a rule-in for oligodendroglioma, and shouldn't be over-claimed.
  - **Calcification** — strongly associated with codeletion; best seen on CT or SWI/GRE. One of the few remaining good reasons to get a CT in a brain-tumour workup.
  - **Cortical–subcortical, frontal, ill-defined margins, heterogeneous, often T1-hypo/T2-hyper, variable and typically minimal enhancement at grade 2.**
- **MR spectroscopy for 2-HG** — a genuine non-invasive molecular biomarker. 2-HG-edited MRS detects the oncometabolite in vivo (Choi et al., *Nat Med* 2012 ⚠ verify PMID). Technically demanding, not universal, but conceptually striking: you can see the mutation's product through the skull.
- **PET:** amino-acid tracers (¹¹C-methionine, ¹⁸F-FET, ¹⁸F-FDOPA) outperform FDG for low-grade glioma; higher uptake correlates with grade. Perfusion MRI (rCBV) is often *paradoxically elevated* in oligodendroglioma even at grade 2 because of that dense chicken-wire capillary network — a classic trap that can make a grade 2 oligodendroglioma look high-grade on perfusion.

### Histopathology

- Monotonous round nuclei with perinuclear halos — the **"fried egg"** appearance (a formalin-fixation artifact, absent on frozen section and smears, which trips up intraoperative diagnosis).
- **Delicate branching "chicken-wire" capillary network.**
- **Microcalcifications**, often perivascular.
- **Secondary structures of Scherer**: perineuronal satellitosis, subpial and perivascular aggregation.
- Grade 3 features: brisk mitotic activity, microvascular proliferation, necrosis. **CNS5 removed the hard "≥6 mitoses per 10 HPF" cutoff** — retrieved summary — because the literature didn't support a clean threshold by mitotic count or Ki-67.
- IHC: **IDH1 R132H-mutant-specific antibody** (positive in ~90% of IDH-mutant gliomas overall, **but a negative stain does NOT exclude — sequence it**, especially here where non-canonical mutations are enriched); **ATRX retained** (loss argues astrocytoma); **p53 wild-type pattern** (strong diffuse nuclear p53 argues astrocytoma); **OLIG2 positive**; **IDH1/2 + retained ATRX + no p53 overexpression** is the immunophenotypic signature. Loss of CIC and FUBP1 nuclear staining can be assessed by IHC and correlates with mutation (Chan 2014 ✅ **PMID:24030748**).

### Molecular testing — mandatory, not optional

1. **IDH1/IDH2 status** — IHC first, then sequencing (Sanger/NGS) if IHC-negative, especially in patients under 55.
2. **1p/19q codeletion** — **FISH** (interphase, showing net whole-arm loss; "77% to 92% of cells" showing net loss in one reference set, retrieved), **SNP array / chromosomal microarray**, **NGS with copy-number calling**, or **MLPA**. **Array or NGS-CNV is preferable to FISH** because FISH probes interrogate a couple of loci and can be fooled by partial deletions — the exact error that turns a glioblastoma into a fake oligodendroglioma. This is a genuinely important caveat to curate.
3. **TERT promoter** (C228T/C250T) — supportive; near-universal in adults, absent in teenagers.
4. **NGS panel** — CIC, FUBP1, NOTCH1, TCF12, PIK3CA, CDKN2A/B copy number, plus a broad exclusion sweep for EGFR amplification / chromosome 7 gain + 10 loss (which would push toward IDH-wildtype glioblastoma).
5. **DNA methylation profiling** (EPIC array + DKFZ classifier) — increasingly a tie-breaker for ambiguous cases and now embedded in routine practice at reference centres.
6. **Liquid biopsy / CSF ctDNA** — emerging. CSF is far more informative than plasma for CNS tumours. Not standard of care; curate as investigational.

**Germline testing:** not routine. Consider only with a striking family history or syndromic features.

### Clinical criteria and differential diagnosis

**Diagnosis is by integrated histological + molecular criteria per WHO CNS5** — there is no clinical criteria set, no DSM-analogue. The differential:

| Alternative | How you tell it apart |
|---|---|
| **Astrocytoma, IDH-mutant** | 1p/19q **intact**; **ATRX loss**; **TP53 mutation**; T2-FLAIR mismatch sign often present |
| **Glioblastoma, IDH-wildtype** | IDH-wildtype; +7/−10; EGFR amplification; TERT promoter mutation *without* IDH mutation; older patients; necrosis/MVP |
| **Clear cell ependymoma** | Perivascular pseudorosettes; EMA dot-like positivity; ZFTA fusion; IDH-wildtype |
| **Central neurocytoma / DNET / other clear-cell neuronal tumours** | Synaptophysin/NeuN positive; intraventricular (neurocytoma); IDH-wildtype |
| **Pilocytic astrocytoma** | KIAA1549-BRAF fusion; Rosenthal fibres; younger; circumscribed |
| **Diffuse leptomeningeal glioneuronal tumour** | 1p deletion **without 19q**, IDH-wildtype — a real mimic, worth naming |
| **Metastasis, demyelinating lesion, abscess** | Clinical/radiologic context |

The differential entries are strong candidates for the `differentials:` block — and per repo memory, **grep the sibling KB entries for their existing MONDO IDs rather than looking up new ones.**

### Screening

**No population screening exists or is justified** — the incidence is far too low. No newborn screening, no carrier screening. Cascade screening not applicable. Say this explicitly.

---

## 11. Outcome / Prognosis

This tumour has, by a wide margin, **the best prognosis of the adult-type diffuse gliomas** — which makes the survival numbers the most-cited facts about it.

**Survival**
- **1-year relative survival 96.5%** — highest among adult-type diffuse gliomas ✅ **PMID:41092086**.
- **5-year relative survival ~74%** (all grades, oligodendroglioma) ⚠ verify against the CBTRUS table directly rather than a secondary source.
- **Median overall survival with RT + PCV in codeleted patients: ~13–14 years.**
  > "In EORTC 26951, median survival was 3.5 years with PCV versus 2.6 years without PCV, with 1p/19q codeletion showing **14.2 years with PCV versus 9.3 years without**. In RTOG 9402, median survival was 4.8 years in both arms for the overall population, but with codeletion showed **13.2 years with PCV versus 7.3 years without**." — retrieved from the joint final report
  > "There was a **40% reduction in the risk of death** in both trials from adding PCV to RT in patients with 1p19q codeleted tumors… estimated PFS and OS probabilities at 20 years from random assignment of **30% and 35%**, respectively." — retrieved
  - Sources: **Cairncross et al., RTOG 9402 long-term, *JCO* 2013** ⚠ verify PMID; **van den Bent et al., EORTC 26951 long-term, *JCO* 2013** ⚠ verify PMID; **Lassman et al., "Joint Final Report of EORTC 26951 and RTOG 9402," *JCO* 2022** ⚠ verify PMID (**PMC9362869** ✅ retrieved).
- The 20-year survival figure is the one to lead with. **A third of these patients are alive 20 years after randomisation.** That reframes the whole entry: this is not primarily a survival problem, it's a *long-term-toxicity-and-function* problem.

**Mortality / morbidity**
- Deaths are overwhelmingly **disease-specific**, following malignant progression.
- The dominant morbidity in long survivors: **late neurocognitive decline** (radiotherapy-attributable in significant part), **chronic epilepsy**, endocrine dysfunction from hypothalamic-pituitary irradiation, secondary malignancy risk from alkylators and RT, and **PCV-specific toxicity** (myelosuppression, vincristine peripheral neuropathy, procarbazine intolerance) — PCV is a hard regimen and a substantial fraction of patients don't complete it.
- **Toxicity module conformance candidates:** `myelosuppression#Multilineage Peripheral Cytopenias` (PCV/temozolomide) and `peripheral_axonal_degeneration#Distal Axonal Degeneration and Demyelination` (vincristine). These are legitimately curatable and are exactly the "side effect as mechanism" pattern the toxicity modules exist for.

**Prognostic factors**
- **Favourable:** 1p/19q codeletion (the single strongest), IDH mutation, younger age, high KPS, grade 2 vs 3, greater extent of resection, frontal location, TERT promoter mutation (favourable *within* IDH-mutant gliomas ⚠ verify — this one is counterintuitive since TERT mutation is adverse in IDH-wildtype tumours, so cite carefully).
- **Adverse:** **CDKN2A/B homozygous deletion** ✅ **PMID:31832685**; **CIC mutation** (associated with unfavourable survival in codeleted tumours — retrieved summary, and loss of CIC/FUBP1 expression associated with shorter time to recurrence ✅ **PMID:24030748**); higher grade; older age; incomplete resection.
- Note the tidy irony: CIC mutation is near-defining of the entity *and* adverse within it. Both statements are true and the entry should carry both without smoothing them together.

---

## 12. Treatment

### The standard-of-care spine

**1. Maximal safe surgical resection**
First move for essentially everyone with accessible disease. Extent of resection correlates with outcome. Awake craniotomy with language/motor mapping is standard for eloquent-area tumours. Cure is not the goal; cytoreduction, tissue for diagnosis, and seizure control are.
- NCIT: **NCIT:C15329** Surgical Procedure, or a more specific craniotomy/tumour-resection term ⚠ look up. `therapeutic_modality: SURGERY`.

**2. Radiotherapy + PCV (the long-established regimen)**
For grade 3 disease, and for grade 2 disease with high-risk features (age >40, subtotal resection, symptomatic).
- **PCV = Procarbazine + Lomustine (CCNU) + Vincristine.** This is a **named regimen** and should use the `regimen_term` slot with the NCIT "PCV regimen" concept ⚠ look up under NCIT:C15697/C62634 reachability, plus `therapeutic_agent` entries for the three drugs (CHEBI: procarbazine ⚠, lomustine ⚠, vincristine ⚠ — verify each with `runoak -i sqlite:obo:chebi`).
- `treatment_term`: **NCIT:C15632** Chemotherapy. `therapeutic_modality: SMALL_MOLECULE`.
- Radiotherapy: **NCIT:C15313** Radiation Therapy, `therapeutic_modality: RADIOTHERAPY`. Typical dose 54 Gy (grade 2) to 59.4 Gy (grade 3) in 1.8–2 Gy fractions; see the **ESTRO-EANO 2024 target-delineation guideline** ⚠ verify PMID.
- Evidence: RTOG 9402 / EORTC 26951 as above. This is one of the best-evidenced treatment recommendations in all of neuro-oncology.

**3. Temozolomide — and an important negative**
Widely used as a gentler alternative to PCV, especially in frail patients or where PCV toxicity is prohibitive. **But the direct evidence does not support substituting TMZ monotherapy for radiotherapy:**
> "Progression-free survival (PFS) was significantly shorter in temozolomide-alone patients compared with RT patients (hazard ratio = 3.12; 95% CI: 1.26, 7.69; P = 0.014)." — CODEL trial initial design analysis, *Neuro-Oncology* 2021 ⚠ verify PMID
The accompanying editorial was titled "**Early results from the CODEL trial for anaplastic oligodendrogliomas: is temozolomide futile?**" ⚠ verify PMID — which tells you the field's mood. **Curate the RT-vs-TMZ comparison as a REFUTE/PARTIAL evidence item on the TMZ-monotherapy treatment**, not as a bland "TMZ is used." A well-curated negative result is worth more here than another affirmative.
- CHEBI: temozolomide **CHEBI:72564** (medium-high confidence ⚠).

**4. Vorasidenib — the era-defining new drug**
Oral, **brain-penetrant dual inhibitor of mutant IDH1 and IDH2**. This is the first therapy that attacks the founding lesion rather than the downstream mass.
- **INDIGO, phase 3, randomised, double-blind, placebo-controlled**, 331 patients with residual/recurrent grade 2 IDH-mutant glioma (astrocytoma or oligodendroglioma), no prior chemo/RT. Randomised 168 vorasidenib / 163 placebo.
  > "In patients with grade 2 IDH-mutant glioma, vorasidenib significantly prolonged progression-free survival and delayed time to next intervention with a predominantly low-grade safety profile." — **Mellinghoff et al., *NEJM* 2023** ✅ **PMID:37272516**
- **FDA approved August 2024** for grade 2 astrocytoma or oligodendroglioma with a susceptible IDH1/IDH2 mutation, **age 12 and older, following surgery**.
- **Secondary and exploratory endpoints published 2025** in *Lancet Oncology* ✅ **PMID:41175888** — worth fetching, as it covers seizure and quality-of-life outcomes, which is exactly the outcome domain that matters for this disease.
- Key toxicity: **transaminase elevation** (ALT/AST), requiring LFT monitoring — a `drug_induced_liver_injury` conformance candidate, though the injury here is generally mild/reversible so don't over-claim the full hepatocyte-death cascade.
- `therapeutic_modality: SMALL_MOLECULE`; `treatment_term`: **NCIT:C93352** Targeted Therapy or **NCIT:C15986** Pharmacotherapy; `therapeutic_agent`: NCIT vorasidenib concept ⚠ look up (CHEBI may not have it — per the repo's own memory, NCIT drug terms often fail `therapeutic_agent` validation, so **check whether CHEBI has a vorasidenib entry first and be ready to fall back to a free-text `preferred_term`**).
- **`target_mechanisms` pattern:** vorasidenib `INHIBITS` the **IDH neomorphic activity / D-2-HG production** node. That's a clean, evidence-bearing drug→mechanism edge and one of the best-justified in the whole entry.
- **Open question worth a `KNOWLEDGE_GAP`:** INDIGO enrolled grade 2 tumours only; benefit in grade 3, and overall-survival benefit at all (PFS was the primary endpoint, and this is a disease where median OS is over a decade — OS data will take many years), remain unproven. Also, patient selection is contested; see "Vorasidenib in IDH1/2-mutant low-grade glioma: the grey zone of patient's selection" (PMC10809174 ⚠).

**5. Antiseizure medication**
Not adjunctive trivia — for many patients this *is* the daily treatment. Levetiracetam is typical first-line (non-enzyme-inducing, so it doesn't perturb chemotherapy pharmacokinetics — an important interaction: enzyme-inducing ASMs like phenytoin and carbamazepine accelerate metabolism of several chemotherapeutics and should be avoided). Worth a curated treatment entry with `target_mechanisms` pointing at the epileptogenesis node.

**6. Supportive care**
Corticosteroids (dexamethasone) for peritumoral oedema — use sparingly given long survival and cumulative steroid toxicity. Neuro-rehabilitation, neuropsychology, driving/occupational counselling. **NCIT:C15747** Supportive Care.

### Investigational

- **Safusidenib** (mutant-IDH1-selective): phase 2 in treatment-naive grade 2 IDH1-mutant glioma reported **ORR 44.4%, clinical benefit rate 81.5%** per RANO-LGG (*Neuro-Oncology*, late 2025) ⚠ verify PMID; the **SIGMA** study has been amended into a **pivotal phase 3** — though the announced phase 3 focus is **IDH1-mutant astrocytoma**, so read carefully before asserting oligodendroglioma applicability.
- **Ivosidenib** (IDH1-selective, approved in AML/cholangiocarcinoma): perioperative phase 1 in low-grade glioma alongside vorasidenib ⚠ (PMC10803248 retrieved as an author-correction record — fetch the primary paper).
- **IDH1-R132H peptide vaccine (IDH1-vac / NOA-16).** Landmark concept: the mutation is a **public neoantigen** — one identical epitope shared across patients, which is about as close to an off-the-shelf cancer vaccine target as oncology gets.
  - **Platten et al., *Nature* 2021** ✅ **PMID:33762734** — first-in-human phase 1, 33 patients, safe and immunogenic.
  - **Final 8-year analysis published July 2026 in *Nature Cancer*** ⚠ verify PMID: 8-year PFS 0.42, OS 0.66; grade IV astrocytoma participants reached median OS 106.1 months. **Caveat that matters for this entry: NOA-16 enrolled IDH1-R132H+ *astrocytomas*, not oligodendrogliomas.** Curate as adjacent/investigational with the population explicitly stated — this is precisely the kind of claim a DR report will over-generalise.
  - **AMPLIFY-NEOVAC**: IDH1-vac + anti-PD-L1 combination, phase 1 ⚠ verify PMID (PMC9125855).
- **PARP inhibitors** exploiting IDH-mutant "BRCAness"; **CDK4/6 inhibitors** for CDKN2A-deleted tumours; **NAMPT/NAD+ pathway inhibitors**; **glutaminase inhibitors**; **checkpoint blockade** (disappointing so far, and §6 Node 11 explains why).

### Treatment strategy

- **Grade 2, young, gross-total resection, asymptomatic:** historically observation with serial MRI. Now genuinely in flux — vorasidenib is FDA-approved precisely for this post-surgical setting, and the 2025 ASCO-SNO guideline addresses when to apply it ⚠ verify the guideline citation.
- **Grade 2 with high-risk features, or grade 3:** RT + PCV remains the evidence-standard.
- **The core strategic tension** (state this explicitly in the entry, it's the clinical heart of the disease): with median survival past 13 years, **when** you deploy radiotherapy determines how much of a patient's remaining decades are spent with radiation-induced cognitive decline. Every treatment decision is a trade between tumour control now and brain function in 2040. IDH inhibitors are attractive largely because they offer a way to *defer* that bill.
- **Personalized medicine:** already fully genotype-driven — the diagnosis *is* a genotype, and IDH-inhibitor eligibility is a genotype. Resources: OncoKB, CIViC, My Cancer Genome.
- **Pharmacogenomics:** no strong glioma-specific PGx. **MGMT promoter methylation** is prognostic/predictive in glioblastoma; in IDH-mutant codeleted tumours MGMT methylation is near-universal (it travels with G-CIMP) and therefore **loses discriminatory value** — a common and citable misconception worth heading off in `notes`.

---

## 13. Prevention

Short section, and the honesty is the content.

- **Primary prevention: none exists.** No modifiable risk factor of established effect. The only actionable item is **avoiding unnecessary diagnostic/therapeutic cranial irradiation**, particularly in children — which is general radiation-protection practice, not oligodendroglioma prevention.
- **Secondary prevention / screening: not indicated.** Incidence far too low for population screening; no screening test exists; screening asymptomatic adults with MRI would produce overwhelming false-positive and incidentaloma harm.
- **Tertiary prevention** — this is where the real content is:
  - **Seizure prevention** with antiseizure medication (the highest-yield intervention for daily function).
  - **Surveillance MRI** on a defined schedule to catch progression while still treatable.
  - **Neurocognitive surveillance** and rehabilitation.
  - **Late-effects monitoring**: endocrine (pituitary axis post-RT), secondary malignancy, cerebrovascular disease post-RT.
  - Prophylactic ASM in patients who have *never* seized is **not** recommended — the evidence doesn't support it and the drugs have costs. A good curatable negative recommendation.
- **Immunization:** not applicable (no vaccine-preventable cause; the IDH1 vaccine is *therapeutic*, not preventive — don't let those two get conflated in the entry).
- **Genetic counselling:** not routine. rs55705857 carrier status is **not** clinically actionable and should not be tested for outside research. This deserves an explicit statement, because a 9-fold relative risk sounds alarming until you multiply it by a baseline incidence of 0.29/100,000.
- **Public health / environmental interventions:** none applicable.

---

## 14. Other Species / Natural Disease

Genuinely interesting, and better-supported than you'd expect.

- **Taxonomy:** *Canis lupus familiaris* (**NCBITaxon:9615** ⚠ verify) is the important one. Also reported in *Felis catus* (NCBITaxon:9685 ⚠), cattle, and horses, but dogs dominate.
- **Naturally occurring canine oligodendroglioma is a real and relatively common spontaneous tumour** — gliomas are among the commonest primary canine brain tumours, and oligodendroglioma is the most frequent glioma subtype in dogs.
- **Breed predisposition:** strongly enriched in **brachycephalic breeds** — Boxer, Boston Terrier, French Bulldog, English Bulldog. VBO has breed terms for all of these ⚠ look up. The brachycephalic skull conformation is a genuine, heritable predisposing factor, which makes dog glioma a natural experiment you cannot run in humans.
- **Comparative pathology and the crucial caveat:** canine gliomas are histologically convincing mimics — and the T2-FLAIR mismatch sign has even been validated as an imaging biomarker in dogs:
  > "The T2-FLAIR mismatch sign as an imaging biomarker for oligodendrogliomas in dogs" — *J Vet Intern Med* (PMC10365042 ✅ retrieved) ⚠ verify PMID.

  **But — and this is the load-bearing difference — canine gliomas are largely IDH-wildtype and do not carry the 1p/19q codeletion.** Dog and human genomes don't share the synteny that would make a 1p/19q codeletion meaningful, and IDH1 R132 mutations are rare in canine glioma. So the dog is an excellent model of *glioma biology, infiltration, and imaging*, and a **poor model of this specific molecular entity**. If you curate canine oligodendroglioma as an `animal_models:` entry, the honest link is `PARTIALLY_RECAPITULATES` at best, with `fidelity: LOW-MODERATE` and `limitations` spelling out the IDH/1p19q divergence.
- **Orthologous genes:** IDH1, IDH2, CIC, FUBP1, TERT are all conserved across mammals (NCBI Gene / Alliance of Genome Resources will give the orthologue IDs). Note that **mouse Tert promoter regulation differs substantially from human** — murine cells maintain telomerase far more readily, which is one reason TERT-promoter biology doesn't model well in mice.
- **Zoonotic potential:** none. Not transmissible. (The transmissible cancers — canine transmissible venereal tumour, Tasmanian devil facial tumour — are a different and unrelated phenomenon.)
- **Resource:** **OMIA** (Online Mendelian Inheritance in Animals) has canine glioma entries; the Canine Comparative Oncology and Genomics Consortium and NCI's Comparative Brain Tumor Consortium run dog glioma trials as parallel-track studies to human trials.

---

## 15. Model Organisms

Here is the uncomfortable truth, and it should be curated as a **`HUMAN_MODEL_MISMATCH` discussion**, not buried:

> **There is no faithful model of 1p/19q-codeleted oligodendroglioma.**

The reasons are structural, not for want of trying:
1. **The codeletion cannot be reproduced in mouse.** Human 1p and 19q genes are scattered across several mouse chromosomes — there is no syntenic block to delete. You could engineer *Cic* and *Fubp1* loss, but not the whole-arm dosage event, and it's plausible the dosage event matters beyond those two genes.
2. **Mutant IDH1 is growth-*suppressive* in most engineered systems.** Expressing IDH1-R132H in neural progenitors often reduces proliferation rather than driving tumours; whole-organism knock-in is frequently lethal or produces haemorrhage rather than glioma. There's even a formal claim that it acts as a tumour suppressor via DNA-damage-response upregulation (**Núñez et al., *Sci Transl Med* 2019** ⚠ verify PMID). The tumour needs the mutation, but the mutation alone doesn't build the tumour.
3. **Human oligodendroglioma cells are notoriously hard to culture.** They lose the codeletion or fail to establish. The field ran on essentially **two cell lines for a decade**: **BT054** and **BT088**, reported in "Oligodendroglioma cell lines containing t(1;19)(q10;p10)" ✅ **PMID:20388696** — and even these have been questioned for drift and for whether they retain the full genotype. Two lines is not a model system, it's a rumour.

**What actually exists:**

| Model | Type | What it captures | Limitations |
|---|---|---|---|
| **BT054, BT088** | Human cell lines with t(1;19)(q10;p10) ✅ PMID:20388696 | Genuine codeletion + IDH1 mutation | Very few lines; drift; slow growth; questioned authenticity — check **Cellosaurus** before use |
| **Diffusely infiltrative xenograft with FUBP1/CIC/IDH1 mutations** | PDX ⚠ (PMC3602110) | Infiltrative growth pattern *and* the right genotype | Single model; immunocompromised host removes the immune arm, which §6 Node 11 says is central |
| **IDH1-R132H + Tp53 + Atrx loss + NRAS-G12V GEMM** | Genetically engineered mouse ⚠ | IDH-mutant gliomagenesis | This is an **astrocytoma-genotype** model (TP53/ATRX). `FAILS_TO_RECAPITULATE` the oligodendroglioma lineage — a legitimate, citable negative link |
| **Cic conditional knockout mice** | GEMM | CIC→ETV derepression, NSC proliferation and lineage bias — retrieved: "Capicua regulates neural stem cell proliferation and lineage specification through control of Ets factors" ⚠ verify PMID (PMC6494820) | No codeletion, no IDH mutation; models one arm only |
| **Patient-derived organoids / hiPSC-derived neural models** | In vitro NAM | Human genetic background; tractable for CRISPR | Nascent for this entity; codeletion still not engineerable |
| **Mutant-IDH1 expression in astrocytes / NSCs** | In vitro | G-CIMP establishment (Turcan 2012 ⚠) | Not a tumour model — models the epigenetic step, which is exactly what it should be linked to |

**Curation guidance:** model the strong ones as `experimental_models:` (cell lines, organoids, iPSC — these are **not** `animal_models:`) and the mouse/dog ones as `animal_models:`, each with `modeled_mechanisms` linking to specific nodes. Use **`FAILS_TO_RECAPITULATE`** where honest — the astrocytoma-genotype GEMM against an oligodendroglioma-lineage node is a textbook case, and per repo policy that requires both `limitations` and `evidence`, which is fine because the literature says it plainly. The overall "no faithful model exists" claim belongs in a **`HUMAN_MODEL_MISMATCH` discussion** with a `prompt` phrased as a question and `proposed_experiments` (engineered syntenic dosage models; conditional Cic/Fubp1 loss on an Idh1-R132H background in an OPC-lineage driver; expanded PDX panels from the codeleted population).

**Databases:** MGI, IMPC, Alliance of Genome Resources, Cellosaurus (for BT054/BT088 provenance), DepMap (thin here), Jackson Labs PDX resources, and the NCI **Comparative Brain Tumor Consortium** for the canine track.

---

## Appendix A — Suggested dismech module conformance

Given the module inventory, this entry is a strong multi-hallmark conformer. Candidates, roughly ranked by how defensible each is:

| Module | Node | Confidence | Basis |
|---|---|---|---|
| `enabling_replicative_immortality` | `#Telomere Maintenance Reactivation` | **High** | TERT promoter mutation in ~98% of adult cases; textbook fit |
| `evading_growth_suppressors` | `#Loss of Cell-Cycle Checkpoint Control` | **Medium-high** | CDKN2A/B homozygous deletion — but only a minority of cases, so scope the node to the progression arm |
| `deregulated_cellular_energetics` | `#Aerobic Glycolysis (Warburg Effect)` | **Medium** | The metabolic rewiring here is IDH/2-HG-centred, which is *not* straightforwardly the Warburg pattern. Read the module before asserting; a forced fit here would be worse than none |
| `sustaining_proliferative_signaling` | `#Constitutive Mitogenic Pathway Activation` | **Medium-high** | CIC loss → ETV1/4/5 derepression → RAS-MAPK output; also PIK3CA |
| `epilepsy_excitation_inhibition_imbalance` | `#Excitation-Inhibition Imbalance` | **High** | The presenting phenotype in 60–90%; peritumoral glutamate/GABA mechanism is well described |
| `dna_repair_synthetic_lethality` | `#PARP and Platinum Synthetic Lethality` | **Medium** | IDH-mutant "BRCAness" is real but the therapeutic arm is investigational; and there's a contradicting DDR-*upregulation* claim. Curate as a hypothesis with both sides |
| `genome_instability_mutation` | `#Mutator Phenotype and Chromosomal Instability` | **Low-medium** | These tumours are actually relatively **genomically quiet** compared with glioblastoma. Don't reach |
| `myelosuppression` | `#Multilineage Peripheral Cytopenias` | **High** (for the PCV treatment arm) | Well-documented dose-limiting toxicity |
| `peripheral_axonal_degeneration` | `#Distal Axonal Degeneration and Demyelination` | **High** (vincristine arm) | Classic vincristine neuropathy |
| `immune_checkpoint_blockade` | — | **Do not conform** | The 2-HG immune-quiescence biology is a *contrast* to this module, not an instance of it. Worth an explicit note |
| `viral_oncogenesis` | — | **Do not conform** | Not a viral tumour |

## Appendix B — Suggested `mechanistic_hypotheses` and `discussions`

1. **Cell of origin** — OPC/NG2 glia vs. SVZ neural stem cell. Genuinely open; the single-cell hierarchy work constrains but doesn't settle it. Two hypothesis groups, both `EMERGING`/`ALTERNATIVE`.
2. **What 1p/19q codeletion actually does beyond CIC and FUBP1** — the two named genes don't obviously account for the whole-arm dosage effect or the tumour's distinctive biology. `KNOWLEDGE_GAP`.
3. **IDH1-R132H: oncogenic driver or partial tumour suppressor?** — Núñez 2019 vs. the mainstream driver model. Two competing curated hypotheses, not one flattened claim.
4. **`HUMAN_MODEL_MISMATCH`: no model reproduces the codeletion** — as detailed in §15. This is the cleanest, most necessary discussion item in the whole entry.
5. **Does IDH inhibition delay malignant transformation, or merely delay radiographic progression?** — INDIGO's endpoint was PFS; the disease's median survival is >13 years. `KNOWLEDGE_GAP` with a stated experimental resolution (long-term follow-up, OS analysis).
6. **Teenage-onset codeleted oligodendroglioma lacking TERT mutation** — a possible distinct biological subgroup. Could be `has_subtypes` or a `KNOWLEDGE_GAP` depending on how strong the source turns out to be.

## Appendix C — First moves when you start curating

```bash
# 1. NEC preflight on any DR report (expect SKIP — this is somatic; do the manual read)
just preflight-dr research/<report>.md MONDO:XXXXXXX

# 2. Fetch every PMID before writing a single evidence block
just fetch-reference PMID:37272516   # INDIGO NEJM
just fetch-reference PMID:41175888   # INDIGO secondary endpoints
just fetch-reference PMID:21817013   # Bettegowda CIC/FUBP1
just fetch-reference PMID:22072542   # Yip CIC/IDH/1p19q
just fetch-reference PMID:24030748   # Chan CIC/FUBP1 prognosis
just fetch-reference PMID:27806376   # Tirosh single-cell
just fetch-reference PMID:41092086   # CBTRUS 2018-2022
just fetch-reference PMID:31832685   # Appay CDKN2A
just fetch-reference PMID:17021403   # Jenkins der(1;19)
just fetch-reference PMID:20388696   # BT054/BT088 cell lines
just fetch-reference PMID:33762734   # Platten IDH1 vaccine

# 3. Verify EVERY ontology term before it lands
just validate-terms kb/disorders/<Slug>.yaml

# 4. Fast snippet check after each edit (seconds, offline)
just count-verified-snippets kb/disorders/<Slug>.yaml

# 5. Once, before the PR — the batched sweep CI runs
just validate-disorders kb/disorders/<Slug>.yaml
```

Two things I'd watch for specifically in this entry: **titles-as-snippets** (a lot of the landmark papers here have result-stating titles, which is tempting and mostly still wrong — quote the abstract's own sentence), and **cohort blending** (any figure drawn from "anaplastic oligodendroglioma" or "low-grade glioma" literature needs its codeletion-status denominator checked before it becomes a frequency band).

---

## Sources

- [CBTRUS Statistical Report: Primary Brain and Other CNS Tumors Diagnosed in the US 2018–2022 (PubMed)](https://pubmed.ncbi.nlm.nih.gov/41092086/) — PMID:41092086
- [CBTRUS Statistical Report 2018–2022 (Neuro-Oncology)](https://academic.oup.com/neuro-oncology/article/27/Supplement_4/iv1/8285946)
- [Vorasidenib in IDH1- or IDH2-Mutant Low-Grade Glioma (INDIGO, NEJM 2023)](https://pubmed.ncbi.nlm.nih.gov/37272516/) — PMID:37272516
- [INDIGO secondary and exploratory endpoints (Lancet Oncology 2025)](https://pubmed.ncbi.nlm.nih.gov/41175888/) — PMID:41175888
- [Mutations in CIC and FUBP1 Contribute to Human Oligodendroglioma (Science 2011)](https://pubmed.ncbi.nlm.nih.gov/21817013/) — PMID:21817013
- [Concurrent CIC mutations, IDH mutations, and 1p/19q loss distinguish oligodendrogliomas from other cancers](https://pubmed.ncbi.nlm.nih.gov/22072542/) — PMID:22072542
- [Loss of CIC and FUBP1 expressions are potential markers of shorter time to recurrence](https://pubmed.ncbi.nlm.nih.gov/24030748/) — PMID:24030748
- [Regulation and function of capicua in mammals (Exp Mol Med 2020)](https://www.nature.com/articles/s12276-020-0411-3)
- [Capicua regulates neural stem cell proliferation and lineage specification through control of Ets factors](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6494820/)
- [Identification of der(1;19)(q10;p10) in five oligodendrogliomas (JNEN 2006)](https://pubmed.ncbi.nlm.nih.gov/17021403/) — PMID:17021403
- [Oligodendroglioma cell lines containing t(1;19)(q10;p10) (Neuro-Oncology 2010)](https://pubmed.ncbi.nlm.nih.gov/20388696/) — PMID:20388696
- [Single-cell RNA-seq supports a developmental hierarchy in human oligodendroglioma (Nature 2016)](https://pubmed.ncbi.nlm.nih.gov/27806376/) — PMID:27806376
- [Oligodendroglioma intra-tumor heterogeneity — Single Cell Portal SCP12](https://singlecell.broadinstitute.org/single_cell/study/SCP12/oligodendroglioma-intra-tumor-heterogeneity)
- [Oncometabolite 2-Hydroxyglutarate Is a Competitive Inhibitor of α-Ketoglutarate-Dependent Dioxygenases (Cancer Cell)](https://www.cell.com/cancer-cell/fulltext/S1535-6108(10)00527-1)
- [D-2-Hydroxyglutarate in Glioma Biology (review)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8464856/)
- [(R)-2-hydroxyglutarate drives immune quiescence in the tumor microenvironment of IDH-mutant gliomas](https://pmc.ncbi.nlm.nih.gov/articles/PMC6448779/)
- [Joint Final Report of EORTC 26951 and RTOG 9402 (JCO 2022)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9362869/)
- [Phase III Trial of Chemoradiotherapy for Anaplastic Oligodendroglioma: Long-Term Results of RTOG 9402 (JCO)](https://ascopubs.org/doi/10.1200/JCO.2012.43.2674)
- [Long-Term Survival in a Significant Proportion of Patients with 1p/19q Codeleted Anaplastic Oligodendroglioma (ESMO)](https://www.esmo.org/oncology-news/long-term-survival-in-a-significant-proportion-of-patients-with-a-1p-19q-codeleted-anaplastic-oligodendroglioma)
- [CODEL: phase III study of RT, RT+TMZ, or TMZ for newly diagnosed 1p/19q codeleted oligodendroglioma](https://academic.oup.com/neuro-oncology/article/23/3/457/5873253)
- [Early results from the CODEL trial: is temozolomide futile?](https://pubmed.ncbi.nlm.nih.gov/33560350/)
- [CDKN2A homozygous deletion is a strong adverse prognosis factor in diffuse malignant IDH-mutant gliomas](https://pubmed.ncbi.nlm.nih.gov/31832685/) — PMID:31832685
- [Oligodendrogliomas arising during teenage years often lack TERT promoter mutation](https://pmc.ncbi.nlm.nih.gov/articles/PMC6145350/)
- [TERT promoter mutation confers favorable prognosis regardless of 1p/19q status in IDH1/2-mutant gliomas](https://pubmed.ncbi.nlm.nih.gov/33228806/)
- [Glioma Groups Based on 1p/19q, IDH, and TERT Promoter Mutations in Tumors (NEJM 2015)](https://www.nejm.org/doi/full/10.1056/NEJMoa1407279)
- [Deciphering gliomagenesis from genome-wide association studies (Neuro-Oncology 2023)](https://academic.oup.com/neuro-oncology/article/25/7/1366/7076931)
- [A noncoding single-nucleotide polymorphism at 8q24 drives IDH1-mutant glioma formation (Science 2022)](https://www.science.org/doi/10.1126/science.abj2890)
- [Australian GWAS confirms higher female risk for adult glioma associated with CCDC26 variants](https://academic.oup.com/neuro-oncology/article/25/7/1355/6948143)
- [IDH1-R132H acts as a tumor suppressor in glioma via epigenetic up-regulation of the DNA damage response (Sci Transl Med)](https://www.science.org/doi/10.1126/scitranslmed.aaq1427)
- [A vaccine targeting mutant IDH1 in newly diagnosed glioma (Nature 2021)](https://pubmed.ncbi.nlm.nih.gov/33762734/) — PMID:33762734
- [IDH1-mutant vaccine in newly diagnosed astrocytoma: final analysis of NOA16 (Nature Cancer 2026)](https://www.nature.com/articles/s43018-026-01199-y)
- [Phase 3 SIGMA Trial of Safusidenib Initiated for IDH1-Mutant Glioma](https://www.targetedonc.com/view/phase-3-sigma-trial-of-safusidenib-initiated-for-idh1-mutant-glioma)
- [A perioperative study of safusidenib in patients with IDH1-mutated glioma](https://pmc.ncbi.nlm.nih.gov/articles/PMC11534100/)
- [AMPLIFY-NEOVAC trial protocol](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9125855/)
- [EANO guidelines on the diagnosis and treatment of diffuse gliomas of adulthood](https://pubmed.ncbi.nlm.nih.gov/33293629/)
- [ESTRO-EANO guideline on target delineation and radiotherapy for IDH-mutant WHO CNS grade 2 and 3 diffuse glioma](https://www.thegreenjournal.com/article/S0167-8140(24)03572-2/fulltext)
- [Diffuse Astrocytic and Oligodendroglial Tumors, Therapy: ASCO-SNO 2025 Guideline Summary](https://reference.medscape.com/cc2/p10/asco-sno-guideline-astrocytic-oligodendroglial-tumors-2026a1000o0r)
- [Updates on the WHO diagnosis of IDH-mutant glioma (J Neurooncol)](https://link.springer.com/article/10.1007/s11060-023-04250-5)
- [Oligodendrogliomas: classifying the same cohort using pre- and post-WHO 2021 criteria (Brain Communications 2025)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12314594/)
- [Pathology Outlines — Oligodendroglioma, IDH mutant and 1p/19q codeleted](https://www.pathologyoutlines.com/topic/cnstumoroligodendrogliomaidhmutant.html)
- [MRI Features Can Predict 1p/19q Status in Intracranial Gliomas (AJNR)](https://www.ajnr.org/content/39/4/687)
- [Imaging of oligodendroglioma (Br J Radiol)](https://academic.oup.com/bjr/article/89/1060/20150857/7445743)
- [The T2-FLAIR mismatch sign as an imaging biomarker for oligodendrogliomas in dogs](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10365042/)
- [A novel, diffusely infiltrative xenograft model of human anaplastic oligodendroglioma with FUBP1, CIC, and IDH1 mutations](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3602110/)
- [Current and Future Frontiers of Molecularly Defined Oligodendrogliomas](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9358027/)
- [Vorasidenib in IDH1/2-mutant low-grade glioma: the grey zone of patient's selection](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10809174/)
- [MR Spectroscopy for Detection of 2-Hydroxyglutarate as a Biomarker for IDH Mutation in Gliomas](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5488000/)
- [ICCR dataset — Chromosomal arm 1p/19q codeletion](https://www.iccr-cancer.org/datasets/docs/iccr-cns-mole-1p19q/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 35 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 16 |
| Quoted claims checked | 0 |
| Quoted claims found in source | 0 |
| Quoted claims with nothing to check against | 1 |

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `PMC:PMC10809174`: "Vorasidenib in IDH1/2-mutant low-grade glioma: the grey zone of patient's selection"
  - The PMC ID service was unreachable, so the quote was not checked

19 of 35 references resolved; the rest could not be looked up either way.