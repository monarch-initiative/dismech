---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-22T11:40:53.006447'
end_time: '2026-06-22T11:54:40.720638'
duration_seconds: 827.71
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Transitional Cell Carcinoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: Transitional_Cell_Carcinoma-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Transitional_Cell_Carcinoma-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: Transitional_Cell_Carcinoma-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Transitional Cell Carcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Transitional Cell Carcinoma** covering all of the
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
- **Disease Name:** Transitional Cell Carcinoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Transitional Cell Carcinoma** covering all of the
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


# Comprehensive Research Report: Transitional Cell Carcinoma (Urothelial Carcinoma)

## Executive Summary

Transitional cell carcinoma, now termed **urothelial carcinoma (UC)**, represents the predominant histological subtype of bladder cancer, accounting for 90-95% of all bladder malignancies (alouini2024riskfactorsassociated pages 1-2, kwon2025advancesintherapy pages 1-2, peng2023targetedtherapiesin pages 1-2). This comprehensive report synthesizes current understanding from recent 2023-2024 literature, covering disease characteristics, molecular pathogenesis, epidemiology, diagnosis, treatment, and research models.

---

## 1. DISEASE INFORMATION

### Overview and Nomenclature

Transitional cell carcinoma is now officially designated as **urothelial carcinoma** following World Health Organization (WHO) nomenclature updates, with the term "transitional cell carcinoma" considered superseded but still acceptable (alouini2024riskfactorsassociated pages 1-2, kolawa2023overviewdiagnosisand pages 1-2). Urothelial carcinoma originates from urothelial cells lining the urinary tract and represents the most common histological form of bladder cancer (dyrskjøt2023bladdercancer pages 1-3).

### Disease Classification

The 2022 WHO Classification of Urinary and Male Genital Tumors delineates multiple histological subtypes beyond conventional UC, including squamous cell carcinoma, small-cell carcinoma, sarcomatoid urothelial carcinoma, micropapillary carcinoma, plasmacytoid carcinoma, urachal carcinoma, and adenocarcinoma (kwon2025advancesintherapy pages 1-2). UC is categorized anatomically into bladder (90-95% of urothelial cancers) and upper tract urothelial carcinoma (UTUC, 5-10%), which includes renal pelvis and ureter malignancies (kolawa2023overviewdiagnosisand pages 1-2, pandolfo2024uppertracturothelial pages 1-2).

Clinically, UC is stratified into:
- **Non-muscle-invasive bladder cancer (NMIBC):** Stages Tis, Ta, and T1, representing ~70-75% of new diagnoses (dyrskjøt2023bladdercancer pages 1-3, lopezbeltran2024advancesindiagnosis pages 1-1)
- **Muscle-invasive bladder cancer (MIBC):** Stages T2-T4, representing ~25-30% of new diagnoses (dyrskjøt2023bladdercancer pages 1-3, peng2023targetedtherapiesin pages 1-2, lopezbeltran2024advancesindiagnosis pages 1-1)

### Molecular Classification

Recent mRNA expression profiling has identified biologically relevant molecular subtypes with distinct prognoses and treatment responses (schwarzova2023molecularclassificationof pages 1-2). The consensus classification includes:
- **Luminal subtypes:** Luminal-papillary (LumP), luminal non-specified, luminal-unstable, and genomically unstable (GU) subtypes, often expressing uroplakins, GATA3, and PPARγ with frequent FGFR3 mutations (schwarzova2023molecularclassificationof pages 1-2, su2025reviewofrecent pages 1-3)
- **Basal/squamous subtypes (Ba/Sq):** Expressing basal markers (KRT5/6, KRT14, EGFR) with aggressive behavior (schwarzova2023molecularclassificationof pages 1-2, su2025reviewofrecent pages 1-3)
- **Neuroendocrine-like (Sc/Ne):** Rare, highly malignant subtype expressing neuroendocrine markers with TP53 and RB1 mutations (su2025reviewofrecent pages 1-3)
- **Mesenchymal-like (mes-like)** and **infiltrated** subtypes (schwarzova2023molecularclassificationof pages 1-2, su2025reviewofrecent pages 1-3)

### Key Identifiers

While specific disease database identifiers (OMIM, Orphanet, MONDO) were not provided in the retrieved 2023-2024 literature, ICD coding and MeSH classifications are used clinically. The data derive from both population-level registries (GLOBOCAN, SEER) and individual patient records (electronic health records, clinical trials) (alouini2024riskfactorsassociated pages 1-2, hoogstraten2023globaltrendsin pages 1-2).

---

## 2. ETIOLOGY

### Disease Causal Factors

Urothelial carcinoma is a multifactorial disease with both genetic and environmental contributors (dyrskjøt2023bladdercancer pages 1-3, hoogstraten2023globaltrendsin pages 1-2).

**Genetic Factors:**
UC exhibits one of the highest somatic mutational burdens among cancers, with mean rates of 7.7 mutations per megabase, surpassed only by lung carcinoma and melanoma (alahmadie2024molecularpathologyof pages 1-3). The APOBEC mutagenesis signature accounts for ~66% of single nucleotide variants (SNVs) in MIBC, reflecting innate immunity-mediated cytidine deaminase activity (alahmadie2024molecularpathologyof pages 1-3).

**Environmental and Mechanistic Factors:**
The urothelium's exposure to carcinogenic metabolites eliminated via urine makes it vulnerable to environmental carcinogens (dyrskjøt2023bladdercancer pages 1-3).

### Risk Factors

**Genetic Risk Factors:**
- Germline pathogenic/likely pathogenic variants in DNA damage response (DDR) genes identified in ~11% of UC patients, with BRCA1 and CHEK2 being most prevalent (1.20% each) (alahmadie2024molecularpathologyof pages 1-3)
- Lynch syndrome association with UTUC (kolawa2023overviewdiagnosisand pages 1-2)
- Somatic alterations in TP53, FGFR3, TERT promoter, PIK3CA, RB1, STAG2, and chromatin modifiers contribute to pathogenesis (su2025reviewofrecent pages 1-3, alahmadie2024molecularpathologyof pages 1-3)

See artifact table for detailed molecular alteration frequencies and associations.

| Gene | Approx. alteration frequency in UC | Predominant alteration type(s) | Functional consequence | Key pathway / process | NMIBC vs MIBC correlation | Prognostic / biologic association | Therapeutic implications | Evidence |
|---|---:|---|---|---|---|---|---|---|
| **FGFR3** | ~70% of NMIBC; ~15% of MIBC; ~39% of non-muscle-invasive specimens and ~14% of muscle-invasive specimens in one real-world series | Activating hotspot mutations, fusions, overexpression | Gain-of-function; ligand-independent receptor activation, increased proliferation/survival | FGFR/RTK-RAS-MAPK; PI3K-AKT | Strongly enriched in NMIBC and luminal-papillary/luminal-like disease; less common in aggressive MIBC | Often linked to papillary, luminal differentiation and relatively better prognosis than TP53-driven disease, but resistance and heterogeneity occur in advanced disease | FDA-approved FGFR inhibitor **erdafitinib** for susceptible FGFR2/3-altered metastatic UC; resistance via second-site FGFR3 mutations and PI3K-mTOR pathway changes | (dyrskjøt2023bladdercancer pages 1-3, su2025reviewofrecent pages 1-3, alahmadie2024molecularpathologyof pages 1-3, peng2023targetedtherapiesin pages 1-2) |
| **TP53** | ~50% of MIBC; nearly half of MIBC in molecular pathology review | Missense/truncating mutations, pathway inactivation; often mutually exclusive with MDM2 amplification and relatively exclusive vs FGFR3 programs | Loss of tumor suppressor function; impaired DNA-damage response, apoptosis, cell-cycle arrest | p53 pathway / cell-cycle checkpoint | Enriched in MIBC, basal/squamous and neuroendocrine-like aggressive disease; less typical of low-grade papillary NMIBC | Associated with genomic instability, invasion, poorer survival, and aggressive phenotypes | Not directly targetable in routine care; may inform risk stratification and subtype biology; abnormal p53 expression may predict response patterns to enfortumab vedotin in exploratory studies | (dyrskjøt2023bladdercancer pages 1-3, su2025reviewofrecent pages 1-3, alahmadie2024molecularpathologyof pages 1-3) |
| **TERT promoter / TERT** | Common / among most frequent early alterations in UC; exact % not provided in available contexts | Promoter mutations, increased expression | Telomerase activation and replicative immortality | Telomere maintenance | Occurs across stages, including early urothelial tumorigenesis | Associated with tumor development; higher expression has been linked to poor prognosis in review literature | Potential urine-based molecular biomarker and disease-monitoring target; no standard direct targeted therapy | (dyrskjøt2023bladdercancer pages 1-3, su2025reviewofrecent pages 1-3) |
| **PIK3CA** | Common recurrent alteration; listed among commonly mutated genes in UC; 45% in one 2025 cohort (external to 2023-24 evidence but consistent with review framing) | Activating hotspot mutations | PI3K pathway activation, enhanced proliferation/survival | PI3K-AKT-mTOR | Seen across UC; co-occurs with FGFR3-rich luminal/NMIBC programs in some genomic landscapes | Supports tumor growth and may contribute to targeted-therapy resistance | Suggests rationale for PI3K/AKT/mTOR-targeted combinations; implicated in resistance to FGFR inhibition | (dyrskjøt2023bladdercancer pages 1-3, alahmadie2024molecularpathologyof pages 1-3, peng2023targetedtherapiesin pages 1-2) |
| **RB1** | Recurrent in MIBC; frequency not quantified in available contexts | Inactivating mutation/deletion | Loss of G1/S checkpoint control | RB / cell-cycle control | More characteristic of aggressive, muscle-invasive and neuroendocrine-like disease | Associated with high-grade biology and progression | Primarily prognostic/biologic marker; may support intensified systemic treatment strategies and subtype classification | (dyrskjøt2023bladdercancer pages 1-3, su2025reviewofrecent pages 1-3, alahmadie2024molecularpathologyof pages 1-3) |
| **STAG2** | Frequently mutated in NMIBC; exact % not provided in available 2023-24 contexts | Inactivating mutations | Cohesin dysfunction, altered chromatid segregation and genomic regulation | Cohesin / chromosome segregation | Especially noted in NMIBC | Marker of early urothelial tumorigenesis and molecular heterogeneity | Potential biomarker for classification and surveillance; no established direct therapy | (dyrskjøt2023bladdercancer pages 1-3, peng2023targetedtherapiesin pages 1-2) |
| **CDKN2A** | Recurrent deletion/alteration in UC | Deletion, loss-of-function | Loss of p16-mediated cell-cycle inhibition | CDK4/6-RB axis | Seen in both NMIBC and MIBC; part of chromosome 9 loss events in urothelial tumorigenesis | Contributes to unchecked proliferation and progression | Theoretic rationale for CDK4/6-directed strategies; not yet routine biomarker-guided standard in UC | (alahmadie2024molecularpathologyof pages 1-3, peng2023targetedtherapiesin pages 1-2) |
| **ERCC2** | Recurrent subset in MIBC; ~20% of SNVs tied to ERCC2-associated mutational signature in one review summary | Missense mutations affecting NER helicase function | Defective nucleotide excision repair, increased mutagenesis | DNA damage response / repair (DDR) | More emphasized in MIBC and treatment-response studies | Associated with tobacco-linked mutational processes and better response to cisplatin-based chemotherapy in DDR-altered tumors | Predictive biomarker candidate for cisplatin sensitivity; also linked to response to radiation and immune checkpoint blockade in DDR-altered UC | (alahmadie2024molecularpathologyof pages 1-3) |
| **MDM2** | ~7% amplification in MIBC | Amplification | p53 pathway suppression | p53 negative regulation | More relevant in MIBC; generally mutually exclusive with TP53 mutation | Supports aggressive biology through p53 functional silencing | Investigational biomarker; theoretical MDM2-targeting relevance but not standard in UC | (alahmadie2024molecularpathologyof pages 1-3) |
| **KDM6A / chromatin-modifier genes** | Commonly altered class in UC; exact % not provided in available contexts | Loss-of-function mutations | Epigenetic dysregulation, altered differentiation programs | Chromatin modification / transcriptional control | Present across UC; part of urothelial molecular heterogeneity | May shape subtype identity and progression risk | Supports epigenetic-therapy research and molecular classification, but no routine targeted use | (dyrskjøt2023bladdercancer pages 1-3, alahmadie2024molecularpathologyof pages 1-3) |
| **KMT2D / KMT2C / KMT2A** | Recurrently altered; distinct prevalence reported between UTUC and bladder UC | Mutations, likely loss/dysregulation | Chromatin remodeling defects and transcriptional dysregulation | Histone modification / chromatin regulation | Contribute to biologic differences between UTUC and bladder UC | May underlie site-specific pathogenesis and heterogeneity | Potential stratification biomarkers in genomic profiling; investigational therapeutic relevance | (schwarzova2023molecularclassificationof pages 1-2, alahmadie2024molecularpathologyof pages 1-3) |
| **HRAS** | Recurrent but less common than FGFR3/TP53 | Activating mutations | MAPK pathway activation | RAS-MAPK | More often associated with non–muscle-invasive pathways in classic urothelial models | Supports proliferative signaling | Primarily biologic marker; potential eligibility for future RAS-pathway strategies | (su2025reviewofrecent pages 1-3, peng2023targetedtherapiesin pages 1-2) |
| **ERBB2 (HER2)** | Overexpression / activation in subset; exact % not given in available contexts | Amplification/overexpression, mutation in subset | Enhanced proliferation, invasion, metastasis signaling | ERBB/HER2 RTK signaling | More often discussed in advanced/aggressive disease workups | Linked to invasion and metastasis in review literature | Candidate biomarker for HER2-directed therapy trials and precision oncology approaches | (su2025reviewofrecent pages 1-3, lopezbeltran2024advancesindiagnosis pages 1-1) |
| **PTEN** | Recurrent but less common than TP53/FGFR3 | Loss-of-function mutation/deletion | Reduced negative regulation of PI3K signaling | PI3K-AKT-mTOR | More relevant in invasive/aggressive molecular programs | May contribute to progression and therapy resistance | Supports rationale for PI3K/AKT/mTOR combination strategies | (su2025reviewofrecent pages 1-3, peng2023targetedtherapiesin pages 1-2) |
| **DDR gene group (e.g., BRCA1, CHEK2, PMS2 and related genes)** | Pathogenic germline variants found in ~11.24% of one Chinese UC cohort; deleterious DDR alterations in ~22.9% UTUC and ~33.9% UCB | Germline or somatic pathogenic variants | Impaired homologous recombination / checkpoint repair | DNA damage response / repair | Present in both UTUC and bladder UC, with prevalence differences by site | May raise mutational burden and treatment sensitivity | Potential relevance to platinum response, immunotherapy response, and future PARP-based strategies; also germline counseling implications | (alahmadie2024molecularpathologyof pages 1-3) |
| **APOBEC mutational process** | Not a gene alteration but dominant mutational signature; accounted for ~66% of SNVs in TCGA MIBC per review summary | Cytidine deaminase mutational signature | Hypermutation and genomic diversification | Mutagenesis / innate immunity-related editing | Strongly emphasized in MIBC | Associated in review summary with improved 5-year overall survival in MIBC despite high mutation burden | Relevant to biomarker development, immunogenicity, and molecular taxonomy rather than direct targeting | (alahmadie2024molecularpathologyof pages 1-3) |


*Table: This table summarizes recurrent molecular alterations in transitional cell carcinoma/urothelial carcinoma, emphasizing stage associations, pathway biology, prognostic patterns, and current or emerging therapeutic relevance. It is useful for linking disease mechanisms to precision oncology and biomarker-driven management.*

**Environmental Risk Factors:**
- **Tobacco smoking:** The primary risk factor, implicated in ~50% of bladder cancer diagnoses; UTUC incidence is 2-3 times greater in tobacco users, accounting for ~50% of male and 33% of female cases (dyrskjøt2023bladdercancer pages 1-3, kolawa2023overviewdiagnosisand pages 1-2, hoogstraten2023globaltrendsin pages 1-2)
- **Occupational exposures:** Aromatic amines in dye, paint, petroleum, and metal industries account for ~20% of UBC cases (alouini2024riskfactorsassociated pages 1-2)
- **Chemical carcinogens:** Polycyclic aromatic hydrocarbons (PAHs), 4-aminobiphenyl (alouini2024riskfactorsassociated pages 1-2)
- **Aristolochic acid exposure:** Established risk factor particularly relevant in endemic regions (kolawa2023overviewdiagnosisand pages 1-2, pandolfo2024uppertracturothelial pages 1-2)
- **Chlorinated water:** Trihalomethanes in drinking water and swimming pools increase bladder cancer risk (alouini2024riskfactorsassociated pages 1-2)
- **Air pollution:** Volatile organic compounds (VOCs), PAHs, and particulate matter <2.5μm linked to UBC (alouini2024riskfactorsassociated pages 1-2)
- **Radiation:** Pelvic radiation therapy increases UTUC risk (kolawa2023overviewdiagnosisand pages 1-2)

**Medical and Lifestyle Factors:**
- Chemotherapeutic agents, oral hypoglycemic drugs, and chronic bladder irritation (alouini2024riskfactorsassociated pages 1-2)
- Alcohol consumption, processed meat, and whole milk; higher intakes of selenium and vitamins A and E (alouini2024riskfactorsassociated pages 1-2)
- Age (median diagnosis at 70 years), male sex (3.3:1 male:female ratio) (alouini2024riskfactorsassociated pages 1-2, hoogstraten2023globaltrendsin pages 1-2)

### Protective Factors

Literature on protective factors is limited in the retrieved 2023-2024 sources. Smoking cessation represents a primary prevention strategy, with implications for reducing incidence (hoogstraten2023globaltrendsin pages 1-2). Studies investigating lifestyle factors (diet, exercise) and bladder cancer outcomes are identified as a research priority (hoogstraten2023globaltrendsin pages 1-2).

### Gene-Environment Interactions

The ERCC2 mutational signature accounts for ~20% of SNVs in MIBC and is associated with smoking exposure independent of ERCC2 mutation status, demonstrating gene-environment interactions in mutagenesis (alahmadie2024molecularpathologyof pages 1-3). The interplay between APOBEC-mediated mutagenesis and environmental carcinogen exposure contributes to UC's high mutational burden (alahmadie2024molecularpathologyof pages 1-3).

---

## 3. PHENOTYPES

### Clinical Presentations

**Symptoms:**
- **Hematuria:** Most common presentation (~80% of UTUC cases); frequently gross and painless (pandolfo2024uppertracturothelial pages 1-2, lopezbeltran2024advancesindiagnosis pages 1-1)
- **Flank pain:** Present in ~20% of UTUC cases (pandolfo2024uppertracturothelial pages 1-2)
- **Constitutional symptoms:** Weight loss, fever, night sweats, anorexia in advanced/metastatic disease (pandolfo2024uppertracturothelial pages 1-2)
- **Bladder irritative symptoms:** Urgency, frequency in some NMIBC cases

**Phenotype Characteristics:**
- **Age of onset:** Median 70 years; predominantly adult-onset disease (alouini2024riskfactorsassociated pages 1-2)
- **Severity:** Variable from low-grade papillary (indolent) to high-grade invasive (aggressive) (lopezbeltran2024advancesindiagnosis pages 1-1)
- **Progression:** NMIBC shows 31-78% recurrence and 1-45% progression at 5 years; MIBC and UTUC follow more aggressive courses (lopezbeltran2024advancesindiagnosis pages 1-1)
- **Frequency:** Gross hematuria precedes diagnosis in majority; constitutional symptoms indicate metastasis (pandolfo2024uppertracturothelial pages 1-2, lopezbeltran2024advancesindiagnosis pages 1-1)

### HPO Term Suggestions

- HP:0000790 - Hematuria
- HP:0000083 - Renal insufficiency (in UTUC with obstruction)
- HP:0030078 - Lung adenocarcinoma (for metastatic sites)
- HP:0012531 - Pain
- HP:0001824 - Weight loss
- HP:0001945 - Fever
- HP:0030731 - Carcinoma

### Quality of Life Impact

Bladder cancer imposes substantial impacts on patient quality of life, morbidity, mortality, and healthcare costs (lopezbeltran2024advancesindiagnosis pages 1-1). NMIBC requires frequent cystoscopic surveillance, causing anxiety and procedural burden. MIBC necessitates radical cystectomy with urinary diversion, significantly affecting daily functioning, body image, and sexual function. Metastatic disease is associated with poor prognosis and palliative care needs (kwon2025advancesintherapy pages 1-2, lopezbeltran2024advancesindiagnosis pages 1-1).

---

## 4. GENETIC/MOLECULAR INFORMATION

### Causal Genes and Pathogenic Variants

Detailed molecular alterations are summarized in the artifact table below. Key genes include:

**Most Frequently Altered Genes:**
- **TP53:** Mutated in ~50% of MIBC; loss of tumor suppressor function, mutually exclusive with MDM2 amplification (~7%) (su2025reviewofrecent pages 1-3, alahmadie2024molecularpathologyof pages 1-3)
- **FGFR3:** Activating mutations in ~70% of NMIBC and ~15% of MIBC; gain-of-function driving luminal-papillary subtypes (su2025reviewofrecent pages 1-3, alahmadie2024molecularpathologyof pages 1-3)
- **TERT promoter:** Among most frequent early alterations; telomerase activation (su2025reviewofrecent pages 1-3)
- **PIK3CA:** Activating mutations common (~45% in one cohort); PI3K-AKT-mTOR pathway activation (alahmadie2024molecularpathologyof pages 1-3)
- **RB1:** Inactivating mutations/deletions in MIBC; loss of G1/S checkpoint control (su2025reviewofrecent pages 1-3, alahmadie2024molecularpathologyof pages 1-3)
- **STAG2:** Frequently mutated in NMIBC; cohesin dysfunction (alahmadie2024molecularpathologyof pages 1-3, peng2023targetedtherapiesin pages 1-2)
- **CDKN2A:** Recurrent deletion; loss of p16-mediated cell cycle inhibition (alahmadie2024molecularpathologyof pages 1-3, peng2023targetedtherapiesin pages 1-2)
- **ERCC2:** Mutations affecting DNA nucleotide excision repair; associated with cisplatin sensitivity (alahmadie2024molecularpathologyof pages 1-3)

| Gene | Approx. alteration frequency in UC | Predominant alteration type(s) | Functional consequence | Key pathway / process | NMIBC vs MIBC correlation | Prognostic / biologic association | Therapeutic implications | Evidence |
|---|---:|---|---|---|---|---|---|---|
| **FGFR3** | ~70% of NMIBC; ~15% of MIBC; ~39% of non-muscle-invasive specimens and ~14% of muscle-invasive specimens in one real-world series | Activating hotspot mutations, fusions, overexpression | Gain-of-function; ligand-independent receptor activation, increased proliferation/survival | FGFR/RTK-RAS-MAPK; PI3K-AKT | Strongly enriched in NMIBC and luminal-papillary/luminal-like disease; less common in aggressive MIBC | Often linked to papillary, luminal differentiation and relatively better prognosis than TP53-driven disease, but resistance and heterogeneity occur in advanced disease | FDA-approved FGFR inhibitor **erdafitinib** for susceptible FGFR2/3-altered metastatic UC; resistance via second-site FGFR3 mutations and PI3K-mTOR pathway changes | (dyrskjøt2023bladdercancer pages 1-3, su2025reviewofrecent pages 1-3, alahmadie2024molecularpathologyof pages 1-3, peng2023targetedtherapiesin pages 1-2) |
| **TP53** | ~50% of MIBC; nearly half of MIBC in molecular pathology review | Missense/truncating mutations, pathway inactivation; often mutually exclusive with MDM2 amplification and relatively exclusive vs FGFR3 programs | Loss of tumor suppressor function; impaired DNA-damage response, apoptosis, cell-cycle arrest | p53 pathway / cell-cycle checkpoint | Enriched in MIBC, basal/squamous and neuroendocrine-like aggressive disease; less typical of low-grade papillary NMIBC | Associated with genomic instability, invasion, poorer survival, and aggressive phenotypes | Not directly targetable in routine care; may inform risk stratification and subtype biology; abnormal p53 expression may predict response patterns to enfortumab vedotin in exploratory studies | (dyrskjøt2023bladdercancer pages 1-3, su2025reviewofrecent pages 1-3, alahmadie2024molecularpathologyof pages 1-3) |
| **TERT promoter / TERT** | Common / among most frequent early alterations in UC; exact % not provided in available contexts | Promoter mutations, increased expression | Telomerase activation and replicative immortality | Telomere maintenance | Occurs across stages, including early urothelial tumorigenesis | Associated with tumor development; higher expression has been linked to poor prognosis in review literature | Potential urine-based molecular biomarker and disease-monitoring target; no standard direct targeted therapy | (dyrskjøt2023bladdercancer pages 1-3, su2025reviewofrecent pages 1-3) |
| **PIK3CA** | Common recurrent alteration; listed among commonly mutated genes in UC; 45% in one 2025 cohort (external to 2023-24 evidence but consistent with review framing) | Activating hotspot mutations | PI3K pathway activation, enhanced proliferation/survival | PI3K-AKT-mTOR | Seen across UC; co-occurs with FGFR3-rich luminal/NMIBC programs in some genomic landscapes | Supports tumor growth and may contribute to targeted-therapy resistance | Suggests rationale for PI3K/AKT/mTOR-targeted combinations; implicated in resistance to FGFR inhibition | (dyrskjøt2023bladdercancer pages 1-3, alahmadie2024molecularpathologyof pages 1-3, peng2023targetedtherapiesin pages 1-2) |
| **RB1** | Recurrent in MIBC; frequency not quantified in available contexts | Inactivating mutation/deletion | Loss of G1/S checkpoint control | RB / cell-cycle control | More characteristic of aggressive, muscle-invasive and neuroendocrine-like disease | Associated with high-grade biology and progression | Primarily prognostic/biologic marker; may support intensified systemic treatment strategies and subtype classification | (dyrskjøt2023bladdercancer pages 1-3, su2025reviewofrecent pages 1-3, alahmadie2024molecularpathologyof pages 1-3) |
| **STAG2** | Frequently mutated in NMIBC; exact % not provided in available 2023-24 contexts | Inactivating mutations | Cohesin dysfunction, altered chromatid segregation and genomic regulation | Cohesin / chromosome segregation | Especially noted in NMIBC | Marker of early urothelial tumorigenesis and molecular heterogeneity | Potential biomarker for classification and surveillance; no established direct therapy | (dyrskjøt2023bladdercancer pages 1-3, peng2023targetedtherapiesin pages 1-2) |
| **CDKN2A** | Recurrent deletion/alteration in UC | Deletion, loss-of-function | Loss of p16-mediated cell-cycle inhibition | CDK4/6-RB axis | Seen in both NMIBC and MIBC; part of chromosome 9 loss events in urothelial tumorigenesis | Contributes to unchecked proliferation and progression | Theoretic rationale for CDK4/6-directed strategies; not yet routine biomarker-guided standard in UC | (alahmadie2024molecularpathologyof pages 1-3, peng2023targetedtherapiesin pages 1-2) |
| **ERCC2** | Recurrent subset in MIBC; ~20% of SNVs tied to ERCC2-associated mutational signature in one review summary | Missense mutations affecting NER helicase function | Defective nucleotide excision repair, increased mutagenesis | DNA damage response / repair (DDR) | More emphasized in MIBC and treatment-response studies | Associated with tobacco-linked mutational processes and better response to cisplatin-based chemotherapy in DDR-altered tumors | Predictive biomarker candidate for cisplatin sensitivity; also linked to response to radiation and immune checkpoint blockade in DDR-altered UC | (alahmadie2024molecularpathologyof pages 1-3) |
| **MDM2** | ~7% amplification in MIBC | Amplification | p53 pathway suppression | p53 negative regulation | More relevant in MIBC; generally mutually exclusive with TP53 mutation | Supports aggressive biology through p53 functional silencing | Investigational biomarker; theoretical MDM2-targeting relevance but not standard in UC | (alahmadie2024molecularpathologyof pages 1-3) |
| **KDM6A / chromatin-modifier genes** | Commonly altered class in UC; exact % not provided in available contexts | Loss-of-function mutations | Epigenetic dysregulation, altered differentiation programs | Chromatin modification / transcriptional control | Present across UC; part of urothelial molecular heterogeneity | May shape subtype identity and progression risk | Supports epigenetic-therapy research and molecular classification, but no routine targeted use | (dyrskjøt2023bladdercancer pages 1-3, alahmadie2024molecularpathologyof pages 1-3) |
| **KMT2D / KMT2C / KMT2A** | Recurrently altered; distinct prevalence reported between UTUC and bladder UC | Mutations, likely loss/dysregulation | Chromatin remodeling defects and transcriptional dysregulation | Histone modification / chromatin regulation | Contribute to biologic differences between UTUC and bladder UC | May underlie site-specific pathogenesis and heterogeneity | Potential stratification biomarkers in genomic profiling; investigational therapeutic relevance | (schwarzova2023molecularclassificationof pages 1-2, alahmadie2024molecularpathologyof pages 1-3) |
| **HRAS** | Recurrent but less common than FGFR3/TP53 | Activating mutations | MAPK pathway activation | RAS-MAPK | More often associated with non–muscle-invasive pathways in classic urothelial models | Supports proliferative signaling | Primarily biologic marker; potential eligibility for future RAS-pathway strategies | (su2025reviewofrecent pages 1-3, peng2023targetedtherapiesin pages 1-2) |
| **ERBB2 (HER2)** | Overexpression / activation in subset; exact % not given in available contexts | Amplification/overexpression, mutation in subset | Enhanced proliferation, invasion, metastasis signaling | ERBB/HER2 RTK signaling | More often discussed in advanced/aggressive disease workups | Linked to invasion and metastasis in review literature | Candidate biomarker for HER2-directed therapy trials and precision oncology approaches | (su2025reviewofrecent pages 1-3, lopezbeltran2024advancesindiagnosis pages 1-1) |
| **PTEN** | Recurrent but less common than TP53/FGFR3 | Loss-of-function mutation/deletion | Reduced negative regulation of PI3K signaling | PI3K-AKT-mTOR | More relevant in invasive/aggressive molecular programs | May contribute to progression and therapy resistance | Supports rationale for PI3K/AKT/mTOR combination strategies | (su2025reviewofrecent pages 1-3, peng2023targetedtherapiesin pages 1-2) |
| **DDR gene group (e.g., BRCA1, CHEK2, PMS2 and related genes)** | Pathogenic germline variants found in ~11.24% of one Chinese UC cohort; deleterious DDR alterations in ~22.9% UTUC and ~33.9% UCB | Germline or somatic pathogenic variants | Impaired homologous recombination / checkpoint repair | DNA damage response / repair | Present in both UTUC and bladder UC, with prevalence differences by site | May raise mutational burden and treatment sensitivity | Potential relevance to platinum response, immunotherapy response, and future PARP-based strategies; also germline counseling implications | (alahmadie2024molecularpathologyof pages 1-3) |
| **APOBEC mutational process** | Not a gene alteration but dominant mutational signature; accounted for ~66% of SNVs in TCGA MIBC per review summary | Cytidine deaminase mutational signature | Hypermutation and genomic diversification | Mutagenesis / innate immunity-related editing | Strongly emphasized in MIBC | Associated in review summary with improved 5-year overall survival in MIBC despite high mutation burden | Relevant to biomarker development, immunogenicity, and molecular taxonomy rather than direct targeting | (alahmadie2024molecularpathologyof pages 1-3) |


*Table: This table summarizes recurrent molecular alterations in transitional cell carcinoma/urothelial carcinoma, emphasizing stage associations, pathway biology, prognostic patterns, and current or emerging therapeutic relevance. It is useful for linking disease mechanisms to precision oncology and biomarker-driven management.*

### Chromosomal Abnormalities

- Chromosome 9 deletion common in NMIBC and MIBC, affecting CDKN2A, PTCH1, TSC1 (peng2023targetedtherapiesin pages 1-2)
- MIBC characterized by aneuploidy, chromothripsis, and genomic rearrangements; NMIBC typically near-diploid (peng2023targetedtherapiesin pages 1-2)

### Somatic vs. Germline

Most UC mutations are somatic (acquired). Germline DDR gene variants (BRCA1, CHEK2, PMS2) identified in ~11% of patients have implications for hereditary cancer risk assessment and family counseling (alahmadie2024molecularpathologyof pages 1-3).

### Functional Consequences

- **TP53 mutations:** Loss of apoptosis, DNA damage response, cell cycle arrest → genomic instability (su2025reviewofrecent pages 1-3)
- **FGFR3 mutations:** Gain-of-function → ligand-independent receptor activation, proliferation, luminal differentiation (su2025reviewofrecent pages 1-3, alahmadie2024molecularpathologyof pages 1-3)
- **ERCC2 mutations:** Defective DNA repair → increased mutagenesis and cisplatin sensitivity (alahmadie2024molecularpathologyof pages 1-3)

### Epigenetic Information

DNA methylation and chromatin modifications are recognized as important in UC but were not detailed extensively in the retrieved 2023-2024 literature. Chromatin-modifying genes (KDM6A, KMT2D, KMT2C) are recurrently altered, affecting transcriptional regulation and differentiation programs (alahmadie2024molecularpathologyof pages 1-3).

---

## 5. ENVIRONMENTAL INFORMATION

### Environmental Factors

- **Tobacco smoke:** PAHs, aromatic amines (4-aminobiphenyl) (alouini2024riskfactorsassociated pages 1-2, hoogstraten2023globaltrendsin pages 1-2)
- **Occupational carcinogens:** Aromatic amines in industrial settings (dye, paint, petroleum, metals) (alouini2024riskfactorsassociated pages 1-2)
- **Aristolochic acid:** Plant-derived nephrotoxin in endemic regions (kolawa2023overviewdiagnosisand pages 1-2, pandolfo2024uppertracturothelial pages 1-2)
- **Chlorinated water disinfection byproducts:** Trihalomethanes (alouini2024riskfactorsassociated pages 1-2)
- **Air pollution:** VOCs, PAHs, PM2.5 (alouini2024riskfactorsassociated pages 1-2)

### Lifestyle Factors

- **Smoking:** Dominant modifiable risk factor (dyrskjøt2023bladdercancer pages 1-3, hoogstraten2023globaltrendsin pages 1-2)
- **Diet:** Processed meat, whole milk, selenium, vitamins A and E (alouini2024riskfactorsassociated pages 1-2)
- **Alcohol consumption** (alouini2024riskfactorsassociated pages 1-2)

Research on lifestyle factors' associations with UC outcomes is scarce and represents a priority area (hoogstraten2023globaltrendsin pages 1-2).

### Infectious Agents

Not prominently featured in UC etiology in the retrieved literature. Schistosomiasis is associated with squamous cell carcinoma in endemic regions but was not emphasized in the 2023-2024 sources reviewed.

---

## 6. MECHANISM / PATHOPHYSIOLOGY

### Molecular Pathways

**Receptor Tyrosine Kinase (RTK) Signaling:**
- **FGFR3 pathway:** Activating mutations → MAPK and PI3K-AKT pathway activation → proliferation and survival (alahmadie2024molecularpathologyof pages 1-3, peng2023targetedtherapiesin pages 1-2)
- **ERBB2 (HER2) pathway:** Overexpression/amplification → proliferation, invasion, metastasis (su2025reviewofrecent pages 1-3)

**Cell Cycle Dysregulation:**
- **p53 pathway:** TP53 mutations → loss of checkpoint control, apoptosis resistance, genomic instability (su2025reviewofrecent pages 1-3, alahmadie2024molecularpathologyof pages 1-3)
- **RB1 pathway:** Inactivation → G1/S transition deregulation (su2025reviewofrecent pages 1-3, alahmadie2024molecularpathologyof pages 1-3)
- **CDKN2A loss:** Loss of p16 → unchecked CDK4/6 activity (alahmadie2024molecularpathologyof pages 1-3, peng2023targetedtherapiesin pages 1-2)

**PI3K-AKT-mTOR Pathway:**
- PIK3CA activating mutations and PTEN loss → enhanced proliferation, survival, therapy resistance (alahmadie2024molecularpathologyof pages 1-3, peng2023targetedtherapiesin pages 1-2)

**DNA Damage Response (DDR):**
- ERCC2, BRCA1, CHEK2, PMS2, and other DDR gene alterations → defective repair, increased mutagenesis, cisplatin sensitivity (alahmadie2024molecularpathologyof pages 1-3)

**Chromatin Modification:**
- KDM6A, KMT2D/C/A alterations → epigenetic dysregulation, altered differentiation (alahmadie2024molecularpathologyof pages 1-3)

### Cellular Processes

- **Apoptosis dysregulation:** TP53 loss, BCL-2 family alterations (su2025reviewofrecent pages 1-3)
- **Proliferation signaling:** RTK-RAS-MAPK, PI3K-AKT-mTOR hyperactivation (alahmadie2024molecularpathologyof pages 1-3, peng2023targetedtherapiesin pages 1-2)
- **Cell cycle checkpoint loss:** RB1, CDKN2A, TP53 pathway disruption (su2025reviewofrecent pages 1-3, alahmadie2024molecularpathologyof pages 1-3)
- **Epithelial-mesenchymal transition (EMT):** Basal/squamous subtypes exhibit EMT features (schwarzova2023molecularclassificationof pages 1-2, su2025reviewofrecent pages 1-3)

### Immune System Involvement

UC exhibits high mutational burden and neoantigen load, rendering it immunogenic and responsive to immune checkpoint inhibition (peng2023targetedtherapiesin pages 1-2). The tumor microenvironment (TME) includes cancer-associated fibroblasts, immunosuppressive cells (Tregs, MDSCs), and extracellular matrix components that influence therapeutic response (peng2023targetedtherapiesin pages 1-2). PD-L1 expression and T cell inflammation scores correlate with immunotherapy response (peng2023targetedtherapiesin pages 1-2).

### Molecular Profiling

**Transcriptomics:**
mRNA expression profiling defines luminal, basal, neuroendocrine-like, and other molecular subtypes with distinct treatment responses (schwarzova2023molecularclassificationof pages 1-2, su2025reviewofrecent pages 1-3).

**Genomics:**
High mutation burden (mean 7.7/Mb), APOBEC and ERCC2 mutational signatures, copy number alterations (alahmadie2024molecularpathologyof pages 1-3, peng2023targetedtherapiesin pages 1-2).

**Proteomics and Metabolomics:**
Not extensively detailed in retrieved 2023-2024 literature but recognized as emerging areas for biomarker discovery.

### Gene Ontology (GO) Suggestions

- GO:0008283 - cell proliferation
- GO:0006915 - apoptotic process
- GO:0006281 - DNA repair
- GO:0007049 - cell cycle
- GO:0016568 - chromatin modification
- GO:0038127 - ERBB signaling pathway
- GO:0038095 - Fc-epsilon receptor signaling pathway (for immune components)

### Cell Type Ontology (CL) Suggestions

- CL:0000731 - urothelial cell
- CL:0002618 - transitional epithelial cell
- CL:0000066 - epithelial cell
- CL:0000115 - endothelial cell (tumor vasculature)
- CL:0000235 - macrophage (tumor-associated macrophages)
- CL:0000084 - T cell (tumor-infiltrating lymphocytes)

---

## 7. ANATOMICAL STRUCTURES AFFECTED

### Organ Level

**Primary Organs:**
- **Urinary bladder:** 90-95% of UC (dyrskjøt2023bladdercancer pages 1-3, peng2023targetedtherapiesin pages 1-2)
- **Upper urinary tract:** Renal pelvis, renal calyces, ureter (5-10% of UC) (kolawa2023overviewdiagnosisand pages 1-2, pandolfo2024uppertracturothelial pages 1-2)
- **Proximal urethra** (rare) (peng2023targetedtherapiesin pages 1-2)

**Secondary Involvement:**
- **Lymph nodes:** Regional pelvic and retroperitoneal nodes (dyrskjøt2023bladdercancer pages 1-3)
- **Metastatic sites:** Lungs, liver, bones (dyrskjøt2023bladdercancer pages 1-3)

**Body Systems:**
- Urinary system (primary)
- Lymphatic system (metastatic spread)
- Skeletal, respiratory, hepatic systems (distant metastases)

### Tissue and Cell Level

**Tissue Types:**
- **Transitional epithelium (urothelium):** Primary tissue of origin (dyrskjøt2023bladdercancer pages 1-3)
- **Lamina propria:** Submucosal connective tissue in T1 disease (dyrskjøt2023bladdercancer pages 1-3)
- **Detrusor muscle (muscularis propria):** Invaded in MIBC (T2-T4) (dyrskjøt2023bladdercancer pages 1-3)
- **Perivesical fat:** Involved in T3 disease (dyrskjøt2023bladdercancer pages 1-3)

**Cell Populations:**
- **Urothelial cells:** Primary cells of origin (CL:0000731, CL:0002618) (dyrskjøt2023bladdercancer pages 1-3)
- **Umbrella cells:** Surface urothelial layer (dyrskjøt2023bladdercancer pages 1-3)
- **Basal and intermediate urothelial cells:** Underlying layers (dyrskjøt2023bladdercancer pages 1-3)

### Subcellular Level

- **Nucleus:** TP53, RB1, chromatin modifier gene alterations (su2025reviewofrecent pages 1-3, alahmadie2024molecularpathologyof pages 1-3)
- **Cell membrane:** FGFR3, ERBB2, Nectin-4, Trop-2 surface receptors (targets for therapy) (su2025reviewofrecent pages 1-3, peng2023targetedtherapiesin pages 1-2)
- **Cytoplasm:** PI3K-AKT-mTOR, MAPK signaling cascades (alahmadie2024molecularpathologyof pages 1-3, peng2023targetedtherapiesin pages 1-2)

### UBERON Term Suggestions

- UBERON:0001255 - urinary bladder
- UBERON:0001223 - renal pelvis
- UBERON:0000056 - ureter
- UBERON:0000057 - urethra
- UBERON:0001008 - renal system
- UBERON:0001255 - bladder wall
- UBERON:0004648 - lamina propria of urinary bladder
- UBERON:0013233 - bladder detrusor muscle

---

## 8. TEMPORAL DEVELOPMENT

### Onset

- **Age:** Median 70 years at diagnosis; predominantly adult-onset (alouini2024riskfactorsassociated pages 1-2)
- **Pattern:** Often insidious; gross hematuria is the alerting symptom in most cases (lopezbeltran2024advancesindiagnosis pages 1-1)
- **Early detection:** Improves prognosis; minimally invasive diagnostic options are needed (hoogstraten2023globaltrendsin pages 1-2)

### Progression

**Disease Stages:**
- **NMIBC:** Ta (non-invasive papillary), Tis (carcinoma in situ), T1 (lamina propria invasion) (dyrskjøt2023bladdercancer pages 1-3)
- **MIBC:** T2 (muscle invasion), T3 (perivesical tissue invasion), T4 (adjacent organ invasion) (dyrskjøt2023bladdercancer pages 1-3)
- **Metastatic:** Regional lymph nodes → distant sites (lungs, liver, bones) (dyrskjøt2023bladdercancer pages 1-3)

**Progression Rates:**
- NMIBC: 31-78% recurrence, 1-45% progression to MIBC at 5 years (lopezbeltran2024advancesindiagnosis pages 1-1)
- Carcinoma in situ: ~50% progression at 5 years if untreated (lopezbeltran2024advancesindiagnosis pages 1-1)
- UTUC: 60% invasive, 30% metastatic at diagnosis (more aggressive than bladder UC) (kolawa2023overviewdiagnosisand pages 1-2)

**Progression Rate:** Variable; low-grade NMIBC is indolent with frequent recurrence but rare progression; high-grade MIBC and UTUC progress rapidly (kolawa2023overviewdiagnosisand pages 1-2, lopezbeltran2024advancesindiagnosis pages 1-1)

**Disease Course:** 
- NMIBC: Often relapsing-remitting with surveillance (lopezbeltran2024advancesindiagnosis pages 1-1)
- MIBC/metastatic: Progressive (dyrskjøt2023bladdercancer pages 1-3)

**Disease Duration:** Chronic with long-term surveillance for NMIBC; poor survival for metastatic disease (median OS 15 months untreated) (dyrskjøt2023bladdercancer pages 1-3)

### Patterns

**Critical Periods:**
- Early detection (before muscle invasion) offers better outcomes (dyrskjøt2023bladdercancer pages 1-3, hoogstraten2023globaltrendsin pages 1-2)
- Timely radical cystectomy or multimodality therapy for MIBC is critical (lopezbeltran2024advancesindiagnosis pages 1-1)

---

## 9. INHERITANCE AND POPULATION

### Epidemiology

Comprehensive epidemiology data are presented in the artifact table below.

| Epidemiology domain | Statistic / finding | Value | Population / scope | Year / source framing | Citation |
|---|---|---:|---|---|---|
| Global incidence | New bladder cancer cases worldwide | 573,000 | Global, all bladder cancers; >90% are urothelial / transitional-cell histology | GLOBOCAN 2020 summarized in 2023 review | (hoogstraten2023globaltrendsin pages 1-2, dyrskjøt2023bladdercancer pages 1-3) |
| Global incidence | New bladder cancer cases worldwide | 613,799 | Global, all bladder cancers | GLOBOCAN 2022 summarized in 2024 review | (alouini2024riskfactorsassociated pages 1-2) |
| Global incidence | Bladder cancer rank among all cancers | 10th most common cancer globally | Global | 2020 review synthesis | (hoogstraten2023globaltrendsin pages 1-2) |
| Global incidence | Age-standardized incidence rate (ASR) | 5.6 per 100,000 | Global | 2022 global estimate | (alouini2024riskfactorsassociated pages 1-2) |
| Global incidence by sex | Male incident cases | 471,077 (76.7%) | Global | 2022 global estimate | (alouini2024riskfactorsassociated pages 1-2) |
| Global incidence by sex | Female incident cases | 142,722 (23.3%) | Global | 2022 global estimate | (alouini2024riskfactorsassociated pages 1-2) |
| Sex ratio | Male:female incident case ratio | ~3.3:1 | Global, based on 471,077 vs 142,722 cases | 2022 global estimate | (alouini2024riskfactorsassociated pages 1-2) |
| Global mortality | Bladder cancer deaths worldwide | 220,347 | Global | 2022 global estimate | (alouini2024riskfactorsassociated pages 1-2) |
| Global mortality | Age-standardized mortality rate | 1.9 per 100,000 | Global | 2022 global estimate | (alouini2024riskfactorsassociated pages 1-2) |
| Global mortality by sex | Male share of bladder cancer deaths | 75.1% | Global | 2022 global estimate | (alouini2024riskfactorsassociated pages 1-2) |
| Global prevalence | 5-year prevalence | 490,902 | Global | 2022 global estimate | (alouini2024riskfactorsassociated pages 1-2) |
| Prevalence distribution | Highest regional share of 5-year prevalence | Europe 154.4 | Regional share as reported in review | 2022 global estimate summarized in 2024 review | (alouini2024riskfactorsassociated pages 1-2) |
| Prevalence distribution | Other regional 5-year prevalence shares | Asia 131.1; North America 66.8; Latin America/Caribbean 21.5; Africa 19.6; Oceania 3.6 | Regional shares as reported in review | 2022 global estimate summarized in 2024 review | (alouini2024riskfactorsassociated pages 1-2) |
| Geographic distribution | Highest male ASR reported | 40 per 100,000 | Greece | GLOBOCAN 2020 summarized in 2023 review | (hoogstraten2023globaltrendsin pages 1-2) |
| Geographic distribution | Lowest male ASR reported | <1 per 100,000 | Several African countries, including Côte d’Ivoire and Liberia | GLOBOCAN 2020 summarized in 2023 review | (hoogstraten2023globaltrendsin pages 1-2) |
| Geographic distribution | Highest female ASR reported | 9 per 100,000 | Hungary | GLOBOCAN 2020 summarized in 2023 review | (hoogstraten2023globaltrendsin pages 1-2) |
| Geographic distribution | Lowest female ASR reported | <1 per 100,000 | Several African and Eastern Mediterranean countries | GLOBOCAN 2020 summarized in 2023 review | (hoogstraten2023globaltrendsin pages 1-2) |
| Age distribution | Median age at diagnosis | 70 years | Bladder cancer overall | 2024 review | (alouini2024riskfactorsassociated pages 1-2) |
| Age distribution (advanced disease cohort) | Median age at start of first-line treatment | 73 years (IQR 66–80) | US advanced urothelial carcinoma cohort, n=7,260 | 2011–2023 EHR cohort, published 2024 | (thomas2024treatmentpatternsand pages 1-2) |
| US burden | Projected new bladder cancer cases | 82,290 | United States | 2023 projection, reported in 2024 study | (thomas2024treatmentpatternsand pages 1-2) |
| US burden | Projected bladder cancer deaths | 16,710 | United States | 2023 projection, reported in 2024 study | (thomas2024treatmentpatternsand pages 1-2) |
| Stage distribution at presentation | Non-muscle-invasive bladder cancer (NMIBC) at diagnosis | ~70–75% | Bladder urothelial carcinoma | 2023–2024 reviews | (schwarzova2023molecularclassificationof pages 1-2, lopezbeltran2024advancesindiagnosis pages 1-1) |
| Stage distribution at presentation | Muscle-invasive bladder cancer (MIBC) at diagnosis | ~25–30% | Bladder urothelial carcinoma | 2023–2024 reviews | (dyrskjøt2023bladdercancer pages 1-3, schwarzova2023molecularclassificationof pages 1-2, peng2023targetedtherapiesin pages 1-2, lopezbeltran2024advancesindiagnosis pages 1-1) |
| Histology distribution | Urothelial / transitional cell carcinoma among bladder cancers | 90–95% | Bladder cancer overall | 2023–2024 reviews | (dyrskjøt2023bladdercancer pages 1-3, kolawa2023overviewdiagnosisand pages 1-2, kwon2025advancesintherapy pages 1-2, peng2023targetedtherapiesin pages 1-2) |
| Upper tract share | Upper tract urothelial carcinoma (UTUC) among urothelial carcinomas | 5–10% | Urothelial carcinoma overall | 2023–2024 reviews | (kolawa2023overviewdiagnosisand pages 1-2, pandolfo2024uppertracturothelial pages 1-2) |
| UTUC stage distribution | Invasive disease at diagnosis | ~60% | Upper tract urothelial carcinoma | 2023 review | (kolawa2023overviewdiagnosisand pages 1-2) |
| UTUC stage distribution | Metastatic disease at diagnosis | ~30% | Upper tract urothelial carcinoma | 2023 review | (kolawa2023overviewdiagnosisand pages 1-2) |
| Clinical presentation | Hematuria frequency in UTUC | ~80% | Upper tract urothelial carcinoma | 2024 guideline review | (pandolfo2024uppertracturothelial pages 1-2) |
| Temporal trend | Expected global case trend | Number of new cases expected to double by 2040 | Global bladder cancer burden | WHO-based projection summarized in 2023 review | (dyrskjøt2023bladdercancer pages 1-3) |
| Temporal trend | Incidence pattern | Incidence has not been stable worldwide over time and is influenced by ageing, population growth, and smoking exposure | Global | 2023 epidemiology review | (hoogstraten2023globaltrendsin pages 1-2) |
| Survival context | 5-year survival for localized bladder cancer | 71% | United States | Reported in 2024 cohort study | (thomas2024treatmentpatternsand pages 1-2) |
| Survival context | 5-year survival for metastatic bladder cancer | 8.3% | United States | Reported in 2024 cohort study | (thomas2024treatmentpatternsand pages 1-2) |
| Survival context | NMIBC overall survival | 90% | General bladder cancer review context | 2024 BMJ review | (lopezbeltran2024advancesindiagnosis pages 1-1) |


*Table: This table compiles recent 2023-2024 epidemiology statistics for transitional cell carcinoma/urothelial carcinoma, including incidence, mortality, prevalence, demographics, geography, stage at presentation, and time trends. It is useful as a quick-reference summary for disease burden and population characteristics.*

**Key Statistics:**
- **Global incidence:** 613,799 new cases in 2022 (alouini2024riskfactorsassociated pages 1-2); 573,000 in 2020 (hoogstraten2023globaltrendsin pages 1-2)
- **Global mortality:** 220,347 deaths in 2022; ASR 1.9 per 100,000 (alouini2024riskfactorsassociated pages 1-2)
- **Prevalence:** 5-year prevalence of 490,902 cases in 2022 (alouini2024riskfactorsassociated pages 1-2)
- **Ranking:** 10th most common cancer globally; 6th in men (hoogstraten2023globaltrendsin pages 1-2)
- **US burden:** 82,290 new cases and 16,710 deaths projected for 2023 (thomas2024treatmentpatternsand pages 1-2)

### Inheritance (Genetic Etiology)

Urothelial carcinoma is predominantly a **sporadic** disease with somatic mutations. Germline pathogenic variants in DDR genes (BRCA1, CHEK2, PMS2, and others) were identified in ~11% of Chinese UC patients, suggesting hereditary susceptibility in a subset (alahmadie2024molecularpathologyof pages 1-3). Lynch syndrome association with UTUC indicates autosomal dominant inheritance in those families (kolawa2023overviewdiagnosisand pages 1-2).

- **Inheritance pattern:** Primarily sporadic; germline DDR variants suggest autosomal dominant susceptibility in subset
- **Penetrance:** Not well-characterized for UC-specific germline variants
- **Consanguinity role:** Not emphasized in literature
- **Founder effects:** Not detailed in retrieved sources

### Population Demographics

**Sex Ratio:**
- Male:female ratio ~3.3:1 globally (471,077 vs 142,722 cases in 2022) (alouini2024riskfactorsassociated pages 1-2)
- Male predominance attributed to historical smoking prevalence and occupational exposures (hoogstraten2023globaltrendsin pages 1-2)

**Age Distribution:**
- Median age at diagnosis: 70 years (alouini2024riskfactorsassociated pages 1-2)
- Advanced disease cohort median age: 73 years (IQR 66-80) (thomas2024treatmentpatternsand pages 1-2)

**Geographic Distribution:**
- **Highest incidence:** Greece (male ASR 40/100,000), Hungary (female ASR 9/100,000) (hoogstraten2023globaltrendsin pages 1-2)
- **Lowest incidence:** Several African countries (<1/100,000 for both sexes) (hoogstraten2023globaltrendsin pages 1-2)
- **Regional prevalence (5-year):** Europe 154.4%, Asia 131.1%, North America 66.8% of global cases (alouini2024riskfactorsassociated pages 1-2)

**Temporal Trends:**
- Global cases expected to double by 2040 due to population aging and growth (dyrskjøt2023bladdercancer pages 1-3)
- Incidence not stable worldwide; influenced by smoking trends and demographic changes (hoogstraten2023globaltrendsin pages 1-2)

---

## 10. DIAGNOSTICS

### Clinical Tests

**Laboratory Tests:**
- **Urinalysis:** Hematuria detection (pandolfo2024uppertracturothelial pages 1-2)
- **Urine cytology:** Diagnostic adjunct, especially for high-grade disease and carcinoma in situ (kolawa2023overviewdiagnosisand pages 1-2)
- **Blood tests:** Renal function, anemia assessment

**Biomarkers:**
Urine-based molecular biomarkers are emerging for non-invasive diagnosis and surveillance:
- Urinary exosomal lncRNA (e.g., SNHG16) shows promise; AUC 0.791 vs. 0.597 for cytology in one 2023 study (lopezbeltran2024advancesindiagnosis pages 1-1)
- Cell-free DNA (ctDNA) in plasma for minimal residual disease detection and relapse monitoring (dyrskjøt2023bladdercancer pages 1-3)
- PD-L1 expression, FGFR3 mutations, tumor mutational burden (TMB) as predictive biomarkers for therapy selection (peng2023targetedtherapiesin pages 1-2, lopezbeltran2024advancesindiagnosis pages 1-1)

**Imaging Studies:**
- **CT urography:** Standard for UTUC and staging (kolawa2023overviewdiagnosisand pages 1-2, pandolfo2024uppertracturothelial pages 1-2)
- **Cystoscopy with biopsy:** Gold standard for bladder UC diagnosis and surveillance (dyrskjøt2023bladdercancer pages 1-3, hoogstraten2023globaltrendsin pages 1-2)
- **Ureteroscopy with biopsy:** For UTUC (kolawa2023overviewdiagnosisand pages 1-2, pandolfo2024uppertracturothelial pages 1-2)
- **Cross-sectional imaging (CT, MRI):** For staging MIBC and metastatic disease (dyrskjøt2023bladdercancer pages 1-3)

**Functional Tests:**
- Cystoscopy remains primary functional/visual diagnostic method (dyrskjøt2023bladdercancer pages 1-3, hoogstraten2023globaltrendsin pages 1-2)

**Biopsy and Pathology:**
- **TURBT:** Provides tissue for histopathologic grading and staging (dyrskjøt2023bladdercancer pages 1-3, lopezbeltran2024advancesindiagnosis pages 1-1)
- **Histopathology:** WHO/ISUP grading (low vs. high grade), TNM staging (dyrskjøt2023bladdercancer pages 1-3)
- **Immunohistochemistry:** p53, FGFR3, PD-L1, urothelial markers (CK20, CK7, uroplakins) for subtyping and biomarker assessment (su2025reviewofrecent pages 1-3, alahmadie2024molecularpathologyof pages 1-3)

### Genetic Testing

**Overview:**
Tumor genomic profiling is increasingly used for precision medicine and biomarker-driven therapy selection (lopezbeltran2024advancesindiagnosis pages 1-1).

**Targeted Gene Panels:**
- Cancer gene panels (e.g., 618-gene NGS panel in one study) identify actionable FGFR2/3, ERBB2, PIK3CA, DDR gene alterations (alahmadie2024molecularpathologyof pages 1-3)

**Whole Exome Sequencing (WES):**
- Used in research and select clinical settings for comprehensive mutational profiling (alahmadie2024molecularpathologyof pages 1-3)

**Single Gene Testing:**
- FGFR3 mutation testing for erdafitinib eligibility (peng2023targetedtherapiesin pages 1-2)
- Germline DDR gene testing (BRCA1, CHEK2, PMS2) for hereditary risk assessment (alahmadie2024molecularpathologyof pages 1-3)

**Liquid Biopsy:**
- Circulating tumor DNA (ctDNA) and urinary DNA for non-invasive monitoring (dyrskjøt2023bladdercancer pages 1-3, lopezbeltran2024advancesindiagnosis pages 1-1)

### Omics-Based Diagnostics

- **RNA sequencing / transcriptomics:** Molecular subtyping (luminal, basal, neuroendocrine-like) (schwarzova2023molecularclassificationof pages 1-2, su2025reviewofrecent pages 1-3)
- **Proteomics:** Emerging for biomarker discovery
- **Metabolomics:** Investigational
- **Epigenomics:** DNA methylation profiling for early detection and prognostication (su2025reviewofrecent pages 1-3)

### Clinical Criteria

- **TNM classification (AJCC 8th edition):** Stages Tis, Ta, T1-T4, N0-N3, M0-M1 (dyrskjøt2023bladdercancer pages 1-3)
- **WHO/ISUP grading:** Low-grade vs. high-grade (dyrskjøt2023bladdercancer pages 1-3)
- **Risk stratification:** Low, intermediate, high-risk NMIBC based on grade, stage, multifocality, size, CIS presence (lopezbeltran2024advancesindiagnosis pages 1-1)

### Differential Diagnosis

- Benign bladder lesions (cystitis, papilloma)
- Other histologic subtypes (squamous cell carcinoma, adenocarcinoma, small-cell carcinoma)
- Upper tract vs. bladder origin distinction in UTUC (kolawa2023overviewdiagnosisand pages 1-2)

### Screening

Population-based screening for bladder cancer is not established. High-risk groups (heavy smokers, occupational exposures, hereditary syndromes) may benefit from surveillance, but evidence is limited (hoogstraten2023globaltrendsin pages 1-2). Awareness campaigns and early hematuria investigation are public health priorities (hoogstraten2023globaltrendsin pages 1-2).

---

## 11. OUTCOME/PROGNOSIS

### Survival and Mortality

**5-Year Survival Rates:**
- **Localized bladder cancer:** 71% (US) (thomas2024treatmentpatternsand pages 1-2)
- **Metastatic bladder cancer:** 8.3% (US) (thomas2024treatmentpatternsand pages 1-2)
- **NMIBC overall survival:** 90% (lopezbeltran2024advancesindiagnosis pages 1-1)
- **MIBC:** ~50% 5-year survival after radical cystectomy (lopezbeltran2024advancesindiagnosis pages 1-1)
- **UTUC:** 57-73% 5-year disease-specific survival (less favorable than bladder UC) (kolawa2023overviewdiagnosisand pages 1-2)

**Mortality Rates:**
- Global age-standardized mortality rate: 1.9 per 100,000 (alouini2024riskfactorsassociated pages 1-2)
- Male share of deaths: 75.1% globally (alouini2024riskfactorsassociated pages 1-2)
- Untreated metastatic disease: median survival ~15 months (dyrskjøt2023bladdercancer pages 1-3)

### Morbidity and Function

- NMIBC: High recurrence burden (31-78% at 5 years) necessitates frequent cystoscopy, impacting quality of life (lopezbeltran2024advancesindiagnosis pages 1-1)
- MIBC: Radical cystectomy with urinary diversion causes significant morbidity (body image, sexual function, bowel complications) (lopezbeltran2024advancesindiagnosis pages 1-1)
- Metastatic disease: Palliative care needs, functional decline (kwon2025advancesintherapy pages 1-2)

### Complications

- **NMIBC:** Progression to MIBC (1-45% at 5 years), recurrence (lopezbeltran2024advancesindiagnosis pages 1-1)
- **MIBC:** Postoperative complications (infection, ileus, urinary leak), local recurrence (30% after cystectomy, median 12 months), distant metastases (lopezbeltran2024advancesindiagnosis pages 1-1)
- **Metastatic disease:** Organ failure, cachexia, pain (dyrskjøt2023bladdercancer pages 1-3)

### Prognostic Factors

**Clinical:**
- Stage (NMIBC vs. MIBC vs. metastatic) (dyrskjøt2023bladdercancer pages 1-3, lopezbeltran2024advancesindiagnosis pages 1-1)
- Grade (low vs. high) (dyrskjøt2023bladdercancer pages 1-3)
- CIS presence (lopezbeltran2024advancesindiagnosis pages 1-1)
- Tumor size, multifocality, recurrence history (lopezbeltran2024advancesindiagnosis pages 1-1)
- Nodal status, metastases (dyrskjøt2023bladdercancer pages 1-3, lopezbeltran2024advancesindiagnosis pages 1-1)

**Molecular:**
- TP53 mutations: Associated with poor survival (su2025reviewofrecent pages 1-3)
- FGFR3 mutations: Associated with better prognosis in some contexts but heterogeneous (su2025reviewofrecent pages 1-3)
- STAG2 alterations: Associated with improved OS, especially in TP53-wild-type tumors (alahmadie2024molecularpathologyof pages 1-3)
- DDR gene alterations: May predict response to cisplatin and immunotherapy (alahmadie2024molecularpathologyof pages 1-3)
- Molecular subtype: Basal/squamous worse than luminal-papillary (schwarzova2023molecularclassificationof pages 1-2, su2025reviewofrecent pages 1-3)
- Tumor mutational burden (TMB), APOBEC signature: Higher TMB associated with immunotherapy response (alahmadie2024molecularpathologyof pages 1-3)

---

## 12. TREATMENT

Comprehensive treatment modalities are detailed in the artifact table below.

| Disease stage | Treatment type | Specific agents / procedures | Mechanism of action | Indication / use case | Response rate / key efficacy data | FDA status / regulatory note | Suggested MAXO term(s) | Evidence |
|---|---|---|---|---|---|---|---|---|
| NMIBC | Endoscopic surgery | Transurethral resection of bladder tumor (TURBT) | Endoscopic resection/debulking for diagnosis, staging, and local control | Initial management of most NMIBC; foundation before adjuvant intravesical therapy | Standard first intervention; recurrence remains common, with NMIBC recurrence reported at ~31–78% within 5 years in review literature | Standard of care | MAXO: transurethral resection; endoscopic surgical excision | (lopezbeltran2024advancesindiagnosis pages 1-1, peng2023targetedtherapiesin pages 1-2) |
| NMIBC | Intravesical immunotherapy | Bacillus Calmette-Guérin (BCG) | Local immune activation in bladder, promoting antitumor immunity | Gold standard for high-grade/high-risk NMIBC after TURBT; reduces recurrence and progression | Widely accepted standard; exact pooled response not given in available contexts, but described as gold standard for high-risk NMIBC | FDA-approved, established standard | MAXO: intravesical immunotherapy; bacillus Calmette-Guérin administration | (lopezbeltran2024advancesindiagnosis pages 1-1, dyrskjøt2023bladdercancer pages 1-3) |
| NMIBC | Intravesical chemotherapy | Post-TURBT intravesical chemotherapy (agent not always specified in source context) | Local cytotoxic exposure to residual urothelial tumor cells | Low/intermediate-risk NMIBC after TURBT; also used when recurrence-risk reduction is desired | Standard adjunctive therapy; exact response rates not stated in available contexts | Standard practice; specific agents vary | MAXO: intravesical chemotherapy administration | (dyrskjøt2023bladdercancer pages 1-3, lopezbeltran2024advancesindiagnosis pages 1-1) |
| BCG-unresponsive NMIBC | Systemic immunotherapy | Pembrolizumab | PD-1 checkpoint blockade restoring antitumor T-cell activity | High-risk BCG-unresponsive NMIBC in patients seeking bladder preservation / not undergoing cystectomy | Described as a recent FDA-approved option; exact CR rate not stated in available contexts here | FDA-approved for BCG-unresponsive high-risk NMIBC | MAXO: immune checkpoint inhibitor therapy; pembrolizumab administration | (lopezbeltran2024advancesindiagnosis pages 1-1) |
| BCG-unresponsive NMIBC | Intravesical gene therapy | Nadofaragene firadenovec (Adstiladrin) | Gene therapy delivering interferon pathway stimulation via adenoviral vector | Conservative treatment option for BCG-unresponsive NMIBC | Reported as promising and FDA-approved in review literature; exact response metrics not stated in available contexts | FDA-approved | MAXO: intravesical gene therapy; viral vector gene delivery | (lopezbeltran2024advancesindiagnosis pages 1-1) |
| High-risk / refractory NMIBC | Radical surgery | Radical cystectomy | Complete removal of bladder for definitive local control | Recommended for selected high-risk, recurrent, or BCG-unresponsive NMIBC | Offers definitive local control but with major morbidity; no single response rate stated | Standard of care option | MAXO: cystectomy; radical surgical excision | (lopezbeltran2024advancesindiagnosis pages 1-1) |
| MIBC | Radical surgery | Radical cystectomy with lymph node dissection | Removal of primary tumor and regional nodes | Standard local treatment for localized MIBC | Standard of care; overall outcomes depend on pathologic stage and perioperative therapy | Standard of care | MAXO: cystectomy; lymph node dissection | (dyrskjøt2023bladdercancer pages 1-3, schwarzova2023molecularclassificationof pages 1-2, lopezbeltran2024advancesindiagnosis pages 1-1) |
| MIBC | Neoadjuvant systemic chemotherapy | Cisplatin-based chemotherapy (commonly gemcitabine/cisplatin in modern practice) | Platinum-induced DNA damage/crosslinking causing tumor cell death | Standard pre-cystectomy treatment for cisplatin-eligible MIBC | Standard of care; review notes improved outcomes and pathologic response in neoadjuvant setting, but exact pooled rate not given in available contexts | Standard of care | MAXO: neoadjuvant chemotherapy; platinum-based chemotherapy | (dyrskjøt2023bladdercancer pages 1-3, lopezbeltran2024advancesindiagnosis pages 1-1) |
| MIBC (cisplatin-ineligible or selected bladder preservation) | Bladder-preserving multimodality therapy | TURBT + chemoradiation / trimodality therapy | Maximal resection plus radiosensitizing systemic therapy and radiation | Alternative to cystectomy for selected localized MIBC | Recognized standard bladder-preservation approach in suitable patients; exact response rate not listed in available contexts | Guideline-supported standard in selected patients | MAXO: combined modality therapy; radiochemotherapy; bladder preservation therapy | (dyrskjøt2023bladdercancer pages 1-3, lopezbeltran2024advancesindiagnosis pages 1-1) |
| MIBC (adjuvant) | Immunotherapy | Nivolumab | PD-1 checkpoint blockade | High-risk muscle-invasive urothelial carcinoma after radical surgery | CheckMate-274 described as showing disease-free survival benefit | FDA-approved adjuvant therapy | MAXO: adjuvant immunotherapy; nivolumab administration | (kolawa2023overviewdiagnosisand pages 1-2, lopezbeltran2024advancesindiagnosis pages 1-1) |
| MIBC (neoadjuvant, investigational/expanding) | Chemo-immunotherapy | Gemcitabine + cisplatin + pembrolizumab | Cytotoxic chemotherapy plus PD-1 blockade | Investigational / phase 2 neoadjuvant approach for MIBC | In LCCC1520, 22/39 patients responded by pathologic downstaging | Investigational / not established standard from available contexts | MAXO: neoadjuvant chemoimmunotherapy; pembrolizumab administration | (lopezbeltran2024advancesindiagnosis pages 1-1) |
| Advanced / metastatic UC | First-line systemic chemotherapy | Cisplatin-based regimens | Platinum DNA crosslinking with combination cytotoxic therapy | Standard first-line treatment for cisplatin-eligible locally advanced/metastatic UC | Remains standard first-line option; exact ORR not given in available contexts | Established standard | MAXO: systemic chemotherapy; platinum-based chemotherapy | (thomas2024treatmentpatternsand pages 1-2, lopezbeltran2024advancesindiagnosis pages 1-1) |
| Advanced / metastatic UC | First-line systemic chemotherapy | Carboplatin-based regimens | Platinum-based cytotoxic therapy for cisplatin-ineligible patients | Front-line option for cisplatin-ineligible advanced UC | In a US cohort, carboplatin-containing regimens were the most common first-line therapy (30.9%) | Standard clinical option | MAXO: systemic chemotherapy; carboplatin administration | (thomas2024treatmentpatternsand pages 1-2) |
| Advanced / metastatic UC | Immunotherapy | Pembrolizumab, nivolumab, avelumab; PD-1/PD-L1 inhibitors as a class | Immune checkpoint blockade | Used after platinum progression; some agents used in cisplatin-ineligible disease or maintenance settings depending on label | In the US cohort, PD-1/PD-L1 inhibitors were 29.9% of first-line treatments and predominant in later lines (52.0% second line) | Multiple FDA approvals in UC settings | MAXO: immune checkpoint inhibitor therapy; PD-1 inhibitor therapy; PD-L1 inhibitor therapy | (thomas2024treatmentpatternsand pages 1-2, lopezbeltran2024advancesindiagnosis pages 1-1) |
| Advanced / metastatic UC | Targeted therapy | Erdafitinib | Pan-FGFR tyrosine kinase inhibitor targeting susceptible FGFR2/3 alterations | FGFR2/3-altered metastatic UC after prior therapy | Real-world response rate reported as 40%; median PFS 2.8 months; median OS 6.6 months | FDA-approved targeted therapy | MAXO: targeted molecular therapy; fibroblast growth factor receptor inhibitor therapy; erdafitinib administration | (peng2023targetedtherapiesin pages 1-2) |
| Advanced / metastatic UC | Antibody-drug conjugate | Enfortumab vedotin | Anti-Nectin-4 antibody linked to monomethyl auristatin E, delivering microtubule toxin to tumor cells | Advanced/metastatic UC after prior therapy; increasingly used in later lines | In US practice, adoption increased after 2019; 8.1% of second-line and 18.6% of third-line treatments in one cohort | FDA-approved | MAXO: antibody-drug conjugate therapy; enfortumab vedotin administration | (thomas2024treatmentpatternsand pages 1-2, peng2023targetedtherapiesin pages 1-2) |
| Advanced / metastatic UC | Antibody-drug conjugate | Sacituzumab govitecan | Anti-Trop-2 antibody linked to SN-38 (topoisomerase I inhibitor payload) | Later-line advanced/metastatic UC | In US practice, used in 0.5% of second-line and 4.0% of third-line treatments in one cohort, reflecting newer adoption | FDA-approved during study period context | MAXO: antibody-drug conjugate therapy; sacituzumab govitecan administration | (thomas2024treatmentpatternsand pages 1-2, peng2023targetedtherapiesin pages 1-2) |
| Advanced / metastatic UC | Immunotherapy +/or targeted sequencing-guided care | Biomarker-directed treatment selection (FGFR, PD-L1, ctDNA, DDR alterations) | Precision-oncology stratification | Increasingly relevant across metastatic disease to select patients for checkpoint blockade or FGFR inhibition | Reviews emphasize urgent need for better selection criteria rather than uniform benefit for all patients | Biomarker use partly established, partly evolving | MAXO: precision medicine treatment selection; molecularly guided therapy | (lopezbeltran2024advancesindiagnosis pages 1-1, peng2023targetedtherapiesin pages 1-2) |
| UTUC / invasive urothelial carcinoma | Perioperative chemotherapy | Platinum-based neoadjuvant or adjuvant chemotherapy | DNA-damaging cytotoxic therapy | High-grade upper tract urothelial carcinoma and invasive urothelial carcinoma | POUT trial summarized as DFS 70% vs 51% at 2 years for adjuvant platinum chemotherapy vs surveillance; retrospective pathologic response in UTUC neoadjuvant cohorts ~48% | Guideline-supported in selected patients | MAXO: adjuvant chemotherapy; neoadjuvant chemotherapy; nephroureterectomy-associated systemic therapy | (kolawa2023overviewdiagnosisand pages 1-2) |


*Table: This table summarizes stage-specific treatment modalities for transitional cell carcinoma/urothelial carcinoma, from NMIBC to metastatic disease. It links therapies to mechanisms, indications, efficacy signals, regulatory status, and suggested MAXO-style annotations for knowledge-base use.*

### Pharmacotherapy

**Intravesical Therapy (NMIBC):**
- **Bacillus Calmette-Guérin (BCG):** Gold standard immunotherapy for high-risk NMIBC; reduces recurrence and progression (lopezbeltran2024advancesindiagnosis pages 1-1) (MAXO: intravesical immunotherapy)
- **Intravesical chemotherapy:** Post-TURBT adjuvant (dyrskjøt2023bladdercancer pages 1-3, lopezbeltran2024advancesindiagnosis pages 1-1) (MAXO: intravesical chemotherapy)

**Systemic Chemotherapy:**
- **Cisplatin-based (gemcitabine/cisplatin):** Standard neoadjuvant for MIBC and first-line for metastatic UC (dyrskjøt2023bladdercancer pages 1-3, thomas2024treatmentpatternsand pages 1-2, lopezbeltran2024advancesindiagnosis pages 1-1) (MAXO: neoadjuvant chemotherapy, systemic platinum chemotherapy)
- **Carboplatin-based:** For cisplatin-ineligible patients; 30.9% of first-line treatments in US cohort (thomas2024treatmentpatternsand pages 1-2) (MAXO: carboplatin administration)

**Pharmacogenomics:**
- ERCC2 and DDR gene alterations predict cisplatin sensitivity (alahmadie2024molecularpathologyof pages 1-3)
- FGFR3 alterations predict erdafitinib eligibility (peng2023targetedtherapiesin pages 1-2)

### Advanced Therapeutics

**Immunotherapy:**
- **Checkpoint inhibitors (PD-1/PD-L1):** Pembrolizumab, nivolumab, avelumab, atezolizumab (thomas2024treatmentpatternsand pages 1-2, lopezbeltran2024advancesindiagnosis pages 1-1)
  - FDA-approved for post-platinum metastatic UC, BCG-unresponsive NMIBC (pembrolizumab), adjuvant MIBC (nivolumab) (kolawa2023overviewdiagnosisand pages 1-2, lopezbeltran2024advancesindiagnosis pages 1-1)
  - 29.9% of first-line, 52.0% of second-line treatments in US cohort (thomas2024treatmentpatternsand pages 1-2)
  - (MAXO: immune checkpoint inhibitor therapy, pembrolizumab/nivolumab/atezolizumab administration)

**Targeted Therapies:**
- **Erdafitinib:** Pan-FGFR inhibitor for FGFR2/3-altered metastatic UC (peng2023targetedtherapiesin pages 1-2)
  - Response rate 40%, median PFS 2.8 months, median OS 6.6 months (peng2023targetedtherapiesin pages 1-2)
  - Resistance mechanisms: second-site FGFR3 mutations, PI3K-mTOR pathway alterations, TP53/AKT1 mutations (peng2023targetedtherapiesin pages 1-2)
  - (MAXO: targeted molecular therapy, FGFR inhibitor therapy, erdafitinib administration)

**Antibody-Drug Conjugates (ADCs):**
- **Enfortumab vedotin (EV):** Anti-Nectin-4 ADC delivering auristatin E (thomas2024treatmentpatternsand pages 1-2, peng2023targetedtherapiesin pages 1-2)
  - FDA-approved; 8.1% of second-line, 18.6% of third-line in US cohort (thomas2024treatmentpatternsand pages 1-2)
  - (MAXO: antibody-drug conjugate therapy, enfortumab vedotin administration)
- **Sacituzumab govitecan (SG):** Anti-Trop-2 ADC with SN-38 payload (thomas2024treatmentpatternsand pages 1-2, peng2023targetedtherapiesin pages 1-2)
  - FDA-approved; 0.5% of second-line, 4.0% of third-line in US cohort (thomas2024treatmentpatternsand pages 1-2)
  - (MAXO: antibody-drug conjugate therapy, sacituzumab govitecan administration)

**Gene Therapy:**
- **Nadofaragene firadenovec (Adstiladrin):** Intravesical adenoviral IFN gene therapy for BCG-unresponsive NMIBC (lopezbeltran2024advancesindiagnosis pages 1-1) (MAXO: intravesical gene therapy)

### Surgical and Interventional

**Surgery:**
- **TURBT:** Initial management for NMIBC (lopezbeltran2024advancesindiagnosis pages 1-1) (MAXO: transurethral resection)
- **Radical cystectomy with lymphadenectomy:** Standard for MIBC (dyrskjøt2023bladdercancer pages 1-3, lopezbeltran2024advancesindiagnosis pages 1-1) (MAXO: cystectomy, lymph node dissection)
- **Radical nephroureterectomy (RNU):** Standard for high-grade UTUC (kolawa2023overviewdiagnosisand pages 1-2) (MAXO: nephroureterectomy)

**Bladder-Preserving Multimodality Therapy:**
- TURBT + chemoradiation for selected MIBC (dyrskjøt2023bladdercancer pages 1-3, lopezbeltran2024advancesindiagnosis pages 1-1) (MAXO: combined modality therapy, radiochemotherapy)

### Supportive and Rehabilitative

- Urinary diversion management (ileal conduit, neobladder care)
- Pain control, nutritional support for metastatic disease
- Psychosocial support for quality of life (lopezbeltran2024advancesindiagnosis pages 1-1)

### Treatment Outcomes and Resistance

**Response Rates:**
- Erdafitinib: 40% ORR but brief responses (median PFS 2.8 months) (peng2023targetedtherapiesin pages 1-2)
- Checkpoint inhibitors: Variable; biomarker selection needed (lopezbeltran2024advancesindiagnosis pages 1-1)

**Side Effects:**
- Erdafitinib: Dose reductions (38%) and interruptions (50%) common (peng2023targetedtherapiesin pages 1-2)
- BCG: Local bladder irritation, systemic BCG sepsis (rare)
- Chemotherapy: Myelosuppression, nephrotoxicity (cisplatin), neuropathy
- Immunotherapy: Immune-related adverse events (colitis, pneumonitis, endocrinopathies)

**Resistance Mechanisms:**
- FGFR inhibitors: Second-site FGFR3 mutations, PI3K-mTOR pathway activation, TP53/AKT1 mutations (peng2023targetedtherapiesin pages 1-2)
- Immunotherapy: PD-L1-negative tumors, low TMB, immunosuppressive TME (peng2023targetedtherapiesin pages 1-2)

### Treatment Attrition

In a US cohort of 7,260 advanced UC patients, only 37% progressed to second-line and 12% to third-line treatment, highlighting treatment attrition and need for more effective first-line therapies (thomas2024treatmentpatternsand pages 1-2).

---

## 13. PREVENTION

### Prevention Levels

**Primary Prevention:**
- **Tobacco control:** Smoking cessation programs, taxation, public education (hoogstraten2023globaltrendsin pages 1-2)
- **Occupational safety:** Reducing aromatic amine exposures in industrial settings (alouini2024riskfactorsassociated pages 1-2)
- **Water quality:** Monitoring and reducing chlorinated water byproducts (alouini2024riskfactorsassociated pages 1-2)
- **Air quality:** Reducing VOCs and PM2.5 pollution (alouini2024riskfactorsassociated pages 1-2)

**Secondary Prevention:**
- **Early detection:** Prompt hematuria investigation (hoogstraten2023globaltrendsin pages 1-2)
- **High-risk surveillance:** For hereditary syndromes (Lynch), occupational exposures (kolawa2023overviewdiagnosisand pages 1-2)

**Tertiary Prevention:**
- **Surveillance after TURBT:** Cystoscopy protocols to detect recurrence (dyrskjøt2023bladdercancer pages 1-3)
- **Adjuvant BCG or chemotherapy:** Prevents progression in NMIBC (lopezbeltran2024advancesindiagnosis pages 1-1)

### Screening

Population-based screening is not established. Awareness campaigns for hematuria as alarm symptom are public health priorities (hoogstraten2023globaltrendsin pages 1-2).

### Behavioral Interventions

- **Smoking cessation:** Most impactful modifiable risk factor (hoogstraten2023globaltrendsin pages 1-2)
- **Dietary modifications:** Reducing processed meat, increasing fruits/vegetables (evidence limited) (alouini2024riskfactorsassociated pages 1-2)

### Genetic Counseling

For patients with germline DDR gene variants or Lynch syndrome, genetic counseling addresses hereditary risk, family screening, and cascade testing (alahmadie2024molecularpathologyof pages 1-3).

### Public Health Interventions

- Tobacco control policies (WHO Framework Convention on Tobacco Control implementation) (hoogstraten2023globaltrendsin pages 1-2)
- Occupational health regulations for aromatic amine exposures (alouini2024riskfactorsassociated pages 1-2)
- Water safety standards and monitoring (alouini2024riskfactorsassociated pages 1-2)
- Environmental protection policies for air quality (alouini2024riskfactorsassociated pages 1-2)

---

## 14. OTHER SPECIES / NATURAL DISEASE

Natural disease in companion animals and wildlife was not extensively covered in the retrieved 2023-2024 human-focused literature. UC in dogs is recognized in veterinary oncology but was not detailed in the sources reviewed.

### Comparative Biology

Evolutionary conservation of DNA damage response, cell cycle control, and RTK signaling pathways across species supports translational research from animal models to human UC.

---

## 15. MODEL ORGANISMS

### Model Types

**Murine Models:**
- **Patient-derived xenograft (PDX) models:** Established from human UC tissue in immunodeficient mice (NSG); recapitulate tumor heterogeneity (lopezbeltran2024advancesindiagnosis pages 1-1)
- **Double-humanized models:** PDX tumors in humanized immune system mice for immunotherapy testing (lopezbeltran2024advancesindiagnosis pages 1-1)
- **Genetically engineered mouse models (GEMMs):** KRAS-driven bladder cancer initiation models combined with organoid technology (lopezbeltran2024advancesindiagnosis pages 1-1)
- **Chemically induced models:** N-butyl-N-(4-hydroxybutyl)nitrosamine (BBN) model for bladder carcinogenesis studies

**Cell Lines:**
- Human UC cell lines: T24, 5637, RT4, UMUC3, J82 (lopezbeltran2024advancesindiagnosis pages 1-1)
- PDX-derived cell lines (e.g., PDX257S) with aggressive/tumorigenic characteristics (lopezbeltran2024advancesindiagnosis pages 1-1)

**Organoid Models:**
- Patient-derived organoids in decellularized pig bladder scaffolds for drug screening; 83.3% reliability in predicting treatment responses (lopezbeltran2024advancesindiagnosis pages 1-1)
- GEMM-derived organoids for tumor evolution studies (lopezbeltran2024advancesindiagnosis pages 1-1)

**Zebrafish Models:**
- Zebrafish xenografts for rapid drug screening; zebrafish tumor xenograft (ZTX) approaches mentioned (lopezbeltran2024advancesindiagnosis pages 1-1)

### Genetic Models

- **Knockout/knock-in mice:** FGFR3 mutant, TP53/RB1 loss models
- **Conditional models:** Urothelium-specific Cre-lox systems
- **Humanized models:** For immune checkpoint and CAR-T studies

### Model Characteristics

**Phenotype Recapitulation:**
- PDX models preserve tumor heterogeneity, molecular subtypes, and patient-specific genomic features (lopezbeltran2024advancesindiagnosis pages 1-1)
- GEMMs recapitulate single-cell molecular features and cellular communication networks of human UC (lopezbeltran2024advancesindiagnosis pages 1-1)
- 3D organoid models in decellularized scaffolds mimic in vivo tumor architecture and drug response (83.3% predictive capacity vs. 33.3% for 2D culture) (lopezbeltran2024advancesindiagnosis pages 1-1)

**Model Limitations:**
- Lack of human immune system (addressed by humanized models) (lopezbeltran2024advancesindiagnosis pages 1-1)
- Absence of stromal/microenvironment components in some models (lopezbeltran2024advancesindiagnosis pages 1-1)
- Differences in mouse vs. human bladder anatomy and urothelial biology

### Applications

- Preclinical drug screening (immunotherapy, targeted therapy, ADCs) (lopezbeltran2024advancesindiagnosis pages 1-1)
- Tumor evolution and metastasis studies (lopezbeltran2024advancesindiagnosis pages 1-1)
- Biomarker validation
- Mechanisms of resistance research (peng2023targetedtherapiesin pages 1-2, lopezbeltran2024advancesindiagnosis pages 1-1)

### Resources

- **Mouse repositories:** Jackson Laboratory, Charles River
- **Cell line repositories:** ATCC, DSMZ
- **PDX consortia:** Academic cancer centers with PDX programs
- **Databases:** IMSR (International Mouse Strain Resource), Cellosaurus

---

## CITATIONS AND EVIDENCE SOURCES

This report synthesizes recent 2023-2024 peer-reviewed literature from high-impact journals including Nature Reviews, JAMA Network Open, BMJ, Cancer Discovery, Frontiers in Immunology, MedComm, Cancers, and others. Key evidence sources include:

- Comprehensive reviews on bladder cancer epidemiology, molecular pathology, and treatment (dyrskjøt2023bladdercancer pages 1-3, hoogstraten2023globaltrendsin pages 1-2, lopezbeltran2024advancesindiagnosis pages 1-1)
- Molecular classification studies (schwarzova2023molecularclassificationof pages 1-2, su2025reviewofrecent pages 1-3)
- Genomic profiling studies (alahmadie2024molecularpathologyof pages 1-3, peng2023targetedtherapiesin pages 1-2)
- Real-world treatment pattern analyses (thomas2024treatmentpatternsand pages 1-2)
- UTUC-specific guidelines and reviews (kolawa2023overviewdiagnosisand pages 1-2, pandolfo2024uppertracturothelial pages 1-2)
- Preclinical model development (lopezbeltran2024advancesindiagnosis pages 1-1)

All statistics and molecular data are derived from primary research articles, systematic reviews, and authoritative clinical guidelines published between 2023-2025.

---

## LIMITATIONS AND FUTURE DIRECTIONS

1. **Evidence Gaps:** Lifestyle factor associations with UC outcomes are understudied (hoogstraten2023globaltrendsin pages 1-2). Protective factor research is limited.

2. **Biomarker Validation:** While promising biomarkers (PD-L1, TMB, FGFR3, ctDNA) are emerging, prospective validation trials are needed to define optimal patient selection criteria (lopezbeltran2024advancesindiagnosis pages 1-1).

3. **Treatment Resistance:** Mechanisms of resistance to immunotherapy and targeted therapies require further elucidation to develop combination strategies (peng2023targetedtherapiesin pages 1-2, lopezbeltran2024advancesindiagnosis pages 1-1).

4. **Model Refinement:** Incorporating human immune and stromal components into preclinical models will improve translatability (lopezbeltran2024advancesindiagnosis pages 1-1).

5. **Health Disparities:** Cancer registry coverage is incomplete in low-resource regions, limiting global burden estimates (hoogstraten2023globaltrendsin pages 1-2).

6. **Personalized Medicine:** Integration of molecular subtyping, biomarker-driven therapy selection, and novel combination regimens represents the frontier of UC management (lopezbeltran2024advancesindiagnosis pages 1-1).

---

## CONCLUSION

Transitional cell carcinoma (urothelial carcinoma) is a molecularly heterogeneous disease with significant global health burden. Advances in genomic profiling, molecular classification, and targeted therapies are transforming UC management. Key priorities include tobacco control for primary prevention, development of less-invasive diagnostic biomarkers, improved patient selection for immunotherapy and targeted therapies, and continued research into resistance mechanisms and novel therapeutic combinations. The integration of precision medicine approaches promises to improve outcomes for patients across the disease spectrum from NMIBC to metastatic UC.

References

1. (alouini2024riskfactorsassociated pages 1-2): Souhail Alouini. Risk factors associated with urothelial bladder cancer. International Journal of Environmental Research and Public Health, 21:954, Jul 2024. URL: https://doi.org/10.3390/ijerph21070954, doi:10.3390/ijerph21070954. This article has 71 citations.

2. (kwon2025advancesintherapy pages 1-2): Whi-An Kwon, Ho Kyung Seo, Geehyun Song, Min-Kyung Lee, and Weon Seo Park. Advances in therapy for urothelial and non-urothelial subtype histologies of advanced bladder cancer: from etiology to current development. Biomedicines, Jan 2025. URL: https://doi.org/10.3390/biomedicines13010086, doi:10.3390/biomedicines13010086. This article has 16 citations.

3. (peng2023targetedtherapiesin pages 1-2): Mei Peng, Xuetong Chu, Yan Peng, Duo Li, Zhirong Zhang, Weifan Wang, Xiaochen Zhou, Di Xiao, and Xiaoping Yang. Targeted therapies in bladder cancer: signaling pathways, applications, and challenges. MedComm, Dec 2023. URL: https://doi.org/10.1002/mco2.455, doi:10.1002/mco2.455. This article has 35 citations.

4. (kolawa2023overviewdiagnosisand pages 1-2): Adam Kolawa, Anishka D’Souza, and Varsha Tulpule. Overview, diagnosis, and perioperative systemic therapy of upper tract urothelial carcinoma. Cancers, 15:4813, Sep 2023. URL: https://doi.org/10.3390/cancers15194813, doi:10.3390/cancers15194813. This article has 31 citations.

5. (dyrskjøt2023bladdercancer pages 1-3): Lars Dyrskjøt, Donna E. Hansel, Jason A. Efstathiou, Margaret A. Knowles, Matthew D. Galsky, Jeremy Teoh, and Dan Theodorescu. Bladder cancer. Nature Reviews Disease Primers, Oct 2023. URL: https://doi.org/10.1038/s41572-023-00468-9, doi:10.1038/s41572-023-00468-9. This article has 608 citations.

6. (pandolfo2024uppertracturothelial pages 1-2): Savio Domenico Pandolfo, Simone Cilio, Achille Aveta, Zhenjie Wu, Clara Cerrato, Luigi Napolitano, Francesco Lasorsa, Giuseppe Lucarelli, Paolo Verze, Salvatore Siracusano, Carmelo Quattrone, Matteo Ferro, Eugenio Bologna, Riccardo Campi, Francesco Del Giudice, Riccardo Bertolo, Daniele Amparore, Sara Palumbo, Celeste Manfredi, and Riccardo Autorino. Upper tract urothelial cancer: guideline of guidelines. Cancers, 16:1115, Mar 2024. URL: https://doi.org/10.3390/cancers16061115, doi:10.3390/cancers16061115. This article has 45 citations.

7. (lopezbeltran2024advancesindiagnosis pages 1-1): Antonio Lopez-Beltran, Michael S Cookson, Brendan J Guercio, and Liang Cheng. Advances in diagnosis and treatment of bladder cancer. BMJ, 384:e076743, Feb 2024. URL: https://doi.org/10.1136/bmj-2023-076743, doi:10.1136/bmj-2023-076743. This article has 569 citations and is from a domain leading peer-reviewed journal.

8. (schwarzova2023molecularclassificationof pages 1-2): Lucia Schwarzova, Zuzana Varchulova Novakova, Lubos Danisovic, and Stanislav Ziaran. Molecular classification of urothelial bladder carcinoma. Molecular Biology Reports, 50:7867-7877, Jul 2023. URL: https://doi.org/10.1007/s11033-023-08689-7, doi:10.1007/s11033-023-08689-7. This article has 43 citations and is from a peer-reviewed journal.

9. (su2025reviewofrecent pages 1-3): Peng Su, Ying Yang, and Hong Zheng. Review of recent molecular pathology of bladder urothelial carcinoma. Discover Oncology, Mar 2025. URL: https://doi.org/10.1007/s12672-025-02128-8, doi:10.1007/s12672-025-02128-8. This article has 2 citations.

10. (hoogstraten2023globaltrendsin pages 1-2): Lisa M. C. van Hoogstraten, Alina Vrieling, Antoine G. van der Heijden, Manolis Kogevinas, Anke Richters, and Lambertus A. Kiemeney. Global trends in the epidemiology of bladder cancer: challenges for public health and clinical practice. Nature Reviews Clinical Oncology, 20:287-304, Mar 2023. URL: https://doi.org/10.1038/s41571-023-00744-3, doi:10.1038/s41571-023-00744-3. This article has 417 citations and is from a domain leading peer-reviewed journal.

11. (alahmadie2024molecularpathologyof pages 1-3): Hikmat Al-Ahmadie and George J. Netto. Molecular pathology of urothelial carcinoma. Clinics in laboratory medicine, 44 2:181-198, Jun 2024. URL: https://doi.org/10.1016/j.cll.2023.08.010, doi:10.1016/j.cll.2023.08.010. This article has 18 citations and is from a peer-reviewed journal.

12. (thomas2024treatmentpatternsand pages 1-2): Vinay Mathew Thomas, Yeonjung Jo, Nishita Tripathi, Soumyajit Roy, Beverly Chigarira, Arshit Narang, Georges Gebrael, Chadi Hage Chehade, Nicolas Sayegh, Gliceida Galarza Fortuna, Richard Ji, Patrick Campbell, Haoran Li, Neeraj Agarwal, Sumati Gupta, and Umang Swami. Treatment patterns and attrition with lines of therapy for advanced urothelial carcinoma in the us. JAMA Network Open, 7:e249417, May 2024. URL: https://doi.org/10.1001/jamanetworkopen.2024.9417, doi:10.1001/jamanetworkopen.2024.9417. This article has 31 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Transitional_Cell_Carcinoma-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Transitional_Cell_Carcinoma-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](Transitional_Cell_Carcinoma-deep-research-falcon_artifacts/artifact-02.md)