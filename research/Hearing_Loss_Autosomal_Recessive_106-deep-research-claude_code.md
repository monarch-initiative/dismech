---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-27T15:07:39.728923'
end_time: '2026-08-27T15:12:56.680060'
duration_seconds: 316.95
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hearing Loss Autosomal Recessive 106
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
  num_turns: 31
  total_cost_usd: 1.3552029999999995
  session_id: 98b3127c-432a-57dc-acc9-774218ba8a79
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 7
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 10
  on_topic: 10
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hearing Loss Autosomal Recessive 106
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hearing Loss Autosomal Recessive 106** covering all of the
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

I now have comprehensive, well-cited data spanning the founding 2015 report through the 2026 expansion study, a canine model, and de novo case. I have enough for a thorough report.

I now have sufficient depth across genetics, mechanism, clinical spectrum, animal models, and management. Compiling the final comprehensive report.

# Hearing Loss, Autosomal Recessive 106 (DFNB106) — Comprehensive Research Report

## 1. Disease Information

**Overview.** Autosomal recessive deafness-106 (DFNB106) is a rare, genetically defined form of **nonsyndromic sensorineural hearing loss** caused by biallelic pathogenic variants in **EPS8L2** (EPS8-Like protein 2), a gene encoding an actin-binding stereocilia protein of cochlear hair cells. Unlike most autosomal recessive nonsyndromic hearing loss (ARNSHL), which is typically congenital, stable, and profound, DFNB106 is distinctive for being **prelingual-to-childhood onset and progressive**, evolving from mild/moderate loss at low frequencies toward severe-to-profound loss, particularly at high frequencies, over years ([Dahmani et al. 2015, PMID:26282398](https://pmc.ncbi.nlm.nih.gov/articles/PMC4539681/); [Owrang et al. 2026, PMID:41514136](https://pmc.ncbi.nlm.nih.gov/articles/PMC12789209/)).

**Key identifiers:**
- **OMIM (phenotype):** #617637 — DEAFNESS, AUTOSOMAL RECESSIVE 106; DFNB106
- **OMIM (gene):** *614988 — EPS8-LIKE PROTEIN 2; EPS8L2
- **Gene locus:** 11p15.13 (NCBI Gene ID 64787; HGNC:21296; UniProt Q9H6S3)
- **MONDO:** MONDO:0033198 (confirmed via ClinVar cross-reference)
- **MedGen:** C4539954
- **ClinVar example record:** RCV000499522 (NM_022772.4(EPS8L2):c.1014del, p.Ser339fs) — Pathogenic, 1-star review
- **Synonyms:** DFNB106; Deafness, autosomal recessive 106; EPS8L2-related hearing loss

**Source of information.** Nearly all information available is derived from a small number of published **family case series/cohort reports** (whole-exome sequencing of individual pedigrees), not large-scale EHR-aggregated data — reflecting the extreme rarity of this specific locus. As of the most recent (2026) synthesis, only **8 families / ~14 affected individuals worldwide** have been reported in the literature ([Owrang et al. 2026, PMID:41514136](https://pmc.ncbi.nlm.nih.gov/articles/PMC12789209/)).

---

## 2. Etiology

**Disease causal factor:** Purely genetic — biallelic (homozygous or compound heterozygous) loss-of-function or spliceogenic variants in **EPS8L2**. There is no known environmental, infectious, or acquired contributor; this is a monogenic Mendelian disorder.

### Genetic risk factors
- **Causal gene:** EPS8L2 (11p15.13). All reported pathogenic alleles predict truncation, nonsense-mediated decay, or aberrant splicing leading to frameshift — i.e., **loss-of-function** as the shared mechanism.
- **Consanguinity as an enabling risk factor:** Several reported families are consanguineous (Algerian second-cousin union; Iranian and Pakistani consanguineous pedigrees), consistent with autosomal recessive transmission and increasing homozygosity risk for a rare allele ([Dahmani et al. 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4539681/); [Wang et al. 2017, PMID:28281779](https://pubmed.ncbi.nlm.nih.gov/28281779/)).
- **Founder effect:** Two unrelated Iranian families in the 2026 report share a **4.17 Mb run of homozygosity** (overlapping interval Chr11:g.197337–4367675, GRCh38) around a recurrent EPS8L2 missense/spliceogenic variant, suggestive of a regional founder allele rather than independent mutation events ([Owrang et al. 2026, PMID:41514136](https://pmc.ncbi.nlm.nih.gov/articles/PMC12789209/)).
- **Gene constraint:** gnomAD v4.0 reports EPS8L2 pLI = 0 and LOEUF = 1.17, indicating the gene is **not strongly constrained against heterozygous loss-of-function** in the general population — consistent with a purely recessive disease mechanism where carriers are unaffected.

### Protective factors
None reported. No modifier alleles, protective variants, or environmental protective exposures have been described for this ultra-rare condition.

### Gene-environment interactions
None documented; no evidence of environmental modulation of onset or severity has been reported.

---

## 3. Phenotypes

All phenotypic data reported to date are **auditory** — no extra-auditory features are described in any published case, consistent with the "nonsyndromic" designation.

| Phenotype | HPO term (suggested) | Onset | Severity/progression | Frequency |
|---|---|---|---|---|
| Bilateral sensorineural hearing loss | HP:0000407 (Sensorineural hearing impairment) | Typically 3–7 yrs (range: presymptomatic infancy to prelingual) | Moderate at onset → severe/profound; **progressive in 5/6 individuals with longitudinal data** | Universal (defining feature) |
| High-frequency sloping hearing loss | HP:0000407 / audiometric pattern | Childhood | Classic pattern in original Algerian and Iranian (Family 2) kindreds | Common |
| **U-shaped audiogram** (novel 2026 finding) | HP:0000365 (Hearing impairment), pattern descriptor | Childhood–adult | Mid-frequency-predominant loss; newly reported in two individuals sharing the c.767C>G, p.(Thr256Arg) variant | 2/9 documented individuals |
| Progressive threshold elevation | — | Years-long | E.g., Algerian sibling: 30→90 dB (age 6) worsening to 40→100 dB (age 10) across frequencies | Predominant pattern |
| Stable/plateaued hearing loss (subset) | — | — | One Iranian proband: only 4 dB PTA change over 10 years ("did not meet the definition of progressive"); one individual stable in her 4th decade after earlier progression | Minority |

**Characteristics:**
- **Age of onset:** Ranges from **presymptomatic at birth** (passing newborn hearing screening) to recognition around 4 years (most common), preschool age, or prelingual in some kindreds. The 2026 study documents the **first pre-symptomatic case**: a German child who passed newborn screening but developed measurable loss by ~23 months, confirming that normal hearing at birth is compatible with the genotype ([Owrang et al. 2026, PMID:41514136](https://pmc.ncbi.nlm.nih.gov/articles/PMC12789209/)).
- **Severity:** Moderate-to-severe/profound, variable across families and even within the same variant.
- **Progression:** Documented in the majority (5/6) of individuals with serial audiograms — an unusual feature for ARNSHL, most of which (e.g., GJB2-related) is congenital and stable.
- **Speech outcomes:** Speech discrimination scores of 70–96% reported in the two most recent Iranian probands, correlating with moderate rather than profound loss at last follow-up.

**Quality of life:** Not formally measured with standardized instruments (EQ-5D/SF-36) in any report; clinical narrative notes affected children use hearing aids, and delayed language/speech development was observed in at least one case ("unclear language" and non-response to sound from age 2, Family 1 proband).

---

## 4. Genetic/Molecular Information

### Causal gene and variant catalog
All known pathogenic EPS8L2 variants (NM_022772.4 transcript; 21 exons, 715-aa protein):

| Variant (cDNA) | Protein | Type | Zygosity/family | Source |
|---|---|---|---|---|
| c.1014delC | p.Ser339Alafs*15 | Frameshift (exon 12) | Homozygous — Algerian founding family | [PMID:26282398](https://pmc.ncbi.nlm.nih.gov/articles/PMC4539681/) |
| c.737delC | frameshift | Frameshift (Pakistani family F11) | Homozygous, consanguineous | [Wang et al. 2017, PMID:28281779](https://pubmed.ncbi.nlm.nih.gov/28281779/) |
| c.738delA / p.(Val247Cysfs*6) | Frameshift | Exon 9 | Cited as supporting evidence for exon-9 biological importance | [Owrang et al. 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC12789209/) |
| c.818_827dup | p.(Ala279Glyfs*36) | Frameshift (exon 10) | Compound het, maternal allele — German Family 1 (novel) | PMID:41514136 |
| c.1430dup | p.(Val478Serfs*25) | Frameshift (exon 15) | Compound het, paternal allele — German Family 1 (previously reported) | PMID:41514136 |
| c.1878C>A | p.(Tyr626Ter) | **First nonsense variant** (exon 19, SAM/PNT domain) | Homozygous — Iranian Family 2 | PMID:41514136 |
| c.767C>G | p.(Thr256Arg) | **First missense variant**, shown by minigene assay to cause complete exon 9 skipping (r.701_768del, p.(Gly234Alafs*55)) | Homozygous — Iranian Families 3 & 4 (founder allele) | PMID:41514136 |
| c.357_361dupGGTGC | p.(Gln121Argfs*67) | Frameshift, *de novo* on one allele | Compound het (with c.1317dupG) — 39-year-old male, first de novo-containing case | [Gan et al. 2026, PMID:41578500] |
| c.1317dupG | p.(Leu440Alafs*63) | Frameshift, maternally inherited | Compound het (above) | PMID:41578500 |

**Variant classification:** All reported variants are **pathogenic or likely pathogenic** per ACMG/AMP criteria (e.g., the spliceogenic missense classified PM2_P, PM3_M, PVS1_S). All converge mechanistically on **loss of function** — via frameshift/premature termination, nonsense-mediated decay, or exon skipping.

**Population frequency:** Pathogenic EPS8L2 alleles are essentially absent from population databases — the recurrent c.767C>G founder variant was found in only **1 carrier among ~40,000 exomes** (UCL Queen Square database) and was **absent from gnomAD, TopMed, and All of Us** ([PMID:41514136](https://pmc.ncbi.nlm.nih.gov/articles/PMC12789209/)), underscoring extreme rarity.

**Somatic vs. germline:** All variants are germline; no somatic mosaicism reported.

**Functional consequence:** Uniformly loss-of-function — truncated/absent protein (frameshift/nonsense with NMD) or exon-skipping-induced frameshift (spliceogenic missense). No gain-of-function or dominant-negative alleles have been described.

### Modifier genes
None identified to date.

### Epigenetic information
Not investigated/reported for this gene-disease relationship.

### Chromosomal abnormalities
None reported; disease is caused by small intragenic variants, not structural/copy-number changes.

---

## 5. Environmental Information
No environmental factors, lifestyle factors, or infectious triggers have been implicated. DFNB106 is a purely monogenic disorder with no reported gene-environment modulation.

---

## 6. Mechanism / Pathophysiology

### Protein structure and localization
EPS8L2 (EPS8 Signaling Adaptor L2) is a **715-amino-acid, F-actin-binding member of the EPS8 protein family** (EPS8, EPS8L1, EPS8L2, EPS8L3), containing a phosphotyrosine-binding (PTB) domain, an SH3 domain, an effector domain, and (per the 2026 paper) a SAM/pointed (SAM/PNT) domain near the C-terminus. In cochlear and vestibular hair cells, EPS8L2 localizes specifically to the **tips of the shorter and intermediate rows of stereocilia**, distinguishing it from EPS8, which localizes to and elongates the **tallest** stereocilia row ([Dahmani et al. 2015, PMID:26282398](https://pmc.ncbi.nlm.nih.gov/articles/PMC4539681/); [Furness et al. 2013 PNAS, PMID:23918390](https://www.pnas.org/doi/10.1073/pnas.1304644110)).

### Causal chain (cellular process → tissue → organism)
1. **Molecular:** Loss-of-function EPS8L2 variant → absent or truncated actin-binding adaptor protein at stereocilia tips.
2. **Cellular:** Failure to maintain (not initially build) the actin core of the short/intermediate stereocilia rows in mature hair cells → gradual disorganization and shortening of these rows, with variable width abnormalities.
3. **Tissue:** Progressive deterioration of the hair bundle "staircase" architecture required for mechanotransduction in cochlear (and vestibular) hair cells of the organ of Corti.
4. **Organism:** Progressive, typically postlingual-onset sensorineural hearing loss, sloping toward high frequencies (or U-shaped in the spliceogenic-variant cases), because mechanotransduction becomes progressively impaired as the affected stereocilia rows degrade with age/use rather than failing to form in the first place.

This gives DFNB106 a mechanistically distinct signature versus most ARNSHL: **EPS8 loss causes early, static, profound deafness (failure to elongate stereocilia in the first place — DFNB102)**, whereas **EPS8L2 loss causes late-onset, progressive deafness (failure to *maintain* mature stereocilia)** — a "maintenance vs. morphogenesis" dichotomy within one paralog family ([Furness et al. 2013](https://www.pnas.org/doi/10.1073/pnas.1304644110); [EPS8/DFNB102 review, PMID not extracted, PMC9837036]).

### Molecular pathway
EPS8L2 acts through **actin cytoskeleton dynamics regulation** — bundling/capping activity at stereocilia tips, and (based on EPS8-family biology) potential modulation of Rac/SOS1-linked signaling relevant to membrane/cytoskeletal remodeling (GeneCards annotation).

**Suggested GO terms:**
- GO:0051017 — actin filament bundle assembly
- GO:0032420 — stereocilium
- GO:0003785 — actin monomer binding
- GO:0060088 — auditory receptor cell stereocilium organization

**Suggested CL terms:**
- CL:0000601 — inner hair cell of Corti's organ (or cochlear outer/inner hair cell, CL:0000589)

**Suggested UBERON terms:**
- UBERON:0001844 — cochlea / organ of Corti
- UBERON:0009865 — stereocilium bundle (if available) or UBERON:0002106 (spiral organ)

### Molecular profiling / advanced technologies
- **Zebrafish whole-mount in situ hybridization (WISH):** *eps8l2* is expressed in the **otic vesicle** — specifically the presumptive utricular and saccular maculae — and in the **pronephric duct**; later stages show broader otic-vesicle expression plus scattered spinal cord expression ([Owrang et al. 2026, PMID:41514136](https://pmc.ncbi.nlm.nih.gov/articles/PMC12789209/)).
- **Minigene/splicing assay:** For the c.767C>G missense variant, RT-PCR of a minigene construct demonstrated **complete exon 9 skipping**, converting a presumed benign missense change into a functional null allele — directly confirming spliceogenicity by wet-lab assay rather than in silico prediction alone (only 2/6 splice-prediction algorithms had flagged it).
- No transcriptomic, proteomic, or single-cell datasets specific to human EPS8L2-deficient tissue have been published (human inner-ear tissue is not accessible for biopsy).

---

## 7. Anatomical Structures Affected

- **Organ level:** Inner ear only (cochlea and, to a lesser functional extent demonstrated in mouse, the vestibular system) — no other organ system involvement reported (nonsyndromic).
- **Tissue/cell level:** Cochlear and vestibular **hair cells** (CL:0000601/CL:0000602), specifically their **stereocilia bundles**.
- **Subcellular level:** Stereocilia actin core/tip complex — the specific site of EPS8L2 localization (GO:0005884 actin filament; GO:0032420 stereocilium).
- **Localization:** Bilateral, symmetric involvement in all reported human cases (no unilateral or asymmetric presentations documented).

---

## 8. Temporal Development

- **Onset:** Ranges from prelingual/infantile to early childhood (~4–7 years most typical); one documented **presymptomatic** case with normal newborn hearing screening followed by measurable loss detected by ~23 months.
- **Onset pattern:** Insidious/gradual rather than acute.
- **Progression:** **Progressive in the majority of longitudinally followed cases (5/6)** — an atypical feature for ARNSHL. Progression can continue into adulthood (one individual "in her fourth decade" with prior progression now described as stable over the last decade of follow-up), suggesting eventual plateauing in at least some individuals.
- **Disease course pattern:** Chronic, generally progressive-then-potentially-stabilizing; not episodic or relapsing-remitting.
- **Critical period:** The 2026 paper explicitly frames early infancy/toddlerhood as a **"therapeutic window"** — before stereocilia degeneration is complete — for any future molecular intervention, based on parallel work in EPS8 (DFNB102) mouse gene-therapy models (see Treatment section).

---

## 9. Inheritance and Population

- **Inheritance pattern:** Autosomal recessive (both homozygous and compound heterozygous genotypes documented).
- **Penetrance:** Appears complete for biallelic loss-of-function genotypes, though age-dependent (phenotype may not be measurable at birth).
- **Expressivity:** Variable — age of onset, severity, rate of progression, and audiogram shape (sloping vs. U-shaped) differ even among carriers of the same variant (e.g., within the shared founder-variant Iranian families).
- **Genetic anticipation:** Not applicable/not reported (not a repeat-expansion disorder).
- **Germline mosaicism:** Not reported.
- **Founder effects:** A shared ~4.17 Mb homozygous haplotype around c.767C>G in two ostensibly unrelated Iranian families strongly suggests a regional founder allele.
- **Consanguinity:** A major contributing factor in most reported pedigrees (Algerian, Iranian, Pakistani).
- **Carrier frequency:** Cannot be reliably estimated — pathogenic alleles are essentially unseen in gnomAD/TopMed/All of Us; the disease is considered ultra-rare.
- **Epidemiology:** No formal prevalence/incidence estimate exists. Only **8 families (~14 affected individuals)** have been published worldwide as of the January 2026 update ([Owrang et al. 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC12789209/)), spanning Algeria, Pakistan (≥2 families), Iran (≥3 families), Germany, and China (1 case). For context, ARNSHL overall accounts for ~80% of genetic nonsyndromic hearing loss, with GJB2/DFNB1 explaining roughly 16.9% globally (up to 27.1% in European cohorts) and >85 genes implicated overall in ARNSHL — DFNB106 is a very minor contributor to this landscape.
- **Geographic/ethnic distribution:** Cases reported across North Africa (Algeria), South Asia (Pakistan), the Middle East (Iran), Europe (Germany, with mixed Greek/German parentage), and East Asia (China) — no single predominant population, though consanguineous-marriage-practicing populations are overrepresented, as expected for rare recessive disease ascertainment.
- **Sex ratio:** No sex predilection reported (X-linked/mitochondrial mechanisms excluded; autosomal recessive).

---

## 10. Diagnostics

- **Clinical/audiologic tests:** Standard pure-tone audiometry (air and bone conduction across 125 Hz–8 kHz), speech reception threshold and speech discrimination testing. Serial audiometry over years is essential to document the characteristic progression.
- **Newborn hearing screening:** May be **passed** (normal) despite carrying a biallelic pathogenic EPS8L2 genotype — a critical diagnostic pitfall, since a normal newborn screen does not rule out DFNB106 given its progressive, sometimes-delayed onset.
- **Genetic testing:**
  - **Whole-exome sequencing (WES)** has been the discovery and diagnostic method for essentially all reported cases (candidate-gene approach after excluding GJB2), reflecting how rare/unrecognized this gene is on standard hearing-loss panels.
  - **Targeted deafness gene panels** may include EPS8L2 (e.g., listed on the Genomics England PanelApp "Monogenic hearing loss" panel) but coverage varies by lab.
  - **Autozygosity/homozygosity mapping** has been used in consanguineous families to define candidate intervals and detect founder alleles.
  - **Minigene/splicing functional assays** are recommended when a missense variant is discovered, given the demonstrated risk of missense variants (e.g., c.767C>G) acting as cryptic splice-disrupting alleles rather than simple amino-acid substitutions — routine in silico tools alone missed this in most predictors.
- **Differential diagnosis:** Other genetic causes of progressive, nonsyndromic, prelingual-to-childhood-onset sensorineural hearing loss (e.g., STRC-related, TMPRSS3-related, OTOF-related, other DFNB loci), and syndromic causes should be excluded via broader panel/exome testing and clinical evaluation (absence of other organ involvement supports "nonsyndromic" classification).
- **Screening:** No population-level screening program exists for EPS8L2 given its rarity; identification is via diagnostic exome/genome sequencing after clinical suspicion (progressive ARNSHL, especially with a family history or normal-but-later-failing newborn screen).

---

## 11. Outcome/Prognosis

- **Mortality:** None — DFNB106 causes isolated hearing loss with no reported effect on life expectancy or systemic morbidity.
- **Morbidity:** Communication/speech-language developmental impact from progressive hearing loss, particularly if diagnosis and intervention (hearing aids) are delayed; documented delayed speech/language recognition in at least one proband.
- **Disease course:** Progressive threshold elevation over years to decades in most individuals; in a minority, progression appears to plateau (documented stability over a decade in an adult in her 4th decade of life; near-stability over 10 years in one Iranian proband).
- **Prognostic factors:** Earlier recognition and hearing-aid fitting appear associated with better functional outcomes (standard audiology principle); no genotype-severity correlation has yet been established across the small number of reported variants, though the two individuals with the spliceogenic c.767C>G variant shared a distinctive U-shaped audiogram, hinting at a possible variant-specific pattern.
- **General ARNSHL cochlear implant data (not DFNB106-specific, given no published case yet requiring implantation):** Progressive vs. congenital profound hearing loss show no significant difference in cochlear implant outcomes; genetic etiology overall does not reduce implant benefit, with performance driven mainly by age at implantation and duration of hearing loss prior to intervention.

---

## 12. Treatment

**No disease-specific or FDA-approved therapy exists for DFNB106.** Management is symptomatic/supportive, following standard practice for progressive sensorineural hearing loss:

- **Hearing aids** (NCIT:C15302 is for physical therapy; the relevant NCIT concept is closer to "Hearing Aid" under assistive devices) — used by affected children as soon as loss is documented; one German proband fitted with aids from young childhood, his presymptomatic sibling scheduled for first aids at 2 years 8 months once threshold elevation was confirmed.
- **Cochlear implantation** — not yet reported for a confirmed DFNB106 case in the literature, but by extrapolation from general ARNSHL cochlear-implant literature, would be expected to be effective if hearing loss progresses to severe/profound levels, with outcomes driven by implantation timing rather than genotype per se.
- **Genetic counseling** (NCIT:C15240) — recommended given the autosomal recessive inheritance, ~25% recurrence risk per pregnancy for carrier couples, and the discovery of a Fars-region Iranian founder allele relevant to regional carrier screening.
- **Speech and audiologic rehabilitation** (NCIT:C159273 speech therapy) — standard adjunct for children with progressive hearing loss.

### Experimental/preclinical therapeutic direction ("therapeutic window")
The 2026 Owrang et al. paper explicitly discusses gene-therapy precedent from the sister gene EPS8 (DFNB102): a preclinical AAV-mediated (Anc80L65 serotype) EPS8 gene-replacement study in *Eps8* knockout mice **rescued hair-bundle structure but not functional hearing**, and rescue efficacy dropped sharply if AAV delivery was delayed past **postnatal day 1–2** ("when delayed to postnatal day 3, almost no recovery was observed"). The authors argue this underscores the urgency of **early molecular diagnosis** for EPS8L2, since its **later, more gradual onset** (compared to EPS8/DFNB102's early profound congenital deafness) may in principle offer a longer intervention window for a future EPS8L2-directed gene therapy — though no such therapy has yet been developed or tested for EPS8L2 itself. This is framed as a rationale for early genetic testing/referral, not as an available treatment.

No clinical trials (NCT) specific to EPS8L2/DFNB106 were identified in the search.

---

## 13. Prevention

- **Primary prevention:** Not applicable in the biological sense (no modifiable risk factor); the only "primary prevention" lever is **reproductive genetic counseling** for known-carrier couples (e.g., preimplantation genetic diagnosis or prenatal testing where a familial variant is known), particularly relevant in consanguineous unions or populations carrying an identified founder allele (e.g., the Fars, Iran region).
- **Secondary prevention/early detection:** Universal **newborn hearing screening** remains valuable but is explicitly shown to be insufficient alone for DFNB106, since affected infants can pass screening and only develop measurable loss in the second year of life — supporting a case for **genetic newborn screening or expanded gene panels** in at-risk families (e.g., known familial variant, consanguinity, family history of progressive childhood-onset ARNSHL) to enable close audiologic monitoring even after a normal screen.
- **Tertiary prevention:** Early hearing-aid fitting and speech-language intervention to minimize the developmental impact of progressive threshold elevation.
- **Genetic/carrier screening:** Expanded carrier screening panels in consanguineous or founder populations could, in principle, include EPS8L2, though it is not yet part of standard commercial hearing-loss carrier panels given its rarity.

---

## 14. Other Species / Natural Disease

**This is one of the best-documented sections for DFNB106, given a notable naturally occurring canine model:**

- **Rhodesian Ridgeback dog — early-onset adult deafness:** A genome-wide association study (23 affected vs. 162 control dogs) followed by Sanger sequencing identified a **12-bp in-frame deletion in EPS8L2**, segregating in an **autosomal recessive** pattern; "all affected dogs were homozygous for the deletion" ([Kawakami et al. 2022, PMID:35385474](https://pubmed.ncbi.nlm.nih.gov/35385474/), *PLoS ONE*). This represents a **spontaneous, naturally occurring veterinary phenocopy** of human DFNB106 and is a strong translational/comparative model, since it arose without laboratory engineering and mirrors the human recessive, hair-cell-maintenance mechanism.
  - Suggested NCBI Taxon: NCBITaxon:9615 (Canis lupus familiaris); breed identifiers via VBO would apply to "Rhodesian Ridgeback."
- **Mouse (Mus musculus, engineered knockout):** *Eps8l2*-null mice (targeted knockout, not naturally occurring) — see Model Organisms below.
- **No other species' natural disease has been reported** for EPS8L2 to date (unlike some hearing-loss genes with described feline or bovine natural mutants).
- **Comparative biology:** The EPS8 gene family (EPS8, EPS8L1, EPS8L2, EPS8L3) and its stereocilia-tip actin-regulatory role are evolutionarily conserved across mammals, underpinning why the mouse, dog, and human phenotypes converge on the same "progressive stereocilia maintenance failure" mechanism rather than divergent pathology.
- **Zoonotic potential:** Not applicable — this is a non-infectious monogenic disorder.

---

## 15. Model Organisms

| Model | Type | Key findings | Source |
|---|---|---|---|
| **Mouse (*Eps8l2* knockout)** | Engineered, germline null (MGI:2138828) | **Late-onset, progressive, severe hearing loss** (especially high frequencies) due to gradual disorganization of cochlear hair bundles; stereocilia of the **tall row become shorter and fewer**, while middle and short rows are relatively preserved — the mirror image of the human/dog phenotype pattern but consistent with a stereocilia-maintenance (not morphogenesis) defect. Directly recapitulates human progressive, postnatal-onset hearing loss. | [Furness et al. 2013, PNAS, PMID:23918390](https://www.pnas.org/doi/10.1073/pnas.1304644110) |
| **Zebrafish (*Danio rerio*)** | Expression study (WISH), not a knockout/phenotype model to date | *eps8l2* expressed in otic vesicle (utricular/saccular macula precursors) and pronephric duct during development; supports conserved otic relevance across vertebrates but no functional loss-of-function zebrafish model has yet been published. | [Owrang et al. 2026, PMID:41514136](https://pmc.ncbi.nlm.nih.gov/articles/PMC12789209/) |
| **Dog (Rhodesian Ridgeback)** | Naturally occurring, spontaneous | See "Other Species" above — a naturally arising, homozygous 12-bp in-frame EPS8L2 deletion causing early-onset adult deafness; valuable as an outbred, naturally occurring large-animal model with autosomal recessive transmission matching the human disease exactly. | [Kawakami et al. 2022, PMID:35385474] |

**Model limitations:** The mouse knockout shows a somewhat different stereocilia-row pattern (tall row affected) than what would be predicted from EPS8L2's normal tip localization at short/intermediate rows in wild-type animals — this apparent paradox is discussed in the primary literature but not fully resolved, and represents an open question about full concordance between mouse structural findings and the exact human audiometric/histopathologic correlate (human temporal bone histopathology is unavailable). No iPSC-derived otic organoid model of EPS8L2 deficiency has yet been published. Preclinical AAV gene-therapy rescue data exist only for the paralogous gene EPS8 (DFNB102 mouse model), not yet for EPS8L2 itself, and even that related rescue restored structure without restoring functional hearing — an important caveat when extrapolating "therapeutic window" arguments to EPS8L2.

---

## Summary of Key Citations

1. Dahmani M, et al. "EPS8L2 is a new causal gene for childhood onset autosomal recessive progressive hearing loss." *Orphanet J Rare Dis.* 2015. PMID:[26282398](https://pmc.ncbi.nlm.nih.gov/articles/PMC4539681/) — founding report (Algerian family).
2. Furness DN, et al. "Progressive hearing loss and gradual deterioration of sensory hair bundles in the ears of mice lacking the actin-binding protein Eps8L2." *PNAS.* 2013;110(34):13898–13903. PMID:[23918390](https://www.pnas.org/doi/10.1073/pnas.1304644110) — mouse knockout, mechanistic basis.
3. Wang R, et al. "Molecular Analysis of Twelve Pakistani Families with Nonsyndromic or Syndromic Hearing Loss." *Genet Test Mol Biomarkers.* 2017. PMID:[28281779](https://pubmed.ncbi.nlm.nih.gov/28281779/) — second EPS8L2 family (Pakistan, c.737delC).
4. Kawakami T, et al. "Early onset adult deafness in the Rhodesian Ridgeback dog is associated with an in-frame deletion in the EPS8L2 gene." *PLoS One.* 2022. PMID:[35385474](https://pubmed.ncbi.nlm.nih.gov/35385474/) — canine natural model.
5. Owrang [lead author], et al. "Expansion of Molecular and Clinical Aspects of EPS8L2 (DFNB106)-Associated Hearing Loss Emphasizes a Potential Therapeutic Window." *Mol Neurobiol.* 2026 (online Jan 2026). PMID:[41514136](https://pmc.ncbi.nlm.nih.gov/articles/PMC12789209/) — most comprehensive, current synthesis (4 new families, splicing functional assay, therapeutic-window discussion, zebrafish expression).
6. Gan H, et al. "Identification and phased de novo mutation of the EPS8L2 gene in a patient with progressive hearing loss." *Medicine (Baltimore).* 2026. PMID:41578500 — first compound-het case including a de novo allele.
7. OMIM #617637 (DFNB106) and *614988 (EPS8L2) — https://omim.org/entry/617637 ; https://omim.org/entry/614988
8. ClinVar RCV000499522 — MONDO:0033198 cross-reference.

**Data gaps to flag explicitly for curation:** No published human temporal-bone histopathology; no confirmed cochlear-implant outcome case specific to DFNB106; no iPSC/organoid model; no EPS8L2-specific gene therapy (only paralog EPS8 preclinical data exists); prevalence/incidence figures are not formally estimated (only cumulative case counts across published families).

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 10 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.