---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-28T16:55:20.956567'
end_time: '2026-08-28T17:05:12.646252'
duration_seconds: 591.69
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Kidney Sarcoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 17
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 26
  verified: 26
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 3
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Kidney_Sarcoma-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Kidney Sarcoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Kidney Sarcoma** covering all of the
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
- **Disease Name:** Kidney Sarcoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Kidney Sarcoma** covering all of the
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


# Kidney Sarcoma: Comprehensive Disease-Characteristics Report

**Evidence cut-off:** December 2024, with emphasis on 2023–2024 literature. **Scope:** “Kidney sarcoma” is an umbrella category rather than one molecular disease. Evidence is dominated by retrospective registries, small series, and extrapolation from histology-matched soft-tissue sarcoma (STS); prospective kidney-sarcoma-specific trials are essentially absent.

## Executive summary

Primary renal sarcomas are malignant mesenchymal tumors arising in the kidney, renal capsule, sinus, vessels, or supporting soft tissue. They must not be conflated with **sarcomatoid renal-cell carcinoma**, an epithelial carcinoma showing mesenchymal-appearing dedifferentiation, or with **clear cell sarcoma of kidney (CCSK)**, a specific pediatric tumor. The strongest contemporary epidemiologic study—1,279 adults in SEER/NCDB, published May 2024—found an age-adjusted incidence of **0.53 per million persons/year**, accounting for **0.25% of renal malignancies**, but encompassing **43 histotypes**. Median overall survival was approximately **25 months**. At presentation, 33.3% were T3, 14.2% T4, and 29.1% metastatic; 81.6% underwent surgery. Histotype, stage, metastasis, necrosis, surgical margin, age, sex, and comorbidity materially affected survival. (uhlig2024epidemiologytreatmentand pages 1-2, uhlig2024epidemiologytreatmentand pages 5-7, uhlig2024epidemiologytreatmentand pages 9-10)

The authoritative interpretation is therefore **histology-first management at a sarcoma reference center**, not uniform treatment as kidney cancer. The 2024 investigators concluded that renal sarcomas “include 43 histiotypes with distinct epidemiology, clinical presentation, outcomes and sensitivity to systemic therapy,” and observed that real-world care frequently followed renal-cancer rather than STS principles. (uhlig2024epidemiologytreatmentand pages 1-2, uhlig2024epidemiologytreatmentand pages 7-9)

## 1. Disease information

### Definition, category, and identifiers

- **Preferred name:** kidney sarcoma; common clinical synonym: **primary renal sarcoma**.
- **Category:** rare malignant mesenchymal neoplasm of the kidney; an anatomic umbrella containing multiple WHO-defined STS histotypes.
- **MONDO:** **MONDO:0002930 — kidney sarcoma**. Open Targets recognizes it as a distinct disease entity. (OpenTargets Search: kidney sarcoma)
- **Related but distinct:** **MONDO:0005006 — clear cell sarcoma of kidney**; **MONDO:0010434 — synovial sarcoma**. (OpenTargets Search: kidney sarcoma)
- **MeSH:** generally indexed through *Sarcoma*, *Kidney Neoplasms*, and the specific histotype; a unique kidney-sarcoma MeSH heading is not consistently used.
- **ICD-10-CM:** no histologically precise single code. Registries commonly combine site **C64.-, malignant neoplasm of kidney except renal pelvis**, with an ICD-O-3 morphology code such as leiomyosarcoma 8890/3, angiosarcoma 9120/3, synovial sarcoma 9040–9043/3, or Ewing sarcoma 9260/3.
- **ICD-11:** coded by malignant kidney site plus morphology/histopathology; local coding systems should retain both dimensions.
- **OMIM/Orphanet:** no single inherited-disorder entry adequately represents the heterogeneous adult umbrella. Individual molecular subtypes may have separate disease records.

**Important exclusions:** Sarcomatoid RCC is not a sarcoma; it can occur in most RCC subtypes, represents about 4% of all RCC but approximately 20% of metastatic RCC, and is WHO/ISUP grade 4. Its biology and checkpoint-based RCC treatment differ from primary renal sarcoma. CCSK is likewise a distinct childhood renal tumor with BCOR-family biology. (OpenTargets Search: kidney sarcoma)

**Evidence provenance:** The principal quantitative evidence is aggregated disease-level registry data, not individual EHR records. SEER and NCDB provide de-identified population/hospital-level observations; case reports and institutional series contribute individual-patient evidence. (uhlig2024epidemiologytreatmentand pages 1-2, uhlig2024epidemiologytreatmentand pages 9-10)

## 2. Etiology, risk, and protective factors

### Causal factors

Most cases are **sporadic cancers caused by acquired somatic alterations**. There is no single causal gene for “kidney sarcoma.” Instead, causal events depend on histotype: SS18::SSX in synovial sarcoma, EWSR1::FLI1 or related ETS fusion in Ewing sarcoma, BCOR internal tandem duplication or YWHAE::NUTM2 in CCSK, and EWSR1::CREB3L1 in sclerosing epithelioid fibrosarcoma. These are generally tumor-defining somatic rearrangements, not inherited alleles. (OpenTargets Search: kidney sarcoma, bradford2020primaryrenalewing pages 7-7, baydar2015primarysclerosingepithelioid pages 12-12)

### Risk factors

- **Age and sex:** these are demographic associations, not proven causes. Adult renal sarcoma had median age about 60 years; renal leiomyosarcoma (LMS) occurred at a median of 62, whereas renal PNET/Ewing-family tumors occurred much younger, around 33 in the registry. LMS was female-predominant (male:female ratio 0.46), while angiosarcoma was male-predominant (3.82). (uhlig2024epidemiologytreatmentand pages 3-5, uhlig2024epidemiologytreatmentand pages 7-9)
- **Ionizing radiation and hereditary cancer predisposition:** recognized general STS risks, but kidney-specific attributable risks have not been quantified in modern cohorts.
- **Smoking, obesity, hepatitis C, asbestos, VHL, Birt–Hogg–Dubé, and hereditary papillary RCC:** these are established or proposed **renal carcinoma** associations and should not be automatically assigned to primary renal sarcoma. A renal-tumor educational review lists them together, but it does not establish histotype-specific causality; this is a key evidence-quality limitation. (mohd2022etiologiesgrossappearance pages 9-10)
- **Infectious causes:** none established for conventional primary renal sarcoma. EBV-associated smooth-muscle tumors may occur under profound immunosuppression, but they are a separate clinicopathologic context.
- **Gene–environment interaction:** no replicated renal-sarcoma-specific G×E interaction has been demonstrated.

### Protective factors

No genetic variant, diet, drug, lifestyle behavior, vaccine, or occupational intervention has been shown specifically to prevent primary renal sarcoma. General avoidance of unnecessary ionizing radiation and tobacco is reasonable health policy but is not evidence-based kidney-sarcoma prophylaxis.

## 3. Phenotypes

Clinical manifestations reflect an enlarging renal/retroperitoneal mass and metastatic spread. Frequencies are incompletely reported because histotypes are rare and registry symptom fields are limited.

- **Renal/abdominal mass** — usually adult or adolescent onset according to subtype; often large and progressive. Suggested HPO: **HP:0009726, renal neoplasm**; **HP:0031500, abdominal mass**.
- **Flank or abdominal pain** — variable, progressive as capsule or adjacent structures are involved. HPO: **HP:0031605, flank pain**; **HP:0002027, abdominal pain**.
- **Hematuria** — intermittent gross or microscopic bleeding when collecting-system or vascular structures are invaded. HPO: **HP:0000790, hematuria**.
- **Constitutional effects:** weight loss, fatigue, fever, anorexia, or anemia in advanced disease. Suggested HPO: **HP:0001824, weight loss**; **HP:0012378, fatigue**; **HP:0001945, fever**; **HP:0001903, anemia**.
- **Metastatic manifestations:** cough/dyspnea from pulmonary metastases and bone pain/pathologic fracture from osseous spread. Among metastatic adult cases, lung involvement was reported in **68%** and bone involvement in **41.2%**. (uhlig2024epidemiologytreatmentand pages 3-5)
- **Laboratory abnormalities:** anemia, hematuria, impaired renal function, or elevated inflammatory indices can occur, but none is sensitive or specific. There is no validated serum tumor marker.

Severity is highly variable but frequently substantial: median tumor diameter was approximately **10 cm**, and almost half of registry patients had T3–T4 disease. Pain, cancer-related fatigue, loss of renal function after nephrectomy, systemic-therapy toxicity, fear of recurrence, and metastatic disability impair quality of life. No kidney-sarcoma-specific EQ-5D, SF-36, or PROMIS reference dataset was identified. (uhlig2024epidemiologytreatmentand pages 1-2, uhlig2024epidemiologytreatmentand pages 7-9)

## 4. Genetic and molecular information

| Subtype / typical age | Defining tumor alteration | Useful IHC | Clinical behavior | Usual treatment framework |
|---|---|---|---|---|
| Adult renal leiomyosarcoma; typically older adults, median age about 62 y in national data | Usually complex-karyotype smooth-muscle sarcoma; no single pathognomonic renal-specific fusion established in gathered evidence | Smooth-muscle markers are typically used in practice; p16/p53 overexpression reported as potential prognostic indicators in review literature | Most common adult renal sarcoma histotype; often presents as a large renal mass and can be locally advanced or metastatic; among renal sarcoma histotypes, outcomes were relatively more favorable than angiosarcoma in 2024 registry analysis (uhlig2024epidemiologytreatmentand pages 1-2, uhlig2024epidemiologytreatmentand pages 3-5, uhlig2024epidemiologytreatmentand pages 5-7, mohd2022etiologiesgrossappearance pages 9-10) | Complete surgical resection/nephrectomy is the mainstay; systemic therapy considered for advanced disease, with histology-tailored soft-tissue sarcoma regimens rather than renal-cell-carcinoma-specific therapy (uhlig2024epidemiologytreatmentand pages 5-7, uhlig2024epidemiologytreatmentand pages 7-9, uhlig2024epidemiologytreatmentand pages 9-10) |
| Renal synovial sarcoma; usually adolescents/young-to-middle-aged adults | **SS18::SSX** fusion (classically SS18-SSX1/2), causing BAF/chromatin-remodeling dysregulation; this is the defining lesion of synovial sarcoma generally (OpenTargets Search: kidney sarcoma) | TLE1, cytokeratin/EMA, CD99 may support diagnosis; SS18-SSX fusion-specific testing or molecular confirmation is preferred; diffuse SS18-SSX antibody staining is useful in modern practice for synovial sarcoma generally (OpenTargets Search: kidney sarcoma) | Rare primary renal spindle-cell sarcoma; can mimic other renal spindle tumors, so expert molecular pathology is important | Surgery with negative margins when localized; for advanced disease, treatment is generally extrapolated from synovial/soft-tissue sarcoma practice, with chemotherapy in selected patients (uhlig2024epidemiologytreatmentand pages 7-9, uhlig2024epidemiologytreatmentand pages 9-10) |
| Renal Ewing sarcoma / PNET; mainly children, adolescents, and young adults | **EWSR1::FLI1** or related Ewing-family fusion; defining molecular event of Ewing sarcoma family tumors (bradford2020primaryrenalewing pages 7-7, bradford2020primaryrenalewing pages 5-7) | CD99+, FLI1+, NKX2.2+ are useful supportive markers; molecular confirmation is required (bradford2020primaryrenalewing pages 5-7) | Aggressive renal presentation with high metastatic burden at diagnosis; pooled analysis found metastases at diagnosis in about 53% and nodal disease more frequent than in skeletal Ewing sarcoma (bradford2020primaryrenalewing pages 7-7, bradford2020primaryrenalewing pages 5-7) | Multimodal therapy: neoadjuvant/adjuvant **VDC/IE**-based chemotherapy, nephrectomy aiming for negative margins, and selective radiotherapy (bradford2020primaryrenalewing pages 7-7) |
| Pediatric clear cell sarcoma of kidney (CCSK); usually early childhood; distinct entity often confused with “kidney sarcoma” | **BCOR internal tandem duplication** is characteristic in many cases; **YWHAE::NUTM2** occurs in a subset; biologically distinct from adult primary renal sarcoma umbrella (OpenTargets Search: kidney sarcoma) | BCOR immunoreactivity is commonly used in practice; differential diagnosis requires molecular correlation because BCOR expression can occur in other sarcomas (OpenTargets Search: kidney sarcoma) | Pediatric malignant renal tumor distinct from adult renal sarcomas; included here because of naming confusion rather than because it is the same disease category | Pediatric renal-tumor protocols using surgery plus multiagent chemotherapy, with radiotherapy in selected cases; not managed as adult renal sarcoma (OpenTargets Search: kidney sarcoma) |
| Primary renal angiosarcoma; usually adults | No single defining recurrent renal-specific alteration established in gathered evidence; endothelial-lineage malignant vascular sarcoma | Endothelial markers are typically used in practice (for example CD31/CD34/ERG in angiosarcoma workups) | Very rare and aggressive; 2024 renal-sarcoma analysis found worse prognosis than leiomyosarcoma (HR 2.42) (uhlig2024epidemiologytreatmentand pages 5-7) | Surgery when feasible; systemic therapy for advanced disease is extrapolated from angiosarcoma/STS practice; radiation used infrequently overall in renal sarcoma cohorts (uhlig2024epidemiologytreatmentand pages 5-7, uhlig2024epidemiologytreatmentand pages 7-9) |
| Malignant rhabdoid tumor of kidney; predominantly infants/young children, but adult renal rhabdoid tumors were captured in registry data | Classically associated with **SMARCB1/INI1** loss in malignant rhabdoid tumors generally; renal-sarcoma registry identified this as one of the more common histotypes | INI1/SMARCB1 loss is the key diagnostic immunophenotypic finding in routine practice for rhabdoid tumors generally | Highly aggressive; one of the more common histotypes in the adult registry compilation despite overall rarity of adult cases (uhlig2024epidemiologytreatmentand pages 1-2, uhlig2024epidemiologytreatmentand pages 7-9) | Surgery is central when possible; multimodal pediatric or rhabdoid-tumor-directed systemic therapy is typically required, but renal-specific adult evidence is sparse (uhlig2024epidemiologytreatmentand pages 5-7, uhlig2024epidemiologytreatmentand pages 7-9) |
| Sclerosing epithelioid fibrosarcoma of kidney (SEF); very rare adults | **EWSR1::CREB3L1** fusion reported in renal SEF; molecularly distinctive fibroblastic sarcoma (baydar2015primarysclerosingepithelioid pages 12-12) | MUC4, vimentin, BCL2 positive; negative for S100, CD34, desmin in reported renal cases (baydar2015primarysclerosingepithelioid pages 12-12) | Exceptionally rare; at least one reported renal case had widespread metastases at diagnosis, indicating potentially aggressive behavior (baydar2015primarysclerosingepithelioid pages 12-12) | Complete excision when feasible; no renal-SEF-specific systemic standard established in gathered evidence (baydar2015primarysclerosingepithelioid pages 12-12) |


*Table: This table summarizes the major histologic entities that present as primary renal sarcoma or are commonly confused with it, highlighting subtype-defining molecular alterations, practical diagnostic markers, behavior, and treatment logic. It is useful for distinguishing the heterogeneous adult renal sarcoma umbrella from specific fusion-defined and pediatric renal tumor entities.*

### Interpretation of variants

These rearrangements/ITDs are **somatic structural oncogenic events**, generally absent from population germline databases; therefore, gnomAD allele frequency and Mendelian carrier frequency are not meaningful. They should be reported under AMP/ASCO/CAP somatic-oncology conventions, not assigned germline ACMG pathogenicity without separate constitutional testing.

- **Synovial sarcoma:** t(X;18) produces **SS18::SSX1/SSX2**, replacing native SS18 in the BAF/SWI–SNF chromatin-remodeling complex and reprogramming enhancer accessibility. Open Targets strongly associates SS18, SSX1, and SSX2 with synovial sarcoma. (OpenTargets Search: kidney sarcoma)
- **Ewing sarcoma:** usually **EWSR1::FLI1**, an aberrant ETS transcription factor that rewires enhancer activity, cell-cycle programs, differentiation, and invasion. Renal disease shares the canonical molecular lesion but has disproportionately aggressive presentation. (bradford2020primaryrenalewing pages 7-7, bradford2020primaryrenalewing pages 5-7)
- **CCSK:** most tumors contain a **BCOR exon-15 internal tandem duplication**; a smaller, usually mutually exclusive group carries **YWHAE::NUTM2**. NTRK3 transcription/protein overexpression is reported across BCOR-family tumors, including CCSK, but is not equivalent to an actionable NTRK fusion. (OpenTargets Search: kidney sarcoma)
- **SEF:** reported renal tumors were MUC4-positive and carried **EWSR1::CREB3L1**. One of two patients had disseminated disease at diagnosis. (baydar2015primarysclerosingepithelioid pages 12-12)
- **LMS:** usually has a complex genome rather than one defining fusion; disruption of TP53/RB1/PTEN-associated cell-cycle and survival control is biologically plausible across LMS. Renal-specific comprehensive genomic series remain scarce.

No validated kidney-sarcoma modifier genes, protective alleles, founder variants, germline mosaicism, anticipation, or carrier frequency are known. Constitutional testing is appropriate only when age, multiple tumors, family history, or pathology suggests a predisposition syndrome.

## 5. Environmental information

There is no reproducible renal-sarcoma-specific association with smoking, alcohol, diet, exercise, air pollution, pesticides, or occupational agents. Prior radiotherapy is a recognized general cause of radiation-induced STS after latency, but a primary renal sarcoma should be labeled radiation-associated only when accepted temporal and anatomic criteria are met. No bacterial, viral, fungal, or parasitic cause applies to the conventional disease. Prevention databases should therefore record most proposed exposures as **unknown/not established**, not negative causal facts.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Initiation:** a renal mesenchymal/progenitor, smooth-muscle, vascular-endothelial, or poorly differentiated precursor acquires a subtype-defining fusion or complex tumor-suppressor damage.
2. **Upstream transcriptional/chromatin dysregulation:** fusion proteins such as SS18::SSX and EWSR1::FLI1 alter chromatin occupancy and transcription; BCOR lesions disturb Polycomb-associated repression.
3. **Downstream processes:** sustained proliferation, failed differentiation, apoptosis evasion, angiogenesis, extracellular-matrix remodeling, invasion, and metastatic dissemination.
4. **Tissue injury:** expansile growth causes compression and ischemia; invasion produces hemorrhage, necrosis, collecting-system bleeding, and replacement of renal parenchyma.
5. **Clinical expression:** mass, pain, hematuria, anemia, loss of renal function, and lung/bone/nodal metastases.

Suggested GO biological processes include **GO:0007049 cell cycle**, **GO:0008283 cell population proliferation**, **GO:0006915 apoptotic process**, **GO:0001525 angiogenesis**, **GO:0030198 extracellular matrix organization**, **GO:0007155 cell adhesion**, **GO:0016477 cell migration**, and **GO:0006355 regulation of DNA-templated transcription**. Relevant cell types include **CL:0000192 smooth muscle cell** for LMS, **CL:0000115 endothelial cell** for angiosarcoma, **CL:0000057 fibroblast** for fibroblastic sarcomas, and an incompletely resolved primitive mesenchymal progenitor for fusion-driven round-cell tumors.

### Molecular profiling and advanced technologies

No TCGA-scale, kidney-sarcoma-specific single-cell, spatial-transcriptomic, proteomic, metabolomic, lipidomic, or integrated multi-omics atlas was identified. Existing evidence comes mainly from bulk tumor sequencing, fusion assays, IHC, and histotype-level sarcoma datasets. This lack of renal-specific molecular profiling is a major research gap and precludes defining a universal metabolic or immune signature.

## 7. Anatomical structures affected

- **Primary organ:** kidney — suggested **UBERON:0002113**.
- **Potential sites of origin:** renal capsule, parenchymal interstitium, renal sinus, pelvis-adjacent soft tissue, and renal vascular smooth muscle/endothelium.
- **Local extension:** perinephric fat, Gerota fascia, renal vein/inferior vena cava, adrenal gland, psoas, bowel, pancreas, spleen, liver, or abdominal wall depending on side and size.
- **Secondary organs:** lung and bone predominate; regional lymph nodes are particularly important in renal Ewing sarcoma. Renal ESFT nodal disease occurred in approximately **24%**, compared with 3.2% in skeletal ESFT. (bradford2020primaryrenalewing pages 5-7)
- **Laterality:** generally unilateral; no consistent right/left preference is established.
- **Subcellular compartments:** nucleus/chromatin for fusion-driven transcriptional mechanisms (**GO:0005634 nucleus**, **GO:0000785 chromatin**); cytoskeleton/contractile apparatus in LMS; endothelial junctions and extracellular matrix in angiosarcoma.

## 8. Temporal development

Adult LMS and angiosarcoma usually develop insidiously in middle-to-late adulthood; renal synovial and Ewing sarcomas affect younger patients; CCSK and rhabdoid tumor are chiefly pediatric. The course is progressive rather than episodic. Localized disease may enter treatment-induced remission after complete resection, but high-grade tumors can recur locally or hematogenously years later.

Renal Ewing sarcoma is often rapidly progressive: pooled evidence found **53.2% metastatic at diagnosis**, substantially exceeding the general Ewing population. In the reported pediatric/young-adult institutional series, five of seven patients relapsed after initial remission. (bradford2020primaryrenalewing pages 7-7, bradford2020primaryrenalewing pages 5-7)

Staging should use the applicable **AJCC soft-tissue sarcoma site/stage framework**, supplemented by FNCLCC grade where valid for the histotype. CCSK, rhabdoid tumor, and Ewing sarcoma follow pediatric/diagnosis-specific staging and response systems rather than adult retroperitoneal STS rules.

## 9. Inheritance and population

The overall incidence was **0.53 cases per million persons annually** during 2004–2016, stable over time (AAPC 0.7%; p=0.6). LMS alone occurred at 0.14/million and malignant rhabdoid tumor at 0.06/million. (uhlig2024epidemiologytreatmentand pages 1-2)

No conventional inheritance pattern, penetrance, anticipation, carrier state, founder effect, or consanguinity relationship applies to the umbrella diagnosis. Most defining alterations are acquired in the tumor. The national cohort showed marked sex variation by histotype rather than one universal sex ratio. No robust ethnicity-specific or geographic concentration is established; apparent differences are vulnerable to small numbers and registry ascertainment. (uhlig2024epidemiologytreatmentand pages 3-5)

## 10. Diagnostics

### Recommended workflow

1. **Imaging:** multiphasic contrast CT or MRI of the abdomen/pelvis to define renal origin, local invasion, vessel involvement, and resectability; CT chest for pulmonary staging. MRI is especially useful for venous thrombus and soft-tissue planes. PET/CT is selective, not a substitute for chest/abdominal staging.
2. **Multidisciplinary review:** radiology, urologic/sarcoma surgery, medical and radiation oncology, and specialist sarcoma pathology before definitive treatment.
3. **Biopsy:** image-guided coaxial core biopsy along a tract that can be removed or safely encompassed. Upfront surgery may be reasonable for a resectable renal mass when management would not change, but biopsy is particularly valuable for unresectable/metastatic disease or when neoadjuvant therapy is contemplated.
4. **Histology/IHC:** determine spindle, round-cell, pleomorphic, vascular, or epithelioid pattern; assess mitoses, necrosis, grade, and margins. A practical panel may include pancytokeratin/EMA and PAX8 to exclude carcinoma; SMA/desmin/h-caldesmon for LMS; ERG/CD31 for angiosarcoma; S100/SOX10; myogenin/MyoD1; CD99/NKX2.2; TLE1 and SS18–SSX; BCOR; INI1; MDM2; STAT6; and MUC4 according to morphology.
5. **Molecular confirmation:** targeted RNA sequencing is preferred for suspected fusion sarcoma; alternatives include break-apart FISH, RT-PCR, or fusion-specific IHC. DNA NGS is useful for complex-genome tumors and actionable alterations but can miss RNA-level fusions.

### Differential diagnosis

The essential exclusions are sarcomatoid RCC, collecting-duct/urothelial carcinoma, Wilms tumor, CCSK, malignant rhabdoid tumor, angiomyolipoma/PEComa, solitary fibrous tumor, retroperitoneal liposarcoma secondarily involving kidney, metastasis, lymphoma, and benign leiomyoma. Renal sarcoma and retroperitoneal sarcoma can be difficult to distinguish anatomically; expert radiology and examination of the resection relationship to renal parenchyma/capsule are required. (uhlig2024epidemiologytreatmentand pages 9-10)

No blood/urine biomarker, liquid-biopsy assay, WES/WGS screen, CMA, karyotype, mitochondrial assay, or repeat-expansion test is recommended for routine asymptomatic screening. Germline panel/WES is reserved for clinical suspicion of inherited predisposition.

## 11. Outcome and prognosis

Across the 2024 adult cohort, median OS was **25 months**, although outcomes differed greatly by histotype and stage. Angiosarcoma had worse survival than LMS (**HR 2.42**). Independently favorable factors included younger age, female sex, lower comorbidity, lower T stage, negative margins, no necrosis, no distant metastasis, and LMS histology. (uhlig2024epidemiologytreatmentand pages 1-2, uhlig2024epidemiologytreatmentand pages 5-7)

Positive margins occurred in **21.3%** overall and **40.6%** of T4 resections, emphasizing the importance of planned en-bloc surgery. Distant disease was present in approximately 29–32%. (uhlig2024epidemiologytreatmentand pages 3-5, uhlig2024epidemiologytreatmentand pages 5-7)

For renal Ewing sarcoma, localized survival was reported at approximately **55%**, while metastatic and nodal disease predicted inferior OS. Pulmonary-only metastasis generally fares better than bone/bone-marrow disease, but renal-primary outcomes remain worse than conventional localized Ewing benchmarks. (bradford2020primaryrenalewing pages 7-7, bradford2020primaryrenalewing pages 5-7)

Functional morbidity includes nephrectomy-related reduction in renal reserve, chronic kidney disease risk, chemotherapy cardiotoxicity/myelosuppression, ifosfamide nephrotoxicity/Fanconi syndrome, radiation injury, chronic pain, and disability from metastatic disease. Kidney-specific quality-of-life and disability-adjusted-life-year estimates are unavailable.

## 12. Treatment and real-world implementation

### Localized adult disease

**Complete en-bloc resection with microscopically negative margins (R0)** is the only established curative foundation—usually radical nephrectomy, occasionally organ-sparing resection for carefully selected small lesions. In the national cohort, 81.6% underwent resection and 69.3% underwent radical/total nephrectomy. Suggested NCIt terms: **Radical Nephrectomy**, **Partial Nephrectomy**, **Surgical Resection**, and **Metastasectomy**. (uhlig2024epidemiologytreatmentand pages 1-2, uhlig2024epidemiologytreatmentand pages 3-5)

Routine lymphadenectomy is not supported for all adult STS histotypes, although suspicious nodes should be removed and nodal evaluation is particularly relevant to renal Ewing sarcoma. Radiotherapy may be considered for close/positive margins, unresectable local disease, palliation, or selected radiosensitive histotypes, but renal-adjacent bowel/liver/spinal cord and the remaining kidney constrain dose.

### Systemic therapy

Treatment should follow **histotype-specific STS practice**:

- **Adult LMS/undifferentiated or pleomorphic STS:** doxorubicin, doxorubicin–ifosfamide when tumor shrinkage is critical, or gemcitabine–docetaxel; later options may include pazopanib, trabectedin, dacarbazine, or eribulin according to histology, prior therapy, jurisdiction, and patient fitness.
- **Renal synovial sarcoma:** comparatively ifosfamide-sensitive; anthracycline/ifosfamide-based therapy is commonly used for high-risk or advanced disease.
- **Renal Ewing sarcoma:** interval-compressed **VDC/IE**—vincristine/doxorubicin/cyclophosphamide alternating with ifosfamide/etoposide—plus nephrectomy/local control and completion chemotherapy. The review describes 8–12 weeks of preoperative chemotherapy followed by negative-margin surgery and selective postoperative radiation. Suggested NCIt terms include the individual agents, **Combination Chemotherapy**, **External Beam Radiation Therapy**, and **Nephrectomy**. (bradford2020primaryrenalewing pages 7-7)
- **CCSK/rhabdoid tumor:** pediatric cooperative-group protocols combining nephrectomy, intensive multiagent chemotherapy, and stage/risk-directed radiotherapy; these should not be treated as adult LMS.
- **Angiosarcoma:** taxane- or anthracycline-based therapy and selected antiangiogenic approaches are extrapolated from nonrenal angiosarcoma.

In real-world renal sarcoma, systemic therapy was used in only **16.1% of localized cases**, 39.8% of T4 cases, and 54.6% of metastatic cases; 93.3% of systemic treatment was adjuvant and only 4.6% neoadjuvant. Primary-site radiotherapy was used in 5.2%. Registry associations suggested benefit from systemic treatment in LMS, angiosarcoma, and clear-cell sarcoma, but confounding by indication prevents causal interpretation. (uhlig2024epidemiologytreatmentand pages 5-7, uhlig2024epidemiologytreatmentand pages 7-9)

### Targeted, immune, cellular, and experimental treatment

Broad DNA/RNA profiling is reasonable in advanced disease to identify rare actionable fusions or mutations. Open Targets links kidney sarcoma chiefly to chemotherapy targets such as TOP2A and tubulins, reflecting anthracycline and microtubule-directed regimens rather than kidney-specific dependencies. In synovial sarcoma, SS18/SSX are causal but not yet routine drug targets. (OpenTargets Search: kidney sarcoma)

Checkpoint inhibitors have no established kidney-sarcoma-wide role; efficacy is histotype-dependent and generally lower in fusion-driven, low-mutation-burden tumors. Do not extrapolate the marked checkpoint sensitivity of **sarcomatoid RCC** to true renal sarcoma.

Relevant basket or adjacent trials identified include **NCT02795819** (AR-42 plus pazopanib; phase I, terminated after six participants), **NCT03798106** (pazopanib plus durvalumab in metastatic STS; phase II, completed), and **NCT06444880** (ubamatamab ± cemiplimab in MUC16-expressing SMARCB1-deficient malignancies; phase II, active-not-recruiting). These are not proof of efficacy specifically in primary renal sarcoma.

## 13. Prevention

- **Primary prevention:** no disease-specific intervention or vaccine.
- **Secondary prevention:** no population screening; rarity makes ultrasound, CT, urine, or molecular screening unjustified in average-risk asymptomatic people.
- **High-risk genetics:** counseling and syndrome-specific surveillance only when a constitutional predisposition is clinically demonstrated; no kidney-sarcoma-specific carrier screening, prenatal test, or preimplantation-testing recommendation exists.
- **Tertiary prevention:** expert surgery, preservation of contralateral renal function, avoidance of nephrotoxins, rehabilitation, thrombosis/pain/nutrition management, and structured surveillance to detect resectable recurrence.
- **Follow-up:** chest and abdominal cross-sectional imaging should be individualized by grade, histotype, stage, and treatment; high-grade disease requires closer early follow-up because lung relapse is common.

## 14. Other species and natural disease

Naturally occurring primary renal LMS has been reported in domestic cats (**NCBI Taxon 9685; Felis catus**), but evidence consists primarily of isolated veterinary case reports. Similar renal spindle-cell morphology and smooth-muscle immunophenotype provide comparative-pathology interest, not a validated translational model. Breed predisposition and Vertebrate Breed Ontology associations are unknown. Sporadic renal sarcomas also occur in dogs, but robust incidence and molecular-concordance studies are lacking. There is **no zoonotic or cross-species transmission**.

## 15. Model organisms and experimental systems

No single model captures the 43-histotype renal-sarcoma umbrella. Models are subtype-specific:

- human cell lines and 2-D/3-D cultures;
- subcutaneous or renal-subcapsular xenografts in immunodeficient mice;
- patient-derived xenografts/orthotopic xenografts;
- fusion-driven Ewing or synovial sarcoma genetically engineered mouse models;
- zebrafish embryo and chick chorioallantoic-membrane xenografts for rapid invasion and drug-response studies.

Renal-subcapsular xenografting supplies a vascular microenvironment and allows growth/metastasis studies, but implantation site does not prove renal cell of origin. Xenografts retain human tumor genetics but lack an intact human immune system; GEMMs model initiation and immune interactions but can underrepresent human genomic complexity and metastasis. Accordingly, these systems support mechanism and drug discovery at the **histotype level**, not validation of one universal kidney-sarcoma mechanism.

## Evidence appraisal and research priorities

The 2024 SEER/NCDB analysis is the best contemporary population evidence, but it lacked treatment-regimen detail, mutation status, complete grade information, and robust radiotherapy numbers. Its treatment-survival associations are retrospective. The renal Ewing literature is larger than that for most subtypes but remains vulnerable to publication bias. (uhlig2024epidemiologytreatmentand pages 9-10, bradford2020primaryrenalewing pages 5-7)

Priority needs are prospective international registration with central pathology review; mandatory RNA-fusion and DNA profiling; histotype-stratified treatment data; renal-specific organoid/PDX models; single-cell and spatial profiling; circulating-tumor-DNA studies; patient-reported outcomes; and trials that enroll by molecular histotype rather than merely renal site.

### Selected recent and authoritative sources

1. **Uhlig J, et al. “Epidemiology, treatment and outcomes of primary renal sarcomas in adult patients.” Scientific Reports. Published May 2024.** DOI/URL: https://doi.org/10.1038/s41598-024-60174-8. Abstract quotation: “Accounting for 0.25% of renal malignancies, renal sarcomas include 43 histiotypes with distinct epidemiology, clinical presentation, outcomes and sensitivity to systemic therapy.” (uhlig2024epidemiologytreatmentand pages 1-2)
2. **Bradford K, et al. “Primary Renal Ewing Sarcoma in Children and Young Adults.” Journal of Pediatric Hematology/Oncology. Published April 2020.** DOI/URL: https://doi.org/10.1097/MPH.0000000000001804. Abstract quotation: “primary renal ESFT presentations seem to be more aggressive and have worse outcomes.” (bradford2020primaryrenalewing pages 7-7, bradford2020primaryrenalewing pages 5-7)
3. **Baydar DE, et al. “Primary sclerosing epithelioid fibrosarcoma of kidney…” Diagnostic Pathology. Published October 2015.** DOI/URL: https://doi.org/10.1186/s13000-015-0420-z. The reported renal tumors showed MUC4 expression and EWSR1–CREB3L1 fusion. (baydar2015primarysclerosingepithelioid pages 12-12)
4. **Open Targets Platform, kidney sarcoma MONDO:0002930.** Disease–target evidence includes chemotherapy-associated TOP2A/tubulin targets and subtype-defining SS18/SSX associations for synovial sarcoma: https://platform.opentargets.org/. (OpenTargets Search: kidney sarcoma)

References

1. (uhlig2024epidemiologytreatmentand pages 1-2): Johannes Uhlig, Annemarie Uhlig, Hari Deshpande, Philipp Ströbel, Lutz Trojan, Joachim Lotz, Michael Hurwitz, Omeed Hafez, Peter Humphrey, Viktor Grünwald, and Hyun S. Kim. Epidemiology, treatment and outcomes of primary renal sarcomas in adult patients. Scientific Reports, May 2024. URL: https://doi.org/10.1038/s41598-024-60174-8, doi:10.1038/s41598-024-60174-8. This article has 7 citations and is from a peer-reviewed journal.

2. (uhlig2024epidemiologytreatmentand pages 5-7): Johannes Uhlig, Annemarie Uhlig, Hari Deshpande, Philipp Ströbel, Lutz Trojan, Joachim Lotz, Michael Hurwitz, Omeed Hafez, Peter Humphrey, Viktor Grünwald, and Hyun S. Kim. Epidemiology, treatment and outcomes of primary renal sarcomas in adult patients. Scientific Reports, May 2024. URL: https://doi.org/10.1038/s41598-024-60174-8, doi:10.1038/s41598-024-60174-8. This article has 7 citations and is from a peer-reviewed journal.

3. (uhlig2024epidemiologytreatmentand pages 9-10): Johannes Uhlig, Annemarie Uhlig, Hari Deshpande, Philipp Ströbel, Lutz Trojan, Joachim Lotz, Michael Hurwitz, Omeed Hafez, Peter Humphrey, Viktor Grünwald, and Hyun S. Kim. Epidemiology, treatment and outcomes of primary renal sarcomas in adult patients. Scientific Reports, May 2024. URL: https://doi.org/10.1038/s41598-024-60174-8, doi:10.1038/s41598-024-60174-8. This article has 7 citations and is from a peer-reviewed journal.

4. (uhlig2024epidemiologytreatmentand pages 7-9): Johannes Uhlig, Annemarie Uhlig, Hari Deshpande, Philipp Ströbel, Lutz Trojan, Joachim Lotz, Michael Hurwitz, Omeed Hafez, Peter Humphrey, Viktor Grünwald, and Hyun S. Kim. Epidemiology, treatment and outcomes of primary renal sarcomas in adult patients. Scientific Reports, May 2024. URL: https://doi.org/10.1038/s41598-024-60174-8, doi:10.1038/s41598-024-60174-8. This article has 7 citations and is from a peer-reviewed journal.

5. (OpenTargets Search: kidney sarcoma): Open Targets Query (kidney sarcoma, 50 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (bradford2020primaryrenalewing pages 7-7): Kathryn Bradford, Alexander Nobori, Brittany Johnson, Wendy Allen-Rhoades, Bindi Naik-Mathuria, Eduard H. Panosyan, Moran Gotesman, Joseph Lasky, Jerry Cheng, Alan Ikeda, Jeffrey Goldstein, Arun Singh, and Noah Federman. Primary renal ewing sarcoma in children and young adults. Journal of Pediatric Hematology/Oncology, 42:474-481, Apr 2020. URL: https://doi.org/10.1097/mph.0000000000001804, doi:10.1097/mph.0000000000001804. This article has 24 citations.

7. (baydar2015primarysclerosingepithelioid pages 12-12): Dilek Ertoy Baydar, Kemal Kosemehmetoglu, Oguz Aydin, Julia A. Bridge, Berrin Buyukeren, and Fazil Tuncay Aki. Primary sclerosing epithelioid fibrosarcoma of kidney with variant histomorphologic features: report of 2 cases and review of the literature. Diagnostic Pathology, Oct 2015. URL: https://doi.org/10.1186/s13000-015-0420-z, doi:10.1186/s13000-015-0420-z. This article has 35 citations and is from a peer-reviewed journal.

8. (uhlig2024epidemiologytreatmentand pages 3-5): Johannes Uhlig, Annemarie Uhlig, Hari Deshpande, Philipp Ströbel, Lutz Trojan, Joachim Lotz, Michael Hurwitz, Omeed Hafez, Peter Humphrey, Viktor Grünwald, and Hyun S. Kim. Epidemiology, treatment and outcomes of primary renal sarcomas in adult patients. Scientific Reports, May 2024. URL: https://doi.org/10.1038/s41598-024-60174-8, doi:10.1038/s41598-024-60174-8. This article has 7 citations and is from a peer-reviewed journal.

9. (mohd2022etiologiesgrossappearance pages 9-10): Ahmed B Mohd, Reem A Ghannam, Omar B Mohd, Rama Elayan, Khaled Albakri, Nesreen Huneiti, Farah Daraghmeh, Eman Al-khatatbeh, and Mohammad Al-thnaibat. Etiologies, gross appearance, histopathological patterns, prognosis, and best treatments for subtypes of renal carcinoma: an educational review. Cureus, Dec 2022. URL: https://doi.org/10.7759/cureus.32338, doi:10.7759/cureus.32338. This article has 24 citations.

10. (bradford2020primaryrenalewing pages 5-7): Kathryn Bradford, Alexander Nobori, Brittany Johnson, Wendy Allen-Rhoades, Bindi Naik-Mathuria, Eduard H. Panosyan, Moran Gotesman, Joseph Lasky, Jerry Cheng, Alan Ikeda, Jeffrey Goldstein, Arun Singh, and Noah Federman. Primary renal ewing sarcoma in children and young adults. Journal of Pediatric Hematology/Oncology, 42:474-481, Apr 2020. URL: https://doi.org/10.1097/mph.0000000000001804, doi:10.1097/mph.0000000000001804. This article has 24 citations.

## Artifacts

- [Edison artifact artifact-00](Kidney_Sarcoma-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 26 |
| Resolved | 26 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 3 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 0 |

Every term resolved, and every label the report gave matched.