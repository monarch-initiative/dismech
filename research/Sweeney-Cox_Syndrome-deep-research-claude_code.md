---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-28T22:26:44.818466'
end_time: '2026-08-28T22:38:48.925362'
duration_seconds: 724.11
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Sweeney-Cox Syndrome
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
  - claude-opus-5[1m]
  web_search_requests: 16
  num_turns: 51
  total_cost_usd: 4.401402
  session_id: 76a029d3-918c-4cd0-8e09-a86606a1d238
  stop_reason: end_turn
  permission_denials: 2
  denied_tools:
  - Bash
  assistant_text_blocks: 1
fell_back: true
requested_provider: falcon
provider_attempts:
- provider: falcon
  succeeded: false
  error_type: ProviderNotConfiguredError
  remedy: the provider is not configured
  retryable: false
- provider: claude_code
  succeeded: true
citation_count: 25
reference_validation:
  total_references: 21
  verified: 21
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 1
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:40020686
  relevance_assessed: 21
  on_topic: 12
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 94
  verified: 88
  not_found: 0
  obsolete: 0
  unverifiable: 6
  confabulation_rate: 0.0
  labels_checked: 73
  labels_matching: 64
  labels_mismatched: 3
  mislabelled_terms:
  - term_id: DOID:0080538
    reported_labels:
    - Disease Ontology
    ontology_label: Sweeney-Cox syndrome
  - term_id: NCIT:C15329
    reported_labels:
    - Nasal airway
    - Craniosynostosis (E117D patient)
    - Orbital bone deficiency, hypertelorism
    - Cleft palate, velopharyngeal insufficiency
    - Imperforate anus
    - Bilateral cryptorchidism
    - Microtia
    - Feeding failure
    ontology_label: Surgical Procedure
  - term_id: NCIT:C16186
    reported_labels:
    - Bilateral talipes equinovarus
    ontology_label: Orthopedic Surgical Procedure
  labels_variant: 6
  unresolvable_prefixes:
  - ORPHA
  - OMIM
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Sweeney-Cox Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Sweeney-Cox Syndrome** covering all of the
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

# Sweeney–Cox Syndrome (SWCOS) — Comprehensive Research Report

**Prepared:** 2026-08-28 · **Target:** `MONDO:0060592` · **Category:** Mendelian, autosomal dominant, craniofacial dysostosis/frontonasal dysplasia spectrum

---

## Evidence-quality preamble (read first)

Sweeney–Cox syndrome is an **ultra-rare, recently delineated entity with a total published cohort of three individuals**. This dominates every section below. Two important consequences for knowledge-base curation:

1. **Nearly every phenotype frequency is 1/2 or 2/2**, derived from the two index patients in Kim et al. 2017. These are not population frequencies and must not be curated as if they were.
2. **ClinGen's Craniofacial Malformations GCEP classified the TWIST1–Sweeney-Cox syndrome gene–disease relationship as `Limited`** (3–4 points) in its 2026 round-one curation — the weakest of its three TWIST1 assertions. This is the single most important recent development for this entry and is stated verbatim below.

Throughout, I distinguish:
- **[CACHED]** — quote verified against a file already in `references_cache/` (usable as a dismech evidence `snippet:` as-is).
- **[WEB]** — retrieved from a database or full text online during this session; the claim is sound but the exact string has **not** been verified against a fetched reference cache file and must be re-fetched with `just fetch-reference` before being quoted.
- **[UNVERIFIED]** — flagged inference or a detail I could not independently confirm.

---

## 1. Disease Information

### Overview

Sweeney–Cox syndrome (SWCOS) is an autosomal dominant congenital craniofacial dysostosis caused by *de novo* heterozygous missense substitution of a single highly conserved glutamic acid residue — **Glu117** — in the basic DNA-binding domain of **TWIST1**. It sits at the frontonasal-dysplasia end of the TWIST1 phenotypic spectrum: patients have severe hypertelorism, deficient formation of the bony orbits and eyelids (upper eyelid colobomas, pseudoproptosis), nasal and midfacial hypoplasia, dysplastic ears, and a variable set of extracranial malformations. It is mechanistically and clinically distinct from **Saethre–Chotzen syndrome (SCS)**, the classical TWIST1 *haploinsufficiency* disorder characterized by coronal craniosynostosis.

The disease was named for the two clinicians who contributed the index patients — **E. Sweeney** and **H. Cox**, both co-authors on the delineating paper.

**Delineating publication:**

> "Here, we describe a new clinical entity, Sweeney-Cox syndrome, associated with distinct de novo amino acid substitutions (p.Glu117Val and p.Glu117Gly) at a highly conserved glutamic acid residue located in the basic DNA binding domain of TWIST1, in two subjects with frontonasal dysplasia and additional malformations."
> — Kim S, Twigg SRF, Scanlon VA, et al. *Hum Mol Genet* 2017;26(11):2118–2132. **PMID:28369379**, DOI 10.1093/hmg/ddx107 **[CACHED]**

### Key identifiers

| Resource | Identifier |
|---|---|
| MONDO | `MONDO:0060592` (label: "Sweeney-Cox syndrome"; related synonym "SWCOS") **[WEB — OLS4]** |
| OMIM | **#617746** SWEENEY-COX SYNDROME; SWCOS |
| Gene (OMIM) | ***601622** TWIST1 |
| Disease Ontology | `DOID:0080538` |
| UMLS / MedGen | `C4540299` |
| Orphanet | **No dedicated ORPHA code identified.** Repeated searches of Orphanet and the ORDO branch of OLS returned no Sweeney-Cox term. Orphanet lists TWIST1 under Saethre–Chotzen syndrome (ORPHA:794) and related craniosynostoses. Treat "no ORPHA code" as the working assumption but re-verify against a current Orphadata refresh before asserting it in the KB. |
| ICD-10 | No specific code. Closest: **Q75.8** (other specified congenital malformations of skull and face bones) or **Q87.0** (congenital malformation syndromes predominantly affecting facial appearance). |
| ICD-11 | No specific code. Closest: **LB70** (structural developmental anomalies of the face) / **LD24.5** region. |
| MeSH | No specific descriptor. Indexed under *Abnormalities, Multiple*; *Acrocephalosyndactylia*; *Eye Abnormalities*; *Macrostomia* per the PubMed record for PMID:28369379 **[CACHED — see keywords block]** |
| ZFIN human disease term | `ZDB-TERM-190716-1` (no zebrafish models registered) **[WEB]** |
| GTR condition | `C4540299` — 7 clinical tests listed, all TWIST1-based **[WEB]** |

### Synonyms and alternative names

- **SWCOS** (OMIM abbreviation)
- *TWIST1-related Sweeney-Cox syndrome* (ClinGen dyadic naming convention, used in Genet Med 2026)
- Descriptively referenced in the literature as "TWIST1 basic-domain (Glu117) frontonasal dysplasia" — not a formal synonym.
- **Do not** use "frontonasal dysplasia type 4" or similar — FND1/2/3 are the ALX3/ALX4/ALX1 entities and are distinct.

### Source of information

**Entirely aggregated disease-level and case-report literature.** There is no EHR-derived cohort, no registry, no natural-history study, and no patient organization. All human phenotype data trace to three published individuals. HPO annotations for `OMIM:617746` cite **PMID:28369379 exclusively** for every term **[WEB — HPO/ontology.jax.org API]**.

---

## 2. Etiology

### Primary causal factor

A **single heterozygous *de novo* missense substitution at TWIST1 codon 117** (NM_000474.4), replacing a glutamic acid that makes base-specific contacts with the E-box DNA motif. No environmental, infectious, or multifactorial contribution is described or plausible.

**Reported causal alleles (all three published patients):**

| cDNA (NM_000474.4) | Protein | Patient | Phenotype | Source |
|---|---|---|---|---|
| c.350A>T | p.(Glu117Val) | Kim 2017, Subject 1 (male) | SWCOS, no craniosynostosis | PMID:28369379 |
| c.350A>G | p.(Glu117Gly) | Kim 2017, Subject 2 (female) | SWCOS, more severe | PMID:28369379 |
| c.351G>T | p.(Glu117Asp) | Takenouchi 2018 (male infant) | SWCOS facial phenotype **+ bicoronal craniosynostosis + ablepharon** | PMID:30450715 / ClinVar VCV002572412 |

> ⚠️ **Nomenclature discrepancy worth flagging.** The Takenouchi abstract states "**c.351C>G p.Glu117Asp**" **[CACHED]**, but ClinVar represents the same protein change as **c.351G>T** (VCV002572412) **[WEB]**. The ClinVar representation is internally consistent (GAG→GAT); the published `c.351C>G` cannot yield Asp from a Glu codon under NM_000474.4. Per repo policy, **never alter an identifier inside an evidence snippet** — quote the paper as published and record the reconciliation in `notes:`.

### Genetic risk factors

- **Causal variant class:** ultra-localized missense hotspot. Of ~100 TWIST1 mutations reported in SCS, none previously affected codon 117 **[CACHED, PMID:28369379]**.
- **Susceptibility loci / modifier genes:** none identified. Sample size (n=3) precludes any modifier analysis.
- **Family history:** all three cases *de novo*; unaffected parents.
- **Parental age effect:** not assessed (n=3).

### Environmental risk factors

**None described.** No toxin, teratogen, occupational, dietary, or infectious association has been reported or proposed. Sex distribution in the published cohort is 2 male : 1 female — not interpretable at this n.

### Protective factors

**None known.** No protective variants, modifier alleles, or environmental exposures have been described. gnomAD does not report the Glu117 substitutions (consistent with *de novo*, fully penetrant severe disease) **[UNVERIFIED — should be checked directly at gnomad.broadinstitute.org before curating as an allele-frequency claim].**

### Gene–environment interactions

**Not applicable / none reported.** This is a fully penetrant *de novo* dominant developmental disorder with no evidence of environmental modulation.

---

## 3. Phenotypes

### The authoritative annotation set

The HPO disease annotation for `OMIM:617746` contains **48 phenotype terms plus inheritance and clinical-course terms**, all sourced to PMID:28369379, all with frequencies expressed as fractions of the two index patients **[WEB — ontology.jax.org/api/network/annotation/OMIM:617746]**. Reproduced in full below, since this is directly loadable into a dismech `phenotypes:` block.

#### Head and neck — craniofacial (the diagnostic core)

| HP ID | Term | Freq |
|---|---|---|
| HP:0000316 | **Hypertelorism** | 2/2 |
| HP:0000636 | **Upper eyelid coloboma** | 2/2 |
| HP:0005487 | **Prominent metopic ridge** | 2/2 |
| HP:0000455 | **Broad nasal tip** | 2/2 |
| HP:0011800 | Midface retrusion | 1/2 |
| HP:0000430 | Underdeveloped nasal alae | 1/2 |
| HP:0002000 | Short columella | 1/2 |
| HP:0009765 | Low hanging columella | 1/2 |
| HP:0000431 | Wide nasal bridge | 1/2 |
| HP:0000453 | Choanal atresia | 1/2 |
| HP:0000322 | Short philtrum | 1/2 |
| HP:0000160 | Narrow mouth | 1/2 |
| HP:0000218 | High palate | 1/2 |
| HP:0009099 | Median cleft palate | 1/2 |
| HP:0000220 | Velopharyngeal insufficiency | 1/2 |
| HP:0000347 | Micrognathia | 1/2 |
| HP:0000248 | Brachycephaly | 1/2 |
| HP:0005469 | Flat occiput | 1/2 |
| HP:0000260 | Wide anterior fontanel | 1/2 |
| HP:0000349 | Widow's peak | 1/2 |
| HP:0000294 | Low anterior hairline | 1/2 |
| HP:0000475 | Broad neck | 1/2 |

#### Ear

| HP ID | Term | Freq |
|---|---|---|
| HP:0000378 | Cupped ear | 1/2 |
| HP:0000369 | Low-set ears | 1/2 |
| HP:0009901 | Crumpled ear | 1/2 |
| HP:0008551 | Microtia | 1/2 |
| HP:0000396 | Overfolded helix | 1/2 |
| HP:0009909 | Uplifted earlobe | 1/2 |
| HP:0000365 | **Hearing impairment** | 1/2 (conductive in Subject 1) |

#### Eye

| HP ID | Term | Freq |
|---|---|---|
| HP:0000316 | Hypertelorism | 2/2 |

Note: **pseudoproptosis** (secondary to deficient bony orbits, accentuated by midface hypoplasia) is described in OMIM's clinical synopsis and the Arizona Hereditary Ocular Diseases entry but is **not** in the HPO annotation set **[WEB]**. Consider `HP:0000520 Proptosis` with an explanatory `description` making clear it is *pseudo*proptosis of orbital-volume origin, or leave unbound with prose — the mechanistic distinction matters and no HPO term captures it cleanly.

#### Nervous system

| HP ID | Term | Freq |
|---|---|---|
| HP:0001263 | **Global developmental delay** | 2/2 |
| HP:0000750 | Delayed speech and language development | 1/2 |
| HP:0001321 | Cerebellar hypoplasia | 1/2 |

#### Limbs and skeletal

| HP ID | Term | Freq |
|---|---|---|
| HP:0100807 | Long fingers | 1/2 |
| HP:0009882 | Short distal phalanx of finger | 1/2 |
| HP:0010709 | 2-4 finger cutaneous syndactyly | 1/2 |
| HP:0005650 | 2-5 finger cutaneous syndactyly | 1/2 |
| HP:0010715 | 2-5 toe syndactyly | 1/2 |
| HP:0001776 | Bilateral talipes equinovarus | 1/2 |
| HP:0000894 | Short clavicles | 1/2 |
| HP:0000774 | Narrow chest | 1/2 |

#### Cardiovascular / haematologic

| HP ID | Term | Freq |
|---|---|---|
| HP:0001655 | Patent foramen ovale | 1/2 |
| HP:0001643 | Patent ductus arteriosus | 1/2 |
| HP:0001746 | **Asplenia** | 1/2 |

#### Digestive / genitourinary

| HP ID | Term | Freq |
|---|---|---|
| HP:0002023 | **Anal atresia** (imperforate anus) | 1/2 |
| HP:0002020 | Gastroesophageal reflux | 1/2 |
| HP:0008689 | Bilateral cryptorchidism | 1/1 (male only) |

#### Skin, hair, nails / prenatal

| HP ID | Term | Freq |
|---|---|---|
| HP:0002230 | Generalized hirsutism | 1/2 |
| HP:0001792 | Small nail | 1/2 |
| HP:0001561 | Polyhydramnios | 1/2 |

#### Course and inheritance

| HP ID | Term |
|---|---|
| HP:0003577 | **Congenital onset** (2/2) |
| HP:0000006 | Autosomal dominant inheritance |

### Phenotypes reported in the third patient (Takenouchi 2018) — NOT in the HPO annotation set

The p.Glu117Asp patient extends the phenotype and is the key to the SWCOS↔SCS boundary:

> "Herein, we document a male infant with the distinctive facial features of ablepharon, hypertelorism, cheek pads adjacent to the corners of the mouth, and bilateral coronal suture craniosynostosis who had a de novo heterozygous mutation in the basic domain of TWIST1, that is, c.351C>G p.Glu117Asp."
> — **PMID:30450715** **[CACHED]**

Additional HP suggestions for this patient (**verify all with `just validate-terms` / OAK before binding**):
- `HP:0004440` Coronal craniosynostosis **[UNVERIFIED ID]**
- `HP:0001363` Craniosynostosis (parent term, safer)
- **Ablepharon** — no confident HPO ID; `HP:0000636` Upper eyelid coloboma understates it. Consider free-text `preferred_term` with no `term:` binding rather than manufacturing a match (per the repo's "no term beats a bad one" rule).
- **Cheek pads adjacent to the corners of the mouth** — shared with Barber–Say and ablepharon–macrostomia syndromes; no clean HPO term. Free text recommended.

### Phenotype characteristics

- **Age of onset:** congenital in 3/3 (`HP:0003577`). Malformations are established during embryonic craniofacial morphogenesis (~weeks 4–8); the phenotype is fully expressed at birth.
- **Severity:** variable but uniformly severe facially. Subject 2 (p.Glu117Gly) was markedly more severe than Subject 1 (p.Glu117Val): she required **tracheostomy from birth**, had cardiac defects, asplenia, and progressed to **corneal scarring with phthisis of the right eye** despite lid coloboma repair **[WEB — PMC5438873; Arizona HOD]**.
- **Progression:** the malformation burden is **static/non-progressive** — it is a structural dysostosis, not a degenerative process. What *does* progress is **secondary/complication morbidity**: corneal exposure keratopathy → scarring → phthisis bulbi; conductive hearing loss; feeding/airway compromise; and, in the E117D patient, craniosynostosis with its attendant risk of raised intracranial pressure.
- **Frequency among affected:** see tables. **Facial features (hypertelorism, upper eyelid coloboma, prominent metopic ridge, broad nasal tip) and global developmental delay are 2/2; everything else is 1/2.**

### Quality-of-life impact

No formal QoL instrument (EQ-5D, PROMIS, SF-36) has ever been administered. Per-phenotype impacts inferred from the case descriptions **[WEB]**:

| Phenotype | Functional impact |
|---|---|
| Upper eyelid coloboma / ablepharon | Corneal exposure → keratopathy, scarring, vision loss (documented phthisis in Subject 2) |
| Velopharyngeal insufficiency / cleft palate | Speech intelligibility, feeding, need for surgery |
| Choanal atresia / airway compromise | Tracheostomy dependence (Subject 2) |
| Conductive hearing loss + microtia | Language acquisition, amplification need |
| Global developmental delay | Moderate learning disability documented in Subject 1; educational support |
| Syndactyly, talipes equinovarus, short distal phalanges | Hand function, ambulation, orthopaedic surgery |
| Facial dysmorphism | Psychosocial burden, repeated reconstructive surgery |
| Imperforate anus | Neonatal surgery, continence |

---

## 4. Genetic / Molecular Information

### Causal gene

| Field | Value |
|---|---|
| Symbol | **TWIST1** |
| Approved name | twist family bHLH transcription factor 1 |
| HGNC | **`hgnc:12428`** (lowercase prefix per repo convention) **[WEB — rest.genenames.org]** |
| Cytoband | **7p21.1** |
| Ensembl | ENSG00000122691 |
| NCBI Gene | 7291 |
| UniProt | **Q15672** (202 aa) |
| OMIM gene | *601622 |
| Reference transcript | NM_000474.4 |
| Aliases (GTR) | ACS3, BPES2, BPES3, CRS, SCS, bHLHa38 |

### Protein architecture and the Glu117 hotspot

- **bHLH domain: residues 108–159** (UniProt Q15672 FT DOMAIN) **[WEB]**.
- **Residues 1–105: disordered**; **residues 161–191: sufficient for transactivation** **[WEB]**.
- **Glu117 lies within the basic (DNA-contacting) region** at the N-terminal end of the bHLH fold. Sequence context around it (positions 111–120): `V M A N V R E R Q R` — i.e. **E117** flanked by the basic arginines R116/R118/R120. (R120G is an independently reported pathogenic SCS/craniosynostosis allele, ClinVar VCV001474221 **[WEB]** — underlining that this short stretch is a mutational hotspot for two mechanistically different diseases.)
- **Functional role of the conserved glutamate:** it makes the sequence-specific base contacts that define E-box recognition:

> "is responsible for the sequence-specific contacts of adjacent bases (CA) that constitute the symmetrical E box binding motif CANNTG"
> — Kim et al. 2017 full text **[WEB — PMC5438873]**

- **Structural resource:** **PDB `8OSB` — "TWIST1-TCF4-ALX4 complex on specific DNA"**, X-ray, 2.90 Å, residues 101–167 **[WEB — UniProt/RCSB]**. This is the directly relevant structure for modelling the Glu117 substitutions, and it captures TWIST1 in the ternary arrangement that the Coordinator-motif biology (§6) predicts.

### Variant classification and population frequency

ClinVar records at codon 117 and immediate neighbours **[WEB — NCBI E-utilities]**:

| VCV | HGVS | Protein | Classification | Review status | Condition |
|---|---|---|---|---|---|
| VCV000444875 | c.350A>T | p.Glu117Val | **Pathogenic** | no assertion criteria provided | **Sweeney-Cox syndrome** |
| VCV000444876 | c.350A>G | p.Glu117Gly | **Pathogenic** | criteria provided, single submitter | TWIST1-related craniosynostosis; Saethre-Chotzen syndrome |
| VCV002572412 | c.351G>T | p.Glu117Asp | **Pathogenic** | criteria provided, single submitter | **Sweeney-Cox syndrome** |
| VCV001418275 | c.349G>T | p.Glu117Ter | Pathogenic | criteria provided, single submitter | TWIST1-related craniosynostosis; SCS |
| VCV001474221 | c.358C>G | p.Arg120Gly | Pathogenic/Likely pathogenic | multiple submitters, no conflicts | SCS; TWIST1-related craniosynostosis |

Two curation-relevant observations:
1. **`p.Glu117Ter` (nonsense) is annotated to Saethre–Chotzen/craniosynostosis, not Sweeney-Cox** — exactly as the mechanism predicts. Truncation at 117 = loss of allele = haploinsufficiency = SCS. Missense at 117 = poisoned protein = SWCOS. The same codon produces two different diseases by two different mechanisms. This is a clean, curatable mechanistic contrast.
2. **ClinVar's condition assignment is inconsistent** — p.Glu117Gly, one of the two original SWCOS alleles, is filed under "TWIST1-related craniosynostosis; Saethre-Chotzen syndrome." Do not treat ClinVar's condition field as authoritative for SWCOS membership; use the primary literature.

- **Variant type:** all missense (single-nucleotide substitution).
- **Origin:** **germline, *de novo*** in 3/3. No somatic involvement; no mosaicism reported.
- **Allele frequency:** absent from population databases (expected for *de novo* severe dominant disease) **[UNVERIFIED — confirm in gnomAD directly].**

### Functional consequence — the central mechanistic claim

**Antimorphic (dominant-negative), not loss-of-function.** This is the defining molecular statement about the disease and it is asserted independently in two cached papers:

> "The genetic analysis favors a predominantly dominant-negative mechanism for the action of amino acid substitutions at this highly conserved glutamic acid residue"
> — **PMID:28369379** **[CACHED]**

> "Heterozygous localized TWIST1 and TWIST2 basic domain substitutions exert antimorphic effects to cause Sweeney-Cox syndrome, Barber-Say syndrome, and ablepharon-macrostomia syndrome, respectively."
> — **PMID:30450715** **[CACHED]**

For dismech schema purposes:
- On `GeneticContext`: `functional_impact_category: DOMINANT_NEGATIVE` — this is the variant-consequence slot and it is the right one here.
- Do **not** use `LOSS_OF_FUNCTION`; that is the SCS mechanism and conflating them erases the whole point of the entity.

### Modifier genes

**None identified.** Candidate modifiers on mechanistic grounds only (no human data): `TCF12` (HGNC:11623, the obligate E-protein partner, itself a coronal craniosynostosis gene), `TCF3`/E12, `HAND2`, and the homeodomain Coordinator partners `ALX1`, `ALX4`, `MSX1`, `PRRX1`. All speculative — do not curate as modifiers.

### Epigenetic information

No disease-specific DNA-methylation, histone, or chromatin dataset exists for SWCOS patients. **However**, TWIST1's own molecular action is chromatin-level: it drives chromatin opening and H3K27 acetylation at Coordinator-motif enhancers in cranial neural crest cells (§6). A Glu117 substitution is therefore expected to produce a **genome-wide enhancer-accessibility defect** in CNCCs — a testable and completely unexplored hypothesis, and a good candidate for a `KNOWLEDGE_GAP` discussion in the entry.

### Chromosomal abnormalities

Not a mechanism for SWCOS. Note for differential purposes: **7p21 deletions encompassing TWIST1** cause SCS (haploinsufficiency), and a **430 kb duplication involving TWIST1 regulatory elements** causes auriculocondylar syndrome **[WEB — PMC9411924]**. Neither produces the SWCOS phenotype, again because SWCOS requires a *poisoned protein*, not altered dosage.

---

## 5. Environmental Information

- **Environmental factors:** none. No toxicological, radiation, pollution, or occupational association reported. CTD contains no SWCOS-specific chemical–disease association.
- **Lifestyle factors:** none. No maternal smoking, alcohol, folate, or nutritional association has been reported or investigated (n=3 precludes it).
- **Infectious agents:** not applicable.

**Curation guidance:** the `environmental:` section should be left empty, or, if a curator wishes to record that the search was performed, use the sanctioned waiver form — `review_notes:` beginning exactly `Left deliberately uncited.` followed by ≥20 words describing the searches run (CTD, PubMed teratogen queries, EPA) and why nothing quotable was found.

---

## 6. Mechanism / Pathophysiology

This is the richest section of the entry and where SWCOS earns its place in a mechanism knowledge base. The causal chain is unusually well-supported for an n=3 disease because the *gene* is deeply studied even though the *disease* is not.

### 6.1 The causal chain (upstream → downstream)

```
[1] De novo heterozygous TWIST1 c.350A>T / c.350A>G / c.351G>T
        ↓  (MOLECULAR)
[2] Glu117 substitution in the bHLH basic region
        ↓  (MOLECULAR)
[3] Loss/degradation of sequence-specific E-box (CANNTG) recognition,
    with RETAINED dimerization and residual DNA binding
        ↓  (MOLECULAR)
[4] Mutant protein sequesters wild-type TWIST1 and E-proteins (TCF3/TCF12)
    into NON-PRODUCTIVE heterodimers  →  DOMINANT-NEGATIVE
        ↓  (MOLECULAR)
[5] Failure of TWIST1-dependent Coordinator-motif enhancer activation
    (chromatin opening + H3K27ac) in cranial neural crest cells
        ↓  (CELLULAR)
[6] Failure to activate the frontonasal ectomesenchyme program —
    ALX1, ALX3, ALX4 not induced in the frontonasal prominence
        ↓  (CELLULAR)
[7] Impaired CNCC EMT, migration, survival, and skeletogenic differentiation
        ↓  (TISSUE)
[8] Deficient frontonasal / periocular / orbital / nasal skeletal
    and soft-tissue morphogenesis
        ↓  (ORGANISM)
[9] Hypertelorism, deficient bony orbits with pseudoproptosis, eyelid
    colobomas, nasal hypoplasia, cleft palate/VPI, dysplastic ears
```

A parallel branch, dose-dependent, explains why one allele adds craniosynostosis:

```
[3'] Milder antimorphic effect (p.Glu117Asp)  →  net activity close to
     the haploinsufficient (SCS) range  →  coronal suture boundary
     failure  →  bicoronal craniosynostosis IN ADDITION to the
     SWCOS facial phenotype
```

> "The present observation suggests that a localized TWIST1 basic domain substitution, that is, p.Glu117Asp, in TWIST1 may exert a mild antimorphic effect similar to that of haploinsufficiency, leading to craniosynostosis and ablepharon."
> — **PMID:30450715** **[CACHED]**

### 6.2 The dosage-continuum model (the key conceptual contribution)

Kim et al. propose that TWIST1/TWIST2 basic-domain phenotypes lie on a **single continuum of residual protein activity**, and that the identity of the substituting amino acid sets the position on that continuum:

> "phenotypes of individuals who are heterozygous for TWIST1 or TWIST2 mutations fall on a continuum" — correlating with protein activity levels; SWCOS alleles produce more severe dominant-negative effects than haploinsufficient SCS mutations, potentially reducing functional protein **below the threshold required for neural crest survival** **[WEB — PMC5438873]**

This makes SWCOS a textbook **allelic-series / threshold** disorder and is worth modelling explicitly as a `mechanistic_hypotheses` group in the dismech entry.

| Gene | Residue | Substitution | Disease | Position on activity continuum |
|---|---|---|---|---|
| TWIST1 | Glu117 | Ter (nonsense) | Saethre–Chotzen | 50% (haploinsufficiency) |
| TWIST1 | Glu117 | **Asp** | SWCOS + craniosynostosis | mild antimorph ≈ haploinsufficiency |
| TWIST1 | Glu117 | **Val** | **Sweeney–Cox** | strong antimorph |
| TWIST1 | Glu117 | **Gly** | **Sweeney–Cox** (severe) | strong antimorph |
| TWIST2 | Glu75 | Ala / Gln | Barber–Say | antimorph |
| TWIST2 | Glu75 | Lys | Ablepharon–macrostomia | most severe antimorph |

The TWIST2 comparison is from Marchegiani et al., *Am J Hum Genet* 2015, **PMID:26119818**: AMS = p.Glu75Lys; BSS = p.Glu75Gln or p.Glu75Ala; "the two syndromes differed based solely upon the nature of the substituting amino acid" **[WEB]**.

### 6.3 Molecular pathways and protein dysfunction

**TWIST1 normal function (UniProt Q15672):**
> "Efficient DNA binding requires dimerization with another bHLH protein. Homodimer or heterodimer with E proteins such as TCF3." … "Regulates cranial suture patterning and fusion." **[WEB]**

**Why a basic-domain missense is worse than a null.** The mutant retains its HLH dimerization surface but has a corrupted DNA-reading head. It therefore continues to titrate the limited pool of wild-type TWIST1 and E-proteins into complexes that occupy or fail at target enhancers:

> mutant proteins likely "sequester WT protein in non-productive heterodimers comprising either HLH-2/HLH-8-Glu29† or HLH-8/HLH-8-Glu29†" **[WEB — PMC5438873]**

**The Coordinator motif — the highest-resolution account of what Glu117 actually does.** Bhatt/Kim et al., *Cell* 2024 (**PMID:38262408**) showed that a composite DNA element called the **Coordinator** — an **E-box plus a homeodomain TAAT site separated by a 6-bp spacer** — "guides cooperative and selective binding between the bHLH family mesenchymal regulator TWIST1 and a collective of HD factors" **[WEB]**. Mechanistically:

> TWIST1 binds the E-box, drives chromatin opening, promotes homeodomain recruitment of ALX1, ALX4, MSX1 or PRRX1, and promotes enhancer acetylation at the coordinator motif **[WEB]**

Because Glu117 is precisely the residue that reads the E-box half of the Coordinator, a Glu117 substitution should **collapse the entire cooperative assembly**, not merely weaken one contact. This provides a direct, structure-anchored explanation for the frontonasal specificity of SWCOS, and PDB `8OSB` (TWIST1–TCF4–ALX4 on DNA) is the corresponding structure.

**Direct downstream target — Alx1.** A 2026 paper (already in the local reference cache) closes the loop from TWIST1 to the frontonasal-dysplasia gene program:

> "ECR1, whose homologous region in the human genome harbors a lead single nucleotide variation significantly associated with facial and cranial vault shape differences, exhibits high enrichment of Twist1 transcription factor occupancy in mouse embryonic frontonasal tissues and drove Twist1-dependent reporter transgene expression specifically in the developing periocular and frontonasal mesenchyme in transgenic mice."
> — Huang Y, Iyyanar PPR, Xu J, et al. *Dev Biol* 2026. **PMID:41850652** **[CACHED]**

and, framing SWCOS explicitly:

> "Mutations in TWIST1 have been associated with Sweeney-Cox (OMIM 617746) and Saethre-Chotzen (OMIM 101400) syndromes, with Sweeney-Cox syndrome characterized by hypertelorism with severe deficiency in frontal bones and hypoplasia of the nose and facial bones while Saethre-Chotzen syndrome exhibits craniosynostosis with hypertelorism and maxillary hypoplasia"
> — **PMID:41850652** **[CACHED]**

> "mice with lineage-specific inactivation of Twist1 in migrating neural crest cells, exhibited dramatic loss of Alx1 mRNA expression in the developing frontonasal CNCCs"
> — **PMID:41850652** **[CACHED]**

**This is the mechanistic bridge that makes SWCOS a *frontonasal dysplasia*:** biallelic *ALX1* loss causes FND3 (OMIM 613456) with severe midfacial hypoplasia and extreme microphthalmia; TWIST1 sits directly upstream of *ALX1* through the ECR1 enhancer; so a dominant-negative TWIST1 phenocopies part of the ALX program. Curate this as an explicit causal edge.

**Dimer-selection / phosphorylation axis (SCS-derived, mechanistically adjacent).** Twist1–Hand2 dimer choice is modulated by PKA and PP2A phosphorylation of conserved helix-I residues, and multiple SCS-associated TWIST1 mutations alter this **[WEB — PMC2568820, Firulli et al.]**. Glu117 is in the basic region rather than the helices, so this is a *different* route to the same "dimer misallocation" endpoint — worth noting but do not conflate.

### 6.4 Cellular processes

| Process | GO suggestion | Evidence |
|---|---|---|
| Neural crest cell migration | `GO:0001755` | Twist1 cKO CNCCs show ~50% fewer migratory cells and 68% shorter migration distance **[CACHED, PMID:35781329]** |
| Epithelial-to-mesenchymal transition | `GO:0001837` | Twist1-null delaminated CNCCs retain E-cadherin and epithelial morphology **[CACHED, PMID:35781329]** |
| Neural crest cell differentiation | `GO:0014033` | Loss of skeletogenic differentiation **[CACHED, PMID:19414008]** |
| Cranial suture morphogenesis | `GO:0060363` | UniProt: "Regulates cranial suture patterning and fusion" **[WEB]** |
| Osteoblast differentiation | `GO:0001649` | TWIST1–RUNX2 antagonism via the Twist-box **[WEB]** |
| Regulation of transcription by RNA Pol II | `GO:0006357` | core TWIST1 function |
| E-box binding | `GO:0070888` | the directly disrupted molecular function — **this is the node Glu117 hits** |
| Protein dimerization activity | `GO:0046983` | retained in mutant; the basis of the dominant-negative effect |
| Neural tube closure | `GO:0001843` | Twist1-null embryos show complete NTD **[CACHED, PMID:35781329]** |

The critical modelling insight: **`GO:0070888` E-box binding is `DECREASED`/`LOSS_OF_FUNCTION` while `GO:0046983` protein dimerization activity is `UNCHANGED`.** That dissociation *is* the disease mechanism, and a well-built dismech entry should make it visible as two separate `molecular_functions` descriptors on the same or adjacent nodes.

Direct quotes available for CNCC biology:

> "Twist1 suppresses Irf6 and other epithelial genes in CNCCs during the epithelial-to-mesenchymal transition (EMT) process and cell migration. Conversely, a loss of Twist1 leads to a sustained expression of epithelial and cell adhesion markers in migratory CNCCs."
> — Bertol JW, et al. *Development* 2022. **PMID:35781329** **[CACHED]**

> "TWIST1 has been shown to promote cell survival and proliferation of migratory CNCCs during craniofacial development"
> — **PMID:35781329** **[CACHED]**

> "Loss of Twist1 in neural crest cells and their derivatives impairs skeletogenic differentiation and leads to the loss of bones of the snout, upper face and skull vault."
> — Bildsoe H, et al. *Dev Biol* 2009. **PMID:19414008** **[CACHED]**

### 6.5 Systems not involved

- **Metabolic changes:** none. Not a metabolic disease; no enzyme deficiency, no biochemical marker.
- **Immune system involvement:** none, despite TWIST1's known repression of TNF/IL1B in other contexts (UniProt) — no immunologic phenotype has been reported in any SWCOS patient. Note the 1/2 **asplenia**: this is a *structural* developmental defect (laterality/mesoderm-derived organ agenesis), and it does carry a real functional-asplenia infection risk (see §11/§13), but it is not evidence of a primary immune mechanism.
- **Tissue damage mechanisms:** SWCOS is a **dysmorphogenesis**, not a tissue-injury disease. There is no oxidative stress, ischemia, fibrosis, or necrosis component. The only genuine "tissue damage" is **secondary corneal exposure injury** from the eyelid defect (documented: corneal scarring → phthisis bulbi).
- **Biochemical abnormalities:** none. No diagnostic lab abnormality exists.

### 6.6 Molecular profiling

**No SWCOS-patient omics data exist** — no transcriptomics, proteomics, metabolomics, lipidomics, or single-cell data from any of the three patients.

Relevant *gene-level* datasets that could be re-used with clear labelling as model/normal-development data (not patient data), all GEO **[WEB, via PMID:41850652]**:

| Accession | Content |
|---|---|
| `GSE230316` | Twist1 ChIP-seq, E10.5 mouse embryonic facial tissue |
| `GSE89435` / `GSE89436` | H3K27ac ChIP-seq + ATAC-seq, E10.5 mouse frontonasal prominence |

> ⚠️ **Dataset-curation caution.** Per the repo's dataset SOP, these are *not* Sweeney-Cox datasets. A gene-driven search for TWIST1 returns craniosynostosis, EMT, and cancer datasets — classic `GENE_ONLY` / Named Entity Confusion territory. If curated at all, they must be tagged as mouse developmental resources with explicit provenance `notes`, never as disease datasets. Run `just verify-datasets` on anything added.

**Functional genomics / dosage.** A 2025 Cell Genomics study examined "how concentrations of the dosage-sensitive TFs TWIST1 and SOX9 affect regulatory element chromatin accessibility in facial progenitor cells" (**PMID:40020686**) **[WEB]** — directly relevant to the threshold model in §6.2 and the best available quantitative handle on TWIST1 dose-response.

---

## 7. Anatomical Structures Affected

### Organ level

**Primary (2/2 or 3/3 involvement):**
- Craniofacial skeleton — frontal bones, **bony orbits** (deficient, producing pseudoproptosis), nasal bones/capsule, maxilla, palate
- **Eyelids** — upper lid colobomas; ablepharon in the E117D patient
- **Nose** — hypoplastic alae, short/low columella, broad tip
- **External ear** — microtia, crumpled/cupped, low-set, overfolded helix
- **Palate / velopharynx**

**Secondary and variable (1/2):**
- CNS — cerebellar hypoplasia; global developmental delay in 2/2
- Cardiovascular — PDA, PFO
- Spleen — **asplenia**
- GI — anal atresia, GERD
- GU — bilateral cryptorchidism
- Limbs — hands (syndactyly, long fingers, short distal phalanges), feet (talipes equinovarus, 2-5 toe syndactyly)
- Thorax — narrow chest, short clavicles
- Airway — choanal atresia; tracheostomy dependence

**Body systems:** skeletal (craniofacial predominant), visual/ocular adnexal, auditory, nervous, cardiovascular, digestive, genitourinary, lymphoid/splenic, respiratory (upper airway).

### Tissue and cell level

**The single defining cell type is the cranial neural crest cell and its ectomesenchymal derivatives.** Bildsoe et al. showed the requirement is *not* uniform across derivatives:

> "Since Twist1 is expressed in the tissues of the maxillary eminence and the mandibular arch, this finding suggests that the requirement for Twist1 is not the same in all neural crest derivatives."
> — **PMID:19414008** **[CACHED]**

And a non-cell-autonomous component reaches mesoderm-derived bone:

> "The effect of the loss of Twist1 function is not restricted to neural crest-derived bones, since the predominantly mesoderm-derived parietal and interparietal bones are also affected, presumably as a consequence of lost interactions with neural crest-derived tissues."
> — **PMID:19414008** **[CACHED]**

**CL suggestions (verify every one with `just validate-terms` before binding):**

| CL | Term | Role |
|---|---|---|
| `CL:0000333` | migratory cranial neural crest cell | **primary affected cell type** |
| `CL:0000134` | mesenchymal stem cell | ectomesenchyme |
| `CL:0000062` | osteoblast | skeletogenic differentiation failure |
| `CL:0000138` | chondrocyte | nasal/orbital cartilage |
| `CL:0000057` | fibroblast | craniofacial mesenchyme |

**Tissue types:** neural crest–derived ectomesenchyme (connective/skeletal), membranous bone, cartilage, and — for the eyelid — surface ectoderm-derived structures whose development depends on the underlying mesenchyme.

### Subcellular level

- `GO:0005634` **nucleus** — normal site of TWIST1 action; where the dominant-negative complexes form.
- `GO:0090575` RNA polymerase II transcription regulator complex.
- **Unexpected non-nuclear pool:** TWIST1 is also found in apical endocytic vesicles in the neuroepithelium and physically interacts with β- and δ-catenin:
  > "TWIST1 is expressed in endocytic vesicles at the apical surface and interacts with β/δ-catenins during neural tube closure"
  > — **PMID:35781329** **[CACHED]**

  Relevant GO: `GO:0030139` endocytic vesicle; `GO:0016342`/adherens-junction associations. Whether a Glu117 substitution affects this cytoplasmic pool is **completely unknown** — a good `KNOWLEDGE_GAP`.

### Localization

**UBERON suggestions — treat ALL as leads requiring OAK verification** (`uv run runoak -i sqlite:obo:uberon info "l^<label>"`):
- face, head, nose, orbit / orbital region, eyelid, external ear, palate, mandible, maxilla, frontal bone, skull vault, coronal suture, frontonasal prominence, neural crest, spleen, anus, testis, limb.

**Lateralization:** predominantly **bilateral and symmetric** — bilateral upper eyelid colobomas, bilateral talipes, bilateral cryptorchidism, bilateral coronal synostosis (E117D patient), bilateral syndactyly. Asymmetry is **not** a feature (contrast Saethre–Chotzen, where facial asymmetry is characteristic — a useful differential discriminator).

---

## 8. Temporal Development

### Onset

- **Congenital** — `HP:0003577`, 2/2. Malformations are complete at birth.
- **Embryologic critical window:** cranial neural crest specification, delamination, migration, and frontonasal patterning — approximately **weeks 3–8 of human gestation** (mouse E8.5–E11.5, the window across which the Twist1 phenotypes are established).
- **Prenatal detectability:** polyhydramnios in 1/2. Severe hypertelorism, orbital deficiency and nasal hypoplasia are in principle detectable on second-trimester ultrasound, but **no prenatally diagnosed case has been published**.
- **Onset pattern:** not acute/subacute/chronic — it is a **structural developmental anomaly**, present ab initio.

### Progression

- **Disease course: stable / non-progressive** for the primary malformations. There is no degeneration, no relapsing-remitting pattern, no end-stage.
- **What does change over time is complication burden.** Documented trajectory in Subject 2: eyelid coloboma → surgical repair → **corneal scarring → phthisis of the right eye** **[WEB — PMC5438873, Arizona HOD]**. This is treatment-modifiable secondary damage, not disease progression, and should be modelled as a downstream complication edge rather than a `progression:` phase.
- **In the E117D patient**, craniosynostosis introduces the one genuinely time-critical element: untreated bicoronal synostosis risks raised intracranial pressure and requires surgical release in infancy.
- **Duration:** lifelong.
- **Progression rate:** not applicable.

### Patterns

- **Remission:** none — the concept does not apply.
- **Critical periods for intervention:**
  1. **Neonatal (days):** airway (tracheostomy for choanal atresia/airway compromise), imperforate anus (colostomy/anoplasty), **corneal protection** — arguably the most time-critical and most under-appreciated, since sight loss is preventable.
  2. **Infancy (0–12 mo):** cranial vault surgery *if* synostosis present; hearing assessment and amplification (language window).
  3. **Early childhood:** palate repair / VPI management for speech; syndactyly release; orchidopexy.
  4. **Childhood–adolescence:** staged craniofacial and orbital reconstruction; ongoing developmental support.

---

## 9. Inheritance and Population

### Epidemiology

- **Prevalence: not established.** No Orphanet prevalence class; no registry; no population estimate anywhere in the literature.
- **Total published cases: 3** (2 in Kim 2017; 1 in Takenouchi 2018).
- **Incidence:** unknown.

**Recommended dismech `Prevalence` record** (per the structured-prevalence policy in CLAUDE.md — do *not* use the deprecated free-text `percentage`):

```yaml
prevalence:
- population: Worldwide
  measure_type: CASES_IN_LITERATURE
  prevalence_class: ULTRA_RARE
  notes: >-
    Three published individuals as of August 2026 (two in the delineating
    report, one subsequent case). No prevalence or incidence estimate has
    been published; no Orphanet epidemiology record exists.
```

Do **not** populate `rate_per_100000` — there is no numeric estimate to normalize, and inventing one would be fabrication.

### Genetic parameters

- **Inheritance:** **Autosomal dominant** (`HP:0000006`), all cases *de novo*. Confirmed across sources including the Asian craniosynostosis series:
  > "The pattern of inheritance is autosomal dominant in Saethre-Chotzen syndrome, Robinow-Sorauf syndrome, and Sweeney-Cox syndrome."
  > — Dhiman S, et al. *J Pediatr Genet* 2024. **PMID:39502847** **[CACHED]**
- **Penetrance:** presumed **complete** — 3/3 carriers affected, all severely. No unaffected carrier has been reported. (With n=3 and no transmitting parents, this is an assumption, not a measurement.)
- **Expressivity:** **variable**, and — importantly — the variability tracks the substituting amino acid rather than being stochastic. Val vs Gly vs Asp gives three distinguishable severity/feature profiles.
- **Recurrence risk:** for parents of a *de novo* proband, low but not zero (gonadal mosaicism cannot be excluded); for an affected individual, 50%. **No SWCOS patient has reproduced**, so vertical transmission has never been observed.
- **Genetic anticipation:** not applicable (not a repeat expansion).
- **Germline mosaicism:** not reported; theoretically possible.
- **Founder effects:** none — three unrelated individuals, three different substitutions.
- **Consanguinity:** irrelevant (dominant, *de novo*).
- **Carrier frequency:** not applicable.

### Population demographics

- **Affected populations:** no ethnic predilection. Reported patients came from UK-based clinical genetics services (Kim 2017, contributed by E. Sweeney and H. Cox) and Japan (Takenouchi 2018) — consistent with ascertainment through specialist craniofacial centres rather than any population enrichment.
- **Geographic distribution:** no clustering; sporadic worldwide.
- **Variant geography:** none — each allele reported once.
- **Sex ratio:** 2 male : 1 female. **Not interpretable**; no sex bias is expected for an autosomal dominant *de novo* condition. Do not curate a sex ratio.
- **Age distribution:** all identified in infancy/childhood. No adult SWCOS patient has been described in the literature, so nothing is known about the adult phenotype.

---

## 10. Diagnostics

### The diagnostic pathway in one sentence

**Recognition of the characteristic facial gestalt → molecular confirmation of a TWIST1 codon-117 missense variant.** There is no biochemical or imaging test that makes the diagnosis.

### Clinical tests

- **Laboratory tests:** **none diagnostic.** No enzyme assay, metabolite, or blood/urine marker. No LOINC-codable disease-specific analyte exists.
- **Biomarkers:** none. The only "biomarker" is the genotype.
- **Imaging:**
  - **Craniofacial CT with 3D reconstruction** — the key structural study; defines orbital bone deficiency, suture status, and midface hypoplasia. Takenouchi et al. used spiral CT (MeSH keyword "Tomography, Spiral Computed" on the PubMed record, **[CACHED]**).
  - **Brain MRI** — for cerebellar hypoplasia (1/2) and developmental-delay workup.
  - **Echocardiography** — PDA/PFO.
  - **Abdominal ultrasound** — **essential**, to detect asplenia, which is otherwise silent and carries real infection risk.
  - **Ophthalmic assessment including corneal examination** — for exposure keratopathy.
- **Functional tests:** audiologic assessment (conductive loss); speech/VPI evaluation (nasendoscopy, videofluoroscopy).
- **Electrophysiology:** electrodiagnostic testing was **normal** in Subject 1 despite small eyes and no vision concerns **[WEB — Arizona HOD]**. ECG as part of cardiac workup.
- **Biopsy / histopathology:** **no role.** No characteristic histopathology has been described. Do not curate a `histopathology:` block.

### Genetic testing — the diagnostic modality

| Approach | Utility for SWCOS |
|---|---|
| **Trio whole-exome sequencing (WES)** | **First-line and highest-yield.** The de novo status, the non-classical phenotype, and the broad frontonasal-dysplasia differential all favour unbiased exome. This is how the E117D case was identified. |
| Whole-genome sequencing (WGS) | Reasonable alternative; adds regulatory/structural variant detection (relevant given TWIST1 regulatory-region duplications cause other phenotypes) |
| **Craniosynostosis / craniofacial gene panels** | Will include TWIST1 (present on ≥85% of GTR craniosynostosis panels — the criterion by which ClinGen selected it for curation **[CACHED, PMID:42059179]**). Adequate if the clinician already suspects a TWIST1 disorder, but a panel chosen for *craniosynostosis* may not be reached for a *frontonasal dysplasia* presentation. |
| **Single-gene TWIST1 sequencing** | Appropriate only when the gestalt is recognized. TWIST1's coding region is small (202 aa, principally one coding exon) so this is cheap and fast. |
| Chromosomal microarray (CMA) | **Will not detect SWCOS.** Useful only to exclude 7p21 deletions (→ SCS) and other CNV syndromes in the differential. Used in the Dhiman 2024 series alongside WES and Sanger **[CACHED, PMID:39502847]**. |
| Karyotype / FISH | No role beyond excluding gross rearrangements. |
| mtDNA testing | No role. |
| Repeat-expansion testing | No role. |

**Critical interpretive point:** because SWCOS and SCS are caused by variants in the *same gene, at the same codon*, **the report must specify the variant, not just the gene.** A laboratory report reading "pathogenic TWIST1 variant → Saethre-Chotzen syndrome" is a real misdiagnosis risk — and ClinVar's own condition assignment for p.Glu117Gly demonstrates it happening in practice (§4).

### Omics-based diagnostics

**None applicable.** No RNA-seq, proteomic, metabolomic, epigenomic (methylation episignature), or liquid-biopsy test exists or is under development for SWCOS. A DNA-methylation episignature has not been sought — a plausible but purely speculative future avenue given n=3.

### Clinical criteria

**No formal diagnostic criteria, consensus statement, or society guideline exists.** Diagnosis is: characteristic facial gestalt + confirmed TWIST1 codon-117 missense.

Proposed working gestalt (synthesized from the 3 published patients — explicitly *not* a validated criterion set):
1. Marked hypertelorism, **and**
2. Upper eyelid coloboma or ablepharon with deficient bony orbits/pseudoproptosis, **and**
3. Nasal hypoplasia (hypoplastic alae, short columella, broad tip), **and**
4. *De novo* heterozygous TWIST1 p.Glu117 missense substitution.

### Differential diagnosis

| Condition | Gene | How to distinguish |
|---|---|---|
| **Saethre–Chotzen syndrome** (OMIM 101400) | TWIST1 (haploinsufficiency) | Coronal synostosis dominant, **facial asymmetry**, ptosis, low frontal hairline, broad hallux; **lacks** eyelid coloboma and severe orbital bone deficiency. Same gene, different mechanism. Note the E117D patient blurs this boundary. |
| **Barber–Say syndrome** | TWIST2 p.Glu75Gln/Ala | Ablepharon, macrostomia, hypertelorism, **hypertrichosis, redundant/atrophic skin**; **no craniosynostosis** |
| **Ablepharon–macrostomia syndrome** | TWIST2 p.Glu75Lys | Most severe ablepharon + macrostomia; **no craniosynostosis** |
| **Robinow–Sorauf syndrome** | TWIST1 | Craniosynostosis + **bifid hallux** |
| **Craniofrontonasal syndrome** | EFNB1 (X-linked) | Hypertelorism, bifid nasal tip, coronal synostosis, **longitudinally grooved nails**, sternal anomalies; paradoxical female-severe X-linked inheritance |
| **Frontonasal dysplasia 1/2/3** | ALX3 / ALX4 / ALX1 | **Autosomal recessive**; FND3 has extreme microphthalmia and bilateral facial clefting |
| **Acromelic frontonasal dysostosis** | ZSWIM6 | FND + distinctive limb (tibial/preaxial) anomalies |
| **Teebi hypertelorism syndrome** | SPECC1L | Hypertelorism, prominent forehead; milder |
| **Treacher Collins / mandibulofacial dysostosis** | TCOF1, POLR1C/D | Downslanting palpebral fissures, **lower** lid coloboma (vs upper in SWCOS), malar and mandibular hypoplasia |
| **RNA Pol I–related craniofacial syndromes** | POLR1A/B/C/D | A 2025 report describes a patient with "features overlapping with Sweeney-Cox, Saethre-Cox, Robinow-Sorauf, and Treacher-Collins" (**PMID:41010008**) **[WEB]** — direct evidence that SWCOS enters real-world differential lists |

The framing from Takenouchi is the cleanest single statement of the differential:

> "Sweeney-Cox syndrome, Barber-Say syndrome, and ablepharon-macrostomia syndrome share the facial features of ablepharon, hypertelorism, underdevelopment of the eyelids, and cheek pads adjacent to the corners of the mouth."
> — **PMID:30450715** **[CACHED]**

> "Our review showed that Sweeney-Cox syndrome appears to share many characteristics with Barber-Say syndrome and ablepharon-macrostomia syndrome except for craniosynostosis, which is a cardinal feature of Saethre-Chotzen syndrome."
> — **PMID:30450715** **[CACHED]**

### Screening

- **Newborn screening:** not applicable and not appropriate (no treatable metabolic component).
- **Carrier screening:** not applicable (*de novo* dominant).
- **Cascade screening:** not applicable (no familial cases).
- **Prenatal testing:** available on request for a couple with a previously affected child — targeted testing for the known familial variant by amniocentesis/CVS, or PGT-M. Recurrence risk is low (gonadal mosaicism only), so this is a counselling decision rather than a recommendation.

---

## 11. Outcome / Prognosis

**All prognostic statements below are extrapolations from three patients. There is no survival data, no natural-history study, and no cohort. Curate accordingly.**

### Survival and mortality

- **Survival rate (5-/10-year/overall):** **unknown — no data.** All three published patients were alive at report.
- **Life expectancy:** **not established.** Not obviously reduced by the malformation complex itself in the absence of lethal cardiac or CNS anomalies, but the two known severe-end features that plausibly affect it are (a) airway compromise requiring tracheostomy and (b) **asplenia**, which confers lifelong overwhelming-post-splenectomy-infection–type risk if unrecognized.
- **Mortality rate / disease-specific mortality:** no data.
- **Note on the allelic series:** Takenouchi raises the possibility that some codon-117 substitutions may be **lethal** and therefore unascertained:
  > "This suggests that any amino acid substitutions at Glu117 would likely lead to the Sweeney-Cox syndrome phenotype or lethality."
  > — **PMID:30450715** **[CACHED]**

  This is a strong candidate for an ascertainment-bias `discussions` entry: the three living patients may represent the *survivable* tail of the allelic series.

### Morbidity and function

- **Developmental outcome:** global developmental delay in 2/2; **moderate learning disability** documented in Subject 1 **[WEB — PMC5438873]**. Whether delay is intrinsic (cerebellar hypoplasia, CNS involvement) or partly secondary (hearing loss, prolonged hospitalization, tracheostomy) is unresolved — a genuine knowledge gap.
- **Sensory outcome:** conductive hearing loss (1/2); **vision loss from corneal exposure is documented and is the most clearly preventable morbidity** (phthisis of the right eye in Subject 2 despite lid repair).
- **Communication:** delayed speech and language; velopharyngeal insufficiency and cleft palate compound this.
- **Disability outcomes:** surgical burden across craniofacial, ophthalmic, ENT, orthopaedic, urologic and colorectal domains; long-term multidisciplinary dependence.
- **Quality-of-life measures:** **never assessed with any instrument.**

### Complications

Airway obstruction; exposure keratopathy → corneal scarring → phthisis bulbi; recurrent otitis media / conductive hearing loss; feeding difficulty and GERD; speech impairment from VPI; **infection risk from asplenia**; raised intracranial pressure if craniosynostosis is untreated; anaesthetic risk from difficult airway across repeated surgeries.

### Recovery potential

The structural anomalies are not recoverable, only reconstructable. Functional outcomes for **airway, feeding, hearing and speech are substantially improvable** with timely intervention; **vision is preservable only if corneal protection is instituted early**.

### Prognostic factors

Entirely inferential, but the strongest candidate is **the identity of the substituting amino acid at codon 117** — the same variable that drives the phenotypic continuum. On current evidence: Asp → milder antimorph, adds synostosis; Val → intermediate; Gly → most severe (tracheostomy, cardiac defects, asplenia, eye loss). **n=1 per allele. This is a hypothesis, not a genotype–phenotype rule**, and should be curated with `status: EMERGING` if modelled as a `mechanistic_hypotheses` group.

Other plausible prognostic factors: presence of asplenia, presence of cardiac defect, degree of airway compromise, timeliness of corneal protection.

### Prognostic biomarkers

**None.**

---

## 12. Treatment

### The honest summary

**There is no disease-modifying therapy, no drug, no clinical trial, and no published management guideline for Sweeney-Cox syndrome.** Management is entirely symptomatic, surgical, and supportive, delivered by a multidisciplinary craniofacial team. The Arizona Hereditary Ocular Diseases entry states it plainly: no specific treatment exists for the underlying condition; individual malformations receive targeted care **[WEB]**.

### Pharmacotherapy

**None.** No drug targets the mechanism. No pharmacogenomic considerations. Leave `therapeutic_agent` absent throughout.

### Surgical and interventional (the mainstay)

| Intervention | Indication | NCIT suggestion (**all require `runoak` verification**) |
|---|---|---|
| Eyelid coloboma repair / oculoplastic reconstruction | Corneal protection — **highest priority** | `NCIT:C15329` Surgical Procedure |
| Corneal protection (lubricants, tarsorrhaphy, moisture chambers) | Exposure keratopathy | `NCIT:C15747` Supportive Care |
| Tracheostomy | Airway obstruction (performed in Subject 2 from birth) | `NCIT:C15329` Surgical Procedure |
| Choanal atresia repair | Nasal airway | `NCIT:C15329` |
| Cranial vault remodelling / fronto-orbital advancement | Craniosynostosis (E117D patient) | `NCIT:C15329` |
| Orbital / midface reconstruction, hypertelorism correction (facial bipartition, box osteotomy) | Orbital bone deficiency, hypertelorism | `NCIT:C15329` |
| Palatoplasty; pharyngoplasty for VPI | Cleft palate, velopharyngeal insufficiency | `NCIT:C15329` |
| Anoplasty / colostomy | Imperforate anus | `NCIT:C15329` |
| Orchidopexy | Bilateral cryptorchidism | `NCIT:C15329` |
| Syndactyly release | 2-4 / 2-5 cutaneous syndactyly | `NCIT:C16186` Orthopedic Surgical Procedure |
| Clubfoot management (Ponseti casting ± surgery) | Bilateral talipes equinovarus | `NCIT:C16186` |
| Auricular reconstruction | Microtia | `NCIT:C15329` |
| Gastrostomy | Feeding failure | `NCIT:C15329` |

`therapeutic_modality: SURGERY` for all of the above (mechanically inferable from the NCIT surgical-action terms per the CLAUDE.md backfill table); `DEVICE` for hearing aids and tracheostomy hardware, which cannot be inferred mechanically and needs a per-entry decision.

### Supportive and rehabilitative

| Intervention | NCIT suggestion | Modality |
|---|---|---|
| Hearing amplification / audiologic management | (no reliable NCIT action term for device usage) | `DEVICE` |
| Speech and language therapy | `NCIT:C159273` Speech Therapy | `BEHAVIORAL` |
| Occupational therapy | `NCIT:C121351` Occupational Therapy | `BEHAVIORAL` |
| Physical therapy | `NCIT:C15302` Physical Therapy | `BEHAVIORAL` |
| Nutritional support / feeding management | `NCIT:C15433` Nutritional Support | ⚠️ **do not auto-tag `BEHAVIORAL`** — see the CLAUDE.md caution |
| Developmental / educational support | `NCIT:C15747` Supportive Care | `BEHAVIORAL` |
| Genetic counselling | `NCIT:C15240` Genetic Counseling | `BEHAVIORAL` |
| **Antibiotic prophylaxis + immunization for functional asplenia** | `NCIT:C15986` Pharmacotherapy | `SMALL_MOLECULE` |

The asplenia management item is worth curating explicitly: it is standard of care for asplenia generally (penicillin prophylaxis + pneumococcal/meningococcal/Hib vaccination), it is genuinely life-saving, and it is easy to miss in a patient whose clinical attention is dominated by the face.

### Advanced therapeutics

- **Gene therapy / gene editing:** none for SWCOS. Conceptually, a dominant-negative allele is an **allele-specific silencing** target (ASO or siRNA knockdown of the mutant transcript, or base editing of the c.350/c.351 substitution) — but the disease is established embryonically, so postnatal correction cannot reverse existing dysmorphogenesis. This is a fundamental, not merely practical, barrier and should be stated as such rather than presented as a pipeline.
- **A relevant adjacent result:** RNA nanoparticle gene therapy has been used successfully in *Twist1* mutant **mice** — PEGylated-peptide nanoparticles delivering plasmid DNA expressing **miR-200a**, injected subscalp at P7–P10, inhibited premature suture fusion, increased Gli1⁺/Six2⁺ suture stem cells, and sustained the effect to 56 days (*Science Advances* 2025) **[WEB — PMC12372882]**.
  > ⚠️ **This targets craniosynostosis in a Twist1-haploinsufficient (SCS) model, not Sweeney-Cox.** It is postnatal suture biology, not embryonic frontonasal patterning, and it would not address the SWCOS phenotype. Cite it only with that scope explicitly stated, and grade it `evidence_source: MODEL_ORGANISM`.
- **Cell therapy, RNA therapies, targeted therapy, immunotherapy:** none applicable.

### Experimental treatments / clinical trials

**Zero.** A search of ClinicalTrials.gov and ICTRP returns no interventional or observational study for Sweeney-Cox syndrome. The `clinical_trials:` block should be empty.

### Treatment outcomes, algorithms, personalized medicine

- **Response rates:** no data.
- **Adverse events:** those of the individual procedures; the cumulative anaesthetic risk of a difficult airway across many operations is the notable syndrome-specific concern.
- **Treatment algorithms:** none published. Care follows general craniofacial-team principles.
- **Combination therapy / genotype-guided treatment:** not applicable — genotype currently informs prognosis and counselling only, not therapy choice.

---

## 13. Prevention

### Primary prevention

**Not possible.** *De novo* dominant variants are not preventable by any known intervention. There is no modifiable risk factor, no periconceptional supplement, and no exposure to avoid.

### Secondary prevention (early detection)

This is where prevention is actually meaningful in SWCOS — not preventing the disease, but preventing its avoidable sequelae:

1. **Corneal protection from day one.** The documented loss of an eye to exposure keratopathy in Subject 2 is the strongest argument in the literature for aggressive, immediate ocular surface management in any infant with eyelid coloboma/ablepharon.
2. **Abdominal ultrasound to detect asplenia**, followed by prophylaxis and immunization.
3. **Newborn hearing screening** and ongoing audiologic surveillance.
4. **Cranial imaging for suture status** — the E117D case establishes that craniosynostosis can accompany SWCOS, so it should be actively excluded rather than assumed absent, with ICP surveillance if present.
5. **Airway assessment** for choanal atresia at birth.
6. **Developmental surveillance** from infancy.

### Tertiary prevention

Staged reconstructive surgery to prevent functional deterioration; ICP monitoring; speech therapy to prevent entrenched articulation patterns; antibiotic prophylaxis for asplenia; dental and orthodontic follow-up given midface hypoplasia.

### Immunization

Routine childhood schedule, **plus asplenia-indicated vaccines** (pneumococcal, meningococcal, Hib) where asplenia is present. There is no SWCOS-specific vaccine.

### Genetic screening and counselling

- **Population/carrier screening:** not applicable.
- **Prenatal testing / PGT-M:** available for the known familial variant after an affected child; recurrence risk low (gonadal mosaicism only).
- **Genetic counselling** (`NCIT:C15240`): the essential preventive intervention. Must cover: *de novo* origin, ~50% transmission risk from an affected individual, low sibling recurrence risk, the SWCOS-vs-SCS distinction (so the family is not given SCS prognostic information), and the limits of what is known from three patients.

### Behavioural, public-health, environmental interventions, prophylaxis

Not applicable, except the asplenia antibiotic prophylaxis noted above.

---

## 14. Other Species / Natural Disease

- **Species affected (natural disease):** **none known.** No naturally occurring Sweeney-Cox syndrome has been reported in any non-human species. Nothing in OMIA corresponds to it.
- **Breed (VBO):** not applicable.
- **Orthologous genes:**

| Species | NCBI Taxon | Gene | Note |
|---|---|---|---|
| Human | `NCBITaxon:9606` | TWIST1 (Gene 7291) | Glu117 |
| Mouse | `NCBITaxon:10090` | *Twist1* | equivalent glutamate; extensively studied |
| Zebrafish | `NCBITaxon:7955` | *twist1a*, *twist1b* | ZFIN lists **no** models for this disease |
| *C. elegans* | `NCBITaxon:6239` | ***hlh-8*** — the **single** Twist homolog | equivalent residue **Glu29** — the basis of the disease model |
| *Drosophila* | `NCBITaxon:7227` | *twist* | founding member; mesoderm specification |

- **Veterinary relevance:** none. TWIST1-adjacent note of comparative interest: a severe craniofacial phenotype in **Burmese cats** is caused by homozygous disruption of *Alx1* — the gene TWIST1 directly regulates through the ECR1 enhancer **[CACHED, PMID:41850652, citing Lyons et al. 2016]**. This is a natural animal model of the *downstream* node, not of SWCOS itself, and should not be curated as a SWCOS animal model.
- **Comparative pathology:** the mouse *Twist1* neural-crest conditional knockout reproduces the *direction* of the human defect — loss of snout, upper face and skull vault bones — but as a recessive tissue-specific null, not as a dominant-negative heterozygote.
- **Evolutionary conservation:** exceptional. The glutamate is conserved from *C. elegans* HLH-8 (Glu29) through *Drosophila* Twist to human TWIST1 (Glu117) and TWIST2 (Glu75). This conservation is what licensed the worm allelic series and is itself the strongest *a priori* evidence for pathogenicity.
- **Zoonotic potential / cross-species transmission:** not applicable.

---

## 15. Model Organisms

### 15.1 *Caenorhabditis elegans* — the definitive SWCOS model

**This is the only model organism in which the actual SWCOS disease alleles have been engineered and studied**, and it is the source of the dominant-negative conclusion.

- **Model type:** invertebrate; CRISPR-engineered knock-in allelic series at the endogenous *hlh-8* locus.
- **Rationale:** *C. elegans* has a **single** Twist homolog (*hlh-8*), eliminating the paralogue redundancy that confounds vertebrate models, and permitting single-cell-resolution readouts in the developing mesoderm.
- **Alleles engineered:** all five human disease substitutions at the equivalent **Glu29** residue — Glu29Val and Glu29Gly (SWCOS), Glu29Ala and Glu29Gln (Barber–Say), Glu29Lys (AMS). A Glu29Asp allele corresponding to the Takenouchi patient is also described in this line of work **[UNVERIFIED — confirm which paper generated the Asp allele before citing].**
- **Readouts:** target-gene expression in vulval and enteric muscle; constipation/defecation defect; egg-laying/embryo-retention phenotype.
- **Result — graded severity:**
  > "This allelic series revealed that different substitutions exhibit graded severity, in terms of both gene expression and cellular phenotype, which we incorporate into a model explaining the various human disease phenotypes."
  > — **PMID:28369379** **[CACHED]**

  Reported ordering, most to least severe: **Glu29Lys (AMS) > Glu29Val (and Glu29Asp) > Glu29Gly ≈ Glu29Ala ≈ Glu29Gln**, with the weaker alleles retaining residual target-gene expression (74–100% in intestinal muscles) **[WEB — PMC5438873]**.
- **Dominant-negative evidence:** *hlh-8* null alleles behave **recessively**, whereas **all** Glu29 heterozygotes showed semi-dominant embryo retention and reduced target-gene expression in vulval muscle — i.e. the mutant proteins interfere with wild-type HLH-8 **[WEB — PMC5438873]**. This heterozygote-vs-null contrast is the crux of the argument and is exactly what a `RECAPITULATES` link with a mechanism-level `target` should point at.
- **Tissue-specific sensitivity:** vulval muscles (heterodimer-dependent) were more sensitive than enteric muscles (where HLH-8 homodimers matter) **[WEB]** — an elegant internal control showing the defect is dimer-context-dependent.
- **Phenotype recapitulation:** **excellent for mechanism, nil for morphology.** The worm reproduces the *molecular logic* (allele-specific graded antimorphism, heterozygous interference) but has no craniofacial structures, no neural crest, and no vertebrate skeleton. This is the textbook case for `PARTIALLY_RECAPITULATES` with an explicit `limitations` string.
- **Suggested dismech link:**
  ```yaml
  animal_models:
  - name: C. elegans hlh-8 Glu29 disease-allele series
    species: Caenorhabditis elegans
    genotype: hlh-8(Glu29Val), hlh-8(Glu29Gly) knock-in heterozygotes and homozygotes
    publication: PMID:28369379
    modeled_mechanisms:
    - target: <the dominant-negative dimer-sequestration node>
      relationship: PARTIALLY_RECAPITULATES
      fidelity: MODERATE
      limitations: >-
        C. elegans has no neural crest, no craniofacial skeleton, and no
        vertebrate suture biology; the model recapitulates the allele-specific
        antimorphic logic and heterozygous interference, not the human
        frontonasal phenotype. Readouts are mesodermal muscle lineages.
  ```
- **Database:** WormBase.

### 15.2 Mouse — the gene model, not the disease model

**No mouse carrying a Twist1 Glu117-equivalent knock-in has been reported.** This is the single largest experimental gap for SWCOS.

| Model | Phenotype | Relevance |
|---|---|---|
| ***Twist1*<sup>−/−</sup> null** | Embryonic lethal at mid-gestation; complete neural tube closure defect at E11.5 **[CACHED, PMID:35781329]** | Establishes requirement; not a disease model |
| ***Twist1*<sup>+/−</sup> heterozygote** | **100% craniosynostosis** (though not complete coronal fusion); acrocephalic, brachycephalic, wide skull; shortened cranial base **[WEB]** | Established **Saethre–Chotzen** model — **NOT** a SWCOS model. Do not curate it as one. |
| ***Twist1*<sup>fl/fl</sup>; Wnt1-Cre / Wnt1-Cre2** (NCC-conditional) | Loss of snout, upper face and skull vault bones; no recognizable maxilla; malformed mandible; exencephaly; ~50% fewer migratory CNCCs, 68% shorter migration **[CACHED, PMID:19414008 + PMID:35781329]** | **Closest phenocopy of the SWCOS craniofacial defect** — but as a tissue-specific *null*, not a dominant negative |
| ***Twist1*<sup>fl/fl</sup>; Sox10-Cre** | Dramatic disruption of frontonasal development; failure to activate *Alx1*, *Alx3*, *Alx4* in the FNP **[CACHED, PMID:41850652]** | The mechanistic link to the frontonasal gene program |
| ***Alx1*<sup>ΔDE1/ΔDE1</sup>** (Twist1-bound enhancer deletion) | Hypoplastic/disrupted nasal cartilages, shortened premaxilla (10/10), malocclusion (7/10), disorganized extraocular muscles; >80% loss of *Alx1* mRNA at E10.5 **[CACHED, PMID:41850652]** | Models the *downstream node*; shows what losing the TWIST1→ALX1 edge does |
| ***Twist1* phospho-incompetent knock-in lines** | Epidermal blebbing, edema, neural tube defects, CNCC-derived structural abnormalities **[CACHED, PMID:35781329]** | Dimer-regulation axis (SCS-adjacent) |
| ***Irf6*<sup>+/−</sup>; *Twist1*<sup>+/−</sup> compound** | Mandibular agnathia, fused maxilla, cleft palate, holoprosencephaly **[CACHED, PMID:35781329]** | Genetic-interaction model |

> **Curation warning.** The temptation to attach *Twist1*<sup>+/−</sup> mice to a Sweeney-Cox entry should be resisted — that genotype models **haploinsufficiency**, the mechanism SWCOS explicitly is *not*. If included at all, it belongs with `relationship: FAILS_TO_RECAPITULATE` against the dominant-negative node, with `limitations` and `evidence` supplied (both required for that relationship value by `test_failure_to_recapitulate_links_are_substantiated`).

### 15.3 Zebrafish

- ZFIN carries the human disease term `ZDB-TERM-190716-1` for Sweeney-Cox syndrome with **no genes and no models registered** **[WEB]**.
- A zebrafish *twist* model of **Saethre-Chotzen** craniosynostosis exists (altered bone growth dynamics prefiguring suture fusion) **[WEB — PMC6207424]** — again, SCS not SWCOS.
- The paralogue duplication (*twist1a*/*twist1b*) makes zebrafish a poorer choice than *C. elegans* for a dominant-negative allelic series.

### 15.4 Cellular / in vitro systems

- **hPSC-derived cranial neural crest cells (hCNCCs)** — the most promising unexploited system. The Coordinator-motif work (**PMID:38262408**) and the TF-dosage work (**PMID:40020686**) both use hCNCC differentiation and directly interrogate TWIST1 binding, chromatin opening, and dose-response. **Knocking a p.Glu117Val allele into hPSCs and differentiating to CNCC would be the single highest-value experiment for this disease** and is, as far as I can determine, not yet published.
- **Structural/biophysical:** PDB `8OSB` (TWIST1–TCF4–ALX4 on DNA) supports in silico modelling of E117V/G/D.
- **Patient-derived lines:** none reported. No fibroblast or iPSC line from any of the three patients is described or deposited.

### 15.5 Applications and gaps

**Answerable with existing models:** the dominant-negative-vs-null distinction; graded allele severity; the TWIST1→ALX1 regulatory edge; CNCC EMT/migration/survival requirements; suture biology.

**Not answerable with existing models — recommended `discussions` entries:**
- `HUMAN_MODEL_MISMATCH` — the antimorphic mechanism is demonstrated only in *C. elegans* mesodermal muscle; it has **never been tested in a vertebrate craniofacial context**, and no mammalian model of a Glu117-equivalent substitution exists.
- `KNOWLEDGE_GAP` — why is the *frontonasal/periocular* region specifically vulnerable, when TWIST1 is expressed throughout CNCCs and pharyngeal arches? (The Coordinator/homeodomain-partner hypothesis is the leading answer but is untested for Glu117.)
- `KNOWLEDGE_GAP` — is the developmental delay intrinsic (cerebellar hypoplasia, CNS TWIST1 function) or secondary (hearing loss, hospitalization, airway)?
- `KNOWLEDGE_GAP` — does a Glu117 substitution affect the non-nuclear, β/δ-catenin-associated TWIST1 pool described in PMID:35781329?
- `KNOWLEDGE_GAP` — Takenouchi's lethality conjecture: are the three known patients the survivable tail of the codon-117 allelic series?

---

## Curation appendix — ready-to-use evidence items

These snippets are **exact substrings of files already in `references_cache/`** and will pass `just count-verified-snippets` / `just validate-references` without further fetching. Everything else in this report must be fetched with `just fetch-reference <ID>` before it can be quoted.

```yaml
# Disease definition / delineation
- reference: PMID:28369379
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: "Here, we describe a new clinical entity, Sweeney-Cox syndrome, associated with distinct de novo amino acid substitutions (p.Glu117Val and p.Glu117Gly) at a highly conserved glutamic acid residue located in the basic DNA binding domain of TWIST1, in two subjects with frontonasal dysplasia and additional malformations."
  explanation: Delineates the entity and its two founding de novo TWIST1 alleles.

# Codon-117 specificity vs the SCS mutation spectrum
- reference: PMID:28369379
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: "Although about one hundred different TWIST1 mutations have been reported in patients with the dominant haploinsufficiency Saethre-Chotzen syndrome (typically associated with craniosynostosis), substitutions uniquely affecting the Glu117 codon were not observed previously."
  explanation: Establishes codon 117 as a distinct hotspot separate from the SCS haploinsufficiency spectrum.

# Dominant-negative mechanism
- reference: PMID:28369379
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: "The genetic analysis favors a predominantly dominant-negative mechanism for the action of amino acid substitutions at this highly conserved glutamic acid residue"
  explanation: C. elegans allelic series supports antimorphic rather than loss-of-function action.

# Graded severity across the allelic series
- reference: PMID:28369379
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: "This allelic series revealed that different substitutions exhibit graded severity, in terms of both gene expression and cellular phenotype, which we incorporate into a model explaining the various human disease phenotypes."
  explanation: Basis for the activity-continuum model relating substituting residue to disease.

# Antimorphic effect shared with the TWIST2 disorders
- reference: PMID:30450715
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: "Heterozygous localized TWIST1 and TWIST2 basic domain substitutions exert antimorphic effects to cause Sweeney-Cox syndrome, Barber-Say syndrome, and ablepharon-macrostomia syndrome, respectively."
  explanation: Independent statement of the antimorphic mechanism across the paralogous hotspots.

# Third patient: craniosynostosis + ablepharon with p.Glu117Asp
- reference: PMID:30450715
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: "Herein, we document a male infant with the distinctive facial features of ablepharon, hypertelorism, cheek pads adjacent to the corners of the mouth, and bilateral coronal suture craniosynostosis who had a de novo heterozygous mutation in the basic domain of TWIST1, that is, c.351C>G p.Glu117Asp."
  explanation: Extends the phenotype to include craniosynostosis and adds the third causal allele.

# The SWCOS / SCS boundary
- reference: PMID:30450715
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: "Our review showed that Sweeney-Cox syndrome appears to share many characteristics with Barber-Say syndrome and ablepharon-macrostomia syndrome except for craniosynostosis, which is a cardinal feature of Saethre-Chotzen syndrome."
  explanation: Positions SWCOS in the differential against the TWIST2 disorders and SCS.

# Mild-antimorph model for the Asp allele
- reference: PMID:30450715
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: "The present observation suggests that a localized TWIST1 basic domain substitution, that is, p.Glu117Asp, in TWIST1 may exert a mild antimorphic effect similar to that of haploinsufficiency, leading to craniosynostosis and ablepharon."
  explanation: Supports the dose-continuum edge linking milder antimorphism to a synostosis phenotype.

# Inheritance
- reference: PMID:39502847
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: "The pattern of inheritance is autosomal dominant in Saethre-Chotzen syndrome, Robinow-Sorauf syndrome, and Sweeney-Cox syndrome."
  explanation: Confirms autosomal dominant inheritance for SWCOS.

# Twist1 requirement in frontonasal / skull vault development (mouse)
- reference: PMID:19414008
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: "Loss of Twist1 in neural crest cells and their derivatives impairs skeletogenic differentiation and leads to the loss of bones of the snout, upper face and skull vault."
  explanation: Mouse NCC-conditional null supports the neural-crest skeletogenic node.

# Non-cell-autonomous extension to mesodermal bone
- reference: PMID:19414008
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: "The effect of the loss of Twist1 function is not restricted to neural crest-derived bones, since the predominantly mesoderm-derived parietal and interparietal bones are also affected, presumably as a consequence of lost interactions with neural crest-derived tissues."
  explanation: Supports a non-cell-autonomous edge from NCC dysfunction to mesoderm-derived skull vault bone.

# TWIST1 in CNCC EMT
- reference: PMID:35781329
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: "Twist1 suppresses Irf6 and other epithelial genes in CNCCs during the epithelial-to-mesenchymal transition (EMT) process and cell migration. Conversely, a loss of Twist1 leads to a sustained expression of epithelial and cell adhesion markers in migratory CNCCs."
  explanation: Supports the EMT/migration node downstream of TWIST1 dysfunction.

# TWIST1 as a CNCC survival/proliferation factor
- reference: PMID:35781329
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: "TWIST1 has been shown to promote cell survival and proliferation of migratory CNCCs during craniofacial development"
  explanation: Supports the CNCC survival node in the causal chain.

# SWCOS vs SCS phenotype framing (2026)
- reference: PMID:41850652
  supports: SUPPORT
  evidence_source: OTHER
  snippet: "Mutations in TWIST1 have been associated with Sweeney-Cox (OMIM 617746) and Saethre-Chotzen (OMIM 101400) syndromes, with Sweeney-Cox syndrome characterized by hypertelorism with severe deficiency in frontal bones and hypoplasia of the nose and facial bones while Saethre-Chotzen syndrome exhibits craniosynostosis with hypertelorism and maxillary hypoplasia"
  explanation: Current framing of the SWCOS phenotype in contrast with SCS.

# TWIST1 -> ALX1 regulatory edge
- reference: PMID:41850652
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: "mice with lineage-specific inactivation of Twist1 in migrating neural crest cells, exhibited dramatic loss of Alx1 mRNA expression in the developing frontonasal CNCCs"
  explanation: Supports the causal edge from TWIST1 dysfunction to failure of the frontonasal ALX gene program.
```

### The finding that most changes how this entry should be written

ClinGen's Craniofacial Malformations GCEP evaluated TWIST1 against three separate disease assertions and reached three different verdicts — **Definitive** for Saethre-Chotzen, **Moderate** for TWIST1-related craniosynostosis, and **Limited** for Sweeney-Cox:

> "Three rare but clinically defined and distinguishable gene-disease pairs were found to have Limited evidence ranging from 3 to 4 points to support the relationship by the Cranio GCEP: FGFR1-related osteoglophonic dysplasia (OMIM:166250), TWIST1-related Sweeney-Cox syndrome (OMIM:617746), and FGFR2 and lacrimo-auriculo-dento-digital (LADD) syndrome (OMIM:149730)"
> — Edoh EYA, et al. *Genet Med* 2026. **PMID:42059179** **[CACHED]**

with the operational consequence spelled out in the same paper:

> "According to ACMG technical standards, genes classified as Moderate, Strong, or Definitive are eligible for inclusion in diagnostic testing panels, whereas those below this threshold should not be considered."
> — **PMID:42059179** **[CACHED]**

Two things follow. First, this is a **clinically distinguishable entity with a well-supported mechanism whose gene–disease validity is nonetheless formally `Limited`** — the constraint is case count (3), not evidence quality, and the paper is explicit that Moderate and Limited curations are revisited every three years. Second, a dismech entry that presents SWCOS with the same confidence as a Definitive relationship would be overstating the field's own position. State the `Limited` classification in the entry, cite it, and let the mechanism sections carry the weight they legitimately can.

---

## Sources

- [Kim S, Twigg SRF, et al. Localized TWIST1 and TWIST2 basic domain substitutions cause four distinct human diseases that can be modeled in *Caenorhabditis elegans*. Hum Mol Genet 2017 — PMID:28369379](https://pubmed.ncbi.nlm.nih.gov/28369379/) · [full text PMC5438873](https://pmc.ncbi.nlm.nih.gov/articles/PMC5438873/) · [Oxford Academic](https://academic.oup.com/hmg/article/26/11/2118/3091092)
- [Takenouchi T, et al. Ablepharon and craniosynostosis in a patient with a localized TWIST1 basic domain substitution. Am J Med Genet A 2018 — PMID:30450715](https://pubmed.ncbi.nlm.nih.gov/30450715/)
- [Edoh EYA, et al. Evidence-based classification of genes implicated in craniosynostosis disorders using the ClinGen curation framework. Genet Med 2026 — PMID:42059179](https://pubmed.ncbi.nlm.nih.gov/42059179/)
- [Huang Y, et al. A Twist1-regulated distal enhancer crucial for Alx1 gene expression and function during craniofacial development. Dev Biol 2026 — PMID:41850652](https://pubmed.ncbi.nlm.nih.gov/41850652/)
- [Dhiman S, et al. TWIST1 Gene Variants Cause Craniosynostosis with Limb Abnormalities in Asian Patients. J Pediatr Genet 2024 — PMID:39502847](https://pubmed.ncbi.nlm.nih.gov/39502847/)
- [Bertol JW, et al. TWIST1 interacts with β/δ-catenins during neural tube development. Development 2022 — PMID:35781329](https://pubmed.ncbi.nlm.nih.gov/35781329/)
- [Bildsoe H, et al. Requirement for Twist1 in frontonasal and skull vault development in the mouse embryo. Dev Biol 2009 — PMID:19414008](https://www.sciencedirect.com/science/article/pii/S0012160609002814)
- [DNA-guided transcription factor cooperativity shapes face and limb mesenchyme. Cell 2024 — PMID:38262408](https://www.cell.com/cell/fulltext/S0092-8674(23)01438-1)
- [Marchegiani S, et al. Recurrent Mutations in the Basic Domain of TWIST2 Cause Ablepharon Macrostomia and Barber-Say Syndromes. Am J Hum Genet 2015 — PMID:26119818](https://pubmed.ncbi.nlm.nih.gov/26119818/)
- [The ALX4 dimer structure provides insight into how disease alleles impact function. Nat Commun 2025 — PMID:40410151](https://www.nature.com/articles/s41467-025-59728-9)
- [Inhibition of craniosynostosis and premature suture fusion in Twist1 mutant mice with RNA nanoparticle gene therapy. Sci Adv 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12372882/)
- [OMIM #617746 — Sweeney-Cox syndrome](https://www.omim.org/entry/617746) · [Clinical Synopsis](https://omim.org/clinicalSynopsis/617746) · [OMIM *601622 TWIST1](https://omim.org/entry/601622)
- [HPO annotations for OMIM:617746 (ontology.jax.org API)](https://ontology.jax.org/api/network/annotation/OMIM:617746)
- [UniProt Q15672 — TWIST1_HUMAN](https://rest.uniprot.org/uniprotkb/Q15672.txt) · [HGNC:12428](https://rest.genenames.org/fetch/symbol/TWIST1) · [RCSB PDB 8OSB](https://www.rcsb.org/structure/8OSB)
- [ClinVar — TWIST1 variants at codon 117](https://www.ncbi.nlm.nih.gov/clinvar/RCV003314297/)
- [GTR condition C4540299 — Sweeney-Cox syndrome](https://www.ncbi.nlm.nih.gov/gtr/conditions/C4540299/) · [Disease Ontology DOID:0080538](https://www.informatics.jax.org/disease/DOID:0080538) · [ZFIN human disease term](https://zfin.org/ZDB-TERM-190716-1)
- [Hereditary Ocular Diseases — Sweeney-Cox Syndrome (Univ. of Arizona)](https://disorders.eyes.arizona.edu/disorders/sweeney-cox-syndrome-0)

---

**Next step:** if you want this turned into the KB entry, the highest-value first pass is the pathophysiology chain in §6.1 — nine nodes with `biological_scale` tags already assigned, the `GO:0070888` E-box-binding-lost / `GO:0046983` dimerization-retained contrast as the mechanistic core, and eleven cache-verified snippets ready to attach. Say the word and I'll draft it against the untracked `kb/disorders/Sweeney-Cox_Syndrome.yaml` on this branch.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 21 |
| Resolved | 21 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 21 |
| On topic | 12 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:40020686` *(abstract only)*: "how concentrations of the dosage-sensitive TFs TWIST1 and SOX9 affect regulatory element chromatin accessibility in facial progenitor cells"
  - closest text in source: "We applied transfer learning to predict how concentrations of the dosage-sensitive TFs TWIST1 and SOX9 affect regulatory element (RE) chromatin accessibility in facial progenitor cells, achieving near-experimental accuracy"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 94 |
| Resolved | 88 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 6 |
| Terms whose name was checked | 73 |
| Terms named correctly | 64 |
| Terms named as a **different** term | 3 |
| Terms whose name is worth a second look | 6 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `DOID:0080538` (4 mentions) - the report calls it "Disease Ontology"; DOID calls it **Sweeney-Cox syndrome**
- `NCIT:C15329` (10 mentions) - the report calls it "Nasal airway", "Craniosynostosis (E117D patient)", "Orbital bone deficiency, hypertelorism", "Cleft palate, velopharyngeal insufficiency", "Imperforate anus", "Bilateral cryptorchidism", "Microtia", "Feeding failure"; NCIT calls it **Surgical Procedure**
- `NCIT:C16186` (2 mentions) - the report calls it "Bilateral talipes equinovarus"; NCIT calls it **Orthopedic Surgical Procedure**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0002023` (1 mention) - the report calls it "Anal atresia** (imperforate anus)"; HP calls it **Anal atresia**, and lists "Imperforate anus" among its other names
- `HP:0003577` (3 mentions) - the report calls it "Congenital onset** (2/2)"; HP calls it **Congenital onset**
- `GO:0006357` (1 mention) - the report calls it "Regulation of transcription by RNA Pol II"; GO calls it **regulation of transcription by RNA polymerase II**
- `CL:0000333` (1 mention) - the report calls it "migratory cranial neural crest cell"; CL calls it **migratory neural crest cell**
- `NCBITaxon:6239` (1 mention) - the report calls it "C. elegans"; NCBITaxon calls it **Caenorhabditis elegans**, and lists "Rhabditis elegans" among its other names
- `NCBITaxon:7227` (1 mention) - the report calls it "Drosophila"; NCBITaxon calls it **Drosophila melanogaster**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCIT:C15329` - called "Nasal airway", "Craniosynostosis (E117D patient)", "Orbital bone deficiency, hypertelorism", "Cleft palate, velopharyngeal insufficiency", "Imperforate anus", "Bilateral cryptorchidism", "Microtia", "Feeding failure"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIM`.