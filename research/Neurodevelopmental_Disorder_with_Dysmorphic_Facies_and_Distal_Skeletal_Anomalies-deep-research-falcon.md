---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-15T08:32:04.584198'
end_time: '2026-08-15T08:42:38.578115'
duration_seconds: 633.99
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Neurodevelopmental Disorder with Dysmorphic Facies and Distal Skeletal
    Anomalies
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 7
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Neurodevelopmental_Disorder_with_Dysmorphic_Facies_and_Distal_Skeletal_Anomalies-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder with Dysmorphic Facies and Distal Skeletal Anomalies
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder with Dysmorphic Facies and Distal Skeletal Anomalies** covering all of the
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
- **Disease Name:** Neurodevelopmental Disorder with Dysmorphic Facies and Distal Skeletal Anomalies
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder with Dysmorphic Facies and Distal Skeletal Anomalies** covering all of the
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


# Neurodevelopmental Disorder with Dysmorphic Facies and Distal Skeletal Anomalies

## Executive summary

**Neurodevelopmental disorder with dysmorphic facies and distal skeletal anomalies (NDDFDSA)** is an ultra-rare, predominantly de novo autosomal-dominant developmental disorder caused by pathogenic variation affecting **ZMIZ1**, a transcriptional coregulator associated with chromatin remodeling. The syndrome is characterized principally by developmental delay/intellectual disability, speech and behavioral abnormalities, recognizable facial dysmorphism, and distal limb/skeletal anomalies. Current knowledge comes from small case series, individual case reports, curated disease resources, and experimental models—not population-scale cohorts or EHR studies. Open Targets associates the disease specifically with ZMIZ1 and traces the principal human evidence to Carapito et al., 2019 (PMID **30639322**). (OpenTargets Search: Neurodevelopmental disorder with dysmorphic facies and distal skeletal anomalies, c.2024zmiz1isa pages 14-15)

The most important recent development is a 2024 cortex-specific mouse and transcriptomic study. It showed embryonically enriched ZMIZ1 expression, altered cortical neurogenesis and synaptic-gene expression after Zmiz1 deletion, reduced motor-cortex and layer-6 thickness, and increased repetitive behavior. These data support a causal chain from altered transcription/chromatin regulation to defective neuronal differentiation, connectivity, and synaptic signaling. They do **not**, however, establish a druggable pathway or disease-specific treatment. (c.2024zmiz1isa pages 6-8, c.2024zmiz1isa pages 2-3, c.2024zmiz1isa pages 1-2)

| Domain | Established finding | Evidence type/strength | Key identifier or ontology suggestion |
|---|---|---|---|
| Disease identity | Rare Mendelian neurodevelopmental syndrome defined as **Neurodevelopmental disorder with dysmorphic facies and distal skeletal anomalies**; disease-target resources link it specifically to **ZMIZ1**. (OpenTargets Search: Neurodevelopmental disorder with dysmorphic facies and distal skeletal anomalies, c.2024zmiz1isa pages 14-15) | Disease-level curated database association plus foundational primary literature citation | **OMIM 618659**; **EFO_0010659**; suggested MONDO label: ZMIZ1-associated neurodevelopmental disorder |
| Causal gene | Established causal gene is **ZMIZ1** (*zinc finger MIZ-type containing 1*); Open Targets shows this disease associated with **ZMIZ1** only. (OpenTargets Search: Neurodevelopmental disorder with dysmorphic facies and distal skeletal anomalies, c.2024zmiz1isa pages 14-15) | Curated disease-gene association supported by human primary literature | **ZMIZ1**; **ENSG00000108175** |
| Inheritance | Reported as a dominant developmental disorder largely driven by **de novo** pathogenic variants/rearrangements; practical counseling frame is **mostly de novo autosomal dominant**. (c.2024zmiz1isa pages 1-2, c.2024zmiz1isa pages 14-15) | Human disease literature and review-level synthesis; moderate confidence | Suggested inheritance term: autosomal dominant; HPO inheritance concept validation recommended |
| Data provenance | Current knowledge is derived from **aggregated disease-level resources** and **small human case reports/series**, not EHR-scale cohorts. (OpenTargets Search: Neurodevelopmental disorder with dysmorphic facies and distal skeletal anomalies, c.2024zmiz1isa pages 14-15) | Strong resource-level observation | Evidence source class: rare-disease case-series aggregation |
| Core phenotype categories | Core manifestations span **global neurodevelopmental impairment** (ID/developmental delay), **behavioral/neuropsychiatric features** (including ASD/ADHD-related features), **dysmorphic facies**, and **distal skeletal anomalies**; additional reported features may broaden the spectrum. (c.2024zmiz1isa pages 1-2, c.2024zmiz1isa pages 10-11, c.2024zmiz1isa pages 15-16, c.2024zmiz1isa pages 14-15) | Human syndrome reports plus broader 2024 synthesis; moderate confidence because exact frequencies were not extracted | Suggested HPO anchors: **Intellectual disability**, **Global developmental delay**, **Autistic behavior**, **Attention deficit hyperactivity disorder**, **Abnormal facial shape**, **Skeletal dysplasia/anomaly of the distal limbs** |
| Onset/course | Disorder is best understood as **congenital/early-childhood onset neurodevelopmental disease** affecting brain development, with persistent developmental and behavioral consequences rather than a remitting course. (c.2024zmiz1isa pages 2-3, c.2024zmiz1isa pages 1-2) | Indirect but strong developmental-biology support plus human phenotype framing | Suggested HPO anchors: **Congenital onset**, **Developmental delay** |
| Molecular function | ZMIZ1 acts as a **transcriptional co-regulator/co-activator** and **chromatin remodeler-associated factor** rather than a classic DNA-binding transcription factor. (c.2024zmiz1isa pages 2-3, c.2024zmiz1isa pages 3-6) | Strong mechanistic support from structural/epigenetic analyses and prior literature synthesis | Suggested GO: **transcription coregulator activity**, **chromatin organization**, **positive regulation of transcription by RNA polymerase II** |
| Structural biology | ZMIZ1 is highly constrained for loss-of-function and is enriched for **intrinsically disordered regions** and **linear interacting peptides**, supporting roles in multiprotein complex assembly and regulatory signaling. (c.2024zmiz1isa pages 2-3, c.2024zmiz1isa pages 3-6) | Strong computational/structural evidence integrated with disease interpretation | Suggested annotations: intrinsically disordered protein; protein complex assembly |
| Chromatin/epigenetic mechanism | ZMIZ1-bound sites are associated with **activating histone marks** (H3K4me1/2/3, H3K9ac, H3K27ac, H3K79me2) and minimal repressive marks, supporting a model of **transcriptional activation/open chromatin regulation**. (c.2024zmiz1isa pages 2-3, c.2024zmiz1isa pages 6-8, c.2024zmiz1isa pages 3-6) | Strong mechanistic evidence from public ChIP/epigenomic analyses | Suggested GO: **histone modification**, **chromatin remodeling**; CHEBI suggestions: **H3K27ac**, **H3K9ac** |
| Developmental expression | ZMIZ1 is **highly expressed in embryonic brain** in mouse and human, then decreases postnatally; enrichment is notable in **cortex, hippocampus, and cerebellum** and in excitatory projection-neuron lineages. (c.2024zmiz1isa pages 1-2, c.2024zmiz1isa pages 2-3) | Strong expression evidence from public transcriptomic atlases | UBERON: **cerebral cortex**, **hippocampus**, **cerebellum**; CL suggestions: **cortical projection neuron**, **excitatory neuron**, **oligodendrocyte precursor cell**, **astrocyte**, **endothelial cell** |
| Pathophysiology | Best-supported causal chain: **ZMIZ1 dysfunction → altered chromatin/transcriptional regulation during embryonic brain development → impaired neurogenesis, neuronal differentiation, axon/projection development, and synaptic signaling → neurodevelopmental and behavioral phenotypes**. (c.2024zmiz1isa pages 2-3, c.2024zmiz1isa pages 6-8, c.2024zmiz1isa pages 10-11) | Strong multi-layer evidence from mouse transcriptomics and integrated biology; human mechanism remains inferential | Suggested GO: **neurogenesis**, **neuron differentiation**, **axon development**, **synaptic signaling**, **chemical synaptic transmission** |
| Pathway/network context | Interaction/network analyses place ZMIZ1 with **NOTCH1, TP53, SMAD3/4, AR, CTNNB1, CNTNAP2, TBR1, SATB1**, and other neurodevelopmentally relevant factors; synaptic pathways affected include **AMPA receptor activation**, **GABA signaling**, and **neurotransmitter release cycle**. (c.2024zmiz1isa pages 8-10, c.2024zmiz1isa pages 10-11, c.2024zmiz1isa pages 6-8) | Moderate-to-strong systems-level evidence | Suggested pathway tags: **Notch signaling**, **synaptic signaling**, **glutamatergic signaling**, **GABAergic signaling** |
| 2024 mouse model findings | Cortex-specific **Zmiz1 knockout** caused **104 DEGs** at P7, reduced **motor cortical thickness** with significant **layer 6 thinning** at P3, and increased **repetitive behavior** in marble-burying assays; synaptic genes such as **Gria2, Tnc, Cplx3** were downregulated. (c.2024zmiz1isa pages 6-8, c.2024zmiz1isa pages 8-10, c.2024zmiz1isa pages 11-12) | Strong primary in vivo evidence (mouse) from 2024 study | Model type: conditional mouse knockout; GO/CL suggestions: **corticothalamic projection neuron**, **callosal projection neuron** |
| Diagnostic approach | Diagnosis is primarily **molecular**, usually by **exome/genome sequencing** or broad neurodevelopmental disorder testing, with CNV/structural-variant methods relevant because translocations/rearrangements involving ZMIZ1 have also been reported. (c.2024zmiz1isa pages 14-15, c.2024zmiz1isa pages 1-2) | Strong practice inference from gene-discovery context and structural-variant literature | Suggested tests: **WES**, **WGS**, **trio sequencing**, **chromosomal microarray**, **structural variant analysis** |
| Differential diagnosis | Differential diagnosis includes other **syndromic intellectual disability/autism disorders** with facial and skeletal findings, especially disorders involving transcriptional/chromatin regulators. (c.2024zmiz1isa pages 1-2, c.2024zmiz1isa pages 10-11) | Indirect but reasonable syndrome-level inference | Suggested ontology grouping: syndromic neurodevelopmental disorder |
| Management | No disease-specific therapy is established; management is **supportive and phenotype-directed**, including developmental surveillance, **speech/occupational/physical therapy**, behavioral/psychiatric care, and organ-system evaluation guided by individual findings. (c.2024zmiz1isa pages 10-11, c.2024zmiz1isa pages 11-12) | Standard-of-care inference for rare Mendelian NDDs; limited disease-specific outcome data | NCIT suggestions: **Speech Therapy**, **Occupational Therapy**, **Physical Therapy**, **Behavioral Intervention** |
| Prevention/genetic counseling | Primary prevention is not established; after variant identification, families may receive **genetic counseling**, recurrence-risk assessment, and options for **prenatal diagnosis** or **preimplantation genetic testing**. (c.2024zmiz1isa pages 1-2, c.2024zmiz1isa pages 14-15) | Standard Mendelian-genetics practice inference | NCIT suggestions: **Genetic Counseling**, **Prenatal Genetic Testing**, **Preimplantation Genetic Diagnosis** |
| Epidemiology | **Prevalence, incidence, sex ratio, penetrance, expressivity estimates, carrier frequency, and founder effects are not established** from currently retrieved evidence. (OpenTargets Search: Neurodevelopmental disorder with dysmorphic facies and distal skeletal anomalies, c.2024zmiz1isa pages 14-15) | Major evidence gap | Evidence-gap flag |
| Variant-level detail | Exact **patient counts, phenotype frequencies, and HGVS-level variant list** from the foundational cohort were not available in retrieved full-text evidence and should not be imputed. (OpenTargets Search: Neurodevelopmental disorder with dysmorphic facies and distal skeletal anomalies, c.2024zmiz1isa pages 14-15) | Major evidence gap / inaccessible detailed cohort tabulation | Curation priority: retrieve full Carapito et al. 2019 and later case reports |
| Treatments/clinical trials | No disease-specific **approved targeted therapy** or **relevant interventional clinical trial** was identified in the retrieved searches. (OpenTargets Search: Neurodevelopmental disorder with dysmorphic facies and distal skeletal anomalies) | Search-based negative finding | Evidence-gap flag; supportive care remains standard |


*Table: This table summarizes the highest-confidence established facts for ZMIZ1-associated neurodevelopmental disorder, including identity, inheritance, mechanism, model evidence, diagnostics, management, and major evidence gaps. It is designed as a compact curation aid for a disease knowledge base.*

## 1. Disease information

### Definition and identifiers

- **Preferred name:** Neurodevelopmental disorder with dysmorphic facies and distal skeletal anomalies.
- **Common alternatives:** NDDFDSA; ZMIZ1-associated neurodevelopmental disorder; ZMIZ1-related neurodevelopmental disorder; syndromic intellectual disability due to ZMIZ1 variants.
- **OMIM:** **#618659**.
- **Open Targets/EFO:** **EFO_0010659**.
- **Causal-gene identifiers:** **ZMIZ1**, *zinc finger MIZ-type containing 1*; Ensembl **ENSG00000108175**; UniProt **Q9ULJ6**.
- **MONDO:** A definitive MONDO identifier was not recovered in the available evidence; the disease should not be confused with similarly named TRPM3- or RNU4-2-associated disorders. Open Targets returns ZMIZ1 as the sole target for EFO_0010659. (OpenTargets Search: Neurodevelopmental disorder with dysmorphic facies and distal skeletal anomalies)
- **Orphanet, MeSH, ICD-10/ICD-11:** No disease-specific identifiers were established in the retrieved evidence. Clinically, patients are generally coded under broader intellectual disability, developmental disorder, congenital-anomaly, or genetic-syndrome categories.

The landmark report is Carapito et al., **“ZMIZ1 variants cause a syndromic neurodevelopmental disorder,”** *American Journal of Human Genetics*, published 2019, 104:319–330, DOI [10.1016/j.ajhg.2018.12.007](https://doi.org/10.1016/j.ajhg.2018.12.007), PMID **30639322**. (OpenTargets Search: Neurodevelopmental disorder with dysmorphic facies and distal skeletal anomalies, c.2024zmiz1isa pages 14-15)

### Data provenance

Evidence is aggregated at disease level from OMIM/Open Targets and from rare-disease case ascertainment, exome/genome sequencing, structural-variant studies, and isolated clinical reports. It is not based on a population registry or longitudinal EHR cohort. The 2024 mechanistic investigation used public human datasets and a conditional mouse model; it did not recruit a new human cohort. (c.2024zmiz1isa pages 1-2, c.2024zmiz1isa pages 14-15)

## 2. Etiology

### Causal factors and genetic risk

The primary cause is germline disruption of **ZMIZ1** by pathogenic coding variants, regulatory variants, or chromosomal rearrangements affecting the gene or its regulatory context. Most reported disease-associated variants are de novo, supporting autosomal-dominant inheritance. ZMIZ1 is highly constrained against loss-of-function variation: only 7 loss-of-function variants were observed versus 52.1 expected in the referenced dataset, corresponding to an observed/expected ratio of **0.13**. Missense constraint was less extreme but still evident (447 observed versus 699.1 expected; ratio **0.64**). (c.2024zmiz1isa pages 2-3)

Disease-associated single-nucleotide variants are distributed across the protein but cluster in the TPR, alanine-rich, central proline-rich, and C-terminal proline-rich domains. The 2024 analysis estimated that 65% of disease-causing SNVs occurred in those regions; normalized by domain length, the alanine-rich region had the largest reported mutation burden. This is computational/domain-level evidence, not a validated genotype–phenotype rule. (c.2024zmiz1isa pages 3-6)

Balanced chromosomal rearrangements may disrupt ZMIZ1 directly or produce position effects, so pathogenicity is not restricted to SNVs or small indels. This supports genome/structural-variant analysis where exome testing is negative. (c.2024zmiz1isa pages 14-15)

### Environmental, infectious, and lifestyle risk

No environmental toxin, infection, diet, lifestyle, occupational exposure, parental-age effect, or sex-specific risk has been established for NDDFDSA. Environmental factors can affect neurodevelopment generally, but none should be entered as a disease-specific causal factor without further evidence.

### Protective factors and gene–environment interaction

No protective alleles, modifier genes, preventive exposures, or demonstrated gene–environment interactions are known. ZMIZ1 has broader associations with immune regulation and vitamin-D-responsive biology, but these observations concern other phenotypes and do not establish vitamin D or immune exposure as a modifier of NDDFDSA. (c.2024zmiz1isa pages 15-16)

## 3. Phenotypes

### Core phenotype framework

The directly supported phenotype spectrum includes developmental delay/intellectual impairment, speech-development delay, motor impairment, autism-related or social-communication deficits, repetitive or other behavioral abnormalities, dysmorphic facial features, and distal skeletal abnormalities. Seizures have been described among the broader human phenotypes cited by the 2024 study, but exact disease-specific frequency was not recoverable. (c.2024zmiz1isa pages 10-11)

Suggested knowledge-base mappings are:

| Phenotype category | Type, onset, course, and functional effect | Suggested HPO terms |
|---|---|---|
| Developmental delay/intellectual disability | Developmental sign; apparent in infancy or childhood; severity and expressivity variable; generally persistent and lifelong. Affects learning, independence, and adaptive function. | Global developmental delay **HP:0001263**; Intellectual disability **HP:0001249** |
| Speech/language delay | Developmental symptom, generally early childhood; can materially impair communication and education. | Delayed speech and language development **HP:0000750** |
| Autism/social-communication abnormalities | Behavioral phenotype; childhood onset; variable severity and persistence. | Autistic behavior **HP:0000729**; Abnormal social behavior **HP:0012433** |
| Attention/hyperactivity or aggression/anxiety | Behavioral changes; variably reported rather than obligatory. | Attention deficit hyperactivity disorder **HP:0007018**; Aggressive behavior **HP:0000718**; Anxiety **HP:0000739** |
| Motor delay or impaired motor function | Developmental sign; may affect mobility and daily activities. | Motor delay **HP:0001270**; Abnormality of movement **HP:0100022** |
| Seizures | Neurologic sign reported in the broader spectrum; frequency, type, and prognosis not established. | Seizure **HP:0001250** |
| Facial dysmorphism | Congenital physical manifestation; specific combinations vary among individuals. | Abnormal facial shape **HP:0001999**; individual facial HPO terms should be curated patient by patient |
| Distal skeletal/limb anomalies | Congenital physical findings involving hands, fingers, feet, or toes; generally structural and stable. | Abnormality of the hand **HP:0001155**; Abnormality of the foot **HP:0001760**; Abnormality of the digits **HP:0011297** |
| Hirschsprung disease | Reported in a 2021 patient with a de novo pathogenic ZMIZ1 variant; possible spectrum expansion, not an established common feature. | Hirschsprung disease **HP:0002251** |

The 2021 Hirschsprung case is Valind et al., *Journal of Pediatric Surgery Case Reports* 71:101889, DOI [10.1016/j.epsc.2021.101889](https://doi.org/10.1016/j.epsc.2021.101889). The 2024 authors state: **“a case study revealed a de novo pathogenic variant in ZMIZ1 in a patient with developmental delay and Hirschsprung Disease.”** (c.2024zmiz1isa pages 10-11, c.2024zmiz1isa pages 15-16)

### Frequencies and quality of life

Reliable percentages for individual clinical features could not be extracted from the available foundational full text. Frequencies should therefore remain **unknown**, not be estimated from the syndrome name or from secondary summaries. No EQ-5D, SF-36, PROMIS, disease-specific quality-of-life instrument, or formal caregiver-burden study was identified. Functional burden is nevertheless expected from impaired cognition, communication, behavior, and motor development.

## 4. Genetic and molecular information

### Gene and protein

**ZMIZ1** encodes a PIAS-like transcriptional coregulator, also called Zimp10. The protein is unusually disordered: the 2024 analysis classified approximately **66.4%** as intrinsically disordered and **50.3%** as linear interacting peptides, whereas about 22.3% comprised structured functional domains. These properties are consistent with multiprotein-complex formation, transcriptional regulation, and potentially phase-separated regulatory assemblies. (c.2024zmiz1isa pages 3-6)

### Variant spectrum and classification

Reported disease mechanisms encompass de novo missense and other coding variants, regulatory-region variation, direct gene disruption, and chromosomal position effects. Exact HGVS variants and patient-level ACMG classifications from the foundational cohort were unavailable in the retrieved text and should be obtained directly from PMID 30639322 and current ClinVar records before variant-level database ingestion. (c.2024zmiz1isa pages 2-3, c.2024zmiz1isa pages 14-15)

The variants are germline in the congenital syndrome. Somatic ZMIZ1 alterations are relevant to cancer biology but are not causal evidence for NDDFDSA. Population allele frequencies for individual pathogenic variants were not recovered; pathogenic de novo variants would generally be expected to be absent or exceptionally rare in reference populations, but each variant requires direct gnomAD/ClinVar verification.

### Functional consequence

The most coherent current model is altered dosage or function of a transcriptional coactivator, producing dysregulated developmental gene expression. Although haploinsufficiency/functional loss is strongly supported by gene constraint and knockout phenotypes, not every missense allele has been experimentally proven to act through simple loss of function. Dominant-negative or allele-specific effects therefore remain possible for some variants.

### Modifier genes, chromosomal abnormalities, and epigenetics

No validated modifier gene is known. Candidate interacting proteins include NOTCH1, TP53, SMAD3/4, androgen receptor, CTNNB1, CNTNAP2, SATB1, TBR1, HDAC1, BRCA1, and SWI/SNF/BAF components SMARCA4 and SMARCE1. These are interaction/network candidates, not proven clinical modifiers. (c.2024zmiz1isa pages 8-10, c.2024zmiz1isa pages 10-11)

At ZMIZ1-bound sites, activating marks H3K4me1/2/3, H3K9ac, H3K27ac, and H3K79me2 were enriched, while H3K9me3 and H3K27me3 were minimal in K562 ENCODE-derived analyses. This supports coactivator/open-chromatin function but is not a disease-specific patient methylation signature. (c.2024zmiz1isa pages 6-8, c.2024zmiz1isa pages 3-6)

## 5. Environmental information

No disease-specific environmental, lifestyle, infectious, nutritional, radiation, or occupational determinant has been demonstrated. Smoking, alcohol, diet, and exercise have no established role in causing or preventing this monogenic congenital disorder. Standard avoidance of teratogens remains general prenatal care rather than NDDFDSA-specific prevention.

## 6. Mechanism and pathophysiology

### Causal chain

1. A pathogenic germline ZMIZ1 variant or structural disruption alters ZMIZ1 dosage/function.
2. The defect perturbs transcriptional coregulation and chromatin-associated developmental programs during embryogenesis.
3. Neurogenesis, neuronal differentiation, axon/projection morphogenesis, and synaptic-gene expression become dysregulated.
4. Cortical architecture and excitatory/inhibitory circuit development are altered.
5. These upstream developmental changes plausibly produce intellectual, language, motor, autistic/behavioral, and seizure phenotypes. Parallel effects in craniofacial and distal skeletal developmental programs likely produce dysmorphism and limb anomalies, although the skeletal causal chain is much less experimentally resolved. (c.2024zmiz1isa pages 6-8, c.2024zmiz1isa pages 2-3)

### Recent transcriptomic and pathway evidence

In cortex-specific Zmiz1-knockout mice, P7 RNA sequencing identified **104 differentially expressed genes**, including 35 downregulated and 69 upregulated genes. Sixteen overlapped SFARI autism-risk genes, including **ABAT, AHI1, CACNA2D1, CACNA2D3, CUX2, DPYSL2, GRIA1, GRIA2, RORB, SATB1, SATB2, SLC6A1, TAOK1, TCF4**, and ZMIZ1. Twenty-six DEGs mapped to SynGO genes. Enriched processes included neurogenesis, neuron differentiation, axon development, neuron-projection morphogenesis, synapse organization, neurotransmitter release, AMPA-receptor activation, chemical synaptic transmission, and GABA signaling. (c.2024zmiz1isa pages 8-10, c.2024zmiz1isa pages 6-8)

The authors directly reported that **“Biological processes such as neurogenesis, neuron development and differentiation, axon development, and neuron projection morphogenesis were significantly affected in the Zmiz1-KO cortex.”** They also found downregulation of **Gria2, Tnc, and Cplx3** by qPCR. (c.2024zmiz1isa pages 10-11, c.2024zmiz1isa pages 6-8)

### Cell and tissue context

ZMIZ1 expression peaks during mouse embryonic days E12–E18 and declines postnatally; human brain data show a comparable prenatal enrichment. Expression is highest in cortex and cerebellum and is also prominent in hippocampus. It occurs in neurons, endothelial cells, pericytes, astrocytes, Bergmann glia, oligodendrocytes, and oligodendrocyte precursor cells, with stronger expression in excitatory than GABAergic neurons. Cortical ventricular/subventricular progenitors and callosal and corticothalamic projection-neuron lineages are particularly relevant. (c.2024zmiz1isa pages 2-3, c.2024zmiz1isa pages 1-2)

Suggested ontology terms include:

- **GO biological process:** neurogenesis **GO:0022008**; neuron differentiation **GO:0030182**; axon development **GO:0061564**; synaptic signaling **GO:0099536**; chemical synaptic transmission **GO:0007268**; chromatin organization **GO:0006325**.
- **GO cellular component:** nucleus **GO:0005634**; chromatin **GO:0000785**; axon **GO:0030424**; dendrite **GO:0030425**; synapse **GO:0045202**; postsynaptic membrane **GO:0045211**.
- **Cell Ontology suggestions:** neural progenitor cell; excitatory neuron; glutamatergic neuron; GABAergic neuron; cortical projection neuron; corticothalamic projection neuron; callosal projection neuron; astrocyte; oligodendrocyte; oligodendrocyte precursor cell; endothelial cell; pericyte. Exact CL identifiers should be validated against the release used by the knowledge base.

### Omics and advanced technologies

The principal disease-relevant profiling consists of bulk cortical RNA-seq, qPCR, public developmental and single-cell transcriptomic atlases, Ribo-seq, interaction-network analysis, and ENCODE-derived chromatin analysis. The P7 cortex data are deposited under **GEO GSE225435**. No disease-specific patient proteomic, metabolomic, lipidomic, spatial-transcriptomic, or integrated multi-omic signature has been established. Human patient-derived iPSC and organoid studies were proposed as future work rather than reported as completed disease models. (c.2024zmiz1isa pages 11-12, c.2024zmiz1isa pages 12-14)

## 7. Anatomical structures affected

The **central nervous system** is the principal functional system, especially cerebral cortex, hippocampus, cerebellum, developing cortical plate, and neuronal axon/dendrite/synapse compartments. Craniofacial structures and distal appendicular skeleton are clinically affected. Possible enteric nervous-system involvement is suggested by Hirschsprung disease in one case. (c.2024zmiz1isa pages 10-11, c.2024zmiz1isa pages 2-3)

Suggested UBERON mappings are cerebral cortex **UBERON:0000956**, hippocampus **UBERON:0002421**, cerebellum **UBERON:0002037**, brain **UBERON:0000955**, hand **UBERON:0002398**, foot **UBERON:0002387**, and enteric nervous system **UBERON:0002005**. Distal skeletal findings may be bilateral or asymmetric depending on the anomaly; no consistent lateralization is established.

## 8. Temporal development

NDDFDSA is a congenital developmental disorder, although developmental and behavioral manifestations become evident progressively during infancy and childhood as milestones are assessed. The expression peak during embryonic brain development identifies prenatal neurogenesis and circuit formation as critical vulnerability periods. (c.2024zmiz1isa pages 2-3, c.2024zmiz1isa pages 1-2)

No formal staging system exists. Structural dysmorphism and skeletal anomalies are generally stable, whereas developmental demands may make cognitive, language, and behavioral impairments more apparent with age. The condition is expected to be lifelong; episodic remission or spontaneous recovery has not been documented. Longitudinal natural-history data are insufficient to determine whether any neurologic component is degenerative.

## 9. Inheritance and population

The inheritance model is **autosomal dominant, usually de novo**. Variable expressivity is evident from the breadth of developmental, behavioral, skeletal, and occasional additional-organ findings. Penetrance has not been quantified. Parental germline mosaicism remains a theoretical recurrence mechanism for apparently de novo variants, as in other dominant developmental disorders, but a disease-specific mosaicism rate is unknown.

No prevalence, incidence, carrier frequency, founder variant, anticipation, population enrichment, geographic clustering, consanguinity effect, sex ratio, or age distribution has been established. The disorder is ultra-rare and ascertainment is likely limited by recent recognition and use of broad genomic testing. Open Targets identifies only five evidence records, all linked to the same foundational PMID, illustrating the limited independent evidence base rather than disease prevalence. (OpenTargets Search: Neurodevelopmental disorder with dysmorphic facies and distal skeletal anomalies)

## 10. Diagnostics

### Recommended molecular strategy

1. **Trio WES or WGS** is the preferred first-line approach for unexplained syndromic developmental delay/intellectual disability, especially with facial and distal skeletal findings.
2. Ensure analysis includes **ZMIZ1** coding variants, splice variants, de novo calling, and copy-number detection.
3. **WGS** has added value for regulatory variants, balanced rearrangements, and position effects.
4. Use **chromosomal microarray** for deletions/duplications, while recognizing that CMA will not detect most balanced rearrangements.
5. Consider karyotyping, genome sequencing, or targeted breakpoint analysis when a balanced translocation/inversion is suspected.
6. Confirm candidate variants and parental status by an orthogonal method; classify under current ACMG/AMP criteria.

No biochemical assay, circulating biomarker, biopsy, or pathognomonic imaging signature exists. Laboratory, EEG, MRI, ophthalmologic, gastrointestinal, and skeletal imaging should be directed by symptoms. Genetic testing, rather than facial gestalt alone, is required for confirmation. The 2024 authors explicitly proposed that **“ZMIZ1 mutation testing may aid in identifying ASD risk, enabling early diagnosis,”** but this is an expert research recommendation rather than a validated screening guideline. (c.2024zmiz1isa pages 10-11, c.2024zmiz1isa pages 11-12)

### Differential diagnosis

Important differentials include other syndromic neurodevelopmental disorders with facial and distal limb abnormalities, including chromatin/transcription-regulator disorders, TRPM3-related neurodevelopmental disorder with hypotonia and skeletal anomalies, Coffin–Siris spectrum disorders, KBG syndrome, Kabuki syndrome, Wiedemann–Steiner syndrome, Cornelia de Lange spectrum, and pathogenic CNVs. Distinguishing features require full phenotyping and molecular testing; similar disease names should not be treated as synonyms.

### Screening

NDDFDSA is not part of routine newborn screening. Cascade testing is appropriate after identifying a familial variant. Population carrier screening is not indicated for a disorder that is predominantly de novo dominant.

## 11. Outcome and prognosis

No survival curves, mortality rates, life-expectancy estimates, or validated prognostic biomarkers are available. The available literature does not indicate an intrinsically fatal or degenerative syndrome, but the evidence base is too small to establish normal life expectancy.

Long-term morbidity is likely driven by intellectual and language impairment, behavioral/psychiatric manifestations, motor limitations, seizures where present, and orthopedic or gastrointestinal complications. Prognosis should therefore be individualized according to developmental severity, communication ability, seizure control, mobility, feeding, and organ involvement. No formal quality-of-life or recovery-rate data exist.

## 12. Treatment

There is **no approved disease-modifying pharmacotherapy**, gene therapy, RNA therapy, cell therapy, or ZMIZ1-targeted treatment. No disease-specific interventional ClinicalTrials.gov study was identified.

Current management is multidisciplinary and phenotype directed:

- Early developmental intervention and individualized education.
- Speech/language therapy, including augmentative communication where needed.
- Occupational and physical therapy for adaptive and motor impairment.
- Behavioral therapy and child psychiatry for autism, ADHD, anxiety, aggression, or sleep disturbance.
- Standard antiseizure treatment if epilepsy occurs.
- Orthopedic/podiatric assessment for functionally important distal skeletal anomalies.
- Feeding, nutrition, hearing, vision, and gastrointestinal evaluation as clinically indicated.
- Surgical management for Hirschsprung disease or another congenital anomaly when present.

Suggested NCIT concepts include **Physical Therapy**, **Occupational Therapy**, **Speech Therapy**, **Behavior Therapy**, **Anticonvulsant Therapy**, **Orthopedic Surgery**, and **Genetic Counseling**; exact NCIT codes should be validated against the target terminology release.

The 2024 study does not justify direct clinical targeting of AMPA, GABA, NOTCH, p53, or chromatin pathways. Its authors conclude that further animal, iPSC, organoid, and gene-regulatory-network studies are needed before therapeutic approaches can be defined. (c.2024zmiz1isa pages 10-11, c.2024zmiz1isa pages 11-12)

## 13. Prevention

Primary prevention through lifestyle modification, vaccination, environmental remediation, or prophylactic medication is not applicable. Secondary prevention consists of early molecular diagnosis and prompt developmental intervention. Tertiary prevention involves seizure management, rehabilitation, behavioral support, orthopedic care, and surveillance for individual complications.

Genetic counseling should explain the predominantly de novo dominant mechanism, the low but nonzero recurrence possibility from parental germline mosaicism, and the 50% transmission risk for an affected individual with a heterozygous pathogenic variant, subject to penetrance and reproductive fitness. Once a familial pathogenic variant is known, prenatal diagnosis and preimplantation genetic testing are technically possible. These are reproductive options, not treatments for an affected fetus or child.

## 14. Other species and natural disease

No naturally occurring ZMIZ1-associated veterinary syndrome homologous to human NDDFDSA was identified. There is no zoonotic or cross-species transmission because this is a germline genetic disorder.

Relevant orthologs include mouse **Zmiz1** (*Mus musculus*, NCBI Taxonomy **10090**) and zebrafish **zmiz1** ortholog(s) (*Danio rerio*, Taxonomy **7955**). ZMIZ1’s developmental expression and essential vascular functions are evolutionarily conserved, but these are experimental observations rather than documented natural animal disease. Whole-body Zmiz1 loss in mice is associated with embryonic viability and vascular-development defects. (c.2024zmiz1isa pages 14-15)

## 15. Model organisms

### Cortex-specific mouse model

The strongest disease-relevant model is an **Emx1-Cre conditional Zmiz1 knockout** targeting cortical progenitors. At P3, knockout mice had significantly reduced motor-cortex thickness and significant layer-6 thinning; developing upper layers showed a nonsignificant reduction trend, while layer 5 was not significantly altered. Adult knockout mice displayed increased repetitive behavior in a marble-burying assay. P7 cortex showed 104 DEGs and altered neurodevelopmental and synaptic pathways. (c.2024zmiz1isa pages 6-8, c.2024zmiz1isa pages 3-6)

This model recapitulates selected human domains—abnormal cortical development and repetitive behavior—but does not reproduce the full facial, distal skeletal, language, or intellectual phenotype. It is therefore best suited to studying cortical neurogenesis, projection-neuron development, synaptic networks, and candidate molecular interventions, not whole-syndrome severity.

### Other models and resources

- **Conventional/vascular mouse models:** useful for embryonic viability, angiogenesis, and pleiotropic ZMIZ1 function but less specific to NDDFDSA neurobehavioral pathology.
- **Cellular systems:** public human and mouse expression datasets, K562 ChIP-derived chromatin profiles, and neuronal transcriptome/translatome datasets have been used; no validated patient-derived cellular diagnostic model exists.
- **Future systems:** patient-derived iPSCs, cortical organoids, and variant-specific knock-in models were recommended to determine allele-specific effects and therapeutic reversibility. (c.2024zmiz1isa pages 1-2, c.2024zmiz1isa pages 11-12)
- **Resources:** Jackson Laboratory Emx1-Cre stock **005628**; study transcriptome **GEO GSE225435**. (c.2024zmiz1isa pages 11-12)

## Evidence assessment and curation priorities

The strongest human causal evidence remains the 2019 case series (PMID 30639322), while the strongest current mechanistic evidence is Rajan et al., published **15 April 2024**, *Frontiers in Psychiatry* 15:1375492, DOI [10.3389/fpsyt.2024.1375492](https://doi.org/10.3389/fpsyt.2024.1375492). Its abstract states: **“Our analysis reveals that Zmiz1 regulates multiple developmental processes, including neurogenesis, neuron connectivity, and synaptic signaling.”** (c.2024zmiz1isa pages 1-2)

Priority gaps are: (1) a complete current ClinVar/HGVS variant inventory; (2) exact phenotype frequencies from the foundational and subsequent cohorts; (3) longitudinal natural history; (4) penetrance and recurrence estimates; (5) patient-derived functional studies; (6) rigorous craniofacial and skeletal mechanisms; and (7) disease-specific treatment trials. Until those gaps are filled, quantitative frequencies, genotype–phenotype correlations, and prognosis should be recorded as unknown rather than inferred from related neurodevelopmental disorders.

References

1. (OpenTargets Search: Neurodevelopmental disorder with dysmorphic facies and distal skeletal anomalies): Open Targets Query (Neurodevelopmental disorder with dysmorphic facies and distal skeletal anomalies, 4 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (c.2024zmiz1isa pages 14-15): Rajan K. C., Alina S. Tiemroth, Abbigail N. Thurmon, Stryder M. Meadows, and Maria J. Galazo. Zmiz1 is a novel regulator of brain development associated with autism and intellectual disability. Frontiers in Psychiatry, Apr 2024. URL: https://doi.org/10.3389/fpsyt.2024.1375492, doi:10.3389/fpsyt.2024.1375492. This article has 12 citations.

3. (c.2024zmiz1isa pages 6-8): Rajan K. C., Alina S. Tiemroth, Abbigail N. Thurmon, Stryder M. Meadows, and Maria J. Galazo. Zmiz1 is a novel regulator of brain development associated with autism and intellectual disability. Frontiers in Psychiatry, Apr 2024. URL: https://doi.org/10.3389/fpsyt.2024.1375492, doi:10.3389/fpsyt.2024.1375492. This article has 12 citations.

4. (c.2024zmiz1isa pages 2-3): Rajan K. C., Alina S. Tiemroth, Abbigail N. Thurmon, Stryder M. Meadows, and Maria J. Galazo. Zmiz1 is a novel regulator of brain development associated with autism and intellectual disability. Frontiers in Psychiatry, Apr 2024. URL: https://doi.org/10.3389/fpsyt.2024.1375492, doi:10.3389/fpsyt.2024.1375492. This article has 12 citations.

5. (c.2024zmiz1isa pages 1-2): Rajan K. C., Alina S. Tiemroth, Abbigail N. Thurmon, Stryder M. Meadows, and Maria J. Galazo. Zmiz1 is a novel regulator of brain development associated with autism and intellectual disability. Frontiers in Psychiatry, Apr 2024. URL: https://doi.org/10.3389/fpsyt.2024.1375492, doi:10.3389/fpsyt.2024.1375492. This article has 12 citations.

6. (c.2024zmiz1isa pages 10-11): Rajan K. C., Alina S. Tiemroth, Abbigail N. Thurmon, Stryder M. Meadows, and Maria J. Galazo. Zmiz1 is a novel regulator of brain development associated with autism and intellectual disability. Frontiers in Psychiatry, Apr 2024. URL: https://doi.org/10.3389/fpsyt.2024.1375492, doi:10.3389/fpsyt.2024.1375492. This article has 12 citations.

7. (c.2024zmiz1isa pages 15-16): Rajan K. C., Alina S. Tiemroth, Abbigail N. Thurmon, Stryder M. Meadows, and Maria J. Galazo. Zmiz1 is a novel regulator of brain development associated with autism and intellectual disability. Frontiers in Psychiatry, Apr 2024. URL: https://doi.org/10.3389/fpsyt.2024.1375492, doi:10.3389/fpsyt.2024.1375492. This article has 12 citations.

8. (c.2024zmiz1isa pages 3-6): Rajan K. C., Alina S. Tiemroth, Abbigail N. Thurmon, Stryder M. Meadows, and Maria J. Galazo. Zmiz1 is a novel regulator of brain development associated with autism and intellectual disability. Frontiers in Psychiatry, Apr 2024. URL: https://doi.org/10.3389/fpsyt.2024.1375492, doi:10.3389/fpsyt.2024.1375492. This article has 12 citations.

9. (c.2024zmiz1isa pages 8-10): Rajan K. C., Alina S. Tiemroth, Abbigail N. Thurmon, Stryder M. Meadows, and Maria J. Galazo. Zmiz1 is a novel regulator of brain development associated with autism and intellectual disability. Frontiers in Psychiatry, Apr 2024. URL: https://doi.org/10.3389/fpsyt.2024.1375492, doi:10.3389/fpsyt.2024.1375492. This article has 12 citations.

10. (c.2024zmiz1isa pages 11-12): Rajan K. C., Alina S. Tiemroth, Abbigail N. Thurmon, Stryder M. Meadows, and Maria J. Galazo. Zmiz1 is a novel regulator of brain development associated with autism and intellectual disability. Frontiers in Psychiatry, Apr 2024. URL: https://doi.org/10.3389/fpsyt.2024.1375492, doi:10.3389/fpsyt.2024.1375492. This article has 12 citations.

11. (c.2024zmiz1isa pages 12-14): Rajan K. C., Alina S. Tiemroth, Abbigail N. Thurmon, Stryder M. Meadows, and Maria J. Galazo. Zmiz1 is a novel regulator of brain development associated with autism and intellectual disability. Frontiers in Psychiatry, Apr 2024. URL: https://doi.org/10.3389/fpsyt.2024.1375492, doi:10.3389/fpsyt.2024.1375492. This article has 12 citations.

## Artifacts

- [Edison artifact artifact-00](Neurodevelopmental_Disorder_with_Dysmorphic_Facies_and_Distal_Skeletal_Anomalies-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |

All extracted references resolved successfully.