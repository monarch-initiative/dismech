---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-31T23:11:39.035836'
end_time: '2026-08-31T23:24:22.214256'
duration_seconds: 763.18
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Hypertrophic Cardiomyopathy 14
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
  - claude-opus-5[1m]
  web_search_requests: 7
  num_turns: 67
  total_cost_usd: 5.406228499999999
  session_id: 50074fff-d34e-4341-a8a5-3295b22eb76b
  stop_reason: end_turn
  permission_denials: 5
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
citation_count: 27
reference_validation:
  total_references: 24
  verified: 24
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 24
  on_topic: 14
  validator_version: 0.2.1
term_validation:
  total_terms: 82
  verified: 79
  not_found: 0
  obsolete: 0
  unverifiable: 3
  confabulation_rate: 0.0
  labels_checked: 25
  labels_matching: 22
  labels_variant: 3
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
- **Disease Name:** Hypertrophic Cardiomyopathy 14
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Hypertrophic Cardiomyopathy 14** covering all of the
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

# Hypertrophic Cardiomyopathy 14 (CMH14 / MYH6-attributed HCM)

**Research report for dismech KB entry `kb/disorders/Hypertrophic_Cardiomyopathy_14.yaml`**
Compiled 2026-08-31. All PMIDs below were fetched into `references_cache/` and quotes are exact abstract/full-text substrings unless marked otherwise.

---

## ⚠ Headline finding — read before curating

**The gene–disease relationship this entry is named for has been formally *disputed*.** OMIM 613251 (CMH14) and MONDO:0013197 ("Any hypertrophic cardiomyopathy in which the cause of the disease is a mutation in the MYH6 gene") were minted from two reports totalling three probands. The ClinGen Hereditary Cardiovascular Disease Gene Curation Expert Panel downgraded MYH6–HCM from **Limited** to **Disputed** on 2023-07-12 and reaffirmed that in JACC in 2025.

> "This classification was originally approved by the ClinGen Hypertrophic Cardiomyopathy Gene Curation Expert Panel on November 1, 2017, with a classification of 'Limited'. It was reevaluated by the ClinGen Hereditary Cardiovascular Disease Gene Curation Expert Panel on July 12, 2023. As a result of this reevaluation, the classification was changed from 'Limited' to 'Disputed' due to absence of new compelling genetic and experimental evidence."
> — `CGGV:assertion_ee5380a4-0dee-49aa-b911-141502648144-2023-07-12T020000.000Z` (already cached in this worktree)

> "The mechanism for disease remains unknown."
> — same record

This is not a peripheral caveat; it determines how nearly every section below must be written. **Curation recommendation:** curate CMH14 as a *disputed nosological entity* — a real MONDO/OMIM concept whose clinical validity has been retracted by expert review — rather than as a mechanism-bearing disease. Concretely:

- Every pathophysiology node beyond "rare heterozygous MYH6 missense variant in a person meeting HCM criteria" is **inferred by analogy to MYH7**, not demonstrated for MYH6, and should say so in `description` and carry `directness: INDIRECT`.
- The strongest evidence in the file will be the ClinGen `CGGV:` assertion and the JACC reappraisal (`PMID:39971408`), not the original case reports.
- A `discussions:` entry with `kind: KNOWLEDGE_GAP` attached to `pathophysiology#` is the honest home for the mechanism.
- Consider whether the correct dismech disposition is a stub `entry_type: OUT_OF_SCOPE` or a `has_subtypes`/`mappings` note on `Hypertrophic_Cardiomyopathy` rather than a standalone entry. That call is a curator's, not mine — but the evidence base does not support an independent mechanism entry.

---

## 1. Disease Information

### Overview

Hypertrophic cardiomyopathy 14 (CMH14) is the MYH6-attributed member of the numbered OMIM hypertrophic cardiomyopathy series. It denotes hypertrophic cardiomyopathy — unexplained left ventricular hypertrophy, classically asymmetric and septal, not explained by loading conditions — in a person carrying a heterozygous missense variant in *MYH6*, encoding the α (alpha) heavy chain of cardiac myosin. It is not a clinically distinguishable entity: no CMH14-specific phenotype, imaging finding, natural history, or treatment exists. Its only definitional feature is the genotype, and that genotype–phenotype link is the disputed one.

The concept traces to exactly two publications:

- **Niimura et al., *Circulation* 2002** (PMID:11815426) — one MYH6 missense variant (R795Q) among 31 patients with elderly-onset HCM.
- **Carniel et al., *Circulation* 2005** (PMID:15998695) — one MYH6 missense variant (Q1065H) in 1 of 21 HCM probands.

ClinGen's tally: *"It has been associated with HCM in 3 probands in 2 publications. Four unique heterozygous missense variants have been reported in humans with limited evidence to support their pathogenicity."*

### Key identifiers

| Resource | Identifier |
|---|---|
| MONDO | **MONDO:0013197** — "hypertrophic cardiomyopathy 14" |
| OMIM (phenotype) | **613251** — CARDIOMYOPATHY, FAMILIAL HYPERTROPHIC, 14; CMH14 |
| OMIM (gene) | **160710** — MYH6 |
| HGNC | **hgnc:7576** — MYH6 (note lowercase prefix per repo convention) |
| NCBI Gene | 4624 |
| Ensembl | ENSG00000197616 |
| UniProt | P13533 (MYH6_HUMAN, myosin-6 / α-MHC) |
| Cytogenetic location | 14q11.2 |
| RefSeq transcript | NM_002471.4 |
| Orphanet | **No dedicated code.** Closest is ORPHA:217569 (familial isolated hypertrophic cardiomyopathy). Orphanet does not maintain per-gene HCM numbers. |
| ICD-10 | I42.1 (obstructive HCM), I42.2 (other HCM) |
| ICD-11 | BC43.0 (hypertrophic cardiomyopathy) |
| MeSH | D002312 "Cardiomyopathy, Hypertrophic, Familial" |
| Parent MONDO | MONDO:0005045 (hypertrophic cardiomyopathy) |

### Synonyms

CMH14; cardiomyopathy, familial hypertrophic, 14; hypertrophic cardiomyopathy caused by mutation in MYH6; MYH6-related hypertrophic cardiomyopathy; α-myosin heavy chain hypertrophic cardiomyopathy. (The existing YAML synonym list is correct.)

### Provenance of the underlying information

**Aggregated disease-level resources plus a very small number of individual case reports.** There is no EHR cohort, registry, or biobank study of CMH14 as such — the total human evidence base is 3 probands. The most informative sources are meta-level: the ClinGen curation record, the Walsh et al. case-vs-control burden analysis (PMID:27532257), and gnomAD population frequencies.

---

## 2. Etiology

### Disease causal factors

**Asserted:** heterozygous missense variation in *MYH6* (14q11.2), autosomal dominant, acting on the α-cardiac myosin heavy chain motor.

**Actual evidentiary status:** the causal claim does not survive contemporary gene-level burden analysis. Walsh et al. (PMID:27532257) compared variant burden in cardiomyopathy cases against ExAC and reported for MYH6 an excess-variant odds ratio of **1.06 (95% CI 0.34–3.34)** with an etiological fraction of **0.06 (0.00–0.70)** — i.e. indistinguishable from background. The paper names MYH6 explicitly as one of the offenders:

> "For example, MYBPC3, MYH6, and SCN5A have all been reported to be major contributors to DCM but show little or no excess burden despite adequate numbers and power; instead, we see that these are in fact genes that have the highest background variation."
> — Walsh et al., *Genet Med* 2017 (PMID:27532257)

This is the mechanistic crux: *MYH6 carries an unusually high rate of rare missense variation in unselected populations* (gnomAD v4 pLI = 0, LOEUF ≈ 0.63; it is not LoF-constrained), so a rare MYH6 missense allele found in an HCM proband is a weak observation. The A1004S variant, reported in DCM, sits at ~1.1% in the general population (Anfinson et al. 2022, PMID:35621855) — far commoner than the disease.

ClinGen also discounted the Carniel proband on exactly this ground: *"Additional missense variants have been reported in humans, but were not scored because probands have variants in another HCM gene (Rubattu et al. 2016… Liu et al. 2021… Suzuki et al. 2022), or high frequency in the population (Carniel et al. 2005)."*

### Genetic risk factors

**Candidate causal variants (the entire reported set for HCM):**

| Variant | cDNA | Domain | Source | Current ClinVar status |
|---|---|---|---|---|
| p.Arg795Gln | c.2384G>A, rs267606907 | head/converter region | Niimura 2002 (PMID:11815426) | **Uncertain significance** (VarID 14147; 5/6 submitters VUS; OMIM's 2002 "Pathogenic" no longer contributes). gnomAD exomes AF 0.00004; TOPMed 0.00002 |
| p.Gln1065His | c.3195G>C, rs267606904 | S2/tail | Carniel 2005 (PMID:15998695) | **Conflicting** (VarID 14149; 6 VUS + 3 likely benign). gnomAD overall AF ≈ 0.00015; ~0.1% in East Asian ancestry (ExAC) |
| MYH6-rs372446459 | — | — | Liu 2021 (PMID:34087240) | Co-occurred with TNNT2-rs397516484 in the same proband — not scorable in isolation |
| p.Lys364fs (c.1091_1092insTGAA) | frameshift | head | Suzuki 2022 (PMID:35911064) | Co-occurred with MYH7 p.Pro731Thr — the MYH7 allele is the parsimonious explanation |

Rubattu et al. (PMID:27483260) found MYH6 variants in 3/41 (7.5%) of identified variants in a 70-patient Italian NGS cohort, and noted a distribution signal worth recording:

> "The distribution of the identified gene mutations was similar between the two groups with the exceptions of MYH6 and TNNT2. In fact, mutations in MYH6 were identified in the LO group only, whereas mutations in TNNT2 were identified in the EO group only."
> — Rubattu et al. 2016 (PMID:27483260), late-onset (≥65 y) vs early-onset (≤25 y)

This converges with Niimura's original elderly-onset finding and is the *only* replicated phenotypic association in the literature: to whatever extent MYH6 variants associate with HCM at all, they do so in **late-onset, family-history-negative** disease — the phenotype for which the causal prior is weakest and phenocopy risk highest.

**Susceptibility / modifier loci:** none established for CMH14. The general HCM modifier landscape (common-variant polygenic scores, hypertension, sarcomere-negative status) applies non-specifically and is not MYH6-informed.

**Related MYH6 gene–disease relationships (ClinGen, HGNC:7576)** — these are the important nosological neighbours and *should* be recorded in the entry, because they show the gene is real even where the HCM link is not:

| Disease | MONDO | MOI | ClinGen classification | Date |
|---|---|---|---|---|
| MYH6-related congenital heart defects | MONDO:0800442 | AD | **Definitive** | 2023-05-09 |
| Dilated cardiomyopathy 1EE | MONDO:0013198 | AD | Limited | 2026-03-04 |
| **Hypertrophic cardiomyopathy** | MONDO:0005045 | AD | **Disputed** | 2023-07-12 |

MYH6 also carries a well-replicated arrhythmia association outside ClinGen's HCM curation — see §3.

### Environmental risk factors

None specific to CMH14. Generic HCM modifiers of phenotype expression: age, systemic hypertension (`HP:0000822`), athletic conditioning (a diagnostic confounder rather than a cause), obesity, and male sex. None have been studied in MYH6 carriers.

### Protective factors

**Not established.** No protective MYH6 allele is described. Guideline-era HCM care (ICD for primary prevention, septal reduction, myosin inhibitors) modifies outcome but is disease-level, not genotype-level.

### Gene–environment interactions

**Not applicable / not studied for CMH14.** No GxE literature exists for MYH6 in HCM. Note one genuinely interesting environmental observation for the *gene*: Gorza et al. (PMID:6234108) showed that chronic haemodynamic overload shifts human **atrial** MHC composition toward β, i.e. the α-MHC content of the tissue where MYH6 actually dominates is itself load-dependent. That is a mechanism-relevant load–isoform interaction, but it has never been tested against MYH6 genotype.

---

## 3. Phenotypes

**There is no CMH14-specific phenotype.** The phenotype list below is the OMIM 613251 clinical synopsis and the HCM phenotype in general. Frequencies are HCM-level, not MYH6-level, and must be curated with that qualifier — the 3-proband evidence base cannot support any frequency claim.

### Core cardiac phenotypes (all `category: Cardiovascular`)

| Phenotype | HP term | Onset | Severity | Course | Frequency (HCM overall) |
|---|---|---|---|---|---|
| Hypertrophic cardiomyopathy | `HP:0001639` Hypertrophic cardiomyopathy | 3rd–8th decade (per OMIM 613251) | Variable | Progressive | Definitional |
| Left ventricular hypertrophy | `HP:0001712` Left ventricular hypertrophy | as above | Max wall thickness 19.9 ± 3.8 mm in the Niimura elderly cohort | Progressive | Definitional |
| Asymmetric septal hypertrophy | `HP:0001670` Asymmetric septal hypertrophy | as above | Variable | Progressive | Majority |
| Systolic anterior motion of mitral valve / LVOT obstruction | *(no clean HP term; use `preferred_term` + `HP:0001653` Mitral regurgitation for the consequence)* | as above | SAM in 58% of Niimura cohort; LVOT gradient mean 63 ± 42.8 mmHg in 11 patients | Dynamic, load-dependent | ~1/3 at rest in HCM broadly |
| Exertional dyspnea | `HP:0002875` Exertional dyspnea | Adult | Mild–severe | Progressive | Most common presenting symptom |
| Chest pain / angina | `HP:0100749` Chest pain; `HP:0001681` Angina pectoris | Adult | Variable | Episodic, exertional | Common |
| Syncope | `HP:0001279` Syncope; `HP:0031972` Presyncope | Adult | Variable | Episodic | ~15–25% in HCM |
| Palpitations | `HP:0001962` Palpitations | Adult | Mild–moderate | Episodic | Common |
| Atrial fibrillation | `HP:0005110` Atrial fibrillation | Adult, rises with age | Moderate | Paroxysmal → persistent | ~20% lifetime in HCM |
| Left atrial enlargement | `HP:0031295` Left atrial enlargement | Adult | — | Progressive | Common |
| Ventricular arrhythmia / VT | `HP:0004308` Ventricular arrhythmia; `HP:0004756` Ventricular tachycardia | Adult | Severe | Episodic | NSVT ~20–30% on monitoring |
| Sudden cardiac death | `HP:0001645` Sudden cardiac death | Any age | Fatal | Acute | ~0.5%/yr contemporary HCM |
| Congestive heart failure | `HP:0001635` Congestive heart failure | Late | Severe | Progressive | Minority; end-stage |
| Myocardial fibrosis | `HP:0001685` Myocardial fibrosis | Adult | — | Progressive | LGE on CMR in ~60% |
| Cardiac arrest | `HP:0001695` Cardiac arrest | Any | Fatal/near-fatal | Acute | Minority |

**OMIM 613251 clinical synopsis phenotype set**, per the entry: ventricular hypertrophy (often asymmetric, involving the interventricular septum); dyspnea; syncope; collapse; palpitations; chest pain — exercise-triggered. Age of onset third to eighth decade. Variability within and between families, "ranging from benign to malignant forms with a high risk of cardiac failure and sudden cardiac death."

### The MYH6-specific phenotype signals that *are* real (and are not HCM)

These belong in the entry as differential/context, not as CMH14 phenotypes:

**Sick sinus syndrome (`HP:0011704`)** — the single best-supported MYH6 human phenotype association:

> "A missense variant in this gene, c.2161C>T, results in the conceptual amino acid substitution p.Arg721Trp, has an allelic frequency of 0.38% in Icelanders and associates with sick sinus syndrome with an odds ratio = 12.53 and P = 1.5 × 10⁻²⁹. We show that the lifetime risk of being diagnosed with sick sinus syndrome is around 6% for non-carriers of c.2161C>T but is approximately 50% for carriers."
> — Holm et al., *Nat Genet* 2011 (PMID:21378987)

Also `HP:0001688` Sinus bradycardia, `HP:0012722` Heart block.

**Atrial septal defect (`HP:0001631`)** — the ClinGen **Definitive** MYH6 relationship:

> "The underlying mutation is a missense substitution, I820N, in alpha-myosin heavy chain (MYH6), a structural protein expressed at high levels in the developing atria, which affects the binding of the heavy chain to its regulatory light chain."
> — Ching et al., *Nat Genet* 2005 (PMID:15735645)

**Hypoplastic left heart syndrome with reduced RV EF** — recessive/compound-heterozygous MYH6:

> "Secondary family-based filtering for de novo and recessive variants revealed rare inherited missense mutations on both paternal and maternal alleles of MYH6… in 2 patients who developed right ventricular dysfunction 3 to 11 years postoperatively. Parents and siblings who were heterozygous carriers had normal echocardiograms."
> — Theis et al., *Circ Cardiovasc Genet* 2015 (PMID:26085007)

**Dilated cardiomyopathy (`HP:0001644`)** — Carniel's *same* paper that supplied the HCM proband found three DCM probands (P830L, A1004S, E1457K), and framed MYH6 as a pleiotropic locus:

> "This study suggests that mutations in MYH6 may cause a spectrum of phenotypes ranging from DCM to HCM."
> — Carniel et al. 2005 (PMID:15998695)

That pleiotropy claim, read alongside the burden data, is better explained as non-specific rare variation than as a genuine allelic series.

### Quality-of-life impact

No CMH14-specific QoL data. HCM-level: the disease-specific instrument is the **Kansas City Cardiomyopathy Questionnaire (KCCQ-23/KCCQ-CSS)**, used as a primary or key secondary endpoint in EXPLORER-HCM and SEQUOIA-HCM; generic instruments are SF-36 and EQ-5D. Dominant QoL drivers in HCM are exertional limitation, ICD-related anxiety and shock burden, activity restriction, and reproductive/family-screening distress. **Not available for CMH14 specifically — do not curate a per-phenotype QoL claim.**

---

## 4. Genetic / Molecular Information

### Causal gene

***MYH6*** (myosin heavy chain 6, cardiac muscle, alpha), `hgnc:7576`, OMIM 160710, 14q11.2, transcript NM_002471.4, protein NP_002462.2 / UniProt P13533 (1939 aa). It lies head-to-head with *MYH7* (β-MHC) in a tandem gene cluster; the two proteins are ~93% identical, which is exactly why the MYH7 mechanistic literature has been borrowed to explain MYH6 and exactly why that borrowing is unsafe.

Weiss et al. sequenced the whole family and drew the relevant conclusion about how these isoforms differ:

> "Results indicate that functional diversity among MyHCs is likely to be accomplished by having small pockets of sequence diversity in an otherwise highly conserved molecule."
> — Weiss et al., *J Mol Biol* 1999 (PMID:10388558) — cited by ClinGen as part of the (limited) experimental support

### Pathogenic variants

Covered in §2. Key point for the KB: **not one MYH6 variant is currently classified Pathogenic or Likely Pathogenic for HCM by any ClinVar submitter applying ACMG/AMP criteria.** The two OMIM allelic variants are VUS (R795Q) and conflicting-VUS/likely-benign (Q1065H). Curate `functional_impact_category` as **absent or `UNKNOWN`**, not `GAIN_OF_FUNCTION` — the schema's `FunctionalImpactEnum` should not be used to assert a consequence nobody has demonstrated.

- **Variant type/class:** missense throughout (one reported frameshift, p.Lys364fs, in a proband also carrying an MYH7 variant).
- **Somatic vs germline:** germline only. No somatic role; MYH6 is not a COSMIC/cancer gene in this context.
- **Population frequency:** see table in §2. The population-genetic signature is the diagnostic problem — MYH6 is not LoF-constrained (gnomAD v4 pLI 0, LOEUF ≈ 0.63) and carries high background missense variation.
- **Functional consequences:** unknown for the HCM-reported alleles. The functional work that exists is on *other* MYH6 alleles from *other* phenotypes (see §6).

### Modifier genes

None established. What the literature actually shows is **oligogenic confounding rather than modification**: two of the four HCM-reported MYH6 probands also carried a variant in a definitive HCM gene (TNNT2, MYH7). Suzuki et al. argued the double hit drives severity —

> "Family members with the double variants demonstrated severe phenotypes, such as sudden cardiac-related death and heart failure. These double variants were well segregated and might be responsible for the severity of cardiovascular events in affected family members."
> — Suzuki et al., *J Cardiol Cases* 2022 (PMID:35911064)

— but ClinGen declined to score these, and the parsimonious reading is that the definitive-gene allele is causal and MYH6 is a passenger. If dismech curates this, `relationship_type: MODIFIER` on the MYH6 `genetic:` entry with an explicit `notes:` stating the alternative interpretation would be honest; asserting modification would not.

### Epigenetic information

**Not available for CMH14.** No methylation, histone, or chromatin study addresses MYH6 variant carriers. The MYH6/MYH7 locus is under well-characterised developmental and hormonal (thyroid hormone) transcriptional control and is regulated by the *Mir-208a* intronic miRNA within Myh6, plus antisense/lncRNA regulation of the MYH7/MYH6 switch — but this is isoform-switch biology, not CMH14 epigenetics. Do not curate as disease mechanism.

### Chromosomal abnormalities

**Not applicable.** No CNV, translocation, or aneuploidy mechanism; ClinGen records **no dosage-sensitivity curation** for MYH6 (0 classifications), so haploinsufficiency and triplosensitivity are both unassessed.

---

## 5. Environmental Information

- **Environmental factors:** none identified. No toxicological, radiation, occupational, or pollutant association with CMH14 (CTD has no MYH6–HCM environmental interaction of note).
- **Lifestyle factors:** high-intensity competitive athletics is relevant to HCM management (risk stratification, shared decision-making on participation per the 2024 AHA/ACC guideline) and to differential diagnosis (athlete's heart), but is not an aetiological factor. Hypertension and obesity influence LVH phenotype non-specifically.
- **Infectious agents:** **not applicable.**

For the dismech `environmental:` block: I would leave it empty rather than manufacture entries. If the `check-environmental-evidence` gate ever needs an answer here, the waiver sentence form ("Left deliberately uncited." + ≥20 words of recorded search) is the right instrument.

---

## 6. Mechanism / Pathophysiology

### Ordered causal chain

**Read this whole section as inference.** ClinGen's verdict — *"The mechanism for disease remains unknown"* — is the primary finding. Every arrow below is either (a) demonstrated for a *different* MYH6 allele in a *different* phenotype, or (b) demonstrated for MYH7 and transposed. I mark each step accordingly.

**Branch A — the asserted (MYH7-analogy) chain, entirely INFERRED for MYH6:**

1. A heterozygous *MYH6* missense allele **results in** a single amino acid substitution in α-cardiac myosin heavy chain. *[Demonstrated — this is just the variant.]*
2. The substituted residue **is predicted to** perturb motor-domain, converter, lever-arm, or coiled-coil tail structure. *[Computational only. Carniel: "All MYH6 mutations were distributed in highly conserved residues, were predicted to change the structure or chemical bonds of alphaMyHC." Note "predicted" — no biophysical assay was done on Q1065H or R795Q. The human α-MHC structure has never been solved; all structural inference is by homology to β-MHC (Anfinson 2022, PMID:35621855).]*
3. Altered actomyosin cross-bridge kinetics **lead to** hypercontractility with impaired relaxation and inefficient ATP utilisation. *[Transposed from MYH7. Never measured for any HCM-reported MYH6 allele.]*
4. Sarcomeric energetic stress and altered Ca²⁺ handling **lead to** activation of hypertrophic signalling in ventricular cardiomyocytes (`CL:0002131` regular ventricular cardiac myocyte). *[Inferred.]*
5. Hypertrophic signalling **results in** cardiomyocyte hypertrophy and myofibrillar disarray (`GO:0014898` cardiac muscle hypertrophy in response to stress). *[Inferred.]*
6. Sustained hypertrophy plus microvascular ischaemia **result in** interstitial and replacement fibrosis via cardiac fibroblast (`CL:0000057` fibroblast) activation → `HP:0001685` Myocardial fibrosis. *[Inferred; established for HCM generally.]*
7. Asymmetric septal thickening (`UBERON:0002094` interventricular septum) **results in** dynamic LVOT obstruction with systolic anterior motion of the mitral valve → `HP:0001653` Mitral regurgitation and `HP:0002875` Exertional dyspnea. *[Established for HCM; not MYH6-attributed.]*
8. Diastolic stiffening **results in** elevated filling pressures → `HP:0031295` Left atrial enlargement → `HP:0005110` Atrial fibrillation.
9. Fibrosis and disarray **create** a re-entrant substrate → `HP:0004756` Ventricular tachycardia → `HP:0001645` Sudden cardiac death.

**Branch B — the alternative and arguably better-supported chain, "MYH6 is an atrial gene":**

1. α-MHC is the **atrial**-predominant isoform in the adult human heart, a minor ventricular component. *[Demonstrated.]*

> "Myosin heavy chain alpha was found to be a major component of atrial myosin and a minor component of ventricular myosin, while heavy chain beta was found to be a major component of ventricular myosin and a minor component of atrial myosin."
> — Gorza et al., *Circ Res* 1984 (PMID:6234108) — the expression evidence ClinGen scored

2. A MYH6 missense allele therefore **acts principally on** atrial cardiomyocytes (`CL:0002129` regular atrial cardiac myocyte) and the developing atrium, not the adult LV. Anfinson et al. found exactly this pattern in patient tissue: *"atrial sarcomeres were disrupted with the R443P, K849del, and E1503V variants, while the ventricular sarcomere structure remained intact… consistent with α-MHC being the predominant atrial MHC isoform postnatally."* (PMID:35621855)
3. Atrial sarcomere disorganisation and contractile impairment **lead to** the phenotypes MYH6 is definitively or strongly associated with — atrial septal defect, sick sinus syndrome, HLHS — and **do not straightforwardly lead to** ventricular hypertrophy.
4. Where ventricular pathology *is* seen in MYH6 carriers, it may be **secondary** to atrial dysfunction: *"Given the predominance of β-MHC in the postnatal ventricles, it is possible that ventricular fibrosis is, at the cellular level, a downstream response to atrial cardiomyocyte dysfunction caused by MYH6 variants in the patients studied."* (PMID:35621855)

**Branch B is the single most useful thing in this report for dismech.** It explains why the MYH6–HCM link is weak on first principles — the gene's product is barely present in the tissue that hypertrophies — and it converts an "absence of evidence" curation into a positive mechanistic statement. It also has an elegant model-organism proof of the atrial→ventricular direction:

> "We find that the zebrafish locus weak atrium encodes an atrium-specific myosin heavy chain that is required for atrial myofibrillar organization and contraction… However, the weak atrium mutant ventricle becomes unusually compact, exhibiting a thickened myocardial wall, a narrow lumen and changes in myocardial gene expression. As weak atrium/atrial myosin heavy chain is expressed only in the atrium, the ventricular phenotypes in weak atrium mutants represent a secondary response to atrial dysfunction."
> — Berdougo et al., *Development* 2003 (PMID:14573521)

A thickened ventricular myocardial wall arising *secondarily* to an atrium-restricted myosin defect is the closest thing in the whole literature to a mechanism by which MYH6 could produce ventricular hypertrophy — and it is a zebrafish nonsense allele, not a human HCM missense allele. Curate it as `evidence_source: MODEL_ORGANISM`, `directness: INDIRECT`, and say plainly in `explanation` what the inference step is.

### Molecular pathways

- Actomyosin cross-bridge cycling / thick-filament regulation. Reactome R-HSA-390522 (Striated Muscle Contraction); KEGG hsa04260 (Cardiac muscle contraction) and hsa05410 (Hypertrophic cardiomyopathy).
- Downstream hypertrophic signalling implicated in HCM generally (calcineurin–NFAT, MAPK, PI3K–AKT–mTOR, TGF-β to fibroblasts) — **none demonstrated for MYH6**.

### Cellular processes (GO — all CURIEs below verified against `cache/go/terms.csv`)

| GO term | Label |
|---|---|
| `GO:0060048` | cardiac muscle contraction |
| `GO:0086003` | cardiac muscle cell contraction |
| `GO:0055117` | regulation of cardiac muscle contraction |
| `GO:0002026` | regulation of the force of heart contraction |
| `GO:0030049` | muscle filament sliding |
| `GO:0000146` | microfilament motor activity |
| `GO:0016887` | ATP hydrolysis activity |
| `GO:0051015` | actin filament binding |
| `GO:0003779` | actin binding |
| `GO:0030017` | sarcomere (CC) |
| `GO:0032982` | myosin filament (CC) |
| `GO:0014898` | cardiac muscle hypertrophy in response to stress |
| `GO:0055008` | cardiac muscle tissue morphogenesis |
| `GO:0002027` | regulation of heart rate |
| `GO:0086001` | cardiac muscle cell action potential |

For a CMH14 node, `GO:0000146` / `GO:0016887` / `GO:0051015` with `modifier: UNKNOWN`-equivalent (i.e. **omit `modifier`**) is more honest than tagging `GAIN_OF_FUNCTION`. Per the repo's GOF/LOF guidance, "the pathway is very active" would be `INCREASED`; here nobody has measured whether it is.

### Protein dysfunction

α-MHC is an ATP-driven actin-based motor; ClinGen scored biochemical function evidence for *"MHC-α interactions with ATP, actin and the light chains (Weiss et al. 1999)."* The functional studies that exist target non-HCM alleles:

- **I820N (ASD):** decreases α-MHC affinity for the regulatory light chain (Ching 2005, PMID:15735645).
- **E933del (SSS):** enhances MyBP-C binding; slows electrical propagation in HL-1 atrial cardiomyocytes; disrupts sarcomere structure with perinuclear α-MHC aggregation in NRVCMs.
- **R721W (SSS):** disrupted sarcomere structure and perinuclear aggregation in NRVCMs.
- **A230P, A1366D, E526K, R1822_E1823dup, R443P:** decreased sarcomere organisation in cultured cardiomyocytes; **H252Q** *increased* myofibril striations; **V700M** no effect despite being predicted damaging.
- **A1004S (DCM):** slower and reduced shortening in NRVCMs; **P830L (DCM):** no difference from WT — the opposite of what the structural prediction implied.

All from Anfinson et al. 2022 (PMID:35621855). The pattern is important: **in vitro effect does not track with in silico prediction, and no HCM-reported allele has been assayed at all.** Anfinson also notes: *"At present, no such 'mutational hotspots' have been identified in MYH6"* — unlike MYH7, where clustering informs ACMG/AMP classification.

### Metabolic changes

Liu et al. (PMID:34087240) reported metabolomic disturbance in a pedigree carrying MYH6-rs372446459 *together with* TNNT2-rs397516484:

> "They also showed disturbances of carbohydrate metabolism, including the citrate cycle (TCA cycle), glycolysis/gluconeogenesis, fructose and mannose metabolism, pentose and glucuronate interconversions and amino sugar and nucleotide sugar metabolism."

**Do not attribute this to MYH6.** The proband carried two sarcomere variants; the metabolomic signal cannot be assigned. If curated, it needs `directness: INDIRECT` and an `explanation` naming the confound.

### Immune system involvement

**Not applicable.** No autoimmune or immunodeficiency component.

### Tissue damage mechanisms

Myocardial fibrosis (`HP:0001685`), microvascular dysfunction/ischaemia, and myocyte disarray are the canonical HCM tissue lesions — established for HCM, unstudied in MYH6 carriers. Anfinson notes other groups have reported fibrosis in MYH6 carriers' *conduction system*, ventricular walls, and ventricular septum.

### Biochemical abnormalities / epigenetic changes / molecular profiling

- **Transcriptomics:** GTEx confirms MYH6 atrial-appendage-predominant expression. No CMH14 case–control transcriptomic dataset exists. One relevant in-vitro finding: MYH6-R443P iPSC-CMs showed *"sarcomere disorganization and the upregulation of MYH7"* — an isoform-compensation signal (PMID:35621855).
- **Proteomics, metabolomics, lipidomics, spatial transcriptomics, single-cell, multi-omics, CRISPR/RNAi screens:** **no CMH14-specific data.** Do not populate a `datasets:` block by relaxing the search to "MYH6" or to "hypertrophic cardiomyopathy" — that is precisely the Named Entity Confusion trap the repo's dataset guidance warns about (searching a causal gene surfaces whatever disease the gene is famous for; here that would return ASD/HLHS/SSS datasets, and relaxing to the parent term collapses CMH14 into generic HCM). If `datasets:` is populated at all, every accession needs `just verify-datasets` **plus** manual relevance triage, and I would expect the honest answer to be an empty block.

---

## 7. Anatomical Structures Affected

### Organ level

- **Primary:** heart (`UBERON:0000948`); specifically the left ventricle (`UBERON:0002084` heart left ventricle), left ventricular myocardium (`UBERON:0006566`), interventricular septum (`UBERON:0002094`), myocardium (`UBERON:0002349`).
- **On the Branch-B mechanism**, the primary site is instead the cardiac atrium — right cardiac atrium (`UBERON:0002078`) and the atrial septum / cardiac septum (`UBERON:0002099`) — plus the sinoatrial node region.
- **Secondary:** pulmonary circulation (post-capillary pulmonary hypertension from elevated filling pressures); systemic circulation and brain (cardioembolic stroke from AF).
- **Body system:** cardiovascular, exclusively. **CMH14 is a non-syndromic, heart-restricted phenotype** — no skeletal, neurological, renal, or dermatological involvement, which is a useful negative for differential diagnosis against syndromic LVH mimics.

### Tissue and cell level

| Cell type | CL term | Role |
|---|---|---|
| cardiac muscle cell | `CL:0000746` | general |
| regular ventricular cardiac myocyte | `CL:0002131` | site of asserted hypertrophy/disarray |
| regular atrial cardiac myocyte | `CL:0002129` | site where α-MHC actually predominates |
| fibroblast | `CL:0000057` | interstitial fibrosis |
| cardiac endothelial cell | `CL:0010008` | microvascular dysfunction |
| Purkinje myocyte | `CL:0002068` | conduction-system involvement (relevant to the SSS/conduction phenotypes) |

Tissue types: striated cardiac muscle; cardiac connective tissue/interstitium.

### Subcellular level

Sarcomere (`GO:0030017`), thick/myosin filament (`GO:0032982`), A-band and M-band, contractile fibre. Mitochondrial energetic involvement is inferred from MYH7 biology, not shown for MYH6.

### Localization and lateralization

Bilateral in the sense of being a whole-organ genetic disease, but the hypertrophy is characteristically **asymmetric** — septal-predominant, with the basal anteroseptum the classic site (`HP:0001670`). Apical, mid-cavity, and concentric variants occur. On Branch B the relevant asymmetry is chamber-level (atrial > ventricular), not wall-level.

---

## 8. Temporal Development

### Onset

- **OMIM 613251:** "variable age of onset from the third to eighth decade of life."
- **The replicated signal is late onset.** Niimura's cohort: *"Initial symptoms occurred at 59.3 (+/-12.3) years, and diagnosis was made at 62.8 (+/-10.8) years. None had family histories of cardiomyopathy."* Carniel's HCM proband was diagnosed at 27 and died of congestive heart failure at 45 — the exception. Rubattu found MYH6 variants **only** in the late-onset (≥65 y) group.
- **Onset pattern:** insidious and chronic. Hypertrophy develops subclinically; presentation is usually with exertional symptoms, an incidental murmur/ECG abnormality, or a family/screening echo.
- **HPO onset:** `Adult onset` / `Middle age onset` / `Late onset` are the defensible categories. Do **not** curate childhood onset for CMH14.

**Note the epistemic trap here.** Elderly-onset, family-history-negative HCM is exactly the setting where a rare missense variant is *least* likely to be causal and a phenocopy (hypertensive LVH, cardiac amyloidosis, age-related sigmoid septum) is *most* likely — and it is the only setting where MYH6 variants have been replicated. Niimura's own framing acknowledged the distributional oddity: *"The distribution of mutations in elderly-onset disease is strikingly different (P<0.00001) from that of familial, early onset hypertrophic cardiomyopathy."*

### Progression

- **Stages:** the HCM natural-history stages apply — (i) subclinical/G+P− genotype-positive phenotype-negative; (ii) classic hypertrophic phase with or without obstruction; (iii) adverse remodelling; (iv) end-stage/"burnt-out" HCM with systolic dysfunction (EF <50%), affecting ~3–5% of HCM patients.
- **Rate:** slow and variable over decades.
- **Course:** chronic, progressive, lifelong; punctuated by episodic arrhythmic events.
- **The one CMH14-specific progression claim in the literature** is Carniel's, and it is derived from a single proband: *"the HCM phenotype was characterized by progression toward dilation, left ventricular dysfunction, and refractory heart failure."* If curated as a `progression:` phase, it needs an explicit n=1 caveat in `notes` — a single patient cannot establish a phenotype's natural history.

### Patterns

- **Remission:** none spontaneous. Obstruction is relieved by septal reduction therapy or myosin inhibition, and symptoms remit; the myopathy does not.
- **Critical periods:** adolescence/early adulthood is the window of maximal hypertrophy development in *sarcomeric* HCM and drives the paediatric screening schedule — but is likely irrelevant to a late-onset MYH6 phenotype. For the definitive MYH6 congenital phenotypes, the critical period is cardiac septation in embryogenesis.

---

## 9. Inheritance and Population

### Epidemiology

- **HCM overall:** phenotypic prevalence classically ~1 in 500 (0.2%; 200 per 100,000). The JACC reappraisal opens with exactly this figure: *"Hypertrophic cardiomyopathy (HCM) is an inherited cardiac condition affecting ∼1 in 500 and exhibits marked genetic heterogeneity."* (PMID:39971408). Genotypic prevalence including non-penetrant carriers may approach 1 in 200.
- **CMH14 specifically:** **no prevalence estimate exists and none can be constructed.** With 3 probands worldwide and a disputed gene–disease relationship, the correct dismech `prevalence` record is `measure_type: CASES_IN_LITERATURE` with `prevalence_class: NOT_YET_DOCUMENTED` (or `UNKNOWN`) and `notes` recording the 3-proband count. Do **not** compute a `rate_per_100000`.
- **Incidence:** not available.

### For genetic etiology

- **Inheritance pattern:** autosomal dominant as asserted (ClinGen MOI: AD). HPO `HP:0000006` Autosomal dominant inheritance.
- **Penetrance:** unknown and, on the burden data, likely very low or zero for the reported alleles. Note the instructive contrast: for the *sick sinus syndrome* association, penetrance is quantified and high (lifetime risk ~50% for R721W carriers vs ~6% non-carriers, Holm 2011). Nothing comparable exists for HCM.
- **Expressivity:** OMIM describes "variability within and between families, ranging from benign to malignant forms." With n=3, this is HCM-general language, not a CMH14 observation.
- **Genetic anticipation:** **not applicable** (not a repeat-expansion disorder).
- **Germline mosaicism:** not reported.
- **Founder effects:** none for HCM alleles. There *is* a MYH6 founder-like signal for a different phenotype — R721W at 0.38% allele frequency in Icelanders (Holm 2011) — worth recording as context but not as CMH14 epidemiology.
- **Consanguinity:** not relevant to the dominant HCM claim. It *is* relevant to the recessive MYH6–HLHS mechanism (compound heterozygosity; Theis 2015).
- **Carrier frequency:** not applicable to a dominant condition. The relevant population figure is the *allele* frequency of the reported variants (§2) — and their commonness relative to the disease is the argument against pathogenicity.

### Population demographics

- **Affected populations:** no ethnic enrichment for CMH14. Q1065H is notably commoner in East Asian ancestry (~0.1% in ExAC), which further undercuts pathogenicity rather than indicating a founder disease population.
- **Geographic distribution:** reported probands are from US (Niimura), US/Italy (Carniel), Italy (Rubattu), China (Liu; Wang iPSC line), and Japan (Suzuki). This is publication geography, not disease geography.
- **Sex ratio:** not established for CMH14. HCM overall is diagnosed more often in men (roughly 3:2), though this partly reflects ascertainment; women present later and with worse outcomes. Niimura's late-onset cohort was 18 women / 13 men.
- **Age distribution:** skewed late — see §8.

---

## 10. Diagnostics

**CMH14 is diagnosed as HCM plus a genotype. There is no CMH14-specific test.**

### Clinical tests

| Modality | Findings | Notes |
|---|---|---|
| **Transthoracic echocardiography** | LV wall thickness ≥15 mm (≥13 mm with family history), asymmetric septal hypertrophy, SAM of the mitral valve, dynamic LVOT gradient (rest + Valsalva + exercise provocation), diastolic dysfunction, LA enlargement | First-line. Niimura cohort: max wall thickness 19.9 ± 3.8 mm, SAM in 58%, LVOT gradient mean 63 ± 42.8 mmHg in 11 patients |
| **Cardiac MRI with LGE** | Confirms wall thickness where echo windows are poor; quantifies late gadolinium enhancement (fibrosis); detects apical/anterolateral hypertrophy and apical aneurysm | Extensive LGE (≥15% LV mass) is an SCD risk modifier in the 2024 AHA/ACC guideline |
| **12-lead ECG** | LVH voltage, repolarisation abnormality, deep narrow Q waves, giant negative T waves (apical HCM). Abnormal in >90% of HCM | Also the modality that would detect the MYH6-associated conduction phenotypes: sinus bradycardia, sinus pauses, AV block |
| **Ambulatory ECG (24–48 h Holter / extended)** | NSVT detection for SCD risk stratification; AF detection | Guideline-recommended at diagnosis and periodically |
| **Exercise stress testing** | Provokable LVOT gradient; abnormal blood-pressure response; functional capacity | |
| **Laboratory** | NT-proBNP / BNP; high-sensitivity troponin. **Critically, the amyloid rule-out panel:** serum/urine immunofixation, serum free light chains, and ⁹⁹ᵐTc-PYP/DPD bone scintigraphy | In a 60–80-year-old with new LVH — the CMH14 demographic — transthyretin cardiac amyloidosis is the single most important phenocopy to exclude |
| **Endomyocardial biopsy** | Myocyte hypertrophy, myofibrillar disarray, interstitial fibrosis, small-vessel disease | Rarely indicated; used to exclude infiltrative disease |

Note that no biomarker distinguishes CMH14 from any other HCM, and none is MYH6-informed.

### Genetic testing

- **Recommended approach:** a **targeted HCM gene panel** on the proband, per the 2024 AHA/ACC guideline. The panel should be *narrow*. This is the operational consequence of the ClinGen work, and it is stated bluntly in the reappraisal: *"Nine (29%) genes were downgraded to disputed, further discouraging clinical reporting of variants in these genes."* (PMID:39971408). MYH6 is one of those nine.
- **Practical implication:** **a MYH6 variant found on a legacy broad panel should not be reported as causative of HCM, and should not be used for cascade testing.** A laboratory still returning MYH6 for HCM is using a stale gene list. Rubattu reached the same conclusion empirically in 2016: *"Our findings support the choice of a limited, well-selected panel of HCM genes as the best tool for diagnostic purposes."*
- **The genes that should be on the panel** (ClinGen Definitive/Strong/Moderate, per PMID:39971408 — 29 genes): the sarcomere core MYBPC3, MYH7, TNNT2, TNNI3, TPM1, ACTC1, MYL2, MYL3 plus **TNNC1** (newly upgraded, *"a 9th sarcomere gene with definitive HCM association"*); sarcomere-associated ACTN2, CSRP3, FHOD3, FLNC (missense), PLN, DES, ALPK3, TRIM63 (AR), PRKAG2; syndromic/phenocopy GLA, LAMP2, TTR, FHL1, CACNA1C, PTPN11, RAF1, RIT1; and MT-TI, KLHL24 (moderate).
- **WES / WGS:** reasonable when the phenotype is syndromic or panel-negative with strong family history. WGS was the discovery modality for the recessive MYH6–HLHS finding (Theis 2015).
- **Single-gene testing:** appropriate only for cascade testing of a known familial variant. **Not applicable to MYH6/HCM**, since no MYH6 variant meets the P/LP bar.
- **CMA, karyotyping, FISH, mtDNA testing, repeat-expansion testing:** **not indicated** for CMH14. CMA has a role in syndromic congenital heart disease, and mtDNA testing is relevant for the MT-TI phenocopy — neither is a CMH14 test.

### Clinical criteria

**Diagnosis** (2024 AHA/ACC, PMID:38718139; 2023 ESC cardiomyopathy guideline, PMID:37622657): LV wall thickness ≥15 mm in any segment by any imaging modality, not solely explained by abnormal loading conditions; ≥13 mm in first-degree relatives of an affected proband or in genotype-positive individuals. Paediatric criteria use z-scores (≥2 SD, or ≥2.5 SD in relatives).

**Differential diagnosis** — and this is where CMH14's late-onset skew matters most:

| Mimic | Distinguishing features |
|---|---|
| **Transthyretin cardiac amyloidosis (ATTR)** | Low voltage relative to wall thickness, apical sparing on strain, positive PYP scan, biventricular thickening, older age. *The top consideration in a 70-year-old with new "HCM."* |
| Hypertensive LVH / age-related basal septal bulge | Concentric, hypertension history, typically <15 mm |
| Athlete's heart | Wall <15 mm, dilated LV cavity, normal diastolic function, regression on detraining |
| Fabry disease (GLA) | X-linked, angiokeratoma, neuropathy, renal involvement, low α-Gal A |
| Danon disease (LAMP2) | Massive LVH, WPW pre-excitation, myopathy, intellectual disability |
| PRKAG2 glycogen storage cardiomyopathy | Marked pre-excitation and conduction disease |
| RASopathies (PTPN11, RAF1, RIT1 — Noonan spectrum) | Dysmorphology, pulmonary valve stenosis, short stature |
| Aortic stenosis / subaortic membrane | Fixed rather than dynamic gradient |
| Mitochondrial cardiomyopathy (incl. MT-TI) | Maternal inheritance, multisystem |

### Screening

- **Cascade clinical screening of first-degree relatives** — ECG + echo, repeating every 1–2 years in adolescence and every 3–5 years in adults — is the guideline standard and **remains appropriate for CMH14 families**, because the phenotype is real even where the genotype attribution is not.
- **Cascade genetic testing** is **not appropriate** for a MYH6 variant, since no such variant is P/LP. This distinction (clinical screening yes, genetic screening no) is the key practical point for the entry.
- **Newborn screening:** not applicable.
- **Preparticipation athletic screening:** ECG-based programmes detect HCM but are population-level and not CMH14-specific.

---

## 11. Outcome / Prognosis

**All figures below are HCM-level. There is no CMH14 survival, mortality, or morbidity dataset.**

- **Survival / mortality:** contemporary HCM cohorts show near-normal life expectancy with modern management; HCM-related mortality ~0.5%/yr, down from historical tertiary-referral estimates of 2–4%/yr. Sudden cardiac death, heart failure, and stroke are the three modes.
- **Life expectancy:** approaching that of the general population in guideline-managed cohorts; substantially reduced in the minority progressing to end-stage disease.
- **Morbidity / disability:** exertional limitation, AF-related stroke, ICD-related complications, restriction from competitive sport. **Disease-specific instrument: KCCQ.** No ICF-coded disability data for CMH14.
- **Complications:** LVOT obstruction; atrial fibrillation with thromboembolism; ventricular arrhythmia and SCD; progressive heart failure; infective endocarditis (rare); end-stage systolic dysfunction requiring transplant.
- **Recovery potential:** none — the myopathy is not reversible. Symptomatic and haemodynamic improvement with obstruction relief is excellent.
- **Prognostic factors (HCM SCD risk, per 2024 AHA/ACC / HCM Risk-SCD):** prior cardiac arrest or sustained VT; family history of SCD; unexplained syncope; maximal LV wall thickness ≥30 mm; NSVT; LV apical aneurysm; LV systolic dysfunction (EF <50%); extensive LGE on CMR.
- **Genotype as a prognostic factor:** sarcomere-positive HCM is associated with earlier onset and worse outcomes than sarcomere-negative HCM in general. **This does not transfer to MYH6.** A MYH6 VUS should not be entered into risk stratification, and I would flag any clinical use of it as an error.
- **Prognostic biomarkers:** NT-proBNP and hs-troponin correlate with adverse outcome in HCM; LGE burden is the strongest imaging prognosticator. None MYH6-specific.

---

## 12. Treatment

**There is no MYH6-directed therapy, and no evidence that MYH6 genotype should alter management.** Management is standard HCM care. NCIT bindings below are verified against `cache/ncit/terms.csv` where marked ✓.

### Pharmacotherapy

| Treatment | `treatment_term` | `therapeutic_agent` | `therapeutic_modality` |
|---|---|---|---|
| Beta blockade (first-line for obstructive and symptomatic HCM) | `NCIT:C15986` Pharmacotherapy ✓ | `CHEBI:6904` metoprolol ✓ | `SMALL_MOLECULE` |
| Non-dihydropyridine calcium channel blockade (beta-blocker intolerant) | `NCIT:C15986` ✓ | `CHEBI:9948` verapamil ✓; `CHEBI:101278` diltiazem ✓ | `SMALL_MOLECULE` |
| Disopyramide (added for refractory obstruction) | `NCIT:C15986` ✓ | `NCIT:C61730` Disopyramide ✓ | `SMALL_MOLECULE` |
| **Cardiac myosin inhibition — mavacamten** | `NCIT:C15986` ✓ | `CHEBI:756998` mavacamten ✓ / `NCIT:C174901` Mavacamten ✓ | `SMALL_MOLECULE` |
| **Cardiac myosin inhibition — aficamten** | `NCIT:C15986` ✓ | `CHEBI:747213` aficamten ✓ | `SMALL_MOLECULE` |
| Anticoagulation for AF (DOAC preferred; CHA₂DS₂-VASc not used — any AF in HCM warrants anticoagulation) | `NCIT:C15986` ✓ | — | `SMALL_MOLECULE` |
| Antiarrhythmic therapy for AF/VT | `NCIT:C15986` ✓ | `CHEBI:2663` amiodarone ✓ | `SMALL_MOLECULE` |

**The mechanistic irony worth curating.** Mavacamten and aficamten are allosteric inhibitors of **cardiac β-myosin (MYH7)** ATPase, reducing the number of force-generating cross-bridges. They target the ventricular isoform. If CMH14 were genuinely an α-MHC (MYH6) disease, the pharmacological rationale for these agents in it would be indirect at best. Anfinson et al. raise the corresponding therapeutic question for MYH6 carriers and note it cuts both ways:

> "However, choosing to use a cardiac MHC-specific activator vs. inhibitor requires the understanding of whether a specific variant will cause systolic or diastolic dysfunction."
> — Anfinson et al. 2022 (PMID:35621855)

Their `evidence_source` for that passage is a review, and the drug-approval detail in it is dated (mavacamten approval was pending at writing; it has since been approved) — quote it for the mechanistic point, not the regulatory status.

**Pivotal trials (for a `clinical_trials:` block):**
- **EXPLORER-HCM**, NCT03470545, `PHASE_III`, `COMPLETED` — mavacamten in symptomatic obstructive HCM (Olivotto et al., *Lancet* 2020, PMID:32871100).
- **SEQUOIA-HCM**, NCT05186818, `PHASE_III`, `COMPLETED` — aficamten in obstructive HCM (Maron et al., *NEJM* 2024, PMID:38739079).

Use the enum values `PHASE_III` / `COMPLETED`, not the prose spellings.

### Pharmacogenomics

**No CPIC or PharmGKB guideline is keyed to MYH6.** Mavacamten dosing *is* pharmacogenomically guided — by **CYP2C19** metabolizer status (poor metabolizers require reduced starting dose and altered titration; this is in the US label and in the 2024 guideline). That is a drug-metabolism interaction, not a MYH6 interaction, and should be curated on the treatment, not the gene.

### Advanced therapeutics

- **Gene therapy / gene editing:** none for CMH14. AAV-based approaches (e.g. MYBPC3 replacement, allele-specific editing for MYH7) are in early development for *other* HCM genotypes. Nothing MYH6-directed.
- **RNA-based therapy (ASO/siRNA):** none for CMH14. Leave `aso_details` absent.
- **Cell therapy, immunotherapy:** not applicable.

### Surgical and interventional

| Intervention | NCIT |
|---|---|
| Septal myectomy (surgical, for drug-refractory obstruction) | `NCIT:C15329` Surgical Procedure ✓ |
| Alcohol septal ablation (catheter-based alternative) | `NCIT:C49236` Therapeutic Procedure ✓ |
| **ICD implantation** for primary or secondary SCD prevention | `NCIT:C15329` ✓ with `qualifiers` predicate `NCIT:C16830` Medical Device ✓ carrying the ICD device term; `therapeutic_modality: DEVICE` |
| Permanent pacemaker (for the MYH6-associated bradyarrhythmia phenotypes, not for HCM per se) | as above, `DEVICE` |
| Catheter ablation for AF | `NCIT:C49236` ✓ |
| Heart transplantation (end-stage) | `NCIT:C15289` Organ Transplantation ✓ |

Per the repo's device rule: bind the clinical *action* (`NCIT:C15329`) and carry the device in a `qualifiers` predicate–value pair with `NCIT:C16830` as the predicate. Do not put a device term in the `treatment_term.term` slot.

### Supportive, rehabilitative, and counselling

- Supportive care `NCIT:C15747` ✓ — heart-failure management, volume optimisation, avoidance of dehydration and high-dose vasodilators/diuretics in obstructive physiology.
- Exercise counselling — the 2024 guideline liberalised recommendations toward shared decision-making on vigorous and competitive activity; `therapeutic_modality: BEHAVIORAL`.
- Cardiac rehabilitation `NCIT:C15302` Physical Therapy ✓ / `NCIT:C15315` Rehabilitation — moderate-intensity exercise is now considered beneficial.
- **Genetic counselling** `NCIT:C15240` ✓ — and this is the one place where CMH14's disputed status changes clinical practice directly. The counselling content is: *this MYH6 variant does not explain the HCM, cascade genetic testing on it is not indicated, and relatives need clinical (ECG/echo) screening regardless.* `therapeutic_modality: BEHAVIORAL`.

### Treatment strategy

Guideline algorithms (2024 AHA/ACC PMID:38718139; 2023 ESC PMID:37622657) branch on **obstructive vs non-obstructive** physiology and on SCD risk — **not on genotype**. Beta blocker → add/switch verapamil or disopyramide → myosin inhibitor → septal reduction therapy for refractory obstruction; parallel SCD risk assessment for ICD; parallel AF management. Personalised-medicine approaches in HCM are genotype-informed for family screening and for phenocopy-specific therapy (e.g. agalsidase for Fabry, tafamidis for ATTR) — neither pathway is available for MYH6.

---

## 13. Prevention

- **Primary prevention (preventing the disease):** **not possible** — a germline dominant condition. Reproductive options (PGT-M, prenatal diagnosis) exist in principle for definitively pathogenic HCM variants; **they are not offered for a VUS**, which is what every MYH6 HCM allele currently is.
- **Secondary prevention (early detection):**
  - Cascade **clinical** screening of first-degree relatives — ECG and echo, every 1–2 years in adolescence, every 3–5 years in adults. Appropriate and recommended.
  - Cascade **genetic** screening — **not indicated** for MYH6, as above.
  - Preparticipation athletic screening — population-level, not CMH14-specific.
- **Tertiary prevention (preventing complications in affected people):** this is where nearly all real preventive value sits.
  - **ICD** for primary SCD prevention in high-risk patients (the largest single mortality intervention in HCM).
  - **Anticoagulation** for any documented AF, to prevent cardioembolic stroke.
  - **Relief of LVOT obstruction** to prevent progressive symptoms and remodelling.
  - Blood-pressure control, weight management, sleep-apnoea treatment, endocarditis awareness.
- **Immunization:** not applicable as disease prevention; influenza/COVID/pneumococcal vaccination is standard for patients with structural heart disease.
- **Risk stratification:** HCM Risk-SCD (ESC) and the 2024 AHA/ACC major-risk-marker approach. Note both are validated on HCM cohorts and neither incorporates MYH6 genotype.
- **Genetic counselling:** see §12. The counselling message is dominated by the disputed-gene finding.
- **Public health / environmental interventions:** **not applicable.** No environmental exposure to modify.

---

## 14. Other Species / Natural Disease

- **Taxonomy:** *Homo sapiens*, `NCBITaxon:9606`. Species used experimentally: *Mus musculus* `NCBITaxon:10090`; *Danio rerio* `NCBITaxon:7955`; *Rattus norvegicus* `NCBITaxon:10116`; *Gallus gallus* `NCBITaxon:9031` (Ching's chick morpholino).
- **Orthologous genes:** mouse *Myh6* (MGI:97255, NCBI Gene 17888); rat *Myh6* (NCBI Gene 29556); zebrafish *myh6* / *amhc* (ZFIN ZDB-GENE-031112-1); chick *MYH6*. The α/β MHC pair is deeply conserved across gnathostomes.

**The single most important comparative fact — and it is a trap for anyone extrapolating from mouse:** the α/β ventricular isoform ratio is *inverted* between human and rodent. Adult human ventricle is β-MHC (MYH7)-dominant with α-MHC a minor component; adult mouse and rat ventricle is α-MHC (Myh6)-dominant. A mouse *Myh6* ventricular phenotype therefore has no straightforward human counterpart. ClinGen made this exact call when refusing to score the classic mouse HCM models:

> "Additional studies on mice models of HCM using pre-engineered heterozygous, pathogenic MYH7 variant orthologous to the human p.R403Q allele into the mouse MYH6 were reviewed, but not scored because these mice models are not analogous to human MYH6."
> — ClinGen `CGGV:assertion_ee5380a4…`

This should be curated in dismech as a `discussions:` entry with **`kind: HUMAN_MODEL_MISMATCH`**, not `KNOWLEDGE_GAP` — evidence exists in the model, and it is the translational validity that is the open question. That is precisely the distinction the repo's guidance draws.

- **Natural disease in other species:** hypertrophic cardiomyopathy is the commonest feline heart disease (~15% of cats; higher in Maine Coon and Ragdoll breeds), and it is a genuine spontaneous animal model. **But it is not MYH6.** The identified feline causal variants are in ***MYBPC3*** — Maine Coon p.A31P and Ragdoll p.R820W (OMIA 000515-9685). No MYH6 variant causes naturally occurring HCM in any species. Curate this as a negative comparative finding; it is informative, and the VBO breed terms (Maine Coon, Ragdoll) belong on the *feline MYBPC3* concept, not here.
- **Comparative pathology:** myocyte hypertrophy, disarray, and interstitial fibrosis are conserved lesions across human and feline HCM.
- **Evolutionary conservation of mechanism:** the sarcomere and the α/β MHC duplication are ancient and conserved; the chamber-specific *deployment* of the two isoforms differs by species, which is exactly what breaks the translational chain here.
- **Zoonotic potential / cross-species transmission:** **not applicable.**

---

## 15. Model Organisms

**No model organism carries a human CMH14-associated MYH6 allele.** This is the experimental gap, and it is stark: of the four MYH6 variants reported in HCM probands, zero have been functionally assayed in any system.

### Available models and what they actually show

| Model | Type | Allele | What it recapitulates | `ModelMechanismLink` guidance |
|---|---|---|---|---|
| **αMHC-403 knock-in mouse** (Geisterfer-Lowrance 1996, PMID:8614836) | `animal_models:`, *Mus musculus* | mouse *Myh6* R403Q — an **MYH7**-derived human allele placed in the mouse α-MHC gene | *"Cardiac histopathology and dysfunction in the alpha MHC 403/+ mice resembled human FHC… myocyte disarray, hypertrophy, and fibrosis increased with age."* Homozygotes die at 7 days; sedentary heterozygotes survive 1 year; young males more affected than females | **`relationship: FAILS_TO_RECAPITULATE` for CMH14 specifically** — it models human MYH7 HCM, not MYH6 HCM. `fidelity: LOW`. `limitations:` the allele is orthologous to human MYH7 R403Q, and mouse ventricle is α-MHC-dominant whereas human ventricle is β-MHC-dominant, so the model is a mouse-genetics convenience, not an MYH6 model. **Requires `limitations` + `evidence` per `test_failure_to_recapitulate_links_are_substantiated`.** ClinGen explicitly declined to score it. |
| **zebrafish *weak atrium* (*wea*) / *myh6*** (Berdougo 2003, PMID:14573521) | `animal_models:`, *Danio rerio* | nonsense allele truncating Amhc C-terminus | Atrial myofibrillar disorganisation and loss of atrial contraction; **secondary** ventricular compaction with a thickened myocardial wall and narrow lumen | `relationship: PARTIALLY_RECAPITULATES` against a "ventricular wall thickening secondary to atrial contractile failure" node. `fidelity: LOW–MODERATE`. `limitations:` null allele vs human missense; two-chambered heart; the ventricular change is compaction, not the sarcomeric disarray of human HCM. The most mechanistically informative model available. |
| **zebrafish *myh6* knockdown + human variant rescue** (reviewed in PMID:35621855) | `animal_models:` | rescue with human MYH6-WT, -E933del, -R1252Q | Bradycardia in knockdowns (137.7 ± 2.2 bpm vs 150.2 ± 1.6 uninjected); WT and R1252Q rescue heart rate, **E933del fails to** | Models the **conduction** phenotype, not HCM. `relationship: MEASURES` against a rate/conduction node; do not link to a hypertrophy node. |
| **Patient-derived iPSC line, MYH6 c.3755G>A** (Wang et al. 2021, PMID:33385793) | `experimental_models:` (NAM), `experimental_model_type` iPSC-derived | *"a G3755A heterozygote mutation in the MYH6 gene"* from an HCM patient | A resource paper — line generation and characterisation only. **No disease phenotype demonstrated.** | Curate as an available model with **no** `modeled_mechanisms` link, or a link with `relationship: MEASURES` and `fidelity: UNKNOWN`. Do not let a resource paper carry a mechanistic claim. |
| **MYH6-R443P patient iPSC-CMs** (HLHS; PMID:35621855) | `experimental_models:` | R443P | *"decreased the shortening rate, relaxation rate, extent of shortening, percent shortening, and calcium transient amplitude at the single CM level… without affecting action potentials"*; sarcomere disorganisation and MYH7 upregulation | The best-characterised MYH6 human cellular model — but the allele is an **HLHS** allele. Relevant as mechanism-of-the-gene context, `evidence_source: IN_VITRO`, `directness: INDIRECT`. |
| **NRVCM / HL-1 transfection systems** (PMID:35621855) | `experimental_models:`, in vitro | A230P, A1004S, P830L, E526K, E933del, R721W, H252Q, V700M, A1366D, R1822_E1823dup | Variable and prediction-discordant sarcomere and contractility effects (see §6) | Useful negative-result material. `V700M` (no effect despite "likely damaging" predictions) and `P830L` (no shortening deficit) are worth curating as `supports: REFUTE` items against a naive structure→function claim. |
| ***Myh6* null / haploinsufficient mouse** | `animal_models:` | targeted ablation | Gene-dosage effects and functional deficits in the heart; homozygous null is embryonic lethal | Models **loss of function**. Since no HCM-reported MYH6 allele has a demonstrated LoF mechanism, this cannot be linked to a CMH14 node without an inference step. |

### Model types not available

Rat, *Drosophila*, *C. elegans*, yeast, organ-chip, and engineered heart tissue models of MYH6-HCM: **none exist**. No humanized MYH6 mouse, no conditional MYH6 knock-in of a human HCM allele, no CRISPR-corrected isogenic iPSC pair for any CMH14 variant.

Anfinson et al. state the scope of the whole field plainly:

> "To date, zebrafish embryos are the only animal model that has been used to study human MYH6 variants."
> — PMID:35621855

and

> "Relative to the large body of literature assessing MYH7 variants, few studies have sought to understand MYH6 variant pathology at the molecular level."

### Resources

MGI (Myh6, MGI:97255) and IMPC/KOMP for mouse alleles; ZFIN for *myh6*/*wea*; Alliance of Genome Resources for orthology; Cellosaurus/hPSCreg for the patient iPSC line from PMID:33385793; IMSR/MMRRC for mouse strain distribution.

---

## Curation summary for the dismech entry

The placeholder file currently asserts a `pathophysiology` node "MYH6 Missense Variant in Alpha-Myosin Heavy Chain" and a `Left Ventricular Hypertrophy` phenotype. Both are defensible, but the entry's substance should be the epistemic situation, not a borrowed MYH7 causal chain. Concretely:

1. **Rewrite `description`** to state that MYH6–HCM is ClinGen-Disputed and that the mechanism is unknown.
2. **Keep the pathophysiology graph short and honest.** One or two nodes, with `biological_scale: MOLECULAR` on the variant node. Do not build a 7-node MYH7-style chain; the `check-causal-targets` gate will happily accept a fabricated chain, and nothing else will catch it.
3. **Lead evidence** with `CGGV:assertion_ee5380a4-0dee-49aa-b911-141502648144-2023-07-12T020000.000Z` (already cached, quotable by row: `MYH6 | HGNC:7576 | hypertrophic cardiomyopathy | MONDO:0005045 | AD | Disputed | SOP9 | Hereditary Cardiovascular Disease Gene Curation Expert Panel | 2023-07-12T02:00:00.000Z`) and `PMID:39971408`.
4. **Add a `discussions:` entry, `kind: HUMAN_MODEL_MISMATCH`**, for the mouse αMHC-403 problem — the model exists and is famous, and its inapplicability to MYH6 is the substantive point.
5. **Add a `discussions:` entry, `kind: KNOWLEDGE_GAP`**, `attaches_to: pathophysiology#…`, for the unmeasured biophysics of R795Q and Q1065H.
6. **Leave `datasets:` empty** unless a genuinely CMH14-relevant accession survives manual relevance triage. I found none.
7. **Record the atrial-isoform argument (Branch B)** — Gorza 1984 + Berdougo 2003 + Anfinson 2022 — as the positive mechanistic content of the entry. It is the one thing here that is both well-evidenced and explanatory.
8. **`conforms_to` candidates:** check `just list-modules` for a cardiomyopathy remodeling module before conforming. `cardiomyopathy_maladaptive_remodeling` is the likely target for a fibrosis/remodeling node — but conform only if the entry ends up carrying such a node, which on the evidence it may not.

References fetched into `references_cache/` during this work: PMID:11815426, 15998695, 27483260, 33385793, 34087240, 35911064, 21378987, 10388558, 6234108, 8614836, 24092743, 15735645, 26085007, 35621855, 14573521, 39971408, 30681346, 38718139, 37622657, 32871100, 38739079, 27532257, 23074333. Two mis-targeted fetches (PMID:14568893, PMID:35544178) are stale and should be deleted before committing; I did not remove them, as the deletion command needed approval this session.

**Sources:**
- [OMIM #613251 — CARDIOMYOPATHY, FAMILIAL HYPERTROPHIC, 14](https://omim.org/entry/613251)
- [OMIM #160710 — MYH6](https://omim.org/entry/160710)
- [ClinGen MYH6 curation results (HGNC:7576)](https://search.clinicalgenome.org/kb/genes/HGNC:7576)
- [ClinGen gene-validity assertion — MYH6 / hypertrophic cardiomyopathy (Disputed)](https://search.clinicalgenome.org/kb/gene-validity/CGGV:assertion_ee5380a4-0dee-49aa-b911-141502648144-2023-07-12T020000.000Z)
- [Hespe et al., JACC 2025 — Genes Associated With HCM: A Reappraisal (PMID:39971408)](https://pubmed.ncbi.nlm.nih.gov/39971408/) · [PMC preprint](https://pmc.ncbi.nlm.nih.gov/articles/PMC11312670/)
- [Ingles et al. 2019 — Evaluating the Clinical Validity of HCM Genes (PMID:30681346)](https://pubmed.ncbi.nlm.nih.gov/30681346/)
- [Niimura et al., Circulation 2002 (PMID:11815426)](https://pubmed.ncbi.nlm.nih.gov/11815426/)
- [Carniel et al., Circulation 2005 (PMID:15998695)](https://pubmed.ncbi.nlm.nih.gov/15998695/)
- [Rubattu et al. 2016 (PMID:27483260)](https://pubmed.ncbi.nlm.nih.gov/27483260/)
- [Walsh et al., Genet Med 2017 (PMID:27532257)](https://pubmed.ncbi.nlm.nih.gov/27532257/)
- [Holm et al., Nat Genet 2011 (PMID:21378987)](https://pubmed.ncbi.nlm.nih.gov/21378987/)
- [Ching et al., Nat Genet 2005 (PMID:15735645)](https://pubmed.ncbi.nlm.nih.gov/15735645/)
- [Theis et al., Circ Cardiovasc Genet 2015 (PMID:26085007)](https://pubmed.ncbi.nlm.nih.gov/26085007/)
- [Anfinson et al., J Cardiovasc Dev Dis 2022 (PMID:35621855)](https://pubmed.ncbi.nlm.nih.gov/35621855/)
- [Berdougo et al., Development 2003 (PMID:14573521)](https://journals.biologists.com/dev/article/130/24/6121/42189/Mutation-of-weak-atrium-atrial-myosin-heavy-chain)
- [Gorza et al., Circ Res 1984 (PMID:6234108)](https://pubmed.ncbi.nlm.nih.gov/6234108/)
- [Geisterfer-Lowrance et al., Science 1996 (PMID:8614836)](https://pubmed.ncbi.nlm.nih.gov/8614836/)
- [Weiss et al., J Mol Biol 1999 (PMID:10388558)](https://pubmed.ncbi.nlm.nih.gov/10388558/)
- [Liu et al., Clin Chim Acta 2021 (PMID:34087240)](https://pubmed.ncbi.nlm.nih.gov/34087240/)
- [Suzuki et al., J Cardiol Cases 2022 (PMID:35911064)](https://pubmed.ncbi.nlm.nih.gov/35911064/)
- [Wang et al. 2021 iPSC line (PMID:33385793)](https://pubmed.ncbi.nlm.nih.gov/33385793/)
- [Ommen et al., 2024 AHA/ACC HCM Guideline (PMID:38718139)](https://pubmed.ncbi.nlm.nih.gov/38718139/)
- [Arbelo et al., 2023 ESC Cardiomyopathy Guideline (PMID:37622657)](https://pubmed.ncbi.nlm.nih.gov/37622657/)
- [ClinVar VCV000014147 — MYH6 p.Arg795Gln](https://www.ncbi.nlm.nih.gov/clinvar/variation/14147/)
- [ClinVar VCV000014149 — MYH6 p.Gln1065His](https://www.ncbi.nlm.nih.gov/clinvar/variation/14149/)
- [gnomAD v4.0 gene constraint](https://gnomad.broadinstitute.org/news/2024-03-gnomad-v4-0-gene-constraint/)

**Next step:** tell me whether you want the entry curated as a disputed-entity `Disease` file (my recommendation, and I'd write it against the evidence above), or whether the lump/split call should go the other way — a `SUBTYPE`/`OUT_OF_SCOPE` disposition on `Hypertrophic_Cardiomyopathy` with the stub deleted and the reasoning recorded in `notes`.

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 24 |
| On topic | 14 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 82 |
| Resolved | 79 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 3 |
| Terms whose name was checked | 25 |
| Terms named correctly | 22 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 3 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0013197` (2 mentions) - the report calls it "Any hypertrophic cardiomyopathy in which the cause of the disease is a mutation in the MYH6 gene"; MONDO calls it **hypertrophic cardiomyopathy 14**, and lists "hypertrophic cardiomyopathy caused by mutation in MYH6" among its other names
- `GO:0030017` (2 mentions) - the report calls it "sarcomere (CC)"; GO calls it **sarcomere**
- `GO:0032982` (2 mentions) - the report calls it "myosin filament (CC)"; GO calls it **myosin filament**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0005045` - called "hypertrophic cardiomyopathy", "Hypertrophic cardiomyopathy"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `MGI`.

79 of 82 terms resolved to a current term; the rest could not be looked up either way.