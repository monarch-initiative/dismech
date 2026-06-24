---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-21T10:52:31.884970'
end_time: '2026-06-21T11:04:09.877913'
duration_seconds: 697.99
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Obsessive-Compulsive Disorder
  mondo_id: ''
  category: Psychiatric
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 16
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: Obsessive-Compulsive_Disorder-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Obsessive-Compulsive_Disorder-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: Obsessive-Compulsive_Disorder-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Obsessive-Compulsive Disorder
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Obsessive-Compulsive Disorder** covering all of the
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
- **Disease Name:** Obsessive-Compulsive Disorder
- **MONDO ID:**  (if available)
- **Category:** Psychiatric

## Research Objectives

Please provide a comprehensive research report on **Obsessive-Compulsive Disorder** covering all of the
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



# Comprehensive Research Report: Obsessive-Compulsive Disorder (OCD)

## 1. Disease Information

### Overview and Definition
Obsessive-Compulsive Disorder (OCD) is a neuropsychiatric condition characterized by unwanted obsessions (repetitive thoughts, images, or urges) and/or compulsions (repetitive behaviors or mental acts) that cause significant distress and functional impairment (jalal2023obsessive‐compulsivedisorderetiology pages 1-2, roh2023clinicaladvancesin pages 1-2). OCD affects approximately 1-3% of the general population, making it a common psychiatric disorder with substantial public health burden (jalal2023obsessive‐compulsivedisorderetiology pages 1-2, stein2025obsessivecompulsivedisorderin pages 1-2, strom2025genomewideanalysesidentify pages 1-2).

### Classification and Identifiers
In the DSM-5 and ICD-11, OCD was reclassified from the anxiety disorder category to a new grouping called "Obsessive-Compulsive and Related Disorders" (OCRD), reflecting improved understanding of its distinct neurobiological substrates (jalal2023obsessive‐compulsivedisorderetiology pages 1-2, roh2023clinicaladvancesin pages 1-2, jalal2023obsessive‐compulsivedisorderetiology pages 2-3). This category includes hoarding disorder, body dysmorphic disorder, trichotillomania, and excoriation disorder (jalal2023obsessive‐compulsivedisorderetiology pages 2-3).

### Diagnostic Criteria
According to DSM-5, diagnosis requires the presence of obsessions and/or compulsions that are time-consuming (taking more than one hour per day) and cause significant distress or interfere with everyday activities including social and occupational functioning (jalal2023obsessive‐compulsivedisorderetiology pages 1-2). The DSM-5 includes a specifier for insight level, recognizing that patients vary from good/fair insight to absent insight or delusional beliefs (jalal2023obsessive‐compulsivedisorderetiology pages 1-2, jalal2023obsessive‐compulsivedisorderetiology pages 2-3).

## 2. Etiology

### Disease Causal Factors
OCD etiology involves a complex interplay of genetic vulnerability, environmental exposures, and neurobiological mechanisms (dhiman2025hereditarypatternsand pages 1-1, roh2023clinicaladvancesin pages 1-2, liu2023earlyidentificationand pages 1-2).

### Risk Factors

**Genetic Risk Factors:** OCD demonstrates substantial heritability. Twin-based heritability estimates range from 27-47% in adults and 45-65% in children, with pediatric-onset OCD showing higher genetic loading than adult-onset cases (dhiman2025hereditarypatternsand pages 1-1, strom2025genomewideanalysesidentify pages 1-2, liu2023earlyidentificationand pages 1-2). Family studies indicate genetic contribution of 35-50% (roh2023clinicaladvancesin pages 1-2). 

The largest genome-wide association study (GWAS) meta-analysis to date, combining 53,660 OCD cases and 2,044,417 controls, identified 30 independent genome-wide significant loci (strom2025genomewideanalysesidentify pages 1-2, strom2025genomewideanalysesidentify pages 2-3). Key findings include:
- Approximately 11,500 genetic variants explain 90% of OCD genetic heritability, indicating highly polygenic architecture (strom2025genomewideanalysesidentify pages 2-3)
- SNP-based heritability estimated at 6.7% (SE 0.3%) assuming 1% population prevalence, with higher estimates in clinically ascertained samples (strom2025genomewideanalysesidentify pages 2-3)
- Priority candidate genes include WDR6, DALRD3, and CTNND1, along with multiple genes in the major histocompatibility complex (MHC) region (strom2025genomewideanalysesidentify pages 1-2, strom2025genomewideanalysesidentify pages 3-4)

**Environmental Risk Factors:** While specific environmental factors remain under investigation, adverse lifetime experiences may induce neurobiological adaptations within a genetic vulnerability window (roh2023clinicaladvancesin pages 1-2). The OCDTWIN project is systematically investigating environmental risk factors through discordant monozygotic twin pairs (dhiman2025hereditarypatternsand pages 1-1).

**Gene-Environment Interactions:** Limited direct evidence exists for specific gene-environment interactions in OCD, though the OCDTWIN study aims to isolate unique environmental risk factors in the causal pathway while controlling for genetic influences (dhiman2025hereditarypatternsand pages 1-1).

| Gene/Locus | Chromosome Location | Function/Description | Evidence Type (GWAS/TWAS/PWAS) | P-value or significance | Key Findings |
|---|---|---|---|---|---|
| OCD GWAS meta-analysis summary | Genome-wide | Large-scale common-variant architecture of OCD | GWAS | 30 independent genome-wide significant loci in 53,660 cases and 2,044,417 controls; 1,672 SNPs exceeded genome-wide significance; threshold P < 5×10⁻⁸ (strom2025genomewideanalysesidentify pages 1-2, strom2025genomewideanalysesidentify pages 2-3) | Largest reported OCD GWAS identified 30 loci, substantially expanding prior findings and supporting a highly polygenic architecture (strom2025genomewideanalysesidentify pages 1-2, strom2025genomewideanalysesidentify pages 2-3) |
| Polygenic architecture | Genome-wide | Aggregate common-variant contribution to OCD risk | GWAS / MiXeR | ~11,500 causal variants (SE 607) explain 90% of OCD SNP-based heritability (strom2025genomewideanalysesidentify pages 2-3) | Indicates OCD risk is distributed across thousands of variants rather than a few high-penetrance loci, consistent with complex polygenic inheritance (strom2025genomewideanalysesidentify pages 2-3) |
| SNP-based heritability | Genome-wide | Common-variant heritability estimate | GWAS | h²SNP 6.7% (SE 0.3%) overall assuming 1% prevalence; subgroup estimates higher in clinically ascertained samples; earlier published estimates ranged ~8.5% to 16%, with older reports up to 28–37% depending on design/assumptions (strom2025genomewideanalysesidentify pages 1-2, strom2025genomewideanalysesidentify pages 2-3) | Supports measurable but incomplete capture of total OCD heritability by common SNPs; twin-based heritability remains higher than SNP-based estimates (strom2025genomewideanalysesidentify pages 1-2) |
| Twin/family heritability | Genome-wide | Familial genetic contribution | Family/twin studies summarized in review | Adults ~27–47%; children ~45–65% (strom2025genomewideanalysesidentify pages 1-2); broader review notes genetic contribution ~35–50% (roh2023clinicaladvancesin pages 1-2) | Higher heritability in pediatric-onset OCD supports stronger genetic loading in early-onset presentations (strom2025genomewideanalysesidentify pages 1-2, liu2023earlyidentificationand pages 1-2) |
| WDR6 | 2q33 | WD repeat domain 6; prioritized likely causal effector gene | GWAS + gene prioritization + TWAS-COLOC/SMR-HEIDI | Among 25 genes prioritized as most likely causal; implicated by multiple methods (strom2025genomewideanalysesidentify pages 1-2, strom2025genomewideanalysesidentify pages 3-4) | One of only two genes prioritized by both TWAS-COLOC and SMR-HEIDI filters, strengthening causal inference beyond positional association alone (strom2025genomewideanalysesidentify pages 3-4) |
| DALRD3 | 2q33 | DALR anticodon binding domain-containing 3; prioritized likely causal effector gene | GWAS + gene prioritization + TWAS-COLOC/SMR-HEIDI | Among 25 genes prioritized as most likely causal; implicated by multiple methods (strom2025genomewideanalysesidentify pages 1-2, strom2025genomewideanalysesidentify pages 3-4) | Along with WDR6, one of the strongest cross-method priority genes, supported by convergent colocalization/causality filters (strom2025genomewideanalysesidentify pages 3-4) |
| CTNND1 | 6p22 | Catenin delta-1; adhesion/synaptic-related gene, prioritized candidate | GWAS + TWAS + PWAS + colocalization | CTNND1 protein downregulation in human dlPFC associated with OCD risk: Z = -4.49, P = 7.11×10⁻⁶; TWAS in prefrontal cortex: Z = -6.86, P = 6.90×10⁻¹² (strom2025genomewideanalysesidentify pages 3-4) | Especially notable because it was implicated by three orthogonal approaches (mBAT-combo, TWAS, PWAS) and also showed evidence for colocalization, making it one of the most biologically convergent OCD genes (strom2025genomewideanalysesidentify pages 3-4) |
| MHC region / 6p21.33 locus | 6p21.33 | Major histocompatibility complex region; dense immune-related locus | GWAS | Lead SNP rs4990036, P = 1.45×10⁻¹¹; 118 genes within regional window (strom2025genomewideanalysesidentify pages 2-3) | MHC-region signal suggests possible neuroimmune contribution to OCD biology, although fine-mapping is challenging because of high linkage disequilibrium and gene density (strom2025genomewideanalysesidentify pages 1-2, strom2025genomewideanalysesidentify pages 2-3) |
| rs78587207 locus | 11q12.1 | Genome-wide significant lead SNP region | GWAS | P = 5.28×10⁻¹² (strom2025genomewideanalysesidentify pages 2-3) | One of the strongest individual loci in the meta-analysis; also overlaps signals seen in schizophrenia, well-being, neuroticism, and educational attainment databases (strom2025genomewideanalysesidentify pages 2-3) |
| rs13262595 locus | 8q24.3 | Genome-wide significant lead SNP region | GWAS | P = 1.31×10⁻¹¹ (strom2025genomewideanalysesidentify pages 2-3) | Strong association signal with cross-trait overlap including schizophrenia, neuroticism, and educational attainment, highlighting pleiotropy (strom2025genomewideanalysesidentify pages 2-3) |
| rs10877425 locus | 12q14.1 | Genome-wide significant lead SNP region | GWAS | P = 1.62×10⁻¹¹ (strom2025genomewideanalysesidentify pages 2-3) | High-confidence OCD locus without a highlighted nearby gene in the summary table, illustrating that some strong associations remain functionally unresolved (strom2025genomewideanalysesidentify pages 2-3) |
| rs7626445 locus | 3p21.31 | Genome-wide significant lead SNP region | GWAS | P = 1.74×10⁻¹¹ (strom2025genomewideanalysesidentify pages 2-3) | Associated region overlaps neuroticism, smoking, blood cell count, and height traits, again indicating polygenic pleiotropy (strom2025genomewideanalysesidentify pages 2-3) |
| rs2564930 locus | 3p21.1 | Genome-wide significant lead SNP region | GWAS | P = 3.41×10⁻¹¹ (strom2025genomewideanalysesidentify pages 2-3) | Strong signal in a region also linked to schizophrenia, neuroticism, blood cell count, and BMI (strom2025genomewideanalysesidentify pages 2-3) |
| rs4702 locus | 15q26.1 | Genome-wide significant lead SNP region | GWAS | P = 9.07×10⁻¹⁰ (strom2025genomewideanalysesidentify pages 2-3) | Notable because the same locus shows associations with bipolar disorder, major depressive disorder, and risk-taking behavior, consistent with shared psychiatric liability (strom2025genomewideanalysesidentify pages 2-3) |
| Gene-based discovery summary | Genome-wide | Aggregated gene-level prioritization from multiple methods | mBAT-combo / TWAS / SMR / PWAS / PsyOPS | 251 genes significant in at least one gene-based method; 48 genes implicated by ≥2 methods; 25 genes passed additional causal-support filters (strom2025genomewideanalysesidentify pages 2-3, strom2025genomewideanalysesidentify pages 3-4) | Multi-method integration greatly narrowed the candidate list from hundreds of genes to a smaller set of more plausible effector genes for functional follow-up (strom2025genomewideanalysesidentify pages 2-3, strom2025genomewideanalysesidentify pages 3-4) |
| Tissue enrichment | Brain tissues | Regional expression enrichment of OCD-associated genes | MAGMA / LDSC | Enrichment seen in anterior cingulate cortex, frontal cortex, cortex, nucleus accumbens, hippocampus, caudate, putamen, hypothalamus, substantia nigra, cerebellum and related brain tissues (strom2025genomewideanalysesidentify pages 3-4) | Supports a brain-circuit model centered on cortico-striatal and limbic systems rather than a diffuse whole-body signal (strom2025genomewideanalysesidentify pages 3-4, jalal2023obsessive‐compulsivedisorderetiology pages 2-3) |
| Cell-type enrichment | Hippocampus, cortex, striatum | Neuronal cell classes implicated by genetic risk | Single-cell enrichment from GWAS signals | Significant enrichment in excitatory neurons in hippocampus/cortex and D1/D2 dopamine receptor-containing medium spiny neurons in striatum (strom2025genomewideanalysesidentify pages 1-2, strom2025genomewideanalysesidentify pages 3-4) | Provides cell-type specificity linking OCD genetic risk to excitatory cortical/hippocampal neurons and striatal medium spiny neurons, consistent with CSTC circuit models (strom2025genomewideanalysesidentify pages 1-2, strom2025genomewideanalysesidentify pages 3-4, jalal2023obsessive‐compulsivedisorderetiology pages 2-3) |
| Cross-trait genetic correlations | Genome-wide | Shared inherited liability with other disorders/traits | GWAS genetic correlation | OCD shared genetic risk with 65 of 112 phenotypes; especially anxiety, depression, anorexia nervosa, Tourette syndrome; negative associations with inflammatory bowel diseases, educational attainment, and BMI (strom2025genomewideanalysesidentify pages 1-2) | Reinforces that OCD genetics overlap substantially with other psychiatric phenotypes while also showing inverse relationships with some immune/metabolic traits (strom2025genomewideanalysesidentify pages 1-2) |
| Ascertainment and heterogeneity analyses | Genome-wide | Robustness of results across cohorts | GWAS / GenomicSEM | No statistically significant heterogeneity across the 30 lead loci by Cochran’s Q; moderate-to-high genetic correlations across ascertainment subgroups (strom2025genomewideanalysesidentify pages 2-3) | Suggests that major loci are broadly consistent across different OCD cohorts, even though ascertainment strategy influences genome-wide architecture to some extent (strom2025genomewideanalysesidentify pages 2-3) |


*Table: This table summarizes the major genetic findings for obsessive-compulsive disorder from recent large-scale GWAS and gene-prioritization analyses. It highlights the most important loci, candidate genes, heritability estimates, and polygenic architecture features that are most useful for a disease knowledge base.*

## 3. Phenotypes

### Symptom Dimensions
OCD symptoms are classified into partially distinct subtypes (jalal2023obsessive‐compulsivedisorderetiology pages 2-3):
1. Contamination fears and compulsive cleaning
2. Obsessive thoughts about causing harm and compulsive checking
3. Obsessions with symmetry and compulsive ordering
4. Obsessions with collecting and compulsive hoarding (now a separate disorder in DSM-5)
5. Purely obsessional subtype with unwanted thoughts about sex, violence, and blasphemy

**Suggested HPO Terms:**
- HP:0000722 (Obsessive-compulsive behavior)
- HP:0000733 (Repetitive compulsive behavior)
- HP:0000723 (Restricted interests)

### Phenotype Characteristics

**Age of Onset:** OCD demonstrates a bimodal onset with peaks at 12-14 years and 20-22 years (liu2023earlyidentificationand pages 1-2). More than 80% of OCD cases begin by early adulthood (stein2025obsessivecompulsivedisorderin pages 1-2). Half of adult patients exhibited symptoms starting in childhood or adolescence (farrell2023closingthegap pages 1-2, liu2023earlyidentificationand pages 1-2).

**Severity:** In community samples, most OCD cases are mild (47.0%) or very mild (27.5%), with smaller percentages designated as moderate (22.9%) or severe (2.7%) by Yale-Brown Obsessive-Compulsive Scale (stein2025obsessivecompulsivedisorderin pages 1-2).

**Progression:** OCD typically starts in childhood or adolescence and often persists throughout life, causing functional impairment across multiple domains (roh2023clinicaladvancesin pages 1-2). The 12-month prevalence (3.0%) is nearly as high as lifetime prevalence (4.1%), suggesting highly persistent course (stein2025obsessivecompulsivedisorderin pages 1-2).

### Quality of Life Impact
OCD causes substantial disability and is among the leading causes of illness-related burden according to the World Health Organization (roh2023clinicaladvancesin pages 1-2, farrell2023closingthegap pages 1-2). Childhood onset is associated with greater OCD severity, more symptoms, higher comorbidity, and poorer prognosis relative to adult onset (farrell2023closingthegap pages 1-2).

## 4. Genetic/Molecular Information

### Causal Genes and Pathogenic Variants
The 2025 GWAS meta-analysis identified 249 potential effector genes for OCD, with 25 classified as most likely causal candidates (strom2025genomewideanalysesidentify pages 1-2). Key genes include:

- **WDR6** (2q33): WD repeat domain 6, prioritized by both TWAS-COLOC and SMR-HEIDI causality filters (strom2025genomewideanalysesidentify pages 3-4)
- **DALRD3** (2q33): DALR anticodon binding domain-containing 3, also prioritized by convergent causal inference methods (strom2025genomewideanalysesidentify pages 3-4)
- **CTNND1** (6p22): Catenin delta-1, implicated by three orthogonal approaches (mBAT-combo, TWAS, PWAS) with evidence for colocalization; protein downregulation in dorsolateral prefrontal cortex associated with OCD risk (Z = -4.49, P = 7.11×10⁻⁶) (strom2025genomewideanalysesidentify pages 3-4)
- **MHC region genes** (6p21.33): Multiple genes in the major histocompatibility complex region (strom2025genomewideanalysesidentify pages 1-2, strom2025genomewideanalysesidentify pages 2-3)

### Variant Classification
The current evidence primarily derives from common variant GWAS rather than rare coding variants. The polygenic architecture suggests thousands of small-effect variants rather than high-penetrance mutations (strom2025genomewideanalysesidentify pages 2-3).

### Cell Type and Tissue Enrichment
OCD genetic risk shows significant enrichment in:
- **Excitatory neurons** in hippocampus and cerebral cortex
- **D1 and D2 type dopamine receptor-containing medium spiny neurons** in the striatum (strom2025genomewideanalysesidentify pages 1-2, strom2025genomewideanalysesidentify pages 3-4)

Tissue enrichment analysis revealed significant signals in anterior cingulate cortex, frontal cortex, nucleus accumbens, hippocampus, caudate, putamen, hypothalamus, and cerebellum (strom2025genomewideanalysesidentify pages 3-4).

## 5. Environmental Information

### Environmental Factors
The specific environmental contributors to OCD remain under active investigation. The OCDTWIN project is systematically evaluating early life exposures including perinatal variables, psychosocial stressors, and health-related information through register linkages (dhiman2025hereditarypatternsand pages 1-1).

### Lifestyle Factors
Limited specific data available from retrieved sources.

## 6. Mechanism / Pathophysiology

### Molecular Pathways
The dominant pathophysiological model implicates dysfunction in cortico-striato-thalamo-cortical (CSTC) circuits (jalal2023obsessive‐compulsivedisorderetiology pages 1-2, roh2023clinicaladvancesin pages 1-2, jalal2023obsessive‐compulsivedisorderetiology pages 2-3). These parallel circuits are responsible for reward and motivational processes, executive function, motor and response inhibition, and habit-based behavior (jalal2023obsessive‐compulsivedisorderetiology pages 2-3).

Key CSTC circuits include (jalal2023obsessive‐compulsivedisorderetiology pages 2-3):
1. **Affective circuit**: Projects from anterior cingulate cortex (ACC) and ventromedial prefrontal cortex (vmPFC) to nucleus accumbens, involved in emotion and reward processing
2. **Dorsal cognitive circuit**: Projects from dorsolateral prefrontal cortex (dlPFC) to caudate nucleus, pertinent to executive function and working memory
3. **Ventral cognitive circuit**: Projects from anterolateral orbitofrontal cortex to putamen, responsible for motor and response inhibition
4. **Sensorimotor circuit**: Projects from premotor cortical regions to putamen, involved in habit-based behavior

### Neurochemical Systems
**Serotonin:** Dysfunction in serotonergic neurotransmission is strongly implicated, as evidenced by the efficacy of selective serotonin reuptake inhibitors (SSRIs) (roh2023clinicaladvancesin pages 1-2, jalal2023obsessive‐compulsivedisorderetiology pages 2-3).

**Dopamine:** Dopaminergic systems play an important role, particularly in striatal function and the generation of compulsive behaviors (jalal2023obsessive‐compulsivedisorderetiology pages 2-3).

**Glutamate:** Glutamatergic dysregulation within CSTC circuits is increasingly recognized as contributing to OCD pathophysiology (jalal2023obsessive‐compulsivedisorderetiology pages 2-3).

### Cellular Processes
OCD involves aberrant activity within CSTC circuits, with evidence of overactivity in orbitofrontal cortex and striatum that can normalize following successful pharmacological and psychological treatment (jalal2023obsessive‐compulsivedisorderetiology pages 2-3).

**Suggested GO Terms:**
- GO:0007165 (Signal transduction)
- GO:0007268 (Chemical synaptic transmission)
- GO:0042493 (Response to drug)
- GO:0050890 (Cognition)

**Suggested CL Terms:**
- CL:0000540 (Neuron)
- CL:0000100 (Motor neuron)
- CL:0000679 (Glutamatergic neuron)

## 7. Anatomical Structures Affected

### Organ and System Level
**Primary Organs:** Central nervous system, particularly brain regions within CSTC circuits

**Brain Systems:** 
- Orbitofrontal cortex (OFC)
- Anterior cingulate cortex (ACC)
- Dorsolateral prefrontal cortex (dlPFC)
- Ventromedial prefrontal cortex (vmPFC)
- Striatum (caudate nucleus, putamen, nucleus accumbens)
- Thalamus
- Cerebellum (jalal2023obsessive‐compulsivedisorderetiology pages 2-3, strom2025genomewideanalysesidentify pages 3-4)

### Cell and Tissue Level
**Cell Types Affected:**
- Excitatory neurons in hippocampus and cortex
- D1 and D2 dopamine receptor-containing medium spiny neurons in striatum (strom2025genomewideanalysesidentify pages 1-2, strom2025genomewideanalysesidentify pages 3-4)

**Suggested UBERON Terms:**
- UBERON:0000955 (Brain)
- UBERON:0002037 (Cerebellum)
- UBERON:0001950 (Neocortex)
- UBERON:0002435 (Striatum)
- UBERON:0001897 (Thalamus)

## 8. Temporal Development

### Onset
**Typical Age of Onset:** Bimodal distribution with peaks at 12-14 years and 20-22 years (liu2023earlyidentificationand pages 1-2). More than 80% of cases begin by early adulthood, with more than half of adult OCD patients having onset in childhood or adolescence (stein2025obsessivecompulsivedisorderin pages 1-2, farrell2023closingthegap pages 1-2).

**Onset Pattern:** Can be acute, subacute, or insidious. Childhood-onset OCD is associated with greater severity and higher genetic loading compared to adult-onset (farrell2023closingthegap pages 1-2, liu2023earlyidentificationand pages 1-2).

### Progression
**Disease Course:** OCD typically demonstrates a chronic course with high persistence. The 12-month prevalence (3.0%) nearly equals lifetime prevalence (4.1%), suggesting minimal spontaneous remission (stein2025obsessivecompulsivedisorderin pages 1-2). Studies in youth suggest a higher percentage have an episodic course compared to adults (liu2023earlyidentificationand pages 1-2).

**Duration:** Delayed diagnosis is common, with a gap between onset and diagnosis of approximately 7-10 years in adults and more than 2 years in children (liu2023earlyidentificationand pages 1-2). Australian data suggest more than 9 years of untreated illness for OCD (farrell2023closingthegap pages 1-2).

## 9. Inheritance and Population

### Epidemiology
**Prevalence:** Lifetime prevalence across 10 countries in World Mental Health surveys is 4.1%, with 12-month prevalence of 3.0% (stein2025obsessivecompulsivedisorderin pages 1-2). Estimates from literature range from 1-3% of the general population (jalal2023obsessive‐compulsivedisorderetiology pages 1-2, strom2025genomewideanalysesidentify pages 1-2).

**Incidence:** Pediatric-onset OCD affects approximately 2-4% of children and adolescents (liu2023earlyidentificationand pages 1-2).

### Inheritance Pattern
OCD demonstrates polygenic inheritance with moderate heritability. Twin-based heritability: 27-47% in adults, 45-65% in children (dhiman2025hereditarypatternsand pages 1-1, strom2025genomewideanalysesidentify pages 1-2). Family studies show OCD is more prevalent in first-degree relatives of affected individuals (farrell2023closingthegap pages 1-2).

### Population Demographics
**Age Distribution:** Bimodal onset with peaks in adolescence (12-14 years) and young adulthood (20-22 years) (liu2023earlyidentificationand pages 1-2).

**Sex Ratio:** Available sources did not provide definitive male:female ratios.

**Geographic Distribution:** OCD appears cross-culturally prevalent with relatively consistent rates across high-income countries (HICs) and low-middle income countries (LMICs), though treatment rates are much higher in HICs (40.5%) than LMICs (7.0%) (stein2025obsessivecompulsivedisorderin pages 1-2).

## 10. Diagnostics

### Clinical Criteria
**DSM-5 Diagnostic Criteria:** Presence of obsessions and/or compulsions that are time-consuming (>1 hour/day) and cause significant distress or functional impairment. Symptoms must not be attributable to other mental or physical disorders (jalal2023obsessive‐compulsivedisorderetiology pages 1-2). 

**Differential Diagnosis:** Must distinguish from other obsessive-compulsive and related disorders, anxiety disorders, and psychotic disorders. Level of insight distinguishes OCD with poor/absent insight from primary psychotic illness (jalal2023obsessive‐compulsivedisorderetiology pages 1-2).

### Clinical Tests
**Severity Assessment:** Yale-Brown Obsessive-Compulsive Scale (Y-BOCS) is the standard severity measure (stein2025obsessivecompulsivedisorderin pages 1-2).

**Imaging Studies:** Neuroimaging reveals functional abnormalities in CSTC circuits, particularly in orbitofrontal cortex, anterior cingulate cortex, striatum, and thalamus (jalal2023obsessive‐compulsivedisorderetiology pages 2-3). Both structural MRI and functional MRI demonstrate aberrant CSTC connectivity and activity (jalal2023obsessive‐compulsivedisorderetiology pages 2-3).

### Genetic Testing
While specific genes have been identified through GWAS, genetic testing is not currently part of routine clinical diagnosis given the highly polygenic architecture. Research applications include whole exome sequencing and genome-wide genotyping for risk prediction and mechanistic studies (strom2025genomewideanalysesidentify pages 1-2).

## 11. Outcome/Prognosis

### Disease Course and Morbidity
OCD is highly persistent, with 12-month prevalence nearly matching lifetime prevalence (stein2025obsessivecompulsivedisorderin pages 1-2). The condition causes substantial functional impairment across academic, occupational, and social domains (farrell2023closingthegap pages 1-2). Childhood onset is associated with greater severity, more symptoms, and poorer prognosis than adult onset (farrell2023closingthegap pages 1-2).

### Quality of Life
OCD is ranked among the leading causes of illness-related disability by the World Health Organization (roh2023clinicaladvancesin pages 1-2). The disorder significantly impacts daily functioning, with severe cases experiencing substantial disability in occupational and social domains (farrell2023closingthegap pages 1-2).

### Treatment Response
Only 19.8% of respondents with OCD in World Mental Health surveys received any mental health treatment in the past year (stein2025obsessivecompulsivedisorderin pages 1-2). Approximately 50% of OCD patients do not respond adequately to initial treatments (huang2025advancingobsessive–compulsivedisorder pages 1-2). Treatment adherence during exposure and response prevention predicts both short-term and long-term outcomes (farrell2023closingthegap pages 1-2).

## 12. Treatment

### Pharmacotherapy
**First-Line:** Selective serotonin reuptake inhibitors (SSRIs) including fluoxetine, sertraline, fluvoxamine, paroxetine, and escitalopram are considered first-line pharmacotherapy (roh2023clinicaladvancesin pages 1-2, huang2025advancingobsessive–compulsivedisorder pages 1-2). SSRIs modulate serotonergic neurotransmission and downstream CSTC circuit activity (roh2023clinicaladvancesin pages 1-2).

**Augmentation:** Atypical antipsychotics are used for augmentation in SSRI partial responders, particularly those with tic-related presentations (roh2023clinicaladvancesin pages 1-2).

### Psychotherapy
**Cognitive Behavioral Therapy with Exposure and Response Prevention (CBT-ERP):** Gold-standard psychological treatment involving systematic exposure to obsessional triggers with prevention of compulsive responses (roh2023clinicaladvancesin pages 1-2, farrell2023closingthegap pages 1-2). CBT-ERP promotes inhibitory learning, fear extinction, and improved cognitive control (farrell2023closingthegap pages 1-2).

**Treatment Modalities:** Delivered through individual therapy, family-based approaches, group therapy, and internet-delivered formats. Intensive or concentrated ERP (over consecutive days) may be beneficial for severe or treatment-resistant cases (farrell2023closingthegap pages 1-2).

### Advanced Therapeutics
**Neuromodulation:** Transcranial magnetic stimulation (TMS) and deep brain stimulation (DBS) targeting CSTC circuit nodes are used for treatment-refractory OCD (roh2023clinicaladvancesin pages 1-2, huang2025advancingobsessive–compulsivedisorder pages 1-2).

**Neurosurgical Interventions:** Ablative procedures such as anterior cingulotomy are reserved for severe, treatment-refractory cases (jalal2023obsessive‐compulsivedisorderetiology pages 2-3).

### Treatment Strategy
Staged-care models match treatment intensity to illness severity, comorbidity burden, and prior treatment response. This approach aims to deliver "right care, first time" and close treatment gaps (farrell2023closingthegap pages 1-2).

**Suggested MAXO Terms:**
- MAXO:0000011 (Psychotherapy)
- MAXO:0000058 (Pharmacotherapy)
- MAXO:0001298 (Cognitive behavioral therapy)

| Treatment Category | Specific Interventions | Mechanism of Action | Evidence Level | Efficacy/Response Rates | Key Citations |
|---|---|---|---|---|---|
| First-line psychotherapy | Cognitive behavioral therapy with exposure and response prevention (CBT-ERP); individual, family-based, group, internet/digital, and staged-care CBT-ERP for youth | Repeated, systematic exposure to obsessional triggers with prevention of rituals/avoidance; promotes inhibitory learning, fear extinction, reduced negative reinforcement, and improved cognitive control over compulsions | High; described as gold-standard/first-line in recent reviews and guidelines | Strong efficacy across adults and youth; not all patients remit, and a substantial minority remain symptomatic; pediatric review notes CBT-ERP is highly effective, though underused in practice; adherence during ERP predicts better short- and long-term outcomes (roh2023clinicaladvancesin pages 1-2, farrell2023closingthegap pages 1-2) | (roh2023clinicaladvancesin pages 1-2, farrell2023closingthegap pages 1-2) |
| First-line pharmacotherapy | Selective serotonin reuptake inhibitors (SSRIs): fluoxetine, sertraline, fluvoxamine, paroxetine, escitalopram/citalopram (class-level evidence emphasized) | Block serotonin reuptake, increasing synaptic serotonin; downstream modulation of cortico-striato-thalamo-cortical (CSTC) circuit activity and symptom-related salience processing | High; consistently recommended as first-line pharmacotherapy in adult OCD reviews | Effective for many patients, but a large proportion show only partial response; one 2025 review cited in retrieved evidence notes ~50% may not respond adequately to standard treatments; SSRIs and CBT both reduce symptoms, with partly distinct neural effects and common reduction of insula activity during symptom provocation after treatment (roh2023clinicaladvancesin pages 1-2, huang2025advancingobsessive–compulsivedisorder pages 1-2) | (roh2023clinicaladvancesin pages 1-2, huang2025advancingobsessive–compulsivedisorder pages 1-2) |
| Combined first-line treatment | CBT-ERP plus SSRI, especially for moderate-severe illness, comorbidity, or partial response to monotherapy | Combines behavioral extinction/response prevention with serotonergic modulation of CSTC dysfunction | Moderate-high; recommended in treatment overviews and staged-care models | Used when symptom burden, comorbidity, or prior treatment history justify escalation; recent pediatric staged-care framework recommends matching intensity to severity and previous response rather than one-size-fits-all care (roh2023clinicaladvancesin pages 1-2, farrell2023closingthegap pages 1-2) | (roh2023clinicaladvancesin pages 1-2, farrell2023closingthegap pages 1-2) |
| Second-line / augmentation | Atypical antipsychotic augmentation of SSRIs (class-level; e.g., risperidone/aripiprazole commonly referenced in OCD practice reviews), especially for SSRI partial responders or tic-related presentations | Dopamine/serotonin receptor modulation; intended to reduce persistent compulsivity and augment SSRI effect in refractory CSTC dysfunction | Moderate; recommended in adult treatment reviews as augmentation rather than monotherapy | Useful in a subset of partial responders; evidence supports use after adequate SSRI trial and/or CBT failure rather than as initial treatment (roh2023clinicaladvancesin pages 1-2) | (roh2023clinicaladvancesin pages 1-2) |
| Second-line / treatment optimization | High-intensity or concentrated ERP; intensive outpatient/residential ERP; improving adherence and therapist fidelity | Increases exposure dose, reduces accommodation/avoidance, and strengthens ritual prevention in severe or chronic cases | Moderate; supported by clinical studies and service-model literature | Treatment adherence predicts post-treatment, 3-month, and 1-year OCD severity and work/social functioning in difficult-to-treat cases, suggesting optimization of ERP delivery is a key modifiable lever (farrell2023closingthegap pages 1-2) | (farrell2023closingthegap pages 1-2) |
| Novel / experimental neuromodulation | Repetitive transcranial magnetic stimulation (TMS), including circuit-targeted stimulation approaches | Noninvasive modulation of dysfunctional frontostriatal/CSTC activity, potentially affecting inhibition, salience, and compulsive motor patterns | Emerging/moderate; highlighted in recent reviews as promising but not universally first-line | Considered for refractory OCD; recent reviews frame TMS as a developing option alongside advances in neuroimaging/electrophysiology-guided personalization (roh2023clinicaladvancesin pages 1-2) | (roh2023clinicaladvancesin pages 1-2) |
| Novel / experimental neuromodulation | Deep brain stimulation (DBS) targeting CSTC-related nodes; ventral/striatal and related circuit targets discussed in recent reviews | Direct electrical modulation of pathologic frontostriatal network dynamics in severe, treatment-refractory OCD | Moderate for severe refractory illness; generally reserved for highly selected patients | Used after failure of standard therapies; recent modeling/review work emphasizes frontostriatal circuit rebalancing as the conceptual basis for benefit (huang2025advancingobsessive–compulsivedisorder pages 1-2, jalal2023obsessive‐compulsivedisorderetiology pages 2-3) | (huang2025advancingobsessive–compulsivedisorder pages 1-2, jalal2023obsessive‐compulsivedisorderetiology pages 2-3) |
| Neurosurgical interventions | Ablative neurosurgery/lesion procedures such as anterior cingulotomy or related psychosurgical approaches in extreme refractory cases | Interrupts maladaptive CSTC loops implicated in persistent obsessions/compulsions | Limited but established for rare, severe, otherwise intractable cases | Historical and contemporary literature cited in recent reviews indicates symptom improvement can occur in carefully selected severe cases; reserved for last-resort use due to invasiveness (jalal2023obsessive‐compulsivedisorderetiology pages 2-3) | (jalal2023obsessive‐compulsivedisorderetiology pages 2-3) |
| Treatment resistance approaches | Personalized staged-care pathways; escalation based on severity, comorbidity, and prior treatment history; multimodal service design | Matches treatment intensity to illness stage and complexity; aims to reduce undertreatment and delayed access | Moderate; especially developed in pediatric OCD service literature | Proposed to close the “treatment gap” and “quality gap”; youth OCD often experiences long delays to care, and staged models aim to deliver the least intrusive effective intervention first, escalating as needed (farrell2023closingthegap pages 1-2, liu2023earlyidentificationand pages 1-2) | (farrell2023closingthegap pages 1-2, liu2023earlyidentificationand pages 1-2) |
| Treatment resistance approaches | Mechanism-informed monitoring with imaging/brain-based biomarkers (research use), and circuit-informed intervention selection | Uses neural signatures such as insula/frontostriatal activity to understand or predict response and tailor interventions | Emerging/experimental | 2024 longitudinal imaging study found CBT and SSRIs both reduced symptoms but produced partly divergent brain changes, with a common reduction in insula activity during symptom provocation; currently more useful mechanistically than diagnostically in routine care (roh2023clinicaladvancesin pages 1-2) | (roh2023clinicaladvancesin pages 1-2) |


*Table: This table summarizes current OCD treatment strategies across first-line, second-line, experimental, and treatment-resistant settings. It highlights mechanisms, approximate evidence strength, and clinically relevant outcome patterns from recent reviews and studies.*

## 13. Prevention

### Secondary Prevention
Early identification and intervention in pediatric OCD is critical, as delayed treatment is associated with worse prognosis (liu2023earlyidentificationand pages 1-2). Interventions focus on preventing conversion of obsessive-compulsive symptoms into full-blown OCD (liu2023earlyidentificationand pages 1-2).

### Tertiary Prevention
Focuses on alleviating mild to moderate OCD and preventing complications, though interventions for comorbidities remain in their infancy (liu2023earlyidentificationand pages 1-2).

### Screening
Systematic screening programs for OCD are not currently widespread. The duration of untreated OCD remains among the highest of all psychiatric disorders, highlighting need for improved early detection (liu2023earlyidentificationand pages 1-2).

## 14. Other Species / Natural Disease

Limited information available in retrieved sources regarding naturally occurring OCD in other species.

## 15. Model Organisms

### Genetic Models
Multiple transgenic mouse models have been developed to study OCD mechanisms (huang2025advancingobsessive–compulsivedisorder pages 1-2):

**Key Mouse Models:**
- **Hoxb8-KO:** Excessive grooming/self-injury phenotype
- **Slc1a1-KO:** Glutamatergic dysfunction model
- **Sapap3-KO:** Well-established compulsive grooming model with corticostriatal synaptic abnormalities
- **Slitrk5-KO:** Excessive grooming and anxiety-like behaviors
- **Spred2-KO:** Repetitive grooming/compulsive-like behavior

### Circuit Models
Optogenetic stimulation of orbitofrontal cortex-ventromedial striatum (OFC-VMS) connections can induce OCD-like grooming behaviors in mice, supporting the CSTC circuit model (jalal2023obsessive‐compulsivedisorderetiology pages 2-3).

### Zebrafish Models
Zebrafish models with altered slitrk5a demonstrate OCD-like "checking" behaviors, useful for high-throughput screening (huang2025advancingobsessive–compulsivedisorder pages 1-2).

### Model Limitations
No single model captures the full human OCD syndrome, particularly intrusive obsessions, symptom dimensions, fluctuating insight, and comorbidity patterns (huang2025advancingobsessive–compulsivedisorder pages 1-2, jalal2023obsessive‐compulsivedisorderetiology pages 2-3).

| Model Type | Specific Model Name | Species | Genes Involved | OCD-like Phenotypes Observed | Brain Regions/Circuits Affected | Utility/Applications | Limitations |
|---|---|---|---|---|---|---|---|
| Genetic knockout | Hoxb8-KO | Mouse | **Hoxb8** | Excessive grooming/self-injury–like repetitive behavior; compulsive grooming phenotype used as an OCD-relevant endophenotype | Cortico-striato-thalamo-cortical (CSTC)-relevant circuitry broadly implicated; also linked to microglial/hematopoietic contributions rather than a single canonical OCD node (huang2025advancingobsessive–compulsivedisorder pages 1-2) | Useful for studying repetitive grooming, neuroimmune contributions, and disentangling compulsive motor output from anxiety-like behaviors (huang2025advancingobsessive–compulsivedisorder pages 1-2) | Face validity for grooming is strong, but limited construct validity for intrusive obsessions; captures only a subset of human OCD phenomenology (huang2025advancingobsessive–compulsivedisorder pages 1-2) |
| Genetic knockout | Slc1a1-KO | Mouse | **Slc1a1** / EAAT3 | Repetitive/compulsive-like behaviors and anxiety-related phenotypes in an OCD risk-gene framework | Glutamatergic signaling within CSTC-related circuits; striatum/cortex glutamate homeostasis is the main mechanistic relevance (huang2025advancingobsessive–compulsivedisorder pages 1-2, jalal2023obsessive‐compulsivedisorderetiology pages 2-3) | Useful for probing glutamatergic mechanisms and testing candidate glutamate-modulating interventions (huang2025advancingobsessive–compulsivedisorder pages 1-2, jalal2023obsessive‐compulsivedisorderetiology pages 2-3) | Human OCD is polygenic; single-gene knockout incompletely models symptom heterogeneity and cognitive obsessions (huang2025advancingobsessive–compulsivedisorder pages 1-2) |
| Genetic knockout | Sapap3-KO | Mouse | **Sapap3 / Dlgap3** | Excessive grooming, anxiety-like behavior, repetitive acts; one of the best-established compulsive grooming models | Corticostriatal synapses, especially striatal dysfunction within CSTC circuitry (huang2025advancingobsessive–compulsivedisorder pages 1-2, jalal2023obsessive‐compulsivedisorderetiology pages 2-3) | High translational value for corticostriatal synaptopathy, habit/compulsivity mechanisms, and rescue experiments with circuit or pharmacologic interventions (huang2025advancingobsessive–compulsivedisorder pages 1-2) | Strong for compulsions/grooming but does not model intrusive obsessions or full symptom dimensions seen in humans (huang2025advancingobsessive–compulsivedisorder pages 1-2, jalal2023obsessive‐compulsivedisorderetiology pages 2-3) |
| Genetic knockout | Slitrk5-KO | Mouse | **Slitrk5** | Excessive grooming and anxiety-like/compulsive-like behaviors | Orbitofrontal-striatal and broader CSTC dysfunction relevant to compulsivity (huang2025advancingobsessive–compulsivedisorder pages 1-2, jalal2023obsessive‐compulsivedisorderetiology pages 2-3) | Useful for studying synaptogenesis-related mechanisms and corticostriatal abnormalities in OCD-like behavior (huang2025advancingobsessive–compulsivedisorder pages 1-2) | Limited to a narrow behavioral phenotype; genetic effect sizes in humans are smaller and more polygenic than in knockout models (huang2025advancingobsessive–compulsivedisorder pages 1-2) |
| Genetic knockout | Spred2-KO | Mouse | **Spred2** | Repetitive grooming/compulsive-like behavior in transgenic OCD modeling summaries | CSTC-related signaling abnormalities; mechanistically linked to intracellular signaling regulation rather than a single OCD-specific node (huang2025advancingobsessive–compulsivedisorder pages 1-2) | Useful for investigating intracellular signaling contributions to repetitive behavior and for comparative model selection across transgenic strains (huang2025advancingobsessive–compulsivedisorder pages 1-2) | Less extensively validated than Sapap3-KO; uncertain breadth of translational relevance to diverse OCD symptom dimensions (huang2025advancingobsessive–compulsivedisorder pages 1-2) |
| Genetic/optogenetic circuit model | Repeated OFC–VMS stimulation model | Mouse | Circuit perturbation model rather than a single gene | Induced OCD-like grooming/compulsive behavior after repeated stimulation | **Orbitofrontal cortex (OFC)** and **ventromedial striatum (VMS)** within CSTC loops (jalal2023obsessive‐compulsivedisorderetiology pages 2-3) | Strong causal tool for testing whether abnormal CSTC activity can generate compulsive behaviors; valuable for circuit-level intervention studies (jalal2023obsessive‐compulsivedisorderetiology pages 2-3) | Not a natural disease model; limited ecological validity and does not capture developmental/polygenic aspects of OCD (jalal2023obsessive‐compulsivedisorderetiology pages 2-3) |
| Transgenic model class | Knockout mouse models (aggregate class reviewed in recent literature) | Mouse | Includes **Hoxb8, Slc1a1, Sapap3, Slitrk5, Spred2** | Repetitive grooming, anxiety-like behavior, compulsive-like rituals; model-specific variation | Recurrently implicate **CSTC circuits**, especially orbitofrontal, striatal, and thalamic pathway abnormalities (huang2025advancingobsessive–compulsivedisorder pages 1-2, jalal2023obsessive‐compulsivedisorderetiology pages 2-3) | Comparative platform for selecting models by mechanism: synaptic, glutamatergic, signaling, or neuroimmune hypotheses; supports neuromodulation and drug development work (huang2025advancingobsessive–compulsivedisorder pages 1-2) | No single model captures the full human syndrome, especially obsessions, symptom dimensions, fluctuating insight, and comorbidity (huang2025advancingobsessive–compulsivedisorder pages 1-2, jalal2023obsessive‐compulsivedisorderetiology pages 2-3) |
| Zebrafish genetic model | **slitrk5a** altered zebrafish model | Zebrafish | **slitrk5a** | “Checking”-like repetitive behavior reported as OCD-like in zebrafish model literature | Vertebrate brain circuit analogs relevant to repetitive behavioral control; not directly homologous to mammalian CSTC architecture (huang2025advancingobsessive–compulsivedisorder pages 1-2) | Useful for high-throughput genetics and drug screening, rapid developmental studies, and comparative validation of OCD risk genes (huang2025advancingobsessive–compulsivedisorder pages 1-2) | Behavioral homology to human obsessions/compulsions is indirect; circuit correspondence to human OCD is limited (huang2025advancingobsessive–compulsivedisorder pages 1-2) |
| Other species/model note | Zebrafish and other lower-animal OCD-relevant models (general mention) | Zebrafish / lower vertebrates | Varies by construct | Repetitive/compulsive-like phenotypes are used as analog readouts | Developmental and conserved neural pathway studies; not direct one-to-one CSTC replication (huang2025advancingobsessive–compulsivedisorder pages 1-2) | Helpful for scalable screening and testing conserved gene-function effects across species (huang2025advancingobsessive–compulsivedisorder pages 1-2) | Reduced face validity for complex human psychopathology, especially intrusive thoughts and higher-order cognition (huang2025advancingobsessive–compulsivedisorder pages 1-2) |
| Pharmacological / environmental models | Not specified in the available OCD contexts | Not specified | Not specified | Typically used in the field for repetitive behavior provocation, but no specific OCD pharmacological model was detailed in the available contexts | Not specified in available contexts | Can complement genetic models when available | Not enough source detail in the available contexts to summarize specific models responsibly (huang2025advancingobsessive–compulsivedisorder pages 1-2) |


*Table: This table summarizes major animal models used in obsessive-compulsive disorder research, emphasizing transgenic mouse lines and zebrafish models mentioned in the available sources. It is useful for comparing each model’s phenotypes, implicated circuits, translational uses, and major limitations.*

---

## Summary

Obsessive-Compulsive Disorder is a common, chronic neuropsychiatric disorder affecting 1-3% of the population with onset typically in childhood, adolescence, or young adulthood. The condition demonstrates substantial heritability (27-47% in adults, 45-65% in children) with highly polygenic architecture involving thousands of genetic variants. The largest GWAS identified 30 genome-wide significant loci and prioritized key genes including WDR6, DALRD3, and CTNND1.

OCD pathophysiology centers on dysfunction in cortico-striato-thalamo-cortical (CSTC) circuits involving orbitofrontal cortex, anterior cingulate cortex, striatum, and thalamus, with dysregulation of serotonergic, dopaminergic, and glutamatergic neurotransmission. Genetic risk is enriched in excitatory neurons of hippocampus and cortex, and dopamine receptor-containing medium spiny neurons in striatum.

First-line treatments include cognitive behavioral therapy with exposure and response prevention (CBT-ERP) and selective serotonin reuptake inhibitors (SSRIs), though approximately 50% of patients show inadequate response to initial interventions. Novel treatments include neuromodulation (TMS, DBS) for refractory cases. Staged-care models aim to match treatment intensity to clinical severity and prior response.

OCD causes substantial functional impairment and disability, with only 19.8% of affected individuals receiving treatment in the past year globally. Early identification and intervention are critical, particularly in pediatric-onset cases which demonstrate higher genetic loading and potentially worse prognosis without adequate treatment.


References

1. (jalal2023obsessive‐compulsivedisorderetiology pages 1-2): Baland Jalal, Samuel R. Chamberlain, and Barbara J. Sahakian. Obsessive‐compulsive disorder: etiology, neuropathology, and cognitive dysfunction. Brain and Behavior, May 2023. URL: https://doi.org/10.1002/brb3.3000, doi:10.1002/brb3.3000. This article has 162 citations and is from a peer-reviewed journal.

2. (roh2023clinicaladvancesin pages 1-2): Daeyoung Roh, Ki Won Jang, and Chan-Hyung Kim. Clinical advances in treatment strategies for obsessive-compulsive disorder in adults. Clinical Psychopharmacology and Neuroscience, 21:676-685, Jul 2023. URL: https://doi.org/10.9758/cpn.23.1075, doi:10.9758/cpn.23.1075. This article has 29 citations.

3. (stein2025obsessivecompulsivedisorderin pages 1-2): Dan J. Stein, Ayelet Meron Ruscio, Yasmin Altwaijri, Wai Tat Chiu, Nancy A. Sampson, Sergio Aguilar-Gaxiola, Ali Al-Hamzawi, Jordi Alonso, Stephanie Chardoul, Oye Gureje, Chiyi Hu, Elie G. Karam, John J. McGrath, Fernando Navarro-Mateu, Kate M. Scott, Juan Carlos Stagnaro, Yolanda Torres, Cristian Vladescu, Jacek Wciórka, Miguel Xavier, Ronald C. Kessler, Yasmin A. Altwaijri, Laura Helena Andrade, Lukoye Atwoli, Corina Benjet, Guilherme Borges, Ronny Bruffaerts, Brendan Bunting, Jose Miguel Caldas-de-Almeida, Graça Cardoso, Louisa Degenhardt, Giovanni de Girolamo, Josep Maria Haro, Meredith G. Harris, Hristo Hinkov, Chiyi Hu, Peter de Jonge, Aimee Nasser Karam, Georges Karam, Alan E. Kazdin, Norito Kawakami, Andrzej Kiejna, Viviane Kovess-Masfety, Maria Elena Medina-Mora, Jacek Moskalewicz, Daisuke Nishi, Marina Piazza, José Posada-Villa, Annelieke Roest, Margreet ten Have, Nathan Tintle, Maria Carmen Viana, Daniel V. Vigo, David R. Williams, Bogdan Wojtyniak, and Alan M. Zaslavsky. Obsessive-compulsive disorder in the world mental health surveys. BMC Medicine, Jul 2025. URL: https://doi.org/10.1186/s12916-025-04209-5, doi:10.1186/s12916-025-04209-5. This article has 41 citations and is from a domain leading peer-reviewed journal.

4. (strom2025genomewideanalysesidentify pages 1-2): Nora I. Strom, Zachary F. Gerring, Marco Galimberti, Dongmei Yu, Matthew W. Halvorsen, Abdel Abdellaoui, Cristina Rodriguez-Fontenla, Julia M. Sealock, Tim Bigdeli, Jonathan R. Coleman, Behrang Mahjani, Jackson G. Thorp, Katharina Bey, Christie L. Burton, Jurjen J. Luykx, Gwyneth Zai, Silvia Alemany, Christine Andre, Kathleen D. Askland, Julia Bäckman, Nerisa Banaj, Cristina Barlassina, Judith Becker Nissen, O. Joseph Bienvenu, Donald Black, Michael H. Bloch, Sigrid Børte, Rosa Bosch, Michael Breen, Brian P. Brennan, Helena Brentani, Joseph D. Buxbaum, Jonas Bybjerg-Grauholm, Enda M. Byrne, Judit Cabana-Dominguez, Beatriz Camarena, Adrian Camarena, Carolina Cappi, Angel Carracedo, Miguel Casas, Maria Cristina Cavallini, Valentina Ciullo, Edwin H. Cook, Jesse Crosby, Bernadette A. Cullen, Elles J. De Schipper, Richard Delorme, Srdjan Djurovic, Jason A. Elias, Xavier Estivill, Martha J. Falkenstein, Bengt T. Fundin, Lauryn Garner, Christina Gironda, Fernando S. Goes, Marco A. Grados, Jakob Grove, Wei Guo, Jan Haavik, Kristen Hagen, Kelly Harrington, Alexandra Havdahl, Kira D. Höffler, Ana G. Hounie, Donald Hucks, Christina Hultman, Magdalena Janecka, Eric Jenike, Elinor K. Karlsson, Kara Kelley, Julia Klawohn, Janice E. Krasnow, Kristi Krebs, Christoph Lange, Nuria Lanzagorta, Daniel Levey, Kerstin Lindblad-Toh, Fabio Macciardi, Brion Maher, Brittany Mathes, Evonne McArthur, Nathaniel McGregor, Nicole C. McLaughlin, Sandra Meier, Euripedes C. Miguel, Maureen Mulhern, Paul S. Nestadt, Erika L. Nurmi, Kevin S. O’Connell, Lisa Osiecki, Olga Therese Ousdal, Teemu Palviainen, Nancy L. Pedersen, Fabrizio Piras, Federica Piras, Sriramya Potluri, Raquel Rabionet, Alfredo Ramirez, Scott Rauch, Abraham Reichenberg, Mark A. Riddle, Stephan Ripke, Maria C. Rosário, Aline S. Sampaio, Miriam A. Schiele, Anne Heidi Skogholt, Laura G. Sloofman, Jan Smit, María Soler Artigas, Laurent F. Thomas, Eric Tifft, Homero Vallada, Nathanial van Kirk, Jeremy Veenstra-VanderWeele, Nienke N. Vulink, Christopher P. Walker, Ying Wang, Jens R. Wendland, Bendik S. Winsvold, Yin Yao, Hang Zhou, Andres Metspalu, Tõnu Esko, Reedik Mägi, Mari Nelis, Georgi Hudjashov, Chris German, Arpana Agrawal, Pino Alonso, Götz Berberich, Kathleen K. Bucholz, Cynthia M. Bulik, Danielle Cath, Damiaan Denys, Valsamma Eapen, Howard Edenberg, Peter Falkai, Thomas V. Fernandez, Abby J. Fyer, J. M. Gaziano, Dan A. Geller, Hans J. Grabe, Benjamin D. Greenberg, Gregory L. Hanna, Ian B. Hickie, David M. Hougaard, Norbert Kathmann, James Kennedy, Dongbing Lai, Mikael Landén, Stéphanie Le Hellard, Marion Leboyer, Christine Lochner, James T. McCracken, Sarah E. Medland, Preben B. Mortensen, Benjamin M. Neale, Humberto Nicolini, Merete Nordentoft, Michele Pato, Carlos Pato, David L. Pauls, John Piacentini, Christopher Pittenger, Danielle Posthuma, Josep Antoni Ramos-Quiroga, Steven A. Rasmussen, Margaret A. Richter, David R. Rosenberg, Stephan Ruhrmann, Jack F. Samuels, Sven Sandin, Paul Sandor, Gianfranco Spalletta, Dan J. Stein, S. Evelyn Stewart, Eric A. Storch, Barbara E. Stranger, Maurizio Turiel, Thomas Werge, Ole A. Andreassen, Anders D. Børglum, Susanne Walitza, Kristian Hveem, Bjarne K. Hansen, Christian Rück, Nicholas G. Martin, Lili Milani, Ole Mors, Ted Reichborn-Kjennerud, Marta Ribasés, Gerd Kvale, David Mataix-Cols, Katharina Domschke, Edna Grünblatt, Michael Wagner, John-Anker Zwart, Gerome Breen, Gerald Nestadt, Jaakko Kaprio, Paul D. Arnold, Dorothy E. Grice, James A. Knowles, Helga Ask, Karin J. Verweij, Lea K. Davis, Dirk J. Smit, James J. Crowley, Jeremiah M. Scharf, Murray B. Stein, Joel Gelernter, Carol A. Mathews, Eske M. Derks, and Manuel Mattheisen. Genome-wide analyses identify 30 loci associated with obsessive–compulsive disorder. Nature Genetics, 57:1389-1401, May 2025. URL: https://doi.org/10.1038/s41588-025-02189-z, doi:10.1038/s41588-025-02189-z. This article has 70 citations and is from a highest quality peer-reviewed journal.

5. (jalal2023obsessive‐compulsivedisorderetiology pages 2-3): Baland Jalal, Samuel R. Chamberlain, and Barbara J. Sahakian. Obsessive‐compulsive disorder: etiology, neuropathology, and cognitive dysfunction. Brain and Behavior, May 2023. URL: https://doi.org/10.1002/brb3.3000, doi:10.1002/brb3.3000. This article has 162 citations and is from a peer-reviewed journal.

6. (dhiman2025hereditarypatternsand pages 1-1): Abhinay Dhiman, Sidharth Mehan, Zuber Khan, Aarti Tiwari, Ghanshyam Das Gupta, and Acharan Singh Narula. Hereditary patterns and genetic associations in obsessive-compulsive disorder (ocd): neuropsychiatric insights, genetic influences, and treatment perspectives. Mar 2025. URL: https://doi.org/10.2174/0115665232316708240828063527, doi:10.2174/0115665232316708240828063527. This article has 8 citations and is from a peer-reviewed journal.

7. (liu2023earlyidentificationand pages 1-2): Xingyu Liu and Qing Fan. Early identification and intervention in pediatric obsessive-compulsive disorder. Brain Sciences, 13:399, Feb 2023. URL: https://doi.org/10.3390/brainsci13030399, doi:10.3390/brainsci13030399. This article has 25 citations.

8. (strom2025genomewideanalysesidentify pages 2-3): Nora I. Strom, Zachary F. Gerring, Marco Galimberti, Dongmei Yu, Matthew W. Halvorsen, Abdel Abdellaoui, Cristina Rodriguez-Fontenla, Julia M. Sealock, Tim Bigdeli, Jonathan R. Coleman, Behrang Mahjani, Jackson G. Thorp, Katharina Bey, Christie L. Burton, Jurjen J. Luykx, Gwyneth Zai, Silvia Alemany, Christine Andre, Kathleen D. Askland, Julia Bäckman, Nerisa Banaj, Cristina Barlassina, Judith Becker Nissen, O. Joseph Bienvenu, Donald Black, Michael H. Bloch, Sigrid Børte, Rosa Bosch, Michael Breen, Brian P. Brennan, Helena Brentani, Joseph D. Buxbaum, Jonas Bybjerg-Grauholm, Enda M. Byrne, Judit Cabana-Dominguez, Beatriz Camarena, Adrian Camarena, Carolina Cappi, Angel Carracedo, Miguel Casas, Maria Cristina Cavallini, Valentina Ciullo, Edwin H. Cook, Jesse Crosby, Bernadette A. Cullen, Elles J. De Schipper, Richard Delorme, Srdjan Djurovic, Jason A. Elias, Xavier Estivill, Martha J. Falkenstein, Bengt T. Fundin, Lauryn Garner, Christina Gironda, Fernando S. Goes, Marco A. Grados, Jakob Grove, Wei Guo, Jan Haavik, Kristen Hagen, Kelly Harrington, Alexandra Havdahl, Kira D. Höffler, Ana G. Hounie, Donald Hucks, Christina Hultman, Magdalena Janecka, Eric Jenike, Elinor K. Karlsson, Kara Kelley, Julia Klawohn, Janice E. Krasnow, Kristi Krebs, Christoph Lange, Nuria Lanzagorta, Daniel Levey, Kerstin Lindblad-Toh, Fabio Macciardi, Brion Maher, Brittany Mathes, Evonne McArthur, Nathaniel McGregor, Nicole C. McLaughlin, Sandra Meier, Euripedes C. Miguel, Maureen Mulhern, Paul S. Nestadt, Erika L. Nurmi, Kevin S. O’Connell, Lisa Osiecki, Olga Therese Ousdal, Teemu Palviainen, Nancy L. Pedersen, Fabrizio Piras, Federica Piras, Sriramya Potluri, Raquel Rabionet, Alfredo Ramirez, Scott Rauch, Abraham Reichenberg, Mark A. Riddle, Stephan Ripke, Maria C. Rosário, Aline S. Sampaio, Miriam A. Schiele, Anne Heidi Skogholt, Laura G. Sloofman, Jan Smit, María Soler Artigas, Laurent F. Thomas, Eric Tifft, Homero Vallada, Nathanial van Kirk, Jeremy Veenstra-VanderWeele, Nienke N. Vulink, Christopher P. Walker, Ying Wang, Jens R. Wendland, Bendik S. Winsvold, Yin Yao, Hang Zhou, Andres Metspalu, Tõnu Esko, Reedik Mägi, Mari Nelis, Georgi Hudjashov, Chris German, Arpana Agrawal, Pino Alonso, Götz Berberich, Kathleen K. Bucholz, Cynthia M. Bulik, Danielle Cath, Damiaan Denys, Valsamma Eapen, Howard Edenberg, Peter Falkai, Thomas V. Fernandez, Abby J. Fyer, J. M. Gaziano, Dan A. Geller, Hans J. Grabe, Benjamin D. Greenberg, Gregory L. Hanna, Ian B. Hickie, David M. Hougaard, Norbert Kathmann, James Kennedy, Dongbing Lai, Mikael Landén, Stéphanie Le Hellard, Marion Leboyer, Christine Lochner, James T. McCracken, Sarah E. Medland, Preben B. Mortensen, Benjamin M. Neale, Humberto Nicolini, Merete Nordentoft, Michele Pato, Carlos Pato, David L. Pauls, John Piacentini, Christopher Pittenger, Danielle Posthuma, Josep Antoni Ramos-Quiroga, Steven A. Rasmussen, Margaret A. Richter, David R. Rosenberg, Stephan Ruhrmann, Jack F. Samuels, Sven Sandin, Paul Sandor, Gianfranco Spalletta, Dan J. Stein, S. Evelyn Stewart, Eric A. Storch, Barbara E. Stranger, Maurizio Turiel, Thomas Werge, Ole A. Andreassen, Anders D. Børglum, Susanne Walitza, Kristian Hveem, Bjarne K. Hansen, Christian Rück, Nicholas G. Martin, Lili Milani, Ole Mors, Ted Reichborn-Kjennerud, Marta Ribasés, Gerd Kvale, David Mataix-Cols, Katharina Domschke, Edna Grünblatt, Michael Wagner, John-Anker Zwart, Gerome Breen, Gerald Nestadt, Jaakko Kaprio, Paul D. Arnold, Dorothy E. Grice, James A. Knowles, Helga Ask, Karin J. Verweij, Lea K. Davis, Dirk J. Smit, James J. Crowley, Jeremiah M. Scharf, Murray B. Stein, Joel Gelernter, Carol A. Mathews, Eske M. Derks, and Manuel Mattheisen. Genome-wide analyses identify 30 loci associated with obsessive–compulsive disorder. Nature Genetics, 57:1389-1401, May 2025. URL: https://doi.org/10.1038/s41588-025-02189-z, doi:10.1038/s41588-025-02189-z. This article has 70 citations and is from a highest quality peer-reviewed journal.

9. (strom2025genomewideanalysesidentify pages 3-4): Nora I. Strom, Zachary F. Gerring, Marco Galimberti, Dongmei Yu, Matthew W. Halvorsen, Abdel Abdellaoui, Cristina Rodriguez-Fontenla, Julia M. Sealock, Tim Bigdeli, Jonathan R. Coleman, Behrang Mahjani, Jackson G. Thorp, Katharina Bey, Christie L. Burton, Jurjen J. Luykx, Gwyneth Zai, Silvia Alemany, Christine Andre, Kathleen D. Askland, Julia Bäckman, Nerisa Banaj, Cristina Barlassina, Judith Becker Nissen, O. Joseph Bienvenu, Donald Black, Michael H. Bloch, Sigrid Børte, Rosa Bosch, Michael Breen, Brian P. Brennan, Helena Brentani, Joseph D. Buxbaum, Jonas Bybjerg-Grauholm, Enda M. Byrne, Judit Cabana-Dominguez, Beatriz Camarena, Adrian Camarena, Carolina Cappi, Angel Carracedo, Miguel Casas, Maria Cristina Cavallini, Valentina Ciullo, Edwin H. Cook, Jesse Crosby, Bernadette A. Cullen, Elles J. De Schipper, Richard Delorme, Srdjan Djurovic, Jason A. Elias, Xavier Estivill, Martha J. Falkenstein, Bengt T. Fundin, Lauryn Garner, Christina Gironda, Fernando S. Goes, Marco A. Grados, Jakob Grove, Wei Guo, Jan Haavik, Kristen Hagen, Kelly Harrington, Alexandra Havdahl, Kira D. Höffler, Ana G. Hounie, Donald Hucks, Christina Hultman, Magdalena Janecka, Eric Jenike, Elinor K. Karlsson, Kara Kelley, Julia Klawohn, Janice E. Krasnow, Kristi Krebs, Christoph Lange, Nuria Lanzagorta, Daniel Levey, Kerstin Lindblad-Toh, Fabio Macciardi, Brion Maher, Brittany Mathes, Evonne McArthur, Nathaniel McGregor, Nicole C. McLaughlin, Sandra Meier, Euripedes C. Miguel, Maureen Mulhern, Paul S. Nestadt, Erika L. Nurmi, Kevin S. O’Connell, Lisa Osiecki, Olga Therese Ousdal, Teemu Palviainen, Nancy L. Pedersen, Fabrizio Piras, Federica Piras, Sriramya Potluri, Raquel Rabionet, Alfredo Ramirez, Scott Rauch, Abraham Reichenberg, Mark A. Riddle, Stephan Ripke, Maria C. Rosário, Aline S. Sampaio, Miriam A. Schiele, Anne Heidi Skogholt, Laura G. Sloofman, Jan Smit, María Soler Artigas, Laurent F. Thomas, Eric Tifft, Homero Vallada, Nathanial van Kirk, Jeremy Veenstra-VanderWeele, Nienke N. Vulink, Christopher P. Walker, Ying Wang, Jens R. Wendland, Bendik S. Winsvold, Yin Yao, Hang Zhou, Andres Metspalu, Tõnu Esko, Reedik Mägi, Mari Nelis, Georgi Hudjashov, Chris German, Arpana Agrawal, Pino Alonso, Götz Berberich, Kathleen K. Bucholz, Cynthia M. Bulik, Danielle Cath, Damiaan Denys, Valsamma Eapen, Howard Edenberg, Peter Falkai, Thomas V. Fernandez, Abby J. Fyer, J. M. Gaziano, Dan A. Geller, Hans J. Grabe, Benjamin D. Greenberg, Gregory L. Hanna, Ian B. Hickie, David M. Hougaard, Norbert Kathmann, James Kennedy, Dongbing Lai, Mikael Landén, Stéphanie Le Hellard, Marion Leboyer, Christine Lochner, James T. McCracken, Sarah E. Medland, Preben B. Mortensen, Benjamin M. Neale, Humberto Nicolini, Merete Nordentoft, Michele Pato, Carlos Pato, David L. Pauls, John Piacentini, Christopher Pittenger, Danielle Posthuma, Josep Antoni Ramos-Quiroga, Steven A. Rasmussen, Margaret A. Richter, David R. Rosenberg, Stephan Ruhrmann, Jack F. Samuels, Sven Sandin, Paul Sandor, Gianfranco Spalletta, Dan J. Stein, S. Evelyn Stewart, Eric A. Storch, Barbara E. Stranger, Maurizio Turiel, Thomas Werge, Ole A. Andreassen, Anders D. Børglum, Susanne Walitza, Kristian Hveem, Bjarne K. Hansen, Christian Rück, Nicholas G. Martin, Lili Milani, Ole Mors, Ted Reichborn-Kjennerud, Marta Ribasés, Gerd Kvale, David Mataix-Cols, Katharina Domschke, Edna Grünblatt, Michael Wagner, John-Anker Zwart, Gerome Breen, Gerald Nestadt, Jaakko Kaprio, Paul D. Arnold, Dorothy E. Grice, James A. Knowles, Helga Ask, Karin J. Verweij, Lea K. Davis, Dirk J. Smit, James J. Crowley, Jeremiah M. Scharf, Murray B. Stein, Joel Gelernter, Carol A. Mathews, Eske M. Derks, and Manuel Mattheisen. Genome-wide analyses identify 30 loci associated with obsessive–compulsive disorder. Nature Genetics, 57:1389-1401, May 2025. URL: https://doi.org/10.1038/s41588-025-02189-z, doi:10.1038/s41588-025-02189-z. This article has 70 citations and is from a highest quality peer-reviewed journal.

10. (farrell2023closingthegap pages 1-2): Lara J. Farrell, Allison M. Waters, Eric A. Storch, Gabrielle Simcock, Iain E. Perkes, Jessica R. Grisham, Katelyn M. Dyason, and Thomas H. Ollendick. Closing the gap for children with ocd: a staged-care model of cognitive behavioural therapy with exposure and response prevention. Clinical Child and Family Psychology Review, 26:642-664, Jul 2023. URL: https://doi.org/10.1007/s10567-023-00439-2, doi:10.1007/s10567-023-00439-2. This article has 32 citations and is from a domain leading peer-reviewed journal.

11. (huang2025advancingobsessive–compulsivedisorder pages 1-2): Xinyuejia Huang, Linglong Xiao, Mengqi Wang, Yang Wu, Hao Deng, and Wei Wang. Advancing obsessive–compulsive disorder research: insights from transgenic animal models and innovative therapies. Brain Sciences, 15:43, Jan 2025. URL: https://doi.org/10.3390/brainsci15010043, doi:10.3390/brainsci15010043. This article has 1 citations.

## Artifacts

- [Edison artifact artifact-00](Obsessive-Compulsive_Disorder-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Obsessive-Compulsive_Disorder-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](Obsessive-Compulsive_Disorder-deep-research-falcon_artifacts/artifact-02.md)