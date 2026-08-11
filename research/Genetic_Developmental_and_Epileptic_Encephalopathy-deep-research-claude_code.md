---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-07-31T00:14:04.375255'
end_time: '2026-07-31T00:19:29.167947'
duration_seconds: 324.79
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Genetic Developmental and Epileptic Encephalopathy
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
    extra_args: []
run_metadata:
  models_used:
  - claude-haiku-4-5-20251001
  - claude-sonnet-5
  web_search_requests: 16
  num_turns: 17
  total_cost_usd: 1.7151305
  session_id: 1cf817d3-a544-533d-aab9-ff6c499e43b3
  stop_reason: end_turn
citation_count: 31
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Genetic Developmental and Epileptic Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Genetic Developmental and Epileptic Encephalopathy** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Output

# Genetic Developmental and Epileptic Encephalopathy (DEE) — Comprehensive Research Report

## 1. Disease Information

**Overview.** Developmental and Epileptic Encephalopathy (DEE) is a diagnostic category — not a single disease — formalized by the ILAE 2017 Classification and refined by the ILAE Task Force on Nosology and Definitions in 2022, which split early-onset epilepsy syndromes into (a) self-limited epilepsies with age-related spontaneous remission and (b) DEEs, in which seizures and/or the underlying epileptiform activity itself contribute to a progressive or static encephalopathy with developmental impairment that is independent of (and often precedes) seizure onset. **"Genetic DEE"** denotes the subset — now understood to be the majority of DEE cases once modern sequencing is applied — in which a single-gene (monogenic) or, less commonly, oligogenic/copy-number variant is the etiology, as opposed to structural (malformations, HIE, stroke), metabolic, infectious, or immune causes. DEEs are the most severe end of the developmental and epileptic spectrum: drug-resistant seizures of multiple types, epileptiform EEG abnormalities, and intellectual disability/developmental regression, typically presenting in infancy or early childhood. ([MedLink Neurology](https://www.medlink.com/articles/developmental-and-epileptic-encephalopathies); [Nature Reviews Disease Primers 2024, Scheffer et al., DOI:10.1038/s41572-024-00546-6](https://www.nature.com/articles/s41572-024-00546-6); [Epilepsy Foundation](https://www.epilepsy.com/what-is-epilepsy/rare-epilepsies/developmental-and-epileptic-encephalopathy))

**Key identifiers.**
- **OMIM Phenotypic Series:** [PS308350](https://www.omim.org/phenotypicSeries/PS308350) — "Developmental and epileptic encephalopathy," an umbrella series currently listing **123 numbered entries** (DEE1 through DEE9x+), each corresponding to a distinct causal gene (e.g., DEE1/ARX #308350, DEE2/CDKL5 #300672, DEE9/PCDH19 #300088, DEE42/GRIN1 #617106, DEE50/CACNA1A #616457).
- **MONDO:** the umbrella concept maps to **MONDO:0010246** ("developmental and epileptic encephalopathy," a grouping term cross-referencing OMIM PS308350); individual gene-defined subtypes each carry their own MONDO ID (e.g., DEE2/CDKL5 disorder, DEE9/PCDH19-clustering epilepsy).
- **Orphanet:** listed both as an umbrella grouping and as ~100+ individual gene-specific ORPHA entries (e.g., Dravet syndrome ORPHA:33069, CDKL5 deficiency disorder, STXBP1 encephalopathy).
- **ICD-11:** most individual DEEs fall under `8A61-8A62` (developmental and epileptic encephalopathy codes) in the ICD-11 neurology chapter, replacing the non-specific ICD-10 G40.x/Q04 mappings.
- **MeSH:** "Epileptic Syndromes," "Spasms, Infantile" and related descriptors are used as approximations; there is no single dedicated MeSH heading for genetic DEE as a class.

**Synonyms/alternative names:** "genetic epileptic encephalopathy," "early-onset epileptic encephalopathy (EOEE)," "malignant epilepsy of infancy," historically overlapping with "West syndrome," "Ohtahara syndrome," "early myoclonic encephalopathy (EME)," "Dravet syndrome," "Lennox-Gastaut syndrome," and (per the current 2022 ILAE nosology) many are now renamed with the causal gene as the syndrome name (e.g., "SCN1A-DEE," "STXBP1-DEE," "KCNQ2-DEE"). The 2022 ILAE terminology also folds in "developmental encephalopathy" (developmental impairment without frequent epileptiform activity) and "epileptic encephalopathy" (impairment driven mainly by epileptiform activity) as component concepts within the DEE spectrum.

**Data provenance:** Most of the literature base is **aggregated disease-level** knowledge (case series, gene-specific natural history cohorts, systematic reviews, ClinVar/gene-disease curation, and increasingly large national/international patient registries such as the RIKEE, Rare Epilepsy Network, and gene-specific foundation registries — e.g., FamilieSCN2A, CDKL5 Centers of Excellence). A growing minority is derived from population-based, prospective **individual-level EHR/clinical cohorts** (e.g., the Scottish national cohort, PMID:31363746, and the companion "Epidemiology of DEE" study, PMID:36581463) that ascertain every child with new-onset seizures in a defined region/time window — these are the most reliable source of incidence/prevalence figures cited below.

---

## 2. Etiology

**Disease causal factors.** By definition, genetic DEE is caused by a pathogenic variant — usually a **de novo, heterozygous, single-nucleotide or small indel variant** — in one of a rapidly growing list of genes. Next-generation sequencing (whole-exome/whole-genome sequencing, WES/WGS) has now implicated **more than 900 genes** in DEE pathogenesis. In clinical diagnostic cohorts, exome/panel sequencing establishes a molecular diagnosis in roughly **35–43%** of unselected DEE cases (higher — ~41% — when seizure onset is under 2 years of age, vs. ~18% for later onset), reflecting how heavily the genetic architecture is skewed toward infantile-onset disease. ([PubMed 35701389](https://pubmed.ncbi.nlm.nih.gov/35701389/); [PMC10816140](https://pmc.ncbi.nlm.nih.gov/articles/PMC10816140/); [PMC12562696](https://pmc.ncbi.nlm.nih.gov/articles/PMC12562696/))

The most frequently implicated genes across diagnostic cohorts are **SCN1A** (Dravet syndrome — the single most common monogenic DEE, expected population frequency ≥1:20,000, and the archetype gene), **STXBP1**, **SCN2A**, **KCNQ2**, **CDKL5**, **SCN8A**, **PCDH19** (X-linked, affects heterozygous females), **GRIN1/GRIN2A/GRIN2B/GRIN2D**, **GABRA1/GABRB2/GABRB3/GABRG2**, **GNAO1**, **ARX**, **FOXG1**, **SPTAN1**, and dozens of others (e.g., **HCN1, FGF12, PLCB1, WWOX, SLC35A2, ST3GAL3, ATP6V1A**). ([EAN Spring School slide deck, McTague/Nabbout](https://www.ean.org/fileadmin/user_upload/ean/ean/learn/educational_events/Spring_School/Nabbout_Landscape_of_genetic_in_DEEs_Mc_Tague.pdf); [PMC12562696](https://pmc.ncbi.nlm.nih.gov/articles/PMC12562696/))

**Genetic risk factors.**
- Causal variants: predominantly **de novo dominant** (autosomal or X-linked). Recurrent "hotspot" pathogenic variants occur in several genes (e.g., KCNQ2 recurrent missense variants clustering in the pore/voltage-sensor domains).
- Susceptibility/modifier loci are an active area of study but poorly characterized for most single-gene DEEs; polygenic background may modulate expressivity/severity in some genes (e.g., SCN1A modifier loci affecting Dravet syndrome severity, studied in mouse genetic background experiments).
- Rare biallelic (autosomal recessive) forms exist for a subset of genes (e.g., some **STXBP1**, **PIGA**, and metabolic-DEE genes), and germline/somatic **mosaicism** is documented (notably for **PCDH19**, where affected females are typically heterozygous post-zygotic mosaic-unaffected-carrier males transmit to daughters — the "cellular interference" model).

**Environmental risk factors:** Largely not causal for genetic DEE per se, but febrile illness is a well-documented **trigger/exacerbating factor** in several gene-specific DEEs (e.g., fever-triggered seizure clusters in PCDH19-clustering epilepsy and in Dravet syndrome/SCN1A). Perinatal factors (prematurity, hypoxic injury) are relevant to the *non-genetic* DEE differential but are not causal for the monogenic forms; they may occasionally act as second hits modulating phenotype severity.

**Protective factors:** No established genetic protective variants for DEE broadly. In SCN1A-Dravet syndrome, some evidence suggests that variants reducing background Nav1.6 (SCN8A) function can partially compensate for Nav1.1 haploinsufficiency in mouse models (a genetic modifier concept), but this is not yet clinically actionable. Early, aggressive control of seizure burden and avoidance of sodium-channel-blocking antiseizure medications (contraindicated in SCN1A loss-of-function Dravet syndrome) function as protective clinical-management factors rather than biological protective factors.

**Gene-environment interactions:** The clearest documented interaction is fever/hyperthermia acting on genetically hyperexcitable or dysfunctional interneuron circuits (SCN1A, PCDH19) to precipitate seizure clusters — a mechanism actively studied with animal thermal-induction models.

---

## 3. Phenotypes

DEE phenotypes span **symptoms/signs, laboratory/EEG abnormalities, and behavioral/cognitive manifestations**. Representative phenotype categories with suggested HPO terms:

| Phenotype | HPO term (suggested) | Onset | Frequency/notes |
|---|---|---|---|
| Multiple seizure types (focal, tonic, myoclonic, atonic, spasms) | HP:0032900 (Seizure), HP:0011097 (Epileptic spasm), HP:0002123 (Generalized myoclonic seizure), HP:0002133 (Focal-onset seizure) | Neonatal–infancy (often <2y) | Nearly universal (defining feature) |
| Developmental delay / regression | HP:0001263 (Developmental delay), HP:0002376 (Developmental regression) | Often precedes seizures, or occurs with seizure onset | Universal by definition of DEE |
| Intellectual disability | HP:0001249 (Intellectual disability) | Emerges progressively | 79% severe ID reported in KCNQ2-DEE cohorts; near-universal in CDKL5, STXBP1 |
| EEG burst-suppression pattern | HP:0010851 (Burst-suppression) | Neonatal (Ohtahara/EIMFS-type presentations) | Present in ~62% of early KCNQ2-DEE |
| Hypsarrhythmia / infantile spasms | HP:0011097; HP:0012469 (Infantile spasms) | 3–12 months | Classic in West-syndrome-type DEEs (e.g., some KCNQ2, STXBP1, CDKL5) |
| Autistic features | HP:0000729 (Autistic behavior) | Childhood | ~67% in KCNQ2-DEE; frequent across CDKL5, STXBP1, PCDH19 |
| Hand stereotypies / Rett-like features | HP:0004328 (Hand stereotypies) | Childhood | Characteristic of CDKL5 deficiency disorder |
| Microcephaly (acquired) | HP:0000252 | Postnatal deceleration | Reported in CDKL5, FOXG1-DEE |
| Motor dysfunction / hypotonia / spasticity | HP:0001252 (Hypotonia), HP:0002061 (Spastic tetraparesis) | Variable | 80–90% in STXBP1 |
| Feeding difficulties / dysphagia | HP:0011968 | Infancy | Common, especially CDKL5 (PEG placement frequent) |
| Cortical visual impairment | HP:0100704 | Infancy/childhood | Reported in CDKL5 |
| ADHD/OCD/psychiatric comorbidity | HP:0007018; HP:0000722 | School age | ~30–70% in PCDH19, STXBP1 cohorts |

**Characteristics.**
- **Onset:** highly gene-dependent — neonatal (KCNQ2, STXBP1, SCN2A/SCN8A gain-of-function, GNAO1), early infantile (SCN1A/Dravet ~5–8 months, CDKL5 <4 months, PCDH19 6–36 months), or later childhood in milder allelic series.
- **Severity/progression:** typically progressive early, often plateauing; a subset (notably some KCNQ2-DEE) shows eventual seizure freedom (~73%) despite persistent severe intellectual disability — illustrating that seizure control and developmental outcome are partially dissociable, a key DEE concept.
- **Course:** episodic seizure clustering is characteristic of PCDH19 and Dravet syndrome (fever-triggered clusters); other genes show a more chronic, drug-resistant daily-seizure pattern (e.g., CDKL5, STXBP1).
- **QoL impact:** severe — most children require lifelong caregiver support; validated DEE-specific QoL instruments (e.g., the Quality of Life in Childhood Epilepsy [QOLCE], and newer DEE-specific PRO measures used in Dravet/CDKL5/STXBP1 trials) consistently show impairment across physical, cognitive, and family-burden domains. ([Nature Reviews Disease Primers 2024](https://www.nature.com/articles/s41572-024-00546-6) covers QoL explicitly per its abstract scope.)

---

## 4. Genetic/Molecular Information

**Causal genes** (representative, non-exhaustive; each an OMIM DEE phenotypic-series entry):
- **SCN1A** (OMIM *182389; DEE6/Dravet syndrome #607208) — voltage-gated Na⁺ channel Nav1.1, predominantly expressed in GABAergic interneurons; loss-of-function (haploinsufficiency).
- **STXBP1** (*602926; DEE4 #612164) — syntaxin-binding protein 1 (Munc18-1), core SNARE-complex regulator of synaptic vesicle fusion; predominantly loss-of-function/haploinsufficiency.
- **SCN2A** (*182390; DEE11 #613721) — Nav1.2, predominantly in excitatory neurons; **both gain-of-function (early-infantile, severe)** and **loss-of-function (later-onset, milder, autism-predominant)** variants cause distinct phenotypes on the same gene.
- **KCNQ2** (*602235; DEE7 #613720) — Kv7.2 voltage-gated K⁺ channel subunit (M-current); dominant-negative or loss-of-function variants.
- **CDKL5** (*300203; DEE2 #300672) — X-linked cyclin-dependent-kinase-like 5, a serine/threonine kinase important for neuronal synaptic maturation; loss-of-function.
- **SCN8A** (*600702; DEE13 #614558) — Nav1.6; typically gain-of-function.
- **PCDH19** (*300460; DEE9 #300088) — X-linked protocadherin-19, a cell-adhesion molecule; unusually, affects **heterozygous females** (cellular-interference mechanism), while hemizygous males are typically unaffected carriers.
- **GRIN1/GRIN2A/GRIN2B/GRIN2D** — NMDA receptor subunits; gain- or loss-of-function depending on variant location (pre-M1, M3, M4 helices).
- **GABRA1/GABRB2/GABRB3/GABRG2** — GABA-A receptor subunits; loss-of-function impairing GABAergic inhibition.
- **GNAO1** (*139311; DEE17 #615473) — Gαo subunit; loss of cAMP-inhibitory function, also causes a prominent movement-disorder phenotype.
- **ARX** (*300382; DEE1 #308350) — X-linked homeobox transcription factor; spectrum from lissencephaly to infantile spasms to isolated intellectual disability depending on variant type/location.

**Pathogenic variant classification (ACMG/AMP via ClinVar/ClinGen):** the overwhelming majority of reported DEE variants are classified **Pathogenic/Likely Pathogenic**; VUS remain common in less well-studied genes and require functional/segregation follow-up. **Variant types:** missense (most common, especially in channel/receptor genes — often clustering in functionally critical domains: pore, voltage-sensor, ligand-binding), frameshift/nonsense/splice-site (common in haploinsufficiency genes like STXBP1, CDKL5), and occasionally structural (partial gene deletions, e.g., in **SLC35A2**, or larger CNVs overlapping DEE loci).

**Allele frequency:** essentially **absent from population databases** (gnomAD, TOPMed) for the pathogenic DEE variants themselves, consistent with strong negative selection against de novo dominant, early-lethal/severely-disabling alleles — absence from gnomAD is itself used as supporting evidence (ACMG PM2) in variant classification.

**Somatic vs. germline:** the great majority of DEE-causing variants are **germline de novo**; **parental germline mosaicism** is well documented (important for recurrence-risk counseling, since apparently "de novo" variants can recur in siblings at rates of a few percent) and **somatic mosaicism in the proband** is documented for several genes (notably PCDH19 males, and mosaic SCN1A/SCN2A).

**Functional consequences:** span **loss-of-function** (channel/receptor haploinsufficiency, most common mechanism overall), **gain-of-function** (increased channel current, e.g., SCN2A/SCN8A early-infantile variants), and **dominant-negative** effects (e.g., some KCNQ2 pore variants disrupting tetrameric channel assembly) — the distinction is clinically critical because it determines precision-therapy direction (sodium-channel blockers help gain-of-function SCN2A/SCN8A but are contraindicated/harmful in loss-of-function SCN1A-Dravet syndrome).

**Modifier genes:** poorly characterized in humans; mouse genetic-background studies (e.g., Scn1a Dravet models on different inbred strains) show strong modifier effects on seizure severity and SUDEP risk, implicating candidate modifier loci not yet translated to human genetic counseling.

**Epigenetic information:** limited disease-specific data; **FOXG1** and **CDKL5** intersect with chromatin/transcriptional regulation pathways relevant to Rett-spectrum overlap. DNA methylation studies in DEE are largely investigational.

**Chromosomal abnormalities:** copy-number variants overlapping DEE genes (e.g., 15q11-q13 duplications affecting GABRB3, Xp22 deletions affecting CDKL5/ARX region) are recognized causes; array-based/ES-based CNV calling is now integrated into standard DEE diagnostic workups.

---

## 5. Environmental Information

Genetic DEE is, by definition, gene-driven, but several **environmental modulators** are clinically important:
- **Febrile illness/hyperthermia:** the dominant seizure trigger in SCN1A-Dravet syndrome and PCDH19-clustering epilepsy; vaccination-associated fever can also trigger the first Dravet syndrome seizure (a well-documented but non-causal temporal association — vaccination does not cause the underlying SCN1A mutation).
- **Sleep deprivation, illness, and metabolic stress** are general seizure-threshold-lowering factors across most DEEs, as in epilepsy generally.
- **Infectious agents:** not a direct cause of genetic DEE, but concurrent/triggering infections (viral URIs, gastroenteritis) frequently precede seizure clusters.
- **Lifestyle/behavioral factors:** not established as disease-modifying for genetic DEE specifically (contrast with acquired/structural epilepsies where perinatal/lifestyle factors are more directly causal).

---

## 6. Mechanism / Pathophysiology

The pathophysiology of genetic DEE converges on **disrupted neuronal excitability and/or disrupted neurodevelopmental programs**, broadly falling into two overlapping mechanistic classes reviewed in [Nature Reviews Disease Primers 2024 (Scheffer et al.)](https://www.nature.com/articles/s41572-024-00546-6) and [PMC11763800 "Pathogenesis of Intellectual Disability Beyond Channelopathies"](https://pmc.ncbi.nlm.nih.gov/articles/PMC11763800/):

1. **Channelopathies** — direct disruption of voltage-gated ion channels (Na⁺: SCN1A/SCN2A/SCN8A/SCN1B; K⁺: KCNQ2/KCNQ3, KCNB1; Ca²⁺: CACNA1A) or ligand-gated channels (GABA-A receptor subunits, NMDA receptor subunits GRIN1/2A/2B/2D) causing an **excitation/inhibition (E/I) imbalance**. Mechanistically:
   - SCN1A loss-of-function selectively impairs Nav1.1 current in **GABAergic interneurons** (parvalbumin- and somatostatin-positive), producing **disinhibition** and network hyperexcitability — the accepted mechanism for Dravet syndrome.
   - SCN2A/SCN8A gain-of-function increases persistent/late Na⁺ current in excitatory pyramidal neurons, directly increasing intrinsic excitability; loss-of-function SCN2A variants instead impair excitatory neurotransmission and correlate with a milder, later-onset, autism-predominant phenotype — illustrating a single gene producing opposite mechanistic and clinical poles.
   - GABA-A receptor subunit variants (GABRA1/B2/B3/G2) directly reduce **phasic and/or tonic inhibitory GABAergic signaling**; tonic (extrasynaptic GABA-A-receptor-mediated) inhibition disruption is an emerging, specifically implicated DEE mechanism.
   - GRIN2B and related NMDA receptor variants (pre-M1/M3/M4 helix) alter glutamatergic excitatory drive and can be gain- or loss-of-function depending on variant location.

2. **Synaptopathies / neurodevelopmental-program disruption** — genes not encoding channels but disrupting synaptic vesicle trafficking, synaptic protein scaffolding, or neuronal signaling cascades:
   - **STXBP1** (Munc18-1) — core regulator of SNARE-complex-mediated synaptic vesicle fusion; haploinsufficiency impairs both excitatory and inhibitory neurotransmitter release, and recent work shows GABAergic/glycinergic and glutamatergic neurons mediate **distinct** components of the STXBP1 encephalopathy phenotype ([PMC10993039](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10993039/)).
   - **CDKL5** — a kinase important for activity-dependent synaptic maturation and dendritic spine development; loss-of-function impairs neuronal circuit maturation rather than acute channel function.
   - **PCDH19** — a cell-adhesion protocadherin; disease mechanism is **cellular interference** between PCDH19-mutant and wild-type neurons in a mosaic tissue, disrupting normal neuronal patterning/network formation (explaining the unusual female-restricted, mosaicism-dependent inheritance).
   - **GNAO1** — disrupted G-protein/cAMP signal transduction affecting neuronal excitability and additionally producing a hyperkinetic movement disorder via basal ganglia circuit dysfunction.
   - **ARX** — transcription factor controlling GABAergic interneuron migration/differentiation during cortical development; disease mechanism is fundamentally a **developmental/migrational** one rather than acute channel dysfunction, explaining the ARX phenotypic spectrum from lissencephaly to isolated epilepsy.

3. **Beyond channelopathy/synaptopathy** mechanisms reviewed in PMC11763800 include impaired neurogenesis, disrupted dendrite/axon growth, and (for a subset of genes, e.g., mTOR-pathway-adjacent genes in focal cortical dysplasia-associated DEEs) **mTOR pathway hyperactivation** driving abnormal cortical lamination and cytomegalic neurons — though the classic mTORopathies (TSC1/2, DEPDC5, mTOR) are more commonly discussed under focal/structural epilepsy overlap than "pure" genetic DEE.

**Causal chain (generalized):** germline variant → altered channel/synaptic-protein function (loss-of-function, gain-of-function, or dominant-negative) → cell-type-specific dysfunction (interneuron hypoexcitability in Dravet; pyramidal hyperexcitability in SCN2A/SCN8A-GOF; synaptic vesicle release failure in STXBP1) → network-level excitation/inhibition imbalance and/or disrupted circuit maturation → clinical seizures **and, in parallel, independently** → impaired synaptic plasticity/neurodevelopment → intellectual disability/developmental regression (the "two-hit," partially seizure-independent model that distinguishes DEE nosologically from simple "epilepsy with comorbid ID").

**Suggested GO terms:** GO:0034765 (regulation of ion transmembrane transport), GO:0007268 (chemical synaptic transmission), GO:0051966 (regulation of synaptic transmission, glutamatergic), GO:0032228 (regulation of synaptic transmission, GABAergic), GO:0016082 (synaptic vesicle priming), GO:0007399 (nervous system development).
**Suggested CL terms:** CL:0000617 (GABAergic interneuron), CL:0002608 (GABAergic neuron), CL:0000679 (glutamatergic neuron), CL:0000598 (pyramidal neuron), CL:0000359 (vasoinhibitory... [n/a]) — specifically CL:0002608 and CL:0000617 for interneuron-selective mechanisms (SCN1A), and CL:0000679/CL:0000598 for excitatory-neuron-predominant mechanisms (SCN2A/SCN8A gain-of-function).

**Molecular profiling / advanced technologies:** iPSC-derived neuron models are increasingly used to directly compare gain- vs. loss-of-function electrophysiological phenotypes at the patient-variant level (e.g., SCN2A iPSC-neuron studies distinguishing GOF vs. LOF firing patterns — [bioRxiv 2023.02.14.528217](https://www.biorxiv.org/content/10.1101/2023.02.14.528217.full.pdf)); single-cell and circuit-level mouse studies (e.g., early postnatal CA3 hippocampal hyperexcitability in SCN2A-DEE mouse models — [bioRxiv 2025.06.29.661458](https://www.biorxiv.org/content/10.1101/2025.06.29.661458.full.pdf)) are elucidating developmental-stage-specific circuit mechanisms.

---

## 7. Anatomical Structures Affected

- **Organ level:** primary organ is the **brain/CNS** (UBERON:0000955). Secondary/systemic involvement is largely a consequence of severe neurological disease: gastrointestinal (feeding difficulties, gastroesophageal reflux — often requiring gastrostomy), musculoskeletal (scoliosis from hypotonia/immobility), respiratory (aspiration pneumonia, a leading non-SUDEP cause of death), and cardiac (some genes, e.g., SCN1A/SCN8A/SCN1B, implicate cardiac Na⁺ channel cross-reactivity as a plausible SUDEP mechanism given shared channel biology).
- **Body systems:** primarily nervous system; secondarily digestive, respiratory, musculoskeletal, and in movement-disorder-associated genes (GNAO1, ARX), the basal ganglia motor system.
- **Tissue/cell level:** cerebral cortex (particularly interneuron populations, UBERON:0000956), hippocampus (UBERON:0002421 — a key epileptogenic focus in Dravet and SCN2A models), and thalamocortical circuits. Cell populations: GABAergic interneurons (CL:0000617/CL:0002608 — Nav1.1-dependent), glutamatergic pyramidal neurons (CL:0000598), and to a lesser extent astrocytes (documented astrocyte remodeling in Dravet mouse models — see model organism section).
- **Subcellular level:** plasma membrane ion channels and channel complexes (GO:0034705 ion channel complex), presynaptic active zone/SNARE machinery (relevant to STXBP1), postsynaptic density/NMDA and GABA-A receptor complexes.
- **Localization (UBERON):** cerebral cortex (UBERON:0000956), hippocampus (UBERON:0002421), basal ganglia (UBERON:0002420, relevant to GNAO1), and more diffusely, whole brain (UBERON:0000955) given the typically generalized/multifocal nature of most genetic DEEs (contrasted with focal structural epilepsies).
- **Lateralization:** typically **bilateral/generalized** dysfunction, consistent with a diffuse channelopathy/synaptopathy mechanism rather than a focal lesion, though EEG can show multifocal or shifting focal features (especially in KCNQ2-DEE and EIMFS-type presentations).

---

## 8. Temporal Development

- **Onset:** ranges from **neonatal** (first days–weeks of life: KCNQ2, STXBP1, SCN2A/SCN8A-GOF, GNAO1, GRIN1) through **early infantile** (weeks–months: SCN1A/Dravet syndrome, typically 5–8 months; CDKL5, typically <4 months) to **later infancy/early childhood** (PCDH19, typically 6–36 months). Onset pattern is usually **acute/subacute** at the seizure level but the developmental impairment component can be **insidious**, sometimes preceding recognized seizures.
- **Progression:** Disease "stages" are not formally codified in oncology-style staging systems but are conventionally described by **evolving electroclinical syndrome** — e.g., a Ohtahara-syndrome-like (burst-suppression) neonatal presentation evolving into West-syndrome-like infantile spasms/hypsarrhythmia, which may further evolve into a Lennox-Gastaut-syndrome-like multi-seizure-type pattern in later childhood — the so-called "epileptic encephalopathy continuum" ([PubMed 35951482, "genetic heterogeneity to phenotypic continuum"](https://pubmed.ncbi.nlm.nih.gov/35951482/)). Progression rate is gene- and variant-dependent, ranging from rapidly severe (early-infantile SCN2A/SCN8A-GOF) to more indolent (later-onset, milder allelic series of the same genes).
- **Course pattern:** most genetic DEEs are **chronic and static-to-progressive** rather than truly relapsing-remitting, though PCDH19 and Dravet syndrome show a distinctive **episodic/clustering** seizure pattern layered on a chronic developmental trajectory. A notable and clinically important pattern (well documented in KCNQ2-DEE) is **seizure remission with persistent cognitive impairment** — i.e., seizure control does not track with developmental outcome, a defining conceptual feature separating "epileptic" from "developmental" components of DEE.
- **Remission:** spontaneous partial seizure remission is well described in KCNQ2-DEE (~73% eventual seizure freedom) and in some PCDH19 cases (seizure clusters typically diminish in adolescence); developmental impairment is far less likely to remit.
- **Critical periods:** the first 1–2 years of life are widely regarded as a critical developmental window where uncontrolled seizure activity may compound genetically-driven synaptic/circuit disruption — the rationale underlying "time is brain" arguments for rapid genetic diagnosis and early precision-guided treatment.

---

## 9. Inheritance and Population

**Epidemiology.** A large, prospective, population-based cohort (Scottish national cohort) found DEE incidence of **169 per 100,000 live births (≈1 in 590)**, with a point prevalence of **112 per 100,000 children** ([PMC10065214 / PMID:36581463, "Epidemiology of Developmental and Epileptic Encephalopathy and of Intellectual Disability and Epilepsy in Children"](https://pmc.ncbi.nlm.nih.gov/articles/PMC10065214/)). Related cohort work reports the adjusted incidence of epilepsies presenting in the first 3 years of life at **239 per 100,000 live births**, early-infantile DEE (onset <3 months) at **~10/100,000 live births**, infantile epileptic spasms syndrome at **58.2/100,000 (≈1 in 1,700)**, and early myoclonic-atypical-spasms-type presentations at **16.4/100,000 (≈1 in 6,100)**. SCN1A/Dravet syndrome alone has an expected population frequency of **≥1:20,000**.

**Inheritance pattern:** overwhelmingly **autosomal dominant, de novo** for the most common genes (SCN1A, STXBP1, SCN2A, KCNQ2, SCN8A, GNAO1, GRIN2B); **X-linked** for CDKL5, PCDH19, ARX, FOXG1 (with PCDH19 uniquely affecting heterozygous females and sparing hemizygous males via cellular interference); rare **autosomal recessive** forms exist for a subset of genes (e.g., some metabolic/glycosylation-pathway DEE genes and occasional biallelic presentations).

**Penetrance:** generally **high/complete** for the classic de novo dominant channelopathy genes, though variable expressivity is substantial (e.g., the SCN2A GOF-vs-LOF spectrum, and mild/attenuated allelic KCNQ2 phenotypes). **PCDH19 shows unusual, mosaicism-dependent penetrance** — affected heterozygous females vs. unaffected hemizygous male carriers.

**Expressivity:** highly variable, both within a gene (allelic series, e.g., SCN2A/SCN8A/KCNQ2 spanning benign familial neonatal epilepsy at the mild end to severe neonatal-onset DEE at the severe end) and even for identical or similar variants — supporting a role for genetic background/modifier effects.

**Genetic anticipation:** not a recognized feature of the major DEE genes (which are not repeat-expansion disorders); not applicable to this class as currently understood.

**Germline mosaicism:** documented and clinically important for recurrence-risk counseling — an apparently de novo variant in a proband carries a residual (several-percent) sibling recurrence risk due to unrecognized parental germline mosaicism, and is specifically well-described for SCN1A and other DEE genes.

**Founder effects:** not prominently described for most DEE genes (mutations arise recurrently de novo rather than being inherited from a founder population), though certain recurrent hotspot variants (e.g., specific KCNQ2 missense positions) recur across unrelated families due to mutational hotspot biology rather than shared ancestry.

**Consanguinity:** relevant primarily to the minority of autosomal recessive DEE genes; increases pretest probability for biallelic causes in consanguineous families.

**Carrier frequency:** not typically applicable to de novo dominant disease; relevant mainly for recessive DEE genes and for PCDH19 male carriers (who are unaffected transmitters).

**Population demographics:** No strong, well-replicated ethnic/geographic enrichment has been established for the major genetic DEEs as a class (contrast with some single-gene metabolic disorders); ascertainment is affected by access to genetic testing, so reported incidence is likely an underestimate in regions with limited NGS access. **Sex ratio** is roughly equal for autosomal dominant genes but strongly skewed by X-linked genes (CDKL5 and PCDH19 predominantly affect females; ARX/FOXG1-related phenotypes show sex-specific presentations). **Age distribution** is concentrated in infancy/early childhood at diagnosis, with increasing recognition of an adult DEE population as the first generation of genetically diagnosed infants ages into adulthood.

---

## 10. Diagnostics

**Clinical/EEG tests:** interictal and ictal EEG (burst-suppression pattern, hypsarrhythmia, multifocal epileptiform discharges), video-EEG for seizure semiology characterization, brain MRI (to exclude structural causes and to identify secondary structural changes such as diffuse atrophy), and in selected cases, metabolic screening (plasma amino acids, urine organic acids, CSF neurotransmitters, biotinidase, pyridoxine/pyridoxal-5-phosphate trial) to exclude treatable metabolic DEE mimics (a critical step before committing to a purely "genetic, non-treatable-metabolic" workup).

**Genetic testing.** Current consensus favors **early, first-line genome-wide sequencing** (WES or WGS, often as a rapid trio test) over sequential single-gene or small panel testing, given the extreme genetic heterogeneity (>900 genes):
- **WES as first-line** has been directly studied and validated as an efficient first-tier test in DEE cohorts, with diagnostic yields commonly cited around **35–43%** ([PMC10816140, "Whole Exome Sequencing as a First-Line Molecular Genetic Test in DEE"](https://pmc.ncbi.nlm.nih.gov/articles/PMC10816140/); [PubMed 35701389](https://pubmed.ncbi.nlm.nih.gov/35701389/)).
- **Targeted gene panels** remain in use where WES/WGS access is limited, with lower diagnostic yield in comparative studies (e.g., ~22% panel vs. higher WES yield in a Turkish cohort — [PMC12562696](https://pmc.ncbi.nlm.nih.gov/articles/PMC12562696/)); panels risk missing genes not yet included and non-coding/structural variants.
- **Chromosomal microarray (CMA)** remains indicated to detect CNVs not well captured by exome sequencing, particularly for genes like CDKL5/ARX in the Xp22 region.
- **Trio sequencing** (proband + both parents) substantially improves variant interpretation by enabling direct de novo confirmation, which is often the single strongest piece of evidence for pathogenicity in this de novo-dominant-predominant disease class.
- **RNA sequencing / functional follow-up** is increasingly used to resolve splicing VUS.
- **Mitochondrial DNA and repeat-expansion testing** are reserved for specific clinical phenotype overlaps (mitochondrial DEE mimics, and repeat-expansion disorders are not typically part of the core genetic DEE gene set).

**Clinical diagnostic criteria:** the ILAE 2022 operational framework for diagnosing DEE requires (1) epilepsy (recurrent unprovoked seizures) plus (2) developmental impairment attributable to the epilepsy/epileptiform activity and/or the underlying etiology, assessed against age-appropriate developmental milestones, with an "operational definition" recently published to standardize trial-eligibility criteria ([PMC11997937, Epilepsia 2025, "Operational definition of developmental and epileptic encephalopathies to underpin the design of therapeutic trials"](https://pmc.ncbi.nlm.nih.gov/articles/PMC11997937/)).

**Differential diagnosis:** structural epilepsies (cortical malformations, HIE), metabolic/treatable epileptic encephalopathies (pyridoxine-dependent epilepsy, GLUT1 deficiency, biotinidase deficiency, non-ketotic hyperglycinemia, creatine deficiency syndromes — all of which must be excluded/treated specifically since they are potentially reversible), mitochondrial disorders, and chromosomal syndromes with epilepsy as a feature.

**Screening:** no population newborn-screening program currently exists for genetic DEE (unlike some single-gene metabolic disorders); rapid genomic sequencing in the NICU/PICU setting for infants presenting with early-life refractory seizures functions as a de facto early-detection strategy. Cascade/carrier screening is relevant mainly for the recessive and X-linked forms.

---

## 11. Outcome/Prognosis

**Mortality:** genetic DEEs carry markedly elevated premature mortality. A large cohort study of people with genetic DEEs reported **42/510 deaths (8%)**, a mortality rate of **6.1 per 1,000 person-years**, of which **SUDEP accounted for 19/42 deaths (48%)** — the leading identifiable cause ([Neurology 2023, "Rates of Status Epilepticus and Sudden Unexplained Death in Epilepsy in People With Genetic Developmental and Epileptic Encephalopathies," PMC10115508](https://pmc.ncbi.nlm.nih.gov/articles/PMC10115508/)). A meta-analysis of randomized trial/extension-study populations estimated an overall SUDEP rate of **~4.3 per 1,000 person-years** and overall mortality of **~8.8 per 1,000 person-years** across DEE trial cohorts, with SUDEP risk highest in Dravet syndrome and comparatively lower (but still substantial) in Lennox-Gastaut syndrome and infantile epileptic spasms syndrome ([Epilepsia 2025 meta-analysis, "SUDEP and mortality in developmental and epileptic encephalopathies"](https://onlinelibrary.wiley.com/doi/10.1002/epi.70348)). For Dravet syndrome specifically, mortality is reported at **15–20%**, with 73% of deaths before age 10 and ~93% before age 20; SUDEP accounts for ~49% of Dravet deaths. Non-SUDEP causes of death include **status epilepticus, aspiration pneumonia, and seizure-related accidental injury/drowning**. Early mortality is also specifically documented in **STXBP1-related disorders** ([PMC11828786](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11828786/)).

**Morbidity/function:** the majority of survivors have lifelong, severe intellectual disability, motor impairment, and behavioral/psychiatric comorbidity (autism, ADHD, anxiety) as described in the Phenotypes section; functional independence in adulthood is rare for the most severe gene-associated forms (CDKL5, STXBP1, early-infantile SCN2A/SCN8A-GOF), while some milder allelic variants (later-onset KCNQ2, some PCDH19) permit partial functional independence.

**Complications:** status epilepticus, aspiration pneumonia (a leading non-SUDEP cause of death), fractures/injury from seizures or falls, scoliosis, feeding/nutritional failure requiring gastrostomy, and psychiatric comorbidity requiring dedicated management.

**Prognostic factors:** earlier seizure onset is generally associated with worse cognitive outcome (documented specifically in PCDH19, where early onset correlates with disease severity); the specific causal gene and variant type (gain- vs loss-of-function) strongly predicts both seizure course and treatment responsiveness; achievement of early seizure control is associated with (though not fully protective against) better developmental trajectory.

---

## 12. Treatment

**Pharmacotherapy — general antiseizure medications (ASMs):** broad-spectrum ASMs (valproate, clobazam, topiramate, levetiracetam, lamotrigine, rufinamide, felbamate, lacosamide, vigabatrin) are used empirically, often in combination, given high rates of pharmacoresistance. **Critical gene-specific contraindication:** sodium-channel-blocking ASMs (phenytoin, carbamazepine, oxcarbazepine, lamotrigine at high dose) can **worsen** seizures in SCN1A loss-of-function Dravet syndrome and are generally avoided, while the same drug class can be **beneficial** in SCN2A/SCN8A gain-of-function DEE — a textbook example of genotype-guided precision prescribing in this disease class.

**Recently approved/DEE-specific pharmacotherapies:**
- **Stiripentol** — potentiates GABAergic transmission; approved as adjunct for Dravet syndrome.
- **Cannabidiol (Epidiolex)** — FDA/EMA-approved for Dravet syndrome and Lennox-Gastaut syndrome.
- **Fenfluramine** — serotonergic/sigma-1-receptor agonist mechanism; approved for Dravet syndrome and, more recently, CDKL5 deficiency disorder and Lennox-Gastaut syndrome.
All three are highlighted as effective, well-tolerated additions to the DEE armamentarium ([tandfonline review; DelveInsight pipeline overview](https://www.delveinsight.com/blog/developmental-and-epileptic-encephalopathy-pipeline-therapies)).
- **ACTH/oral corticosteroids** — mainstay for infantile-spasms-type presentations regardless of underlying gene.

**Pharmacogenomics:** the SCN1A/SCN2A/SCN8A gain-of-function vs. loss-of-function dichotomy described above is the clearest example of pharmacogenomic decision-making currently in DEE clinical practice; **cenobamate** has recently been explored as an add-on for SCN8A-DEE specifically ([medRxiv 2024.10.17.24312949](https://www.medrxiv.org/content/10.1101/2024.10.17.24312949.full.pdf)).

**Advanced therapeutics (investigational/emerging):**
- **Antisense oligonucleotide (ASO) therapy:** an SCN1A-upregulating ASO strategy (targeting a non-productive splice isoform to boost productive SCN1A transcript and restore Nav1.1 haploinsufficiency) has entered clinical development for Dravet syndrome; conversely, an SCN2A-lowering ASO strategy has been studied preclinically for SCN2A gain-of-function DEE ([bioRxiv 2020.09.09.289900, "Antisense oligonucleotide therapy for SCN2A gain-of-function epilepsy"](https://www.biorxiv.org/content/10.1101/2020.09.09.289900.full.pdf)).
- **Gene therapy:** AAV-mediated gene-replacement/upregulation strategies are in preclinical-to-early-clinical development for Dravet syndrome (SCN1A upregulation via engineered transcription factors) and other haploinsufficiency genes (e.g., STXBP1, SCN1A).
- **Base editing:** an adenine base editor packaged in dual AAVs (SCN8A-ABE) corrected a gain-of-function SCN8A variant and significantly increased survival and reduced/eliminated seizures in a mouse model, illustrating a genome-editing path toward curative therapy ([PMC12871382](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12871382/)).

**Surgical/interventional:** vagus nerve stimulation (VNS) is used in selected drug-resistant DEE patients, including gene-specific case reports (e.g., KCNB1-DEE — [PMC12446608](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12446608/)) and studied in young children specifically ([PMC10624125](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10624125/)); corpus callosotomy for drop attacks; focal resective surgery is rarely applicable given the typically diffuse/genetic (non-focal-lesional) substrate, but may be considered when a coexisting focal structural abnormality (e.g., focal cortical dysplasia) is identified.

**Supportive/rehabilitative care:** ketogenic diet has demonstrated efficacy across multiple DEE subtypes and is a well-established non-pharmacological cornerstone ([PMC12358386, "Progress of ketogenic diet in the treatment of developmental epileptic encephalopathy"](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12358386/)); physical/occupational/speech therapy, nutritional support (including gastrostomy), and multidisciplinary developmental support are standard.

**Suggested MAXO terms:** MAXO:0000647 (chemotherapy — n/a here), MAXO:0000088 (dietary intervention — ketogenic diet), MAXO:0000011 (physical therapy), MAXO:0001017 (vaccination — n/a), MAXO:0000004 (surgical procedure — VNS/callosotomy), MAXO:0001001 (gene therapy), MAXO:0000950 (supportive care). Pharmacotherapy entries would use NCIT:C15986 (Pharmacotherapy) with `therapeutic_agent` bound to CHEBI (e.g., cannabidiol, stiripentol, fenfluramine) or NCIT drug-class terms.

**Treatment outcomes:** response rates vary widely by gene and drug; adverse events for the newer agents include appetite/weight changes and cardiac monitoring requirements for fenfluramine (historical cardiac-valvulopathy concerns from its earlier obesity-drug formulation, now mitigated by low-dose, monitored DEE use), sedation for cannabidiol/clobazam combinations, and hepatotoxicity monitoring for valproate/stiripentol/felbamate combinations.

---

## 13. Prevention

**Primary prevention:** not currently possible in the traditional sense (no way to prevent de novo mutation occurrence); the closest analog is **avoidance of known seizure triggers** (fever management, sleep hygiene) in already-diagnosed patients to reduce secondary seizure-related morbidity, and **avoidance of contraindicated sodium-channel-blocking ASMs** in SCN1A-Dravet syndrome to prevent iatrogenic seizure worsening.

**Secondary prevention:** early genetic diagnosis enabling gene-informed ASM selection (the sodium-channel-blocker example above) functions as a form of secondary prevention of avoidable seizure exacerbation and status epilepticus.

**Genetic counseling:** central to management — recurrence-risk counseling for parents (typically low but non-zero due to germline mosaicism, as discussed above), and reproductive options (preimplantation genetic diagnosis, prenatal testing) once a familial pathogenic variant is identified.

**Screening/early detection:** no population-level newborn screening program exists for genetic DEE; rapid/ultra-rapid genomic sequencing for critically ill infants with early-life seizures functions as the practical "early detection" pathway, enabling faster gene-informed management.

**Prophylaxis:** SUDEP-risk-reduction counseling (nocturnal supervision/monitoring devices, seizure-alert systems, optimized seizure control) is a key preventive intervention given the high SUDEP burden documented above; some centers discuss rescue-medication protocols (e.g., benzodiazepine rescue therapy) as prophylaxis against prolonged seizures/status epilepticus.

---

## 14. Other Species / Natural Disease

Naturally occurring DEE-like disease in companion animals is not well characterized as a direct ortholog of any single human genetic DEE (unlike, e.g., some canine epilepsy loci); OMIA does list canine idiopathic epilepsy loci, but a documented natural-disease parallel specific to SCN1A/STXBP1/etc. orthologs in domestic species was not identified in this search pass. **Orthologous genes** are highly conserved across vertebrates (Scn1a, Stxbp1, Scn2a, Kcnq2, Cdkl5, Pcdh19, Gnao1, Arx all have well-annotated mouse, rat, and zebrafish orthologs per NCBI Gene/Alliance of Genome Resources), which underpins the extensive model-organism literature below. No zoonotic or cross-species transmission relevance applies, as this is a non-infectious monogenic disease class.

---

## 15. Model Organisms

Model systems are extensively used and are reviewed comparatively in [PMC8547712, "Overlaps, gaps, and complexities of mouse models of Developmental and Epileptic Encephalopathy"](https://pmc.ncbi.nlm.nih.gov/articles/PMC8547712/).

**Mouse models:**
- **Scn1a⁺/⁻ (Dravet syndrome) mice** — the best-characterized DEE model; recapitulate spontaneous seizures, premature/SUDEP-like mortality, hyperactivity, social-interaction deficits, and cognitive impairment beginning around the second–third postnatal week, closely paralleling the human Nav1.1-interneuron-hypoexcitability mechanism. Genetic-rescue studies (Scn1a reactivation after symptom onset) have shown reversal of pathological phenotypes, supporting gene-therapy feasibility ([Nature Communications 2021, PMID via doi:10.1038/s41467-021-27837-w](https://www.nature.com/articles/s41467-021-27837-w)). Astrocyte remodeling has also been documented as a longer-lasting pathological feature in this model ([bioRxiv 2026.01.06.697745](https://www.biorxiv.org/content/10.64898/2026.01.06.697745.full.pdf)).
- **Scn2a knock-in mice** (e.g., p.A263V gain-of-function variant knocked into the endogenous locus) — show increased persistent Na⁺ current in heterologous expression and spontaneous generalized tonic-clonic seizures in vivo, confirming gain-of-function mechanism and enabling early postnatal circuit-level study of CA3 hippocampal hyperexcitability ([bioRxiv 2025.06.29.661458](https://www.biorxiv.org/content/10.1101/2025.06.29.661458.full.pdf)). A separate Scn2a knockout (haploinsufficiency) model shows an autistic-like phenotype attenuated with age, modeling the loss-of-function end of the SCN2A allelic spectrum ([PMC6733925](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6733925/)).
- **Scn1b (Na⁺ channel β1 subunit) mice** — model human SCN1B-linked DEE, reproducing both epilepsy and SUDEP ([PMC10903178](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10903178/)).
- **Scn8a mutation-associated models** — used to test base-editing correction (SCN8A-ABE), with AAV-delivered adenine base editing improving survival and reducing/eliminating seizures ([PMC12871382](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12871382/)).
- **Gabrg2 knock-in mice** — model GABRG2-related epileptic encephalopathy, showing spontaneous generalized seizures and cognitive impairment, directly linking GABA-A receptor dysfunction to the DEE phenotype ([PMC12501280](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12501280/)).

**iPSC-derived neuron / cellular models:** patient-derived iPSC neurons carrying gain-of-function vs. loss-of-function SCN2A variants show **distinctive, mechanism-concordant electrophysiological phenotypes** in vitro, supporting the model's utility for genotype-specific mechanism dissection and drug screening ([bioRxiv 2023.02.14.528217](https://www.biorxiv.org/content/10.1101/2023.02.14.528217.full.pdf)).

**Model characteristics/limitations:** mouse models generally recapitulate core seizure phenotypes and premature mortality well, and increasingly reproduce behavioral/cognitive comorbidities, but the PMC8547712 review specifically emphasizes **gaps and overlaps** — i.e., not all mouse models fully capture the human developmental-regression component, genetic background strongly modifies phenotype severity/penetrance (complicating cross-model comparison), and species differences in interneuron subtype proportions and network architecture limit direct translational inference for cognitive/behavioral endpoints. iPSC-neuron models, while capturing cell-autonomous electrophysiology well, lack the multicellular network and whole-organism developmental context needed to model the "developmental" component of DEE.

**Applications:** these models are used for (1) mechanistic dissection (channelopathy vs. synaptopathy, GOF vs. LOF), (2) precision-therapy validation (genotype-matched sodium-channel-blocker response), and (3) advanced-therapeutic proof-of-concept (ASO, gene therapy, base editing) prior to human trials, as detailed in the Treatment section above.

**Resources:** MGI (Mouse Genome Informatics) for Scn1a/Scn2a/Stxbp1/Kcnq2/Cdkl5 alleles; IMPC/KOMP for systematic knockout phenotyping; ZFIN for zebrafish scn1lab Dravet models (an additional model system not detailed above but widely used for high-throughput drug screening in Dravet syndrome).

---

## Summary of Key Ontology-Term Suggestions for KB Curation

- **MONDO:** MONDO:0010246 (umbrella "developmental and epileptic encephalopathy" grouping term, OMIM PS308350) plus individual gene-specific MONDO IDs per subtype.
- **HP terms:** HP:0032900 (Seizure), HP:0011097 (Epileptic spasm), HP:0001263 (Developmental delay), HP:0002376 (Developmental regression), HP:0001249 (Intellectual disability), HP:0010851 (EEG with burst suppression), HP:0000729 (Autistic behavior), HP:0004328 (Hand stereotypies), HP:0010984 (Digenic inheritance — n/a here but relevant framework), HP:0001252 (Hypotonia).
- **GO terms:** GO:0034765, GO:0007268, GO:0051966, GO:0032228, GO:0016082, GO:0007399.
- **CL terms:** CL:0000617, CL:0002608 (GABAergic interneuron), CL:0000679, CL:0000598 (glutamatergic/pyramidal neuron).
- **UBERON terms:** UBERON:0000955 (brain), UBERON:0000956 (cerebral cortex), UBERON:0002421 (hippocampus), UBERON:0002420 (basal ganglia).
- **MAXO terms:** MAXO:0000088 (dietary/ketogenic diet), MAXO:0000011 (physical therapy), MAXO:0000004 (surgical procedure — VNS), MAXO:0001001 (gene therapy).
- **CHEBI terms (representative drugs):** cannabidiol, fenfluramine, stiripentol, valproate, clobazam.

---

## Curation Note on Scope

Given dismech's schema conventions, "Genetic Developmental and Epileptic Encephalopathy" is best modeled either as (a) an umbrella **Grouping** (analogous to `Mucopolysaccharidoses` or `Digenic_and_Oligogenic_Disorders`) with `grouping_basis: SHARED_MECHANISM`/`SHARED_PHENOTYPE` pointing down to individual gene-defined member entries (SCN1A-Dravet syndrome, STXBP1-DEE, SCN2A-DEE, KCNQ2-DEE, CDKL5 deficiency disorder, PCDH19-clustering epilepsy, etc. — several of which likely already exist or should be created as standalone `Disease` entries), each conforming to the existing `epilepsy_excitation_inhibition_imbalance` mechanism module for the shared excitation/inhibition-imbalance convergence point; or (b) if the KB intends a single entry for the umbrella concept itself, it should be scoped narrowly to the shared definitional/diagnostic/epidemiological content above, with gene-specific pathophysiology, evidence, and precision-therapy detail deferred to the individual gene-level entries — consistent with the "lump vs. split" design guidance in this repository's decision register.