---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-26T22:11:15.281558'
end_time: '2026-08-26T22:20:46.437192'
duration_seconds: 571.16
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Congenital Primary Megaureter
  mondo_id: ''
  category: Congenital
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 26
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 2
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Congenital_Primary_Megaureter-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Primary Megaureter
- **MONDO ID:**  (if available)
- **Category:** Congenital

## Research Objectives

Please provide a comprehensive research report on **Congenital Primary Megaureter** covering all of the
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
- **Disease Name:** Congenital Primary Megaureter
- **MONDO ID:**  (if available)
- **Category:** Congenital

## Research Objectives

Please provide a comprehensive research report on **Congenital Primary Megaureter** covering all of the
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


# Congenital Primary Megaureter: Comprehensive Disease-Characteristics Report

## Executive summary

Congenital primary megaureter is a congenital anomaly of the kidney and urinary tract (CAKUT) in which the ureter is abnormally enlarged—generally **>7–8 mm** in a child—without an acquired cause. “Megaureter” is an imaging description, not a complete etiologic diagnosis. Cases must be classified by the presence or absence of vesicoureteral reflux (VUR) and obstruction. The best-characterized disease subtype is **primary obstructive megaureter (POM)**, also called primary non-refluxing obstructive megaureter, caused by a short adynamic or aperistaltic distal ureteral segment at the ureterovesical junction (UVJ). (boswell2024advancementsinsurgical pages 1-2, aiello2022efficacyandsafety pages 1-2)

Most prenatally detected POMs are initially observed because approximately **70–80%** improve or resolve without surgery. Intervention is reserved for febrile/recurrent urinary infection, pain or stones, progressive hydroureteronephrosis, renal-parenchymal thinning, or declining differential renal function. The principal recent development is increasing use of endoscopic high-pressure balloon dilation; however, the evidence remains dominated by retrospective, single-center series rather than randomized trials. (ortiz2018longtermoutcomesin pages 1-2, boswell2024advancementsinsurgical pages 1-2, boswell2024advancementsinsurgical pages 2-4, aiello2022efficacyandsafety pages 1-2)

The following table provides a compact ontology-ready summary; suggested ontology terms should be verified against the current releases before database ingestion.

| Domain | Knowledge-base statement | Quantitative evidence | Suggested ontology terms/IDs | Evidence level or caveat |
|---|---|---|---|---|
| Definition / classification | Congenital primary megaureter is a pediatric imaging-defined ureteral dilatation, usually >7–8 mm, that must be etiologically classified; the key primary subtype for this entry is primary obstructive/non-refluxing megaureter (POM), i.e., distal ureterovesical junction obstruction without vesicoureteral reflux. | Diameter threshold: >7–8 mm; classified by reflux present/absent and obstruction present/absent. | Candidate terms for curator verification: MONDO primary megaureter/congenital megaureter; MeSH megaureter; UBERON ureter, ureterovesical junction; HPO Hydroureter, Hydronephrosis | Strong review-level synthesis plus primary series; nomenclature varies across sources (primary obstructive, primary non-refluxing, congenital obstructive megaureter). (boswell2024advancementsinsurgical pages 1-2, aiello2022efficacyandsafety pages 1-2) |
| Data provenance | Most disease information is aggregated from disease-level reviews, retrospective pediatric cohorts, and registry studies rather than EHR-derived large population datasets. | No unified disease registry prevalence estimate identified. | Evidence model tags: human clinical; retrospective cohort; review; registry | Important for KB curation because many statements are from specialty-center series, not population-wide surveillance. (ortiz2018longtermoutcomesin pages 1-2, boswell2024advancementsinsurgical pages 1-2, NCT05639283 chunk 1) |
| Core phenotype | Typical phenotype is hydroureteronephrosis detected antenatally or in infancy/early childhood; diagnosis often follows prenatal ultrasound showing urinary tract dilatation. | CAKUT overall detectable on fetal ultrasonography; POM accessible to antenatal screening from second trimester; primary megaureter cited as 5–10% of prenatal hydronephrosis cases in one review/case-based synthesis. | HPO candidate terms: Antenatal hydronephrosis; Hydroureter; Hydronephrosis; Abnormal urinary system imaging finding | Direct disease-specific prenatal detection supported; 5–10% figure comes from later review/case literature and should be curator-verified before hard-coding. (NCT05639283 chunk 1, shrateh2025bilateralprimarynonrefluxing pages 2-5) |
| Principal clinical phenotypes | Common manifestations include urinary tract infection, progressive hydronephrosis/hydroureter, flank/loin pain, hematuria, nephrolithiasis, and loss of renal function in a subset; many infants remain asymptomatic under surveillance. | In one 79-POM surgical cohort, indications combined worsening hydroureteronephrosis with UTI, parenchymal thinning, and/or impaired differential renal function; in a small 11-case mixed megaureter series, febrile UTI occurred in 63.64% and lower back pain in 45.45%. | HPO candidate terms: Urinary tract infection; Flank pain; Hematuria; Nephrolithiasis; Decreased renal function; Renal parenchymal thinning | Symptom frequencies are highly cohort-dependent and enriched for referred/surgical patients. (ortiz2018longtermoutcomesin pages 1-2, morsoUnknownyearsupervidedbypr. pages 90-96, cayon2024comparativestudyof pages 1-2) |
| Anatomy affected | Primary organs: ureter and kidney collecting system; the lesion localizes to the distal/terminal ureter at the ureterovesical junction, with secondary impact on renal pelvis/calyces and renal parenchyma. | Distal obstructive/adynamic segment reported as short; one source notes 0.5–4 cm aperistaltic segment. | UBERON candidate terms: ureter; distal ureter; ureterovesical junction; renal pelvis; kidney; urinary system | Disease-specific localization is consistent across reviews and cohorts. (isac2025predictivefactorsfor pages 1-2, boswell2024advancementsinsurgical pages 1-2, NCT05639283 chunk 1) |
| Tissue / cell level | Pathology centers on distal ureteral smooth-muscle and extracellular-matrix abnormality, with functional aperistalsis/adynamia. | Histologic themes: focal muscle-fiber deficiency, proximal muscular hypertrophy, abnormal circular-fiber predominance, collagen infiltration/fibrosis. | CL candidate terms: smooth muscle cell; fibroblast; urothelial cell. GO candidate terms: smooth muscle contraction; extracellular matrix organization; collagen fibril organization; peristalsis | Mechanistic evidence is mainly histopathology and review synthesis, not modern single-cell data. (isac2025predictivefactorsfor pages 1-2, morsoUnknownyearsupervidedbypr. pages 29-32, NCT05639283 chunk 1, aiello2022efficacyandsafety pages 1-2) |
| Mechanism / causal chain | Proposed chain: congenital distal ureteral smooth-muscle differentiation defect → adynamic/aperistaltic UVJ segment → functional urinary outflow obstruction → upstream hydroureteronephrosis/tortuosity and stasis → infection, renal parenchymal thinning/scarring, and possible renal function decline. Spontaneous improvement likely reflects maturation of distal ureteral function over time. | Spontaneous resolution estimated around 72–80% in observational/review literature; maturation may continue for the first years of life. | GO candidate terms: smooth muscle cell differentiation; ureteral peristalsis; response to mechanical stress; fibrosis; kidney development | Disease-specific mechanism is plausible and repeatedly cited, but molecular drivers remain insufficiently defined. (boswell2024advancementsinsurgical pages 1-2, aiello2022efficacyandsafety pages 1-2, isac2025predictivefactorsfor pages 1-2, NCT05639283 chunk 1) |
| Laterality / demographics | Male predominance is typical; unilateral disease is more common, but bilateral involvement is well recognized. | Trial synopsis: affects four times more boys than girls; bilateral in 25%; contralateral renal dysplasia in 15%. Older summary: bilateral in ~25%, contralateral absence/dysplasia 10–15%. | HPO candidate terms: Bilateral hydroureter; Unilateral hydroureter; Renal dysplasia | These proportions derive from specialty literature and registry synopsis rather than population registries. (NCT05639283 chunk 1, morsoUnknownyearsupervidedbypr. pages 29-32) |
| Natural history | Most primary non-refluxing/obstructive megaureters improve or resolve without surgery, usually with gradual proximal-to-distal reduction in dilatation. A minority progress and require intervention. | Historic prenatal cohort: spontaneous resolution in 72% at mean >2 years; prospective data summarized in 2024 review: ureter <10 mm had 76% resolution over median 5 years vs 17% for ≥10 mm over median 9 years; 2025 conservative cohort: 57% spontaneous resolution at median 45.75 months. | HPO candidate terms: Spontaneous resolution; Persistent hydroureter; Progressive hydronephrosis | Natural-history estimates differ by inclusion criteria and era; 2025 cohort is newer but small and outside requested 2023–2024 priority window. (boswell2024advancementsinsurgical pages 1-2, isac2025predictivefactorsfor pages 1-2, isac2025predictivefactorsfor pages 10-12) |
| Prognostic / resolution predictors | Worse spontaneous-resolution likelihood is associated with greater hydronephrosis severity and larger ureteral diameter. | Predictors cited: SFU grade 3–4 hydronephrosis and ureter diameter >13 mm; <10 mm vs ≥10 mm ureter threshold associated with 76% vs 17% resolution in one prospective study; 2025 cohort found hydronephrosis grade significant (p=0.046). | HPO candidate terms: Severe hydronephrosis; Enlarged ureter | Good candidate features for prognostic annotations; external validation remains limited. (boswell2024advancementsinsurgical pages 1-2, isac2025predictivefactorsfor pages 10-12) |
| Diagnostics: ultrasound | Serial renal/bladder ultrasound is the backbone of diagnosis and follow-up, measuring pelvis/calyces/distal ureter diameter and renal parenchyma. | Example surveillance in one cohort: at birth, 1 month, then every 3 months during conservative follow-up; after EBD, US at 3, 6, 12, and 18 months then annually. | LOINC/RadLex candidate terms: renal/bladder ultrasound; UBERON kidney/ureter/bladder; HPO renal pelvis dilatation | Strong real-world use; exact protocols vary by center. (ortiz2018longtermoutcomesin pages 1-2, ortiz2018longtermoutcomesin pages 4-5, boswell2024advancementsinsurgical pages 1-2) |
| Diagnostics: VCUG | Voiding cystourethrography is used early to exclude reflux and secondary causes; absence of reflux plus significant ureteral dilation supports POM. | Postoperative VCUG in one EBD cohort was reserved for UTI or persistent dilatation without renographic obstruction. | Candidate terms: VCUG; HPO Vesicoureteral reflux (for exclusion); UBERON bladder/urethra | Essential differential test; reflux does not absolutely exclude obstructive component in mixed/ORM cases. (boswell2024advancementsinsurgical pages 1-2, ortiz2018longtermoutcomesin pages 4-5) |
| Diagnostics: MAG-3 renography | Diuretic renography helps assess obstruction and split renal function, but delayed washout alone should not automatically trigger surgery in an asymptomatic stable child. | Obstruction threshold in one cohort: T1/2 >20 min after furosemide; BAPU criteria summarized in 2024 review: initial DRF <40% or DRF drop ≥5% on serial scans support surgery. | Candidate terms: MAG-3 renogram; Differential renal function; Obstructive washout pattern | Important caveat: washout curves are error-prone in tortuous dilated ureters and practice varies because of radiation/cost/catheterization burden. (ortiz2018longtermoutcomesin pages 1-2, boswell2024advancementsinsurgical pages 1-2, boswell2024advancementsinsurgical pages 2-4) |
| Differential diagnosis | Secondary megaureter causes must be ruled out, including posterior urethral valves, neurogenic bladder, and other bladder outlet/voiding disorders; obstructed refluxing megaureter also exists. | No single quantitative differential metric identified. | Candidate terms: posterior urethral valves; neurogenic bladder; secondary megaureter; obstructed refluxing megaureter | Diagnosis is etiologic exclusion plus imaging pattern recognition. (boswell2024advancementsinsurgical pages 1-2) |
| Conservative management | Observation is first-line for most cases; some centers use low-dose antibiotic prophylaxis during infancy/surveillance, but broader hydronephrosis literature indicates prophylaxis benefit remains controversial and should be individualized. | One POM cohort used low-dose antibiotic prophylaxis during conservative surveillance and usually stopped it by 6 months after adequate postoperative drainage; broader 2024 hydronephrosis review: CAP benefit remains controversial. | NCIT candidate interventions: Active surveillance; Antibiotic prophylaxis | Disease-specific randomized evidence for prophylaxis is lacking. (ortiz2018longtermoutcomesin pages 1-2, ortiz2018longtermoutcomesin pages 4-5) |
| Operative criteria | Intervention is generally reserved for worsening hydroureteronephrosis plus clinical or functional deterioration: febrile/recurrent UTI, pain, stones, hematuria, declining DRF, marked progressive dilation, or parenchymal thinning. | In 79 operated POMs: worsening UHN+UTI 38%; worsening UHN+parenchymal thinning 36.7%; worsening UHN+DRF impairment 17.7%; all three 7.6%. | HPO candidate terms: Progressive hydronephrosis; Recurrent urinary tract infections; Renal function decline. NCIT candidate: Surgical indication | These frequencies reflect reasons for surgery among selected operated patients, not disease prevalence. (ortiz2018longtermoutcomesin pages 1-2, aiello2022efficacyandsafety pages 1-2, cayon2024comparativestudyof pages 1-2) |
| Standard surgery | Traditional gold standard is distal ureteral reimplantation/ureteroneocystostomy, with or without tapering/tailoring/remodeling. | Reported success for open reimplantation ± tapering: ~90–95% or 90–96%. | NCIT candidate interventions: Ureteral reimplantation; Ureteroneocystostomy; Ureteroplasty/tapering | High success but greater technical complexity and morbidity in infants with very dilated ureters and small bladders. (ortiz2018longtermoutcomesin pages 4-5, aiello2022efficacyandsafety pages 1-2, boswell2024advancementsinsurgical pages 2-4) |
| Endoscopic balloon dilation (EBD/HPBD) | High-pressure balloon dilation of the UVJ has become a major minimally invasive treatment option for POM and can be definitive in many infants/children. | Systematic review: success 69–100%, may avoid surgery in up to 77%, complications 0–50% mostly infectious or stent-related; 100-case long-term series: success 87.3%, secondary VUR 21.5%, re-stenosis 12.2%, reimplantation needed in 12.7%, mean follow-up 6.4±3.8 years. | NCIT candidate interventions: Endoscopic balloon dilation; Ureteral stent placement; Endoscopic injection for VUR | Evidence is largely retrospective single-center and heterogeneous; still probably the most important recent real-world shift. (aiello2022efficacyandsafety pages 1-2, ortiz2018longtermoutcomesin pages 1-2, ortiz2018longtermoutcomesin pages 7-8, boswell2024advancementsinsurgical pages 2-4) |
| Recent 2024 procedural development | Some centers now perform POM balloon dilation under cystoscopic control alone, omitting fluoroscopy to reduce ionizing radiation. | Comparative 2024 study (23 patients): hospital stay 1 vs 2 days (CS vs RX, p=0.009); OR time 30 vs 78 min (p=0.001); long-term success 100% vs 71%. | NCIT candidate interventions: Radiation-sparing endoscopic balloon dilation; Cystoscopy | Small retrospective study; promising but not definitive. (cayon2024comparativestudyof pages 1-2) |
| Stents / temporizing drainage | Internal stents or cutaneous ureterostomy may be used as temporizing strategies, especially in infants or infection, but stents have notable complication burdens. | Review summary: older stenting literature left about half avoiding surgery after 3–6 months; more recent 35-ureter study showed only 25% avoided subsequent surgery and ~40% had stent-period issues. | NCIT candidate interventions: Ureteral stent placement; Cutaneous ureterostomy; Nephrostomy | Mostly historical/bridging role; not a definitive solution for many patients. (boswell2024advancementsinsurgical pages 2-4) |
| Robotic / laparoscopic surgery | Minimally invasive reconstructive surgery is increasingly reported for selected centers and surgeons, including robotic Lich-Gregoir and other extravesical/transvesicoscopic techniques. | Robotic Lich-Gregoir series: 18 patients, 39% tapered, all improved hydronephrosis over median 2 years; multicenter comparison of 47 laparoscopic vs 48 robotic cases: 94–97% success, 2–4% high-grade complications; single-center robotic vs open: 91–92% success, 8–9% complication rates. | NCIT candidate interventions: Robotic ureteral reimplantation; Laparoscopic ureteral reimplantation | Highly center-dependent learning curve; broad uptake remains limited. (boswell2024advancementsinsurgical pages 4-5) |
| Outcomes / prognosis | Renal drainage and imaging usually improve after successful intervention; long-term prognosis is generally good with preserved renal function when monitored and treated appropriately, but untreated progressive cases risk scarring/function loss. | After EBD: MAG-3 drainage improved from T1/2 >50 min baseline to 9.8±4.5 min post-op (p<0.001); mean DRF 44.4% to 46.2% (p<0.05), with no later deterioration in that series. | HPO candidate terms: Renal scarring; Chronic kidney disease; Preserved renal function | Mortality/life expectancy statistics specific to this disease were not identified. (ortiz2018longtermoutcomesin pages 4-5, NCT05639283 chunk 1) |
| Epidemiology | Primary megaureter is an uncommon congenital urinary tract malformation within CAKUT; disease-specific population prevalence/incidence remains poorly defined. | CAKUT overall affects >1% of live births; clinical-trial synopsis calls congenital obstructive megaureter the second most common cause of hydronephrosis; one older summary cites megaureter as 23% of obstructive uropathy cases. | Candidate terms: CAKUT; congenital urinary tract obstruction | Use caution: most epidemiology is extrapolated from CAKUT/hydronephrosis or tertiary-center series, not dedicated population studies. (mahmoud2024congenitalanomaliesof pages 1-2, NCT05639283 chunk 1, morsoUnknownyearsupervidedbypr. pages 29-32) |
| Genetics / inheritance | No validated disease-specific monogenic cause, recurrent pathogenic variant set, inheritance pattern, penetrance estimate, or ClinGen-style gene-disease curation was identified for congenital primary megaureter itself. | None established from retrieved disease-specific evidence. | Candidate annotation: genetics unknown/heterogeneous; broader CAKUT genes for separate curation only (e.g., PAX2, TBX18, SIX2, BMP4 in CAKUT context) | Important negative finding: do not over-attribute broad CAKUT genes to primary megaureter without direct evidence. (mahmoud2024congenitalanomaliesof pages 1-2) |
| Environmental / protective factors | No disease-specific environmental risk factor, protective factor, or gene-environment interaction was identified for primary megaureter. Broader CAKUT literature implicates maternal diabetes, obesity, malnutrition, alcohol, and nephrotoxic medications in urinary tract maldevelopment generally. | None disease-specific. | Candidate annotation: environmental evidence unavailable for disease-specific entry | Keep separate from generic CAKUT etiologic risk factors. (mahmoud2024congenitalanomaliesof pages 1-2) |
| Molecular profiling / epigenetics | No validated disease-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial, or epigenetic biomarker set was identified in the retrieved evidence. | Not available. | Candidate annotation: no omics signature established | Useful KB gap statement. (isac2025predictivefactorsfor pages 1-2, mahmoud2024congenitalanomaliesof pages 1-2) |
| Other species / model organisms | No validated natural veterinary disease model or dedicated model-organism system for primary congenital megaureter was identified in retrieved evidence. | Not available. | Candidate annotation: model organism unavailable/not established | Absence of evidence from targeted search; curator may revisit specialist databases separately. (isac2025predictivefactorsfor pages 1-2) |
| Clinical trials / current research | Interventional trial activity is sparse; one relevant completed observational registry-style study is POMME. Current research focus is on optimizing selection for observation vs minimally invasive intervention and comparing endoscopic with reconstructive approaches. | POMME / NCT05639283: completed retrospective observational study, enrollment 120, University Hospital Strasbourg; no relevant gene/cell/RNA/drug trials found. | Trial IDs: NCT05639283; candidate evidence tags: observational registry, real-world study | Supports statement that management advances are procedural rather than molecular/targeted. (NCT05639283 chunk 1, boswell2024advancementsinsurgical pages 1-2) |


*Table: This table summarizes ontology-ready, disease-specific facts for congenital primary megaureter, emphasizing definition, pathophysiology, natural history, diagnostics, treatment, and key evidence gaps. It is designed to help curate a structured knowledge-base entry while clearly separating direct evidence from broader CAKUT context.*

## 1. Disease information

### Definition and classification

A megaureter is a ureter measuring more than approximately 7–8 mm, usually identified by pediatric ultrasonography. King/Smith-style classification separates it into: (1) refluxing, non-obstructed; (2) obstructed, non-refluxing—POM; (3) refluxing and obstructed; and (4) neither refluxing nor obstructed. Each may be primary or secondary. Primary disease originates in the ureter/UVJ; secondary megaureter results from such conditions as posterior urethral valves, neurogenic bladder, or other high-pressure bladder/outlet disorders. (boswell2024advancementsinsurgical pages 1-2, aiello2022efficacyandsafety pages 1-2)

The 2024 review’s exact abstract wording is: **“Megaureter management first relies on determining the underlying cause, whether by obstruction, reflux, or a combination.”** This is clinically important because treatment of reflux alone can miss a coexisting obstructive component. (boswell2024advancementsinsurgical pages 1-2)

### Names and identifiers

Common names include **congenital megaureter**, **primary megaureter**, **primary obstructive megaureter**, **primary non-refluxing megaureter**, **primary non-refluxing obstructive megaureter**, **congenital obstructive megaureter**, and **functional UVJ obstruction**. “Primary non-refluxing megaureter” is sometimes used as a broader observational cohort label and may include obstructed and non-obstructed units.

No confidently disease-specific OMIM, Orphanet, or MONDO identifier was established in the retrieved authoritative material. A current ontology lookup should therefore be performed before assigning a code; do not substitute a generic hydronephrosis or CAKUT identifier. The relevant ClinicalTrials.gov record maps the condition to MeSH **Hydronephrosis, D006869**, but this is broader than POM. ICD coding is likewise generally under congenital obstructive defects of the renal pelvis/ureter or other congenital urinary malformations rather than a uniquely validated POM code. (NCT05639283 chunk 1)

### Data provenance

The evidence is aggregated at disease level from reviews, retrospective pediatric-urology cohorts, imaging follow-up studies, and a small number of prospective observational cohorts. It is not principally based on individual longitudinal EHR records or a population-wide disease registry. This limits precise prevalence and phenotype-frequency estimates.

## 2. Etiology and risk or protective factors

### Direct disease mechanism

POM is attributed to abnormal development or maturation of the terminal ureter, producing an adynamic/aperistaltic segment and functional obstruction at the UVJ. Histologic descriptions include focal smooth-muscle deficiency, disproportionate circular-muscle bundles, proximal muscular hypertrophy, collagen infiltration, and increased collagen I/III. Delayed smooth-muscle differentiation may explain why many cases resolve during infancy or early childhood. (isac2025predictivefactorsfor pages 1-2, morsoUnknownyearsupervidedbypr. pages 29-32, NCT05639283 chunk 1, aiello2022efficacyandsafety pages 1-2)

### Genetic factors

No validated single causal gene, recurrent pathogenic variant, inheritance pattern, penetrance estimate, founder allele, or carrier frequency was identified specifically for isolated congenital primary megaureter. Consequently, broad CAKUT genes must not automatically be annotated as causal for this phenotype.

A 2024 CAKUT review lists genes including **PAX2, TBX18, SIX2, BMP4, and NRIP1** and states that monogenic variants may explain up to 20% of CAKUT overall. That evidence applies to the heterogeneous CAKUT spectrum, not specifically to isolated POM. Genetic testing is more defensible when megaureter is bilateral, familial, syndromic, associated with renal dysplasia/agenesis, or accompanied by other congenital anomalies. (mahmoud2024congenitalanomaliesof pages 1-2)

### Environmental, infectious, and lifestyle factors

No toxin, infection, diet, smoking exposure, occupational factor, or lifestyle behavior has been demonstrated as a disease-specific cause of primary megaureter. Maternal diabetes, obesity, malnutrition, alcohol, and medications that disturb renal development have been discussed for CAKUT collectively, but disease-specific effect sizes for POM are unavailable. No established genetic or environmental protective factors or gene–environment interaction has been demonstrated. (mahmoud2024congenitalanomaliesof pages 1-2)

## 3. Phenotypes

The typical onset is prenatal, neonatal, or early childhood. Severity ranges from asymptomatic ureteral dilation to progressive obstructive nephropathy.

* **Hydroureter/megaureter:** congenital imaging sign, usually persistent but often gradually improving. Suggested HPO: *Hydroureter* and *Abnormality of the ureter*.
* **Hydronephrosis/hydroureteronephrosis:** commonly antenatal; severity is variable and is an important prognostic marker. Suggested HPO: *Hydronephrosis* and *Antenatal hydronephrosis*.
* **Urinary tract infection/pyelonephritis:** episodic, usually febrile when clinically consequential; caused by urinary stasis and sometimes postoperative reflux. Suggested HPO: *Recurrent urinary tract infections* and *Pyelonephritis*.
* **Flank, abdominal, or loin pain:** more typical in symptomatic older children or adults; episodic or persistent. Suggested HPO: *Flank pain* and *Abdominal pain*.
* **Hematuria and nephrolithiasis:** less common manifestations and accepted reasons to consider intervention. Suggested HPO: *Hematuria* and *Nephrolithiasis*.
* **Renal-parenchymal thinning, scarring, dysplasia, or reduced renal function:** uncommon but clinically serious downstream manifestations. Suggested HPO: *Renal cortical thinning*, *Renal scarring*, *Renal dysplasia*, and *Decreased renal function*.

In a selected cohort of 79 operated POM units, indications were worsening hydroureteronephrosis with UTI in 38%, parenchymal thinning in 36.7%, impaired differential function in 17.7%, and the combination of UTI plus impaired function in 7.6%. These are **surgical-cohort frequencies**, not prevalence among all affected children. (ortiz2018longtermoutcomesin pages 1-2)

Disease-specific quality-of-life instruments or EQ-5D/SF-36 data were not identified. Most asymptomatic children have little day-to-day impairment but undergo prolonged imaging and infection surveillance; recurrent pyelonephritis, pain, hospitalization, and surgery can materially affect child and family well-being.

## 4. Genetic and molecular information

There is presently insufficient evidence to populate a disease-specific causal-gene or pathogenic-variant table. No robust ClinGen-level gene–disease relationship, pathogenic variant spectrum, allele frequency, somatic event, modifier gene, chromosomal abnormality, or pharmacogenomic association was identified.

Accordingly, routine isolated-POM management is not genotype directed. If genomic testing is clinically indicated because of syndromic or complex CAKUT, chromosomal microarray followed by a CAKUT panel or exome/genome sequencing may be considered under clinical-genetics guidance. Results should be interpreted against the patient’s complete renal and extrarenal phenotype; a variant in a general kidney-development gene is not automatically explanatory for megaureter. Broad CAKUT evidence supports NGS as an adjunct in selected patients, but not as a replacement for functional urinary-tract imaging. (mahmoud2024congenitalanomaliesof pages 1-2)

No disease-specific DNA-methylation signature, histone alteration, chromatin abnormality, or validated epigenetic biomarker is known from the retrieved evidence.

## 5. Environmental information

There is no evidence that postnatal pollution, radiation, occupation, diet, exercise, alcohol, smoking, or infection creates congenital primary megaureter. The malformation is present during fetal urinary-tract development. General maternal CAKUT risks may be recorded as contextual—not POM-specific—evidence. No vaccine or antimicrobial prevention of the congenital lesion is applicable. (mahmoud2024congenitalanomaliesof pages 1-2)

## 6. Mechanism and pathophysiology

### Causal chain

The best-supported disease model is:

**disturbed terminal-ureter smooth-muscle differentiation/maturation → short distal adynamic or aperistaltic segment → impaired antegrade urine transport at the UVJ → proximal ureteral dilation and tortuosity → renal-pelvic/calyceal dilation and urinary stasis → febrile UTI, pressure/mechanical injury, parenchymal thinning or scarring → loss of differential renal function in severe progressive cases.** (isac2025predictivefactorsfor pages 1-2, NCT05639283 chunk 1, aiello2022efficacyandsafety pages 1-2)

Upstream processes are smooth-muscle differentiation, extracellular-matrix organization, and acquisition of coordinated peristalsis. Downstream processes are urinary stasis, infection/inflammation, mechanical distension, fibrosis/scarring, and obstructive nephropathy. The spontaneous-resolution phenotype supports a developmental-maturation mechanism rather than an invariably fixed anatomic stenosis.

Suggested GO annotations include *smooth muscle cell differentiation*, *smooth muscle contraction*, *ureteral peristalsis*, *extracellular matrix organization*, *collagen fibril organization*, *response to mechanical stimulus*, and *fibrotic process*. Candidate Cell Ontology terms include **smooth muscle cell**, **fibroblast**, and **urothelial cell**. These are biologically appropriate annotations but should be mapped to exact current GO/CL identifiers by an ontology curator.

### Molecular profiling gaps

No replicated disease-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, multi-omic, or CRISPR-screen signature was identified. TGF-β and collagen remodeling have been proposed in maturation/fibrosis, but there is not enough evidence to designate a clinically actionable molecular pathway or biomarker. (isac2025predictivefactorsfor pages 1-2)

## 7. Anatomical structures affected

The primary site is the **distal ureter and UVJ**; upstream structures include the remaining ureter, renal pelvis, calyces, renal parenchyma, and occasionally the contralateral urinary tract. Suggested UBERON concepts are ureter, distal ureter, ureterovesical junction, urinary bladder, renal pelvis, kidney, and urinary system.

The relevant tissues are ureteral smooth muscle, extracellular matrix/connective tissue, urothelium, and—secondarily—renal parenchyma. No disease-defining subcellular organelle abnormality is known. Disease is usually unilateral, but approximately **25%** of cases are bilateral; one registry synopsis reports contralateral renal dysplasia in approximately **15%**. Male predominance is marked, with the POMME record describing roughly four times as many boys as girls. (NCT05639283 chunk 1)

## 8. Temporal development and natural history

The lesion is congenital and can be detected by ultrasound from the second trimester. Many affected newborns remain asymptomatic. Resolution is generally gradual and may proceed from proximal to distal ureter as peristaltic function matures. (NCT05639283 chunk 1, boswell2024advancementsinsurgical pages 1-2)

Observational literature reports approximately **72–80% spontaneous improvement/resolution**. A prospective study summarized in the 2024 review found 76% resolution over a median five years when ureteral diameter was <10 mm, versus 17% over a median nine years when diameter was ≥10 mm. Higher SFU hydronephrosis grade and ureteral diameter >13 mm predict a greater likelihood of meeting surgical criteria. (boswell2024advancementsinsurgical pages 1-2, aiello2022efficacyandsafety pages 1-2)

The critical intervention window is not a fixed age. It is defined by emerging febrile infection, progressive dilation or parenchymal thinning, and declining function. Stable asymptomatic dilation—even with delayed renographic washout—does not necessarily represent renal-damaging obstruction. Long-term surveillance is important because resolution may take years and late symptomatic presentation is possible.

## 9. Inheritance and population

Disease-specific population incidence and prevalence per 100,000 are not well established. Primary megaureter has been estimated to account for approximately 5–10% of prenatal hydronephrosis in secondary literature, but this estimate is not equivalent to population prevalence. CAKUT as a whole affects more than 1% of live births and accounts for a large fraction of childhood kidney failure; these broader figures should not be assigned directly to POM. (shrateh2025bilateralprimarynonrefluxing pages 2-5, mahmoud2024congenitalanomaliesof pages 1-2)

Available cohorts consistently indicate male predominance and predominantly unilateral disease, with bilaterality near 25%. No reliable ethnic, geographic, founder, consanguinity, anticipation, germline-mosaicism, or carrier-frequency pattern has been established. (NCT05639283 chunk 1)

## 10. Diagnostics

### Diagnostic pathway

1. **Prenatal/postnatal renal-bladder ultrasonography:** establishes ureteral and collecting-system dilation, tortuosity, debris, renal size, and parenchymal thickness.
2. **VCUG:** evaluates VUR and excludes posterior urethral valves or other lower-tract pathology. Absence of reflux with substantial distal ureteral dilation supports POM, but reflux does not absolutely exclude a mixed obstructive-refluxing megaureter.
3. **MAG-3 diuretic renography:** estimates differential renal function (DRF) and drainage. A T½ >20 minutes has historically been called obstructive, but washout is technically unreliable in a very dilated, tortuous ureter and should not be used alone to mandate surgery.
4. **Urinalysis and urine culture:** indicated with fever or urinary symptoms. Serum creatinine/eGFR is useful in bilateral disease, a solitary kidney, suspected renal failure, or severe obstruction.
5. **CT/MR urography:** not routine in infants; reserved for unclear anatomy, older patients, or suspected secondary causes.

The 2024 expert review cautions that delayed washout alone is not an appropriate operative trigger. More persuasive functional criteria are initial DRF <40% or a serial decline of at least 5%, considered together with symptoms and ultrasound progression. (boswell2024advancementsinsurgical pages 1-2, boswell2024advancementsinsurgical pages 2-4)

One published protocol obtained ultrasound at birth, one month, and every three months during conservative surveillance. After balloon dilation, ultrasound was performed at 3, 6, 12, and 18 months and annually thereafter; MAG-3 scans were obtained at 6 and 18 months. Protocols differ among centers. (ortiz2018longtermoutcomesin pages 1-2, ortiz2018longtermoutcomesin pages 4-5)

### Differential diagnosis

Important exclusions are refluxing megaureter, mixed obstructed-refluxing megaureter, posterior urethral valves, neurogenic or high-pressure bladder, ureterocele/duplicated collecting system, ectopic ureter, UVJ calculus or acquired stricture, retroperitoneal compression, and severe bladder/bowel dysfunction. POM is therefore a clinicoradiologic and functional diagnosis rather than a diagnosis based solely on ureteral diameter.

### Genetic and omics testing

No genetic, circulating, proteomic, metabolomic, epigenomic, or liquid-biopsy test diagnoses isolated POM. CMA, CAKUT panels, WES, or WGS are reserved for selected syndromic, familial, bilateral, or multisystem presentations. Karyotyping, FISH, mitochondrial testing, and repeat-expansion assays have no routine disease-specific role.

## 11. Outcome and prognosis

With observation and timely treatment where needed, prognosis and renal preservation are generally favorable. Disease-specific mortality and reduced life expectancy have not been demonstrated; five- or ten-year survival statistics are therefore not meaningful endpoints. Morbidity derives instead from recurrent pyelonephritis, renal scarring, pain/stones, repeated imaging, stent complications, surgery, and—in severe bilateral or solitary-kidney disease—renal failure. The POMME registry synopsis explicitly identifies repeated pyelonephritis, kidney scarring, and impaired kidney function as clinically relevant risks. (NCT05639283 chunk 1)

After successful endoscopic dilation in a 79-unit long-term cohort, MAG-3 drainage improved from T½ >50 minutes to 9.8±4.5 minutes, mean DRF increased from 44.4% to 46.2%, and no subsequent functional deterioration was observed. Pelvic diameter fell from 19.2 to 5.2 mm and ureteral diameter from 14.9 to 6.6 mm at long-term follow-up. These favorable results are from a selected treated cohort rather than comparative randomized evidence. (ortiz2018longtermoutcomesin pages 4-5)

Poorer prognostic features include high-grade hydronephrosis, large ureteral diameter, progressive parenchymal thinning, recurrent febrile UTI, DRF <40%, and a serial DRF decline ≥5%. No validated molecular prognostic biomarker exists. (boswell2024advancementsinsurgical pages 1-2, boswell2024advancementsinsurgical pages 2-4)

## 12. Treatment

### Observation and supportive treatment

Active surveillance is first-line for most asymptomatic infants with stable renal function. Families should receive fever/UTI education and prompt urine testing for unexplained fever. Low-dose continuous antibiotic prophylaxis is used variably in infancy or high-risk dilation, but its benefit is uncertain and no POM-specific randomized evidence establishes an optimal drug or duration. Suggested NCIT concepts are **Active Surveillance** and **Antibiotic Prophylaxis**. (ortiz2018longtermoutcomesin pages 1-2)

### Indications for intervention

Accepted indications include recurrent/febrile UTI despite appropriate management, pain, stones or hematuria, progressive ureteral/collecting-system dilation, parenchymal thinning, DRF <40%, or a ≥5% fall in DRF. Delayed renographic drainage in an otherwise stable asymptomatic child is insufficient by itself. (boswell2024advancementsinsurgical pages 2-4, aiello2022efficacyandsafety pages 1-2)

### Ureteral reimplantation

Open ureteroneocystostomy with excision of the adynamic distal segment, with or without ureteral tapering/tailoring, remains the traditional definitive operation. Reported success is approximately **90–96%**. It is technically more difficult in infants because a markedly dilated ureter must be implanted into a small bladder; potential complications include secondary obstruction, reflux, bladder dysfunction, and surgical morbidity. Suggested NCIT interventions are **Ureteral Reimplantation**, **Ureteroneocystostomy**, and **Ureteroplasty**. (ortiz2018longtermoutcomesin pages 4-5, aiello2022efficacyandsafety pages 1-2)

### Endoscopic high-pressure balloon dilation

HPBD/EBD dilates the stenotic UVJ, generally followed by temporary ureteral stenting. A 2022 systematic review of 13 retrospective studies reported success rates of **69–100%**, avoidance of open surgery in up to 77%, and complication rates of 0–50%, mainly infection- or stent-related. Its exact abstract conclusion states: **“the overall level of evidence for HPBD is still low and further comparative studies or randomized clinical trials are needed.”** (aiello2022efficacyandsafety pages 1-2)

In the largest long-term series, 100 POM units were treated and 79 with adequate follow-up analyzed. Median operative age was four months, median operating time 20 minutes, and median hospital stay one day. Long-term success was 87.3%; secondary VUR occurred in 21.5%, restenosis in 12.2%, and 12.7% ultimately required reimplantation. Repeat dilation successfully treated 8/9 restenoses, while endoscopic injection treated 13/17 secondary VUR cases. The authors concluded: **“EBD may be considered first-line treatment in POM.”** (ortiz2018longtermoutcomesin pages 1-2, ortiz2018longtermoutcomesin pages 4-5)

### Recent 2024 developments

A 2024 retrospective comparison of 23 children evaluated cystoscopic-only versus radiologically controlled balloon dilation. Cystoscopic-only treatment had shorter operating time (30 versus 78 minutes; p=0.001), shorter hospitalization (one versus two days; p=0.009), and reported long-term success of 100% versus 71%, without more complications. The small, nonrandomized design precludes definitive superiority, but it supports a radiation-sparing implementation. (cayon2024comparativestudyof pages 1-2)

Robotic/laparoscopic reimplantation is increasingly used in specialized centers. Published series report approximately 91–97% success, but patient selection, follow-up, and surgeon learning curves vary. The 2024 expert conclusion is that endoscopic and minimally invasive procedures dominate recent literature but still require collaborative prospective comparison. (boswell2024advancementsinsurgical pages 1-2, boswell2024advancementsinsurgical pages 4-5)

### Temporizing procedures and advanced therapeutics

Nephrostomy, cutaneous ureterostomy, or internal stenting can decompress severe infection, renal failure, solitary-kidney obstruction, or technically difficult infant anatomy. Stents can cause UTI, migration, hematuria, and stones; a review summarized a roughly 40% stent-period problem rate in one longer-term series. (boswell2024advancementsinsurgical pages 2-4)

No gene therapy, cell therapy, RNA therapy, immunotherapy, molecularly targeted drug, or genotype-guided treatment exists. There is no relevant pharmacogenomic guidance.

## 13. Prevention

Primary prevention is not currently possible because no modifiable POM-specific cause has been established. Prenatal ultrasound provides secondary prevention through early recognition, postnatal confirmation, and renal-function surveillance. Tertiary prevention consists of rapid treatment of febrile UTI, monitoring of dilation and DRF, selective prophylactic antibiotics, and timely decompression/reconstruction before irreversible renal injury.

Routine population carrier screening, cascade testing, preimplantation testing, or disease-specific prenatal molecular diagnosis is unsupported because no validated causal gene has been established. Genetic counseling is appropriate when disease is familial, bilateral, syndromic, or associated with additional CAKUT. Vaccination has no disease-specific preventive role.

## 14. Other species and natural disease

No well-validated naturally occurring veterinary counterpart, breed predisposition, VBO annotation, or cross-species transmission issue was identified. The disorder is noninfectious and has no zoonotic potential. Sporadic hydroureter/megaureter may occur in animals as a structural urinary abnormality, but the retrieved evidence was insufficient to equate those cases with human primary congenital megaureter or assign conserved causal genes.

## 15. Model organisms

No dedicated mouse, rat, zebrafish, organoid, iPSC, or other model was identified as a validated model of isolated human POM. Developmental or knockout models that produce hydroureter can inform ureteral smooth-muscle differentiation and urinary-tract morphogenesis, but phenotypic similarity alone does not establish disease equivalence. No model currently supports drug screening or precision therapy for POM. This is a major research gap.

## Clinical trials and current research implementation

The relevant registered study is **POMME, NCT05639283**, a completed French retrospective observational study of 120 children treated for congenital obstructive megaureter. It was designed to identify operability factors rather than test an intervention; the registry was updated December 8, 2023. No relevant randomized drug, device, gene, RNA, or cell-therapy trial was identified. (NCT05639283 chunk 1)

Thus, current real-world innovation is procedural: better selection for surveillance, radiation-sparing endoscopy, HPBD, and laparoscopic/robotic reconstruction. The principal expert concern is evidence quality—heterogeneous definitions, retrospective single-center studies, variable follow-up, and inconsistent definitions of success. (aiello2022efficacyandsafety pages 6-7, boswell2024advancementsinsurgical pages 1-2, boswell2024advancementsinsurgical pages 2-4)

## Key sources and URLs

* Boswell TC. **Advancements in Surgical Management of Megaureters.** *Current Urology Reports*. Published online July 2, 2024. DOI: https://doi.org/10.1007/s11934-024-01214-8. (boswell2024advancementsinsurgical pages 1-2)
* González Cayón J, et al. **Comparative study of cystoscopic control vs. radiological control in the endoscopic treatment of primary obstructive megaureter.** *Cirugía Pediátrica*. January 2024. DOI: https://doi.org/10.54847/cp.2024.01.13. (cayon2024comparativestudyof pages 1-2)
* Aiello G, et al. **Efficacy and safety of high-pressure balloon dilatation for primary obstructive megaureter in children: a systematic review.** *Frontiers in Urology*. November 8, 2022. DOI: https://doi.org/10.3389/fruro.2022.1042689. (aiello2022efficacyandsafety pages 1-2)
* Ortiz R, et al. **Long-Term Outcomes in Primary Obstructive Megaureter Treated by Endoscopic Balloon Dilation: Experience After 100 Cases.** *Frontiers in Pediatrics*. October 5, 2018. DOI: https://doi.org/10.3389/fped.2018.00275. (ortiz2018longtermoutcomesin pages 1-2)
* Mahmoud AH, et al. **Congenital anomalies of the kidney and urinary tract.** *Frontiers in Medicine*. July 15, 2024. DOI: https://doi.org/10.3389/fmed.2024.1384676. This is broader CAKUT evidence, not POM-specific evidence. (mahmoud2024congenitalanomaliesof pages 1-2)
* ClinicalTrials.gov. **POMME—Primary Obstructive Megaureter Management in Eastern Interregional Area.** NCT05639283; registry update December 8, 2023. https://clinicaltrials.gov/study/NCT05639283. (NCT05639283 chunk 1)

## Evidence limitations and curation cautions

The strongest evidence concerns imaging, natural history, and surgery. Disease-specific epidemiology, quality of life, human genetics, molecular profiling, environmental causation, biomarkers, and animal models remain poorly characterized. Exact PMID values were not available in the retrieved records; DOI and registry URLs are therefore supplied rather than guessed. Ontology identifiers beyond directly supported MeSH D006869 should be verified against current HPO, MONDO, UBERON, GO, CL, NCIT, ICD, OMIM, and Orphanet releases before production use.

References

1. (boswell2024advancementsinsurgical pages 1-2): Timothy C. Boswell. Advancements in surgical management of megaureters. Current Urology Reports, 25:215-223, Jul 2024. URL: https://doi.org/10.1007/s11934-024-01214-8, doi:10.1007/s11934-024-01214-8. This article has 10 citations and is from a peer-reviewed journal.

2. (aiello2022efficacyandsafety pages 1-2): Giuseppe Aiello, Alessandro Morlacco, Marta Bianco, Matteo Soligo, Davide Meneghesso, Enrico Vidal, Waifro Rigamonti, and Fabrizio Dal Moro. Efficacy and safety of high-pressure balloon dilatation for primary obstructive megaureter in children: a systematic review. Frontiers in Urology, Nov 2022. URL: https://doi.org/10.3389/fruro.2022.1042689, doi:10.3389/fruro.2022.1042689. This article has 8 citations.

3. (ortiz2018longtermoutcomesin pages 1-2): Ruben Ortiz, Alberto Parente, Laura Perez-Egido, Laura Burgos, and José Maria Angulo. Long-term outcomes in primary obstructive megaureter treated by endoscopic balloon dilation. experience after 100 cases. Frontiers in Pediatrics, Oct 2018. URL: https://doi.org/10.3389/fped.2018.00275, doi:10.3389/fped.2018.00275. This article has 56 citations.

4. (boswell2024advancementsinsurgical pages 2-4): Timothy C. Boswell. Advancements in surgical management of megaureters. Current Urology Reports, 25:215-223, Jul 2024. URL: https://doi.org/10.1007/s11934-024-01214-8, doi:10.1007/s11934-024-01214-8. This article has 10 citations and is from a peer-reviewed journal.

5. (NCT05639283 chunk 1):  Primary Obstructive Megaureter Management in Eastern Interregional Area. University Hospital, Strasbourg, France. 2020. ClinicalTrials.gov Identifier: NCT05639283

6. (shrateh2025bilateralprimarynonrefluxing pages 2-5): Oadi N. Shrateh, Sarah Nafea, Fahad Khan, Fawad Ali, Muhammad Faheem, and Naeem Sheikh. Bilateral primary nonrefluxing unobstructed megaureter in an adult: a case report and review of the literature. Journal of Medical Case Reports, Oct 2025. URL: https://doi.org/10.1186/s13256-025-05603-6, doi:10.1186/s13256-025-05603-6. This article has 3 citations and is from a peer-reviewed journal.

7. (morsoUnknownyearsupervidedbypr. pages 90-96): F MORSO, AA BELKHADEM, and A MEBKHOUT. Supervided by: pr. azzouni ms. Unknown journal, Unknown year.

8. (cayon2024comparativestudyof pages 1-2): J. González Cayón, A. Parente Hernández, A. Ramírez Calazans, V. Vargas Cruz, Á. Escassi Gil, and RM Paredes Esteban. Comparative study of cystoscopic control vs. radiological control in the endoscopic treatment of primary obstructive megaurater. Cirugia pediatrica : organo oficial de la Sociedad Espanola de Cirugia Pediatrica, 37 1:22-26, Jan 2024. URL: https://doi.org/10.54847/cp.2024.01.13, doi:10.54847/cp.2024.01.13. This article has 0 citations.

9. (isac2025predictivefactorsfor pages 1-2): George Vlad Isac and Nicolae Sebastian Ionescu. Predictive factors for spontaneous resolution in primary obstructive megaureter: the impact of hydronephrosis severity on clinical outcomes. Apr 2025. URL: https://doi.org/10.3390/jcm14072463, doi:10.3390/jcm14072463. This article has 4 citations.

10. (morsoUnknownyearsupervidedbypr. pages 29-32): F MORSO, AA BELKHADEM, and A MEBKHOUT. Supervided by: pr. azzouni ms. Unknown journal, Unknown year.

11. (isac2025predictivefactorsfor pages 10-12): George Vlad Isac and Nicolae Sebastian Ionescu. Predictive factors for spontaneous resolution in primary obstructive megaureter: the impact of hydronephrosis severity on clinical outcomes. Apr 2025. URL: https://doi.org/10.3390/jcm14072463, doi:10.3390/jcm14072463. This article has 4 citations.

12. (ortiz2018longtermoutcomesin pages 4-5): Ruben Ortiz, Alberto Parente, Laura Perez-Egido, Laura Burgos, and José Maria Angulo. Long-term outcomes in primary obstructive megaureter treated by endoscopic balloon dilation. experience after 100 cases. Frontiers in Pediatrics, Oct 2018. URL: https://doi.org/10.3389/fped.2018.00275, doi:10.3389/fped.2018.00275. This article has 56 citations.

13. (ortiz2018longtermoutcomesin pages 7-8): Ruben Ortiz, Alberto Parente, Laura Perez-Egido, Laura Burgos, and José Maria Angulo. Long-term outcomes in primary obstructive megaureter treated by endoscopic balloon dilation. experience after 100 cases. Frontiers in Pediatrics, Oct 2018. URL: https://doi.org/10.3389/fped.2018.00275, doi:10.3389/fped.2018.00275. This article has 56 citations.

14. (boswell2024advancementsinsurgical pages 4-5): Timothy C. Boswell. Advancements in surgical management of megaureters. Current Urology Reports, 25:215-223, Jul 2024. URL: https://doi.org/10.1007/s11934-024-01214-8, doi:10.1007/s11934-024-01214-8. This article has 10 citations and is from a peer-reviewed journal.

15. (mahmoud2024congenitalanomaliesof pages 1-2): Anfal Hussain Mahmoud, Iman M. Talaat, Abdelaziz Tlili, and Rifat Hamoudi. Congenital anomalies of the kidney and urinary tract. Jul 2024. URL: https://doi.org/10.3389/fmed.2024.1384676, doi:10.3389/fmed.2024.1384676. This article has 42 citations.

16. (aiello2022efficacyandsafety pages 6-7): Giuseppe Aiello, Alessandro Morlacco, Marta Bianco, Matteo Soligo, Davide Meneghesso, Enrico Vidal, Waifro Rigamonti, and Fabrizio Dal Moro. Efficacy and safety of high-pressure balloon dilatation for primary obstructive megaureter in children: a systematic review. Frontiers in Urology, Nov 2022. URL: https://doi.org/10.3389/fruro.2022.1042689, doi:10.3389/fruro.2022.1042689. This article has 8 citations.

## Artifacts

- [Edison artifact artifact-00](Congenital_Primary_Megaureter-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.