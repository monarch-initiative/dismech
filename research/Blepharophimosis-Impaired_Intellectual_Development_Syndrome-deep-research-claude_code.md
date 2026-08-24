---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-01T09:34:14.157545'
end_time: '2026-08-01T09:54:21.897148'
duration_seconds: 1207.74
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Blepharophimosis-Impaired Intellectual Development Syndrome
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
  web_search_requests: 6
  num_turns: 74
  total_cost_usd: 6.4625605
  session_id: 11125b8f-2282-4ef0-8c17-8bacb690761f
  stop_reason: end_turn
citation_count: 23
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Blepharophimosis-Impaired Intellectual Development Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Blepharophimosis-Impaired Intellectual Development Syndrome** covering all of the
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

# Blepharophimosis‑Impaired Intellectual Development Syndrome (BIS) — Comprehensive Research Report

**Prepared:** 2026‑08‑01 · **Target entity:** MONDO:0859139 · **Gene:** *SMARCA2* (hgnc:11098) · **Category:** Mendelian, autosomal dominant, ultra‑rare

> **Verification note for curators.** Quotes marked **[V]** were confirmed character‑for‑character against a cached PubMed abstract (`references_cache/PMID_32694869.md`, `references_cache/PMID_38884529.md`), against the open‑access Sarli et al. 2024 PDF read directly, or against a verbatim E‑utilities abstract fetch. Quotes marked **[V?]** were returned by a fetch layer that may have normalized whitespace — re‑run `just fetch-reference` and `just validate-references` before committing them as evidence `snippet:` values. Statements with no quote are attributed but not quotable.
>
> **NEC (Named Entity Confusion) preflight — this disease is HIGH RISK.** "Blepharophimosis–intellectual disability syndrome" is a *family* of mechanistically unrelated MONDO entities: **MONDO:0017393** (generic), **MONDO:0011365** SBBYS type (*KAT6B*), **MONDO:0010477** MKB type (*MASP1*), **MONDO:0009583** Ohdo type, **MONDO:0011432** Verloes type, **MONDO:0979360** ADNP‑related, and **MONDO:0859139** — the *SMARCA2* entity that is the subject of this report. Any deep‑research output for this disease must be gene‑checked (*SMARCA2*) and OMIM‑checked (**619293**) before use. The MONDO↔OMIM↔ORPHA identity triple was confirmed in this session (see §1).

---

## 1. Disease Information

### 1.1 Overview

Blepharophimosis‑impaired intellectual development syndrome (BIS) is a congenital, recognizable neurodevelopmental/malformation syndrome defined in 2020 by Cappuccio et al. It is caused by **de novo, non‑truncating (missense) heterozygous variants in *SMARCA2*** that cluster **outside the ATPase/helicase domains**, and it is clinically and molecularly distinct from the other *SMARCA2* disorder, **Nicolaides‑Baraitser syndrome (NCBRS, OMIM 601358)**, whose variants sit **inside** the ATPase domain.

**[V]** *"Of 20 individuals, 14 showed a recognizable phenotype with recurrent features including epicanthal folds, blepharophimosis, and downturned nasal tip along with variable degree of intellectual disability (or blepharophimosis intellectual disability syndrome [BIS])."* — Cappuccio et al., *Genet Med* 2020 (PMID:32694869; DOI 10.1038/s41436-020-0898-y)

**[V]** *"We identified a novel recognizable syndrome named BIS associated with clustered de novo SMARCA2 variants outside the helicase domains, phenotypically and molecularly distinct from NCBRS."* — PMID:32694869

**[V]** *"Blepharophimosis with intellectual disability (BIS) is a recently recognized disorder distinct from Nicolaides-Baraister syndrome that presents with distinct facial features of blepharophimosis, developmental delay, and intellectual disability."* — Sarli et al., *Am J Med Genet C* 2024 (PMID:38884529; DOI 10.1002/ajmg.c.32089)

The cardinal triad is **blepharophimosis + epicanthus + developmental delay/intellectual disability**, each present in 14/14 (100%) of the founding cohort, with a downturned/short nose, sparse eyebrows and eyelashes, thin upper lip vermilion, and broad nasal bridge completing a recognizable gestalt.

### 1.2 Identifiers

| Resource | Identifier | Notes |
|---|---|---|
| MONDO | **MONDO:0859139** | label: *blepharophimosis-impaired intellectual development syndrome*; synonym *SMARCA2-related blepharophimosis-intellectual disability syndrome* (verified via OLS4) |
| OMIM (phenotype) | **#619293** | BLEPHAROPHIMOSIS‑IMPAIRED INTELLECTUAL DEVELOPMENT SYNDROME; BIS |
| OMIM (gene) | 600014 | *SMARCA2* |
| Orphanet | **ORPHA:637013** | preferred term "SMARCA2-related blepharophimosis-intellectual disability syndrome"; disorder type **malformation syndrome** (Orphadata `rd-cross-referencing` API) |
| ICD‑10 | **Q87.0** | via Orphanet, mapping type NTBT (ORPHA narrower than ICD code) — "Congenital malformation syndromes predominantly affecting facial appearance" |
| ICD‑11 | not asserted in the retrieved Orphanet record | **gap** |
| UMLS | **C5443984** (MONDO xref) and **C5816784** (Orphanet xref) | two CUIs map to this entity — flag for mapping curation |
| MedGen | **1779966** | concept C5443984 |
| MeSH | no dedicated descriptor | indexed under *Blepharophimosis*, *Intellectual Disability*, *Transcription Factors* |
| Gene | *SMARCA2*, **hgnc:11098**, Entrez 6595, Ensembl ENSG00000080503, UniProt **P51531**, RefSeq **NM_003070**, locus **9p24.3** (HGNC REST, verified) |

### 1.3 Synonyms

- BIS
- Blepharophimosis with intellectual disability
- Blepharophimosis intellectual disability syndrome
- SMARCA2‑related blepharophimosis‑intellectual disability syndrome
- Blepharophimosis‑impaired intellectual development syndrome

**Do not use** the bare string "blepharophimosis‑intellectual disability syndrome" as an unqualified synonym — it collides with ≥5 other MONDO entities (see NEC warning).

### 1.4 Provenance of information

All information is **disease‑level aggregated** (case series + ontology/database aggregation). There is **no EHR‑derived or registry‑derived cohort** for BIS. The evidence base is essentially two publications plus database curation:

1. **Cappuccio et al. 2020** (PMID:32694869) — 20 individuals/18 families ascertained by NGS; 14 with the BIS gestalt. This is the source of the OMIM clinical synopsis and of essentially all HPO annotations.
2. **Sarli et al. 2024** (PMID:38884529) — 15 individuals with BIS‑causing *SMARCA2* variants (10 previously reported), 12 with class II *ADNP* HVDAS; episignature study.

**[V]** *"The 15 individuals with de novo missense SMARCA2 variants all had the BIS phenotype and 10 of them were previously described (Cappuccio et al., 2020)."* — Sarli et al. 2024, Results

Cumulative published BIS individuals as of mid‑2026: **≈19–20** (14 + 5 new in Sarli), plus 4 individuals labelled "BIS_atypical". This is a genuinely ultra‑rare, thinly reported entity.

---

## 2. Etiology

### 2.1 Primary cause

BIS is a **monogenic, de novo dominant** disorder. The cause is a heterozygous **non‑truncating (missense) germline variant in *SMARCA2***, arising de novo in all reported cases.

**[V]** *"In contrast to most NCBRS variants, all SMARCA2 variants associated with BIS are localized outside the helicase domains."* — PMID:32694869

There is **no known environmental, infectious, or multifactorial contribution**. No teratogen, exposure, or maternal factor has been implicated.

### 2.2 Genetic risk factors

- **Causal:** de novo missense *SMARCA2* variants in two hotspot regions (see §4).
- **Susceptibility loci:** none identified. No GWAS applies (ultra‑rare Mendelian).
- **Modifier genes:** none identified. Phenotypic variability (e.g., ambulation, speech, seizures) is unexplained; the founding cohort is too small to detect modifiers. **Explicit knowledge gap.**
- **Recurrent alleles** — the strongest genotype signal is recurrence of *the same amino acid changes in unrelated probands*, which is itself evidence of mutational hotspots at functionally constrained residues (Arg525, Arg937, Leu529, Gly513 — §4).

### 2.3 Environmental risk factors

None known. **Advanced paternal age** is a generic risk factor for de novo missense variants across NDDs and is biologically plausible here, but has **not** been specifically studied in BIS — do not curate it as a BIS risk factor without a BIS‑specific citation.

### 2.4 Protective factors

None known, genetic or environmental. Not applicable to a de novo dominant developmental disorder.

### 2.5 Gene–environment interactions

None reported. Not applicable.

---

## 3. Phenotypes

### 3.1 Frequency table — HPO annotations derived from OMIM:619293

Retrieved from the HPO/Monarch annotation API (`ontology.jax.org/api/network/annotation/OMIM:619293`). Denominators reflect Cappuccio's 14 BIS individuals (some features scored in subsets). **These n/N fractions are the single best source for dismech `frequency:` bands, and each fraction is itself the quantitative justification the frequency‑evidence SOP requires.**

#### Cardinal / obligate features (100%)

| HPO | Term | Fraction | Suggested band |
|---|---|---|---|
| HP:0000581 | Blepharophimosis | 14/14 | OBLIGATE / VERY_FREQUENT |
| HP:0000286 | Epicanthus | 14/14 | OBLIGATE / VERY_FREQUENT |
| HP:0001263 | Global developmental delay | 14/14 | OBLIGATE / VERY_FREQUENT |
| HP:0001249 | Intellectual disability | 14/14 | OBLIGATE / VERY_FREQUENT |

#### Craniofacial (the recognizable gestalt)

| HPO | Term | Fraction | % |
|---|---|---|---|
| HP:0000219 | Thin upper lip vermilion | 12/14 | 86 |
| HP:0000653 | Sparse eyelashes | 11/14 | 79 |
| HP:0045075 | Sparse eyebrow | 11/14 | 79 |
| HP:0000431 | Wide nasal bridge | 10/14 | 71 |
| HP:0045025 | Narrow palpebral fissure | 10/14 | 71 |
| HP:0002553 | Highly arched eyebrow | 10/14 | 71 |
| HP:0002263 | Exaggerated cupid's bow | 8/14 | 57 |
| HP:0002007 | Frontal bossing | 7/14 | 50 |
| HP:0000430 | Underdeveloped nasal alae | 7/14 | 50 |
| HP:0010751 | Dimple chin | 6/14 | 43 |
| HP:0012368 | Flat face | 5/14 | 36 |
| HP:0000664 | Synophrys | 4/14 | 29 |
| HP:0000322 | Short philtrum | 4/14 | 29 |
| HP:0000418 | Narrow nasal ridge | 4/14 | 29 |
| HP:0000445 | Wide nose | 4/14 | 29 |
| HP:0002209 | Sparse scalp hair | 4/14 | 29 |
| HP:0000463 | Anteverted nares | 3/14 | 21 |
| HP:0000294 | Low anterior hairline | 3/13 | 23 |
| HP:0001357 | Plagiocephaly | 3/14 | 21 |
| HP:0000154 | Wide mouth | 2/14 | 14 |
| HP:0000527 | Long eyelashes | 2/14 | 14 |
| HP:0002307 | Drooling | 2/14 | 14 |
| HP:0000574 | Thick eyebrow | 1/14 | 7 |

**Curation note:** *sparse scalp hair* is present in only 4/14 (29%) of BIS but ~97% of NCBRS — this is one of the two most discriminating features between the allelic disorders (the other being blepharophimosis, absent in NCBRS).

#### Nervous system / neurodevelopment

| HPO | Term | Fraction | % |
|---|---|---|---|
| HP:0031936 | Delayed ability to walk | 10/14 | 71 |
| HP:0000750 | Delayed speech and language development | 9/13 | 69 |
| HP:0001252 | Hypotonia | 9/12 | 75 |
| HP:0001250 | Seizure | 3/14 | 21 |
| HP:0000744 | Low frustration tolerance | 2/13 | 15 |
| HP:0033725 | Thin corpus callosum | 1/14 | 7 |
| HP:0012110 | Hypoplasia of the pons | 1/14 | 7 |
| HP:0002308 | Chiari malformation | 1/9 | 11 |
| HP:0000729 | Autistic behavior | 1/13 | 8 |
| HP:0007018 | Attention deficit hyperactivity disorder | 1/13 | 8 |
| HP:0000733 | Motor stereotypy | 1/13 | 8 |
| HP:0100025 | Overfriendliness | 1/13 | 8 |

#### Eye / vision

| HPO | Term | Fraction | % |
|---|---|---|---|
| HP:0000316 | Hypertelorism | 8/14 | 57 |
| HP:0000508 | Ptosis | 2/14 | 14 |

Sarli Table 2 (BIS column, sourced from Cappuccio 2020) additionally records **vision issue 64%**, **myopia/hypermetropia 42%**, **strabismus 14%**. OMIM's clinical synopsis lists astigmatism, hyperopia, esotropia, myopia, and cortical visual impairment. HPO terms to consider: HP:0000545 Myopia, HP:0000540 Hypermetropia, HP:0000486 Strabismus, HP:0000642 Astigmatism, HP:0100704 Cerebral visual impairment (**verify each with OAK before use — not verified in this session**).

#### Limbs, skeleton, connective tissue

| HPO | Term | Fraction | % |
|---|---|---|---|
| HP:0001182 | Tapered finger | 8/14 | 57 |
| HP:0001371 | Flexion contracture | 6/14 | 43 |
| HP:0001763 | Pes planus | 4/13 | 31 |
| HP:0010624 | Aplastic/hypoplastic toenail | 4/11 | 36 |
| HP:0002650 | Scoliosis | 3/12 | 25 |
| HP:0001382 | Joint hypermobility | 3/12 | 25 |
| HP:0001762 | Talipes equinovarus | 2/14 | 14 |
| HP:0009882 | Short distal phalanx of finger | 2/12 | 17 |
| HP:0004209 | Clinodactyly of the 5th finger | 2/14 | 14 |
| HP:0001385 | Hip dysplasia | 2/14 | 14 |
| HP:0002750 | Delayed skeletal maturation | 1/6 | 17 |

**Contrast with NCBRS:** *prominent interphalangeal joints* (84% in NCBRS) is **not** a BIS feature; BIS limb findings are contractures, tapering fingers, and foot deformity.

#### Growth (from Sarli Table 2, BIS column, "From Cappuccio et al. 2020")

| Feature | BIS % |
|---|---|
| Microcephaly | 43 |
| Low birth weight | 36 |
| Short birth length | 29 |
| Short stature (≤2 SD) | 25 |
| Macrocephaly | – (not seen) |

HPO terms: HP:0000252 Microcephaly, HP:0001518 Small for gestational age, HP:0004322 Short stature (**verify with OAK**).

#### Other systems

| HPO | Term | Fraction | % |
|---|---|---|---|
| HP:0002020 | Gastroesophageal reflux | 4/13 | 31 |
| HP:0011968 | Feeding difficulties | 2/13 | 15 |
| HP:0000028 | Cryptorchidism | 3/7 males | 43 |
| HP:0000047 | Hypospadias | 1/7 males | 14 |
| HP:0000010 | Recurrent urinary tract infections | 1/13 | 8 |
| HP:0000066 | Labial hypoplasia | 1/5 females | 20 |
| HP:0000805 | Enuresis | 1/14 | 7 |
| HP:0002837 | Recurrent bronchitis | 3/14 | 21 |
| HP:0006532 | Recurrent pneumonia | 1/14 | 7 |
| HP:0001643 | Patent ductus arteriosus | 1/13 | 8 |
| HP:0000369 | Low-set ears | 2/14 | 14 |
| HP:0000358 | Posteriorly rotated ears | 1/14 | 7 |
| HP:0006297 | Enamel hypoplasia | 1/12 | 8 |
| HP:0000689 | Dental malocclusion | 1/12 | 8 |
| HP:0000691 | Microdontia | 1/12 | 8 |

Sarli Table 2 records **GI/feeding issues 46%**, **abnormal ears 64%**, **hearing loss 0%** (a useful negative — HPO "EXCLUDED" candidate for HP:0000365 Hearing impairment), **brain abnormalities ~40%**.

### 3.2 Phenotype characteristics

- **Type mix:** predominantly **congenital physical/dysmorphic manifestations** (craniofacial, ocular adnexal, limb) plus **neurodevelopmental/behavioral** features. **No BIS‑specific laboratory abnormality exists** — there is no biochemical marker. The only laboratory‑style biomarker is the peripheral‑blood **DNA methylation episignature** (§6, §10).
- **Onset:** **congenital** for the facial gestalt and structural anomalies; developmental delay evident in infancy. HPO onset term: HP:0003577 Congenital onset (**verify**).
- **Severity:** **variable** — ID ranges from mild to severe; 35% never develop speech ("absent speech", Sarli Table 2), 30% do not achieve independent walking (inferred from 70% "delayed walking" plus OMIM's "sometimes with inability to walk").
- **Progression:** **non‑progressive / static** developmental disorder. Unlike NCBRS, there is **no report of progressive facial coarsening** (coarse face only 17% in BIS vs ~80% in NCBRS) and no neurodegeneration. Seizures, when present, are not described as intractable in BIS. Musculoskeletal features (contractures, scoliosis) may progress mechanically with growth.
- **Episodic elements:** seizures (21%) and recurrent respiratory infections (~21–50%) are the episodic components.

### 3.3 Quality‑of‑life impact

No BIS‑specific QoL instrument data exist (no EQ‑5D, SF‑36, PROMIS, or disease‑specific PRO study). **Explicit gap.** Inferred per‑phenotype impact:

| Phenotype | QoL domain affected |
|---|---|
| Intellectual disability / absent speech (35%) | communication, independence, education, lifelong care needs — dominant driver |
| Delayed/absent ambulation (~30% non‑ambulant) | mobility, self‑care |
| Blepharophimosis + ptosis + narrow fissures | visual field (if severe), social/facial recognition, potential amblyopia risk |
| Vision issues (64%) | learning, mobility |
| Feeding difficulties / GERD (46%) | nutrition, aspiration risk, caregiver burden |
| Behavioral problems (65%) | family/school functioning |
| Contractures, scoliosis, foot deformity | mobility, pain, orthopedic burden |
| Seizures (21%) | safety, medication burden |

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene

***SMARCA2*** (hgnc:11098; "SWI/SNF related BAF chromatin remodeling complex subunit ATPase 2"; aliases **BRM**, SNF2L2, hSNF2a, BAF190) at **9p24.3**, 34 exons, RefSeq **NM_003070.3**, protein **P51531**, **1,590 aa**. OMIM gene 600014.

*SMARCA2* is one of the two **mutually exclusive catalytic ATPase subunits** of the mammalian SWI/SNF (mSWI/SNF, BAF) complex; the paralog is *SMARCA4* (BRG1).

**[V]** *"Nontruncating variants in SMARCA2, encoding a catalytic subunit of SWI/SNF chromatin remodeling complex, cause Nicolaides-Baraitser syndrome (NCBRS), a condition with intellectual disability and multiple congenital anomalies."* — PMID:32694869

**[V]** *"BIS is caused by pathogenic variants in SMARCA2, that encodes the catalytic subunit of the superfamily II helicase group of the BRG1 and BRM-associated factors (BAF) forming the BAF complex, a chromatin remodeling complex involved in transcriptional regulation."* — PMID:38884529

### 4.2 Protein architecture (UniProt P51531, verified this session)

| Domain | Residues |
|---|---|
| QLQ | 173–208 |
| **HSA** (helicase/SANT‑associated; binds the actin‑related protein "Arp" module: ACTL6A/ACTB) | **436–508** |
| Helicase ATP‑binding (DExx, RecA‑like lobe 1) | **736–901** |
| Helicase C‑terminal (RecA‑like lobe 2) | 1054–1216 |
| Bromodomain | 1378–1506 |

### 4.3 The two BIS variant clusters

Per OMIM 619293's molecular genetics narrative: the BIS mutations *"clustered in 2 regions located outside of the catalytic ATPase helicase domains. Some occurred in exons 8 or 9, corresponding to a region between the HSA and helicase ATP-binding domain, whereas others occurred in exon 19, mapping to the linker region located between the DExx helicase ATP-binding and helicase C-terminal domains."* **[V?]**

Mechanistic interpretation:

**[V]** *"BIS-causing variants were found to cluster around an alpha-helix domain, that defines an interaction surface with other subunits of the BAF complex."* — Sarli et al. 2024, Introduction

### 4.4 Reported BIS variants (NM_003070.3 / P51531)

From Sarli et al. 2024 **Table 1** (read directly from the open‑access PDF; ACMG codes as published). This is the most complete public variant list for BIS.

| Protein change | cDNA | Cases | Region | ACMG codes (as published) |
|---|---|---|---|---|
| p.(Glu512Lys) | c.1534G>A | 1 | post‑HSA cluster | PS2, PS3, PM1, PP2, PM2, PM5 |
| p.(Gly513Val) | c.1538G>T | 1 | post‑HSA cluster | PS2, PS3, PM1, PP2, PM2, PM5 |
| p.(Arg525Cys) | c.1573C>T | 2 | post‑HSA cluster | PS2, PS3, PM1, PP2, PM2, PM5 |
| p.(Arg525His) | c.1574G>A | 1 | post‑HSA cluster | PS2, PS3, PM1, PP2, PM2, PM5 |
| p.(Leu529Val) | c.1585G>C | 2 (+1 validation) | post‑HSA cluster | PS2, PM1, PP2, PP3, PM2 (case 13) |
| p.(Met856Val) | c.2566A>G | 1 | ATPase lobe 1 / linker cluster | PS2, PS3, PM1, PP2, PM2, PM5 |
| p.(Arg937Cys) | c.2809C>T | 3 | lobe1–lobe2 linker | PS2, PM1, PP2, PP3, PM2, PM5 |
| p.(Arg937His) | c.2810G>A | 3 | lobe1–lobe2 linker | PS2, PM1, PP2, PP3, PM2, PM5 |
| p.(Asp510Gly) | c.6286C>A *(as printed)* | 1 (validation) | post‑HSA cluster | NA |
| **p.(Leu766Val)** | c.2296C>G | 3 | ATPase lobe 1 | NA — labelled **"BIS_atypical"** |
| **p.(Asn486Lys)** | c.1458C>A | 1 | HSA domain | NA — labelled **"BIS_atypical"** |

**Two curation cautions:**

1. **The p.(Asp510Gly) row's cDNA notation (`c.6286C>A`) is internally inconsistent** with the protein change and with the 4,773‑nt CDS implied by a 1,590‑aa protein. Treat the cDNA as a probable typographical error in the published table; cite the protein change only, or omit.
2. **p.(Met856Val) and p.(Leu766Val) fall *inside* UniProt's annotated helicase ATP‑binding domain (736–901)**, which is in tension with the paper's blanket statement that BIS variants are "outside the helicase domains." The discrepancy is a domain‑boundary definitional difference (the authors' "helicase domains" correspond to the ultra‑conserved catalytic motifs, not the full InterPro/UniProt DExx span). **Curate the "outside the helicase domain" claim as the authors' framing, and do not assert that residue 856 lies outside UniProt's DExx domain.** This is a legitimate, citable nuance — and it is precisely why p.(Leu766Val) is classified "atypical."

**Hotspot summary:** two clusters — **~486–534** (HSA C‑terminus / post‑HSA α‑helix, exons 8–9) and **~766–937** (ATPase lobe 1 and the lobe1–lobe2 linker, exon 19). **Arg525 and Arg937 are recurrent, multi‑allelic hotspot residues** (Arg→Cys and Arg→His at both), a classic signature of a constrained protein–protein interaction surface.

### 4.5 ClinVar landscape

ClinVar (`db=clinvar`, `SMARCA2[gene] AND "blepharophimosis-impaired intellectual development syndrome"[dis]`) returns **46 records**. Selected germline classifications:

| Variant | Classification | Submitted condition |
|---|---|---|
| c.1574G>A p.(Arg525His) | **Pathogenic/Likely pathogenic** | BIS |
| c.1601A>G p.(Asp534Gly) | Likely pathogenic | BIS |
| c.1390G>A p.(Glu464Lys) | Likely pathogenic | BIS |
| c.2870A>G p.(Gln957Arg) | Likely pathogenic | BIS |
| c.1874C>T p.(Pro625Leu) | Likely pathogenic | BIS |
| c.4466A>G p.(Tyr1489Cys) | Likely pathogenic | BIS |
| c.1537G>A p.(Gly513Ser) | Conflicting | BIS |
| c.1541A>G p.(Tyr514Cys) | Conflicting | BIS |
| c.2296C>G p.(Leu766Val) | **Uncertain significance** | BIS |
| c.1259G>T p.(Arg420Leu) | Uncertain significance | BIS |
| c.31C>T p.(Pro11Ser) | Benign/Likely benign | BIS |
| whole‑gene‑spanning deletion c.(-37+1_-36-1)_(3981+1_3982-1)del | Likely pathogenic | BIS |

**Critical interpretation caveat:** the ClinVar "condition" field is **submitter‑assigned**, so *any* *SMARCA2* variant submitted under the BIS condition label appears here — including benign variants and a multi‑exon deletion whose mechanism (haploinsufficiency) is **inconsistent with the published BIS missense/hotspot model**. Do **not** treat ClinVar condition labels as evidence that these variants cause BIS. Only p.(Arg525His), p.(Arg525Cys), p.(Glu512Lys), p.(Gly513Val), p.(Leu529Val), p.(Met856Val), p.(Arg937Cys/His) are literature‑anchored BIS alleles. Variants such as p.(Glu464Lys), p.(Asp534Gly), p.(Gln957Arg), p.(Pro625Leu), and p.(Tyr1489Cys) represent a **plausible but unpublished phenotypic/allelic expansion** — worth flagging as a `KNOWLEDGE_GAP` discussion, not as curated genetics.

### 4.6 Population allele frequency

All reported BIS alleles are **absent from population databases** (gnomAD/1000G/ExAC), consistent with ACMG **PM2** applied throughout Sarli Table 1. I was **unable to retrieve gnomAD constraint metrics** (pLI/LOEUF/missense Z) in this session — the gnomAD GraphQL endpoint is not reachable via plain GET. **Do not curate numeric constraint values from memory.** Fetch them separately if needed.

### 4.7 Somatic vs germline

**Germline, de novo.** Not a somatic/cancer mechanism in BIS. Note for disambiguation: *SMARCA2* is heavily studied in oncology as a **synthetic‑lethal target in SMARCA4‑deficient cancers** (PROTAC degraders — PMIDs 36357397, 36216795, 38557192, 39378885). That is mechanistically *inverse* to BIS and must not be conflated with BIS treatment (§12).

### 4.8 Functional consequence — loss of function, dominant negative, or gain of function?

The mechanism is **not simple haploinsufficiency**. Convergent lines of evidence:

1. **ClinGen dosage sensitivity curation (SMARCA2, CCID:007899, last evaluated 2013‑03‑27): haploinsufficiency score 0 ("No Evidence for Haploinsufficiency"); triplosensitivity score 0.** The curation notes that in the NCBRS/CSS papers *"in neither paper is evidence provided for a loss of function effect of the mutation"* **[V?]**, that authors invoked a *"gain of function effect of the mutant protein"* **[V?]**, that patients with **9p deletions overlapping *SMARCA2* did not present with the NCBRS phenotype**, and that *SMARCA2* knockout mice are *"viable and fertile."*
2. **All disease alleles are non‑truncating.** Truncating *SMARCA2* variants are not the established mechanism for either allelic disorder.
3. **For NCBRS**, the founding paper explicitly separates assembly from catalysis: **[V]** *"The mutations cluster within sequences that encode ultra-conserved motifs in the catalytic ATPase region of the protein. These alterations likely do not impair SWI/SNF complex assembly but may be associated with disrupted ATPase activity."* — Van Houdt et al., *Nat Genet* 2012 (PMID:22366787)
4. **For BIS**, the variant location implies the *complementary* defect: not catalysis but **complex interface integrity** — the residues sit on an α‑helix forming an interaction surface with other BAF subunits (Sarli 2024, quoted above). Cappuccio's yeast assay result supports a distinct functional class: **[V]** *"Yeast phenotype assays differentiated NCBRS from non-NCBRS SMARCA2 variants."*

**Best current model:** BIS alleles are **hypomorphic/dominant‑interfering variants that perturb BAF module assembly or subunit engagement**, whereas NCBRS alleles are **ATPase‑catalysis‑impairing** variants. Both are incorporated into complexes (hence dominant, non‑haploinsufficient behavior). **Direct biochemical proof for the BIS class — complex co‑IP, nucleosome remodeling assays, ATAC‑seq in patient‑relevant cells — has not been published. This is the single largest mechanistic gap and is a strong candidate for a `KNOWLEDGE_GAP` discussion entry.**

### 4.9 Modifier genes

None identified.

### 4.10 Epigenetic information

This is BIS's most distinctive molecular dimension, and unusually strong for so rare a disorder.

- **BIS has its own peripheral‑blood DNA methylation episignature**, distinguishable from NCBRS: **[V]** *"Transcriptomic and DNA methylation signatures differentiated NCBRS from BIS and those with nonspecific phenotype."* (PMID:32694869)
- **BIS is a clinically available EpiSign™ episignature disorder** — the London Health Sciences Centre/EpiSign conditions list includes the row **"Blepharophimosis-impaired intellectual development syndrome (BIS) — *SMARCA2* (619293)"** under "Episignature Disorders", separately from **"Nicolaides-Baraitser syndrome (NCBRS) — *SMARCA2* (601358)"** and **"Helsmoortel-van der Aa syndrome (HVDAS) — *ADNP* (615873)."** (verified by reading the EpiSign Conditions List PDF, June 2024 revision)
- **BIS shares a phenotype‑specific episignature with class II HVDAS:** **[V]** *"A distinct episignature was shared by 15 individuals with BIS-causing SMARCA2 pathogenic variants and 12 individuals with class II HVDAS caused by truncating pathogenic ADNP variants."* — PMID:38884529
- **[V]** *"This represents first evidence of a sensitive phenotype-specific episignature biomarker shared across distinct genetic conditions that also exhibit unique gene-specific episignatures."* — PMID:38884529
- **Technical parameters** (Sarli 2024, read from PDF): Illumina EPIC array; 31 individuals total (16 F/15 M); discovery n=23, validation n=4, non‑NCBRS‑non‑BIS n=4; 772,557 probes after filtering; 200 DMPs in initial selection, refined to a **final set of 239 differentially methylated CpG probes**; SVM classifier with MVP scores ~1 for cases; robustness by 20 rounds of leave‑25%‑out cross‑validation; the BIS‑HVDAS profile is **relatively hypomethylated**; highest DMP overlap with the HVDAS_C (ADNP central) cohort at **26%**; of 4 "BIS_atypical" samples only **1 (case 31, p.Asn486Lys)** clustered with the BIS‑HVDAS positives.
- **Paralog convergence at the methylation level:** an independent cohort found *"common episignatures affecting homologous residues in highly conserved paralogous proteins (SMARCA2 M856V and SMARCA4 M866V)"* **[V]** — Levy/Ciaccio et al., *HGG Adv* 2024 (PMID:38751117). This is direct evidence that the BIS Met856 allele and its *SMARCA4* paralogous counterpart converge on one epigenomic consequence — excellent support for a shared‑mechanism pathophysiology node.

### 4.11 Chromosomal abnormalities

Not a mechanism for BIS. **Distinguish carefully from 9p24.3/9p deletion syndromes**, which delete *SMARCA2* among many genes and produce a *different* phenotype (see PMIDs 41137173, 40196253, 41995485, 40836298 for contemporary 9p deletion cohorts). This distinction is itself the key argument against haploinsufficiency (§4.8).

---

## 5. Environmental Information

- **Environmental factors:** none known. No toxicant, radiation, pollutant, or occupational exposure implicated.
- **Lifestyle factors:** none. Not applicable to a de novo germline dominant disorder.
- **Infectious agents:** none causal. Recurrent bronchitis (21%) and pneumonia (7%) are **secondary complications** — plausibly related to hypotonia, GERD, and aspiration — not etiologic agents.

**Section 5 is genuinely "not applicable" for BIS. Do not populate speculative environmental content.**

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (proposed pathograph for dismech)

```
[MOLECULAR] De novo missense SMARCA2 variant in one of two hotspot clusters
            (HSA-adjacent α-helix ~486–534; ATPase lobe1/linker ~766–937)
                    │
                    ▼
[MOLECULAR] Altered SMARCA2 interaction surface with partner BAF subunits
            (α-helix at the inter-subunit interface; HSA-proximal Arp-module contact)
            → perturbed BAF (mSWI/SNF) complex assembly / subunit engagement,
              WITHOUT haploinsufficiency and WITHOUT the catalytic-motif lesion of NCBRS
                    │
                    ▼
[MOLECULAR] Impaired ATP-dependent nucleosome remodeling by BRM-containing BAF
            (GO:0140658 ATP-dependent chromatin remodeler activity ↓/ABNORMAL;
             GO:0006338 chromatin remodeling ABNORMAL)
                    │
                    ▼
[MOLECULAR] Altered chromatin accessibility at BAF-dependent enhancers/promoters
            → BIS-specific transcriptomic signature AND BIS-specific
              genome-wide DNA methylation episignature in peripheral blood
                    │
                    ▼
[CELLULAR]  Dysregulated BAF-dependent transcriptional programs in neural
            progenitors and differentiating neurons (npBAF→nBAF subunit switching;
            GO:0071564 npBAF complex)
                    │
                    ▼
[TISSUE]    Abnormal CNS development (thin corpus callosum, pontine hypoplasia,
            Chiari malformation in a minority; ~40% any brain abnormality)
            AND abnormal craniofacial / periocular morphogenesis
            (blepharophimosis, epicanthus, narrow palpebral fissures, nasal shape)
                    │
                    ▼
[ORGANISM]  Global developmental delay, intellectual disability, hypotonia,
            delayed/absent speech and ambulation, behavioral phenotype,
            recognizable facial gestalt, contractures/foot deformity,
            feeding difficulties/GERD, seizures (21%)
```

**Convergent parallel arm (shared final common pathway, well supported):**

```
Truncating ADNP variant in the bipartite nuclear localization (BNL) domain (class II HVDAS)
   → mutant ADNP retains/loses nuclear import but cannot recruit BAF
   → same disruption of BAF chromatin-remodeling output
   → SHARED phenotype-specific episignature + overlapping narrow-palpebral-fissure craniofacial phenotype
```

**[V]** *"We speculate that class II ADNP variants and BIS-causing SMARCA2 variants disrupt the chromatin remodeling activity of the BAF complexes, thus explaining their functional overlap."* — Sarli et al. 2024, Discussion

**[V]** *"ADNP was found to bind directly to SMARCA2, SMARCA4, and SMARCC2 through its C-terminal end (Helsmoortel et al., 2014)."* — Sarli et al. 2024, citing PMID reference to Helsmoortel et al. 2014

Sarli's Discussion also notes the mechanistic hypothesis that mutant ADNP *"still binds to the DNA, but is no longer capable of recruiting the BAF complex, leading to diminished functionality of the complex and ultimately to deregulation of several genes"* **[V?]**.

### 6.2 Molecular pathways

- **mSWI/SNF (BAF) ATP‑dependent chromatin remodeling** — the sole primary pathway. Not a signaling cascade disorder (no Wnt/MAPK/mTOR/PI3K primary lesion). Reactome/KEGG coverage of SWI/SNF is thin; the authoritative mechanistic reviews are *Nucleus* 2023 "Mechanism of action of the SWI/SNF family complexes" (PMID:36633435) and the cryo‑EM structural literature.
- **Downstream:** BAF‑dependent transcriptional regulation by RNA polymerase II at enhancers; neural progenitor proliferation/differentiation programs.

### 6.3 Cellular processes

- **Chromatin remodeling and nucleosome repositioning** at BAF target loci.
- **Neural progenitor self‑renewal → neuronal differentiation transition.** BAF subunit switching is the canonical mechanism: **[V?]** *"these subunits are replaced by the homologous BAF45b, BAF45c, and BAF53b"* as progenitors differentiate, and blocking the switch impairs neuronal differentiation — Lessard et al., *Neuron* 2007 (PMID:17640523). UniProt's function annotation for P51531 likewise records participation in *"neural development transitions between stem/progenitor and postmitotic states."*
- **Cell‑cycle control** — BRM loss impairs G0/G1 arrest in response to confluency or DNA damage (Reyes et al. 1998, PMID:9843504). Relevance to BIS neurodevelopment is plausible but unproven.
- **Not implicated:** apoptosis‑centric, autophagy, inflammasome, or fibrotic mechanisms. No `conforms_to` fit with the fibrotic/senescence/hallmark modules.

### 6.4 Protein dysfunction

Altered **protein–protein interaction surface** rather than misfolding, aggregation, or catalytic‑site destruction. The BIS α‑helix cluster is predicted to sit at a BAF inter‑subunit interface. This places BIS squarely within the framework of Valencia et al.'s pan‑BAF structural analysis:

**[V?]** *"Whereas mutations within the SMARCA2 helicase cause NCBRS, SMARCA2 mutations outside of this domain are implicated in a distinct disorder, blepharophimosis-impaired intellectual disability syndrome."* — Valencia et al., *Nat Genet* 2023;55:1400–1412 (PMID:37500730, PMC10412456)

Valencia et al. establish that BAF‑complex genes *"harbor the greatest number of de novo missense and protein-truncating variants among nuclear protein complexes"* and that non‑truncating NDD variants *"cluster in four key structural regions associated with high disease severity, including mSWI/SNF-nucleosome interfaces, the ATPase-core ARID-armadillo repeat (ARM) module insertion site, the Arp module and DNA-binding domains."* **[V?]** The BIS HSA‑adjacent cluster is topologically consistent with the **Arp‑module interface** arm of that framework (the HSA helix engages ACTL6A/ACTB). *Note: Valencia et al. is a structural/computational analysis — it reports no wet‑lab assay of the specific BIS alleles.*

Newer BAF structural biology worth tracking for mechanism: a SWI/SNF‑specific Ig‑like domain ("SWIFT") acting as a transcription‑factor binding platform, *Science* 2026 (PMID:41477818).

### 6.5 Metabolic changes

**None known.** BIS is not a metabolic disorder; there is no enzyme deficiency, no accumulating metabolite, no metabolomic signature. Do not model against `metabolic_intoxication_decompensation` or `lysosomal_substrate_accumulation`.

### 6.6 Immune system involvement

No primary immune mechanism. Recurrent bronchitis/pneumonia are best explained by hypotonia/aspiration rather than immunodeficiency; no immunologic workup abnormality is reported. Do not curate an immunodeficiency claim.

### 6.7 Tissue damage mechanisms

Not a tissue‑injury disorder — the pathology is **developmental (morphogenetic and neurodevelopmental)**, not degenerative. No oxidative stress, ischemia, fibrosis, or necrosis mechanism.

### 6.8 Biochemical abnormalities

None measurable clinically. No enzyme assay, receptor assay, or ion‑channel defect. The measurable molecular abnormality is epigenomic (methylation array), not biochemical.

### 6.9 Molecular profiling

| Modality | Status in BIS |
|---|---|
| **Transcriptomics** | Performed on **blood leukocytes** in the founding study; a BIS transcriptomic signature distinguishes BIS from NCBRS **[V]** (PMID:32694869). No tissue‑level or neural transcriptome exists. |
| **DNA methylation / epigenomics** | Strongest data; see §4.10. EPIC array, 239‑probe classifier, clinically deployed via EpiSign. |
| **Proteomics** | None for BIS. General BAF proteomics (Lessard 2007; Mashtalir et al.) informs the mechanism only. |
| **Metabolomics / lipidomics** | None. Not expected to be informative. |
| **Single‑cell / spatial transcriptomics** | **None for BIS.** A high‑value gap — single‑cell analysis of BAF‑dependent programs in human neural progenitors and periocular/craniofacial neural crest would directly test the mechanism. |
| **Functional genomics (CRISPR/RNAi)** | No BIS‑allele‑specific screen. *SMARCA2* appears in DepMap as a **paralog‑dependency** node in SMARCA4‑mutant lines — cancer context, not BIS. |
| **AI/multimodal diagnostics** | *"Artificial intelligence-driven genotype-epigenotype-phenotype approaches to resolve challenges in syndrome diagnostics"* — *EBioMedicine* 2025 (PMID:40280028) — relevant because BIS is defined by a recognizable gestalt **plus** an episignature, the exact combination such models exploit. |

### 6.10 Suggested ontology terms for the pathograph

**Verified in this session via OLS4:**

| Term | ID | Use |
|---|---|---|
| chromatin remodeling | **GO:0006338** | ABNORMAL on the remodeling node |
| ATP‑dependent chromatin remodeler activity | **GO:0140658** | molecular_functions, DECREASED/ABNORMAL |
| SWI/SNF superfamily‑type complex | **GO:0070603** | cellular component anchor |
| npBAF complex | **GO:0071564** | neural progenitor BAF specialization |
| neural progenitor cell | **CL:0011020** | cell_types |
| eyelid | **UBERON:0001711** | anatomical site of blepharophimosis |

**Plausible but NOT verified this session — run `just validate-terms` before use:** GO:0006357 (regulation of transcription by RNA polymerase II), GO:0030182 (neuron differentiation), GO:0007399 (nervous system development), GO:0071565 (nBAF complex), CL:0000681 (radial glial cell — verified label in the CL search above), UBERON:0000955 (brain), UBERON:0002336 (corpus callosum), UBERON:0000988 (pons), CHEBI:15422 (ATP).

---

## 7. Anatomical Structures Affected

### 7.1 Organ level

**Primary:**
- **Central nervous system** — global developmental delay/ID (100%), hypotonia (75%), seizures (21%), structural brain anomalies in ~40% (thin corpus callosum, pontine hypoplasia, Chiari malformation each ~1/14).
- **Periocular / eyelid and adnexal structures** — blepharophimosis (100%), narrow palpebral fissures (71%), epicanthus (100%), ptosis (14%), sparse eyelashes (79%).
- **Craniofacial skeleton and soft tissue** — nasal bridge/alae/tip, philtrum, upper lip vermilion, chin, forehead, ears (64%).

**Secondary / variable:**
- Musculoskeletal — contractures (43%), tapering fingers (57%), pes planus (31%), talipes equinovarus (14%), scoliosis (25%), hip dysplasia (14%), toenail hypoplasia (36%).
- Gastrointestinal — GERD (31%), feeding difficulties (15%).
- Respiratory — recurrent bronchitis (21%), pneumonia (7%) (secondary).
- Genitourinary — cryptorchidism (43% of males), hypospadias (14% of males), labial hypoplasia.
- Cardiovascular — patent ductus arteriosus (1/13) — **isolated report; not an established BIS feature.**
- Dentition — enamel hypoplasia, malocclusion, microdontia (each ~1/12 in BIS; note that dental disease is far more prominent in *SMARCA2*‑related epilepsy cohorts overall, 52.8%, which are ATPase‑domain/NCBRS‑weighted).

**Body systems:** nervous, visual/ocular adnexal, musculoskeletal, digestive, genitourinary, integumentary (hair/nails), respiratory (secondary).

**Notably spared:** hearing (0% hearing loss in BIS vs 32% in HVDAS — a useful discriminator); no hepatic, renal‑parenchymal, endocrine, or hematologic involvement reported.

### 7.2 Tissue and cell level

Because the lesion is in a broadly expressed chromatin remodeler, the affected cell populations are inferred from BAF developmental biology rather than measured in BIS tissue:

- **Neural progenitor cells / radial glia** (CL:0011020, CL:0000681) — npBAF‑dependent proliferation.
- **Postmitotic differentiating neurons** — nBAF‑dependent maturation, dendritic outgrowth.
- **Cranial neural crest–derived mesenchyme and periocular mesenchyme** — the presumed substrate for the blepharophimosis/epicanthus/nasal phenotype. **This is an inference: no BIS study has examined periocular or neural‑crest tissue. Flag as a `HUMAN_MODEL_MISMATCH`/`KNOWLEDGE_GAP` rather than asserting it.**
- **Eyelid epithelium and tarsal plate** (UBERON:0003844/0003845, UBERON:0004773/0004774) — anatomically implicated by the phenotype.

### 7.3 Subcellular level

- **Nucleus** (primary compartment; UniProt: nucleus, also localizes to sites of DNA damage).
- **Chromatin / nucleosome** — the functional substrate.
- **SWI/SNF superfamily‑type complex (GO:0070603)** and **npBAF complex (GO:0071564)** as the molecular machines.

### 7.4 Localization and lateralization

**Bilateral and symmetric.** Blepharophimosis, epicanthus, narrow palpebral fissures, contractures, and foot deformities are described bilaterally. **Plagiocephaly (21%)** is the only asymmetric craniofacial finding recorded. No lateralized/unilateral pattern is reported.

---

## 8. Temporal Development

### 8.1 Onset

- **Congenital.** Facial gestalt, epicanthus, blepharophimosis, and structural anomalies are present at birth. Low birth weight (36%) and short birth length (29%) indicate **prenatal** onset of the growth phenotype.
- **Onset pattern:** insidious recognition of the neurodevelopmental component during infancy; delayed walking and delayed speech become apparent in the first 1–3 years.
- **Prenatal detectability:** limited. No BIS‑specific prenatal ultrasound signature exists. For orientation only, a fetus with a de novo *SMARCA2* pathogenic variant presented with **caudal regression, sacral agenesis, and congenital vertical talus** (PMID:38877377, *Prenat Diagn* 2024) — but that report frames the findings as an expansion of the **NCBRS** spectrum, not BIS. **Do not attribute caudal regression to BIS.**

### 8.2 Progression

- **Course: static / non‑progressive** developmental disorder with a **chronic, lifelong** duration.
- **Stages:** no formal staging system exists or is appropriate.
- **Rate:** not applicable — developmental trajectory, not degeneration.
- **Ages reported:** Sarli's BIS subjects spanned **1 to 17.5 years**; the oldest published individuals are adolescents/young adults. **There is no adult natural‑history data at all.** Whether the BIS facial gestalt evolves with age (as NCBRS coarsening does) is **unknown** — a concrete, high‑value gap, and a point of practical diagnostic importance since gestalt recognition drives ascertainment.
- **Distinguishing feature vs NCBRS:** BIS shows only 17% coarse facies vs ~80% in NCBRS, and no reported progressive coarsening; BIS seizures (21%) are neither as frequent nor as refractory as NCBRS epilepsy (65%, "often difficult to manage" per GeneReviews).

### 8.3 Patterns

- **Remission:** none; not applicable.
- **Critical periods:** (a) **embryonic/fetal craniofacial and CNS morphogenesis** — the window in which the malformation phenotype is determined and therefore **not** therapeutically accessible postnatally; (b) **infancy–early childhood** — the actionable window for early intervention, feeding/GERD management, and amblyopia prevention; (c) **growth years** — contracture, scoliosis, and foot‑deformity surveillance.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

- **Prevalence: no published estimate.** The Orphanet epidemiology endpoint returned no prevalence record for ORPHA:637013 in this session; MONDO/OMIM carry none.
- **Reported cases: ≈19–20 published individuals** (14 in Cappuccio 2020 + 5 new in Sarli 2024), plus 4 "BIS_atypical". By any reasonable reading this is **ultra‑rare**, i.e. `CASES_IN_LITERATURE` with `prevalence_class: NOT_YET_DOCUMENTED` or `ULTRA_RARE` in dismech terms. **Do not fabricate a numeric rate.**
- For calibration, the allelic disorder is itself vanishingly rare: **[V?]** *"The prevalence of SMARCA2-NCBRS is not known, but is estimated to be extremely low. Fewer than 100 affected individuals have been described."* — GeneReviews, *SMARCA2‑Related Nicolaides‑Baraitser Syndrome* (NBK321516)
- **Incidence:** unknown; not estimable.
- **Ascertainment bias:** BIS is diagnosed by exome/genome sequencing in syndromic NDD cohorts, then gestalt‑confirmed. It is almost certainly **under‑diagnosed**, because (i) the gestalt was only described in 2020, (ii) non‑ATPase‑domain *SMARCA2* missense variants would previously have been called VUS, and (iii) episignature testing that resolves them is not universally available.

### 9.2 Inheritance genetics

| Parameter | BIS |
|---|---|
| **Pattern** | **Autosomal dominant** (HP:0000006), de novo in all reported cases |
| **Penetrance** | Presumed **complete** for de novo pathogenic hotspot variants; no unaffected carrier reported. No incomplete‑penetrance evidence exists — but with n≈20 and 100% de novo ascertainment, penetrance is effectively **untested**. |
| **Expressivity** | **Variable** — ID severity, ambulation, speech acquisition, seizures, and skeletal involvement all vary among carriers of the *same* recurrent allele (e.g., three individuals with p.Arg937His). This intra‑allelic variability is itself notable and unexplained. |
| **Anticipation** | Not applicable (no repeat expansion). |
| **Germline/gonadal mosaicism** | Not reported in BIS. By analogy, GeneReviews notes for NCBRS that sib recurrence risk is elevated only if parental gonadal mosaicism is suspected. Treat mosaicism as theoretically possible, undocumented. |
| **Founder effects** | None. |
| **Consanguinity** | No role (dominant, de novo). |
| **Carrier frequency** | Not applicable. |
| **Recurrence risk** | Empirically ~0 for siblings of a proband with a confirmed de novo variant (standard low residual risk for undetected parental mosaicism, conventionally quoted ~1%); **50% for the offspring** of an affected individual, though no reproduction by an affected individual has been reported. |

### 9.3 Population demographics

- **Ethnic/geographic distribution:** The founding cohort was ascertained across **Italy, France, UK, Portugal, Czech Republic, Netherlands, Japan, Canada, USA**; Sarli added Turin, Milan, Rome, Caen, Dijon, Coimbra, Birmingham, Manchester, Oxford, Tokyo, and Greenwood SC. There is **no evidence of ethnic or geographic clustering** — the distribution reflects the geography of the collaborating clinical‑genetics networks, not disease biology.
- **Variant geography:** none. Recurrent alleles (Arg525, Arg937) recur across unrelated families in different countries, consistent with independent de novo mutational hotspots rather than shared ancestry.
- **Sex ratio:** approximately balanced. Sarli's 15 BIS individuals were **8 female / 7 male**; the founding HPO denominators imply 7 males and 5 females scored for sex‑specific features. **No sex bias; no X‑linked or sex‑limited component.**
- **Age distribution of affected individuals:** children and adolescents (1–17.5 years reported). Adults are absent from the literature — an ascertainment artifact of a 2020 disease definition, not evidence of reduced survival.

---

## 10. Diagnostics

### 10.1 Diagnostic strategy (recommended pathway)

1. **Clinical recognition** of the gestalt: blepharophimosis + epicanthus + narrow palpebral fissures + sparse eyebrows/eyelashes + broad nasal bridge + short nose with downturned tip + thin upper lip + DD/ID.
2. **Exome or genome sequencing** (or a comprehensive ID/NDD gene panel including *SMARCA2*) — the route used in the founding cohort: **[V]** *"By next-generation sequencing, we identified candidate variants in SMARCA2 in 20 individuals from 18 families with a syndromic neurodevelopmental disorder not consistent with NCBRS."*
3. **Variant localization** — determine whether the missense variant falls in a BIS hotspot (outside the catalytic ATPase motifs, in the HSA‑adjacent α‑helix ~486–534 or the lobe1/linker region ~766–937) vs an NCBRS ATPase‑motif position. **Domain position is the primary genotype–phenotype discriminator.**
4. **Trio testing** to establish de novo status (ACMG PS2 — applied to every BIS variant in Sarli Table 1).
5. **Episignature testing (EpiSign™)** for VUS resolution and confirmation. BIS is an explicitly listed EpiSign episignature disorder (*SMARCA2*, OMIM 619293), distinct from the NCBRS entry.

### 10.2 Genetic testing modalities

| Modality | Utility for BIS |
|---|---|
| **WES** | **High** — primary diagnostic route; all reported cases found by NGS. |
| **WGS** | High; adds non‑coding/structural resolution but no BIS‑specific advantage. |
| **Multigene ID/NDD panels** | Useful if *SMARCA2* is included. *SMARCA2* is a Genomics England PanelApp gene on the Intellectual disability panel. |
| **Single‑gene *SMARCA2* sequencing** | Reasonable when the gestalt is recognized; must cover the full CDS, not only ATPase exons (historic NCBRS‑focused assays may have targeted the helicase region). |
| **Chromosomal microarray** | **Low yield for BIS**, but essential to *exclude* 9p24.3/9p deletion syndromes, which overlap in gene content but not phenotype. |
| **Karyotype / FISH** | Not indicated. |
| **mtDNA testing** | Not indicated. |
| **Repeat expansion testing** | Not indicated. |
| **Prenatal / postnatal targeted testing** | Targeted testing for a known familial variant is feasible; de novo prenatal diagnosis of BIS is not currently practicable on ultrasound findings alone. |

### 10.3 Omics‑based diagnostics

- **Epigenomics — clinically actionable.** Genome‑wide methylation (Illumina EPIC) episignature analysis, delivered as EpiSign™, is the one omics assay in routine diagnostic use for BIS. It resolves *SMARCA2* VUS and separates BIS from NCBRS. **Caveat to curate: BIS and class II HVDAS share the phenotype‑specific episignature (PMID:38884529), so a positive BIS‑HVDAS signature is not by itself gene‑specific — it must be interpreted alongside the sequencing result.**
- **Transcriptomics** — used as a research‑grade discriminator in the founding study (blood leukocytes); not a routine clinical test.
- **Proteomics / metabolomics / liquid biopsy** — no role.

### 10.4 Variant‑interpretation tooling

A **gene‑specific machine‑learning pathogenicity predictor** has been developed using *SMARCA2* and *SMARCA4* NDD variants — reported accuracy **0.93** on holdout data for the gene‑specific model and **0.91** for the generalized BAF‑subunit predictor, outperforming generic tools; the authors emphasize *"gene-specific calibration of predictors"* (Reilly et al., *HGG Adv* 2026, PMID:41764075; preprint PMID:41000737). This is directly relevant to reclassifying the numerous *SMARCA2* VUS submitted under the BIS condition label (§4.5).

### 10.5 Non‑genetic clinical tests

There is **no diagnostic biochemical, imaging, or electrophysiologic test for BIS.** The following are **management/complication assessments**, not diagnostics:

| Test | Purpose | Expected findings |
|---|---|---|
| **Brain MRI** | Structural assessment | Normal in ~60%; thin corpus callosum, pontine hypoplasia, or Chiari malformation each in ~1/14 |
| **EEG** | If seizures suspected | Seizures in 21%; BAF‑complex disorders more broadly associated with *"slow background activity on EEG"* (PMID:42528014) |
| **Ophthalmologic exam** | Blepharophimosis, ptosis, refractive error, strabismus, amblyopia risk | vision issue 64%, refractive error 42%, strabismus 14%, ptosis 14% |
| **Audiologic assessment** | Baseline (standard NDD care) | hearing loss **0%** in BIS |
| **Swallow study / pH‑impedance** | Feeding difficulty, GERD | GI/feeding issues 46% |
| **Skeletal survey / spine and hip imaging** | Contractures, scoliosis, hip dysplasia | contractures 43%, scoliosis 25% |
| **Dental evaluation** | Enamel/eruption anomalies | uncommon in BIS; prominent in *SMARCA2* epilepsy cohorts overall (52.8%) |
| **Developmental / cognitive assessment** | Severity, service eligibility | ID 100%, absent speech 35% |
| **Biopsy / histopathology** | **No role.** No characteristic tissue pathology exists. |

### 10.6 Clinical criteria and differential diagnosis

**No formal consensus diagnostic criteria exist for BIS** (as is also true for NCBRS per GeneReviews). Diagnosis = suggestive gestalt + de novo non‑truncating *SMARCA2* variant at a hotspot position, ideally with episignature support.

**Differential diagnosis — the discriminating features that matter:**

| Condition | Gene(s) | MONDO | Discriminators from BIS |
|---|---|---|---|
| **Nicolaides‑Baraitser syndrome** | *SMARCA2* (ATPase domain) | — (OMIM 601358) | Allelic. NCBRS: sparse scalp hair 97%, prominent interphalangeal joints 84%, coarse facies ~80%, epilepsy 65% often refractory, progressive coarsening. BIS: blepharophimosis 100% (absent in NCBRS), sparse hair only 29%, seizures 21%, no progressive coarsening. **Distinct episignature; distinct yeast‑assay behavior.** |
| **Helsmoortel‑Van der Aa syndrome, class II** | *ADNP* (BNL‑domain truncating) | MONDO:0979360 (ADNP‑related BIS) | **Shares the episignature and narrows the palpebral fissures.** Distinguishers: HVDAS has downslanting palpebral fissures (33%) and hearing loss (32%), autism ~67%, sleep disturbance 65%; BIS has 0% hearing loss and no downslanting fissures. **Sequencing is required to separate them — the methylation biomarker cannot.** |
| **Ohdo syndrome, SBBYS variant** | *KAT6B* | MONDO:0011365 | Blepharophimosis + ID + patellar hypoplasia, long thumbs/great toes, dental anomalies, hypothyroidism. |
| **Ohdo syndrome, MKB (Maat‑Kievit‑Brunner) type** | *MASP1* | MONDO:0010477 | X‑linked; 3MC spectrum features. |
| **Blepharophimosis‑ID, Verloes type / Ohdo type** | unresolved | MONDO:0011432 / MONDO:0009583 | Historic clinical entities; molecularly undefined — a frequent source of literature confusion. |
| **Sifrim‑Hitz‑Weiss syndrome** | *CHD4* | — | Short palpebral fissures + ID + congenital anomalies; *ADNP* interacts with *CHD4* (noted in Sarli's Discussion). |
| **Coffin‑Siris syndrome 1–4** | *ARID1B, ARID1A, SMARCB1, SMARCA4* | — | BAFopathy sibs; 5th‑digit/nail hypoplasia, hypertrichosis rather than sparse hair. |
| **Blepharophimosis‑ptosis‑epicanthus inversus syndrome (BPES)** | *FOXL2* | — | Eyelid phenotype **without** ID; premature ovarian insufficiency in type I. |
| **Baraitser‑Winter syndrome** | *ACTB, ACTG1* | — | Ptosis, iris/retinal coloboma, pachygyria; *ACTB* is an **Arp‑module BAF subunit**, so mechanistic proximity is real. |
| **Kabuki syndrome** | *KMT2D, KDM6A* | — | Long palpebral fissures with everted lower lids — the opposite eyelid morphology. |
| **9p24.3 / distal 9p deletion syndrome** | contiguous, incl. *SMARCA2* | — | CNV, not missense; different phenotype; **the key argument against *SMARCA2* haploinsufficiency.** |

### 10.7 Screening

- **Newborn screening:** not applicable and not appropriate (no treatable metabolic component; no NBS assay).
- **Carrier screening:** not applicable (de novo dominant).
- **Cascade screening:** not applicable for de novo variants; would apply only to the offspring of an affected individual.
- **Reverse‑phenotyping screening:** the practically useful "screen" is **retrospective re‑analysis of unsolved NDD cohorts for non‑ATPase‑domain *SMARCA2* missense variants**, followed by episignature confirmation — the approach that generated the entity in the first place.

---

## 11. Outcome / Prognosis

### 11.1 Survival and mortality

- **No mortality data exist for BIS.** No deaths are reported among the ~20 published individuals.
- **Life expectancy: unknown, presumed not markedly shortened** in the absence of severe epilepsy or major organ malformation. There is **no** cardiac, renal, hepatic, or oncologic component to drive excess mortality. Recurrent respiratory infections (21–50%) and aspiration risk from feeding difficulty/GERD (46%) are the plausible mortality contributors in the most severely affected, non‑ambulant subset — **by analogy with severe NDDs generally, not from BIS data.**
- **5‑/10‑year survival, disease‑specific mortality:** not applicable / not measured. **Do not populate numeric survival fields.**

### 11.2 Morbidity and function

- **Dominant morbidity is neurodevelopmental disability:** ID 100%; absent speech 35%; non‑ambulant ~30%; behavioral problems 65%. Most affected individuals will require **lifelong support**, with a substantial minority (those with absent speech and no independent ambulation) requiring **full‑time care**.
- **Secondary morbidity:** orthopedic (contractures 43%, scoliosis 25%), nutritional/GI (46%), ophthalmologic (64%), respiratory infections.
- **Quality‑of‑life instruments:** none administered. ICF‑based functional outcome data: none. **Explicit gap.**

### 11.3 Disease course and complications

Chronic, stable, lifelong. Complications to anticipate: aspiration pneumonia, failure to thrive, amblyopia/uncorrected refractive error, progressive contracture and scoliosis with growth, seizure emergence, dental disease, behavioral escalation in adolescence. **Recovery potential: none — this is a static developmental disorder.** Function improves with development and intervention; the underlying chromatin lesion is not reversible.

### 11.4 Prognostic prediction

- **Best candidate prognostic factor: variant position.** In the allelic disorder this is established — **[V?]** *"All individuals with a pathogenic variant within the C-terminal helicase region of the ATPase domain have severe intellectual disability and epilepsy, a frequency higher than that in individuals with pathogenic variants in other parts of the gene."* (GeneReviews NBK321516, NCBRS). **For BIS specifically, no intra‑BIS genotype–severity correlation has been established** — indeed three individuals sharing p.Arg937His differ phenotypically, arguing that variant identity alone is insufficient. **Curate this as an open question, not as a correlation.**
- **Prognostic biomarkers:** none. The episignature is diagnostic, **not** prognostic — MVP score has no demonstrated relationship to severity.
- Practical early prognostic indicators (severity of hypotonia, age at walking, speech acquisition by age 3, seizure onset) are generic NDD predictors, not BIS‑validated.

---

## 12. Treatment

**There is no disease‑modifying or targeted therapy for BIS. Management is entirely supportive, anticipatory, and multidisciplinary.** No published BIS‑specific management guideline exists; the closest applicable framework is the GeneReviews management section for *SMARCA2*‑related NCBRS, which states that no cure exists and care is supportive and multidisciplinary.

### 12.1 Supportive / rehabilitative management (the core of care)

| Intervention | Indication in BIS | Suggested NCIT `treatment_term` | `therapeutic_modality` |
|---|---|---|---|
| Early intervention / developmental therapy | DD/ID 100% | NCIT:C15315 Rehabilitation | BEHAVIORAL |
| Physical therapy | Hypotonia 75%, delayed walking 71%, contractures 43% | **NCIT:C15302** Physical Therapy | BEHAVIORAL |
| Occupational therapy | Fine motor, ADLs, hand contractures | **NCIT:C121351** Occupational Therapy | BEHAVIORAL |
| Speech and language therapy / AAC | Speech delay 69%, absent speech 35% | **NCIT:C159273** Speech Therapy | BEHAVIORAL |
| Nutritional support / feeding management | Feeding difficulty 15%, GERD 31%, poor growth | **NCIT:C15433** Nutritional Support | (determine per agent — do **not** auto‑tag BEHAVIORAL) |
| Anti‑seizure medication | Seizures 21% | **NCIT:C15986** Pharmacotherapy | SMALL_MOLECULE |
| Ophthalmologic correction (refraction, amblyopia therapy, ptosis/blepharophimosis surgery where visual axis is compromised) | Vision issue 64%, ptosis 14% | NCIT:C15329 Surgical Procedure / NCIT:C49236 Therapeutic Procedure | SURGERY / DEVICE |
| Orthopedic management (orthoses, serial casting, tenotomy, scoliosis and clubfoot surgery) | Contractures, talipes 14%, scoliosis 25%, hip dysplasia 14% | **NCIT:C16186** Orthopedic Surgical Procedure | SURGERY |
| Dental care | Enamel/eruption anomalies | NCIT:C15747 Supportive Care | — |
| Behavioral / ADHD / autism support | Behavioral problems 65% | NCIT:C181743 Behavioral Counseling | BEHAVIORAL |
| Genetic counseling | Recurrence risk, family planning | **NCIT:C15240** Genetic Counseling | BEHAVIORAL |
| Supportive care (general) | Multisystem | **NCIT:C15747** Supportive Care | — |

*NCIT IDs above are drawn from the dismech‑vetted list in CLAUDE.md; verify NCIT:C15315, C49236, C181743 with OAK before use.*

### 12.2 Pharmacotherapy specifics

- **Anti‑seizure medications:** no BIS‑specific evidence. Extrapolatable data: in a *SMARCA2*‑related epilepsy cohort (24 own + 46 literature cases, mostly ATPase‑domain variants), **seizure control was achieved in 45.8% using valproate or levetiracetam** (PMID:40513420, *Seizure* 2025). GeneReviews likewise notes levetiracetam and valproic acid often show initial response in NCBRS. **Curate this as extrapolated, NCBRS/ATPase‑weighted evidence, not BIS evidence** — BIS epilepsy is both rarer (21%) and apparently milder.
- **Pharmacogenomics:** no BIS‑specific PGx. Standard CPIC guidance applies to the drugs used (e.g., *HLA‑B\*15:02*/carbamazepine, *CYP2C9*/phenytoin) — general practice, not disease‑specific.

### 12.3 Advanced therapeutics — status: none, and one important negative

- **Gene therapy / gene editing:** none. Conceptually challenging: the phenotype is largely **prenatal and morphogenetic** (craniofacial structure is fixed before birth), and the mechanism is a **dominant‑interfering missense allele in a broadly required chromatin regulator** — allele‑specific silencing (ASO/siRNA against the mutant allele) is the only theoretically coherent modality, and no such program exists.
- **ASOs / siRNA / mRNA:** none. Note *SMARCA2* has no ASO program; the mechanism does not fit any of the three FDA‑approved ASO paradigms cleanly (there is no splice lesion and no accumulating toxic transcript in the usual sense).
- **Cell therapy, immunotherapy:** not applicable.
- **⚠ Critical negative to record — SMARCA2 degraders are NOT a BIS therapy.** Multiple clinical programs target **SMARCA2 for degradation** in *SMARCA4*‑deficient cancers (NCT06560645 PRT7732, terminated; NCT05639751 PRT3789, completed; NCT06682806, terminated; NCT06561685 LY4050784; NCT07284186 PLX‑61639; preclinical PMIDs 36357397, 36216795, 38557192, 39378885, 40280558, 41184243). **These reduce SMARCA2 and would be expected to be harmful, not helpful, in a SMARCA2‑opathy.** An automated pipeline mining "SMARCA2 + drug" will surface these; they must be explicitly excluded from BIS treatment curation.

### 12.4 Trials and registries

No interventional trial for BIS exists. Relevant observational studies that may enroll BIS individuals:
- **NCT01793168** — Rare Disease Patient Registry & Natural History Study (CoRDS, Sanford), recruiting, observational.
- **NCT04463316** — "GROWing Up With Rare GENEtic Syndromes", recruiting, observational.

### 12.5 Treatment outcomes, adverse events, algorithms

- **Response rates:** none reported (no trials).
- **Adverse events:** those of the individual supportive interventions; nothing BIS‑specific.
- **Algorithms / combination therapy / genotype‑guided treatment:** none exist. **Explicit gap** — a BIS management guideline is an unmet need, and the NCBRS GeneReviews surveillance schedule (growth, seizures, development at each visit; dental review at least every 6 months) is the best available proxy.

---

## 13. Prevention

### 13.1 Prevention levels

- **Primary prevention: not possible.** De novo germline missense variants are not preventable. No modifiable exposure exists.
- **Secondary prevention (early detection and intervention):** the actionable level. Early molecular diagnosis via ES/GS in infants with DD + blepharophimosis enables early intervention, feeding/GERD management, amblyopia prevention, and avoids the diagnostic odyssey. **Episignature testing shortens time‑to‑diagnosis for *SMARCA2* VUS.**
- **Tertiary prevention (complication avoidance):** the practical mainstay — aspiration prevention (feeding/GERD management), amblyopia prevention (refractive correction, ptosis surgery where the visual axis is obstructed), contracture and scoliosis prevention (PT, orthoses, positioning), seizure control, dental prophylaxis, nutritional optimization.

### 13.2 Immunization

No disease‑specific vaccine. **Routine immunization is important and should be emphasized**, given recurrent bronchitis (21%) and pneumonia (7%) — including influenza and pneumococcal vaccination per standard schedules for children with neurodisability.

### 13.3 Screening and reproductive options

- **Population screening:** none; not justified for an ultra‑rare de novo disorder.
- **Genetic counseling:** indicated for every family. Key messages: (i) the variant is de novo, (ii) sibling recurrence risk is very low (residual risk for undetected parental gonadal mosaicism, conventionally ~1%), (iii) offspring risk for an affected individual is 50%.
- **Prenatal testing / PGT:** technically available for a known familial variant (relevant only in the theoretical case of a transmitting affected parent, or for reassurance in a subsequent pregnancy). **PGT‑M is not indicated for a proven de novo variant** other than at parental request.
- **Risk stratification:** not applicable.

### 13.4 Behavioral, public health, environmental interventions, prophylaxis

Not applicable to etiology. The only public‑health‑relevant lever is **access to exome/genome sequencing and to episignature testing** in NDD diagnostic pathways — a health‑systems issue, not an environmental one. No prophylactic medication is indicated.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** *Homo sapiens* (**NCBITaxon:9606**) is the only species in which BIS occurs. BIS is a human clinical entity defined by a human gestalt.
- **Breed (VBO):** not applicable. No breed‑associated *SMARCA2* disorder is known.
- **Orthologous genes:** mouse ***Smarca2*** (**MGI:99603**, verified via MGI), with orthologs across vertebrates (rat, zebrafish *smarca2*), and the deeply conserved yeast ortholog ***SNF2*** in *Saccharomyces cerevisiae* — the ortholog that made the founding functional assay possible. Retrieve NCBI Gene IDs for non‑human orthologs before curating them; I verified only the mouse MGI ID in this session.
- **Naturally occurring animal disease:** **none reported.** No OMIA entry for a *SMARCA2* Mendelian disorder in a domestic species. **BIS has no natural animal counterpart.**
- **Veterinary relevance:** none.
- **Comparative pathology:** the informative comparison is *negative* and mechanistically important — **mouse *Smarca2*/Brm null animals do not model BIS or NCBRS**: **[V?]** *"BRM-/- mice develop normally, suggesting that an observed up-regulation of the BRG1 protein can functionally replace BRM."* (Reyes et al., *EMBO J* 1998, PMID:9843504). ClinGen's dosage curation cites exactly this — *SMARCA2* knockout mice are "viable and fertile" — as evidence against a loss‑of‑function mechanism.
- **Evolutionary conservation:** very high. The ATPase/helicase motifs are described as **"ultra-conserved"** (Van Houdt 2012 **[V]**), and BAF/SWI‑SNF architecture is conserved from yeast Snf2 to human BRM/BRG1 — the basis for the yeast complementation strategy. Separately, the human **paralogs *SMARCA2*/*SMARCA4* converge at homologous residues** (M856V/M866V, shared episignature; PMID:38751117), evidence of conserved residue‑level function within the paralog pair.
- **Zoonotic potential / cross‑species susceptibility:** not applicable (genetic disorder).

---

## 15. Model Organisms

### 15.1 Yeast (*Saccharomyces cerevisiae*) — the model that defined BIS

The **only model system with published, BIS‑allele‑specific data.** Cappuccio et al. expressed the human variants in the context of the yeast Snf2 ortholog and used growth/phenotype assays as a functional stratifier:

**[V]** *"To stratify variant interpretation, we functionally analyzed SMARCA2 variants in yeasts and performed transcriptomic and genome methylation analyses on blood leukocytes."*

**[V]** *"Yeast phenotype assays differentiated NCBRS from non-NCBRS SMARCA2 variants."*

Structural inference from the yeast Snf2 homolog placed the mutated BIS residues on an α‑helix at the SWI/SNF inter‑subunit interface **[V]** (Sarli 2024 Introduction, summarizing Cappuccio 2020).

- **Strengths:** deep conservation of the Snf2 ATPase; tractable, quantitative, scalable; directly discriminated the two disease classes — exactly the assay a variant‑classification pipeline needs.
- **Limitations:** yeast has no nervous system, no eyelids, no craniofacial development, and lacks the metazoan BAF subunit repertoire (no ADNP, no BAF45/53 paralog switching, no cBAF/PBAF/ncBAF diversification). It can report on **catalysis and complex integrity**, not on **phenotype**. Curate yeast results as `evidence_source: IN_VITRO` (or `OTHER` for a heterologous‑organism assay) — **not** as evidence for human phenotypes.

### 15.2 Mouse (*Mus musculus*) — available but non‑recapitulating

- Gene: ***Smarca2***, MGI:99603. **10 mutant alleles** across endonuclease‑mediated (5), targeted (4), and gene‑trapped (1) categories (MGI, verified).
- Reported mutant phenotype systems: behavior/neurological, growth/body size, homeostasis/metabolism, muscle physiology, reproductive system. MGI notes homozygotes for a targeted mutation "may exhibit infertility and a slightly increased body weight in some genetic backgrounds."
- Founding characterization (Reyes et al. 1998, PMID:9843504): **null mice develop normally** with BRG1 upregulation compensating; adults ~**15% heavier**; increased hepatic mitotic index; mutant embryonic fibroblasts **[V?]** *"deficient...ability to arrest in the G0/G1 phase of the cell cycle in response to cell confluency or DNA damage."*
- **Phenotype recapitulation: poor to absent.** No mouse shows blepharophimosis, ID, or the BIS craniofacial gestalt. **No knock‑in mouse carrying a BIS hotspot allele (e.g., Arg525His, Arg937His, Met856Val) has been reported.**
- **This is a textbook `HUMAN_MODEL_MISMATCH`, not a `KNOWLEDGE_GAP`:** model‑organism evidence exists (Smarca2‑null mice), but its translational validity is the open question — because the null does not model a dominant‑interfering missense allele, and BRG1 compensation in mouse may not mirror human BRM/BRG1 dosage relationships. The obvious resolving experiment is a **conditional knock‑in of a BIS hotspot allele** with craniofacial and neurodevelopmental phenotyping.

### 15.3 Human cellular models

- **Patient peripheral blood leukocytes** — the substrate for both the BIS transcriptomic and DNA methylation signatures (Cappuccio 2020; Sarli 2024). Accessible, clinically validated, but **not the affected tissue** — an inherent limitation: a blood episignature is a surrogate readout of chromatin dysregulation, not a measure of neural or periocular pathobiology.
- **iPSC‑derived neurons / neural progenitors / organoids:** **none reported for BIS.** This is the highest‑value missing model. A BAF‑relevant precedent exists in the MorPhiC framework (iPSC‑derived multicellular systems, null alleles, `category: Cellular` phenotypes, `evidence_source: IN_VITRO`), but *SMARCA2* is not among the flagged MorPhiC anchor genes (ISL1, EOMES, GCM1, NKX2‑1) and no MorPhiC *SMARCA2* dataset was identified.
- **Cell lines / biochemical reconstitution:** extensive *SMARCA2* biochemistry exists in the **cancer** literature (degrader pharmacology, SMARCA4‑deficient synthetic lethality). None of it interrogates BIS alleles. Reconstituted BAF complexes with BIS variants — testing assembly, ACTL6A/Arp‑module engagement, nucleosome remodeling, and ATPase activity — is the missing biochemistry.

### 15.4 Zebrafish, *Drosophila*, *C. elegans*

- **Zebrafish** *smarca2* ortholog exists; **no BIS model reported.** Zebrafish would be a reasonable system for craniofacial/neural‑crest patterning readouts.
- ***Drosophila*** *brm* is the founding family member and the source of the name "brahma"; classic developmental genetics, but **no BIS allele modeling.**
- ***C. elegans*** — not used.

### 15.5 Model resources

MGI (informatics.jax.org, MGI:99603), IMPC/KOMP/IMSR for *Smarca2* allele availability, ZFIN for *smarca2*, FlyBase for *brm*, SGD for *SNF2*, Alliance of Genome Resources for cross‑species integration, Cellosaurus/ATCC for cell lines.

### 15.6 Research applications and the honest bottom line

Existing models can address: BAF catalytic mechanism (yeast, biochemistry), BAF subunit switching in neural development (mouse, Lessard 2007), and variant classification (yeast assay, ML predictors). **No existing model addresses the two questions that matter most for BIS: why these specific interface variants cause blepharophimosis, and what the dominant‑interfering allele does to BAF function in human neural and periocular tissue.**

---

## Appendix A — Reference list with verification status

| PMID / ID | Citation | Role | Cache status |
|---|---|---|---|
| **32694869** | Cappuccio G, Sayou C, Tanno PL, et al. De novo SMARCA2 variants clustered outside the helicase domain cause a new recognizable syndrome with intellectual disability and blepharophimosis distinct from Nicolaides-Baraitser syndrome. *Genet Med* 2020;22(11):1838‑1850. DOI 10.1038/s41436-020-0898-y | **Founding / defining publication** | ✅ cached, abstract verbatim available |
| **38884529** | Sarli C, van der Laan L, Reilly J, et al. Blepharophimosis with intellectual disability and Helsmoortel-Van Der Aa Syndrome share episignature and phenotype. *Am J Med Genet C* 2024;196(4):e32089. DOI 10.1002/ajmg.c.32089 | Episignature; variant table; phenotype frequencies; open access (CC BY) | ✅ cached, abstract verbatim; full text read |
| 22366787 | Van Houdt JKJ, et al. Heterozygous missense mutations in SMARCA2 cause Nicolaides-Baraitser syndrome. *Nat Genet* 2012 | NCBRS mechanism; ATPase‑motif clustering | verbatim abstract retrieved; **needs `just fetch-reference`** |
| 37500730 | Valencia AM, Sankar A, van der Sluijs PJ, et al. Landscape of mSWI/SNF chromatin remodeling complex perturbations in neurodevelopmental disorders. *Nat Genet* 2023;55:1400‑1412 (PMC10412456) | BAF structural framework; explicit BIS vs NCBRS statement | **needs fetch** |
| 38751117 | DNA methylation analysis in patients with neurodevelopmental disorders improves variant interpretation and reveals complexity. *HGG Adv* 2024 (PMC11216013) | SMARCA2 M856V / SMARCA4 M866V paralog episignature convergence | verbatim abstract retrieved; **needs fetch** |
| 40513420 | Genotype and phenotype correlation in epilepsy patients with SMARCA2 variants. *Seizure* 2025;131:73‑83 | SMARCA2 epilepsy (ATPase‑weighted); ASM response | **needs fetch**; quotes **[V?]** only |
| 17640523 | Lessard J, et al. An essential switch in subunit composition of a chromatin remodeling complex during neural development. *Neuron* 2007;55:201‑15 | npBAF→nBAF switching | **needs fetch** |
| 9843504 | Reyes JC, Barra J, Muchardt C, et al. Altered control of cellular proliferation in the absence of mammalian brahma (SNF2alpha). *EMBO J* 1998;17:6979‑91 | Brm‑null mouse; model mismatch | **needs fetch** |
| 42528014 | Genotypic and Phenotypic Profile of 50 Cases With Chromatin Remodeling Complexes-Related Neurological Disorders. *CNS Neurosci Ther* 2026 | BAF vs CHD clinical patterns | **needs fetch** |
| 41764075 / 41000737 | Gene-specific pathogenicity predictor for chromatin remodeling BAF complex-associated NDDs. *HGG Adv* 2026 / bioRxiv 2025 | SMARCA2/4 VUS classification, acc. 0.93/0.91 | **needs fetch** |
| 40280028 | AI-driven genotype-epigenotype-phenotype approaches to resolve challenges in syndrome diagnostics. *EBioMedicine* 2025 | gestalt + episignature diagnostics | **needs fetch** |
| 36633435 | Mechanism of action of the SWI/SNF family complexes. *Nucleus* 2023 | mechanism review | **needs fetch** |
| 41477818 | A SWI/SNF-specific Ig-like domain, SWIFT, is a transcription factor binding platform. *Science* 2026 | current BAF structural biology | **needs fetch** |
| 38877377 | Caudal regression in fetus with de novo SMARCA2 pathogenic variant. *Prenat Diagn* 2024 | prenatal; **framed as NCBRS spectrum, not BIS** | **needs fetch**; use with caution |
| 34521483 | Nicolaides-Baraitser syndrome in a patient with hypertrophic cardiomyopathy and SMARCA2 gene deletion. *Cardiol Young* 2022;32:821‑823 | complicates the deletion/haploinsufficiency picture | **needs fetch** |
| NBK321516 | GeneReviews®: *SMARCA2*-Related Nicolaides-Baraitser Syndrome | NCBRS comparator; prevalence; management; genotype‑phenotype | not a PMID — cite as GeneReviews/Bookshelf |
| ORPHA:637013 | Orphanet, *SMARCA2-related blepharophimosis-intellectual disability syndrome* | identifiers, ICD‑10 Q87.0, disorder type | ⚠ **no ORPHA_637013 cache exists in this repo** — run `just structured-rebuild-orphanet --id 637013` |
| OMIM 619293 | BLEPHAROPHIMOSIS-IMPAIRED INTELLECTUAL DEVELOPMENT SYNDROME; BIS | clinical synopsis; two‑cluster variant narrative | omim.org returns 403 to automated fetch; text obtained indirectly — **treat the exon 8/9 + exon 19 sentence as [V?]** |
| — | HPO/Monarch annotation API, `OMIM:619293` | all n/14 phenotype frequencies | retrieved directly ✅ |
| — | EpiSign™ Conditions List (London Health Sciences Centre, rev. June 2024) | BIS as a clinically available episignature disorder | PDF read directly ✅ |
| — | ClinGen Dosage Sensitivity, *SMARCA2*, CCID:007899 (eval. 2013‑03‑27) | HI score 0; anti‑haploinsufficiency argument | consider ingesting as `CGDS:HGNC_11098` via `just clingen-dosage-rebuild` |
| NCT01793168, NCT04463316 | CoRDS registry; GROWing Up With Rare GENEtic Syndromes | observational enrollment options | fetch via `just fetch-reference NCT…` |

## Appendix B — Prioritized knowledge gaps (candidate `discussions` entries)

1. **`KNOWLEDGE_GAP` — mechanism of the BIS allele class.** No biochemical assay of BIS variants on BAF assembly, Arp‑module engagement, nucleosome remodeling, or ATPase activity. `attaches_to` the interface/remodeling nodes. Proposed experiments: co‑IP/mass spec of BAF from BIS‑variant cells; in vitro reconstitution + remodeling assay; ATAC‑seq/CUT&RUN in isogenic knock‑ins.
2. **`KNOWLEDGE_GAP` — why blepharophimosis?** No mechanistic account links *SMARCA2* interface variants to periocular/eyelid morphogenesis. Nothing is known about BRM function in periocular neural crest.
3. **`HUMAN_MODEL_MISMATCH` — mouse *Smarca2* null is viable, fertile, and normal‑appearing**, so it cannot model a dominant‑interfering missense allele; BRG1 compensation may not translate. Resolving experiment: BIS hotspot knock‑in mouse.
4. **`KNOWLEDGE_GAP` — no adult natural history.** All reported individuals are ≤17.5 years. Unknown whether the gestalt evolves, whether new complications emerge, and what adult function/QoL look like.
5. **`KNOWLEDGE_GAP` — intra‑BIS genotype–phenotype correlation.** Three individuals share p.Arg937His yet differ phenotypically; no severity predictor exists, and no modifier has been sought.
6. **`KNOWLEDGE_GAP` — allelic/phenotypic expansion outside ClinVar's literature.** Several *SMARCA2* variants classified Likely pathogenic for BIS in ClinVar (p.Glu464Lys, p.Asp534Gly, p.Gln957Arg, p.Pro625Leu, p.Tyr1489Cys) sit outside the two published clusters and are unpublished. Do the clusters need redefining, or are these mislabeled?
7. **Data‑quality flags:** (a) the p.(Asp510Gly)/`c.6286C>A` inconsistency in Sarli Table 1; (b) UniProt places p.Met856Val and p.Leu766Val *inside* the annotated helicase ATP‑binding domain (736–901), in tension with "outside the helicase domains"; (c) two UMLS CUIs (C5443984, C5816784) map to MONDO:0859139.
8. **Diagnostic caveat worth curating explicitly:** the BIS episignature is **phenotype‑specific, not gene‑specific** — it is shared with class II *ADNP* HVDAS, so a positive result requires sequencing to assign the gene.

---

**Sources:**
- [Cappuccio et al. 2020, *Genetics in Medicine* (PMID:32694869)](https://pubmed.ncbi.nlm.nih.gov/32694869/) · [publisher](https://www.nature.com/articles/s41436-020-0898-y)
- [Sarli et al. 2024, *Am J Med Genet C* (PMID:38884529)](https://onlinelibrary.wiley.com/doi/10.1002/ajmg.c.32089) · [open-access PDF](https://iris.unito.it/bitstream/2318/2027350/2/217_Blepharophimosis%20with%20ID%20%20Helsmoortel%E2%80%90Van%20Der%20Aa_2024.pdf)
- [Van Houdt et al. 2012, *Nature Genetics* (PMID:22366787)](https://pubmed.ncbi.nlm.nih.gov/22366787/)
- [Valencia et al. 2023, *Nature Genetics* (PMID:37500730 / PMC10412456)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10412456/)
- [DNA methylation analysis in NDDs, *HGG Advances* 2024 (PMID:38751117)](https://pubmed.ncbi.nlm.nih.gov/38751117/)
- [Genotype and phenotype correlation in epilepsy patients with SMARCA2 variants, *Seizure* 2025 (PMID:40513420)](https://pubmed.ncbi.nlm.nih.gov/40513420/)
- [Lessard et al. 2007, *Neuron* (PMID:17640523)](https://pubmed.ncbi.nlm.nih.gov/17640523/)
- [Reyes et al. 1998, *EMBO J* (PMID:9843504)](https://pubmed.ncbi.nlm.nih.gov/9843504/)
- [SMARCA2-Related Nicolaides-Baraitser Syndrome, GeneReviews (NBK321516)](https://www.ncbi.nlm.nih.gov/books/NBK321516/)
- [OMIM #619293](https://omim.org/entry/619293) · [MedGen C5443984](https://www.ncbi.nlm.nih.gov/medgen/1779966) · [Monarch MONDO:0859139](https://monarchinitiative.org/MONDO:0859139)
- [Orphadata cross-referencing API, ORPHA:637013](https://api.orphadata.com/rd-cross-referencing/orphacodes/637013?lang=en)
- [HPO annotation API, OMIM:619293](https://ontology.jax.org/api/network/annotation/OMIM:619293)
- [UniProt P51531](https://rest.uniprot.org/uniprotkb/P51531.json) · [HGNC:11098](https://rest.genenames.org/fetch/symbol/SMARCA2) · [MGI:99603](https://www.informatics.jax.org/marker/MGI:99603)
- [ClinGen Dosage Sensitivity, SMARCA2](https://search.clinicalgenome.org/kb/gene-dosage/SMARCA2)
- [EpiSign Conditions List (June 2024)](https://episign.com/wp-content/uploads/2024/06/EpiSign-Conditions-List.pdf)
- [ClinicalTrials.gov API v2](https://clinicaltrials.gov/) · [Genomics England PanelApp, SMARCA2](https://panelapp.genomicsengland.co.uk/panels/285/gene/SMARCA2/)