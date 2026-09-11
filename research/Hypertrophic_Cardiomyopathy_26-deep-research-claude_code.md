---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-01T20:55:36.190747'
end_time: '2026-08-01T21:10:07.352206'
duration_seconds: 871.16
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hypertrophic Cardiomyopathy 26
  mondo_id: ''
  category: Genetic
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
  web_search_requests: 20
  num_turns: 53
  total_cost_usd: 4.548623250000001
  session_id: ffc709ba-09ef-4215-b22a-32ae330f332d
  stop_reason: end_turn
citation_count: 23
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypertrophic Cardiomyopathy 26
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Hypertrophic Cardiomyopathy 26** covering all of the
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

# Comprehensive Research Report: Hypertrophic Cardiomyopathy 26 (CMH26; *FLNC*-related HCM)

**Prepared:** 2026-08-01 · **Target entity:** MONDO:0014883 / OMIM:617047 · **Gene:** *FLNC* (hgnc:3756)

---

## ⚠️ Framing Caveat — Read Before Curating

**CMH26 is an OMIM gene-series label, not a clinically coherent standalone disease.** Three facts must shape the KB entry:

1. **The same gene produces at least four distinct cardiac entities**, and the genotype–phenotype split is mechanistically real: **non-truncating (missense/in-frame) variants → HCM/RCM/myofibrillar myopathy** (aggregate-forming, proteotoxic); **truncating variants → DCM/left-dominant arrhythmogenic cardiomyopathy** (haploinsufficiency). CMH26 refers *only* to the former arm.
2. **MONDO:0014883 folds "cardiomyopathy, familial restrictive 5" in as an exact synonym** (verified locally with OAK). In practice, *FLNC*-missense HCM and *FLNC*-missense RCM are one continuum, and the newest data argue the "hypertrophic" label is partly a misnomer — the phenotype is **hypertrophic-restrictive without hypercontractility**.
3. **The evidence base is genuinely contested.** ClinGen calls *FLNC* (non-LOF) **Definitive** for HCM, but at least one large cohort found no case–control excess, and the most recent burden analysis puts the **etiologic fraction for rare *FLNC* missense in unselected HCM at only 0.45** — meaning roughly half of *FLNC* missense variants found in HCM patients are incidental. Curate the `mechanistic_hypotheses` / `supports: PARTIAL` machinery accordingly.

**Items I could not verify** are flagged inline: OMIM full text returned HTTP 403; gnomAD numeric constraint metrics for *FLNC* could not be retrieved; the Heart Rhythm 2026 paper's PMID was not obtainable (cited by journal/PII).

---

## 1. Disease Information

### Overview

Hypertrophic cardiomyopathy 26 (CMH26) is the form of familial hypertrophic cardiomyopathy caused by heterozygous variants in *FLNC*, encoding **filamin C** — a large, muscle-specific actin-cross-linking protein of the sarcomeric Z-disc. It was defined as a distinct genetic form in 2014 by whole-exome sequencing of Spanish HCM families (PMID:25351925). The characteristic molecular signature is **intracellular filamin C aggregate formation** with sarcomeric disarray, and the characteristic clinical signature — as refined by later work — is a **hypertrophic-restrictive phenotype with small LV cavity, severe diastolic dysfunction, a distinctive repolarization ECG, and frequent extracardiac (musculoskeletal) findings**, rather than the classic hypercontractile obstructive HCM of sarcomeric (*MYH7*/*MYBPC3*) disease.

### Key Identifiers (verified)

| Resource | Identifier | Label |
|---|---|---|
| MONDO | **MONDO:0014883** | hypertrophic cardiomyopathy 26 |
| OMIM | **617047** | CARDIOMYOPATHY, FAMILIAL HYPERTROPHIC, 26; CMH26 |
| MedGen | 934716 | Hypertrophic cardiomyopathy 26 |
| UMLS | C4310749 | — |
| DOID | DOID:0110327 | — |
| GARD | GARD:0025029 | — |
| Gene | **hgnc:3756** (*FLNC*), OMIM \*102565, UniProt **Q14315**, 7q32.1 | filamin C |
| Orphanet | *No CMH26-specific ORPHA code.* Umbrella: **ORPHA:217569** familial isolated hypertrophic cardiomyopathy | — |
| ICD-10 | **I42.1** (obstructive HCM) / **I42.2** (other HCM); RCM presentation → **I42.5** | — |
| ICD-11 | **BC43.0** Hypertrophic cardiomyopathy | — |
| MeSH | D002312 Cardiomyopathy, Hypertrophic, Familial | — |

MONDO definition (verbatim, OAK `sqlite:obo:mondo`): *"Any hypertrophic cardiomyopathy in which the cause of the disease is a mutation in the FLNC gene."* Logical axiom: `MONDO:0005045 AND RO:0004003 some HGNC:3756`. Parent: `MONDO:0024573` familial hypertrophic cardiomyopathy.

### Synonyms (from MONDO, verified)

CMH26 · cardiomyopathy, familial hypertrophic, 26 · cardiomyopathy, familial hypertrophic, type 26 · hypertrophic cardiomyopathy type 26 · *FLNC* hypertrophic cardiomyopathy · hypertrophic cardiomyopathy caused by mutation in FLNC · **cardiomyopathy, familial restrictive 5** (note the RCM conflation)

Clinically used but non-ontological: "cardiac filaminopathy," "*FLNC*-related cardiomyopathy," "non-truncating *FLNC* cardiomyopathy."

### Data provenance

Aggregated disease-level: OMIM, MONDO, MedGen, ClinGen GCEP, ClinVar. Individual-patient: family-based cohort studies (Spanish, UK, Chinese, Russian cohorts) and case series; UK Biobank / gnomAD used as population comparators. No EHR-derived phenotype algorithm exists for CMH26 specifically.

---

## 2. Etiology

### Primary cause

Heterozygous, autosomal-dominant, **non-truncating** germline variants in *FLNC* — predominantly missense substitutions and small in-frame deletions. There is no infectious or environmental cause. Foundational statement (PMID:25351925, verbatim abstract):

> "Whole-exome sequencing reveals a variant in the gene encoding the sarcomeric protein filamin C (p.A1539T) that segregates with the disease in this family. Sequencing of 92 HCM cases identifies seven additional variants segregating with the disease in eight families. Patients with FLNC mutations show marked sarcomeric abnormalities in cardiac muscle, and functional analysis reveals that expression of these FLNC variants resulted in the formation of large filamin C aggregates."

### Genetic risk factors

- **Causal:** *FLNC* missense/in-frame variants, enriched in the **ROD2 domain (Ig-like repeats 16–23)**, which mediates sarcomere binding and signalling (PMID:32112656). Also reported in the N-terminal actin-binding domain (e.g., V123A) and the C-terminal rod (e.g., H2315N).
- **Variant-class modifier (the dominant genetic determinant of phenotype):** truncating vs non-truncating. Truncating *FLNC* variants were **absent from 1,078 HCM patients** in the largest genotype-phenotype study (PMID:27908349).
- **Oligogenic / second-hit:** co-occurring sarcomere-gene variants can modify severity; documented in families where *FLNC* co-segregates with e.g. *MYLK2*. Evidence is anecdotal, not systematic.
- **Founder effect:** *FLNC* **p.Trp2710Ter** observed "in 36 affected individuals across 6 Hong Kong Chinese families" (ClinGen HCM reappraisal, PMID:39132495) — note this is a *last-exon* nonsense variant that escapes NMD and behaves as an aggregate-former, i.e., mechanistically non-LOF.

### Environmental / lifestyle risk factors

No established environmental cause. As with all HCM, **high-intensity competitive exercise** is a recognised arrhythmic trigger and disease-expression modifier, and hemodynamic loading (hypertension, obesity) worsens hypertrophy. **Age is the strongest expressivity modifier** — penetrance in *FLNC* families is markedly age-dependent (see §9). No occupational or toxin exposure is implicated.

### Protective factors

None established genetically. No protective *FLNC* alleles have been reported. Environmental "protection" is limited to conventional cardiovascular risk-factor control and avoidance of arrhythmic triggers — i.e., tertiary prevention rather than true protection.

### Gene–environment interaction

Mechanistically plausible and worth curating as a **hypothesis**, not a fact: filamin C is the direct mechanosensor of the CASA (chaperone-assisted selective autophagy) pathway — "the CASA complex... senses the mechanical unfolding of the actin-crosslinking protein filamin. Contraction of the actin network results in the mechanical unfolding of protein domains within the filamin rods, leading to recognition by the CASA chaperone complex." A misfolding-prone filamin C variant therefore sits at the exact node where **mechanical load is transduced into proteostatic demand**, giving a direct molecular route by which exercise/afterload could accelerate aggregate accumulation. No human study has tested this directly. → Curate as `kind: KNOWLEDGE_GAP`.

---

## 3. Phenotypes

Frequencies below come from small, ascertainment-biased family series; treat all as **soft**. Where I cannot support a `FrequencyEnum` band with a quantitative source, I say so — per `docs/frequency-evidence-guidelines.md`, omit rather than fabricate.

### Cardiac — core

| Phenotype | HPO (verified) | Frequency / notes | Source |
|---|---|---|---|
| Hypertrophic cardiomyopathy | **HP:0001639** | Defining feature | PMID:25351925 |
| Left ventricular hypertrophy | **HP:0001712** | Defining; often mild/moderate, concentric | PMID:28356264 |
| Concentric hypertrophic cardiomyopathy | **HP:0005157** | Common pattern | Heart Rhythm 2026 |
| Restrictive cardiomyopathy | **HP:0001723** | Substantial overlap; RCM5 is a MONDO synonym | PMID:26666891 |
| Left ventricular diastolic dysfunction | **HP:0025168** | "more severe diastolic dysfunction" in ECG-positive carriers | Heart Rhythm 2026 |
| Myocardial fibrosis (LGE on CMR) | **HP:0001685** | 67% in the truncating cohort; frequent but less quantified in missense HCM | PMID:27908349 |
| Congestive heart failure | **HP:0001635** | Frequent; driver of transplant | PMID:26666891 |
| Left atrial enlargement | **HP:0031295** | Secondary to diastolic dysfunction | MedGen HPO annotations |
| Mitral regurgitation | **HP:0001653** | Reported | MedGen |
| Cardiomegaly | **HP:0001640** | Variable | — |

### Cardiac — electrical / arrhythmic

| Phenotype | HPO | Notes |
|---|---|---|
| **Sudden cardiac death** | **HP:0001645** | The headline risk. "FLNC-mutated patients have higher incidence of sudden cardiac death" (PMID:25351925). In the truncating cohort: 40 SCD events across 21 of 28 families (PMID:27908349) |
| Ventricular arrhythmia | **HP:0004308** | 82% in truncating carriers (PMID:27908349) |
| Ventricular tachycardia | **HP:0004756** | — |
| Ventricular fibrillation | **HP:0001663** | — |
| Cardiac arrest | **HP:0001695** | — |
| Atrial fibrillation | **HP:0005110** | Listed in MedGen HPO set; incl. permanent AF |
| T-wave inversion | **HP:0010872** | **The distinctive feature** — a repolarization phenotype in 37% of *FLNC*-variant HCM/RCM vs 1.0% of control HCM |
| Abnormal QT interval | **HP:0031547** | Prolonged QTc listed in MedGen |
| Atrioventricular block | **HP:0001678** | MedGen |
| Bundle branch block | **HP:0011710** | Left BBB, left anterior fascicular block (MedGen) |
| Syncope | **HP:0001279** | — |
| Palpitations | **HP:0001962** | — |

### Symptoms (patient-reported)

Dyspnea **HP:0002094**; chest pain **HP:0100749**; exercise intolerance **HP:0003546**; syncope **HP:0001279**.

### Extracardiac — musculoskeletal (a discriminating feature)

The 2026 Heart Rhythm study reports **musculoskeletal abnormalities in 4 of 12 (33%) ECG-positive families**. This is a genuine differentiator from sarcomeric HCM and should be curated as a phenotype category. Because *FLNC* also causes myofibrillar myopathy-5 and distal myopathy-4, overlap features include:

- Muscle weakness **HP:0001324**; distal muscle weakness **HP:0002460**; proximal muscle weakness **HP:0003701**
- Elevated circulating creatine kinase **HP:0003236** / mildly elevated CK **HP:0008180**
- Flexion contracture **HP:0001371**; scoliosis **HP:0002650**

Important counterpoint for the truncating arm: *"Clinical skeletal myopathy was not observed"* in the 28 truncating-variant families (PMID:27908349) — i.e., overt myopathy tracks with the aggregate-forming (non-LOF) mechanism, consistent with CMH26.

### Other reported

Stroke (thromboembolic, AF-related) — MedGen lists "stroke disorder."

### Onset, severity, progression

- **Onset:** predominantly adult; wide range. Aggregate-forming missense variants can present in childhood/infancy with RCM (severe end); classic CMH26 families present in the 3rd–6th decades.
- **Severity:** highly variable, even within a family. Gómez et al. found *"Most of the FLNC variants were associated with mild forms of HCM and a reduced penetrance"* (PMID:28356264) — directly contradicting a uniformly malignant picture.
- **Progression:** chronic, progressive. Restrictive physiology and diastolic failure drive the course; a subset progresses to end-stage heart failure requiring transplant (PMID:26666891). Arrhythmic risk is present throughout, not only at end stage.

### Quality-of-life impact

No CMH26-specific QoL data exist. Extrapolating from HCM generally: exertional dyspnea and exercise restriction dominate; ICD carriers experience anxiety and shock-related distress; the restrictive subphenotype carries a worse functional burden than obstructive HCM at equivalent wall thickness. **Flag as a data gap — do not populate numeric QoL values.**

---

## 4. Genetic / Molecular Information

### Causal gene

***FLNC*** — filamin C (gamma). HGNC:3756 (repo casing: `hgnc:3756`). Cytoband **7q32.1**. OMIM \*102565. UniProt **Q14315**. 48 exons; **2,725 aa** protein.

**Domain architecture (UniProt Q14315, verified):** two N-terminal **calponin-homology (CH1/CH2) actin-binding domains**, followed by **24 immunoglobulin-like (Ig) repeats** with intervening hinges. Functional partition: **ROD1 = Ig 1–15**, **ROD2 = Ig 16–23**, **Ig24 = the dimerization domain**. A muscle-specific **intradomain insert (residues 2162–2243) within Ig20 directs Z-line targeting**.

### Pathogenic variants

**Variant classes and the genotype–phenotype rule (the single most important curation fact):**

Verdonschot et al. (PMID:32112656) state it directly — truncating variants causing **reduced protein dosage** produce DCM with arrhythmias; **missense variants disrupting dimerization and folding** trigger aggregate accumulation, manifesting as **HCM or myofibrillar myopathy**; and **HCM-associated variants cluster predominantly in the ROD2 domain**.

**Representative CMH26 variants:**

| Variant | Domain | Phenotype | Functional evidence |
|---|---|---|---|
| **p.Ala1539Thr (A1539T)** | ROD1/ROD2 boundary | HCM, Spanish 4-generation family | Large perinuclear filamin C aggregates in rat neonatal cardiomyocytes and mouse myoblasts (PMID:25351925) |
| **p.His2315Asn (H2315N)** | C-terminal rod (ROD2) | HCM, 3 affected Spanish siblings | Segregation (OMIM 102565) |
| **p.Val123Ala (V123A)** | N-terminal actin-binding domain | HCM | Reported allelic variant; *functional data not independently verified in this search* |
| **p.Ser1624Leu (S1624L)** | Ig repeat | Familial RCM (AD) | *"Histopathology of heart tissue... showed cytoplasmic inclusions suggesting protein aggregates, which were filamin-C specific for the p.S1624L by immunohistochemistry"* (PMID:26666891) |
| **p.Ile2160Phe (I2160F)** | Ig20 region | Familial RCM (AD) | Segregation + aggregates (PMID:26666891) |
| **p.Val2264Met (V2264M)** | Ig20, ROD2 | RCM | iPSC-CM: Z-disk expansion, sarcomeric disorganization, aggregation (PMID:39315490) |
| **p.Trp2710Ter (W2710X)** | Ig24 dimerization domain | MFM5 ± cardiac; HK Chinese founder | *Last-exon* nonsense → escapes NMD → improper folding, cannot dimerize, abnormal aggregation. Mechanistically **non-LOF** |
| **p.Arg1267Gln (R1267Q)** | Ig11, ROD1 | Arrhythmogenic CM (contrast case) | Severe Ca²⁺ and Naᵥ1.5 dysfunction; haploinsufficiency-like (PMID:39315490) |

**Classification (ACMG/AMP):** *FLNC* missense variant interpretation is difficult. Gómez et al. found 20 candidate variants in 22 of 448 HCM patients, of which only **6 (in 7 patients) were finally classified as likely pathogenic, 10 as VUS, and 4 as likely benign** (PMID:28356264). Expect a high VUS rate. Domain location (ROD2), demonstrated aggregation, and family segregation are the strongest supporting lines.

**Allele frequency / population data:** *FLNC* tolerates a substantial burden of rare missense variation in the general population, which is exactly why burden analysis matters. Cui et al. found *FLNC* mutations in **7.22% of HCM patients vs 4.23% of controls (p = 0.101, not significant)**, concluding "FLNC mutation was found to be very common in both the healthy population and HCM patients... and generally FLNC mutation does not cause HCM" (Mol Genet Genomic Med 2018, doi:10.1002/mgg3.488). The 2026 Heart Rhythm burden analysis against 122,348 gnomAD controls quantified this as an **etiologic fraction of 0.45 (95% CI 0.36–0.54)** for unselected HCM. *I was unable to retrieve gnomAD's numeric pLI/LOEUF/missense-Z for FLNC — do not populate those fields without direct lookup.*

**Somatic vs germline:** exclusively **germline**. No somatic role.

**Functional consequence:** for CMH26, the mechanism is **not simple loss of function**. It is a **toxic gain-of-function / dominant-negative proteinopathy** — misfolded filamin C that cannot dimerize normally, aggregates, sequesters binding partners, and overwhelms Z-disc protein turnover. This is the mechanistic dividing line from truncating-*FLNC* DCM/ACM (haploinsufficiency).

### Modifier genes

No validated modifier loci. Candidate modifiers on mechanistic grounds (untested): ***BAG3***, ***HSPB8***, ***HSPB7***, ***CRYAB***, ***STUB1/CHIP***, ***SQSTM1*** — all CASA/proteostasis components whose own variants cause overlapping myofibrillar myopathy/cardiomyopathy. Curate as hypothesis.

### Epigenetics

No *FLNC*-specific methylation or chromatin data. Not applicable.

### Chromosomal abnormalities

Not a mechanism in CMH26. **Technical caveat with real clinical consequence:** *"FLNC has a pseudogene located 53.6kb downstream from the functional FLNC gene, and exons 46, 47, and 48 are 98% homologous in the functional and pseudogene"* (ClinGen HCM reappraisal, PMID:39132495) — short-read NGS can mis-map reads in this region, producing false positives/negatives. This belongs in the diagnostics section of the entry.

---

## 5. Environmental Information

- **Environmental factors:** none causal. No toxin, radiation, pollutant, or occupational exposure is implicated.
- **Lifestyle factors:** high-intensity competitive athletics is an arrhythmic trigger in HCM broadly; hypertension and obesity aggravate hypertrophy. **Modifiers of expression, not causes.**
- **Infectious agents:** not applicable.

---

## 6. Mechanism / Pathophysiology

### The causal chain (proposed pathograph for the KB)

```
[MOLECULAR] FLNC non-truncating variant (ROD2-clustered missense / in-frame del)
    ↓
[MOLECULAR] Filamin C misfolding and impaired Ig24-mediated homodimerization
    ↓
[MOLECULAR] Filamin C aggregate formation (cytoplasmic/perinuclear inclusions)
    ↓
[CELLULAR] Sequestration of Z-disc binding partners (desmin, myotilin, myozenin, ZASP, BAG3)
    ↓
[CELLULAR] Impaired Z-disc protein turnover → proteotoxic stress
    ↓
[CELLULAR] Lysosomal biogenesis (TFEB nuclear translocation) + enhanced autophagic flux
    ↓
[CELLULAR] Sarcomeric disarray, Z-disc misalignment, Z-disk expansion
    ↓
[TISSUE]   Myocyte disarray + interstitial/replacement myocardial fibrosis
    ↓
[TISSUE]   Increased myocardial stiffness; LV hypertrophy WITHOUT hypercontractility
    ↓
[ORGANISM] Diastolic dysfunction / restrictive physiology → heart failure
[ORGANISM] Fibrotic + structurally disorganized substrate → reentrant ventricular arrhythmia → SCD
```

### Molecular pathways

- **Actin cytoskeletal cross-linking / Z-disc assembly** — GO:0051015 actin filament binding; GO:0051764 actin crosslink formation; GO:0045214 sarcomere organization; GO:0030239 myofibril assembly; GO:0051260 protein homooligomerization (dimerization).
- **Chaperone-assisted selective autophagy (CASA)** — the central pathway. HSPA8 (Hsc70) + HSPB8 + BAG3 recognize mechanically unfolded filamin rod domains; *"BAG3 cooperates with the HSPA8-associated ubiquitin ligase STUB1/CHIP and its partner UBE2D in the ubiquitination of chaperone-bound FLNC. This provides a signal for the recruitment of the autophagic ubiquitin receptor SQSTM1."* GO:0006914 autophagy; GO:0016236 macroautophagy; GO:0061684 chaperone-mediated autophagy; GO:0006511 ubiquitin-dependent protein catabolic process; GO:0034620 cellular response to unfolded protein.
- **Mechanotransduction** — GO:0009612 response to mechanical stimulus. Filamin C is the mechanosensor itself, not merely a structural strut.
- **Lysosomal biogenesis / TFEB axis** — GO:0005764 lysosome. Directly demonstrated in isogenic hiPSC-CMs.
- **Cardiac hypertrophic signalling** — GO:0003300 cardiac muscle hypertrophy (downstream/secondary).
- **Ion handling (variant-specific)** — Naᵥ1.5 kinetics and Ca²⁺ transient disturbance shown for R1267Q > V2264M in patient iPSC-CMs (PMID:39315490); relevant to the arrhythmic arm.

### Definitive mechanistic experiment (the key citation for the entry)

Agarwal et al., *Circ Res* 2021 (**PMID:34405687**) — isogenic CRISPR hiPSC-CM series. Verbatim conclusions:

> "FLNC expression is required for sarcomere organization and physiologic function. Variants that produce misfolded FLNC proteins cause the accumulation of FLNC and FLNC binding partners which leads to increased lysosome expression and activation of autophagic pathways. Surprisingly, similar pathways were activated in FLNC haploinsufficient hiPSC-CMs, likely initiated by the loss of stoichiometric FLNC protein interactions and impaired turnover of proteins at the Z-disc. These results indicate that both FLNC haploinsufficient variants and variants that produce misfolded FLNC protein cause disease by similar proteotoxic mechanisms, and indicate the therapeutic potential for augmenting protein degradative pathways to treat a wide range of FLNC-related cardiomyopathies."

And on the HCM-relevant arm specifically:

> "We also studied a heterozygous in-frame deletion (FLNC+/∆7aa) which did not affect FLNC expression but caused aggregate formation, similar to FLNC variants associated with hypertrophic cardiomyopathy (HCM). FLNC−/− hiPSC-CMs demonstrated profound sarcomere misassembly and reduced contractility. While sarcomere formation and function were unaffected in FLNC+/− and FLNC+/∆7aa hiPSC-CMs, these heterozygous variants caused increases in lysosome content, enhancement of autophagic flux, and accumulation of FLNC-binding partners and Z-disc proteins."

This is a **mechanistically important nuance**: in heterozygous (i.e., patient-realistic) cells, sarcomere structure and contractile function were *preserved* — the primary lesion is **proteostatic, not contractile**. That aligns strikingly with the 2026 clinical finding of hypertrophy **without hypercontractility**, and argues against a myosin-hyperactivity model for CMH26.

### Protein dysfunction

Misfolding of Ig-like rod repeats; loss of Ig24-mediated homodimerization (canonical for W2710X: *"the W2710X protein had improper folding, was unable to form dimers, and showed abnormal aggregation"*); formation of insoluble aggregates enriched in FLNC, **desmin**, and multiple binding partners (Agarwal 2021). Note the inversion in the truncating arm: *"Immunohistochemical staining of myocardial tissue showed no abnormal filamin C aggregates in patients with truncating FLNC mutations"* (PMID:27908349) — aggregates are the CMH26/MFM signature specifically.

### Metabolic changes

No primary metabolic defect. Secondary: energetic inefficiency of hypertrophied, fibrotic myocardium; increased autophagic/lysosomal degradative load. Not a metabolic disease.

### Immune system involvement

None primary. No autoimmune or immunodeficiency component. Low-grade sterile inflammation may accompany fibrotic remodelling (generic, not *FLNC*-specific).

### Tissue damage mechanisms

Myocyte disarray, Z-disc disruption, myocyte loss with replacement fibrosis (HP:0001685; LGE-positive on CMR), electrical anisotropy from the fibrotic substrate. Mouse work adds direct biomechanical data: FLNC loss "reduced systolic force development in single cardiomyocytes and isolated papillary muscles but did not affect twitch kinetics or calcium transients," with "significant defects in Z-disk alignment and altered myofilament lattice geometry" (Int J Mol Sci 2022;23:871, PMC8779483).

### Biochemical abnormalities

Filamin C aggregation (loss of solubility); disrupted stoichiometry of the Z-disc interactome; elevated lysosomal protein content; depletion of ATG5/ATG7/BECN1 (consistent with increased autophagic consumption); accumulation of Z-disc proteins in total lysate despite enhanced flux — i.e., **degradation cannot keep pace with damaged-protein production**.

### Epigenetic changes

None reported for CMH26. Data gap.

### Molecular profiling

- **Transcriptomics:** *FLNC*⁻/⁻ hiPSC-CMs show reduced thin-filament gene expression (PMID:34405687). Patient-specific iPSC-CM RNA-seq shows variant-specific transcriptome shifts in action-potential/sodium-transport and structural cardiomyocyte genes (PMID:39315490).
- **Proteomics:** aggregate composition profiling (FLNC, desmin, myotilin, binding partners) — Agarwal 2021 and the W2710X homozygous-expression study (PMC7650280).
- **Metabolomics / lipidomics:** no CMH26-specific data. Gap.
- **Single-cell / spatial:** no *FLNC*-cardiomyopathy-specific single-cell or spatial atlas identified. Gap — a good `KNOWLEDGE_GAP` entry.
- **Functional genomics screens:** no *FLNC*-focused CRISPR/RNAi screen identified; isogenic CRISPR hiPSC-CM series (Agarwal) is the closest.

---

## 7. Anatomical Structures Affected

### Organ level
- **Primary:** heart — **UBERON:0000948**; specifically myocardium **UBERON:0002349**, left ventricle myocardium **UBERON:0006566**, interventricular septum **UBERON:0002094**, cardiac ventricle **UBERON:0002082**.
- **Secondary:** cardiac atrium **UBERON:0002081** (atrial enlargement/AF, secondary to diastolic dysfunction); systemic/pulmonary venous congestion in heart failure; brain (cardioembolic stroke, secondary to AF).
- **Extracardiac primary (variant-dependent):** skeletal muscle tissue **UBERON:0001134** — myopathic/musculoskeletal involvement in ~33% of ECG-positive *FLNC* HCM families.
- **Body systems:** cardiovascular (primary), musculoskeletal (secondary/overlap).

### Tissue and cell level
- **Cardiac muscle cell — CL:0000746** (primary target)
- **Regular ventricular cardiac myocyte — CL:0002131**
- **Fibroblast of cardiac tissue — CL:0002548** (fibrotic remodelling effector)
- **Skeletal muscle fiber — CL:0008002** (filaminopathy overlap)

### Subcellular level
- **Z disc — GO:0030018** (the primary lesion site)
- **Sarcolemma — GO:0042383**; **costamere — GO:0043034**; **intercalated disc — GO:0014704** (filamin C's normal localisation set, per UniProt: "myofibrillar Z-discs... with minor amounts at the sarcolemma")
- **Inclusion body — GO:0016234** (the pathological structure)
- **Lysosome — GO:0005764** (expanded compartment)

### Localization / lateralization
Bilateral/global myocardial involvement. Hypertrophy is typically **concentric** in *FLNC* HCM with a characteristically **small LV cavity** — distinguishing it from the asymmetric septal hypertrophy typical of *MYH7*/*MYBPC3* disease. Skeletal involvement, when present, follows the distal-predominant filaminopathy pattern.

---

## 8. Temporal Development

- **Onset:** predominantly **adult** (3rd–6th decade) for the classic CMH26 HCM presentation. Aggregate-forming missense variants presenting as RCM can manifest in **childhood or infancy**, sometimes requiring early transplant. Congenital presentation occurs only with biallelic *FLNC* variants (a distinct, severe, non-CMH26 entity).
- **Onset pattern:** **insidious/chronic**. Frequently detected on family cascade screening or incidental ECG before symptoms.
- **Stages:** (i) genotype-positive/phenotype-negative; (ii) ECG abnormality without overt hypertrophy — *this is the notable early marker in FLNC disease*; (iii) established hypertrophy with preserved systolic function and progressive diastolic impairment; (iv) restrictive physiology with heart failure; (v) end-stage requiring transplant. Arrhythmic risk is **not confined to late stages** — SCD can be the presenting event.
- **Progression rate:** slow to moderate, highly variable between and within families.
- **Course pattern:** **progressive** and lifelong, punctuated by episodic arrhythmic events.
- **Duration:** chronic, lifelong. No spontaneous remission. "Remission" is only treatment-induced symptom control or, definitively, transplantation.
- **Critical periods:** (a) adolescence/early adulthood — when screening should begin and competitive-sport counselling matters; (b) age >40 — penetrance rises steeply, making continued surveillance of genotype-positive relatives essential; (c) first detection of restrictive physiology or LGE — the window for ICD decision-making.

---

## 9. Inheritance and Population

### Epidemiology

No CMH26-specific prevalence figure exists. Derive it:

- HCM overall affects **~1 in 500** clinically ascertained, with genotype-based estimates as high as ~1 in 200 (≈200–500 per 100,000).
- *FLNC* candidate variants were found in **22 of 448 HCM patients (4.9%)**, but only **7 of 448 (1.6%)** carried variants finally classified likely pathogenic (PMID:28356264).
- Applying the ~1.6% likely-pathogenic yield to a 1/500 HCM prevalence gives an order-of-magnitude CMH26 point prevalence of **~3 per 100,000** — i.e., Orphanet band **BAND_1_9_PER_100000**. **This is a derived estimate, not a published one; label it as such in `notes:`.**
- Incidence: not established.

### Inheritance

- **Autosomal dominant** (HP:0000006). Truncating *FLNC* variants cosegregate with a **combined LOD score of 9.5** (PMID:27908349); CMH26 missense families likewise segregate dominantly.
- **Penetrance: incomplete and strongly age-dependent.** In the founding CMH26 families, **14 of 16 carriers over 40 years of age were symptomatic (>87% penetrance)**. In the truncating cohort, *"Penetrance was >97% in carriers older than 40 years"* (PMID:27908349). But Gómez et al. describe *"a reduced penetrance, with few affected in the families to confirm the segregation"* (PMID:28356264) — penetrance in unselected missense carriers is materially lower than in intensively ascertained families. **Curate both; do not average them.**
- **Expressivity: highly variable** — the same variant can produce HCM, RCM, isolated ECG abnormality, or myopathy in different relatives.
- **Genetic anticipation:** not applicable (no repeat expansion). Do not assert.
- **Germline mosaicism:** not reported for *FLNC*. Gap.
- **Founder effects:** *FLNC* p.Trp2710Ter in Hong Kong Chinese families (6 families, 36 affected). Spanish families dominate the original CMH26 literature (ascertainment, not necessarily a founder effect).
- **Consanguinity:** irrelevant for dominant CMH26; relevant only for the rare biallelic congenital DCM form.
- **Carrier frequency:** not applicable (dominant). Relevant metric is population frequency of rare *FLNC* missense variants, which is non-trivial — precisely the reason for the low etiologic fraction.

### Population demographics

- **Affected populations:** reported worldwide — Spanish, Dutch, Italian, UK, Chinese (mainland and Hong Kong), Russian, North American cohorts. No ethnic group is known to be disproportionately affected beyond the HK Chinese founder variant.
- **Geographic distribution:** cosmopolitan.
- **Sex ratio:** no established sex bias for CMH26. (One *Flnc*-deficiency mouse study specifically examined male mice; do not over-read this into human sex distribution.)
- **Age distribution:** peak clinical recognition in adulthood; markedly skewed to >40 years by penetrance.

---

## 10. Diagnostics

### Imaging and functional testing
- **Transthoracic echocardiography** — LVH, **small LV cavity**, diastolic dysfunction, atrial enlargement, restrictive filling. Notably: *FLNC* carriers with the characteristic ECG "had smaller left ventricular cavity size, lower contractility, and more severe diastolic dysfunction and were more likely to have a restrictive phenotype" (Heart Rhythm 2026). **The absence of hypercontractility is itself a diagnostic clue.**
- **Cardiac MRI with LGE** — myocardial fibrosis quantification (HP:0001685); central to arrhythmic risk stratification and to distinguishing *FLNC* from sarcomeric HCM.
- **12-lead ECG** — carries the highest-yield discriminating signal (below).
- **Ambulatory ECG / Holter, exercise testing** — NSVT detection for SCD risk stratification.
- **Electrophysiology study** — selected cases.

### The distinctive ECG (the most actionable diagnostic finding)

A **distinct repolarization phenotype** was present in **37% (19/51 individuals from 12 families)** of *FLNC*-variant HCM/RCM patients vs **1.0% (2/197)** of a control HCM cohort. Its discriminative power is quantified by the etiologic-fraction split: **0.45 (95% CI 0.36–0.54) across all HCM cases vs 0.98 (95% CI 0.97–0.99) in "ECG-positive" cases** (Heart Rhythm 2026, PII S1547-5271(26)00121-9).

**Curation implication:** this is an excellent candidate for a `definitions[]` entry with `definition_type: PHENOTYPE_ALGORITHM` and `derivation_basis: ESTABLISHED_CRITERIA` (or `MECHANISTIC_HYPOTHESIS` if framed prospectively), `validation_status.status: UNVALIDATED`, `attaches_to` the repolarization/fibrosis node — an ECG-first case-finding rule that raises *FLNC* missense PPV from ~45% to ~98%.

### Laboratory
- **Creatine kinase** (LOINC 2157-6) — screen for skeletal-muscle involvement; HP:0003236 / HP:0008180.
- **NT-proBNP / BNP** — heart-failure severity; HP:0033534 increased circulating brain natriuretic peptide concentration.
- **Troponin** — nonspecific.

### Biopsy / histopathology
Endomyocardial biopsy is not routine but is diagnostically decisive when performed: **cytoplasmic inclusions consistent with protein aggregates, filamin-C-positive by immunohistochemistry** (PMID:26666891). Skeletal muscle biopsy in overlap cases shows myofibrillar myopathy features (Z-disc-derived sarcomeric lesions, desmin/filamin C accumulation). **The aggregate finding is the pathognomonic feature separating CMH26 from truncating-*FLNC* disease**, where aggregates are absent (PMID:27908349).

### Genetic testing

- **Recommended approach:** multigene **cardiomyopathy NGS panel including *FLNC***. *FLNC* is now standard on comprehensive HCM/DCM/ACM panels; it was historically absent, and pre-2014 negative panels should be reflexed.
- **WES/WGS:** valuable for atypical/syndromic presentations and originally how CMH26 was discovered. WGS additionally resolves the pseudogene-homologous region better than short-read exome capture.
- **Single-gene testing:** appropriate only for **cascade/predictive testing** of relatives once a familial variant is known.
- **CMA / karyotype / FISH / mtDNA / repeat-expansion testing:** **not indicated** for CMH26.
- **Critical technical caveat:** the 53.6 kb-downstream *FLNC* pseudogene with **98% homology across exons 46–48** creates a real mis-mapping hazard — variants in those exons should be orthogonally confirmed (long-read or Sanger with gene-specific primers).
- **Interpretation caution:** given the ~45% etiologic fraction, **a rare *FLNC* missense variant in HCM should not be treated as causal by default.** Weight ROD2 location, the characteristic ECG, restrictive physiology, extracardiac features, aggregate histology, and segregation.

### Clinical criteria and differential diagnosis

Diagnosis of HCM follows the **2023 ESC cardiomyopathy guidelines** and the **2024 AHA/ACC HCM guideline**: LV wall thickness ≥15 mm (or ≥13 mm with family history/genotype) unexplained by loading conditions.

**Differential diagnosis with distinguishing features:**

| Condition | Distinguishing feature |
|---|---|
| Sarcomeric HCM (*MYH7*, *MYBPC3*) | Asymmetric septal hypertrophy, LVOT obstruction, **hypercontractility**; no characteristic repolarization ECG; no aggregates |
| Cardiac amyloidosis (ATTR/AL) | Low-voltage ECG, apical sparing strain, positive PYP/DPD scintigraphy or biopsy Congo red |
| Fabry disease (*GLA*) | Low native T1 on CMR, short PR, neuropathic pain, α-Gal A deficiency |
| Danon disease (*LAMP2*) | WPW pre-excitation, X-linked, marked LVH, intellectual disability |
| *PRKAG2* glycogen storage cardiomyopathy | Pre-excitation, conduction disease |
| Noonan/RASopathy | Dysmorphology, pulmonary valve stenosis, short stature |
| Truncating-*FLNC* DCM/ACM | Dilated LV, systolic dysfunction, low QRS voltage + inferolateral TWI, **no aggregates** |
| Desminopathy (*DES*) / *BAG3* myofibrillar myopathy | Overlapping aggregate pathology — the closest mechanistic mimic |
| Athlete's heart | Normal/supranormal diastolic function, regression on detraining |

### Screening
**Cascade genetic testing** of first-degree relatives is the cornerstone, with clinical screening (ECG + echo) of genotype-positive relatives. **Given age-dependent penetrance, genotype-positive/phenotype-negative relatives require lifelong periodic surveillance** — a negative echo in youth does not discharge them. No newborn or population screening exists or is indicated.

---

## 11. Outcome / Prognosis

### Survival and mortality
No CMH26-specific survival curves exist. Available anchors:

- Elevated SCD risk is the founding observation: *"Clinical studies indicate that FLNC-mutated patients have higher incidence of sudden cardiac death"* (PMID:25351925).
- In the ECG-positive *FLNC* HCM/RCM group, **heart failure death, transplant, or cardiac arrest occurred in at least one individual in 7 of 12 families (58%)** (Heart Rhythm 2026).
- For contrast (the truncating arm, **not** CMH26): 40 SCD events across 21 of 28 families, ventricular arrhythmias in 82% (PMID:27908349).
- Counterweight: *"Most of the FLNC variants were associated with mild forms of HCM"* (PMID:28356264).

**Net reading:** *FLNC*-related HCM/RCM appears to carry above-average risk relative to sarcomeric HCM, driven by both arrhythmia and diastolic heart failure — but the risk is concentrated in the ECG-positive/restrictive subgroup, and unselected *FLNC* missense carriers may do well. Do not populate a single global mortality figure.

### Morbidity and function
Progressive exertional limitation from diastolic dysfunction; heart failure hospitalizations; AF with stroke risk; ICD-related morbidity (inappropriate shocks, lead complications, psychological burden). Where restrictive physiology dominates, functional limitation is disproportionate to wall thickness.

### Complications
Sudden cardiac death; sustained VT/VF; progressive heart failure to end stage; atrial fibrillation; cardioembolic stroke; conduction disease requiring pacing; in overlap cases, progressive skeletal myopathy.

### Recovery potential
None spontaneously. Structural damage (fibrosis, aggregates) is irreversible with current therapy. **Cardiac transplantation is the only definitive intervention** for end-stage disease and is well documented in *FLNC* RCM: patients "presented with heart failure due to severe diastolic dysfunction requiring heart transplantation in some cases" (PMID:26666891).

### Prognostic factors
Adverse: the characteristic repolarization ECG; restrictive physiology with small LV cavity; extensive LGE/myocardial fibrosis; NSVT; unexplained syncope; family history of SCD; falling ejection fraction; age >40 (penetrance and event accrual).

### Prognostic biomarkers
LGE burden on CMR is the best-supported imaging biomarker. NT-proBNP tracks heart-failure severity. **No validated *FLNC*-specific molecular prognostic biomarker exists** — a genuine gap. Aggregate burden on biopsy is diagnostic, not validated as prognostic.

---

## 12. Treatment

**There is no disease-modifying therapy for CMH26.** Management is symptom-directed plus SCD prevention, per general HCM/cardiomyopathy guidelines, with two *FLNC*-specific modifications.

### Pharmacotherapy

| Treatment | NCIT (verified) | CHEBI (verified) | Notes |
|---|---|---|---|
| Beta-blocker (e.g. metoprolol) | Pharmacotherapy **NCIT:C15986** + agent **NCIT:C29576** Beta-Adrenergic Antagonist | metoprolol **CHEBI:6904** | First-line for symptoms; rate control aids diastolic filling |
| Non-dihydropyridine CCB (verapamil) | **NCIT:C15986** + **NCIT:C333** Calcium Channel Blocker | verapamil **CHEBI:9948** | Alternative; caution in restrictive physiology/low output |
| Disopyramide | **NCIT:C15986** + **NCIT:C61730** Disopyramide | disopyramide **CHEBI:4657** | For obstruction — **rarely relevant in CMH26**, which is typically non-obstructive |
| Amiodarone | **NCIT:C15986** | amiodarone **CHEBI:2663** | Arrhythmia suppression |
| Anticoagulation (AF) | **NCIT:C15986** + **NCIT:C263** Anticoagulant Agent | — | Stroke prevention; low threshold in HCM with AF |
| Diuretics / HF therapy | **NCIT:C15986** | — | Congestion; use cautiously in restrictive physiology (preload-dependent) |
| **Mavacamten** | **NCIT:C15986** + **NCIT:C174901** Mavacamten | — | **Mechanistically questionable in CMH26.** Cardiac myosin inhibitors target hypercontractility; *FLNC* HCM is characterized by **lower contractility, not hypercontractility**, and hiPSC-CM work found heterozygous *FLNC* variants left contractile function unaffected. Curate with an explicit caveat — do not present as standard of care for this genotype. |

**Pharmacogenomics:** no *FLNC*-specific PGx. Standard CYP2D6-metoprolol and CYP2C9/VKORC1-warfarin considerations apply generically.

### Device and interventional

| Intervention | NCIT (verified) |
|---|---|
| **ICD implantation** (primary/secondary SCD prevention) | **NCIT:C80435** Implantable Cardioverter-Defibrillator Placement; device **NCIT:C93238** |
| Catheter ablation (AF, VT) | Therapeutic Procedure NCIT:C49236 |
| Pacemaker for conduction disease | — |
| Septal reduction (myectomy/alcohol ablation) | Surgical Procedure NCIT:C15329 — **seldom applicable**; CMH26 is usually non-obstructive |
| **Heart transplantation** | **NCIT:C15246** Heart Transplantation |
| Genetic counselling & cascade testing | **NCIT:C15240** Genetic Counseling |

**ICD threshold — the *FLNC*-specific modification.** The 2023 ESC cardiomyopathy guidelines treat *FLNC* as a **high-risk genotype**: when a patient with DCM/NDLVC carries a P/LP variant in a gene such as *FLNC* associated with SCD, an ICD "should be considered in primary prevention even with LVEF > 35% when there are additional risk factors" (Class IIa, LoE C), within a multiparametric framework (LVEF < 50% plus ≥2 of syncope, LGE on CMR, inducible sustained monomorphic VT at EPS, high-risk genotype). Ortiz-Genga et al. put it bluntly for the truncating arm: *"Prompt implantation of a cardiac defibrillator should be considered in affected patients harboring truncating mutations in FLNC."* **Note the scope boundary:** these recommendations are anchored to the DCM/ACM (truncating) arm. Whether they transfer to non-truncating CMH26 is not settled — curate as a `KNOWLEDGE_GAP`, not as established practice.

### Advanced / experimental therapeutics

- **Gene therapy:** no *FLNC* AAV programme in trials. **Important mechanistic caveat** — *FLNC* is a 2,725-aa protein whose ~8.2 kb coding sequence **exceeds AAV packaging capacity**, and for aggregate-forming (dominant-negative) CMH26 variants gene *addition* would not address the toxic species anyway. Allele-specific knockdown or base/prime editing is the theoretically appropriate modality; none is in development.
- **RNA-based therapy:** none for *FLNC*. Allele-specific ASO/siRNA silencing of the mutant allele is a rational but unpursued strategy.
- **Proteostasis augmentation — the most mechanistically grounded direction.** Agarwal et al. explicitly conclude their data "indicate the therapeutic potential for augmenting protein degradative pathways to treat a wide range of FLNC-related cardiomyopathies" (PMID:34405687). No clinical programme exists.
- **Adjacent precedent worth tracking:** AAV gene therapy for **BAG3**-associated DCM is in clinical development (**NCT07137338**, RP-A701, Rocket Pharmaceuticals, Phase 1; **NCT07426419**, AFTX-201, Affinia Therapeutics). BAG3 is filamin C's direct CASA co-chaperone partner, so these trials validate the pathway clinically even though they do not treat *FLNC* disease. Cite as pathway-adjacent, **not** as a CMH26 treatment.
- **Immunotherapy / cell therapy / targeted oncology-style agents:** not applicable.

### Supportive, rehabilitative, and lifestyle
Heart-failure supportive care (**NCIT:C15747**); exercise prescription with avoidance of high-intensity competitive sport; cardiac rehabilitation (**NCIT:C15315**) in stable HF; physical therapy (**NCIT:C15302**) where skeletal myopathy coexists; psychological support for ICD carriers.

### Treatment strategy summary
1. Confirm variant class (truncating vs non-truncating) — it changes both prognosis and the arrhythmia strategy.
2. Phenotype comprehensively: ECG (look for the repolarization signature), echo (cavity size, diastolic function, contractility), CMR with LGE, CK, and musculoskeletal exam.
3. Symptom control: beta-blocker first-line; careful diuresis; scrutinize myosin-inhibitor use.
4. Risk-stratify for SCD using a multiparametric model that upweights the *FLNC* genotype and LGE burden.
5. Cascade-test relatives; enroll genotype-positive relatives in lifelong surveillance.
6. Refer early to advanced HF/transplant when restrictive physiology emerges.

---

## 13. Prevention

- **Primary prevention (of the disease):** not possible — germline. Only **reproductive** options prevent transmission: preimplantation genetic testing for monogenic disease (PGT-M), prenatal diagnosis, donor gametes. Requires a confirmed P/LP familial variant, which is often unavailable given the high VUS rate.
- **Secondary prevention (early detection):** **cascade genetic testing** of first-degree relatives + ECG/echo surveillance of carriers. Because the ECG abnormality can precede overt hypertrophy, ECG is the highest-yield early screening modality in *FLNC* families. Surveillance intervals should follow HCM family-screening guidance (roughly 1–3 yearly in adolescence, 3–5 yearly in adults), continued indefinitely given age-dependent penetrance.
- **Tertiary prevention (of complications):** ICD for SCD; anticoagulation for AF-related stroke; guideline-directed HF therapy; competitive-sport restriction; timely transplant referral.
- **Immunization:** not applicable to disease pathogenesis. Routine influenza/COVID/pneumococcal vaccination is standard supportive care in heart failure.
- **Population screening:** not indicated. The low etiologic fraction of *FLNC* missense variants makes population-level *FLNC* screening actively harmful (VUS burden, overdiagnosis).
- **Genetic counselling (NCIT:C15240):** essential. Must cover 50% transmission risk, **incomplete age-dependent penetrance**, **highly variable expressivity**, the VUS problem, reproductive options, and the implications of a high-risk genotype for ICD decisions.
- **Public health / environmental interventions:** not applicable.
- **Prophylaxis:** ICD is the only true prophylactic intervention. No prophylactic pharmacotherapy prevents phenotype development in genotype-positive/phenotype-negative carriers — and none should be asserted.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** *Homo sapiens* **NCBITaxon:9606** (disease entity). Experimental species: *Mus musculus* **NCBITaxon:10090**, *Danio rerio* **NCBITaxon:7955**, *Rattus norvegicus* **NCBITaxon:10116** (neonatal cardiomyocyte transfection).
- **Breed (VBO):** not applicable — no breed-associated *FLNC* cardiomyopathy identified.
- **Orthologous genes:** mouse *Flnc* (NCBI Gene 68794); zebrafish has **two paralogs, *flnca* and *flncb*** (genome duplication), requiring double mutants to model human loss.
- **Natural disease in other species:** **I found no naturally occurring *FLNC*-associated cardiomyopathy in any non-human species.** A targeted OMIA search returned feline HCM entries for *MYBPC3* (OMIA:002951, OMIA:002952), *MYH7* (OMIA:002212), *ALMS1* (OMIA:002316), and *TNNT2* — but **no *FLNC* entry**. Feline HCM is the most important naturally occurring animal HCM model (reported incidence up to ~15% in some cat populations), but it is not *FLNC*-mediated. **State this explicitly as a negative finding in the KB rather than leaving the section empty.**
- **Veterinary relevance:** none established for *FLNC* specifically.
- **Comparative biology:** filamin C is highly conserved across vertebrates in domain architecture (CH1/CH2 + 24 Ig repeats) and in its Z-disc/CASA role; zebrafish double mutants and mouse conditional knockouts both reproduce Z-disc disruption, indicating deep conservation of the mechanism.
- **Zoonotic potential / cross-species transmission:** not applicable (genetic disease).

---

## 15. Model Organisms

### Mouse (*Mus musculus*, NCBITaxon:10090)

| Model | Design | Findings | Source |
|---|---|---|---|
| **Inducible cardiac-specific *Flnc* KO (icKO)** | *Flnc*^fl/fl × Myh6-MerCreMer; tamoxifen in adulthood | Rapid-onset DCM in adults with previously normal hearts. "Loss of FLNC reduced systolic force development in single cardiomyocytes and isolated papillary muscles but did not affect twitch kinetics or calcium transients." EM/IF: "significant defects in Z-disk alignment and altered myofilament lattice geometry" | Int J Mol Sci 2022;23:871 (PMC8779483) |
| **Constitutive *Flnc*⁻/⁻** | Germline null | Perinatal lethal with severe myogenesis and myotube defects; establishes filamin C as essential for muscle development | Dalkilic et al. (classic; *PMID not independently verified in this search*) |
| **Filamin C deficiency, myocardial integrity** | — | "Filamin C is essential for mammalian myocardial integrity" | PMC9907827 |
| **Reduced filamin C** | Partial reduction | "Reduction of Filamin C Results in Altered Proteostasis, Cardiomyopathy, and Arrhythmias" — links dosage reduction to both proteostatic disturbance and arrhythmia | J Am Heart Assoc 2023, doi:10.1161/JAHA.123.030467 (*full abstract not retrievable — publisher 403*) |
| **PDI involvement in *Flnc*-deficiency DCM (male mice)** | — | Protein disulfide isomerase implicated | PMC11915583 |

### Zebrafish (*Danio rerio*, NCBITaxon:7955)
Double *flnca*/*flncb* mutants: "The cardiac morphological phenotype of double flnc mutant embryos is characterized by decreased cardiac output and stroke volume, similar to what is observed in patients with cardiomyopathies. Double flnca and flncb mutant hearts exhibited irregular z-discs." Single mutants are largely unaffected — **paralog redundancy is the key experimental limitation.**

### Human iPSC-derived cardiomyocytes (the most human-relevant system)
- **Isogenic CRISPR series (WT / *FLNC*⁻/⁻ / *FLNC*⁺/⁻ / *FLNC*⁺/^∆7aa)** — the definitive mechanistic model, PMID:34405687. The ∆7aa in-frame deletion is the designed CMH26 analog (aggregate-forming without expression loss).
- **Patient-specific iPSC-CMs (R1267Q ACM vs V2264M RCM)** — variant-specific Ca²⁺ handling, Naᵥ1.5 kinetics, action potentials, transcriptomes (PMID:39315490).

### Cell lines / in vitro
Rat neonatal cardiomyocytes and mouse myoblasts transfected with A1539T — perinuclear filamin C aggregates (PMID:25351925). Myoblast lines expressing S1624L — cytoplasmic aggregates (PMID:26666891). Homozygous W2710X expression system for sarcomeric lesion pathomechanism (PMC7650280).

### Phenotype recapitulation and limitations — **curate as `HUMAN_MODEL_MISMATCH`, not `KNOWLEDGE_GAP`**

This is a textbook case of the distinction the schema draws:

- **Mouse and zebrafish *Flnc* loss-of-function models produce DCM and Z-disc disruption, not hypertrophic cardiomyopathy.** They model the **truncating/haploinsufficiency arm** (DCM/ACM) — *not* CMH26. Using them as evidence for CMH26 pathophysiology is a category error.
- **No mouse knock-in of a human CMH26 missense variant (A1539T, H2315N) reproducing an HCM phenotype was identified in this search.** This is the single biggest model gap for the entry.
- Zebrafish paralog redundancy (*flnca* + *flncb*) requires double mutants, distancing the model from human heterozygous dominant disease.
- hiPSC-CMs are immature (fetal-like sarcomeres, altered Ca²⁺ handling, no true diastolic loading) and cannot model restrictive physiology, fibrosis, or arrhythmic reentry — precisely the features that define the clinical CMH26 phenotype.

Suggested `proposed_experiments`: (1) knock-in mouse carrying a ROD2 CMH26 missense variant with longitudinal echo/ECG phenotyping; (2) engineered heart tissue from CMH26-variant hiPSC-CMs under physiological load to test whether mechanical stress accelerates aggregation; (3) proteostasis-augmentation intervention (TFEB activation or CASA enhancement) in that system.

### Model resources
MGI (*Flnc*, MGI:95557), IMPC/KOMP, ZFIN (*flnca*, *flncb*), Alliance of Genome Resources, Cellosaurus/hPSCreg for the iPSC lines, IMSR/MMRRC for mouse strain sourcing.

---

## Curation Recommendations for the dismech Entry

1. **Replace the placeholder pathophysiology node** with the 9-node causal chain in §6, tagging `biological_scale` per node (MOLECULAR → CELLULAR → TISSUE → ORGANISM as annotated).
2. **Add `mechanistic_hypotheses`** with two groups: `flnc_proteotoxic_aggregation` (status: canonical/established) and `flnc_mechanical_load_accelerates_aggregation` (status: EMERGING).
3. **Add a `discussions` entry** `kind: HUMAN_MODEL_MISMATCH` for the mouse/zebrafish LOF-models-DCM-not-HCM problem (§15).
4. **Add a `discussions` entry** `kind: KNOWLEDGE_GAP` for the contested etiologic fraction — the Cui 2018 null result should be curated as `supports: REFUTE` or `PARTIAL` evidence against a simple *FLNC*→HCM causal claim.
5. **Consider a `definitions[]` PHENOTYPE_ALGORITHM** for the ECG-first case-finding rule (§10), with `validation_status.status: UNVALIDATED` and the 0.45→0.98 etiologic-fraction shift as its rationale.
6. **Consider `conforms_to`** against `cardiomyopathy_maladaptive_remodeling#Ventricular Remodeling`. Note that `cardiac_ion_channel_repolarization` is **not** an appropriate module here — CMH26 is a structural/proteostatic cardiomyopathy, and the ECG repolarization signature is a downstream marker of the structural substrate, not a primary channelopathy.
7. **A new module is arguably warranted**: `z_disc_proteostasis_aggregation` (or extending an existing proteinopathy module) — the CASA/BAG3/HSPB8/filamin C axis recurs across *FLNC*, *DES*, *BAG3*, *CRYAB*, and *MYOT* myofibrillar myopathies and cardiomyopathies. That is exactly the "conserved pathological process recurring across multiple disorders" the module system exists for.
8. **Before committing any evidence item, run `just fetch-reference PMID:XXXX` and `just validate-references`.** The verbatim abstract text quoted above came from web fetches, not from the sanctioned cache layer — it must be re-verified against `references_cache/` before it lands in YAML.
9. **NEC preflight is not required here** — the MONDO record was verified locally by OAK, and the gene (*FLNC*), OMIM xref (617047), and synonyms all align. Note only that MONDO folds "cardiomyopathy, familial restrictive 5" into this entity, which is a lumping decision worth recording in the entry's notes.

---

## Sources

- [OMIM #617047 — Cardiomyopathy, Familial Hypertrophic, 26 (CMH26)](https://omim.org/entry/617047) *(full text returned HTTP 403; content accessed via MedGen/MONDO/secondary sources)*
- [OMIM \*102565 — Filamin C; FLNC](https://omim.org/entry/102565)
- [MedGen: Hypertrophic cardiomyopathy 26 (C4310749)](https://www.ncbi.nlm.nih.gov/medgen/934716)
- [Valdés-Mas R et al. Mutations in filamin C cause a new form of familial hypertrophic cardiomyopathy. Nat Commun 2014;5:5326. PMID:25351925](https://pubmed.ncbi.nlm.nih.gov/25351925/)
- [Gómez J et al. Screening of the Filamin C Gene in a Large Cohort of Hypertrophic Cardiomyopathy Patients. Circ Cardiovasc Genet 2017;10(2):e001584. PMID:28356264](https://pubmed.ncbi.nlm.nih.gov/28356264/)
- [Ortiz-Genga MF et al. Truncating FLNC Mutations Are Associated With High-Risk Dilated and Arrhythmogenic Cardiomyopathies. J Am Coll Cardiol 2016;68(22):2440-51. PMID:27908349](https://pubmed.ncbi.nlm.nih.gov/27908349/)
- [Brodehl A et al. Mutations in FLNC are Associated with Familial Restrictive Cardiomyopathy. Hum Mutat 2016;37(3):269-79. PMID:26666891](https://pubmed.ncbi.nlm.nih.gov/26666891/)
- [Verdonschot JAJ et al. A mutation update for the FLNC gene in myopathies and cardiomyopathies. Hum Mutat 2020;41(6):1091-1111. PMID:32112656](https://pubmed.ncbi.nlm.nih.gov/32112656/)
- [Agarwal R et al. Filamin C Cardiomyopathy Variants Cause Protein and Lysosome Accumulation. Circ Res 2021;129(7). PMID:34405687](https://pmc.ncbi.nlm.nih.gov/articles/PMC9053646/)
- [Cui H et al. Mutation profile of FLNC gene and its prognostic relevance in patients with hypertrophic cardiomyopathy. Mol Genet Genomic Med 2018;6(6):1104-13.](https://onlinelibrary.wiley.com/doi/full/10.1002/mgg3.488)
- [Hypertrophic cardiomyopathy caused by filamin-C variants has restrictive and extracardiac features and a distinctive ECG. Heart Rhythm, Feb 2026; PII S1547-5271(26)00121-9](https://www.heartrhythmjournal.com/article/S1547-5271(26)00121-9/fulltext?rss=yes)
- [ClinGen Hereditary Cardiovascular Disease GCEP: Reappraisal of Genes associated with Hypertrophic Cardiomyopathy. PMID:39132495](https://pmc.ncbi.nlm.nih.gov/articles/PMC11312670/)
- [Distinct molecular features of FLNC mutations, associated with different clinical phenotypes (iPSC-CM; R1267Q vs V2264M). PMID:39315490](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11904857/)
- [Subcellular Remodeling in Filamin C Deficient Mouse Hearts Impairs Myocyte Tension Development. Int J Mol Sci 2022;23:871](https://pmc.ncbi.nlm.nih.gov/articles/PMC8779483/)
- [Reduction of Filamin C Results in Altered Proteostasis, Cardiomyopathy, and Arrhythmias. J Am Heart Assoc 2023](https://www.ahajournals.org/doi/10.1161/JAHA.123.030467)
- [Homozygous expression of the MFM-associated p.W2710X filamin C variant reveals major pathomechanisms of sarcomeric lesion formation](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7650280/)
- [Cellular Mechanotransduction Relies on Tension-Induced and Chaperone-Assisted Autophagy (CASA / filamin mechanosensing)](https://www.sciencedirect.com/science/article/pii/S0960982213001334)
- [The chaperone-assisted selective autophagy complex dynamics and dysfunctions. Autophagy 2023](https://www.tandfonline.com/doi/full/10.1080/15548627.2022.2160564)
- [2023 ESC Guidelines for the management of cardiomyopathies. Eur Heart J 2023;44(37):3503](https://academic.oup.com/eurheartj/article/44/37/3503/7246608)
- [UniProt Q14315 — Filamin-C (FLNC)](https://rest.uniprot.org/uniprotkb/Q14315.txt)
- [OMIA:000515-9685 — Hypertrophic cardiomyopathy in Felis catus (no FLNC entry found)](https://omia.org/OMIA000515/9685/)
- [NCT07137338 — RP-A701 AAV gene therapy, BAG3 DCM (pathway-adjacent)](https://clinicaltrials.gov/study/NCT07137338)
- [NCT07426419 — AFTX-201 AAV gene therapy, BAG3 DCM (pathway-adjacent)](https://clinicaltrials.gov/study/NCT07426419)