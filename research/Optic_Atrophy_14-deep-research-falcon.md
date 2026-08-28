---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-28T11:31:25.404877'
end_time: '2026-08-28T11:43:03.419597'
duration_seconds: 698.01
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Optic Atrophy 14 (MIEF1/MID51-related)
  mondo_id: MONDO:0957824
  category: Neurological Disorders
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
  on_topic: 5
  validator_version: 0.2.1
term_validation:
  total_terms: 13
  verified: 13
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0957824
    reported_labels:
    - if available
    ontology_label: optic atrophy 14
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Optic_Atrophy_14-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Optic Atrophy 14 (MIEF1/MID51-related)
- **MONDO ID:** MONDO:0957824 (if available)
- **Category:** Neurological Disorders

## Research Objectives

Please provide a comprehensive research report on **Optic Atrophy 14 (MIEF1/MID51-related)** covering all of the
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
- **Disease Name:** Optic Atrophy 14 (MIEF1/MID51-related)
- **MONDO ID:** MONDO:0957824 (if available)
- **Category:** Neurological Disorders

## Research Objectives

Please provide a comprehensive research report on **Optic Atrophy 14 (MIEF1/MID51-related)** covering all of the
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


# Optic Atrophy 14 (MIEF1/MID51-related): Comprehensive Disease-Characteristics Report

## Executive summary and evidence limits

Optic atrophy 14 (OPA14) is an ultra-rare, apparently autosomal-dominant mitochondrial-dynamics disorder caused by heterozygous variants in **MIEF1**, encoding the outer-mitochondrial-membrane protein MID51. Its defining phenotype is isolated, late-onset, progressive bilateral optic neuropathy, unusual among inherited optic neuropathies because peripheral visual-field loss precedes or exceeds central loss. The entire disease-defining clinical evidence retrieved traces to two women reported in 2021; consequently, frequencies calculated below describe that two-person series, not reliable population estimates. Open Targets recognizes the MIEF1–OPA14 association but likewise grounds its four evidence records in the same publication, PMID **33632269**. (OpenTargets Search: optic atrophy 14-MIEF1, charif2021dominantmutationsin pages 1-3)

The most important verified findings and evidence gaps are summarized here:

| domain | verified finding | quantitative details | evidence type/strength |
|---|---|---|---|
| disease identity | Optic atrophy 14 is a very rare inherited optic neuropathy associated with **MIEF1** (MID51); MONDO disease mapping supports the association. | MONDO:0957824; MIEF1 Ensembl **ENSG00000100335**; Open Targets association score **0.5659** with 4 evidence items tied to PMID 33632269. (OpenTargets Search: optic atrophy 14-MIEF1) | Curated disease-target database + primary human report; moderate for identity, limited by few cases. |
| Patient 1 | Female with late-adult onset, non-syndromic optic neuropathy featuring peripheral visual field loss progressing to central loss, optic disc pallor/excavation, abnormal VEP, normal ERG/retina. | Age **55**; origin **Maghreb**; first noted visual problem in **2002**; right-eye BVA **10/20** initially, by **2015** right eye **1/20**, left eye **18/20**; elevated sedimentation rate **44 mm**; no peripheral neuropathy reported. (charif2021dominantmutationsin pages 4-6, charif2021dominantmutationsin pages 3-4) | Primary human case report; strong for phenotype in this individual. |
| Patient 2 | Female with late-adult onset optic neuropathy after cesarean delivery, superior altitudinal/peripheral field loss, optic disc pallor/excavation, macular microcysts, severe RNFL loss, abnormal VEP, normal brain MRI/ENT. | Age **47**; born in **Egypt**; onset **2002**, **1 month after cesarean**; initial BVA right **3/20**, left **10/20**; by **2012** right **2/20**, left **8/20**; by **2015** right **hand moving**, left **4/20**; IOP right **9 mmHg**, left **10 mmHg**. (charif2021dominantmutationsin pages 4-6, charif2021dominantmutationsin pages 3-4) | Primary human case report; strong for phenotype in this individual. |
| genetics | Two heterozygous missense MIEF1 variants were identified and confirmed by Sanger sequencing; inheritance interpreted as dominant/monoallelic, but familial segregation data were not reported. | Patient 1: **c.718T>A, p.Y240N**, absent from cited databases; Patient 2: **c.436C>T, p.R146W**, **rs778124994**, gnomAD frequency **1.99e-5**; variants predicted damaging by **SIFT/PolyPhen** and disease-causing by **MutationTaster**. ClinVar records **RCV003387453/RCV003387454** released **2023-10-28**. (charif2021dominantmutationsin pages 3-4, OpenTargets Search: optic atrophy 14-MIEF1) | Primary human genetics + curated variant database; moderate-high for variant-disease link, limited by n=2 and absent segregation. |
| functional mechanism | Disease-linked MID51 variants do **not** disrupt mitochondrial localization or oligomerization, but **do** impair mitochondrial network dynamics/fusion in cell assays; p.Y240N lies in the DRP1-binding region. | Mutant proteins localized to mitochondria similarly to WT; oligomerization pattern retained; mito-PAGFP assays showed significantly reduced fusion versus WT; p.Y240 located in DRP1-binding loop **238-242**; MID51 is an outer mitochondrial membrane DRP1 adaptor. (charif2021dominantmutationsin pages 3-4, charif2021dominantmutationsin pages 6-8, atkins2016theroleof pages 1-2, atkins2016theroleof pages 8-9) | Disease-specific in vitro functional evidence + broader mechanistic literature; moderate-high for mechanism, indirect for retinal tissue. |
| epidemiology | Extremely rare cause of hereditary optic neuropathy; no population prevalence or incidence established. | In the original French unsolved ION cohort, **2/200** cases carried MIEF1 variants (**1.0%**). In a larger 2023 hereditary optic neuropathy dataset, MIEF1 accounted for **2 individuals** and ~**1.08%** of positive optic atrophy diagnoses in the relevant subgroup; overall positive diagnostic rate across 2,186 probands was **30%**. (charif2021dominantmutationsin pages 3-4, rocatcher2023thetop10 pages 2-3, rocatcher2023thetop10 pages 1-1) | Cohort-based observational evidence; moderate for rarity within referral cohorts, low for general-population frequency. |
| diagnosis | Current diagnosis relies on ophthalmic phenotyping plus molecular testing after exclusion of more common optic neuropathy causes; expanded gene panels improve detection of rare genes like MIEF1. | In both cases: normal retina, pale moderately excavated optic discs, abnormal VEP; Patient 2 had OCT evidence of RNFL collapse in all quadrants. Negative/normal workup included OPA1/OPA3/WFS1 and primary LHON mtDNA mutations, SNP array (no CNV/chromosomal abnormality/large ROH), anti-NMO and anti-MOG serology in Patient 2, and glaucoma-compatible findings absent at presentation. Initial study panel covered **22 genes** with **>95%** of bases at **>100X** coverage. (charif2021dominantmutationsin pages 4-6, charif2021dominantmutationsin pages 6-8, rocatcher2023thetop10 pages 2-3) | Primary clinical diagnostic evidence + cohort practice data; high for reported cases. |
| treatment | No disease-specific therapy, clinical trial, or formal management guideline was identified for MIEF1-related optic atrophy; care is supportive. | No treatment response data reported in the two cases. Reviews of inherited optic neuropathies discuss **idebenone** (approved for LHON in Europe), antioxidants, gene/RNA-based therapies, cysteamine, and NAD+ strategies, but **not as established therapy for MIEF1 optic atrophy**. (d’esposito2024insightsonthe pages 11-12, d’esposito2024insightsonthe pages 1-2, d’esposito2024insightsonthe pages 12-14) | Direct evidence absent for MIEF1; only low-strength extrapolation from broader optic neuropathy literature. |
| evidence gaps | Major unanswered questions remain on natural history, penetrance, segregation, sex effects, modifier genes, environmental triggers, pathology outside the optic nerve, and translational models. | Only **2 published disease-defining patients** were identified in retrieved evidence; no validated prevalence/incidence, no mortality/prognosis statistics, no disease-specific animal/iPSC/omics studies, no preventive factors, and no interventional trials found. (charif2021dominantmutationsin pages 3-4, d’esposito2024insightsonthe pages 12-14) | Strong evidence of knowledge scarcity; conclusions limited by ultra-rare case count. |


*Table: This table summarizes the verified evidence base for MIEF1/MID51-related optic atrophy, separating patient-level findings from broader mechanistic and epidemiologic evidence. It is useful for quickly identifying what is established, what is extrapolated, and what remains unknown.*

## 1. Disease information

### Definition

OPA14 is a nonsyndromic inherited optic neuropathy involving retinal ganglion-cell (RGC) degeneration, retinal nerve-fiber-layer (RNFL) loss, optic-disc pallor, visual-field constriction, and progressive visual impairment. The defining authors described it as an “unusual form of late-onset progressive optic neuropathy characterized by the initial loss of peripheral visual fields.” This contrasts with the central-to-peripheral field progression typical of most inherited optic neuropathies. (charif2021dominantmutationsin pages 1-3, charif2021dominantmutationsin pages 3-4)

### Identifiers and synonyms

- **MONDO:** MONDO:0957824, *optic atrophy 14*.
- **Causal target:** **MIEF1**, Ensembl **ENSG00000100335**, approved name *mitochondrial elongation factor 1*.
- **Protein/synonyms:** MID51, MiD51, mitochondrial dynamics protein 51; MIEF1-related optic neuropathy; dominant MIEF1-related optic atrophy.
- **Primary publication:** Charif et al., *Molecular Neurodegeneration*, published February 2021; PMID **33632269**; DOI and URL: https://doi.org/10.1186/s13024-021-00431-w. (charif2021dominantmutationsin pages 1-3, OpenTargets Search: optic atrophy 14-MIEF1)
- **ClinVar condition records:** RCV003387453 and RCV003387454, reported through Open Targets with release date 28 October 2023. (OpenTargets Search: optic atrophy 14-MIEF1)
- **OMIM:** the retrieved primary article gives MIEF1-related disease context but does not supply an OPA14 OMIM number; therefore none should be assigned from this evidence set.
- **Orphanet, ICD-10, ICD-11 and MeSH:** no disease-specific entries were verified. Broader codes for optic atrophy/hereditary optic neuropathy may be used clinically, but are not specific to OPA14.

The evidence consists of an aggregated disease-level ontology record linked to a primary, patient-level research cohort—not EHR-derived population data. Open Targets aggregates literature, Genomics England and EVA/ClinVar evidence, but all four association items cited the same human paper. (OpenTargets Search: optic atrophy 14-MIEF1)

## 2. Etiology, risk, protective and environmental factors

### Causal factor

The established cause is a **germline heterozygous MIEF1 missense variant** that perturbs MID51-dependent mitochondrial-network dynamics. Both reported variants were confirmed by Sanger sequencing. A monoallelic autosomal, non-imprinted model is recorded by Open Targets and is biologically consistent with the authors’ designation of dominant disease. However, familial segregation was not reported, so transmission versus de novo occurrence remains unresolved. (charif2021dominantmutationsin pages 3-4, OpenTargets Search: optic atrophy 14-MIEF1)

### Genetic risk factors

Two disease-associated variants are known from the defining report:

1. **NM_019008.5:c.718T>A; p.(Tyr240Asn), p.Y240N**, exon 6. It was absent from the databases queried in 2021 and affects the MID51 DRP1-binding region.
2. **NM_019008.5:c.436C>T; p.(Arg146Trp), p.R146W**, exon 5; dbSNP **rs778124994**; reported gnomAD allele frequency **1.99 × 10⁻⁵**. Arg146 is conserved with MID49, although no specific function was assigned to that region. (charif2021dominantmutationsin pages 3-4)

Both were predicted damaging by SIFT and PolyPhen and disease-causing by MutationTaster. These predictions are supporting—not independently decisive—evidence. Functional assays substantially strengthen causality, but the tiny case count and absent segregation require caution in asserting penetrance or a broad genotype–phenotype relationship. (charif2021dominantmutationsin pages 3-4)

No susceptibility loci, modifier genes, protective alleles, founder variants, anticipation, germline mosaicism, or carrier-frequency estimates have been established. Because this is dominant disease, “carrier” is not clinically equivalent to an unaffected recessive carrier; variant-positive relatives may instead have age-dependent or presently unquantified risk.

### Non-genetic factors and gene–environment interaction

No validated toxin, infection, dietary, smoking, alcohol, occupational, sex, or lifestyle risk factor is known. Patient 2 noticed loss one month after cesarean delivery, but a temporal association in one person does not establish pregnancy or surgery as a trigger. Patient 1 had seronegative rheumatoid polyarthritis treated with leflunomide; patient 2 had hypothyroidism, hypercholesterolemia and iron deficiency. Neither pattern was interpreted as causal. (charif2021dominantmutationsin pages 4-6)

No protective environmental factor or demonstrated gene–environment interaction exists. General avoidance of tobacco, excessive alcohol and known mitochondrial/optic-nerve toxins is biologically prudent in mitochondrial optic neuropathy, but this is extrapolation, not OPA14-specific evidence.

## 3. Phenotypes

Because only two patients are documented, “2/2” means the published series, not an estimated disease frequency.

- **Late-adult visual loss (symptom):** 2/2 women noticed visual dysfunction in adulthood; the clinical assessments occurred at ages 55 and 47. Onset was chronic/insidious in Patient 1 before an acute worsening and apparently sudden/painless in Patient 2. Suggested HPO: **Adult onset (HP:0003581)**, **Visual impairment (HP:0000505)**.
- **Painless bilateral optic neuropathy/atrophy (sign):** 2/2 had pale, moderately excavated optic discs and normal retina apart from Patient 2’s macular microcysts. Suggested HPO: **Optic atrophy (HP:0000648)**, **Bilateral optic atrophy** where supported by the current HPO release. (charif2021dominantmutationsin pages 3-4, charif2021dominantmutationsin pages 4-6)
- **Peripheral visual-field loss (functional sign):** 2/2; Patient 2 had severely narrowed isopters and a bilateral superior altitudinal defect. Peripheral-to-central evolution is the phenotype’s most discriminating feature. Suggested HPO: **Constricted visual fields (HP:0001133)** and **Visual field defect (HP:0001123)**. (charif2021dominantmutationsin pages 3-4, charif2021dominantmutationsin pages 4-6)
- **Reduced visual acuity (symptom/sign):** progressive and severe but variable between eyes. Suggested HPO: **Decreased visual acuity (HP:0007663)**.
- **RNFL loss (imaging sign):** documented by OCT in Patient 2, with collapse in all quadrants of both eyes. Suggested HPO: **Retinal nerve fiber layer thinning**, subject to current HPO term verification. (charif2021dominantmutationsin pages 4-6)
- **Abnormal VEP (electrophysiological abnormality):** strongly affected bilaterally in 2/2. Suggested HPO: **Abnormal visual evoked potentials (HP:0030453)**.
- **Normal photoreceptor function:** Patient 1’s scotopic and photopic ERGs were normal, supporting optic-nerve rather than generalized retinal disease. (charif2021dominantmutationsin pages 4-6)
- **Macular microcysts:** present in Patient 2 only (1/2); likely secondary to severe optic neuropathy rather than defining macular dystrophy. Suggested HPO: **Cystoid macular edema (HP:0011505)** only if the clinical morphology satisfies that term.
- **Extraocular neurological/systemic disease:** no additional neurological or neuromuscular syndrome was observed in either patient. Peripheral neuropathy was absent in Patient 1; Patient 2 had no diabetes, epilepsy or neuromuscular disorder, and normal brain MRI and ENT examination. (charif2021dominantmutationsin pages 3-4, charif2021dominantmutationsin pages 4-6)

### Patient-level course

**Patient 1:** Maghreb-origin woman, age 55. A faint right-eye problem was noticed in 2002 with best visual acuity (BVA) 10/20. In 2015 she developed acute painless loss, mainly peripheral in both eyes and central in the right: right 1/20, left 18/20. VEPs were strongly abnormal; ERGs and retina were normal. (charif2021dominantmutationsin pages 4-6)

**Patient 2:** Egyptian-born woman, age 47, without youthful visual complaints. One month after an uneventful cesarean delivery in 2002, painless loss began in the right eye (3/20), then left (10/20). Acuity progressed to 2/20 and 8/20 in 2012, and hand-motion and 4/20 in 2015. OCT showed bilateral RNFL collapse; IOP was 9/10 mmHg, VEPs were severely affected, and MRI was normal. (charif2021dominantmutationsin pages 4-6)

### Quality of life

No EQ-5D, SF-36, PROMIS or disease-specific quality-of-life instrument was reported. Nevertheless, hand-motion vision in one eye, marked field constriction and bilateral acuity loss imply substantial limitations in mobility, driving, reading and occupational independence. Those functional consequences are clinically plausible but were not quantitatively assessed.

## 4. Genetic and molecular information

**Gene:** MIEF1; transcript used in the report **NM_019008.5**; protein MID51. The retrieved evidence does not provide a verified HGNC numeric identifier, so it is not inferred here. (charif2021dominantmutationsin pages 3-4)

**Variant class:** both are germline heterozygous missense substitutions. No frameshift, nonsense, splice, structural, somatic or chromosomal cause of OPA14 has been demonstrated. SNP-array testing in both patients found no chromosomal abnormality, copy-number variant or large homozygous interval. (charif2021dominantmutationsin pages 4-6)

**Functional consequence:** the data support an altered-function mechanism rather than simple mistargeting or failure to oligomerize. Both proteins reached mitochondria and formed monomers, dimers, tetramers and rare high-molecular-weight species similarly to wild type, but failed to produce the wild-type increase in mitochondrial fusion and disrupted network dynamics. p.Y240N directly affects the DRP1-interacting loop at residues 238–242. Whether the human disease mechanism is dominant-negative, partial loss of regulatory function, or another gain-of-abnormal-function effect remains unproven. (charif2021dominantmutationsin pages 3-4, charif2021dominantmutationsin pages 6-8)

No modifier-gene, methylation, histone, chromatin, repeat-expansion or disease-specific epigenetic evidence is available.

## 5. Environmental information

No environmental toxin, ionizing radiation, pollution, occupational exposure, lifestyle behavior or infectious agent has been causally implicated. Lyme and Treponema serology were normal in Patient 1; anti-NMO and anti-MOG tests were negative in Patient 2. These findings helped exclude acquired inflammatory/infectious mimics rather than identify causal exposures. (charif2021dominantmutationsin pages 4-6)

## 6. Mechanism and pathophysiology

### Disease-specific causal chain

1. **Upstream trigger:** heterozygous p.Y240N or p.R146W MID51 substitution.
2. **Protein-level defect:** preserved outer-mitochondrial-membrane targeting and self-oligomerization, but impaired regulation of mitochondrial fusion/fission dynamics.
3. **Organelle-level consequence:** reduced mitochondrial fusion events relative to wild-type MID51 and disrupted network remodeling in live-cell mito-PAGFP assays.
4. **Cell vulnerability:** RGCs and their long axons have unusually high ATP requirements and substantial unmyelinated intra-retinal segments; current expert reviews therefore regard mitochondrial energetic/dynamic failure and oxidative stress as central vulnerabilities.
5. **Tissue injury:** RGC/axon degeneration produces RNFL collapse, optic-disc pallor, abnormal VEPs, peripheral field loss and eventually severe acuity loss. (charif2021dominantmutationsin pages 1-3, charif2021dominantmutationsin pages 3-4, charif2021dominantmutationsin pages 4-6, d’esposito2024insightsonthe pages 2-4)

### MID51 biology

MID51 is an integral outer-mitochondrial-membrane DRP1 adaptor. Its N-terminal transmembrane region anchors it, while a cytosolic nucleotidyltransferase-like domain binds ADP. General mechanistic studies indicate that ADP-bound MID51 stimulates DRP1 GTPase activity and oligomerization, connecting metabolic state to fission. Expression context matters: endogenous MID51 can organize productive DRP1 fission complexes, whereas overexpression can sequester inactive DRP1 and produce apparent mitochondrial elongation/fusion. This context dependence cautions against reducing OPA14 to simply “too much” or “too little” fission. (atkins2016theroleof pages 1-2, atkins2016theroleof pages 8-9, simpson2023posttranslationalcontrolof pages 52-57)

Suggested ontology annotations include:

- **GO biological process:** mitochondrial fission; mitochondrial fusion; regulation of mitochondrial organization; mitochondrial morphogenesis; mitophagy; cellular response to oxidative stress; neuron apoptotic process.
- **GO cellular component:** mitochondrion; mitochondrial outer membrane; mitochondrial fission site; mitochondria-associated ER membrane.
- **GO molecular function:** DRP1 binding/protein binding; adenyl ribonucleotide binding.
- **Cell Ontology:** **retinal ganglion cell (CL:0000740)** as the primary vulnerable cell; HeLa cell is the experimental system, not a disease-relevant retinal cell.

There is no direct OPA14 evidence for immune-mediated pathology, respiratory-chain enzyme deficiency, altered metabolites/lipids, apoptosis measurements, mitophagy flux, mtDNA instability, transcriptomic signatures or RGC-specific bioenergetics. Those remain plausible downstream research areas rather than established annotations.

### Molecular profiling and advanced technologies

No disease-specific RNA-seq, single-cell sequencing, spatial transcriptomics, proteomics, metabolomics, lipidomics, methylomics, CRISPR screen, patient-derived iPSC, retinal organoid or multi-omics study was identified. The only functional system was transient expression of tagged wild-type or mutant MID51 in HeLa cells, assessed by confocal microscopy, immunoprecipitation and mito-PAGFP fusion assays. (charif2021dominantmutationsin pages 3-4, charif2021dominantmutationsin pages 6-8)

## 7. Anatomical structures affected

- **Primary organ/system:** eye and visual nervous system.
- **Primary cells/tissue:** RGCs and their axons; retinal nerve-fiber layer; optic-nerve head and optic nerve.
- **Laterality:** bilateral in both reported patients, with asymmetric severity in Patient 1 and more symmetric progression in Patient 2.
- **Retina:** structurally normal overall; Patient 2 had macular microcysts, while Patient 1 had normal photopic/scotopic ERGs.
- **Brain and other organs:** no demonstrated primary involvement; Patient 2’s brain MRI was normal. (charif2021dominantmutationsin pages 3-4, charif2021dominantmutationsin pages 4-6)

Suggested anatomy terms: **UBERON:0000966 retina**, **UBERON:0001785 retinal nerve fiber layer**, **UBERON:0000962 optic nerve**, and mitochondrial outer membrane as the relevant GO cellular compartment. Exact identifiers should be release-validated before database import.

## 8. Temporal development

OPA14 appears to be a chronic, lifelong, progressive disorder with late-adult clinical recognition. A latent peripheral-field defect may precede perceived acuity loss by years. The reported course combines insidious early dysfunction with sudden painless subjective worsening, followed by continued progression over 10–13 years. Patient 1 preserved good left-eye acuity despite severe right-eye disease; Patient 2 progressed bilaterally to profound impairment. No remission, episodic recovery or treatment-induced improvement was documented. (charif2021dominantmutationsin pages 3-4, charif2021dominantmutationsin pages 4-6)

No formal staging system or progression-rate model exists. A practical observational scheme would be: early peripheral-field constriction; intermediate bilateral field/acuity involvement with disc pallor; advanced severe RNFL loss and profound visual impairment. This is a proposed clinical abstraction, not a validated scale.

## 9. Inheritance and population

Inheritance is classified as **autosomal dominant/monoallelic**, but the evidence is based on heterozygosity and functional studies rather than reported multigenerational segregation. Penetrance, age dependence, expressivity across families, de novo rate, parental mosaicism, anticipation and reproductive fitness are unknown. (OpenTargets Search: optic atrophy 14-MIEF1)

The original study found MIEF1 variants in **2/200 (1.0%)** French molecularly unresolved inherited-optic-neuropathy referrals. This is a selected-cohort diagnostic fraction, not prevalence. (charif2021dominantmutationsin pages 3-4)

A 2023 analysis of 2,186 hereditary-optic-neuropathy probands reported an overall molecular diagnosis in 30%; the autosomal subgroup had 451 diagnoses among 1,680 referrals, and ten major genes accounted for 96% of those diagnoses. MIEF1 appeared in only two individuals among the rare-gene findings, confirming that it is a minor diagnostic contributor. Reported “1.08%” refers to the relevant diagnosed subgroup, not the general population. (rocatcher2023thetop10 pages 2-3, rocatcher2023thetop10 pages 1-1)

Population prevalence, annual incidence, geographic distribution, ancestry-specific enrichment and sex ratio cannot be estimated. Both known patients were women—one of Maghreb origin and one born in Egypt—but n=2 cannot support a female predisposition or North African founder effect.

## 10. Diagnostics

### Clinical evaluation

The phenotype should prompt neuro-ophthalmic assessment comprising best-corrected acuity, color vision, pupils, slit-lamp examination, IOP, dilated funduscopy, automated and/or kinetic perimetry, optic-disc/RNFL and macular OCT, and VEP. ERG is useful when retinal dystrophy is a concern. Color-vision data were not reported in the defining cases. MRI of brain/orbits with contrast and inflammatory/infectious testing should be guided by presentation, particularly for acute or asymmetric loss.

Findings supporting OPA14 are bilateral pale/excavated discs with normal IOP, marked peripheral or superior-altitudinal field loss, progressive RNFL thinning and severely abnormal VEP despite an otherwise normal retina. (charif2021dominantmutationsin pages 3-4, charif2021dominantmutationsin pages 4-6)

### Molecular testing

1. Exclude common mitochondrial and nuclear optic-neuropathy causes using a comprehensive hereditary optic-neuropathy panel that includes **MIEF1**, **OPA1, OPA3, WFS1, ACO2, SPG7, MFN2, AFG3L2, RTN4IP1, TMEM126A, NR2F1, FDXR, DNM1L, MFF**, and relevant mtDNA variants.
2. Confirm candidate MIEF1 variants by an orthogonal method and perform parental/relative testing for segregation and penetrance assessment.
3. If panel testing is negative, WES/WGS can identify newly recognized genes, intronic variants, mtDNA changes and structural variants, subject to assay validation.
4. CMA is reasonable when syndromic features or developmental abnormalities suggest a copy-number disorder; it was negative in both OPA14 cases. Karyotyping/FISH, repeat-expansion testing and liquid biopsy are not routine OPA14 tests. (charif2021dominantmutationsin pages 4-6, charif2021dominantmutationsin pages 6-8, rocatcher2023thetop10 pages 2-3)

The original 22-gene panel achieved >100× coverage for 95% of targeted bases, with Sanger fill-in of poorly covered regions. Modern broader panels or exome/genome sequencing are preferable because the 2023 cohort demonstrated extensive locus heterogeneity. (charif2021dominantmutationsin pages 4-6, rocatcher2023thetop10 pages 1-1)

### Differential diagnosis

Important alternatives include OPA1-dominant optic atrophy, LHON, WFS1/ACO2/MFN2/SPG7/AFG3L2-related neuropathies, glaucoma, toxic/nutritional optic neuropathy, compressive lesions, ischemic optic neuropathy, neuromyelitis-optica-spectrum disorder, MOG-associated disease and infectious optic neuropathy. Peripheral-to-central field progression, normal IOP, absent disc edema and a pathogenic functional MIEF1 variant favor OPA14, but no consensus diagnostic criteria exist. (charif2021dominantmutationsin pages 3-4, charif2021dominantmutationsin pages 4-6)

### Screening

There is no newborn or population screening. Once a credible pathogenic familial variant is established, targeted cascade testing with pre-test counseling and baseline/serial ophthalmic assessment is appropriate. Testing asymptomatic minors requires individualized consideration because onset appears adult and no preventive therapy is proven.

## 11. Outcome and prognosis

The documented outcome is progressive, irreversible visual morbidity. Over approximately 13 years, Patient 2 reached hand-motion vision in the right eye and 4/20 in the left; Patient 1 reached 1/20 in the right while retaining 18/20 in the left. Thus, severe bilateral disability is possible, but asymmetry and retained useful vision can occur. (charif2021dominantmutationsin pages 3-4, charif2021dominantmutationsin pages 4-6)

No survival, mortality, life-expectancy, recovery-rate or validated prognostic-biomarker data exist. Neither patient had a life-limiting neurological syndrome, so available evidence supports vision-dominant morbidity rather than reduced survival. Prognostic inference from variant, onset age, OCT thickness or initial visual field is currently impossible.

## 12. Treatment and current implementation

No pharmacological, surgical, gene, cell, RNA or immune therapy is approved or clinically validated specifically for OPA14. No MIEF1-specific interventional trial or treatment-response series was identified. The 2021 report describes clinical progression, not a therapeutic intervention. (charif2021dominantmutationsin pages 3-4, charif2021dominantmutationsin pages 4-6)

Current real-world management is therefore supportive:

- periodic neuro-ophthalmic follow-up with acuity, fields and OCT;
- low-vision rehabilitation, optical/electronic aids, orientation-and-mobility training and occupational accommodations;
- management of reversible coincident deficiencies and avoidance of recognized optic-nerve toxins;
- genetic counseling and cascade testing;
- psychological and social support for progressive visual disability.

Suggested NCIT-level intervention concepts include **Genetic Counseling**, **Genetic Testing**, **Ophthalmologic Examination**, **Optical Coherence Tomography**, **Visual Field Test**, **Low Vision Rehabilitation**, and **Assistive Device**; identifiers should be checked against the target NCIT release.

Recent 2023–2024 reviews discuss idebenone, coenzyme Q10, cysteamine/NAD⁺ strategies, AAV gene therapy, CRISPR and RNA therapies for other optic neuropathies. Idebenone is approved in Europe for LHON—not MIEF1 disease—and none should be prescribed as OPA14-directed therapy without evidence or a protocol. Experts emphasize integrating genotype and phenotype while recognizing that mitochondrial-dynamics therapeutics remain investigational. (d’esposito2024insightsonthe pages 11-12, d’esposito2024insightsonthe pages 1-2, d’esposito2024insightsonthe pages 12-14)

## 13. Prevention

Primary prevention by lifestyle change, immunization or prophylactic medication is unavailable because OPA14 is genetic. Reproductive options after identification of a well-supported familial variant include genetic counseling, prenatal diagnosis and preimplantation genetic testing; these require discussion of uncertain penetrance and the limited variant evidence.

Secondary prevention consists of cascade testing and surveillance to detect presymptomatic field/RNFL changes, although no study proves that early detection alters progression. Tertiary prevention centers on low-vision care, fall-risk reduction, workplace adaptation and avoiding additional acquired optic-nerve injury. Vaccination and infectious-disease public-health measures have no disease-specific role.

## 14. Other species and natural disease

No naturally occurring MIEF1-related optic atrophy was identified in companion animals, livestock or wildlife, and there is no zoonotic or cross-species transmission. MIEF1/MID51 biology is evolutionarily conserved among vertebrates, but conservation alone is not evidence of a homologous veterinary disorder. NCBI Taxon identifiers relevant to future comparative work include **Homo sapiens: 9606** and **Mus musculus: 10090**; ortholog gene IDs should be verified directly in the current NCBI Gene release before import.

## 15. Model organisms and research models

The disease-defining model was **transfected HeLa cells**, not an organismal or retinal model. Tagged p.Y240N and p.R146W proteins were tested for mitochondrial localization, oligomerization and fusion/network behavior by live-cell confocal microscopy and mito-PAGFP. This model provides strong evidence for variant-dependent organelle dysfunction but cannot reproduce RGC identity, optic-nerve architecture, age-dependent penetrance, visual-field loss or long-term neurodegeneration. (charif2021dominantmutationsin pages 3-4, charif2021dominantmutationsin pages 6-8)

No OPA14-specific knock-in/knockout mouse, rat, zebrafish, Drosophila, C. elegans, yeast, patient fibroblast, iPSC-RGC or retinal organoid model was identified. Priority models are heterozygous p.Y240N and p.R146W knock-in animals and patient-derived iPSC-RGCs, with endpoints including DRP1 recruitment, mitochondrial transport/fission/fusion, mitophagy, ATP/ROS, axonal survival, RNFL thickness and visual function.

## Recent developments and expert interpretation

The principal post-discovery development is diagnostic rather than therapeutic. The 2023, 2,186-proband study showed that comprehensive sequencing produces a 30% overall diagnostic rate, while MIEF1 remains among the individually rare contributors; this supports retaining MIEF1 on broad optic-neuropathy panels rather than using it as first-line single-gene testing. (rocatcher2023thetop10 pages 2-3, rocatcher2023thetop10 pages 1-1)

A 2024 review reinforced high energetic demand, mitochondrial dysfunction and oxidative stress as central to RGC vulnerability and highlighted genotype–phenotype integration and emerging molecular therapies. None of those advances has yet produced an OPA14-specific intervention. (d’esposito2024insightsonthe pages 11-12, d’esposito2024insightsonthe pages 1-2, d’esposito2024insightsonthe pages 2-4)

## Knowledge-base confidence statement

**High confidence:** MIEF1 association; the two reported variants and patient phenotypes; bilateral late-onset peripheral-field-predominant optic neuropathy; abnormal MID51 network regulation in HeLa-cell assays.

**Moderate confidence:** autosomal-dominant mechanism and nonsyndromic classification, because familial segregation and broader natural history remain unavailable.

**Low or insufficient evidence:** penetrance, population epidemiology, sex/ancestry effects, variant-specific prognosis, environmental triggers, protective factors, biochemical biomarkers, treatment, prevention of progression, advanced omics and organismal models.

### Key primary-source quotation

The disease-defining abstract states: “Using targeted sequencing of genes involved in mitochondrial dynamics, we report the first heterozygous variants in MIEF1 linked to disease, which cause an unusual form of late-onset progressive optic neuropathy characterized by the initial loss of peripheral visual fields.” It further reports that the variants “do not disrupt MID51’s localization to the outer mitochondrial membrane or its oligomerization, but rather, significantly disrupt mitochondrial network dynamics.” (charif2021dominantmutationsin pages 1-3)

References

1. (OpenTargets Search: optic atrophy 14-MIEF1): Open Targets Query (optic atrophy 14-MIEF1, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (charif2021dominantmutationsin pages 1-3): Majida Charif, Yvette C. Wong, Soojin Kim, Agnès Guichet, Catherine Vignal, Xavier Zanlonghi, Philippe Bensaid, Vincent Procaccio, Dominique Bonneau, Patrizia Amati-Bonneau, Pascal Reynier, Dimitri Krainc, and Guy Lenaers. Dominant mutations in mief1 affect mitochondrial dynamics and cause a singular late onset optic neuropathy. Molecular Neurodegeneration, Feb 2021. URL: https://doi.org/10.1186/s13024-021-00431-w, doi:10.1186/s13024-021-00431-w. This article has 20 citations and is from a highest quality peer-reviewed journal.

3. (charif2021dominantmutationsin pages 4-6): Majida Charif, Yvette C. Wong, Soojin Kim, Agnès Guichet, Catherine Vignal, Xavier Zanlonghi, Philippe Bensaid, Vincent Procaccio, Dominique Bonneau, Patrizia Amati-Bonneau, Pascal Reynier, Dimitri Krainc, and Guy Lenaers. Dominant mutations in mief1 affect mitochondrial dynamics and cause a singular late onset optic neuropathy. Molecular Neurodegeneration, Feb 2021. URL: https://doi.org/10.1186/s13024-021-00431-w, doi:10.1186/s13024-021-00431-w. This article has 20 citations and is from a highest quality peer-reviewed journal.

4. (charif2021dominantmutationsin pages 3-4): Majida Charif, Yvette C. Wong, Soojin Kim, Agnès Guichet, Catherine Vignal, Xavier Zanlonghi, Philippe Bensaid, Vincent Procaccio, Dominique Bonneau, Patrizia Amati-Bonneau, Pascal Reynier, Dimitri Krainc, and Guy Lenaers. Dominant mutations in mief1 affect mitochondrial dynamics and cause a singular late onset optic neuropathy. Molecular Neurodegeneration, Feb 2021. URL: https://doi.org/10.1186/s13024-021-00431-w, doi:10.1186/s13024-021-00431-w. This article has 20 citations and is from a highest quality peer-reviewed journal.

5. (charif2021dominantmutationsin pages 6-8): Majida Charif, Yvette C. Wong, Soojin Kim, Agnès Guichet, Catherine Vignal, Xavier Zanlonghi, Philippe Bensaid, Vincent Procaccio, Dominique Bonneau, Patrizia Amati-Bonneau, Pascal Reynier, Dimitri Krainc, and Guy Lenaers. Dominant mutations in mief1 affect mitochondrial dynamics and cause a singular late onset optic neuropathy. Molecular Neurodegeneration, Feb 2021. URL: https://doi.org/10.1186/s13024-021-00431-w, doi:10.1186/s13024-021-00431-w. This article has 20 citations and is from a highest quality peer-reviewed journal.

6. (atkins2016theroleof pages 1-2): Kathleen Atkins, Asish Dasgupta, Kuang-Hueih Chen, Jeff Mewburn, and Stephen L. Archer. The role of drp1 adaptor proteins mid49 and mid51 in mitochondrial fission: implications for human disease. Clinical science, 130 21:1861-74, Nov 2016. URL: https://doi.org/10.1042/cs20160030, doi:10.1042/cs20160030. This article has 142 citations and is from a peer-reviewed journal.

7. (atkins2016theroleof pages 8-9): Kathleen Atkins, Asish Dasgupta, Kuang-Hueih Chen, Jeff Mewburn, and Stephen L. Archer. The role of drp1 adaptor proteins mid49 and mid51 in mitochondrial fission: implications for human disease. Clinical science, 130 21:1861-74, Nov 2016. URL: https://doi.org/10.1042/cs20160030, doi:10.1042/cs20160030. This article has 142 citations and is from a peer-reviewed journal.

8. (rocatcher2023thetop10 pages 2-3): Aude Rocatcher, Valérie Desquiret-Dumas, Majida Charif, Marc Ferré, Philippe Gohier, Delphine Mirebeau-Prunier, Christophe Verny, Dan Milea, Guy Lenaers, Catherine Vignal, Cédric Lamirel, Rabih Hage, Hélène Dollfus, Isabelle Meunier, Xavier Zanlonghi, Valérie Touitou, Pierre Lebranchu, Sylvie Odent, Caroline Froment Tilikete, Luc Jeanjean, Sabine Defoort-Dhellemmes, Isabelle Drumare-Bouvet, Vasily Smirnov, Catherine Vincent-Delorme, Damien Biotti, Fanny Varenne, Patrick Calvas, Nicolas Chassaing, Mickael Cohen, Christophe Orssaud, Fanny Mochel, Agathe Roubertie, Annick Toutain, Frédéric Pollet-Villard, Marie Noelle Bonnet Dupeyron, Céline Boulicot, Béatrice Cochener, Alice Goldenberg, Marie Line Jacquemont, Christine Francannet, Dominique Bonneau, Pascal Reynier, and Patrizia Amati-Bonneau. The top 10 most frequently involved genes in hereditary optic neuropathies in 2186 probands. Brain : a journal of neurology, 146:455-460, Nov 2023. URL: https://doi.org/10.1093/brain/awac395, doi:10.1093/brain/awac395. This article has 53 citations.

9. (rocatcher2023thetop10 pages 1-1): Aude Rocatcher, Valérie Desquiret-Dumas, Majida Charif, Marc Ferré, Philippe Gohier, Delphine Mirebeau-Prunier, Christophe Verny, Dan Milea, Guy Lenaers, Catherine Vignal, Cédric Lamirel, Rabih Hage, Hélène Dollfus, Isabelle Meunier, Xavier Zanlonghi, Valérie Touitou, Pierre Lebranchu, Sylvie Odent, Caroline Froment Tilikete, Luc Jeanjean, Sabine Defoort-Dhellemmes, Isabelle Drumare-Bouvet, Vasily Smirnov, Catherine Vincent-Delorme, Damien Biotti, Fanny Varenne, Patrick Calvas, Nicolas Chassaing, Mickael Cohen, Christophe Orssaud, Fanny Mochel, Agathe Roubertie, Annick Toutain, Frédéric Pollet-Villard, Marie Noelle Bonnet Dupeyron, Céline Boulicot, Béatrice Cochener, Alice Goldenberg, Marie Line Jacquemont, Christine Francannet, Dominique Bonneau, Pascal Reynier, and Patrizia Amati-Bonneau. The top 10 most frequently involved genes in hereditary optic neuropathies in 2186 probands. Brain : a journal of neurology, 146:455-460, Nov 2023. URL: https://doi.org/10.1093/brain/awac395, doi:10.1093/brain/awac395. This article has 53 citations.

10. (d’esposito2024insightsonthe pages 11-12): Fabiana D’Esposito, Marco Zeppieri, Maria Francesca Cordeiro, Matteo Capobianco, Alessandro Avitabile, Giuseppe Gagliano, Mutali Musa, Piero Barboni, and Caterina Gagliano. Insights on the genetic and phenotypic complexities of optic neuropathies. Genes, 15(12):1559, Nov 2024. URL: https://doi.org/10.3390/genes15121559, doi:10.3390/genes15121559. This article has 12 citations.

11. (d’esposito2024insightsonthe pages 1-2): Fabiana D’Esposito, Marco Zeppieri, Maria Francesca Cordeiro, Matteo Capobianco, Alessandro Avitabile, Giuseppe Gagliano, Mutali Musa, Piero Barboni, and Caterina Gagliano. Insights on the genetic and phenotypic complexities of optic neuropathies. Genes, 15(12):1559, Nov 2024. URL: https://doi.org/10.3390/genes15121559, doi:10.3390/genes15121559. This article has 12 citations.

12. (d’esposito2024insightsonthe pages 12-14): Fabiana D’Esposito, Marco Zeppieri, Maria Francesca Cordeiro, Matteo Capobianco, Alessandro Avitabile, Giuseppe Gagliano, Mutali Musa, Piero Barboni, and Caterina Gagliano. Insights on the genetic and phenotypic complexities of optic neuropathies. Genes, 15(12):1559, Nov 2024. URL: https://doi.org/10.3390/genes15121559, doi:10.3390/genes15121559. This article has 12 citations.

13. (d’esposito2024insightsonthe pages 2-4): Fabiana D’Esposito, Marco Zeppieri, Maria Francesca Cordeiro, Matteo Capobianco, Alessandro Avitabile, Giuseppe Gagliano, Mutali Musa, Piero Barboni, and Caterina Gagliano. Insights on the genetic and phenotypic complexities of optic neuropathies. Genes, 15(12):1559, Nov 2024. URL: https://doi.org/10.3390/genes15121559, doi:10.3390/genes15121559. This article has 12 citations.

14. (simpson2023posttranslationalcontrolof pages 52-57): Post-translational control of mitochondria by Fbxo7 in Parkinson's disease This article has 0 citations.

## Artifacts

- [Edison artifact artifact-00](Optic_Atrophy_14-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0957824` (3 mentions) - the report calls it "if available"; MONDO calls it **optic atrophy 14**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000740` (1 mention) - the report calls it "Cell Ontology:** **retinal ganglion cell"; CL calls it **retinal ganglion cell**