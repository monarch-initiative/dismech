---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-27T03:32:47.813707'
end_time: '2026-08-27T03:37:45.468521'
duration_seconds: 297.65
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Leukocyte Adhesion Deficiency Type II
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
  - claude-sonnet-5
  web_search_requests: 19
  num_turns: 25
  total_cost_usd: 1.4424039999999998
  session_id: 00937d02-a143-56ac-a731-3747f9ee4c64
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 33
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 7
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Leukocyte Adhesion Deficiency Type II
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Leukocyte Adhesion Deficiency Type II** covering all of the
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

# Leukocyte Adhesion Deficiency Type II — Comprehensive Research Report

## 1. Disease Information

**Overview.** Leukocyte Adhesion Deficiency Type II (LAD II) is an ultra-rare autosomal recessive congenital disorder of glycosylation caused by defective transport of GDP-fucose into the Golgi apparatus. The resulting global hypofucosylation of glycoconjugates abolishes selectin-ligand function on leukocytes (causing an immunodeficiency phenotype of recurrent infections and persistent leukocytosis) and produces the Bombay (hh) erythrocyte blood phenotype, together with severe psychomotor and growth retardation. It is classified simultaneously as a primary immunodeficiency (leukocyte adhesion defect) and as a congenital disorder of glycosylation (CDG).

**Key identifiers:**
- **OMIM phenotype:** #266265 — Congenital Disorder of Glycosylation, Type IIc (CDG2C) ([OMIM](https://omim.org/entry/266265))
- **OMIM gene:** *605881 — SLC35C1 ([OMIM](https://omim.org/entry/605881))
- **Orphanet:** ORPHA:99843 — Leukocyte adhesion deficiency type II ([Orphanet](https://www.orpha.net/en/disease/detail/99843))
- **HGNC gene ID:** HGNC:20197 (SLC35C1)
- **NCBI GTR condition:** C0398739

**Synonyms:** LAD-II, LAD2; CDG-IIc / CDG2C; SLC35C1-CDG; GDP-fucose transporter deficiency; GDP-L-fucose transporter 1 deficiency; Rambam-Hasharon syndrome (after the hospital where early cases were characterized) ([Wikipedia](https://en.wikipedia.org/wiki/Congenital_disorder_of_glycosylation_type_IIc)).

**Data provenance.** Because fewer than 30 cases have ever been reported (Orphanet states <10; a 2024 review cites 19 diagnosed cases — [ScienceDirect 2024](https://sciencedirect.com/science/article/pii/S1357272524000943)), essentially all available information derives from individual case reports and small case series (typically 1–3 patients each) rather than large aggregated cohorts or registries — this is a case-report-driven literature, not an EHR/registry-derived one.

---

## 2. Etiology

**Disease Causal Factors.** LAD II is a monogenic, purely genetic disorder — there is no known environmental or infectious causal contribution to disease initiation. It is caused by biallelic loss-of-function variants in **SLC35C1** (11p11.2), encoding the Golgi GDP-fucose transporter (FUCT1) ([Nature Genetics, Lübke et al. 2001, PMID:11326279](https://pubmed.ncbi.nlm.nih.gov/11326279/)).

**Genetic Risk Factors.**
- Biallelic pathogenic **SLC35C1** variants (homozygous or compound heterozygous) are necessary and sufficient. Two founder missense mutations dominate the earliest-reported cases:
  - **p.Arg147Cys (R147C)** — identified in the first reported (Turkish-derived) patient ([Lübke et al. 2001](https://pubmed.ncbi.nlm.nih.gov/11326279/)).
  - **p.Thr308Arg (T308R)** — a founder mutation among Arab-Israeli families; genealogic review found two patients' great-grandmothers were sisters, and all three original Arab-Israeli patients lived within roughly a 10-square-mile area, indicating a common founder ([Etzioni et al. 2002, PMID:12116250](https://pubmed.ncbi.nlm.nih.gov/12116250/)). Patients homozygous for T308R had a more severe growth and cognitive phenotype than the R147C patient.
  - Additional pathogenic alleles reported include splice-site, frameshift (e.g., compound heterozygous c.247_249delGTG + c.177_179delTAA), and other missense variants; a 2024 functional survey examined 11 distinct mutant SLC35C1 proteins and found differential residual transport activity correlating with phenotypic severity ([ScienceDirect 2024](https://sciencedirect.com/science/article/pii/S1357272524000943)).
  - **Consanguinity/founder populations**: reported cases cluster in consanguineous Turkish and Arab (Israeli/Palestinic) kindreds, consistent with a rare autosomal recessive founder-driven disorder.
- No susceptibility loci or polygenic risk factors are described — this is a single-gene Mendelian disease.

**Environmental Risk Factors.** None established; age of onset and severity are gene-dosage/allele-dependent rather than environmentally triggered, although infectious burden (recurrent bacterial infections) is a consequence, not a cause, of the underlying glycosylation defect.

**Protective Factors.**
- **Genetic:** None specific reported; however, residual/hypomorphic SLC35C1 alleles (rather than complete null alleles) are associated with the recently described **milder phenotypic variant** (see below), effectively acting as a modifying/protective genotype relative to classic severe LAD II.
- **Environmental/Dietary:** Exogenous dietary **L-fucose** functions as a "protective"/corrective intervention rather than a naturally protective exposure — oral fucose supplementation can restore fucosylated glycan synthesis via a transporter-independent salvage pathway (see Mechanism and Treatment sections).

**Gene-Environment Interactions.** The central gene-environment interaction in LAD II is therapeutic rather than pathogenic: supplementing the diet with L-fucose bypasses the defective SLC35C1-dependent de novo GDP-fucose synthesis/transport pathway by feeding an alternative "salvage" route that preferentially uses exogenous fucose over de novo-synthesized GDP-fucose ([Yu et al., J Biol Chem 2022, PMC9304781](https://ncbi.nlm.nih.gov/pmc/articles/PMC9304781)). This is the mechanistic basis for oral fucose therapy's efficacy in a subset of patients.

---

## 3. Phenotypes

LAD II phenotypes span three broad domains: immunodeficiency/hematologic, growth/neurodevelopmental, and dysmorphic/dental. Onset is typically infancy to early childhood.

**Immunologic / Hematologic (laboratory abnormalities and clinical signs):**
- **Persistent leukocytosis with neutrophilia**, WBC counts reported in the range of 30,000–150,000/mm³ (HP: Leukocytosis, HP:0001974; HP: Neutrophilia, HP:0011897) ([Wikipedia](https://en.wikipedia.org/wiki/Congenital_disorder_of_glycosylation_type_IIc)).
- **Recurrent bacterial infections** — pneumonia, otitis media, cellulitis/skin infections, urinary tract infections, gum/periodontal infections (HP: Recurrent bacterial infections, HP:0002718; HP: Recurrent respiratory infections, HP:0002205; HP: Otitis media, HP:0000388).
- Impaired neutrophil motility/chemotaxis and defective leukocyte rolling/adhesion due to absent selectin-ligand (sialyl-Lewis X) expression — a laboratory/functional finding rather than a symptom per se.
- Unlike LAD I, most LAD II patients **can form pus** and abscesses, and infections tend to be milder and less life-threatening than in LAD I, though this is not universal across reports ([StatPearls, NCBI Bookshelf NBK539770](https://www.ncbi.nlm.nih.gov/books/NBK539770/)).
- **Bombay (hh) blood phenotype** — absence of the H antigen on erythrocytes due to defective fucosylation, essentially pathognomonic when combined with the clinical picture (HP term candidates: Abnormal erythrocyte morphology is imprecise; best captured structurally rather than via a specific HP term — record via blood group/biochemical finding).

**Growth (onset: infancy/early childhood, typically progressive/stable rather than episodic):**
- **Severe growth retardation / short stature**, often including intrauterine growth retardation and failure to thrive (HP: Short stature, HP:0004322; HP: Intrauterine growth retardation, HP:0001511; HP: Failure to thrive, HP:0001508). Severity varies with genotype (T308R > R147C in the founder cohort).

**Neurodevelopmental (progressive but variably severe; dominates the adult clinical picture):**
- **Severe intellectual disability / psychomotor retardation** (HP: Intellectual disability, severe, HP:0010864).
- Seizures (HP:0001250), ataxia (HP:0001251), cerebral atrophy (HP:0002059) reported in some patients ([GARD](https://rarediseases.info.nih.gov/diseases/4634/leukocyte-adhesion-deficiency-type-ii/)).
- Notably, **in adulthood, intellectual deficit and growth retardation — not infections — dominate the clinical picture**, reflecting relative stabilization of the immunologic phenotype with age and the persistence of the neurodevelopmental defect ([Orphanet](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=99843)).

**Dysmorphic/Craniofacial:**
- Distinctive facies, most consistently a **depressed/flat nasal bridge**; also described: micrognathia, coarse facial appearance (HP: Depressed nasal bridge, HP:0005280; HP: Micrognathia, HP:0000347).

**Dental/Periodontal (age-dependent, progressive):**
- **Severe periodontitis with gingival inflammation, alveolar bone loss, and early/premature loss of primary and permanent teeth** — a hallmark late feature, mechanistically explained by defective neutrophil recruitment to the gingival sulcus (HP: Periodontitis, HP:0000704; HP: Gingivitis; recurring theme across LAD subtypes) ([PLOS Pathogens, Moutsopoulos et al.](https://journals.plos.org/plospathogens/article?id=10.1371%2Fjournal.ppat.1004698)).

**Other reported features:** chronic diarrhea, keratitis, anemia (variably reported per GARD).

**A recently delineated milder phenotypic spectrum.** Tahata et al. (2022, *Am J Med Genet A* 188(7):2005–2018, [Wiley](https://onlinelibrary.wiley.com/doi/abs/10.1002/ajmg.a.62737)) and an earlier case report ([PMID:24403049](https://pubmed.ncbi.nlm.nih.gov/24403049/)) describe patients with **short stature and developmental delay but minimal or absent immune/hematologic manifestations** — i.e., growth/neurodevelopmental phenotype without the classic recurrent-infection/leukocytosis picture. A 2020 *Journal of Human Genetics* report similarly described biallelic SLC35C1 variants causing **isolated short stature with intellectual disability** without an overt immunodeficiency ([Nature/JHG 2020](https://www.nature.com/articles/s10038-020-0764-4)). This indicates a genotype-correlated phenotypic continuum from classic severe LAD II to a mild "SLC35C1-CDG" presentation.

**Quality of life impact:** Not systematically studied with validated instruments (no EQ-5D/SF-36 data identified); qualitatively, recurrent infections and periodontal disease impose major morbidity in childhood, while intellectual disability and short stature dominate long-term functional/QoL impact into adulthood.

---

## 4. Genetic/Molecular Information

**Causal Gene:** SLC35C1 (previously FUCT1), OMIM *605881, HGNC:20197, chromosome **11p11.2**. Encodes a **10-transmembrane-domain Golgi antiporter** (364 amino acids, ~39.8 kDa) that imports cytosolic GDP-fucose into the Golgi lumen in exchange for GMP; transmembrane domains 3, 4, 7, and 9 are highly conserved (domains 4 and 9 notably hydrophilic), and the cytosolic C-terminus is essential for transport activity ([GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=SLC35C1); [PMID:22492235](https://pubmed.ncbi.nlm.nih.gov/22492235/)).

**Pathogenic Variants:**
- **Variant types:** missense (R147C, T308R, G281D, and others), splice-region, and small in-frame/frameshift deletions (e.g., compound heterozygous c.247_249delGTG / c.177_179delTAA) are all reported ([ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/); e.g. RCV000984510 for p.Gly281Asp, RCV001506269 for a synonymous/splice variant).
- **ACMG classification:** ClinVar entries for SLC35C1 variants associated with LAD II are generally classified pathogenic/likely pathogenic in the context of biallelic inheritance.
- **Functional consequence:** predominantly **loss of function** — reduced or absent GDP-fucose transport activity into the Golgi, producing global hypofucosylation. A 2024 functional screen of 11 mutant SLC35C1 proteins found a gradient of residual activity that tracks with clinical severity, providing a mechanistic explanation for the phenotypic spectrum ([ScienceDirect 2024](https://sciencedirect.com/science/article/pii/S1357272524000943)).
- **Allele frequency:** Given extreme rarity and founder-effect clustering, population allele frequencies in gnomAD are expected to be very low/absent for the specific founder alleles (not independently verified in this search).
- **Somatic vs. germline:** exclusively germline.

**Modifier Genes / Alternative Pathways.**
- **SLC35C2** is a putative paralogous transporter; a 2023 *J Biol Chem* study provided *in vivo* evidence for residual GDP-fucose transport in the combined absence of SLC35C1 and SLC35C2, indicating an additional, still-uncharacterized transport/salvage route ([PMC10709068](https://pmc.ncbi.nlm.nih.gov/articles/PMC10709068/)).
- A parallel **fucose salvage pathway** (dietary/exogenous fucose → fucose kinase/GDP-fucose pyrophosphorylase → cytosolic GDP-fucose, independent of de novo synthesis) preferentially incorporates exogenous over de novo GDP-fucose and is the mechanistic basis for the efficacy of oral fucose therapy even in SLC35C1-null backgrounds ([Yu et al. 2022, PMC9304781](https://ncbi.nlm.nih.gov/pmc/articles/PMC9304781)).
- A 2006 report described "LAD II patients with a dual defect of the GDP-fucose transporter," suggesting additional genetic complexity/modifiers in some cases ([Blood 107(10):3959](https://ashpublications.org/blood/article/107/10/3959/109832/)).

**Epigenetic Information:** No disease-specific epigenetic (methylation/histone) mechanisms have been reported for LAD II; the defect is purely biosynthetic/transport-based at the level of nucleotide-sugar delivery, not gene expression regulation.

**Chromosomal Abnormalities:** Not applicable — LAD II is caused by point/small-indel variants within SLC35C1, not by large chromosomal rearrangements, aneuploidy, or CNVs.

---

## 5. Environmental Information

LAD II has **no established environmental, lifestyle, or infectious causal contributors** — it is a fully penetrant monogenic recessive disorder. The "environmental" dimension relevant to this disease is therapeutic (dietary fucose supplementation), not causal or risk-modifying in the pathogenic sense. No occupational, toxin, or pollutant exposures have been linked to disease risk or severity. No infectious agent triggers the underlying molecular defect (though the disease predisposes to opportunistic and recurrent bacterial infections as a downstream consequence).

---

## 6. Mechanism / Pathophysiology

**Causal chain (upstream → downstream):**

1. **Molecular defect (upstream):** Biallelic loss-of-function SLC35C1 variants abolish or reduce Golgi GDP-fucose transporter (FUCT1) activity.
2. **Biochemical consequence:** GDP-fucose synthesized in the cytosol (via the de novo GDP-mannose → GDP-fucose pathway) cannot be efficiently transported across the Golgi membrane into the lumen, where fucosyltransferases require it as substrate.
3. **Glycosylation consequence:** Global **hypofucosylation** of N-glycans, O-glycans, and glycolipids — a Golgi/molecular-function-level defect (candidate GO term: **fucosylation, GO:0036065**; **GDP-fucose transmembrane transporter activity, GO:0005457**).
4. **Cell-surface consequence on leukocytes:** Failure to synthesize **sialyl-Lewis X (SLeX/CD15s)**, the fucosylated tetrasaccharide ligand required for E-, P-, and L-selectin binding (candidate biological process: selectin ligand biosynthesis).
5. **Functional consequence — leukocyte trafficking:** Loss of selectin-ligand function abolishes **leukocyte rolling** on activated endothelium, the first step of the leukocyte adhesion cascade preceding firm adhesion and transendothelial migration. In the Slc35c1-knockout mouse, E-, L-, and P-selectin–dependent rolling in cremaster venules was virtually absent, firm adhesion was strongly reduced, and neutrophil migration to the inflamed peritoneum was reduced by ~89% ([Blood 112(4):1472, Smith et al. / mouse model paper](https://ashpublications.org/blood/article/112/4/1472/25356/)).
6. **Clinical consequence:** Impaired neutrophil extravasation to infection sites → recurrent bacterial infections, marked peripheral **leukocytosis** (neutrophils cannot leave the circulation), and periodontal disease (failure of neutrophil surveillance of the gingival sulcus).
7. **Parallel, independent consequence — erythrocytes:** Loss of α1,2-fucosylation of the H-antigen precursor on red cells produces the **Bombay (hh) blood phenotype**, a diagnostically useful but pathophysiologically separate readout of the same core biochemical defect.
8. **Parallel, independent consequence — growth/CNS:** Global hypofucosylation of glycoproteins/glycolipids required for normal growth-factor signaling and neurodevelopment is thought to underlie the severe growth retardation and intellectual disability, though the precise fucosylated substrates responsible for the neurodevelopmental phenotype are less well characterized than the selectin-ligand mechanism.

**Cell types and processes involved (ontology anchors):**
- **Cell types (CL):** neutrophil (CL:0000775), erythrocyte (CL:0000232), vascular endothelial cell (CL:0000071) — the selectin-expressing "receiver" cell in the rolling interaction.
- **Molecular functions (GO):** GDP-fucose transmembrane transporter activity (GO:0005457); fucosyltransferase activity (GO:0008417); selectin binding.
- **Biological processes (GO):** protein fucosylation (GO:0036065); leukocyte cell-cell adhesion (GO:0007159); leukocyte tethering or rolling (GO:0050901); inflammatory response (GO:0006954).
- **Anatomical structures (UBERON):** Golgi apparatus (subcellular; GO:0005794, cellular component) is the actual site of the primary molecular lesion.

**Molecular Profiling.** Direct transcriptomic/proteomic/metabolomic disease-specific profiling datasets were not identified in this search (consistent with the disease's extreme rarity and the case-report nature of the literature); the principal "omics" readout used clinically and in research is targeted **glycomic analysis** (serum glycoprotein core fucosylation, neutrophil CD15a/SLeX expression by flow cytometry) rather than genome-wide expression/proteomics.

**Advanced technologies:** No single-cell, spatial transcriptomic, or CRISPR functional-genomics screens specific to LAD II were identified; functional characterization has instead relied on site-directed mutagenesis of SLC35C1 in CHO mutant cell lines to map functional transmembrane domains ([PMID:22492235](https://pubmed.ncbi.nlm.nih.gov/22492235/)).

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** hematopoietic/immune system (neutrophil dysfunction), skeletal/growth system (short stature), central nervous system (intellectual disability, seizures, cerebral atrophy), periodontium/oral cavity (severe periodontitis).
- **Secondary:** respiratory system (recurrent pneumonia), skin/soft tissue (recurrent cellulitis/skin infections), ears (otitis media), gastrointestinal tract (chronic diarrhea in some patients), eyes (keratitis in some patients).
- **Body systems involved:** immune, musculoskeletal (growth), nervous, integumentary, dental/periodontal.

**Tissue and cell level:**
- Neutrophils/granulocytes (functionally defective selectin-ligand expression) — CL:0000775.
- Vascular endothelium (the counterpart in the failed adhesion interaction) — CL:0000071.
- Erythrocytes (Bombay phenotype) — CL:0000232.
- Gingival/periodontal tissue (site of chronic inflammatory destruction).

**Subcellular level:**
- **Golgi apparatus** — the primary site of the molecular lesion (GO Cellular Component: Golgi apparatus, GO:0005794; Golgi membrane, GO:0000139), where the defective GDP-fucose transporter normally resides and functions.

**Localization:** Systemic/multi-organ rather than focal; no lateralization pattern is described.

---

## 8. Temporal Development

**Onset.** First signs typically emerge in **infancy or early childhood** — recurrent infections and growth failure are usually the presenting features ([Orphanet](https://www.orpha.net/en/disease/detail/99843)). Some growth impairment (intrauterine growth retardation) can be present prenatally/at birth.

**Onset pattern:** Insidious/chronic rather than acute, punctuated by episodes of recurrent bacterial infection.

**Progression:**
- The **immunologic/infectious phenotype tends to improve or stabilize with age**, becoming less prominent in adolescence and adulthood.
- The **neurodevelopmental and growth phenotype is persistent and often progressive/dominant** in the long term — "in adulthood, intellectual deficit and growth retardation, rather than infections, dominate the clinical picture" ([Orphanet](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?lng=EN&Expert=99843)).
- **Periodontal disease is progressive**, with cumulative alveolar bone loss and early loss of both primary and permanent dentition over childhood/adolescence.

**Disease course pattern:** Chronic, with infections occurring in a **recurrent/relapsing** pattern superimposed on a stable underlying biochemical defect; growth and cognitive impairment follow a more **stable-to-progressive** developmental trajectory rather than an episodic one.

**Duration:** Lifelong (the underlying molecular lesion is permanent), though clinical management (fucose supplementation, antimicrobial prophylaxis) can substantially modify the disease course.

**Remission patterns:** Treatment-induced clinical improvement (not cure) has been documented with oral fucose therapy — resolution of chronic skin infections and normalization of neutrophil counts/selectin ligand expression have been reported in fucose-responsive patients ([Marquardt et al. 1999, PMID:10590041](https://pubmed.ncbi.nlm.nih.gov/10590041/); [Sturla et al. 2000, PMID:10877554](https://pubmed.ncbi.nlm.nih.gov/10877554/)). No spontaneous remission is described.

**Critical periods:** Early diagnosis and initiation of fucose therapy (and neurodevelopmental support) in infancy/early childhood appears most likely to yield developmental benefit, based on the reported catch-up growth/head circumference and cognitive improvement observed with early, sustained treatment ([ScienceDirect L-fucose case report 2026](https://www.sciencedirect.com/science/article/abs/pii/S1096719226000107)).

---

## 9. Inheritance and Population

**Epidemiology.** LAD II is one of the rarest known primary immunodeficiencies/CDGs. Orphanet lists prevalence as **fewer than 10 reported cases worldwide**; a 2024 review states **19 diagnosed cases** to date ([ScienceDirect 2024](https://sciencedirect.com/science/article/pii/S1357272524000943)). No formal incidence rate has been calculated given the extremely small denominator.

**Inheritance pattern:** **Autosomal recessive.** Both parents are obligate heterozygous carriers (typically asymptomatic); each pregnancy carries a 25% recurrence risk for an affected child, 50% carrier risk, and 25% unaffected/non-carrier risk.

**Penetrance:** Appears fully penetrant for biallelic loss-of-function genotypes, though **expressivity is highly variable** (see below) — ranging from the classic severe multi-system phenotype to a milder isolated short-stature/developmental-delay presentation with little or no immune involvement.

**Expressivity:** **Variable**, genotype-correlated. The R147C founder allele produced a milder phenotype than the T308R founder allele in the original Etzioni cohort ([PMID:12116250](https://pubmed.ncbi.nlm.nih.gov/12116250/)); more recent reports of hypomorphic alleles produce an even milder "SLC35C1-CDG" phenotype (short stature/developmental delay without overt immunodeficiency) ([Tahata et al. 2022](https://onlinelibrary.wiley.com/doi/abs/10.1002/ajmg.a.62737); [JHG 2020](https://www.nature.com/articles/s10038-020-0764-4)).

**Genetic anticipation:** Not applicable/not described (not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically reported for SLC35C1/LAD II in this search.

**Founder effects:** Well documented. The **T308R** mutation is a founder allele in an Arab-Israeli population (traced to a shared great-grandmother lineage, geographically clustered within ~10 square miles) ([Etzioni et al. 2002](https://pubmed.ncbi.nlm.nih.gov/12116250/)). The **R147C** mutation was described in a Turkish-derived family. Both findings are consistent with rare-disease founder effects amplified by consanguinity.

**Consanguinity:** A recognized major risk factor — most/all early reported cases arose in consanguineous unions in Turkish and Arab-Israeli kindreds.

**Carrier frequency:** Not established in general population databases given the disease's extreme rarity; expected to be elevated locally within founder-affected consanguineous communities.

**Population demographics:**
- **Affected populations:** predominantly reported in Turkish and Arab (Israeli/Middle Eastern) kindreds, reflecting founder-effect ascertainment rather than a demonstrated broader ethnic predisposition; sporadic cases have also been reported outside these populations.
- **Geographic distribution:** Case clusters reported from Israel/Middle East and Turkey; isolated cases reported elsewhere (e.g., North America, per the Tahata et al. 2022 new-family report).
- **Sex ratio:** No sex predilection is reported (autosomal recessive inheritance).
- **Age distribution:** Diagnosis is typically made in infancy/early childhood; the surviving cohort described spans childhood through adulthood, with long-term follow-up reports available for some of the earliest-diagnosed patients.

---

## 10. Diagnostics

**Clinical Tests:**
- **Complete blood count:** marked leukocytosis with neutrophilia (WBC often 30,000–150,000/mm³), a near-universal and easily obtained first clue.
- **Flow cytometry:** demonstration of **absent or markedly reduced sialyl-Lewis X (CD15s/CD15a) expression** on neutrophils using a monoclonal antibody is the key functional immunologic test ([StatPearls NBK539770](https://www.ncbi.nlm.nih.gov/books/NBK539770/)).
- **Blood typing (ABO/H antigen typing):** essential — the **Bombay (hh) blood phenotype** is present in essentially all reported LAD II patients and is exceedingly rare in the general population, making it a strong diagnostic pointer; there is a published report of LAD II being incidentally diagnosed via ABO typing ([ScienceDirect, incidental diagnosis](https://www.sciencedirect.com/science/article/abs/pii/S1521661620307592)).
- **Serum glycoprotein core fucosylation analysis** (glycomic/biochemical assay) can demonstrate global hypofucosylation and is used to monitor treatment response to oral fucose.
- Neutrophil chemotaxis/rolling functional assays (research-level, not routine clinical) confirm the selectin-ligand defect.

**Genetic Testing:**
- **Recommended approach:** targeted **SLC35C1 single-gene sequencing** or inclusion in a primary immunodeficiency/CDG gene panel is the standard confirmatory test once the clinical/biochemical phenotype (leukocytosis, absent SLeX, Bombay phenotype) raises suspicion (commercial test listed in NCBI GTR, e.g., [Test ID 507358](https://www.ncbi.nlm.nih.gov/gtr/tests/507358/)).
- Whole-exome/whole-genome sequencing is increasingly the diagnostic route for atypical or mild presentations (e.g., isolated short stature with developmental delay) where the classic immunologic clues are absent or subtle, as illustrated by the JHG 2020 report identifying SLC35C1 variants in a short-stature/ID cohort without a primary CDG or immunodeficiency indication ([Nature/JHG 2020](https://www.nature.com/articles/s10038-020-0764-4)).
- Chromosomal microarray, karyotyping, FISH, mitochondrial DNA testing, and repeat-expansion testing are **not relevant** to LAD II diagnosis (it is a point-mutation/small-indel single-gene disorder).

**Omics-Based Diagnostics:** No standardized transcriptomic, proteomic, or liquid-biopsy diagnostic modality is used; targeted glycomics (as above) is the relevant "omics" adjunct.

**Clinical Criteria / Differential Diagnosis:** No formal consensus diagnostic-criteria statement (e.g., DSM/ICD-style) exists given the disease's rarity; diagnosis is a clinical-biochemical-genetic triad (leukocytosis + recurrent infection + growth/developmental delay, confirmed by absent SLeX/Bombay phenotype and SLC35C1 sequencing). Key differentials include:
- **LAD I** (ITGB2/CD18 deficiency) — clinically more severe infections, delayed umbilical cord separation, absent pus formation, normal growth/cognition, normal blood group; distinguished by CD18 flow cytometry and ITGB2 sequencing.
- **LAD III** (FERMT3/kindlin-3 deficiency) — LAD-like immunodeficiency plus a Glanzmann-like bleeding diathesis.
- Other congenital disorders of glycosylation (CDG-I and other CDG-II subtypes) — distinguished by transferrin isoelectric focusing pattern and specific gene panels.
- Other syndromic causes of growth failure/intellectual disability when the immunologic phenotype is mild or absent (the "mild LAD II variant" differential).

**Screening:** No population-based newborn or carrier screening program exists for LAD II given its extreme rarity; genetic counseling and targeted carrier testing are offered within affected founder-population kindreds/consanguineous families once an index case is identified.

---

## 11. Outcome/Prognosis

**Survival and Mortality:** No formal survival statistics (e.g., 5-/10-year survival rates) are available given the very small number of reported cases; published long-term follow-up reports (e.g., the JACI "long-term follow-up" report on an original index case, [JACI](https://www.jacionline.org/article/S0091-6749(98)70104-6/fulltext)) indicate that patients can survive into adulthood, particularly with modern infection management and, where applicable, fucose supplementation.

**Morbidity:**
- Infections tend to become **less frequent/severe with age**, shifting the long-term morbidity burden toward **intellectual disability, short stature, and periodontal disease/tooth loss**.
- Severe periodontitis is a major source of chronic morbidity, frequently resulting in complete or near-complete tooth loss by adolescence.
- Neurodevelopmental impairment (severe intellectual disability in the classic phenotype) is typically lifelong and is the dominant determinant of functional outcome and quality of life.

**Disease Course / Complications:**
- Recurrent bacterial infections (pneumonia, otitis media, skin/soft-tissue infection) in childhood.
- Progressive periodontal destruction.
- In the mouse model, female Slc35c1-null mice show reproductive complications (abortion, small litters, failure to nurture pups), raising the possibility of analogous reproductive/perinatal vulnerabilities, though this has not been systematically documented in human patients.

**Recovery Potential:** Not a degenerative/fatal disease in most surviving cases; the biochemical/immunologic defect can be substantially — though not completely — corrected pharmacologically with oral fucose in a subset of patients (see Treatment), improving infection frequency, growth parameters, and reportedly cognition/speech in treated individuals.

**Prognostic Factors:**
- **Genotype:** patients with milder/hypomorphic SLC35C1 alleles have a substantially better growth/cognitive prognosis than those with classic null alleles (T308R vs. R147C comparison; the emerging "mild variant" spectrum).
- **Fucose-therapy responsiveness** itself appears prognostic — patients who respond biochemically (rise in SLeX/CD15a expression, normalization of core fucosylation) tend to show the greatest clinical improvement; some genotypes (e.g., certain T308R-associated presentations) have historically shown limited or partial response.
- Early initiation of supportive/pharmacologic therapy likely improves developmental outcome, based on catch-up growth and cognitive gains reported with sustained early treatment.

**Prognostic Biomarkers:** Neutrophil CD15a/sialyl-Lewis X expression by flow cytometry and serum glycoprotein core-fucosylation level serve as both diagnostic and treatment-response/prognostic biomarkers.

---

## 12. Treatment

**Pharmacotherapy — Oral L-fucose supplementation (the central, disease-modifying therapy):**
- **Mechanism:** Exogenous dietary L-fucose is taken up and phosphorylated/converted to GDP-fucose via the cytosolic **salvage pathway**, which can supply the Golgi with GDP-fucose largely independent of the defective SLC35C1-mediated de novo route, restoring at least partial fucosylation capacity ([Yu et al. 2022, PMC9304781](https://ncbi.nlm.nih.gov/pmc/articles/PMC9304781)).
- **Foundational evidence:** Marquardt et al. (1999, *Blood* 94(12):3976–85, [PMID:10590041](https://pubmed.ncbi.nlm.nih.gov/10590041/)) — "Correction of Leukocyte Adhesion Deficiency Type II With Oral Fucose": oral fucose supplementation induced expression of fucosylated selectin ligands on neutrophils and core fucosylation of serum glycoproteins in the treated patient, with disappearance of chronic skin infections and improvement in behavior/attention span.
- Sturla et al. (2000, *Blood*, [PMID:10877554](https://pubmed.ncbi.nlm.nih.gov/10877554/)) — "Fucose supplementation in leukocyte adhesion deficiency type II" — corroborated reappearance of functional selectin ligands with normalization of neutrophil counts.
- A subsequent case (27 months of therapy) showed improvement in **speech and cognition**, CD15 expression, and core fucosylation of serum glycoproteins ([review cited via 2024 search synthesis]).
- A 2026 case report of a patient with a mono-allelic SLC35C1 variant and global hypofucosylation treated with L-fucose documented improvements in weight, head circumference, IgG normalization, and developmental catch-up ([ScienceDirect 2026](https://www.sciencedirect.com/science/article/abs/pii/S1096719226000107)).
- **Not all patients respond equally** — response appears genotype-dependent, and fucose therapy is generally regarded as beneficial but not curative.
- **NCIT term suggestion:** Pharmacotherapy (NCIT:C15986); more specifically, dietary/nutritional supplementation (NCIT:C15433, used cautiously per curation guidance to avoid over-classifying as "dietary/behavioral" when the agent is a specific chemical compound — L-fucose is better modeled as a small-molecule pharmacotherapy with `therapeutic_agent` bound to the relevant CHEBI term for L-fucose).

**Advanced/Investigational Therapeutics:**
- **AVTX-803** (Avalo Therapeutics) — an investigational oral L-fucose formulation specifically developed for LAD II, granted FDA Fast Track Designation (FTD), Orphan Drug Designation (ODD), and Rare Pediatric Disease Designation (RPDD), making it potentially eligible for a Priority Review Voucher.
  - **LADDER trial (NCT05462587):** a pivotal, 16-week, randomized, double-blind, two-period crossover withdrawal study (n=2 enrolled at initiation) assessing AVTX-803 efficacy/safety in LAD II, with the **primary endpoint being change in leukocyte sialyl-Lewis X (SLeX) antigen expression** between treatment periods. As of an April 2026 ClinicalTrials.gov verification, the (now Phase 3) study status is **RECRUITING**, with estimated primary completion **November 30, 2026** ([Mayo Clinic trial listing](https://www.mayo.edu/research/clinical-trials/cls-20531379); [BioSpace press release](https://www.biospace.com/avalo-therapeutics-announces-first-patient-dosed-in-the-avtx-803-pivotal-trial-ladder-for-the-treatment-of-leukocyte-adhesion-deficiency-type-ii-lad-ii-topline-pivotal-trial-results-expected-1h2023)).
  - **Extension study (NCT05754450):** assessing long-term safety/efficacy of AVTX-803.
  - An earlier related trial, **NCT03354533** ("Study of ORL-1F [L-fucose] in Patients With Leukocyte Adhesion Deficiency Type II"), was a completed Phase 1/2 study of an L-fucose formulation ([ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT03354533)).
  - This represents the most significant recent (2023–2026) translational development in LAD II — movement from off-label compassionate oral fucose use toward a regulatory-track, purpose-built oral fucose drug product with a pivotal registrational trial actively recruiting as of 2026.

**Surgical/Interventional:** No disease-specific surgical intervention; periodontal surgical management may be attempted for severe periodontitis but is often "recalcitrant to treatment," per the periodontal literature.

**Supportive Care:**
- Aggressive antimicrobial prophylaxis/treatment of recurrent bacterial infections (NCIT:C15747, Supportive Care; consider antibiotic pharmacotherapy, NCIT:C15986).
- Intensive dental/periodontal care and monitoring (NCIT category: dental/oral healthcare procedures) given the near-universal severe periodontal disease.
- Nutritional support for growth failure/failure to thrive.

**Rehabilitative:** Developmental/early intervention services, physical/occupational/speech therapy for psychomotor and cognitive delay (NCIT:C15302 Physical Therapy; NCIT:C159273 Speech Therapy; NCIT:C121351 Occupational Therapy), particularly given reported cognitive gains coincident with fucose therapy.

**Experimental:** Beyond AVTX-803, no gene therapy, cell therapy, or RNA-based therapeutic approach specific to LAD II was identified in this search (contrast with LAD I, for which a lentiviral gene therapy trial, RP-L201, is registered as NCT03825783).

**Treatment Outcomes:**
- Response rates to oral fucose are not formally quantified across a large cohort (reflecting the very small total patient population) but are reported as clinically meaningful in multiple case reports, with biochemical (SLeX/CD15a, core fucosylation) and clinical (infection frequency, growth, cognition/speech) endpoints improving in responders.
- Side effects/adverse events specific to oral fucose supplementation were not detailed in the sources reviewed here beyond general tolerability implied by long-term (multi-year) use in case reports.

**Treatment Strategy:** Standard-of-care as currently practiced: **"a trial of fucose supplementation is recommended in all patients diagnosed with LAD II"** ([StatPearls NBK539770](https://www.ncbi.nlm.nih.gov/books/NBK539770/)), combined with proactive infection management, periodontal care, and developmental support — essentially monotherapy (fucose) plus multidisciplinary supportive care, rather than combination pharmacotherapy.

**Personalized Medicine:** Given genotype-phenotype correlation and genotype-dependent treatment responsiveness, SLC35C1 variant characterization (and functional assay of residual transporter activity where available) is increasingly relevant to anticipating both disease severity and likely response to fucose-based therapy — an emerging precision-medicine dimension for this ultra-rare disease.

---

## 13. Prevention

**Primary Prevention:** Not applicable in the population-based sense (no vaccination or modifiable risk-factor strategy prevents this monogenic recessive disorder). The only relevant "primary prevention" lever is **reproductive/genetic**: carrier screening and genetic counseling in known founder/consanguineous populations, and prenatal or preimplantation genetic testing for at-risk couples once a familial SLC35C1 pathogenic variant is identified.

**Secondary Prevention:** Early clinical recognition (leukocytosis + recurrent infection + growth delay triad) followed by prompt diagnostic confirmation (flow cytometry for SLeX, Bombay blood typing, SLC35C1 sequencing) allows earlier initiation of fucose therapy and infection-prevention measures — the closest analog to "secondary prevention" for this disorder, aimed at limiting downstream developmental and periodontal morbidity.

**Tertiary Prevention:** Ongoing antimicrobial prophylaxis, structured dental/periodontal surveillance and intervention, and developmental therapies to limit the functional impact of established intellectual disability and periodontal disease.

**Immunization:** No disease-specific vaccine strategy; standard childhood immunizations are presumably still indicated (not contraindicated), though no specific guidance was identified in this search.

**Screening and Early Detection:**
- No population-based newborn screening program for LAD II exists.
- **Genetic/carrier screening** within known founder-mutation communities (e.g., specific Arab-Israeli and Turkish kindreds carrying T308R/R147C) is the most relevant targeted screening strategy, alongside cascade testing of relatives of an index case.
- **Risk stratification:** essentially pedigree-based (consanguinity, known carrier status) rather than population risk-score based.

**Behavioral Interventions:** Not applicable (no lifestyle-modifiable risk factor).

**Counseling:** **Genetic counseling** is central given autosomal recessive inheritance, especially in consanguineous/founder populations, covering recurrence risk (25% per pregnancy for carrier couples), carrier testing of relatives, and reproductive options (prenatal diagnosis, preimplantation genetic testing) once the familial pathogenic variant(s) are known.

**Public Health / Environmental Interventions:** Not applicable — there is no environmental exposure to mitigate.

**Prophylaxis:** Ongoing infection prophylaxis (e.g., antibiotic prophylaxis in high-risk periods) is a reasonable clinical practice extrapolated from general immunodeficiency management, though no LAD II-specific prophylactic regimen/guideline was identified in this search.

---

## 14. Other Species / Natural Disease

**Taxonomy:** No naturally occurring LAD II has been reported in non-human species (companion animals, livestock, or wildlife) in the sources reviewed. This contrasts with LAD I, which has recognized naturally occurring bovine (BLAD, bovine leukocyte adhesion deficiency) and canine analogs.

**Gene orthology:** Slc35c1 is conserved across model organisms — mouse (MGI:2443301, *Slc35c1*), zebrafish (ZFIN: slc35c1, ZDB-GENE-041212-11), rat (RGD:1309463), and others — but no report of spontaneous/natural LAD II-like disease in these species was found; all animal data derive from engineered knockout models (see Section 15).

**Comparative Biology:** The core molecular mechanism (Golgi GDP-fucose transport supporting selectin-ligand fucosylation and leukocyte rolling) is evolutionarily conserved, as demonstrated by the concordant phenotype (leukocytosis, defective selectin-dependent rolling/adhesion) in the engineered mouse knockout, supporting cross-species conservation of the pathway even though the disease itself is human-specific/engineered rather than naturally occurring elsewhere.

**Transmission/Zoonotic potential:** Not applicable — LAD II is a non-communicable, purely genetic disorder with no zoonotic or cross-species transmission dimension.

---

## 15. Model Organisms

**Model Type:** Mammalian, genetically engineered (knockout).

**Primary model — Slc35c1-knockout mouse:**
- Reported in Blood 112(4):1472 (2008), "Leukocyte trafficking in a mouse model for leukocyte adhesion deficiency II/congenital disorder of glycosylation IIc" ([ASH Publications](https://ashpublications.org/blood/article/112/4/1472/25356/)).
- **Genetic model type:** constitutive knockout (Slc35c1−/−).
- **Phenotype recapitulation:**
  - Approximately half of surviving knockout mice were fertile; pregnant knockout females uniformly aborted or had very small litters and failed to nurture pups — a reproductive phenotype **not** systematically described in human LAD II patients, representing a potential model-specific or under-ascertained feature.
  - **Prominent leukocytosis** driven primarily by a ~5-fold increase in circulating neutrophils — directly recapitulates the hallmark human laboratory finding.
  - **E-, L-, and P-selectin–dependent leukocyte rolling in cremaster muscle venules was virtually absent**, with a strong (though incomplete) decrease in firm leukocyte adhesion — faithfully recapitulates the human selectin-ligand defect mechanism.
  - **Neutrophil migration to the inflamed peritoneum was reduced by 89%**, modeling the human recurrent-infection susceptibility mechanistically.
  - **Lymphocyte homing to lymph nodes was reduced to 1–2% of normal**, but **homing to the spleen was completely normal** — this dissociation is proposed to explain why LAD II patients do not show the profound lymphocyte-trafficking defects that might otherwise be predicted, i.e., a partial/tissue-selective recapitulation that helps explain a milder-than-expected component of the human phenotype.
- **Model limitations:** the mouse model's reproductive/fertility phenotype (abortion, failure to nurture pups) has no clearly documented human correlate in the literature reviewed, and the degree of neurodevelopmental/growth phenotype recapitulation in the mouse was not detailed in the sources retrieved here — suggesting the mouse model may be most robust for the immunologic/selectin-trafficking axis of the disease rather than the growth/CNS axis.
- **Research applications:** in vivo dissection of selectin-ligand biology, leukocyte rolling/adhesion dynamics, and testing of fucose-repletion strategies at the mechanistic level.

**Other model systems:** No Drosophila, C. elegans, zebrafish, or iPSC-based disease models specific to LAD II/SLC35C1 loss were identified in this search (zebrafish and other species carry an annotated slc35c1 ortholog per model-organism databases, but no disease-modeling publication using these orthologs was retrieved).

**Cellular/functional models:** CHO (Chinese hamster ovary) mutant cell lines lacking functional GDP-fucose transport have been used as an **in vitro functional model** to map SLC35C1 structure-function relationships (transmembrane domain mutagenesis) rather than to model organismal disease per se ([PMID:22492235](https://pubmed.ncbi.nlm.nih.gov/22492235/)).

**Resources:** MGI (Slc35c1, MGI:2443301) for the mouse gene/allele records; no dedicated LAD II model-organism repository or IMPC/KOMP-specific disease-model resource was identified beyond standard gene-centric databases.

---

## Summary of Suggested Ontology Term Bindings for KB Curation

| Category | Term |
|---|---|
| Disease (MONDO) | Not confirmed in this search — recommend verifying directly via the MONDO/OxO API before binding (search results did not surface a definitive MONDO CURIE for LAD II specifically, only for LAD I, MONDO:0007293) |
| OMIM phenotype | 266265 |
| OMIM gene | 605881 |
| Orphanet | ORPHA:99843 |
| HGNC gene | HGNC:20197 (SLC35C1) |
| GO Molecular Function | GO:0005457 (GDP-fucose transmembrane transporter activity) |
| GO Biological Process | GO:0036065 (fucosylation); GO:0050901 (leukocyte tethering or rolling); GO:0007159 (leukocyte cell-cell adhesion) |
| GO Cellular Component | GO:0005794 (Golgi apparatus) |
| CL | CL:0000775 (neutrophil); CL:0000071 (blood vessel endothelial cell); CL:0000232 (erythrocyte) |
| HP (representative) | HP:0001974 (Leukocytosis); HP:0011897 (Neutrophilia); HP:0002718 (Recurrent bacterial infections); HP:0004322 (Short stature); HP:0001511 (Intrauterine growth retardation); HP:0010864 (Severe intellectual disability); HP:0005280 (Depressed nasal bridge); HP:0000704 (Periodontitis); HP:0001250 (Seizure) |
| NCIT (treatment) | NCIT:C15986 (Pharmacotherapy) with `therapeutic_agent` bound to L-fucose (verify exact CHEBI CURIE before binding); NCIT:C15747 (Supportive Care) |
| Clinical trials | NCT05462587 (AVTX-803 LADDER, pivotal, recruiting as of 2026); NCT05754450 (AVTX-803 extension); NCT03354533 (ORL-1F, completed) |

**Note on ontology terms:** the GO/CL/HP identifiers above are provided as strong candidate bindings based on standard, well-established ontology term meanings for these concepts, but per this repository's term-validation contract (`dismech-terms` skill), each should still be run through `just validate-terms`/OAK lookup before being committed to a KB entry, since this research pass did not itself query OAK/OLS directly.

---

### Sources

- [OMIM #266265 — Congenital Disorder of Glycosylation, Type IIc](https://omim.org/entry/266265)
- [OMIM *605881 — SLC35C1](https://omim.org/entry/605881)
- [Orphanet: Leukocyte adhesion deficiency type II (ORPHA:99843)](https://www.orpha.net/en/disease/detail/99843)
- [Wikipedia: Congenital disorder of glycosylation type IIc](https://en.wikipedia.org/wiki/Congenital_disorder_of_glycosylation_type_IIc)
- [NORD: Leukocyte Adhesion Deficiency Syndromes](https://rarediseases.org/rare-diseases/leukocyte-adhesion-deficiency-syndromes/)
- [GARD: Leukocyte adhesion deficiency type II](https://rarediseases.info.nih.gov/diseases/4634/leukocyte-adhesion-deficiency-type-ii/)
- [StatPearls: Leukocyte Adhesion Deficiency (NBK539770)](https://www.ncbi.nlm.nih.gov/books/NBK539770/)
- [Lübke et al. 2001, Nature Genetics — gene identification, PMID:11326279](https://pubmed.ncbi.nlm.nih.gov/11326279/)
- [Etzioni et al. 2002, Am J Med Genet — founder effect/genotype-phenotype, PMID:12116250](https://pubmed.ncbi.nlm.nih.gov/12116250/)
- [Marquardt et al. 1999, Blood — Correction of LAD II with Oral Fucose, PMID:10590041](https://pubmed.ncbi.nlm.nih.gov/10590041/)
- [Sturla et al. 2000, Blood — Fucose supplementation in LAD II, PMID:10877554](https://pubmed.ncbi.nlm.nih.gov/10877554/)
- [Tahata et al. 2022, AJMG-A — mild variant and l-fucose therapy](https://onlinelibrary.wiley.com/doi/abs/10.1002/ajmg.a.62737)
- [Congenital disorder of fucosylation type 2c presenting with short stature and minimal adhesion defect, PMID:24403049](https://pubmed.ncbi.nlm.nih.gov/24403049/)
- [Biallelic SLC35C1 variants and isolated short stature/ID, J Hum Genet 2020](https://www.nature.com/articles/s10038-020-0764-4)
- [Mutations in SLC35C1 and fucosylation pattern diversity, 2024, ScienceDirect](https://sciencedirect.com/science/article/pii/S1357272524000943)
- [Yu et al. 2022, J Biol Chem — fucose salvage pathway independent of SLC35C1, PMC9304781](https://ncbi.nlm.nih.gov/pmc/articles/PMC9304781)
- [In vivo evidence for GDP-fucose transport absent SLC35C1/SLC35C2, 2023, PMC10709068](https://pmc.ncbi.nlm.nih.gov/articles/PMC10709068/)
- [Leukocyte trafficking in Slc35c1-deficient mouse model, Blood 112(4):1472](https://ashpublications.org/blood/article/112/4/1472/25356/)
- [LAD II patients with dual GDP-fucose transporter defect, Blood 107(10):3959](https://ashpublications.org/blood/article/107/10/3959/109832/)
- [Identification of functional elements of SLC35C1 in CHO mutant, PMID:22492235](https://pubmed.ncbi.nlm.nih.gov/22492235/)
- [GeneCards: SLC35C1](https://www.genecards.org/cgi-bin/carddisp.pl?gene=SLC35C1)
- [Incidental diagnosis of LAD II via ABO typing, ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1521661620307592)
- [Avalo Therapeutics AVTX-803 LADDER pivotal trial press release](https://www.biospace.com/avalo-therapeutics-announces-first-patient-dosed-in-the-avtx-803-pivotal-trial-ladder-for-the-treatment-of-leukocyte-adhesion-deficiency-type-ii-lad-ii-topline-pivotal-trial-results-expected-1h2023)
- [ClinicalTrials.gov: A Study to Evaluate Efficacy and Safety of AVTX-803 (NCT05462587)](https://clinicaltrials.gov/study/NCT05462587)
- [ClinicalTrials.gov: AVTX-803 Extension Study (NCT05754450)](https://clinicaltrials.gov/study/NCT05754450)
- [ClinicalTrials.gov: Study of ORL-1F (L-fucose) (NCT03354533)](https://clinicaltrials.gov/study/NCT03354533)
- [Mayo Clinic AVTX-803 trial listing](https://www.mayo.edu/research/clinical-trials/cls-20531379)
- [L-fucose supplementation in mono-allelic SLC35C1 variant patient, 2026, ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1096719226000107)
- [PLOS Pathogens: Subgingival Microbial Communities in Leukocyte Adhesion Deficiency](https://journals.plos.org/plospathogens/article?id=10.1371%2Fjournal.ppat.1004698)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.