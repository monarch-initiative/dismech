---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-05T00:04:03.495656'
end_time: '2026-08-05T00:28:07.519432'
duration_seconds: 1444.02
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Post-Traumatic Epilepsy
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
  web_search_requests: 28
  num_turns: 54
  total_cost_usd: 4.141259999999999
  session_id: f78931f6-d050-4dd3-8e0b-23a006cd25ec
  stop_reason: end_turn
citation_count: 22
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Post-Traumatic Epilepsy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Post-Traumatic Epilepsy** covering all of the
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

# Post-Traumatic Epilepsy (PTE) — Comprehensive Research Report

**Prepared:** 2026-08-05 · **Target entity:** `MONDO:0043264` post-traumatic epilepsy · **Category:** Complex / acquired (non-Mendelian)

> **A note on how to read this.** PTE is not a genetic disease that happens to have an environmental trigger — it's the reverse. It's an *acquired* epilepsy where a single dated insult (the head injury) starts a clock, and over weeks to years the brain quietly rewires itself into something that seizes. That makes it unusually valuable: unlike almost every other epilepsy, you know exactly when the wound was made, so you can watch the scar form. That's why the field treats it as the model system for human epileptogenesis.
>
> **Verification status.** Ontology IDs below marked ✅ were checked against local OAK adapters during this session (`sqlite:obo:{hp,go,cl,uberon,chebi,ncit,mondo}`). Citations marked ✅ had their abstracts fetched and quoted verbatim. Citations marked ⚠️ come from secondary/search-summary sources and **must be re-fetched with `just fetch-reference PMID:…` and snippet-verified before being committed as dismech evidence.**

---

## 1. Disease Information

### Overview

Post-traumatic epilepsy is a recurrent, unprovoked seizure disorder that develops as a consequence of traumatic brain injury (TBI). The defining feature is *latency*: the seizures that matter are the **late** ones (>7 days post-injury), separated from the trauma by a silent interval during which the injured tissue is remodeling itself into an epileptogenic network.

The conventional temporal taxonomy — and it matters, because the three categories have different mechanisms, different predictive value, and different treatment implications:

| Category | Timing | Nature |
|---|---|---|
| **Immediate** post-traumatic seizures | <24 h | Largely acute symptomatic / concussive convulsions; often non-epileptic |
| **Early** post-traumatic seizures | ≤7 days | Acute symptomatic (provoked); preventable by short-course ASMs; a *risk marker* for PTE, not PTE itself |
| **Late** post-traumatic seizures | >7 days | Unprovoked; **constitute PTE** |

Per current ILAE criteria, epilepsy may be diagnosed after two unprovoked seizures **or** one unprovoked seizure with a ≥60% ten-year recurrence risk. Because the recurrence risk after a single *late* seizure following severe TBI is roughly 80% at 10 years, **a single late post-traumatic seizure after severe TBI is sufficient to diagnose PTE** ⚠️ (recurrence figure reported as "82% at 10 years… 62% within one year" — verify against the primary source).

### Key identifiers

| Resource | Identifier | Status |
|---|---|---|
| MONDO | **MONDO:0043264** post-traumatic epilepsy | ✅ verified via OAK |
| MeSH | **D004834** (Epilepsy, Post-Traumatic) | ✅ (MONDO xref) |
| UMLS | **C0014557** | ✅ (MONDO xref) |
| SNOMED CT | **75023009** | ✅ (MONDO xref) |
| MedGen | **4991** | ✅ (MONDO xref) |
| OMIM | *none* — not a Mendelian entity | — |
| Orphanet | *none* — not a rare disease | — |
| ICD-10-CM | No dedicated code. Coded as epilepsy (`G40.-`, commonly `G40.209`) **plus** sequela of intracranial injury (`S06.-` with 7th character S, or `T90.5`) | ⚠️ verify against current coding guidance |
| ICD-11 | Epilepsy `8A6-` block; structural etiology qualifier; no unique PTE stem code | ⚠️ verify |

### Synonyms (from MeSH D004834 via MONDO) ✅

post-traumatic epilepsy (exact); epilepsy, traumatic; traumatic epilepsy; post-traumatic seizure disorder; early post-traumatic seizures; late post-traumatic seizures; impact seizure; concussive convulsion(s).

**Curation caution:** MONDO's inherited MeSH synonym list lumps "early post-traumatic seizures" and "concussive convulsions" under this term. Mechanistically these are *acute symptomatic seizures*, not epilepsy. The MONDO definition itself flags this: *"Concussive convulsions are nonepileptic phenomena that occur immediately after head injury"* ✅ (MONDO:0043264 `def`). This is a genuine ontology-vs-biology mismatch worth recording as a `discussions` note in the dismech entry.

### Information provenance

Both. Modern PTE epidemiology is dominated by **individual-patient registry/EHR linkage** (Norwegian Trauma Registry, Swedish national registers, Taiwan NHI, US Level 1 trauma centers, TRACK-TBI, EpiBioS4Rx). Mechanistic content is overwhelmingly **model-organism** derived (rodent lateral fluid percussion and controlled cortical impact). Aggregated disease-level resources (Orphanet, OMIM) contribute essentially nothing here.

---

## 2. Etiology

### Primary causal factor

**Traumatic brain injury.** The mechanical insult is necessary; nothing else in this entry substitutes for it. Everything downstream is dose-response on injury severity and lesion type.

### Risk factors — environmental / injury-related

The strongest predictors are all properties of the injury itself:

- **Injury severity** — the dominant gradient. Annegers et al. ✅ (PMID:9414327, *N Engl J Med* 1998;338:20-4) followed 4,541 TBI patients in Olmsted County, MN (1935–1984): *"The overall standardized incidence ratio was 3.1"*, rising to *"17.0 (95 percent confidence interval, 12.3 to 23.6)"* after severe injuries, versus 2.9 (moderate) and 1.5 (mild, *"with no increase over the expected number after five years"*).
- **Penetrating injury** — the highest-risk category of all (see §9).
- **Intracranial hemorrhage / subdural hematoma / cortical contusion** — Annegers ✅ named *"brain contusion with subdural hematoma, skull fracture, loss of consciousness or amnesia for more than one day, and an age of 65 years or older"* as significant risk factors. Kazis et al. ⚠️ (PMID:38398011, *Biomedicines* 2024;12(2):410) report intracranial hemorrhage CIR 1.60.
- **Early post-traumatic seizures** — the single strongest clinical marker. Kazis et al. ⚠️ report *"occurrence of early seizures was significantly associated with an increased risk of PTE"* (CIR 7.28).
- **Depressed skull fracture**, **coma >24 h**, **need for neurosurgical evacuation**.
- **Age** — bimodal risk. Elderly (≥65) per Annegers ✅; young children carry high risk in the abusive-head-trauma setting (§9).
- **Male sex** — ~32% increased risk vs women ⚠️ (Kazis, PMID:38398011).
- **Alcohol misuse** — history of alcohol abuse *"more than doubling the likelihood of PTE"* ⚠️ (Kazis, PMID:38398011).
- **Hospital-acquired infection during the acute admission** — a striking, relatively new signal: adjusted RR 1.59 (95% CI 1.11–2.28; p=0.011) ⚠️ (registry-based cohort, PMC11296124). This is mechanistically coherent with the systemic-inflammation arm of epileptogenesis.

### Risk factors — genetic

There is **no causal gene**. PTE genetics is entirely about *modifier / susceptibility* alleles, and the evidence base is weak. Cotter et al. ⚠️ (PMID:28242442, *Seizure* 2017) systematically reviewed candidate variants; Misra et al. ⚠️ (PMID:36912749, *Eur J Neurol* 2023) concluded that *"current evidence on the association of genetic polymorphisms in epilepsy secondary to TBI or stroke is of low quality and lacks validation."* Treat every allele below as `SUSCEPTIBILITY` with modest confidence. Details in §4.

### Protective factors

- **Genetic protective factors:** none established. (The APOE ε2/ε3 "protection" claim is just the inverse of a non-replicated ε4 risk signal — do not curate it as protective.)
- **Environmental/interventional protective factors:**
  - **Injury prevention** is the only intervention with unambiguous benefit — helmets, restraints, fall prevention, body armor. Preventing the TBI prevents the epilepsy.
  - **Short-course ASM prophylaxis (≤7 days)** reduces *early* seizures but **does not prevent PTE** — a well-replicated null. Pease et al. ✅ note the field's premise that *"Studies in preclinical models of PTE have identified tractable pathways and novel therapeutic strategies that can potentially prevent epilepsy, which remain to be validated in humans"* — i.e., nothing is validated yet.
  - **SSRIs** have been examined as a modifier of post-TBI epilepsy risk in a population cohort ⚠️ (PLOS One 2019) — exploratory only.

### Gene–environment interaction

The whole disease *is* a gene–environment interaction: a fixed environmental insult of measurable magnitude, filtered through host inflammatory and neurotransmitter genotype. The best-characterized example is **IL1B rs1143634** ⚠️ (Diamond et al., PMID:26149793, *Epilepsia* 2015), where the CT genotype was associated with *lower serum IL-1β, higher CSF/serum IL-1β ratio, and increased PTE risk* — a genotype that changes how the brain compartmentalizes the injury's inflammatory response, rather than one that causes seizures on its own. That CSF/serum ratio detail is the mechanistically interesting part: the variant appears to shift where the cytokine ends up, not just how much there is.

---

## 3. Phenotypes

### Core seizure phenotypes

| Phenotype | HPO term | Verified | Characteristics |
|---|---|---|---|
| Recurrent unprovoked seizures | **HP:0001250** Seizure | ✅ | Defining feature |
| Focal-onset seizures | **HP:0007359** Focal-onset seizure | ✅ | **Predominant type.** MONDO def: *"The majority of seizures have a focal onset that correlates clinically with the site of brain injury"* ✅ |
| Focal motor seizure | **HP:0011153** Focal motor seizure | ✅ | Common with peri-rolandic contusion |
| Focal impaired-awareness seizure | **HP:0011146** Dialeptic seizure | ✅ | Frequent with temporal/mesial involvement |
| Focal to bilateral tonic-clonic | **HP:0002069** Bilateral tonic-clonic seizure | ✅ | Common presenting event |
| Status epilepticus | **HP:0002133** Status epilepticus | ✅ | Occasional; higher acute mortality |
| Interictal EEG abnormality | **HP:0002353** EEG abnormality | ✅ | Epileptiform discharges; HFOs (see §10) |

Generalized-onset seizures (**HP:0002197** ✅) and myoclonic seizures (**HP:0032794** ✅) are uncommon and should prompt reconsideration of the diagnosis.

### Structural / imaging phenotypes

| Phenotype | HPO term | Verified |
|---|---|---|
| Intracranial hemorrhage (index injury) | **HP:0002170** | ✅ |
| Gliosis (perilesional) | **HP:0002171** | ✅ |
| Hippocampal atrophy | **HP:0410170** | ✅ |
| Cerebral cortical atrophy | **HP:0002120** | ✅ |

### Comorbid / neuropsychiatric phenotypes

Golub & Reddy ⚠️ (PMID:35302046, *Pharmacol Rev* 2022;74:387-438) frame this well: *"A variety of comorbidities, including difficulty focusing, anxiety, learning and memory impairment, motor dysfunction, and sleep disturbances reduce the quality of life for many patients with PTE."*

| Phenotype | HPO term | Verified | Notes |
|---|---|---|---|
| Cognitive impairment | **HP:0100543** | ✅ | Additive on top of baseline TBI deficit |
| Memory impairment | **HP:0002354** | ✅ | |
| Depression | **HP:0000716** | ✅ | Bidirectional with seizure burden |
| Anxiety | **HP:0000739** | ✅ | |
| Irritability | **HP:0000737** | ✅ | |
| Sleep disturbance | **HP:0002360** | ✅ | |
| Psychosis | **HP:0000709** | ✅ | Less common |
| Headache | **HP:0002315** | ✅ | Frequently persistent post-traumatic headache |

### Onset, severity, progression, frequency

- **Age of onset:** any; determined by age at injury, not by a developmental program.
- **Latency from injury to first late seizure:** the signature parameter. Kazis et al. ⚠️ (PMID:38398011), n=2,862: *"latency period… ranging from 8 days to 20 years. The median latency period was 24.0 months."* Most cases declare within 2 years; a real tail extends decades (§8).
- **Severity:** variable. Roughly one third become drug-resistant — Pease et al. ⚠️ describe *"approximately one-third of patients with PTE fail to achieve seizure freedom despite treatment with multiple antiseizure medications."*
- **Progression:** episodic (seizures) on a background that is usually stable-to-slowly-progressive; not a neurodegenerative trajectory in the ALS sense, though repeated seizures worsen recovery. Pease et al. ✅: *"The repeated seizures that characterize PTE impair neurological recovery and increase the risk of poor outcomes after TBI."*
- **Frequency among affected individuals:** see §9 for population-level incidence.

### Quality of life

No PTE-specific validated instrument; QOLIE-31/QOLIE-89 (epilepsy-specific), SF-36, and EQ-5D are used, alongside GOS-E for TBI outcome. PTE independently predicts worse long-term functional outcome after severe TBI ⚠️ (*Neurology* 2023, doi:10.1212/WNL.0000000000207183). Driving restriction, employment loss, and ASM cognitive side effects are the dominant day-to-day burdens — the drugs meant to help can themselves blunt the cognition the injury already dented.

---

## 4. Genetic / Molecular Information

**Causal genes: none.** PTE is an acquired, non-Mendelian condition. Do not curate a `genetic:` block implying causation; use `relationship_type: SUSCEPTIBILITY` / `MODIFIER` throughout.

### Candidate modifier / susceptibility loci

From Cotter et al. ⚠️ (PMID:28242442) and Misra et al. ⚠️ (PMID:36912749):

| Gene | Variant | Reported effect | Confidence |
|---|---|---|---|
| **IL1B** (hgnc:5992 ⚠️ — verify) | rs1143634 | CT genotype → lower serum IL-1β, higher CSF/serum ratio, ↑ PTE risk (p=0.005; *"Those with IL-1β rs1143634 CT genotype developed PTE in 47.7% of cases (p = 0.008)"* ⚠️) | Best-supported single signal (PMID:26149793) |
| **ADORA1** (adenosine A1 receptor) | rs10920573, rs3766553 | ↑ PTE risk; rs10920573 among "most promising" | Moderate |
| **GAD1** (glutamate decarboxylase 1) | rs3828275, rs3791878, rs769391 | Altered GABA synthesis capacity → PTE risk | Weak–moderate |
| **APOE** | ε4 allele | *"Increased risk of late posttraumatic seizures associated with inheritance of APOE epsilon4 allele"* (PMID:12810485 ⚠️); **but** meta-analysis OR 1.8 (95% CI 0.6–5.6) — **non-significant** ⚠️ | Inconsistent; curate as REFUTE/PARTIAL alongside the original claim |
| **MTHFR** | C677T | Reported association | Weak |
| **UGT1A6 / CYP2C9** | — | Associated with valproate levels and *early* post-traumatic seizures (PMC5574127 ⚠️) — pharmacokinetic, not epileptogenic | Pharmacogenomic, distinct claim |
| **ADORA2A** | rs2298383 | Associated with epilepsy risk **in Chinese pediatric general epilepsy**, *not* PTE ⚠️ | **Do not curate as a PTE association** — this is a scope error the search literature repeatedly makes |

**Variant classification:** all of the above are common polymorphisms / susceptibility alleles, not ACMG-classifiable pathogenic variants. No ClinVar pathogenic entries exist for PTE as such. All germline; allele frequencies are common (gnomAD MAF typically >0.05) — check gnomAD per-variant before curating.

**Functional consequence:** regulatory/quantitative rather than loss-of-function — altered cytokine production (IL1B), altered adenosinergic tone (ADORA1), altered GABA synthesis (GAD1), altered lipid handling/repair (APOE).

### Epigenetics

Not well characterized in human PTE. Preclinical work implicates chromatin-level regulation of inflammatory and glutamatergic genes and, most concretely, **miRNA dysregulation** — see §10 for the EpiBioS4Rx plasma miRNA data (miR-212-3p, miR-132-3p, miR-183-5p, miR-323-3p, miR-434-3p, miR-9a-3p, miR-124-3p) ✅ (PMID:39661396). A genuine knowledge gap worth a `KNOWLEDGE_GAP` discussion entry.

### Chromosomal abnormalities

None. Not applicable.

---

## 5. Environmental Information

- **Primary environmental factor:** mechanical trauma to the head — motor vehicle collisions, falls (dominant in the elderly), assaults, sports, blast and ballistic injury, abusive head trauma in infants.
- **Occupational/military exposure:** combat penetrating head injury carries the highest documented PTE risk of any exposure (§9).
- **Lifestyle:** alcohol misuse operates twice — as a cause of injury and as an independent risk amplifier for PTE ⚠️ (Kazis, PMID:38398011).
- **Infectious agents:** not causal. But **hospital-acquired infection during the acute admission** is an emerging risk factor (aRR 1.59) ⚠️ (PMC11296124), plausibly acting through systemic inflammatory amplification of the neuroinflammatory cascade. Post-traumatic CNS infection (meningitis, abscess after penetrating injury or CSF leak) adds independent epileptogenic risk.

---

## 6. Mechanism / Pathophysiology

This is where the dismech entry earns its keep. The causal chain below is proposed as the pathophysiology graph; every node has a plausible `biological_scale` tag.

### The causal chain (trigger → clinical manifestation)

**Node 1 — Mechanical Brain Injury and Primary Tissue Disruption** (`TISSUE`)
Contusion, axonal shearing, vascular tearing, hemorrhage. This is the only genuinely upstream event. UBERON:0000955 brain ✅; UBERON:0000956 cerebral cortex ✅.

**Node 2 — Blood–Brain Barrier Breakdown and Serum Protein Extravasation** (`TISSUE`)
The barrier fails and serum albumin floods the neuropil. This is the best-worked-out mechanistic arm in the entire field. UBERON:0000120 blood brain barrier ✅; CL:0000071 blood vessel endothelial cell ✅.

**Node 3 — Astrocytic Albumin Uptake via TGF-β Receptor / ALK5 Signaling** (`MOLECULAR`)
Astrocytes take up extravasated albumin through TGF-β receptor signaling, which switches on a transcriptional program. Ivens et al. ⚠️ (PMID:17121744, *Brain* 2007) — "TGF-beta receptor-mediated albumin uptake into astrocytes is involved in neocortical epileptogenesis." Weissberg et al. ⚠️ (PMID:25836421, *Neurobiol Dis* 2015): *"Activation of the astrocytic ALK5/TGF-β-pathway induces excitatory, but not inhibitory, synaptogenesis that precedes the appearance of seizures."*
GO:0007179 transforming growth factor beta receptor signaling pathway ✅; CL:0000127 astrocyte ✅; GO:0048143 astrocyte activation ✅.

**Node 4 — Neuroinflammatory Amplification** (`CELLULAR`)
Microglial activation, IL-1β/IL-1R1 signaling, NLRP3 inflammasome, HMGB1/TLR4, IL-6, TNF, MMP-9. This arm both sustains BBB leakage (a feed-forward loop — the leak feeds the inflammation that widens the leak) and directly lowers seizure threshold via IL-1β-mediated NMDA receptor phosphorylation.
GO:0150076 neuroinflammatory response ✅; GO:0006954 inflammatory response ✅; GO:0001774 microglial cell activation ✅; CL:0000129 microglial cell ✅; CL:0000738 leukocyte ✅.

**Node 5 — Iron Deposition and Oxidative/Ferroptotic Injury** (`MOLECULAR`)
Extravasated erythrocytes break down; hemoglobin → heme → free iron drives Fenton chemistry, lipid peroxidation, and ferroptosis in perilesional tissue. Direct cortical injection of hemoglobin or FeCl₃ produces chronic epileptic seizures in rats ⚠️ — the classic iron-induced epilepsy model. Ferroptosis inhibition (baicalein) reduces seizure score, number, and duration in FeCl₃-induced PTE ⚠️ (PMC6568039); iron chelation with deferoxamine suppresses epilepsy in the same paradigm ⚠️.
GO:0097707 ferroptosis ✅; GO:0006979 response to oxidative stress ✅; CHEBI:29033 iron(2+) ✅; CHEBI:4356 desferrioxamine B ✅. *(Note: GO:0055072 "iron ion homeostasis" is **obsolete** ✅ — do not use it.)*

**Node 6 — Loss of Inhibitory Interneurons and Chloride-Homeostasis Failure** (`CELLULAR`)
Selective vulnerability of hilar parvalbumin- and somatostatin-expressing GABAergic interneurons; downregulation of the K-Cl cotransporter KCC2 (SLC12A5) shifts the GABA_A reversal potential so that GABA becomes depolarizing rather than hyperpolarizing. The brake doesn't just wear out — it starts pushing.
CL:0000617 GABAergic neuron ✅; CHEBI:16865 gamma-aminobutyric acid ✅. (No verified CL term for "parvalbumin-positive interneuron" was found in this session — use CL:0000617 with a more specific `preferred_term`.)

**Node 7 — Excitatory Synaptic Reorganization and Aberrant Plasticity** (`CELLULAR`)
Mossy fiber sprouting in the dentate gyrus creating recurrent excitatory circuits; excitatory synaptogenesis driven by Node 3; mTORC1 pathway activation driving aberrant growth; impaired astrocytic glutamate clearance (EAAT2/GLT-1) raising extracellular glutamate.
GO:0050808 synapse organization ✅; GO:0031929 TOR signaling ✅; GO:0035249 synaptic transmission, glutamatergic ✅; GO:0014048 regulation of glutamate secretion ✅; GO:0060291 long-term synaptic potentiation ✅; UBERON:0001885 dentate gyrus of hippocampal formation ✅.

**Node 8 — Reactive Gliosis and Perilesional Scar** (`TISSUE`)
Astroglial scar with altered potassium buffering (Kir4.1 downregulation) and aquaporin-4 mislocalization. HP:0002171 Gliosis ✅; CL:0000125 glial cell ✅.

**Node 9 — Hyperexcitable, Hypersynchronous Network** (`CELLULAR`/`TISSUE`)
The convergent endpoint. Pease et al. ✅ define it: *"Epileptogenesis is the process whereby previously normal brain tissue becomes prone to recurrent abnormal electrical activity, ultimately resulting in seizures."*

**Node 10 — Recurrent Unprovoked Seizures (PTE)** (`ORGANISM`)
Clinical manifestation. Feeds back onto Nodes 4 and 6 — seizures beget seizures.

### Module conformance opportunities (dismech-specific)

This entry is a strong conformer to the existing **`epilepsy_excitation_inhibition_imbalance`** module (key target: `#Excitation-Inhibition Imbalance`) — Nodes 6, 7, 9 map almost directly. Node 8 has partial affinity to **`fibrotic_response`** (glial scarring is the CNS analog, though not a true myofibroblast/ECM program — flag rather than force it). Node 5 is a candidate anchor if a ferroptosis/iron-injury module is ever created.

### Upstream vs downstream summary

Upstream and irreversible: Nodes 1–2. The **therapeutic window** sits in Nodes 3–5 (the latent period), which is precisely why every antiepileptogenesis trial targets TGF-β, IL-1, mTOR, or iron. Nodes 6–9 are downstream consolidation; once they're set, you're treating epilepsy, not preventing it.

### Metabolic, proteomic, transcriptomic

- **Metabolic:** post-traumatic mitochondrial dysfunction, impaired glucose metabolism, altered adenosine tone (adenosine kinase upregulation is a proposed epileptogenic mechanism in acquired epilepsy generally ⚠️ — the PTE-specific evidence was not confirmed in this session).
- **Proteomic/fluid:** IL-6, IL-8, IL-10, HMGB1, MMP-9 evaluated prospectively in TBI→PTE cohorts; results largely negative (see §10) ⚠️ (PMC12676904).
- **Transcriptomic:** plasma miRNA signatures ✅ (PMID:39661396); brain-tissue single-cell data for human PTE are essentially absent — a clear `KNOWLEDGE_GAP`.

---

## 7. Anatomical Structures Affected

**Organ:** brain (**UBERON:0000955** ✅). System: nervous system, exclusively (secondary systemic effects follow from seizures and ASM exposure, not from the disease process).

**Regional predilection** — TBI preferentially damages the polar regions where brain meets bone:

| Structure | UBERON | Verified | Role |
|---|---|---|---|
| Cerebral cortex | UBERON:0000956 | ✅ | Contusion sites; focal seizure onset zones |
| Neocortex | UBERON:0001950 | ✅ | Perilesional epileptogenic cortex |
| Frontal lobe | UBERON:0016525 | ✅ | Common contusion site (orbitofrontal) |
| Temporal lobe | UBERON:0001871 | ✅ | Common contusion site; mesial temporal onset |
| Hippocampal formation | UBERON:0002421 | ✅ | Sclerosis, mossy fiber sprouting |
| Ammon's horn | UBERON:0001954 | ✅ | CA1/CA3 neuronal loss |
| Dentate gyrus | UBERON:0001885 | ✅ | Hilar interneuron loss; granule cell reorganization |
| Entorhinal cortex | UBERON:0002728 | ✅ | Layer III vulnerability |
| Blood–brain barrier | UBERON:0000120 | ✅ | Site of the initiating leak |

**Cell populations:** CL:0000540 neuron ✅, CL:0000598 pyramidal neuron ✅, CL:0002608 hippocampal neuron ✅, CL:0000617 GABAergic neuron ✅, CL:0000127 astrocyte ✅, CL:0000129 microglial cell ✅, CL:0000125 glial cell ✅, CL:0000071 blood vessel endothelial cell ✅, CL:0000128 oligodendrocyte ✅.

**Subcellular:** mitochondria (oxidative injury), plasma membrane (KCC2, EAAT2, Kir4.1, aquaporin-4 mislocalization), synapse (excitatory synaptogenesis), lysosome (astrocytic albumin trafficking). Bind GO Cellular Component terms at curation time — none were verified in this session.

**Lateralization:** typically **unilateral/asymmetric**, tracking the lesion; bilateral in diffuse or blast injury and in abusive head trauma. Notably, *"A left parietal lobe lesion and the presence of hemosiderin staining were linked to the development of PTE"* ⚠️ — a lateralization signal that has not been consistently replicated.

---

## 8. Temporal Development

**Onset pattern:** insidious, following a defined latent period. This is a **secondary/acquired onset** — age of onset = age at injury + latency.

**Latency distribution** ⚠️ (Kazis, PMID:38398011, n=2,862): median **24.0 months**; range **8 days to 20 years**. Most cases declare within the first 2 years; the risk curve flattens but never reaches zero.

**The very long tail is real and clinically important.** Raymont et al. ⚠️ (PMID:20644150, *Neurology* 2010), Vietnam Head Injury Study phase 3 at 30–35 years post-injury: seizure prevalence 43.7% (87/199), and *"11 of 87 (12.6%) reported very late onset of PTE after phase 2 (more than 14 years after injury)."* PTE can first appear 35 years after a combat head injury.

**Severity-dependent duration of excess risk:** Annegers ✅ found mild injuries carried elevated risk *"with no increase over the expected number after five years"* — i.e., mild TBI risk is transient, severe TBI risk is lifelong.

**Disease stages:**
1. **Acute/insult phase** (0–7 days) — primary + secondary injury, early symptomatic seizures.
2. **Latent phase / epileptogenesis** (days → months–years) — clinically silent, biologically busy. The therapeutic window.
3. **Chronic phase** — established PTE with recurrent unprovoked seizures.
4. **Refractory phase** (~⅓ of patients) — drug resistance, surgical evaluation.

**Course:** chronic, lifelong once established; seizures episodic. **Remission:** spontaneous remission occurs but is less common than in idiopathic generalized epilepsies; treatment-induced seizure freedom is achieved in roughly two-thirds.

**Critical period:** days-to-weeks after injury. Every antiepileptogenic strategy in §12 is an attempt to intervene here.

---

## 9. Inheritance and Population

### Epidemiology

**Fraction of all epilepsy:**
- Pease et al. ✅: *"Post-traumatic epilepsy (PTE) accounts for 5% of all epilepsies."*
- Kazis et al. ⚠️ (PMID:38398011): *"Previous TBI accounts for approximately 5% of new cases and 20% of prevalent cases."*
- Commonly cited as **10–20% of symptomatic (structural) epilepsies** ⚠️.

**Cumulative incidence after TBI:**

| Cohort | Finding | Source |
|---|---|---|
| Olmsted County, US (1935–84) | SIR 3.1 overall; **1.5** mild / **2.9** moderate / **17.0** (95% CI 12.3–23.6) severe | ✅ PMID:9414327 |
| Norway, nationwide (2015–20), n=8,660 vs 84,024 controls | Cumulative epilepsy incidence **3.1% at 2 yr, 4.0% at 5 yr** (controls 0.2% / 0.5%); severe TBI *"11.8% [95% CI 9.7-14.4%] after 2 years and 13.2% [10.8-16.0%]"* at 5 yr; **7.7× risk** vs trauma-free controls over 5 yr | ✅ PMID:38903174 |
| Sweden, nationwide register | **10-year risk 4.0%** (95% CI 3.8–4.2) after any TBI vs 0.9% in controls | ⚠️ Karlander et al., *JNNP* 2021;92:617-621 (PMID not verified) |
| Sweden, 10-yr by lesion type | Focal cerebral injury **12.9%**; diffuse **8.1%**; extracerebral **7.3%**; skull fracture **2.8%**; mild TBI **2.6%** | ⚠️ via PMID:38398011 |
| Vietnam Head Injury Study (penetrating) | PTE prevalence **43.7–53%** | ⚠️ PMID:20644150, PMID:3929158 |
| Severe non-penetrating TBI, Iran (n=803) | 10.2% late post-traumatic seizures | ⚠️ |
| Pediatric abusive head trauma | ~30% develop PTE within 2–5 yr; **36% by age 5** post-injury | ⚠️ |

**Curation note for the `prevalence:` block:** use `measure_type: PERIOD_PREVALENCE` or `ANNUAL_INCIDENCE` as appropriate and record the *base population* (TBI survivors vs general population) in `population:` — these numbers are conditional on injury and are meaningless without it. For the general population, PTE prevalence should be derived as ~5% of epilepsy prevalence, giving roughly **30–40 per 100,000** (`prevalence_class: BAND_1_5_PER_10000`) — but this is a derivation, so mark it in `notes:` rather than dressing it up as a sourced figure.

**Sex ratio:** male predominance, driven both by TBI incidence (men sustain more severe TBI) and by a possible ~32% independent risk elevation ⚠️.

**Age distribution:** bimodal in risk — young children (especially abusive head trauma, reported risks *"as high as 60%"* ⚠️) and adults ≥65 (Annegers ✅). Peak *absolute* case numbers follow the young-adult male TBI peak.

**Geographic distribution:** follows TBI epidemiology — road-traffic injury burden in LMICs, falls in aging high-income populations, conflict zones for penetrating injury. No genetic founder effects; not applicable.

### Inheritance

**Not heritable.** Inheritance pattern: **multifactorial / not applicable**. Do not populate `inheritance:` with an HPO mode-of-inheritance term. No penetrance, expressivity, anticipation, mosaicism, founder effect, consanguinity, or carrier frequency parameters apply.

---

## 10. Diagnostics

### Clinical criteria — the actual diagnostic basis

PTE is a **clinical diagnosis**: a history of TBI plus ≥1 late (>7 day) unprovoked seizure meeting ILAE epilepsy criteria. There is no confirmatory test.

**Differential diagnosis** — and this is where most diagnostic error lives:
- **Psychogenic non-epileptic seizures (PNES)** — markedly over-represented after TBI; requires video-EEG to distinguish. The single most important differential.
- **Acute symptomatic (provoked) seizures** — metabolic derangement, drug/alcohol withdrawal, sepsis, hyponatremia. Provoked ≠ epilepsy.
- **Concussive convulsions** — immediate, non-epileptic (explicitly noted in the MONDO definition ✅).
- **Syncope** with convulsive features; post-traumatic movement disorders; sleep disorders.
- **Pre-existing epilepsy** that predated the injury — or caused it (a seizure-induced fall producing the TBI).

### Electrophysiology

- **Routine and prolonged EEG / continuous EEG (cEEG)** — the diagnostic workhorse. Detects interictal epileptiform discharges and non-convulsive seizures.
- **High-frequency oscillations (HFOs)** — ripples 80–250 Hz and fast ripples 250–500 Hz ⚠️ (PMID:38398011) are the leading electrophysiological biomarker candidate. *"fast ripples representing pathological synchronization of cellular assemblies related to seizure onset zones"* ⚠️.
- **Quantitative EEG** — early (days 2–5) increased delta spectral power discriminates PTE risk after severe TBI ⚠️; preclinical accuracies near 95%/AUC ~0.98 have been reported ⚠️ and should be treated with appropriate skepticism given model-to-human gaps.

### Imaging

- **CT** (acute) — hemorrhage, contusion, fracture; establishes the injury substrate.
- **MRI with SWI/GRE** — hemosiderin and microbleed detection. *"Microbleeds of diffuse vascular injury and resulting iron residues… are robustly detected by susceptibility weighted imaging"* ⚠️.
- **T1-weighted magnetization transfer MRI** — *"gliosis surrounding hemosiderin deposits… precede PTE"* ⚠️.
- **DTI** — decreased fractional anisotropy, increased mean diffusivity ⚠️ (PMID:38398011).
- **Dynamic contrast-enhanced MRI** — BBB permeability quantification; mechanistically the most direct imaging readout of Node 2.
- **PET/SPECT, MEG** — for surgical localization in refractory cases.

### Fluid biomarkers

Honest summary: **no validated fluid biomarker exists.** A prospective international study of IL-6, IL-8, IL-10, HMGB1 and MMP-9 (blood at days 2 and 4, 24-month follow-up) concluded these *"may not serve as sensitive biomarkers of PTE"* — though *"a faster decline in IL-6 levels in the non-PTE groups suggests a more rapid resolution of inflammation among patients who do not develop PTE"* ⚠️ (PMC12676904). GFAP and S100B are validated for TBI severity/CT-positivity (GFAP AUC 0.85 vs S100B 0.67 in TRACK-TBI ⚠️, PMID:32854584) but **not** for PTE prediction.

The most rigorous prospective biomarker data are preclinical: Heiskanen et al. ✅ (PMID:39661396, *Epilepsia* 2025, EpiBioS4Rx Project 1, n=245 rats across Finland/Australia/USA): *"None of the seven miRNAs differentiated TBI rats that did and did not develop epilepsy (p > .05)… However, miR-212-3p differentiated rats that developed epilepsy with seizure clusters… with an area under the curve (AUC) of .81."* Conclusion: *"miR-212-3p alone or in combination with miR-132-3p shows promise as a translational prognostic biomarker for the development of severe PTE with seizure clusters."*

**Curation note:** this is a textbook `HUMAN_MODEL_MISMATCH` candidate — a rigorously harmonized multi-site rodent biomarker result whose human translation is entirely unestablished. Also note the EpiBioS4Rx harmonization methods paper ⚠️ (PMID:38056191) as the *"first demonstration of the feasibility of protocol harmonization for performing powered preclinical multi-center trials."*

### Genetic testing

**Not indicated.** No diagnostic genetic test. WGS/WES/panels/CMA/karyotype/FISH/mtDNA/repeat-expansion testing all: **not applicable**. Genotyping of IL1B/ADORA1/APOE is research-only. The only defensible clinical genetic testing scenario is when the "post-traumatic" attribution is doubted and a genetic epilepsy is in the differential.

### Screening

No population screening. **Risk stratification** of TBI survivors (severity, lesion type, early seizures, cEEG findings) is the practical analog, and is the enrolment strategy for antiepileptogenesis trials rather than a clinical service.

---

## 11. Outcome / Prognosis

**Mortality.** PTE substantially raises death risk above TBI alone:
- Taiwan population-based cohort ⚠️: mortality IR 71.8 vs 27.6 per 1,000 person-years (PTE vs TBI alone); **aHR 2.31 (95% CI 1.96–2.73)**.
- Late post-traumatic seizures ⚠️ (PMID:19508123): 27% died at 8–15 years post-injury vs 10% without LPTS, and *"individuals with LPTS died at a younger age (54.1 versus 67.7 years)"* — over a decade of life lost.
- Acquired epilepsy generally carries a median SMR ~2.3 ⚠️.
- Excess mortality becomes evident roughly **1 year** after injury ⚠️ (PMID:35852600, *J Neurol* 2022) — i.e., it is not just the acute injury killing people.
- SUDEP risk applies as in other focal epilepsies (PTE-specific rates not well established — a knowledge gap).

**Morbidity and function.** PTE independently predicts worse long-term functional outcome after severe TBI ⚠️ (*Neurology* 2023). Pease et al. ✅: *"The repeated seizures that characterize PTE impair neurological recovery and increase the risk of poor outcomes after TBI."*

**Treatment response.** ~⅔ achieve seizure freedom on ASMs; **~⅓ are pharmacoresistant** ⚠️. Golub & Reddy ⚠️ (PMID:35302046): *"There is currently no approved treatment that can prevent onset of spontaneous seizures associated with brain injury, and many cases of PTE are refractory to antiseizure medications."*

**Prognostic factors:** injury severity; penetrating vs closed; presence and volume of intracranial hemorrhage; early post-traumatic seizures; age; number of ASMs failed (the standard drug-resistance predictor); recurrence after a first late seizure (~80% at 10 years ⚠️).

**Prognostic biomarkers:** none validated. Candidates: HFOs, early delta power, DTI/SWI features, plasma miR-212-3p/miR-132-3p ✅ (rodent only).

---

## 12. Treatment

### The central therapeutic fact

**Nothing prevents PTE.** Prophylactic ASMs reduce *early* seizures and do not touch late seizures or epileptogenesis. Pease et al. ⚠️: *"Multiple randomized controlled trials have shown that short-term antiseizure prophylaxis does not prevent the development of PTE."* Every treatment below is symptomatic.

### Acute prophylaxis (early seizure prevention — NOT antiepileptogenesis)

**Neurocritical Care Society 2024 guideline** ✅ (Frontera JA et al., PMID:38316735, *Neurocrit Care* 2024) — the current authoritative statement, and refreshingly candid about how thin the evidence is:

> *"Based on GRADE criteria, we suggest that ASM or no ASM may be used in patients hospitalized with moderate-severe TBI (weak recommendation, low quality of evidence). If used, we suggest LEV over PHT/fPHT (weak recommendation, very low quality of evidence) for a short duration (≤ 7 days, weak recommendation, low quality of evidence)."*

and:

> *"There were no significant differences in early or late seizure with longer versus shorter ASM use, though cognitive outcomes and adverse events appear worse with protracted use."*

Brain Trauma Foundation (4th ed.) ⚠️: phenytoin recommended (Level IIA) to decrease incidence of early PTS; *"Prophylactic use of phenytoin or valproate is not recommended for preventing late post traumatic seizures."*

| Treatment | dismech pattern |
|---|---|
| Levetiracetam prophylaxis | `treatment_term` NCIT:C15986 Pharmacotherapy ✅; `therapeutic_agent` CHEBI:6437 levetiracetam ✅; `therapeutic_modality: SMALL_MOLECULE` |
| Phenytoin / fosphenytoin prophylaxis | NCIT:C15986 ✅ + CHEBI:8107 phenytoin ✅ |

### Chronic pharmacotherapy for established PTE

Standard focal-epilepsy ASMs — levetiracetam, lacosamide, carbamazepine/oxcarbazepine, lamotrigine, valproate, brivaracetam, perampanel, topiramate, zonisamide. No agent is PTE-specific and no head-to-head evidence establishes superiority in this population. All: `treatment_term` **NCIT:C15986 Pharmacotherapy** ✅ + a CHEBI `therapeutic_agent`.

**Pharmacogenomics:** *HLA-B\*15:02* (carbamazepine SJS/TEN in Southeast Asian ancestry) and *HLA-A\*31:01*; *CYP2C9* poor metabolizers and phenytoin toxicity; *UGT1A6/CYP2C9* and valproate levels ⚠️ (PMC5574127). These are ASM-class facts, not PTE-specific — curate them where the drug is curated. (Note: the existing dismech `drug_hypersensitivity_scar` module is the natural home for the HLA-linked SCAR risk.)

### Surgical and interventional

- **Resective epilepsy surgery** (lesionectomy, anterior temporal lobectomy ± amygdalohippocampectomy) for drug-resistant, well-localized PTE. Outcomes in PTE are generally poorer than in mesial temporal sclerosis, because post-traumatic lesions are often multifocal — the injury didn't respect anatomical boundaries. `treatment_term` NCIT:C15329 Surgical Procedure ✅; `therapeutic_modality: SURGERY`.
- **Neuromodulation** — vagus nerve stimulation, responsive neurostimulation (RNS), deep brain stimulation (ANT-DBS) for non-resectable/multifocal cases. `therapeutic_modality: DEVICE`; `treatment_term` NCIT:C49236 Therapeutic Procedure ✅ (no reliable NCIT device-modality term is inferable — see the CLAUDE.md backfill table).
- **Laser interstitial thermal therapy (LITT)** — ablative alternative.

### Supportive and rehabilitative

Cognitive rehabilitation, physical therapy (NCIT:C15302 ✅), occupational and speech therapy, psychiatric management of depression/anxiety, driving-restriction counseling, seizure-safety education. NCIT:C15315 Rehabilitation ✅; NCIT:C15747 Supportive Care ✅. `therapeutic_modality: BEHAVIORAL`.

### Experimental / antiepileptogenic

This is the field's open frontier, and so far it's a graveyard of negative trials:

| Agent | Target | Status |
|---|---|---|
| **Levetiracetam** (prevention) | SV2A | Phase 2 safety/feasibility ⚠️ (PMID:22777131, NCT01463033); PTE HR 0.48, **p=0.18** — underpowered, not significant |
| **Biperiden** (anticholinergic) | Muscarinic | Multicenter RCT, n=312, moderate/severe TBI, 10-day treatment ⚠️ (NCT01048138; *Front Neurol* 2024). *"Data analysis indicated lack of evidence of biperiden for either the incidence of post-traumatic epilepsy or the mortality rate."* **Negative.** |
| **Rapamycin / mTOR inhibitors** | mTORC1 | Preclinical only. *"Rapamycin treatment for one month after TBI decreased the seizure frequency and rate of developing posttraumatic epilepsy during an entire 16 week monitoring session"* ⚠️ (PMID:23691153); replicated in rat ⚠️ (PMID:29904395). CHEBI:9168 sirolimus ✅ |
| **SJN2511 / ALK5-TGF-β inhibitors** | Node 3 | Preclinical. *"Treatment with SJN2511, a specific ALK5/TGF-β inhibitor, prevents synaptogenesis and epilepsy"* ⚠️ (PMID:25836421) |
| **Anakinra / IL-1R antagonists** | IL-1β | Preclinical + case-level; no PTE RCT ⚠️ |
| **Ceftriaxone** | GLT-1/EAAT2 upregulation | Preclinical glutamate modulation ⚠️ |
| **Deferoxamine / ferroptosis inhibitors (baicalein)** | Iron, ferroptosis | Preclinical, FeCl₃ model ⚠️. CHEBI:4356 desferrioxamine B ✅ |
| **Cortical excitability probing (TMS)** | Biomarker development | NCT05517954 |

Register clinical trials in the dismech `clinical_trials:` block with `phase:` as the enum form (e.g. `PHASE_II`) and evidence referencing `clinicaltrials:NCT…` after `just fetch-reference`.

---

## 13. Prevention

**Primary prevention — the only proven lever.** Prevent the TBI: helmets (motorcycle, bicycle, sport), seatbelts and airbags, speed control and impaired-driving enforcement, fall prevention in the elderly (vision correction, home hazard reduction, medication review, strength/balance training), firearm safety, combat helmet and body-armor design, child-abuse prevention programs. Every prevented severe TBI removes a 13% five-year epilepsy risk ✅ (PMID:38903174).

**Secondary prevention.** Aggressive acute neurocritical care to limit secondary injury (ICP control, avoidance of hypoxia/hypotension, hemorrhage evacuation), plus ≤7-day ASM prophylaxis to prevent early seizures ✅ (PMID:38316735). Infection control during the acute admission is a plausible, testable secondary-prevention target given the aRR 1.59 signal ⚠️.

**Tertiary prevention.** Seizure control to prevent injury, status epilepticus, SUDEP, and further functional decline; ASM adherence support; comorbidity treatment (depression, sleep); driving and occupational safety counseling.

**Immunization, genetic screening, genetic counseling, prophylactic surgery:** **not applicable.** (NCIT:C15240 Genetic Counseling ✅ exists but should not be curated for this entry.)

**Public health:** road safety legislation, alcohol policy, sports concussion protocols and return-to-play rules, elder fall-prevention programs, domestic violence and child-abuse intervention.

---

## 14. Other Species / Natural Disease

- **Species:** *Homo sapiens* (**NCBITaxon:9606**) — primary. Naturally occurring post-traumatic epilepsy is documented in **dogs** (*Canis lupus familiaris*, NCBITaxon:9615) and occasionally **cats** (*Felis catus*, NCBITaxon:9685) as "structural epilepsy of traumatic origin" under the IVETF (International Veterinary Epilepsy Task Force) classification ⚠️ — verify NCBITaxon IDs and IVETF citations before curating.
- **Breed (VBO):** no breed-specific predisposition; head trauma is the determinant, not lineage. Not applicable.
- **Orthologous genes:** not applicable — no causal gene. Modifier orthologs (*Il1b*, *Adora1*, *Gad1*, *Apoe*) exist across mammals but carry no established veterinary PTE association.
- **OMIA:** no PTE entry expected (OMIA covers inherited traits).
- **Comparative pathology:** the core mechanisms — BBB breakdown, albumin/TGF-β astrocyte signaling, iron deposition, interneuron loss, mossy fiber sprouting — are conserved across rodent, canine, and human injured brain, which is why the rodent models retain face validity.
- **Zoonotic potential / transmission:** **not applicable.**

---

## 15. Model Organisms

PTE has arguably the best-developed epileptogenesis model portfolio of any acquired epilepsy — the field can induce the injury on a known day and then watch for months.

### Induced (injury) models — the workhorses

| Model | Species | Characteristics |
|---|---|---|
| **Lateral fluid percussion injury (LFPI)** | Rat (Sprague-Dawley), mouse | The reference model. *"43% to 50% of injured animals developed epilepsy, with a latency period between 7 weeks to 1 year. Mean seizure frequency was 0.3±0.2 seizures per day and mean seizure duration was 113±46 s"* ⚠️. Reproduces contusion, subdural/intracerebral hematoma, hippocampal sclerosis, reactive gliosis, mossy fiber sprouting ⚠️. Key refs: Kharatishvili et al., *Neuroscience* 2006 ⚠️; D'Ambrosio et al., *Brain* 2004;127:304 ⚠️ |
| **Controlled cortical impact (CCI)** | Mouse, rat | Highly reproducible mechanics. *"Although a large proportion of CCI mice do not develop spontaneous seizures, spontaneous epileptiform spiking occurs suggestive of ongoing epileptogenesis"* ⚠️ (Bolkvadze & Pitkänen, *J Neurotrauma* 2012 ⚠️) |
| **Weight drop / impact acceleration** | Rat, mouse | Diffuse injury; lower PTE yield |
| **Blast injury** | Rat, mouse, swine | Military-relevant; emerging |
| **Undercut / partial isolation cortex** | Rat, cat | Chronic cortical hyperexcitability; mechanistic dissection |
| **Iron/FeCl₃ or hemoglobin cortical injection** | Rat, mouse | Isolates the iron/ferroptosis arm (Node 5) ⚠️ |

### The methodological state of the art

**EpiBioS4Rx** (NINDS Center Without Walls; Finland, Australia, USA) is the field-defining multicenter effort. Its harmonization paper ⚠️ (PMID:38056191) reported the *"first demonstration of the feasibility of protocol harmonization for performing powered preclinical multi-center trials for biomarker and therapy discovery of post-traumatic epilepsy."* Its Project 1 biomarker study ✅ (PMID:39661396) randomized **n=245 adult male Sprague-Dawley rats** to LFPI or sham across three sites with 7th-month video-EEG — a scale and rigor almost unheard of in preclinical neuroscience.

**Genetic models:** conditional/transgenic lines are used as *mechanistic probes layered onto* an injury model, not as standalone PTE models — e.g. KCC2 (Slc12a5) disruption in parvalbumin interneurons *"associated with a decreased seizure threshold and a progressive loss of parvalbumin-positive interneurons"* ⚠️, and TGF-β/ALK5 pathway manipulation ⚠️ (PMID:25836421).

### Phenotype recapitulation and limitations

**Recapitulated well:** focal onset seizures; latent period; hippocampal sclerosis and mossy fiber sprouting; interneuron loss; BBB breakdown; reactive gliosis; iron deposition; interictal spikes and HFOs; the severity–incidence gradient.

**Not recapitulated / limitations** — worth an explicit `HUMAN_MODEL_MISMATCH` discussion entry:
- Rodents are lissencephalic; human contusion patterns depend on gyral/skull geometry.
- Most studies use **young adult male** rodents; human PTE risk peaks in the elderly and in young children, and sex differences are unmodeled.
- Seizure frequency in rodent PTE is low (~0.3/day), demanding months of video-EEG and huge n — the main reason preclinical trials have been underpowered.
- Absence-like spike-wave discharges in certain rat strains have been **mistaken for PTE** — a documented confound requiring strain-matched controls ⚠️ (arXiv:1509.05802, "Lack of appropriate controls leads to mistaking absence seizures for post-traumatic epilepsy"). If you take one methodological caution from this section, take that one.
- Comorbidity phenotypes (depression, cognition) are measured with instruments of uncertain human correspondence.
- **Every antiepileptogenic agent that worked in these models has so far failed or gone untested in humans.**

### Resources

MGI (mouse), RGD (rat), Alliance of Genome Resources, IMPC/KOMP; EpiBioS4Rx data-sharing portal; NINDS Common Data Elements for TBI; FITBIR (Federal Interagency TBI Repository).

---

## Appendix A — Suggested `pathophysiology` node skeleton for the dismech entry

| # | Node name | `biological_scale` | Key terms | Downstream |
|---|---|---|---|---|
| 1 | Mechanical Brain Injury and Primary Tissue Disruption | TISSUE | UBERON:0000956 ✅ | → 2 |
| 2 | Blood-Brain Barrier Breakdown and Serum Albumin Extravasation | TISSUE | UBERON:0000120 ✅, CL:0000071 ✅ | → 3, 4, 5 |
| 3 | Astrocytic Albumin Uptake via TGF-beta/ALK5 Signaling | MOLECULAR | GO:0007179 ✅, GO:0048143 ✅, CL:0000127 ✅ | → 7 |
| 4 | Neuroinflammatory Amplification | CELLULAR | GO:0150076 ✅, GO:0001774 ✅, CL:0000129 ✅ | → 2 (feed-forward), 6, 9 |
| 5 | Iron Deposition and Ferroptotic Oxidative Injury | MOLECULAR | GO:0097707 ✅, GO:0006979 ✅, CHEBI:29033 ✅ | → 6 |
| 6 | Inhibitory Interneuron Loss and Chloride Homeostasis Failure | CELLULAR | CL:0000617 ✅, CHEBI:16865 ✅ | → 9 |
| 7 | Excitatory Synaptic Reorganization and Aberrant Plasticity | CELLULAR | GO:0050808 ✅, GO:0031929 ✅, GO:0035249 ✅, UBERON:0001885 ✅ | → 9 |
| 8 | Reactive Gliosis and Perilesional Scar Formation | TISSUE | CL:0000125 ✅ | → 9 |
| 9 | Neuronal Hyperexcitability and Network Hypersynchrony | CELLULAR | — | → 10 |
| 10 | Recurrent Unprovoked Seizures | ORGANISM | HP:0007359 ✅ | → 4, 6 (feedback) |

Suggested `conforms_to`: node 9 → `epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance`.
Suggested treatment `target_mechanisms`: rapamycin `INHIBITS` node 7; ALK5 inhibitor `INHIBITS` node 3; anakinra `INHIBITS` node 4; deferoxamine `INHIBITS` node 5. All experimental — pair each with the correct `evidence_source: MODEL_ORGANISM`.

## Appendix B — Citation ledger

**Abstract-verified in this session (✅ — quotes above are verbatim, but still run `just fetch-reference` before committing):**
`PMID:38570704` · `PMID:9414327` · `PMID:38903174` · `PMID:38316735` · `PMID:39661396`

**Needs independent verification before curation (⚠️):**
`PMID:38398011` · `PMID:35302046` · `PMID:20644150` · `PMID:3929158` · `PMID:12810485` · `PMID:26149793` · `PMID:28242442` · `PMID:36912749` · `PMID:23691153` · `PMID:29904395` · `PMID:25836421` · `PMID:17121744` · `PMID:38056191` · `PMID:22777131` · `PMID:35852600` · `PMID:19508123` · `PMID:32854584` · Karlander *JNNP* 2021 (PMID unresolved) · Bolkvadze & Pitkänen *J Neurotrauma* 2012 (PMID unresolved) · Kharatishvili *Neuroscience* 2006 (PMID unresolved) · D'Ambrosio *Brain* 2004 (PMID unresolved) · *Neurology* 2023 doi:10.1212/WNL.0000000000207183 (PMID unresolved)

**Ontology terms verified against local OAK adapters this session:** all HP, GO, CL, UBERON, CHEBI, NCIT, and MONDO IDs marked ✅ above. **GO:0055072 is obsolete** — do not use. No verified CL term for "parvalbumin-positive interneuron" was found; use CL:0000617 with a specific `preferred_term`. HGNC IDs are **not** verified and must be checked before use.

---

**Sources:**
- [Insights into epileptogenesis from post-traumatic epilepsy — Nat Rev Neurol 2024 (PMID:38570704)](https://pubmed.ncbi.nlm.nih.gov/38570704/)
- [A population-based study of seizures after traumatic brain injuries — NEJM 1998 (PMID:9414327)](https://pubmed.ncbi.nlm.nih.gov/9414327/)
- [Risk of epilepsy after TBI: nationwide Norwegian matched cohort — Front Neurol 2024 (PMID:38903174)](https://pubmed.ncbi.nlm.nih.gov/38903174/)
- [NCS Guidelines for Seizure Prophylaxis in Moderate-Severe TBI — Neurocrit Care 2024 (PMID:38316735)](https://pubmed.ncbi.nlm.nih.gov/38316735/)
- [Plasma microRNAs as prognostic biomarkers, EpiBioS4Rx Project 1 — Epilepsia 2025 (PMID:39661396)](https://pubmed.ncbi.nlm.nih.gov/39661396/)
- [Epidemiology, Risk Factors, and Biomarkers of PTE — Biomedicines 2024 (PMID:38398011)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10886732/)
- [Post-Traumatic Epilepsy and Comorbidities — Pharmacol Rev 2022 (PMID:35302046)](https://pubmed.ncbi.nlm.nih.gov/35302046/)
- [Correlates of posttraumatic epilepsy 35 years following combat brain injury — Neurology 2010 (PMID:20644150)](https://pubmed.ncbi.nlm.nih.gov/20644150/)
- [Genetic biomarkers of posttraumatic epilepsy: a systematic review — Seizure 2017 (PMID:28242442)](https://pubmed.ncbi.nlm.nih.gov/28242442/)
- [IL-1β associations with posttraumatic epilepsy development — Epilepsia 2015 (PMID:26149793)](https://pubmed.ncbi.nlm.nih.gov/26149793/)
- [Impact of genetic polymorphisms on epilepsy risk after acute brain injury — Eur J Neurol 2023 (PMID:36912749)](https://pubmed.ncbi.nlm.nih.gov/36912749/)
- [Albumin induces excitatory synaptogenesis through astrocytic TGF-β/ALK5 signaling (PMID:25836421)](https://pubmed.ncbi.nlm.nih.gov/25836421/)
- [TGF-beta receptor-mediated albumin uptake into astrocytes in neocortical epileptogenesis (PMID:17121744)](https://pubmed.ncbi.nlm.nih.gov/17121744/)
- [Rapamycin attenuates the development of posttraumatic epilepsy (PMID:23691153)](https://pubmed.ncbi.nlm.nih.gov/23691153/)
- [EpiBioS4Rx preclinical harmonization (PMID:38056191)](https://pubmed.ncbi.nlm.nih.gov/38056191/)
- [Biperiden as antiepileptogenic after TBI — randomized clinical trial, Front Neurol 2024](https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2024.1443982/full)
- [Hospital-acquired infections as a risk factor for PTE — registry cohort](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11296124/)
- [Risk and cause of death in post-traumatic epilepsy — J Neurol 2022 (PMID:35852600)](https://pubmed.ncbi.nlm.nih.gov/35852600/)
- [Inflammatory proteins as acute biomarkers of post-traumatic epilepsy](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12676904/)
- [Baicalein suppresses ferroptosis in FeCl₃-induced posttraumatic epileptic seizures](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6568039/)
- [Animal Models of Post-Traumatic Epilepsy — Diagnostics 2020](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7169449/)
- [Brain Trauma Foundation Guidelines for the Management of Severe TBI, 4th Edition](https://braintrauma.org/coma/guidelines/severe-tbi)