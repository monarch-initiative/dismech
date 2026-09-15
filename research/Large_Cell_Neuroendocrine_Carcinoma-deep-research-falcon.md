---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-09T18:14:02.701518'
end_time: '2026-09-09T18:26:30.397040'
duration_seconds: 747.7
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Large Cell Neuroendocrine Carcinoma
  mondo_id: ''
  category: Neoplastic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 43
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 7
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Large_Cell_Neuroendocrine_Carcinoma-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Large Cell Neuroendocrine Carcinoma
- **MONDO ID:**  (if available)
- **Category:** Neoplastic

## Research Objectives

Please provide a comprehensive research report on **Large Cell Neuroendocrine Carcinoma** covering all of the
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
- **Disease Name:** Large Cell Neuroendocrine Carcinoma
- **MONDO ID:**  (if available)
- **Category:** Neoplastic

## Research Objectives

Please provide a comprehensive research report on **Large Cell Neuroendocrine Carcinoma** covering all of the
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


# Large Cell Neuroendocrine Carcinoma: Disease-Characteristics Report

## Scope and evidence note

**Large cell neuroendocrine carcinoma (LCNEC)** is a morphologic category of poorly differentiated, high-grade epithelial neuroendocrine carcinoma, not a single inherited syndrome. It most often refers to **pulmonary LCNEC**; morphologically similar carcinomas occur in the gastrointestinal, pancreatic, genitourinary, gynecologic, head-and-neck, and other organs. Because pulmonary disease dominates the evidence base, findings should not automatically be transferred to extrapulmonary LCNEC. Most evidence is aggregated disease-level evidence from pathology cohorts, registries, retrospective clinical series, and reviews—not individual-patient EHR evidence.

The following table provides a compact knowledge-base summary; the narrative afterward expands the requested domains.

| Knowledge-base field | Pulmonary LCNEC | Extrapulmonary LCNEC / poorly differentiated NEC | Ontology / identifier suggestions | Evidence |
|---|---|---|---|---|
| Definition and classification | Rare, high-grade pulmonary neuroendocrine carcinoma with large-cell, non-small-cell cytology, neuroendocrine architecture, extensive proliferation, necrosis, and neuroendocrine-marker expression. WHO reclassified it within pulmonary neuroendocrine carcinomas in 2015 and retained this concept in 2021. | Large-cell morphologic subtype of poorly differentiated neuroendocrine carcinoma arising outside the lung; reported in gastrointestinal, pancreatic, genitourinary, gynecologic, and other organs. It must be distinguished from well-differentiated grade-3 NET and mixed neuroendocrine–non-neuroendocrine neoplasms. | MONDO:0005057, large cell neuroendocrine carcinoma; MONDO:0003960, pulmonary large cell neuroendocrine carcinoma; category: neoplastic disease | (yang2022pulmonarylargecell pages 2-3, yang2022pulmonarylargecell pages 1-2, stumpo2023extrapulmonaryneuroendocrinecarcinomas pages 15-17) |
| Epidemiology | Approximately 0.3%–3% of lung cancers and 2.1%–3.5% of surgically resected lung cancers. Mean age is generally 60–70 years; patients are predominantly male and heavy smokers, with one synthesis reporting smoking histories in 92.8%. | Extremely rare and site-dependent; approximately 37% of all extrapulmonary NECs arise in the gastroenteropancreatic tract, followed by genitourinary and gynecologic sites. LCNEC-specific incidence by extrapulmonary organ is generally unavailable. | Adult onset; rare disease | (yang2022pulmonarylargecell pages 2-3, stumpo2023extrapulmonaryneuroendocrinecarcinomas pages 15-17) |
| Hallmark pathology | Organoid nests, peripheral palisading, trabeculae or rosettes; large polygonal cells with abundant cytoplasm, vesicular or coarse chromatin, and prominent nucleoli; extensive necrosis; more than 10 mitoses/2 mm², commonly 60–80/2 mm². | Similar poorly differentiated large-cell morphology, but organ-specific WHO criteria and associated non-neuroendocrine components must be assessed. Small-cell versus large-cell separation may have molecular and treatment relevance. | Suggested processes: cell proliferation, cell-cycle dysregulation, necrotic cell death | (yang2022pulmonarylargecell pages 3-4, zhang2024molecularfeaturesof pages 1-2) |
| Molecular alterations and subtypes | Frequent somatic alterations include **TP53** (~82.3%), **RB1** (~39.1%), **KEAP1** (~20.9%), **STK11** (~18.2%), **KRAS** (~12.7%), and **EGFR** (~11.9%). Major groups are SCLC-like (**TP53/RB1** co-altered), NSCLC-like (often RB1-intact with **STK11/KEAP1/KRAS** alterations), and rare carcinoid-like/**MEN1** tumors. POU2F3-positive tuft-cell-like LCNEC represents approximately 12%–20%. | Alterations vary by organ: colorectal NEC is enriched for **KRAS**, gastric NEC may show **TERT** amplification, and biliary NEC may harbor **ARID1A** alterations. A 257-patient comparative cohort found potentially targetable alterations or biomarkers in 22.2% of GEP-NECs. These are acquired tumor drivers, not established germline causes. | Open Targets-supported genes: **TP53, RB1, SMARCA4, STK11, KEAP1, CDKN2A, BRAF, IDH2** | (OpenTargets Search: large cell neuroendocrine carcinoma, yang2022pulmonarylargecell pages 3-4, zhang2024molecularfeaturesof pages 1-2, jimbo2024pou2f3expressingsmallcell pages 1-9) |
| Major clinical phenotypes and metastases | Frequently incidental or nonspecific: cough, chest pain, hemoptysis, and respiratory symptoms. Common metastatic sites are liver, bone, brain, and adrenal gland. Brain metastases occur in about 19.2%–20% overall and up to 35% of stage-IV disease; neurologic deficits, raised intracranial pressure, and seizures may result. | Symptoms depend on the primary organ and metastatic burden. Most are nonfunctional carcinomas; local obstruction, bleeding, pain, weight loss, and liver or distant metastases are more typical than classic hormone syndromes. | Suggested HPO concepts: cough, hemoptysis, chest pain, dyspnea, seizure, increased intracranial pressure, and metastases to brain, liver, or bone | (yang2022pulmonarylargecell pages 2-3, yang2022pulmonarylargecell pages 1-2, popov2024clinicalcharacteristicstreatment pages 1-2) |
| Diagnosis | Requires adequate tissue morphology plus at least one neuroendocrine marker: synaptophysin, chromogranin A, or CD56/NCAM1. INSM1 is positive in approximately 68%–91.3% and is a useful adjunct; TTF-1 is positive in about 54.8%. Ki-67 supports high-grade status but is not independently diagnostic. Small biopsies are prone to misclassification. | Requires organ-directed imaging and biopsy, confirmation of poor differentiation and large-cell morphology, neuroendocrine immunophenotyping, and exclusion of a pulmonary primary. Molecular or methylation profiling may help assign an unknown primary. | Diagnostic concepts: histopathology; immunohistochemistry; tumor next-generation sequencing; CT; MRI; FDG-PET | (yang2022pulmonarylargecell pages 2-3, popov2024clinicalcharacteristicstreatment pages 1-2, yang2022pulmonarylargecell pages 3-4, corti2024emergingtreatmentoptions pages 14-16) |
| Differential diagnosis | SCLC, basaloid or poorly differentiated squamous carcinoma, adenocarcinoma with neuroendocrine-marker expression, carcinoid tumor, SMARCA4-deficient thoracic tumor, and metastatic extrapulmonary NEC. A coexisting NSCLC component supports combined LCNEC; an SCLC component is classified as combined SCLC. | Well-differentiated NET G3, small-cell NEC, organ-specific adenocarcinoma or squamous carcinoma, lymphoma, melanoma, and mixed neuroendocrine–non-neuroendocrine neoplasm. | Suggested approach: morphology integrated with broad epithelial, neuroendocrine, and organ-lineage IHC panels | (yang2022pulmonarylargecell pages 9-9, yang2022pulmonarylargecell pages 3-4, zhang2024molecularfeaturesof pages 1-2, jimbo2024pou2f3expressingsmallcell pages 27-32) |
| Standard treatment | Resectable early disease: anatomic pulmonary resection with lymph-node staging, usually followed by platinum-based adjuvant chemotherapy because surgery alone has high recurrence. Advanced disease: platinum–etoposide is common; platinum–irinotecan or NSCLC-type platinum–gemcitabine/taxane may be considered, especially for RB1-intact/NSCLC-like tumors. Thoracic or brain radiotherapy is used selectively. | Localized disease may receive surgery or definitive chemoradiation. Advanced disease is generally treated with platinum–etoposide; no universally accepted second-line regimen exists. Treatment should incorporate primary site and actionable molecular alterations. | Suggested NCIt intervention concepts: surgical resection; cisplatin; carboplatin; etoposide; irinotecan; radiation therapy; stereotactic radiosurgery | (yang2022pulmonarylargecell pages 7-8, yang2022pulmonarylargecell pages 5-7, stumpo2023extrapulmonaryneuroendocrinecarcinomas pages 15-17, corti2024emergingtreatmentoptions pages 14-16) |
| Emerging targets and trials | Investigational chemoimmunotherapy includes atezolizumab–platinum–etoposide, phase II NCT05470595 (67 planned; active, not recruiting), and durvalumab–carboplatin–etoposide, phase II NCT06418087 (49 planned; recruiting). DLL3 is commonly expressed and is being explored with bispecific antibodies, radioligands, and cellular therapies; LCNEC-specific efficacy remains unproven. | Investigational approaches include dual checkpoint blockade, chemoimmunotherapy, DLL3 targeting, PRRT in receptor-positive disease, and genotype-matched **BRAF, KRAS G12C, ALK, NTRK**, or **RET** therapy. NCT06393816 evaluates durvalumab plus platinum–etoposide in NEC; NCT04079712 evaluates cabozantinib–nivolumab–ipilimumab in poorly differentiated NEC. | Suggested targets/interventions: DLL3; PD-1; PD-L1; CTLA-4; immune-checkpoint inhibitor therapy; molecularly targeted therapy | (corti2024emergingtreatmentoptions pages 14-16, serrano2024deltalikeligand3 pages 1-2, robinson2023futuretherapeuticstrategies pages 14-14, peddio2024dll3asa pages 1-3, NCT05470595 chunk 2) |
| Prognosis | Aggressive, rapidly progressive, and prone to early relapse: reported recurrence is 63.9%–82% within one year and 91% within two years after surgery. Stage-I five-year survival is approximately 27%–67%. In a 2024 brain-metastasis cohort, median overall survival was 16 months from LCNEC diagnosis and 7 months after brain-metastasis diagnosis; synchronous versus metachronous brain metastasis yielded 11 versus 27 months. | Usually poor and governed by stage, primary site, differentiation, proliferation, and treatment response. Advanced extrapulmonary NEC studies commonly report median progression-free survival around 2–5 months and overall survival around 5–11 months, although LCNEC-only estimates are sparse. | Adverse features: advanced TNM stage, large tumor, distant or synchronous brain metastases; possible molecular modifiers include **KEAP1**, RB1 status, and immune infiltration | (popov2024clinicalcharacteristicstreatment pages 1-2, yang2022pulmonarylargecell pages 7-8, robinson2023futuretherapeuticstrategies pages 14-14, robinson2023futuretherapeuticstrategies pages 17-18) |
| Prevention | No LCNEC-specific chemoprevention or vaccine exists. Tobacco avoidance and cessation are the most biologically supported primary-prevention measures. Eligible high-risk smokers may undergo standard low-dose CT lung-cancer screening, but there is no LCNEC-specific screening test. | No established organ-independent prevention or screening program. Apply standard prevention and screening for the organ of origin and modifiable carcinogenic exposures where relevant. Germline carrier or cascade screening is not routinely indicated because LCNEC is primarily sporadic and somatically driven. | Tobacco-use prevention; smoking cessation; low-dose computed tomography screening | (yang2022pulmonarylargecell pages 2-3, yang2022pulmonarylargecell pages 1-2) |
| Models | The 2023 **46LCNEC** murine line was derived from spontaneous CMV-QKO mouse LCNEC and forms syngeneic allografts in immunocompetent or immunodeficient mice. It retains the parental tumor’s LCNEC transcriptomic program and supports therapy and immunotherapy experiments, but murine and multifocal GEMMs do not fully capture human heterogeneity. | HROC57 is a BRAF-mutant colorectal LCNEC cell-line/PDX pair sensitive to etoposide, cisplatin, and 5-FU. NEC organoids and PDXs commonly retain **TP53/RB1/KRAS/BRAF** alterations; model numbers, standardization, and availability remain limited. | Species/model suggestions: *Mus musculus*; genetically engineered mouse model; syngeneic allograft; patient-derived xenograft; tumor organoid; cancer cell line | (recuero2023novelmousecell pages 1-2, detjen2021modelsofgastroenteropancreatic pages 9-10, recuero2023novelmousecell pages 7-8) |


*Table: Compact comparison of pulmonary LCNEC and extrapulmonary large-cell or poorly differentiated neuroendocrine carcinoma, covering classification, molecular biology, clinical features, management, prognosis, prevention, and models.*

## 1. Disease information

### Definition and classification

LCNEC is defined by: (1) neuroendocrine architecture, such as organoid nests, trabeculae, peripheral palisading, or rosettes; (2) large-cell/non-small-cell cytology with abundant cytoplasm, vesicular or coarse chromatin, and often prominent nucleoli; (3) extensive proliferation and usually necrosis; and (4) neuroendocrine differentiation demonstrated by morphology and immunohistochemistry. Pulmonary LCNEC was described as a distinct entity in 1991, categorized as a large-cell/NSCLC variant in the 1999–2004 WHO schemes, and moved into the pulmonary neuroendocrine-carcinoma family in 2015, a concept retained in WHO 2021. Biologically it often resembles SCLC more than conventional NSCLC. (yang2022pulmonarylargecell pages 1-2, yang2022pulmonarylargecell pages 3-4)

A useful exact abstract statement from Yang et al. (published 11 October 2022) is: **“Pulmonary large cell neuroendocrine carcinoma (LCNEC) is a rare subtype of malignant pulmonary tumor.”** The review further reports that LCNEC is more aggressive than other NSCLC and has behavior similar to SCLC. [DOI/URL](https://doi.org/10.3389/pore.2022.1610730). (yang2022pulmonarylargecell pages 2-3, yang2022pulmonarylargecell pages 1-2)

### Identifiers and synonyms

- **MONDO:** MONDO:0005057, *large cell neuroendocrine carcinoma*; MONDO:0003960, *pulmonary large cell neuroendocrine carcinoma*. Site-specific MONDO entries include pancreatic LCNEC (MONDO:0006347) and ovarian large-cell neuroendocrine carcinoma (MONDO:0003049). (OpenTargets Search: large cell neuroendocrine carcinoma)
- **Synonyms:** LCNEC; large-cell neuroendocrine carcinoma; large-cell neuroendocrine cancer; pulmonary LCNEC; lung LCNEC; large-cell poorly differentiated neuroendocrine carcinoma. “High-grade neuroendocrine carcinoma” is broader and also includes small-cell NEC.
- **MeSH:** no uniquely specific LCNEC descriptor was established in the retrieved evidence; indexing commonly uses *Carcinoma, Neuroendocrine* plus the anatomic-site neoplasm.
- **ICD:** ICD-O morphology coding is more appropriate than a single ICD-10 diagnosis code. ICD-10-CM and ICD-11 generally combine anatomic-site malignancy coding with neuroendocrine histology; a universally specific cross-organ LCNEC code was not established in the retrieved sources.
- **OMIM/Orphanet:** no Mendelian OMIM disease entry or established inherited LCNEC syndrome was identified. LCNEC is principally a sporadic somatic neoplasm.

## 2. Etiology, risk, and protective factors

### Causal and risk factors

Pulmonary LCNEC has a strong tobacco association: patients are usually older, male, heavy smokers, and one synthesis found a smoking history in **92.8%**. Mean diagnostic age is approximately 60–70 years. The defensible causal chain is chronic tobacco-carcinogen exposure → accumulated somatic DNA damage and clonal selection → loss of cell-cycle/genome-surveillance pathways, often TP53 and RB1 or STK11/KEAP1-associated pathways → high-grade neuroendocrine lineage programs → invasive and metastatic carcinoma. Smoking is therefore the principal established environmental risk factor, although LCNEC-specific dose-response and attributable-risk estimates remain limited. (yang2022pulmonarylargecell pages 2-3, yang2022pulmonarylargecell pages 1-2)

For extrapulmonary LCNEC, risks are organ dependent. Some cervical cases can be HPV-associated, whereas prostate neuroendocrine carcinoma may emerge under androgen-receptor pathway treatment pressure; neither mechanism should be generalized to pulmonary LCNEC. No infectious agent is established as a universal LCNEC cause.

### Genetic susceptibility, protective factors, and gene–environment interaction

The recurrent alterations described below are overwhelmingly **somatic tumor alterations**, not inherited causal variants. No reproducible LCNEC-specific germline susceptibility locus, protective allele, founder mutation, carrier frequency, Mendelian inheritance pattern, anticipation, or consanguinity effect is established. Consequently, population allele frequencies and ACMG germline pathogenicity classifications are generally **not applicable** to the common tumor-driver profile.

No LCNEC-specific protective drug, diet, supplement, or exercise intervention has demonstrated risk reduction. Tobacco avoidance and cessation are the best-supported environmental protective measures by inference from the strong smoking association. Formal LCNEC-specific gene–environment interaction studies are lacking; tobacco exposure plausibly interacts with deficient TP53/RB1-mediated checkpoint control, but quantitative G×E estimates are unavailable.

## 3. Phenotypes

Pulmonary LCNEC is typically **adult/late-onset**, insidious, severe, and progressive. It may be detected incidentally. Presenting symptoms are nonspecific and include cough, chest pain, hemoptysis, dyspnea, constitutional decline, and manifestations of local compression. Suggested HPO mappings include **Cough (HP:0012735), Hemoptysis (HP:0002105), Dyspnea (HP:0002094), Chest pain (HP:0100749), Fatigue (HP:0012378),** and **Weight loss (HP:0001824)**. Exact frequency estimates for individual presenting symptoms are not robustly established. (yang2022pulmonarylargecell pages 2-3, yang2022pulmonarylargecell pages 1-2)

Disease commonly spreads to liver, bone, brain, adrenal glands, and lymph nodes. Suggested terms include **Neoplasm metastatic to liver (HP:0002896), Neoplasm metastatic to bone (HP:0002797),** and brain metastasis as a clinical-neoplasm annotation. In a 52-patient Vienna brain-metastasis cohort, **76.9%** were neurologically symptomatic: 24 had neurologic deficits, 18 increased intracranial pressure, and 6 seizures; 51.9% had one brain metastasis and 23% had more than three. Suggested HPO terms include **Seizure (HP:0001250), Increased intracranial pressure (HP:0002516), Headache (HP:0002315),** and focal neurologic deficit terms selected per manifestation. (popov2024clinicalcharacteristicstreatment pages 1-2)

Classic functioning-neuroendocrine syndromes are uncommon in pulmonary LCNEC. Hormonal laboratory abnormalities or paraneoplastic syndromes can occur in high-grade NEC generally, but LCNEC-specific frequencies are not established. Quality-of-life studies using EQ-5D, SF-36, or LCNEC-specific instruments are scarce; the principal impacts are respiratory limitation, neurologic disability from brain metastases, treatment toxicity, pain, impaired work/daily activity, and psychological burden.

## 4. Genetic and molecular information

### Somatic drivers and molecular classes

Reported pulmonary LCNEC mutation frequencies include **TP53 82.3%, RB1 39.1%, KEAP1 20.9%, STK11 18.2%, KRAS 12.7%, and EGFR 11.9%**. Open Targets additionally associates LCNEC with **SMARCA4, CDKN2A, BRAF,** and **IDH2**. These are tumor-level associations and do not prove germline causation. (OpenTargets Search: large cell neuroendocrine carcinoma, yang2022pulmonarylargecell pages 3-4)

Three practical genomic patterns are recognized:

1. **SCLC-like:** TP53/RB1 co-mutation, deletion, or protein loss; converges on defective p53-mediated DNA-damage responses and RB/E2F cell-cycle restriction.
2. **NSCLC-like:** often RB1-intact, with STK11, KEAP1, and/or KRAS alterations; these affect AMPK–mTOR metabolic sensing, NRF2 oxidative-stress regulation, and RAS–MAPK signaling.
3. **Carcinoid-like/rare:** MEN1-associated patterns, likely representing a biologically distinct minority or diagnostic boundary group. (popov2024clinicalcharacteristicstreatment pages 1-2, yang2022pulmonarylargecell pages 3-4, corti2024emergingtreatmentoptions pages 14-16)

Variants include missense and truncating mutations, deletions/copy-number loss, amplifications, and occasional rearrangements. Their exact HGVS distribution and gnomAD frequency are not meaningful without a specified case because they are heterogeneous somatic events. For clinical annotation, variants should be recorded using AMP/ASCO/CAP somatic tiers rather than automatically labeled germline “pathogenic” under ACMG criteria.

### 2024 lineage and target findings

A 2024 resection study of 146 pulmonary NECs identified a **POU2F3-dominant tuft-cell-like phenotype**. It included 14 POU2F3-dominant LCNECs, 27 ASCL1-dominant LCNECs, and 10 triple-negative LCNECs; no NEUROD1-dominant LCNEC was found. POU2F3-dominant SCLC and LCNEC overlapped morphologically and showed lower TTF-1, CEA, and conventional neuroendocrine-marker expression but higher BCL2, MYC, and KIT. POU2F3 correlated inversely with synaptophysin (ρ=−0.67) and positively with KIT (ρ=0.60). LCNEC-P showed RB1 loss in 64% versus 35% of LCNEC-non-P, although the difference was not significant. POU2F3-dominant NEC had better recurrence-free survival but all patients were smokers, underscoring a lineage–exposure relationship requiring validation. Published October 2024; [DOI/URL](https://doi.org/10.1097/PAS.0000000000002145). (jimbo2024pou2f3expressingsmallcell pages 1-9, jimbo2024pou2f3expressingsmallcell pages 21-27, jimbo2024pou2f3expressingsmallcell pages 27-32, jimbo2024pou2f3expressingsmallcell pages 9-15)

**DLL3**, an inhibitory Notch ligand downstream of ASCL1, is minimally expressed in most normal tissues but enriched in SCLC, LCNEC, and combined pulmonary NEC. A 2024 standardized-IHC study evaluated 548 suitable specimens and found heterogeneous expression across pulmonary and extrapulmonary high-grade NENs. Another stage-IV LCNEC cohort reported DLL3-high expression in 74%, including 6/6 STK11-mutant and 10/11 KEAP1-mutant tumors. Published November 2024; [DOI/URL](https://doi.org/10.1038/s41698-024-00739-y). (serrano2024deltalikeligand3 pages 1-2, serrano2024deltalikeligand3 pages 10-11, peddio2024dll3asa pages 1-3)

A February 2024 targeted-sequencing study of **257 patients**—99 GEP-NECs, 57 lung NECs, and 101 digestive adenocarcinomas—showed organ-specific biology: TERT amplification in gastric NEC, KRAS mutation in colorectal NEC, and ARID1A mutation in biliary NEC; small- versus large-cell NEC differed in KEAP1 and CDH1. Potentially targetable alterations/biomarkers occurred in **22.2%** of GEP-NECs. Genotype-matched treatment was associated with PFS of 12.5 versus 3.0 months (HR 0.40; p=0.006), though this nonrandomized result is vulnerable to selection bias. [DOI/URL](https://doi.org/10.21147/j.issn.1000-9604.2024.01.09). (zhang2024molecularfeaturesof pages 1-2)

### Epigenetic and structural information

SMARCA4 loss implicates SWI/SNF chromatin-remodeling dysfunction; POU2F3, ASCL1, and NEUROD1 identify lineage-regulatory states rather than single causal lesions. However, LCNEC-specific methylome, histone-mark, chromatin-accessibility, single-cell, spatial-transcriptomic, proteomic, metabolomic, and lipidomic datasets remain limited. No recurrent pathognomonic translocation or aneuploidy defines LCNEC. Copy-number losses of RB1/CDKN2A and amplifications such as TERT or MYC-family changes may occur, depending on site and subtype.

## 5. Environmental and lifestyle information

Tobacco smoke is the principal established exposure for pulmonary LCNEC. No LCNEC-specific evidence establishes alcohol, diet, exercise, ambient pollution, radiation, occupational toxins, or infection as independent causal factors, although standard lung-cancer risks remain biologically plausible. For cervical LCNEC, HPV testing is relevant; for pulmonary LCNEC, HPV is not an established cause. There is no zoonotic or transmissible component.

## 6. Mechanism and pathophysiology

### Causal chain

**Upstream:** carcinogenic exposure or site-specific oncogenic pressure produces somatic mutations and copy-number changes. **Core transformation:** loss of TP53 disables DNA-damage checkpoints and apoptosis; RB1 loss releases E2F-driven S-phase entry. In NSCLC-like disease, STK11 loss alters AMPK/mTOR control, KEAP1 loss activates NRF2-dependent antioxidant programs, and KRAS activates MAPK signaling. **Lineage specification:** ASCL1/NEUROD1 or POU2F3 programs establish neuroendocrine or tuft-cell-like states; ASCL1 can induce DLL3, which suppresses Notch signaling. **Downstream:** unchecked cell cycling, genomic instability, resistance to apoptosis, metabolic adaptation, extensive necrosis, stromal remodeling, invasion, hematogenous dissemination, and treatment resistance produce the observed aggressive phenotype. (yang2022pulmonarylargecell pages 3-4, serrano2024deltalikeligand3 pages 1-2, jimbo2024pou2f3expressingsmallcell pages 1-9)

Relevant GO suggestions include **regulation of cell cycle (GO:0051726), DNA damage response (GO:0006974), apoptotic process (GO:0006915), MAPK cascade (GO:0000165), response to oxidative stress (GO:0006979), Notch signaling pathway (GO:0007219), neuroendocrine cell differentiation, angiogenesis (GO:0001525),** and **cell migration (GO:0016477)**. Cell Ontology suggestions include **pulmonary neuroendocrine cell (CL:0000450)**, epithelial cell, tuft cell, T lymphocyte, macrophage, endothelial cell, and fibroblast; the exact cell of origin is not conclusively established.

Immune involvement is heterogeneous. CD8-positive T-cell infiltration has been associated with prognosis, but STK11/KEAP1-altered tumors may exhibit relatively immune-cold biology. PD-L1 and tumor-mutational burden are imperfect predictive biomarkers. DLL3’s restricted surface expression provides a route for bispecific T-cell engagers, CAR-T cells, antibody–drug conjugates, or radioligands. (yang2022pulmonarylargecell pages 7-8, serrano2024deltalikeligand3 pages 1-2, serrano2024deltalikeligand3 pages 10-11)

Subcellular ontology suggestions include **nucleus (GO:0005634)** for TP53/RB1/transcriptional programs, **chromatin (GO:0000785)** for SMARCA4 dysfunction, **plasma membrane (GO:0005886)** for DLL3/KIT/receptor targets, and **mitochondrion (GO:0005739)** for oxidative/metabolic adaptation.

## 7. Anatomical structures affected

Pulmonary LCNEC usually arises as a peripheral lung mass, often in an upper lobe and frequently the right upper lobe. Mediastinal and hilar lymph-node involvement is common. Suggested UBERON annotations are **lung (UBERON:0002048), lung lobe, bronchus (UBERON:0002185), pulmonary epithelium, hilar lymph node,** and **mediastinal lymph node**. Imaging may show lobulation, irregular or spiculated margins, emphysema, notching, pleural indentation, cavitation, and nodal enlargement. No consistent lateralization exists. (yang2022pulmonarylargecell pages 2-3, yang2022pulmonarylargecell pages 7-8)

Secondary organs include brain, liver, skeleton, adrenal gland, and lymphatic sites. Extrapulmonary LCNEC can arise in essentially any epithelial organ; approximately 37% of extrapulmonary NECs occur in the gastroenteropancreatic tract, followed by genitourinary and gynecologic systems. This 37% statistic concerns EP-NEC overall, not LCNEC alone. (stumpo2023extrapulmonaryneuroendocrinecarcinomas pages 15-17)

## 8. Temporal development

Onset is usually insidious in older adults rather than congenital or pediatric. LCNEC progresses rapidly and is often regionally advanced or metastatic at recognition. Pulmonary disease is staged with the lung-cancer TNM system; extrapulmonary disease uses the relevant organ-specific TNM framework.

Postoperative recurrence is frequent: **63.9%–82% within one year and 91% within two years** in reported series, commonly involving mediastinal or supraclavicular nodes. Remission is generally treatment-induced, not spontaneous, and relapse after platinum sensitivity is common. The principal intervention window is complete resection of localized disease followed by consideration of adjuvant systemic treatment; in advanced disease, early molecular profiling and clinical-trial referral are important because durable standard options are limited. (yang2022pulmonarylargecell pages 7-8)

## 9. Inheritance and population epidemiology

Pulmonary LCNEC represents approximately **0.3%–3% of lung cancers** and **2.1%–3.5% of surgically resected lung cancers**. Incidence may be underestimated because cytology and small biopsies commonly misclassify it. Patients are predominantly men, heavy smokers, and age 60–70 years. Robust population incidence per 100,000 person-years, prevalence, ethnicity-specific rates, and geographic variation are not consistently established. (yang2022pulmonarylargecell pages 2-3)

LCNEC is sporadic and somatically driven; inheritance, penetrance, expressivity, anticipation, germline mosaicism, founder effects, carrier frequency, and consanguinity are not applicable to typical cases. Genetic counseling is indicated only when personal/family history or tumor findings suggest an independent hereditary cancer syndrome.

## 10. Diagnostics

### Pathology and immunohistochemistry

WHO 2021 pulmonary criteria require neuroendocrine architecture, large-cell cytology, and **>10 mitoses/2 mm²**, typically 60–80/2 mm²; necrosis is often extensive. At least one neuroendocrine marker—**synaptophysin, chromogranin A, or CD56/NCAM1**—should support differentiation. **INSM1** is positive in approximately 68%–91.3% and is a useful nuclear adjunct; TTF-1 is positive in approximately 54.8%. Ki-67 is usually high and useful in crushed biopsies but does not independently establish LCNEC. (yang2022pulmonarylargecell pages 2-3, yang2022pulmonarylargecell pages 3-4)

Small biopsies are problematic because architecture, mitotic rate, necrosis, and cytologic size may be undersampled. Expert thoracic-pathology review and sufficient tissue are therefore valuable. POU2F3 IHC can identify a neuroendocrine-marker-low tuft-cell-like group and explain SCLC/LCNEC overlap. (jimbo2024pou2f3expressingsmallcell pages 1-9, jimbo2024pou2f3expressingsmallcell pages 27-32)

### Imaging, laboratory tests, and biomarkers

Contrast-enhanced chest CT defines the primary tumor and nodes; FDG-PET/CT supports systemic staging. Brain MRI is appropriate for neurologic symptoms and generally for advanced disease because brain metastases occur in approximately 19.2%–20% overall and up to 35% of stage-IV cases. CT/MRI of abdomen and pelvis evaluates liver and adrenal spread. Somatostatin-receptor imaging is less consistently informative than in well-differentiated NET and should be individualized. (popov2024clinicalcharacteristicstreatment pages 1-2)

Routine blood counts, renal/hepatic function, electrolytes, and treatment-baseline tests are necessary but nonspecific. CEA, NSE, proGRP, chromogranin A, and circulating tumor DNA can be investigated, but no serum biomarker is sufficiently sensitive and specific for diagnosis or screening. Liquid biopsy is promising for tumor genotyping and monitoring but is not a histologic substitute.

### Molecular testing

For advanced disease, a broad somatic NGS panel is reasonable, including **TP53, RB1, STK11, KEAP1, KRAS, BRAF, EGFR, ALK, RET, NTRK1/2/3, ERBB2, MET, IDH2, SMARCA4, CDKN2A, APC, ARID1A,** and MSI/TMB assessment. RB1 status may help choose an SCLC-like versus NSCLC-like chemotherapy strategy, although this remains incompletely validated. WES/WGS and RNA-seq can detect uncommon fusions or clarify lineage but are not routine diagnostic necessities; CMA, karyotyping, mitochondrial testing, and repeat-expansion testing have no standard role. (OpenTargets Search: large cell neuroendocrine carcinoma, corti2024emergingtreatmentoptions pages 14-16, zhang2024molecularfeaturesof pages 1-2)

### Differential diagnosis and screening

The differential includes SCLC, basaloid or poorly differentiated squamous carcinoma, adenocarcinoma with focal neuroendocrine-marker expression, carcinoid/NET G3, SMARCA4-deficient thoracic tumor, lymphoma, melanoma, and metastatic NEC. A non-neuroendocrine NSCLC component supports combined LCNEC; an SCLC component is classified as combined SCLC. (yang2022pulmonarylargecell pages 3-4)

There is no LCNEC-specific population screening test. Eligible smokers should receive standard low-dose CT lung-cancer screening according to national criteria; suspicious lesions still require tissue diagnosis.

## 11. Outcome and prognosis

Pulmonary LCNEC has survival comparable to SCLC and poorer than most conventional NSCLCs. Reported stage-I five-year survival ranges widely from **27% to 67%**, reflecting cohort selection and treatment differences. Adverse factors include advanced TNM stage, larger tumor, older age, high neutrophil-to-lymphocyte ratio, prior malignancy, distant metastasis, and synchronous brain metastasis; immune infiltration, KEAP1 status, POU2F3 phenotype, and RB1 status are investigational modifiers. (yang2022pulmonarylargecell pages 7-8, jimbo2024pou2f3expressingsmallcell pages 1-9)

In the 2024 Vienna cohort, median OS was **16 months from LCNEC diagnosis** and **7 months after brain-metastasis diagnosis**. Synchronous brain metastasis conferred median OS of 11 versus 27 months for metachronous disease (p=0.003). The paper’s abstract states: **“Patients with LCNEC and BM have a poor prognosis, particularly when synchronous BM are present.”** Published online 8 December 2023; journal issue 2024; [DOI/URL](https://doi.org/10.1007/s10585-023-10250-6). (popov2024clinicalcharacteristicstreatment pages 1-2)

Long-term morbidity includes recurrent thoracic disease, respiratory compromise, pain, neurologic disability, treatment-related cytopenias/neuropathy/renal injury, and reduced independence. LCNEC-specific validated quality-of-life statistics and disability weights are not available.

## 12. Treatment

### Localized pulmonary LCNEC

Complete anatomic resection—typically lobectomy with systematic nodal evaluation—is favored when operable. Surgery alone is often inadequate because of early recurrence, so platinum-based adjuvant chemotherapy is commonly considered, especially for stage II–III and high-risk stage I disease. Evidence remains mostly retrospective. A 2024 real-world resection study of pulmonary high-grade NEC found early stage, younger age, minimally invasive surgery, and normal preoperative CEA favorable; within LCNEC, VATS was associated with improved OS and DFS, but causal interpretation is limited by selection bias. [DOI/URL](https://doi.org/10.1186/s13023-024-03240-8). (yang2022pulmonarylargecell pages 7-8)

Suggested NCIt intervention mappings: **Lobectomy; Pneumonectomy; Lymph Node Dissection; Cisplatin; Carboplatin; Etoposide; Adjuvant Chemotherapy.**

### Advanced pulmonary LCNEC

Platinum–etoposide remains the most commonly used first-line regimen. Small retrospective series report ORRs of **50%–73%** and median OS of **9.2–44 months**, with substantial heterogeneity. Platinum–irinotecan is an alternative. Molecularly, TP53/RB1-altered tumors may behave more SCLC-like, whereas RB1-wild-type/STK11–KEAP1–KRAS tumors may benefit more from an NSCLC-type platinum–gemcitabine or platinum–taxane regimen; this is an expert precision-oncology strategy, not a universally proven standard. Second-line amrubicin produced ORR **27.7%** and median OS **5.1 months** in one report. (yang2022pulmonarylargecell pages 5-7, corti2024emergingtreatmentoptions pages 14-16)

Thoracic radiotherapy was not associated with an OS benefit in stage I–II retrospective analyses but was beneficial in stage III (p<0.001). In stage III–IV cohorts, chest radiotherapy plus prophylactic cranial irradiation was associated with median PFS of 20.5 versus 6.4 months and OS of 33.4 versus 8.6 months, although PCI comparisons were not unequivocally significant. Brain metastases are treated with resection, stereotactic radiosurgery, whole-brain radiotherapy, and systemic therapy according to number, size, symptoms, and extracranial control. Routine prophylactic cranial irradiation is not established for LCNEC. (popov2024clinicalcharacteristicstreatment pages 1-2, yang2022pulmonarylargecell pages 5-7)

### Immunotherapy and targeted therapy

Retrospective pulmonary data suggest activity of PD-1/PD-L1 blockade: one series reported partial remission in 60% of PD-L1-positive patients; another found median OS of 12.4 versus 6.0 months with versus without checkpoint inhibition. These observations are nonrandomized and cannot establish efficacy. (yang2022pulmonarylargecell pages 5-7)

Actionable alterations should be treated according to tumor-agnostic or organ-specific evidence where appropriate: BRAF V600E, KRAS G12C, NTRK/ALK/RET fusions, MSI-high/dMMR, TMB-high, and selected EGFR or ERBB2 alterations. In small NEN subsets, NTRK inhibitors achieved ORR 40% among five patients; pralsetinib produced responses in two of three RET-fusion NENs. Such tiny basket subsets support testing, not LCNEC-wide efficacy. (corti2024emergingtreatmentoptions pages 14-16)

DLL3 is a leading emerging target. Its high prevalence and minimal normal-tissue expression support bispecific antibodies, CAR-T cells, antibody–drug conjugates, and alpha-radioligands. However, expression is heterogeneous and LCNEC-specific response data remain immature. In platinum-treated LCNEC, DLL3 positivity did not significantly alter five-year OS (58.3% versus 35.7%; p=0.36) or recurrence-free survival (41.7% versus 35.7%; p=0.74). (serrano2024deltalikeligand3 pages 1-2, serrano2024deltalikeligand3 pages 10-11, peddio2024dll3asa pages 1-3)

### Extrapulmonary LCNEC

Localized disease may receive surgery or chemoradiation. Advanced extrapulmonary poorly differentiated NEC is generally treated with platinum–etoposide, mirroring SCLC; no consensus second-line standard exists. Site, morphology, Ki-67, molecular profile, organ function, and performance status should guide subsequent FOLFIRI, FOLFOX, taxane/irinotecan, temozolomide-based, immunotherapy, or targeted approaches. A 2023 review’s abstract accurately summarizes current expert opinion: **“Platinum-based chemotherapy currently represents the standard of care for EP-NECs of any site.”** Published December 2023; [DOI/URL](https://doi.org/10.3390/jcm12247715). (stumpo2023extrapulmonaryneuroendocrinecarcinomas pages 15-17)

### Current trials and advanced therapeutics

- **NCT05470595:** phase II, single-arm atezolizumab plus platinum/etoposide for advanced pulmonary LCNEC; 67 participants; active, not recruiting. Exact registry title: “A Single-arm Trial of Atezolizumab/Platinum/Etoposide for the Treatment of Advanced Large-cell Neuroendocrine Cancer of the Lung.” [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT05470595). (NCT05470595 chunk 2)
- **NCT06418087:** phase II durvalumab with carboplatin/etoposide in pulmonary LCNEC; recruiting; planned n=49. [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT06418087).
- **NCT06393816 (FIRST-NEC):** phase II durvalumab plus platinum/etoposide in NEC; recruiting; planned n=80. [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT06393816).
- **NCT06049966:** phase I atezolizumab in LCNEC; completed; n=22. [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT06049966).
- **NCT06736418:** phase I ^225Ac-ABD147 in previously platinum-treated SCLC or pulmonary LCNEC; active, not recruiting; n=17. [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT06736418).
- **NCT04079712:** phase II cabozantinib plus nivolumab/ipilimumab in poorly differentiated NEC; active, not recruiting; n=17. [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT04079712).
- **NCT05680922:** phase I LB2102 DLL3-directed CAR-T therapy is principally an extensive-stage SCLC study, not an established LCNEC trial; active, not recruiting; n=41. [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT05680922). Its exact title is “DLL3-Directed Chimeric Antigen Receptor T-cells in Subjects With Extensive Stage Small Cell Lung Cancer.” (NCT05680922 chunk 2)

No approved gene-replacement, CRISPR, antisense, siRNA, or LCNEC-specific cell therapy exists. Toxicity follows the intervention: platinum causes myelosuppression, nephrotoxicity, ototoxicity, and neuropathy; etoposide causes marrow suppression and alopecia; checkpoint blockade causes immune-related adverse events; DLL3 T-cell engagers/CAR-T approaches can cause cytokine-release and neurotoxicity syndromes.

## 13. Prevention

**Primary prevention:** avoid tobacco initiation, promote cessation, and reduce secondhand-smoke and occupational carcinogen exposure. No LCNEC-specific vaccine or chemopreventive agent exists.

**Secondary prevention:** no LCNEC-specific screening program exists. Standard low-dose CT screening for eligible high-risk smokers may detect pulmonary LCNEC incidentally. There is no newborn, carrier, prenatal, preimplantation, or cascade screening indication for sporadic LCNEC.

**Tertiary prevention:** complete staging, smoking cessation after diagnosis, vaccination and infection prevention during systemic therapy, thromboembolism assessment, surveillance imaging, early management of brain metastases, nutrition, pain/palliative care, and rehabilitation can reduce complications. Prophylactic cranial irradiation is not established routinely.

## 14. Other species and natural disease

Naturally occurring neuroendocrine carcinomas are reported in veterinary species, but no well-defined breed-specific, epidemiologically validated natural LCNEC counterpart was established in the retrieved evidence. Consequently, VBO breed identifiers, veterinary incidence, and conserved spontaneous causal variants cannot be assigned confidently. LCNEC is neither infectious nor zoonotic and has no cross-species transmission.

Orthologs of key drivers—including **Trp53, Rb1, Stk11, Keap1, Kras, Smarca4,** and **Pou2f3**—are conserved in *Mus musculus* (NCBI Taxonomy **10090**), supporting mechanistic modeling, but orthology does not imply inherited natural disease.

## 15. Model organisms and experimental systems

### Pulmonary LCNEC models

Recuero et al. developed the **46LCNEC** murine line from spontaneous LCNEC arising in a CMV-QKO genetically engineered mouse model. It forms syngeneic allografts in immunocompetent and immunodeficient mice, retains the parental LCNEC transcriptomic signature, grows rapidly, and permits controlled efficacy and immunotherapy studies. The abstract states: **“RNA-seq analysis demonstrated that our cell lines and syngeneic tumors maintained the transcriptome program from the original transgenic primary tumor and displayed strong similarities to human SCLC or LCNEC.”** Published October 2023; [DOI/URL](https://doi.org/10.3390/ijms242015284). (recuero2023novelmousecell pages 1-2, recuero2023novelmousecell pages 7-8)

The model’s strengths are reproducibility, high penetrance, defined tumor number, low relative cost, and an intact immune system in syngeneic hosts. Limitations are murine biology, incomplete human genomic heterogeneity, and multifocal GEMM tumors at different progression stages, which can bias response assessment. (recuero2023novelmousecell pages 7-8)

### Extrapulmonary models

**HROC57** is a BRAF-mutant colorectal large-cell NEC cell-line/PDX pair. It was sensitive to etoposide, cisplatin, and 5-fluorouracil and resistant to rapamycin, broadly paralleling clinical NEC sensitivity. Colorectal NEC organoids formed a distinct transcriptomic group; both analyzed organoids carried TP53 mutations, while one also carried APC, BRAF, and KRAS alterations. WNT/R-spondin dependence varied with APC genotype. (detjen2021modelsofgastroenteropancreatic pages 9-10)

Patient-derived NEC PDXs NEC913 and NEC1452 had >80% Ki-67 positivity and TP53/RB1 loss; NEC913 retained SSTR2 and enabled octreotide-targeted imaging, whereas NEC1452 was SSTR2-negative. These represent high-grade GEP-NEC rather than universally validated LCNEC models.

Across the field, cell lines enable perturbation and drug screening; organoids preserve genotype–phenotype relationships; PDXs preserve tumor architecture but lack an intact human immune system; syngeneic models permit immunology; and GEMMs address initiation/evolution but may not reproduce human tobacco mutagenesis. Model scarcity and inconsistent molecular characterization remain major barriers.

## Knowledge-base conclusions and evidence gaps

1. **LCNEC is a pathology-defined, high-grade somatic cancer**, not a Mendelian disease. Pulmonary and extrapulmonary forms should receive distinct site annotations.
2. **TP53/RB1 versus STK11/KEAP1/KRAS biology** is the most clinically relevant molecular division, but prospective treatment assignment remains unproven. (popov2024clinicalcharacteristicstreatment pages 1-2, yang2022pulmonarylargecell pages 3-4, corti2024emergingtreatmentoptions pages 14-16)
3. **2024 developments** include POU2F3-defined tuft-cell-like LCNEC, cross-tissue genomic comparisons, broad DLL3 profiling, and dedicated pulmonary chemoimmunotherapy trials. (serrano2024deltalikeligand3 pages 1-2, zhang2024molecularfeaturesof pages 1-2, jimbo2024pou2f3expressingsmallcell pages 1-9)
4. Histology plus neuroendocrine IHC remains essential; genomics supplements but does not replace morphology.
5. Major gaps include LCNEC-specific incidence per 100,000, prospective randomized treatment data, validated predictive biomarkers, patient-reported outcomes, germline/G×E evidence, epigenomic and spatial/single-cell atlases, and representative human models.

References

1. (yang2022pulmonarylargecell pages 2-3): Lan Yang, Ying Fan, and Hongyang Lu. Pulmonary large cell neuroendocrine carcinoma. Pathology and Oncology Research, Oct 2022. URL: https://doi.org/10.3389/pore.2022.1610730, doi:10.3389/pore.2022.1610730. This article has 54 citations.

2. (yang2022pulmonarylargecell pages 1-2): Lan Yang, Ying Fan, and Hongyang Lu. Pulmonary large cell neuroendocrine carcinoma. Pathology and Oncology Research, Oct 2022. URL: https://doi.org/10.3389/pore.2022.1610730, doi:10.3389/pore.2022.1610730. This article has 54 citations.

3. (stumpo2023extrapulmonaryneuroendocrinecarcinomas pages 15-17): Sara Stumpo, Maria Giovanna Formelli, Irene Persano, Elena Parlagreco, Eleonora Lauricella, Maria Grazia Rodriquenz, Luigi Pio Guerrera, Ina Valeria Zurlo, Davide Campana, Maria Pia Brizzi, Mauro Cives, Anna La Salvia, and Giuseppe Lamberti. Extrapulmonary neuroendocrine carcinomas: current management and future perspectives. Dec 2023. URL: https://doi.org/10.3390/jcm12247715, doi:10.3390/jcm12247715. This article has 26 citations.

4. (yang2022pulmonarylargecell pages 3-4): Lan Yang, Ying Fan, and Hongyang Lu. Pulmonary large cell neuroendocrine carcinoma. Pathology and Oncology Research, Oct 2022. URL: https://doi.org/10.3389/pore.2022.1610730, doi:10.3389/pore.2022.1610730. This article has 54 citations.

5. (zhang2024molecularfeaturesof pages 1-2): Jianwei Zhang, Hanxiao Chen, Junli Zhang, Sha Wang, Yanfang Guan, Wenguang Gu, Jie Li, Xiaotian Zhang, Jian Li, Xicheng Wang, Zhihao Lu, Jun Zhou, Zhi Peng, Yu Sun, Yang Shao, Lin Shen, Minglei Zhuo, and Ming Lu. Molecular features of gastroenteropancreatic neuroendocrine carcinoma: a comparative analysis with lung neuroendocrine carcinoma and digestive adenocarcinomas. Chinese journal of cancer research = Chung-kuo yen cheng yen chiu, 36 1:90-102, Feb 2024. URL: https://doi.org/10.21147/j.issn.1000-9604.2024.01.09, doi:10.21147/j.issn.1000-9604.2024.01.09. This article has 6 citations.

6. (OpenTargets Search: large cell neuroendocrine carcinoma): Open Targets Query (large cell neuroendocrine carcinoma, 23 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

7. (jimbo2024pou2f3expressingsmallcell pages 1-9): Naoe Jimbo, Chiho Ohbayashi, Maiko Takeda, Tomomi Fujii, Suguru Mitsui, Ryuko Tsukamoto, Yugo Tanaka, Tomoo Itoh, and Yoshimasa Maniwa. Pou2f3-expressing small cell lung carcinoma and large cell neuroendocrine carcinoma show morphologic and phenotypic overlap. The American Journal of Surgical Pathology, 48:4-15, Oct 2024. URL: https://doi.org/10.1097/pas.0000000000002145, doi:10.1097/pas.0000000000002145. This article has 29 citations.

8. (popov2024clinicalcharacteristicstreatment pages 1-2): Petar Popov, Ariane Steindl, Ladislaia Wolff, Elisabeth S. Bergen, Franziska Eckert, Josa M Frischer, Georg Widhalm, Thorsten Fuereder, Markus Raderer, Anna S. Berghoff, Matthias Preusser, and Barbara Kiesewetter. Clinical characteristics, treatment, and outcome of patients with large cell neuroendocrine carcinoma of the lung and brain metastases – data from a tertiary care center. Clinical & Experimental Metastasis, 41:25-32, Dec 2024. URL: https://doi.org/10.1007/s10585-023-10250-6, doi:10.1007/s10585-023-10250-6. This article has 13 citations and is from a peer-reviewed journal.

9. (corti2024emergingtreatmentoptions pages 14-16): Francesca Corti, Roberta Elisa Rossi, Pietro Cafaro, Gaia Passarella, Antonella Turla, Sara Pusceddu, Jorgelina Coppa, Simone Oldani, Alessandro Guidi, Raffaella Longarini, and Diego Luigi Cortinovis. Emerging treatment options for neuroendocrine neoplasms of unknown primary origin: current evidence and future perspectives. Cancers, 16:2025, May 2024. URL: https://doi.org/10.3390/cancers16112025, doi:10.3390/cancers16112025. This article has 5 citations.

10. (yang2022pulmonarylargecell pages 9-9): Lan Yang, Ying Fan, and Hongyang Lu. Pulmonary large cell neuroendocrine carcinoma. Pathology and Oncology Research, Oct 2022. URL: https://doi.org/10.3389/pore.2022.1610730, doi:10.3389/pore.2022.1610730. This article has 54 citations.

11. (jimbo2024pou2f3expressingsmallcell pages 27-32): Naoe Jimbo, Chiho Ohbayashi, Maiko Takeda, Tomomi Fujii, Suguru Mitsui, Ryuko Tsukamoto, Yugo Tanaka, Tomoo Itoh, and Yoshimasa Maniwa. Pou2f3-expressing small cell lung carcinoma and large cell neuroendocrine carcinoma show morphologic and phenotypic overlap. The American Journal of Surgical Pathology, 48:4-15, Oct 2024. URL: https://doi.org/10.1097/pas.0000000000002145, doi:10.1097/pas.0000000000002145. This article has 29 citations.

12. (yang2022pulmonarylargecell pages 7-8): Lan Yang, Ying Fan, and Hongyang Lu. Pulmonary large cell neuroendocrine carcinoma. Pathology and Oncology Research, Oct 2022. URL: https://doi.org/10.3389/pore.2022.1610730, doi:10.3389/pore.2022.1610730. This article has 54 citations.

13. (yang2022pulmonarylargecell pages 5-7): Lan Yang, Ying Fan, and Hongyang Lu. Pulmonary large cell neuroendocrine carcinoma. Pathology and Oncology Research, Oct 2022. URL: https://doi.org/10.3389/pore.2022.1610730, doi:10.3389/pore.2022.1610730. This article has 54 citations.

14. (serrano2024deltalikeligand3 pages 1-2): Alejandra G. Serrano, Pedro Rocha, Cibelle Freitas Lima, Allison Stewart, Bingnan Zhang, Lixia Diao, Junya Fujimoto, Robert J. Cardnell, Wei Lu, Khaja Khan, Beate Sable, Aaron R. Ellison, Ignacio I. Wistuba, Kyle F. Concannon, Daniel M. Halperin, Czerniak Bogdan, Kanishka Sircar, Miao Zhang, Kasey Cargill, Qi Wang, Ana Aparicio, Alexander Lazar, Sharia Hernandez, Jeannelyn Estrella, Preetha Ramalingam, Adel El-Naggar, Neda Kalhor, Carl M. Gay, Lauren Averett Byers, and Luisa M. Solis Soto. Delta-like ligand 3 (dll3) landscape in pulmonary and extra-pulmonary neuroendocrine neoplasms. NPJ Precision Oncology, Nov 2024. URL: https://doi.org/10.1038/s41698-024-00739-y, doi:10.1038/s41698-024-00739-y. This article has 46 citations and is from a peer-reviewed journal.

15. (robinson2023futuretherapeuticstrategies pages 14-14): Matthew D. Robinson, Daniel Livesey, Richard A. Hubner, Juan W. Valle, and Mairéad G. McNamara. Future therapeutic strategies in the treatment of extrapulmonary neuroendocrine carcinoma: a review. Therapeutic Advances in Medical Oncology, Jan 2023. URL: https://doi.org/10.1177/17588359231156870, doi:10.1177/17588359231156870. This article has 14 citations and is from a peer-reviewed journal.

16. (peddio2024dll3asa pages 1-3): Annarita Peddio, Erica Pietroluongo, Maria Rosaria Lamia, Angelo Luciano, Aldo Caltavituro, Roberto Buonaiuto, Giovanna Pecoraro, Pietro De Placido, Giovannella Palmieri, Roberto Bianco, Mario Giuliano, and Alberto Servetto. Dll3 as a potential diagnostic and therapeutic target in neuroendocrine neoplasms: a narrative review. Critical Reviews in Oncology/Hematology, 204:104524, Dec 2024. URL: https://doi.org/10.1016/j.critrevonc.2024.104524, doi:10.1016/j.critrevonc.2024.104524. This article has 29 citations.

17. (NCT05470595 chunk 2):  A Single-arm Trial of Atezolizumab/Platinum/Etoposide for the Treatment of Advanced Large-cell Neuroendocrine Cancer of the Lung. Technische Universität Dresden. 2022. ClinicalTrials.gov Identifier: NCT05470595

18. (robinson2023futuretherapeuticstrategies pages 17-18): Matthew D. Robinson, Daniel Livesey, Richard A. Hubner, Juan W. Valle, and Mairéad G. McNamara. Future therapeutic strategies in the treatment of extrapulmonary neuroendocrine carcinoma: a review. Therapeutic Advances in Medical Oncology, Jan 2023. URL: https://doi.org/10.1177/17588359231156870, doi:10.1177/17588359231156870. This article has 14 citations and is from a peer-reviewed journal.

19. (recuero2023novelmousecell pages 1-2): Enrique Recuero, Sara Lázaro, Corina Lorz, Ana Belén Enguita, Ramón Garcia-Escudero, and Mirentxu Santos. Novel mouse cell lines and in vivo models for human high-grade neuroendocrine lung carcinoma, small cell lung carcinoma (sclc), and large cell neuroendocrine carcinoma (lcnec). International Journal of Molecular Sciences, 24(20):15284, Oct 2023. URL: https://doi.org/10.3390/ijms242015284, doi:10.3390/ijms242015284. This article has 8 citations.

20. (detjen2021modelsofgastroenteropancreatic pages 9-10): Katharina Detjen, Linda Hammerich, Burcin Özdirik, Münevver Demir, Bertram Wiedenmann, Frank Tacke, Henning Jann, and Christoph Roderburg. Models of gastroenteropancreatic neuroendocrine neoplasms: current status and future directions. Neuroendocrinology, 111:217-236, Jul 2021. URL: https://doi.org/10.1159/000509864, doi:10.1159/000509864. This article has 30 citations and is from a peer-reviewed journal.

21. (recuero2023novelmousecell pages 7-8): Enrique Recuero, Sara Lázaro, Corina Lorz, Ana Belén Enguita, Ramón Garcia-Escudero, and Mirentxu Santos. Novel mouse cell lines and in vivo models for human high-grade neuroendocrine lung carcinoma, small cell lung carcinoma (sclc), and large cell neuroendocrine carcinoma (lcnec). International Journal of Molecular Sciences, 24(20):15284, Oct 2023. URL: https://doi.org/10.3390/ijms242015284, doi:10.3390/ijms242015284. This article has 8 citations.

22. (jimbo2024pou2f3expressingsmallcell pages 21-27): Naoe Jimbo, Chiho Ohbayashi, Maiko Takeda, Tomomi Fujii, Suguru Mitsui, Ryuko Tsukamoto, Yugo Tanaka, Tomoo Itoh, and Yoshimasa Maniwa. Pou2f3-expressing small cell lung carcinoma and large cell neuroendocrine carcinoma show morphologic and phenotypic overlap. The American Journal of Surgical Pathology, 48:4-15, Oct 2024. URL: https://doi.org/10.1097/pas.0000000000002145, doi:10.1097/pas.0000000000002145. This article has 29 citations.

23. (jimbo2024pou2f3expressingsmallcell pages 9-15): Naoe Jimbo, Chiho Ohbayashi, Maiko Takeda, Tomomi Fujii, Suguru Mitsui, Ryuko Tsukamoto, Yugo Tanaka, Tomoo Itoh, and Yoshimasa Maniwa. Pou2f3-expressing small cell lung carcinoma and large cell neuroendocrine carcinoma show morphologic and phenotypic overlap. The American Journal of Surgical Pathology, 48:4-15, Oct 2024. URL: https://doi.org/10.1097/pas.0000000000002145, doi:10.1097/pas.0000000000002145. This article has 29 citations.

24. (serrano2024deltalikeligand3 pages 10-11): Alejandra G. Serrano, Pedro Rocha, Cibelle Freitas Lima, Allison Stewart, Bingnan Zhang, Lixia Diao, Junya Fujimoto, Robert J. Cardnell, Wei Lu, Khaja Khan, Beate Sable, Aaron R. Ellison, Ignacio I. Wistuba, Kyle F. Concannon, Daniel M. Halperin, Czerniak Bogdan, Kanishka Sircar, Miao Zhang, Kasey Cargill, Qi Wang, Ana Aparicio, Alexander Lazar, Sharia Hernandez, Jeannelyn Estrella, Preetha Ramalingam, Adel El-Naggar, Neda Kalhor, Carl M. Gay, Lauren Averett Byers, and Luisa M. Solis Soto. Delta-like ligand 3 (dll3) landscape in pulmonary and extra-pulmonary neuroendocrine neoplasms. NPJ Precision Oncology, Nov 2024. URL: https://doi.org/10.1038/s41698-024-00739-y, doi:10.1038/s41698-024-00739-y. This article has 46 citations and is from a peer-reviewed journal.

25. (NCT05680922 chunk 2):  DLL3-Directed Chimeric Antigen Receptor T-cells in Subjects With Extensive Stage Small Cell Lung Cancer. Legend Biotech USA Inc. 2023. ClinicalTrials.gov Identifier: NCT05680922

## Artifacts

- [Edison artifact artifact-00](Large_Cell_Neuroendocrine_Carcinoma-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 30 |
| Resolved | 29 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 1 |
| Unverifiable | 0 |

### Obsolete terms

These terms are real but deprecated. Citing one is not a fabrication; it does mean the report is naming something the ontology has retired:

- `CL:0000450` (CL_0000450) (1 mention) - replaced by `CL:0000136`

29 of 30 terms resolved to a current term; the rest could not be looked up either way.
