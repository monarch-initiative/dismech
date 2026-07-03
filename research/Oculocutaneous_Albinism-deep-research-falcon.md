---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T21:31:11.151544'
end_time: '2026-06-17T21:55:20.203905'
duration_seconds: 1449.05
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Oculocutaneous Albinism
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 34
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 2
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: Oculocutaneous_Albinism-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Oculocutaneous_Albinism-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: image-1.png
  path: Oculocutaneous_Albinism-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: '## Context ID: pqac-00000020 I have extracted the table titled ''Albinism
    Prevalence Data Categorized by Continent'' from page 4 of the document. This table
    provi'
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Oculocutaneous Albinism
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Oculocutaneous Albinism** covering all of the
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
- **Disease Name:** Oculocutaneous Albinism
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Oculocutaneous Albinism** covering all of the
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


## Disease Characteristics Research Report: Oculocutaneous Albinism (OCA)

### Target Disease
- **Disease name:** Oculocutaneous albinism (OCA)
- **MONDO ID:** Not found in the tool-retrieved sources in this run (gap noted).
- **Category:** Rare genetic disorder of pigmentation / inherited eye disease (syndromic and non-syndromic forms).

---

## 1. Disease Information

### Overview / definition
Oculocutaneous albinism (OCA) comprises inherited disorders characterized by reduced or absent melanin biosynthesis affecting **eyes, skin, and hair**, with characteristic ocular manifestations (e.g., reduced visual acuity, foveal hypoplasia, nystagmus, iris transillumination) and increased UV-related skin disease risk. (ambrosio2025advancinginsightsinto pages 11-13, thomas2023oculocutaneousalbinismanda pages 1-3, kromberg2023determiningaworldwide pages 1-2)

### Key identifiers (available from retrieved evidence)
- **MeSH:** *Albinism, Oculocutaneous* **D016115** (ClinicalTrials.gov browse terms). (NCT07313618 chunk 2)
- **MeSH (broader):** *Albinism* **D000417**. (NCT01176435 chunk 1)
- **ICD-10:** **E70.3** (*Albinism*) explicitly referenced in a genomic medicine cohort paper using ICD-10 coding. (fassad2026wholegenomesequencinguncovers pages 5-8)
- **OMIM (gene/subtype IDs in GeneReviews excerpt):** OCA1/TYR **606933**, OCA2 **611409**, OCA3/TYRP1 **115501**, OCA6/SLC24A5 **609802**, OCA7/LRMDA **614537**, OCA8/DCT **191275**, and ocular albinism OA1/GPR143 **300808**. (thomas2023oculocutaneousalbinismand pages 7-8)

**Not captured in retrieved texts during this run:** Orphanet/ORDO ORPHA codes, ICD-11 codes, and MONDO identifiers for OCA. (NCT07313618 chunk 2, NCT00001153 chunk 1, NCT04068961 chunk 1)

### Synonyms / alternative names (as used in evidence)
- “Oculocutaneous albinism type 1 (OCA1)” (TYR-related). (NCT07313618 chunk 1)
- “Oculocutaneous albinism type 1B (OCA1B)” (residual tyrosinase activity phenotype; nitisinone trial enrollment definition). (NCT01838655 chunk 1, NCT01838655 chunk 7)
- “Ocular albinism (OA)” (often GPR143-related; X-linked). (chan2023diagnosticyieldof pages 1-2, thomas2023oculocutaneousalbinismand pages 16-18)

### Evidence source type
The information summarized here is derived from **aggregated disease-level resources** (GeneReviews overview; systematic review) and **cohort studies/trials** rather than EHR-only sources. (kromberg2023determiningaworldwide pages 1-2, thomas2023oculocutaneousalbinismand pages 13-16, chan2023diagnosticyieldof pages 2-4)

---

## 2. Etiology

### Disease causal factors
**Primary cause:** germline genetic variants disrupting melanogenesis and/or melanosome function. Canonical OCA results from impaired melanin biosynthesis (e.g., TYR) or altered melanosomal homeostasis/biogenesis (e.g., OCA2, SLC45A2). (ambrosio2025advancinginsightsinto pages 11-13, thomas2023oculocutaneousalbinismand pages 13-16)

### Genetic risk factors (causal genes)
GeneReviews lists nonsyndromic OCA genes: **TYR, OCA2, TYRP1, SLC45A2, SLC24A5, LRMDA (C10orf11), DCT**, inherited **autosomal recessive**; ocular albinism due to **GPR143** is **X-linked**. (thomas2023oculocutaneousalbinismand pages 13-16, thomas2023oculocutaneousalbinismand pages 16-18)

### Recent (2024) developments: oligogenic/common-variant contributions
A 2024 Nature Communications study reported that **dual heterozygosity** for **TYR:c.1205G>A (p.Arg402Gln; rs1126809)** and **OCA2:c.1327G>A (p.Val443Ile; rs74653330)** is associated with increased probability of an albinism diagnosis (**OR 12.8; 95% CI 6.0–24.7; p=2.1×10−8**), and is associated with altered visual acuity and central retinal thickness (endophenotypes). (green2024thecooccurrenceof pages 1-2, green2024thecooccurrenceof pages 2-3)

### Environmental risk factors
OCA itself is genetic, but **UV exposure** is a major determinant of cutaneous morbidity (sun damage, precancer/cancer), motivating strict photoprotection and surveillance. (thomas2023oculocutaneousalbinismand pages 13-16)

### Protective factors / gene-environment interactions
No specific protective genetic variants were identified in the retrieved sources in this run. Clinically, **sun avoidance and photoprotection** reduce downstream UV-related skin disease risk (gene–environment: congenital hypopigmentation increases UV sensitivity; UV behavior modifies outcomes). (thomas2023oculocutaneousalbinismand pages 13-16)

---

## 3. Phenotypes

### Core ocular phenotypes (with frequencies where available)
A U.S. pediatric cohort (genetically tested OA/OCA; n=53 tested) reported the following phenotype frequencies:
- **Nystagmus:** 89% (chan2023diagnosticyieldof pages 2-4)
- **Foveal hypoplasia:** 85% (chan2023diagnosticyieldof pages 2-4)
- **Fundus hypopigmentation:** 68% (chan2023diagnosticyieldof pages 2-4)
- **Iris transillumination defects:** 38% (chan2023diagnosticyieldof pages 2-4)

GeneReviews summary series report very high frequency of key ocular signs (useful for diagnosis): iris transillumination defects ~91–100%, fundus hypopigmentation >94%, foveal hypoplasia 94–100%, and chiasmal misrouting 84–100%. (thomas2023oculocutaneousalbinismanda pages 1-3)

Additional quantitative clinical descriptors from GeneReviews include strabismus affecting ~71% overall (up to 100% in OCA1), and visual acuity spanning roughly 20/15 to 20/800 with median ~20/80 (logMAR ~0.60). (thomas2023oculocutaneousalbinismand pages 3-7)

### Neurodevelopmental and behavioral phenotype (2023 pediatric cohort)
A 2023 European Journal of Pediatrics cohort (18 children, molecularly confirmed OCA) found:
- **Global neurodevelopmental impairment in 56%**, not evolving into intellectual disability. (galli2023oculocutaneousalbinismthe pages 1-2)
- Behavioral screening risks: internalizing problems 33%, externalizing 11%, both 28%; **autistic-like features in 67%** (none meeting autism criteria in that report). (galli2023oculocutaneousalbinismthe pages 1-2, galli2023oculocutaneousalbinismthe pages 5-6)
- Visual acuity correlated with performance IQ and adaptive functioning measures. (galli2023oculocutaneousalbinismthe pages 1-2)

### Skin/dermatologic phenotype
OCA is associated with increased risk of UV-related skin disease and skin cancers; melanoma detection can be challenging because melanomas may be amelanotic in albinism, motivating regular dermatologic surveillance. (thomas2023oculocutaneousalbinismand pages 13-16)

### Suggested HPO terms (examples)
See ontology mapping artifact below (includes HP terms for foveal hypoplasia, nystagmus, strabismus, photophobia, reduced visual acuity, etc.).

---

## 4. Genetic / Molecular Information

### Causal genes and inheritance
- **Autosomal recessive nonsyndromic OCA:** TYR, OCA2, TYRP1, SLC45A2, SLC24A5, LRMDA, DCT. (thomas2023oculocutaneousalbinismand pages 13-16)
- **X-linked ocular albinism:** GPR143. (thomas2023oculocutaneousalbinismand pages 16-18)

The GeneReviews excerpt provides OMIM subtype identifiers for multiple OCA loci (useful for knowledge base cross-references). (thomas2023oculocutaneousalbinismand pages 7-8)

### Pathogenic/likely pathogenic variants and variant architecture (recent genetics)
A 2024 study supports an **oligogenic susceptibility** model for at least a subset of individuals: the TYR p.Arg402Gln and OCA2 p.Val443Ile combination increases diagnosis probability (OR 12.8). (green2024thecooccurrenceof pages 2-3)

### Functional consequences and molecular profiling (iPSC model; 2024)
A 2024 iPSC-derived retinal pigment epithelium (RPE) model of OCA1A supports a mechanism in which **mutant tyrosinase is absent or inactive** and **mature pigmented melanosomes are lacking**:
- TYR mutant misfolding/ER retention and loss of enzymatic activity are discussed as upstream events. (subramani2024generationandcharacterization pages 1-2)
- OCA1A RPE showed no pigmented stage III/IV melanosomes, markedly reduced melanin, and absent TYR protein/activity on Western blot and enzyme assays. (subramani2024generationandcharacterization pages 8-11)

### Suggested GO / CL terms
See ontology mapping artifact below for suggested GO processes/components (melanin biosynthesis, melanosome organization; ER protein folding) and cell types (melanocyte; retinal pigment epithelial cell; retinal ganglion cell). (subramani2024generationandcharacterization pages 8-11, thomas2023oculocutaneousalbinismanda pages 1-3)

---

## 5. Environmental Information

OCA is not environmentally caused; environmental exposures mainly modify downstream morbidity. The primary modifiable environmental factor is **UV exposure**, which drives sun damage and skin cancer risk in the context of hypopigmented skin. (thomas2023oculocutaneousalbinismand pages 13-16)

---

## 6. Mechanism / Pathophysiology

### Core causal chain (gene → cell biology → clinical manifestations)
1. **Upstream genetic defect** in melanogenesis genes (e.g., TYR, OCA2) reduces melanin biosynthesis or disrupts melanosome function. (ambrosio2025advancinginsightsinto pages 11-13, thomas2023oculocutaneousalbinismand pages 13-16)
2. **Cellular/subcellular dysfunction**: In TYR-related OCA1A, tyrosinase can be misfolded/retained and enzymatically inactive, yielding absent melanin and abnormal melanosome maturation; iPSC-RPE evidence supports absence of mature pigmented melanosomes and absent TYR activity/protein. (subramani2024generationandcharacterization pages 1-2, subramani2024generationandcharacterization pages 8-11)
3. **Tissue-level ocular developmental effects**: impaired retinal pigmentation associates with **foveal hypoplasia** and **abnormal optic pathway development/misrouting**, which contributes to nystagmus, reduced acuity, and strabismus. (ambrosio2025advancinginsightsinto pages 11-13, thomas2023oculocutaneousalbinismanda pages 1-3)

### Pathway-level notes
- TYR is described as initiating melanogenesis by converting L-tyrosine to L-DOPA and downstream intermediates. (ambrosio2025advancinginsightsinto pages 11-13)
- OCA2 can modulate **melanosome pH**, impacting tyrosinase activity (a mechanistic basis for modifier/interaction effects, consistent with oligogenic susceptibility findings). (green2024thecooccurrenceof pages 2-3)

### Suggested GO terms / CL terms
Included in artifact-01. (subramani2024generationandcharacterization pages 8-11, thomas2023oculocutaneousalbinismanda pages 1-3)

---

## 7. Anatomical Structures Affected

### Organ/system level
- **Eye/visual system** (retina/fovea; optic chiasm/visual pathways): major morbidity and disability driver. (ambrosio2025advancinginsightsinto pages 11-13, thomas2023oculocutaneousalbinismanda pages 1-3)
- **Skin**: hypopigmentation and UV susceptibility, including skin cancer surveillance burden. (thomas2023oculocutaneousalbinismand pages 13-16)

### Tissue/cell level
- **Retinal pigment epithelium (RPE)** is a key ocular pigment cell population; patient iPSC-derived RPE demonstrates disease-recapitulating pigmentation defects in TYR-related OCA1A. (subramani2024generationandcharacterization pages 1-2, subramani2024generationandcharacterization pages 8-11)

### Suggested UBERON terms
Included in artifact-01. (thomas2023oculocutaneousalbinismanda pages 1-3, thomas2023oculocutaneousalbinismand pages 13-16)

---

## 8. Temporal Development

OCA is typically **congenital/early onset**, with visual impairment present from infancy/childhood. Neurodevelopmental delays in the 2023 pediatric cohort appeared early (56% global impairment) and were reported not to progress to intellectual disability. (galli2023oculocutaneousalbinismthe pages 1-2)

---

## 9. Inheritance and Population

### Inheritance
- Nonsyndromic OCA (TYR, OCA2, TYRP1, SLC45A2, SLC24A5, LRMDA, DCT): **autosomal recessive**. (thomas2023oculocutaneousalbinismand pages 13-16)
- Ocular albinism (GPR143): **X-linked**. (thomas2023oculocutaneousalbinismand pages 16-18)

### Epidemiology (systematic review; 2023)
A 2023 systematic review found that OCA prevalence estimates are geographically uneven and often outdated:
- Only **26/193 countries (13%)** had published OCA prevalence figures; studies were disproportionately from Africa. (kromberg2023determiningaworldwide pages 1-2)
- Highest prevalence in population isolates ranged **1 in 22 to 1 in 1300** (mean **1 in 464**). (kromberg2023determiningaworldwide pages 1-2)
- Mean prevalence across four African countries: **1 in 4264** (range **1 in 1755–1 in 7900**). (kromberg2023determiningaworldwide pages 1-2)
- European estimates (three countries): mean **~1 in 12,000** (range **1 in 10,000–1 in 15,000**), potentially underestimated in fair-skinned populations. (kromberg2023determiningaworldwide pages 1-2, kromberg2023determiningaworldwide pages 3-5)

A key data table from this review is captured as an image (see cited table). (kromberg2023determiningaworldwide media 0f424986)

---

## 10. Diagnostics

### Clinical diagnostic features
High-frequency ocular signs include iris transillumination, fundus hypopigmentation, foveal hypoplasia, nystagmus, and optic pathway misrouting; VEP can support misrouting diagnosis, and OCT supports foveal hypoplasia grading (correlating with visual acuity). (thomas2023oculocutaneousalbinismanda pages 1-3)

### Genetic testing yield and real-world implementation (2023)
In a diverse U.S. pediatric cohort, genetic testing had a high diagnostic yield:
- Initial yield **66%**, increasing to **70%** after VUS reinterpretation; yield higher for OCA (**76%**) than OA (**33%**, p=0.007). (chan2023diagnosticyieldof pages 1-2)
- Most common solved genes were **OCA2 (28%)** and **TYR (20%)**; Hermansky–Pudlak syndrome variants were identified in **9%**. (chan2023diagnosticyieldof pages 1-2)

These data support real-world practice of using multigene panels/exome approaches with periodic reinterpretation of variants. (chan2023diagnosticyieldof pages 2-4)

### Differential diagnosis
Syndromic albinism conditions (e.g., Hermansky–Pudlak, Chediak–Higashi) and other pigment/retinal disorders should be considered when systemic features (bleeding diathesis, immunodeficiency, etc.) are present. (ambrosio2025advancinginsightsinto pages 11-13, chan2023diagnosticyieldof pages 1-2)

---

## 11. Outcome / Prognosis

Life expectancy is typically not reduced in nonsyndromic OCA, but morbidity is substantial due to lifelong low vision and preventable skin cancer burden; squamous/basal cell carcinomas can contribute to mortality in high UV environments. (kromberg2023determiningaworldwide pages 1-2, thomas2023oculocutaneousalbinismand pages 13-16)

---

## 12. Treatment

### Current standard management (supportive; real-world implementation)
GeneReviews emphasizes multidisciplinary supportive care:
- **Ophthalmology surveillance:** annual evaluations in children (<16 years), including refractive correction, strabismus/head posture assessment, and filter glasses. (thomas2023oculocutaneousalbinismand pages 13-16)
- **Low-vision/education interventions:** early intervention programs, individualized education plans (IEP), accommodations (magnifiers, enlarged text, assistive technology). (thomas2023oculocutaneousalbinismand pages 13-16)
- **Dermatology:** yearly total body skin exam is recommended with low biopsy threshold; melanoma can be difficult to detect because it may lack pigment; annual to biennial skin examination is recommended depending on exposure and context. (thomas2023oculocutaneousalbinismand pages 13-16)
- **Avoidance:** prolonged unprotected sun exposure should be avoided. (thomas2023oculocutaneousalbinismand pages 13-16)

### Emerging/experimental therapies and trials
**Nitisinone (OCA1B):** A completed NIH/NEI pilot phase 1/2 study (NCT01838655; ClinicalTrials.gov) tested **2 mg oral nitisinone daily for 12 months** in **5 adults** with OCA1B; the primary endpoint was change in iris pigmentation on an 8-point iris transillumination scale at 12 months, with visual function and pigmentation secondary outcomes. (NCT01838655 chunk 1)

**Levodopa (L-DOPA):** A completed randomized, placebo-controlled, double-masked phase 2 trial (NCT01176435) enrolled **45 participants** (ages 3–60) and tested oral levodopa/carbidopa dosing vs placebo with **binocular BCVA** as primary outcome over **20 weeks**. (NCT01176435 chunk 1)

**Gene therapy (OCA1):** A recruiting Early Phase 1 trial (NCT07313618; first posted 2026-01-02) tests **JWK010** (AAV vector encoding tyrosinase) via a **single suprachoroidal injection** (3+3 dose escalation; up to 18 children aged 5–12 with biallelic TYR pathogenic variants). Outcomes include safety, BCVA, fundus pigmentation, OCT, ERG, and VEP/MRI optic pathway measures. (NCT07313618 chunk 1)

### Suggested MAXO terms
Included in artifact-01 (genetic counseling, ophthalmologic examination, photoprotection, dermatologic surveillance, gene therapy, nitisinone therapy, levodopa therapy). (thomas2023oculocutaneousalbinismand pages 13-16, NCT01838655 chunk 1)

---

## 13. Prevention

Primary prevention of OCA is not currently possible (genetic), but prevention of complications is central:
- **Tertiary prevention:** strict photoprotection, avoidance of unprotected sun exposure, and regular dermatologic surveillance to prevent/early-detect precancerous/cancerous lesions. (thomas2023oculocutaneousalbinismand pages 13-16)
- **Secondary prevention (functional):** early vision services and educational accommodations to mitigate developmental/educational impacts of low vision. (thomas2023oculocutaneousalbinismand pages 13-16, galli2023oculocutaneousalbinismthe pages 1-2)

---

## 14. Other Species / Natural Disease

No OMIA/veterinary natural disease resources were retrieved in this run. (gap noted)

---

## 15. Model Organisms

A 2024 patient-derived **iPSC-RPE “disease-in-a-dish”** model provides a human cellular model of TYR-related OCA1A with absent pigmentation, absent TYR protein/activity, and defects in mature melanosomes, supporting mechanistic studies and therapeutic development. (subramani2024generationandcharacterization pages 1-2, subramani2024generationandcharacterization pages 8-11)

---

## Embedded Evidence Artifacts

### Evidence map table (genes, phenotypes, epidemiology, trials)
| Item | Details / statistics | Evidence source (year; DOI/URL) | Citation |
|---|---|---|---|
| Disease definition and core features | Oculocutaneous albinism (OCA) is a group of genetic disorders with absent or reduced melanin biosynthesis causing hypopigmentation of the eyes, skin, and hair, with common ocular findings including reduced visual acuity, foveal hypoplasia, nystagmus, iris transillumination defects, and optic pathway misrouting. ClinicalTrials.gov also indexes the condition under MeSH **Albinism, Oculocutaneous (D016115)**. | GeneReviews overview (2023); ClinicalTrials.gov NCT07313618 / NCT01838655; https://clinicaltrials.gov/study/NCT07313618 ; https://clinicaltrials.gov/study/NCT01838655 | (thomas2023oculocutaneousalbinismanda pages 1-3, NCT07313618 chunk 1, NCT01838655 chunk 8) |
| Inheritance pattern: nonsyndromic OCA | Nonsyndromic OCA caused by **TYR, OCA2, TYRP1, SLC45A2, SLC24A5, LRMDA/C10orf11, DCT/TYRP2** is inherited in an **autosomal recessive** manner. | GeneReviews overview (2023) | (thomas2023oculocutaneousalbinismand pages 13-16) |
| Inheritance pattern: ocular albinism | Ocular albinism caused by **GPR143 (OA1)** is inherited in an **X-linked** manner. | GeneReviews overview (2023) | (thomas2023oculocutaneousalbinismand pages 13-16, thomas2023oculocutaneousalbinismand pages 16-18) |
| Major causal genes: TYR | **TYR** causes OCA1; TYR encodes tyrosinase, the rate-limiting enzyme of melanin synthesis. OCA1A reflects complete loss of tyrosinase activity; OCA1B reflects residual activity. | Review / GeneReviews-derived summaries (2023); NPJ Genomic Medicine (2022) doi:10.1038/s41525-021-00275-9 https://doi.org/10.1038/s41525-021-00275-9 | (ambrosio2025advancinginsightsinto pages 11-13, thomas2023oculocutaneousalbinismand pages 13-16) |
| Major causal genes: OCA2 | **OCA2** causes OCA2 and is a common cause of OCA; in the 2023 U.S. pediatric cohort it accounted for **28%** of solved cases. | Genes (2023) doi:10.3390/genes14010135 https://doi.org/10.3390/genes14010135 | (chan2023diagnosticyieldof pages 1-2) |
| Major causal genes: TYRP1 | **TYRP1** causes OCA3; TYRP1 supports tyrosinase stability and melanogenesis. | Review summary (2025) / GeneReviews-derived gene list (2023) https://doi.org/10.3390/jcm14020614 | (ambrosio2025advancinginsightsinto pages 11-13, thomas2023oculocutaneousalbinismand pages 13-16) |
| Major causal genes: SLC45A2 | **SLC45A2** causes OCA4; implicated as a melanosomal transporter affecting pigmentation. | Review summary (2025) https://doi.org/10.3390/jcm14020614 ; GeneReviews overview (2023) | (ambrosio2025advancinginsightsinto pages 11-13, thomas2023oculocutaneousalbinismand pages 13-16) |
| Major causal genes: SLC24A5 | **SLC24A5** causes OCA6; encodes a K+-dependent Na+/Ca2+ exchanger important for melanosome homeostasis/pigmentation. | Pigment Cell Melanoma Res. (2020) doi:10.1111/pcmr.12879 https://doi.org/10.1111/pcmr.12879 ; GeneReviews overview (2023) | (thomas2023oculocutaneousalbinismand pages 13-16) |
| Major causal genes: LRMDA / C10orf11 | **LRMDA (C10orf11)** is listed among causal genes for autosomal recessive nonsyndromic OCA. | GeneReviews overview (2023) | (thomas2023oculocutaneousalbinismand pages 13-16) |
| Major causal genes: DCT / TYRP2 | **DCT (TYRP2)** is listed among causal genes for autosomal recessive nonsyndromic OCA. | GeneReviews overview (2023) | (thomas2023oculocutaneousalbinismand pages 13-16) |
| Major causal gene: GPR143 | **GPR143** causes X-linked ocular albinism (OA1). | GeneReviews overview (2023) | (thomas2023oculocutaneousalbinismand pages 13-16, thomas2023oculocutaneousalbinismand pages 16-18) |
| Diagnostic yield of genetic testing | In a diverse U.S. pediatric OA/OCA cohort, initial genetic diagnostic yield was **66% (35/53)** and increased to **70%** after VUS reinterpretation; yield was higher for OCA (**76%**) than OA (**33%**, p=0.007). | Genes (2023) doi:10.3390/genes14010135 https://doi.org/10.3390/genes14010135 | (chan2023diagnosticyieldof pages 2-4, chan2023diagnosticyieldof pages 1-2) |
| Ocular phenotype frequency: nystagmus | In the 2023 pediatric testing cohort, **nystagmus occurred in 89%** of tested OA/OCA patients. | Genes (2023) doi:10.3390/genes14010135 https://doi.org/10.3390/genes14010135 | (chan2023diagnosticyieldof pages 2-4) |
| Ocular phenotype frequency: foveal hypoplasia | In the 2023 pediatric testing cohort, **foveal hypoplasia occurred in 85%**. GeneReviews reports foveal hypoplasia in **94–100%** across OCA/OA series. | Genes (2023) doi:10.3390/genes14010135 https://doi.org/10.3390/genes14010135 ; GeneReviews overview (2023) | (chan2023diagnosticyieldof pages 2-4, thomas2023oculocutaneousalbinismanda pages 1-3) |
| Ocular phenotype frequency: fundus hypopigmentation | In the 2023 pediatric testing cohort, **fundus hypopigmentation occurred in 68%**. GeneReviews reports fundus hypopigmentation in **>94%**. | Genes (2023) doi:10.3390/genes14010135 https://doi.org/10.3390/genes14010135 ; GeneReviews overview (2023) | (chan2023diagnosticyieldof pages 2-4, thomas2023oculocutaneousalbinismanda pages 1-3) |
| Ocular phenotype frequency: iris transillumination defects | In the 2023 pediatric testing cohort, **iris transillumination defects occurred in 38%**. GeneReviews reports iris TID in **~91–100%** in classic series. | Genes (2023) doi:10.3390/genes14010135 https://doi.org/10.3390/genes14010135 ; GeneReviews overview (2023) | (chan2023diagnosticyieldof pages 2-4, thomas2023oculocutaneousalbinismanda pages 1-3) |
| Ocular phenotype frequency: chiasmal misrouting | GeneReviews reports abnormal optic chiasm decussation / visual pathway misrouting in **84–100%** of tested individuals. | GeneReviews overview (2023) | (thomas2023oculocutaneousalbinismanda pages 1-3) |
| Other ocular burden | Strabismus affects **~71%** overall and up to **100% in OCA1**; visual acuity can range from about **20/15 to 20/800** with median around **20/80** in reviewed cohorts. | GeneReviews overview (2023) | (thomas2023oculocutaneousalbinismanda pages 3-7, thomas2023oculocutaneousalbinismand pages 3-7) |
| Epidemiology: global summary | A 2023 systematic review found that only **26/193 countries (13%)** had published OCA prevalence figures; most data were outdated and African studies were overrepresented (**15/34, 44%**). | IOVS (2023) doi:10.1167/iovs.64.10.14 https://doi.org/10.1167/iovs.64.10.14 | (kromberg2023determiningaworldwide pages 1-2) |
| Epidemiology: Africa | Mean prevalence across four African countries was **1 in 4,264** (range **1 in 1,755 to 1 in 7,900**). | IOVS (2023) doi:10.1167/iovs.64.10.14 https://doi.org/10.1167/iovs.64.10.14 | (kromberg2023determiningaworldwide pages 1-2) |
| Epidemiology: Europe | Mean prevalence across three European countries was **~1 in 12,000** (range **1 in 10,000 to 1 in 15,000**), likely underestimated in fair-skinned populations. | IOVS (2023) doi:10.1167/iovs.64.10.14 https://doi.org/10.1167/iovs.64.10.14 | (kromberg2023determiningaworldwide pages 1-2, kromberg2023determiningaworldwide pages 3-5) |
| Epidemiology: population isolates | Highest rates were reported in population isolates, ranging from **1 in 22 to 1 in 1,300** (mean **1 in 464**). | IOVS (2023) doi:10.1167/iovs.64.10.14 https://doi.org/10.1167/iovs.64.10.14 | (kromberg2023determiningaworldwide pages 1-2, kromberg2023determiningaworldwide pages 3-5) |
| Epidemiology: common estimates and subtype differences | Older “global” estimates such as **1 in 17,000** are not generalizable. OCA2 is noted as especially common in southern Africa (~**1 in 4,000**), whereas OCA1 is relatively more common in European cohorts. | IOVS (2023) doi:10.1167/iovs.64.10.14 https://doi.org/10.1167/iovs.64.10.14 | (kromberg2023determiningaworldwide pages 1-2) |
| Current care / surveillance implementation | Real-world management includes annual ophthalmologic follow-up in children, low-vision/educational support, and **annual to biennial skin examinations** with strict sun protection; yearly dermatologist review is recommended because amelanotic melanoma can be hard to detect. | GeneReviews overview (2023) | (thomas2023oculocutaneousalbinismand pages 13-16) |
| Trial/intervention: nitisinone | **NCT01838655**; completed NIH/NEI phase 1/2 pilot in adults with **OCA1B**; **5 participants**; **2 mg oral nitisinone daily for 12 months**; primary endpoint was mean change in iris pigmentation on an 8-point transillumination scale at 12 months. | ClinicalTrials.gov NCT01838655; first posted 2013; https://clinicaltrials.gov/study/NCT01838655 | (NCT01838655 chunk 1) |
| Trial/intervention: L-DOPA | **NCT01176435**; completed phase 2 randomized double-masked placebo-controlled trial; **45 participants**, ages **3–60 years**; tested oral **levodopa/carbidopa** at two dose levels vs placebo for **20 weeks** with binocular best-corrected visual acuity as primary outcome. | ClinicalTrials.gov NCT01176435; first posted 2010; https://clinicaltrials.gov/study/NCT01176435 | (NCT01176435 chunk 1) |
| Trial/intervention: JWK010 gene therapy | **NCT07313618**; recruiting early phase 1 trial in China; single **suprachoroidal AAV-tyrosinase (JWK010)** injection in one eye for children **5–12 years** with biallelic **TYR** pathogenic variants; dose-escalation **3+3** design; estimated enrollment **9–18**; primary endpoint is safety, with secondary measures including BCVA, fundus pigmentation, SS-OCT macular structure, ERG, and VEP/MRI visual pathway assessment. | ClinicalTrials.gov NCT07313618; first posted 2026-01-02; https://clinicaltrials.gov/study/NCT07313618 | (NCT07313618 chunk 1) |


*Table: This table summarizes core disease concepts, genes, phenotype frequencies, epidemiology, and current/emerging interventions for oculocutaneous albinism using the cited GeneReviews, cohort, systematic review, and ClinicalTrials.gov sources. It is useful as a compact evidence map for a disease knowledge base entry.*

### Ontology mapping table (HPO/GO/CL/UBERON/MAXO suggestions)
| Domain | Term label | Suggested ontology ID | Supporting evidence summary | Citation |
|---|---|---|---|---|
| Phenotype | Foveal hypoplasia | HP:0000647 | Core ocular feature of OCA; reported in 85% of a U.S. pediatric genetic-testing cohort, and 94-100% in GeneReviews summary series. | (chan2023diagnosticyieldof pages 2-4, thomas2023oculocutaneousalbinismanda pages 1-3) |
| Phenotype | Nystagmus | HP:0000639 | Present in 89% of the U.S. pediatric cohort; 100% in the Italian neurodevelopment cohort of 18 children. | (chan2023diagnosticyieldof pages 2-4, galli2023oculocutaneousalbinismthe pages 4-5) |
| Phenotype | Strabismus | HP:0000486 | Reported in ~71% overall and up to 100% in OCA1 in GeneReviews; 78% in the pediatric neurodevelopment cohort. | (thomas2023oculocutaneousalbinismanda pages 3-7, galli2023oculocutaneousalbinismthe pages 4-5) |
| Phenotype | Photophobia | HP:0000613 | Common visual symptom; present in 44% of the pediatric neurodevelopment cohort. | (galli2023oculocutaneousalbinismthe pages 4-5) |
| Phenotype | Iris transillumination defect | HP:0001088 | Seen in 38% of the U.S. cohort and ~91-100% in classic GeneReviews series; useful diagnostic sign. | (chan2023diagnosticyieldof pages 2-4, thomas2023oculocutaneousalbinismanda pages 1-3) |
| Phenotype | Reduced visual acuity | HP:0007663 | Universal or near-universal ocular burden; GeneReviews reports acuity ranging about 20/15-20/800 with median ~20/80, and the neurodevelopment cohort found reduced acuity in 100%. | (thomas2023oculocutaneousalbinismanda pages 3-7, galli2023oculocutaneousalbinismthe pages 4-5) |
| Phenotype | Fundus hypopigmentation / hypopigmented fundus | HP:0007990 | Fundus hypopigmentation occurred in 68% of the U.S. cohort and >94% in GeneReviews summary data. | (chan2023diagnosticyieldof pages 2-4, thomas2023oculocutaneousalbinismanda pages 1-3) |
| Phenotype | Refractive error | HP:0000545 | Refractive errors are frequent in OCA; hypermetropia and with-the-rule astigmatism are common, and 100% of children in the neurodevelopment cohort had refractive errors. | (thomas2023oculocutaneousalbinismanda pages 3-7, galli2023oculocutaneousalbinismthe pages 4-5) |
| Phenotype | Abnormal head posture | HP:0000456 | Anomalous/abnormal head posture is common in albinism; 89% in the neurodevelopment cohort. | (thomas2023oculocutaneousalbinismanda pages 3-7, galli2023oculocutaneousalbinismthe pages 4-5) |
| Phenotype | Glare sensitivity | HP:0000746 | All 65 participants in a Botswana real-world cohort reported glare sensitivity (100%), supporting its relevance to low-vision management. | (thomas2023oculocutaneousalbinismanda pages 3-7) |
| Phenotype | Skin cancer susceptibility / increased skin cancer risk | HP:0032445 | OCA confers increased UV-related skin disease risk including SCC, BCC, melanoma, and Merkel cell carcinoma; annual to biennial skin examination is recommended. | (thomas2023oculocutaneousalbinismanda pages 3-7, thomas2023oculocutaneousalbinismand pages 13-16) |
| Phenotype | Global developmental delay / neurodevelopmental impairment | HP:0001263 | In a 2023 pediatric cohort, 56% had global neurodevelopmental impairment without progression to intellectual disability. | (galli2023oculocutaneousalbinismthe pages 1-2, galli2023oculocutaneousalbinismthe pages 5-6) |
| Phenotype | Autistic-like features / behavioral abnormality | HP:0000729 | 67% of children in the neurodevelopment cohort showed one or more autistic-like features; internalizing behavioral risk occurred in 33%. | (galli2023oculocutaneousalbinismthe pages 1-2, galli2023oculocutaneousalbinismthe pages 5-6) |
| Mechanism | Melanin biosynthetic process | GO:0042438 | Central upstream defect in OCA; TYR is the rate-limiting enzyme and impaired melanin biosynthesis underlies hypopigmentation and abnormal ocular development. | (ambrosio2025advancinginsightsinto pages 11-13, subramani2024generationandcharacterization pages 1-2) |
| Mechanism | Melanosome organization | GO:0032438 | Multiple OCA genes affect melanosome biogenesis/maturation; OCA1A iPSC-RPE showed absence of mature stage III/IV pigmented melanosomes. | (ambrosio2025advancinginsightsinto pages 11-13, subramani2024generationandcharacterization pages 8-11) |
| Mechanism | Melanosome membrane | GO:0031902 | OCA2 and SLC45A2 act through melanosomal function/pH regulation; disease mechanisms localize to melanosome-associated membrane systems. | (ambrosio2025advancinginsightsinto pages 11-13, green2024thecooccurrenceof pages 2-3) |
| Mechanism | Endoplasmic reticulum retention / protein folding defect | GO:0034976 | OCA1A TYR mutant protein can misfold, be retained in the ER, and lose enzymatic activity; iPSC-RPE showed absent TYR protein/activity. | (subramani2024generationandcharacterization pages 1-2, subramani2024generationandcharacterization pages 8-11) |
| Mechanism | Regulation of melanosomal pH |  | OCA2 modulates melanosome pH, affecting tyrosinase activity; SLC24A5 and SLC45A2 are also implicated in melanosome homeostasis. | (ambrosio2025advancinginsightsinto pages 11-13, green2024thecooccurrenceof pages 2-3) |
| Mechanism | Visual pathway misrouting / abnormal optic nerve decussation |  | Chiasmal misrouting is a hallmark downstream developmental consequence of reduced melanin, reported in 84-100% in GeneReviews. | (thomas2023oculocutaneousalbinismanda pages 1-3) |
| Cell type | Melanocyte | CL:0000148 | Primary pigment-producing cell type affected in skin/hair hypopigmentation; relevant to UV protection and cutaneous cancer susceptibility. | (ambrosio2025advancinginsightsinto pages 11-13, kromberg2023determiningaworldwide pages 1-2) |
| Cell type | Retinal pigment epithelial cell | CL:0002586 | Key ocular pigment cell type; patient-derived OCA1A iPSC-RPE lacked pigmentation, TYR protein, and mature melanosomes. | (subramani2024generationandcharacterization pages 1-2, subramani2024generationandcharacterization pages 8-11) |
| Cell type | Retinal ganglion cell | CL:0000740 | Relevant to optic pathway development and chiasmal misrouting in albinism. | (ambrosio2025advancinginsightsinto pages 11-13, thomas2023oculocutaneousalbinismanda pages 1-3) |
| Anatomy | Eye | UBERON:0000970 | Primary organ affected with reduced pigmentation, refractive abnormalities, nystagmus, strabismus, and low vision. | (ambrosio2025advancinginsightsinto pages 11-13, galli2023oculocutaneousalbinismthe pages 4-5) |
| Anatomy | Retina | UBERON:0000966 | Retinal hypopigmentation and structural abnormalities are central to disease; OCT often demonstrates foveal hypoplasia. | (ambrosio2025advancinginsightsinto pages 11-13, thomas2023oculocutaneousalbinismanda pages 1-3) |
| Anatomy | Fovea centralis | UBERON:0006612 | Developmentally underformed in OCA; severity correlates with visual acuity. | (thomas2023oculocutaneousalbinismanda pages 3-7, thomas2023oculocutaneousalbinismanda pages 1-3) |
| Anatomy | Optic chiasm | UBERON:0001709 | Site of abnormal decussation / visual pathway misrouting. | (ambrosio2025advancinginsightsinto pages 11-13, thomas2023oculocutaneousalbinismanda pages 1-3) |
| Anatomy | Skin | UBERON:0002097 | Major extraocular site of hypopigmentation and UV-related morbidity. | (kromberg2023determiningaworldwide pages 1-2, thomas2023oculocutaneousalbinismand pages 13-16) |
| Anatomy | Epidermis | UBERON:0001003 | Relevant cutaneous compartment for melanin deficiency and photoprotection interventions. | (kromberg2023determiningaworldwide pages 1-2, thomas2023oculocutaneousalbinismand pages 13-16) |
| Intervention | Genetic counseling | MAXO:0000055 | Recommended for inheritance risk assessment, carrier testing, family planning, and prenatal/preimplantation testing once familial variants are known. | (thomas2023oculocutaneousalbinismand pages 13-16, thomas2023oculocutaneousalbinismand pages 16-18) |
| Intervention | Low vision rehabilitation |  | GeneReviews recommends low-vision clinic review as needed; educational accommodations, magnifiers, enlarged text, and assistive technology are standard real-world supports. | (thomas2023oculocutaneousalbinismand pages 13-16) |
| Intervention | Sunscreen / photoprotection |  | Strict sun protection is standard supportive care; annual to biennial skin examination is recommended because UV-related skin damage risk is increased. | (thomas2023oculocutaneousalbinismand pages 13-16) |
| Intervention | Dermatologic surveillance |  | Yearly total-body skin examination by a trained dermatologist is highly recommended; low threshold for biopsy because melanoma may be amelanotic. | (thomas2023oculocutaneousalbinismand pages 13-16) |
| Intervention | Ophthalmologic examination |  | Annual ophthalmologic review in children is recommended, including refractive error, strabismus/head posture, and filter-glass needs; OCT/VEP are useful diagnostic adjuncts. | (thomas2023oculocutaneousalbinismand pages 13-16, thomas2023oculocutaneousalbinismanda pages 1-3) |
| Intervention | Gene therapy |  | Early-phase interventional development is active: JWK010 (AAV-tyrosinase) is a recruiting dose-escalation OCA1 trial using suprachoroidal injection with safety as the primary endpoint. | (NCT07313618 chunk 1) |
| Intervention | Nitisinone therapy |  | Completed NIH pilot trial in adult OCA1B used 2 mg oral nitisinone daily for 12 months to assess iris pigmentation and visual outcomes. | (NCT01838655 chunk 1) |
| Intervention | Levodopa therapy |  | Completed randomized placebo-controlled phase 2 trial tested oral levodopa/carbidopa in 45 individuals with albinism over 20 weeks, with binocular BCVA as the primary endpoint. | (NCT01176435 chunk 1) |


*Table: This table maps major oculocutaneous albinism phenotypes, mechanisms, anatomical sites, cell types, and management strategies to suggested ontology terms. It is designed as a knowledge-base ready artifact that links clinical and mechanistic evidence to HPO, GO, CL, UBERON, and MAXO concepts with supporting citations.*

---

## Key visual evidence (epidemiology table image)
The prevalence-by-continent table from the 2023 systematic review is provided as a cropped figure for direct use in epidemiology extraction workflows. (kromberg2023determiningaworldwide media 0f424986)

---

## Notes on evidence gaps relative to requested template
- **MONDO / Orphanet / ICD-11 identifiers:** not present in the retrieved evidence during this run; would require direct ontology/registry queries beyond the current tool evidence set. (NCT07313618 chunk 2, NCT04068961 chunk 1)
- **PMIDs:** Some items (e.g., GeneReviews overview and ClinicalTrials.gov records) are not primarily indexed by PMID; where possible, the GeneReviews reference list indicates related PubMed-indexed trials/papers, but PMIDs were not consistently extractable from the current text chunks. (thomas2023oculocutaneousalbinismand pages 16-18, NCT01838655 chunk 1)


References

1. (ambrosio2025advancinginsightsinto pages 11-13): Lucia Ambrosio, Tatiana Perepelkina, Abdelrahman M. Elhusseiny, Anne B. Fulton, and Jose Efren Gonzalez Monroy. Advancing insights into pediatric macular diseases: a comprehensive review. Journal of Clinical Medicine, 14:614, Jan 2025. URL: https://doi.org/10.3390/jcm14020614, doi:10.3390/jcm14020614. This article has 4 citations.

2. (thomas2023oculocutaneousalbinismanda pages 1-3): MG Thomas, J Zippin, and BP Brooks. Oculocutaneous albinism and ocular albinism overview. Unknown journal, 2023.

3. (kromberg2023determiningaworldwide pages 1-2): Jennifer G. R. Kromberg, Kaitlyn A. Flynn, and Robyn A. Kerr. Determining a worldwide prevalence of oculocutaneous albinism: a systematic review. Investigative Opthalmology &amp; Visual Science, 64:14, Jul 2023. URL: https://doi.org/10.1167/iovs.64.10.14, doi:10.1167/iovs.64.10.14. This article has 61 citations.

4. (NCT07313618 chunk 2): Fang Lu. Safety and Efficacy of a Single Suprachoroidal Injection of JWK010 Gene Therapy in Subjects With Oculocutaneous Albinism Type 1 (OCA1). West China Hospital. 2025. ClinicalTrials.gov Identifier: NCT07313618

5. (NCT01176435 chunk 1):  Trial of L-DOPA as a Treatment to Improve Vision in Albinism. University of Minnesota. 2010. ClinicalTrials.gov Identifier: NCT01176435

6. (fassad2026wholegenomesequencinguncovers pages 5-8): Mahmoud R. Fassad, Pradeep C. Vasudevan, Julian Barwell, Gail DE Maconachie, Savita Madhusudhan, David Hunt, Irene Gottlob, Mariya Moosajee, Omar A. Mahroo, Andrew R. Webster, Michel Michaelides, and Mervyn G. Thomas. Whole-genome sequencing uncovers diverse genetic causes and phenotypic signatures in infantile nystagmus and albinism. npj Genomic Medicine, May 2026. URL: https://doi.org/10.1038/s41525-026-00580-1, doi:10.1038/s41525-026-00580-1. This article has 0 citations and is from a peer-reviewed journal.

7. (thomas2023oculocutaneousalbinismand pages 7-8): MG Thomas, J Zippin, and BP Brooks. Oculocutaneous albinism and ocular albinism overview. Unknown journal, 2023.

8. (NCT00001153 chunk 1):  Visual Function and Ocular Pigmentation in Albinism. National Eye Institute (NEI). 1976. ClinicalTrials.gov Identifier: NCT00001153

9. (NCT04068961 chunk 1):  New Strategies of Genetic Study of Patients With Oculocutaneous Albinism. University Hospital, Bordeaux. 2010. ClinicalTrials.gov Identifier: NCT04068961

10. (NCT07313618 chunk 1): Fang Lu. Safety and Efficacy of a Single Suprachoroidal Injection of JWK010 Gene Therapy in Subjects With Oculocutaneous Albinism Type 1 (OCA1). West China Hospital. 2025. ClinicalTrials.gov Identifier: NCT07313618

11. (NCT01838655 chunk 1):  Nitisinone for Type 1B Oculocutaneous Albinism. National Eye Institute (NEI). 2013. ClinicalTrials.gov Identifier: NCT01838655

12. (NCT01838655 chunk 7):  Nitisinone for Type 1B Oculocutaneous Albinism. National Eye Institute (NEI). 2013. ClinicalTrials.gov Identifier: NCT01838655

13. (chan2023diagnosticyieldof pages 1-2): Kyle S Chan, Brenda L. Bohnsack, Alexander Ing, Andrew Drackley, Valerie Castelluccio, Kevin X. Zhang, Hantamalala Ralay-Ranaivo, and Jennifer L. Rossen. Diagnostic yield of genetic testing for ocular and oculocutaneous albinism in a diverse united states pediatric population. Genes, 14:135, Jan 2023. URL: https://doi.org/10.3390/genes14010135, doi:10.3390/genes14010135. This article has 13 citations.

14. (thomas2023oculocutaneousalbinismand pages 16-18): MG Thomas, J Zippin, and BP Brooks. Oculocutaneous albinism and ocular albinism overview. Unknown journal, 2023.

15. (thomas2023oculocutaneousalbinismand pages 13-16): MG Thomas, J Zippin, and BP Brooks. Oculocutaneous albinism and ocular albinism overview. Unknown journal, 2023.

16. (chan2023diagnosticyieldof pages 2-4): Kyle S Chan, Brenda L. Bohnsack, Alexander Ing, Andrew Drackley, Valerie Castelluccio, Kevin X. Zhang, Hantamalala Ralay-Ranaivo, and Jennifer L. Rossen. Diagnostic yield of genetic testing for ocular and oculocutaneous albinism in a diverse united states pediatric population. Genes, 14:135, Jan 2023. URL: https://doi.org/10.3390/genes14010135, doi:10.3390/genes14010135. This article has 13 citations.

17. (green2024thecooccurrenceof pages 1-2): David J. Green, Vincent Michaud, Eulalie Lasseaux, Claudio Plaisant, Tomas Fitzgerald, Ewan Birney, Graeme C. Black, Benoît Arveiler, and Panagiotis I. Sergouniotis. The co-occurrence of genetic variants in the tyr and oca2 genes confers susceptibility to albinism. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-52763-y, doi:10.1038/s41467-024-52763-y. This article has 9 citations and is from a highest quality peer-reviewed journal.

18. (green2024thecooccurrenceof pages 2-3): David J. Green, Vincent Michaud, Eulalie Lasseaux, Claudio Plaisant, Tomas Fitzgerald, Ewan Birney, Graeme C. Black, Benoît Arveiler, and Panagiotis I. Sergouniotis. The co-occurrence of genetic variants in the tyr and oca2 genes confers susceptibility to albinism. Nature Communications, Sep 2024. URL: https://doi.org/10.1038/s41467-024-52763-y, doi:10.1038/s41467-024-52763-y. This article has 9 citations and is from a highest quality peer-reviewed journal.

19. (thomas2023oculocutaneousalbinismand pages 3-7): MG Thomas, J Zippin, and BP Brooks. Oculocutaneous albinism and ocular albinism overview. Unknown journal, 2023.

20. (galli2023oculocutaneousalbinismthe pages 1-2): Jessica Galli, Erika Loi, Laura Dusi, Nadia Pasini, Andrea Rossi, Vera Scaglioni, Lucia Mauri, and Elisa Fazzi. Oculocutaneous albinism: the neurological, behavioral, and neuro-ophthalmological perspective. European Journal of Pediatrics, 182:2723-2733, Apr 2023. URL: https://doi.org/10.1007/s00431-023-04938-w, doi:10.1007/s00431-023-04938-w. This article has 14 citations and is from a peer-reviewed journal.

21. (galli2023oculocutaneousalbinismthe pages 5-6): Jessica Galli, Erika Loi, Laura Dusi, Nadia Pasini, Andrea Rossi, Vera Scaglioni, Lucia Mauri, and Elisa Fazzi. Oculocutaneous albinism: the neurological, behavioral, and neuro-ophthalmological perspective. European Journal of Pediatrics, 182:2723-2733, Apr 2023. URL: https://doi.org/10.1007/s00431-023-04938-w, doi:10.1007/s00431-023-04938-w. This article has 14 citations and is from a peer-reviewed journal.

22. (subramani2024generationandcharacterization pages 1-2): Janavi Subramani, Niharika Patlolla, Rajani Battu, Taslimarif Saiyed, and Rajarshi Pal. Generation and characterization of retinal pigment epithelium from patient ipsc line to model oculocutaneous albinism (oca)1a disease. Journal of Biosciences, 49:1-14, Jan 2024. URL: https://doi.org/10.1007/s12038-023-00406-7, doi:10.1007/s12038-023-00406-7. This article has 5 citations and is from a peer-reviewed journal.

23. (subramani2024generationandcharacterization pages 8-11): Janavi Subramani, Niharika Patlolla, Rajani Battu, Taslimarif Saiyed, and Rajarshi Pal. Generation and characterization of retinal pigment epithelium from patient ipsc line to model oculocutaneous albinism (oca)1a disease. Journal of Biosciences, 49:1-14, Jan 2024. URL: https://doi.org/10.1007/s12038-023-00406-7, doi:10.1007/s12038-023-00406-7. This article has 5 citations and is from a peer-reviewed journal.

24. (kromberg2023determiningaworldwide pages 3-5): Jennifer G. R. Kromberg, Kaitlyn A. Flynn, and Robyn A. Kerr. Determining a worldwide prevalence of oculocutaneous albinism: a systematic review. Investigative Opthalmology &amp; Visual Science, 64:14, Jul 2023. URL: https://doi.org/10.1167/iovs.64.10.14, doi:10.1167/iovs.64.10.14. This article has 61 citations.

25. (kromberg2023determiningaworldwide media 0f424986): Jennifer G. R. Kromberg, Kaitlyn A. Flynn, and Robyn A. Kerr. Determining a worldwide prevalence of oculocutaneous albinism: a systematic review. Investigative Opthalmology &amp; Visual Science, 64:14, Jul 2023. URL: https://doi.org/10.1167/iovs.64.10.14, doi:10.1167/iovs.64.10.14. This article has 61 citations.

26. (NCT01838655 chunk 8):  Nitisinone for Type 1B Oculocutaneous Albinism. National Eye Institute (NEI). 2013. ClinicalTrials.gov Identifier: NCT01838655

27. (thomas2023oculocutaneousalbinismanda pages 3-7): MG Thomas, J Zippin, and BP Brooks. Oculocutaneous albinism and ocular albinism overview. Unknown journal, 2023.

28. (galli2023oculocutaneousalbinismthe pages 4-5): Jessica Galli, Erika Loi, Laura Dusi, Nadia Pasini, Andrea Rossi, Vera Scaglioni, Lucia Mauri, and Elisa Fazzi. Oculocutaneous albinism: the neurological, behavioral, and neuro-ophthalmological perspective. European Journal of Pediatrics, 182:2723-2733, Apr 2023. URL: https://doi.org/10.1007/s00431-023-04938-w, doi:10.1007/s00431-023-04938-w. This article has 14 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Oculocutaneous_Albinism-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Oculocutaneous_Albinism-deep-research-falcon_artifacts/artifact-01.md)
![## Context ID: pqac-00000020 I have extracted the table titled 'Albinism Prevalence Data Categorized by Continent' from page 4 of the document. This table provi](Oculocutaneous_Albinism-deep-research-falcon_artifacts/image-1.png)