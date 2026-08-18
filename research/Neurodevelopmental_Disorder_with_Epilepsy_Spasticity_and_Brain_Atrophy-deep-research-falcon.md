---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-15T08:33:20.743950'
end_time: '2026-08-15T08:43:07.981619'
duration_seconds: 587.24
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Neurodevelopmental Disorder with Epilepsy, Spasticity, and Brain Atrophy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 17
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Neurodevelopmental_Disorder_with_Epilepsy_Spasticity_and_Brain_Atrophy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder with Epilepsy, Spasticity, and Brain Atrophy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder with Epilepsy, Spasticity, and Brain Atrophy** covering all of the
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
- **Disease Name:** Neurodevelopmental Disorder with Epilepsy, Spasticity, and Brain Atrophy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder with Epilepsy, Spasticity, and Brain Atrophy** covering all of the
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


# Neurodevelopmental Disorder With Epilepsy, Spasticity, and Brain Atrophy (NEDESBA)

## Executive summary

NEDESBA is an ultra-rare, autosomal-recessive, progressive neurodevelopmental/neurodegenerative **TRAPPopathy** caused by biallelic pathogenic variants in **TRAPPC4**. The usual presentation is an initially unremarkable neonatal period followed during early infancy by profound developmental impairment or regression, progressive microcephaly, epilepsy, spastic tetraplegia, impaired vision, and progressive cerebral—often also cerebellar—atrophy. The recurrent hypomorphic splice variant **NM_016146.5:c.454+3A>G** accounts for most published cases. Patient-fibroblast and yeast experiments directly demonstrate impaired TRAPP-complex assembly, delayed Golgi trafficking, and defective autophagic flux. No disease-modifying treatment or disease-specific clinical trial has been established; current practice is molecular diagnosis, symptomatic epilepsy management, multidisciplinary supportive care, and genetic counseling. (bergen2020deficienciesinvesicular pages 1-2, ghosh2021arelativelycommon pages 1-2, hall2024trappopathiesseveremultisystem pages 7-9)

| Field | Evidence-backed value | Suggested ontology/identifier |
|---|---|---|
| Disease name | Neurodevelopmental disorder with epilepsy, spasticity, and brain atrophy (NEDESBA); TRAPPC4-related neurodevelopmental disorder (forno2025childneurologytrappc4related pages 1-2, ghosh2021arelativelycommon pages 1-2) | MONDO:0032894; OMIM phenotype: 618741 |
| Disease type / evidence granularity | Mendelian, aggregated disease-level knowledge derived primarily from published case series/cohorts plus functional cellular/yeast studies, not EHR-derived population studies (bergen2020deficienciesinvesicular pages 1-2, ghosh2021arelativelycommon pages 2-3) | Disease category: Mendelian disorder |
| Causal gene | **TRAPPC4** (trafficking protein particle complex subunit 4; synbindin), core TRAPP subunit (bergen2020deficienciesinvesicular pages 2-3, ghosh2021arelativelycommon pages 1-2, bergen2020deficienciesinvesicular pages 1-2) | HGNC: TRAPPC4; Ensembl: ENSG00000196655; OMIM gene: 610971 |
| Primary disease mechanism class | Autosomal recessive TRAPPopathy with defective vesicular trafficking and autophagy due to reduced/altered TRAPPC4 function (direct evidence) (bergen2020deficienciesinvesicular pages 1-2, hall2024trappopathiesseveremultisystem pages 7-9) | GO: vesicle-mediated transport; GO: autophagy; Rab1 GEF-related TRAPP function |
| Inheritance | Autosomal recessive; all confirmed affected individuals reported with biallelic/homozygous pathogenic variants (ghosh2021arelativelycommon pages 2-3, forno2025childneurologytrappc4related pages 1-2, hall2024trappopathiesseveremultisystem pages 7-9) | HP:0000007 |
| MONDO/target association | Open Targets shows disease-target association between MONDO_0032894 and **TRAPPC4** (OpenTargets Search: neurodevelopmental disorder with epilepsy spasticity and brain atrophy-TRAPPC4) | MONDO_0032894 ↔ ENSG00000196655 |
| Recurrent pathogenic variant | Homozygous splice-site variant **NM_016146.5:c.454+3A>G**; rs375776811; recurrent across unrelated families; causes aberrant/leaky splicing with reduced full-length transcript and protein (bergen2020deficienciesinvesicular pages 1-2, ghosh2021arelativelycommon pages 2-3, ghosh2021arelativelycommon pages 1-2) | ClinVar: VCV000812649.1; variant type: splice-region/intronic |
| Founder vs hotspot | Not established as a founder allele; SNP array/haplotype data favored **hotspot or recurrent variant** rather than shared founder effect in at least some families (direct evidence) (bergen2020deficienciesinvesicular pages 1-2) | Population-genetic note: founder effect not established |
| Additional reported TRAPPC4 variants | 2024 review summarizes missense **p.Leu64Pro** and **p.Pro93Leu** in Indian families; also ClinVar-listed **p.Leu125Pro** and **p.Gly213Ter220delinsXaa** reported as pathogenic/likely pathogenic in AR NEDESBA spectrum. These statements are **review-level synthesis** and should be independently verified in variant databases/primary case reports before KB hard-coding (hall2024trappopathiesseveremultisystem pages 7-9) | HGVS protein variants; ACMG class: verify in ClinVar/lab submission |
| Allele frequency | Carrier frequency for c.454+3A>G estimated at **2.4–5.4 per 10,000** healthy individuals; heterozygous MAF reported about **0.033–0.054%** in unaffected cohorts/public datasets (ghosh2021arelativelycommon pages 1-2, ghosh2021arelativelycommon pages 4-6, ghosh2021arelativelycommon pages 6-7) | Population databases: gnomAD/100K Genomes/GeneDx cohorts (study-reported) |
| Penetrance | Reported homozygous individuals were clinically affected, suggesting **full penetrance in known cases** for homozygous c.454+3A>G; broader penetrance across all TRAPPC4 variants remains not established (ghosh2021arelativelycommon pages 4-6) | Penetrance: appears high/complete for known homozygotes |
| Typical onset | Usually normal pregnancy/neonatal course followed by onset in **first months of life**; seizures often begin in the **first 6 months** (ghosh2021arelativelycommon pages 4-6, bergen2020deficienciesinvesicular pages 1-2) | HPO onset: infantile onset |
| Disease course | Severe **progressive encephalopathy/neurodegeneration** with developmental stagnation, regression, microcephaly progression, and worsening brain atrophy (ghosh2021arelativelycommon pages 4-6, ghosh2021arelativelycommon pages 6-7) | HP:0002344; progressive course |
| Developmental phenotype | Profound psychomotor delay / severe developmental delay is a core feature; developmental stagnation and loss of acquired milestones common (ghosh2021arelativelycommon pages 1-2, ghosh2021arelativelycommon pages 4-6) | HP:0011344; HP:0001263; HP:0002376 |
| Regression frequency | Psychomotor regression reported in **all phenotyped individuals** in expanded cohort text (ghosh2021arelativelycommon pages 4-6, ghosh2021arelativelycommon pages 6-7) | HP:0002376 |
| Epilepsy frequency | Early-onset epilepsy is a core feature; in initial Brain cohort seizures in **7/7**; larger cohort states all patients had seizure onset in first 6 months where described (bergen2020deficienciesinvesicular pages 15-16, ghosh2021arelativelycommon pages 4-6) | HP:0001250 |
| Seizure types | Variable: infantile spasms, focal, tonic-clonic, atonic, tonic; occasional gelastic seizures reported in earlier cases (ghosh2021arelativelycommon pages 4-6, ghosh2021arelativelycommon pages 6-7) | HP:0012469; HP:0002123; HP:0002069 |
| EEG | Non-specific; generalized disorganization and epileptiform discharges reported (ghosh2021arelativelycommon pages 4-6) | EEG abnormality; HPO term suggestion: HP:0002353 |
| Spasticity / motor syndrome | Spastic tetraplegia/spastic quadriparesis and hyperreflexia are major hallmarks; initial cohort had impaired mobility **7/7** (bergen2020deficienciesinvesicular pages 15-16, ghosh2021arelativelycommon pages 4-6, bergen2020deficienciesinvesicular pages 1-2) | HP:0002510; HP:0001270; HP:0001347 |
| Microcephaly | Common and often progressive/severe; initial cohort **7/7**; expanded cohort mean OFC approximately **-5.77 SD** at ~5 years (bergen2020deficienciesinvesicular pages 15-16, ghosh2021arelativelycommon pages 4-6) | HP:0000252 |
| Intellectual disability | Severe/profound intellectual disability/developmental impairment; initial cohort **7/7** (bergen2020deficienciesinvesicular pages 15-16, bergen2020deficienciesinvesicular pages 1-2) | HP:0001249 |
| Visual involvement | Visual impairment/poor pursuits common; initial cohort vision issues **3/6**; later review estimated visual impairment around **83%** but this is secondary synthesis and may reflect ascertainment differences (forno2025childneurologytrappc4related pages 2-4, bergen2020deficienciesinvesicular pages 15-16, ghosh2021arelativelycommon pages 4-6) | HP:0000505; HP:0000657; HP:0001133 |
| Cataracts / optic findings | Bilateral cataracts reported in some patients; optic nerve pallor in 2025 case report/reviewed siblings (ghosh2021arelativelycommon pages 4-6, forno2025childneurologytrappc4related pages 1-2) | HP:0000518; HP:0000648 |
| Hearing involvement | Sensorineural hearing loss reported; initial cohort hearing loss **2/6**; later review-level estimate ~14% (forno2025childneurologytrappc4related pages 2-4, bergen2020deficienciesinvesicular pages 15-16, bergen2020deficienciesinvesicular pages 1-2) | HP:0000407 |
| Movement disorders | Dystonia/ataxia/dyskinesia present in a subset; review-level estimate ~44% movement disorder, but direct cohort counts are smaller (forno2025childneurologytrappc4related pages 2-4, ghosh2021arelativelycommon pages 4-6) | HP:0001332; HP:0001251; HP:0100022 |
| Muscle involvement | Reduced muscle mass/wasting common clinically; primary muscle disease **not established**. Rare cases with elevated lactate/CK and episodic rhabdomyolysis-like features reported (ghosh2021arelativelycommon pages 6-7, hall2024trappopathiesseveremultisystem pages 7-9) | HP:0003202; HP:0003391; possible HP:0003201 |
| Dysmorphism | Subtle, non-specific facial dysmorphism frequent: bitemporal narrowing, thick eyebrows, full cheeks, long philtrum, wide mouth, tented upper lip, pointed chin (ghosh2021arelativelycommon pages 4-6) | HPO suggestions: HP:0000341, HP:0000316, HP:0000179 |
| Brain MRI | Consistent **global cerebral atrophy**, often cortical + cerebellar atrophy, ventriculomegaly/ventricular enlargement, white matter loss/abnormalities, enlarged subarachnoid spaces, thin corpus callosum/hypoplasia; sometimes brainstem or basal ganglia involvement (ghosh2021arelativelycommon pages 4-6, ghosh2021arelativelycommon pages 6-7, bergen2020deficienciesinvesicular pages 1-2) | HP:0002059; HP:0001272; HP:0001273; HP:0002120; HP:0002079 |
| MRI progression | Older children often show more severe cerebral/cerebellar atrophy, suggesting progression (ghosh2021arelativelycommon pages 6-7) | Progressive neuroimaging abnormality |
| Affected anatomy | Primary: CNS/brain—cerebral cortex, cerebellum, corpus callosum, white matter; likely vulnerable neuronal populations include pyramidal neurons, Purkinje cells, and motor neurons based on expression/biology (direct + inference) (bergen2020deficienciesinvesicular pages 2-3, hall2024trappopathiesseveremultisystem pages 7-9) | UBERON: brain, cerebellum, cerebral cortex, corpus callosum; CL: pyramidal neuron, Purkinje cell, motor neuron |
| Upstream molecular defect | TRAPPC4 is a core component of TRAPP complexes and essential for **Rab1 GEF activity**; pathogenic variants reduce TRAPPC4 transcript/protein and destabilize/impair TRAPP complex assembly (direct evidence) (bergen2020deficienciesinvesicular pages 1-2, bergen2020deficienciesinvesicular pages 15-16) | GO:0034058? Rab GEF complex-related; Rab1 pathway |
| Cellular mechanism | **Direct evidence:** delayed trafficking into and out of the Golgi in patient fibroblasts; basal autophagy defect and delayed autophagic flux, possibly due to unsealed autophagosomes; rescue by lentiviral WT TRAPPC4 (bergen2020deficienciesinvesicular pages 1-2, bergen2020deficienciesinvesicular pages 16-17) | GO:0006888 ER-to-Golgi vesicle-mediated transport; GO:0006914 autophagy; GO:0048193 Golgi vesicle transport |
| Neuronal mechanism beyond fibroblasts | **Inference/expert synthesis:** neurodegeneration likely reflects high neuronal dependence on membrane trafficking/autophagy; TRAPPC4 may contribute to dendrite maturation via syndecan-2-associated vesicle recruitment (review of prior basic science, not direct NEDESBA patient evidence) (hall2024trappopathiesseveremultisystem pages 7-9) | GO: dendrite development; CL: pyramidal neuron |
| Environmental/lifestyle risks | **Not established.** No disease-specific environmental, toxin, lifestyle, sex, or infectious causal risk factors identified. Infections are reported as causes of death/clinical stressors, not established etiologic triggers (ghosh2021arelativelycommon pages 6-7) | Unknown/not established |
| Diagnostics: core approach | Molecular diagnosis by **WES/WGS** with segregation analysis; RNA studies useful because splice variant may be missed/deprioritized by exome filtering. Ancillary evaluation includes MRI and EEG (ghosh2021arelativelycommon pages 4-6, ghosh2021arelativelycommon pages 2-3, ghosh2021arelativelycommon pages 6-7, bergen2020deficienciesinvesicular pages 1-2) | WES/WGS; RNA-seq; Sanger confirmation |
| RNA-based diagnosis | RNA-seq from fibroblasts demonstrated partial exon 3 skipping and aberrant cryptic splice donor usage, supporting pathogenicity and utility of transcript analysis (ghosh2021arelativelycommon pages 1-2, ghosh2021arelativelycommon pages 6-7) | Transcriptomics / RNA-seq |
| Differential diagnostic neighborhood | Other TRAPPopathies and early infantile neurodegenerative/developmental epileptic encephalopathies with microcephaly, spasticity, and brain atrophy; disease-specific formal criteria **not established** (ghosh2021arelativelycommon pages 1-2, bergen2020deficienciesinvesicular pages 15-16) | TRAPPopathy spectrum |
| Biomarkers | No validated disease-specific circulating biomarker established. Occasional elevated lactate/CK/transaminases reported in some individuals with muscle involvement, but not specific or consistently present (ghosh2021arelativelycommon pages 6-7, hall2024trappopathiesseveremultisystem pages 7-9) | Biomarker status: not established |
| Treatment | No disease-modifying therapy established. Symptomatic treatment includes anti-seizure medications with often **partial response** (levetiracetam, clobazam; in a 2025 case levetiracetam/valproate initially responsive) plus multidisciplinary supportive care (forno2025childneurologytrappc4related pages 1-2, ghosh2021arelativelycommon pages 4-6, hall2024trappopathiesseveremultisystem pages 7-9) | NCIT: Anticonvulsant Therapy; Supportive Care |
| Clinical trials | **No disease-specific interventional clinical trials identified** in search results available here (clinical-trials search negative) (OpenTargets Search: neurodevelopmental disorder with epilepsy spasticity and brain atrophy-TRAPPC4) | ClinicalTrials.gov: none found |
| Prevention / family planning | Primary prevention not established. Practical prevention is genetic counseling, cascade family testing, carrier detection, and reproductive options (prenatal/preimplantation testing) once familial variant is known; screening utility specifically suggested because recurrent allele has measurable carrier frequency in some populations (ghosh2021arelativelycommon pages 6-7) | Genetic counseling; carrier screening |
| Prognosis | Severe lifelong neurodevelopmental disability with progressive neurologic decline. Early death reported in **5/23** individuals in one series, mean **8.8 years**, mainly from infections; full survival distribution remains unknown (ghosh2021arelativelycommon pages 6-7) | Prognosis: poor, progressive |
| Epidemiology | Ultra-rare; no population prevalence/incidence studies. By 2025, review/case literature suggested approximately **32 reported cases**, but this likely includes overlapping published cohorts and should be treated cautiously (forno2025childneurologytrappc4related pages 2-4) | Prevalence/incidence: unknown |
| Population distribution | Families reported from multiple ancestries including Iranian, Egyptian, Portuguese, English, mixed European-American, Turkish, Caucasian, French-Canadian; no single founder proven (ghosh2021arelativelycommon pages 2-3, bergen2020deficienciesinvesicular pages 1-2) | Geographic distribution: multicontinental case reports |
| Sex ratio | **Not established** from available summarized evidence (ghosh2021arelativelycommon pages 4-6) | Unknown/not established |
| Natural disease in other species | **Not established**; no naturally occurring veterinary disease linked to TRAPPC4 identified in available evidence (hall2024trappopathiesseveremultisystem pages 7-9) | OMIA: no evidence found |
| Experimental models | **Direct models:** patient fibroblasts and yeast **trs23** temperature-sensitive model validated trafficking/autophagy defects. **Mouse:** complete knockout is embryonic lethal (review-level statement). Disease-specific advanced neuronal/iPSC/organoid models are limited/not yet established in published direct evidence summarized here (hall2024trappopathiesseveremultisystem pages 7-9, bergen2020deficienciesinvesicular pages 16-17, bergen2020deficienciesinvesicular pages 1-2) | Model systems: fibroblast; Saccharomyces cerevisiae trs23; mouse KO (embryonic lethal) |
| Key knowledge gaps | Variant spectrum beyond c.454+3A>G, natural history, standardized outcome measures, prognostic biomarkers, tissue-specific mechanisms in neurons, and therapeutic strategies all remain incompletely defined (hall2024trappopathiesseveremultisystem pages 7-9) | Research gap annotation |


*Table: This table condenses the main evidence-backed knowledge-base fields for TRAPPC4-related NEDESBA, including identifiers, recurrent and additional variants, phenotype frequencies, mechanism, diagnostics, prognosis, and model systems. It also flags where evidence is direct versus inferred and where items remain unknown or not established.*

## 1. Disease information

**Definition.** NEDESBA is a severe Mendelian encephalopathy in which deficient TRAPPC4 function disrupts intracellular membrane trafficking and autophagy. It was first molecularly delineated by Van Bergen et al.; the report was accepted October 7, 2019 and published in *Brain* in 2020. Open Targets links the disease to one target, TRAPPC4, supported by five evidence records. (OpenTargets Search: neurodevelopmental disorder with epilepsy spasticity and brain atrophy-TRAPPC4, bergen2020deficienciesinvesicular pages 1-2)

**Identifiers and names**

- **MONDO:** MONDO:0032894.
- **OMIM phenotype:** 618741.
- **OMIM gene:** TRAPPC4, 610971.
- **Gene:** TRAPPC4, trafficking protein particle complex subunit 4; Ensembl ENSG00000196655; historical protein name **synbindin**.
- **Synonyms:** NEDESBA; TRAPPC4-related neurodevelopmental disorder; TRAPPC4-related encephalopathy; TRAPPC4-related early-infantile neurodegenerative syndrome; severe syndromic intellectual disability due to TRAPPC4 deficiency.
- **Orphanet:** no confidently verified disease-specific ORPHA identifier was found in the retrieved evidence.
- **ICD-10/ICD-11 and MeSH:** no specific code or descriptor is established; coding ordinarily uses broader categories for developmental/epileptic encephalopathy, intellectual disability, epilepsy, microcephaly, and spastic quadriplegia.

The knowledge base is aggregated from published families, case series, diagnostic cohorts, patient-derived fibroblasts, and experimental models—not from population-level EHR surveillance. The foundational article studied seven children from three families; the subsequent expansion described 23 patients from 17 families and brought the authors’ combined reported total to 27. Counts in later reviews overlap these publications and must not be summed as independent cases. (ghosh2021arelativelycommon pages 1-2, ghosh2021arelativelycommon pages 4-6, ghosh2021arelativelycommon pages 2-3, bergen2020deficienciesinvesicular pages 1-2)

**Exact primary-literature quotation:** “Here, we report 23 patients from 17 independent families with an early-infantile-onset neurodegenerative presentation” carrying homozygous c.454+3A>G. (ghosh2021arelativelycommon pages 1-2)

## 2. Etiology, risk, protective factors, and gene–environment interaction

### Causal factor

The primary cause is **germline biallelic TRAPPC4 dysfunction**. The predominant allele, c.454+3A>G, is a leaky noncanonical splice-site variant: RNA sequencing showed partial exon 3 skipping and use of a downstream cryptic donor, producing frameshifted transcripts predicted to undergo nonsense-mediated decay. Residual correctly spliced transcript explains viability and supports a hypomorphic loss-of-function mechanism. Complete Trappc4 knockout is reportedly embryonic lethal in mice. (ghosh2021arelativelycommon pages 1-2, ghosh2021arelativelycommon pages 4-6, hall2024trappopathiesseveremultisystem pages 7-9)

### Genetic risk

- Homozygosity or compound heterozygosity for pathogenic TRAPPC4 alleles is the established risk.
- Heterozygous c.454+3A>G carriers appear clinically unaffected.
- Study-reported carrier frequency was **2.4–5.4 per 10,000** healthy individuals; heterozygous allele frequencies were approximately 0.033–0.054% in GeneDx and 100,000 Genomes datasets. (ghosh2021arelativelycommon pages 1-2, ghosh2021arelativelycommon pages 4-6)
- No shared haplotype was demonstrated across Turkish and Caucasian families, favoring a recurrent hotspot over a proven founder effect. A remote common ancestor cannot be excluded. (ghosh2021arelativelycommon pages 6-7, bergen2020deficienciesinvesicular pages 1-2)

### Environmental, infectious, lifestyle, and protective factors

No toxin, diet, lifestyle, occupational exposure, pathogen, sex, parental age, or environmental exposure is known to cause NEDESBA. Infections caused several reported deaths but are not established etiologic triggers. No genetic protective variants, modifier genes, dietary protection, or validated gene–environment interaction has been identified. Residual wild-type TRAPPC4 expression is likely a determinant of viability and may modify severity, but this is a mechanistic inference rather than a validated protective allele. (ghosh2021arelativelycommon pages 6-7, hall2024trappopathiesseveremultisystem pages 7-9)

## 3. Phenotypes

The best quantified initial cohort had seizures, intellectual disability, developmental delay/regression, microcephaly, and impaired mobility in **7/7**; MRI abnormalities in **4/4**, hearing loss in **2/6**, and visual problems in **3/6** evaluable individuals. Later series broadened the spectrum, but missing data and cohort overlap limit precise percentages. (bergen2020deficienciesinvesicular pages 15-16)

| Phenotype and type | Characteristics and frequency | Suggested HPO term |
|---|---|---|
| Developmental delay/intellectual disability | Severe-to-profound; motor, language, and social stagnation begins in the first months | Global developmental delay HP:0001263; intellectual disability HP:0001249 |
| Developmental regression | Progressive loss of early milestones; reported in all phenotyped individuals in the expanded series | Developmental regression HP:0002376 |
| Epilepsy | Usually begins before 6 months; spasms, focal, tonic, atonic, and tonic-clonic seizures; occasional gelastic seizures | Seizure HP:0001250; infantile spasms HP:0012469 |
| EEG abnormality | Nonspecific generalized disorganization and epileptiform discharges | Abnormal EEG HP:0002353 |
| Progressive microcephaly | Severe; mean OFC approximately **−5.77 SD at about age 5 years** in the expanded cohort | Microcephaly HP:0000252; progressive microcephaly HP:0000253 |
| Spastic tetraplegia/hyperreflexia | Core progressive motor manifestation; contractures and severe mobility impairment follow | Spastic tetraplegia HP:0002510; hyperreflexia HP:0001347; joint contracture HP:0001371 |
| Movement disorder | Dystonia, dyskinesia, or ataxia in a subset; a later synthesis estimated 44% | Dystonia HP:0001332; ataxia HP:0001251 |
| Visual dysfunction | Poor/absent visual pursuit, cortical visual dysfunction, optic pallor/atrophy; later synthesis estimated 83%, but ascertainment differs | Visual impairment HP:0000505; optic atrophy HP:0000648 |
| Cataract | Bilateral cataracts in three expanded-cohort patients | Cataract HP:0000518 |
| Sensorineural hearing loss | 2/6 in the initial cohort; later synthesis estimated 14% | Sensorineural hearing impairment HP:0000407 |
| Brain atrophy | Universal or near-universal in imaged cohorts; progressive cerebral ± cerebellar involvement | Cerebral atrophy HP:0002059; cerebellar atrophy HP:0001272 |
| White-matter/callosal abnormalities | White-matter loss, ventriculomegaly, enlarged subarachnoid spaces, thin/hypoplastic corpus callosum | Abnormal cerebral white matter HP:0002500; ventriculomegaly HP:0002119; thin corpus callosum HP:0002079 |
| Muscle wasting | Common, probably often secondary to immobility; occasional CK/lactate elevation or rhabdomyolysis-like episodes | Muscle wasting HP:0003202; elevated CK HP:0003236 |
| Facial appearance | Subtle bitemporal narrowing, thick eyebrows, full cheeks, long philtrum, wide mouth, tented upper lip, pointed chin | Long philtrum HP:0000343; thick eyebrow HP:0000574; pointed chin HP:0000307 |

Seizures showed partial responses to levetiracetam or clobazam in many patients, although refractory epilepsy occurred. The profound cognitive, motor, visual, communication, and feeding/mobility burden implies major lifelong impairment in activities of daily living. No NEDESBA-specific EQ-5D, SF-36, PROMIS, caregiver-burden, or quality-of-life study is available. (ghosh2021arelativelycommon pages 4-6, ghosh2021arelativelycommon pages 6-7)

## 4. Genetic and molecular information

### Gene and variant spectrum

**TRAPPC4** encodes a core component shared by mammalian TRAPPII and TRAPPIII complexes. The major allele is:

- **NM_016146.5:c.454+3A>G**, hg38 chr11:119020256A>G, rs375776811; ClinVar aggregate accession reported as **VCV000812649.1**. It is an intronic splice-altering, hypomorphic loss-of-function allele. (ghosh2021arelativelycommon pages 2-3, ghosh2021arelativelycommon pages 6-7)

The December 2024 expert review also summarized homozygous missense variants **p.Leu64Pro** and **p.Pro93Leu** in three individuals from two Indian families, plus ClinVar-listed p.Leu125Pro and p.Gly213Ter220delinsXaa. The missense changes were predicted to reduce stability or alter intramolecular interactions, but these claims require variant-level confirmation in the original case reports and current ClinVar submissions before assigning definitive ACMG classes in a production database. (hall2024trappopathiesseveremultisystem pages 7-9)

All reported disease variants are germline. Somatic TRAPPC4 mutation is not part of NEDESBA. No recurrent disease-causing chromosomal deletion, translocation, inversion, repeat expansion, mitochondrial variant, modifier gene, or disease-specific epigenetic signature has been established. The absence of additional clinically relevant TRAPPC4 variants among more than 10,000 screened neurodevelopmental cases in the 2021 study emphasized the unusual dominance of c.454+3A>G in early reports. (ghosh2021arelativelycommon pages 1-2, ghosh2021arelativelycommon pages 2-3)

### Penetrance and expressivity

All known c.454+3A>G homozygotes in the expanded study were affected, suggesting high or complete penetrance in identified homozygotes. Expressivity is variable for seizure type/control, cataract, hearing loss, dystonia/ataxia, muscle biochemical abnormalities, and hypothalamic findings. Anticipation has not been reported. Germline mosaicism is theoretically possible for any recessive variant but has not been documented. (ghosh2021arelativelycommon pages 4-6)

## 5. Environmental information

No environmental toxicant, radiation, pollution, smoking, alcohol, diet, exercise pattern, occupation, or infectious agent is implicated in causation. Infection is clinically relevant as a complication: five deaths in one series were attributed to infections. Unlike some other TRAPPopathies, infection-triggered regression or metabolic crises have not been established systematically for TRAPPC4 disease. (ghosh2021arelativelycommon pages 6-7)

## 6. Mechanism and pathophysiology

### Evidence-supported causal chain

1. **Upstream genetic lesion:** biallelic hypomorphic TRAPPC4 variants reduce correctly spliced transcript and TRAPPC4 protein.
2. **Complex dysfunction:** reduced TRAPPC4 impairs assembly or stability of core TRAPP complexes. TRAPPC4 is required for Rab1 guanine-nucleotide exchange activity.
3. **Trafficking defect:** patient fibroblasts show delayed entry into and exit from the Golgi using VSVG-GFP-ts045.
4. **Autophagy defect:** fibroblasts show impaired basal autophagy and delayed autophagic flux, possibly involving unsealed autophagosomes.
5. **Cellular vulnerability:** long-lived neurons depend heavily on membrane/protein homeostasis, axodendritic transport, and autophagy; pyramidal neurons, Purkinje cells, and motor neurons express TRAPPC4 and are plausible vulnerable populations.
6. **Tissue phenotype:** neuronal dysfunction and loss produce developmental regression, epilepsy, cortical/cerebellar atrophy, microcephaly, and corticospinal spasticity. Steps 1–4 are directly demonstrated; the detailed neuron-to-phenotype bridge remains biologically compelling but incompletely tested in disease-specific neuronal models. (bergen2020deficienciesinvesicular pages 2-3, bergen2020deficienciesinvesicular pages 16-17, hall2024trappopathiesseveremultisystem pages 7-9, bergen2020deficienciesinvesicular pages 1-2)

**Exact primary-literature quotation:** “Lentiviral expression of wild-type TRAPPC4 in these fibroblasts restored trafficking, suggesting that the trafficking defect was due to reduced TRAPPC4 levels.” (bergen2020deficienciesinvesicular pages 1-2)

**Exact primary-literature quotation:** “the fibroblasts had a basal autophagy defect and a delay in autophagic flux, possibly due to unsealed autophagosomes.” (bergen2020deficienciesinvesicular pages 1-2)

Suggested annotations include **GO:0006888** ER-to-Golgi vesicle-mediated transport, **GO:0048193** Golgi vesicle transport, **GO:0006914** autophagy, **GO:0016192** vesicle-mediated transport, and Rab-protein signal transduction. Candidate cell terms include pyramidal neuron, Purkinje cell, upper motor neuron, lower motor neuron, oligodendrocyte, and astrocyte; only neuronal expression/vulnerability is reasonably supported, whereas glial involvement remains inferential.

No validated NEDESBA transcriptomic signature beyond aberrant TRAPPC4 splicing, nor disease-specific proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or integrated multi-omics atlas, is available. Occasional lactate/CK elevations do not establish a primary metabolic pathway defect. Immune dysregulation is not established. (ghosh2021arelativelycommon pages 6-7, hall2024trappopathiesseveremultisystem pages 7-9)

## 7. Anatomical structures affected

The primary organ is the **central nervous system**. MRI implicates bilateral cerebral cortex and subcortical white matter, corpus callosum, cerebellum, ventricles/subarachnoid spaces, and variably brainstem and basal ganglia. Suggested anatomy terms include UBERON:0000955 brain, UBERON:0001954 Ammon’s horn/hippocampal formation where relevant to basic expression studies, UBERON:0002037 cerebellum, UBERON:0001851 cortex, UBERON:0002336 corpus callosum, and UBERON:0002437 cerebral white matter. Disease is generally diffuse and bilateral rather than lateralized. Skeletal muscle wasting is often secondary, though primary muscle involvement may occur in a minority. (ghosh2021arelativelycommon pages 6-7, hall2024trappopathiesseveremultisystem pages 7-9)

At the subcellular level, implicated compartments are the endoplasmic reticulum–Golgi trafficking axis, Golgi apparatus, transport vesicles, recycling endosomes, autophagosomes, and lysosomal degradation pathway. Suggested GO Cellular Component annotations are Golgi apparatus, ER–Golgi intermediate compartment, transport vesicle, TRAPP complex, autophagosome, and lysosome. (hall2024trappopathiesseveremultisystem pages 7-9, bergen2020deficienciesinvesicular pages 1-2)

## 8. Temporal development

Pregnancy, delivery, and the neonatal period are often unremarkable. Developmental stagnation and encephalopathy emerge within the first months; seizures usually begin by six months. Some children acquire limited early milestones before losing them. Microcephaly, spasticity, contractures, disability, and MRI atrophy progress through childhood. Cerebellar and cerebral atrophy appeared more severe in older children. The disease is chronic, lifelong, and progressive rather than relapsing-remitting; spontaneous remission is not reported. (ghosh2021arelativelycommon pages 4-6, ghosh2021arelativelycommon pages 6-7)

The infancy period is probably the key diagnostic and therapeutic window because injury begins early, but no trial has established that presymptomatic intervention changes outcome. Later-onset regression and seizures are possible with some missense alleles, suggesting genotype-dependent timing. (forno2025childneurologytrappc4related pages 1-2, hall2024trappopathiesseveremultisystem pages 7-9)

## 9. Inheritance and population

Inheritance is **autosomal recessive** (HPO HP:0000007). For two carrier parents, standard Mendelian counseling predicts a 25% affected, 50% carrier, and 25% non-carrier probability per pregnancy, assuming both parental variants are pathogenic and penetrance is high.

No population prevalence or incidence has been measured. The disease is therefore best classified as ultra-rare. A 2025 report estimated approximately 32 published cases, but this includes overlapping cohorts and should not be treated as a prevalence numerator. Families have Iranian, Egyptian, Portuguese, English, mixed European-American, Caucasian, Turkish, French-Canadian, and Indian backgrounds; there is no demonstrated ethnic restriction. Sex ratio and age-specific population distribution are unknown. (forno2025childneurologytrappc4related pages 2-4, ghosh2021arelativelycommon pages 2-3, bergen2020deficienciesinvesicular pages 1-2)

Consanguinity may facilitate homozygosity but is not required; several families were nonconsanguineous. No confirmed founder population, genetic anticipation, or population-specific disease prevalence is known. (ghosh2021arelativelycommon pages 6-7)

## 10. Diagnostics

### Recommended clinical and molecular approach

1. Recognize the combination of infantile developmental stagnation/regression, progressive microcephaly, epilepsy, spastic quadriparesis, and diffuse brain atrophy.
2. Obtain brain MRI, EEG, audiology, ophthalmology assessment, feeding/swallowing assessment, and neurologic/rehabilitation evaluation.
3. Use a developmental-and-epileptic-encephalopathy or spasticity/brain-atrophy multigene panel containing **TRAPPC4**, or preferably trio WES/WGS where the phenotype is nonspecific.
4. Confirm candidate variants and segregation with Sanger sequencing.
5. If c.454+3A>G or another potential splice variant is found—or WES is negative despite a compelling phenotype—perform RNA studies from fibroblasts or another informative tissue. RNA-seq directly demonstrated exon 3 skipping and cryptic donor use. (ghosh2021arelativelycommon pages 2-3, ghosh2021arelativelycommon pages 6-7)

**Exact abstract quotation:** “No other clinically relevant TRAPPC4 variants were identified among any of over 10,000 patients with neurodevelopmental conditions.” (ghosh2021arelativelycommon pages 1-2)

CMA can detect alternative copy-number diagnoses but is not the primary test for the recurrent single-nucleotide allele. Karyotyping, FISH, mitochondrial DNA, and repeat-expansion testing have no disease-specific indication unless suggested by the differential diagnosis. There are no formal clinical diagnostic criteria and no validated biochemical biomarker. CK, lactate, and transaminases may be checked when weakness, rhabdomyolysis, or acute deterioration occurs, but abnormalities are inconsistent and nonspecific. (ghosh2021arelativelycommon pages 6-7)

Important differentials include other TRAPPopathies—particularly TRAPPC2L, TRAPPC6B, TRAPPC9, TRAPPC11, and TRAPPC12 disorders—and other developmental/epileptic encephalopathies, hereditary spastic paraplegias, pontocerebellar degenerations, mitochondrial disorders, congenital disorders of glycosylation, and neurodegenerative conditions causing microcephaly and atrophy. (ghosh2021arelativelycommon pages 1-2, bergen2020deficienciesinvesicular pages 15-16)

## 11. Outcome and prognosis

The expected outcome is severe lifelong disability, typically with profound cognitive and communication impairment, nonambulatory spastic tetraplegia, epilepsy, visual dysfunction, and complete dependence for daily care. Recovery of lost skills has not been documented. Complications likely include aspiration/feeding difficulty, respiratory infections, contractures, scoliosis, pain, low bone density, immobility, and antiseizure-drug adverse effects, although not all have been systematically quantified.

In the expanded cohort, **5/23 (21.7%)** died from infections at a mean age of **8.8 years**. This is not a population mortality estimate: the cohort was small, follow-up heterogeneous, and survival curves were not reported. Five- and ten-year survival, overall life expectancy, validated prognostic biomarkers, and standardized quality-of-life outcomes remain unknown. (ghosh2021arelativelycommon pages 6-7)

## 12. Treatment and current applications

There is **no approved disease-modifying, gene, cell, RNA, or targeted therapy** for NEDESBA. No disease-specific interventional trial was identified in the ClinicalTrials.gov searches performed for this report.

Current implementation is supportive and individualized:

- **Epilepsy:** standard antiseizure medications selected by seizure type; levetiracetam, clobazam, and valproate have been used. Partial response is common, but drug resistance occurs. Suggested NCIT concept: Anticonvulsant Therapy.
- **Motor management:** physical and occupational therapy, positioning, stretching, orthoses, mobility/seating equipment, surveillance for hip displacement/scoliosis, and management of spasticity/contractures. Suggested NCIT concepts: Physical Therapy, Occupational Therapy, Rehabilitation Therapy, Supportive Care.
- **Communication and feeding:** speech/augmentative-communication therapy; swallow and nutritional assessment; enteral feeding when clinically indicated.
- **Vision/hearing:** ophthalmologic and audiologic surveillance; treat cataract or hearing impairment where feasible.
- **Respiratory and infection prevention:** airway-clearance plans, aspiration mitigation, routine vaccination, and prompt treatment of infections.
- **Bone health and pain:** assess vitamin D/calcium status, immobility-related osteopenia, fractures, and discomfort.

The most compelling experimental direction is restoration of adequate TRAPPC4 expression because wild-type transduction rescued trafficking in patient fibroblasts. This is proof of mechanism, not evidence that gene replacement is safe or effective in patients. Autophagy or Rab-pathway modulation is likewise hypothetical and may have broad off-target effects. The 2024 review concluded that therapeutic development remains largely unexplored. (bergen2020deficienciesinvesicular pages 16-17, hall2024trappopathiesseveremultisystem pages 7-9)

No disease-specific pharmacogenomic guidance, treatment-response rate, surgical algorithm, immunotherapy, or combination-therapy evidence exists.

## 13. Prevention

The genetic defect cannot currently be prevented through lifestyle modification, vaccination, environmental control, or prophylactic medication. Relevant prevention is genetic and tertiary:

- **Primary/reproductive:** counseling, parental confirmation, cascade testing, partner testing where appropriate, prenatal diagnosis, or preimplantation genetic testing after familial variants are established.
- **Secondary:** no population or newborn biochemical screening exists. Targeted carrier testing may be reasonable in an affected family; broader carrier screening requires validation despite the measurable c.454+3A>G carrier frequency.
- **Tertiary:** early seizure management, rehabilitation, aspiration precautions, vaccination, infection control, contracture prevention, nutritional support, and bone-health surveillance may reduce complications but do not prevent neurodegeneration. The 2021 investigators specifically suggested that the recurrent allele’s frequency could support screening-based early carrier detection in some populations. (ghosh2021arelativelycommon pages 6-7)

## 14. Other species and natural disease

TRAPPC4 is evolutionarily conserved; its yeast ortholog is **Trs23**. No naturally occurring companion-animal, livestock, or wildlife disorder definitively homologous to human NEDESBA was identified, and there is no zoonotic or cross-species transmission. Relevant taxa for experimental work include *Homo sapiens* (NCBI Taxon 9606), *Mus musculus* (10090), and *Saccharomyces cerevisiae* (4932). Breed-specific VBO annotation is not applicable. (hall2024trappopathiesseveremultisystem pages 7-9, bergen2020deficienciesinvesicular pages 1-2)

## 15. Model organisms and experimental systems

### Direct disease models

- **Patient fibroblasts:** reproduce reduced TRAPPC4, impaired TRAPP assembly/stability, delayed Golgi trafficking, and defective autophagic flux. Wild-type TRAPPC4 rescue establishes causal specificity.
- **Yeast trs23 temperature-sensitive model:** shows constitutive/stress-induced autophagy defects and temperature-dependent secretory defects, validating conserved function.
- **Mouse knockout:** complete loss is embryonic lethal, demonstrating essentiality but limiting its utility as a postnatal disease model. A hypomorphic or conditional neural model would be more appropriate. (hall2024trappopathiesseveremultisystem pages 7-9, bergen2020deficienciesinvesicular pages 1-2)

The 2024 review emphasized that disease-specific neurological modeling remained limited to fibroblasts and yeast. Neuronal iPSC lines, brain organoids, conditional/hypomorphic mice, and zebrafish would enable study of cell-type vulnerability, developmental timing, electrophysiology, and therapeutic rescue, but published NEDESBA-specific validation was not available through 2024. Data from other TRAPP-gene models may illuminate shared biology but cannot be assumed to reproduce TRAPPC4 disease. (hall2024trappopathiesseveremultisystem pages 7-9)

## Recent developments and expert assessment

The principal 2023–2024 developments were continued recognition of TRAPPC4 within the broader TRAPPopathy spectrum, clinical reports expanding muscle and radiologic findings, and the December 2024 review’s synthesis of additional missense variants and major research gaps. The expert consensus remains that TRAPP complexes regulate ER–Golgi/plasma-membrane traffic and autophagy, but the reasons particular subunits produce distinct neurological, muscular, or skeletal phenotypes are unresolved. For TRAPPC4 specifically, neuronal models, prospective natural-history cohorts, standardized outcomes, biomarkers, and preclinical treatment studies are priorities. (hall2024trappopathiesseveremultisystem pages 7-9)

## Key publications

1. **Van Bergen NJ et al.** “Deficiencies in vesicular transport mediated by TRAPPC4 are associated with severe syndromic intellectual disability.” *Brain*. Published 2020; accepted October 7, 2019. **PMID: 31794024.** DOI: https://doi.org/10.1093/brain/awz374. Foundational human cohort and direct trafficking/autophagy experiments. (bergen2020deficienciesinvesicular pages 1-2)
2. **Kaur P et al.** “Recurrent bi-allelic splicing variant c.454+3A>G in TRAPPC4 is associated with progressive encephalopathy and muscle involvement.” *Brain*. 2020. **PMID: 32125366.** DOI: https://doi.org/10.1093/brain/awaa046. Clinical expansion emphasizing muscle involvement. (OpenTargets Search: neurodevelopmental disorder with epilepsy spasticity and brain atrophy-TRAPPC4)
3. **Ghosh SG et al.** “A relatively common homozygous TRAPPC4 splicing variant is associated with an early-infantile neurodegenerative syndrome.” *European Journal of Human Genetics*. Online 2020; volume publication 2021. **PMID: 33011761.** DOI: https://doi.org/10.1038/s41431-020-00717-5. Expanded cohort, carrier frequency, natural history, and RNA-seq. (OpenTargets Search: neurodevelopmental disorder with epilepsy spasticity and brain atrophy-TRAPPC4, ghosh2021arelativelycommon pages 1-2)
4. **Hall R et al.** “TRAPPopathies: Severe Multisystem Disorders Caused by Variants in Genes of the Transport Protein Particle (TRAPP) Complexes.” *International Journal of Molecular Sciences*. December 2024;25:13329. DOI: https://doi.org/10.3390/ijms252413329. Current expert review and research agenda. (hall2024trappopathiesseveremultisystem pages 7-9)

## Evidence limitations

NEDESBA evidence remains dominated by one recurrent allele, small retrospective cohorts, overlapping cases, inconsistent follow-up, and functional studies in non-neuronal fibroblasts and yeast. Frequencies should therefore be interpreted as **reported-cohort frequencies**, not population estimates. No prospective natural-history registry, formal diagnostic guideline, validated biomarker, controlled treatment study, disease-specific quality-of-life instrument, or robust neuronal/animal therapeutic model was identified. Claims concerning newer rare variants should be checked against their primary reports and current ClinVar records before clinical classification.

References

1. (bergen2020deficienciesinvesicular pages 1-2): Nicole J Van Bergen, Yiran Guo, Noraldin Al-Deri, Zhanna Lipatova, Daniela Stanga, Sarah Zhao, Rakhilya Murtazina, Valeriya Gyurkovska, Davut Pehlivan, Tadahiro Mitani, Alper Gezdirici, Jayne Antony, Felicity Collins, Mary J H Willis, Zeynep H Coban Akdemir, Pengfei Liu, Jaya Punetha, Jill V Hunter, Shalini N Jhangiani, Jawid M Fatih, Jill A Rosenfeld, Jennifer E Posey, Richard A Gibbs, Ender Karaca, Sean Massey, Thisara G Ranasinghe, Patrick Sleiman, Chris Troedson, James R Lupski, Michael Sacher, Nava Segev, Hakon Hakonarson, and John Christodoulou. Deficiencies in vesicular transport mediated by trappc4 are associated with severe syndromic intellectual disability. Brain : a journal of neurology, 143:112-130, Dec 2020. URL: https://doi.org/10.1093/brain/awz374, doi:10.1093/brain/awz374. This article has 58 citations.

2. (ghosh2021arelativelycommon pages 1-2): Shereen G. Ghosh, Marcello Scala, Christian Beetz, Guy Helman, Valentina Stanley, Xiaoxu Yang, Martin W. Breuss, Neda Mazaheri, Laila Selim, Fatemeh Hadipour, Lynn Pais, Chloe A. Stutterd, Vasiliki Karageorgou, Amber Begtrup, Amy Crunk, Jane Juusola, Rebecca Willaert, Leigh A. Flore, Kelly Kennelly, Christopher Spencer, Martha Brown, Pamela Trapane, Anna C. E. Hurst, S. Lane Rutledge, Dana H. Goodloe, Marie T. McDonald, Vandana Shashi, Kelly Schoch, Hoda Tomoum, Raghda Zaitoun, Zahra Hadipour, Hamid Galehdari, Alistair T. Pagnamenta, Majid Mojarrad, Alireza Sedaghat, Patrícia Dias, Sofia Quintas, Atiyeh Eslahi, Gholamreza Shariati, Peter Bauer, Cas Simons, Henry Houlden, Mahmoud Y. Issa, Maha S. Zaki, Reza Maroofian, and Joseph G. Gleeson. A relatively common homozygous trappc4 splicing variant is associated with an early-infantile neurodegenerative syndrome. European Journal of Human Genetics, 29:271-279, Sep 2021. URL: https://doi.org/10.1038/s41431-020-00717-5, doi:10.1038/s41431-020-00717-5. This article has 24 citations and is from a domain leading peer-reviewed journal.

3. (hall2024trappopathiesseveremultisystem pages 7-9): Riley Hall, Vallari Sawant, Jinchao Gu, Tim Sikora, Ben Rollo, Silvia Velasco, Jinkuk Kim, Nava Segev, John Christodoulou, and Nicole J. Van Bergen. Trappopathies: severe multisystem disorders caused by variants in genes of the transport protein particle (trapp) complexes. International Journal of Molecular Sciences, 25:13329, Dec 2024. URL: https://doi.org/10.3390/ijms252413329, doi:10.3390/ijms252413329. This article has 9 citations.

4. (forno2025childneurologytrappc4related pages 1-2): Andreia Forno, Joana Oliveira, Marta Zegre Amorim, Carla Conceição, and Paulo Rego Sousa. Child neurology: trappc4-related neurodevelopmental disorder. May 2025. URL: https://doi.org/10.1212/wnl.0000000000213538, doi:10.1212/wnl.0000000000213538. This article has 1 citations and is from a highest quality peer-reviewed journal.

5. (ghosh2021arelativelycommon pages 2-3): Shereen G. Ghosh, Marcello Scala, Christian Beetz, Guy Helman, Valentina Stanley, Xiaoxu Yang, Martin W. Breuss, Neda Mazaheri, Laila Selim, Fatemeh Hadipour, Lynn Pais, Chloe A. Stutterd, Vasiliki Karageorgou, Amber Begtrup, Amy Crunk, Jane Juusola, Rebecca Willaert, Leigh A. Flore, Kelly Kennelly, Christopher Spencer, Martha Brown, Pamela Trapane, Anna C. E. Hurst, S. Lane Rutledge, Dana H. Goodloe, Marie T. McDonald, Vandana Shashi, Kelly Schoch, Hoda Tomoum, Raghda Zaitoun, Zahra Hadipour, Hamid Galehdari, Alistair T. Pagnamenta, Majid Mojarrad, Alireza Sedaghat, Patrícia Dias, Sofia Quintas, Atiyeh Eslahi, Gholamreza Shariati, Peter Bauer, Cas Simons, Henry Houlden, Mahmoud Y. Issa, Maha S. Zaki, Reza Maroofian, and Joseph G. Gleeson. A relatively common homozygous trappc4 splicing variant is associated with an early-infantile neurodegenerative syndrome. European Journal of Human Genetics, 29:271-279, Sep 2021. URL: https://doi.org/10.1038/s41431-020-00717-5, doi:10.1038/s41431-020-00717-5. This article has 24 citations and is from a domain leading peer-reviewed journal.

6. (bergen2020deficienciesinvesicular pages 2-3): Nicole J Van Bergen, Yiran Guo, Noraldin Al-Deri, Zhanna Lipatova, Daniela Stanga, Sarah Zhao, Rakhilya Murtazina, Valeriya Gyurkovska, Davut Pehlivan, Tadahiro Mitani, Alper Gezdirici, Jayne Antony, Felicity Collins, Mary J H Willis, Zeynep H Coban Akdemir, Pengfei Liu, Jaya Punetha, Jill V Hunter, Shalini N Jhangiani, Jawid M Fatih, Jill A Rosenfeld, Jennifer E Posey, Richard A Gibbs, Ender Karaca, Sean Massey, Thisara G Ranasinghe, Patrick Sleiman, Chris Troedson, James R Lupski, Michael Sacher, Nava Segev, Hakon Hakonarson, and John Christodoulou. Deficiencies in vesicular transport mediated by trappc4 are associated with severe syndromic intellectual disability. Brain : a journal of neurology, 143:112-130, Dec 2020. URL: https://doi.org/10.1093/brain/awz374, doi:10.1093/brain/awz374. This article has 58 citations.

7. (OpenTargets Search: neurodevelopmental disorder with epilepsy spasticity and brain atrophy-TRAPPC4): Open Targets Query (neurodevelopmental disorder with epilepsy spasticity and brain atrophy-TRAPPC4, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

8. (ghosh2021arelativelycommon pages 4-6): Shereen G. Ghosh, Marcello Scala, Christian Beetz, Guy Helman, Valentina Stanley, Xiaoxu Yang, Martin W. Breuss, Neda Mazaheri, Laila Selim, Fatemeh Hadipour, Lynn Pais, Chloe A. Stutterd, Vasiliki Karageorgou, Amber Begtrup, Amy Crunk, Jane Juusola, Rebecca Willaert, Leigh A. Flore, Kelly Kennelly, Christopher Spencer, Martha Brown, Pamela Trapane, Anna C. E. Hurst, S. Lane Rutledge, Dana H. Goodloe, Marie T. McDonald, Vandana Shashi, Kelly Schoch, Hoda Tomoum, Raghda Zaitoun, Zahra Hadipour, Hamid Galehdari, Alistair T. Pagnamenta, Majid Mojarrad, Alireza Sedaghat, Patrícia Dias, Sofia Quintas, Atiyeh Eslahi, Gholamreza Shariati, Peter Bauer, Cas Simons, Henry Houlden, Mahmoud Y. Issa, Maha S. Zaki, Reza Maroofian, and Joseph G. Gleeson. A relatively common homozygous trappc4 splicing variant is associated with an early-infantile neurodegenerative syndrome. European Journal of Human Genetics, 29:271-279, Sep 2021. URL: https://doi.org/10.1038/s41431-020-00717-5, doi:10.1038/s41431-020-00717-5. This article has 24 citations and is from a domain leading peer-reviewed journal.

9. (ghosh2021arelativelycommon pages 6-7): Shereen G. Ghosh, Marcello Scala, Christian Beetz, Guy Helman, Valentina Stanley, Xiaoxu Yang, Martin W. Breuss, Neda Mazaheri, Laila Selim, Fatemeh Hadipour, Lynn Pais, Chloe A. Stutterd, Vasiliki Karageorgou, Amber Begtrup, Amy Crunk, Jane Juusola, Rebecca Willaert, Leigh A. Flore, Kelly Kennelly, Christopher Spencer, Martha Brown, Pamela Trapane, Anna C. E. Hurst, S. Lane Rutledge, Dana H. Goodloe, Marie T. McDonald, Vandana Shashi, Kelly Schoch, Hoda Tomoum, Raghda Zaitoun, Zahra Hadipour, Hamid Galehdari, Alistair T. Pagnamenta, Majid Mojarrad, Alireza Sedaghat, Patrícia Dias, Sofia Quintas, Atiyeh Eslahi, Gholamreza Shariati, Peter Bauer, Cas Simons, Henry Houlden, Mahmoud Y. Issa, Maha S. Zaki, Reza Maroofian, and Joseph G. Gleeson. A relatively common homozygous trappc4 splicing variant is associated with an early-infantile neurodegenerative syndrome. European Journal of Human Genetics, 29:271-279, Sep 2021. URL: https://doi.org/10.1038/s41431-020-00717-5, doi:10.1038/s41431-020-00717-5. This article has 24 citations and is from a domain leading peer-reviewed journal.

10. (bergen2020deficienciesinvesicular pages 15-16): Nicole J Van Bergen, Yiran Guo, Noraldin Al-Deri, Zhanna Lipatova, Daniela Stanga, Sarah Zhao, Rakhilya Murtazina, Valeriya Gyurkovska, Davut Pehlivan, Tadahiro Mitani, Alper Gezdirici, Jayne Antony, Felicity Collins, Mary J H Willis, Zeynep H Coban Akdemir, Pengfei Liu, Jaya Punetha, Jill V Hunter, Shalini N Jhangiani, Jawid M Fatih, Jill A Rosenfeld, Jennifer E Posey, Richard A Gibbs, Ender Karaca, Sean Massey, Thisara G Ranasinghe, Patrick Sleiman, Chris Troedson, James R Lupski, Michael Sacher, Nava Segev, Hakon Hakonarson, and John Christodoulou. Deficiencies in vesicular transport mediated by trappc4 are associated with severe syndromic intellectual disability. Brain : a journal of neurology, 143:112-130, Dec 2020. URL: https://doi.org/10.1093/brain/awz374, doi:10.1093/brain/awz374. This article has 58 citations.

11. (forno2025childneurologytrappc4related pages 2-4): Andreia Forno, Joana Oliveira, Marta Zegre Amorim, Carla Conceição, and Paulo Rego Sousa. Child neurology: trappc4-related neurodevelopmental disorder. May 2025. URL: https://doi.org/10.1212/wnl.0000000000213538, doi:10.1212/wnl.0000000000213538. This article has 1 citations and is from a highest quality peer-reviewed journal.

12. (bergen2020deficienciesinvesicular pages 16-17): Nicole J Van Bergen, Yiran Guo, Noraldin Al-Deri, Zhanna Lipatova, Daniela Stanga, Sarah Zhao, Rakhilya Murtazina, Valeriya Gyurkovska, Davut Pehlivan, Tadahiro Mitani, Alper Gezdirici, Jayne Antony, Felicity Collins, Mary J H Willis, Zeynep H Coban Akdemir, Pengfei Liu, Jaya Punetha, Jill V Hunter, Shalini N Jhangiani, Jawid M Fatih, Jill A Rosenfeld, Jennifer E Posey, Richard A Gibbs, Ender Karaca, Sean Massey, Thisara G Ranasinghe, Patrick Sleiman, Chris Troedson, James R Lupski, Michael Sacher, Nava Segev, Hakon Hakonarson, and John Christodoulou. Deficiencies in vesicular transport mediated by trappc4 are associated with severe syndromic intellectual disability. Brain : a journal of neurology, 143:112-130, Dec 2020. URL: https://doi.org/10.1093/brain/awz374, doi:10.1093/brain/awz374. This article has 58 citations.

## Artifacts

- [Edison artifact artifact-00](Neurodevelopmental_Disorder_with_Epilepsy_Spasticity_and_Brain_Atrophy-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |

All extracted references resolved successfully.