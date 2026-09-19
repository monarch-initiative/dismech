---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-opus-5[1m]
cached: false
start_time: '2026-08-16T10:01:38.451520'
end_time: '2026-08-16T10:19:18.966402'
duration_seconds: 1060.52
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Dihydropyrimidine Dehydrogenase Deficiency
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
  num_turns: 61
  total_cost_usd: 7.475237000000003
  session_id: 3f1db4b3-9a9e-4112-a013-3765d91d0eff
  stop_reason: end_turn
  permission_denials: 5
  denied_tools:
  - Bash
  assistant_text_blocks: 1
citation_count: 15
reference_validation:
  total_references: 40
  verified: 38
  not_found: 2
  unverifiable: 0
  confabulation_rate: 0.05
  quotes_checked: 3
  quotes_valid: 3
  unresolved_references:
  - PMID:31745289
  - PMID:9323575
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dihydropyrimidine Dehydrogenase Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dihydropyrimidine Dehydrogenase Deficiency** covering all of the
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

# Dihydropyrimidine Dehydrogenase Deficiency — Research Report for Knowledge Base Curation

> **A note on how to read this before you use it.** DPD deficiency is really *two diseases wearing one gene's coat*, and if you curate it as one blended entity you will end up with a pathograph that makes no sense. There is (a) a rare autosomal-recessive inborn error of pyrimidine catabolism with an infantile neurological presentation, and (b) an extremely common pharmacogenetic vulnerability in which otherwise-healthy people metabolize fluoropyrimidine chemotherapy so slowly that a standard dose becomes an overdose. Same enzyme, same gene, same biochemistry — completely different clinical entry points, evidence bases, and literature. I have kept the two causal chains structurally separate throughout, and Section 6 gives them as two distinct pathophysiology cascades. Genotype–phenotype correlation is famously weak *within* arm (a) and reasonably strong *within* arm (b).
>
> Confidence is flagged inline. Everything marked **[verified this session]** was pulled directly from PubMed/E-utilities, the gnomAD v4 GraphQL API, OLS4, the HPO API, or the HGNC REST API during this run. Items marked **[standard reference, not re-verified]** are widely stated in the literature but I did not independently confirm them here — treat those as leads requiring the usual dismech verification pass before they become evidence items.

---

## 1. Disease Information

### Overview

Dihydropyrimidine dehydrogenase (DPD) deficiency is an autosomal recessive disorder of pyrimidine catabolism caused by biallelic or monoallelic loss-of-function variation in *DPYD*. DPD is the first and rate-limiting enzyme of the three-step pyrimidine degradation pathway, converting uracil and thymine to 5,6-dihydrouracil and 5,6-dihydrothymine respectively, in an NADPH-dependent reduction.

Because the same enzyme is responsible for catabolizing >80% of an administered dose of 5-fluorouracil (5-FU), the deficiency has a dual identity: a classical inborn error of metabolism presenting in infancy with thymine-uraciluria and neurological disease, *and* the single most important pharmacogenetic determinant of severe and fatal fluoropyrimidine toxicity.

The canonical framing from the largest phenotype series **[verified this session]**:

> "Dihydropyrimidine dehydrogenase (DPD) deficiency is an autosomal recessive disease characterised by thymine-uraciluria in homozygous deficient patients and has been associated with a variable clinical phenotype."
> — Van Kuilenburg et al., *Hum Genet* 1999;104(1):1–9. **PMID:10071185**

And the pharmacogenetic framing **[verified this session]**:

> "Fluoropyrimidine treatment can result in severe toxicity in up to 30% of patients and is often the result of reduced activity of the key metabolic enzyme dihydropyrimidine dehydrogenase (DPD), mostly caused by genetic variants in the gene encoding DPD (DPYD)."
> — Henricks et al., *Lancet Oncol* 2018;19(11):1459–1467. **PMID:30348537**

### Key identifiers **[verified this session via OLS4 MONDO term + xrefs, and HGNC REST]**

| Resource | Identifier |
|---|---|
| **MONDO** | `MONDO:0010130` — dihydropyrimidine dehydrogenase deficiency |
| **OMIM (disease)** | `OMIM:274270` — DIHYDROPYRIMIDINE DEHYDROGENASE DEFICIENCY; DPYDD |
| **OMIM (gene)** | `OMIM:612779` — *DPYD* |
| **Orphanet** | `ORPHA:1675` (note: **not** ORPHA:37, a common misattribution) |
| **MeSH** | `MESH:D054067` |
| **NCIT** | `NCIT:C84672` |
| **DOID** | `DOID:14218` |
| **SNOMED CT** | `77365006` |
| **UMLS** | `C1959620` |
| **MedGen** | `409522` |
| **MedDRA** | `10052622` |
| **GARD** | `0000019` |
| **ICD-9** | `277.2` (MONDO relatedTo) |
| **ICD-11 foundation** | `701689290` |
| **HGNC** | `HGNC:3012` — *DPYD*, dihydropyrimidine dehydrogenase, 1p21.3 |
| **NCBI Gene** | `1806` |
| **Ensembl** | `ENSG00000188641` |
| **UniProt** | `Q12882` (DPYD_HUMAN) |
| **EC number** | EC 1.3.1.2 |

ICD-10 is conventionally **E79.8** (other disorders of purine and pyrimidine metabolism) **[standard reference, not re-verified]**.

### Synonyms **[verified this session, from MONDO exact/related synonyms]**

- DPD deficiency
- DPYD deficiency ("DYPD deficiency" appears as a typo-synonym in MONDO)
- Dihydrouracil dehydrogenase deficiency
- Familial pyrimidinaemia / familial pyrimidinemia
- Thymine-uraciluria; hereditary thymine-uraciluria (related synonym)
- Fluorouracil toxicity / 5-FU toxicity (used loosely for the pharmacogenetic arm; **do not treat as an exact synonym** — the toxicity is a drug reaction, not the metabolic disorder)

### Nature of the evidence base

This is an unusual disease for dismech because the two arms have **completely different data provenance**:

- **Inborn-error arm**: individual patient reports and small aggregated series. The largest single dataset is 22 patients from 17 families (PMID:10071185). Aggregated disease-level resources (OMIM, Orphanet, GARD) essentially summarize these case series.
- **Pharmacogenetic arm**: very large prospective cohorts and EHR/laboratory datasets. Deenen et al. screened 2,038 patients; Henricks et al. enrolled 1,181; the GPCO-RNPGx analysis covers **19,376 consecutive French patients** with paired phenotype and genotype. This arm has population-scale, individual-level data of a quality most rare diseases never see.

---

## 2. Etiology

### Primary causal factor

Germline loss-of-function variation in *DPYD* (1p21.3), inherited in an autosomal recessive fashion for the metabolic disease. For fluoropyrimidine toxicity risk the inheritance behaves as **codominant/gene-dosage**: heterozygotes have measurably reduced DPD activity and materially elevated toxicity risk, so from a drug-safety standpoint a single deleterious allele is clinically actionable.

*DPYD* is one of the largest genes in the human genome (~950 kb, 23 exons) **[standard reference, not re-verified]**, which matters mechanistically — it is a large mutational target, and this is part of why deep intronic and structural lesions are a recurring and under-ascertained cause (see Section 4).

### Genetic risk factors

The four variants with established clinical validity and the basis of every current guideline panel **[verified this session]**:

> "We assessed the effect of prospective screening for the four most relevant DPYD variants (DPYD\*2A [rs3918290, c.1905+1G>A, IVS14+1G>A], c.2846A>T [rs67376798, D949V], c.1679T>G [rs55886062, DPYD\*13, I560S], and c.1236G>A [rs56038477, E412E, in haplotype B3]) on patient safety..."
> — Henricks et al. 2018, **PMID:30348537**

The meta-analysis that established clinical validity for the latter two **[verified this session]**:

> "DPYD c.1679T>G was significantly associated with fluoropyrimidine-associated toxicity (adjusted RR 4·40, 95% CI 2·08-9·30, p<0·0001)... DPYD\*2A and c.2846A>T were also significantly associated with severe fluoropyrimidine-associated toxicity (adjusted RR 2·85, 95% CI 1·75-4·62, p<0·0001; and 3·02, 2·22-4·10, p<0·0001, respectively)."
> — Meulendijks et al., *Lancet Oncol* 2015;16(16):1639–1650. **PMID:26603945**

An ancestry-restricted risk allele **[verified this session]**:

> "The DPYD-Y186C variant was unique to individuals of African ancestry, and DPD activity was 46% lower in carriers as compared with noncarriers (279 ± 35 vs. 514 ± 168 pmol 5-FU min(-1) mg(-1); P = 0.00029). In this study, 26% of the African Americans with reduced DPD activity were carriers of Y186C."
> — Offer et al., *Clin Pharmacol Ther* 2013;94(1):158–166. **PMID:23588312**

### Environmental / non-genetic risk factors

For the **toxicity arm**, the environmental exposure is not incidental — it is the necessary trigger. The exposure is:

- 5-fluorouracil (intravenous), capecitabine (oral 5-FU prodrug), tegafur, and topical/cutaneous 5-FU. The DPWG guideline explicitly covers all three systemic agents and flags cutaneous exposure **[verified this session]**: *"subjects with a gene activity score of 0 are recommended to avoid systemic and cutaneous 5-fluorouracil or capecitabine"* (PMID:31745289).
- Iatrogenic overdose independent of genotype — infusion pump programming errors, dose miscalculation, accidental or intentional capecitabine ingestion **[verified this session]**: *"Life-threatening 5-FU overdoses occur because of infusion pump errors, dosage miscalculations, and accidental or suicidal ingestion of capecitabine."* (Ma et al., PMID:27622829)

Non-genetic **confounders of the phenotype test** (important for the KB's diagnostics section): chronic kidney disease produces a high false-positive rate on uracil-based screening (PMID:37011867, *Clin Chim Acta* 2023), and pre-analytical sample handling materially changes measured uracil (PMID:36412238).

For the **inborn-error arm**, there is a recurring suggestion in the literature that intercurrent stressors unmask or worsen the neurological phenotype. The head-imaging case report is explicit **[verified this session]**: *"Anoxic stress may have contributed to the clinical presentation and brain findings in this case."* (Enns et al., PMID:15303009). This is a single-case inference — curate it as PARTIAL evidence at best.

Consanguinity is a recognized contributor to the homozygous metabolic form (the Enns case was born to a consanguineous Pakistani couple), and uniparental isodisomy of chromosome 1 has produced homozygosity for an extremely rare *DPYD* variant in at least one patient (PMID:30349988) — a mechanism worth flagging because it defeats carrier-based family risk assumptions.

### Protective factors

- **Wild-type/normal-metabolizer status** (activity score 2) is the reference state — standard dosing is safe.
- **c.29C>G (C29R, DPYD\*9A)**: homozygotes in an African-American cohort showed *higher* DPD activity **[verified this session]**: *"homozygous carriers of C29R showed 27% higher DPD activity as compared with noncarriers (609 ± 152 and 480 ± 152 pmol 5-FU min(-1) mg(-1), respectively; P = 0.013)."* (PMID:23588312). This is the closest thing to a protective allele in the literature; note it is an in-cohort enzymatic observation, not a demonstrated clinical protection.
- **Exogenous uridine** is pharmacologically protective against 5-FU cytotoxicity by competitive displacement — the mechanistic basis of the uridine triacetate antidote (Section 12).

### Gene–environment interaction

This disease *is* a gene–environment interaction in its purest textbook form. The genotype is clinically silent until the environmental exposure (fluoropyrimidine) occurs; the exposure is well-tolerated until the genotype is present. The interaction is quantitative and dose-dependent, which is exactly why genotype-guided *dose reduction* — rather than binary avoidance — works for heterozygotes.

For the KB, this argues for curating the fluoropyrimidine exposure as a linked `environmental[]` entry with `influences_mechanisms` → `environmental_effect: TRIGGERS` on the "Impaired 5-FU catabolism" node, with its own evidence. ECTO grounding for "exposure to 5-fluorouracil" should be searched; if no suitable ECTO term exists, leave `exposure_term` free-text and record the search in `notes:` per the environmental-term audit convention.

---

## 3. Phenotypes

### Arm A — Inborn error of pyrimidine metabolism (biallelic, complete/near-complete deficiency)

The canonical phenotype statement **[verified this session]**:

> "A large phenotypic variability has been observed, with convulsive disorders, motor retardation and mental retardation being the most abundant manifestations. A clear correlation between the genotype and phenotype has not been established."
> — Van Kuilenburg et al. 1999, **PMID:10071185**

That last sentence is the single most important curation caveat in this entry. **Do not assert genotype–phenotype correlation for the neurological arm.** This belongs in the KB as a `discussions:` entry with `kind: KNOWLEDGE_GAP`.

| Phenotype | Suggested HP term | Type | Onset | Course | Frequency |
|---|---|---|---|---|---|
| Seizure / convulsive disorder | `HP:0001250` Seizure | Clinical sign | Neonatal–infantile | Episodic, often drug-refractory | Most abundant manifestation (PMID:10071185) — curate as FREQUENT only with a countable denominator, else omit `frequency:` |
| Intellectual disability | `HP:0001249` Intellectual disability | Clinical | Childhood (recognized) | Static-to-progressive | Among the most abundant (PMID:10071185) |
| Global developmental delay / motor retardation | `HP:0001263` Global developmental delay | Clinical | Infantile | Variable | Among the most abundant (PMID:10071185) |
| Microcephaly | `HP:0000252` Microcephaly | Physical | Congenital/infantile | Progressive or static | Reported (OMIM, MONDO description) |
| Hypertonia | `HP:0001276` Hypertonia | Clinical sign | Infantile | Variable | Reported (MONDO description explicitly says "increased muscle tone (hypertonia)") |
| Hypotonia | `HP:0001252` Hypotonia | Clinical sign | Infantile | Variable | Reported — **note the literature reports both hypo- and hypertonia**; curate as two separate phenotypes, not one "abnormal tone" |
| Autistic behavior | `HP:0000717` Autism | Behavioral | Childhood | Persistent | Reported (OMIM, MONDO) |
| Nystagmus | `HP:0000639` Nystagmus | Clinical sign | Infantile | — | Reported ocular abnormality |
| Strabismus | `HP:0000486` Strabismus | Clinical sign | Infantile | — | Reported ocular abnormality |
| Microphthalmia | `HP:0000568` Microphthalmia | Physical | Congenital | Static | Reported ocular abnormality |
| Growth delay / failure to thrive | `HP:0001510` Growth delay | Clinical | Infantile | — | Reported (PMID:15303009 case) |
| Encephalopathy | `HP:0001298` Encephalopathy | Clinical | Infantile, may be acute | Episodic | PMID:12971429 (acute neurological presentation); PMID:15303009 |
| Cerebral atrophy | `HP:0002059` Cerebral atrophy | Imaging | Infantile | Progressive | "diffuse cerebral atrophy" (PMID:15303009) |
| Abnormal cerebral white matter morphology | `HP:0002500` | Imaging | Infantile | — | "white-matter hyperintensity"; "abnormal T2 prolongation in the cerebral white matter and brainstem" (PMID:15303009) |
| **Uraciluria** | `HP:0012127` Uraciluria | Laboratory | Congenital | Persistent | Defining biochemical feature — present in essentially all homozygotes |
| Elevated urinary thymine | `HP:6000331` Elevated urinary thymine level | Laboratory | Congenital | Persistent | Defining biochemical feature |
| Abnormal urinary pyrimidine level | `HP:0033162` | Laboratory | — | — | Parent term if you want a single roll-up |

All HP IDs and labels above **[verified this session against the HPO API]**.

Additional imaging finding, verbatim **[verified this session]**:

> "Head MRI showed prominent sulci and abnormal T2 prolongation in the cerebral white matter and brainstem. Thus, DPD deficiency may feature prominent brain abnormalities involving the cerebral white matter and brainstem."
> — Enns et al., *J Inherit Metab Dis* 2004;27(4):513–522. **PMID:15303009**

Note the **brainstem** involvement — that is a distinguishing imaging feature worth curating separately from generic white-matter change.

**Critical phenotype caveat.** A large fraction of biochemically-deficient individuals are entirely asymptomatic. From the MONDO/GARD description **[verified this session]**: *"DPD deficiency can have a wide range of severity; some individuals may have various neurological problems, while others have no signs and symptoms."* The classic illustration is PMID:9323575 — a girl with partial epilepsy and a **symptom-free sister** carrying the same biochemical deficiency. This is the strongest available argument that DPD deficiency is *necessary but not sufficient* for the neurological phenotype, and should be curated as an explicit `discussions:` KNOWLEDGE_GAP with the modifier-gene hypothesis attached.

### Arm B — Fluoropyrimidine toxicity phenotypes (heterozygous or biallelic, drug-exposed)

These are **drug-reaction phenotypes**, and in dismech terms they belong downstream of an exposure-triggered node, not in the constitutive phenotype list of the metabolic disease.

| Toxicity | Suggested HP term | Notes |
|---|---|---|
| Neutropenia | `HP:0001875` Decreased total neutrophil count | 18.5% of patients in the Indian prospective cohort (PMID:41259730) |
| Thrombocytopenia | `HP:0001873` Thrombocytopenia | 15.1% (PMID:41259730) |
| Pancytopenia | `HP:0001876` Pancytopenia | Severe/complete deficiency |
| Diarrhea | `HP:0002014` Diarrhea | 12.3% (PMID:41259730); DPWG lists it as a defining toxicity |
| Oral mucositis / stomatitis | `HP:0000155` Oral ulcer (nearest HP; **HPO has no clean "mucositis" term — verified this session, search returned nothing**) | DPWG-listed toxicity |
| Hand-foot syndrome (palmar-plantar erythrodysesthesia) | **No good HP term — verified this session**; nearest terms (`HP:0025538` Palmar edema, `HP:0025537` Plantar edema) are poor fits | DPWG-listed toxicity. Notably **not** associated with c.1679T>G or HapB3 in the meta-analysis (PMID:26603945) — a real dissociation worth curating |
| Cardiotoxicity | (search UBERON/HP for cardiac-specific term) | "rapid reversal of severe acute cardiotoxicity" (PMID:27622829) |
| Neurotoxicity / leukoencephalopathy | `HP:0002352` Leukoencephalopathy | 5-FU-induced acute leukoencephalopathy is reported **even without DPD deficiency** (PMID:41610218, 2026) — do not over-attribute |
| Death (treatment-related mortality) | — | Deenen: drug-induced death reduced from 10% to 0% with genotype-guided dosing (PMID:26573078) |

The toxicity-type dissociation, verbatim **[verified this session]**:

> "Analysis of individual types of toxicity showed consistent associations of c.1679T>G and c.1236G>A/HapB3 with gastrointestinal toxicity (adjusted RR 5·72, 95% CI 1·40-23·33, p=0·015; and 2·04, 1·49-2·78, p<0·0001, respectively) and haematological toxicity (adjusted RR 9·76, 95% CI 3·03-31·48, p=0·00014; and 2·07, 1·17-3·68, p=0·013, respectively), but not with hand-foot syndrome."
> — PMID:26603945

### Quality-of-life impact

No DPD-deficiency-specific EQ-5D / SF-36 / PROMIS instrument or dataset was identified in this session. **This is a genuine gap — do not invent QoL figures.** Reasonable proxies to note in `notes:` rather than as evidence:

- Arm A: QoL burden is dominated by refractory epilepsy and intellectual disability; use the generic literature on infantile epileptic encephalopathy only as context, explicitly not as DPD-specific evidence.
- Arm B: the closest quantitative proxy is treatment interruption and hospitalization. Deenen reported toxicity-related outcomes; Meulendijks reported *"toxicity-related hospitalisation"* as an endpoint associated with high pretreatment uracil (PMID:28427087). The Indian cohort reported *"Both groups had no problems in completing treatment"* after dose reduction (PMID:41259730) — i.e. genotype-guided dosing preserved treatment continuity.

---

## 4. Genetic / Molecular Information

### Causal gene

***DPYD*** — dihydropyrimidine dehydrogenase, `HGNC:3012`, 1p21.3, NCBI Gene 1806, Ensembl `ENSG00000188641`, UniProt `Q12882`, gene OMIM `612779`. **[all verified this session via HGNC REST]**

Protein: 1,025 aa, functions as a homodimer of ~111 kDa subunits **[verified this session via PMID:11179210 — "the homodimeric pig liver enzyme (2x 111 kDa)"]**.

### Pathogenic variants

**Population frequencies from gnomAD v4 [computed directly from the gnomAD GraphQL API this session]** — global allele frequency and selected ancestry groups:

| Variant | rsID | gnomAD v4 ID (GRCh38) | Global AF | AFR | AMR | EAS | NFE | SAS | ASJ | FIN |
|---|---|---|---|---|---|---|---|---|---|---|
| **DPYD\*2A** c.1905+1G>A (splice donor) | rs3918290 | 1-97450058-C-T | 0.00456 | 0.00058 | 0.0017 | **0.0** | 0.0050 | 0.0029 | 0.0069 | **0.0243** |
| **c.2846A>T** (p.D949V) | rs67376798 | 1-97082391-T-A | 0.00328 | 0.00118 | 0.0017 | **0.0** | 0.0061 | 0.00062 | 0.00058 | 0.00009 |
| **DPYD\*13** c.1679T>G (p.I560S) | rs55886062 | 1-97515787-A-C | 0.00039 | 0.00019 | 0.00007 | **0.0** | 0.00071 | 0.0 | 0.0 | 0.00019 |
| **c.1236G>A / HapB3** (p.E412E, synonymous tag) | rs56038477 | 1-97573863-C-T | 0.01310 | 0.00294 | 0.00727 | 0.00058 | 0.0214 | 0.0162 | 0.00547 | 0.0142 |
| **c.557A>G** (p.Y186C) | rs115232898 | 1-97699474-T-C | 0.00580 | **0.0202** | 0.00197 | 0.0 | 0.00004 | 0.0 | 0.0 | 0.0 |
| c.1627A>G (DPYD\*5, p.I543V) | rs1801159 | 1-97515839-T-C | 0.186 | 0.159 | 0.237 | 0.255 | 0.196 | 0.096 | 0.194 | 0.167 |
| c.2194G>A (DPYD\*6, p.V732I) | rs1801160 | 1-97305364-C-T | 0.0401 | 0.0245 | 0.0459 | 0.0154 | 0.0452 | 0.0930 | 0.107 | 0.0221 |

Read the ancestry columns carefully — this table is the whole health-equity argument in one place. **DPYD\*2A, c.2846A>T, and c.1679T>G are all absent (AF = 0) in East Asian populations**, while **c.557A>G is ~500-fold enriched in African-ancestry populations relative to Non-Finnish European** (0.0202 vs 0.00004). A four-variant panel derived from European cohorts is nearly uninformative in East Asian patients and misses the dominant risk allele in African-ancestry patients. Note also the striking Finnish enrichment of DPYD\*2A (0.0243, ~5× NFE) — a founder-effect signal.

`*5` and `*6` are high-frequency and are **not** considered clinically actionable decreased-function alleles by CPIC/DPWG; include them only to document that common *DPYD* variation ≠ risk variation.

### Variant classes and functional consequences

| Class | Example | Consequence |
|---|---|---|
| Canonical splice-donor | c.1905+1G>A (DPYD\*2A) | Exon 14 skipping → 165-nt in-frame deletion → **no function** (activity value 0). Established as the most common lesion in complete deficiency |
| Missense, no function | c.1679T>G (p.I560S, \*13) | **No function** (activity value 0) |
| Missense, decreased function | c.2846A>T (p.D949V) | **Decreased function** (activity value 0.5) |
| Missense, decreased function, ancestry-restricted | c.557A>G (p.Y186C) | ~46% reduced DPD activity in carriers (PMID:23588312) |
| Deep intronic → cryptic splice site | c.1129-5923C>G (HapB3 causal allele) | Creates a cryptic splice donor; 44-bp intron-10 pseudo-exon inserted into mature mRNA |
| Genomic deletion | *DPYD* exons 21–23; large intragenic deletions | Loss of function; **invisible to targeted genotyping and to most exome pipelines** |
| Uniparental isodisomy | Chr 1 UPD → homozygosity for a rare variant | PMID:30349988 |

The HapB3 mechanism, verbatim **[verified this session]** — this is the key paper for why the synonymous c.1236G>A "works":

> "In one patient a genomic DPYD deletion of exons 21-23 was observed. In five patients a deep intronic mutation c.1129-5923C>G was identified creating a cryptic splice donor site. As a consequence, a 44 bp fragment corresponding to nucleotides c.1129-5967 to c.1129-5924 of intron 10 was inserted in the mature DPD mRNA. The deleterious c.1129-5923C>G mutation proved to be in cis with three intronic polymorphisms (c.483 + 18G>A, c.959-51T>G, c.680 + 139G>A) and the synonymous mutation c.1236G>A of a previously identified haplotype."
> — van Kuilenburg et al., *Hum Genet* 2010;128(5):529–538. **PMID:20803296**

And the conclusion that should drive the KB's diagnostic recommendations:

> "Our study demonstrates that a genomic deletion affecting DPYD and a deep intronic mutation affecting pre-mRNA splicing can cause severe 5FU-associated toxicity. We conclude that screening for DPD deficiency should include a search for genomic rearrangements and aberrant splicing."
> — PMID:20803296

Curation note: **c.1236G>A is a linkage tag, not the causal allele.** It is a synonymous change; its predictive power comes entirely from being in *cis* with c.1129-5923C>G. Getting this wrong is a common error in DPD entries — the KB should record `functional_impact_category` accordingly and put the causal claim on the intronic variant.

Historical mutation spectrum in complete deficiency **[verified this session]**:

> "In this group of patients, 7 different mutations have been identified, including 2 deletions [295-298delTCAT, 1897delC], 1 splice-site mutation [IVS14+1G>A)] and 4 missense mutations (85T>C, 703C>T, 2658G>A, 2983G>T). Analysis of the prevalence of the various mutations among DPD patients has shown that the G-->A point mutation in the invariant splice donor site is by far the most common (52%)..."
> — PMID:10071185

### Somatic vs germline

The disease is **germline**. Somatic *DPYD* alteration is not a recognized disease mechanism. However, *DPYD* expression is biologically relevant in tumors: tumor DPD expression influences 5-FU efficacy, and dihydropyrimidine accumulation has been implicated in EMT (Shaul et al., *Cell* 2014;158(5) — **PMID:25171410**, "Dihydropyrimidine accumulation is required for the epithelial-mesenchymal transition"). Flag this as adjacent cancer biology, **not** as DPD-deficiency pathophysiology.

### Modifier genes

Not established. The strongest indirect evidence for modifiers is the asymptomatic-sibling observation (PMID:9323575) and the explicit absence of genotype–phenotype correlation (PMID:10071185). Candidate downstream loci in the same pathway — *DPYS* (dihydropyrimidinase) and *UPB1* (β-ureidopropionase), which cause the two downstream inborn errors — are mechanistically plausible modifiers but I found no evidence establishing them as such. Meulendijks tested *TYMS* variants alongside *DPYD* and found **[verified this session]**: *"None of the DPYD variants alone, or TYMS variants alone, were associated with severe toxicity."* in that particular 550-patient analysis (PMID:28427087) — a useful negative result.

### Epigenetics

*DPYD* promoter methylation has been proposed as a contributor to reduced tumor/normal-tissue DPD expression. I did **not** verify primary sources for this in this session — treat as an unverified lead requiring its own literature pass before any evidence item is written.

### Chromosomal abnormalities

Whole-chromosome events are not a typical cause, with one important exception: **uniparental isodisomy of chromosome 1** producing homozygosity for a rare *DPYD* variant (PMID:30349988). Large intragenic deletions detectable by MLPA/CMA are established (PMID:20803296; PMID:38528593, a 2024 novel large intragenic deletion case report).

---

## 5. Environmental Information

- **Environmental factors**: The dominant "environmental" factor is pharmaceutical exposure — 5-FU, capecitabine, tegafur, and cutaneous 5-FU. No occupational, radiation, or pollutant exposure has been established as a cause or modifier.
- **Lifestyle factors**: None established. Do not populate this section speculatively.
- **Infectious agents**: Not applicable.

**Suggested CHEBI grounding [all verified this session via OLS4 except where noted]:**
- `CHEBI:46345` 5-fluorouracil
- `CHEBI:31348` capecitabine
- `CHEBI:17568` uracil
- `CHEBI:17821` thymine
- `CHEBI:15901` 5,6-dihydrouracil
- `CHEBI:27468` 5,6-dihydrothymine
- `CHEBI:16958` beta-alanine
- `CHEBI:27389` 3-aminoisobutyric acid (β-aminoisobutyrate)
- `CHEBI:16704` uridine
- `CHEBI:90914` uridine triacetate
- tegafur — CHEBI lookup timed out this session; **verify before use**

---

## 6. Mechanism / Pathophysiology

### The enzyme

DPD catalyzes the committed, rate-limiting step of pyrimidine catabolism. It is a spectacularly complex redox enzyme. Verbatim **[verified this session]**:

> "Dihydropyrimidine dehydrogenase catalyzes the first step in pyrimidine degradation: the NADPH-dependent reduction of uracil and thymine to the corresponding 5,6-dihydropyrimidines. Its controlled inhibition has become an adjunct target for cancer therapy, since the enzyme is also responsible for the rapid breakdown of the chemotherapeutic drug 5-fluorouracil. The crystal structure of the homodimeric pig liver enzyme (2x 111 kDa) determined at 1.9 A resolution reveals a highly modular subunit organization, consisting of five domains with different folds. Dihydropyrimidine dehydrogenase contains two FAD, two FMN and eight [4Fe-4S] clusters, arranged in two electron transfer chains that pass the dimer interface twice."
> — Dobritzsch et al., *EMBO J* 2001;20(4):650–660. **PMID:11179210**

The structure also directly explains the drug interaction:

> "The ternary complex of an inactive mutant of the enzyme with bound NADPH and 5-fluorouracil reveals the architecture of the substrate-binding sites and residues responsible for recognition and binding of the drug."
> — PMID:11179210

Mechanistically it is a two-site ping-pong enzyme: NADPH reduces FAD at one active site, electrons traverse a ~56 Å [4Fe-4S] wire, and reduced FMN at the second site reduces the pyrimidine ring. This means loss-of-function variants can act by at least four distinct routes — substrate-site disruption, cofactor-binding disruption, electron-wire disruption, or dimer-interface/folding disruption — which is a nice mechanistic reason why so many different missense positions produce deficiency.

### The pathway

**Pyrimidine catabolism (three steps):**
1. **DPD** (*DPYD*): uracil → 5,6-dihydrouracil; thymine → 5,6-dihydrothymine. NADPH-dependent. **Rate-limiting.**
2. **Dihydropyrimidinase** (*DPYS*): ring opening → N-carbamyl-β-alanine / N-carbamyl-β-aminoisobutyrate
3. **β-ureidopropionase** (*UPB1*): → **β-alanine** and **β-aminoisobutyrate** + CO₂ + NH₃

Deficiency at step 1 blocks the entire pathway, causing simultaneous **substrate accumulation** (uracil, thymine, and 5-hydroxymethyluracil) and **product depletion** (β-alanine).

### Causal chain A — Inborn error → neurological disease

```
DPYD biallelic LOF variant  [MOLECULAR]
  → absent/near-absent DPD enzyme activity  [MOLECULAR]
    → block of pyrimidine nucleobase catabolism  [MOLECULAR]
      ├→ accumulation of uracil, thymine, 5-hydroxymethyluracil
      │    in urine, plasma, and CSF  [ORGANISM]
      │      → putative neurotoxicity / disturbed pyrimidine homeostasis
      │        in the developing CNS  [TISSUE]
      └→ depletion of β-alanine (an inhibitory neurotransmitter)
           and β-aminoisobutyrate  [MOLECULAR]
             → altered inhibitory neurotransmission  [CELLULAR]
               → neuronal hyperexcitability / seizures  [ORGANISM]
               → white matter and brainstem injury  [TISSUE]
                 → developmental delay, intellectual disability,
                   microcephaly, autistic behavior  [ORGANISM]
```

The mechanistic hypothesis behind this chain, stated in the authors' own hedged language **[verified this session]**:

> "An altered beta-alanine, uracil and thymine homeostasis might underlie the various clinical abnormalities encountered in patients with DPD deficiency."
> — PMID:10071185

**Curate that hedge.** "Might underlie" is not "does underlie." This chain should be entered as a `mechanistic_hypotheses` entry with `status: EMERGING` or `ALTERNATIVE`, not as a settled canonical cascade. The pathogenesis of the neurological phenotype in DPD deficiency is genuinely unresolved — which is exactly why the same biochemistry produces an epileptic infant and an asymptomatic sibling.

A supporting piece of evidence from an unexpected direction, which strengthens the β-alanine limb **[verified this session]**:

> "Dpyd encodes the rate-limiting enzyme in the metabolic pathway that catabolizes uracil and thymidine to β-alanine, an inhibitory neurotransmitter. Thus, data support β-alanine as a neurotransmitter that promotes sleep in mice."
> — Keenan et al., *Curr Biol* 2021;31(23):5238–5248. **PMID:34653361** (`evidence_source: MODEL_ORGANISM`)

This is the best available functional support for β-alanine depletion having a real CNS consequence — but it is a mouse sleep phenotype, not a human seizure phenotype. Flag as `HUMAN_MODEL_MISMATCH`, not as human evidence.

The white-matter pathogenesis is explicitly unknown **[verified this session]**:

> "The pathogenesis of the white-matter abnormalities is unknown, although environmental factors and altered energy metabolism may be involved."
> — PMID:15303009

### Causal chain B — Pharmacogenetic → fluoropyrimidine toxicity

```
DPYD deleterious variant (mono- or biallelic)  [MOLECULAR]
  → reduced DPD catalytic activity  [MOLECULAR]
    → [ENVIRONMENTAL TRIGGER: fluoropyrimidine administration]
      → impaired catabolic clearance of 5-FU (>80% of dose
        normally cleared by DPD)  [ORGANISM]
        → increased systemic 5-FU exposure / prolonged half-life  [ORGANISM]
          ├→ FdUMP-mediated thymidylate synthase inhibition
          │    → thymineless stress, DNA damage  [CELLULAR]
          └→ FUTP misincorporation into RNA  [MOLECULAR]
               → RNA dysfunction  [CELLULAR]
                 → cytotoxicity in rapidly proliferating tissues  [TISSUE]
                   ├→ bone marrow  → myelosuppression → neutropenia,
                   │                  thrombocytopenia, pancytopenia
                   ├→ GI mucosa    → mucositis, severe diarrhea
                   ├→ skin/adnexa  → hand-foot syndrome
                   ├→ myocardium   → acute cardiotoxicity
                   └→ CNS          → acute neurotoxicity / leukoencephalopathy
                     → treatment-related morbidity and death  [ORGANISM]
```

The FUTP-into-RNA limb is confirmed by the antidote's mechanism of action, which is the cleanest available functional evidence for it **[verified this session]**:

> "Uridine triacetate delivers high concentrations of uridine, which competes with toxic 5-FU metabolites."
> — Ma et al., PMID:27622829

### Suggested module conformance

- **`myelosuppression`** — Chain B's marrow limb is a textbook conformer: cytotoxic insult to proliferating HSPCs → marrow suppression → multilineage cytopenias → infection/bleeding/dose-limiting toxicity. The disorder-specific substitution is "excess systemic 5-FU due to impaired DPD catabolism" as the cytotoxic driver. **Key conformance target: `myelosuppression#Multilineage Peripheral Cytopenias`.** Strongly recommended.
- **`epilepsy_excitation_inhibition_imbalance`** — Chain A's seizure limb is a plausible conformer via the β-alanine/inhibitory-neurotransmission route (`epilepsy_excitation_inhibition_imbalance#Excitation-Inhibition Imbalance`). But conform **only** if you are willing to assert the β-alanine mechanism, which the literature hedges. Given `status: EMERGING`, I would hold this back or attach it to the hypothesis group rather than declaring bare `conforms_to`.
- **`metabolic_intoxication_decompensation`** — tempting but I'd advise **against**. DPD deficiency does not classically produce catabolic-stress-triggered acute metabolic crises with acidosis/hyperammonemia/hypoglycemia. The acute-presentation case (PMID:12971429) is a single report. Forcing this conformance would over-claim.
- **Candidate new module** — there is no dismech module for "pharmacogenomic clearance failure" (impaired drug catabolism → supratherapeutic exposure → dose-dependent toxicity). This pattern recurs across *DPYD*/fluoropyrimidines, *TPMT*-*NUDT15*/thiopurines, *UGT1A1*/irinotecan, and *CYP2D6*/codeine. If dismech ever wants one, DPD deficiency is the ideal flagship conformer. Worth raising as a proposal rather than shoehorning this entry into an existing module.

### GO term suggestions **[all verified this session via OLS4]**

| Term | Label | Suggested modifier |
|---|---|---|
| `GO:0017113` | dihydropyrimidine dehydrogenase (NADP+) activity | `LOSS_OF_FUNCTION` (molecular_functions) |
| `GO:0006212` | uracil catabolic process | `DECREASED` |
| `GO:0006210` | thymine catabolic process | `DECREASED` |
| `GO:0006208` | pyrimidine nucleobase catabolic process | `DECREASED` |
| `GO:0019483` | beta-alanine biosynthetic process | `DECREASED` |
| `GO:0050660` | flavin adenine dinucleotide binding | (cofactor annotation) |
| `GO:0010181` | FMN binding | (cofactor annotation) |
| `GO:0051539` | 4 iron, 4 sulfur cluster binding | (cofactor annotation) |
| `GO:0070402` | NADPH binding | (cofactor annotation) |

Note on the modifier choice: for the enzyme activity node, `LOSS_OF_FUNCTION` is justified for the biallelic complete-deficiency case (the process is genuinely outside normal regulatory constraint — it is abolished). For the heterozygous pharmacogenetic case, `DECREASED` is the honest quantitative call. If you model these as separate nodes (recommended), the modifiers differ, and that difference is itself informative.

### Cell types and tissues

| Level | Term | Role |
|---|---|---|
| Primary site of DPD activity | `CL:0000182` hepatocyte | Liver is the dominant site of 5-FU catabolism |
| Surrogate assay tissue | `CL:2000001` peripheral blood mononuclear cell | PBMC DPD activity is the classical enzymatic phenotyping substrate |
| Toxicity target | Hematopoietic progenitors (bone marrow) | Chain B, marrow limb |
| Toxicity target | Intestinal/oral mucosal epithelium | Chain B, GI limb |
| Chain A target | Neurons; CNS white matter (oligodendrocytes/myelin) | Chain A |

All CL IDs **[verified this session]**.

### Molecular profiling

- **Metabolomics** is the diagnostically decisive modality here: urinary/plasma uracil, thymine, dihydrouracil, and the UH2/U ratio. Repositories: HMDB, Metabolomics Workbench, MetaboLights. See Section 10.
- **Transcriptomics/proteomics/lipidomics/single-cell/spatial**: I found **no DPD-deficiency-specific datasets** in this session. Do not fabricate dataset accessions. If the KB wants `datasets:` records, run `just discover-datasets` and apply the standard relevance triage — and be aware that searching the gene symbol *DPYD* will surface colorectal-cancer 5-FU-response studies, which are about the drug, not the disease. That is textbook Named Entity Confusion reached through dataset search.
- **Functional genomics**: DepMap contains *DPYD* dependency/expression data in the context of 5-FU sensitivity. Relevant to the cancer-pharmacology arm only.

---

## 7. Anatomical Structures Affected

### Organ level

| Organ/system | Involvement | UBERON |
|---|---|---|
| **Liver** | Primary metabolic site of DPD activity — the enzymatic lesion's principal location, though the liver itself is not injured | `UBERON:0002107` liver |
| **Central nervous system** | Primary clinical target in Arm A | `UBERON:0001017` central nervous system |
| Cerebral white matter | T2 hyperintensity, hypoplasia/atrophy (PMID:15303009) | `UBERON:0002316` white matter |
| Brainstem | T2 prolongation (PMID:15303009) — distinguishing feature | search UBERON for brainstem |
| **Bone marrow** | Secondary — toxicity target in Arm B | `UBERON:0002371` bone marrow |
| GI mucosa | Secondary — toxicity target in Arm B | `UBERON:0000344` mucosa (parent; find a GI-specific child) |
| Skin (palms/soles) | Secondary — hand-foot syndrome in Arm B | — |
| Heart | Secondary — acute cardiotoxicity in Arm B | — |
| Eye | Arm A: microphthalmia, nystagmus, strabismus | — |

All UBERON IDs listed **[verified this session]** except brainstem and GI-specific mucosa, which need a lookup.

### Subcellular

DPD is a **cytosolic** enzyme. Suggested GO cellular component: `GO:0005829` cytosol **[not verified this session — check before use]**. This is worth curating explicitly because it distinguishes DPD deficiency from the mitochondrial metabolic disorders it can superficially resemble on a metabolic-workup differential.

### Lateralization

Neurological/imaging findings are **bilateral and symmetric** (diffuse cerebral atrophy, diffuse white matter change). Ocular findings may be unilateral or bilateral. No asymmetric pattern is described.

---

## 8. Temporal Development

### Onset

**Arm A (metabolic):**
- Onset is typically **neonatal to infantile**. Presentation at birth is documented (PMID:16151913, "Dihydropyrimidine dehydrogenase deficiency presenting at birth"). The review framing: *"Patients may present with a wide range of neurological symptoms during the first years of life."* (PMID:15303009) **[verified this session]**
- Pattern: usually insidious (developmental delay recognized over months) but can be **acute** — PMID:12971429, "Dihydropyrimidine dehydrogenase deficiency and acute neurological presentation."
- Suggested `OnsetDescriptor`: `onset_category: NEONATAL` and/or `INFANTILE`, with a second `Inheritance`-independent note that a substantial fraction never present at all.

**Arm B (pharmacogenetic):**
- Onset is **exposure-defined**: any age, whenever a fluoropyrimidine is first given. Median onset of toxicity is within the **first cycle** — Meulendijks' primary endpoint was explicitly *"grade ⩾3 toxicity... occurring during the first cycle of treatment"* (PMID:28427087), and the Indian prospective study assessed toxicity *"after the first cycle of chemotherapy"* (PMID:41259730). **[verified this session]**
- Pattern: **acute**, often hyperacute in complete deficiency.

### Progression

**Arm A:** Variable. Some patients have a static encephalopathy; developmental regression is reported in some. Duration is **chronic and lifelong** — the enzymatic defect never resolves. There is no established staging system.

**Arm B:** Rapidly evolving over days. Verbatim **[verified this session]**:

> "Increased susceptibility to 5-fluorouracil (5-FU)/capecitabine can lead to rapidly occurring toxicity caused by impaired clearance, dihydropyrimidine dehydrogenase deficiency, and other genetic variations in the enzymes that metabolize 5-FU."
> — PMID:27622829

### Critical periods — this is the most actionable temporal fact in the entry

There is a hard, quantified intervention window for the toxicity arm. Uridine triacetate must be given early:

> "Patients received uridine triacetate as soon as possible (most within the first 96 hours after 5-FU/capecitabine)."
> — PMID:27622829 **[verified this session]**

Supporting model data (from the same research program, reported via the manufacturer/preclinical literature): treatment started within 24 h was most effective; starting beyond 96–120 h was far less effective **[found via web search summary, primary source not verified this session — verify before writing as evidence]**.

The other critical period is **pre-treatment**: the entire clinical value of DPYD testing rests on doing it *before* the first dose. Both the FDA boxed warning language and the EMA recommendation are framed as pre-treatment requirements.

Recovery kinetics after antidote **[verified this session]**:

> "Among the 141 uridine triacetate-treated overdose patients with a diagnosis of cancer... 53 resumed chemotherapy in < 30 days (median time after 5-FU, 19.6 days), and this indicated a rapid recovery from toxicity."
> — PMID:27622829

---

## 9. Inheritance and Population

### Inheritance

- **Autosomal recessive** for the metabolic disease (`HP:0000007` autosomal recessive inheritance **[not verified this session — confirm HP ID]**).
- **Codominant / gene-dosage** for fluoropyrimidine toxicity risk. This is the practical framing behind the **activity score** system, and it is why heterozygotes are clinically actionable. Verbatim **[verified this session]**:

> "The DPYD-gene activity score, determined by four DPYD variants, predicts DPD activity and can be used to optimize an individual's starting dose. The gene activity score ranges from 0 (no DPD activity) to 2 (normal DPD activity)."
> — Lunenburg et al., DPWG guideline, *Eur J Hum Genet* 2020;28(4):508–517. **PMID:31745289**

CPIC assigns activity values of 0, 0.5, or 1 per allele (no function / decreased function / normal function); the sum gives the activity score, mapping to normal metabolizer (2), intermediate metabolizer (1–1.5), or poor metabolizer (0–0.5) **[per CPIC 2017 guideline, PMID:29152729 — the abstract itself is a scope statement only, so the activity-score detail must be quoted from the guideline body or from the DPWG abstract above, which does state it verbatim]**.

**Curation warning on PMID:29152729:** the CPIC 2017 update's PubMed abstract is a *purpose statement*, not a findings abstract. Verbatim, in full **[verified this session]**:

> "The purpose of this guideline is to provide information for the interpretation of clinical dihydropyrimidine dehydrogenase (DPYD) genotype tests so that the results can be used to guide dosing of fluoropyrimidines (5-fluorouracil and capecitabine). Detailed guidelines for the use of fluoropyrimidines, their clinical pharmacology, as well as analyses of cost-effectiveness are beyond the scope of this document."

Any snippet you attribute to PMID:29152729 must come from that text or from the full article, not from the widely-paraphrased dosing table.

### Penetrance and expressivity

- **Arm A**: markedly **incomplete penetrance** and **highly variable expressivity**. The symptom-free-sibling case (PMID:9323575) is the reference example. No genotype–phenotype correlation established (PMID:10071185).
- **Arm B**: penetrance is **exposure-conditional and high**. In the Indian prospective cohort **[verified this session]**: *"Severe toxicities (grade ≥3)... in mutation carriers (72.7%) as compared with mutation noncarriers (37.0%, P = .03)"* (PMID:41259730). In the historical untreated-dose-reduction comparator: *"The risk of grade ≥ 3 toxicity was thereby significantly reduced from 73% (95% CI, 58% to 85%) in historical controls (n = 48) to 28% (95% CI, 10% to 53%) by genotype-guided dosing (P < .001)"* (PMID:26573078).

### Genetic anticipation

Not applicable — no repeat expansion mechanism.

### Germline mosaicism

Not reported in the literature I surveyed. **Uniparental isodisomy** is documented (PMID:30349988) and is the more relevant non-Mendelian mechanism for this gene.

### Epidemiology

**Partial deficiency (the pharmacogenetically relevant state):**

The best-anchored figure comes from the 19,376-patient French population **[verified this session]**:

> "Mean U was 9.9 ± 10.1 ng/mL (median 8.7, range 1.6-856). According to French recommendations, 7.3 % of patients were partially deficient (U 16-150 ng/mL) and 0.02 % completely deficient (U≥150 ng/mL). DPYD variant frequencies were \*2A: 0.83 %, \*13: 0.17 %, D949V: 1.16 %, \*7: 0.05 % (2 homozygous patients with U at 22 and 856 ng/mL)."
> — Launay et al., *Clin Chem Lab Med* 2024;62(12):2415–2424. **PMID:38896022**

The commonly-quoted **3–8%** partial-deficiency prevalence in European-ancestry populations is consistent with this **[widely cited; the 7.3% figure above is the strongest single primary anchor]**.

Genotype-based carrier frequency, from prospective screening **[verified this session]**:
- Deenen: *"A total of 2,038 patients were prospectively screened for DPYD\*2A, of whom 22 (1.1%) were heterozygous polymorphic."* (PMID:26573078)
- Henricks (four-variant panel): *"Of 1103 evaluable patients, 85 (8%) were heterozygous DPYD variant allele carriers, and 1018 (92%) were DPYD wild-type patients."* (PMID:30348537)
- Indian cohort (four-variant panel): *"Of the 146 study participants, 11 (7.5%) had a DPYD mutation. HapB3 (rs56038477) was the most commonly encountered variant (72.7% of patients)..."* (PMID:41259730)

**Complete deficiency:** ~0.02% by uracil phenotype in the French population (PMID:38896022). Estimates of 0.01–0.3% appear in the literature. The number of reported patients with the full neurological phenotype is in the low hundreds worldwide **[standard reference, not re-verified]**.

Suggested `Prevalence` records for the KB:

```yaml
prevalence:
- population: France (consecutive pre-treatment oncology patients, 2015-2022)
  measure_type: POINT_PREVALENCE
  prevalence_class: ABOVE_1_IN_1000
  rate_per_100000: 7300.0
  notes: >-
    Partial DPD deficiency by uracil-based phenotyping (plasma U 16-150 ng/mL),
    n=19,376. This is a phenotype-defined partial-deficiency rate, not the
    prevalence of the Mendelian neurological disorder.
- population: France (consecutive pre-treatment oncology patients, 2015-2022)
  measure_type: POINT_PREVALENCE
  prevalence_class: BAND_1_5_PER_10000
  rate_per_100000: 20.0
  notes: >-
    Complete DPD deficiency by uracil-based phenotyping (plasma U >=150 ng/mL),
    n=19,376.
```

Both with `evidence: reference: PMID:38896022` and the verbatim snippet above.

### Population demographics

- **Geographic/ancestry distribution**: see the gnomAD table in Section 4. Headline points: DPYD\*2A shows a strong **Finnish founder enrichment** (AF 0.0243 vs 0.005 NFE); the three European-derived actionable variants are **absent in East Asians**; c.557A>G is enriched ~500-fold in African-ancestry populations.
- **Sex ratio**: 1:1 expected for an autosomal recessive disorder. No sex bias in the toxicity arm has been established that I could verify. There are literature reports of higher fluoropyrimidine toxicity in women generally, but this is not DPD-specific and should not be attributed here.
- **Age distribution**: Arm A is pediatric-onset. Arm B follows the age distribution of cancer patients receiving fluoropyrimidines — i.e. skews strongly older adult.

---

## 10. Diagnostics

### The central diagnostic tension — curate this carefully

DPD deficiency is diagnosed by **two non-equivalent approaches** — genotyping and phenotyping — and the field's most important recent finding is that **they disagree badly**. This is the single most consequential thing to get right in the KB's diagnostics section.

The EMA endorsed both **[verified this session]**:

> "In 2020, the European Medicines Agency (EMA) recommended two methods for pre-treatment DPD deficiency testing in clinical practice: phenotyping using endogenous uracil concentration or genotyping for DPYD risk variant alleles."
> — de With et al., *ESMO Open* 2023;8(2):101197. **PMID:36989883**

The 2024 head-to-head analysis in 19,376 patients found poor concordance **[verified this session]**:

> "Sixty-six% of variant carriers exhibited uracilemia <16 ng/mL, challenging correct identification of DPD deficiency based on U. The sensitivity (% patients with a deficient phenotype among variant carriers) of U threshold at 16 ng/mL was 34 %. The best discriminant marker for identifying variant carriers was UH2/U2. UH2/U2<0.942 (29.7 % of patients) showed enhanced sensitivity (81 %) in identifying deleterious genotypes compared to 16 ng/mL U."
> — PMID:38896022

> "These results reaffirm the poor concordance between DPD phenotyping and genotyping, suggesting that both approaches may be complementary and that targeted DPYD genotyping is not sufficiently reliable to identify all patients with complete deficiency."
> — PMID:38896022

Set against the earlier prospective evidence that uracil *does* predict toxicity **[verified this session]**:

> "High pretreatment uracil concentration was strongly predictive of severe, including fatal, fluoropyrimidine-associated toxicity, and is a highly promising phenotypic marker to identify patients at risk of severe fluoropyrimidine-associated toxicity."
> — Meulendijks et al., *Br J Cancer* 2017;116(11):1415–1424. **PMID:28427087**

> "High pretreatment uracil concentrations (>16 ng ml-1) were strongly associated with global severe toxicity (OR 5.3, P=0.009), severe gastrointestinal toxicity (OR 33.7, P<0.0001), toxicity-related hospitalisation..."
> — PMID:28427087

**These are not contradictory results, and the KB should say so explicitly.** Uracil predicts *toxicity* well (Meulendijks) but predicts *genotype* poorly (Launay). They are answering different questions. This deserves a `discussions:` entry with `kind: KNOWLEDGE_GAP` and a `mechanistic_hypotheses` framing, not a single flattened "uracil is the test" claim.

### Laboratory tests

| Test | Analyte | Notes |
|---|---|---|
| **Urine pyrimidine analysis** | Uracil, thymine, 5-hydroxymethyluracil | Diagnostic for Arm A. This is the test that finds the inborn error. PMID:15303009 recommends it explicitly for unexplained white-matter/brainstem MRI findings |
| **Plasma uracil (U)** | Uracil | Pre-treatment phenotyping. French/EMA thresholds: U ≥16 ng/mL = partial deficiency; U ≥150 ng/mL = complete deficiency (PMID:38896022) |
| **UH2/U or UH2/U² ratio** | Dihydrouracil/uracil | UH2/U² < 0.942 outperforms the U threshold for identifying variant carriers (sensitivity 81% vs 34%) (PMID:38896022) |
| **PBMC DPD enzyme activity** | pmol 5-FU·min⁻¹·mg⁻¹ | Reference/research assay; normal ~514 ± 168 in European-Americans (PMID:23588312) |
| **5-FU degradation rate (5-FUDR) assay** | ex vivo | Alternative functional phenotyping |
| **Therapeutic drug monitoring of 5-FU** | 5-FU AUC | Complements phenotyping; can catch under-exposure after dose reduction |

**Pre-analytical warning worth curating:** plasma uracil is exquisitely sensitive to sample handling (PMID:36412238, "Plasma Uracil as a DPD Phenotyping Test: Pre-Analytical Handling Matters!"), and chronic kidney disease produces a high false-positive rate (PMID:37011867). Both are real, actionable caveats.

LOINC codes for uracil/dihydrouracil should be looked up before curating `reference_ranges` — I did not verify them this session. If you do add `reference_ranges`, the French thresholds map naturally onto `interpretation_bands`:

```yaml
interpretation_bands:
- name: Normal DPD activity
  upper_bound: 16.0
  unit: ng/mL
  abnormal_flag: NORMAL
- name: Partial DPD deficiency
  lower_bound: 16.0
  upper_bound: 150.0
  unit: ng/mL
  abnormal_flag: HIGH
  severity: MODERATE
- name: Complete DPD deficiency
  lower_bound: 150.0
  unit: ng/mL
  abnormal_flag: CRITICAL_HIGH
  severity: SEVERE
```

with `evidence: PMID:38896022` and the verbatim threshold sentence.

### Imaging

Brain MRI in Arm A: prominent sulci, diffuse cerebral atrophy, T2 hyperintensity in cerebral white matter **and brainstem** (PMID:15303009; also PMID:25565930, abnormal MRI in two Malaysian siblings). Imaging is supportive, not diagnostic.

### Genetic testing

- **Targeted genotyping (the guideline standard)**: the four CPIC/DPWG variants — DPYD\*2A (rs3918290), c.1679T>G (rs55886062), c.2846A>T (rs67376798), c.1236G>A/HapB3 (rs56038477). This is what every current guideline panel means by "DPYD genotyping."
- **Extended panels**: c.557A>G (rs115232898) is included by Mayo Clinic and several US commercial laboratories and by the NHS North West GLH since September 2025 **[web-search-sourced; verify the NHS detail before using as evidence]**. CPIC recommends 50% starting-dose reduction for heterozygous carriers.
- **Full-gene sequencing**: catches rare and private variants. PMID:42510779 (2026) specifically addresses outcomes of patients carrying unusual *DPYD* variants found by protocol implementation.
- **CNV/MLPA/CMA**: **required** to catch the large intragenic deletions documented in PMID:20803296 and PMID:38528593. Targeted genotyping misses these entirely.
- **Deep intronic coverage**: c.1129-5923C>G must be either directly assayed or captured via its c.1236G>A tag. Exome sequencing will miss it.
- **WGS**: theoretically catches all of the above; not standard of care for this indication.
- **Karyotype/FISH/mtDNA/repeat expansion**: not applicable.

The authors' own conclusion on testing scope **[verified this session]**:

> "We conclude that screening for DPD deficiency should include a search for genomic rearrangements and aberrant splicing."
> — PMID:20803296

Also worth curating (2024): *"DPYD genotype should be extended to rare variants: report on two cases of phenotype / genotype discrepancy"* — *Cancer Chemother Pharmacol* 2024, doi:10.1007/s00280-024-04738-5. **[title verified via web search; PMID not confirmed this session]**

### Clinical criteria and differential diagnosis

There is no consensus clinical diagnostic criteria set (DSM/ICD-style) for DPD deficiency — diagnosis is biochemical and/or molecular.

**Differential diagnosis:**

| Condition | Distinguishing feature |
|---|---|
| **Dihydropyrimidinase deficiency** (*DPYS*) | Elevated urinary **dihydrouracil and dihydrothymine** (the DPD products) rather than uracil/thymine — the pattern is diagnostic |
| **β-ureidopropionase deficiency** (*UPB1*) | Elevated **N-carbamyl-β-alanine / N-carbamyl-β-aminoisobutyrate** |
| Other early infantile epileptic encephalopathies | Normal urine pyrimidines |
| Mitochondrial encephalopathies | Lactate/pyruvate abnormalities; DPD is cytosolic |
| Non-DPD causes of fluoropyrimidine toxicity | 5-FU leukoencephalopathy has been reported **without** DPD deficiency (PMID:41610218, 2026); also *TYMS* variants, drug interactions, renal impairment |
| Iatrogenic 5-FU overdose | Normal genotype/phenotype; history of pump/dosing error |

The *DPYS* and *UPB1* disorders are the key differentials because they are the two downstream steps of the same pathway — a single urine pyrimidine profile distinguishes all three. For the KB, this is also a natural **Grouping** candidate: "Disorders of Pyrimidine Degradation," with `grouping_basis: [SHARED_PATHWAY]` and three DISEASE members.

### Screening

- **Newborn screening**: DPD deficiency is **not** on standard newborn screening panels. Urine pyrimidine analysis is a targeted metabolic workup, not a population screen.
- **Pre-treatment pharmacogenetic screening**: now effectively universal in guideline terms — see Section 13.
- **Cascade screening**: relatives of an identified carrier should be offered *DPYD* testing before any fluoropyrimidine exposure. This is high-yield and cheap, and is under-practiced.

---

## 11. Outcome / Prognosis

### Arm A

No survival statistics specific to DPD deficiency were identified in this session. **Do not manufacture a life-expectancy figure.** Prognosis is dominated by the severity of the epilepsy and encephalopathy; a substantial fraction of biochemically-deficient people are asymptomatic and have normal life expectancy. Aspiration pneumonia (`HP:0011951`) and complications of severe neurodisability are the plausible causes of premature death in severely affected patients, but I found no cohort quantifying this.

The most important prognostic statement is the negative one: **genotype does not predict outcome** in Arm A (PMID:10071185).

### Arm B — quantified, and this is where the good numbers live

**Mortality without intervention:**

> "In the historical cohort, 21 of 25 patients (84%) died."
> — PMID:27622829 (untreated 5-FU overdose, supportive care only) **[verified this session]**

**Mortality with antidote:**

> "A total of 137 of 142 overdose patients (96%) treated with uridine triacetate survived and had a rapid reversal of severe acute cardiotoxicity and neurotoxicity; in addition, mucositis and leukopenia were prevented, or the patients recovered from them."
> — PMID:27622829 **[verified this session]**

**Mortality with genotype-guided prevention:**

> "The risk of grade ≥ 3 toxicity was thereby significantly reduced from 73% (95% CI, 58% to 85%) in historical controls (n = 48) to 28% (95% CI, 10% to 53%) by genotype-guided dosing (P < .001); drug-induced death was reduced from 10% to 0%."
> — PMID:26573078 **[verified this session]**

**Residual risk even with guideline dosing** — the honest caveat:

> "Overall, fluoropyrimidine-related severe toxicity was higher in DPYD variant carriers (33 [39%] of 85 patients) than in wild-type patients (231 [23%] of 1018 patients; p=0·0013)."
> — PMID:30348537 **[verified this session]**

That is a genotype-guided-dosed carrier population **still** experiencing more severe toxicity than wild-type. Dose reduction narrows the gap; it does not close it. The 2025 commentary title says it plainly: *"Reducing Fluorouracil Doses in Patients With Partial Dihydropyrimidine Dehydrogenase Deficiency Is a Treatment Safety Strategy, Not a Panacea of Precision Dosing"* (Hertz & Venook, *JCO Precis Oncol* 2025;9:e2500440, **PMID:40638877**). Curate this as a `discussions:` entry — the "genotyping solves it" framing is an overstatement the field is actively pushing back on.

### Efficacy preservation — the other key prognostic question

The standing worry about dose reduction is undertreatment. The evidence says efficacy is preserved:

> "Adequate treatment of genotype-guided dosing was further demonstrated by a similar incidence of grade ≥ 3 toxicity compared with wild-type patients receiving the standard dose (23%; P = .64)"
> — PMID:26573078 **[verified this session]**

> "Individuals with DPYD mutations experience increased toxicity and dose adjustments; however, treatment efficacy was not affected."
> — PMID:41259730 **[verified this session]**

> "Evidence demonstrates that dose individualization based on guidance from the Clinical Pharmacogenetics Implementation Consortium reduces toxicity risk while maintaining treatment effectiveness and potentially reducing overall costs."
> — Kratz et al., *ASCO Educ Book* 2026;46(3):e521184. **PMID:42048619** **[verified this session]**

### Prognostic factors and biomarkers

- **Activity score** (0–2) is the primary prognostic stratifier for the toxicity arm.
- **Pretreatment plasma uracil >16 ng/mL** predicts severe and fatal toxicity (OR 5.3 global, OR 33.7 GI) (PMID:28427087).
- **Number of deleterious alleles** — biallelic/poor metabolizers have qualitatively higher risk than heterozygotes.
- **Time to antidote administration** is the dominant prognostic factor once toxicity is underway.

---

## 12. Treatment

### Arm A — Inborn error

There is **no disease-modifying therapy**. Management is symptomatic and supportive:

| Treatment | `treatment_term` | `therapeutic_modality` | Notes |
|---|---|---|---|
| Anticonvulsant therapy | `NCIT:C64172` Anticonvulsant Therapy | `SMALL_MOLECULE` | Seizure control; no DPD-specific agent established |
| Supportive care | `NCIT:C15747` Supportive Care | `OTHER` | Developmental support, feeding |
| Nutritional support | `NCIT:C15433` Nutritional Support | depends on the intervention — **do not blind-tag as `BEHAVIORAL`** per the CLAUDE.md caveat | For failure to thrive |
| Genetic counseling | `NCIT:C15240` Genetic Counseling | `OTHER` | Recurrence risk; cascade testing |
| **Lifelong fluoropyrimidine avoidance** | see note below | — | The single most important intervention for every affected individual, symptomatic or not |

All NCIT IDs **[verified this session via OLS4]**. Note that `NCIT:C64172`'s reachability from `NCIT:C25218` (Clinical Intervention or Procedure) should be checked with `just validate-terms` before commit.

β-alanine supplementation is a theoretically attractive intervention given the pathway logic. I found **no clinical evidence** for it in this session. Do not curate it as a treatment.

### Arm B — Prevention of fluoropyrimidine toxicity

**Genotype-guided dosing (DPWG, verbatim) [verified this session]:**

> "For patients initiating 5-fluorouracil or capecitabine: subjects with a gene activity score of 0 are recommended to avoid systemic and cutaneous 5-fluorouracil or capecitabine; subjects with a gene activity score of 1 or 1.5 are recommended to initiate therapy with 50% the standard dose of 5-fluorouracil or capecitabine. For subjects initiating tegafur: subjects with a gene activity score of 0, 1 or 1.5 are recommended to avoid tegafur. Subjects with a gene activity score of 2 (reference) should receive a standard dose."
> — PMID:31745289

**Refinement from the prospective study [verified this session]:**

> "For DPYD\*2A and c.1679T>G carriers, a 50% initial dose reduction was adequate. For c.1236G>A and c.2846A>T carriers, a larger dose reduction of 50% (instead of 25%) requires investigation."
> — PMID:30348537

Note the asymmetry: the 2018 study used 25% reductions for c.1236G>A and c.2846A>T and found them insufficient; current CPIC guidance uses a uniform 50% reduction for intermediate metabolizers. If you curate the dosing algorithm, cite the *current* guideline for the recommendation and PMID:30348537 for the empirical basis.

**Rescue therapy — uridine triacetate:**

```yaml
treatments:
- name: Uridine Triacetate
  description: >-
    Emergency antidote for 5-fluorouracil or capecitabine overdose or early-onset
    severe toxicity, including toxicity due to DPD deficiency. Delivers high
    concentrations of uridine, which competes with cytotoxic 5-FU metabolites for
    incorporation into RNA. FDA-approved 2015. Must be given early - most treated
    patients received it within 96 hours of fluoropyrimidine exposure.
  therapeutic_modality: SMALL_MOLECULE
  treatment_term:
    preferred_term: Pharmacotherapy
    term:
      id: NCIT:C15986
      label: Pharmacotherapy
    therapeutic_agent:
    - preferred_term: uridine triacetate
      term:
        id: CHEBI:90914
        label: uridine triacetate
  evidence:
  - reference: PMID:27622829
    supports: SUPPORT
    evidence_source: HUMAN_CLINICAL
    snippet: "In these studies, uridine triacetate was a safe and effective lifesaving antidote for capecitabine and 5-FU overexposure, and it facilitated the rapid resumption of chemotherapy."
    explanation: Two open-label clinical studies establishing uridine triacetate as an effective antidote for fluoropyrimidine overexposure.
```

`NCIT:C2379` (Uridine Triacetate) is available as an alternative `therapeutic_agent` grounding **[verified this session]** — but note the memory-recorded caveat that NCIT drug terms frequently fail `therapeutic_agent` enum validation in this repo; **prefer the CHEBI term**.

Adverse events of the antidote itself **[verified this session]**: *"Adverse reactions in patients receiving uridine triacetate included vomiting (8.1%), nausea (4.6%), and diarrhea (3.5%)."* (PMID:27622829)

**Supportive management of established toxicity**: G-CSF for neutropenia, antibiotics for febrile neutropenia, fluid/electrolyte support for diarrhea, mucositis care. None is DPD-specific.

### Pharmacogenomics

This disease *is* a pharmacogenomics entry. Resources: **PharmGKB** (DPYD–fluoropyrimidine pathway and clinical annotations), **CPIC** (Level A gene–drug pair), **DPWG** (clinical implication score "essential"), **FDA Table of Pharmacogenomic Biomarkers in Drug Labeling**.

DPWG's own framing of the strength of recommendation **[verified this session]**:

> "Based on the DPWG clinical implication score, DPYD genotyping is considered 'essential', therefore directing DPYD testing prior to initiating fluoropyrimidines."
> — PMID:31745289

### Advanced therapeutics

- **Gene therapy / gene editing / RNA therapies**: none in development for DPD deficiency that I identified. This is not a currently-addressed target.
- **Cell therapy**: not applicable.
- **DPD inhibitors as a therapeutic strategy** (the *inverse* concept — deliberately inhibiting DPD to boost 5-FU exposure, e.g. eniluracil, or the DPD-inhibitory fluoropyrimidine S-1) is real and interesting context, and PMID:11179210 alludes to it (*"Its controlled inhibition has become an adjunct target for cancer therapy"*). It is **not** a treatment for DPD deficiency — file under `notes:` or a `discussions:` entry, never under `treatments:`.

### Experimental / trials

`NCT02324452` — the Alpe2U prospective DPYD genotype-guided dosing study underlying PMID:30348537 **[verified this session: "This trial is registered with ClinicalTrials.gov, number NCT02324452, and is complete."]**. Suitable for a `clinical_trials:` record:

```yaml
clinical_trials:
- name: NCT02324452
  phase: NOT_APPLICABLE   # verify against the registry record before commit
  status: COMPLETED
  description: >-
    Prospective multicentre safety analysis of DPYD genotype-guided dose
    individualisation of fluoropyrimidine therapy in 17 Dutch hospitals.
```

Fetch the registry record with `just fetch-reference NCT02324452` before writing any snippet, and confirm the phase enum against the actual record — I did not verify it.

---

## 13. Prevention

### Primary prevention

For Arm A there is no primary prevention beyond reproductive options. For Arm B, primary prevention is the entire story: **test before you dose.**

The current regulatory position **[verified this session]**:

> "Recent regulatory and guideline changes have established pretreatment DPYD genotyping as a critical strategy to prevent severe fluoropyrimidine toxicity. Following earlier European leadership by the European Medicines Agency, the US Food and Drug Administration added boxed warnings to capecitabine and 5-fluorouracil labels recommending genetic testing before therapy. Concurrent updates from the National Comprehensive Cancer Network and ASCO align US with European practice supporting universal testing."
> — Kratz et al., *ASCO Educ Book* 2026;46(3):e521184. **PMID:42048619**

This is the strongest, most recent, and most citable statement of the current standard. **[The specific dates — capecitabine boxed warning October 2025, 5-FU label February 2026 — came from a secondary web source and are NOT verified. Do not write those dates into the KB without checking the FDA labels directly.]**

Implementation status in Europe **[verified this session]**:

> "Following publication of the EMA recommendations, 87% and 75% of the countries reported an increase in the amount of genotype and phenotype testing, respectively."
> — PMID:36989883

> "The EMA recommendations have supported the implementation of DPD deficiency testing in Europe. Key factors for successful implementation were test reimbursement and clear clinical guidelines."
> — PMID:36989883

### Secondary prevention

- Early recognition of first-cycle toxicity → immediate fluoropyrimidine discontinuation → uridine triacetate within the 96-hour window.
- Therapeutic drug monitoring of 5-FU to catch both over- and under-exposure after dose adjustment (PMC7700344, "Association of 5-FU Therapeutic Drug Monitoring to DPD Phenotype Assessment May Reduce 5-FU Under-Exposure" **[title only; verify]**).

### Tertiary prevention

- Dose titration upward from a reduced starting dose based on observed tolerance — the Deenen protocol used *"an initial dose reduction of ≥ 50% followed by dose titration based on tolerance"* with a median achieved dose-intensity of 48% (range 17%–91%) (PMID:26573078) **[verified this session]**.
- Permanent avoidance flagging in the EHR/allergy list for identified poor metabolizers.

### Genetic screening and counseling

- **Cascade testing** of first-degree relatives of identified carriers, before any oncology exposure.
- **Carrier/prenatal/PGD**: technically available for families with a severely affected child. No professional guideline mandates it; the wide phenotypic variability and high asymptomatic rate make counseling genuinely difficult and this should be stated as such.
- `NCIT:C15240` Genetic Counseling; `NCIT:C15709` Genetic Testing; `NCIT:C68762` Pharmacogenomic Test **[all verified this session; check `NCIT:C68762` reachability from `NCIT:C25218` — it is a "test" concept and may not validate as a clinical intervention]**.

### Public health and equity

The equity dimension is a first-class part of prevention for this disease and should be curated, not left as an aside. From the 2026 ASCO Educational Book **[verified this session]**:

> "Despite growing adoption, implementation challenges persist, including workflow integration, clinician education, and equitable access... Barriers are more pronounced in resource-constrained settings, where limited infrastructure, reimbursement uncertainty, and insufficient pharmacogenomic education hinder implementation. Regional initiatives illustrate education-focused, context-adapted strategies to expand testing and address population-specific variant knowledge gaps."
> — PMID:42048619

And on patient advocacy as a driver:

> "Patient advocacy, particularly efforts led by Advocates for Universal DPD/DPYD Testing, has accelerated policy change, increased clinician awareness, and highlighted ethical implications of preventable harm."
> — PMID:42048619

Supporting systematic review: *"DPYD genetic polymorphisms in non-European patients with severe fluoropyrimidine-related toxicity: a systematic review"* — **PMID:38886557** (2024) **[title/PMID from search; abstract not verified this session]**.

The gnomAD table in Section 4 is the quantitative backbone of this argument and should be cited alongside the narrative.

### No vaccination, immunization, sanitation, vector-control, or environmental-remediation dimension

Not applicable. Leave these empty rather than padding them.

---

## 14. Other Species / Natural Disease

- **Taxonomy**: `NCBITaxon:9606` *Homo sapiens*. Model species: `NCBITaxon:10090` *Mus musculus*, `NCBITaxon:9823` *Sus scrofa* (the pig liver enzyme is the structural reference).
- **Breed (VBO)**: Not applicable — no breed-associated natural disease known.
- **Orthologs**: mouse *Dpyd* (chromosome 3); pig *DPYD*; rat *Dpyd*. Bacterial and fungal orthologs exist and have been characterized structurally (e.g. *E. coli* DPD, PMID:34097066).
- **Natural disease in other species**: **None identified. [verified this session]** An OMIA advanced search on gene symbol *DPYD* returned "No phene records found." This is a genuine, searched-and-absent result and should be recorded as such in `notes:` rather than left blank — the absence is informative.
- **Veterinary relevance**: No established natural veterinary disease. 5-FU is notoriously and severely toxic to cats and dogs (fatal neurotoxicity from accidental exposure to topical 5-FU creams), but that is a species-level sensitivity, not DPD deficiency, and should not be conflated with it in the KB.
- **Comparative biology / evolutionary conservation**: DPD is deeply conserved — the pyrimidine catabolic pathway and the enzyme's remarkable cofactor architecture (2× FAD, 2× FMN, 8× [4Fe-4S]) are shared from bacteria to mammals (PMID:11179210; PMID:34097066). The pig enzyme's structure is the reference model for the human enzyme, which is itself a strong statement about conservation.
- **Zoonotic potential / cross-species transmission**: Not applicable.

---

## 15. Model Organisms

### Mouse

**The best-characterized model is a *Dpyd* knockout — and its published phenotype is not what you would expect.** Verbatim **[verified this session]**:

> "Validation studies were performed using activity monitoring and EEG/EMG recording in Collaborative Cross mouse strains with and without the PWK/PhJ haplotype at this location, as well as EEG and EMG recording of sleep and wake in Dpyd knockout mice and wild-type littermate controls. Mice lacking Dpyd had 78.4 min less sleep during the lights-off period than wild-type mice (p = 0.007; Cohen's d = -0.94). There was no difference in other measured behaviors in knockout mice, including assays evaluating cognitive-, social-, and affective-disorder-related behaviors."
> — Keenan et al., *Curr Biol* 2021;31(23):5238–5248. **PMID:34653361**

That last sentence is the load-bearing one for the KB. ***Dpyd* knockout mice do not recapitulate the human neurological phenotype** — no cognitive, social, or affective abnormality was detected. They have a sleep phenotype instead. This is a textbook `FAILS_TO_RECAPITULATE` / `HUMAN_MODEL_MISMATCH` situation and should be curated as such:

```yaml
animal_models:
- name: Dpyd knockout mouse
  species: Mouse
  genotype: Dpyd knockout (homozygous null)
  publication: PMID:34653361
  modeled_mechanisms:
  - target: Beta-Alanine Depletion and Altered Inhibitory Neurotransmission
    relationship: PARTIALLY_RECAPITULATES
    fidelity: LOW
    description: >-
      Loss of Dpyd blocks the pathway generating beta-alanine and produces a
      measurable CNS phenotype (reduced sleep during the active period),
      supporting a real neurological consequence of the enzymatic block.
    limitations: >-
      The observed phenotype is reduced sleep, not seizures or developmental
      impairment. No difference was detected in cognitive-, social-, or
      affective-disorder-related behavioral assays, so the model does not
      reproduce the epilepsy, intellectual disability, or autistic behavior
      that define the severe human presentation.
    readouts:
    - name: Total sleep during lights-off period (EEG/EMG)
      target: Beta-Alanine Depletion and Altered Inhibitory Neurotransmission
      direction: DECREASED
      interpretation: >-
        78.4 minutes less sleep than wild-type littermates (Cohen's d = -0.94),
        the only behavioral domain in which knockouts differed.
      evidence:
      - reference: PMID:34653361
        supports: SUPPORT
        evidence_source: MODEL_ORGANISM
        snippet: "Mice lacking Dpyd had 78.4 min less sleep during the lights-off period than wild-type mice (p = 0.007; Cohen's d = -0.94)."
        explanation: Direct EEG/EMG measurement in Dpyd knockout versus wild-type littermate controls.
  - target: Seizure Generation
    relationship: FAILS_TO_RECAPITULATE
    fidelity: LOW
    limitations: >-
      No seizure or epilepsy phenotype was reported, and the study explicitly
      found no differences in other measured behavioral domains.
    evidence:
    - reference: PMID:34653361
      supports: SUPPORT
      evidence_source: MODEL_ORGANISM
      snippet: "There was no difference in other measured behaviors in knockout mice, including assays evaluating cognitive-, social-, and affective-disorder-related behaviors."
      explanation: Negative behavioral result establishing that the knockout does not reproduce the human neurobehavioral phenotype.
```

Note that `FAILS_TO_RECAPITULATE` links require both `limitations` and `evidence` per `test_failure_to_recapitulate_links_are_substantiated` — both are supplied above.

The associated `HUMAN_MODEL_MISMATCH` discussion writes itself: *evidence exists in a model (β-alanine depletion produces a real CNS phenotype in mice) but its translational validity to the human epileptic encephalopathy is the open question.*

**Diversity Outbred / Collaborative Cross mice** are also relevant as a natural-variation model **[verified this session]**: a linkage peak for total sleep on chromosome 3 (LOD 7.14), with reduced *Dpyd* expression associated with the PWK/PhJ allele — an eQTL-driven partial-loss model rather than a null.

Resources: **MGI** (mouse *Dpyd*), **IMPC** — note that IMPC lists `OMIM:274270` in its disease-model index **[seen in search results this session; the specific IMPC phenotype data were not reviewed]**, **IMSR**, **Jackson Laboratory** (DO/CC strains).

### Other models

- **Pig liver enzyme** — the structural workhorse. The 1.9 Å crystal structure with bound NADPH and 5-FU (PMID:11179210) is the basis for essentially all structure–function interpretation of human *DPYD* missense variants. `evidence_source: IN_VITRO`.
- **Mammalian cell expression systems** — recombinant expression of *DPYD* variants with enzyme-activity measurement relative to wild type is the standard functional-validation route for VUS. See PMID:23328581 ("Phenotypic profiling of DPYD variations relevant to 5-fluorouracil sensitivity using real-time cellular analysis and in vitro measurement of enzyme activity"). `evidence_source: IN_VITRO`.
- **Patient PBMCs** — ex vivo DPD activity measurement in primary human cells; arguably the highest-fidelity "model" available since it uses the patient's own genotype (PMID:23588312). `evidence_source: HUMAN_CLINICAL` or `IN_VITRO` depending on framing — the Offer study measured circulating mononuclear-cell enzyme activity in healthy volunteers, so `IN_VITRO` is defensible for the assay claim while the population-frequency claim is `HUMAN_CLINICAL`. **Split the evidence items** so each carries a single `evidence_source`.
- **Zebrafish / Drosophila / C. elegans**: no established DPD-deficiency models identified.
- **UPase knockout mouse** (PMID:21954436) is *not* a DPD model — it targets uridine phosphorylase — but it is mechanistically adjacent, demonstrating that uridine availability protects normal tissue from 5-FU toxicity. Useful supporting context for the uridine-triacetate mechanism; do not miscatalog it as a *Dpyd* model.

### Applications and limitations

**What the models are good for:** enzyme structure–function; variant functional classification; uridine-rescue pharmacology; β-alanine neurobiology.

**What they cannot currently do:** reproduce the human neurological phenotype. There is, as far as I can tell, **no animal model of DPD-deficiency epileptic encephalopathy.** That is the single largest gap in this disease's experimental toolkit, and it is worth curating as a `discussions:` entry with `kind: KNOWLEDGE_GAP` and a `proposed_experiments` block.

---

## Curation Summary and Warnings

**Things to get right:**

1. **Two arms, two chains.** Do not blend the inborn-error pathophysiology with the pharmacogenetic toxicity pathophysiology into one cascade. Section 6 gives them separately for a reason.
2. **No genotype–phenotype correlation in Arm A** — PMID:10071185 says so explicitly. Curate this as a KNOWLEDGE_GAP, not as an omission.
3. **The β-alanine mechanism is a hypothesis** ("might underlie"), not settled fact. `mechanistic_hypotheses` with `status: EMERGING`.
4. **c.1236G>A is a tag, not the cause** — the causal allele is the deep intronic c.1129-5923C>G.
5. **Phenotyping and genotyping disagree**, and the disagreement is a real finding (PMID:38896022), not a measurement failure. Uracil predicts toxicity well, genotype poorly.
6. **The mouse knockout fails to model the human disease.** `FAILS_TO_RECAPITULATE` + `HUMAN_MODEL_MISMATCH`.
7. **Dose reduction reduces but does not eliminate excess risk** (39% vs 23% severe toxicity even with genotype-guided dosing, PMID:30348537). Don't over-claim.
8. **CPIC PMID:29152729's abstract is a scope statement.** Any dosing-table snippet attributed to it must come from the article body, not from paraphrase.

**Named Entity Confusion risk for this disease: LOW-MODERATE.** *DPYD* is unambiguous and the MONDO causal gene is clear, so `just preflight-dr` should PASS cleanly on any DR report. The real confusion risk here is not entity-level but **arm-level** — a DR tool may silently produce a report entirely about 5-FU pharmacogenomics with nothing on the inborn error, or vice versa. Check that any DR report covers both before curating from it. The related-disease confusion risk (*DPYS* dihydropyrimidinase deficiency vs *DPYD* dihydropyrimidine dehydrogenase deficiency — one letter apart, adjacent steps of the same pathway) is real and worth an explicit check.

**Verified PMIDs used in this report:** 10071185, 11179210, 15303009, 20803296, 23588312, 25171410, 26573078, 26603945, 27622829, 28427087, 29152729, 30348537, 31745289, 34653361, 36621118, 36989883, 38896022, 40638877, 41259730, 42048619. Additional PMIDs cited by title/summary only and requiring `just fetch-reference` verification before use: 9323575, 12971429, 16151913, 21954436, 23328581, 25565930, 30349988, 34097066, 36412238, 37011867, 38528593, 38886557, 41610218, 42510779.

**Sources consulted online:**
- [CPIC — DPYD guidelines](https://cpicpgx.org/gene/dpyd/)
- [DPWG guideline for DPYD and fluoropyrimidines (PMC7080718)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7080718/)
- [OMIM #274270 — Dihydropyrimidine Dehydrogenase Deficiency](https://omim.org/entry/274270)
- [GARD — Dihydropyrimidine dehydrogenase deficiency](https://rarediseases.info.nih.gov/diseases/19/dihydropyrimidine-dehydrogenase-deficiency)
- [Launay et al. 2024, GPCO-RNPGx uracil vs genotype analysis](https://pubmed.ncbi.nlm.nih.gov/38896022/)
- [Kratz et al. 2026, ASCO Educational Book — implementing DPYD testing](https://ascopubs.org/doi/10.1200/EDBK-26-521184)
- [Ho et al. 2025, guide for implementing DPYD genotyping (Clin Pharmacol Ther)](https://ascpt.onlinelibrary.wiley.com/doi/10.1002/cpt.3567)
- [Offer et al. 2013 — DPYD Y186C in African ancestry (PMC3821392)](https://pmc.ncbi.nlm.nih.gov/articles/PMC3821392/)
- [Dobritzsch et al. 2001 — DPD crystal structure (EMBO J)](https://www.embopress.org/doi/full/10.1093/emboj/20.4.650)
- [Ma et al. 2016 — uridine triacetate emergency use](https://pubmed.ncbi.nlm.nih.gov/27622829/)
- [gnomAD](https://gnomad.broadinstitute.org/) (v4 allele frequencies, queried directly)
- [OLS4 / EMBL-EBI](https://www.ebi.ac.uk/ols4/) (MONDO, GO, CHEBI, CL, UBERON, NCIT term verification)
- [HPO API, Jackson Laboratory](https://ontology.jax.org/) (HP term verification)
- [HGNC REST](https://rest.genenames.org/) (DPYD gene record)
- [OMIA — DPYD search](https://www.omia.org/) (no animal phene records)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 40 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 2 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 3 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `PMID:31745289` (4 mentions) - Identifier did not resolve to a record
- `PMID:9323575` (3 mentions) - Identifier did not resolve to a record