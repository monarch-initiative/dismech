---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-17T02:56:25.919872'
end_time: '2026-08-17T03:24:02.494660'
duration_seconds: 1656.57
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Neurodevelopmental Disorder with Hypotonia and Speech Delay, With
    or Without Seizures
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 4
reference_validation:
  total_references: 2
  verified: 2
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Neurodevelopmental_Disorder_with_Hypotonia_and_Speech_Delay-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder with Hypotonia and Speech Delay, With or Without Seizures
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder with Hypotonia and Speech Delay, With or Without Seizures** covering all of the
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
- **Disease Name:** Neurodevelopmental Disorder with Hypotonia and Speech Delay, With or Without Seizures
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder with Hypotonia and Speech Delay, With or Without Seizures** covering all of the
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


# Research report: Neurodevelopmental disorder with hypotonia and speech delay, with or without seizures

## Executive summary and evidence limits

**Neurodevelopmental disorder with hypotonia and speech delay, with or without seizures (NEDHSS)** is an extremely rare, recently delineated genetic neurodevelopmental disorder caused by pathogenic variation in **EIF4A2** (also called **DDX2B**). Its defining manifestations are developmental impairment—particularly delayed or severely impaired speech—hypotonia, and epilepsy in a subset of affected individuals. The principal human evidence is the 2023 founding report, *“Rare EIF4A2 variants are associated with a neurodevelopmental disorder characterized by intellectual disability, hypotonia, and epilepsy”* (PMID **36528028**). A 2024 authoritative review classified the EIF4A2–disease relationship as established, while noting predominantly de novo variants and one individual with a homozygous variant. (lederbauer2024theroleof pages 6-7, OpenTargets Search: Neurodevelopmental disorder with hypotonia and speech delay, with or without seizures-EIF4A2)

The evidence base remains very small. Consequently, prevalence, penetrance, most phenotype frequencies, long-term survival, validated genotype–phenotype relationships, treatment-response rates, and quality-of-life measurements cannot yet be estimated reliably. Statements below distinguish established disease-specific observations from reasonable clinical practice and mechanistic inference.

The following table provides ontology-ready summary annotations.

| Domain | Key findings for NEDHSS | Suggested ontology terms / identifiers | Evidence |
|---|---|---|---|
| Identity / identifiers | Disease name: **Neurodevelopmental disorder with hypotonia and speech delay, with or without seizures**; acronym **NEDHSS**. Authoritative disease identifiers available include **OMIM #620455** and **MONDO:0957541**. Disease-level information is derived from aggregated rare-disease/genotype-phenotype resources and the founding primary study, not EHR-only evidence. | **Validated identifiers:** OMIM:620455; MONDO:0957541. **Suggested synonym(s):** EIF4A2-related neurodevelopmental disorder; EIF4A2-related NDD. | (lederbauer2024theroleof pages 6-7, OpenTargets Search: Neurodevelopmental disorder with hypotonia and speech delay, with or without seizures-EIF4A2) |
| Causal gene / inheritance | Causal gene: **EIF4A2** (alias **DDX2B**), encoding eukaryotic translation initiation factor 4A2. Current understanding supports **predominantly de novo autosomal dominant** disease, with review-level evidence also noting **one individual with a homozygous variant**, so a possible **autosomal recessive** presentation remains uncertain. | **Validated gene:** EIF4A2 / ENSG00000156976. **Suggested inheritance terms:** HP:0000006 Autosomal dominant inheritance; HP:0000007 Autosomal recessive inheritance (uncertain/possible, not fully established). | (lederbauer2024theroleof pages 6-7, OpenTargets Search: Neurodevelopmental disorder with hypotonia and speech delay, with or without seizures-EIF4A2) |
| Core phenotypes | Core clinical concept from disease name and review evidence: **hypotonia**, **speech delay/language impairment**, and **seizures in a subset**. Broader developmental impairment/intellectual disability is also implicated in the primary association literature summarized by secondary sources. | **Suggested HPO terms:** HP:0001252 Hypotonia; HP:0002463 Delayed speech and language development; HP:0001250 Seizure; HP:0001263 Global developmental delay; HP:0001249 Intellectual disability. | (lederbauer2024theroleof pages 6-7, OpenTargets Search: Neurodevelopmental disorder with hypotonia and speech delay, with or without seizures-EIF4A2) |
| Mechanism / pathophysiology | EIF4A2 is a **DEAD-box RNA helicase** and part of the **translation-initiation machinery**; disease mechanism is currently understood at a high level as disruption of RNA helicase/translation-related neurodevelopmental processes. The 2024 review states that **missense and loss-of-function variants** are associated with NEDHSS, but disease-specific causal molecular cascades remain incompletely defined. | **Suggested GO terms:** GO:0003724 RNA helicase activity; GO:0006413 translational initiation; GO:0006412 translation; GO:0002181 cytoplasmic translation; GO:0003676 nucleic acid binding. **Suggested mechanism label:** disturbed post-transcriptional gene-expression control during neurodevelopment. | (lederbauer2024theroleof pages 6-7) |
| Anatomy / cell types | Primary system affected is the **nervous system/brain**; phenotype implies involvement of neural circuits supporting muscle tone, language, and seizure susceptibility. No disease-specific cell-type-resolved human dataset was identified in the retrieved evidence. | **Suggested UBERON terms:** UBERON:0001016 nervous system; UBERON:0000955 brain; UBERON:0002596 cerebral cortex. **Suggested CL terms:** CL:0000540 neuron; CL:0002319 neural cell; CL:0000127 astrocyte (supporting-cell hypothesis, not disease-specificly validated). | (lederbauer2024theroleof pages 6-7) |
| Diagnostics | Most informative disease-specific test category is **genetic testing**, especially exome/genome-based testing in individuals with unexplained developmental delay, hypotonia, and speech delay with/without seizures. Open Targets evidence links the disease to EIF4A2 through genetic evidence including variant databases; no disease-specific biochemical biomarker or imaging signature was identified in retrieved evidence. | **Suggested diagnostic approach terms:** trio WES/WGS; targeted reanalysis of NDD gene panels including EIF4A2. **Suggested HPO-driven indication terms:** HP:0001263, HP:0001252, HP:0002463, HP:0001250. | (OpenTargets Search: Neurodevelopmental disorder with hypotonia and speech delay, with or without seizures-EIF4A2, lederbauer2024theroleof pages 6-7) |
| Management | No NEDHSS-specific therapy or interventional trial was identified. Current management is supportive: developmental therapies, speech-language therapy, physical/occupational therapy, neurologic monitoring, and standard seizure management when epilepsy is present. | **Suggested NCIT terms:** Speech Therapy; Physical Therapy; Occupational Therapy; Anticonvulsant Therapy; Genetic Counseling. | (OpenTargets Search: Neurodevelopmental disorder with hypotonia and speech delay, with or without seizures-EIF4A2, lederbauer2024theroleof pages 6-7) |
| Major evidence gaps | Major unresolved areas include: true **prevalence/incidence**, penetrance/expressivity, disease-specific **variant catalog and genotype-phenotype correlations**, validated **functional mechanism**, **animal/model-system** evidence specific to NEDHSS, biomarkers, natural-history cohorts, treatment-response data, and environmental or gene-environment modifiers. | **Suggested evidence-gap tags:** epidemiology unavailable; no validated biomarker; no disease-specific clinical guidelines found; no relevant registered interventional trials found in retrieved searches. | (OpenTargets Search: Neurodevelopmental disorder with hypotonia and speech delay, with or without seizures-EIF4A2, lederbauer2024theroleof pages 6-7) |


*Table: This compact table summarizes the current evidence base and ontology-ready annotations for NEDHSS, including identifiers, causal gene, phenotype concepts, mechanism, anatomy, diagnostics, management, and key knowledge gaps. It is useful for knowledge-base population where suggested ontology terms must be distinguished from validated disease-specific findings.*

## 1. Disease information

### Definition

NEDHSS is a monogenic developmental disorder in which altered EIF4A2 function is associated with intellectual/global developmental impairment, hypotonia, marked speech or language delay, and variably present seizures. The phenotype belongs to the growing group of neurodevelopmental disorders caused by dysfunction of DEAD-box RNA helicases and post-transcriptional gene regulation. (lederbauer2024theroleof pages 6-7)

### Identifiers and synonyms

- **MONDO:** **MONDO:0957541**.
- **OMIM phenotype:** **#620455**.
- **Causal gene:** **EIF4A2**, alias **DDX2B**; Ensembl **ENSG00000156976**.
- **Preferred acronym:** **NEDHSS**.
- **Useful synonyms:** *EIF4A2-related neurodevelopmental disorder*; *EIF4A2-related NDD*; *neurodevelopmental disorder characterized by intellectual disability, hypotonia, and epilepsy*.
- **Orphanet, MeSH, ICD-10 and ICD-11:** no disorder-specific identifiers were established in the retrieved evidence. Coding will generally require broader developmental-disorder, hypotonia, speech/language-disorder, intellectual-disability, and epilepsy categories.

Open Targets associates only EIF4A2 with MONDO:0957541 and reports five evidence records linked to PMID 36528028; its aggregate target–disease score was approximately **0.743**. This is a database confidence score, not prevalence or penetrance. (OpenTargets Search: Neurodevelopmental disorder with hypotonia and speech delay, with or without seizures-EIF4A2)

The available information is primarily **aggregated disease-level evidence** derived from a published rare-disease cohort, variant databases, OMIM/MONDO, and expert review—not an individual-patient EHR dataset. (OpenTargets Search: Neurodevelopmental disorder with hypotonia and speech delay, with or without seizures-EIF4A2)

## 2. Etiology

### Causal and genetic factors

The established cause is germline variation in **EIF4A2**. The 2024 review states directly that “missense and loss-of-function variants in EIF4A2 (DDX2B) are associated with” NEDHSS and lists evidence from de novo variants plus one homozygous individual. The best-supported inheritance model is therefore **autosomal dominant, usually de novo**, while a possible recessive form remains provisional because it rests on one reported homozygous case. (lederbauer2024theroleof pages 6-7)

Open Targets aggregates missense and frameshift/other loss-of-function evidence and similarly records monoallelic and biallelic allelic requirements. Individual variants must nevertheless be interpreted under ACMG/AMP criteria rather than classified solely from gene-level association. (OpenTargets Search: Neurodevelopmental disorder with hypotonia and speech delay, with or without seizures-EIF4A2)

### Other risk, protective, and gene–environment factors

No environmental toxin, infection, radiation exposure, lifestyle behavior, parental age effect, susceptibility locus, modifier gene, protective allele, dietary factor, or reproducible gene–environment interaction has been established for NEDHSS. The disorder should therefore be represented as primarily genetic, not multifactorial. Absence of evidence is important here: environmental exposures should not be entered as causal or protective knowledge-base assertions.

## 3. Phenotypes

The core phenotype is pediatric neurodevelopmental impairment. Exact percentages from the founding EIF4A2 cohort were not recoverable from the available full-text evidence, so frequencies should be encoded qualitatively unless verified directly against PMID 36528028.

### Core manifestations

1. **Hypotonia**—clinical sign; typically congenital or recognized in infancy/early childhood; severity appears variable. Suggested HPO: **HP:0001252**.
2. **Delayed speech and language development**—developmental sign and functional impairment; a defining feature and potentially severe. Suggested HPO: **HP:0000750/HP:0002463** as locally appropriate; verify the current HPO label/version before production import.
3. **Global developmental delay**—pediatric developmental sign. Suggested HPO: **HP:0001263**.
4. **Intellectual disability**—cognitive phenotype; severity is variable in the reported disease spectrum. Suggested HPO: **HP:0001249**, with severity-specific children when documented.
5. **Seizures/epilepsy**—neurologic manifestation present in only a subset, as expressed by “with or without seizures.” Suggested HPO: **HP:0001250**; add seizure-type terms only from patient-level records.

Possible secondary consequences include delayed motor milestones, impaired mobility from hypotonia, communication dependence, educational support needs, feeding or safety issues associated with hypotonia, and injury or hospitalization risk when seizures are uncontrolled. These consequences are clinically plausible but should not be encoded as universal NEDHSS phenotypes without patient-level confirmation.

### Quality of life

No NEDHSS-specific EQ-5D, SF-36, PROMIS, caregiver-burden, or adaptive-function study was found. The expected major burdens are communication impairment, developmental dependence, therapy requirements, and—when present—epilepsy, but quantitative effects are unknown.

## 4. Genetic and molecular information

### Gene and protein

**EIF4A2** encodes eukaryotic translation initiation factor 4A-II, an ATP-dependent DEAD-box RNA helicase. It participates in translation initiation by remodeling RNA structure so that the translation machinery can scan structured 5′ untranslated regions. Its disease relevance therefore lies in post-transcriptional control of protein production rather than a classic metabolic-enzyme deficiency. EIF4A2 is also called **DDX2B**, explaining its inclusion in DEAD/DExH-box helicase reviews. (lederbauer2024theroleof pages 6-7)

### Pathogenic-variant spectrum

- Reported classes include **missense** and **loss-of-function**, including database-supported frameshift variants.
- Most established cases are **germline de novo heterozygous** variants.
- One **homozygous** individual has been reported, making recessive inheritance possible but not conclusively established.
- Somatic variation is not the basis of the constitutional disorder.
- Disease-causing alleles are expected to be absent or exceptionally rare in population databases, but exact gnomAD frequencies must be checked variant by variant.
- No validated founder variant, carrier frequency, mutational hotspot, modifier gene, or recurrent chromosomal rearrangement was established in the retrieved evidence. (OpenTargets Search: Neurodevelopmental disorder with hypotonia and speech delay, with or without seizures-EIF4A2, lederbauer2024theroleof pages 6-7)

The functional direction may differ by allele. It is therefore premature to label all NEDHSS variants uniformly as haploinsufficient, dominant-negative, or gain-of-function. Missense alleles could alter ATP/RNA binding, helicase kinetics, or protein interactions, whereas truncating variants may reduce functional dosage. Functional evidence is required for variant-specific conclusions.

### Epigenetics and chromosomal abnormalities

No reproducible NEDHSS episignature, DNA-methylation profile, histone abnormality, imprinting mechanism, or recurrent EIF4A2-containing copy-number syndrome was identified. Large deletions or duplications affecting EIF4A2 would require independent interpretation because neighboring genes may influence phenotype.

## 5. Environmental information

No disease-specific environmental, occupational, nutritional, infectious, smoking, alcohol, exercise, pollution, or radiation association is known. Infectious agents do not cause NEDHSS. Fever or illness may provoke seizures in susceptible individuals generally, but that is not evidence that infection causes the underlying disorder.

## 6. Mechanism and pathophysiology

### Proposed causal chain

**Pathogenic germline EIF4A2 variant → altered amount or biochemical activity of eIF4A-II → impaired ATP-dependent RNA remodeling and translation initiation → abnormal translation of developmentally important neuronal transcripts → disturbed neuronal maturation/circuit function → developmental delay, impaired speech/language, hypotonia, and variable seizure susceptibility.**

The upstream step—EIF4A2 variation—is established. The intermediate transcript targets, affected cell populations, and relationship between altered translation and individual clinical manifestations remain incompletely demonstrated and should be labeled **mechanistic inference**, not settled fact. The 2024 review confirms the disease association but does not provide a complete disease-specific molecular cascade. (lederbauer2024theroleof pages 6-7)

### Ontology suggestions

- **GO biological process:** translational initiation (**GO:0006413**); translation (**GO:0006412**); cytoplasmic translation (**GO:0002181**); RNA metabolic process (**GO:0016070**).
- **GO molecular function:** RNA helicase activity (**GO:0003724**); ATP binding (**GO:0005524**); RNA binding (**GO:0003723**).
- **GO cellular component:** cytoplasm (**GO:0005737**); eukaryotic translation-initiation-factor complex terms should be selected after confirming the current GO annotation for EIF4A2.
- **Candidate cell types:** neuron (**CL:0000540**), neural progenitor cell, cortical excitatory neuron, inhibitory interneuron, and motor neuron. Only the generic neuronal annotation is presently justified; subtype involvement has not been demonstrated directly.

No NEDHSS-specific metabolomic, lipidomic, proteomic, single-cell, spatial-transcriptomic, patient-organoid, CRISPR-screen, or integrated multi-omic signature was found. There is likewise no established immune, inflammatory, oxidative-stress, fibrosis, ischemia, or tissue-necrosis mechanism.

## 7. Anatomical structures affected

The primary affected system is the **nervous system**, especially brain networks underlying development, language, motor tone, and seizure control. Suggested terms include **UBERON:0001016 nervous system**, **UBERON:0000955 brain**, and—more cautiously—**UBERON:0000956 cerebral cortex** after ontology-version verification. Skeletal muscle may be functionally affected through central hypotonia, but a primary myopathy has not been established. No consistent lateralization is known.

At the subcellular level, the relevant process is cytoplasmic translation/RNA–protein complex function. Disease-specific damage to mitochondria, lysosomes, endoplasmic reticulum, myelin, or peripheral nerve has not been demonstrated.

## 8. Temporal development

Onset is congenital or early pediatric in concept: hypotonia and developmental delays become apparent during infancy or early childhood, while speech impairment becomes evident as language milestones are missed. Seizures may occur or remain absent. The available literature does not define formal early, intermediate, or advanced stages.

NEDHSS is expected to be lifelong. There is insufficient longitudinal evidence to determine whether motor or cognitive function is static, slowly improving with development and therapy, or progressive in particular genotypes. Regression, remission patterns, adult natural history, and critical treatment windows have not been characterized. Early childhood remains the practical intervention window for developmental therapies because of neuroplasticity, although this has not been tested specifically in NEDHSS.

## 9. Inheritance and population

- **Primary inheritance:** autosomal dominant, commonly de novo.
- **Possible additional inheritance:** autosomal recessive, based on one homozygous individual; uncertain.
- **Penetrance and expressivity:** not quantified; expressivity is evidently variable because seizures are optional and variant classes differ.
- **Anticipation:** not reported and not expected from the known sequence-variant mechanism.
- **Parental germline mosaicism:** not specifically documented but remains a standard possibility after an apparently de novo result.
- **Founder effects, consanguinity contribution, carrier frequency, ethnic enrichment, geographic clustering and sex ratio:** unknown.
- **Prevalence/incidence:** no population estimate is available; this is an ultra-rare disorder known from a small number of molecular diagnoses.

For a confirmed de novo dominant variant, sibling recurrence is low but not zero because of possible parental germline mosaicism; an affected individual's transmission risk is conventionally 50% per pregnancy. For a genuinely recessive family, parental carrier status would imply a 25% recurrence risk. Counseling must follow the actual variant and segregation result rather than the disease label alone.

## 10. Diagnostics

### Recommended approach

1. Document developmental, neurologic, speech-language, feeding, growth, and family histories; perform neurologic and dysmorphology examinations.
2. Use standardized developmental/cognitive, adaptive-function, motor, and speech-language assessments.
3. Perform **trio exome or genome sequencing** as a preferred molecular approach, or an NDD/epilepsy panel that includes EIF4A2. Trio analysis is especially useful for establishing de novo occurrence.
4. Confirm clinically significant variants with an orthogonal method and perform parental segregation testing.
5. Apply ACMG/AMP criteria using population frequency, predicted molecular consequence, inheritance, phenotype fit, ClinVar assertions, and functional evidence.

CMA remains useful when a copy-number disorder is possible; genome sequencing can detect sequence and structural variants simultaneously. Karyotyping or FISH is not a primary EIF4A2 test unless a rearrangement is suspected. Mitochondrial, repeat-expansion, or biochemical testing should be driven by the differential diagnosis rather than ordered specifically for NEDHSS. No diagnostic blood, urine, CSF, enzyme, proteomic, metabolomic, or epigenetic biomarker is validated. Open Targets’ genetic evidence supports EIF4A2 as the molecular marker but is not itself a diagnostic assay. (OpenTargets Search: Neurodevelopmental disorder with hypotonia and speech delay, with or without seizures-EIF4A2)

### Phenotype-directed studies

- **EEG** for suspected seizures, regression, or episodic altered awareness.
- **Brain MRI** when seizures, focal neurologic findings, abnormal head growth, regression, or another structural disorder is suspected; no pathognomonic NEDHSS MRI pattern is known.
- **Hearing and vision assessment**, because sensory impairment can aggravate communication delay.
- Feeding/swallowing, sleep, orthopedic, and respiratory evaluations when clinically indicated.

### Differential diagnosis

The differential is broad and includes other RNA-helicase/translation disorders—especially DDX3X-, DDX6-, and DHX30-related disease—as well as PURA syndrome, Phelan–McDermid syndrome, Angelman syndrome, Pitt–Hopkins syndrome, HNRNPU-related disorder, and ion-channel developmental epileptic encephalopathies. Molecular testing is essential because hypotonia, language delay, intellectual disability, and seizures are nonspecific.

There are no validated clinical diagnostic criteria, newborn-screening assay, or population screening program. Cascade testing is appropriate once a familial pathogenic or likely pathogenic variant is established.

## 11. Outcome and prognosis

No 5- or 10-year survival, life-expectancy, mortality, hospitalization, or disease-specific disability statistic is available. There is no evidence that NEDHSS is intrinsically degenerative or life-limiting, but severe developmental disability and uncontrolled epilepsy can increase morbidity. Long-term communication, independent living, mobility, and educational outcomes have not been quantified.

Potential prognostic factors—still unvalidated—include severity of early developmental impairment, presence and control of epilepsy, feeding or respiratory complications associated with hypotonia, and variant-specific functional effect. There is no validated prognostic biomarker.

## 12. Treatment

### Current care

There is no approved EIF4A2-directed or disease-modifying therapy. Management is individualized and multidisciplinary:

- **Speech-language therapy**, including augmentative and alternative communication when needed.
- **Physical therapy** for hypotonia, posture, mobility, and contracture prevention.
- **Occupational therapy** for fine-motor and adaptive skills.
- Early developmental/educational intervention and behavioral support.
- Feeding evaluation, nutritional support, and swallow-safety intervention when indicated.
- Standard antiseizure medication selected by seizure type and tolerability; no NEDHSS-specific preferred drug or response rate is known.
- Orthopedic, sleep, respiratory, vision, and hearing management according to manifestations.
- Genetic counseling and family psychosocial support.

Suggested NCIT intervention concepts include **Speech Therapy**, **Physical Therapy**, **Occupational Therapy**, **Anticonvulsant Therapy**, **Assistive Communication Device**, and **Genetic Counseling**; exact NCIT codes should be resolved against the current NCIT release.

No disease-specific pharmacogenomic guidance, surgical treatment, gene replacement, CRISPR therapy, antisense oligonucleotide, RNA therapy, cell therapy, immunotherapy, or combination-treatment algorithm has been validated. Dedicated ClinicalTrials.gov searches found no relevant NEDHSS/EIF4A2 interventional trial in the retrieved results.

## 13. Prevention

Primary prevention through lifestyle or environmental modification is not possible for a germline monogenic disorder. Relevant measures are reproductive and tertiary:

- Pre- and post-test genetic counseling.
- Parental testing and recurrence-risk assessment, including discussion of germline mosaicism.
- Prenatal diagnosis or preimplantation genetic testing when a familial pathogenic variant is known, subject to local practice and family preference.
- Early recognition, developmental intervention, seizure surveillance, and feeding/respiratory safety measures to reduce secondary disability and complications.

Vaccination, antimicrobial prophylaxis, environmental remediation, and public-health control programs do not prevent NEDHSS.

## 14. Other species and natural disease

No naturally occurring EIF4A2-associated NEDHSS analogue in companion animals, livestock, or wildlife was identified. There is no zoonotic potential or cross-species transmission because this is an inherited genetic condition. EIF4A2 orthologs and core translation-initiation mechanisms are evolutionarily conserved, supporting comparative functional studies, but conservation alone does not constitute a natural animal disease model.

## 15. Model organisms and experimental systems

No sufficiently documented NEDHSS-specific mouse, rat, zebrafish, Drosophila, *C. elegans*, patient-iPSC, neural-organoid, or isogenic cellular model was identified in the retrieved disease evidence. This is a major research gap. Priority models would include:

- Patient-variant knock-in and conditional neuronal mouse models.
- Zebrafish or Drosophila assays for developmental, locomotor, and seizure phenotypes.
- Patient-derived iPSC neurons and cortical organoids.
- Ribosome profiling, quantitative translation assays, RNA interactomics, and rescue with wild-type EIF4A2.

Such systems should test whether individual alleles cause loss of function, dominant-negative interference, gain of function, or altered transcript selectivity. Model validity would require rescue experiments and concordance with human hypotonia, developmental, language-network, and seizure phenotypes.

## Recent developments and authoritative interpretation

The decisive development was the 2023 primary association study (PMID **36528028**), which established rare EIF4A2 variants as a cause of a disorder characterized by intellectual disability, hypotonia, and epilepsy. In August 2024, Lederbauer and colleagues reviewed DEAD/DExH-box helicases in neurodevelopmental disease and classified EIF4A2 as a **definitely established** NDD gene, naming NEDHSS and OMIM #620455. Their evidence summary records “de novo variants, 1 individual with a homozygous variant,” supporting dominant inheritance while leaving recessive inheritance uncertain. DOI: **10.3389/fnmol.2024.1414949**; URL: https://doi.org/10.3389/fnmol.2024.1414949. (lederbauer2024theroleof pages 6-7)

Open Targets currently maps EIF4A2 to **MONDO:0957541**, with genetic evidence repeatedly linked to PMID 36528028. This is useful external corroboration, although it does not replace case-level clinical interpretation. (OpenTargets Search: Neurodevelopmental disorder with hypotonia and speech delay, with or without seizures-EIF4A2)

## Principal references

1. Paul MS, Duncan AR, Genetti CA, Pan H, Jackson A, Grant PE, et al. **Rare EIF4A2 variants are associated with a neurodevelopmental disorder characterized by intellectual disability, hypotonia, and epilepsy.** *American Journal of Human Genetics*. 2023;110:548 ff. PMID: **36528028**. Publication record: https://pubmed.ncbi.nlm.nih.gov/36528028/. This is the foundational primary human genetic report. (OpenTargets Search: Neurodevelopmental disorder with hypotonia and speech delay, with or without seizures-EIF4A2)
2. Lederbauer J, Das S, Piton A, Lessel D, Kreienkamp H-J. **The role of DEAD- and DExH-box RNA helicases in neurodevelopmental disorders.** *Frontiers in Molecular Neuroscience*. Published August 2024;17:1414949. DOI: **10.3389/fnmol.2024.1414949**. https://doi.org/10.3389/fnmol.2024.1414949. This is the key recent expert review and source for the current evidence classification. (lederbauer2024theroleof pages 6-7)

### Knowledge-base caution

Only the disease identity, EIF4A2 association, core hypotonia/speech-development/seizure phenotype, principal variant classes, and predominantly de novo inheritance should presently be treated as high-confidence disease assertions. Numerical phenotype frequencies, variant-level mechanisms, recessive inheritance, progression, adult prognosis, biomarkers, and treatment efficacy require direct validation in larger cohorts and should be encoded as provisional or unknown.

References

1. (lederbauer2024theroleof pages 6-7): Johannes Lederbauer, Sarada Das, Amelie Piton, Davor Lessel, and Hans-Jürgen Kreienkamp. The role of dead- and dexh-box rna helicases in neurodevelopmental disorders. Frontiers in Molecular Neuroscience, Aug 2024. URL: https://doi.org/10.3389/fnmol.2024.1414949, doi:10.3389/fnmol.2024.1414949. This article has 4 citations.

2. (OpenTargets Search: Neurodevelopmental disorder with hypotonia and speech delay, with or without seizures-EIF4A2): Open Targets Query (Neurodevelopmental disorder with hypotonia and speech delay, with or without seizures-EIF4A2, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

## Artifacts

- [Edison artifact artifact-00](Neurodevelopmental_Disorder_with_Hypotonia_and_Speech_Delay-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 2 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |

All extracted references resolved successfully.