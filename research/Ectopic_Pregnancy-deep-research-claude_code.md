---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-03T22:32:02.349967'
end_time: '2026-08-03T22:43:12.348750'
duration_seconds: 670.0
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Ectopic Pregnancy
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-opus-5[1m]
  web_search_requests: 18
  num_turns: 49
  total_cost_usd: 3.912443
  session_id: a927eea8-1a56-4c7e-9075-04fbb6b989e4
  stop_reason: end_turn
citation_count: 19
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Ectopic Pregnancy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Ectopic Pregnancy** covering all of the
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

Research done. Here's the full report.

---

# Ectopic Pregnancy — Comprehensive Disease Characteristics Report

**Prepared:** 2026-08-03 · **Target KB:** dismech (`kb/disorders/Ectopic_Pregnancy.yaml`) · **Category:** Complex

> **Read-me-first caveat (important for the curator):** every ontology CURIE below is tagged either ✅ **verified this session** (I looked it up live in OLS4/EBI) or ⚠️ **candidate — run `just validate-terms` / OAK before committing**. Do not paste the ⚠️ ones in without checking. Same discipline for snippets: everything in a fenced quote block below was pulled verbatim from a real abstract via Europe PMC or PubMed during this session, but you still need `just fetch-reference PMID:X` + `just validate-references` before it lands, because the reference validator normalizes whitespace and my line-wrapping is not the cache's line-wrapping.

---

## 1. Disease Information

### Overview

Ectopic pregnancy (EP) is the implantation and development of a conceptus outside the endometrial cavity of the uterus. Over 98% of extrauterine implantations occur in the fallopian tube. It is the leading cause of maternal death in the first trimester. The core problem is anatomical: an invasive human trophoblast lands in a tissue with no decidual investment and no capacity to accommodate a growing gestation, so it erodes into maternal vessels and through the tubal wall, producing haemorrhage and hypovolaemic shock.

A crucial framing update from the 2026 *Human Reproduction Update* review — ectopic pregnancy is no longer purely an *extra*uterine concept. A second class, **uterine ectopic pregnancy** (caesarean scar, interstitial, cervical, intramural), is defined as implantation outside the endometrial cavity but *within the confines of the uterus*, and is rising fast.

```
"Ectopic pregnancy, defined as the implantation of a developing pregnancy outside of
the endometrial cavity of the uterus, is the leading cause of early-pregnancy maternal
mortality. The majority of ectopic pregnancies implant in a fallopian tube."
```
— Chong KY, de Waard L, Oza M, van Wely M, Jurkovic D, Memtsa M, Woolner A, Mol BW. *Ectopic pregnancy.* **Nat Rev Dis Primers** 2024. **PMID:39668167**. Evidence source: `HUMAN_CLINICAL` (narrative review).

```
"An ectopic pregnancy is a pregnancy which occurs outside of the uterine cavity, and
over 98% implant in the Fallopian tube. Tubal ectopic pregnancy remains the most common
cause of maternal mortality in the first trimester of pregnancy."
```
— Shaw JLV, Dey SK, Critchley HOD, Horne AW. *Current knowledge of the aetiology of human tubal ectopic pregnancy.* **Hum Reprod Update** 2010;16(4):432–44. **PMID:20071358**. Evidence source: `HUMAN_CLINICAL`.

### Identifiers

| Resource | Identifier | Label | Status |
|---|---|---|---|
| MONDO | `MONDO:0000755` | ectopic pregnancy | ✅ verified (OLS4) |
| MONDO | `MONDO:0043762` | tubal pregnancy | ✅ verified |
| MONDO | `MONDO:0043759` | abdominal ectopic pregnancy | ✅ verified |
| MONDO | `MONDO:0044098` | ovarian ectopic pregnancy | ✅ verified |
| MONDO | `MONDO:0044101` | pregnancy, cornual | ✅ verified |
| HPO | `HP:0031456` | Ectopic pregnancy | ✅ verified (OLS4) |
| ICD-10-CM | `O00` (O00.0 abdominal, O00.1 tubal, O00.2 ovarian, O00.8 other, O00.9 unspecified) | Ectopic pregnancy | ⚠️ high confidence, standard |
| ICD-11 MMS | `JA01` (JA01.0 abdominal, JA01.1 tubal) | Ectopic pregnancy | ⚠️ verify in ICD-11 browser — a competing `JA00` reading appeared in search; `JA00` is spontaneous abortion |
| MeSH | `D011271` Pregnancy, Ectopic; `D011274` Pregnancy, Tubal | — | ⚠️ verify |
| Orphanet | Not a rare disease — **no ORPHA entry expected**. Do not fabricate one. | | |
| OMIM | **Not applicable.** No Mendelian OMIM entry; this is a multifactorial complication of pregnancy. | | |
| GWAS Catalog | `GCST90272883` (Pujol Gualdo 2023 meta-analysis summary statistics) | ✅ stated in the paper's own abstract | |

**Note on ORPHA/OMIM:** the dismech instinct is to reach for an ORPHA record. Resist here — EP is common (1–2% of pregnancies), so it falls outside Orphanet's scope. Cite ACOG, NICE, and the primary literature instead.

### Synonyms

Extrauterine pregnancy; extra-uterine gestation; tubal pregnancy (site-specific); eccyesis (archaic); "EP". Site-qualified variants: ampullary, isthmic, fimbrial, interstitial (cornual), ovarian, abdominal, cervical, caesarean-scar (CSP), intramural, heterotopic (coexistent intra- and extrauterine).

**Terminology caution for curators:** "cornual pregnancy" and "interstitial pregnancy" are used interchangeably in older literature but are not synonymous in modern classification — cornual properly refers to implantation in the horn of a bicornuate/septate uterus, interstitial to the intramyometrial segment of the tube. The 2026 review explicitly calls out that new classification and terminology were developed to reduce misdiagnosis.

### Data provenance character

Both. Population-level incidence and mortality come from **aggregate registry sources** (national birth/death certificates, FinnGen/Estonian Biobank ICD-10 O00 register extraction, Orphanet-style epidemiology is absent). Mechanistic and per-phenotype data come from **individual-patient tissue studies** (fallopian tube biopsies at hysterectomy or salpingectomy) and **EHR/clinical cohorts**. The GWAS specifically defines cases by ICD-10 registry code:

```
"We identified ectopic pregnancy cases from national registers by ICD (International
Classification of Disease) codes (ICD-10 O00), and all remaining women were considered
controls."
```
— Pujol Gualdo N, Mägi R, Laisk T. **Hum Reprod** 2023. **PMID:37877466**.

---

## 2. Etiology

### 2.1 Causal framework — the two-hit model

The field has converged on a **dual-lesion** model, which is exactly the shape dismech wants for a pathograph. It is not one mechanism; it is *retention* plus *receptivity*:

```
"tubal ectopic pregnancy is caused by a combination of retention of the embryo within
the Fallopian tube due to impaired embryo-tubal transport and alterations in the tubal
environment allowing early implantation to occur"
```
— Shaw JLV et al. **Hum Reprod Update** 2010. **PMID:20071358**. Evidence source: `HUMAN_CLINICAL`.

That sentence is the single best anchor for a top-level `pathophysiology` node pair:
1. **Impaired embryo-tubal transport** (the embryo doesn't leave) — ciliary + smooth-muscle failure.
2. **Aberrant tubal receptivity** (the tube lets it in) — the tube adopts a pro-implantation microenvironment it should never have.

Neither alone is sufficient. This is worth curating as two upstream nodes converging on a shared downstream "Tubal Implantation" node.

### 2.2 Environmental / acquired risk factors (dominant)

The canonical quantitative source is the Auvergne population-based case-control register (803 cases, 1,683 controls):

- **Prior pelvic infection** — adjusted OR **3.4** (95% CI 2.4–5.0)
- **Heavy smoking (>20 cig/day vs never)** — adjusted OR **3.9** (95% CI 2.6–5.9); dose-dependent
- **Prior medical (medication) induced abortion** — adjusted OR **2.8** (95% CI 1.1–7.2); *no* association with surgical abortion (OR 1.1, 0.8–1.6)
- Age (independent effect), prior spontaneous abortion, infertility history, prior IUD use
- **Total attributable risk of all investigated factors = 0.76**

— Bouyer J et al. *Risk Factors for Ectopic Pregnancy: A Comprehensive Analysis Based on a Large Case-Control, Population-based Study in France.* **Am J Epidemiol** 2003;157(3):185–194. ⚠️ **Fetch the PMID and re-verify these numbers against the abstract before curating** — I read them from secondary sources and the Ovid/HAL full text, not the PubMed abstract itself.

Additional established risk factors (broad consensus across ACOG PB 193 / NICE / Nat Rev Dis Primers):

| Risk factor | Direction / magnitude | Notes |
|---|---|---|
| Prior ectopic pregnancy | 7–13× increased odds; recurrence 10–20% | Strongest single clinical predictor |
| Prior tubal surgery (incl. sterilization, reversal) | Strongly increased | Sterilization failure pregnancies are disproportionately ectopic |
| *Chlamydia trachomatis* infection / PID | OR ~3.4 | Mechanism established at molecular level (§6) |
| Salpingitis isthmica nodosa | Increased | `MONDO:0003616` ✅ verified |
| Cigarette smoking | OR up to 3.9, dose-dependent | Mechanism established (§6) |
| IVF / ART | ~2.5–5× vs natural conception; 1.4–5.4% of ART cycles | See §2.4 |
| Tubal factor infertility | Strong, and compounds with prior EP | PMID:32143813 "double whammy" cohort, n=2,892 |
| Endometriosis | Increased in ART cohorts | |
| IUD in situ | *Relative* increase, *absolute* decrease | See §2.5 — this one is routinely miscurated |
| Advanced maternal age (>35) | Increased | Also 3.5× higher EP mortality vs <25 |
| Prior caesarean section | Specific driver of caesarean-scar EP | The fastest-rising subtype |
| DES exposure in utero | Historical; tubal anomalies | Cohort now largely post-reproductive |

### 2.3 Infectious etiology

*Chlamydia trachomatis* (⚠️ `NCBITaxon:813` — verify) is the dominant infectious cause and the only one with a worked-out molecular chain (§6.1). *Neisseria gonorrhoeae* (⚠️ `NCBITaxon:485` — verify) contributes through the same PID → salpingitis → tubal damage route; recent work implicates IL-17C as a driver of gonococcal fallopian tube damage (Nature Communications 2024, PMC11069574 — ⚠️ fetch PMID).

### 2.4 ART as an iatrogenic etiology

EP incidence after IVF is elevated roughly **2.5–5-fold** over natural conception, with reported per-cycle rates of **1.4–5.4%**. Large series report total EP rates around **1.8–2.1%** of IVF pregnancies. Fresh vs frozen transfer shows **no consistent difference** in the largest contemporary retrospective series (2.16% fresh vs 2.07% frozen, n=16,048; PMID:35743455 — ⚠️ verify). Independent ART-specific risk factors: tubal factor infertility, endometriosis, and diminished ovarian reserve (5.51% vs 2.99%).

⚠️ **Curator warning:** the literature here is genuinely conflicting (one older series reported 7.6% after frozen-thawed vs 2.4% fresh). Curate this as an area of uncertainty, ideally with a `KNOWLEDGE_GAP` discussion, rather than asserting a fresh/frozen direction.

### 2.5 Protective factors

- **Any effective contraception** — the dominant protective factor. This is the classic epidemiological trap: **an IUD raises the *proportion* of pregnancies that are ectopic while lowering the *absolute* risk of ectopic pregnancy**, because it prevents intrauterine pregnancy far more efficiently than tubal. Curate this explicitly; conflating the two is a common error.
- **Smoking cessation** — dose-response reversal implied by the cotinine/PROKR1 mechanism (§6.2), though no RCT.
- **Chlamydia screening programmes** — population-level primary prevention (see §13).
- **Rapid conception after a prior EP** — an interpregnancy interval of ≤3 months was associated with *lower* recurrence odds than 6–18 months (~4× difference) in a UK tertiary cohort (⚠️ Dooley et al., *Ultrasound Obstet Gynecol* 2025, PMC12209686 — verify PMID; single-centre, retrospective, plausibly confounded).
- **Genetic protective alleles:** none established. Do not invent any.

### 2.6 Gene–environment interaction

The GWAS provides the only rigorous handle, and it is a **genetic correlation with smoking**:

```
"We also characterize the phenotypic and genetic correlations with other phenotypes,
identifying a genetic correlation with smoking and diseases of the (genito)urinary and
gastrointestinal system, and phenotypic correlations with various reproductive health
diagnoses, reflecting the previously known epidemiological associations."
```
— Pujol Gualdo N et al. **PMID:37877466**.

Mechanistically, the strongest G×E candidate is the **CNR1/endocannabinoid axis**: exogenous cannabinoid exposure phenocopies genetic CB1 loss in mice (§15), and reduced CB1 expression is seen in human EP tissue with a *suggestive but statistically non-significant* CNR1 polymorphism signal (§4.2). This is a genuine, curatable hypothesis — but it must be curated as `EMERGING`, not established.

---

## 3. Phenotypes

### 3.1 Presenting symptoms and signs

⚠️ **Frequency-evidence discipline:** per `docs/frequency-evidence-guidelines.md`, the percentages below come from single-centre case series and secondary clinical references, **not** from a pooled meta-analysis. Several are internally inconsistent across sources (abdominal pain reported as 82.9%, 97%, and 98.6% in different series). My recommendation: curate the *associations* with confidence and **omit `frequency:` for most, or use only the coarse `VERY_FREQUENT`/`FREQUENT` bands** with the specific series cited. Do not curate a precise percentage from a secondary source.

| Phenotype | Category | Reported frequency | HPO suggestion |
|---|---|---|---|
| Abdominal / pelvic pain | Symptom | 82.9–98.6% (series-dependent); up to 9% report *no* pain | `HP:0002027` Abdominal pain ⚠️ |
| Amenorrhoea / missed period | Symptom | 63.4–74.1% | `HP:0000141` Amenorrhea ⚠️ |
| Abnormal vaginal bleeding | Sign | 40–56.4% | ⚠️ needs OAK lookup — "Vaginal hemorrhage"/"Metrorrhagia"; do not guess an ID |
| Adnexal tenderness | Sign | present in ~64% (36% lack it) | ⚠️ may have no HP term; consider free-text `preferred_term` |
| Adnexal mass | Sign | ~50% palpable | ⚠️ lookup needed |
| Abdominal tenderness | Sign | ~75% | ⚠️ lookup needed |
| Shoulder-tip pain (diaphragmatic irritation from haemoperitoneum) | Symptom | Occasional; high specificity for rupture | ⚠️ lookup needed |
| Syncope / presyncope | Symptom | Occasional; rupture marker | `HP:0001279` Syncope ⚠️ |
| Tachycardia | Sign | Rupture/shock | `HP:0001649` Tachycardia ⚠️ |
| Hypotension | Sign | Rupture/shock | `HP:0002615` Hypotension ⚠️ |
| Anaemia | Lab | Post-haemorrhage | `HP:0001903` Anemia ⚠️ |
| Haemoperitoneum | Imaging/operative | Defines rupture | ⚠️ lookup needed — likely exists in HPO, verify |
| Hypovolaemic shock | Sign | The lethal endpoint | ⚠️ lookup needed |
| Suboptimally rising serum hCG | Lab | Near-universal in viable-EP diagnosis | ⚠️ likely no HP term — curate as `biochemical` with LOINC |
| Infertility (subsequent) | Long-term outcome | See §11 | `HP:0000789` Infertility ⚠️ |

**The classic triad** (pain + amenorrhoea + vaginal bleeding) is present in only ~50% of patients. This is diagnostically load-bearing and should be curated as an explicit note, because it drives the diagnostic algorithm's reliance on hCG + ultrasound over history.

### 3.2 Onset, severity, progression

- **Age of onset:** reproductive age only, ~15–45 y. Not congenital, not paediatric, not geriatric. There is no "age of onset" in the Mendelian sense — onset is **gestational**, typically **6–8 weeks' gestation** for tubal EP, later (up to 10–16 weeks or beyond) for interstitial and caesarean-scar EP because those sites accommodate more growth before failing.
- **Severity:** highly variable — bimodal. A spectrum runs from a small failing EP destined to resolve with no intervention, through to catastrophic rupture with shock. The 2026 review flags that modern ultrasound now detects the benign tail that was previously invisible:

```
"Improvements in the organization and provision of care for women presenting with early
pregnancy complications, in conjunction with better quality and wider use of ultrasound
imaging, have resulted in an increased ability to detect small failing ectopic
pregnancies, which were impossible to diagnose in the past. Many of these pregnancies are
destined to resolve spontaneously without the need for any intervention."
```
— Farren J, Al Wattar BH, Jurkovic D. **Hum Reprod Update** 2026. **PMID:41061761**.

- **Progression:** acute-to-subacute, **self-limited in one direction or the other** — it is not a chronic disease. It resolves (spontaneous regression / tubal abortion), is treated, or ruptures. Rupture is the acute catastrophic transition.
- **Quality of life:** the psychological dimension is repeatedly under-curated and both major reviews call it out explicitly:

```
"After ectopic pregnancy, patients may experience ongoing morbidity, including chronic
pain, infertility and psychological distress. Assessment of ectopic pregnancy should focus
on prompt diagnosis based on clinical and investigative findings but should also reflect a
patient-centred approach with acknowledgement of potential psychological distress
associated with pregnancy loss and reduced future fertility."
```
— Chong KY et al. **Nat Rev Dis Primers** 2024. **PMID:39668167**.

⚠️ No EQ-5D or SF-36 utility values for EP were located in this search. Do not fabricate them. If you need them, a targeted search of the early-pregnancy-loss PROM literature is the next step.

---

## 4. Genetic / Molecular Information

**Framing for dismech:** this is a **complex/multifactorial** trait with **low but non-zero SNP heritability**. There are **no causal genes**, **no pathogenic variants**, **no ACMG-classifiable variants**, **no chromosomal abnormalities**, and **no clinical genetic testing**. Curating a `genetic:` block with `relationship_type: CAUSAL` would be wrong. Use `SUSCEPTIBILITY`.

### 4.1 GWAS — the only rigorous genetic evidence

First and, as of this writing, only large-scale GWAS meta-analysis: **7,070 cases / 248,810 controls** (Estonian Biobank + FinnGen).

```
"We identified two genome-wide significant loci on chromosomes 1 (rs4971091,
P = 5.32×10-9) and 10 (rs11598956, P = 2.41×10-8) potentially associated with ectopic
pregnancy. Follow-up analyses propose MUC1, which codes for an epithelial glycoprotein
with an important role in barrier function, as the most likely candidate gene for the
association on chromosome 1."
```
— Pujol Gualdo N, Mägi R, Laisk T. **Hum Reprod** 2023;38(12):2516. **PMID:37877466**. Evidence source: `HUMAN_CLINICAL`.

- **Candidate gene:** **MUC1** (mucin 1, cell surface associated) — ⚠️ `hgnc:7508`, **verify**. Biologically coherent: MUC1 is an anti-adhesive apical glycoprotein whose *removal* from the endometrial surface is part of normal receptivity. A variant altering MUC1 barrier function in tubal epithelium plausibly permits ectopic attachment. Suggest `GO:0007566` embryo implantation ⚠️ and a cell-surface/barrier GO CC term.
- **Chromosome 10 locus (rs11598956):** no confidently assigned gene. Do not assign one.
- **Heritability:** observed SNP h² = 0.0106 (SE 0.0019) → **liability-scale SNP heritability 7.03% (SE 0.013)** ⚠️ (these figures come from the paper body/preprint, not the abstract — verify before quoting).
- **Familial aggregation:** daughters of mothers with EP reportedly carry ~50% higher risk ⚠️ — **secondary-source claim, chase the primary reference before curating.**
- **Ancestry limitation, in the authors' own words:** *"the findings are based on European-based ancestry populations, with limited data on other populations, and we only captured maternal genomes."* Curate this as a stated limitation.

### 4.2 CNR1 — a candidate that did not reach significance

Horne et al. genotyped the 1359G/A (**rs1049353**) CNR1 polymorphism in EP vs intrauterine pregnancy:

```
"Although of 1359G/A (rs1049353) polymorphisms of CNR1 gene suggests differential
distribution of genotypes between the small, available cohorts of women with EP and those
with IUP, results were not statistically significant."
```
— Horne AW, Phillips JA 3rd, Kane N, Lourenco PC, McDonald SE, Williams ARW, Simon C, Dey SK, Critchley HOD. *CB1 expression is attenuated in Fallopian tube and decidua of women with ectopic pregnancy.* **PLoS One** 2008. **PMID:19093002**.

**Curate this as a negative/underpowered result**, explicitly. It is a good candidate for `supports: NO_EVIDENCE` or `PARTIAL` with an explanation noting the sample size. The authors themselves ask for replication in a larger pool. `CNR1` ⚠️ `hgnc:2159` — verify.

### 4.3 Modifier genes, epigenetics, chromosomal abnormalities

- **Modifier genes:** none established.
- **Epigenetics:** ⚠️ **No robust EP-specific methylation or chromatin dataset was located in this search.** Scattered small studies exist on endometrial methylation in EP but I did not verify any. **Report as a knowledge gap** rather than curating weak claims.
- **Chromosomal abnormalities:** karyotypic abnormality rates in ectopic conceptuses are broadly comparable to intrauterine early loss; there is no EP-specific aneuploidy signature. Do **not** curate an aneuploidy mechanism.
- **Somatic vs germline:** all genetic signal is **maternal germline susceptibility**. There is no somatic component (this is not neoplasia — though note gestational trophoblastic disease can rarely arise at an ectopic site; PMC11290199 tubal ectopic molar pregnancy).

---

## 5. Environmental Information

### 5.1 Chemical / toxicological

- **Cigarette smoke, specifically nicotine and its metabolite cotinine** — the best-characterized environmental exposure with a defined receptor-level mechanism (§6.2). ⚠️ CHEBI: nicotine `CHEBI:17688`, cotinine `CHEBI:68641` — **verify both.**
- **Exogenous cannabinoids** — mechanistically implicated via CB1 (§6.3 and §15). Wild-type mice treated with **methanandamide** phenocopy the Cnr1-null transport defect. Human epidemiological confirmation is **not** established; curate as `MODEL_ORGANISM` evidence with an explicit `HUMAN_MODEL_MISMATCH` or `KNOWLEDGE_GAP` discussion, since cannabis-use data in EP cohorts is thin. This is exactly the case the `HUMAN_MODEL_MISMATCH` kind was designed for.
- **Diethylstilbestrol (DES)** — historical in-utero exposure causing tubal structural anomalies.

### 5.2 Lifestyle

Smoking (dose-dependent, the dominant modifiable factor). Douching has been associated in some series (plausibly a PID-mediated effect). Alcohol, diet, and exercise have **no established association** — do not curate one.

### 5.3 Infectious agents

*Chlamydia trachomatis* is the flagship. See §6.1 for the mechanism. *Neisseria gonorrhoeae* via the same PID pathway. Both act as **triggers of the "impaired transport" arm and the "aberrant receptivity" arm simultaneously**, which is unusual and worth noting in the pathograph — Chlamydia both destroys cilia and upregulates PROKR2.

---

## 6. Mechanism / Pathophysiology

This is the richest section and the one dismech should invest in. I'll lay it out as a causal chain suitable for direct translation into `pathophysiology` nodes with `downstream` edges.

### Proposed pathograph skeleton

```
[Chlamydia infection] ─┐
[Smoking / cotinine]  ─┤
[Tubal surgery/damage]─┼──> [Impaired Embryo-Tubal Transport] ──┐
[CB1 signalling loss] ─┘         (ciliary + smooth muscle)      │
                                                                 ├──> [Embryo Retention
[Chlamydia → TLR2/NFkB → PROKR2] ─┐                              │      in Fallopian Tube]
[Cotinine → nAChRα7 → PROKR1]     ─┼─> [Aberrant Tubal          ─┘            │
[MUC1 barrier variant]            ─┘    Receptivity]                          v
                                                          [Tubal Implantation without Decidua]
                                                                              │
                                                                              v
                                                       [Unrestrained Trophoblast Invasion
                                                        of Tubal Muscularis]  ← CSF1/CSF1R
                                                                              │
                                                                              v
                                              [Tubal Wall Erosion & Vascular Disruption]
                                                                              │
                                                          ┌───────────────────┴──────────┐
                                                          v                              v
                                              [Tubal Rupture]              [Tubal Abortion /
                                                          │                 Spontaneous Resolution]
                                                          v
                                       [Haemoperitoneum → Hypovolaemic Shock → Maternal Death]
```

### 6.1 Chlamydia → TLR2 → NF-κB → PROKR2 (the receptivity arm)

The single cleanest molecular chain in the whole field, and it is fully quotable:

```
"Chlamydia trachomatis and smoking are major risk factors for tubal ectopic pregnancy
(EP), but the underlying mechanisms of these associations are not completely understood.
Fallopian tube (FT) from women with EP exhibit altered expression of prokineticin
receptors 1 and 2 (PROKR1 and PROKR2); smoking increases FT PROKR1, resulting in a
microenvironment predisposed to EP."
```

```
"Transfection of OE-E6/E7 cells with dominant-negative TLR2 or IκBα abrogated the
C. trachomatis-induced PROKR2 expression. We propose that ligation of tubal TLR2 and
activation of NFκB by C. trachomatis leads to increased tubal PROKR2, thereby predisposing
the tubal microenvironment to ectopic implantation."
```
— Shaw JLV, Wills GS, Lee K-F, Horner PJ, McClure MO, Abrahams VM, Wheelhouse N, Jabbour HN, Critchley HOD, Entrican G, Horne AW. **Am J Pathol** 2011;178(1):253–260. **PMID:21224062**. Evidence source: `IN_VITRO` (organ culture + OE-E6/E7 oviductal epithelial cell line + dominant-negative transfection), with a `HUMAN_CLINICAL` component (FT tissue from women with serological evidence of past infection).

⚠️ **Split the evidence items.** The FT-tissue comparison (`P < 0.05`, past-infection vs not) is human observational; the explant/cell-line infection and the dominant-negative rescue are `IN_VITRO`. Per CLAUDE.md, one `evidence_source` per item.

Genes: `PROKR2` ⚠️, `PROKR1` ⚠️, `TLR2` ⚠️, `NFKBIA` ⚠️, `PROK1`/`PROK2` ⚠️ — all need HGNC lookup (lowercase `hgnc:` prefix per repo convention).
GO: `GO:0034134` toll-like receptor 2 signaling pathway ⚠️; NF-κB signalling ⚠️ (the GO label has changed over time — look it up, don't guess); `GO:0006954` inflammatory response ⚠️; `GO:0001525` angiogenesis ⚠️.

### 6.2 Smoking → cotinine → nAChRα7 → PROKR1 (the second receptivity arm)

The exact structural parallel to the Chlamydia arm, from the same group — which is why these two risk factors converge on one node:

```
"In EP, embryo retention within the Fallopian tube (FT) is thought to be due to impaired
smooth muscle contractility (SMC) and alterations in the tubal microenvironment. Smoking is
a major risk factor for EP. FTs from women with EP exhibit altered prokineticin receptor-1
(PROKR1) expression, the receptor for prokineticins (PROK). PROK1 is angiogenic, regulates
SMC, and is involved in intrauterine implantation."
```

```
"PROKR1 transcription was higher in FTs from smokers (P<0.01). nAChRα-7 expression was
demonstrated in FT epithelium. Cotinine treatment of FT explants and OE-E6/E7 cells
increased PROKR1 expression (P<0.05), which was negated by cotreatment with nAChRα-7
antagonist. Smoking targets human FTs via nAChRα-7 to increase tubal PROKR1, leading to
alterations in the tubal microenvironment that could predispose to EP."
```
— Shaw JL, Oliver E, Lee KF, Entrican G, Jabbour HN, Critchley HO, Horne AW. *Cotinine exposure increases Fallopian tube PROKR1 expression via nicotinic AChRalpha-7: a potential mechanism explaining the link between smoking and tubal ectopic pregnancy.* **Am J Pathol** 2010. **PMID:20864676**. Evidence source: `IN_VITRO` (explants + cell line + receptor antagonist rescue) plus `HUMAN_CLINICAL` (smoker vs non-smoker FT, n=21).

Gene: `CHRNA7` ⚠️ (nicotinic acetylcholine receptor α7).

**Nice mechanistic detail for the KB:** PROK1 signalling is *both* angiogenic *and* a regulator of smooth-muscle contractility — so the prokineticin axis touches both arms of the two-hit model at once, not just receptivity. Worth an explicit note.

### 6.3 Endocannabinoid tone → oviductal transport (the retention arm)

The mouse genetics here are the strongest causal evidence in the entire EP mechanism literature — but they are mouse.

```
"Ectopic pregnancy is a major reproductive health issue. Although other underlying causes
remain largely unknown, one cause of ectopic pregnancy is embryo retention in the fallopian
tube. Here we show that genetic or pharmacologic silencing of cannabinoid receptor CB1
causes retention of a large number of embryos in the mouse oviduct, eventually leading to
pregnancy failure. This is reversed by isoproterenol, a beta-adrenergic receptor agonist.
Impaired oviductal embryo transport is also observed in wild-type mice treated with
methanandamide. Collectively, the results suggest that aberrant cannabinoid signaling
impedes coordinated oviductal smooth muscle contraction and relaxation crucial to normal
oviductal embryo transport. Colocalization of CB1 and beta2-adrenergic receptors in the
oviduct muscularis implies that a basal endocannabinoid tone in collaboration with
adrenergic receptors coordinates oviductal motility for normal journey of embryos into the
uterus."
```
— Wang H, Guo Y, Wang D, Kingsley PJ, Marnett LJ, Das SK, DuBois RN, Dey SK. *Aberrant cannabinoid signaling impairs oviductal transport of embryos.* **Nat Med** 2004;10(10):1074–80. **PMID:15378054**. Evidence source: `MODEL_ORGANISM`.

The human counterpart (correlative, not causal):

```
"In normal FT, CB1 mRNA was higher in luteal compared to follicular-phase (p<0.05). CB1
protein was located in smooth muscle of the wall and of endothelial vessels, and luminal
epithelium of FT. In FT from women with EP, CB1 mRNA expression was low. CB1 mRNA
expression was also significantly lower (p<0.05) in endometrium of women with EP compared
to intrauterine pregnancies (IUP)."
```
— Horne AW et al. **PLoS One** 2008. **PMID:19093002**. Evidence source: `HUMAN_CLINICAL`.

⚠️ **Critical curation note:** mice **do not get tubal ectopic pregnancy** — Cnr1-null mice get oviductal retention and *pregnancy failure*, not tubal implantation. The mouse model captures the retention arm and not the implantation arm. This is a textbook `HUMAN_MODEL_MISMATCH` discussion: evidence exists in a model, but the model cannot produce the human endpoint. Do **not** let `MODEL_ORGANISM` evidence stand alone for a human phenotype.

Genes: `CNR1` ⚠️, `ADRB2` ⚠️. GO: `GO:0006939` smooth muscle contraction ⚠️; `GO:0007186` G protein-coupled receptor signaling pathway ⚠️. CHEBI: anandamide ⚠️, methanandamide ⚠️, isoprenaline ⚠️.

### 6.4 Ciliary destruction — the tissue-damage arm

The IL-1-initiated destruction of ciliated fallopian tube epithelium is the mechanistic bridge from infection to permanent transport failure:

```
"Chlamydia trachomatis infection is associated with severe Fallopian tube tissue damage
leading to tubal infertility and ectopic pregnancy. To explore the molecular mechanisms
behind infection an ex vivo model was established from human Fallopian tubes and examined
by scanning electron microscopy and immunohistochemistry. Extensive tissue destruction
affecting especially ciliated cells was observed in C. trachomatis infected human Fallopian
tube organ culture. Interleukin-1 (IL-1) produced by epithelial cells was detected after
infection. Addition of IL-1 receptor antagonist (IL-1RA) completely eliminated tissue
destruction induced by C. trachomatis."
```
— Hvid M, Baczynska A, Deleuran B, Fedder J, Knudsen HJ, Christiansen G, Birkelund S. *Interleukin-1 is the initiator of Fallopian tube destruction during Chlamydia trachomatis infection.* **Cell Microbiol** 2007. **PMID:17614966**. Evidence source: `IN_VITRO` (human FT ex vivo organ culture — note the authors emphasize leukocytes are *absent*, which is what makes the IL-1-is-primary claim work).

Additional: IL-1 → IL-8 via p38 MAPK → neutrophil recruitment in vivo. Genes: `IL1B` ⚠️, `IL1RN` ⚠️, `IL8`/`CXCL8` ⚠️, `MAPK14` ⚠️, `IL10` ⚠️.
GO: `GO:0003341` cilium movement ⚠️; `GO:0006954` inflammatory response ⚠️.
CL: ciliated epithelial cell of the fallopian tube ⚠️ — **look this up properly**, there is a specific CL term but I will not guess the ID.

### 6.5 Unrestrained trophoblast invasion — the rupture arm

This is the step that makes EP lethal rather than merely a failed pregnancy. **In the absence of decidua, there is nothing to restrain trophoblast.** The histopathology is described as resembling placenta accreta: chorionic villi in direct contact with the muscularis, with implantation-site trophoblast continuing to proliferate through the wall.

Site matters: ampullary pregnancies are more often intraluminal with preserved muscularis (~52% intraluminal, of which ~85% preserve muscularis), whereas isthmic pregnancies invade extraluminally with earlier and deeper wall penetration — consistent with isthmic EP presenting earlier and rupturing more readily. ⚠️ These figures are from PMC12041030 and the classic *Am J Obstet Gynecol* 1988 histopathologic study (S0002-9378(88)80176-5) — **fetch both PMIDs and verify.**

The contemporary single-cell mechanism for rupture specifically:

```
"Tubal ectopic pregnancy (TEP) occurs when an embryo aberrantly implants in the fallopian
tube, leading to abortive or ruptured tubal ectopic pregnancy (AEP or REP). Poor outcomes
of REP include maternal infertility or mortality. Current studies on the prevention and
treatment of ruptured tubal ectopic pregnancy (REP) are unfortunately hampered by a lack of
the cell spectrum and cell-cell communications in the maternal-foetal interface. Here, we
investigate the mechanisms of tubal rupture through single-cell transcriptome profiling of
the fallopian tube-trophoblast interface in REP, AEP and intrauterine pregnancy patients.
In REP, extravillous trophoblast (EVTs) cells form a dominant cell population, displaying
aggressive invasion and proliferation, with robust differentiation into three subsets. Cell
communication analysis identified colony-stimulating factor 1 (CSF1), overexpressed by
fallopian tube secretory epithelial cells in REP, with CSF1R on EVTs and macrophages, as a
ligand/receptor pair that stimulates EVT invasion and macrophage accumulation. CSF1+
secretory epithelial cells stimulate EVTs migration and invasion, leading to a tubal
rupture in REP."
```
— Zhao X, Yan L, Ji S, Zhang Y, Ha L, He C, Tian Y, Chen L, Zhu Q, Li M, Zhang J. *Colony-stimulating factor 1 positive (CSF1+) secretory epithelial cells induce excessive trophoblast invasion in tubal pregnancy rupture.* **Cell Prolif** 2023. **PMID:36721079**. Evidence source: `HUMAN_CLINICAL` (patient tissue scRNA-seq) — arguably split, since the migration/invasion stimulation experiments are `IN_VITRO`.

**This is the single most curatable modern mechanism paper for the rupture node.** It gives a named ligand-receptor pair (CSF1/CSF1R ⚠️ `hgnc:` lookup needed), a named cell type (fallopian tube secretory epithelial cell), and a discriminating comparison (ruptured vs abortive vs intrauterine).

### 6.6 EGFR — the therapeutic-target hypothesis that failed

Trophoblast proliferation is EGFR-dependent, which motivated the gefitinib hypothesis. The GEM3 trial refuted it clinically (§12). This is a beautiful `supports: REFUTE` evidence item and dismech should curate it as such — a mechanistically sound target that did not translate.
Gene: `EGFR` ⚠️. GO: `GO:0007173` epidermal growth factor receptor signaling pathway ⚠️.

### 6.7 Metabolic / proteomic / other omics

- **Metabolomics / lipidomics:** ⚠️ **nothing robust located.** Report as a gap.
- **Proteomics:** no validated EP proteomic signature located.
- **Transcriptomics:** covered above (scRNA-seq). Additionally a fallopian tube epithelium single-cell atlas identifies an `OVGP1+` progenitor population with bidirectional secretory/ciliated differentiation trajectories and reports gene-network associations with ectopic pregnancy (bioRxiv 2024.12.20.629653) — ⚠️ **preprint, not peer-reviewed at time of search. Do not cite as established.** A spatial atlas of human ectopic pregnancy integrating scRNA-seq and spatial transcriptomics is also in development (⚠️ verify publication status).
- **Immune microenvironment (scRNA-seq, 2025):** 28 clusters / 13 major cell types at implantation vs non-implantation sites; T/NK cells and macrophages predominant; CD4+ T cells at implantation sites showing dual pro-inflammatory and tolerogenic function; CD8+ subsets with impaired function and reduced immune surveillance. ⚠️ *BMC Pregnancy Childbirth* 2025 (s12884-025-08232-5) — **fetch PMID and verify before curating; this is recent and I have not read the abstract directly.**
- **Functional genomics screens (CRISPR/RNAi):** none in this disease. Not applicable.

---

## 7. Anatomical Structures Affected

### Organ level

| Structure | Role | UBERON |
|---|---|---|
| Fallopian tube (uterine tube / oviduct) | **Primary site — >98%** | `UBERON:0003889` ⚠️ verify |
| — ampulla | Most common tubal segment (~70% of tubal EP) | ⚠️ lookup |
| — isthmus | Deeper/earlier invasion, earlier rupture | ⚠️ lookup |
| — fimbria / infundibulum | Less common | ⚠️ lookup |
| — interstitial (intramural) segment | Rare, late-rupturing, high mortality | ⚠️ lookup |
| Uterus (myometrium — caesarean scar, intramural) | Rising "uterine ectopic" class | `UBERON:0000995` uterus ⚠️ |
| Uterine cervix | Cervical EP, ~0.5% | ⚠️ lookup |
| Ovary | Ovarian EP, ~1.6% | `UBERON:0000992` ⚠️ |
| Peritoneal cavity / abdominal viscera | Abdominal EP, ~0.6% | ⚠️ lookup |
| Endometrium | **Secondary** — Arias-Stella reaction, decidual cast, *no* villi | `UBERON:0001295` ⚠️ |

**Site distribution** (large Chinese series, 2012–2019): tubal **84.70%**, caesarean scar **8.63%**, cornual **2.68%**, ovarian **1.56%**, abdominal **0.61%**, cervical **0.49%**, heterotopic **0.43%**. The CSP fraction rose from **5.74%** (2012–2015) to **11.81%** (2016–2019). ⚠️ *Reprod Health* 2022, PMC9392275 — **fetch PMID and verify.** Note this cohort is from a high-caesarean-rate population, so the CSP share is not globally generalizable; the tubal share here (84.7%) is lower than the classic ">98% of *extrauterine*" figure because this denominator includes uterine ectopics.

### Body systems

Female reproductive system (primary); cardiovascular (haemorrhagic shock, secondary); haematological (anaemia, transfusion requirement).

### Tissue / cell level

| Cell type | Role | CL |
|---|---|---|
| Fallopian tube ciliated epithelial cell | Transport; destroyed by Chlamydia/IL-1 | ⚠️ specific CL term exists — look it up |
| Fallopian tube secretory epithelial cell | CSF1 source driving rupture; OVGP1+ progenitor | ⚠️ lookup |
| Tubal smooth muscle cell (muscularis) | Peristalsis; CB1/β2-AR colocalization | `CL:0000192` smooth muscle cell ⚠️ |
| Extravillous trophoblast | Invades muscularis; dominant in ruptured EP | ⚠️ lookup (`CL:0008036`?) |
| Macrophage | Accumulates via CSF1R; permits invasion | `CL:0000235` ⚠️ |
| CD4+ / CD8+ T cell, NK cell | Altered implantation-site immune milieu | ⚠️ lookup |
| Endothelial cell | Vascular remodelling and erosion | ⚠️ lookup |
| Decidual stromal cell | **Conspicuously ABSENT at the ectopic site** — this absence *is* the mechanism | ⚠️ lookup |

**Curation suggestion:** the *absence* of decidua is the load-bearing anatomical fact. Consider a pathophysiology node named something like "Implantation Without Decidual Investment" with `modifier: DECREASED` or `ABSENT` on a decidualization process term (`GO:0046697` decidualization ⚠️) rather than only listing cell types that *are* there.

### Subcellular

Motile cilium / axoneme (ciliary transport failure) ⚠️; apical plasma membrane glycocalyx (MUC1 barrier) ⚠️; cell surface receptor complexes (TLR2, PROKR1/2, nAChRα7, CB1, CSF1R, EGFR) ⚠️. Look up GO CC terms rather than guessing.

### Lateralization

**Unilateral** in essentially all cases (one tube). Bilateral simultaneous tubal EP is a genuine but vanishingly rare curiosity. Heterotopic pregnancy is a distinct concept — simultaneous intrauterine *and* ectopic, ~0.43% of EPs in the series above, and substantially more common after ART.

---

## 8. Temporal Development

**Onset.** Gestational, not chronological. Tubal EP typically becomes symptomatic at **6–8 weeks' gestation**. Interstitial and caesarean-scar EP present later (often 8–16 weeks) because the surrounding myometrium accommodates more growth — and consequently rupture there is more catastrophic. Onset pattern is **acute to subacute**; a substantial minority are detected **asymptomatically** on early ultrasound in modern early-pregnancy units.

**Course.** Not chronic. Three trajectories:
1. **Spontaneous resolution / tubal abortion** — increasingly recognized; many small failing EPs never need intervention.
2. **Treated resolution** — medical (methotrexate, median time to resolution **28.0 days** in GEM3) or surgical.
3. **Rupture** — the acute catastrophic branch; in fatal cases, "excessive hemorrhage, shock, or renal failure accompanied 67.4% of ectopic pregnancy deaths among hospitalized women" (Creanga 2011).

**Critical intervention window.** Between first detectability (~5 weeks by TVUS/hCG) and rupture. This window is exactly what the diagnostic algorithm (§10) exists to exploit, and it is why the mortality decline of §11 happened.

**Duration.** Self-limited — days to weeks. hCG clearance during successful expectant management: median **19 days** (range 5–82) in one cohort with mean initial β-hCG 488 IU/L. ⚠️ PMC4443555 — verify PMID.

---

## 9. Epidemiology and Population

### Incidence / prevalence

- **~1–2% of all pregnancies** in the United States. This is the headline figure.
- Ectopic pregnancies account for **3–4% of pregnancy-related deaths** despite being 1–2% of pregnancies.
- Among people presenting for abortion care, the rate is much lower (**0.13–0.59%**) — a selection effect worth noting for EHR phenotype work.
- Post-ART: **1.4–5.4%** per cycle, ~2.5–5× baseline.

⚠️ **Curate these using structured `Prevalence` slots, not the deprecated `percentage` field.** Suggested shape:

```yaml
prevalence:
- population: United States
  measure_type: POINT_PREVALENCE   # proportion of pregnancies — see caveat below
  prevalence_class: ABOVE_1_IN_1000
  rate_per_100000: 1500.0          # 1.5% of pregnancies, midpoint of 1–2%
  notes: >
    Expressed as a proportion of PREGNANCIES, not of the general population.
    The dismech PrevalenceMeasureEnum has no "proportion of pregnancies"
    measure type; record the denominator explicitly here.
```

**This is a real modelling problem and you should flag it.** The dismech `PrevalenceMeasureEnum` assumes a population denominator. EP incidence is conventionally reported per *pregnancy*. Either add a note making the denominator unambiguous, or raise it as an open schema question — silently coercing "1–2% of pregnancies" into a per-100,000-population rate would be wrong by a large factor.

### Mortality

```
"Between 1980 and 2007, 876 deaths were attributed to ectopic pregnancy. The ectopic
pregnancy mortality ratio declined by 56.6%, from 1.15 to 0.50 deaths per 100,000 live
births between 1980-1984 and 2003-2007; at the current average annual rate of decline, this
ratio will further decrease by 28.5% to 0.36 ectopic pregnancy deaths per 100,000 live
births by 2013-2017. The ectopic pregnancy mortality ratio was 6.8 times higher for African
Americans than whites and 3.5 times higher for women older than 35 years than those younger
than 25 years during 2003-2007. Of the 76 deaths among women hospitalized between 1998 and
2007, 70.5% were tubal pregnancies; salpingectomy was performed in 80.6% of cases. Excessive
hemorrhage, shock, or renal failure accompanied 67.4% of ectopic pregnancy deaths among
hospitalized women."
```
— Creanga AA, Shapiro-Mendoza CK, Bish CL, Zane S, Berg CJ, Callaghan WM. *Trends in ectopic pregnancy mortality in the United States: 1980-2007.* **Obstet Gynecol** 2011. **PMID:21422853**. Evidence source: `HUMAN_CLINICAL` (national vital statistics + Nationwide Inpatient Sample).

**The 6.8× Black–white mortality disparity is the most important single number in this section** and should be curated prominently, not buried. It is a disparity in *mortality*, not in incidence — i.e. it reflects access to timely diagnosis and management, which is precisely what the authors conclude.

### Inheritance

- **Pattern:** multifactorial / complex. **Not Mendelian.** No AD/AR/X-linked mode. If an `Inheritance` block is curated at all, `HP:0010982` polygenic inheritance ⚠️ with `relationship_type: SUSCEPTIBILITY` gene typing is the only defensible option — and honestly, given a liability-scale h² of ~7%, you could reasonably omit it.
- **Penetrance / expressivity / anticipation / germline mosaicism / founder effects / carrier frequency / consanguinity:** **all not applicable.** Do not fabricate entries for these.

### Demographics

- **Sex ratio:** not applicable — occurs only in people who can become pregnant. Do not curate a M:F ratio.
- **Age:** reproductive years; risk rises with maternal age; mortality 3.5× higher at >35 vs <25.
- **Race/ethnicity:** 6.8× mortality disparity for African Americans (US, 2003–2007). Incidence disparities also reported in a large California system (⚠️ *Perm J* 10.7812/TPP/21.099 — verify).
- **Geography:** the underlying risk-factor distribution tracks PID/chlamydia prevalence and caesarean rates. Case-fatality is far higher in low-resource settings where surgical and transfusion capacity is limited — ⚠️ I did not verify a specific LMIC case-fatality figure; find one before curating.
- **Ancestry limitation in genetics:** European-ancestry biobanks only (§4.1).

---

## 10. Diagnostics

### Core algorithm

Two pillars, for four decades:

```
"Over the last four decades, the foundations of non-invasive diagnosis have been
transvaginal sonography and serum β-human chorionic gonadotropin, with diagnostic
laparoscopy as a confirmatory test if surgical treatment is planned."
```
— Chong KY et al. **Nat Rev Dis Primers** 2024. **PMID:39668167**.

### Laboratory / biomarkers

| Test | Use | LOINC |
|---|---|---|
| Serum β-hCG (quantitative), serial | Trend interpretation; discriminatory zone; treatment monitoring | ⚠️ LOINC lookup required |
| Serum progesterone | Adjunct for viability; low values favour failing pregnancy | ⚠️ lookup |
| CBC / haemoglobin | Haemorrhage assessment | ⚠️ lookup |
| Blood type & Rh | **RhD-negative patients need anti-D prophylaxis** | ⚠️ lookup |

**Discriminatory zone.** The serum hCG level above which an intrauterine gestational sac should be visible on TVUS — conventionally cited around **1,500–3,500 mIU/mL**, with modern practice favouring the **higher** end (≈3,500) to avoid interrupting a viable early intrauterine pregnancy. ⚠️ **This is guideline-level consensus, not a single-paper number — cite ACOG PB 193 (PMID:29470343) and verify the exact threshold language in the bulletin rather than quoting a number from memory.** A single hCG value never diagnoses EP; the *trend* and the ultrasound do.

**Pregnancy of unknown location (PUL).** A distinct diagnostic category, not a diagnosis. Risk-prediction models (the M4/M6 family) triage PUL into low- vs high-risk. ⚠️ *BJOG* 2019 PMID:30129999 "Diagnostic protocols for the management of pregnancy of unknown location" is the right anchor — **fetch and read it**; my search did not surface M6 details directly.

### Imaging

**Transvaginal ultrasound is the diagnostic test of record.** Findings: adnexal mass separate from the ovary ("blob" or "bagel" sign), tubal ring, empty uterus with a decidual reaction (a pseudosac must not be mistaken for a gestational sac), free fluid in the pouch of Douglas, and in the definitive case an extrauterine gestational sac with yolk sac or embryo ± cardiac activity. Doppler shows a "ring of fire" peritrophoblastic flow. Colour-Doppler and 3D imaging matter especially for caesarean-scar and interstitial EP, where misdiagnosis is common. ⚠️ *Emerg Radiol* 2022 PMID:34618256 is a good imaging-pitfalls reference.

MRI is second-line, used for equivocal caesarean-scar/interstitial/abdominal cases.

### Histopathology

Chorionic villi and/or implantation-site trophoblast in tubal mucosa, muscularis, or serosa is **confirmatory**. Villi in direct contact with muscularis, accreta-like. In the uterus: **Arias-Stella reaction** in endometrial glands and decidualized stroma **without villi** — a decidual cast is not a diagnosis of EP by itself, but villi absent from uterine curettings in a patient with a positive pregnancy test and rising hCG is strong evidence.

### Genetic testing

**Not indicated. There is no clinical genetic test for ectopic pregnancy.** WGS, WES, panels, CMA, karyotype, FISH, mtDNA, and repeat-expansion testing are all **not applicable**. The GWAS loci have no clinical predictive utility. Say this explicitly in the KB rather than leaving the section blank — an empty section reads as "not yet curated," a stated "not applicable" reads as knowledge.

### Omics-based diagnostics

None in clinical use. Research-stage only (scRNA-seq, spatial transcriptomics — §6.7). No validated liquid biopsy, proteomic, or metabolomic test.

### Clinical criteria and differential diagnosis

**Guidelines:** ACOG Practice Bulletin No. 193 *Tubal Ectopic Pregnancy* (**PMID:29470343**, 2018; supersedes No. 191, PMID:29232273); NICE NG126 *Ectopic pregnancy and miscarriage: diagnosis and initial management* (PMID:31393678, updated 2023); RCOG Green-top guidance.

```
"Ectopic pregnancy is defined as a pregnancy that occurs outside of the uterine cavity.
The most common site of ectopic pregnancy is the fallopian tube. Most cases of tubal ectopic
pregnancy that are detected early can be treated successfully either with minimally invasive
surgery or with medical management using methotrexate. However, tubal ectopic pregnancy in an
unstable patient is a medical emergency that requires prompt surgical intervention."
```
— ACOG Committee on Practice Bulletins—Gynecology. **Obstet Gynecol** 2018. **PMID:29470343**.

**Differential diagnosis** (with distinguishing features — good `differentials` block material):

| Condition | Distinguishing feature |
|---|---|
| Threatened / incomplete miscarriage | Intrauterine sac or villi present; hCG falling |
| Normal early intrauterine pregnancy | hCG rising appropriately; sac appears at discriminatory zone |
| Corpus luteum cyst / haemorrhagic ovarian cyst | Within the ovary, moves *with* it on probe pressure |
| Ovarian torsion | Whirlpool sign, absent Doppler flow, no hCG requirement |
| Appendicitis | RLQ, fever, leucocytosis, ± negative pregnancy test |
| PID / tubo-ovarian abscess | Fever, discharge, cervical motion tenderness |
| Gestational trophoblastic disease | Very high hCG, characteristic vesicular ultrasound |
| Heterotopic pregnancy | **The trap** — an intrauterine sac does *not* exclude a coexisting EP, especially post-ART |

### Screening

There is no screening test for ectopic pregnancy itself. **Screening is for the upstream risk factor:** population *Chlamydia trachomatis* screening in sexually active young people, which is the principal evidence-based prevention lever (§13). ⚠️ *Infect Dis Clin North Am* 2023 PMID:37005162 for the chlamydia screening update.

---

## 11. Outcome / Prognosis

### Mortality

- **US mortality ratio: 0.50 deaths per 100,000 live births (2003–2007)**, down 56.6% from 1.15 (1980–1984); projected 0.36 by 2013–2017 (Creanga, PMID:21422853).
- EP causes **3–4% of all pregnancy-related deaths** despite affecting 1–2% of pregnancies.
- Among fatal hospitalized cases: 70.5% tubal, salpingectomy in 80.6%, and 67.4% accompanied by excessive haemorrhage/shock/renal failure.
- Disparities: **6.8× higher in African Americans**; **3.5× higher at age >35 vs <25**.

### Morbidity

- **Rupture** with haemoperitoneum and hypovolaemic shock — the acute catastrophic outcome.
- **Blood transfusion** and emergency surgery are themselves sources of morbidity (explicitly named as such in the Nat Rev Dis Primers abstract).
- **Loss of a fallopian tube** (salpingectomy in the majority of surgical cases).
- **Chronic pelvic pain.**
- **Subfertility / infertility.**
- **Psychological distress** — grief of pregnancy loss compounded by threat to life and to future fertility. Both major reviews name it; it is consistently under-measured.

### Fertility outcomes

- **Subsequent intrauterine pregnancy: ~50–80%.** ⚠️ secondary-source range — verify.
- **Recurrence: ~10–20%** (7–13× the baseline odds). UK tertiary cohort: 10.4% recurrent extrauterine EP among 567 women; a 5-year follow-up cohort: 18.9% of 217.
- **Salpingotomy does not improve fertility over salpingectomy** — the ESEP trial is definitive here and directly contradicts long-standing surgical intuition:

```
"The cumulative ongoing pregnancy rate was 60·7% after salpingotomy and 56·2% after
salpingectomy (fecundity rate ratio 1·06, 95% CI 0·81-1·38; log-rank p=0·678). Persistent
trophoblast occurred more frequently in the salpingotomy group than in the salpingectomy
group (14 [7%] vs 1 [<1%]; RR 15·0, 2·0-113·4). Repeat ectopic pregnancy occurred in 18
women (8%) in the salpingotomy group and 12 (5%) women in the salpingectomy group (RR 1·6,
0·8-3·3)."
```
— Mol F, van Mello NM, Strandell A, ... Hajenius PJ; ESEP study group. *Salpingotomy versus salpingectomy in women with tubal pregnancy (ESEP study): an open-label, multicentre, randomised controlled trial.* **Lancet** 2014;383(9927):1483–89. **PMID:24499812**. Evidence source: `HUMAN_CLINICAL` (RCT, n=446).

⚠️ **Important scope condition** the abstract states and curators drop: the trial enrolled women **with a healthy contralateral tube**. The conclusion does not extend to women whose other tube is damaged or absent. Curate that qualifier.

Note also the practical detail that 20% of the salpingotomy arm was converted to salpingectomy intraoperatively for persistent bleeding.

### Prognostic factors

For **methotrexate success**, the initial β-hCG is the dominant predictor (⚠️ Lipscomb et al. 1999 — **fetch PMID and verify these bands**):

| Initial β-hCG (mIU/mL) | Approx. single-dose success |
|---|---|
| <5,000 | >90% |
| 5,000–9,999 | ~87% (13% failure) |
| 10,000–14,999 | ~82% (18% failure) |
| >15,000 | <70% |

Early kinetics also predict: day 1–4 post-treatment hCG change predicts single-dose success (**PMID:37178269**, *Hum Reprod* 2023 — ⚠️ fetch abstract).

For **expectant management**: low and falling hCG. Predicted success ~97% with discharge β-hCG <650 IU/L *and* ≥50% decrease from admission; with starting hCG >2,000 mIU/mL and declining values, 93.3% still failed expectant management. ⚠️ Verify both figures against primary sources — they come from different cohorts with different definitions.

Other prognostic factors: presence of fetal cardiac activity (worse), large adnexal mass, free fluid volume, and implantation site (isthmic and interstitial worse than ampullary).

---

## 12. Treatment

Three management strategies, chosen by haemodynamic stability, hCG, ultrasound findings, and patient preference.

```
"Once diagnosed, ectopic pregnancy can be managed expectantly, treated medically with
methotrexate or managed surgically. Future fertility is an important but often overlooked
aspect in the management of ectopic pregnancy."
```
— Chong KY et al. **Nat Rev Dis Primers** 2024. **PMID:39668167**.

### 12.1 Surgical

**Laparoscopic salpingectomy is the reference standard.**

```
"Minimally invasive surgical skills are now widespread, and laparoscopic surgery is
recognized as the best and safest operative treatment for extrauterine ectopic pregnancies.
Based on the evidence from randomized trials published a decade ago, laparoscopic
salpingectomy is accepted as the optimal surgical treatment for tubal ectopic pregnancy."
```
— Farren J, Al Wattar BH, Jurkovic D. **Hum Reprod Update** 2026. **PMID:41061761**.

Note the same review immediately flags that this is **under renewed scrutiny**: *"with recent advances in surgical techniques and improvement in surgical skills, the appropriateness of tubal removal versus conservation is under increasing scrutiny."* Curate the standard *and* the live debate.

- **Salpingectomy** — removal of the affected tube. Definitive; ~0% persistent trophoblast.
- **Salpingotomy/salpingostomy** — tube-conserving. **7% persistent trophoblast (RR 15.0)**; requires post-op hCG surveillance; no fertility benefit (ESEP).
- **Laparotomy** — reserved for haemodynamic instability or massive haemoperitoneum.
- **Adjuncts:** blood transfusion, anti-D immunoglobulin for RhD-negative patients.

Suggested treatment annotations:
```yaml
- name: Laparoscopic Salpingectomy
  therapeutic_modality: SURGERY
  treatment_term:
    preferred_term: Surgical Procedure
    term: {id: NCIT:C15329, label: Surgical Procedure}   # ⚠️ a specific NCIT
    # salpingectomy term likely exists — search NCIT with OAK first and prefer it
```

### 12.2 Medical — methotrexate

Antifolate; inhibits dihydrofolate reductase, halting rapidly dividing trophoblast. Regimens: single-dose (50 mg/m² IM), two-dose, and multi-dose with leucovorin rescue.

- **Contraindications:** haemodynamic instability, ruptured EP, fetal cardiac activity (relative), high hCG, breastfeeding, hepatic/renal/haematological impairment, immunodeficiency, active peptic ulcer.
- **Adverse effects:** stomatitis, nausea, transaminitis, bone-marrow suppression; **separation pain** (a transient pain increase, easily confused with rupture, requiring careful counselling).
- **Failure rate ~30%**, requiring rescue surgery — stated in GEM3's own rationale.
- The 2026 review notes bluntly: *"By contrast, the efficacy of medical management with methotrexate has been questioned."* This is a genuine shift and should be curated, not smoothed over.

```yaml
- name: Methotrexate
  therapeutic_modality: SMALL_MOLECULE
  treatment_term:
    preferred_term: Pharmacotherapy
    term: {id: NCIT:C15986, label: Pharmacotherapy}
    therapeutic_agent:
    - preferred_term: methotrexate
      term: {id: CHEBI:44185, label: methotrexate}   # ⚠️ VERIFY — and note the
      # memory entry "therapeutic-agent-chebi-only-cache": prefer CHEBI over NCIT here
```

### 12.3 Expectant management

Now mainstream, and the 2026 review calls it one of the field's key developments:

```
"The necessity to avoid overtreatment and the potential for iatrogenic harm in such cases
has facilitated the introduction of expectant management into mainstream clinical practice.
This represents one of the key developments in the care for women with ectopic pregnancies."
```
— Farren J et al. **PMID:41061761**.

Candidates: haemodynamically stable, low and falling hCG, small mass, no fetal cardiac activity, reliable follow-up.

### 12.4 Site-specific management

Caesarean-scar, interstitial, cervical, and abdominal EP each require distinct approaches (local methotrexate, uterine artery embolization, hysteroscopic or laparoscopic resection, gestational-sac aspiration). The 2026 review notes uterine ectopics carry higher morbidity and mortality, are harder to diagnose, and uniquely may reach fetal viability — raising a genuinely hard ethical decision:

```
"Another challenge, which is peculiar to uterine ectopic pregnancies, is their potential to
progress to reach foetal viability, albeit with a high risk of extreme prematurity. This
requires women and clinicians to make difficult decisions about whether these pregnancies
should be terminated to protect maternal health, despite some possibility of a good foetal
outcome."
```
— Farren J et al. **PMID:41061761**.

### 12.5 Experimental — and one important negative trial

**GEM3** is the most important recent therapeutic trial and it is a **negative** one. Curate it as `supports: REFUTE` against the EGFR-adjuvant hypothesis:

```
"Between Nov 2, 2016, and Oct 6, 2021, 328 participants were allocated to methotrexate and
gefitinib (n=165) or methotrexate and placebo (n=163). Three participants in the placebo
group withdrew. Surgical intervention occurred in 50 (30%) of 165 participants in the
gefitinib group and in 47 (29%) of 160 participants in the placebo group (adjusted risk
ratio 1·15, 95% CI 0·85 to 1·58; adjusted risk difference -0·01, 95% CI -0·10 to 0·09;
p=0·37). Without surgical intervention, median time to resolution was 28·0 days in the
gefitinib group and 28·0 days in the placebo group (subdistribution hazard ratio 1·03, 95%
CI 0·75 to 1·40). Serious adverse events occurred in five (3%) of 165 participants in the
gefitinib group and in six (4%) of 162 participants in the placebo group. Diarrhoea and rash
were more common in the gefitinib group."
```

```
"In women with a tubal ectopic pregnancy, adding oral gefitinib to parenteral methotrexate
does not offer clinical benefit over methotrexate and increases minor adverse reactions."
```
— Horne AW, Tong S, Moakes CA, Middleton LJ, Duncan WC, Mol BW, Whitaker LHR, Jurkovic D, Coomarasamy A, Nunes N, Holland T, Clarke F, Doust AM, Daniels JP; GEM3 collaborative. **Lancet** 2023. **PMID:36738759**. Registered ISRCTN67795930.

⚠️ **Clinical-trial curation note:** GEM3 is an **ISRCTN**, not an NCT. The dismech `clinical_trials` block and `just fetch-reference` are built around ClinicalTrials.gov NCT identifiers. Either find a corresponding NCT registration, or cite the Lancet paper as an ordinary PMID evidence item rather than forcing an ISRCTN into an NCT-shaped slot. Also remember `phase` is an **enum** (`PHASE_III`), not free text.

Other experimental directions (all early-stage): nanomedicine-based targeted delivery (PMID:37471169), and pharmacological alternatives reviewed in PMID:36361110.

### 12.6 Pharmacogenomics

⚠️ No EP-specific pharmacogenomic guidance. Generic methotrexate PGx (e.g. *MTHFR*, *SLC19A1*) exists in PharmGKB but is **not** validated for the single-dose EP indication and has no CPIC guideline for this use. Do not curate it as EP-specific.

### 12.7 Supportive care

Analgesia, IV fluids and transfusion, anti-D prophylaxis, contraception counselling (methotrexate mandates a pregnancy-avoidance interval — ⚠️ verify the currently recommended duration from ACOG PB 193; recommendations have changed and I will not quote a number I haven't read), bereavement support, and explicit counselling about future fertility and recurrence risk.

---

## 13. Prevention

### Primary

- **Chlamydia screening and treatment programmes** — the principal evidence-based lever. Preventing PID prevents the tubal damage that causes EP.
- **Smoking cessation.**
- **Safer-sex / STI prevention** and partner notification.
- **Avoiding unnecessary tubal surgery**; careful technique when tubal surgery is required.
- **In ART:** single embryo transfer, and consideration of prophylactic salpingectomy for hydrosalpinx before IVF (⚠️ this last one has its own evidence base — verify before curating).
- **Reducing the primary caesarean rate** — the upstream prevention for the fastest-growing EP subtype.

### Secondary

- **Early pregnancy assessment units (EPAU)** with rapid access to TVUS and serial hCG. This organizational intervention is what actually drove the mortality decline, and the 2026 review credits it directly.
- **Risk-stratified early scanning** for women with prior EP, tubal surgery, or ART conception.
- **PUL protocols** with structured risk prediction.

### Tertiary

- Post-treatment hCG surveillance to catch persistent trophoblast (especially after salpingotomy, where the risk is 7%).
- Early scanning in the *next* pregnancy given 10–20% recurrence.
- Anti-D prophylaxis to prevent alloimmunization affecting future pregnancies.

### Not applicable

**Immunization:** no vaccine (a chlamydia vaccine would be indirect prevention, and none is licensed). **Genetic screening / carrier screening / PGD / prenatal testing / genetic counselling:** **not applicable** — there is no Mendelian genetics here. State this explicitly.

---

## 14. Other Species / Natural Disease

This section is unusually interesting for EP and is a genuine differentiator for the KB entry.

```
"Ectopic pregnancy denotes a pregnancy occurring elsewhere than in the cavity of the
uterus... While this condition is well-known in humans, it is rarely diagnosed in animals.
However, the causes and mechanisms leading to an ectopic implantation of the ovum are not
always clearly defined in humans or animals... Several differences exist in ectopic
pregnancies between human beings and animal species. While abdominal pregnancy has been
described in both human and animal species, tubal ectopic pregnancies would appear to be
restricted to primates. Other than anecdotal cases, this pathological condition does not
occur in laboratory, domestic or farm animals. Several factors are described as being the
cause of these differences."
```
— Corpa JM. *Ectopic pregnancy in animals and humans.* **Reproduction** 2006;131(4):631. **PMID:16595714**. Evidence source: `OTHER` (comparative review) or `MODEL_ORGANISM` depending on how you read it — I'd argue `OTHER`, since it's a cross-species narrative synthesis rather than a primary animal study.

**Key comparative facts:**
- **Tubal ectopic pregnancy is essentially restricted to primates** (⚠️ `NCBITaxon:9443` Primates — verify). This is a striking and curatable claim.
- **Abdominal "ectopic" pregnancy in domestic animals is usually *secondary*** — following uterine rupture, with the fetus expelled into the peritoneal cavity — not primary ectopic implantation. Veterinary case reports in dogs, cats, rabbits, and ruminants almost always describe this secondary form. **Do not curate these as equivalent to human tubal EP.**
- **Mechanistic explanation:** the human/great-ape reproductive strategy combines **spontaneous decidualization** and **deeply invasive haemochorial placentation**. A trophoblast evolved to burrow aggressively into maternal tissue and remodel spiral arteries will happily do so wherever it lands. Deep invasion with spiral artery remodelling is documented in gorillas and chimpanzees, indicating it predates the human lineage split. Most mammals have less invasive placentation and induced (not spontaneous) decidualization, so a retained embryo simply fails rather than implanting ectopically.

**This is the strongest argument for why EP is a distinctly human disease and why animal models fail** — and it deserves a `HUMAN_MODEL_MISMATCH` discussion in the entry.

⚠️ Sources for the placental-evolution claims: *Unique Aspects of Human Placentation* (PMC8347521) and Carter & Pijnenborg, *Evolution of invasive placentation with special reference to non-human primates* (Best Pract Res Clin Obstet Gynaecol) — **fetch PMIDs before citing.** An anecdotal ectopic pregnancy in the southern grass skink also turned up; entertaining, but not curation-grade.

**OMIA:** ⚠️ no OMIA entry expected for a non-heritable, non-Mendelian condition — verify rather than fabricate. **VBO breeds:** not applicable. **Zoonotic potential:** not applicable. **Orthologous genes:** relevant genes (*Cnr1*, *Muc1*, *Tlr2*, *Prokr1/2*, *Csf1*) are well conserved with mouse orthologs; ⚠️ pull NCBI Gene IDs if you curate them.

---

## 15. Model Organisms

**The headline is a negative:** there is **no animal model that reproduces human tubal ectopic pregnancy.** The 2010 review says so plainly, noting existing data are *"mostly descriptive"* with *"few adequate animal models available."* Curate this limitation front and centre.

### What models do exist, and what each captures

| Model | Type | Captures | Does NOT capture |
|---|---|---|---|
| **Cnr1−/− mouse** (`MGI` ⚠️) | Genetic KO, mammalian | Oviductal embryo **retention**; the transport arm; rescued by isoproterenol | Tubal **implantation**. Mice get retention → pregnancy failure, not EP |
| **Methanandamide-treated WT mouse** | Pharmacological induction | Phenocopies the transport defect | Same limitation |
| **Cnr1/Cnr2 double KO mouse** | Genetic | Implantation defects (⚠️ *Endocrinology* 2019 160(4):938 — verify PMID) | |
| **Human fallopian tube explant / organ culture** | *Ex vivo*, human tissue | Chlamydia-induced ciliary destruction; IL-1 initiation; PROKR1/2 induction | No embryo, no implantation |
| **OE-E6/E7 oviductal epithelial cell line** | *In vitro*, human | TLR2/NF-κB → PROKR2; nAChRα7 → PROKR1; dominant-negative rescue | Cell-autonomous only |
| **Mouse Chlamydia salpingitis model** | Induced infection | Tubal inflammation and damage | Not ectopic implantation |
| **Non-human primates** | Mammalian | The only taxa with genuine tubal EP | Rare, sporadic, ethically and practically prohibitive as an experimental system |
| **Trophoblast + blood vessel organoids** | *In vitro*, human | WNT2B and intravillous vascularization in EP vs IUP (⚠️ bioRxiv 2022.04.18.488605 — **preprint, verify status**) | Not a whole-organ model |

**Reciprocal embryo transfer finding worth curating** (from the Wang/Dey work): transferring embryos between Cnr1−/− and wild-type females showed that **maternal** CB1 loss drives oviductal retention regardless of the embryo's genotype. That cleanly localizes the defect to the maternal tract rather than the conceptus. ⚠️ This detail is from the paper body/secondary description, not the abstract quoted above — **verify against full text before curating a snippet.**

### Model databases

MGI (mouse `Cnr1`, `Muc1`, `Tlr2`, `Csf1`), IMPC/KOMP for null alleles, Cellosaurus for OE-E6/E7, Alliance of Genome Resources for orthology. ⚠️ Pull accessions rather than guessing them.

### Recommended dismech discussion block

```yaml
discussions:
- kind: HUMAN_MODEL_MISMATCH
  prompt: >
    Does oviductal embryo retention in Cnr1-null mice model human tubal ectopic
    pregnancy, given that mice do not develop tubal implantation?
  rationale: >
    Cnr1-null mice show robust oviductal embryo retention, but the retained embryos
    fail rather than implanting in the oviduct. Human tubal ectopic pregnancy requires
    both retention AND a receptive tubal microenvironment permitting implantation.
    Tubal ectopic pregnancy appears restricted to primates, plausibly because
    spontaneous decidualization and deeply invasive haemochorial placentation are
    primate-specific. The mouse therefore models only the transport arm of the
    two-hit model.
  # attaches_to: pathophysiology#<your retention node>   ⚠️ multivalued — it's a LIST
```

---

## Consolidated Ontology Term Suggestions

### ✅ Verified live this session (OLS4/EBI)
`MONDO:0000755` ectopic pregnancy · `MONDO:0043762` tubal pregnancy · `MONDO:0043759` abdominal ectopic pregnancy · `MONDO:0044098` ovarian ectopic pregnancy · `MONDO:0044101` pregnancy, cornual · `MONDO:0000922` pelvic inflammatory disease · `MONDO:0001173` acute salpingitis · `MONDO:0003616` salpingitis isthmica nodosa · `HP:0031456` Ectopic pregnancy

### ⚠️ Candidates — run OAK / `just validate-terms` before committing
**HP:** abdominal pain, amenorrhea, vaginal haemorrhage, syncope, tachycardia, hypotension, anaemia, shock, haemoperitoneum, infertility, polygenic inheritance (`HP:0010982`)
**GO BP:** cilium movement, smooth muscle contraction, embryo implantation, decidualization, inflammatory response, angiogenesis, toll-like receptor 2 signaling pathway, canonical NF-κB signal transduction, EGFR signaling pathway, GPCR signaling pathway
**CL:** fallopian tube ciliated epithelial cell, fallopian tube secretory epithelial cell, smooth muscle cell, extravillous trophoblast, macrophage, CD4+/CD8+ αβ T cell, NK cell, decidual stromal cell
**UBERON:** fallopian tube, ampulla/isthmus/infundibulum of fallopian tube, uterus, endometrium, myometrium, uterine cervix, ovary, peritoneal cavity
**CHEBI:** methotrexate, gefitinib, nicotine, cotinine, progesterone, anandamide, methanandamide, isoprenaline
**NCIT:** `NCIT:C15986` Pharmacotherapy, `NCIT:C15329` Surgical Procedure, `NCIT:C15747` Supportive Care — plus specific salpingectomy / salpingotomy / laparoscopy / blood transfusion / ultrasound terms that almost certainly exist and should be searched for rather than approximated
**HGNC (lowercase prefix per repo convention):** `muc1`, `cnr1`, `adrb2`, `prokr1`, `prokr2`, `prok1`, `tlr2`, `nfkbia`, `chrna7`, `il1b`, `il1rn`, `cxcl8`, `csf1`, `csf1r`, `egfr`, `ovgp1`

---

## Evidence Summary — verified quotes ready for curation

| PMID | Short cite | Evidence source | Use |
|---|---|---|---|
| 39668167 | Chong 2024 Nat Rev Dis Primers | HUMAN_CLINICAL | Definition, mortality framing, morbidity, management overview |
| 41061761 | Farren 2026 Hum Reprod Update | HUMAN_CLINICAL | Modern classification, uterine ectopics, expectant management, MTX questioned |
| 20071358 | Shaw 2010 Hum Reprod Update | HUMAN_CLINICAL | **The two-hit aetiology statement** — the pathograph anchor |
| 21422853 | Creanga 2011 Obstet Gynecol | HUMAN_CLINICAL | Mortality trends, racial and age disparities, cause of death |
| 29470343 | ACOG PB 193 (2018) | HUMAN_CLINICAL | Guideline definition and management standard |
| 37877466 | Pujol Gualdo 2023 Hum Reprod | HUMAN_CLINICAL | GWAS, MUC1, heritability, smoking genetic correlation |
| 21224062 | Shaw 2011 Am J Pathol | IN_VITRO + HUMAN_CLINICAL (split!) | Chlamydia → TLR2 → NF-κB → PROKR2 |
| 20864676 | Shaw 2010 Am J Pathol | IN_VITRO + HUMAN_CLINICAL (split!) | Cotinine → nAChRα7 → PROKR1 |
| 15378054 | Wang 2004 Nat Med | MODEL_ORGANISM | CB1 loss → oviductal retention |
| 19093002 | Horne 2008 PLoS One | HUMAN_CLINICAL | CB1 attenuated in EP tissue; CNR1 polymorphism **negative** |
| 17614966 | Hvid 2007 Cell Microbiol | IN_VITRO | IL-1 initiates ciliated-cell destruction |
| 36721079 | Zhao 2023 Cell Prolif | HUMAN_CLINICAL (+IN_VITRO) | scRNA-seq; CSF1/CSF1R drives rupture |
| 24499812 | Mol 2014 Lancet (ESEP) | HUMAN_CLINICAL (RCT) | Salpingotomy vs salpingectomy; no fertility benefit |
| 36738759 | Horne 2023 Lancet (GEM3) | HUMAN_CLINICAL (RCT) | Gefitinib+MTX **negative** — curate as REFUTE |
| 16595714 | Corpa 2006 Reproduction | OTHER | Tubal EP restricted to primates |

---

## Explicit knowledge gaps (curate as `KNOWLEDGE_GAP` discussions rather than leaving blank)

1. **No adequate animal model of tubal ectopic pregnancy exists** — stated by the field's own review; the mechanism literature is consequently "mostly descriptive."
2. **The chromosome 10 GWAS locus (rs11598956) has no assigned gene.**
3. **All genetic data are European-ancestry, maternal-genome-only.** Paternal and fetal genome contributions are unstudied.
4. **No EP epigenomic, proteomic, metabolomic, or lipidomic dataset** of curation quality was located.
5. **Fresh vs frozen embryo transfer:** the literature genuinely conflicts on EP risk direction.
6. **Methotrexate efficacy is now openly questioned** by a 2026 authoritative review, but no head-to-head trial resolves MTX vs expectant management across the moderate-hCG range.
7. **Whether salpingectomy remains optimal** is under active re-examination as surgical technique improves — the ESEP conclusion may not survive.
8. **No validated QoL/utility instrument data** (EQ-5D, SF-36) for ectopic pregnancy despite universal acknowledgement of psychological morbidity.
9. **The interpregnancy-interval finding** (short interval protective against recurrence) is counterintuitive, single-centre, and retrospective — replication needed.
10. **Cannabis exposure and human EP risk** is mechanistically predicted by the mouse CB1 work but epidemiologically unestablished.

---

## Curation gotchas specific to this entry

A few landmines I hit while researching, worth writing down before you open the YAML:

- **Denominator confusion.** "1–2%" is *of pregnancies*, not of the population. The `Prevalence` slots assume a population denominator. Flag this rather than silently converting.
- **IUD direction reversal.** Relative proportion up, absolute risk down. Easy to curate backwards.
- **The `>98%` figure is of *extrauterine* EPs.** Once you include caesarean-scar and other uterine ectopics in the denominator, tubal drops to ~85%. Two different numbers, two different denominators, both correct.
- **ISRCTN ≠ NCT.** GEM3 won't fit the `clinical_trials` block's fetch pipeline.
- **Split the Shaw papers' evidence items.** Both mix human tissue observation with cell-line experiments; one `evidence_source` per item.
- **The ESEP conclusion has a scope condition** (healthy contralateral tube) that gets dropped constantly.
- **Don't fabricate ORPHA/OMIM/genetic-testing content.** Explicit "not applicable" beats a plausible-looking invention every time — and this is exactly the disease where a deep-research tool would be tempted to hallucinate a rare-disease identifier.
- **Named Entity Confusion risk here is low** (no eponym, no numbered series, no gene-adjacent sibling), but "cornual" vs "interstitial" is a genuine terminology collision worth watching.

---

**Sources:**
[Shaw 2010 Hum Reprod Update — PMID:20071358](https://pubmed.ncbi.nlm.nih.gov/20071358/) · [Chong 2024 Nat Rev Dis Primers — PMID:39668167](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:39668167&resultType=core&format=json) · [Farren 2026 Hum Reprod Update — PMID:41061761](https://pubmed.ncbi.nlm.nih.gov/41061761/) · [Creanga 2011 — PMID:21422853](https://pubmed.ncbi.nlm.nih.gov/21422853/) · [ACOG PB 193 — PMID:29470343](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:29470343&resultType=core&format=json) · [Pujol Gualdo 2023 GWAS — PMID:37877466](https://academic.oup.com/humrep/article/38/12/2516/7329306) · [Shaw 2011 Chlamydia/PROKR2 — PMID:21224062](https://pubmed.ncbi.nlm.nih.gov/21224062/) · [Shaw 2010 Cotinine/PROKR1 — PMID:20864676](https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:20864676&resultType=core&format=json) · [Wang 2004 Nat Med — PMID:15378054](https://pubmed.ncbi.nlm.nih.gov/15378054/) · [Horne 2008 PLoS One — PMID:19093002](https://pubmed.ncbi.nlm.nih.gov/19093002/) · [Hvid 2007 — PMID:17614966](https://pubmed.ncbi.nlm.nih.gov/17614966/) · [Zhao 2023 CSF1 scRNA-seq — PMID:36721079](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10334268/) · [Mol 2014 ESEP — PMID:24499812](https://pubmed.ncbi.nlm.nih.gov/24499812/) · [Horne 2023 GEM3 — PMID:36738759](https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(22)02478-3/fulltext) · [Corpa 2006 — PMID:16595714](https://pubmed.ncbi.nlm.nih.gov/16595714/) · [Bouyer 2003 Am J Epidemiol](https://academic.oup.com/aje/article-abstract/157/3/185/71089) · [EP site distribution / CSP trend](https://pmc.ncbi.nlm.nih.gov/articles/PMC9392275/) · [Unique Aspects of Human Placentation](https://pmc.ncbi.nlm.nih.gov/articles/PMC8347521/) · [MONDO/HP lookups — EBI OLS4](https://www.ebi.ac.uk/ols4/)