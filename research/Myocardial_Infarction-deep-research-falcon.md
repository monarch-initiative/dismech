---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-05T18:50:31.446039'
end_time: '2026-07-05T19:07:07.576584'
duration_seconds: 996.13
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Myocardial Infarction
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 54
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: Myocardial_Infarction-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Myocardial_Infarction-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: Myocardial_Infarction-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Myocardial Infarction
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Myocardial Infarction** covering all of the
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
- **Disease Name:** Myocardial Infarction
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Myocardial Infarction** covering all of the
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


# Comprehensive Research Report: Myocardial Infarction

## 1. Disease Information

### Overview
Myocardial infarction (MI) is defined as cardiomyocyte necrosis in a clinical setting consistent with acute myocardial ischemia, identified through clinical symptoms (prolonged chest pain), biochemical markers (elevated cardiac troponin), and instrumental findings (ECG changes and/or regional wall motion abnormalities) (fede2025myocardialischemiareperfusioninjury pages 1-2). MI is the leading component of cardiovascular disease (CVD) contributing to mortality, with approximately 4 million CVD-related deaths annually in Europe alone (młynarska2024fromatheroscleroticplaque pages 17-19). MI is classified into five types: Type 1 (atherosclerosis-related, most common), Type 2 (oxygen supply-demand mismatch), Type 3 (sudden cardiac death), Type 4 (PCI-related), and Type 5 (CABG-related) (młynarska2024fromatheroscleroticplaque pages 17-19).

### Key Identifiers
- **MONDO ID:** MONDO:0005068 (myocardial infarction); MONDO:0004781 (acute myocardial infarction) (OpenTargets Search: myocardial infarction)
- **ICD-10:** I21 (Acute myocardial infarction); I22 (Subsequent myocardial infarction)
- **ICD-11:** BA41 (Acute myocardial infarction)
- **MeSH:** D009203

### Common Synonyms
Heart attack, acute myocardial infarction (AMI), STEMI (ST-elevation myocardial infarction), NSTEMI (non-ST-elevation myocardial infarction), coronary thrombosis, acute coronary syndrome (broader term)

---

## 2. Etiology

### Disease Causal Factors
Type 1 MI results from atherosclerotic plaque destabilization—either rupture or erosion—in coronary arteries, leading to thrombus formation that interrupts myocardial blood flow (das2025networkpharmacologyapproaches pages 1-2, młynarska2024fromatheroscleroticplaque pages 17-19). The pathogenesis involves chronic inflammation, lipid accumulation, endothelial dysfunction, and ultimately acute coronary artery occlusion.

### Risk Factors

**Genetic Risk Factors:**
GWAS analyses have identified numerous susceptibility loci for MI. Meta-analyses combining Saudi Arabian cohorts with the CardioGRAMplusC4D and UK BioBank GWAS revealed 66 loci with genome-wide significance (p < 5 × 10⁻⁸). Key genes implicated include *PCSK9*, *CETP*, *CDKN2B-AS1* (involved in lipid metabolism, inflammation, and endothelial function), *STOX1*, *VPS26A*, and *LDLR* (zhou2024associationofmetabolic pages 1-2, zhou2024associationofmetabolic pages 10-13). Polygenic risk scores (PRS) demonstrate that a high genetic risk is associated with a threefold increase in MI risk (OR: 3.074, 95% CI: 2.354–4.014) (zhou2024associationofmetabolic pages 1-2). Elevated lipoprotein(a) levels are independently associated with an increased risk of coronary artery disease, with risk increasing threefold in young patients (zhou2024associationofmetabolic pages 13-15).

**Environmental and Lifestyle Risk Factors:**
Traditional risk factors include hypercholesterolemia (high LDL-C), cigarette smoking, chronic kidney disease, diabetes mellitus, hypertension, obesity, sedentary lifestyle, and poor dietary habits (młynarska2024fromatheroscleroticplaque pages 17-19, zhou2024associationofmetabolic pages 13-15). Air pollution, even below regulatory thresholds, promotes atherosclerosis, vascular dysfunction, and cardiac events.

### Protective Factors
Moderate fat intake (>15 energy percent), moderate alcohol consumption (<30 g/day), and non-smoking reduce MI risk even in individuals with high genetic predisposition (zhou2024associationofmetabolic pages 1-2, zhou2024associationofmetabolic pages 13-15). MI risk is negatively correlated with the consumption of olive oil, sesame oil, and perilla oil (rg = −0.364), which have anti-inflammatory and vasodilatory effects (zhou2024associationofmetabolic pages 13-15).

### Gene-Environment Interactions
PRS interacts significantly with dietary fat intake, alcohol consumption, and smoking status to modulate MI risk, demonstrating that healthy lifestyle habits can substantially mitigate genetic susceptibility (zhou2024associationofmetabolic pages 1-2, zhou2024associationofmetabolic pages 13-15).

**Suggested HPO terms for risk factors:** HP:0003119 (Abnormality of lipid metabolism); HP:0000822 (Hypertension); HP:0001513 (Obesity); HP:0005978 (Type II diabetes mellitus)

---

## 3. Phenotypes

### Symptoms and Clinical Signs
- **Chest pain (angina pectoris):** Prolonged substernal chest pressure or pain, the hallmark symptom; HP:0001681 (Angina pectoris)
- **Dyspnea:** Shortness of breath; HP:0002094
- **Diaphoresis:** Profuse sweating
- **Nausea/vomiting**
- **Radiating pain:** To left arm, jaw, or back
- **Syncope or presyncope:** HP:0001279
- **Cardiogenic shock:** Complicates up to 10% of AMI cases, particularly in STEMI

**Atypical presentations:** Over one-third of NSTE-ACS patients may present with normal ECG findings (młynarska2024fromatheroscleroticplaque pages 7-8). Older patients often exhibit atypical symptoms with diminished sensitivity of traditional symptoms with age.

### Laboratory Abnormalities
- **Elevated cardiac troponins (cTnI and cTnT):** The most effective biomarkers for AMI diagnosis (das2025networkpharmacologyapproaches pages 12-13)
- **Elevated CK-MB, LDH** (rises 24–48 hours post-injury) (das2025networkpharmacologyapproaches pages 12-13)
- **Elevated CRP, interleukins, TNF-α**
- **ECG changes:** ST-segment elevation, ST depression, T-wave abnormalities; LOINC codes applicable

### Quality of Life Impact
Post-MI patients experience significant reductions in quality of life, with long-term impacts on functional capacity, psychological well-being (anxiety, depression), and return-to-work rates, particularly in younger patients.

---

## 4. Genetic/Molecular Information

### Key Susceptibility Genes and Targets
OpenTargets analysis identifies the following high-priority targets for MI (MONDO:0005068) (OpenTargets Search: myocardial infarction):

| Target Gene Symbol | Full Target Name | Target Category | Association Score | Drug Class/Examples | Clinical Stage | Evidence |
|---|---|---|---:|---|---|---|
| GUCY1A1 | Guanylate cyclase 1 soluble subunit alpha 1 | Enzyme / nitric oxide receptor subunit | 0.695 | Soluble guanylate cyclase stimulators/activators; nitrates act upstream via NO-sGC-cGMP signaling | Approved-linked evidence in OpenTargets | (OpenTargets Search: myocardial infarction) |
| LDLR | Low density lipoprotein receptor | Receptor | 0.689 | LDL-lowering strategies acting through LDLR pathway: statins, PCSK9 inhibitors, inclisiran | Literature + clinical/approved-linked evidence | (OpenTargets Search: myocardial infarction, ramosregalado2024theinfluenceof pages 10-11) |
| PCSK9 | Proprotein convertase subtilisin/kexin type 9 | Secreted protease | 0.670 | PCSK9 inhibitors: evolocumab, alirocumab; siRNA inclisiran | Approved | (OpenTargets Search: myocardial infarction, ramosregalado2024theinfluenceof pages 10-11) |
| ADRB1 | Adrenoceptor beta 1 | G protein-coupled receptor | 0.624 | Beta-blockers: metoprolol, bisoprolol, atenolol | Approved | (OpenTargets Search: myocardial infarction, młynarska2024fromatheroscleroticplaque pages 11-12) |
| P2RY12 | Purinergic receptor P2Y12 | G protein-coupled receptor | 0.620 | P2Y12 inhibitors: clopidogrel, prasugrel, ticagrelor, cangrelor | Approved / Phase 4 evidence | (OpenTargets Search: myocardial infarction, młynarska2024fromatheroscleroticplaque pages 11-12, nicolau2025molecularmechanismsof pages 8-10) |
| AGTR1 | Angiotensin II receptor type 1 | G protein-coupled receptor | 0.617 | ARBs: losartan, valsartan, candesartan | Approved | (OpenTargets Search: myocardial infarction, ramosregalado2024theinfluenceof pages 10-11) |
| HMGCR | 3-hydroxy-3-methylglutaryl-CoA reductase | Enzyme | 0.616 | Statins: atorvastatin, rosuvastatin, simvastatin | Approved | (OpenTargets Search: myocardial infarction, alradwan2024emergingtrendsand pages 4-7, ramosregalado2024theinfluenceof pages 10-11) |
| ACE | Angiotensin I converting enzyme | Enzyme | 0.612 | ACE inhibitors: ramipril, lisinopril, enalapril | Approved | (OpenTargets Search: myocardial infarction, ramosregalado2024theinfluenceof pages 10-11) |
| PLAT | Plasminogen activator, tissue type | Serine protease | 0.566* | Thrombolytics/fibrinolytics: alteplase, tenecteplase | Approved | (OpenTargets Search: myocardial infarction, occhipinti2025pharmacologicalandinterventional pages 6-8) |
| LPA | Lipoprotein(a) | Lipoprotein / secreted risk factor | 0.435* | Emerging Lp(a)-lowering agents: olpasiran, pelacarsen; indirect lowering with PCSK9 inhibitors | Clinical development / emerging | (OpenTargets Search: myocardial infarction) |
| APOE | Apolipoprotein E | Lipid transport protein | 0.428* | No direct MI-targeted approved therapy; informs lipid biology/risk stratification | Literature-associated | (OpenTargets Search: myocardial infarction) |
| PTGS2 | Prostaglandin-endoperoxide synthase 2 (COX-2) | Enzyme | 0.606 | NSAID/COX pathway modulators; aspirin acts primarily on PTGS1 rather than PTGS2 | Approved-linked / Phase 4 evidence | (OpenTargets Search: myocardial infarction) |
| TCF21 | Transcription factor 21 | Transcription factor | 0.373* | No approved direct therapy; biomarker/mechanistic target in vascular remodeling | Literature-associated | (OpenTargets Search: myocardial infarction) |
| SORT1 | Sortilin 1 | Sorting receptor | 0.365* | No approved direct MI therapy; implicated in lipoprotein trafficking and residual risk biology | Literature-associated | (OpenTargets Search: myocardial infarction) |
| ITGA2B | Integrin subunit alpha 2b | Platelet integrin receptor subunit | 0.360* | GPIIb/IIIa inhibitors: abciximab, eptifibatide, tirofiban | Approved / Phase 3 evidence | (OpenTargets Search: myocardial infarction, sagris2024myocardialischemia–reperfusioninjury pages 8-10, occhipinti2025pharmacologicalandinterventional pages 6-8) |
| ITGB3 | Integrin subunit beta 3 | Platelet integrin receptor subunit | 0.360* | GPIIb/IIIa inhibitors: abciximab, eptifibatide, tirofiban | Approved / Phase 3 evidence | (OpenTargets Search: myocardial infarction, sagris2024myocardialischemia–reperfusioninjury pages 8-10, occhipinti2025pharmacologicalandinterventional pages 6-8) |


*Table: This table summarizes key myocardial infarction drug targets prioritized from OpenTargets together with clinically relevant drug classes and development stage. It is useful for linking disease biology to established and emerging therapeutic mechanisms.*

### GWAS Findings
GWAS meta-analyses have identified over 66 loci associated with MI at genome-wide significance. The *SHISA5* locus (rs11707229) was notably enriched at >12% minor allele frequency in Saudi MI populations. Genes including *PCSK9*, *LDLR*, *APOE*, *LPA*, *TCF21*, and *SORT1* are consistently implicated (OpenTargets Search: myocardial infarction, zhou2024associationofmetabolic pages 10-13). Genetic variants rs3864814 and rs2081208 are associated with MI through colocalization analysis with genes *STOX1*, *VPS26A*, and *RP11-744D14.2* (zhou2024associationofmetabolic pages 10-13).

### Epigenetic Information
DNA methylation, histone modifications (particularly via HDAC inhibitors), and non-coding RNAs (miR-144, miR-22) are key regulators of gene expression associated with atherosclerosis, MI, and cardiac remodeling. HDAC inhibitors reduce cardiomyocyte apoptosis, while specific microRNAs modulate oxidative stress pathways during ischemia-reperfusion injury (das2025networkpharmacologyapproaches pages 9-10).

---

## 5. Environmental Information

### Environmental Factors
Air pollution promotes atherosclerosis, vascular dysfunction, and cardiac events even below current regulatory thresholds. Occupational exposures, noise pollution, and extreme temperatures are additional contributors.

### Lifestyle Factors
Smoking, sedentary lifestyle, high-fat and high-sugar diets, and excessive alcohol consumption are established modifiable risk factors (młynarska2024fromatheroscleroticplaque pages 17-19). Physical activity reduces cardiovascular risk through improved cardiac output, vascular efficiency, and metabolic health.

---

## 6. Mechanism / Pathophysiology

### Overview of Pathophysiological Cascade
The pathophysiology of MI begins with atherosclerotic plaque rupture or erosion, leading to thrombus formation and coronary artery occlusion. Prolonged ischemia causes irreversible cardiomyocyte death, beginning in the subendocardium and progressing as a necrotic wavefront toward the subepicardium (buja2023pathobiologyofmyocardial pages 2-4, buja2023pathobiologyofmyocardial pages 1-2). Reversible injury lasts approximately 15 minutes, with irreversible injury developing between 20–60 minutes after coronary occlusion (buja2023pathobiologyofmyocardial pages 2-4).

### Molecular Pathways
The following table summarizes the major signaling pathways involved:

| Pathway Name | Key Components/Mediators | Role in MI Pathophysiology | Cellular Process Affected | Therapeutic Implications |
|---|---|---|---|---|
| MAPK (p38, JNK, ERK1/2) | p38 MAPK, JNK, ERK1/2, ADAM17, ACE2, Bim | Activated during ischemia/reperfusion and post-MI remodeling; promotes inflammatory signaling, apoptosis, mitochondrial dysfunction, ferroptosis, and adverse remodeling/fibrosis. p38/JNK are generally injury-amplifying; ERK can be context-dependent with survival and remodeling effects. (wang2025theroleof pages 16-17, wang2025theroleof pages 4-6) | Apoptosis, mitochondrial fission, oxidative stress response, ferroptosis, remodeling | Experimental inhibition of p38/JNK/ERK-axis components can reduce myocardial injury; pathway is a candidate for cardioprotection and anti-remodeling therapies, though translation remains challenging. (wang2025theroleof pages 16-17, wang2025theroleof pages 4-6) |
| PI3K/AKT/mTOR | PI3K, AKT, mTOR, BAD, Mdm2, PKD1, GLUT4 | Core pro-survival pathway in MI and reperfusion injury; suppresses apoptosis, modulates autophagy, supports metabolic adaptation, and can limit inflammatory injury. Reduced signaling is associated with greater injury. (fede2025myocardialischemiareperfusioninjury pages 26-28, das2025networkpharmacologyapproaches pages 7-9, fede2025myocardialischemiareperfusioninjury pages 10-12) | Cell survival, glucose uptake, metabolism, autophagy control, anti-apoptotic signaling | Therapies that enhance PI3K/AKT signaling or fine-tune mTOR/autophagy may reduce infarct size and improve reperfusion outcomes; a major cardioprotective target in preclinical studies. (das2025networkpharmacologyapproaches pages 7-9, fede2025myocardialischemiareperfusioninjury pages 10-12) |
| NF-κB | NF-κB, TLR4, MyD88, IL-1β, TNF-α, IL-6, Beclin-1 | Central inflammatory transcriptional program activated by DAMPs and innate immune receptors after cardiomyocyte necrosis; drives cytokine/chemokine expression, leukocyte recruitment, and can suppress protective autophagy in some contexts. (fede2025myocardialischemiareperfusioninjury pages 26-28, das2025networkpharmacologyapproaches pages 7-9, fede2025myocardialischemiareperfusioninjury pages 10-12, hilgendorf2024repairofthe pages 3-4) | Inflammation, cytokine production, leukocyte recruitment, autophagy regulation | Anti-inflammatory strategies targeting upstream TLR4/MyD88/NF-κB signaling may attenuate reperfusion injury and maladaptive remodeling; promising but requires timing-specific modulation. (fede2025myocardialischemiareperfusioninjury pages 26-28, das2025networkpharmacologyapproaches pages 7-9) |
| Wnt/β-catenin | Canonical Wnt/β-catenin, non-canonical Wnt/PCP, Wnt/Ca2+, JNK, CaMKII, PKC, calcineurin | Wnt signaling shows pathway-specific effects in MI/I/R injury: canonical Wnt/β-catenin tends to support recovery and survival, whereas non-canonical Wnt signaling can worsen apoptosis, calcium overload, inflammation, fibrosis, and hypertrophy. (zhang2024ischemiareperfusioninjurymolecular pages 3-4) | Apoptosis, macrophage polarization, oxidative stress, ECM remodeling, angiogenesis, fibrosis | Selective activation of canonical Wnt or inhibition of damaging non-canonical Wnt branches is a potential precision strategy for limiting reperfusion injury and fibrosis. (zhang2024ischemiareperfusioninjurymolecular pages 3-4) |
| TGF-β/Smad | TGF-β, TGF-β receptors, Smad proteins, MMP-2, MMP-9 | Master profibrotic pathway after MI; activated during repair/remodeling and drives fibroblast activation, myofibroblast conversion, collagen synthesis, EndoMT, and scar formation. Essential for structural repair but excessive activation promotes pathological fibrosis. (yin2023postmyocardialinfarctionfibrosis pages 6-8, hilgendorf2024repairofthe pages 3-4) | Fibroblast activation, collagen deposition, scar formation, fibrosis, EndoMT | Targeted modulation may preserve necessary scar formation while reducing adverse remodeling; attractive for anti-fibrotic therapy after MI. (yin2023postmyocardialinfarctionfibrosis pages 6-8, hilgendorf2024repairofthe pages 3-4) |
| NLRP3 inflammasome | NLRP3, ASC, caspase-1, IL-1β, ROS, DAMPs | Activated in macrophages, fibroblasts, and injured myocardium after ischemia/reperfusion; links mitochondrial damage and oxidative stress to IL-1β release and inflammatory amplification, and contributes to pyroptotic cell death. (fede2025myocardialischemiareperfusioninjury pages 26-28, das2025networkpharmacologyapproaches pages 7-9, fede2025myocardialischemiareperfusioninjury pages 1-2, hilgendorf2024repairofthe pages 15-17) | Inflammasome activation, pyroptosis, sterile inflammation | NLRP3/caspase-1/IL-1 axis inhibitors are promising candidates to reduce infarct inflammation, reperfusion injury, and downstream remodeling. (sagris2024myocardialischemia–reperfusioninjury pages 8-10, fede2025myocardialischemiareperfusioninjury pages 26-28) |
| TLR4/MyD88 | TLR4, MyD88, DAMPs/alarmins, HMGB1, NF-κB | One of the earliest innate immune sensing systems after MI; recognizes DAMPs released from necrotic cardiomyocytes and triggers downstream inflammatory cascades, endothelial activation, and leukocyte recruitment. (fede2025myocardialischemiareperfusioninjury pages 26-28, hilgendorf2024repairofthe pages 3-4, hilgendorf2024repairofthe pages 1-3) | Innate immune activation, cytokine induction, leukocyte trafficking | TLR4/MyD88 blockade is a mechanistically strong anti-inflammatory strategy for limiting sterile injury and reperfusion damage, but may risk impairing necessary repair if over-suppressed. (fede2025myocardialischemiareperfusioninjury pages 26-28, hilgendorf2024repairofthe pages 3-4) |
| JAK-STAT | JAKs, STATs, IL-6, STAT3 | Implicated in vascular inflammation, smooth muscle cell proliferation/differentiation, and post-MI inflammatory signaling; also participates in reparative cytokine signaling such as IL-10/STAT3-mediated suppression of excessive inflammation. (młynarska2024fromatheroscleroticplaque pages 17-19, hilgendorf2024repairofthe pages 19-20) | Cytokine signaling, inflammation resolution, vascular remodeling, cell proliferation | JAK inhibition has been proposed as a strategy in atherosclerosis/MI biology, while preserving beneficial STAT3-mediated repair signaling may be important; pathway likely needs selective modulation. (młynarska2024fromatheroscleroticplaque pages 17-19, hilgendorf2024repairofthe pages 19-20) |
| Apoptosis | Fas, TNF receptors, cytochrome c, caspase-8, caspase-9, executioner caspases, BAX/BAK, Bcl-2 | Major programmed cell-death pathway in ischemia/reperfusion injury; initiated during ischemia and executed during reperfusion via intrinsic mitochondrial and extrinsic death-receptor mechanisms. (fede2025myocardialischemiareperfusioninjury pages 26-28, das2025networkpharmacologyapproaches pages 7-9, fede2025myocardialischemiareperfusioninjury pages 1-2) | Programmed cell death, cardiomyocyte loss | Anti-apoptotic therapies, mitochondrial stabilizers, and survival-pathway activators may reduce infarct expansion and preserve viable myocardium. (das2025networkpharmacologyapproaches pages 15-16, fede2025myocardialischemiareperfusioninjury pages 26-28) |
| Necroptosis | RIPK1, RIPK3, MLKL | Regulated necrotic death contributes to cardiomyocyte loss during reperfusion and overlaps with inflammatory amplification because cell lysis releases DAMPs. (fede2025myocardialischemiareperfusioninjury pages 10-12, fede2025myocardialischemiareperfusioninjury pages 1-2) | Regulated necrotic cell death, DAMP release | RIPK/MLKL-targeted inhibition is a potential cardioprotective approach in reperfusion injury. (fede2025myocardialischemiareperfusioninjury pages 10-12) |
| Pyroptosis | Caspase-1, caspase-4/5/11, GSDMD, NLRP3, ASC, calpains | Inflammatory cell death pathway activated by inflammasomes in MIRI; causes membrane pore formation, cytokine release, and propagation of sterile inflammation. (fede2025myocardialischemiareperfusioninjury pages 10-12, fede2025myocardialischemiareperfusioninjury pages 12-14, fede2025myocardialischemiareperfusioninjury pages 1-2) | Inflammatory programmed cell death, cytokine release | Caspase-1, GSDMD, or inflammasome inhibition may reduce inflammatory tissue damage and infarct progression. (sagris2024myocardialischemia–reperfusioninjury pages 8-10, fede2025myocardialischemiareperfusioninjury pages 12-14) |
| Ferroptosis | Iron-dependent lipid peroxidation machinery, ROS, MAPK/ERK-associated regulators | Emerging reperfusion-related death mechanism characterized by iron-dependent lipid peroxidation; contributes to myocardial injury and interacts with oxidative stress/MAPK signaling. (wang2025theroleof pages 16-17, wang2025theroleof pages 4-6, das2025networkpharmacologyapproaches pages 4-6) | Lipid peroxidation-driven cell death, oxidative membrane damage | Ferroptosis inhibitors and antioxidant/lipid-peroxidation-targeting strategies are under investigation as adjunct cardioprotective therapies. (wang2025theroleof pages 16-17, das2025networkpharmacologyapproaches pages 4-6) |
| Autophagy | Beclin-1, mTOR, LAMP2, ATF6, IRE1, PERK, ROS | Context-dependent in MI: basal or adaptive autophagy can be protective, but dysregulated or excessive autophagy during reperfusion may worsen injury. Controlled by PI3K/AKT/mTOR, TLR4/NF-κB, ER stress, and ROS signaling. (das2025networkpharmacologyapproaches pages 7-9, fede2025myocardialischemiareperfusioninjury pages 10-12, fede2025myocardialischemiareperfusioninjury pages 12-14) | Organelle quality control, stress adaptation, cell survival vs cell death balance | Therapies that restore balanced autophagic flux rather than simple inhibition/activation may improve myocardial salvage and remodeling. (das2025networkpharmacologyapproaches pages 7-9, fede2025myocardialischemiareperfusioninjury pages 10-12) |


*Table: This table summarizes the major molecular signaling pathways implicated in myocardial infarction pathophysiology, emphasizing their mediators, biological roles, affected cellular processes, and therapeutic relevance. It is useful for linking mechanistic disease biology to candidate intervention points.*

### Ischemia-Reperfusion Injury
Reperfusion, while essential for myocardial salvage, paradoxically contributes up to 50% of the final infarct size through ischemia-reperfusion injury (MIRI) (buja2023pathobiologyofmyocardial pages 1-2, das2025networkpharmacologyapproaches pages 1-2). Key mechanisms include:

- **Oxidative stress:** Excessive ROS production from mitochondria, NADPH oxidases, and xanthine oxidase causes lipid peroxidation, protein oxidation, and DNA damage (das2025networkpharmacologyapproaches pages 2-4, das2025networkpharmacologyapproaches pages 4-6)
- **Calcium overload:** Disruption of Ca²⁺ homeostasis via Na⁺/Ca²⁺ exchanger activation activates injury pathways (das2025networkpharmacologyapproaches pages 2-4, sagris2024myocardialischemia–reperfusioninjury pages 2-3)
- **Mitochondrial dysfunction:** Sustained opening of the mitochondrial permeability transition pore (MPTP) results in loss of mitochondrial membrane potential and cessation of ATP production (buja2023pathobiologyofmyocardial pages 1-2)
- **Inflammatory response:** Neutrophil activation, cytokine release (TNF-α, IL-1β, IL-6), and adhesion molecule upregulation (ICAM-1, VCAM-1) (das2025networkpharmacologyapproaches pages 9-10, fede2025myocardialischemiareperfusioninjury pages 1-2)
- **Multiple cell death pathways:** Apoptosis, necroptosis, pyroptosis, ferroptosis, and dysregulated autophagy (fede2025myocardialischemiareperfusioninjury pages 1-2, das2025networkpharmacologyapproaches pages 4-6)

### Post-MI Cardiac Repair
Post-MI repair involves three overlapping phases: inflammatory, proliferative, and maturation/remodeling (hilgendorf2024repairofthe pages 3-4, hilgendorf2024repairofthe pages 1-3):

1. **Inflammatory phase:** DAMPs from dying cardiomyocytes activate TLR/NLR signaling, driving pro-inflammatory cytokine production (IL-1, TNF-α, IL-6) and chemokine-mediated recruitment of neutrophils and monocytes via CCL2/CCR2 signaling (hilgendorf2024repairofthe pages 3-4, hilgendorf2024repairofthe pages 1-3, ramosregalado2024theinfluenceof pages 6-7)
2. **Proliferative phase:** Macrophage efferocytosis triggers anti-inflammatory mediator release (IL-10, TGF-β), activating fibroblasts and promoting myofibroblast conversion (hilgendorf2024repairofthe pages 1-3, hilgendorf2024repairofthe pages 19-20)
3. **Maturation phase:** Organized collagen deposition forms protective scar tissue; excessive fibrosis leads to adverse remodeling and heart failure (hilgendorf2024repairofthe pages 1-3, hilgendorf2024repairofthe pages 23-25)

Cardiac macrophages are the predominant immune cells, existing in heterogeneous subpopulations with pro-inflammatory CCR2⁺ monocyte-derived macrophages and anti-inflammatory resident populations (Trem2hi, Bhlhe41⁺) (hilgendorf2024repairofthe pages 14-15, yang2025omicsbasedapproachtowards pages 4-5).

**Suggested GO terms:** GO:0006915 (apoptotic process); GO:0006954 (inflammatory response); GO:0042060 (wound healing); GO:0048661 (positive regulation of smooth muscle cell proliferation)
**Suggested CL terms:** CL:0000746 (cardiac muscle cell); CL:0000235 (macrophage); CL:0000775 (neutrophil); CL:0000057 (fibroblast)

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary:** Heart (UBERON:0000948), specifically myocardium (UBERON:0002349)
- **Secondary:** Lungs (pulmonary edema), kidneys (cardiorenal syndrome), brain (cardiogenic embolism)
- **Body systems:** Cardiovascular system (UBERON:0004535)

### Tissue and Cell Level
- **Cardiomyocytes** (CL:0000746): Primary target of ischemic injury
- **Endothelial cells** (CL:0000115): Endothelial dysfunction and microvascular injury
- **Cardiac fibroblasts** (CL:0000057): Fibrotic remodeling and scar formation
- **Vascular smooth muscle cells** (CL:0000359): Atherosclerotic plaque stability

### Subcellular Level
- **Mitochondria** (GO:0005739): Central role in MPTP opening and energy cessation
- **Sarcoplasmic reticulum:** Calcium handling dysfunction (SERCA2a impairment)
- **Cell membrane:** Lipid peroxidation damage

### Localization
Ischemic injury begins in the papillary muscle and subendocardium, then progresses toward the subepicardium (buja2023pathobiologyofmyocardial pages 2-4). The left anterior descending (LAD) coronary artery territory is the most commonly affected.

---

## 8. Temporal Development

### Onset
- **Typical age:** Predominantly adult and geriatric populations; increasing recognition of MI in younger patients (<45 years)
- **Onset pattern:** Acute, with sudden onset of symptoms
- **Critical window:** Reversible injury ~15 minutes; irreversible injury 20–60 minutes post-occlusion (buja2023pathobiologyofmyocardial pages 2-4)

### Progression
- **Acute phase (hours):** Cardiomyocyte death, inflammatory cascade initiation
- **Subacute phase (days–weeks):** Inflammatory resolution, granulation tissue formation, scar maturation
- **Chronic phase (weeks–months):** Ventricular remodeling, potential progression to heart failure
- **Reperfusion window:** If restored within 3–4 hours, significant myocardial salvage is achievable (buja2023pathobiologyofmyocardial pages 2-4)

---

## 9. Inheritance and Population

### Epidemiology
Cardiovascular diseases, led by ischemic heart disease (IHD) including MI, are the leading cause of death globally. According to GBD 2021, high systolic blood pressure is the dominant modifiable risk factor, with resource-abundant regions showing notable reductions in age-standardized death rates (EAPC of −3.43, 95% CI: −3.32, −3.53), while resource-limited regions experienced stagnation or increases.

### Genetic Architecture
MI is a polygenic/multifactorial disease with complex inheritance. A high PRS is associated with a threefold increase in MI risk (zhou2024associationofmetabolic pages 1-2). Key loci include 9p21 (*CDKN2B-AS1*), *LPA*, *PCSK9*, and *LDLR*. Penetrance is incomplete and strongly modified by environmental/lifestyle factors.

### Population Demographics
- **Sex ratio:** Males have higher incidence and earlier onset; females present more frequently with atypical symptoms
- **Age distribution:** Risk increases substantially with age; young MI (age <45) has a distinct risk profile with greater genetic contribution
- **Geographic variation:** Central Asia and Eastern Europe have the highest burden; high-income regions show declining trends

---

## 10. Diagnostics

### Clinical Tests
**ECG Criteria:** For STEMI diagnosis, new ST-segment elevation is required in ≥2 contiguous leads: ≥2.5 mm in men <40 years, ≥2 mm in men >40 years, or ≥1.5 mm in women in leads V2–V3, and/or ≥1 mm in other leads (młynarska2024fromatheroscleroticplaque pages 7-8).

**Biomarkers:** High-sensitivity cardiac troponin (hs-cTn I and T) is the preferred biomarker, with a rise-and-fall pattern above the 99th percentile upper reference limit consistent with acute myocardial injury (fede2025myocardialischemiareperfusioninjury pages 1-2, das2025networkpharmacologyapproaches pages 12-13). LDH rises later (24–48 hours) and may help differentiate infarction from reperfusion injury (das2025networkpharmacologyapproaches pages 12-13).

**Imaging:** Cardiac MRI is the gold standard for assessing myocardial damage, using late gadolinium enhancement (LGE) to distinguish infarcted from viable tissue and T2-weighted imaging for edema assessment (das2025networkpharmacologyapproaches pages 12-13). Echocardiography is widely used for wall motion assessment. Coronary angiography remains the definitive tool for identifying culprit lesions.

### Clinical Criteria
The Fourth Universal Definition of Myocardial Infarction (2018), published by ESC/ACC/AHA/WHF, establishes MI diagnosis based on evidence of myocardial injury (troponin rise/fall) in a clinical context of myocardial ischemia (fede2025myocardialischemiareperfusioninjury pages 1-2).

---

## 11. Outcome/Prognosis

### Survival and Mortality
MI remains the leading cause of cardiovascular mortality globally. In-hospital mortality for STEMI has declined substantially with primary PCI implementation. Cardiogenic shock complicates approximately 10% of AMI cases and carries high mortality. Long-term outcomes depend on infarct size, left ventricular function, completeness of revascularization, and comorbidities.

### Complications
- Heart failure (from adverse ventricular remodeling)
- Arrhythmias (reperfusion arrhythmias, ventricular fibrillation, sudden cardiac death)
- Mechanical complications (ventricular septal rupture, free wall rupture, papillary muscle rupture)
- Recurrent ischemic events
- Pericarditis (Dressler syndrome)

### Prognostic Biomarkers
- Infarct size (measured by cardiac MRI or peak troponin)
- Left ventricular ejection fraction
- Microvascular obstruction on cardiac MRI
- NT-proBNP levels
- High-sensitivity CRP

---

## 12. Treatment

### Pharmacotherapy

**Antiplatelet Therapy (MAXO:0001001):**
Dual antiplatelet therapy (DAPT) combining aspirin with a P2Y12 receptor inhibitor is standard care. Prasugrel is preferred over ticagrelor for PCI patients, with clopidogrel reserved for high bleeding risk or contraindications (młynarska2024fromatheroscleroticplaque pages 11-12, nicolau2025molecularmechanismsof pages 8-10). Cangrelor provides rapid intravenous platelet inhibition during PCI (nicolau2025molecularmechanismsof pages 8-10, occhipinti2025pharmacologicalandinterventional pages 6-8).

**Anticoagulants:**
Unfractionated heparin (UFH) is recommended for STEMI patients undergoing primary PCI, with enoxaparin and bivalirudin as alternatives (młynarska2024fromatheroscleroticplaque pages 11-12). Fondaparinux is preferred for NSTE-ACS patients not undergoing early invasive angiography (młynarska2024fromatheroscleroticplaque pages 11-12).

**Beta-Blockers:**
Metoprolol is recommended for STEMI patients without acute heart failure, reducing ventricular fibrillation risk and microvascular obstruction (młynarska2024fromatheroscleroticplaque pages 11-12).

**Statins:**
Atorvastatin, rosuvastatin, and simvastatin reduce LDL-cholesterol by up to 50% and exert cardioprotective anti-inflammatory effects (alradwan2024emergingtrendsand pages 4-7, ramosregalado2024theinfluenceof pages 10-11).

**ACE Inhibitors/ARBs:**
ACE inhibitors and ARBs provide cardioprotection by mitigating adverse effects of angiotensin II during and after MI (ramosregalado2024theinfluenceof pages 10-11).

**PCSK9 Inhibitors:**
Evolocumab and alirocumab provide additional LDL-lowering and modulate inflammatory responses via TLR4/NFκB signaling interference (ramosregalado2024theinfluenceof pages 10-11).

**Novel Agents:**
SGLT2 inhibitors (dapagliflozin) show clinical promise in both diabetic and non-diabetic MI patients, reducing inflammatory response and infarct size (ramosregalado2024theinfluenceof pages 10-11). Anti-inflammatory agents including tocilizumab (IL-6 inhibitor), anakinra (IL-1 receptor antagonist), and colchicine show cardioprotective effects by reducing infarct size (sagris2024myocardialischemia–reperfusioninjury pages 8-10).

### Interventional Procedures (MAXO:0000474)
Primary percutaneous coronary intervention (PCI) is the gold standard for STEMI reperfusion. The 2023 ESC guidelines recommend consideration of intravascular imaging (OCT/IVUS) to guide PCI (Class IIa) (nicolau2025molecularmechanismsof pages 15-17).

### Experimental Therapies
Key currently recruiting Phase 3 clinical trials are summarized below:

| NCT Number | Trial Name/Description | Intervention/Drug | Sponsor | Enrollment | Novel Mechanism/Target |
|---|---|---|---|---:|---|
| NCT06118281 | ARTEMIS – research study of ziltivekimab vs placebo after heart attack | Ziltivekimab | Novo Nordisk A/S | 10000 | Anti-inflammatory IL-6 pathway inhibition to reduce recurrent events after MI (sagris2024myocardialischemia–reperfusioninjury pages 8-10) |
| NCT07478003 | PULSE-MI 2 – prehospital pulse-dose glucocorticoid in STEMI | Pulse-dose glucocorticoid | Rigshospitalet, Denmark | 5204 | Early anti-inflammatory immunomodulation during acute STEMI/reperfusion |
| NCT06174753 | Dapagliflozin in STEMI | Dapagliflozin | Ottawa Heart Institute Research Corporation | 256 | SGLT2 inhibition; metabolic and anti-inflammatory cardioprotection with infarct-limiting potential (ramosregalado2024theinfluenceof pages 10-11) |
| NCT06364150 | Therapeutic use of angiopoietin-primed autologous peripheral blood stem cell in myocardial infarction | Angiopoietin-primed autologous peripheral blood stem cells | Seoul National Hospital | 30 | Regenerative cell therapy aimed at myocardial repair and neovascularization (das2025networkpharmacologyapproaches pages 32-33, alradwan2024emergingtrendsand pages 4-7) |
| NCT05577988 | Early de-escalation to low-potency single antiplatelet therapy guided by genetics vs systematic high-potency single antiplatelet therapy after ACS | Genotype-guided antiplatelet de-escalation | Assistance Publique - Hôpitaux de Paris | 2468 | Precision antiplatelet therapy using pharmacogenetic guidance for P2Y12-pathway modulation (młynarska2024fromatheroscleroticplaque pages 11-12, nicolau2025molecularmechanismsof pages 8-10) |
| NCT07320625 | Efficacy of montelukast on STEMI patients | Montelukast | Shanghai Zhongshan Hospital | 512 | Leukotriene receptor antagonism to modulate inflammation in STEMI |
| NCT07301034 | Study of ziltivekimab effect on coronary plaque vs placebo after heart attack | Ziltivekimab with plaque imaging endpoint | Novo Nordisk A/S | 332 | IL-6 pathway inhibition with imaging-based assessment of plaque biology/inflammation |
| NCT07467213 | Routine use of potassium competitive acid blocker vs guideline-directed gastrointestinal protection in acute myocardial infarction | Potassium-competitive acid blocker strategy | Samsung Medical Center | 5000 | Supportive strategy to optimize GI protection during intensive antithrombotic therapy after AMI |
| NCT07295223 | GALACTUS – effect of GLP-1 and antidiabetic SGLT2 agents for myocardial infarction and ultrasensitive inflammatory surveillance | GLP-1 agent and SGLT2 agent strategy | Instituto Mexicano del Seguro Social | 44 | Cardiometabolic and anti-inflammatory modulation using incretin/SGLT2 pathways after MI (ramosregalado2024theinfluenceof pages 10-11) |


*Table: This table summarizes currently recruiting phase 3 interventional trials in myocardial infarction and related acute coronary syndromes mentioned in the evidence-gathering workflow. It highlights sponsor, scale, and the mechanistic rationale of each study to support translational and therapeutic landscape mapping.*

### Advanced Therapeutics
- **Cell therapy:** Stem cell and progenitor cell transplantation for myocardial repair (das2025networkpharmacologyapproaches pages 32-33, alradwan2024emergingtrendsand pages 4-7)
- **Gene therapy:** CRISPR-based approaches for genetic correction of CVD risk factors; anti-apoptotic gene therapy with Bcl-2 (das2025networkpharmacologyapproaches pages 32-33, alradwan2024emergingtrendsand pages 4-7)
- **RNA-based therapies:** MicroRNA modulation for cardioprotection; siRNA inclisiran for PCSK9 silencing
- **Immunotherapies:** IL-1 and IL-6 inhibitors (canakinumab, tocilizumab) to reduce cardiovascular events (sagris2024myocardialischemia–reperfusioninjury pages 8-10)

---

## 13. Prevention

### Primary Prevention
- Risk factor modification: Blood pressure control, LDL-cholesterol reduction, smoking cessation, weight management, regular physical activity
- Statin therapy for high-risk individuals
- Aspirin for selected high-risk patients (with evolving guidelines)

### Secondary Prevention
- DAPT therapy post-MI
- High-intensity statin therapy
- ACE inhibitors/ARBs
- Beta-blockers
- Cardiac rehabilitation
- Risk stratification using polygenic risk scores (PRS) may improve early intervention in genetically predisposed individuals (zhou2024associationofmetabolic pages 1-2)

### Tertiary Prevention
- Optimization of heart failure management
- Implantable cardioverter-defibrillator (ICD) for high-risk patients
- Long-term antiplatelet and lipid-lowering therapy

### Behavioral Interventions
Diet modification (Mediterranean diet, omega-3 fatty acids), regular exercise, stress management, and alcohol moderation are established risk-reducing strategies (zhou2024associationofmetabolic pages 1-2, zhou2024associationofmetabolic pages 13-15).

---

## 14. Other Species / Natural Disease

### Naturally Occurring Disease
MI occurs naturally in dogs, cats, horses, and non-human primates, though it is less common than in humans. Companion animals, particularly dogs, can develop MI secondary to coronary atherosclerosis or vasculitis.

### Comparative Biology
Zebrafish have high genetic homology with humans (70% of human genes have identifiable zebrafish orthologs) and offer unique advantages for cardiovascular research due to their remarkable cardiac regenerative capacity (wang2026zebrafishincardiovascular pages 1-3). Unlike mammals, zebrafish scars after cardiac injury are temporary and do not permanently hinder regeneration (wang2026zebrafishincardiovascular pages 14-16).

---

## 15. Model Organisms

### Small Animal Models
**Mouse and Rat Models:** Left anterior descending (LAD) coronary artery ligation is the standard injury model, inducing ischemia followed by reperfusion (alsadder2025cardiacischaemia–reperfusioninjury pages 8-9, das2025networkpharmacologyapproaches pages 10-12). Genetically modified models include Spontaneously Hypertensive Rats (SHR), diabetic rats, and Apoe⁻/⁻ mice for studying cardiovascular disease mechanisms. Limitations include higher heart rates and different electrophysiological properties compared to humans (alsadder2025cardiacischaemia–reperfusioninjury pages 8-9).

**Zebrafish Models (Danio rerio; NCBI Taxon: 7955):** Zebrafish offer high-throughput screening capability, embryonic transparency for real-time cardiac imaging, and robust cardiac regenerative capacity through cardiomyocyte proliferation (wang2026zebrafishincardiovascular pages 14-16, wang2026zebrafishincardiovascular pages 1-3). Injury models include cryoinjury and genetic ablation. Comparative single-cell profiling has identified distinct cardiac resident macrophage populations (hbaa⁺ Mac and timp4.3⁺ Mac3) essential for zebrafish heart regeneration. Key limitation: two-chambered heart with single-circuit circulation (wang2026zebrafishincardiovascular pages 14-16).

### Large Animal Models
**Porcine Models:** Offer the greatest translational value due to closest resemblance to human cardiac physiology. Used for PCI-related research and device testing. Limitation: typically healthy animals that don't fully represent pathological comorbidity conditions (alsadder2025cardiacischaemia–reperfusioninjury pages 8-9).

### In Vitro Models
Emerging models include iPSC-derived cardiomyocytes and organ-on-chip systems for studying ischemia-reperfusion injury with improved human relevance (alsadder2025cardiacischaemia–reperfusioninjury pages 14-15).

### Model Limitations
Translation of preclinical findings to clinical settings remains challenging due to species differences in cardiac physiology, immune responses, and myocardial repair mechanisms. Variability in experimental protocols between in vitro and in vivo models can lead to inconsistent results and reproducibility issues (das2025networkpharmacologyapproaches pages 10-12, alsadder2025cardiacischaemia–reperfusioninjury pages 14-15).

---

## Summary of Key Ontology Annotations

**Disease Ontology:** MONDO:0005068 (myocardial infarction)
**Key HPO Terms:** HP:0001658 (Myocardial infarction); HP:0001681 (Angina pectoris); HP:0001649 (Tachycardia); HP:0002094 (Dyspnea)
**Key GO Terms:** GO:0006915 (apoptotic process); GO:0006954 (inflammatory response); GO:0042060 (wound healing); GO:0097193 (intrinsic apoptotic signaling pathway); GO:0070059 (intrinsic apoptotic signaling in response to ER stress)
**Key UBERON Terms:** UBERON:0000948 (heart); UBERON:0002349 (myocardium); UBERON:0001621 (coronary artery)
**Key CL Terms:** CL:0000746 (cardiac muscle cell); CL:0000235 (macrophage); CL:0000775 (neutrophil); CL:0000057 (fibroblast); CL:0000115 (endothelial cell)
**Key CHEBI Terms:** CHEBI:39025 (high-density lipoprotein cholesterol); CHEBI:39026 (low-density lipoprotein cholesterol)
**Key MAXO Terms:** MAXO:0001001 (antiplatelet therapy); MAXO:0000474 (surgical intervention); MAXO:0000009 (drug therapy)

References

1. (fede2025myocardialischemiareperfusioninjury pages 1-2): Maria Sofia Fede, Gloria Daziani, Francesco Tavoletta, Angelo Montana, Paolo Compagnucci, Gaia Goteri, Margherita Neri, and Francesco Paolo Busardò. Myocardial ischemia/reperfusion injury: molecular insights, forensic perspectives, and therapeutic horizons. Cells, 14:1509, Sep 2025. URL: https://doi.org/10.3390/cells14191509, doi:10.3390/cells14191509. This article has 30 citations.

2. (młynarska2024fromatheroscleroticplaque pages 17-19): Ewelina Młynarska, Witold Czarnik, Piotr Fularski, Joanna Hajdys, Gabriela Majchrowicz, Magdalena Stabrawa, Jacek Rysz, and Beata Franczyk. From atherosclerotic plaque to myocardial infarction—the leading cause of coronary artery occlusion. Jul 2024. URL: https://doi.org/10.3390/ijms25137295, doi:10.3390/ijms25137295. This article has 152 citations.

3. (OpenTargets Search: myocardial infarction): Open Targets Query (myocardial infarction, 25 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

4. (das2025networkpharmacologyapproaches pages 1-2): Joy Das, Ashok Kumar Sah, Ranjay Kumar Choudhary, Rabab H. Elshaikh, Utpal Bhui, Shreya Chowdhury, Anass M. Abbas, Manar G. Shalabi, Nadeem Ahmad Siddique, Raji Rubayyi Alshammari, Navjyot Trivedi, Khoula Salim Ali Buwaiqi, Said Al Ghenaimi, and Pranav Kumar Prabhakar. Network pharmacology approaches to myocardial infarction reperfusion injury: exploring mechanisms, pathophysiology, and novel therapies. Biomedicines, 13:1532, Jun 2025. URL: https://doi.org/10.3390/biomedicines13071532, doi:10.3390/biomedicines13071532. This article has 15 citations.

5. (zhou2024associationofmetabolic pages 1-2): Junyu Zhou, Meiling Liu, and Sunmin Park. Association of metabolic diseases and moderate fat intake with myocardial infarction risk. Nutrients, 16:4273, Dec 2024. URL: https://doi.org/10.3390/nu16244273, doi:10.3390/nu16244273. This article has 2 citations.

6. (zhou2024associationofmetabolic pages 10-13): Junyu Zhou, Meiling Liu, and Sunmin Park. Association of metabolic diseases and moderate fat intake with myocardial infarction risk. Nutrients, 16:4273, Dec 2024. URL: https://doi.org/10.3390/nu16244273, doi:10.3390/nu16244273. This article has 2 citations.

7. (zhou2024associationofmetabolic pages 13-15): Junyu Zhou, Meiling Liu, and Sunmin Park. Association of metabolic diseases and moderate fat intake with myocardial infarction risk. Nutrients, 16:4273, Dec 2024. URL: https://doi.org/10.3390/nu16244273, doi:10.3390/nu16244273. This article has 2 citations.

8. (młynarska2024fromatheroscleroticplaque pages 7-8): Ewelina Młynarska, Witold Czarnik, Piotr Fularski, Joanna Hajdys, Gabriela Majchrowicz, Magdalena Stabrawa, Jacek Rysz, and Beata Franczyk. From atherosclerotic plaque to myocardial infarction—the leading cause of coronary artery occlusion. Jul 2024. URL: https://doi.org/10.3390/ijms25137295, doi:10.3390/ijms25137295. This article has 152 citations.

9. (das2025networkpharmacologyapproaches pages 12-13): Joy Das, Ashok Kumar Sah, Ranjay Kumar Choudhary, Rabab H. Elshaikh, Utpal Bhui, Shreya Chowdhury, Anass M. Abbas, Manar G. Shalabi, Nadeem Ahmad Siddique, Raji Rubayyi Alshammari, Navjyot Trivedi, Khoula Salim Ali Buwaiqi, Said Al Ghenaimi, and Pranav Kumar Prabhakar. Network pharmacology approaches to myocardial infarction reperfusion injury: exploring mechanisms, pathophysiology, and novel therapies. Biomedicines, 13:1532, Jun 2025. URL: https://doi.org/10.3390/biomedicines13071532, doi:10.3390/biomedicines13071532. This article has 15 citations.

10. (ramosregalado2024theinfluenceof pages 10-11): Lisaidy Ramos-Regalado, Sebastià Alcover, Lina Badimon, and Gemma Vilahur. The influence of metabolic risk factors on the inflammatory response triggered by myocardial infarction: bridging pathophysiology to treatment. Cells, 13:1125, Jun 2024. URL: https://doi.org/10.3390/cells13131125, doi:10.3390/cells13131125. This article has 17 citations.

11. (młynarska2024fromatheroscleroticplaque pages 11-12): Ewelina Młynarska, Witold Czarnik, Piotr Fularski, Joanna Hajdys, Gabriela Majchrowicz, Magdalena Stabrawa, Jacek Rysz, and Beata Franczyk. From atherosclerotic plaque to myocardial infarction—the leading cause of coronary artery occlusion. Jul 2024. URL: https://doi.org/10.3390/ijms25137295, doi:10.3390/ijms25137295. This article has 152 citations.

12. (nicolau2025molecularmechanismsof pages 8-10): Andre M. Nicolau, Pedro G. Silva, Hernan Patricio G. Mejía, Juan F. Granada, Grzegorz L. Kaluza, Daniel Burkhoff, Thiago Abizaid, Brunna Pileggi, Antônio F. D. Freire, Roger R. Godinho, Carlos M. Campos, Fabio S. de Brito, Alexandre Abizaid, and Pedro H. C. Melo. Molecular mechanisms of microvascular obstruction and dysfunction in percutaneous coronary interventions: from pathophysiology to therapeutics—a comprehensive review. International Journal of Molecular Sciences, 26:6835, Jul 2025. URL: https://doi.org/10.3390/ijms26146835, doi:10.3390/ijms26146835. This article has 20 citations.

13. (alradwan2024emergingtrendsand pages 4-7): Ibrahim Alradwan, Nojoud AL Fayez, Mohammad N. Alomary, Abdullah A. Alshehri, Alhassan H. Aodah, Fahad A. Almughem, Khulud A. Alsulami, Ahmad M. Aldossary, Abdullah O. Alawad, Yahya M. K. Tawfik, and Essam A. Tawfik. Emerging trends and innovations in the treatment and diagnosis of atherosclerosis and cardiovascular disease: a comprehensive review towards healthier aging. Pharmaceutics, 16:1037, Aug 2024. URL: https://doi.org/10.3390/pharmaceutics16081037, doi:10.3390/pharmaceutics16081037. This article has 31 citations.

14. (occhipinti2025pharmacologicalandinterventional pages 6-8): Giovanni Occhipinti, Michele Strosio, Riccardo Rinaldi, Andrea Ruberti, and Salvatore Brugaletta. Pharmacological and interventional prevention and treatment of microvascular obstruction following primary pci in stemi. Journal of Cardiovascular Development and Disease, 12:440, Nov 2025. URL: https://doi.org/10.3390/jcdd12110440, doi:10.3390/jcdd12110440. This article has 1 citations.

15. (sagris2024myocardialischemia–reperfusioninjury pages 8-10): Marios Sagris, Anastasios Apostolos, Panagiotis Theofilis, Nikolaos Ktenopoulos, Odysseas Katsaros, Sotirios Tsalamandris, Konstantinos Tsioufis, Konstantinos Toutouzas, and Dimitris Tousoulis. Myocardial ischemia–reperfusion injury: unraveling pathophysiology, clinical manifestations, and emerging prevention strategies. Biomedicines, 12:802, Apr 2024. URL: https://doi.org/10.3390/biomedicines12040802, doi:10.3390/biomedicines12040802. This article has 73 citations.

16. (das2025networkpharmacologyapproaches pages 9-10): Joy Das, Ashok Kumar Sah, Ranjay Kumar Choudhary, Rabab H. Elshaikh, Utpal Bhui, Shreya Chowdhury, Anass M. Abbas, Manar G. Shalabi, Nadeem Ahmad Siddique, Raji Rubayyi Alshammari, Navjyot Trivedi, Khoula Salim Ali Buwaiqi, Said Al Ghenaimi, and Pranav Kumar Prabhakar. Network pharmacology approaches to myocardial infarction reperfusion injury: exploring mechanisms, pathophysiology, and novel therapies. Biomedicines, 13:1532, Jun 2025. URL: https://doi.org/10.3390/biomedicines13071532, doi:10.3390/biomedicines13071532. This article has 15 citations.

17. (buja2023pathobiologyofmyocardial pages 2-4): L. Maximilian Buja. Pathobiology of myocardial ischemia and reperfusion injury: models, modes, molecular mechanisms, modulation, and clinical applications. Cardiology in Review, 31:252-264, Feb 2023. URL: https://doi.org/10.1097/crd.0000000000000440, doi:10.1097/crd.0000000000000440. This article has 111 citations and is from a peer-reviewed journal.

18. (buja2023pathobiologyofmyocardial pages 1-2): L. Maximilian Buja. Pathobiology of myocardial ischemia and reperfusion injury: models, modes, molecular mechanisms, modulation, and clinical applications. Cardiology in Review, 31:252-264, Feb 2023. URL: https://doi.org/10.1097/crd.0000000000000440, doi:10.1097/crd.0000000000000440. This article has 111 citations and is from a peer-reviewed journal.

19. (wang2025theroleof pages 16-17): Xueyang Wang, Ruiqi Liu, and Dan Liu. The role of the mapk signaling pathway in cardiovascular disease: pathophysiological mechanisms and clinical therapy. International Journal of Molecular Sciences, 26:2667, Mar 2025. URL: https://doi.org/10.3390/ijms26062667, doi:10.3390/ijms26062667. This article has 51 citations.

20. (wang2025theroleof pages 4-6): Xueyang Wang, Ruiqi Liu, and Dan Liu. The role of the mapk signaling pathway in cardiovascular disease: pathophysiological mechanisms and clinical therapy. International Journal of Molecular Sciences, 26:2667, Mar 2025. URL: https://doi.org/10.3390/ijms26062667, doi:10.3390/ijms26062667. This article has 51 citations.

21. (fede2025myocardialischemiareperfusioninjury pages 26-28): Maria Sofia Fede, Gloria Daziani, Francesco Tavoletta, Angelo Montana, Paolo Compagnucci, Gaia Goteri, Margherita Neri, and Francesco Paolo Busardò. Myocardial ischemia/reperfusion injury: molecular insights, forensic perspectives, and therapeutic horizons. Cells, 14:1509, Sep 2025. URL: https://doi.org/10.3390/cells14191509, doi:10.3390/cells14191509. This article has 30 citations.

22. (das2025networkpharmacologyapproaches pages 7-9): Joy Das, Ashok Kumar Sah, Ranjay Kumar Choudhary, Rabab H. Elshaikh, Utpal Bhui, Shreya Chowdhury, Anass M. Abbas, Manar G. Shalabi, Nadeem Ahmad Siddique, Raji Rubayyi Alshammari, Navjyot Trivedi, Khoula Salim Ali Buwaiqi, Said Al Ghenaimi, and Pranav Kumar Prabhakar. Network pharmacology approaches to myocardial infarction reperfusion injury: exploring mechanisms, pathophysiology, and novel therapies. Biomedicines, 13:1532, Jun 2025. URL: https://doi.org/10.3390/biomedicines13071532, doi:10.3390/biomedicines13071532. This article has 15 citations.

23. (fede2025myocardialischemiareperfusioninjury pages 10-12): Maria Sofia Fede, Gloria Daziani, Francesco Tavoletta, Angelo Montana, Paolo Compagnucci, Gaia Goteri, Margherita Neri, and Francesco Paolo Busardò. Myocardial ischemia/reperfusion injury: molecular insights, forensic perspectives, and therapeutic horizons. Cells, 14:1509, Sep 2025. URL: https://doi.org/10.3390/cells14191509, doi:10.3390/cells14191509. This article has 30 citations.

24. (hilgendorf2024repairofthe pages 3-4): Ingo Hilgendorf, Stefan Frantz, and Nikolaos G. Frangogiannis. Repair of the infarcted heart: cellular effectors, molecular mechanisms and therapeutic opportunities. Circulation Research, 134:1718-1751, Jun 2024. URL: https://doi.org/10.1161/circresaha.124.323658, doi:10.1161/circresaha.124.323658. This article has 172 citations and is from a highest quality peer-reviewed journal.

25. (zhang2024ischemiareperfusioninjurymolecular pages 3-4): Meng Zhang, Qian Liu, Hui Meng, Hongxia Duan, Xin Liu, Jian Wu, Fei Gao, Shijun Wang, Rubin Tan, and Jinxiang Yuan. Ischemia-reperfusion injury: molecular mechanisms and therapeutic targets. Signal Transduction and Targeted Therapy, Jan 2024. URL: https://doi.org/10.1038/s41392-023-01688-x, doi:10.1038/s41392-023-01688-x. This article has 731 citations and is from a peer-reviewed journal.

26. (yin2023postmyocardialinfarctionfibrosis pages 6-8): Xiaoying Yin, Xinxin Yin, Xin Pan, Jingyu Zhang, Xinhui Fan, Jiaxin Li, X. Zhai, Lijun Jiang, Panpan Hao, Jiali Wang, and Yuguo Chen. Post-myocardial infarction fibrosis: pathophysiology, examination, and intervention. Frontiers in Pharmacology, Mar 2023. URL: https://doi.org/10.3389/fphar.2023.1070973, doi:10.3389/fphar.2023.1070973. This article has 99 citations.

27. (hilgendorf2024repairofthe pages 15-17): Ingo Hilgendorf, Stefan Frantz, and Nikolaos G. Frangogiannis. Repair of the infarcted heart: cellular effectors, molecular mechanisms and therapeutic opportunities. Circulation Research, 134:1718-1751, Jun 2024. URL: https://doi.org/10.1161/circresaha.124.323658, doi:10.1161/circresaha.124.323658. This article has 172 citations and is from a highest quality peer-reviewed journal.

28. (hilgendorf2024repairofthe pages 1-3): Ingo Hilgendorf, Stefan Frantz, and Nikolaos G. Frangogiannis. Repair of the infarcted heart: cellular effectors, molecular mechanisms and therapeutic opportunities. Circulation Research, 134:1718-1751, Jun 2024. URL: https://doi.org/10.1161/circresaha.124.323658, doi:10.1161/circresaha.124.323658. This article has 172 citations and is from a highest quality peer-reviewed journal.

29. (hilgendorf2024repairofthe pages 19-20): Ingo Hilgendorf, Stefan Frantz, and Nikolaos G. Frangogiannis. Repair of the infarcted heart: cellular effectors, molecular mechanisms and therapeutic opportunities. Circulation Research, 134:1718-1751, Jun 2024. URL: https://doi.org/10.1161/circresaha.124.323658, doi:10.1161/circresaha.124.323658. This article has 172 citations and is from a highest quality peer-reviewed journal.

30. (das2025networkpharmacologyapproaches pages 15-16): Joy Das, Ashok Kumar Sah, Ranjay Kumar Choudhary, Rabab H. Elshaikh, Utpal Bhui, Shreya Chowdhury, Anass M. Abbas, Manar G. Shalabi, Nadeem Ahmad Siddique, Raji Rubayyi Alshammari, Navjyot Trivedi, Khoula Salim Ali Buwaiqi, Said Al Ghenaimi, and Pranav Kumar Prabhakar. Network pharmacology approaches to myocardial infarction reperfusion injury: exploring mechanisms, pathophysiology, and novel therapies. Biomedicines, 13:1532, Jun 2025. URL: https://doi.org/10.3390/biomedicines13071532, doi:10.3390/biomedicines13071532. This article has 15 citations.

31. (fede2025myocardialischemiareperfusioninjury pages 12-14): Maria Sofia Fede, Gloria Daziani, Francesco Tavoletta, Angelo Montana, Paolo Compagnucci, Gaia Goteri, Margherita Neri, and Francesco Paolo Busardò. Myocardial ischemia/reperfusion injury: molecular insights, forensic perspectives, and therapeutic horizons. Cells, 14:1509, Sep 2025. URL: https://doi.org/10.3390/cells14191509, doi:10.3390/cells14191509. This article has 30 citations.

32. (das2025networkpharmacologyapproaches pages 4-6): Joy Das, Ashok Kumar Sah, Ranjay Kumar Choudhary, Rabab H. Elshaikh, Utpal Bhui, Shreya Chowdhury, Anass M. Abbas, Manar G. Shalabi, Nadeem Ahmad Siddique, Raji Rubayyi Alshammari, Navjyot Trivedi, Khoula Salim Ali Buwaiqi, Said Al Ghenaimi, and Pranav Kumar Prabhakar. Network pharmacology approaches to myocardial infarction reperfusion injury: exploring mechanisms, pathophysiology, and novel therapies. Biomedicines, 13:1532, Jun 2025. URL: https://doi.org/10.3390/biomedicines13071532, doi:10.3390/biomedicines13071532. This article has 15 citations.

33. (das2025networkpharmacologyapproaches pages 2-4): Joy Das, Ashok Kumar Sah, Ranjay Kumar Choudhary, Rabab H. Elshaikh, Utpal Bhui, Shreya Chowdhury, Anass M. Abbas, Manar G. Shalabi, Nadeem Ahmad Siddique, Raji Rubayyi Alshammari, Navjyot Trivedi, Khoula Salim Ali Buwaiqi, Said Al Ghenaimi, and Pranav Kumar Prabhakar. Network pharmacology approaches to myocardial infarction reperfusion injury: exploring mechanisms, pathophysiology, and novel therapies. Biomedicines, 13:1532, Jun 2025. URL: https://doi.org/10.3390/biomedicines13071532, doi:10.3390/biomedicines13071532. This article has 15 citations.

34. (sagris2024myocardialischemia–reperfusioninjury pages 2-3): Marios Sagris, Anastasios Apostolos, Panagiotis Theofilis, Nikolaos Ktenopoulos, Odysseas Katsaros, Sotirios Tsalamandris, Konstantinos Tsioufis, Konstantinos Toutouzas, and Dimitris Tousoulis. Myocardial ischemia–reperfusion injury: unraveling pathophysiology, clinical manifestations, and emerging prevention strategies. Biomedicines, 12:802, Apr 2024. URL: https://doi.org/10.3390/biomedicines12040802, doi:10.3390/biomedicines12040802. This article has 73 citations.

35. (ramosregalado2024theinfluenceof pages 6-7): Lisaidy Ramos-Regalado, Sebastià Alcover, Lina Badimon, and Gemma Vilahur. The influence of metabolic risk factors on the inflammatory response triggered by myocardial infarction: bridging pathophysiology to treatment. Cells, 13:1125, Jun 2024. URL: https://doi.org/10.3390/cells13131125, doi:10.3390/cells13131125. This article has 17 citations.

36. (hilgendorf2024repairofthe pages 23-25): Ingo Hilgendorf, Stefan Frantz, and Nikolaos G. Frangogiannis. Repair of the infarcted heart: cellular effectors, molecular mechanisms and therapeutic opportunities. Circulation Research, 134:1718-1751, Jun 2024. URL: https://doi.org/10.1161/circresaha.124.323658, doi:10.1161/circresaha.124.323658. This article has 172 citations and is from a highest quality peer-reviewed journal.

37. (hilgendorf2024repairofthe pages 14-15): Ingo Hilgendorf, Stefan Frantz, and Nikolaos G. Frangogiannis. Repair of the infarcted heart: cellular effectors, molecular mechanisms and therapeutic opportunities. Circulation Research, 134:1718-1751, Jun 2024. URL: https://doi.org/10.1161/circresaha.124.323658, doi:10.1161/circresaha.124.323658. This article has 172 citations and is from a highest quality peer-reviewed journal.

38. (yang2025omicsbasedapproachtowards pages 4-5): Chao Yang, Huajun Li, Yuxing Chen, Weizi Zhu, and Jian’an Wang. Omics-based approach towards macrophages: new perspectives of biology and function in the normal and diseased heart. International Journal of Biological Sciences, 21:3666-3688, May 2025. URL: https://doi.org/10.7150/ijbs.112061, doi:10.7150/ijbs.112061. This article has 3 citations and is from a peer-reviewed journal.

39. (nicolau2025molecularmechanismsof pages 15-17): Andre M. Nicolau, Pedro G. Silva, Hernan Patricio G. Mejía, Juan F. Granada, Grzegorz L. Kaluza, Daniel Burkhoff, Thiago Abizaid, Brunna Pileggi, Antônio F. D. Freire, Roger R. Godinho, Carlos M. Campos, Fabio S. de Brito, Alexandre Abizaid, and Pedro H. C. Melo. Molecular mechanisms of microvascular obstruction and dysfunction in percutaneous coronary interventions: from pathophysiology to therapeutics—a comprehensive review. International Journal of Molecular Sciences, 26:6835, Jul 2025. URL: https://doi.org/10.3390/ijms26146835, doi:10.3390/ijms26146835. This article has 20 citations.

40. (das2025networkpharmacologyapproaches pages 32-33): Joy Das, Ashok Kumar Sah, Ranjay Kumar Choudhary, Rabab H. Elshaikh, Utpal Bhui, Shreya Chowdhury, Anass M. Abbas, Manar G. Shalabi, Nadeem Ahmad Siddique, Raji Rubayyi Alshammari, Navjyot Trivedi, Khoula Salim Ali Buwaiqi, Said Al Ghenaimi, and Pranav Kumar Prabhakar. Network pharmacology approaches to myocardial infarction reperfusion injury: exploring mechanisms, pathophysiology, and novel therapies. Biomedicines, 13:1532, Jun 2025. URL: https://doi.org/10.3390/biomedicines13071532, doi:10.3390/biomedicines13071532. This article has 15 citations.

41. (wang2026zebrafishincardiovascular pages 1-3): Ranran Wang, Qian Zhang, Shuhui Zhang, Ziyan Wang, Zongyuan Zhou, Tianyi Yuan, and Bo Zhang. Zebrafish in cardiovascular disease research: from model to application. International Journal of Biological Sciences, 22:4806-4825, Apr 2026. URL: https://doi.org/10.7150/ijbs.131893, doi:10.7150/ijbs.131893. This article has 0 citations and is from a peer-reviewed journal.

42. (wang2026zebrafishincardiovascular pages 14-16): Ranran Wang, Qian Zhang, Shuhui Zhang, Ziyan Wang, Zongyuan Zhou, Tianyi Yuan, and Bo Zhang. Zebrafish in cardiovascular disease research: from model to application. International Journal of Biological Sciences, 22:4806-4825, Apr 2026. URL: https://doi.org/10.7150/ijbs.131893, doi:10.7150/ijbs.131893. This article has 0 citations and is from a peer-reviewed journal.

43. (alsadder2025cardiacischaemia–reperfusioninjury pages 8-9): Lujain Alsadder and Abdulaziz Hamadah. Cardiac ischaemia–reperfusion injury: pathophysiology, therapeutic targets and future interventions. Biomedicines, 13:2084, Aug 2025. URL: https://doi.org/10.3390/biomedicines13092084, doi:10.3390/biomedicines13092084. This article has 19 citations.

44. (das2025networkpharmacologyapproaches pages 10-12): Joy Das, Ashok Kumar Sah, Ranjay Kumar Choudhary, Rabab H. Elshaikh, Utpal Bhui, Shreya Chowdhury, Anass M. Abbas, Manar G. Shalabi, Nadeem Ahmad Siddique, Raji Rubayyi Alshammari, Navjyot Trivedi, Khoula Salim Ali Buwaiqi, Said Al Ghenaimi, and Pranav Kumar Prabhakar. Network pharmacology approaches to myocardial infarction reperfusion injury: exploring mechanisms, pathophysiology, and novel therapies. Biomedicines, 13:1532, Jun 2025. URL: https://doi.org/10.3390/biomedicines13071532, doi:10.3390/biomedicines13071532. This article has 15 citations.

45. (alsadder2025cardiacischaemia–reperfusioninjury pages 14-15): Lujain Alsadder and Abdulaziz Hamadah. Cardiac ischaemia–reperfusion injury: pathophysiology, therapeutic targets and future interventions. Biomedicines, 13:2084, Aug 2025. URL: https://doi.org/10.3390/biomedicines13092084, doi:10.3390/biomedicines13092084. This article has 19 citations.

## Artifacts

- [Edison artifact artifact-00](Myocardial_Infarction-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Myocardial_Infarction-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](Myocardial_Infarction-deep-research-falcon_artifacts/artifact-02.md)