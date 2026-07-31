---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-31T00:15:18.405315'
end_time: '2026-07-31T00:20:52.542589'
duration_seconds: 334.14
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Fragile X-Associated Primary Ovarian Insufficiency
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
  - claude-sonnet-5
  web_search_requests: 21
  num_turns: 20
  total_cost_usd: 1.9077731999999998
  session_id: 86acbce9-59a4-5f93-ab4c-3858ee16e2c7
  stop_reason: end_turn
citation_count: 37
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Fragile X-Associated Primary Ovarian Insufficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Fragile X-Associated Primary Ovarian Insufficiency** covering all of the
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

# Fragile X-Associated Primary Ovarian Insufficiency (FXPOI): Comprehensive Research Report

## 1. Disease Information

**Overview:** Fragile X-associated primary ovarian insufficiency (FXPOI) is a chronic reproductive endocrine disorder in which women carrying a *premutation*-length CGG-repeat expansion in the *FMR1* gene develop hypergonadotropic hypogonadism (oligomenorrhea/amenorrhea with elevated FSH and low estradiol) before age 40. It is one of three recognized clinical disorders on the *FMR1*-related spectrum — alongside Fragile X Syndrome (FXS, full mutation, >200 CGG repeats, transcriptional silencing) and Fragile X-associated Tremor/Ataxia Syndrome (FXTAS, premutation, late-onset neurodegeneration) — and is the **leading known monogenic/inherited cause of idiopathic primary ovarian insufficiency (POI)** in women.

**Key identifiers:**
- **OMIM:** #311360 — *Premature Ovarian Failure 1 (POF1)*, mapped to the *FMR1* locus (OMIM gene 309550) at Xq27.3
- **Orphanet:** ORPHA:642691 — Fragile X-associated primary ovarian insufficiency
- **MedGen:** CUI C4552079 — "Premature ovarian failure 1"
- **GeneReviews:** *FMR1* Disorders (NBK1384) — the umbrella clinical reference covering FXS/FXTAS/FXPOI
- **MeSH:** Primary Ovarian Insufficiency (D016649); Fragile X Syndrome (D005600) as related term
- **Suggested MONDO term:** a MONDO entry cross-referencing OMIM:311360/ORPHA:642691 (exact MONDO CURIE should be verified directly against the Mondo release, as web search did not resolve a stable ID)
- **ICD-10:** E28.31 (Primary ovarian failure) is the closest coded diagnosis; there is no FXPOI-specific ICD-10/11 code — coding relies on the genetic diagnosis (*FMR1* premutation) plus E28.31/E28.310

**Synonyms:** Fragile X-associated premature ovarian failure/insufficiency; FXPOI; Premature Ovarian Failure 1 (POF1); *FMR1*-premutation-associated POI.

**Evidence base:** Predominantly aggregated, disease-level clinical-genetics literature (cohort studies of premutation carriers ascertained through fragile X family studies, IVF/infertility clinics, and population-based carrier screening), supplemented by mouse and cell-culture (granulosa cell) mechanistic studies. Large population-based data (e.g., UK Biobank) are only recently becoming available and show smaller effect sizes than the highly ascertained fragile-X-family cohorts that dominate the literature (Morbey et al., *Hum Reprod* 2026).

---

## 2. Etiology

**Disease Causal Factor — genetic (monogenic, X-linked, dosage/repeat-length dependent):** FXPOI is caused by a **premutation-range CGG trinucleotide repeat expansion (55–200 repeats) in the 5′ untranslated region (UTR) of *FMR1*** (fragile X messenger ribonucleoprotein 1, HGNC:3775, Xq27.3). Unlike the full mutation (>200 repeats) that causes FXS via CpG-island hypermethylation and transcriptional silencing, the premutation range remains largely unmethylated and is actively transcribed, producing a **toxic gain-of-function** at the RNA (and possibly protein) level rather than a straightforward loss of FMRP protein function.

**Genetic risk factors:**
- **CGG repeat number** is the principal quantitative risk factor, but the relationship is **non-linear ("inverted-U" / "FXPOI paradox")**: risk rises through the low-to-mid premutation range and **peaks around 70–100 repeats (highest risk at 85–89 repeats)**, then **paradoxically declines at the largest premutation sizes (>100–120 repeats)**, approaching the risk of non-carriers (<45 repeats) at the extremes (Allen et al., *Genet Med* 2021, PMID:33927378; Elizur et al., *PLOS ONE* 2014, PMC4143194). This is proposed to reflect a balance between increasing toxic-RNA burden (rises with repeat length) and decreasing translational efficiency/FMRP output at very large premutation sizes (partial protective effect).
- **AGG interruptions** within the CGG tract stabilize the repeat and reduce risk of intergenerational expansion, but do **not** show a clear association with age at amenorrhea/FXPOI risk itself (Mailick et al., PMC6086008) — distinguishing their role (relevant to FXS anticipation risk in offspring) from FXPOI risk in the carrier herself.
- **X-chromosome inactivation (XCI) skewing**: preferential inactivation of the premutation-bearing X allele is associated with **higher AMH / better ovarian reserve** (protective), i.e., skewed XCI toward the *normal* allele attenuates the phenotype, analogous to its protective role in FXTAS/FXS severity (PMC5410032).
- **Modifier/susceptibility loci**: genome-wide and candidate-gene studies (e.g., variation near *ESR1*, other menopause-timing loci identified via GWAS of natural menopause age) have been explored as modifiers of FXPOI onset age, though no single modifier gene has achieved the evidentiary weight of the *FMR1* repeat length itself; this remains an active research area (PMC4124461, "Approaches to identify genetic variants that influence the risk for onset of FXPOI").

**Environmental/other risk factors:** No established non-genetic environmental cause; FXPOI is specifically the *FMR1*-premutation-attributable subtype of POI. General POI risk modifiers (smoking, pelvic radiation/chemotherapy, autoimmune disease) are not part of the FXPOI causal chain but are relevant differential/comorbid considerations (see Section 10).

**Protective factors:**
- Genetic: shorter/longer-than-mid-range CGG repeat size (outside the 70–100 "risk zone"); skewed XCI toward the normal allele.
- No established environmental/lifestyle protective factor specific to FXPOI has been robustly demonstrated in the literature retrieved.

**Gene-environment interaction:** Not well characterized for FXPOI specifically; the disorder is regarded as a highly penetrant-by-genotype (repeat-length-dependent) condition rather than one with strong documented GxE modulation.

---

## 3. Phenotypes

**Core reproductive/endocrine phenotype (laboratory abnormality + clinical sign):**
- **Oligomenorrhea/amenorrhea** before age 40 — HPO: consider Amenorrhea (HP:0000141) / Oligomenorrhea (HP:0030041)
- **Hypergonadotropic hypogonadism** — elevated FSH (>25 IU/L on two occasions ≥1 month apart, per consensus diagnostic criteria) and LH, with low estradiol — HPO: Hypergonadotropic hypogonadism (HP:0000815); Elevated circulating follicle stimulating hormone level (HP:0008232)
- **Hot flashes / vasomotor symptoms** consistent with hypoestrogenism — HPO: Hot flashes (HP:0030788, if present) / general hypoestrogenism-related symptoms
- **Reduced/absent ovarian reserve** — low AMH, low antral follicle count — HPO: Decreased ovarian reserve is not a distinct canonical HPO term in all releases; "Premature ovarian insufficiency" (HP:0008209) is the closest umbrella term
- **Infertility/subfertility** — HPO: Female infertility (HP:0000786)
- **Primary or secondary amenorrhea with delayed puberty** in the earliest-onset cases (reported as young as age 11) — HPO: Delayed puberty (HP:0000823), Primary amenorrhea (HP:0000786/HP:0000730 depending on release)

**Onset/characteristics:**
- **Age of onset**: variable — mean age at menopause/amenorrhea in FXPOI is reported roughly a decade earlier than the general population (mid-30s to early 40s on average), with rare reported onset as early as 11 years old (primary amenorrhea/delayed puberty phenotype) through the usual definitional cutoff of 40 years.
- **Severity/course**: **highly variable and non-linear** — menses may cease abruptly and permanently, or fluctuate irregularly for years before complete cessation ("occult" or intermittent ovarian insufficiency is common; some carriers retain intermittent ovulatory cycles even after FSH elevation).
- **Frequency among carriers**: **~20% (range cited 20–30%)** of *FMR1* premutation carriers develop FXPOI, versus **~1%** background POI prevalence in the general female population — i.e., a substantial relative-risk increase, though penetrance is incomplete and repeat-length-dependent (non-linear, see Section 2).

**Downstream/associated phenotypes (estrogen-deficiency sequelae):**
- Reduced bone mineral density / early osteoporosis risk — HPO: Osteoporosis (HP:0000939) — via the `osteoporosis_bone_resorption` mechanism-module logic if curated in dismech
- Increased cardiovascular risk (early estrogen loss) — general cardiovascular risk elevation, not a specific structural phenotype
- Psychological impact: depression and anxiety related to infertility/hormonal loss — HPO: Anxiety (HP:0000739), Depressivity (HP:0000716)
- Broader **premutation-carrier comorbidities** (not FXPOI-specific but co-occurring in the same genotype group under the umbrella "Fragile X Premutation Associated Conditions," FXPAC): FXTAS in later life (males and some female carriers), Fragile X-Associated Neuropsychiatric Disorders (FXAND: anxiety ~82%, ADHD ~66.5%, ASD ~32.8% in young carriers), autonomic dysfunction, hypertension, arrhythmia, neuropathy, thyroid autoimmunity, fibromyalgia/chronic pain (Movaghar et al./Hunter et al., PMC7578382; PMC9778214).

**Quality of life impact:** FXPOI carries a compound QoL burden — grief/loss related to infertility and premature reproductive aging, psychiatric comorbidity (anxiety/depression), and long-term health impacts of estrogen deficiency (bone, cardiovascular, possibly cognitive). The 2011 NFXF Clinical & Research Consortium consensus document explicitly identifies depression/anxiety, reduced bone mineral density, and increased cardiovascular risk as the three principal downstream morbidities requiring proactive management.

---

## 4. Genetic/Molecular Information

**Causal gene:** ***FMR1*** (Fragile X Messenger Ribonucleoprotein 1; HGNC:3775; OMIM *309550; Xq27.3). Encodes FMRP, an RNA-binding protein regulating mRNA transport/translation at synapses (central to the FXS loss-of-function mechanism); FXPOI mechanism is distinct (see Section 6).

**Variant/allele classification by CGG repeat number in the 5′ UTR:**
| Category | Repeat range | Methylation | Associated disease |
|---|---|---|---|
| Normal | ~5–44 | Unmethylated | None |
| Intermediate/"gray zone" | 45–54 | Unmethylated | Uncertain; possibly mildly elevated risk of instability/subtle phenotypes |
| **Premutation** | **55–200** | Typically unmethylated, transcribed | **FXPOI, FXTAS**, some FXAND |
| Full mutation | >200 | Hypermethylated, silenced | Fragile X Syndrome |

- **Variant type:** unstable trinucleotide (CGG) repeat expansion — not a missense/nonsense/structural variant in the conventional sense; classified functionally rather than via standard ACMG/AMP missense criteria. ClinVar/GTR entries for *FMR1* repeat-expansion testing exist but classification is by repeat-length tier rather than a single pathogenic variant call.
- **Allele frequency / carrier frequency:** Population estimates vary by ascertainment and ethnicity — pan-ethnic premutation carrier frequency roughly **1 in 200–300 women** in several large carrier-screening cohorts (Owens et al. 2018 AJMG-A: 1 in 201; Genetics in Medicine 2011 national screening estimate ~1 in 148–178 in some cohorts), with a meta-analytic estimate as high as **1 in 129 women**, and substantial regional/ethnic variation (e.g., ~1 in 600–777 in some Asian cohorts). Premutation prevalence is enriched in women ascertained specifically for POI (~2.0% in POI cohorts vs ~0.4% in unselected controls), underscoring *FMR1* testing's diagnostic yield in POI workups.
- **Somatic vs germline:** Germline, X-linked; the repeat is also somatically variable/mosaic in some carriers (repeat-length mosaicism is well documented across the *FMR1* spectrum).
- **Functional consequence:** Not classic loss-of-function; premutation-range transcripts show a **toxic RNA gain-of-function** (see Section 6), with a possible secondary contribution from repeat-associated non-AUG (RAN) translation producing an abnormal polyglycine-containing protein, FMRpolyG.

**Modifier genes/factors:** AGG interruption pattern (protects against intergenerational full-mutation expansion, not clearly protective for FXPOI onset itself); XCI skewing ratio (functionally modifies phenotype expression, not a "gene" per se but a key epigenetic modifier); candidate genome-wide modifiers of ovarian aging/menopause timing (under investigation, not yet definitively validated for FXPOI specifically).

**Epigenetic information:** Central to the FXS/FXPOI distinction — the full mutation triggers CpG-island hypermethylation and heterochromatinization silencing *FMR1* transcription (causing FXS via FMRP loss), whereas the premutation range largely escapes this silencing, remains transcriptionally active (often with *elevated* mRNA levels relative to normal alleles due to reduced translational efficiency triggering a compensatory transcriptional upregulation), and it is this elevated/expanded transcript itself that is pathogenic in FXPOI.

**Chromosomal abnormalities:** Not applicable — FXPOI is a repeat-expansion disorder at a single locus, not a large-scale chromosomal rearrangement/aneuploidy (distinguishing it from Turner syndrome and other chromosomal causes of POI in the differential diagnosis).

**Suggested gene/ontology annotations:** Gene: `hgnc:3775` (FMR1). Inheritance: X-linked, dominant with incomplete/age- and repeat-length-dependent penetrance (HP:0001417 X-linked dominant inheritance, or more precisely captured via the dismech `Inheritance` block with `inheritance_term` — note this is *not* classic digenic/oligogenic, but repeat-length is a genuinely graded/quantitative penetrance modifier worth capturing structurally).

---

## 5. Environmental Information

No specific environmental toxin, occupational exposure, or lifestyle factor has been established as a direct cause or major modifier of FXPOI in the literature surveyed — it is fundamentally a monogenic, repeat-length-dependent disorder. General POI risk factors that are **not** part of the FXPOI mechanism but are relevant to the broader differential diagnosis and comorbidity picture include: smoking (associated with earlier natural menopause generally), pelvic radiation, gonadotoxic chemotherapy (alkylating agents), and autoimmune conditions (autoimmune oophoritis, autoimmune polyglandular syndrome). No infectious agent is implicated in FXPOI.

---

## 6. Mechanism / Pathophysiology

FXPOI's pathophysiology is best understood as a graded causal chain from a genetic lesion to an organ-level clinical syndrome:

**1. Trigger — Premutation CGG-repeat expansion (55–200 repeats) in *FMR1* 5′UTR** → the expanded, largely unmethylated allele is actively transcribed, producing **elevated levels of *FMR1* mRNA** containing the expanded CGG tract (2- to 8-fold increases reported in premutation carriers relative to normal-allele controls), while **FMRP protein translation is relatively reduced/inefficient** at larger repeat sizes (a partial loss-of-function component coexists with the dominant gain-of-function RNA mechanism).

**2. Molecular mechanism — RNA toxic gain-of-function (leading hypothesis) ± RAN-translation protein toxicity (secondary/complementary hypothesis):**
- **RNA toxicity:** The expanded CGG-repeat-containing *FMR1* mRNA forms **intranuclear RNA aggregates/foci** that sequester RNA-binding proteins essential for normal cellular function. In human granulosa-cell culture models, expanded CGG-repeat RNA accumulates in these intranuclear structures and **causes significant granulosa-cell death independent of FMRpolyG expression**, directly supporting an RNA-driven (not solely protein-driven) toxic mechanism (Rosario et al., *FASEB J* 2022, PMID:36250920). Specific granulosa-cell proteins sequestered by the CGG-RNA aggregates (e.g., FUS, PA2G4, TRA2β — shown reduced in ovarian follicles of an *Fmr1* premutation mouse model) may become functionally deregulated as a consequence.
- **RAN translation / FMRpolyG:** Repeat-associated non-AUG (RAN) translation of the expanded CGG repeat produces an abnormal, aggregation-prone polyglycine-containing protein, **FMRpolyG**, detected in premutation-carrier peripheral blood mononuclear cells and in FMR1-premutation granulosa cells, and proposed as a parallel/complementary toxic-protein mechanism to the RNA-aggregate pathway (PMC8951797; the "RNA or protein based?" debate is reviewed in Mila et al., *Mol Hum Reprod* 2020, PMC7566375). Current evidence favors RNA toxicity as necessary and sufficient for granulosa-cell death, with RAN-translation/FMRpolyG as a potentially contributing but non-essential secondary insult.

**3. Cellular consequence — Granulosa cell dysfunction and death, altered folliculogenesis signaling:**
- Human granulosa cells cultured with CGG-repeat-expanded constructs show significant cell death (dose/repeat-length dependent, mirroring the human non-linear risk curve — worst around 80–120 repeats).
- Premutation carriers show **dysregulated AMH expression in mural granulosa cells** and elevated FSH-receptor mRNA/protein — evidence of disrupted folliculogenesis signaling rather than simple follicle depletion alone (PMC8266831; PLOS ONE 2014 PMC4143194).
- Mouse *Fmr1*-knockout studies additionally implicate **premature activation/recruitment of the primordial follicle pool via increased mTOR/S6K signaling** (i.e., accelerated "burn-through" of ovarian reserve rather than purely increased follicle death), with rapamycin (an mTOR inhibitor) reversing the accelerated-recruitment phenotype and preserving follicle numbers/reproductive lifespan in mice — a mechanistically and therapeutically important finding (Mok-Lin, Ascano, Serganov, Rosenwaks, Tuschl, Williams, *Sci Rep* 2018, 8:588, PMC5766488).

**4. Tissue-level consequence — Accelerated ovarian follicle depletion:** Knock-in mouse models carrying expanded CGG repeats (130, 90, and 100–199 CGG repeat lines have been generated) show **normal establishment of the primordial follicle pool** but a **faster subsequent loss of follicles across all follicle classes** (Hoffman et al., PMID:22470123), i.e., the lesion is in follicle *maintenance/attrition rate*, not initial pool formation — directly analogous to the human clinical picture of normal pubertal onset followed by accelerated reproductive aging.

**5. Organism-level outcome — Depleted ovarian follicle population** → **hypergonadotropic hypogonadism** (compensatory pituitary FSH/LH rise as negative feedback from declining estradiol/inhibin B) → **amenorrhea, hypoestrogenism, infertility before age 40**, with downstream estrogen-deficiency morbidity (bone loss, cardiovascular risk) and psychosocial impact.

**Suggested ontology terms for pathophysiology nodes:**
- Gene/protein: `hgnc:3775` FMR1
- Molecular process: GO:0006417 (regulation of translation); GO:0016556 (mRNA modification, if RAN-translation node is modeled); consider a free-text/qualifier for "RAN translation" and "RNA foci/aggregate formation" if no precise GO term exists
- Cellular process: GO:0006915 (apoptotic process) for granulosa cell death; GO:0001541 (ovarian follicle development) for the folliculogenesis disruption node; GO:0008585 (female gonad development)
- mTOR-related node (mouse mechanism): GO:0038202 (TORC1 signaling) 
- Cell type: CL:0000501 (granulosa cell) — primary cellular target; oocyte (CL:0000023) as the follicle unit ultimately depleted
- Anatomical: UBERON:0000992 (ovary); UBERON:0001301 (ovarian follicle)
- Downstream organism-level phenotype nodes: hypergonadotropic hypogonadism, amenorrhea, osteoporosis (could `conforms_to` the existing `osteoporosis_bone_resorption` module downstream of the estrogen-deficiency node), and potentially a cross-reference to `cellular_senescence`/accelerated-aging framing is **not** well supported by current evidence and should not be over-claimed — this is accelerated follicle attrition via a specific RNA-toxicity/mTOR-hyperactivation mechanism, not generic senescence.

**Note on module fit for this codebase:** Given dismech's existing `renal_cystogenesis`-style and hallmark-style module conventions, FXPOI's causal chain (repeat expansion → RNA toxic gain-of-function/RAN translation → granulosa cell death + mTOR-driven premature follicle recruitment → accelerated follicle depletion → hypergonadotropic hypogonadism) is a clean, atomic, well-evidenced chain suitable for direct `pathophysiology` modeling on the disease entry; it does not obviously need a new shared mechanism module unless curators identify other CGG-repeat RNA-toxicity disorders (e.g., FXTAS itself, or other repeat-expansion diseases) to lump under a shared "RAN-translation/RNA-foci toxicity" module — that would be a design decision for curators, not asserted here.

---

## 7. Anatomical Structures Affected

- **Primary organ:** Ovary (UBERON:0000992), specifically the **ovarian follicles** (UBERON:0001301) and their constituent **granulosa cells** (CL:0000501) and **oocytes** (CL:0000023).
- **Secondary/systemic involvement (via estrogen deficiency):**
  - Skeletal system — bone (reduced mineral density; UBERON:0002481 bone tissue)
  - Cardiovascular system — general elevated risk with chronic estrogen deficiency
  - Reproductive tract more broadly (uterus — atrophic changes with prolonged hypoestrogenism)
  - CNS/behavioral — psychiatric comorbidity (anxiety, depression), and note the co-occurring but mechanistically distinct CNS involvement of FXTAS in the same premutation-carrier population (cerebellum, particularly the middle cerebellar peduncles, in FXTAS — not part of FXPOI's own mechanism but frequently co-discussed in the same patients)
- **Tissue/cell level:** granulosa cells (proliferative/steroidogenic support cells of the follicle) are the principal cellular target shown to undergo CGG-RNA-aggregate-induced death in vitro; oocytes are secondarily lost as the follicular unit is depleted.
- **Subcellular level:** **nucleus** — intranuclear RNA aggregates/foci are the key subcellular pathological structure (GO Cellular Component: nucleoplasm, GO:0005654; consider "ribonucleoprotein complex," GO:1990904, for the RNA-foci structure specifically).
- **Localization:** Bilateral, systemic (both ovaries affected as a consequence of a germline, X-linked genetic lesion present in all cells) — not a focal/lateralized process.

---

## 8. Temporal Development

- **Onset:** Variable — typically manifests in the 3rd–4th decade of life (consistent with the "before age 40" definitional threshold), though case reports document ovarian insufficiency as early as **age 11** presenting as primary amenorrhea/delayed puberty. Onset pattern is generally **insidious/subacute** — irregular cycles often precede frank amenorrhea by months to years ("occult" FXPOI with subclinical diminished ovarian reserve before FSH crosses the diagnostic threshold).
- **Progression:** Not a classically staged disease, but conceptually: (1) normal pubertal onset and follicle pool establishment → (2) accelerated follicle attrition (subclinical/occult phase, detectable via declining AMH/antral follicle count) → (3) rising FSH with cycle irregularity → (4) hypergonadotropic amenorrhea meeting formal FXPOI criteria. Progression rate is **variable between individuals** and does not map cleanly onto repeat length alone (the non-linear repeat-risk curve, Section 2).
- **Disease course pattern:** Can be **abrupt and permanent** cessation of menses in some carriers, or **intermittent/fluctuating** (menses "come and go" over years) in others before permanent cessation — an important counseling point since intermittent ovulatory function means **spontaneous pregnancy remains possible even after a formal FXPOI diagnosis** in some carriers, unlike typical post-menopausal ovarian failure.
- **Duration:** Chronic, generally irreversible once established (analogous to natural menopause, just early), though the intermittent early phase is not necessarily permanent.
- **Remission:** No treatment-induced remission of ovarian function itself exists; intermittent spontaneous ovulatory function (not true "remission") can occur, particularly in the earlier/occult phase.
- **Critical periods / intervention windows:** The **occult/pre-diagnostic phase** (declining ovarian reserve markers, before permanent amenorrhea) is the key window for **fertility-preservation counseling and family-planning decisions**, since options (oocyte/embryo cryopreservation) are foreclosed after full follicle depletion. This is the central rationale for early *FMR1* premutation identification (via family cascade testing or population carrier screening) well before clinical FXPOI onset.

---

## 9. Inheritance and Population

- **Epidemiology:** FXPOI affects **~20% (range 20–30%)** of female *FMR1* premutation carriers, versus a background POI prevalence of **~1%** in the general female population — making it, in aggregate, one of the more common identifiable monogenic contributors to POI once accounted for across the premutation-carrier population (though overall population-attributable incidence is limited by the premutation carrier frequency itself, ~1/130–1/300 women). A recent very large, less-ascertained UK Biobank analysis (~92,000 women; Morbey et al., *Hum Reprod* 2026) found that *FMR1* repeat length increases POI risk from around 36 repeats onward but shows **more modest effect sizes and limited incremental diagnostic utility over a polygenic menopause-timing score** in an unselected population — an important caveat that most of the ~20–30% penetrance figures derive from highly ascertained fragile-X-family cohorts and may overstate absolute risk in unselected premutation carriers identified by population screening.
- **Inheritance pattern:** **X-linked**, with the premutation transmitted from either parent but expansion-instability behavior occurring almost exclusively during **maternal transmission** (a male premutation carrier transmits the premutation to daughters essentially unchanged in size — a key feature distinguishing X-linked *FMR1* transmission from typical X-linked dominant/recessive patterns). Penetrance for FXPOI itself is **incomplete and quantitatively repeat-length-dependent** rather than following simple dominant/recessive rules; a Mendelian dominant/incompletely-penetrant framing, structured as `inheritance_term` bound to an appropriate HPO mode-of-inheritance term (e.g., X-linked dominant inheritance, HP:0001423, with an explicit note on repeat-length-dependent, incomplete penetrance) is the closest fit, though curators should confirm the exact HPO term against the schema's controlled inheritance vocabulary.
- **Penetrance:** Age- and CGG-repeat-size dependent (non-linear, peaking at 85–89 repeats; see Section 2); **not fully penetrant** even at maximal-risk repeat sizes.
- **Expressivity:** Variable — from subclinical diminished ovarian reserve to primary amenorrhea in adolescence; modified by X-inactivation skewing.
- **Genetic anticipation:** FXPOI itself does not show classic anticipation in the carrier, but the **premutation allele is unstable and can expand to the full mutation (causing FXS) in offspring of female carriers** — this is the central genetic-counseling anticipation concern for the *FMR1* locus overall. Expansion risk is repeat-size dependent: **59–79 repeats expand to the full mutation in <50% of transmissions**, while **>90 repeats expand to full mutation in >90% of transmissions**; AGG interruptions reduce expansion risk.
- **Germline mosaicism / somatic mosaicism:** Repeat-length mosaicism across tissues is well documented for the *FMR1* CGG tract generally.
- **Founder effects:** Not prominently described for FXPOI-relevant premutation alleles specifically (contrast with some other repeat-expansion disorders); ethnic/geographic variation in premutation carrier frequency is more attributable to general population-genetic variation in repeat-length distribution than a single founder allele.
- **Consanguinity:** Not a relevant risk factor (X-linked, repeat-instability mechanism, not recessive allele combination).
- **Carrier frequency:** See Section 4 — approximately 1/129–1/300 women pan-ethnically, with substantial cohort/ethnicity-dependent variation; enriched (~2%) among women specifically ascertained for POI.
- **Population demographics:** No strong published evidence of a specific geographically or ethnically restricted high-prevalence founder population for the premutation size range most relevant to FXPOI (contrast to some Ashkenazi-Jewish-enriched Mendelian conditions); sex distribution is **exclusively female by definition** (FXPOI is an ovarian phenotype), though male premutation carriers are relevant as unaffected-by-FXPOI transmitting parents and as an at-risk population for FXTAS. Age distribution of affected individuals spans adolescence (rare) through the late 30s (most common presentation window, given the <40-year diagnostic cutoff).

---

## 10. Diagnostics

**Clinical/laboratory tests:**
- **Diagnostic criteria (consensus):** Absent menses ≥4 months **plus** menopausal-range serum FSH (**>25 IU/L** on ≥2 occasions ≥1 month apart) in a woman **under age 40** with a known *FMR1* premutation.
- **AMH (anti-Müllerian hormone):** Reduced AMH is a useful **earlier/screening marker** of declining ovarian reserve, preceding overt FSH elevation ("occult" FXPOI detection); notably, premutation carriers show *dysregulated* (not simply low) AMH expression at the granulosa-cell level, an active mechanistic research area (PMC8266831).
- **FSH/LH, estradiol:** standard hypergonadotropic hypogonadism labs (LOINC codes exist for FSH, LH, estradiol, AMH panels).
- **Pelvic ultrasound:** antral follicle count, ovarian volume assessment.
- **Karyotype, adrenal/ovarian autoantibodies:** performed as part of the standard POI diagnostic workup to rule out Turner syndrome and autoimmune oophoritis in the differential (ACOG Committee Opinion, "Primary Ovarian Insufficiency in Adolescents and Young Women," 2014).

**Genetic testing:**
- **First-line/definitive test:** *FMR1* CGG-repeat sizing by PCR/Southern blot (specialized fragile-X repeat-sizing assay, not standard NGS) — this is the specific test that establishes premutation-range (55–200 repeats) status and is the basis of the FXPOI diagnosis in a woman with clinical POI.
- **Recommended testing context:** ACOG and ACMG-aligned guidance recommends *FMR1* premutation testing as part of the standard POI diagnostic evaluation (alongside karyotype and autoimmune workup) in any woman diagnosed with POI, given the diagnostic yield (~2% of POI cases).
- **Cascade/family testing:** once a premutation is identified in a proband (e.g., in the context of an FXS-affected child or FXTAS-affected relative), cascade testing of at-risk maternal relatives is standard practice for both FXPOI and reproductive/family-planning counseling.
- **AGG interruption analysis:** increasingly offered alongside repeat sizing to refine offspring expansion-risk counseling (though not shown to refine FXPOI risk to the carrier herself).
- Whole exome/genome sequencing, standard multi-gene NGS panels, chromosomal microarray, and karyotype are **not** the primary diagnostic modality for the *FMR1* repeat expansion itself (repeat-expansion disorders generally require specialized repeat-sizing assays rather than standard short-read NGS, though long-read sequencing methods are emerging for repeat-expansion diagnostics broadly).

**Differential diagnosis for POI presentation (before/alongside *FMR1* testing):** Turner syndrome and other X-chromosome abnormalities (karyotype), autoimmune oophoritis/autoimmune polyglandular syndrome (adrenal/ovarian antibodies, thyroid autoimmunity), iatrogenic causes (chemotherapy, pelvic radiation, oophorectomy), galactosemia (in the context of neonatal/early presentations), other rare monogenic POI genes (e.g., *BMP15*, *FIGLA*, *NR5A1*, *FOXL2*, mitochondrial POI genes), and secondary (hypothalamic-pituitary) causes of amenorrhea (which present with low/normal rather than elevated FSH, distinguishing "primary" ovarian from central causes).

**Screening:** No population-wide newborn or universal screening program for FXPOI specifically exists; the relevant screening context is (a) **carrier screening in reproductive-age women** (increasingly offered as part of expanded carrier screening panels, per ACOG guidance on *FMR1* carrier screening), and (b) **targeted testing of women presenting with POI or unexplained infertility/diminished ovarian reserve**.

---

## 11. Outcome/Prognosis

- **Fertility/survival framing:** FXPOI is not a mortality-associated condition per se; the "outcome" of clinical interest is **reproductive** (loss of fertility, timing of menopause) and **long-term health** (estrogen-deficiency morbidity), not survival.
- **Fertility outcomes:** Loss of fertility before age 40, though — importantly — **intermittent ovulatory function can persist even after formal FXPOI diagnosis** in a subset of women (unlike natural post-menopausal ovarian failure), meaning spontaneous conception, while unlikely, is not impossible after diagnosis; this materially affects contraceptive and family-planning counseling.
- **Morbidity:** Chronic estrogen deficiency drives the principal morbidity burden: **reduced bone mineral density/early osteoporosis risk**, **increased cardiovascular disease risk** (accelerated relative to women with typical-age menopause), and **psychiatric morbidity** (depression, anxiety related to infertility and hormonal loss) — explicitly identified as the three key morbidity domains in the 2011 NFXF consensus recommendations.
- **Quality of life:** Significantly impacted by the combination of infertility-related grief, hormonal symptoms (vasomotor symptoms, mood), and (for many carriers) the broader family context of having/anticipating an FXS-affected child, compounding psychosocial burden beyond the ovarian phenotype alone.
- **Prognostic factors:** CGG repeat size (non-linearly, per the risk curve), age at presentation, degree of X-inactivation skewing, and baseline/serial AMH trajectory are the main factors influencing individual prognosis and time-course, though **no validated clinical prediction model exists to precisely forecast timing of complete ovarian failure for an individual carrier**.
- **Recovery potential:** No treatment reverses the underlying follicle depletion; hormone replacement addresses downstream estrogen-deficiency symptoms/morbidity but does not restore fertility.

---

## 12. Treatment

**Pharmacotherapy (symptom/morbidity management, not disease-reversing):**
- **Hormone replacement therapy (estrogen ± progestin)** is the mainstay for managing vasomotor symptoms and — critically — for **bone and cardiovascular protection** in women with premature estrogen deficiency; standard POI management guidelines (extrapolated from general POI/HRT literature, as FXPOI-specific RCTs are limited) recommend HRT continued at least until the average natural age of menopause (~51 years) unless contraindicated.
  - Suggested MAXO/NCIT: `NCIT:C15986` Pharmacotherapy + `therapeutic_agent` bound to CHEBI estrogen/progestin compounds (e.g., estradiol).
- **Bone health:** calcium/vitamin D supplementation, DXA bone density monitoring, and bisphosphonates or other bone-protective agents in established osteoporosis, per general POI/osteoporosis management guidelines.
- **Psychiatric/psychological support:** treatment of comorbid anxiety/depression (pharmacologic and psychotherapeutic) is explicitly recommended given the high burden of mood symptoms in this population.

**Fertility-related interventions:**
- **Fertility preservation (oocyte or embryo cryopreservation)**, ideally undertaken **before** significant ovarian reserve decline — i.e., as early as possible after a premutation is identified in a woman of reproductive age, given the unpredictable and sometimes rapid course of follicle depletion. MAXO term: consider `MAXO:0000950` (supportive care) or a more specific reproductive-technology term if the schema supports it (fertility preservation is not cleanly covered by the standard MAXO treatment list referenced in this repo's CLAUDE.md; NCIT has more specific fertility-preservation procedure terms that should be looked up directly via OAK).
- **Donor oocyte IVF**: standard option for carriers who have progressed to overt ovarian failure and desire biological pregnancy.
- **Preimplantation genetic testing (PGT)** for carriers pursuing IVF, to select against full-mutation expansion in offspring — a reproductive-genetic intervention distinct from FXPOI treatment per se but highly relevant to the same patient population's family planning.

**Experimental/emerging:**
- **mTOR-pathway modulation (rapamycin)**: mouse model evidence (Mok-Lin et al., *Sci Rep* 2018) that rapamycin reverses premature primordial-follicle recruitment and preserves ovarian reserve in *Fmr1*-knockout mice is a promising **preclinical, not yet clinically validated**, therapeutic lead — explicitly a `MODEL_SYSTEM_EXTRAPOLATION`-type finding (per this repo's schema conventions) that has **not** been shown to translate to human FXPOI prevention/treatment; any dismech curation of this should be flagged as model-organism evidence only, not extrapolated to a human treatment recommendation.
- No *FMR1*-targeted gene therapy, RNA-targeted therapy (e.g., ASO), or disease-modifying pharmacotherapy specific to FXPOI has reached clinical use or late-stage trials based on the literature surveyed; this remains an area of active preclinical mechanistic research (RNA-toxicity-targeted approaches are conceptually plausible given the RAN-translation/RNA-foci mechanism but not yet clinically developed for FXPOI specifically).

**Treatment strategy:** Management is fundamentally **supportive/preventive** rather than curative — early identification (via *FMR1* testing in POI workups or cascade/carrier screening), proactive fertility-preservation counseling before reserve is lost, HRT for symptom control and long-term bone/cardiovascular protection, and psychiatric screening/support, per the NFXF Clinical & Research Consortium's 2011 consensus and later updates (5th International Conference on FMR1 Premutation recommendations, PMC10529056).

---

## 13. Prevention

- **Primary prevention** of FXPOI itself (preventing the genetic lesion) is not possible — it is a germline genetic condition; "prevention" in practice means **preventing its downstream consequences** through early detection.
- **Secondary prevention (early detection):** Identification of *FMR1* premutation carrier status **before** onset of clinical FXPOI — via (a) cascade testing of at-risk female relatives of a known fragile-X family, or (b) expanded reproductive/prenatal carrier screening — enables anticipatory fertility-preservation counseling and family-planning decisions while ovarian reserve is still adequate.
- **Genetic counseling:** A central preventive/management tool — carriers should receive counseling on (a) their own FXPOI risk (repeat-length-informed, though imprecise for an individual), (b) offspring expansion-to-full-mutation risk (repeat-size- and AGG-interruption-informed), and (c) reproductive options including prenatal diagnosis or PGT.
- **Tertiary prevention (preventing complications once FXPOI has occurred):** HRT to prevent/mitigate osteoporosis and cardiovascular disease, bone density monitoring, and mental health screening/support — i.e., preventing the *downstream* morbidity of established ovarian insufficiency, per the consensus management recommendations discussed in Section 12.
- **Screening programs:** No population-wide newborn screening; the relevant screening is targeted reproductive carrier screening (increasingly included in expanded carrier-screening panels) and diagnostic-context testing of women presenting with POI/infertility.
- **Public health/environmental interventions:** Not applicable — no environmental exposure to mitigate.

---

## 14. Other Species / Natural Disease

- No naturally occurring veterinary/companion-animal analog of FXPOI has been identified in the literature surveyed (unlike Fragile X Syndrome, for which no robust natural-disease animal counterpart exists either — the condition is modeled exclusively via engineered genetic models, not naturally occurring animal disease).
- **Orthologous gene:** *Fmr1* is highly conserved; mouse *Fmr1* (MGI:95523) is the standard ortholog used for modeling (NCBI Gene mouse Fmr1: Gene ID 14265).
- No OMIA (Online Mendelian Inheritance in Animals) entry for a natural CGG-repeat-expansion ovarian insufficiency disorder was identified — this is expected, as trinucleotide-repeat instability disorders of this type are essentially unique to the human *FMR1* locus's particular repeat architecture and are not known to occur naturally in veterinary species.
- **Comparative biology:** FMRP function and the RNA-binding/translational-regulation biology are broadly conserved across mammals, supporting the validity of mouse knock-in models for mechanistic study (see Section 15), though no spontaneous/natural veterinary disease exists to compare.

---

## 15. Model Organisms

**Genetic mouse models (knock-in, the dominant model system for FXPOI mechanism research):**
- **CGG-repeat knock-in mice**: at least three independently generated knock-in lines carrying expanded CGG repeats in the murine *Fmr1* 5′UTR — commonly cited repeat sizes include **~130 CGG repeats**, **~90 CGG repeats**, and a **100–199 CGG repeat** line — used to model the premutation state and its RNA-toxicity consequences in vivo.
  - **Key phenotype recapitulation:** normal establishment of the primordial follicle pool (i.e., the *initial* reproductive endowment is unaffected) but an **accelerated rate of follicle loss across all follicle classes**, closely mirroring the human clinical pattern of normal puberty followed by premature reproductive aging (Hoffman et al., PMID:22470123).
  - Reduced expression of specific RNA-binding proteins (FUS, PA2G4, TRA2β) demonstrated in ovarian follicles of a premutation knock-in mouse model, supporting the human granulosa-cell RNA-sequestration mechanism.
- ***Fmr1*-knockout (null) mice** (a distinct, loss-of-function-only model, not repeat-expansion "premutation" per se) also show **premature recruitment of the primordial follicle pool** via **increased mTOR/S6 kinase activity**, with rapamycin reversing the phenotype — this specific mechanistic lead (mTOR hyperactivation → premature follicle recruitment) currently derives from the *knockout* rather than repeat-expansion knock-in model, an important nuance: the mTOR-hyperactivation mechanism observed in *Fmr1*-null mice may reflect FMRP loss-of-function rather than the CGG-repeat-RNA gain-of-function mechanism thought to dominate the human premutation/FXPOI phenotype, so translational applicability of the rapamycin finding specifically to human FXPOI (a gain-of-function-driven condition) should be considered with appropriate caution — an explicit `HUMAN_MODEL_MISMATCH`-type caveat if curated in dismech, since the knockout model isolates loss-of-FMRP-function whereas human FXPOI is attributed primarily to premutation-range RNA toxicity, a mechanistically distinct (though possibly convergent, via mTOR) pathway.

**In vitro / cellular models:**
- **Human granulosa-cell culture models** transfected with expanded-CGG-repeat *FMR1* constructs are the key human-cell system directly demonstrating **CGG-RNA-aggregate-induced granulosa cell death**, independent of FMRpolyG — the most direct human-tissue-relevant mechanistic evidence available (Rosario et al. 2022; earlier work in *Fertility and Sterility* establishing the original "RNA toxic gain-of-function" granulosa-cell model).
- **Patient-derived granulosa cells** obtained from IVF cycles of premutation carriers have been used directly (not just engineered cell lines) to show elevated *FMR1* mRNA, dysregulated AMH, and elevated FSH-receptor expression correlating with reduced oocyte yield — a valuable "natural human cellular model" complementing the engineered systems.

**Model limitations:** Mouse models recapitulate the accelerated-follicle-loss phenotype well but do not fully capture the human non-linear ("inverted-U") repeat-length risk curve in vivo across a matched range of repeat sizes within a single study, nor the full spectrum of human FXAND/psychiatric comorbidity; and as noted above, the mechanistically important mTOR/rapamycin finding derives from a null (knockout) rather than repeat-expansion (knock-in) model, creating a translational-validity gap between the proposed therapeutic lead and the actual human disease mechanism that should be flagged rather than assumed resolved.

**Applications:** These models are used to dissect (a) RNA- vs protein-mediated toxicity, (b) the follicle-pool-establishment-vs-attrition-rate question, (c) candidate therapeutic targets (mTOR pathway), and (d) sequestered-protein identification (FUS, PA2G4, TRA2β) as downstream biomarker/mechanism candidates.

---

## Summary Table for Curation

| Domain | Key value |
|---|---|
| Gene | *FMR1*, HGNC:3775, Xq27.3 |
| Causal lesion | CGG-repeat premutation expansion, 55–200 repeats, 5′UTR |
| OMIM | #311360 (POF1) |
| Orphanet | ORPHA:642691 |
| Penetrance in carriers | ~20% (20–30%), non-linear by repeat size, peak risk 85–89 repeats |
| Background POI prevalence | ~1% |
| Diagnostic criteria | Amenorrhea ≥4 mo + FSH >25 IU/L ×2, age <40, known *FMR1* premutation |
| Core mechanism | CGG-repeat RNA toxic gain-of-function (intranuclear RNA foci) ± RAN-translation FMRpolyG → granulosa cell death + mTOR-driven premature follicle recruitment → accelerated follicle depletion |
| Key cell type | Granulosa cell (CL:0000501) |
| Key organ | Ovary (UBERON:0000992) |
| Treatment | Symptomatic/preventive: HRT, fertility preservation, bone/cardiovascular monitoring, psychiatric support; no disease-modifying therapy |

---

## Sources

- [Understanding decreased fertility in women carriers of the FMR1 premutation: a possible mechanism for FXPOI](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4141264/)
- [Evidence for a fragile X messenger ribonucleoprotein 1 (FMR1) mRNA gain-of-function toxicity mechanism contributing to the pathogenesis of FXPOI (PMID:36250920)](https://pubmed.ncbi.nlm.nih.gov/36250920/)
- [Use of model systems to understand the etiology of FXPOI](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4139715/)
- [Expression of FMRpolyG in Peripheral Blood Mononuclear Cells of Women with FMR1 Premutation](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8951797/)
- [Refining the risk for FXPOI by FMR1 CGG repeat size (PMID:33927378)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8460441/)
- [Insight and Recommendations for Fragile X-Premutation-Associated Conditions, 5th International Conference](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10529056/)
- [MedlinePlus: Fragile X-associated primary ovarian insufficiency](https://medlineplus.gov/download/genetics/condition/fragile-x-associated-primary-ovarian-insufficiency.pdf)
- [Orphanet: Fragile X-associated primary ovarian insufficiency (ORPHA:642691)](https://www.orpha.net/en/disease/detail/642691)
- [OMIM #311360 — Premature Ovarian Failure 1 (POF1)](https://omim.org/entry/311360)
- [FMR1 Disorders — GeneReviews (NBK1384)](https://www.ncbi.nlm.nih.gov/books/NBK1384/)
- [Approaches to identify genetic variants that influence the risk for onset of FXPOI](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4124461/)
- [Premature ovarian failure — Orphanet Journal of Rare Diseases](https://link.springer.com/article/10.1186/1750-1172-1-9)
- [Is there a CGG repeat threshold to predict occult premature ovarian failure in fragile X premutation carriers?](https://www.fertstert.org/article/S0015-0282(19)30181-5/fulltext)
- [FMR1 Premutation Testing: CGG Repeat Ranges, FXPOI, FXTAS & Genetic Interpretation](https://lamkinclinic.com/fmr1/)
- [FXPOI: Pattern of AGG Interruptions Does not Show an Association With Age at Amenorrhea](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6086008/)
- [Large-scale analysis of FMR1 CGG repeat length and risk of premature ovarian insufficiency in over 92,000 women — Human Reproduction](https://academic.oup.com/humrep/article/41/6/998/8658897)
- [Dysregulation of anti-Müllerian hormone expression levels in mural granulosa cells of FMR1 premutation carriers](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8266831/)
- [Fragile X-Associated Primary Ovarian Insufficiency (FXPOI) Treatment Recommendation — NFXF](https://fragilex.org/our-research/treatment-recommendations/fragile-x-associated-primary-ovarian-insufficiency)
- [FRAGILE X-ASSOCIATED PRIMARY OVARIAN INSUFFICIENCY Consensus Document (2011)](https://fragilex.org/wp-content/uploads/2018/11/FX_PrimaryOvarianInsufficiency_Consensus_Document.pdf)
- [Fragile X Associated Primary Ovarian Insufficiency (FXPOI): Case Report and Literature Review](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6278244/)
- [NICHD: About Fragile X-Associated Primary Ovarian Insufficiency](https://www.nichd.nih.gov/health/topics/fxpoi/conditioninfo)
- [Ovarian abnormalities in a mouse model of fragile X primary ovarian insufficiency (PMID:22470123)](https://pubmed.ncbi.nlm.nih.gov/22470123/)
- [Premature recruitment of oocyte pool and increased mTOR activity in Fmr1 knockout mice and reversal of phenotype with rapamycin](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5766488/)
- [The impact of FMR1 gene mutations on human reproduction and development: a systematic review](https://pmc.ncbi.nlm.nih.gov/articles/PMC5010819/)
- [The molecular mechanisms that underlie fragile X-associated premature ovarian insufficiency: is it RNA or protein based?](https://pmc.ncbi.nlm.nih.gov/articles/PMC7566375/)
- [Elevated Levels of FMR1 mRNA in Granulosa Cells Are Associated with Low Ovarian Reserve in FMR1 Premutation Carriers](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4143194/)
- [Association of skewed X-chromosome inactivation with FMR1 CGG repeat length and anti-Müllerian hormone levels](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5410032/)
- [FMR1 premutation carrier frequency in patients undergoing routine population-based carrier screening — Genetics in Medicine](https://www.nature.com/articles/gim920117)
- [FMR1 premutation frequency in a large, ethnically diverse population referred for carrier testing (Owens et al. 2018)](https://onlinelibrary.wiley.com/doi/full/10.1002/ajmg.a.38692)
- [Population-based estimates of the prevalence of FMR1 expansion mutations in women with early menopause and primary ovarian insufficiency](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3914024/)
- [Prevalence of the FMR1 Gene Premutation in Young Women with Diminished Ovarian Reserve in an IVF Program](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11353426/)
- [Primary Ovarian Insufficiency in Adolescents and Young Women — ACOG Committee Opinion](https://www.acog.org/clinical/clinical-guidance/committee-opinion/articles/2014/07/primary-ovarian-insufficiency-in-adolescents-and-young-women)
- [Primary Ovarian Insufficiency — StatPearls](https://www.ncbi.nlm.nih.gov/books/NBK589674/)
- [Primary ovarian insufficiency: update on clinical and genetic findings](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11466302/)
- [Fragile X Premutation Associated Conditions (FXPAC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7267017/)
- [Fragile X-Associated Neuropsychiatric Disorders (FXAND) in Young Fragile X Premutation Carriers](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9778214/)
- [Cardiovascular Problems in the Fragile X Premutation](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7578382/)