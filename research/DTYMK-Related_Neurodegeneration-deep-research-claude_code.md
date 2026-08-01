---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-01T13:56:55.440690'
end_time: '2026-08-01T14:12:23.437936'
duration_seconds: 928.0
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: DTYMK-Related Neurodegeneration
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
  web_search_requests: 5
  num_turns: 61
  total_cost_usd: 4.58695425
  session_id: a0311977-6dc8-4876-94a4-530016f2b6da
  stop_reason: end_turn
citation_count: 21
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** DTYMK-Related Neurodegeneration
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **DTYMK-Related Neurodegeneration** covering all of the
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

# DTYMK-Related Neurodegeneration — Comprehensive Research Report

**Preferred disease name:** Childhood-onset neurodegeneration with progressive microcephaly (CONPM)
**Target MONDO ID:** `MONDO:0859241`
**Category:** Mendelian, autosomal recessive, ultra-rare (≤5 reported patients worldwide as of 2025)
**Report date:** 2026-08-01

---

## ⚠️ Curation Preflight Warnings (read before using this report)

**1. Named-Entity / topic confusion risk is HIGH for this gene.** A PubMed query for `DTYMK` returns ~58 records, of which **the large majority are cancer-bioinformatics papers** (hepatocellular carcinoma prognostic signatures, lung adenocarcinoma pan-cancer analyses, uveal melanoma, colorectal cancer). Only **five** primary records concern the human neurodegenerative disease. A deep-research tool asked about "DTYMK" will very plausibly return a coherent, well-cited, snippet-validating report about **DTYMK as an oncology biomarker** rather than about CONPM. Per the repo NEC preflight (CLAUDE.md §2b), the identity anchors for this entry are: gene **DTYMK / HGNC:3061 / OMIM \*188345**, phenotype **OMIM #619847**, locus **2q37.3**. Any report whose dominant subject is tumor prognosis is off-target.

**2. Second NEC-adjacent risk:** the first clinical report (Lam et al. 2019, PMID:31271740) framed DTYMK as a **mitochondrial DNA depletion syndrome (MDDS)** gene, not as a nuclear-genome-instability disorder. The two framings coexist in the literature and are *not* the same mechanistic claim. Do not blend them into a single unqualified causal chain — see §6.

**3. Quote provenance.** Abstract text reproduced below under "verbatim abstract" was fetched from NCBI E-utilities and is quotable. Sentences marked **[full-text]** were extracted from PMC full text by an intermediate summarizer and **must be re-verified against the source before being used as an evidence `snippet:`** — they are reported here as leads, not as validated quotes.

**4. Ontology IDs** suggested throughout are candidates. Every one must be verified with `just validate-terms` / OAK before commit.

---

## 1. Disease Information

### Overview

CONPM is an ultra-rare autosomal recessive neurometabolic/neurodegenerative disorder caused by biallelic loss-of-function variants in *DTYMK*, which encodes deoxythymidylate kinase (thymidylate kinase, TMPK; EC 2.7.4.9). TMPK catalyses the **penultimate step of dTTP biosynthesis** (dTMP → dTDP). Because both the *de novo* (thymidylate synthase) and the *salvage* (thymidine kinase) routes to dTTP converge on dTMP **upstream** of TMPK, loss of TMPK constitutes a complete block of the canonical dTTP supply — a fact the discovery paper explicitly calls remarkable given that affected children are born alive.

Clinically the disorder presents as **congenital-to-infantile onset, severe and progressive (postnatal-worsening) microcephaly, profound global developmental delay or frank developmental regression, early-onset seizures, spasticity with pyramidal signs, cortical blindness/absent visual tracking, feeding failure, and death in early childhood** in the severe form, with a milder end of the spectrum (small head circumference, severe intellectual disability, hypotonia, poor speech, motor delay) documented in the sibling pair reported by Lam et al.

The neuroimaging signature is distinctive: **profound generalized cerebral atrophy with severe ventricular and subarachnoid space enlargement, shrinkage/"disappearance" of the basal ganglia, and relative sparing of brainstem and cerebellum.**

### Key identifiers

| Resource | Identifier | Notes |
|---|---|---|
| OMIM (phenotype) | **#619847** — NEURODEGENERATION, CHILDHOOD-ONSET, WITH PROGRESSIVE MICROCEPHALY; CONPM | |
| OMIM (gene) | **\*188345** — DEOXYTHYMIDYLATE KINASE; DTYMK | 2q37.3 |
| MONDO | **MONDO:0859241** | Label: "Neurodegeneration, childhood-onset, with progressive microcephaly"; xrefs GARD:0027309, MEDGEN:1801540, OMIM:619847, UMLS:C5676972. **No definition and no synonyms in MONDO** — a curation gap worth noting. |
| MedGen | UID 1801540 / CUI **C5676972** | |
| GARD | 0027309 | |
| UMLS | C5676972 | |
| Orphanet | **No dedicated ORPHA code identified.** Searches of Orphanet and of the local dismech Orphanet cache (`references_cache/ORPHA_*.md`) returned no DTYMK/CONPM entry. Treat Orphanet epidemiology as unavailable rather than substituting a near-miss ORPHA code. |
| ICD-10 | No specific code. In practice coded under **G31.8/G31.9** (other/unspecified degenerative disease of nervous system) with **Q02** (microcephaly) and **G40.x** (epilepsy) as needed. *Approximate — verify against local coding practice before asserting.* |
| ICD-11 | No specific code identified. Nearest foundation concepts are the hereditary degenerative CNS disease and microcephaly stems. *Not verified; do not assert a specific code.* |
| MeSH | No dedicated descriptor. Indexed via *Microcephaly* (D008831), *Neurodegenerative Diseases* (D019636), *Nucleoside-Phosphate Kinase* / thymidylate kinase concepts. |

### Synonyms and alternative names

- Childhood-onset neurodegeneration with progressive microcephaly (**CONPM**) — OMIM/MONDO preferred
- DTYMK-related neurodegeneration
- DTYMK deficiency; thymidylate kinase (TMPK) deficiency; dTMP kinase deficiency
- Deoxythymidylate kinase deficiency
- *DTYMK*-related mitochondrial DNA depletion syndrome (Lam et al. framing; **not** an OMIM-recognized MDDS numbered subtype)

### Provenance of information

**Aggregated disease-level resources plus individual-patient case reports.** There is no registry, no natural-history cohort, and no EHR-derived data for this disorder. All human phenotype information derives from **five individually described patients in three publications**. HPO annotations for OMIM:619847 are denominator-annotated over n=2 or n=4 individuals (see §3), which is itself a useful signal that all "frequencies" are case-count fractions, not population estimates.

---

## 2. Etiology

### Disease causal factors

**Purely genetic (monogenic, autosomal recessive).** Biallelic loss-of-function variants in *DTYMK* (HGNC:3061). No environmental, infectious, or acquired etiology is known or postulated. No somatic mechanism in this disease (somatic *DTYMK* dysregulation is an oncology topic — see §12 note — and is mechanistically unrelated).

**Primary quote (verbatim abstract, PMID:34918187):**
> "Here, we describe two unrelated children with bi-allelic variants in DTYMK, encoding dTMPK, which catalyzes the penultimate step in dTTP biosynthesis."
> "In summary, by combining genetic and biochemical approaches in multiple models we identified loss-of-function of DTYMK as the cause of a severe postnatal neurodegenerative disease and highlight the essential nature of dTTP synthesis in the maintenance of genome stability and neuronal survival."

### Genetic risk factors

- **Causal variants:** biallelic (homozygous or compound heterozygous) *DTYMK* variants — see §4.
- **Consanguinity** is a documented risk contributor: Individual II of Vanoevelen et al. was born to consanguineous Egyptian parents and was homozygous for p.Pro81Leu **[full-text]**. The 2025 Mexican case was likewise homozygous for p.Pro81Leu (PMID:40696808).
- **Carrier status:** heterozygous carriers are unaffected. Mouse data support this directly — heterozygous *Dtymk* mice show ~3-fold reduced expression with **no** neural tube defects (PMID:38621447).
- **No susceptibility loci, GWAS signals, or modifier genes** have been reported. GWAS Catalog / PheGenI contain nothing relevant to CONPM.

### Environmental risk factors

**None identified.** No toxin, exposure, lifestyle, occupational, maternal, or seasonal factor has been implicated. Age, sex, and parity are not risk factors (see §9 for the sex distribution caveat: n is too small to interpret).

One negative environmental experiment is informative: Tiani & Stover fed heterozygous *Dtymk* dams **three different diets** (folate-manipulated) and found no diet-dependent increase in neural tube defect risk in het offspring (PMID:38621447) — i.e., no demonstrated folate/one-carbon dietary modifier of *Dtymk* haploinsufficiency in mouse.

### Protective factors

**None identified.** No protective allele, modifier, dietary, or lifestyle factor is documented.

However, there is one striking **endogenous compensatory phenomenon** that functions like a protective mechanism at the cellular level and is arguably the central unresolved question of this disease: **non-neural tissues appear to be substantially spared, and patient fibroblasts proliferate normally despite undetectable TMPK activity.** This is discussed as a mechanism/knowledge-gap in §6 rather than a protective factor, because the responsible enzyme is unidentified.

**Verbatim abstract (PMID:34926941, ACS Omega 2021):**
> "In conclusion, TMPK mutations identified in patients represent loss of function mutations but surprisingly the proliferation rate of the patient-derived fibroblasts was normal, suggesting the existence of an alternative and hitherto unknown compensatory TMPK-like enzyme for dTTP synthesis."

**Verbatim abstract (PMID:34994281, Nucleosides Nucleotides Nucleic Acids 2022):**
> "Deficiency in TMPK activity due to genetic alterations of *DTYMK*, i.e., the gene coding for TMPK, causes severe microcephaly in humans. However, no defects were observed in other tissues, suggesting the existence of a compensatory enzyme for dTTP synthesis."
> "…because of its low activity, isoform 6 is unlikely be able to compensate for the loss of TMPK activity caused by deletions and/or point mutations of the *DTYMK* gene."

### Gene–environment interactions

**None documented.** CTD, PheGenI, and the primary literature contain no GxE evidence for *DTYMK*/CONPM. Theoretically plausible but untested interactions worth flagging as knowledge gaps: (i) thymidine/deoxynucleoside availability (relevant to the NCT04802707 trial, §12); (ii) antifolate or nucleoside-analogue drug exposure in carriers, given that the pathway is the target of 5-FU/methotrexate-class agents; (iii) genotoxic exposure (UV/ionizing radiation) given the demonstrated DNA-damage-response defect. **None of these are supported by data — do not curate as evidence-backed.**

---

## 3. Phenotypes

### 3.1 HPO annotations for OMIM:619847 (authoritative, with case-count frequencies)

Retrieved from the HPO annotation API (`ontology.jax.org/api/network/annotation/OMIM:619847`). **Frequencies are n-of-N counts over the reported cases, not population frequencies.** Denominators of 4 indicate annotation across both clinical reports (Vanoevelen n=2 + Lam n=2); denominators of 2 indicate a single report.

| HP ID | Phenotype | Count | Suggested dismech FrequencyEnum |
|---|---|---|---|
| **HP:0001263** | Global developmental delay | **4/4** | OBLIGATE / VERY_FREQUENT |
| **HP:0002059** | Cerebral atrophy | **3/4** | VERY_FREQUENT |
| **HP:0011451** | Primary microcephaly | 2/2 | VERY_FREQUENT |
| HP:0000252 | Microcephaly | 1/2 | (redundant with above; prefer HP:0011451 + progressive qualifier) |
| **HP:0001252** | Hypotonia | 2/2 | VERY_FREQUENT |
| **HP:0012704** | Widened subarachnoid space | 2/2 | VERY_FREQUENT |
| **HP:0003593** | Infantile onset | 2/2 | — (onset, not phenotype) |
| **HP:0003577** | Congenital onset | 2/2 | — (onset) |
| **HP:0003819** | Death in childhood | 2/2 | VERY_FREQUENT |
| **HP:0002151** | Increased circulating lactate | 2/2 | VERY_FREQUENT |
| **HP:0000028** | Cryptorchidism | 2/4 | FREQUENT (males only) |
| HP:0001249 | Intellectual disability | 1/1 | (only assessable in survivors) |
| HP:0001250 | Seizure | 1/2 | FREQUENT |
| HP:0002133 | Status epilepticus | 1/2 | FREQUENT |
| HP:0002373 | Febrile seizure (3 mo–6 y) | 1/2 | FREQUENT |
| HP:0001336 | Myoclonus | 1/2 | FREQUENT |
| HP:0002376 | Developmental regression | 1/2 | FREQUENT |
| HP:0001257 | Spasticity | 1/2 | FREQUENT |
| HP:0002510 | Spastic tetraplegia | 1/2 | FREQUENT |
| HP:0001276 | Hypertonia | 1/2 | FREQUENT |
| HP:0002179 | Opisthotonus | 1/2 | FREQUENT |
| HP:0001347 | Hyperreflexia | 1/2 | FREQUENT |
| HP:0002169 | Clonus | 1/2 | FREQUENT |
| HP:0003487 | Babinski sign | 1/2 | FREQUENT |
| HP:0002451 | Limb dystonia | 1/2 | FREQUENT |
| HP:0100021 | Cerebral palsy | 1/2 | FREQUENT |
| HP:0002171 | Gliosis | 1/2 | FREQUENT (neuropathology) |
| HP:0006956 | Lateral ventricle dilatation | 1/2 | FREQUENT |
| HP:0100704 | Cerebral visual impairment | 1/2 | FREQUENT |
| HP:0000407 | Sensorineural hearing impairment | 1/2 | FREQUENT |
| HP:0011968 | Feeding difficulties | 1/2 | FREQUENT |
| HP:0033454 | Tube feeding | 1/2 | FREQUENT |
| HP:0002015 | Dysphagia | 1/2 | FREQUENT |
| HP:0001601 | Laryngomalacia | 1/2 | FREQUENT |
| HP:0002878 | Respiratory failure | 1/2 | FREQUENT |
| HP:0004322 | Short stature | 1/2 | FREQUENT |
| HP:0001518 | Small for gestational age | 1/2 | FREQUENT |
| HP:0003348 | Hyperalaninemia | 1/2 | FREQUENT |
| HP:0000054 | Micropenis | 1/2 | FREQUENT (males) |
| HP:0000341 | Narrow forehead | 1/2 | FREQUENT |
| HP:0000293 | Full cheeks | 1/2 | FREQUENT |
| HP:0001561 | Polyhydramnios | 1/2 | FREQUENT (prenatal) |
| HP:0001623 | Breech presentation | 1/2 | FREQUENT (prenatal) |
| **HP:0000007** | Autosomal recessive inheritance | — | inheritance slot |

**Phenotypes documented in the literature but NOT in the current HPO annotation set** (candidate HPO-annotation gaps worth flagging upstream):

| Phenotype | Suggested HP term | Source |
|---|---|---|
| Basal ganglia atrophy / "disappearance of the basal ganglia" | **HP:0006979** (Abnormal basal ganglia morphology) or HP:0002135 (Abnormality of the basal ganglia) — *the specific "basal ganglia atrophy" concept should be verified with OAK* | PMID:34918187 abstract, verbatim: "Brain imaging revealed severe cerebral atrophy and disappearance of the basal ganglia." |
| Absent visual tracking / no eye contact | HP:0000618 (Blindness) or HP:0007843? — prefer **HP:0100704** (cerebral visual impairment, already annotated) | PMID:34918187 **[full-text]** |
| Cerebellar atrophy | HP:0001272 | PMID:40696808 (Mexican case reports "cortical and cerebellar atrophy" — **note this CONTRADICTS the cerebellar sparing in Vanoevelen; see §7 discrepancy note**) |
| Microcytic hypochromic anemia | HP:0004840 (verify) | PMID:34918187 **[full-text]**, Individual II |
| Elevated hepatic transaminases | HP:0002910 | PMID:34918187 **[full-text]**, Individual II |
| Failure to thrive / growth retardation | HP:0001508 | PMID:34918187 abstract: "severe microcephaly and growth retardation with minimal neurodevelopment" |
| Epilepsy (as distinct from single seizures) | HP:0001250 with `temporality: RECURRENT` | PMID:40696808 |
| Absent speech | HP:0001344 | Lam et al. milder sibling phenotype (per OMIM summary) |

### 3.2 Phenotype characteristics by domain

**Neurodevelopmental / cognitive**
- **Type:** clinical sign + developmental
- **Onset:** congenital to infantile (HP:0003577 2/2; HP:0003593 2/2). Feeding problems from **day 3 of life** in Individual I **[full-text]**.
- **Severity:** severe to profound in the Vanoevelen/Hernández-Carreto cases (essentially **no milestones achieved**); moderate-severe intellectual disability with poor speech in the Lam siblings.
- **Progression:** **progressive with frank regression** — this is the defining feature separating CONPM from static primary microcephaly. Individual I was hypotonic at birth then "developed spasticity with opisthotonus within 1 year of age" **[full-text]**.
- **QoL:** catastrophic. Total dependence for all activities of daily living; no communication; tube feeding; recurrent aspiration/respiratory illness. No formal QoL instrument (EQ-5D, PROMIS, PedsQL) has been applied — a genuine data gap.

**Microcephaly**
- **Type:** physical manifestation / clinical sign
- **Onset:** **congenital but predominantly postnatal-progressive.** Individual I had OFC 31 cm at birth (2nd centile — i.e., borderline, not markedly microcephalic) and reached **−7.6 SD by 9 months**; Individual II reached **−7.4 SD by 26 months** **[full-text]**. This trajectory (near-normal at birth → extreme by 1–2 years) is the single most curation-relevant temporal detail and should drive a `clinical_course: PROGRESSIVE` qualifier.
- **Severity:** extreme (−7 SD or worse).
- **Frequency:** 2/2 in the severe cases; small head circumference in the milder siblings.

**Seizures / epilepsy**
- **Type:** clinical sign
- **Onset:** 6 months (febrile seizures, Individual I); 15 months (myoclonic jerks, Individual II) **[full-text]**; epilepsy present in the 2-year-old Mexican case (PMID:40696808).
- **Semiology:** febrile seizures, myoclonic jerks, status epilepticus.
- **EEG:** Individual I had a **flat-trace EEG** treated with phenobarbital **[full-text]** — consistent with profound cortical loss rather than a primary channelopathy.
- **Progression:** progressive; drug response poor.

**Motor / tone**
- Biphasic pattern: **neonatal hypotonia → evolving spastic hypertonia** with hyperreflexia, clonus, extensor plantar responses, spastic tetraplegia, opisthotonus, limb dystonia. Individual II retained "good control of the head" while having increased distal tone, bilateral clonus, and positive Babinski signs **[full-text]**.

**Visual**
- Absent visual tracking/eye contact from the first months; annotated as cerebral (cortical) visual impairment (HP:0100704). "No eye contact was ever made" (Individual I) **[full-text]**.

**Growth / feeding**
- SGA (1/2), short stature (1/2), poor feeding from the neonatal period requiring nasogastric tube, dysphagia, laryngomalacia. Individual II birth weight 2250 g (−1.8 SD) **[full-text]**.

**Laboratory abnormalities** — important because they are the metabolic-workup handles
- **Increased circulating lactate (HP:0002151) — 2/2.** LOINC: 2524-7 (Lactate [Moles/volume] in Serum or Plasma), 32693-4 (Lactate, blood); CSF lactate LOINC 2519-7.
- **Hyperalaninemia (HP:0003348) — 1/2.** LOINC 26603-3 (Alanine [Moles/volume] in Plasma). The lactate+alanine pattern is the classic mitochondrial-disease screen and explains why the Lam siblings were worked up as MDDS.
- Microcytic hypochromic anemia and elevated liver enzymes (Individual II) **[full-text]**.
- **Fibroblast dTMPK enzyme activity** — the diagnostic functional assay (see §10).

**Urogenital**
- Cryptorchidism 2/4, micropenis 1/2 — notable as the only consistent extra-CNS *structural* finding, and worth flagging mechanistically since gonadal/germline tissue is highly proliferative.

**Neuropathology**
- Gliosis (HP:0002171). "Pathology in individual I confirms massive neuronal dropout, only sparing the dentate nucleus and brain stem." **[full-text]**

---

## 4. Genetic / Molecular Information

### Gene

| Field | Value |
|---|---|
| Symbol | **DTYMK** |
| HGNC | **HGNC:3061** → dismech CURIE form **`hgnc:3061`** (lowercase per repo convention) |
| Approved name | deoxythymidylate kinase |
| Previous symbols | CDC8, TYMK, TMPK |
| Aliases | dTMP kinase, thymidylate (dTMP) kinase |
| Locus | **2q37.3** |
| NCBI Gene | 1841 |
| Ensembl | ENSG00000168393 |
| RefSeq transcript | **NM_012145.4** (isoform 1, the characterized functional enzyme) |
| UniProt | **P23919** (thymidylate kinase / dTMP kinase), 212 aa |
| EC | **2.7.4.9** |
| OMIM gene | \*188345 |

**Protein:** 212-aa homodimeric P-loop kinase of the thymidylate kinase family. Reaction: **dTMP + ATP → dTDP + ADP** (Mg²⁺-dependent). Localizes to **cytosol, nucleus, and mitochondrion** (UniProt P23919). Human Protein Atlas reports **low tissue specificity** (tau 0.29), detected in all tissues, assigned to the "Bone marrow – Nuclear processes" expression cluster, with HPA IF subcellular localization to mitochondria and moderate, non-distinctive expression across brain regions. **Curation note:** the absence of brain-enriched expression means the brain-restricted phenotype is *not* explained by expression pattern — it must be explained by the proliferative/repair demands of neurodevelopment plus the postmitotic vulnerability of neurons.

### Reported pathogenic variants (all germline; ClinVar-verified)

| cDNA (NM_012145.4) | Protein | Type | ClinVar VCV | Classification | Review status | Population AF |
|---|---|---|---|---|---|---|
| **c.242C>T** | **p.Pro81Leu** | missense | VCV001686905 | Likely pathogenic | criteria provided, single submitter | gnomAD 0.00001 |
| **c.382G>A** | **p.Asp128Asn** | missense | VCV001686904 | Pathogenic | no assertion criteria provided | gnomAD 0.00002; ExAC 0.00002; TOPMed 0.00001; ESP 0.00008; 1000G 0.00020 |
| **c.295G>A** | **p.Ala99Thr** | missense | VCV001686903 | Pathogenic | no assertion criteria provided | gnomAD 0.00003; gnomAD exomes 0.00001; TOPMed 0.00003 |
| **c.287_320del** | **p.Asp96fs** | frameshift deletion (34 bp) | VCV001686902 | Pathogenic | no assertion criteria provided | not reported |
| c.265_270del | p.Gln89_Gly90del | in-frame deletion | VCV004277573 | Likely pathogenic | criteria provided, single submitter | not reported |
| c.239+1045_239+1050del | (deep intronic) | deletion | VCV003065236 | VUS / VUS-high | criteria provided, multiple submitters, no conflicts | not reported |

**Genotype assignments by patient:**

| Patient | Ancestry | Genotype | Source |
|---|---|---|---|
| Individual I (F) | Dutch, non-consanguineous | **compound heterozygous** c.242C>T (p.Pro81Leu, paternal) / c.382G>A (p.Asp128Asn, maternal) | PMID:34918187 **[full-text]** |
| Individual II (M) | Egyptian, consanguineous | **homozygous** c.242C>T (p.Pro81Leu) | PMID:34918187 **[full-text]** |
| Lam siblings ×2 | Chinese (Hong Kong) | **compound heterozygous, two variants in trans** — the ACS Omega functional paper identifies the four patient variants as "P81L, A99T, D128N, and a frameshift", and ClinVar links both c.295G>A (p.Ala99Thr) and c.287_320del (p.Asp96fs) to CONPM, so **A99T + D96fs is the strongly-supported inferred pairing for the Lam siblings**. *Verify against the Clin Chim Acta full text before curating the phase assignment as fact.* | PMID:31271740; PMID:34926941 |
| Mexican case (M, 2 y) | Mexican | **homozygous** c.242C>T (p.Pro81Leu) | PMID:40696808 (verbatim abstract) |

**p.Pro81Leu is the recurrent allele**, seen in 3 of 5 reported patients across Egyptian, Dutch, and Mexican ancestries — consistent with recurrent mutation rather than a founder effect (no shared haplotype reported; the three ancestries are unrelated).

### Functional consequences — **loss of function via loss of obligate dimerization**

**Verbatim abstract (PMID:34926941, ACS Omega 2021):**
> "Here we show that in fibroblasts derived from a patient, the P81L and D128N mutations led to a complete loss of TMPK activity in mitochondria and extremely low and unstable TMPK activity in cytosol. Despite the lack of TMPK activity, the patient-derived fibroblasts apparently grew normal. … The wild-type TMPK mainly exists as a dimer with high substrate binding affinity, that is, low *K*M value and high catalytic efficiency, that is, *k*cat/*K*M. In contrast, all mutants were present as monomers with dramatically reduced substrate binding affinity and catalytic efficiencies. Based on the human TMPK structure, none of the mutated amino acids interacted directly with the substrates."

**Kinetics [full-text, Table 2 of PMID:34926941 — re-verify before use]:**

| Enzyme | dTMP *K*M (μM) | dTMP *k*cat (s⁻¹) | dTMP *k*cat/*K*M (M⁻¹s⁻¹) | ATP *K*M (μM) | ATP *k*cat/*K*M (M⁻¹s⁻¹) |
|---|---|---|---|---|---|
| WT | 1.75 ± 0.88 | 3.24 ± 0.23 | 1.85 × 10⁶ | 1.11 ± 0.15 | 2.51 × 10⁶ |
| A99T | 24.6 ± 5.4 | 6.92 ± 0.42 | 0.28 × 10⁶ (**−85%**) | 41.3 ± 4.03 | 0.11 × 10⁶ (**−96%**) |
| P81L | 115.9 ± 31.2 | 17.2 ± 2.13 | 0.14 × 10⁶ (**−92%**) | 43.1 ± 3.67 | 0.12 × 10⁶ (**−95%**) |
| **D128N** | too low for reliable kinetic analysis | — | — | — | — |

**Key mechanistic insight for the pathophysiology graph:** the missense substitutions are **not active-site contact residues**. They act **allosterically/structurally**, converting the obligate homodimer into a catalytically crippled monomer. This is a *dimerization-disruption LoF*, not a substrate-binding LoF — a distinction worth capturing as a distinct MOLECULAR-scale pathophysiology node.

**Cellular enzyme activity [full-text, PMID:34918187]:**
- Individual I fibroblasts: **0.62 pmol/min/mg protein** (essentially undetectable)
- Mother: 43.65 pmol/min/mg; Father: 31.08 pmol/min/mg (both normal)
- Statistical significance: mother vs. proband p = 1.46 × 10⁻⁶; father vs. proband p = 5.77 × 10⁻⁶
- **Compartment-specific finding:** no detectable TMPK activity in mitochondria; low, unstable activity in cytosol (PMID:34926941 abstract, verbatim above).

### Modifier genes

**None identified.** The most important open question in this space is not a modifier *gene* per se but the identity of the **unknown compensatory TMPK-like enzyme** postulated to sustain dTTP synthesis in non-neural tissue. Frisk et al. systematically excluded the five non-canonical *DTYMK* mRNA isoforms (isoforms 2–5 lack essential substrate-binding elements; isoform 6 retains intact catalytic centres but has **<0.1% of isoform-1 activity**) — PMID:34994281. Vanoevelen et al. considered and rejected **CMPK2**: "has no apparent capability to use dTMP as a substrate, it would appear unlikely that CMPK2 can fulfill this function. Thus, a compensatory pathway for dTTP generation remains to be proven." **[full-text]**

**This is the single best `KNOWLEDGE_GAP` discussion item for the dismech entry.**

### Epigenetics

No DNA methylation, histone-modification, chromatin, or episignature data exist for CONPM. *DTYMK* is not on any published rare-disease episignature panel. **Not applicable / no data.**

### Chromosomal abnormalities

None reported as a cause of CONPM. Note that *DTYMK* lies at **2q37.3**, within the interval commonly deleted in **2q37 deletion / Brachydactyly–Mental Retardation syndrome** (which dismech already curates as `2q37_Microdeletion_Syndrome.yaml`, driven by *HDAC4*). **There is no evidence that *DTYMK* haploinsufficiency contributes to the 2q37 deletion phenotype**, and the mouse heterozygote data argue against it (PMID:38621447). Do **not** cross-link these two entries as mechanistically related without new evidence; a "same locus, different mechanism" note is appropriate if any link is made at all.

### Population constraint

gnomAD constraint metrics (pLI / LOEUF / missense Z) for *DTYMK* **could not be retrieved** through available tooling in this session (the gnomAD browser is a JS app and the GraphQL endpoint requires POST). **Do not assert a pLI or LOEUF value from memory.** Fetch these directly before curating a constraint claim. The relevant *biological* constraint statement that IS evidenced: homozygous *Dtymk* knockout is embryonic lethal in mouse while heterozygotes are normal (PMID:38621447) — i.e., **recessive essentiality, not haploinsufficiency**.

---

## 5. Environmental Information

- **Environmental factors:** none. No entries in CTD linking environmental chemicals to CONPM. (CTD does contain *DTYMK*–chemical interactions from toxicogenomic screens, but these are gene-expression associations in unrelated experimental contexts and are **not** disease-etiologic — do not curate them as risk factors.)
- **Lifestyle factors:** not applicable (congenital-onset monogenic disorder).
- **Infectious agents:** not causal. Infection is however a **major proximate cause of death**: Individual I died at 18 months from cardiopulmonary arrest following a respiratory illness; Individual II died at 32 months from **pneumonia** and coma **[full-text]**. Curate these as complications/terminal events (§11), not as etiology.
- **Fever as a trigger:** Individual I had **recurrent febrile seizures** (HP:0002373) **[full-text]**. Whether fever is a genuine decompensation trigger (as in some intoxication-type IEMs) is unstudied — a legitimate hypothesis-flagged item, not an evidenced claim.

---

## 6. Mechanism / Pathophysiology

### 6.1 The causal chain (proposed pathograph, upstream → downstream)

```
[MOLECULAR] Biallelic DTYMK LoF variants (p.Pro81Leu / p.Asp128Asn / p.Ala99Thr / p.Asp96fs)
     │
     ▼
[MOLECULAR] Loss of TMPK homodimerization → monomeric, catalytically crippled enzyme
     │  (kcat/KM reduced 85–96%; D128N below detection)
     ▼
[MOLECULAR] Loss of dTMP → dTDP phosphorylation (EC 2.7.4.9); COMPLETE block of the
     │  canonical dTTP supply, because de novo (TYMS) and salvage (TK1/TK2) both
     │  converge on dTMP UPSTREAM of TMPK
     ▼
[CELLULAR] dTTP insufficiency in cells with high replicative/repair demand
     │        ├──► Impaired DNA replication; S-phase collapse (patient fibroblasts 2.8% S-phase
     │        │     vs. 23.65%/16.03% in parents) [full-text]
     │        ├──► Nucleotide-pool imbalance → RIBONUCLEOTIDE MISINCORPORATION into genomic DNA
     │        │     (dtymk⁻/⁻ zebrafish gDNA fragility comparable to Rnaseh2⁻/⁻ mouse) [full-text]
     │        └──► Impaired DNA damage response (persistent γH2AX 24 h post-UV) [full-text]
     ▼
[CELLULAR] Genome instability in the developing and mature CNS
     ▼
[CELLULAR] Neuronal apoptosis / neuronal dropout
     │  (dtymk mutant zebrafish: significantly more apoptotic cells in forebrain,
     │   p = 6.45 × 10⁻⁶ vs. wild type) [full-text]
     ▼
[TISSUE] Progressive cerebral and striatal atrophy with gliosis;
     │  relative sparing of brainstem, cerebellum, dentate nucleus
     ▼
[ORGANISM] Progressive microcephaly, developmental regression, epilepsy, spastic
            tetraplegia, cortical blindness → early childhood death

        ┌─ PARALLEL / CONTESTED ARM (Lam et al. 2019) ─────────────────────┐
        │ Mitochondrial TMPK activity loss → mitochondrial dTTP pool       │
        │ depletion → mtDNA replication failure → mtDNA DEPLETION →        │
        │ OXPHOS deficiency → lactic acidemia (HP:0002151, 2/2) and        │
        │ hyperalaninemia (HP:0003348, 1/2)                                │
        │ STATUS: mtDNA depletion shown "in silico" only in one sibling;   │
        │ mitochondrial TMPK activity loss confirmed biochemically         │
        │ (PMID:34926941). Curate as an EMERGING mechanistic_hypothesis.   │
        └──────────────────────────────────────────────────────────────────┘

        ┌─ UNRESOLVED COMPENSATION (the central paradox) ──────────────────┐
        │ Unknown "TMPK-like" enzyme sustains dTTP in non-neural tissue →  │
        │ near-normal bulk dNTP pools; normal fibroblast proliferation;    │
        │ viability to birth despite complete canonical-pathway block.     │
        │ Identity unknown. CMPK2 and DTYMK isoform 6 both excluded.       │
        │ Curate as KNOWLEDGE_GAP.                                         │
        └──────────────────────────────────────────────────────────────────┘
```

### 6.2 Molecular pathways

- **Pyrimidine deoxyribonucleotide biosynthesis** — KEGG **hsa00240** (Pyrimidine metabolism). Reactome hosts the reaction under pyrimidine deoxyribonucleotide biosynthesis (the Reactome ContentService returned 403 in this session; **fetch and verify the exact stable ID before curating** — do not assert an R-HSA ID from memory).
- **De novo arm:** dUMP —(TYMS, folate-dependent)→ dTMP
- **Salvage arm:** thymidine —(TK1 cytosolic / TK2 mitochondrial)→ dTMP
- **Convergence point:** dTMP —(**DTYMK/TMPK, blocked**)→ dTDP —(NME/NDPK)→ dTTP
- Downstream: DNA replication, DNA repair, mtDNA replication.

### 6.3 Cellular processes and GO term suggestions

| Process | Suggested GO term | Modifier |
|---|---|---|
| dTMP kinase activity (molecular function) | **GO:0004798** dTMP kinase activity | DECREASED / ABSENT |
| ATP binding | GO:0005524 | — |
| dTDP biosynthetic process | **GO:0006233** | DECREASED |
| dTTP biosynthetic process | **GO:0006235** | DECREASED |
| Thymidine biosynthetic process | GO:0046105 | DECREASED |
| DNA replication | **GO:0006260** | DECREASED |
| DNA repair | **GO:0006281** | DECREASED |
| Cellular response to DNA damage stimulus / DDR signal transduction | GO:0006974 / GO:0000077 | DECREASED (impaired resolution) |
| Apoptotic process / neuron apoptotic process | **GO:0006915** / **GO:0051402** | INCREASED |
| Mitochondrial DNA replication | **GO:0006264** | DECREASED (hypothesis arm) |
| Brain development / forebrain development | GO:0007420 / GO:0030900 | DECREASED |
| Cell cycle / G1-S transition | GO:0007049 / GO:0000082 | DECREASED |
| Protein homodimerization activity | GO:0042803 | DECREASED (the LoF mechanism) |

*All GO IDs above are candidates — verify each with `uv run runoak -i sqlite:obo:go info GO:XXXXXXX -O obo` before commit.*

### 6.4 Protein dysfunction

Loss of function via **failure of obligate homodimerization**. Not misfolding-aggregation, not gain of function, not dominant-negative (heterozygous parents and heterozygous mice are unaffected). Structural rationale: the substituted residues (P81, A99, D128) do not contact substrate; structural modelling explains how each substitution destabilizes the dimer interface / catalytic architecture (PMID:34926941). Structure resources: PDB entries for human TMPK exist (search "human thymidylate kinase" in PDB); AlphaFold model AF-P23919.

### 6.5 Metabolic changes

- Profound reduction of dTDP/dTTP synthetic *flux* through the canonical route.
- **Paradox to curate carefully:** measured steady-state **dNTP pools in patient fibroblasts and in zebrafish mutant larvae "resemble those of normal controls"** **[full-text]**. The disease is therefore best modeled as a **flux/compartment/demand-limited** defect, not a bulk pool-depletion defect. This distinction matters for any downstream biomarker claim — a normal fibroblast dNTP panel does **not** exclude CONPM.
- Secondary systemic markers: elevated lactate (2/2) and hyperalaninemia (1/2) → a mitochondrial-disease-like biochemical signature that will route these patients into an MDDS workup.
- CHEBI candidates (verify with OAK): dTMP **CHEBI:17013**, dTDP **CHEBI:58369**, dTTP **CHEBI:37568**, ATP **CHEBI:30616**, thymidine **CHEBI:17748**, deoxycytidine **CHEBI:15698**, L-lactate **CHEBI:16651**, L-alanine **CHEBI:16977**.

### 6.6 Immune system involvement

**None known.** No autoimmunity, immunodeficiency, or interferonopathy has been reported. This is worth an explicit negative note because the mechanism — **ribonucleotide misincorporation into genomic DNA, explicitly benchmarked in the paper against *Rnaseh2*-null mouse DNA** — is the exact molecular lesion of **Aicardi–Goutières syndrome type 4** (RNASEH2B/C/A), which *is* a type I interferonopathy. Whether CONPM has an unrecognized cGAS-STING/interferon component is an **explicitly attractive, entirely untested hypothesis** and an excellent `KNOWLEDGE_GAP` / `proposed_experiments` item (measure interferon signature in patient fibroblasts and dtymk zebrafish).

### 6.7 Tissue damage mechanisms

Neuronal apoptosis and neuronal dropout with reactive gliosis; not oxidative stress, ischemia, or fibrosis. Zebrafish histology showed "empty spaces, indicative of neurodegeneration" in brain **[full-text]**. Human neuropathology: "massive neuronal dropout, only sparing the dentate nucleus and brain stem" **[full-text]**.

### 6.8 Biochemical abnormalities

Enzyme deficiency (EC 2.7.4.9). Diagnostic assay: dTMPK activity in cultured fibroblasts (see §10). No receptor or ion-channel defect.

### 6.9 Epigenetic changes

No data.

### 6.10 Molecular profiling

- **Transcriptomics:** no patient RNA-seq published for CONPM. GTEx/HPA show broad, non-tissue-specific *DTYMK* expression.
- **Proteomics / metabolomics / lipidomics:** no disease-specific studies. No MetaboLights or PRIDE datasets for CONPM.
- **Single-cell / spatial:** none.
- **Functional genomics screens:** *DTYMK* is a **common essential gene in DepMap** CRISPR screens (consistent with the mouse embryonic lethality) — verify the current DepMap common-essential call before citing. The uveal-melanoma study demonstrates **pharmacological DTYMK inhibition (YMU1) synergizing with PARP1 inhibition (pamiparib)** (PMID:39195238), which is independent orthogonal support for the "DTYMK loss → DNA repair burden" arm of the mechanism, in a cancer rather than neuronal context.

**Verbatim abstract (PMID:39195238, Cells 2024):**
> "Our hypothesis of the double hit into tumoral DNA metabolism as a possible therapeutic option in uveal melanoma was confirmed since combined targeting of DTYMK and PARP1 affected all tested cytophysiological parameters with the highest efficiency."

---

## 7. Anatomical Structures Affected

### Organ level

- **Primary:** brain (central nervous system). **UBERON:0000955** (brain).
- **Secondary:** none primarily; respiratory (aspiration pneumonia, respiratory failure, laryngomalacia), GI (dysphagia, feeding failure), haematological (microcytic anemia, 1 patient), hepatic (transaminase elevation, 1 patient), urogenital (cryptorchidism, micropenis).
- **Body systems:** nervous (dominant); with secondary respiratory, digestive, and reproductive involvement.

### Regional CNS involvement — **the sparing pattern is diagnostically important**

| Structure | UBERON candidate | Involvement |
|---|---|---|
| Cerebral hemispheres / cerebral cortex | UBERON:0000956 | **Severely atrophic** ("dramatic atrophy of the cerebral hemispheres") |
| Basal ganglia / striatum | UBERON:0002420 (basal ganglion); UBERON:0002435 (striatum) | **Severely affected — "disappearance of the basal ganglia"** (abstract, verbatim); "basal nuclei were small" **[full-text]** |
| Lateral ventricles | UBERON:0002285 (telencephalic ventricle) | **Severely enlarged** (ex vacuo) |
| Subarachnoid space | UBERON:0002450 (verify) | **Widened**, 2/2 (HP:0012704) |
| Thalamus | UBERON:0001897 | "appeared to have a normal size" **[full-text]** — **spared** |
| Brainstem | UBERON:0002298 | **Spared** (both patients) |
| Cerebellum | UBERON:0002037 | **Spared** in Vanoevelen patients — **but the 2025 Mexican case reports "cortical and cerebellar atrophy" (PMID:40696808 abstract, verbatim). Curate this as a documented inter-patient discrepancy, not as a resolved fact.** |
| Dentate nucleus | UBERON:0002688 | **Spared** on neuropathology **[full-text]** |

- **Lateralization:** bilateral and symmetric (generalized atrophy). No asymmetry reported.

### Tissue and cell level

| Cell type | CL candidate | Role |
|---|---|---|
| Neuron | **CL:0000540** | Primary target; apoptosis/dropout |
| CNS neuron (sensu Vertebrata) | CL:0000117 | more specific alternative |
| Neural progenitor / neuronal stem cell | CL:0000047 | Likely the proliferative compartment where dTTP demand is highest (mechanistically inferred; **not directly demonstrated in human tissue** — flag as inference) |
| Medium spiny neuron | CL:0000706 (verify) | Implied by striatal loss |
| Astrocyte | CL:0000127 | Gliosis (HP:0002171) |
| Microglial cell | CL:0000129 | Presumed reactive; not directly demonstrated |
| Fibroblast | CL:0000057 | The *ex vivo* assay tissue; notably **functionally spared** despite enzyme loss |

**Key modeling caution:** the phenotype has two temporally distinct cellular substrates — (a) a **proliferative** phase defect (neural progenitors, replication/S-phase) explaining microcephaly, and (b) a **postmitotic** defect (mature neurons, DNA repair burden) explaining progressive degeneration. These should be separate pathophysiology nodes with distinct `biological_scale: CELLULAR` tags, not bundled.

### Subcellular level

| Compartment | GO CC | Note |
|---|---|---|
| Nucleus | GO:0005634 | genomic DNA replication/repair; site of ribonucleotide misincorporation |
| Cytosol | GO:0005829 | residual, unstable TMPK activity in patient cells |
| Mitochondrion | **GO:0005739** | **Complete loss of TMPK activity** in patient fibroblast mitochondria (PMID:34926941) — the anchor for the mtDNA-depletion hypothesis arm |

---

## 8. Temporal Development

### Onset

- **Congenital onset** (HP:0003577) 2/2 and **infantile onset** (HP:0003593) 2/2 — both annotated, reflecting that prenatal/neonatal features (SGA, polyhydramnios, breech, neonatal feeding failure, neonatal hypotonia) precede the overt neurological syndrome.
- Prenatal signals are nonspecific: polyhydramnios 1/2, breech presentation 1/2, SGA 1/2. **Head circumference is near-normal at birth** (Individual I: 31 cm, 2nd centile) — CONPM is **not** reliably detectable by prenatal or newborn OFC.
- **Onset pattern:** insidious/chronic-progressive with a subacute regression phase in infancy.

### Progression

- **Rate: rapid by neurodegenerative standards.** OFC crosses from ~2nd centile to **−7.6 SD within 9 months** (Individual I) and to −7.4 SD by 26 months (Individual II) **[full-text]**.
- **Course:** relentlessly progressive; no remission, no relapsing-remitting pattern, no plateau documented in the severe form.
- **Stages (proposed, for curation):**
  1. **Neonatal (0–3 mo):** hypotonia, feeding failure, NG-tube dependence, absent visual fixation. OFC near-normal.
  2. **Infantile decline (3–15 mo):** rapid OFC deceleration, spasticity replacing hypotonia, opisthotonus, seizure onset, no milestones acquired/loss of acquired milestones.
  3. **Advanced (15 mo–death):** spastic tetraplegia, myoclonus, status epilepticus, flat-trace EEG, complete cortical/striatal atrophy on imaging, respiratory and swallowing failure.
  4. **Terminal:** intercurrent respiratory infection → pneumonia/cardiopulmonary arrest.
- **Duration:** lifelong; life-limiting. **Death in childhood 2/2 (HP:0003819)** — ages 18 and 32 months in the two severe cases.
- **Milder end of spectrum:** the Lam siblings survived to allow assessment of intellectual disability and speech, indicating a genuinely broader survival range. Precise ages/outcomes require the Clin Chim Acta full text.

### Patterns

- **Remission:** none, spontaneous or treatment-induced.
- **Critical periods:** the **first 12 months** — the window during which OFC collapses and the atrophy becomes established. Any disease-modifying intervention would almost certainly need to act prenatally or in the first months. **Curate this as the therapeutic window, and note that no such intervention exists.**
- **Fever/illness as a decompensation trigger:** suggested by febrile seizures and by the fact that both deaths followed intercurrent respiratory infection, but **not established** as a metabolic-decompensation mechanism.

---

## 9. Inheritance and Population

### Epidemiology

- **Prevalence: not documented.** No ORPHA prevalence class is available (no Orphanet entry found). For a dismech `Prevalence` record the honest structured encoding is:
  - `measure_type: CASES_IN_LITERATURE`
  - `prevalence_class: ULTRA_RARE` (or `NOT_YET_DOCUMENTED`)
  - `notes: "Five patients reported worldwide as of 2025 (Vanoevelen 2022 n=2; Lam 2019 n=2; Hernández-Carreto 2025 n=1)."`
  - **Do not** populate `rate_per_100000`.
- **Incidence:** unknown.
- **Verbatim abstract (PMID:40696808):** "Only four cases have been reported in the literature to date. This paper's objective is to describe the fifth globally reported case of CONPM and the first documented in a Mexican patient…"

### Genetic epidemiology

| Parameter | Value | Evidence |
|---|---|---|
| **Inheritance** | **Autosomal recessive** — HP:0000007 | HPO annotation; OMIM #619847; all patients biallelic; parents unaffected heterozygotes |
| **Penetrance** | Appears complete for biallelic LoF; n too small for a formal estimate | 5/5 biallelic individuals affected |
| **Expressivity** | **Variable** — this is explicit in the OMIM summary: severe (no milestones, death <3 y) vs. milder (small head, severe ID, poor speech, motor delay). Genotype–phenotype correlation is **not established**; note that p.Pro81Leu homozygotes span the severe end (Egyptian, Mexican cases) | OMIM #619847; PMID:34918187; PMID:31271740 |
| **Genetic anticipation** | **Not applicable** (no repeat expansion) | — |
| **Germline mosaicism** | Not reported | — |
| **Founder effect** | **None demonstrated.** p.Pro81Leu recurs across three unrelated ancestries (Dutch, Egyptian, Mexican) without a reported shared haplotype — favours recurrent mutation | ClinVar; PMID:34918187; PMID:40696808 |
| **Consanguinity** | Contributory in at least the Egyptian case (documented consanguinity, homozygous P81L) and presumptively in the Mexican homozygous case | PMID:34918187 **[full-text]**; PMID:40696808 |
| **Carrier frequency** | Not established. Individual allele frequencies in gnomAD are ~1–3 × 10⁻⁵; the aggregate carrier frequency for pathogenic *DTYMK* alleles has not been computed and **should not be estimated here** | ClinVar/gnomAD |

### Population demographics

- **Affected populations:** Dutch, Egyptian, Chinese (Hong Kong), Mexican — i.e., **no ethnic clustering**; the disorder is pan-ethnic and its rarity is a function of allele rarity, not population structure.
- **Geographic distribution:** none (case reports from Europe, North Africa, East Asia, Latin America).
- **Variant geography:** p.Pro81Leu reported in Netherlands, Egypt, Mexico; p.Asp128Asn in the Netherlands; p.Ala99Thr and p.Asp96fs in Hong Kong.
- **Sex ratio:** among the fully characterized cases, 1 female (Individual I) and 2 males (Individual II, Mexican case); the Lam siblings' sexes require the full text. **n = 5 is far too small to infer a sex ratio — curate as "no sex bias reported"** rather than a ratio.
- **Age distribution:** all affected individuals identified in infancy/early childhood; no adult-onset or adult-diagnosed cases.

---

## 10. Diagnostics

### Clinical / laboratory tests

| Test | Finding | LOINC / notes |
|---|---|---|
| **Plasma lactate** | Elevated, 2/2 (HP:0002151) | LOINC 2524-7 / 32693-4 |
| **Plasma amino acids (alanine)** | Hyperalaninemia, 1/2 (HP:0003348) | LOINC 26603-3 |
| **CBC** | Microcytic hypochromic anemia (1 patient) **[full-text]** | |
| **Liver enzymes** | Elevated (1 patient) **[full-text]** | ALT LOINC 1742-6; AST 1920-8 |
| **Fibroblast dTMPK enzyme activity** | **The confirmatory functional assay.** Patient 0.62 pmol/min/mg vs. parents 43.65 and 31.08 pmol/min/mg **[full-text]**. Available only as a research assay. | No LOINC code identified |
| **Subcellular fractionation TMPK assay** | Absent mitochondrial activity; low/unstable cytosolic activity (PMID:34926941) | research assay |
| **Fibroblast dNTP pool quantification** | **Normal or near-normal — a NEGATIVE result does not exclude the diagnosis** **[full-text]** | research assay; important caveat |
| **Cell-cycle/S-phase analysis of fibroblasts** | Reduced S-phase fraction (2.8% vs. 16–24% parental) **[full-text]** | research assay |
| **mtDNA copy number (muscle/blood)** | mtDNA depletion asserted **"in silico"** in one Lam sibling — i.e., **inferred, not directly quantified** (PMID:31271740 verbatim). Direct qPCR mtDNA copy-number quantification in patient tissue is an outstanding validation experiment. | LOINC not established |

### Imaging

**Brain MRI is the highest-yield diagnostic modality.** Expected findings:
- Profound generalized cerebral atrophy (HP:0002059)
- Marked lateral ventricular dilatation (HP:0006956) and widened subarachnoid spaces (HP:0012704)
- **Small/"disappeared" basal ganglia** — the most distinctive feature
- Normal-sized thalamus, brainstem, and (usually) cerebellum
- Serial imaging showing progression is more informative than a single study.

**Verbatim (PMID:34918187 abstract):** "Brain imaging revealed severe cerebral atrophy and disappearance of the basal ganglia."

### Electrophysiology

- **EEG:** abnormal; **flat trace** documented in the advanced stage of Individual I **[full-text]**. No pathognomonic pattern.
- EMG/NCS/ECG: no reported abnormalities; peripheral nerve involvement not described.

### Biopsy / pathology

- **Neuropathology (post-mortem, Individual I):** massive neuronal dropout with sparing of dentate nucleus and brainstem; gliosis **[full-text]**.
- **Skin biopsy for fibroblast culture is the key diagnostic specimen** (enables the enzyme assay).
- Muscle biopsy: no characteristic ragged-red/COX-negative findings reported; if the MDDS hypothesis is pursued, muscle mtDNA quantification would be the test.

### Genetic testing

- **Recommended first-tier approach: whole-exome sequencing (WES) or whole-genome sequencing (WGS) with trio analysis.** All five reported patients were diagnosed by exome sequencing. WES is what identified the Mexican case ("confirmed through whole-exome sequencing (WES)", PMID:40696808 verbatim) and the Lam siblings ("whole exome sequencing is often needed for their diagnoses", PMID:31271740 verbatim).
- **Gene panels:** *DTYMK* should be — and in some laboratories now is — included on **(a) progressive/primary microcephaly panels, (b) neurodegeneration-in-childhood panels, and (c) mitochondrial DNA depletion syndrome panels.** Its inclusion is inconsistent across vendors; verify panel content in GTR for any specific lab before recommending. Confirm current listings at https://www.ncbi.nlm.nih.gov/gtr/.
- **Single-gene testing:** appropriate only for targeted familial-variant testing / cascade screening after a proband diagnosis.
- **Sanger confirmation + segregation** in both parents is essential to establish biallelic status and phase (as done in PMID:40696808).
- **CMA / karyotype / FISH:** low yield for CONPM itself. CMA remains reasonable as part of a general microcephaly workup and would detect a 2q37.3 deletion contributing one allele in a compound-heterozygous configuration — worth explicitly considering, since a whole-gene deletion in trans with a point variant would be missed by exome-only analysis.
- **mtDNA testing:** mtDNA sequencing and **copy-number quantification** are indicated given the MDDS differential and the lactate/alanine profile.
- **Repeat expansion testing:** not indicated.
- **RNA-seq:** useful as a second-tier tool to resolve the deep-intronic VUS (c.239+1045_239+1050del, VCV003065236) or other candidate splice-affecting alleles.

### Clinical criteria and differential diagnosis

No consensus diagnostic criteria exist (too few patients). Diagnosis = compatible phenotype + biallelic *DTYMK* variants (± functional confirmation).

**Differential diagnosis — the most useful section for a curator, because CONPM's imaging and biochemical profile overlaps several well-known entities:**

| Differential | Distinguishing features |
|---|---|
| **Primary autosomal recessive microcephaly (MCPH; ASPM, WDR62, etc.)** | MCPH is **congenital and largely static**; CONPM head circumference is near-normal at birth then collapses postnatally, with frank *degeneration* and basal ganglia loss |
| **Mitochondrial DNA depletion syndromes (TK2, DGUOK, POLG, RRM2B, SUCLA2, MPV17, FBXL4, TWNK)** | Overlapping lactate/alanine elevation and nucleotide-metabolism logic; distinguish by mtDNA copy number and gene. **This is the single highest-risk misclassification** — Lam et al. explicitly proposed DTYMK *as* an MDDS gene |
| **Aicardi–Goutières syndrome (RNASEH2A/B/C, TREX1, SAMHD1, ADAR, IFIH1)** | Mechanistically adjacent (ribonucleotide misincorporation / nucleic-acid metabolism), also causes progressive microcephaly with basal ganglia involvement — but AGS has **intracranial calcification, CSF pleocytosis, raised CSF interferon-α, and an interferon signature**, none of which have been reported (or, importantly, *looked for*) in CONPM |
| **Pontocerebellar hypoplasia (TSEN54 etc.)** | PCH has **cerebellar/pontine hypoplasia**; CONPM classically spares brainstem and cerebellum |
| **Congenital infection (TORCH/CMV/Zika)** | Serology/PCR; intracranial calcification; non-Mendelian |
| **Other serine/nucleotide/one-carbon IEMs (PYCR2, PNKP, serine biosynthesis defects)** | Distinguished genetically; PNKP is another DNA-repair microcephaly with epileptic encephalopathy and is a close clinical mimic |
| **Molybdenum cofactor deficiency / sulfite oxidase deficiency** | Early catastrophic encephalopathy with cystic cerebral destruction; distinguished by urine sulfite/S-sulfocysteine, low urate |

### Screening

- **Newborn screening:** **not applicable.** There is no analyte biomarker, no treatment, and head circumference is near-normal at birth. CONPM fails standard Wilson–Jungner criteria.
- **Carrier screening:** *DTYMK* is **not** on standard expanded carrier screening panels. Its inclusion would be defensible only in the context of a known family.
- **Cascade screening:** targeted variant testing of at-risk relatives and reproductive partners after a proband diagnosis — this is the highest-value screening application.

---

## 11. Outcome / Prognosis

### Survival and mortality

- **Death in childhood (HP:0003819) in 2/2 of the severely affected annotated individuals.**
- **Documented ages at death: 18 months** (Individual I, cardiopulmonary arrest following respiratory illness) and **32 months** (Individual II, pneumonia and coma) **[full-text]**.
- The milder Lam siblings survived long enough for formal intellectual assessment, establishing that survival beyond early childhood occurs at the mild end. Precise survival data require the primary full text.
- No 5-/10-year survival statistics, no life-expectancy estimate, no mortality rate — **n is too small.** For dismech, curate "death in early childhood in the severe form; survival documented in the milder form" with the two specific ages, rather than any derived rate.
- **Disease-specific mortality:** deaths are attributable to the disease via its complications (respiratory infection, aspiration, respiratory failure) rather than to a single organ failure.

### Morbidity and function

- Profound, permanent, global disability: no independent sitting, rolling, vocalizing, or smiling in the severe form ("he did not roll over, sit, vocalize, or smile") **[full-text]**; total care dependence; enteral feeding; refractory epilepsy; cortical blindness; spastic tetraplegia.
- **No quality-of-life instrument has been applied.** No EQ-5D, PedsQL, PROMIS, or CPCHILD data exist. Do not populate QoL scores.
- GBD/WHO carry no disease-specific burden estimate.

### Complications

Aspiration and recurrent respiratory infection → **pneumonia (a documented cause of death)**; respiratory failure (HP:0002878); laryngomalacia (HP:0001601); dysphagia (HP:0002015) with tube-feeding dependence (HP:0033454); status epilepticus (HP:0002133); failure to thrive/short stature; contractures secondary to spastic tetraplegia (expected, not explicitly reported); microcytic anemia; transaminase elevation.

### Recovery potential

**None.** Neuronal loss is irreversible; no disease-modifying therapy exists; no recovery or plateau has been documented in the severe form.

### Prognostic factors

No validated prognostic model. Observationally suggestive (all **low-confidence**, n=5):
- **Rate of OFC decline in the first year** is the most face-valid clinical prognostic index.
- **Age at seizure onset** (6 months vs. 15 months, both severe).
- **Residual enzyme activity:** biochemically plausible as the primary determinant (p.Ala99Thr retains the highest residual kcat/KM of the characterized missense alleles, and the Lam siblings carrying A99T are at the milder end — **an appealing but unproven genotype–phenotype correlation with n=2; explicitly flag as a hypothesis, not a finding**).
- **Prognostic biomarkers:** none validated.

---

## 12. Treatment

### There is no disease-specific or disease-modifying therapy. Management is entirely supportive.

### Pharmacotherapy

| Treatment | Purpose | Evidence | NCIT candidate |
|---|---|---|---|
| **Phenobarbital** | Seizure control (used in Individual I) **[full-text]** | Case-level, n=1 | `NCIT:C15986` Pharmacotherapy + `therapeutic_agent` CHEBI:8069 phenobarbital (verify) |
| **Carbamazepine** | Myoclonic jerks (used in Individual II) **[full-text]** | Case-level, n=1. *Clinical caveat worth recording: carbamazepine can exacerbate myoclonic seizures; the choice reflects a single clinician's decision, not a guideline.* | `NCIT:C15986` + CHEBI:3387 carbamazepine (verify) |
| Antiseizure medication (general) | Refractory epilepsy | No CONPM-specific efficacy data | `NCIT:C15986` |

**Pharmacogenomics:** no CPIC/PharmGKB guidance specific to *DTYMK*. A worth-noting theoretical consideration (**unstudied — do not curate as evidence**): the affected pathway is the target of thymidylate-synthase inhibitors (5-FU, capecitabine) and antifolates (methotrexate); whether *DTYMK* carriers or patients have altered sensitivity is unknown.

### Advanced therapeutics

- **Gene therapy:** none. No preclinical AAV or gene-replacement program identified. *DTYMK* is small (212 aa CDS, well within AAV capacity) and the disease is recessive LoF — i.e., theoretically tractable — but the **postnatal-degeneration timeline and the near-complete atrophy by 12–24 months make the therapeutic window extremely narrow**, and no program exists.
- **Gene editing / cell therapy / mRNA / siRNA / ASO:** none. ASO is mechanistically inapplicable (missense LoF, not a splice or knockdown target — with the possible exception of the deep-intronic VUS if it proves splice-altering).
- **Enzyme replacement:** not feasible — TMPK is an intracellular, nuclear/cytosolic/mitochondrial kinase acting on a phosphorylated, membrane-impermeant substrate.

### Substrate/nucleoside supplementation — **the one active clinical-trial handle, with a critical mechanistic caveat**

**NCT04802707 — "Deoxynucleosides Pyrimidines as Treatment for Mitochondrial Depletion Syndrome"**, Phase II, open-label, single-centre, recruiting; deoxycytidine (dC) + deoxythymidine (dT) orally, escalating over 22 days then maintained at 400 mg/kg; ages 0–60; up to ~200 participants. **This trial explicitly lists *DTYMK* among its eligible genotypes.**

The record is already present in the dismech reference cache (`references_cache/clinicaltrials_NCT04802707.md`), and the following is a verified quotable snippet from that cached file:

> "The subjects included are children (0-18Y), with positive MDS diagnosis and express mutations in one of the following genes: POLG, POLG2, C10orf2, RRM2B, MPV17, SUCLA2, SUCLG1, FBXL4, DTYMK."

**⚠️ Mechanistic caveat that MUST accompany this trial in the knowledge base.** Deoxynucleoside substrate-enhancement therapy works in **TK2 deficiency** because supplying dThd/dCtd bypasses a *kinase-limited first* salvage step. In DTYMK deficiency the block is at **dTMP → dTDP**, i.e., **downstream of where supplemental thymidine enters the pathway** (thymidine → TK1/TK2 → dTMP → **[BLOCK]**). Supplying more dThd therefore increases the substrate that is already accumulating proximal to the block and has **no obvious mechanistic route to restoring dTTP**. Supplemental dCtd could in principle relieve dNTP-pool imbalance on the pyrimidine side, but that is speculative.

**Recommended curation:** record NCT04802707 as a clinical trial whose eligibility includes *DTYMK*, and attach an explicit `discussions` entry of `kind: KNOWLEDGE_GAP` (or a `mechanistic_hypotheses` entry with `status: EMERGING`) stating that the substrate-bypass rationale is **not established for DTYMK** given the position of the enzymatic block, with `proposed_experiments` = measure dTTP pools and mtDNA copy number in DTYMK-deficient cells ± dT/dC. Do **not** curate dC/dT as an evidenced treatment for CONPM.

### Surgical and interventional

- **Gastrostomy (PEG)** for tube-feeding dependence — clinically standard for this level of dysphagia (NG tube documented; PEG not explicitly reported). `NCIT:C15329` Surgical Procedure; consider a gastrostomy-specific NCIT term.
- Orchidopexy for cryptorchidism, where clinically indicated. `NCIT:C16186` Orthopedic Surgical Procedure is *not* correct here — look up a urological/orchidopexy NCIT term.
- Airway management for laryngomalacia and respiratory failure.

### Supportive and rehabilitative

| Intervention | NCIT candidate | `therapeutic_modality` |
|---|---|---|
| Multidisciplinary supportive/palliative care | `NCIT:C15747` Supportive Care | OTHER |
| Nutritional support / enteral feeding | `NCIT:C15433` Nutritional Support | *do not auto-tag BEHAVIORAL — see CLAUDE.md backfill guidance*; here it is enteral nutrition, closest to OTHER/BEHAVIORAL — decide per entry |
| Physical therapy (spasticity, contracture prevention) | `NCIT:C15302` Physical Therapy | BEHAVIORAL |
| Occupational therapy | `NCIT:C121351` Occupational Therapy | BEHAVIORAL |
| Seizure management | `NCIT:C15986` Pharmacotherapy | SMALL_MOLECULE |
| Respiratory care / aspiration prevention | `NCIT:C15747` Supportive Care | OTHER |
| **Genetic counselling** | `NCIT:C15240` Genetic Counseling | OTHER |

*All NCIT IDs must be verified with `uv run runoak -i sqlite:obo:ncit info NCIT:Cxxxxx -O obo`.*

### Treatment outcomes, adverse events, algorithms

- No response-rate data (no disease-specific therapy has been trialled in CONPM).
- No CONPM-specific adverse-event data. FAERS contains nothing indexed to this disease.
- **No treatment algorithm, guideline, NCCN/society pathway, or GeneReviews chapter exists** for CONPM. Management follows generic severe-neurodegenerative-encephalopathy principles.
- **Personalized medicine:** the only genotype-guided element currently available is reproductive (see §13).

---

## 13. Prevention

### Primary prevention

**Not achievable for an affected fetus/child** — the disorder is determined at conception. Prevention is entirely **reproductive**:
- **Genetic counselling** for at-risk couples: 25% recurrence risk per pregnancy, 50% carrier risk for unaffected sibs, standard AR counselling. `NCIT:C15240`.
- **Carrier testing** of the proband's parents and extended family (particularly relevant in consanguineous kindreds).
- **Prenatal diagnosis** by CVS or amniocentesis with targeted testing of the known familial variants.
- **Preimplantation genetic testing for monogenic disease (PGT-M)** — technically straightforward once the familial variants are known.
- **Consanguinity counselling** in populations where first-cousin union is common.

### Secondary prevention (early detection)

- **No population screening is justified or available.** Newborn screening is not applicable (no analyte, no treatment, normal birth OFC).
- The practical "early detection" measure is **serial head-circumference monitoring** in infancy, which will flag the OFC deceleration and trigger a workup — but this detects the disease after neuronal loss has begun and does not alter outcome.
- **Cascade testing within a known family** is the only genuinely effective early-detection route.

### Tertiary prevention (preventing complications) — this is where real clinical benefit lies

- **Aspiration prevention:** early swallow assessment, thickened feeds, timely conversion from NG to gastrostomy. Directly targets the documented cause of death (pneumonia).
- **Respiratory infection prophylaxis:** routine immunizations, influenza and RSV prophylaxis, pneumococcal vaccination, chest physiotherapy, prompt treatment of intercurrent infection.
- **Seizure control** to prevent status epilepticus.
- **Contracture and positioning management** for spastic tetraplegia.
- **Nutritional optimization** to prevent iron-deficiency/microcytic anemia and further growth failure.

### Immunization

No disease-specific vaccine. **Routine childhood immunization plus respiratory-pathogen prophylaxis is a high-value intervention** given that both documented deaths followed respiratory infection. `NCIT:C15346` Vaccination.

### Public health and environmental interventions

Not applicable. No environmental modifiable risk exists.

---

## 14. Other Species / Natural Disease

### Orthologs (Alliance of Genome Resources, all high-confidence "best score")

| Species | NCBITaxon | Gene | Database ID |
|---|---|---|---|
| Mouse (*Mus musculus*) | NCBITaxon:10090 | *Dtymk* | MGI:108396 |
| Rat (*Rattus norvegicus*) | NCBITaxon:10116 | *Dtymk* | RGD:1309614 |
| Zebrafish (*Danio rerio*) | NCBITaxon:7955 | *dtymk* | ZFIN:ZDB-GENE-990603-11 |
| Fruit fly (*Drosophila melanogaster*) | NCBITaxon:7227 | *Dtymk* | FB:FBgn0034299 |
| Nematode (*C. elegans*) | NCBITaxon:6239 | *dtmk-1* | WB:WBGene00011272 |
| Budding yeast (*S. cerevisiae*) | NCBITaxon:4932 | ***CDC8*** | SGD:S000003818 |
| *Xenopus laevis* | NCBITaxon:8355 | *dtymk.S* | Xenbase:XB-GENE-1004312 |
| *Xenopus tropicalis* | NCBITaxon:8364 | *dtymk* | Xenbase:XB-GENE-1004306 |

The yeast ortholog name **CDC8** (cell division cycle 8) — which is also the *human* gene's legacy alias — is a direct historical signal of the gene's core cell-cycle function and of deep evolutionary conservation.

### Naturally occurring disease in other species

**None known.** A search of OMIA and the veterinary literature identified **no naturally occurring DTYMK-related disease** in companion animals, livestock, or wildlife. No breed-associated variant; **no VBO breed identifier applicable.** No zoonotic potential and no cross-species transmission (this is a Mendelian metabolic disorder, not a transmissible condition).

### Comparative biology

- **Evolutionary conservation is exceptionally deep** — a functional TMPK ortholog is present from yeast through humans, consistent with dTTP synthesis being a universal requirement.
- **Comparative pathology diverges in an interesting and curation-relevant way:**
  - **Mouse:** homozygous null is **embryonic lethal** (PMID:38621447) — mouse does NOT recapitulate the human "viable but neurodegenerative" phenotype.
  - **Zebrafish:** homozygous mutant is **viable through early larval stages with microcephaly and neurodegeneration, then lethal** — this is the closest phenocopy.
  - **Human:** viable to birth with normal-sized head, then postnatal neurodegeneration.
  - **This species gradient (mouse lethal < zebrafish larval-lethal < human postnatal-degenerative) is itself evidence that the hypothesized compensatory dTTP pathway differs in capacity across species** — an elegant framing for the `HUMAN_MODEL_MISMATCH` discussion.
- **Enzymatic substrate specificity diverges too:** *Drosophila* TMPK phosphorylates dTMP, dUMP, **and also dGMP and dIMP** (at low efficiency), unlike human TMPK (PMID:38518117 abstract, verbatim below) — relevant if a fly model is used, because compensation logic may differ.

**Verbatim abstract (PMID:38518117):**
> "Unlike human TMPK, DmTMPK phosphorylated not only dTMP and dUMP but also dGMP and dIMP although with low efficiency. ATP and dATP are the most efficient phosphate donor but at higher concentration (>1 mM) ATP inhibited DmTMPK activity."

---

## 15. Model Organisms

### 15.1 Zebrafish — the flagship model (best phenocopy)

**Allele:** CRISPR-generated **5-bp deletion in exon 4**, producing a premature stop codon 19 amino acids downstream **[full-text]**. Source: Vanoevelen et al., PMID:34918187. Should be registered/lookup-able at ZFIN (ZDB-GENE-990603-11).

**Phenotype recapitulation — strong:**

| Feature | Zebrafish *dtymk*⁻/⁻ | Human CONPM | Recapitulates? |
|---|---|---|---|
| Microcephaly | Head size significantly smaller than siblings (p = 1.52 × 10⁻¹³) | Severe progressive microcephaly | ✅ |
| Neurodegeneration | "Empty spaces, indicative of neurodegeneration" in brain | Massive neuronal dropout | ✅ |
| Neuronal apoptosis | Significantly more apoptotic cells in forebrain (p = 6.45 × 10⁻⁶ vs. WT) | Neuronal apoptosis inferred | ✅ |
| Seizure-like activity | "Twitching movements, reminiscent of epileptic seizures" from 3 dpf | Seizures from 6–15 months | ✅ (behavioral proxy) |
| Enzyme loss | 1.80 pmol/min/mg vs. sibling 38.55 / WT 41.43 | 0.62 vs. parental 31–44 | ✅ (quantitatively parallel) |
| Early lethality | >40% dead by 5 dpf | Death at 18–32 months | ✅ (accelerated) |
| Ribonucleotide misincorporation | gDNA migrates lower + broad smear on alkaline gel; comparable to *Rnaseh2*⁻/⁻ mouse DNA | Not measured in humans | ⚠️ model-only |
| Impaired DDR | Persistent γH2AX 24 h post-UV | Not measured in humans | ⚠️ model-only |
| Small eyes, pericardial/intestinal edema, brain edema (2/3), absent Meckel's cartilage | Present | **Not features of human disease** | ❌ model-specific |

**Limitations:** (i) the fish shows non-CNS malformations (cardiac/intestinal edema, absent Meckel's cartilage, microphthalmia) that are **not** part of the human phenotype, suggesting a broader requirement in fish; (ii) the compressed larval timeline cannot model postnatal *progressive* degeneration over months–years; (iii) the two mechanistically most novel findings — ribonucleotide misincorporation and defective DDR — are **demonstrated only in fish, never in human tissue**. → **This is a textbook `HUMAN_MODEL_MISMATCH` discussion item** (evidence exists in a model; human translational validity is the open question), not a plain `KNOWLEDGE_GAP`.

**Verbatim abstract (PMID:34918187):**
> "In addition, we generated dtymk mutant zebrafish that replicate this phenotype of microcephaly, neuronal cell death and early lethality. An increase of ribonucleotide incorporation in the genome as well as impaired responses to DNA damage were observed in dtymk mutant zebrafish, providing novel pathophysiological insights."

**Supporting zebrafish developmental work (PMID:35346037, BMC Neuroscience 2022) — verbatim abstract excerpts:**
> "Our findings reveal that maternal-stored dNTPs are only sufficient for 6 cell division cycles, and the levels of dNTPs are inversely correlated to cell cycle length during early embryogenesis. TMPK and TK activities are prominent in the cytosol of embryos, larvae and adult fish and brain contains the highest TMPK activity."
> "Our results suggest that active dNTP synthesis in early embryogenesis is vital and that Dtymk is essential for neurodevelopment, which is supported by a recent study of dtymk knockout zebrafish with neurological disorder and lethal outcomes. Furthermore, there is a novel TMPK-like enzyme expressed at later stages of development."

**Note the last sentence** — it is independent, orthogonal support for the "unknown compensatory TMPK-like enzyme," this time from a developmental-stage expression study rather than from patient cells.

### 15.2 Mouse — essentiality established, disease NOT modeled

Tiani & Stover, *Arch Biochem Biophys* 2024, **PMID:38621447**, DOI 10.1016/j.abb.2024.109991.

- **Homozygous *Dtymk* knockout is embryonic lethal.**
- **Heterozygotes** across three dietary conditions showed **no open neural tube defects**, despite ~3-fold reduced dTYMK expression.
- **Implication:** the standard mouse null is **not a usable CONPM model.** A viable model would require a **hypomorphic knock-in** (e.g., the human p.Pro81Leu or p.Ala99Thr allele) or a **conditional/neural-specific conditional knockout** (Nestin-Cre, Emx1-Cre). **No such mouse has been reported** — this is the single most valuable missing reagent in the field and a strong `proposed_experiments` entry.
- Resources to check for existing alleles: MGI (MGI:108396), IMPC, KOMP/EuMMCR, IMSR.

### 15.3 Drosophila — characterized enzyme, no disease model yet

PMID:38518117 (Hu Frisk & Wang 2024) cloned, expressed, purified, and kinetically characterized *Dm*TMPK, explicitly as groundwork for a fly disease model: "*Drosophila* has been used as an animal model to study pathogenic mechanism of neurological disorders… This study has laid a solid foundation for future study of TMPK function in *Drosophila*." **No *Dtymk* mutant fly phenotype has been published.** Caveat: broader substrate specificity than human TMPK (see §14).

### 15.4 In vitro / cellular models

- **Patient-derived dermal fibroblasts** (Individual I) — the workhorse. Available from the Vanoevelen/Bierau group (Maastricht). Used for enzyme assay, subcellular fractionation, S-phase analysis, dNTP pools. **Key limitation: fibroblasts proliferate normally and thus do not phenocopy the disease** — they are a biochemical readout, not a disease model.
- **Recombinant TMPK (WT, P81L, A99T, D128N)** expressed and purified for kinetics and size-exclusion dimerization analysis (PMID:34926941).
- **iPSC / neural organoids: none reported.** Given that (a) the phenotype is neuron-specific, (b) fibroblasts are spared, and (c) the compensating enzyme is unknown, **patient-iPSC-derived cortical neurons and cerebral organoids are the obvious highest-value missing model.** This is also directly relevant to MorPhiC-style cellular-phenotype curation (§CLAUDE.md MorPhiC pattern): a *DTYMK*-null iPSC line with `category: Cellular` phenotypes and `evidence_source: IN_VITRO` would be a natural future annotation — **but note that *DTYMK* is not among the current MorPhiC anchor genes (ISL1, EOMES, GCM1, NKX2-1), so no MorPhiC data exist today.**
- **Cancer cell lines:** MP41/MP46 uveal melanoma with the TMPK inhibitor **YMU1** (PMID:39195238) — a pharmacological loss-of-function system, useful as orthogonal mechanistic support but **not** a neurodegeneration model.

### 15.5 Yeast

*S. cerevisiae* **CDC8** — the classical cell-division-cycle mutant. Historically the source of the "TMPK is required for cell-cycle progression" understanding. Not used as a CONPM model but valuable for conservation arguments.

---

## Appendix A — Master citation list

| PMID | Citation | DOI | Relevance |
|---|---|---|---|
| **34918187** | Vanoevelen JM, Bierau J, Grashorn JC, et al. **DTYMK is essential for genome integrity and neuronal survival.** *Acta Neuropathol.* 2022. | 10.1007/s00401-021-02394-0 | **Landmark / disease-defining paper.** 2 patients, enzymology, zebrafish model, ribonucleotide misincorporation, DDR defect |
| **31271740** | Lam CW, Yeung WL, Ling TK, Wong KC, Law CY. **Deoxythymidylate kinase, DTYMK, is a novel gene for mitochondrial DNA depletion syndrome.** *Clin Chim Acta.* 2019 Sep;496:93-99. | 10.1016/j.cca.2019.06.028 | **First clinical report** (2 siblings); MDDS framing; milder end of spectrum |
| **40696808** | Hernández-Carreto R, Acosta-Rodríguez-Bueno PC, Barragán-Arevalo T, et al. **Childhood-Onset Neurodegeneration With Progressive Microcephaly (CONPM) due to a DTYMK Homozygous Pathogenic Variant: Outlining the Phenotype of an Ultra-Rare Disease.** *Am J Med Genet A.* 2025. | 10.1002/ajmg.a.64187 | **Fifth reported case**; establishes "only four cases prior"; homozygous P81L; cerebellar atrophy discrepancy |
| **34926941** | Frisk JH, Vanoevelen JM, Bierau J, Pejler G, Eriksson S, Wang L. **Biochemical Characterizations of Human TMPK Mutations Identified in Patients with Severe Microcephaly: Single Amino Acid Substitutions Impair Dimerization and Abolish Their Catalytic Activity.** *ACS Omega.* 2021. | 10.1021/acsomega.1c05288 | **Definitive functional/variant characterization**; kinetics; dimerization mechanism; mitochondrial vs cytosolic activity; compensatory-enzyme paradox |
| **34994281** | Hu Frisk J, Pejler G, Eriksson S. **Structural and functional analysis of human thymidylate kinase isoforms.** *Nucleosides Nucleotides Nucleic Acids.* 2022. | 10.1080/15257770.2021.2023748 | Excludes *DTYMK* isoforms as the compensating enzyme; "no defects were observed in other tissues" |
| **35346037** | Frisk JH, Örn S, Pejler G, et al. **Differential expression of enzymes in thymidylate biosynthesis in zebrafish at different developmental stages: implications for dtymk mutation-caused neurodegenerative disorders.** *BMC Neurosci.* 2022. | 10.1186/s12868-022-00704-0 | Developmental dNTP demand; brain has highest TMPK activity; independent evidence for a novel TMPK-like enzyme |
| **38621447** | Tiani KA, Stover PJ. **DTYMK is an essential gene in mice and heterozygosity does not cause neural tube defects.** *Arch Biochem Biophys.* 2024. | 10.1016/j.abb.2024.109991 | Mouse essentiality; heterozygote tolerance; negative diet/NTD result |
| **38518117** | Hu Frisk J, Wang L. **Molecular characterization of *Drosophila melanogaster* thymidylate kinase.** *Nucleosides Nucleotides Nucleic Acids.* 2024;43(8):734-742. | 10.1080/15257770.2024.2332410 | Fly model groundwork; substrate-specificity divergence |
| **39195238** | Oziębło S, Mizera J, Górska A, et al. **Co-Targeting of DTYMK and PARP1 as a Potential Therapeutic Approach in Uveal Melanoma.** *Cells.* 2024;13(16):1348. | 10.3390/cells13161348 | Orthogonal pharmacological support for the DTYMK–DNA-repair axis (oncology context) |
| **NCT04802707** | Deoxynucleosides Pyrimidines as Treatment for Mitochondrial Depletion Syndrome. Phase II, recruiting. | — | Only trial with *DTYMK* eligibility; **already in `references_cache/clinicaltrials_NCT04802707.md`** |

**Database records:** OMIM #619847; OMIM \*188345; MONDO:0859241; MedGen C5676972 / UID 1801540; HGNC:3061; UniProt P23919; ClinVar VCV001686902/3/4/5, VCV004277573, VCV003065236; Human Protein Atlas ENSG00000168393; Alliance of Genome Resources HGNC:3061 orthology; HPO annotation set for OMIM:619847.

---

## Appendix B — Curation checklist and flagged gaps for the dismech entry

**Verification required before commit**
1. Run `just fetch-reference` for every PMID above; verify every snippet is an exact substring. All **[full-text]**-marked sentences in this report came through an intermediate summarizer and **must be re-verified against the PMC source** (PMC8742820, PMC8679000) before use as evidence.
2. Run `just validate-terms` on every HP/GO/CL/UBERON/CHEBI/NCIT ID suggested here — none have been OAK-verified in this session.
3. Fetch gnomAD constraint values directly; **do not assert pLI/LOEUF from this report** (retrieval failed).
4. Verify the Reactome stable ID for pyrimidine deoxyribonucleotide biosynthesis (ContentService returned 403).
5. Obtain the Lam 2019 full text to confirm (a) the phase/pairing of A99T + D96fs, (b) the siblings' sexes and ages, (c) whether mtDNA depletion was measured or only inferred.

**Recommended `discussions` entries**
- `kind: KNOWLEDGE_GAP` — **identity of the compensatory TMPK-like enzyme.** Attaches to the dTTP-biosynthesis-block node. Supported by three independent papers (PMID:34926941, 34994281, 35346037). Proposed experiments: unbiased biochemical purification of dTMP-kinase activity from patient fibroblasts; CRISPR screen for synthetic lethality with *DTYMK* loss.
- `kind: HUMAN_MODEL_MISMATCH` — **ribonucleotide misincorporation and DDR failure are shown only in zebrafish**, never in human neurons or patient tissue; and mouse null is embryonic lethal while humans reach term. Proposed experiments: patient-iPSC cortical neurons/organoids; alkaline-gel and γH2AX assays in human cells; humanized hypomorphic knock-in mouse.
- `kind: KNOWLEDGE_GAP` — **interferon signature untested**, despite the mechanistic parallel to *RNASEH2*-deficient AGS explicitly drawn in the primary paper.
- `mechanistic_hypotheses` (`status: EMERGING`) — **mtDNA depletion arm** (Lam 2019, mitochondrial TMPK activity loss in PMID:34926941). Edges from the mitochondrial-TMPK-loss node should opt into this hypothesis group. Flag that the mtDNA depletion itself was shown "in silico" only.
- `kind: KNOWLEDGE_GAP` — **deoxynucleoside (dC/dT) substrate therapy rationale is not established for *DTYMK***, because the enzymatic block lies downstream of thymidine entry; yet NCT04802707 lists *DTYMK* as eligible.
- Inter-patient discrepancy: **cerebellar sparing (Vanoevelen) vs. cerebellar atrophy (Hernández-Carreto 2025)**.

**Suggested `biological_scale` tags for pathophysiology nodes**
`MOLECULAR` — DTYMK LoF variants; loss of homodimerization; loss of dTMP kinase activity; dTTP biosynthesis block.
`CELLULAR` — impaired DNA replication / S-phase collapse; ribonucleotide misincorporation; impaired DNA damage response; neuronal apoptosis.
`TISSUE` — cerebral and striatal atrophy with gliosis.
`ORGANISM` — progressive microcephaly; developmental regression; lactic acidemia; early childhood death.

**Module conformance candidates:** none of the existing dismech modules is a clean fit. `genome_instability_mutation` covers a genome-maintenance-defect → mutator-phenotype chain but is scoped to oncogenesis, and CONPM's output is neuronal apoptosis rather than clonal evolution — **do not force conformance.** If a module is warranted later, the natural one would be a new "nucleotide-pool-imbalance genome instability" or "replication-stress neurodegeneration" module shared with AGS/*RNASEH2*, PNKP, and the MDDS nucleotide-salvage disorders.

---

## Sources

- [DTYMK is essential for genome integrity and neuronal survival — Acta Neuropathologica (PMC8742820)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8742820/)
- [Biochemical Characterizations of Human TMPK Mutations Identified in Patients with Severe Microcephaly — ACS Omega (PMC8679000)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8679000/)
- [Deoxythymidylate kinase, DTYMK, is a novel gene for mitochondrial DNA depletion syndrome — PubMed 31271740](https://pubmed.ncbi.nlm.nih.gov/31271740/)
- [Childhood-Onset Neurodegeneration With Progressive Microcephaly (CONPM) due to a DTYMK Homozygous Pathogenic Variant — Am J Med Genet A (PMID 40696808)](https://pubmed.ncbi.nlm.nih.gov/40696808/)
- [Differential expression of enzymes in thymidylate biosynthesis in zebrafish — BMC Neuroscience](https://bmcneurosci.biomedcentral.com/articles/10.1186/s12868-022-00704-0)
- [Structural and functional analysis of human thymidylate kinase isoforms — PubMed 34994281](https://pubmed.ncbi.nlm.nih.gov/34994281/)
- [DTYMK is an essential gene in mice and heterozygosity does not cause neural tube defects — PubMed 38621447](https://pubmed.ncbi.nlm.nih.gov/38621447/)
- [Molecular characterization of Drosophila melanogaster thymidylate kinase — PubMed 38518117](https://pubmed.ncbi.nlm.nih.gov/38518117/)
- [Co-Targeting of DTYMK and PARP1 as a Potential Therapeutic Approach in Uveal Melanoma — Cells 2024](https://pubmed.ncbi.nlm.nih.gov/39195238/)
- [OMIM #619847 — NEURODEGENERATION, CHILDHOOD-ONSET, WITH PROGRESSIVE MICROCEPHALY; CONPM](https://omim.org/entry/619847)
- [OMIM \*188345 — DEOXYTHYMIDYLATE KINASE; DTYMK](https://omim.org/entry/188345)
- [MedGen — Childhood-onset neurodegeneration with progressive microcephaly (UID 1801540)](https://www.ncbi.nlm.nih.gov/medgen/1801540)
- [HPO annotations for OMIM:619847 — Human Phenotype Ontology](https://ontology.jax.org/api/network/annotation/OMIM:619847)
- [MONDO:0859241 — EBI Ontology Lookup Service](https://www.ebi.ac.uk/ols4/ontologies/mondo)
- [HGNC:3061 — DTYMK](https://rest.genenames.org/fetch/symbol/DTYMK)
- [UniProt P23919 — Thymidylate kinase](https://rest.uniprot.org/uniprotkb/P23919)
- [Human Protein Atlas — DTYMK tissue expression](https://www.proteinatlas.org/ENSG00000168393-DTYMK/tissue)
- [Alliance of Genome Resources — DTYMK orthologs](https://www.alliancegenome.org/gene/HGNC:3061)
- [ClinVar — DTYMK variants](https://www.ncbi.nlm.nih.gov/clinvar/?term=DTYMK%5Bgene%5D)
- [NCT04802707 — Deoxynucleosides Pyrimidines as Treatment for Mitochondrial Depletion Syndrome](https://clinicaltrials.gov/study/NCT04802707)