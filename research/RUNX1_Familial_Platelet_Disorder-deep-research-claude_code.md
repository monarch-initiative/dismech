---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-31T19:54:40.088219'
end_time: '2026-08-31T19:59:47.702973'
duration_seconds: 307.61
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: RUNX1 Familial Platelet Disorder with Associated Myeloid Malignancy
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
  web_search_requests: 15
  num_turns: 21
  total_cost_usd: 1.3096565999999998
  session_id: 70de5b01-cdc4-5635-9abb-0681d0e2fde9
  stop_reason: end_turn
  assistant_text_blocks: 3
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderAuthError
  status_code: 403
  remedy: the API key is missing, invalid, or lacks access to this endpoint
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 36
reference_validation:
  total_references: 17
  verified: 17
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 6
  quotes_valid: 4
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:41924923
  - DOI:10.1002/hem3.70057
  relevance_assessed: 17
  on_topic: 15
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 38
  verified: 35
  not_found: 0
  obsolete: 1
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 21
  labels_matching: 11
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: HP:0002488
    reported_labels:
    - "Acute myeloid leukemia would map via MONDO/HP disease terms rather than phenotype\
      \ terms \u2014 flag for curation"
    ontology_label: Acute leukemia
  - term_id: HP:0005506
    reported_labels:
    - Leukemia, general
    ontology_label: Chronic myelogenous leukemia
  - term_id: UBERON:0001977
    reported_labels:
    - "platelet \u2014 note: UBERON models platelet as a cell type via CL, not strictly\
      \ organ"
    ontology_label: blood serum
  labels_variant: 7
  obsolete_terms:
  - term_id: GO:0043433
    ontology_label: obsolete negative regulation of DNA-binding transcription factor
      activity
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** RUNX1 Familial Platelet Disorder with Associated Myeloid Malignancy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **RUNX1 Familial Platelet Disorder with Associated Myeloid Malignancy** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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

I'll research RUNX1-FPDMM using web search and fetch tools to gather current, well-cited information.

I have enough material to compile a comprehensive, well-cited report now.

I now have sufficient depth and citations to write the full report.

---

# RUNX1 Familial Platelet Disorder with Associated Myeloid Malignancy (RUNX1‑FPDMM): Comprehensive Research Report

## 1. Disease Information

**Overview.** RUNX1‑FPDMM (also called FPD/AML, familial platelet disorder with propensity to myeloid malignancy, or "hereditary thrombocytopenia and hematological cancer predisposition syndrome associated with RUNX1") is an autosomal dominant condition caused by heterozygous germline pathogenic variants in *RUNX1*. It is defined by (1) quantitative and qualitative platelet defects causing a bleeding diathesis and (2) a markedly elevated, lifelong risk of myeloid malignancy — principally myelodysplastic syndrome (MDS) and acute myeloid leukemia (AML), with T‑ and B‑cell acute lymphoblastic leukemia also reported ([GeneReviews, updated 2024–2025](https://www.ncbi.nlm.nih.gov/books/NBK568319/)). It was first delineated as a Mendelian entity by Song et al. in 1999 and is now formally recognized by the WHO 5th‑edition and ICC classifications as a prototypic "myeloid neoplasm with germline predisposition and pre-existing platelet disorder."

**Key identifiers:**
- OMIM disease: **#601399** — Platelet Disorder, Familial, with Associated Myeloid Malignancy (FPDMM) ([OMIM](https://omim.org/entry/601399))
- OMIM gene (*RUNX1*): **\*151385**, chromosome **21q22.12** ([OMIM](https://www.omim.org/entry/151385))
- HGNC: gene ID **10471**
- Orphanet: **ORPHA:71290** — Familial platelet disorder with associated myeloid malignancy ([Orphanet](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=71290&Lng=GB))
- MONDO: **MONDO:0100083**
- ClinVar condition record example: NM_001754.5(RUNX1):c.602G>A (p.Arg201Gln) AND "Hereditary thrombocytopenia and hematological cancer predisposition syndrome associated with RUNX1" ([ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/RCV000015550/))
- NCI PDQ summary exists as a dedicated cancer genetics resource: "RUNX1‑Familial Platelet Disorder (PDQ®)" ([NCBI Bookshelf NBK598339](https://www.ncbi.nlm.nih.gov/books/NBK598339/))

**Synonyms:** FPD/AML; familial platelet disorder with propensity to AML; thrombocytopenia 2 (historic); familial platelet syndrome with predisposition to acute myelogenous leukemia (Orphanet synonym).

**Evidence basis:** This entry is derived almost entirely from aggregated disease-level resources — GeneReviews, OMIM, Orphanet, WHO/ICC classification, ClinGen curation, and case-series/cohort literature (~200 families and >130 individuals reported cumulatively) — rather than from a single large EHR population, reflecting genuine rarity.

---

## 2. Etiology

**Primary cause:** Heterozygous germline loss-of-function or dominant-negative pathogenic variants in *RUNX1* (encoding RUNX1/AML1/CBFA2, a core-binding transcription factor that heterodimerizes with CBFβ). This is a purely monogenic, highly penetrant-for-phenotype/variably-penetrant-for-malignancy Mendelian disorder — there is no known environmental or infectious primary cause of the germline predisposition itself.

**Genetic risk factors:**
- **Causal variants:** ~80% are detected by sequence analysis — missense, nonsense, splice-site variants, and small indels, concentrated in the **Runt homology domain (RHD)**, which mediates both DNA binding and CBFβ heterodimerization; variants also occur in the **transactivation domain (TAD)** and at splice sites. ~20% are gross deletions/duplications (including whole-gene deletion) detected by dosage analysis ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK568319/)).
- **Mechanistic classes:** frameshift and large deletions → haploinsufficiency (loss-of-function); some missense/nonsense variants in the RHD act as **dominant-negative** alleles that impair DNA binding/transactivation of the wild-type allele product, generally associated with a more severe phenotype than simple haploinsufficiency ([Simon et al., *Leukemia* 2020, functional classification of RUNX1 variants](https://www.nature.com/articles/s41375-021-01200-w)).
- **Second-hit/somatic modifier variants driving progression to malignancy:** somatic pathogenic variants in *ASXL1, CBL, CDC25C, FLT3, PHF6, SRSF2,* and *WT1*, plus loss of the remaining wild-type *RUNX1* allele (often via **acquired uniparental disomy of chromosome 21**, or biallelic RUNX1 inactivation). Age-related clonal hematopoiesis genes — **TET2 and DNMT3A** — are the most frequently observed secondary somatic variants in surveillance cohorts and are thought to mark early clonal evolution rather than transformation itself ([PMC9320507, "Beyond Pathogenic RUNX1 Germline Variants"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9320507/)).
- **Genotype–severity correlation:** functional class (null/haploinsufficient vs. dominant-negative) and possibly variant location within RHD vs. TAD influence leukemogenic risk, though penetrance remains incompletely predictable from genotype alone.

**Environmental/lifestyle risk factors:** Not disease-causing, but GeneReviews management guidance flags **obesity and chemical/genotoxic exposure** (e.g., unnecessary ionizing radiation, tobacco smoke) as plausible modifiers that may increase malignancy risk in carriers, and recommends avoidance as a precaution rather than as an evidence-graded finding.

**Protective factors:** No validated genetic or environmental protective factors are established in the literature; this remains an evidence gap.

**Gene–environment interaction:** No specific GxE interaction has been characterized; the dominant model is a two-(or multi-)hit somatic evolution model layered on a haploinsufficient/dominant-negative germline background, analogous to but mechanistically distinct from classical tumor-suppressor two-hit kinetics (biallelic inactivation is one but not the only path to leukemic transformation here — cooperating epigenetic-regulator mutations are more common).

---

## 3. Phenotypes

**Bleeding/platelet phenotype** (present in ~90% of affected individuals):
- **Thrombocytopenia:** typically mild-to-moderate (platelet counts 50–150 × 10⁹/L); a subset have normal counts (>150 × 10⁹/L) despite qualitative dysfunction.
- **Qualitative platelet dysfunction** exceeding what platelet count alone predicts: abnormal aggregation (blunted response to arachidonic acid, collagen, ADP, epinephrine), abnormal secretion, and **platelet dense-granule and/or alpha-granule storage pool deficiency** on electron microscopy in roughly half of tested patients.
- **Clinical bleeding:** easy bruising without trauma, mucocutaneous bleeding, gum bleeding, menorrhagia, peri-/post-partum hemorrhage, excess surgical/dental bleeding; **20–25%** require platelet transfusion or antifibrinolytics for hemostatic challenges ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK568319/)).
- Suggested HPO terms: HP:0001873 (Thrombocytopenia), HP:0011869 (Abnormal platelet function), HP:0000978 (Bruising susceptibility), HP:0000979 (Purpura), HP:0000032 (Dysmenorrhea/Menorrhagia — HP:0000132 Menorrhagia), HP:0011024 (Abnormality of the digestive system — for GI bleeding as needed).

**Hematologic malignancy phenotype:**
- Lifetime risk of hematologic malignancy: **~35–50%** (frequently cited as ~44% by age 50) ([HemaSphere 2025, Ernst et al.](https://onlinelibrary.wiley.com/doi/full/10.1002/hem3.70057); [natural history study, Blood 2023, PMID 37738626](https://ashpublications.org/blood/article/142/25/2146/498043/Natural-history-study-of-patients-with-familial)).
- Median age of malignancy onset: **33 years**, though pediatric- and later adult-onset cases both occur.
- Predominant malignancies: AML and MDS are the most common initial presentations (AML in ~26.9%, MDS in ~13.4% of malignancy presentations in cohort data); T‑ and B‑cell ALL and lymphomas occur in a minority of families (~25% of families report a lymphoid malignancy at some point).
- HPO terms: HP:0004808 (Myelodysplasia), HP:0004808-adjacent HP:0002488 (Acute myeloid leukemia would map via MONDO/HP disease terms rather than phenotype terms — flag for curation), HP:0005506 (Leukemia, general).

**Skin manifestations:** eczema and/or psoriasis reported in ~50% of families, typically childhood-onset and mild, managed topically (HP:0000964 Eczema; HP:0003765 Psoriasiform dermatitis / HP:0003765).

**Bone marrow histopathology:** hypocellular-to-normocellular marrow; **atypical, non-dysplastic megakaryocytes** — small, hypolobated, scant cytoplasm — a described feature distinguishing pre-leukemic RUNX1-FPDMM marrow from classic MDS dysplasia ([Haematologica, bone marrow pathology in FPDMM](https://haematologica.org/article/view/8214)).

**Quality of life:** No dedicated EQ-5D/SF-36 disease-specific data were identified in the literature; qualitative burden is described via chronic bleeding-diathesis management, psychosocial impact of unexplained bruising (including risk of misattributed child-abuse concern, explicitly flagged in GeneReviews management guidance), and the substantial anxiety burden of lifelong malignancy surveillance — this is a genuine evidence gap rather than an omission.

---

## 4. Genetic/Molecular Information

**Causal gene:** *RUNX1* (RUNX Family Transcription Factor 1; previously AML1/CBFA2), HGNC:10471, chromosome 21q22.12, 12 exons.

**Protein domains:**
- **Runt homology domain (RHD)**, exons 2–4, ~128 amino acids: mediates sequence-specific DNA binding (5′-PyGPyGGTPy-3′ consensus) and heterodimerization with **CBFβ**, which stabilizes RHD–DNA contacts. Most pathogenic missense/nonsense variants cluster here ([ScienceDirect structural review](https://www.sciencedirect.com/science/article/abs/pii/S1079979603000226); [GeneCards](https://www.genecards.org/card/RUNX1)).
- **Transactivation domain (TAD)**, C-terminal/exon 6 region: required for transcriptional activation and contains a nuclear matrix-targeting signal essential for in vivo function.

**Variant spectrum and classification (ACMG/AMP-graded):**
- Missense, nonsense, frameshift, splice-site variants, and small indels (~80% of pathogenic findings by sequence analysis) plus gross deletions/duplications, including whole-gene deletion (~20%, detected by CNV/dosage analysis).
- ClinVar carries numerous graded examples, e.g., NM_001754.5(RUNX1):c.602G>A (p.Arg201Gln) and c.1283dup (p.Leu429fs) associated with "Hereditary thrombocytopenia and hematological cancer predisposition syndrome associated with RUNX1."
- **Functional classification (Simon et al., *Leukemia* 2021)** stratifies variants by transcriptional activity into loss-of-function/haploinsufficient vs. dominant-negative classes, which correlates with clinical severity ([Nature/Leukemia](https://www.nature.com/articles/s41375-021-01200-w)).
- gnomAD/population databases: pathogenic RUNX1-FPDMM variants are essentially absent or present only as extreme rarities in the general population given the phenotype's severity and rarity (~200 families reported worldwide); this is consistent with dominant, disease-causing rarity rather than a common-variant susceptibility architecture.

**Somatic vs. germline distinction (critical for testing):**
- Somatic *RUNX1* mutations are common in sporadic AML/MDS and in breast cancer, unrelated to germline predisposition; **variant allele fraction <40%** in tumor tissue is a practical (not absolute) heuristic suggesting a somatic rather than constitutional origin ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK568319/)).
- Critical technical pitfall: **acquired loss of heterozygosity via uniparental disomy of chromosome 21** can occur in hematopoietic tissue of carriers, causing false-negative *germline* testing results from blood/marrow DNA. GeneReviews explicitly recommends **cultured skin fibroblasts** (buccal samples as a fallback, with risk of blood contamination) for definitive germline testing, and states testing during active malignancy is unreliable because ~10% of *sporadic* hematologic malignancy cases carry (typically somatic) RUNX1 variants incidentally.

**Somatic "second hits" driving leukemic transformation:** most frequently affect epigenetic regulators **TET2** and **DNMT3A** (age-related clonal hematopoiesis genes, seen on longitudinal surveillance), plus cooperating driver mutations in *ASXL1, CBL, CDC25C, FLT3, PHF6, SRSF2, WT1*, and biallelic *RUNX1* loss ([PMC9320507](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9320507/); [Blood Advances 2024, genomic landscape](https://ashpublications.org/bloodadvances/article/8/2/497/498801/Genomic-landscape-of-patients-with-germline-RUNX1)). A 2025 focused study (PMC11919008) further characterizes germline RUNX1 variant frequency and function specifically within diagnosed myeloid neoplasm cohorts.

**Modifier genes:** No validated independent modifier locus beyond the acquired somatic events above; functional variant class (haploinsufficient vs. dominant-negative) is currently the best-supported intrinsic modifier of risk.

**Epigenetics:** RUNX1 haploinsufficiency itself alters chromatin/transcriptional output at hematopoietic target loci (see Mechanism, below); no disease-specific DNA methylation biomarker panel is yet clinically validated, though clonal TET2/DNMT3A mutations (epigenetic regulators) are mechanistically linked to progression.

**Chromosomal abnormalities:** Whole-gene or partial-gene deletions of *RUNX1* (21q22.12) are a recognized causal mechanism (~20% of pathogenic findings), detectable by chromosomal microarray/MLPA; distinguish from **constitutional trisomy 21 (Down syndrome)**, which independently confers its own myeloid leukemia predisposition through a different (GATA1-related, transient abnormal myelopoiesis) mechanism — a differential that should not be conflated with RUNX1-FPDMM.

---

## 5. Environmental Information

RUNX1‑FPDMM is a purely monogenic predisposition; environmental factors modulate the timing/likelihood of second-hit malignant transformation rather than causing the underlying platelet/predisposition phenotype.

- **Chemical/toxin exposure:** GeneReviews management guidance advises avoidance of unnecessary genotoxic exposures (radiation, tobacco smoke, occupational chemical exposures) as a precautionary measure to reduce mutagenic pressure on the already-haploinsufficient hematopoietic compartment, though this is expert consensus rather than a quantified epidemiologic effect size.
- **Lifestyle factors:** Obesity is flagged as a possible malignancy-risk modifier; NSAIDs, antiplatelet agents, and statins are specifically listed as agents to avoid because they can unmask or worsen the underlying qualitative platelet defect (bleeding risk, not malignancy risk).
- **Infectious agents:** No infectious trigger has been identified or is biologically plausible as a primary driver; this is not an infection-associated disease.

---

## 6. Mechanism / Pathophysiology

### Causal chain (numbered, from germline lesion to clinical manifestations)

1. A heterozygous germline pathogenic variant in *RUNX1* **reduces functional RUNX1 dosage** in hematopoietic stem/progenitor cells — either by simple loss-of-function/haploinsufficiency (frameshift, nonsense, deletion) or by a **dominant-negative** mechanism in which a mutant RHD protein still binds CBFβ/DNA but fails to transactivate target genes, poisoning the wild-type allele's output (Simon et al. 2021).
2. Reduced RUNX1:CBFβ transcriptional activity **impairs megakaryocyte maturation and polyploidization**, demonstrated directly in a rhesus macaque RUNX1-FPDMM model in which CD34+ HSPCs showed "impaired in vitro megakaryocytic differentiation, with a striking defect in polyploidization" and marrow "megakaryocytic dysplasia similar to human FPDMM" (Blood 2023, DOI 10.1182/blood.2022018193, PMID 36322931).
3. This leads to **quantitative thrombocytopenia** (reduced platelet output from dysplastic megakaryocytes) — the clinical bleeding phenotype's first component.
4. In parallel, RUNX1 haploinsufficiency directly **downregulates specific platelet-granule biogenesis genes**, most notably **PLDN** (pallidin), a subunit of the BLOC-1 complex required for dense-granule biogenesis: "PLDN is a direct transcriptional target of RUNX1, and its decreased expression constitutes a mechanism for the platelet dense granule deficiency in patients with RUNX1 haplodeficiency" ([ASH abstract, PLDN mechanism](https://ashpublications.org/blood/article/122/21/567/94164/RUNX1-Regulates-PLDN-Pallidin-Expression-In)). Additional dysregulated RUNX1 targets include **RAB27B, MYL9, ALOX12, PF4, PRKCQ (PKC‑θ), RAB1B, TREML1, ITGA2, MPL, NFE2, NOTCH4,** and **A4GALT**.
5. Loss of these targets produces **qualitative platelet dysfunction**: decreased aggregation, decreased secretion (dense- and alpha-granule storage pool deficiency, plus a broader defect in acid-hydrolase/lysosomal secretion independent of granule content — [Haemophilia 2017, Rao et al.](https://onlinelibrary.wiley.com/doi/10.1111/hae.13280)), reduced myosin light chain/pleckstrin phosphorylation, reduced 12-HETE production, and impaired αIIbβ3 activation ([J Thromb Haemost 2014, Glembotsky et al., PMID 24606315](https://pubmed.ncbi.nlm.nih.gov/24606315/)). This qualitative defect explains why **bleeding severity exceeds what platelet count alone predicts**.
6. Independently, chronically reduced RUNX1 dosage in hematopoietic stem cells creates a **pre-leukemic clonal state**: the residual (haploinsufficient or dominant-negative-poisoned) HSC/progenitor pool is intrinsically primed for clonal drift. In the rhesus macaque model, RUNX1-edited HSPC clones **progressively expanded relative to control-edited clones over time** even without additional mutations — direct in vivo evidence that reduced RUNX1 dosage alone confers a clonal competitive advantage.
7. Over years, this primed clone **acquires cooperating somatic ("second-hit") mutations** — most commonly in the epigenetic regulators **TET2** and **DNMT3A** (age-related clonal hematopoiesis genes), and less commonly in *ASXL1, CBL, CDC25C, FLT3, PHF6, SRSF2, WT1*, or biallelic *RUNX1* inactivation (frequently via acquired uniparental disomy of chromosome 21) ([Genomic Landscape studies](https://www.sciencedirect.com/science/article/pii/S0006497121030743); [Blood Advances 2024](https://ashpublications.org/bloodadvances/article/8/2/497/498801/Genomic-landscape-of-patients-with-germline-RUNX1)).
8. Clonal outgrowth with these cooperating lesions **leads to** myelodysplastic syndrome — marrow dysplasia and cytopenias — which in a substantial fraction of patients **progresses to** overt acute myeloid leukemia (or, less commonly, T-/B-lymphoblastic leukemia/lymphoma via a still less well-characterized branch of the same predisposed hematopoietic compartment).
9. Because malignant transformation depends on this multi-hit somatic evolution layered on a chronically haploinsufficient stem cell compartment, **RUNX1‑FPDMM-associated leukemia is not curable with chemotherapy alone** — the germline lesion persists in every surviving HSC — and **allogeneic hematopoietic stem cell transplantation is the only curative modality**, a direct mechanistic consequence of step 1 rather than merely a treatment-guideline statement.

**Branch point (step 9, inferred/translationally important):** the rhesus macaque data specifically predict that **autologous gene-correction/gene-therapy approaches will be mechanistically challenged**, because corrected (wild-type-restored) HSPCs did *not* show a competitive advantage over RUNX1-heterozygous mutant HSPCs long-term in the primate model — i.e., simply correcting a fraction of stem cells may not be sufficient to outcompete the pre-existing mutant clone, an inference explicitly flagged by the study authors as a challenge for curative gene therapy design (PMID 36322931).

### Molecular pathways, cellular processes, and profiling
- **Pathway:** RUNX1:CBFβ core-binding-factor transcriptional network governing megakaryopoiesis and myeloid/lymphoid differentiation (KEGG/Reactome: "Transcriptional regulation by RUNX1," [Reactome R-HSA-8878171](https://reactome.org/content/detail/R-HSA-8878171)).
- **Cellular processes:** megakaryocyte differentiation and polyploidization (defective); platelet granule biogenesis and secretion (defective); HSC self-renewal/clonal fitness (dysregulated, pro-clonal).
- **Suggested GO terms:** GO:0030220 (platelet formation), GO:0007596 (blood coagulation), GO:0045055 (regulated exocytosis — granule secretion), GO:0030220-adjacent GO:0061564-type differentiation terms, GO:0004725-unrelated (not applicable here — RUNX1 is a transcription factor, not a phosphatase); more precisely GO:0043433 (negative regulation of DNA-binding transcription factor activity, for dominant-negative variant mechanism), GO:0030099 (myeloid cell differentiation).
- **Suggested CL terms:** CL:0000556 (megakaryocyte), CL:0000767 (basophil — not primary), CL:0000037 (hematopoietic stem cell), CL:0000234 (phagocyte — not primary); most central: CL:0000556 megakaryocyte and CL:0000037 HSC.
- **Molecular profiling:** No large-scale disease-dedicated transcriptomic/proteomic/metabolomic public dataset was identified beyond targeted RUNX1-target-gene expression studies (PLDN, RAB27B, MYL9, etc.) and the genomic-landscape (targeted/whole-exome) sequencing cohorts cited above; single-cell and spatial transcriptomic characterization of RUNX1‑FPDMM marrow specifically is an evidence gap relative to sporadic AML/MDS single-cell atlases.
- **Functional genomics screens:** CRISPR-based functional variant classification (Simon et al. 2021) is the primary functional-genomics dataset directly informing pathogenicity/severity stratification for this disease.

---

## 7. Anatomical Structures Affected

- **Primary organ/system:** Bone marrow (hematopoietic system) — megakaryocyte lineage primarily, with secondary myeloid (and occasionally lymphoid) lineage involvement upon transformation.
- **Secondary involvement:** Skin (eczema/psoriasis in ~50% of families); systemic bleeding manifestations (mucosal surfaces — gingiva, uterus/reproductive tract — menorrhagia, peripartum hemorrhage; GI tract in severe bleeding).
- **Tissue/cell level:** Megakaryocytes (CL:0000556) — small, hypolobated, scant-cytoplasm, non-dysplastic-appearing but functionally abnormal; hematopoietic stem/progenitor cells (CL:0000037); platelets (anucleate cell fragments) with dense-granule (lysosome-related organelle) and alpha-granule defects.
- **Subcellular level:** Platelet dense granules and alpha granules (GO Cellular Component: GO:0042582 azurophil granule-adjacent; specifically GO:0031091 platelet alpha granule, and the platelet dense granule / delta granule compartment linked to **BLOC-1 complex** dysfunction via PLDN loss); nucleus (RUNX1 is a nuclear transcription factor, GO:0005634).
- **Localization/laterality:** Systemic/hematologic — not applicable to lateralization; marrow involvement is diffuse/multifocal rather than localized.
- **UBERON suggestions:** UBERON:0002371 (bone marrow), UBERON:0001977 (platelet — note: UBERON models platelet as a cell type via CL, not strictly organ), UBERON:0002097 (skin of body) for the dermatologic manifestations.

---

## 8. Temporal Development

- **Onset of platelet/bleeding phenotype:** Often present from birth/early childhood (congenital thrombocytopenia recognized incidentally or via bleeding symptoms), though it may go unrecognized for years given mild severity.
- **Onset of malignancy:** Highly variable — pediatric AML/MDS cases occur, but median age of malignancy onset is **33 years**, spanning a wide range into later adulthood; this is a lifelong, not time-limited, risk window.
- **Progression pattern:** Not a single linear staged disease — better modeled as (a) a **stable baseline phenotype** (thrombocytopenia/bleeding, present from an early age and generally non-progressive in isolation) with (b) a **superimposed, stochastic clonal-evolution risk** that can manifest at any point in life as MDS (often insidious, detected via cytopenia surveillance) which may then **progress** to overt AML. Some patients transform directly to AML without a preceding clinically apparent MDS phase.
- **Remission/course:** MDS/AML in this context is generally **not self-limited** and, per GeneReviews, "not thought to be curable with chemotherapy alone" because the germline lesion persists in the entire stem cell compartment — allogeneic HSCT is required for cure.
- **Critical periods/intervention windows:** The literature explicitly frames the open clinical question as **when (if ever) to intervene preemptively** with HSCT versus continued surveillance — a 2025 paper proposes a formal "shared decision-making framework" for exactly this question, underscoring that no consensus critical intervention window yet exists ([PMID 41924923, preemptive HSCT decision framework](https://pubmed.ncbi.nlm.nih.gov/41924923/)).

---

## 9. Inheritance and Population

- **Inheritance pattern:** Autosomal dominant. Most probands inherit the variant from an affected (sometimes subclinically affected/unrecognized) parent; de novo occurrence is reported but its proportion is not firmly established in the literature.
- **Penetrance:** **Incomplete and variable.** GeneReviews states penetrance is formally "unknown"; commonly cited figures are a **35–50% lifetime risk of hematologic malignancy** (frequently summarized as ~44% by age 50), while **"a minority of individuals have no clinical or laboratory features"** despite carrying a pathogenic variant — i.e., even the bleeding/platelet phenotype is not fully penetrant. RUNX1 is explicitly grouped with ANKRD26, DDX41, and ETV6 as a **"variable malignant penetrance"** germline predisposition syndrome, distinct from high-penetrance syndromes ([Seminars in Hematology 2024 review](https://www.sciencedirect.com/science/article/abs/pii/S1521692624000021)).
- **Expressivity:** Highly variable, both between and within families — spectrum from asymptomatic carriage to severe transfusion-dependent bleeding and/or early leukemic transformation.
- **Anticipation, mosaicism, founder effects:** No genetic anticipation phenomenon (not a repeat-expansion disorder). **Germline mosaicism** and **somatic (hematopoietic-tissue-restricted) loss of heterozygosity via uniparental disomy 21** are both specifically discussed as causes of apparent non-transmission or false-negative parental testing — this is a distinctive, clinically important feature of RUNX1-FPDMM genetic counseling (mandates non-hematopoietic tissue, e.g., cultured fibroblasts, for definitive parental/germline testing). No specific founder variant/population is described; the ~200 reported families span diverse ancestries without a dominant founder mutation.
- **Consanguinity:** Not a relevant risk factor for this autosomal *dominant* disorder.
- **Epidemiology:** Rare disease — approximately **200 families** described worldwide in the literature to date, likely an underestimate due to underdiagnosis (mild bleeding phenotypes are easily missed, and molecular testing requires awareness of the false-negative blood-DNA pitfall). No formal population-based prevalence/incidence rate (cases per 100,000) has been established; Orphanet does not list a numeric prevalence class for ORPHA:71290 in the material reviewed. A **2023 U.S./international natural history study enrolled 214 participants including 111 patients with 39 different RUNX1 variants from 45 unrelated families** — the largest prospective cohort to date (Blood 2023, PMID 37738626).
- **Sex ratio / geographic distribution:** No sex predilection or endemic geographic clustering has been reported; cases are described across North America, Europe, and Asia (e.g., a French pediatric cohort, [PMC9928638](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9928638/), and a French inherited-platelet-disorder network study of nine families, [PMC4845427](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4845427/)).

---

## 10. Diagnostics

**Laboratory/clinical tests:**
- CBC with differential (thrombocytopenia, often mild); peripheral smear (normal platelet size, distinguishing from macrothrombocytopenia syndromes like MYH9-related disease).
- Platelet aggregometry: decreased response to arachidonic acid, collagen; decreased ADP/epinephrine-induced secretion.
- Platelet electron microscopy: dense-granule/alpha-granule storage pool deficiency (in ~50%).
- Bone marrow aspirate/biopsy: performed when constitutional symptoms or evolving cytopenias arise, looking for the atypical (non-dysplastic) small hypolobated megakaryocyte pattern versus frank MDS dysplasia.

**Genetic testing (definitive diagnosis):**
- **Gene-targeted sequence analysis** of *RUNX1*: detects ~80% of pathogenic variants (missense/nonsense/splice/small indel).
- **Gene-targeted deletion/duplication (dosage) analysis**: detects the remaining ~20% (exon-level or whole-gene deletions/duplications).
- **Multigene inherited-platelet-disorder/bone-marrow-failure panels** (including *RUNX1, ANKRD26, ETV6, CEBPA, DDX41, GATA2, TP53*) are recommended as an efficient first-line strategy given phenotypic overlap; comprehensive **exome/genome sequencing** is reserved for atypical presentations.
- **Critical pitfall:** test **cultured skin fibroblasts** (preferred) or buccal cells (acceptable, risk of blood contamination) rather than peripheral blood/marrow DNA for germline confirmation, because **somatically acquired uniparental disomy of chromosome 21** in hematopoietic tissue can mask (false-negative) or, conversely, an incidental somatic RUNX1 variant found during active leukemia workup (~10% of unrelated hematologic malignancies) can be misinterpreted as germline without orthogonal tissue confirmation ([GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK568319/)).
- Variant allele fraction <40% in tumor/marrow tissue is a practical (non-definitive) flag suggesting somatic rather than germline origin, pending confirmatory fibroblast testing.

**Differential diagnosis (per GeneReviews):** ANKRD26-related thrombocytopenia, CEBPA-associated familial AML, DDX41-associated familial MDS/AML, ETV6-related thrombocytopenia, GATA2 deficiency, Li-Fraumeni syndrome (*TP53*); acquired mimics include immune thrombocytopenia and drug-induced thrombocytopenia (NSAIDs, antiplatelet agents, statins). A direct 2023 Blood comparative study specifically distinguishes **RUNX1, ETV6, and ANKRD26** hereditary platelet disorders, noting that although they "may initially present as similarly mild-moderate thrombocytopenia, each ... [has] distinct penetrance of HM and a different range of somatic alterations associated with malignancy development" ([PMID 36626254](https://pubmed.ncbi.nlm.nih.gov/36626254/)).

**Screening/surveillance for known carriers** (no formal published consensus guideline exists on frequency, per literature review, though GeneReviews offers expert-consensus recommendations):
- Clinical exam for constitutional symptoms (fatigue, fever, weight loss, dyspnea) every 6–12 months.
- CBC with differential every 3–4 months.
- Bone marrow examination triggered by new symptoms or CBC abnormalities (not routinely scheduled in the absence of a trigger).
- Skin exam as needed.
- A 2025 publication formally proposes a **shared decision-making framework** to fill the gap in consensus surveillance/timing guidance, explicitly noting "guidelines on the type of testing or frequency of surveillance have not been published" ([PMID 41924923](https://pubmed.ncbi.nlm.nih.gov/41924923/)).

**Prenatal/preimplantation testing:** Feasible once a familial variant is identified; uptake and professional guidance vary by family/center.

---

## 11. Outcome/Prognosis

- **Malignancy risk:** 35–50% lifetime risk (often summarized ~44%), median onset age 33 years; AML and MDS are the dominant malignancy types (AML ~26.9%, MDS ~13.4% as initial presentation in cohort data).
- **Curability:** MDS/AML arising in this context is generally **not curable by chemotherapy alone**; **allogeneic HSCT is the only curative approach**, consistent with the mechanistic persistence of the germline lesion in every hematopoietic stem cell.
- **Transplant outcomes:** Case reports and small series describe successful allogeneic HSCT for RUNX1‑FPDMM-associated MDS/AML, including a detailed case report/literature review ([PMC9800216](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9800216/)); a dedicated 2025 HemaSphere study specifically examined **AML outcomes in germline RUNX1 deficiency**, characterizing disease features and transplant/treatment outcomes in this population (Ernst et al. 2025, [DOI 10.1002/hem3.70057](https://onlinelibrary.wiley.com/doi/full/10.1002/hem3.70057)) — a key resource for prognostic detail beyond what could be fully retrieved here (site access was restricted during this research pass; recommend direct follow-up retrieval for exact survival statistics).
- **Related-donor transplant caveat:** because RUNX1-FPDMM is autosomal dominant with variable expressivity, **potential related HSCT donors must be genetically tested and excluded as variant carriers** before use as a stem cell source — a critical, disease-specific transplant-planning consideration flagged throughout the clinical literature.
- **Morbidity outside of malignancy:** primarily bleeding-related (transfusion dependence in a minority, procedural bleeding risk requiring premedication), and dermatologic (eczema/psoriasis, generally mild).
- **Quality of life / disability data:** No RUNX1-FPDMM-specific EQ-5D/SF-36/PROMIS dataset was identified; this is a notable evidence gap.
- **Prognostic factors under active study:** variant functional class (dominant-negative vs. haploinsufficient), clonal hematopoiesis mutation burden (TET2/DNMT3A) and its trajectory on serial sequencing, and specific cooperating driver mutations (ASXL1, CBL, FLT3, PHF6, SRSF2, WT1) at time of transformation.

---

## 12. Treatment

**Pharmacotherapy for bleeding manifestations:**
- Desmopressin (DDAVP) — NCIT term for pharmacotherapy: NCIT:C15986 (Pharmacotherapy); specific agent term for desmopressin should be bound via CHEBI/NCIT lookup.
- Antifibrinolytics: epsilon-aminocaproic acid, tranexamic acid — for surgical/dental/menstrual bleeding management.
- Platelet transfusion (NCIT: transfusion-related procedure term) reserved for severe bleeding episodes or high-risk procedures.

**Topical therapy for skin manifestations:** emollients and topical corticosteroids for eczema/psoriasis (NCIT:C15986-adjacent topical pharmacotherapy terms).

**Definitive/curative therapy for malignancy:**
- **Allogeneic hematopoietic stem cell transplantation** (NCIT:C15431, Hematopoietic Cell Transplantation) — the only curative approach for MDS/AML in this syndrome; timing (preemptive vs. at overt malignancy) remains actively debated and is the subject of a 2025 shared decision-making framework publication.
- Standard AML/MDS induction chemotherapy and hypomethylating agents (e.g., azacitidine) plus venetoclax are used as in sporadic disease for bridging/cytoreduction, though **not curative as monotherapy** in this germline-predisposed context. Notably, *RUNX1*-mutated AML/MDS (germline or somatic) shows meaningful response rates to venetoclax-based regimens in broader AML/MDS cohorts (e.g., RUNX1-mutated subgroup ORR 54% in one venetoclax/azacitidine study), though these studies were not RUNX1-FPDMM-specific.
- A dedicated early-phase trial specifically targets **RUNX1-mutant relapsed/refractory AML/MDS** with **omacetaxine and venetoclax** (NCT04874194) — while enrollment criteria include somatic RUNX1-mutant disease broadly rather than being exclusive to germline FPDMM, it is directly relevant to this molecular subgroup ([ClinicalTrials.gov protocol](https://cdn.clinicaltrials.gov/large-docs/94/NCT04874194/Prot_SAP_001.pdf); [PMC12447878](https://pmc.ncbi.nlm.nih.gov/articles/PMC12447878/)).

**Experimental/gene-therapy landscape:**
- Autologous gene-correction approaches are under early preclinical investigation, but the **rhesus macaque RUNX1-FPDMM model (PMID 36322931)** demonstrated that corrected/control-edited HSPCs **did not outcompete** RUNX1-heterozygous mutant HSPCs long-term — a specific, mechanistically grounded caution that curative gene therapy for this disorder faces a nontrivial clonal-competition barrier not present in simpler monogenic HSC disorders.
- A 2025 review, "Targeting RUNX1 Germline Variants: Agents Under Investigation" (*Current Hematologic Malignancy Reports*), catalogs emerging pharmacologic strategies aimed at clonal hematopoiesis interception in this population ([Springer](https://link.springer.com/article/10.1007/s11899-025-00767-w)).

**Supportive care:** genetic counseling (NCIT:C15240), medical alert documentation to prevent misattributed-bleeding (child abuse) concerns, avoidance counseling for antiplatelet/NSAID medications and contact sports.

**Treatment algorithm summary:** (1) manage bleeding symptomatically/prophylactically; (2) structured surveillance (CBC q3–4 months, exam q6–12 months, marrow exam if triggered); (3) upon MDS/AML diagnosis, pursue allogeneic HSCT (related donors must be RUNX1-variant-tested and excluded) as the only curative modality, with cytoreductive chemotherapy/hypomethylating-agent bridging as needed; (4) no validated pharmacologic clonal-hematopoiesis-interception therapy yet exists outside clinical trials.

---

## 13. Prevention

- **Primary prevention:** Not applicable in the classic sense (germline variant cannot be prevented once inherited); avoidance of genotoxic exposures (radiation, smoking, occupational chemical exposure) and platelet-function-impairing medications (NSAIDs, antiplatelet agents, statins) is recommended as a precautionary risk-reduction measure for both bleeding and, speculatively, malignancy risk.
- **Secondary prevention (early detection):** Structured hematologic surveillance in known carriers (as above) to catch MDS/pre-AML changes at the earliest, most treatable stage; this is the closest analog to a "screening program" for this disorder, though it is expert-consensus rather than a formally validated USPSTF/CDC-style program.
- **Genetic screening:** Cascade testing of at-risk relatives once a familial variant is identified is explicitly recommended (using non-hematopoietic tissue for definitive results) to identify asymptomatic carriers who need surveillance; prenatal and preimplantation genetic testing are technically available once the familial variant is known, with uptake being a family-preference-driven decision.
- **Genetic counseling:** Central to management — communicating the 50% transmission risk to offspring, the variable/incomplete penetrance (a minority of carriers are entirely asymptomatic), the germline-mosaicism/loss-of-heterozygosity testing pitfalls, and reproductive options.
- **Tertiary prevention:** Once malignancy develops, allogeneic HSCT is pursued specifically to prevent relapse/progression, given the ineffectiveness of chemotherapy alone at achieving durable remission in this predisposed stem cell compartment.
- **Immunization/prophylaxis/public health measures:** Not applicable — this is not an infectious or environmentally-driven condition amenable to vaccination or public-health-level intervention.

---

## 14. Other Species / Natural Disease

- **Taxonomy of model use:** *Macaca mulatta* (rhesus macaque, NCBITaxon:9544), *Danio rerio* (zebrafish, NCBITaxon:7955), *Mus musculus* (mouse, NCBITaxon:10090) are the principal non-human systems used — this is a research-model landscape rather than a naturally occurring veterinary disease.
- **Naturally occurring veterinary disease:** No OMIA entry or naturally occurring companion-animal/livestock phenocopy of RUNX1-FPDMM specific to a germline RUNX1 variant was identified in this search; this is an evidence gap (worth a targeted OMIA search if precise veterinary comparanda are needed) rather than a confirmed absence.
- **Orthologous gene:** *Runx1* is highly conserved across vertebrates (mouse, zebrafish orthologs confirmed functionally essential for definitive hematopoiesis; NCBI Gene mouse Runx1 and zebrafish runx1 entries exist), underlying the strong translational relevance of the animal models below despite no known spontaneous animal phenocopy.
- **Comparative pathology:** Complete constitutional *Runx1* knockout is embryonic lethal in mouse (loss of all definitive hematopoiesis, death ~E12.5–13); this establishes RUNX1 as absolutely essential for HSC emergence from hemogenic endothelium, and by extension explains why FPDMM arises from **partial (heterozygous)** rather than complete loss of function — complete biallelic loss is not compatible with a viable postnatal disease state, reinforcing the haploinsufficiency/dominant-negative disease model in humans.
- **Zoonotic potential:** None; not applicable.

---

## 15. Model Organisms

- **Mouse models:** Multiple germline loss-of-function *Runx1*-FPD mouse models exist. One key model demonstrated **"hematopoietic cell autonomous disruption of hematopoiesis in a germline loss-of-function mouse model of RUNX1-FPD"** ([PMID 36741355](https://pubmed.ncbi.nlm.nih.gov/36741355/)). Compound-mutant mice (RUNX1-FPD background plus a cooperating secondary mutation) developed MDS/AML with **~30% penetrance**, directly modeling the two-hit progression described in the human mechanism section (2023 ASH/EHA presentation, [ScienceDirect abstract](https://www.sciencedirect.com/science/article/pii/S301472X23013899)). These models are explicitly being used and shared with the field to test candidate drugs for delaying/preventing/reversing clonal HSC expansion.
  - Complete *Runx1* knockout mice are embryonic lethal (E13), confirming RUNX1's essential, non-redundant role in definitive HSC emergence — relevant context for why FPDMM models use partial/heterozygous or hematopoietic-cell-conditional alleles rather than full knockouts.
- **Zebrafish models:** Zebrafish *runx1* knockout embryos are transiently "bloodless" during embryonic definitive hematopoiesis but, unexpectedly, **recover and develop multi-lineage hematopoiesis as adults**, revealing a RUNX1-independent, developmental-stage-specific compensatory hematopoietic program not present in mammals — an important **species-translation caveat** (a candidate `HUMAN_MODEL_MISMATCH`-type consideration for curation: complete loss is tolerated long-term in zebrafish but embryonic-lethal in mouse and pathogenic-but-viable as heterozygous loss in humans) ([Blood, "Development of RUNX1-Independent Hematopoiesis in Three Zebrafish runx1-KO Models"](https://www.sciencedirect.com/science/article/pii/S0006497119829385)). CBFβ and RUNX1 were also shown to be required at **two distinct steps** of zebrafish HSC development, refining the developmental-timing model of RUNX1 dependency ([Blood 2014, PMID-linked study](https://ashpublications.org/blood/article/124/1/70/33159/CBF-and-RUNX1-are-required-at-2-different-steps)).
- **Non-human primate model (highest translational fidelity):** The **rhesus macaque RUNX1-FPDMM competitive-repopulation model** (CRISPR/Cas9 NHEJ editing of autologous HSPCs, transplanted as a mixed RUNX1-edited/AAVS1-control-edited population) is the most human-relevant model to date. It **recapitulates** megakaryocytic dysplasia and the polyploidization defect seen in human marrow, and **demonstrates in vivo clonal expansion of RUNX1-mutant HSPCs relative to controls** — directly supporting the pre-leukemic clonal-priming mechanism proposed for human disease, and yielding the specific translational caution about gene-therapy feasibility described above (Blood 2023, PMID 36322931, DOI 10.1182/blood.2022018193).
- **Model limitations:** No model fully recapitulates the human bleeding-diathesis/dense-granule-deficiency phenotype with clinical-grade fidelity alongside the full malignancy-progression timeline in a single system; the mouse compound-mutant models best capture leukemic progression kinetics (30% penetrance), while the macaque model best captures the megakaryocyte/HSC-fitness phenotype, and zebrafish models are primarily informative for developmental RUNX1 dependency rather than adult disease modeling.
- **Resources:** Models described in the cited primary literature are stated to be shared with investigators (mouse model, per RUNX1 Research Program communications); no dedicated public repository (JAX/IMSR/ZFIN stock number) was confirmed in this search pass and should be verified directly with the originating labs (RUNX1 Research Program, [runx1-fpd.org](https://www.runx1-fpd.org/runx1-radar)) before citing a specific stock/strain identifier.

---

## Summary of Notable Evidence Gaps (flagged rather than smoothed over)

1. **No consensus surveillance or preemptive-HSCT timing guideline** exists in the literature to date; a 2025 shared decision-making framework is the closest current answer (PMID 41924923).
2. **No formal population-based prevalence/incidence rate** (cases per 100,000) is established — only "≈200 families reported."
3. **No disease-specific QoL instrument data** (EQ-5D/SF-36/PROMIS) were located.
4. **De novo variant proportion** is not precisely quantified in current GeneReviews text.
5. **No confirmed naturally occurring veterinary/OMIA phenocopy** was found — absence is reported as unconfirmed rather than definitively ruled out.
6. The **HemaSphere 2025 AML-outcomes paper** (Ernst et al.) could not be fully retrieved (403 error) in this session; its precise survival/outcome statistics should be verified by direct PMID/DOI lookup (DOI: 10.1002/hem3.70057) before being cited with specific numbers in a curated entry.

---

### Full Source List

- [GeneReviews: RUNX1 Familial Platelet Disorder with Associated Myeloid Malignancies](https://www.ncbi.nlm.nih.gov/books/NBK568319/) (updated Jan 2024/2025)
- [OMIM #601399 FPDMM](https://omim.org/entry/601399); [OMIM *151385 RUNX1](https://www.omim.org/entry/151385)
- [Orphanet ORPHA:71290](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=71290&Lng=GB)
- [NCI PDQ: RUNX1-Familial Platelet Disorder](https://www.ncbi.nlm.nih.gov/books/NBK598339/)
- [NORD: FPDMM](https://rarediseases.org/rare-diseases/familial-platelet-disorder-with-associated-myeloid-malignancy/)
- Ernst et al. 2025, HemaSphere, "Disease characteristics and outcomes of AML in germline RUNX1 deficiency" — [DOI 10.1002/hem3.70057](https://onlinelibrary.wiley.com/doi/full/10.1002/hem3.70057)
- Natural history study, *Blood* 2023 — PMID 37738626, DOI 10.1182/blood.2023019746 — [link](https://ashpublications.org/blood/article/142/25/2146/498043/Natural-history-study-of-patients-with-familial)
- Rhesus macaque model, *Blood* 2023 — PMID 36322931, DOI 10.1182/blood.2022018193 — [link](https://ashpublications.org/blood/article/141/3/231/486973/A-RUNX1-FPDMM-rhesus-macaque-model-reproduces-the)
- Simon et al., functional classification of RUNX1 variants, *Leukemia* 2021 — [link](https://www.nature.com/articles/s41375-021-01200-w)
- "Beyond Pathogenic RUNX1 Germline Variants" — [PMC9320507](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9320507/)
- Genomic landscape, *Blood Advances* 2024 — [link](https://ashpublications.org/bloodadvances/article/8/2/497/498801/Genomic-landscape-of-patients-with-germline-RUNX1)
- Hereditary platelet disorders (RUNX1/ETV6/ANKRD26), *Blood* 2023 — PMID 36626254 — [link](https://ashpublications.org/blood/article/141/13/1533/494072/Hereditary-platelet-disorders-associated-with-germ)
- Glembotsky et al., platelet function mechanism, *J Thromb Haemost* 2014 — PMID 24606315
- PLDN/pallidin mechanism, ASH abstract — [link](https://ashpublications.org/blood/article/122/21/567/94164/RUNX1-Regulates-PLDN-Pallidin-Expression-In)
- Bone marrow histopathology, *Haematologica* — [link](https://haematologica.org/article/view/8214)
- Preemptive HSCT shared decision-making framework — PMID 41924923
- Zebrafish *runx1*-KO models, *Blood* — [link](https://www.sciencedirect.com/science/article/pii/S0006497119829385)
- CBFβ/RUNX1 zebrafish HSC steps, *Blood* 2014 — [link](https://ashpublications.org/blood/article/124/1/70/33159/CBF-and-RUNX1-are-required-at-2-different-steps)
- Hematopoietic-cell-autonomous mouse model — PMID 36741355
- Germline predisposition to myeloid neoplasms review, *Seminars in Hematology* 2024 — [link](https://www.sciencedirect.com/science/article/abs/pii/S1521692624000021)
- Omacetaxine + venetoclax RUNX1-mutant AML/MDS trial (NCT04874194) — [protocol](https://cdn.clinicaltrials.gov/large-docs/94/NCT04874194/Prot_SAP_001.pdf); [PMC12447878](https://pmc.ncbi.nlm.nih.gov/articles/PMC12447878/)
- "Targeting RUNX1 Germline Variants: Agents Under Investigation," *Curr Hematol Malig Rep* 2025 — [link](https://link.springer.com/article/10.1007/s11899-025-00767-w)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 17 |
| Resolved | 17 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 6 |
| Quoted claims found in source | 4 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 17 |
| On topic | 15 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:41924923` *(abstract only)*: "guidelines on the type of testing or frequency of surveillance have not been published"
  - closest text in source: "We introduce a shared decision-making framework designed to support individuals with RUNX1-FPD, their families, and their multidisciplinary clinical teams in evaluating whether and when to pursue preemptive HSCT versus continued surveillance"
- `DOI:10.1002/hem3.70057` *(abstract only)*: "Disease characteristics and outcomes of AML in germline RUNX1 deficiency"
  - closest text in source: "AbstractFamilial Platelet Disorder with associated Myeloid Malignancy (FPDMM, FPD/AML, RUNX1‐FPD), caused by monoallelic deleterious germline RUNX1 variants, is characterized by bleeding diathesis and predisposition for hematologic malignancies, particularly myelodysplastic syndrome (MDS) and acute myeloid leukemia (AML)"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 2 |
| Terms whose name was checked | 21 |
| Terms named correctly | 11 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 7 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `HP:0002488` (1 mention) - the report calls it "Acute myeloid leukemia would map via MONDO/HP disease terms rather than phenotype terms — flag for curation"; HP calls it **Acute leukemia**
- `HP:0005506` (1 mention) - the report calls it "Leukemia, general"; HP calls it **Chronic myelogenous leukemia**
- `UBERON:0001977` (1 mention) - the report calls it "platelet — note: UBERON models platelet as a cell type via CL, not strictly organ"; UBERON calls it **blood serum**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0043433` (obsolete negative regulation of DNA-binding transcription factor activity) (1 mention)

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0011024` (1 mention) - the report calls it "Abnormality of the digestive system — for GI bleeding as needed"; HP calls it **Abnormality of the gastrointestinal tract**
- `HP:0004808` (2 mentions) - the report calls it "Myelodysplasia"; HP calls it **Acute myeloid leukemia**, and lists "Acute myeloid leukaemia" among its other names
- `GO:0045055` (1 mention) - the report calls it "regulated exocytosis — granule secretion"; GO calls it **regulated exocytosis**
- `GO:0043433` (1 mention) - the report calls it "negative regulation of DNA-binding transcription factor activity, for dominant-negative variant mechanism"; GO calls it **obsolete negative regulation of DNA-binding transcription factor activity**, and lists "negative regulation of DNA binding transcription factor activity" among its other names
- `CL:0000556` (3 mentions) - the report calls it "megakaryocyte", "Tissue/cell level:** Megakaryocytes"; CL calls it **megakaryocyte**
- `CL:0000767` (1 mention) - the report calls it "basophil — not primary"; CL calls it **basophil**
- `CL:0000234` (1 mention) - the report calls it "phagocyte — not primary"; CL calls it **phagocyte**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `CL:0000556` - called "megakaryocyte", "Tissue/cell level:** Megakaryocytes"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.