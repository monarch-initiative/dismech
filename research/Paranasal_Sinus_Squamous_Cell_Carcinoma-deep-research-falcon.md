---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T10:17:42.668749'
end_time: '2026-06-17T10:30:02.272566'
duration_seconds: 739.6
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Paranasal Sinus Squamous Cell Carcinoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 32
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Paranasal_Sinus_Squamous_Cell_Carcinoma-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Paranasal Sinus Squamous Cell Carcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Paranasal Sinus Squamous Cell Carcinoma** covering all of the
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
- **Disease Name:** Paranasal Sinus Squamous Cell Carcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Paranasal Sinus Squamous Cell Carcinoma** covering all of the
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


## Comprehensive Research Report: Paranasal Sinus Squamous Cell Carcinoma (Sinonasal Squamous Cell Carcinoma)

### Target disease
- **Disease name (preferred working label):** Paranasal Sinus Squamous Cell Carcinoma (PNS-SCC)
- **Common literature umbrella term:** **Sinonasal squamous cell carcinoma (SNSCC / snSCC)**, which includes SCCs of the **nasal cavity and paranasal sinuses** (kacorzyk2025currentevidenceof pages 1-2, ferrari2021sinonasalsquamouscell pages 2-3).
- **MONDO ID / Orphanet / OMIM:** Not available in the retrieved sources; requires dedicated ontology lookup beyond the current evidence set (kacorzyk2025currentevidenceof pages 1-2).

### 1) Disease information (concepts, definitions, identifiers)
**Definition and scope.** Sinonasal carcinoma refers to malignancies arising in the **nasal cavity and paranasal sinuses**, and **sinonasal squamous cell carcinoma** accounts for **over half** of sinonasal carcinomas in some series/reviews (kacorzyk2025currentevidenceof pages 1-2). In a large narrative review, SNSCC was reported to account for ~50–60% of sinonasal cancers and is subclassified into **keratinizing (~50%)** and **non-keratinizing (~30%)** forms, with other variants comprising ~20% (ferrari2021sinonasalsquamouscell pages 2-3).

**Key identifiers/coding (site-based).** Population registries commonly code sinonasal cancers using ICD-10 topography **C30.0** (nasal cavity) and **C31.0–C31.9** (accessory/paranasal sinuses, including maxillary/ethmoid/frontal/sphenoid) (binazzi2024genderdifferencesin pages 2-3, binazzi2024genderdifferencesin pages 5-7). Because “paranasal sinus SCC” is a **site-defined** carcinoma, ICD-O morphology (SCC) must be paired with site codes; exact ICD-O morphology codes were not provided in retrieved sources (kacorzyk2025currentevidenceof pages 1-2).

| Identifier system | Code/term | Scope/notes | Source URL (if known) | Publication year/date (if applicable) |
|---|---|---|---|---|
| Disease label | Paranasal Sinus Squamous Cell Carcinoma | Practical disease label for SCC arising in accessory/paranasal sinuses; usually discussed within the broader sinonasal SCC literature, because sinonasal carcinoma includes the nasal cavity and paranasal sinuses (kacorzyk2025currentevidenceof pages 1-2, binazzi2024genderdifferencesin pages 2-3) | https://doi.org/10.3390/cancers16112053; https://doi.org/10.5603/njo.106945 | 2024-05; 2025-10 |
| Disease label / synonym | Sinonasal Squamous Cell Carcinoma (SNSCC; snSCC) | Standard umbrella term in current literature; snSCC accounts for over half of sinonasal carcinomas, and the maxillary sinus is the most common site followed by nasal cavity and ethmoid sinus (kacorzyk2025currentevidenceof pages 1-2, ferrari2021sinonasalsquamouscell pages 2-3) | https://doi.org/10.5603/njo.106945; https://doi.org/10.3390/cancers13112835 | 2025-10; 2021-06 |
| ICD-10 topography | C30.0 — Malignant neoplasm of nasal cavity | Nasal cavity subsite used in sinonasal cancer registries; part of the sinonasal spectrum, not strictly a paranasal sinus site (binazzi2024genderdifferencesin pages 5-7, binazzi2024genderdifferencesin pages 2-3) | https://doi.org/10.3390/cancers16112053 | 2024-05 |
| ICD-10 topography | C31.0 — Malignant neoplasm of maxillary sinus | Major paranasal sinus subsite; maxillary sinus is a frequent/common primary site and often the most common for SNSCC-focused series (binazzi2024genderdifferencesin pages 5-7, koller2024sinonasalcancercases pages 1-3, ferrari2021sinonasalsquamouscell pages 2-3) | https://doi.org/10.3390/cancers16112053; https://doi.org/10.23749/mdl.v115i1.15066; https://doi.org/10.3390/cancers13112835 | 2024-05; 2024-02; 2021-06 |
| ICD-10 topography | C31.1 — Malignant neoplasm of ethmoidal sinus | Ethmoid sinus subsite used in registry analyses; common accessory sinus code within sinonasal epidemiology (binazzi2024genderdifferencesin pages 5-7, binazzi2024genderdifferencesin pages 3-5) | https://doi.org/10.3390/cancers16112053 | 2024-05 |
| ICD-10 topography | C31.2 — Malignant neoplasm of frontal sinus | Accessory/paranasal sinus topography code; relevant for frontal sinus malignancies within sinonasal cancer classification (binazzi2024genderdifferencesin pages 2-3) | https://doi.org/10.3390/cancers16112053 | 2024-05 |
| ICD-10 topography | C31.3 — Malignant neoplasm of sphenoidal sinus | Accessory/paranasal sinus topography code within the sinonasal ICD-10 group C31.0–C31.9 cited by registry-based SNC studies (binazzi2024genderdifferencesin pages 2-3) | https://doi.org/10.3390/cancers16112053 | 2024-05 |
| ICD-10 topography | C31.8 — Overlapping lesion of accessory sinuses | Used when overlapping paranasal sinus involvement prevents assignment to a single sinus subsite; falls within C31.0–C31.9 sinonasal registry coding framework (binazzi2024genderdifferencesin pages 2-3) | https://doi.org/10.3390/cancers16112053 | 2024-05 |
| ICD-10 topography | C31.9 — Malignant neoplasm of accessory sinus, unspecified | Used for unspecified accessory/paranasal sinus primary site; included in the sinonasal topography family C31.0–C31.9 (binazzi2024genderdifferencesin pages 2-3) | https://doi.org/10.3390/cancers16112053 | 2024-05 |
| ICD-O note | Squamous cell carcinoma histology (ICD-O morphology; specific morphology code not retrieved here) | Topography codes above define site; SCC is the morphology/histology. Retrieved sources describe SCC/snSCC as a major histology, but did not provide the exact ICD-O morphology code and this requires external oncology coding lookup (kacorzyk2025currentevidenceof pages 1-2, binazzi2024genderdifferencesin pages 2-3) | https://doi.org/10.5603/njo.106945; https://doi.org/10.3390/cancers16112053 | 2025-10; 2024-05 |
| MeSH / disease family | Paranasal Sinus Neoplasms | Appropriate broader controlled-vocabulary concept for tumors of the paranasal sinuses; SNC/SNSCC literature commonly groups nasal cavity and paranasal sinus cancers together, with SCC a major morphology (kacorzyk2025currentevidenceof pages 1-2, binazzi2024genderdifferencesin pages 2-3) | Not provided in retrieved sources | Not retrieved |
| Synonym | Paranasal sinus SCC | Common descriptive synonym emphasizing accessory sinus origin; usually overlaps with maxillary/ethmoid/frontal/sphenoid sinus SCC cases within SNSCC series (ferrari2021sinonasalsquamouscell pages 2-3, koller2024sinonasalcancercases pages 1-3) | https://doi.org/10.3390/cancers13112835; https://doi.org/10.23749/mdl.v115i1.15066 | 2021-06; 2024-02 |
| Synonym | Maxillary sinus SCC | Common site-specific synonym; maxillary sinus is the predominant paranasal sinus site in several registry/series datasets (koller2024sinonasalcancercases pages 1-3, ferrari2021sinonasalsquamouscell pages 2-3) | https://doi.org/10.23749/mdl.v115i1.15066; https://doi.org/10.3390/cancers13112835 | 2024-02; 2021-06 |
| Synonym | Nasal cavity SCC | Site-specific synonym for the non-sinus sinonasal counterpart; often analyzed together with paranasal sinus SCC under SNSCC/SNC (kacorzyk2025currentevidenceof pages 1-2, binazzi2024genderdifferencesin pages 5-7) | https://doi.org/10.5603/njo.106945; https://doi.org/10.3390/cancers16112053 | 2025-10; 2024-05 |
| Synonym | Schneiderian carcinoma | Less specific legacy/pathology-oriented synonym that may be used for carcinomas arising from Schneiderian mucosa; requires case-level histologic clarification because not all Schneiderian carcinomas are conventional SCC (ferrari2021sinonasalsquamouscell pages 2-3) | https://doi.org/10.3390/cancers13112835 | 2021-06 |
| MONDO | Not found in retrieved sources; requires external ontology lookup | No MONDO identifier was present in the retrieved evidence set (kacorzyk2025currentevidenceof pages 1-2) | Not available from retrieved sources | Not retrieved |
| Orphanet | Not found in retrieved sources; requires external ontology lookup | No Orphanet identifier was present in the retrieved evidence set (kacorzyk2025currentevidenceof pages 1-2) | Not available from retrieved sources | Not retrieved |
| OMIM | Not found in retrieved sources; requires external ontology lookup | OMIM is generally not the primary identifier source for a site-defined adult epithelial carcinoma and was not provided in retrieved sources (kacorzyk2025currentevidenceof pages 1-2) | Not available from retrieved sources | Not retrieved |


*Table: This table summarizes the main site-based coding systems and common names used for paranasal/sinonasal squamous cell carcinoma. It highlights the distinction between ICD-10 topography codes and SCC histology, while noting which ontology identifiers were not available in the retrieved evidence.*

**Data provenance.** Evidence here comes from **aggregated disease-level** sources: national registries and large retrospective cohorts (Italy ReNaTuNS; Brazilian hospital registry) and disease-level reviews; no EHR-derived individual-level datasets were retrieved in this run (binazzi2024genderdifferencesin pages 1-2, koller2024sinonasalcancercases pages 1-3, kacorzyk2025currentevidenceof pages 1-2).

### 2) Etiology (causal factors, risks, protective factors, G×E)
#### 2.1 Primary causal and risk factors
**Occupational carcinogen exposure** is a dominant etiologic theme for sinonasal cancers and is repeatedly emphasized in registry-based work (binazzi2024genderdifferencesin pages 1-2, binazzi2024genderdifferencesin pages 5-7). In the Italian ReNaTuNS registry paper (Cancers, 2024-05-28; URL https://doi.org/10.3390/cancers16112053), the abstract states: **“Sinonasal cancer (SNC) is strongly associated with occupational exposure to several carcinogens involved in SNC’s etiology”** (binazzi2024genderdifferencesin pages 2-3).

Quantitative exposure patterns in ReNaTuNS (exposure assessed in 76.3% of cases):
- Wood and leather dusts were the most frequent identified occupational carcinogens: **41% of men and 33% of women** had wood/leather dust exposure (binazzi2024genderdifferencesin pages 1-2).
- Among exposed cases, **wood dust** accounted for **43% of male** and **19% of female** exposures; **leather dust** accounted for **25% of male** and **30% of female** exposures (binazzi2024genderdifferencesin pages 5-7).
- Other exposures/agents noted in the registry report include lower-frequency exposures such as **hexavalent chromium and formaldehyde** (binazzi2024genderdifferencesin pages 5-7).

**Tobacco** is cited as an etiologic factor in clinical reviews of snSCC (kacorzyk2025currentevidenceof pages 2-3), and is also implicated in malignant transformation of inverted papilloma in sinonasal tract (ferrari2021sinonasalsquamouscell pages 2-3).

**HPV (human papillomavirus)**: HPV is detected in a subset of SNSCC and is often associated with improved outcomes in review-level syntheses (kacorzyk2025currentevidenceof pages 2-3, ferrari2021sinonasalsquamouscell pages 2-3). Ferrari et al. (Cancers, 2021-06-07; URL https://doi.org/10.3390/cancers13112835) summarize that HPV is detected in ~20–25% of SNSCCs and may be more common in non-keratinizing SNSCC (ferrari2021sinonasalsquamouscell pages 2-3). A later clinician-facing synthesis reports broader ranges (HPV detected **8–62%**) and notes association with improved survival (kacorzyk2025currentevidenceof pages 2-3). 

#### 2.2 Protective factors
No genetic or environmental protective factors specific to paranasal sinus SCC were identified in the retrieved evidence set. However, prevention-relevant risk modification is supported: reduction of occupational exposures and tobacco cessation logically reduce risk burden in populations with occupationally attributable SNC (binazzi2024genderdifferencesin pages 1-2, binazzi2024genderdifferencesin pages 5-7).

#### 2.3 Gene–environment interactions
The retrieved sources do not provide explicit statistical G×E interaction models (e.g., genotype × wood-dust exposure) for SNSCC/PNS-SCC. The main actionable G×E concept is that **occupational carcinogen exposure** is a major upstream driver of sinonasal carcinogenesis in registry data (binazzi2024genderdifferencesin pages 1-2, binazzi2024genderdifferencesin pages 5-7).

### 3) Phenotypes / clinical presentation (with HPO suggestions)
Clinical reviews emphasize that sinonasal carcinoma diagnosis is often delayed because early symptoms are nonspecific and the anatomy is complex (kacorzyk2025currentevidenceof pages 1-2). While detailed symptom frequencies were not retrievable in the current evidence set, typical phenotype categories for PNS-SCC (to be verified against dedicated clinical series) include:
- **Nasal obstruction** (suggest HPO: *Nasal obstruction* HP:0001742)
- **Epistaxis** (HP:0000421)
- **Facial pain** / *Facial pain* (HP:0011137)
- **Facial swelling** (HP:0012368)
- **Anosmia/hyposmia** (HP:0000458 / HP:0004409)
- **Orbital involvement** leading to diplopia or proptosis in advanced disease (e.g., *Diplopia* HP:0000651; *Proptosis* HP:0000520)

Disease course features supported by evidence:
- **High local recurrence burden** is a hallmark outcome phenotype: local recurrence is reported as the main failure pattern, ~50% in clinician-focused synthesis, with **median time to local recurrence ~8–16 months** (kacorzyk2025currentevidenceof pages 2-3).

Quality-of-life impact: A systematic review of psychological impact in sinonasal cancers is available in retrieved papers, but it did not provide site-specific quantitative distress effect sizes in the extracted evidence; it supports that sinonasal cancer patients can experience significant distress and QoL impacts (kacorzyk2025currentevidenceof pages 2-3).

### 4) Genetic / molecular information (somatic alterations; biomarkers; actionable targets)
#### 4.1 HPV/p16 as a molecular subtype and prognostic biomarker (2023 primary evidence)
Wang et al. (Neoplasma, 2023-06; URL https://doi.org/10.4149/neo_2023_230117n34) provide large-cohort evidence for p16 IHC in SNSCC. From the abstract: **“p16 was found in 22.0% (38/173) of SNSCC patients”** and **“p16-positive patients had a considerably superior 5-year overall survival (OS) rate (80.7% vs. 57.5%, p=0.039)”** (wang2023immunohistochemicalp16expression pages 1-2). The abstract further reports a maxillary-sinus–specific effect: **“In maxillary sinus lesions, p16-positive SNSCC had a better 5-year OS (87.4% vs. 49.2%, p=0.03)”** (wang2023immunohistochemicalp16expression pages 1-2). Importantly, the authors note a key limitation: **“we could not analyze the relationship between p16 and HPV in SNSCC due to a lack of HPV status testing.”** (wang2023immunohistochemicalp16expression pages 6-7). 

Interpretation: p16 IHC appears to identify a prognostically favorable subgroup in non–T4b disease and especially in maxillary sinus tumors in this cohort, but p16 is not definitively equivalent to transcriptionally active HPV in SNSCC without direct HPV assays (wang2023immunohistochemicalp16expression pages 1-2, wang2023immunohistochemicalp16expression pages 6-7).

#### 4.2 Immune biomarkers
A clinician-facing synthesis reports **PD-L1 expression in ~45%** of cases, supporting biologic plausibility of checkpoint blockade in some patients (kacorzyk2025currentevidenceof pages 2-3).

#### 4.3 Somatic alterations and actionable targets (evidence limitations)
The retrieved evidence set contains review-level statements that SNSCC has ongoing advances in molecular definition (ferrari2021sinonasalsquamouscell pages 2-3, kacorzyk2025currentevidenceof pages 1-2) but does not include a modern (2023–2024) primary multi-omic/genomic study focused specifically on **paranasal sinus SCC** (maxillary/ethmoid/frontal/sphenoid SCC) with a complete alteration frequency table. As a result, the following are best treated as **candidate** pathways/targets inferred from broad SNSCC reviews rather than fully extracted primary genomic statistics:
- Cell-cycle dysregulation (p16/CDKN2A axis) (wang2023immunohistochemicalp16expression pages 1-2)
- Immune evasion via PD-1/PD-L1 (terazawa2025immunecheckpointinhibitors pages 2-4)

### 5) Mechanism / pathophysiology (causal chain; GO/CL suggestions)
#### 5.1 Causal chain (integrated from occupational/viral evidence)
1. **Exposure/trigger (upstream):** chronic inhalational exposure to occupational carcinogens (e.g., wood/leather dusts; other chemical exposures) and/or HPV infection in a subset (binazzi2024genderdifferencesin pages 5-7, ferrari2021sinonasalsquamouscell pages 2-3).
2. **Mucosal injury/inflammation and genomic/epigenomic perturbation (intermediate):** repeated epithelial damage and inflammatory microenvironment; in HPV-associated cases, viral oncogene expression disrupts cell-cycle checkpoints (review-level concept; direct E6/E7 measurements not extracted here) (ferrari2021sinonasalsquamouscell pages 2-3, wang2023immunohistochemicalp16expression pages 1-2).
3. **Neoplastic transformation:** SCC develops from sinonasal mucosal epithelium; can arise de novo or in association with inverted papilloma (kacorzyk2025currentevidenceof pages 1-2, ferrari2021sinonasalsquamouscell pages 2-3).
4. **Local invasion and recurrence (downstream):** advanced local invasion is common at diagnosis, and local recurrence is a principal failure pattern (kacorzyk2025currentevidenceof pages 2-3).

#### 5.2 Suggested ontology terms
- **GO Biological Process (examples):** epithelial cell proliferation (GO:0050673), regulation of cell cycle (GO:0051726), response to oxidative stress (GO:0006979), immune evasion (GO:0045087-related; general).
- **Cell types (CL examples):** epithelial cell (CL:0000066), squamous epithelial cell (CL:0000240), CD8-positive T cell (CL:0000625), macrophage (CL:0000235) (immune infiltration relevance supported conceptually by immunotherapy biology) (terazawa2025immunecheckpointinhibitors pages 2-4).
- **Anatomy (UBERON examples):** paranasal sinus (UBERON:0001825), maxillary sinus (UBERON:0001830), ethmoid sinus (UBERON:0001826), frontal sinus (UBERON:0001828), sphenoid sinus (UBERON:0001827), nasal cavity (UBERON:0001707) (subsite distribution supported in registries/reviews) (ferrari2021sinonasalsquamouscell pages 2-3, binazzi2024genderdifferencesin pages 5-7).

### 6) Anatomical structures affected
**Primary sites/subsites.** Across large SNSCC syntheses and registries, the dominant sites include **maxillary sinus**, **nasal cavity**, and **ethmoid sinus**. In a narrative review, main subsites were maxillary sinus (~60%), nasal cavity (25%), ethmoid complex (15%) (ferrari2021sinonasalsquamouscell pages 2-3). In ReNaTuNS, nasal cavity comprised ~50% in both sexes, with ethmoid more frequent in men and maxillary more frequent in women (binazzi2024genderdifferencesin pages 1-2).

### 7) Temporal development (onset and progression)
- **Typical age:** Registry and review evidence supports predominantly **older adult onset**; ReNaTuNS reports incidence rising with age and peaking in older age groups (binazzi2024genderdifferencesin pages 1-2). A review reports mean age ~65 (kacorzyk2025currentevidenceof pages 2-3).
- **Progression/presentation:** Diagnosis is often delayed due to nonspecific symptoms (kacorzyk2025currentevidenceof pages 1-2). Advanced stage at diagnosis is common in sinonasal cancers in general, contributing to high local recurrence risk (kacorzyk2025currentevidenceof pages 2-3).

### 8) Inheritance and population
No Mendelian inheritance pattern is expected for site-defined carcinomas like PNS-SCC; no germline causal genes were retrieved.

### 9) Epidemiology and demographics (recent registry data prioritized)
#### 9.1 Incidence and sex/age distribution (Italy; 2024)
Italian National Sinonasal Cancer Registry (ReNaTuNS) analysis (Binazzi et al., Cancers, 2024-05; URL https://doi.org/10.3390/cancers16112053) provides contemporary incidence estimates and sex differences:
- **Incidence rates:** **0.76 per 100,000 person-years in men** and **0.24 per 100,000 in women** (binazzi2024genderdifferencesin pages 1-2).
- **Case distribution:** 2,851 epithelial SNC patients; **73% men and 27% women** (binazzi2024genderdifferencesin pages 1-2).
- **Subsite-specific rates (per 100,000):** nasal cavity C30.0: 0.51 (men) vs 0.15 (women); maxillary C31.0: 0.16 vs 0.06; ethmoid C31.1: 0.18 vs 0.04 (binazzi2024genderdifferencesin pages 5-7, binazzi2024genderdifferencesin pages 3-5).
- **Occupational exposure prevalence differs by morphology:** for **SCC**, occupational exposure proportions were **44% in males** and **17% in females** (binazzi2024genderdifferencesin pages 5-7).

Abstract quote (Binazzi 2024): **“Occupational exposures to wood and leather dusts were the most frequent (41% for men, 33% for women).”** (binazzi2024genderdifferencesin pages 2-3).

#### 9.2 Incidence and morphology distribution (Brazil; 2024)
Brazilian nationwide Hospital Cancer Registry (Koller et al., La Medicina del Lavoro, 2024-02; URL https://doi.org/10.23749/mdl.v115i1.15066) identified **2,384** sinonasal cancer cases (2007–2021): **1,553 (65.1%) men** and **831 (34.9%) women**; mean age **59 years** (koller2024sinonasalcancercases pages 1-3). The maxillary sinus was the most frequent primary site (**~51–53%**), and SCC was the predominant morphology (**65.5% men; 54.5% women**) (koller2024sinonasalcancercases pages 1-3). Reported rates were low: crude incidence **1.0 per million person-years in men** and **0.5 per million in women**; age-standardized rates **1.0 (men) and 0.4 (women)** per million (koller2024sinonasalcancercases pages 1-3).

### 10) Diagnostics
#### 10.1 Clinical and imaging diagnostics
A clinician-facing synthesis notes CT and MRI are central for staging, with FDG-PET/CT used in staging assessment (kacorzyk2025currentevidenceof pages 2-3). Because sinonasal anatomy is complex, imaging is essential to evaluate skull base/orbit involvement, which also carries prognostic significance (p16 subgroup effects in Wang 2023 highlight orbital and skull base invasion as clinically meaningful stratifiers) (wang2023immunohistochemicalp16expression pages 1-2).

Suggested imaging-related ontology terms (not exhaustive):
- MAXO: radiologic imaging procedure; computed tomography; magnetic resonance imaging; positron emission tomography.

#### 10.2 Pathology and biomarkers
- Histopathologic diagnosis of SCC; keratinizing vs non-keratinizing forms are commonly used descriptors (ferrari2021sinonasalsquamouscell pages 2-3, kacorzyk2025currentevidenceof pages 1-2).
- Biomarkers used in practice/research include **p16 IHC** and **PD-L1 IHC (CPS)** (wang2023immunohistochemicalp16expression pages 1-2, terazawa2025immunecheckpointinhibitors pages 2-4).

### 11) Outcomes / prognosis
**Overall survival and recurrence patterns.** In clinician-focused synthesis, 5-year OS with curative intent is ~50%, local recurrence ~50% (median 8–16 months), regional recurrence 5–11%, distant metastases 2–10% (kacorzyk2025currentevidenceof pages 2-3). Ferrari et al. report conventional SNSCC 5-year disease-specific survival ~45% and strong survival stratification by nodal/distant disease status (ferrari2021sinonasalsquamouscell pages 2-3).

**Nodal/distant disease burden.** Regional node risk ~13% overall in one synthesis, with differences by subsite (maxillary sinus higher) (kacorzyk2025currentevidenceof pages 2-3). 

**HPV/p16 prognostic value (primary evidence).** p16 positivity was associated with improved 5-year OS in non–T4b disease and particularly in maxillary sinus tumors (Wang 2023) (wang2023immunohistochemicalp16expression pages 1-2).

**Immunotherapy outcomes (retrospective real-world series).** Terazawa et al. (Cancers, 2025-09; URL https://doi.org/10.3390/cancers17172872) analyzed 18 SNSCC patients treated with nivolumab or pembrolizumab (2017–2024): **ORR 43.8%**, **DCR 56.3%**, median **OS 21.5 months**, median **PFS 7.9 months**; pembrolizumab group had higher ORR/DCR than nivolumab (terazawa2025immunecheckpointinhibitors pages 1-2, terazawa2025immunecheckpointinhibitors pages 2-4).

Abstract quote (Terazawa 2025): **“The ORR and DCR for all patients were 43.8% and 56.3%, respectively.”** and **“Median OS and PFS were 21.5 and 7.9 months, respectively.”** (terazawa2025immunecheckpointinhibitors pages 1-2).

### 12) Treatment (current practice, real-world implementation, and recent developments)
#### 12.1 Standard local therapy (curative intent)
Standard-of-care is multimodal. In clinician-facing synthesis and narrative review, **surgery with negative margins followed by postoperative radiotherapy** is emphasized as the backbone when feasible; chemoradiotherapy is used when surgery is not feasible (kacorzyk2025currentevidenceof pages 2-3, kacorzyk2025currentevidenceof pages 1-2). IMRT is preferred; proton therapy is considered when photon constraints cannot be met (kacorzyk2025currentevidenceof pages 1-2).

**Induction chemotherapy**: Platinum-based induction is used in selected locally advanced cases; clinician synthesis reports partial response rates of **~35–57%** (kacorzyk2025currentevidenceof pages 2-3).

Suggested MAXO terms (examples): surgical resection; endoscopic surgery; radiotherapy; intensity-modulated radiotherapy; chemoradiotherapy; platinum-based chemotherapy.

#### 12.2 Systemic therapy and immunotherapy (latest developments prioritized)
**Checkpoint inhibitors for recurrent/metastatic disease.** Major head-and-neck immunotherapy trials excluded SNSCC, leading to reliance on retrospective cohorts and dedicated trials (terazawa2025immunecheckpointinhibitors pages 2-4, terazawa2025immunecheckpointinhibitors pages 1-2). Real-world retrospective outcomes in SNSCC are summarized above (Terazawa 2025) (terazawa2025immunecheckpointinhibitors pages 1-2).

**Prospective trial development specific to nasal cavity/paranasal sinus SCC.** Two key ClinicalTrials.gov trials directly enrolling nasal cavity/paranasal sinus SCC were retrieved:

1) **I-NAPA: pembrolizumab + induction chemotherapy before radiation**
- **NCT05027633** (ClinicalTrials.gov; sponsor: MD Anderson; first posted 2021; URL https://clinicaltrials.gov/study/NCT05027633)
- Design: single-arm phase II, open-label; **Stage II–IVb** nasal cavity/paranasal sinus SCC, treatment-naïve.
- Intervention: pembrolizumab + docetaxel + cisplatin/carboplatin induction, prior to radiation.
- Primary endpoint: ORR; target improvement **from 60% historical to 80%** with addition of immunotherapy (NCT05027633 chunk 1).

2) **Neoadjuvant cemiplimab + carboplatin/paclitaxel (randomized) with response-adapted definitive therapy**
- **NCT07281417** (ClinicalTrials.gov; sponsor: NCI; 2026; URL https://clinicaltrials.gov/study/NCT07281417)
- Design: randomized, open-label phase II; Stage III–IVB SNSCC.
- Arms: cemiplimab + carboplatin/paclitaxel vs carboplatin/paclitaxel alone; 2 cycles; definitive therapy (CRT vs surgery) adapted to response.
- Primary endpoint: event-free survival; secondary endpoints include ORR, OS, toxicity, organ preservation, ctDNA/omics correlatives, HPV and PD-L1 CPS correlation (NCT07281417 chunk 1, NCT07281417 chunk 2).

Suggested MAXO terms (examples): immune checkpoint inhibitor therapy; pembrolizumab therapy; nivolumab therapy; cemiplimab therapy; neoadjuvant therapy.

### 13) Prevention
**Primary prevention (occupational/public health).** ReNaTuNS emphasizes the surveillance value of registries and the importance of occupational history; occupational exposures are frequent and likely account for a large attributable fraction of sinonasal cancers (binazzi2024genderdifferencesin pages 1-2, binazzi2024genderdifferencesin pages 2-3). Preventive measures therefore center on:
- Engineering controls and exposure reduction for wood/leather dusts and other carcinogens.
- Smoking cessation programs (tobacco as recognized risk factor in reviews) (kacorzyk2025currentevidenceof pages 2-3).

**HPV prevention/secondary prevention.** Given HPV involvement in a subset and possible prognostic association, HPV testing and broader HPV prevention measures (including vaccination policies) may become more relevant, although this is not yet standardized in all practice settings (ferrari2021sinonasalsquamouscell pages 2-3, wang2023immunohistochemicalp16expression pages 1-2).

### 14) Other species / natural disease
No veterinary natural disease analogs or cross-species transmission evidence were retrieved.

### 15) Model organisms
No model organism, PDX, or cell-line resources specific to paranasal sinus SCC were retrieved in the current evidence set; this is a documented gap (objective 11) requiring targeted resource searches (e.g., Cellosaurus, PDX repositories).

---

## Key recent sources (prioritizing 2023–2024)
- **Binazzi et al.** *Gender Differences in Sinonasal Cancer Incidence: Data from the Italian Registry.* **Cancers**. **2024-05**. https://doi.org/10.3390/cancers16112053 (binazzi2024genderdifferencesin pages 1-2, binazzi2024genderdifferencesin pages 5-7)
- **Koller et al.** *Sinonasal Cancer Cases in a Nationwide Hospital Cancer Registry in Brazil, 2007–2021.* **La Medicina del Lavoro**. **2024-02**. https://doi.org/10.23749/mdl.v115i1.15066 (koller2024sinonasalcancercases pages 1-3)
- **Wang et al.** *Immunohistochemical p16 expression in the prognosis of patients with sinonasal squamous cell carcinoma.* **Neoplasma**. **2023-06**. https://doi.org/10.4149/neo_2023_230117n34 (wang2023immunohistochemicalp16expression pages 1-2)
- **Lucidi et al.** *Tumors of the Nose and Paranasal Sinuses: Promoting Factors and Molecular Mechanisms—A Systematic Review.* **Int J Mol Sci**. **2023-01**. https://doi.org/10.3390/ijms24032670 (limited extractable quantitative detail in retrieved pages) (lucidi2023tumorsofthe pages 17-18, lucidi2023tumorsofthe pages 18-20)

## Limitations of this evidence package
- MONDO/Orphanet/MeSH IDs were not directly retrievable from the current sources; this report flags these for external ontology lookup.
- Detailed symptom frequencies, comprehensive modern genomic alteration frequencies (2023–2024 primary multi-omics), and validated animal/model system resources were not present in the retrieved evidence set.


References

1. (kacorzyk2025currentevidenceof pages 1-2): Urszula Kacorzyk, Ewa Chmielik, and Tomasz Rutkowski. Current evidence of sinonasal carcinoma for clinical practitioners. part 1. Nowotwory. Journal of Oncology, 75:287-295, Oct 2025. URL: https://doi.org/10.5603/njo.106945, doi:10.5603/njo.106945. This article has 0 citations.

2. (ferrari2021sinonasalsquamouscell pages 2-3): Marco Ferrari, Stefano Taboni, Andrea Luigi Camillo Carobbio, Enzo Emanuelli, Roberto Maroldi, Paolo Bossi, and Piero Nicolai. Sinonasal squamous cell carcinoma, a narrative reappraisal of the current evidence. Cancers, 13:2835, Jun 2021. URL: https://doi.org/10.3390/cancers13112835, doi:10.3390/cancers13112835. This article has 84 citations.

3. (binazzi2024genderdifferencesin pages 2-3): Alessandra Binazzi, Davide di Marzio, Carolina Mensi, Dario Consonni, Lucia Miligi, Sara Piro, Jana Zajacovà, Denise Sorasio, Paolo Galli, Angela Camagni, Roberto Calisti, Stefania Massacesi, Ilaria Cozzi, Anna Balestri, Stefano Murano, Ugo Fedeli, Vera Comiati, Silvia Eccher, Sara Lattanzio, and Alessandro Marinaccio. Gender differences in sinonasal cancer incidence: data from the italian registry. Cancers, 16:2053, May 2024. URL: https://doi.org/10.3390/cancers16112053, doi:10.3390/cancers16112053. This article has 9 citations.

4. (binazzi2024genderdifferencesin pages 5-7): Alessandra Binazzi, Davide di Marzio, Carolina Mensi, Dario Consonni, Lucia Miligi, Sara Piro, Jana Zajacovà, Denise Sorasio, Paolo Galli, Angela Camagni, Roberto Calisti, Stefania Massacesi, Ilaria Cozzi, Anna Balestri, Stefano Murano, Ugo Fedeli, Vera Comiati, Silvia Eccher, Sara Lattanzio, and Alessandro Marinaccio. Gender differences in sinonasal cancer incidence: data from the italian registry. Cancers, 16:2053, May 2024. URL: https://doi.org/10.3390/cancers16112053, doi:10.3390/cancers16112053. This article has 9 citations.

5. (koller2024sinonasalcancercases pages 1-3): Francisco Koller, Dario Consonni, Carolina Mensi, Luciana de Alcantara Nogueira, Cristiano de Oliveira Ribeiro, Paulo Ricardo Bittencourt Guimarães, and Luciana Puchalski Kalinke. Sinonasal cancer cases in a nationwide hospital cancer registry in brazil, 2007-2021. La Medicina del Lavoro, 115:e2024004, Feb 2024. URL: https://doi.org/10.23749/mdl.v115i1.15066, doi:10.23749/mdl.v115i1.15066. This article has 3 citations.

6. (binazzi2024genderdifferencesin pages 3-5): Alessandra Binazzi, Davide di Marzio, Carolina Mensi, Dario Consonni, Lucia Miligi, Sara Piro, Jana Zajacovà, Denise Sorasio, Paolo Galli, Angela Camagni, Roberto Calisti, Stefania Massacesi, Ilaria Cozzi, Anna Balestri, Stefano Murano, Ugo Fedeli, Vera Comiati, Silvia Eccher, Sara Lattanzio, and Alessandro Marinaccio. Gender differences in sinonasal cancer incidence: data from the italian registry. Cancers, 16:2053, May 2024. URL: https://doi.org/10.3390/cancers16112053, doi:10.3390/cancers16112053. This article has 9 citations.

7. (binazzi2024genderdifferencesin pages 1-2): Alessandra Binazzi, Davide di Marzio, Carolina Mensi, Dario Consonni, Lucia Miligi, Sara Piro, Jana Zajacovà, Denise Sorasio, Paolo Galli, Angela Camagni, Roberto Calisti, Stefania Massacesi, Ilaria Cozzi, Anna Balestri, Stefano Murano, Ugo Fedeli, Vera Comiati, Silvia Eccher, Sara Lattanzio, and Alessandro Marinaccio. Gender differences in sinonasal cancer incidence: data from the italian registry. Cancers, 16:2053, May 2024. URL: https://doi.org/10.3390/cancers16112053, doi:10.3390/cancers16112053. This article has 9 citations.

8. (kacorzyk2025currentevidenceof pages 2-3): Urszula Kacorzyk, Ewa Chmielik, and Tomasz Rutkowski. Current evidence of sinonasal carcinoma for clinical practitioners. part 1. Nowotwory. Journal of Oncology, 75:287-295, Oct 2025. URL: https://doi.org/10.5603/njo.106945, doi:10.5603/njo.106945. This article has 0 citations.

9. (wang2023immunohistochemicalp16expression pages 1-2): Li Wang, Hua-Tao Quan, Jie Wang, Tian-Ci Tang, Yi Li, and Xin-Mao Song. Immunohistochemical p16 expression in the prognosis of patients with sinonasal squamous cell carcinoma. Neoplasma, 70 3:451-457, Jun 2023. URL: https://doi.org/10.4149/neo\_2023\_230117n34, doi:10.4149/neo\_2023\_230117n34. This article has 3 citations and is from a peer-reviewed journal.

10. (wang2023immunohistochemicalp16expression pages 6-7): Li Wang, Hua-Tao Quan, Jie Wang, Tian-Ci Tang, Yi Li, and Xin-Mao Song. Immunohistochemical p16 expression in the prognosis of patients with sinonasal squamous cell carcinoma. Neoplasma, 70 3:451-457, Jun 2023. URL: https://doi.org/10.4149/neo\_2023\_230117n34, doi:10.4149/neo\_2023\_230117n34. This article has 3 citations and is from a peer-reviewed journal.

11. (terazawa2025immunecheckpointinhibitors pages 2-4): Kosuke Terazawa, Masashi Kuroki, Ken Saijo, Tatsuhiko Yamada, Ryota Iinuma, Ryo Kawaura, Hiroshi Okuda, Kenichi Mori, Hirofumi Shibata, Ryo Utakata, Miki Umeda, and Takenori Ogawa. Immune checkpoint inhibitors in sinonasal squamous cell carcinoma: a retrospective study and literature review. Cancers, 17:2872, Sep 2025. URL: https://doi.org/10.3390/cancers17172872, doi:10.3390/cancers17172872. This article has 2 citations.

12. (terazawa2025immunecheckpointinhibitors pages 1-2): Kosuke Terazawa, Masashi Kuroki, Ken Saijo, Tatsuhiko Yamada, Ryota Iinuma, Ryo Kawaura, Hiroshi Okuda, Kenichi Mori, Hirofumi Shibata, Ryo Utakata, Miki Umeda, and Takenori Ogawa. Immune checkpoint inhibitors in sinonasal squamous cell carcinoma: a retrospective study and literature review. Cancers, 17:2872, Sep 2025. URL: https://doi.org/10.3390/cancers17172872, doi:10.3390/cancers17172872. This article has 2 citations.

13. (NCT05027633 chunk 1):  Immunotherapy With Chemotherapy and Chemoradiation for Advanced Squamous Cancer of Nasal Cavity / Paranasal Sinuses (I-NAPA). M.D. Anderson Cancer Center. 2021. ClinicalTrials.gov Identifier: NCT05027633

14. (NCT07281417 chunk 1):  Testing the Addition of Cemiplimab (REGN2810) to Chemotherapy Treatment Given Prior to Surgery in Patients With Sinonasal Squamous Cell Carcinoma. National Cancer Institute (NCI). 2026. ClinicalTrials.gov Identifier: NCT07281417

15. (NCT07281417 chunk 2):  Testing the Addition of Cemiplimab (REGN2810) to Chemotherapy Treatment Given Prior to Surgery in Patients With Sinonasal Squamous Cell Carcinoma. National Cancer Institute (NCI). 2026. ClinicalTrials.gov Identifier: NCT07281417

16. (lucidi2023tumorsofthe pages 17-18): Daniela Lucidi, Carla Cantaffa, Matteo Miglio, Federica Spina, Matteo Alicandri Ciufelli, Alessandro Marchioni, and Daniele Marchioni. Tumors of the nose and paranasal sinuses: promoting factors and molecular mechanisms—a systematic review. International Journal of Molecular Sciences, 24:2670, Jan 2023. URL: https://doi.org/10.3390/ijms24032670, doi:10.3390/ijms24032670. This article has 18 citations.

17. (lucidi2023tumorsofthe pages 18-20): Daniela Lucidi, Carla Cantaffa, Matteo Miglio, Federica Spina, Matteo Alicandri Ciufelli, Alessandro Marchioni, and Daniele Marchioni. Tumors of the nose and paranasal sinuses: promoting factors and molecular mechanisms—a systematic review. International Journal of Molecular Sciences, 24:2670, Jan 2023. URL: https://doi.org/10.3390/ijms24032670, doi:10.3390/ijms24032670. This article has 18 citations.

## Artifacts

- [Edison artifact artifact-00](Paranasal_Sinus_Squamous_Cell_Carcinoma-deep-research-falcon_artifacts/artifact-00.md)