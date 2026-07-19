---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-05T18:50:34.400227'
end_time: '2026-07-05T19:13:52.012141'
duration_seconds: 1397.61
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Small Cell Lung Cancer
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 48
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: Small_Cell_Lung_Cancer-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Small_Cell_Lung_Cancer-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: Small_Cell_Lung_Cancer-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Small Cell Lung Cancer
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Small Cell Lung Cancer** covering all of the
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
- **Disease Name:** Small Cell Lung Cancer
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Small Cell Lung Cancer** covering all of the
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


# Comprehensive Research Report: Small Cell Lung Cancer (SCLC)

---

## 1. Disease Information

### Overview
Small cell lung cancer (SCLC) is a highly aggressive neuroendocrine malignancy accounting for approximately 10–15% of all lung cancers (zugazagoitia2024factsandhopes pages 1-1, redin2024smallcelllung pages 1-3). It is characterized by rapid growth, high metastatic capacity, early dissemination, and a strong epidemiologic and biologic association with tobacco carcinogens (megyesfalvi2023clinicalinsightsinto pages 1-2). Although SCLC is initially highly responsive to platinum-based chemotherapy, these responses are transient, and approximately 90% of patients experience rapid disease recurrence (redin2024smallcelllung pages 1-3). The 5-year survival rate remains dismally low at approximately 5–7% (huang2025molecularsubtypesand pages 1-2, redin2024smallcelllung pages 1-3).

### Key Identifiers
- **MONDO ID:** MONDO:0008433 (small cell lung carcinoma) (OpenTargets Search: small cell lung cancer)
- **ICD-10:** C34 (malignant neoplasm of bronchus and lung; SCLC specified as small cell carcinoma)
- **ICD-O-3 Morphology:** 8041/3 (small cell carcinoma, NOS)
- **MeSH:** D055752 (Small Cell Lung Carcinoma)
- **Orphanet:** ORPHA:70573

### Synonyms and Alternative Names
Common synonyms include: small cell carcinoma of the lung, oat cell carcinoma, small cell undifferentiated carcinoma, and neuroendocrine carcinoma of the lung (small cell type). SCLC is classified among high-grade pulmonary neuroendocrine neoplasms.

### Data Sources
Information in this report is derived from aggregated disease-level resources including comprehensive peer-reviewed reviews, SEER database analyses, clinical trial registries, and the OpenTargets Platform.

---

## 2. Etiology

### Disease Causal Factors
The dominant causal factor in SCLC is **tobacco smoke exposure**. SCLC has the strongest epidemiologic link to tobacco carcinogens among all lung cancer subtypes, with the vast majority of patients being current or former heavy smokers (megyesfalvi2023clinicalinsightsinto pages 1-2). Genomically, SCLC is characterized by near-universal inactivation of the tumor suppressor genes **TP53** (~92% of cases) and **RB1** (~74%), which represent the initial steps in malignant transformation (redin2024smallcelllung pages 1-3). Additional recurrent genetic alterations include inactivating mutations in **PTEN**, **CREBBP**, **EP300**, **KMT2D**, **NOTCH** family genes, and activating mutations in **PIK3CA** (megyesfalvi2023clinicalinsightsinto pages 5-5, OpenTargets Search: small cell lung cancer). MYC family amplification (MYC, MYCL, MYCN) is also frequent (megyesfalvi2023clinicalinsightsinto pages 5-5).

### Risk Factors
**Genetic risk factors:** TP53 and RB1 co-alteration is the defining molecular event essential for SCLC pathogenesis (huang2025molecularsubtypesand pages 1-2, redin2024smallcelllung pages 1-3). An integrative analysis of 3,600 real-world SCLC cases identified new genetic subtypes including STK11-mutant tumors (1.7%) and TP53/RB1 wild-type tumors (5.5%), of which 12.7% were HPV-positive. CCNE1 amplification was associated with decreased overall survival, while 4q12 gene amplifications were associated with increased survival (OpenTargets Search: small cell lung cancer).

**Environmental risk factors:** Tobacco smoking is the predominant environmental risk factor. Additional environmental exposures including radon gas and air pollution contribute to lung cancer risk (huang2025molecularsubtypesand pages 1-2). The disease predominantly affects elderly male heavy smokers (huang2023incidencesurvivalcomparison pages 1-2).

### Protective Factors
Smoking cessation is the primary protective factor. The declining incidence of SCLC in the United States over the past two decades (48.6% decrease from 2000 to 2020) is attributed to reduced smoking rates (uprety2025trendsinthe pages 1-2, uprety2025trendsinthe pages 2-4).

---

## 3. Phenotypes

### Symptoms and Clinical Signs
SCLC commonly presents with centrally located hilar or mediastinal masses, cough, dyspnea, chest pain, hemoptysis, and weight loss. Due to its rapid doubling time and early metastatic spread, approximately 70–80% of patients present with extensive-stage (metastatic) disease at diagnosis (huang2025molecularsubtypesand pages 1-2, redin2024smallcelllung pages 1-3).

- **HPO:** HP:0002094 (Dyspnea), HP:0012735 (Cough), HP:0002105 (Hemoptysis), HP:0001824 (Weight loss)

### Paraneoplastic Syndromes
SCLC is notably associated with paraneoplastic syndromes due to its neuroendocrine differentiation. These include:
- **SIADH (Syndrome of Inappropriate Antidiuretic Hormone secretion)** — the most common paraneoplastic syndrome in SCLC
- **Lambert-Eaton Myasthenic Syndrome (LEMS)** — characterized by calcium-channel antibodies (megyesfalvi2023clinicalinsightsinto pages 27-27)
- **Cushing syndrome** — ectopic ACTH production
- **Anti-Hu antibody-related paraneoplastic syndromes** — presenting with progressive dysautonomia and neuropathy (megyesfalvi2023clinicalinsightsinto pages 27-27)

Patients with neurologic paraneoplastic syndromes have been associated with improved prognosis and increased tumor-infiltrating lymphocytes (megyesfalvi2023clinicalinsightsinto pages 27-27).

### Quality of Life Impact
SCLC profoundly impacts quality of life through rapid symptom progression, metastatic disease burden (particularly brain metastases), and treatment-related toxicity. The aggressive disease course and short survival significantly affect functional status and psychosocial well-being.

---

## 4. Genetic/Molecular Information

### Causal Genes and Pathogenic Variants
The genes coding for the tumor suppressors **p53** (TP53) and **retinoblastoma** (RB1) are inactivated in the vast majority of SCLC tumors. These two deleterious genetic events represent the initial steps in SCLC development, making them essential for a lung epithelial cell to progress toward malignancy (huang2025molecularsubtypesand pages 1-2, megyesfalvi2023clinicalinsightsinto pages 1-2). TP53 is mutated in approximately 92% of cases and RB1 in approximately 74% (redin2024smallcelllung pages 1-3).

Additional recurrently altered genes include:
- **PTEN** (pathway: PI3K-AKT-mTOR) — more frequent alterations in brain metastases (OpenTargets Search: small cell lung cancer)
- **CREBBP** and **EP300** — chromatin remodeling/histone acetyltransferase genes (OpenTargets Search: small cell lung cancer)
- **KMT2D** — lysine methyltransferase involved in epigenetic regulation (OpenTargets Search: small cell lung cancer)
- **NOTCH** family genes — tumor suppressive role in NE lineage (megyesfalvi2023clinicalinsightsinto pages 5-5)
- **PIK3CA** — activating mutations (megyesfalvi2023clinicalinsightsinto pages 5-5)
- **MYC/MYCL/MYCN** — amplifications driving aggressive phenotype (megyesfalvi2023clinicalinsightsinto pages 5-5)
- **SMARCA4** — catalytic subunit of SWI/SNF complex, mutations in 1.5–4% of cases (redin2024smarca4controlsstate pages 1-2)
- **KEAP1** — may contribute to SCLC pathogenesis (OpenTargets Search: small cell lung cancer)

### Molecular Subtypes
Recent multi-omic studies have revealed distinct molecular subtypes driven by lineage-defining transcription factors (huang2025molecularsubtypesand pages 1-2, redin2024smallcelllung pages 1-3):

| Subtype | Transcription factor / defining program | Approx. frequency | Neuroendocrine status | Key molecular features / pathway enrichment | Suggested targeted therapies / vulnerabilities |
|---|---|---:|---|---|---|
| SCLC-A | **ASCL1** | ~70% | NE-high | Canonical neuroendocrine subtype; enriched for **BCL2, DLL3, SOX2, RET, MYCL1** and ASCL1-driven lineage programs (redin2024smallcelllung pages 1-3, huang2025molecularsubtypesand pages 7-9, huang2025molecularsubtypesand pages 2-4) | **DLL3-targeting agents** (e.g., tarlatamab), **BCL2 inhibitors** (venetoclax), **LSD1 inhibitors**, **HDAC inhibitors**; RET/BCL2-directed strategies under study (huang2025molecularsubtypesand pages 7-9, patel2023smallcelllung pages 1-2) |
| SCLC-N | **NEUROD1** | ~15% | NE-high | More aggressive/proliferative state; associated with **MYC co-expression/amplification**, neuronal signaling, chemoresistance, and elevated **AURKA/AURKB** dependence (redin2024smallcelllung pages 1-3, huang2025molecularsubtypesand pages 7-9, huang2025molecularsubtypesand pages 2-4) | **Aurora kinase inhibitors** (e.g., alisertib), MYC-directed approaches, cell-cycle pathway targeting; IMPDH inhibitors proposed in review literature (huang2025molecularsubtypesand pages 7-9, huang2025molecularsubtypesand pages 2-4) |
| SCLC-P | **POU2F3** | 7–15% | NE-low / non-NE | Tuft-cell-like subtype; depends on **IGF1R signaling** and shows relative **DNA repair deficiencies**; transcriptomically distinct from classic NE SCLC (redin2024smallcelllung pages 1-3, huang2025molecularsubtypesand pages 2-4, redin2024smallcelllung pages 4-6) | **IGF1R inhibitors**, **PARP inhibitors**, DNA-damaging agents, SWI/SNF ATPase-directed approaches proposed for selected tumors (huang2025molecularsubtypesand pages 7-9, huang2025molecularsubtypesand pages 2-4) |
| SCLC-Y | **YAP1** (debated as stable subtype in some studies) | 3–10% | NE-low / non-NE | Linked to low-NE state, lineage plasticity, EMT/non-NE features, and therapy resistance; YAP/Notch/REST programs implicated. Some reviews note this category is biologically less stable or inconsistently reproduced across datasets (redin2024smallcelllung pages 1-3, huang2025molecularsubtypesand pages 2-4, redin2024smallcelllung pages 11-13, redin2024smallcelllung pages 13-14) | No single standard targeted therapy; candidate approaches include **ERBB pathway targeting** in specific low-NE/YAP-associated transitions and broader plasticity-directed/epigenetic strategies (huang2025molecularsubtypesand pages 13-15, redin2024smarca4controlsstate pages 1-2, redin2024smallcelllung pages 13-14) |
| SCLC-I | **Inflamed / immune program** rather than dominant ASCL1/NEUROD1/POU2F3 | Not firmly fixed; distinct subset | Often NE-low / inflamed | Characterized by **inflamed gene signatures**, higher **HLA/antigen-presentation**, immune checkpoint expression, mesenchymal features, and greater immune-cell infiltration versus NE-high “immune desert” tumors (zugazagoitia2024factsandhopes pages 1-1, megyesfalvi2023clinicalinsightsinto pages 6-7) | Greatest rationale for **immune checkpoint blockade**; biomarker-enriched immunotherapy strategies and combination immunotherapy approaches are emphasized (zugazagoitia2024factsandhopes pages 1-1, chen2024advancesinpredictive pages 2-4, megyesfalvi2023clinicalinsightsinto pages 6-7) |


*Table: This table summarizes the main molecular subtypes of small cell lung cancer, their defining transcriptional programs, approximate frequencies, biologic features, and leading therapeutic hypotheses. It is useful for mapping subtype biology to emerging precision-treatment strategies.*

### Epigenetic Information
Epigenetic regulation plays a critical role in SCLC biology. SMARCA4, the catalytic subunit of the SWI/SNF chromatin remodeling complex, controls neuroendocrine state plasticity by binding to ASCL1 and NEUROD1 gene loci and enhancing chromatin accessibility (redin2024smarca4controlsstate pages 1-2). State transitions in SCLC appear to be epigenetically rather than mutationally determined, with SMARCA4 inhibition inducing loss of NE features and activation of non-NE signaling pathways (redin2024smarca4controlsstate pages 1-2). DNA methylation patterns correlate with EZH2 expression and define clinically relevant subtypes (redin2024smallcelllung pages 11-13). CREBBP loss sensitizes tumors to HDAC inhibition (redin2024smallcelllung pages 13-14).

---

## 5. Environmental Information

### Environmental and Lifestyle Factors
Tobacco smoking is the dominant environmental risk factor, with SCLC having the strongest association with tobacco carcinogens among lung cancer subtypes (megyesfalvi2023clinicalinsightsinto pages 1-2). The declining incidence of SCLC directly parallels declining smoking rates in the United States, with the age-adjusted incidence rate dropping from 9 per 100,000 in 2000 to 4.6 per 100,000 in 2020 (uprety2025trendsinthe pages 1-2). Additional environmental exposures including radon gas and air pollution contribute to lung carcinogenesis risk (huang2025molecularsubtypesand pages 1-2).

### Infectious Agents
While not a primary etiologic factor, HPV-positive SCLC has been identified in a subset of TP53/RB1 wild-type tumors, with 12.7% of this uncommon genotype testing HPV-positive (OpenTargets Search: small cell lung cancer).

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways
SCLC pathogenesis involves multiple interconnected signaling cascades:
- **TP53/RB1 inactivation pathway:** Near-universal loss of both tumor suppressors eliminates cell cycle control and senescence barriers, enabling indefinite proliferation (papavassiliou2024p53andrb pages 4-5)
- **MYC signaling:** MYC amplification drives NE-low phenotype with high NEUROD1 expression and promotes subtype transition from SCLC-A to SCLC-N (megyesfalvi2023clinicalinsightsinto pages 5-5)
- **Notch signaling:** Activated by MYC, mediates NE plasticity and lineage switching (megyesfalvi2023clinicalinsightsinto pages 5-5)
- **BCL2 anti-apoptotic pathway:** Elevated BCL2 expression is a transcriptional target of ASCL1, suppressing apoptosis (megyesfalvi2023clinicalinsightsinto pages 5-5)
- **PI3K-AKT-mTOR pathway:** PTEN deletions and PIK3CA mutations activate this pro-survival cascade (megyesfalvi2023clinicalinsightsinto pages 5-5)
- **YAP/Notch/REST network:** Controls neuroendocrine cell fate determination (redin2024smallcelllung pages 11-13)

GO Terms: GO:0008283 (cell population proliferation), GO:0006915 (apoptotic process), GO:0007219 (Notch signaling pathway)

### Cellular Processes and Cell Types
SCLC can arise from multiple pulmonary cell types including basal cells, neuroendocrine cells, club cells, and alveolar type 2 (AT2) cells (redin2024smallcelllung pages 4-6). The SCLC-P subtype shows transcriptomic similarity to tuft cells, suggesting tuft cell precursors as a possible origin (redin2024smallcelllung pages 4-6). Neuroendocrine cells of the lung are characterized by dense-core granules and NE marker expression (megyesfalvi2023clinicalinsightsinto pages 5-5).

CL terms: CL:1000223 (lung neuroendocrine cell), CL:0000083 (epithelial cell of lung), CL:0002063 (type II pneumocyte)

### Immune Evasion Mechanisms
SCLC employs multiple immune evasion strategies:
- **T cell exclusion:** NE-high SCLCs are characterized as "immune desert" tumors with minimal infiltrating immune cells (megyesfalvi2023clinicalinsightsinto pages 6-7)
- **MHC-class I downregulation:** Reduced antigen processing and presentation machinery (zugazagoitia2024factsandhopes pages 1-1)
- **Surface glycolipid/glycoprotein overexpression:** GD2 ganglioside engages siglec7 on macrophages and NK cells to suppress immunity (zugazagoitia2024factsandhopes pages 2-3)
- **CD47 overexpression:** Inhibits macrophage-mediated phagocytosis through SIRPα binding (zugazagoitia2024factsandhopes pages 2-3)
- **PD-L1 upregulation:** T-cell checkpoint immune inhibitory signaling (zugazagoitia2024factsandhopes pages 2-3)

### Tumor Microenvironment
The SCLC tumor microenvironment is characterized by abundant, aggressively growing cancer cells that vastly outnumber immune cells, with minimal interdigitated tumor-associated immune stroma (zugazagoitia2024factsandhopes pages 2-3). However, the SCLC-I (inflamed) subtype demonstrates higher immune-cell infiltration, elevated checkpoint and HLA expression, and greater potential benefit from immunotherapy (megyesfalvi2023clinicalinsightsinto pages 6-7).

---

## 7. Anatomical Structures Affected

### Primary Organs
- **Lung** (UBERON:0002048) — primary site; tumors typically arise centrally in hilar/mediastinal regions
- **Brain** — frequent metastatic site; contrast-enhanced MRI is standard for evaluation (megyesfalvi2023clinicalinsightsinto pages 10-11)
- **Liver** — common metastatic site; liver metastasis is most common distant site in SCLC (OpenTargets Search: small cell lung cancer)
- **Bone** — frequent metastatic site
- **Adrenal glands** — common metastatic site

### Tissue and Cell Level
- Pulmonary neuroendocrine cells (CL:1000223)
- Small blue cells with scant cytoplasm, hyperchromatic nuclei, and salt-and-pepper chromatin (megyesfalvi2023clinicalinsightsinto pages 10-11)
- Dense-core neurosecretory granules (ultrastructural hallmark)

---

## 8. Temporal Development

### Onset
SCLC predominantly affects adults aged 60–80 years, with the disease being rare in patients under 40. The peak incidence is in the seventh decade of life (huang2023incidencesurvivalcomparison pages 1-2). Onset is typically subacute to acute, with rapid symptom progression over weeks to months.

### Progression and Staging
SCLC is staged using two systems:
1. **Veterans Affairs Lung Study Group (VALSG):** Limited-stage (LS-SCLC, ~30% of patients) vs. Extensive-stage (ES-SCLC, ~70% of patients) (huang2025molecularsubtypesand pages 1-2, redin2024smallcelllung pages 1-3)
2. **AJCC TNM staging system:** Increasingly used for prognostic refinement

Disease progression is extremely rapid, with a median doubling time of approximately 30 days. Despite high initial chemosensitivity, drug resistance develops rapidly, and recurrence occurs in the majority of patients (megyesfalvi2023clinicalinsightsinto pages 1-2).

### Disease Course
- **LS-SCLC:** Median survival 15–20 months with chemoradiation; 5-year survival 20–25% (chen2024aretrospectivestudy pages 1-2)
- **ES-SCLC:** Median survival historically ~10 months with chemotherapy; improved to 12–13 months with immunotherapy addition, and up to 19.3 months with anti-angiogenic combination regimens (chen2024advancesinpredictive pages 2-4, cheng2024benmelstobartanlotiniband pages 1-2)

---

## 9. Inheritance and Population

### Epidemiology
SCLC is not a heritable Mendelian disorder but rather a sporadic malignancy driven by somatic mutations accumulated through carcinogenic exposure.

**Incidence:** A comprehensive SEER database analysis of 188,426 SCLC patients (2000–2020) demonstrated that the age-adjusted incidence rate declined by an average of 3% annually, from 9 per 100,000 in 2000 to 4.6 per 100,000 in 2020 — a 48.6% overall decrease (uprety2025trendsinthe pages 1-2, uprety2025trendsinthe pages 2-4). In 2023, there were approximately 238,340 new lung cancer cases in the United States, with SCLC comprising approximately 13% (chen2024aretrospectivestudy pages 1-2).

**Population Demographics:**
- Incidence declines were observed across all age groups, sexes, and races, with younger groups (<50 years) showing sharper declines (APC -6.4%) compared to older populations (80+, APC -1.6%) (uprety2025trendsinthe pages 2-4)
- Males experienced steeper incidence declines (-3.5% APC) than females (-2.5% APC) (uprety2025trendsinthe pages 2-4)
- The disease predominantly affects elderly male heavy smokers (huang2023incidencesurvivalcomparison pages 1-2)
- Five-year overall survival remains less than 10–15% across all stages (chen2024aretrospectivestudy pages 1-2, huang2023incidencesurvivalcomparison pages 1-2)

**Survival trends:** Despite declining incidence and incidence-based mortality (from 6.6 in 2005 to 3.5 in 2020), 1-year relative survival rates have not improved significantly over the two-decade period, indicating the need for more effective systemic therapies (uprety2025trendsinthe pages 1-2).

---

## 10. Diagnostics

### Clinical Tests and Imaging
- **Chest radiography:** Initial imaging; may be unremarkable in ~4% of SCLC patients (megyesfalvi2023clinicalinsightsinto pages 9-9)
- **Contrast-enhanced CT:** Chest and upper abdomen for evaluating local invasiveness and staging (megyesfalvi2023clinicalinsightsinto pages 9-9)
- **18F-FDG PET-CT:** Key diagnostic tool demonstrating intense uptake due to SCLC's high metabolic activity; also helps estimate prognosis — higher metabolic tumor burden and total lesion glycolysis are associated with poor prognosis (megyesfalvi2023clinicalinsightsinto pages 9-9)
- **Contrast-enhanced brain MRI:** Standard for evaluating brain metastases (megyesfalvi2023clinicalinsightsinto pages 10-11)
- **Gallium-68 dotatate PET-CT:** For tumors with high somatostatin receptor expression (megyesfalvi2023clinicalinsightsinto pages 9-9)

### Tissue Diagnosis
- **Flexible bronchoscopy:** Preferred for centrally located tumors (megyesfalvi2023clinicalinsightsinto pages 10-10)
- **Endobronchial ultrasound-guided transbronchial needle aspiration (EBUS-TBNA):** For peribronchial tumors and mediastinal lymph node staging (megyesfalvi2023clinicalinsightsinto pages 10-10, megyesfalvi2023clinicalinsightsinto pages 10-11)
- **CT-guided transthoracic needle biopsy:** Sensitivity exceeding 90% for peripheral lesions (megyesfalvi2023clinicalinsightsinto pages 10-10)

### Pathology
Characteristic cytologic findings include small blue cells approximately 1.5 times the size of lymphocytes with scant cytoplasm, hyperchromatic oval or elongated nuclei with well-developed nuclear molding, and a finely dispersed "salt and pepper" chromatin pattern (megyesfalvi2023clinicalinsightsinto pages 10-11).

### Biomarkers
- **Neuroendocrine markers:** Synaptophysin, chromogranin A, CD56 (NCAM)
- **Transcription factor-based subtyping:** ASCL1, NEUROD1, POU2F3, YAP1 (IHC and RNA-based)
- **PD-L1 expression:** Evaluated but inconsistent as predictive biomarker for immunotherapy response (chen2024advancesinpredictive pages 2-4)
- **Tumor mutational burden (TMB):** Exploratory predictive biomarker (chen2024advancesinpredictive pages 2-4)
- **SLFN11 expression:** Predictive biomarker for PARP inhibitor sensitivity (huang2025molecularsubtypesand pages 7-9)
- **Circulating tumor DNA (ctDNA):** Emerging role in diagnosis and dynamic monitoring (megyesfalvi2023clinicalinsightsinto pages 10-10, chen2024advancesinpredictive pages 2-4)
- **Circulating tumor cells (CTCs):** Potential for liquid biopsy diagnosis (chen2024advancesinpredictive pages 2-4)

---

## 11. Outcome/Prognosis

### Survival and Mortality
- **Overall 5-year survival:** <7–10% across all stages (huang2025molecularsubtypesand pages 1-2, redin2024smallcelllung pages 1-3, chen2024aretrospectivestudy pages 1-2)
- **LS-SCLC 5-year survival:** 20–25% with concurrent chemoradiation (chen2024aretrospectivestudy pages 1-2)
- **ES-SCLC median OS with chemotherapy alone:** ~10–11.9 months (bonanno2024realworldimpactof pages 1-2, cheng2024benmelstobartanlotiniband pages 1-2)
- **ES-SCLC median OS with chemoimmunotherapy:** 12.3 months (atezolizumab, IMpower133) to 12.9 months (durvalumab, CASPIAN) (chen2024advancesinpredictive pages 2-4)
- **ES-SCLC 3-year survival with chemoimmunotherapy:** ~17.6% (CASPIAN) vs. ~5.8% with chemotherapy alone (zugazagoitia2024factsandhopes pages 3-3)
- **ES-SCLC 5-year survival with atezolizumab:** 12.1% (IMpower133 extension) (zugazagoitia2024factsandhopes pages 3-3)
- **ES-SCLC with benmelstobart + anlotinib + chemo (ETER701):** Median OS 19.3 months — the highest recorded in a randomized trial (cheng2024benmelstobartanlotiniband pages 1-2)

### Prognostic Factors
Age, sex, disease stage (TNM), T stage, N stage, M stage, liver metastasis, brain metastasis, bone metastasis, and treatment modality are independent prognostic factors (huang2023incidencesurvivalcomparison pages 1-2). CCNE1 amplification is associated with decreased survival, while 4q12 amplifications are associated with improved survival (OpenTargets Search: small cell lung cancer). Patients with neurologic paraneoplastic syndromes show improved prognosis (megyesfalvi2023clinicalinsightsinto pages 27-27).

---

## 12. Treatment

### Disease-Target Associations (OpenTargets)
The following table summarizes the key therapeutic targets identified from OpenTargets (MONDO:0008433) and the supporting literature:

| Target Gene Symbol | Target Name | Association Score | Key Evidence (approved drugs, clinical stage, relevant PMIDs) | Role in SCLC |
|---|---|---:|---|---|
| RB1 | RB transcriptional corepressor 1 | 0.73 | OpenTargets lists 5 supporting evidence items for MONDO_0008433, including literature PMIDs 34430610, 35792876, 26168399, 22941188, 24071849; recurrently identified as a defining SCLC tumor suppressor alteration (OpenTargets Search: small cell lung cancer, megyesfalvi2023clinicalinsightsinto pages 1-2) | Core tumor suppressor; near-universal functional loss helps drive cell-cycle deregulation and lineage transformation in SCLC (OpenTargets Search: small cell lung cancer, megyesfalvi2023clinicalinsightsinto pages 1-2) |
| TOP1 | DNA topoisomerase I | 0.65 | OpenTargets includes approval-stage evidence and clinical report IDs linked to TOP1-directed therapy plus regulatory records; literature and clinical evidence support topoisomerase-targeting treatment relevance in SCLC (OpenTargets Search: small cell lung cancer, patel2023smallcelllung pages 1-2) | Therapeutic target class rather than lineage driver; relevant because SCLC is highly chemotherapy-sensitive initially and topoisomerase-directed agents are part of the treatment landscape, including irinotecan-based regimens and lurbinectedin-era development context (OpenTargets Search: small cell lung cancer, patel2023smallcelllung pages 1-2) |
| TP53 | Tumor protein p53 | 0.63 | OpenTargets lists 5 evidence items including PMIDs 35340160, 37534137, 40113013, 30279957, 31737176; repeatedly described as nearly universal inactivation in SCLC (OpenTargets Search: small cell lung cancer, megyesfalvi2023clinicalinsightsinto pages 1-2) | Foundational tumor suppressor loss; with RB1 inactivation it is a hallmark initiating event in most SCLC and underlies genomic instability, apoptosis evasion, and aggressive behavior (OpenTargets Search: small cell lung cancer, megyesfalvi2023clinicalinsightsinto pages 1-2) |
| CD274 (PD-L1) | CD274 molecule | 0.62 | OpenTargets includes 5 literature-backed evidence items (PMIDs 32773010, 39810133, 38132164, 37040387, 31315783); clinical use supported by atezolizumab and durvalumab with platinum-etoposide in ES-SCLC (OpenTargets Search: small cell lung cancer, chen2024advancesinpredictive pages 2-4, bonanno2024realworldimpactof pages 1-2) | Immune checkpoint target; PD-L1-axis blockade is part of current first-line standard therapy for extensive-stage SCLC, though benefits are modest and biomarker performance is imperfect (chen2024advancesinpredictive pages 2-4, bonanno2024realworldimpactof pages 1-2) |
| CDK6 | Cyclin dependent kinase 6 | 0.62 | OpenTargets lists literature PMIDs 39136283 and 35117162 plus approval/phase 4 evidence; CDK4/6 dependency is most relevant in RB1-retained subsets (OpenTargets Search: small cell lung cancer) | Cell-cycle kinase target; may represent an actionable vulnerability in uncommon RB1-proficient SCLC tumors rather than classic RB1-null disease (OpenTargets Search: small cell lung cancer) |
| CDK4 | Cyclin dependent kinase 4 | 0.59 | OpenTargets lists literature PMIDs 39136283 and 31199581 plus approval/phase 4 evidence; CDK4/6 inhibitor sensitivity has been linked to RB1-expressing SCLC subsets (OpenTargets Search: small cell lung cancer) | Similar to CDK6, supports a precision-medicine niche in RB1-intact SCLC, where CDK4/6 blockade may suppress tumor growth (OpenTargets Search: small cell lung cancer) |
| DLL3 | Delta like canonical Notch ligand 3 | 0.59 | OpenTargets includes literature PMIDs 38468968, 41331586, 31819500, 31452726 and approval-stage evidence; DLL3-targeted BiTE therapy tarlatamab is highlighted in recent SCLC therapeutic reviews and trials (OpenTargets Search: small cell lung cancer, megyesfalvi2023clinicalinsightsinto pages 19-20, zugazagoitia2024factsandhopes pages 7-8) | Lineage-associated surface antigen enriched in neuroendocrine SCLC; major emerging therapeutic target for bispecific T-cell engagers, ADCs, and CAR-T approaches (megyesfalvi2023clinicalinsightsinto pages 19-20, zugazagoitia2024factsandhopes pages 7-8) |
| TOP2A | DNA topoisomerase II alpha | 0.58 | OpenTargets includes literature PMIDs 38806610, 37407689, 39921782 plus approval-stage evidence; mechanistically relevant to etoposide-based therapy backbone in SCLC (OpenTargets Search: small cell lung cancer, patel2023smallcelllung pages 1-2) | Cytotoxic therapy target linked to the etoposide backbone of standard treatment; reflects persistent dependence of SCLC management on DNA damage and topoisomerase-directed chemotherapy (OpenTargets Search: small cell lung cancer, patel2023smallcelllung pages 1-2) |


*Table: This table summarizes the leading OpenTargets disease-target associations for small cell lung cancer (MONDO_0008433) and links them to their clinical or biological roles in SCLC. It is useful for distinguishing foundational drivers such as TP53/RB1 from actionable therapeutic targets such as PD-L1, DLL3, CDK4/6, and topoisomerases.*

### Standard First-Line Therapy

**Limited-Stage SCLC:**
- Concurrent thoracic radiotherapy with platinum-etoposide chemotherapy (cisplatin or carboplatin plus etoposide) (megyesfalvi2023clinicalinsightsinto pages 1-2)
- Prophylactic cranial irradiation (PCI) for responders
- MAXO: MAXO:0000058 (chemotherapy), MAXO:0000014 (radiation therapy)

**Extensive-Stage SCLC:**
- Platinum-etoposide chemotherapy combined with anti-PD-L1 immunotherapy (atezolizumab or durvalumab) — current standard of care established by IMpower133 and CASPIAN trials (megyesfalvi2023clinicalinsightsinto pages 1-2, chen2024advancesinpredictive pages 2-4, bonanno2024realworldimpactof pages 1-2)
- Atezolizumab + carboplatin/etoposide: median OS 12.3 vs. 10.3 months (chen2024advancesinpredictive pages 2-4)
- Durvalumab + platinum/etoposide: median OS 12.9 vs. 10.5 months (chen2024advancesinpredictive pages 2-4)
- MAXO: MAXO:0001480 (immune checkpoint inhibitor therapy)

**Real-world impact:** After introduction of chemo-immunotherapy (May 2020), 12-month OS rate increased from 15% to 28% (p=0.03), and 18-month OS rate from 2.1% to 12% (p=0.009), with reduced hospitalization duration (bonanno2024realworldimpactof pages 1-2, bonanno2024realworldimpactof pages 3-5).

### Second-Line and Relapsed SCLC
- **Topotecan:** Previously the primary approved option for relapsed SCLC (patel2023smallcelllung pages 1-2)
- **Lurbinectedin:** FDA accelerated approval in 2020 with 35% overall response rate (patel2023smallcelllung pages 1-2)
- **Lurbinectedin + atezolizumab:** ORR 57.7%, median PFS 4.9 months in immunotherapy-naive patients (zugazagoitia2024factsandhopes pages 5-6)

### Emerging Targeted Therapies

**DLL3-Targeting Agents:**
- **Tarlatamab (AMG 757):** DLL3×CD3 bispecific T-cell engager; achieved 23.4% ORR with median duration of response of 12.3 months in heavily pretreated ES-SCLC (megyesfalvi2023clinicalinsightsinto pages 19-20, zugazagoitia2024factsandhopes pages 7-8). FDA approved for relapsed SCLC in 2024.

**Antibody-Drug Conjugates (ADCs):**
- **Ifinatamab deruxtecan (I-DXd):** Anti-B7-H3 ADC; 53% response rate in SCLC patients (patel2023smallcelllung pages 6-8)
- **Sacituzumab govitecan:** Anti-TROP2 ADC; 18% ORR, 7.1 month median OS (patel2023smallcelllung pages 6-8)

**PARP Inhibitors:**
- Rucaparib + nivolumab: clinical benefit in 56% of patients, 7.4 months median PFS (megyesfalvi2023clinicalinsightsinto pages 19-20)
- Talazoparib + atezolizumab maintenance: modest PFS improvement in SLFN11-positive tumors (zugazagoitia2024factsandhopes pages 5-6)

**CDK4/6 Inhibitors:**
- RB1-proficient SCLC (~14% of cases) shows sensitivity to palbociclib and abemaciclib (OpenTargets Search: small cell lung cancer)

**Anti-Angiogenic Combinations:**
- ETER701: Benmelstobart + anlotinib + etoposide/carboplatin achieved unprecedented median OS of 19.3 months in ES-SCLC (cheng2024benmelstobartanlotiniband pages 1-2, zugazagoitia2024factsandhopes pages 3-3)

### Key Clinical Trials

| NCT Number | Trial Name/Description | Phase | Status | Enrollment | Key Intervention |
|---|---|---|---|---:|---|
| NCT04234607 | ETER701: first-line extensive-stage SCLC trial of benmelstobart + anlotinib + etoposide/carboplatin versus comparator arms; reported median OS 19.3 vs 11.9 months for triplet vs chemotherapy alone (cheng2024benmelstobartanlotiniband pages 1-2, zugazagoitia2024factsandhopes pages 3-3) | Phase 3 | Completed/reported | 738 | Benmelstobart (PD-L1 inhibitor) + anlotinib + etoposide/carboplatin |
| NCT02763579 | IMpower133: landmark first-line ES-SCLC trial establishing atezolizumab + carboplatin/etoposide as a standard option; median OS 12.3 vs 10.3 months versus placebo + chemotherapy (chen2024advancesinpredictive pages 2-4, bonanno2024realworldimpactof pages 1-2) | Phase 3 | Completed | 403 | Atezolizumab + carboplatin + etoposide |
| NCT03043872 | CASPIAN: landmark first-line ES-SCLC trial establishing durvalumab + platinum/etoposide; median OS 12.9 vs 10.5 months versus chemotherapy alone (chen2024advancesinpredictive pages 2-4, bonanno2024realworldimpactof pages 1-2) | Phase 3 | Completed | 805 | Durvalumab + etoposide + platinum |
| NCT03319940 | First-in-human tarlatamab (AMG 757) study in relapsed/advanced SCLC and other NECs; established clinical activity for DLL3-targeted BiTE therapy (zugazagoitia2024factsandhopes pages 7-8) | Phase 1 | Active, not recruiting | 269 | Tarlatamab monotherapy |
| NCT05361395 | First-line tarlatamab combination trial in ES-SCLC (DeLLphi-305 concept): tarlatamab with carboplatin, etoposide, and PD-L1 inhibitor (sen2024emergingadvancesin pages 1-3) | Phase 1 | Active, not recruiting | 184 | Tarlatamab + carboplatin + etoposide + PD-L1 inhibitor |
| NCT05740566 | Phase 3 tarlatamab trial in relapsed SCLC referenced through DLL3/CD3 evidence; major confirmatory randomized program for DLL3-targeted BiTE therapy (OpenTargets Search: small cell lung cancer) | Phase 3 | Ongoing | NR | Tarlatamab versus standard therapy |
| NCT06203210 | Phase 3 trial of ifinatamab deruxtecan versus physician’s choice in relapsed SCLC (patel2023smallcelllung pages 6-8, OpenTargets Search: small cell lung cancer) | Phase 3 | Recruiting | 540 | Ifinatamab deruxtecan (B7-H3 ADC) |
| NCT07218146 | DLLEVATE: Phase 3 trial of ZL-1310 versus investigator’s choice in relapsed SCLC (OpenTargets Search: small cell lung cancer) | Phase 3 | Recruiting | 480 | ZL-1310 |
| NCT06498479 | ARTEMIS-008: Phase 3 trial of HS-20093 compared with topotecan in relapsed SCLC (OpenTargets Search: small cell lung cancer) | Phase 3 | Recruiting | 460 | HS-20093 versus topotecan |
| NCT07015892 | Dose-escalation radiotherapy in limited-stage SCLC randomized Phase 3 study (OpenTargets Search: small cell lung cancer) | Phase 3 | Recruiting | 300 | Dose-escalated thoracic radiotherapy |
| NCT04402788 | RAPTOR: addition of radiation therapy to maintenance atezolizumab in extensive-stage SCLC after chemoimmunotherapy (OpenTargets Search: small cell lung cancer) | Phase 2/3 | Recruiting | 138 | Thoracic radiation + atezolizumab |


*Table: This table summarizes landmark and actively recruiting small cell lung cancer trials identified in the research, spanning chemoimmunotherapy, DLL3-targeted therapy, antibody-drug conjugates, and radiation strategies. It is useful for quickly comparing the current clinical development landscape and the studies that shaped present standards of care.*

### Telomere-Targeting Approaches
6-Thio-2'-deoxyguanosine (6TdG), currently in phase II clinical trials, is a nucleoside analog preferentially incorporated by telomerase into telomeres, leading to telomere dysfunction. In SCLC preclinical models, low intermittent doses inhibited tumor growth, reduced metastatic burden, depleted cancer-initiating cells, and activated innate and adaptive anti-tumor immune responses through STING signaling (eglenenpolat2024atelomeretargetingdrug pages 1-2).

---

## 13. Prevention

### Primary Prevention
- **Smoking cessation and prevention** remain the most important preventive strategies. The 48.6% decline in SCLC incidence from 2000–2020 directly correlates with reduced smoking rates (uprety2025trendsinthe pages 1-2, uprety2025trendsinthe pages 2-4)
- **Radon mitigation** in homes and workplaces
- **Air pollution reduction** policies

### Secondary Prevention (Screening)
Low-dose CT (LDCT) lung cancer screening programs detect predominantly non-small cell lung cancers. SCLC is less commonly detected by screening due to its rapid growth kinetics and interval presentation. However, broader adoption of LDCT screening may increase early-stage SCLC detection.

### Tertiary Prevention
- **Prophylactic cranial irradiation (PCI):** Reduces brain metastasis incidence in responding LS-SCLC patients
- **Thoracic radiotherapy consolidation:** Addition of TRT showed significant survival benefits in ES-SCLC patients receiving immunotherapy plus chemotherapy (median PFS 10.76 vs. 7.63 months; median OS 21.67 vs. 16.6 months) (OpenTargets Search: small cell lung cancer)

---

## 14. Other Species / Natural Disease

SCLC is primarily a human disease and does not commonly occur naturally in other species in an identical form. However, spontaneous neuroendocrine tumors have been reported in rodents and dogs. Comparative pathology studies utilize orthologous genes (murine Trp53 and Rb1) in genetically engineered models to recapitulate human disease features.

---

## 15. Model Organisms

### Genetically Engineered Mouse Models (GEMMs)
The foundational SCLC GEMM was generated by **Meuwissen et al.** using lung-specific compound deletion of Trp53 and Rb1 genes, which led to SCLC tumor development resembling human disease. A key finding was the long tumor latent period of 9–12 months after genetic deletion, indicating that secondary oncogenic alterations are required for malignant transformation (papavassiliou2024p53andrb pages 4-5). Additional GEMMs incorporating further genetic aberrations (e.g., Rbl2/p130 deletion, Myc overexpression, Pten deletion) alongside Trp53/Rb1 loss showed shorter latency periods (papavassiliou2024p53andrb pages 4-5).

A GEMM with a mutant c-Myc allele demonstrated tumor progression and metastasis associated with subtype transition from SCLC-A to SCLC-N and low-NE YAP1+ SCLC, modeling the plasticity observed in human disease (redin2024smarca4controlsstate pages 1-2).

### Cell Lines
Established SCLC cell lines include mouse-derived lines (984 from Rb/p53 KO mice; RPP from Rb/p130/p53 triple KO) and human lines (H1048, H69, H510, H841) (eglenenpolat2024atelomeretargetingdrug pages 1-2).

### Patient-Derived Xenografts (PDXs)
PDX models maintain the molecular and biologic features of original patient tumors and are used for preclinical drug testing. They have been employed for ChIPseq characterization of epigenetic regulators like SMARCA4 and for testing novel therapeutic combinations (redin2024smarca4controlsstate pages 1-2, eglenenpolat2024atelomeretargetingdrug pages 1-2).

### Syngeneic and Humanized Models
Syngeneic SCLC models are critical for studying immune responses in vivo and testing immunotherapeutic approaches, including 6TdG studies that demonstrated immune-dependent anti-tumor activity (eglenenpolat2024atelomeretargetingdrug pages 1-2).

### Model Limitations
- Long latency periods in GEMMs (9–12 months) limit throughput
- In vitro TP53/RB1-null cells demonstrate indefinite proliferation but not spontaneous malignant transformation, representing a precancerous state rather than fully malignant SCLC (papavassiliou2024p53andrb pages 4-5)
- PDX models lack an intact immune system (requiring humanized mouse approaches)
- Cell line models may not capture the full intratumoral heterogeneity and plasticity of patient tumors
- Single-biopsy molecular classification may miss intratumoral subtype mixing (redin2024smallcelllung pages 4-6)

---

## Summary

Small cell lung cancer remains one of the most challenging malignancies in oncology, defined by its aggressive biology, near-universal TP53/RB1 inactivation, and rapid chemoresistance development. The molecular reclassification into transcription factor-defined subtypes (SCLC-A, SCLC-N, SCLC-P, SCLC-Y/I) has opened new avenues for precision medicine (huang2025molecularsubtypesand pages 1-2, redin2024smallcelllung pages 1-3). While chemo-immunotherapy has become the standard of care for ES-SCLC with modest survival improvements, emerging therapies including DLL3-targeting bispecific T-cell engagers (tarlatamab), antibody-drug conjugates, and anti-angiogenic combinations (ETER701) show promising activity (megyesfalvi2023clinicalinsightsinto pages 19-20, zugazagoitia2024factsandhopes pages 7-8, cheng2024benmelstobartanlotiniband pages 1-2). The integration of multi-omic data, dynamic liquid biopsy monitoring, and subtype-specific therapeutic strategies represents the future direction for improving outcomes in this devastating disease (huang2025molecularsubtypesand pages 13-15).

References

1. (zugazagoitia2024factsandhopes pages 1-1): Jon Zugazagoitia, Handerson Osma, Javier Baena, Alvaro C. Ucero, and Luis Paz-Ares. Facts and hopes on cancer immunotherapy for small cell lung cancer. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:2872-2883, Apr 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-1159, doi:10.1158/1078-0432.ccr-23-1159. This article has 29 citations.

2. (redin2024smallcelllung pages 1-3): Esther Redin, Álvaro Quintanal-Villalonga, and Charles M. Rudin. Small cell lung cancer profiling: an updated synthesis of subtypes, vulnerabilities, and plasticity. Trends in Cancer, 10:935-946, Oct 2024. URL: https://doi.org/10.1016/j.trecan.2024.07.008, doi:10.1016/j.trecan.2024.07.008. This article has 47 citations and is from a peer-reviewed journal.

3. (megyesfalvi2023clinicalinsightsinto pages 1-2): Zsolt Megyesfalvi, Carl M. Gay, Helmut Popper, Robert Pirker, Gyula Ostoros, Simon Heeke, Christian Lang, Konrad Hoetzenecker, Anna Schwendenwein, Kristiina Boettiger, Paul A. Bunn, Ferenc Renyi‐Vamos, Karin Schelch, Helmut Prosch, Lauren A. Byers, Fred R. Hirsch, and Balazs Dome. Clinical insights into small cell lung cancer: tumor heterogeneity, diagnosis, therapy, and future directions. CA: A Cancer Journal for Clinicians, 73:620-652, Jun 2023. URL: https://doi.org/10.3322/caac.21785, doi:10.3322/caac.21785. This article has 506 citations and is from a domain leading peer-reviewed journal.

4. (huang2025molecularsubtypesand pages 1-2): Daoyuan Huang, Jingchao Wang, Li Chen, Weiwei Jiang, Hiroyuki Inuzuka, David K. Simon, and Wenyi Wei. Molecular subtypes and targeted therapeutic strategies in small cell lung cancer: advances, challenges, and future perspectives. Molecules, 30:1731, Apr 2025. URL: https://doi.org/10.3390/molecules30081731, doi:10.3390/molecules30081731. This article has 21 citations.

5. (OpenTargets Search: small cell lung cancer): Open Targets Query (small cell lung cancer, 41 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (megyesfalvi2023clinicalinsightsinto pages 5-5): Zsolt Megyesfalvi, Carl M. Gay, Helmut Popper, Robert Pirker, Gyula Ostoros, Simon Heeke, Christian Lang, Konrad Hoetzenecker, Anna Schwendenwein, Kristiina Boettiger, Paul A. Bunn, Ferenc Renyi‐Vamos, Karin Schelch, Helmut Prosch, Lauren A. Byers, Fred R. Hirsch, and Balazs Dome. Clinical insights into small cell lung cancer: tumor heterogeneity, diagnosis, therapy, and future directions. CA: A Cancer Journal for Clinicians, 73:620-652, Jun 2023. URL: https://doi.org/10.3322/caac.21785, doi:10.3322/caac.21785. This article has 506 citations and is from a domain leading peer-reviewed journal.

7. (huang2023incidencesurvivalcomparison pages 1-2): Liling Huang, Yu Feng, Tongji Xie, Haohua Zhu, Le Tang, and Yuankai Shi. Incidence, survival comparison, and novel prognostic evaluation approaches for stage iii-iv pulmonary large cell neuroendocrine carcinoma and small cell lung cancer. BMC Cancer, Apr 2023. URL: https://doi.org/10.1186/s12885-023-10797-3, doi:10.1186/s12885-023-10797-3. This article has 24 citations and is from a peer-reviewed journal.

8. (uprety2025trendsinthe pages 1-2): Dipesh Uprety, Randell Seaton, Abesh Niroula, Tarik Hadid, Kaushal Parikh, and Julie J. Ruterbusch. Trends in the incidence and survival outcomes in patients with small cell lung cancer in the united states: an analysis of the seer database. Cancer Medicine, Feb 2025. URL: https://doi.org/10.1002/cam4.70608, doi:10.1002/cam4.70608. This article has 17 citations and is from a peer-reviewed journal.

9. (uprety2025trendsinthe pages 2-4): Dipesh Uprety, Randell Seaton, Abesh Niroula, Tarik Hadid, Kaushal Parikh, and Julie J. Ruterbusch. Trends in the incidence and survival outcomes in patients with small cell lung cancer in the united states: an analysis of the seer database. Cancer Medicine, Feb 2025. URL: https://doi.org/10.1002/cam4.70608, doi:10.1002/cam4.70608. This article has 17 citations and is from a peer-reviewed journal.

10. (megyesfalvi2023clinicalinsightsinto pages 27-27): Zsolt Megyesfalvi, Carl M. Gay, Helmut Popper, Robert Pirker, Gyula Ostoros, Simon Heeke, Christian Lang, Konrad Hoetzenecker, Anna Schwendenwein, Kristiina Boettiger, Paul A. Bunn, Ferenc Renyi‐Vamos, Karin Schelch, Helmut Prosch, Lauren A. Byers, Fred R. Hirsch, and Balazs Dome. Clinical insights into small cell lung cancer: tumor heterogeneity, diagnosis, therapy, and future directions. CA: A Cancer Journal for Clinicians, 73:620-652, Jun 2023. URL: https://doi.org/10.3322/caac.21785, doi:10.3322/caac.21785. This article has 506 citations and is from a domain leading peer-reviewed journal.

11. (redin2024smarca4controlsstate pages 1-2): Esther Redin, Harsha Sridhar, Yingqian A. Zhan, Barbara Pereira Mello, Hong Zhong, Vidushi Durani, Amin Sabet, Parvathy Manoj, Irina Linkov, Juan Qiu, Richard P. Koche, Elisa de Stanchina, Maider Astorkia, Doron Betel, Álvaro Quintanal-Villalonga, and Charles M. Rudin. Smarca4 controls state plasticity in small cell lung cancer through regulation of neuroendocrine transcription factors and rest splicing. Journal of Hematology & Oncology, Jul 2024. URL: https://doi.org/10.1186/s13045-024-01572-3, doi:10.1186/s13045-024-01572-3. This article has 41 citations and is from a domain leading peer-reviewed journal.

12. (huang2025molecularsubtypesand pages 7-9): Daoyuan Huang, Jingchao Wang, Li Chen, Weiwei Jiang, Hiroyuki Inuzuka, David K. Simon, and Wenyi Wei. Molecular subtypes and targeted therapeutic strategies in small cell lung cancer: advances, challenges, and future perspectives. Molecules, 30:1731, Apr 2025. URL: https://doi.org/10.3390/molecules30081731, doi:10.3390/molecules30081731. This article has 21 citations.

13. (huang2025molecularsubtypesand pages 2-4): Daoyuan Huang, Jingchao Wang, Li Chen, Weiwei Jiang, Hiroyuki Inuzuka, David K. Simon, and Wenyi Wei. Molecular subtypes and targeted therapeutic strategies in small cell lung cancer: advances, challenges, and future perspectives. Molecules, 30:1731, Apr 2025. URL: https://doi.org/10.3390/molecules30081731, doi:10.3390/molecules30081731. This article has 21 citations.

14. (patel2023smallcelllung pages 1-2): Shruti R. Patel and Millie Das. Small cell lung cancer: emerging targets and strategies for precision therapy. Cancers, 15:4016, Aug 2023. URL: https://doi.org/10.3390/cancers15164016, doi:10.3390/cancers15164016. This article has 39 citations.

15. (redin2024smallcelllung pages 4-6): Esther Redin, Álvaro Quintanal-Villalonga, and Charles M. Rudin. Small cell lung cancer profiling: an updated synthesis of subtypes, vulnerabilities, and plasticity. Trends in Cancer, 10:935-946, Oct 2024. URL: https://doi.org/10.1016/j.trecan.2024.07.008, doi:10.1016/j.trecan.2024.07.008. This article has 47 citations and is from a peer-reviewed journal.

16. (redin2024smallcelllung pages 11-13): Esther Redin, Álvaro Quintanal-Villalonga, and Charles M. Rudin. Small cell lung cancer profiling: an updated synthesis of subtypes, vulnerabilities, and plasticity. Trends in Cancer, 10:935-946, Oct 2024. URL: https://doi.org/10.1016/j.trecan.2024.07.008, doi:10.1016/j.trecan.2024.07.008. This article has 47 citations and is from a peer-reviewed journal.

17. (redin2024smallcelllung pages 13-14): Esther Redin, Álvaro Quintanal-Villalonga, and Charles M. Rudin. Small cell lung cancer profiling: an updated synthesis of subtypes, vulnerabilities, and plasticity. Trends in Cancer, 10:935-946, Oct 2024. URL: https://doi.org/10.1016/j.trecan.2024.07.008, doi:10.1016/j.trecan.2024.07.008. This article has 47 citations and is from a peer-reviewed journal.

18. (huang2025molecularsubtypesand pages 13-15): Daoyuan Huang, Jingchao Wang, Li Chen, Weiwei Jiang, Hiroyuki Inuzuka, David K. Simon, and Wenyi Wei. Molecular subtypes and targeted therapeutic strategies in small cell lung cancer: advances, challenges, and future perspectives. Molecules, 30:1731, Apr 2025. URL: https://doi.org/10.3390/molecules30081731, doi:10.3390/molecules30081731. This article has 21 citations.

19. (megyesfalvi2023clinicalinsightsinto pages 6-7): Zsolt Megyesfalvi, Carl M. Gay, Helmut Popper, Robert Pirker, Gyula Ostoros, Simon Heeke, Christian Lang, Konrad Hoetzenecker, Anna Schwendenwein, Kristiina Boettiger, Paul A. Bunn, Ferenc Renyi‐Vamos, Karin Schelch, Helmut Prosch, Lauren A. Byers, Fred R. Hirsch, and Balazs Dome. Clinical insights into small cell lung cancer: tumor heterogeneity, diagnosis, therapy, and future directions. CA: A Cancer Journal for Clinicians, 73:620-652, Jun 2023. URL: https://doi.org/10.3322/caac.21785, doi:10.3322/caac.21785. This article has 506 citations and is from a domain leading peer-reviewed journal.

20. (chen2024advancesinpredictive pages 2-4): Tong Chen, Mingzhao Wang, Yanchao Chen, Yang Cao, and Yutao Liu. Advances in predictive biomarkers associated with immunotherapy in extensive-stage small cell lung cancer. Cell & Bioscience, Sep 2024. URL: https://doi.org/10.1186/s13578-024-01283-9, doi:10.1186/s13578-024-01283-9. This article has 24 citations and is from a peer-reviewed journal.

21. (papavassiliou2024p53andrb pages 4-5): Kostas A. Papavassiliou, Amalia A. Sofianidi, Vassiliki A. Gogou, Nektarios Anagnostopoulos, and Athanasios G. Papavassiliou. P53 and rb aberrations in small cell lung cancer (sclc): from molecular mechanisms to therapeutic modulation. International Journal of Molecular Sciences, 25:2479, Feb 2024. URL: https://doi.org/10.3390/ijms25052479, doi:10.3390/ijms25052479. This article has 39 citations.

22. (zugazagoitia2024factsandhopes pages 2-3): Jon Zugazagoitia, Handerson Osma, Javier Baena, Alvaro C. Ucero, and Luis Paz-Ares. Facts and hopes on cancer immunotherapy for small cell lung cancer. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:2872-2883, Apr 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-1159, doi:10.1158/1078-0432.ccr-23-1159. This article has 29 citations.

23. (megyesfalvi2023clinicalinsightsinto pages 10-11): Zsolt Megyesfalvi, Carl M. Gay, Helmut Popper, Robert Pirker, Gyula Ostoros, Simon Heeke, Christian Lang, Konrad Hoetzenecker, Anna Schwendenwein, Kristiina Boettiger, Paul A. Bunn, Ferenc Renyi‐Vamos, Karin Schelch, Helmut Prosch, Lauren A. Byers, Fred R. Hirsch, and Balazs Dome. Clinical insights into small cell lung cancer: tumor heterogeneity, diagnosis, therapy, and future directions. CA: A Cancer Journal for Clinicians, 73:620-652, Jun 2023. URL: https://doi.org/10.3322/caac.21785, doi:10.3322/caac.21785. This article has 506 citations and is from a domain leading peer-reviewed journal.

24. (chen2024aretrospectivestudy pages 1-2): Yao Chen, Ling Yao, Qingquan Chen, Yiming Hu, Xi Zhu, Rongrong Dai, Xiaoyang Chen, Yifu Zeng, Yong Zhu, Duanhong Song, and Yixiang Zhang. A retrospective study on the impact of radiotherapy on the survival outcomes of small cell lung cancer patients based on the seer database. Scientific Reports, Jul 2024. URL: https://doi.org/10.1038/s41598-024-65314-8, doi:10.1038/s41598-024-65314-8. This article has 8 citations and is from a peer-reviewed journal.

25. (cheng2024benmelstobartanlotiniband pages 1-2): Ying Cheng, Jianhua Chen, Wei Zhang, Chao Xie, Qun Hu, Ningning Zhou, Chun Huang, Shihong Wei, Hong Sun, Xingya Li, Yan Yu, Jinhuo Lai, Huaping Yang, Haohui Fang, Hualin Chen, Peng Zhang, Kangsheng Gu, Qiming Wang, Jianhua Shi, Tienan Yi, Xingxiang Xu, Xianwei Ye, Daqing Wang, Conghua Xie, Chunling Liu, Yulong Zheng, Daren Lin, Wu Zhuang, Ping Lu, Guohua Yu, Jinzhang Li, Yuhai Gu, Baolan Li, Rong Wu, Ou Jiang, Zaiyi Wang, Guowu Wu, Haifeng Lin, Diansheng Zhong, Yanhua Xu, Yongqian Shu, Di Wu, Xingwu Chen, Jie Wang, Minghui Wang, and Runxiang Yang. Benmelstobart, anlotinib and chemotherapy in extensive-stage small-cell lung cancer: a randomized phase 3 trial. Nature Medicine, 30:2967-2976, Jul 2024. URL: https://doi.org/10.1038/s41591-024-03132-1, doi:10.1038/s41591-024-03132-1. This article has 154 citations and is from a highest quality peer-reviewed journal.

26. (megyesfalvi2023clinicalinsightsinto pages 9-9): Zsolt Megyesfalvi, Carl M. Gay, Helmut Popper, Robert Pirker, Gyula Ostoros, Simon Heeke, Christian Lang, Konrad Hoetzenecker, Anna Schwendenwein, Kristiina Boettiger, Paul A. Bunn, Ferenc Renyi‐Vamos, Karin Schelch, Helmut Prosch, Lauren A. Byers, Fred R. Hirsch, and Balazs Dome. Clinical insights into small cell lung cancer: tumor heterogeneity, diagnosis, therapy, and future directions. CA: A Cancer Journal for Clinicians, 73:620-652, Jun 2023. URL: https://doi.org/10.3322/caac.21785, doi:10.3322/caac.21785. This article has 506 citations and is from a domain leading peer-reviewed journal.

27. (megyesfalvi2023clinicalinsightsinto pages 10-10): Zsolt Megyesfalvi, Carl M. Gay, Helmut Popper, Robert Pirker, Gyula Ostoros, Simon Heeke, Christian Lang, Konrad Hoetzenecker, Anna Schwendenwein, Kristiina Boettiger, Paul A. Bunn, Ferenc Renyi‐Vamos, Karin Schelch, Helmut Prosch, Lauren A. Byers, Fred R. Hirsch, and Balazs Dome. Clinical insights into small cell lung cancer: tumor heterogeneity, diagnosis, therapy, and future directions. CA: A Cancer Journal for Clinicians, 73:620-652, Jun 2023. URL: https://doi.org/10.3322/caac.21785, doi:10.3322/caac.21785. This article has 506 citations and is from a domain leading peer-reviewed journal.

28. (bonanno2024realworldimpactof pages 1-2): Laura Bonanno, Lorenzo Calvetti, Alessandro Dal Maso, Alberto Pavan, Loc Carlo Bao, Mattia De Nuzzo, Stefano Frega, Giulia Sartori, Alessandra Ferro, Giulia Pasello, Paolo Morandi, Giuseppe Aprile, and Valentina Guarneri. Real-world impact of the introduction of chemo-immunotherapy in extended small cell lung cancer: a multicentric analysis. Frontiers in Immunology, Jan 2024. URL: https://doi.org/10.3389/fimmu.2024.1353889, doi:10.3389/fimmu.2024.1353889. This article has 11 citations and is from a peer-reviewed journal.

29. (zugazagoitia2024factsandhopes pages 3-3): Jon Zugazagoitia, Handerson Osma, Javier Baena, Alvaro C. Ucero, and Luis Paz-Ares. Facts and hopes on cancer immunotherapy for small cell lung cancer. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:2872-2883, Apr 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-1159, doi:10.1158/1078-0432.ccr-23-1159. This article has 29 citations.

30. (megyesfalvi2023clinicalinsightsinto pages 19-20): Zsolt Megyesfalvi, Carl M. Gay, Helmut Popper, Robert Pirker, Gyula Ostoros, Simon Heeke, Christian Lang, Konrad Hoetzenecker, Anna Schwendenwein, Kristiina Boettiger, Paul A. Bunn, Ferenc Renyi‐Vamos, Karin Schelch, Helmut Prosch, Lauren A. Byers, Fred R. Hirsch, and Balazs Dome. Clinical insights into small cell lung cancer: tumor heterogeneity, diagnosis, therapy, and future directions. CA: A Cancer Journal for Clinicians, 73:620-652, Jun 2023. URL: https://doi.org/10.3322/caac.21785, doi:10.3322/caac.21785. This article has 506 citations and is from a domain leading peer-reviewed journal.

31. (zugazagoitia2024factsandhopes pages 7-8): Jon Zugazagoitia, Handerson Osma, Javier Baena, Alvaro C. Ucero, and Luis Paz-Ares. Facts and hopes on cancer immunotherapy for small cell lung cancer. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:2872-2883, Apr 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-1159, doi:10.1158/1078-0432.ccr-23-1159. This article has 29 citations.

32. (bonanno2024realworldimpactof pages 3-5): Laura Bonanno, Lorenzo Calvetti, Alessandro Dal Maso, Alberto Pavan, Loc Carlo Bao, Mattia De Nuzzo, Stefano Frega, Giulia Sartori, Alessandra Ferro, Giulia Pasello, Paolo Morandi, Giuseppe Aprile, and Valentina Guarneri. Real-world impact of the introduction of chemo-immunotherapy in extended small cell lung cancer: a multicentric analysis. Frontiers in Immunology, Jan 2024. URL: https://doi.org/10.3389/fimmu.2024.1353889, doi:10.3389/fimmu.2024.1353889. This article has 11 citations and is from a peer-reviewed journal.

33. (zugazagoitia2024factsandhopes pages 5-6): Jon Zugazagoitia, Handerson Osma, Javier Baena, Alvaro C. Ucero, and Luis Paz-Ares. Facts and hopes on cancer immunotherapy for small cell lung cancer. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:2872-2883, Apr 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-1159, doi:10.1158/1078-0432.ccr-23-1159. This article has 29 citations.

34. (patel2023smallcelllung pages 6-8): Shruti R. Patel and Millie Das. Small cell lung cancer: emerging targets and strategies for precision therapy. Cancers, 15:4016, Aug 2023. URL: https://doi.org/10.3390/cancers15164016, doi:10.3390/cancers15164016. This article has 39 citations.

35. (sen2024emergingadvancesin pages 1-3): Triparna Sen, Nobuyuki Takahashi, Subhamoy Chakraborty, Naoko Takebe, Amin H. Nassar, Nagla A. Karim, Sonam Puri, and Abdul Rafeh Naqash. Emerging advances in defining the molecular and therapeutic landscape of small-cell lung cancer. Nature reviews. Clinical oncology, 21:610-627, Jul 2024. URL: https://doi.org/10.1038/s41571-024-00914-x, doi:10.1038/s41571-024-00914-x. This article has 137 citations.

36. (eglenenpolat2024atelomeretargetingdrug pages 1-2): Buse Eglenen-Polat, Ryan R. Kowash, Hai-Cheng Huang, Silvia Siteni, Mingrui Zhu, Kenian Chen, Matthew E. Bender, Ilgen Mender, Victor Stastny, Benjamin J. Drapkin, Prithvi Raj, John D. Minna, Lin Xu, Jerry W. Shay, and Esra A. Akbay. A telomere-targeting drug depletes cancer initiating cells and promotes anti-tumor immunity in small cell lung cancer. Nature Communications, Jan 2024. URL: https://doi.org/10.1038/s41467-024-44861-8, doi:10.1038/s41467-024-44861-8. This article has 27 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Small_Cell_Lung_Cancer-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Small_Cell_Lung_Cancer-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](Small_Cell_Lung_Cancer-deep-research-falcon_artifacts/artifact-02.md)