---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-29T00:44:05.364939'
end_time: '2026-08-29T00:58:38.834994'
duration_seconds: 873.47
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hyperostosis Cranialis Interna
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
  web_search_requests: 11
  num_turns: 73
  total_cost_usd: 5.332203000000002
  session_id: cea86725-875c-4523-9369-1c86a32fed3e
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
citation_count: 32
reference_validation:
  total_references: 39
  verified: 39
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 4
  quotes_valid: 3
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:794825
  relevance_assessed: 39
  on_topic: 12
  off_topic: 3
  off_topic_references:
  - PMID:21445361
  - DOI:10.1038/ncomms11601
  - DOI:10.1152/ajpgi.00244.2022
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 63
  verified: 59
  not_found: 0
  obsolete: 1
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 39
  labels_matching: 39
  obsolete_terms:
  - term_id: GO:0019933
    ontology_label: obsolete cAMP-mediated signaling
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
- **Disease Name:** Hyperostosis Cranialis Interna
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hyperostosis Cranialis Interna** covering all of the
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

# Hyperostosis Cranialis Interna (HCI) — Comprehensive Disease Research Report

**Prepared:** 2026-08-29 · **Target:** `kb/disorders/Hyperostosis_Cranialis_Interna.yaml` · **Category:** Mendelian (autosomal dominant sclerosing bone dysplasia)

---

## ⚠️ Read this first: a Named Entity Confusion hazard specific to this disease

The string "hyperostosis cranialis interna" is used in the literature in **two mutually incompatible senses**, and conflating them will corrupt the entry:

| Sense | What it is | Sources |
|---|---|---|
| **(A) The Mendelian disease** — MONDO:0007765 / OMIM 144755 / ORPHA:443098 | An autosomal dominant sclerosing bone dysplasia caused by heterozygous `SLC39A14` p.Leu441Arg, described in **one extended Dutch kindred** and, to date, nowhere else | Manni 1990 (PMID:2300107); Waterval 2010 (PMID:20140965); Hendrickx 2018 (PMID:29621230) |
| **(B) A descriptive radiological label** — non-Mendelian, sporadic internal skull-table thickening, overlapping **hyperostosis frontalis interna** (HFI) and Morgagni-Stewart-Morel syndrome | Used loosely in isolated case reports with no family history and no genetic testing | Alsaleh 2025 (PMID:40091967); Otken 2023 (PMID:37546094) |

**Curation implication:** only sense (A) is a dismech `Disease` entry. Evidence drawn from sense-(B) case reports (e.g. the 2025 Cureus CSF-leak case, the 2023 cadaveric report) must **not** be used to support phenotype frequencies, mechanism, or inheritance claims in this entry. Both are flagged explicitly in Section 10 (Differential diagnosis).

---

## 1. Disease Information

### Overview

Hyperostosis cranialis interna is a hereditary sclerosing bone dysplasia in which **endosteal bone deposition thickens the inner table of the calvaria and the skull base**, progressively narrowing the cranial neuroforamina and entrapping cranial nerves I, II, V, VII and VIII. It is the only known genetic bone dysplasia whose skeletal involvement is **confined to the craniofacial skeleton** — the appendicular skeleton and spine are radiologically and biochemically normal.

> "Hyperostosis cranialis interna is a hereditary bone disorder that is characterized by endosteal hyperostosis and osteosclerosis of the calvaria and the skull base (OMIM 144755). The progressive bone overgrowth causes entrapment and dysfunction of cranial nerves I, II, V, VII, and VIII, its first symptoms often presenting during the second decade."
> — Waterval JJ, Stokroos RJ, Bauer NJ, De Bondt RB, Manni JJ. *Am J Med Genet A.* 2010;152A(3):547–555. **PMID:20140965**, DOI:10.1002/ajmg.a.33205

> "HCI is a unique autosomal-dominant sclerosing bone dysplasia affecting the skull base and the calvaria, characterized by cranial nerve deficits due to stenosis of neuroforamina, whereby the mandible is affected to a lesser extent."
> — Waterval JJ, van Dongen TM, Stokroos RJ, De Bondt BJ, Chenault MN, Manni JJ. *AJNR Am J Neuroradiol.* 2012;33(3):453–461. **PMID:22194361**, DOI:10.3174/ajnr.A2830

> "HCI is the only genetic bone dysplasia known that is confined to the craniofacial area."
> — same source, PMID:22194361

### Key identifiers

| Resource | Identifier |
|---|---|
| **MONDO** | `MONDO:0007765` — *hyperostosis cranialis interna* (verified via OLS4; synonyms "HCIN", "hyperostosis cranialis interna (disease)") |
| **OMIM** | `144755` — HYPEROSTOSIS CRANIALIS INTERNA; HCIN |
| **Orphanet** | `ORPHA:443098` |
| **ICD-10** | `M85.2` (Hyperostosis of skull) — per Orphanet cross-reference |
| **ICD-11** | Not specifically coded; maps to the FB80-series "other specified disorders of bone density and structure" |
| **UMLS** | `C1840404` (per NIH GTR condition page) |
| **MeSH** | No dedicated descriptor; indexed under *Hyperostosis* (D015576) |
| **Causal gene** | `SLC39A14` — HGNC:20858, NCBI Gene 23516, Ensembl ENSG00000104635, UniProt Q15043, OMIM 608736, cytoband 8p21.3 |

### Synonyms and alternative names

- HCI; HCIN
- "Hyperostosis cranialis interna (disease)" (MONDO exact synonym)
- "Hyperostosis cranalis interna" (MONDO exact synonym — a propagated typographic variant)
- Historical: "Dominant generalized cortical hyperostosis with multiple cranial nerve involvement" (PMID:794825, a 1976 Dutch-language description that predates the 1990 delineation and may describe the same or a related entity — **verify before citing**)

### Data provenance

Essentially **all** primary knowledge derives from **aggregated case-series description of a single extended pedigree**, not from EHR/population data. There is no registry, no cohort study, and no population-scale genomic ascertainment. The genetic finding rests on a **single family, single variant, single WES proband** with segregation. Curate accordingly: frequencies below are *n/13* fractions from one kindred, not population estimates.

---

## 2. Etiology

### Primary cause — monogenic

Heterozygous missense mutation in `SLC39A14` (ZIP14), a plasma-membrane divalent-metal (Zn²⁺/Mn²⁺/Fe²⁺) transporter.

> "Hyperostosis Cranialis Interna (HCI) is a rare bone disorder characterized by progressive intracranial bone overgrowth at the skull. Here we identified by whole-exome sequencing a dominant mutation (L441R) in SLC39A14 (ZIP14)."
> — Hendrickx G, Borra VM, Steenackers E, *et al.*, Van Hul W. *PLoS Genet.* 2018;14(4):e1007321. **PMID:29621230**, DOI:10.1371/journal.pgen.1007321

The mutation is **not** a simple loss of function. It is a **trafficking-defective, intracellularly-retained allele** that behaves as a gain of pathological signalling (see Section 6):

> "We show that L441R ZIP14 is no longer trafficked towards the plasma membrane and excessively accumulates intracellular zinc, resulting in hyper-activation of cAMP-CREB and NFAT signaling."
> — PMID:29621230

**Historical mapping context.** Before the gene was found, linkage placed the locus at 8p21 and excluded the obvious candidates:

> "Linkage analysis in a family with HCI resulted in the localization of the disease-causing gene to a region on chromosome 8p21 delineated by markers D8S282 and D8S382. Interesting candidate genes in this region are BMP1, LOXL2, and ADAM28. Sequence analysis of these genes did not reveal any putative mutations. This suggests that a gene not previously involved in a sclerosing bone dysplasia is responsible for the abnormal growth in the skull of these patients."
> — Borra VM, Waterval JJ, Stokroos RJ, Manni JJ, Van Hul W. *Calcif Tissue Int.* 2013;93(1):93–98. **PMID:23640157**, DOI:10.1007/s00223-013-9732-8

### Risk factors

- **Genetic:** the causal variant itself. No susceptibility loci, no GWAS, no modifier loci have been reported (the pedigree is far too small for modifier mapping).
- **Environmental / lifestyle / occupational / infectious:** **none identified**. No toxin, radiation, dietary, or infectious contribution has been proposed or tested. Given ZIP14's role in metal transport, dietary zinc/manganese/iron status is a *biologically plausible but entirely untested* modifier — record as a knowledge gap, not as a risk factor.
- **Age/sex/family history:** family history is the only clinical risk factor. No sex bias has been reported in the kindred (see Section 9).

### Protective factors

**None known.** No protective variants, no modifier alleles, no dietary or lifestyle exposure has been reported to reduce penetrance or severity. gnomAD-based constraint analysis of `SLC39A14` has not been used to argue any protective allele for this phenotype.

### Gene–environment interactions

**No data.** This is a genuine, well-defined knowledge gap: ZIP14 substrate availability (dietary Zn, Mn, Fe) is the obvious axis, and the paralogous biallelic ZIP14 disease (hypermanganesemia with dystonia 2) is *pharmacologically modifiable by chelation* (PMID:27231142) — yet no study has asked whether metal status modifies the HCI bone phenotype. Suitable for a `KNOWLEDGE_GAP` discussion with `proposed_experiments`.

---

## 3. Phenotypes

### HPO annotation set for OMIM:144755 (retrieved from the HPO annotation API, 2026-08-29)

Frequencies are **n/13 affected individuals** from the Dutch kindred (Waterval 2010), except where HPO records a qualitative band.

| HP ID | Label (canonical, verified) | Frequency | Onset | Category |
|---|---|---|---|---|
| `HP:0004490` | **Calvarial hyperostosis** | 13/13 | — | Radiological/structural |
| `HP:0005746` | **Osteosclerosis of the base of the skull** | 13/13 | — | Radiological/structural |
| `HP:0005890` | **Hyperostosis cranialis interna** | — | — | Radiological/structural (disease-specific HPO term) |
| `HP:0001751` | **Abnormal vestibular function** | 10/13 | — | Clinical sign |
| `HP:0010628` | **Facial palsy** | 9/13 | — | Clinical sign (CN VII) |
| `HP:0000407` | **Sensorineural hearing impairment** | 8/8 tested | — | Clinical sign (CN VIII) |
| `HP:0000458` | **Anosmia** | 6/13 | Young adult | Symptom (CN I) |
| `HP:0002315` | **Headache** | 5/10 | Young adult | Symptom |
| `HP:0007906` | **Ocular hypertension** | 1/13 | — | Laboratory/clinical measurement |
| `HP:0007099` | **Chiari type I malformation** | 1/13 | — | Structural complication |
| `HP:0000648` | **Optic atrophy** | — | — | Clinical sign (CN II) |
| `HP:0007663` | **Reduced visual acuity** | — | — | Symptom (CN II) |
| `HP:0000360` | **Tinnitus** | — | — | Symptom (CN VIII) |
| `HP:0004409` | **Hyposmia** | — | — | Symptom (CN I) |
| `HP:0000520` | **Proptosis** | Very rare | — | Physical manifestation |
| `HP:0009926` | **Epiphora** | Very rare | — | Symptom |
| `HP:0200026` | **Ocular pain** | Very rare | — | Symptom |
| `HP:0000265` | Mastoiditis | Very rare | — | Complication |
| `HP:0003621` | **Juvenile onset** | — | — | Onset modifier |
| `HP:0011462` | **Young adult onset** | — | — | Onset modifier |

**Additional HPO terms to consider (verified labels, not in the current OMIM annotation set but supported by the literature):**

| HP ID | Label | Justification |
|---|---|---|
| `HP:0006824` | Cranial nerve paralysis | Umbrella term for the defining mechanism |
| `HP:0002516` | Increased intracranial pressure | Orphanet summary cites "headaches due to increased ocular and intracranial pressure" |
| `HP:0011001` | Increased bone mineral density | Osteosclerosis; note the caveat below that hyperostotic bone is *less* attenuating than normal cortex |
| `HP:0000365` | Hearing impairment | Parent of the SNHL annotation |

**Trigeminal (CN V) involvement** is named in the disease definition ("impairment of facial sensibility") but carries no discrete HPO annotation in the OMIM set; a facial-hypoesthesia term should be sourced with OAK before binding.

### Phenotype characteristics

**Age of onset.** Second decade is typical, but paediatric presentation occurs — a documented case presented with **bilateral facial palsy at age 8** (PMID:19371457).

> "…its first symptoms often presenting during the second decade." — PMID:20140965

**Severity and expressivity.** Markedly variable within the same kindred:

> "Patients are mildly to severely affected." — PMID:23640157

**Progression.** Progressive during childhood and early adult life, then **plateauing after the fourth decade** — clinically important because it defines the therapeutic window. Per the Orphanet summary of the disease: radiological progression is minimal after the fourth decade, although decreased intracranial volume can lead to death in severe cases.

**Disease course by nerve:**
- **CN VII (facial):** classically **recurrent** facial palsy — episodic, then fixed. This is the presenting sign in the index description (Manni 1990, PMID:2300107).
- **CN VIII:** progressive sensorineural hearing loss and progressive vestibular failure, up to **bilateral vestibular areflexia**.
- **CN I:** hyposmia progressing to anosmia.
- **CN II:** progressive visual loss with optic atrophy.

**Quality of life.** No EQ-5D, SF-36, or PROMIS data exist for HCI. The functional burden is inferable and severe: combined bilateral deafness + bilateral vestibular areflexia + facial paralysis + visual loss + anosmia in a single patient. **Record as a knowledge gap** — a disease-specific PRO instrument has never been applied.

### Objective function-test findings (the closest thing to a phenotype-frequency study)

> "Due to the symmetrical bilateral nature of this disease, the sensitivity of visual evoked potentials (VEPs), masseter reflex and blink reflex is decreased (25-37.5%), therefore reducing the value of single registration. Increased hearing thresholds and increased BERA latency times were found in 60-70%. The inter-peak latency I-V parameter in BERA has the ability to determine nerve encroachment reliably. 50% of the patients had vestibular abnormalities. No patient had disease-related absence of otoacoustic emissions, because the cochlea is not affected."
> — Waterval JJ, Bischoff MP, Stokroos RJ, Anteunis LJ, Hilkman DM, Kingma H, Manni JJ. *Clin Neurol Neurosurg.* 2013;115(9):1765–1770. **PMID:23622937**, DOI:10.1016/j.clineuro.2013.03.008

**Mechanistically decisive detail:** preserved otoacoustic emissions prove the lesion is **retrocochlear nerve compression, not cochlear disease** — a strong constraint on the pathophysiology chain and a good candidate evidence item.

---

## 4. Genetic / Molecular Information

### Causal gene

**`SLC39A14`** (solute carrier family 39 member 14), encoding **ZIP14** (metal cation symporter ZIP14).
HGNC:20858 · 8p21.3 · UniProt Q15043 · OMIM 608736 · Ensembl ENSG00000104635 · Entrez 23516
Aliases: ZIP14, ZIP-14, KIAA0062, NET34.

### The pathogenic variant

| Field | Value |
|---|---|
| **cDNA** | `NM_001128431.4(SLC39A14):c.1322T>G` |
| **Protein** | `p.Leu441Arg` (p.L441R) |
| **Exon** | Exon 8 |
| **Type** | Missense, single nucleotide variant |
| **Zygosity** | Heterozygous |
| **Origin** | Germline, inherited (autosomal dominant) |
| **ClinVar** | VCV000523143 — **Pathogenic**, review status "no assertion criteria provided" (single legacy submission; this is a *weak* review status despite functional support) |
| **Population frequency** | Absent from dbSNP, 1000 Genomes, ExAC; absent from 100 ethnically matched controls |
| **In silico** | CADD 29.4 |
| **Protein domain** | Within the **fifth transmembrane helix**; UniProt annotates TM helix at residues **425–445**, so residue 441 lies inside a TM span |
| **Functional class** | **Not a null.** Trafficking-defective / mislocalizing allele producing pathological intracellular signalling — best modelled as `GAIN_OF_FUNCTION` at the *pathway-state* level rather than a `LOSS_OF_FUNCTION` variant consequence (see the dismech GOF/LOF decision table) |

Supporting full-text statements (Hendrickx 2018, PMID:29621230 — **these are full-text quotes obtained through a fetch-and-summarize path; re-verify as exact substrings against a fetched reference cache entry before using them as evidence `snippet:` values**):

- "Whole-exome sequencing (WES) was performed on one affected individual from the family with HCI."
- "this missense mutation has a Combined Annotation Dependent Depletion (CADD) score of 29.4, indicating it belongs to the top 0.11% most deleterious substitutions"
- "was not found in 100 control individuals with the same ethnic background and is not present in sequence databases, including dbSNP, 1000 Genomes Project and ExAc databases"
- "This variant co-segregates with the disease in the complete family"

### Other `SLC39A14` variants in ClinVar listed against "Hyperostosis cranialis interna"

Retrieved 2026-08-29 (9 records). **Only one is pathogenic for HCI**; the rest are gene-level aggregation artefacts and must not be curated as HCI alleles:

| HGVS | Classification | Note |
|---|---|---|
| `c.1322T>G (p.Leu441Arg)` | **Pathogenic** | The HCI allele |
| `c.134A>G (p.Gln45Arg)` | Uncertain significance | Single submitter |
| `c.1301G>A (p.Gly434Glu)` | Uncertain significance | Single submitter |
| `c.751-9C>G` | Likely pathogenic | Listed against *both* HCI and hypermanganesemia with dystonia 2; the biallelic-disease assignment is the substantive one |
| `c.939+8G>C`, `c.1333-25G>A`, `c.98T>C`, `c.195A>G`, `c.457+45G>T` | Benign / Likely benign | Condition list is gene-level, not disease-specific |

### The allelic-disease contrast (important for the entry)

`SLC39A14` produces **two clinically unrelated diseases by two different mechanisms**:

| | **HCI** (MONDO:0007765, OMIM 144755) | **Hypermanganesemia with dystonia 2** (MONDO:0014864, OMIM 617013) |
|---|---|---|
| Inheritance | Autosomal dominant, single missense | Autosomal recessive, biallelic LOF |
| Mechanism | Mistrafficked ZIP14; intracellular Zn accumulation; cAMP-CREB/NFAT hyperactivation | Failed hepatic Mn uptake → systemic Mn accumulation → neurotoxicity |
| Tissue | Calvaria + skull base only | Basal ganglia; no bone phenotype reported |
| Treatable | No disease-modifying therapy | Chelation with disodium calcium edetate |

> "Although manganese is an essential trace metal, little is known about its transport and homeostatic regulation. Here we have identified a cohort of patients with a novel autosomal recessive manganese transporter defect caused by mutations in SLC39A14. Excessive accumulation of manganese in these patients results in rapidly progressive childhood-onset parkinsonism-dystonia with distinctive brain magnetic resonance imaging appearances and neurodegenerative features on post-mortem examination. … Chelation with disodium calcium edetate lowers blood manganese levels in patients and can lead to striking clinical improvement."
> — Tuschl K, Meyer E, Valdivia LE, *et al. Nat Commun.* 2016;7:11601. **PMID:27231142**, DOI:10.1038/ncomms11601

### Modifier genes, epigenetics, chromosomal abnormalities

- **Modifier genes:** none identified. Intrafamilial severity varies widely ("mildly to severely affected", PMID:23640157) so modifiers almost certainly exist, but the pedigree cannot power their detection.
- **Epigenetics:** **no data.** No methylation, histone, or chromatin study in HCI. (Note: an enterocyte-specific `Zip14` deletion mouse has been reported to alter intestinal homeostasis *through epigenetic mechanisms* — *Am J Physiol Gastrointest Liver Physiol* 2023, DOI:10.1152/ajpgi.00244.2022 — but this concerns gut, not bone, and is not evidence about HCI.)
- **Chromosomal abnormalities:** none. HCI is not a CNV/structural disorder; CMA and karyotype are uninformative.

---

## 5. Environmental Information

- **Environmental factors:** none established. HCI is fully explained by the germline variant.
- **Lifestyle factors:** none established.
- **Infectious agents:** none — not applicable.
- **Untested but mechanistically plausible:** dietary/systemic zinc, manganese and iron status, given ZIP14's substrate profile. **Do not curate as an `environmental:` entry with `influences_mechanisms`** — there is no citable evidence. If recorded at all, it belongs in a `KNOWLEDGE_GAP` discussion.

---

## 6. Mechanism / Pathophysiology

### The causal chain (upstream → downstream)

```
SLC39A14 c.1322T>G (p.L441R), heterozygous  [MOLECULAR]
   ↓  misfolding/retention within TM5
ZIP14 fails to traffic to the plasma membrane;
trapped in cytoplasm within early and late endosomes  [MOLECULAR/CELLULAR]
   ↓
Loss of extracellular Zn²⁺ uptake  +  paradoxical accumulation
of intracellular labile zinc  [MOLECULAR]
   ↓
Hyper-activation of cAMP-CREB signalling (~5-fold) and
NFAT signalling (~2-fold) in osteoblasts  [CELLULAR]
   ↓
Increased osteoblast-mediated endosteal bone formation
(inner table of calvaria + skull base)  [CELLULAR]
   ↓
Endosteal hyperostosis / osteosclerosis of calvaria and
skull base; dense, well-organized bone with reduced
Haversian channels and osteocytes  [TISSUE]
   ↓
Progressive stenosis of cranial neuroforamina
(optic canal, IAC, cribriform plate, foramina of CN V)  [TISSUE]
   ↓
Cranial nerve compression / entrapment → CN I, II, V, VII, VIII
dysfunction; reduced intracranial volume → raised ICP  [ORGANISM]
```

### Molecular pathways

**cAMP–CREB.** ZIP14's normal physiological role is to *facilitate* GPCR→cAMP–CREB signalling by suppressing basal phosphodiesterase activity — established in the knockout, where the effect runs in the opposite direction:

> "Here we report that the cell membrane-localized Zn transporter SLC39A14 controls G-protein coupled receptor (GPCR)-mediated signaling. Mice lacking Slc39a14 (Slc39a14-KO mice) exhibit growth retardation and impaired gluconeogenesis, which are attributable to disrupted GPCR signaling in the growth plate, pituitary gland, and liver. The decreased signaling is a consequence of the reduced basal level of cyclic adenosine monophosphate (cAMP) caused by increased phosphodiesterase (PDE) activity in Slc39a14-KO cells."
> — Hojyo S, Fukada T, Shimoda S, Ohashi W, Bin BH, Koseki H, Hirano T. *PLoS One.* 2011;6(3):e18059. **PMID:21445361**, DOI:10.1371/journal.pone.0018059

This is the key logical pivot: **KO → *reduced* cAMP-CREB and osteopenia; L441R → *hyper-activated* cAMP-CREB and hyperostosis.** The HCI allele is therefore mechanistically the *inverse* of a null, which is exactly why the disease is dominant and why it is not phenocopied by haploinsufficiency.

**Calcineurin–NFAT.** Doubled in the L441R condition (PMID:29621230). NFAT signalling is a canonical osteoblast/osteoclast differentiation regulator.

**Zinc homeostasis.** Loss of plasma-membrane Zn²⁺ import coexisting with intracellular Zn²⁺ accumulation — a compartmentalization defect rather than a whole-cell zinc deficit.

### Cellular processes and cell types

- **Osteoblast** (`CL:0000062`) — the primary effector. The osteoblast-restricted knock-in reproduces the bone phenotype; the osteoclast-restricted one does not.
- **Osteoclast** (`CL:0000092`) — ZIP14 is expressed but is not the driver of HCI. (It *is* the driver in the constitutive-KO osteopenia phenotype — see Section 15.)
- **Osteocyte** (`CL:0000137`) — reduced in number within HCI bone (histology below).
- Processes: `GO:0001649` osteoblast differentiation; `GO:0030282` bone mineralization; `GO:0001957` intramembranous ossification (the calvaria and much of the skull vault form by intramembranous ossification — the likely reason the phenotype is craniofacially restricted); `GO:0045453` bone resorption.

### Protein dysfunction

ZIP14 is an "Electroneutral transporter of the plasma membrane mediating the cellular uptake of the divalent metal cations zinc, manganese and iron that are important for tissue homeostasis, metabolism, development and immunity" (UniProt Q15043). p.L441R inserts a **charged arginine into a transmembrane helix (425–445)** — a classic destabilizing substitution that would be expected to trigger ER/endosomal retention, consistent with the observed localization to early and late endosome membranes (which are, notably, *native* ZIP14 locations per UniProt, suggesting the mutant is stalled in a normal part of the itinerary rather than misrouted to a novel compartment).

Reported functional results (PMID:29621230, full text — re-verify before snippet use):
- WT ZIP14 increased ⁶⁵Zn uptake ~4-fold; L441R showed "no sign of ⁶⁵Zn uptake from the extracellular space"
- L441R produced a significantly "stronger (p<0.001) increase in intracellular Zn accumulation" than WT
- L441R "is not present on the plasma membrane, but appears to be trapped in the cytoplasm"
- cAMP-CREB: "significant (p = 0.004) 5-fold increase"; NFAT signalling doubled

### Tissue-level pathology (human bone histology)

From the HCI patient specimen (PMID:29621230, full text — re-verify):
- "patient interna is wider and characterized by a great and dense amount of well-organized bone, suggesting an increased bone formation or decreased bone resorption"
- "number of Haversian channels and osteocytes are significantly lower in the patient interna"

And from the linkage paper:

> "Histomorphological investigations showed increased bone formation with a normal tissue structure. Biochemical parameters were normal." — PMID:23640157

**Note the tension** between "well-organized bone / normal tissue structure" and the CT finding that the deposited bone is *less* dense than normal cortex:

> "The attenuation of the deposited hyperostotic bone was lower than normal cortical bone." — PMID:22194361

This is a real, curatable nuance: HCI bone is *abundant but hypomineralized relative to normal cortex* — it is a quantity, not a quality, lesion.

### Metabolic, immune, biochemical

- **Metabolic changes:** none demonstrated in bone. Systemic biochemistry is normal (PMID:23640157). ZIP14 has metabolic roles elsewhere (hepatic gluconeogenesis, insulin signalling) that are **not** reported as abnormal in HCI patients.
- **Immune involvement:** none. No autoimmunity, immunodeficiency, or inflammation reported.
- **Serum Zn / Mn / Fe in HCI patients:** **not measured/not reported.** A conspicuous gap — the paralogous recessive disease is defined by hypermanganesaemia, and nobody has published metal levels in HCI carriers. High-value `proposed_experiment`.

### Molecular profiling and advanced technologies

**None available for HCI.** No transcriptomics, proteomics, metabolomics, lipidomics, single-cell, spatial, multi-omics, or CRISPR/RNAi screen has been performed on HCI tissue. There is no GEO/ArrayExpress dataset for this disease. Do **not** manufacture `datasets:` records; gene-only searches on `SLC39A14` will surface manganese-neurotoxicity and hepatology datasets that are `GENE_ONLY`/`CONFLICT` for this entry.

### Suggested ontology bindings (labels verified against OLS4/local caches unless flagged)

**Biological processes (GO):**
| CURIE | Canonical label | Suggested `modifier` |
|---|---|---|
| `GO:0071578` | zinc ion import across plasma membrane | `DECREASED` |
| `GO:0006882` | intracellular zinc ion homeostasis | `ALTERED` state → use `INCREASED` for labile Zn accumulation |
| `GO:0072659` | protein localization to plasma membrane | `DECREASED` |
| `GO:0007189` | adenylate cyclase-activating G protein-coupled receptor signaling pathway | `GAIN_OF_FUNCTION` (qualitative — signalling escapes normal PDE restraint) |
| `GO:0033173` | calcineurin-NFAT signaling cascade | `INCREASED` |
| `GO:0001649` | osteoblast differentiation | `INCREASED` |
| `GO:0030282` | bone mineralization | `INCREASED` |
| `GO:0001957` | intramembranous ossification | `INCREASED` |
| `GO:0045453` | bone resorption | consider `DECREASED` — *hypothesis only*, the histology says "increased bone formation **or** decreased bone resorption" |

⚠️ **`GO:0019933` ("cAMP-mediated signaling") is OBSOLETE in GO** — do not bind it. Use `GO:0007189` (verified in the local `cache/go/terms.csv`).

**Molecular functions (GO):** `GO:0005385` zinc ion transmembrane transporter activity (verified, in local cache); `GO:0005384` manganese ion transmembrane transporter activity (from UniProt annotation, verify with OAK before binding).

**Cell types (CL):** `CL:0000062` osteoblast; `CL:0000092` osteoclast; `CL:0000137` osteocyte; `CL:0007010` preosteoblast (all verified in `cache/cl/terms.csv`).

**Chemical entities (CHEBI):** zinc(2+), manganese(2+), iron(2+), cAMP — resolve CURIEs with OAK before binding; not verified here.

---

## 7. Anatomical Structures Affected

### Organ level

- **Primary:** the **skull** — specifically the **inner table (lamina interna) of the calvaria** and the **skull base**. Frontal, parietal, temporal and occipital regions are all involved; the sphenoid bone and clivus show the highest metabolic activity.
- **Secondary:** cranial nerves I, II, V, VII, VIII; the orbit (ocular hypertension, proptosis, epiphora); the intracranial compartment (reduced volume, raised ICP, and in one case a Chiari type I malformation, `HP:0007099`, 1/13).
- **Explicitly spared:** the appendicular skeleton, vertebral column, and the cochlea. Mandibular involvement is present but lesser (PMID:22194361).
- **Body systems:** skeletal (primary); nervous — cranial nerves (secondary); special senses (olfactory, visual, auditory, vestibular).

> "There was significant thickening of the skull in the frontal, parietal, temporal, and occipital regions, which was mainly due to thickening of the inner table of the skull." — PMID:22194361

> "…which is confined to the skull, especially the calvarium and the skull base. The rest of the skeleton is not affected." — PMID:23640157

### Metabolic topography

> "(18)F-Fluoride uptake is statistically significantly higher in the sphenoid bone and clivus regions of affected family members."
> — Waterval JJ, Van Dongen TM, Stokroos RJ, Teule JG, Kemerink GJ, Brans B, Nieman FH, Manni JJ. *Eur J Nucl Med Mol Imaging.* 2011;38(5):884–893. **PMID:21079950**, DOI:10.1007/s00259-010-1655-2

### Tissue / cell level

- Tissue: **compact/cortical bone of the calvarial inner table**; endosteal surface.
- Cells: osteoblast (`CL:0000062`) — driver; osteocyte (`CL:0000137`) — reduced density in affected bone; osteoclast (`CL:0000092`) — expresses ZIP14 but is not the HCI effector cell.

### Subcellular level (GO Cellular Component)

- Normal ZIP14: `GO:0005886` plasma membrane, `GO:0016323` basolateral plasma membrane, `GO:0016324` apical plasma membrane.
- Mutant ZIP14: retained in **early endosome membrane** and **late endosome membrane** (UniProt-annotated native locations; the mutant fails to progress beyond them). Resolve `GO:0031901`/`GO:0031902` (early/late endosome membrane) with OAK before binding — not verified here.

### Localization and lateralization

**Bilateral and strikingly symmetric.** This is not incidental — it is what degrades the diagnostic yield of side-to-side electrophysiological comparison:

> "Due to the symmetrical bilateral nature of this disease, the sensitivity of visual evoked potentials (VEPs), masseter reflex and blink reflex is decreased (25-37.5%), therefore reducing the value of single registration." — PMID:23622937

**Suggested UBERON bindings (verified via OLS4):**
| CURIE | Canonical label |
|---|---|
| `UBERON:0004339` | vault of skull |
| `UBERON:0002517` | basicranium |
| `UBERON:0017692` | internal surface of cranial base |
| `UBERON:0011859` | internal acoustic meatus |
| `UBERON:0005745` | optic foramen |
| `UBERON:0018413` | facial nerve canal |

Cribriform plate and foramen ovale/rotundum terms should be resolved with OAK before binding.

---

## 8. Temporal Development

**Onset.** Insidious, chronic. HPO records both `HP:0003621` juvenile onset and `HP:0011462` young adult onset. Typically second decade; headache and anosmia are annotated with young-adult onset; documented paediatric onset at age 8 with bilateral facial palsy (PMID:19371457).

**Stages (proposed for `progression:`):**

| Phase | Description |
|---|---|
| **Presymptomatic** | At-risk carrier; radiological hyperostosis already detectable on CT before symptoms. This is the window in which prophylactic decompression has been argued for. |
| **Early symptomatic** | Recurrent facial palsy; hyposmia; subclinical BERA I–V interpeak prolongation |
| **Established** | Fixed facial paresis; progressive SNHL; vestibular hypofunction to areflexia; anosmia; visual decline |
| **Late (post-4th decade)** | Radiological progression minimal; deficits fixed; in severe cases, reduced intracranial volume with raised ICP — potentially fatal |

**Progression rate.** Slow and progressive over decades, **with a plateau after the fourth decade** (Orphanet/OMIM summary). Deficits already established do not remit.

**Course pattern.** Progressive overall; the *facial nerve* component is characteristically **recurrent/episodic** early on before becoming fixed — a `RECURRENT` `temporality` qualifier is appropriate for the facial-palsy phenotype.

**Duration.** Chronic, lifelong.

**Remission.** No spontaneous remission of the bone disease. Treatment-induced functional recovery is documented after surgical decompression (House-Brackmann I and II at one year — PMID:19371457) but the underlying hyperostosis is unaffected.

**Critical period / intervention window.** Explicit in the literature, and the single most actionable clinical statement in the entry:

> "Surgical decompression of the accessible impaired cranial nerves is advised in the early symptomatic period or even in the presymptomatic period in high-risk individuals." — PMID:20140965

---

## 9. Inheritance and Population

### Epidemiology

- **Prevalence:** **not documented.** Orphanet (ORPHA:443098) does not publish a prevalence class for this disease, and no registry exists. The honest structured record is a `CASES_IN_LITERATURE` measure, not a rate.
- **Incidence:** not available.
- **Case count:** the disease has been reported in **one Dutch kindred**, comprising three related families with common progenitors, 32 individuals over five generations.

> "Until today the disease has been described in only three related Dutch families with common progenitors and which consist of 32 individuals over five generations. HCI was observed in 12 family members over four generations." — PMID:23640157

⚠️ **Numeric discrepancy to record explicitly:** Borra 2013 states **12 affected over four generations**; Waterval 2010 analyses **13 affected individuals of three related families (32 individuals)**; the HPO frequency denominators are `/13`. Curate 13 (with the /13 denominators) and note the 12-vs-13 discrepancy in `notes:` rather than silently picking one.

Suggested `prevalence` record shape:

```yaml
prevalence:
- population: Worldwide
  measure_type: CASES_IN_LITERATURE
  prevalence_class: ULTRA_RARE
  notes: >-
    Reported in a single extended Dutch kindred. Waterval 2010 analyses 13 affected
    individuals among three related families totalling 32 individuals; Borra 2013
    reports 12 affected over four generations across five generations of pedigree.
    No prevalence rate has been published; Orphanet ORPHA:443098 records no
    prevalence class.
```

### Genetic epidemiology

- **Inheritance pattern:** **Autosomal dominant** (HPO annotation for OMIM:144755; stated in every primary source). Bind `HP:0000006` (Autosomal dominant inheritance) — resolve label with OAK before binding.
- **Penetrance:** appears high/complete for the *radiological* phenotype — calvarial hyperostosis and skull-base osteosclerosis are annotated at **13/13**. Clinical penetrance of individual nerve deficits is incomplete and age-dependent (facial palsy 9/13; anosmia 6/13). No formal penetrance estimate has been published.
- **Expressivity:** **variable** — "Patients are mildly to severely affected" (PMID:23640157).
- **Anticipation:** not reported; not expected (not a repeat-expansion disorder).
- **Germline mosaicism:** not reported.
- **Founder effect:** the variant is, in effect, a **private founder allele of one Dutch kindred** with common progenitors. It is *not* a population founder variant in the usual sense — do not describe it as a Dutch population founder mutation.
- **Consanguinity:** not relevant (dominant).
- **Carrier frequency:** not applicable (dominant); the allele is absent from population databases.

### Demographics

- **Affected populations:** Dutch (single kindred). No other ethnicity reported. The apparent Dutch specificity is an ascertainment artefact of a single pedigree, not established population biology.
- **Geographic distribution:** the Netherlands (Nijmegen/Maastricht ascertainment).
- **Sex ratio:** not reported as skewed; no sex bias described in the pedigree. Autosomal dominant transmission with male-to-male transmission implied by the pedigree structure. **Record as unknown rather than 1:1.**
- **Age distribution:** affected individuals span childhood to old age within the kindred; symptomatic ascertainment concentrates in the second-to-fourth decades.

---

## 10. Diagnostics

### Imaging — the diagnostic mainstay

**CT (high-resolution, bone algorithm)** is the primary diagnostic test. From PMID:22194361:
- Linear measurement of **inner table, medulla (diploë) and outer table** at defined skull locations
- **Attenuation (HU) measurement** of the same regions
- **Neuroforamina width** measurement
- Findings: significant thickening in frontal, parietal, temporal and occipital regions, **predominantly of the inner table**; hyperostotic bone attenuation **lower than normal cortical bone**

> "The observed radiologic abnormalities explain the possible impairment of the olfactory, optic, trigeminal, facial, and vestibulocochlear nerves." — PMID:22194361

**MRI** — complementary, for nerve/soft-tissue assessment and to exclude mimics.

**¹⁸F-fluoride (NaF) PET/CT** — a quantitative bone-metabolism test with a demonstrated role here:

> "(18)F-Fluoride PET/CT is useful in quantifying the metabolic activity in HCI and provides information about the process of disturbed bone metabolism in this specific disorder." — PMID:21079950

Study design for reference: "Nine affected family members, seven non-affected family members and nine non-HCI non-family members underwent (18)F-fluoride PET/CT scans. SUVs were systematically measured in the different regions of interest: frontal bone, sphenoid bone, petrous bone and clivus." (PMID:21079950)

Note that ¹⁸F-NaF PET quantification methodology has since been systematically reviewed across 29 bone conditions including HCI (de Ruiter RD *et al., Ann Nucl Med.* 2025; **PMID:39729191**, DOI:10.1007/s12149-024-01991-9).

### Functional / electrophysiological testing (the recommended monitoring panel)

Per PMID:23622937, the evidence-based recommendation is explicit about what to use *and what to drop*:

> "In patients with HCI and similar craniofacial sclerosing bone dysplasias we advise monitoring of vestibulocochlear nerve function with tone and speech audiometry, BERA and vestibular tests. VEPs are important to monitor optic nerve function in combination with radiological and ophthalmologic examination. We do not advise the routine use of blink and masseter reflex."

**Recommended:** pure-tone and speech audiometry; **BERA — the I–V interpeak latency specifically** ("has the ability to determine nerve encroachment reliably"); vestibular testing (electronystagmography); VEPs for CN II in combination with imaging and ophthalmology.
**Not recommended for routine use:** blink reflex, masseter reflex (sensitivity 25–37.5% owing to bilateral symmetry).
**Also tested and informative as a negative:** otoacoustic emissions are **preserved** — their preservation is the evidence that the cochlea is spared and the lesion is retrocochlear.

Additional: olfactory testing (for CN I), ophthalmological examination including **intraocular pressure** (`HP:0007906` ocular hypertension, 1/13), visual acuity and fundoscopy for optic atrophy.

### Laboratory tests and biomarkers

**None diagnostic.** Routine bone biochemistry is normal:

> "Biochemical parameters were normal." — PMID:23640157

There is **no validated biomarker** for HCI. Serum/plasma zinc and manganese have not been reported in HCI patients — a testable gap given the allelic recessive disease is defined by hypermanganesaemia. LOINC-coded reference ranges are therefore not applicable to this entry.

### Biopsy / histopathology

Rarely indicated diagnostically, but reported: increased bone formation with normal tissue architecture (PMID:23640157); wider, dense, well-organized inner table with reduced Haversian channels and osteocytes (PMID:29621230).

### Genetic testing

- **Recommended first-line in a known family:** **targeted single-variant testing** for `SLC39A14` c.1322T>G (p.Leu441Arg) — this is cascade testing within the kindred and is the only high-yield test outside it.
- **Single-gene sequencing of `SLC39A14`:** appropriate for a sporadic case with a compatible CT phenotype.
- **Gene panels:** sclerosing bone dysplasia / high-bone-mass panels. `SLC39A14` is not universally included — verify panel content in GTR before ordering.
- **WES:** how the gene was found (one proband); reasonable for an undiagnosed craniofacial sclerosing dysplasia.
- **WGS:** no established incremental utility over WES here.
- **CMA / karyotype / FISH:** **not indicated** — HCI is not a structural/CNV disorder.
- **mtDNA testing, repeat-expansion testing:** not applicable.
- **Omics-based diagnostics** (RNA-seq, proteomics, metabolomics, epigenomics, liquid biopsy): **none validated or reported** for HCI.

### Clinical criteria

There are **no formal published diagnostic criteria, no society guideline, and no DSM/ICD-based algorithm.** The operational diagnosis is: characteristic CT pattern (inner-table–predominant calvarial + skull-base hyperostosis with normal appendicular skeleton) + cranial neuropathy in ≥1 of CN I/II/V/VII/VIII + autosomal dominant family history and/or `SLC39A14` p.L441R.

The clinical trigger for suspicion, per the authors of the phenotype study, is **adult- or childhood-onset facial or vestibulocochlear nerve impairment** in the right radiological context.

### Differential diagnosis

**Other sclerosing bone dysplasias with craniofacial involvement** — the discriminator is whether the *long bones* are involved:

> "Besides HCI, several bone dysplasias with hyperostosis and sclerosis of the craniofacial bones are known. Examples are Van Buchem disease, sclerosteosis, craniometaphyseal dysplasia, and Camurati-Engelmann disease. However, in these cases the long bones are affected as well." — PMID:23640157

| Condition | Distinguishing feature vs HCI |
|---|---|
| **Van Buchem disease** (`SOST`) | Generalized endosteal hyperostosis including long bones, mandible enlargement |
| **Sclerosteosis** (`SOST`) | Gigantism, syndactyly, long-bone involvement |
| **Craniometaphyseal dysplasia** (`ANKH`, `GJA1`) | Metaphyseal flaring of long bones |
| **Camurati-Engelmann disease** (`TGFB1`) | Diaphyseal sclerosis, limb pain, waddling gait |
| **Hyperostosis frontalis interna (HFI)** | Frontal-only, common, non-Mendelian, strongly female/postmenopausal, usually asymptomatic; **the most important mimic** |
| **Morgagni-Stewart-Morel syndrome** | HFI + obesity + virilism + neuropsychiatric features |
| **Fibrous dysplasia / Paget disease of bone** | Focal/mosaic, distinct radiology, abnormal ALP |
| **IAC exostoses / osteomas** | Focal, unilateral, non-familial (see PMID:32499994) |
| **Osteopetrosis, pycnodysostosis** | Generalized skeletal sclerosis, marrow failure, fractures |

The definitive review for this differential — with a large CT/MRI image collection and craniofacial embryology — is:

> "In this review we provide a complete overview of the existing sclerosing bone dysplasias with craniofacial involvement. Clinical presentation, disease course, the craniofacial symptoms, genetic transmission pattern and pathophysiology are discussed. There is an emphasis on radiologic features with a large collection of CT and MRI images. In previous reviews the craniofacial area of the sclerosing bone dysplasias was underexposed. However, craniofacial symptoms are often the first symptoms to address a physician."
> — Waterval JJ, Borra VM, Van Hul W, Stokroos RJ, Manni JJ. *Bone.* 2014;60:48–67. **PMID:24325978**, DOI:10.1016/j.bone.2013.12.003

**Also in the differential of the *presenting complaint*:** multiple cranial-nerve palsies of any cause (see PMID:2300109, "Multiple cranial-nerve palsies: a diagnostic challenge", published alongside the original 1990 description).

### Screening

- **Newborn screening:** not applicable, none exists.
- **Carrier screening:** not applicable (dominant).
- **Cascade screening:** **this is the operative screening modality.** At-risk relatives in the kindred should undergo targeted variant testing, and gene-positive individuals should enter radiological (CT) and functional (audiometry/BERA/vestibular/VEP/olfaction/IOP) surveillance — the whole rationale being to identify the presymptomatic window for decompression.

---

## 11. Outcome / Prognosis

### Survival and mortality

- **No survival data, no life-expectancy figure, no mortality rate has been published.** There is no registry and the total literature cohort is ~13 people.
- Severe disease is described as potentially fatal via reduced intracranial volume (per the OMIM/Orphanet disease summaries: decreased intracranial volume can lead to death in severe cases). Treat this as an **authoritative-summary claim without a primary case-level citation attached in the sources retrieved here** — verify against the OMIM entry text or Manni 1990 before curating it as a mortality claim.
- **Disease-specific mortality:** unquantified.

### Morbidity and function

The morbidity burden is sensory-neurological rather than skeletal: bilateral sensorineural deafness, bilateral vestibular areflexia (with the balance disability that implies), facial paralysis (functional and social/aesthetic), anosmia, and visual loss. Several of these are individually disabling and they co-occur.

**No ICF coding, no disability registry data, no QoL instrument (EQ-5D/SF-36/PROMIS) has ever been applied to HCI.** Record as a knowledge gap.

### Complications

- Raised intracranial pressure; headache (`HP:0002315`, 5/10)
- Ocular hypertension (`HP:0007906`, 1/13); proptosis; epiphora; ocular pain
- Chiari type I malformation (`HP:0007099`, 1/13) — presumably secondary to posterior fossa volume reduction
- Mastoiditis (`HP:0000265`, very rare)
- **Surgical complication:** cerebral vasospasm after auditory brainstem implantation — Waterval JJ, Stokroos RJ, Dings J, Van Overbeeke JJ, Manni JJ. *Clin Neurol Neurosurg.* 2011;113(8):693–697. **PMID:21665359**, DOI:10.1016/j.clineuro.2011.05.005 (no abstract available in Europe PMC; obtain full text before citing specifics)

### Recovery potential

Established nerve deficits do not spontaneously recover. **Timely decompression can restore function** — the strongest positive outcome datum in the literature is a single paediatric case:

> "Using a middle fossa craniotomy approach, both internal auditory canals were unroofed and cranial nerves VII and VIII were decompressed, with a one-year interval between sides. The mimic function recovered. One year post-operatively, the right and left facial sides had been restored to House-Brackmann grades I and II, respectively."
> — Waterval JJ, Stokroos RJ, De Bondt RB, Manni JJ. *J Laryngol Otol.* 2009;123(9):1058–1062. **PMID:19371457**, DOI:10.1017/S0022215109005349

### Prognostic factors

No validated model. Clinically implied factors: **age at intervention** (earlier = better, hence the presymptomatic-surgery argument); degree of foraminal stenosis on CT; BERA I–V interpeak latency as a marker of nerve encroachment; the post-fourth-decade radiological plateau as a favourable natural-history feature. **Prognostic biomarkers: none.**

---

## 12. Treatment

**There is no disease-modifying therapy.** Management is symptomatic and surgical.

> "The treatment is symptomatic." — PMID:23640157

### Surgical / interventional (the principal modality)

| Treatment | Detail | NCIT suggestion |
|---|---|---|
| **Surgical decompression of cranial nerves** | Middle-fossa craniotomy with unroofing of the internal auditory canal, decompressing CN VII and VIII; performed bilaterally with a staged interval | `NCIT:C15329` Surgical Procedure (verify a more specific neurosurgical/decompression term with OAK) |
| **Optic nerve decompression** | Advised for CN II involvement in the early symptomatic/presymptomatic period (PMID:20140965) | `NCIT:C15329` Surgical Procedure |
| **Auditory brainstem implantation (ABI)** | Used for hearing rehabilitation when the cochlear nerve is non-functional; **carries documented risk of cerebral vasospasm in HCI** (PMID:21665359) | `DEVICE` modality; NCIT term to be resolved with OAK |
| **Prophylactic decompression** | Explicitly proposed: "Surgical decompression of the internal auditory canal is recommended therapeutically, but may also be performed prophylactically in younger patients with hyperostosis cranialis interna." (PMID:19371457) | — |

Evidence base and quality: this is **level-4/5 evidence — case reports and a single-family case series.** There is no comparative study, no RCT, no consensus guideline. Curate the surgical recommendations as expert-opinion-grade with `evidence_source: HUMAN_CLINICAL` and be explicit in `explanation` that they rest on individual cases.

`therapeutic_modality` assignments: `SURGERY` for the decompressions; `DEVICE` for ABI/hearing devices.

### Pharmacotherapy

**No pharmacological treatment exists.** Notably:
- **Bisphosphonates and other antiresorptives are not established** for HCI and are mechanistically questionable — the lesion is excess *formation*, not deficient resorption. Do not curate speculative antiresorptive use.
- **Chelation therapy (disodium calcium edetate)** is effective in the *allelic recessive* disease (hypermanganesemia with dystonia 2, PMID:27231142) and has **no evidence or rationale** in HCI, whose mechanism is intracellular zinc accumulation from a mistrafficked transporter, not systemic manganese excess. **This is a trap — do not transfer the treatment across the allelic boundary.**
- **Pharmacogenomics:** not applicable.

### Advanced therapeutics

**None.** No gene therapy, gene editing, ASO, siRNA, mRNA therapy, cell therapy, targeted therapy or immunotherapy exists or is in development for HCI. There is no `therapeutic_agent` to curate.

The only forward-looking therapeutic statement in the literature is at the level of target biology, not a candidate drug:

> "Collectively, we reveal ZIP14 as a novel regulator of bone homeostasis, and that manipulating ZIP14 might be a therapeutic strategy for bone diseases." — PMID:29621230

Note carefully: that sentence proposes ZIP14 modulation for **common bone disease (osteoporosis)**, not as a treatment for HCI. The paper's framing is that the L438R mouse "mimic[s] the disparate actions of estrogen on cortical and trabecular bone through osteoblasts." Do not curate it as an HCI therapeutic lead.

### Supportive / rehabilitative

- Hearing rehabilitation: hearing aids, bone-conduction devices, cochlear implantation (limited value once the lesion is retrocochlear — preserved OAEs indicate cochlear function is intact but the nerve is the bottleneck), ABI as above.
- Vestibular rehabilitation for balance dysfunction / areflexia.
- Ocular surface protection and oculoplastic management for facial palsy (lagophthalmos, epiphora).
- Facial reanimation / physiotherapy for established facial paresis.
- Ophthalmological management of raised IOP.
- NCIT suggestions: `NCIT:C15315` Rehabilitation, `NCIT:C15747` Supportive Care, `NCIT:C15302` Physical Therapy — verify each label with OAK before binding.

### Experimental treatments

**No clinical trials.** A ClinicalTrials.gov search for hyperostosis cranialis interna returns no interventional studies; there are no NCT or ICTRP identifiers to curate for this disease.

### Treatment strategy

The one clear, citable algorithm statement:

> "Surgical decompression of the accessible impaired cranial nerves is advised in the early symptomatic period or even in the presymptomatic period in high-risk individuals." — PMID:20140965

Combined with the monitoring panel from PMID:23622937, the operational pathway is: genotype → serial CT + audiometry/BERA/vestibular/VEP/olfaction/IOP surveillance → decompress the accessible foramina at the earliest sign of encroachment → rehabilitate residual deficits.

---

## 13. Prevention

**Primary prevention of the disease itself is impossible** — it is a germline dominant mutation with no environmental component. Everything below is secondary or tertiary.

- **Primary prevention:** not applicable. No vaccination, no risk-factor modification.
- **Secondary prevention (early detection):** the core of management. **Cascade genetic testing** of at-risk relatives followed by presymptomatic CT and cranial-nerve function surveillance, so that decompression can be offered inside the intervention window.
- **Tertiary prevention (complication avoidance):** decompression to prevent irreversible nerve loss; corneal protection in facial palsy; IOP control; vestibular rehabilitation to prevent falls; ICP monitoring in severe disease.
- **Immunization:** not applicable.
- **Screening programmes:** no population or newborn screening; not appropriate for a single-kindred ultra-rare dominant disorder.
- **Genetic screening / reproductive options:** prenatal diagnosis and preimplantation genetic testing are technically available for a known familial `SLC39A14` variant. No published case of either in HCI; present them as available options, not as documented practice.
- **Risk stratification:** genotype is the stratifier. No clinical risk model exists.
- **Behavioural interventions:** none.
- **Genetic counselling:** indicated — autosomal dominant, 50% recurrence risk per pregnancy, high radiological penetrance with **variable clinical expressivity** (a counselling point that should be made explicitly: a gene-positive child cannot be told how severely they will be affected). NCIT suggestion: `NCIT:C15240` Genetic Counseling.
- **Public health / environmental interventions:** not applicable.
- **Prophylaxis:** the only "prophylaxis" in the literature is **prophylactic surgical decompression** in younger patients (PMID:19371457) — an aggressive recommendation resting on a single case, and worth curating with that caveat visible.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** No naturally occurring animal counterpart of HCI has been reported in any species. Human only (`NCBITaxon:9606`).
- **Breed (VBO):** not applicable — no companion-animal breed predisposition described.
- **Orthologous genes:** mouse `Slc39a14` (the residue equivalent to human L441 is **L438** — the mouse knock-in allele is L438R); zebrafish `slc39a14` (CRISPR nulls characterized in PMID:27231142 and in a 2020 bioRxiv study of manganese deficiency/hypersensitivity). Resolve NCBI Gene IDs for the orthologues before curating.
- **OMIA:** no OMIA entry corresponding to HCI.
- **Veterinary relevance:** none.
- **Comparative pathology:** the informative comparative finding is a **negative one** — the calvarial phenotype is *not* conserved in mouse (Section 15). Cranial vault ossification and the relative contribution of intramembranous ossification differ substantially between human and mouse, which is the leading explanation.
- **Evolutionary conservation:** ZIP14's metal-transport and cAMP-regulatory functions are conserved across vertebrates ("SLC39A14 functions as a pivotal manganese transporter in vertebrates" — PMID:27231142); the *skeletal site-specificity* of the HCI phenotype is not.
- **Zoonotic potential / cross-species transmission:** not applicable.

---

## 15. Model Organisms

### Mouse — conditional `Zip14` L438R knock-in (the HCI model)

**Design** (Hendrickx 2018, PMID:29621230): conditional knock-in overexpressing the mouse orthologous mutant `Zip14` L438R, driven by tissue-specific Cre:

| Cre driver | Target cell | Outcome |
|---|---|---|
| **Sox2-Cre** (ubiquitous) | all | **Perinatal lethality** — "ubiquitous expression of mutant Zip14 results in perinatal lethality" |
| **Runx2-Cre** | osteoblast lineage | Severe cortical bone phenotype (below) |
| **CtsK-Cre** | osteoclast lineage | Minimal skeletal effect |

**Osteoblast-specific (`Zip14^L438R` Ob-KI) phenotype, male mice, femur:**

| Parameter | Direction | p |
|---|---|---|
| Cortical thickness (Ct.Th) | ↑ | 6.0E-6 |
| Cortical porosity (Ct.Po) | ↓ | 0.0014 |
| Midshaft diameter (Ms.D) | ↓ | 4.1E-6 |
| Endosteal bone formation rate (BFR/BS) | ↑ | 0.0012 |
| Trabecular BV/TV | ↓ | 0.0071 |
| Trabecular number (Tb.N) | ↓ | 0.033 |
| Trabecular separation (Tb.Sp) | ↑ | 0.035 |
| Connectivity density (Conn.D) | ↓ | 0.018 |

> "Conditional knock-in mice overexpressing L438R Zip14 in osteoblasts have a severe skeletal phenotype marked by a drastic increase in cortical thickness due to an enhanced endosteal bone formation, resembling the underlying pathology in HCI patients. Remarkably, L438R Zip14 also generates an osteoporotic trabecular bone phenotype. The effects of osteoblastic overexpression of L438R Zip14 therefore mimic the disparate actions of estrogen on cortical and trabecular bone through osteoblasts." — PMID:29621230

### ⚠️ The model's central limitation — a `HUMAN_MODEL_MISMATCH`, not a knowledge gap

**The mouse reproduces the cellular mechanism (endosteal cortical thickening via osteoblasts) but does NOT reproduce the anatomical hallmark of the human disease (calvarial hyperostosis).** The authors say so explicitly. Full-text statements (PMID:29621230 — **re-verify as exact substrings before snippet use**):

- "we were surprised to see no calvarial phenotype as this is truly opposite of what we see in HCI patients"
- "loss of endogenous Zip14 did not affect the calvariae, even though the appendicular skeleton and vertebral column were osteoporotic"
- "aberrations in Zn homeostasis by Zip14 do not seem to affect calvariae of mice, even though the rest of the skeleton is affected"
- "Although calvarial porosity appears lower in these mice there were no significant differences in calvarial parameters"

This maps directly onto a dismech `discussions` entry with `kind: HUMAN_MODEL_MISMATCH`, and onto `modeled_mechanisms` links with **split relationships** on the same model:

```yaml
animal_models:
- name: Osteoblast-specific Zip14 L438R conditional knock-in mouse (Runx2-Cre)
  species: Mouse
  genotype: Zip14^fl(L438R); Runx2-Cre
  publication: PMID:29621230
  modeled_mechanisms:
  - target: Increased Endosteal Bone Formation
    relationship: RECAPITULATES
    fidelity: MODERATE
  - target: Calvarial and Skull Base Hyperostosis
    relationship: FAILS_TO_RECAPITULATE
    fidelity: LOW
    limitations: >-
      No significant calvarial thickness or porosity difference was observed in
      Runx2-Cre L438R knock-in mice, and loss of endogenous Zip14 likewise left
      the calvariae unaffected while the appendicular skeleton and vertebral
      column were osteoporotic. The craniofacial restriction that defines HCI in
      humans is absent from the mouse.
    evidence:   # required for FAILS_TO_RECAPITULATE
    - reference: PMID:29621230
      ...
```

Additional limitations to record: the knock-in is an **overexpression** construct (supraphysiological, unlike the human heterozygous single-copy allele); ubiquitous expression is perinatally lethal, so no whole-organism model of the human genotype exists; skull-base foramina and cranial-nerve entrapment cannot be modelled at all in mouse.

### Mouse — constitutive `Slc39a14` knockout (mechanism-supporting, not disease-modelling)

Two independent KO characterizations, both showing **the opposite bone phenotype**, which is what establishes that HCI is not a loss-of-function disease:

> "Mice lacking Slc39a14 (Slc39a14-KO mice) exhibit growth retardation and impaired gluconeogenesis, which are attributable to disrupted GPCR signaling in the growth plate, pituitary gland, and liver. The decreased signaling is a consequence of the reduced basal level of cyclic adenosine monophosphate (cAMP) caused by increased phosphodiesterase (PDE) activity in Slc39a14-KO cells. We conclude that SLC39A14 facilitates GPCR-mediated cAMP-CREB signaling by suppressing the basal PDE activity…" — Hojyo *et al.*, **PMID:21445361**

> "In this study, we thoroughly investigated the bone phenotypes of Zip14-KO mice, demonstrating that the KO mice exhibited osteopenia in both trabecular and cortical bones. In Zip14-KO mice, bone resorption was increased, whereas the bone formation rate was unchanged. Zip14 mRNA was expressed in normal osteoclasts both in vivo and in vitro, but receptor activator of NF-κB ligand (RANKL)-induced osteoclastogenesis was not impaired in bone marrow-derived macrophages prepared from Zip14-KO mice."
> — Sasaki S, Tsukamoto M, Saito M, Hojyo S, Fukada T, Takami M, Furuichi T. *FEBS Open Bio.* 2018;8(4):655–663. **PMID:29632817**, DOI:10.1002/2211-5463.12399

*(The Sasaki abstract as retrieved contains an apparent typographical artefact — "inhibiting bore resorption" — in its concluding sentence. Avoid quoting that sentence; the two sentences quoted above are clean.)*

**Curation note:** these KO mice are models of `SLC39A14` *biology*, **not** of HCI. Their `modeled_mechanisms` links, if curated at all, belong to the mechanism nodes about ZIP14/cAMP-CREB physiology with explicit `limitations` stating that the null allele produces the inverse skeletal phenotype.

### Zebrafish

CRISPR `slc39a14` null zebrafish show manganese dyshomeostasis and altered locomotor activity (PMID:27231142). **Relevant to the recessive manganese disease, not to HCI.** No zebrafish bone phenotype for the L441R-equivalent allele has been reported.

### In vitro / cellular models

The functional characterization in PMID:29621230 used transfected cell systems: ⁶⁵Zn uptake assays, FluoZin-3 labile-zinc imaging, subcellular localization with early/late endosome markers, and luciferase reporters for CRE and NFAT response elements. `evidence_source: IN_VITRO` for all of these.

**No iPSC, organoid, or patient-derived osteoblast model of HCI exists.** No CRISPR or RNAi functional-genomics screen has been run against this disease. No entry in DepMap, GenomeRNAi, or the Human Cell Atlas is disease-relevant here.

### Model resources

MGI (mouse `Slc39a14`, MGI gene page), IMPC/KOMP (constitutive KO alleles), ZFIN (`slc39a14`), Alliance of Genome Resources. The L438R conditional knock-in line is a **bespoke line from the Van Hul/Schinke laboratories** and is not, as far as can be determined, deposited in a public repository (IMSR/EMMA/MMRRC) — availability should be confirmed with the authors rather than assumed.

---

## Summary of high-value knowledge gaps for the KB entry

Ranked by curatable value:

1. **`HUMAN_MODEL_MISMATCH`** — the mouse knock-in reproduces endosteal cortical thickening but explicitly fails to reproduce calvarial hyperostosis, the defining lesion. Authors state they were "surprised." This is the single most important structured claim in the entry.
2. **Why craniofacial-only?** No mechanism explains why a ubiquitously expressed transporter produces a skeletal lesion confined to the skull. Intramembranous vs endochondral ossification and neural-crest vs mesoderm skull origin are the obvious hypotheses; neither has been tested.
3. **Serum/tissue zinc, manganese and iron have never been measured in HCI patients** — despite the allelic recessive disease being a metal-accumulation disease with a chelation therapy.
4. **Increased formation vs decreased resorption is unresolved** — the histology paper says "increased bone formation **or** decreased bone resorption"; the mouse implicates formation; the null implicates resorption. These are different mechanistic claims.
5. **No QoL, survival, or natural-history quantification** exists beyond n≈13 in one family.
6. **The single-family, single-variant evidence base.** One WES proband, one family, one ClinVar submission with "no assertion criteria provided" review status. High mechanistic confidence, low genetic-epidemiological confidence — and those should be recorded separately.
7. **The "death from decreased intracranial volume" claim** appears in the OMIM/Orphanet disease summaries but was not traced here to a primary case report. Verify before curating it as a mortality claim.

---

## Sources

- [OMIM #144755 — HYPEROSTOSIS CRANIALIS INTERNA; HCIN](https://omim.org/entry/144755)
- [OMIM #617013 — HYPERMANGANESEMIA WITH DYSTONIA 2](https://omim.org/entry/617013)
- [Orphanet: Hyperostosis cranialis interna (ORPHA:443098)](https://orpha.net/consor/cgi-bin/OC_Exp.php?Expert=443098&lng=EN) · [Orphanet-derived record, ORPHA:443098](https://chorobyrzadkie.gov.pl/en/disease_card/443098)
- [Manni JJ *et al.* Hyperostosis cranialis interna. A new hereditary syndrome with cranial-nerve entrapment. *NEJM* 1990 — PMID:2300107](https://pubmed.ncbi.nlm.nih.gov/2300107/)
- [Manni JJ *et al.* Eighth cranial nerve dysfunction in hyperostosis cranialis interna. *Acta Otolaryngol* 1992 — PMID:1575042](https://pubmed.ncbi.nlm.nih.gov/1575042/)
- [Waterval JJ *et al.* Phenotypic manifestations and management of HCI. *Am J Med Genet A* 2010 — PMID:20140965](https://onlinelibrary.wiley.com/doi/10.1002/ajmg.a.33205)
- [Waterval JJ *et al.* Facial nerve decompression via middle fossa approach for HCI. *J Laryngol Otol* 2009 — PMID:19371457](https://pubmed.ncbi.nlm.nih.gov/19371457/)
- [Waterval JJ *et al.* Bone metabolic activity in HCI measured with 18F-fluoride PET. *Eur J Nucl Med Mol Imaging* 2011 — PMID:21079950](https://pubmed.ncbi.nlm.nih.gov/21079950/)
- [Waterval JJ *et al.* Cerebral vasospasm after auditory brainstem implantation in HCI. *Clin Neurol Neurosurg* 2011 — PMID:21665359](https://pubmed.ncbi.nlm.nih.gov/21665359/)
- [Waterval JJ *et al.* Imaging features and progression of HCI. *AJNR* 2012 — PMID:22194361](https://www.ajnr.org/content/33/3/453)
- [Waterval JJ *et al.* Neurophysiologic, audiometric and vestibular function tests in HCI. *Clin Neurol Neurosurg* 2013 — PMID:23622937](https://www.sciencedirect.com/science/article/abs/pii/S030384671300108X)
- [Borra VM *et al.* Localization of the gene for HCI to chromosome 8p21. *Calcif Tissue Int* 2013 — PMID:23640157](https://pubmed.ncbi.nlm.nih.gov/23640157/)
- [Waterval JJ *et al.* Sclerosing bone dysplasias with involvement of the craniofacial skeleton. *Bone* 2014 — PMID:24325978](https://www.sciencedirect.com/science/article/abs/pii/S8756328213004912)
- [Hendrickx G *et al.* Conditional mouse models support the role of SLC39A14 (ZIP14) in HCI and in bone homeostasis. *PLoS Genet* 2018 — PMID:29621230](https://journals.plos.org/plosgenetics/article?id=10.1371%2Fjournal.pgen.1007321) · [PMC5903675](https://pmc.ncbi.nlm.nih.gov/articles/PMC5903675/)
- [Hojyo S *et al.* SLC39A14/ZIP14 controls GPCR-mediated signaling required for systemic growth. *PLoS One* 2011 — PMID:21445361](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0018059)
- [Sasaki S *et al.* Disruption of mouse Slc39a14 is associated with decreased bone mass. *FEBS Open Bio* 2018 — PMID:29632817](https://pubmed.ncbi.nlm.nih.gov/29632817/)
- [Tuschl K *et al.* Mutations in SLC39A14 disrupt manganese homeostasis and cause childhood-onset parkinsonism-dystonia. *Nat Commun* 2016 — PMID:27231142](https://www.nature.com/articles/ncomms11601) · [SLC39A14 Deficiency, GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK431123/)
- [Goodarzi A *et al.* Internal Acoustic Canal Stenosis Due to Hyperostosis. *J Neurol Surg B* 2020 — PMID:32499994](https://pubmed.ncbi.nlm.nih.gov/32499994/)
- [Alsaleh AS *et al.* HCI Presenting With Cerebrospinal Fluid Leak. *Cureus* 2025 — PMID:40091967](https://pubmed.ncbi.nlm.nih.gov/40091967/)
- [Otken E *et al.* Hyperostosis Fronto-Parieto-Occipitalis: A Cadaveric Case Report. *Cureus* 2023 — PMID:37546094](https://pubmed.ncbi.nlm.nih.gov/37546094/)
- [Bergen DJM *et al.* High Bone Mass Disorders. *JBMR* 2023 — PMID:36161343](https://doi.org/10.1002/jbmr.4715)
- [Huang T *et al.* Zinc Homeostasis in Bone: Zinc Transporters and Bone Diseases. *IJMS* 2020 — PMID:32059605](https://doi.org/10.3390/ijms21041236)
- [de Ruiter RD *et al.* Validation of quantitative [18F]NaF PET uptake parameters in bone diseases. *Ann Nucl Med* 2025 — PMID:39729191](https://doi.org/10.1007/s12149-024-01991-9)
- [ClinVar VCV000523143 — SLC39A14 c.1322T>G (p.Leu441Arg)](https://www.ncbi.nlm.nih.gov/clinvar/) · [NIH GTR: Hyperostosis cranialis interna (C1840404)](https://www.ncbi.nlm.nih.gov/gtr/conditions/C1840404/)
- [HGNC:20858 SLC39A14](https://rest.genenames.org/fetch/symbol/SLC39A14) · [UniProt Q15043 (ZIP14)](https://www.uniprot.org/uniprotkb/Q15043) · [HPO annotations for OMIM:144755](https://ontology.jax.org/) · [MONDO:0007765 via OLS4](https://www.ebi.ac.uk/ols4/ontologies/mondo)

---

**Next step:** if you want this turned into the YAML at `kb/disorders/Hyperostosis_Cranialis_Interna.yaml`, say the word and I'll run `just fetch-reference` for each PMID first so every snippet above is verified as an exact substring before it goes into an `evidence:` block — several of the Hendrickx full-text quotes in Sections 4, 6 and 15 came through a summarizing fetch and must be re-verified against the cache before use.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 39 |
| Resolved | 39 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 4 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 39 |
| On topic | 12 |
| Off topic | 3 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:794825` *(abstract only)*: "Dominant generalized cortical hyperostosis with multiple cranial nerve involvement"
  - closest text in source: "The authors report an observation of dominant generalized cortical hyperostosis with multiple and unilateral involvement of a certain number of cranial nerves"

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:21445361` (3 mentions) - The zinc transporter SLC39A14/ZIP14 controls G-protein coupled receptor-mediated signaling required for systemic growth.
  - shared terms: zip14
- `DOI:10.1038/ncomms11601` (1 mention) - Mutations in SLC39A14 disrupt manganese homeostasis and cause childhood-onset parkinsonism–dystonia
  - shared terms: patient, manganese
- `DOI:10.1152/ajpgi.00244.2022` (1 mention) - Enterocyte-specific deletion of metal transporter Zip14 (Slc39a14) alters intestinal homeostasis through epigenetic mechanisms
  - shared terms: zip14

Weighed against this report's own most characteristic terms: `hci`, `bone`, `disease`, `hyperostosis`, `zip14`, `nerve`, `affected`, `phenotype`, `interna`, `patient`, `normal`, `facial`, `dominant`, `family`, `vestibular`, `cranialis`, `waterval`, `manganese`, `allele`, `manni`.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 63 |
| Resolved | 59 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 3 |
| Terms whose name was checked | 39 |
| Terms named correctly | 39 |
| Terms named as a **different** term | 0 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0019933` (obsolete cAMP-mediated signaling) (1 mention)

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `OMIM`.

59 of 63 terms resolved to a current term; the rest could not be looked up either way.