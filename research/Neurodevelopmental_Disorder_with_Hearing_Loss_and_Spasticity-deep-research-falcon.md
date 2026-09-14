---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-15T08:33:34.105196'
end_time: '2026-08-15T08:46:43.251798'
duration_seconds: 789.15
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Neurodevelopmental Disorder with Hearing Loss and Spasticity
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 15
reference_validation:
  total_references: 6
  verified: 5
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.167
  unresolved_references:
  - DOI:10.3390/jcm14238442](https://doi.org/10.3390/jcm14238442
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Neurodevelopmental_Disorder_with_Hearing_Loss_and_Spasticity-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder with Hearing Loss and Spasticity
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder with Hearing Loss and Spasticity** covering all of the
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
- **Disease Name:** Neurodevelopmental Disorder with Hearing Loss and Spasticity
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder with Hearing Loss and Spasticity** covering all of the
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


# Neurodevelopmental Disorder with Hearing Loss and Spasticity: Research Report

## Executive summary

**Neurodevelopmental disorder with hearing loss and spasticity (NEDHLS)** is an ultra-rare, autosomal-recessive Mendelian disorder caused by biallelic germline variants in **AFG2B**, historically named **SPATA5L1**. Its defining phenotype comprises infantile-onset global developmental impairment, usually bilateral sensorineural hearing loss, and evolving motor dysfunction—most characteristically spasticity and/or dystonia. Epilepsy, microcephaly, cerebral or white-matter volume loss, delayed myelination, corpus-callosum hypoplasia, and dysmorphism are variable. The foundational report described 25 affected individuals; fewer than 30 had been reported before a detailed 2025 case, so robust prevalence, survival, penetrance, and genotype–phenotype estimates remain unavailable. (OpenTargets Search: Neurodevelopmental disorder with hearing loss and spasticity, polczyk2025neurodevelopmentaldisorderwith pages 1-2, polczyk2025neurodevelopmentaldisorderwith pages 6-7)

The major recent advance is mechanistic. A 2024 *Cell* study established that AFG2B/SPATA5L1 participates with SPATA5, C1ORF109, and CINP in the **55LCC AAA+ ATPase complex**, which maintains replisome proteostasis and genome integrity. Deficiency causes replication-fork stress first, followed by cohesion defects and micronucleation. This is strong biochemical and cellular evidence, but it does not yet prove exactly how particular neural and cochlear cell populations produce every clinical manifestation. (krishnamoorthy2024thespata5spata5l1atpase pages 1-3, krishnamoorthy2024thespata5spata5l1atpase pages 8-10, krishnamoorthy2024thespata5spata5l1atpase pages 10-12)

The following table provides a knowledge-base-oriented overview.

| domain | established finding | ontology/identifier suggestions | evidence type/source |
|---|---|---|---|
| Disease identity | Neurodevelopmental disorder with hearing loss and spasticity is the exact disease entity linked to **AFG2B** (alias **SPATA5L1**). Open Targets maps the disease to **MONDO:0859206** and the causal target to **AFG2B**. | **MONDO suggestion:** MONDO:0859206; **gene suggestion:** AFG2B/SPATA5L1; **disease label suggestion:** AFG2B-related neurodevelopmental disorder with hearing loss and spasticity | Curated disease-target resource plus cited literature linkage (OpenTargets Search: Neurodevelopmental disorder with hearing loss and spasticity) |
| Key identifiers | The disorder is described as **OMIM phenotype 619616** in a recent case report discussing SPATA5L1-related disease. | **OMIM suggestion:** 619616 | Human clinical case report / literature synthesis (polczyk2025neurodevelopmentaldisorderwith pages 4-6) |
| Synonymy / nomenclature | Recent literature uses **SPATA5L1-related neurodevelopmental disorder**, **AFG2B-related disorder**, and the descriptive disease name with hearing loss and spasticity. | **Synonym suggestions:** SPATA5L1-related NDD; AFG2B-related NEDHLS | Human clinical case report and review-style discussion (polczyk2025neurodevelopmentaldisorderwith pages 1-2, polczyk2025neurodevelopmentaldisorderwith pages 7-9) |
| Genetic etiology | Cause is **biallelic germline variants in SPATA5L1/AFG2B**; inheritance is **autosomal recessive**. | **Inheritance suggestion:** HP:0000007 Autosomal recessive inheritance | Open Targets/literature association and human clinical genetics report (OpenTargets Search: Neurodevelopmental disorder with hearing loss and spasticity, polczyk2025neurodevelopmentaldisorderwith pages 4-6) |
| Example pathogenic variants | A recent patient had compound heterozygous **c.1918C>T (p.Arg640Ter)** and **c.2066G>T (p.Gly689Val)**, inherited **in trans** from carrier parents. | **Variant annotation suggestion:** HGVS c./p. notation; ACMG/AMP classification in case report: p.Arg640Ter uncertain significance, p.Gly689Val likely/pathogenic in cited resources | Human trio-WES case report (polczyk2025neurodevelopmentaldisorderwith pages 4-6) |
| Core neurodevelopmental phenotype | Established clinical spectrum includes **global psychomotor/developmental delay**, **intellectual disability/developmental impairment**, and abnormal motor development. | **HPO suggestions:** HP:0001263 Global developmental delay; HP:0001249 Intellectual disability; HP:0011344 Severe global developmental delay (severity if documented per case) | Foundational human cohort summarized by later case report; direct recent case findings (polczyk2025neurodevelopmentaldisorderwith pages 9-10, polczyk2025neurodevelopmentaldisorderwith pages 7-9, polczyk2025neurodevelopmentaldisorderwith pages 2-4) |
| Hearing phenotype | **Bilateral sensorineural hearing loss** is a core feature; in the 2025 case it was detected in infancy and measured at **60 dBnHL** with hearing aids fitted. | **HPO suggestions:** HP:0000407 Sensorineural hearing impairment; HP:0008619 Bilateral hearing impairment | Human clinical case report (polczyk2025neurodevelopmentaldisorderwith pages 7-9, polczyk2025neurodevelopmentaldisorderwith pages 2-4) |
| Motor phenotype | Published cases commonly show **spasticity and/or dystonia**; the recent infant case showed early **central hypotonia** with concern for later evolution toward a spastic-dystonic pattern. | **HPO suggestions:** HP:0001257 Spasticity; HP:0001332 Dystonia; HP:0001252 Hypotonia; **disease-overlap suggestion:** cerebral palsy spectrum phenotype | Human cohort summary and detailed case follow-up (polczyk2025neurodevelopmentaldisorderwith pages 9-10, polczyk2025neurodevelopmentaldisorderwith pages 7-9, polczyk2025neurodevelopmentaldisorderwith pages 6-7) |
| Epilepsy / EEG | **Epilepsy** is part of the reported disease spectrum, but not universal. In the 2025 case, early EEG was negative; later EEG showed **bilateral sharp waves, incomplete FO-FW complexes, and theta activity** without clinically confirmed seizures to date. | **HPO suggestions:** HP:0001250 Seizure; HP:0010848 Abnormal EEG | Human clinical case report (polczyk2025neurodevelopmentaldisorderwith pages 7-9, polczyk2025neurodevelopmentaldisorderwith pages 6-7) |
| Craniofacial / ocular findings | Variable **craniofacial dysmorphism** is reported; the recent case had **bitemporal narrowing, wide mouth, epicanthal folds**, plus **intermittent strabismus**, hypermetropia, and astigmatism. | **HPO suggestions:** HP:0001999 Bitemporal narrowing; HP:0000286 Epicanthus; HP:0000341 Broad mouth / wide mouth; HP:0000486 Strabismus | Human clinical case report (polczyk2025neurodevelopmentaldisorderwith pages 7-9, polczyk2025neurodevelopmentaldisorderwith pages 2-4) |
| Brain imaging phenotype | MRI abnormalities can include **cortical/white matter atrophy or volume loss**, **delayed myelination**, **thin/hypoplastic corpus callosum**, and white matter T2 hyperintensities. | **HPO suggestions:** HP:0007058 Delayed CNS myelination; HP:0002079 White matter abnormality; HP:0002078 Cerebral atrophy; HP:0001273 Agenesis/hypoplasia of corpus callosum (use hypoplasia when appropriate) | Human clinical case report; consistent with earlier cohort per author summary (polczyk2025neurodevelopmentaldisorderwith pages 7-9, polczyk2025neurodevelopmentaldisorderwith pages 6-7) |
| Molecular complex | SPATA5L1/AFG2B functions in the **SPATA5-SPATA5L1-C1orf109-CINP** complex, termed **55LCC**. The complex is a DNA-binding AAA+ ATPase assembly with unusual **4:2:2:2 stoichiometry** for SPATA5:SPATA5L1:C1orf109:CINP. | **GO suggestions:** GO:0140657 ATP-dependent activity, acting on DNA (suggestion); GO:0006260 DNA replication; **complex label suggestion:** 55LCC complex | Structural/biochemical/cell-biology study in Cell 2024 (krishnamoorthy2024thespata5spata5l1atpase pages 1-3, krishnamoorthy2024thespata5spata5l1atpase pages 5-7, krishnamoorthy2024thespata5spata5l1atpase pages 10-12) |
| Mechanistic disease model | 55LCC binds DNA, shows ATPase activity enhanced specifically by **replication fork DNA**, and promotes **ubiquitin-independent replisome proteostasis**. Loss of the complex causes **replication stress**, reduced fork progression/restart, and downstream chromosome instability. | **GO suggestions:** GO:0006281 DNA repair; GO:0045005 DNA replication restart; GO:0031573 mitotic cell cycle checkpoint; GO:0031267 small GTPase-independent? not established, avoid; **use suggested terms only where broadly matching:** DNA replication, response to replication stress, protein unfolding/proteostasis | Mechanistic cell/biochemistry study (krishnamoorthy2024thespata5spata5l1atpase pages 3-5, krishnamoorthy2024thespata5spata5l1atpase pages 8-10, krishnamoorthy2024thespata5spata5l1atpase pages 5-7, krishnamoorthy2024thespata5spata5l1atpase pages 10-12) |
| Replisome substrates / downstream biology | Replisome-associated factors reported as processed by 55LCC include **POLD3, RFC1, POLA1, POLD1**; additional processed factors include **ATR, ATRIP, RAD21** under replication stress conditions. | **GO suggestions:** GO:0005657 replication fork; **protein/pathway suggestions:** DNA polymerase delta complex, RFC complex, ATR signaling | Mechanistic cell/biochemistry study (krishnamoorthy2024thespata5spata5l1atpase pages 8-10, krishnamoorthy2024thespata5spata5l1atpase pages 10-12) |
| Cell compartments / localization | The complex associates with **chromatin**, including **replicating chromatin**, and chromatin association varies across the cell cycle. | **GO Cellular Component suggestions:** GO:0000785 chromatin; GO:0005657 replication fork; GO:0005634 nucleus | Cell-based chromatin assays (krishnamoorthy2024thespata5spata5l1atpase pages 3-5, krishnamoorthy2024thespata5spata5l1atpase pages 10-12) |
| Affected anatomy and cell types | Clinical and mechanistic evidence implicate the **central nervous system** and **auditory system**; recent literature also notes SPATA5L1 enrichment in **neurons**, **glial nuclei**, and **neurosensory hair cells**. | **UBERON suggestions:** brain, cerebral white matter, corpus callosum, inner ear/cochlea; **CL suggestions:** neuron, glial cell, hair cell | Human case synthesis and mechanistic discussion (polczyk2025neurodevelopmentaldisorderwith pages 1-2, polczyk2025neurodevelopmentaldisorderwith pages 7-9) |
| Diagnostic strategy | Current practice is genomic diagnosis via **trio whole-exome sequencing** or broader sequencing with segregation analysis; CNV and uniparental disomy analysis may be performed to exclude alternative causes. Clinical workup includes **audiology**, **EEG**, **brain MRI**, and neurologic/developmental assessment. | **Testing suggestions:** WES/WGS; segregation testing; MRI brain; audiology/BAEP; EEG; **HPO-driven phenotyping suggested** | Human case report demonstrating real-world diagnostic workflow (polczyk2025neurodevelopmentaldisorderwith pages 4-6, polczyk2025neurodevelopmentaldisorderwith pages 6-7, polczyk2025neurodevelopmentaldisorderwith pages 2-4) |
| Management / real-world care | No disease-specific therapy was identified. Current care is **supportive and rehabilitative**, including **hearing aids**, early **physical/neurodevelopmental rehabilitation** (including Vojta-based therapy in one report), and monitoring for seizures and motor evolution. | **NCIT intervention suggestions:** hearing aid device; physical therapy; occupational therapy; speech/hearing rehabilitation; antiseizure therapy if clinically indicated | Human case management and trial-gap search (polczyk2025neurodevelopmentaldisorderwith pages 4-6, polczyk2025neurodevelopmentaldisorderwith pages 7-9, polczyk2025neurodevelopmentaldisorderwith pages 2-4, OpenTargets Search: Neurodevelopmental disorder with hearing loss and spasticity) |
| Prognosis / disease course | Disease appears **chronic** with early-childhood onset and persistent neurodevelopmental disability; expression is **variable**, especially for seizures and the timing of spastic-dystonic features. Robust survival or life-expectancy data were not identified. | **Course suggestions:** congenital/infantile onset neurodevelopmental disorder; variable expressivity | Human clinical reports with explicit knowledge gaps (polczyk2025neurodevelopmentaldisorderwith pages 7-9, polczyk2025neurodevelopmentaldisorderwith pages 6-7) |
| Epidemiology | Ultra-rare Mendelian disorder; recent literature notes **fewer than 30 affected individuals** reported to date, and one recent paper cites a **cohort of 25 patients** from Richard et al. | **Epidemiology suggestion:** prevalence/incidence unknown | Recent clinical case report summarizing prior literature (polczyk2025neurodevelopmentaldisorderwith pages 1-2, polczyk2025neurodevelopmentaldisorderwith pages 6-7) |
| Population / consanguinity | Both **consanguineous and non-consanguineous** family structures are represented in the literature summary; the 2025 case arose in a **non-consanguineous** family. Population-specific founder frequency was not established here. | **Counseling suggestion:** carrier testing and reproductive counseling for at-risk relatives | Human clinical case report / literature synthesis (polczyk2025neurodevelopmentaldisorderwith pages 6-7, polczyk2025neurodevelopmentaldisorderwith pages 2-4) |
| Modifier / environmental factors | No established environmental risk factors, protective factors, or gene-environment interactions were identified in the available evidence. | **Knowledge-gap suggestion:** none established | Negative/insufficient evidence from available sources (OpenTargets Search: Neurodevelopmental disorder with hearing loss and spasticity, polczyk2025neurodevelopmentaldisorderwith pages 7-9) |
| Experimental therapeutics / trials | No relevant disease-specific interventional clinical trial was found in the trial search. Translational work is mechanistic/preclinical rather than therapeutic at present. | **Trial status suggestion:** no disease-specific registered interventional study identified | Clinical trial search and disease-target resource (OpenTargets Search: Neurodevelopmental disorder with hearing loss and spasticity) |


*Table: This table summarizes high-confidence disease facts for AFG2B/SPATA5L1-related neurodevelopmental disorder with hearing loss and spasticity, including identifiers, phenotypes, mechanism, diagnostics, and current care gaps. It is designed as a compact knowledge-base artifact with suggested ontology mappings clearly labeled as suggestions.*

## 1. Disease information

### Definition and identifiers

* **Preferred name:** Neurodevelopmental disorder with hearing loss and spasticity.
* **Abbreviation:** NEDHLS.
* **MONDO:** **MONDO:0859206**.
* **OMIM phenotype:** **619616**.
* **Causal gene:** **AFG2B** (current approved symbol in Open Targets; historical literature symbol **SPATA5L1**), Ensembl ENSG00000171763.
* **Common names:** AFG2B-related disorder; SPATA5L1-related neurodevelopmental disorder; SPATA5L1-related neurodevelopmental disorder with hearing loss and spasticity.
* **Foundational publication:** Richard et al., “Bi-allelic variants in SPATA5L1 lead to intellectual disability, spastic-dystonic cerebral palsy, epilepsy, and hearing loss,” *American Journal of Human Genetics* 108:2006–2016, published October 2021; PMID **34626583**; DOI [10.1016/j.ajhg.2021.08.003](https://doi.org/10.1016/j.ajhg.2021.08.003).
* **Recent mechanism paper:** Krishnamoorthy et al., *Cell* 187:2250–2268.e31, published April 2024; PMID **38554706**; DOI [10.1016/j.cell.2024.03.002](https://doi.org/10.1016/j.cell.2024.03.002). (OpenTargets Search: Neurodevelopmental disorder with hearing loss and spasticity, krishnamoorthy2024thespata5spata5l1atpase pages 1-3, polczyk2025neurodevelopmentaldisorderwith pages 4-6)

No disease-specific MeSH descriptor or unique ICD-10/ICD-11 code was established in the retrieved evidence. In clinical coding, manifestations such as developmental disability, sensorineural hearing loss, epilepsy, dystonia, or spastic cerebral palsy would therefore generally require separate codes; this is not equivalent to a dedicated NEDHLS code.

The evidence is primarily **aggregated disease-level evidence assembled from individually phenotyped patients**, family segregation data, and experimental studies. It is not derived from a population-scale EHR cohort. (polczyk2025neurodevelopmentaldisorderwith pages 1-2, polczyk2025neurodevelopmentaldisorderwith pages 9-10)

## 2. Etiology, risk, and protective factors

NEDHLS is caused by **biallelic AFG2B/SPATA5L1 variants**, usually homozygous or compound heterozygous, inherited in an autosomal-recessive pattern. The available data support loss of function or severe functional impairment—through truncation, impaired protein stability, defective complex assembly, or impaired ATPase/replisome-processing function—as the causal model. Patient-associated SPATA5L1 variants tested in the 2024 study compromised viability or 55LCC function; some behaved as partial-loss-of-function or hypomorphic alleles. (krishnamoorthy2024thespata5spata5l1atpase pages 7-8, krishnamoorthy2024thespata5spata5l1atpase pages 12-14)

A recent example is compound heterozygosity for **c.1918C>T (p.Arg640Ter)** and **c.2066G>T (p.Gly689Val)**, inherited in trans from unaffected carrier parents. The reporting laboratory called p.Arg640Ter a VUS and p.Gly689Val likely pathogenic, while also noting ClinVar pathogenic classification for p.Gly689Val. The authors applied PVS1/PM2/PM3/PP4 reasoning to the truncating allele. These classifications should be re-evaluated against the current ClinVar record and ACMG/AMP specifications before clinical use. (polczyk2025neurodevelopmentaldisorderwith pages 4-6)

The p.Gly689Val allele is recurrent: it occurred in four people in the original 25-person cohort. Most other reported variants appear private, and the cohort is too small for reliable allele-specific prognosis. (polczyk2025neurodevelopmentaldisorderwith pages 6-7)

No validated susceptibility loci, modifier genes, protective alleles, environmental causes, lifestyle risks, infectious triggers, or gene–environment interactions are known. Consanguinity can increase the probability that partners carry the same rare allele but is not required; the 2025 case involved non-consanguineous parents. A de novo FRYL variant in that case was considered uncertain and potentially artifactual, not an established modifier. (polczyk2025neurodevelopmentaldisorderwith pages 7-9, polczyk2025neurodevelopmentaldisorderwith pages 2-4)

## 3. Phenotypes

The phenotype is congenital or infantile in biological origin, although clinical recognition usually occurs when developmental milestones or hearing are assessed. Exact cohort-wide percentages could not be verified from the accessible primary full text; qualitative frequencies below should not be converted into penetrance estimates.

* **Global developmental/psychomotor delay and intellectual disability:** core, often severe and persistent. Suggested HPO: **HP:0001263**, **HP:0001249**. In the 2025 patient, parental concern began at four months; at 14 months, motor organization approximated a 12-week developmental level. (polczyk2025neurodevelopmentaldisorderwith pages 1-2, polczyk2025neurodevelopmentaldisorderwith pages 2-4)
* **Sensorineural hearing impairment:** core and described as nearly universal in the literature summary. Suggested HPO: **HP:0000407** and bilateral hearing impairment **HP:0008619**. The recent patient had bilateral 60-dBnHL loss diagnosed at seven months and received hearing aids. Hearing loss substantially affects speech-language acquisition and communication. (polczyk2025neurodevelopmentaldisorderwith pages 1-2, polczyk2025neurodevelopmentaldisorderwith pages 2-4)
* **Motor disorder:** spasticity and/or dystonia predominated in most members of the original cohort, producing a spastic-dystonic cerebral-palsy phenotype. Suggested HPO: **HP:0001257**, **HP:0001332**. Early hypotonia may precede hypertonia: the recent child remained centrally hypotonic at 14 months, later developing upper-limb stiffening. This supports age-dependent evolution rather than requiring spasticity in infancy. (polczyk2025neurodevelopmentaldisorderwith pages 7-9, polczyk2025neurodevelopmentaldisorderwith pages 6-7)
* **Hypotonia:** variable, particularly early. Suggested HPO: **HP:0001252**. It impairs antigravity posture, rolling, sitting, and mobility. (polczyk2025neurodevelopmentaldisorderwith pages 6-7, polczyk2025neurodevelopmentaldisorderwith pages 2-4)
* **Epilepsy/EEG abnormality:** common but not obligatory. Suggested HPO: **HP:0001250**, abnormal EEG **HP:0010848**. The recent child had no epileptiform activity at nine months; at approximately two years, bilateral sharp waves and other abnormalities appeared, but clinical epilepsy remained unconfirmed. (polczyk2025neurodevelopmentaldisorderwith pages 7-9, polczyk2025neurodevelopmentaldisorderwith pages 6-7)
* **Microcephaly:** variable. Suggested HPO: **HP:0000252**. The recent child’s head circumference was below the third percentile after age two. (polczyk2025neurodevelopmentaldisorderwith pages 1-2, polczyk2025neurodevelopmentaldisorderwith pages 6-7)
* **MRI abnormalities:** cerebral/cortical and white-matter volume loss, delayed myelination, periventricular T2 hyperintensity, mild ventriculomegaly, and thin/hypoplastic corpus callosum. Suggested HPO: **HP:0002078**, **HP:0007058**, **HP:0002079**, **HP:0001273**. (polczyk2025neurodevelopmentaldisorderwith pages 7-9, polczyk2025neurodevelopmentaldisorderwith pages 6-7)
* **Dysmorphism:** variable and reported in roughly one-third according to the later literature summary; findings can include bitemporal narrowing, wide mouth, and epicanthal folds. Suggested HPO: **HP:0001999**, **HP:0000286**, and broad/wide mouth mapping after ontology validation. (polczyk2025neurodevelopmentaldisorderwith pages 7-9, polczyk2025neurodevelopmentaldisorderwith pages 2-4)
* **Ophthalmic findings:** strabismus, refractive errors, and occasionally cortical visual impairment. Suggested HPO: **HP:0000486**, hypermetropia **HP:0000540**, astigmatism **HP:0000483**. (polczyk2025neurodevelopmentaldisorderwith pages 1-2, polczyk2025neurodevelopmentaldisorderwith pages 2-4)
* **Primitive reflex persistence/abnormal postural reactions:** potentially useful early motor signs, but not validated as disease-specific biomarkers. In one child, all seven Vojta postural reactions were abnormal at 11 and 14 months, and Moro, rooting, and Babkin reflexes persisted. (polczyk2025neurodevelopmentaldisorderwith pages 6-7)

No NEDHLS-specific EQ-5D, SF-36, PROMIS, or caregiver-burden study was found. Nevertheless, severe impairment of communication, mobility, self-care, education, and independent living is clinically foreseeable from the documented combined hearing and neurodevelopmental disabilities; this is an inference rather than a quantified disease-specific result.

## 4. Genetic and molecular information

**AFG2B/SPATA5L1** encodes an AAA+ ATPase-family protein. Open Targets assigns an exact disease–target association score of approximately 0.726 and links the association to PMIDs 34626583 and 38554706. (OpenTargets Search: Neurodevelopmental disorder with hearing loss and spasticity)

Reported pathogenic classes include missense, nonsense, frameshift, and likely splice-disrupting alleles, although a definitive exhaustive variant table and current gnomAD frequencies were not recoverable from the available primary text. Variants are germline, not somatic. The recessive inheritance and unaffected heterozygous parents are consistent with disease requiring two damaging alleles. (polczyk2025neurodevelopmentaldisorderwith pages 9-10, polczyk2025neurodevelopmentaldisorderwith pages 4-6)

Functional studies show several routes to pathogenicity:

1. reduced protein stability;
2. defective interaction or assembly within 55LCC;
3. reduced ATP binding/hydrolysis or pore-mediated unfoldase activity;
4. impaired replisome-substrate processing;
5. cellular replication stress and chromosome instability. (krishnamoorthy2024thespata5spata5l1atpase pages 7-8, krishnamoorthy2024thespata5spata5l1atpase pages 12-14)

Most patient mutants in the 2024 experiments were unstable after endogenous wild-type protein was removed. **I466M and G689V** were exceptions in retaining stability, although preserved abundance does not establish normal function. The patient-associated **V245E** allele severely compromised viability in CRISPR-rescue assays. (krishnamoorthy2024thespata5spata5l1atpase pages 7-8, krishnamoorthy2024thespata5spata5l1atpase pages 8-10)

No validated modifier gene, disease-specific methylation signature, chromosomal rearrangement, repeat expansion, mitochondrial-DNA defect, or somatic mechanism has been established. Large CNVs and uniparental disomy were specifically not explanatory in the recent patient. (polczyk2025neurodevelopmentaldisorderwith pages 4-6)

## 5. Environmental information

No toxin, radiation, pollution, occupation, diet, smoking, alcohol, exercise pattern, or infectious agent has been implicated causally. Prenatal history was uneventful in the detailed recent case. NEDHLS is not infectious, environmentally acquired, or zoonotic. Environmental and lifestyle measures may improve general health but are not known to alter the primary molecular defect. (polczyk2025neurodevelopmentaldisorderwith pages 2-4)

## 6. Mechanism and pathophysiology

### Upstream molecular defect

SPATA5 and AFG2B/SPATA5L1 are type-II AAA+ ATPases related to the CDC48/p97 family. Together with C1ORF109 and CINP they form the stable four-member **55LCC** complex. Cryo-EM and orthogonal interaction studies indicate a **4:2:2:2 stoichiometry**—four SPATA5, two SPATA5L1, two C1ORF109, and two CINP subunits—forming a funnel/lid over a stacked-ring ATPase motor. ATP binding stabilizes the complex. (krishnamoorthy2024thespata5spata5l1atpase pages 3-5, krishnamoorthy2024thespata5spata5l1atpase pages 5-7)

The complete complex has **3.6-fold greater ATP hydrolysis than SPATA5 alone**, and replication-fork DNA specifically increases its ATPase activity. Mutating conserved Walker-B residues abolishes hydrolysis. Suggested annotations include ATP hydrolysis activity, DNA binding, protein unfolding, **GO:0006260 DNA replication**, **GO:0005657 replication fork**, and **GO:0000785 chromatin**. (krishnamoorthy2024thespata5spata5l1atpase pages 5-7)

### Replisome proteostasis

55LCC interacts with POLD1/POLD3, RFC1, cohesin components, and other nuclear and cytoplasmic complexes. In S phase and after replication damage, its ATPase/pore activity appears to unfold replisome proteins, making them accessible to calpain-family or related cysteine proteases. Processed substrates include POLD3, RFC1, POLA1, POLD1, ATR, ATRIP, and RAD21. This turnover is largely ubiquitin- and proteasome-independent. The authors’ mechanistic conclusion was that 55LCC “acts as an unfoldase,” facilitating cleavage and removal of replisome proteins from chromatin. (krishnamoorthy2024thespata5spata5l1atpase pages 8-10, krishnamoorthy2024thespata5spata5l1atpase pages 10-12)

### Downstream causal chain

**Biallelic damaging AFG2B variants → impaired 55LCC abundance/assembly/ATPase activity → defective replisome-protein remodeling → replication-fork slowing, stalling, and defective restart → exposed single-stranded DNA and replication stress → later ATR checkpoint activation, cohesion loss, and micronuclei → impaired survival or development of vulnerable neural and auditory cells → developmental disability, motor-system dysfunction, epilepsy, and hearing loss.**

In engineered cells, phosphorylated RPA and fork shortening appeared within 18–24 hours; mitotic abnormalities emerged around 48–72 hours; approximately **25% of cells** had micronuclei after 72 hours of induced depletion. Thus, replication stress is experimentally upstream of chromosomal instability. (krishnamoorthy2024thespata5spata5l1atpase pages 8-10)

An unfolded-protein response, including increased CHOP and spliced XBP1, also followed 55LCC loss. Earlier work additionally links complex members to late ribosome assembly, but the 2024 study found the replication/genome-instability phenotype separable from the reported ribosomal function. No disease-specific patient tissue transcriptome, proteome, metabolome, lipidome, single-cell atlas, spatial transcriptome, or integrated multi-omic signature has yet been established. (krishnamoorthy2024thespata5spata5l1atpase pages 3-5, krishnamoorthy2024thespata5spata5l1atpase pages 8-10)

Suggested cell terms are **neuron**, **glial cell**, and inner-ear **sensory hair cell**; these should be mapped to exact CL identifiers during curation. The evidence for enrichment in neurons, glial nuclei, and neurosensory hair cells comes from later synthesis, whereas the causal replication experiments used cultured cells rather than patient neural tissue. (polczyk2025neurodevelopmentaldisorderwith pages 1-2)

## 7. Anatomical structures affected

The primary systems are the **central nervous system** and **auditory system**. Brain structures implicated by imaging include cerebral cortex, white matter, corpus callosum, periventricular regions, and anterior temporal regions. Motor manifestations implicate corticospinal and extrapyramidal networks, although tract-specific pathology has not been demonstrated. Suggested UBERON mappings include brain, cerebral cortex, cerebral white matter, corpus callosum, inner ear, and cochlea. (polczyk2025neurodevelopmentaldisorderwith pages 7-9, polczyk2025neurodevelopmentaldisorderwith pages 6-7)

Hearing loss is bilateral in the reported detailed case and generally sensorineural, supporting cochlear hair-cell and/or auditory-neural involvement. At the subcellular level, the relevant compartments include nucleus, chromatin, replication fork, and the 55LCC macromolecular complex. (krishnamoorthy2024thespata5spata5l1atpase pages 3-5, polczyk2025neurodevelopmentaldisorderwith pages 2-4)

No consistent primary cardiovascular, pulmonary, renal, hepatic, gastrointestinal, endocrine, immune, or hematologic phenotype has been established for NEDHLS. Thrombocytopenia appears in the broader SPATA5/55LCC disease discussion but should not be assigned to AFG2B-related NEDHLS without patient-level confirmation. (krishnamoorthy2024thespata5spata5l1atpase pages 12-14)

## 8. Temporal development

Onset is **infantile and insidious**, not acute. Developmental delay and hypotonia can be evident by four months; hearing loss may be recognized within the first year; spasticity/dystonia and EEG abnormalities may emerge later. (polczyk2025neurodevelopmentaldisorderwith pages 6-7, polczyk2025neurodevelopmentaldisorderwith pages 2-4)

The course is chronic and lifelong. A practical—not formally validated—staging model is:

1. **Early infancy:** hypotonia, abnormal visual/social engagement, delayed motor milestones, hearing impairment.
2. **Later infancy/childhood:** persistent global delay, abnormal postural control, possible microcephaly and MRI abnormalities.
3. **Evolving course:** spastic-dystonic motor disorder and possible epilepsy/EEG abnormalities.

No relapsing-remitting pattern, spontaneous remission, or disease-defined end stage is known. Early auditory and developmental intervention is rational because infancy is a critical period for language and motor development, but no study has quantified a disease-specific window for modifying the underlying disorder. (polczyk2025neurodevelopmentaldisorderwith pages 7-9, polczyk2025neurodevelopmentaldisorderwith pages 2-4)

## 9. Inheritance and population

Inheritance is **autosomal recessive**. For two confirmed heterozygous carrier parents, standard Mendelian recurrence expectations are 25% affected, 50% carrier, and 25% unaffected/non-carrier per pregnancy, subject to confirmation that both alleles are truly pathogenic. No anticipation is expected, and no founder effect, germline mosaicism rate, carrier frequency, ethnic enrichment, geographic concentration, or sex bias has been demonstrated.

The foundational cohort contained **25 patients**, and a 2025 report described the total literature as fewer than 30 affected individuals. Prevalence, incidence, mortality, and population carrier frequency are unknown; absence from epidemiologic registries should not be interpreted as zero prevalence. (polczyk2025neurodevelopmentaldisorderwith pages 1-2, polczyk2025neurodevelopmentaldisorderwith pages 6-7)

Penetrance among individuals with clearly pathogenic biallelic genotypes appears high for neurodevelopmental impairment, but exact penetrance is not calculable. Expressivity is variable, particularly for epilepsy, microcephaly, imaging abnormalities, and the timing of hypertonia. (polczyk2025neurodevelopmentaldisorderwith pages 7-9)

## 10. Diagnostics

### Clinical workup

The recognizable combination is developmental delay plus bilateral sensorineural hearing loss and hypotonia or evolving spastic-dystonic motor dysfunction. Evaluation should include detailed neurologic/developmental examination, formal audiology or auditory brainstem response, ophthalmology, brain MRI, and EEG when seizures or episodic unresponsiveness are suspected. Serial assessment is important because EEG and tone abnormalities may evolve. (polczyk2025neurodevelopmentaldisorderwith pages 7-9, polczyk2025neurodevelopmentaldisorderwith pages 6-7)

There is no validated blood, urine, enzyme, metabolite, proteomic, epigenetic, biopsy, or liquid-biopsy biomarker. Replication-stress measurements remain research assays.

### Molecular diagnosis

Preferred testing is **trio WES or WGS** with copy-number calling and confirmation of two rare, plausibly damaging AFG2B variants in trans. A neurodevelopmental/hearing-loss/spasticity panel that includes AFG2B is reasonable when rapid targeted testing is preferred. Sanger or equivalent orthogonal confirmation and parental segregation are appropriate. The recent real-world workflow used trio WES, mitochondrial-genome analysis, noncoding ClinVar-variant analysis, CNV assessment, and UPD assessment. (polczyk2025neurodevelopmentaldisorderwith pages 4-6)

WGS may identify noncoding, structural, or poorly captured variants missed by WES, although NEDHLS-specific incremental yield is unknown. RNA sequencing may help resolve suspected splice variants, but no validated disease-specific RNA diagnostic was identified. CMA can exclude alternative pathogenic CNVs but cannot reliably detect most causal single-nucleotide or small indel alleles. Karyotype, FISH, mitochondrial testing, and repeat-expansion testing are not first-line disease-specific tests unless the phenotype suggests another diagnosis.

### Differential diagnosis

Key genetic differentials include **SPATA5/AFG2A-related neurodevelopmental disorder**, HPDL-related neurodegeneration/spasticity, hereditary spastic paraplegias, mitochondrial disorders, congenital infections, and other syndromic hearing-loss/epileptic encephalopathies. SPATA5-related disease reportedly has earlier seizures, more marked microcephaly, and frequent movement disorders, while AFG2B disease more consistently features sensorineural hearing loss and spastic-dystonic cerebral palsy; substantial overlap prevents clinical distinction without molecular testing. (polczyk2025neurodevelopmentaldisorderwith pages 7-9)

No population or newborn genetic screening program exists. Audiologic newborn screening may detect hearing loss but is neither sensitive nor specific for NEDHLS.

## 11. Outcome and prognosis

No 5- or 10-year survival estimates, life-expectancy data, mortality rates, or validated prognostic biomarkers exist. Available reports support persistent developmental and motor disability rather than recovery to typical development. Hearing amplification can improve sound access but does not reverse the genetic neurodevelopmental disorder. (polczyk2025neurodevelopmentaldisorderwith pages 7-9, polczyk2025neurodevelopmentaldisorderwith pages 2-4)

Potential long-term morbidity includes severe communication impairment, limited mobility, contractures from spasticity, epilepsy, feeding or nutritional difficulty secondary to neurologic disability, and caregiver burden, although NEDHLS-specific complication rates are unavailable. Younger age without seizures or spasticity cannot be assumed to predict a mild course because these features may emerge later. (polczyk2025neurodevelopmentaldisorderwith pages 7-9, polczyk2025neurodevelopmentaldisorderwith pages 6-7)

## 12. Treatment and current implementation

There is **no approved disease-modifying pharmacotherapy**, gene therapy, RNA therapy, cell therapy, or genotype-guided drug. No relevant disease-specific interventional trial was identified by searching the disease name and AFG2B/SPATA5L1.

Current treatment is multidisciplinary and phenotype-directed:

* hearing aids; cochlear-implant assessment if hearing loss meets standard audiologic criteria;
* early communication intervention, including speech-language and hearing rehabilitation;
* physical and occupational therapy, positioning, mobility devices, and contracture prevention;
* standard spasticity management where needed, potentially including oral antispastic medication, botulinum toxin, orthoses, or specialist procedures;
* standard antiseizure medication selected according to seizure type if epilepsy is confirmed;
* nutritional/feeding, ophthalmologic, orthopedic, and psychosocial support.

The detailed 2025 case used hearing aids and early reflex-locomotion/Vojta-oriented rehabilitation. The report documented persistent abnormalities, not a controlled treatment-response estimate. Suggested NCIT concepts include hearing-aid intervention, physical therapy, occupational therapy, speech therapy, rehabilitation, anticonvulsant therapy, and botulinum-toxin treatment; exact NCIT identifiers require terminology-service validation. (polczyk2025neurodevelopmentaldisorderwith pages 4-6, polczyk2025neurodevelopmentaldisorderwith pages 7-9, polczyk2025neurodevelopmentaldisorderwith pages 2-4)

The 2024 mechanism identifies 55LCC, calpain-linked processing, replication stress, and proteostasis as research targets, but directly inhibiting this essential complex would be biologically risky: all four components were pan-essential across several cell lines. Mechanistic rescue or gene-replacement approaches remain preclinical concepts, not current clinical applications. (krishnamoorthy2024thespata5spata5l1atpase pages 3-5, krishnamoorthy2024thespata5spata5l1atpase pages 10-12)

## 13. Prevention

There is no vaccine, behavioral prevention, environmental prophylaxis, or medication that prevents disease in a person with a causal biallelic genotype.

**Primary genetic prevention/reproductive options** include carrier testing of parents and adult relatives, genetic counseling, partner testing, preimplantation genetic testing for monogenic disease, and prenatal diagnosis by chorionic-villus sampling or amniocentesis once familial variants are established. **Secondary prevention** consists of early molecular diagnosis, audiology, developmental surveillance, and seizure monitoring. **Tertiary prevention** targets complications through rehabilitation, hearing support, spasticity management, orthopedic surveillance, and epilepsy treatment.

Variant interpretation must be finalized before using a familial allele for reproductive testing, particularly when one allele remains a VUS. (polczyk2025neurodevelopmentaldisorderwith pages 4-6)

## 14. Other species and natural disease

No naturally occurring AFG2B-equivalent syndrome in a companion animal, livestock species, or wildlife population was identified. Consequently, breed ontology identifiers, veterinary prevalence, and zoonotic transmission are not applicable. The disorder is inherited rather than transmissible.

AFG2B/SPATA5L1 orthologs and the ATPase/proteostasis machinery are evolutionarily conserved, enabling experimental modeling, but conservation alone does not establish a spontaneous veterinary disease.

## 15. Model organisms and experimental systems

The strongest disease-relevant models currently retrieved are **in vitro biochemical and engineered human-cell systems**, not a fully validated organismal NEDHLS model.

* Recombinant 55LCC supported ATPase, nucleic-acid-binding, thermal-stability, mass-photometry, native-mass-spectrometry, and cryo-EM studies.
* HeLa S3 and engineered degron/CRISPR-rescue systems established complex essentiality, patient-variant effects, replication-fork defects, stress responses, cohesion loss, and micronucleation.
* DNA-fiber assays, iPOND, chromatin fractionation, co-immunoprecipitation, and mass spectrometry defined replisome interactions and temporal effects. (krishnamoorthy2024thespata5spata5l1atpase pages 7-8, krishnamoorthy2024thespata5spata5l1atpase pages 41-46, krishnamoorthy2024thespata5spata5l1atpase pages 3-5, krishnamoorthy2024thespata5spata5l1atpase pages 8-10)

These models reproduce the molecular defect—impaired replisome proteostasis and genome stability—but cannot by themselves reproduce cognition, spastic-dystonic cerebral palsy, hearing behavior, or developmental trajectories. No retrieved evidence established a stable Afg2b-knockout mouse, rat, zebrafish, Drosophila, patient-derived iPSC neuron, cochlear organoid, or cerebral organoid that recapitulates NEDHLS. Such models are priorities for resolving tissue selectivity and testing allele-specific rescue.

## Evidence appraisal and principal knowledge gaps

The **human disease association** is strong because multiple unrelated patients carry recessive biallelic variants with compatible phenotypes and familial segregation. The **molecular mechanism** is supported by high-quality structural, biochemical, and cell-biological experiments published in 2024. However, the bridge from replication stress to selective human brain and cochlear pathology remains inferential. (OpenTargets Search: Neurodevelopmental disorder with hearing loss and spasticity, krishnamoorthy2024thespata5spata5l1atpase pages 7-8, krishnamoorthy2024thespata5spata5l1atpase pages 1-3)

The most important gaps are: reliable phenotype frequencies from expanded cohorts; longitudinal natural history; variant-level penetrance and functional calibration; population carrier frequency; validated neural/cochlear models; patient-derived multi-omics; quantitative quality-of-life outcomes; treatment-response data; and disease-specific clinical trials.

### Key abstract-supported statements

The foundational paper’s title itself states the principal human conclusion: **“Bi-allelic variants in SPATA5L1 lead to intellectual disability, spastic-dystonic cerebral palsy, epilepsy, and hearing loss.”** PMID 34626583; October 2021; [DOI URL](https://doi.org/10.1016/j.ajhg.2021.08.003). (OpenTargets Search: Neurodevelopmental disorder with hearing loss and spasticity, polczyk2025neurodevelopmentaldisorderwith pages 9-10)

The 2024 mechanistic study concluded that the complex processes replisome substrates and regulates genome stability, proposing that **“55LCC acts as an unfoldase”** and facilitates subsequent cysteine-protease cleavage and removal of replisome proteins from chromatin. PMID 38554706; April 2024; [DOI URL](https://doi.org/10.1016/j.cell.2024.03.002). (krishnamoorthy2024thespata5spata5l1atpase pages 10-12)

A 2025 detailed case report concluded that integrating genomic sequencing with structured motor assessment can refine recognition and management; it also documented that biallelic disease may initially present with hypotonia and no confirmed epilepsy, illustrating age-dependent and variable expression. Published November 2025; [DOI 10.3390/jcm14238442](https://doi.org/10.3390/jcm14238442). (polczyk2025neurodevelopmentaldisorderwith pages 1-2, polczyk2025neurodevelopmentaldisorderwith pages 7-9)

References

1. (OpenTargets Search: Neurodevelopmental disorder with hearing loss and spasticity): Open Targets Query (Neurodevelopmental disorder with hearing loss and spasticity, 6 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (polczyk2025neurodevelopmentaldisorderwith pages 1-2): Artur Polczyk, Ewelina Wolańska, Anna Zimny, Agnieszka Zubkiewicz-Kucharska, Mateusz Biela, Agnieszka Pawelak, and Robert Śmigiel. Neurodevelopmental disorder with psychomotor delay, hearing loss, and spasticity caused by compound heterozygous spata5l1 variants—expanding phenotype. Journal of Clinical Medicine, 14:8442, Nov 2025. URL: https://doi.org/10.3390/jcm14238442, doi:10.3390/jcm14238442. This article has 1 citations.

3. (polczyk2025neurodevelopmentaldisorderwith pages 6-7): Artur Polczyk, Ewelina Wolańska, Anna Zimny, Agnieszka Zubkiewicz-Kucharska, Mateusz Biela, Agnieszka Pawelak, and Robert Śmigiel. Neurodevelopmental disorder with psychomotor delay, hearing loss, and spasticity caused by compound heterozygous spata5l1 variants—expanding phenotype. Journal of Clinical Medicine, 14:8442, Nov 2025. URL: https://doi.org/10.3390/jcm14238442, doi:10.3390/jcm14238442. This article has 1 citations.

4. (krishnamoorthy2024thespata5spata5l1atpase pages 1-3): Vidhya Krishnamoorthy, Martina Foglizzo, Robert L. Dilley, Angela Wu, Arindam Datta, Parul Dutta, Lisa J. Campbell, Oksana Degtjarik, Laura J. Musgrove, Antonio N. Calabrese, Elton Zeqiraj, and Roger A. Greenberg. The spata5-spata5l1 atpase complex directs replisome proteostasis to ensure genome integrity. Cell, 187:2250-2268.e31, Apr 2024. URL: https://doi.org/10.1016/j.cell.2024.03.002, doi:10.1016/j.cell.2024.03.002. This article has 18 citations and is from a highest quality peer-reviewed journal.

5. (krishnamoorthy2024thespata5spata5l1atpase pages 8-10): Vidhya Krishnamoorthy, Martina Foglizzo, Robert L. Dilley, Angela Wu, Arindam Datta, Parul Dutta, Lisa J. Campbell, Oksana Degtjarik, Laura J. Musgrove, Antonio N. Calabrese, Elton Zeqiraj, and Roger A. Greenberg. The spata5-spata5l1 atpase complex directs replisome proteostasis to ensure genome integrity. Cell, 187:2250-2268.e31, Apr 2024. URL: https://doi.org/10.1016/j.cell.2024.03.002, doi:10.1016/j.cell.2024.03.002. This article has 18 citations and is from a highest quality peer-reviewed journal.

6. (krishnamoorthy2024thespata5spata5l1atpase pages 10-12): Vidhya Krishnamoorthy, Martina Foglizzo, Robert L. Dilley, Angela Wu, Arindam Datta, Parul Dutta, Lisa J. Campbell, Oksana Degtjarik, Laura J. Musgrove, Antonio N. Calabrese, Elton Zeqiraj, and Roger A. Greenberg. The spata5-spata5l1 atpase complex directs replisome proteostasis to ensure genome integrity. Cell, 187:2250-2268.e31, Apr 2024. URL: https://doi.org/10.1016/j.cell.2024.03.002, doi:10.1016/j.cell.2024.03.002. This article has 18 citations and is from a highest quality peer-reviewed journal.

7. (polczyk2025neurodevelopmentaldisorderwith pages 4-6): Artur Polczyk, Ewelina Wolańska, Anna Zimny, Agnieszka Zubkiewicz-Kucharska, Mateusz Biela, Agnieszka Pawelak, and Robert Śmigiel. Neurodevelopmental disorder with psychomotor delay, hearing loss, and spasticity caused by compound heterozygous spata5l1 variants—expanding phenotype. Journal of Clinical Medicine, 14:8442, Nov 2025. URL: https://doi.org/10.3390/jcm14238442, doi:10.3390/jcm14238442. This article has 1 citations.

8. (polczyk2025neurodevelopmentaldisorderwith pages 7-9): Artur Polczyk, Ewelina Wolańska, Anna Zimny, Agnieszka Zubkiewicz-Kucharska, Mateusz Biela, Agnieszka Pawelak, and Robert Śmigiel. Neurodevelopmental disorder with psychomotor delay, hearing loss, and spasticity caused by compound heterozygous spata5l1 variants—expanding phenotype. Journal of Clinical Medicine, 14:8442, Nov 2025. URL: https://doi.org/10.3390/jcm14238442, doi:10.3390/jcm14238442. This article has 1 citations.

9. (polczyk2025neurodevelopmentaldisorderwith pages 9-10): Artur Polczyk, Ewelina Wolańska, Anna Zimny, Agnieszka Zubkiewicz-Kucharska, Mateusz Biela, Agnieszka Pawelak, and Robert Śmigiel. Neurodevelopmental disorder with psychomotor delay, hearing loss, and spasticity caused by compound heterozygous spata5l1 variants—expanding phenotype. Journal of Clinical Medicine, 14:8442, Nov 2025. URL: https://doi.org/10.3390/jcm14238442, doi:10.3390/jcm14238442. This article has 1 citations.

10. (polczyk2025neurodevelopmentaldisorderwith pages 2-4): Artur Polczyk, Ewelina Wolańska, Anna Zimny, Agnieszka Zubkiewicz-Kucharska, Mateusz Biela, Agnieszka Pawelak, and Robert Śmigiel. Neurodevelopmental disorder with psychomotor delay, hearing loss, and spasticity caused by compound heterozygous spata5l1 variants—expanding phenotype. Journal of Clinical Medicine, 14:8442, Nov 2025. URL: https://doi.org/10.3390/jcm14238442, doi:10.3390/jcm14238442. This article has 1 citations.

11. (krishnamoorthy2024thespata5spata5l1atpase pages 5-7): Vidhya Krishnamoorthy, Martina Foglizzo, Robert L. Dilley, Angela Wu, Arindam Datta, Parul Dutta, Lisa J. Campbell, Oksana Degtjarik, Laura J. Musgrove, Antonio N. Calabrese, Elton Zeqiraj, and Roger A. Greenberg. The spata5-spata5l1 atpase complex directs replisome proteostasis to ensure genome integrity. Cell, 187:2250-2268.e31, Apr 2024. URL: https://doi.org/10.1016/j.cell.2024.03.002, doi:10.1016/j.cell.2024.03.002. This article has 18 citations and is from a highest quality peer-reviewed journal.

12. (krishnamoorthy2024thespata5spata5l1atpase pages 3-5): Vidhya Krishnamoorthy, Martina Foglizzo, Robert L. Dilley, Angela Wu, Arindam Datta, Parul Dutta, Lisa J. Campbell, Oksana Degtjarik, Laura J. Musgrove, Antonio N. Calabrese, Elton Zeqiraj, and Roger A. Greenberg. The spata5-spata5l1 atpase complex directs replisome proteostasis to ensure genome integrity. Cell, 187:2250-2268.e31, Apr 2024. URL: https://doi.org/10.1016/j.cell.2024.03.002, doi:10.1016/j.cell.2024.03.002. This article has 18 citations and is from a highest quality peer-reviewed journal.

13. (krishnamoorthy2024thespata5spata5l1atpase pages 7-8): Vidhya Krishnamoorthy, Martina Foglizzo, Robert L. Dilley, Angela Wu, Arindam Datta, Parul Dutta, Lisa J. Campbell, Oksana Degtjarik, Laura J. Musgrove, Antonio N. Calabrese, Elton Zeqiraj, and Roger A. Greenberg. The spata5-spata5l1 atpase complex directs replisome proteostasis to ensure genome integrity. Cell, 187:2250-2268.e31, Apr 2024. URL: https://doi.org/10.1016/j.cell.2024.03.002, doi:10.1016/j.cell.2024.03.002. This article has 18 citations and is from a highest quality peer-reviewed journal.

14. (krishnamoorthy2024thespata5spata5l1atpase pages 12-14): Vidhya Krishnamoorthy, Martina Foglizzo, Robert L. Dilley, Angela Wu, Arindam Datta, Parul Dutta, Lisa J. Campbell, Oksana Degtjarik, Laura J. Musgrove, Antonio N. Calabrese, Elton Zeqiraj, and Roger A. Greenberg. The spata5-spata5l1 atpase complex directs replisome proteostasis to ensure genome integrity. Cell, 187:2250-2268.e31, Apr 2024. URL: https://doi.org/10.1016/j.cell.2024.03.002, doi:10.1016/j.cell.2024.03.002. This article has 18 citations and is from a highest quality peer-reviewed journal.

15. (krishnamoorthy2024thespata5spata5l1atpase pages 41-46): Vidhya Krishnamoorthy, Martina Foglizzo, Robert L. Dilley, Angela Wu, Arindam Datta, Parul Dutta, Lisa J. Campbell, Oksana Degtjarik, Laura J. Musgrove, Antonio N. Calabrese, Elton Zeqiraj, and Roger A. Greenberg. The spata5-spata5l1 atpase complex directs replisome proteostasis to ensure genome integrity. Cell, 187:2250-2268.e31, Apr 2024. URL: https://doi.org/10.1016/j.cell.2024.03.002, doi:10.1016/j.cell.2024.03.002. This article has 18 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Neurodevelopmental_Disorder_with_Hearing_Loss_and_Spasticity-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.3390/jcm14238442](https://doi.org/10.3390/jcm14238442` (1 mention) - Identifier did not resolve to a record