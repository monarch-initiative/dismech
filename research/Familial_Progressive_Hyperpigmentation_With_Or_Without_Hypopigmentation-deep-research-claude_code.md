---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-28T20:08:11.868890'
end_time: '2026-08-28T20:20:07.955680'
duration_seconds: 716.09
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Familial Progressive Hyperpigmentation With Or Without Hypopigmentation
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
  web_search_requests: 20
  num_turns: 50
  total_cost_usd: 4.4438189999999995
  session_id: c0b3cbc9-34b1-44c4-b2d8-9e74be992953
  stop_reason: end_turn
  permission_denials: 1
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
citation_count: 50
reference_validation:
  total_references: 29
  verified: 29
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 45
  quotes_valid: 30
  quotes_unsupported: 15
  unsupported_quote_references:
  - PMID:19375057
  - PMID:29186243
  - PMC:PMC2680999
  - PMID:22577587
  - PMID:24479586
  - PMID:14635084
  quotes_not_checkable: 1
  relevance_assessed: 29
  on_topic: 15
  off_topic: 1
  off_topic_references:
  - PMC:PMC8544362
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 43
  verified: 38
  not_found: 0
  obsolete: 2
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 5
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: NCIT:C15747
    reported_labels:
    - Direct cosmetic benefit, zero risk
    - Visible congenital difference
    ontology_label: Supportive Care
  obsolete_terms:
  - term_id: GO:0014065
    ontology_label: obsolete phosphatidylinositol 3-kinase signaling
    replaced_by: GO:0043491
  - term_id: GO:0005615
    ontology_label: obsolete extracellular space
    replaced_by: GO:0005576
  unresolvable_prefixes:
  - ORPHA
  - MGI
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Familial Progressive Hyperpigmentation With Or Without Hypopigmentation
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Familial Progressive Hyperpigmentation With Or Without Hypopigmentation** covering all of the
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

# Familial Progressive Hyperpigmentation With Or Without Hypopigmentation (FPHH)

**Research report for dismech KB entry** · MONDO:0007771 · OMIM #145250 · Gene: *KITLG* · Compiled 2026-08-28

**Scope note.** FPHH is an ultra-rare Mendelian genodermatosis with a literature base of roughly 15–20 primary reports, essentially all single-family or single-case genetic studies. Several template sections (epidemiology with rates, natural-history cohorts, clinical trials, treatment-outcome data, prognostic biomarkers, omics atlases, veterinary natural disease) have **no published data at all**, and I mark those explicitly rather than inferring. Where the literature is internally inconsistent (melanocyte counts; variant counts; RefSeq accessions) I flag the conflict instead of resolving it silently.

**Ontology-term caveat.** CURIEs below are *leads for a curator*, not validated bindings. Per the repo's term contract (`dismech-terms`), each must be confirmed with `just validate-terms` / OAK before it enters YAML — a label mismatch or a term outside the dynamic enum will fail CI, and no term beats a bad one. I have marked the ones I am least confident about.

---

## 1. Disease Information

### Overview

FPHH is an autosomal dominant pigmentary genodermatosis in which **diffuse, progressive hyperpigmentation** — present at birth or appearing in early infancy — enlarges and coalesces with age, in most (not all) patients intermingled with **café-au-lait macules (CALMs), lentigines, and hypopigmented ash-leaf macules**. It is caused by heterozygous **gain-of-function missense variants in *KITLG*** (KIT ligand / stem cell factor) at 12q21.32, which increase melanogenic signalling through the melanocyte KIT receptor.

> "Familial progressive hyper- and hypopigmentation (FPHH, MIM 145250) is a rare hereditary skin disorder that is predominantly characterized by progressive, diffuse, partly blotchy hyperpigmented lesions intermingled with scattered hypopigmented spots, lentigines and sometimes Cafe-au-lait spots (CALs)." — Wang J *et al.* 2021, *BMC Med Genomics* ([PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/))

> "Familial progressive hyperpigmentation (FPH) is an autosomal-dominantly inherited disorder characterized by hyperpigmented patches in the skin, present in early infancy and increasing in size and number with age." — Wang ZQ *et al.* 2009, *Am J Hum Genet* ([PMID:19375057](https://pubmed.ncbi.nlm.nih.gov/19375057/))

The disorder is essentially **skin-limited**. Nails, hair, teeth, mucosae and internal organs are typically normal ("none of them showed any other skin, nail, hair, teeth, mucosal or systemic diseases" — [PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/)), with rare exceptions discussed in §3.

### The FPH / FPHH split — important for entry scoping

Two OMIM entities exist and are **not** the same disease:

| Entity | OMIM | Locus/gene | Distinguishing feature |
|---|---|---|---|
| **FPHH** — hyperpigmentation with or without hypopigmentation, familial progressive | **#145250** | *KITLG*, 12q21.32 | Hypopigmented/ash-leaf macules **may** be present; CALMs, lentigines |
| **FPH1** — hyperpigmentation, familial progressive, 1 | #614233 | **19pter–p13.1**, gene unknown | Hyperpigmentation only, no hypopigmented component; mapped in a 3-generation Han Chinese family, onset as early as age 5 |

Amyere *et al.* explicitly separate them and place FPH nearer DUH2:

> "FPHH is distinct from familial progressive hyperpigmentation (FPH), in which no hypopigmented features are present, and which is phenotypically and histologically closer to Dyschromatosis Universalis Hereditaria 2 (DUH2)." — Amyere *et al.* 2011, *J Invest Dermatol* ([PMID:21368769](https://pubmed.ncbi.nlm.nih.gov/21368769/))

Complicating this, OMIM folded the original *KITLG* FPH family (Wang 2009) into #145250, so **the "FPH" label in the 2009 paper and the "FPHH" label in later papers refer to the same *KITLG* allelic entity**, while OMIM #614233 (FPH1) is a genetically distinct, still-unsolved locus. The dismech entry should cover the *KITLG* entity (MONDO:0007771 / OMIM #145250) and record FPH1 as a differential/related-but-distinct concept, not as a subtype.

### Identifiers

| Resource | Identifier |
|---|---|
| MONDO | **MONDO:0007771** — "hyperpigmentation with or without hypopigmentation, familial progressive" (as used in the existing stub) |
| OMIM | **#145250** (FPHH); gene *KITLG* **\*184745** |
| Orphanet | **ORPHA:280628** "Familial progressive hyper- and hypopigmentation"; **ORPHA:79146** "Familial progressive hyperpigmentation" (separate concept) |
| MedGen / UMLS | **C1840392** |
| GTR condition | [C1840392](https://www.ncbi.nlm.nih.gov/gtr/conditions/C1840392/) — 42 tests listed for *KITLG*, 8 clinical tests for this condition |
| Genomics England PanelApp | *KITLG* — **Green** on "Pigmentary skin disorders" (panel 559), monoallelic |
| ICD-10 | No specific code; maps under **L81.x** (other disorders of pigmentation) — *no authoritative source found assigning a specific code; treat as uncoded* |
| ICD-11 | Best fit **EL5x** family (disorders of skin pigmentation) — *not verified; do not bind without checking* |

**Note for the curator:** Orphanet is programmatically blocked from web fetch, but this repo already ingests Orphadata. `just structured-rebuild-orphanet --id 280628` (and `--id 79146`) will produce quotable `ORPHA:` cache rows for the definition, prevalence class, HPO frequencies, and gene-disease row — a better evidence source for §3 and §9 than anything available on the open web.

### Synonyms

- Familial progressive hyper- and hypopigmentation (**FPHH**)
- Familial progressive hyperpigmentation with or without hypopigmentation
- **Melanosis universalis hereditaria** (used as a synonym by GTR and by [PMID:39152874](https://pubmed.ncbi.nlm.nih.gov/39152874/))
- Congenital hypomelanotic and hypermelanotic macules (GTR synonym)
- **Westerhof syndrome** (for the 1978 Hindustani-origin family with growth/mental retardation, [PMID:666331](https://pubmed.ncbi.nlm.nih.gov/666331/))
- Familial progressive hypo- and hyperpigmentation (variant word order used in some case reports)
- Universal melanosis / melanosis diffusa congenita / familial diffuse melanosis (older, loosely applied terms)
- Gene aliases relevant to search: *SCF*, *SF*, *MGF*, *KL-1*, *SLF*, *SHEP7*, *DCUA*, *FPH2*, *FPHH*, *DFNA69*, *WS2F*

### Evidence provenance

**All of it is aggregated disease-level and case/family-level literature.** There is no EHR-derived cohort, no registry, and no biobank series for FPHH. Every quantitative statement in this report traces to a single-family report or an in-vitro experiment. This matters for the entry: frequencies are qualitative, and prevalence is undocumented (see §9).

---

## 2. Etiology

### Primary cause — *KITLG* gain of function

FPHH is a **monogenic, non-environmental, non-infectious** disorder. Heterozygous missense variants in *KITLG* increase the melanogenic output of the KITLG→KIT axis in skin.

> "To our knowledge, these data provided the first genetic evidence that the FPH disease is caused by the KITLG N36S mutation, which has a gain-of-function effect on the melanin synthesis" — [PMID:19375057](https://pubmed.ncbi.nlm.nih.gov/19375057/)

> "Most of the FPHH-causing mutations in KITLG are clustered within the conserved VTNNV motif (amino acids 33–37) in exon 2, and a mutated VTNNV domain may increase the affinity of KITLG to the c-Kit receptor, suggesting that the mutation causes a downstream gain-of-function effect." — [PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/)

> "All the reported mutations affected the residues within the KIT ligand domain, leading to an increased affinity to the kit receptor." — Huang *et al.* ([PMID:39152874](https://pubmed.ncbi.nlm.nih.gov/39152874/))

### Locus heterogeneity — a substantial fraction of FPHH is *not* *KITLG*

This is a well-documented and under-appreciated feature and should be curated as a **knowledge gap**:

> "However, many FPHH families without KITLG mutations have been identified, indicating additional locus heterogeneity for this disorder" — [PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/)

> "sequencing analysis did not show any mutation of the KITLG gene in the ten affected individuals" ... the family "provided evidence for genetic heterogeneity of this genodermatosis" — Chinese 4-generation family, 14 affected ([PMID:29186243](https://pubmed.ncbi.nlm.nih.gov/29186243/), *An Bras Dermatol*)

See also the explicitly titled report "Familial progressive hyperpigmentation and hypopigmentation without KITLG mutation" ([PMID:27859606](https://pubmed.ncbi.nlm.nih.gov/27859606/); letter, abstract not available in cache — **do not use for snippet evidence**, cite only for the existence of KITLG-negative families, or better, cite [PMID:29186243](https://pubmed.ncbi.nlm.nih.gov/29186243/) which has extractable text).

The unsolved **FPH1 locus at 19pter–p13.1** (OMIM 614233) is a second, independent line of evidence for heterogeneity within the broader clinical concept.

### Risk factors

- **Genetic (causal, not "risk"):** a heterozygous *KITLG* KIT-ligand-domain missense allele is sufficient. There are no reported susceptibility loci or modifier genes for FPHH.
- **Family history:** the dominant determinant; an affected parent confers 50% transmission risk. But de novo occurrence is well documented (§9), so a negative family history does not exclude the diagnosis.
- **Ancestry:** case reports are heavily weighted to **Han Chinese** and **Japanese** populations, with additional European (Slovenian, Danish, German), Filipino, and Hindustani-origin families. This almost certainly reflects **ascertainment and publication bias**, not a true founder effect — no shared haplotype has been reported, and the recurrent alleles (p.Thr34Ile, p.Asn36Ser) are at CpG-poor but structurally constrained residues where recurrence is expected from a mutational hotspot, not descent.
- **Environmental:** **none identified.** Not toxin-, radiation-, drug-, or occupation-related. Age is not a risk factor for onset (congenital/infantile) but *is* the driver of lesion accumulation (§8).
- **Sex:** no sex bias reported; both sexes affected in every pedigree (e.g. seven affected — three men, four women — in family 1 of [PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/); 9 men and 5 women in the KITLG-negative family, [PMID:29186243](https://pubmed.ncbi.nlm.nih.gov/29186243/)).
- **Consanguinity:** irrelevant for FPHH itself (dominant). It *is* relevant to the allelic recessive *KITLG* disorders (WS2F, biallelic hypomelanosis–deafness, [PMID:35543077](https://pubmed.ncbi.nlm.nih.gov/35543077/)).

### Protective factors

**None reported.** No protective allele, dietary factor, or exposure has been described. By mechanistic inference (not evidence), **photoprotection** would be expected to limit UV-driven darkening superimposed on the constitutive hyperpigmentation, but I found no study testing this in FPHH — curate as inference in `notes`, not as an evidence-backed claim.

### Gene–environment interactions

**No published GxE data for FPHH.** Two mechanistically plausible but unevidenced axes worth recording as knowledge gaps:

1. **UV × KITLG-GOF.** SCF/KIT is a keratinocyte-derived paracrine arm of the UV tanning response; a constitutively hyperactive ligand could plausibly exaggerate UV-induced melanogenesis. Untested in FPHH.
2. **Somatic second hits.** Hida *et al.* provide the one hard example of a post-zygotic modifier of the phenotype — copy-neutral LOH at the *KITLG* locus confined to a hypopigmented macule (see §4, §6). That is a genetic–somatic interaction, not environmental.

---

## 3. Phenotypes

### Core cutaneous phenotype

| Phenotype | Type | Onset | Course | Frequency | Candidate HPO |
|---|---|---|---|---|---|
| Diffuse/blotchy hyperpigmentation | Physical manifestation | Birth or first weeks | Progressive, then plateaus | ~100% (definitional) | Hyperpigmentation of the skin (**HP:0000953**); Progressive hyperpigmentation (listed by GTR — *ID unverified*) |
| Hypopigmented macules ("ash-leaf", confetti) | Physical manifestation | Infancy | Progressive in number | Common but **not obligate** — the "with or without" in the disease name | Hypopigmented skin patches (**HP:0001053**, *verify*) |
| Café-au-lait macules | Physical manifestation | Birth to childhood | Increase in number | Frequent; "the most common skin problems present in FPHH patients" besides the dyspigmentation ([PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/)) | Café-au-lait spot (**HP:0000957**); Multiple café-au-lait spots (**HP:0007565**) |
| Lentigines | Physical manifestation | Childhood, "gradually appeared and increased in number" ([PMID:39152874](https://pubmed.ncbi.nlm.nih.gov/39152874/)) | Progressive | Frequent | Multiple lentigines (**HP:0001003**, *verify*) |
| Palmoplantar involvement | Physical manifestation | With disease | Static/progressive | Frequent ("frequently on the palms, soles and oral mucosa" — [PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/)) but **not universal** (spared in the family of [PMID:29186243](https://pubmed.ncbi.nlm.nih.gov/29186243/)) | Palmoplantar hyperpigmentation — *no confident HPO ID; check* |
| Oral mucosal / conjunctival pigmentation | Clinical sign | With disease | Progressive | Variable; prominent in some ([PMID:22577587](https://pubmed.ncbi.nlm.nih.gov/22577587/): tongue, palate, gingiva), absent in others | Abnormal oral mucosa morphology / oral pigmentation — *check* |
| Hypopigmented striae along Blaschko lines | Physical manifestation | Reported once | — | Rare (1 case) | Blaschko-linear hypopigmentation (a PanelApp phenotype label for *KITLG*) |
| Vitiligo | Physical manifestation | — | — | Rare — "Vitiligo was found in one family" ([PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/)); GTR lists it | Vitiligo (**HP:0001045**, *verify*) |
| Hyperkeratosis | Clinical sign | — | — | Rare; listed by GTR/HPO | Hyperkeratosis (**HP:0000962**) |
| Longitudinal melanonychia | Clinical sign | — | — | Rare (single case, both thumbs) | Melanonychia — *check* |

Quantitative anchors from individual families:

- Lesion size: "the patches (0.2–0.8 cm) progressed successively over her face, neck, trunk and limbs with age," plus "a small number of larger pigmented lesions that were several centimeters in diameter on her trunk and limbs" ([PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/)).
- Full-body extent in the index FPH family: "extensive hyperpigmentation of the conjunctive face, neck, trunk, limbs, lips, oral mucosa, palms, and soles" ([PMC2680999](https://pmc.ncbi.nlm.nih.gov/articles/PMC2680999/)).
- Morphologic range: "Dispigmentation patterns can range from well-isolated café-au-lait/hypopigmented patches on a background of normal-appearing skin to a confetti-like or mottled appearance" ([PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/)).

### Extracutaneous features — rare, family-specific, and contested

Two pedigrees carry non-cutaneous findings, and one large series explicitly did not:

- **Westerhof family (1978, [PMID:666331](https://pubmed.ncbi.nlm.nih.gov/666331/)):** 14 affected across 3 generations, Hindustani origin; "Some family members with macules also had retarded growth and mental deficiency." No male-to-male transmission observed. Pre-molecular; *KITLG* status unknown.
- **Chinese 2-year-old girl ([IJDVL variant case](https://ijdvl.com/familial-progressive-hypo-and-hyperpigmentation-a-variant-case/), cited as ref 11 in [PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/)):** "mild mental retardation and epilepsy," seizures exceeding 10 hours in the first year, "hyperthermia, frequently over 40 °C," repeated infections, longitudinal melanonychia, reticulate facial pigmentation.
- **Counterweight:** across the eight *KITLG*-mutation-positive FPHH families tabulated by Wang J *et al.*, "**mental retardation was not present in these FPHH patients**"; the recurring extra findings were "Sparse lateral eyebrows and malignancy (pharyngeal cancer, papillary thyroid cancer and melanoma) ... in two families" and "Short sutures ... in only one family" ([PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/)).

**Curation guidance:** treat neurodevelopmental features as *unconfirmed and probably not part of the KITLG-defined entity*. The two pedigrees reporting them are either pre-molecular or *KITLG*-untested, and the molecularly confirmed series contradicts them. Record as a `KNOWLEDGE_GAP` discussion rather than as a phenotype with a frequency.

**Malignancy:** the three cancers (pharyngeal, papillary thyroid, melanoma) in two families are the only cancer signal, are unreplicated, and are not established as disease-associated. Note that the index FPH family was explicitly cancer-free: "None of the affected members in this family was found to have skin cancer" ([PMC2680999](https://pmc.ncbi.nlm.nih.gov/articles/PMC2680999/)). Do **not** curate FPHH as a cancer-predisposition syndrome.

### Quality-of-life impact

**No FPHH-specific QoL instrument data exist** — no DLQI, EQ-5D, SF-36, or PROMIS study. What the literature supports: the burden is **cosmetic and psychosocial**, in a highly visible, congenital, progressive, whole-body distribution including the face. One case report is explicit that "The treatment is based solely on cosmetic purposes" ([PMID:22577587](https://pubmed.ncbi.nlm.nih.gov/22577587/)). There is no documented functional impairment, pain, pruritus, or organ dysfunction. Curate QoL as a knowledge gap with an inferred psychosocial-burden note.

---

## 4. Genetic / Molecular Information

### Gene

| Field | Value |
|---|---|
| Symbol | ***KITLG*** (KIT ligand; stem cell factor, SCF; mast cell growth factor, MGF; Steel factor) |
| HGNC | **hgnc:6343** (lowercase prefix per repo convention) |
| NCBI Gene | 4254 |
| Ensembl | ENSG00000049130 |
| UniProt | **P21583** |
| OMIM | \*184745 |
| Cytoband | **12q21.32** (older papers write 12q21 / 12q21.31-q23.1 / 12q21.12-q22 as linkage intervals) |
| RefSeq transcripts | **NM_000899** (variant b, 10 exons, includes exon 6 with the primary proteolytic cleavage site → soluble SCF) and **NM_003994** (variant a, 9 exons, exon 6 skipped → predominantly membrane-bound) |

**RefSeq accession caution.** FPHH papers cite `NM_000899.4` / `NM_000899.5` ([PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/), [PMID:41779177](https://pubmed.ncbi.nlm.nih.gov/41779177/)), but Vona *et al.* cite `NM_000889.4` ([PMID:35543077](https://pubmed.ncbi.nlm.nih.gov/35543077/)) — almost certainly a typographical error for NM_000899.4, since NM_000889 is *ITGB7*. Do not propagate the Vona accession into the entry.

### The variant landscape

All reported FPHH alleles are **heterozygous missense** substitutions in the **KIT-ligand (receptor-binding) domain**. There are no truncating, splice, or structural FPHH alleles — consistent with a gain-of-function mechanism where loss-of-function would give a different disease.

**Hotspot 1 — exon 2, the "VTNNV" motif, residues 33–37** (extended to **VTNNVK**, 33–38, by Huang *et al.*). This β-strand is the third β-strand of KITLG and is directly involved in receptor engagement.

| cDNA | Protein | Report | PMID |
|---|---|---|---|
| c.98T>C | p.Val33Ala | Amyere 2011 (FPHH family) | [21368769](https://pubmed.ncbi.nlm.nih.gov/21368769/) |
| c.100A>C | p.Thr34Pro | Amyere 2011 (separate FPHH family) | [21368769](https://pubmed.ncbi.nlm.nih.gov/21368769/) |
| c.101C>T | p.Thr34Ile | recurrent; sporadic Chinese case | [33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/) |
| c.104A>T | p.Asn35Ile | novel, Chinese family 1 (4 generations, 7 affected) | [33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/) |
| c.105T>A | p.Asn35Lys | novel, Chinese pedigree, co-segregating | [36453959](https://pubmed.ncbi.nlm.nih.gov/36453959/) |
| **c.107A>G** | **p.Asn36Ser** | the index FPH allele (6-generation Chinese family, LOD 4.35 at D12S81); **recurrent** — also found in 2 of the 7 Amyere FPHH families | [19375057](https://pubmed.ncbi.nlm.nih.gov/19375057/), [21368769](https://pubmed.ncbi.nlm.nih.gov/21368769/) |
| — | p.Val37 (residue implicated; specific substitution not stated in accessible text) | tabulated by Wang J 2021 | [33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/) |
| c.113A>C | p.Lys38Thr | **de novo**, sporadic 15-year-old Han Chinese boy; extends hotspot to VTNNVK | [39152874](https://pubmed.ncbi.nlm.nih.gov/39152874/) |

**Hotspot 2 — exon 4, the ligand core / third α-helix.** Fewer alleles, and phenotypically indistinguishable so far.

| cDNA | Protein | Report | PMID |
|---|---|---|---|
| c.329A>T | p.Asp110Val | **de novo**, Slovenian patient; 3rd α-helix | [34716665](https://pubmed.ncbi.nlm.nih.gov/34716665/) |
| c.329A>G | p.Asp110Gly | **de novo**; also previously reported as a **post-zygotic mosaic** variant in a 6-year-old boy with congenital linear and mottled hyperpigmentation | [41779177](https://pubmed.ncbi.nlm.nih.gov/41779177/); mosaic case cited in [33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/) |
| c.337G>A | p.Glu113Lys | novel; "located within another ligand-receptor interaction site" | [32189379](https://pubmed.ncbi.nlm.nih.gov/32189379/) |

**Other:** p.Ser78Leu — novel, in the Blaschko-linear case ([PMID:39269165](https://pubmed.ncbi.nlm.nih.gov/39269165/); cDNA position not given in the abstract — **do not invent one**).

> "Notably, seven known mutations were clustered in a highly conserved short amino acid sequence VTNNV (amino acids 33–37) ... The VTNNV domain of the KITLG protein (amino acids 33–37) lies within the third b-strand of the protein and is responsible for its binding functions." — [PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/)

**Count discrepancy to flag:** Wang J *et al.* (2021) state eight FPHH alleles; Huang *et al.* (2024/2026) state "only 10 KITLG mutations reported to cause FPHH" while also writing "seven in nine" are in exon 2. Report the count as *approximately 10–12 as of 2026* rather than adopting either figure as exact.

### Variant classification and population frequency

- ACMG/AMP evidence applied to c.104A>T and c.101C>T: **PS4** (prevalence in affected vs controls), **PM1** (mutational hotspot), **PP2**, **PP3**; both classified **likely pathogenic** ([PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/)).
- p.Lys38Thr: MutationTaster "disease causing"; "**absent in the public databases such as ExAC, dbSNP, and gnomAD**"; classified **likely pathogenic** ([PMID:39152874](https://pubmed.ncbi.nlm.nih.gov/39152874/)).
- p.Asn36Ser: segregated with disease and "was not detected in 296 healthy unrelated Chinese individuals"; ClinVar RCV000013661 / VCV000379240.
- Wang J *et al.* additionally sequenced "100 unrelated normal Chinese Han individuals ... to exclude polymorphic variants" — variants absent.

**Population frequency: effectively zero.** All FPHH alleles are absent or ultra-rare in gnomAD/ExAC/1000 Genomes. I did not retrieve *KITLG* gene-level constraint metrics (pLI/LOEUF/missense-Z) from gnomAD; a curator wanting them should query gnomAD directly rather than rely on any figure here.

### Origin: germline, de novo, and somatic

- **Germline, inherited:** the majority — multigenerational pedigrees with clean co-segregation.
- **De novo:** at least three independent cases (p.Lys38Thr, p.Asp110Val, p.Asp110Gly), all confirmed absent in both parents. Sporadic presentation is therefore common enough that a negative family history should not deter testing.
- **Somatic mosaicism:** a de novo mosaic c.329A>G (p.Asp110Gly) produced "congenital linear and mottled hyperpigmentation" in a 6-year-old boy — i.e. **a Blaschko-linear mosaic form of the same allele** (cited in [PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/)).
- **Somatic reversion (the most mechanistically interesting finding in this disease):**

> "Digital polymerase chain reaction analysis of the DNA from skin and blood tissues indicated a copy-neutral loss of heterozygosity at the KITLG locus, only in the hypopigmented macule. These findings suggest that the hypopigmented macules might result from revertant mosaicism." — Hida *et al.* 2025, *J Dermatol* ([PMID:39269165](https://pubmed.ncbi.nlm.nih.gov/39269165/))

### Functional consequence

**Gain of function**, established biochemically for p.Asn36Ser and inferred structurally for the rest:

> "Function analysis of the soluble form of sKITLG revealed that mutant sKITLG N36S increased the content of the melanin by 109% compared with the wild-type sKITLG in human A375 melanoma cells. Consistent with this result, the tyrosinase activity was significantly increased by mutant sKITLG N36S compared to wild-type control." — [PMID:19375057](https://pubmed.ncbi.nlm.nih.gov/19375057/)

Absolute values from the full text: "melanin content increased from 16.2 pg per cell (WT sKITLG) to 33.9 pg per cell (mutant sKITLG N36S)"; n=6, two-sided Student's *t* test ([PMC2680999](https://pmc.ncbi.nlm.nih.gov/articles/PMC2680999/)).

Structural rationale for the VTNNV alleles: "Both 35Asn and 34Thr are polar, hydrophilic amino acids, and the mutant became nonpolar, hydrophobic isoleucine; therefore, it might change the features of the protein and affect the ligand affinity to its receptor c-Kit" ([PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/)). Note the authors' own hedge: "definitive functional analyses of this mutation are needed."

**Important schema note for dismech:** per CLAUDE.md's gain/loss decision tree, the variant-level claim belongs in `GeneticContext.functional_impact_category: GAIN_OF_FUNCTION`; the pathway-activity claim ("melanogenesis driven outside normal keratinocyte-paracrine control") belongs in `Descriptor.modifier`. Because the KITLG→KIT signal here is genuinely released from its normal regulatory setpoint by a constitutively higher-affinity ligand — not merely running hot — `modifier: GAIN_OF_FUNCTION` on the KIT-signalling node is defensible; `INCREASED` on downstream melanin-biosynthesis nodes is the safer, PATO-bound choice. This entry is a legitimate candidate to be the **first** in the KB to carry both slots on one mutation-driven node.

### Allelic disorders (same gene, different mechanism/dose) — essential context

| Disorder | OMIM | Inheritance | Mechanism |
|---|---|---|---|
| **FPHH** | 145250 | AD | Heterozygous **GOF** missense, KIT-ligand domain |
| **DFNA69** — nonsyndromic deafness 69, congenital unilateral/asymmetric | 616697 | AD | Heterozygous, e.g. p.Ser96Ter, p.His67_Cys68delinsArg, p.Leu104Val |
| **Waardenburg syndrome type 2F** | 619947 | **AR** | Biallelic; e.g. homozygous c.94C>T p.Arg32Cys |
| Biallelic hypomelanosis + SNHL | — | **AR** | Biallelic LOF → generalized hypomelanosis; residual function → WS2/piebaldism-like |
| Skin/hair/eye pigmentation variation 7 (SHEP7) | 611664 | complex | Common regulatory variation |
| Testicular germ cell tumour susceptibility | 273300 | complex | rs995030 etc., OR ≈ 2.4–2.6 per risk allele |

Vona *et al.*'s dose model is the cleanest statement of the allelic architecture:

> "We speculate that KITLG biallelic loss-of-function variants cause generalized hypomelanosis, whilst variants with residual function lead to a variable auditory-pigmentary disorder mostly reminiscent of Waardenburg syndrome type 2 or piebaldism." — [PMID:35543077](https://pubmed.ncbi.nlm.nih.gov/35543077/)

Note also that **heterozygous carriers of a *KITLG* null "exhibited lighter-coloured skin than expected for their ethnic background"** ([PMID:35543077](https://pubmed.ncbi.nlm.nih.gov/35543077/)) — a direct human dose–response readout on the opposite side of wild-type from FPHH. Together, FPHH (hypermorph) and the null carriers (hypomorph) bracket *KITLG* as a **continuously dose-sensitive determinant of human skin pigmentation**. That is the single strongest mechanistic framing for this entry.

Interesting corollary from Huang *et al.*: the receptor mirrors the ligand — "Mutations in KIT, encoding for the receptor of KITLG, could lead to piebaldism (loss of function in KIT) or skin hyperpigmentation (gain of function in KIT)."

### Modifier genes, epigenetics, chromosomal abnormalities

- **Modifier genes: none identified.** Variable expressivity is unexplained.
- **Epigenetics: no DNA-methylation, histone, or chromatin data exist for FPHH.** The one 2026 study found transcriptional consequences (MITF) but did not assay epigenome.
- **Chromosomal abnormalities: none.** FPHH is not a CNV/microdeletion disorder; CMA and karyotype are not indicated (§10). The only large-scale genomic event described is the **copy-neutral LOH confined to a hypopigmented macule** ([PMID:39269165](https://pubmed.ncbi.nlm.nih.gov/39269165/)) — a somatic, lesion-restricted event, not a constitutional one.

---

## 5. Environmental Information

**Not applicable in any causal sense.** There are no environmental factors, lifestyle factors, or infectious agents implicated in FPHH. It is fully penetrant-or-not on genotype, congenital in onset, and has no exposure-linked triggers in any published pedigree.

For the `environmental:` block, the honest curation is **either an empty section with a knowledge-gap discussion, or a `review_notes:` waiver** beginning `Left deliberately uncited.` followed by ≥20 words describing the searches run (PubMed FPHH × exposure; CTD *KITLG*; ECTO term search for UV/solar radiation exposure) and why nothing citable was found. Do not manufacture a UV-exposure link — it is mechanistically plausible for the tanning arm of KIT signalling but has never been tested in FPHH, and asserting it would fail `check-environmental-evidence` on substance even if it passed on form.

---

## 6. Mechanism / Pathophysiology

### The causal chain

**Step 1 — Mutant ligand (MOLECULAR).** A heterozygous missense substitution in the KIT-ligand domain of KITLG — overwhelmingly in the VTNNVK β-strand (residues 33–38), occasionally in the exon-4 α-helical core (Asp110, Glu113) — alters the receptor-contact surface. Predicted consequence: **increased affinity of KITLG for KIT**, i.e. a hypermorphic ligand rather than more ligand.

- GO: `GO:0005173` stem cell factor receptor binding (*verify label*); `GO:0005125` cytokine activity
- Descriptor: `modifier: GAIN_OF_FUNCTION`; `functional_impact_category: GAIN_OF_FUNCTION`

**Step 2 — Paracrine over-stimulation of melanocyte KIT (CELLULAR).** KITLG is made by the melanocyte's neighbours, not by the melanocyte:

> "KITLG, as KIT LIGAND, is produced locally in human skin by epidermal keratinocytes and endothelial cells, where it induces the migration, development and survival of melanocytes." — [PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/)

> "After KITLG binds the c-KIT receptor, dimerization is triggered. It initiates signal transduction via the RAS/MAPK pathway to upregulate melanoblast proliferation" — [PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/)

This is a **keratinocyte→melanocyte paracrine axis**, which makes FPHH a disease of the melanocyte's *niche signal*, not of the melanocyte's own genome. Cell types: keratinocyte (`CL:0000312`) and blood-vessel endothelial cell (`CL:0000071`) as sources; melanocyte (`CL:0000148`) and melanoblast (`CL:0000541`) as targets.

- GO: `GO:0038109` Kit signaling pathway (*verify*); `GO:0004714` transmembrane receptor protein tyrosine kinase activity; `GO:0007169` cell-surface receptor protein tyrosine kinase signaling pathway

**Step 3 — Downstream cascades (CELLULAR).** KIT activation feeds **RAS–RAF–MAPK**, **PI3K–AKT**, **JAK–STAT**, and **PLCγ1** ([GeneCards/UniProt P21583](https://www.genecards.org/cgi-bin/carddisp.pl?gene=KITLG)). The FPHH literature emphasizes RAS/MAPK: "KITLG/c-Kit and Ras/MAPK pathways are crucial for controlling pigmentation" ([PMID:35543077](https://pubmed.ncbi.nlm.nih.gov/35543077/)).

- GO: `GO:0000165` MAPK cascade; `GO:0014065` phosphatidylinositol 3-kinase signaling

**Step 4 — MITF induction (MOLECULAR).** MITF is the master melanocyte transcription factor and the convergence point. The 2026 functional study is the first to show transcriptome-wide consequences:

> "results showed that the mutation broadly affected the transcription and translation of genes responsible for melanin synthesis, especially the melanin gene MITF." — Wu *et al.* 2026, *Mol Genet Genomics* ([PMID:41779177](https://pubmed.ncbi.nlm.nih.gov/41779177/))

**Step 5 — Tyrosinase up-regulation and increased melanogenesis (CELLULAR).** Directly measured: tyrosinase activity and melanin content both rise (§4). Tyrosinase is the rate-limiting enzyme converting L-tyrosine → DOPA → dopaquinone → melanin.

- GO: `GO:0042438` melanin biosynthetic process; `GO:0004503` monophenol monooxygenase (tyrosinase) activity; `GO:0042470` melanosome (CC)
- CHEBI: L-tyrosine (`CHEBI:17895`, *verify*); melanin/eumelanin — *no confident CHEBI ID; check before binding*

**Step 6 — Melanin transfer and epidermal deposition (TISSUE).** Melanosomes are transferred to basal keratinocytes; histology shows melanin accumulation "throughout the epidermis, especially in the basal cell layer" ([PMID:29186243](https://pubmed.ncbi.nlm.nih.gov/29186243/)).

- UBERON: skin of body (`UBERON:0002097`); epidermis (`UBERON:0001003`); stratum basale — *verify ID*

**Step 7 — Clinical hyperpigmentation, progressive with age (ORGANISM).**

### The unexplained half: why hypopigmentation?

This is the entry's headline knowledge gap, stated plainly by the field:

> "Disturbances in the KITLG-KIT interaction result in diffuse hyperpigmentation in FPHH. **However, the mechanisms behind hypopigmented macule formation remain unclear.**" — Hida *et al.* ([PMID:39269165](https://pubmed.ncbi.nlm.nih.gov/39269165/))

Two competing/complementary hypotheses, both worth curating as `mechanistic_hypotheses` with distinct `hypothesis_group_id`s:

**Hypothesis A — revertant somatic mosaicism (EMERGING, one case).** Copy-neutral LOH at the *KITLG* locus removes the mutant allele in a clone of skin, producing a wild-type (hence relatively hypopigmented) patch on a hyperpigmented background. Supported by: LOH detected by digital PCR "only in the hypopigmented macule," and the lesions following **Blaschko lines** — the signature of clonal cutaneous mosaicism. Note Amyere *et al.* also flagged "Loss of Heterozygosity" and "Gene Dosage" as MeSH keywords back in 2011 ([PMID:21368769](https://pubmed.ncbi.nlm.nih.gov/21368769/)), so the idea has a longer pedigree than the single 2025 report.

**Hypothesis B — distinct pathogenesis for CALMs.** From the same paper: "café-au-lait spots do not follow the lines of Blaschko and can superimpose on the hypopigmented striae, indicating a distinct pathogenesis." So FPHH skin plausibly carries **three superimposed lesion classes with three mechanisms**: constitutive diffuse hyperpigmentation (germline GOF), clonal hypopigmented reversion (somatic LOH), and CALMs (mechanism unknown).

**Hypothesis C — melanocyte exhaustion/depletion (speculative).** Chronic supraphysiological KIT stimulation could plausibly deplete the melanocyte stem-cell pool in patches. **No direct evidence.** The histology is at least consistent with *absence* of functioning melanocytes in hypopigmented skin (S100/HMB45 "almost completely negative"), but that cannot distinguish reversion from depletion.

### Histopathology — with an explicit conflict to resolve

**Hyperpigmented skin:**
> "Histopathological and immunohistochemical staining for S100 and HMB45 of skin biopsy specimens from the hyperpigmented areas showed a striking increase in melanin throughout the epidermis, especially in the basal cell layer." — [PMID:29186243](https://pubmed.ncbi.nlm.nih.gov/29186243/)

> "strong basilar and suprabasilar hyperpigmentation ... Masson-Fontana stained sections showed an increase in the number of melanocytes in the basal and suprabasal cell layers." — [PMID:22577587](https://pubmed.ncbi.nlm.nih.gov/22577587/)

**Hypopigmented skin:**
> "The staining for S100 and HMB45 were almost completely negative in the hypopigmentation areas." — [PMID:29186243](https://pubmed.ncbi.nlm.nih.gov/29186243/) — i.e. **melanocytes are absent, not merely underproductive**, which favours Hypothesis A or C over a pure "less melanin per cell" model.

**⚠ Conflict — do not paper over this.** Wang ZQ *et al.* 2009 contains an internal contradiction. Its figure caption reports the authors' own biopsy as showing "a significant increase of the number of melanocytes and of the melanin content in the basal keratinocytes, as well as a slight increase in the size of melanocytes," while the main text, citing prior FPH literature, states biopsies showed "increased melanin in the basal layer, **but no increase in the number of melanocytes** within the epidermis" ([PMC2680999](https://pmc.ncbi.nlm.nih.gov/articles/PMC2680999/)). Whether FPHH hyperpigmentation is **melanocyte hyperplasia** or **per-melanocyte hyperfunction** is therefore genuinely unsettled — and it matters, because KIT signalling drives *both* proliferation and melanogenesis. Curate as two evidence items with different `supports` values, or as a `KNOWLEDGE_GAP` discussion attached to the melanogenesis node. **Do not assert either as fact.**

### Other mechanism domains

- **Protein dysfunction:** altered receptor-binding surface, not misfolding or aggregation. SWISS-MODEL 3D modelling shows side-chain changes at Thr34/Asn35 converting polar/hydrophilic to nonpolar/hydrophobic residues ([PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/)). No crystal structure of a mutant KITLG–KIT complex has been solved; PDB structures of wild-type SCF/KIT exist and would be the substrate for such work.
- **Isoform biology (under-explored, likely important):** exon 6 encodes the primary proteolytic cleavage site; NM_000899 (variant b) yields **soluble SCF**, NM_003994 (variant a) yields **membrane-bound SCF**. "The soluble form mainly stimulates cellular proliferation; the membrane-bound isoform induces an activation of the receptor more prolonged than the soluble one." Every functional FPHH experiment to date used the **soluble** form (sKITLG). Whether FPHH alleles differentially affect the two isoforms is unknown and is a good `Experiment` proposal.
- **Metabolic changes:** confined to melanin/tyrosine metabolism. No systemic metabolic derangement; "Hematology and blood chemistry did not reveal any abnormalities" ([PMID:22577587](https://pubmed.ncbi.nlm.nih.gov/22577587/)).
- **Immune involvement:** none for FPHH. (KITLG is central to **mast cell** development, `CL:0000097`, but no mast-cell phenotype has been reported in FPHH patients — a notable negative worth recording.)
- **Tissue damage mechanisms:** **none.** FPHH involves no oxidative injury, ischaemia, fibrosis, inflammation, or necrosis. The tissue is structurally normal and abnormally pigmented. This is a *dysregulation* disease, not a *destruction* disease — relevant when deciding module conformance (it conforms to **no** fibrotic/inflammatory/degenerative module in `kb/modules/`).
- **Molecular profiling:** transcriptomics only — the 2026 RNA-seq of adenine-base-editor–engineered cells ([PMID:41779177](https://pubmed.ncbi.nlm.nih.gov/41779177/)). **No proteomics, metabolomics, lipidomics, single-cell, spatial, multi-omics, or CRISPR-screen data specific to FPHH.** No GEO series exists for FPHH; do not fabricate a `datasets:` accession — `just discover-datasets` will surface *KITLG*-adjacent melanocyte studies that are **GENE_ONLY** at best and require the manual relevance triage CLAUDE.md warns about.

---

## 7. Anatomical Structures Affected

**Organ level**
- **Primary:** skin (`UBERON:0002097`) — the only consistently affected organ. Integumentary system.
- **Secondary:** oral mucosa (`UBERON:0000344`, *verify*), lips, conjunctiva (`UBERON:0001811`, *verify*) — pigmented in some patients, spared in others.
- **No** cardiovascular, neurological, digestive, respiratory, endocrine, renal, or skeletal involvement in molecularly confirmed FPHH.
- **Allelic-disorder context only:** the **stria vascularis** of the cochlea (`UBERON:0002499`, *verify*) is the site of the *KITLG* hearing phenotype (DFNA69/WS2F), via intermediate cells = cochlear melanocytes. Do not attribute hearing loss to FPHH itself.

**Regional distribution:** face, neck, trunk, limbs; frequently palms and soles; occasionally sparing them. Distribution is **bilateral and broadly symmetric/generalized** for the diffuse hyperpigmentation, but the superimposed macules are **random and asymmetric**, and the reverted hypopigmented lesions follow **Blaschko lines** (mosaic, not anatomically symmetric).

**Tissue level:** stratified squamous epithelium of the epidermis (`UBERON:0001003`); specifically the **basal and suprabasal layers**. Dermis is uninvolved except as the source of endothelial KITLG.

**Cell level**
| Cell type | CL (verify) | Role |
|---|---|---|
| Melanocyte | `CL:0000148` | Primary effector — hyperfunctional and/or hyperplastic |
| Melanoblast | `CL:0000541` | Developmental target of KIT signalling |
| Keratinocyte | `CL:0000312` | Ligand source (paracrine) and melanin recipient |
| Basal cell of epidermis | *check* | Site of melanin accumulation |
| Blood-vessel endothelial cell | `CL:0000071` | Second dermal ligand source |
| Mast cell | `CL:0000097` | KIT-dependent lineage; no reported FPHH phenotype (negative finding) |

**Subcellular level:** melanosome (`GO:0042470`) — melanin synthesis and transfer; plasma membrane (`GO:0005886`) — KIT receptor and membrane-bound KITLG; extracellular space (`GO:0005615`) — soluble sKITLG.

---

## 8. Temporal Development

**Onset:** **congenital to early infantile.** Multiple independent formulations:
- "Generalized hyper- and hypopigmentation with irregular patches was found at birth" ([PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/))
- "One week after birth, it was shown that her diffuse hyperpigmented skin was intermixed with some small lentigines/CAL-like lesions" ([PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/))
- "present at birth or develop early in infancy" (OMIM #145250 description)
- "The pigmentation was present since birth and eventually increased thereafter" ([PMID:22577587](https://pubmed.ncbi.nlm.nih.gov/22577587/))
- HPO onset category: **Congenital onset** / **Neonatal onset** (`HP:0003577` / `HP:0003623`, *verify*)

**Onset pattern:** insidious and chronic — never acute, never episodic.

**Progression — this is the defining temporal signature and has a documented biphasic rate:**

> "This process was rapid during childhood and slower during adolescence, and it resulted in extensive hyperpigmentation of the conjunctive face, neck, trunk, limbs, lips, oral mucosa, palms, and soles." — [PMC2680999](https://pmc.ncbi.nlm.nih.gov/articles/PMC2680999/)

> "With increasing age, the lesions increased in both size and number and became more noticeable" — [PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/)

Progression is by **three simultaneous axes**: individual patches *enlarge*, new patches *appear*, and adjacent patches *become confluent* ("increase in size, number and confluence with age" — Orphanet phrasing for the FPH concept).

**Suggested `progression:` phases for the entry:**
| Phase | Timing | Description |
|---|---|---|
| Congenital/neonatal | Birth to ~1 month | Diffuse hyperpigmentation ± large CALM-like patches present or emerging |
| Rapid childhood progression | Infancy → ~puberty | Fastest accrual of new lentigines, CALMs, hypopigmented macules; patch enlargement |
| Adolescent deceleration | Puberty → early adulthood | Same process, slower rate |
| Adult stable/extensive | Adulthood | Extensive, largely stable involvement; a 53-year-old affected male showed no new disease category, and no skin cancer |

**Disease course:** **chronic, lifelong, progressive, non-remitting.** No spontaneous remission reported. No relapsing-remitting behaviour. Not self-limited. Life expectancy is unaffected (§11).

**Remission:** none spontaneous. The only documented *local* lightening is the somatic-reversion mechanism producing hypopigmented macules ([PMID:39269165](https://pubmed.ncbi.nlm.nih.gov/39269165/)) — which is a lesion-level genetic event, not clinical remission. Treatment-induced lightening is cosmetic and, by analogy to other benign pigmented lesions, expected to be temporary (§12).

**Critical periods:** infancy and childhood are the window of maximal lesion accrual, which is when a purely mechanistic argument for early intervention would apply — but **no intervention exists to test that**, so this is an inference, not a recommendation.

---

## 9. Inheritance and Population

### Epidemiology

**No prevalence or incidence estimate exists in the literature**, and the field says so explicitly:

> "Because FPHH is very rare with reduced penetrance, no clear incidence rate of this disease has been documented." — [PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/)

For the `prevalence:` block, the correct structured record is:

```yaml
prevalence:
- population: Worldwide
  measure_type: UNKNOWN
  prevalence_class: ULTRA_RARE        # or NOT_YET_DOCUMENTED
  notes: >-
    No incidence or prevalence estimate has been published. Fewer than ~25 molecularly
    confirmed families are reported worldwide as of 2026.
```

Do **not** compute a `rate_per_100000`. A defensible order-of-magnitude anchor for `notes`: roughly 10–12 distinct *KITLG* alleles across on the order of 15–20 published families/probands, plus an unknown number of *KITLG*-negative families — i.e. well under 1 per 1,000,000. Consider fetching `ORPHA:280628` for an Orphanet-assigned prevalence class, which would be quotable.

### Inheritance

- **Autosomal dominant** (`HP:0000006`), consistently across all *KITLG*-positive pedigrees. Six-generation ([PMID:19375057](https://pubmed.ncbi.nlm.nih.gov/19375057/)) and four-generation ([PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/)) pedigrees with clean co-segregation.
- **Penetrance: incomplete/reduced.** "FPHH is thought to be an autosomal dominant disorder **with reduced penetrance**" ([PMID:21368769](https://pubmed.ncbi.nlm.nih.gov/21368769/)); "a rare autosomal dominant disorder **with variable penetrance**" ([PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/)). **No numeric penetrance estimate is available.** Note also that the Wang 2009 family showed *perfect* co-segregation ("cosegregated perfectly with affected, but not with unaffected, members"), so penetrance may be allele-dependent.
- **Expressivity: variable** — extent of hyperpigmentation, presence/absence of the hypopigmented component, CALM burden, and mucosal involvement all differ within and between families. Huang *et al.* raise the possibility of allele-specific severity: "Further cases of FPHH caused by the same mutation are warranted to elucidate if the extensive involvement is mutation related."
- **Genotype–phenotype correlation: none established.** "no clear genotype-phenotype correlations have been established" ([PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/)). Exon-2 VTNNVK and exon-4 core alleles are not clinically distinguishable in current data.
- **Genetic anticipation:** not reported and not expected (missense, not repeat expansion).
- **De novo rate:** unquantified but clearly non-trivial — ≥3 confirmed de novo probands out of a small published total.
- **Germline mosaicism:** not reported for FPHH. **Somatic** mosaicism is documented (the mosaic p.Asp110Gly linear-hyperpigmentation case). Recurrence counselling should nevertheless mention germline mosaicism as a theoretical residual risk for apparently de novo cases.
- **Founder effects:** none identified. Recurrent alleles (p.Asn36Ser in a Chinese FPH family *and* two European FPHH families; p.Thr34Ile) are best explained by **hotspot recurrence**, not shared ancestry — and the trans-continental recurrence of p.Asn36Ser argues directly against a founder.
- **Consanguinity:** not a factor for FPHH; relevant only to the recessive *KITLG* disorders.
- **Carrier frequency:** not applicable (dominant); "carriers" are affected.

### Population demographics

- **Reported ancestries:** Han Chinese (most reports), Japanese, Slovenian, Danish, German, US, Hindustani-origin, Filipino (for the allelic WS2F allele). The Chinese predominance is best read as ascertainment bias — the disease is visually striking, and several large Chinese dermatogenetics groups have driven the field.
- **Geographic distribution of variants:** exon-2 VTNNVK alleles reported from both East Asia and Europe; exon-4 alleles from Slovenia (p.Asp110Val), Japan (p.Glu113Lys), and China (p.Asp110Gly). No geographic clustering by allele.
- **Sex ratio:** ~1:1; no sex-limited expression, no skewing. No male-to-male transmission was observed in the Westerhof family, but this is a small-pedigree artefact — male-to-male transmission is present in later pedigrees, excluding X-linkage.
- **Age distribution of affected individuals:** all ages; the disease is present from birth and persists lifelong. Published patients range from a 2-year-old to a 53-year-old.

---

## 10. Diagnostics

### Diagnostic approach in one line

FPHH is a **clinical diagnosis confirmed by *KITLG* sequencing**, made in an infant or child with congenital diffuse hyperpigmentation plus dyspigmented macules, after NF1/Legius and the dyschromatoses have been considered.

### Genetic testing — the definitive test

| Modality | Utility for FPHH |
|---|---|
| **Single-gene *KITLG* sequencing** | **First-line and usually sufficient.** All coding exons + flanking intronic sequence, Sanger or NGS. Exons 2 and 4 carry every reported allele. Method as used by [PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/): "All exons and their flanking intronic sequences of the KITLG gene were amplified by polymerase chain reaction ... sequenced directly using an ABI Prism 3730" |
| **Targeted gene panel** | Strongly indicated when the differential is broad. *KITLG* is **Green** on Genomics England PanelApp "Pigmentary skin disorders" (panel 559), monoallelic. A dyschromatosis/pigmentary panel should also carry *ABCB6*, *SASH1*, *NF1*, *SPRED1*, *PTPN11*, *TSC1/TSC2*, *KIT*, *MITF*, *SOX10*, *PAX3*, *STK11* |
| **WES** | Used successfully for de novo/sporadic cases ([PMID:39152874](https://pubmed.ncbi.nlm.nih.gov/39152874/), [PMID:41779177](https://pubmed.ncbi.nlm.nih.gov/41779177/), [PMID:36453959](https://pubmed.ncbi.nlm.nih.gov/36453959/)). Valuable because it simultaneously excludes *NF1*/*SPRED1*: "no suspected disease-causing variants in NF1 or SPRED1 leading to similar manifestations were identified in the whole-exome sequencing" |
| **WGS** | No specific added value demonstrated; reasonable for *KITLG*-negative families where a novel locus is suspected |
| **Trio testing** | Important — establishes de novo status and informs recurrence risk |
| **Lesional (skin) DNA testing** | **Under-used and mechanistically important.** Digital PCR on DNA from *individual lesions* detected copy-neutral LOH present only in the hypopigmented macule ([PMID:39269165](https://pubmed.ncbi.nlm.nih.gov/39269165/)). Blood-only testing will miss both mosaic causal alleles and revertant clones |
| CMA / karyotype / FISH | **Not indicated.** No CNV or cytogenetic mechanism |
| mtDNA testing | Not indicated |
| Repeat expansion testing | Not indicated |

**Variant interpretation:** apply ACMG/AMP. Documented codes for FPHH alleles: **PS4, PM1** (VTNNVK hotspot), **PP1/PP2** (co-segregation), **PP3** (in-silico: SIFT "deleterious", PolyPhen-2 "possibly damaging", MutationTaster "disease causing"), **PM2** (absent from gnomAD/ExAC/dbSNP). Typical resulting classification: **likely pathogenic**.

### Clinical/laboratory tests

- **Routine labs are normal and serve to exclude mimics, not to diagnose.** A full endocrine screen in one case — "estimation of serum ACTH, α and β MSH, T3 T4 TSH, and Cortisol levels" — was normal ([PMID:22577587](https://pubmed.ncbi.nlm.nih.gov/22577587/)). This is the standard workup to exclude Addison disease and ACTH/MSH-driven hyperpigmentation.
- **Biomarkers: none.** No circulating, imaging, or molecular biomarker for FPHH.
- **Imaging: not indicated** for FPHH itself. (Indicated only if NF1 remains in the differential.)
- **Wood's lamp examination:** useful clinically to delineate hypopigmented/ash-leaf macules — standard pigmentary-disorder practice, no FPHH-specific citation.
- **Dermoscopy:** no published FPHH-specific dermoscopic criteria.
- **Audiology:** **worth considering**, not because FPHH causes deafness but because *KITLG* alleles can, and the DFNA69 phenotype is *unilateral or asymmetric* and therefore easily missed. Frame as prudent given the gene, and cite the allelic literature ([PMID:35543077](https://pubmed.ncbi.nlm.nih.gov/35543077/)), never as an FPHH feature.

### Biopsy / histopathology

Supportive, not diagnostic. Findings (§6): increased melanin throughout the epidermis, maximal in the basal layer; Masson–Fontana positive; S100 and HMB45 highlight melanocytes in hyperpigmented skin and are "almost completely negative" in hypopigmented areas. Melanocyte *number* is disputed. No pigmentary incontinence or interface change is characteristic — their presence should redirect to post-inflammatory dyspigmentation or DUH.

### Diagnostic criteria and differential diagnosis

**There are no formal, society-published diagnostic criteria for FPHH.** Diagnosis rests on the clinical triad (congenital/early-infantile onset + diffuse progressive hyperpigmentation + superimposed CALMs/lentigines/hypopigmented macules) + AD family history (when present) + *KITLG* variant.

| Differential | How to distinguish |
|---|---|
| **Neurofibromatosis type 1** | CALMs + axillary/inguinal freckling, but **no diffuse background hyperpigmentation**; Lisch nodules, neurofibromas, optic glioma; *NF1* variant |
| **Legius syndrome** | "characterized by familial café-au-lait spots and skin fold freckling, caused by mutations in SPRED1" ([PMID:21368769](https://pubmed.ncbi.nlm.nih.gov/21368769/)); no diffuse hyperpigmentation |
| **Dyschromatosis universalis hereditaria (DUH1/2/3)** | Hyper- **and** hypopigmented macules but on **normal-appearing background skin**, not diffuse hyperpigmentation; reticulate; *ABCB6* (DUH3) / *SASH1*. **DUH2 maps to 12q21–q23 — overlapping the FPHH locus**, and Amyere *et al.* suggest *KITLG* may underlie DUH2 too ("mutations in a single gene cause various pigmentation disorders: FPH, FPHH, and likely DUH2") |
| **LEOPARD / Noonan with multiple lentigines** | Lentigines + cardiac, growth, genital, deafness features; *PTPN11* |
| **Tuberous sclerosis complex** | Ash-leaf macules **without** diffuse hyperpigmentation; angiofibromas, shagreen patch, seizures, tubers |
| **Peutz–Jeghers syndrome** | Perioral/mucosal lentigines, GI polyposis; *STK11* |
| **Piebaldism / Waardenburg** | Congenital **stable** leukoderma with white forelock; loss-of-function *KIT*/*KITLG*/*MITF*/*PAX3*/*SOX10* — the mechanistic mirror image |
| **Addison disease / Cushing / ACTH-driven** | Acquired, mucosal + palmar-crease accentuation, abnormal endocrine labs |
| **Carbon baby syndrome (universal acquired melanosis)** | Acquired diffuse darkening, non-familial |
| **Haemochromatosis, drug-induced (incl. imatinib), heavy metals, smoker's melanosis** | Acquired, exposure history, distinctive labs |
| **Naegeli–Franceschetti–Jadassohn / dermatopathia pigmentosa reticularis** | Reticulate pigmentation **with** nail/dental/sweating abnormalities; *KRT14* |

Sources for the differential list: [PMID:22577587](https://pubmed.ncbi.nlm.nih.gov/22577587/), [PMID:39152874](https://pubmed.ncbi.nlm.nih.gov/39152874/), [PMID:21368769](https://pubmed.ncbi.nlm.nih.gov/21368769/), [IJDVL variant case](https://ijdvl.com/familial-progressive-hypo-and-hyperpigmentation-a-variant-case/), and the DUH literature ([PMID:37353900](https://pubmed.ncbi.nlm.nih.gov/37353900/)).

### Screening

- **Newborn screening: no.** Not screenable, not treatable, no biochemical marker.
- **Carrier screening: not applicable** (dominant).
- **Cascade testing: yes, appropriate** — targeted *KITLG* variant testing of at-risk relatives once a familial variant is known, remembering reduced penetrance.
- **Prenatal / PGT: technically feasible** once the familial variant is known. Whether it is *offered* is a values question for a non-lethal, non-progressive-beyond-skin cosmetic condition; that judgement belongs to the family and their genetic counsellor, not to this report.

---

## 11. Outcome / Prognosis

**Survival and mortality: normal.** No FPHH-attributable mortality has ever been reported. No excess mortality, no reduction in life expectancy, no disease-specific mortality rate. Affected individuals survive into at least the sixth decade with no systemic disease (a 53-year-old affected male is described in the index family, [PMC2680999](https://pmc.ncbi.nlm.nih.gov/articles/PMC2680999/)). SEER, GBD, CDC, and national mortality databases contain nothing on this disease.

**Morbidity and function: no physical disability.** No functional impairment, no ICF-codable disability, no organ failure. The burden is **cosmetic and psychosocial**, in a disorder that is visible, whole-body, facial, congenital, and progressive — but there are **no QoL instrument data of any kind** (§3). This gap is real and worth recording as such rather than filled with plausible-sounding numbers.

**Complications**
- **Cutaneous malignancy: not established.** Melanoma occurred in one of two families that also reported pharyngeal and papillary thyroid cancer ([PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/)); the index six-generation family had none ("None of the affected members in this family was found to have skin cancer"). Given that KIT-GOF *receptor* mutations cause GIST, the theoretical concern is not absurd — but the FPHH ligand alleles have no demonstrated neoplastic risk, and a *KITLG*-GOF melanoma link would be a significant claim requiring far more than one family. Curate as an open question, explicitly not as an established complication.
- **No infections, no organ failure, no secondary systemic complications.**

**Recovery potential: none, and none needed.** The pigmentary phenotype is permanent; it neither resolves nor threatens health.

**Prognostic factors: none identified.** No age, severity, biomarker, or genotype predictor of course. Since no genotype–phenotype correlation exists, allele identity currently carries no prognostic information.

**Prognostic biomarkers: none.**

---

## 12. Treatment

**Bottom line: there is no disease-modifying therapy, no approved drug, no clinical trial, and no published treatment series for FPHH.** Management is cosmetic and supportive. Every statement below is either directly sourced to FPHH literature (little) or drawn from general hyperpigmentation management and labelled as such.

### What the FPHH literature actually says

> "The treatment is based solely on cosmetic purposes. The cosmetic oral treatment including depigmentation procedure of the gingiva can be carried out." — [PMID:22577587](https://pubmed.ncbi.nlm.nih.gov/22577587/) (patient declined; recommended "periodic evaluation")

That is essentially the entirety of the FPHH-specific treatment evidence base.

### Supportive / cosmetic management (extrapolated from general dyschromia management — flag as such)

General hyperpigmentation management comprises "photoprotection, topical lightening agents, oral agents, chemical peels, and laser therapy" ([PMID:35158001](https://pubmed.ncbi.nlm.nih.gov/35158001/), *JAAD* review Part II). Applied to FPHH:

| Intervention | Rationale | Candidate NCIT (verify) | Evidence in FPHH |
|---|---|---|---|
| Photoprotection (broad-spectrum SPF ≥30, physical measures) | Limits UV-driven superimposed darkening and PIH after any procedure | `NCIT:C15747` Supportive Care | **None.** Inference only |
| Camouflage cosmetics | Direct cosmetic benefit, zero risk | `NCIT:C15747` | None |
| **Genetic counselling** | The single most clearly indicated intervention — AD, 50% recurrence, reduced penetrance, de novo cases | `NCIT:C15240` Genetic Counseling | Standard of care by inference from inheritance |
| Topical lightening (hydroquinone `CHEBI:17594`, tretinoin `CHEBI:15367`, triple-combination cream) | Standard for epidermal hyperpigmentation | `NCIT:C15986` Pharmacotherapy + `therapeutic_agent` | **None in FPHH.** Also mechanistically dubious here: the drive is a continuous constitutive signal, so any lightening should relapse |
| **Q-switched Nd:YAG laser (1064/532 nm)** | "The gold standard in managing benign hyperpigmentations is currently 1064/532 nanometers Q-Switched lasers"; 36.4–76.6% success in solar lentigines | Laser therapy — *no confident NCIT ID; check* | **None in FPHH.** Note picosecond laser has been used in *SASH1*-DUH ([Skin Health Dis 2025](https://academic.oup.com/skinhd/article/5/3/191/8117750)), the nearest published precedent |
| Gingival depigmentation | For symptomatic oral pigmentation | *check* | The one FPHH-specific procedural suggestion ([PMID:22577587](https://pubmed.ncbi.nlm.nih.gov/22577587/)) |
| Psychosocial support | Visible congenital difference | `NCIT:C15747` | None; inference |

**Two cautions the curator should keep in the entry, because they are genuine risks rather than boilerplate:**
1. **Post-inflammatory hyperpigmentation.** In skin that is constitutively hypermelanotic under a hyperactive melanogenic drive, any laser or peel carries an elevated PIH risk. The general literature already recommends "broad-spectrum sunscreen with SPF ≥ 30 and physical photoprotection ... after Q-switched laser treatment to prevent post-inflammatory hyperpigmentation" ([Tandfonline 2024 RCT](https://www.tandfonline.com/doi/full/10.1080/09546634.2024.2398768)).
2. **Expected relapse.** Ablating melanin does not touch the germline GOF signal.

### Targeted therapy — the mechanistically obvious idea, and why it is not a recommendation

The pathway is druggable. **Imatinib** and other KIT inhibitors reliably cause depigmentation:

> Imatinib "inhibits the phosphorylation of c-kit receptor through SCF-induced melanocyte proliferation and melanogenesis"; "even at low concentrations it causes decreases in total melanin content and tyrosinase activity"; "The inhibition of melanogenesis is due to suppressed expression of tyrosinase and microphthalmia-associated transcription factor (MiTF)" ([PMID:24479586](https://pubmed.ncbi.nlm.nih.gov/24479586/), and see [PMID:14635084](https://pubmed.ncbi.nlm.nih.gov/14635084/))

Depigmentation occurs in 33–41% of imatinib-treated patients (up to ~80% in pigmented populations) and is reversible on withdrawal. Picardo & Cardinali's commentary gestures at exactly this: the KITLG/c-Kit findings "offer hope for the development of new and efficacious treatment strategies" ([PMID:21566575](https://pubmed.ncbi.nlm.nih.gov/21566575/)).

**But:** systemic imatinib for a benign cosmetic condition is not a defensible risk–benefit trade, and imatinib *also* causes hyperpigmentation in some patients ([PMC11401049](https://pmc.ncbi.nlm.nih.gov/articles/PMC11401049/)) — the pigmentary response is unpredictable. A **topical/intralesional** KIT inhibitor would be the rational形 of this idea and **does not exist**. Curate this as a `mechanistic_hypotheses` / `Experiment` proposal or a `discussions` entry, **never as a treatment**.

### Everything else

- **Pharmacogenomics:** not applicable — no drug is used.
- **Gene therapy, gene editing, cell therapy, RNA therapies (ASO/siRNA), immunotherapy, monoclonal antibodies, surgery, rehabilitation:** **none applicable, none reported.** Note that an allele-selective siRNA/ASO against a dominant GOF ligand is conceptually feasible; nothing has been attempted. Base editing appears in this literature **only as a laboratory tool** for modelling ([PMID:41779177](https://pubmed.ncbi.nlm.nih.gov/41779177/)), not as therapy — do not miscurate it as a `GENE_EDITING` treatment.
- **Clinical trials:** a ClinicalTrials.gov search for FPHH/*KITLG* pigmentation yields **no interventional trials**. Do not populate `clinical_trials:`.
- **Treatment algorithms / combination therapy / personalized medicine:** no FPHH-specific pathway exists. The nearest generalizable statement is that "A multimodal approach combining laser therapy and medical treatment may enhance outcomes" for hyperpigmentation broadly.

---

## 13. Prevention

**Primary prevention of the disease itself is impossible** — FPHH is a germline monogenic condition with no environmental component. What is preventable is *transmission* and *procedural harm*.

| Level | Applicable? | Detail |
|---|---|---|
| **Primary** | Only reproductive | **Genetic counselling** (`NCIT:C15240`) — AD, 50% recurrence per pregnancy from an affected parent, reduced penetrance, documented de novo cases (so unaffected parents of a proband have low but non-zero recurrence risk via possible germline mosaicism). Prenatal diagnosis and PGT-M are technically available once the familial variant is known; whether to offer them for a non-life-limiting cosmetic condition is a family-level values decision |
| **Secondary** | Limited | **Cascade testing** of at-risk relatives; early dermatologic recognition to avoid a diagnostic odyssey and, importantly, to avoid **misdiagnosis as NF1**, which would trigger unnecessary NF1 surveillance (imaging, ophthalmology) and cause real anxiety and cost |
| **Tertiary** | Limited | Photoprotection to limit superimposed UV darkening (inferred, not evidenced); careful patient selection before laser/peel to avoid PIH; periodic skin examination — reasonable general practice in a patient with numerous pigmented lesions, and made more reasonable (though not established) by the single family reporting melanoma |

**Not applicable:** immunization, population screening programmes, newborn screening, behavioural/lifestyle interventions, public-health interventions, environmental interventions, chemoprophylaxis. There is no risk-stratification model.

---

## 14. Other Species / Natural Disease

**No naturally occurring animal homolog of FPHH exists.** OMIA lists no *KITLG*-GOF hyperpigmentation phenotype in any domestic species, and I found no veterinary report. Curate this section as explicitly empty rather than stretching to fill it.

**What does exist is the mirror-image phenotype** — *Kitl* loss of function, which is one of the classic loci of mouse genetics:

- **Mouse *Kitl* — the Steel (*Sl*) locus** (MGI:96974; NCBI Gene 17311; NCBITaxon:10090). "Mouse strains carrying mutations at the Steel (Sl) locus are anemic and display defects in pigmentation and gametogenesis"; "homozygotes of viable mutant alleles have white coats and are sterile and severely anaemic."
- The key insight from *Sl* vs *W* (*Kit*) genetics — directly relevant to FPHH's paracrine mechanism: "the defect in Sl is not intrinsic to the progenitor stem cells of the affected tissues, but rather lies in the **environment** in which melanoblast, germ cell, and hematopoietic progenitors differentiate and proliferate." FPHH is the same architecture with the sign reversed: a niche-derived signal that is *too strong*.
- *Sl* mutations "exert deleterious effects on three migratory cell lineages (primordial germ cells, melanocytes and hematopoietic stem cells) resulting in loss of pigmentation, reduced fertility and anemia."
- **Human relevance of the dose axis:** "Mutant alleles of the KITLG gene are lethal in homozygous mice and produce a variable level of coat-color dilution in heterozygous mice" ([PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/)) — which matches the human observation that heterozygous *KITLG*-null carriers have lighter-than-expected skin.

**Orthologs:** *Kitl* (mouse, MGI:96974), *Kitlg* (rat), *kitlga/kitlgb* (zebrafish — the duplicated teleost paralogs; *kitlga* governs melanophore development), plus conserved orthologs across vertebrates. The KITLG–KIT axis is **deeply evolutionarily conserved as the core melanocyte-development module** across vertebrates, which is why the mouse and zebrafish literatures translate well.

**Comparative pathology:** the *loss*-of-function side translates cleanly (mouse *Sl*/*W*, human piebaldism/WS2, dog/horse/pig *KIT* white-spotting alleles). The *gain*-of-function side — FPHH's actual mechanism — has **no natural animal counterpart**, which is precisely why the engineered models in §15 matter.

**Zoonosis / cross-species transmission:** not applicable.

---

## 15. Model Organisms

### The honest headline

**There is no animal model carrying a human FPHH allele.** No knock-in mouse expressing p.Asn36Ser, p.Thr34Ile, p.Asp110Val, or any other FPHH variant has been reported. Everything below either models the *pathway* in the right direction (K14-Scf), models the *gene* in the wrong direction (Kitl LOF), or models the *variant* in cells rather than an organism. This should be curated as an explicit `HUMAN_MODEL_MISMATCH` discussion, not as a routine `KNOWLEDGE_GAP`: model evidence exists and is informative for the pathway, but no model reproduces the human FPHH mechanism.

### Available systems

**1. K14-Scf (K14-Kitl) transgenic mouse — the closest functional analog of FPHH.** *Krt14* promoter drives SCF in basal keratinocytes; this is a **gain of keratinocyte-derived KITLG signal**, the same directional perturbation as FPHH.

- Phenotype: "constitutive expression of SCF by epidermal keratinocytes results in retention of melanocytes in the interfollicular basal layer and pigmentation of the epidermis itself"; "Forced expression of SCF in K14-Scf transgenic mice promotes proliferation, differentiation, and migration of melanoblasts during embryogenesis as well as melanocyte stem cells during hair cycling, resulting in **a larger number of epidermal melanocytes and epidermal hyperpigmentation**."
- **Why it matters for §6's unresolved question:** this model produces hyperpigmentation *via increased epidermal melanocyte number*. That is direct model-organism support for the "melanocyte hyperplasia" side of the disputed FPHH histology.
- **Fidelity: MODERATE.** Right pathway, right direction, right cell-cell axis, right tissue outcome. **Limitations:** transgenic overexpression of *wild-type* SCF at supraphysiological levels driven by a heterologous promoter — not a heterozygous, endogenously regulated, affinity-altered ligand. It also fixes the ligand *level* rather than the ligand *quality*, so it cannot address the affinity hypothesis at all. And it is fundamentally a **humanizing** model (normal mouse epidermis lacks interfollicular melanocytes), meaning it corrects a species difference rather than reproducing a disease.
- Suggested link: `relationship: PARTIALLY_RECAPITULATES`, `fidelity: MODERATE`, readouts = epidermal melanocyte count (`INCREASED`), epidermal melanin content (`INCREASED`).

**2. *Kitlg*^Δ/+ frameshift mouse (2025) — the LOF counterpart.** Xiao *et al.*, *Genes & Diseases* 2025; **PMID:41584853**, DOI 10.1016/j.gendis.2025.101890 ([PMC12824913](https://pmc.ncbi.nlm.nih.gov/articles/PMC12824913/)). CRISPR/Cas9 heterozygous *Kitlg* c.81_84del, p.E27DfsX5.

- Phenotype: "Abnormal hair coloration (white hair on belly/forehead) in most mutant mice"; "Some *Kitlg*^Δ/+ mice displayed unilateral or asymmetric hearing loss; others retained normal hearing."
- Mechanism: "reduced KITLG expression impairs melanin synthesis in the stria vascularis without affecting intermediate cell migration"; proposes "a dual-hit model" with compensatory cAMP activation explaining incomplete penetrance.
- **Fidelity for FPHH: this model is `FAILS_TO_RECAPITULATE` FPHH** — it is a haploinsufficiency model producing *hypo*pigmentation and deafness (DFNA69/WS2F), the opposite phenotype. Its value to an FPHH entry is (a) confirming *KITLG* dose-sensitivity of pigmentation in vivo, and (b) modelling the **incomplete penetrance** that FPHH also shows. If curated, it must carry `limitations` and its own evidence per `test_failure_to_recapitulate_links_are_substantiated`.

**3. Steel (*Sl*) allelic series** — the historical LOF resource (MGI:96974); dozens of alleles from null (homozygous lethal) to hypomorphic (viable, white-coated, sterile, anaemic). Same directional caveat as above.

**4. Cell models — where the actual FPHH variants have been tested.**
- **A375 human melanoma cells + recombinant soluble sKITLG (WT vs N36S).** Readouts: melanin content 16.2 → 33.9 pg/cell; tyrosinase activity significantly increased; n=6, two-sided *t*-test ([PMID:19375057](https://pubmed.ncbi.nlm.nih.gov/19375057/), [PMC2680999](https://pmc.ncbi.nlm.nih.gov/articles/PMC2680999/)). `evidence_source: IN_VITRO`. **Limitation worth stating in the entry:** A375 is a melanoma line, not a normal melanocyte, and the assay adds exogenous soluble ligand rather than modelling heterozygous endogenous expression in a keratinocyte–melanocyte co-culture.
- **Adenine base editor–engineered cells + RNA-seq (2026).** The first modern functional platform for FPHH: "Functional changes were explored at a cellular level with the help of adenine base editors, and the differentially expressed genes in the melanin pathway were detected through RNA-sequencing" ([PMID:41779177](https://pubmed.ncbi.nlm.nih.gov/41779177/)). This is the model system to build on — it edits the endogenous locus rather than adding recombinant protein.
- **Human explanted skin (historical, cited in [PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/)):** "Injection of the soluble form of sKITLG resulted in hyperpigmentation of the grafted skin tissue, while injection of the KIT- or KITLG-blocking antibodies into the explanted human skin led to a loss of melanocytes." A **human-tissue** bidirectional demonstration of the axis — the highest-fidelity evidence available and a strong candidate for an `experimental_models:` entry with `modeled_mechanisms`.
- **In silico:** SIFT, PolyPhen-2, MutationTaster, SWISS-MODEL homology modelling ([PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/), [PMID:39152874](https://pubmed.ncbi.nlm.nih.gov/39152874/)). `evidence_source: COMPUTATIONAL`.

**5. Not yet used but obvious:** zebrafish *kitlga* (melanophore patterning, live imaging, high throughput); human iPSC-derived melanocytes; keratinocyte–melanocyte co-culture or 3D reconstructed skin with an FPHH allele knocked into the *keratinocyte* compartment — which is the only system that would test the paracrine architecture properly. None reported.

### Proposed experiments worth curating

1. **Knock-in mouse** carrying an FPHH allele (p.Asn36Ser or p.Asp110Val) at endogenous *Kitl*. `would_support`: `pathophysiology#KITLG Gain-of-Function Signaling`. `supporting_outcome`: progressive epidermal hyperpigmentation with age; increased epidermal melanocyte number and/or melanin per cell.
2. **Direct binding kinetics** (SPR/BLI) of mutant vs WT KITLG against KIT ectodomain. This tests the field's central *unproven* assumption — every "increased affinity" statement in the literature is inference from structure, never measured. `would_refute` if Kd is unchanged.
3. **Isoform-resolved functional assay** — soluble vs membrane-bound mutant KITLG, since all existing data used the soluble form only.
4. **Lesion-level genomics across a patient's skin** — digital PCR / low-pass WGS on paired hyper-, hypo-, CALM, and normal-appearing skin, to test whether the revertant-mosaicism finding ([PMID:39269165](https://pubmed.ncbi.nlm.nih.gov/39269165/)) generalizes beyond one patient and whether CALMs carry a separate somatic event.
5. **Topical KIT inhibition** in the K14-Scf mouse, as proof of concept for a non-systemic targeted approach.

### Resources

MGI (*Kitl* MGI:96974, Steel allele series, IMSR strain availability), IMPC/KOMP, Alliance of Genome Resources, ZFIN (*kitlga*), Cellosaurus/ATCC (A375, CVCL_0132), Addgene (ABE constructs).

---

## Summary of gaps to curate as `discussions`

| Gap | Kind | Why it matters |
|---|---|---|
| Mechanism of hypopigmented macule formation | `KNOWLEDGE_GAP` | Explicitly stated as unknown by the field; revertant-mosaicism hypothesis rests on one patient |
| Melanocyte hyperplasia vs per-cell hyperfunction | `KNOWLEDGE_GAP` | Primary literature is internally contradictory ([PMC2680999](https://pmc.ncbi.nlm.nih.gov/articles/PMC2680999/)) |
| Increased KITLG–KIT affinity never directly measured | `KNOWLEDGE_GAP` | The central mechanistic claim is structural inference, not biophysics |
| *KITLG*-negative FPHH families / second locus | `KNOWLEDGE_GAP` | Multiple families; FPH1 at 19pter–p13.1 unsolved |
| No animal model of any FPHH allele | `HUMAN_MODEL_MISMATCH` | K14-Scf models the pathway direction but not the allele; *Kitlg*^Δ/+ models the opposite direction |
| Penetrance unquantified; no genotype–phenotype correlation | `KNOWLEDGE_GAP` | Blocks counselling precision |
| No prevalence estimate | `KNOWLEDGE_GAP` | `prevalence_class: ULTRA_RARE` with `measure_type: UNKNOWN` is the honest record |
| Neurodevelopmental features: entity feature or coincidence? | `KNOWLEDGE_GAP` | Two pedigrees report them; the molecularly confirmed series contradicts |
| Malignancy signal in two families | `KNOWLEDGE_GAP` | Unreplicated; must not be curated as an established complication |
| No QoL data despite a highly visible congenital condition | `KNOWLEDGE_GAP` | Attach to `clinical_burden#` |
| Isoform (soluble vs membrane-bound) effects untested | `KNOWLEDGE_GAP` | All functional work used sKITLG only |

---

## Sources

- [Wang ZQ et al. 2009, Am J Hum Genet — PMID:19375057](https://pubmed.ncbi.nlm.nih.gov/19375057/) · [PMC2680999 full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC2680999/)
- [Amyere M et al. 2011, J Invest Dermatol — PMID:21368769](https://pubmed.ncbi.nlm.nih.gov/21368769/) · [JID full text](https://jidonline.org/article/S0022-202X(15)35302-1/fulltext)
- [Picardo M & Cardinali G 2011, J Invest Dermatol — PMID:21566575](https://pubmed.ncbi.nlm.nih.gov/21566575/)
- [Zeng L et al. 2016, Clin Exp Dermatol — PMID:27859606](https://pubmed.ncbi.nlm.nih.gov/27859606/)
- [Chinese FPHH family, genetic heterogeneity — PMID:29186243, An Bras Dermatol (SciELO)](https://www.scielo.br/j/abd/a/M5DQLMdMBNFP35L9RwsxqxR/?format=html&lang=en)
- [Kato M et al. 2020, J Dermatol — PMID:32189379](https://pubmed.ncbi.nlm.nih.gov/32189379/)
- [Wang J et al. 2021, BMC Med Genomics — PMID:33407466](https://pubmed.ncbi.nlm.nih.gov/33407466/) · [PMC7789533](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7789533/)
- [Gorenjak M et al. 2021, Mol Genet Genomic Med — PMID:34716665](https://pubmed.ncbi.nlm.nih.gov/34716665/)
- [Vona B et al. 2022, J Eur Acad Dermatol Venereol — PMID:35543077](https://pubmed.ncbi.nlm.nih.gov/35543077/)
- [Xu Z et al. 2022, Zhonghua Yi Xue Yi Chuan Xue Za Zhi — PMID:36453959](https://pubmed.ncbi.nlm.nih.gov/36453959/)
- [Huang X et al., Indian J Dermatol Venereol Leprol — PMID:39152874](https://ijdvl.com/a-novel-kitlg-mutation-causes-familial-progressive-hyperpigmentation-and-hypopigmentation-with-multiple-caf-au-lait-macules/)
- [Hida T et al. 2025, J Dermatol — PMID:39269165](https://pubmed.ncbi.nlm.nih.gov/39269165/)
- [Wu B et al. 2026, Mol Genet Genomics — PMID:41779177](https://pubmed.ncbi.nlm.nih.gov/41779177/)
- [Xiao Y et al. 2025, Genes & Diseases (Kitlg mouse) — PMC12824913](https://pmc.ncbi.nlm.nih.gov/articles/PMC12824913/)
- [Westerhof W et al. 1978, Arch Dermatol — PMID:666331](https://pubmed.ncbi.nlm.nih.gov/666331/)
- [FPH oral case report — PMID:22577587 / PMC3337584](https://pmc.ncbi.nlm.nih.gov/articles/PMC3337584/)
- [Familial progressive hypo- and hyperpigmentation: a variant case, IJDVL](https://ijdvl.com/familial-progressive-hypo-and-hyperpigmentation-a-variant-case/)
- [OMIM #145250 FPHH](https://www.omim.org/entry/145250) · [OMIM #614233 FPH1](https://omim.org/entry/614233) · [OMIM \*184745 KITLG](https://omim.org/entry/184745) · [OMIM #616697 DFNA69](https://omim.org/entry/616697) · [OMIM #619947 WS2F](https://omim.org/entry/619947)
- [GTR condition C1840392](https://www.ncbi.nlm.nih.gov/gtr/conditions/C1840392/) · [ClinVar VCV000379240](https://www.ncbi.nlm.nih.gov/clinvar/variation/379240/)
- [Genomics England PanelApp — KITLG, Pigmentary skin disorders](https://panelapp.genomicsengland.co.uk/panels/559/gene/KITLG/)
- [Orphanet ORPHA:79146](https://www.orpha.net/en/disease/detail/79146) · [ORPHA:280628](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=280628&amp=&lng=EN)
- [MalaCards — FPHH](https://www.malacards.org/card/hyperpigmentation_with_or_without_hypopigmentation_familial_progressive) · [GeneCards KITLG](https://www.genecards.org/cgi-bin/carddisp.pl?gene=KITLG) · [MGI Kitl MGI:96974](https://www.informatics.jax.org/marker/MGI:96974)
- [Zhou et al. 2023, DUH retyping — PMID:37353900](https://pubmed.ncbi.nlm.nih.gov/37353900/) · [OMIM #127500 DUH1](https://www.omim.org/entry/127500) · [OMIM 612715 DUH2](https://omim.org/entry/612715)
- [Disorders of hyperpigmentation Part II, JAAD — PMID:35158001](https://pubmed.ncbi.nlm.nih.gov/35158001/) · [Q-switched laser retrospective — PMC8544362](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8544362/) · [Post-QS-laser PIH RCT 2024](https://www.tandfonline.com/doi/full/10.1080/09546634.2024.2398768)
- [Imatinib inhibits human epidermal melanocytes — PMID:24479586](https://pubmed.ncbi.nlm.nih.gov/24479586/) · [Imatinib causes skin hypopigmentation — PMID:14635084](https://pubmed.ncbi.nlm.nih.gov/14635084/) · [Imatinib-induced hyperpigmentation — PMC11401049](https://pmc.ncbi.nlm.nih.gov/articles/PMC11401049/)
- [K14-Scf model context, Cell Reports](https://www.cell.com/cell-reports/fulltext/S2211-1247(17)30684-8) · [SCF rescues pigmentation in albino mice — PMID:19682281](https://pubmed.ncbi.nlm.nih.gov/19682281/)
- [KITLG rs995030 / TGCT — OMIM #273300](https://www.omim.org/entry/273300) · [SHEP7 OMIM #611664](https://omim.org/entry/611664?search=kitlg&highlight=kitlg)

---

**Suggested next step:** before drafting the YAML, run `just structured-rebuild-orphanet --id 280628 --id 79146` (needs the Orphadata bulk XML) to get quotable `ORPHA:` rows for the prevalence class, HPO frequency table, and gene-disease assertion — that would convert three of the qualitative gaps above (prevalence, phenotype frequencies, gene-disease validity) into snippet-validated evidence. Want me to attempt that, or go straight to expanding the stub's `pathophysiology` and `phenotypes` blocks from what is already in `references_cache/`?

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 29 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 45 |
| Quoted claims found in source | 30 |
| Quoted claims **not** found in source | 15 |
| Quoted claims with nothing to check against | 1 |
| References weighed for topical relevance | 29 |
| On topic | 15 |
| Off topic | 1 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:19375057` *(abstract only)*: "To our knowledge, these data provided the first genetic evidence that the FPH disease is caused by the KITLG N36S mutation, which has a gain-of-function effect on the melanin synthesis"
  - closest text in source: "To our knowledge, these data provided the first genetic evidence that the FPH disease is caused by the KITLGN36S mutation, which has a gain-of-function effect on the melanin synthesis and opens a new avenue for exploration of the genetic mechanism of FPH."
- `PMID:29186243` *(abstract only)*: "Familial progressive hyperpigmentation and hypopigmentation without KITLG mutation"
  - closest text in source: "BACKGROUND: Familial progressive hyper- and hypopigmentation (FPHH) is a rare genodermatosis that is characterized by diffuse hyper- and hypopigmented spots on the skin and mucous membranes"
- `PMC:PMC2680999` *(abstract only)*: "extensive hyperpigmentation of the conjunctive face, neck, trunk, limbs, lips, oral mucosa, palms, and soles"
  - closest text in source: "Familial progressive hyperpigmentation (FPH) is an autosomal-dominantly inherited disorder characterized by hyperpigmented patches in the skin, present in early infancy and increasing in size and number with age"
- `PMC:PMC2680999` *(abstract only)*: "None of the affected members in this family was found to have skin cancer"
  - closest text in source: "This mutant "G" allele cosegregated perfectly with affected, but not with unaffected, members of the FPH family"
- `PMID:22577587` *(abstract only)*: "The treatment is based solely on cosmetic purposes"
  - Text part not found as substring: 'The treatment is based solely on cosmetic purposes' (note: only abstract available for PMID:22577587, full text may contain this excerpt)
- `PMID:19375057` *(abstract only)*: "Function analysis of the soluble form of sKITLG revealed that mutant sKITLG N36S increased the content of the melanin by 109% compared with the wild-type sKITLG in human A375 melanoma cells. Consistent with this result, the tyrosinase activity was significantly increased by mutant sKITLG N36S compared to wild-type control."
  - closest text in source: "Function analysis of the soluble form of sKITLG revealed that mutant sKITLGN36S increased the content of the melanin by 109% compared with the wild-type sKITLG in human A375 melanoma cells"
- `PMID:22577587` *(abstract only)*: "strong basilar and suprabasilar hyperpigmentation ... Masson-Fontana stained sections showed an increase in the number of melanocytes in the basal and suprabasal cell layers."
  - closest text in source: "Familial progressive hyperpigmentation (FPH) is a rare genodermatosis characterized by hyperpigmented patches in the skin and mucous membranes, present in early infancy, and increase in size and number with age"
- `PMID:29186243` *(abstract only)*: "The staining for S100 and HMB45 were almost completely negative in the hypopigmentation areas."
  - closest text in source: "Histopathological and immunohistochemical staining for S100 and HMB45 of skin biopsy specimens from the hyperpigmented areas showed a striking increase in melanin throughout the epidermis, especially in the basal cell layer, and staining of hypopigmented area specimens displayed lower levels of melanin in the epidermis"
- `PMC:PMC2680999` *(abstract only)*: "increased melanin in the basal layer, **but no increase in the number of melanocytes** within the epidermis"
  - closest text in source: "Function analysis of the soluble form of sKITLG revealed that mutant sKITLGN36S increased the content of the melanin by 109% compared with the wild-type sKITLG in human A375 melanoma cells"
- `PMID:22577587` *(abstract only)*: "Hematology and blood chemistry did not reveal any abnormalities"
  - Text part not found as substring: 'Hematology and blood chemistry did not reveal any abnormalities' (note: only abstract available for PMID:22577587, full text may contain this excerpt)
- `PMID:22577587` *(abstract only)*: "The pigmentation was present since birth and eventually increased thereafter"
  - closest text in source: "Familial progressive hyperpigmentation (FPH) is a rare genodermatosis characterized by hyperpigmented patches in the skin and mucous membranes, present in early infancy, and increase in size and number with age"
- `PMC:PMC2680999` *(abstract only)*: "This process was rapid during childhood and slower during adolescence, and it resulted in extensive hyperpigmentation of the conjunctive face, neck, trunk, limbs, lips, oral mucosa, palms, and soles."
  - closest text in source: "Familial progressive hyperpigmentation (FPH) is an autosomal-dominantly inherited disorder characterized by hyperpigmented patches in the skin, present in early infancy and increasing in size and number with age"
- `PMID:22577587` *(abstract only)*: "The treatment is based solely on cosmetic purposes. The cosmetic oral treatment including depigmentation procedure of the gingiva can be carried out."
  - closest text in source: "Our paper stresses the need for the dentist to be aware of the systemic conditions that can also manifest in the oral cavity."
- `PMID:24479586` *(abstract only)*: "The inhibition of melanogenesis is due to suppressed expression of tyrosinase and microphthalmia-associated transcription factor (MiTF)"
  - closest text in source: "This inhibition of melanogenesis was due to suppressed expression of tyrosinase and microphthalmia-associated transcription factor (MiTF)"
- `PMID:14635084` *(abstract only)*: "The inhibition of melanogenesis is due to suppressed expression of tyrosinase and microphthalmia-associated transcription factor (MiTF)"
  - closest text in source: "Microphthalmia (Mi), a basic helix-loop-helix leucine zipper (bHLHZip) transcription factor, is phosphorylated by MAP kinase at a serine residue (S73)"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMC:PMC8544362` (3 mentions) - Nanosecond Q-Switched 1064/532 nm Laser to Treat Hyperpigmentations: A Double Center Retrospective Study.
  - shared terms: hyperpigmentation

Weighed against this report's own most characteristic terms: `fphh`, `kitlg`, `hyperpigmentation`, `skin`, `disease`, `allele`, `gene`, `kit`, `variant`, `family`, `hypopigmented`, `macule`, `melanocyte`, `cell`, `progressive`, `affected`, `genetic`, `phenotype`, `congenital`, `disorder`.

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `DOI:10.1080/09546634.2024.2398768`: "broad-spectrum sunscreen with SPF ≥ 30 and physical photoprotection ... after Q-switched laser treatment to prevent post-inflammatory hyperpigmentation"
  - Reference resolved but exposes no abstract or full text to search

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 43 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 3 |
| Terms whose name was checked | 6 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `NCIT:C15747` (3 mentions) - the report calls it "Direct cosmetic benefit, zero risk", "Visible congenital difference"; NCIT calls it **Supportive Care**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0014065` (obsolete phosphatidylinositol 3-kinase signaling) (1 mention) - replaced by `GO:0043491`
- `GO:0005615` (obsolete extracellular space) (1 mention) - replaced by `GO:0005576`

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `NCIT:C15747` - called "Direct cosmetic benefit, zero risk", "Visible congenital difference"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.