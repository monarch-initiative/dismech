---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-07-31T18:26:04.961473'
end_time: '2026-07-31T18:45:22.923270'
duration_seconds: 1157.96
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Microcephaly-Capillary Malformation Syndrome
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
  num_turns: 91
  total_cost_usd: 6.57161775
  session_id: 91f0adb8-08c0-45eb-b61d-b3a39e0132fb
  stop_reason: end_turn
citation_count: 32
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Microcephaly-Capillary Malformation Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Microcephaly-Capillary Malformation Syndrome** covering all of the
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

# Microcephaly–Capillary Malformation Syndrome (MIC-CAP): Comprehensive Research Report

**Prepared:** 2026-07-31 · **Target MONDO:** MONDO:0013659 · **Category:** Mendelian (autosomal recessive)

---

## Evidence-provenance note (read before curating)

Quotes below are marked with a verification status, because the dismech SOP requires evidence `snippet:` values to be exact substrings of a validator-generated `references_cache/` file:

- **[CACHE-VERIFIED]** — quote checked character-for-character against an existing file in `references_cache/` in this worktree (PMIDs 24354023, 23542699, 39169623, 36033615, 27531570, 29907875, 25692795, 31638258, 25266620).
- **[TRANSCRIBED]** — quote obtained by transcription of the live PubMed record via web fetch. High confidence, but **run `just fetch-reference PMID:<id>` and `just validate-references` before committing** (PMIDs 21815250, 35962715, 38951308, 11713295, 21531206, 18758443, 33253913, 40441142).
- **[SOURCE-PARAPHRASE]** — factual content from GeneReviews/Orphanet/HPO/ClinVar/UniProt web records, not suitable as a verbatim snippet without re-fetch.

Ontology IDs were checked against OLS4 / the HPO API where noted; a handful are flagged **[VERIFY]**.

---

## 1. Disease Information

### Overview

Microcephaly–capillary malformation syndrome (MIC-CAP) is an ultra-rare autosomal recessive neurocutaneous disorder — formally a *developmental and epileptic encephalopathy with a cutaneous vascular signature* — defined by the co-occurrence of **congenital and progressive microcephaly**, **multiple small generalized cutaneous capillary malformations**, **early-onset intractable epilepsy**, **profound global developmental delay**, and **hypoplastic distal phalanges**. It is caused by biallelic loss-of-function variants in *STAMBP*, which encodes the endosome-associated K63-specific deubiquitinating isopeptidase AMSH.

The defining GeneReviews summary [CACHE-VERIFIED, PMID:24354023]:

> "The defining clinical characteristics of the microcephaly-capillary malformation (MIC-CAP) syndrome are typically present at birth: microcephaly and generalized cutaneous capillary malformations (a few to hundreds of oval/circular macules or patches varying in size from 1-2 mm to several cm), hypoplastic distal phalanges of the hands and/or feet, early-onset intractable epilepsy, and profound developmental delay."

And the molecular definition [CACHE-VERIFIED, PMID:23542699]:

> "Microcephaly-capillary malformation (MIC-CAP) syndrome is characterized by severe microcephaly with progressive cortical atrophy, intractable epilepsy, profound developmental delay and multiple small capillary malformations on the skin."

MIC-CAP is conceptually the **mirror image** of megalencephaly–capillary malformation (MCAP/M-CM, *PIK3CA*-related overgrowth): both couple a capillary malformation phenotype to a PI3K-AKT-mTOR signaling abnormality, but MCAP is a mosaic gain-of-function overgrowth disorder while MIC-CAP is a germline recessive loss-of-function undergrowth disorder. This pairing is a useful curation anchor and a common source of **Named Entity Confusion (NEC)** — see §1.4.

### Key identifiers

| Resource | Identifier | Notes |
|---|---|---|
| MONDO | **MONDO:0013659** | label: `microcephaly-capillary malformation syndrome` (OLS4-verified) |
| OMIM (disease) | **#614261** | MICROCEPHALY-CAPILLARY MALFORMATION SYNDROME; MICCAP |
| OMIM (gene) | ***606247*** | STAMBP |
| Orphanet | **ORPHA:294016** | "Microcephaly-capillary malformation syndrome" |
| UMLS | C3280296 | via NIH GTR condition page |
| HGNC | **HGNC:16950** → dismech CURIE `hgnc:16950` | STAMBP (lowercase prefix per repo convention) |
| NCBI Gene | 10617 | |
| Ensembl | ENSG00000124356 | |
| UniProt | **O95630** (STABP_HUMAN) | STAM-binding protein |
| GeneReviews | NBK174452 / PMID:24354023 | Carter, Mirzaa, McDonell, Boycott; posted 2013-12-12, updated **2021-03-18** |
| ICD-10 | No specific code. Coded compositionally: **Q02** (microcephaly) + **Q82.5** (congenital non-neoplastic nevus) | Orphanet maps ORPHA:294016 to Q02 |
| ICD-11 | No specific stem code; nearest are LD24.M0 (microcephaly) / LA90 congenital vascular malformation of skin **[VERIFY against current ICD-11 release]** |
| MeSH | No dedicated descriptor. Indexed via *Microcephaly* (D008831), *Vascular Malformations* (D054079), *Ubiquitin Thiolesterase* (D043422), *Endosomal Sorting Complexes Required for Transport* | |

### Synonyms and alternative names

- MIC-CAP syndrome (the standard abbreviation)
- MICCAP (OMIM style)
- Microcephaly–capillary malformation syndrome
- STAMBP-related microcephaly–capillary malformation syndrome
- *Historical/descriptive*: "A new syndrome with multiple capillary malformations, intractable seizures, and brain and limb anomalies" (Carter et al. 2011, Am J Med Genet A 155A:301–306, the original delineation)
- *Emerging/broader*: **STAMBP-related neurodevelopmental disorder** — justified by PMID:36033615, which reported a *STAMBP* patient **without** cutaneous capillary malformation

### Data provenance character

Essentially all human knowledge of MIC-CAP is **aggregated case-level literature**, not EHR- or registry-derived: a series of single-family case reports plus one multiplex exome cohort (PMID:23542699, 5 families) and one follow-up delineation series (PMID:35962715, 4 new + 2 followed patients). There is **no patient registry, no natural-history study, no EHR-derived cohort, and no ICEES/COHD-type comorbidity signal** for this disease. Curators should expect `CASES_IN_LITERATURE` to be the only defensible `measure_type` for prevalence.

### NEC preflight (mandatory before using any deep-research output)

MIC-CAP sits in **two high-NEC-risk classes** simultaneously:

1. **Near-homograph collision**: **MIC-CAP** (microcephaly, *STAMBP*, AR, MONDO:0013659, OMIM 614261) vs. **MCAP / M-CM** (mega*lencephaly*-capillary malformation-polymicrogyria, *PIK3CA*, mosaic, MONDO:0013192, OMIM 602501). Identical "capillary malformation" token, opposite head-size direction, opposite mutational mechanism. A DR report that repeatedly names **PIK3CA** or describes **overgrowth/somatic mosaicism/alpelisib** is describing MCAP, not MIC-CAP — **discard entirely**.
2. **Capillary-malformation family collision**: CM-AVM syndrome (*RASA1*/*EPHB4*, AD), Sturge-Weber (*GNAQ*, mosaic), and diffuse capillary malformation with overgrowth all share the CM token.

**Anchors:** the causal gene must be **STAMBP**; OMIM xref must be **614261**; inheritance must be **autosomal recessive**; head size must be **micro**cephaly. If any of these four disagree with the DR report, rebuild from primary literature.

---

## 2. Etiology

### Disease causal factors

MIC-CAP is **monogenic and fully genetically determined**: biallelic (homozygous or compound heterozygous) pathogenic variants in *STAMBP* (2p13.1). There is no known environmental, infectious, or multifactorial contribution. The landmark discovery [CACHE-VERIFIED, PMID:23542699]:

> "We used whole-exome sequencing of five patients with MIC-CAP syndrome and identified recessive mutations in STAMBP, a gene encoding the deubiquitinating (DUB) isopeptidase STAMBP (STAM-binding protein, also known as AMSH, associated molecule with the SH3 domain of STAM) that has a key role in cell surface receptor-mediated endocytosis and sorting."

Confirmed independently [CACHE-VERIFIED, PMID:29907875]:

> "Microcephaly-capillary malformation syndrome is a congenital and neurodevelopmental disorder caused by biallelic mutations in the STAMBP gene."

### Risk factors

**Genetic (causal):**
- Biallelic *STAMBP* pathogenic variants — necessary and sufficient. `GENO` relationship type: `CAUSAL`.
- **Consanguinity** is the single strongest population-level risk factor, and drives homozygous presentations. Documented in an Egyptian family [CACHE-VERIFIED, PMID:27531570]: *"We describe two brothers from a consanguineous family of Egyptian ancestry"*; in a Saudi family [CACHE-VERIFIED, PMID:25266620]: *"We describe two brothers (ages 7 and 12 years) from consanguineous parents of Saudi ancestry"*; and in an Arab family (PMID:25692795, MeSH-indexed `Consanguinity`).
- **Carrier parents** (obligate heterozygotes) — asymptomatic; see §9.
- **Uniparental isodisomy (UPD)** is an unusual but documented non-Mendelian route [CACHE-VERIFIED, PMID:24354023]: *"in some instances both pathogenic variants are inherited from one parent (uniparental isodisomy)."* GeneReviews attributes this to 1/15 families (maternal isodisomy of chromosome 2 homozygosing p.Arg424*, patient P4.1 in PMID:23542699).

**Environmental:** **None identified.** No toxin, teratogen, radiation, occupational, dietary, maternal-age, or infectious risk factor has been implicated. This is an important negative for the KB — MIC-CAP is a mechanistically "pure" genetic microcephaly, in explicit contrast to acquired congenital microcephalies (congenital Zika, CMV, toxoplasmosis, fetal alcohol spectrum), which are the principal **differential** rather than co-factors.

**Sex:** No sex bias expected or reported (autosomal recessive). Reported patients include both sexes.

### Protective factors

- **Genetic:** No modifier or protective allele identified. However, **residual protein expression is strongly protective at the phenotype level** — a genotype-driven "protective" gradient rather than a separate locus. GeneReviews describes a female homozygous for the leaky intronic variant c.1005+358A>G with *"threefold reduction in STAMBP transcript expression; STAMBP protein expression was markedly reduced but not absent"* who *"achieved independent walking and short-phrase speech at age five"* [SOURCE-PARAPHRASE, GeneReviews NBK174452] — far exceeding the typical outcome of no head control and no independent sitting.
- **Environmental:** None. No diet, supplement, or exposure is known to modify risk or course. (Ketogenic diet is a *treatment* for the epilepsy, not a protective factor — and in the one reported trial it failed; see §12.)

### Gene–environment interactions

No established GxE interaction. Two **iatrogenic gene–environment style interactions** are clinically actionable and should be curated as treatment-safety items rather than etiologic factors:

1. **Valproic acid caution.** [CACHE-VERIFIED, PMID:24354023]: *"Agents/circumstances to avoid: Valproic acid may or may not be associated with adverse effects."* GeneReviews elaborates that one male died at 12 months of *"septic shock following acute pancreatitis, possibly secondary to valproate therapy"*, while other patients tolerated valproate without issue [SOURCE-PARAPHRASE].
2. **Catabolic/infectious stress** precipitates decompensation via aspiration pneumonia and status epilepticus — a general severe-neurodisability interaction, not MIC-CAP-specific.

---

## 3. Phenotypes

### Authoritative frequency data

The HPO annotation set for OMIM:614261 (retrieved from the HPO API, `ontology.jax.org`) is the best-curated frequency source and should seed the dismech `phenotypes:` block. Frequencies are **n/N counted-cohort** values, which map cleanly to dismech `FrequencyEnum` bands with derivable justification (see `docs/frequency-evidence-guidelines.md`).

| HPO ID | Label (canonical) | HPO frequency | Derived band | System |
|---|---|---|---|---|
| **HP:0000253** | Progressive microcephaly | **10/10 (100%)** | OBLIGATE / VERY_FREQUENT | Head & neck |
| **HP:0025104** | Capillary malformation | **10/10 (100%)** | OBLIGATE / VERY_FREQUENT | Skin |
| **HP:0001250** | Seizure | **10/10 (100%)**, onset *in infancy* | VERY_FREQUENT | Nervous |
| **HP:0001263** | Global developmental delay | **10/10 (100%)** | VERY_FREQUENT | Nervous |
| **HP:0003577** | Congenital onset | **10/10 (100%)** | — (clinical course) | Clinical course |
| **HP:0009882** | Short distal phalanx of finger | **19/20 (95%)** | VERY_FREQUENT | Limbs |
| **HP:0009879** | Simplified gyral pattern | **9/9 (100%)** | VERY_FREQUENT | Nervous (imaging) |
| **HP:0012510** | Extra-axial cerebrospinal fluid accumulation | **9/9 (100%)** | VERY_FREQUENT | Nervous (imaging) |
| **HP:0001285** | Spastic tetraparesis | **8/10 (80%)** | VERY_FREQUENT | Musculature |
| **HP:0000648** | Optic atrophy | **6/8 (75%)** | FREQUENT | Eye |
| **HP:0001518** | Small for gestational age | **7/10 (70%)** | FREQUENT | Growth |
| **HP:0025517** | Hypoplastic hippocampus | **6/7 (86%)** | VERY_FREQUENT | Nervous (imaging) |
| **HP:0001336** | Myoclonus | **6/10 (60%)** | FREQUENT | Nervous |
| **HP:0003429** | CNS hypomyelination | **5/8 (63%)** | FREQUENT | Nervous (imaging) |
| **HP:0012469** | Infantile spasms | **4/9 (44%)** | FREQUENT | Nervous |
| HP:0011344 | Severe global developmental delay | reported | FREQUENT | Nervous |
| HP:0002059 | Cerebral atrophy | reported | FREQUENT | Nervous |
| HP:0012448 | Delayed myelination | reported | FREQUENT | Nervous |
| HP:0002079 | Hypoplasia of the corpus callosum | reported | OCCASIONAL | Nervous |
| HP:0001252 / HP:0001290 | Hypotonia / Generalized hypotonia | reported | FREQUENT | Musculature |
| HP:0001508 | Failure to thrive | reported | FREQUENT | Growth |
| HP:0004322 | Short stature | **Occasional** | OCCASIONAL | Growth |
| HP:0001156 | Brachydactyly | reported | FREQUENT | Limbs |
| HP:0030084 | Clinodactyly | reported | OCCASIONAL | Limbs |
| HP:0001792 | Small nail | reported | FREQUENT | Skin/nails |
| HP:0010721 | Abnormal hair whorl | reported | OCCASIONAL | Skin/hair |
| HP:0003196 | Short nose | reported | FREQUENT | Head & neck |
| HP:0000445 | Wide nose | reported | OCCASIONAL | Head & neck |
| HP:0000340 | Sloping forehead | reported | FREQUENT | Head & neck |
| HP:0000327 | Hypoplasia of the maxilla | reported | OCCASIONAL | Head & neck |
| HP:0000175 | Cleft palate | 1 individual | VERY_RARE | Head & neck |
| HP:0000508 | Ptosis | reported | OCCASIONAL | Eye |
| HP:0000316 | Hypertelorism | reported | OCCASIONAL | Eye |
| HP:0000365 | Hearing impairment | 1 individual (sensorineural) | VERY_RARE | Ear |
| HP:0000369 | Low-set ears | reported | OCCASIONAL | Ear |
| HP:0000076 | Vesicoureteral reflux | **Occasional** | OCCASIONAL | Genitourinary |
| HP:0001629 | Ventricular septal defect | reported | OCCASIONAL | Cardiovascular |
| HP:0001631 | Atrial septal defect | reported | OCCASIONAL | Cardiovascular |
| HP:0001655 | Patent foramen ovale | reported | OCCASIONAL | Cardiovascular |
| HP:0001667 | Right ventricular hypertrophy | reported | VERY_RARE | Cardiovascular |
| HP:0000007 | Autosomal recessive inheritance | — | — | Inheritance |

GeneReviews adds two counted frequencies out of its 18-individual denominator [SOURCE-PARAPHRASE, NBK174452]: *"Myoclonus of limbs and eyelids is common (8/18 reported individuals)"* and *"Optic atrophy (10/18 reported individuals)"*, plus single-case reports of sensorineural hearing impairment, cleft palate, and **adrenal insufficiency** (1 individual — no standard HP term beyond HP:0000846 Adrenal insufficiency).

### Phenotype-by-phenotype detail

**1. Progressive microcephaly (HP:0000253)** — *congenital onset, severe, progressive*
The cardinal feature and the one that most sharply separates MIC-CAP from MCAP. Occipitofrontal circumference (OFC) at birth ranges **−1.8 to −8 SD**, worsening to **−2.5 to −8 SD** on later assessment (PMID:23542699 Table 1) [SOURCE-PARAPHRASE]. The Chinese case illustrates the severity at 17 months [CACHE-VERIFIED, PMID:31638258]: *"The head circumference was 39.5 cm (Z-score, −5.8 SD)."* Because the head is small at birth **and** falls further across postnatal life, both `HP:0011451` (Congenital microcephaly) and `HP:0000253` (Progressive microcephaly) are defensible; **HP:0000253 with `clinical_course: PROGRESSIVE`** is the better single annotation and matches the HPO disease annotation. **QoL:** microcephaly per se is not symptomatic, but it is the imaging/biometric proxy for the neuronal loss that drives everything else.

**2. Generalized cutaneous capillary malformations (HP:0025104)** — *congenital, non-progressive in number, cosmetic*
The eponymous cutaneous sign. Morphology per GeneReviews suggestive-findings: *"Pink or red, blanchable, roughly oval or circular macules or patches"* distributed widely over the body [SOURCE-PARAPHRASE], numbering *"a few to hundreds"*, sized *"1-2 mm to several cm"* [CACHE-VERIFIED, PMID:24354023]; McDonell reports 2–20 mm lesions visible at birth [SOURCE-PARAPHRASE, PMID:23542699]. Confirmed across ancestries [CACHE-VERIFIED, PMID:27531570]: *"multiple cutaneous capillary malformations"*; and [CACHE-VERIFIED, PMID:31638258]: *"sporadic, multiple, small capillary malformations."* **Critically, they are not universal in the broadened *STAMBP* spectrum** — see phenotype 12. **QoL:** the lesions are asymptomatic and blanchable; the burden is cosmetic and diagnostic rather than functional. They do **not** carry the Sturge-Weber risks (no leptomeningeal angiomatosis, no glaucoma reported).

**3. Early-onset intractable epilepsy (HP:0001250; HP:0012469 infantile spasms; HP:0011097 epileptic spasms)** — *neonatal/infantile onset, severe, refractory, partially stabilizing*
The dominant morbidity. GeneReviews: seizures *"can be focal, tonic, and complex partial and can include infantile spasms, appear to stabilize after age two years"* [CACHE-VERIFIED, PMID:24354023]. The natural history in a single well-documented case [CACHE-VERIFIED, PMID:31638258]: *"The child developed early-onset epilepsy after 3 months, with a generalized tonic-clonic seizure, which progressed to clusters of infantile spasms (2–10 clusters/day) 1 month later."* Multi-drug refractoriness is the rule [CACHE-VERIFIED, PMID:24354023]: *"multiple anticonvulsant medications are frequently required for adequate seizure control."* The disorder is now framed as a **recognizable developmental and epileptic encephalopathy (DEE)** (PMID:35770778, *Epileptic Disord* 2022, title). **EEG:** interictal hypsarrhythmia is documented [CACHE-VERIFIED, PMID:31638258]: *"Interictal electroencephalography showed hypsarrhythmia and slow wave background with bioccipital spike-slow wave during waking."* Suggested terms: HP:0002521 (Hypsarrhythmia), HP:0011153 (Focal motor seizure), HP:0002069 (Bilateral tonic-clonic seizure), HP:0011098 (Speech apraxia — n/a), HP:0032794 (Refractory epilepsy) **[VERIFY]**. **QoL:** the single largest driver — status epilepticus risk, sedation from polypharmacy, sleep disruption, caregiver burden.

**4. Profound global developmental delay / intellectual disability (HP:0001263, HP:0011344)** — *congenital, profound, static-to-slowly-regressive*
Universal (10/10). GeneReviews: *"Developmental progress is minimal. Most individuals do not attain head control or independent sitting due to spastic quadriparesis"* [SOURCE-PARAPHRASE]. Suggested: HP:0002187 (Profound global developmental delay) **[VERIFY]** as a more specific alternative to HP:0011344. **QoL:** total dependence for all activities of daily living.

**5. Spastic quadriparesis with central hypotonia (HP:0001285, HP:0001290)** — *infantile, progressive*
8/10 (HPO); 9/10 in the McDonell series. The **mixed tone** pattern is clinically distinctive and management-relevant [CACHE-VERIFIED, PMID:24354023]: *"Central hypotonia and peripheral hypertonia require attention to proper seating and bracing to maintain posture and prevent contractures."* **QoL:** contractures, positioning pain, scoliosis risk, inability to sit.

**6. Myoclonus and hyperkinetic movement disorder (HP:0001336; HP:0002072 chorea; HP:0002072/HP:0100660 dyskinesia)** — *infantile, chronic*
[CACHE-VERIFIED, PMID:24354023]: *"Myoclonus of the limbs and eyelids is common; other abnormal movements (dyskinetic, choreiform) may be seen."* Prominent dyskinesia was the notable feature of the Chinese case [CACHE-VERIFIED, PMID:31638258]: *"The boy could not hold his head and had prominent dyskinesia of the whole body, particularly involuntary movement of the tongue and mouth"* — and the authors note *"dyskinesia was more prominent in the present study and was infrequent in previous cases."* Suggested: HP:0100660 (Dyskinesia) **[VERIFY]**, HP:0002072 (Chorea) **[VERIFY]**.

**7. Hypoplastic distal phalanges and nail hypoplasia (HP:0009882, HP:0001792, HP:0001156)** — *congenital, static*
19/20 — the most reliable *non-neurological, non-cutaneous* diagnostic handle, and the feature that most efficiently separates MIC-CAP from primary autosomal recessive microcephaly on physical exam. Affects hands **and/or** feet.

**8. Ophthalmologic involvement (HP:0000648 optic atrophy; HP:0000618 blindness)** — *infantile, progressive*
6/8 to 10/18. Congenital blindness reported in the Egyptian sibs [CACHE-VERIFIED, PMID:27531570]: *"presenting with microcephaly, apparent global developmental delay, seizures, spasticity, congenital blindness, and multiple cutaneous capillary malformations."* Structurally correlated with hypoplasia of the optic nerves/chiasm on MRI. **QoL:** compounds the sensory deprivation of profound ID.

**9. Growth failure / feeding difficulty (HP:0001508, HP:0001518, HP:0004322, HP:0011968 feeding difficulties)** — *congenital→postnatal, progressive*
SGA in 7/10; postnatal failure to thrive near-universal. [CACHE-VERIFIED, PMID:31638258]: *"the patient was 8 kg [Z-score, −2.8 Standard Deviation (SD)] in weight and 63 cm (Z-score, −6.8 SD) in length."* Feeding-tube dependence is standard of care [CACHE-VERIFIED, PMID:24354023]: *"A feeding tube is essential to optimize nutrition and weight gain while reducing the risk of aspiration."* **QoL:** aspiration pneumonia is a leading proximate cause of hospitalization and death.

**10. Dysmorphic facial features** — *congenital, static*
Sloping forehead (HP:0000340), short nose (HP:0003196), wide nose (HP:0000445), maxillary hypoplasia (HP:0000327), low-set ears (HP:0000369), ptosis (HP:0000508), hypertelorism (HP:0000316). [CACHE-VERIFIED, PMID:29907875]: *"severe global developmental delay, progressive microcephaly, refractory seizures, dysmorphic facial features, and multiple capillary malformations."* [CACHE-VERIFIED, PMID:31638258]: *"The patient had drooping mouth corners, a short nose and neck."*

**11. Rare/expanding features (each 1–2 individuals; curate as VERY_RARE with the specific PMID)**
- **Congenital hypothyroidism** (HP:0000851) — two independent families. [CACHE-VERIFIED, PMID:25692795]: *"previously unreported findings of congenital hypothyroidism and alopecia areata."* [CACHE-VERIFIED, PMID:25266620]: *"these boys exhibited certain novel and distinctive phenotypic features (congenital hypothyroidism and autistic-like behavior with intermittent repetitive hand-flapping movements)."* Two-family replication makes this the strongest of the "rare" features.
- **Alopecia areata** (HP:0002232) — PMID:25692795.
- **Autistic behavior / stereotypies** (HP:0000729, HP:0000733) — PMID:25266620 (hand-flapping); PMID:36033615 (formal ASD diagnosis).
- **Adrenal insufficiency** (HP:0000846) — 1 individual, GeneReviews.
- **Cleft palate** (HP:0000175), **sensorineural hearing impairment** (HP:0000407) — 1 individual each.
- **Congenital heart defects** — VSD/ASD/PFO/RVH.
- **Vesicoureteral reflux** (HP:0000076).
- **Recurrent pneumonia** (HP:0006532) — [CACHE-VERIFIED, PMID:31638258]: *"received immunoglobulin intravenously as a result of recurrent pneumonia."*
- **Recurrent unilateral epistaxis** (HP:0000421) — PMID:38058451 (dual MIC-CAP + Mowat-Wilson diagnosis; attribute cautiously).

**12. Phenotype-expansion caveat — capillary malformation is NOT obligate**
The most important recent nosological finding for KB scoping [CACHE-VERIFIED, PMID:36033615]:

> "The patient was presented with global developmental delay, autism spectrum disorder, microcephaly, epilepsy, and dysmorphic facial features but without apparent capillary malformation on the skin and organs."

and:

> "Our findings demonstrate that the clinical phenotype of STAMBP mutations is highly variable, and patients with different STAMBP mutations show differences in the severity of symptoms."

**Curation implication:** the disease entity should be framed as *STAMBP-related neurodevelopmental disorder, of which classic MIC-CAP is the severe/complete form*. The dismech entry should keep the MIC-CAP name (matching MONDO:0013659) but record this variability in `notes` or as a `has_subtypes` split (classic MIC-CAP vs. attenuated/CM-negative *STAMBP*-NDD), and should **not** encode `HP:0025104` as strictly obligate.

**Quality-of-life summary.** No EQ-5D, SF-36, PROMIS, PedsQL, or any validated instrument has been applied to a MIC-CAP cohort — a genuine and citable evidence gap. Inferentially, affected children sit at the most severe end of the pediatric neurodisability spectrum: GMFCS-equivalent level V, no independent sitting, no speech, cortical visual impairment, gastrostomy dependence, refractory epilepsy. Caregiver burden is correspondingly extreme, and GeneReviews explicitly recommends *"a complex care / palliative care team"* [CACHE-VERIFIED, PMID:24354023].

---

## 4. Genetic / Molecular Information

### Causal gene

**STAMBP** — "STAM binding protein" (HGNC:16950, `hgnc:16950`), **2p13.1**, Entrez 10617, ENSG00000124356, OMIM *606247. Reference transcript **NM_006463.4** (used by PMID:29907875). Protein: **STAM-binding protein / AMSH** (UniProt **O95630**), **424 aa**.

Protein architecture (UniProt O95630; PMID:18758443; PMID:40441142):

| Region | Approx. residues | Function |
|---|---|---|
| **MIT domain** (microtubule-interacting and trafficking) | N-terminal ~1–100 | Binds ESCRT-III CHMP proteins (CHMP1A/CHMP3); **autoinhibits the catalytic domain** |
| **SH3-binding motif (SBM)** | ~residues 219–240 (includes Ser236) | Binds the SH3 domain of STAM1/STAM2; recruits AMSH to the ESCRT-0 complex; required for protein stability |
| **Clathrin-binding region** | central | endosomal/clathrin association |
| **MPN⁺/JAMM domain** (catalytic) | **257–388**, JAMM motif **335–348** | Zn²⁺-dependent isopeptidase; K63-linkage-specific |
| Zn²⁺ coordination | H335, H337, D348 (+ contacts at 350, 390, 396, 398; indirect at 280) | 2 Zn²⁺ per subunit |

Enzymology: EC 3.4.19.- zinc metalloprotease. **Strictly K63-linkage-selective** — cleaves Lys63-linked polyubiquitin, does **not** cleave Lys48-linked chains (UniProt; PMID:18758443).

### Pathogenic variant spectrum

Nine families from the discovery cohort [SOURCE-PARAPHRASE, PMID:23542699 / PMC4000253]:

| Patient | cDNA | Protein | Zygosity | Ancestry |
|---|---|---|---|---|
| P1.1 / P1.2 (sibs) | c.125A>G ; c.532C>T | p.Glu42Gly ; p.Arg178* | comp het | African-American |
| P2.1 | c.112C>T ; c.279+5G>T | p.Arg38Cys ; splice | comp het | European |
| P3.1 | c.299T>A ; c.1270C>T | p.Phe100Tyr ; p.Arg424* | comp het | European |
| P4.1 | c.1270C>T | p.Arg424* | **homozygous by maternal isodisomy** | European |
| P5.1 | c.1005+358A>G | deep-intronic, **leaky** splicing | homozygous | European |
| P6.1 | c.1134_1138delACTAA ; c.203+5G>A | p.Lys378Asnfs*2 ; splice | comp het | European |
| P7.1 | c.112C>T ; c.203+5G>A | p.Arg38Cys ; splice | comp het | European |
| P8.1 | c.112C>T ; c.938C>T | p.Arg38Cys ; **p.Thr313Ile** | comp het | European |
| P9.1 | c.41G>C ; (2nd) | p.Arg14Pro ; — | comp het | Polynesian |

Variants added by later reports:

| Variant | Protein | Zygosity | Population | Reference |
|---|---|---|---|---|
| c.908A>G | **p.Lys303Arg** | homozygous | Egyptian (consanguineous) | [CACHE-VERIFIED, PMID:27531570]: *"we uncovered a homozygous missense variant in STAMBP (p.K303R) in the two siblings, inherited from heterozygous carrier parents"* |
| c.707C>T | **p.Ser236Phe** (SH3-binding motif) | homozygous | Japanese | [CACHE-VERIFIED, PMID:29907875]: *"the novel homozygous mutation located in the SH3 binding motif of STAMBP (NM_006463.4) (c.707C>T: p.Ser236Phe)"* |
| novel splice variant | — | homozygous | Arab (Saudi/Kuwaiti) | PMID:25692795 (also PMID:25266620 sibs) |
| c.843_844del ; c.920G>A | **p.Cys282Trpfs\*11 ; p.Gly307Glu** | comp het | Chinese | [CACHE-VERIFIED, PMID:36033615] |
| novel variant | — | — | Chinese | PMID:31638258 |
| **c.376-1G>A** (intron 4 splice acceptor) | — | — | Indian | PMID:41603106 (2026) |
| novel variants | — | — | Chinese (co-occurring Mowat-Wilson) | PMID:38058451 |

**Recurrent variants:** **p.Arg38Cys** (c.112C>T) is the clearest recurrent allele — 3 of 9 discovery families. **p.Arg424\*** (c.1270C>T) recurs in 2 families. These are the two alleles worth flagging for targeted testing.

**ClinVar snapshot** (STAMBP, P/LP query; 52 records) [SOURCE-PARAPHRASE] — representative classified entries:

| Variant | Consequence | Germline classification | Condition |
|---|---|---|---|
| c.133C>T (p.Arg45Ter) | nonsense | Likely pathogenic (multiple submitters, no conflicts) | MIC-CAP |
| c.5_6dup (p.Asp3fs) | frameshift | **Pathogenic** | MIC-CAP |
| c.487dup (p.His163fs) | frameshift | **Pathogenic** | — |
| c.376-1G>A | splice acceptor | Likely pathogenic | MIC-CAP |
| c.1006-2A>T | splice acceptor | Likely pathogenic | MIC-CAP |
| c.868-1G>A | splice acceptor | Likely pathogenic | — |
| c.113G>A (p.Arg38His) | missense | **Conflicting classifications** | MIC-CAP |
| c.824C>G (p.Thr275Ser) | missense | VUS | MIC-CAP |
| c.41G>T (p.Arg14Leu), c.32C>T (p.Pro11Leu), c.692C>G (p.Pro231Arg) | missense | VUS | — |

**Variant-class distribution:** the spectrum is dominated by **truncating (nonsense/frameshift) and splice-disrupting alleles**, with a minority of missense. This is a classic complete-loss-of-function architecture.

**Structural clustering of missense alleles — an important and under-appreciated pattern.** McDonell noted that **five of six** discovery missense variants (**R14P, R38C, E42G, Y63C, F100Y**) cluster in the **N-terminal MIT domain**, not the catalytic JAMM domain [SOURCE-PARAPHRASE, PMC4000253]. The single JAMM-domain missense, **p.Thr313Ile**, sits *"in the distal ubiquitin binding site within the JAMM domain"* and *"eliminates a hydrogen bond between the ubiquitin carbon backbone and STAMBP, likely decreasing ubiquitin binding."* Later alleles fit the same picture: **S236F** in the SBM, **K303R** and **G307E** flanking the JAMM domain.

The 2025 structural work explains why MIT-domain mutations are so damaging [TRANSCRIBED, PMID:40441142]:

> "we conducted comprehensive biochemical analyses of full-length STAMBP and several fragments and demonstrated that the MIT domain binds tightly to the catalytic domain (CD), resulting in autoinhibition of its activity. The crystal structure of the MIT-CD complex reveals that the MIT domain occupies a large portion of the distal ubiquitin-binding site of the CD domain, thereby obstructing substrate binding. Additionally, our biochemical data show that STAM1 binding to STAMBP facilitates substrate binding and enhances its activity, whereas binding of CHMP3 does not relieve autoinhibition or enhance activity."

So the MIT domain is not a passive tether — it is a regulatory clamp whose relief requires STAM1 binding. MIT-domain and SBM missense variants therefore disrupt the **regulated activation** of AMSH and/or its stability, rather than the catalytic chemistry itself.

**Functional consequence class: LOSS OF FUNCTION**, achieved through at least two distinct routes:
1. **Protein destabilization / absence** — the dominant route. Directly shown for S236F [CACHE-VERIFIED, PMID:29907875]: *"Immunoblot analysis of patient-derived lymphoblastoid cell lines (LCLs) revealed a severe reduction in STAMBP expression, indicating that Ser236Phe induces protein instability."* The proposed mechanism is elegant: *"The substitution of Ser236Phe found in the case patient was located in the SH3-binding motif, and we propose the mutation may block STAM binding and subsequently induce STAMBP degradation."* Generalized in the discovery paper [CACHE-VERIFIED, PMID:23542699]: *"Patient cell lines showed reduced STAMBP expression."*
2. **Catalytic/substrate-binding impairment** — T313I.

No gain-of-function or dominant-negative mechanism is reported. Heterozygotes are unaffected, consistent with pure recessive LOF.

**Allele frequencies.** No MIC-CAP pathogenic allele reaches appreciable frequency in gnomAD; all reported disease alleles are rare or private. **Precise gnomAD constraint metrics (pLI, LOEUF, missense Z) for STAMBP could not be retrieved** — the gnomAD browser requires a GraphQL POST that the available tooling cannot issue. **Action for curator: query gnomAD v4 for ENSG00000124356 directly.** A priori, LOEUF is expected to be permissive (recessive genes are typically not LoF-constrained in heterozygotes).

**Somatic vs. germline.** MIC-CAP variants are **exclusively germline biallelic**. This is a sharp contrast to MCAP (mosaic somatic *PIK3CA*) and to Sturge-Weber (mosaic somatic *GNAQ*), and is worth an explicit `notes` statement to forestall confusion. Separately, *STAMBP* is recurrently dysregulated **somatically in cancer** — melanoma (SLUG stabilization, PMID:30454887), lung adenocarcinoma (EGFR/MAPK, PMID:34102455), pancreatic ductal adenocarcinoma (BAG3, PMID:41611844; gemcitabine resistance, PMID:39242557), colorectal cancer (YY1/c-Myc, PMID:41456274; CXCR4/MDSC, PMID:41559433). These are **oncology findings about the same protein, not about MIC-CAP**, and should not be imported into the disease entry except as a mechanistic cross-reference.

**Modifier genes.** None identified. The best candidate axis is *STAM1/STAM2*, given that STAM1 binding both stabilizes AMSH and relieves its autoinhibition (PMID:40441142) — a testable hypothesis, not an established modifier.

**Epigenetics.** No DNA methylation, histone-modification, or chromatin study of MIC-CAP exists. No episignature has been described (contrast: many NDDs now have EpiSign classifiers). **Genuine gap.** Note the mechanistic irony that *STAMBP* work is repeatedly published from the Shanghai Key Laboratory of *Medical Epigenetics* — this reflects lab affiliation, not an epigenetic disease mechanism.

**Chromosomal abnormalities.** No recurrent CNV. GeneReviews reports **0/15 families** with a detectable deletion/duplication, so CMA has essentially no diagnostic yield for MIC-CAP. The one structural mechanism of note is **uniparental isodisomy of chromosome 2**, which homozygoses a single paternal/maternal allele (1/15 families) and has direct recurrence-risk consequences (§9).

---

## 5. Environmental Information

**Not applicable — a deliberate and citable negative.**

- **Environmental factors:** none. No CTD/TOXNET chemical–disease association for MIC-CAP. No radiation, pollution, or occupational exposure implicated.
- **Lifestyle factors:** none. No maternal smoking, alcohol, nutrition, or exercise association.
- **Infectious agents:** none causal. Infection matters only as (a) the principal **differential diagnosis** for congenital microcephaly with a cutaneous sign — congenital Zika (dermatologic findings absent, but microcephaly + simplified gyri + calcifications overlap), congenital CMV (blueberry-muffin rash mimics capillary malformations in the newborn), congenital toxoplasmosis, congenital rubella; and (b) a leading **complication** — recurrent aspiration pneumonia [CACHE-VERIFIED, PMID:31638258]: *"received immunoglobulin intravenously as a result of recurrent pneumonia."*

The distinction matters clinically: in a newborn with microcephaly and scattered red macules, the TORCH/Zika workup is mandatory before attributing findings to MIC-CAP.

---

## 6. Mechanism / Pathophysiology

### The causal chain, upstream → downstream

```
[MOLECULAR — trigger]
Biallelic STAMBP LOF variants
  → reduced or absent AMSH protein (destabilization via SBM/MIT disruption, NMD of truncating alleles,
    or catalytic/substrate-binding failure via T313I)
  → loss of Zn²⁺-dependent K63-linkage-specific deubiquitinase activity at the endosome
        │
[CELLULAR — proximal convergence node]
  → failure of ESCRT-associated deubiquitination of K63-Ub cargo during MVB sorting
        │
        ├────────────────────────────┬──────────────────────────────┬───────────────────────┐
[ARM A: proteostasis]        [ARM B: signaling]            [ARM C: progenitor]      [ARM D: inflammation]
K63-Ub conjugate             failure of receptor            impaired NSC/NPC         NLRP3 K63-Ub
aggregation (+p62,           downregulation → cargo         proliferation;           accumulation →
TDP-43, glutamate            recycling instead of           CFLAR (c-FLIP)           inflammasome
receptors)                   lysosomal degradation          downregulation           activation
   ↓                              ↓                              ↓                        ↓
↑ autophagosomes            constitutive, serum-           death-receptor          ↑ IL-1β
(LC3-II)                    INSENSITIVE RAS-MAPK           apoptosis in NPCs        (in vitro only)
   ↓                        and PI3K-AKT-mTOR                   ↓                        ↓
caspase-3 activation        activation                     reduced cortical         neuroinflammation
↑ apoptosis                      ↓                         progenitor pool          (mouse brain)
   ↓                        dysregulated capillary              ↓                        ↓
[TISSUE]                    endothelial patterning         smaller cortex           microglial activation
progressive neuronal loss        ↓
(CA1 hippocampus, cortex)   CUTANEOUS CAPILLARY
   ↓                        MALFORMATIONS
[ORGANISM]
progressive microcephaly · cortical atrophy · simplified gyri · intractable epilepsy ·
spastic quadriparesis · optic atrophy · profound DD · early death
```

### Normal AMSH function (the baseline the disease departs from)

AMSH is the endosomal "editor" of the ubiquitin signal that consigns internalized receptors to lysosomal destruction. Activated cell-surface receptors are tagged with K63-linked polyubiquitin, recognized by ESCRT-0 (STAM/HRS), and handed down the ESCRT-I/II/III chain into intraluminal vesicles of the multivesicular body. AMSH, recruited via its SBM to the STAM SH3 domain and via its MIT domain to ESCRT-III CHMP3, removes those K63 chains — thereby rescuing cargo from degradation and recycling ubiquitin. Its linkage specificity is structurally hard-wired [TRANSCRIBED, PMID:18758443]:

> "The Zn(2+)-dependent DUBs AMSH and AMSH-LP regulate receptor trafficking by specifically cleaving Lys 63-linked polyubiquitin chains from internalized receptors."
> "The core and Ins-1 form a catalytic groove that accommodates the Lys 63 side chain of the proximal ubiquitin and the isopeptide-linked carboxy-terminal tail of the distal ubiquitin."

**GO terms for normal function:** `GO:0061578` K63-linked deubiquitinase activity (OLS-verified) · `GO:0070536` protein K63-linked deubiquitination (OLS-verified) · `GO:0016579` protein deubiquitination · `GO:0071985` multivesicular body sorting pathway (OLS-verified) · `GO:0032509` endosome transport via multivesicular body sorting pathway (OLS-verified) · `GO:0043162` ubiquitin-dependent protein catabolic process via the multivesicular body sorting pathway (OLS-verified) · `GO:0031623` receptor internalization **[VERIFY]** · `GO:0008270` zinc ion binding **[VERIFY]** · `GO:0008237` metallopeptidase activity **[VERIFY]**.

**GO cellular components:** `GO:0005769` early endosome **[VERIFY]** · `GO:0005771` multivesicular body **[VERIFY]** · `GO:0000813` ESCRT I complex / `GO:0036452` ESCRT complex **[VERIFY]** · `GO:0005634` nucleus · `GO:0005829` cytosol. UniProt localizes AMSH to nucleus, cytoplasm, early endosomes, and peripheral membrane.

### Arm A — Ubiquitin-conjugate aggregation, autophagy, and apoptosis

The originally proposed and best-replicated mechanism. Patient-derived LCL findings [CACHE-VERIFIED, PMID:23542699]:

> "Patient cell lines showed reduced STAMBP expression associated with accumulation of ubiquitin-conjugated protein aggregates, elevated apoptosis and insensitive activation of the RAS-MAPK and PI3K-AKT-mTOR pathways."

and the authors' own causal interpretation:

> "our findings of a congenital human disorder caused by a defective DUB protein that functions in endocytosis implicates ubiquitin-conjugate aggregation and elevated apoptosis as factors potentially influencing the progressive neuronal loss underlying MIC-CAP syndrome."

Supporting experimental detail [SOURCE-PARAPHRASE, PMC4000253]: *STAMBP* siRNA knockdown in T98G cells produced elevated conjugated-ubiquitin aggregates (anti-FK2 IF); patient LCLs (P1.1, P3.1, P7.1) showed the same after 24 h serum starvation; **lentiviral STAMBP transduction reversed the phenotype** (a genuine rescue, strengthening causal attribution). Apoptosis was read out by **cleaved caspase-3** and **Annexin V** in P1.2, P3.1, P7.1. Autophagic flux was elevated (**LC3-II** ↑ after bafilomycin A1), consistent with increased autophagosome content.

The mouse work independently establishes the same chain in vivo, and identifies the substrates [TRANSCRIBED, PMID:21531206]:

> "Here, we demonstrate that AMSH(-/-) mice developed ubiquitinated protein accumulations as early as embryonic day 10 (E10), and that severe deposits were present in the brain at postnatal day 8 (P8) and P18."
> "Interestingly, TDP-43 was found to accumulate and colocalize with glial marker-positive cells in the brain."
> "Glutamate receptor and p62 accumulations were also found; these molecules colocalized with ubiquitinated aggregates in the brain."
> "These data suggest that AMSH plays an important role in degrading ubiquitinated proteins and glutamate receptors in vivo."

Two mechanistically loaded observations here deserve KB capture. **TDP-43 accumulation** places MIC-CAP in unexpected proximity to the ALS/FTD proteinopathies (the authors state *"AMSH(-/-) mice provide an animal model for neurodegenerative diseases, which are commonly characterized by the generation of proteinaceous aggregates"*). **Glutamate receptor accumulation** offers a direct, and largely untested, explanation for the epilepsy: failure to downregulate ionotropic glutamate receptors would produce a cell-autonomous excitation/inhibition imbalance — a natural link to the `epilepsy_excitation_inhibition_imbalance` module.

**GO terms:** `GO:0006914` autophagy **[VERIFY]** · `GO:0016236` macroautophagy **[VERIFY]** · `GO:0051402` neuron apoptotic process (OLS-verified) · `GO:0097190` apoptotic signaling pathway **[VERIFY]** · `GO:0043524` negative regulation of neuron apoptotic process **[VERIFY]** · `GO:0043161` proteasome-mediated ubiquitin-dependent protein catabolic process **[VERIFY]** · `GO:0016240`/`GO:0034389` protein aggregate/inclusion body assembly **[VERIFY]**.

### Arm B — Constitutive, serum-insensitive RAS-MAPK and PI3K-AKT-mTOR signaling → the capillary malformations

This arm is what explains the *cutaneous* half of the syndrome, and it is the reason MIC-CAP belongs in the RASopathy/PI3K-vascular-anomaly conceptual neighborhood despite its recessive LOF genetics. [CACHE-VERIFIED, PMID:23542699]:

> "The latter cellular phenotype is notable considering the established connection between these pathways and their association with vascular and capillary malformations."

Experimental detail [SOURCE-PARAPHRASE, PMC4000253]:
- **RAS-MAPK:** elevated RAS-GTP pulled down from patient LCLs; pS338-C-RAF maintained in the *absence* of serum (i.e., pathway is on when it should be off); pERK1/2 elevated **even after MEK1/2 inhibition** — "insensitive" rather than merely "elevated."
- **PI3K-AKT-mTOR:** elevated phospho-PI3K; pAKT-T308, pTSC2-T1462 and pS6-S240/244 all maintained under serum starvation.
- **Rescue:** lentiviral STAMBP restored *"a normal signaling response to serum starvation."*

The logic is coherent: if K63-Ub cargo cannot be deubiquitinated and committed to the MVB, activated RTKs persist in the endosomal compartment and continue to signal. **Signaling from the endosome, not just the plasma membrane, is the mechanistic crux.**

**Important dissenting datum — do not curate this arm as settled.** [CACHE-VERIFIED, PMID:29907875]:

> "Contrary to previously reported STAMBP mutations, the Ser236Phe mutation did not lead to constitutive activation of the PI3K-AKT-mTOR pathway in patient-derived LCLs, as indicated by the expression of phosphorylated S6 ribosomal protein, suggesting that it is not the major pathomechanism underlying the disorder in this patient."

This is a genuine, allele-specific contradiction and an ideal `mechanistic_hypotheses` entry with `status: EMERGING` plus a `discussions` block of `kind: KNOWLEDGE_GAP`. Note that this patient nonetheless had **multiple capillary malformations** — so if mTOR activation were the necessary cause of the CMs, S236F should not have produced them. Either the CM mechanism is mTOR-independent, or the LCL readout does not reflect endothelial biology.

**GO terms:** `GO:0000165` MAPK cascade **[VERIFY]** · `GO:0007265` Ras protein signal transduction **[VERIFY]** · `GO:0014065` phosphatidylinositol 3-kinase signaling **[VERIFY]** · `GO:0031929` TOR signaling **[VERIFY]** · `GO:0038095`/`GO:0007169` transmembrane receptor protein tyrosine kinase signaling pathway **[VERIFY]** · `GO:0001525` angiogenesis **[VERIFY]** · `GO:0001569` branching involved in blood vessel morphogenesis **[VERIFY]**.

**Module conformance opportunity:** this arm maps onto `rtk_grb2_signaling_adaptation` (RTK phosphotyrosine docking → proliferation output) and, in the negative direction, is the loss-of-downregulation mirror of `sustaining_proliferative_signaling`.

### Arm C — Neural progenitor proliferation failure (the competing microcephaly mechanism)

The apoptosis model does not fully explain a brain that is **already small at birth** (OFC −1.8 to −8 SD). Human cortical organoid work supplies the missing developmental arm [CACHE-VERIFIED, PMID:36033615]:

> "Cortical organoids with STAMBP knockout (KO) showed significantly lower proliferation of neural stem cells (NSCs), leading to smaller organoids that are characteristic of microcephaly. Furthermore, STAMBP disruption did not affect apoptosis in early cortical organoids."

and, establishing variant-specific causality:

> "After re-expressing wild-type STAMBP, STAMBP G307E , and STAMBP T313I (a known pathogenic mutation) within STAMBP KO organoids, only STAMBP WT rescued the impaired proliferation of STAMBP deficient organoids, but not STAMBP G307E and STAMBP T313I ."

The hESC-derived NPC work identifies a molecular effector and, notably, restores a death pathway — but a *different* one [TRANSCRIBED, PMID:38951308]:

> "We found that STAMBP is dispensable for the pluripotency maintenance or neural differentiation of hESCs. However, neural progenitor cells (NPCs) derived from STAMBP-deficient hESCs fail to be long-term maintained/expanded in vitro. We identified the anti-apoptotic protein CFLAR is down-regulated in those affected NPCs and ectopic expression of CFLAR rescues NPC defects induced by STAMBP-deficiency."

**Synthesis for the KB.** Two-phase model, best curated as two nodes rather than one:
- **Prenatal phase (developmental):** reduced NSC/NPC proliferation and CFLAR-dependent death-receptor apoptosis in the progenitor pool → small brain **at birth**.
- **Postnatal phase (degenerative):** ubiquitin-aggregate-driven, caspase-3-mediated apoptosis of post-mitotic neurons, plus neuroinflammation → **progressive** atrophy, epilepsy, and regression.

This resolves the "congenital *and* progressive" microcephaly that a single mechanism cannot account for, and it makes the `HUMAN_MODEL_MISMATCH` designation appropriate for the apoptosis-vs-proliferation discrepancy between mouse (apoptosis-dominant) and human organoid (proliferation-dominant, apoptosis-negative) systems.

**GO terms:** `GO:0021987` cerebral cortex development **[VERIFY]** · `GO:0061351` neural precursor cell proliferation **[VERIFY]** · `GO:0050767` regulation of neurogenesis **[VERIFY]** · `GO:0008283` cell population proliferation **[VERIFY]** · `GO:0097191` extrinsic apoptotic signaling pathway **[VERIFY]** (CFLAR/death-receptor arm).

### Arm D — Neuroinflammation and the NLRP3 inflammasome

The CNS-conditional mouse adds an inflammatory component absent from the original model [CACHE-VERIFIED, PMID:39169623]:

> "In this MIC-CAP syndrome mouse model, early-onset neuronal death occurs specifically in the hippocampus and cortex, accompanied by aggregation of ubiquitinated proteins, and massive neuroinflammation."

Mechanistically plausible, because AMSH restrains NLRP3 via exactly the K63 chemistry it is specialized for [TRANSCRIBED, PMID:33253913]:

> "Here we identify the deubiquitinase STAM-binding protein (STAMBP) as a negative regulator of the NLRP3 inflammasome."
> "While STAMBP does not modulate NLRP3 protein abundance, cellular depletion of the deubiquitinase increased NLRP3 K63 chain polyubiquitination resulting in increased NLRP3 inflammasome activation."
> "These findings describe a unique mechanism of non-degradative ubiquitination of NLRP3 by STAMBP to limit excessive inflammasome activation and to reduce injurious IL-1β signaling."

**Curation caution:** PMID:33253913 is a monocyte/CRISPR study with no MIC-CAP patient data. Curate as `evidence_source: IN_VITRO` supporting a *hypothesized* IL-1β arm; do not assert clinical inflammasome-driven disease. It is, however, the most tractable **repurposing hypothesis** in the whole disease (IL-1 blockade, e.g. anakinra) and belongs in a `discussions` / `proposed_experiments` block.

**GO terms:** `GO:0002376` immune system process · `GO:0072559` NLRP3 inflammasome complex **[VERIFY]** · `GO:0050702` interleukin-1 beta secretion **[VERIFY]** · `GO:0006954` inflammatory response **[VERIFY]** · `GO:0001774` microglial cell activation **[VERIFY]**.

### Protein dysfunction, metabolic, and biochemical layers

- **Protein dysfunction:** loss of function by destabilization (dominant route) or substrate-binding failure. Notably, this is a disorder of **failed protein clearance**, so the pathologic species is not the mutant protein itself but the **accumulated K63-ubiquitinated substrate pool** (p62/SQSTM1, TDP-43, glutamate receptors). Conceptually adjacent to `amyloidogenesis` and `lysosomal_substrate_accumulation` in the dismech module set — the shared logic is "an enzyme that clears something is missing, so the something accumulates and is cytotoxic" — though the substrate is a ubiquitin-conjugate pool rather than a lipid or a fibril.
- **Metabolic changes:** none identified. Blood and urine metabolic screening is **normal** [CACHE-VERIFIED, PMID:31638258]: *"Blood and urinary metabolic screening indicated normal results."* This is diagnostically useful (excludes inborn errors) and means MIC-CAP does **not** conform to `metabolic_intoxication_decompensation`.
- **Biochemical abnormalities:** no enzyme assay, biomarker, or metabolite is abnormal in a clinically measurable way. The only "biochemical" readouts are research-grade immunoblots (STAMBP level, pS6, cleaved caspase-3, LC3-II, FK2 ubiquitin-conjugate IF).
- **Immune involvement:** no immunodeficiency or autoimmunity. Alopecia areata in one family (PMID:25692795) is the sole autoimmune-adjacent report and is probably coincidental at n=1. Recurrent pneumonia is aspiration-related, not immunologic.
- **Tissue damage mechanism:** apoptotic neuronal death (not necrosis, not ischemia, not fibrosis), regionally selective for hippocampal CA1 and cerebral cortex, with secondary neuroinflammation.

### Molecular profiling

**Transcriptomics / proteomics / metabolomics / lipidomics / single-cell / spatial:** **no MIC-CAP-specific dataset exists.** No GEO/ArrayExpress series, no PRIDE submission, no MetaboLights study, no single-cell atlas of patient or model tissue. The closest available resources are the *Stambp^Sox1-cKO* mouse brain and the *STAMBP*-KO cortical organoid system, either of which would be an obvious substrate for such profiling. **This is one of the clearest, most actionable gaps in the disease.**

**Functional genomics screens:** *STAMBP* appears in DepMap and in a high-throughput DUB-autophagy screen (PMID:32453962), but no MIC-CAP-directed CRISPR screen has been published.

---

## 7. Anatomical Structures Affected

### Organ level

**Primary:**
- **Brain** (`UBERON:0000955`) — the dominant target organ and, per the mouse gene-therapy work, the *sufficient* one: [CACHE-VERIFIED, PMID:39169623] *"our findings reveal a central role of brain defects in the pathogenesis of STAMBP deficiency."*
- **Skin** (`UBERON:0002097` skin of body) — capillary malformations, generalized distribution.

**Secondary / systemic:**
- **Eye and optic pathway** (`UBERON:0000970` eye; `UBERON:0000941` optic nerve **[VERIFY]**; `UBERON:0000959` optic chiasma **[VERIFY]**) — optic atrophy, optic nerve/chiasm hypoplasia, cortical visual impairment, congenital blindness.
- **Musculoskeletal** — distal phalanges (`UBERON:0004300` distal phalanx **[VERIFY]**), nails (`UBERON:0001705` nail **[VERIFY]**); secondary contractures/scoliosis from spasticity.
- **Gastrointestinal** — oropharyngeal dysphagia, aspiration; gastrostomy dependence.
- **Respiratory** (`UBERON:0002048` lung) — recurrent aspiration pneumonia (secondary).
- **Endocrine** — thyroid (`UBERON:0002046` **[VERIFY]**) in congenital hypothyroidism (2 families); adrenal gland (`UBERON:0002369` **[VERIFY]**) in 1 case.
- **Cardiovascular** — septal defects, PFO (occasional).
- **Genitourinary** — vesicoureteral reflux (occasional).

**Body systems:** nervous (primary), integumentary (primary), visual, musculoskeletal, digestive, respiratory, endocrine, cardiovascular.

### Regional CNS specificity — a strikingly selective vulnerability

The regional selectivity is one of the most mechanistically interesting features of the disease and is consistent across human imaging, human neuropathology, and mouse.

- **Hippocampus** (`UBERON:0002421` hippocampal formation **[VERIFY]**), specifically the **CA1 field** (`UBERON:0003881` CA1 field of hippocampus — OLS-verified). [TRANSCRIBED, PMID:11713295]: *"Examination of brain sections at P6 demonstrated significant loss of neurons and apoptotic cells in the CA1 subfield of the hippocampus."* Human correlate: hypoplastic hippocampus in 6/7.
- **Cerebral cortex** (`UBERON:0000956`). [TRANSCRIBED, PMID:11713295]: *"Brain atrophy developed by P16 and was accompanied by complete loss of the CA1 neurons in the hippocampus and marked atrophy of the cerebral cortex."* [CACHE-VERIFIED, PMID:39169623]: *"early-onset neuronal death occurs specifically in the hippocampus and cortex."*
- **Cerebellum is relatively spared** — a genuine dissociation. [TRANSCRIBED, PMID:11713295]: *"AMSH-deficient hippocampal neuronal cells were unable to survive in vitro, even in the presence of several stimulatory cytokines, while AMSH-deficient cerebellar neurons, thymocytes, and embryonic fibroblasts survived normally."* The human neuropathology matches [SOURCE-PARAPHRASE, GeneReviews]: *"disproportionately small cerebral hemispheres compared to the cerebellum."* **This cell-autonomous, region-restricted survival requirement is the single most distinctive cellular phenotype in MIC-CAP and deserves its own pathophysiology node.**
- **Corpus callosum** (`UBERON:0002336` **[VERIFY]**) — thinning/hypoplasia.
- **White matter** (`UBERON:0002316` white matter **[VERIFY]**) — hypomyelination, delayed myelination, white-matter loss.
- **Extra-axial CSF space** (`UBERON:0006330`? **[VERIFY]**) — increased extra-axial space in 9/9.

**Lateralization:** bilateral and symmetric throughout (brain atrophy, optic atrophy, digital hypoplasia). Capillary malformations are **generalized and randomly distributed**, explicitly *not* dermatomal/segmental — a useful discriminator from Sturge-Weber (V1 trigeminal distribution) and from mosaic segmental vascular anomalies. The one asymmetric report is unilateral epistaxis in the dual-diagnosis case (PMID:38058451).

### Tissue and cell level

| Cell type | CL term | Role |
|---|---|---|
| Neuron | `CL:0000540` **[VERIFY]** | primary target of apoptotic loss |
| Hippocampal neuron | **`CL:0002608`** (OLS-verified) | CA1 pyramidal neurons — most vulnerable population |
| Neural progenitor cell | **`CL:0011020`** (OLS-verified) | reduced proliferation (organoid/hESC arm) |
| Neural stem cell | `CL:0000047` **[VERIFY]** | "NSC" in PMID:36033615 |
| Radial glial cell | `CL:0000681` **[VERIFY]** | cortical progenitor; inferred, not directly assayed |
| Capillary endothelial cell | **`CL:0002144`** (OLS-verified) | substrate of the capillary malformations |
| Microglial cell | `CL:0000129` **[VERIFY]** | neuroinflammation (mouse) |
| Astrocyte | `CL:0000127` **[VERIFY]** | glial marker-positive TDP-43 accumulation (PMID:21531206) |
| Cerebellar neuron | `CL:0000121` Purkinje cell **[VERIFY]** | **spared** — curate as an explicit negative |
| Lymphoblast / EBV-LCL | `CL:0000542` lymphocyte **[VERIFY]** | the workhorse patient-cell model, not a disease site |
| Fibroblast | `CL:0000057` **[VERIFY]** | **spared** in mouse |
| Thymocyte | `CL:0000893` **[VERIFY]** | **spared** in mouse |

**Tissue types:** nervous tissue (primary), vascular endothelium/connective tissue of dermis, skeletal (terminal phalangeal ossification), ectodermal appendages (nail).

### Subcellular level

| Compartment | GO CC term | Relevance |
|---|---|---|
| Early endosome | `GO:0005769` **[VERIFY]** | AMSH's principal site of action |
| Multivesicular body / late endosome | `GO:0005771`, `GO:0005770` **[VERIFY]** | cargo sorting failure |
| ESCRT complexes | `GO:0036452` **[VERIFY]** | ESCRT-0 (STAM) and ESCRT-III (CHMP3) partners |
| Lysosome | `GO:0005764` **[VERIFY]** | failed terminal degradation |
| Autophagosome | `GO:0005776` **[VERIFY]** | elevated LC3-II |
| Cytoplasmic ubiquitin-conjugate aggregates / inclusion body | `GO:0016234` inclusion body **[VERIFY]** | the pathologic accumulation |
| Plasma membrane | `GO:0005886` | receptor internalization origin |
| Nucleus, cytosol | `GO:0005634`, `GO:0005829` | secondary AMSH pools (UniProt) |

**Xogenesis note:** MIC-CAP forms two candidate pathological structures — (1) intracellular **ubiquitin-conjugate/p62/TDP-43 aggregates**, and (2) the cutaneous **capillary malformation** itself. Neither has an established MPATH continuant analogous to `granuloma` or `thrombus`; a curator considering the Xogenesis anchor convention should treat both as **OBO gaps** and anchor with `OGMS:0000078`/`OGMS:0000081` plus UBERON site only.

---

## 8. Temporal Development

### Onset

- **Onset category: CONGENITAL** — HPO annotates `HP:0003577` (Congenital onset) at **10/10**. [CACHE-VERIFIED, PMID:24354023]: *"The defining clinical characteristics ... are typically present at birth."*
- **Prenatal onset** is inferable from birth OFC of −1.8 to −8 SD and SGA in 7/10, and is directly supported in the mouse, where ubiquitinated protein accumulation begins at **E10** [TRANSCRIBED, PMID:21531206].
- **Onset pattern: insidious/chronic with a subacute epileptic inflection.** Microcephaly and CMs are present at birth; seizures declare themselves in the neonatal period to the first months. In the Chinese case, seizure onset was at **3 months** with escalation to infantile spasms at **4 months** [CACHE-VERIFIED, PMID:31638258]. GeneReviews describes *"neonatal-onset intractable epilepsy"*.

### Progression

**Stages (proposed for `progression:` curation):**

| Stage | Timing | Features |
|---|---|---|
| **Prenatal** | conception → birth | Reduced NSC proliferation; small brain and SGA at birth; CMs and digital hypoplasia already formed |
| **Early infantile (declaration)** | birth → ~6 mo | Seizure onset, often escalating to infantile spasms/hypsarrhythmia; hypotonia; feeding difficulty |
| **Late infantile / toddler (peak severity)** | ~6 mo → 2 y | Maximal seizure burden and refractoriness; head circumference falls further; emergence of spastic quadriparesis and myoclonus; optic atrophy; failure to thrive; gastrostomy |
| **Childhood (plateau)** | > 2 y | Seizures *"appear to stabilize after age two years"* [CACHE-VERIFIED, PMID:24354023]; developmental trajectory flat; contractures; recurrent aspiration |
| **Terminal** | variable, infancy → adolescence | Death from aspiration pneumonia, status epilepticus, sepsis, or unexplained sudden death |

**Progression rate:** the microcephaly is genuinely and relentlessly **progressive** (`clinical_course: PROGRESSIVE`) — OFC falling from −1.8/−8 SD at birth to −2.5/−8 SD later, with radiographically progressive cerebral atrophy. Development is essentially **static at a profoundly low ceiling** rather than frankly regressive in most patients. The two axes should be curated separately.

**Course pattern:** chronic-progressive with superimposed episodic seizure exacerbations. Not relapsing-remitting.

**Duration:** lifelong, with markedly shortened lifespan.

### Patterns

- **Remission:** none spontaneous. The one meaningful partial remission is pharmacological and specific: **vigabatrin** produced an 80% seizure reduction within a week where four other agents and a ketogenic diet had failed [CACHE-VERIFIED, PMID:31638258]: *"the patient received vigabatrin (60 mg/kg/day) and the seizures reduced by 80% a week later."* Confounded by the patient's death three weeks later, so long-term efficacy is unknown — the authors say so explicitly.
- **Critical periods:**
  - **Prenatal neurogenesis (roughly GW 8–20)** — the window in which the proliferation defect fixes brain size. Almost certainly **not** rescuable postnatally.
  - **Neonatal/early-infantile period** — the therapeutic window demonstrated in mouse. [CACHE-VERIFIED, PMID:39169623]: *"neonatal AAV9-mediated gene supplementation of Stambp in the brain could significantly improve neurological defects, sustain growth, and prolong the lifespan"*, supporting the claim that *"postnatal gene replacement is an effective approach to cure the disease."* This is the central translational finding for MIC-CAP and defines the intervention window that any future human trial would target.
  - **First 2 years** — maximal seizure burden; the period where aggressive AED optimization has the most to gain.

---

## 9. Inheritance and Population

### Epidemiology

- **Prevalence: unknown; ultra-rare.** GeneReviews states plainly [SOURCE-PARAPHRASE, NBK174452]: *"Prevalence is unknown. To date 18 affected individuals (including 3 sets of sibs) from 15 families worldwide have molecularly confirmed MIC-CAP syndrome"* (as of the 2021-03-18 update).
- Orphanet: *"no prevalence information available ... Not enough data available about incidence and published cases."*
- **Current cumulative literature count (this report's tally):** the 18 in GeneReviews, plus 4 new patients in PMID:35962715 (2022), plus the *STAMBP*-NDD patient without CMs (PMID:36033615), the dual-diagnosis patient (PMID:38058451), the 2026 Indian patient (PMID:41603106), and the Russian case (PMID:32929933) — with some overlap. A defensible statement is **"approximately 25–30 molecularly confirmed individuals reported worldwide as of mid-2026."** Note that PMID:31638258 (2019) independently counted *"18 pathogenic mutations ... reported in 16 patients from 8 ethnic groups."*
- **Incidence:** not estimable.

**Dismech `Prevalence` block recommendation:**
```yaml
prevalence:
- population: Worldwide
  measure_type: CASES_IN_LITERATURE
  prevalence_class: ULTRA_RARE
  notes: >-
    Prevalence unknown. GeneReviews (2021 update) reported 18 molecularly confirmed
    individuals from 15 families; subsequent case reports bring the cumulative
    published total to roughly 25-30 individuals as of mid-2026.
  evidence:
  - reference: PMID:24354023
    supports: SUPPORT
    evidence_source: HUMAN_CLINICAL
    snippet: "To date, the diagnosis has been confirmed in 18 individuals from 15 families."
    explanation: GeneReviews cumulative count of molecularly confirmed cases.
```
*(The snippet above is cache-verified against `references_cache/PMID_24354023.md`.)*

### Genetic transmission

- **Inheritance pattern: AUTOSOMAL RECESSIVE.** HPO: `HP:0000007`. [CACHE-VERIFIED, PMID:24354023]: *"MIC-CAP syndrome is an autosomal recessive disorder caused by biallelic STAMBP pathogenic variants."* Note that the MedlinePlus-derived summary retrieved during this research incorrectly stated autosomal dominant inheritance — that was a retrieval artifact, not the source's content; **AR is unambiguous** across OMIM, Orphanet, GeneReviews, and every primary report.
- **Penetrance:** appears **complete** in biallelic individuals — no unaffected homozygote has been reported. Heterozygous carriers (including all obligate-carrier parents) are entirely asymptomatic.
- **Expressivity: variable**, and increasingly recognized as such. The range runs from death in infancy to a child who *"achieved independent walking and short-phrase speech at age five"* (the leaky c.1005+358A>G homozygote), and now includes a patient without the eponymous capillary malformations (PMID:36033615). The best-supported determinant is **residual protein level** [SOURCE-PARAPHRASE, GeneReviews]: *"complete absence of protein production leading to the most severe phenotypes"*, with *"The effect of pathogenic variant(s) on the protein STAMBP likely influences the severity."*
- **Genetic anticipation:** not applicable (no repeat expansion).
- **Germline mosaicism:** not reported.
- **Uniparental isodisomy:** documented in **1/15 families** and carries a materially different recurrence risk — see the counseling block below.
- **Founder effects:** none identified. Reported alleles are private or recurrent-by-chance (p.Arg38Cys in 3 European families is more plausibly a mutational hotspot at a CpG dinucleotide than a founder haplotype, though no haplotype analysis has been done — a real gap).
- **Consanguinity:** a major contributor to homozygous cases, documented in Egyptian, Saudi, and Arab families (PMIDs 27531570, 25266620, 25692795).
- **Carrier frequency:** not established. Given ~25–30 cases worldwide, carrier frequency is presumably far below 1/1000 in outbred populations. **No newborn or carrier screening panel includes *STAMBP*.**

### Recurrence risk (essential for the `prevention`/`counseling` sections)

Two distinct scenarios, both from [CACHE-VERIFIED, PMID:24354023]:

**Standard biparental inheritance** — *"If both parents are known to be heterozygous for a STAMBP pathogenic variant, each sib of an affected individual has at conception a 25% chance of being affected, a 50% chance of being an asymptomatic carrier, and a 25% chance of being unaffected and not a carrier."*

**Uniparental isodisomy** — *"If the proband has MIC-CAP syndrome as the result of uniparental isodisomy, only one parent is heterozygous for a STAMBP pathogenic variant, and if neither parent has a chromosome rearrangement, each sib of an affected individual has at conception a 50% chance of being an asymptomatic carrier and an approximately 50% chance of being unaffected and not a carrier. The risk to sibs of a proband of being affected is unknown but is presumed to be less than 1%."*

This UPD distinction changes counseling from 25% to <1% and is therefore one of the highest-value facts in the entire entry.

### Population demographics

- **Affected populations:** *"Most reported individuals are of European descent; individuals from other ethnic backgrounds (African, Arab, Asian, and Polynesian) have also been reported"* [SOURCE-PARAPHRASE, GeneReviews]. Documented ancestries across the literature: European, African-American, Polynesian, Egyptian, Saudi/Arab, Kuwaiti, Japanese, Chinese, Indian, Russian. PMID:31638258 counted *"8 ethnic groups."* The European predominance almost certainly reflects **ascertainment through exome-sequencing-rich health systems**, not true biology.
- **Geographic distribution:** worldwide; no endemic focus. Elevated case density is expected in high-consanguinity regions (Middle East, North Africa, South Asia).
- **Variant geography:** p.Arg38Cys and p.Arg424* in European families; p.Lys303Arg in an Egyptian family; p.Ser236Phe in a Japanese family; p.Gly307Glu/p.Cys282Trpfs*11 in a Chinese family; c.376-1G>A in an Indian family. Too few families for meaningful population-genetic inference.
- **Sex ratio:** ~1:1 expected; both sexes reported. No sex effect on severity has been described.
- **Age distribution of living affected individuals:** heavily skewed to infancy and early childhood by early mortality. *"The oldest living individual known was 12 years old at last assessment"* [SOURCE-PARAPHRASE, GeneReviews]; PMID:25266620 reports the longest follow-up, two brothers aged 7 and 12.

---

## 10. Diagnostics

### Diagnostic approach

Diagnosis is **clinical recognition confirmed by molecular testing**; there is no biochemical or functional confirmatory assay. [CACHE-VERIFIED, PMID:24354023]:

> "The diagnosis of MIC-CAP syndrome is established in a proband with suggestive findings and biallelic pathogenic variants in STAMBP identified by molecular genetic testing."

### Suggestive clinical findings (GeneReviews) [SOURCE-PARAPHRASE]

1. Head circumference *"more than two standard deviations (SD) below the mean"*
2. *"Pink or red, blanchable, roughly oval or circular macules or patches"* widely distributed
3. *"Neonatal-onset intractable epilepsy"*
4. Hypoplastic distal phalanges with abnormal nails
5. Characteristic facial dysmorphism and neuroimaging abnormalities

The combination of **microcephaly + generalized blanchable capillary macules + hypoplastic distal phalanges** is essentially pathognomonic and should trigger *STAMBP* testing directly.

### Genetic testing

| Modality | Utility in MIC-CAP | Notes |
|---|---|---|
| **Single-gene *STAMBP* sequencing** | **High** — 15/15 families detected by sequence analysis (GeneReviews Table 1) | Reasonable first-line when the clinical gestalt is classic |
| **Multigene panel** (microcephaly / DEE / vascular anomaly panels) | High | *STAMBP* is included on most epileptic-encephalopathy and primary-microcephaly panels |
| **WES** | **High — the historical discovery modality.** Every major MIC-CAP report used WES: PMID:23542699 (5 patients), PMID:27531570 (*"uncovered by exome sequencing"*), PMID:29907875 (*"through whole-exome sequencing"*), PMID:36033615 (*"Whole exome sequencing was performed on a patient presenting with a neurodevelopmental disorder"*) | Best choice for an atypical or CM-negative presentation |
| **WGS** | Superior for one specific reason: the **deep-intronic c.1005+358A>G** allele is invisible to WES | Consider WGS (± RNA-seq) when WES finds a single heterozygous *STAMBP* variant |
| **CMA** | **Very low yield** — 0/15 families had a detectable del/dup | Still appropriate as a general microcephaly workup step |
| **Karyotype / FISH** | Not indicated | |
| **mtDNA testing** | Not indicated | |
| **Repeat-expansion testing** | Not indicated | |
| **SNP array / UPD testing** | **Specifically indicated** when a proband is homozygous for a variant carried by only one parent — identifies uniparental isodisomy (1/15 families) and changes recurrence risk from 25% to <1% | High counseling value |
| **RNA sequencing** | Emerging adjunct — would resolve leaky/deep-intronic splice alleles by quantifying transcript reduction | Not yet standard |

### Laboratory tests and biomarkers

- **No diagnostic biomarker exists.** No blood, urine, or CSF analyte is specific to MIC-CAP.
- **Metabolic screening is normal and should be sent to exclude alternatives** [CACHE-VERIFIED, PMID:31638258]: *"Blood and urinary metabolic screening indicated normal results."*
- **TORCH/Zika serology and PCR** — mandatory in a newborn with microcephaly.
- **Thyroid function (TSH, free T4)** — congenital hypothyroidism reported in 2 independent families; newborn screening will usually catch it, but explicit testing is warranted. LOINC: `3016-3` (TSH) **[VERIFY]**, `3024-7` (free T4) **[VERIFY]**.
- **Research-only assays** (not clinically available): STAMBP immunoblot on patient LCLs (PMIDs 23542699, 29907875); anti-FK2 ubiquitin-conjugate immunofluorescence; phospho-S6/pERK/pAKT immunoblot; cleaved caspase-3 / Annexin V.

### Imaging

**Brain MRI** is the key imaging study, and the findings are consistent enough to be diagnostically supportive [SOURCE-PARAPHRASE, GeneReviews]:

> "Simplified gyral pattern (reduced number of gyri and shallow sulci) with increased extra-axial space and progressive cerebral atrophy"
> "Cortical myelination may be reduced or abnormal"
> "Hippocampal hypoplasia, thinning of the corpus callosum, hypoplasia of the optic nerves and/or optic chiasm and other malformations of cortical development"

Real-world example [CACHE-VERIFIED, PMID:31638258]: *"The MRI scans showed slightly dilated lateral ventricles and increased extra-axial spaces."*

**Hand/foot radiographs** — confirm distal phalangeal hypoplasia.
**Echocardiogram** — screen for septal defects.
**Renal ultrasound / VCUG** — if vesicoureteral reflux is suspected.

### Electrophysiology

- **EEG** — essential. Hypsarrhythmia with a slow background and multifocal epileptiform discharges [CACHE-VERIFIED, PMID:31638258]: *"Interictal electroencephalography showed hypsarrhythmia and slow wave background with bioccipital spike-slow wave during waking."*
- **VEP / ERG** — assess optic atrophy and cortical visual impairment.
- **BAER** — one case of sensorineural hearing impairment; audiologic screening is reasonable.
- **ECG** — not specifically indicated.

### Biopsy and pathology

- **Skin biopsy** — not required for diagnosis; the CMs are clinically recognizable. No distinctive dermatopathology has been published, which is itself notable (a skin-biopsy study of MIC-CAP CMs, with endothelial pERK/pS6 staining, would be a high-value and easily-obtained experiment).
- **Neuropathology** (autopsy, rare) [SOURCE-PARAPHRASE, GeneReviews]: *"very small brain...with disproportionately small cerebral hemispheres compared to the cerebellum, diffuse cortical atrophy, thin corpus callosum, and white matter loss."* Note that PMID:23542699 includes a neuropathologist (J. Woulfe) among its authors.
- **Ubiquitin/p62/TDP-43 immunohistochemistry** on brain tissue would be the direct human test of the mouse aggregate findings — **to our knowledge this has not been reported in human MIC-CAP brain, and it is arguably the single most important missing human experiment.**

### Clinical criteria and differential diagnosis

There are **no formal consensus diagnostic criteria** (no society guideline, no DSM/ICD operational definition). Diagnosis rests on GeneReviews' suggestive findings plus molecular confirmation.

**Differential diagnosis** (GeneReviews list, with the discriminators):

| Condition | Gene(s) | Inheritance | How it differs from MIC-CAP |
|---|---|---|---|
| **CM-AVM syndrome** | *RASA1*, *EPHB4* | AD | Multiple small CMs are similar, but *"no microcephaly, intractable epilepsy, or neurologic impairment"*; AVM/AVF risk instead |
| **Primary autosomal recessive microcephaly (MCPH)** | *ASPM*, *WDR62*, *MCPH1*, etc. | AR | Congenital microcephaly with simplified gyri, but *"normal facies (except narrow/sloping forehead), mild-to-severe cognitive impairment without major motor delay, normal growth except mild short stature"*; **no CMs, no distal limb anomalies, epilepsy not intractable**. *ASPM* alone *"explains 30%-50% of primary microcephaly depending on geographic origin"* |
| **MCAP / megalencephaly-capillary malformation** | *PIK3CA* (mosaic) | sporadic/mosaic | **Opposite head size (megalencephaly)**, overgrowth, polymicrogyria, somatic mosaicism |
| **Sturge-Weber syndrome** | *GNAQ* (mosaic) | sporadic/mosaic | Segmental facial port-wine stain in V1 distribution, leptomeningeal angiomatosis, glaucoma; not generalized micro-CMs |
| **Congenital infection (Zika, CMV, toxoplasmosis, rubella)** | — | acquired | Positive serology/PCR, intracranial calcifications, chorioretinitis; blueberry-muffin rash can mimic CMs |
| **Diffuse capillary malformation with overgrowth (DCMO)** | *GNA11*/*GNAQ* mosaic | mosaic | Overgrowth rather than microcephaly |

**The discriminating sentence** [SOURCE-PARAPHRASE, GeneReviews]: *"MIC-CAP syndrome is distinguished from primary autosomal recessive microcephaly by the presence of capillary malformations, intractable epilepsy, severe neurologic impairment, and distal limb anomalies."*

### Screening

- **Newborn screening:** *STAMBP* is **not** on any NBS panel and would not meet Wilson-Jungner criteria (no presymptomatic treatment currently exists). Congenital hypothyroidism *is* on standard NBS panels and will incidentally capture that MIC-CAP feature.
- **Carrier screening:** *STAMBP* is not on standard expanded carrier screening panels. Reasonable to include in bespoke panels for high-consanguinity populations.
- **Cascade screening:** offered to at-risk relatives once familial variants are known [CACHE-VERIFIED, PMID:24354023]: *"Once the STAMBP pathogenic variants have been identified in an affected family member ... carrier testing for at-risk family members, prenatal testing for pregnancies at increased risk, and preimplantation genetic testing are possible."*

---

## 11. Outcome / Prognosis

### Survival and mortality

- **Life expectancy: markedly shortened, magnitude unquantified.** GeneReviews [SOURCE-PARAPHRASE]: *"Unknown but shortened because of severe neurologic impairments. The oldest living individual known was 12 years old at last assessment."*
- **No survival curve, 5-year survival figure, or actuarial life table exists.** With ~25–30 total reported patients, none can be computed — this should be stated as an explicit gap rather than estimated.
- **Deaths reported:** *"At least three children have died in infancy"* (GeneReviews). The single well-characterized cause: a male aged 12 months whose *"cause of death...was thought to be septic shock following acute pancreatitis, possibly secondary to valproate therapy."* Additional deaths in the literature include the Chinese boy who *"suddenly succumbed 3 weeks later; no definitive causes were found as no autopsy was performed"* [CACHE-VERIFIED, PMID:31638258] — a presentation compatible with SUDEP.
- **Longest survival:** 12 years (two independent reports: GeneReviews' oldest living individual, and the older of the two brothers in PMID:25266620).
- The mouse model is **uniformly lethal**, which usefully brackets the severity of complete protein loss [CACHE-VERIFIED, PMID:39169623]: *"complete penetrance of preweaning death"*; and [TRANSCRIBED, PMID:11713295]: *"all the AMSH-deficient mice exhibited postnatal growth retardation and died between postnatal day 19 (P19) and P23."*

### Morbidity and function

- **Functional outcome is at the floor of the pediatric disability range.** [SOURCE-PARAPHRASE, GeneReviews]: *"Developmental progress is minimal. Most individuals do not attain head control or independent sitting due to spastic quadriparesis."* No speech, no independent mobility, no self-feeding.
- **The known exception** — the leaky-splice-variant homozygote who walked independently and used short phrases by age 5 — demonstrates that residual protein buys substantial function and is the strongest available proof-of-concept that partial *STAMBP* restoration would be clinically meaningful in humans.
- **Disability classification:** ICF-equivalent profound multiple disability; GMFCS level V; cortical visual impairment; enteral-feeding dependence.
- **Quality-of-life measures: none published.** No EQ-5D, PedsQL, SF-36, PROMIS, CPCHILD, or caregiver-burden instrument has been administered in MIC-CAP. **Explicit gap.**

### Complications

| Complication | Mechanism | Frequency |
|---|---|---|
| Aspiration pneumonia | oropharyngeal dysphagia | Common; drives feeding-tube recommendation and IVIG use in one case |
| Status epilepticus | refractory DEE | Expected; not systematically quantified |
| Failure to thrive / malnutrition | feeding dysfunction + growth failure | Near-universal |
| Contractures, hip subluxation, scoliosis | spastic quadriparesis | Expected; drives the bracing/seating recommendation |
| Cortical visual impairment / blindness | optic atrophy + cortical loss | 6/8–10/18 |
| Sepsis | secondary to pneumonia, pancreatitis | at least 1 fatal |
| **Valproate-associated pancreatitis** | idiosyncratic drug reaction | 1 fatal case; basis for the "agents to avoid" note |
| Sudden unexplained death (possible SUDEP) | refractory epilepsy | ≥1 |

**Recovery potential: none.** MIC-CAP is a static-plus-degenerative encephalopathy with no reversible component. No treatment currently alters the natural history.

### Prognostic factors

1. **Residual STAMBP protein level — the dominant prognostic factor.** Complete absence → most severe phenotype; hypomorphic/leaky alleles → substantially better motor and language outcome. GeneReviews: *"complete absence of protein production leading to the most severe phenotypes."*
2. **Variant class** as a proxy: biallelic truncating/null → severe; ≥1 leaky splice or partially functional missense → attenuated.
3. **Seizure control** — refractoriness in the first two years correlates with the worst trajectory; seizures *"appear to stabilize after age two years,"* so surviving that window is prognostically favorable.
4. **Feeding/respiratory status** — aspiration risk is the main proximate mortality driver, so early gastrostomy is plausibly outcome-modifying (unproven).
5. **Presence/absence of capillary malformations** is *not* prognostic — the CM-negative patient (PMID:36033615) had a comparatively milder neurodevelopmental course, but n=1.

**Prognostic biomarkers:** none validated. STAMBP protein level on immunoblot is the obvious candidate and is currently research-only. Establishing a quantitative STAMBP-level → severity relationship would be a genuinely useful, low-cost study.

---

## 12. Treatment

**No disease-modifying therapy exists for humans. All current management is supportive.** [CACHE-VERIFIED, PMID:24354023]:

> "Treatment of manifestations: Supportive care by multidisciplinary specialists including a medical geneticist, neurologist, developmental pediatrician, and feeding specialist is recommended."

### Current standard of care

| Intervention | Detail | NCIT term | Modality |
|---|---|---|---|
| **Multidisciplinary supportive care** | genetics, neurology, developmental pediatrics, feeding specialist | `NCIT:C15747` Supportive Care | — |
| **Anticonvulsant polytherapy** | *"multiple anticonvulsant medications are frequently required for adequate seizure control"* [CACHE-VERIFIED, PMID:24354023] | `NCIT:C64172` Anticonvulsant Therapy (OLS-verified); agent class `NCIT:C264` Anticonvulsant Agent (OLS-verified); action `NCIT:C15986` Pharmacotherapy | `SMALL_MOLECULE` |
| **Gastrostomy feeding** | *"A feeding tube is essential to optimize nutrition and weight gain while reducing the risk of aspiration"* [CACHE-VERIFIED, PMID:24354023] | `NCIT:C157864` Gastrostomy Tube Procedure or `NCIT:C52006` Gastrostomy (both OLS-verified) | `SURGERY` |
| **Seating, bracing, positioning** | *"Central hypotonia and peripheral hypertonia require attention to proper seating and bracing to maintain posture and prevent contractures"* [CACHE-VERIFIED, PMID:24354023] | `NCIT:C15302` Physical Therapy / `NCIT:C15315` Rehabilitation | `BEHAVIORAL` / `DEVICE` |
| **Genetic counseling** | recurrence risk, carrier testing, prenatal/PGT options | `NCIT:C15240` Genetic Counseling | — |
| **Complex care / palliative care** | *"Regular follow up with a child neurologist for seizure management and a complex care / palliative care team"* [CACHE-VERIFIED, PMID:24354023] | `NCIT:C15747` Supportive Care | — |
| **Levothyroxine** | for the congenital hypothyroidism subset (PMIDs 25692795, 25266620) | `NCIT:C15986` Pharmacotherapy + agent `CHEBI:15062`? **[VERIFY levothyroxine CHEBI]** | `SMALL_MOLECULE` |

### Specific antiseizure medications, with the one real efficacy signal

The best-documented drug sequence in the literature [CACHE-VERIFIED, PMID:31638258]:

> "The patient was treated successively with levetiracetam (40–50 mg/kg/day), topiramate (6–7 mg/kg/day), valproic acid (30 mg/kg/day) and corticosteroids at the outpatient clinic. The spasms decreased and became myoclonic, but the epilepsy remained refractory."

Ketogenic diet then failed:

> "During the follow-up, the seizures were still not well controlled, although the ketogenic diet ratio was modified from 2:1 to 4:1 (4 g fat/l g combined protein, carbohydrate)."

**Vigabatrin then worked, strikingly:**

> "After 1 month, the patient received vigabatrin (60 mg/kg/day) and the seizures reduced by 80% a week later."

With the authors' own honest caveat:

> "Although the patient in the present study responded well to vigabatrin, the long-term efficacy of the drug could not be evaluated due to the early death of the patient."

**Curation guidance:** vigabatrin (`CHEBI:63638`, OLS-verified) is worth curating as a treatment with an explicit `n=1` caveat and `evidence_source: HUMAN_CLINICAL`. It is biologically coherent — vigabatrin is first-line for infantile spasms generally — but this is a single case with three weeks of follow-up. **Do not present it as established MIC-CAP therapy.**

Agents and CHEBI IDs: valproic acid `CHEBI:39867` (OLS-verified), vigabatrin `CHEBI:63638` (OLS-verified), levetiracetam `CHEBI:6437` **[VERIFY]**, topiramate `CHEBI:9625` **[VERIFY]**. Ketogenic diet `NCIT:C173168` (OLS-verified), modality `BEHAVIORAL`.

### Agents to avoid

**Valproic acid** carries a specific, mortality-linked caution [CACHE-VERIFIED, PMID:24354023]: *"Agents/circumstances to avoid: Valproic acid may or may not be associated with adverse effects."* The underlying event was a fatal acute pancreatitis with septic shock at 12 months. The GeneReviews hedging is deliberate — other patients tolerated valproate — so this should be curated as a **caution with heightened pancreatic monitoring**, not an absolute contraindication.

### Pharmacogenomics

No *STAMBP*-specific pharmacogenomic interaction is known. General pediatric-epilepsy PGx applies and should be considered: *HLA-B\*15:02* / *HLA-A\*31:01* for carbamazepine hypersensitivity, *CYP2C9* for phenytoin dosing, *POLG* for valproate hepatotoxicity (relevant given the valproate signal — *POLG* testing before valproate is standard in unexplained DEE and would be prudent here). CPIC/PharmGKB guidelines apply unchanged.

### Advanced therapeutics

**Gene replacement therapy — the leading translational prospect, preclinical.** [CACHE-VERIFIED, PMID:39169623]:

> "Importantly, neonatal AAV9-mediated gene supplementation of Stambp in the brain could significantly improve neurological defects, sustain growth, and prolong the lifespan of StambpSox1-cKO mice. Together, our findings reveal a central role of brain defects in the pathogenesis of STAMBP deficiency and provide preclinical evidence that postnatal gene replacement is an effective approach to cure the disease."

Why this is unusually promising for a microcephaly gene:
- *STAMBP* cDNA is small (424 aa, ~1.3 kb) — comfortably within AAV packaging capacity.
- The rate-limiting pathology is **CNS-intrinsic** — the Sox1-cKO (CNS-restricted) mouse phenocopies the global null, so brain-directed delivery should be sufficient. This is a genuinely important finding: it means peripheral/endothelial correction may be unnecessary.
- **Postnatal** intervention worked, meaning the therapeutic window is not closed at birth.
- AAV9 CNS gene therapy is a clinically validated route (onasemnogene abeparvovec for SMA).

Limits to state plainly: mouse only; neonatal dosing (human equivalent window is narrow and would require prenatal or immediate-postnatal diagnosis); improvement not cure; no IND, no trial, no human data. NCIT `NCIT:C15238` Gene Therapy; modality `GENE_THERAPY`.

**Other advanced modalities:** no cell therapy, no ASO, no siRNA, no mRNA therapy, no small-molecule targeted agent, no immunotherapy has been developed or trialled. `aso_details` is not applicable.

### Rationally-derived experimental hypotheses (none tested in MIC-CAP)

These belong in `discussions` with `kind: KNOWLEDGE_GAP` and `proposed_experiments`, **not** in `treatments`:

1. **mTOR inhibition (sirolimus/everolimus).** Rationale: patient LCLs show constitutive PI3K-AKT-mTOR activation (PMID:23542699); sirolimus is established in *PIK3CA*-related vascular anomalies and everolimus in TSC-associated epilepsy. Counter-argument: the S236F patient had CMs *without* mTOR activation (PMID:29907875), and inhibiting a pathway in a cell already dying from failed proteostasis could plausibly worsen matters. **Speculative.**
2. **MEK inhibition.** Same logic via the RAS-MAPK arm; same caveats.
3. **IL-1β blockade (anakinra/canakinumab).** Rationale: AMSH restrains NLRP3 via K63-deubiquitination (PMID:33253913) and the mouse shows *"massive neuroinflammation"* (PMID:39169623). Attractive because anakinra is already used in refractory epilepsy syndromes (FIRES). **Untested.**
4. **CFLAR/death-receptor pathway modulation.** Rationale: *"ectopic expression of CFLAR rescues NPC defects induced by STAMBP-deficiency"* (PMID:38951308). Currently a cell-culture rescue with no druggable route.
5. **Autophagy/proteostasis enhancement.** Rationale: ubiquitin-conjugate aggregates plus elevated LC3-II. Direction of benefit unclear — flux is already up.

### Treatment strategy summary

There is **no published treatment algorithm** for MIC-CAP. Practical sequence, synthesized from GeneReviews plus the case literature:

1. Confirm diagnosis molecularly; counsel family on recurrence risk (checking for UPD).
2. Establish seizure control with standard DEE-directed ASMs; consider **vigabatrin early** given the infantile-spasms phenotype and the one reported response; consider *POLG* status and exercise caution with valproate, monitoring lipase/amylase if used.
3. Assess swallowing early; place a gastrostomy before recurrent aspiration is established.
4. Ophthalmology (optic atrophy/CVI), audiology, thyroid function, echocardiogram at baseline.
5. Physiotherapy, orthotics, seating; contracture prophylaxis.
6. Introduce complex-care/palliative-care involvement early — this is explicitly recommended and reflects realistic prognosis.
7. Discuss research participation; there are no open trials, but natural-history data collection is badly needed.

### Clinical trials

**A ClinicalTrials.gov search returns no interventional or observational study for MIC-CAP or *STAMBP*.** Curators should record zero trials. Note that **NCT05577754** (alpelisib in MCAP) surfaces in searches for "capillary malformation" — it is for **megalencephaly**-CAP (*PIK3CA*) and is **not** applicable to MIC-CAP. Including it would be a Named Entity Confusion error.

---

## 13. Prevention

### Primary prevention

No primary prevention of the genetic lesion is possible. The available levers are reproductive:

- **Preconception carrier testing** in families with a known variant, and in consanguineous couples in high-prevalence settings.
- **Consanguinity counseling** at the community/public-health level — the only population-level intervention with any plausible effect, and relevant given the Egyptian, Saudi, Arab, and Kuwaiti families reported.
- **Preimplantation genetic testing (PGT-M)** and **prenatal diagnosis (CVS/amniocentesis)** — both explicitly available once familial variants are known [CACHE-VERIFIED, PMID:24354023]: *"carrier testing for at-risk family members, prenatal testing for pregnancies at increased risk, and preimplantation genetic testing are possible."*
- **Gamete/embryo donation** as an alternative reproductive option.

**Not applicable:** vaccination, chemoprophylaxis, dietary or lifestyle modification, environmental remediation, vector control — none has any bearing on a monogenic recessive disorder with no environmental component.

### Secondary prevention (early detection)

- **No newborn screening** for *STAMBP*, and no near-term prospect of it — NBS requires a presymptomatic intervention, which does not yet exist. **However, the AAV9 mouse result changes the calculus prospectively:** if postnatal gene replacement ever reaches the clinic, *STAMBP* would become a rational NBS candidate, since the demonstrated therapeutic window is neonatal. Worth recording as a forward-looking note.
- **Prenatal ultrasound** may detect microcephaly and IUGR in the third trimester in a pregnancy already known to be at risk, but is neither sensitive nor specific enough for population screening.
- **Cascade testing** of at-risk relatives once the familial variants are known.
- **Risk stratification:** the only meaningfully high-risk group is *sibs of an affected proband* — 25% with biparental inheritance, <1% with UPD.

### Tertiary prevention (preventing complications in affected individuals)

This is where nearly all realizable prevention lies, and it maps directly onto the GeneReviews surveillance recommendations [CACHE-VERIFIED, PMID:24354023]: *"Regular follow up with a child neurologist for seizure management and a complex care / palliative care team or experienced pediatrician to monitor for complications associated with severe neurologic impairment."*

| Target complication | Preventive measure |
|---|---|
| Aspiration pneumonia | Early swallowing assessment; **gastrostomy** — *"A feeding tube is essential"*; positioning; oral-secretion management |
| Malnutrition / growth failure | Enteral nutrition with dietitian oversight |
| Contractures, hip subluxation, scoliosis | *"proper seating and bracing to maintain posture and prevent contractures"*; PT/OT; orthopedic surveillance |
| Status epilepticus | Optimized ASM regimen; written rescue-medication plan for families |
| **Valproate-associated pancreatitis** | Avoid or use valproate cautiously; monitor amylase/lipase if used — this is a *preventable* death mode based on the one documented fatality |
| Respiratory infection | Routine immunizations incl. influenza/RSV prophylaxis; chest physiotherapy |
| Vision/hearing deprivation | Ophthalmology and audiology surveillance |
| Untreated hypothyroidism | Thyroid function testing (NBS plus targeted retesting) |
| Dental disease, pressure injury, constipation | Standard complex-care protocols for profound neurodisability |

### Counseling

Genetic counseling is the central preventive intervention. Content must cover: autosomal recessive inheritance; the **25% vs. <1% recurrence-risk fork depending on biparental inheritance vs. uniparental isodisomy**; carrier status of sibs; prenatal and PGT options; the poor prognosis and the appropriateness of early palliative-care involvement; and the absence of disease-modifying therapy alongside the existence of promising preclinical gene-therapy data. NCIT: `NCIT:C15240` Genetic Counseling.

---

## 14. Other Species / Natural Disease

### Taxonomy and orthologs

| Species | NCBI Taxon | Gene | Gene ID | Notes |
|---|---|---|---|---|
| *Homo sapiens* | NCBITaxon:9606 | *STAMBP* | 10617 | reference |
| *Mus musculus* | NCBITaxon:10090 | *Stambp* | 14676 **[VERIFY]** | the principal disease model |
| *Rattus norvegicus* | NCBITaxon:10116 | *Stambp* | — **[VERIFY]** | no disease model reported |
| *Danio rerio* | NCBITaxon:7955 | *stambp* | — **[VERIFY]** | no published MIC-CAP model |
| *Drosophila melanogaster* | NCBITaxon:7227 | *AMSH* (CG battery) **[VERIFY]** | — | ESCRT/Notch trafficking studies |
| *C. elegans* | NCBITaxon:6239 | ortholog present **[VERIFY]** | — | |
| *Arabidopsis thaliana* | NCBITaxon:3702 | *AMSH3* | — | Plant ortholog; endosomal localization requires ALIX (PMID:26324913) |
| *Magnaporthe oryzae* | NCBITaxon:318829 | *MoAMSH* | — | Fungal ortholog inhibits autophagy via MoAtg6 (PMID:41310665, 2025) |

**Human paralog:** *STAMBPL1* (AMSH-LP), which shares the K63-specific JAMM activity and provided the crystal structures in PMID:18758443. *STAMBPL1* is **not** a MIC-CAP gene and evidently cannot compensate for *STAMBP* loss in neurons — a notable and unexplained lack of paralog redundancy.

### Evolutionary conservation

The AMSH/ESCRT axis is conserved from plants and fungi to mammals, and the K63-linkage-selective JAMM chemistry is conserved across the family. **The disease-relevant function — a cell-autonomous survival requirement in forebrain neurons — is, however, a vertebrate/mammalian specialization**, since plant and fungal orthologs regulate autophagy and endosomal sorting without any neuronal context. This makes mouse the only species in which the disease mechanism is meaningfully modelable.

### Natural disease in other species

**None reported.** A search of the comparative-genetics literature finds:
- **No OMIA entry** for a naturally occurring *STAMBP* disorder in any domestic or wild animal species.
- No canine, feline, bovine, ovine, equine, or porcine microcephaly-capillary malformation phenotype attributed to *STAMBP*.
- No VBO breed-specific association.

All animal *Stambp* disease phenotypes are **laboratory-engineered**, not natural. This is a clean negative worth recording explicitly.

### Comparative pathology

The mouse-to-human concordance is unusually good for a microcephaly gene, which is what makes the model credible:

| Feature | Human MIC-CAP | *Stambp*/AMSH-null mouse |
|---|---|---|
| Microcephaly | congenital + progressive | *"progressive microcephaly"* [PMID:39169623] |
| Growth failure | SGA 7/10, postnatal FTT | *"postnatal growth retardation"* [PMIDs 11713295, 39169623] |
| Hippocampal vulnerability | hypoplastic hippocampus 6/7 | *"complete loss of the CA1 neurons in the hippocampus"* [PMID:11713295] |
| Cortical atrophy | progressive, universal | *"marked atrophy of the cerebral cortex"* [PMID:11713295] |
| Cerebellar sparing | *"disproportionately small cerebral hemispheres compared to the cerebellum"* | *"AMSH-deficient cerebellar neurons ... survived normally"* [PMID:11713295] |
| Ubiquitin aggregates | patient LCLs | brain, from E10 [PMID:21531206] |
| Neuroinflammation | not assessed in human | *"massive neuroinflammation"* [PMID:39169623] |
| Early death | ≥3 infant deaths; oldest 12 y | P19–P23, 100% penetrant |
| **Capillary malformations** | **universal (10/10)** | **NOT reported** |
| **Epilepsy** | **universal (10/10)** | **NOT reported** |

**The two mismatches are the interesting part** and should be curated as `kind: HUMAN_MODEL_MISMATCH` (evidence exists in the model, but translational validity for these specific features is the open question):
1. **No capillary malformation in the mouse.** Either the vascular phenotype requires human-specific dermal vascular biology, or it is too subtle to have been looked for. Nobody appears to have examined mouse skin vasculature systematically in a *Stambp* null. **A tractable, cheap experiment.**
2. **No reported seizures in the mouse.** Given hippocampal CA1 destruction and glutamate-receptor accumulation, a seizure phenotype is predicted; the absence may simply reflect that no one has done video-EEG on these animals before they die at P19–P23. **Also tractable.**

### Zoonotic potential and cross-species transmission

**Not applicable.** MIC-CAP is a non-transmissible germline genetic disorder.

---

## 15. Model Organisms

### Mouse models — the workhorse

**1. Constitutive AMSH/*Stambp* knockout (Ishii et al., 2001)** — the original, still the most-cited [TRANSCRIBED, PMID:11713295]:

> "To investigate the in vivo functional role of AMSH, we have generated AMSH-deficient mice by gene targeting."
> "The AMSH-deficient mice were morphologically indistinguishable from their littermates at birth, and histopathological examinations revealed normal morphogenesis in all tissues tested. However, all the AMSH-deficient mice exhibited postnatal growth retardation and died between postnatal day 19 (P19) and P23."
> "Taken together, these observations indicate that AMSH is an essential molecule for the survival of neuronal cells in early postnatal mice."

Note the important detail that the mice are **normal at birth** and degenerate postnatally — a partial mismatch with the human congenital microcephaly, and further support for the two-phase (developmental + degenerative) model in §6.

**2. Same line, proteostasis characterization (2011)** [TRANSCRIBED, PMID:21531206] — establishes E10 onset of ubiquitin accumulation, and TDP-43 / p62 / glutamate-receptor co-accumulation. Framed by its authors as a **neurodegeneration model** as much as a MIC-CAP model.

**3. CNS-conditional *Stambp*^Sox1-cKO (Hu et al., 2024)** — the current best preclinical model, and the one purpose-built for therapy testing [CACHE-VERIFIED, PMID:39169623]:

> "To establish a suitable preclinical animal model for clinical therapeutic practice, we generated a central nervous system (CNS)-specific Stambp knockout mouse model (Stambp Sox1-cKO) that phenocopies Stambp null mice including progressive microcephaly, postnatal growth retardation and complete penetrance of preweaning death."

The *Sox1-Cre* driver deletes across neural-plate-derived CNS lineages. That this **fully phenocopies the global null** is the model's key scientific contribution: it localizes the lethal pathology to the CNS and justifies brain-restricted therapy. Applications: gene-therapy dosing/timing, biomarker development, neuroinflammation studies.

**MGI/IMSR:** the mouse gene is *Stambp*, chromosome 6 **[VERIFY MGI accession — the MGI marker page could not be retrieved during this research; do not cite an MGI ID without confirming it]**. Check MGI, IMPC, KOMP/EuMMCR, and IMSR for currently distributed alleles.

### Human cellular and organoid models

**4. Patient-derived EBV-transformed lymphoblastoid cell lines (LCLs)** — the standard patient-material assay system. Used in PMID:23542699 (P1.1, P1.2, P3.1, P7.1: ubiquitin aggregates, cleaved caspase-3, Annexin V, RAS-GTP, pERK, pAKT, pS6, LC3-II, plus lentiviral rescue) and PMID:29907875 (STAMBP immunoblot, pS6). **Strength:** genuine patient genotype, easy to bank. **Major limitation:** a B-lymphoblast is not a neuron and not an endothelial cell — the two cell types that actually matter. The S236F pS6 discrepancy may well be an artifact of this mismatch, and the KB should say so.

**5. *STAMBP*-knockout human cortical organoids (Hu et al., 2022)** [CACHE-VERIFIED, PMID:36033615] — *"A 3D human cortical organoid model was used to investigate the function of STAMBP and the pathogenicity of the novel mutation (c.920G > A, p.G307E)."* Recapitulates reduced organoid size via NSC proliferation failure and supports **variant-specific functional testing** (WT rescues; G307E and T313I do not). This is the best available **human** assay for classifying *STAMBP* VUS — directly relevant to the several VUS sitting in ClinVar.

**6. *STAMBP*-deficient hESC-derived NPCs (2024)** [TRANSCRIBED, PMID:38951308] — establishes that STAMBP is dispensable for pluripotency and for neural differentiation per se, but required for long-term NPC maintenance via CFLAR. Also yields a methods insight the authors flag: *"counteracting this cell death pathway could be beneficial to the generation of NPCs in vitro."*

**7. Transformed cell lines** — T98G glioblastoma with *STAMBP* siRNA (PMID:23542699); monocyte lines with CRISPR *STAMBP* KO for inflammasome work (PMID:33253913). Useful for pathway dissection, not for disease modeling.

**8. Biochemical/structural systems** — recombinant AMSH-LP DUB domain ± K63-di-ubiquitin (PMID:18758443, 1.2 Å and 1.6 Å); full-length STAMBP and MIT-CD complex (PMID:40441142). These provide the structural basis for interpreting missense variants and are directly useful for ACMG PS3/PM1 argumentation.

### Models that do NOT exist (all are real, fillable gaps)

- **No zebrafish *stambp* model** — surprising, given that zebrafish is the standard rapid model for both microcephaly and vascular patterning, and would be the natural system in which to test whether AMSH loss produces a capillary phenotype.
- **No *Drosophila* or *C. elegans* MIC-CAP model.**
- **No conditional endothelial-specific *Stambp* knockout** — this is the **single most important missing model**, because it is the only way to test the capillary-malformation arm directly. A *Cdh5-CreER;Stambp^fl/fl* mouse would resolve whether the CMs are endothelial-cell-autonomous and whether they are mTOR-dependent.
- **No patient-derived iPSC lines** reported in a public repository (check hPSCreg/Cellosaurus before asserting this definitively).
- **No humanized or knock-in point-mutation mouse** (e.g., a *Stambp*^R38C/R38C or ^T313I/T313I allele that would test genotype-phenotype correlation in vivo).
- **No large-animal model.**

### Phenotype recapitulation summary

| Human feature | Mouse KO | Cortical organoid | hESC-NPC | Patient LCL |
|---|---|---|---|---|
| Microcephaly / small brain | ✅ progressive | ✅ smaller organoids | — | — |
| Neuronal loss (CA1, cortex) | ✅ strongly | ❌ no apoptosis early | ✅ NPC death (CFLAR) | ✅ ↑caspase-3, Annexin V |
| Ubiquitin aggregates | ✅ from E10 | — | — | ✅ |
| RAS-MAPK / PI3K-mTOR activation | not assessed | — | — | ✅ (except S236F) |
| Reduced progenitor proliferation | not assessed | ✅ primary finding | ✅ | — |
| Neuroinflammation | ✅ | — | — | — |
| Growth failure / early death | ✅ 100% penetrant | n/a | n/a | n/a |
| **Capillary malformations** | ❌ | ❌ (no vasculature) | ❌ | ❌ |
| **Epilepsy** | ❌ not reported | ❌ | ❌ | ❌ |

### Resources to query

MGI (informatics.jax.org), IMPC, KOMP/EuMMCR, IMSR, MMRRC, EMMA, Alliance of Genome Resources, ZFIN (no model expected), Cellosaurus / hPSCreg (iPSC lines), Addgene (STAMBP constructs), PDB (AMSH-LP DUB domain structures from PMID:18758443; MIT-CD complex from PMID:40441142).

---

## Consolidated curation checklist for the dismech entry

**Recommended dismech modeling decisions:**

1. **Entity scope:** single `Disease` entry, `disease_term: MONDO:0013659`. Consider `has_subtypes` splitting **Classic MIC-CAP** vs. **Attenuated / CM-negative STAMBP-NDD** (PMID:36033615), since capillary malformation is no longer obligate.
2. **`biological_scale` tagging:** MOLECULAR (STAMBP LOF; loss of K63-DUB activity) → CELLULAR (ESCRT sorting failure; Ub-conjugate aggregation; NSC proliferation failure; apoptosis) → TISSUE (CA1/cortical neuronal loss; dermal capillary malformation) → ORGANISM (microcephaly, DEE, spastic quadriparesis).
3. **Candidate module conformances to evaluate:**
   - `epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance` — well-supported, especially via glutamate-receptor accumulation (PMID:21531206).
   - `rtk_grb2_signaling_adaptation` — the RTK-downregulation-failure arm.
   - `peripheral_axonal_degeneration` — **probably not**; this is a central, not peripheral, degeneration.
   - A "failed clearance → substrate accumulation → cytotoxicity" pattern shared with `lysosomal_substrate_accumulation` and `amyloidogenesis`, but the substrate class (K63-Ub conjugate pool) differs enough that a **new module** may be warranted rather than a forced conformance.
4. **`mechanistic_hypotheses` to declare:**
   - `ubiquitin_aggregate_apoptosis` (CANONICAL) — PMIDs 23542699, 11713295, 21531206, 39169623.
   - `mtor_mapk_capillary_malformation` (EMERGING, contested) — supported by PMID:23542699, **refuted for one allele** by PMID:29907875.
   - `progenitor_proliferation_failure` (EMERGING) — PMIDs 36033615, 38951308; explains congenital (vs. progressive) microcephaly.
   - `nlrp3_il1b_neuroinflammation` (EMERGING, in vitro only) — PMIDs 33253913, 39169623.
5. **`discussions` blocks:**
   - `HUMAN_MODEL_MISMATCH` — mouse shows apoptosis-dominant pathology; human organoids show proliferation-dominant pathology with **no** early apoptosis (PMID:36033615). Also: mouse lacks both capillary malformations and epilepsy, the two human features most in need of a model.
   - `KNOWLEDGE_GAP` — no human brain ubiquitin/TDP-43 IHC; no skin-biopsy endothelial signaling study; no omics of any kind; no QoL instrument; no natural-history study; no gnomAD constraint retrieved; no endothelial-conditional mouse.
6. **Evidence hygiene:** run `just fetch-reference` for every PMID marked **[TRANSCRIBED]** (21815250, 35962715, 38951308, 11713295, 21531206, 18758443, 33253913, 40441142) and re-verify snippets before commit. The nine **[CACHE-VERIFIED]** PMIDs are already safe to quote.
7. **Ontology hygiene:** run `just validate-terms` on the finished file. Terms marked **[VERIFY]** in this report were reasoned from convention, not confirmed against OAK/OLS in this session.
8. **NEC guardrail:** add a `notes` line distinguishing MIC-CAP (*STAMBP*, AR, microcephaly) from MCAP/M-CM (*PIK3CA*, mosaic, megalencephaly). The two are the most confusable disease pair in this corner of the nosology, and the alpelisib trial NCT05577754 is a live trap.

---

## Sources

**Primary literature (PubMed/PMC):**
- [PMID:23542699 — McDonell et al. 2013, *Nat Genet* — STAMBP mutations cause MIC-CAP](https://pubmed.ncbi.nlm.nih.gov/23542699/) · [PMC4000253](https://pmc.ncbi.nlm.nih.gov/articles/PMC4000253/)
- [PMID:24354023 / NBK174452 — Carter, Mirzaa, McDonell, Boycott — GeneReviews (updated 2021-03-18)](https://www.ncbi.nlm.nih.gov/books/NBK174452/)
- [PMID:21815250 — Mirzaa et al. 2011, *Am J Med Genet A*](https://pubmed.ncbi.nlm.nih.gov/21815250/) · [PMID:21834052 — Carter & Boycott 2011 commentary](https://pubmed.ncbi.nlm.nih.gov/21834052/) · Carter et al. 2011, *Am J Med Genet A* 155A:301–306 (original delineation)
- [PMID:35962715 — Further clinical delineation, 2022](https://pubmed.ncbi.nlm.nih.gov/35962715/) · [PMID:41603106 — Expanding the phenotype, 2026](https://pubmed.ncbi.nlm.nih.gov/41603106/) · [PMID:35770778 — MIC-CAP as recognizable DEE, 2022](https://pubmed.ncbi.nlm.nih.gov/35770778/)
- [PMID:27531570](https://pubmed.ncbi.nlm.nih.gov/27531570/) · [PMID:29907875](https://pubmed.ncbi.nlm.nih.gov/29907875/) · [PMID:25692795](https://pubmed.ncbi.nlm.nih.gov/25692795/) · [PMID:25266620](https://pubmed.ncbi.nlm.nih.gov/25266620/) · [PMID:31638258](https://pubmed.ncbi.nlm.nih.gov/31638258/) · [PMID:38058451](https://pubmed.ncbi.nlm.nih.gov/38058451/) · [PMID:32929933](https://pubmed.ncbi.nlm.nih.gov/32929933/)
- [PMID:36033615 — cortical organoid, proliferation defect, 2022](https://pubmed.ncbi.nlm.nih.gov/36033615/) · [PMID:38951308 — hESC-NPC/CFLAR, 2024](https://pubmed.ncbi.nlm.nih.gov/38951308/) · [PMID:39169623 — AAV9 gene therapy in Stambp^Sox1-cKO, 2024](https://pubmed.ncbi.nlm.nih.gov/39169623/)
- [PMID:11713295 — AMSH-deficient mice, 2001](https://pubmed.ncbi.nlm.nih.gov/11713295/) · [PMID:21531206 — AMSH and ubiquitinated protein degradation in CNS, 2011](https://pubmed.ncbi.nlm.nih.gov/21531206/)
- [PMID:18758443 — Sato et al., structural basis for K63-specific cleavage, *Nature* 2008](https://pubmed.ncbi.nlm.nih.gov/18758443/) · [PMID:40441142 — MIT-domain autoinhibition, *Structure* 2025](https://pubmed.ncbi.nlm.nih.gov/40441142/) · [PMID:33253913 — STAMBP and the NLRP3 inflammasome, 2021](https://pubmed.ncbi.nlm.nih.gov/33253913/)

**Databases:**
- [OMIM #614261 (MICCAP)](https://omim.org/entry/614261) · OMIM *606247 (STAMBP)
- [Orphanet ORPHA:294016](https://www.orpha.net/en/disease/detail/294016)
- [HPO annotations for OMIM:614261 (ontology.jax.org API)](https://ontology.jax.org/api/network/annotation/OMIM:614261)
- [UniProt O95630](https://rest.uniprot.org/uniprotkb/O95630.txt) · [HGNC:16950](https://rest.genenames.org/fetch/symbol/STAMBP)
- ClinVar (STAMBP P/LP query, NCBI E-utilities) · [NIH GTR condition C3280296](https://www.ncbi.nlm.nih.gov/gtr/conditions/C3280296/)
- [MONDO:0013659 via EBI OLS4](https://www.ebi.ac.uk/ols4/api/search?q=microcephaly-capillary%20malformation%20syndrome&ontology=mondo) (also used for GO/CL/UBERON/CHEBI/NCIT verification)
- [MedlinePlus Genetics: microcephaly-capillary malformation syndrome](https://medlineplus.gov/download/genetics/condition/microcephaly-capillary-malformation-syndrome.pdf) · [GARD entry](https://rarediseases.info.nih.gov/diseases/17354/microcephaly-capillary-malformation-syndrome)