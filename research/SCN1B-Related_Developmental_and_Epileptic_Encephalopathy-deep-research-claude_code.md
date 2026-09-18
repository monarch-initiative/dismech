---
provider: claude_code
model: claude-haiku-4-5-20251001, claude-sonnet-5
cached: false
start_time: '2026-08-19T13:21:02.728002'
end_time: '2026-08-19T13:25:33.319705'
duration_seconds: 270.59
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: SCN1B-Related Developmental and Epileptic Encephalopathy
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
  num_turns: 20
  total_cost_usd: 1.8953504999999995
  session_id: 6f8bf895-3ab0-55cb-a154-acb932b43f03
  stop_reason: end_turn
  assistant_text_blocks: 2
citation_count: 22
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 16
  on_topic: 14
  validator_version: 0.2.1
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SCN1B-Related Developmental and Epileptic Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **SCN1B-Related Developmental and Epileptic Encephalopathy** covering all of the
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

I'll research SCN1B-Related Developmental and Epileptic Encephalopathy now, using web search to verify facts and gather citations.

I now have comprehensive, well-sourced material. Compiling the full research report.

# SCN1B-Related Developmental and Epileptic Encephalopathy: Comprehensive Research Report

## 1. Disease Information

**Overview:** SCN1B-related Developmental and Epileptic Encephalopathy (referred to in OMIM as Developmental and Epileptic Encephalopathy 52, "DEE52") is a rare, autosomal recessive, severe infantile-onset epilepsy syndrome caused by biallelic (homozygous or compound heterozygous) loss-of-function variants in *SCN1B*, the gene encoding the voltage-gated sodium channel β1/β1B non-pore-forming subunits. Affected infants present with refractory seizures beginning in the first months of life, global developmental delay/regression, hypotonia, and a high risk of premature death, including sudden unexpected death in epilepsy (SUDEP). Clinically, the phenotype overlaps substantially with Dravet syndrome but is generally considered more severe, since developmental impairment can precede or accompany seizure onset rather than following a period of normal development, as in classic Dravet syndrome (PMID not directly given; Aeby et al. 2019, PMC6917350).

Distinctly, **heterozygous** *SCN1B* variants (the classic example being p.Cys121Trp/C121W) cause a much milder phenotype: **Genetic (Generalized) Epilepsy with Febrile Seizures Plus (GEFS+)**, historically labeled "GEFS+1" as the first sodium-channel-subunit gene linked to this syndrome (Wallace et al. 1998). *SCN1B* variants have also been separately implicated in cardiac arrhythmia syndromes, notably **Brugada syndrome**, reflecting the gene's dual expression in brain and heart.

**Key identifiers:**
- **Gene:** SCN1B (Sodium Voltage-Gated Channel Beta Subunit 1); **HGNC:10586**; **OMIM gene entry *600235**
- **DEE52 (biallelic/recessive form):** **OMIM #617350** — "DEVELOPMENTAL AND EPILEPTIC ENCEPHALOPATHY 52; DEE52"
- **GEFS+1 (heterozygous/dominant form):** OMIM #604233 (GEFS+ type 1)
- Suggested MONDO term: a MONDO ID mapping to OMIM:617350 (DEE52) should be confirmed via MONDO lookup at curation time, as it was not independently verified in this research pass
- **Chromosomal location:** 19q13.11–q13.12
- **Synonyms:** SCN1B-related epileptic encephalopathy; Early Infantile Epileptic Encephalopathy 52 (EIEE52, older nomenclature); Dravet syndrome, SCN1B-related; DEE52

**Evidence base:** Information is derived from aggregated case reports and case series (fewer than a dozen families reported worldwide as of the most recent literature — Aeby et al. 2019 note this was only the "eighth reported SCN1B patient" with biallelic disease), supplemented by extensive mechanistic and mouse-model studies rather than large-cohort epidemiological/EHR data given the extreme rarity of the disorder.

## 2. Etiology

**Disease causal factors:** DEE52 is a monogenic, purely genetic disorder. It is caused by **biallelic (homozygous or compound heterozygous) loss-of-function variants in SCN1B**, most reported cases arising in the setting of parental **consanguinity** (Patino et al. 2009, PMID:19710327; Aeby et al. 2019; Muhammad et al. 2026, consanguineous Pakistani family). No environmental or infectious causal factor is implicated in the primary genetic lesion, though **fever/hyperthermia** is a major seizure trigger/exacerbating factor once the genetic predisposition is present (paralleling Dravet syndrome biology).

**Genetic risk factors:**
- Homozygous or compound heterozygous **SCN1B loss-of-function variants**: missense (e.g., p.Arg125Cys/R125C, p.Arg85Cys/R85C, p.Arg89Cys/R89C, p.Tyr119Asp/Y119D), splice-site variants, and presumed protein-truncating variants
- Consanguinity substantially raises risk given the autosomal recessive inheritance
- By contrast, **heterozygous** SCN1B missense variants (e.g., C121W) are risk factors for the distinct, milder GEFS+ phenotype via a dominant, gain-of-function-like mechanism, and for Brugada syndrome (Watanabe et al. 2008, Scientific Reports 2014 study of 145 SCN5A-negative Brugada patients)

**Environmental risk factors/triggers:** Fever, vaccination-associated fever (reported as a seizure trigger in the R125C case; Patino et al. 2009), transitions in sleep state, and hot baths are reported precipitants of seizure exacerbation/status epilepticus (Aeby et al. 2019).

**Protective factors:** None specifically documented for SCN1B-DEE52 in the literature reviewed. In the general Dravet-spectrum literature, avoidance of hyperthermia and of sodium-channel-blocking antiepileptics is considered protective against exacerbation (see Treatment, Section 12).

**Gene-environment interactions:** The primary interaction is genotype (loss-of-function SCN1B) × fever/hyperthermia, which precipitates status epilepticus and is mechanistically explained by impaired β1-mediated modulation of Nav1.1 current density/inactivation kinetics being further destabilized by temperature-sensitive channel gating — directly modeled in Scn1b-null and Scn1b-c.265C>T knock-in mice, which show hyperthermia-induced generalized seizures (PMID:40763036).

## 3. Phenotypes

### Neurological/seizure phenotypes
- **Seizure onset:** Early infantile, typically 2.5–6 months of age (OMIM #617350 clinical synopsis: onset at or before age 6 months)
- **Seizure types:** Multifocal myoclonus, focal (hemiclonic) seizures, generalized tonic-clonic seizures, myoclonic and hemiclonic **status epilepticus** (up to 8 episodes in the first 2 years in one patient; Aeby et al. 2019), fever-triggered convulsions occurring several times weekly in another patient (Patino et al. 2009)
- **EEG findings:** Frequent bilateral central spikes occurring in bursts with high-voltage slow waves (Aeby et al. 2019)
- **Refractoriness:** Seizures refractory to multiple standard antiepileptic drugs (valproic acid, clobazam, clonazepam, phenytoin reported ineffective; Patino et al. 2009)
- **Developmental impairment:** Severe global developmental delay/psychomotor stagnation or regression; in the Aeby case, the patient was unable to hold her head up at age 5 despite social interactivity
- **Tone/motor abnormalities:** Global/axial hypotonia from birth, appendicular spasticity, tetrapyramidal syndrome
- **Microcephaly:** Reported in the OMIM clinical synopsis
- **Brain imaging:** Nonspecific brain atrophy reported on neuroimaging (OMIM #617350)
- **Ataxia:** Demonstrated mechanistically in Scn1b-null mice via cerebellar Purkinje cell hypoexcitability (Yuan et al. 2025, PMID:40923316) — a plausible human correlate given cerebellar Scn1b expression, though this specific phenotype is best documented in the mouse model rather than confirmed human cases at time of writing

### Sensory phenotypes
- **Bilateral sensorineural hearing loss** (~50 dB threshold), with brainstem auditory pathway involvement demonstrated by wave V loss at lower stimulus intensities (Aeby et al. 2019) — HP:0000407 (Sensorineural hearing impairment)

### Cardiac phenotypes (emerging)
- Altered cardiac excitability and arrhythmia susceptibility, demonstrated in both Scn1b-c.265C>T knock-in mice and patient-derived iPSC-cardiomyocytes (2025 JCI Insight paper, PMID:40763036) — mechanistically linking SCN1B-DEE52 to elevated SUDEP risk via a dual neuro-cardiac mechanism, analogous to findings in Dravet syndrome/SCN1A more broadly

### Mortality
- **Premature death** occurred in 4 of 9 patients in the original OMIM-cited cohort, at ages ranging from 7 months to 5 years (OMIM #617350)
- Death from **respiratory insufficiency secondary to aspiration pneumonia** reported at 13 months in the R125C patient (Patino et al. 2009)
- High risk of **SUDEP**, consistent across multiple case reports and modeled directly in mice

### Suggested HPO terms
- HP:0011097 (Epileptic encephalopathy) / HP:0002133 (Status epilepticus)
- HP:0002123 (Generalized myoclonic seizures) / HP:0032792 (Motor seizure) / HP:0011159 (Generalized tonic-clonic seizure)
- HP:0002071 (Abnormality of extrapyramidal motor function) / HP:0001252 (Hypotonia) / HP:0001257 (Spasticity)
- HP:0000252 (Microcephaly)
- HP:0007359 (Focal-onset seizure)
- HP:0011451 (Fever-induced seizures) — captures the hyperthermia-triggering phenomenon
- HP:0001511 (Intrauterine/global developmental delay) → HP:0011344 (Severe global developmental delay) / HP:0002376 (Developmental regression)
- HP:0000407 (Sensorineural hearing impairment)
- HP:0002059 (Cerebral atrophy)
- HP:0001663 (Ventricular arrhythmia) / cardiac phenotype terms as emerging evidence matures

### Quality of life impact
Case series consistently report profound impact on daily functioning: total dependence for basic care, absence of independent ambulation or head control at age 5 in the most detailed reported case, and a substantial mortality burden in early childhood — collectively representing among the most severe ends of the DEE spectrum.

## 4. Genetic/Molecular Information

**Causal gene:** SCN1B (HGNC:10586; OMIM *600235), encoding two splice isoforms, β1 and β1B, non-pore-forming auxiliary subunits of voltage-gated sodium channels.

**Reported pathogenic biallelic variants (DEE52):**
| Variant (cDNA/protein) | Zygosity | Source |
|---|---|---|
| c.373C>T, p.Arg125Cys (R125C) | Homozygous | Patino et al. 2009, PMID:19710327 (Moroccan consanguineous family) |
| c.253C>T, p.Arg85Cys (R85C) | Homozygous | Aeby et al. 2019, PMC6917350 |
| c.265C>T, p.Arg89Cys (R89C) | Homozygous | 2025 cardiac excitability study, PMID:40763036 |
| p.Tyr119Asp (Y119D) | Homozygous | Referenced in OMIM #617350 family series |
| Homozygous splice-site variant | Homozygous | Referenced in OMIM #617350 family series; also a novel homozygous splice-site variant reported in a consanguineous Pakistani family (Muhammad et al., Mol Genet Genomic Med 2026) |

**Heterozygous variant causing GEFS+ (distinct phenotype):**
- **c.363T>G, p.Cys121Trp (C121W)** — the founding GEFS+ mutation (Wallace et al. 1998), disrupting a critical intramolecular disulfide bond in the extracellular β1 immunoglobulin (Ig) loop domain. Shown to be an ancient founder variant shared by ≥14 unrelated GEFS+ families across Australia/UK/US via a common ~260 kb ancestral haplotype persisting for roughly 800 years (Grinton et al. 2022). Penetrance estimated at ~70% (12/44 studied carriers asymptomatic).

**Variant classification (ACMG/AMP framework):** Recessive DEE52 variants are typically classified pathogenic/likely pathogenic based on: (1) absence/near-absence in population databases (gnomAD), (2) segregation with disease in consanguineous pedigrees, (3) functional evidence of loss of β1 modulatory function, and (4) recurrence across unrelated families at conserved residues in the extracellular Ig-loop domain (multiple independent Arg→Cys substitutions at Arg85, Arg89, Arg125 cluster in this domain).

**Functional consequences — mechanistically well-characterized loss of function:**
- **p.Arg125Cys**: Markedly reduced cell-surface trafficking despite normal total cellular protein expression — biotinylation assays showed only ~6.7% of wild-type β1 levels reaching the plasma membrane; the mutant failed to modulate sodium current properties when co-expressed with Nav1.1 in mammalian cells, consistent with a **functional null** allele (Patino et al. 2009, PMID:19710327)
- **p.Arg85Cys**: By contrast, this variant trafficks normally to the plasma membrane (confirmed via biotinylation and confocal colocalization with wheat germ agglutinin), yet still fails to confer the wild-type β1 effect of increasing transient/persistent Nav1.1 current density and accelerating fast inactivation kinetics — demonstrating that loss of function can occur **independent of trafficking defects**, via impaired protein-protein modulatory interaction with the α subunit (Aeby et al. 2019)
- Scala et al. 2021 (Epilepsia, PMID pending exact ID — study of 9 patients/4 families) further characterized multiple SCN1B DEE52 variants' effects on voltage-gated sodium channel function, reinforcing loss-of-function as the convergent mechanism across the allelic series
- By contrast, the **heterozygous C121W** GEFS+ variant produces a distinct **gain-of-function** effect in some assay systems ("β1-C121W Is Down But Not Out," Reid et al./Isom lab, J Neurosci 2016, PMID:27277800) — underscoring that dominant GEFS+ and recessive DEE52 variants, though both disrupting normal β1 structure/function, produce mechanistically and clinically distinct outcomes

**Modifier genes:** None specifically established for SCN1B-DEE52; by analogy to Dravet syndrome (SCN1A), genetic background may modulate severity, but this has not been directly studied for SCN1B.

**Epigenetic information:** Not established/reported for this disorder.

**Chromosomal abnormalities:** Not a recognized mechanism for this disorder — pathogenic variants are point mutations/small indels/splice variants rather than large structural rearrangements in the reported literature.

**Suggested gene/protein ontology terms:**
- Gene: hgnc:10586 (SCN1B)
- GO Molecular Function: voltage-gated sodium channel activity (GO:0005248); regulates ion channel activity
- GO Biological Process: regulation of sodium ion transmembrane transporter activity; regulation of action potential

## 5. Environmental Information

**Environmental factors:** No toxin, radiation, or occupational exposure is implicated as a primary cause. **Fever/hyperthermia** is the dominant environmental modulator of disease expression — precipitating status epilepticus in patients and directly reproduced in Scn1b-null and Scn1b-c.265C>T knock-in mice as hyperthermia-induced generalized seizures.

**Lifestyle factors:** Hot baths and sleep-state transitions are reported seizure triggers (Aeby et al. 2019); these parallel well-established Dravet syndrome trigger profiles.

**Infectious agents:** Not a direct cause; febrile infections act as nonspecific triggers of hyperthermia-related seizure exacerbation rather than being disease-causal. One case report notes seizure onset temporally associated with **post-vaccination fever** (Patino et al. 2009), reflecting the fever trigger rather than any vaccine-specific pathogenic mechanism.

**Suggested ECTO term:** exposure to elevated body temperature / febrile illness as a seizure trigger (specific ECTO CURIE to be confirmed at curation time).

## 6. Mechanism / Pathophysiology

**Causal chain summary:**
Biallelic SCN1B loss-of-function variant → loss of normal β1/β1B-mediated modulation of voltage-gated sodium channel α subunits (principally Nav1.1/SCN1A, also relevant to Nav1.6/SCN8A and cardiac Nav1.5/SCN5A) → failure to normally increase Na+ current density and to normally accelerate fast inactivation kinetics → altered excitability in specific neuronal populations (notably **GABAergic interneurons**, whose relative hypoexcitability is the presumptive substrate of Dravet-spectrum disinhibition, paralleling the SCN1A/Nav1.1 disease model) and **cerebellar Purkinje cells** → network hyperexcitability, hypersynchrony, and hyperthermia-sensitized seizure threshold → recurrent seizures, status epilepticus, and progressive/associated developmental encephalopathy; separately, altered cardiomyocyte excitability (β1 also regulates cardiac Na+, K+ currents and Ca2+ handling) → atrial/ventricular arrhythmia susceptibility → contributes to SUDEP risk via a dual neuro-cardiac mechanism.

**Molecular pathways/protein function:** β1/β1B are **non-pore-forming, single-transmembrane-domain auxiliary subunits** with an extracellular immunoglobulin (Ig)-like loop domain. Beyond channel gating modulation, β1 subunits function as **cell adhesion molecules** (interacting with contactin, neurofascin, ankyrin, tenascin) and participate in **regulated intramembrane proteolysis** (via BACE1 and γ-secretase cleavage) that generates an intracellular domain capable of influencing gene transcription — giving β1 a non-canonical signaling role beyond direct channel modulation (OMIM #600235 function summary; Frontiers 2018 review, PMC5924814).

**Cellular processes:** Altered neuronal excitability (excitatory/inhibitory imbalance); reported "excitatory and inhibitory neuron defects" in a Scn1b-linked EIEE52 mouse model (PMC7664274); cerebellar granule neuron and Purkinje cell pathfinding/excitability defects (Yuan et al. 2025); cardiomyocyte electrical remodeling and structural fibrosis (increased transient outward K+ current density and ventricular fibrosis reported in Scn1b-mutant mice).

**Tissue damage mechanisms:** Not a primary structural/degenerative disease mechanism; pathology is predominantly functional/electrophysiological (channelopathy) rather than driven by oxidative stress, ischemia, or classic fibrotic/necrotic injury, though secondary cardiac fibrosis has been reported in mouse models.

**Biochemical abnormality:** Core defect is an **ion channel auxiliary subunit deficiency/dysfunction** — impaired Na+ channel modulation (reduced peak/persistent current, altered inactivation kinetics) rather than a classical enzyme deficiency.

**Molecular profiling / advanced technologies:**
- **Model-organism transcriptomics**: Scn1b-null mice show altered *Scn1a* mRNA expression normalized toward wild-type levels upon AAV-mediated β1 gene replacement therapy (PMC11870736), suggesting a downstream transcriptional consequence of β1 loss on the primary Dravet gene itself
- **iPSC-cardiomyocyte modeling**: iPSC-CMs derived from SCN1B-c.265C>T DEE52 patients were used to directly assess human cardiac electrophysiological consequences of the disease genotype (PMID:40763036)
- **Single-cell/cell-type-specific mouse genetics**: Purkinje-cell-specific conditional Scn1b deletion mice recapitulate a DEE-like phenotype, isolating the cerebellar contribution to the disease (bioRxiv 2024.11.19.624370)

**Causal chain — upstream vs. downstream:**
1. **Upstream (molecular):** SCN1B biallelic LOF variant → loss of β1 protein function/trafficking
2. **Intermediate (cellular):** Impaired Nav channel modulation in interneurons, pyramidal neurons, Purkinje cells, and cardiomyocytes
3. **Downstream (tissue/organism):** Cortical/cerebellar network hyperexcitability + cardiac arrhythmia substrate
4. **Clinical:** Refractory epilepsy, status epilepticus, developmental encephalopathy, ataxia, cardiac arrhythmia, SUDEP

**Suggested GO terms:** GO:0086010 (membrane depolarization during action potential); GO:0035725 (sodium ion transmembrane transport); GO:0086002 (cardiac muscle cell action potential involved in contraction)
**Suggested CL terms:** CL:0000617 (GABAergic interneuron); CL:0000121 (Purkinje cell); CL:0000746 (cardiac muscle cell)

## 7. Anatomical Structures Affected

**Organ level:**
- **Primary:** Central nervous system (cerebral cortex, cerebellum, brainstem)
- **Secondary:** Cardiovascular system (increasingly recognized — atrial/ventricular arrhythmia substrate); auditory system (sensorineural hearing loss, likely brainstem auditory pathway); respiratory system (secondary complication — aspiration pneumonia leading to fatal respiratory insufficiency reported)
- **Body systems:** Nervous system (primary); cardiovascular system (emerging); ear/audiovestibular system

**Tissue/cell level:**
- Cerebral cortical pyramidal neurons and GABAergic interneurons (CL:0000598 pyramidal neuron; CL:0000617 GABAergic interneuron)
- Cerebellar Purkinje cells and granule neurons (CL:0000121 Purkinje cell; CL:0000120 granule cell)
- Cardiomyocytes (CL:0000746)
- Cochlear/brainstem auditory pathway neurons (implicated by ABR wave V findings)

**Subcellular level:** Plasma membrane (site of Nav channel complex and β1 trafficking; GO:0005886 plasma membrane); the Ig-loop extracellular domain of β1 mediates both channel modulation and cell-adhesion interactions at the membrane surface.

**Localization/UBERON suggestions:** UBERON:0000955 (brain); UBERON:0002037 (cerebellum); UBERON:0001851 (cortex); UBERON:0000948 (heart); UBERON:0001846 (auditory brainstem structures, or more specific brainstem term)

**Lateralization:** Bilateral involvement is typical (bilateral central EEG spikes; bilateral sensorineural hearing loss).

## 8. Temporal Development

**Onset:** Early infantile — typically 2.5 to 6 months of age; OMIM #617350 specifies onset "at or before age 6 months." Hypotonia may be present from birth, preceding overt seizure onset in some cases (Aeby et al. 2019), supporting an "encephalopathy" framing (developmental impairment intrinsic to the genotype) rather than purely "epileptic encephalopathy" (impairment secondary to seizures).

**Onset pattern:** Acute/subacute onset of seizures against a background of congenital or very-early hypotonia.

**Progression:** Progressive/severe — psychomotor stagnation or regression is characteristic; disease course is chronic and typically lifelong for survivors, with substantial early mortality (4/9 in the OMIM-cited series died between 7 months and 5 years).

**Disease course pattern:** Recurrent, refractory seizures with recurrent status epilepticus episodes (fever/temperature-transition triggered), interspersed with variable interictal function; not classically "relapsing-remitting" but rather chronically active with periodic severe exacerbations.

**Critical periods:** Mouse model data strongly implicate a **narrow neonatal therapeutic window** — AAV-mediated β1 gene replacement was dramatically effective when administered at postnatal day 2 (P2) but completely ineffective at P10, with P10-treated null mice dying at the same P16–P25 timeframe as untreated animals (PMC11870736). This suggests an analogous early-postnatal critical window may exist in human disease-modifying intervention, though this remains speculative for humans given current biallelic LOF (rather than replaceable single-variant) genotypes.

## 9. Inheritance and Population

**Epidemiology:** DEE52 is exceptionally rare — fewer than 10 families/patients had been reported in the literature as of the most recent detailed case series (Aeby et al. 2019 describes the "eighth reported SCN1B patient" with biallelic disease), with additional isolated cases and small series published subsequently (e.g., a 2026 consanguineous Pakistani family report). No formal prevalence or incidence estimate exists; it is an ultra-rare/orphan disease with only case-report-level epidemiological data available.

**Inheritance pattern:** **Autosomal recessive** for DEE52 (biallelic SCN1B variants) — distinct from the **autosomal dominant** inheritance of heterozygous SCN1B-related GEFS+.

**Penetrance:** For the recessive DEE52 form, penetrance appears high/complete in reported homozygotes (all reported biallelic carriers manifest disease). For the heterozygous GEFS+ C121W founder variant, penetrance is estimated at ~70% (12/44 carriers unaffected; Grinton et al. 2022), demonstrating markedly different penetrance behavior between the two allelic classes.

**Expressivity:** Variable within GEFS+ families (ranging from simple febrile seizures to severe epileptic encephalopathy phenotypes are described broadly for GEFS+ spectrum disorders); DEE52 case reports show more uniform severe presentation, though phenotype severity (developmental impact, presence/absence of hearing loss, cardiac involvement) varies somewhat across the small number of reported cases.

**Genetic anticipation:** Not reported/applicable (not a repeat-expansion disorder).

**Germline mosaicism:** Not specifically documented for SCN1B in the literature reviewed.

**Founder effects:** Well-documented for the heterozygous **C121W GEFS+ variant**, traced to a shared ancestral haplotype (~260 kb) persisting approximately 800 years across geographically dispersed families (Australia, UK, US) (Grinton et al. 2022) — a notable example of a disease-causing founder mutation under only weak negative selection given incomplete penetrance and generally mild phenotype in most carriers.

**Consanguinity role:** Central to DEE52 — the majority of reported biallelic cases arise in consanguineous pedigrees (Moroccan family, Patino et al. 2009; additional consanguineous families in subsequent reports), consistent with the rarity of the recessive allele requiring homozygosity by descent.

**Carrier frequency:** Not established in population databases; given ultra-rarity of reported pathogenic biallelic genotypes, carrier frequency for specific DEE52-causing alleles is presumed very low/population-specific (consistent with founder or private variants in consanguineous kindreds), though a precise gnomAD-derived carrier frequency was not identified in this research pass and should be checked directly in gnomAD at curation time.

**Population demographics:** Reported cases span diverse populations (Moroccan, and other consanguineous kindreds internationally, including at least one Pakistani family), consistent with a recessive disorder whose expression is driven by consanguinity/homozygosity rather than population-specific founder effects (in contrast to the heterozygous GEFS+ C121W founder variant, which shows a specific multi-national but genealogically linked distribution).

**Sex ratio:** Not specifically reported as skewed in the literature reviewed (autosomal gene, no evidence of sex-specific penetrance differences documented).

## 10. Diagnostics

**Clinical tests:**
- **EEG:** Bilateral central spikes in bursts with high-voltage slow waves; ictal recordings during status epilepticus episodes
- **Auditory brainstem response (ABR):** Documents sensorineural hearing loss and brainstem pathway involvement (wave V loss at lower intensities) — recommended given the reported association
- **Brain MRI:** Nonspecific atrophy may be seen; used to exclude structural/acquired causes
- **Cardiac evaluation:** Given emerging arrhythmia risk, ECG/Holter monitoring and cardiology referral are reasonable given the mechanistic overlap with Brugada-spectrum SCN1B disease and direct evidence of arrhythmia substrate in disease models

**Genetic testing approach:**
- **Recommended:** Epilepsy gene panel testing (including SCN1A, SCN1B, SCN2A, SCN8A, GABRG2, and other DEE-associated genes) or **whole exome/genome sequencing**, particularly important given that SCN1B-DEE52's clinical presentation can closely mimic SCN1A-Dravet syndrome — making single-gene SCN1A testing alone insufficient
- **Single-gene testing:** Reasonable when SCN1B is specifically suspected (e.g., consanguinity, prior family history, or after negative SCN1A testing in a Dravet-like presentation)
- **Segregation analysis:** Parental testing to confirm biallelic inheritance (heterozygous carrier parents) is standard confirmatory practice in reported cases
- **Chromosomal microarray/karyotype:** Not primarily indicated, as the disease mechanism is point variant/small lesion rather than copy-number or structural

**Clinical criteria:** No formal consensus diagnostic criteria specific to SCN1B-DEE52 exist (given its rarity); diagnosis relies on genetic confirmation in the context of a Dravet-like or early infantile DEE clinical picture with refractory infantile-onset seizures, fever sensitivity, and developmental impairment.

**Differential diagnosis:** SCN1A-related Dravet syndrome/DEE (most important differential, given phenotypic overlap); other DEE genes (SCN2A, SCN8A, KCNQ2, STXBP1, CDKL5, PCDH19); other causes of early infantile epileptic encephalopathy with hypotonia.

**Screening:** No population-based newborn screening applies given ultra-rarity; genetic counseling and carrier screening are relevant in consanguineous families or those with a previously affected child, and prenatal/preimplantation genetic testing may be offered once a familial variant is identified.

## 11. Outcome/Prognosis

**Mortality:** Substantial — 4 of 9 patients in the OMIM-cited cohort died, at ages 7 months to 5 years; a specific fatal case (respiratory insufficiency from aspiration pneumonia) occurred at 13 months (Patino et al. 2009). SUDEP risk is emphasized across multiple sources, increasingly attributed to a **combined neuro-cardiac mechanism** given 2025 evidence of cardiac excitability abnormalities in both mouse models and patient-derived iPSC-cardiomyocytes.

**Morbidity/function:** Survivors experience profound, persistent neurodevelopmental impairment — in the most detailed reported case, the patient remained unable to hold her head up at age 5 despite treatment-related seizure improvement, illustrating that seizure control alone does not equate to developmental rescue.

**Complications:** Refractory status epilepticus (recurrent, sometimes >8 episodes in early childhood); aspiration pneumonia/respiratory compromise; sensorineural hearing loss; presumptive cardiac arrhythmia risk.

**Recovery potential:** Poor for the developmental component even with seizure control — fenfluramine treatment achieved seizure freedom from status epilepticus in one reported case, but "motor and cognitive development remained severely impaired despite seizure improvement" (Aeby et al. 2019), underscoring that this is a true developmental *and* epileptic encephalopathy rather than a purely seizure-driven regression.

**Prognostic factors:** Early treatment/seizure control (associated with reduced status epilepticus frequency, though not necessarily improved developmental outcome); presence of cardiac involvement (plausibly linked to elevated mortality risk, though not yet formally quantified in humans).

## 12. Treatment

**Pharmacotherapy — general principles:** Because the underlying mechanism is **loss of function** (paralleling SCN1A-Dravet biology), **sodium channel blocking antiepileptics are contraindicated/relatively contraindicated**, as further pharmacological sodium channel inhibition can aggravate seizures. This includes carbamazepine, and by extension the broader sodium-channel-blocker class used cautiously or avoided (phenytoin was tried without success in the R125C case, consistent with this principle).

**Reported effective/attempted therapies:**
- **Fenfluramine**: Documented as effective in one reported SCN1B-DEE52 case (started at 28 months, 0.6 mg/kg/day), achieving significant reduction in seizure frequency and complete resolution of status epilepticus episodes through 2-year follow-up (Aeby et al. 2019) — consistent with fenfluramine's established efficacy in Dravet-spectrum sodium-channelopathy epilepsies more broadly (NCIT: pharmacotherapy; specific agent term applicable — fenfluramine)
- **Valproic acid, clobazam, clonazepam, phenytoin**: Reported as ineffective/refractory in at least one severe case (Patino et al. 2009) — standard broad-spectrum antiepileptics used per typical DEE/Dravet-spectrum protocols, with variable individual response

**Advanced/experimental therapeutics:**
- **Gene replacement therapy (preclinical, mouse model):** AAV vector carrying β1 subunit cDNA, delivered via bilateral intracerebroventricular injection, dramatically effective when administered neonatally (P2) in Scn1b-null mice — reducing seizure severity/duration, preventing hyperthermia-induced seizures, normalizing *Scn1a* mRNA expression, and extending survival past P100 versus 100% mortality by P21 in untreated animals. Critically, the same therapy was **ineffective when delayed to P10** (juvenile timing), with treated animals dying in the same window as untreated controls — highlighting a narrow critical treatment window (2025, PMC11870736). This remains a preclinical proof-of-concept; the authors note that actual human DEE52 patients typically express **mutant** (rather than fully absent) β1 protein, so translational applicability requires further study.
- No SCN1B-specific approved gene therapy, ASO, or targeted molecular therapy currently exists in clinical use; management otherwise follows general Dravet-spectrum/DEE supportive and pharmacological principles (e.g., stiripentol, cannabidiol, and other agents used in Dravet syndrome, by extrapolation, though not specifically documented for SCN1B-DEE52 in the sources reviewed here).

**Supportive care:** Fever management/avoidance of hyperthermia triggers; management of status epilepticus per standard protocols; nutritional/respiratory support given aspiration risk; multidisciplinary developmental/rehabilitative therapies (physical, occupational, speech) for the severe global developmental impairment.

**Suggested NCIT terms:** NCIT:C15986 (Pharmacotherapy) as the generic action term, with `therapeutic_agent` bound to specific agents (e.g., fenfluramine — CHEBI term to be verified) where documented; NCIT:C15238 (Gene Therapy) for the preclinical AAV approach.

## 13. Prevention

**Primary prevention:** Genetic counseling for consanguineous families or those with a prior affected child is the principal preventive strategy, given autosomal recessive inheritance; prenatal diagnosis or preimplantation genetic testing can be offered once the familial pathogenic variant(s) are identified.

**Secondary prevention:** Early genetic diagnosis in an infant presenting with early infantile refractory seizures and hypotonia enables prompt avoidance of contraindicated sodium-channel-blocking antiepileptics, potentially limiting iatrogenic seizure exacerbation.

**Screening:** No population-level newborn screening program exists for this ultra-rare condition; targeted carrier screening is relevant in populations/families with known consanguinity or a prior affected relative.

**Behavioral interventions:** Fever avoidance/aggressive antipyretic management and avoidance of known seizure triggers (hot baths, rapid sleep-state transitions) represent practical risk-reduction measures analogous to Dravet syndrome management, though not formally studied as a "prevention" strategy specific to SCN1B-DEE52.

**Public health/prophylaxis:** Not applicable at a population level given disorder rarity; management is entirely individualized/family-based.

## 14. Other Species / Natural Disease

No naturally occurring SCN1B-associated disease has been reported in non-human species (e.g., companion animals or wildlife) in the literature reviewed. All animal data derive from **engineered mouse models** (see Section 15) rather than spontaneously occurring veterinary disease. **Orthologous gene:** mouse *Scn1b* (MGI:98247, "sodium channel, voltage-gated, type I, beta"), located on mouse chromosome 7, with well-conserved function across mammals as demonstrated by the strong phenotypic concordance between mouse knockout models and human disease.

## 15. Model Organisms

**Mouse models (the dominant model system for this disease):**

1. **Scn1b-null (knockout) mice** — the foundational model (Isom laboratory, University of Michigan): recapitulate spontaneous generalized seizures beginning in the second postnatal week, increased hyperthermia-induced seizure sensitivity, **ataxia**, failure to thrive, cardiac arrhythmia, and **SUDEP**, closely mirroring the human DEE52/Dravet-like phenotype. Mice die by approximately postnatal day 21 (P21) without intervention.
   - Cerebellar mechanism: Purkinje cells and interneurons show increased action-potential-initiation thresholds and decreased repetitive firing frequency; reduced transient and resurgent sodium current densities in Purkinje cells underlie the ataxic phenotype (Yuan et al. 2025, JCI Insight, PMID:40923316)
   - Cardiac phenotype: altered cardiomyocyte excitability, atrial/ventricular arrhythmia susceptibility, sinoatrial node dysfunction and atrial fibrillation in neonatal Scn1b-null mice, increased transient outward K+ current density, and ventricular fibrosis; altered cardiac energetics also reported (multiple JCI Insight/Cardiovascular Research papers, 2024–2025)
   - Hippocampal circuit-level: complex synaptic and intrinsic interactions disrupt hippocampal input/output function (bioRxiv 2023)

2. **Scn1b-c.265C>T (p.R89C) knock-in mice** — a patient-variant-specific knock-in model of DEE52, showing spontaneous and hyperthermia-induced generalized seizures and SUDEP, used alongside patient-derived iPSC-cardiomyocytes to directly link the human pathogenic genotype to cardiac excitability abnormalities (PMID:40763036, 2025)

3. **Scn1b-C121W mice** — model the heterozygous **GEFS+** variant rather than DEE52; shown to produce a "deleterious gain-of-function" electrophysiological effect distinct from the biallelic loss-of-function DEE52 mechanism (Reid/Isom lab, J Neurosci 2016, PMID:27277800)

4. **Purkinje-cell-specific conditional Scn1b knockout mice** — a novel cell-type-restricted model isolating the cerebellar contribution to the DEE phenotype (bioRxiv 2024.11.19.624370)

**Model characteristics — phenotype recapitulation:** The Scn1b-null and knock-in mouse models recapitulate the core human triad of (1) treatment-refractory, hyperthermia-sensitive seizures, (2) high premature mortality/SUDEP, and (3) (increasingly) cardiac electrical abnormality — making them high-fidelity models for mechanistic and preclinical therapeutic studies (e.g., the AAV gene-replacement study, PMC11870736). Limitation: full Scn1b-null mice model complete absence of β1, whereas most human DEE52 patients express a mutant (mistrafficked or non-functional but present) protein rather than a true null — a translational caveat explicitly noted by the gene-therapy study authors.

**Applications:** These models have been used to study seizure semiology and hyperthermia sensitivity, cerebellar/ataxia mechanisms, cardiac arrhythmogenesis and SUDEP mechanisms, hippocampal circuit dysfunction, and to test AAV-based gene replacement as a proof-of-concept disease-modifying therapy.

**Resources:** MGI (Scn1b, MGI:98247) for allele/strain records; the Isom laboratory (University of Michigan) is the principal source of Scn1b-null and knock-in mouse lines cited across this literature.

---

## Summary of Key Ontology Term Suggestions for KB Curation

| Category | Suggested term(s) |
|---|---|
| Disease | OMIM:617350 (DEE52); confirm MONDO ID at curation time |
| Gene | hgnc:10586 (SCN1B) |
| Phenotypes (HP) | Status epilepticus, Myoclonic seizures, Focal seizures, Hypotonia, Microcephaly, Sensorineural hearing impairment, Global developmental delay, Developmental regression, Fever-induced seizures |
| Cell types (CL) | GABAergic interneuron, Purkinje cell, cardiac muscle cell |
| Anatomy (UBERON) | brain, cerebellum, cerebral cortex, heart |
| GO processes | sodium ion transmembrane transport, membrane depolarization during action potential |
| Treatment (NCIT) | Pharmacotherapy (NCIT:C15986) with fenfluramine as `therapeutic_agent`; Gene Therapy (NCIT:C15238) for the preclinical AAV approach |

---

## Notes on Evidence Gaps

- No formal population prevalence/incidence figure exists; the disease is characterized entirely through case reports/small series (fewer than ~10 reported families).
- The MONDO CURIE for DEE52 was not independently verified in this research pass and should be confirmed via direct MONDO/OAK lookup before KB entry.
- Cardiac phenotype data in humans (as opposed to mouse/iPSC models) remain preliminary; direct clinical arrhythmia documentation in SCN1B-DEE52 patients was not identified in the sources reviewed, though the mechanistic and model-organism evidence for cardiac involvement is substantial and recent (2024–2025).
- The exact PMID for the Scala et al. 2021 Epilepsia functional-variant study and for the 2025 "Altered cardiac excitability" JCI Insight paper's companion abstract details should be independently confirmed (PMID:40763036 was identified via search but full abstract text could not be directly retrieved due to access restrictions).

Sources:
- [SCN1B‐linked early infantile developmental and epileptic encephalopathy (Aeby et al. 2019, Ann Clin Transl Neurol)](https://onlinelibrary.wiley.com/doi/10.1002/acn3.50921)
- [SCN1B‐linked early infantile DEE — full text, PMC6917350](https://pmc.ncbi.nlm.nih.gov/articles/PMC6917350/)
- [OMIM #617350 — Developmental and Epileptic Encephalopathy 52](https://www.omim.org/entry/617350)
- [OMIM *600235 — SCN1B gene](https://omim.org/entry/600235)
- [A Functional Null Mutation of SCN1B in a Patient with Dravet Syndrome (Patino et al. 2009, J Neurosci) — PMC2749953](https://pmc.ncbi.nlm.nih.gov/articles/PMC2749953/)
- [A functional null mutation of SCN1B... — PubMed PMID:19710327](https://pubmed.ncbi.nlm.nih.gov/19710327/)
- [Altered cardiac excitability and arrhythmia in models of SCN1B-linked DEE — PubMed PMID:40763036](https://pubmed.ncbi.nlm.nih.gov/40763036/)
- [Altered cardiac excitability and arrhythmia in models of SCN1B-linked DEE — PMC12487680](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12487680/)
- [Ataxia and cerebellar hypoexcitability in a mouse model of SCN1B-linked Dravet syndrome — PubMed PMID:40923316](https://pubmed.ncbi.nlm.nih.gov/40923316/)
- [Ataxia and cerebellar hypoexcitability — PMC12487675](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12487675/)
- [A novel mouse model for DEE by Purkinje cell-specific deletion of Scn1b (bioRxiv 2024)](https://www.biorxiv.org/content/10.1101/2024.11.19.624370.full.pdf)
- [Neonatal but not juvenile gene therapy reduces seizures and prolongs lifespan in SCN1B–Dravet syndrome mice — PMC11870736](https://pmc.ncbi.nlm.nih.gov/articles/PMC11870736/)
- [β1-C121W Is Down But Not Out: Epilepsy-Associated Scn1b-C121W Results in a Deleterious Gain-of-Function — PMC4899524](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4899524/)
- [β1-C121W Is Down But Not Out — PubMed PMID:27277800](https://pubmed.ncbi.nlm.nih.gov/27277800/)
- [The millennium variant – SCN1B, gene validity, and GEFS+ (Beyond the Ion Channel blog, discussing Grinton et al. 2022 founder haplotype)](http://epilepsygenetics.net/2023/01/10/the-millennium-variant-scn1b-gene-validity-and-gefs/)
- [SCN1B Genetic Variants: A Review of the Spectrum of Clinical Phenotypes and a Report of Early Myoclonic Encephalopathy — PMC9600564](https://pmc.ncbi.nlm.nih.gov/articles/PMC9600564/)
- [Generalized epilepsy with febrile seizures plus: Mutation of the sodium channel subunit SCN1B — Neurology](https://www.neurology.org/doi/10.1212/WNL.58.9.1426)
- [SCN1B gene variants in Brugada Syndrome: a study of 145 SCN5A-negative patients — Scientific Reports](https://www.nature.com/articles/srep06470)
- [Voltage-Gated Sodium Channel β1/β1B Subunits Regulate Cardiac Physiology and Pathophysiology — PMC5924814](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5924814/)
- [Identification of a Novel Homozygous SCN1B Splice-Site Variant in a Consanguineous Family with Early-Onset Epilepsy — Molecular Genetics & Genomic Medicine (2026)](https://onlinelibrary.wiley.com/doi/10.1002/mgg3.70214)
- [Scn1b MGI Mouse Gene Detail — MGI:98247](https://www.informatics.jax.org/marker/MGI:98247)
- [SCN1B Gene — GeneCards](https://www.genecards.org/cgi-bin/carddisp.pl?gene=SCN1B)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 14 |
| Off topic | 0 |

All extracted references resolved successfully.