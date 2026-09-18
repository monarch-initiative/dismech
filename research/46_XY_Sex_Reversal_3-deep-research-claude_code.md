---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-09-01T06:35:02.370179'
end_time: '2026-09-01T06:40:29.301987'
duration_seconds: 326.93
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: 46,XY sex reversal 3
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
  web_search_requests: 12
  num_turns: 16
  total_cost_usd: 1.2291169999999998
  session_id: a30dd6db-6ed6-5228-b1c5-d3969da15772
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 45
reference_validation:
  total_references: 28
  verified: 28
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 0
  quotes_unsupported: 1
  unsupported_quote_references:
  - PMID:17200175
  relevance_assessed: 28
  on_topic: 26
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 35
  verified: 33
  not_found: 0
  obsolete: 0
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 4
  labels_matching: 4
  unresolvable_prefixes:
  - OMIM
  adapter: 'ols:'
  validator_version: 0.4.5
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** 46,XY sex reversal 3
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **46,XY sex reversal 3** covering all of the
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

Good, I now have enough substantive detail across mechanism, genetics, and clinical spectrum. Let me fill remaining gaps: prevalence/epidemiology numbers, treatment specifics, and differential diagnosis/other DSD genes for context.

I have sufficient material now to compile a comprehensive report. Let me write it up.

# 46,XY Sex Reversal 3 (SRXY3) — Comprehensive Research Report

## 1. Disease Information

**Overview:** 46,XY sex reversal 3 (SRXY3), also referred to as 46,XY complete or partial gonadal dysgenesis due to NR5A1 mutation, is a monogenic disorder/difference of sex development (DSD) in which an individual with a 46,XY karyotype fails to undergo normal testis determination because of heterozygous loss-of-function (or, less commonly, dominant-negative/gain-of-function) mutation in **NR5A1**, the gene encoding steroidogenic factor 1 (SF-1, also called Ad4BP). The clinical presentation ranges from complete gonadal dysgenesis with a female phenotype and streak gonads (the "Swyer syndrome" end of the spectrum) to partial gonadal dysgenesis with ambiguous genitalia, to isolated hypospadias or male infertility in individuals with apparently normal external genitalia. Heterozygous female (46,XX) relatives carrying the same variant can present with primary ovarian insufficiency (POI) or, less commonly, 46,XX testicular/ovotesticular DSD — reflecting the pleiotropic, dose-sensitive role of SF-1 in gonadal development in both sexes.

**Key identifiers:**
- **OMIM:** #612965 — *46,XY SEX REVERSAL 3; SRXY3* (gene-disease relationship: NR5A1, OMIM gene 184757, chromosome 9q33.3)
- **Gene:** NR5A1 (HGNC:7983; also known as SF1, AD4BP, ELP, FTZF1, POF7, SRXY3, SF-1)
- **Note on nomenclature confusion:** SRXY3 (OMIM #612965) is caused by NR5A1. This is distinct from **SRXY6** (OMIM #618973), which is caused by **MAP3K1** — a different gene on a different pathway, frequently confused with SRXY3 in casual literature searches because both are "46,XY sex reversal" numbered entries and both converge on the same downstream ovarian-promoting transcriptional program (WNT4/β-catenin/FOXL2). This report focuses specifically on the **NR5A1-associated SRXY3** entity as requested.
- **Orphanet:** covered within "46,XY disorders of sex development" / "46,XY gonadal dysgenesis" umbrella terms (Orphanet does not maintain a separate numbered entry identical to OMIM's SRXY3 split; NR5A1-related DSD is cross-referenced under Orphanet gonadal dysgenesis entries).
- **MeSH/ICD-11:** falls under "46,XY disorder of sex development" (ICD-11 LD2A.1/related codes); MeSH term *Disorders of Sex Development*, *46, XY Disorder of Sex Development*.
- **Common synonyms:** NR5A1-related 46,XY DSD; SF-1-related gonadal dysgenesis; 46,XY complete/partial gonadal dysgenesis (NR5A1 type); Swyer syndrome (for the complete form, when caused by NR5A1); steroidogenic factor 1 deficiency (testis-restricted phenotype).

**Data provenance:** Nearly all disease knowledge derives from aggregated case reports, case series, and multi-center/international DSD registry cohorts (e.g., the I-DSD registry), rather than from a single large epidemiological or EHR-based population study — reflecting the rarity of the condition. Molecular mechanism data are drawn from a combination of human patient-variant functional studies (transactivation assays, cell-based reporter assays) and the mouse *Sf1*-knockout model.

## 2. Etiology

**Primary cause:** Heterozygous pathogenic variants in **NR5A1** (missense, nonsense, frameshift, splice-site, and rarely whole-gene deletions) that reduce SF-1's transcriptional activity toward genes required for testis differentiation, or in some cases produce protein with altered structural/interaction properties. Achermann et al. (1999) first identified a heterozygous 2-bp deletion in exon 3 of NR5A1 (disrupting the zinc-finger DNA-binding domain) in a 46,XY patient with complete gonadal dysgenesis and primary adrenal failure — establishing NR5A1 as a human DSD gene ([PubMed](https://pubmed.ncbi.nlm.nih.gov/)). Subsequent series (e.g., Lin et al. 2007, "Heterozygous missense mutations in steroidogenic factor 1…are associated with 46,XY disorders of sex development with normal adrenal function," [PMID:17200175](https://pubmed.ncbi.nlm.nih.gov/17200175/)) showed that most human NR5A1 variants causing DSD do **not** cause adrenal insufficiency, in contrast to the original report and to the murine null phenotype — indicating that human adrenal development is comparatively more resistant to SF-1 haploinsufficiency than gonadal (particularly testicular) development.

**Genetic risk factors:**
- Causal: heterozygous NR5A1 loss-of-function or dominant-negative variants (missense variants clustering in the DNA-binding domain [zinc fingers], the ligand-binding domain, and the hinge/FTZ-F1 box) — inherited in an **autosomal dominant** pattern with a striking degree of **sex-limited and variable expressivity**.
- Modifier/digenic contributions: because clinical phenotype varies even among carriers of the identical variant (including within families), additional genetic modifiers (in genes such as GATA4, WT1, MAP3K1, or others in the testis-determination network) are hypothesized but not fully characterized.
- The recurrent **p.Arg92Trp (R92W)** variant is notable as acting as a "molecular switch": it has been reported causing 46,XX testicular/ovotesticular DSD in some individuals and 46,XY (SRXY3) gonadal dysgenesis in a sibling within the same family, illustrating profound phenotypic plasticity from a single allele.

**Environmental risk factors:** None established. This is a purely monogenic, cell-autonomous developmental gene-dosage disorder; no toxin, teratogen, maternal exposure, or infectious trigger has been implicated in human NR5A1-related DSD.

**Protective factors:** No specific protective genetic or environmental factor is described. 46,XX carriers of the same pathogenic variant are typically asymptomatic with normal fertility (variant is "silent" in the XX genetic background for gonadal sex, though can later manifest as POI) — this sex-limited penetrance is itself the notable modifying phenomenon, attributed to the fact that SF-1 haploinsufficiency compromises the SRY-dependent, dosage-sensitive tipping point of testis determination but is less rate-limiting for the (in a sense, "default") ovarian program.

**Gene–environment interactions:** None specifically documented; this is regarded as a cell-intrinsic transcriptional-network dosage disorder rather than one with meaningful gene–environment interaction.

## 3. Phenotypes

Phenotypic severity in SRXY3 forms a continuum, driven by the degree of residual SF-1 function and its impact on the testis-determination network:

**Complete form (Swyer-syndrome-like, "complete gonadal dysgenesis"):**
- Female external genitalia at birth (typical, unambiguous)
- Streak (fibrous, non-functional) gonads bilaterally
- Persistent Müllerian structures (uterus, fallopian tubes) — since Sertoli-cell-derived anti-Müllerian hormone (AMH) was never produced
- **Primary amenorrhea and absent pubertal development** at expected puberty age (no spontaneous breast development, no menarche) due to absence of functional gonadal estrogen production
- HPO suggestions: `HP:0008222` (Gonadal dysgenesis), `HP:0000813` (Streak gonad), `HP:0000141` (Delayed puberty)/`HP:0000786` (Primary amenorrhea), `HP:0000007`(?) not applicable; more precisely `HP:0000010` (Recurrent... n/a); `HP:0000141` (Delayed puberty), `HP:0000027` (Azoospermia n/a for female phenotype)

**Partial form (partial gonadal dysgenesis):**
- Ambiguous/atypical external genitalia at birth — clitoromegaly or micropenis/hypospadias spectrum, palpable or non-palpable gonads
- Variable Müllerian remnants (partial AMH production)
- Undervirilization at birth, with the striking phenomenon of **spontaneous virilization at puberty** in some individuals (rising endogenous androgen from residual Leydig-cell function overcoming initial ambiguity), described across multiple case series
- HPO: `HP:0000062` (Ambiguous genitalia), `HP:0000047` (Hypospadias), `HP:0000054` (Micropenis), `HP:0008670` (Bifid scrotum, if applicable)

**Mild/isolated form (male-appearing, later-presenting):**
- Isolated hypospadias without other genital ambiguity (NR5A1 variants found in ~5–7% of hypospadias-only cohorts)
- Bilateral anorchia ("vanishing testes syndrome")
- Male infertility (oligo/azoospermia) discovered in adulthood, with otherwise normal virilization — Leydig cell (testosterone) function relatively preserved while Sertoli cell/spermatogenic function fails
- HPO: `HP:0000028` (Cryptorchidism), `HP:0000798` (Anorchia), `HP:0000027` (Azoospermia), `HP:0012735` (Cervical... n/a)

**46,XX carriers (heterozygous, same variant, different karyotype):**
- Primary ovarian insufficiency: secondary or primary amenorrhea, hypergonadotropic hypogonadism, infertility, hypoestrogenism (HPO: `HP:0008209` Primary ovarian failure, `HP:0000786` Primary amenorrhea)
- Rarely, 46,XX testicular or ovotesticular DSD (NR5A1 established as a novel disease gene for this presentation — Genetics in Medicine, 2017)

**Phenotype characteristics:**
- *Onset:* Congenital (genital phenotype apparent at birth in ambiguous/female-appearing cases) or delayed presentation to puberty/adulthood in mild/isolated cases (hypospadias, infertility, POI)
- *Severity:* Highly variable, spanning a spectrum from complete female phenotype to normally virilized infertile male, even within the same family and same genotype
- *Progression:* Generally non-progressive structurally (gonadal dysgenesis is a fixed developmental outcome), but clinical detection of gonadoblastoma/dysgerminoma risk is a time-dependent complication requiring surveillance
- *Frequency among cohorts:* NR5A1 variants account for roughly 4–20% of 46,XY DSD cases depending on cohort selection and sequencing depth (a commonly cited range is ~8–15%; one random unselected cohort found 9.2% [9/98]; a hypospadias-inclusive series found 6.5% [5/77])
- *Quality of life impact:* Significant psychosocial burden from gender-identity considerations in ambiguous-genitalia presentations, infertility (frequently permanent, as streak/dysgenetic gonads lack functional gametes), need for lifelong hormone replacement, and anxiety around gonadal malignancy surveillance/prophylactic gonadectomy decisions.

## 4. Genetic/Molecular Information

**Causal gene:** NR5A1 (Nuclear Receptor Subfamily 5 Group A Member 1), HGNC:7983, chromosome 9q33.3, OMIM gene *184757. Encodes steroidogenic factor 1 (SF-1/Ad4BP), an orphan nuclear receptor transcription factor with an N-terminal zinc-finger DNA-binding domain (two C4-type zinc fingers plus an "FTZ-F1 box" that confers additional DNA-binding specificity), a hinge region, and a C-terminal ligand-binding domain (LBD) that also mediates protein–protein interactions and coactivator recruitment.

**Variant spectrum:**
- Missense variants predominate and cluster in the zinc-finger DNA-binding domain and the LBD; nonsense, frameshift, and splice-site variants (leading to premature termination) are also reported (e.g., p.Lys38*, p.Leu80Trpfs*8, c.1138+1G>T)
- ClinVar entries specifically linked to "46,XY sex reversal 3" include variants such as NM_004959.5(NR5A1):c.274C>T (p.Arg92Trp) — the recurrent variant discussed above
- Structural modeling studies (Domenice et al., *Human Molecular Genetics* 2019, [doi:10.1093/hmg/ddz002](https://dx.doi.org/10.1093/hmg/ddz002) — note: this reference specifically concerns MAP3K1 domain disruption and should not be conflated with NR5A1 structural work, included here for completeness of the SRXY-family literature) have been complemented by NR5A1-specific structural analyses showing that variants can destabilize the zinc-finger fold or disrupt LBD coactivator-binding surfaces.
- **Functional consequence:** predominantly **loss-of-function/haploinsufficiency** — reduced transactivation of SF-1 target promoters in reporter assays (e.g., CYP11A1, StAR, AMH, INSL3 promoters), consistent with a dosage-sensitive threshold model of testis determination.
- **Allele frequency:** NR5A1 pathogenic variants causing DSD are individually rare/private (mostly absent or at extremely low frequency in gnomAD), consistent with a dominant, largely sporadic/de novo or small-family-transmitted disorder; no common population variant is disease-causing.
- **Somatic vs. germline:** All reported NR5A1 DSD-causing variants are **germline**; no somatic mosaicism series is a defining feature of this entity (distinct from some other DSD genes).
- **Inheritance verification:** Both **de novo** and **familial (inherited from an unaffected or POI-affected mother)** transmissions are documented; de novo missense variants have been specifically reported (e.g., a de novo p.Arg313Cys variant with distal hypospadias).

**Modifier genes:** Not firmly established; genotype–phenotype correlation is explicitly reported as poor/absent even for identical variants — implicating unidentified genetic background modifiers (candidate network partners: GATA4, WT1, ZFPM2/FOG2, MAP3K1, SOX9) or stochastic developmental variation.

**Epigenetic information:** No disease-specific DNA methylation or histone-modification signature has been established for NR5A1-related DSD in humans; SF-1 itself, however, is known to interact with chromatin-remodeling and coactivator complexes (e.g., SRC/p160 family, CBP/p300) as part of its normal transcriptional mechanism, which is disrupted by LBD-domain mutations.

**Chromosomal abnormalities:** SRXY3 is a single-gene disorder; it is distinct from cytogenetic 46,XY sex-reversal syndromes caused by SRY deletion/translocation, Xp duplications, or 9p/10q deletions encompassing DMRT1/other dosage-sensitive sex genes — these represent differential diagnoses rather than part of the SRXY3 mechanism per se.

## 5. Environmental Information

No environmental toxins, occupational exposures, radiation, lifestyle factors, or infectious agents are implicated in NR5A1-related 46,XY sex reversal. This is consistent with its classification as a purely monogenic developmental disorder of a cell-autonomous transcription-factor network. (This section is included per the template for completeness; searches of CTD, PubMed, and toxicology literature returned no disease-specific environmental etiology.)

## 6. Mechanism / Pathophysiology

**Causal chain (numbered, from initiating lesion to clinical manifestation):**

1. A heterozygous pathogenic **NR5A1** variant is inherited or arises de novo, reducing the transcriptional activity (or, less often, altering the target specificity) of one SF-1 allele — **leads to** reduced total SF-1 dosage/activity in the bipotential genital ridge during the critical window of gonadal sex determination (~week 6–9 of human gestation).
2. Reduced SF-1 activity **impairs synergistic co-activation, together with WT1, GATA4/FOG2, and CBX2, of SRY expression** at its testis-specific enhancer (demonstrated mechanistically for the murine ortholog; a conserved NR5A1-responsive enhancer regulating SRY has been directly identified — [Nature Communications 2024](https://www.nature.com/articles/s41467-024-47162-2)) — **results in** insufficient or delayed SRY transcription in pre-Sertoli precursor cells.
3. Insufficient SRY, combined with SF-1's direct synergistic role at the *SOX9* testis-specific enhancer core (TESCO/Enh13, where NR5A1 binding sites act together with SRY-, SOX9-, and GATA4-binding sites) — **leads to** failure to reach the threshold level of SOX9 up-regulation required to commit Sertoli cell precursors to the male pathway (this is inferred largely from the mouse enhancer-dissection literature and extrapolated to humans, since direct human enhancer perturbation data are unavailable).
4. Failure of the SOX9-driven feed-forward loop **results in** failure of Sertoli cell differentiation (or only partial/delayed differentiation in partial forms) — **leads to** deficient or absent Sertoli-cell products: anti-Müllerian hormone (AMH/MIS) is reduced or absent, and downstream Leydig-cell recruitment/differentiation signals (e.g., DHH from Sertoli cells) are diminished.
5. Reduced/absent AMH **results in** persistence of Müllerian duct derivatives (uterus, fallopian tubes, upper vagina) — a direct, well-demonstrated consequence, not inferred.
6. In parallel, SF-1 haploinsufficiency **directly impairs Leydig cell steroidogenic gene transactivation** — SF-1 is a master regulator of *StAR*, *CYP11A1*, *CYP17A1*, *HSD3B2*, and *INSL3* promoters — **leading to** reduced fetal testosterone and INSL3 production, which **results in** incomplete masculinization of the Wolffian ducts and external genitalia (micropenis, hypospadias, cryptorchidism, or complete female external genitalia depending on severity).
7. Concomitantly, insufficient testis-pathway commitment **permits activation of the "default"/pro-ovarian transcriptional program** — increased CTNNB1 (β-catenin) signaling and upregulation of WNT4 and FOXL2, with decreased SRY/SOX9 — **branch point:** in cells where this ovarian-promoting program dominates, gonadal tissue differentiates toward ovarian-like/streak morphology rather than testicular morphology, producing the dysgenetic ("streak") gonad seen pathologically. (This WNT4/FOXL2 mechanistic detail is best documented for the related MAP3K1 disorder but is understood to converge on the same testis-vs-ovary bistable switch that SF-1 dosage also gates — the general principle, not necessarily every specific factor, is thought to extend to NR5A1-mediated dysgenesis.)
8. Dysgenetic gonadal tissue, especially when intra-abdominal/streak in morphology and retaining Y-chromosome material, **carries an elevated risk of malignant germ cell transformation** (gonadoblastoma, progressing to dysgerminoma/other germ cell tumors) — this is a well-established downstream clinical consequence, driving surveillance/prophylactic gonadectomy recommendations, rather than a primary mechanistic step.
9. In the postnatal/pubertal period, absent or deficient gonadal sex-steroid production (estrogen from dysgenetic tissue, or androgen in partial forms) **results in** absent/incomplete secondary sexual characteristic development, primary amenorrhea (in female-raised individuals), or, at the milder end, isolated infertility with otherwise normal pubertal virilization when Leydig-cell function is relatively spared but Sertoli/spermatogenic function is not.

**Molecular pathways involved:** Nuclear receptor signaling (NR5A1/SF-1 pathway); WNT/β-catenin signaling (WNT4–CTNNB1–FOXL2 axis) as the counter-programming pathway; steroidogenesis pathway (StAR–CYP11A1–CYP17A1–HSD3B2 cascade); TGF-β family signaling downstream (AMH/AMHR2 signaling for Müllerian regression).
- GO suggestions: `GO:0007548` (sex differentiation), `GO:0008406` (gonad development), `GO:0071371` (cellular response to gonadotropin), `GO:0060009` (Sertoli cell development), `GO:0060009`, `GO:0030238` (male sex determination), `GO:0060065` (uterus development, for retained Müllerian structures), `GO:0006694` (steroid biosynthetic process).

**Cellular processes:** Failure of Sertoli cell commitment/differentiation from bipotential supporting-cell precursors; impaired Leydig cell steroidogenic differentiation; apoptosis of the developing genital ridge has been specifically documented as the mechanism underlying gonadal *agenesis* in the complete murine *Sf1*-null phenotype (SF1-deficient mice show "complete adrenal and gonadal agenesis owing to apoptosis in the developing genital ridge").

**Protein dysfunction:** Loss-of-function via disrupted DNA binding (zinc-finger domain variants abolish or reduce sequence-specific promoter binding), disrupted ligand/coactivator binding (LBD variants), or reduced protein stability/nuclear localization (frameshift variants altering C-terminal sequence have been shown to alter subcellular SF-1 localization in at least one functional study of NR5A1 frameshift mutants).

**Biochemical abnormalities:** Reduced transactivation of steroidogenic enzyme promoters (StAR, CYP11A1, CYP17A1, HSD3B2) in reporter assays; reduced AMH promoter transactivation; reduced INSL3 expression.

**Immune system involvement:** None described; not an immune-mediated disease.

**Tissue damage mechanisms:** Not applicable in the classic "damage" sense (this is a developmental patterning failure rather than an acquired-injury disease); however, secondary tissue consequences include streak-gonad fibrosis and, critically, neoplastic transformation risk in retained dysgenetic gonadal tissue.

**Molecular/omics profiling:** Disease-specific transcriptomic/proteomic/single-cell atlases of human NR5A1-mutant gonadal tissue are limited (tissue is rarely available prior to gonadectomy, and gonadectomy is often performed early); most single-cell and spatial transcriptomic insight into the SF-1-dependent testis-determination network derives from **mouse gonad single-cell atlases** (e.g., Human Cell Atlas / GEO datasets of E10.5–E13.5 mouse genital ridge), which have mapped Nr5a1 expression to bipotential and pre-Sertoli/pre-granulosa somatic gonadal progenitors, rather than from human disease-tissue omics.

## 7. Anatomical Structures Affected

**Organ level:**
- Primary: gonads (testes fail to form normally; streak gonads or dysgenetic testes result), and (secondarily, as a consequence of absent/reduced AMH) internal Müllerian-derivative structures (uterus, fallopian tubes, upper vagina)
- Secondary/complication organs: adrenal cortex (rarely affected in humans, in contrast to mouse model, but a subset of NR5A1 variants — particularly those affecting the LBD — has been associated with primary adrenal insufficiency); external genitalia (penis/clitoris, urethra, labioscrotal folds) reflecting the degree of prenatal androgen exposure
- Body systems: reproductive/endocrine system primarily; the hypothalamic–pituitary–gonadal (HPG) axis secondarily, with hypergonadotropic hypogonadism as the biochemical hallmark in adolescence/adulthood

**Tissue and cell level:**
- Bipotential gonadal ridge somatic cells (the cell population expressing NR5A1 earliest, prior to sex-specific differentiation)
- Sertoli cells (CL:0000216) — primary affected cell type on the testis-determination side; fail to differentiate/mature
- Leydig cells (CL:0000178) — steroidogenic function impaired
- Granulosa cells (CL:0000501) and theca cells — the "default" cell fates that streak-gonad tissue may partially adopt
- Germ cells — indirectly affected; abnormal niche support predisposes to malignant transformation (gonadoblastoma cells)

**Subcellular level:**
- Nucleus (GO:0005634) — SF-1 is a nuclear receptor transcription factor; variants affecting nuclear localization signals disrupt normal nuclear accumulation
- Chromatin/promoter-bound transcriptional complexes (GO:0000785, GO:0005667) — site of SF-1's DNA-binding and coactivator-recruitment function

**Localization:** Bilateral gonads (intra-abdominal in dysgenetic/streak presentations, which is itself clinically important because intra-abdominal cryptorchid position confers higher tumor risk than a scrotal position); internal Müllerian structures in the pelvis; external genitalia (perineal/genital tubercle-derived structures). Typically **bilateral and symmetric** in presentation, though asymmetric gonadal differentiation (unilateral streak, contralateral dysgenetic testis — "mixed gonadal dysgenesis"-like patterns) can occur, more classically described with Y-chromosome mosaicism but occasionally reported with NR5A1 variants as well.

## 8. Temporal Development

**Onset:** Congenital at the level of underlying gonadal maldevelopment (occurs in utero during the sex-determination window, ~6th–9th week of gestation), but clinical **presentation** can be:
- Neonatal (ambiguous genitalia noted at birth)
- Infantile (bilateral anorchia, isolated hypospadias)
- Pubertal (delayed/absent puberty, primary amenorrhea in female-raised complete gonadal dysgenesis cases; spontaneous virilization in some partial cases)
- Adult (infertility as the presenting complaint in individuals with normal genitalia and secondary sexual characteristics)

**Progression:** The underlying gonadal dysgenesis itself is a fixed, non-progressive developmental outcome (streak gonads do not "further degenerate" in a classic progressive sense), but the **clinical course** includes a time-dependent risk trajectory for germ-cell malignant transformation in retained gonadal tissue, which increases with age if gonads are not removed — this is the key "disease course" consideration driving management timing.

**Disease stages:** Not formally staged in an oncologic sense; clinically categorized descriptively as complete vs. partial gonadal dysgenesis based on degree of testicular differentiation and genital virilization (Prader-like scoring is sometimes applied to genital ambiguity).

**Critical periods:** The sex-determination window in utero (roughly Carnegie stages 17–23 / 6th–9th gestational week) is the critical window during which SF-1 dosage must reach the threshold for SRY/SOX9 upregulation; after this window closes, gonadal fate (testis vs. streak/ovarian-like) is essentially fixed. Puberty is a second clinically important "critical period" — it is when the functional consequences of gonadal dysgenesis (absent pubertal maturation) typically first become clinically undeniable in previously unrecognized cases, and it is also the recommended time to initiate hormone replacement therapy.

**Remission patterns:** Not applicable — this is a structural developmental condition, not a relapsing-remitting disease.

## 9. Inheritance and Population

**Epidemiology:** No population-based incidence/prevalence figure specific to NR5A1-related SRXY3 exists (as is typical for rare monogenic DSD subtypes); the disorder is characterized instead through its representation within 46,XY DSD cohorts. NR5A1 variants are found in roughly **4–20%** of 46,XY DSD cases across published series, with commonly cited midpoint estimates around **8–15%**; specific cohort figures include 9.2% (9/98, unselected cohort), 6.5% (5/77, hypospadias-inclusive cohort), and 7.04% (5/71, another regional cohort). 46,XY DSD overall (all causes) is estimated at roughly 1 in 4,500–5,000 live births, making NR5A1-attributable SRXY3 an ultra-rare condition on a population basis.

**Inheritance pattern:** **Autosomal dominant**, with pronounced **sex-limited penetrance** — virtually complete penetrance for a gonadal/genital phenotype in 46,XY carriers, but the same variant in 46,XX carriers usually produces no gonadal-sex-reversal phenotype (normal fertility in most 46,XX carriers), though a meaningful subset later develop primary ovarian insufficiency, and rarely 46,XX testicular/ovotesticular DSD.

**Penetrance:** Near-complete for the 46,XY gonadal phenotype, though **expressivity is highly variable** even within a single pedigree carrying an identical variant (siblings can present anywhere from complete female phenotype to normally virilized male with isolated infertility) — indicating that penetrance of the *specific severity* is not deterministic even though penetrance of *some* phenotypic effect in 46,XY individuals is very high.

**Expressivity:** Markedly variable, as above; explicitly reported in the literature that there is "no specific genotype–phenotype correlation," even for the identical variant.

**Genetic anticipation:** Not described — NR5A1 variants are conventional point mutations/indels, not a repeat-expansion mechanism, so anticipation is not expected and is not reported.

**Germline mosaicism:** Not specifically well-characterized as a recurrent feature, though as with any autosomal dominant disorder it remains a theoretical mechanism for unaffected-parent transmission and should be considered in genetic counseling for recurrence risk when a parent tests negative on peripheral blood but a child is affected.

**Founder effects:** No specific population founder variant has been widely reported for NR5A1 SRXY3; variants are generally private/family-specific.

**Consanguinity:** Not a major factor, consistent with a dominant (not recessive) inheritance mechanism; consanguinity is more relevant to recessive DSD genes (e.g., some steroidogenesis enzyme deficiencies) than to NR5A1.

**Carrier frequency:** Not applicable in the traditional recessive-carrier sense, since this is a dominant disorder; population database (gnomAD) frequency of specific pathogenic NR5A1 alleles is essentially zero/near-absent, consistent with high selective/reproductive pressure against penetrant variants (via infertility) balanced by ongoing de novo mutation.

**Population demographics:** No specific ethnic or geographic enrichment has been robustly established; cohorts have been reported across European, Ukrainian, East Asian, Australasian, and other populations, with geographic/ethnic differences in the *specific variant spectrum* noted (e.g., the Frontiers 2024 worldwide cohort study of 46,XY DSD genetic diagnoses specifically examined geographic/ethnic differences in variant distribution across genes including NR5A1). Sex ratio is definitionally skewed toward clinical ascertainment in 46,XY individuals (since that is the karyotype in which the phenotype is fully penetrant), though 46,XX carriers are ascertained via POI/infertility workups or family cascade testing. Age distribution spans neonatal through adult presentation as described above.

## 10. Diagnostics

**Clinical/laboratory tests:**
- Karyotype (46,XY) — foundational diagnostic step in any DSD evaluation
- Basal and hCG-stimulated testosterone, and Leydig-cell-function testing to assess masculinization potential
- AMH and inhibin B levels (low/undetectable in complete gonadal dysgenesis, reflecting absent Sertoli cell function) — LOINC-codable biomarkers
- Gonadotropins (LH, FSH) — elevated (hypergonadotropic hypogonadism pattern) once gonadal failure occurs, particularly evident at expected puberty
- Pelvic ultrasound/MRI to assess for presence/absence of uterus and to attempt gonadal localization (though streak gonads are frequently not reliably visualized by imaging — "difficulty in detecting streak gonads using MRI" is specifically noted in the surgical-management literature, which is why prophylactic gonadectomy timing decisions often precede definitive imaging confirmation)

**Genetic testing:**
- Targeted NR5A1 single-gene sequencing, or (more commonly now) a **46,XY DSD multigene panel** (including SRY, NR5A1, MAP3K1, SOX9, WT1, DHH, GATA4, ZFPM2, DHX37, and others) or **exome/genome sequencing** — increasingly the diagnostic modality of choice, markedly increasing diagnostic yield versus historical single-gene Sanger sequencing
- Chromosomal microarray to exclude structural chromosomal causes of 46,XY sex reversal (e.g., SRY-region deletion, Xp21 duplication (DAX1/NR0B1), 9p or 10q deletions)
- Segregation/familial cascade testing is important given the AD, sex-limited inheritance — testing mothers/sisters for POI risk counseling

**Clinical criteria:** No formal DSM/ICD-style diagnostic algorithm exists beyond standard DSD diagnostic pathways (karyotype + hormonal profile + imaging + genetic testing), as codified in international DSD consensus statements (e.g., the Chicago Consensus and its updates).

**Differential diagnosis:** Other monogenic causes of 46,XY complete/partial gonadal dysgenesis must be excluded/considered in parallel, including: **SRY** mutation/deletion, **MAP3K1** (SRXY6), **SOX9** (campomelic dysplasia spectrum), **WT1** (Denys-Drash and Frasier syndromes), **DHH**, **GATA4**/**ZFPM2 (FOG2)**, **DHX37**, **CBX2**, **DMRT1** (9p deletion), and androgen biosynthesis/action defects (5-alpha-reductase deficiency, complete androgen insensitivity syndrome — though these differ mechanistically by preserving normal testis formation with a downstream hormonal defect rather than primary gonadal dysgenesis).

**Screening:** Not part of routine newborn screening programs (NR5A1 DSD is identified via clinical suspicion from ambiguous genitalia, not a biochemical newborn screen analyte); genetic counseling and targeted cascade genetic testing is offered to at-risk relatives once a proband variant is identified, particularly for POI risk counseling in female relatives and reproductive/family-planning counseling in male carriers who wish to have children.

## 11. Outcome/Prognosis

**Survival/mortality:** Not a life-limiting condition per se; mortality risk, when present, relates almost entirely to unrecognized/unsurveilled gonadal malignancy (gonadoblastoma progressing to invasive dysgerminoma or other germ cell tumor) rather than to the underlying endocrine/developmental defect itself. With appropriate surveillance/prophylactic gonadectomy, prognosis for survival is excellent and comparable to the general population.

**Morbidity:**
- Infertility is a near-universal and often irreversible consequence in the complete/partial gonadal dysgenesis forms (streak gonads lack functional germ cells); milder/isolated presentations may retain some fertility potential, though impaired
- Lifelong dependence on hormone replacement therapy (estrogen ± progesterone in female-raised individuals following gonadectomy; testosterone if indicated in male-raised individuals with inadequate endogenous production) to achieve pubertal development, maintain bone density, and support cardiovascular/metabolic health
- Psychosocial morbidity related to DSD diagnosis disclosure, gender identity, body image, and fertility loss is well recognized as a major component of long-term quality of life in this population, though disease-specific quantitative QOL instrument data (EQ-5D/SF-36) specific to NR5A1-DSD were not identified in available literature (most QOL literature on DSD is broader, cross-etiology).

**Complications:**
- **Gonadoblastoma and dysgerminoma** — the principal, well-characterized complication, driving management guidelines
- Osteoporosis/reduced bone mineral density if hormone replacement is inadequate or delayed
- Rarely, primary adrenal insufficiency in the subset of variants affecting adrenal-relevant SF-1 function (requiring monitoring for adrenal crisis risk in these specific cases)

**Recovery potential:** The underlying gonadal dysgenesis is not reversible; management is entirely substitutive/preventive (hormone replacement, tumor-risk mitigation) rather than curative. Assisted reproduction using donor gametes and, in female-raised individuals with a preserved uterus, gestational surrogacy or (where the uterus is retained and functional) donor-egg IVF with the individual's own uterus, are reproductive options that have been described in the DSD literature generally.

**Prognostic factors:** Degree of residual gonadal (particularly Sertoli/Leydig) function correlates with pubertal developmental potential and fertility prognosis; intra-abdominal gonadal location correlates with higher malignancy risk than a scrotal/inguinal position.

## 12. Treatment

**Pharmacotherapy (hormone replacement):**
- Estrogen replacement (e.g., transdermal or oral estradiol) initiated around the expected age of puberty in female-raised individuals with gonadal failure, to induce breast development and support bone/cardiovascular health — NCIT term candidate: `NCIT:C15986` (Pharmacotherapy), with therapeutic agent specifics (e.g., estradiol) as `therapeutic_agent`
- Progesterone/progestin added subsequently for endometrial protection and cycle regulation in those with a retained uterus
- Testosterone replacement in male-raised individuals with inadequate endogenous Leydig cell function

**Surgical/interventional:**
- **Prophylactic gonadectomy** (typically laparoscopic) — historically recommended for essentially all 46,XY gonadal dysgenesis cases with intra-abdominal streak/dysgenetic gonads, given the elevated germ cell tumor risk; more recent, nuanced surgical-management literature (2025 narrative review) discusses individualized approaches — "well-formed testes may be preserved under strict surveillance" while "streak-like intra-abdominal gonads carry high germ cell tumor risk, warranting early gonadectomy" — reflecting an evolving, more conservative paradigm balancing endogenous hormone production/fertility potential against tumor risk. NCIT candidate: `NCIT:C15329` (Surgical Procedure) / more specific gonadectomy term if available.
- Genital reconstructive surgery (feminizing or masculinizing genitoplasty) is considered based on sex of rearing, individual/family preference, and current DSD-care consensus emphasizing delayed, patient-involved decision-making where feasible for non-emergent procedures.

**Supportive/psychosocial care:**
- Genetic counseling for the patient and at-risk relatives (particularly regarding POI risk in female relatives)
- Psychological support and DSD-specialized multidisciplinary team involvement (endocrinology, urology/gynecology, genetics, psychology) — reflected in modern guidelines' emphasis on individualized, multidisciplinary management

**Fertility-related interventions:**
- Fertility preservation counseling prior to gonadectomy where any viable gonadal/germ cell tissue exists (increasingly discussed in recent literature, e.g., the 2025 case series on postoperative hormone replacement and fertility preservation in Swyer syndrome with dysgerminoma)
- Assisted reproductive technology (donor oocyte/sperm as needed; gestational options where uterus is present and functional)

**Experimental/investigational:** No gene-specific targeted molecular therapy (e.g., small molecule SF-1 agonist to rescue transactivation) has reached clinical development for NR5A1-related DSD; management remains substitutive/surgical rather than mechanism-correcting. No disease-specific registered clinical trials (NCT) targeting NR5A1 gonadal dysgenesis mechanism-correction were identified; trials in this space are more typically registry/natural-history studies (e.g., I-DSD registry-linked cohort studies) rather than interventional drug trials.

**Treatment algorithm considerations:** Timing of gonadectomy relative to puberty/hormone initiation is an active area of clinical judgment — some protocols recommend gonadectomy before starting estrogen replacement specifically because streak gonads are difficult to characterize by imaging once hormonally suppressed/altered.

## 13. Prevention

**Primary prevention:** Not applicable in the classic sense — this is a de novo/inherited monogenic condition with no modifiable environmental risk factor; primary prevention of the underlying mutation itself is not possible with current technology (though preimplantation genetic testing (PGT-M) is a reproductive option for known-carrier families wishing to avoid transmission).

**Secondary prevention (early detection):** Prompt recognition of ambiguous genitalia at birth and appropriate DSD diagnostic workup (karyotype, hormonal evaluation, genetic testing) allows early identification, enabling timely surveillance planning for gonadal malignancy risk and appropriately timed hormone replacement to avoid missed/delayed puberty.

**Tertiary prevention:** Prophylactic gonadectomy (or structured surveillance for retained gonads) specifically functions as tertiary prevention against gonadoblastoma/dysgerminoma progression; hormone replacement functions as tertiary prevention against osteoporosis and cardiovascular sequelae of prolonged hypogonadism.

**Genetic counseling:** Central to prevention-adjacent care in this disorder — counseling addresses recurrence risk for future pregnancies (50% transmission risk per pregnancy for an affected/carrier parent, with karyotype-dependent phenotypic expression), POI risk disclosure and reproductive planning for female carriers, and cascade testing of at-risk relatives. Prenatal and preimplantation genetic testing are options for families with an identified pathogenic variant who wish to inform reproductive decisions.

**Screening:** No population-level newborn or carrier screening program exists for NR5A1 (unlike some other rare disease categories with established newborn screening panels); detection is exclusively via clinical/genetic ascertainment.

## 14. Other Species / Natural Disease

**Taxonomy/orthologs:** NR5A1 is highly conserved; mouse ortholog *Nr5a1* (NCBI Gene, MGI-catalogued); zebrafish has two co-orthologs, **nr5a1a** and **nr5a1b**, arising from the teleost genome duplication.

**Natural disease in other species:** No well-documented spontaneous/naturally occurring NR5A1-mutant DSD phenotype in companion animals or wildlife was identified in available literature (unlike some other Mendelian disease genes with veterinary natural-disease counterparts cataloged in OMIA); the primary cross-species data come from engineered/laboratory models rather than naturally occurring veterinary cases.

**Comparative biology:** The testis-determination role of SF-1/Nr5a1 is deeply conserved across vertebrates — from fish through mammals, Nr5a1 is one of the earliest markers of gonadal somatic cell differentiation, generally expressed in the bipotential gonad **before** SRY (in species with an SRY-based system), underscoring its role as a foundational, upstream node of the gonadal-competence network rather than a sex-specific switch itself (its dosage, and cooperating partners, is what tips the sex-specific outcome).

## 15. Model Organisms

**Mouse (primary model):**
- **Constitutive *Sf1* (Nr5a1) knockout mice** (Luo, Ikeda, Parker, *Cell* 1994) — the foundational model: homozygous null mice show complete **adrenal and gonadal agenesis**, **XY male-to-female sex reversal** of internal and external genitalia, persistent Müllerian structures, impaired pituitary gonadotrope marker expression, and agenesis of the ventromedial hypothalamic nucleus (VMH); mice die neonatally from adrenal insufficiency, necessitating conditional/tissue-specific approaches for later-stage study.
- **Mechanism established in this model:** gonadal/adrenal agenesis results from **apoptosis in the developing genital ridge** in the absence of Sf1.
- **Conditional/tissue-specific knockouts** (e.g., Sertoli-cell-specific *Sf1* deletion) have been used to dissect its **post-sex-determination role in Sertoli cell survival** — demonstrating an ongoing maintenance requirement beyond the initial determination window, not just an initiation role.
- **Heterozygous *Sf1*+/− mice** and various knock-in point-mutant mice modeling specific human variants have been generated to study dosage sensitivity and genotype-specific effects, informing the human haploinsufficiency model.
- **Limitations:** the mouse model shows obligate, fully penetrant adrenal insufficiency with homozygous loss, which is **not** representative of the human heterozygous, adrenal-sparing phenotype typical of most human NR5A1 DSD cases — a clear human-model mismatch relevant to translational interpretation (heterozygous mouse models more closely, though still imperfectly, recapitulate the human dosage-sensitive gonadal phenotype).

**Zebrafish:**
- Two co-orthologs, *nr5a1a* and *nr5a1b*; *nr5a1a* is required for **Sertoli cell survival post sex determination** (PMC6418149), analogous to the mouse conditional-knockout finding, and links to the *cyp19a1a* (aromatase)/*foxl2* ovarian-differentiation pathway as an activator, situating Nr5a1a at the same testis/ovary network node conserved from fish to mammals.
- Zebrafish offer high-throughput genetic and live-imaging tractability for dissecting early somatic gonadal cell (SGC) specification, though zebrafish sex determination is not SRY-dependent, limiting direct translational modeling of the SRY-SF1 enhancer interaction central to the mammalian mechanism.

**Cellular/in vitro models:**
- Heterologous cell-based reporter/transactivation assays (e.g., in adrenal, Leydig, and Sertoli cell lines such as JEG-3, TM3/TM4, or COS cells transfected with wild-type vs. mutant NR5A1 constructs) are the standard functional-validation approach for novel human variants, used across essentially all the cited human-variant characterization studies (e.g., Lin et al. 2007 tested loss-of-function in adrenal, Leydig, and Sertoli cell lines).
- Patient-derived iPSC and gonadal organoid modeling of NR5A1 variants represents an emerging but not yet extensively published approach for this specific gene (general DSD organoid/iPSC modeling is an active research direction across the field, but disease-specific NR5A1 organoid literature was not identified in this search).

**Applications:** These models collectively enable study of (1) the transcriptional threshold/dosage mechanism of testis determination, (2) the SF-1–SRY–SOX9 enhancer synergy, (3) the ongoing post-determination maintenance role of SF-1 in Sertoli cell survival, and (4) structure-function characterization of specific human missense variants for clinical variant classification (ACMG/AMP functional-evidence criteria).

---

## Ontology Term Summary (suggested bindings)

| Category | Term |
|---|---|
| Gene | HGNC:7983 (NR5A1) |
| Disease (OMIM) | OMIM:612965 |
| Phenotype (HP) | HP:0008222 Gonadal dysgenesis; HP:0000813 Streak gonad; HP:0000062 Ambiguous genitalia; HP:0000047 Hypospadias; HP:0000028 Cryptorchidism; HP:0000798 Anorchia; HP:0000027 Azoospermia; HP:0000786 Primary amenorrhea; HP:0008209 Primary ovarian failure |
| GO Biological Process | GO:0008406 gonad development; GO:0007548 sex differentiation; GO:0030238 male sex determination; GO:0060009 Sertoli cell development; GO:0060065 uterus development |
| Cell Type (CL) | CL:0000216 Sertoli cell; CL:0000178 Leydig cell; CL:0000501 granulosa cell |
| Anatomy (UBERON) | UBERON:0000992 gonad; UBERON:0000995 uterus; UBERON:0000473 testis |
| Treatment (NCIT) | NCIT:C15986 Pharmacotherapy (estrogen/progesterone/testosterone replacement); NCIT:C15329 Surgical Procedure (gonadectomy) |

---

### Sources

- [Entry - #612965 - 46,XY SEX REVERSAL 3; SRXY3 - OMIM](https://www.omim.org/entry/612965)
- [Entry - #613762/#618973 - 46,XY SEX REVERSAL 6; SRXY6 (MAP3K1) - OMIM](https://omim.org/entry/613762)
- [MAP3K1 Variant Causes Hyperactivation of Wnt4/β-Catenin/FOXL2 Signaling — PMC8927045](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8927045/)
- [Pathogenic Variants in MAP3K1 Cause 46,XY Gonadal Dysgenesis: A Review - PubMed 35290982](https://pubmed.ncbi.nlm.nih.gov/35290982/)
- [MAP3K1-related gonadal dysgenesis: Six new cases and review of the literature - PubMed 28504475](https://pubmed.ncbi.nlm.nih.gov/28504475/)
- [Mutations in MAP3K1 cause 46,XY DSD... - PubMed 21129722](https://pubmed.ncbi.nlm.nih.gov/21129722/)
- [46,xy Sex Reversal 3 - MalaCards](https://www.malacards.org/card/46xy_sex_reversal_3_2)
- [46,XY sex reversal 3 - NORD/Mondo](https://rarediseases.org/mondo-disease/46xy-sex-reversal-3/)
- [ClinVar Miner: variants in NR5A1 for 46,XY sex reversal 3](https://clinvarminer.genetics.utah.edu/variants-by-mondo-condition/13066/gene/NR5A1)
- [NM_004959.5(NR5A1):c.274C>T (p.Arg92Trp) AND 46,XY sex reversal 3 - ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/RCV000256210/)
- [NR5A1 Loss-of-Function Mutations Lead to 46,XY Partial Gonadal Dysgenesis - PubMed 27463801](https://pubmed.ncbi.nlm.nih.gov/27463801/)
- [New NR5A1 mutations and phenotypic variations of gonadal dysgenesis - PMC5411087](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5411087/)
- [Four Novel NR5A1 Mutations... - PubMed 29190620](https://pubmed.ncbi.nlm.nih.gov/29190620/)
- [Five novel mutations in steroidogenic factor 1 (SF1, NR5A1)... - PMC2359628](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2359628/)
- [Wide spectrum of NR5A1-related phenotypes in 46,XY and 46,XX individuals - PMC5347970](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5347970/)
- [Case Report: Severe Gonadal Dysgenesis... Novel NR5A1 Variant - PMC9294228](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9294228/)
- [Pubertal development in 46,XY patients with NR5A1 mutations - PMC8816419](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8816419/)
- [Mutation Analysis of NR5A1 in 77 Patients with 46,XY DSD - PMC3197579](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3197579/)
- [New NR5A1 mutations and phenotypic variations of gonadal dysgenesis - PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0176720)
- [Genotype-phenotype correlation of NR5A1 variants - medRxiv](https://www.medrxiv.org/content/10.1101/2024.08.27.24312633.full.pdf)
- [Steroidogenic Factor 1, a Goldilocks Transcription Factor... - PMC9959402](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9959402/)
- [Steroidogenic factor-1 (SF-1, NR5A1) and human disease - PMC3057017](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3057017/)
- [Update--steroidogenic factor 1 (SF-1, NR5A1) - PubMed 20595937](https://pubmed.ncbi.nlm.nih.gov/20595937/)
- [Minireview: Steroidogenic Factor 1... - Molecular Endocrinology](https://academic.oup.com/mend/article/24/7/1322/2706129)
- [Heterozygous missense mutations in SF1/Ad4BP/NR5A1... - PubMed 17200175](https://pubmed.ncbi.nlm.nih.gov/17200175/)
- [Steroidogenic Factor 1: an Essential Mediator of Endocrine Development - Endocrine Society](https://www.endocrine.org/~/media/endosociety/files/ep/rphr/57/rphr_vol_57_ch_02_steroidogenic_factor.pdf)
- [The role of SF1 in adrenal and reproductive function - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S109671920200032X)
- [Clinical Spectrum, Surgical Management, and Outcomes of NR5A1-Related 46,XY DSD - PMC12654113](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12654113/)
- [Role of NR5A1 Gene Mutations in DSD: Molecular and Clinical Features - PMC11119465](https://pmc.ncbi.nlm.nih.gov/articles/PMC11119465/)
- [Novel NR5A1 variants associated with hypospadias and DSD - PMC12708181](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12708181/)
- [NR5A1 is a novel disease gene for 46,XX testicular and ovotesticular DSD - Genetics in Medicine](https://www.gimjournal.org/article/S1098-3600(21)02426-6/fulltext)
- [Ten novel mutations in NR5A1... 46,XX ovarian insufficiency - PubMed 22549935](https://pubmed.ncbi.nlm.nih.gov/22549935/)
- [The novel p.Cys65Tyr mutation in NR5A1... primary ovarian insufficiency - PMC3900668](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3900668/)
- [A conserved NR5A1-responsive enhancer regulates SRY in testis-determination - Nature Communications](https://www.nature.com/articles/s41467-024-47162-2)
- [GATA4 binding to the Sox9 enhancer mXYSRa/Enh13 - PMC11743149](https://pmc.ncbi.nlm.nih.gov/articles/PMC11743149/)
- [Worldwide cohort study of 46,XY DSD genetic diagnoses - PMC11194351](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11194351/)
- [Identification and functional analysis of fourteen NR5A1 variants - PubMed 32738419](https://pubmed.ncbi.nlm.nih.gov/32738419/)
- [Clinical and genetic characteristics of a large international cohort with rare NR5A1/SF-1 variants - ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2352396423005078)
- [46,XY Complete Gonadal Dysgenesis (Swyer Syndrome)... - PMC11746928](https://pmc.ncbi.nlm.nih.gov/articles/PMC11746928/)
- [Perspective on postoperative HRT and fertility preservation in Swyer syndrome with dysgerminoma - EJOG](https://www.ejog.org/article/S0301-2115(25)01133-9/fulltext)
- ['Size does matter': Prophylactic gonadectomy in Swyer syndrome - ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S2468784718304811)
- [Zebrafish as an emerging model to study gonad development - PMC7498840](https://pmc.ncbi.nlm.nih.gov/articles/PMC7498840/)
- [Steroidogenic Factor 1 (Nr5a1) is Required for Sertoli Cell Survival Post Sex Determination - PMC6418149](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6418149/)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 28 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 0 |
| Quoted claims **not** found in source | 1 |
| References weighed for topical relevance | 28 |
| On topic | 26 |
| Off topic | 0 |

### Quotes not found in the cited source

Searched the abstract, any retrieved full text, and the title. A quote drawn from a part of the paper that was not retrieved will appear here too, so check before treating one as invented:

- `PMID:17200175`: "Heterozygous missense mutations in steroidogenic factor 1…are associated with 46,XY disorders of sex development with normal adrenal function,"
  - closest text in source: "Taken together, these cases show that heterozygous missense mutations in NR5A1/SF1 are emerging as a relatively frequent association with 46,XY disorders of sex development with intact adrenal steroid biosynthesis"

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 35 |
| Resolved | 33 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 2 |
| Terms whose name was checked | 4 |
| Terms named correctly | 4 |
| Terms named as a **different** term | 0 |

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `OMIM`.

33 of 35 terms resolved to a current term; the rest could not be looked up either way.
