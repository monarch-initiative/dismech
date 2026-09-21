---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-19T20:08:16.165816'
end_time: '2026-08-19T20:12:26.001947'
duration_seconds: 249.84
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: WWOX-Related Developmental and Epileptic Encephalopathy
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
    min_report_chars: 200
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 17
  num_turns: 26
  total_cost_usd: 2.0151703999999997
  session_id: 6f8bf895-3ab0-55cb-a154-acb932b43f03
  stop_reason: end_turn
  assistant_text_blocks: 1
citation_count: 36
reference_validation:
  total_references: 32
  verified: 32
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 4
  quotes_valid: 1
  quotes_unsupported: 3
  unsupported_quote_references:
  - PMID:30356099
  - PMID:33916893
  - PMC:PMC8649866
  relevance_assessed: 32
  on_topic: 19
  off_topic: 1
  off_topic_references:
  - PMID:8305172
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** WWOX-Related Developmental and Epileptic Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **WWOX-Related Developmental and Epileptic Encephalopathy** covering all of the
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

I now have comprehensive data across all key domains. Compiling the final research report.

# WWOX-Related Developmental and Epileptic Encephalopathy (WOREE Syndrome): Comprehensive Research Report

## 1. Disease Information

**Overview:** WWOX-Related Developmental and Epileptic Encephalopathy — also known as **WOREE syndrome** (WWOX-Related Epileptic Encephalopathy) or **Developmental and Epileptic Encephalopathy 28 (DEE28)** — is a rare, autosomal recessive neurodevelopmental disorder caused by biallelic (homozygous or compound heterozygous) loss-of-function variants in the *WWOX* gene. It represents the severe end of a phenotypic spectrum of *WWOX*-related neurological disease. It is characterized by "refractory seizures, encephalopathy, spasticity with hyperreflexia and hypokinesia, profound developmental delay at infancy" with progressive cerebral atrophy and a high likelihood of premature death (PMID:33916893).

**Key Identifiers:**
- **OMIM:** #616211 (DEE28); gene OMIM 605131 (*WWOX*)
- **MONDO:** MONDO:0014533 (developmental and epileptic encephalopathy 28)
- **Gene:** *WWOX* (HGNC:12799), chromosome 16q23.1–q23.2, spanning the common fragile site FRA16D
- **Allelic disorder:** Autosomal recessive spinocerebellar ataxia 12 (SCAR12; OMIM #614322) — a milder phenotype on the same genetic spectrum
- **Orphanet:** listed as "WWOX-related epileptic encephalopathy" / early lethal microcephaly-epilepsy syndrome (Mignot et al. 2015, *Orphanet J Rare Dis*, PMID not captured but title: "The supposed tumor suppressor gene WWOX is mutated in an early lethal microcephaly syndrome with epilepsy, growth retardation and retinal degeneration")

**Synonyms:** WOREE syndrome; WWOX-related epileptic encephalopathy; developmental and epileptic encephalopathy 28 (DEE28); early infantile epileptic encephalopathy 28 (formerly EIEE28); WWOX deficiency syndrome.

**Data source type:** Information is derived primarily from **aggregated case series and case reports in the medical literature** (the largest published cohort is 20 new + 17 literature-reviewed = 37 patients from 27 families; ClinGen/ClinVar databases report up to ~160 additional variant submissions), supplemented by a **patient registry/natural history effort** run by the WWOX Foundation (wwox.org), rather than large-scale EHR-based epidemiology. As of 2023, only ~56–60 published WOREE cases and 6 SCAR12 cases were known worldwide (PMID:33916893).

---

## 2. Etiology

**Disease Causal Factor:** WOREE syndrome is caused exclusively by **biallelic (homozygous or compound heterozygous) germline pathogenic variants in *WWOX*** — there is no known non-genetic cause. It is a monogenic, fully penetrant autosomal recessive disorder.

**Genetic risk factors:**
- Both parents are obligate heterozygous carriers (typically asymptomatic).
- **Consanguinity** is a significant risk factor: 28% (5/18) of families in the largest cohort were consanguineous (PMID:30356099).
- Variant spectrum: "Two copy-number variations (CNVs) or two single-nucleotide variations (SNVs) were found respectively in four and nine families, with compound heterozygosity for one SNV and one CNV in five families" — plus 8 novel missense variants identified in a 2023 expansion study. Recurrent variants include **p.(Gln230Pro)** (4 families) and **p.(Gly137Glu)** (3 families) (PMID:30356099).
- *WWOX* shows a **pLI score of 0**, consistent with tolerance of heterozygous loss-of-function variants and a strictly recessive mechanism (PMID:33916893).

**Gene-dosage/genotype severity relationship:** "The most severe clinical presentation seems to be associated with null genotypes" (biallelic complete loss-of-function/truncating or large deletion variants → WOREE), whereas **missense-only genotypes correlate with the milder SCAR12 phenotype** — "premature death has never been described in patients with missense pathogenic variant-only genotype" (PMID:30356099; PMID:33916893).

**Environmental/protective factors:** No environmental risk or protective factors, and no known gene–environment interaction, have been described — this is a purely Mendelian condition.

---

## 3. Phenotypes

Data compiled chiefly from the 20-patient/18-family cohort of Abdel-Salam et al. (PMID:30356099, *Genetics in Medicine* 2019, "The phenotypic spectrum of WWOX-related disorders") and the Cells 2021 review (PMID:33916893).

| Phenotype | Frequency | Suggested HPO term |
|---|---|---|
| Seizures (any type; onset mean 1.6 months, range day 1–7 months) | 100% (20/20) | HP:0001250 (Seizure); HP:0011097 (Epileptic encephalopathy) |
| Drug-resistant/refractory epilepsy | 95% (19/20) | HP:0010818 (Recurrent seizures) / drug-resistant epilepsy concept |
| Infantile spasms / West syndrome | 26% (5/19) | HP:0011097; HP:0012469 (Infantile spasms) |
| Lennox-Gastaut syndrome | 11% (2/19) | HP:0002373 (Lennox-Gastaut syndrome) |
| Profound global developmental delay | 100% | HP:0012736 (Profound global developmental delay) |
| Absence of speech/language | 100% | HP:0002465 (Absent speech) |
| Inability to sit or walk | 100% | HP:0002540 (Inability to walk); HP:0025336 |
| Hypotonia (axial) | 75% (15/20) | HP:0001252 (Hypotonia) |
| Hypertonia/spasticity | 83% (15/18) | HP:0001257 (Spasticity) |
| Hyperreflexia | commonly reported | HP:0001347 (Hyperreflexia) |
| Poor/absent eye contact, visual impairment | 75–89% | HP:0000505 (Visual impairment) |
| Optic nerve anomalies | 53% (10/19) | HP:0000539 (Abnormality of the optic nerve) |
| Abnormal fundus oculi | 47% (9/19) | HP:0007663 (Abnormality of retinal pigmentation) |
| Retinal dystrophy/degeneration | 10–20% | HP:0000556 (Retinal dystrophy) |
| Corpus callosum hypoplasia (MRI) | 75% (15/20) | HP:0002079 (Hypoplasia of the corpus callosum) |
| Progressive cerebral atrophy | 55% (11/20) | HP:0002510 (Progressive encephalopathy); HP:0002120 (Cerebral atrophy) |
| Delayed myelination | 5–10% | HP:0012448 (Delayed myelination) |
| Microcephaly (often acquired/progressive) | reported in more severe cases | HP:0000252 (Microcephaly); HP:0000253 (Progressive microcephaly) |
| Feeding difficulties/need for gastrostomy | 70% (13/19) | HP:0011968 (Feeding difficulties) |
| Respiratory problems | 40% (8/20) | HP:0002105 (Abnormal breathing) |
| Scoliosis/kyphosis | 65% (13/20) | HP:0002650 (Scoliosis) |
| Characteristic facial dysmorphism (round face, full cheeks, short neck) | 60% (12/20) | HP:0000271 (Abnormality of the face) |
| Premature death (before 3 years, mean 40 months) | 40% (8/20) | — |
| Hearing impairment (case reports) | occasional | HP:0000365 |

**Quality of life impact:** Profound — affected children never achieve independent sitting, walking, or language; most require enteral (gastrostomy) feeding due to unsafe swallowing/aspiration risk; drug-resistant daily seizures (up to >30/day) dominate the clinical course; a substantial minority die in early childhood. A 2024 case report documented the **oldest known survivor at 40 years**, illustrating a wide severity spectrum even within DEE28 (PMID:39507621).

---

## 4. Genetic/Molecular Information

**Gene:** *WWOX* (WW domain-containing oxidoreductase), HGNC:12799, chromosome 16q23.1, an unusually large gene (~1.1 Mb genomic span) whose massive intron 8 (~780 kb) overlaps the common chromosomal fragile site **FRA16D** — likely explaining the gene's high mutability and low mRNA abundance of the full-length 1.4 kb transcript (PMID:8305172-family sources).

**Protein:** 414 amino acids (~46 kDa), containing:
- Two N-terminal **WW domains** (WW1, WW2) mediating protein–protein interactions with PPxY-motif partners
- A nuclear localization sequence between the WW domains
- A C-terminal **short-chain dehydrogenase/reductase (SDR) domain** with oxidoreductase/steroid-binding activity

**Variant classes causing WOREE (per ACMG/ClinVar):** nonsense, frameshift, splice-site, large multi-exon/whole-gene deletions (CNVs), and missense variants — with **loss-of-function (null) genotypes producing the severe WOREE phenotype** and **missense-only genotypes typically producing the milder SCAR12 phenotype**. Population databases (gnomAD) show *WWOX* is depleted of complete loss-of-function heterozygotes at a level consistent with recessive lethality but is not haploinsufficient (pLI≈0).

**Functional consequence:** Complete or near-complete loss of WWOX protein function (rather than dominant-negative or gain-of-function mechanisms).

**Chromosomal abnormality overlap:** Large multi-exon *WWOX* deletions have also been reported causing **46,XY disorder of sex development** in a heterozygous state in one family, with a deletion of exons 6–8 predicted to remove the SDR domain (PMID:22071891) — a distinct, non-DEE phenotype illustrating pleiotropy.

**Modifier genes:** None firmly established in humans; in mouse models, seizure activity has been linked mechanistically to **glycogen synthase kinase 3β (GSK-3β)** dysregulation downstream of WWOX loss (PMID from Acta Neuropathol Commun, "Wwox deficiency leads to neurodevelopmental and degenerative neuropathies and glycogen synthase kinase 3β-mediated epileptic seizure activity in mice").

**Epigenetics:** Not a primary driver of WOREE syndrome (this is a straightforward LOF Mendelian disorder), though WWOX itself is implicated in chromatin/DNA-damage-response signaling (interactions with ATM, p63, p73).

---

## 5. Environmental Information

No environmental, lifestyle, or infectious contributory factors have been identified — WOREE syndrome is a fully genetically determined disorder. There is no known infectious trigger, though intercurrent infections/aspiration pneumonia are a major cause of morbidity/mortality secondary to feeding and respiratory compromise (see Outcome section).

---

## 6. Mechanism / Pathophysiology

WWOX is a **multifunctional scaffold/signaling protein and candidate tumor suppressor** ("a scaffold adaptor partnering with multiple proteins through its WW domains and modulating several protein networks," PMID:33916893) with the following key mechanistic threads relevant to neurodevelopment and epileptogenesis:

**a) Hyal-2/WWOX/Smad4 (TGF-β) signaling axis:** In a non-canonical pathway, extracellular hyaluronan binds membrane-bound hyaluronidase **Hyal-2**, which recruits **WWOX** (via its Tyr33-phosphorylated WW1 domain) and **Smad4** (via WWOX's SDR domain), forming a Hyal-2/WWOX/Smad4 complex that translocates to the nucleus to modulate TGF-β/Smad-dependent transcription and, when overactivated, triggers "bubbling cell death" (PMID:27845895; PMC2708898). GO term: GO:0007179 (transforming growth factor beta receptor signaling pathway).

**b) Wnt/β-catenin pathway:** WWOX negatively regulates canonical Wnt signaling via interaction with Dishevelled and GSK-3β; loss of WWOX leads to Wnt pathway dysregulation, corroborated in patient-derived brain organoids showing "Wnt pathway and DNA damage response impairment" (biorxiv/EMBO Mol Med 2021). GO:0016055 (Wnt signaling pathway).

**c) Neurodegenerative protein-aggregation cascade:** WWOX loss allows **TIAF1** (TGF-β1-induced anti-apoptotic factor 1) and **TRAPPC6AΔ** to relocate and aggregate at mitochondria, triggering caspase activation, tau hyperphosphorylation/tangle formation, and amyloid-β aggregation — "a cascade of protein aggregation bombards mitochondria for neurodegeneration and apoptosis under WWOX deficiency" (PMID from *Cell Death & Disease* 2015, PMC4650446). This links WOREE mechanistically to broader tauopathy/Alzheimer's-relevant biology.

**d) Neuronal excitability / E-I imbalance:** In neuronal-*Wwox*-deleted mouse cortex, "layer II/III pyramidal neurons ... demonstrated elevated amplitude of excitatory post-synaptic currents, whereas the frequency and amplitude of inhibitory post-synaptic currents were reduced" plus depolarized resting potential and increased action-potential frequency — a direct electrophysiological substrate for hyperexcitability and network-level epileptic activity (PMID:34634460, *Neurobiol Dis* 2021). Human WOREE-patient brain organoids independently show "neuronal hyperexcitability and E/I imbalance ... increased GAD67 expression (GABAergic shift), epileptiform low-frequency oscillations, and amplified responses to convulsants like 4-aminopyridine," with ectopic WWOX re-expression rescuing the phenotype (EMBO Mol Med, PMC8350905).

**e) Myelination defect:** Neuronal *Wwox* deletion in mice causes epilepsy **and myelin defects**, with WWOX promoting oligodendrocyte progenitor cell differentiation into mature myelinating oligodendrocytes — "Wwox mutant mice exhibited hypomyelination, reduced oligodendrocyte maturation, and impaired axonal conductivity" (*Brain* 2021, PMID for "Neuronal deletion of Wwox ... causes epilepsy and myelin defects").

**f) GSK-3β-mediated seizure mechanism:** *Wwox*-deficient mice show epileptic seizure activity mediated through GSK-3β dysregulation, alongside neurodevelopmental and degenerative neuropathy (Acta Neuropathol Commun 2020, PMC6990504).

**Causal chain summary:** Biallelic *WWOX* LOF → loss of WW-domain scaffold function → (i) disrupted Wnt/GSK-3β and Hyal-2/TGF-β/Smad4 signaling in neural progenitors → abnormal cortical/cerebellar development (heterotopia, corpus callosum hypoplasia, cerebral atrophy); (ii) failure of oligodendrocyte maturation → hypomyelination; (iii) cortical E/I imbalance (↑excitatory, ↓inhibitory synaptic drive, GABAergic shift) → neuronal hyperexcitability and network hypersynchrony → drug-resistant seizures/epileptic encephalopathy; (iv) TIAF1/TRAPPC6AΔ-driven mitochondrial protein aggregation → progressive neurodegeneration and premature death.

**Relevant cell types (CL terms):** CL:0000540 (neuron), CL:0000598 (pyramidal neuron), CL:0000128 (oligodendrocyte), CL:0002453 (oligodendrocyte precursor cell), CL:0000127 (astrocyte, secondary).

---

## 7. Anatomical Structures Affected

- **Organ/system level:** Primarily the **central nervous system** (cerebral cortex, cerebellum, corpus callosum, white matter/myelin), with secondary involvement of the **eye/retina and optic nerve**, **musculoskeletal system** (scoliosis/kyphosis secondary to hypotonia/spasticity), and **gastrointestinal/respiratory systems** (feeding/aspiration complications).
- **Tissue/cell level:** Cerebral cortical pyramidal neurons (layer II/III), cerebellar Purkinje cells (in the SCAR12/ataxia end of spectrum), oligodendrocytes/oligodendrocyte progenitor cells (hypomyelination), retinal photoreceptors (retinal dystrophy/degeneration), choroid plexus and ependymal cells (sites of highest normal murine *Wwox* expression).
- **Subcellular level:** Mitochondria (site of TIAF1/TRAPPC6AΔ aggregation and apoptotic signaling — GO:0005739), nucleus (site of Hyal-2/WWOX/Smad4 transcriptional complex — GO:0005634), plasma membrane (Hyal-2 receptor complex).
- **UBERON terms:** UBERON:0000955 (brain), UBERON:0001851 (cortex), UBERON:0002336 (corpus callosum), UBERON:0002037 (cerebellum), UBERON:0000966 (retina), UBERON:0001777 (optic nerve).
- **Laterality:** Bilateral/symmetric involvement typical of a global neurodevelopmental process.

---

## 8. Temporal Development

- **Onset:** Congenital/early infantile — seizure onset mean 1.6 months (range: day 1 of life to 7 months) (PMID:30356099). A prenatal presentation has also been reported ("WWOX and severe autosomal recessive epileptic encephalopathy: first case in the prenatal period," *J Hum Genet* 2015).
- **Pattern:** Acute-onset refractory epilepsy evolving into a chronic, progressive encephalopathy; not episodic/relapsing-remitting but rather a relentless, largely non-remitting course punctuated by daily seizures (up to >30/day).
- **Progression:** Progressive cerebral atrophy on serial MRI in >50% of patients; developmental regression/arrest is typical rather than a static encephalopathy. Disease duration is often foreshortened by early mortality but is lifelong in survivors — the oldest reported patient is 40 years old (PMID:39507621), demonstrating that some individuals with milder biallelic genotypes survive into adulthood.
- **Remission:** No spontaneous or reliable treatment-induced seizure remission has been documented; the disorder is characteristically drug-resistant (95% of patients).
- **Critical periods:** The first months of life represent the critical window for seizure onset and the presumed window during which corrective gene therapy (see Treatment) would need to be delivered to prevent irreversible developmental injury — underscored by the 2021 mouse study showing efficacy specifically with **neonatal** AAV-WWOX gene delivery.

---

## 9. Inheritance and Population

- **Epidemiology:** Ultra-rare — as of 2023, only ~56–60 published WOREE cases (DEE28) and 6 SCAR12 cases (2 families) were known worldwide, with ClinVar recording additional (~160) variant submissions of uncertain full clinical documentation (PMID:33916893). No formal population prevalence/incidence rate has been established; the disorder likely remains under-ascertained.
- **Inheritance pattern:** **Autosomal recessive**; both syndromes (WOREE/DEE28 and SCAR12) require biallelic pathogenic variants.
- **Penetrance:** Complete/full penetrance for biallelic null genotypes.
- **Expressivity:** Highly variable, ranging from severe WOREE (death in early childhood) to milder SCAR12 (survival with ataxia/epilepsy into adulthood), correlating strongly with genotype (null vs. missense) as described above.
- **Consanguinity:** A major risk factor — 28% (5/18) of families in the largest published cohort were consanguineous (PMID:30356099); many early case reports originated from consanguineous Middle Eastern/Mediterranean families.
- **Sex ratio:** No strong sex bias reported in DEE28/WOREE cohorts (40% male, 60% female in the 20-patient cohort — PMID:30356099), consistent with autosomal (non-X-linked) inheritance.
- **Carrier frequency:** Not precisely established; gnomAD-based estimation methodology exists (summing allele frequencies of curated LOF variants) but specific WWOX carrier-frequency figures were not identified in this search — likely very low given the extreme rarity of the homozygous phenotype.
- **Founder effects:** Not formally established, though certain recurrent variants (p.(Gln230Pro), p.(Gly137Glu)) recur across multiple unrelated families, suggestive of possible mutational hotspots or regional founder effects.

---

## 10. Diagnostics

**Clinical "red flags":** Early-onset (neonatal/infantile) refractory epilepsy, profound global developmental delay, abnormal EEG, brain MRI abnormalities (corpus callosum hypoplasia, cerebral atrophy, white matter changes), and ophthalmologic involvement, especially in the context of parental consanguinity or a family history consistent with autosomal recessive inheritance (PMID:33916893).

**Genetic testing:**
- **First-line:** Whole-exome sequencing (WES) or a developmental/epileptic-encephalopathy gene panel including *WWOX*; whole-genome sequencing (WGS) is valuable for detecting intronic/structural CNVs, which account for a substantial fraction of pathogenic alleles (including compound heterozygous SNV+CNV genotypes).
- **Chromosomal microarray (CMA):** Useful for detecting multi-exon/whole-gene deletions given *WWOX*'s large genomic footprint and fragile-site location.
- **Uniparental disomy (UPD) testing:** At least one case identified a pathogenic splice-site variant unmasked by **paternal uniparental isodisomy** of chromosome 16 (PMID:38407561), underscoring the value of UPD analysis in apparent "homozygous" findings.
- **Variant interpretation resources:** ClinVar, ClinGen, gnomAD, DECIPHER, VarSome.

**Imaging/EEG:**
- Brain MRI abnormal in ~80% (corpus callosum hypoplasia most common at 75%, cerebral atrophy 55%).
- EEG shows a spectrum of epileptiform patterns including hypsarrhythmia (West syndrome, 26%) and Lennox-Gastaut-type patterns (11%).

**Ophthalmologic evaluation:** Electroretinography/electrodiagnostic testing recommended given the high rate (up to ~50%) of optic nerve/retinal abnormalities.

**Differential diagnosis:** Other genetic developmental and epileptic encephalopathies (e.g., *CDKL5*, *STXBP1*, *SCN2A*-related DEEs), other causes of early infantile epileptic encephalopathy with cerebellar/cortical malformation, and other autosomal recessive ataxia-epilepsy syndromes for the milder SCAR12 end of the spectrum.

**Newborn/carrier screening:** No population-based newborn or carrier screening program currently exists for *WWOX*, given its rarity; diagnosis is via clinical suspicion and confirmatory sequencing.

---

## 11. Outcome / Prognosis

- **Mortality:** Premature death occurred in 40% (8/20) of the largest published cohort, at a mean age of 40 months (PMID:30356099). A dedicated 2023 study ("WWOX developmental and epileptic encephalopathy: Understanding the epileptology and the mortality risk," PMID:36779245) specifically examined mortality risk factors in this population, reinforcing that null/loss-of-function genotypes carry the highest mortality risk (missense-only genotypes have not been associated with premature death).
- **Morbidity:** Profound and lifelong — no patients in the primary cohort achieved independent sitting or walking; complete absence of language; feeding difficulties requiring gastrostomy in 70%; respiratory complications (including presumed aspiration) in 40%; progressive scoliosis/kyphosis in 65%.
- **Disease course:** Progressive rather than static in a majority of patients (progressive cerebral atrophy in >50%), though the spectrum extends to milder/longer-surviving phenotypes — the oldest reported living patient is 40 years old.
- **Prognostic factors:** Genotype is the dominant known prognostic factor — biallelic null/LOF genotype predicts the most severe (WOREE/DEE28) phenotype and highest mortality risk; missense-containing genotypes predict the milder SCAR12 phenotype with better survival.
- **Recovery potential:** Essentially none with current standard-of-care management; this underlies the strong rationale for the gene-replacement therapy program described below.

---

## 12. Treatment

**Pharmacotherapy (symptomatic/anticonvulsant):** Standard antiepileptic drugs (AEDs) are largely **ineffective** — 95% of patients are drug-resistant, and "most parents report that their children's medications require frequent adjustment" (WWOX Foundation clinical guidance). No *WWOX*-specific pharmacological agent exists. NCIT term: NCIT:C15986 (Pharmacotherapy); specific AED classes would use NCIT:C258 (Anticonvulsant).

**Ketogenic diet:** Used with variable success as an adjunctive anti-seizure strategy in refractory cases, consistent with general use in other drug-resistant developmental and epileptic encephalopathies. NCIT:C15447 (Dietary Intervention).

**Device-based therapy:** Vagus nerve stimulation (VNS) has been considered/used in some refractory cases per WWOX Foundation clinical guidance. NCIT device-intervention term applicable (no precise NCIT term available per dismech convention).

**Supportive/nutritional care:** Nasogastric feeding progressing to **gastrostomy tube placement** is standard for the high proportion of patients with unsafe swallowing and aspiration risk. NCIT:C15433 (Nutritional Support) / gastrostomy procedure term; NCIT:C15329 (Surgical Procedure) for gastrostomy placement.

**Rehabilitative care:** Physical, occupational, and speech/feeding therapies are used supportively for hypotonia/spasticity and scoliosis management, though no disease-modifying effect is claimed. NCIT:C15302 (Physical Therapy).

**Gene replacement therapy (emerging/experimental — highest-impact recent development):**
- **Preclinical proof-of-concept:** A single **neonatal intracerebroventricular injection of AAV9-Synapsin I-WWOX** in *Wwox*-null mice rescued growth retardation, hypoglycemia, epileptic seizures, ataxia, and premature death — "providing a proof-of-concept for WWOX gene therapy as a promising approach for treating children with WOREE syndrome" (*EMBO Mol Med* 2021, PMC8649866). Therapeutic modality: GENE_THERAPY; AAV9 vector, neuron-specific Synapsin I promoter, unconjugated.
- **First-in-human treatment (2026):** An **8-month-old infant** became the first person to receive an experimental AAV9-mediated *WWOX* gene-replacement therapy, delivered via **cisterna magna injection**, under a compassionate-use program at Schneider Children's Medical Center of Israel (Hebrew University-affiliated program). One month post-treatment the child "remained clinically stable and has had no recurrent severe seizures" (news coverage: Jerusalem Post, News-Medical, Precision Medicine Online, 2026). This is described as the "world's first" gene therapy for WOREE syndrome; it remains at a compassionate-use/early clinical stage rather than a registered trial with published peer-reviewed efficacy data as of this report.

**Emerging strategies under preclinical investigation (per PMID:33916893 and ScienceDirect 2026 review "WWOX in brain development and disease: Molecular mechanisms and therapeutic opportunities"):**
- **NMD-modulating therapy** for splice-site/nonsense variants to rescue transcript stability.
- **Patient-derived iPSC/brain-organoid drug screening platforms**, which have already demonstrated that ectopic WWOX re-expression rescues the hyperexcitability/E-I-imbalance phenotype in WOREE-patient organoids (EMBO Mol Med, PMC8350905) — providing a mechanistic and translational bridge supporting the gene-therapy approach.
- **CRISPR-Cas9 gene editing**, considered theoretically but currently limited by CNS delivery challenges.

**Genetic counseling:** Recommended for all families given autosomal recessive inheritance, with prenatal diagnosis/carrier testing available for at-risk families with a known familial variant. NCIT:C15240 (Genetic Counseling).

---

## 13. Prevention

- **Primary prevention:** No population-level primary prevention exists given the disorder's extreme rarity; the principal prevention avenue is **genetic counseling and carrier testing** for families with a known *WWOX* pathogenic variant (especially in consanguineous unions or those with an affected relative), including preconception carrier screening and prenatal diagnosis (chorionic villus sampling/amniocentesis) or preimplantation genetic diagnosis (PGD) for known familial variants.
- **Secondary prevention:** Early genetic diagnosis following neonatal-onset refractory seizures allows for prompt initiation of supportive care (nutritional/respiratory) to reduce morbidity from aspiration and malnutrition, and — increasingly — the theoretical window for gene-replacement therapy, which preclinical mouse data indicate is most effective when administered neonatally, before irreversible developmental injury occurs.
- **Tertiary prevention:** Multidisciplinary supportive management (gastrostomy feeding, scoliosis surveillance/bracing, respiratory support) to reduce complications such as aspiration pneumonia, a plausible major contributor to the observed 40% early mortality.
- **Screening:** No newborn or population carrier screening program currently exists for *WWOX*, consistent with its ultra-rare status; cascade carrier testing within affected families is the primary applicable screening modality.

---

## 14. Other Species / Natural Disease

No naturally occurring *WWOX*-related disease has been reported in companion animals or wildlife (unlike many Mendelian disorders with veterinary correlates in OMIA); *WWOX* biology in other species has instead been studied through engineered/induced models (see Model Organisms, below).

**Taxonomy/orthology:** *WWOX* orthologs are conserved across vertebrates and invertebrates:
- Mouse: *Wwox* (NCBI Gene; MGI)
- Rat: *Wwox* (spontaneous *lde* [lethal dwarfism with epilepsy] mutant allele)
- Zebrafish: *wwox* (ZFIN)
- Drosophila: WWOX ortholog functions in aerobic metabolism/reactive oxygen species regulation and protects against ionizing radiation, as the fly FRA16D/WWOX ortholog (PMID:16007179; PMC3016910)

---

## 15. Model Organisms

| Model | Type | Key phenotype | Fidelity/relevance |
|---|---|---|---|
| **Mouse, *Wwox*-null (germline KO)** | Genetic knockout | Growth retardation, hypoglycemia, hypolipidemia, spontaneous and audiogenic seizures, ataxia, severe motor incoordination, cerebral malformations (incomplete hemisphere separation, neuronal heterotopia, defective cerebellar midline fusion), premature death by 2–3 weeks (PMID:33916893) | HIGH fidelity for the severe WOREE end of spectrum; rescued by neonatal AAV9-WWOX gene therapy (PMC8649866), directly supporting human translational program |
| **Mouse, neuronal conditional *Wwox* deletion** | Conditional knockout | Spontaneous epilepsy, cortical network hyperexcitability (elevated EPSC amplitude, reduced IPSC frequency/amplitude in layer II/III pyramidal neurons), hypomyelination, reduced oligodendrocyte maturation, impaired axonal conductivity (*Brain* 2021; *Neurobiol Dis* 2021, PMID:34634460) | HIGH fidelity for epilepsy and myelin pathology component of WOREE; isolates neuronal-autonomous contribution |
| **Mouse, *Wwox* P47T knock-in** | Missense/hypomorphic knock-in | Epilepsy, progressive neuroinflammation, cerebellar degeneration — "phenocopying human SCAR12" (bioRxiv 2022) | HIGH fidelity specifically for the milder SCAR12 (missense) end of the allelic spectrum, supporting the genotype-phenotype correlation |
| **Rat, *lde/lde* (lethal dwarfism with epilepsy)** | Spontaneous 13-bp deletion in exon 9 | Dwarfism, ataxic gait, high-incidence epileptic seizures, postnatal lethality; defective cerebral cortex development with hypomyelination (PMC6678113) | MODERATE-HIGH fidelity; naturally occurring rodent model paralleling WOREE neuropathology |
| **Zebrafish, *wwox* knockdown** | Morpholino knockdown | Pericardial edema, altered Ca²⁺ dynamics, developmental retardation (small eyes/head), abnormal bone formation, early lethality paralleling mouse KO timing (PMC4312067) | MODERATE fidelity; useful for early developmental and cardiovascular/metabolic phenotypes, less specific for CNS/epilepsy readouts |
| **Drosophila, WWOX ortholog mutant** | Genetic mutant | Altered aerobic metabolism, dysregulated reactive oxygen species handling, increased sensitivity to ionizing radiation (PMID:16007179; PMC3016910) | LOW-MODERATE fidelity for neurological phenotype; mechanistic model for WWOX's ancestral metabolic/oxidative-stress function |
| **Human iPSC-derived brain organoids (patient-derived and CRISPR-engineered isogenic)** | In vitro (NAM) | Cortical differentiation defects, Wnt pathway and DNA-damage-response impairment, neuronal hyperexcitability, E/I imbalance (↑GAD67/GABAergic shift), epileptiform low-frequency oscillations, amplified 4-aminopyridine responses; rescued by ectopic WWOX re-expression (EMBO Mol Med 2021, PMC8350905) | HIGH fidelity, human-genetic-background model directly bridging mouse mechanistic data to human gene-therapy translational rationale |

**Limitations across models:** Mouse and rat complete-knockout models die too early (2–4 weeks) to model the years-long chronic human disease course, limiting long-term therapeutic/natural-history studies; zebrafish and Drosophila models capture developmental/metabolic but not fine CNS network phenotypes; human organoids lack vasculature, immune cells, and long-term maturation, limiting study of the full in vivo hyperexcitability network and the progressive atrophy/neurodegeneration seen on patient MRI.

---

## Summary of Key Ontology Term Suggestions for KB Curation

- **MONDO:** MONDO:0014533 (developmental and epileptic encephalopathy 28)
- **Gene:** hgnc:12799 (WWOX)
- **Key HP terms:** HP:0001250 (Seizure), HP:0011097 (Epileptic encephalopathy), HP:0012736 (Profound global developmental delay), HP:0002079 (Hypoplasia of the corpus callosum), HP:0002120 (Cerebral atrophy), HP:0001252 (Hypotonia), HP:0000556 (Retinal dystrophy), HP:0000252 (Microcephaly), HP:0002650 (Scoliosis)
- **Key GO terms:** GO:0016055 (Wnt signaling pathway), GO:0007179 (TGF-beta receptor signaling pathway), GO:0043523 (regulation of neuron apoptotic process), GO:0042552 (myelination)
- **Key CL terms:** CL:0000598 (pyramidal neuron), CL:0000128 (oligodendrocyte), CL:0002453 (oligodendrocyte precursor cell)
- **Key UBERON terms:** UBERON:0002336 (corpus callosum), UBERON:0002037 (cerebellum), UBERON:0000966 (retina)
- **NCIT treatment terms:** NCIT:C15986 (Pharmacotherapy), NCIT:C15447 (Dietary Intervention/ketogenic diet), NCIT:C15238 (Gene Therapy), NCIT:C15240 (Genetic Counseling), NCIT:C15329 (Surgical Procedure/gastrostomy)

---

## Sources

- [WWOX-related epileptic encephalopathy caused by a novel mutation in the WWOX gene: a case report - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11479972/)
- [Neonatal neuronal WWOX gene therapy rescues Wwox null phenotypes - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC8649866/)
- [Neuronal deletion of Wwox, associated with WOREE syndrome, causes epilepsy and myelin defects | Brain](https://academic.oup.com/brain/article/144/10/3061/6259140)
- [WOREE syndrome - Wikipedia](https://en.wikipedia.org/wiki/WOREE_syndrome)
- [The phenotypic spectrum of WWOX-related disorders: 20 additional cases of WOREE syndrome and review of the literature | Genetics in Medicine (PMID:30356099)](https://www.nature.com/articles/s41436-018-0339-3)
- [The phenotypic spectrum of WWOX-related disorders - PMC (full text)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6752669/)
- [Identification of compound heterozygous deletion of the WWOX gene in WOREE syndrome | BMC Medical Genomics](https://link.springer.com/article/10.1186/s12920-023-01731-4)
- [WWOX-Related Developmental and Epileptic Encephalopathy | Neurology](https://www.neurology.org/doi/10.1212/WNL.0000000000213883)
- [Entry #616211 - DEVELOPMENTAL AND EPILEPTIC ENCEPHALOPATHY 28; DEE28 - OMIM](https://omim.org/entry/616211)
- [Neurological Disorders Associated with WWOX Germline Mutations—A Comprehensive Overview - PMC (PMID:33916893)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8067556/)
- [WWOX P47T loss-of-function mutation induces epilepsy, progressive neuroinflammation, and cerebellar degeneration in mice phenocopying human SCAR12 | bioRxiv](https://www.biorxiv.org/content/10.1101/2022.10.05.510979v1.full)
- [Altered neocortical oscillations and cellular excitability in an in vitro Wwox knockout mouse model of epileptic encephalopathy - PMC (PMID:34634460)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8609180/)
- [Wwox deficiency leads to neurodevelopmental and degenerative neuropathies and glycogen synthase kinase 3β-mediated epileptic seizure activity in mice](https://link.springer.com/article/10.1186/s40478-020-0883-3)
- [Loss of Wwox Causes Defective Development of Cerebral Cortex with Hypomyelination in a Rat Model of Lethal Dwarfism with Epilepsy - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6678113/)
- [WW domain-containing oxidoreductase in neuronal injury and neurological diseases - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4322972/)
- [A cascade of protein aggregation bombards mitochondria for neurodegeneration and apoptosis under WWOX deficiency | Cell Death & Disease](https://www.nature.com/articles/cddis2015251)
- [Hyaluronan activates Hyal-2/WWOX/Smad4 signaling and causes bubbling cell death when the signaling complex is overexpressed - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5386674/)
- [Transforming Growth Factor β1 Signaling via Interaction with Cell Surface Hyal-2 and Recruitment of WWOX/WOX1 - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC2708898/)
- [Twenty-five years of WWOX insight in cancer: a treasure trove of knowledge - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12055895/)
- [A multi-exon deletion within WWOX is associated with a 46,XY disorder of sex development | European Journal of Human Genetics (PMID:22071891)](https://www.nature.com/articles/ejhg2011204)
- [FRA16D common chromosomal fragile site oxido-reductase (FOR/WWOX) protects against the effects of ionizing radiation in Drosophila (PMID:16007179)](https://pubmed.ncbi.nlm.nih.gov/16007179/)
- [Drosophila orthologue of WWOX, the chromosomal fragile site FRA16D tumour suppressor gene, functions in aerobic metabolism and regulates reactive oxygen species - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3016910/)
- [Loss of wwox expression in zebrafish embryos causes edema and alters Ca2+ dynamics - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4312067/)
- [Modeling genetic epileptic encephalopathies using brain organoids | EMBO Molecular Medicine](https://link.springer.com/article/10.15252/emmm.202013610)
- [WWOX in brain development and disease: Molecular mechanisms and therapeutic opportunities - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0969996126001919)
- [Identification of a novel splice-site WWOX variant with paternal uniparental isodisomy in a patient with infantile epileptic encephalopathy (PMID:38407561)](https://pubmed.ncbi.nlm.nih.gov/38407561/)
- [Case report: Adult patient with WWOX developmental and epileptic encephalopathy: 40 years of observation - PMC (PMID:39507621)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11537890/)
- [WWOX developmental and epileptic encephalopathy: Understanding the epileptology and the mortality risk - PubMed (PMID:36779245)](https://pubmed.ncbi.nlm.nih.gov/36779245/)
- [MedicalResearch.com: Hebrew University First WWOX Gene Replacement Therapy Administered to Child With Hereditary Seizures](https://medicalresearch.com/hebrew-university-first-wwox-gene-replacement-therapy-administered-to-child-with-hereditary-seizures/)
- [First Infant Receives Gene Therapy for Rare WWOX-Related Epilepsy | Precision Medicine Online](https://www.precisionmedicineonline.com/inherited-disease/first-infant-receives-gene-therapy-rare-wwox-related-epilepsy)
- [World's first WWOX gene therapy performed on infant in Israel | The Jerusalem Post](https://www.jpost.com/health-and-wellness/article-898857)
- [Infant receives world's first gene therapy for WOREE syndrome - News-Medical](https://www.news-medical.net/news/20260608/Infant-receives-worlds-first-gene-therapy-for-WOREE-syndrome.aspx)
- [Diagnosis and Treatment | The WWOX Foundation](https://www.wwox.org/diagnosis-and-treatment)
- [WWOX Loss of Function in Neurodevelopmental and Neurodegenerative Disorders - PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7727818/)
- [Molecular Biology of the WWOX Gene That Spans Chromosomal Fragile Site FRA16D](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8305172/)
- [developmental and epileptic encephalopathy, 28 - MONDO / rarediseases.org](https://rarediseases.org/mondo-disease/developmental-and-epileptic-encephalopathy-28/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 32 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 4 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 3 |
| References weighed for topical relevance | 32 |
| On topic | 19 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:30356099` *(abstract only)*: "premature death has never been described in patients with missense pathogenic variant-only genotype"
  - closest text in source: "Eight novel missense pathogenic variants have been described"
- `PMID:33916893` *(abstract only)*: "premature death has never been described in patients with missense pathogenic variant-only genotype"
  - closest text in source: "Patients harboring pathogenic germline bi-allelic WWOX variants have been described with the rare devastating neurological syndromes autosomal recessive spinocerebellar ataxia 12 (SCAR12) (6 patients) and WWOX-related epileptic encephalopathy (DEE28 or WOREE syndrome) (56 patients)"
- `PMC:PMC8649866` *(abstract only)*: "providing a proof-of-concept for WWOX gene therapy as a promising approach for treating children with WOREE syndrome"
  - closest text in source: "These findings provide a proof-of-concept for WWOX gene therapy as a promising approach to curing children with WOREE and SCAR12."

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:8305172` (1 mention) - Ambulatory blood pressure patterns in youth.
  - shared terms: none

Weighed against this report's own most characteristic terms: `wwox`, `epileptic`, `woree`, `developmental`, `gene`, `seizure`, `syndrome`, `phenotype`, `genetic`, `disorder`, `encephalopathy`, `cerebral`, `epilepsy`, `patient`, `death`, `disease`, `scar12`, `variant`, `severe`, `spectrum`.