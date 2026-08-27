---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-18T15:13:36.787550'
end_time: '2026-08-18T15:20:23.918759'
duration_seconds: 407.13
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Neurodevelopmental Disorder With or Without Autism or Seizures
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
  web_search_requests: 18
  num_turns: 36
  total_cost_usd: 2.6049056999999998
  session_id: 8a6f8a92-07a1-5a78-8642-588997865743
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 27
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 16
  on_topic: 15
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder With or Without Autism or Seizures
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder With or Without Autism or Seizures** covering all of the
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

I'll research this now using web search and fetch tools.

# Neurodevelopmental Disorder With or Without Autism or Seizures (NEDAUS) — Comprehensive Research Report

## 1. Disease Information

**Overview:** Neurodevelopmental disorder with or without autism or seizures (NEDAUS), also referred to as CUL3-related neurodevelopmental disorder, is an autosomal dominant condition caused by heterozygous, predominantly de novo, loss-of-function (and some missense/hypomorphic) variants in **CUL3** (Cullin-3). It is characterized by global developmental delay apparent in infancy, impaired intellectual development, and speech delay, with variable additional features including seizures (sometimes with developmental regression), autism spectrum disorder (ASD) or other behavioral abnormalities, dysmorphic facial features, hand/foot anomalies, cardiac defects, and failure to thrive/growth restriction ([OMIM #619239](https://omim.org/entry/619239); Nakashima et al. 2020, PMID:32341456).

**Key identifiers:**
- **OMIM phenotype:** #619239 — NEURODEVELOPMENTAL DISORDER WITH OR WITHOUT AUTISM OR SEIZURES; NEDAUS
- **OMIM gene:** *603136 — CULLIN 3; CUL3
- **MONDO:** MONDO:0030994 ([Monarch Initiative](https://monarchinitiative.org/MONDO:0030994))
- **HGNC:** 2553 (CUL3)
- **NCBI Gene ID:** 8452
- **Chromosome location:** 2q36.2
- **GTR/MedGen concept:** C5543225 ([NCBI GTR](https://www.ncbi.nlm.nih.gov/gtr/conditions/C5543225/); [MedGen](https://www.ncbi.nlm.nih.gov/medgen/1784023))
- **ClinGen/GenCC:** curated as a definitive/moderate–definitive gene-disease relationship by multiple Intellectual Disability/Autism and Syndromic Disorders GCEPs ([ClinGen](https://search.clinicalgenome.org/kb/genes/HGNC:2553); [GenCC](https://thegencc.org/genes/HGNC:2553/disease))

**Synonyms/related terms:** CUL3-related neurodevelopmental disorder; Cullin-3 haploinsufficiency syndrome; NEDAUS. Note: CUL3 is a **dual-disease gene** — distinct, mechanistically unrelated pathogenic variants (specifically those disrupting exon 9 splicing) cause **pseudohypoaldosteronism type IIE (PHA2E; OMIM #614496)**, a renal salt-wasting/hypertension disorder acting through the WNK-kinase pathway, not through the neurodevelopmental mechanism described here ([PMC4604684](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4604684/); OMIM #614496). This distinction is important for curation — NEDAUS and PHA2E are separate MONDO/OMIM entities despite sharing a gene.

**Source of information:** Data are derived from aggregated case series and cohort studies (clinical genetics case reports, exome-sequencing cohorts, and multi-center collaborations), not from a single large EHR/registry-based dataset. The largest published cohorts to date are ~26 individuals (Sadler et al. 2024/2025, PMID:39501558) and 37 families (Blackburn et al. 2025, *Ann Neurol*, DOI:10.1002/ana.27077), supplemented by numerous smaller case reports. Exact population prevalence is unknown; the disease is considered rare ([MedlinePlus Genetics](https://medlineplus.gov/genetics/condition/cul3-related-neurodevelopmental-disorder/)).

---

## 2. Etiology

**Disease causal factor:** NEDAUS is a monogenic Mendelian disorder caused by heterozygous pathogenic variants in **CUL3**, encoding Cullin-3, the scaffold protein of Cullin-RING E3 ubiquitin ligase (CRL3) complexes. The overwhelming majority of reported cases arise from **de novo** variants; germline mosaicism and rare familial transmission (autosomal dominant, presumably with variable expressivity) have been reported but are uncommon.

**Genetic risk factors:**
- Heterozygous loss-of-function (nonsense, frameshift, canonical splice-site) variants are the most common mechanism, consistent with a **haploinsufficiency** model.
- Missense variants also occur and, in a subset, have been shown to impair CRL3 complex assembly or substrate ubiquitination.
- A large-deletion (CNV) encompassing *CUL3* has also been reported (Sadler et al., PMID:39501558).
- **CUL3 is independently established as one of the highest-confidence autism spectrum disorder risk genes** by two landmark exome sequencing consortia:
  - De Rubeis et al. 2014 (Autism Sequencing Consortium, PMID:25363760) — CUL3 met genome-wide significance (FDR ≈0.01) among de novo/rare damaging variant enrichment in ASD.
  - Satterstrom et al. 2020 (*Cell*, PMID:31981491) — large-scale exome sequencing of 35,584 samples (11,986 with ASD) identified 102 ASD-associated genes at FDR ≤0.1; CUL3 was among the top-ranked, high-confidence genes.
  - SFARI Gene database assigns CUL3 a **Category 1 ("high confidence")** ASD gene score ([gene.sfari.org/database/human-gene/CUL3](https://gene.sfari.org/database/human-gene/CUL3)).
- Analysis of published mutations found approximately 20 CUL3 variants (13 protein-truncating, 7 missense) across ASD/developmental-delay/schizophrenia cohorts, with essentially no comparable variants found in unaffected controls.

**Environmental risk factors:** None specifically established; as a monogenic de novo disorder, standard advanced-paternal-age associations with de novo mutation rate may apply generally but are not specifically quantified for CUL3.

**Protective factors:** None established in the literature.

**Gene-environment interactions:** Not reported; the disorder's penetrance and expressivity appear driven primarily by variant type/location and possibly genetic background/modifiers rather than documented environmental modifiers.

---

## 3. Phenotypes

Phenotype frequencies below are drawn primarily from the largest published cohort (Sadler et al. 2024/2025, n=26, PMID:39501558; [full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC11617854/)) and the Blackburn et al. 2025 cohort (n=37 families, *Ann Neurol*), supplemented by MedlinePlus Genetics and OMIM.

| Phenotype | Frequency (approx.) | Suggested HPO term |
|---|---|---|
| Global developmental delay | Near-universal | HP:0001263 |
| Speech/motor developmental delay | 88% | HP:0000750 / HP:0001270 |
| Intellectual disability | 77% | HP:0001249 |
| Learning disorder | 89% | HP:0002194 |
| Behavioral abnormalities | 76% | HP:0000708 |
| Autism spectrum disorder / autistic features | ~33–36% | HP:0000717 |
| Seizures (variable types incl. infantile spasms) | Subset (reported in original 3-case series, ~67% had infantile spasms; overall cohort seizure rate lower, estimated in the range of a fifth to a third of cases) | HP:0001250; infantile spasms HP:0011097 |
| ADHD | 33% (signature-positive subgroup) | HP:0007018 |
| Hand/foot abnormalities (curved 5th finger, high foot arches, toe webbing) | 51–60% | HP:0001167 (camptodactyly of finger); HP:0001762 (talipes); HP:0001777 (syndactyly of toes) |
| Dysmorphic facial features (long triangular face, large forehead, pointed chin, deep-set eyes) | 50–52% | HP:0000275 (narrow face); HP:0000341 (prominent forehead); HP:0000307 (pointed chin); HP:0000490 (deeply set eye) |
| Cardiac/septal defects | 35% | HP:0001671 |
| Brain MRI abnormalities | 56% | HP:0012443 |
| Fetal/intrauterine growth restriction | 35–59% | HP:0001511 |
| Feeding problems / poor feeding | 36% | HP:0011968 |
| Failure to thrive | Present in subset | HP:0001508 |
| Hypotonia (childhood) progressing to dystonia/tremor/spasms (adulthood) | Reported in a subset | HP:0001252 (hypotonia); HP:0001332 (dystonia); HP:0001337 (tremor) |
| Microcephaly | Subset | HP:0000252 |
| Poor visual contact | Subset | HP:0000618-adjacent |
| GERD | Reported | HP:0002020 |
| Genitourinary anomalies | Reported in subset | HP:0000119 |

**Phenotype characteristics:**
- **Onset:** Congenital/infantile — developmental delay is apparent from infancy in essentially all cases.
- **Progression:** Variable — most features are static/developmental rather than progressive, but adult-onset movement disorder (dystonia, tremor, spasms) has been described, and seizure onset can be accompanied by developmental regression in some patients.
- **Severity:** Highly variable, ranging from mild learning difficulties to profound intellectual disability with epilepsy; some carriers have neither seizures nor autism despite pathogenic variants (variable expressivity/incomplete penetrance for specific features).
- **Quality of life impact:** Not systematically quantified with standardized instruments (EQ-5D/SF-36) in the literature to date; impact is inferred to be substantial given the combination of intellectual disability, behavioral, and motor involvement, with early multidisciplinary therapy recommended.

---

## 4. Genetic/Molecular Information

**Causal gene:** CUL3 (Cullin 3), OMIM *603136, chromosome 2q36.2, HGNC:2553, NCBI Gene ID 8452, UniProt Q13618.

**Variant classes reported (cohort of 26, PMID:39501558):**
- Nonsense: 8 cases
- Frameshift: 9 cases
- Missense: 5 cases
- Splice-site: 3 cases
- Copy number variant (large deletion encompassing CUL3): 1 case

**Functional consequence:** Predominantly **loss of function via haploinsufficiency** — truncating and splice-disrupting variants are the majority class, consistent with a dosage-sensitive gene. Missense variants have been shown in functional studies (e.g., Gao et al. 2023, PMID:37558490) to impair Cullin-3 scaffolding activity within CRL3 complexes.

**Allele frequency:** CUL3 loss-of-function variants are under strong purifying selection in population databases (gnomAD), consistent with high intolerance to loss-of-function variation (pLI ≈1), supporting pathogenicity of de novo truncating variants; no NEDAUS-causing variants are expected/observed at appreciable frequency in gnomAD.

**Origin:** Overwhelmingly germline de novo; distinguish from CUL3 **somatic** involvement, which is not a recognized feature of NEDAUS (unlike some cancer contexts where CUL3 substrate adaptors are somatically altered).

**Modifier genes/epigenetics:** A robust **DNA methylation episignature** comprising 213 differentially methylated probes has been identified in a subset of CUL3 pathogenic-variant carriers ("signature-positive" cases), with high sensitivity/specificity for distinguishing affected individuals from controls, and predominant hypomethylation changes (Sadler et al. 2024/2025, PMID:39501558). This episignature may aid reclassification of variants of uncertain significance and suggests a downstream epigenetic mechanism (potentially via disrupted CRL3-mediated turnover of chromatin-modifying enzymes).

**Chromosomal abnormalities:** A large deletion encompassing the CUL3 locus has been reported causing the phenotype (contiguous gene/whole-gene deletion mechanism), reinforcing haploinsufficiency as the operative mechanism.

**Gene-disease validity:** CUL3 is recognized by ClinGen-affiliated expert panels (Intellectual Disability and Autism GCEP) with substantial published evidence (at least seven unrelated cases in the literature meeting curation criteria per Genomics England PanelApp) and is a **definitive** gene-disease relationship in Gen2Phen/PanelApp curation for intellectual disability ([PanelApp](https://panelapp.genomicsengland.co.uk/panels/285/gene/CUL3/)).

---

## 5. Environmental Information

No specific environmental, lifestyle, or infectious causal factors have been established for NEDAUS; it is understood as a purely monogenic disorder driven by de novo germline CUL3 variation. No CTD (Comparative Toxicogenomics Database) gene-environment interaction records specific to CUL3-associated neurodevelopmental disease were identified in this search.

---

## 6. Mechanism / Pathophysiology

**Molecular function of CUL3:** CUL3 encodes Cullin-3, the elongated scaffold protein that "orchestrates the assembly" of **Cullin-RING E3 ubiquitin ligase 3 (CRL3/BCR complexes)** — Cullin-3 binds RBX1 at one end (recruiting an E2 ubiquitin-conjugating enzyme) and a BTB-domain-containing substrate adaptor protein at the other, bridging E2 enzyme and substrate to catalyze **substrate ubiquitination**, typically targeting proteins for 26S proteasomal degradation (reviewed in PMC10416632, PMID:37575562).

**Causal chain (molecular → cellular → organismal):**
1. **Trigger:** Heterozygous de novo loss-of-function (or damaging missense) CUL3 variant → **CUL3 haploinsufficiency**.
2. **Molecular consequence:** Reduced/impaired CRL3 ubiquitin ligase complex assembly and activity → **disrupted ubiquitin-proteasome-mediated protein turnover** of CRL3 substrates, including small GTPase **RhoA** (via BACURD1/2 [KCTD adaptors]), with downstream evidence also implicating altered turnover of chromatin-modifying enzymes (proposed mechanism for the observed methylation episignature).
3. **Cellular consequence:** In Cul3-haploinsufficient mouse models, **elevated/dysregulated RhoA signaling** disrupts actin cytoskeletal dynamics, impairing **cortical neurogenesis**, dendritic growth, filamentous actin puncta formation, and spontaneous neuronal network activity (Amar/Dong et al. 2021, *Mol Psychiatry*, PMID:33727673). Pharmacological RhoA inhibition rescued dendrite length and network activity phenotypes in this model, directly demonstrating RhoA as a key downstream effector.
4. **Circuit/systems consequence:** Conditional Cul3 ablation restricted to cholinergic neurons of the basal forebrain recapitulates ASD-like social and sensory-gating deficits and cognitive impairment, implicating **prefrontal cortex cholinergic projections** in the behavioral phenotype (PMID:36693858). Postnatal, forebrain-restricted excitatory-neuron Cul3 deletion (CaMKIIα-Cre model) produces repetitive jumping, reduced marble burying, hyperlocomotion, impaired motor coordination, and hindlimb clasping (Sekar et al. 2025, *Genes Brain Behav*, PMC12536218).
5. **Organismal consequence:** Global developmental delay, intellectual disability, autistic features/behavioral abnormalities, and in a subset, seizures (with occasional regression) and dysmorphic/structural features.

**Cell types/processes implicated:**
- Cortical neural progenitor cells / radial glia (neurogenesis defect)
- Excitatory forebrain (pyramidal) neurons (dendritic/synaptic defects)
- Cholinergic basal forebrain neurons (behavioral/cognitive circuit)
- Suggested GO terms: GO:0016567 (protein ubiquitination), GO:0031461 (cullin-RING ubiquitin ligase complex), GO:0007399 (nervous system development), GO:0021987 (cerebral cortex development), GO:0035556 (intracellular signal transduction, RhoA-related)
- Suggested CL terms: CL:0000030 (neuroblast, generic — for cortical neural progenitor), CL:0000598 (pyramidal neuron), CL:0002453 (oligodendrocyte precursor cell — not specifically implicated, included only if relevant), CL:0011005 (GABAergic neuron — not primary), cholinergic neuron (CL:0000108)

**Distinct mechanism for PHA2E (differential note):** Exon-9-disrupting CUL3 variants (a structurally distinct mutational class from the truncating/missense variants causing NEDAUS) impair CRL3-mediated ubiquitination of **WNK kinases** (via the KLHL3 adaptor) in the distal nephron, causing familial hyperkalemic hypertension (PHA2E) — a completely separate clinical entity that curators should not conflate with NEDAUS despite the shared gene (PMC4604684).

**Molecular profiling:** DNA methylation array (episignature) data support pathway-level evidence of altered epigenetic regulation in CUL3 haploinsufficiency (Sadler et al., PMID:39501558). No large-scale transcriptomic/proteomic human patient datasets were identified; mouse model studies provide transcriptomic/proteomic profiling of embryonic through adult brain (Amar et al. 2021, PMID:33727673).

---

## 7. Anatomical Structures Affected

- **Organ level (primary):** Central nervous system (brain — cerebral cortex specifically implicated in animal models).
- **Secondary/associated organ involvement:** Cardiovascular system (septal defects), gastrointestinal system (feeding difficulties, GERD), musculoskeletal system (hand/foot anomalies), genitourinary system (anomalies in a subset), growth (failure to thrive, IUGR).
- **Tissue/cell level:** Cerebral cortex — neural progenitor cells, pyramidal (excitatory) neurons; basal forebrain cholinergic neurons; prefrontal cortex circuitry.
- **Subcellular level:** Cytoskeleton (actin dynamics via RhoA), ubiquitin-proteasome system components (CRL3 complex assembly), and by extension chromatin/epigenetic machinery (implicated by the methylation episignature).
- **Suggested UBERON terms:** UBERON:0000955 (brain), UBERON:0000956 (cerebral cortex), UBERON:0001890 (forebrain), UBERON:0002037 (cerebellum — not specifically implicated but sometimes assessed on MRI), UBERON:0000948 (heart, for septal defects).
- **Suggested GO Cellular Component terms:** GO:0031461 (cullin-RING ubiquitin ligase complex), GO:0015629 (actin cytoskeleton), GO:0005634 (nucleus, for epigenetic effects).
- **Laterality:** Not applicable — a diffuse neurodevelopmental process rather than a lateralized structural lesion, though individual brain MRI anomalies (reported in 56% of signature-positive cases) may show focal or global findings.

---

## 8. Temporal Development

- **Onset:** Congenital/infantile onset; global developmental delay is apparent from infancy in essentially all reported patients. Seizures, when present, are often infantile-onset (infantile spasms reported in the original Nakashima et al. 2020 case series).
- **Progression:** Largely a static/developmental disorder rather than degenerative, though:
  - Developmental **regression** can follow seizure onset in a subset.
  - Movement-disorder features (dystonia, tremor, spasms) have been reported to emerge or become more prominent in **adulthood**, following childhood hypotonia — suggesting an evolving, age-dependent motor phenotype.
- **Disease course:** Chronic, lifelong neurodevelopmental condition; no reports of spontaneous resolution of the core intellectual/developmental features.
- **Critical periods:** Early childhood is emphasized as the critical window for intervention — specialist guidance (e.g., CUL3 Foundation/family advocacy resources) recommends initiating physical, occupational, speech, and behavioral therapies "as early as possible, ideally before a child begins school" ([cul3.org](https://www.cul3.org/common-questions)).

---

## 9. Inheritance and Population

- **Epidemiology:** Prevalence and incidence are unknown/not established; the condition is rare, with only several dozen molecularly confirmed cases published to date (aggregate across case reports and the two largest cohorts of 26 and 37 individuals). The CUL3 patient advocacy organization states there is no reliable estimate of the number of individuals living with the condition worldwide, and likely substantial underascertainment ([cul3.org](https://www.cul3.org/common-questions)).
- **Inheritance pattern:** Autosomal dominant (OMIM #619239); the great majority of cases are **de novo**; rare parent-to-child transmission and germline mosaicism are possible but not well-quantified.
- **Penetrance:** Appears high for the core developmental delay/intellectual disability phenotype but **incomplete/variable for specific features** — seizures and autism are present in only a subset of variant carriers ("with or without" nomenclature reflects this variable expressivity), and some individuals show neither.
- **Expressivity:** Highly variable across affected individuals, even among those with similar variant classes.
- **Genetic anticipation:** Not reported/applicable (not a repeat-expansion disorder).
- **Founder effects:** None specifically reported.
- **Consanguinity:** Not a relevant risk factor, given the dominant de novo mechanism.
- **Carrier frequency:** Not applicable (de novo dominant disorder, not a recessive carrier-screening condition).
- **Population demographics:** No ethnic, geographic, or sex-based enrichment has been specifically reported; the Sadler et al. cohort included 15 males and 11 females, without strong sex skew noted. Cases have been reported from multiple countries (Japan, Malaysia, Netherlands, USA, Turkey, China, and others), consistent with a pan-ethnic de novo disorder.

---

## 10. Diagnostics

- **Genetic testing (primary diagnostic modality):**
  - **Whole exome sequencing (WES)** or **whole genome sequencing (WGS)** with trio (parent-child) analysis is the standard approach, given the de novo, genetically heterogeneous nature of neurodevelopmental disorders; this is how essentially all published cases have been identified.
  - **Multi-gene neurodevelopmental disorder / intellectual disability / autism gene panels** that include CUL3 are also used clinically (e.g., Genomics England PanelApp intellectual disability panel lists CUL3 as a "green"/definitive gene).
  - **Chromosomal microarray (CMA)** can detect the large-deletion CNV mechanism encompassing CUL3.
  - Single-gene Sanger confirmation is used once a candidate variant is identified.
- **Emerging diagnostic tool — DNA methylation episignature:** A CUL3-specific episignature (213 differentially methylated CpG probes, predominantly hypomethylated in "signature-positive" cases) has been validated as a functional classifier that can help resolve variants of uncertain significance (Sadler et al. 2024/2025, PMID:39501558) — an approach paralleling episignature testing used for other chromatin/ubiquitin-pathway neurodevelopmental disorders.
- **Clinical/phenotypic criteria:** No formal consensus clinical diagnostic criteria exist (as for a purely molecularly defined disorder); diagnosis rests on genetic confirmation plus compatible phenotype.
- **Differential diagnosis:** Other monogenic neurodevelopmental disorders with overlapping developmental delay/autism/seizure phenotype, particularly other ubiquitin-proteasome pathway or chromatin-regulator disorders; and, importantly, **must be distinguished from PHA2E** (exon-9 splice-region CUL3 variants) which is a distinct renal/endocrine phenotype without neurodevelopmental features.
- **Supportive/monitoring investigations** (per patient advocacy clinical guidance, cul3.org): cardiac echocardiogram, EEG, brain MRI, growth monitoring, and referrals to developmental pediatrics, cardiology, neurology, endocrinology, gastroenterology, and psychology as indicated by individual presentation.
- **Screening:** No population or newborn screening program exists (rare, de novo, molecularly heterogeneous disorder); prenatal detection is occurring increasingly via prenatal exome/genome sequencing when structural anomalies (e.g., growth restriction) are noted on ultrasound (Gofin et al. 2026, *Prenatal Diagnosis*, "CUL3-Related Neurodevelopmental Disorder: Expanding the Prenatal Phenotype").

---

## 11. Outcome/Prognosis

- **Survival/mortality:** No specific mortality data or life-expectancy reduction has been reported in the literature reviewed; the disorder is not classically associated with early mortality, though cardiac defects and severe epilepsy in a subset of patients could theoretically affect morbidity.
- **Morbidity/function:** Variable functional impairment ranging from mild learning disability to significant intellectual disability with motor and behavioral involvement; adult-onset movement disorder (dystonia/tremor/spasms) may add to long-term morbidity in some patients.
- **Quality of life:** Not formally measured with standardized QOL instruments in published literature to date.
- **Complications:** Seizures (with possible regression), cardiac septal defects, feeding difficulties/failure to thrive, and orthopedic/limb anomalies are recurring complications.
- **Recovery potential:** Developmental gains are achievable with early, sustained multidisciplinary therapy (physical, occupational, speech, behavioral), per current expert/family-advocacy guidance, though the underlying intellectual disability and neurodevelopmental features are lifelong.
- **Prognostic factors:** Presence/absence of seizures and autism are the major axes of clinical heterogeneity noted in the disorder's name and clinical descriptions; whether specific variant type (truncating vs. missense) or "episignature-positive" status correlates with a more severe/distinct phenotype is an active area of study (the episignature-positive subgroup in Sadler et al. showed higher rates of ADHD, MRI abnormalities, cardiac defects, and feeding problems, suggesting a possible phenotype-genotype/epigenotype correlation).

---

## 12. Treatment

There is **no disease-modifying or curative treatment**; management is entirely supportive/symptomatic, consistent with the current understanding stated by the patient advocacy organization: "There is currently no cure or drug treatment" ([cul3.org](https://www.cul3.org/common-questions)).

- **Supportive/rehabilitative care:**
  - Physical therapy — NCIT:C15302 (Physical Therapy)
  - Occupational therapy — NCIT:C121351 (Occupational Therapy)
  - Speech-language therapy — NCIT:C159273 (Speech Therapy)
  - Behavioral therapy/counseling (for autism-spectrum features) — NCIT:C181743 (Behavioral Counseling) or a therapeutic-procedure equivalent
  - Early intervention services are specifically emphasized as most effective when initiated before school age.
- **Pharmacotherapy:** Symptomatic only — e.g., antiseizure medications for the subset with epilepsy (agent selection driven by seizure type, not CUL3-specific; infantile spasms historically treated per standard protocols such as ACTH/vigabatrin in the general infantile-spasms population, though no CUL3-specific efficacy data were identified) — NCIT:C15986 (Pharmacotherapy).
- **Surgical/interventional:** Cardiac surgical correction for septal defects when clinically indicated — NCIT:C15329 (Surgical Procedure).
- **Genetic counseling:** NCIT:C15240 (Genetic Counseling) — recommended for all families given the (usually de novo) inheritance, to discuss recurrence risk (low but nonzero due to possible germline mosaicism) and reproductive options.
- **Experimental/research directions:** Mechanistic mouse-model work (Amar et al. 2021, PMID:33727673) demonstrating that pharmacological **RhoA inhibition rescues dendritic and network activity phenotypes** identifies RhoA/actin-cytoskeleton signaling as a plausible future therapeutic target, though this remains preclinical and has not translated to human trials.
- **Clinical trials:** No CUL3/NEDAUS-specific interventional trials were identified in this search (ClinicalTrials.gov was not directly queried in this pass but no trial was surfaced via general search).

---

## 13. Prevention

- No primary prevention exists for this de novo genetic disorder.
- **Secondary prevention/early detection:** Prenatal diagnosis via exome/genome sequencing is increasingly reported, especially when fetal growth restriction or structural anomalies are noted on ultrasound (Gofin et al. 2026, *Prenatal Diagnosis*); this enables early postnatal surveillance and early-intervention referral.
- **Genetic counseling:** Central preventive/risk-management tool for families, addressing recurrence risk (low, given predominant de novo origin, but genetic counselors should discuss the possibility of parental germline mosaicism).
- **Tertiary prevention:** Early multidisciplinary surveillance (cardiac, neurologic/EEG, growth, GI) to detect and manage complications early, as recommended by patient advocacy/clinical guidance.

---

## 14. Other Species / Natural Disease

- No naturally occurring CUL3-related neurodevelopmental disease has been reported in companion animals or wildlife (OMIA search not specifically performed, but no evidence surfaced).
- **Comparative biology:** CUL3 is highly evolutionarily conserved; the *Drosophila melanogaster* ortholog Cullin-3 and the murine ortholog *Cul3* (MGI:1347360) are used extensively in mechanistic modeling (see Model Organisms below), reflecting deep conservation of the CRL3 ubiquitin-ligase pathway across metazoans.
- **Zoonotic potential:** Not applicable (a genetic, non-infectious disorder).

---

## 15. Model Organisms

Multiple genetically engineered animal and invertebrate models recapitulate aspects of CUL3 haploinsufficiency:

**Mouse models:**
1. **Germline haploinsufficient Cul3 mouse (Amar/Dong et al. 2021, *Mol Psychiatry*, PMID:33727673):** CRISPR/Cas9-generated 1-bp frameshifting insertion in exon 6 of *Cul3* (C57BL/6N background). Phenotypes: reduced cortical volume from early postnatal development (on brain MRI), social and cognitive deficits, hyperactive behavior, reduced dendritic growth and filamentous actin puncta, reduced spontaneous neuronal network activity — **rescued by pharmacological RhoA inhibition**, directly implicating RhoA as the key downstream mechanistic substrate. Access: [PMC8443683](https://pmc.ncbi.nlm.nih.gov/articles/PMC8443683/) / [bioRxiv preprint](https://www.biorxiv.org/content/10.1101/2020.02.07.939256v1).
2. **Cholinergic-neuron-restricted Cul3 knockout (2023, *Translational Psychiatry*, PMID:36693858):** Conditional ablation of Cul3 in cholinergic neurons recapitulates ASD-like social and sensory-gating deficits and cognitive impairment, with diminished basal-forebrain cholinergic neuron activity and implication of prefrontal cortex cholinergic projections in the cognitive phenotype.
3. **Postnatal forebrain-restricted conditional knockout (Sekar et al. 2025, *Genes Brain Behav*, PMC12536218):** CaMKIIα-Cre x floxed-*Cul3* mice with delayed postnatal deletion in predominantly forebrain excitatory neurons. Phenotypes: repetitive jumping, reduced marble burying, increased locomotion, impaired motor coordination, and increased hindlimb clasping — demonstrating that even **postnatal**, cell-type-restricted loss of Cul3 (not just developmental/germline loss) is sufficient to cause robust behavioral abnormalities, relevant to therapeutic-window considerations.
4. **Cul3 gene resource:** MGI:1347360 ([Mouse Genome Informatics](https://www.informatics.jax.org/marker/MGI:1347360)).

**Drosophila model:**
- Neuronal knockdown of Cullin3 in flies (2024, *Scientific Reports*, [PMC10794434](https://pmc.ncbi.nlm.nih.gov/articles/PMC10794434/)) reproduces multiple ASD-relevant phenotypes: short sleep, reduced courtship behavior, impaired courtship-suppression learning/memory, faster starvation and lower triacylglyceride levels (metabolic/lipid dysregulation), heightened hyperoxia sensitivity (oxidative stress), and severe mushroom-body neuroanatomical defects (93% of knockdown brains missing at least one lobe; ~36% lacking αβ projections) — establishing an invertebrate model of both behavioral and structural neurodevelopmental phenotypes.

**Applications:** These models collectively support study of (a) cortical neurogenesis and dendritic/cytoskeletal defects, (b) circuit-specific (cholinergic/prefrontal) contributions to cognitive and social phenotypes, (c) postnatal reversibility/rescue windows, and (d) conserved metabolic/sleep phenotypes — and provide the RhoA-pathway rescue data that constitute the field's leading candidate mechanism-based therapeutic hypothesis.

**Limitations:** No model fully recapitulates the human seizure phenotype or the specific dysmorphic/growth features reported clinically; cross-species translational fidelity for the epilepsy and craniofacial/limb components remains an open question (a candidate `HUMAN_MODEL_MISMATCH`-type gap for curation purposes).

---

## Summary of Key Primary Literature (PMID-anchored)

| Citation | PMID/DOI | Contribution |
|---|---|---|
| De Rubeis et al. 2014, *Nature* | PMID:25363760 | CUL3 identified as high-confidence ASD gene (Autism Sequencing Consortium) |
| Nakashima et al. 2020, *J Hum Genet* | PMID:32341456 | First clinical description establishing NEDAUS (3 patients, de novo CUL3 variants) |
| Satterstrom et al. 2020, *Cell* | PMID:31981491 | Large-scale exome sequencing confirms CUL3 among 102 high-confidence ASD genes |
| Amar/Dong et al. 2021, *Mol Psychiatry* | PMID:33727673 | Haploinsufficient Cul3 mouse model; RhoA-dependent cortical/synaptic mechanism |
| Cholinergic Cul3 KO, 2023, *Transl Psychiatry* | PMID:36693858 | Basal-forebrain cholinergic circuit mechanism for behavioral phenotype |
| Review, 2023, *Front Psychiatry* | PMID:37575562 | "Current trends of high-risk gene Cul3 in neurodevelopmental disorders" |
| Nonsense mutation case report, 2023, *Medicine* | — | ASD + epilepsy phenotype, Chinese cohort |
| Sadler et al. 2024/2025, *HGG Advances* (ScienceDirect) | PMID:39501558 | Largest cohort to date (n=26); episignature discovery; detailed phenotype frequencies |
| Blackburn et al. 2025, *Ann Neurol* | DOI:10.1002/ana.27077 | 37-family cohort establishing loss-of-function CUL3 as cause of syndromic NDD |
| Sekar et al. 2025, *Genes Brain Behav* | PMC12536218 | Postnatal forebrain conditional knockout mouse model |
| Gofin et al. 2026, *Prenatal Diagnosis* | DOI:10.1002/pd.70106 | Expanded prenatal phenotype (fetal growth restriction) |

---

### Sources
- [OMIM #619239 — NEDAUS](https://omim.org/entry/619239)
- [OMIM *603136 — CUL3](https://omim.org/entry/603136)
- [MONDO:0030994 — Monarch Initiative](https://monarchinitiative.org/MONDO:0030994)
- [MedlinePlus Genetics — CUL3-related neurodevelopmental disorder](https://medlineplus.gov/genetics/condition/cul3-related-neurodevelopmental-disorder/)
- [NIH GTR — Condition C5543225](https://www.ncbi.nlm.nih.gov/gtr/conditions/C5543225/)
- [Sadler et al., PMC11617854 (PMID:39501558)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11617854/)
- [PubMed 32341456 — Nakashima et al. 2020](https://pubmed.ncbi.nlm.nih.gov/32341456/)
- [PubMed 33727673 — Amar/Dong et al. 2021](https://pubmed.ncbi.nlm.nih.gov/33727673/)
- [PubMed 36693858 — Cholinergic Cul3 KO 2023](https://pubmed.ncbi.nlm.nih.gov/36693858/)
- [PubMed 37575562 — Review, Front Psychiatry 2023](https://pubmed.ncbi.nlm.nih.gov/37575562/)
- [PubMed 31981491 — Satterstrom et al. 2020](https://pubmed.ncbi.nlm.nih.gov/31981491/)
- [SFARI Gene — CUL3](https://gene.sfari.org/database/human-gene/CUL3)
- [Genomics England PanelApp — CUL3](https://panelapp.genomicsengland.co.uk/panels/285/gene/CUL3/)
- [ClinGen — CUL3 gene curation](https://search.clinicalgenome.org/kb/genes/HGNC:2553)
- [Drosophila Cullin3 knockdown model, PMC10794434](https://pmc.ncbi.nlm.nih.gov/articles/PMC10794434/)
- [Sekar et al. 2025, PMC12536218 — postnatal forebrain Cul3 KO](https://pmc.ncbi.nlm.nih.gov/articles/PMC12536218/)
- [Blackburn et al. 2025, Annals of Neurology](https://onlinelibrary.wiley.com/doi/10.1002/ana.27077)
- [Gofin et al. 2026, Prenatal Diagnosis](https://obgyn.onlinelibrary.wiley.com/doi/10.1002/pd.70106)
- [PHA2E — OMIM #614496 (differential/distinct CUL3 phenotype)](https://omim.org/entry/614496)
- [PMC4604684 — CUL3 exon 9 mutation mechanism in PHA2E](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4604684/)
- [CUL3 Foundation — Common Questions (patient/family resource)](https://www.cul3.org/common-questions)
- [MalaCards — NEDAUS](https://www.malacards.org/card/neurodevelopmental_disorder_with_or_without_autism_or_seizures)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 15 |
| Off topic | 0 |

All extracted references resolved successfully.