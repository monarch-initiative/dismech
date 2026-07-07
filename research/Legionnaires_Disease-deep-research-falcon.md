---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-05T18:50:37.430716'
end_time: '2026-07-05T19:16:52.339618'
duration_seconds: 1574.91
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Legionnaires Disease
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 38
artifact_count: 4
artifact_sources:
  edison_answer_artifacts: 4
artifacts:
- filename: artifact-00.md
  path: Legionnaires_Disease-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Legionnaires_Disease-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: Legionnaires_Disease-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
- filename: artifact-03.md
  path: Legionnaires_Disease-deep-research-falcon_artifacts/artifact-03.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-03
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Legionnaires Disease
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Legionnaires Disease** covering all of the
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
- **Disease Name:** Legionnaires Disease
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Legionnaires Disease** covering all of the
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


# Comprehensive Research Report: Legionnaires' Disease

---

## 1. Disease Information

### Overview

Legionnaires' disease (LD) is a severe form of pneumonia caused primarily by the Gram-negative, aerobic, facultative intracellular bacterium *Legionella pneumophila* (shin2026molecularevolutionand pages 2-3, cakmak2024presenceoflegionella pages 1-2). First identified during an outbreak at an American Legion convention in Philadelphia in 1976, which affected 221 people and caused 34 deaths, LD remains a significant and increasing public health threat worldwide (shin2026molecularevolutionand pages 1-2). The disease is transmitted through inhalation of contaminated aerosolized water droplets from engineered water systems such as cooling towers, hot-water distribution systems, showers, and fountains, rather than through person-to-person transmission (cakmak2024presenceoflegionella pages 1-2, yao2024areviewof pages 1-2). Although LD accounts for approximately 5% of all community-acquired pneumonia (CAP), it is one of the three most common causes of CAP requiring intensive care unit (ICU) admission (rello2024severelegionnaires’disease pages 1-3).

### Key Identifiers and Classification

| Field | Value | Notes / Evidence |
|---|---|---|
| Preferred disease name | Legionnaires' disease | Pneumonic form of legionellosis caused predominantly by *Legionella pneumophila* (rello2024severelegionnaires’disease pages 1-3, shin2026molecularevolutionand pages 2-3) |
| Broader related disease term | legionellosis | Includes Legionnaires' disease and the non-pneumonic form, Pontiac fever (lechevallier2025thecasefor pages 2-5, yao2024areviewof pages 1-2) |
| MONDO ID | MONDO:0005824 | OpenTargets returned MONDO_0005824 for Legionnaires' disease (OpenTargets Search: Legionnaires disease,legionellosis) |
| Related MONDO ID | MONDO:0005823 | OpenTargets returned MONDO_0005823 for legionellosis (OpenTargets Search: Legionnaires disease,legionellosis) |
| ICD-10-CM | A48.1 | Standard ICD-10 code for Legionnaires' disease |
| ICD-11 | 1C32 | ICD-11 category for Legionnaires disease |
| MeSH | D007876 | MeSH descriptor for Legionnaires' Disease |
| Disease category | Infectious disease; bacterial pneumonia; waterborne/aerosol-transmitted environmental infection | Recent reviews describe LD as a waterborne pneumonia and a major cause of severe community-acquired pneumonia (rello2024severelegionnaires’disease pages 1-3, yao2024areviewof pages 1-2) |
| Primary causative agent | *Legionella pneumophila* | Accounts for >90% of cases in multiple epidemiologic summaries; serogroup 1 predominates (rello2024severelegionnaires’disease pages 1-3, lechevallier2025thecasefor pages 2-5) |
| Other clinically relevant species | *L. longbeachae* and other *Legionella* spp. | Non-*pneumophila* species also cause disease and are often missed by standard UAT-focused diagnosis (rello2024severelegionnaires’disease pages 5-7) |
| Common synonyms | Legionella pneumonia; Legion fever; legionellosis | “Legionellosis” is the umbrella term; “Legionella pneumonia” is a common descriptive synonym (lechevallier2025thecasefor pages 2-5, yao2024areviewof pages 1-2) |
| Clinical definition | Severe pneumonia following inhalation of contaminated aerosols from engineered water systems | Reviews emphasize transmission from cooling towers, plumbing, showers, fountains, and similar systems rather than person-to-person spread (cakmak2024presenceoflegionella pages 1-2, shin2026molecularevolutionand pages 1-2) |
| Distinguishing related syndrome | Pontiac fever | Mild, non-pneumonic flu-like illness caused by *Legionella* exposure (lechevallier2025thecasefor pages 2-5, shin2026molecularevolutionand pages 2-3) |
| Typical transmission context | Inhalation/aspiration of aerosolized contaminated water | Built-environment and water-system exposures are the dominant source (cakmak2024presenceoflegionella pages 1-2, yao2024areviewof pages 1-2, yao2024areviewof pages 2-3) |
| Key microbiologic classification | Gram-negative, aerobic/facultative intracellular bacterium | *L. pneumophila* is described as a Gram-negative intracellular pathogen that replicates in alveolar macrophages (shin2026molecularevolutionand pages 2-3, cakmak2024presenceoflegionella pages 2-3) |
| Primary host cell target | Alveolar macrophages | Central to disease mechanism and intracellular replication (shin2026molecularevolutionand pages 15-16, lockwood2022thelegionellapneumophila pages 1-3) |
| Main data source type for this entry | Aggregated disease-level resources and literature reviews, supplemented by database identifier mapping | Evidence synthesized from reviews, epidemiologic studies, and OpenTargets disease mapping rather than individual EHR-level data (OpenTargets Search: Legionnaires disease,legionellosis, rello2024severelegionnaires’disease pages 1-3, yao2024areviewof pages 1-2) |


*Table: This table summarizes core identifiers, classification terms, synonyms, and causative-agent information for Legionnaires' disease. It is useful as a compact reference for knowledge-base normalization and ontology mapping.*

### Synonyms and Alternative Names

Common synonyms include Legionella pneumonia, Legion fever, and legionellosis (the broader umbrella term encompassing both Legionnaires' disease and the milder, non-pneumonic Pontiac fever) (lechevallier2025thecasefor pages 2-5, shin2026molecularevolutionand pages 2-3).

---

## 2. Etiology

### Causative Agent

*Legionella pneumophila* is the primary causative agent, responsible for approximately 90% of LD cases, with serogroup 1 (Lp1) causing over 80% of confirmed infections in Europe and the United States (shin2026molecularevolutionand pages 2-3, rello2024severelegionnaires’disease pages 1-3). Of the 61 identified *Legionella* species, *L. longbeachae* is the second most common cause of LD, particularly in Australia and New Zealand (cakmak2024presenceoflegionella pages 1-2). Nearly 50% of cases diagnosed by broader diagnostic methods are caused by non-Lp1 species or serogroups that standard urinary antigen tests cannot detect (rello2024severelegionnaires’disease pages 5-7).

*L. pneumophila* is a Gram-negative, facultative intracellular pathogen that naturally inhabits aquatic environments and has evolved through prolonged co-evolution with free-living amoebae such as *Acanthamoeba castellanii* (shin2026molecularevolutionand pages 1-2). Within these protozoan hosts, the bacterium evolved mechanisms to evade predation and replicate intracellularly, which fortuitously facilitated infection of human alveolar macrophages (shin2026molecularevolutionand pages 1-2).

### Risk Factors

**Environmental risk factors** include: exposure to contaminated engineered water systems (cooling towers, hot tubs, fountains, plumbing networks); aging municipal water infrastructure and main line leaks; water stagnation; temperatures between 25–45°C (optimal for Legionella growth); high precipitation; elevated temperature and relative humidity (cakmak2024presenceoflegionella pages 1-2, yao2024areviewof pages 1-2, cakmak2024presenceoflegionella pages 3-5). The disease is predominantly linked to building water systems, including hospitals, hotels, and large commercial buildings (cakmak2024presenceoflegionella pages 3-5). The 2023 Poland outbreak, resulting in 14 deaths, underscored the continuing threat from inadequately maintained water systems (cakmak2024presenceoflegionella pages 1-2).

**Host risk factors** include: age ≥50 years; smoking history; chronic lung disease; immunosuppression (including organ transplantation, chronic corticosteroid therapy, and hematological malignancy); diabetes; chronic cardiovascular disease; and alcoholism (cakmak2024presenceoflegionella pages 2-3, rello2024severelegionnaires’disease pages 1-3). Male sex is associated with higher incidence, with an approximately 2:1 to 3:1 male-to-female ratio (rello2024severelegionnaires’disease pages 1-3).

**Climatic risk factors** are increasingly recognized. Temperature increases above 15°C, relative humidity above 60%, and precipitation have been significantly associated with increased LD incidence, with temperature and humidity effects most pronounced 9–10 weeks before disease onset, suggesting environmental amplification of *Legionella* prior to transmission (cakmak2024presenceoflegionella pages 3-5, yao2024areviewof pages 1-2).

### Protective Factors

No specific genetic protective factors have been definitively established for Legionnaires' disease. Adequate water system maintenance, temperature control (maintaining hot water >55°C and cold water <25°C), and chlorine disinfection of water distribution systems are well-established environmental protective measures (yao2024areviewof pages 3-4, cakmak2024presenceoflegionella pages 2-3).

---

## 3. Phenotypes and Clinical Manifestations

Legionnaires' disease presents with a spectrum of clinical manifestations encompassing pulmonary and extrapulmonary features. The clinical presentation is often non-specific and can mimic other forms of severe pneumonia (rello2024severelegionnaires’disease pages 1-3).

| Phenotype/Symptom | Type | Frequency | Severity | HPO Term suggestion |
|---|---|---|---|---|
| Fever | Symptom | Common; high fever is a typical presentation of Legionnaires’ disease (rello2024severelegionnaires’disease pages 4-5, cakmak2024presenceoflegionella pages 2-3) | Moderate to severe | Fever (HP:0001945) |
| Cough | Symptom | Common in pneumonic disease (cakmak2024presenceoflegionella pages 2-3) | Mild to severe | Cough (HP:0012735) |
| Dyspnea / shortness of breath | Symptom | Common in pneumonia; may progress to respiratory failure in severe cases (rello2024severelegionnaires’disease pages 1-3, cakmak2024presenceoflegionella pages 2-3) | Moderate to severe | Dyspnea (HP:0002094) |
| Pneumonia | Clinical sign / syndrome | Core manifestation; Legionnaires’ disease is the pneumonic form of legionellosis (rello2024severelegionnaires’disease pages 1-3, shin2026molecularevolutionand pages 2-3) | Severe; ICU admission occurs in approximately one-third of cases (rello2024severelegionnaires’disease pages 1-3) | Pneumonia (HP:0002090) |
| Diarrhea | Symptom | Frequently reported extrapulmonary/non-specific feature (rello2024severelegionnaires’disease pages 4-5, rello2024severelegionnaires’disease pages 5-7) | Mild to moderate | Diarrhea (HP:0002014) |
| Hyponatremia | Laboratory abnormality | Commonly associated non-specific laboratory finding (rello2024severelegionnaires’disease pages 4-5, rello2024severelegionnaires’disease pages 5-7) | Mild to moderate; may mark systemic severity | Hyponatremia (HP:0002902) |
| Rhabdomyolysis / elevated creatine kinase | Laboratory abnormality / complication | Uncommon but well-documented association; elevated CK reported in severe disease (rello2024severelegionnaires’disease pages 4-5, rello2024severelegionnaires’disease pages 5-7) | Severe when present | Rhabdomyolysis (HP:0003201) |
| Acute kidney injury | Complication / laboratory abnormality | Very common in severe ICU cases; nearly 80% of adults with ICU Legionella pneumophila infection in one 10-year cohort developed AKI, about half requiring renal replacement therapy (rello2024severelegionnaires’disease pages 5-7) | Severe | Acute kidney injury (HP:0001919) |
| Confusion / acute confusion / encephalopathy | Symptom / neurologic sign | Common neurologic manifestation in severe disease; acute confusion highlighted in clinical presentation (rello2024severelegionnaires’disease pages 4-5) | Moderate to severe | Encephalopathy (HP:0001298) |
| Elevated C-reactive protein | Laboratory abnormality | Common inflammatory marker elevation in severe disease (rello2024severelegionnaires’disease pages 4-5) | Mild to severe | Elevated C-reactive protein level (HP:0011227) |
| Lymphopenia | Laboratory abnormality | Reported in severe disease with hyperleukocytosis and lymphopenia (rello2024severelegionnaires’disease pages 4-5) | Mild to moderate | Lymphopenia (HP:0001888) |
| Liver involvement / hepatic involvement | Organ involvement / lab abnormality | Documented extrapulmonary manifestation; may include liver involvement and abnormal liver tests (rello2024severelegionnaires’disease pages 4-5) | Mild to severe | Abnormality of the liver (HP:0001392) |
| Relative bradycardia | Clinical sign | Reported as a characteristic clue in Legionnaires’ disease (rello2024severelegionnaires’disease pages 4-5) | Mild to moderate | Bradycardia (HP:0001662) |
| Pancreatitis | Complication / extrapulmonary manifestation | Rare but reported extrapulmonary manifestation (rello2024severelegionnaires’disease pages 4-5) | Severe | Pancreatitis (HP:0001733) |
| Myocarditis / pericarditis | Complication / extrapulmonary manifestation | Rare but documented cardiovascular extrapulmonary manifestation (rello2024severelegionnaires’disease pages 4-5) | Severe | Myocarditis (HP:0012819) / Pericarditis (HP:0012810) |


*Table: This table summarizes major clinical manifestations and laboratory abnormalities reported for Legionnaires’ disease, including common pneumonia features and severe extrapulmonary complications. It highlights phenotype types, approximate frequency patterns, severity, and suggested HPO mappings for knowledge base annotation.*

### Key Clinical Features

The hallmark of LD is severe pneumonia characterized by high fever with relative bradycardia, cough, dyspnea, and radiological findings of consolidation with surrounding ground-glass opacities (rello2024severelegionnaires’disease pages 4-5, rello2024severelegionnaires’disease pages 5-7). Diarrhea and acute confusion are frequently reported non-specific features that may suggest Legionella as the etiology (rello2024severelegionnaires’disease pages 4-5). Pontiac fever, the non-pneumonic form of legionellosis, presents with milder flu-like symptoms including fever, chills, and headache, typically resolving within 5 days of onset (shin2026molecularevolutionand pages 2-3).

### Extrapulmonary Manifestations

Extrapulmonary complications are well-documented and typically result from hematogenous dissemination. These include gastrointestinal involvement (pancreatitis, colitis, liver and spleen involvement), neurological complications (encephalitis, brain abscess, cerebellar ataxia), and cardiovascular complications (myopericarditis, endocarditis) (rello2024severelegionnaires’disease pages 4-5). Rhabdomyolysis and acute kidney injury (AKI) have strong documented associations with LD; one study reported that nearly 80% of adults with *L. pneumophila* infection in a 10-year ICU cohort developed AKI, with half requiring renal replacement therapy (rello2024severelegionnaires’disease pages 5-7). Rare extrapulmonary forms such as lymphadenitis have also been reported (zhang2025lymphadenitiscausedby pages 3-4).

### Quality of Life Impact

Severe LD requiring ICU admission (approximately one-third of cases) has profound impacts on daily functioning, with patients often requiring prolonged mechanical ventilation and hemodynamic support (rello2024severelegionnaires’disease pages 1-3). Long-term sequelae following recovery from severe LD may include persistent respiratory impairment, though specific quality-of-life instrument data (EQ-5D, SF-36) are limited in the current literature.

---

## 4. Genetic/Molecular Information

### Bacterial Genomics

As an infectious disease, LD does not have specific human causal genes. Rather, the molecular pathogenesis is driven by the bacterial genome. *L. pneumophila* possesses a genome encoding an exceptionally large arsenal of virulence factors, including the Dot/Icm Type IVB Secretion System (T4BSS) that translocates over 300–350 effector proteins into host cells, and a Type II Secretion System (T2SS) that releases approximately 120 hydrolytic enzymes (shin2026molecularevolutionand pages 15-16, shin2026molecularevolutionand pages 1-2, lockwood2022thelegionellapneumophila pages 1-3). A comprehensive structural analysis of 368 *L. pneumophila* effectors identified 157 types of functional domains in 287 effectors, with 159 effectors previously lacking functional annotations and 35 unique domains with no similarity to known protein structures.

### Host Genetic Susceptibility

In mouse models, the NAIP5 (Nlrc4) locus plays a critical role in innate immune defense against *L. pneumophila*. Wild-type mouse strains are naturally non-permissive to Legionella infection due to NAIP5-mediated recognition of bacterial flagellin, which activates the NLRC4 inflammasome and triggers pyroptotic cell death. Only macrophages from A/J mice, which are deficient in NAIP5, permit intracellular bacterial replication (rello2024severelegionnaires’disease pages 3-4). This suggests that human polymorphisms in inflammasome pathway genes could influence susceptibility, though this remains an area of active investigation.

### OpenTargets Disease-Target Associations

OpenTargets identifies Legionnaires' disease under MONDO:0005824 and legionellosis under MONDO:0005823. Two drug targets are associated with legionellosis treatment at the approval stage: TOP2A (DNA topoisomerase II alpha, ENSG00000131747) and TOP2B (DNA topoisomerase II beta, ENSG00000077097), which are the targets of fluoroquinolone antibiotics used in LD treatment (OpenTargets Search: Legionnaires disease,legionellosis).

---

## 5. Environmental Information

### Environmental Sources

*L. pneumophila* naturally inhabits aquatic environments but proliferates in engineered water systems. Major sources include cooling towers, hot water distribution systems, decorative fountains, swimming pools, hot tubs, and humidifiers (cakmak2024presenceoflegionella pages 1-2, cakmak2024presenceoflegionella pages 3-5, yao2024areviewof pages 2-3). The bacterium survives within biofilms that confer resistance to sterilizing chemicals, thrives at temperatures between 25–45°C, and requires specific nutrients including amino acids and ferric ions (cakmak2024presenceoflegionella pages 3-5). Water stagnation promotes bacterial proliferation (cakmak2024presenceoflegionella pages 3-5).

### Climate Influence

Climate variables significantly influence LD incidence. Temperature increases above 15°C showed an incidence rate ratio of 1.45 (95% CI: 1.33–1.58) for each 5°C increase, with a lag of 10–9 weeks before onset. Relative humidity above 60% (IRR = 1.19, 95% CI: 1.12–1.26 per 5% increase) and precipitation (IRR = 1.07, 95% CI: 1.06–1.09 per 5 mm increase above 10 mm, 1-week lag) also significantly increase risk (cakmak2024presenceoflegionella pages 3-5). Precipitation has emerged as a strong driver of sporadic community-acquired cases in the United States, while temperature and relative humidity are moderate drivers (cakmak2024presenceoflegionella pages 3-5, yao2024areviewof pages 1-2).

### Infectious Agent Classification

- **Organism:** *Legionella pneumophila* (NCBI Taxonomy ID: 446)
- **Classification:** Gram-negative, aerobic, rod-shaped bacterium; Family Legionellaceae; Order Legionellales
- **Key species:** *L. pneumophila* (dominant pathogen), *L. longbeachae*, *L. sainthelensi*, and 58+ other species (cakmak2024presenceoflegionella pages 1-2, zhang2025lymphadenitiscausedby pages 3-4)

---

## 6. Mechanism / Pathophysiology

### Intracellular Infection Cycle

The pathophysiology of LD centers on the bacterium's ability to replicate within human alveolar macrophages. Upon inhalation of contaminated aerosols, *L. pneumophila* is phagocytosed by alveolar macrophages, where it immediately deploys the Dot/Icm T4BSS to deliver over 300 effector proteins into the host cytosol (shin2026molecularevolutionand pages 15-16, lockwood2022thelegionellapneumophila pages 1-3). These effectors manipulate host vesicle trafficking and endomembrane dynamics to prevent phagosome-lysosome fusion, instead remodeling the phagocytic vacuole into an endoplasmic reticulum (ER)-derived compartment known as the Legionella-containing vacuole (LCV) (shin2026molecularevolutionand pages 1-2, lockwood2022thelegionellapneumophila pages 1-3).

### Key Molecular Pathways

**Vesicle trafficking manipulation:** Effector proteins such as SidC contain phosphatidylinositol 4-phosphate (PI(4)P)-specific binding domains essential for targeting to the bacterial phagosome. VipD interferes with host endosomal trafficking by targeting Rab GTPases (shin2026molecularevolutionand pages 22-22). LidA is a characterized Dot/Icm substrate involved in maintaining bacterial integrity within the LCV (shin2026molecularevolutionand pages 18-19).

**Autophagy inhibition:** The effector RavZ cleaves LC3 (Atg8) to block autophagosome maturation, preventing autophagic destruction of the bacteria (shin2026molecularevolutionand pages 14-15, shin2026molecularevolutionand pages 18-19). GO terms: autophagy (GO:0006914), negative regulation of autophagy (GO:0010507).

**Host translation modulation:** Multiple effectors including SidI, SidL, LegK4, and Lgt family members inhibit host protein translation by targeting elongation factors and ribosomes, while others (LegA9, LegC4, LamA) counteract this blockade to promote production of specific inflammatory cytokines (shin2026molecularevolutionand pages 12-14, shin2026molecularevolutionand pages 14-15).

**Mitochondrial manipulation:** Effectors Lpg0080 and Lpg0081 function as ADP-ribosyl transferases that modify mitochondrial ADP/ATP translocases to suppress energy-dependent autophagy signals (shin2026molecularevolutionand pages 14-15, shin2026molecularevolutionand pages 12-14).

**Nutrient acquisition:** The conserved core effector MavN scavenges iron from the host cell, which is essential for bacterial growth within the LCV; iron limitation triggers growth arrest and host cell exit (lockwood2022thelegionellapneumophila pages 26-28). LppA degrades phytate to overcome nutritional restriction (lockwood2022thelegionellapneumophila pages 26-28). GO terms: iron ion transport (GO:0006826), siderophore-dependent iron import into cell (GO:0048238).

### Immune Response

**Inflammasome activation:** Bacterial flagellin is sensed by Naip5, which complexes with NLRC4 to activate the inflammasome in a Dot/Icm-dependent manner, triggering caspase-1 activation and pyroptotic cell death (shin2026molecularevolutionand pages 12-14). GO terms: inflammasome complex (GO:0061702), pyroptosis (GO:0070269).

**Differential cell-type responses:** Macrophages and dendritic cells (DCs) respond distinctly to *L. pneumophila*. In macrophages, the bacterium establishes robust intracellular replication, while DCs undergo rapid cell death through two mechanisms: early caspase-11 and NLRP3 inflammasome-dependent pyroptosis, and later effector-triggered apoptosis driven by T4SS effector-mediated blockade of host protein synthesis (depleting pro-survival proteins Mcl-1 and cFLIP) (shin2026molecularevolutionand pages 12-14).

**Epigenetic reprogramming:** *L. pneumophila* modulates macrophage functions through epigenetic reprogramming via the C-type lectin receptor Mincle, representing a novel mechanism of host cell manipulation.

**Tissue damage:** Replication of *L. pneumophila* within macrophages and monocytes triggers a hyperactive inflammatory response that damages lung tissue, resulting in the severe pneumonia characteristic of LD (cakmak2024presenceoflegionella pages 2-3). Host cell exit during late infection involves heterogeneous transition from replicative to transmissive forms, with the bacterium producing flagella and secreting phospholipases (PlaA, PlaB, PlaD, PlcC) to lyse the LCV and host cell (lockwood2022thelegionellapneumophila pages 26-28).

### Cell Types Involved

- Alveolar macrophages (CL:0000583) — primary target and replicative niche
- Dendritic cells (CL:0000451) — activate pyroptosis and restrict infection
- Neutrophils (CL:0000775) — essential for early innate immune control
- Monocytes (CL:0000576) — recruited during infection

---

## 7. Anatomical Structures Affected

### Organ Level

- **Primary:** Lungs (UBERON:0002048) — site of primary infection and pneumonia
- **Secondary:** Kidneys (UBERON:0002113) — AKI in up to 80% of ICU cases; liver (UBERON:0002107); spleen; gastrointestinal tract (UBERON:0005409); central nervous system (UBERON:0001017); heart (UBERON:0000948) — myocarditis/pericarditis (rello2024severelegionnaires’disease pages 4-5, rello2024severelegionnaires’disease pages 5-7)
- **Body systems:** Respiratory, renal, gastrointestinal, neurological, cardiovascular (rello2024severelegionnaires’disease pages 4-5)

### Tissue and Cell Level

- Pulmonary alveolar epithelium — site of initial aerosol deposition
- Alveolar macrophages (CL:0000583) — primary intracellular replicative niche
- Lung interstitium — inflammatory infiltrate and tissue damage

### Subcellular Level

- Legionella-containing vacuole (LCV) — ER-derived compartment (GO:0005783 — endoplasmic reticulum)
- Mitochondria (GO:0005739) — targeted by effectors for metabolic manipulation
- Endosomes/lysosomes (GO:0005764) — phagosome-lysosome fusion is inhibited

---

## 8. Temporal Development

### Onset

- **Incubation period:** 2–10 days after exposure for Legionnaires' disease; 5–72 hours for Pontiac fever (shin2026molecularevolutionand pages 2-3)
- **Onset pattern:** Acute; symptoms develop rapidly following incubation
- **Typical age of onset:** Adult and geriatric populations; highest burden in individuals >70 years (zhong2025theglobalburden pages 1-2, zhong2025theglobalburden pages 6-8)

### Progression

- LD can progress rapidly from initial pneumonia to respiratory failure, septic shock, and multi-organ dysfunction
- ICU admission occurs in approximately one-third of cases (rello2024severelegionnaires’disease pages 1-3)
- Disease duration is typically 2–6 weeks with appropriate treatment; prolonged in severe and immunocompromised cases (zhang2025lymphadenitiscausedby pages 4-6)
- Pontiac fever is self-limited, resolving within 5 days (shin2026molecularevolutionand pages 2-3)

---

## 9. Inheritance and Population

### Epidemiology

| Metric | Value | Source/Year |
|---|---|---|
| Global age-standardized DALY rate (ASR-DALYs) | 24.74 per 100,000 | GBD-based global analysis, 2021 (zhong2025theglobalburden pages 1-2, zhong2025theglobalburden pages 2-4) |
| Global age-standardized death rate (ASDR) | 0.86 per 100,000 | GBD-based global analysis, 2021 (zhong2025theglobalburden pages 1-2, zhong2025theglobalburden pages 2-4) |
| US annual cases | 52,000-70,000 estimated annually; 10,000 reported cases in 2018 | US epidemiology summaries/reviews (cakmak2024presenceoflegionella pages 2-3, cakmak2024presenceoflegionella pages 3-5) |
| EU/EEA notification rate | 2.2 per 100,000 in 2018-2019; up from 1.2-1.4 per 100,000 in 2012-2016 | EU/EEA surveillance analysis, 2023 (cakmak2024presenceoflegionella pages 3-5) |
| Overall mortality rate | 7-10% overall | Recent reviews, 2024 (cakmak2024presenceoflegionella pages 1-2, rello2024severelegionnaires’disease pages 1-3) |
| Mortality in severe/ICU cases | Up to 40% | Severe Legionnaires’ disease review, 2024 (rello2024severelegionnaires’disease pages 1-3) |
| Swiss incidence trend | Increased from 1.1 to 5.6 per 100,000 between 2000 and 2020 | Global burden study citing Swiss surveillance trend (zhong2025theglobalburden pages 6-8) |
| Age group with highest burden | >70 years; 101.85 ASR-DALYs per 100,000 | GBD-based global analysis, 2021 (zhong2025theglobalburden pages 1-2) |
| Sex ratio | Male predominance, approximately 2:1 to 3:1 | Epidemiologic reviews and surveillance summaries (rello2024severelegionnaires’disease pages 1-3, yao2024areviewof pages 1-2) |
| Case fatality in otherwise healthy individuals | ~10% | Review summary (shin2026molecularevolutionand pages 2-3) |
| Case fatality in high-risk patients | >25% | Review summary for elderly, smokers, immunocompromised, and comorbid patients (shin2026molecularevolutionand pages 2-3) |
| ICU admission rate | Approximately one-third of cases | Severe Legionnaires’ disease review, 2024 (rello2024severelegionnaires’disease pages 1-3) |
| Annual treatment costs in the US | >$340 million | US epidemiology/economic burden summary (cakmak2024presenceoflegionella pages 3-5) |


*Table: This table summarizes the most relevant recent epidemiology and global burden metrics for Legionnaires' disease, including incidence, mortality, healthcare burden, and age-stratified risk. It is useful as a compact reference for disease knowledge base population and comparative public health assessment.*

The global burden of Legionella-associated diseases has shifted significantly over the 1990–2021 period, with the overall age-standardized DALY and death rates declining (EAPC: −1.42% and −0.75%, respectively), but with concerning upward trends in specific age groups (15–49 years: EAPC 0.43% for DALYs; 50–69 years: EAPC 0.14%) (zhong2025theglobalburden pages 1-2, zhong2025theglobalburden pages 2-4). Sub-Saharan Africa carries the highest regional burden, while high-income regions have the lowest (zhong2025theglobalburden pages 2-4).

In the EU/EEA, LD notification rates increased from 1.2–1.4 per 100,000 population in 2012–2016 to 1.8–2.2 per 100,000 in 2017–2019, representing a 33.9% increase above predicted levels (cakmak2024presenceoflegionella pages 3-5). In the United States, the estimated 52,000–70,000 annual cases represent a more than five-fold increase since the early 2000s, with Legionella being the leading cause of waterborne disease outbreaks, responsible for 43% of outbreaks and 94% of hospitalizations (cakmak2024presenceoflegionella pages 3-5). The reported incidence increased 249% between 2000 and 2011 (shin2026molecularevolutionand pages 2-3).

### Population Demographics

- **Age distribution:** Highest burden in individuals >70 years (101.85 ASR-DALYs per 100,000 in 2021) (zhong2025theglobalburden pages 1-2)
- **Sex ratio:** Male predominance, approximately 2:1 to 3:1 (rello2024severelegionnaires’disease pages 1-3)
- **Racial and socioeconomic disparities:** In the US, poverty level was the strongest risk factor for legionellosis in multivariate models; racial and socioeconomic inequities are largely understudied but emerging as important drivers (cakmak2024presenceoflegionella pages 3-5)
- **Seasonal patterns:** Clear seasonality with trough in early spring and peak in autumn (peak-to-trough ratio = 3.62) (cakmak2024presenceoflegionella pages 3-5)

---

## 10. Diagnostics

### Clinical Tests

| Method | Sensitivity | Specificity | Time to Result | Detects | Advantages | Limitations |
|---|---:|---:|---|---|---|---|
| Urinary antigen test (UAT) | 70-90% | ~100% | 15-30 min | *L. pneumophila* serogroup 1 antigen in urine | Rapid, widely available, useful first-line test, supports early targeted therapy (rello2024severelegionnaires’disease pages 5-7) | Misses non-serogroup 1 *L. pneumophila* and other *Legionella* species; underestimates true epidemiology (rello2024severelegionnaires’disease pages 5-7, shin2026molecularevolutionand pages 2-3) |
| PCR / nucleic acid amplification test (respiratory specimen) | 96.8-97.7% | High | Hours to <24 h | All *Legionella* species/serogroups, depending on assay design | Higher sensitivity than UAT; detects non-Lp1 infections; rapid; useful on sputum/BAL (rello2024severelegionnaires’disease pages 5-7, NCT00452153 chunk 1) | Requires respiratory specimen and molecular lab capacity; assay standardization varies; some methods may detect nonviable organisms (rello2024severelegionnaires’disease pages 5-7, cakmak2024presenceoflegionella pages 5-6) |
| Culture (BCYE and related methods) | 50-80% | 100% | Days to weeks | All culturable *Legionella* species from respiratory/environmental samples | Gold standard; enables species/serogroup identification, typing, and outbreak source matching (zhang2025lymphadenitiscausedby pages 3-4, cakmak2024presenceoflegionella pages 5-6) | Slow; lower sensitivity than PCR; requires specialized media and expertise; affected by prior antibiotics (zhang2025lymphadenitiscausedby pages 3-4) |
| Serology | Variable | Variable | Weeks | Host antibody response to *Legionella* | May support retrospective diagnosis or epidemiologic studies (zhang2025lymphadenitiscausedby pages 3-4, NCT00452153 chunk 1) | Not useful for early acute management; delayed seroconversion; immunosuppressed patients may not mount detectable antibodies (zhang2025lymphadenitiscausedby pages 3-4) |
| Next-generation sequencing (NGS) / metagenomic sequencing | High analytical sensitivity; exact clinical sensitivity not yet standardized | High when sufficient sequence depth/interpretation is achieved | Typically 1-3 days, varies by platform | Broad pathogen detection, including fastidious/unexpected *Legionella* spp. | Unbiased detection; can identify multiple pathogens simultaneously; useful when routine tests are negative (zhang2025lymphadenitiscausedby pages 3-4, zhang2025lymphadenitiscausedby pages 4-6) | Expensive; limited availability; turnaround and bioinformatics burden; interpretation/contamination issues; not standard first-line testing (zhang2025lymphadenitiscausedby pages 4-6) |
| Legiolert / Most Probable Number (MPN) | Not directly comparable to clinical sensitivity | Not directly comparable | ~7 days (environmental monitoring) | Environmental *L. pneumophila* in water systems | Practical for water-system surveillance and risk management; useful for prevention programs (cakmak2024presenceoflegionella pages 5-6, cakmak2024presenceoflegionella pages 2-3) | Environmental, not patient diagnosis; does not establish clinical disease by itself (cakmak2024presenceoflegionella pages 5-6, cakmak2024presenceoflegionella pages 2-3) |


*Table: This table summarizes the major diagnostic methods for Legionnaires' disease, including performance characteristics, turnaround times, and practical strengths and limitations. It is useful for comparing rapid clinical tests with confirmatory and environmental methods.*

**Urinary antigen test (UAT)** is the most widely used first-line diagnostic, detecting *L. pneumophila* serogroup 1 antigen with 70–90% sensitivity and nearly 100% specificity, with results available in 15–30 minutes (rello2024severelegionnaires’disease pages 5-7). However, UAT misses non-serogroup 1 and non-*pneumophila* species, significantly underestimating true LD incidence (rello2024severelegionnaires’disease pages 5-7, shin2026molecularevolutionand pages 2-3).

**PCR** from respiratory specimens (BAL or sputum) offers superior sensitivity (96.8–97.7%) and can detect all *Legionella* species and serogroups (rello2024severelegionnaires’disease pages 5-7). Nucleic acid-based testing increases detection of non-*pneumophila* serogroup 1 species compared to non-NAT methods (rello2024severelegionnaires’disease pages 5-7).

**Culture** on buffered charcoal yeast extract (BCYE) agar remains the gold standard with 100% specificity but only 50–80% sensitivity, requiring days to weeks for results (zhang2025lymphadenitiscausedby pages 3-4, cakmak2024presenceoflegionella pages 5-6).

**Next-generation sequencing (NGS)** is emerging as a highly sensitive method capable of simultaneously identifying multiple pathogens with low pathogen load requirements (zhang2025lymphadenitiscausedby pages 3-4, zhang2025lymphadenitiscausedby pages 4-6).

### Imaging

Chest radiography and CT scanning show consolidations that are typically larger than expected, surrounded by ground-glass opacities, and can progress from patchy infiltrates to bilateral interstitial pneumonia (rello2024severelegionnaires’disease pages 4-5, rello2024severelegionnaires’disease pages 5-7).

### Laboratory Abnormalities

Common findings include hyponatremia, elevated creatine kinase, impaired renal function, hyperleukocytosis with lymphopenia, and elevated C-reactive protein (rello2024severelegionnaires’disease pages 4-5).

### Differential Diagnosis

Other causes of severe community-acquired pneumonia including *Streptococcus pneumoniae*, *Mycoplasma pneumoniae*, *Chlamydophila pneumoniae*, influenza virus, and other atypical pneumonia pathogens must be considered (rello2024severelegionnaires’disease pages 1-3).

---

## 11. Outcome/Prognosis

### Mortality

Overall mortality of LD ranges from 7–10%, though estimates vary from 4% to 40% depending on clinical setting (cakmak2024presenceoflegionella pages 1-2, rello2024severelegionnaires’disease pages 1-3). Fatality rate is approximately 10% in otherwise healthy individuals and exceeds 25% in high-risk patients including the elderly, smokers, and immunocompromised individuals (shin2026molecularevolutionand pages 2-3). Mortality in ICU patients, immunocompromised patients, or those with nosocomial infection can reach 40% despite appropriate antimicrobial therapy (rello2024severelegionnaires’disease pages 1-3).

### Complications

Major complications include acute respiratory distress syndrome, septic shock, and acute renal failure. Nearly 80% of ICU patients with *L. pneumophila* developed AKI in one 10-year cohort, with approximately half requiring renal replacement therapy (rello2024severelegionnaires’disease pages 5-7, rello2024severelegionnaires’disease pages 1-3). Rhabdomyolysis and extrapulmonary dissemination to the liver, spleen, gastrointestinal tract, nervous system, and cardiovascular system are well-documented complications (rello2024severelegionnaires’disease pages 4-5).

### Prognostic Factors

Factors influencing mortality include ICU admission requirement, underlying immune status, nosocomial versus community acquisition, timing of appropriate antimicrobial therapy, and the host immune response (hyperinflammation and/or immunoparalysis) (rello2024severelegionnaires’disease pages 1-3). Early antibiotic therapy within 24 hours of hospital admission with macrolides or levofloxacin is protective against clinical deterioration and ICU admission (rello2024severelegionnaires’disease pages 5-7).

---

## 12. Treatment

### Pharmacotherapy

**First-line agents:** Treatment is based on macrolides (azithromycin), fluoroquinolones (levofloxacin, moxifloxacin), or a combination of both, as recommended by IDSA guidelines (rello2024severelegionnaires’disease pages 5-7, rello2024severelegionnaires’disease pages 1-3). MAXO terms: MAXO:0000058 (antimicrobial treatment).

- **Azithromycin:** Commonly administered at 0.5 g daily, initially intravenous for 2 weeks followed by 2 weeks oral in severe cases (zhang2025lymphadenitiscausedby pages 3-4)
- **Fluoroquinolones:** Levofloxacin is widely used; fluoroquinolones target bacterial DNA topoisomerase II (TOP2A/TOP2B) (OpenTargets Search: Legionnaires disease,legionellosis)
- **β-lactam and aminoglycoside antibiotics are ineffective** against Legionella due to poor cell membrane penetration and inability to reach intracellular bacteria (zhang2025lymphadenitiscausedby pages 3-4, zhang2025lymphadenitiscausedby pages 4-6)

**Treatment duration:** 2 weeks for immunocompetent hosts; 3 weeks for immunosuppressed patients; prolonged treatment in severe cases (zhang2025lymphadenitiscausedby pages 4-6).

**Alternative agents:** Effective alternatives include doxycycline, tigecycline, cotrimoxazole, and rifampicin (zhang2025lymphadenitiscausedby pages 4-6). Omadacycline, a newer tetracycline antibiotic, has been highlighted as an effective option with good lung tissue penetration, particularly suitable for patients with quinolone intolerance or hepatic/renal impairment (cakmak2024presenceoflegionella pages 5-6).

### Supportive Care

Severe cases require respiratory support including mechanical ventilation, hemodynamic support with vasoactive agents, and renal replacement therapy for AKI (rello2024severelegionnaires’disease pages 5-7, rello2024severelegionnaires’disease pages 1-3). MAXO terms: MAXO:0000756 (mechanical ventilation), MAXO:0001174 (renal replacement therapy).

### Clinical Trials

Several clinical studies have addressed LD diagnostics and management:
- **NCT03064737:** Bacterial and human biomarkers of prognostic value for severe Legionnaire's disease (Hospices Civils de Lyon; 300 participants) (NCT00452153 chunk 1)
- **NCT00452153:** Evaluation of Legionella PCR techniques for routine diagnosis (Centre Hospitalier Universitaire de Saint Etienne; 200 participants) (NCT00452153 chunk 1)
- **NCT07352462:** Volatile organic compounds analysis for respiratory infection diagnosis (not yet recruiting; 777 participants)

---

## 13. Prevention

### Primary Prevention

**Water management programs** are the cornerstone of LD prevention. The WHO recommends implementing water safety plans based on HACCP (Hazard Analysis and Critical Control Points) principles to identify and manage risks in building water systems (yao2024areviewof pages 4-5). These plans should guide construction, design, routine monitoring, and management of water systems in hospitals, long-term care facilities, spas, and hotels (yao2024areviewof pages 4-5).

**Temperature control** is the most effective primary prevention measure:
- Hot water systems should maintain circulating water above 55°C (yao2024areviewof pages 3-4, yao2024areviewof pages 2-3, yao2024areviewof pages 11-11)
- Cold water should be kept below 25°C (yao2024areviewof pages 3-4)
- Thermal disinfection (raising water to 65°C) has successfully contained outbreaks (yao2024areviewof pages 4-5)
- *L. pneumophila* thrives at 25–45°C but is killed at temperatures >60°C (cakmak2024presenceoflegionella pages 3-5)

**Water disinfection:** Maintenance of free chlorine levels (0.2–4.0 mg/L) throughout distribution systems is required under the US Safe Drinking Water Act (cakmak2024presenceoflegionella pages 2-3). Regular cleaning and disinfection of cooling towers, fountains, and other water features are essential (yao2024areviewof pages 2-3).

**Regulatory frameworks:** Multiple countries have implemented standards for Legionella monitoring and control. Australia's AS/NZS 3666:2011 specifies minimum requirements for air and water supply system management. China implemented comprehensive standards in 2023–2024 addressing monitoring and hygienic management of central air conditioning systems (yao2024areviewof pages 7-8). MAXO terms: MAXO:0000486 (environmental intervention).

### Secondary Prevention

**Environmental monitoring:** Routine water sampling from water tanks, air conditioning systems, shower heads, faucets, and thermal pools enables early detection of contamination sources (cakmak2024presenceoflegionella pages 2-3). Monitoring for *L. pneumophila* specifically (rather than all Legionella species) has been recommended for public water systems, as it is the overwhelming cause of illness and has simple analytical methods (lechevallier2025thecasefor pages 2-5).

**Surveillance systems:** Established surveillance networks enable detection of epidemiological trends and timely intervention, including the European Surveillance System (TESSy) and European Working Group for Legionella Infections (EWGLI) guidelines for travel-associated LD (yao2024areviewof pages 11-11).

### Immunization

No vaccine is currently available for Legionnaires' disease. Vaccine development remains an area of ongoing research.

---

## 14. Other Species / Natural Disease

### Taxonomy and Environmental Hosts

*L. pneumophila* (NCBI Taxonomy ID: 446) naturally parasitizes free-living amoebae in aquatic environments, including *Acanthamoeba castellanii* and *Dictyostelium discoideum* (torresescobar2024anutritionalimmunity pages 30-32, schmidt2024theuniquelegionella pages 21-23). The bacterium has co-evolved with these protozoan hosts over evolutionary timescales, developing mechanisms for intracellular survival that proved transferable to human alveolar macrophages (shin2026molecularevolutionand pages 1-2).

### Zoonotic and Cross-Species Considerations

LD is not a zoonotic disease in the traditional sense — humans are considered accidental hosts who become infected through exposure to environmental *Legionella* rather than through animal-to-human transmission (yao2024areviewof pages 1-2). Guinea pigs are naturally susceptible to *L. pneumophila* infection and develop pneumonia similar to human disease, while most wild-type mouse strains are naturally resistant (shin2026molecularevolutionand pages 2-3, rello2024severelegionnaires’disease pages 3-4).

---

## 15. Model Organisms

### Animal Models

**Mouse models:** Murine models are the most commonly used for studying anti-Legionella immune responses, but wild-type mice are naturally non-permissive to infection due to NAIP5-mediated inflammasome activation (rello2024severelegionnaires’disease pages 3-4). A/J mice, which are deficient in NAIP5, permit intracellular bacterial replication and are used as a permissive model. C57BL/6 mice are used for survival and CFU experiments via intranasal or intratracheal inoculation (schmidt2024theuniquelegionella pages 21-23, rello2024severelegionnaires’disease pages 3-4).

**Guinea pig models:** Guinea pigs are naturally susceptible and develop pneumonia resembling human LD, making them valuable for studying early inflammatory events during experimental pneumonia (torresescobar2024anutritionalimmunity pages 30-32, shin2026molecularevolutionand pages 2-3).

### Protozoan Models

**Acanthamoeba castellanii:** Used extensively to study intracellular replication, virulence factor function, and host-pathogen dynamics. Represents the natural environmental host (torresescobar2024anutritionalimmunity pages 30-32, schmidt2024theuniquelegionella pages 21-23).

**Dictyostelium discoideum:** Employed as a genetically tractable model for studying host-pathogen interactions and genetic analysis of bacterial virulence determinants (torresescobar2024anutritionalimmunity pages 30-32).

### Cell Line and Primary Cell Models

- **THP-1 cells:** Human monocytic cell line differentiated into macrophage-like cells for infection studies (schmidt2024theuniquelegionella pages 17-18, schmidt2024theuniquelegionella pages 21-23)
- **Bone marrow-derived macrophages (BMDMs)** and **dendritic cells (BMDCs):** From C57BL/6 or A/J mice for studying innate immune responses
- **Human monocyte-derived macrophages (hMDMs):** Primary human cells for translational studies (schmidt2024theuniquelegionella pages 17-18)
- **U2OS cells:** Human osteosarcoma epithelial cells for studying intracellular bacterial effector functions (schmidt2024theuniquelegionella pages 21-23)

### Model Limitations

A key limitation of mouse models is that wild-type strains resist *L. pneumophila* infection, requiring the use of NAIP5-deficient strains that do not fully recapitulate the human immune response. Guinea pig models more closely recapitulate human disease but are less amenable to genetic manipulation (shin2026molecularevolutionand pages 2-3, rello2024severelegionnaires’disease pages 3-4). Transposon sequencing approaches in animal models are complicated by the suboptimal nature of available *L. pneumophila* infection models for conventional saturated mutant library screens.

---

## Summary

Legionnaires' disease is a severe, increasingly prevalent waterborne pneumonia caused by the facultative intracellular pathogen *Legionella pneumophila*. The disease burden is rising globally, driven by aging populations, increasing immunosuppression, climate change, aging water infrastructure, and improved diagnostic detection (rello2024severelegionnaires’disease pages 1-3, cakmak2024presenceoflegionella pages 3-5, zhong2025theglobalburden pages 1-2). The pathophysiology centers on the extraordinary Dot/Icm Type IV Secretion System, which delivers over 300 effector proteins to manipulate host cell processes including vesicle trafficking, autophagy, translation, and metabolism (shin2026molecularevolutionand pages 15-16, shin2026molecularevolutionand pages 1-2, lockwood2022thelegionellapneumophila pages 1-3). While diagnostic capabilities have improved with UAT and PCR-based methods, the true epidemiological burden remains underestimated due to diagnostic limitations and under-testing (rello2024severelegionnaires’disease pages 5-7, shin2026molecularevolutionand pages 2-3). Treatment relies on macrolides and fluoroquinolones, and prevention strategies focus on comprehensive water management programs with temperature control and disinfection (rello2024severelegionnaires’disease pages 5-7, yao2024areviewof pages 3-4, yao2024areviewof pages 4-5). Future priorities include development of broader diagnostic tests, identification of severity biomarkers, evaluation of host-directed therapies, and enhanced public health surveillance to address the rising global burden of this important infectious disease (rello2024severelegionnaires’disease pages 1-3).

References

1. (shin2026molecularevolutionand pages 2-3): Cheon Jee Shin and Yousef Abu Kwaik. Molecular evolution and adaptations of legionella pneumophila from amoebae hosts to macrophages. Frontiers in Cellular and Infection Microbiology, Feb 2026. URL: https://doi.org/10.3389/fcimb.2026.1787137, doi:10.3389/fcimb.2026.1787137. This article has 0 citations.

2. (cakmak2024presenceoflegionella pages 1-2): Ömer Çakmak, Tuba Aldemir, Erdi Ergene, Ulaş Acaröz, Damla Arslan-acaroz, and Nuri Taş. Presence of legionella pneumophila in tap water and its importance for public health. Veteriner Farmakoloji ve Toksikoloji Derneği Bülteni, 15:64-76, Aug 2024. URL: https://doi.org/10.38137/vftd.1432171, doi:10.38137/vftd.1432171. This article has 1 citations.

3. (shin2026molecularevolutionand pages 1-2): Cheon Jee Shin and Yousef Abu Kwaik. Molecular evolution and adaptations of legionella pneumophila from amoebae hosts to macrophages. Frontiers in Cellular and Infection Microbiology, Feb 2026. URL: https://doi.org/10.3389/fcimb.2026.1787137, doi:10.3389/fcimb.2026.1787137. This article has 0 citations.

4. (yao2024areviewof pages 1-2): Xiao Hui Yao, Fan Shen, Jing Hao, Lu Huang, and Bin Keng. A review of legionella transmission risk in built environments: sources, regulations, sampling, and detection. Frontiers in Public Health, Jul 2024. URL: https://doi.org/10.3389/fpubh.2024.1415157, doi:10.3389/fpubh.2024.1415157. This article has 31 citations.

5. (rello2024severelegionnaires’disease pages 1-3): Jordi Rello, Camille Allam, Alfonsina Ruiz-Spinelli, and Sophie Jarraud. Severe legionnaires’ disease. Annals of Intensive Care, Apr 2024. URL: https://doi.org/10.1186/s13613-024-01252-y, doi:10.1186/s13613-024-01252-y. This article has 85 citations and is from a peer-reviewed journal.

6. (lechevallier2025thecasefor pages 2-5): Mark W. LeChevallier. The case for monitoring for legionella pneumophila in drinking water distribution systems. Water, 17:475, Feb 2025. URL: https://doi.org/10.3390/w17040475, doi:10.3390/w17040475. This article has 8 citations.

7. (OpenTargets Search: Legionnaires disease,legionellosis): Open Targets Query (Legionnaires disease,legionellosis, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

8. (rello2024severelegionnaires’disease pages 5-7): Jordi Rello, Camille Allam, Alfonsina Ruiz-Spinelli, and Sophie Jarraud. Severe legionnaires’ disease. Annals of Intensive Care, Apr 2024. URL: https://doi.org/10.1186/s13613-024-01252-y, doi:10.1186/s13613-024-01252-y. This article has 85 citations and is from a peer-reviewed journal.

9. (yao2024areviewof pages 2-3): Xiao Hui Yao, Fan Shen, Jing Hao, Lu Huang, and Bin Keng. A review of legionella transmission risk in built environments: sources, regulations, sampling, and detection. Frontiers in Public Health, Jul 2024. URL: https://doi.org/10.3389/fpubh.2024.1415157, doi:10.3389/fpubh.2024.1415157. This article has 31 citations.

10. (cakmak2024presenceoflegionella pages 2-3): Ömer Çakmak, Tuba Aldemir, Erdi Ergene, Ulaş Acaröz, Damla Arslan-acaroz, and Nuri Taş. Presence of legionella pneumophila in tap water and its importance for public health. Veteriner Farmakoloji ve Toksikoloji Derneği Bülteni, 15:64-76, Aug 2024. URL: https://doi.org/10.38137/vftd.1432171, doi:10.38137/vftd.1432171. This article has 1 citations.

11. (shin2026molecularevolutionand pages 15-16): Cheon Jee Shin and Yousef Abu Kwaik. Molecular evolution and adaptations of legionella pneumophila from amoebae hosts to macrophages. Frontiers in Cellular and Infection Microbiology, Feb 2026. URL: https://doi.org/10.3389/fcimb.2026.1787137, doi:10.3389/fcimb.2026.1787137. This article has 0 citations.

12. (lockwood2022thelegionellapneumophila pages 1-3): Daniel C. Lockwood, Himani Amin, Tiago R. D. Costa, and Gunnar N. Schroeder. The legionella pneumophila dot/icm type iv secretion system and its effectors. May 2022. URL: https://doi.org/10.1099/mic.0.001187, doi:10.1099/mic.0.001187. This article has 64 citations and is from a peer-reviewed journal.

13. (cakmak2024presenceoflegionella pages 3-5): Ömer Çakmak, Tuba Aldemir, Erdi Ergene, Ulaş Acaröz, Damla Arslan-acaroz, and Nuri Taş. Presence of legionella pneumophila in tap water and its importance for public health. Veteriner Farmakoloji ve Toksikoloji Derneği Bülteni, 15:64-76, Aug 2024. URL: https://doi.org/10.38137/vftd.1432171, doi:10.38137/vftd.1432171. This article has 1 citations.

14. (yao2024areviewof pages 3-4): Xiao Hui Yao, Fan Shen, Jing Hao, Lu Huang, and Bin Keng. A review of legionella transmission risk in built environments: sources, regulations, sampling, and detection. Frontiers in Public Health, Jul 2024. URL: https://doi.org/10.3389/fpubh.2024.1415157, doi:10.3389/fpubh.2024.1415157. This article has 31 citations.

15. (rello2024severelegionnaires’disease pages 4-5): Jordi Rello, Camille Allam, Alfonsina Ruiz-Spinelli, and Sophie Jarraud. Severe legionnaires’ disease. Annals of Intensive Care, Apr 2024. URL: https://doi.org/10.1186/s13613-024-01252-y, doi:10.1186/s13613-024-01252-y. This article has 85 citations and is from a peer-reviewed journal.

16. (zhang2025lymphadenitiscausedby pages 3-4): Cangjian Zhang and Minlei Zhao. Lymphadenitis caused by legionella sainthelensi infection: a case report and literature review. Frontiers in Medicine, May 2025. URL: https://doi.org/10.3389/fmed.2025.1574205, doi:10.3389/fmed.2025.1574205. This article has 2 citations.

17. (rello2024severelegionnaires’disease pages 3-4): Jordi Rello, Camille Allam, Alfonsina Ruiz-Spinelli, and Sophie Jarraud. Severe legionnaires’ disease. Annals of Intensive Care, Apr 2024. URL: https://doi.org/10.1186/s13613-024-01252-y, doi:10.1186/s13613-024-01252-y. This article has 85 citations and is from a peer-reviewed journal.

18. (shin2026molecularevolutionand pages 22-22): Cheon Jee Shin and Yousef Abu Kwaik. Molecular evolution and adaptations of legionella pneumophila from amoebae hosts to macrophages. Frontiers in Cellular and Infection Microbiology, Feb 2026. URL: https://doi.org/10.3389/fcimb.2026.1787137, doi:10.3389/fcimb.2026.1787137. This article has 0 citations.

19. (shin2026molecularevolutionand pages 18-19): Cheon Jee Shin and Yousef Abu Kwaik. Molecular evolution and adaptations of legionella pneumophila from amoebae hosts to macrophages. Frontiers in Cellular and Infection Microbiology, Feb 2026. URL: https://doi.org/10.3389/fcimb.2026.1787137, doi:10.3389/fcimb.2026.1787137. This article has 0 citations.

20. (shin2026molecularevolutionand pages 14-15): Cheon Jee Shin and Yousef Abu Kwaik. Molecular evolution and adaptations of legionella pneumophila from amoebae hosts to macrophages. Frontiers in Cellular and Infection Microbiology, Feb 2026. URL: https://doi.org/10.3389/fcimb.2026.1787137, doi:10.3389/fcimb.2026.1787137. This article has 0 citations.

21. (shin2026molecularevolutionand pages 12-14): Cheon Jee Shin and Yousef Abu Kwaik. Molecular evolution and adaptations of legionella pneumophila from amoebae hosts to macrophages. Frontiers in Cellular and Infection Microbiology, Feb 2026. URL: https://doi.org/10.3389/fcimb.2026.1787137, doi:10.3389/fcimb.2026.1787137. This article has 0 citations.

22. (lockwood2022thelegionellapneumophila pages 26-28): Daniel C. Lockwood, Himani Amin, Tiago R. D. Costa, and Gunnar N. Schroeder. The legionella pneumophila dot/icm type iv secretion system and its effectors. May 2022. URL: https://doi.org/10.1099/mic.0.001187, doi:10.1099/mic.0.001187. This article has 64 citations and is from a peer-reviewed journal.

23. (zhong2025theglobalburden pages 1-2): Yonghong Zhong, Linfeng Shen, Yan Zhou, Yibo Sun, Xiaofang Fu, and Huaqiong Huang. The global burden and trends of legionella spp. infection-associated diseases from 1990 to 2021: an observational study. Journal of Epidemiology and Global Health, Jan 2025. URL: https://doi.org/10.1007/s44197-025-00342-9, doi:10.1007/s44197-025-00342-9. This article has 13 citations and is from a peer-reviewed journal.

24. (zhong2025theglobalburden pages 6-8): Yonghong Zhong, Linfeng Shen, Yan Zhou, Yibo Sun, Xiaofang Fu, and Huaqiong Huang. The global burden and trends of legionella spp. infection-associated diseases from 1990 to 2021: an observational study. Journal of Epidemiology and Global Health, Jan 2025. URL: https://doi.org/10.1007/s44197-025-00342-9, doi:10.1007/s44197-025-00342-9. This article has 13 citations and is from a peer-reviewed journal.

25. (zhang2025lymphadenitiscausedby pages 4-6): Cangjian Zhang and Minlei Zhao. Lymphadenitis caused by legionella sainthelensi infection: a case report and literature review. Frontiers in Medicine, May 2025. URL: https://doi.org/10.3389/fmed.2025.1574205, doi:10.3389/fmed.2025.1574205. This article has 2 citations.

26. (zhong2025theglobalburden pages 2-4): Yonghong Zhong, Linfeng Shen, Yan Zhou, Yibo Sun, Xiaofang Fu, and Huaqiong Huang. The global burden and trends of legionella spp. infection-associated diseases from 1990 to 2021: an observational study. Journal of Epidemiology and Global Health, Jan 2025. URL: https://doi.org/10.1007/s44197-025-00342-9, doi:10.1007/s44197-025-00342-9. This article has 13 citations and is from a peer-reviewed journal.

27. (NCT00452153 chunk 1):  Evaluation of Legionella PCR Techniques for the Routine Diagnosis of Legionellosis. Centre Hospitalier Universitaire de Saint Etienne. 2007. ClinicalTrials.gov Identifier: NCT00452153

28. (cakmak2024presenceoflegionella pages 5-6): Ömer Çakmak, Tuba Aldemir, Erdi Ergene, Ulaş Acaröz, Damla Arslan-acaroz, and Nuri Taş. Presence of legionella pneumophila in tap water and its importance for public health. Veteriner Farmakoloji ve Toksikoloji Derneği Bülteni, 15:64-76, Aug 2024. URL: https://doi.org/10.38137/vftd.1432171, doi:10.38137/vftd.1432171. This article has 1 citations.

29. (yao2024areviewof pages 4-5): Xiao Hui Yao, Fan Shen, Jing Hao, Lu Huang, and Bin Keng. A review of legionella transmission risk in built environments: sources, regulations, sampling, and detection. Frontiers in Public Health, Jul 2024. URL: https://doi.org/10.3389/fpubh.2024.1415157, doi:10.3389/fpubh.2024.1415157. This article has 31 citations.

30. (yao2024areviewof pages 11-11): Xiao Hui Yao, Fan Shen, Jing Hao, Lu Huang, and Bin Keng. A review of legionella transmission risk in built environments: sources, regulations, sampling, and detection. Frontiers in Public Health, Jul 2024. URL: https://doi.org/10.3389/fpubh.2024.1415157, doi:10.3389/fpubh.2024.1415157. This article has 31 citations.

31. (yao2024areviewof pages 7-8): Xiao Hui Yao, Fan Shen, Jing Hao, Lu Huang, and Bin Keng. A review of legionella transmission risk in built environments: sources, regulations, sampling, and detection. Frontiers in Public Health, Jul 2024. URL: https://doi.org/10.3389/fpubh.2024.1415157, doi:10.3389/fpubh.2024.1415157. This article has 31 citations.

32. (torresescobar2024anutritionalimmunity pages 30-32): Ascención Torres-Escobar, Ashley Wilkins, María D Juárez-Rodríguez, Magdalena Circu, Brian Latimer, Ana-Maria Dragoi, and Stanimir S. Ivanov. A nutritional immunity blockade controls extracellular bacterial replication in legionella pneumophila infections. bioRxiv, Jan 2024. URL: https://doi.org/10.1101/2024.01.21.576562, doi:10.1101/2024.01.21.576562. This article has 1 citations.

33. (schmidt2024theuniquelegionella pages 21-23): Silke Schmidt, Sonia Mondino, Laura Gomez-Valero, Pedro Escoll, Danielle P. A. Mascarenhas, Augusto Gonçalves, Pedro H. M. Camara, Francisco J. Garcia Rodriguez, Christophe Rusniok, Martin Sachse, Maryse Moya-Nilges, Thierry Fontaine, Dario S. Zamboni, and Carmen Buchrieser. The unique legionella longbeachae capsule favors intracellular replication and immune evasion. Sep 2024. URL: https://doi.org/10.1371/journal.ppat.1012534, doi:10.1371/journal.ppat.1012534. This article has 6 citations and is from a highest quality peer-reviewed journal.

34. (schmidt2024theuniquelegionella pages 17-18): Silke Schmidt, Sonia Mondino, Laura Gomez-Valero, Pedro Escoll, Danielle P. A. Mascarenhas, Augusto Gonçalves, Pedro H. M. Camara, Francisco J. Garcia Rodriguez, Christophe Rusniok, Martin Sachse, Maryse Moya-Nilges, Thierry Fontaine, Dario S. Zamboni, and Carmen Buchrieser. The unique legionella longbeachae capsule favors intracellular replication and immune evasion. Sep 2024. URL: https://doi.org/10.1371/journal.ppat.1012534, doi:10.1371/journal.ppat.1012534. This article has 6 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Legionnaires_Disease-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Legionnaires_Disease-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](Legionnaires_Disease-deep-research-falcon_artifacts/artifact-02.md)
- [Edison artifact artifact-03](Legionnaires_Disease-deep-research-falcon_artifacts/artifact-03.md)