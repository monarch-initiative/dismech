---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-30T09:06:28.496625'
end_time: '2026-06-30T09:28:15.316443'
duration_seconds: 1306.82
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Fatal Infantile Encephalocardiomyopathy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 37
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: Fatal_Infantile_Encephalocardiomyopathy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Fatal_Infantile_Encephalocardiomyopathy-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: Fatal_Infantile_Encephalocardiomyopathy-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Fatal Infantile Encephalocardiomyopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Fatal Infantile Encephalocardiomyopathy** covering all of the
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
- **Disease Name:** Fatal Infantile Encephalocardiomyopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Fatal Infantile Encephalocardiomyopathy** covering all of the
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


# Comprehensive Research Report: Fatal Infantile Encephalocardiomyopathy

---

## 1. Disease Information

### Overview

Fatal infantile encephalocardiomyopathy (also designated cardioencephalomyopathy, fatal infantile, due to cytochrome c oxidase deficiency type 1; CEMCOX1) is a severe autosomal recessive mitochondrial disorder caused by biallelic pathogenic variants in the *SCO2* gene. The disease was first recognized in 1999 when Papadopoulou et al. identified mutations in *SCO2* in three unrelated infants presenting with a distinctive combination of cardioencephalomyopathy and severe cytochrome c oxidase (COX; complex IV) deficiency (papadopoulou1999fatalinfantilecardioencephalomyopathy pages 1-2). The condition is characterized by neonatal or early infantile onset of hypertrophic cardiomyopathy, encephalopathy, muscular hypotonia, lactic acidosis, and respiratory failure, typically leading to death within the first months to year of life (pronicka2013thenaturalhistory pages 5-6, gurgelgiannetti2013mitochondrialcardioencephalomyopathydue pages 4-4).

### Key Identifiers

- **MONDO ID:** MONDO:0015487 (fatal infantile encephalocardiomyopathy) and MONDO:0011451 (cardioencephalomyopathy, fatal infantile, due to cytochrome c oxidase deficiency 1) (OpenTargets Search: -SCO2)
- **OMIM:** #604377 (Mitochondrial Complex IV Deficiency, Nuclear Type 2; MC4DN2)
- **Orphanet:** ORPHA:137675
- **Gene (OMIM):** SCO2 (604272)
- **Ensembl Gene ID:** ENSG00000284194 (OpenTargets Search: -SCO2)

### Synonyms and Alternative Names

- Fatal infantile cardioencephalomyopathy with COX deficiency
- SCO2-related cardioencephalomyopathy
- Mitochondrial complex IV deficiency, nuclear type 2 (MC4DN2)
- Fatal infantile hypertrophic cardioencephalomyopathy
- SCO2 deficiency

### Information Source

Disease-level information is derived from aggregated resources (OMIM, Orphanet, OpenTargets) and from individual patient case reports and case series in the primary literature.

---

## 2. Etiology

### Disease Causal Factors

Fatal infantile encephalocardiomyopathy is a monogenic (Mendelian) disorder caused by biallelic pathogenic variants in the nuclear-encoded *SCO2* gene (NM_005138). *SCO2* encodes a mitochondrial inner membrane metallochaperone protein (Sco2) that functions as a copper transporter essential for the assembly of the CuA site within the COX2 subunit of cytochrome c oxidase, the terminal enzyme of the mitochondrial electron transport chain (papadopoulou1999fatalinfantilecardioencephalomyopathy pages 1-2, rebelo2018sco2mutationscause pages 7-10). Loss of Sco2 function results in failure of COX assembly, leading to severe complex IV deficiency and impaired oxidative phosphorylation (papadopoulou1999fatalinfantilecardioencephalomyopathy pages 1-2, gurgelgiannetti2013mitochondrialcardioencephalomyopathydue pages 2-3).

### Genetic Risk Factors

The disease is caused exclusively by germline, biallelic pathogenic variants in *SCO2*. The most common pathogenic allele is the c.418G>A (p.Glu140Lys; E140K) missense variant, which is located adjacent to the conserved CXXXC copper-binding motif and is considered either a founder allele or a mutational hotspot, particularly frequent in European populations of Polish, Czech, and Slovak descent (sambuughin2013exomesequencingreveals pages 3-3, jaksch2001homozygosity(e140k)in pages 1-2, pronicka2013thenaturalhistory pages 1-2). The E140K variant is present on at least one allele in the vast majority (at least 42 of 43) of reported cases of SCO2 deficiency (sambuughin2013exomesequencingreveals pages 3-3). Other identified pathogenic variants include nonsense mutations (Q53X, R90X, W36X, T241X), missense variants (S225F, R173W, M177T, G193S, V160A, P233T), and intragenic deletions (papadopoulou1999fatalinfantilecardioencephalomyopathy pages 1-2, pronicka2013thenaturalhistory pages 4-5, sambuughin2013exomesequencingreveals pages 3-3).

### Environmental and Protective Factors

As a strictly genetic, autosomal recessive mitochondrial disorder, no environmental risk factors, lifestyle factors, or protective factors have been identified. No gene-environment interactions are known.

---

## 3. Phenotypes

### Clinical Phenotype Spectrum

The clinical presentation of SCO2 deficiency shows a genotype-phenotype correlation, as established in the largest cohort study of 36 Polish children (pronicka2013thenaturalhistory pages 4-5). Three major phenotypic groups have been delineated:

| Group | Genotype | Clinical phenotype name | Number of patients | Age of onset | Need for ventilation (%) | Key clinical features | Survival |
|---|---|---|---:|---|---:|---|---|
| 1 | Compound heterozygous **p.E140K** with null alleles (**p.Q53X**, **p.R90X**, **p.W36X**, or **p.T241X**) | Neonatal cardiomyopathic phenotype | 8 | At birth / neonatal | 87.5% | Neonatal hypertrophic cardiomyopathy, encephalomyopathy, lactic acidosis, profound muscle weakness with absent reflexes, hypertonic episodes, limb dystonia, nystagmus, convulsions; considered the classic severe phenotype (pronicka2013thenaturalhistory pages 5-6, pronicka2013thenaturalhistory pages 4-5) | Usually death before 4 months of age (pronicka2013thenaturalhistory pages 5-6) |
| 2 | Homozygous **p.E140K/p.E140K** | Infantile SMA-like / Leigh-like phenotype | 25 | **4.2 ± 1.4 months** | 62.2% | Hypotonia, progressive encephalopathy, peripheral neuropathy/SMA-like presentation, Leigh-like neuroimaging features, muscle weakness, absent reflexes, tremor/opsoclonus in some patients, cardiomyopathy less prominent than Group 1 (pronicka2013thenaturalhistory pages 4-5, jaksch2001homozygosity(e140k)in pages 6-7) | Longer survival than Group 1; delayed course in mid/late infancy, with reported survival around ~13 months in earlier E140K homozygotes and variable survival in cohort (jaksch2001homozygosity(e140k)in pages 6-7, jaksch2001homozygosity(e140k)in pages 3-6) |
| 3 | Compound heterozygous **p.E140K/p.M177T** | Milder encephalopathic phenotype | 3 | **11 ± 4.3 months** | Not reported in excerpt | Milder, nonspecific encephalomyopathy with delayed onset; less severe than cardiomyopathic and SMA-like groups; establishes genotype-phenotype correlation for **p.M177T** as a milder allele when paired with **p.E140K** (pronicka2013thenaturalhistory pages 4-5, pronicka2013thenaturalhistory pages 1-2) | **2–4 years** (pronicka2013thenaturalhistory pages 1-2) |


*Table: This table summarizes the three genotype-phenotype correlation groups reported by Pronicka et al. for 36 Polish children with SCO2 deficiency. It highlights how different allelic combinations, especially E140K with null alleles versus homozygous E140K or E140K/M177T, are associated with markedly different onset, severity, ventilation needs, and survival.*

### Detailed Phenotypic Features

The core phenotypic features and suggested HPO terms include:

- **Hypertrophic cardiomyopathy** (HP:0001639): The hallmark feature, particularly prominent in neonatal-onset cases. Obstructive forms have been reported. Severity is typically severe and progressive (jaksch2001homozygosity(e140k)in pages 1-2, pronicka2013thenaturalhistory pages 5-6).
- **Muscular hypotonia** (HP:0001252): Present from birth in 100% of neonatal-onset cases (pronicka2013thenaturalhistory pages 4-5, pronicka2013thenaturalhistory pages 5-6).
- **Lactic acidosis** (HP:0003128): Consistently present; elevated blood lactate (e.g., 5.1 mmol/L) and elevated lactate-to-pyruvate ratio (e.g., 25:1) reflecting impaired aerobic metabolism (verdijk2008phenotypicconsequencesof pages 1-2, gurgelgiannetti2013mitochondrialcardioencephalomyopathydue pages 2-3).
- **Respiratory insufficiency** (HP:0002093): Requiring mechanical ventilation in 87.5% of Group 1 and 62.2% of Group 2 patients (pronicka2013thenaturalhistory pages 4-5).
- **Encephalopathy** (HP:0001298): Progressive, with Leigh-like pattern on MRI including white matter involvement and basal ganglia lesions (jaksch2001homozygosity(e140k)in pages 1-2, gurgelgiannetti2013mitochondrialcardioencephalomyopathydue pages 2-3).
- **Spinal muscular atrophy-like phenotype** (HP:0007269): Neurogenic muscular atrophy resembling SMA, with absent reflexes and spinal cord atrophy (pronicka2013thenaturalhistory pages 5-6, gurgelgiannetti2013mitochondrialcardioencephalomyopathydue pages 4-4).
- **Seizures/convulsions** (HP:0001250): Reported in a subset of patients (pronicka2013thenaturalhistory pages 5-6).
- **Axonal sensorimotor neuropathy** (HP:0003390): Severe neuropathy documented in multiple cases (gurgelgiannetti2013mitochondrialcardioencephalomyopathydue pages 2-3).
- **Feeding difficulties** (HP:0011968): Common in neonatal-onset cases (jaksch2001homozygosity(e140k)in pages 1-2).
- **Nystagmus** (HP:0000639) and **dystonia** (HP:0001332): Reported particularly in neonatal cardiomyopathic group (pronicka2013thenaturalhistory pages 5-6).

### Quality of Life Impact

The disease has a devastating impact on quality of life. Affected infants are typically ventilator-dependent, immobile, and require continuous intensive care. Survival is measured in weeks to months for the most severe forms.

---

## 4. Genetic/Molecular Information

### Causal Gene

- **Gene:** *SCO2* (Synthesis of Cytochrome C Oxidase 2)
- **HGNC ID:** HGNC:10604
- **OMIM Gene:** 604272
- **Ensembl:** ENSG00000284194 (OpenTargets Search: -SCO2)
- **Chromosomal location:** 22q13.33
- **Gene function:** Encodes a mitochondrial inner membrane metallochaperone that delivers copper to the CuA site of COX2 during complex IV assembly (papadopoulou1999fatalinfantilecardioencephalomyopathy pages 1-2, rebelo2018sco2mutationscause pages 7-10)

### Pathogenic Variants

The following table summarizes the principal pathogenic variants:

| Variant name | Nucleotide change | Protein change | Variant type | Location relative to SCO2 copper-binding motif or functional region | Associated phenotype severity or pattern | Notes on frequency or founder effect | Key references |
|---|---|---|---|---|---|---|---|
| E140K | c.418G>A; historically also reported as G1541A | p.Glu140Lys | Missense | Adjacent to the conserved CXXXC copper-binding motif | Pathogenic in homozygous or compound heterozygous state; homozygotes tend to show relatively milder, delayed infantile SMA-like or Leigh-like disease, whereas compound heterozygotes with a null allele often show classic severe neonatal cardioencephalomyopathy | Most common SCO2 pathogenic allele in European ancestry; present in at least 42 of 43 reported cases in one review cohort; likely founder allele or hotspot; particularly frequent in Polish, Czech, and Slovak patients | (papadopoulou1999fatalinfantilecardioencephalomyopathy pages 1-2, sambuughin2013exomesequencingreveals pages 3-3, jaksch2001homozygosity(e140k)in pages 3-6, jaksch2001homozygosity(e140k)in pages 1-2, pronicka2013thenaturalhistory pages 1-2) |
| Q53X | c.157C>T | p.Gln53Ter | Nonsense | Upstream of conserved functional core; truncates protein before copper-handling region | Severe classic fatal infantile cardioencephalomyopathy when in trans with E140K; neonatal onset common | Recurrent null allele in early reports | (tay2004associationofmutations pages 1-2, papadopoulou1999fatalinfantilecardioencephalomyopathy pages 1-2) |
| R90X | not specified in retrieved context | p.Arg90Ter | Nonsense | Upstream of copper-binding region | Severe neonatal cardiomyopathic phenotype when paired with E140K | Reported as one of the null alleles in Polish cohort group 1 | (pronicka2013thenaturalhistory pages 4-5, pronicka2013thenaturalhistory pages 1-2) |
| W36X | not specified in retrieved context | p.Trp36Ter | Nonsense | Far upstream of copper-binding motif | Severe neonatal cardiomyopathic phenotype when paired with E140K | Rare null allele; grouped with severe neonatal presentations | (pronicka2013thenaturalhistory pages 4-5, pronicka2013thenaturalhistory pages 1-2) |
| T241X | not specified in retrieved context | p.Thr241Ter | Nonsense | Downstream of copper-binding motif but truncating before full mature protein function | Severe neonatal cardiomyopathic phenotype when paired with E140K | Rare null allele; grouped with severe neonatal presentations | (pronicka2013thenaturalhistory pages 4-5, pronicka2013thenaturalhistory pages 1-2) |
| S225F | c.1797C>T | p.Ser225Phe | Missense | Downstream of copper-binding motif in conserved region | Severe infantile fatal disease when in trans with E140K | One of the original pathogenic missense alleles described with classic disease | (papadopoulou1999fatalinfantilecardioencephalomyopathy pages 1-2, jaksch2001homozygosity(e140k)in pages 3-6) |
| R173W or R171W | not specified in retrieved context | p.Arg173Trp or p.Arg171Trp | Missense | Near but downstream of E140K and the copper-binding region | Associated with severe disease when compound heterozygous with E140K; exact codon differs by transcript or report convention | Reported in early series as a severe partner allele to E140K | (jaksch2001homozygosity(e140k)in pages 6-7, jaksch2001homozygosity(e140k)in pages 3-6) |
| M177T | not specified in retrieved context | p.Met177Thr | Missense | Downstream of copper-binding motif | Milder encephalopathic phenotype with later onset around 11 months and survival of roughly 2 to 4 years when in trans with E140K | Defines the mildest group in the Polish genotype-phenotype series | (pronicka2013thenaturalhistory pages 4-5, pronicka2013thenaturalhistory pages 1-2) |
| G193S | not specified in retrieved context | p.Gly193Ser | Missense | Downstream of copper-binding motif | Severe cardioencephalomyopathy reported; also used in patient-derived iPSC cardiomyocyte disease modeling | Noted in a consanguineous Indian family; important non-European recurrent allele | (hallas2018investigatingthecardiac pages 9-10, sambuughin2013exomesequencingreveals pages 3-3) |
| V160A | not specified in retrieved context | p.Val160Ala | Missense | Downstream of E140K, likely affecting folding rather than direct copper ligation | Severe loss-of-function allele associated with fatal infantile presentation | Novel mutation reported in a family with fatal infantile hyperthermia and SCO2 deficiency; absent from 47,500 public exomes at time of report | (sambuughin2013exomesequencingreveals pages 3-3) |
| P233T | not specified in retrieved context | p.Pro233Thr | Missense | Downstream conserved region; likely perturbs protein interactions | Severe loss-of-function allele associated with fatal infantile presentation | Novel mutation reported with V160A; absent from 47,500 public exomes at time of report | (sambuughin2013exomesequencingreveals pages 3-3) |


*Table: This table summarizes the principal SCO2 variants reported in fatal infantile encephalocardiomyopathy, highlighting their molecular class, relationship to the copper-binding region, and observed genotype-phenotype effects. It is useful for variant interpretation, especially the common founder-like E140K allele and the distinction between severe null-associated and milder M177T-associated genotypes.*

All pathogenic variants are germline, autosomal recessively inherited. The E140K variant, while not observed in large population databases at appreciable frequencies, is present in nearly all reported cases and may represent a founder allele in Central European populations (sambuughin2013exomesequencingreveals pages 3-3, pronicka2013thenaturalhistory pages 1-2). Functional consequence: all variants cause loss of function through either protein truncation (nonsense) or disruption of copper binding, protein folding, or protein stability (missense) (papadopoulou1999fatalinfantilecardioencephalomyopathy pages 1-2, verdijk2008phenotypicconsequencesof pages 1-2, sambuughin2013exomesequencingreveals pages 3-3).

### Modifier Genes

No modifier genes have been formally identified. However, the SCO2 protein is known to function as a homodimer, and the severity of COX deficiency may vary with different allelic combinations, suggesting functional heterogeneity at the protein level (jaksch2001homozygosity(e140k)in pages 6-7).

### Epigenetic Information

No specific epigenetic changes (DNA methylation, histone modifications) have been reported for this disorder.

---

## 5. Environmental Information

As a monogenic mitochondrial disorder, no environmental factors, lifestyle factors, or infectious agents are implicated in disease causation. The disease is entirely genetic in origin.

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways

The primary affected pathway is the **oxidative phosphorylation (OXPHOS) pathway**, specifically mitochondrial complex IV (cytochrome c oxidase) biogenesis. SCO2 is a copper metallochaperone that delivers copper (Cu+) to the CuA site within the COX2 subunit of cytochrome c oxidase (papadopoulou1999fatalinfantilecardioencephalomyopathy pages 1-2, rebelo2018sco2mutationscause pages 7-10). The copper delivery pathway involves COX17 → SCO1/SCO2/COA6 → COX2 CuA site. SCO2 additionally plays regulatory roles in cellular copper homeostasis beyond its direct role in COX assembly (jaksch2001homozygosity(e140k)in pages 1-2, leary2013novelmutationsin pages 2-4).

**Relevant KEGG pathways:** Oxidative phosphorylation (hsa00190); **Reactome:** Cytochrome c oxidase biogenesis.

### Cellular Processes

The causal chain from genetic defect to clinical manifestation proceeds as follows:

1. **Upstream trigger:** Biallelic *SCO2* mutations → reduced or absent functional Sco2 protein (verdijk2008phenotypicconsequencesof pages 1-2)
2. **Copper transport failure:** Impaired copper delivery to COX2 CuA site → disrupted CuA biogenesis (rebelo2018sco2mutationscause pages 7-10, papadopoulou1999fatalinfantilecardioencephalomyopathy pages 1-2)
3. **Complex IV assembly defect:** Loss of mtDNA-encoded COX subunits and accumulation of aberrant assembly intermediates → severe COX deficiency (papadopoulou1999fatalinfantilecardioencephalomyopathy pages 1-2, yang2010analysisofmouse pages 9-11)
4. **OXPHOS dysfunction:** Impaired electron transport chain → reduced ATP production → energy failure in high-demand tissues (hallas2018investigatingthecardiac pages 9-10, gurgelgiannetti2013mitochondrialcardioencephalomyopathydue pages 2-3)
5. **Metabolic derangement:** Shift to anaerobic glycolysis → lactic acidosis, elevated lactate/pyruvate ratio (verdijk2008phenotypicconsequencesof pages 1-2, gurgelgiannetti2013mitochondrialcardioencephalomyopathydue pages 2-3)
6. **Compensatory and pathological responses:**
   - Mitochondrial proliferation via PGC1α/AMPK signaling (hallas2018investigatingthecardiac pages 9-10)
   - Mitochondrial swelling, disorganized cristae, intramitochondrial vacuoles (hallas2018investigatingthecardiac pages 9-10)
   - Glycogen and lipid accumulation in cardiomyocytes and myocytes (hallas2018investigatingthecardiac pages 9-10, gurgelgiannetti2013mitochondrialcardioencephalomyopathydue pages 2-3)
   - Intracellular calcium overload → delayed afterdepolarizations and arrhythmias (hallas2018investigatingthecardiac pages 9-10, hallas2018investigatingthecardiac pages 9-9)
   - p53-dependent apoptosis in cardiac cells (martinezmorentin2015cardiacdeficiencyof pages 10-11)
7. **Clinical manifestation:** Hypertrophic cardiomyopathy, cardiac failure, encephalopathy, neuromuscular degeneration, respiratory failure (jaksch2001homozygosity(e140k)in pages 1-2, pronicka2013thenaturalhistory pages 5-6)

### Protein Dysfunction

The SCO2 protein contains a conserved CXXXC copper-binding motif essential for its metallochaperone function. The E140K mutation, located adjacent to this motif, disrupts copper binding properties and alters cellular copper metabolism, leading to significantly increased copper uptake in fibroblasts as a compensatory mechanism (jaksch2001homozygosity(e140k)in pages 1-2). In patient tissues, markedly decreased steady-state levels of fully assembled complex IV are observed, with loss of COX subunits I, II, and IV (papadopoulou1999fatalinfantilecardioencephalomyopathy pages 1-2, yang2010analysisofmouse pages 9-11).

### Metabolic Changes

Key biochemical abnormalities include:
- Elevated blood lactate and pyruvate (verdijk2008phenotypicconsequencesof pages 1-2)
- Reduced COX/complex IV enzyme activity (4–51% residual activity depending on genotype) (jaksch2001homozygosity(e140k)in pages 3-6)
- Reduced mitochondrial copper content despite normal total tissue copper (yang2010analysisofmouse pages 1-2)
- Secondary decrease in complex III activity (yang2010analysisofmouse pages 11-12)

**GO terms:** GO:0006123 (mitochondrial electron transport, cytochrome c to oxygen); GO:0005507 (copper ion binding); GO:0043005 (neuron projection); GO:0016226 (iron-sulfur cluster assembly)

**Cell types involved:** Cardiomyocytes (CL:0000746), skeletal muscle fibers (CL:0000190), motor neurons (CL:0000100), hepatocytes (CL:0000182)

---

## 7. Anatomical Structures Affected

### Organ Level

- **Primary organs:** Heart (UBERON:0000948), brain (UBERON:0000955), skeletal muscle (UBERON:0001134)
- **Secondary involvement:** Liver, kidney (in some variants), spinal cord (pronicka2013thenaturalhistory pages 5-6, jaksch2001homozygosity(e140k)in pages 1-2)
- **Body systems:** Cardiovascular system, nervous system, musculoskeletal system

### Tissue and Cell Level

- **Cardiac muscle** (UBERON:0001133): Hypertrophic changes, myofibrillary disorganization
- **Skeletal muscle** (UBERON:0001134): Neurogenic atrophy pattern, COX-deficient fibers
- **Cerebral white matter** (UBERON:0002437): Demyelination, Leigh-like changes on MRI
- **Basal ganglia** (UBERON:0002420): Lesions seen on neuroimaging
- **Spinal cord anterior horn cells** (UBERON:0002257): Neurogenic muscular atrophy (pronicka2013thenaturalhistory pages 5-6, jaksch2001homozygosity(e140k)in pages 1-2)

### Subcellular Level

- **Mitochondria** (GO:0005739): Enlarged with disorganized cristae, intramitochondrial vacuoles, compensatory proliferation
- **Mitochondrial inner membrane** (GO:0005743): Site of SCO2 localization and COX assembly
- **Mitochondrial intermembrane space** (GO:0005758): Copper trafficking pathway

---

## 8. Temporal Development

### Onset

- **Typical age of onset:** Neonatal (birth) in severe compound heterozygous cases (Group 1); 4.2 ± 1.4 months in homozygous E140K cases (Group 2); approximately 11 ± 4.3 months in milder compound heterozygous cases (Group 3) (pronicka2013thenaturalhistory pages 4-5).
- **Onset pattern:** Acute or subacute in the neonatal form; insidious in milder forms.
- The disease has been associated with early fetal lethality and spontaneous abortion in some families, suggesting possible prenatal onset (tay2004associationofmutations pages 1-2).

### Progression

- **Disease course:** Uniformly progressive and fatal in the classic form
- **Progression rate:** Rapid in neonatal cardiomyopathic form (death before 4 months); somewhat slower in E140K homozygotes (survival ~13 months); slowest in E140K/M177T compound heterozygotes (2–4 years) (pronicka2013thenaturalhistory pages 5-6, jaksch2001homozygosity(e140k)in pages 3-6, pronicka2013thenaturalhistory pages 1-2)
- **Duration:** Days to months in severe forms; up to 2–4 years in the mildest described genotype

---

## 9. Inheritance and Population

### Inheritance

- **Pattern:** Autosomal recessive (AR) (papadopoulou1999fatalinfantilecardioencephalomyopathy pages 1-2)
- **Penetrance:** Complete in biallelic pathogenic variant carriers
- **Expressivity:** Variable, strongly correlated with genotype (pronicka2013thenaturalhistory pages 4-5)
- **Genetic anticipation:** Not described
- **Consanguinity role:** Documented in some families, particularly with the G193S homozygous mutation in an Indian consanguineous family (sambuughin2013exomesequencingreveals pages 3-3)
- **Carrier frequency:** Not precisely determined; the E140K variant has been described as particularly frequent in Central European populations

### Founder Effects

The E140K (p.Glu140Lys) variant is present in nearly all reported European patients and is especially frequent in Czech, Slovak, and Polish populations, consistent with a founder effect or recurrent mutational hotspot (sambuughin2013exomesequencingreveals pages 3-3, pronicka2013thenaturalhistory pages 1-2). The G193S variant has been reported specifically in an Indian family (sambuughin2013exomesequencingreveals pages 3-3).

### Epidemiology

- **Prevalence/Incidence:** Not precisely determined. The disease is ultra-rare. At least 43 cases of Sco2 deficiency had been reported by 2013 (sambuughin2013exomesequencingreveals pages 3-3), and 36 Polish children were described in a single national cohort study (pronicka2013thenaturalhistory pages 4-5). SCO2 mutations represent one of the most common nuclear genetic causes of isolated COX deficiency in children (gurgelgiannetti2013mitochondrialcardioencephalomyopathydue pages 4-4, pronicka2013thenaturalhistory pages 1-2).
- **Sex ratio:** No consistent sex predilection reported in humans; sex-dependent onset differences observed in mouse models (yang2010analysisofmouse pages 6-7)
- **Geographic distribution:** Predominantly reported in European populations, with isolated cases in other populations (sambuughin2013exomesequencingreveals pages 3-3)

---

## 10. Diagnostics

### Clinical Tests

- **Biochemical:** Spectrophotometric measurement of mitochondrial respiratory chain enzyme activities in muscle and/or heart tissue reveals markedly decreased complex IV (COX) activity, often with mild decreases in complexes I and III. Residual COX activity ranges from 4–51% depending on genotype (jaksch2001homozygosity(e140k)in pages 3-6). Elevated blood lactate, pyruvate, and lactate/pyruvate ratio are characteristic (verdijk2008phenotypicconsequencesof pages 1-2).
- **Histochemistry:** Oxidative histochemistry of muscle biopsy shows COX-deficient fibers with neurogenic atrophy pattern (SMA-like). Mitochondrial proliferation and absence of COX activity on histochemical staining are characteristic (gurgelgiannetti2013mitochondrialcardioencephalomyopathydue pages 2-3).
- **Imaging:** Brain MRI shows Leigh-like changes including basal ganglia lesions and white matter abnormalities; echocardiography demonstrates hypertrophic cardiomyopathy, often of the left ventricle (jaksch2001homozygosity(e140k)in pages 1-2, gurgelgiannetti2013mitochondrialcardioencephalomyopathydue pages 2-3).
- **Electrophysiology:** EMG/nerve conduction studies may demonstrate neurogenic changes and axonal sensorimotor neuropathy (gurgelgiannetti2013mitochondrialcardioencephalomyopathydue pages 2-3).

### Genetic Testing

- **Recommended approach:** Next-generation sequencing (NGS) gene panels for mitochondrial disease or COX deficiency, or whole-exome sequencing (WES) (papadopoulou1999fatalinfantilecardioencephalomyopathy pages 1-2, sambuughin2013exomesequencingreveals pages 3-3)
- **Single gene testing:** *SCO2* Sanger sequencing targeting the E140K common variant as a first-line approach in patients with clinical suspicion of COX-deficient cardioencephalomyopathy
- **WES utility:** Has been successfully used to identify novel *SCO2* variants in atypical presentations (sambuughin2013exomesequencingreveals pages 3-3)
- **Mitochondrial DNA testing:** Indicated to exclude mtDNA-related causes of COX deficiency

### Differential Diagnosis

Key differential diagnoses include:
- Leigh syndrome (SURF1 mutations)
- Spinal muscular atrophy (SMN1 mutations)
- Other causes of infantile hypertrophic cardiomyopathy (e.g., Pompe disease, Noonan syndrome, Barth syndrome)
- Other nuclear-encoded COX assembly factor deficiencies (SCO1, COX10, COX15, COA6, COX18)
- mtDNA-related COX deficiencies (papadopoulou1999fatalinfantilecardioencephalomyopathy pages 1-2, gurgelgiannetti2013mitochondrialcardioencephalomyopathydue pages 2-3)

### Screening

Diagnosis of SCO2 mutations enables preimplantation or prenatal genetic diagnosis in subsequent pregnancies for carrier families (gurgelgiannetti2013mitochondrialcardioencephalomyopathydue pages 4-4).

---

## 11. Outcome/Prognosis

### Survival and Mortality

- **Prognosis:** Uniformly fatal in the classic neonatal cardiomyopathic form, with death typically occurring before 4 months of age (pronicka2013thenaturalhistory pages 5-6). Compound heterozygotes carrying E140K with a null allele have neonatal onset and survival of 1–6 months (jaksch2001homozygosity(e140k)in pages 3-6). Homozygous E140K patients may survive longer (median ~13 months) with delayed onset (jaksch2001homozygosity(e140k)in pages 3-6). The mildest described genotype (E140K/M177T) allows survival of 2–4 years (pronicka2013thenaturalhistory pages 1-2).
- **Cause of death:** Typically cardiac failure due to progressive hypertrophic cardiomyopathy, often compounded by respiratory failure and lactic acidosis (freisinger2004reversionofhypertrophic pages 12-13, jaksch2001homozygosity(e140k)in pages 1-2).

### Prognostic Factors

The strongest prognostic determinant is the genotype. Compound heterozygosity for E140K with a null allele (nonsense or deletion) portends the severest course; homozygous E140K is somewhat milder; and E140K/M177T is the mildest known combination (pronicka2013thenaturalhistory pages 4-5, pronicka2013thenaturalhistory pages 1-2).

---

## 12. Treatment

### Current Therapeutic Approaches

No curative treatment exists. Management is largely supportive:

- **Supportive care (MAXO:0000950):** Respiratory support including mechanical ventilation, nutritional support, seizure management (jaksch2001homozygosity(e140k)in pages 1-2)
- **Cardiac management:** Diuretics (furosemide, spironolactone); beta-blockers and calcium channel blockers (propranolol, verapamil) have shown limited benefit (freisinger2004reversionofhypertrophic pages 6-10, jaksch2001homozygosity(e140k)in pages 1-2)
- **Mitochondrial cofactor supplementation (MAXO:0001298):** Carnitine, riboflavin, coenzyme Q10, creatine, ascorbate have been administered empirically, without proven efficacy (freisinger2004reversionofhypertrophic pages 6-10, jaksch2001homozygosity(e140k)in pages 1-2)

### Copper Supplementation

Copper-histidine (Cu-His) supplementation has been explored as a targeted treatment rationale based on the copper transport function of SCO2:

- **In vitro evidence:** Cu-His rescued COX activity in SCO2-deficient myoblasts at concentrations up to 300 µM without visible toxicity (jaksch2001cytochromecoxidase pages 7-8).
- **Clinical experience:** One patient with homozygous E140K showed cardiac improvement (normalized ECG signs) after subcutaneous Cu-His (30 mg/kg/day for 60 days) followed by oral copper (140 mg/day), surviving to 42 months (freisinger2004reversionofhypertrophic pages 6-10, freisinger2004reversionofhypertrophic pages 1-3). However, two other patients treated at late disease stages showed no benefit, likely due to irreversible damage in post-mitotic tissues (jaksch2001cytochromecoxidase pages 7-8, jaksch2001homozygosity(e140k)in pages 6-7). The limited evidence suggests early treatment might be critical.

### Experimental/Emerging Therapies

- **Protein replacement therapy:** A TAT peptide-fused recombinant Sco2 fusion protein was developed and successfully transduced into patient fibroblasts, contributing to effective COX assembly and partial recovery of COX activity. In mice, radiolabeled fusion Sco2 protein was biodistributed to peripheral tissues and delivered to mitochondria (Miliotou et al. 2023, PMID: 36678773).
- **mRNA-based therapy:** An IVT-mRNA delivery platform using protein transduction domain technology was developed; PTD-IVT-mRNA of full-length *SCO2* was successfully transduced into patient fibroblasts, translated, imported into mitochondria, and processed to mature protein, achieving recovery of COX activity (Miliotou et al. 2023, PMID: 36678773).
- **NAD+-dependent approaches:** NAD+ precursors activating Sirt1 corrected the phenotype in the Sco2 KI/KO mouse model (Cerutti et al. 2014; Cell Metabolism).
- **No clinical trials** specific to SCO2-related cardioencephalomyopathy were identified in ClinicalTrials.gov.

---

## 13. Prevention

### Primary Prevention

- **Genetic counseling (MAXO:0000079):** Essential for carrier families; autosomal recessive inheritance means 25% recurrence risk for carrier parents (gurgelgiannetti2013mitochondrialcardioencephalomyopathydue pages 4-4)
- **Carrier screening:** Targeted *SCO2* E140K variant screening may be considered in Central European populations with family history

### Secondary Prevention

- **Prenatal diagnosis:** Available through chorionic villus sampling or amniocentesis when familial variants are known (gurgelgiannetti2013mitochondrialcardioencephalomyopathydue pages 4-4)
- **Preimplantation genetic diagnosis (PGD):** Feasible for known familial variants

### Tertiary Prevention

No established interventions to prevent disease complications once onset occurs.

---

## 14. Other Species / Natural Disease

No naturally occurring disease equivalent has been reported in companion animals or wildlife. The disorder is recognized exclusively in humans.

---

## 15. Model Organisms

Multiple model systems have been developed for SCO2 deficiency research:

| Species | Model type | Genetic modification | Key phenotypes | Recapitulation of human disease features | Limitations |
|---|---|---|---|---|---|
| *Mus musculus* | Constitutive knockout | Homozygous **Sco2** null allele | Embryonic lethal during early gestation; severe morphological abnormalities; profound COX deficiency (yang2010analysisofmouse pages 4-6, yang2010analysisofmouse pages 1-2) | Confirms that complete SCO2 loss is incompatible with development and supports essential SCO2 function in COX biogenesis, consistent with the severe loss-of-function nature of human disease (yang2010analysisofmouse pages 4-6, yang2010analysisofmouse pages 1-2) | Does not model postnatal cardioencephalomyopathy because homozygous null animals die before birth (yang2010analysisofmouse pages 4-6) |
| *Mus musculus* | Knock-in (KIKI) | Homozygous **Sco2 E129K/E129K** knock-in, corresponding to human **E140K** | Viable, fertile, normal lifespan; reduced COX activity; impaired complex IV assembly; reduced mitochondrial copper; muscle weakness and poor endurance, but relatively mild phenotype (yang2010analysisofmouse pages 7-9, yang2010analysisofmouse pages 11-12, yang2010analysisofmouse pages 1-2) | Models the common human founder-like E140K allele and reproduces biochemical defects, mitochondrial copper abnormalities, and muscle weakness seen in milder human SCO2 deficiency (yang2010analysisofmouse pages 11-12, yang2010analysisofmouse pages 1-2) | No overt cardiomyopathy or fatal infantile course; much milder than typical human fatal infantile encephalocardiomyopathy (yang2010analysisofmouse pages 7-9, yang2010analysisofmouse pages 4-6) |
| *Mus musculus* | Compound KI/KO (KIKO) | One **Sco2 E129K** knock-in allele plus one null allele | Viable; reduced COX activity in brain, muscle, heart, and liver; defective complex IV assembly with abnormal intermediates; reduced mitochondrial copper; poor treadmill performance, muscle weakness, sex-dependent onset; no significant cardiac dysfunction (yang2010analysisofmouse pages 6-7, yang2010analysisofmouse pages 9-11, yang2010analysisofmouse pages 1-2) | Best murine approximation of human compound-heterozygous disease; captures respiratory chain deficiency, assembly defects, tissue vulnerability, and functional myopathy (yang2010analysisofmouse pages 6-7, yang2010analysisofmouse pages 9-11, yang2010analysisofmouse pages 1-2) | Fails to reproduce the hallmark infantile hypertrophic cardiomyopathy and early lethality of the human disorder (yang2010analysisofmouse pages 6-7, yang2010analysisofmouse pages 7-9) |
| *Drosophila melanogaster* | Cardiac-specific knockdown | Cardiac-specific **scox** knockdown | Severe dilated cardiomyopathy, enlarged conical chamber size, myofibrillary disorganization, mitochondrial dysfunction, p53-dependent apoptosis; cardiac phenotype rescued by dominant-negative p53 (martinezmorentin2015cardiacdeficiencyof pages 10-11) | Provides a tractable cardiac model linking SCO-family deficiency to mitochondrial dysfunction and cardiomyopathy mechanisms, especially apoptosis-driven cardiac injury (martinezmorentin2015cardiacdeficiencyof pages 10-11) | Cardiac phenotype is dilated rather than hypertrophic; insect heart biology differs substantially from human infant myocardium; does not model multisystem encephalopathy (martinezmorentin2015cardiacdeficiencyof pages 10-11) |
| *Homo sapiens* | Patient-derived cellular model | iPSC-derived cardiomyocytes from patients with **SCO2** mutations (including compound heterozygous **E140K** and homozygous **G193S**) | Major ultrastructural mitochondrial abnormalities, disorganized cristae, attenuated inotropic responses, delayed afterdepolarizations, increased beat-rate variability, impaired SR Ca2+ handling due to ATP shortage (hallas2018investigatingthecardiac pages 9-10, hallas2018investigatingthecardiac pages 9-9) | Closely models human cardiomyocyte-specific pathophysiology, including ATP deficiency, calcium dysregulation, arrhythmogenicity, and mitochondrial structural defects relevant to hypertrophic cardiomyopathy (hallas2018investigatingthecardiac pages 9-10, hallas2018investigatingthecardiac pages 9-9) | In vitro system lacks whole-organism developmental, neurologic, and survival phenotypes; cannot model systemic disease progression or tissue-tissue interactions (hallas2018investigatingthecardiac pages 9-10, hallas2018investigatingthecardiac pages 9-9) |


*Table: This table summarizes the principal in vivo and cellular models used to study SCO2-related fatal infantile encephalocardiomyopathy. It highlights what each model captures about human disease and where each model falls short, which is useful for interpreting mechanistic and translational studies.*

Key findings from model organisms include the demonstration that complete Sco2 loss is embryonic lethal in mice (yang2010analysisofmouse pages 4-6), that partial loss causes COX deficiency and muscle weakness but not cardiomyopathy in mice (yang2010analysisofmouse pages 7-9), and that cardiac-specific scox knockdown in *Drosophila* produces p53-dependent apoptosis and dilated cardiomyopathy (martinezmorentin2015cardiacdeficiencyof pages 10-11). Patient-derived iPSC cardiomyocytes have provided the most relevant insights into human cardiac pathophysiology, demonstrating ATP shortage, calcium dysregulation, and arrhythmogenesis (hallas2018investigatingthecardiac pages 9-10, hallas2018investigatingthecardiac pages 9-9).

---

## Summary

Fatal infantile encephalocardiomyopathy (MONDO:0015487) is an ultra-rare, autosomal recessive mitochondrial disorder caused by biallelic pathogenic variants in *SCO2*, encoding a copper metallochaperone essential for cytochrome c oxidase assembly. The disease presents with neonatal or early infantile onset of hypertrophic cardiomyopathy, progressive encephalopathy, muscular hypotonia, and lactic acidosis, with a uniformly fatal course in the most severe genotypes. The E140K variant serves as either a founder allele or mutational hotspot in European populations and is present on at least one allele in the vast majority of reported cases. Genotype-phenotype correlations are well-established, with compound heterozygosity for E140K and null alleles producing the most severe phenotype. Current treatment is limited to supportive care, with copper-histidine supplementation showing preliminary promise in a single case. Emerging protein replacement and mRNA-based therapeutic approaches are in preclinical development. No registered clinical trials were identified for this condition.

References

1. (papadopoulou1999fatalinfantilecardioencephalomyopathy pages 1-2): Lefkothea C. Papadopoulou, Carolyn M. Sue, Mercy M. Davidson, Kurenai Tanji, Ichizo Nishino, James E. Sadlock, Sindu Krishna, Winsome Walker, Jeanette Selby, D. Moira Glerum, Rudy Van Coster, Gilles Lyon, Emmanuel Scalais, Roger Lebel, Paige Kaplan, Sara Shanske, Darryl C. De Vivo, Eduardo Bonilla, Michio Hirano, Salvatore DiMauro, and Eric A. Schon. Fatal infantile cardioencephalomyopathy with cox deficiency and mutations in sco2, a cox assembly gene. Nature Genetics, 23:333-337, Nov 1999. URL: https://doi.org/10.1038/15513, doi:10.1038/15513. This article has 715 citations and is from a highest quality peer-reviewed journal.

2. (pronicka2013thenaturalhistory pages 5-6): Ewa Pronicka, Dorota Piekutowska-Abramczuk, Tamara Szymańska-Dębińska, Liliana Bielecka, Paweł Kowalski, Sylwia Łuczak, Agnieszka Karkucińska-Więckowska, Marek Migdał, Jolanta Kubalska, Janusz Zimowski, Ewa Jamroz, Jolanta Wierzba, Jolanta Sykut-Cegielska, Maciej Pronicki, Jacek Zaremba, and Małgorzata Krajewska-Walasek. The natural history of sco2 deficiency in 36 polish children confirmed the genotype-phenotype correlation. Mitochondrion, 13 6:810-6, Nov 2013. URL: https://doi.org/10.1016/j.mito.2013.05.007, doi:10.1016/j.mito.2013.05.007. This article has 33 citations and is from a peer-reviewed journal.

3. (gurgelgiannetti2013mitochondrialcardioencephalomyopathydue pages 4-4): Juliana Gurgel-Giannetti, Guilherme Oliveira, Geraldo Brasileiro Filho, Poliana Martins, Mariz Vainzof, and Michio Hirano. Mitochondrial cardioencephalomyopathy due to a novel sco2 mutation in a brazilian patient: case report and literature review. JAMA neurology, 70 2:258-61, Feb 2013. URL: https://doi.org/10.1001/jamaneurol.2013.595, doi:10.1001/jamaneurol.2013.595. This article has 19 citations and is from a highest quality peer-reviewed journal.

4. (OpenTargets Search: -SCO2): Open Targets Query (-SCO2, 9 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (rebelo2018sco2mutationscause pages 7-10): Adriana P Rebelo, Dimah Saade, Claudia V Pereira, Amjad Farooq, Tyler C Huff, Lisa Abreu, Carlos T Moraes, Diana Mnatsakanova, Kathy Mathews, Hua Yang, Eric A Schon, Stephan Zuchner, and Michael E Shy. Sco2 mutations cause early-onset axonal charcot-marie-tooth disease associated with cellular copper deficiency. Brain, 141:662–672, Mar 2018. URL: https://doi.org/10.1093/brain/awx369, doi:10.1093/brain/awx369. This article has 68 citations and is from a highest quality peer-reviewed journal.

6. (gurgelgiannetti2013mitochondrialcardioencephalomyopathydue pages 2-3): Juliana Gurgel-Giannetti, Guilherme Oliveira, Geraldo Brasileiro Filho, Poliana Martins, Mariz Vainzof, and Michio Hirano. Mitochondrial cardioencephalomyopathy due to a novel sco2 mutation in a brazilian patient: case report and literature review. JAMA neurology, 70 2:258-61, Feb 2013. URL: https://doi.org/10.1001/jamaneurol.2013.595, doi:10.1001/jamaneurol.2013.595. This article has 19 citations and is from a highest quality peer-reviewed journal.

7. (sambuughin2013exomesequencingreveals pages 3-3): Nyamkhishig Sambuughin, Xinyue Liu, Sunita Bijarnia, Tarina Wallace, Ishwar C Verma, Susan Hamilton, Sheila Muldoon, Luke J Tallon, and Shuishu Wang. Exome sequencing reveals sco2 mutations in a family presented with fatal infantile hyperthermia. Journal of Human Genetics, 58:226-228, Jan 2013. URL: https://doi.org/10.1038/jhg.2012.156, doi:10.1038/jhg.2012.156. This article has 15 citations and is from a peer-reviewed journal.

8. (jaksch2001homozygosity(e140k)in pages 1-2): M. Jaksch, Rita Horvath, Nina Horn, D. P. Auer, Carol Macmillan, J. Peters, K. Gerbitz, I. Kraegeloh-Mann, A. Muntau, V. Karcagi, R. Kalmanchey, Hanns Lochmüller, E. Shoubridge, and Peter Freisinger. Homozygosity (e140k) in sco2 causes delayed infantile onset of cardiomyopathy and neuropathy. Neurology, 57:1440-1446, Oct 2001. URL: https://doi.org/10.1212/wnl.57.8.1440, doi:10.1212/wnl.57.8.1440. This article has 114 citations and is from a highest quality peer-reviewed journal.

9. (pronicka2013thenaturalhistory pages 1-2): Ewa Pronicka, Dorota Piekutowska-Abramczuk, Tamara Szymańska-Dębińska, Liliana Bielecka, Paweł Kowalski, Sylwia Łuczak, Agnieszka Karkucińska-Więckowska, Marek Migdał, Jolanta Kubalska, Janusz Zimowski, Ewa Jamroz, Jolanta Wierzba, Jolanta Sykut-Cegielska, Maciej Pronicki, Jacek Zaremba, and Małgorzata Krajewska-Walasek. The natural history of sco2 deficiency in 36 polish children confirmed the genotype-phenotype correlation. Mitochondrion, 13 6:810-6, Nov 2013. URL: https://doi.org/10.1016/j.mito.2013.05.007, doi:10.1016/j.mito.2013.05.007. This article has 33 citations and is from a peer-reviewed journal.

10. (pronicka2013thenaturalhistory pages 4-5): Ewa Pronicka, Dorota Piekutowska-Abramczuk, Tamara Szymańska-Dębińska, Liliana Bielecka, Paweł Kowalski, Sylwia Łuczak, Agnieszka Karkucińska-Więckowska, Marek Migdał, Jolanta Kubalska, Janusz Zimowski, Ewa Jamroz, Jolanta Wierzba, Jolanta Sykut-Cegielska, Maciej Pronicki, Jacek Zaremba, and Małgorzata Krajewska-Walasek. The natural history of sco2 deficiency in 36 polish children confirmed the genotype-phenotype correlation. Mitochondrion, 13 6:810-6, Nov 2013. URL: https://doi.org/10.1016/j.mito.2013.05.007, doi:10.1016/j.mito.2013.05.007. This article has 33 citations and is from a peer-reviewed journal.

11. (jaksch2001homozygosity(e140k)in pages 6-7): M. Jaksch, Rita Horvath, Nina Horn, D. P. Auer, Carol Macmillan, J. Peters, K. Gerbitz, I. Kraegeloh-Mann, A. Muntau, V. Karcagi, R. Kalmanchey, Hanns Lochmüller, E. Shoubridge, and Peter Freisinger. Homozygosity (e140k) in sco2 causes delayed infantile onset of cardiomyopathy and neuropathy. Neurology, 57:1440-1446, Oct 2001. URL: https://doi.org/10.1212/wnl.57.8.1440, doi:10.1212/wnl.57.8.1440. This article has 114 citations and is from a highest quality peer-reviewed journal.

12. (jaksch2001homozygosity(e140k)in pages 3-6): M. Jaksch, Rita Horvath, Nina Horn, D. P. Auer, Carol Macmillan, J. Peters, K. Gerbitz, I. Kraegeloh-Mann, A. Muntau, V. Karcagi, R. Kalmanchey, Hanns Lochmüller, E. Shoubridge, and Peter Freisinger. Homozygosity (e140k) in sco2 causes delayed infantile onset of cardiomyopathy and neuropathy. Neurology, 57:1440-1446, Oct 2001. URL: https://doi.org/10.1212/wnl.57.8.1440, doi:10.1212/wnl.57.8.1440. This article has 114 citations and is from a highest quality peer-reviewed journal.

13. (verdijk2008phenotypicconsequencesof pages 1-2): Rob M. Verdijk, Ronald de Krijger, Kees Schoonderwoerd, Valeria Tiranti, Hubert Smeets, Lutgarde C.P. Govaerts, and René de Coo. Phenotypic consequences of a novel sco2 gene mutation. American Journal of Medical Genetics Part A, 146A:2822-2827, Nov 2008. URL: https://doi.org/10.1002/ajmg.a.32523, doi:10.1002/ajmg.a.32523. This article has 32 citations.

14. (tay2004associationofmutations pages 1-2): Stacey K. H. Tay, Sara Shanske, Paige Kaplan, and Salvatore DiMauro. Association of mutations in sco2, a cytochrome c oxidase assembly gene, with early fetal lethality. Archives of neurology, 61 6:950-2, Jun 2004. URL: https://doi.org/10.1001/archneur.61.6.950, doi:10.1001/archneur.61.6.950. This article has 58 citations.

15. (hallas2018investigatingthecardiac pages 9-10): Tova Hallas, Binyamin Eisen, Yuval Shemer, Ronen Ben Jehuda, Lucy N. Mekies, Shulamit Naor, Revital Schick, Sivan Eliyahu, Irina Reiter, Eugene Vlodavsky, Yeshayahu (Shai) Katz, Katrin Õunap, Avraham Lorber, Richard Rodenburg, Hanna Mandel, Mihaela Gherghiceanu, and Ofer Binah. Investigating the cardiac pathology of sco2‐mediated hypertrophic cardiomyopathy using patients induced pluripotent stem cell–derived cardiomyocytes. Journal of Cellular and Molecular Medicine, 22:913-925, Nov 2018. URL: https://doi.org/10.1111/jcmm.13392, doi:10.1111/jcmm.13392. This article has 35 citations and is from a peer-reviewed journal.

16. (leary2013novelmutationsin pages 2-4): Scot C. Leary, Hana Antonicka, Florin Sasarman, Woranontee Weraarpachai, Paul A. Cobine, Min Pan, Garry K. Brown, Ruth Brown, Jacek Majewski, Kevin C. H. Ha, Shamima Rahman, and Eric A. Shoubridge. Novel mutations in sco1 as a cause of fatal infantile encephalopathy and lactic acidosis. Human Mutation, 34:1366-1370, Oct 2013. URL: https://doi.org/10.1002/humu.22385, doi:10.1002/humu.22385. This article has 56 citations and is from a domain leading peer-reviewed journal.

17. (yang2010analysisofmouse pages 9-11): Hua Yang, Sonja Brosel, Rebeca Acin-Perez, Vesna Slavkovich, Ichizo Nishino, Raffay Khan, Ira J. Goldberg, Joseph Graziano, Giovanni Manfredi, and Eric A. Schon. Analysis of mouse models of cytochrome c oxidase deficiency owing to mutations in sco2. Human molecular genetics, 19 1:170-80, Oct 2010. URL: https://doi.org/10.1093/hmg/ddp477, doi:10.1093/hmg/ddp477. This article has 94 citations and is from a domain leading peer-reviewed journal.

18. (hallas2018investigatingthecardiac pages 9-9): Tova Hallas, Binyamin Eisen, Yuval Shemer, Ronen Ben Jehuda, Lucy N. Mekies, Shulamit Naor, Revital Schick, Sivan Eliyahu, Irina Reiter, Eugene Vlodavsky, Yeshayahu (Shai) Katz, Katrin Õunap, Avraham Lorber, Richard Rodenburg, Hanna Mandel, Mihaela Gherghiceanu, and Ofer Binah. Investigating the cardiac pathology of sco2‐mediated hypertrophic cardiomyopathy using patients induced pluripotent stem cell–derived cardiomyocytes. Journal of Cellular and Molecular Medicine, 22:913-925, Nov 2018. URL: https://doi.org/10.1111/jcmm.13392, doi:10.1111/jcmm.13392. This article has 35 citations and is from a peer-reviewed journal.

19. (martinezmorentin2015cardiacdeficiencyof pages 10-11): Leticia Martínez-Morentin, Lidia Martínez, Sarah Piloto, Hua Yang, Eric A. Schon, Rafael Garesse, Rolf Bodmer, Karen Ocorr, Margarita Cervera, and Juan J. Arredondo. Cardiac deficiency of single cytochrome oxidase assembly factor scox induces p53-dependent apoptosis in a drosophila cardiomyopathy model. Human molecular genetics, 24 13:3608-22, Mar 2015. URL: https://doi.org/10.1093/hmg/ddv106, doi:10.1093/hmg/ddv106. This article has 28 citations and is from a domain leading peer-reviewed journal.

20. (yang2010analysisofmouse pages 1-2): Hua Yang, Sonja Brosel, Rebeca Acin-Perez, Vesna Slavkovich, Ichizo Nishino, Raffay Khan, Ira J. Goldberg, Joseph Graziano, Giovanni Manfredi, and Eric A. Schon. Analysis of mouse models of cytochrome c oxidase deficiency owing to mutations in sco2. Human molecular genetics, 19 1:170-80, Oct 2010. URL: https://doi.org/10.1093/hmg/ddp477, doi:10.1093/hmg/ddp477. This article has 94 citations and is from a domain leading peer-reviewed journal.

21. (yang2010analysisofmouse pages 11-12): Hua Yang, Sonja Brosel, Rebeca Acin-Perez, Vesna Slavkovich, Ichizo Nishino, Raffay Khan, Ira J. Goldberg, Joseph Graziano, Giovanni Manfredi, and Eric A. Schon. Analysis of mouse models of cytochrome c oxidase deficiency owing to mutations in sco2. Human molecular genetics, 19 1:170-80, Oct 2010. URL: https://doi.org/10.1093/hmg/ddp477, doi:10.1093/hmg/ddp477. This article has 94 citations and is from a domain leading peer-reviewed journal.

22. (yang2010analysisofmouse pages 6-7): Hua Yang, Sonja Brosel, Rebeca Acin-Perez, Vesna Slavkovich, Ichizo Nishino, Raffay Khan, Ira J. Goldberg, Joseph Graziano, Giovanni Manfredi, and Eric A. Schon. Analysis of mouse models of cytochrome c oxidase deficiency owing to mutations in sco2. Human molecular genetics, 19 1:170-80, Oct 2010. URL: https://doi.org/10.1093/hmg/ddp477, doi:10.1093/hmg/ddp477. This article has 94 citations and is from a domain leading peer-reviewed journal.

23. (freisinger2004reversionofhypertrophic pages 12-13): P. Freisinger, R. Horvath, C. Macmillan, J. Peters, and M. Jaksch. Reversion of hypertrophic cardiomyopathy in a patient with deficiency of the mitochondrial copper binding protein sco2: is there a potential effect of copper? Journal of Inherited Metabolic Disease, 27:67-79, Mar 2004. URL: https://doi.org/10.1023/b:boli.0000016614.47380.2f, doi:10.1023/b:boli.0000016614.47380.2f. This article has 94 citations and is from a peer-reviewed journal.

24. (freisinger2004reversionofhypertrophic pages 6-10): P. Freisinger, R. Horvath, C. Macmillan, J. Peters, and M. Jaksch. Reversion of hypertrophic cardiomyopathy in a patient with deficiency of the mitochondrial copper binding protein sco2: is there a potential effect of copper? Journal of Inherited Metabolic Disease, 27:67-79, Mar 2004. URL: https://doi.org/10.1023/b:boli.0000016614.47380.2f, doi:10.1023/b:boli.0000016614.47380.2f. This article has 94 citations and is from a peer-reviewed journal.

25. (jaksch2001cytochromecoxidase pages 7-8): M. Jaksch, C. Paret, R. Stucka, N. Horn, J. Müller‐Höcker, R. Horvath, N. Trepesch, G. Stecker, P. Freisinger, C. Thirion, J. Müller, R. Lunkwitz, G. Rödel, E. Shoubridge, and Hanns Lochmüller. Cytochrome c oxidase deficiency due to mutations in sco2, encoding a mitochondrial copper-binding protein, is rescued by copper in human myoblasts. Human molecular genetics, 10 26:3025-35, Dec 2001. URL: https://doi.org/10.1093/hmg/10.26.3025, doi:10.1093/hmg/10.26.3025. This article has 171 citations and is from a domain leading peer-reviewed journal.

26. (freisinger2004reversionofhypertrophic pages 1-3): P. Freisinger, R. Horvath, C. Macmillan, J. Peters, and M. Jaksch. Reversion of hypertrophic cardiomyopathy in a patient with deficiency of the mitochondrial copper binding protein sco2: is there a potential effect of copper? Journal of Inherited Metabolic Disease, 27:67-79, Mar 2004. URL: https://doi.org/10.1023/b:boli.0000016614.47380.2f, doi:10.1023/b:boli.0000016614.47380.2f. This article has 94 citations and is from a peer-reviewed journal.

27. (yang2010analysisofmouse pages 4-6): Hua Yang, Sonja Brosel, Rebeca Acin-Perez, Vesna Slavkovich, Ichizo Nishino, Raffay Khan, Ira J. Goldberg, Joseph Graziano, Giovanni Manfredi, and Eric A. Schon. Analysis of mouse models of cytochrome c oxidase deficiency owing to mutations in sco2. Human molecular genetics, 19 1:170-80, Oct 2010. URL: https://doi.org/10.1093/hmg/ddp477, doi:10.1093/hmg/ddp477. This article has 94 citations and is from a domain leading peer-reviewed journal.

28. (yang2010analysisofmouse pages 7-9): Hua Yang, Sonja Brosel, Rebeca Acin-Perez, Vesna Slavkovich, Ichizo Nishino, Raffay Khan, Ira J. Goldberg, Joseph Graziano, Giovanni Manfredi, and Eric A. Schon. Analysis of mouse models of cytochrome c oxidase deficiency owing to mutations in sco2. Human molecular genetics, 19 1:170-80, Oct 2010. URL: https://doi.org/10.1093/hmg/ddp477, doi:10.1093/hmg/ddp477. This article has 94 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Fatal_Infantile_Encephalocardiomyopathy-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Fatal_Infantile_Encephalocardiomyopathy-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](Fatal_Infantile_Encephalocardiomyopathy-deep-research-falcon_artifacts/artifact-02.md)