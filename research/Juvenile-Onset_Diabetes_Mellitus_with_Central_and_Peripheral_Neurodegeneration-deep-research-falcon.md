---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-20T07:12:18.616341'
end_time: '2026-08-20T07:22:04.594691'
duration_seconds: 585.98
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Juvenile-Onset Diabetes Mellitus With Central and Peripheral Neurodegeneration
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 18
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 5
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Juvenile-Onset_Diabetes_Mellitus_with_Central_and_Peripheral_Neurodegeneration-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Juvenile-Onset Diabetes Mellitus With Central and Peripheral Neurodegeneration
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Juvenile-Onset Diabetes Mellitus With Central and Peripheral Neurodegeneration** covering all of the
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
- **Disease Name:** Juvenile-Onset Diabetes Mellitus With Central and Peripheral Neurodegeneration
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Juvenile-Onset Diabetes Mellitus With Central and Peripheral Neurodegeneration** covering all of the
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


# Juvenile-Onset Diabetes Mellitus With Central and Peripheral Neurodegeneration

## Executive summary

**Disease mapping.** The requested entity corresponds to **autosomal-recessive DNAJC3 deficiency**, most commonly called **diabetes mellitus and multisystemic neurodegeneration** or **DNAJC3-related neuroendocrine disorder with insulin dysregulation**. It is an ultra-rare syndromic monogenic diabetes caused by biallelic loss-of-function variants in **DNAJC3** (P58IPK/ERdj6), an endoplasmic-reticulum (ER) BiP co-chaperone. Its core manifestations are non-autoimmune juvenile diabetes, short stature, progressive cerebellar and peripheral ataxia/neuropathy, sensorineural hearing loss, and variable cognitive, retinal, thyroid, pituitary, and pancreatic abnormalities. Some children first have hyperinsulinemic hypoglycemia (HH), producing an age-dependent, sometimes biphasic course from excessive insulin release to beta-cell failure and diabetes. (welters2024congenitalhyperinsulinismin pages 1-2, ocansey2022biallelicdnajc3variants pages 4-6)

The evidence base remains small: chiefly individual families and sibling reports, patient-derived fibroblasts, beta-cell experiments, and knockout mice. Consequently, prevalence, penetrance, phenotype frequencies, survival, and treatment-response rates cannot yet be estimated reliably.

The following table summarizes the principal evidence.

| evidence domain | source/model | main finding | quantitative/example data | strength/limitation |
|---|---|---|---|---|
| Foundational human disease description | Human families with biallelic DNAJC3 loss | DNAJC3 deficiency causes a syndromic disorder combining juvenile/early-onset diabetes with central and peripheral neurodegeneration, often including ataxia, hearing loss, cognitive impairment, short stature, hypothyroidism, retinal findings, and pancreatic abnormalities (welters2024congenitalhyperinsulinismin pages 1-2, ocansey2022biallelicdnajc3variants pages 4-6, alwatban2021casereporthomozygous pages 4-5, alwatban2021casereporthomozygous pages 1-2) | Reported features across cases include ataxia, peripheral neuropathy, sensorineural hearing loss, retinal dystrophy, short stature, hypothyroidism, and pancreatic atrophy/hypoplasia; diabetes is generally non-autoimmune (welters2024congenitalhyperinsulinismin pages 1-2, alwatban2021casereporthomozygous pages 4-5, alwatban2021casereporthomozygous pages 1-2) | Strong syndrome-level consistency across independent families; limitation: very small number of published patients and incomplete ascertainment (ocansey2022biallelicdnajc3variants pages 4-6, alwatban2021casereporthomozygous pages 4-5) |
| Inheritance and causal variants | Human pedigrees/case series | Inheritance is autosomal recessive with homozygous or compound-heterozygous loss-of-function variants in DNAJC3 (alwatban2021casereporthomozygous pages 4-5, ocansey2022biallelicdnajc3variants pages 1-2, ocansey2022biallelicdnajc3variants pages 4-6) | Examples: p.Arg194*; large homozygous deletion spanning exons 6-12; p.Arg393*; p.Arg346*/p.Met1Val; splice-site c.393+2T>G and c.393+2T>C; c.1367_1370delAGAA (p.Lys456SerfsTer85) (ocansey2022biallelicdnajc3variants pages 4-6, alwatban2021casereporthomozygous pages 4-5, ocansey2022biallelicdnajc3variants pages 1-2, ocansey2022biallelicdnajc3variants pages 2-3) | Multiple recurrent LoF alleles support causality; limitation: no robust penetrance or population-frequency summary available from the retrieved evidence (ocansey2022biallelicdnajc3variants pages 4-6, ocansey2022biallelicdnajc3variants pages 2-3) |
| 2024 metabolic expansion study | Human index case plus young knockout mice | Hyperinsulinemic hypoglycemia can be a primary manifestation of DNAJC3 deficiency and may precede later diabetes, supporting a biphasic endocrine phenotype (welters2024congenitalhyperinsulinismin pages 1-2, welters2024congenitalhyperinsulinismin pages 2-3, welters2024congenitalhyperinsulinismin pages 9-10) | Human case: recurrent hypoglycemia from infancy; diazoxide responsive; persisted into adolescence. Mouse: 4-week-old KO mice had reduced total in vivo insulin secretion capacity but increased high-glucose-stimulated insulin release at islet level (welters2024congenitalhyperinsulinismin pages 2-3, welters2024congenitalhyperinsulinismin pages 9-10) | Valuable because it integrates patient and mechanistic mouse data; limitation: largely driven by one newly described human case and preclinical inference (welters2024congenitalhyperinsulinismin pages 2-3, welters2024congenitalhyperinsulinismin pages 9-10) |
| Human endocrine natural history | Human cases/siblings | Insulin dysregulation appears age-related, with early hyperinsulinism/hypoglycemia in some patients and later hyperglycemia/diabetes in adolescence or adulthood (ocansey2022biallelicdnajc3variants pages 3-4, ocansey2022biallelicdnajc3variants pages 6-7, ocansey2022biallelicdnajc3variants pages 4-6) | Ocansey report explicitly describes a spectrum “evolving from hyperinsulinaemic hypoglycaemia to diabetes mellitus”; one prior case had infancy hypoglycemia before diabetes at age 12 years (ocansey2022biallelicdnajc3variants pages 3-4, ocansey2022biallelicdnajc3variants pages 4-6) | Suggestive and clinically important; limitation: natural history remains poorly defined because longitudinal data are sparse (ocansey2022biallelicdnajc3variants pages 6-7, ocansey2022biallelicdnajc3variants pages 4-6) |
| Human neurologic phenotype | Human case reports/series | Neurologic involvement affects both central and peripheral nervous systems, including cerebellar/peripheral ataxia, developmental delay or cognitive impairment, and demyelinating/sensorimotor neuropathy (ocansey2022biallelicdnajc3variants pages 1-2, ocansey2022biallelicdnajc3variants pages 3-4, ocansey2022biallelicdnajc3variants pages 2-3, alwatban2021casereporthomozygous pages 4-5) | Example findings: peroneal motor nerve conduction velocity 31 m/s indicating demyelinating neuropathy; generalized myelin maturation delay; white-matter lesions; progressive gait ataxia (ocansey2022biallelicdnajc3variants pages 3-4, ocansey2022biallelicdnajc3variants pages 2-3, welters2024congenitalhyperinsulinismin pages 2-3) | Reproducible multisystem phenotype across reports; limitation: severity is variable, and some patients show only subtle neurologic abnormalities early in life (welters2024congenitalhyperinsulinismin pages 2-3, alwatban2021casereporthomozygous pages 1-2) |
| Imaging/anatomical evidence | Human MRI/imaging | Pancreatic atrophy/hypoplasia and neuroimaging abnormalities are emerging components of the phenotype (alwatban2021casereporthomozygous pages 4-5, alwatban2021casereporthomozygous pages 1-2, alwatban2021casereporthomozygous pages 7-8) | Small/atrophic pancreas on MRI in two siblings; other reports note small anterior pituitary and white-matter lesions (alwatban2021casereporthomozygous pages 4-5, alwatban2021casereporthomozygous pages 1-2, ocansey2022biallelicdnajc3variants pages 2-3, welters2024congenitalhyperinsulinismin pages 2-3) | Supports multisystem structural involvement; limitation: imaging has not been performed systematically across cases (alwatban2021casereporthomozygous pages 7-8) |
| Molecular mechanism: normal DNAJC3 function | Human/cell biology synthesis in disease-focused papers | DNAJC3 is an ER-resident BiP co-chaperone that helps refold misfolded proteins and dampens PERK-mediated UPR signaling; deficiency disrupts ER homeostasis and promotes apoptosis (welters2024congenitalhyperinsulinismin pages 1-2, jennings2021intracellularlipidaccumulation pages 1-2) | Functions described include BiP-assisted refolding in the ER lumen and indirect inhibition of PERK/eIF2α signaling during sustained stress (welters2024congenitalhyperinsulinismin pages 1-2, jennings2021intracellularlipidaccumulation pages 1-2) | Mechanistically coherent across disease papers; limitation: mostly inferred from cell and animal systems rather than direct human tissue experiments (welters2024congenitalhyperinsulinismin pages 1-2, jennings2021intracellularlipidaccumulation pages 1-2) |
| Patient-cell proteomics and organelle pathology | Patient-derived fibroblasts/proteomics | Loss of DNAJC3 is associated with perturbed lipid/cholesterol metabolism, ER-Golgi dysfunction, amyloid precursor protein defects, and mitochondrial morphology/OXPHOS abnormalities (jennings2021intracellularlipidaccumulation pages 1-2) | Reported observations include intracellular lipid accumulation, increased sensitivity to cholesterol stress, UPR activation, ER-Golgi alterations, β-amyloid accumulation, and impaired mitochondrial oxidative phosphorylation (jennings2021intracellularlipidaccumulation pages 1-2) | Strong mechanistic depth from unbiased proteomics plus functional assays; limitation: fibroblasts may not fully model pancreatic beta cells or neurons (jennings2021intracellularlipidaccumulation pages 1-2) |
| Beta-cell injury mechanism | Human islets/cell lines/mouse | DNAJC3 deficiency promotes beta-cell dysfunction and apoptosis, providing a mechanistic basis for diabetes (welters2024congenitalhyperinsulinismin pages 1-2, welters2024congenitalhyperinsulinismin pages 7-9, jennings2021intracellularlipidaccumulation pages 1-2) | Evidence cited includes apoptosis in INS-1E cells, primary rat beta cells, and human islets; KO mice develop hypoinsulinemia and gradual hyperglycemia with age (welters2024congenitalhyperinsulinismin pages 1-2, welters2024congenitalhyperinsulinismin pages 7-9) | Cross-species convergence supports pathogenic mechanism; limitation: limited direct histopathology from affected human pancreas (welters2024congenitalhyperinsulinismin pages 7-9, alwatban2021casereporthomozygous pages 7-8) |
| Proposed hyperinsulinism mechanism | Human+mouse mechanistic proposal | Early hyperinsulinism may result from excessive ER-to-cytosol calcium leak via Sec61 when DNAJC3/BiP gating is impaired (welters2024congenitalhyperinsulinismin pages 9-10, welters2024congenitalhyperinsulinismin pages 1-2) | Human concept linked to diazoxide-responsive HH; mouse islets showed significantly higher insulin release during high-glucose stimulation despite lower insulin content (welters2024congenitalhyperinsulinismin pages 9-10, welters2024congenitalhyperinsulinismin pages 1-2) | Novel and disease-specific mechanistic hypothesis; limitation: calcium imaging confirmation in DNAJC3-deficient human islets is still lacking (welters2024congenitalhyperinsulinismin pages 9-10) |
| Real-world management | Human case reports | Management is supportive and phenotype-directed: diazoxide for HH, insulin or metformin/lifestyle for diabetes, levothyroxine for hypothyroidism, and multidisciplinary neurologic/endocrine follow-up (ocansey2022biallelicdnajc3variants pages 2-3, welters2024congenitalhyperinsulinismin pages 2-3, alwatban2021casereporthomozygous pages 4-5, alwatban2021casereporthomozygous pages 1-2) | Diazoxide doses reported from 7.5-10 mg/kg/day initially, tapered to 2.2 mg/kg/day by age 14 in one patient; one diabetic sibling initially used metformin/lifestyle then later insulin (welters2024congenitalhyperinsulinismin pages 2-3, alwatban2021casereporthomozygous pages 4-5) | Directly relevant to current care; limitation: no disease-specific trials or standardized treatment algorithms were identified (welters2024congenitalhyperinsulinismin pages 2-3, alwatban2021casereporthomozygous pages 4-5) |
| Growth hormone experience | Human case reports/literature review | rhGH has shown limited growth benefit and may raise concern for worsening hyperglycemia in patients with limited beta-cell reserve (alwatban2021casereporthomozygous pages 7-8, alwatban2021casereporthomozygous pages 1-2) | Off-label GH and recombinant IGF-1 showed no meaningful growth response in the 2024 case; 2021 review suggested hyperglycemia risk may outweigh benefit (welters2024congenitalhyperinsulinismin pages 2-3, alwatban2021casereporthomozygous pages 7-8) | Helpful caution for endocrine management; limitation: based on small uncontrolled observations (alwatban2021casereporthomozygous pages 7-8, welters2024congenitalhyperinsulinismin pages 2-3) |
| Evidence gaps | Across literature | Major gaps remain in epidemiology, formal diagnostic criteria, prognostic biomarkers, genotype-phenotype correlations, omics biomarkers in target tissues, and interventional trials (ocansey2022biallelicdnajc3variants pages 4-6, alwatban2021casereporthomozygous pages 7-8, welters2024congenitalhyperinsulinismin pages 9-10) | No prevalence/incidence estimates, no disease-specific clinical trials retrieved, and only limited longitudinal natural-history data were available (ocansey2022biallelicdnajc3variants pages 4-6, welters2024congenitalhyperinsulinismin pages 9-10) | Important for knowledge-base completeness; limitation: absence of data should not be interpreted as absence of effect or absence of clinical relevance (ocansey2022biallelicdnajc3variants pages 4-6, welters2024congenitalhyperinsulinismin pages 9-10) |


*Table: This table condenses the strongest currently retrieved evidence for DNAJC3-related juvenile-onset diabetes with multisystemic neurodegeneration, spanning human case reports, the 2024 human-plus-mouse study, fibroblast proteomics, management observations, and key knowledge gaps.*

## 1. Disease information

### Definition and nomenclature

This is a **Mendelian, multisystem proteostasis disorder** in which biallelic DNAJC3 deficiency compromises ER stress adaptation. Pancreatic beta cells and neurons appear particularly vulnerable, yielding endocrine dysfunction plus central and peripheral neurodegeneration. The foundational report described diabetes with multisystemic neurodegeneration; later reports broadened the phenotype to hypothyroidism, pancreatic atrophy, retinal disease, neutropenia, and congenital/childhood HH. (alwatban2021casereporthomozygous pages 4-5, ocansey2022biallelicdnajc3variants pages 1-2, welters2024congenitalhyperinsulinismin pages 1-2)

**Synonyms:**

- DNAJC3 deficiency / DNAJC3-related disorder
- Diabetes mellitus and multisystemic neurodegeneration
- Syndromic juvenile-onset diabetes due to DNAJC3
- DNAJC3-related neuroendocrine developmental disorder with insulin dysregulation
- P58IPK deficiency

**Identifiers.** OMIM commonly catalogs the phenotype as **Diabetes mellitus and multisystemic neurodegeneration, autosomal recessive (DMND)**, generally reported as **OMIM 616192**, and DNAJC3 as **OMIM 601184**. These numerical mappings should be revalidated against the live OMIM record before database ingestion because the retrieved papers did not reproduce the identifiers. A disease-specific MONDO, Orphanet, MeSH, ICD-10, or ICD-11 code was not established in the retrieved primary literature; therefore, assigning a generic diabetes or ataxia code would lose the syndromic meaning. Recommended knowledge-base representation is a DNAJC3-related monogenic disease concept linked to its component diabetes, neuropathy, ataxia, deafness, and endocrine phenotypes.

**Source granularity.** The available clinical information comes from aggregated case reports and very small family series, not EHR-scale cohorts. For example, the 2021 report described two Saudi brothers, while the 2022 paper described two affected siblings identified through the 100,000 Genomes Project. (alwatban2021casereporthomozygous pages 4-5, ocansey2022biallelicdnajc3variants pages 2-3, ocansey2022biallelicdnajc3variants pages 6-7)

## 2. Etiology, risk, and protective factors

### Causal factor

The established cause is **germline biallelic loss of DNAJC3 function**, inherited autosomal recessively. Reported alleles include:

- **c.580C>T, p.Arg194Ter**;
- a homozygous approximately **72.7-kb deletion involving exons 6–12** and neighboring sequence;
- **c.1177C>T, p.Arg393Ter**;
- compound heterozygous **c.1036C>T, p.Arg346Ter / c.1A>G, p.Met1Val**;
- splice variants **c.393+2T>G** and **c.393+2T>C**;
- **c.1367_1370delAGAA, p.Lys456SerfsTer85**, which elongates and disrupts the J-domain-containing protein. (alwatban2021casereporthomozygous pages 4-5, ocansey2022biallelicdnajc3variants pages 1-2, ocansey2022biallelicdnajc3variants pages 4-6)

These are predominantly nonsense, frameshift, splice-disrupting, or multiexon-deletion alleles consistent with loss of function. The disease is germline, not somatic. Individual ClinVar classifications and gnomAD frequencies were not available in the retrieved full text and should be imported variant-by-variant rather than inferred. The heterozygous p.His238Asn allele proposed in familial type 2 diabetes has weak evidence: it was also found in unaffected individuals and occurs at low population frequency, arguing against treating heterozygous DNAJC3 variation as an established dominant cause. (jennings2021intracellularlipidaccumulation pages 1-2)

### Risk and protective factors

- **Genetic risk:** two pathogenic/likely pathogenic alleles in trans; consanguinity increases the probability of homozygosity. Several reported families were consanguineous. (alwatban2021casereporthomozygous pages 1-2, ocansey2022biallelicdnajc3variants pages 2-3)
- **Family history:** an affected sibling or known carrier parents substantially increases prior probability; recurrence risk for two carrier parents is 25% per conception.
- **Modifiers:** no validated modifier genes, protective alleles, or quantitative penetrance modifiers are known.
- **Environment/lifestyle:** no toxin, infection, diet, smoking, occupational, or geographic exposure is established as causal. Ordinary metabolic stress may influence beta-cell reserve but is not a primary cause.
- **Possible gene–treatment interaction:** growth hormone (GH) antagonizes insulin action and could unmask hyperglycemia in a person with limited beta-cell reserve. In six reported treated patients, however, hyperglycemia persisted or recurred after GH withdrawal, confirming underlying disease rather than GH as the cause. (alwatban2021casereporthomozygous pages 7-8)
- **Protective factors:** no disease-preventing environmental intervention is demonstrated. Early detection and treatment of hypoglycemia protects against secondary neurologic injury but does not correct DNAJC3 deficiency.

## 3. Phenotypes

Because published numbers are extremely small and ascertainment differs among reports, frequencies below are qualitative rather than population estimates.

| Phenotype | Type, onset, course and impact | Suggested HPO term |
|---|---|---|
| Non-autoimmune diabetes mellitus | Usually childhood/adolescence; insidious and progressive, with residual insulin initially but eventual insulin requirement. GAD2 antibodies were absent in four of five foundational subjects; the original article required an erratum to correct this point. (synofzik2015absenceofbip pages 1-1) | Juvenile-onset diabetes mellitus; HP:0000819 Diabetes mellitus |
| Hyperinsulinemic hypoglycemia | Infancy/childhood; diazoxide-responsive; may remit before later diabetes, although a 2024 patient retained HH through adolescence. Hypoglycemia can be asymptomatic. (ocansey2022biallelicdnajc3variants pages 6-7, welters2024congenitalhyperinsulinismin pages 2-3) | HP:0000825 Hyperinsulinemia; HP:0001943 Hypoglycemia; HP:0001985 Hypoketotic hypoglycemia |
| Severe short stature/growth failure | Usually evident in infancy; persistent and often severe. One child remained approximately −4 SD despite GH and IGF-1. (welters2024congenitalhyperinsulinismin pages 2-3) | HP:0004322 Short stature; HP:0001510 Growth delay |
| Cerebellar/peripheral ataxia | Childhood onward; variable but often progressive, impairing walking and long-distance mobility. (alwatban2021casereporthomozygous pages 4-5, alwatban2021casereporthomozygous pages 7-8) | HP:0001251 Ataxia; HP:0002072 Cerebellar ataxia; HP:0002131 Episodic ataxia is **not** characteristic |
| Sensorimotor neuropathy | Childhood/adolescence; demyelinating or mixed sensorimotor involvement. Peroneal motor conduction velocity was 31 m/s in one child. (ocansey2022biallelicdnajc3variants pages 3-4) | HP:0000763 Peripheral neuropathy; HP:0003431 Sensorimotor neuropathy; HP:0007108 Demyelinating peripheral neuropathy |
| Sensorineural hearing loss | Common across reported families; generally bilateral, childhood onset, and functionally important for language/education. (alwatban2021casereporthomozygous pages 4-5, welters2024congenitalhyperinsulinismin pages 1-2) | HP:0000407 Sensorineural hearing impairment; HP:0000365 Hearing impairment |
| Developmental/cognitive impairment | Variable global developmental delay, delayed language, learning difficulties, or intellectual disability. (alwatban2021casereporthomozygous pages 1-2, ocansey2022biallelicdnajc3variants pages 2-3) | HP:0001263 Global developmental delay; HP:0001249 Intellectual disability; HP:0000750 Delayed speech and language development |
| Hypothyroidism | Usually primary, sometimes detected in infancy; generally manageable with levothyroxine. (alwatban2021casereporthomozygous pages 1-2, welters2024congenitalhyperinsulinismin pages 2-3) | HP:0000821 Hypothyroidism |
| Microcephaly | Reported as consistent in some families, but not universal across the full spectrum. (ocansey2022biallelicdnajc3variants pages 4-6) | HP:0000252 Microcephaly |
| Retinal/ocular disease | Retinal dystrophy, rod–cone dysfunction, myopia, coloboma, or other ocular findings in selected patients; variable expressivity. (ocansey2022biallelicdnajc3variants pages 2-3, ocansey2022biallelicdnajc3variants pages 4-6) | HP:0000556 Retinal dystrophy; HP:0000608 Retinal degeneration; HP:0000545 Myopia; HP:0000588 Optic nerve coloboma if applicable |
| Pancreatic hypoplasia/atrophy | MRI finding in two brothers; may reflect abnormal development plus progressive tissue loss. Exocrine function can remain normal. (alwatban2021casereporthomozygous pages 4-5, alwatban2021casereporthomozygous pages 7-8) | HP:0012092 Abnormal pancreas morphology; HP:0001734 Pancreatic hypoplasia |
| White-matter/myelin abnormalities | Variable MRI finding: nonspecific frontal lesions or delayed myelin maturation; MRI can also be normal despite ataxia. (alwatban2021casereporthomozygous pages 1-2, ocansey2022biallelicdnajc3variants pages 2-3, welters2024congenitalhyperinsulinismin pages 2-3) | HP:0002500 Abnormal cerebral white matter morphology; HP:0012448 Delayed myelination |
| Pituitary hypoplasia | Small anterior pituitary in the 2022 siblings, but pituitary hormone function may be normal. (ocansey2022biallelicdnajc3variants pages 1-2, ocansey2022biallelicdnajc3variants pages 4-6) | HP:0012504 Pituitary hypoplasia |
| Neutropenia | Persistent neutrophils 0.6–0.8 ×10⁹/L in the 2022 siblings; a possible expanded phenotype, not established as core. (ocansey2022biallelicdnajc3variants pages 2-3) | HP:0001875 Neutropenia |

**Quality of life.** No validated EQ-5D, SF-36, or PROMIS cohort data exist. One severely affected young adult could not complete high school, used a wheelchair for long distances, and required help with outdoor activities; his more mildly affected brother completed high school, worked, drove, and remained independent. This illustrates marked variable expressivity rather than a measurable average burden. (alwatban2021casereporthomozygous pages 7-8)

## 4. Genetic and molecular information

**Causal gene:** **DNAJC3**, encoding DnaJ heat-shock-protein family member C3, also known as **P58IPK** or **ERdj6**. Suggested annotations include HGNC symbol DNAJC3 and protein-function terms for ER chaperone binding and unfolded-protein response regulation; the precise HGNC numeric identifier should be retrieved directly from HGNC.

DNAJC3 contains an N-terminal substrate-binding region and a C-terminal J domain. It binds hydrophobic regions of misfolded ER proteins; ATP-dependent J-domain interaction activates the HSPA5/BiP folding cycle. DNAJC3 also restrains PERK signaling, thereby limiting eIF2α phosphorylation and helping restart translation after stress. (welters2024congenitalhyperinsulinismin pages 1-2, jennings2021intracellularlipidaccumulation pages 1-2)

**Functional consequence:** established disease alleles largely cause absent or severely impaired protein, defective BiP co-chaperone activity, maladaptive UPR signaling, and stress-induced apoptosis. The p.Lys456SerfsTer85 allele is predicted to alter the J domain and prevent effective BiP ATPase activation. (ocansey2022biallelicdnajc3variants pages 1-2, ocansey2022biallelicdnajc3variants pages 4-6)

**Chromosomal, epigenetic, and modifier information:** no recurrent aneuploidy, translocation, inversion, repeat expansion, disease-specific methylation signature, or validated modifier gene has been established. One affected child had normal 46,XX karyotype, array-CGH, and Prader–Willi-region methylation testing during an earlier diagnostic work-up. (welters2024congenitalhyperinsulinismin pages 2-3)

## 5. Environmental information

This is not an infectious, toxic, occupational, nutritional, or lifestyle-induced disease. No pathogen or environmental trigger is required. Rotavirus infection led to detection—not proof of causation—of recurrent hypoglycemia in one infant. (welters2024congenitalhyperinsulinismin pages 2-3)

Lifestyle measures can support diabetes care but do not remove the molecular defect. Metformin and lifestyle modification temporarily managed diabetes in one patient before insulin was required. (alwatban2021casereporthomozygous pages 4-5)

## 6. Mechanism and pathophysiology

### Upstream causal chain

1. **Biallelic DNAJC3 loss** reduces ER-resident P58IPK/ERdj6 activity.
2. **BiP-assisted protein folding and ER recovery fail**, while PERK–eIF2α stress signaling is inadequately restrained.
3. Secretory cells with high protein-folding demand—notably **pancreatic beta cells** and selected neurons—develop maladaptive ER stress.
4. Downstream lipid/cholesterol dysregulation, ER–Golgi disturbance, mitochondrial dysfunction, impaired oxidative phosphorylation, and apoptosis reduce beta-cell and neuronal survival.
5. Beta-cell loss causes hypoinsulinemia and diabetes; neuronal injury produces ataxia, neuropathy, hearing loss, and cognitive manifestations. (welters2024congenitalhyperinsulinismin pages 1-2, jennings2021intracellularlipidaccumulation pages 1-2)

### Biphasic insulin mechanism: current 2024 model

The 2024 study proposed an additional early mechanism. Sec61 transports nascent polypeptides and can leak ER calcium; luminal BiP promotes channel closure. Deletion of DNAJC3 or DNAJB11 increases Sec61-mediated leakage. In beta cells, excess ER-to-cytosol Ca²⁺ may initially provoke inappropriate insulin exocytosis and HH. With persistent ER stress, apoptosis reduces beta-cell mass, shifting the phenotype toward insulin deficiency and diabetes. (welters2024congenitalhyperinsulinismin pages 9-10)

This remains a **strong mechanistic hypothesis**, not fully demonstrated in human beta cells: direct calcium imaging in DNAJC3-deficient human islets is still needed. The article accurately summarizes its novelty as: **“This is the first genetic mechanism explaining HH solely by the disruption of intracellular calcium homeostasis.”** (welters2024congenitalhyperinsulinismin pages 1-2)

### Molecular profiling

**Patient-fibroblast proteomics and functional studies** found perturbed lipid metabolism, mitochondrial bioenergetics, ER–Golgi function, and amyloid-beta processing. Cells accumulated lipids, were unusually sensitive to cholesterol stress, activated the UPR, showed altered ER–Golgi machinery and APP processing, and had abnormal mitochondrial morphology and oxidative phosphorylation. The authors’ abstract states: **“the loss of DNAJC3 affects lipid/cholesterol homeostasis, leading to UPR activation, β-amyloid accumulation, and impairment of mitochondrial oxidative phosphorylation.”** (jennings2021intracellularlipidaccumulation pages 1-2)

No disease-specific single-cell, spatial-transcriptomic, epigenomic, metabolomic, or lipidomic cohort is currently available. The fibroblast proteome may identify pathways but cannot substitute for affected human islets, cerebellum, peripheral nerve, cochlea, or retina.

### Suggested ontology annotations

- **GO biological process:** protein folding in ER; response to ER stress; unfolded protein response; regulation of translation; calcium-ion homeostasis; intrinsic apoptotic signaling in response to ER stress; regulation of insulin secretion; mitochondrial organization; oxidative phosphorylation; lipid/cholesterol homeostasis.
- **GO cellular component:** endoplasmic-reticulum lumen; ER membrane; Sec61 translocon complex; mitochondrion; Golgi apparatus.
- **Cell Ontology:** pancreatic beta cell (**CL:0000169**); neuron (**CL:0000540**); peripheral sensory neuron; motor neuron; cerebellar neuron/Purkinje cell; Schwann cell; retinal photoreceptor; cochlear hair cell; thyroid follicular cell.
- **Chemical ontology:** calcium ion (**CHEBI:29108**), glucose (**CHEBI:17234**), insulin, cholesterol (**CHEBI:16113**).

## 7. Anatomical structures affected

**Primary organs/systems:**

- **Endocrine pancreas**, especially islet beta cells; pancreatic hypoplasia/atrophy can be visible on MRI.
- **Central nervous system**, including cerebellar circuitry and cerebral white matter.
- **Peripheral nervous system**, involving sensory and motor axons and/or myelin.
- **Inner ear/auditory pathway**, causing bilateral sensorineural loss.
- **Retina**, variably involving rod and cone photoreceptors.
- **Thyroid and pituitary**, with primary hypothyroidism and occasional small anterior pituitary. (ocansey2022biallelicdnajc3variants pages 3-4, ocansey2022biallelicdnajc3variants pages 2-3, welters2024congenitalhyperinsulinismin pages 1-2)

**Secondary involvement:** skeletal growth, cognition, mobility, education, and psychosocial independence. Classic diabetic microvascular complications have not been systematically quantified.

**Suggested UBERON sites:** pancreas/islet of Langerhans; brain/cerebellum/cerebral white matter; peripheral nerve; cochlea; retina; thyroid gland; pituitary gland. **Subcellular site:** ER lumen and membrane are upstream; mitochondria and ER–Golgi machinery are important downstream compartments. No consistent lateralization is reported; hearing, neuropathy, and retinal manifestations are generally bilateral/systemic.

## 8. Temporal development

The disorder is chronic and lifelong, but its components emerge asynchronously:

- **Infancy:** growth failure, hypothyroidism, developmental delay, and HH may appear. In the 2024 case, recurrent glucose below 40 mg/dL was first recognized at nine months. (welters2024congenitalhyperinsulinismin pages 2-3)
- **Childhood:** short stature persists; hearing loss, developmental/learning problems, retinal findings, ataxia, and neuropathy emerge variably.
- **Adolescence:** diabetes commonly becomes apparent as beta-cell reserve declines. Documented onsets include ages 11, 12, and 14 years. (alwatban2021casereporthomozygous pages 4-5, alwatban2021casereporthomozygous pages 1-2, ocansey2022biallelicdnajc3variants pages 4-6)
- **Adulthood:** neurologic disability may progress, although severity is variable and MRI may remain normal in a mildly affected adult. (alwatban2021casereporthomozygous pages 1-2)

The most distinctive trajectory is **early HH → remission or declining diazoxide requirement → later hyperglycemia/diabetes**, but not every patient is recognized in the hypoglycemic phase, and HH persisted to age 14 in the 2024 report. (ocansey2022biallelicdnajc3variants pages 6-7, welters2024congenitalhyperinsulinismin pages 2-3)

There is no known spontaneous molecular remission. Treated endocrine abnormalities can be controlled, but neurodegeneration and beta-cell loss are not known to reverse.

## 9. Inheritance and population

- **Inheritance:** autosomal recessive.
- **Penetrance:** likely high for a multisystem phenotype among people with severe biallelic loss-of-function alleles, but age-dependent and not formally quantified.
- **Expressivity:** clearly variable, including neurological severity, MRI findings, retinal disease, and timing of dysglycemia. (alwatban2021casereporthomozygous pages 1-2, ocansey2022biallelicdnajc3variants pages 4-6)
- **Anticipation:** not expected and not reported.
- **Germline mosaicism:** not documented; a small residual risk remains theoretically possible after an apparently de novo event.
- **Consanguinity:** important in multiple reports but not required; the 2024 patient had non-consanguineous German parents. (ocansey2022biallelicdnajc3variants pages 2-3, welters2024congenitalhyperinsulinismin pages 2-3)
- **Founder effects/carrier frequency:** none established.
- **Sex ratio:** no reliable estimate or demonstrated sex bias.
- **Geography/ancestry:** affected families have included Turkish, Middle Eastern/Arab, British and German backgrounds, supporting worldwide occurrence rather than geographic restriction. (alwatban2021casereporthomozygous pages 4-5, welters2024congenitalhyperinsulinismin pages 2-3, ocansey2022biallelicdnajc3variants pages 4-6)

No population prevalence, incidence per 100,000, or carrier-frequency estimate is available. The safest classification is **ultra-rare**, with published evidence limited to a small number of families.

## 10. Diagnostics

### Clinical suspicion

Consider DNAJC3 deficiency in a child or young adult with **antibody-negative diabetes or HH plus two or more of short stature, ataxia, neuropathy, hearing loss, developmental impairment, retinal dystrophy, hypothyroidism, or pancreatic atrophy**. The overlap with mitochondrial diabetes, Wolfram syndrome, Wolcott–Rallison syndrome, Marinesco–Sjögren syndrome, and complex inherited neuropathies is substantial. DNAJC3 should specifically enter the differential for diabetes–deafness–neurodegeneration presentations. (alwatban2021casereporthomozygous pages 6-7, alwatban2021casereporthomozygous pages 7-8)

### Recommended evaluation

1. **Glycemic assessment:** fasting/random glucose, HbA1c, oral or mixed-meal testing as appropriate, C-peptide, insulin, and diabetes autoantibodies.
2. **During hypoglycemia:** paired glucose, insulin, C-peptide, beta-hydroxybutyrate, free fatty acids, cortisol and growth hormone; glucagon response; acylcarnitines, amino acids, and urine organic acids to exclude metabolic mimics. In the 2024 patient, glucose 52 mg/dL was accompanied by insulin 6.5 mU/L, C-peptide 1.4 ng/mL and beta-hydroxybutyrate 0.1 mmol/L at age 14. (welters2024congenitalhyperinsulinismin pages 2-3)
3. **Endocrine:** TSH/free T4, growth velocity, IGF-1 and targeted pituitary testing.
4. **Neurologic:** examination, developmental/neuropsychological testing, brain MRI, EMG and nerve-conduction studies.
5. **Sensory:** formal audiology; ophthalmologic examination, optical coherence tomography and electroretinography where indicated.
6. **Anatomical:** pancreatic MRI or ultrasound; MRI may disclose a small/atrophic pancreas even with preserved exocrine function. (alwatban2021casereporthomozygous pages 4-5, alwatban2021casereporthomozygous pages 7-8)

### Genetic testing strategy

- First-line: an NGS **syndromic monogenic-diabetes/HH panel** that includes DNAJC3, ideally with copy-number analysis.
- If the phenotype is neurologically dominant: a complex ataxia/neuropathy panel must also include DNAJC3.
- WES or WGS is appropriate when panel testing is negative or the phenotype is broad. WES diagnosed the Saudi siblings; WGS identified the 2022 family. (alwatban2021casereporthomozygous pages 1-2, ocansey2022biallelicdnajc3variants pages 2-3)
- Confirm variants and segregation with Sanger sequencing or validated orthogonal methods.
- Use deletion/duplication analysis for multiexon CNVs. Standard karyotype, CMA, FISH, mitochondrial DNA, and repeat-expansion tests do not directly detect the usual cause unless used to investigate alternatives.
- RNA studies may clarify splice variants; no validated diagnostic proteomic, metabolomic, or methylation assay exists.

The 2024 research panel achieved mean target coverage of 624× with about 99% of targets covered at least 20×, illustrating high-sensitivity targeted sequencing rather than a required clinical threshold. (welters2024congenitalhyperinsulinismin pages 9-10)

### Differential diagnosis

Important alternatives include WFS1/CISD2 Wolfram syndrome; EIF2AK3 Wolcott–Rallison syndrome; SIL1 Marinesco–Sjögren syndrome; mitochondrial m.3243A>G diabetes-deafness; WFS1, OPA1 and other deafness/optic-neuropathy disorders; HNF1B and CEL-related pancreatic disease; hereditary ataxias and Charcot–Marie–Tooth disorders; and FICD-related BiP dysregulation. Distinguishing clues for DNAJC3 are autosomal-recessive inheritance, severe short stature, combined central/peripheral neurodegeneration, non-autoimmune diabetes or preceding HH, and pancreatic atrophy.

No consensus diagnostic criteria or population/newborn screening program exists. Cascade testing is appropriate once familial variants are known.

## 11. Outcome and prognosis

Quantitative survival, life-expectancy, mortality, and five- or ten-year outcome data are unavailable. Published patients have survived into adulthood, but the cohort is too small and young to define lifespan.

Major morbidity comes from progressive gait impairment/neuropathy, hearing loss, developmental or cognitive disability, visual disease, severe short stature, hypoglycemic brain-injury risk, and lifelong diabetes. One adult required a wheelchair for long distances and assistance with outside activities, whereas his brother remained independently mobile and employed, demonstrating broad prognostic variability. (alwatban2021casereporthomozygous pages 7-8)

Likely adverse prognostic indicators include early/severe neurologic involvement, recurrent untreated hypoglycemia, profound hearing/visual loss, advanced pancreatic atrophy, and low C-peptide, but none is validated as a prognostic biomarker. No disease-specific biomarker predicts neurologic progression.

## 12. Treatment and current applications

There is **no approved disease-modifying, gene, cell, RNA, or targeted UPR therapy** for DNAJC3 deficiency and no disease-specific interventional clinical trial was identified.

### Current real-world management

- **HH:** regular feeding/avoidance of prolonged fasting, glucose monitoring and **diazoxide** when responsive; chlorothiazide may accompany diazoxide. One patient received 7.5–10 mg/kg/day in childhood, tapered to 2.2 mg/kg/day by age 14 while maintaining glucose above 70 mg/dL. Monitor fluid retention, hypertrichosis, pulmonary hypertension and blood counts according to standard CHI practice. (ocansey2022biallelicdnajc3variants pages 2-3, welters2024congenitalhyperinsulinismin pages 2-3)
- **Diabetes:** individualized nutrition, continuous glucose monitoring where accessible, and insulin when secretion becomes inadequate. Metformin/lifestyle measures may temporarily suffice in mild early hyperglycemia but did not prevent later insulin need in a reported patient. (alwatban2021casereporthomozygous pages 4-5)
- **Hypothyroidism:** levothyroxine.
- **Hearing loss:** hearing aids, educational accommodations, and cochlear-implant assessment where appropriate.
- **Neurologic disability:** physical and occupational therapy, gait aids, orthotics, fall prevention, wheelchair support, and neuropathic-pain treatment.
- **Development/communication:** speech-language therapy, neuropsychology, individualized education, and psychosocial support.
- **Vision:** low-vision and retinal surveillance services.
- **Nutrition:** dietetic review for growth failure and diabetes/HH balance.

**GH/IGF-1 caution.** GH or recombinant IGF-1 produced little or no linear-growth response in reported patients. Because GH can worsen hyperglycemia in a person with limited beta-cell reserve, the 2021 authors argued that risk may outweigh benefit unless true GH deficiency is demonstrated and glycemia is monitored closely. (welters2024congenitalhyperinsulinismin pages 2-3, alwatban2021casereporthomozygous pages 7-8)

Suggested NCI Thesaurus intervention concepts include insulin therapy, diazoxide treatment, thyroid-hormone replacement, glucose monitoring, physical therapy, occupational therapy, hearing aid, cochlear implantation, and genetic counseling; exact NCIT codes should be resolved against the current NCIT release.

## 13. Prevention

**Primary prevention** of disease in an already conceived affected individual is unavailable. Reproductive options for a known carrier couple include genetic counseling, partner/cascade testing, prenatal diagnosis, and preimplantation genetic testing for monogenic disease.

**Secondary prevention** centers on early recognition: test siblings for familial variants; screen genetically affected children for fasting hypoglycemia/HH, thyroid dysfunction, hearing loss, neuropathy, retinal disease, and emerging diabetes. The 2024 authors explicitly concluded that clinicians should screen for HH in DNAJC3 deficiency and consider DNAJC3 in congenital hyperinsulinism. (welters2024congenitalhyperinsulinismin pages 1-2)

**Tertiary prevention** includes preventing hypoglycemic brain injury, optimizing glycemia to reduce conventional diabetic complications, treating hypothyroidism and hearing loss promptly, and rehabilitation to prevent falls and contractures. Vaccination has no disease-specific preventive role beyond routine diabetes and general-health recommendations.

## 14. Other species and natural disease

No well-established naturally occurring veterinary equivalent or zoonotic disease was identified. The disorder is genetic and **not transmissible between species**.

Orthologous Dnajc3/P58IPK genes are conserved in laboratory mammals and other vertebrates, reflecting conservation of ER proteostasis. Taxonomy suggestions for experimental evidence are **Mus musculus (NCBI Taxon 10090)** and, for referenced beta-cell experiments, **Rattus norvegicus (Taxon 10116)** and **Homo sapiens (Taxon 9606)**. Exact ortholog NCBI Gene identifiers should be imported from NCBI rather than inferred from the articles.

## 15. Model organisms and experimental systems

### Mouse model

The principal disease model is the **Dnajc3/P58IPK knockout mouse**, including the C57BL/6-Dnajc3tm8663Wcl line available through MMRRC. Mature knockouts develop beta-cell apoptosis, reduced beta-cell mass, hypoinsulinemia and progressive hyperglycemia, recapitulating the human diabetic mechanism. (welters2024congenitalhyperinsulinismin pages 7-9, welters2024congenitalhyperinsulinismin pages 9-10)

In the 2024 study, isolated islets from 3–8-week-old knockouts released more insulin during high-glucose stimulation, while islet insulin content was already significantly reduced by three weeks. Four-week-old mice had decreased basal and stimulated plasma insulin and impaired glucose tolerance, but no fasting- or challenge-associated hypoglycemia. Thus, mice reproduce beta-cell failure well but do not fully reproduce the prolonged human HH phase. (welters2024congenitalhyperinsulinismin pages 9-10)

### Cellular systems

- Patient-derived dermal fibroblasts: useful for proteomics, cholesterol stress, ER–Golgi, APP and mitochondrial/OXPHOS studies. Limitation: not a secretory beta cell or neuron. (jennings2021intracellularlipidaccumulation pages 1-2)
- INS-1E cells and primary rat beta cells: model ER stress, insulin secretion and apoptosis.
- Human islets: strongest ex-vivo beta-cell relevance; DNAJC3 loss/silencing has been associated with beta-cell apoptosis, although available material is limited. (welters2024congenitalhyperinsulinismin pages 1-2)
- Retinal neurons: support vulnerability of neural sensory cells to DNAJC3 loss. (welters2024congenitalhyperinsulinismin pages 1-2)

No validated disease-specific zebrafish, Drosophila, C. elegans, organoid, humanized-knock-in, or patient-iPSC neuronal/beta-cell model was established in the retrieved literature. Developing isogenic CRISPR-corrected patient iPSC beta cells, cerebellar neurons, peripheral neurons and retinal organoids is a major research opportunity.

## Recent development and evidence assessment

The key 2023–2024 advance is the **20 January 2024** human-plus-mouse study, which showed that HH may dominate through adolescence and proposed defective DNAJC3/BiP gating of Sec61 as the link between ER proteostasis and inappropriate intracellular calcium-triggered insulin secretion. Its abstract states: **“HH may be a primary symptom of DNAJC3 deficiency and can persist until adolescence.”** DOI: https://doi.org/10.3390/ijms25021270. (welters2024congenitalhyperinsulinismin pages 1-2)

The strongest disease-specific omics study remains Jennings et al., published **6 October 2021**, DOI: https://doi.org/10.3389/fcell.2021.710247. Its patient-fibroblast proteomics connects ER stress to lipid accumulation, APP/amyloid processing, and mitochondrial bioenergetic failure. (jennings2021intracellularlipidaccumulation pages 1-2)

Important clinical expansions are Alwatban et al., **September 2021**, DOI: https://doi.org/10.3389/fendo.2021.742278, documenting pancreatic atrophy and major intrafamilial variability; and Ocansey et al., published online **October 2021/in the 2022 volume**, DOI: https://doi.org/10.1097/MCD.0000000000000397, confirming congenital HH and adding possible neutropenia and retinal manifestations. (alwatban2021casereporthomozygous pages 4-5, ocansey2022biallelicdnajc3variants pages 1-2, ocansey2022biallelicdnajc3variants pages 2-3)

## Knowledge-base cautions and research priorities

1. Do not calculate phenotype percentages from the published cases as though they were a registry cohort.
2. Record HH and diabetes as potentially sequential—not mutually exclusive—phenotypes.
3. Distinguish the demonstrated ER-stress/beta-cell-apoptosis mechanism from the still-to-be-directly-confirmed Sec61/Ca²⁺ hypothesis.
4. Treat neutropenia, pituitary hypoplasia, retinal coloboma and some dysmorphic findings as provisional/variable extensions.
5. Revalidate OMIM, MONDO, Orphanet, HGNC, HPO, GO, CL, UBERON and NCIT numeric identifiers against their live releases before ingestion.
6. Highest-priority studies are a multicenter natural-history registry, systematic variant curation, standardized endocrine and neurologic surveillance, target-tissue iPSC models, direct calcium imaging, and therapeutic testing of proteostasis/ER-stress interventions.

**PMID note:** DOI and publication dates are supplied where established by the retrieved full texts. PubMed identifiers were not exposed in those source records and have therefore not been guessed; they should be resolved programmatically through Crossref/PubMed during database ingestion.

References

1. (welters2024congenitalhyperinsulinismin pages 1-2): Alena Welters, Oliver Nortmann, Laura Wörmeyer, Clemens Freiberg, Daniel Eberhard, Nadine Bachmann, Carsten Bergmann, Ertan Mayatepek, Thomas Meissner, and Sebastian Kummer. Congenital hyperinsulinism in humans and insulin secretory dysfunction in mice caused by biallelic dnajc3 variants. International Journal of Molecular Sciences, 25:1270, Jan 2024. URL: https://doi.org/10.3390/ijms25021270, doi:10.3390/ijms25021270. This article has 1 citations.

2. (ocansey2022biallelicdnajc3variants pages 4-6): Sharon Ocansey, Debbie Pullen, Patricia Atkinson, Antonia Clarke, Medard Hadonou, Charlene Crosby, John Short, Ian Christopher Lloyd, Damian Smedley, Albanese Assunta, Pratik Shah, and Meriel McEntagart. Biallelic dnajc3 variants in a neuroendocrine developmental disorder with insulin dysregulation. Clinical Dysmorphology, 31:11-17, Oct 2022. URL: https://doi.org/10.1097/mcd.0000000000000397, doi:10.1097/mcd.0000000000000397. This article has 8 citations and is from a peer-reviewed journal.

3. (alwatban2021casereporthomozygous pages 4-5): Saud Alwatban, Haifa Alfaraidi, Abdulaziz Alosaimi, Iram Alluhaydan, Majid Alfadhel, Michel Polak, and Angham Almutair. Case report: homozygous dnajc3 mutation causes monogenic diabetes mellitus associated with pancreatic atrophy. Frontiers in Endocrinology, Sep 2021. URL: https://doi.org/10.3389/fendo.2021.742278, doi:10.3389/fendo.2021.742278. This article has 10 citations.

4. (alwatban2021casereporthomozygous pages 1-2): Saud Alwatban, Haifa Alfaraidi, Abdulaziz Alosaimi, Iram Alluhaydan, Majid Alfadhel, Michel Polak, and Angham Almutair. Case report: homozygous dnajc3 mutation causes monogenic diabetes mellitus associated with pancreatic atrophy. Frontiers in Endocrinology, Sep 2021. URL: https://doi.org/10.3389/fendo.2021.742278, doi:10.3389/fendo.2021.742278. This article has 10 citations.

5. (ocansey2022biallelicdnajc3variants pages 1-2): Sharon Ocansey, Debbie Pullen, Patricia Atkinson, Antonia Clarke, Medard Hadonou, Charlene Crosby, John Short, Ian Christopher Lloyd, Damian Smedley, Albanese Assunta, Pratik Shah, and Meriel McEntagart. Biallelic dnajc3 variants in a neuroendocrine developmental disorder with insulin dysregulation. Clinical Dysmorphology, 31:11-17, Oct 2022. URL: https://doi.org/10.1097/mcd.0000000000000397, doi:10.1097/mcd.0000000000000397. This article has 8 citations and is from a peer-reviewed journal.

6. (ocansey2022biallelicdnajc3variants pages 2-3): Sharon Ocansey, Debbie Pullen, Patricia Atkinson, Antonia Clarke, Medard Hadonou, Charlene Crosby, John Short, Ian Christopher Lloyd, Damian Smedley, Albanese Assunta, Pratik Shah, and Meriel McEntagart. Biallelic dnajc3 variants in a neuroendocrine developmental disorder with insulin dysregulation. Clinical Dysmorphology, 31:11-17, Oct 2022. URL: https://doi.org/10.1097/mcd.0000000000000397, doi:10.1097/mcd.0000000000000397. This article has 8 citations and is from a peer-reviewed journal.

7. (welters2024congenitalhyperinsulinismin pages 2-3): Alena Welters, Oliver Nortmann, Laura Wörmeyer, Clemens Freiberg, Daniel Eberhard, Nadine Bachmann, Carsten Bergmann, Ertan Mayatepek, Thomas Meissner, and Sebastian Kummer. Congenital hyperinsulinism in humans and insulin secretory dysfunction in mice caused by biallelic dnajc3 variants. International Journal of Molecular Sciences, 25:1270, Jan 2024. URL: https://doi.org/10.3390/ijms25021270, doi:10.3390/ijms25021270. This article has 1 citations.

8. (welters2024congenitalhyperinsulinismin pages 9-10): Alena Welters, Oliver Nortmann, Laura Wörmeyer, Clemens Freiberg, Daniel Eberhard, Nadine Bachmann, Carsten Bergmann, Ertan Mayatepek, Thomas Meissner, and Sebastian Kummer. Congenital hyperinsulinism in humans and insulin secretory dysfunction in mice caused by biallelic dnajc3 variants. International Journal of Molecular Sciences, 25:1270, Jan 2024. URL: https://doi.org/10.3390/ijms25021270, doi:10.3390/ijms25021270. This article has 1 citations.

9. (ocansey2022biallelicdnajc3variants pages 3-4): Sharon Ocansey, Debbie Pullen, Patricia Atkinson, Antonia Clarke, Medard Hadonou, Charlene Crosby, John Short, Ian Christopher Lloyd, Damian Smedley, Albanese Assunta, Pratik Shah, and Meriel McEntagart. Biallelic dnajc3 variants in a neuroendocrine developmental disorder with insulin dysregulation. Clinical Dysmorphology, 31:11-17, Oct 2022. URL: https://doi.org/10.1097/mcd.0000000000000397, doi:10.1097/mcd.0000000000000397. This article has 8 citations and is from a peer-reviewed journal.

10. (ocansey2022biallelicdnajc3variants pages 6-7): Sharon Ocansey, Debbie Pullen, Patricia Atkinson, Antonia Clarke, Medard Hadonou, Charlene Crosby, John Short, Ian Christopher Lloyd, Damian Smedley, Albanese Assunta, Pratik Shah, and Meriel McEntagart. Biallelic dnajc3 variants in a neuroendocrine developmental disorder with insulin dysregulation. Clinical Dysmorphology, 31:11-17, Oct 2022. URL: https://doi.org/10.1097/mcd.0000000000000397, doi:10.1097/mcd.0000000000000397. This article has 8 citations and is from a peer-reviewed journal.

11. (alwatban2021casereporthomozygous pages 7-8): Saud Alwatban, Haifa Alfaraidi, Abdulaziz Alosaimi, Iram Alluhaydan, Majid Alfadhel, Michel Polak, and Angham Almutair. Case report: homozygous dnajc3 mutation causes monogenic diabetes mellitus associated with pancreatic atrophy. Frontiers in Endocrinology, Sep 2021. URL: https://doi.org/10.3389/fendo.2021.742278, doi:10.3389/fendo.2021.742278. This article has 10 citations.

12. (jennings2021intracellularlipidaccumulation pages 1-2): Matthew J. Jennings, Denisa Hathazi, Chi D. L. Nguyen, Benjamin Munro, Ute Münchberg, Robert Ahrends, Annette Schenck, Ilse Eidhof, Erik Freier, Matthis Synofzik, Rita Horvath, and Andreas Roos. Intracellular lipid accumulation and mitochondrial dysfunction accompanies endoplasmic reticulum stress caused by loss of the co-chaperone dnajc3. Frontiers in Cell and Developmental Biology, Oct 2021. URL: https://doi.org/10.3389/fcell.2021.710247, doi:10.3389/fcell.2021.710247. This article has 28 citations.

13. (welters2024congenitalhyperinsulinismin pages 7-9): Alena Welters, Oliver Nortmann, Laura Wörmeyer, Clemens Freiberg, Daniel Eberhard, Nadine Bachmann, Carsten Bergmann, Ertan Mayatepek, Thomas Meissner, and Sebastian Kummer. Congenital hyperinsulinism in humans and insulin secretory dysfunction in mice caused by biallelic dnajc3 variants. International Journal of Molecular Sciences, 25:1270, Jan 2024. URL: https://doi.org/10.3390/ijms25021270, doi:10.3390/ijms25021270. This article has 1 citations.

14. (synofzik2015absenceofbip pages 1-1): Matthis Synofzik, Tobias B. Haack, Robert Kopajtich, Matteo Gorza, Doron Rapaport, Markus Greiner, Caroline Schönfeld, Clemens Freiberg, Stefan Schorr, Reinhard W. Holl, Michael A. Gonzalez, Andreas Fritsche, Petra Fallier-Becker, Richard Zimmermann, Tim M. Strom, Thomas Meitinger, Stephan Züchner, Rebecca Schüle, Ludger Schöls, and Holger Prokisch. Absence of bip co-chaperone dnajc3 causes diabetes mellitus and multisystemic neurodegeneration. The American Journal of Human Genetics, 96:514, Mar 2015. URL: https://doi.org/10.1016/j.ajhg.2015.02.003, doi:10.1016/j.ajhg.2015.02.003. This article has 146 citations.

15. (alwatban2021casereporthomozygous pages 6-7): Saud Alwatban, Haifa Alfaraidi, Abdulaziz Alosaimi, Iram Alluhaydan, Majid Alfadhel, Michel Polak, and Angham Almutair. Case report: homozygous dnajc3 mutation causes monogenic diabetes mellitus associated with pancreatic atrophy. Frontiers in Endocrinology, Sep 2021. URL: https://doi.org/10.3389/fendo.2021.742278, doi:10.3389/fendo.2021.742278. This article has 10 citations.

## Artifacts

- [Edison artifact artifact-00](Juvenile-Onset_Diabetes_Mellitus_with_Central_and_Peripheral_Neurodegeneration-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.