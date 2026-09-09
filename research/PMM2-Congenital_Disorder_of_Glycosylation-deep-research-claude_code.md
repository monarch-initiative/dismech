---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-27T18:52:18.139142'
end_time: '2026-08-27T18:56:11.989350'
duration_seconds: 233.85
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: PMM2-Congenital Disorder of Glycosylation
  mondo_id: ''
  category: ''
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
  web_search_requests: 13
  num_turns: 15
  total_cost_usd: 1.0915857999999998
  session_id: 00937d02-a143-56ac-a731-3747f9ee4c64
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 41
reference_validation:
  total_references: 19
  verified: 19
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 19
  on_topic: 15
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PMM2-Congenital Disorder of Glycosylation
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **PMM2-Congenital Disorder of Glycosylation** covering all of the
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

I'll research PMM2-CDG using web search to gather current, well-cited information for this comprehensive report.

I now have sufficient research material to write a comprehensive, well-cited report. Let me compile it.

# PMM2-Congenital Disorder of Glycosylation (PMM2-CDG): Comprehensive Research Report

## 1. Disease Information

### Overview
PMM2-CDG (formerly known as **CDG-Ia** or "carbohydrate-deficient glycoprotein syndrome type I") is an autosomal recessive inborn error of metabolism caused by biallelic pathogenic variants in *PMM2*, the gene encoding phosphomannomutase 2. It is **the most common and best-characterized disorder of N-linked protein glycosylation in humans**, accounting for roughly 60% of all diagnosed CDG cases, with more than 1,000 patients reported worldwide across >900 published cases ([Frontiers in Endocrinology, 2025](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2025.1594118/full); [Orphanet](https://www.orpha.net/en/disease/detail/79318)). PMM2-CDG is a multisystem disease: because essentially all secreted and membrane glycoproteins require N-glycosylation for correct folding, stability, and trafficking, defective glycosylation produces a broad, variable phenotype spanning neurological, gastrointestinal, hepatic, cardiac, renal, coagulation, endocrine, and skeletal systems.

### Key Identifiers
| Resource | Identifier |
|---|---|
| OMIM | **#212065** (Congenital Disorder of Glycosylation, Type Ia) |
| Gene (OMIM) | **PMM2**, *601785* |
| Orphanet | **ORPHA:79318** |
| MONDO | MONDO:0015286 (PMM2-CDG) |
| ICD-10 | E77.8 (Other disorders of glycoprotein metabolism) |
| ICD-11 | 5C56.0Y / related metabolic disorder codes |
| HGNC | PMM2, HGNC:9115 |
| MeSH | Congenital Disorders of Glycosylation |

Source: [OMIM #212065](https://omim.org/entry/212065); [GeneReviews — PMM2-CDG](https://www.ncbi.nlm.nih.gov/books/NBK1110/)

### Synonyms / Alternative Names
- CDG-Ia / CDG1A / CDGS1
- Congenital disorder of glycosylation type Ia
- Phosphomannomutase 2 deficiency
- Carbohydrate-deficient glycoprotein syndrome type I (historical)
- Jaeken syndrome (historical eponym, after Jaak Jaeken who first described the disorder in 1980)

### Data Source Character
Most published information derives from **aggregated case series and multicenter cohort studies** (e.g., the 96-patient French cohort, the 50-patient coagulation cohort, and international registries such as the Frontiers in Congenital Disorders of Glycosylation Consortium (FCDGC) natural history study), rather than raw individual EHR mining. Orphanet and OMIM entries synthesize published cohort and case-report literature.

---

## 2. Etiology

### Disease Causal Factors
PMM2-CDG is caused **exclusively by biallelic (compound heterozygous or homozygous) pathogenic variants in *PMM2*** (chromosome 16p13.2), which encodes phosphomannomutase 2, the enzyme that isomerizes mannose-6-phosphate (M6P) to mannose-1-phosphate (M1P) — an essential precursor for GDP-mannose and dolichol-phosphate-mannose synthesis required for N-glycan assembly ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1110/); [PMID 22956764](https://pubmed.ncbi.nlm.nih.gov/22956764/)). There is no known environmental or infectious causal pathway — this is a purely monogenic mechanistic disease.

### Genetic Risk Factors
- **Causal variants**: >120 pathogenic *PMM2* variants have been reported (missense predominating, with fewer nonsense, splice-site, and small indel variants). Missense predominance reflects that complete loss of PMM2 activity is embryonic lethal in humans (consistent with mouse data below).
- **Most common pathogenic alleles**:
  - **c.422G>A (p.Arg141His / R141H)** — the single most frequent PMM2-CDG allele. It has **no detectable residual enzymatic activity** and has never been observed in homozygosity in a living patient, implying that R141H homozygosity is embryonic/fetal lethal. gnomAD heterozygote carrier frequency is ~0.39% overall (891/224,376), rising to ~0.84% in the Finnish subpopulation ([ClinVar VCV000007706](https://www.ncbi.nlm.nih.gov/clinvar/variation/7706/)).
  - **c.357C>A/G (p.Phe119Leu / F119L)** — retains ~25% residual enzymatic activity, likely due to impaired dimerization; among 18 Danish CDG-Ia patients, F119L together with R141H accounted for 88% of alleles.
  - The compound heterozygote genotype **R141H/F119L** is the most frequent genotype worldwide and is the genotype modeled in the leading mouse model (see Section 15).
- Genotype–phenotype correlation is imperfect but broadly: genotypes combining two severe/null alleles are rarer (often embryonic lethal or very severe), while a null allele paired with a hypomorphic (partial-activity) allele like F119L is compatible with survival across the full clinical spectrum ([PMC12042452, "genotype–phenotype correlations in PMM2-CDG"](https://pmc.ncbi.nlm.nih.gov/articles/PMC12042452/)).

### Protective/Modifier Factors
No validated protective genetic variants are established. Hypomorphic alleles with higher residual PMM2 activity (vs. null alleles) act as de facto "protective" modifiers of severity in trans-heterozygotes.

### Environmental Risk Factors
None established — this is a purely genetic (autosomal recessive, biallelic) disease with no known environmental, occupational, or lifestyle contributors to disease occurrence. (Environmental factors can modulate the *severity* of acute decompensations — e.g., febrile illness, surgery, and fasting can precipitate stroke-like episodes, bleeding, or hypoglycemic crises — but do not cause the underlying disease.)

### Gene-Environment Interactions
Not a primary feature of this monogenic disorder; the closest analog is that intercurrent physiologic stress (infection, fasting, surgery) interacts with baseline coagulopathy and hypoglycemia susceptibility to precipitate acute complications.

---

## 3. Phenotypes

PMM2-CDG phenotypes span a wide severity spectrum from neonatal death to mild adult presentation. Below are phenotype categories with suggested HPO terms.

### Neurological
| Phenotype | Frequency/Onset | Suggested HPO |
|---|---|---|
| Cerebellar hypoplasia (present at birth, "figure-8" or "batwing" cerebellum on MRI) → progressive cerebellar atrophy | Present in nearly all infants at birth; progresses | HP:0001321 (Cerebellar hypoplasia), HP:0001272 (Cerebellar atrophy) |
| Hypotonia | Common, early infancy | HP:0001252 |
| Ataxia/dysmetria/tremor | Progressive, childhood onward | HP:0001251 (Ataxia), HP:0001337 (Tremor) |
| Abnormal (esotropic/roving) eye movements, strabismus | Early, frequent | HP:0000486 (Strabismus), HP:0000496 (Abnormal eye movements) |
| Psychomotor delay / intellectual disability (mild–moderate, usually non-progressive plateau) | Infancy/childhood | HP:0001263, HP:0001249 |
| Peripheral neuropathy | Later childhood/adult | HP:0009830 |
| Seizures | Subset | HP:0001250 |
| Stroke-like episodes (SLEs) | ~18% of cohort, often provoked by febrile illness | HP:0002401 |

Source: [PMC12042452](https://pmc.ncbi.nlm.nih.gov/articles/PMC12042452/); [PMC10530657 (coagulation cohort)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10530657/); Neurology case report on unusual eye movements.

### Dysmorphic / Physical
- **Inverted/hypoplastic nipples** and **abnormal fat distribution/lipodystrophy** (suprapubic fat pads, "orange-peel" skin over buttocks) — considered classic, near-pathognomonic early signs (HP:0003186 Inverted nipples; HP:0009026 Abnormal subcutaneous fat tissue distribution).
- Facial dysmorphism (large ears, high forehead) — HP:0000238 etc.

### Gastrointestinal/Hepatic
- Failure to thrive, feeding difficulty/vomiting, enteropathy — HP:0001508, HP:0011968
- Hepatomegaly, elevated transaminases, hepatic fibrosis — HP:0002240, HP:0002910
- Recurrent pancreatitis (subset) — HP:0001733

### Cardiac
- Pericardial effusion, hypertrophic cardiomyopathy — HP:0001636, HP:0001700

### Renal
- Nephrotic-range proteinuria/renal cysts in a subset — HP:0000100

### Hematologic (laboratory abnormalities)
- Coagulopathy from hypoglycosylated clotting factors/inhibitors — see Section 6/10. Antithrombin deficiency is the single most common lab abnormality, found in **83.3% of patients**, with activity <50% (normal 80–130%) in 62.5% of the cohort ([PMC10530657](https://pmc.ncbi.nlm.nih.gov/articles/PMC10530657/)). Also common: Factor XI deficiency, protein C deficiency, protein S and Factor IX deficiency (less common).
- Bleeding symptoms in 16%; thrombosis in 10% of a large cohort.

### Endocrine (laboratory/clinical)
- Hypothyroidism (glycosylation-dependent TSH/thyroglobulin dysfunction)
- Hyperinsulinemic hypoglycemia — reported in ~2.5% of a 933-patient PMM2-CDG review, with hyperinsulinism confirmed in 43% of the hypoglycemic subgroup; diazoxide-responsive in most treated cases ([PMC7012739](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7012739/); [PMC9680396](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9680396/))
- Hypogonadotropic hypogonadism / abnormal FSH-LH glycoforms in females (elevated FSH from birth, later ovarian failure)
- Growth hormone axis abnormalities (short stature) — reflecting IGFBP-3 hypoglycosylation ([Frontiers Endocrinology 2025](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2025.1594118/full))

### Phenotype Characteristics
- **Onset**: Congenital/neonatal-infantile in the classic (and most common) presentation; a distinct **late-onset/adult phenotype** is increasingly recognized, sometimes presenting primarily with cerebellar ataxia or stroke-like episodes without the classic infantile multisystem picture ([Orphanet Journal of Rare Diseases, 29 French adult patients](https://ojrd.biomedcentral.com/articles/10.1186/s13023-014-0207-4)).
- **Severity/progression**: Highly variable — ranges from infants who die in the first year of life (severe multisystem/hydrops-like presentation with cardiac/renal/hepatic failure) to mildly affected adults with only ataxia and mild cognitive involvement. Three recognized natural-history stages: **(1) infantile multisystem type**, **(2) late-infantile/childhood ataxia–intellectual disability type (ages 3–10)**, **(3) adult stable disability type** ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1110/)).
- **Course**: Neurological (cerebellar) disease is generally non-progressive after early childhood plateau in survivors, though cerebellar atrophy on imaging can progress radiographically even as clinical function stabilizes ([PMC8360885, activities of daily living correlates](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8360885/)).

### Quality of Life
A cross-sectional adaptive functioning study found PMM2-CDG substantially impacts adaptive functioning across the lifespan and imposes significant parental stress, particularly around motor and communication domains ([Scientific Reports, 2023](https://www.nature.com/articles/s41598-023-49518-y), PMC10739927). A patient-reported outcomes study (Orphanet J Rare Dis, 2022) identified fatigue, gastrointestinal symptoms, and mobility/ataxia as top patient/caregiver concerns not always captured by clinician-rated instruments ([OJRD 2022](https://ojrd.biomedcentral.com/articles/10.1186/s13023-022-02551-y)).

---

## 4. Genetic/Molecular Information

### Causal Gene
- **PMM2** (phosphomannomutase 2), HGNC:9115, chromosome 16p13.2, OMIM *601785. Encodes a cytosolic enzyme that functions as a homodimer.

### Variant Classification and Type
- Predominantly **missense** variants (reflecting embryonic lethality of complete null/null genotypes); fewer nonsense, frameshift, and splice-site alleles.
- ClinVar/ACMG classification: Both R141H and F119L are classified **Pathogenic** ([ClinVar RCV000008145](https://www.ncbi.nlm.nih.gov/clinvar/RCV000008145/)).
- Functional consequences are predominantly **hypomorphic loss-of-function** — destabilizing the protein fold/reducing dimerization/catalytic efficiency rather than classic null alleles, consistent with the observation that complete biallelic null genotypes are not observed in living patients.

### Allele Frequency
- R141H heterozygote frequency in gnomAD: ~0.39% overall population, ~0.84% in Finnish subpopulation.
- Population-based carrier-frequency modeling (using gnomAD allele frequencies across all known pathogenic *PMM2* alleles) estimates a theoretical birth prevalence as high as 1:20,000, though observed/diagnosed birth prevalence is substantially lower (1:77,000–1:286,000 in some analyses; see Section 9) — a gap attributed to embryonic lethality of severe genotype combinations and underdiagnosis ([PMC8383291](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8383291/)).

### Somatic vs. Germline
Exclusively **germline** — PMM2-CDG is a classic Mendelian recessive disorder with no somatic mosaicism subtype reported as clinically significant.

### Modifier Genes
**MPI** (mannose phosphate isomerase) activity ratio relative to PMM2 modulates response to mannose-based therapies (the PMM2:MPI ratio determines whether supplemental mannose is shunted productively into the pathway or diverted) — this is a pharmacologically relevant "modifier" relationship rather than a classic genetic modifier locus ([treatment reviews, ScienceDirect](https://www.sciencedirect.com/science/article/pii/S0304416520301987)).

### Chromosomal Abnormalities
Not applicable — PMM2-CDG is caused by point mutations/small indels in a single gene, not large structural/chromosomal rearrangements.

### Molecular/Structural Insights
A 2025 comprehensive update integrates molecular dynamics and structural analysis of PMM2 mutant proteins to refine genotype-phenotype correlations, showing that many pathogenic variants destabilize the dimer interface or active site rather than abolishing catalysis outright ([PMC12042452](https://pmc.ncbi.nlm.nih.gov/articles/PMC12042452/)).

---

## 5. Environmental Information

- **Environmental/toxin factors**: None causally implicated; this is a purely monogenic disease.
- **Lifestyle factors**: Not causal, though diet (mannose/galactose supplementation trials) is relevant therapeutically (Section 12).
- **Infectious agents**: Not causal of the underlying disease, but febrile/infectious illness is a recognized **trigger of acute decompensation** — stroke-like episodes, coagulopathic bleeding events, and metabolic crises are frequently precipitated by intercurrent infection ([PMC10530657](https://pmc.ncbi.nlm.nih.gov/articles/PMC10530657/)).

---

## 6. Mechanism / Pathophysiology

### Core Molecular Defect
PMM2 catalyzes the reversible isomerization of **mannose-6-phosphate (M6P) → mannose-1-phosphate (M1P)** in the cytosol. M1P is the substrate for GDP-mannose pyrophosphorylase, generating **GDP-mannose**, which is required both directly (for cytosolic-face LLO assembly) and via conversion to **dolichol-phosphate-mannose (Dol-P-Man)** (for luminal-face assembly) in construction of the **dolichol-linked oligosaccharide (LLO) precursor**, Glc3Man9GlcNAc2-PP-Dolichol, in the endoplasmic reticulum. Deficient PMM2 activity lowers the M1P pool, causing **truncated/incomplete LLO synthesis**, which the oligosaccharyltransferase (OST) complex then transfers inefficiently — or not at all — onto nascent glycoproteins' Asn-X-Ser/Thr sequons ([PMID 22956764](https://pubmed.ncbi.nlm.nih.gov/22956764/); [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1110/)).

### Cellular Processes / Protein Dysfunction
The resulting **global hypoglycosylation** compromises protein folding, ER quality control, stability, and trafficking across essentially every secreted/membrane glycoprotein — explaining the multisystem phenotype. Recent work has extended understanding to specific immune signaling pathways: hypoglycosylation impairs the **TNFα–TNFR1 signaling axis**, implicating aberrant cytokine signaling in PMM2-CDG immunopathology ([PMC12488661, "Immunopathology in PMM2-CDG"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12488661/)).

### Suggested Ontology Terms
- **GO:0004615** (phosphomannomutase activity)
- **GO:0006487** (protein N-linked glycosylation)
- **GO:0006506** (GPI anchor biosynthetic process, related pathway)
- **GO:0097502** (mannosylation)
- Cellular component: **GO:0005783** (endoplasmic reticulum), **GO:0005793** (ER-Golgi intermediate compartment)

### Endocrine Mechanism
Multiple hormone-axis glycoproteins are directly affected: **thyroglobulin, TSH, prolactin, FSH, LH, and IGFBP-3** are all N-glycosylated and functionally impaired by hypoglycosylation, explaining hypothyroidism, gonadal dysfunction, and growth abnormalities as direct downstream consequences of the core enzymatic defect rather than secondary organ damage ([Frontiers in Endocrinology 2025](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2025.1594118/full)).

### Coagulation Mechanism
Antithrombin, protein C, protein S, and several clotting factors (XI, IX) are glycoproteins whose hypoglycosylation directly reduces their circulating activity/half-life, producing a mixed pro- and anti-thrombotic coagulopathy that can manifest as either spontaneous bleeding or thrombosis/stroke-like episodes depending on which factor imbalance predominates at a given time ([de la Morena-Barrio et al., J Thromb Haemost, PMID referenced in search; PMC10530657](https://pmc.ncbi.nlm.nih.gov/articles/PMC10530657/)).

### Causal Chain Summary (for pathograph modeling)
1. Biallelic *PMM2* pathogenic variants → **decreased phosphomannomutase 2 enzymatic activity** (molecular scale; `LOSS_OF_FUNCTION`/`GAIN...` not applicable — hypomorphic)
2. → Decreased M1P / GDP-mannose / Dol-P-Man pools (molecular)
3. → Truncated lipid-linked oligosaccharide (LLO) synthesis (molecular)
4. → Global protein N-hypoglycosylation (cellular)
5. → Downstream organ-specific consequences: cerebellar granule cell/neuronal developmental disruption (neurological), hypoglycosylated coagulation factors (coagulopathy), hypoglycosylated hormone/hormone receptors (endocrinopathy), hepatocyte dysfunction (hepatic), etc.

### Molecular/Omics Profiling
A 2025 mouse model study (see Section 15) using single-cell/bulk transcriptomic profiling of cerebellar tissue revealed a **neurodevelopmental origin** of PMM2-CDG brain pathology — i.e., cerebellar granule cell development is disrupted prenatally/perinatally rather than purely via later neurodegeneration ([bioRxiv/PMC12157701, "Novel mouse model reveals neurodevelopmental origin of PMM2-CDG brain pathology"](https://pmc.ncbi.nlm.nih.gov/articles/PMC12157701/)).

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary**: Cerebellum/CNS, peripheral nerves, eyes; skin/subcutaneous fat; liver; heart; GI tract; kidney; endocrine glands (thyroid, gonads, pancreatic islets)
- **Body systems**: Nervous, endocrine, digestive, cardiovascular, renal, hematologic/coagulation, integumentary, skeletal
- Suggested UBERON: cerebellum (UBERON:0002037), liver (UBERON:0002107), heart (UBERON:0000948), kidney (UBERON:0002113), thyroid gland (UBERON:0002046)

### Tissue and Cell Level
- Cerebellar granule neurons and Purkinje cells (developmental/degenerative target)
- Hepatocytes (fibrosis, dysfunction)
- Vascular endothelium (coagulation factor synthesis)
- Suggested Cell Ontology: cerebellar granule cell (CL:0000643), hepatocyte (CL:0000182)

### Subcellular Level
- **Endoplasmic reticulum** (site of N-glycosylation/LLO assembly) — GO:0005783
- **Cytosol** (site of PMM2 enzymatic reaction) — GO:0005829
- Golgi apparatus (downstream glycan processing) — GO:0005794

### Localization
Bilateral, symmetric cerebellar hypoplasia/atrophy (not lateralized); systemic (multi-organ) involvement rather than focal.

---

## 8. Temporal Development

- **Onset**: Congenital in the classic form (dysmorphic features and hypotonia apparent at or shortly after birth); a late-onset/adult-presenting phenotype exists with initial symptoms (ataxia, peripheral neuropathy) emerging in adolescence or adulthood.
- **Onset pattern**: Chronic/insidious for the baseline multisystem disease, punctuated by **acute stroke-like episodes, bleeding, and hypoglycemic crises** that are typically provoked by infection, fasting, or surgical stress.
- **Progression / stages** (per GeneReviews): 
  1. Infantile multisystem stage (birth–~3 years): failure to thrive, hypotonia, coagulopathy, hepatic/cardiac/renal involvement; highest mortality risk period.
  2. Late-infantile/childhood ataxia–intellectual disability stage (ages 3–10): cerebellar ataxia and cognitive delay become the dominant clinical picture as acute multisystem crises recede.
  3. Adult stable disability stage: chronic, largely non-progressive neurological disability (ataxia, peripheral neuropathy, mild cognitive impairment) with continued risk of episodic coagulopathic/stroke-like events.
- **Rate**: Highly variable across patients — from neonatal death to stable lifelong mild disability.
- **Remission patterns**: No spontaneous remission of the underlying enzymatic defect; individual acute complications (hypoglycemia, effusions) can resolve with supportive/targeted treatment.
- **Critical periods**: Fetal/early neonatal period is critical for cerebellar developmental injury (per the neurodevelopmental-origin mouse data); early childhood is the period of highest risk for life-threatening multisystem crises.

---

## 9. Inheritance and Population

### Epidemiology
Estimates vary substantially by methodology:
- A 2025 ScienceDirect analysis calculated an incidence estimate of **1 in 33,576 for North America and Europe combined** (1 in 40,375 in North America; 1 in 29,043 in Europe), predicting ~303 live births/year across both regions ([ScienceDirect, "Incidence and prevalence of PMM2-CDG: Past, present, and future"](https://www.sciencedirect.com/science/article/pii/S1096719225001799)).
- Allele-frequency-based (gnomAD) theoretical birth prevalence estimates run as high as **1:20,000**, but later empirical estimates from diagnosed cohorts are lower, **1:77,000 to 1:286,000** ([PMC8383291](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8383291/)) — the gap likely reflects embryonic lethality of severe genotypes and under-ascertainment/underdiagnosis.
- Regional variation: most commonly reported/diagnosed in **Denmark and other Scandinavian countries**; estimated combined CDG prevalence in the Saudi population ~14/million; in Poland ~1/million.

### Inheritance Pattern
**Autosomal recessive.** Both parents are obligate heterozygous carriers; recurrence risk is 25% per pregnancy for unaffected-carrier parents.

### Penetrance / Expressivity
Full penetrance for the biochemical/glycosylation defect in biallelic carriers, but **highly variable clinical expressivity** — genotype only partially predicts phenotype severity, and even patients sharing the identical genotype (e.g., R141H/F119L) can show a wide range of clinical severity, implicating additional genetic/epigenetic/stochastic modifiers not yet fully characterized.

### Genetic Anticipation
Not reported — not a repeat-expansion disorder.

### Germline Mosaicism
Not specifically documented as a recurring feature of PMM2-CDG in the literature reviewed.

### Founder Effects
R141H shows elevated carrier frequency in the Finnish population (gnomAD), consistent with a founder or drift effect in Northern European populations; the disease is disproportionately reported in Scandinavian cohorts.

### Consanguinity
Increases risk in populations/families with elevated consanguinity rates, as for any autosomal recessive disorder, though PMM2-CDG is not specifically enriched in classically consanguineous populations relative to Northern European populations where it is most reported.

### Carrier Frequency
Estimated from gnomAD population allele frequencies; R141H alone carrier frequency ~0.39% (general), ~0.84% (Finnish).

### Sex Ratio / Age Distribution
No strong sex bias reported for disease occurrence (autosomal, so expected 1:1), though certain endocrine manifestations (hypergonadotropic hypogonadism, elevated FSH) are specifically described in affected **females**. Age distribution spans neonatal death through adulthood as described above.

---

## 10. Diagnostics

### First-Line Biochemical Screening
- **Serum transferrin isoelectric focusing (IEF)** / **carbohydrate-deficient transferrin (CDT) analysis**: the standard first-line screening test for N-glycosylation disorders including PMM2-CDG. PMM2-CDG produces a characteristic **Type I transferrin isoform pattern** (loss of entire N-glycan chains, distinguishing it from Type II patterns seen in Golgi-processing CDGs) ([Mayo Clinic Labs test catalog](https://www.mayocliniclabs.com/test-catalog/overview/89891)).
- **Apolipoprotein C-III isoform analysis**: used as a complementary/confirmatory first-line screen alongside transferrin isoform analysis, particularly useful in cases where transferrin results are equivocal or in liver disease (which can confound transferrin glycoform interpretation).
- Sensitivity: a 2024 study reported **94% overall sensitivity** of transferrin isoform analysis for PMM2-CDG detection ([PMID 39216211](https://pubmed.ncbi.nlm.nih.gov/39216211/)) — meaning ~6% of cases could be missed by this screen alone, reinforcing the need for molecular confirmation when clinical suspicion is high despite normal/equivocal screening.

### Enzyme Assay
Phosphomannomutase enzymatic activity assay in **leukocytes or cultured fibroblasts**, used to confirm pathogenicity when genetic variants are of uncertain significance.

### Molecular Genetic Testing
- **Definitive diagnosis**: identification of biallelic pathogenic/likely pathogenic *PMM2* variants by sequencing (single-gene sequencing, CDG-focused gene panel, or exome/genome sequencing).
- Recommended approach per GeneReviews: given the broad, nonspecific multisystem presentation, a **metabolic/CDG gene panel or exome sequencing** is often the practical first-tier molecular test alongside biochemical screening.

### Imaging
- **Brain MRI**: cerebellar hypoplasia at birth progressing to cerebellar atrophy — a key supportive radiological finding correlating with ataxia severity ([PMC8360885](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8360885/)).

### Differential Diagnosis
Other CDG subtypes (particularly MPI-CDG/CDG-Ib, which is treatable with mannose and must be distinguished), other congenital ataxias/cerebellar hypoplasia syndromes, other causes of neonatal coagulopathy/hepatopathy, and other lipodystrophy syndromes.

### Screening
No universal newborn screening program currently exists for PMM2-CDG (unlike some other IEMs); diagnosis is typically clinically triggered. Carrier screening panels for *PMM2* exist commercially (e.g., Myriad Foresight Carrier Screen) for reproductive risk assessment in at-risk populations.

---

## 11. Outcome/Prognosis

### Mortality
Historically, mortality in the first years of life has been reported at roughly **20% in the infantile-onset multisystem form**, primarily from cardiac, hepatic, or coagulopathic/infectious complications, though outcomes have improved with modern supportive care. Long-term follow-up cohorts (e.g., the French cohort of 96 patients) demonstrate that many patients who survive the high-risk infantile period stabilize into the chronic ataxia/intellectual disability phenotype with a near-normal lifespan, though episodic life-threatening events (stroke-like episodes, severe coagulopathy) remain a lifelong risk ([Genetics in Medicine, "Long-term follow-up in PMM2-CDG"](https://www.nature.com/articles/s41436-018-0301-4)).

### Morbidity
Chronic ataxia, peripheral neuropathy, and mild-to-moderate intellectual disability are the dominant sources of long-term morbidity and reduced adaptive functioning/quality of life, as documented in cross-sectional adaptive functioning studies ([PMC10739927](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10739927/)).

### Complications
Recurrent stroke-like episodes (18% of a large cohort), spontaneous bleeding (16%), thrombosis (10%), pericardial effusion, hyperinsulinemic hypoglycemia, hypothyroidism, and hepatic fibrosis are recognized long-term/recurrent complications requiring ongoing surveillance.

### Prognostic Factors
Genotype (presence of two null/severe alleles vs. a hypomorphic allele) partially correlates with severity; degree of residual PMM2 enzymatic activity is a key biochemical prognostic correlate. Early recognition and aggressive management of acute coagulopathic/metabolic crises appears to improve survival through the highest-risk infantile period.

---

## 12. Treatment

**There are currently no FDA/EMA-approved disease-modifying therapies for PMM2-CDG** ([Frontiers search summary](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2025.1594118/full); EMA orphan designation EU/3/18/2047 reflects ongoing drug development, not an approved product). Management is currently **supportive and symptomatic**, with several investigational disease-modifying approaches in active clinical trials.

### Supportive/Symptomatic Care (current standard of care)
- Multidisciplinary management: physical/occupational/speech therapy for ataxia and developmental delay (NCIT:C15302 Physical Therapy; NCIT:C159273 Speech Therapy; NCIT:C121351 Occupational Therapy)
- Nutritional support/feeding interventions for failure to thrive (NCIT:C15447 Dietary Intervention)
- Coagulopathy management: fresh frozen plasma or factor/antithrombin concentrate replacement during acute bleeding, thrombotic, or peri-surgical periods
- Diazoxide for hyperinsulinemic hypoglycemia (successful in 7/10 treated patients in one series) (NCIT:C15986 Pharmacotherapy; therapeutic_agent CHEBI diazoxide)
- Thyroid hormone replacement for hypothyroidism (NCIT:C15986 Pharmacotherapy)
- Cardiac monitoring/management of pericardial effusion and cardiomyopathy
- Genetic counseling for families (NCIT:C15240)

### Investigational Disease-Modifying Therapies

**1. Epalrestat (repurposed aldose reductase inhibitor)** — furthest along in clinical development:
- Originally developed for diabetic neuropathy in Japan; repurposed by Perlara/collaborators based on the hypothesis that aldose reductase inhibition redirects glucose flux to increase mannose/GDP-mannose availability.
- A **Phase III, randomized, double-blind, placebo-controlled trial** in pediatric PMM2-CDG patients (Mayo Clinic-led) enrolled 38 subjects, closed enrollment November 2023, and as of March 2024 all placebo subjects were permitted to cross over to open-label epalrestat at their 15-month visit ([PR Newswire, March 2024](https://www.prnewswire.com/news-releases/phase-iii-clinical-trial-of-pediatric-subjects-with-pmm2-cdg-begins-crossover-to-open-label-epalrestat-302090890.html); [Mayo Clinic trial page](https://www.mayo.edu/research/clinical-trials/cls-20491217)).
- Trial design assesses safety, tolerability, and clinical/metabolic improvement (oral, three-times-daily dosing).
- Therapeutic modality: SMALL_MOLECULE; NCIT treatment_term: Pharmacotherapy (NCIT:C15986).

**2. GLM101 (mannose-1-phosphate replacement therapy)** — Glycomine:
- A glycoprotein-based mannose-1-phosphate replacement therapy designed to bypass the deficient PMM2 enzymatic step by delivering M1P directly into cells, restoring downstream GDP-mannose/Dol-P-Man pathway flux.
- Phase 1 study: NCT05549219 ("24-Week Study to Assess the PD, Safety, Tolerability, and PK of GLM101").
- **Phase 2a open-label results**: among 9 adult/adolescent patients, treatment produced an average **11.9-point improvement on the ICARS (International Cooperative Ataxia Rating Scale)** over 24 weeks, with a favorable safety profile (no serious adverse events; only mild-moderate AEs) ([BioSpace, Glycomine Phase 2 results](https://www.biospace.com/glycomine-announces-encouraging-efficacy-data-from-ongoing-phase-2-clinical-study-in-pmm2-cdg)).
- **Phase 2b "POLAR" trial**: global, randomized, double-blind, placebo-controlled study; enrollment of 43 patients across 15 sites completed as of April 2026, with topline data expected Q4 2026 ([Glycomine press release, April 2026](https://www.glycomine.com/glycomine-completes-enrollment-in-global-phase-2b-polar-study-of-glm101-for-the-treatment-of-pmm2-cdg/)).
- Therapeutic modality: PROTEIN_REPLACEMENT (or classify as small-molecule/metabolite replacement depending on schema fit).

**3. Dietary mannose supplementation**:
- Corrects hypoglycosylation in PMM2-deficient fibroblasts in vitro, but short-term oral/IV mannose monotherapy trials in patients have shown **inconsistent/largely unsuccessful clinical results** ([Orphanet J Rare Dis, "Unsuccessful intravenous D-mannose treatment in PMM2-CDG"](https://link.springer.com/article/10.1186/s13023-019-1213-3)). One study found that after >1 year of dietary mannose supplementation, a majority of patients showed improved glycosylation biomarkers, suggesting a longer treatment horizon may be needed ([Orphanet J Rare Dis 2020, "Dietary mannose supplementation"](https://ojrd.biomedcentral.com/articles/10.1186/s13023-020-01528-z)); efficacy is thought to depend on the individual patient's PMM2:MPI enzymatic activity ratio.

**4. Pharmacological chaperones/proteostasis regulators** (preclinical):
- Screening identified compounds (8 candidates, 4 confirmed as functional chaperones) that increase thermal stability of destabilized/oligomerization-defective PMM2 mutant proteins and increase residual PMM enzymatic activity in cell models — proof-of-concept for a chaperone therapy strategy, not yet in clinical trials ([ResearchGate, "Pharmacological Chaperoning: A Potential Treatment for PMM2-CDG"](https://www.researchgate.net/publication/309416910_Pharmacological_Chaperoning_A_Potential_Treatment_for_PMM2-CDG)).

**5. AAV gene replacement therapy** (preclinical):
- A 2025 study in the novel Pmm2 mouse model showed **AAV-based gene replacement therapy prevented and halted manifestation of abnormal neurological phenotypes** when administered appropriately, providing strong preclinical proof-of-concept for gene therapy in PMM2-CDG ([Gene Therapy (Nature), 2025](https://www.nature.com/articles/s41434-025-00525-w)). Therapeutic modality: GENE_THERAPY.

### Treatment Algorithm
No formal consensus treatment algorithm exists beyond symptomatic/supportive management protocols and acute-crisis management guidance for coagulopathy (multicentric study on hemostasis anomalies and acute management, [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1096719223003049)).

---

## 13. Prevention

- **Primary prevention**: Not applicable in the classic sense (no modifiable environmental cause); the main "primary prevention" lever is **reproductive genetic counseling and carrier screening** for at-risk couples/families, with options for prenatal diagnosis (chorionic villus sampling/amniocentesis with molecular *PMM2* testing) or preimplantation genetic testing in known-carrier couples.
- **Secondary prevention**: No population newborn screening program currently exists (unlike some IEMs on standard newborn screening panels); early clinical recognition based on classic phenotype (inverted nipples, abnormal fat pads, cerebellar hypoplasia, hypotonia) and prompt biochemical/molecular testing shortens diagnostic delay.
- **Tertiary prevention**: Proactive multidisciplinary surveillance (coagulation panels, thyroid function, echocardiography, renal function, glucose monitoring) to catch and manage complications (thrombosis, effusions, hypoglycemia) before they become life-threatening is standard practice in specialized CDG centers.
- **Carrier screening**: Commercially available (e.g., Myriad Foresight Carrier Screen) for reproductive planning.
- **Genetic counseling**: Central to family management given 25% recurrence risk in each subsequent pregnancy for carrier couples.

---

## 14. Other Species / Natural Disease

PMM2-CDG is not known to occur as a naturally-occurring inherited disease in non-human species (unlike some other Mendelian disorders with veterinary counterparts in OMIA). *PMM2* orthologs are broadly conserved (mouse *Pmm2*, zebrafish *pmm2*), which supports engineered animal modeling (Section 15) rather than natural disease occurrence.

---

## 15. Model Organisms

### Mouse Models
- **Original hypomorphic mouse (Pmm2^R137H/F118L^)**: An earlier attempt at a mouse model harboring the mouse-orthologous equivalent of the human R141H/F119L compound heterozygous genotype resulted in **complete embryonic lethality**, making it unsuitable for postnatal disease study ([HMG, Oxford Academic](https://academic.oup.com/hmg/article/25/11/2182/2446102)).
- **Viable hypomorphic model (Pmm2^R137H/F115L^)**: A subsequent, refined hypomorphic mouse line was generated that is viable and recapitulates multiple PMM2-CDG disease features, corresponding to the common human R141H/F119L genotype.
- **Tamoxifen-inducible conditional knockout**: A newer, widely tissue-deficient Pmm2 knockout mouse (inducible) was developed and characterized to reveal **distinct neurological phenotypes** relevant to human PMM2-CDG.
- **2025 novel mouse model — neurodevelopmental origin study**: Demonstrated that PMM2-CDG cerebellar/brain pathology has a **neurodevelopmental origin** (disrupted early brain development) rather than purely progressive neurodegeneration, and the same model was used to show that **AAV-based gene replacement therapy prevents/halts abnormal neurological phenotypes** when given at the appropriate developmental window ([PMC12157701](https://pmc.ncbi.nlm.nih.gov/articles/PMC12157701/); [Gene Therapy 2025](https://www.nature.com/articles/s41434-025-00525-w)).
- Prior hypomorphic alleles tested have historically fallen into two unhelpful extremes: **too mild** (no discernible phenotype) or **too severe** (embryonic lethal) — underscoring the difficulty of modeling a disease where complete loss-of-function is not compatible with survival.

### Zebrafish Models
- **Morpholino knockdown model** (*pmm2* morphants): Reproduces PMM2-CDG-relevant developmental abnormalities including **craniofacial defects** and **impaired motility linked to altered motor neurogenesis** in the spinal cord; global N-glycosylation and LLO levels are reduced, directly recapitulating the human biochemical defect ([PMID 22956764](https://pubmed.ncbi.nlm.nih.gov/22956764/); [Molecular Biology of the Cell](https://www.molbiolcell.org/doi/10.1091/mbc.e12-05-0411)). This model specifically proposed a **substrate-accumulation mechanism** (in addition to simple substrate deficiency) contributing to altered neurogenesis.
- Zebrafish are noted as valuable complementary models given that >70% of human proteins (and ~82% of disease-associated human genes) have zebrafish orthologs.

### Yeast Models
- Yeast (*S. cerevisiae*) models of phosphomannomutase deficiency have been used to study fundamental enzymatic and structural consequences of PMM2 pathogenic variants at the cell-biology level (bioRxiv preprint, "Yeast Models Of Phosphomannomutase 2 Deficiency").

### Cellular/In Vitro Models
- **HepG2 PMM2-CDG knockout cell line**: A CRISPR-engineered hepatocyte-derived knockout model described as "a versatile platform for variant and therapeutic evaluation," useful for testing pharmacological chaperones and other small-molecule interventions in a human cellular context ([ScienceDirect, 2024](https://www.sciencedirect.com/science/article/pii/S1096719224004220)).
- **Patient-derived fibroblasts**: Widely used historically for enzyme activity confirmation and mannose-supplementation proof-of-concept studies.

### Model Applications and Limitations
- Mouse and zebrafish models each recapitulate specific disease facets (neurodevelopmental/cerebellar pathology in mouse; craniofacial and motor neurogenesis defects in zebrafish) but no single model fully recapitulates the human multisystem phenotype (coagulopathy, endocrinopathy, hepatic, cardiac involvement together).
- The species-specific difficulty in generating a viable "null/null"-equivalent model mirrors the human observation that severe biallelic null genotypes are not viable, reinforcing the mechanistic inference of embryonic lethality for complete PMM2 loss across species.

---

## Summary Table: Suggested Ontology Bindings for KB Curation

| Category | Term | ID |
|---|---|---|
| Disease | PMM2-congenital disorder of glycosylation | MONDO:0015286 |
| Gene | PMM2 | hgnc:9115 |
| Molecular function | phosphomannomutase activity | GO:0004615 |
| Biological process | protein N-linked glycosylation | GO:0006487 |
| Cellular component | endoplasmic reticulum | GO:0005783 |
| Phenotype | Cerebellar hypoplasia | HP:0001321 |
| Phenotype | Inverted nipples | HP:0003186 |
| Phenotype | Strabismus | HP:0000486 |
| Phenotype | Ataxia | HP:0001251 |
| Phenotype | Stroke-like episode | HP:0002401 |
| Phenotype | Hypothyroidism | HP:0000821 |
| Phenotype | Antithrombin III deficiency | HP:0031270 (or closest match) |
| Anatomy | Cerebellum | UBERON:0002037 |
| Anatomy | Liver | UBERON:0002107 |
| Cell type | Cerebellar granule cell | CL:0000643 |
| Treatment | Pharmacotherapy (epalrestat, GLM101) | NCIT:C15986 |
| Treatment | Gene Therapy | NCIT:C15238 |
| Treatment | Physical Therapy | NCIT:C15302 |

---

## Sources

- [Frontiers in Endocrinology (2025) — N-glycosylation and endocrine axes in PMM2-CDG](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2025.1594118/full)
- [Orphanet: PMM2-CDG (ORPHA:79318)](https://www.orpha.net/en/disease/detail/79318)
- [29 French adult patients with PMM2-CDG — Orphanet J Rare Dis](https://ojrd.biomedcentral.com/articles/10.1186/s13023-014-0207-4)
- [Patient reported outcomes for PMM2-CDG — Orphanet J Rare Dis (2022)](https://ojrd.biomedcentral.com/articles/10.1186/s13023-022-02551-y)
- [GARD — PMM2-CDG](https://rarediseases.info.nih.gov/diseases/9826/pmm2-congenital-disorder-of-glycosylation)
- [GeneReviews — PMM2-CDG](https://www.ncbi.nlm.nih.gov/books/NBK1110/)
- [OMIM #212065](https://omim.org/entry/212065)
- [EMA Orphan Designation EU/3/18/2047](https://www.ema.europa.eu/en/medicines/human/orphan-designations/eu-3-18-2047)
- [A zebrafish model of PMM2-CDG — PMID 22956764](https://pubmed.ncbi.nlm.nih.gov/22956764/)
- [Immunopathology in PMM2-CDG: TNFα-TNFR1 signalling — PMC12488661](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12488661/)
- [A comprehensive update of genotype–phenotype correlations in PMM2-CDG — PMC12042452](https://pmc.ncbi.nlm.nih.gov/articles/PMC12042452/)
- [Suspected central adrenal insufficiency in PMM2-CDG — PMC12511663](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12511663/)
- [Untangling adaptive functioning of PMM2-CDG — Scientific Reports (2023)](https://www.nature.com/articles/s41598-023-49518-y)
- [Clinical and radiological correlates of ADLs in cerebellar atrophy in PMM2-CDG — PMC8360885](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8360885/)
- [Child Neurology case: PMM2-CDG with unusual eye movements — Neurology](https://www.neurology.org/doi/10.1212/WNL.0b013e31826e2617)
- [Perlara/Mayo Clinic — Phase III epalrestat trial crossover, PR Newswire (2024)](https://www.prnewswire.com/news-releases/phase-iii-clinical-trial-of-pediatric-subjects-with-pmm2-cdg-begins-crossover-to-open-label-epalrestat-302090890.html)
- [Mayo Clinic — Epalrestat Phase I/III trial page](https://www.mayo.edu/research/clinical-trials/cls-20491217)
- [ClinicalTrials.gov NCT05549219 — GLM101 PD/Safety Study](https://clinicaltrials.gov/study/NCT05549219)
- [ClinVar VCV000007706.122 (PMM2 R141H)](https://www.ncbi.nlm.nih.gov/clinvar/variation/7706/)
- [ClinVar RCV000008145 (PMM2 c.422G>A / p.Arg141His)](https://www.ncbi.nlm.nih.gov/clinvar/RCV000008145/)
- [Incidence and prevalence of PMM2-CDG: Past, present, and future — ScienceDirect (2025)](https://www.sciencedirect.com/science/article/pii/S1096719225001799)
- [The Estimated Prevalence of N-Linked CDGs Across Populations — PMC8383291](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8383291/)
- [A mouse model of PMM2-CDG — Human Molecular Genetics](https://academic.oup.com/hmg/article/25/11/2182/2446102)
- [HepG2 PMM2-CDG knockout model — ScienceDirect (2024)](https://www.sciencedirect.com/science/article/pii/S1096719224004220)
- [Novel mouse model reveals neurodevelopmental origin of PMM2-CDG brain pathology — PMC12157701](https://pmc.ncbi.nlm.nih.gov/articles/PMC12157701/)
- [AAV-based gene replacement therapy in PMM2-CDG mouse model — Gene Therapy (Nature, 2025)](https://www.nature.com/articles/s41434-025-00525-w)
- [Dietary mannose supplementation in PMM2-CDG — Orphanet J Rare Dis (2020)](https://ojrd.biomedcentral.com/articles/10.1186/s13023-020-01528-z)
- [Unsuccessful intravenous D-mannose treatment in PMM2-CDG — Orphanet J Rare Dis](https://link.springer.com/article/10.1186/s13023-019-1213-3)
- [Pharmacological Chaperoning: A Potential Treatment for PMM2-CDG — ResearchGate](https://www.researchgate.net/publication/309416910_Pharmacological_Chaperoning_A_Potential_Treatment_for_PMM2-CDG)
- [Sensitivity of transferrin isoform analysis for PMM2-CDG — PMID 39216211](https://pubmed.ncbi.nlm.nih.gov/39216211/)
- [Mayo Clinic Labs — CDG Overview/CDT test catalog](https://www.mayocliniclabs.com/test-catalog/overview/89891)
- [Coagulation abnormalities in a prospective cohort of 50 patients with PMM2-CDG — PMC10530657](https://pmc.ncbi.nlm.nih.gov/articles/PMC10530657/)
- [Association between acute complications in PMM2-CDG and haemostasis anomalies — ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1096719223003049)
- [Long-term follow-up in PMM2-CDG: are we ready to start treatment trials? — Genetics in Medicine (2018)](https://www.nature.com/articles/s41436-018-0301-4)
- [Glycomine — Phase 2 GLM101 efficacy data, BioSpace](https://www.biospace.com/glycomine-announces-encouraging-efficacy-data-from-ongoing-phase-2-clinical-study-in-pmm2-cdg)
- [Glycomine — Phase 2b POLAR study enrollment complete (April 2026)](https://www.glycomine.com/glycomine-completes-enrollment-in-global-phase-2b-polar-study-of-glm101-for-the-treatment-of-pmm2-cdg/)
- [Hypoglycemia in CDG patients due to PMM2 mutations: hyperinsulinemic follow-up — PMC7012739](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7012739/)
- [Hyperinsulinemic Hypoglycemia Due to PMM2 Mutation with ARPKD — PMC9680396](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9680396/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 19 |
| Resolved | 19 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 19 |
| On topic | 15 |
| Off topic | 0 |

All extracted references resolved successfully.