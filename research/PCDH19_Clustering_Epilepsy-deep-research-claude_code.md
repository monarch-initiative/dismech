---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-8
cached: false
start_time: '2026-07-17T23:28:35.811612'
end_time: '2026-07-17T23:35:18.380895'
duration_seconds: 402.57
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: PCDH19 Clustering Epilepsy
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
  - claude-opus-4-8
  web_search_requests: 6
  num_turns: 16
  total_cost_usd: 1.85920825
  session_id: a8912661-de18-4f2f-a4ff-943dc5b7446a
  stop_reason: end_turn
citation_count: 22
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PCDH19 Clustering Epilepsy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PCDH19 Clustering Epilepsy** covering all of the
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

Alright, I've got what I need. Here's the full report.

---

# PCDH19 Clustering Epilepsy — Comprehensive Research Report

**Prepared for dismech KB curation | Category: Mendelian (X-linked)**

> A quick word before we wade in, since this is going into a knowledge base: I've pulled PMIDs from the literature and from search, but per the project's own anti-hallucination SOP, treat every PMID and quote below as a **lead to verify** with `just fetch-reference PMID:XXXX` before it becomes an evidence snippet. I've flagged the handful where my confidence on the exact PMID digits is softer. The ontology IDs (MONDO/HGNC) I pulled straight from the local OAK adapters, so those are solid.

PCDH19 is one of biology's little contrarians. It sits on the X chromosome, and yet it breaks the classic X-linked rulebook completely backwards — the girls (heterozygous) get the disease, and the boys carrying the exact same broken copy (hemizygous) mostly walk away fine. The disease *needs* the mosaic. A brain that's uniformly broken is, paradoxically, a brain that works. That's the whole strange heart of this thing, and it drives basically every section below.

---

## 1. Disease Information

**Overview.** PCDH19 Clustering Epilepsy (PCDH19-CE) is an X-linked developmental and epileptic encephalopathy caused by loss-of-function variants in *PCDH19* (protocadherin 19). Its signature is **early-life seizures that come in tight clusters**, are strongly fever-sensitive, and are frequently accompanied by intellectual disability, autism spectrum features, and other neuropsychiatric problems. It affects females and rare mosaic males, while "transmitting" hemizygous males are typically spared.

**Key identifiers** (verified against local MONDO/HGNC adapters):

| Resource | ID |
|---|---|
| MONDO | **MONDO:0010246** (developmental and epileptic encephalopathy, 9) |
| OMIM (phenotype) | **#300088** (DEE9; formerly EIEE9 / EFMR) |
| OMIM (gene) | **\*300460** (PCDH19) |
| HGNC | **hgnc:14270** (PCDH19) — note the lowercase-prefix convention this repo uses |
| Orphanet | **ORPHA:101039** |
| DOID | DOID:0060848 |
| MeSH | C564715 |
| UMLS | C1848137 · MedGen 338393 · GARD 0010806 |
| Cytogenetic location | **Xq22.1** (OMIM lists Xq22) |

**Synonyms / alternative names** (from MONDO): DEE9; EIEE9; EFMR (Epilepsy and Mental Retardation Limited to Females); Epilepsy, Female-restricted, with Mental Retardation; PCDH19-related female-limited epilepsy (PCDH19-FE / FLE); PCDH19-related infantile epileptic encephalopathy; Juberg-Hellman syndrome; "Girls Clustering Epilepsy." The field has largely converged on **"PCDH19 Clustering Epilepsy"** because the older names got the sex-limitation and the ID emphasis slightly wrong (mosaic males exist; many patients have normal intellect).

**Data provenance.** Disease-level aggregated resources (OMIM, Orphanet, MONDO) plus cohort/case-series literature. Not EHR-derived at the individual level; the large phenotyping series (e.g. Kolc et al., Transl Psychiatry 2020, **PMID:32366910**) are patient-registry/cohort aggregations.

MONDO places it as a subclass of *X-linked intellectual disability–epilepsy syndrome* (MONDO:0016160), *genetic developmental and epileptic encephalopathy* (MONDO:0100062), and *X-linked complex neurodevelopmental disorder* (MONDO:0100148).

---

## 2. Etiology

**Primary cause — genetic.** Heterozygous (female) or mosaic (male) loss-of-function variants in **PCDH19**. This is a monogenic disorder; there is no established environmental *cause*. Fever/illness is a potent **trigger/precipitant** of seizure clusters, not a cause of the disease itself.

**Genetic risk factors.**
- The causal event is the *PCDH19* variant. There is no separate "susceptibility locus" architecture in the GWAS sense — this is Mendelian.
- **Sex is the dominant effect modifier**: being female (constitutively mosaic via random X-inactivation) is effectively the prerequisite for the classic phenotype. Genetic males require *somatic mosaicism* to be affected.
- X-inactivation skewing plausibly modulates the mutant:wild-type cell ratio and hence severity, though a clean genotype–XCI–severity correlation has not been firmly nailed down.

**Environmental / trigger factors.** Febrile illness is the archetypal precipitant of clusters; vaccination-associated fever and intercurrent infection are commonly reported cluster triggers. These modulate *expression/timing*, not disease occurrence.

**Protective factors.** None genetically established. The most striking "protective" observation is the counterintuitive one: **uniform hemizygous expression of mutant PCDH19 in males is protective against the epilepsy** (the mosaic, not the mutation per se, is pathogenic) — the cellular-interference logic in §6.

**Gene–environment interaction.** The central G×E axis is **variant × febrile/inflammatory stress**: the mutant mosaic brain has a lowered threshold such that fever/illness reliably pushes it into clustered seizures. There is emerging interest in a **blood–brain-barrier / neuroinflammation** contribution to that fever sensitivity (see §6).

---

## 3. Phenotypes

Frequencies below are anchored to the standardized phenotyping cohort (Kolc et al. 2020, **PMID:32366910**, n≈112) and corroborating series.

**Seizures (core).**
- **Seizure clusters** — the defining feature: **94%** (106/112) had clustered seizures. Clusters averaged ~4.6 days and ~15 seizures each (range 2–100). → HPO **HP:0032807** *Cluster of seizures* (verify exact HP label); **HP:0001250** *Seizure*.
- **Focal (focal-onset) seizures**, often with a **fearful/affective component** ("fearful screaming") — highly characteristic. → **HP:0007359** *Focal-onset seizure*.
- **Febrile / fever-sensitive seizures** — clusters typically ignited by fever. → **HP:0002373** *Febrile seizure* / **HP:0011171** *Generalized-onset seizure* as applicable; consider `temporality: RECURRENT`.
- Also tonic-clonic, tonic, absence, myoclonic, atonic seizures reported. → **HP:0002069**, **HP:0032792**, **HP:0002121**, **HP:0002123**, **HP:0010819**.

**Neurodevelopmental / cognitive.**
- **Intellectual disability** — spectrum, and importantly **~56% have normal intellect** in the standardized cohort; among the rest: mild 18%, moderate 8%, severe 12.5%, profound 2%. → **HP:0001249** *Intellectual disability* (severity qualifier variable).
- **Autism spectrum disorder** — **~62%** met ASD criteria. → **HP:0000717** *Autism*.
- **Executive dysfunction** — **~63%**. → **HP:0002019**-adjacent / behavioral abnormality terms.
- **ADHD / hyperactivity** — frequently reported. → **HP:0007018** *Attention deficit hyperactivity disorder*.
- **Obsessive-compulsive / psychiatric features** — OCD ~21% of assessed; **psychiatric risk (including psychotic/schizophrenia-spectrum disorders) rises in adulthood**. → **HP:0000722** *Obsessive-compulsive behavior*; **HP:0100753** *Schizophrenia*.
- Aggression, mood/behavioral disturbance common. → **HP:0000718** *Aggressive behavior*.

**Phenotype characteristics (summary).**
- **Onset:** infancy/early childhood; **mean ~12 months, median ~10 months** in females (range 1.5–60 mo); OMIM/Orphanet quote ~10 months average, range ~2 mo–3 yr.
- **Severity:** variable — from normal-cognition/seizure-limited to severe DEE.
- **Course:** **episodic/clustered** seizure pattern superimposed on a chronic disorder; many see seizure attenuation in later childhood/adolescence.
- **Genotype-independent severity driver:** **earlier onset + higher seizure burden → worse ID, ASD, executive dysfunction** (Kolc 2020: association p=0.001 for ASD, p≈4.7×10⁻⁴ for executive dysfunction).

**Quality-of-life impact.** High: **75%** scored "very high" on SDQ impact. Cluster unpredictability, fever-triggered emergencies, and neuropsychiatric comorbidity dominate family burden; adult psychiatric risk is a major long-horizon concern.

---

## 4. Genetic / Molecular Information

**Causal gene.** **PCDH19** (protocadherin 19), Xq22.1, OMIM \*300460, hgnc:14270. Encodes a **δ2-protocadherin**, a **non-clustered** member of the cadherin superfamily — a calcium-dependent cell–cell adhesion glycoprotein predominantly expressed in brain. Domain architecture: **6 extracellular cadherin (EC) repeats**, a transmembrane domain, and a cytoplasmic tail with conserved motifs **CM1/CM2** (per protocadherin structure review, **PMID:34201522** — verify).

**Pathogenic variants.**
- **Variant types:** the full loss-of-function spectrum — **missense, nonsense, frameshift (small indels), splice-site**, and whole/partial-gene **deletions**; a **triplication** mechanism has also been described (MDPI Genes 2024, PMC11506946). Missense variants cluster in the **extracellular cadherin domains** (EC1–EC6), consistent with disrupted homophilic adhesion.
- **>120 distinct variants** reported; most are **family-specific/private**, with a handful of recurrent ones.
- **De novo rate: ~48–70%** across cohorts (Kolc 2020: 48% de novo; epilepsiome/clinical reviews cite ~70%).
- **Classification:** per ACMG/AMP, LoF is an established mechanism, so null variants are readily P/LP; missense VUS burden exists — check ClinVar/ClinGen.
- **Allele frequency:** pathogenic variants are essentially absent from population controls (gnomAD) given severity/de-novo nature.
- **Somatic vs germline:** germline in females; **affected males are typically postzygotic somatic mosaics** (variant allele fraction correlates loosely with phenotype severity — PMC9669318).
- **Functional consequence:** **loss of function / haploinsufficiency at the cellular level**, but the *pathogenic unit is the mosaic tissue*, not the single null cell.

**Modifier genes / downstream expression.** *PCDH19* dysfunction perturbs **steroidogenic gene expression** — notably genes in the **allopregnanolone (neurosteroid) synthesis pathway** (e.g. *AKR1C1/2/3*, *CYP* steroidogenic enzymes), yielding an "allopregnanolone deficiency" signature in patients (Tan et al. 2015 — verify PMID). This is both a candidate modifier axis and a therapeutic hook (§12).

**Epigenetic.** No established disease-defining methylation signature (episignature) as of current literature; **X-inactivation** is the dominant epigenetic determinant because it sets the mosaic ratio. Worth flagging as a knowledge gap.

**Chromosomal abnormalities.** Large *PCDH19* deletions and the reported triplication are detectable by CMA; otherwise this is a single-gene disorder, not an aneuploidy syndrome.

Suggested annotations: gene **hgnc:14270**; GO cellular component **GO:0005911** *cell-cell junction* / **GO:0005912** *adherens junction*; molecular function **GO:0005509** *calcium ion binding*, **GO:0098631** *cell adhesion mediator activity*.

---

## 5. Environmental Information

- **Environmental factors:** no toxin/pollutant/radiation etiology. The relevant "environmental" input is **febrile/inflammatory stress** as a cluster precipitant.
- **Lifestyle factors:** not a driver of disease occurrence; fever management and illness avoidance matter for cluster prevention.
- **Infectious agents:** **not causal**, but **intercurrent infection (via fever/inflammation) is the leading cluster trigger**. This is a candidate node for a BBB/neuroinflammation mechanism rather than a pathogen-specific one.

---

## 6. Mechanism / Pathophysiology

This is the meaty part, and it's genuinely one of the more elegant puzzles in epilepsy genetics. Think of it like a tissue that only misbehaves when you mix two paint colors — a wall painted all one color (all-mutant hemizygous male) looks fine; a wall with random patches of two colors (mosaic female) develops the crack.

**The protein's day job.** PCDH19 is a calcium-dependent adhesion molecule. It does **homophilic binding** (PCDH19-cell to PCDH19-cell) and **partners with N-cadherin (CDH2)** at adherens junctions to form a strongly adhesive complex. Through this it governs **neural progenitor division balance, neuronal migration, axon outgrowth, and synaptogenesis** — the scaffolding of a properly wired cortex.

**Causal chain (upstream → downstream):**

1. **Trigger — PCDH19 LoF variant in a mosaic context.** Random X-inactivation in females (or postzygotic mutation in males) yields a **salt-and-pepper mixture of PCDH19-positive and PCDH19-negative neurons**.
2. **Cellular interference / abnormal cell sorting.** The two populations **mis-sort and mis-communicate** at their boundaries — the mixed population is what's pathogenic, uniform populations are not. Pederick et al. (Neuron 2018, **PMID:29429936** — verify) showed **abnormal cell sorting** segregating wild-type from mutant cells in mosaic mouse cortex, the mechanistic cornerstone of the "why females, not hemizygous males" riddle.
3. **Altered neurogenesis (parallel/contributing arm).** Patient-iPSC and cortical-organoid models (PMC8268119; PMC11024992) show **accelerated/precocious neurogenesis**, a shift toward **asymmetric progenitor divisions**, premature differentiation, longer neurites, up-regulated neurogenic markers (NCAD, MAP2, TUBB3), **mitotic-spindle/centrosome abnormalities** (PCDH19 colocalizes with γ-tubulin; ~17% multipolar metaphases vs 4% control), and **smaller organoids**. Notably, a *Xenopus* model (PNAS 2024, PMC on pnas.org) argues some phenotypes are **mosaicism-independent**, so cellular interference isn't the whole story.
4. **Neurosteroid / GABAergic arm.** *PCDH19* dysfunction **down-regulates allopregnanolone synthesis** (a potent positive allosteric modulator of **GABA_A** receptors). Reduced allopregnanolone → **decreased GABA_A-mediated inhibition** → tilted excitation/inhibition balance. Emerging interneuron data (2025 mouse preprint, biorxiv 688097) show **focal reductions in parvalbumin-expressing cortical interneurons** and **hyperthermic seizure susceptibility** — a concrete substrate for both the E/I imbalance and the fever sensitivity.
5. **E/I imbalance → hyperexcitability → seizures.** The convergent endpoint: **network hyperexcitability and hypersynchrony → clustered focal seizures**, fever-facilitated.
6. **Neurodevelopmental output.** The same adhesion/migration/neurogenesis disruption yields the **ID/ASD/behavioral** phenotype in parallel with the epilepsy.

**Additional proposed contributors** (Trivisano et al., Epilepsy & Behavior 2024, S1525-5050(24)00111-2): asymmetric cell division/heterochrony, altered steroid-gene expression, **blood–brain-barrier dysfunction** (a candidate mediator of fever-triggered clusters), and reduced GABA_A function.

**Cell types / processes for annotation:**
- Cell types: **CL:0000617** *GABAergic neuron*; **CL:0000561** — use **CL:0000499** *stromal*? no — use **CL:0011005** *GABAergic interneuron* / **CL:0000598** *pyramidal neuron*; **CL:0000031** *neuroblast (neural progenitor)*; parvalbumin interneuron (CL for cortical interneuron).
- Biological processes: **GO:0007156** *homophilic cell adhesion via plasma-membrane adhesion molecules*; **GO:0007399** *nervous system development*; **GO:0001764** *neuron migration*; **GO:0022008** *neurogenesis*; **GO:0051301** *cell division* / **GO:0000278** *mitotic cell cycle*; **GO:0006874** *cellular calcium ion homeostasis*; neurosteroid-relevant **GO:0006702** *androgen biosynthetic process* / allopregnanolone synthesis; **GO:0060078** *regulation of postsynaptic membrane potential* (GABA_A).

This is a place to lean on the project's **`epilepsy_excitation_inhibition_imbalance` module** — the "excitation-inhibition imbalance → neuronal hyperexcitability/hypersynchrony → seizure generation" chain (conformance target `epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance`) fits PCDH19-CE's downstream endpoint cleanly, with the PCDH19-specific upstream (mosaic cellular interference + allopregnanolone/GABA_A) substituted in.

---

## 7. Anatomical Structures Affected

- **Organ / system:** central nervous system (**UBERON:0000955** *brain*), specifically **cerebral cortex** (**UBERON:0000956**) and **limbic/frontal networks** (fear/affective seizure semiology implicates temporo-limbic circuitry). Body system: **nervous system** (UBERON:0001016).
- **Tissue / cell:** cortical **neural progenitors** (ventricular/subventricular zone), **GABAergic interneurons** (incl. parvalbumin-expressing), excitatory pyramidal neurons. → CL terms in §6.
- **Subcellular:** **adherens junctions / cell–cell junctions** (**GO:0005912**), **plasma membrane** (GO:0005886), **centrosome / mitotic spindle** (**GO:0005813**, GO:0005819), and GABA_A-receptor-bearing **postsynaptic membrane** (GO:0045211).
- **Localization / lateralization:** brain imaging (MRI) is usually **normal/nonspecific**; no consistent focal lesion. Seizures are **focal but multifocal/bilateral-capable**; no fixed lateralization.

---

## 8. Temporal Development

- **Onset:** **infantile/early-childhood**, mean ~10–12 months (range ~2 months to 3–5 years). Onset is typically **subacute**, heralded by a **fever-triggered seizure cluster**.
- **Progression / course:** **episodic-clustering** superimposed on a chronic neurodevelopmental disorder. Clusters recur (often every few weeks to months, illness-linked) then, characteristically, **seizures tend to attenuate with age**.
- **Remission:** at age ≥11, **~28% seizure-free**; mean seizure "offset" age ~17.6 years (range 11–38); ~14% reach 10-year resolution (Kolc 2020). Seizures frequently ease in adolescence — but **neuropsychiatric burden persists and adult psychiatric risk rises**, so "seizure remission" ≠ "recovery."
- **Critical windows:** the **infantile/early-childhood window** (active neurogenesis + first fever exposures) is when both epileptogenesis and developmental impact are set — the rationale for early diagnosis and cluster-abortive strategies.

---

## 9. Inheritance and Population

- **Inheritance pattern:** **X-linked with an unusual sex-limited expression** — heterozygous females and mosaic males affected; hemizygous ("transmitting") males spared. This is *not* standard X-linked recessive or dominant; model it explicitly. The mechanism is **cellular interference / mosaic-dependent** (§6). → HPO mode-of-inheritance: **HP:0001417** *X-linked inheritance* (with a note on the female-limited, mosaic-dependent expression — this is a genuine curation nuance worth a discussion/knowledge-gap block).
- **Penetrance:** **high in females** — ~**97%** of pathogenic-variant-carrying females are affected (~3% asymptomatic carriers).
- **Expressivity:** **highly variable** (normal cognition + limited seizures → severe DEE), even within families.
- **Anticipation:** not a repeat-expansion disorder; no anticipation.
- **Germline/somatic mosaicism:** central — **affected males are somatic mosaics**; unaffected transmitting fathers pass the variant to affected daughters; **germline/gonadal mosaicism** in a parent can produce recurrence.
- **Founder effects / consanguinity:** not relevant (mostly de novo, private variants; not consanguinity-driven).
- **Carrier frequency:** unaffected hemizygous-male "carriers" transmit; population carrier frequency is not meaningfully tabulated given the de-novo-dominated architecture.
- **Epidemiology:** no precise prevalence figure is established; PCDH19-CE is described as **"one of the most common monogenic epilepsies" and the second most clinically relevant epilepsy gene after *SCN1A***. In **SCN1A-negative Dravet-like females, PCDH19 variants are found in ~25%** (Depienne 2009). For the KB `prevalence` block, the honest fill is a qualitative **`prevalence_class: RARE`** / Orphanet "rare" with `measure_type: UNKNOWN` and notes citing the "second most common epilepsy gene" framing — a hard cases-per-100,000 number isn't well sourced.
- **Demographics:** **overwhelmingly female**; no strong ethnic/geographic clustering (private de novo variants worldwide). Age distribution: pediatric onset, lifelong condition.

---

## 10. Diagnostics

- **Genetic testing is the definitive diagnostic.**
  - **Gene panels** (epilepsy/DEE panels) and **WES/WGS** are first-line, especially in **females with fever-sensitive clustered seizures who are SCN1A-negative** (the classic "looks like Dravet but isn't, and is a girl" scenario). → MAXO **MAXO:0000004**-adjacent; genetic testing action.
  - **Single-gene *PCDH19* sequencing + deletion/duplication analysis** (MLPA/CMA) captures point variants and CNVs (deletions, the reported triplication).
  - **Mosaicism-aware testing** (deep sequencing) is important in **males** — standard sequencing can miss low-VAF somatic variants. → repeat/mosaic detection considerations.
  - Chromosomal microarray for large deletions/duplications.
- **EEG:** interictal often normal early; ictal recordings show **focal onsets** (frontotemporal), sometimes multifocal. No pathognomonic pattern. → electrophysiology (EEG).
- **MRI:** typically **normal or nonspecific** — helps exclude structural mimics rather than confirm.
- **Biomarkers:** **reduced serum/plasma allopregnanolone (allopregnanolone sulfate, Allo-S)** is a mechanistic biomarker and was used to **stratify** patients in the ganaxolone trial — a candidate but not yet a validated clinical diagnostic. → CHEBI: allopregnanolone **CHEBI:50169**.
- **Clinical criteria / differential diagnosis:** no formal consensus criteria; diagnosis is gene-confirmed pattern recognition. **Differentials:** Dravet syndrome (*SCN1A*) — the top mimic; *SCN1B*, *GABRG2*, *STXBP1*, *CDKL5* and other DEEs; febrile seizures plus (GEFS+). The female sex + clustered fever-seizures + SCN1A-negative triad is the key clinical flag.
- **Screening:** not on newborn-screening panels; **cascade/carrier testing** in families (identifying transmitting males and at-risk female relatives) and **prenatal/PGT** for known familial variants are the relevant screening applications.

---

## 11. Outcome / Prognosis

- **Survival/mortality:** generally **not life-limiting** for most; lifespan is broadly preserved. **SUDEP risk** exists as with other DEEs but PCDH19-CE is not characterized by high early mortality. (No robust disease-specific mortality rate published — flag as gap.)
- **Seizure prognosis:** frequently **improves with age** — ~28% seizure-free by ≥11 yr, offset mean ~17.6 yr (§8).
- **Neurodevelopmental/psychiatric prognosis is the real story:** ID (in the ~44% who have it), ASD (~62%), executive dysfunction (~63%) **persist**, and **adult-onset psychiatric illness (including psychotic/schizophrenia-spectrum disorders) is an increasingly recognized late outcome**. So the trajectory is often "seizures fade, the neurodevelopmental/psychiatric load stays."
- **Prognostic factors:** **earlier onset and higher seizure frequency predict worse cognitive/behavioral outcome** (Kolc 2020, robust associations). Genotype–phenotype correlation is otherwise weak.
- **QoL/morbidity:** high family/behavioral burden (§3).

---

## 12. Treatment

There's no cure and no single reliably effective drug — the honest framing from the 2025 systematic review title is literally *"Tough to treat."* Management is **cluster-abortive + broad-spectrum ASM + emerging neurosteroid**.

- **Antiseizure medications (broad-spectrum, polytherapy typical):**
  - **Clobazam / benzodiazepines** — among the more consistently reported effective agents, both for maintenance and acute clusters. → MAXO pharmacotherapy; CHEBI clobazam **CHEBI:31413**.
  - **Bromide (potassium bromide)** — repeatedly noted as **notably effective for PCDH19 clusters** (an old drug finding a niche). → CHEBI bromide **CHEBI:15858**.
  - **Corticosteroids / ACTH** — used for **acute cluster interruption** (case series suggest benefit during severe clusters). → MAXO; CHEBI corticosteroid class.
  - Levetiracetam, valproate, topiramate, stiripentol (single-case benefit), and the ketogenic diet are used with variable/individual response. → **MAXO:0000088** dietary intervention (ketogenic diet).
  - **Sodium-channel blockers** are **less consistently helpful** here than in some epilepsies (and unlike in Dravet, are not strictly contraindicated — an important differential-management point).
- **Neurosteroid / targeted (mechanism-driven):**
  - **Ganaxolone** — synthetic **allopregnanolone analogue**, positive allosteric GABA_A modulator, directly targeting the **allopregnanolone-deficiency** arm. The **VIOLET phase-2 RCT (NCT03865732)** showed a **larger seizure reduction vs placebo (−61.5% vs −24.0%) that did not reach significance (p=0.17)** (Epilepsy Res 2023, **PMID:36870093**). Somnolence was the main AE. → CHEBI ganaxolone; **`therapeutic_modality: SMALL_MOLECULE`**; a good candidate for a `target_mechanisms` link back to the E/I-imbalance / GABA_A node.
- **Acute cluster / rescue:** benzodiazepine rescue protocols; aggressive **fever management** as prophylaxis against triggers.
- **Advanced/experimental:** no approved gene/RNA therapy; the mosaic mechanism makes gene-replacement conceptually tricky (you can't just flood every cell with wild-type without recreating a "uniform" state). Neurosteroid pharmacology remains the most active targeted avenue.
- **Supportive/rehabilitative:** developmental therapies, ASD/behavioral management, psychiatric surveillance into adulthood, **genetic counseling** (**MAXO:0000079**).

Suggested MAXO: **MAXO:0000058**-type pharmacotherapy / **NCIT:C15986** Pharmacotherapy with CHEBI `therapeutic_agent` per the repo's therapeutic-agent pattern; **MAXO:0000088** (ketogenic/dietary); **MAXO:0000079** (genetic counseling); **MAXO:0000950** (supportive care).

---

## 13. Prevention

- **Primary prevention:** none for occurrence (largely de novo). The actionable analog is **trigger avoidance** — proactive **fever/illness management** to reduce clusters (a form of tertiary prevention of seizure events).
- **Secondary prevention:** early genetic diagnosis (panel/WES in SCN1A-negative girls with clustered febrile seizures) to enable prompt cluster-management strategies.
- **Tertiary prevention:** aggressive cluster abortion (benzodiazepines/steroids), developmental and **psychiatric surveillance** to catch adult-onset psychiatric decompensation early.
- **Genetic prevention:** **cascade testing**, prenatal diagnosis and **preimplantation genetic testing** for known familial variants; counseling around **transmitting-male fathers** (all daughters at risk) and **parental gonadal mosaicism** recurrence risk.
- **Genetic counseling** is central (**MAXO:0000079**). No immunization or public-health/environmental prevention applies.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** *Homo sapiens* (**NCBITaxon:9606**) is the disease species. No recognized **naturally occurring** PCDH19 clustering epilepsy in companion animals or wildlife (OMIA has no established natural-disease entry) — this is essentially a human-defined disorder.
- **Orthologs:** *Pcdh19* is **evolutionarily conserved** across vertebrates — mouse (*Pcdh19*, NCBI Gene), rat, and **zebrafish** (*pcdh19*, a well-studied ortholog with roles in neuronal columnar organization and retinal/neural development). Conservation of the adhesion function is high.
- **Comparative biology:** the conserved PCDH19–N-cadherin adhesion and neurodevelopmental roles make cross-species modeling informative; the **mosaic-dependence** is the feature that must be engineered (it doesn't arise "naturally" in uniform-genotype animals).
- **Transmission:** not applicable (non-infectious, non-zoonotic).

---

## 15. Model Organisms

- **Mouse (*Mus musculus*, MGI):** *Pcdh19* knockout / mosaic models are the workhorses. The landmark finding — **abnormal cell sorting** segregating wild-type vs mutant cortical cells in **mosaic (heterozygous female) mice** — recapitulates the human sex-specificity logic (**Pederick et al., Neuron 2018, PMID:29429936** — verify). A **2025 mouse model** shows **hyperthermic (fever) seizure susceptibility and focal loss of parvalbumin interneurons** (biorxiv 688097), directly modeling fever sensitivity + E/I substrate. Conditional/mosaic-inducible designs are needed because uniform nulls (like hemizygous males) don't show the phenotype — the model *must* be mosaic.
- **Rat:** a **focal-mosaic *Pcdh19* rat** reproduces brain developmental abnormalities and behavioral phenotypes (PMC9070467).
- **Zebrafish (*Danio rerio*, ZFIN):** *pcdh19* mutants show neurodevelopmental/columnar-organization defects — good for adhesion/neurogenesis biology.
- **Xenopus:** a *Pcdh19* frog model reproduces epilepsy-like and repetitive behaviors and argues for **mosaicism-independent** contributions (PNAS 2024) — a useful counterweight to a pure cellular-interference view.
- **Cellular / in vitro:** **patient-derived iPSCs**, 2D neural cultures, **cortical/brain organoids** (PMC8268119, PMC11024992, PMC8998847) — these captured **accelerated neurogenesis, asymmetric-division shift, mitotic-spindle/centrosome defects, altered calcium signaling, and abnormal cell sorting in mixed populations**. A **Neurogenin-2-induction iPSC model** (Alaverdian et al., Epileptic Disord 2023, epd2.20065) is a recent addition. These are the natural home for `evidence_source: IN_VITRO`; the mouse/rat/zebrafish/Xenopus data are `MODEL_ORGANISM`.
- **Model characteristics / limitations:** models **recapitulate cell-sorting, neurogenesis, fever-susceptibility, and behavior**, but **no single model reproduces the full human syndrome** (seizure semiology + variable ID/ASD + adult psychiatric risk). The **human-specific neurodevelopmental context** (and the difficulty of matching human XCI mosaic ratios) is a recognized translational gap — a good candidate for a **`HUMAN_MODEL_MISMATCH`** discussion block rather than a plain knowledge gap.

---

## Curation notes / suggested KB scaffolding

- **Identifiers to seed:** `disease_term` → **MONDO:0010246**; causal gene → **hgnc:14270**; OMIM \*300460 / #300088; ORPHA:101039.
- **Module conformance:** strong fit for **`epilepsy_excitation_inhibition_imbalance`** at `#Excitation-Inhibition Imbalance`, with PCDH19-specific upstream nodes (mosaic cellular interference → abnormal cell sorting → allopregnanolone/GABA_A deficit).
- **Inheritance block:** bind **HP:0001417** *X-linked inheritance* but add a `discussions` **KNOWLEDGE_GAP** noting the female-limited, mosaic-dependent, cellular-interference expression that standard X-linked terms don't capture. The germline/gonadal-mosaicism recurrence route is worth an explicit note.
- **Prevalence:** qualitative `RARE` / `measure_type: UNKNOWN`, notes = "second most common monogenic epilepsy gene after SCN1A; ~25% of SCN1A-negative Dravet-like females."
- **Ganaxolone treatment:** clinical-trial block citing **NCT03865732** + `target_mechanisms` to the GABA_A/E-I node; `therapeutic_agent` allopregnanolone-analogue (CHEBI).
- **Human-model-mismatch discussion:** the mosaicism-independent Xenopus findings vs the cell-sorting mouse model make a genuine open question about which mechanism dominates in human disease.

**PMIDs to verify before use** (leads, per project SOP): 32366910 (Kolc phenotype spectrum — fetched, solid), 36870093 (ganaxolone VIOLET — solid), 19752159 (Depienne de novo — from PubMed link), 34201522 (protocadherin structure review — from source, verify), 29429936 (Pederick cell-sorting — verify digits), 18469813 (Dibbens 2008 EFMR discovery — verify), 19282977 (Depienne 2009 PLoS Genet — verify), 18216183 (Scheffer 2008 Brain EFMR — verify), 30542067 (Kolc 2019 meta-analysis — verify), Tan et al. 2015 allopregnanolone (find exact PMID). Run each through `just fetch-reference` and confirm the snippet is an exact abstract substring.

**Sources:**
- [OMIM #300088 (DEE9)](https://omim.org/entry/300088) · [OMIM \*300460 (PCDH19)](https://omim.org/entry/300460) · [Orphanet: PCDH19](https://www.orpha.net/en/disease/gene/PCDH19)
- [MalaCards: DEE9](https://www.malacards.org/card/developmental_and_epileptic_encephalopathy_9)
- [Kolc et al. 2020, standardized phenotype spectrum (PMC7198503)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7198503/) · [Transl Psychiatry version](https://www.nature.com/articles/s41398-020-0803-0)
- [Dissecting PCDH19 in clustering epilepsy — iPSC neurogenesis (PMC8268119)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8268119/) · [Cortical organoid cell-sorting model (PMC11024992)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11024992/) · [2D→3D organoid modeling (PMC8998847)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8998847/)
- [Trivisano et al., pathophysiology & clinical significance, Epilepsy & Behavior 2024](https://www.sciencedirect.com/science/article/abs/pii/S1525505024001112)
- [Ganaxolone VIOLET phase-2 trial (PMID:36870093)](https://pubmed.ncbi.nlm.nih.gov/36870093/) · [Neurosteroids & PCDH19 (IJMS 2021)](https://doi.org/10.3390/ijms22189769)
- ["Tough to treat" systematic review, Seizure 2025](https://www.seizure-journal.com/article/S1059-1311(25)00225-0/fulltext)
- [Mosaicism-independent mechanisms, Xenopus (PNAS 2024)](https://www.pnas.org/doi/10.1073/pnas.2321388121) · [Focal-mosaic rat model (PMC9070467)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9070467/) · [Parvalbumin interneuron mouse preprint 2025](https://www.biorxiv.org/content/10.1101/2025.11.12.688097.full.pdf)
- [Depienne et al., de novo/single-generation EFMR (PMID:19752159)](https://pubmed.ncbi.nlm.nih.gov/19752159/) · [Sporadic IEE resembling Dravet (PMC2633044)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2633044/) · [Mutations/deletions in PCDH19 (PMC3033517)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3033517/)
- [Mosaic males: genotype & VAF (PMC9669318)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9669318/) · [PCDH19 triplication mechanism (PMC11506946)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11506946/) · [Epilepsiome: PCDH19 primer](https://epilepsygenetics.blog/the-epilepsiome/pcdh19-this-is-what-you-need-to-know/)

One honest caveat before you build the entry: I couldn't get OMIM's and MedLink's pages to open directly (they threw 403s at the fetcher), so the OMIM-derived facts here lean on the MONDO record and the search summaries rather than the primary OMIM text — worth a manual glance when you're pinning down the original-reference PMIDs.