---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-28T15:04:34.417236'
end_time: '2026-08-28T15:17:15.099605'
duration_seconds: 760.68
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Diphtheria
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 37
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 2
  off_topic: 1
  off_topic_references:
  - DOI:10.1128/spectrum.00006-23
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 61
  verified: 57
  not_found: 0
  obsolete: 2
  unverifiable: 2
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0005015
    reported_labels:
    - diphtheria; verify against the current MONDO release
    ontology_label: diabetes mellitus
  obsolete_terms:
  - term_id: GO:0009405
    ontology_label: obsolete pathogenesis
  - term_id: GO:0006471
    ontology_label: obsolete protein ADP-ribosylation
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Diphtheria-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Diphtheria
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Diphtheria** covering all of the
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
- **Disease Name:** Diphtheria
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Diphtheria** covering all of the
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


# Diphtheria: comprehensive disease-characteristics report

**Scope and evidence note.** Diphtheria is an infectious, toxin-mediated disease rather than a Mendelian disorder. Accordingly, pathogen genetics, toxigenicity, immunity, exposure, and health-system factors are much more relevant than human causal variants. Evidence below is labeled where useful as **human clinical**, **laboratory/in-vitro**, **animal**, or **surveillance/review**. Publication dates and DOI URLs are supplied for the major retrieved sources; several requested ontology mappings are curator suggestions and should be validated against the current ontology release.

| Domain | Key facts | Quantitative/current evidence | Suggested ontology terms |
|---|---|---|---|
| Etiology / transmission | Acute toxin-mediated bacterial infection classically caused by toxigenic *Corynebacterium diphtheriae*; other CdSC species, especially *C. ulcerans* and rarely *C. pseudotuberculosis*, can produce diphtheria toxin. Transmission is mainly respiratory droplets for respiratory disease and direct/indirect contact for cutaneous disease; zoonotic transmission is important for *C. ulcerans*. Incubation usually 2–5 days. (osarenren2024globalstrategiesfor pages 2-4, prygiel2022newcorynebacteriumspecies pages 1-2, chene2024cutaneousdiphtheriafrom pages 1-2, museux2023corynebacteriaofthe pages 1-2) | 2024 review reported 27,991 suspected cases and 828 deaths across 5 African countries; untreated contagious period 2–3 weeks vs ~1 day after antibiotics in cited review synthesis. In French cutaneous cohort, 39% of isolates were toxigenic; species were *C. diphtheriae* 77% and *C. ulcerans* 23%. (osarenren2024globalstrategiesfor pages 2-4, chene2024cutaneousdiphtheriafrom pages 1-2) | MONDO: diphtheria; MeSH: Diphtheria; NCIT: Infectious Process; NCBITaxon: *C. diphtheriae*, *C. ulcerans* |
| Phenotypes | Core respiratory phenotype: sore throat/pharyngitis, low-grade fever, adherent gray-white pseudomembrane, cervical lymphadenopathy, “bull neck,” dysphagia, airway obstruction. Cutaneous phenotype: chronic ulcer or nonhealing wound, often on limbs, sometimes with gray membrane. Major complications: myocarditis, neuritis/polyneuropathy, respiratory failure. (muhammed2018diphtheriathestrangling pages 2-3, chene2024cutaneousdiphtheriafrom pages 1-2, museux2023corynebacteriaofthe pages 1-2, dinanti2024determinantsofmortality pages 1-2) | In French cutaneous cohort: lower limbs 86.9%, ulcerations 82%, polymicrobial lesions 88.9%. In a 2024 pediatric mortality study, myocarditis and airway obstruction were significantly associated with death; airway obstruction carried ~13-fold higher mortality odds. (chene2024cutaneousdiphtheriafrom pages 1-2, dinanti2024determinantsofmortality pages 1-2) | HPO: HP:0030247 Pseudomembranous pharyngitis; HP:0002039 Dysphagia; HP:0001644 Dilated cardiomyopathy / myocarditis-related cardiac dysfunction; HP:0001257 Spasticity not appropriate—prefer HP:0009830 Peripheral neuropathy; HP:0012735 Cutaneous ulcer; HP:0000456 Neck swelling |
| Mechanism / pathophysiology | Disease has two linked layers: local mucosal/skin infection and systemic toxemia. Diphtheria toxin is phage-encoded, secreted by lysogenized strains; receptor-binding domain binds HB-EGF/proHB-EGF, toxin enters via receptor-mediated endocytosis, acidic endosome enables translocation, catalytic domain ADP-ribosylates EF-2, blocking protein synthesis and causing cell death. Toxin expression is regulated in part by DtxR and iron availability. (wenzel2020humanantibodiesneutralizing pages 1-2, prygiel2022newcorynebacteriumspecies pages 1-2, cerdenotarraga2003thecompletegenome pages 1-2) | DT is a 535-aa, ~58 kDa polypeptide with catalytic, transmembrane, and receptor-binding domains. Genome studies show acquisition of tox plus iron-uptake, adhesin, and fimbrial determinants. NTTB strains exist and may be tox-positive but non-expressing. (wenzel2020humanantibodiesneutralizing pages 1-2, prygiel2022newcorynebacteriumspecies pages 1-2, cerdenotarraga2003thecompletegenome pages 1-2) | GO:0006412 translation; GO:0042776 mitochondrial ATP synthesis not central—prefer GO:0017148 negative regulation of translation by toxin not standard; GO:0009405 pathogenesis; GO:0019219 regulation of nucleobase-containing compound metabolic process; GO:0006886 intracellular protein transport |
| Anatomy / cells | Primary sites are upper respiratory tract mucosa (tonsils, pharynx, larynx, trachea) and skin. Secondary systemic injury affects myocardium and peripheral nerves; kidneys can also be affected. Cell-level involvement includes mucosal epithelial cells, keratinocytes, cardiomyocytes, and peripheral neurons/Schwann-cell-associated tissues. (osarenren2024globalstrategiesfor pages 2-4, wenzel2020humanantibodiesneutralizing pages 1-2, museux2023corynebacteriaofthe pages 1-2, cerdenotarraga2003thecompletegenome pages 1-2) | Respiratory obstruction from pseudomembrane can cause fatal asphyxia; in cutaneous French series, lower limbs predominated. Human toxin complications reflect hematogenous spread to distant organs. (chene2024cutaneousdiphtheriafrom pages 1-2, cerdenotarraga2003thecompletegenome pages 1-2) | UBERON: pharynx, palatine tonsil, larynx, trachea, skin, heart, peripheral nerve; CL: epithelial cell, keratinocyte, cardiomyocyte, neuron, Schwann cell |
| Diagnostics | Diagnosis is clinical first when compatible membrane/airway disease is present; confirm with culture, species identification, and toxigenicity testing. Culture may use tellurite media; current workflows commonly add tox PCR and reference-lab confirmation; Elek test remains classical phenotypic toxin-expression assay. Serology is useful for population immunity studies, not acute diagnosis. (gaillet2024retrospectivestudyof pages 1-2, muhammed2018diphtheriathestrangling pages 2-3, chene2024cutaneousdiphtheriafrom pages 1-2) | In French Guiana, 61 *C. diphtheriae* isolates included 5 tox-gene positive, all Elek-negative. In Kitamura 2023, ELISA cutoffs corresponding to TNT 0.01 IU/mL were 0.060 IU/mL (serum) and 0.044 IU/mL (DBS); applying 0.06 IU/mL to a Vietnam serosurvey classified 54% as susceptible, while multiple-imputation estimate was 35%. (gaillet2024retrospectivestudyof pages 1-2, kitamura2023evaluationandvalidation pages 1-2, kitamura2023evaluationandvalidation pages 6-9, kitamura2023evaluationandvalidation pages 3-6) | NCIT: Polymerase Chain Reaction; LOINC concepts for bacterial culture and antitoxin serology; MeSH: Elek Test |
| Treatment | Immediate therapy should not await lab confirmation when respiratory diphtheria is suspected. Mainstays: diphtheria antitoxin/antiserum to neutralize circulating toxin, antibiotics (classically penicillin or erythromycin), isolation, airway management, cardiac monitoring, and update of immunization after recovery. (osarenren2024globalstrategiesfor pages 1-2, muhammed2018diphtheriathestrangling pages 1-2, dinanti2024determinantsofmortality pages 1-2) | Historical/modern reviews report overall fatality commonly 5–10%, higher in young children; untreated/unvaccinated severe cases may approach ~29% in review synthesis. 2024 pediatric cohorts identify airway obstruction and myocarditis as major mortality drivers. (osarenren2024globalstrategiesfor pages 1-2, wenzel2020humanantibodiesneutralizing pages 1-2, dinanti2024determinantsofmortality pages 1-2) | NCIT: Antitoxin Therapy; Penicillin; Erythromycin; Anti-Bacterial Agent; Airway Management; Cardiac Monitoring |
| Prevention / public health | Prevention is dominated by diphtheria toxoid-containing vaccination, booster maintenance, rapid case recognition, isolation, prophylaxis and vaccination of close contacts, and surveillance. Cutaneous disease also requires wound/contact control; zoonotic *C. ulcerans* requires animal-human interface management. (osarenren2024globalstrategiesfor pages 1-2, osarenren2024globalstrategiesfor pages 2-4, chene2024cutaneousdiphtheriafrom pages 1-2, museux2023corynebacteriaofthe pages 1-2) | Vaccination gaps and disrupted immunization services are repeatedly linked to resurgence. In the French cutaneous cohort, immunization rate was 44%; in companion-animal work, authors emphasized tox-gene testing and management of animal contacts. (chene2024cutaneousdiphtheriafrom pages 1-2, museux2023corynebacteriaofthe pages 1-2, dinanti2024determinantsofmortality pages 1-2) | NCIT: Vaccination; Diphtheria Toxoid Vaccine; Contact Tracing; Chemoprophylaxis; Isolation Precaution |
| Epidemiology / prognosis | Disease burden is now concentrated in under-immunized populations and humanitarian/health-system-fragile settings. Respiratory disease remains the classic severe form, while cutaneous disease is increasingly recognized and epidemiologically important. Prognosis worsens with delayed antitoxin, airway obstruction, myocarditis, incomplete immunization, and young age. (osarenren2024globalstrategiesfor pages 1-2, gaillet2024retrospectivestudyof pages 1-2, osarenren2024globalstrategiesfor pages 2-4, chene2024cutaneousdiphtheriafrom pages 1-2, dinanti2024determinantsofmortality pages 1-2) | French Guiana incidence rose from 0.7/100,000 in 2016 to 7.7/100,000 in 2021; mean age 30.4 years; male:female 1.7:1; 95% of cases were cutaneous. Nigeria early 2023 review cited 733 suspected cases and 89 deaths Jan–Mar 2023. In recent French cutaneous series, 68.3% were men and 56.7% had traveled outside mainland France. (gaillet2024retrospectivestudyof pages 1-2, medugu2023areviewof pages 1-2, chene2024cutaneousdiphtheriafrom pages 1-2) | MeSH: Incidence; Prevalence; Mortality; UBERON/HPO terms for complications |
| Veterinary reservoirs / models | *C. ulcerans* is a major zoonotic reservoir species in companion animals and other mammals; horses can carry tox-positive *C. diphtheriae*. Animal and experimental systems have been central to toxin biology and antitoxin development. Classical toxin-neutralization and intoxication studies use guinea pigs; rodents are naturally resistant unless engineered to express the receptor. (museux2023corynebacteriaofthe pages 1-2, cerdenotarraga2003thecompletegenome pages 1-2, wenzel2020humanantibodiesneutralizing pages 1-2) | Companion-animal survey screened 18,308 animals and found 51 *C. ulcerans* cases (24 toxigenic), plus 2 horses with tox-positive *C. diphtheriae* and 11 *C. rouxii* infections. Phase 1 monoclonal antitoxin program cites prior guinea-pig potency work. (museux2023corynebacteriaofthe pages 1-2, NCT04075175 chunk 1) | NCBITaxon: dog, cat, horse, rat, *C. ulcerans*; NCIT: Animal Model; UBERON: skin, nasal cavity |
| Human genetics / omics applicability notes | Diphtheria is not primarily a Mendelian human genetic disease; there are no established causal human germline genes or inheritance patterns for “having diphtheria.” Relevant genetics are mostly pathogen-side (tox, phage carriage, DtxR-regulated virulence programs) and host receptor biology used mechanistically. Human omics for routine diagnosis are limited; serology and pathogen genomics are more actionable than host genomics. (wenzel2020humanantibodiesneutralizing pages 1-2, prygiel2022newcorynebacteriumspecies pages 1-2, cerdenotarraga2003thecompletegenome pages 1-2) | Recent practical advances center on pathogen genomic surveillance, tox-gene detection, and serosurveys rather than WES/WGS for host diagnosis. Clinical trials include anti-toxin mAb S315 (NCT04075175; completed, n=41) and new DTaP-containing vaccine studies such as NCT06184542 (recruiting, target n=460). (NCT04075175 chunk 1, NCT06184542 chunk 1) | SO/NCIT not applicable for causal human variant annotation; NCIT: Whole Genome Sequencing (pathogen surveillance context), Serologic Test, Monoclonal Antibody Therapy |


*Table: This compact table summarizes the most actionable disease-knowledge-base facts for diphtheria across clinical, mechanistic, epidemiologic, veterinary, and implementation domains. It is designed to support structured curation with recent evidence and ontology term suggestions.*

## 1. Disease information

Diphtheria is an acute communicable bacterial infection, classically of the upper respiratory tract, in which toxigenic *Corynebacterium* colonizes mucosa and secretes diphtheria toxin (DT). Local epithelial injury produces an adherent pseudomembrane and possible airway obstruction; absorbed toxin can injure myocardium, peripheral nerves, and other organs. Cutaneous disease presents primarily as chronic ulcers and is an important reservoir for transmission. Modern definitions vary: the strict definition requires toxin-producing *C. diphtheriae* or *C. ulcerans*, whereas some surveillance systems include non-toxigenic infections by the *C. diphtheriae* species complex (CdSC). (gaillet2024retrospectivestudyof pages 1-2, prygiel2022newcorynebacteriumspecies pages 1-2, chene2024cutaneousdiphtheriafrom pages 1-2, museux2023corynebacteriaofthe pages 1-2)

**Identifiers and synonyms**

- **MONDO:** MONDO:0005015 (diphtheria; verify against the current MONDO release).
- **MeSH:** D004165, *Diphtheria*, confirmed in the ClinicalTrials.gov-derived MeSH record. (NCT04075175 chunk 1)
- **ICD-10:** A36, with A36.0 pharyngeal, A36.1 nasopharyngeal, A36.2 laryngeal, A36.3 cutaneous, A36.8 other, and A36.9 unspecified diphtheria.
- **ICD-11:** 1C1A, diphtheria; extension/subcategory codes should be checked in the current ICD-11 browser.
- **OMIM/Orphanet:** no appropriate Mendelian OMIM disease entry or rare-genetic Orphanet disease entity is expected; this is an acquired infection.
- **Synonyms:** respiratory diphtheria, pharyngeal/faucial diphtheria, laryngeal diphtheria or diphtheritic croup, nasal diphtheria, cutaneous diphtheria, diphtheritic angina, and historically “the strangling angel.”
- **Data provenance:** the entry is aggregated disease-level knowledge based on surveillance, cohorts, microbiology, and mechanistic studies. It is not derived from one patient's EHR, although some source cohorts used retrospective medical records. (gaillet2024retrospectivestudyof pages 1-2, dinanti2024determinantsofmortality pages 1-2)

## 2. Etiology, risks, and protective factors

### Causal factors

The primary cause is infection with a toxigenic strain of *C. diphtheriae*. *C. ulcerans* and, very rarely, *C. pseudotuberculosis* can also produce DT. The bacterial **tox** structural gene is carried by related corynebacteriophages and ordinarily requires lysogenic insertion into the bacterial chromosome. Genotype does not perfectly predict phenotype: “nontoxigenic tox-gene-bearing” strains carry **tox** but fail to express active toxin. (prygiel2022newcorynebacteriumspecies pages 1-2, museux2023corynebacteriaofthe pages 1-2)

Respiratory disease spreads predominantly through droplets or close contact with respiratory secretions. Cutaneous organisms spread through direct skin contact and, less often, contaminated objects. *C. ulcerans* is zoonotic and associated with contact with cats, dogs, livestock, and diverse wild mammals; unpasteurized milk is an uncommon exposure. Humans are the principal reservoir for *C. diphtheriae*. (osarenren2024globalstrategiesfor pages 2-4, medugu2023areviewof pages 1-2, chene2024cutaneousdiphtheriafrom pages 1-2, museux2023corynebacteriaofthe pages 1-2)

### Risk factors

The dominant risk is absent, incomplete, or waned diphtheria-toxoid immunity. Other risks include overcrowding, close contact with a case or carrier, poverty, homelessness, migration or displacement, disrupted vaccination services, civil unrest, limited laboratory/antitoxin access, poor wound hygiene, and travel to endemic regions. Immunocompromise and socioeconomic disadvantage are prominent in cutaneous cohorts. Pandemic-related interruptions in immunization and surveillance contributed to recent resurgence. (osarenren2024globalstrategiesfor pages 1-2, gaillet2024retrospectivestudyof pages 1-2, osarenren2024globalstrategiesfor pages 2-4, medugu2023areviewof pages 1-2, dinanti2024determinantsofmortality pages 1-2)

Age is not intrinsically protective: in well-vaccinated settings, waning antibody can shift cases to adolescents and adults. In the Nigerian outbreak reviewed in 2023, many cases occurred at 5–18 years; historical Indian data likewise showed substantial disease after age five. (medugu2023areviewof pages 1-2, muhammed2018diphtheriathestrangling pages 1-2)

### Protective factors and gene–environment interaction

Primary vaccination and age-appropriate boosters are the strongest protective factors. Rapid identification and antibiotics shorten carriage; isolation, contact tracing, prophylactic antibiotics, and vaccination of contacts interrupt spread. No reproducible human “protective variant,” susceptibility locus, modifier gene, or clinically actionable host pharmacogenomic marker is established. Mechanistically, host expression and species structure of **HBEGF/proHB-EGF**, the toxin receptor, influence cellular/species susceptibility, but this is not a validated human risk-stratification test. Protection is therefore best modeled as the interaction of exposure intensity and pathogen toxigenicity with vaccine-derived neutralizing antibody, not as classical host G×E inheritance. (osarenren2024globalstrategiesfor pages 1-2, wenzel2020humanantibodiesneutralizing pages 1-2, cerdenotarraga2003thecompletegenome pages 1-2)

## 3. Phenotypes

Respiratory symptoms usually begin acutely after a short incubation. Common manifestations include malaise, low-grade fever, sore throat, odynophagia/dysphagia, tonsillitis or pharyngitis, cervical lymphadenopathy and edema, and an adherent gray-white membrane that bleeds if forcibly removed. Extensive edema produces “bull neck.” Nasal disease can cause serosanguineous discharge; laryngeal/tracheal extension causes hoarseness, stridor, croup, and potentially fatal airway obstruction. Suggested HPO terms include **Fever HP:0001945**, **Sore throat HP:0025439**, **Dysphagia HP:0002015**, **Cervical lymphadenopathy HP:0025289**, **Neck swelling HP:0000464**, **Stridor HP:0010307**, **Dyspnea HP:0002094**, and **Upper-airway obstruction HP:0002781**; “diphtheritic pseudomembrane” may require a disease-specific annotation because exact HPO coverage should be verified. (osarenren2024globalstrategiesfor pages 2-4, muhammed2018diphtheriathestrangling pages 2-3, museux2023corynebacteriaofthe pages 1-2, dinanti2024determinantsofmortality pages 1-2)

The pseudomembrane generally forms within two to three days. It reflects fibrin, inflammatory cells, bacteria, and necrotic epithelium. Severity ranges from asymptomatic carriage or localized disease to rapidly progressive obstruction and systemic toxemia; severe cases may die within 6–10 days. (osarenren2024globalstrategiesfor pages 2-4, muhammed2018diphtheriathestrangling pages 2-3)

**Cutaneous diphtheria** commonly causes a chronic, nonhealing, “punched-out” or rolled-edge ulcer, often with dirty-gray membrane. Suggested HPO terms are **Skin ulcer HP:0200042**, **Impaired wound healing HP:0001058**, and **Abnormality of the lower limb HP:0002814**. In a 2024 French series of 63 adults, 86.9% of lesions involved lower limbs, 82% were ulcers, and 88.9% were polymicrobial; mean age was 53.8 years, 68.3% were men, 56.7% had traveled outside mainland France, and only 44% were appropriately immunized. These figures describe a selected metropolitan-French cohort, not universal phenotype frequencies. (chene2024cutaneousdiphtheriafrom pages 1-2)

**Systemic complications** include myocarditis/cardiomyopathy, conduction disturbances and arrhythmia, heart failure, peripheral or cranial neuropathy, palatal paralysis, descending weakness, respiratory-muscle paralysis, acute kidney injury, and thrombocytopenia in severe disease. Suggested HPO terms include **Myocarditis HP:0012819**, **Cardiac arrhythmia HP:0011675**, **Heart failure HP:0001635**, **Peripheral neuropathy HP:0009830**, **Muscle weakness HP:0001324**, **Acute kidney injury HP:0001919**, and **Thrombocytopenia HP:0001873**. Myocarditis often appears in the second week and neuropathy later, sometimes after apparent respiratory improvement. A 2024 Indonesian pediatric cohort found myocarditis and airway obstruction significantly associated with mortality; airway obstruction was associated with approximately 13-fold higher odds of death. (muhammed2018diphtheriathestrangling pages 2-3, dinanti2024determinantsofmortality pages 1-2)

Diphtheritic myocarditis may present with no echocardiographic dysfunction or mild-to-severe dysfunction. In a 2024 Pakistani series restricted to 73 children already diagnosed with diphtheritic myocarditis, 27.4% had rhythm abnormalities, 20% conduction abnormalities, and 30.1% severe echocardiographic dysfunction; those percentages must not be generalized to all diphtheria cases.

Disease-specific validated quality-of-life instruments are scarce. Acute respiratory disease profoundly impairs swallowing, breathing, mobility, schooling/work, and self-care; neuropathy and cardiomyopathy can prolong rehabilitation. Published cohorts focus on survival and organ complications rather than EQ-5D, SF-36, or PROMIS scores.

## 4. Genetic and molecular information

### Human genetics

There are **no established human causal genes, pathogenic germline variants, chromosomal abnormalities, inheritance pattern, penetrance estimates, anticipation, founder variants, or carrier frequency** for diphtheria. ClinVar/HGMD-style ACMG classification, WES/WGS, CMA, karyotyping, FISH, mitochondrial sequencing, and repeat-expansion testing are not indicated for routine diagnosis. **HBEGF** (HGNC:3059) and **EEF2** (HGNC:3214) are mechanistically relevant host genes, not diphtheria-causative genes. No clinically established host modifier or disease-specific epigenetic signature is available.

### Pathogen genetics

The key virulence determinant is phage-borne **tox**, a 1,683-bp gene encoding a 535-amino-acid toxin. **dtxR**, encoding the iron-dependent diphtheria-toxin repressor, coordinates toxin/iron-homeostasis programs; low available iron relieves repression and favors toxin transcription. Adhesins, pili/fimbriae, iron-uptake systems, biofilm-related factors, and other horizontally acquired loci contribute to colonization and virulence. The landmark NCTC13129 genome is a single 2,488,635-bp chromosome with 53.48% GC and 2,320 predicted coding sequences; the analysis identified recent acquisition of toxin, iron-uptake, adhesion, and fimbrial determinants. (prygiel2022newcorynebacteriumspecies pages 1-2, cerdenotarraga2003thecompletegenome pages 1-2)

The clinically meaningful “variant classification” is therefore pathogen-side: **tox-positive/toxin-expressing**, **tox-negative**, or **NTTB**, rather than human ACMG pathogenicity. In one contemporary synthesis, approximately 10–15% of tox-bearing CdSC strains were NTTB because of disruptive changes. Whole-genome sequencing, MLST, and resistance-gene analysis support outbreak linkage and antimicrobial-resistance surveillance but are not replacements for phenotypic toxigenicity testing. (prygiel2022newcorynebacteriumspecies pages 1-2, museux2023corynebacteriaofthe pages 1-2)

## 5. Environmental, lifestyle, and infectious-agent information

The infectious agents are gram-positive, non-spore-forming, nonmotile pleomorphic bacilli in the CdSC. Suggested NCBI Taxonomy mappings include *C. diphtheriae* TaxID **1717**, *C. ulcerans* TaxID **65058**, and *C. pseudotuberculosis* TaxID **1719**; identifiers should be release-validated before ingestion.

Relevant environmental/social exposures are crowding, household or institutional contact, displacement camps, weak sanitation and health infrastructure, interrupted immunization, contact with infected wounds/fomites, and animal contact for *C. ulcerans*. Smoking, diet, alcohol, and exercise are not established direct causal factors, although alcohol-use disorder, homelessness, poor nutrition, and chronic wounds can cluster with cutaneous-disease risk. No radiation, pollution, or occupational toxin is causal. Veterinary, farm, and laboratory work may increase exposure to zoonotic CdSC organisms. (osarenren2024globalstrategiesfor pages 1-2, gaillet2024retrospectivestudyof pages 1-2, prygiel2022newcorynebacteriumspecies pages 1-2, chene2024cutaneousdiphtheriafrom pages 1-2)

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream exposure and colonization:** droplets or contact introduce organisms to pharyngeal/laryngeal epithelium or damaged skin. Bacterial adhesins and pili support attachment; local replication initiates inflammation.
2. **Toxigenesis:** a lysogenized strain expresses and secretes DT. Iron availability regulates expression through DtxR.
3. **Local tissue injury:** DT kills epithelial cells, producing necrosis, fibrin-rich exudate, and the tightly adherent pseudomembrane. Membrane extension and edema narrow the airway.
4. **Cell entry:** the toxin receptor-binding domain binds membrane proHB-EGF/HB-EGF; receptor-mediated endocytosis follows. Endosomal acidification changes toxin conformation, and its translocation domain delivers the catalytic domain into cytosol.
5. **Biochemical lesion:** the catalytic domain transfers ADP-ribose from NAD⁺ to diphthamide on eukaryotic elongation factor 2, halting translation and causing cell dysfunction/death.
6. **Downstream toxemia:** hematogenous toxin reaches cardiomyocytes and peripheral nervous tissue, producing myocarditis, conduction failure, demyelinating/axonal neuropathy, weakness, and possible respiratory failure. Renal and hematologic abnormalities can accompany severe systemic illness. (osarenren2024globalstrategiesfor pages 2-4, wenzel2020humanantibodiesneutralizing pages 1-2, cerdenotarraga2003thecompletegenome pages 1-2)

DT is approximately 58 kDa and has catalytic, translocation, and receptor-binding domains. The retrieved mechanistic study generated 400 recombinant human antibodies; 35 were produced as human IgG1. The best individual antibody had estimated in-vitro potency of 454 IU/mg, while combinations retained activity at higher toxin loads and reached 79.4 IU/mg in an in-vivo intradermal assay. This supports multi-epitope human-antibody replacement of equine antitoxin, but it was preclinical evidence rather than demonstrated patient efficacy. (wenzel2020humanantibodiesneutralizing pages 1-2)

**Suggested GO biological-process terms:** pathogenesis (**GO:0009405**), receptor-mediated endocytosis (**GO:0006898**), protein ADP-ribosylation (**GO:0006471**), cytoplasmic translation (**GO:0002181**), negative regulation of translation (**GO:0017148**), apoptotic process (**GO:0006915**), inflammatory response (**GO:0006954**), and response to iron ion (**GO:0010039**). Relevant compartments include extracellular region (**GO:0005576**), plasma membrane (**GO:0005886**), endosome (**GO:0005768**), endosomal membrane (**GO:0010008**), and cytosol (**GO:0005829**).

**Suggested CL terms:** epithelial cell (**CL:0000066**), keratinocyte (**CL:0000312**), cardiomyocyte (**CL:0000746**), neuron (**CL:0000540**), Schwann cell (**CL:0000218**), macrophage (**CL:0000235**), and neutrophil (**CL:0000775**).

### Molecular profiling and advanced technologies

Pathogen genomics and transcriptomics have identified phage cargo, iron-acquisition systems, adhesins/pili, and regulatory networks. These data are primarily microbial, not host clinical omics. No validated human transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or epigenomic diagnostic signature is in routine use. Single-cell and CRISPR methods are research opportunities rather than established diphtheria knowledge-base associations.

## 7. Anatomical structures affected

The principal sites are the posterior mouth, palatine tonsils, nasopharynx, oropharynx, larynx, and proximal trachea; skin, especially lower-limb skin, is the other major site. Less common local sites include eye, ear, and genital mucosa. Secondary toxin targets include myocardium, cardiac conduction tissue, peripheral nerves, cranial nerves, and kidneys. Disease is not characteristically lateralized. (prygiel2022newcorynebacteriumspecies pages 1-2, chene2024cutaneousdiphtheriafrom pages 1-2, cerdenotarraga2003thecompletegenome pages 1-2)

Suggested UBERON mappings are **pharynx UBERON:0001042**, **palatine tonsil UBERON:0002373**, **larynx UBERON:0001737**, **trachea UBERON:0003126**, **skin UBERON:0002097**, **heart UBERON:0000948**, **myocardium UBERON:0002349**, **kidney UBERON:0002113**, and **peripheral nervous system UBERON:0000010**. At the tissue level, respiratory stratified/squamous epithelium, skin epithelium, cardiac muscle, and peripheral nerve are involved. Relevant subcellular compartments are cell surface, endosome, cytosol, and translational machinery.

## 8. Temporal development

Incubation is usually **2–5 days**, with reported ranges around 1–6 days. Onset is acute. Membrane formation commonly occurs by day 2–3. Early disease comprises colonization, pharyngitis, low fever, and membrane expansion; intermediate disease includes airway compromise and cervical edema; advanced disease includes systemic toxemia, myocarditis, neuritis, renal injury, and respiratory failure. (osarenren2024globalstrategiesfor pages 2-4, muhammed2018diphtheriathestrangling pages 2-3, muhammed2018diphtheriathestrangling pages 1-2)

Untreated persons may remain infectious for 2–3 weeks; effective antibiotics markedly shorten contagiousness, reported as about one day in a 2024 review synthesis. Myocarditis often emerges during the first or second week; neuropathy may appear in weeks 2–6 and recover slowly over weeks to months. Respiratory disease is generally acute and nonrelapsing after eradication, although neurologic deficits can persist. The decisive intervention window is **immediately when respiratory diphtheria is suspected**, before toxin binds cells; antitoxin cannot reverse already internalized toxin. (osarenren2024globalstrategiesfor pages 2-4, muhammed2018diphtheriathestrangling pages 2-3)

## 9. Inheritance and population epidemiology

There is no Mendelian inheritance, penetrance, anticipation, germline mosaicism, consanguinity effect, or human carrier frequency. “Carrier” in this disease means asymptomatic bacterial carriage, not heterozygosity.

Vaccination reduced diphtheria dramatically in high-income countries, but outbreaks persist or recur in under-immunized populations, especially in parts of Africa and Asia and in humanitarian settings. A December 2024 review reported **27,991 suspected cases and 828 deaths across five African countries in 2024**. A 2023 review of Nigeria reported **733 suspected cases and 89 deaths (12.3% case-fatality) during January–March 2023**, mainly in children aged 5–18 years. These counts are time- and definition-dependent and should not be interpreted as stable incidence estimates. (osarenren2024globalstrategiesfor pages 2-4, medugu2023areviewof pages 1-2)

In French Guiana, a 2016–2021 multicenter study found 64 infection episodes in 60 patients; incidence increased from **0.7/100,000 in 2016 to 7.7/100,000 in 2021**. Mean age was 30.4 years, male:female ratio 1.7:1, and 95% of episodes were cutaneous. Only five of 61 *C. diphtheriae* isolates carried **tox**, and all were Elek-negative, demonstrating that CdSC infection counts are not equivalent to toxin-mediated classical diphtheria. (gaillet2024retrospectivestudyof pages 1-2)

Sex effects are inconsistent and probably exposure-dependent rather than biological. Male predominance occurred in French Guiana and metropolitan-French cutaneous cohorts, while a Pakistani myocarditis cohort was nearly sex-balanced. Age distribution depends strongly on vaccine history, booster policies, and outbreak setting.

## 10. Diagnostics

### Clinical and laboratory diagnosis

Suspected respiratory diphtheria is a **clinical emergency**: acute pharyngitis/tonsillitis/laryngitis with low fever and an adherent gray pseudomembrane, especially with bull neck, bleeding on attempted removal, incomplete vaccination, or epidemiologic exposure. Treatment and public-health notification should not await confirmation. (osarenren2024globalstrategiesfor pages 1-2, dinanti2024determinantsofmortality pages 1-2)

Before antibiotics where feasible, obtain throat and nasal swabs from beneath/around the membrane, or swab/tissue from a skin lesion. Microscopy may show pleomorphic gram-positive rods in “Chinese-letter” arrangements. Culture uses selective tellurite-containing media, on which colonies can appear gray/black. Modern reference workflows combine species identification with PCR for **tox**. Because PCR establishes gene carriage rather than active toxin production, a phenotypic assay—classically the Elek immunoprecipitation test—is required for expression. MALDI-TOF can aid species identification but may need updated databases/reference-laboratory confirmation for closely related CdSC species. (gaillet2024retrospectivestudyof pages 1-2, muhammed2018diphtheriathestrangling pages 2-3, chene2024cutaneousdiphtheriafrom pages 1-2)

A negative culture after antibiotics does not reliably exclude disease. Routine imaging is not diagnostic. ECG, troponin/CK and other cardiac enzymes, echocardiography, renal function, CBC/platelets, and neurologic examinations assess complications. Electromyography and nerve-conduction studies can characterize delayed neuropathy. Airway imaging/endoscopy should be used cautiously and only when clinically necessary because manipulation may worsen obstruction.

### Serology and omics

Antitoxin titers assess immunity, not acute infection. Conventionally, <0.01 IU/mL suggests susceptibility, 0.01–0.1 IU/mL partial/basic protection, and ≥0.1 IU/mL more durable protection, although assay-specific calibration matters. In a 2023 Vietnamese validation study, serum/DBS ELISA values corresponding to a TNT threshold of 0.01 IU/mL were 0.060 and 0.044 IU/mL. In a 510-person serosurvey, a corrected cutoff classified 54% as susceptible, whereas multiple imputation estimated 35%, showing that uncorrected ELISA can substantially misclassify population immunity. At the 0.1-IU/mL threshold, AUC was 0.82 for serum and 0.89 for DBS. (kitamura2023evaluationandvalidation pages 9-11, kitamura2023evaluationandvalidation pages 1-2, kitamura2023evaluationandvalidation pages 6-9, kitamura2023evaluationandvalidation pages 3-6)

Pathogen WGS is valuable for outbreak reconstruction, strain taxonomy, and resistance surveillance. Host WES/WGS, RNA-seq, proteomics, metabolomics, epigenomics, and liquid biopsy have no routine diagnostic role.

### Differential diagnosis and screening

Differentials include streptococcal pharyngitis/scarlet fever, infectious mononucleosis, peritonsillar or retropharyngeal abscess, epiglottitis, bacterial tracheitis, candidiasis, Vincent angina, agranulocytosis-related necrotic pharyngitis, and caustic injury. An adherent bleeding membrane, bull neck, low-grade rather than high fever, incomplete vaccination, toxin complications, and isolation of a toxigenic CdSC organism favor diphtheria.

There is no newborn or genetic screening. Outbreak screening consists of clinical assessment and nasal/throat culture/PCR of close contacts; population serosurveys identify immunity gaps.

## 11. Outcome and prognosis

Overall case-fatality is commonly cited around **5–10%**, rising toward 20% in young children in some settings; untreated, unvaccinated severe disease may approach 29% in review syntheses. Values vary markedly with case definition, antitoxin availability, vaccination, referral bias, and outbreak setting. Severe disease can cause death within 6–10 days from asphyxia, cardiogenic shock, or malignant arrhythmia. (osarenren2024globalstrategiesfor pages 1-2, osarenren2024globalstrategiesfor pages 2-4, wenzel2020humanantibodiesneutralizing pages 1-2)

Poor prognostic factors include delayed antitoxin, extensive membrane/bull neck, airway obstruction, myocarditis or arrhythmia, shock, renal injury, thrombocytopenia/leukocytosis in severe disease, young age, absent/incomplete immunization, and limited critical-care access. In the Indonesian 2020–2023 pediatric cohort, myocarditis, airway obstruction, and thrombocytopenia were statistically associated with mortality, and obstruction conferred approximately 13-fold higher death odds. (dinanti2024determinantsofmortality pages 1-2)

Localized cutaneous disease is usually less systemically severe but sustains transmission and may still cause toxemia if the isolate is toxigenic. In French Guiana, 95% of cases were cutaneous and all five tox-PCR-positive isolates were Elek-negative, helping explain the cohort’s different clinical profile from classic respiratory outbreaks. (gaillet2024retrospectivestudyof pages 1-2)

Survivors of uncomplicated disease may recover fully. Neuropathy can require prolonged physical, occupational, respiratory, and swallowing rehabilitation. No meaningful 5- or 10-year survival statistic is used for this acute infection, and formal long-term quality-of-life datasets are limited.

## 12. Treatment

### Immediate algorithm

1. Isolate suspected respiratory cases with droplet precautions; add contact precautions for wounds.
2. Collect cultures/PCR specimens without delaying therapy.
3. Administer **diphtheria antitoxin (DAT)** promptly for suspected respiratory/toxin-mediated disease after appropriate hypersensitivity precautions. DAT neutralizes circulating toxin but not toxin already bound/internalized.
4. Give an effective antibiotic—traditionally **erythromycin** or **penicillin**—to eradicate organisms and stop transmission; follow national guidance, susceptibility results, age, allergy, pregnancy, and local resistance patterns. Macrolide alternatives may be used according to guidelines.
5. Secure and monitor the airway; avoid traumatic membrane removal. Provide ICU care, telemetry/serial ECG, cardiac biomarkers and echocardiography when severe disease is present.
6. Confirm eradication with post-treatment cultures as required; repeat treatment if carriage persists.
7. Vaccinate during convalescence because infection does not reliably confer immunity. (osarenren2024globalstrategiesfor pages 1-2, muhammed2018diphtheriathestrangling pages 1-2, dinanti2024determinantsofmortality pages 1-2)

Suggested NCIT intervention mappings include **Diphtheria Antitoxin**, **Antibiotic Therapy**, **Penicillin**, **Erythromycin**, **Airway Management**, **Mechanical Ventilation**, **Cardiac Monitoring**, **Temporary Cardiac Pacing**, **Vaccination**, and **Rehabilitation Therapy**; exact NCIT concept codes should be release-validated. Equine DAT can cause immediate hypersensitivity/anaphylaxis and delayed serum sickness. Macrolides commonly cause gastrointestinal intolerance and can prolong QT; penicillins can cause allergy.

There is no routine surgery except airway intervention such as intubation or tracheostomy when obstruction cannot otherwise be managed. Supportive care includes fluids without overload, nutrition, aspiration prevention, treatment of heart failure/arrhythmia, renal support, and rehabilitation for neuropathy. Corticosteroids for diphtheritic cardiomyopathy remain inadequately established; small observational findings should not replace guideline care.

### Experimental and recent therapeutic development

A fully human anti-DT monoclonal antibody, **S315**, completed a randomized, triple-masked phase I study in 41 healthy adults (**NCT04075175**; started 23 April 2019, completed 7 October 2019). The study assessed safety and pharmacokinetics, not efficacy in patients with diphtheria. [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT04075175). (NCT04075175 chunk 1)

Preclinical recombinant-antibody combinations neutralized multiple DT domains and are intended to overcome equine-DAT limitations such as serum sickness, batch variation, and animal dependence. The authoritative investigators concluded that these combinations were “candidates for further clinical and regulatory development to replace equine DAT,” but clinical replacement has not yet been established in the evidence reviewed. (wenzel2020humanantibodiesneutralizing pages 1-2)

Gene, cell, RNA, CRISPR, or personalized genotype-guided therapies have no current clinical role.

## 13. Prevention

**Primary prevention:** complete diphtheria-toxoid-containing vaccination and boosters across the life course. Toxoid induces neutralizing antitoxin and primarily prevents toxin-mediated disease; it does not guarantee elimination of colonization by non-toxigenic or zoonotic CdSC organisms. Outbreak responses combine catch-up vaccination, community engagement, mobile/access-focused delivery, and surveillance. (osarenren2024globalstrategiesfor pages 1-2, osarenren2024globalstrategiesfor pages 2-4, chene2024cutaneousdiphtheriafrom pages 1-2)

**Secondary prevention:** rapidly identify and isolate cases; notify public health; culture/PCR close contacts; give recommended antibiotic prophylaxis; update contacts’ vaccination; exclude infected carriers from high-risk settings until eradication is documented. Healthcare workers require appropriate PPE and documented immunization.

**Tertiary prevention:** early DAT, antibiotics, airway protection, telemetry, renal/neurologic monitoring, and rehabilitation prevent death and long-term disability. Antitoxin shortages are a major expert-identified contributor to mortality in low-resource outbreaks. (osarenren2024globalstrategiesfor pages 1-2, medugu2023areviewof pages 1-2)

Serosurveillance can reveal hidden adult immunity gaps, but assay calibration is essential. Dried blood spots performed well against TNT in the 2023 study and offer a lower-cost implementation option in low- and middle-income settings. (kitamura2023evaluationandvalidation pages 9-11, kitamura2023evaluationandvalidation pages 1-2, kitamura2023evaluationandvalidation pages 3-6)

A randomized, blinded phase I pediatric DT-acellular-pertussis vaccine study (**NCT06184542**) began 23 December 2023 and targeted 460 participants aged two months to six years. It evaluates solicited/unsolicited adverse events and antibody concentration, seropositivity, seroconversion, and neutralization outcomes. The retrieved registry record listed it as recruiting with estimated completion in November 2026. [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT06184542). (NCT06184542 chunk 1)

## 14. Other species and natural disease

*C. ulcerans* naturally infects numerous mammals and is an important zoonotic source of diphtheria-like disease. *C. pseudotuberculosis* causes caseous lymphadenitis in sheep/goats and other veterinary syndromes; toxin-producing isolates are rare. *C. silvaticum* has been recovered from wild boar, while *C. rouxii* is an emerging CdSC species. (prygiel2022newcorynebacteriumspecies pages 1-2, museux2023corynebacteriaofthe pages 1-2)

A 2023 French study screened **18,308** symptomatic companion animals. It found 51 *C. ulcerans* cases, 24 toxigenic; rhinitis was most common (18/51). Eleven were monoinfections. German shepherds were overrepresented among dogs (9/28; P<0.00001). Two horses carried tox-positive *C. diphtheriae*, and 11 animals had tox-negative *C. rouxii*. The authors emphasized reference-laboratory **tox** testing and coordinated management of animals and human contacts. This is strong veterinary surveillance evidence for One Health relevance, not proof that every colonized animal transmits to humans. (museux2023corynebacteriaofthe pages 1-2)

Suggested taxa include dog **NCBITaxon:9615**, cat **9685**, horse **9796**, rat **10116**, guinea pig **10141**, mouse **10090**, and human **9606**. Breed-level VBO annotation may include German Shepherd Dog, subject to current VBO verification. There is no orthologous “disease gene” model because diphtheria is infectious; relevant orthologs are host **HBEGF** and **EEF2** and pathogen virulence genes.

## 15. Model organisms and experimental systems

- **Guinea pig:** classical mammalian toxin-intoxication and antitoxin-potency model; sensitive to DT and useful for in-vivo neutralization, pathology, and antitoxin lot testing. S315’s registry cites guinea-pig potency work (PMID **27070129**). Limitations include intoxication rather than full natural respiratory colonization and species-specific dosing. (NCT04075175 chunk 1)
- **Mouse/rat:** naturally relatively resistant because their proHB-EGF receptor interacts poorly with DT. Transgenic mice expressing a toxin-sensitive receptor permit systemic/respiratory-pathogenesis studies. This species restriction is a limitation but also a powerful receptor-mechanism experiment. (cerdenotarraga2003thecompletegenome pages 1-2)
- **Cell culture:** Vero-cell toxin neutralization is a functional reference assay; human respiratory epithelial lines and other HB-EGF-expressing cells support entry/cytotoxicity studies. Limitations include absence of intact airway, immunity, circulation, and organ interactions. (kitamura2023evaluationandvalidation pages 9-11, kitamura2023evaluationandvalidation pages 3-6)
- **Invertebrate models:** *Caenorhabditis elegans* and *Galleria mellonella* can screen non-toxin virulence and bacterial fitness but do not reproduce human DT receptor biology or myocarditis.
- **Ex-vivo/advanced systems:** airway organoids and organ-on-chip systems are plausible for adhesion, epithelial injury, and antitoxin studies, but no validated routine diphtheria model was identified in the retrieved evidence.

Relevant repositories include MGI/IMSR for transgenic mice, RGD for rats, ATCC/Cellosaurus for cell lines, NCBI/ENA for pathogen genomes, and Institut Pasteur’s BIGSdb/PubMLST-type resources for strain epidemiology.

## Selected exact abstract quotations and evidence classification

- **Human clinical/surveillance, French Guiana (published August 2024):** “Estimated incidence increased from 0.7 cases/100,000 population in 2016 to 7.7 cases/100,000 population in 2021.” [DOI](https://doi.org/10.3201/eid3008.231671). (gaillet2024retrospectivestudyof pages 1-2)
- **Human clinical, cutaneous cohort (accepted 19 September 2024):** “Lesions involved the lower limbs (86.9%), corresponded to ulcerations in 82% of cases.” [DOI](https://doi.org/10.1080/22221751.2024.2408324). (chene2024cutaneousdiphtheriafrom pages 1-2)
- **Human clinical, pediatric prognosis (published 9 August 2024):** “Patients with airway obstruction were 13 times more likely to have an increase in mortality compared to patients without airway obstruction.” [DOI](https://doi.org/10.52225/narra.v4i2.776). (dinanti2024determinantsofmortality pages 1-2)
- **Laboratory/serosurveillance (published June 2023):** “DBS is an effective low-cost alternative to serum for future serological studies for diphtheria.” [DOI](https://doi.org/10.1099/jmm.0.001721). (kitamura2023evaluationandvalidation pages 1-2)
- **Veterinary/One Health (published 6 April 2023):** “C. ulcerans represents an important zoonotic risk, and C. rouxii may represent a novel zoonotic agent.” [DOI](https://doi.org/10.1128/spectrum.00006-23). (museux2023corynebacteriaofthe pages 1-2)
- **Molecular/in-vitro and animal neutralization (published January 2020):** “These recombinant antibody combinations are candidates for further clinical and regulatory development to replace equine DAT.” [DOI](https://doi.org/10.1038/s41598-019-57103-5). (wenzel2020humanantibodiesneutralizing pages 1-2)

## Overall expert assessment

Current evidence supports a simple but urgent interpretation: diphtheria resurgence is primarily a failure of population immunity, timely recognition, and access to antitoxin—not emergence of a human genetic disorder. The highest-yield real-world actions are complete toxoid vaccination with boosters, resilient routine-immunization systems, immediate DAT for compatible respiratory disease, microbiologic confirmation including phenotypic toxigenicity, antibiotic eradication, and aggressive contact management. The most important recent research developments are better recognition of cutaneous and zoonotic CdSC disease, pathogen genomic surveillance, improved low-cost serosurveillance using DBS, and human monoclonal-antitoxin development. Major evidence gaps remain in standardized contemporary phenotype frequencies, long-term quality of life, randomized treatment trials, clinically validated omics, and equitable DAT availability.

References

1. (osarenren2024globalstrategiesfor pages 2-4): Jolaawo Osarenren, Pius Omoruyi Omosigho, and Olalekan John Okesanya. Global strategies for addressing diphtheria resurgence epidemiology clinical impact and prevention. Discover Public Health, Dec 2024. URL: https://doi.org/10.1186/s12982-024-00352-1, doi:10.1186/s12982-024-00352-1. This article has 20 citations and is from a peer-reviewed journal.

2. (prygiel2022newcorynebacteriumspecies pages 1-2): Marta Prygiel, Maciej Polak, Ewa Mosiej, Karol Wdowiak, Kamila Formińska, and Aleksandra Zasada. New corynebacterium species with the potential to produce diphtheria toxin. Pathogens, 11:1264, Oct 2022. URL: https://doi.org/10.3390/pathogens11111264, doi:10.3390/pathogens11111264. This article has 33 citations.

3. (chene2024cutaneousdiphtheriafrom pages 1-2): Laure Chêne, Jean-Jacques Morand, Edgar Badell, Julie Toubiana, Fréderic Janvier, Hugo Marthinet, Jean-philippe Suppini, Aude Valois, Gaetan Texier, Sylvain Brisse, and Fabien Dutasta. Cutaneous diphtheria from 2018 to 2022: an observational, retrospective study of epidemiological, microbiological, clinical, and therapeutic characteristics in metropolitan france. Sep 2024. URL: https://doi.org/10.1080/22221751.2024.2408324, doi:10.1080/22221751.2024.2408324. This article has 15 citations and is from a domain leading peer-reviewed journal.

4. (museux2023corynebacteriaofthe pages 1-2): Kristina Museux, Gabriele Arcari, Guido Rodrigo, Melanie Hennart, Edgar Badell, Julie Toubiana, and Sylvain Brisse. Corynebacteria of the <i>diphtheriae</i> species complex in companion animals: clinical and microbiological characterization of 64 cases from france. Jun 2023. URL: https://doi.org/10.1128/spectrum.00006-23, doi:10.1128/spectrum.00006-23. This article has 22 citations and is from a domain leading peer-reviewed journal.

5. (muhammed2018diphtheriathestrangling pages 2-3): S. Muhammed, Y. Muhammed, R. Gupta, and V. Sondhi. Diphtheria: the strangling angel of (older) children. Pediatric Oncall, Jan 2018. URL: https://doi.org/10.7199/ped.oncall.2018.25, doi:10.7199/ped.oncall.2018.25. This article has 0 citations.

6. (dinanti2024determinantsofmortality pages 1-2): Shinta P. Dinanti, Oke R. Ramayani, and Ayodhia P. Pasaribu. Determinants of mortality in relationship between clinical and laboratory characteristics with the outcomes of children with diphtheria: a cross-sectional study at a national hospital of sumatra region in 2020–2023. Narra J, 4(2):e776, Aug 2024. URL: https://doi.org/10.52225/narra.v4i2.776, doi:10.52225/narra.v4i2.776. This article has 1 citations.

7. (wenzel2020humanantibodiesneutralizing pages 1-2): Esther Veronika Wenzel, Margarita Bosnak, Robert Tierney, Maren Schubert, Jeffrey Brown, Stefan Dübel, Androulla Efstratiou, Dorothea Sesardic, Paul Stickings, and Michael Hust. Human antibodies neutralizing diphtheria toxin in vitro and in vivo. Scientific Reports, Jan 2020. URL: https://doi.org/10.1038/s41598-019-57103-5, doi:10.1038/s41598-019-57103-5. This article has 89 citations and is from a peer-reviewed journal.

8. (cerdenotarraga2003thecompletegenome pages 1-2): A. Cerdeño-Tárraga, A. Efstratiou, L. Dover, M. Holden, M. Pallen, S. Bentley, G. Besra, C. Churcher, K. James, A. D. Zoysa, T. Chillingworth, A. Cronin, L. Dowd, T. Feltwell, N. Hamlin, S. Holroyd, K. Jagels, S. Moule, M. Quail, E. Rabbinowitsch, Kim M Rutherford, N. Thomson, L. Unwin, S. Whitehead, B. Barrell, and J. Parkhill. The complete genome sequence and analysis of corynebacterium diphtheriae nctc13129. Nucleic Acids Research, 31(22):6516-6523, Nov 2003. URL: https://doi.org/10.1093/nar/gkg874, doi:10.1093/nar/gkg874. This article has 420 citations and is from a highest quality peer-reviewed journal.

9. (gaillet2024retrospectivestudyof pages 1-2): Mélanie Gaillet, Mélanie Hennart, Vincent Sainte Rose, Edgar Badell, Céline Michaud, Romain Blaizot, Magalie Demar, Luisiane Carvalho, Jean François Carod, Audrey Andrieu, Félix Djossou, Julie Toubiana, Loic Epelboin, and Sylvain Brisse. Retrospective study of infections with corynebacterium diphtheriae species complex, french guiana, 2016–2021. Emerging Infectious Diseases, 30:1542-1551, Aug 2024. URL: https://doi.org/10.3201/eid3008.231671, doi:10.3201/eid3008.231671. This article has 2 citations and is from a domain leading peer-reviewed journal.

10. (kitamura2023evaluationandvalidation pages 1-2): Noriko Kitamura, Akira Endo, Lien T. Le, Trieu B. Nguyen, Hung T. Do, Michiko Toizumi, Lay-Myint Yoshida, Yoshio Mori, Samuel Rose, Androulla Efstratiou, Norman K. Fry, and David Litt. Evaluation and validation of a commercial elisa versus the in vitro toxin neutralization assay for determination of diphtheria anti-toxin in human serum. Jun 2023. URL: https://doi.org/10.1099/jmm.0.001721, doi:10.1099/jmm.0.001721. This article has 3 citations and is from a peer-reviewed journal.

11. (kitamura2023evaluationandvalidation pages 6-9): Noriko Kitamura, Akira Endo, Lien T. Le, Trieu B. Nguyen, Hung T. Do, Michiko Toizumi, Lay-Myint Yoshida, Yoshio Mori, Samuel Rose, Androulla Efstratiou, Norman K. Fry, and David Litt. Evaluation and validation of a commercial elisa versus the in vitro toxin neutralization assay for determination of diphtheria anti-toxin in human serum. Jun 2023. URL: https://doi.org/10.1099/jmm.0.001721, doi:10.1099/jmm.0.001721. This article has 3 citations and is from a peer-reviewed journal.

12. (kitamura2023evaluationandvalidation pages 3-6): Noriko Kitamura, Akira Endo, Lien T. Le, Trieu B. Nguyen, Hung T. Do, Michiko Toizumi, Lay-Myint Yoshida, Yoshio Mori, Samuel Rose, Androulla Efstratiou, Norman K. Fry, and David Litt. Evaluation and validation of a commercial elisa versus the in vitro toxin neutralization assay for determination of diphtheria anti-toxin in human serum. Jun 2023. URL: https://doi.org/10.1099/jmm.0.001721, doi:10.1099/jmm.0.001721. This article has 3 citations and is from a peer-reviewed journal.

13. (osarenren2024globalstrategiesfor pages 1-2): Jolaawo Osarenren, Pius Omoruyi Omosigho, and Olalekan John Okesanya. Global strategies for addressing diphtheria resurgence epidemiology clinical impact and prevention. Discover Public Health, Dec 2024. URL: https://doi.org/10.1186/s12982-024-00352-1, doi:10.1186/s12982-024-00352-1. This article has 20 citations and is from a peer-reviewed journal.

14. (muhammed2018diphtheriathestrangling pages 1-2): S. Muhammed, Y. Muhammed, R. Gupta, and V. Sondhi. Diphtheria: the strangling angel of (older) children. Pediatric Oncall, Jan 2018. URL: https://doi.org/10.7199/ped.oncall.2018.25, doi:10.7199/ped.oncall.2018.25. This article has 0 citations.

15. (medugu2023areviewof pages 1-2): N. Medugu, T.O. Musa-Booth, B. Adegboro, A.O. Onipede, M. Babazhitsu, and R. Amaza. A review of the current diphtheria outbreaks. African Journal of Clinical and Experimental Microbiology, 24:120-129, Apr 2023. URL: https://doi.org/10.4314/ajcem.v24i2.2, doi:10.4314/ajcem.v24i2.2. This article has 30 citations.

16. (NCT04075175 chunk 1):  Evaluate the Safety Pharmacokinetics of a Human Monoclonal Antibody S315 Against Diphtheria Toxin in Healthy Subjects. MassBiologics. 2019. ClinicalTrials.gov Identifier: NCT04075175

17. (NCT06184542 chunk 1):  Phase I Clinical Trial of Diphtheria-Tetanus-acellular Pertussis Component Combined Vaccine. Institute of Medical Biology, Chinese Academy of Medical Sciences. 2023. ClinicalTrials.gov Identifier: NCT06184542

18. (kitamura2023evaluationandvalidation pages 9-11): Noriko Kitamura, Akira Endo, Lien T. Le, Trieu B. Nguyen, Hung T. Do, Michiko Toizumi, Lay-Myint Yoshida, Yoshio Mori, Samuel Rose, Androulla Efstratiou, Norman K. Fry, and David Litt. Evaluation and validation of a commercial elisa versus the in vitro toxin neutralization assay for determination of diphtheria anti-toxin in human serum. Jun 2023. URL: https://doi.org/10.1099/jmm.0.001721, doi:10.1099/jmm.0.001721. This article has 3 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Diphtheria-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 2 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `DOI:10.1128/spectrum.00006-23` (5 mentions) - Corynebacteria of the
            <i>diphtheriae</i>
            Species Complex in Companion Animals: Clinical and Microbiological Characterization of 64 Cases from France
  - shared terms: clinical

Weighed against this report's own most characteristic terms: `disease`, `clinical`, `human`, `diphtheria`, `gene`, `toxin`, `include`, `genetic`, `respiratory`, `cell`, `airway`, `system`, `contact`, `vaccination`, `treatment`, `age`, `genome`, `antitoxin`, `model`, `cutaneous`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 61 |
| Resolved | 57 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 2 |
| Unverifiable | 2 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0005015` (1 mention) - the report calls it "diphtheria; verify against the current MONDO release"; MONDO calls it **diabetes mellitus**

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `GO:0009405` (obsolete pathogenesis) (2 mentions)
- `GO:0006471` (obsolete protein ADP-ribosylation) (1 mention)