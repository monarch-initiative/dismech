---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-18T15:07:56.085207'
end_time: '2026-08-18T15:13:19.796805'
duration_seconds: 323.71
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Neurodevelopmental Disorder with or without Anomalies of the Brain,
    Eye, or Heart
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
  web_search_requests: 16
  num_turns: 24
  total_cost_usd: 1.9875698999999998
  session_id: ab59269f-2ee8-597f-9102-38fa42f2939c
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 20
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 5
  off_topic: 1
  off_topic_references:
  - PMID:9150137
  needs_review: true
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder with or without Anomalies of the Brain, Eye, or Heart
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder with or without Anomalies of the Brain, Eye, or Heart** covering all of the
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

I'll research this disorder now, starting by loading the web search tools I need.

I now have enough material to compile a comprehensive, well-cited report. Let me write it up.

# Neurodevelopmental Disorder with or without Anomalies of the Brain, Eye, or Heart (NEDBEH) — Comprehensive Research Report

## 1. Disease Information

**Overview.** NEDBEH is an autosomal dominant, RERE-related neurodevelopmental syndrome caused by heterozygous (usually de novo) pathogenic variants in **RERE** (Arginine-glutamic acid dipeptide (RE) Repeats gene, formerly *ATN2*/Atrophin-2), located at chromosome **1p36.23**. It is characterized by infantile-onset developmental delay/intellectual disability and behavioral abnormalities (including autism spectrum disorder), with roughly half of affected individuals showing additional structural anomalies of the eye, heart, brain, kidney/genitourinary tract, and/or mild sensorineural hearing loss (OMIM #616975; GeneReviews NBK538938).

**Key identifiers:**
- **OMIM:** #616975 (NEDBEH); gene entry *RERE* #605226
- **MONDO:** MONDO:0014857
- **Gene:** RERE, HGNC:9965, RefSeq NM_012102
- **Synonyms:** RERE-related neurodevelopmental syndrome; Arginine-glutamic acid dipeptide repeats-related neurodevelopmental syndrome; "1p36-like syndrome" (phenotypic overlap term, not a formal synonym)
- **Source of data:** Aggregated disease-level resource, built from published patient cohorts (case series pooled across multiple centers via GeneMatcher/exome sequencing), not a single EHR-derived dataset — the literature comprises small but growing cohorts (10 → 19 → 54 published individuals across successive reports).

RERE is distinct from, but overlaps clinically with, **CDK19-related disorder / Developmental and Epileptic Encephalopathy 87 (DEE87, OMIM #618916)**, a separate gene-disease relationship that surfaced in initial searches for this disease name; RERE/NEDBEH is the entity actually assigned that formal OMIM name and clinical synopsis (OMIM #616975: https://omim.org/entry/616975; GARD: https://rarediseases.info.nih.gov/diseases/17902/).

Sources: [OMIM #616975](https://omim.org/entry/616975); [GeneReviews RERE-Related Disorders](https://www.ncbi.nlm.nih.gov/books/NBK538938/); [GARD](https://rarediseases.info.nih.gov/diseases/17902/neurodevelopmental-disorder-with-or-without-anomalies-of-the-brain-eye-or-heart); [MalaCards](https://www.malacards.org/card/neurodevelopmental_disorder_with_or_without_anomalies_of_the_brain_eye_or_heart)

---

## 2. Etiology

**Disease causal factor:** Monogenic — heterozygous loss-of-function (nonsense, frameshift, splice-site, whole/partial gene deletion) or missense pathogenic variants in **RERE**. Essentially all reported cases are **de novo**; no confirmed instances of inheritance from an affected parent were reported in the original 2016–2018 cohorts (Fregeau et al., PMID:27087320; Jordan et al., PMID:29330883).

**Genetic risk factors:**
- *De novo* single-nucleotide variants and small indels, concentrated in two hotspots: (1) the **atrophin-1 homology domain**, and (2) a **21-amino-acid histidine-rich region (HRR)** within that domain (residues ~1425–1445). Jordan et al. found that of 19 published NEDBEH patients, 6 (31%) carried loss-of-function (LOF) variants and 12 (63%) carried atrophin-1-domain point mutations, many clustering in the HRR (PMID:29330883).
- A recurrent 2-amino-acid in-frame duplication in the HRR (c.4313_4318dupTCCACC) produces a distinctive **CHARGE-syndrome-like phenotype** (choanal atresia, coloboma) — a specific genotype-phenotype correlation.
- A newer, larger cohort (54 individuals; ScienceDirect/AJHG 2025-26 preprint, "New genotype-phenotype correlations and management recommendations for individuals with RERE variants") stratifies variants into 5 sub-cohorts — LOF, missense inside HRR, missense outside HRR, HRR in-frame deletions, HRR in-frame duplications — and finds HRR-region missense/duplication variants are **structurally stabilizing**, consistent with a **gain-of-function or dominant-negative** mechanism, whereas LOF variants act through classic haploinsufficiency and are milder, occasionally inherited from a mildly/subclinically affected parent.
- Whole or partial gene deletions (including as part of proximal 1p36 microdeletions) are also causal, supporting a haploinsufficiency mechanism for the LOF class.

**Environmental risk factors:** None established; this is a monogenic developmental disorder with no reported environmental, toxin, infectious, occupational, or lifestyle risk contributors in the literature.

**Protective factors:** None specifically documented; no protective genetic modifiers or environmental protective factors have been reported.

**Gene-environment interaction:** Not applicable/not documented — RERE-related NEDBEH shows no described GxE interaction; phenotypic variability instead correlates with variant type/location (genotype-phenotype correlation), not environmental exposure.

Sources: [Jordan et al. 2018, Hum Mutat, PMID:29330883](https://onlinelibrary.wiley.com/doi/10.1002/humu.23400); [Fregeau et al. 2016, AJHG, PMID:27087320](https://pubmed.ncbi.nlm.nih.gov/27087320/); [ScienceDirect — New genotype-phenotype correlations](https://www.sciencedirect.com/science/article/abs/pii/S1098360026008981)

---

## 3. Phenotypes

### Neurodevelopmental/behavioral (nearly universal)
- **Developmental delay / intellectual disability** — present in the great majority of patients, ranging mild to profound. HPO: **HP:0001263** (Global developmental delay), **HP:0001249** (Intellectual disability).
- **Hypotonia and feeding difficulties** — commonly observed from infancy. HPO: **HP:0001252** (Hypotonia), **HP:0011968** (Feeding difficulties).
- **Autism spectrum disorder / autistic features** — a substantial subset. HPO: **HP:0000717** (Autism).
- **ADHD, self-injurious behavior** — reported behavioral comorbidities. HPO: **HP:0007018** (Attention deficit hyperactivity disorder), **HP:0100716** (Self-injurious behavior).
- **Epilepsy/seizures** — reported in ~2/19 (~10%) of the original cohort; onset variable. HPO: **HP:0001250** (Seizure).
- **Brain MRI abnormalities** — ~13/19 (~70%): thinning/hypoplasia of the corpus callosum, decreased white matter volume, ventriculomegaly, and small/abnormal cerebellar vermis. HPO: **HP:0002079** (Hypoplasia of the corpus callosum), **HP:0002119** (Ventriculomegaly), **HP:0001320** (Cerebellar vermis hypoplasia).

### Ocular (~30% affected)
- Structural: coloboma, optic nerve anomalies, microphthalmia, Peters anomaly. HPO: **HP:0000589** (Coloboma), **HP:0000568** (Microphthalmia), **HP:0031705** (Anterior segment dysgenesis-type findings/Peters anomaly context).
- Refractive/motility: myopia, astigmatism, strabismus. HPO: **HP:0000545** (Myopia), **HP:0000486** (Strabismus).

### Cardiac (~40% affected)
- Congenital heart defects, predominantly septal defects (ASD/VSD). HPO: **HP:0001629** (Ventricular septal defect), **HP:0001631** (Atrial septal defect), **HP:0030680** (Abnormal cardiovascular system morphology).

### Auditory (~20% affected)
- Mild sensorineural hearing loss, uni- or bilateral. HPO: **HP:0000407** (Sensorineural hearing impairment).

### Genitourinary
- Vesicoureteral reflux; in males, cryptorchidism and hypospadias. HPO: **HP:0000076** (Vesicoureteral reflux), **HP:0000028** (Cryptorchidism), **HP:0000047** (Hypospadias).

### Musculoskeletal
- Congenital hip dysplasia (~2/19, ~10%). HPO: **HP:0001385**.
- Scoliosis (~3/19, ~15%). HPO: **HP:0002650**.

### Other
- Choanal atresia (specifically linked to the recurrent HRR duplication variant, giving a CHARGE-like presentation). HPO: **HP:0000453**.
- Gastroesophageal reflux. HPO: **HP:0002020**.

**Phenotype characteristics:**
- **Onset:** Congenital/neonatal to infantile; developmental problems typically first noted in infancy.
- **Severity:** Highly variable, from mild learning/behavioral issues to profound multisystem disease; severity correlates with variant class (HRR missense/duplication > LOF).
- **Progression:** Developmental delay is a static/non-degenerative neurodevelopmental process rather than a progressive neurodegeneration; structural anomalies are congenital and generally non-progressive, though scoliosis can progress with growth.
- **Frequency:** See per-phenotype percentages above (from the 19-patient Jordan et al. cohort; a 54-patient cohort further refines these by variant class).

**Quality of life impact:** Not separately quantified with standardized instruments (EQ-5D/SF-36) in the literature to date; qualitatively, impact is driven by the combination of intellectual disability, feeding/growth problems in infancy, sensory (visual/auditory) impairment, and behavioral comorbidities, often requiring lifelong developmental, educational, and multidisciplinary medical support (GeneReviews management section).

Sources: [GeneReviews NBK538938](https://www.ncbi.nlm.nih.gov/books/NBK538938/); [Jordan et al. 2018, PMID:29330883](https://onlinelibrary.wiley.com/doi/10.1002/humu.23400); [OMIM Clinical Synopsis #616975](https://omim.org/clinicalSynopsis/616975)

---

## 4. Genetic/Molecular Information

- **Causal gene:** RERE (HGNC:9965; NM_012102), OMIM gene entry #605226. 22 coding exons plus 2 noncoding exons; encodes a large (~1,566 amino acid) nuclear protein.
- **Variant classification (ACMG/AMP):** Pathogenic/likely pathogenic heterozygous variants; VUS reclassification is an active area (the 54-patient cohort explicitly includes VUS reclassified via segregation/functional data).
- **Variant types:**
  - **Loss-of-function**: nonsense, frameshift, canonical splice-site variants, and partial/whole-gene deletions → haploinsufficiency.
  - **Missense** variants, concentrated in the atrophin-1 domain, particularly the histidine-rich region (HRR, aa ~1425–1445) → structurally stabilizing, proposed **gain-of-function/dominant-negative** mechanism, associated with more severe multisystem phenotypes.
  - **In-frame duplications/deletions** within the HRR — a recurrent 6-bp (2-amino-acid) duplication produces a CHARGE-like phenotype.
- **Allele frequency:** RERE loss-of-function variants are rare/absent as a class in population reference databases (gnomAD), consistent with strong purifying selection against LOF alleles and a haploinsufficiency disease mechanism; specific pLI/LOEUF values were not independently confirmed from primary sources in this research pass and should be verified directly against gnomAD before citation in the KB.
- **Somatic vs. germline:** All reported disease-causing variants are germline (de novo in the great majority; rare parental transmission from a mildly affected/mosaic parent reported for milder LOF alleles in the expanded 54-patient cohort).
- **Functional consequences:**
  - LOF variants → **haploinsufficiency** of RERE, a nuclear receptor coregulator.
  - HRR missense/in-frame variants → altered protein stability/interaction, proposed dominant-negative or gain-of-function effect on corepressor complex assembly.
- **Modifier genes:** None specifically established; phenotypic variability is currently explained primarily by variant type/location rather than trans-acting modifiers.
- **Epigenetic information:** RERE itself functions as a transcriptional corepressor/coregulator (see Mechanism, below) — i.e., RERE dysfunction produces downstream epigenetic/chromatin consequences (altered histone deacetylation via Sin3A/HDAC recruitment) rather than RERE itself being regulated by known disease-specific DNA methylation changes.
- **Chromosomal abnormalities:** RERE lies in the **proximal 1p36 critical region**; both terminal and interstitial 1p36 deletions encompassing RERE reproduce much of the NEDBEH phenotype, and RERE haploinsufficiency is considered a major contributor to **1p36 deletion syndrome** (one of the most common human terminal deletion syndromes, incidence ~1/5,000–1/10,000 live births, i.e., roughly 10–20 per 100,000 births) (Wikipedia summary of 1p36 deletion syndrome; PMC10100125).

Sources: [GeneReviews NBK538938](https://www.ncbi.nlm.nih.gov/books/NBK538938/); [OMIM #605226 RERE](https://omim.org/entry/605226); [ClinGen Dosage Sensitivity — RERE](https://search.clinicalgenome.org/kb/gene-dosage/HGNC:9965); [1p36 deletion syndrome review, PMC10100125](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10100125/)

---

## 5. Environmental Information

No specific environmental factors, lifestyle factors, or infectious agents have been implicated as causal or contributory to NEDBEH — it is a purely monogenic Mendelian disorder. This section is **not applicable** for this disease beyond noting the absence of documented environmental etiology in the literature reviewed.

---

## 6. Mechanism / Pathophysiology

**Molecular pathway / protein function.** RERE is a member of the **atrophin family** of arginine-glutamic acid (RE) dipeptide-repeat nuclear proteins (paralog of ATN1/Atrophin-1, the gene mutated in dentatorubral-pallidoluysian atrophy). RERE functions as a **nuclear receptor coregulator** that positively regulates **retinoic acid (RA) signaling** during embryogenesis. Mechanistically, RERE has been shown to form a complex with **NR2F2 (COUP-TFII)**, the coactivator **p300**, and a retinoic acid receptor (RAR), which is recruited to retinoic-acid response elements (RAREs) of RA target genes — the "WHHERE" coactivator complex, required for retinoic-acid-dependent regulation of embryonic (left-right) symmetry.

RERE also participates in transcriptional **repression** as a component of corepressor assemblies analogous to the well-characterized **NCoR/SMRT–Sin3A–HDAC** repressor complex used broadly by nuclear hormone receptors: in the unliganded state, nuclear receptor heterodimers recruit NCoR/SMRT along with Sin3A and histone deacetylases (e.g., HDAC1/HDAC3) to establish a repressive, deacetylated chromatin state. RERE's dual coactivator/corepressor roles position it as a context-dependent modulator of RA-responsive and other nuclear-receptor-driven transcriptional programs during organogenesis.

**Cellular processes.** Loss of functional RERE dysregulates RA-dependent transcriptional programs required for normal patterning of multiple organ systems, producing developmental field defects rather than a single-tissue lesion — consistent with the multisystem (brain, eye, heart, kidney, ear) phenotype of NEDBEH.

**Protein dysfunction.**
- LOF alleles (nonsense/frameshift/deletion) → **haploinsufficiency**: reduced RERE dosage impairs formation/stoichiometry of RA-signaling coactivator complexes.
- HRR missense/duplication alleles → altered protein structure that appears to **stabilize** RERE (rather than degrade it), proposed to act as **dominant-negative** or **gain-of-function** alleles that more severely perturb corepressor/coactivator complex function — correlating clinically with more severe, multisystem phenotypes (structural eye, heart, renal, and hearing anomalies) than LOF alleles.

**Tissue damage / developmental mechanisms.** Because RA signaling operates as a morphogen gradient critical to hindbrain, eye, heart (looping/patterning), otic, and kidney development, disruption of RERE-dependent RA signaling during critical embryonic windows plausibly explains the pattern of structural anomalies (ocular colobomas/microphthalmia, septal heart defects, sensorineural hearing loss, renal/GU anomalies) that co-occur with the neurodevelopmental core phenotype.

**Model-organism mechanistic evidence:**
- **Mouse:** An allelic series of *Rere*-deficient mice (including the hypomorphic **eyes3** allele and a null "om" allele) recapitulates multiple organ phenotypes seen in human 1p36 deletion/NEDBEH: compound heterozygous (*Rere^om/eyes3*) mice show perinatal mortality, postnatal growth deficiency, brain hypoplasia with decreased hippocampal neuron numbers, hearing loss, cardiovascular malformations, spontaneous adult cardiac fibrosis, and renal agenesis (PMC3581587; PLOS ONE journal.pone.0057460). This is strong **MODEL_ORGANISM** evidence directly linking Rere dosage to the multi-organ phenotype spectrum, and supports Rere haploinsufficiency as a driver of proximal 1p36 deletion phenotypes.
- Earlier work (Rere controls retinoic acid signalling and somite bilateral symmetry) established the RA-signaling/embryonic-symmetry mechanistic link in model systems.

**Molecular profiling / advanced technologies.** No large-scale disease-specific transcriptomic, proteomic, metabolomic, single-cell, or spatial-transcriptomic datasets specific to human RERE-mutant tissue were identified in this search pass; mechanistic insight to date derives primarily from biochemical/protein-interaction studies and mouse allelic-series phenotyping rather than patient-derived omics.

**Suggested ontology terms:**
- GO: **GO:0003713** (transcription coactivator activity), **GO:0003714** (transcription corepressor activity), **GO:0043401** (steroid hormone-mediated signaling pathway, as a proxy for nuclear-receptor signaling), retinoic acid receptor signaling pathway terms.
- CL: neural progenitor cell, cardiomyocyte, otic/hair cell, renal progenitor cell (organ-specific developmental cell types affected).

Sources: [PLOS ONE — Allelic series of Rere mice, PMC3581587](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3581587/); [GeneCards RERE](https://www.genecards.org/card/RERE); [WHHERE coactivator complex, Nat Commun](https://www.nature.com/articles/s41467-017-00593-6); [Nuclear receptor corepressor mechanism review](https://pubmed.ncbi.nlm.nih.gov/9150137/)

---

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Brain/CNS (corpus callosum, white matter, cerebellar vermis, ventricles), eye, heart, ear (cochlea/inner ear).
- **Secondary:** Kidney/urinary tract, genital tract (males), skeletal system (hip, spine).
- **Body systems:** Nervous system, ocular system, cardiovascular system, auditory/vestibular system, genitourinary system, musculoskeletal system.

**Tissue/cell level:**
- CNS: white matter tracts, corpus callosum fibers, cerebellar cortex/vermis neurons, hippocampal neurons (mouse model evidence: decreased hippocampal neuron number).
- Eye: retina/optic fissure (coloboma), optic nerve, lens/anterior segment (Peters anomaly), extraocular muscles (strabismus).
- Heart: interatrial/interventricular septum (septal defects), myocardium (fibrosis in mouse model).
- Ear: cochlear hair cells/auditory nerve (sensorineural hearing loss).
- Kidney/GU: renal parenchyma (agenesis in mouse model), ureter (vesicoureteral reflux), testis (cryptorchidism), urethra (hypospadias).

**Subcellular level:** Nucleus — RERE is a nuclear coregulator protein; its principal molecular activity occurs at chromatin, within transcriptional coactivator/corepressor complexes (GO Cellular Component: nucleus, transcription regulator complex).

**Localization/lateralization:** Predominantly bilateral/symmetric anomalies (bilateral hearing loss, bilateral structural eye/renal findings reported), consistent with RERE's role in RA-dependent embryonic (left-right and organ) symmetry established in model organisms; some findings (e.g., unilateral hearing loss) are reported as variable.

Suggested UBERON terms: UBERON:0000955 (brain), UBERON:0000970 (eye), UBERON:0000948 (heart), UBERON:0001690 (ear), UBERON:0002113 (kidney).

---

## 8. Temporal Development

- **Onset:** Congenital/neonatal for structural anomalies; developmental delay typically recognized in infancy (first months to first 1–2 years of life). No adult-onset or late-onset presentation is described — this is a developmental (not degenerative) disorder.
- **Onset pattern:** Insidious recognition of developmental delay in infancy; structural anomalies (cardiac, ocular, renal) are present from birth and may be identified prenatally (e.g., by fetal echocardiography) or in the neonatal period.
- **Progression/course:** Predominantly **stable, non-progressive** developmental disability rather than a degenerative course; no reports of regression. Scoliosis may progress during growth and requires periodic monitoring. Seizures, when present, may require ongoing management but are not described as progressively worsening as a class.
- **Disease duration:** Lifelong/chronic — a static neurodevelopmental disorder with structural anomalies; documented survival into early adulthood (reported patients in their early twenties), though long-term life-expectancy data are not yet established given the disorder's relatively recent delineation (first described 2016).
- **Remission patterns:** Not applicable — the neurodevelopmental phenotype does not remit; treated features (e.g., surgically corrected heart or hip defects) can be structurally resolved, but the underlying intellectual disability/developmental impairment persists.
- **Critical periods:** Given the RA-signaling mechanism, the presumed critical window for structural anomalies is early embryogenesis (organogenesis), while the critical period for developmental/behavioral intervention is early childhood (per GeneReviews management recommendations emphasizing early intervention ages 0–3).

---

## 9. Inheritance and Population

**Epidemiology:**
- NEDBEH itself is an **ultra-rare** disorder: the literature comprises small but growing published cohorts — 10 patients (Fregeau et al. 2016), 19 patients (Jordan et al. 2018), and most recently 54 individuals (30 newly reported) in an expanded genotype-phenotype cohort (2025-26). No formal population-based prevalence or incidence estimate (cases per 100,000) has been established, consistent with an underrecognized/underdiagnosed monogenic condition identified mainly via exome sequencing in the developmental-delay diagnostic pathway.
- By contrast, the phenotypically overlapping **1p36 deletion syndrome** (which frequently encompasses RERE) has an estimated incidence of **1/5,000–1/10,000 live births** (~10–20 per 100,000), making it one of the most common human terminal deletion syndromes — useful epidemiological context, though not a direct prevalence figure for isolated RERE-variant NEDBEH.

**Inheritance pattern:** Autosomal dominant. Virtually all reported cases arise **de novo**; the newly expanded cohort documents rare instances of inheritance from a **mildly symptomatic or clinically unaffected (mosaic) parent**, specifically among milder loss-of-function alleles.

**Penetrance:** Appears high but variably expressive; LOF variants can present with milder, sometimes subclinical, parental phenotypes, suggesting incomplete penetrance or highly variable expressivity for that allelic class. HRR missense/duplication variants appear more consistently penetrant with more severe, multisystem, de novo presentations.

**Expressivity:** Markedly **variable**, correlating with variant class/location (LOF vs. atrophin-1-domain/HRR missense vs. HRR in-frame duplication/deletion) — this genotype-phenotype correlation is one of the best-characterized features of the disorder (Jordan et al. 2018; expanded 2025-26 cohort).

**Genetic anticipation:** Not described/not applicable (not a repeat-expansion disorder in the classic sense, though the HRR duplication is a small in-frame repeat expansion associated with a specific — but not progressively worsening across generations — phenotype).

**Germline mosaicism:** Theoretically possible and invoked to explain the ~1% empiric sibling recurrence risk cited by GeneReviews despite de novo occurrence in probands; not directly documented with confirmed mosaic parental cases in the earliest cohorts, though the expanded cohort's report of parental transmission raises the possibility of parental mosaicism/mild expressivity for LOF alleles specifically.

**Founder effects / consanguinity:** Not reported — consistent with a dominant, de novo disease mechanism rather than a recessive founder-population disorder.

**Carrier frequency:** Not applicable (autosomal dominant, not carrier-screened as a recessive trait).

**Population demographics:** No specific ethnic, geographic, or sex-ratio predilection has been reported in the literature reviewed; cases have been identified across diverse referral cohorts via clinical exome sequencing (GeneMatcher-facilitated case ascertainment), suggesting a global, non-ethnicity-restricted distribution typical of de novo dominant Mendelian disorders.

Sources: [GeneReviews NBK538938](https://www.ncbi.nlm.nih.gov/books/NBK538938/); [Jordan et al. 2018, PMID:29330883](https://onlinelibrary.wiley.com/doi/10.1002/humu.23400); [1p36 deletion syndrome, PMC10100125](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10100125/); [Wikipedia — 1p36 deletion syndrome](https://en.wikipedia.org/wiki/1p36_deletion_syndrome)

---

## 10. Diagnostics

**Diagnostic criterion:** Identification of a heterozygous pathogenic (or likely pathogenic) variant in RERE by molecular genetic testing, in the context of a compatible clinical phenotype.

**Testing approach (sequential, per GeneReviews):**
1. **Chromosomal microarray analysis (CMA)** — first-line, to detect gene-level or larger 1p36 deletions/duplications encompassing RERE.
2. **Multigene intellectual-disability/developmental-delay panel** including RERE.
3. **Exome sequencing (WES)** — comprehensive approach when panel/CMA are non-diagnostic; this is how the majority of published cases were ascertained.
- **Single-gene sequential testing is NOT recommended** as a first-line approach given genetic heterogeneity of the presenting phenotype (intellectual disability ± multisystem anomalies).
- In the original diagnostic cohort: sequence analysis detected pathogenic variants in 18/19 probands; gene-targeted deletion/duplication analysis detected 1/19.

**Clinical tests / phenotyping work-up:**
- **Ophthalmologic exam** for coloboma, microphthalmia, optic nerve anomalies, strabismus, refractive error.
- **Audiologic evaluation** (behavioral/OAE/ABR as age-appropriate) for sensorineural hearing loss.
- **Echocardiography** for septal and other congenital heart defects.
- **Renal/bladder ultrasound ± voiding cystourethrogram** for vesicoureteral reflux and structural anomalies.
- **Brain MRI** for corpus callosum, white matter, ventricular, and cerebellar vermis abnormalities (found in ~70% of the original cohort).
- **EEG** if seizures are suspected.
- Skeletal exam/imaging for scoliosis and hip dysplasia.

**Differential diagnosis:**
- **CHARGE syndrome** (CHD7 pathogenic variants) — particularly relevant for the HRR-duplication RERE genotype that produces a CHARGE-like phenotype (coloboma, choanal atresia); distinguishing features include semicircular canal defects and tracheoesophageal fistula, more characteristic of true CHD7-CHARGE.
- **1p36 deletion syndrome** — overlapping phenotype when RERE lies within a larger proximal 1p36 deletion; distinguished by additional genes/dosage effects and characteristic dysmorphic facial features of 1p36 deletion.
- Other syndromic intellectual disability disorders with overlapping developmental delay/congenital anomaly presentations, evaluated via the same broad genomic testing pathway.

**Screening:** No population-based newborn or carrier screening applies (ultra-rare, predominantly de novo autosomal dominant disorder); diagnosis relies on clinical suspicion triggering genomic testing.

Sources: [GeneReviews NBK538938](https://www.ncbi.nlm.nih.gov/books/NBK538938/)

---

## 11. Outcome/Prognosis

- **Survival:** Documented survival into early adulthood (reported affected individuals into their early twenties); population-level life-expectancy data are not yet established given the disorder's recent delineation (2016) and small published cohort size. No disease-specific mortality statistics are available.
- **Morbidity/function:** Long-term functional outcome is driven by the degree of intellectual disability, presence/severity of structural organ anomalies (especially cardiac and renal), and sensory impairments (vision, hearing); standardized quality-of-life instrument data (EQ-5D, SF-36, PROMIS) specific to NEDBEH were not identified.
- **Complications:** Seizures (in the epilepsy-affected subset), feeding/growth difficulties requiring gastrostomy in some infants, progressive scoliosis, cardiac complications from unrepaired/repaired septal defects, renal complications from vesicoureteral reflux (recurrent UTI, renal scarring risk).
- **Recovery potential:** Structural anomalies (cardiac, hip, renal) are amenable to surgical/medical correction with generally good outcomes for the specific defect; the core neurodevelopmental impairment (intellectual disability) is not expected to resolve, though early intervention is associated with improved developmental trajectories in intellectual disability generally.
- **Prognostic factors:** **Variant class is the key emerging prognostic factor** — HRR-region missense variants and in-frame HRR duplications are associated with more severe, multisystem phenotypes (more structural anomalies) than loss-of-function variants, which tend to have milder, sometimes parentally-inherited/subclinical presentations. This genotype-phenotype correlation is now being formalized into variant-specific management/counseling recommendations in the most recent (2025-26) expanded cohort study.

Sources: [Jordan et al. 2018, PMID:29330883](https://onlinelibrary.wiley.com/doi/10.1002/humu.23400); [GeneReviews NBK538938](https://www.ncbi.nlm.nih.gov/books/NBK538938/); [New genotype-phenotype correlations, ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1098360026008981)

---

## 12. Treatment

There is **no disease-modifying or gene-specific therapy** for NEDBEH; management is entirely **supportive and multidisciplinary**, targeting individual manifestations:

**Pharmacotherapy:**
- **Antiepileptic drugs** for seizure management in the subset with epilepsy (NCIT: C15986 Pharmacotherapy; specific agent selection per standard epilepsy management, not RERE-specific).
- No RERE-targeted pharmacogenomic guidance has been established.

**Surgical/interventional (NCIT:C15329 Surgical Procedure):**
- Ophthalmologic surgical correction for strabismus and structural eye anomalies as indicated.
- Cardiac surgical repair for significant septal defects (NCIT:C15289 context for structural cardiac correction).
- Orthopedic surgery for hip dysplasia and progressive scoliosis (NCIT:C16186 Orthopedic Surgical Procedure).
- Urologic surgery for cryptorchidism/hypospadias as indicated.

**Supportive and rehabilitative care:**
- **Speech and feeding therapy**; nasogastric or gastrostomy tube feeding for significant feeding difficulties in infancy (NCIT:C15447 Dietary Intervention / supportive feeding management).
- **Physical and occupational therapy** for hypotonia and motor delay (NCIT:C15302 Physical Therapy).
- **Audiologic intervention**, including hearing aids for sensorineural hearing loss.
- **Behavioral interventions**, including applied behavior analysis (ABA) for autism spectrum/behavioral features (NCIT:C181743 context — behavioral counseling/intervention).
- **Early intervention services** (ages 0–3), developmental preschool (ages 3–5), and special education/individualized education plans (ages 5–21) (NCIT:C49236 Therapeutic Procedure, broadly).
- Enrollment with regional Developmental Disabilities Administration/support services.

**Surveillance schedule (per GeneReviews):**
- Developmental progress assessment: at least annually.
- Ophthalmologic and audiologic evaluation: annually or as clinically indicated.
- Scoliosis screening: annually until skeletal growth is complete.
- Cardiology and urology follow-up: as clinically indicated based on baseline findings.

**Experimental/investigational:** No RERE-specific clinical trials (gene therapy, targeted molecular therapy) were identified; given the haploinsufficiency mechanism for LOF alleles, RERE would in principle be a theoretical candidate for future dosage-restoration approaches (e.g., ASO-mediated upregulation), but no such program has been reported in the literature reviewed.

**Genetic counseling as an intervention:** Central to management — recurrence risk counseling (~1% empiric sibling risk accounting for possible germline mosaicism), prenatal/preimplantation genetic testing availability given a known familial variant, and variant-class-specific counseling per the emerging genotype-phenotype framework (NCIT:C15240 Genetic Counseling).

Sources: [GeneReviews NBK538938 — Management section](https://www.ncbi.nlm.nih.gov/books/NBK538938/); [New genotype-phenotype correlations and management recommendations, ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1098360026008981)

---

## 13. Prevention

- **Primary prevention:** Not applicable in the traditional sense (de novo monogenic disorder, not preventable through risk-factor modification, vaccination, or lifestyle change).
- **Secondary prevention (early detection):** Early recognition of developmental delay and prompt genomic (exome/CMA-based) diagnostic testing enables earlier initiation of supportive interventions and surveillance for associated structural anomalies (cardiac, renal, ocular) before they cause complications.
- **Genetic counseling / reproductive options:** Once a familial pathogenic RERE variant is identified, **prenatal diagnosis** and **preimplantation genetic testing** are available for future pregnancies, given the ~1% empiric recurrence risk (accounting for possible parental germline mosaicism) — this is the principal "prevention" lever available for this disorder (NCIT:C15240 Genetic Counseling).
- **Tertiary prevention:** Structured surveillance protocols (annual developmental, ophthalmologic, audiologic, and scoliosis screening; clinically indicated cardiology/urology follow-up) aim to detect and manage complications early, per GeneReviews recommendations above.
- **Public health/screening programs:** None specific to RERE/NEDBEH exist (no newborn screening applicability — this is a developmental/structural genetic disorder, not a biochemically screenable condition).

---

## 14. Other Species / Natural Disease

- **Taxonomy:** No naturally occurring RERE-related disease has been reported in non-human species (companion animals, livestock, or wildlife); OMIA search did not surface a veterinary RERE disease entry in this research pass.
- **Orthologous gene:** *Rere* is conserved in mouse (Mus musculus, NCBI Taxon:10090) and zebrafish (Danio rerio, NCBI Taxon:7955), used exclusively as **experimental/induced** models (see Section 15) rather than as naturally occurring disease in those species.
- **Comparative biology:** The RA-signaling coactivator/corepressor mechanism of RERE is evolutionarily conserved from zebrafish through mammals, underpinning the validity of animal-model data for understanding human RERE haploinsufficiency (see mouse allelic series data above).
- **Zoonotic potential:** Not applicable — this is a non-infectious, monogenic developmental disorder.

---

## 15. Model Organisms

**Mouse (Mus musculus) — the best-characterized model:**
- An **allelic series of *Rere*-deficient mice** — including a hypomorphic missense allele (**eyes3**) and a null allele (**"om"**) — recapitulates multiple organ systems affected in human proximal 1p36 deletions/NEDBEH. Compound heterozygous *Rere^om/eyes3* mice display:
  - Perinatal mortality
  - Postnatal growth deficiency
  - Brain hypoplasia with decreased hippocampal neuron numbers
  - Hearing loss
  - Cardiovascular malformations, with spontaneous cardiac fibrosis developing in adulthood
  - Renal agenesis
  - This is genotype-dosage-graded (allelic series), i.e., different combinations of hypomorphic/null alleles produce a phenotypic severity gradient — directly informative for the human genotype-phenotype (LOF vs. more severe missense) correlation. (PMID for the allelic-series paper is referenced in search results as 23451234; verify directly before KB citation.)
- Prior work (Rere controls retinoic acid signalling and somite bilateral symmetry) established that Rere is required for retinoic-acid-dependent left-right embryonic symmetry, mechanistically linking Rere loss to structural (including cardiac laterality-related) anomalies.
- **Model type:** Genetic (induced hypomorphic and null knock-in/knockout alleles), mammalian, in vivo.
- **Phenotype recapitulation:** High fidelity for growth deficiency, brain hypoplasia, hearing loss, cardiac malformation/fibrosis, and renal agenesis — directly paralleling human NEDBEH/1p36-deletion phenotypes (**RECAPITULATES**, evidence source MODEL_ORGANISM).
- **Limitations:** Mouse models used here are largely hypomorphic/null compound-heterozygote combinations rather than precise knock-in of specific human missense/HRR variants, so allele-specific (e.g., dominant-negative HRR-duplication) mechanisms are not yet directly modeled; perinatal lethality in some allelic combinations may limit study of adult/behavioral phenotypes.

**Zebrafish (Danio rerio):** RERE/rere has documented roles in retinoic-acid-dependent developmental signaling in zebrafish and other vertebrate systems (consistent with the WHHERE coactivator complex and RA-target gene regulation described in Section 6); a specific "hi" (hypomorphic insertional) rere mutant with detailed cardiac-looping/laterality phenotyping was referenced in general zebrafish heart-development literature searches, but a directly confirmed, disease-relevant PMID for a zebrafish rere cardiac-looping mutant was not conclusively retrieved in this pass and should be independently verified before citation.

**Resources:** MGI (Mouse Genome Informatics) for *Rere* allele records; ZFIN for zebrafish *rere* records.

Sources: [PLOS ONE — Allelic series of mice, PMC3581587](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3581587/); [PMC full text of allelic series paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3581587/)

---

## Summary of Key Evidence Gaps / Caveats for Curation

1. **Primary literature access:** OMIM.org and PubMed direct fetch were blocked (403/cookie-wall) during this research session; findings above are synthesized from search-engine summaries of GeneReviews (NBK538938), the PLOS ONE mouse allelic-series paper, and secondary aggregator pages (GARD, MalaCards). **Before curating into the dismech KB, fetch each PMID directly (`just fetch-reference PMID:XXXX`) and verify exact abstract snippets** — per the CLAUDE.md evidence SOP, none of the quotes above should be treated as verified verbatim abstract text; they are paraphrased summaries from secondary sources and require independent confirmation.
2. **Key PMIDs to fetch and verify:** Fregeau et al. 2016 (PMID:27087320, AJHG), Jordan et al. 2018 (PMID:29330883, Human Mutation), the mouse allelic-series paper (candidate PMID:23451234 — verify), and the 2025-26 expanded 54-patient genotype-phenotype/management cohort (ScienceDirect S1098360026008981 — PMID not yet confirmed).
3. **gnomAD constraint metrics (pLI/LOEUF) for RERE** were not independently confirmed and should be pulled directly from the gnomAD browser before use.
4. **CDK19/DEE87** is a distinct, separate gene-disease relationship that surfaced during initial searches under a similar-sounding acronym context; do not conflate it with RERE/NEDBEH during curation (a Named-Entity-Confusion risk given the phenotypic overlap of "neurodevelopmental disorder with brain/eye/heart-adjacent features").

**Full source list:**
- [OMIM #616975 — NEDBEH](https://omim.org/entry/616975)
- [OMIM Clinical Synopsis #616975](https://omim.org/clinicalSynopsis/616975)
- [OMIM #605226 — RERE gene](https://omim.org/entry/605226)
- [GeneReviews — RERE-Related Disorders, NBK538938](https://www.ncbi.nlm.nih.gov/books/NBK538938/)
- [GARD — NEDBEH](https://rarediseases.info.nih.gov/diseases/17902/neurodevelopmental-disorder-with-or-without-anomalies-of-the-brain-eye-or-heart)
- [MalaCards — NEDBEH](https://www.malacards.org/card/neurodevelopmental_disorder_with_or_without_anomalies_of_the_brain_eye_or_heart)
- [NORD/MONDO — NEDBEH](https://rarediseases.org/mondo-disease/neurodevelopmental-disorder-with-or-without-anomalies-of-the-brain-eye-or-heart/)
- [Fregeau et al. 2016, AJHG, PMID:27087320](https://pubmed.ncbi.nlm.nih.gov/27087320/)
- [Jordan et al. 2018, Human Mutation, PMID:29330883](https://onlinelibrary.wiley.com/doi/10.1002/humu.23400)
- [Correction to Jordan et al. 2018, PMC12716887](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12716887/)
- [New genotype-phenotype correlations and management recommendations for RERE variants (2025-26 cohort)](https://www.sciencedirect.com/science/article/abs/pii/S1098360026008981)
- [ClinGen Dosage Sensitivity curation — RERE, HGNC:9965](https://search.clinicalgenome.org/kb/gene-dosage/HGNC:9965)
- [GeneCards — RERE](https://www.genecards.org/card/RERE)
- [PLOS ONE — Allelic series of mice reveals RERE role in organs affected in 1p36 deletions, PMC3581587](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3581587/)
- [1p36 deletion syndrome review (86-patient cohort), PMC10100125](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10100125/)
- [Wikipedia — 1p36 deletion syndrome](https://en.wikipedia.org/wiki/1p36_deletion_syndrome)
- [WHHERE coactivator complex and RA-dependent embryonic symmetry, Nature Communications](https://www.nature.com/articles/s41467-017-00593-6)
- [MedlinePlus — RERE gene](https://medlineplus.gov/genetics/gene/rere/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 5 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:9150137` (2 mentions) - Nuclear receptor repression mediated by a complex containing SMRT, mSin3A, and histone deacetylase.
  - shared terms: gene

Weighed against this report's own most characteristic terms: `rere`, `disorder`, `developmental`, `nedbeh`, `variant`, `anomalie`, `structural`, `phenotype`, `affected`, `cohort`, `gene`, `p36`, `established`, `hearing`, `deletion`, `mechanism`, `disease`, `patient`, `brain`, `neurodevelopmental`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.