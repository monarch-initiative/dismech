---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-04T13:55:15.026861'
end_time: '2026-08-04T14:16:06.989765'
duration_seconds: 1251.96
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Placental Abruption
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
  web_search_requests: 7
  num_turns: 83
  total_cost_usd: 7.573395499999999
  session_id: 3f7a16c4-8feb-4ebf-bdf4-34c78e5b8e12
  stop_reason: end_turn
citation_count: 46
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Placental Abruption
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Placental Abruption** covering all of the
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

# Placental Abruption (Abruptio Placentae) — Comprehensive Research Report

**Target:** Placental Abruption · **MONDO:0004846** · Category: Complex (multifactorial, non-Mendelian)
**Report date:** 2026-08-04 · **Evidence cutoff:** literature through mid-2026
**Verification note:** every PMID below was retrieved from NCBI E-utilities during this session and every quoted snippet is a verbatim substring of the retrieved PubMed abstract. Every ontology CURIE was resolved live against EBI OLS4 (HP/GO/CL/UBERON/CHEBI/NCIT/MONDO) or the HGNC REST API. Items I could not verify are explicitly flagged as **UNVERIFIED**.

---

## 1. Disease Information

### 1.1 Overview

Placental abruption is the premature separation of a normally implanted placenta from the uterine wall before delivery of the fetus. It is an *obstetric* rather than a *constitutional* disease: the affected "organ" is a transient fetomaternal organ, the disease exists only during a pregnancy, and it has two patients (the pregnant person and the fetus) whose risks diverge. Mechanistically it is a hemorrhagic disease of the decidua basalis — rupture of maternal decidual vessels produces a retroplacental hematoma that dissects the maternal–fetal interface, destroying gas-exchange surface acutely and generating a large local thrombin burst that drives inflammation, membrane weakening and uterine contraction.

Two clinically and mechanistically distinct presentations exist and should be modeled as separate arms:

1. **Acute abruption** — often trauma- or shear-triggered, with sudden hemorrhage, uterine hypertonus, fetal compromise, coagulopathy.
2. **Chronic/ischemic abruption** — the culmination of long-standing uteroplacental vasculopathy, sharing risk profile and placental lesions with preeclampsia and fetal growth restriction under the "ischemic placental disease" umbrella.

Brandt & Ananth (AJOG 2023, PMID:37164498) — the current definitive review — states: *"Placental abruption is the premature separation of the placenta from its uterine attachment before the delivery of a fetus."* They emphasize both chronic processes (vasculopathy) and acute triggers (abdominal trauma), and report a prevalence of 0.6%–1.2% of pregnancies.

The MeSH scope note (D000037, retrieved from NCBI MeSH) is a compact and citable definition:

> "Premature separation of the normally implanted PLACENTA from the UTERUS. Signs of varying degree of severity include UTERINE BLEEDING, uterine MUSCLE HYPERTONIA, and FETAL DISTRESS or FETAL DEATH."

### 1.2 Key identifiers (all retrieved live)

| Resource | Identifier | Notes |
|---|---|---|
| **MONDO** | `MONDO:0004846` | label: `placental abruption` |
| **HPO** | `HP:0011419` | label: `Placental abruption` — usable as a *phenotype* of other disorders |
| **MeSH** | `D000037` (`MESH:D000037`) | Abruptio Placentae; tree numbers C12.050.703.420.078, C12.050.703.590.132 |
| **NCIT** | `NCIT:C26685` | via MONDO xref |
| **DOID** | `DOID:9667` | |
| **EFO** | `EFO:1001754` | |
| **SNOMED CT** | `415105001` (`SCTID:415105001`) | |
| **UMLS** | `C0000832` | |
| **MedGen** | `49` | |
| **ICD-10-CM** | `O45` (`O45.0-` with coagulation defect; `O45.8-`; `O45.9-`) | ICD-9: 641.20, 640.0, 640.03 |
| **ICD-11** | reported as `JA8C` "Maternal care related to premature separation of placenta" | **UNVERIFIED** — from a secondary web source only; confirm in the WHO ICD-11 browser before curating |
| **OMIM** | none | no Mendelian entry; this is a complex trait |
| **Orphanet** | none | not a rare disease (prevalence ≫ 1/2000) |

**Data-quality flag for curators:** the MONDO textual definition currently retrieved from OLS4 and the Monarch API for `MONDO:0004846` reads *"Vaginal bleeding preceding the 20th week of gestation."* This is **wrong** — that describes threatened abortion, not abruption, and it contradicts MONDO's own synonym set. Worth an upstream MONDO issue; do not propagate this definition into the dismech entry.

### 1.3 Synonyms

`abruptio placentae` · `abruption of placenta` · `premature separation of placenta` · `Abruptio placentae, premature separation of placenta` · `placental abruption (disease)` · `accidental hemorrhage` (historical British usage) · `ablatio placentae` (historical) · `retroplacental hematoma` (the lesion, not strictly the disease) · `Couvelaire uterus` / `uteroplacental apoplexy` (a severe complication, not a synonym).

### 1.4 Nature of the evidence base

Almost all data are **aggregated disease-level** epidemiology from administrative/registry sources (National Inpatient Sample, Nordic birth registries, Kaiser Permanente EHR, NJ vital records) and from placental pathology series. This has a specific and important consequence for a knowledge base: **abruption is ascertained by ICD code or clinician gestalt in most large studies, with no uniform case definition.** Downes et al. (PMID:28329897) name this explicitly: *"There was also considerable variation in, or absence of, the reporting of abruption definitions."* Effect estimates below should be curated with that caveat attached.

Individual-patient EHR-derived work does exist (Oyelese/Kaiser, PMID:38366767; PACER/NJ vital-record linkage, PMID:38273776) and is the best source for recurrence and life-course outcomes.

---

## 2. Etiology

### 2.1 Causal architecture

Abruption is a **final common pathway**, not a single disease. Four upstream routes converge on decidual vessel rupture:

1. **Chronic uteroplacental vasculopathy / ischemic placental disease.** Shallow trophoblast invasion → failure of spiral-artery conversion → high-resistance, high-velocity maternal flow into the intervillous space, decidual necrosis and vessel fragility. This is the route shared with preeclampsia and fetal growth restriction (PMID:24836823).
2. **Acute mechanical shear.** Blunt abdominal trauma, sudden uterine decompression (rupture of membranes with polyhydramnios, delivery of a first twin), short umbilical cord traction, external cephalic version. The uterus is elastic and the placenta is not; deformation shears them apart at the basal plate.
3. **Inflammation/infection.** Chorioamnionitis and PPROM co-travel with abruption; decidual inflammation and hemorrhage are jointly the major decidual contributors to preterm delivery (PMID:15998775).
4. **Hemostatic/thrombotic.** Decidual tissue-factor-dependent hemostasis failure, thrombophilia, and decidual thrombosis with infarction.

### 2.2 Risk factors — quantitative

**Primary source A — Chen et al., BMC Pregnancy Childbirth 2025 (PMID:40140972).** Systematic review + meta-analysis, 54 observational studies, **7,267,241 pregnancies, 47,702 abruption cases**, PROSPERO CRD42024546514.

> "A total of 54 observational studies were included, covering 7,267,241 pregnant women, with 47,702 cases diagnosed with placental abruption."

> "Among these, previous placental abruption (AOR = 2.72, 95% CI [2.16, 3.42]) was found to be the most significant risk factor."

> "Of these, placenta previa (AOR = 7.31, 95% CI [4.78, 11.19]) was identified as the most significant risk factor."

The 18 maternal baseline factors identified (verbatim from abstract): *"maternal age ≥ 35 years, black race, low prepregnancy BMI (< 18.5 kg/m²), unmarried status, smoking during pregnancy, alcohol consumption, inadequate prenatal care (< 4 visits), marijuana use, multiple pregnancy, parity ≥ 3, anemia (hemoglobin < 11 g/dL), previous placental abruption, previous cesarean section, previous miscarriage, previous stillbirth, cervical incompetence, habitual abortions, and assisted reproductive technology."*

The 7 pregnancy-complication factors: *"preterm premature rupture of membranes, preeclampsia, small for gestational age, polyhydramnios, antepartum hemorrhage, gestational hypertension, and placenta previa."*

**Primary source B — Jenabi et al., Syst Rev 2022 umbrella review (PMID:35365209).** Meta-analysis-of-meta-analyses with formal evidence grading. This is the single most important source for *evidence quality*, because its headline finding is negative:

> "There was no risk factor in the present umbrella review with the high level of evidence (class I or II)."

Class III (suggestive) factors, with effect sizes verbatim:

| Factor | Effect |
|---|---|
| Cocaine use | RR 4.55 (95% CI 1.78–6.50) |
| Chronic hypertension | OR 3.13 (95% CI 2.04–4.80) |
| Assisted reproductive technology | OR 1.87 (95% CI 1.70–2.06) |
| Maternal smoking | OR 1.80 (95% CI 1.75–1.85); RR 1.65 (1.51–1.80) |
| Advanced maternal age | OR 1.44 (95% CI 1.35–1.54) |
| Endometriosis | OR 1.40 (95% CI 1.12–1.76) |
| Prior cesarean section | RR 1.38 (95% CI 1.35–1.42) |
| Maternal asthma | RR 1.29 (95% CI 1.14–1.47) |

Class IV (weak): uterine leiomyoma OR 2.63 (1.38–3.88); marijuana use OR 1.78 (1.32–2.40); preeclampsia OR 1.73 (1.47–2.04); pre-pregnancy underweight OR 1.38 (1.12–1.70).

**Primary source C — Ananth, Smulian & Vintzileos, Obstet Gynecol 1999 (PMID:10214847).** The landmark smoking meta-analysis, 13 studies, 1,358,083 pregnancies:

> "Smoking was associated with a 90% increase in the risk of placental abruption (odds ratio [OR] 1.9, 95% confidence interval [CI] 1.8, 2.0)."

> "Pooled population attributable risk percentage for each stratum ranged between 15% and 25%, implying that 15-25% of placental abruption episodes are attributable to cigarette smoking."

> "In the presence of smoking, the risk of abruption was further increased due to chronic hypertension, mild or severe preeclampsia, or chronic hypertension with superimposed preeclampsia."

That last sentence is a **directly citable gene-free interaction claim** (smoking × hypertensive disorder super-additivity) and is the cleanest documented exposure–exposure interaction in this disease.

**Primary source D — prior cesarean.** Keag, Norman & Stock, PLoS Med 2018 (PMID:29360829), 79 cohort studies + 1 RCT, 29,928,274 participants:

> "Pregnancy following cesarean delivery was associated with increased risk of placenta previa (OR 1.74, 1.62 to 1.87; n = 7,101,692; 10 studies), placenta accreta (OR 2.95, 1.32 to 6.60; n = 705,108; 3 studies), and placental abruption (OR 1.38, 1.27 to 1.49; n = 5,667,160; 6 studies)."

**Primary source E — recent NIS analysis.** Wright, Friedman, Ananth & Wen, Am J Perinatol 2026 (PMID:40940025), 80.2 million deliveries 2000–2020: *"Abruption was associated with multiple gestations, hypertensive diagnoses, diabetes, asthma, and Medicaid insurance."*

### 2.3 Genetic risk factors

No causal Mendelian gene. Susceptibility is polygenic and, critically, **two-genome**: maternal *and* fetal/placental genotypes both contribute, and their interaction matters.

Workalemahu et al., Placenta 2018 (PMID:29884306) — GWAS + GWAS meta-analysis, Peruvian PAGE and PAPE cohorts (959 cases / 1553 controls in meta-analysis):

> "Accumulating epidemiological evidence points to strong genetic susceptibility to placental abruption (PA). However, characterization of genes associated with PA remains incomplete."

> "Independent loci (linkage-disequilibrium<0.80) suggestively associated with PA (P-value<5e-5) included rs4148646 and rs2074311 in ABCC8, rs7249210, rs7250184, rs7249100 and rs10401828 in ZNF28, rs11133659 in CTNND2, and rs2074314 and rs35271178 near KCNJ11 in the PAGE GWAS. Similarly, independent loci suggestively associated with PA in the GWAS meta-analysis included rs76258369 near IRX1, and rs7094759 and rs12264492 in ADAM12."

> "Functional analyses of these genes showed trophoblast-like cell interaction, as well as networks involved in endocrine system disorders, cardiovascular diseases, and cellular function."

**Curatorial caution:** these are *suggestive* (P < 5×10⁻⁵), not genome-wide significant (5×10⁻⁸), in a modest sample. Curate them as `SUSCEPTIBILITY` with the significance threshold recorded, and consider a `KNOWLEDGE_GAP` discussion noting that no locus has reached genome-wide significance or been replicated in an independent ancestry.

Workalemahu et al., Int J Mol Epidemiol Genet 2013 (PMID:24046805) — 470 cases / 473 controls, Cardio-Metabo Chip:

> "The top hit in the GWAS analyses was rs1238566 (empirical P-value=1.04e-4 and FDR-adjusted P-value=5.65E-04) in FLI-1 gene, a megakaryocyte-specific transcription factor."

> "SNPs known to regulate MB (e.g. CAMK2B, NR1H3, PPARG, PRKCA, and THRB) and OP (e.g., COX5A, and NDUF family of genes) were associated with PA risk (P-value <0.05)."

FLI1 is a megakaryocyte/endothelial transcription factor — biologically coherent with a hemostatic-failure model.

**Verified HGNC identifiers** (HGNC REST API, this session; note dismech convention is lowercase `hgnc:`):

| Gene | HGNC | Role |
|---|---|---|
| ABCC8 | `hgnc:59` | GWAS suggestive locus (SUR1, K-ATP channel) |
| KCNJ11 | `hgnc:6257` | GWAS suggestive locus (Kir6.2, K-ATP channel) |
| ZNF28 | `hgnc:13073` | GWAS suggestive locus |
| CTNND2 | `hgnc:2516` | GWAS suggestive locus (δ-catenin) |
| ADAM12 | `hgnc:190` | GWAS meta-analysis locus; also a placental serum analyte |
| IRX1 | `hgnc:14358` | GWAS meta-analysis locus |
| FLI1 | `hgnc:3749` | top candidate hit, megakaryocytic TF |
| F5 | `hgnc:3542` | Factor V Leiden thrombophilia |
| F2 | `hgnc:3535` | prothrombin G20210A; also the thrombin effector |
| F3 | `hgnc:3541` | decidual tissue factor — the central hemostatic effector |
| F2R | `hgnc:3537` | PAR-1, the thrombin receptor mediating inflammation |
| MTHFR | `hgnc:7436` | homocysteine/folate route (weak/inconsistent) |
| SERPINE1 | `hgnc:8583` | PAI-1, thrombin-induced |
| MMP1 | `hgnc:7155` | thrombin-induced collagenase → PPROM |
| CXCL8 | `hgnc:6025` | IL-8, thrombin-induced neutrophil chemoattractant |
| PGR | `hgnc:8910` | progesterone receptor — functional withdrawal target |
| CSF2 | `hgnc:2434` | GM-CSF, thrombin-induced membrane weakening |
| IL11 | `hgnc:5966` | thrombin/IL-1β-induced decidual cytokine |
| PAPPA | `hgnc:8602` | first-trimester predictive analyte |
| AFP | `hgnc:317` | second-trimester predictive analyte |

**Thrombophilia.** The best-quality synthesis is the TREATS HTA (Wu et al., Health Technol Assess 2006, PMID:16595080), 72 pregnancy studies:

> "Significant risks for individual thrombophilic defects were also established for early, recurrent and late pregnancy loss; preeclampsia; placental abruption; and intrauterine growth restriction."

Note the counter-current: contemporary obstetric practice has largely **abandoned** thrombophilia screening for placenta-mediated complications because trials of anticoagulation have not shown benefit. Curate the association as real-but-small and flag the therapeutic-inference gap explicitly (a `KNOWLEDGE_GAP` discussion is appropriate: association ≠ actionable). The enoxaparin trial NCT00986765 ("Prevention of Maternal and Perinatal Complications by Enoxaparin in Women With Previous Severe…", COMPLETED, Phase 3) is the relevant trial anchor.

### 2.4 Protective factors

Only three protective factors reached significance in Chen 2025 (the abstract does not name them individually; the full text is needed — **flag as a retrieval gap**). Practically supported protective exposures:

- **Smoking cessation before/early in pregnancy** — implied by the 15–25% population attributable fraction (PMID:10214847). NCIT: `NCIT:C17427` Smoking Cessation.
- **Treatment of mild chronic hypertension.** This is now RCT-grade. The CHAP trial (Tita et al., NEJM 2022, PMID:35363951; **NCT02299414**) used placental abruption inside its primary composite: *"The primary outcome was a composite of preeclampsia with severe features, medically indicated preterm birth at less than 35 weeks' gestation, placental abruption, or fetal or neonatal death."* Result: *"The incidence of a primary-outcome event was lower in the active-treatment group than in the control group (30.2% vs. 37.0%), for an adjusted risk ratio of 0.82 (95% confidence interval [CI], 0.74 to 0.92; P<0.001)."* **Caveat for curators:** this is a composite-outcome benefit, not a demonstrated abruption-specific reduction. Do not curate as "antihypertensives prevent abruption" without that qualifier.
- **Adequate prenatal care (≥4 visits)** — the inverse of the "inadequate prenatal care" risk factor.

No protective *genetic* variant has been identified. State this as absent, not as unknown.

### 2.5 Gene–environment interaction

Genuinely thin literature. The strongest documented interaction is **maternal genome × placental genome**, not gene × exposure: Workalemahu et al. showed that *variations in the placental genome and interactions between maternal–placental genetic variations may contribute to PA risk* (companion study, PMC4280220). The best-quantified *exposure × exposure* interaction is smoking × hypertensive disorders (PMID:10214847, quoted in §2.2).

This is a legitimate `KNOWLEDGE_GAP` for the entry: no GxE study of adequate power exists for abruption.

---

## 3. Phenotypes

### 3.1 Maternal clinical presentation

| Phenotype | HPO term (verified) | Category | Frequency | Notes |
|---|---|---|---|---|
| Vaginal bleeding | `HP:0034263` Abnormal vaginal bleeding | Clinical sign | FREQUENT (~70–80%) | 20–30% **concealed** — blood trapped retroplacentally; absence does not exclude |
| Abdominal pain | `HP:0002027` Abdominal pain | Symptom | FREQUENT | Classically *"out of proportion to the volume of bleeding"* when concealed (Merck Manual Professional) |
| Uterine tenderness / hypertonus | *(no precise HP term; MeSH scope note calls it "uterine MUSCLE HYPERTONIA")* | Clinical sign | FREQUENT | "board-like" tetanic uterus in severe cases; use `preferred_term: Uterine tenderness and hypertonus` with no `term:` or map to a broad parent |
| Back pain | `HP:0003418` Back pain | Symptom | OCCASIONAL | Prominent with posterior placenta |
| Fetal distress (non-reassuring FHR) | `HP:0025116` Fetal distress | Clinical sign | FREQUENT | 79% in the CP-causing cohort (PMID:22805996) |
| Hypovolemic shock | `HP:0031274` Hypovolemic shock | Clinical sign | OCCASIONAL | Sher class 3 |
| Disseminated intravascular coagulation | `HP:0005521` Disseminated intravascular coagulation (acute: `HP:0011880`) | Lab/clinical | OCCASIONAL | OR 6.30 (6.00–6.61) vs no abruption (PMID:40940025) |
| Hypofibrinogenemia | `HP:0011900` Hypofibrinogenemia | Lab abnormality | OCCASIONAL | *"Serum fibrinogen and fibrin-split products (the most sensitive indicator)"* (Merck Manual Professional) |
| Thrombocytopenia | `HP:0001873` Thrombocytopenia | Lab abnormality | OCCASIONAL | consumptive |
| Anemia | `HP:0001903` Anemia | Lab abnormality | FREQUENT | both a risk factor and a consequence |
| Post-partum hemorrhage | `HP:0011891` Post-partum hemorrhage | Complication | OCCASIONAL | OR 1.76 (1.72–1.80) (PMID:40940025) |
| Acute kidney injury | `HP:0001919` Acute kidney injury | Complication | RARE | listed by Downes 2017 (PMID:28329897) |
| Preeclampsia (co-occurring) | `HP:0100602` Preeclampsia | Comorbid | OCCASIONAL | ischemic placental disease overlap |
| Uterine rupture | `HP:0100718` Uterine rupture | Differential/complication | RARE | |

**Couvelaire uterus (uteroplacental apoplexy)** — blood dissecting into the myometrium producing a bruised, boggy, poorly contractile uterus — has no HPO term and no obvious ontology anchor. Curate as free-text `preferred_term` with a histopathology entry; it is a candidate for the Xogenesis-style open-ontology treatment.

### 3.2 Fetal / neonatal phenotypes

| Phenotype | HPO term (verified) | Frequency | Notes |
|---|---|---|---|
| Premature birth | `HP:0001622` Premature birth | VERY FREQUENT | the dominant fetal consequence |
| Stillbirth | `HP:0003826` Stillbirth | FREQUENT within abruption | *"The majority of deaths (77%) occurred in utero"* (PMID:23072758) |
| Neonatal death | `HP:0003811` Neonatal death | OCCASIONAL | |
| Small for gestational age | `HP:0001518` Small for gestational age | FREQUENT | with chronic abruption |
| Intrauterine growth retardation | `HP:0001511` Intrauterine growth retardation | FREQUENT | |
| Neonatal asphyxia | `HP:0012768` Neonatal asphyxia | FREQUENT in severe abruption | umbilical arterial pH 6.728 ± 0.164 in the CP cohort (PMID:22805996) |
| Cerebral palsy | `HP:0100021` Cerebral palsy | OCCASIONAL (long-term) | see §11 |
| Oligohydramnios | `HP:0001562` Oligohydramnios | OCCASIONAL | chronic abruption |
| Preterm premature rupture of membranes | `HP:6000310` Preterm premature rupture of membranes | FREQUENT | bidirectional with abruption |

Downes et al. 2017 (PMID:28329897) enumerate the full outcome set verbatim:

> "Abruption was associated with elevated risk of cesarean delivery, postpartum hemorrhage and transfusion, preterm birth, intrauterine growth restriction or low birth weight, perinatal mortality, and cerebral palsy. Additional maternal outcomes included relaparotomy, hysterectomy, sepsis, amniotic fluid embolism, venous thromboembolism, acute kidney injury, and maternal intensive care unit admission. Additional perinatal outcomes included acidosis, encephalopathy, severe respiratory disorders, necrotizing enterocolitis, acute kidney injury, need for resuscitation, chronic lung disease, infant death, and epilepsy."

### 3.3 Severity grading (Sher classification)

Widely used; from StatPearls (NBK482335). Curate as a `Subtype` set or as a severity scale:

- **Class 0 (asymptomatic):** retroplacental clot found only on post-delivery placental inspection.
- **Class 1 (mild):** minimal/no vaginal bleeding, slight uterine tenderness, normal maternal vitals, no fetal distress.
- **Class 2 (moderate):** none-to-moderate bleeding, significant uterine tenderness with tetanic contractions, maternal tachycardia and orthostatic change, fetal distress, hypofibrinogenemia.
- **Class 3 (severe):** minimal-to-heavy bleeding, board-like tetanic uterus, maternal shock, coagulopathy, fetal death.

Classes 0–1 correspond to partial/marginal separation; classes 2–3 to complete/central separation. StatPearls notes ~70% of cases are low-risk. Page grading (0–3) is an equivalent older scheme.

### 3.4 Quality-of-life impact

Under-studied and a real evidence gap. Documented domains, mostly indirect:

- **Maternal:** ICU admission, transfusion, emergency hysterectomy (permanent loss of fertility), and — for those with fetal death — bereavement and subsequent-pregnancy anxiety. No abruption-specific EQ-5D/SF-36/PROMIS instrument exists.
- **Offspring:** cerebral palsy (`HP:0100021`) and epilepsy carry lifelong functional burden; chronic lung disease of prematurity.
- **Recurrence anxiety** in subsequent pregnancy is clinically salient given the ~5× recurrence odds (PMID:38366767) but is unmeasured in the literature.

Curate as `KNOWLEDGE_GAP`: no validated disease-specific QoL instrument.

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes

**None.** Placental abruption has no Mendelian form, no OMIM phenotype entry, and no gene with definitive ClinGen gene–disease validity. This should be stated affirmatively in the entry — an empty `genetic:` block invites a reviewer to think it was simply not curated.

### 4.2 Susceptibility loci

See §2.3 for the verified list. Summary for the `genetic:` block, all `relationship_type: SUSCEPTIBILITY`:

- **ABCC8** (`hgnc:59`) rs4148646, rs2074311 — and the physically adjacent **KCNJ11** (`hgnc:6257`) rs2074314, rs35271178. These two encode the SUR1/Kir6.2 subunits of the same ATP-sensitive potassium channel; the two "independent" signals are likely one locus. Biologically plausible via vascular smooth-muscle tone and trophoblast metabolism.
- **ZNF28** (`hgnc:13073`) — four SNPs, function unknown.
- **CTNND2** (`hgnc:2516`) rs11133659 — δ-catenin, adhesion/junctional.
- **ADAM12** (`hgnc:190`) rs7094759, rs12264492 — placental metalloprotease, also a first-trimester serum marker of placental function. The convergence of a genetic and a biochemical signal on the same gene makes ADAM12 the most interesting single candidate.
- **IRX1** (`hgnc:14358`) rs76258369 — developmental homeobox TF.
- **FLI1** (`hgnc:3749`) rs1238566 — megakaryocyte/endothelial TF (PMID:24046805).

**Variant classification:** all are common non-coding/intronic SNPs, not ACMG-classifiable pathogenic variants. Do not attempt ACMG classification; record as GWAS-suggestive association only. Allele frequencies are common (this is a common-variant disease); the cohorts were Peruvian, so transferability to other ancestries is unestablished — a genuine `KNOWLEDGE_GAP`.

**Somatic vs germline:** germline (maternal and/or fetal). No somatic contribution.

**Functional consequence:** unknown for all loci; none has a demonstrated molecular mechanism. Say so.

### 4.3 Thrombophilia variants

- **F5** (`hgnc:3542`) c.1601G>A p.Arg534Gln — Factor V Leiden, `rs6025`. A small case-control series reported 8/46 (18%) abruption cases vs 1/46 (2%) controls carrying FVL with APC resistance (secondary report; **verify the primary PMID before curating** — I could not retrieve it directly this session).
- **F2** (`hgnc:3535`) c.*97G>A — prothrombin G20210A, `rs1799963`.
- **MTHFR** (`hgnc:7436`) c.665C>T p.Ala222Val (`rs1801133`, the "C677T") — hyperhomocysteinemia route; associations are weak and inconsistent, and TREATS found MTHFR/hyperhomocysteinaemia *not* associated with postoperative VTE, undercutting the general thrombophilia framing for this variant.

Curate these as `SUSCEPTIBILITY` with `frequency` bands, anchored on TREATS (PMID:16595080), and add the therapeutic-inference caveat from §2.3.

### 4.4 Modifier genes

None established.

### 4.5 Epigenetics

No abruption-specific methylation or histone study of adequate quality was identified in this search. Adjacent evidence exists for ischemic placental disease broadly (shared epigenetic regulation between preeclampsia and IUGR was reported in placental microarray work), but nothing abruption-specific. **Flag as an explicit gap** — an obvious high-value target given the acute-on-chronic model.

### 4.6 Chromosomal abnormalities

Not applicable. No aneuploidy, translocation, or CNV association. Chromosomal microarray, karyotype and FISH have no role in abruption workup (they may be indicated for an associated stillbirth, which is a different indication).

---

## 5. Environmental Information

### 5.1 Chemical / toxicant exposures

- **Tobacco smoke / nicotine** (`CHEBI:18723` nicotine). Strongest modifiable factor: OR 1.9 (1.8–2.0), 15–25% population attributable fraction, with a documented dose–response — *"the OR increased with increasing number of cigarettes smoked"* (PMID:10214847). Mechanism: nicotine-mediated vasoconstriction plus carbon-monoxide-driven chronic hypoxia → decidual necrosis and vessel fragility.
- **Cocaine** (`CHEBI:27958`). RR 4.55 (1.78–6.50) — the largest single effect size for any exposure (PMID:35365209). Mechanism: acute catecholaminergic vasospasm and hypertensive surge causing decidual vessel rupture. James & Coles (PMID:1765257): *"It not only poses a health risk to the pregnant woman, but can precipitate premature labor and abruptio placentae."*
- **Cannabis/marijuana.** OR 1.78 (1.32–2.40), class IV weak evidence.
- **Alcohol.** Identified as an independent risk factor in Chen 2025.
- **Air pollution / preconception environmental exposures.** Covered in the Jenabi umbrella review's remit (PMID:35365209); no exposure reached class I/II evidence. Treat any PM2.5–abruption claim as preliminary.

### 5.2 Physical / mechanical

- **Blunt abdominal trauma** — motor vehicle crashes, falls, intimate partner violence. Abruption can occur with deceleration injury and *without* direct uterine impact, and can present up to 24 h after the event, which is why post-trauma cardiotocographic monitoring is standard. Trauma screening should include tactful assessment for abuse (StatPearls).
- **Sudden uterine decompression** — membrane rupture with polyhydramnios (`HP:0001561`), delivery of the first twin.
- **Short umbilical cord / velamentous cord insertion.** Ananth 2005 (PMID:15672024) identified *"short umbilical cord, and velamentous cord insertion"* among the determinants tracking the temporal trend in abruption.

### 5.3 Lifestyle / demographic

Advanced maternal age ≥35 (OR 1.44), parity ≥3, pre-pregnancy underweight BMI <18.5 (OR 1.38), unmarried status, inadequate prenatal care <4 visits, Medicaid insurance (PMID:40940025) — the last two being markers of access rather than biology, and important to curate as such rather than as causal.

### 5.4 Infectious agents

No single pathogen causes abruption. **Chorioamnionitis** (ascending polymicrobial intraamniotic infection — *Ureaplasma*, *Mycoplasma hominis*, *Gardnerella*, group B *Streptococcus*, *Fusobacterium*, *E. coli*) is both a determinant of abruption trends (PMID:15672024) and a co-traveler with PPROM. Simhan & Canavan (PMID:15715592): *"PPROM is associated with significant maternal and neonatal morbidity and mortality from infection, umbilical cord compression, placental abruption and preterm birth."* They report *"The frequency of positive cultures obtained by transabdominal amniocentesis at the time of presentation with PPROM in the absence of labour is 25-40%."*

The best mechanistic bridge between infection and abruption is the thrombin×TLR4 synergy documented by Mhatre et al. (PMID:27108773) — see §6.4.

---

## 6. Mechanism / Pathophysiology

This is the section that should carry the pathograph. I propose an **eight-node chain with two upstream triggers converging**, plus an inflammatory amplification limb.

### 6.1 The causal chain (proposed pathophysiology nodes)

**Trigger A — Impaired spiral artery remodeling / decidual vasculopathy** · `biological_scale: TISSUE`
Shallow extravillous trophoblast invasion leaves maternal spiral arteries incompletely converted, retaining vasoreactivity and delivering high-velocity flow into the intervillous space. Decidual arterioles develop atherosis and necrosis. This is the chronic arm.
- Cell types: `CL:0008036` extravillous trophoblast; `CL:2000002` decidual cell; endothelial cell of the spiral artery
- Processes: `GO:0061450` trophoblast cell migration (`modifier: DECREASED`); `GO:0071456` cellular response to hypoxia (`INCREASED`)
- Anatomy: `UBERON:0000453` decidua basalis
- Evidence: PMID:24836823 (ischemic placental disease framework); PMID:28178056 (first-trimester analyte abnormalities predict abruption)

**Trigger B — Acute mechanical shear or vasospasm** · `biological_scale: TISSUE`
Trauma, sudden decompression, or cocaine-induced vasospasm mechanically or hemodynamically ruptures decidual vessels. StatPearls: *"Since the uterus is elastic but the placenta is not, sudden uterine stretching causes the vascular structures connecting them to tear."*

**Node 1 — Decidual vessel rupture and hemorrhage into the decidua basalis** · `biological_scale: TISSUE`
The defining lesion. Normally prevented by constitutive decidual tissue factor. Lockwood et al. (PMID:19720393): *"In human pregnancy, decidual cell-expressed tissue factor (TF) prevents decidual hemorrhage (abruption)."* and *"TF expression is highest in decidual cells"* — i.e. the decidua is a hemostatically privileged tissue, and abruption is the failure of that privilege.
- Gene: F3 (`hgnc:3541`)
- Anatomy: `UBERON:0000453` decidua basalis
- Cell type: `CL:2000002` decidual cell

**Node 2 — Retroplacental hematoma formation and placental separation** · `biological_scale: TISSUE`
Accumulating blood dissects the basal plate, propagating separation and further vessel disruption — a positive-feedback loop. This is the **Xogenesis-shaped node** of the entry: a pathological structure (retroplacental hematoma) forms at a defined anatomical site. If the `granuloma_formation`/`thrombogenesis` Xogenesis convention is applied, the anchors would be an OGMS pathological-formation process at `UBERON:0000453` decidua basalis, forming a hematoma continuant. Note that thrombogenesis (`kb/modules/thrombogenesis`) is a plausible partial conformance target for the clot itself, though the causal direction is inverted here (hemorrhage first, clot second).
- Processes: `GO:0007596` blood coagulation; `GO:0030168` platelet activation

**Node 3 — Loss of gas-exchange surface and acute fetoplacental hypoxia** · `biological_scale: ORGANISM`
The separated area is functionally excluded from maternal perfusion. Fetal compromise scales with the fraction separated; classical teaching is that >50% separation is generally incompatible with fetal survival.
- Phenotype: `HP:0025116` Fetal distress; `HP:0012768` Neonatal asphyxia
- Process: `GO:0071456` cellular response to hypoxia (`INCREASED`)

**Node 4 — Local thrombin generation (the mechanistic hub)** · `biological_scale: MOLECULAR`
Decidual TF/FVIIa cleaves prothrombin; the retroplacental clot is a thrombin factory. Everything downstream of node 4 in this entry is thrombin-driven — this is the node other diseases would `conforms_to`.
- Genes: F3 (`hgnc:3541`), F2 (`hgnc:3535`)
- Process: `GO:0007596` blood coagulation (`INCREASED`)

**Node 5 — PAR-1-mediated decidual and endothelial inflammatory activation** · `biological_scale: CELLULAR`
Thrombin signals through protease-activated receptor 1 (F2R, `hgnc:3537`), converting a hemostatic signal into an inflammatory one. Mhatre et al. (PMID:27108773):

> "Thrombin significantly and synergistically augmented LPS-induced HEEC secretion of interleukin (IL)-6, IL-8, granulocyte colony-stimulating factor (G-CSF), and growth-regulated oncogene-alpha (GRO-α), and significantly augmented monocyte chemotactic protein (MCP)-1, tumor necrosis factor-alpha (TNF-α), and vascular endothelial growth factor (VEGF) secretion additively."

> "Similar to thrombin, a PAR1 agonist synergistically augmented the LPS-induced HEEC secretion of inflammatory IL-6, IL-8, G-CSF, and GRO-α."

> "…suggesting a mechanism by which intrauterine abruption and bacterial infection may together be associated with an aggravated uterine inflammatory response."

This synergy is the mechanistic explanation for the epidemiological co-occurrence of abruption and chorioamnionitis and is worth curating as its own edge.
- Process: `GO:0070493` thrombin-activated receptor signaling pathway (`INCREASED`); `GO:0006954` inflammatory response (`INCREASED`)
- Cell types: `CL:2000002` decidual cell; endothelial cell (human endometrial endothelial cell)
- Evidence source: **IN_VITRO**

**Node 6 — Decidual neutrophil recruitment via thrombin-induced IL-8** · `biological_scale: CELLULAR`
Lockwood et al., Am J Pathol 2005 (PMID:16251427) — the cleanest in-vivo-plus-in-vitro pairing in this literature:

> "Abruptions were associated with a marked decidual neutrophil infiltration that peaked after PPROM, whereas decidua from gestational age-matched controls were virtually devoid of neutrophils."

> "Neutrophil infiltrates co-localized with fibrin deposition."

> "…thrombin (0.1 to 2.5 U/ml) elicited a dose-dependent elevation in secreted IL-8 (P<0.05) with 2.5 U/ml of thrombin increasing IL-8 levels by >14-fold in E2 and E2+medroxyprogesterone incubations."

- Gene: CXCL8 (`hgnc:6025`)
- Process: `GO:0030593` neutrophil chemotaxis (`INCREASED`)
- Cell type: neutrophil (`CL:0000775` neutrophil — *verify label before curating*)
- Evidence: the immunostaining arm is HUMAN_CLINICAL; the decidual-cell culture arm is IN_VITRO. **Split into two evidence items with different `evidence_source` values.**

**Node 7 — Matrix metalloproteinase-driven membrane weakening → PPROM** · `biological_scale: MOLECULAR`
Rosen et al. (PMID:12380602):

> "MPA strongly inhibited MMP-1 levels in endometrial stromal and term decidual cells. However, thrombin overcame this suppression, producing MMP-1 levels that were several-fold higher than control levels."

> "Extrapolation of thrombin-enhanced MMP-1 expression in cultured endometrial stromal and decidual cells to the in vivo pregnant state provides an explanation for the strong association between placental abruption and preterm membrane rupture."

Norwitz et al. (PMID:17403427) tested and *excluded* the alternative plasminogen-activator route, concluding: *"abruption-associated decidual proteolysis and preterm labor is mediated primarily by thrombin-enhanced matrix metalloproteinase expression rather than an indirect effect on the plasminogen activator/inhibitor system."* That is a useful **REFUTE/negative** evidence item — thrombin raised PAI-1 without raising uPA or tPA.
- Genes: MMP1 (`hgnc:7155`); SERPINE1 (`hgnc:8583`) for the PAI-1 arm
- Process: `GO:0022617` extracellular matrix disassembly (`INCREASED`); `GO:0042730` fibrinolysis
- Phenotype: `HP:6000310` Preterm premature rupture of membranes
- Evidence source: **IN_VITRO**

**Node 8 — Functional progesterone withdrawal and myometrial activation → preterm delivery** · `biological_scale: CELLULAR`
Lockwood et al., Am J Pathol 2012 (PMID:23058370):

> "In cultured DCs, thrombin inhibited PR but not GR mRNA levels, reduced PR binding to DNA and [(3)H]progesterone binding to PR, and enhanced phosphorylated but not total ERK1/2 levels."

> "Thus, abruption-associated PTD is initiated by functional progesterone withdrawal, as indicated by significantly reduced DC nuclear expression of PR-A and PR-B. Functional withdrawal of progesterone results in increased p-ERK1/2, and is thus one pathway initiating abruption-associated PTD."

- Genes: PGR (`hgnc:8910`)
- Process: `GO:0070471` uterine smooth muscle contraction (`INCREASED`)
- Phenotype: `HP:0001622` Premature birth
- Evidence source: mixed IN_VITRO (culture) + HUMAN_CLINICAL (immunohistochemistry on abruption vs control placentas)

**Node 9 — Consumptive coagulopathy / DIC** · `biological_scale: ORGANISM`
Massive thromboplastin (tissue factor) release from the disrupted decidua into the maternal circulation consumes fibrinogen and platelets. Abruption is the classic obstetric cause of DIC.
- Phenotypes: `HP:0005521` DIC (acute `HP:0011880`); `HP:0011900` Hypofibrinogenemia; `HP:0001873` Thrombocytopenia; `HP:0031274` Hypovolemic shock
- Evidence: PMID:40940025 (DIC OR 6.30, 95% CI 6.00–6.61)

### 6.2 Additional cytokine mediators

Cakmak et al. (PMID:15998775) add IL-11 (`hgnc:5966`) to the thrombin-responsive set, with a striking magnitude:

> "IL-1beta and thrombin elevated IL-11 output during incubations with E2 [24-fold (P < 0.05) and 120-fold (P < 0.05), respectively]. These increases were blunted by the addition of MPA [13-fold (P < 0.05) and 36-fold (P < 0.05), respectively]."

> "Because excess IL-1beta and thrombin generation are associated with chorioamnionitis- and abruption-related PTD, respectively, these findings add to our understanding of the genesis of inflammation- and abruption-associated prematurity."

Note the clean mechanistic dissociation the authors draw: **IL-1β is the chorioamnionitis signal; thrombin is the abruption signal**, converging on the same decidual effectors. That is a good candidate for two `mechanistic_hypotheses` groups or for a shared downstream node with two distinct upstream edges.

CSF2/GM-CSF (`hgnc:2434`) is a further thrombin-induced decidual mediator implicated in fetal-membrane weakening (Am J Pathol, "Thrombin-Induced Decidual Colony-Stimulating Factor-2 Promotes Abruption-Related Preterm Birth by Weakening Fetal Membranes" — **PMID not retrieved this session; verify before curating**).

### 6.3 Immune involvement

Bączkowska et al., Int J Mol Sci 2021 (PMID:34205566) — systematic review, 708 records screened, 22 analyzed:

> "The available evidence indicates that the disruption of the immunological processes on the maternal-fetal interface plays a crucial role in the pathophysiology of placental abruption. The features of chronic non-infectious inflammation and augmented immunological cytotoxic response were found to be present in placental abruption samples in the reviewed studies. Various molecules participate in this process, with only a few being examined. More advanced research is needed to fully explain this complicated process."

That final sentence is an ideal anchor for a `KNOWLEDGE_GAP` discussion. Decidual NK cells (`CL:0002343` decidual natural killer cell, human; `CL:4052028` uterine natural killer cell) are the obvious cell population to name, given their established role in spiral-artery remodeling.

### 6.4 Tissue damage mechanisms

Ischemia (loss of maternal perfusion to the separated segment), hemorrhage, decidual necrosis, infarction, and — for the fetus — hypoxic-ischemic injury. Oxidative stress is implicated via the ischemic placental disease framework and via the mitochondrial-biogenesis/OXPHOS candidate genes of PMID:24046805 (CAMK2B, NR1H3, PPARG, PRKCA, THRB; COX5A and NDUF-family).

### 6.5 Molecular profiling

- **Transcriptomics:** no abruption-specific placental RNA-seq dataset of note was located. The Bączkowska review's 22-study base is candidate-molecule immunohistochemistry, not unbiased omics. **Substantial gap.** Adjacent resources: GTEx (no placenta), Human Cell Atlas maternal–fetal interface reference (Vento-Tormo et al.).
- **Proteomics / metabolomics / lipidomics:** none abruption-specific identified.
- **Single-cell / spatial:** none abruption-specific. The maternal–fetal interface single-cell atlas would be the natural reference tissue for a first study; note as an opportunity, not a finding.
- **Functional genomics screens:** none.

Be explicit in the entry that the omics layer for this disease is essentially empty. That is itself a curatable fact.

---

## 7. Anatomical Structures Affected

### 7.1 Organ level

- **Primary:** `UBERON:0001987` placenta — specifically the maternal/basal aspect.
- **Primary (maternal):** `UBERON:0002450` decidua, and precisely `UBERON:0000453` **decidua basalis** — the site of the initiating hemorrhage. Brandt & Ananth locate the lesion at *"the interface between the decidua… and the placenta."* StatPearls: *"The histologic finding most strongly associated with acute abruption is hemorrhage in the decidua basalis with underlying parenchymal indentation."*
- Also relevant: `UBERON:8600019` placental basal plate; `UBERON:0010008` placental cotyledon; `UBERON:0006878` decidua parietalis (uninvolved comparator).
- **Secondary maternal:** uterus/myometrium (Couvelaire uterus), systemic coagulation system, kidney (`HP:0001919` AKI), pituitary (Sheehan syndrome after massive hemorrhage), cerebrovasculature (long-term, §11).
- **Secondary fetal:** brain (hypoxic-ischemic injury), lung (prematurity), gut (necrotizing enterocolitis).
- **Body systems:** reproductive, cardiovascular/hematologic, and — downstream — nervous and respiratory.

### 7.2 Tissue and cell level

| Cell / tissue | CL term (verified) | Role |
|---|---|---|
| Decidual cell | `CL:2000002` | tissue-factor-expressing hemostatic guardian; thrombin-responsive effector |
| Stromal cell of endometrium | `CL:0002255` | precursor of decidual cells; used in the culture models |
| Extravillous trophoblast | `CL:0008036` | spiral-artery remodeling; deficient invasion is Trigger A |
| Placental villous trophoblast | `CL:2000060` | gas exchange surface lost on separation |
| Anchoring trophoblast | `CL:0002219` | basal-plate attachment |
| Decidual natural killer cell (human) | `CL:0002343` | immune arm of spiral-artery remodeling |
| Uterine natural killer cell | `CL:4052028` | as above |
| Decidual pericyte | `CL:0008033` | vessel-wall stability |
| Endothelial cell (endometrial/spiral artery) | *human endometrial endothelial cell — no exact CL term; use a parent endothelial CL* | thrombin/PAR-1 inflammatory amplifier |
| Neutrophil | `CL:0000775` (*verify label*) | thrombin/IL-8-recruited effector; co-localizes with fibrin |
| Uterine smooth muscle cell / myometrium | | hypertonus, Couvelaire infiltration |

### 7.3 Subcellular level

No distinctive subcellular pathology. Relevant GO cellular components if needed: plasma membrane (PAR-1 signaling), extracellular region/extracellular matrix (MMP-1 substrate), mitochondrion (OXPHOS candidate genes, PMID:24046805).

### 7.4 Localization and laterality

The lesion is focal within a single organ. The clinically meaningful spatial axes are:

- **Marginal vs central separation.** Marginal (edge) separation → revealed bleeding, lower risk. Central separation → concealed hematoma, higher risk, and can be entirely occult. This is the anatomical basis of the concealed-vs-revealed dichotomy and should be curated.
- **Anterior vs posterior placental location.** Posterior placentation makes sonographic detection harder and produces back-predominant pain — a real diagnostic-performance modifier.
- **Fraction of placental surface separated** — the principal determinant of fetal outcome.

Laterality in the conventional sense (unilateral/bilateral) does not apply.

---

## 8. Temporal Development

### 8.1 Onset

- **Age of onset:** not applicable in the usual sense. Onset is defined by *gestational age*, which is the correct time axis for this entry. Merck Manual Professional states incidence peaks at 24–26 weeks. StatPearls: *"Most cases develop before 37 weeks gestation."* Brandt & Ananth (PMID:37164498) is specifically devoted to the late-preterm (34–36 wk) and term (≥37 wk) window, which behaves differently — better fetal outcomes, but a substantial share of the total burden.
- **Onset pattern:** bimodal. Acute abruption is **abrupt** (minutes). Chronic abruption is **insidious**, presenting as *"continued or intermittent dark brown spotting"* (Merck Manual Professional), sometimes with oligohydramnios and growth restriction — the "chronic abruption–oligohydramnios sequence."

The strongest evidence that the disease *begins* long before it presents is the biomarker work. Ananth et al., Obstet Gynecol 2017 (PMID:28178056), 35,307 women / 250 abruption cases from the FASTER cohort:

> "We hypothesized that the origins of abruption may extend to the stages of placental implantation; however, there are no reliable markers to predict its development."

> "Women with an abnormally low pregnancy-associated plasma protein A (fifth percentile or less) were at increased risk of abruption compared with those without abruption (9.6% compared with 5.3%; RR 1.9, 95% CI, 1.2-2.8)."

> "Women with all three abnormal pregnancy-associated plasma protein A, maternal serum alpha-fetoprotein, and inhibin-A analytes were at 8.8-fold (95% CI 2.3-34.3) risk of abruption."

> "These data provide support for our hypothesis that the origins of placental abruption may extend to the early stages of pregnancy."

**Curatorial note:** this is the key evidence for modeling a first-trimester origin node upstream of everything in §6 — abruption at 32 weeks may be the terminal event of a process initiated at implantation. It also justifies `MECHANISTIC_HYPOTHESIS` framing for any early-pregnancy prediction algorithm.

### 8.2 Progression

- **Stages:** Sher classes 0→3 (§3.3) function as severity stages. Progression from class 1 to class 3 can occur over minutes to hours.
- **Rate:** highly variable. Yamada et al. (PMID:22805996) give a chilling quantification of the acute time course in the subset that caused cerebral palsy: *"strong abdominal pain and/or profuse vaginal bleeding occurred 159 ± 99 min prior to admission to an obstetric facility, and the interval until delivery after admission was 47 ± 31 min."* The authors conclude: *"New strategies to shorten the interval until admission to an obstetric facility after onset of symptoms are urgently needed."*
- **Course pattern:** acute abruption is a single catastrophic event; chronic abruption is intermittent/relapsing over weeks.
- **Duration:** **self-limited by delivery.** This is the disease's defining temporal property — abruption resolves absolutely at delivery of the placenta. There is no chronic abruption state postpartum. What persists is (a) the maternal cardiovascular risk trajectory (§11), (b) offspring sequelae, and (c) elevated recurrence risk in future pregnancies.

### 8.3 Patterns

- **Remission:** not applicable within a pregnancy. Small chronic abruptions may stabilize and the pregnancy continue, with the hematoma organizing.
- **Recurrence across pregnancies:** ~5-fold. Oyelese et al., J Obstet Gynaecol Res 2024 (PMID:38366767), Kaiser Permanente Southern California, 126,264 patients with two consecutive singleton births over 30 years:

> "Rates of abruption in the second birth among individuals with and without previous placental abruption were 3.35% and 0.66%, respectively, giving an approximately five-fold increased odds of abruption in a second pregnancy in individuals who had abruption in their first birth when compared with those who did not have placental abruption in their first birth (aOR: 4.95, 95% confidence interval: 3.35-7.31, p < 0.00001)."

> "Interpregnancy interval had no statistically significant association with recurrence."

(StatPearls quotes a recurrence rate of 4–12%; the Kaiser figure of 3.35% is the best contemporary population estimate for a *second* birth specifically.)

- **Critical intervention windows:**
  1. **Preconception/first trimester** — the only window for modifying implantation-stage determinants (smoking cessation, blood-pressure control, ART practice).
  2. **<16 weeks** — the window in which low-dose aspirin is effective for placental disease generally.
  3. **24–34 weeks** — antenatal corticosteroids for fetal lung maturity; magnesium sulfate for neuroprotection.
  4. **The acute event, minutes to hours** — the decisive window. Yamada's ~47 min admission-to-delivery interval defines the operational target.

---

## 9. Inheritance and Population

### 9.1 Epidemiology

| Measure | Value | Population | Source |
|---|---|---|---|
| Overall incidence | **0.64%** (8,724 / 1,358,623) | pooled, 13 studies | PMID:10214847 |
| Prevalence | **0.6%–1.2%** of pregnancies | contemporary review | PMID:37164498 |
| Delivery hospitalizations | **1.2% (2000) → 1.6% (2020)**, AAPC 1.6% (95% CI 1.3%, 2.0%) | US National Inpatient Sample, 80.2M deliveries, 1.1M with abruption | PMID:40940025 |
| Cohort prevalence | **1.1%** (33,058 / 3,093,241 deliveries) | New Jersey, 1993–2020 | PMID:38273776 |
| First-birth rate | **0.63%**; second-birth rate 0.68% | Kaiser Permanente S. California, 1991–2021 | PMID:38366767 |
| Range (Merck) | 0.4%–1.5% | all pregnancies | Merck Manual Professional |
| Nordic vs US | 0.38–0.51% (Nordic) vs 0.6–1.0% (US) | | secondary review source |

**Structured `prevalence` block guidance (dismech convention):** use `measure_type: POINT_PREVALENCE` per delivery, `prevalence_class: ABOVE_1_IN_1000`, `rate_per_100000: 640` for the classic Ananth pooled figure (0.64% × 1000), or `rate_per_100000: 1600` for the 2020 US NIS figure. Keep the verbatim phrasing in `notes`. Do **not** mix the incidence-per-delivery denominator with a population denominator.

### 9.2 Temporal trends and disparities

Ananth et al., AJOG 2005 (PMID:15672024), National Hospital Discharge Survey 1979–2001:

> "The rate of abruption increased 92% (95% CI, 88, 96) among black women between 1979-1981 (0.76%; n = 13,584 women) and 1999-2001 (1.43%; n = 18,960 women). Among white women, the rate increased by 15% (95% CI, 14,16) over the same period, from 0.82% (n = 66,186 women) in 1979-1981 to 0.94% (n = 59,284 women) in 1999-2001."

> "The temporal increase in rates of abruption may reflect a true increase in risk or may be the result of improved diagnosis of both abruption and its determinants."

**Curate the racial disparity as a social/structural exposure, not a biological one.** "Black race" appears as a risk factor in Chen 2025, and Medicaid insurance in Wright 2026; both are markers of differential exposure, access, and chronic stress burden. An entry that curates "black race" as a biological risk factor without that framing is both scientifically wrong and harmful. Ananth's own hedge — that some of the trend may be ascertainment — should be preserved.

### 9.3 Inheritance

- **Pattern:** multifactorial / polygenic. HPO mode-of-inheritance term `HP:0010982` **Polygenic inheritance** is the appropriate binding, paired with `relationship_type: SUSCEPTIBILITY` gene typing per the dismech digenic/oligogenic SOP. Do **not** use `HP:0010984`/`HP:0010983`.
- **Penetrance / expressivity / anticipation / mosaicism / founder effects / consanguinity / carrier frequency:** all **not applicable** — there is no Mendelian allele. Say so explicitly rather than leaving blank.
- **Two-genome caveat worth curating:** susceptibility resides in both the maternal and the fetal/placental genome; Workalemahu et al. specifically examined *"Placental Genome and Maternal-Placental Genetic Interactions."* This is unusual enough to merit a note.

### 9.4 Demographics

- **Sex ratio:** the affected pregnant person is by definition female (`HP:0010982` context). For the *fetus*, Tikkanen et al. (PMID:23072758) found **male fetal sex** an independent risk factor for abruption-related perinatal mortality: *"Prematurity, low birthweight, male fetal sex and maternal smoking were independent risk factors for placental abruption-related perinatal mortality."*
- **Age distribution:** rises with maternal age ≥35 (OR 1.44) but also elevated at the young extreme in some series; the relationship is J-shaped.
- **Geography:** higher reported rates in the US than Nordic countries; whether that is true risk or coding practice is unresolved.
- **Variant geography:** the GWAS loci were discovered in a Peruvian (Andean-admixed) population and have not been replicated elsewhere — a hard limit on generalizability.

---

## 10. Diagnostics

### 10.1 Diagnostic status

**There is no confirmatory antenatal test.** StatPearls: *"No definitive diagnostic test exists."* Abruption is a clinical diagnosis, confirmed (or refuted) retrospectively by placental examination. This should be stated in the entry's `definitions` section rather than buried.

Hurd et al. (PMID:6828278) show the ceiling of clinical detection: *"Diagnosis was confirmed by placental inspection in 59 (1.3%) of 4545 deliveries. Among the 50 patients admitted with a living fetus, the diagnosis was made antenatally in 31 (62%)."* — i.e. roughly a third of abruptions with a live fetus were **not** diagnosed before delivery.

### 10.2 Imaging

Ultrasound is used to **exclude placenta previa**, not to confirm abruption. Glantz & Purnell, J Ultrasound Med 2002 (PMID:12164566) — still the definitive performance study, 149 consecutive patients:

> "Of 55 patients who gave birth within 14 days of sonography, 8 (15%) had scans consistent with abruption, and 29 (53%) had abruption at delivery; the sensitivity, specificity, and positive and negative predictive values of sonography were 24%, 96%, 88%, and 53%, respectively."

> "Sonography is not sensitive for detection of placental abruption, but a positive finding is associated with more aggressive management and worse neonatal outcome."

The physical reason: acute retroplacental hemorrhage is isoechoic with placental tissue, so a fresh hematoma is often invisible. MRI has higher sensitivity but is impractical in an emergency. **A negative scan does not exclude abruption** — this is the single most important diagnostic caveat in the entry and should be curated as a formal `distinguishing_features` or `KNOWLEDGE_GAP` statement.

Relevant NCIT/LOINC: use `NCIT:C92929` Fetal Heart Monitoring and `NCIT:C92836` Non-Stress Test for the monitoring modalities; there is no clean NCIT obstetric-ultrasound clinical-action term reachable from `NCIT:C25218` in the search performed — verify before binding.

### 10.3 Fetal monitoring

Continuous electronic fetal heart rate monitoring is the most informative single test. Category I / II / III tracings guide urgency; a Category III tracing in the setting of bleeding and uterine hypertonus is an indication for immediate delivery. Uterine tocodynamometry showing high-frequency, low-amplitude contractions is characteristic.

### 10.4 Laboratory

| Test | Purpose | Notes |
|---|---|---|
| Complete blood count | anemia, thrombocytopenia | |
| **Fibrinogen** | the key coagulopathy marker | Merck: *"Serum fibrinogen and fibrin-split products (the most sensitive indicator)"*. A low fibrinogen in an obstetric hemorrhage is both diagnostic of consumptive coagulopathy and prognostic |
| PT / aPTT | coagulopathy | |
| Fibrin degradation products / D-dimer | DIC | |
| Type and screen / crossmatch | transfusion readiness | |
| **Kleihauer-Betke** | quantifies fetomaternal hemorrhage | Essential in Rh-negative patients to dose anti-D immune globulin |
| BUN/creatinine | AKI | |

A dismech `reference_ranges` block with `interpretation_bands` on fibrinogen would be well-motivated here: pregnancy raises fibrinogen substantially, so a "normal" non-pregnant value is abnormally low in a bleeding obstetric patient. Curate the pregnancy-specific interval with evidence, and band the values by severity.

### 10.5 Histopathology (the reference standard)

Sampling and lesion definitions should follow the **Amsterdam Placental Workshop Group Consensus Statement** (Khong et al., Arch Pathol Lab Med 2016, PMID:27223167):

> "The group agreed on sets of uniform sampling criteria, placental gross descriptors, pathologic terminologies, and diagnostic criteria. The terminology and microscopic descriptions for maternal vascular malperfusion, fetal vascular malperfusion, delayed villous maturation, patterns of ascending intrauterine infection, and villitis of unknown etiology were agreed upon."

Findings to curate under `histopathology`:
- Adherent **retroplacental hematoma** with underlying **parenchymal indentation/compression** of the maternal surface — the most specific acute finding.
- **Decidual hemorrhage / decidual necrosis** in the decidua basalis.
- **Maternal vascular malperfusion** features (Amsterdam terminology): decidual arteriopathy/atherosis, accelerated villous maturation, infarcts, retroplacental hemorrhage — the chronic-arm signature.
- **Decidual neutrophil infiltration co-localizing with fibrin** (PMID:16251427) — with the crucial control observation that gestational-age-matched control decidua is *"virtually devoid of neutrophils."*
- **Hemosiderin deposition** and organizing hematoma in chronic abruption, dating the process to days–weeks before delivery.
- Concurrent **acute chorioamnionitis** in the infection-associated subgroup.

### 10.6 Genetic and omics diagnostics

**None indicated.** WGS, WES, gene panels, single-gene testing, CMA, karyotype, FISH, mtDNA testing and repeat-expansion testing all have **no role** in diagnosing or managing placental abruption. Thrombophilia panels are not recommended for placenta-mediated complications on current evidence. RNA-seq, proteomics, metabolomics, epigenomics and liquid biopsy have **no validated diagnostic application** here. State each of these as explicitly not applicable — this is more useful to a downstream consumer than an omitted field.

### 10.7 Differential diagnosis

| Condition | Distinguishing features |
|---|---|
| **Placenta previa** (`HP:0430070`) | Painless, bright red, external bleeding; **soft, relaxed uterus**; placenta over the internal os on ultrasound. StatPearls contrast: abruption gives "pain intense/acute; firm, board-like uterus" vs previa "no pain; soft, relaxed uterus" |
| Vasa previa | Bleeding at membrane rupture, rapid fetal exsanguination, fetal (not maternal) blood |
| Uterine rupture (`HP:0100718`) | Prior uterine scar, loss of station, abnormal contraction pattern, sudden FHR deterioration |
| Preterm labor | Contractions without hemorrhage or hypertonus |
| Cervical/vaginal lesion, cervicitis, post-coital bleeding | Visualized on speculum exam |
| Circumvallate placenta / marginal sinus bleed | Milder, often self-limited |
| Non-obstetric acute abdomen (appendicitis, ovarian torsion, nephrolithiasis) | Absent bleeding, different pain character |

### 10.8 Screening

There is **no validated screening test** for abruption in asymptomatic pregnancies. The biomarker combination from PMID:28178056 (low PAPP-A + high MSAFP + abnormal inhibin-A, RR 8.8) is the closest candidate but has never been prospectively validated as a screening instrument — its positive predictive value at population prevalence of ~1% would be poor. If curating a `definitions` entry for a serum-analyte-based case-finding rule, mark it `derivation_basis: MECHANISTIC_HYPOTHESIS` with `validation_status.status: PROPOSED`, and `attaches_to` the early-implantation origin node.

Trial anchors for prediction: NCT03455387 (sFlt-1/PlGF for placental complications), NCT03782168 (plasma biomarkers in placental abruption — **TERMINATED**), NCT01279369 (fetal fibronectin to predict abruption delivery — **TERMINATED**). Two terminated prediction studies is itself informative and worth noting.

---

## 11. Outcome / Prognosis

### 11.1 Perinatal mortality

Tikkanen et al., Acta Obstet Gynecol Scand 2013 (PMID:23072758) — Finnish national registers, 618,735 women / 1.14 million pregnancies / 4,336 abruptions:

> "Overall perinatal mortality with abruption was 119 per 1000 births. Placental abruption explained 7% of all perinatal deaths."

> "The mortality among singleton births (125 per 1000) was higher than among multiple births (40 per 1000). The majority of deaths (77%) occurred in utero."

> "Singleton perinatal mortality with abruption decreased from 173 per 1000 in 1987-1990 to 98 per 1000 in 2000-2005 (p < 0.001)."

> "In singleton births at <32 gestational weeks, overall perinatal mortality was high (345 per 1000) and was not increased by placental abruption."

That last finding is subtle and important: **at very early gestations, prematurity — not abruption per se — dominates mortality.** Curate it; it prevents over-attribution.

Consistently, Delorme et al. (PMID:26646125, EPIPAGE-2) found that among live births 24–34 weeks, abruption as the cause of preterm birth carried *"adjusted OR 1.6 [0.7-3.7]"* for in-hospital death — statistically indistinguishable from preterm labor.

StatPearls gives fetal mortality of 1–40% depending on severity and gestational age, and notes abruption accounts for 10–20% of maternal deaths (in settings without ready blood availability).

### 11.2 Maternal morbidity

Wright et al., Am J Perinatol 2026 (PMID:40940025), 80.2M US deliveries:

> "In adjusted analyses, abruption was associated with a range of adverse outcomes including transfusion (OR = 6.86, 95% CI: 6.70, 7.03), non-transfusion severe maternal morbidity (OR = 4.05, 95% CI: 3.93, 4.17), postpartum hemorrhage (OR = 1.76, 95% CI: 1.72, 1.80), disseminated intravascular coagulation (OR = 6.30, 95% CI: 6.00, 6.61), and critical care procedures (OR = 4.76, 95% CI: 4.26, 5.32)."

Plus, from Downes et al. (PMID:28329897): relaparotomy, hysterectomy, sepsis, amniotic fluid embolism, venous thromboembolism, acute kidney injury, ICU admission. Sheehan syndrome (postpartum pituitary necrosis) after massive hemorrhage (StatPearls).

### 11.3 Offspring neurological outcome

Yamada et al., Early Hum Dev 2012 (PMID:22805996) — Japan Council for Quality Health Care national CP review, 107 infants:

> "Abruptio placenta was responsible for 28 (26%) of the 107 CP infants, and was the single leading causative factor of CP."

> "Of these 28 women, 22 (79%) exhibited non-reassuring fetal status on admission to obstetric facilities at 36.2 ± 2.6 weeks of gestation and had neonates with umbilical cord arterial blood pH (base excess) of 6.728 ± 0.164 (-25 ± 5.4 mmol/L)."

An umbilical arterial pH of 6.73 is profound acidemia. Note the mean gestational age — 36.2 weeks, i.e. **near-term**, which is exactly why Brandt & Ananth devoted a review to the near-term/term window.

### 11.4 Long-term maternal cardiovascular risk

This reframes abruption from an acute obstetric event to a **life-course cardiovascular risk marker**.

Ananth et al., Neurology 2019 (PMID:31420459) — Danish population cohort, 828,289 women, 13,231,559 person-years:

> "Cerebrovascular mortality rates were 0.8 and 0.5 per 10,000 person-years among women with and without abruption, respectively (hazard ratio [HR] 1.6, 95% confidence interval [CI] 0.9-3.0). Abruption was associated with increased rates of nonfatal ischemic stroke (HR 1.4, 95% CI 1.1-1.7) and hemorrhagic stroke (HR 1.4, 95% CI 1.1-1.9)."

> "The association of abruption and stroke was increased with delivery at <34 weeks, when accompanied by ischemic placental disease, and among women with ≥2 abruptions."

> "Disruption of the hemostatic system manifesting as ischemia and hemorrhage may indicate shared etiologies between abruption and cerebrovascular complications."

Note the elegance of the shared-mechanism argument: abruption raises the risk of **both** ischemic and hemorrhagic stroke by the same factor, which points at a systemic vascular/hemostatic diathesis rather than a thrombotic one.

Adams et al., Semin Perinatol 2014 (PMID:24836826) generalize this across ischemic placental disease:

> "Retrospective observational studies comparing pregnancies complicated by ischemic placental disease to uncomplicated pregnancies suggest an increased long-term risk of hypertension, cardiovascular death, metabolic syndrome, and cerebrovascular disease. This association is much stronger in women who had an indicated-preterm delivery due to ischemic placental disease."

The ongoing **PACER** cohort (PMID:38273776) — 1,877,824 birthing persons, 3,093,241 deliveries, median follow-up 15.4 years — is the dedicated infrastructure for this question:

> "Pregnancy offers a unique window to study chronic diseases along the life course and efforts to identify the aetiology of abruption may provide important insights into the causes of future CVD."

This is an excellent candidate for a dismech **comorbidity/trajectory entry** (abruption → later cerebrovascular disease) rather than being buried inside the disorder entry.

### 11.5 Prognostic factors

- **Fraction of placenta separated** (dominant).
- **Gestational age at delivery.**
- **Fetal status at presentation** — a Category III tracing or absent fetal heart tones.
- **Time from symptom onset to delivery** (PMID:22805996).
- **Maternal hemodynamic status and fibrinogen level.**
- **Sher class.**
- **Fetal sex (male) and low birthweight** for mortality (PMID:23072758).
- Partial separation carries lower mortality than complete separation (StatPearls).

**Prognostic biomarkers:** fibrinogen is the only routinely useful one. No molecular prognostic marker is validated.

---

## 12. Treatment

Management is **delivery-centric**: there is no therapy that reverses abruption. The clinical decisions are (a) when to deliver, (b) by what route, and (c) how to support maternal hemostasis.

### 12.1 Immediate stabilization and supportive care

- Large-bore IV access, crystalloid resuscitation, supplemental oxygen, left lateral tilt, continuous maternal and fetal monitoring, transfer to a facility with obstetric and neonatal ICU capability (StatPearls).
- NCIT: `NCIT:C15747` Supportive Care; `NCIT:C94624` Oxygen Therapy; `NCIT:C92929` Fetal Heart Monitoring.
- `therapeutic_modality: OTHER` / `BEHAVIORAL` as appropriate.

### 12.2 Delivery

| Intervention | NCIT (verified) | Modality | Indication |
|---|---|---|---|
| Cesarean delivery | `NCIT:C46088` Cesarean Section (emergency: `NCIT:C92772` Emergency Cesarean Delivery) | `SURGERY` | Non-reassuring fetal status with a live viable fetus; maternal instability; Sher class 2–3 |
| Induction of labor / vaginal delivery | `NCIT:C92814` Induction of Labor | `OTHER` | Fetal demise; stable mother and fetus. Preferred where feasible because it avoids surgical bleeding in a coagulopathic patient. Hypertonic contractions often permit rapid vaginal delivery |
| Emergency hysterectomy | `NCIT:C15256` Hysterectomy | `SURGERY` | Uncontrollable hemorrhage / Couvelaire uterus with atony |

Hurd et al. (PMID:6828278) provide the evidence for **selective (expectant) management** in stable preterm cases:

> "It is concluded that optimal fetal survival and an acceptable cesarean section rate may be obtained by selective management, especially in infants weighing more than 1500 g."

> "There was a significant increase in the incidence of both respiratory distress syndrome and low Apgar scores among the study infants (P less than .005), but these increases were not correlated with mode of delivery or diagnosis-to-delivery interval."

### 12.3 Blood component therapy

| Product | NCIT (verified) | Purpose |
|---|---|---|
| Packed red cells | `NCIT:C15409` Packed Red Blood Cell Transfusion | oxygen-carrying capacity |
| Blood transfusion (general) | `NCIT:C15192` Blood Transfusion | massive transfusion protocol |
| Fresh frozen plasma | `NCIT:C116475` Fresh Frozen Plasma Transfusion | factor replacement |
| Cryoprecipitate | `NCIT:C180873` Cryoprecipitated Plasma / `NCIT:C133260` Cryoprecipitated Antihemophilic Factor | targeted fibrinogen replacement — the key product in abruption-associated DIC |

Given a transfusion OR of 6.86 (PMID:40940025), transfusion should be curated as a near-defining feature of severe abruption rather than an incidental treatment.

### 12.4 Pharmacotherapy

All use `treatment_term: NCIT:C15986` Pharmacotherapy with a `therapeutic_agent`:

| Drug | CHEBI (verified) | Modality | Role |
|---|---|---|---|
| Betamethasone | `CHEBI:3077` | `SMALL_MOLECULE` | antenatal corticosteroid for fetal lung maturity, <34 weeks. NCIT: `NCIT:C114131` Antenatal Steroid Therapy Initiated |
| Dexamethasone | `CHEBI:41879` | `SMALL_MOLECULE` | alternative corticosteroid |
| Magnesium sulfate | `CHEBI:32599` (NCIT:C623) | `SMALL_MOLECULE` | fetal neuroprotection <32 weeks; seizure prophylaxis if preeclamptic. Trial anchors: **NCT00186069** "Magnesium Sulfate vs Placebo for Placental Abruption" (COMPLETED); **NCT00014989** BEAM trial (Phase 3, COMPLETED) |
| Tranexamic acid | `CHEBI:48669` | `SMALL_MOLECULE` | antifibrinolytic adjunct for hemorrhage. Trial anchor: **NCT05840471** "Tranexamic Acid as an Intervention in Abruptio Placenta", COMPLETED, n=116, 2023-01-10 to 2024-02-10, primary outcomes hemostasis / gestational age / favorable perinatal outcome. Evidence base for abruption specifically is thin — do not overstate |
| Oxytocin | `CHEBI:7872` | `PEPTIDE` | labor augmentation and postpartum atony |
| Misoprostol | `CHEBI:63610` | `SMALL_MOLECULE` | uterotonic for postpartum hemorrhage |
| Anti-D (Rho(D)) immune globulin | NCIT: `NCIT:C80832` Human Rho(D) Immune Globulin; administration `NCIT:C92947` | `OTHER` / biologic | Rh-negative patients; dose guided by Kleihauer-Betke |
| Labetalol / nifedipine | `CHEBI:6343` / `CHEBI:7565` | `SMALL_MOLECULE` | blood-pressure control (see CHAP, §2.4). NCIT: `NCIT:C172184` Antihypertensive Therapy |
| Acetylsalicylic acid | `CHEBI:15365` | `SMALL_MOLECULE` | low-dose aspirin <16 weeks in high-risk pregnancies (prevention, §13) |
| Heparin / LMWH | `CHEBI:28304` | `SMALL_MOLECULE` | investigational for recurrence prevention; NCT00986765, NCT01068795 |

**Tocolysis** is controversial and generally contraindicated in acute abruption with fetal compromise; it may be considered in the stable, remote-from-term patient to permit corticosteroid administration. No clean NCIT clinical-action term for tocolysis was found reachable from `NCIT:C25218` — use free-text `preferred_term` with `NCIT:C15986` as the action.

### 12.5 Not applicable

Gene therapy, gene editing, cell therapy, RNA-based therapy, targeted therapy, immunotherapy, pharmacogenomics, and rehabilitation have **no role**. Record explicitly.

### 12.6 Treatment algorithm

Brandt & Ananth (PMID:37164498) describe *"a proposed management algorithm addressing blood loss, vital signs, and urine output"* along with *"blood component therapy, coagulopathy management, and care following fetal demise."* In outline:

1. **Fetal demise** → deliver, vaginal route preferred, aggressive coagulopathy correction.
2. **Live fetus, unstable mother or Category III tracing** → immediate cesarean.
3. **Live fetus, stable, ≥34–37 weeks** → deliver.
4. **Live fetus, stable, <34 weeks, Sher class 1** → hospitalize, corticosteroids, magnesium sulfate for neuroprotection, serial monitoring, serial growth ultrasound; deliver on deterioration.
5. **Postpartum** → monitor for hemorrhage and coagulopathy; neonatal team at delivery.

---

## 13. Prevention

### 13.1 Primary prevention

The honest summary: **no intervention has been shown in an RCT to prevent placental abruption as a standalone outcome.** Everything below is either risk-factor modification with observational support, or an RCT benefit on a composite that included abruption.

- **Smoking cessation** — the highest-yield modifiable target, PAF 15–25% (PMID:10214847). NCIT `NCIT:C17427` Smoking Cessation; `NCIT:C15372` Smoking Cessation Intervention. `therapeutic_modality: BEHAVIORAL`.
- **Cocaine and cannabis cessation** with counseling/rehabilitation support (StatPearls).
- **Blood pressure control in chronic hypertension** — CHAP (PMID:35363951, NCT02299414), composite RR 0.82 (0.74–0.92). Curate with the composite caveat.
- **Low-dose aspirin before 16 weeks** in pregnancies at high risk of placental disease — the strongest evidence is for preterm preeclampsia (ASPRE-type data), with abruption benefit inferred through the ischemic-placental-disease framework rather than demonstrated. Trial anchors: NCT04356326 (Chronic Hypertension and ASA in Pregnancy, Phase 3, RECRUITING), NCT01890005. **Do not curate aspirin as an evidence-based abruption prevention without this qualifier.**
- **Adequate prenatal care** (≥4 visits) and interpregnancy interval counselling — though Oyelese found interpregnancy interval had **no** significant association with recurrence (PMID:38366767), which argues *against* interval-based counselling specifically.
- **Trauma prevention** — seatbelt use with correct lap-belt placement below the gravid uterus, intimate-partner-violence screening.
- **Correction of anemia** (Hb <11 g/dL is an independent risk factor).

### 13.2 Secondary prevention (early detection)

No population screening program exists or is recommended. In a pregnancy with prior abruption, closer antenatal surveillance and patient education on warning signs is standard practice, though unvalidated. Given the 159 ± 99 minute symptom-to-admission interval in the CP cohort (PMID:22805996), **patient education to present immediately for sudden abdominal pain, bleeding, or decreased fetal movement is arguably the highest-value secondary prevention available** — and is measurable.

StatPearls lists education on *"sudden abdominal pain, vaginal bleeding, uterine tenderness, and decreased fetal movement."*

### 13.3 Tertiary prevention

Prevention of complications in the affected pregnancy: massive-transfusion protocols, early fibrinogen replacement, delivery in a facility with blood bank and NICU, anti-D prophylaxis for Rh-negative patients, antenatal corticosteroids and magnesium neuroprotection to mitigate prematurity sequelae.

### 13.4 Immunization, genetic screening, genetic counseling

- **Immunization:** not applicable (no vaccine-preventable etiology). Routine pregnancy immunization is unrelated.
- **Genetic screening / carrier screening / PGT / prenatal genetic testing:** **not applicable.** No causal gene. Thrombophilia screening is not recommended for placenta-mediated complications.
- **Genetic counseling** (`NCIT:C15240`): not indicated for abruption per se. Recurrence counseling — quantitatively, ~5× odds and ~3.35% absolute risk in a second birth (PMID:38366767) — is *obstetric* counseling and should be curated as such, not as genetic counseling.

### 13.5 Risk stratification

Best available: prior abruption (AOR 2.72), placenta previa (AOR 7.31), chronic hypertension (OR 3.13), cocaine use (RR 4.55), plus the first/second-trimester analyte triad (RR 8.8 for all three abnormal, PMID:28178056). No validated multivariable clinical prediction model with external validation exists — a clear `KNOWLEDGE_GAP`.

---

## 14. Other Species / Natural Disease

### 14.1 Taxonomy

- *Homo sapiens* — `NCBITaxon:9606` (the disease as defined).
- *Equus caballus* — `NCBITaxon:9796` — the most relevant natural-disease species (see below).
- *Rattus norvegicus* — `NCBITaxon:10116` — induced model only.
- *Mus musculus* — `NCBITaxon:10090` — induced model only.

### 14.2 Natural disease in other species

**Horse — premature placental separation ("red bag" delivery).** The only well-documented naturally-occurring analog. In the mare, the chorioallantois separates prematurely and presents intact at the vulva (velvety red, rather than the normal white amnion), meaning the foal is being delivered while still perfused by a detached placenta — an acute asphyxial emergency requiring immediate manual rupture of the chorioallantois. It is strongly associated with ascending bacterial/fungal placentitis.

Hong et al., J Vet Diagn Invest 1993 (PMID:8286455) — 1,211 aborted equine fetuses, stillborn foals and placentas, central Kentucky:

> "Placentitis (19.4%) and dystocia-perinatal asphyxia (19.5%) were the 2 most important causes of equine reproductive loss. The other causes (in decreasing order) were contracted foal syndrome and other congenital anomalies (8.5%), twinning (6.1%), improper separation of placenta (4.7%), torsion of umbilical cord (4.5%)…"

So **improper separation of placenta accounted for 4.7% of equine reproductive loss** in this large series. Note the mechanistic divergence, which is the interesting comparative point: the equine epitheliochorial, diffuse, non-invasive placenta has **no decidua and no trophoblast invasion of maternal vessels**. Premature separation in the mare is therefore an adhesion/infection failure, *not* a decidual-hemorrhage disease. The human decidual-hemorrhage mechanism has essentially no equine counterpart.

**Other species.** Sporadic premature placental separation is described in cattle and dogs but is not a recognized syndrome with the human phenotype. No OMIA entry corresponds to human placental abruption (**verify against OMIA before asserting absence**).

### 14.3 Comparative biology — the central caveat

**Deep hemochorial placentation with extensive extravillous trophoblast invasion of maternal spiral arteries is largely restricted to humans and great apes.** Mice and rats are hemochorial but with far shallower and more limited invasion; horses, cattle, pigs and sheep are epitheliochorial/synepitheliochorial and non-invasive.

This is the single most important comparative fact for this entry, and it should be curated as a `HUMAN_MODEL_MISMATCH` discussion rather than a generic `KNOWLEDGE_GAP`: model-organism evidence about decidual hemorrhage exists, but the anatomical substrate that makes human abruption possible — a deeply invaded, decidualized maternal–fetal interface — is not reproduced in any standard model. This limits the translational validity of every animal result in §15.

### 14.4 Orthologous genes

Orthologs of F3, F2, F2R, MMP1, PGR, SERPINE1 exist across mammals (Alliance of Genome Resources / HomoloGene). Notably, **mice lack a direct CXCL8/IL-8 ortholog** (using KC/CXCL1 and MIP-2/CXCL2 instead), so the thrombin→IL-8→decidual neutrophil axis of PMID:16251427 cannot be modeled in mouse without careful substitution. Another concrete `HUMAN_MODEL_MISMATCH` item.

### 14.5 Zoonotic potential

None. Not transmissible; not infectious in the communicable sense.

---

## 15. Model Organisms

### 15.1 The candid summary

There is **no established, widely-used animal model of placental abruption.** This is a genuine and consequential gap: the entire molecular mechanism in §6 rests on human decidual cell culture plus human placental immunohistochemistry, with only scattered in-vivo support.

### 15.2 In vivo models

**Rat — local cold-stress model (the best-characterized).** Khatun et al., Semin Thromb Hemost 2001 (PMID:11372774):

> "Cold stress at 0 degrees C and 12 degrees C significantly decreased uterine blood flow (P < .005, P < .02) compared with controls (23 degrees C)."

> "Cold-induced stress (0 degrees C) also evoked an isometric tension with increased frequency and amplitude in the rat uterus (P < .003, P < .0002) compared with controls (23 degrees C)."

> "Placental histology of rats stressed at 0 degreesC revealed hemorrhages into the decidua basalis."

> "These findings suggest that local cold stress decreases uterine blood flow and increases uterine contraction, resulting in retroplacental hemorrhage in rats. This model may account for human abruptio placentae."

- Model type: **induced**, environmental manipulation (sympathetically-mediated uterine vasoconstriction).
- Phenotype recapitulation: **partial and mechanistically apt** — it reproduces the target lesion (hemorrhage into decidua basalis) via a plausible route (uterine vasoconstriction + hypertonus).
- Limitations: acute and non-physiological stimulus; no chronic vasculopathy arm; does not reproduce coagulopathy or PPROM; rat placentation is shallower than human; no genetic component.
- Evidence source: **MODEL_ORGANISM**.

**Other induced approaches described in the literature** (uterine ischemia-reperfusion, LPS administration, cocaine administration in pregnant rodents) exist but no single one is standardized as an abruption model. Do not assert specifics without a retrieved primary source.

### 15.3 Genetic models

**None purpose-built for abruption.** Knockout/knock-in/conditional/humanized models of the pathway genes (F3, F2R, PGR, MMP1, SERPINE1) exist in mouse and are informative for individual mechanistic steps, but none produces an abruption phenotype. Notably, complete F3 (tissue factor) knockout in mouse is embryonic lethal with yolk-sac vascular failure — which is itself indirect support for the "TF maintains uteroplacental hemostasis" thesis, but it is not an abruption model.

Resources: MGI, IMPC, KOMP, IMSR for the individual gene models; there is no abruption-specific model registry entry.

### 15.4 In vitro / cellular models (where the mechanism actually comes from)

These carry most of the mechanistic weight in §6 and should be curated as **IN_VITRO** evidence throughout.

| System | Used for | Key PMIDs |
|---|---|---|
| **Leukocyte-depleted primary term human decidual cells (DCs)**, cultured with estradiol ± medroxyprogesterone acetate to mimic the pregnant hormonal milieu, ± thrombin | The workhorse system. Established the thrombin→IL-8, thrombin→MMP-1, thrombin→PAI-1, thrombin→IL-11, and thrombin→PR-downregulation results | 16251427, 12380602, 17403427, 15998775, 23058370 |
| **Human endometrial endothelial cells (HEECs)** ± thrombin ± PAR agonists ± LPS | Established the thrombin×TLR4 inflammatory synergy and PAR-1 dependence | 27108773 |
| **Predecidualized cycling endometrial stromal cells** | Non-pregnant comparator for the hormonal-milieu contrast | 12380602 |
| **Human placental/decidual tissue immunohistochemistry** (abruption vs gestational-age-matched control) | The in-vivo validation arm; this is HUMAN_CLINICAL, not in vitro | 16251427, 23058370, 34205566 |

The **hormonal-priming design** in this body of work deserves specific note when curating: the DC cultures deliberately compare E2 alone (proliferative-phase-like) with E2+MPA (pregnancy-like), and the striking finding across papers is that **progestin suppresses the inflammatory/proteolytic response but thrombin overrides that suppression.** That override *is* the mechanism of abruption-associated preterm delivery, and it is the most reusable idea in the entry.

Trophoblast-invasion models (HTR-8/SVneo, primary EVT, trophoblast organoids, iPSC-derived trophoblast) are relevant to Trigger A but have not been applied to abruption specifically.

### 15.5 Research applications and limitations

**Can be studied:** thrombin/PAR-1 signaling in decidual and endometrial endothelial cells; progesterone-receptor regulation; MMP and cytokine induction; neutrophil recruitment; the infection×hemorrhage synergy; membrane weakening.

**Cannot currently be studied in any model:** the initiating decidual vessel rupture in a physiologically deeply-invaded placenta; the natural history from first-trimester implantation defect to third-trimester event; genetic susceptibility (no model carries the human risk alleles); the maternal life-course cardiovascular sequelae; human-specific coagulopathy dynamics.

---

## Appendix A — Consolidated ontology term suggestions (all verified this session)

**Disease:** `MONDO:0004846` placental abruption (with the definition-error caveat, §1.2)
**As a phenotype of other disorders:** `HP:0011419` Placental abruption

**Anatomy (UBERON):** `UBERON:0000453` decidua basalis · `UBERON:0002450` decidua · `UBERON:0006878` decidua parietalis · `UBERON:0001987` placenta · `UBERON:8600019` placental basal plate · `UBERON:0010008` placental cotyledon · `UBERON:0000426` extravillous trophoblast

**Cell types (CL):** `CL:2000002` decidual cell · `CL:0002255` stromal cell of endometrium · `CL:0008036` extravillous trophoblast · `CL:2000060` placental villous trophoblast · `CL:0002219` anchoring trophoblast · `CL:0002343` decidual natural killer cell, human · `CL:4052028` uterine natural killer cell · `CL:0008033` decidual pericyte

**Biological processes (GO):** `GO:0007596` blood coagulation · `GO:0070493` thrombin-activated receptor signaling pathway · `GO:0006954` inflammatory response · `GO:0030593` neutrophil chemotaxis · `GO:0022617` extracellular matrix disassembly · `GO:0071456` cellular response to hypoxia · `GO:0070471` uterine smooth muscle contraction · `GO:0061450` trophoblast cell migration · `GO:0046697` decidualization · `GO:0042730` fibrinolysis · `GO:0030168` platelet activation · `GO:0001893` maternal placenta development

**Phenotypes (HP):** see the tables in §3.1–3.2.

**Chemicals (CHEBI):** `CHEBI:3077` betamethasone · `CHEBI:41879` dexamethasone · `CHEBI:32599` magnesium sulfate · `CHEBI:48669` tranexamic acid · `CHEBI:7872` oxytocin · `CHEBI:63610` misoprostol · `CHEBI:6343` labetalol · `CHEBI:7565` nifedipine · `CHEBI:15365` acetylsalicylic acid · `CHEBI:28304` heparin · `CHEBI:27958` cocaine · `CHEBI:18723` nicotine · `CHEBI:27470` folic acid

**Treatments (NCIT):** `NCIT:C46088` Cesarean Section · `NCIT:C92772` Emergency Cesarean Delivery · `NCIT:C92814` Induction of Labor · `NCIT:C15256` Hysterectomy · `NCIT:C15192` Blood Transfusion · `NCIT:C15409` Packed Red Blood Cell Transfusion · `NCIT:C116475` Fresh Frozen Plasma Transfusion · `NCIT:C180873` Cryoprecipitated Plasma · `NCIT:C114131` Antenatal Steroid Therapy Initiated · `NCIT:C92947` Rh Immune Globulin Administration · `NCIT:C80832` Human Rho(D) Immune Globulin · `NCIT:C17427` Smoking Cessation · `NCIT:C15372` Smoking Cessation Intervention · `NCIT:C172184` Antihypertensive Therapy · `NCIT:C15747` Supportive Care · `NCIT:C94624` Oxygen Therapy · `NCIT:C92929` Fetal Heart Monitoring · `NCIT:C92836` Non-Stress Test · `NCIT:C15986` Pharmacotherapy · `NCIT:C623` Magnesium Sulfate

---

## Appendix B — Module conformance candidates

Reviewing the existing `kb/modules/` inventory, plausible conformance targets for this entry:

- **`thrombogenesis`** — partial. The retroplacental hematoma involves coagulation cascade activation and thrombin-driven fibrin formation (`thrombogenesis#Coagulation Cascade Activation and Thrombin-Driven Fibrin Formation`). But the causal direction is *inverted*: in thrombogenesis a thrombus occludes a vessel; here hemorrhage precedes and drives clot formation, and the clot is the destructive agent by mass effect rather than by occlusion. Declare conformance only at the thrombin/fibrin node, with a note.
- **No existing module covers "ischemic placental disease."** Abruption, preeclampsia and fetal growth restriction share risk factors, recurrence, co-occurrence and placental lesions (PMID:24836823; PMID:24836826). If the KB already carries preeclampsia and FGR entries, **a new `ischemic_placental_disease` mechanism module is the highest-value structural contribution this entry could motivate** — trigger (impaired spiral-artery remodeling) → uteroplacental malperfusion → divergent clinical manifestation (hypertensive / growth-restrictive / hemorrhagic).
- **A `decidual_hemorrhage_thrombin_signaling` module** is also well-supported: thrombin generation → PAR-1 activation → MMP/IL-8/CSF-2/IL-11 induction + functional progesterone withdrawal → PPROM and preterm delivery. This recurs across abruption, PPROM, and subchorionic hematoma, so it is genuinely reusable.
- **`fibrotic_response`, `cellular_senescence`, hallmark modules** — not applicable.

---

## Appendix C — Explicit gaps and negative findings (curate these, don't omit them)

1. No Mendelian gene, no OMIM entry, no ORPHA code.
2. No genome-wide significant, replicated GWAS locus; all associations suggestive, single-ancestry (Peruvian).
3. No abruption-specific transcriptomic, proteomic, metabolomic, epigenomic, single-cell or spatial dataset.
4. No confirmatory antenatal diagnostic test; ultrasound sensitivity 24% (PMID:12164566).
5. No externally-validated clinical prediction model.
6. No RCT demonstrating prevention of abruption as a standalone outcome.
7. No standardized animal model; the human-specific depth of trophoblast invasion is not reproduced in any model (`HUMAN_MODEL_MISMATCH`).
8. Mice lack a CXCL8/IL-8 ortholog, blocking direct modeling of the neutrophil-recruitment arm (`HUMAN_MODEL_MISMATCH`).
9. No validated disease-specific quality-of-life instrument.
10. No uniform case definition across the epidemiological literature (PMID:28329897) — attach this caveat to every effect estimate.
11. The MONDO:0004846 textual definition is factually wrong and should be reported upstream.
12. Two biomarker-prediction trials (NCT03782168, NCT01279369) were terminated — the prediction problem has a track record of failure.
13. The umbrella review found **zero** class I or II evidence risk factors (PMID:35365209) — the entire risk-factor literature is class III or weaker.

---

## Sources

Primary literature (PubMed, all abstracts retrieved and quoted verbatim this session):
[PMID:37164498](https://pubmed.ncbi.nlm.nih.gov/37164498/) ·
[PMID:40940025](https://pubmed.ncbi.nlm.nih.gov/40940025/) ·
[PMID:40140972](https://pubmed.ncbi.nlm.nih.gov/40140972/) ·
[PMID:38366767](https://pubmed.ncbi.nlm.nih.gov/38366767/) ·
[PMID:38273776](https://pubmed.ncbi.nlm.nih.gov/38273776/) ·
[PMID:35365209](https://pubmed.ncbi.nlm.nih.gov/35365209/) ·
[PMID:35363951](https://pubmed.ncbi.nlm.nih.gov/35363951/) ·
[PMID:34205566](https://pubmed.ncbi.nlm.nih.gov/34205566/) ·
[PMID:31420459](https://pubmed.ncbi.nlm.nih.gov/31420459/) ·
[PMID:29884306](https://pubmed.ncbi.nlm.nih.gov/29884306/) ·
[PMID:29360829](https://pubmed.ncbi.nlm.nih.gov/29360829/) ·
[PMID:28329897](https://pubmed.ncbi.nlm.nih.gov/28329897/) ·
[PMID:28178056](https://pubmed.ncbi.nlm.nih.gov/28178056/) ·
[PMID:27223167](https://pubmed.ncbi.nlm.nih.gov/27223167/) ·
[PMID:27108773](https://pubmed.ncbi.nlm.nih.gov/27108773/) ·
[PMID:26646125](https://pubmed.ncbi.nlm.nih.gov/26646125/) ·
[PMID:24836823](https://pubmed.ncbi.nlm.nih.gov/24836823/) ·
[PMID:24836826](https://pubmed.ncbi.nlm.nih.gov/24836826/) ·
[PMID:24046805](https://pubmed.ncbi.nlm.nih.gov/24046805/) ·
[PMID:23072758](https://pubmed.ncbi.nlm.nih.gov/23072758/) ·
[PMID:23058370](https://pubmed.ncbi.nlm.nih.gov/23058370/) ·
[PMID:22805996](https://pubmed.ncbi.nlm.nih.gov/22805996/) ·
[PMID:19720393](https://pubmed.ncbi.nlm.nih.gov/19720393/) ·
[PMID:17403427](https://pubmed.ncbi.nlm.nih.gov/17403427/) ·
[PMID:16595080](https://pubmed.ncbi.nlm.nih.gov/16595080/) ·
[PMID:16251427](https://pubmed.ncbi.nlm.nih.gov/16251427/) ·
[PMID:15998775](https://pubmed.ncbi.nlm.nih.gov/15998775/) ·
[PMID:15715592](https://pubmed.ncbi.nlm.nih.gov/15715592/) ·
[PMID:15672024](https://pubmed.ncbi.nlm.nih.gov/15672024/) ·
[PMID:12380602](https://pubmed.ncbi.nlm.nih.gov/12380602/) ·
[PMID:12164566](https://pubmed.ncbi.nlm.nih.gov/12164566/) ·
[PMID:11372774](https://pubmed.ncbi.nlm.nih.gov/11372774/) ·
[PMID:10214847](https://pubmed.ncbi.nlm.nih.gov/10214847/) ·
[PMID:8286455](https://pubmed.ncbi.nlm.nih.gov/8286455/) ·
[PMID:6828278](https://pubmed.ncbi.nlm.nih.gov/6828278/) ·
[PMID:1765257](https://pubmed.ncbi.nlm.nih.gov/1765257/)

Reference works and databases:
[StatPearls: Placental Abruption (NBK482335)](https://www.ncbi.nlm.nih.gov/books/NBK482335/) ·
[Merck Manual Professional: Placental Abruption](https://www.merckmanuals.com/professional/gynecology-and-obstetrics/antenatal-complications/placental-abruption-abruptio-placentae) ·
[AJOG: Placental abruption at near-term and term gestations](https://www.ajog.org/article/S0002-9378(22)00535-X/fulltext) ·
[BJA Education: Placental abruption (2024)](https://www.bjaed.org/article/S2058-5349(24)00065-9/fulltext) ·
[BMC Pregnancy Childbirth: Independent risk factors for placental abruption](https://link.springer.com/article/10.1186/s12884-025-07482-7) ·
[NCBI MeSH D000037](https://www.ncbi.nlm.nih.gov/mesh/68000037) ·
[EBI OLS4](https://www.ebi.ac.uk/ols4/) (HP, GO, CL, UBERON, CHEBI, NCIT, MONDO term resolution) ·
[Monarch Initiative API — MONDO:0004846](https://api.monarchinitiative.org/v3/api/entity/MONDO:0004846) ·
[HGNC REST API](https://rest.genenames.org/) ·
[ClinicalTrials.gov API v2](https://clinicaltrials.gov/) (NCT02299414, NCT05840471, NCT00186069, NCT00014989, NCT00986765, NCT04356326, NCT03455387, NCT03782168, NCT01279369, NCT04168606)