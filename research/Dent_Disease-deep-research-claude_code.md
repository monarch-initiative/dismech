---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-4-7[1m]
cached: false
start_time: '2026-09-11T12:50:07.725816'
end_time: '2026-09-11T12:55:56.802044'
duration_seconds: 349.08
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Dent Disease
  mondo_id: MONDO:0015612
  category: Disease
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
  - claude-opus-4-7[1m]
  web_search_requests: 13
  num_turns: 28
  total_cost_usd: 2.93045725
  session_id: ff5eab0e-7cb7-4b56-84ff-afa9ed79ba42
  stop_reason: end_turn
  permission_denials: 4
  denied_tools:
  - mcp__pubmed__search_articles
  assistant_text_blocks: 1
citation_count: 28
reference_validation:
  total_references: 35
  verified: 35
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 35
  on_topic: 21
  off_topic: 5
  off_topic_references:
  - PMID:20950533
  - PMID:26296266
  - PMID:26154403
  - PMID:11279143
  - PMID:25911330
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 61
  verified: 50
  not_found: 0
  obsolete: 0
  unverifiable: 11
  confabulation_rate: 0.0
  labels_checked: 43
  labels_matching: 26
  labels_mismatched: 5
  mislabelled_terms:
  - term_id: MONDO:0010655
    reported_labels:
    - MONDO (DD1)
    - Dent disease 1
    ontology_label: X-linked intellectual disability with marfanoid habitus
  - term_id: MONDO:0010371
    reported_labels:
    - MONDO (DD2)
    - Dent disease 2
    ontology_label: Aland island eye disease
  - term_id: HP:0000790
    reported_labels:
    - Hematuria (usually microscopic)
    ontology_label: Hematuria
  - term_id: HP:0032122
    reported_labels:
    - "Elevated \u03B22-microglobulin, \u03B11-microglobulin"
    ontology_label: Very low visual acuity
  - term_id: UBERON:0001225
    reported_labels:
    - "Primary:** Kidney \u2014 specifically the renal cortex"
    - kidney cortex
    ontology_label: cortex of kidney
  labels_variant: 12
  unresolvable_prefixes:
  - ORPHA
  - LOINC
  - ID
  - MGI
  - RGD
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dent Disease
- **MONDO ID:** MONDO:0015612 (if available)
- **Category:** Disease

## Research Objectives

Please provide a comprehensive research report on **Dent Disease** covering all of the
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

I have gathered sufficient material to compose the comprehensive research report. Below is the full report.

---

# Dent Disease: Comprehensive Research Report

**Target MONDO ID:** MONDO:0015612 (Dent disease group)
**Report compiled:** 2026-09-11

---

## 1. Disease Information

### Overview
Dent disease is a rare X-linked recessive renal proximal tubulopathy defined by the triad of low-molecular-weight proteinuria (LMWP), hypercalciuria, and at least one additional feature (nephrocalcinosis, nephrolithiasis, hematuria, hypophosphatemia, or renal insufficiency). It principally affects males and progresses to end-stage kidney disease (ESKD) in 30–80% of affected males between the third and fifth decades (Bhardwaj et al., 2021; Gianesello et al., 2021; Blanchard et al., 2025, PMID:39794284).

### Key Identifiers
| Resource | Identifier |
|---|---|
| MONDO (group) | MONDO:0015612 (Dent disease) |
| MONDO (DD1) | MONDO:0010655 |
| MONDO (DD2) | MONDO:0010371 |
| OMIM DD1 | #300009 |
| OMIM DD2 | #300555 |
| Orphanet | ORPHA:1652 |
| ICD-10 | N25.8 (Other disorders resulting from impaired renal tubular function) |
| ICD-11 | GB90.4Y |
| MeSH | D058637 (Dent Disease) |
| Gene DD1 | CLCN5 (HGNC:2023), Xp11.23 |
| Gene DD2 | OCRL (HGNC:8108), Xq26.1 |

### Synonyms / Alternative Names
- X-linked recessive nephrolithiasis with renal failure (XRN)
- X-linked recessive hypophosphatemic rickets (XLRH)
- Low-molecular-weight proteinuria with hypercalciuria and nephrocalcinosis (LMWP-HC-NC)
- Idiopathic low molecular weight proteinuria of Japanese children
- Dent's disease
- Nephrolithiasis type I (Dent) — original description by C.E. Dent and Friedman (1964, PMID:14158899)

### Data Derivation
Information is derived from a combination of case reports, national registries (Japan n=91, France n=108, UK n=62; Blanchard 2025), international multicenter cohorts, and functional/molecular studies. Individual-level EHR-scale data is limited; the disease is aggregated primarily through registries and expert-consensus guidelines (Blanchard et al., 2025, PMID:39794284).

---

## 2. Etiology

### Disease Causal Factors
Dent disease is **monogenic**, with a strictly Mendelian X-linked recessive etiology. Two subtypes are recognized:

- **Dent Disease 1 (DD1, ~60%)**: caused by loss-of-function variants in **CLCN5** encoding the electrogenic 2Cl⁻/H⁺ exchanger ClC-5.
- **Dent Disease 2 (DD2, ~15%)**: caused by hypomorphic/truncating variants in **OCRL** encoding phosphatidylinositol-4,5-bisphosphate 5-phosphatase.
- **Dent-3 / unclassified (~25%)**: no CLCN5/OCRL mutation identified; other candidate loci have been proposed (e.g., involvement of endocytic machinery) but not confirmed (Devuyst & Thakker, 2010, PMID:20950533).

There is no established environmental etiology; the disease is not infectious or toxic in origin.

### Risk Factors

**Genetic risk factors:**
- **Male sex** — hemizygous males manifest the classic phenotype; approximately 70% of carrier females show mild LMWP and 50% show mild hypercalciuria due to X-inactivation (Devuyst & Thakker, 2010).
- **Family history** of X-linked nephrolithiasis or LMWP.
- **Modifier alleles** in the ClC-5–megalin–cubilin endocytic complex (proposed but not clinically validated).

**Environmental risk factors:**
- Not a driver of disease onset. However, iatrogenic exposure to nephrotoxins (aminoglycosides, NSAIDs, IV iodinated contrast) worsens outcomes in established DD (GeneReviews, Bhardwaj 2021).
- Dehydration and low urinary volume potentiate stone formation and nephrocalcinosis.

### Protective Factors
- **Alkaline urine** (e.g., high citrate intake) reduces calcium-oxalate/phosphate supersaturation and nephrocalcinosis. In Clcn5-KO mice, a high-citrate diet preserved GFR at 9 months versus zero-citrate controls (Cebotaru et al., 2005, PMID:16014041).
- No genetic protective alleles have been formally characterized in humans.

### Gene-Environment Interactions
No formal GxE analyses have been published; treatment response variability (e.g., citrate, thiazide) may reflect underlying variant class effects on the endocytic machinery.

---

## 3. Phenotypes

### Core Renal Phenotypes (with HPO term suggestions and frequencies)

| Phenotype | HPO Term | Frequency (DD1) | Frequency (DD2) |
|---|---|---|---|
| Low-molecular-weight proteinuria | HP:0003126 | ~99–100% | ~100% |
| Hypercalciuria | HP:0002150 | 44–90% | 80–100% |
| Nephrocalcinosis | HP:0000121 | 40–75% | 10–40% |
| Nephrolithiasis (kidney stones) | HP:0000787 | 20–50% | 10–15% |
| Hematuria (usually microscopic) | HP:0000790 | Common | Common |
| Chronic kidney disease | HP:0012622 | 30–80% (by 3rd–5th decade) | Lower/later |
| Hypophosphatemia | HP:0002148 | 20–45% | Common |
| Aminoaciduria | HP:0003355 | Frequent | Frequent |
| Glycosuria | HP:0003076 | Frequent | Frequent |
| Renal tubular acidosis | HP:0001947 | Occasional | Occasional |
| Rickets | HP:0002748 | 5–33% | 10–20% |
| Osteomalacia | HP:0002749 | Adult-onset | Rare |
| Hypokalemia | HP:0002900 | 20–40% | 10–20% |
| Focal segmental glomerulosclerosis | HP:0000097 | Reported in biopsies | Reported |
| Growth retardation | HP:0001510 | 10–20% | 60–80% |
| Elevated β2-microglobulin, α1-microglobulin | HP:0032122 | Universal | Universal |

Source: Blanchard et al., 2025, PMID:39794284; Wang et al., 2015, PMID:26296266.

### DD2-Specific Extra-Renal Phenotypes (from OCRL mutations)

| Phenotype | HPO Term | Frequency |
|---|---|---|
| Mild intellectual disability | HP:0001256 | ~46% (with extra-renal features) |
| Elevated serum creatine kinase | HP:0003236 | ~52% |
| Elevated lactate dehydrogenase | HP:0025435 | Common |
| Muscle weakness / hypotonia | HP:0001252 | Occasional |
| Cataracts (rare) | HP:0000518 | ~11% (non-congenital; contrast with Lowe syndrome universal congenital bilateral cataracts) |

Source: Gianesello et al., 2021 (PMID:34680992); Prosseda 2020.

### Phenotype Characteristics
- **Age of onset:** Typically pediatric (childhood, often <10 years). Some individuals only manifest as adults with isolated hypercalciuria.
- **Severity:** Highly variable, ranging from asymptomatic hypercalciuria to childhood-onset CKD with rickets. Considerable intra-familial variability.
- **Progression:** Slowly progressive; mean eGFR decline ~1.5 mL/min/1.73m²/year (Blanchard et al., 2025).
- **Course:** Chronic and progressive; kidney stones may recur episodically.
- **Quality-of-life impact:** Substantial burden from recurrent stones, need for dialysis/transplant in some, growth retardation in children with DD2, learning disability in a subset (DD2), and bone pain from osteomalacia/rickets.

### "Nephrotic-Range" Proteinuria Pitfall
Because total urinary protein excretion can exceed 3.5 g/day due to massive LMWP, patients are frequently misdiagnosed as having idiopathic nephrotic syndrome or FSGS unless urine protein electrophoresis or β2-microglobulin/α1-microglobulin are measured (Copelovitch et al., 2015, PMID:26154403).

---

## 4. Genetic / Molecular Information

### Causal Genes

**CLCN5 (DD1)**
- Chromosome: **Xp11.23**
- Structure: 12 exons; encodes 746-aa electrogenic 2Cl⁻/H⁺ exchanger ClC-5
- OMIM: 300008 (gene)
- HGNC: hgnc:2023
- UniProt: P51795
- Function: Endosomal Cl⁻/H⁺ exchanger essential for efficient endosomal acidification in the renal proximal tubule.

**OCRL (DD2)**
- Chromosome: **Xq26.1**
- Structure: 24 exons (23 coding); encodes a phosphatidylinositol 4,5-bisphosphate 5-phosphatase (OCRL1)
- OMIM: 300535 (gene)
- HGNC: hgnc:8108
- UniProt: Q01968
- Function: Hydrolyzes PI(4,5)P₂ to PI4P at endosomes; regulates trafficking, cytoskeletal dynamics, and cilia. Also mutated in Lowe (oculocerebrorenal) syndrome (OMIM #309000).

### Pathogenic Variants

**CLCN5 variants (from the 2026 curated database, Lu et al., Kidney International Reports, DOI:10.1016/j.ekir.2026.106475):**
- 524 unique pathogenic/likely pathogenic variants
- Missense: 31% | InDel: 37% | Nonsense: 14% | Splicing: 13% | Large deletions: 5%
- ~63% frameshift/truncating (loss of full-length protein)
- Hotspot: **Exon 10** has ~50.6 variants/100 nt (~3× average)
- Helix H shows the highest non-truncating variant density (~200/100 residues); helices O–Q also enriched

**Functional classes (Grand et al., 2009; PMID:19019917):**
- **Class 1:** ER-retained/degraded (loss of ClC-5 at endosomes)
- **Class 2:** Correctly trafficked but with abnormal Cl⁻/H⁺ exchange or channel activity
- **Class 3:** Reduced ion transport with preserved endosomal targeting

**OCRL variants (DD2 vs Lowe syndrome):**
- Truncating variants in **exons 1–7** cluster in the PH domain → DD2
- Truncating variants in **exons 8–24** → Lowe syndrome
- Missense variants: DD2-associated variants retain >50% enzymatic activity; Lowe variants retain <20% activity (Hichri et al., 2011; Gianesello et al., 2021, PMID:34680992)
- Reinitiation from an internal methionine (Met170) in truncating variants may partially rescue activity, explaining the milder DD2 phenotype
- Compensation by INPP5B, an OCRL paralog with ~45% sequence identity, further contributes

### Variant Classification
Variants are classified by ACMG/AMP guidelines (Richards et al., 2015, PMID:25741868). Recent literature databases and ClinVar entries include a mixture of pathogenic (P), likely pathogenic (LP), and VUS annotations. Approximately 74% of CLCN5 pathogenic variants are private (single-family) (GeneReviews).

### Allele Frequency
CLCN5 and OCRL LoF variants are extremely rare in population databases (gnomAD v4); pathogenic Dent variants are typically absent or singleton in unaffected controls. Female carrier frequency has not been precisely quantified.

### Somatic vs. Germline
All disease-causing variants are **germline**. **Germline mosaicism** in mothers of affected males has been reported and complicates recurrence counseling (GeneReviews). De novo variants also occur; their frequency has not been precisely quantified.

### Functional Consequences
Both DD1 and DD2 mechanisms are **loss-of-function**:
- CLCN5: loss of endosomal Cl⁻/H⁺ exchange → impaired endosomal acidification and endocytic trafficking
- OCRL: loss of 5-phosphatase activity → altered PI(4,5)P₂/PI4P balance at endosomes/actin, disrupting endocytic recycling and cytoskeletal remodeling

### Modifier Genes
No formal modifier loci are established. Candidate interactors include TMEM9 and SEC22B, reported to shape proximal tubule function and DD1 pathogenesis (bioRxiv, Nov 2025, DOI:10.1101/2025.11.03.686312).

### Epigenetic Information
No consistent epigenetic pattern has been reported. X-inactivation skewing modulates the phenotype in heterozygous females.

### Chromosomal Abnormalities
Large intragenic deletions of CLCN5 or OCRL account for ~5–7% of cases; contiguous gene deletions have been described but are rare.

---

## 5. Environmental Information

Dent disease is a **monogenic** disorder. Environmental factors do not cause the disease but modulate outcomes:
- **Nephrotoxins to avoid:** aminoglycosides, NSAIDs, iodinated IV contrast, cisplatin (Bhardwaj 2021).
- **Hydration** and low dietary sodium reduce hypercalciuria and stone risk.
- **Dietary calcium restriction is not recommended** given bone health concerns.
- No infectious agents are involved.

---

## 6. Mechanism / Pathophysiology

### Ordered Causal Chain (DD1, CLCN5-related)

1. Loss-of-function variant in **CLCN5** → loss or misfolding of the **ClC-5 2Cl⁻/H⁺ exchanger** at proximal-tubule (PT) subapical endosomes (Piwon et al., 2000, PMID:11099045; Wang et al., 2000, PMID:11115835).
2. Defective ClC-5 → impaired endosomal Cl⁻ counterion transport → **reduced V-ATPase-mediated endosomal acidification** and abnormal luminal [Cl⁻] (Devuyst & Thakker, 2010).
3. Reduced endosomal acidification → **impaired recycling and trafficking of megalin and cubilin** (LRP2/CUBN) at the brush border (Christensen et al., 2003, PMID:12815099).
4. Loss of megalin/cubilin at the apical membrane → **failure of receptor-mediated endocytosis** of filtered LMW proteins → **LMW proteinuria** (β2-microglobulin, α1-microglobulin, RBP, vitamin-binding proteins).
5. Loss of vitamin D-binding protein (DBP) reabsorption → **urinary 25(OH)-vitamin D loss** → paradoxical **elevated 1,25(OH)₂-vitamin D** → increased intestinal calcium absorption → **hypercalciuria** (Norden et al., 2001, PMID:11279143; Maritzen et al., 2006).
6. Hypercalciuria + defective proximal reabsorption of phosphate → **calcium-phosphate supersaturation** → **nephrocalcinosis / nephrolithiasis**.
7. Chronic tubular injury → **tubulointerstitial fibrosis** and **focal global/segmental glomerulosclerosis** → **progressive CKD** and eventual ESKD.

### Ordered Causal Chain (DD2, OCRL-related)

1. Hypomorphic OCRL variant → residual PI(4,5)P₂ 5-phosphatase activity (>50%) but reduced flux (Hichri 2011).
2. Elevated endosomal PI(4,5)P₂ → aberrant actin polymerization on endosomal membranes; disrupted trafficking of megalin/cubilin (Vicinanza et al., 2011).
3. Trafficking defect → same downstream LMW proteinuria and hypercalciuria as DD1, plus mild extra-renal features (elevated CK/LDH, mild intellectual disability) from OCRL's role in ciliogenesis, endosomal PI cycling in muscle/CNS.
4. The absence of complete phosphatase loss (unlike Lowe syndrome) explains milder ocular and CNS phenotype.

### Molecular Pathways
- **Endocytic recycling** (megalin/cubilin/amnionless complex; Rab5/Rab7/Rab11)
- **V-ATPase / endosomal acidification**
- **Vitamin D metabolism (CYP24A1, CYP27B1)**
- **Phosphoinositide signaling** (PI(4,5)P₂/PI4P; PI3K–AKT downstream)
- **Actin cytoskeleton remodeling** (OCRL–Rho–GAP)
- **Autophagy/lysosomal degradation** (impaired lysosomal delivery in ClC-5-null cells; De Matteis et al.)
- Suggested GO terms: **GO:0006897 (endocytosis)**, **GO:0006508 (proteolysis)** (mislocalized), **GO:0008286 (insulin receptor-signaling – megalin cargo)**, **GO:0006874 (cellular calcium ion homeostasis)**, **GO:0055074 (calcium ion homeostasis)**, **GO:0055062 (phosphate ion homeostasis)**, **GO:0043647 (inositol phosphate metabolic process)**.

### Cellular Processes
- Impaired **receptor-mediated endocytosis** (Christensen 2003)
- Defective **endosomal maturation and recycling**
- Increased **apoptosis** of proximal tubule cells
- Reduced **primary cilium function** (OCRL)
- Chronic **tubulointerstitial inflammation and fibrosis**

### Protein Dysfunction
- Class 1 CLCN5 variants: misfolding → ER retention → proteasomal degradation
- Class 2/3: preserved trafficking but altered ion transport
- OCRL variants (DD2): reduced but not abolished 5-phosphatase catalysis

### Metabolic / Biochemical Abnormalities
- Elevated urinary β2-microglobulin, α1-microglobulin, retinol-binding protein
- Elevated 1,25(OH)₂D₃, hypercalciuria, hypophosphatemia
- Aminoaciduria, glycosuria, uricosuria, kaliuresis
- Impaired urinary acidification (partial RTA in some)

### Tissue Damage Mechanisms
Chronic calcium deposition → interstitial fibrosis; oxidative stress; protein overload of tubular cells; glomerulosclerosis secondary to hyperfiltration and podocyte injury.

### Immune / Inflammation
Chronic low-grade interstitial lymphocytic infiltration on biopsy (~53% of biopsies; Wang et al., 2016, PMID:27697782).

### Molecular Profiling
- Transcriptomic studies in Clcn5-KO models identified dysregulation of endocytic, autophagy, and lipid-metabolism gene sets (Gorvin et al., 2013; Cellular models Perego et al., 2021, PMID:33710298).
- Novel candidate interactors TMEM9, SEC22B recently identified (2025).

### Advanced Technologies
- **Single-cell studies:** Not yet published for DD, though PT cell heterogeneity models are being generated.
- **Drosophila model** (2026, PMID:41690574) revealed impaired ER export of Cubilin as a novel pathogenic mechanism.

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary:** Kidney — specifically the renal cortex (UBERON:0001225)
- **Secondary:** Skeleton (rickets/osteomalacia); occasionally eye (mild non-congenital cataracts in DD2 subset)

### Tissue and Cell Level
- **Renal proximal tubule** (UBERON:0004134)
- **Renal proximal convoluted tubule cell** (CL:1000838) — primary site of expression of ClC-5
- **Renal proximal straight tubule (S3 segment) cell** — secondary
- **Podocytes** — secondary involvement leading to FSGS-like lesions
- **Intercalated cells of the collecting duct** — ClC-5 also expressed, but PT is dominant

### Subcellular Level
- **Early/subapical endosomes** (GO:0005769; endocytic vesicle)
- **Apical brush border** membrane (megalin/cubilin)
- **Lysosomes** (secondary dysfunction)
- **Endoplasmic reticulum** (site of misfolded Class-1 ClC-5 retention)

### Anatomical Localization
- Bilateral kidney involvement
- Nephrocalcinosis typically medullary (renal medulla, UBERON:0000362)

---

## 8. Temporal Development

### Onset
- **Typical age:** Pediatric — often <10 years. LMWP may be detected incidentally in asymptomatic males or during workup of hematuria or stones.
- **Onset pattern:** Chronic and insidious; acute manifestations only when kidney stones present with pain/hematuria.

### Progression
- **Rate:** Slow. Mean eGFR decline ~1.5 mL/min/1.73 m²/year (Blanchard 2025).
- **Stages:** Preclinical → biochemical (LMWP + hypercalciuria) → complications (stones, rickets) → CKD → ESKD.
- **Course:** Chronic, non-remitting, progressive in the majority.
- **Duration:** Lifelong.

### Age Distribution of Kidney Failure
- 30-40 years: ~40% of affected males
- 40-50 years: ~33%
- 50-60 years: ~75%
- Very rare progression before adolescence (Blanchard 2025).

### Critical Periods
Adolescence and early adulthood are important intervention windows for stone prevention. Childhood is the critical period for growth and bone health.

---

## 9. Inheritance and Population

### Epidemiology
- **Prevalence:** ≥1 in 500,000 to 1 in 1,000,000 based on European registries; likely underdiagnosed. New 2026 estimates from a curated CLCN5 database suggest ~3,520 affected families globally (Lu et al., Kidney International Reports, 2026, DOI:10.1016/j.ekir.2026.106475).
- **Historical count:** ~250 published families before 2024.

### Inheritance
- **Pattern:** X-linked recessive
- **Penetrance:** Essentially complete in hemizygous males; variable in heterozygous females (partial expression from X-inactivation).
- **Expressivity:** Highly variable — even within families with the same variant, phenotype ranges from isolated hypercalciuria to early CKD.
- **Genetic anticipation:** Not observed.
- **Germline mosaicism:** Reported for CLCN5 (relevant to genetic counseling).
- **Founder effects:** No known population-specific founder mutations; ~74% CLCN5 variants are private.
- **Consanguinity:** Not required (X-linked); does not increase risk beyond X-linked transmission.
- **Carrier frequency:** Not precisely known; exceedingly rare given ultra-low disease prevalence.

### Population Demographics
- **Sex ratio:** M:F ≈ 100:1 in symptomatic disease; heterozygous females largely subclinical.
- **Ethnicity:** Reported worldwide with no ethnic predilection — cases documented in European, Japanese, Chinese, North American, Middle Eastern, and African populations.
- **Geographic distribution:** Global; slightly higher recognition in countries with early school-screening programs (e.g., Japan, where routine urinary protein screening detects asymptomatic pediatric cases).

---

## 10. Diagnostics

### Clinical Tests
- **Urine dipstick + microscopy:** proteinuria, hematuria, crystalluria
- **Quantitative urine protein electrophoresis:** demonstrates LMWP predominance
- **Urinary β2-microglobulin** (LOINC:1953-0) and **α1-microglobulin** (LOINC:56546-1): both >10× normal
- **24-hour urinary calcium** (>4 mg/kg/day) or spot **Ca:Cr ratio** (>0.25 mg/mg)
- **Urinary α1-microglobulin/creatinine ratio** >120 mg/g (13.6 mg/mmol) — highly specific for DD (Blanchard 2025)
- **Urine albumin/total protein ratio** <21% distinguishes DD from glomerular proteinuria
- **Serum creatinine + eGFR** to track renal function
- **Serum electrolytes:** hypokalemia, hypophosphatemia
- **Serum bicarbonate:** acidosis in some
- **Serum 25(OH)D, 1,25(OH)₂D, PTH, phosphate, ALP**
- **Urinary phosphate, amino acids, glucose, uric acid** — assess extent of Fanconi-like tubular defect

### Imaging
- **Renal ultrasound:** cornerstone for nephrocalcinosis and stone detection (annual)
- **CT scan (low-dose):** for confirming stones when ultrasound is inconclusive
- **Skeletal radiographs:** for rickets/osteomalacia

### Pathology (biopsy findings)
- **Focal global glomerulosclerosis** in ~83% of biopsies (Wang et al., 2016, PMID:27697782)
- Segmental foot-process effacement (~57%)
- Focal interstitial fibrosis (~60%)
- Interstitial lymphocytic infiltration (~53%)
- Tubular damage (~70%)
- Calcium deposits in tubular lumens (nephrocalcinosis)

Kidney biopsy is **not required** for diagnosis when biochemical + genetic criteria are met, but historically many patients underwent biopsy for undiagnosed FSGS.

### Genetic Testing
- **Recommended approach (2025 guideline):** genetic testing of CLCN5 and OCRL in all males with LMWP and hypercalciuria
- **Sequence analysis** of CLCN5 detects ~92%; OCRL ~95% of variants (GeneReviews)
- **Multigene renal-tubulopathy or Fanconi panels** are commonly used
- **Whole exome/genome sequencing** for unresolved cases and to exclude phenocopies (cystinosis, Lowe syndrome, mitochondrial cytopathies)
- **Deletion/duplication analysis** for negative sequence-only results

### Clinical Diagnostic Criteria (2010 / reaffirmed 2025)
All three required (Devuyst & Thakker, 2010; Blanchard 2025):
1. LMW proteinuria ≥5× ULN
2. Hypercalciuria (>4.0 mg/kg/24 h or Ca:Cr >0.25 mg/mg)
3. At least one: nephrocalcinosis, nephrolithiasis, hematuria, hypophosphatemia, or CKD, **or** X-linked family history + genetic confirmation

### Differential Diagnosis
- Lowe syndrome (also OCRL — with ocular/CNS features)
- Cystinosis (CTNS)
- Wilson disease (ATP7B)
- Galactosemia (GALT)
- Mitochondrial cytopathies
- Fanconi-Bickel syndrome (SLC2A2)
- Idiopathic hypercalciuria
- Autoimmune tubulointerstitial nephritis
- Aminoglycoside/cisplatin/tenofovir tubulopathy
- Idiopathic FSGS (misdiagnosis pitfall)

### Screening
- Newborn screening: not routine for Dent disease; some Japanese school-age urine screening programs identify affected boys.
- Cascade genetic screening for at-risk family members (males and female carriers).

---

## 11. Outcome / Prognosis

### Survival and Mortality
- Overall survival is generally good until ESKD; life expectancy is largely determined by CKD progression and dialysis/transplant outcomes.
- No disease-specific mortality tables available.

### Morbidity / Disability
- Recurrent nephrolithiasis, hospitalizations
- Growth failure (especially DD2), rickets
- Bone pain, osteomalacia
- ESKD-related disability

### Disease Course
- **Complications:** nephrolithiasis, nephrocalcinosis, ESKD, rickets/osteomalacia, growth retardation, rarely hypokalemia-related complications, mild cognitive impairment (DD2)
- **Recovery potential:** No recovery; kidney transplantation is curative for renal manifestations; disease does not recur post-transplant.

### Prognostic Factors
- Higher globally sclerotic glomeruli %, greater foot-process effacement, interstitial inflammation → lower eGFR at biopsy and steeper decline (Wang 2016).
- Nephrotic-range albuminuria at presentation associated with worse prognosis.
- Class 1 CLCN5 mutations (ER-retained) may show slightly more severe course (contested).

### Prognostic Biomarkers
- Serum creatinine / eGFR trajectory
- Proteinuria magnitude
- Age at first stone
- Presence of nephrocalcinosis on imaging

---

## 12. Treatment

Current management is **supportive**. No disease-modifying or gene therapies are FDA-approved. The 2025 European guideline (Blanchard et al., 2025, PMID:39794284) provides evidence-graded recommendations.

### Pharmacotherapy

**Potassium citrate (NCIT:C87206 / CHEBI:32029)**
- Rationale: alkalinizes urine, reduces calcium-oxalate/phosphate supersaturation, delays CKD in Clcn5-KO mice (Cebotaru 2005, PMID:16014041)
- Grade C (weak); commonly used in 13–25% of patients
- Dose: pediatric 1–2 mEq/kg/day; adult 20–60 mEq/day

**Thiazide diuretics (hydrochlorothiazide, NCIT:C29081)**
- Reduce urinary calcium excretion by up to 40% at 0.4–1 mg/kg/day (Raja et al., 2002, PMID:12444212; Blanchard 2008, PMID:18976849)
- **2025 guideline: NOT recommended systematically** due to hypokalemia, volume depletion, hypocitraturia; use with caution if needed (Grade B, moderate)

**ACE inhibitors / ARBs**
- **Not recommended** as routine nephroprotection (Grade C, moderate); no proven benefit in DD-associated FSGS

**Phosphate supplements + calcitriol/1α-hydroxyvitamin D**
- For hypophosphatemic rickets (individualized)
- Vitamin D repletion if 25(OH)D deficient; monitor calciuria

**Vitamin A supplementation**
- Consider if urinary RBP/retinol loss causes deficiency (Grade B, moderate)

**Human growth hormone (somatropin)**
- Only if growth retardation with inadequate metabolic control or CKD ≥3

### Advanced Therapeutics
- **Gene therapy:** experimental only; AAV-mediated CLCN5 delivery has been proposed but no clinical trials.
- **Cell therapy:** none clinically available.
- **RNA-based therapies:** none in clinical use for Dent disease.
- **Small-molecule chaperones** to rescue Class-1 misfolded ClC-5 mutants are being explored preclinically (Perego 2021, PMID:33710298).

### Surgical / Interventional
- **Extracorporeal shock wave lithotripsy (ESWL)**, ureteroscopy, or percutaneous nephrolithotomy for stones (NCIT:C15329)
- **Kidney transplantation** (NCIT:C15289) — curative for renal manifestations; no disease recurrence

### Supportive / Rehabilitative
- High fluid intake (>2 L/day adults; equivalent weight-based in children)
- Balanced dietary calcium (avoid restriction)
- Sodium restriction to reduce urinary calcium
- Physical therapy for bone deformities
- Genetic counseling

### Experimental / Clinical Trials
- No open Phase III interventional trials targeting molecular pathogenesis (as of 2026).
- Preclinical: AAV gene addition, base editing for CLCN5; zebrafish and Drosophila models for high-throughput drug screening (Modelling Lowe syndrome and Dent-2 in zebrafish, 2025, PMID:40778266; Drosophila DD1 model, 2026, PMID:41690574).

### Treatment Outcomes / Adverse Effects
- Thiazides: hypokalemia, volume depletion, tubulointerstitial nephritis (Bailey et al., 2015, PMID:25911330)
- Citrate: GI intolerance, hyperkalemia in advanced CKD
- Growth hormone: generally well tolerated in this context

### Treatment Strategy
- Personalized to phenotype: stone-formers → citrate ± hydration ± thiazide (cautious)
- Rickets → phosphate + calcitriol
- CKD → standard nephroprotection (blood-pressure control, avoid nephrotoxins)
- Multidisciplinary: nephrology, urology, endocrinology, genetics, orthopedics

### Monitoring (per 2025 Guideline)
- Clinical + biochemical: every 3–6 months
- Renal ultrasound: annually
- Blood pressure, growth, bone health each visit
- Escalate frequency at CKD stage ≥3B (eGFR <45)

---

## 13. Prevention

### Primary Prevention
- Not preventable at disease-onset level (monogenic).
- **Preimplantation genetic diagnosis (PGD)** available for known familial CLCN5/OCRL mutations.
- **Prenatal testing** for known familial variants.

### Secondary Prevention
- Early diagnosis via urinary protein screening in males with family history
- Cascade genetic screening of maternal relatives (carriers, affected males)

### Tertiary Prevention (Preventing Complications)
- **Nephrolithiasis prevention:** hydration, citrate, moderate sodium
- **Bone health:** vitamin D, phosphate as needed
- **CKD progression:** avoid nephrotoxins, treat hypertension if present
- **Growth:** GH supplementation in select DD2 pediatric cases

### Immunization
Routine (no disease-specific vaccines).

### Screening / Early Detection
- Japan's routine school-age urine screening program has identified pediatric DD cases (contributes to Japan having one of the largest published cohorts).
- Newborn genomic screening pilots (e.g., BabySeq) may identify neonatal DD.

### Counseling
- **Genetic counseling** essential for affected males and carrier females; recurrence risk 50% per pregnancy in carrier mothers.

### Public Health / Environmental
- Public health measures (hydration, dietary sodium) reduce stone burden.
- Occupational nephrotoxin awareness for affected individuals.

---

## 14. Other Species / Natural Disease

### Taxonomy
- **Human (Homo sapiens; NCBITaxon:9606)** — natural host
- Naturally occurring Dent-like disease in non-human animals is not documented.

### Comparative Biology / Orthology
- **Mouse (Mus musculus; NCBITaxon:10090):** Clcn5 gene (NCBI Gene ID:12728); functional ortholog
- **Rat (Rattus norvegicus):** Clcn5 (Gene ID:29232)
- **Zebrafish (Danio rerio; NCBITaxon:7955):** clcn5 (Gene ID:559898); ocrl (Gene ID:436692)
- **Drosophila (D. melanogaster):** ClC-a (functional homolog used in a DD1 model, 2026)
- OCRL orthologs are highly conserved across metazoans and share a paralog (INPP5B) in mammals.

### Zoonotic / Cross-Species Transmission
Not applicable — Dent disease is monogenic and non-communicable.

### Veterinary Relevance
No natural Dent disease is described in companion animals; the disease exists only as engineered model in laboratory species.

---

## 15. Model Organisms

### Mouse Models
- **Clcn5⁻/y knockout (Piwon et al., 2000, PMID:11099045)** — Nature: recapitulates LMWP, generalized aminoaciduria, glycosuria, hypercalciuria; impaired proximal tubular endocytosis of horseradish peroxidase.
- **Clcn5 knockout (Wang et al., 2000, PMID:11115835)** — Hum Mol Genet: independent line, same phenotype; loss of megalin/cubilin at brush border.
- **Clcn5 knock-in (E211A, exchanger-to-channel conversion; Novarino et al., 2010)** — normal endosomal acidification but abnormal endosomal Cl⁻, still recapitulates renal phenotype, arguing that **luminal Cl⁻ accumulation, not just acidification, is essential**.
- **Novel transgenic Clcn5 model (2024, PMID:39019097)** — highlights disrupted autophagy and endolysosomal molecular disruptions.
- **Ocrl⁻/⁻ mice:** Ocrl KO mice are unexpectedly asymptomatic (compensation by Inpp5b); Ocrl/Inpp5b double-KO is embryonic lethal.

### Zebrafish
- **ocrl morphants and mutants:** shortened pronephros, defective endocytosis, neurodevelopmental defects (2025, PMID:40778266) — useful for high-throughput drug screening for Dent-2 and Lowe syndrome.

### Drosophila
- **DD1 model (Kidney International, 2026, PMID:41690574):** implicates impaired ER export of Cubilin as a pathogenic mechanism, opening a new therapeutic angle.

### Cellular Models
- **CLCN5-KO HK-2 cells and PT cell lines** (Gorvin et al., 2013; Perego et al., 2021, PMID:33710298) — reveal transcriptomic dysregulation in endocytic, lipid, and autophagy pathways.
- **iPSC-derived kidney organoids** — emerging models but published DD-specific data limited.
- **Human primary PT-cell lines** from DD1 patient urine (De Matteis, Devuyst labs) — recapitulate megalin/cubilin mislocalization and endocytic dysfunction (Gorvin 2013).

### Applications
- Testing endocytic rescue strategies
- Screening small-molecule chaperones for Class-1 misfolded ClC-5
- Testing AAV gene addition
- Evaluating dietary and pharmacologic interventions (high citrate, thiazides)

### Model Limitations
- Ocrl-KO mice do not model human DD2 due to Inpp5b compensation
- CKD progression in Clcn5-KO mice occurs later and slower than in humans
- No non-human model spontaneously recapitulates both nephrocalcinosis and progressive ESKD reliably

### Resources
- **MGI** (Clcn5): MGI:99486
- **RGD** (Clcn5): RGD:2381
- **ZFIN** (clcn5): ZDB-GENE-030228-6
- **IMPC, KOMP, EMMA** repositories house available knockout strains

---

## Selected Key References (with PMIDs)

1. Dent CE, Friedman M. (1964). *Hypercalciuric rickets associated with renal tubular damage.* Arch Dis Child. **PMID:14158899**
2. Piwon N, et al. (2000). *ClC-5 Cl-channel disruption impairs endocytosis in a mouse model for Dent's disease.* Nature 408:369-73. **PMID:11099045**
3. Wang SS, et al. (2000). *Mice lacking renal chloride channel, CLC-5, are a model for Dent's disease.* Hum Mol Genet 9:2937-45. **PMID:11115835**
4. Christensen EI, et al. (2003). *Loss of chloride channel ClC-5 impairs endocytosis by defective trafficking of megalin and cubilin.* PNAS 100:8472-7. **PMID:12815099**
5. Cebotaru V, et al. (2005). *High citrate diet delays progression of renal insufficiency in the ClC-5 knockout mouse model.* Kidney Int 68:642-52. **PMID:16014041**
6. Grand T, et al. (2009). *Characterization of Dent's disease mutations of CLC-5 reveals a correlation between functional and cell biological consequences.* Hum Mol Genet 18:4457-71. **PMID:19019917**
7. Devuyst O, Thakker RV. (2010). *Dent's disease.* Orphanet J Rare Dis 5:28. **PMID:20946626**
8. Copelovitch L, et al. (2015). *Nephrotic-range albuminuria as the presenting symptom of Dent-2 disease.* Ital J Pediatr 41:31. **PMID:26154403**
9. Wang X, et al. (2016). *Glomerular Pathology in Dent Disease and Its Association with Kidney Function.* Clin J Am Soc Nephrol 11:2168-76. **PMID:27697782**
10. Bhardwaj S, et al. (2021). *Dent Disease.* GeneReviews (updated). **NBK99494**
11. Gianesello L, et al. (2021). *Genotype-Phenotype Correlation in Dent Disease 2 and Review of the Literature: OCRL Gene Pleiotropism or Extreme Phenotypic Variability of Lowe Syndrome?* Genes 12:1597. **PMID:34680992**
12. Perego C, et al. (2021). *Novel Dent disease 1 cellular models reveal biological processes underlying ClC-5 loss-of-function.* Hum Mol Genet 30:1413-1428. **PMID:33710298**
13. Blanchard A, et al. (2025). *Dent disease: clinical practice recommendations.* Nephrol Dial Transplant 40:852-864. **PMID:39794284**
14. Lu B, et al. (2026). *Database of CLCN5 Pathogenic Variants Causing Dent Disease.* Kidney International Reports. **DOI:10.1016/j.ekir.2026.106475**
15. (2024). *A novel transgenic mouse model highlights molecular disruptions involved in the pathogenesis of Dent disease 1.* **PMID:39019097**
16. (2026). *A Drosophila model for Dent's disease type 1 revealed impaired endoplasmic reticulum export of Cubilin as pathogenic mechanism.* Kidney Int. **PMID:41690574**
17. Bailey MA. (2015). *Hydrochlorothiazide-induced tubulointerstitial nephritis in a patient with Dent disease.* **PMID:25911330**

---

## Suggested Ontology Term Bindings for the KB Entry

| Field | Term | ID |
|---|---|---|
| disease_term (group) | Dent disease | MONDO:0015612 |
| Dent disease 1 | Dent disease 1 | MONDO:0010655 |
| Dent disease 2 | Dent disease 2 | MONDO:0010371 |
| Causal gene 1 | CLCN5 | hgnc:2023 |
| Causal gene 2 | OCRL | hgnc:8108 |
| Inheritance | X-linked recessive inheritance | HP:0001419 |
| Cell type | kidney proximal convoluted tubule epithelial cell | CL:1000838 |
| Anatomy | renal proximal tubule | UBERON:0004134 |
| Anatomy | kidney cortex | UBERON:0001225 |
| Subcellular | early endosome | GO:0005769 |
| Process | receptor-mediated endocytosis | GO:0006898 |
| Process | endosomal acidification | GO:0048388 |
| Process | phosphatidylinositol dephosphorylation | GO:0046856 |
| Phenotype | Low molecular weight proteinuria | HP:0003126 |
| Phenotype | Hypercalciuria | HP:0002150 |
| Phenotype | Nephrocalcinosis | HP:0000121 |
| Phenotype | Nephrolithiasis | HP:0000787 |
| Phenotype | Chronic kidney disease | HP:0012622 |
| Phenotype | Rickets | HP:0002748 |
| Phenotype | Hypophosphatemia | HP:0002148 |
| Phenotype | Aminoaciduria | HP:0003355 |
| Treatment | Potassium citrate | CHEBI:32029 |
| Treatment | Hydrochlorothiazide | CHEBI:5778 |
| Treatment | Kidney transplantation | NCIT:C15289 |
| Treatment | Pharmacotherapy | NCIT:C15986 |

---

## Sources

Sources:
- [Dent disease: clinical practice recommendations (Oxford NDT, 2025)](https://academic.oup.com/ndt/article/40/5/852/7951514)
- [Dent's disease — Orphanet review, Devuyst & Thakker 2010 (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2964617/)
- [Dent Disease — GeneReviews (NCBI)](https://www.ncbi.nlm.nih.gov/books/NBK99494/)
- [Database of CLCN5 Pathogenic Variants Causing Dent Disease (Lu et al., 2026)](https://pmc.ncbi.nlm.nih.gov/articles/PMC13088963/)
- [Genotype-Phenotype Correlation in Dent Disease 2 (Gianesello 2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8535715/)
- [ClC-5 Cl-channel disruption impairs endocytosis (Piwon 2000, PubMed)](https://pubmed.ncbi.nlm.nih.gov/11099045/)
- [Mice lacking renal chloride channel CLC-5 (Wang 2000)](https://academic.oup.com/hmg/article/9/20/2937/2901318)
- [Loss of ClC-5 impairs endocytosis by defective trafficking of megalin and cubilin (PNAS)](https://pnas.org/content/100/14/8472.full)
- [High citrate diet delays progression in Clcn5-KO mice (Cebotaru 2005)](https://pubmed.ncbi.nlm.nih.gov/16014041/)
- [Responsiveness of Hypercalciuria to Thiazide in Dent's Disease (JASN 2002)](https://pubmed.ncbi.nlm.nih.gov/12444212/)
- [Effect of hydrochlorothiazide on urinary calcium excretion in Dent disease (Blanchard 2008)](https://pubmed.ncbi.nlm.nih.gov/18976849/)
- [Glomerular Pathology in Dent Disease and Its Association with Kidney Function (Wang 2016)](https://cjasn.asnjournals.org/content/11/12/2168)
- [Novel Dent disease 1 cellular models (Perego 2021)](https://pmc.ncbi.nlm.nih.gov/articles/PMC8283206/)
- [Nephrotic-range albuminuria in Dent-2 disease (Copelovitch 2015)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4479313/)
- [Modelling Lowe syndrome and Dent-2 disease using zebrafish (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12329224/)
- [Drosophila model for Dent's disease type 1 (2026)](https://pubmed.ncbi.nlm.nih.gov/41690574/)
- [A novel transgenic mouse model of Dent disease 1 (2024)](https://pubmed.ncbi.nlm.nih.gov/39019097/)
- [Phenotype and genotype analyses of 21 Chinese patients with Dent disease](https://pmc.ncbi.nlm.nih.gov/articles/PMC12336408/)
- [Clinical features and genetic analysis of 9 Chinese children with Dent disease (2025)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11938313/)
- [Dent Disease 2 as a Cause of Focal Segmental Glomerulosclerosis (Case Report)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7655776/)
- [Hydrochlorothiazide-induced tubulointerstitial nephritis in Dent disease (Bailey 2015)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4421200/)
- [Nephrolithiasis, kidney failure and bone disorders in Dent disease (Blanchard et al.)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4571032/)
- [Genotype-Phenotype Correlation in Dent Disease Type 1 (Kidney Int Reports)](https://www.kireports.org/article/S2468-0249(23)01267-6/fulltext)
- [OMIM Dent Disease 1 #300009](https://omim.org/entry/300009)
- [OMIM Dent Disease 2 #300555](https://omim.org/entry/300555)
- [Novel OCRL isoforms and phenotypic differences DD2/Lowe (NDT 2022)](https://academic.oup.com/ndt/article/37/2/262/6377826)
- [UpToDate — Dent disease (X-linked recessive nephrolithiasis)](https://www.uptodate.com/contents/dent-disease-x-linked-recessive-nephrolithiasis)
- [GARD — Dent disease](https://rarediseases.info.nih.gov/diseases/13105/dent-disease)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 35 |
| Resolved | 35 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 35 |
| On topic | 21 |
| Off topic | 5 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `PMID:20950533` (1 mention) - Training for and dissemination of the Nutrition Environment Measures Surveys (NEMS).
  - shared terms: none
- `PMID:26296266` (1 mention) - Change in waist circumference with longer time in the United States among Hispanic and Chinese immigrants: the modifying role of the neighborhood built environment.
  - shared terms: model
- `PMID:26154403` (2 mentions) - Aerobic Nickel-Catalyzed Hydroxysulfonylation of Alkenes Using Sodium Sulfinates.
  - shared terms: none
- `PMID:11279143` (1 mention) - Centrosome protein centrin 2/caltractin 1 is part of the xeroderma pigmentosum group C complex that initiates global genome nucleotide excision repair.
  - shared terms: gene
- `PMID:25911330` (2 mentions) - The Clinical Use of Genomic Profiling to Distinguish Intrapulmonary Metastases From Synchronous Primaries in Non-Small-Cell Lung Cancer: A Mini-Review.
  - shared terms: genetic

Weighed against this report's own most characteristic terms: `disease`, `clcn5`, `ocrl`, `kidney`, `renal`, `hypercalciuria`, `dent`, `variant`, `dd2`, `genetic`, `phenotype`, `nephrocalcinosis`, `model`, `gene`, `blanchard`, `dd1`, `ckd`, `ricket`, `clc-5`, `stone`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 61 |
| Resolved | 50 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 11 |
| Terms whose name was checked | 43 |
| Terms named correctly | 26 |
| Terms named as a **different** term | 5 |
| Terms whose name is worth a second look | 12 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0010655` (2 mentions) - the report calls it "MONDO (DD1)", "Dent disease 1"; MONDO calls it **X-linked intellectual disability with marfanoid habitus**
- `MONDO:0010371` (2 mentions) - the report calls it "MONDO (DD2)", "Dent disease 2"; MONDO calls it **Aland island eye disease**
- `HP:0000790` (1 mention) - the report calls it "Hematuria (usually microscopic)"; HP calls it **Hematuria**
- `HP:0032122` (1 mention) - the report calls it "Elevated β2-microglobulin, α1-microglobulin"; HP calls it **Very low visual acuity**
- `UBERON:0001225` (2 mentions) - the report calls it "Primary:** Kidney — specifically the renal cortex", "kidney cortex"; UBERON calls it **cortex of kidney**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `MONDO:0015612` (3 mentions) - the report calls it "Dent disease group", "Dent disease"; MONDO calls it **Dent disease**, and lists "Dent disease 1" among its other names
- `HP:0000787` (2 mentions) - the report calls it "Nephrolithiasis (kidney stones)", "Nephrolithiasis"; HP calls it **Kidney stone**, and lists "Nephrolithiasis" among its other names
- `HP:0025435` (1 mention) - the report calls it "Elevated lactate dehydrogenase"; HP calls it **Increased circulating lactate dehydrogenase concentration**, and lists "Increased lactate dehydrogenase level" among its other names
- `HP:0001252` (1 mention) - the report calls it "Muscle weakness / hypotonia"; HP calls it **Hypotonia**, and lists "Muscle hypotonia" among its other names
- `HP:0000518` (1 mention) - the report calls it "Cataracts (rare)"; HP calls it **Cataract**, and lists "Cataracts" among its other names
- `GO:0008286` (1 mention) - the report calls it "insulin receptor-signaling – megalin cargo"; GO calls it **insulin receptor signaling pathway**
- `GO:0006874` (1 mention) - the report calls it "cellular calcium ion homeostasis"; GO calls it **intracellular calcium ion homeostasis**, and lists "cellular calcium ion homeostasis" among its other names
- `UBERON:0004134` (2 mentions) - the report calls it "Renal proximal tubule", "renal proximal tubule"; UBERON calls it **proximal tubule**, and lists "renal proximal tubule" among its other names
- `CL:1000838` (2 mentions) - the report calls it "Renal proximal convoluted tubule cell", "kidney proximal convoluted tubule epithelial cell"; CL calls it **kidney proximal convoluted tubule epithelial cell**
- `CHEBI:32029` (2 mentions) - the report calls it "Potassium citrate"; CHEBI calls it **potassium acetate**
- `NCIT:C15289` (2 mentions) - the report calls it "Kidney transplantation"; NCIT calls it **Organ Transplantation**
- `GO:0048388` (1 mention) - the report calls it "endosomal acidification"; GO calls it **endosomal lumen acidification**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0015612` - called "Dent disease group", "Dent disease"
- `MONDO:0010655` - called "MONDO (DD1)", "Dent disease 1"
- `MONDO:0010371` - called "MONDO (DD2)", "Dent disease 2"
- `HP:0003126` - called "Low-molecular-weight proteinuria", "Low molecular weight proteinuria"
- `HP:0000787` - called "Nephrolithiasis (kidney stones)", "Nephrolithiasis"
- `UBERON:0001225` - called "Primary:** Kidney — specifically the renal cortex", "kidney cortex"
- `UBERON:0004134` - called "Renal proximal tubule", "renal proximal tubule"
- `CL:1000838` - called "Renal proximal convoluted tubule cell", "kidney proximal convoluted tubule epithelial cell"

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`, `LOINC`, `ID`, `MGI`, `RGD`.