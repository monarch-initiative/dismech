---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-15T08:31:46.064486'
end_time: '2026-08-15T08:40:21.881974'
duration_seconds: 515.82
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Neurodevelopmental Disorder with Early-Onset Parkinsonism and Behavioral
    Abnormalities
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
  path: Neurodevelopmental_Disorder_with_Early-Onset_Parkinsonism_and_Behavioral_Abnormalities-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder with Early-Onset Parkinsonism and Behavioral Abnormalities
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder with Early-Onset Parkinsonism and Behavioral Abnormalities** covering all of the
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
- **Disease Name:** Neurodevelopmental Disorder with Early-Onset Parkinsonism and Behavioral Abnormalities
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder with Early-Onset Parkinsonism and Behavioral Abnormalities** covering all of the
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


# Neurodevelopmental Disorder with Early-Onset Parkinsonism and Behavioral Abnormalities

## Executive summary and evidence limitations

This is an **ultra-rare autosomal-recessive neurodevelopmental–neurodegenerative disorder caused by biallelic PTRHD1 variants**. The characteristic sequence is childhood developmental/cognitive impairment, often with behavioral abnormalities, followed in adolescence or early adulthood by progressive parkinsonism. The evidence base remains exceptionally small: the principal reviews describe two consanguineous Iranian families and one sub-Saharan African kindred, with motor onset generally between 20 and 30 years. Accordingly, frequencies below are qualitative rather than population estimates. (guadagnolo2021genotypephenotypecorrelationsin pages 7-8)

Open Targets maps the entity to **MONDO:0958323** and identifies PTRHD1 as the principal target. It also returns CENPO with weaker evidence, apparently reflecting overlapping locus/variant records rather than an independently established second cause; CENPO should therefore not currently be curated as a definitive causal gene for this syndrome. (OpenTargets Search: Neurodevelopmental disorder with early-onset parkinsonism and behavioral abnormalities)

| Domain | Summary |
|---|---|
| Disease name | Neurodevelopmental disorder with early-onset parkinsonism and behavioral abnormalities; a rare Mendelian syndrome linked primarily to biallelic **PTRHD1** variation (established) (OpenTargets Search: Neurodevelopmental disorder with early-onset parkinsonism and behavioral abnormalities, guadagnolo2021genotypephenotypecorrelationsin pages 7-8) |
| MONDO ID | **MONDO:0958323** (established disease identifier from Open Targets disease mapping) (OpenTargets Search: Neurodevelopmental disorder with early-onset parkinsonism and behavioral abnormalities) |
| Causal gene | **PTRHD1** (*peptidyl-tRNA hydrolase domain containing 1*; OMIM gene noted in review as MIM *617342*) is the principal associated gene; **CENPO** also appears in disease-target association resources but with weaker/overlapping evidence and should be treated cautiously for disease causality here (OpenTargets Search: Neurodevelopmental disorder with early-onset parkinsonism and behavioral abnormalities, guadagnolo2021genotypephenotypecorrelationsin pages 7-8) |
| Inheritance | **Autosomal recessive / biallelic** inheritance; reported affected individuals were from consanguineous or likely recessive families (established) (guadagnolo2021genotypephenotypecorrelationsin pages 7-8) |
| Known human evidence / families | Very limited human evidence: initially **3 families** reported in the literature — **2 unrelated consanguineous Iranian families** and **1 sub-Saharan African kindred** — with a later **2024 single case** carrying homozygous **p.Arg122Gln** and juvenile parkinsonism with ID/epilepsy (established for scarcity; exact total case count remains small) (OpenTargets Search: Neurodevelopmental disorder with early-onset parkinsonism and behavioral abnormalities, guadagnolo2021genotypephenotypecorrelationsin pages 7-8) |
| Typical temporal course | **Childhood neurodevelopmental impairment** (global developmental delay/intellectual disability ± behavioral abnormalities) followed by **juvenile/early-adult parkinsonism**, usually in the **20–30 year** range in the earlier reports; progression appears chronic/progressive but detailed natural-history staging is not available (partly established, partly inferred) (guadagnolo2021genotypephenotypecorrelationsin pages 7-8) |
| Core phenotypes with suggested HPO terms | Intellectual disability **HP:0001249**; global developmental delay **HP:0001263**; behavioral abnormality **HP:0000708**; parkinsonism **HP:0001300**; bradykinesia **HP:0002067**; rigidity **HP:0002063**; tremor/postural tremor **HP:0001337**; pyramidal signs/spasticity **HP:0002493 / HP:0001257**; peripheral neuropathy **HP:0009830**; hypersomnia **HP:0001262**; generalized seizures/epilepsy reported in at least one later case **HP:0002197 / HP:0001250** (phenotype set combines established reported findings with ontology suggestions) (guadagnolo2021genotypephenotypecorrelationsin pages 7-8) |
| Variant classes | Reported disease-associated variants include **homozygous missense** variants and a **28-nt frameshift deletion**; later literature adds **homozygous p.Arg122Gln** in an individual with ID, generalized epilepsy, and juvenile parkinsonism (established at class level; exhaustive variant list not recoverable from currently available context) (OpenTargets Search: Neurodevelopmental disorder with early-onset parkinsonism and behavioral abnormalities, guadagnolo2021genotypephenotypecorrelationsin pages 7-8) |
| Mechanism confidence | **Low-to-moderate confidence mechanism.** Reviews propose **loss of function** of PTRHD1 and possible involvement in **ubiquitin-proteasome / protein quality control** biology, but direct disease-specific mechanistic validation remains sparse; no robust pathway model is established (conservative interpretation) (guadagnolo2021genotypephenotypecorrelationsin pages 7-8) |
| Diagnosis | Diagnosis is currently **genomic**: suspected from the syndromic combination of developmental disorder/behavioral abnormalities plus juvenile or early-onset parkinsonism, then confirmed by **WES/WGS or targeted gene panel** showing biallelic PTRHD1 variants. No disease-specific biomarker, clinical criteria, or pathognomonic laboratory test was identified (established scarcity; testing approach partly inferred from rare-disease practice) (guadagnolo2021genotypephenotypecorrelationsin pages 7-8) |
| Treatment | **No disease-specific therapy established.** Management is **supportive/symptomatic**, extrapolated from juvenile parkinsonism and neurodevelopmental care. Published disease-specific quantitative data on levodopa response, DBS, rehabilitation outcomes, or genotype-guided treatment were not identified in the available evidence base (guadagnolo2021genotypephenotypecorrelationsin pages 7-8) |
| Epidemiology | **Ultra-rare**; only a handful of families/cases reported. No reliable prevalence, incidence, carrier frequency, penetrance, sex ratio, or population-based estimates are available (established evidence gap) (guadagnolo2021genotypephenotypecorrelationsin pages 7-8) |
| Trials | **No relevant disease-specific interventional clinical trials identified** for PTRHD1-related disease; no gene therapy, RNA therapy, or targeted experimental program was found in the searched trial resources (guadagnolo2021genotypephenotypecorrelationsin pages 7-8) |
| Major evidence gaps | Missing or very limited data on: full variant spectrum; allele frequencies; penetrance/expressivity; MRI/DAT-SPECT patterns; longitudinal prognosis/survival; treatment response rates; QoL; environmental modifiers; protective factors; epigenetics; transcriptomics/proteomics/metabolomics; and validated animal/cellular disease models (guadagnolo2021genotypephenotypecorrelationsin pages 7-8) |


*Table: This table provides a compact knowledge-base summary of PTRHD1-related neurodevelopmental disorder with early-onset parkinsonism and behavioral abnormalities. It emphasizes established facts, flags inferred points conservatively, and highlights major evidence gaps for curation and future research.*

## 1. Disease information

**Definition.** PTRHD1-related neurodevelopmental disorder is a Mendelian condition combining developmental delay or intellectual disability and behavioral disturbance with juvenile/early-onset parkinsonism. Reported associated findings include pyramidal signs, postural tremor, sensorimotor polyneuropathy, hypersomnia, and, in a later case, generalized epilepsy. (guadagnolo2021genotypephenotypecorrelationsin pages 7-8)

**Identifiers and nomenclature**

- **MONDO:** MONDO:0958323.
- **Gene:** PTRHD1, peptidyl-tRNA hydrolase domain containing 1; gene MIM ***617342** is reported in the reviewed literature.
- **Common names:** “PTRHD1-related neurodevelopmental disorder,” “PTRHD1-related intellectual disability and parkinsonism,” “autosomal-recessive intellectual disability and parkinsonism,” and “PTRHD1-related juvenile-onset parkinsonism.”
- **OMIM disease number, Orphanet number:** not established from the retrieved evidence and should be verified directly before database import.
- **ICD-10/ICD-11 and MeSH:** no disease-specific code or heading was identified. General coding would necessarily use intellectual-disability/developmental-disorder and parkinsonism codes and would lose etiologic specificity.

The source evidence is principally **individual patients and pedigrees reported in primary publications**, subsequently aggregated by reviews and disease databases. It is not based on EHR-scale cohorts or population registries. Open Targets links the disease association to PMIDs **27134041, 27753167, 29143421, 30398675, 34765690, and 34816696**. (OpenTargets Search: Neurodevelopmental disorder with early-onset parkinsonism and behavioral abnormalities)

## 2. Etiology, risk, and protective factors

The primary cause is **germline biallelic PTRHD1 variation**, consistent with autosomal-recessive inheritance. Reported classes include homozygous missense substitutions and a homozygous 28-nucleotide frameshift deletion; loss of function is the leading disease model. (guadagnolo2021genotypephenotypecorrelationsin pages 7-8)

**Risk factors:**

- Carrying two pathogenic/likely pathogenic PTRHD1 alleles is the only established causal risk factor.
- Parental consanguinity increases the probability that both parents carry the same rare allele; two foundational Iranian families were consanguineous. (guadagnolo2021genotypephenotypecorrelationsin pages 7-8)
- No validated susceptibility loci, modifier genes, sex effect, environmental toxin, infectious trigger, lifestyle factor, or occupational exposure has been demonstrated specifically for this disorder.

**Protective factors and gene–environment interactions:** none are known. Protective associations described for idiopathic Parkinson disease must not be transferred to this monogenic childhood-onset syndrome without evidence. No PTRHD1-specific G×E study was found.

## 3. Phenotypes

The phenotype is heterogeneous, and denominators are too small for reliable percentages. Suggested ontology annotations are:

- **Global developmental delay** — HP:0001263; childhood onset; probably common in the neurodevelopmental presentation.
- **Intellectual disability** — HP:0001249; childhood onset, variable severity; a defining recurrent feature.
- **Behavioral abnormality** — HP:0000708; type and severity incompletely standardized.
- **Parkinsonism** — HP:0001300; usually begins around 20–30 years in the initial families and appears progressive. Core components may be annotated as bradykinesia HP:0002067, rigidity HP:0002063, and tremor HP:0001337. (guadagnolo2021genotypephenotypecorrelationsin pages 7-8)
- **Muscle stiffness/rigidity** — HP:0002063.
- **Postural tremor** — HP:0002174 is a more specific candidate if confirmed from the source record; otherwise use HP:0001337.
- **Pyramidal signs/spasticity** — HP:0007256 or HP:0001257, depending on the documented examination.
- **Sensorimotor polyneuropathy** — HP:0007141 or broader peripheral neuropathy HP:0009830.
- **Hypersomnia** — HP:0001262.
- **Generalized epilepsy/seizures** — HP:0002197/HP:0001250; reported in a 2024 individual and not yet established as universal.

Effects on quality of life have not been quantified with EQ-5D, SF-36, PROMIS, or a disease-specific instrument. Nevertheless, the combination of cognitive impairment, behavioral disturbance, parkinsonism, and neuropathy plausibly impairs education, independent living, mobility, communication, employment, and caregiver burden. That functional interpretation is clinically reasonable but has not been measured in a PTRHD1 cohort.

## 4. Genetic and molecular information

**Causal gene:** PTRHD1 is the supported causal gene. Open Targets lists ENSG00000184924 and five supporting evidence records. CENPO is listed at lower association strength, but current evidence does not establish it as a second monogenic cause. (OpenTargets Search: Neurodevelopmental disorder with early-onset parkinsonism and behavioral abnormalities)

**Variants:** published disease alleles include homozygous missense variants and a 28-nt frameshift deletion. A 2024 report described homozygous **p.Arg122Gln** in an individual with intellectual disability, generalized epilepsy, and juvenile parkinsonism. Exact transcript-dependent HGVS expressions, genomic coordinates, ClinVar accessions, ACMG classifications, and gnomAD frequencies should be retrieved directly from ClinVar/gnomAD before variant-level import; they were not recoverable with sufficient certainty from the available full text. (guadagnolo2021genotypephenotypecorrelationsin pages 7-8)

The variants are presumed **constitutional germline**, not somatic. The frameshift supports loss of function; the functional effect of individual missense alleles requires variant-specific evidence. No dominant-negative or gain-of-function mechanism has been demonstrated. No validated modifier gene, disease-specific methylation signature, histone alteration, recurrent translocation, inversion, aneuploidy, or pathogenic large copy-number change was established in the retrieved evidence.

## 5. Environmental information

No toxin, radiation exposure, pollution source, diet, smoking, alcohol use, exercise pattern, occupational exposure, or infectious agent has been causally connected to PTRHD1 disease. The disorder is not infectious, contagious, or zoonotic. Environmental Parkinson-disease associations should be treated only as differential-context information, not as evidence for this syndrome.

## 6. Mechanism and pathophysiology

PTRHD1 encodes a small protein containing a putative peptidyl-tRNA-hydrolase domain. Reviews propose that pathogenic variants impair PTRHD1 function and may disturb the **ubiquitin–proteasome/protein-quality-control system**. Direct biochemical confirmation in disease-relevant human neurons remains limited. (guadagnolo2021genotypephenotypecorrelationsin pages 7-8)

A cautious causal model is:

1. **Upstream:** biallelic pathogenic PTRHD1 variants reduce or alter PTRHD1 protein function.
2. **Intermediate, provisional:** defective protein-quality control and/or peptidyl-tRNA-related processing leads to cellular proteostasis stress.
3. **Cellular vulnerability:** developing neural circuits produce intellectual and behavioral manifestations; later dysfunction or loss in motor circuits produces parkinsonism.
4. **Downstream:** basal-ganglia motor-network dysfunction manifests as bradykinesia, rigidity, and tremor, with possible corticospinal and peripheral-nerve involvement.

Only step 1 and the genotype–phenotype relationship are firmly supported; the intervening molecular chain remains hypothetical. Suggested terms include **GO:0006511 ubiquitin-dependent protein catabolic process**, **GO:0051603 proteolysis involved in cellular protein catabolic process**, **GO:0006457 protein folding**, and **GO:0000502 proteasome complex**. These are mechanism-oriented suggestions, not experimentally validated PTRHD1 disease annotations.

Candidate cell types are **midbrain dopaminergic neuron** (CL:0000700), cortical neuron (CL:0000540), and peripheral neuron (CL:0000533). Relevant subcellular candidates include cytosol (GO:0005829) and proteasome complex (GO:0000502). No disease-specific single-cell, spatial-transcriptomic, transcriptomic, proteomic, metabolomic, lipidomic, CRISPR-screen, or integrated multi-omic dataset was identified.

## 7. Anatomical structures affected

The primary system is the **nervous system**. Clinical parkinsonism implicates bilateral basal-ganglia and nigrostriatal circuitry, while developmental/cognitive features implicate cerebral networks. Pyramidal signs suggest corticospinal-system involvement, and sensorimotor polyneuropathy indicates peripheral nervous-system involvement. These are cliniconeuroanatomical inferences; disease-specific neuropathology is unavailable.

Suggested anatomical terms include brain UBERON:0000955, cerebral cortex UBERON:0000956, basal ganglion UBERON:0002420, substantia nigra UBERON:0002038, striatum UBERON:0002435, spinal cord UBERON:0002240, and peripheral nerve UBERON:0001021. Parkinsonism normally reflects bilateral network dysfunction, but systematic lateralization data are absent.

## 8. Temporal development

The recognizable pattern is **childhood neurodevelopmental impairment followed by juvenile or early-adult parkinsonism**. Initial family reports place motor onset broadly at **20–30 years**. (guadagnolo2021genotypephenotypecorrelationsin pages 7-8)

The condition appears chronic and progressive rather than episodic or relapsing-remitting, but no validated stages, progression rate, median duration, remission rate, or critical therapeutic window has been defined. Developmental surveillance should continue into adulthood because parkinsonism may emerge well after the initial neurodevelopmental diagnosis.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. Foundational evidence came from two unrelated consanguineous Iranian families and one sub-Saharan African kindred. The ascertainment pattern supports homozygosity-by-descent in some families but does not establish an ethnic restriction. (guadagnolo2021genotypephenotypecorrelationsin pages 7-8)

Prevalence, incidence, carrier frequency, sex ratio, penetrance, age-dependent penetrance, founder effects, and geographic variant frequencies are unknown. Expressivity is evidently variable because neurological accompaniments differ among reports. Genetic anticipation is not expected for the known sequence-variant mechanism and has not been reported. Germline mosaicism has not been documented but cannot be excluded in recurrence counseling.

For two confirmed carrier parents, the standard autosomal-recessive risk per pregnancy is 25% affected, 50% carrier, and 25% unaffected/non-carrier, assuming parentage and variant interpretation are secure.

## 10. Diagnostics

There are no standardized disease-specific clinical criteria. Suspicion should be raised by developmental delay/intellectual disability with behavioral abnormalities followed by juvenile parkinsonism, particularly in a consanguineous family or among affected siblings.

**Recommended testing strategy:**

1. Neurologic, developmental, psychiatric/behavioral, sleep, and peripheral-nerve assessment.
2. Brain MRI to exclude structural, metabolic, and neurodegenerative mimics; no pathognomonic PTRHD1 MRI pattern is established.
3. EEG if seizures or regression occur; EMG/nerve-conduction studies if neuropathy is suspected.
4. First-line genomic testing with a neurodevelopmental/movement-disorder panel or trio/family **whole-exome sequencing** that includes PTRHD1 and copy-number analysis.
5. **Whole-genome sequencing** when exome/panel testing is negative, particularly to detect noncoding or structural variants.
6. Confirm candidate variants by an orthogonal method and perform segregation testing. RNA studies may help evaluate splice variants but are not validated clinical biomarkers.

CMA is useful when a broader developmental phenotype suggests a copy-number disorder, but karyotyping and FISH are low-yield unless cytogenetic abnormalities are suspected. Mitochondrial DNA and repeat-expansion testing are differential-driven rather than PTRHD1-specific.

Important differentials include PRKN-, PINK1-, PARK7-, ATP13A2-, FBXO7-, DNAJC6-, SYNJ1-, PLA2G6-, RAB39B-, and WARS2-related disease; Wilson disease; dopa-responsive dystonia; mitochondrial and lysosomal disorders; neurodegeneration with brain iron accumulation; and medication-induced parkinsonism. The 2023 systematic review emphasizes that parkinsonism is increasingly recognized across genetic neurodevelopmental disorders, supporting broad genomic rather than narrowly phenotypic evaluation. No validated blood, CSF, imaging, proteomic, or metabolomic biomarker exists for PTRHD1 disease.

## 11. Outcome and prognosis

No 5- or 10-year survival estimates, mortality rates, or life-expectancy data exist. The principal morbidity is lifelong cognitive/developmental disability compounded by progressive motor impairment, behavioral symptoms, sleep disturbance, and occasionally neuropathy or epilepsy. Recovery of the underlying genetic disorder is not documented. Prognostic biomarkers and validated predictors of progression are absent.

## 12. Treatment and current implementation

No disease-modifying or regulatory-approved PTRHD1-specific therapy exists. No relevant PTRHD1-specific interventional trial was identified in the trial search.

Care is therefore multidisciplinary and symptom-directed:

- A monitored **levodopa/carbidopa trial** is reasonable for function-limiting parkinsonism, but PTRHD1-specific response rates, durability, and dyskinesia risks are not quantified.
- Physical therapy, gait/balance training, occupational therapy, speech-language therapy, assistive communication, and mobility devices should be individualized.
- Educational and behavioral supports are required for developmental and psychiatric manifestations.
- Treat epilepsy, neuropathic symptoms, sleep disturbance, constipation, dysphagia, and nutrition problems according to standard practice.
- Deep-brain stimulation has no established PTRHD1-specific evidence and should not be assumed effective merely from experience in other genetic parkinsonisms.

Suggested NCIt concepts include Levodopa (NCIt drug concept), Carbidopa, Physical Therapy, Occupational Therapy, Speech Therapy, Genetic Counseling, and Deep Brain Stimulation; exact NCIt identifiers should be resolved through the current NCIt release before ingestion.

There is no established gene replacement, CRISPR, ASO, siRNA, mRNA, cell therapy, or pharmacogenomic algorithm. Open Targets supports PTRHD1 as the biological target but does not identify a validated therapeutic program. (OpenTargets Search: Neurodevelopmental disorder with early-onset parkinsonism and behavioral abnormalities)

## 13. Prevention

There is no lifestyle, vaccine, environmental, or drug-based primary prevention for an individual who has inherited two pathogenic alleles. Relevant prevention is reproductive and complication-focused:

- Genetic counseling and cascade testing of at-risk relatives.
- Carrier testing after familial variants are established.
- Prenatal diagnosis or preimplantation genetic testing where legally and ethically acceptable.
- Early developmental intervention and longitudinal movement-disorder surveillance.
- Tertiary prevention through fall reduction, aspiration surveillance, nutrition support, seizure control, and maintenance of mobility.

Population or newborn screening is not justified because prevalence, test performance, natural history, and benefits of presymptomatic treatment are unknown.

## 14. Other species and natural disease

No naturally occurring veterinary analogue attributable to an orthologous PTRHD1 defect was identified. Therefore, no affected breed, OMIA syndrome, zoonotic potential, or cross-species transmission applies. Orthologues likely occur broadly across vertebrates, but NCBI Gene and Taxon identifiers should be verified directly for each species before curation.

## 15. Model organisms and research priorities

No validated PTRHD1 knockout/knock-in mouse, rat, zebrafish, Drosophila, C. elegans, organoid, or patient-iPSC model that robustly reproduces both neurodevelopmental impairment and juvenile parkinsonism was identified. This is a major translational gap.

Priority models would include:

- Isogenic human iPSC-derived cortical and midbrain dopaminergic neurons carrying patient alleles.
- PTRHD1-null and missense knock-in vertebrate models with longitudinal motor, cognitive, sleep, and peripheral-nerve phenotyping.
- Rescue experiments comparing wild-type PTRHD1 with patient variants.
- Quantitative assays of proteasome activity, ubiquitinated proteins, stalled-translation products, cellular stress, neurite development, dopamine handling, and neuronal survival.

These studies are needed before the proposed proteostasis mechanism can be considered established or therapeutically actionable.

## Recent developments and authoritative interpretation

The most relevant recent synthesis is the **2023 systematic review of parkinsonism in genetic neurodevelopmental disorders**, which places PTRHD1 among a growing group in which parkinsonism emerges after an earlier developmental phenotype. The expert implication is practical: patients with genetically unexplained intellectual disability should receive long-term movement surveillance, while juvenile parkinsonism accompanied by developmental or behavioral abnormalities should prompt broad genomic testing.

A 2024 publication reported homozygous **PTRHD1 p.Arg122Gln** in an individual with intellectual disability, generalized epilepsy, and juvenile parkinsonism, extending the possible phenotype but remaining a single-patient observation. No 2023–2024 clinical trial, natural-history cohort, or disease-specific multi-omics study was found.

## Key primary and review literature

- Khodadadi H, et al. **“PTRHD1 (C2orf79) mutations lead to autosomal-recessive intellectual disability and parkinsonism.”** *Movement Disorders*. Published 2017. PMID: **27753167**. DOI: https://doi.org/10.1002/mds.26824.
- Kuipers DJS, et al. **“PTRHD1 loss-of-function mutation in an African family with juvenile-onset parkinsonism and intellectual disability.”** *Movement Disorders*. Published November 2018. PMID: **30398675**. DOI: https://doi.org/10.1002/mds.27501.
- Guadagnolo D, et al. **Genotype-Phenotype Correlations in Monogenic Parkinson Disease.** *Frontiers in Neurology*. Published September 2021. DOI: https://doi.org/10.3389/fneur.2021.648588. This review states that only three families were then documented and summarizes onset at 20–30 years with stiffness, postural tremor, pyramidal signs, sensorimotor polyneuropathy, behavioral disorders, and hypersomnia. (guadagnolo2021genotypephenotypecorrelationsin pages 7-8)
- von Scheibler ENMM, et al. **Parkinsonism in Genetic Neurodevelopmental Disorders: A Systematic Review.** *Movement Disorders Clinical Practice*. Online publication October 2022; 2023 issue. DOI: https://doi.org/10.1002/mdc3.13577.
- Gebert J, et al. **A homozygous PTRHD1 missense variant (p.Arg122Gln) in an individual with intellectual disability, generalized epilepsy, and juvenile parkinsonism.** Published 2024. DOI: https://doi.org/10.1055/a-2256-0722.

The retrievable abstract-level material did not contain exact sentences for most patient-level clinical claims; consequently, fabricated quotations have not been supplied. The PMID-linked primary-paper set and disease-target mapping are independently reflected in Open Targets. (OpenTargets Search: Neurodevelopmental disorder with early-onset parkinsonism and behavioral abnormalities)

References

1. (guadagnolo2021genotypephenotypecorrelationsin pages 7-8): Daniele Guadagnolo, Maria Piane, Maria Rosaria Torrisi, Antonio Pizzuti, and Simona Petrucci. Genotype-phenotype correlations in monogenic parkinson disease: a review on clinical and molecular findings. Frontiers in Neurology, Sep 2021. URL: https://doi.org/10.3389/fneur.2021.648588, doi:10.3389/fneur.2021.648588. This article has 92 citations and is from a peer-reviewed journal.

2. (OpenTargets Search: Neurodevelopmental disorder with early-onset parkinsonism and behavioral abnormalities): Open Targets Query (Neurodevelopmental disorder with early-onset parkinsonism and behavioral abnormalities, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

## Artifacts

- [Edison artifact artifact-00](Neurodevelopmental_Disorder_with_Early-Onset_Parkinsonism_and_Behavioral_Abnormalities-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |

All extracted references resolved successfully.