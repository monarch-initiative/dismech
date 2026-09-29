---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-26T14:46:59.073379'
end_time: '2026-09-26T14:51:25.019496'
duration_seconds: 265.95
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Brugada syndrome
  mondo_id: MONDO:0015263
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
  web_search_requests: 14
  num_turns: 17
  total_cost_usd: 1.3111808
  session_id: 7b67d712-0ae8-4a84-90db-2000fb6a3b90
  stop_reason: end_turn
  assistant_text_blocks: 3
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
citation_count: 68
reference_validation:
  total_references: 37
  verified: 37
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 2
  quotes_valid: 0
  quotes_unsupported: 2
  unsupported_quote_references:
  - PMID:42123485
  relevance_assessed: 37
  on_topic: 26
  needs_review: true
  validator_version: 0.3.0rc3
term_validation:
  total_terms: 15
  verified: 13
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 7
  labels_matching: 5
  labels_variant: 2
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Brugada syndrome
- **MONDO ID:** MONDO:0015263 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Brugada syndrome** covering all of the
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

Brugada syndrome research report, in full.

I have sufficient material now to compile the full report.

Now I have comprehensive material to write the full report.

---

# Brugada Syndrome: Comprehensive Research Report

## 1. Disease Overview and Identifiers

Brugada syndrome (BrS) is an inherited primary electrical disease of the heart characterized by a distinctive coved (type 1) ST-segment elevation in the right precordial leads (V1–V3) on a 12-lead electrocardiogram (ECG), occurring in the absence of structural heart disease, and associated with an increased risk of polymorphic ventricular tachycardia, ventricular fibrillation (VF), and sudden cardiac death (SCD), typically during sleep or at rest ([GeneReviews — Brugada Syndrome, NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK1517/); [MedlinePlus Genetics](https://www.medlineplus.gov/genetics/condition/brugada-syndrome/)). It was first described as a distinct clinical entity by Pedro and Josep Brugada in 1992.

**Key identifiers:**
- **OMIM:** #601144 (BRGDA1) plus multiple additional locus entries (BRGDA2–BRGDA9+) corresponding to different causal/susceptibility genes ([OMIM #601144](https://omim.org/entry/601144))
- **MONDO:** MONDO:0015263
- **Orphanet:** ORPHA:130
- **ICD-10-CM:** I49.8 (other specified cardiac arrhythmias) — no dedicated Brugada-specific code
- **ICD-11:** BC9Z / related channelopathy codes
- **MeSH:** D053840 (Brugada Syndrome)

**Synonyms:** Brugada syndrome; BrS; sudden unexplained nocturnal death syndrome (SUNDS, historically linked, particularly in Southeast Asian populations); Pokkuri death syndrome (Japan); right bundle branch block, persistent ST elevation, and sudden death syndrome.

Most published data derive from aggregated disease-level resources (case series, registries such as BRAVO, SADS-TW, FINGER, PRELUDE, and large single- and multi-center cohorts) rather than a single unified EHR-based population; recent large ECG-based population studies (e.g., a 2024 Mayo Clinic 30-year retrospective of >5.3 million ECGs) provide the closest approximation to real-world, individual-level ascertainment ([Prevalence and Incidence of Type 1 Brugada Pattern: A 30-Year Experience at Mayo Clinic, 2024](https://www.sciencedirect.com/science/article/abs/pii/S0025619624003033)).

---

## 2. Etiology

### 2.1 Genetic Causal Factors

BrS is genetically heterogeneous. Although more than 20–23 genes have been reported in association studies, **SCN5A** (encoding the cardiac sodium channel α-subunit Nav1.5) remains the only gene with robust, clinically actionable evidence for causality, per ClinGen and expert consensus reviews ([Annual Review of Genomics and Human Genetics — The Genetics of Brugada Syndrome](https://www.sads.org/wp-content/uploads/2023/03/The-Genetics-of-Brugada-Syndrome.pdf)). SCN5A loss-of-function (LOF) variants are found in roughly **20–25% of clinically diagnosed BrS patients** ([Cureus 2024](https://www.cureus.com/articles/274198-identification-of-a-scn5a-genetic-variant-associated-with-type-1-brugada-syndrome-brs-in-a-family.pdf); [GeneReviews](https://www.ncbi.nlm.nih.gov/books/NBK1517/)).

Other genes historically implicated but with weaker or now-disputed evidence include:
- **SCN1B, SCN3B** (sodium channel β-subunits)
- **CACNA1C, CACNB2, CACNA2D1** (L-type calcium channel subunits — associated with a mixed Brugada/short-QT phenotype)
- **KCNE3, KCNJ8, KCND3** (potassium channel components affecting Ito)
- **GPD1L, HCN4, RANGRF, SLMAP, TRPM4, PKP2**

A large 2023–2025 gene-curation reappraisal by ClinGen substantially deflated the historical "23-gene panel" — most minor genes lack sufficient case-control or functional replication to be considered disease-causing, leaving SCN5A as the sole "definitive" gene ([European Journal of Human Genetics 2025](https://www.nature.com/articles/s41431-025-01972-0)).

### 2.2 Risk Factors

**Genetic risk factors:**
- SCN5A pathogenic LOF variants (missense, nonsense, frameshift, splice-site) causing reduced peak sodium current (INa)
- Common susceptibility SNPs at **SCN5A-SCN10A** (rs11708996, rs10428132) and near **HEY2** (rs9388451) — first identified in a 2013 GWAS ([Nature Genetics 2013](https://www.nature.com/articles/ng.2712); [PubMed 23872634](https://pubmed.ncbi.nlm.nih.gov/23872634/))
- A 2022 expanded GWAS meta-analysis of 2,820 BrS cases and 10,001 controls identified **21 association signals at 12 loci (10 novel)**, with strong SNP-heritability estimates supporting a substantially polygenic architecture layered on top of monogenic SCN5A disease ([SADS.org — 2022 Nature Genetics GWAS](https://www.sads.org/wp-content/uploads/2022/05/2-2022-Nature-Genetics-BrS.pdf))
- Male sex (prevalence 8–10-fold higher in men than women, attributed in part to greater Ito current density in men, androgen effects, and possibly differential Nav1.5 expression)
- Family history of BrS or unexplained sudden death, particularly at a young age

**Environmental/acquired risk factors:**
- **Fever** — the single most important acute trigger; fever-induced episodes occur in an estimated 20–30% of diagnosed BrS patients, and first clinical manifestation frequently occurs during a febrile illness, especially in children ([search synthesis of clinical literature](https://pubmed.ncbi.nlm.nih.gov/42123485/))
- Sodium-channel-blocking drugs (Class IA/IC antiarrhythmics, tricyclic antidepressants, some anesthetics/local anesthetics, cocaine)
- Excessive alcohol intake, cannabis use
- Electrolyte disturbances (hyperkalemia, hypokalemia)
- Vagotonic states, bradycardia (sleep, post-prandial states — explaining the classic nocturnal timing of events)

### 2.3 Protective Factors

Limited literature exists on protective genetic/environmental factors specific to BrS. Gain-of-function polymorphisms increasing INa density and lower Ito expression (relevant to the sex disparity) are inferentially protective; no dedicated protective-variant catalogue analogous to those for coronary disease exists. Avoidance of triggering drugs and prompt fever control are the primary modifiable "protective" behavioral measures ([BrugadaDrugs.org](https://www.brugadadrugs.org/)).

### 2.4 Gene-Environment Interactions

The clearest gene-environment interaction is the fever-Nav1.5 relationship: temperature-dependent destabilization of mutant Nav1.5 channel gating/inactivation kinetics (particularly for certain trafficking-defective or fast-inactivating SCN5A variants) unmasks or exacerbates the type 1 ECG pattern and arrhythmic risk during febrile states — "fever worsens sodium channel dysfunction by further reducing conductance" ([search synthesis](https://pubmed.ncbi.nlm.nih.gov/42123485/)). Drug-gene interactions are similarly central: sodium-channel-blocking agents unmask latent BrS in genetically susceptible individuals via pharmacologic provocation testing (ajmaline, flecainide, procainamide, pilsicainide), which is diagnostically exploited but also constitutes a real-world risk when such drugs are prescribed inadvertently.

---

## 3. Phenotypes

### 3.1 Clinical Signs / Electrocardiographic Phenotype

- **Type 1 Brugada ECG pattern** (the only diagnostic pattern): coved ST-segment elevation ≥2 mm in ≥1 right precordial lead (V1–V2, standard or superior intercostal placement), followed by a negative T wave, occurring spontaneously or after sodium-channel blocker provocation. HPO: consider **HP:0025145** (or general "abnormal ST segment"/ECG abnormality terms; BrS lacks a fully specific HPO leaf term for the type-1 coved pattern — bind to the most specific reachable descriptor).
- **Type 2/3 (saddleback) patterns** — non-diagnostic on their own; require provocation testing.
- **Syncope** (HP:0001279) — often due to self-terminating polymorphic VT.
- **Nocturnal agonal respiration** — a classical historical description in SUNDS-overlap cases.
- **Sudden cardiac death / aborted cardiac arrest** (HP:0001645-adjacent / cardiac arrest terms) — may be the first presentation in up to 1/3 of cases.
- **Palpitations** (HP:0001962).
- **Atrial fibrillation** — supraventricular arrhythmia comorbidity reported in ~10–20% of BrS cohorts.
- Conduction abnormalities: first-degree AV block, right bundle branch block-like QRS morphology, HV interval prolongation on electrophysiology study.

### 3.2 Phenotype Characteristics

- **Age of onset:** Typically manifests in adulthood, mean age of sudden death/arrhythmic event in the 3rd–4th decade of life (often cited ~40 years); pediatric presentations occur, usually fever-triggered.
- **Severity/frequency:** Highly variable expressivity — from asymptomatic ECG pattern carriers (common, especially among family members of probands) to malignant, recurrent VF/sudden death.
- **Progression:** Episodic — ECG pattern can be concealed at baseline and unmasked only during fever, drug challenge, or vagotonic states ("dynamic" pattern).
- **Sex disparity:** Prevalence and symptomatic expression are 8- to 10-fold higher in males than females.
- **Circadian pattern:** Arrhythmic events cluster during sleep/nocturnal hours and periods of vagal predominance.

### 3.3 Quality of Life Impact

Recurrent ICD shocks (appropriate and inappropriate) are a major quality-of-life burden and psychological stressor in BrS cohorts, driving interest in alternative therapies such as quinidine and catheter ablation to reduce shock burden — one driver of the 2023–2024 shift toward epicardial substrate ablation research ([BRAVO Registry, Circulation 2023](https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.122.063367)).

---

## 4. Genetic/Molecular Information

### 4.1 Causal Gene

**SCN5A** (HGNC:10593; chromosome 3p22.2) encoding **Nav1.5**, the pore-forming α-subunit of the cardiac voltage-gated sodium channel. LOF variants are found in ~20–25% of clinically diagnosed patients ([Karger MPP 2024 review](https://karger.com/mpp/article/32/1/1/835624/The-SCN5A-Gene-Is-a-Predictor-of-Phenotype)).

### 4.2 Variant Classification and Functional Consequences

- Variant types: missense (most common), nonsense, frameshift, splice-site, and occasionally large deletions.
- Functional consequence: predominantly **loss of function** — reduced peak INa via decreased channel trafficking to the membrane, accelerated inactivation, delayed recovery from inactivation, or reduced single-channel conductance.
- A 2024–2025 systematic review/meta-analysis (17 studies, 3,568 BrS patients, 3,030 genotyped) confirmed that LOF-type SCN5A variants (versus non-LOF or normal-function variants) are associated with **worse arrhythmic prognosis**, though the discriminative power is described as only "weak-to-moderate," insufficient for standalone risk stratification ([SCN5A variant type-dependent risk prediction in Brugada syndrome, PMC 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11844247/); [ResearchGate meta-analysis 2024](https://www.researchgate.net/publication/379815880_SCN5A_gene_variants_and_arrhythmic_risk_in_Brugada_Syndrome_an_updated_systematic_review_and_meta-analysis)).
- ACMG/ClinVar classification varies widely by variant; functional electrophysiological studies (patch-clamp, heterologous expression) are frequently required to adjudicate variants of uncertain significance (VUS).

### 4.3 Common/Susceptibility Variants (Polygenic Component)

- **rs11708996** (SCN5A intronic), **rs10428132** (SCN10A), **rs9388451** (near HEY2) — the three GWAS-validated common risk SNPs from the original 2013 discovery cohort, combined into a **BrS polygenic risk score (BrS-PRS)** — likelihood of BrS increases consistently with increasing risk-allele count ([Circulation: Genomic and Precision Medicine, SADS-TW validation, PMC](https://www.ahajournals.org/doi/10.1161/CIRCGEN.119.002797); [PubMed 32490690](https://pubmed.ncbi.nlm.nih.gov/32490690/)).
- The expanded 2022 GWAS (2,820 cases/10,001 controls) found **21 signals across 12 loci**, and demonstrated that in 2,182 unrelated BrS patients, higher PRS was independently associated with a significantly greater risk of a first life-threatening arrhythmic event since birth — supporting reconceptualization of BrS as a partly polygenic, SCN5A-independent-susceptibility disease ([search synthesis, 2022 Nature Genetics](https://www.sads.org/wp-content/uploads/2022/05/2-2022-Nature-Genetics-BrS.pdf)).

### 4.4 Modifier/Regulatory Genes

- **HEY2** — a Notch-pathway bHLH transcription factor specifically expressed in developing ventricular myocardium; indispensable for ventricular myocyte differentiation, chamber identity, and cardiac morphogenesis. GWAS association with BrS implicates altered transcriptional regulation of ion-channel gene expression during cardiac development, rather than a structural channel defect per se.
- **SCN10A** encodes **Nav1.8**, historically considered a neuronal channel, but shown to modestly contribute to cardiac INa; LOF SCN10A variants reduce cardiac sodium current.
- Established transcriptional regulators of Nav1.5/ion-channel expression relevant to BrS susceptibility: **HEY2, TBX20, GATA4, TBX5, IRX3/IRX5**.
- **WT1** — a 2025 preprint identified WT1 as impacting SCN5A expression and cardiac conduction, a novel candidate modifier ([bioRxiv 2025](https://www.biorxiv.org/content/10.1101/2025.01.16.633330.full.pdf)).
- A rare non-coding **enhancer variant in SCN5A** was described (medRxiv, 2023) contributing to unusually high BrS prevalence in Thailand — a population-specific regulatory mechanism ([medRxiv 2023](https://www.medrxiv.org/content/10.1101/2023.12.19.23299785.full.pdf)).

### 4.5 Epigenetics

Dedicated epigenetic (DNA methylation/histone) studies specific to BrS are sparse in the literature relative to other cardiomyopathies; the primary "epigenetic-adjacent" finding is the transcriptional-regulation angle via HEY2/GATA4/TBX5, i.e., altered developmental gene-regulatory programming of ion channel expression rather than classical postnatal epigenetic marks.

### 4.6 Chromosomal Abnormalities

BrS is not typically associated with large structural chromosomal rearrangements; it is a channelopathy driven by point variants/small indels in ion channel and channel-regulatory genes, not copy-number disorders.

---

## 5. Environmental Information (Triggers and Phenocopy Causes)

### 5.1 True Trigger Factors (in genetically susceptible individuals)

- **Fever/febrile illness** — the dominant modifiable trigger (see §2.4). Recommended: "12-lead ECG is strongly recommended even in a low-grade fever state in patients belonging to a high-risk group" ([search synthesis](https://pubmed.ncbi.nlm.nih.gov/42123485/)).
- Sodium-channel-blocking drugs across classes: Class IA (ajmaline, procainamide, disopyramide), Class IC (flecainide, propafenone, pilsicainide), tricyclic/tetracyclic antidepressants, some anesthetics/local anesthetics, lithium, and certain anticonvulsants (e.g., lacosamide, implicated in at least one case report during septicemia — [PMC 2021](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8104292/)).
- Cocaine, cannabis, excessive alcohol intake.
- Vagotonic states (rest, sleep, the post-prandial period) — mechanistically linked to the nocturnal predominance of events.
- Electrolyte disturbances (hyperkalemia).

### 5.2 Brugada Phenocopy — Reversible, Non-Congenital Mimics

Distinct from true BrS, "Brugada phenocopy" describes reversible Brugada-pattern ECGs arising from an acute, identifiable, non-genetic cause, with normalization once the underlying condition resolves ([World Journal of Cardiology 2014, PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3964189/)). Documented causes include:
- Electrolyte abnormalities (notably **hyponatremia** — case report/review, PMC 2025: [Brugada Phenocopy due to Hyponatremia](https://pmc.ncbi.nlm.nih.gov/articles/PMC11882121/); also hyperkalemia)
- **Pulmonary embolism** (right ventricular strain/mechanoelectrical feedback) ([PubMed 36645685](https://pubmed.ncbi.nlm.nih.gov/36645685/); [PubMed 23465226](https://pubmed.ncbi.nlm.nih.gov/23465226/))
- Mechanical compression of the right ventricle/RVOT (mediastinal tumors, pectus excavatum — [PMC 2021](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8308929/))
- Myocardial ischemia or coronary vasospasm
- Myocarditis/pericarditis, and infective processes such as **empyema** ([PMC 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12358182/))
- Poor ECG lead placement/filter artifact (a technical, not physiologic, phenocopy)

This distinction (phenocopy vs. true congenital BrS) is the basis for the differential-diagnosis addition just made to the Brugada_Syndrome.yaml entry in this repository's working branch.

### 5.3 Infectious Agents

No infectious agent is causal for true BrS; infection acts only indirectly via fever as a trigger, or via phenocopy mechanisms (myocarditis, sepsis-associated electrolyte/metabolic derangement).

---

## 6. Mechanism / Pathophysiology

### Causal chain (numbered, from initiating lesion to clinical manifestation)

1. A germline **SCN5A** (or, less commonly, another ion-channel/channel-regulatory gene) loss-of-function variant **reduces functional Nav1.5 channel density or gating efficiency** at the cardiomyocyte membrane, via impaired trafficking, accelerated inactivation, or reduced conductance.
2. This **reduces peak inward sodium current (INa)**, most prominently in the **right ventricular epicardium and RVOT**, a region with intrinsically lower INa density and higher transient outward potassium current (Ito) density than the endocardium or left ventricle ("interventricular differences in sodium current" — [PMC 2018](https://pmc.ncbi.nlm.nih.gov/articles/PMC6046646/)).
3. Reduced INa, combined with relatively unopposed Ito-mediated phase-1 repolarization, causes **loss of the action potential (AP) "dome"** in a subpopulation of RVOT epicardial cells — this occurs **heterogeneously**, not uniformly, across the epicardial surface.
4. Heterogeneous dome loss produces marked **transmural and epicardial dispersion of repolarization** between adjacent sites that retain versus lose the AP dome (the "repolarization hypothesis," now the better-supported of the two classical mechanistic hypotheses — [Cardiovascular Research review; JSR literature review 2024](https://www.jsr.org/hs/index.php/path/article/view/1444)).
5. The voltage gradient between dome-maintaining and dome-losing regions drives **electrotonic current flow ("current-load mismatch")**, which manifests on the surface ECG as the **coved ST-segment elevation** in V1–V3 (type 1 Brugada pattern) — this is the mechanistic substrate for the diagnostic ECG sign itself.
6. Under further destabilizing conditions (fever, sodium-channel-blocking drugs, vagotonic bradycardia), the dome can propagate from a site where it is maintained into an adjacent site where it has been lost, generating a local re-excitation event via **phase 2 reentry** (Yan and Antzelevitch, 1999) — a closely coupled extrasystole arising from the epicardial dispersion substrate ([PMC — Basis for Tissue-Level Phase-2 Reentry](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4637010/)).
7. When three functionally distinct regions coexist in 2D/3D myocardial tissue (a region of delayed dome, a region of lost dome, and normal epicardium), the phase-2-reentrant extrasystole can degenerate into **sustained reentrant circuits**, producing **polymorphic ventricular tachycardia** that can deteriorate into **ventricular fibrillation**.
8. VF causes **hemodynamic collapse and, if untreated, sudden cardiac death** — the terminal clinical manifestation of the pathway; events cluster during sleep/vagal-predominant states because vagotonia further reduces INa/ICa,L balance and favors dome loss.

**Branch — the depolarization/structural hypothesis (partially supported, competing/complementary):** In parallel, an alternative or contributory mechanism proposes that conduction delay in the RVOT — attributable to region-specific **myocardial fibrosis and reduced connexin-43 gap-junction density**, sometimes with abnormal neural crest cell migration during development — produces fractionated, delayed local activation that itself generates the ST-elevation pattern and arrhythmic substrate independent of, or in addition to, dome-loss repolarization abnormalities ([Cardiovascular Research, Amsterdam UMC](https://pure.amsterdamumc.nl/en/publications/pathophysiological-mechanisms-of-brugada-syndrome-depolarization-); [ScienceDirect 2010](https://www.sciencedirect.com/science/article/abs/pii/S0022282810002762)). Current consensus (2024 literature) leans toward the **repolarization hypothesis as the predominant/best-experimentally-supported mechanism**, based on genetically engineered experimental models reproducing the phenotype, while acknowledging the depolarization/current-load-mismatch and structural (fibrosis/connexin) contributions are not mutually exclusive and likely coexist to varying degrees across patients ("depolarization disorder, repolarization disorder, or more?" — [Oxford Academic Cardiovascular Research](https://academic.oup.com/cardiovascres/article/67/3/367/505399)).

**Ajmaline's mechanism (relevant to diagnostic provocation and disease modeling):** Beyond pure INa blockade, ajmaline also modulates potassium and calcium currents and mitochondrial/metabolic pathways; combined sodium- and calcium-current blockade in experimental models reproduces loss of the epicardial AP dome, ST elevation, phase 2 reentry, and spontaneous polymorphic VT/VF — an effect that can be normalized by 4-aminopyridine (an Ito blocker), directly implicating Ito in the repolarization mechanism ([Frontiers in Cardiovascular Medicine 2021](https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2021.782596/pdf?isPublishedV2=false)).

### Molecular/cellular detail relevant to curation

- **Molecular pathway/GO terms:** cardiac muscle cell action potential (GO:0086001); regulation of cardiac muscle cell membrane repolarization; sodium ion transmembrane transport (GO:0035725); ventricular cardiac muscle cell action potential (GO:0086005).
- **Protein dysfunction:** Nav1.5 (UniProt Q14524) misfolding/trafficking defect or altered gating kinetics; a subset of variants are dominant-negative, reducing wild-type channel surface expression via heteromultimerization.
- **Cell types (CL terms):** cardiac ventricular epicardial myocyte (relevant CL terms for right ventricular/RVOT cardiomyocyte); Purkinje fiber cells have also been implicated as an arrhythmogenic trigger source in some substrate-mapping studies.
- **Tissue damage/structural correlate:** Epicardial mapping studies (BRAVO, UNCOVER(BrS)) directly visualize a fibrotic, low-voltage, fractionated-electrogram arrhythmogenic substrate localized to the anterior RVOT epicardium in symptomatic patients — the direct anatomic target of catheter ablation therapy ([Heart Rhythm 2016](https://www.heartrhythmjournal.com/article/S1547-5271(16)30555-0/fulltext)).
- **Single-cell/omics:** No large-scale single-cell transcriptomic atlas specific to human BrS myocardium was identified in this search; most molecular profiling data derive from iPSC-CM electrophysiology and heterologous expression systems rather than patient-tissue omics.

---

## 7. Anatomical Structures Affected

- **Organ level:** Heart — primarily right ventricle, specifically the **right ventricular outflow tract (RVOT)** epicardium; this is the near-universal localization of both the ECG abnormality and the ablatable arrhythmogenic substrate.
- **System:** Cardiovascular system.
- **Tissue/cell level:** Ventricular epicardial myocardium (RVOT); Purkinje conduction system component in some substrate models.
- **Subcellular level:** Plasma membrane (Nav1.5 channel localization, particularly lateral/T-tubule membrane subdomains — a 2020 study found specific decrease of Na+ channel expression on the lateral membrane of cardiomyocytes causes fatal arrhythmias in BrS, [PMC 2020](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7673036/)).
- **Localization/laterality:** Right-sided/RVOT predominant — the electrical and structural abnormality is not diffusely biventricular, a key anatomic feature distinguishing it from most cardiomyopathies. UBERON: right cardiac ventricle; cardiac outflow tract.

---

## 8. Temporal Development

- **Onset:** Typically adult-onset clinically (mean age at first arrhythmic event roughly 40 years), though the underlying channelopathy is congenital/present from birth; pediatric presentation occurs, usually fever-triggered, and neonatal/infant presentations are described but less common.
- **Onset pattern:** Episodic/paroxysmal — clinical events (syncope, VF) are discrete, unpredictable episodes rather than a continuous progressive process.
- **Course:** The ECG phenotype itself can be **dynamic/concealed**, fluctuating between normal, type 2/3, and type 1 patterns depending on autonomic tone, temperature, and drug exposure — this "concealed" nature complicates diagnosis and longitudinal risk assessment.
- **Progression:** Not a degenerative or progressive structural disease in the classic sense (no progressive myocardial loss/scarring analogous to cardiomyopathies), though the epicardial fibrotic substrate identified on mapping may itself be age- or disease-duration related in some patients.
- **Critical periods:** Febrile illness (especially in childhood), and periods of high vagal tone (sleep, rest, post-prandial) represent windows of heightened arrhythmic vulnerability.

---

## 9. Inheritance and Population Genetics

### 9.1 Epidemiology

- **ECG pattern prevalence:** ~0.12–0.8% of the general population shows a Brugada-type ECG pattern (mostly non-diagnostic type 2/3) ([search synthesis](https://pubmed.ncbi.nlm.nih.gov/29844648/)).
- **Syndrome prevalence:** Commonly cited as **~1:2,000 to 1:5,000**, with regional variation.
- A 2024 Mayo Clinic 30-year retrospective of **5,381,186 ECGs from 2,304,809 patients** found 150 patients with at least one ECG showing a type 1 Brugada pattern — of these, **76.0% met BrS criteria, 62.0% were spontaneous, 18.7% fever-induced, and 10.7% drug-induced** ([Mayo Clinic study, 2024](https://www.sciencedirect.com/science/article/abs/pii/S0025619624003033)).
- A 2024 community-based ECG screening study from Kerala, South India found overall Brugada-pattern prevalence of 1.06% (0.04% type I, 1.01% type II/III) ([doaj.org, Indian Heart Journal 2024](https://doaj.org/article/cb232f09f31349ad9c27dfde0bf5b210)).
- Higher background prevalence is reported in **Southeast Asia** (Thailand, Philippines, Japan), historically overlapping with the sudden unexplained nocturnal death syndrome (SUNDS) literature; a 2023 study attributes part of Thailand's elevated prevalence to a population-enriched SCN5A regulatory (enhancer) variant ([medRxiv 2023](https://www.medrxiv.org/content/10.1101/2023.12.19.23299785.full.pdf)).

### 9.2 Inheritance Pattern

- **Autosomal dominant** in the majority of monogenic (SCN5A-positive) cases; the exception is **KCNE5-related BrS**, inherited in an **X-linked** manner ([search synthesis of GeneReviews content](https://www.medlineplus.gov/genetics/condition/brugada-syndrome/)).
- **Mendelian (autosomal dominant) transmission is detectable in fewer than 25% of all clinically confirmed cases** — the majority of cases either lack an identifiable monogenic cause or reflect a more complex, partly polygenic architecture (the SCN5A-SCN10A-HEY2 common-variant burden plus the broader 2022 GWAS 12-locus signal) ([Annual Review of Genomics and Human Genetics summary](https://www.sads.org/wp-content/uploads/2023/03/The-Genetics-of-Brugada-Syndrome.pdf)).
- **Penetrance:** Reduced and age- and sex-dependent; even within SCN5A-positive families, many mutation carriers remain asymptomatic throughout life, and expressivity is highly variable — "reduced penetrance and variable expressivity are hallmarks of Brugada syndrome."
- **Sex ratio:** ~8–10:1 male predominance in symptomatic disease expression, despite equal transmission of the causal variant to both sexes.
- **Founder effects:** Documented in specific populations (e.g., the Thai SCN5A enhancer variant).

### 9.3 Population Demographics

- Higher prevalence/clinical recognition in East and Southeast Asian populations relative to European-ancestry populations.
- Predominantly diagnosed in **young to middle-aged males** (peak clinical presentation 30s–40s).
- Family/cascade screening is standard once a proband is identified, given autosomal dominant transmission and the value of identifying at-risk relatives before a sentinel arrhythmic event.

---

## 10. Diagnostics

### 10.1 Diagnostic ECG Criteria

- **Type 1 Brugada pattern** — coved ST elevation ≥2 mm in ≥1 of V1–V2 (standard or high intercostal-space lead placement), spontaneously or after provocation — is the **only ECG pattern considered diagnostic**.
- **Pharmacologic provocation testing:** Used when resting ECG shows a non-diagnostic (type 2/3, saddleback) pattern in a patient with clinical suspicion. **Intravenous ajmaline is the preferred agent** internationally, though its limited availability (particularly in the US) has driven increased use of **oral or IV flecainide**; procainamide and pilsicainide are also used ([search synthesis](https://pubmed.ncbi.nlm.nih.gov/42123485/)). A 2023 diagnostic refinement — the **r′-wave algorithm** — was proposed to help predict a positive sodium-channel-blocker provocation test result ([PMC 2023](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10056571/)).
- **Fever provocation:** A spontaneous or fever-induced type 1 pattern is itself diagnostic; a 12-lead ECG is recommended during febrile episodes in patients from high-risk families or with a suggestive history. A 2025 MDPI paper specifically examined **type 1 Brugada pattern triggered by low-grade fever** and its diagnostic/risk-stratification implications ([MDPI IJMS 2025](https://www.mdpi.com/1422-0067/27/9/3900); [PubMed 42123485](https://pubmed.ncbi.nlm.nih.gov/42123485/)).

### 10.2 Genetic Testing

- Single-gene (SCN5A) or targeted arrhythmia/channelopathy gene panel testing is recommended following a clinical BrS diagnosis, primarily to enable **cascade family screening**.
- Given only ~20–25% diagnostic yield for SCN5A and the now-limited actionable-gene list post-ClinGen reappraisal, a negative genetic test does **not** exclude BrS, and genetic results should not independently drive risk stratification or ICD decisions.
- Whole-exome/genome sequencing is used mainly in research or when panel testing is non-diagnostic in a strongly phenotype-positive family.

### 10.3 Electrophysiology Study / Risk Stratification Testing

- **Programmed ventricular stimulation (PVS):** Historically used for risk stratification; a pooled analysis found induced arrhythmia was associated with cardiac events during follow-up (HR 2.66), greatest with single/double extrastimuli ([PubMed 26797467](https://pubmed.ncbi.nlm.nih.gov/26797467/)). However, more recent literature (2024–2025) questions its predictive value in specific subgroups — PVS did **not** predict cardiac events in elderly BrS patients in a large Japanese cohort ([PMC 2025](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11931591/)), and current guidelines do not support PVS specifically in **drug-induced type 1** BrS, where SCD risk stratification remains especially challenging. A commentary explicitly asks whether PVS risk prediction is "closing time" ([Revista Española de Cardiología 2021](https://www.revespcardiol.org/en-programmed-electrophysiological-stimulation-for-risk-articulo-S1885585721003686)).
- **Non-invasive ECG risk markers (2024–2025 focus):** β-angle, fragmented QRS, S wave in lead I, early repolarization pattern, the aVR sign, and quantified transmural dispersion of repolarization have shown predictive value for arrhythmic events and are increasingly emphasized as adjuncts/alternatives to invasive PVS ([Frontiers in Cardiovascular Medicine 2025 mini-review](https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2025.1722105/full); [Journal of Interventional Cardiac Electrophysiology 2025](https://link.springer.com/article/10.1007/s10840-025-02101-z)).

### 10.4 Differential Diagnosis

Distinguishing true congenital BrS from **Brugada phenocopy** (see §5.2) is a core diagnostic step — phenocopies are reversible and resolve with treatment of the underlying cause (correcting electrolytes, treating PE, draining an effusion/empyema, resolving ischemia), whereas true BrS is a lifelong genetic predisposition requiring ongoing risk management.

---

## 11. Outcome/Prognosis

- BrS is a recognized major cause of **sudden cardiac death in patients under 50 years old**, particularly in populations without coronary artery disease.
- **Overall risk stratification remains a major unmet clinical challenge** — the majority of BrS carriers (especially those identified through family screening, without prior symptoms) have a relatively benign course, while a minority experience life-threatening arrhythmic events, and current tools imperfectly separate these groups ([Frontiers in Cardiovascular Medicine 2025](https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2025.1722105/full)).
- **Established higher-risk features:** spontaneous (vs. drug-induced) type 1 pattern, prior aborted cardiac arrest or documented VF, unexplained syncope, family history of sudden death, male sex, and (per 2024 JACC data) certain **nonmodifiable risk factors** shown to independently predict outcomes ([JACC 2024](https://www.jacc.org/doi/10.1016/j.jacc.2024.07.037); [JACC 2024 — Risk Stratification: Selecting the Population of Interest](https://www.jacc.org/doi/10.1016/j.jacc.2024.08.076)).
- **ICD complication burden:** A major driver of current management controversy — ICDs are highly effective at preventing SCD but are associated with substantial complication rates (inappropriate shocks, lead failure, infection) in this typically younger patient population, motivating research into risk-stratified, ICD-sparing strategies (quinidine, catheter ablation).

---

## 12. Treatment

### 12.1 Device Therapy

- **Implantable cardioverter-defibrillator (ICD)** remains the only therapy with proven mortality benefit in high-risk BrS patients (recurrent VF, aborted SCD, high-risk PVS/ECG markers). NCIT: consider `NCIT:C15329` (Surgical Procedure) for implantation, with `therapeutic_modality: DEVICE`.

### 12.2 Pharmacotherapy

- **Quinidine** (Class IA antiarrhythmic, Ito blocker) — Class IIa indication for BrS patients with electrical storm or recurrent appropriate ICD shocks; shown to significantly reduce shock burden in patients with malignant ventricular arrhythmia episodes ([JACC 2016](https://www.jacc.org/doi/10.1016/j.jacc.2016.01.042); [Circulation](https://www.ahajournals.org/doi/10.1161/01.cir.0000143159.30585.90)). CHEBI: quinidine (CHEBI:28593).
- **Isoproterenol** (IV infusion) — used acutely for electrical storm suppression by increasing ICa,L and restoring the epicardial AP dome.
- **Antipyretics** — prompt fever treatment is considered one of the most effective, low-risk preventive interventions in BrS patients ([BrugadaDrugs.org](https://www.brugadadrugs.org/)).
- **Drugs to avoid** (comprehensively catalogued at BrugadaDrugs.org, a physician-curated reference): sodium-channel blockers including **ajmaline, flecainide, propafenone, procainamide, pilsicainide, allapinin, ethacizin**; certain tricyclic antidepressants; cocaine; excessive alcohol; and, per case reports, agents such as **lacosamide** in the context of critical illness ([Medscape treatment overview](https://emedicine.medscape.com/article/163751-treatment); [PMC 2021 lacosamide case](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8104292/)).

### 12.3 Catheter Ablation (Major Area of 2023–2025 Development)

Epicardial substrate ablation targeting the anterior RVOT arrhythmogenic substrate has emerged as an important adjunct/alternative therapy, particularly for ICD-refractory or ICD-refusing patients:

- **BRAVO Registry** (Brugada Ablation of VF Substrate Ongoing Multicenter Registry, Circulation 2023): catheter ablation of the epicardial substrate is safe and effective at preventing VF recurrence in high-risk BrS patients; VF burden fell from 1.1 ± 2.1 episodes/month pre-ablation to 0.003 ± 0.14 episodes/month post-ablation (p < 0.0001) ([Circulation 2023](https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.122.063367)).
- A 2024 study of patients with symptomatic BrS who **declined ICD implantation** found catheter ablation (performed in 66.7% of the cohort) associated with significantly better arrhythmic outcomes than ICD alone (primary outcome 5.6% vs. 54.5%, log-rank p = 0.012) over a median 46.2-month follow-up ([EP Europace 2024](https://academic.oup.com/europace/article/26/1/euad318/7330978)).
- **UNCOVER(BrS) study** (2024) demonstrated feasibility and preliminary safety of epicardial substrate ablation via a **hybrid mini-thoracotomy** approach, with no symptomatic arrhythmic recurrences at 12-month follow-up ([PMC 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC12604058/)).
- A 2023 systematic review/meta-analysis discusses the "future direction" of substrate-based ablation across inherited primary arrhythmia syndromes including BrS ([Journal of Arrhythmia 2023](https://onlinelibrary.wiley.com/doi/full/10.1002/joa3.12947)).
- Ongoing debate: whether RVOT epicardial substrate ablation should become **standard of care** in high-risk BrS remains actively discussed in the literature ([PMC commentary](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10824472/)).

### 12.4 Genetic/Precision Approaches

- A registered clinical trial (**NCT07039123**) is evaluating a **polygenic risk score to optimize primary prevention (ICD candidacy) in intermediate-risk BrS populations** — an active translational research direction bridging the 2022 GWAS findings into clinical decision-making ([ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT07039123)).

---

## 13. Prevention

- **Primary prevention:** Avoidance of known pharmacologic and physiologic triggers (sodium-channel-blocking drugs, cocaine, excessive alcohol); prompt antipyretic treatment of fever.
- **Secondary prevention:** Cascade genetic and clinical (ECG ± provocation) screening of first-degree relatives of a BrS proband, given autosomal-dominant transmission.
- **Genetic counseling:** Recommended for all confirmed BrS families given the dominant inheritance pattern, reduced penetrance, and variable expressivity — counseling should explicitly address that a child's risk of inheriting a familial pathogenic variant may functionally translate to less than full disease expression due to penetrance/environmental modifiers.
- **Risk stratification-guided prophylaxis:** ICD implantation in confirmed high-risk patients (prior VF/aborted SCD); quinidine as pharmacologic prophylaxis in select intermediate/high-risk patients or those with recurrent ICD shocks.
- **Public health / point-of-care:** Physician and patient education resources (e.g., BrugadaDrugs.org) function as a de facto prophylactic tool by preventing inadvertent prescription of triggering medications.

---

## 14. Other Species / Comparative Biology

No robust naturally occurring veterinary BrS phenotype analogous to the human disease is well established in the literature surveyed; most cross-species data come from engineered models rather than natural companion-animal or wildlife disease. Orthologous *Scn5a* is well conserved across mammals (mouse, canine, porcine), enabling the modeling described below, but naturally occurring inherited canine/feline Brugada-like disease was not identified in this search.

---

## 15. Model Organisms

- **Murine (mouse) models:** *Scn5a* knockout or knock-in of specific human BrS-associated point mutations are used to replicate a generic or family-specific BrS phenotype; heterozygous *Scn5a*-null mice reproduce conduction slowing and arrhythmia susceptibility, though homozygous knockout is embryonic lethal ([search synthesis](https://pmc.ncbi.nlm.nih.gov/articles/PMC6539778/)).
- **Zebrafish (*Danio rerio*) models:** Increasingly used given cardiac electrophysiological similarities to humans; valuable both for gene-editing (CRISPR) disease modeling and for chemical/drug screening in BrS ([Reviews in Cardiovascular Medicine 2024](https://www.imrpress.com/journal/RCM/25/9/10.31083/j.rcm2509313); [PMC 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11440409/)).
- **Human iPSC-derived cardiomyocytes (iPSC-CMs):** Considered the best current in vitro model for complex inherited arrhythmia syndromes like BrS because they retain the patient's genetic background; used to study Nav1.5 trafficking/gating defects, drug responses, and to test candidate therapeutics ([IJMS 2021, PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8001521/); [PubMed 33802229](https://pubmed.ncbi.nlm.nih.gov/33802229/)).
- **Heterologous expression systems:** HEK293 cells transfected with wild-type or mutant SCN5A/Nav1.5 constructs remain the primary system for detailed biophysical/patch-clamp characterization of variant functional consequences (used to classify VUS as LOF, GOF, or neutral).
- **Model limitations:** Species-specific differences in cardiac electrophysiology (e.g., differing ion channel current densities and repolarization reserve between rodents and humans) limit direct translational extrapolation from murine models; iPSC-CMs, while patient-specific, retain relative electrophysiological immaturity (fetal-like phenotype) compared to adult human cardiomyocytes, a limitation widely acknowledged in the iPSC-CM literature.

---

## Summary of Key Ontology Term Suggestions for Curation

| Domain | Suggested term |
|---|---|
| Disease | MONDO:0015263 (Brugada syndrome) |
| Causal gene | hgnc:10593 (SCN5A) |
| Modifier/susceptibility loci | SCN10A (hgnc:10582), HEY2 (hgnc:16116) |
| Phenotype | Syncope (HP:0001279); Ventricular fibrillation (HP:0001663); Sudden death (search HPO for exact leaf term) |
| Molecular function | protein-coding voltage-gated sodium channel activity (GO:0005248) |
| Biological process | cardiac muscle cell action potential (GO:0086001); ventricular cardiac muscle cell action potential (GO:0086005) |
| Cell type | cardiac ventricular myocyte (search CL for RV/epicardial specificity) |
| Anatomy | right cardiac ventricle / right ventricular outflow tract (UBERON) |
| Chemical/drug | quinidine (CHEBI:28593); flecainide, ajmaline (as trigger/provocation agents) |
| Treatment | NCIT:C15986 (Pharmacotherapy) + therapeutic_agent quinidine; NCIT surgical/device term for ICD; catheter ablation term |

---

## Sources

- [Identification of a SCN5A Genetic Variant Associated With Type 1 Brugada Syndrome (BrS) in a Family, Cureus 2024](https://www.cureus.com/articles/274198-identification-of-a-scn5a-genetic-variant-associated-with-type-1-brugada-syndrome-brs-in-a-family.pdf)
- [Revisiting the prognostic role of SCN5A in Brugada syndrome, PubMed](https://pubmed.ncbi.nlm.nih.gov/38901522)
- [SCN5A variant type-dependent risk prediction in Brugada syndrome, PMC 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11844247/)
- [SCN5A gene variants and arrhythmic risk in Brugada Syndrome: an updated systematic review and meta-analysis](https://www.researchgate.net/publication/379815880_SCN5A_gene_variants_and_arrhythmic_risk_in_Brugada_Syndrome_an_updated_systematic_review_and_meta-analysis)
- [The SCN5A Gene Is a Predictor of Phenotype Severity in Brugada Syndrome, Karger MPP 2024](https://karger.com/mpp/article/32/1/1/835624/The-SCN5A-Gene-Is-a-Predictor-of-Phenotype)
- [SCN5A Mutation Type and a Genetic Risk Score Associate Variably With Brugada Syndrome Phenotype in SCN5A Families, Circ Genom Precis Med](https://www.ahajournals.org/doi/10.1161/CIRCGEN.120.002911)
- [Brugada Syndrome — GeneReviews, NCBI Bookshelf](https://www.ncbi.nlm.nih.gov/books/NBK1517/)
- [Two hypotheses of Brugada Syndrome – Repolarization and Depolarization: Literature Review, JSR 2024](https://www.jsr.org/hs/index.php/path/article/view/1444)
- [The pathophysiological mechanism underlying Brugada syndrome: Depolarization versus repolarization, ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0022282810002762)
- [Pathophysiological mechanisms of Brugada syndrome: Depolarization disorder, repolarization disorder, or more?, Cardiovascular Research](https://academic.oup.com/cardiovascres/article/67/3/367/505399)
- [Basis for the Induction of Tissue-Level Phase-2 Reentry as a Repolarization Disorder in the Brugada Syndrome, PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4637010/)
- [The Mechanism of Ajmaline and Thus Brugada Syndrome: Not Only the Sodium Channel!, Frontiers 2021](https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2021.782596/pdf?isPublishedV2=false)
- [Interventricular differences in sodium current and its potential role in Brugada syndrome, PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6046646/)
- [Specific decreasing of Na+ channel expression on the lateral membrane of cardiomyocytes causes fatal arrhythmias in Brugada syndrome, PMC 2020](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7673036/)
- [Prevalence and Incidence of Type 1 Brugada Pattern: A 30-Year Experience at Mayo Clinic, ScienceDirect 2024](https://www.sciencedirect.com/science/article/abs/pii/S0025619624003033)
- [Worldwide Prevalence of Brugada Syndrome: A Systematic Review and Meta-Analysis, PubMed](https://pubmed.ncbi.nlm.nih.gov/29844648/)
- [Indian Heart Journal, Jan 2024, DOAJ](https://doaj.org/article/cb232f09f31349ad9c27dfde0bf5b210)
- [Brugada Syndrome Risk Stratification: Selecting the Population of Interest, JACC 2024](https://www.jacc.org/doi/10.1016/j.jacc.2024.08.076)
- [Nonmodifiable Risk Factors Predict Outcomes in Brugada Syndrome, JACC 2024](https://www.jacc.org/doi/10.1016/j.jacc.2024.07.037)
- [Brugada Syndrome: From Molecular Mechanisms and Genetics to Risk Stratification, MDPI IJMS 2023](https://www.mdpi.com/1422-0067/24/4/3328)
- [Validation and Disease Risk Assessment of Previously Reported Genome-Wide Genetic Variants Associated With Brugada Syndrome, Circ Genom Precis Med](https://www.ahajournals.org/doi/10.1161/CIRCGEN.119.002797)
- [Genome-wide association analyses identify new Brugada syndrome risk loci, Nature Genetics 2022](https://www.sads.org/wp-content/uploads/2022/05/2-2022-Nature-Genetics-BrS.pdf)
- [Common variants at SCN5A-SCN10A and HEY2 are associated with Brugada syndrome, Nature Genetics 2013](https://www.nature.com/articles/ng.2712)
- [A rare non-coding enhancer variant in SCN5A contributes to the high prevalence of Brugada syndrome in Thailand, medRxiv 2023](https://www.medrxiv.org/content/10.1101/2023.12.19.23299785.full.pdf)
- [The Brugada syndrome associated gene WT1 impacts on SCN5A expression and cardiac conduction, bioRxiv 2025](https://www.biorxiv.org/content/10.1101/2025.01.16.633330.full.pdf)
- [Type 1 Brugada Pattern Triggered by Low-Grade Fever: Implications for Diagnosis and Risk Stratification, MDPI/PubMed](https://www.mdpi.com/1422-0067/27/9/3900)
- [The r'-Wave Algorithm: A New Diagnostic Tool to Predict the Diagnosis of Brugada Syndrome after a Sodium Channel Blocker Provocation Test, PMC 2023](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10056571/)
- [Clinical Management of Brugada Syndrome: Commentary From the Experts, Circ Arrhythm Electrophysiol](https://www.ahajournals.org/doi/10.1161/CIRCEP.123.012072)
- [Long-Term Outcomes of Brugada Substrate Ablation, BRAVO Registry, Circulation 2023](https://www.ahajournals.org/doi/10.1161/CIRCULATIONAHA.122.063367)
- [Outcomes of catheter ablation in high-risk patients with Brugada syndrome refusing an ICD, EP Europace 2024](https://academic.oup.com/europace/article/26/1/euad318/7330978)
- [Hybrid mini-thoracotomy for Brugada syndrome: epicardial substrate characterization and ablation — UNCOVER(BrS) study, PMC 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC12604058/)
- [Future direction of substrate-based catheter ablation in Brugada syndrome, J Arrhythm 2023](https://onlinelibrary.wiley.com/doi/full/10.1002/joa3.12947)
- [Is right ventricular outflow tract epicardial substrate ablation the standard of care in high-risk Brugada syndrome?, PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10824472/)
- [Programmed Ventricular Stimulation for Risk Stratification in the Brugada Syndrome: A Pooled Analysis, PubMed](https://pubmed.ncbi.nlm.nih.gov/26797467/)
- [Risk stratification of elderly patients with Brugada syndrome, PMC 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11931591/)
- [Programmed electrophysiological stimulation for risk prediction in patients with Brugada syndrome: closing time?, Rev Esp Cardiol](https://www.revespcardiol.org/en-programmed-electrophysiological-stimulation-for-risk-articulo-S1885585721003686)
- [Shock Reduction With Long-Term Quinidine in Patients With Brugada Syndrome, JACC 2016](https://www.jacc.org/doi/10.1016/j.jacc.2016.01.042)
- [Efficacy of Quinidine in High-Risk Patients With Brugada Syndrome, Circulation](https://www.ahajournals.org/doi/10.1161/01.cir.0000143159.30585.90)
- [Beyond the type 1 pattern: comprehensive risk stratification in Brugada syndrome, J Interv Card Electrophysiol 2025](https://link.springer.com/article/10.1007/s10840-025-02101-z)
- [MINI REVIEW, Frontiers in Cardiovascular Medicine 2025](https://www.frontiersin.org/journals/cardiovascular-medicine/articles/10.3389/fcvm.2025.1722105/full)
- [Zebrafish as a Model System for Brugada Syndrome, PMC 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11440409/)
- [iPSC-Cardiomyocyte Models of Brugada Syndrome—Achievements, Challenges and Future Perspectives, PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8001521/)
- [Experimental Models of Brugada syndrome, PMC](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6539778/)
- [Entry #601144 BRUGADA SYNDROME 1; BRGDA1, OMIM](https://omim.org/entry/601144)
- [Brugada Syndrome: an exemplar for the genomic basis of sudden death, European Journal of Human Genetics 2025](https://www.nature.com/articles/s41431-025-01972-0)
- [The Genetics of Brugada Syndrome, Annual Review of Genomics and Human Genetics](https://www.sads.org/wp-content/uploads/2023/03/The-Genetics-of-Brugada-Syndrome.pdf)
- [Brugada syndrome: MedlinePlus Genetics](https://www.medlineplus.gov/genetics/condition/brugada-syndrome/)
- [Potential antiarrhythmic drugs in Brugada syndrome patients, BrugadaDrugs.org](https://www.brugadadrugs.org/antiarrhythmic/)
- [Drugs to be avoided by Brugada syndrome patients, BrugadaDrugs.org](https://www.brugadadrugs.org/avoid/)
- [Lacosamide induced Brugada I morphology in the setting of septicemia, PMC 2021](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8104292/)
- [Brugada Syndrome Treatment & Management, Medscape](https://emedicine.medscape.com/article/163751-treatment)
- [Brugada Phenocopy due to Hyponatremia: A Case Report and Review of the Literature, PMC 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11882121/)
- [Beyond the Pleura: A Case Report of Type 1 Brugada Phenocopy in the Setting of Empyema, PMC 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12358182/)
- [Brugada phenocopy: A new electrocardiogram phenomenon, World J Cardiol / PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3964189/)
- [Brugada phenocopy in pulmonary embolism, PubMed](https://pubmed.ncbi.nlm.nih.gov/36645685/)
- [Pectus excavatum with brugada phenocopy electrocardiogram, PMC 2021](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8308929/)
- [Brugada Phenocopy in the context of pulmonary embolism, PubMed](https://pubmed.ncbi.nlm.nih.gov/23465226/)
- [Polygenic Risk Score for Optimizing Primary Prevention in Intermediate-Risk Populations, ClinicalTrials.gov NCT07039123](https://clinicaltrials.gov/study/NCT07039123)

## Reference Validation

Checked with `linkml-reference-validator` 0.3.0rc3.

| Outcome | Count |
| --- | --- |
| References checked | 37 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 2 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 2 |
| References weighed for topical relevance | 37 |
| On topic | 26 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

Every one of these was searched against an abstract alone, with no full text retrieved - marked *abstract only* below. Where full text can be fetched, re-running with it will settle them; where the source publishes only a summary to PubMed, as GeneReviews chapters do, it will not, and the quote has to be checked by hand against the chapter itself.

- `PMID:42123485` *(abstract only)*: "fever worsens sodium channel dysfunction by further reducing conductance"
  - closest text in source: "Fever worsens sodium channel dysfunction, as elevated temperature further reduces their conductance"
- `PMID:42123485` *(abstract only)*: "12-lead ECG is strongly recommended even in a low-grade fever state in patients belonging to a high-risk group"
  - closest text in source: "During the patient's subfebrile episodes, 12-lead ECG recordings revealed ST-segment elevations in leads V1-V3"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 15 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 7 |
| Terms named correctly | 5 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 2 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0086001` (2 mentions) - the report calls it "Molecular pathway/GO terms:** cardiac muscle cell action potential"; GO calls it **cardiac muscle cell action potential**
- `GO:0005248` (1 mention) - the report calls it "protein-coding voltage-gated sodium channel activity"; GO calls it **voltage-gated sodium channel activity**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.

13 of 15 terms resolved to a current term; the rest could not be looked up either way.