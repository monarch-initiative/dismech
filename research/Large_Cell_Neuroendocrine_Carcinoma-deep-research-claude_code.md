---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-20T03:58:08.746596'
end_time: '2026-08-20T04:03:09.059276'
duration_seconds: 300.31
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Large Cell Neuroendocrine Carcinoma
  mondo_id: ''
  category: Neoplastic
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
  num_turns: 22
  total_cost_usd: 2.1790019000000003
  session_id: 4c0ea920-20d3-5d6a-a26e-44c9910bf0c1
  stop_reason: end_turn
  assistant_text_blocks: 3
citation_count: 53
reference_validation:
  total_references: 35
  verified: 35
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 35
  on_topic: 31
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Large Cell Neuroendocrine Carcinoma
- **MONDO ID:**  (if available)
- **Category:** Neoplastic

## Research Objectives

Please provide a comprehensive research report on **Large Cell Neuroendocrine Carcinoma** covering all of the
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

I'll research Large Cell Neuroendocrine Carcinoma (LCNEC) now, using web search across the key domains (classification, genetics, pathophysiology, treatment, prognosis).

I now have sufficient material to compile the comprehensive report.

I have gathered sufficient primary-literature data across all domains. I'll now write the complete report.

# Large Cell Neuroendocrine Carcinoma: A Comprehensive Research Report

## 1. Disease Information

**Overview.** Large cell neuroendocrine carcinoma (LCNEC) is a high-grade, poorly differentiated neuroendocrine carcinoma composed of large malignant epithelial cells that display neuroendocrine morphology (organoid nesting, palisading, rosette-like structures) together with high mitotic activity (>10 mitoses/2mm²) and often geographic necrosis ([PathologyOutlines](https://www.pathologyoutlines.com/topic/lungtumorlargecellne.html); [Wikipedia](https://en.wikipedia.org/wiki/Large_cell_neuroendocrine_carcinoma_of_the_lung)). It was historically classified as a variant of large-cell lung carcinoma but is now recognized in the 2021 WHO Classification of Thoracic Tumours as one of two neuroendocrine *carcinomas* of the lung (alongside small cell lung carcinoma, SCLC), distinct from the low/intermediate-grade neuroendocrine *tumors* (typical and atypical carcinoid) ([PathologyOutlines](https://www.pathologyoutlines.com/topic/lungtumorlargecellne.html)). Although the pulmonary form is the prototype and best studied, LCNEC also arises as a primary tumor in extrapulmonary sites — GI tract, pancreas, cervix, uterus, ovary, bladder, prostate, breast, larynx/pharynx, paranasal sinus, and thymus ([Frontiers, Management of LCNEC, PMID:34513663](https://pubmed.ncbi.nlm.nih.gov/34513663/); [PMC10743506](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10743506/)).

**Key identifiers.**
- **MONDO**: MONDO:0018316-class term(s) for "large cell neuroendocrine carcinoma" (cross-referenced through the Monarch Initiative/NORD MONDO disease pages); the entity has organ-specific children (lung, breast, cervical, thymic, etc.) ([NORD/MONDO](https://rarediseases.org/mondo-disease/large-cell-neuroendocrine-carcinoma/)).
- **ICD-O-3 morphology code**: 8013/3 (Large cell neuroendocrine carcinoma).
- **ICD-11**: 2C25.4 (malignant neuroendocrine neoplasms of bronchus or lung) with extension code XH0NL5 for large cell neuroendocrine carcinoma ([AHA Coding Clinic](https://www.findacode.com/newsletters/aha-coding-clinic/icd/large-cell-neuroendocrine-lung-cancer-I101024.html)).
- **ICD-10-CM**: indexed under C34.- (malignant neoplasm of bronchus and lung) for the pulmonary primary, with topography-specific codes for extrapulmonary primaries.
- **MeSH**: falls under "Carcinoma, Neuroendocrine" (D018277) and "Carcinoma, Large Cell" (D018281).
- No dedicated **OMIM** or **Orphanet** entry exists specifically for sporadic LCNEC, as it is not a classical monogenic disorder; Orphanet does catalog rare neuroendocrine tumor syndromes (e.g., MEN1) that can predispose to related neuroendocrine neoplasia.

**Synonyms/alternative names:** Pulmonary large-cell neuroendocrine carcinoma (LCNEC, PLCNC); large cell/neuroendocrine carcinoma; high-grade neuroendocrine carcinoma (large cell type); "non-small cell neuroendocrine carcinoma" (older, discouraged terminology).

**Data provenance.** The evidence base combines: (1) aggregated population-level registry data (SEER, national cancer registries), (2) large retrospective single- and multi-institutional clinicopathologic cohorts, (3) integrative genomic/transcriptomic sequencing cohorts (tumor-level, not EHR-derived), and (4) a growing number of prospective clinical trials (phase II basket and single-arm trials). There is comparatively little large-scale EHR-based real-world evidence relative to more common cancers, reflecting LCNEC's rarity (~1–3% of all lung cancers) ([PMC8081906](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8081906/)).

---

## 2. Etiology

### Disease Causal Factors
LCNEC does not have a single monogenic cause; it is a somatically acquired, multi-hit malignancy arising in transformed pulmonary neuroendocrine cells or a common progenitor shared with non-neuroendocrine lung epithelium, driven predominantly by tobacco-carcinogen-induced mutagenesis culminating in near-universal biallelic *TP53* inactivation plus a second driver event (*RB1* or *STK11/KEAP1*) (George et al., *Nat Commun* 2018, **PMID:29535388**). A minority of LCNECs arise via histologic transformation from EGFR-mutant lung adenocarcinoma under the selective pressure of EGFR-tyrosine-kinase-inhibitor therapy, driven mechanistically by biallelic *RB1* loss (search synthesis of transdifferentiation literature; PNAS 2019 mouse-model paper, https://www.pnas.org/doi/10.1073/pnas.1821745116).

### Risk Factors

**Genetic/molecular risk factors** (somatic, tumor-intrinsic; germline predisposition is not well established for sporadic LCNEC):
- Biallelic **TP53** inactivation — present in 64–92% of cases across cohorts (synthesis of PMID:33968782 review data).
- Biallelic **RB1** inactivation — 19–42% (concurrent with TP53 in "Type II/SCLC-like" tumors).
- **STK11**/**KEAP1** alterations — 17–33% (concurrent with TP53 in "Type I/NSCLC-like" tumors).
- **KRAS** mutations — 4–24%.
- **NOTCH family** gene alterations (inactivating) — 10–16%, implicated in loss of neuroendocrine differentiation control (George et al., **PMID:29535388**).
- **MYC family** amplification (particularly *MYCL*, *MYCN*, *MYC*) has been implicated in driving transitions between neuroendocrine lineage states (ASCL1→NEUROD1 transition) that phenocopy LCNEC-like histology in SCLC models (*Sci Adv* 2020, https://www.science.org/doi/10.1126/sciadv.abc2578).

**Environmental/behavioral risk factors:**
- **Tobacco smoking** is overwhelmingly the dominant risk factor: 92.8–98% of LCNEC patients have a smoking history, with many series reporting >40 pack-years in a majority of patients ([PMC8162139](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8162139/); [PMC9428409](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9428409/); [PMC6532618](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6532618/)). This mutagenic burden underlies the very high tumor mutational burden and TP53/STK11/KEAP1/KRAS mutation spectrum shared with squamous cell lung carcinoma and SCLC.
- **Age**: median age at diagnosis ~65–66 years, skewing toward older adults ([PMC8081906](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8081906/); PMID:33968782).
- **Sex**: strong male predominance, consistent with the historical smoking-exposure skew, though the male:female gap has been narrowing in more recent cohorts as female smoking rates changed.
- **Prior EGFR-TKI exposure** in *EGFR*-mutant adenocarcinoma is a specific, mechanistically defined risk pathway for acquired (transformed) LCNEC/SCLC.

### Protective Factors
No established genetic or environmental protective factors specific to LCNEC have been robustly identified in the literature reviewed; smoking cessation reduces overall lung cancer risk generically but LCNEC-specific protective/modifier data are sparse.

### Gene–Environment Interactions
The dominant gene–environment interaction is the tobacco-carcinogen mutational signature (SBS4-type, characterized by G>T transversions) converging on the TP53/RB1/STK11/KEAP1 tumor-suppressor network — i.e., chronic carcinogen exposure selects for and produces the specific biallelic tumor-suppressor loss-of-function events that define both LCNEC molecular subtypes. This is inferred from the near-universal smoking history combined with the mutational spectrum reported in comprehensive genomic profiling studies (George et al. **PMID:29535388**; Rekhtman et al., *Clin Cancer Res* 2016, "Genomic Profiling of Large-Cell Neuroendocrine Carcinoma of the Lung," https://aacrjournals.org/clincancerres/article/23/3/757/80338).

---

## 3. Phenotypes

### Clinical signs/symptoms (respiratory, driven by anatomic location)
- **Centrally located tumors** (a substantial minority, more than typical NSCLC adenocarcinoma but less central than SCLC): cough, hemoptysis, bronchial obstruction, post-obstructive/recurrent pneumonia.
  - Suggested HPO terms: Cough (**HP:0012735**), Hemoptysis (**HP:0002105**), Recurrent respiratory infections (**HP:0002205**).
- **Peripherally located tumors**: frequently asymptomatic, identified incidentally on imaging — reflecting the tendency of LCNEC to present as a peripheral nodule/mass more often than SCLC.
- **Constitutional/systemic symptoms** at presentation in advanced disease: weight loss, fatigue, dyspnea, chest pain.
  - HPO: Weight loss (**HP:0001824**), Fatigue (**HP:0012378**), Dyspnea (**HP:0002094**), Chest pain (not a canonical HPO term but codeable via SNOMED CT).

### Paraneoplastic phenomena
LCNEC, sharing biology with SCLC, can produce paraneoplastic syndromes, though less commonly reported than in classic SCLC:
- **SIADH/hyponatremia** (inappropriate ADH secretion)
- **Cushing syndrome** (ectopic ACTH)
- **Lambert–Eaton myasthenic syndrome**
- **Paraneoplastic neurological syndromes** — peripheral neuropathy, limbic encephalitis, and case reports of opsoclonus-myoclonus syndrome as the presenting feature preceding LCNEC diagnosis ([PMC10725307](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10725307/); AJRCCM abstract 2025).
- Rare carcinoid-syndrome-like flushing/diarrhea has been described but is atypical for high-grade NEC.
- Suggested HPO terms: Hyponatremia (**HP:0002902**), Cushingoid facies (**HP:0000174**), Myasthenia (**HP:0003473**), Peripheral neuropathy (**HP:0009830**), Encephalitis (**HP:0002383**).

### Laboratory abnormalities
- Elevated serum **neuron-specific enolase (NSE)** and **pro-gastrin-releasing peptide (ProGRP)** may be seen (SCLC-associated markers, less validated specifically for LCNEC).
- Chromogranin A elevation in serum can occur but is neither sensitive nor specific.

### Phenotype characteristics
- **Age of onset:** predominantly adult/older-adult onset (median 65–66 years); pediatric/young-adult LCNEC is exceptionally rare (case reports exist, e.g., tarlatamab case report in a young adult, [JTO Clin Res Rep](https://www.jtocrr.org/article/S2666-3643(24)00082-1/fulltext)).
- **Severity:** uniformly high grade/aggressive by definition (WHO diagnostic criterion requires high mitotic count and often necrosis).
- **Progression:** rapidly progressive; a majority of patients present with locoregionally advanced or metastatic (stage IV) disease — one large cohort reported 54.6% presenting at stage IV (synthesis, PMID:33968782).
- **Frequency among affected individuals:** By definition, the histologic/molecular features described (necrosis, high Ki-67, TP53 alteration) are present in nearly all diagnosed cases since they constitute diagnostic criteria; paraneoplastic phenomena are comparatively uncommon (case-report level).

### Quality of life impact
Given the aggressive course, poor prognosis (median OS 8–12 months in advanced disease; see Section 11), and frequent late-stage diagnosis, quality-of-life burden is substantial — encompassing respiratory symptom burden, treatment-related toxicity from platinum-etoposide chemotherapy or immunotherapy-related adverse events, and, in a subset, paraneoplastic neurological morbidity that can itself be disabling (e.g., the opsoclonus-myoclonus case series notes significant residual gait instability). Disease-specific QoL instrument data (e.g., EORTC QLQ-LC13) specific to LCNEC (as opposed to lung cancer broadly) were not identified in this search.

---

## 4. Genetic/Molecular Information

### Causal/driver genes and prevalence (from integrative genomic cohorts)

| Gene | Alteration type | Prevalence (pooled from Rekhtman 2016, George et al. 2018 [PMID:29535388], and subsequent reviews) |
|---|---|---|
| **TP53** (HGNC:11998) | Biallelic loss-of-function (missense, truncating, LOH) | 64–92% |
| **RB1** (HGNC:9884) | Biallelic inactivation | 19–42% |
| **STK11** (HGNC:11389) | Inactivating mutation | 17–33% |
| **KEAP1** (HGNC:6396) | Inactivating mutation | 19–31% |
| **KRAS** (HGNC:6407) | Activating mutation (mutually near-exclusive w/ RB1 loss) | 4–24% |
| **NOTCH1/2/3/4** family | Inactivating mutations | 10–16% |
| **MYC/MYCL/MYCN** | Amplification | Reported in subsets, associated with lineage-state transitions |

### Molecular subtyping — Type I vs. Type II LCNEC
The landmark integrative genomic/transcriptomic study by George et al. (*Nat Commun* 2018, n=75 LCNEC, genomic n=60, transcriptomic n=69; **PMID:29535388**) defined two largely mutually exclusive molecular subgroups:

- **Type I LCNEC ("NSCLC-like")**: biallelic **TP53** + **STK11/KEAP1** co-alteration (~37% of the discovery cohort, with other cohorts reporting 13–40%). Transcriptionally these tumors resemble SCLC/carcinoid neuroendocrine programs: **ASCL1^high / DLL3^high / NOTCH^low**.
- **Type II LCNEC ("SCLC-like")**: biallelic **TP53 + RB1** co-alteration (~35–42% of cohorts). These tumors show reduced neuroendocrine differentiation relative to SCLC, with a pattern of **ASCL1^low / DLL3^low / NOTCH^high**, and notably an **upregulation of immune-related pathways** — a potential biological basis for differential immunotherapy responsiveness.
- Despite sharing individual genomic alterations with lung adenocarcinoma and squamous cell carcinoma, LCNEC forms its **own distinct transcriptional cluster most similar to SCLC**, not to NSCLC histologic subtypes — supporting the WHO reclassification of LCNEC as a neuroendocrine carcinoma rather than an NSCLC variant.
- Follow-up real-world cohort data (PMID:33968782-linked synthesis) found substantial heterogeneity: in some series **52.7% of cases do not cleanly classify as either Type I or Type II**, underscoring that this is a useful but imperfect binary framework, likely reflecting a spectrum/continuum of neuroendocrine differentiation states rather than two discrete classes.

### Transcription-factor-based (SCLC-style) subtyping applied to LCNEC
Building on the four-subtype SCLC transcriptional classification (ASCL1, NEUROD1, POU2F3, YAP1), recent work has extended this framework to LCNEC:
- A 2025 *Nature Communications* integrated molecular/clinical characterization of pulmonary LCNEC (https://www.nature.com/articles/s41467-025-63091-0) and companion analyses of NEUROD1/ASCL1/POU2F3/YAP1 expression signatures found that **~80% of LCNEC transcriptomes align with an SCLC-like transcriptional profile**, predominantly ASCL1-driven or NEUROD1-driven with a smaller YAP1-high, low-neuroendocrine subgroup.
- **Prognostic implication:** NE-high subtypes (especially NEUROD1-dominant) show the **worst overall survival**, whereas the **YAP1-high subgroup** — characterized by low neuroendocrine differentiation, elevated immune infiltration, and higher Rb protein expression — is associated with **relatively better prognosis** and potentially greater immunotherapy sensitivity. A cross-tissue five-transcription-factor classification framework for neuroendocrine carcinomas generally (*Cancer Cell* 2024, https://www.cell.com/cancer-cell/fulltext/S1535-6108(24)00163-6) situates LCNEC within this broader neuroendocrine-carcinoma taxonomy.

### Variant classification and population frequency
Most driver alterations in LCNEC are **somatic**, not germline; population allele-frequency databases (gnomAD, ExAC) are not directly informative for a somatic-driver cancer, though tumor-suppressor loss-of-function variant classes (nonsense, frameshift, canonical splice-site, large deletion/LOH) predominate for TP53/RB1/STK11/KEAP1, consistent with a classical two-hit tumor-suppressor mechanism.

### Functional consequences
- **TP53** loss-of-function abrogates DNA-damage checkpoint control and apoptosis, permitting genomic instability.
- **RB1** biallelic loss removes the G1/S checkpoint brake, permitting unrestrained proliferation and correlating with a more SCLC-like, highly proliferative, RB1-null, low-differentiation phenotype (consistent with dismech's general RB1/CDK4-6/E2F "evading growth suppressors" pattern).
- **STK11 (LKB1)** loss deregulates AMPK/mTOR energy-sensing signaling and is separately associated (in NSCLC broadly) with **impaired response to immune checkpoint blockade**, a clinically important correlate carried into LCNEC Type I tumors.
- **KEAP1** loss constitutively activates NRF2 antioxidant signaling, promoting chemoresistance.

### Chromosomal/epigenetic information
Comprehensive DNA methylation or chromatin-state datasets specific to LCNEC were not prominently returned in this search; the transcription-factor-driven lineage-state model (ASCL1/NEUROD1/POU2F3/YAP1) is understood to be substantially governed by chromatin-level lineage plasticity analogous to SCLC, but LCNEC-specific epigenomic (ENCODE/Roadmap-style) datasets are not yet a major established resource for this tumor type — noted here as a **data gap**.

---

## 5. Environmental Information

- **Tobacco smoke** (the dominant environmental exposure) — see Section 2. Suggested exposure term: ECTO tobacco-smoke-exposure class terms (e.g., analogous to "exposure to cigarette smoke").
- No specific occupational toxin, radiation, or pollution exposure was identified in the literature reviewed as an independent LCNEC risk factor beyond the generic lung-carcinogen literature (radon, asbestos) that applies to lung cancer broadly; LCNEC-specific epidemiologic case-control data isolating these factors were not found in this search.
- **Infectious agents**: no established infectious/microbial etiology for pulmonary LCNEC. (Extrapulmonary neuroendocrine carcinomas at some sites, e.g., cervix, may co-occur with high-risk HPV infection as a contributing oncogenic driver at that anatomic site, analogous to the mechanism captured in the `viral_oncogenesis` module for HPV-driven cervical carcinoma, but this is a site-specific consideration for cervical LCNEC rather than a general LCNEC etiology.)

---

## 6. Mechanism / Pathophysiology

### Cell of origin
LCNEC is believed to arise from **pulmonary neuroendocrine cells (PNECs)** or a shared basal/neuroendocrine progenitor, analogous to SCLC. Supporting evidence: expression of the master neuroendocrine transcription factor **ASCL1** (achaete-scute homolog 1), normally restricted to PNECs, is retained in the neuroendocrine-high subset of LCNEC and SCLC, "indicating the neuroendocrine cell origin of these malignancies" (search synthesis). Suggested Cell Ontology term: pulmonary neuroendocrine cell (**CL:0002251**).

Mouse genetic models directly demonstrate that **cell-of-origin determines tumor phenotype** given an identical genetic lesion set: combined inactivation of **Rb1, Rbl1 (p130), Pten, and Trp53** ("quadruple knockout") in **all lung epithelial cell types** (via Ad5-CMV-Cre) produces **LCNEC**, whereas the identical genetic inactivation restricted to **basal cells** (via Ad5-K5-Cre) produces **SCLC** instead (Ferone et al., *PNAS* 2020, https://www.pnas.org/doi/10.1073/pnas.1821745116). This is strong mechanistic (model-organism) evidence that LCNEC and SCLC are genetically overlapping but cell-of-origin-divergent neuroendocrine carcinomas — a key causal-chain insight: **identical driver mutations (Rb1/Trp53/Pten loss) + differing epithelial cell-of-origin context → divergent histologic/molecular tumor phenotype (LCNEC vs. SCLC)**.

### Molecular pathway cascade (causal chain)
1. **Chronic tobacco-carcinogen mutagenesis** in bronchial/PNEC epithelium →
2. **Biallelic TP53 inactivation** (near-universal, "gatekeeper" first hit) →
3. **Second-hit bifurcation** into two convergent-but-distinct pathway states:
   - **RB1 co-loss** → loss of G1/S checkpoint restraint → E2F-driven hyperproliferation, high neuroendocrine differentiation program suppression (ASCL1^low/DLL3^low), NOTCH pathway de-repression (NOTCH^high) → "Type II/SCLC-like" phenotype with high Ki-67 and immune-pathway upregulation.
   - **STK11/KEAP1 co-loss** → AMPK/mTOR and NRF2 pathway dysregulation, retained ASCL1^high/DLL3^high neuroendocrine program, NOTCH^low → "Type I/NSCLC-like" phenotype.
4. Downstream: **loss of NOTCH-mediated lateral inhibition** permits expansion of the neuroendocrine lineage program (paralleling the conserved Notch-controlled neuroendocrine-vs-non-neuroendocrine fate switch described generally for high-grade lung NECs).
5. **MYC-family (MYC/MYCL/MYCN) amplification** can further drive lineage-state transitions (e.g., ASCL1-dominant → NEUROD1-dominant transcriptional states), which histologically and biologically manifest with LCNEC-like features even within an SCLC genomic background (*Sci Adv* 2020).
6. Net result: **unrestrained proliferation (high Ki-67, mean ~65.8%±20.8%), geographic tumor necrosis, and a highly aggressive, chemotherapy-initially-responsive but rapidly relapsing clinical phenotype.**

### Molecular functions / biological processes (suggested GO terms)
- Negative regulation of cell cycle G1/S transition (RB1 loss → **GO:0000082** positive regulation of G1/S transition, dysregulated)
- DNA damage response / apoptotic signaling (TP53; **GO:0006977**, **GO:0006915**)
- Notch signaling pathway (**GO:0007219**)
- Regulation of neuroendocrine cell differentiation (**GO:0071679**-adjacent / achaete-scute lineage specification)
- Cellular response to oxidative stress via NRF2/KEAP1 (**GO:0034614**, **GO:1901031** — regulation of response to oxidative stress)
- AMPK/mTOR signal transduction via STK11/LKB1 (**GO:0032008** relevant analog)

### Immune microenvironment
Type II (RB1-mutant) LCNEC shows **upregulation of immune-related pathways** transcriptionally, potentially correlating with the somewhat better observed responsiveness of RB1-altered/SCLC-like LCNEC to immune checkpoint blockade in some series, while STK11/KEAP1-altered (Type I) tumors — mirroring the well-established NSCLC finding — appear associated with **poorer immunotherapy response** (search synthesis of PMID:33968782-linked review).

### Molecular profiling technologies applied
- **Transcriptomics**: RNA-seq-based lineage subtyping (ASCL1/NEUROD1/POU2F3/YAP1) — see Section 4.
- **Genomics**: targeted and whole-exome sequencing cohorts (George et al. **PMID:29535388**; Rekhtman et al. 2016).
- **Single-cell/spatial**: not prominently represented in the literature surfaced by this search — a likely emerging area but not yet a mature LCNEC-specific resource base (data gap).
- **Functional genomics (CRISPR/DepMap)**: LCNEC-derived cell lines are represented within DepMap broadly as part of the neuroendocrine lung cancer cell line panel, but LCNEC-specific CRISPR screen publications were not surfaced in this search.

---

## 7. Anatomical Structures Affected

### Organ level
- **Primary organ**: lung (bronchus/lung parenchyma) is the prototypical and most-studied site — Uberon: lung (**UBERON:0002048**), bronchus (**UBERON:0002185**).
- **Extrapulmonary primary sites** (each representing a distinct clinical entity under the same histologic/molecular umbrella): gastroenteropancreatic tract (esophagus, stomach, colon, rectum, pancreas), gynecologic tract (cervix, uterus/endometrium, ovary), genitourinary tract (bladder, prostate), breast, thymus, larynx/pharynx, paranasal sinus, and skin/other rare sites. Approximately 37% of extrapulmonary NECs occur in the gastroenteropancreatic tract, with the genitourinary and gynecologic tracts also well represented ([PMC10743506](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10743506/)).
- **Secondary/metastatic involvement**: lung (contralateral/intrapulmonary), liver, bone, brain, and adrenal gland are common metastatic sites, mirroring SCLC's metastatic tropism. SEER-based analysis found single-organ metastasis in 26.0% and multi-organ metastasis in 14.8% of a cohort of 1,335 LCNEC patients, with lung and brain metastases each carrying a median OS of only 8 months ([PMC8971719](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8971719/); [PMC9773085](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9773085/)).

### Tissue/cell level
- Neoplastic cell population: large epithelial cells with neuroendocrine morphology, derived from (or recapitulating) pulmonary neuroendocrine cells — CL:0002251 (pulmonary neuroendocrine cell) as the presumptive normal-cell analog.
- Tumor architecture: organoid nesting, trabeculae, rosettes, palisading, with geographic necrosis.

### Subcellular level
Neuroendocrine secretory-granule machinery is retained in tumor cells (basis for chromogranin A positivity, a dense-core-granule marker) — relevant GO Cellular Component: secretory granule (**GO:0030141**), specifically dense core granule (**GO:0031045**).

### Localization
Approximately central vs. peripheral distribution is roughly split, with **central tumors more often symptomatic** (cough, hemoptysis, obstruction) and **peripheral tumors more often incidental**. No strong left/right or lobar lateralization pattern was identified in this search.

---

## 8. Temporal Development

- **Onset**: adult-onset, typically 6th–7th decade of life (median ~65–66 years); pediatric and young-adult cases are rare outliers.
- **Onset pattern**: often insidious for peripheral tumors (incidental imaging finding); can be more acute/subacute for centrally obstructing tumors (recurrent pneumonia, hemoptysis) or in cases presenting via paraneoplastic neurologic syndrome.
- **Staging**: uses the standard **AJCC/UICC TNM lung cancer staging system** (same schema as NSCLC), unlike SCLC which is often staged with the older limited/extensive-stage system alongside TNM. A majority of patients (>50% in several cohorts) present at **stage IV**.
- **Progression rate**: rapid; LCNEC's proliferative index (mean Ki-67 ~65.8%) situates it biologically between typical/atypical carcinoid (low-grade) and SCLC (very high-grade), but clinically it behaves aggressively, similar to SCLC.
- **Disease course pattern**: generally progressive/relapsing rather than static; initial chemotherapy responses are often followed by relatively rapid relapse, paralleling the SCLC natural history.
- **Recurrence**: common even after complete surgical resection in early-stage disease, motivating investigation of adjuvant chemotherapy (see Section 12).

---

## 9. Inheritance and Population

### Epidemiology
- **Incidence**: age-adjusted incidence of ~0.3 per 100,000 (0.4/100,000 in men, 0.3/100,000 in women), based on SEER 2000–2013 data; incidence appears to have been **rising** over time (from ~0.26 to 0.39 per 100,000 between 2004–2015 in one synthesis) — plausibly reflecting improved diagnostic recognition following the WHO reclassification as much as a true increase ([PMC6441320](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6441320/); PMID:33968782-linked synthesis).
- **Proportion of lung cancers**: LCNEC constitutes roughly **1–3%** of all lung cancers, and pulmonary LCNEC accounts for **0.58%** of all lung/bronchus carcinomas in one SEER-based accounting; it represents about **15% of all pulmonary neuroendocrine neoplasms**.

### Inheritance
LCNEC is predominantly a **sporadic, somatically driven** malignancy without an established Mendelian inheritance pattern (no OMIM entry for a monogenic LCNEC syndrome was identified). It is not classically associated with MEN1 or other hereditary neuroendocrine tumor syndromes the way well-differentiated NETs sometimes are, though the literature reviewed here did not surface data specifically excluding rare hereditary contributions in unusual young-onset cases.

### Population demographics
- **Sex ratio**: strong male predominance historically, tracking smoking-exposure demographics.
- **Age distribution**: peaks in the 6th–7th decades; rare before age 40.
- **Geographic/ethnic variation**: East Asian cohorts have been separately characterized genomically (Kang et al., **PMID:33144445**, "Genomic Profiling and Clinicopathological Characteristics of Neuroendocrine Tumors of the Lung in East Asian Patients"), suggesting some population-level genomic profiling differences exist, though a detailed comparative incidence/ethnicity breakdown was not fully resolved in this search.

---

## 10. Diagnostics

### Histopathology and immunohistochemistry (the diagnostic cornerstone)
Diagnosis requires **combined morphologic assessment plus immunohistochemical confirmation of neuroendocrine differentiation**:
- **Neuroendocrine markers**: chromogranin A (CgA), synaptophysin (Syn), and CD56/NCAM are typically diffusely positive; **INSM1** and **ASCL1 (hASH1)** are emerging, high-sensitivity markers particularly useful in crush-artifact-limited small biopsy specimens ([PathologyOutlines](https://www.pathologyoutlines.com/topic/lungtumorlargecellne.html); PMID:33968782 synthesis).
- **Ki-67 proliferation index**: characteristically high, mean ~65.8% (±20.8%) in one series, and is a key discriminator from carcinoid tumors (which have low Ki-67), especially valuable on small biopsies where architecture is hard to assess ([PMC11404992](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11404992/)). Higher Ki-67 within LCNEC itself has additional prognostic value.
- **TTF-1**: variably positive; TTF-1/c-MYC co-expression phenotypes have been proposed as a stratification tool relevant to DLL3-targeted treatment selection ([PMC8132912](https://pmc.ncbi.nlm.nih.gov/articles/PMC8132912/)).
- WHO recommends that a definitive LCNEC diagnosis, given tissue heterogeneity, be made preferentially on **surgical resection specimens** rather than small biopsies when possible, given sampling limitations.

### Laboratory tests / biomarkers
- Serum NSE, ProGRP, chromogranin A (adjunctive, non-diagnostic).

### Imaging
- **[18F]-FDG PET/CT**: LCNEC exhibits high glucose turnover due to poor differentiation and elevated GLUT1 expression, making FDG-PET well suited to staging, particularly nodal (N) staging, and superior to conventional CT in several validated series ([EJNMMI Research, PMC8298649](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8298649/)).
- **Somatostatin receptor imaging** (¹¹¹In-pentetreotide/Octreoscan, newer ⁶⁸Ga-DOTATATE PET): more established for well-differentiated NETs; utility in high-grade LCNEC (which often has lower/variable SSTR2 expression than low-grade NETs) is comparatively limited, though it may aid staging in select SSTR-avid cases.

### Genetic/genomic testing
- **Comprehensive genomic profiling (CGP)** panels (NGS-based) are increasingly used both for **diagnostic clarification** (distinguishing LCNEC from poorly differentiated NSCLC or SCLC when morphology/IHC is ambiguous) and to inform Type I/Type II molecular subclassification with treatment implications (*Lung Cancer* journal, "Real-World Comprehensive Genomic Profiling Data for Diagnostic Clarity in Pulmonary LCNEC," https://www.lungcancerjournal.info/article/S0169-5002(23)00992-3/fulltext).
- No standardized single-gene or hereditary-panel germline test is indicated given the sporadic somatic etiology.

### Differential diagnosis
Poorly differentiated NSCLC (adenocarcinoma/squamous) lacking neuroendocrine markers; SCLC (smaller cell size, higher nuclear:cytoplasmic ratio, nuclear molding, absent nucleoli — key morphologic discriminators); atypical carcinoid (lower Ki-67, less necrosis).

### Screening
No dedicated LCNEC-specific screening program exists; patients are typically captured within general **low-dose CT lung cancer screening** programs for high-risk smokers, though LCNEC-specific screening-detection yield data were not identified in this search.

---

## 11. Outcome/Prognosis

### Survival statistics (population-based, SEER 2000–2013 cohort)
- **5-year lung cancer-specific survival**: 20.7–20.8%
- **5-year overall survival**: 16.7–16.8%
- **3-year OS / cancer-specific survival**: 22.8% / 26.5% ([PMC6441320](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6441320/))
- **Median overall survival (all comers, mixed-stage)**: reported around 8–12 months in several syntheses; one large cohort reported **median OS 9.7 months** from diagnosis (PMID:33968782-linked synthesis).
- **Metastatic disease**: median OS of only **8 months** for patients with either lung-only or brain-only single-organ metastasis, with 1-year survival rates of 33% and 29% respectively ([PMC8971719](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8971719/)).

### Treatment-outcome-stratified survival (advanced/metastatic disease)
- **Chemotherapy alone**: median OS ~6.5 months.
- **Chemo-immunotherapy**: median OS ~9.6 months (numerically longer, though not always statistically significant in smaller retrospective series) ([ScienceDirect nationwide registry study](https://www.sciencedirect.com/science/article/pii/S0169500225007226)).
- **First-line platinum doublet chemotherapy**: median OS ~9.0 months.
- **Non-platinum chemotherapy**: median OS ~4.0 months.
- **Immune checkpoint inhibitor-containing regimens** (in one series): median OS as high as **26.4 months**, though this likely reflects selection bias toward better-performance-status patients in retrospective cohorts rather than a robustly randomized-trial-confirmed effect size.

### Prognostic factors
- **Stage at diagnosis** (dominant driver of prognosis).
- **Molecular subtype**: NEUROD1-dominant/high-neuroendocrine transcriptional subtype associated with worse OS; YAP1-high/low-neuroendocrine subtype associated with comparatively better prognosis (Nature Communications 2025 integrated characterization).
- **Ki-67 index**: higher values associated with worse survival within the LCNEC category ([PMC11404992](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11404992/)).
- **Complete surgical resection** in early-stage disease is associated with markedly better outcomes; complete resection rates of ~94% with 90-day postoperative mortality of ~7% have been reported in surgical series.
- **Adjuvant chemotherapy** after complete resection, particularly with an **SCLC-type regimen (platinum-etoposide)** rather than an NSCLC-type regimen, is associated with improved survival in several retrospective series, though a randomized-trial-level evidence base is still lacking, and benefit appears more consistent in stage IIB than stage IIA disease ([PMC7736707](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7736707/); [Translational Cancer Research](https://tcr.amegroups.org/article/view/13855/html)).

### Complications
Brain metastasis is common and carries a particularly poor prognosis; other complications parallel those of aggressive lung malignancy generally (post-obstructive pneumonia, pleural effusion, superior vena cava syndrome in central tumors, paraneoplastic morbidity as above).

---

## 12. Treatment

### First-line systemic therapy (advanced/metastatic disease)
- **Platinum–etoposide doublet** chemotherapy has been the standard first-line regimen for metastatic LCNEC for over a decade, based on the phase II **GFPC 0302** study, extrapolating the SCLC treatment paradigm given LCNEC's biological/clinical overlap with SCLC ([synthesis from Frontiers Management of LCNEC, PMID:34513663](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2021.653162/full)). No significant OS difference has been found between platinum-etoposide and platinum-gemcitabine/taxane regimens in comparative retrospective analyses.
- NCIT concept: Chemotherapy (**NCIT:C15632**); Pharmacotherapy (**NCIT:C15986**), with `therapeutic_agent` bound to cisplatin/carboplatin (platinum agents) and etoposide (CHEBI terms available for both).

### Immunotherapy
- **Immune checkpoint inhibitors** (anti-PD-1/PD-L1, alone or combined with chemotherapy) show promising activity, especially in Type II (RB1-altered, immune-pathway-upregulated) tumors.
- **DART (SWOG S1609) basket trial** of combination **nivolumab + ipilimumab** (dual anti-PD-1/anti-CTLA-4 blockade) in the high-grade/non-pancreatic neuroendocrine carcinoma cohort reported an objective response rate of **44%** in the high-grade neuroendocrine carcinoma subset specifically (vs. 0% ORR in low/intermediate-grade disease), and 25–26% ORR in the broader nonpancreatic/high-grade cohorts overall (Patel et al., **PMID:31969335**; companion high-grade NEN cohort report **PMID:33882143**). Dosing: ipilimumab 1 mg/kg IV every 6 weeks + nivolumab 240 mg IV every 2 weeks.
- Ongoing prospective trials are testing **atezolizumab + platinum/etoposide** as first-line therapy specifically in advanced pulmonary LCNEC (NCT05470595), and pembrolizumab-based regimens in previously treated high-grade neuroendocrine carcinomas broadly.
- STK11/KEAP1 co-mutated (Type I) tumors are, by analogy with the broader NSCLC literature, associated with **relative immunotherapy resistance** — a molecularly grounded rationale for future biomarker-stratified trial design.

### Emerging/targeted therapy
- **DLL3-targeted therapy**: DLL3 (Notch-ligand family) is expressed on the surface of a majority of SCLC cells and is also expressed in LCNEC (particularly the ASCL1^high/DLL3^high Type I subgroup), representing a tumor-restricted therapeutic target absent from normal tissue.
  - **Rovalpituzumab tesirine (Rova-T)**, a DLL3-targeted antibody-drug conjugate, showed early promise in phase II but failed in phase III trials and was discontinued.
  - **Tarlatamab**, a DLL3×CD3 bispecific T-cell engager, achieved a 55% objective response rate and median PFS of 4.9 months in the phase 2 **DeLLphi-301** trial (in SCLC); case reports document partial responses in LCNEC as well, including in a young-adult patient ([JTO Clin Res Rep](https://www.jtocrr.org/article/S2666-3643(24)00082-1/fulltext); [PMC11986208](https://pmc.ncbi.nlm.nih.gov/articles/PMC11986208/)). Cytokine release syndrome is a recognized, generally manageable toxicity.
  - NCIT/therapeutic-modality mapping: `therapeutic_modality: ANTISENSE_OLIGONUCLEOTIDE` does not apply here — tarlatamab and Rova-T fall under `MONOCLONAL_ANTIBODY`/bispecific-engager and antibody-drug-conjugate categories respectively (best captured as `MONOCLONAL_ANTIBODY` or `OTHER` pending a dedicated bispecific-T-cell-engager modality value).

### Surgery
- **Surgical resection** with curative intent is the treatment of choice for early-stage (resectable) LCNEC, given the tumor's biological ambiguity and the general principle that localized high-grade lung tumors benefit from resection when feasible ([EJNMMI Research](https://ejnmmires.springeropen.com/articles/10.1186/s13550-021-00811-9)). NCIT: Surgical Procedure (**NCIT:C15329**).

### Radiation
- Radiotherapy is used in the definitive, adjuvant, and palliative settings, including for brain metastasis management (whole-brain RT or stereotactic radiosurgery, by analogy with SCLC brain-metastasis management, though LCNEC-specific prophylactic cranial irradiation data are not well established).

### Combination/sequential strategies
- Endostar (an anti-angiogenic agent) plus pembrolizumab combined with platinum-doublet chemotherapy has been reported in case-report form as a novel first-line approach for advanced pulmonary LCNEC ([PMC9202532](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9202532/)).
- Cabozantinib + nivolumab + ipilimumab is under investigation for poorly differentiated neuroendocrine tumors broadly (NCT04079712).

### Treatment for extrapulmonary LCNEC
Platinum-based chemotherapy (mirroring SCLC/pulmonary LCNEC management) remains the standard-of-care backbone for extrapulmonary neuroendocrine carcinomas of any primary site, with further site-specific and biomarker-driven approaches under active investigation ([PMC10743506](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10743506/)).

---

## 13. Prevention

No LCNEC-specific primary, secondary, or tertiary prevention program was identified in the literature reviewed. Given the overwhelming (92–98%) association with tobacco smoking, **primary prevention via smoking cessation and tobacco control** is the principal actionable prevention lever, consistent with lung cancer prevention broadly (CDC/WHO tobacco control frameworks). **Secondary prevention** (early detection) relies on inclusion within standard **low-dose CT lung cancer screening** programs for eligible high-risk smokers, though LCNEC-specific screening sensitivity/yield data were not found. No LCNEC-specific vaccine, chemoprophylaxis, or genetic/carrier screening program exists, consistent with its sporadic somatic (non-hereditary) etiology.

---

## 14. Other Species / Natural Disease

Naturally occurring LCNEC as a distinct veterinary clinical entity is not well documented in the literature surfaced by this search; pulmonary neuroendocrine tumors are reported in veterinary oncology literature more generally, but a dedicated OMIA (Online Mendelian Inheritance in Animals) entry or veterinary case-series literature specific to "large cell neuroendocrine carcinoma" was not identified — noted here as a **data gap** rather than a confirmed absence.

---

## 15. Model Organisms

### Genetically engineered mouse models (GEMMs)
The most directly relevant and well-characterized model system is the **quadruple-knockout (QKO) mouse**: conditional inactivation of **Rb1, Rbl1 (p130), Pten, and Trp53** in lung epithelium.
- **Cre-driver-dependent phenotype divergence** (Ferone et al., *PNAS* 2020, https://www.pnas.org/doi/10.1073/pnas.1821745116):
  - **Ad5-CMV-Cre** (targets all lung epithelial cell types) → **large-cell neuroendocrine carcinoma**.
  - **Ad5-K5-Cre** (targets basal cells specifically) → **small-cell lung carcinoma**.
- This model directly demonstrates **cell-of-origin as a determinant of neuroendocrine lung cancer histologic subtype** given an identical combinatorial genetic lesion (Rb1/Rbl1/Pten/Trp53 loss), closely recapitulating the human TP53/RB1 co-mutation signature that defines "Type II/SCLC-like" LCNEC.
- **Phenotype recapitulation**: the model produces "high-grade malignant neuroendocrine lung carcinomas strikingly similar to human disease," supporting high translational fidelity for the RB1/TP53-co-mutant molecular subtype specifically; it is less directly informative for the STK11/KEAP1-mutant ("Type I") molecular subtype, which would require a distinct genetic-lesion combination not centered on Rb1 loss.
- **Trp53 mutant-specific models**: Trp53 point-mutant (rather than null) alleles have been shown to drive neuroendocrine lung cancer through a combination of loss-of-function and gain-of-function mechanisms, the latter specifically affecting chemotherapy response (Sotillo et al., *Mol Cancer Ther* 2017, **PMID:** available via https://pmc.ncbi.nlm.nih.gov/articles/PMC5716875/), offering a model for studying platinum-etoposide chemoresistance mechanisms.

### Other model systems
- **Patient-derived cell lines/xenografts (PDX)**: referenced in genomic-profiling and DLL3/tarlatamab preclinical literature but not exhaustively catalogued in this search; LCNEC-specific cell lines exist within broader neuroendocrine lung cancer cell line resources (e.g., within DepMap/Cellosaurus), though a dedicated LCNEC PDX registry akin to CCLE/DepMap-style comprehensive catalogs was not surfaced.
- **EGFR-mutant transformation models**: mouse and cell-line models of EGFR-TKI-resistant transdifferentiation from adenocarcinoma to SCLC/LCNEC, centered on Rb1 biallelic inactivation, are used to study the acquired-resistance mechanistic pathway (search synthesis referencing PNAS 2020 and related EGFR-transdifferentiation literature).

### Applications and limitations
These GEMMs are principally used to study: (1) the causal sufficiency of the TP53/RB1/Pten tumor-suppressor combination for high-grade neuroendocrine lung carcinoma, (2) the cell-of-origin determinant of LCNEC-vs-SCLC histologic fate, and (3) chemotherapy-response mechanisms tied to specific Trp53 mutant alleles. A key **limitation** is that no widely used GEMM directly models the STK11/KEAP1-driven "Type I" molecular subtype of human LCNEC, representing a translational gap for roughly a third of human cases.

---

## Summary of Key Ontology-Term Suggestions

| Domain | Suggested term(s) |
|---|---|
| Disease | MONDO (large cell neuroendocrine carcinoma, organ-specific children); ICD-O-3 8013/3 |
| Causal genes | HGNC:11998 (TP53), HGNC:9884 (RB1), HGNC:11389 (STK11), HGNC:6396 (KEAP1), HGNC:6407 (KRAS) |
| Cell of origin | CL:0002251 (pulmonary neuroendocrine cell) |
| Anatomy | UBERON:0002048 (lung), UBERON:0002185 (bronchus) |
| Key phenotypes | HP:0012735 (Cough), HP:0002105 (Hemoptysis), HP:0002902 (Hyponatremia), HP:0000174 (Cushingoid facies), HP:0003473 (Myasthenia), HP:0002383 (Encephalitis), HP:0001824 (Weight loss) |
| Biological processes | GO:0007219 (Notch signaling pathway), GO:0006977 (DNA damage response, p53 mediator), GO:1901031 (regulation of response to oxidative stress) |
| Treatments | NCIT:C15632 (Chemotherapy), NCIT:C15986 (Pharmacotherapy), NCIT:C15329 (Surgical Procedure), NCIT:C15313 (Radiation Therapy) |

---

## Sources

- [Integrative genomic profiling of large-cell neuroendocrine carcinomas reveals distinct subtypes of high-grade neuroendocrine lung tumors (George et al., Nat Commun 2018, PMID:29535388)](https://www.nature.com/articles/s41467-018-03099-x)
- [Genomic Profiling of Large-Cell Neuroendocrine Carcinoma of the Lung, Clin Cancer Res](https://aacrjournals.org/clincancerres/article/23/3/757/80338/Genomic-Profiling-of-Large-Cell-Neuroendocrine)
- [Molecular Pathology of Pulmonary Large Cell Neuroendocrine Carcinoma: Novel Concepts and Treatments, PMC8100606](https://pmc.ncbi.nlm.nih.gov/articles/PMC8100606/)
- [Genomic Profiling and Clinicopathological Characteristics of Neuroendocrine Tumors of the Lung in East Asian Patients, PMID:33144445](https://pubmed.ncbi.nlm.nih.gov/33144445/)
- [Real-World comprehensive genomic profiling data for diagnostic clarity in pulmonary Large-Cell neuroendocrine carcinoma, Lung Cancer](https://www.lungcancerjournal.info/article/S0169-5002(23)00992-3/fulltext)
- [Integrated molecular and clinical characterization of pulmonary large cell neuroendocrine carcinoma, Nature Communications 2025](https://www.nature.com/articles/s41467-025-63091-0)
- [Molecular Subtypes of Neuroendocrine Carcinoma, Annual Reviews](https://www.annualreviews.org/content/journals/10.1146/annurev-pathmechdis-042524-023153)
- [New molecular classification of large cell neuroendocrine carcinoma and small cell lung carcinoma with potential therapeutic impacts, Transl Lung Cancer Res](https://tlcr.amegroups.org/article/view/39956/html)
- [Molecular subtypes of neuroendocrine carcinomas: A cross-tissue classification framework based on five transcriptional regulators, Cancer Cell](https://www.cell.com/cancer-cell/fulltext/S1535-6108(24)00163-6)
- [Comprehensive Analysis of NEUROD1, ASCL1, POU2F3, and YAP1 Expression Signatures Reveals Unique LCNEC Subgroups](https://www.sciencedirect.com/science/article/pii/S0023683725001448)
- [Prototypical oncogene family Myc defines unappreciated distinct lineage states of small cell lung cancer, Science Advances](https://www.science.org/doi/10.1126/sciadv.abc2578)
- [Differential development of large-cell neuroendocrine or small-cell lung carcinoma upon inactivation of 4 tumor suppressor genes, PNAS 2020](https://www.pnas.org/doi/10.1073/pnas.1821745116)
- [TRP53 Mutants Drive Neuroendocrine Lung Cancer Through Loss-of-Function Mechanisms with Gain-of-Function Effects on Chemotherapy Response, Mol Cancer Ther](https://pmc.ncbi.nlm.nih.gov/articles/PMC5716875/)
- [Clinical and morphological features of large-cell neuroendocrine carcinomas and small-cell lung carcinomas expressing DLL3 and ASCL1 oncoproteins, PMC10739177](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10739177/)
- [TTF-1 and c-MYC-defined Phenotypes of Large Cell Neuroendocrine Carcinoma and DLL3 Expression for Treatment Selection, PMC8132912](https://pmc.ncbi.nlm.nih.gov/articles/PMC8132912/)
- [Targeting DLL3: A New Weapon in Lung Neuroendocrine Tumors?, PMC11986208](https://pmc.ncbi.nlm.nih.gov/articles/PMC11986208/)
- [Tarlatamab for Large Cell Neuroendocrine Carcinoma in a Young Adult: A Case Report, JTO Clin Res Rep](https://www.jtocrr.org/article/S2666-3643(24)00082-1/fulltext)
- [Large Cell Neuroendocrine Carcinoma of the Lung: Clinico-Pathologic Features, Treatment, and Outcomes, PMC5474315](https://pmc.ncbi.nlm.nih.gov/articles/PMC5474315/)
- [Outcomes of Patients with Pulmonary Large Cell Neuroendocrine Carcinoma in I–IV Stage, PMC7911070](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7911070/)
- [Comprehensive Dissection of Treatment Patterns and Outcome for Patients With Metastatic LCNEC, PMC8295750](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8295750/)
- [The Effectiveness of Atezolizumab in Metastatic LCNEC: LANCE Pilot Study, PMC11200835](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11200835/)
- [Based on SEER Database: Population Distribution, Survival Analysis, and Prognostic Factors of Organ Metastasis of Lung LCNEC, PMC8971719](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8971719/)
- [The prognosis analysis of organ metastatic patterns in lung LCNEC: A population-based study, PMC9773085](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9773085/)
- [Clinicopathological characteristics, treatment and survival of pulmonary LCNEC: a SEER population-based study, PMC6441320](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6441320/)
- [Large-Cell Neuroendocrine Carcinoma of the Lung: A Population-Based Study, ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S1525730419302153)
- [Pulmonary Large Cell Neuroendocrine Carcinoma: A Rare Type of Non-Small Cell Lung Cancer, PMC8162139](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8162139/)
- [Clinicopathological characteristics and prognosis of pulmonary LCNEC aged ≥65 years, PMC6532618](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6532618/)
- [Large Cell Neuroendocrine Carcinoma of the Lung: A Case Series of 14 Cases, PMC9428409](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9428409/)
- [Survival outcomes of surgery in patients with pulmonary LCNEC, PMC7881654](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7881654/)
- [Management of Large Cell Neuroendocrine Carcinoma, Frontiers in Oncology, PMID:34513663](https://www.frontiersin.org/journals/oncology/articles/10.3389/fonc.2021.653162/full)
- [Genomic profiling of high-grade large-cell neuroendocrine carcinoma of the colon, J Gastrointest Oncol](https://jgo.amegroups.org/article/view/5031/html)
- [Extrapulmonary Neuroendocrine Carcinomas: Current Management and Future Perspectives, PMC10743506](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10743506/)
- [Managing Metastatic Extrapulmonary Neuroendocrine Carcinoma After First-Line Treatment, Curr Oncol Rep](https://link.springer.com/article/10.1007/s11912-023-01438-w)
- [Clinical Features and Outcomes Analysis of Surgical Resected Pulmonary LCNEC With Adjuvant Chemotherapy, PMC7736707](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7736707/)
- [Outcomes of patients with LCNEC of the lung after complete resection, Transl Cancer Res](https://tcr.amegroups.org/article/view/13855/html)
- [Outcomes for Surgery in Large Cell Lung Neuroendocrine Cancer, J Thorac Oncol](https://www.jto.org/article/S1556-0864(19)33306-4/fulltext)
- [A Phase II Basket Trial of Dual Anti-CTLA-4 and Anti-PD-1 Blockade in Rare Tumors (DART SWOG 1609) in Patients with Nonpancreatic Neuroendocrine Tumors, PMID:31969335](https://pubmed.ncbi.nlm.nih.gov/31969335/)
- [Phase II basket trial DART SWOG S1609: High-grade neuroendocrine neoplasm cohort, PMID:33882143](https://pubmed.ncbi.nlm.nih.gov/33882143/)
- [A Case of Paraneoplastic Neurological Syndrome Leading to the Diagnosis of LCNEC From Opsoclonus-Myoclonus Syndrome, PMC10725307](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10725307/)
- [N-staging in large cell neuroendocrine carcinoma of the lung: diagnostic value of [18F]FDG PET/CT, EJNMMI Research, PMC8298649](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8298649/)
- [Effect of Ki-67 proliferation index on survival in large cell neuroendocrine carcinoma of the lung, PMC11404992](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11404992/)
- [Pathology Outlines - Large cell neuroendocrine carcinoma](https://www.pathologyoutlines.com/topic/lungtumorlargecellne.html)
- [Large cell neuroendocrine carcinoma of the lung, Wikipedia](https://en.wikipedia.org/wiki/Large_cell_neuroendocrine_carcinoma_of_the_lung)
- [large cell neuroendocrine carcinoma, National Organization for Rare Disorders / MONDO](https://rarediseases.org/mondo-disease/large-cell-neuroendocrine-carcinoma/)
- [Large Cell Neuroendocrine Carcinoma of the Lung: Current Understanding and Challenges, PMC8911276](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8911276/)
- [Large Cell Neuro-Endocrine Carcinoma of the Lung: Current Treatment Options and Potential Future Opportunities, PMC8081906](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8081906/)
- [Large cell neuroendocrine lung carcinoma: consensus statement from The British Thoracic Oncology Group and the Association of Pulmonary Pathologists, Br J Cancer](https://www.nature.com/articles/s41416-021-01407-9)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 35 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 35 |
| On topic | 31 |
| Off topic | 0 |

All extracted references resolved successfully.