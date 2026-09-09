---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-28T11:31:24.578943'
end_time: '2026-08-28T11:40:10.688243'
duration_seconds: 526.11
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Primary Ciliary Dyskinesia 30 (ODAD3/CCDC151-related)
  mondo_id: MONDO:0014465
  category: Respiratory Disorders
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 12
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 37
  verified: 37
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0014465
    reported_labels:
    - if available
    ontology_label: primary ciliary dyskinesia 30
  labels_variant: 2
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Primary_Ciliary_Dyskinesia_30-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Primary Ciliary Dyskinesia 30 (ODAD3/CCDC151-related)
- **MONDO ID:** MONDO:0014465 (if available)
- **Category:** Respiratory Disorders

## Research Objectives

Please provide a comprehensive research report on **Primary Ciliary Dyskinesia 30 (ODAD3/CCDC151-related)** covering all of the
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

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Primary Ciliary Dyskinesia 30 (ODAD3/CCDC151-related)
- **MONDO ID:** MONDO:0014465 (if available)
- **Category:** Respiratory Disorders

## Research Objectives

Please provide a comprehensive research report on **Primary Ciliary Dyskinesia 30 (ODAD3/CCDC151-related)** covering all of the
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


# Primary Ciliary Dyskinesia 30 (ODAD3/CCDC151-related): Research Report

## Executive summary and evidence limits

Primary ciliary dyskinesia 30 (PCD30) is a very rare, autosomal-recessive motile ciliopathy caused by biallelic loss-of-function variants in **ODAD3**, historically named **CCDC151**. The defect prevents assembly of the outer dynein-arm docking machinery and outer dynein arms onto motile-ciliary axonemes. Respiratory cilia consequently beat very poorly, producing congenital mucociliary-clearance failure, recurrent sino-oto-pulmonary infection, and progressive bronchiectasis. Dysfunction of embryonic nodal cilia randomizes left–right development; four of the five individuals in the foundational series had a laterality defect. Human gene-specific knowledge remains based principally on five affected individuals from three families, supplemented by one independently reported Arabic case and strong mouse, zebrafish, and other comparative evidence. Most natural-history, prognosis, and treatment statements below therefore derive from **PCD overall**, not specifically PCD30. (hjeij2014ccdc151mutationscause pages 1-2, hjeij2014ccdc151mutationscause pages 2-3, alsaadi2014nonsensemutationin pages 1-2)

| domain | finding | quantitative detail | evidence type/source |
|---|---|---|---|
| Disease identity | ODAD3/CCDC151-related primary ciliary dyskinesia corresponds to a gene-specific form of PCD; ODAD3 is the current HGNC-approved symbol for the former CCDC151 gene product name “outer dynein arm docking complex subunit 3” | Open Targets links ODAD3 to primary ciliary dyskinesia; historical literature uses CCDC151 | Curated disease-target association plus primary human gene-discovery paper (OpenTargets Search: Primary ciliary dyskinesia-ODAD3,CCDC151, hjeij2014ccdc151mutationscause pages 1-2) |
| Inheritance | Inheritance is autosomal recessive | Segregation consistent with recessive disease in reported families | Human clinical genetics/segregation study (hjeij2014ccdc151mutationscause pages 2-3, alsaadi2014nonsensemutationin pages 1-2) |
| Causal variants | Two recurrent truncating variants were identified in the foundational series | c.925G>T (p.Glu309*) and c.1256C>A (p.Ser419*); both absent from 1000 Genomes and EVS in the 2014 report | Human NGS/exome plus Sanger confirmation (hjeij2014ccdc151mutationscause pages 2-3) |
| Reported patients/families | Foundational disease-specific evidence base is very small | 5 affected individuals from 3 unrelated families | Human case series/gene-discovery study (hjeij2014ccdc151mutationscause pages 1-2, hjeij2014ccdc151mutationscause pages 2-3) |
| Core respiratory phenotype | All reported affected individuals had a phenotype consistent with PCD | Recurrent upper and lower airway disease, chronic respiratory symptoms, bronchiectasis, nasal blockage/polyps, otitis media reported across the 5-person series | Human clinical case series (hjeij2014ccdc151mutationscause pages 2-3) |
| Neonatal onset | Early presentation is typical in the reported gene-specific cases | 4/5 had very early involvement with neonatal respiratory distress syndrome | Human clinical case series (hjeij2014ccdc151mutationscause pages 2-3) |
| Laterality phenotype | Laterality defects are common in this gene-specific form | 4/5 had laterality defects; one had congenital heart disease (ventricular septal defect) | Human clinical case series (hjeij2014ccdc151mutationscause pages 2-3) |
| Ultrastructure | Hallmark ciliary defect is isolated outer dynein arm loss | Respiratory cilia showed complete ODA loss and specific loss of ODAs on TEM | Human TEM plus conserved model-organism data (hjeij2014ccdc151mutationscause pages 1-2, hjeij2014ccdc151mutationscause pages 11-15) |
| Protein localization defect | ODAD3/CCDC151 loss disrupts axonemal assembly of ODA machinery | CCDC151 severely reduced or absent from axonemes; axonemal DNAH5, CCDC114, and ARMC4 fail to localize properly | Human immunofluorescence and protein-interaction data (hjeij2014ccdc151mutationscause pages 1-2, hjeij2014ccdc151mutationscause pages 15-16) |
| Mechanism | Disease mechanism is failure of outer dynein arm docking-complex formation | CCDC151 interacts with CCDC114 and is required for assembly of ODA docking components and ODAs onto axonemes | Human co-immunoprecipitation, IF, TEM; mouse/zebrafish corroboration (hjeij2014ccdc151mutationscause pages 1-2, hjeij2014ccdc151mutationscause pages 15-16) |
| Ciliary function | Ciliary beating is severely impaired because ODA force-generating machinery is lost | Report described severely impaired ciliary beating or dysmotility associated with ODA deficiency | Human respiratory cilia studies with animal corroboration (hjeij2014ccdc151mutationscause pages 1-2) |
| Model-organism support | Conservation across species strongly supports causality | CCDC151-deficient zebrafish and mouse show ciliary dysmotility, situs defects, and complex heart defects; prior work also cites Chlamydomonas and Drosophila relevance | Model-organism evidence integrated with human genetics (hjeij2014ccdc151mutationscause pages 1-2, hjeij2014ccdc151mutationscause pages 11-15) |
| General PCD epidemiology (extrapolated, not CCDC151-specific) | PCD is rare and underdiagnosed | Approximate prevalence cited as ~1 in 10,000 in iPCD cohort background; other reviews cite 1:15,000 to 30,000 | Large disease-level cohort/review; extrapolated to this subtype with caution (goutaki2017theinternationalprimary pages 2-3, paff2021currentandfuture pages 1-2) |
| General PCD laterality (extrapolated, not CCDC151-specific) | Laterality defects occur in about half of all PCD cases overall | Around 50% with laterality defects; about 12% may have heterotaxy or complex isomerism in general PCD literature | Disease-level review/background; extrapolated only (hjeij2014ccdc151mutationscause pages 2-3, paff2021currentandfuture pages 1-2) |
| General PCD lung burden (extrapolated, not CCDC151-specific) | Lung disease begins early and can be progressive | In iPCD, children 6–9 years had mean FEV1 z-score -0.84; review cites average FEV1 decline about 0.8% per year | International cohort and review; not subtype-specific (halbeisen2018lungfunctionin pages 2-3, paff2021currentandfuture pages 1-2) |
| Evidence limitation | Natural history, prevalence, prognosis, and treatment-response data specific to ODAD3/CCDC151 are not yet established | No robust 2023–2024 gene-specific cohorts identified; most management is inferred from general PCD practice | Evidence-gap statement based on available literature set (hjeij2014ccdc151mutationscause pages 1-2, goutaki2017theinternationalprimary pages 2-3, paff2021currentandfuture pages 1-2) |


*Table: This table summarizes the core disease-specific evidence for ODAD3/CCDC151-related PCD30 and distinguishes it from broader primary ciliary dyskinesia data. It is useful for quickly separating directly observed subtype facts from extrapolated general PCD knowledge.*

## 1. Disease information

### Definition

PCD30 is a congenital disorder of motile cilia in which ODAD3 deficiency causes isolated outer dynein-arm (ODA) loss and severe ciliary dysmotility. It belongs to the respiratory ciliopathies and clinically manifests as lifelong wet cough, chronic rhinosinusitis, recurrent lower-respiratory infection, otitis media, bronchiectasis, laterality abnormalities, and probable sex-specific fertility impairment. The foundational paper describes PCD generally as producing “lifelong recurrent respiratory infections and irreversible, destructive airway disease (bronchiectasis) of early onset.” (hjeij2014ccdc151mutationscause pages 2-3)

### Identifiers and terminology

- **Preferred disease name:** Primary ciliary dyskinesia 30; ODAD3-related primary ciliary dyskinesia; CCDC151-related PCD.
- **Gene:** **ODAD3**, approved name *outer dynein arm docking complex subunit 3*; legacy symbol **CCDC151**; Ensembl **ENSG00000198003**. Open Targets associates ODAD3 with MONDO primary ciliary dyskinesia on genetic, literature, ClinVar, and expert-curation evidence. (OpenTargets Search: Primary ciliary dyskinesia-ODAD3,CCDC151)
- **MONDO:** The supplied record is **MONDO:0014465**. Database releases should be checked before production because broad PCD is represented in Open Targets as **MONDO:0016575**, and disease-subtype mappings can change. (OpenTargets Search: Primary ciliary dyskinesia-ODAD3,CCDC151)
- **OMIM:** Broad PCD is historically cited as MIM 244400 in the discovery paper. PCD30 is commonly catalogued separately in current genetic resources, but its exact subtype identifier should be programmatically revalidated against the current OMIM release rather than inferred from older articles. (hjeij2014ccdc151mutationscause pages 2-3)
- **Orphanet/MeSH:** Usually indexed under broad *primary ciliary dyskinesia* rather than a dedicated ODAD3 subtype.
- **ICD-10:** No gene-specific code; coding generally uses the jurisdiction’s PCD/Kartagener or bronchiectasis code. **ICD-11** provides a PCD concept but not a routinely used ODAD3-specific code.
- **Synonyms:** Ciliary dyskinesia, primary, 30; PCD30; CCDC151 deficiency; ODAD3 deficiency; CCDC151-related Kartagener syndrome when situs inversus is present. “Kartagener syndrome” is not synonymous with all PCD30 because normally positioned or heterotaxic organs are possible.

The evidence is **aggregated disease-level literature and family-based research**, not an individual EHR extract.

## 2. Etiology, risk, and protective factors

PCD30 is caused by **germline biallelic ODAD3 loss of function**. Familial segregation in the discovery families was consistent with autosomal-recessive inheritance. The initial variants were absent from the 1000 Genomes and NHLBI Exome Variant Server datasets available in 2014. (hjeij2014ccdc151mutationscause pages 2-3)

The principal risk factors are carrier parents, an affected sibling, shared ancestry, and consanguinity. Consanguinity facilitated homozygosity mapping in the reported Bedouin-Arabic and UK-Pakistani families. No environmental exposure causes the genetic disease, and no validated susceptibility loci, modifier genes, protective alleles, epigenetic modifiers, or gene–environment interactions are established specifically for ODAD3-related PCD.

Environmental factors instead modify **downstream morbidity**. Tobacco smoke, vaping, particulate pollution, poor infection control, and delayed antimicrobial treatment plausibly increase respiratory injury; vaccination, smoke avoidance, exercise, airway clearance, and early treatment may reduce complications but do not prevent the underlying ciliopathy. These are expert-practice extrapolations from PCD/bronchiectasis, not ODAD3-specific intervention evidence. PCD treatment evidence remains sparse: a review found only three randomized trials and noted that practice is largely based on expert opinion and cystic-fibrosis extrapolation. (paff2021currentandfuture pages 1-2)

## 3. Phenotypes

### ODAD3-specific observations

All five individuals in the foundational series had recurrent upper- and lower-airway disease, chronic respiratory symptoms and bronchiectasis, with nasal obstruction/polyps and otitis media. Four of five had neonatal respiratory distress and four of five had a laterality defect; one had a ventricular septal defect. (hjeij2014ccdc151mutationscause pages 2-3)

Suggested phenotype annotations are:

- Neonatal respiratory distress — **HP:0002643**; congenital/early, observed in 4/5.
- Chronic wet/productive cough — **HP:0031245**; infancy or early childhood onward, persistent.
- Recurrent respiratory infection — **HP:0002205**; recurrent and lifelong.
- Bronchiectasis — **HP:0002110**; progressive structural complication.
- Chronic rhinosinusitis — **HP:0011109**; persistent.
- Nasal polyposis — **HP:0100582**; variable.
- Recurrent/chronic otitis media — **HP:0000403**; commonly childhood-onset.
- Abnormal ciliary motility — **HP:0012262**; constitutive laboratory/cellular phenotype.
- Absent outer dynein arms — **HP:0012259**; characteristic ultrastructural finding.
- Situs inversus totalis — **HP:0001696**, or heterotaxy — **HP:0030853**; congenital and nonprogressive.
- Congenital heart defect/VSD — **HP:0001627/HP:0001629**; observed in one discovery subject.
- Male infertility due to sperm dysmotility — **HP:0003251/HP:0012206**; biologically expected in motile-cilia PCD but not quantified for ODAD3.

Percentages such as 80% neonatal distress or laterality must be treated as **descriptive fractions, not stable prevalence estimates**, because the denominator is only five and ascertainment favored ODA-deficient PCD.

### General PCD burden

Approximately half of people with PCD have situs inversus or another laterality defect; broad PCD literature estimates complex heterotaxy/isomerism in about 12%. (paff2021currentandfuture pages 1-2, hjeij2014ccdc151mutationscause pages 2-3) In an international study of 991 patients, lung function was impaired in both sexes and every age group. Children aged 6–9 years had mean FEV1 z-score −0.84 and FVC z-score −0.31; mean FEV1 was 91% predicted at 6–9 years and 79% at 18–21 years. These values demonstrate early disease but are not ODAD3-specific. (halbeisen2018lungfunctionin pages 2-3)

Upper-airway disease materially affects well-being. A 2023 genetically confirmed PCD cohort of 58 found chronic rhinosinusitis in all participants, prior sinus surgery in 47%, mean SNOT-20 score 35.8±17, and mean Lund–Mackay CT score 10.2±4.4; frontal- and sphenoid-sinus agenesis occurred in 19% and 9.5% of participants aged at least 16. These findings should not be assigned specifically to ODAD3 without genotype-level data.

## 4. Genetic and molecular information

The foundational study identified **five patients from three families** with homozygous nonsense alleles:

1. **NM_145045.4:c.925G>T, p.(Glu309Ter)**, historically also rendered p.Glu308* because of transcript/numbering differences; found in two unrelated Arabic-origin pedigrees.
2. **NM_145045.4:c.1256C>A, p.(Ser419Ter)** in a consanguineous UK-Pakistani family. Some secondary summaries incorrectly render the nucleotide change as C>T; the primary full text gives **C>A**. (hjeij2014ccdc151mutationscause pages 2-3)

An independent consanguineous Arabic case carried homozygous c.925G>T, had bronchiectasis, recurrent chest infections, chronic productive cough, very low nasal nitric oxide, asthma/allergic rhinitis and pectus excavatum; the allele was absent from 238 controls. (alsaadi2014nonsensemutationin pages 1-2)

These are truncating, germline, recessive loss-of-function variants. Contemporary clinical classification should use ACMG/AMP criteria, current transcript normalization, segregation, phenotype, population frequency, and functional evidence. No somatic mechanism, repeat expansion, mitochondrial defect, recurrent chromosomal rearrangement, or aneuploidy is implicated. Large deletions or noncoding ODAD3 alleles remain possible and justify deletion/duplication analysis or genome sequencing in unresolved cases.

ODAD3 encodes a 595-amino-acid, highly conserved protein with three predicted coiled-coil domains. The two reported truncations lie within coiled-coil regions and are predicted to disrupt protein interactions. No validated ODAD3-specific modifier gene or disease-associated methylation signature is known. (hjeij2014ccdc151mutationscause pages 2-3)

## 5. Environmental and infectious information

Bacteria and viruses are **complications or exacerbation triggers**, not causes. Impaired clearance permits chronic/recurrent airway infection and a mucus–infection–inflammation cycle. Pathogens encountered in PCD/bronchiectasis commonly include *Haemophilus influenzae*, *Staphylococcus aureus*, *Streptococcus pneumoniae*, and later *Pseudomonas aeruginosa*; organism-specific frequencies are unavailable for ODAD3.

Avoidance of tobacco smoke, vaping, biomass smoke, occupational dusts, and excessive air pollution is prudent. Regular physical activity and hydration may support airway clearance. No diet, supplement, alcohol pattern, toxin, radiation exposure, or infectious agent has been shown to alter penetrance of ODAD3 deficiency.

## 6. Mechanism and pathophysiology

### Causal chain

**Biallelic ODAD3 loss of function → absent/truncated ODAD3 in the axoneme → failure to assemble ODAD docking proteins CCDC114/ODAD1 and ARMC4/ODAD2 → failure to localize DNAH5-containing outer dynein arms → loss of most axonemal sliding force → severely dyskinetic or static motile cilia → impaired mucociliary transport → mucus retention, infection and neutrophilic inflammation → airway-wall injury and bronchiectasis.** In embryonic left–right organizers, defective nodal flow randomizes organ laterality and may produce heterotaxy/congenital heart disease. (hjeij2014ccdc151mutationscause pages 1-2, hjeij2014ccdc151mutationscause pages 15-16, hjeij2014ccdc151mutationscause pages 2-3)

ODAs occur at approximately 24-nm intervals along axonemal microtubules and generate as much as four-fifths of the sliding force required for ciliary bending. Thus ODA loss explains the severe motility phenotype. (hjeij2014ccdc151mutationscause pages 2-3)

Human respiratory-cell immunofluorescence showed absent axonemal CCDC114, ARMC4 and DNAH5, while inner-dynein-arm markers remained preserved. Co-immunoprecipitation demonstrated reciprocal association between ODAD3/CCDC151 and CCDC114. TEM showed complete ODA loss. These human cellular results provide direct evidence rather than computational inference. (hjeij2014ccdc151mutationscause pages 1-2, hjeij2014ccdc151mutationscause pages 11-15, hjeij2014ccdc151mutationscause pages 15-16)

### Ontology suggestions

- **GO biological process:** cilium movement (GO:0003341); cilium assembly (GO:0060271); axonemal dynein complex assembly (GO:0070286); mucociliary clearance (GO:0120197); determination of left/right symmetry (GO:0007368).
- **GO cellular component:** motile cilium (GO:0031514); ciliary axoneme (GO:0005930); outer dynein arm (GO:0036157); axonemal dynein complex (GO:0005858); microtubule cytoskeleton (GO:0015630).
- **Cell Ontology:** multiciliated epithelial cell (**CL:0005012**); respiratory epithelial cell; ependymal cell (**CL:0000065**); sperm (**CL:0000019**); embryonic node ciliated cell where supported.
- **Processes downstream:** innate inflammatory response, neutrophil activation, tissue remodeling and fibrosis. These are secondary to clearance failure, not a primary immunodeficiency.

No ODAD3-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or multi-omic patient signature has been established. The decisive profiling methods remain targeted immunofluorescence, TEM, high-speed videomicroscopy, and genomic sequencing.

## 7. Anatomical structures affected

Primary sites are multiciliated epithelia of the nose, paranasal sinuses, middle ear/Eustachian tube, trachea and bronchi; embryonic left–right organizers; and reproductive-tract motile cilia/flagella. Secondary damage includes bronchiectasis, mucus plugging, atelectasis, chronic sinus opacification, conductive hearing impairment, and occasionally respiratory failure.

Suggested anatomy terms include **UBERON:0001004** respiratory system, **UBERON:0002048** lung, **UBERON:0003126** trachea, **UBERON:0002185** bronchus, **UBERON:0000004** nose, **UBERON:0001825** paranasal sinus, **UBERON:0001756** middle ear, and reproductive tract structures. The relevant subcellular structure is the apical 9+2 motile-ciliary axoneme. Laterality may be normal, completely reversed, or heterotaxic; respiratory disease is generally bilateral/diffuse rather than unilateral.

## 8. Temporal development

The molecular defect is congenital. Four of five foundational patients had neonatal respiratory distress; persistent wet cough, nasal congestion and recurrent infection begin in infancy or childhood. Bronchiectasis is an acquired but often early and progressive complication. Laterality and congenital cardiac defects arise during embryogenesis and do not progress. (hjeij2014ccdc151mutationscause pages 2-3)

PCD is lifelong, with fluctuating infectious exacerbations superimposed on chronic disease. Broad PCD estimates suggest average FEV1 decline near 0.8 percentage points annually, but trajectories vary and this rate is not ODAD3-specific. (paff2021currentandfuture pages 1-2) There is no spontaneous molecular remission. Early diagnosis, daily clearance, infection control, hearing surveillance and nutritional support represent the main windows for preventing irreversible damage.

## 9. Inheritance and population

Inheritance is autosomal recessive. For two carrier parents, each pregnancy has a 25% probability of an affected child, 50% probability of an unaffected carrier, and 25% probability of inheriting neither familial allele. Penetrance of biallelic truncating variants appears high, but the available families are too few to estimate it. Expressivity is variable, particularly for laterality; anticipation is not expected. Germline mosaicism has not been specifically reported but cannot be excluded.

Broad PCD prevalence is often estimated around **1:10,000**, with reviews citing approximately 1:15,000–30,000 and substantial underdiagnosis. ODAD3-specific prevalence and incidence are unknown. (goutaki2017theinternationalprimary pages 2-3, paff2021currentandfuture pages 1-2) In the 3,013-person iPCD cohort, 49% were male, ages ranged from 0–92 years, median age was 18, and 38% were aged 10–19. This near-equal sex distribution is consistent with autosomal inheritance. (goutaki2017theinternationalprimary pages 6-7)

The recurrent c.925G>T allele occurred in two Arabic-origin pedigrees. The original investigators could not exclude a founder effect because haplotypes were unavailable, whereas the independent report considered a founder effect unlikely after absence in 238 controls. These interpretations are not definitive. (hjeij2014ccdc151mutationscause pages 15-16, alsaadi2014nonsensemutationin pages 1-2)

## 10. Diagnostics

### Clinical suspicion

Suspect PCD in term neonates with unexplained respiratory distress, persistent year-round wet cough or nasal congestion beginning before six months, recurrent otitis/hearing problems, bronchiectasis without another cause, or any such phenotype combined with situs abnormality. PICADAR may support referral but cannot confirm disease.

### Multimodal testing

No single negative test excludes all PCD. Expert assessment combines:

1. **Nasal nitric oxide (nNO):** typically very low after excluding acute viral illness and cystic fibrosis; best standardized in cooperative patients.
2. **High-speed video microscopy:** assesses beat frequency and waveform, preferably with repeat sampling or air–liquid-interface culture to distinguish primary from secondary dyskinesia.
3. **TEM:** ODAD3 disease predicts a diagnostic Class-1 pattern of absent outer dynein arms. International TEM guidance emphasizes standardized terminology, sample adequacy and distinction between diagnostic Class-1 and supportive Class-2 defects. (hjeij2014ccdc151mutationscause pages 11-15)
4. **Immunofluorescence:** expected absence/reduction of axonemal ODAD3 with absent DNAH5, CCDC114 and ARMC4 but preserved inner-arm components. This is especially informative for variant functional validation. (hjeij2014ccdc151mutationscause pages 1-2, hjeij2014ccdc151mutationscause pages 15-16)
5. **Genetic testing:** begin with a comprehensive PCD panel including ODAD3 and deletion/duplication analysis or use exome/genome sequencing. Demonstration of two pathogenic/likely pathogenic variants in trans confirms molecular diagnosis in an appropriate phenotype.

The foundational families were solved through targeted NGS, WES, autozygosity mapping, segregation testing and Sanger confirmation. (hjeij2014ccdc151mutationscause pages 2-3) A 2024 WGS study found pathogenic/likely pathogenic biallelic diagnoses in 7/8 selected PCD cases and resolved 3–13-kb deletions; it estimated that standard testing currently solves about 70% of PCD and argued that WGS can identify structural, noncoding, and novel-gene mechanisms. These figures concern PCD generally, not ODAD3.

CMA, karyotyping and FISH are not first-line tests for isolated PCD30; mitochondrial and repeat-expansion testing are not indicated. RNA studies may clarify splice or noncoding variants but are not routine diagnostic biomarkers. Carrier and cascade testing should target confirmed familial variants.

### Differential diagnosis

Important alternatives are cystic fibrosis, immunodeficiency, aspiration/swallowing dysfunction, post-infectious bronchiectasis, allergic bronchopulmonary aspergillosis, severe asthma, congenital airway malformation, Young syndrome, alpha-1 antitrypsin deficiency, and acquired secondary ciliary injury. CF is distinguished by sweat chloride/CFTR testing; immune disease by quantitative immunoglobulins and vaccine responses; secondary dyskinesia should improve on repeat/cultured sampling. Kartagener syndrome denotes the PCD-plus-situs-inversus phenotype rather than a separate mechanism.

## 11. Outcome and prognosis

No ODAD3-specific survival curve, mortality rate, life expectancy, transplant-free survival, or validated prognostic biomarker exists. Broad PCD can progress from chronic infection to bronchiectasis, airflow obstruction, chronic *Pseudomonas* infection, oxygen dependence, respiratory failure and lung transplantation. The iPCD investigators explicitly noted that age-standardized mortality data were unavailable and that genotype effects on mortality remained unclear. (goutaki2017theinternationalprimary pages 2-3)

Disease severity is not necessarily mild. In general PCD, FEV1 is already reduced in early school age and can approximate cystic-fibrosis impairment during childhood. (halbeisen2018lungfunctionin pages 2-3) Potential adverse prognostic factors include delayed diagnosis, low baseline FEV1, poor nutritional status, frequent exacerbations, chronic *Pseudomonas*, inadequate airway clearance and extensive bronchiectasis. Unlike CCDC39/CCDC40-associated microtubular disorganization, ODAD3 has not been proven to define an especially aggressive lung-function trajectory.

Quality of life is impaired by daily treatment burden, cough, sputum, sinus symptoms, hearing difficulty, fatigue, school/work disruption and fertility concerns. Valid tools include QOL-PCD, SNOT-20/22, spirometry and exacerbation frequency; no ODAD3-specific patient-reported measure exists.

## 12. Treatment and current applications

There is no approved ODAD3-restoring or curative therapy. Management should occur in a specialist multidisciplinary PCD/bronchiectasis center.

- **Daily individualized airway-clearance physiotherapy** and regular aerobic exercise are foundational (NCIt concepts: Respiratory Therapy; Physical Therapy; Exercise Therapy).
- **Antibiotics** should be given promptly for exacerbations, guided by sputum/nasopharyngeal cultures and prior microbiology. New *Pseudomonas* isolation is commonly treated with eradication protocols extrapolated from bronchiectasis/CF.
- **Azithromycin maintenance** may be considered for frequent exacerbations after checking ECG/QT risk, hearing, liver function, drug interactions, and nontuberculous mycobacteria. PCD treatment reviews identify the randomized BESTCILIA trial as a major disease-specific advance, while emphasizing antimicrobial-resistance risk and limited long-term evidence. (paff2021currentandfuture pages 1-2)
- **Nebulized hypertonic saline** can be trialed for sputum mobilization, but a small PCD RCT did not establish a robust primary quality-of-life benefit; bronchospasm and treatment burden should be monitored.
- **Bronchodilators/inhaled corticosteroids** are not routine disease-modifying therapy; use when coexisting asthma or demonstrable reversibility warrants them.
- **ENT care:** saline nasal irrigation, hearing surveillance, individualized hearing aids/grommets, and selected sinus surgery. Evidence remains largely observational.
- **Advanced disease:** oxygen, noninvasive ventilation, selected lobectomy only for exceptional localized destructive disease, and lung transplantation for end-stage respiratory failure.

The evidence base is modest: current treatment primarily seeks “improving mucociliary clearance and early treatment of bacterial airway infections,” and no causal treatment was available in the reviewed clinical literature. (paff2021currentandfuture pages 1-2)

### Emerging therapy and trials

mRNA replacement, gene addition/editing, read-through therapy and airway epithelial correction are rational strategies, but none has established clinical efficacy for ODAD3. Trials retrieved for PCD overall included phase-1 inhaled mRNA program RCT1100 (**NCT05737485**, completed; **NCT06600425**, completed), ENaC inhibition (**NCT02871778**, phase 2, 123 participants, completed), diagnostic-care utility (**NCT03704207**, recruiting), and airway-clearance/physiotherapy studies. These are not ODAD3-specific and trial status should be rechecked at https://clinicaltrials.gov before use. No genotype-guided pharmacogenomic recommendation exists.

## 13. Prevention

Primary prevention of an affected conception is possible only through informed reproductive options: carrier testing, partner testing, prenatal diagnosis, and preimplantation genetic testing for a known familial variant. There is no newborn population screen for PCD30.

Secondary prevention consists of early recognition, cascade testing of relatives, and prompt specialist referral. Tertiary prevention includes daily airway clearance, respiratory cultures, timely antibiotics, routine spirometry, nutrition and hearing monitoring, influenza and COVID-19 immunization, age-appropriate pneumococcal vaccination, smoke avoidance, exercise, and hygiene measures. Vaccines prevent infectious complications, not ODAD3 deficiency.

Genetic counseling should explain recessive recurrence risks, uncertainty in phenotype prediction, variable organ laterality, fertility implications, and the possibility that a VUS is not diagnostic without segregation and functional evidence.

## 14. Other species and natural disease

ODAD3/CCDC151 function is evolutionarily conserved in motile cilia. Orthologous defects have been studied in mouse (*Mus musculus*, NCBI Taxon 10090), zebrafish (*Danio rerio*, 7955), fruit fly (*Drosophila melanogaster*, 7227), green alga *Chlamydomonas reinhardtii* (3055), and planarian systems. The 2014 study concluded from human cells, mice and zebrafish that CCDC151 is required for ODA/docking-complex assembly and correct left–right patterning. (hjeij2014ccdc151mutationscause pages 1-2, hjeij2014ccdc151mutationscause pages 11-15)

No established naturally occurring veterinary ODAD3 syndrome, breed predisposition, VBO annotation, or animal-health prevalence was identified. The condition is inherited and noninfectious, with no zoonotic or cross-species transmission.

## 15. Model organisms

- **Mouse:** the ENU-derived **Ccdc151^Snbl (Snowball)** allele is a splice-site variant, c.828+2T>C. Homozygous mice show ciliary dysmotility, ODA loss, situs inversus/heterotaxy and complex heart defects. The model strongly reproduces axonemal and developmental disease, although murine airway anatomy, lifespan and infection exposure limit direct prediction of chronic human bronchiectasis. (hjeij2014ccdc151mutationscause pages 1-2, hjeij2014ccdc151mutationscause pages 2-3)
- **Zebrafish:** the **flanders/ccdc151^ts272a** mutant and morpholino models show motile-cilia defects, ODA loss, abnormal left–right signaling and situs/cardiac abnormalities. They are particularly useful for live imaging of Kupffer’s-vesicle flow and rapid rescue experiments, but do not reproduce human chronic airway disease. (hjeij2014ccdc151mutationscause pages 1-2, hjeij2014ccdc151mutationscause pages 3-4)
- **Chlamydomonas:** the orthologous **oda10** null lacks ODAs, offering a tractable axonemal assembly model. (hjeij2014ccdc151mutationscause pages 2-3)
- **Drosophila/planarian and human nasal epithelial cells:** useful for conserved trafficking/motility and direct patient-specific IF, TEM and high-speed-video studies, respectively. (hjeij2014ccdc151mutationscause pages 11-15)

## Key recent developments, 2023–2024

Recent advances mostly concern PCD broadly rather than new ODAD3 cohorts: a 2024 state-of-the-art pediatric review emphasized underdiagnosis, expanded phenotypes, genotype–phenotype relationships and emerging therapeutics; 2024 WGS work demonstrated improved detection of structural and noncoding mechanisms; and 2023 imaging studies quantified substantial sinonasal structural disease and quality-of-life burden. Nevertheless, no 2023–2024 study established ODAD3-specific prevalence, longitudinal decline, treatment response, single-cell profile, or targeted therapy. The foundational ODAD3 evidence therefore remains Hjeij et al., published **4 September 2014**, DOI https://doi.org/10.1016/j.ajhg.2014.08.005, PMID **25192045**. (OpenTargets Search: Primary ciliary dyskinesia-ODAD3,CCDC151, hjeij2014ccdc151mutationscause pages 1-2, hjeij2014ccdc151mutationscause pages 15-16)

### Representative exact source statements

- The discovery series reported: “In total, the mutational analysis detected CCDC151 loss-of-function nonsense mutations affecting five PCD individuals in three families.” (hjeij2014ccdc151mutationscause pages 2-3)
- It further stated: “Four of the five affected individuals had laterality defects.” (hjeij2014ccdc151mutationscause pages 2-3)
- The independent report described “a novel nonsense mutation in a homozygous state … NM_145045.4:c.925G>T:p.[E309*]” and noted that it was absent from 238 controls. (alsaadi2014nonsensemutationin pages 1-2)
- Mechanistically, affected cells showed CCDC114 and ARMC4 “undetectable in the ciliary axonemes,” while reciprocal co-immunoprecipitation supported an ODAD3–CCDC114 interaction. (hjeij2014ccdc151mutationscause pages 15-16)

Overall, ODAD3-related PCD30 is a well-supported molecular diagnosis with a clear ODA-docking mechanism, but its disease-specific epidemiology and natural history remain severely underpowered. Knowledge-base assertions should retain provenance labels—**human ODAD3-specific**, **model-organism**, or **general-PCD extrapolation**—rather than treating all PCD statistics as subtype-specific.

References

1. (hjeij2014ccdc151mutationscause pages 1-2): Rim Hjeij, Alexandros Onoufriadis, Christopher M. Watson, Christopher E. Slagle, Nikolai T. Klena, Gerard W. Dougherty, Małgorzata Kurkowiak, Niki T. Loges, Christine P. Diggle, Nicholas F.C. Morante, George C. Gabriel, Kristi L. Lemke, You Li, Petra Pennekamp, Tabea Menchen, Franziska Konert, June Kehlet Marthin, Dorus A. Mans, Stef J.F. Letteboer, Claudius Werner, Thomas Burgoyne, Cordula Westermann, Andrew Rutman, Ian M. Carr, Christopher O’Callaghan, Eduardo Moya, Eddie M.K. Chung, Eamonn Sheridan, Kim G. Nielsen, Ronald Roepman, Kerstin Bartscherer, Rebecca D. Burdine, Cecilia W. Lo, Heymut Omran, and Hannah M. Mitchison. Ccdc151 mutations cause primary ciliary dyskinesia by disruption of the outer dynein arm docking complex formation. American Journal of Human Genetics, 95:257-274, Sep 2014. URL: https://doi.org/10.1016/j.ajhg.2014.08.005, doi:10.1016/j.ajhg.2014.08.005. This article has 209 citations and is from a highest quality peer-reviewed journal.

2. (hjeij2014ccdc151mutationscause pages 2-3): Rim Hjeij, Alexandros Onoufriadis, Christopher M. Watson, Christopher E. Slagle, Nikolai T. Klena, Gerard W. Dougherty, Małgorzata Kurkowiak, Niki T. Loges, Christine P. Diggle, Nicholas F.C. Morante, George C. Gabriel, Kristi L. Lemke, You Li, Petra Pennekamp, Tabea Menchen, Franziska Konert, June Kehlet Marthin, Dorus A. Mans, Stef J.F. Letteboer, Claudius Werner, Thomas Burgoyne, Cordula Westermann, Andrew Rutman, Ian M. Carr, Christopher O’Callaghan, Eduardo Moya, Eddie M.K. Chung, Eamonn Sheridan, Kim G. Nielsen, Ronald Roepman, Kerstin Bartscherer, Rebecca D. Burdine, Cecilia W. Lo, Heymut Omran, and Hannah M. Mitchison. Ccdc151 mutations cause primary ciliary dyskinesia by disruption of the outer dynein arm docking complex formation. American Journal of Human Genetics, 95:257-274, Sep 2014. URL: https://doi.org/10.1016/j.ajhg.2014.08.005, doi:10.1016/j.ajhg.2014.08.005. This article has 209 citations and is from a highest quality peer-reviewed journal.

3. (alsaadi2014nonsensemutationin pages 1-2): Muslim M. Alsaadi, A. Mesut Erzurumluoglu, Santiago Rodriguez, Philip A. I. Guthrie, Tom R. Gaunt, Hager Z. Omar, Mohammad Mubarak, Khalid K. Alharbi, Ammar C. Al-Rikabi, and Ian N. M. Day. Nonsense mutation in coiled-coil domain containing 151 gene (<i>ccdc151</i>) causes primary ciliary dyskinesia. Nov 2014. URL: https://doi.org/10.1002/humu.22698, doi:10.1002/humu.22698. This article has 47 citations and is from a domain leading peer-reviewed journal.

4. (OpenTargets Search: Primary ciliary dyskinesia-ODAD3,CCDC151): Open Targets Query (Primary ciliary dyskinesia-ODAD3,CCDC151, 3 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (hjeij2014ccdc151mutationscause pages 11-15): Rim Hjeij, Alexandros Onoufriadis, Christopher M. Watson, Christopher E. Slagle, Nikolai T. Klena, Gerard W. Dougherty, Małgorzata Kurkowiak, Niki T. Loges, Christine P. Diggle, Nicholas F.C. Morante, George C. Gabriel, Kristi L. Lemke, You Li, Petra Pennekamp, Tabea Menchen, Franziska Konert, June Kehlet Marthin, Dorus A. Mans, Stef J.F. Letteboer, Claudius Werner, Thomas Burgoyne, Cordula Westermann, Andrew Rutman, Ian M. Carr, Christopher O’Callaghan, Eduardo Moya, Eddie M.K. Chung, Eamonn Sheridan, Kim G. Nielsen, Ronald Roepman, Kerstin Bartscherer, Rebecca D. Burdine, Cecilia W. Lo, Heymut Omran, and Hannah M. Mitchison. Ccdc151 mutations cause primary ciliary dyskinesia by disruption of the outer dynein arm docking complex formation. American Journal of Human Genetics, 95:257-274, Sep 2014. URL: https://doi.org/10.1016/j.ajhg.2014.08.005, doi:10.1016/j.ajhg.2014.08.005. This article has 209 citations and is from a highest quality peer-reviewed journal.

6. (hjeij2014ccdc151mutationscause pages 15-16): Rim Hjeij, Alexandros Onoufriadis, Christopher M. Watson, Christopher E. Slagle, Nikolai T. Klena, Gerard W. Dougherty, Małgorzata Kurkowiak, Niki T. Loges, Christine P. Diggle, Nicholas F.C. Morante, George C. Gabriel, Kristi L. Lemke, You Li, Petra Pennekamp, Tabea Menchen, Franziska Konert, June Kehlet Marthin, Dorus A. Mans, Stef J.F. Letteboer, Claudius Werner, Thomas Burgoyne, Cordula Westermann, Andrew Rutman, Ian M. Carr, Christopher O’Callaghan, Eduardo Moya, Eddie M.K. Chung, Eamonn Sheridan, Kim G. Nielsen, Ronald Roepman, Kerstin Bartscherer, Rebecca D. Burdine, Cecilia W. Lo, Heymut Omran, and Hannah M. Mitchison. Ccdc151 mutations cause primary ciliary dyskinesia by disruption of the outer dynein arm docking complex formation. American Journal of Human Genetics, 95:257-274, Sep 2014. URL: https://doi.org/10.1016/j.ajhg.2014.08.005, doi:10.1016/j.ajhg.2014.08.005. This article has 209 citations and is from a highest quality peer-reviewed journal.

7. (goutaki2017theinternationalprimary pages 2-3): M. Goutaki, Elisabeth Maurer, F. Halbeisen, I. Amirav, A. Barbato, L. Behan, M. Boon, C. Casaulta, A. Clément, S. Crowley, E. Haarman, C. Hogg, B. Karadag, C. Koerner-Rettberg, M. Leigh, M. Loebinger, H. Mazurek, L. Morgan, K. Nielsen, H. Omran, N. Schwerk, S. Scigliano, C. Werner, P. Yiallouros, Z. Zivković, J. Lucas, and C. Kuehni. The international primary ciliary dyskinesia cohort (ipcd cohort): methods and first results. The European Respiratory Journal, Jan 2017. URL: https://doi.org/10.1183/13993003.01181-2016, doi:10.1183/13993003.01181-2016. This article has 81 citations.

8. (paff2021currentandfuture pages 1-2): Tamara Paff, Heymut Omran, Kim G. Nielsen, and Eric G. Haarman. Current and future treatments in primary ciliary dyskinesia. Sep 2021. URL: https://doi.org/10.3390/ijms22189834, doi:10.3390/ijms22189834. This article has 150 citations.

9. (halbeisen2018lungfunctionin pages 2-3): Florian S. Halbeisen, Myrofora Goutaki, Ben D. Spycher, Israel Amirav, Laura Behan, Mieke Boon, Claire Hogg, Carmen Casaulta, Suzanne Crowley, Eric G. Haarman, Bulent Karadag, Cordula Koerner-Rettberg, Michael R. Loebinger, Henryk Mazurek, Lucy Morgan, Kim G. Nielsen, Heymut Omran, Francesca Santamaria, Nicolaus Schwerk, Guillaume Thouvenin, Panayiotis Yiallouros, Jane S. Lucas, Philipp Latzin, and Claudia E. Kuehni. Lung function in patients with primary ciliary dyskinesia: an ipcd cohort study. European Respiratory Journal, 52:1801040, Jul 2018. URL: https://doi.org/10.1183/13993003.01040-2018, doi:10.1183/13993003.01040-2018. This article has 128 citations and is from a highest quality peer-reviewed journal.

10. (goutaki2017theinternationalprimary pages 6-7): M. Goutaki, Elisabeth Maurer, F. Halbeisen, I. Amirav, A. Barbato, L. Behan, M. Boon, C. Casaulta, A. Clément, S. Crowley, E. Haarman, C. Hogg, B. Karadag, C. Koerner-Rettberg, M. Leigh, M. Loebinger, H. Mazurek, L. Morgan, K. Nielsen, H. Omran, N. Schwerk, S. Scigliano, C. Werner, P. Yiallouros, Z. Zivković, J. Lucas, and C. Kuehni. The international primary ciliary dyskinesia cohort (ipcd cohort): methods and first results. The European Respiratory Journal, Jan 2017. URL: https://doi.org/10.1183/13993003.01181-2016, doi:10.1183/13993003.01181-2016. This article has 81 citations.

11. (hjeij2014ccdc151mutationscause pages 3-4): Rim Hjeij, Alexandros Onoufriadis, Christopher M. Watson, Christopher E. Slagle, Nikolai T. Klena, Gerard W. Dougherty, Małgorzata Kurkowiak, Niki T. Loges, Christine P. Diggle, Nicholas F.C. Morante, George C. Gabriel, Kristi L. Lemke, You Li, Petra Pennekamp, Tabea Menchen, Franziska Konert, June Kehlet Marthin, Dorus A. Mans, Stef J.F. Letteboer, Claudius Werner, Thomas Burgoyne, Cordula Westermann, Andrew Rutman, Ian M. Carr, Christopher O’Callaghan, Eduardo Moya, Eddie M.K. Chung, Eamonn Sheridan, Kim G. Nielsen, Ronald Roepman, Kerstin Bartscherer, Rebecca D. Burdine, Cecilia W. Lo, Heymut Omran, and Hannah M. Mitchison. Ccdc151 mutations cause primary ciliary dyskinesia by disruption of the outer dynein arm docking complex formation. American Journal of Human Genetics, 95:257-274, Sep 2014. URL: https://doi.org/10.1016/j.ajhg.2014.08.005, doi:10.1016/j.ajhg.2014.08.005. This article has 209 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Primary_Ciliary_Dyskinesia_30-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 37 |
| Resolved | 37 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 3 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 2 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014465` (2 mentions) - the report calls it "if available"; MONDO calls it **primary ciliary dyskinesia 30**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0003341` (1 mention) - the report calls it "GO biological process:** cilium movement"; GO calls it **cilium movement**
- `GO:0031514` (1 mention) - the report calls it "GO cellular component:** motile cilium"; GO calls it **motile cilium**