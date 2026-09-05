---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-14T13:38:22.784401'
end_time: '2026-08-14T13:54:08.257756'
duration_seconds: 945.48
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cartilage-hair hypoplasia
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
  web_search_requests: 3
  num_turns: 41
  total_cost_usd: 4.575767000000001
  session_id: f8dcf781-66f0-4858-ba6a-582539c47d04
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 24
reference_validation:
  total_references: 63
  verified: 63
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cartilage-hair hypoplasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Cartilage-hair hypoplasia** covering all of the
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

I'll research this now.

sup Harry — dug into this one properly. Below's the full report. One thing up front that matters a lot for dismech: **I've marked which abstracts I have verbatim vs. which I only have summarized.** The little fetch model quote-marks its own paraphrases, and those are exactly the fake-looking-real snippets that pass a vibe check and fail `just count-verified-snippets`. Anything in the "paraphrase only" bucket needs a `just fetch-reference` before it becomes a `snippet:`.

---

# Cartilage-Hair Hypoplasia (CHH) — Comprehensive Research Report

**Prepared:** 2026-08-14 · **Target KB entry:** `kb/disorders/Cartilage-Hair_Hypoplasia.yaml`

---

## 0. Evidence-verification status (read this first)

I pulled abstracts through Europe PMC. These I have **verbatim and safe to quote**:

| PMID | Short handle |
|---|---|
| 11207361 | Ridanpää 2001 *Cell* — gene discovery |
| 31379817 | Vakkilainen 2019 *Front Immunol* — 30-yr follow-up, mortality |
| 30410491 | Vakkilainen 2018 *Front Immunol* — autoimmunity/allergy |
| 35115551 | Robertson 2022 *Nat Commun* — ribosomopathy |
| 31551465 | Vakkilainen 2019 *Sci Rep* — G2 cell-cycle delay |
| 31237961 | Sun 2019 *JBMR* — zebrafish *rmrp* model |
| 28126377 | Aubert 2017 *JACI* — telomere biology |
| 33675005 | Vakkilainen 2021 *J Clin Immunol* — lung imaging |
| 32849667 | Vakkilainen 2020 *Front Immunol* — live vaccines |
| 20375313 | Bordon 2010 *Blood* — EBMT HSCT cohort |
| 42170584 | Vakkilainen 2025 *J Hum Immun* — comprehensive review |

These I have **paraphrase only — re-fetch before quoting**: 18698627, 17701897, 16252239, 16254002, 18804272, 24009312, 25764362, 8444246, 11391344, 37115363, 38862721, 34956076, 38676846, 38187867, 22420014 (GeneReviews — a book chapter, not abstract-shaped anyway).

Ontology IDs below are **suggestions**. Every one needs `just validate-terms` before it lands. I flag the shakier ones explicitly.

---

## 1. Disease Information

### Overview

Cartilage-hair hypoplasia is what happens when you break the cell's ribosome factory in a way that's bad but not lethal. It's an autosomal recessive, multi-system disorder in which a single non-protein-coding RNA gene — *RMRP* — is disabled, and the fallout lands hardest on the tissues that need to divide fastest: growth-plate cartilage, hair follicles, the T-cell compartment, and the erythroid line. Hence the four-part clinical signature: short-limbed short stature, fine sparse hair, combined immunodeficiency, and macrocytic anemia. Layered on top are Hirschsprung disease, autoimmunity, and a genuinely alarming lymphoma risk.

The 2025 review states it cleanly (**verbatim, PMID:42170584**):

> "Cartilage-hair hypoplasia (CHH) is a rare syndromic inborn error of immunity, caused by variants in the noncoding RNA gene RMRP. The effects of RMRP deficiency are pleiotropic, affecting the ribosomal RNA processing, cell cycle, and gene regulation. Typical clinical manifestations of CHH include chondrodysplasia with short stature, hair hypoplasia, combined immunodeficiency, and anemia. In addition, individuals with CHH have increased prevalence of malignancies, Hirschsprung's disease, and autoimmunity. The only curative option for immunodeficiency or severe anemia in CHH remains hematopoietic stem cell transplantation."

Historically it's McKusick's disease — described in 1965 in the Old Order Amish of Lancaster County, Pennsylvania (PMID:14284412, *"DWARFISM IN THE AMISH. II. CARTILAGE-HAIR HYPOPLASIA"*).

### Identifiers

| Resource | ID | Confidence |
|---|---|---|
| MONDO | **MONDO:0009595** — "cartilage-hair hypoplasia" | **Verified via OLS4 this session** |
| OMIM | 250250 (CHH) | High |
| OMIM | *157660 (*RMRP* gene) | Medium — verify |
| OMIM | 607095 (Anauxetic dysplasia 1) | Medium — verify |
| OMIM | 250460 (Metaphyseal dysplasia without hypotrichosis) | Medium — verify |
| Orphanet | ORPHA:175 | High (Orphanet blocked my fetch — cite via the cached `ORPHA:175` structured source instead) |
| ICD-10 | Q78.5 (Metaphyseal dysplasia) | Medium |
| ICD-11 | **VERIFY** — I could not confirm | Low |
| UMLS | C0175787 | Medium — verify |
| HGNC | **HGNC:10031** (*RMRP*) → dismech form `hgnc:10031` | Medium — verify |

MONDO exact synonyms confirmed from OLS4: *cartilage hair hypoplasia*, *metaphyseal chondrodysplasia, McKusick type*, *autosomal recessive metaphyseal chondrodysplasia*, *McKusick Type Metaphyseal Chondrodysplasia*. Related: *CHH*.

Other names in the wild: metaphyseal chondrodysplasia McKusick type, McKusick-type metaphyseal dysplasia, CHH.

**Sibling entities worth their own dismech entries or a `Grouping`:**
- **Anauxetic dysplasia 1** (*RMRP*, severe end of the same allelic spectrum)
- **Metaphyseal dysplasia without hypotrichosis / MDWH** (*RMRP*, mild end)
- **Anauxetic dysplasia 2** (*POP1*, PMID:27380734) — same holoenzyme, different subunit
- **Anauxetic dysplasia 3** (*NEPRO*, PMID:31250547, PMID:37294112) — likewise

There's a real modeling decision here: GeneReviews treats MDWH–CHH–AD as one **"CHH–AD spectrum"** (PMID:22420014). Given dismech's lump/split conventions, the cleanest shape is probably a separate `Cartilage-Hair_Hypoplasia` entry plus a `Grouping` (`grouping_basis: SHARED_GENE_FAMILY` + `SHARED_MECHANISM`) covering the RNase MRP holoenzyme disorders, with `POP1`/`NEPRO` entries as future members. Flagging it, not deciding it.

### Data provenance

Nearly everything quantitative comes from **aggregated disease-level cohort studies**, not EHR. The Finnish national CHH cohort (Helsinki; Mäkitie, Taskinen, Vakkilainen) is the dominant source — ~80–123 genetically confirmed patients followed prospectively since 1985, cross-linked to the Finnish Cancer Registry and national Cause-of-Death Registry. That's why the epidemiology is unusually good for a disease this rare, and also why you should treat the numbers as **Finnish-founder-population numbers** rather than universal ones.

---

## 2. Etiology

### Primary cause

Biallelic pathogenic variants in ***RMRP*** (9p13.3), which encodes the ~267–268 nt non-coding RNA subunit of the **RNase MRP** ribonucleoprotein. It's an RNA polymerase III transcript — no protein product, ever. This is the historically important bit: *RMRP* was the first nuclear non-coding RNA gene tied to a human disease (**verbatim, PMID:31551465**: *"RMRP was the first non-coding nuclear RNA gene implicated in a disease."*).

Ridanpää's original *Cell* paper, **verbatim (PMID:11207361)**:

> "The recessively inherited developmental disorder, cartilage-hair hypoplasia (CHH) is highly pleiotropic with manifestations including short stature, defective cellular immunity, and predisposition to several cancers. The endoribonuclease RNase MRP consists of an RNA molecule bound to several proteins. It has at least two functions, namely, cleavage of RNA in mitochondrial DNA synthesis and nucleolar cleaving of pre-rRNA. We describe numerous mutations in the untranslated RMRP gene that cosegregate with the CHH phenotype. Insertion mutations immediately upstream of the coding sequence silence transcription while mutations in the transcribed region do not. The association of protein subunits with RNA appears unaltered. We conclude that mutations in RMRP cause CHH by disrupting a function of RNase MRP RNA that affects multiple organ systems."

That last sentence is a genuinely good dismech evidence snippet for a top-level pathophysiology node.

### Genetic risk factors

Not a susceptibility-locus disease — it's straight Mendelian recessive. Two functional classes of allele:

1. **Transcribed-region variants** (e.g. n.71A>G, the big one) — the RNA is made but works badly.
2. **Promoter insertions/duplications** — transcription is knocked down or silenced. Ridanpää: *"Insertion mutations immediately upstream of the coding sequence silence transcription while mutations in the transcribed region do not."* Tan 2023 (PMID:37115363) showed homozygous promoter duplications cause severely reduced transcript abundance and, notably, **SCID-level** immunodeficiency.

No established modifier genes. No GWAS loci. Carriers are asymptomatic and — worth stating explicitly for counseling — **not at increased cancer risk** (GeneReviews, PMID:22420014). The one hint of a heterozygote effect is biochemical, not clinical: Aubert found telomerase activity varied by *gene dose* between carriers and patients (**verbatim, PMID:28126377**: *"telomerase activity is affected in a gene dose-dependent manner when comparing heterozygote RMRP carriers with patients with CHH."*).

### Environmental risk factors

None established for **causation** — this is a fully penetrant genetic disease. But there are real environmental *modifiers of outcome*, and dismech should model them as `influences_mechanisms` with `environmental_effect: EXACERBATES` rather than as causes:

- **Varicella-zoster exposure** — potentially fatal in CHH with significant cellular immunodeficiency; historically a named cause of death. Prompts the "immediate high-dose IV acyclovir" rule.
- **Live attenuated vaccines**, especially oral poliovirus — vaccine-associated paralytic poliomyelitis in a CHH child is one of the oldest reports in the literature (PMID:165279, 1975, *"Combined immunodeficiency and vaccine-related poliomyelitis in a child with cartilage-hair hypoplasia"*). Note this is now nuanced — see §13.
- **UV exposure** — a plausible modifier of the basal-cell / squamous-cell carcinoma excess, though I found no CHH-specific dose-response study. Treat as inferred, not evidenced.
- **Respiratory pathogen burden** — recurrent pneumonia is one of the strongest mortality predictors (§11).

### Protective factors

- **Consanguinity avoidance / outbreeding** in founder populations — mechanically obvious, no CHH-specific study.
- No protective alleles reported.
- No dietary or lifestyle protective factor with evidence. Growth hormone specifically does **not** help (GeneReviews: *"no sustained benefit, not recommended"*).

### Gene–environment interaction

The clean, well-evidenced one: **genotype sets immune competence, and immune competence sets the consequence of pathogen and vaccine exposure.** Vakkilainen 2020 (PMID:32849667) is the direct test — live viral vaccines turned out to be tolerated in Finnish CHH patients with mild/absent clinical immunodeficiency, with no serious adverse events across 40 MMR and 10 VZV recipients, while remaining contraindicated at the SCID end. That's a genotype→immune-phenotype→exposure-outcome chain, and it's exactly the shape dismech's `influences_mechanisms` slot wants.

---

## 3. Phenotypes

Frequencies below are mostly from GeneReviews (PMID:22420014) and the Finnish cohorts. **Every `frequency:` you curate needs its own quantitative snippet** — most of these come from the GeneReviews summary rather than from a quotable abstract sentence, so per the frequency-evidence SOP, omit the band rather than manufacture support.

### Skeletal (near-universal)

| Phenotype | Suggested HP | Freq | Notes |
|---|---|---|---|
| Disproportionate short-limb short stature | HP:0003026 (Short long bone) / HP:0008873 (Disproportionate short-limb short stature) | 100% | Recognizable at birth, sometimes prenatally |
| Metaphyseal dysplasia | HP:0002980 (Femoral bowing) + HP:0000944 (Abnormal metaphysis morphology) | 100% (75/75 with films, PMID:25764362) | Flaring, cupping, marginal serration, fragmentation, scalloping; cystic radiolucencies extending into diaphysis |
| Genu varum / bowed legs | HP:0002970 (Genu varum) | 87% (85/96) | Commonest reason for orthopaedic referral |
| Short metacarpals/phalanges, "short pudgy hands" | HP:0010049 (Short metacarpal) | 100% | Bullet-shaped middle phalanges; cone-shaped epiphyses |
| Joint hypermobility | HP:0001382 (Joint hypermobility) | 100% | Rarely symptomatic |
| Limited elbow extension | HP:0001377 (Limited elbow extension) | 81% (56/69) | Radial head subluxation/dislocation; *"not a single patient had any issues of consequence"* |
| Coxa vara | HP:0002812 (Coxa vara) | 27% (19/71) | |
| Lumbar lordosis | HP:0002938 (Lumbar hyperlordosis) | common | Rarely needs treatment |
| Scoliosis | HP:0002650 (Scoliosis) | variable | Observation → bracing → fusion |
| Atlantoaxial instability | HP:0003318? **VERIFY** — better: HP:0003468 (Atlantoaxial instability) | AD >> CHH | Prominent in anauxetic dysplasia; PMID:25764362 found no surgical cases in 12 CHH C-spines |

**Adult height** (PMID:25764362, n=135): males median **131.1 cm** (110.7–149.0), females median **122.5 cm** (103.7–137.4). GeneReviews gives the spectrum range as 104–151 cm for CHH, versus **<85 cm** for anauxetic dysplasia. Growth: short at birth, further deceleration in the first 2 years, and a *"very weak or absent pubertal growth spurt."* Model this as `clinical_course: PROGRESSIVE` on a growth-failure node with `onset_category: CONGENITAL_ONSET`.

**Craniofacial** (PMID:34956076, 17 patients vs 34 controls): significantly decreased length of upper jaw, lower jaw, and clivus. Basilar invagination *not* observed. Midfacial hypoplasia, macroglossia, and dental anomalies are AD-predominant features.

### Hair and skin

- **Hypotrichosis** — HP:0001006 (Hypotrichosis) or HP:0002212 (Fine hair) + HP:0002213 (Fine hair)/HP:0008070 (Sparse hair). Fine, silky, sparse, often light-colored; eyebrows and eyelashes involved. Classic old-literature finding: reduced hair shaft diameter with absent or small pigment core (PMID:5533438, PMID:4787841).
- **Complete alopecia** — HP:0002293 (Alopecia of scalp) — ~15%, involving scalp, eyelashes and body hair (GeneReviews).
- **Neonatal erythroderma** — HP:0001019 (Erythroderma) — an emerging, under-recognized presentation (PMID:40110983, PMID:41616907). Nice detail for a "diagnostic pitfall" note.
- **Hypopigmentation / light hair** — common in the Finnish cohort.

### Immunologic

The heart of the disease. GeneReviews: cellular immune deficiency in **~88%**, clinical infections in **35–65%**, mostly infancy and childhood.

| Feature | Suggested HP | Freq / detail |
|---|---|---|
| Combined immunodeficiency | HP:0005387 (Combined immunodeficiency) | 24% symptomatic in the Finnish prospective cohort |
| Humoral immunodeficiency alone | HP:0004313 (Decreased circulating antibody level) | 19% |
| **Asymptomatic** | — | **57% (46/80)** — critical for framing |
| T-cell lymphopenia | HP:0005403 (Decreased T cell count) | Near-universal on labs |
| **CD8 lymphocytopenia** | HP:0005407? **VERIFY** | Novel phenotype flagged by Kavadas 2008 (PMID:18804272) |
| Impaired lymphocyte proliferation | HP:0031381 (Abnormal lymphocyte proliferation) **VERIFY** | 9/12 severe in Kavadas |
| SCID | HP:0004430 (Severe combined immunodeficiency) | Minority; associated with promoter duplications (PMID:37115363) |
| Recurrent respiratory infections | HP:0002205 (Recurrent respiratory infections) | |
| Bronchiectasis | HP:0002110 (Bronchiectasis) | **29–52%** (PMID:33675005, verbatim) |
| Recurrent pneumonia | HP:0006532 (Recurrent pneumonia) | Major mortality driver |
| Severe varicella | HP:0004429? **VERIFY** | Historically fatal |
| Neutropenia | HP:0001875 (Neutropenia) | Reported since 1970 (PMID:4188537) |

The Finnish 30-year data (**verbatim, PMID:31379817**) is the single best structured source here:

> "Half of the patients (57%, n = 46) manifested no symptoms of immunodeficiency during follow-up while 19% (n = 15) and 24% (n = 19) demonstrated symptoms of humoral or combined immunodeficiency, including six cases of adult-onset immunodeficiency. In a significant proportion of patients (17/79, 22%), clinical features of immunodeficiency progressed over time."

That "**22% progressed over time**" plus "**six cases of adult-onset immunodeficiency**" is the clinically load-bearing insight: CHH immunodeficiency is not a fixed congenital deficit you can rule out once. It creeps.

### Immune dysregulation / autoimmunity / allergy

From **verbatim PMID:30410491** (n=104, median age 39.2 y):

> "Clinical autoimmunity was common (11/104, 10.6%) and included conditions previously undescribed in subjects with CHH (narcolepsy, psoriasis, idiopathic thrombocytopenic purpura, and multifocal motor axonal neuropathy). Patients with autoimmunity more often had recurrent pneumonia, sepsis, high immunoglobulin (Ig) E and/or undetectable IgA levels. The mortality rates were higher in subjects with AI diseases (χ(2)2 = 14.056, p = 0.0002). ... We confirmed the high prevalence of asthma (23%) and allergic rhinoconjunctivitis (39%). Gastrointestinal complaints, mostly persistent diarrhea, were also frequently reported (32/104, 31%)."

So: autoimmunity **10.6%**, asthma **23%** (HP:0002099), allergic rhinoconjunctivitis **39%** (HP:0003193/HP:0000509), chronic diarrhea **31%** (HP:0002028, `temporality: CHRONIC`). And a lovely mechanistic oddity worth a `notes:` line — *"Despite the history of allergic rhinitis, no eosinophils were observed in nasal cytology in five tested patients."* The allergy phenotype may not be conventionally eosinophilic.

Also: **serum autoantibody positivity frequently occurs without matching clinical disease** (Biggs 2017, PMID:28631025). Don't curate autoantibody positivity as an autoimmune phenotype.

Granulomas (cutaneous/systemic, including lymphomatoid granulomatosis, PMID:29744913) occur and drive anti-TNF-α or HSCT decisions.

### Hematologic

- **Mild macrocytic anemia** — HP:0001889 (Macrocytic anemia) — **~80%** of CHH, typically resolves in childhood.
- **Severe persistent anemia** — **~6%**, phenocopying Diamond-Blackfan anemia; **50–75%** of those needed transfusion or transplant (GeneReviews).
- Neutropenia and lymphopenia as above.

The DBA resemblance isn't a coincidence — it's the ribosomopathy family showing its hand (PMID:20194897, *Blood* ribosomopathy review, which explicitly names CHH).

### Gastrointestinal

- **Hirschsprung disease** — HP:0002251 — **7–8%** of CHH, concentrated in severe phenotypes (Mäkitie 2001, PMID:11391344, *"Hirschsprung disease is associated especially with severe cartilage-hair hypoplasia"* — paraphrase, re-fetch). Massively enriched over the ~1/5000 population baseline (PMID:11694544). It is *not* reported in AD or MDWH.
- **Malabsorption** — secondary to infection in the first two years.
- **Chronic diarrhea** — 31% (above).

### Reproductive

- **Males:** impaired spermatogenesis — reduced sperm concentration, motility, and morphology; testicular volume below age norms with *normal* gonadotropins/testosterone (GeneReviews). HP:0000798 (Abnormal spermatogenesis) **VERIFY**.
- **Females:** possible hypogonadotropic or normogonadotropic hypogonadism with absent puberty; a dedicated gynecologic series exists (PMID:30445974, PMID:30561899) and pregnancies do occur (14 women, 42 pregnancies — Holopainen preprint).

### Malignancy

Treated in §11 — it's a prognostic feature more than a "phenotype," but for HP purposes: HP:0002665 (Lymphoma), HP:0002671 (Basal cell carcinoma), HP:0001909 (Leukemia).

### Quality of life

**Genuinely thin.** I found no EQ-5D, SF-36, or PROMIS study in CHH. Per-phenotype QoL statements would be speculation. What *is* documented: 43% undergo lower-limb realignment surgery (PMID:25764362); the elbow contracture and joint laxity are radiographically striking but functionally near-silent (*"not a single patient had any issues of consequence with that loss of motion"*); and adult stature ~122–131 cm carries the accessibility burdens common to skeletal dysplasia. **This is a real knowledge gap — worth a `discussions` entry with `kind: KNOWLEDGE_GAP`.**

---

## 4. Genetic/Molecular Information

### The gene

***RMRP*** — RNA component of mitochondrial RNA processing endoribonuclease. Chromosome **9p13.3**. Single-exon, **non-protein-coding**, RNA polymerase III transcript, ~267–268 nt. Suggested `hgnc:10031` (**verify**).

The clinically decisive practical consequence: **it's non-coding, so standard exome pipelines miss it.** Multiple sources say this outright. This belongs in the diagnostics section of the entry as a first-class fact, not a footnote.

### Variant landscape

**The dominant allele.** The founder variant is written several ways across the literature — **n.71A>G**, **g.70A>G**, **70A→G**, **c.70A>G**, **n.72A>G** — because numbering conventions for this transcript have shifted. *Pick one and note the aliases*; this is a classic curation trap. GeneReviews reports it as **g.71A>G** and gives its distribution:

- **100%** of Old Order Amish CHH alleles
- **92%** of Finnish CHH alleles
- **48%** of non-Finnish CHH alleles

Ancient shared founder haplotype across populations (Nature EJHG worldwide mutation spectrum study — *"ancient founder origin of the major 70A→G mutation"*).

**Other recurrent alleles:**
- **n.262G>T** — historically cited as an Amish-associated allele (verify against current sources; GeneReviews now emphasizes 71A>G at 100% in Amish)
- **n.197C>T** — Brazilian founder effect on a shared haplotype of predominantly European ancestry (PMID:38862721)
- **n.64C>T** — homozygous, reported in Italy (PMID:33444820)
- **Promoter insertions/duplications** — the transcription-silencing class. GeneReviews notes the mechanism precisely: they *increase the spacing of regulatory elements*, and insertions of **24–26 bp** reduce transcription efficiency. Homozygous promoter duplications → severely reduced transcript → SCID (PMID:37115363).

**Variant classes:** point substitutions in the transcribed region; promoter insertions/duplications; rarely whole-gene deletions. Sequence analysis detects ~100%; deletion/duplication analysis is a low-yield add-on (GeneReviews).

**Origin:** germline, biallelic. No somatic CHH. (*RMRP* is separately over-expressed as an oncogenic lncRNA in various sporadic cancers — PMID:33996836 — which is a completely different biology and should **not** be conflated in the entry.)

**Functional consequence:** loss of function / hypomorphic. Complete null is presumed non-viable — no human has been reported with two true null alleles, and RNase MRP is essential in yeast. Suggested `functional_impact_category: PARTIAL_LOSS_OF_FUNCTION` for most transcribed-region alleles, `LOSS_OF_FUNCTION` for promoter-silencing ones.

**Allele frequency:** gnomAD coverage of *RMRP* is poor (non-coding, short, historically excluded from exome capture). The carrier frequencies below come from population studies, not gnomAD.

### Genotype–phenotype correlation — the good bit

This is unusually well worked out, and it maps beautifully onto a two-branch dismech pathograph. Thiel 2007 (PMID:17701897, paraphrase — re-fetch):

- **rRNA cleavage impairment** (ribosome assembly) → severity of **bone dysplasia**
- **mRNA cleavage impairment** (cell-cycle regulation) → presence of **hair hypoplasia, immunodeficiency, and hematologic abnormality**

GeneReviews adds that anauxetic dysplasia arises from variants that severely impair *both*, particularly 5.8S rRNA cleavage and cyclin B1 mRNA processing.

So the entry should carry **two parallel mechanism branches from a shared upstream node**, not one linear chain. That's the structurally interesting thing about this disease.

### Modifier genes

None established. Kavadas 2008 documented *"significant, even intrafamilial, phenotypic heterogeneity"* — siblings with identical genotypes diverging clinically — which is strong evidence that modifiers (genetic or stochastic) exist without any being identified. Good `KNOWLEDGE_GAP` candidate.

### Epigenetics

No CHH-specific methylation or chromatin study found. **Not available.**

### Chromosomal abnormalities

None. Not a CNV/aneuploidy disorder (rare whole-gene deletions aside).

---

## 5. Environmental Information

Short section, honestly. CHH is not an environmental disease.

- **Environmental factors:** no toxin, radiation, or occupational exposure implicated in causation. CTD has no CHH entry of substance.
- **Lifestyle:** no evidence of dietary or behavioral modification of disease course. GH therapy explicitly unhelpful.
- **Infectious agents:** no infectious *cause*, but infection is the dominant *complication*. Named organisms/entities across the literature: varicella-zoster virus (severe/fatal disease), vaccine-derived poliovirus (PMID:165279), *Epstein-Barr virus* (EBV-positive Hodgkin lymphoma in CHH-AD siblings, PMID:41460196), and the usual recurrent bacterial respiratory pathogens driving bronchiectasis. EBV is the most mechanistically interesting — it links the immunodeficiency node to the lymphoma node.

For the pathograph: model infections as `influences_mechanisms` targeting the immunodeficiency node with `environmental_effect: EXACERBATES`, and remember the CLAUDE.md guidance that only `TRIGGERS`/`EXACERBATES` count as causal for compliance scoring — don't inflate.

---

## 6. Mechanism / Pathophysiology

Here's the causal architecture. I'd build it as one upstream lesion fanning into **two mechanistic arms** that reconverge on tissue-specific outcomes.

### The enzyme

**RNase MRP** is a nucleolar ribonucleoprotein — one catalytic RNA (*RMRP*) wrapped in ~10 protein subunits: **POP1, POP4 (RPP29), POP5, RPP14, RPP20 (POP7), RPP21, RPP25, RPP30, RPP38, RPP40**, plus NEPRO. It's an evolutionary sibling of RNase P — same architectural family, different substrate menu. Think of it as a pair of molecular scissors that got repurposed for several unrelated jobs over evolutionary time, which is exactly why breaking it produces such a scattered, pleiotropic mess.

Structural work exists: RPP20–RPP25 in complex with the P3 domain of the RNA (PMID:33571640) — useful if the entry wants a protein-structure claim.

Critically, Ridanpää showed the CHH mutations don't stop the proteins binding: *"The association of protein subunits with RNA appears unaltered."* Robertson 2022 refines this — the 70AG allele **reduces the amount of intact complex**, rather than making a mis-assembled one.

### Known catalytic functions (i.e. the fan-out)

1. **Pre-rRNA processing.** Cleaves internal transcribed spacer 1 (ITS1, site A3 in yeast) during ribosome biogenesis, feeding 5.8S rRNA maturation. **This is the arm that makes CHH a ribosomopathy.**
2. **Cell-cycle control via cyclin mRNA cleavage.** Degrades cyclin B2 (and per GeneReviews, cyclin B1) mRNA at mitotic exit. Break this and you break the G2→M transition.
3. **Mitochondrial DNA replication.** Processes the RNA primer at the mtDNA heavy-strand origin — the "MRP" in the name.
4. **Telomere biology.** *RMRP* associates with TERT; the TERT–RMRP complex has RNA-dependent RNA polymerase activity producing double-stranded RMRP RNA processed into siRNA (Rogler 2014 lineage).
5. **Small-RNA gene silencing.** *RMRP* is processed into **RMRP-S1** and **RMRP-S2**, which act as miRNAs (PMID:24009312).

### Arm A — the ribosomopathy arm (→ skeleton, growth)

**Verbatim, PMID:35115551** (this is the single best mechanistic snippet available):

> "RMRP encodes a non-coding RNA forming the core of the RNase MRP ribonucleoprotein complex. Mutations cause Cartilage Hair Hypoplasia (CHH), characterized by skeletal abnormalities and impaired T cell activation. Yeast RNase MRP cleaves a specific site in the pre-ribosomal RNA (pre-rRNA) during ribosome synthesis. CRISPR-mediated disruption of RMRP in human cells lines caused growth arrest, with pre-rRNA accumulation. Here, we analyzed disease-relevant primary cells, showing that mutations in RMRP impair mouse T cell activation and delay pre-rRNA processing. Patient-derived human fibroblasts with CHH-linked mutations showed similar pre-rRNA processing delay. Human cells engineered with the most common CHH mutation (70AG in RMRP) show specifically impaired pre-rRNA processing, resulting in reduced mature rRNA and a reduced ratio of cytosolic to mitochondrial ribosomes. Moreover, the 70AG mutation caused a reduction in intact RNase MRP complexes. Together, these results indicate that CHH is a ribosomopathy."

**Chain:** biallelic *RMRP* lesion → reduced intact RNase MRP complex → delayed/impaired pre-rRNA cleavage at ITS1 → reduced mature cytosolic rRNA → **reduced cytosolic:mitochondrial ribosome ratio** → reduced translational capacity → impaired proliferation of growth-plate chondrocytes → metaphyseal dysplasia and short-limb short stature.

That ribosome-ratio finding is unusually specific and quotable. Also worth an `attaches_to` link: Hermanns 2005 (PMID:16254002) showed the 70A>G allele *shifts the 5.8S rRNA ratio* in yeast — i.e. it's not just less rRNA, it's the wrong mixture of 5.8S isoforms.

The p53 connection completes the arm: ribosome biogenesis stress activates p53, and *"this pathway appears to be a critical mediator of many of the clinical features of ribosomopathies"* (PMID:20194897, needs re-fetch to quote).

### Arm B — the cell-cycle arm (→ hair, immunity, blood, cancer)

**Verbatim, PMID:31551465:**

> "Transcriptome analysis identified 35 significantly upregulated and 130 downregulated genes in CHH fibroblasts. The downregulated genes were significantly connected to the cell cycle. Multiple other pathways, involving regulation of apoptosis, bone and cartilage formation, and lymphocyte function, were also affected, as well as PI3K-Akt signaling. Cell-cycle studies indicated that the CHH cells were delayed specifically in the passage from G2 phase to mitosis."

**Chain:** *RMRP* lesion → impaired cyclin B1/B2 mRNA cleavage → dysregulated mitotic cyclin turnover → **G2→M transition delay** → reduced proliferative output in high-turnover lineages (T cells, erythroid progenitors, hair follicle matrix keratinocytes) → combined immunodeficiency + macrocytic anemia + hypotrichosis.

Hermanns adds a transcriptional flavor: upregulation of **cytokine** and cell-cycle genes, linking altered ribosomal processing to *"modified cytokine signaling and cell cycle progression in lymphocytic and chondrocytic lineages"* (paraphrase — re-fetch).

### Arm C — telomere maintenance (→ immune senescence, cancer)

**Verbatim, PMID:28126377:**

> "Lymphocyte cultures from patients with CHH display growth defects in vitro, which is consistent with an immune deficiency cellular phenotype. Here we show that telomere length and telomerase activity are impaired in primary lymphocyte subsets from patients with CHH. Notably, telomerase activity is affected in a gene dose-dependent manner when comparing heterozygote RMRP carriers with patients with CHH. Telomerase deficiency in patients with CHH is not mediated by abnormal telomerase gene transcript levels relative to those of endogenous genes."

That last sentence is a genuinely nice piece of negative evidence — the telomerase defect is **post-transcriptional**, which rules out the simplest explanation. The mechanism remains unidentified (*"through an as yet unidentified mechanism"*) — perfect `KNOWLEDGE_GAP` material.

Note the phenotypic overlap with dyskeratosis congenita this creates. Worth a `differential_diagnosis` entry.

### Arm D — small-RNA gene silencing (→ tissue-specific programs)

Rogler 2014 (PMID:24009312, paraphrase — re-fetch): *RMRP* yields RMRP-S1/S2, which are **significantly reduced** in CHH patient fibroblasts and a CHH B-cell line. Over 900 genes were regulated (~75% down), with pathway enrichment in **skeletal development, hair development, and hematopoietic differentiation**, naming **PTCH2** (hedgehog) and **SOX4**. This is the most direct mechanistic bridge to the *hair* phenotype specifically, which the ribosome arm alone doesn't explain well.

### Arm E — Wnt/β-catenin in cartilage (from the zebrafish)

**Verbatim, PMID:31237961:**

> "We found that rmrp is required for the patterning and shaping of pharyngeal arches. Rmrp mutation inhibits the intramembranous ossification of skull bones and promotes vertebrae ossification. The abnormalities of endochondral bone ossification are variable, depending on the degree of dysregulated chondrogenesis. Moreover, rmrp mutation inhibits cell proliferation and promotes apoptosis through dysregulating the expressions of cell-cycle- and apoptosis-related genes. We also demonstrate that rmrp mutation upregulates canonical Wnt/β-catenin signaling; the pharmacological inhibition of Wnt/β-catenin could partially alleviate the chondrodysplasia and increased vertebrae mineralization in rmrp mutants."

The pharmacological rescue is the payload — it identifies Wnt/β-catenin as a *druggable* node. Tag `evidence_source: MODEL_ORGANISM` and, per dismech policy, don't let it stand alone for a human phenotype.

Complementary chondrocyte work: *RMRP* expression is dynamically regulated during chondrocyte hypertrophy and determines chondrogenic differentiation (PMID:28743979); CHH fibroblast chondrogenic-differentiation pathway analysis in PMID:34988338.

### Cellular / molecular annotations

**Suggested GO biological processes (all VERIFY):**
- rRNA processing — GO:0006364
- maturation of 5.8S rRNA — GO:0000460 **VERIFY**
- ribosome biogenesis — GO:0042254
- mRNA cleavage — GO:0006379 **VERIFY**
- G2/M transition of mitotic cell cycle — GO:0000086
- regulation of cell cycle — GO:0051726
- telomere maintenance via telomerase — GO:0007004
- canonical Wnt signaling pathway — GO:0060070 (`modifier: INCREASED` per the zebrafish)
- endochondral ossification — GO:0001958
- chondrocyte differentiation — GO:0002062
- T cell activation — GO:0042110 (`modifier: DECREASED`)
- mitochondrial DNA replication — GO:0006264
- gene silencing by miRNA — GO:0035195

**Suggested GO molecular functions:**
- ribonuclease activity / endoribonuclease activity — GO:0004521 / GO:0004519

**Suggested GO cellular components:**
- nucleolus — GO:0005730 (primary site of RNase MRP action)
- mitochondrion — GO:0005739
- cytosolic ribosome — GO:0022626

**Suggested CL cell types (VERIFY):**
- chondrocyte — CL:0000138
- growth plate chondrocyte / hypertrophic chondrocyte — **VERIFY**
- T cell — CL:0000084; CD8-positive alpha-beta T cell — CL:0000625
- erythroid progenitor cell — CL:0000038 **VERIFY**
- hair follicle keratinocyte / matrix cell — **VERIFY**
- fibroblast — CL:0000057 (the workhorse of the in-vitro literature)
- enteric neuron / neural crest cell — CL:0007011 **VERIFY** (for the Hirschsprung branch)

### Molecular profiling summary

- **Transcriptomics:** yes — CHH fibroblast RNA-seq, 35 up / 130 down, cell cycle + PI3K-Akt (PMID:31551465). Rogler's >900 small-RNA-regulated genes (PMID:24009312). Hermanns' cytokine/cell-cycle upregulation (PMID:16254002).
- **Proteomics:** none CHH-specific found.
- **Metabolomics / lipidomics:** none found. **Not available.**
- **Single-cell / spatial:** none found. **Not available** — and a legitimate gap given the tissue-specific ribosome-ratio finding practically begs for it.
- **Functional genomics:** CRISPR disruption of *RMRP* in human cell lines → growth arrest with pre-rRNA accumulation (PMID:35115551); targeted CRISPR disruption revealing a role for RNase MRP RNA (Goldfarb & Cech, PMID:28115465).

---

## 7. Anatomical Structures Affected

**Primary organs / systems:**

| Structure | Suggested UBERON | Involvement |
|---|---|---|
| Long bone metaphysis | UBERON:0002225 (bone metaphysis) **VERIFY** | Primary — femur, tibia especially |
| Epiphyseal/growth plate cartilage | UBERON:0006255? **VERIFY** (epiphyseal plate) | Primary lesion site |
| Femur / tibia | UBERON:0000981 / UBERON:0000979 | Bowing, varus |
| Vertebral column | UBERON:0000955? no — UBERON:0002240 (spinal cord) is wrong; use UBERON:0000956? **VERIFY** — want vertebral column UBERON:0002412 | Lordosis, scoliosis; AD cervical instability |
| Hair follicle | UBERON:0002073 | Hypoplastic |
| Thymus / T-cell compartment | UBERON:0002370 | Impaired T-cell output |
| Bone marrow | UBERON:0002371 | Macrocytic anemia, neutropenia |
| Lung / bronchus | UBERON:0002048 / UBERON:0002185 | Secondary — bronchiectasis |
| Large intestine / colon | UBERON:0001155 | Hirschsprung (aganglionic segment) |
| Enteric nervous system | UBERON:0002005 **VERIFY** | Absent ganglion cells |
| Testis / ovary | UBERON:0000473 / UBERON:0000992 | Impaired spermatogenesis; hypogonadism |
| Skin | UBERON:0002097 | BCC/SCC; granulomas; neonatal erythroderma |
| Mandible / maxilla / clivus | UBERON:0001684 / UBERON:0002397 / **VERIFY** | Shortened (PMID:34956076) |

**Body systems:** skeletal, immune, hematopoietic, integumentary, gastrointestinal, respiratory (secondary), reproductive.

**Subcellular:** nucleolus (GO:0005730) is the star — that's where the ribosome-biogenesis lesion lives. Mitochondrion (GO:0005739) for the mtDNA primer function. Cytosolic ribosome (GO:0022626) for the depleted product.

**Lateralization:** **bilateral and symmetric** throughout. Metaphyseal changes, bowing, and hair involvement are symmetric. Asymmetry should prompt reconsideration of the diagnosis.

---

## 8. Temporal Development

**Onset:** congenital. Short limbs are recognizable at birth and increasingly **prenatally** — there's now a whole small literature on it (PMID:41525162 narrative review of prenatal diagnosis; PMID:41720498 familial prenatal ultrasound; PMID:33567347 early prenatal presentation of the CHH/AD spectrum). GeneReviews notes ultrasound may detect severe cases at **16–18 weeks**. Suggested `onset_category: CONGENITAL_ONSET` (with `ANTENATAL_ONSET` for the severe end).

**Course by domain — and they diverge, which is the key structural point:**

| Domain | Course |
|---|---|
| Growth | Progressive deceleration through the first 2 years, then proportionate tracking with a weak/absent pubertal spurt. Final height reached in adolescence. |
| Immunodeficiency | **Variable and often progressive.** 22% progressed over follow-up; adult-onset immunodeficiency documented in 6 patients (PMID:31379817). Not a static congenital deficit. |
| Anemia | Usually **remitting** — mild macrocytic anemia typically resolves during childhood. ~6% persist severely. |
| Infections | Peak burden in infancy and childhood (35–65%), then generally decreasing. |
| Bronchiectasis | Prevalence high (29–52%) but **progression is slow or absent** — see below. |
| Malignancy | **Late and progressive risk** — cumulative, rising with age (41% by age 65). |
| Autoimmunity | Adult-onset and mortality-associated. |

That bronchiectasis finding deserves its own mention because it overturned an assumption (**verbatim, PMID:33675005**):

> "We determined the rate and correlates of progression of structural lung changes in a prospectively followed cohort of 16 patients with cartilage-hair hypoplasia. ... Imaging findings remained identical or improved due to disappearance of inflammatory changes in all evaluated patients. ... In conclusion, our results suggest slow if any development of bronchiectasis in selected subjects with cartilage-hair hypoplasia."

**Disease duration:** chronic, lifelong. No spontaneous remission of the underlying disorder. The only "remission" available is treatment-induced — HSCT resets the immune and hematologic arms (and *only* those arms).

**Critical intervention windows:**
1. **Newborn screening period** — TREC-based SCID screening can catch the severe end before first infection (PMID:41831046, PMID:41727503).
2. **Before major organ damage** — Bordon's central argument: transplant *"before the development of severe infections, major organ damage, or malignancy might jeopardize the outcome."*
3. **Late childhood/adolescence** — timing for corrective osteotomy.
4. **Lifelong** — malignancy surveillance never stops, because 8 of 15 non-skin cancers occurred in patients with **no preceding clinical immunodeficiency symptoms**.

---

## 9. Inheritance and Population

### Epidemiology

| Population | Figure | Source |
|---|---|---|
| **Finland** | Incidence **1:23,000**; carrier frequency **1:76** | GeneReviews (PMID:22420014) |
| **Old Order Amish** | Prevalence **1–2:1,000**; carrier frequency **1:10** | GeneReviews |
| **Global** | ~**700 individuals** documented in the literature | GeneReviews |
| **Anauxetic dysplasia** | <10 reported cases | GeneReviews |

For a dismech `prevalence` block, normalizing: Finland 1:23,000 → **rate_per_100000 ≈ 4.3**, `measure_type: ANNUAL_INCIDENCE` (it's stated as incidence), `prevalence_class: BAND_1_9_PER_100000`. Amish 1–2:1,000 → **rate_per_100000 = 100–200**, `prevalence_class: ABOVE_1_IN_1000`. Global rarity elsewhere: `ULTRA_RARE`. Note these are wildly different populations — do **not** collapse them into one record.

### Inheritance

- **Autosomal recessive**, HP:0000007. Recurrence risk 25% affected / 50% carrier / 25% unaffected non-carrier per pregnancy.
- **Penetrance:** essentially complete for the *skeletal* phenotype. Markedly **incomplete/variable for the extraskeletal features** — 57% of the Finnish cohort never manifested clinical immunodeficiency. This is the single most important counseling nuance in the disease.
- **Expressivity:** highly variable, including **intrafamilial** variability among identical genotypes (PMID:18804272).
- **Anticipation:** not applicable — no repeat expansion.
- **Germline mosaicism:** not reported.
- **Founder effects:** yes, prominently — Amish, Finnish, and Brazilian (n.197C>T, PMID:38862721). The 71A>G allele traces to an **ancient shared founder haplotype**.
- **Consanguinity:** contributory in non-founder populations (Turkish, Pakistani, Moroccan case reports). PMID:27740950 documents the Finnish founder allele appearing in a Pakistani family — nice illustration that "founder" ≠ "confined to that population."

### Demographics

- **Ethnic distribution:** highest in Old Order Amish and Finns; described worldwide (Brazil, Turkey, Korea, Japan, Italy, Spain, Pakistan, India). First Korean cases reported only in 2024 (PMID:38787970) — ascertainment, not absence.
- **Sex ratio:** ~1:1, as expected for autosomal recessive. No reported skew. (Sex-specific *manifestations* differ — spermatogenic failure vs. hypogonadism — but incidence does not.)
- **Age distribution:** diagnosed in infancy/early childhood classically; increasingly prenatally; and mild cases can be diagnosed late — PMID:28094436 reports CHH **with normal height in childhood**, and PMID:31413121 reports MDWH presenting with late-onset manifestations. Median age in the Finnish adult cohort was 39.2 years, with a range to 73.6 — people do reach old age with this.

---

## 10. Diagnostics

### The one thing that matters most

***RMRP* is non-coding, so exome sequencing does not cover it.** A negative WES does not exclude CHH. This is the most consequential practical fact in the whole diagnostic section, and it should be prominent in the entry (a `definitions` note or a `notes:` line on the genetic block).

### Diagnostic pathway

1. **Clinical + radiographic suspicion:** short-limb disproportionate short stature; metaphyseal dysplasia on skeletal survey; bowed femora/tibiae; bullet-shaped middle phalanges; joint hypermobility with limited elbow extension; fine silky hair; ± infections, anemia, GI dysfunction.
2. **Confirmatory:** **direct Sanger sequencing of *RMRP*** (including the promoter — don't sequence only the transcribed region, or you'll miss the promoter duplication class). Detects ~100% of variants. Deletion/duplication analysis as a low-yield adjunct.
3. **Panel testing:** skeletal dysplasia panels and IEI panels that *explicitly include* the *RMRP* locus. Check the panel design.
4. **WGS:** works (covers non-coding regions) where WES does not.
5. Karyotype/CMA/FISH/mtDNA/repeat testing: **not indicated.**

### Laboratory / immunologic workup

- CBC with indices — macrocytic anemia (↑MCV), neutropenia, lymphopenia
- Lymphocyte subsets — CD3/CD4/**CD8** (CD8 lymphocytopenia is the Kavadas signature), naive vs memory
- **TRECs** — newborn SCID screening detects the severe end
- Lymphocyte proliferation to mitogens/antigens
- Immunoglobulins IgG/IgA/IgM/**IgE** — note the association of **high IgE and/or undetectable IgA** with autoimmunity and mortality (PMID:30410491); low IgM associated with subtle bronchiectasis (PMID:33675005)
- Vaccine antibody titers
- Autoantibody panel — **with the caveat that positivity often has no clinical correlate** (PMID:28631025)
- Erythrocyte adenosine deaminase — *normal* in CHH; historically used to separate it from DBA (PMID:1151542, PMID:23252420)

### Imaging

- Skeletal survey (diagnostic)
- Lower-limb alignment films (surgical planning)
- Cervical spine films — mandatory in AD, annual; lower yield in classic CHH
- **Chest HRCT or MRI** for bronchiectasis. Vakkilainen's imaging study supports **MRI** and argues against frequent repeat imaging given the slow progression — a radiation-sparing point worth curating.
- Abdominal ultrasound every 1–2 years in children for malignancy surveillance

### Histopathology

- Growth plate: hypoplastic, disorganized chondrocyte columns, reduced proliferative zone
- Hair shaft: reduced diameter, absent/small pigment core
- Rectal suction biopsy: **absent ganglion cells** in the Hirschsprung subset
- Skin/nodes: granulomas, lymphomatoid granulomatosis in a subset

### Differential diagnosis

| Condition | Gene | Discriminator |
|---|---|---|
| Schmid metaphyseal chondrodysplasia | *COL10A1* | **No extraskeletal features at all** — no hair, immune, or anemia involvement |
| Shwachman-Diamond syndrome | *SBDS* | Pancreatic exocrine insufficiency + neutropenia dominate; milder skeletal disease |
| Diamond-Blackfan anemia | ribosomal proteins | Severe anemia dominates; normal erythrocyte ADA in CHH, elevated in DBA |
| Omenn syndrome | *RAG1/2* etc. | Ichthyosiform erythroderma, septicemia, more acutely severe (**and note CHH itself can present with neonatal erythroderma — real overlap**) |
| Schimke immuno-osseous dysplasia | *SMARCAL1* | Nephropathy, spondyloepiphyseal (not metaphyseal) dysplasia, hyperpigmented macules (PMID:18627050) |
| Dyskeratosis congenita | *DKC1*, *TERT* etc. | Overlapping telomere biology, but nail dystrophy/leukoplakia/reticular pigmentation |
| Anauxetic dysplasia 2 | *POP1* | Skeletal phenotype without clinical immunodeficiency (reduced lymphocyte proliferation on labs only) |
| Anauxetic dysplasia 3 | *NEPRO* | Sparse hair **but no immunodeficiency** |
| *EXTL3*-related | *EXTL3* | Spondyloepimetaphyseal dysplasia + developmental delay + liver cysts |

### Screening

- **Newborn SCID/TREC screening** — catches severe CHH, and GeneReviews notes it may carry prognostic information. Multiple recent papers put CHH in the syndromic-IEI-detected-by-TREC bucket (PMID:41831046, PMID:41727503).
- **Carrier screening** — high value in Amish and Finnish populations given 1:10 and 1:76 carrier frequencies.
- **Cascade testing** of at-risk relatives once family variants are known.
- **Prenatal / PGT** — available once the familial variants are identified; ultrasound detects severe cases from 16–18 weeks.

---

## 11. Outcome / Prognosis

### Mortality — the headline numbers

From **verbatim PMID:31379817**, the 30-year Finnish prospective cohort (n=80):

> "Altogether 20 patients had deceased (SMR = 7.0, 95%CI = 4.3-11); most commonly from malignancy (n = 7, SMR = 10, 95%CI = 4.1-21) and lung disease (n = 4, SMR = 46, 95%CI = 9.5-130)."

So: **overall standardized mortality ratio 7.0** against the Finnish national rate. Lung disease carries an SMR of **46** — the highest single ratio in the study, and the reason pulmonary follow-up gets its own literature.

**Validated risk factors for early death** (same source, verbatim):

> "Mortality associated with birth length below -4 standard deviation (compared to normal, SMR/SMR ratio = 5.4, 95%CI = 1.5-20), symptoms of combined immunodeficiency (compared to asymptomatic, SMR/SMR ratio = 3.9, 95%CI = 1.3-11), Hirschsprung disease (odds ratio (OR) 7.2, 95%CI = 1.04-55), pneumonia in the first year of life or recurrently in adulthood (OR = 7.6/19, 95%CI = 1.3-43/2.6-140) and autoimmunity in adulthood (OR = 39, 95%CI = 3.5-430)."

These were subsequently **validated in an independent analysis** (PMID:38676846) — and separately, shorter birth length plus decreased T-cell production/function predicted severe infections in non-SCID CHH children (PMID:38187867). Birth length below −4 SD is a beautifully simple, universally measured prognostic marker; it deserves to be a first-class item in the entry.

The paper's own conclusion is the clinical takeaway (**verbatim**):

> "In conclusion, patients with CHH may develop adult-onset immunodeficiency or malignancy without preceding clinical symptoms of immune defect, warranting careful follow-up."

### Malignancy

Taskinen 2008 (PMID:18698627, n=123 Finnish patients, **2,365 person-years** — paraphrase, re-fetch before quoting): **14 cancers observed vs. 2 expected**. Non-Hodgkin lymphoma most frequent (n=9), **SIR 90.2 (CI 39.0–180)**. Conclusion: significantly increased risk of NHL and basal cell carcinoma **at early age**, with poor overall prognosis.

GeneReviews adds: ~**11%** developed malignancy over 39-year follow-up (14/123); Kaplan-Meier estimate **41% probability by age 65**; commonest are NHL, squamous cell carcinoma, and leukemia; **median survival after cancer diagnosis: 3 months** (9 of 14 died). A separate series of 16 CHH lymphoma patients: DLBCL predominant, **69% mortality (11/16)**.

An SIR of 90 for NHL is one of the highest in any inherited condition. This should be a prominent, well-evidenced node.

The countercurrent worth curating: PMID:41460196 reports two CHH-AD siblings with **relapsed/refractory EBV-positive Hodgkin lymphoma** achieving durable (30-month) remission with gemcitabine/vinorelbine + brentuximab vedotin **without transplant** — evidence that targeted consolidation may change this grim picture.

### Morbidity and function

- Adult height 122–131 cm median with associated accessibility burden
- ~43% undergo lower-limb realignment surgery
- Bronchiectasis in 29–52%, though slowly progressive
- Chronic diarrhea in 31%
- Subfertility in both sexes
- Recurrent infection burden in the symptomatic 43%

**Formal QoL instrument data: not available.** Flag as a gap.

### Prognostic factors — summary table

| Factor | Direction | Evidence |
|---|---|---|
| Birth length < −4 SD | ↑ mortality (SMR ratio 5.4) | PMID:31379817 |
| Symptomatic combined immunodeficiency | ↑ mortality (SMR ratio 3.9) | PMID:31379817 |
| Hirschsprung disease | ↑ mortality (OR 7.2) | PMID:31379817 |
| Pneumonia, first year of life | ↑ mortality (OR 7.6) | PMID:31379817 |
| Recurrent pneumonia in adulthood | ↑ mortality (OR 19) | PMID:31379817 |
| Adult autoimmunity | ↑ mortality (OR 39) | PMID:31379817, PMID:30410491 |
| Undetectable IgA and/or high IgE | ↑ autoimmunity, ↑ mortality | PMID:30410491 |
| Decreased T-cell production/function | ↑ severe infection | PMID:38187867 |
| Malignancy (esp. NHL) | catastrophic — median 3 mo survival | GeneReviews / PMID:18698627 |
| Asymptomatic status at follow-up (57%) | favorable — but **not** protective against later cancer | PMID:31379817 |

That last row matters: **8 of 15 patients with non-skin cancer had no preceding clinical immunodeficiency symptoms.** Being asymptomatic does not earn you a pass on surveillance.

---

## 12. Treatment

No disease-modifying therapy exists. Management is complication-directed, with one curative option that fixes exactly half the disease.

### Hematopoietic stem cell transplantation

The only curative option for the immune and hematologic arms. **It does not correct growth failure.** Bordon 2010 (**verbatim, PMID:20375313**):

> "Previous reports in single CHH patients with significant immunodeficiencies have demonstrated that allogeneic hematopoietic stem cell transplantation (HSCT) is an effective treatment for the severe immunodeficiency, while growth failure remains unaffected. ... we performed a European collaborative survey reporting on 16 patients with CHH and immunodeficiency who underwent HSCT. Immune dysregulation, lymphoid malignancy, and autoimmunity were important features in this cohort. Thirteen patients were transplanted in early childhood (approximately 2.5 years). The other 3 patients were transplanted at adolescent age. Of 16 patients, 10 (62.5%) were long-term survivors, with a median follow-up of 7 years. T-lymphocyte numbers and function have normalized, and autoimmunity has resolved in all survivors. HSCT should be considered in CHH patients with severe immunodeficiency/autoimmunity, before the development of severe infections, major organ damage, or malignancy might jeopardize the outcome of HSCT and the quality of life in these patients."

GeneReviews puts overall survival at **63–80%** and notes normalization of T cells, resolution of autoimmunity, and *catch-up growth* in some series — worth flagging as a discrepancy with Bordon's "growth failure remains unaffected." Curate the discrepancy honestly rather than picking a side; it might be a `KNOWLEDGE_GAP` or a real difference in conditioning era.

Suggested annotation: `treatment_term` NCIT:C15431 (Hematopoietic Cell Transplantation) **verify**; `therapeutic_modality: CELL_THERAPY` (per the CLAUDE.md mechanical-backfill table, C15431 → CELL_THERAPY); `target_mechanisms` pointing at the immunodeficiency and anemia nodes with `treatment_effect` set appropriately.

### Immunologic / infectious management

| Intervention | Detail | Suggested NCIT |
|---|---|---|
| Immunoglobulin replacement | For documented hypogammaglobulinemia / impaired specific antibody | NCIT:C15986 Pharmacotherapy + agent **verify** |
| Antibiotic prophylaxis | For recurrent infections | NCIT:C15986 |
| **High-dose IV acyclovir** | **Immediately** on varicella exposure/infection — potentially life-saving | NCIT:C15986 + CHEBI:2453 (aciclovir) **verify** |
| Airway clearance physiotherapy | Bronchiectasis, per pulmonologist | NCIT:C15302 Physical Therapy → `BEHAVIORAL` |
| Anti-TNF-α therapy | For granulomas — **carries a rare fatal PML risk**, per GeneReviews | NCIT:C15986 + NCIT:C20401 Monoclonal Antibody |

### Hematologic

- Red cell transfusion **with iron chelation** for severe persistent anemia
- HSCT for transfusion-dependent anemia (rarely needed)

### Skeletal / orthopaedic

- **Corrective osteotomy** for varus deformity — late childhood/adolescence; 43% of patients, mean age ~11.7–14.5 years (PMID:25764362). NCIT:C16186 Orthopedic Surgical Procedure → `SURGERY`.
- Scoliosis: observation → bracing → fusion by curve magnitude
- AD-specific: cervical fusion for atlantoaxial instability; **special anaesthetic precautions** for airway/neck manipulation; kyphoscoliosis surgery if lung function is compromised
- **Growth hormone: not recommended** — no sustained benefit (GeneReviews). Curate this as an explicit negative treatment recommendation; it's the kind of thing families ask about.

### Gastrointestinal

- Surgical management of Hirschsprung disease (pull-through). Note the poor prognosis association (PMID:11391344) — HSCR in CHH is a mortality marker, not just a surgical problem.

### Endocrine / reproductive

- Hormonal induction of puberty where indicated
- Fertility counseling for both sexes

### Malignancy

- Standard protocols; NHL carries poor prognosis with conventional cytotoxic regimens
- Emerging: brentuximab vedotin + gemcitabine/vinorelbine achieved 30-month HSCT-free remission in refractory Hodgkin lymphoma in CHH-AD (PMID:41460196)
- Caution warranted with cytotoxic intensity given the underlying proliferation defect and marrow reserve — inferred, not directly evidenced

### Pharmacogenomics

**No CHH-specific pharmacogenomic data found.** Not available.

### Experimental / future directions

- **Wnt/β-catenin inhibition** — pharmacological inhibition partially rescued chondrodysplasia and vertebral mineralization in the zebrafish model (PMID:31237961). The only mechanism-directed lead with in-vivo rescue data. Preclinical only.
- **PI3K-Akt** — flagged as affected in CHH fibroblast transcriptomics (PMID:31551465); the authors explicitly note the findings *"indicate possible pathways for therapeutic intervention."*
- **L-leucine / mTOR activation** — established as a ribosomopathy strategy in DBA and del(5q) MDS (PMID:22734070). **Not tested in CHH.** Speculative, but a defensible `proposed_experiments` item.
- **RNA-based replacement/correction** — conceptually attractive for a single non-coding RNA gene. No published program found.
- **ClinicalTrials.gov:** the only CHH trial I identified is **NCT02383797**, the live VZV vaccine safety trial (5 subjects) in PMID:32849667. Worth a `clinical_trials` entry with `phase` as an enum value and target phenotypes bound to HP terms.

---

## 13. Prevention

**Primary prevention** of the disease itself isn't possible — it's a congenital genetic disorder. What's available:

- **Genetic counseling** (NCIT:C15240 Genetic Counseling → the entry's `treatments` or a prevention block): 25% recurrence risk; carrier testing for relatives; special weight in Amish and Finnish communities where carrier frequency is 1:10 and 1:76.
- **Carrier screening** in founder populations.
- **Prenatal diagnosis / PGT** once familial variants are known; ultrasound from 16–18 weeks for severe phenotypes.

**Secondary prevention (early detection):**

- **Newborn TREC/SCID screening** — identifies the severe immunodeficient end pre-symptomatically.
- Immune function testing at diagnosis in every patient, including the asymptomatic — because 57% look fine and 22% will progress.

**Tertiary prevention (complication avoidance) — this is where most of the value is:**

GeneReviews' surveillance schedule, which maps cleanly onto a dismech management block:

| Domain | Frequency |
|---|---|
| Growth (CHH-specific curves) | Annually through childhood |
| Immune function | At diagnosis; interval by initial result |
| Joints and spine (clinical + radiographic) | Annually in childhood |
| Spine radiographs (AD) | Annually |
| Respiratory assessment | By infection frequency; HRCT/MRI if bronchiectasis suspected |
| CBC (if prior anemia) | Annually |
| **Malignancy screening** — exam, CBC, LDH, uric acid | Annually |
| Abdominal ultrasound (children) | Every 1–2 years |
| Pubertal assessment | Annually through adolescence |

Plus: **immediate high-dose IV acyclovir on varicella exposure** — the single highest-yield prophylactic rule in the disease.

### Immunization — the nuanced one

Default: **live vaccines contraindicated in SCID**; inactivated vaccines safe and encouraged. But Vakkilainen 2020 (**verbatim, PMID:32849667**) genuinely moved this:

> "A large proportion of patients have been immunized with live viral vaccines, including measles-mumps-rubella (MMR) (n = 40, 38%) and VZV (n = 10, 10%) vaccines, with no serious adverse events. ... Patients with CHH demonstrated seropositivity rates of 96%/75%/91% to measles, mumps and rubella, respectively, measured at a medium of 24 years post-immunization. Clinical trial participants developed humoral and cellular responses to VZV vaccine. One trial participant developed post-immunization rash and knee swelling, both resolved without treatment. Conclusion: No serious adverse events have been recorded after immunization with live viral vaccines in Finnish patients with CHH. Patients generate humoral and cellular immune response to live viral vaccines. Immunization with live vaccines may be considered in selected CHH patients with no or clinically mild immunodeficiency."

Curate that as a **conditional** recommendation gated on immune phenotype, not a blanket one. And keep the historical vaccine-associated poliomyelitis case (PMID:165279) as the counterweight — it's why the rule existed.

**Public health / environmental interventions:** not applicable beyond general infection control and, plausibly, sun protection given the BCC/SCC excess (inferred).

---

## 14. Other Species / Natural Disease

Thin section, and honestly interesting for what's *absent*.

- **Taxonomy:** human — NCBITaxon:9606. No naturally occurring CHH homolog reported in companion animals or wildlife.
- **OMIA:** I found no OMIA entry for an *RMRP* disorder in any species. **Not available.**
- **Breed (VBO):** not applicable.
- **Orthologs:** *RMRP* is conserved across eukaryotes — RNase MRP is present in yeast (*NME1*), where it's **essential**. Mouse *Rmrp*, zebrafish *rmrp*. The yeast work is where the ITS1/A3 cleavage function was originally defined, and Hermanns 2005 used yeast to show the 70A>G allele shifts 5.8S rRNA ratios. That's a genuinely useful piece of evolutionary conservation evidence — the disease-causing base change breaks the enzyme the same way a billion years of divergence apart.
- **Zoonotic potential / cross-species transmission:** not applicable (genetic disorder).
- **Comparative biology:** the deep conservation of RNase MRP's rRNA-processing role is the strongest cross-species claim available. The *divergent* bits — the miRNA-generating and telomerase-associating functions — appear more vertebrate/human-specific, which is worth noting as a limitation on how far yeast data can carry a human mechanistic claim.

---

## 15. Model Organisms

### Zebrafish — the workhorse

***rmrp* knockout zebrafish** (PMID:31237961) is the best-characterized whole-organism model, and the paper explicitly frames itself as filling a void: *"there are no viable animal models for CHH."*

**Recapitulates:** dysregulated chondrogenesis, abnormal endochondral ossification, inhibited intramembranous skull ossification, pharyngeal arch patterning defects, reduced proliferation, increased apoptosis, upregulated canonical Wnt/β-catenin.

**Does not capture:** hair (fish don't have any), the adaptive immune phenotype, anemia, Hirschsprung disease, malignancy predisposition. Also *promotes* vertebral ossification — a direction opposite to the general hypo-ossification story, which the authors themselves flag as variable.

**Applications:** skeletal development mechanism; and crucially it's the only system with a **pharmacological rescue** (Wnt inhibition), making it the natural platform for drug screening.

Suggested dismech shape: `animal_models` entry, `species: Zebrafish`, `modeled_mechanisms` with `target: <chondrodysplasia node>`, `relationship: PARTIALLY_RECAPITULATES`, `fidelity: MODERATE`, `limitations` naming the missing hair/immune/hematologic arms, and readouts for chondrogenesis and vertebral mineralization. The Wnt-inhibitor arm gets a `RESTORED` readout.

### Mouse

**No viable germline *Rmrp* knockout mouse exists** — constitutive loss is presumed embryonic lethal (RNase MRP is essential). What does exist:

- **Mouse primary T cells carrying *Rmrp* mutations** — Robertson 2022 (PMID:35115551) showed *"mutations in RMRP impair mouse T cell activation and delay pre-rRNA processing."* This is the model for the **immune** arm specifically.
- Rogler 2014 (PMID:24009312) used transgenic/knockdown approaches for the small-RNA silencing work.

`relationship: RECAPITULATES` for the T-cell activation node only; `fidelity: MODERATE`; `limitations`: cell-level, not organismal; doesn't address skeletal or hair phenotype.

### Human cellular models — the strongest evidence base

This is where CHH is actually best modeled, which makes sense for a disease this developmentally embedded.

| System | Findings | PMID |
|---|---|---|
| **Patient-derived fibroblasts** | Delayed pre-rRNA processing; G2→M delay; 35 up/130 down transcriptome; reduced RMRP-S1/S2 | 35115551, 31551465, 24009312 |
| **CRISPR *RMRP* disruption, human cell lines** | Growth arrest with pre-rRNA accumulation | 35115551, 28115465 |
| **Engineered 70AG human cells** | Specifically impaired pre-rRNA processing; reduced mature rRNA; **reduced cytosolic:mitochondrial ribosome ratio**; reduced intact RNase MRP complexes | 35115551 |
| **Patient B-cell line** | Reduced RMRP-S1/S2 | 24009312 |
| **CHH patient lymphocyte cultures** | In-vitro growth defect; short telomeres; reduced telomerase activity | 28126377 |
| **CHH fibroblast chondrogenic differentiation** | Pathway dissection of chondrogenesis | 34988338 |
| **Chondrocyte hypertrophy models** | *RMRP* expression dynamically regulated; determines chondrogenic differentiation | 28743979 |
| **Yeast (*S. cerevisiae*)** | 70A>G alters 5.8S rRNA ratio | 16254002 |

For dismech, most of these belong in `experimental_models:` (non-animal systems) with `modeled_mechanisms` links, per the CLAUDE.md distinction. The **engineered 70AG human cell line** is the single highest-fidelity model of the causal mechanism available and deserves `fidelity: HIGH` for the pre-rRNA processing node.

**Notably absent:** iPSC-derived chondrocytes or organoids from CHH patients; no CHH entry in DepMap-style functional-genomics resources beyond the CRISPR growth-arrest observation. Real opportunity, real gap.

### Model limitations, collectively

Nothing available reproduces the **full** pleiotropy. The skeleton has a fish, the immune system has mouse T cells and human lymphocytes, the ribosome mechanism has engineered human cells — and **nothing at all** models the hair phenotype, the Hirschsprung association, or the lymphoma predisposition in vivo. If the entry carries a `HUMAN_MODEL_MISMATCH` discussion, that's the shape of it: the models are each faithful to one arm and blind to the others, so no single system can test a claim about the disease as a whole.

---

## Suggested dismech pathograph skeleton

Sketching the node/edge structure since that's the actual deliverable target:

```
Biallelic RMRP loss-of-function                      [MOLECULAR]
  ├─▸ Reduced intact RNase MRP complex               [MOLECULAR]
  │     ├─▸ Impaired pre-rRNA ITS1 cleavage          [MOLECULAR]   ← Arm A
  │     │     └─▸ Reduced mature cytosolic rRNA / ribosome deficit [CELLULAR]
  │     │           ├─▸ Impaired chondrocyte proliferation [CELLULAR]
  │     │           │     └─▸ Metaphyseal dysplasia   [TISSUE]
  │     │           │           └─▸ Short-limb short stature [ORGANISM]
  │     │           └─▸ Impaired erythroid progenitor proliferation [CELLULAR]
  │     │                 └─▸ Macrocytic anemia       [ORGANISM]
  │     ├─▸ Impaired cyclin B1/B2 mRNA cleavage       [MOLECULAR]   ← Arm B
  │     │     └─▸ G2→M transition delay               [CELLULAR]
  │     │           ├─▸ Impaired T-cell proliferation/activation [CELLULAR]
  │     │           │     └─▸ Combined immunodeficiency [ORGANISM]
  │     │           │           ├─▸ Recurrent infection → bronchiectasis [TISSUE]
  │     │           │           └─▸ Immune dysregulation → autoimmunity [ORGANISM]
  │     │           └─▸ Impaired hair follicle keratinocyte proliferation [CELLULAR]
  │     │                 └─▸ Hypotrichosis           [ORGANISM]
  │     ├─▸ Impaired telomerase activity / telomere shortening [MOLECULAR] ← Arm C
  │     │     └─▸ Lymphocyte replicative exhaustion   [CELLULAR]
  │     └─▸ Reduced RMRP-S1/S2 small RNAs             [MOLECULAR]   ← Arm D
  │           └─▸ Dysregulated PTCH2/SOX4 developmental programs [CELLULAR]
  └─▸ (zebrafish) Upregulated canonical Wnt/β-catenin [CELLULAR]    ← Arm E

Combined immunodeficiency + telomere dysfunction ──▸ Lymphomagenesis (NHL) [ORGANISM]
```

Candidate **module conformance**: this entry is a natural conformer for a *ribosomopathy* module if one gets built (alongside Diamond-Blackfan, Shwachman-Diamond, Treacher Collins — note `pharyngeal_arch_patterning_serial_homology` already covers the TCOF1 ribosome-biogenesis→neural-crest route, and the zebrafish pharyngeal arch finding here is a suggestive but **not sufficient** link — don't wire it without evidence). Also plausibly `myelosuppression`-adjacent for the cytopenia arm, though that module is scoped to *drug* toxicity, so probably not.

---

## Gaps and cautions for curation

1. **Ontology IDs above are suggestions.** Run `just validate-terms` before any of them land. I flagged the ones I'm least sure of; the vertebral-column and hair-follicle-keratinocyte ones especially.
2. **Variant nomenclature is genuinely inconsistent** across the literature (n.71A>G / g.70A>G / n.72A>G / c.70A>G for the same allele). Pick one canonical form, record aliases in `notes:`, and don't let two forms coexist in the entry as if they were different variants.
3. **Most frequency figures come from GeneReviews prose, not from quotable abstract sentences.** Per the frequency-evidence SOP, omit the band rather than attach a snippet that only supports the association.
4. **The Finnish cohort dominates the quantitative literature.** Prevalence, mortality, autoimmunity, and cancer figures are all Finnish-founder-population estimates. Say so in `population:` fields rather than presenting them as global.
5. **Genuine knowledge gaps** worth `discussions` entries: the mechanism of the telomerase defect (*"as yet unidentified"*); the absence of identified modifier genes despite documented intrafamilial variability; the HSCT-and-growth discrepancy between Bordon and GeneReviews; no QoL instrument data; no metabolomic/proteomic/single-cell data; no model of the hair, Hirschsprung, or lymphoma arms.
6. **Don't conflate** germline *RMRP* loss-of-function (this disease) with *RMRP* over-expression as an oncogenic lncRNA in sporadic cancers. Same gene, opposite direction, unrelated biology.

---

## Sources

- [GeneReviews: Cartilage-Hair Hypoplasia – Anauxetic Dysplasia Spectrum Disorders (PMID:22420014, rev. 2025-08-07)](https://www.ncbi.nlm.nih.gov/books/NBK84550/)
- [Vakkilainen S. Cartilage-hair hypoplasia: A comprehensive review. J Hum Immun 2025 (PMID:42170584)](https://rupress.org/jhi/article/1/4/e20250142/278347/Cartilage-hair-hypoplasia-A-comprehensive)
- [Ridanpää M et al. Cell 2001 (PMID:11207361)](https://www.sciencedirect.com/science/article/pii/S0092867401002057)
- [Robertson N et al. Nat Commun 2022 (PMID:35115551)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8814244/)
- [Vakkilainen S et al. Front Immunol 2019 — 30-year follow-up (PMID:31379817)](https://europepmc.org/article/MED/31379817)
- [Vakkilainen S et al. Front Immunol 2018 — autoimmunity (PMID:30410491)](https://europepmc.org/article/MED/30410491)
- [Vakkilainen S et al. Sci Rep 2019 — G2 cell cycle (PMID:31551465)](https://europepmc.org/article/MED/31551465)
- [Aubert G et al. J Allergy Clin Immunol 2017 — telomeres (PMID:28126377)](https://europepmc.org/article/MED/28126377)
- [Sun X et al. J Bone Miner Res 2019 — zebrafish (PMID:31237961)](https://europepmc.org/article/MED/31237961)
- [Bordon V et al. Blood 2010 — EBMT HSCT cohort (PMID:20375313)](https://europepmc.org/article/MED/20375313)
- [Vakkilainen S et al. J Clin Immunol 2021 — lung imaging (PMID:33675005)](https://europepmc.org/article/MED/33675005)
- [Vakkilainen S et al. Front Immunol 2020 — live vaccines (PMID:32849667)](https://europepmc.org/article/MED/32849667)
- [Taskinen M et al. Am J Med Genet A 2008 — cancer risk (PMID:18698627)](https://europepmc.org/article/MED/18698627)
- [Thiel CT et al. Am J Hum Genet 2007 — genotype-phenotype (PMID:17701897)](https://europepmc.org/article/MED/17701897)
- [Hermanns P et al. Hum Mol Genet 2005 (PMID:16254002)](https://academic.oup.com/hmg/article/14/23/3723/559481)
- [Rogler LE et al. Hum Mol Genet 2014 — RMRP-S1/S2 (PMID:24009312)](https://europepmc.org/article/MED/24009312)
- [Kavadas FD et al. J Allergy Clin Immunol 2008 (PMID:18804272)](https://europepmc.org/article/MED/18804272)
- [Orthopaedic manifestations of CHH, 135 patients (PMID:25764362)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4417732/)
- [Hussen BM et al. Front Cell Dev Biol 2021 — RMRP lncRNA review (PMID:33996836)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8120005/)
- [Tan R et al. J Clin Immunol 2023 — promoter duplications/SCID (PMID:37115363)](https://europepmc.org/article/MED/37115363)
- [Gomes ME et al. Sci Rep 2024 — Brazilian founder (PMID:38862721)](https://europepmc.org/article/MED/38862721)
- [Arponen H et al. Front Endocrinol 2021 — craniofacial (PMID:34956076)](https://europepmc.org/article/MED/34956076)
- [Orphanet: Cartilage-hair hypoplasia (ORPHA:175)](https://www.orpha.net/en/disease/detail/175)
- [MONDO:0009595 via OLS4](https://www.ebi.ac.uk/ols4/ontologies/mondo/classes?obo_id=MONDO:0009595)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 63 |
| Resolved | 63 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |

All extracted references resolved successfully.