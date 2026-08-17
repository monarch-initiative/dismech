---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-15T08:35:55.301507'
end_time: '2026-08-15T08:43:05.720240'
duration_seconds: 430.42
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Neurodevelopmental Disorder with Central Hypotonia and Dysmorphic
    Facies
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 13
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
  path: Neurodevelopmental_Disorder_with_Central_Hypotonia_and_Dysmorphic_Facies-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder with Central Hypotonia and Dysmorphic Facies
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder with Central Hypotonia and Dysmorphic Facies** covering all of the
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
- **Disease Name:** Neurodevelopmental Disorder with Central Hypotonia and Dysmorphic Facies
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder with Central Hypotonia and Dysmorphic Facies** covering all of the
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


# Neurodevelopmental Disorder with Central Hypotonia and Dysmorphic Facies

## Executive summary

**Neurodevelopmental disorder with central hypotonia and dysmorphic facies (NEDCHDF)** is an exceptionally rare, monogenic developmental chromatinopathy caused by heterozygous, usually de novo missense variants in the major 14-3-3-binding motif of **HDAC4**. The defining evidence remains a 2021 series of seven unrelated individuals; consequently, prevalence, penetrance, survival, long-term natural history, and treatment-response estimates are not established. The disorder must not be conflated with **2q37 deletion/brachydactyly–mental retardation syndrome**, which usually reflects HDAC4 haploinsufficiency or a larger contiguous-gene deletion and has a different phenotype and molecular mechanism. Open Targets maps the disease to **MONDO:0859232**, **HDAC4** (ENSG00000068024), and literature including PMID **33537682**. (OpenTargets Search: Neurodevelopmental disorder with central hypotonia and dysmorphic facies, wakeling2021missensesubstitutionsat pages 1-6)

The best-supported pathogenic chain is: variant in HDAC4 residues 242–248 → impaired phosphorylation-dependent 14-3-3 binding → reduced cytoplasmic sequestration → inferred increase in nuclear HDAC4/corepressor activity → altered developmental transcription, probably including excessive repression of **MEF2C**- and **RUNX2**-dependent programs → neurodevelopmental, craniofacial, and skeletal manifestations. Only the impaired binding step has been directly demonstrated for selected variants; increased nuclear activity and downstream transcriptional effects remain compelling but incompletely tested hypotheses. (wakeling2021missensesubstitutionsat pages 12-17, wakeling2021missensesubstitutionsat pages 9-12)

The defining evidence is summarized below.

| Domain | Established findings | Quantitative evidence in defining 7-person cohort | Suggested ontology terms | Evidence limitations |
|---|---|---|---|---|
| Disease identity | Distinct Mendelian neurodevelopmental disorder caused by **HDAC4** missense variants affecting the major 14-3-3 regulatory motif; distinguished from **HDAC4 haploinsufficiency/2q37 deletion syndrome (BDMR)** by phenotype and proposed mechanism (wakeling2021missensesubstitutionsat pages 1-6, wakeling2021missensesubstitutionsat pages 9-12) | Defining cohort: **7 unrelated individuals** (wakeling2021missensesubstitutionsat pages 1-6, wakeling2021missensesubstitutionsat pages 6-9) | Suggested: **MONDO:0859232**; **OMIM:619797**; NCBI Gene/ HGNC for **HDAC4** | MONDO/OMIM identifiers are disease-resource mappings; cohort size comes from one discovery report |
| Causal gene / variant class | **Heterozygous de novo missense variants** in **HDAC4** clustering at residues **242-248** around phospho-Ser246 within the 14-3-3 binding site; variants reported to alter **Thr244, Glu247, or Pro248** (wakeling2021missensesubstitutionsat pages 1-6, wakeling2021missensesubstitutionsat pages 6-9) | **7/7 de novo**; **5/7** affect **Pro248** (wakeling2021missensesubstitutionsat pages 1-6, wakeling2021missensesubstitutionsat pages 6-9) | Suggested: Sequence Ontology **missense_variant**; HP suggested **De novo mutation** if phenotype-modeling requires; GO suggested **protein binding**, **protein localization** | Full per-patient HGVS list was not fully recoverable from the parsed table extract |
| Core neurodevelopmental phenotype | Universal developmental delay / intellectual disability with central hypotonia; all school-age individuals required special education, with one relatively milder case (wakeling2021missensesubstitutionsat pages 6-9) | **DD/ID 7/7**; **hypotonia 7/7** (wakeling2021missensesubstitutionsat pages 6-9) | Suggested HPO: **Developmental delay (HP:0001263)**, **Intellectual disability (HP:0001249)**, **Central hypotonia (HP:0011443)** | Severity stratification and milestone ages were incompletely extractable from the malformed table |
| Seizures / neurologic features | Epilepsy is common; one case had infantile spasms refractory to medication, two had generalized seizures beginning in mid-childhood; movement abnormalities included hand stereotypies or dystonic limb movements (wakeling2021missensesubstitutionsat pages 6-9) | **Seizures 3/7** (wakeling2021missensesubstitutionsat pages 6-9) | Suggested HPO: **Seizure (HP:0001250)**, **Infantile spasms (HP:0012469)**, **Stereotypy (HP:0000733)**, **Dystonia (HP:0001332)** | Frequency for movement disorder/stereotypies was described narratively, not fully tabulated in available extract |
| Sleep | Sleep disturbance reported in a subset (wakeling2021missensesubstitutionsat pages 6-9) | **3/7** (wakeling2021missensesubstitutionsat pages 6-9) | Suggested HPO: **Sleep disturbance (HP:0002360)** | Type/severity of sleep disorder not consistently specified |
| Brain imaging | Variable, nonspecific brain MRI abnormalities occurred in most imaged cases (wakeling2021missensesubstitutionsat pages 6-9, wakeling2021missensesubstitutionsat pages 12-17) | **MRI nonspecific changes 5/7** (wakeling2021missensesubstitutionsat pages 6-9) | Suggested HPO: **Abnormality of brain MRI (HP:0410263)** | Specific neuroanatomical lesions were not consistently detailed in accessible text |
| Craniofacial / oral phenotype | Recurrent facial features included hypertelorism, full lower lip, long palpebral fissures, frontal hair upsweep, widely spaced teeth, and large ears; significant drooling in early childhood was common (wakeling2021missensesubstitutionsat pages 6-9) | Multi-case recurrent features reported qualitatively; exact counts not fully recoverable except statement that **at least 6/7** had **dental anomalies, hypertelorism and/or hip defects** (wakeling2021missensesubstitutionsat pages 12-17, wakeling2021missensesubstitutionsat pages 9-12) | Suggested HPO: **Hypertelorism (HP:0000316)**, **Long palpebral fissure (HP:0000639)**, **Full lower lip (HP:0000179)**, **Widely spaced teeth (HP:0000687)**, **Large ears (HP:0000400)**, **Drooling (HP:0002307)** | Individual feature frequencies are incompletely extractable from the parsed PDF table |
| Feeding / swallowing | Swallowing difficulties and/or drooling are highlighted as distinguishing features compared with BDMR (wakeling2021missensesubstitutionsat pages 9-12) | Cohort-wide count not fully extractable; described as clinically recurrent/common (wakeling2021missensesubstitutionsat pages 6-9, wakeling2021missensesubstitutionsat pages 9-12) | Suggested HPO: **Dysphagia (HP:0002015)**, **Feeding difficulties (HP:0011968)**, **Drooling (HP:0002307)** | Exact numerator/denominator for swallowing problems unavailable in accessible text |
| Skeletal / orthopedic phenotype | Hip dislocation or subluxation, progressive scoliosis/kyphosis, and joint laxity/hypermobility were frequent; delayed anterior fontanel closure seen in two cases (wakeling2021missensesubstitutionsat pages 6-9, wakeling2021missensesubstitutionsat pages 9-12) | **Hip dislocation/subluxation 4/7**; **scoliosis/kyphosis 5/7**; **delayed fontanel closure 2/7** (wakeling2021missensesubstitutionsat pages 6-9) | Suggested HPO: **Hip dislocation (HP:0002827)**, **Hip subluxation (HP:0001388)**, **Scoliosis (HP:0002650)**, **Kyphosis (HP:0002808)**, **Joint hypermobility (HP:0001382)**, **Delayed closure of the anterior fontanelle (HP:0001476)** | Progression details were narrative; some features grouped together (e.g., scoliosis/kyphosis) |
| Growth | Growth was generally unremarkable except relatively large head size in one case (wakeling2021missensesubstitutionsat pages 6-9) | No robust abnormal-growth frequency; authors state growth parameters were “generally unremarkable” (wakeling2021missensesubstitutionsat pages 6-9) | Suggested HPO: **Relative macrocephaly (HP:0004482)** if supported case-wise | Limited anthropometric summary only |
| Negative / distinguishing features | Unlike BDMR/2q37 deletion syndrome, the cohort lacked reported autism, obesity, and brachydactyly type E; also lacked BDMR-typical broad face/brachycephaly/broad upturned nose (wakeling2021missensesubstitutionsat pages 6-9, wakeling2021missensesubstitutionsat pages 9-12) | **Autism 0/7 reported**; **obesity 0/7 reported**; **brachydactyly type E 0/7 reported** (wakeling2021missensesubstitutionsat pages 6-9, wakeling2021missensesubstitutionsat pages 9-12) | Suggested HPO negatives for curation only if allowed: absence of **Autistic behavior (HP:0000729)**, **Obesity (HP:0001513)**, **Brachydactyly type E (HP:0005863)** | These are reported absences in a small cohort, not proof of impossibility |
| Molecular mechanism | Variants impair phosphorylation-dependent **14-3-3** interaction at the key HDAC4 shuttling motif, reducing cytoplasmic sequestration and supporting a **gain-of-function via increased nuclear HDAC4 activity**; downstream effects on **RUNX2** and **MEF2C** are proposed (wakeling2021missensesubstitutionsat pages 9-12, wakeling2021missensesubstitutionsat pages 12-17, wakeling2021missensesubstitutionsat pages 6-9) | Functional assay showed **~2-fold reduced 14-3-3β binding** for **p.Thr244Lys** and **p.Glu247Gly** in HEK-293 co-immunoprecipitation assays (wakeling2021missensesubstitutionsat pages 9-12) | Suggested GO: **protein binding (GO:0005515)**, **protein localization to nucleus / nucleocytoplasmic transport** (suggested only), **negative regulation of transcription by RNA polymerase II (GO:0000122)**; suggested CL: **HEK-293 cell** not a CL term, so avoid strict CL assertion | Reduced binding is experimentally shown only for two variants; increased nuclear activity and transcriptional consequences are strongly inferred/proposed rather than directly measured in patient tissue |
| Differential diagnosis | Should be distinguished from **2q37 deletion syndrome / brachydactyly-mental retardation syndrome (BDMR)** caused by HDAC4 loss-of-function or larger deletions; defining differences include more severe DD/ID and presence of swallowing difficulties/drooling, congenital hip defects, progressive kyphoscoliosis, delayed fontanel closure, and absence of autism/obesity/brachydactyly E (wakeling2021missensesubstitutionsat pages 1-6, wakeling2021missensesubstitutionsat pages 9-12, le2019genotypeandphenotype pages 6-7) | Comparator evidence includes a **103-individual** 2q37 deletion cohort supporting HDAC4 as major contributor to BDMR but with different/overlapping features (le2019genotypeandphenotype pages 6-7, le2019genotypeandphenotype pages 2-3) | Suggested MONDO/OMIM differential: **2q37 deletion syndrome / BDMR (OMIM:600430)** | Differential interpretation depends on small n for OMIM 619797 and heterogeneous comparator deletions |
| Diagnostics / management implication | Diagnosis currently depends on sequencing-based detection of **HDAC4** missense variants in the 242-248 motif and clinical correlation; no disease-specific interventional trial or established targeted therapy identified in available evidence (wakeling2021missensesubstitutionsat pages 6-9, wakeling2021missensesubstitutionsat pages 12-17) | Cohort identified by **WES/clinical exome sequencing**, with Sanger confirmation (wakeling2021missensesubstitutionsat pages 6-9) | Suggested NCIT: **Whole Exome Sequencing**, **Sanger Sequencing** | No validated biomarker, natural-history study, or evidence-based treatment algorithm found in retrieved sources |


*Table: This table summarizes the defining clinical and mechanistic evidence for Neurodevelopmental Disorder with Central Hypotonia and Dysmorphic Facies (OMIM 619797) from the foundational 7-person cohort. It is useful for rapid knowledge-base curation because it separates established observations, explicit cohort counts, suggested ontology mappings, and evidence limitations.*

## 1. Disease information

### Definition and identifiers

NEDCHDF is a congenital/early-childhood neurodevelopmental syndrome characterized by developmental delay or intellectual disability, central hypotonia, distinctive facial appearance, and frequent neurologic and orthopedic abnormalities. The defining report called it a **“novel intellectual disability syndrome.”** Its accepted identifiers are:

- **OMIM:** 619797.
- **MONDO:** **MONDO:0859232**.
- **Causal gene:** **HDAC4**, histone deacetylase 4; OMIM gene 605314; Ensembl ENSG00000068024.
- **Common names:** neurodevelopmental disorder with central hypotonia and dysmorphic facies; HDAC4-related neurodevelopmental disorder; HDAC4 14-3-3-binding-site disorder; the discovery-paper designation “novel intellectual disability syndrome.” (OpenTargets Search: Neurodevelopmental disorder with central hypotonia and dysmorphic facies, wakeling2021missensesubstitutionsat pages 1-6)
- **Orphanet, MeSH, ICD-10/ICD-11:** no disease-specific identifier was established in the retrieved evidence. Coding will generally fall under broader intellectual-disability, developmental-disorder, hypotonia, or congenital-malformation categories.

The present description is **aggregated disease-level information derived from a very small published patient series**, not from an EHR population or registry. The foundational article was received September 18, 2020, accepted November 16, 2020, and published in January 2021: Wakeling et al., *Human Genetics and Genomics Advances* 2:100015, DOI: [10.1016/j.xhgg.2020.100015](https://doi.org/10.1016/j.xhgg.2020.100015), PMID **33537682**. (OpenTargets Search: Neurodevelopmental disorder with central hypotonia and dysmorphic facies, wakeling2021missensesubstitutionsat pages 1-6)

### Critical nosologic distinction

NEDCHDF is distinct from **2q37 deletion syndrome/brachydactyly–mental retardation syndrome** (BDMR; OMIM 600430). BDMR commonly results from HDAC4 loss of function or larger 2q37 deletions and classically includes brachydactyly type E, mild-to-moderate ID, obesity, autistic features, and broad facial morphology. The NEDCHDF cohort instead had more substantial DD/ID, dysphagia/drooling, hip defects, progressive kyphoscoliosis, and occasional delayed fontanel closure, without reported obesity, autism, or brachydactyly E. (wakeling2021missensesubstitutionsat pages 1-6, wakeling2021missensesubstitutionsat pages 9-12)

## 2. Etiology, risk, and protective factors

### Causal factor

The established cause is a **germline heterozygous de novo missense variant in HDAC4**, clustered in the invariant 14-3-3-binding motif spanning amino acids 242–248 around phospho-Ser246. Four distinct variants affecting Thr244, Glu247, or Pro248 were reported among seven unrelated individuals; five of seven variants affected Pro248. Explicitly discussed protein changes include **p.Thr244Lys, p.Glu247Gly, p.Pro248Ala, and p.Pro248Leu**. (wakeling2021missensesubstitutionsat pages 1-6, wakeling2021missensesubstitutionsat pages 6-9, wakeling2021missensesubstitutionsat pages 9-12)

### Risk and protective factors

- **Genetic risk:** presence of a pathogenic motif-disrupting HDAC4 allele. The founding variants were absent from gnomAD at the affected motif positions, and HDAC4 was highly constrained against loss-of-function variation (reported pLI=1), although that constraint metric pertains more directly to haploinsufficiency. (wakeling2021missensesubstitutionsat pages 6-9, wakeling2021missensesubstitutionsat pages 1-6)
- **Environmental, infectious, lifestyle, occupational, sex, or ancestry risk factors:** none established.
- **Protective alleles, modifier genes, diet, or lifestyle factors:** none established.
- **Gene–environment interaction:** no disease-specific evidence. HDAC4 is a signal-responsive nucleocytoplasmic shuttle, so cellular signaling can regulate its localization, but this is not evidence for a clinical environmental modifier. (wakeling2021missensesubstitutionsat pages 6-9)

Because most variants arose de novo, advanced parental age could not be evaluated in the seven-person series and should not be asserted as a risk factor.

## 3. Phenotypes

### Core and recurrent findings

The following frequencies come only from the defining seven-person cohort and therefore have wide uncertainty:

- **Developmental delay/intellectual disability: 7/7.** All school-age individuals attended special schools; severity was generally substantial, although one individual had milder cognitive, motor, and speech impairment. Suggested HPO: **HP:0001263 Developmental delay**, **HP:0001249 Intellectual disability**, **HP:0000750 Delayed speech and language development**. (wakeling2021missensesubstitutionsat pages 6-9)
- **Hypotonia: 7/7**, described as central in the disease name. Suggested HPO: **HP:0011443 Central hypotonia**. (wakeling2021missensesubstitutionsat pages 6-9)
- **Epilepsy: 3/7.** One patient had infantile spasms continuing despite medication; two developed difficult-to-control generalized seizures in mid-childhood. Suggested HPO: **HP:0001250 Seizure**, **HP:0012469 Infantile spasms**, **HP:0002197 Generalized-onset seizure**, **HP:0002345 Action tremor** only if separately documented—not a core term. (wakeling2021missensesubstitutionsat pages 6-9)
- **Nonspecific brain-MRI abnormalities: 5/7.** Suggested HPO: **HP:0410263 Abnormality of brain MRI**; the available evidence does not support one consistent structural lesion. (wakeling2021missensesubstitutionsat pages 6-9)
- **Sleep disturbance: 3/7.** Suggested HPO: **HP:0002360 Sleep disturbance**. (wakeling2021missensesubstitutionsat pages 6-9)
- **Movement/behavioral findings:** hand stereotypies in one patient and dystonic limb movements in another. No autistic features were reported. Suggested HPO: **HP:0000733 Stereotypy**, **HP:0001332 Dystonia**; record autistic behavior as an observed-negative finding, not an exclusion criterion. (wakeling2021missensesubstitutionsat pages 6-9)
- **Craniofacial/oral features:** hypertelorism, long palpebral fissures, full lower lip, frontal hair upsweep, widely spaced teeth, large ears, and dental anomalies. Suggested HPO: **HP:0000316 Hypertelorism**, **HP:0000639 Long palpebral fissure**, **HP:0000179 Full lower lip**, **HP:0000687 Widely spaced teeth**, **HP:0000400 Large ears**, and **HP:0000164 Abnormality of the dentition**. At least 6/7 had dental anomalies, hypertelorism, and/or hip-joint defects, but that composite count must not be interpreted as the frequency of each component. (wakeling2021missensesubstitutionsat pages 12-17, wakeling2021missensesubstitutionsat pages 6-9)
- **Feeding/oromotor involvement:** dysphagia and significant childhood drooling were recurrent; drooling generally persisted except in one patient. Suggested HPO: **HP:0002015 Dysphagia**, **HP:0011968 Feeding difficulties**, **HP:0002307 Drooling**. Exact individual frequencies were not recoverable from the published table extract. (wakeling2021missensesubstitutionsat pages 6-9, wakeling2021missensesubstitutionsat pages 9-12)
- **Orthopedic findings:** hip dislocation/subluxation **4/7**, scoliosis/kyphosis **5/7**, and joint hypermobility/laxity **3/7**. Suggested HPO: **HP:0002827 Hip dislocation**, **HP:0001388 Hip subluxation**, **HP:0002650 Scoliosis**, **HP:0002808 Kyphosis**, **HP:0001382 Joint hypermobility**. (wakeling2021missensesubstitutionsat pages 6-9)
- **Delayed anterior-fontanel closure: 2/7**; suggested HPO **HP:0001476**. (wakeling2021missensesubstitutionsat pages 6-9)
- **Growth:** generally unremarkable; one individual had a relatively large head. Obesity was absent in this small cohort. Suggested case-specific HPO: **HP:0004482 Relative macrocephaly**. (wakeling2021missensesubstitutionsat pages 6-9, wakeling2021missensesubstitutionsat pages 9-12)

### Severity, progression, and quality of life

Manifestations begin in infancy or early childhood through hypotonia and delayed milestones. Neurodevelopmental disability is chronic; seizure onset ranged from infancy to mid-childhood. Progressive kyphoscoliosis was explicitly noted, whereas the cognitive course was not shown to be neurodegenerative. Functional burden includes special-education needs, impaired mobility, communication limitations, feeding/swallowing problems, drooling, sleep disturbance, epilepsy, and orthopedic care. No disease-specific EQ-5D, SF-36, PROMIS, caregiver-burden, or adaptive-function study is available. (wakeling2021missensesubstitutionsat pages 6-9, wakeling2021missensesubstitutionsat pages 9-12)

## 4. Genetic and molecular information

**HDAC4** encodes a class IIa histone deacetylase/transcriptional corepressor with an N-terminal regulatory region and C-terminal deacetylase domain. The disorder-associated variants are germline missense substitutions, not somatic variants or recurrent chromosomal abnormalities. All seven founding cases were de novo. Formal ClinVar classifications and exact genomic/cDNA HGVS expressions should be verified against the current transcript **NM_006037.4** before database ingestion; the source confirms Sanger validation but the retrieved table did not permit reliable extraction of every cDNA coordinate. (wakeling2021missensesubstitutionsat pages 6-9)

The variants are best interpreted as **motif-specific gain-of-function/dysregulating alleles**, not simple HDAC4 haploinsufficiency. No affected-position missense variant was present in gnomAD in the report. No founder variant, modifier gene, protective allele, pathogenic mosaic case, epigenetic “episignature,” or recurrent large-scale rearrangement specific to NEDCHDF has been demonstrated. (wakeling2021missensesubstitutionsat pages 6-9, wakeling2021missensesubstitutionsat pages 9-12)

For contrast, HDAC4 haploinsufficiency and 2q37 deletions constitute a related but different disorder. A 103-person 2q37 analysis found incomplete penetrance and variable expressivity; reported aggregate frequencies included craniofacial dysmorphism 86%, cognitive/behavioral issues 79%, brachydactyly E 48%, and overweight/obesity 34%. HDAC4-specific loss-of-function examples included c.2399_2400insC (p.Gly801Trpfs*77) and an intragenic 65-bp deletion. (le2019genotypeandphenotype pages 6-7, le2019genotypeandphenotype pages 2-3)

## 5. Environmental information

No toxin, radiation, pollution, maternal exposure, diet, smoking, alcohol, physical-activity pattern, occupational agent, or infectious organism is known to cause or trigger NEDCHDF. It is not infectious or zoonotic. Environmental interventions cannot prevent a de novo germline variant, although standard supportive environments and early developmental services may reduce secondary disability.

## 6. Mechanism and pathophysiology

### Upstream molecular defect

HDAC4 normally shuttles between nucleus and cytoplasm. Phosphorylation of Ser246, Ser467, and Ser632 creates 14-3-3-binding sites; the residues 242–248 motif makes a major contribution to cytoplasmic sequestration. The disease variants alter residues around Ser246, potentially reducing phosphorylation and/or direct 14-3-3 affinity. (wakeling2021missensesubstitutionsat pages 6-9, wakeling2021missensesubstitutionsat pages 9-12)

In HEK-293 cells, co-immunoprecipitation showed that **p.Thr244Lys and p.Glu247Gly had approximately twofold lower affinity for 14-3-3β** than wild-type HDAC4. In-silico 14-3-3 scores were 88.6% of wild type for p.Glu247Gly, 45.9% for p.Pro248Ala, 44.5% for p.Pro248Leu, and 94.2% for p.Thr244Lys; those predictions are supportive rather than equivalent to functional validation. (wakeling2021missensesubstitutionsat pages 9-12)

### Downstream chain

Reduced 14-3-3 binding is predicted to decrease cytoplasmic retention and increase nuclear HDAC4. Nuclear HDAC4 acts predominantly as a transcriptional corepressor and interacts with **MEF2C** and **RUNX2**. Increased repression of MEF2C-related neuronal/synaptic programs plausibly contributes to DD/ID, seizures, stereotypies, and MRI abnormalities; increased RUNX2 repression plausibly contributes to hip defects, delayed fontanel closure, dental abnormalities, and scoliosis. The paper emphasized that these downstream effects **“remain to be determined”** and may involve additional unidentified pathways. (wakeling2021missensesubstitutionsat pages 12-17, wakeling2021missensesubstitutionsat pages 9-12)

Suggested ontology annotations include **GO:0005515 protein binding**, **GO:0000122 negative regulation of transcription by RNA polymerase II**, **GO:0051170 import into nucleus**, **GO:0051168 nuclear export**, **GO:0001501 skeletal system development**, **GO:0007399 nervous system development**, and **GO:0050808 synapse organization**. These are suggested mechanistic mappings, not all experimentally enriched terms from patient tissue.

### Cells, compartments, and profiling

The implicated compartments are **nucleus** (GO:0005634) and **cytoplasm** (GO:0005737). Likely disease-relevant cells include neurons (**CL:0000540**), neural progenitor cells (**CL:0011020**), chondrocytes (**CL:0000138**), and osteoblast-lineage cells (**CL:0000062**), but direct patient-cell evidence is limited to a heterologous HEK-293 binding assay. No NEDCHDF-specific single-cell, spatial-transcriptomic, patient-brain transcriptomic, proteomic, metabolomic, lipidomic, CRISPR-screen, or multi-omics dataset was identified. (wakeling2021missensesubstitutionsat pages 6-9, wakeling2021missensesubstitutionsat pages 9-12)

There is no demonstrated disease-specific metabolic, immune, inflammatory, oxidative-stress, ischemic, fibrotic, or tissue-necrosis mechanism.

## 7. Anatomical structures affected

- **Primary system:** central nervous system and developing brain—suggested UBERON **UBERON:0000955 brain**, **UBERON:0001017 central nervous system**.
- **Musculoskeletal:** vertebral column (**UBERON:0001130**), hip joint (**UBERON:0001464**), craniofacial skeleton, teeth, and anterior fontanel.
- **Oromotor/feeding structures:** oral cavity and swallowing apparatus; involvement is functional rather than a consistent structural lesion.
- **Secondary/variable systems:** ocular, cardiac, renal, and genital findings occurred in isolated cases in the source table, but the evidence does not establish them as core disease features. (wakeling2021missensesubstitutionsat pages 24-29)
- **Lateralization:** no consistent unilateral, bilateral, or asymmetric pattern.

## 8. Temporal development

Onset is congenital or in infancy, with hypotonia and delayed milestones. The disease is chronic and lifelong. Epilepsy may begin with infantile spasms or emerge in mid-childhood. Kyphosis/scoliosis can progress. Drooling may persist beyond early childhood. No formal stages, remission pattern, median progression rate, or longitudinal natural-history trajectory has been defined. Early childhood is the most plausible intervention window for developmental, communication, feeding, and orthopedic support, but this is clinical reasoning rather than trial-proven disease-specific evidence. (wakeling2021missensesubstitutionsat pages 6-9, wakeling2021missensesubstitutionsat pages 9-12)

## 9. Inheritance and population

The molecular inheritance pattern is **autosomal dominant**, with all seven defining cases caused by de novo variants. Penetrance of these specific motif variants appears high in the ascertained cases but cannot be quantified because unaffected carriers and population-based ascertainment are lacking. Expressivity is variable, including variation in cognitive severity, epilepsy, movement disorder, MRI findings, and orthopedic complications. (wakeling2021missensesubstitutionsat pages 6-9, wakeling2021missensesubstitutionsat pages 1-6)

No prevalence or incidence per 100,000, carrier frequency, sex ratio, ancestry enrichment, geographic clustering, founder effect, anticipation, or role for consanguinity is known. Only seven unrelated individuals defined the disorder, so any numerical epidemiologic estimate would be unreliable. Parental blood-negative de novo status leaves a small residual recurrence risk from parental germline mosaicism; no disease-specific mosaic recurrence series is available.

## 10. Diagnostics

### Recommended approach

1. Recognize syndromic DD/ID with central hypotonia, characteristic facial/dental findings, dysphagia or drooling, epilepsy, hip instability, and scoliosis/kyphosis.
2. Use trio **whole-exome sequencing or genome sequencing**, or a comprehensive neurodevelopmental-disorder panel that includes **HDAC4**. The discovery cohort used WES/clinical exome sequencing and Sanger confirmation. (wakeling2021missensesubstitutionsat pages 6-9)
3. Prioritize de novo missense variants in HDAC4 residues 242–248 and apply ACMG/AMP evidence including de novo occurrence, population absence, motif/domain location, computational evidence, and variant-specific functional data.
4. Confirm by Sanger sequencing and test both parents. If phenotype instead suggests BDMR—especially brachydactyly E, obesity, autism, or a broad/upturned nose—perform chromosomal microarray to detect a 2q37 deletion. (le2019genotypeandphenotype pages 2-3, wakeling2021missensesubstitutionsat pages 9-12)

**WGS** can identify coding SNVs, indels, CNVs, and structural/noncoding variants in one assay, but no NEDCHDF-specific incremental-yield study exists. **CMA** is valuable for the 2q37 deletion differential but will usually miss the defining single-nucleotide missense alleles. Karyotyping and FISH are appropriate only when a large rearrangement is suspected. Mitochondrial DNA and repeat-expansion tests are not specifically indicated unless another phenotype suggests them.

### Clinical evaluation

Baseline evaluation should include developmental and neurologic assessment; EEG if seizures or suspicious events occur; brain MRI when clinically indicated; feeding/swallowing assessment; growth and head circumference; audiology/ophthalmology; hip and spine examination with imaging as indicated; dental review; and targeted cardiac or renal assessment based on examination. No enzyme assay, blood metabolite, validated circulating biomarker, biopsy, or disease-specific electrophysiologic signature exists.

### Differential diagnosis

Major differentials include 2q37 deletion/BDMR, MEF2C haploinsufficiency syndrome, RUNX2-related cleidocranial dysplasia, other chromatinopathies, cerebral palsy/central hypotonia syndromes, congenital muscular or neuromuscular disorders, and other monogenic developmental epileptic encephalopathies. The combination of a de novo HDAC4 14-3-3-motif variant and absence of brachydactyly E strongly supports NEDCHDF. (wakeling2021missensesubstitutionsat pages 12-17, wakeling2021missensesubstitutionsat pages 9-12)

There are no standardized clinical criteria, newborn-screening assay, or population-screening program.

## 11. Outcome and prognosis

No survival curve, mortality rate, life-expectancy estimate, or prognostic biomarker is available. The published individuals included children and older patients, but the cohort is too small and follow-up too limited to infer normal or shortened lifespan. Morbidity is driven by intellectual/developmental disability, speech impairment, mobility limitations, epilepsy—sometimes medication resistant—dysphagia, drooling, sleep problems, and progressive orthopedic disease. (wakeling2021missensesubstitutionsat pages 6-9)

Recovery to typical development has not been documented. Functional gains can reasonably be expected from rehabilitation and seizure/feeding/orthopedic management, but no response rate has been measured. Potential adverse prognostic features are severe early developmental impairment, refractory infantile spasms/generalized epilepsy, clinically important dysphagia, and progressive kyphoscoliosis; these remain expert extrapolations rather than validated predictors.

## 12. Treatment and current applications

There is **no approved disease-modifying or genotype-specific therapy**, no NEDCHDF treatment guideline, and no relevant interventional trial identified in the ClinicalTrials.gov search.

Current real-world management is multidisciplinary and phenotype directed:

- early physical, occupational, speech-language, and augmentative-communication therapy;
- feeding therapy, swallow-safety assessment, texture modification, nutrition support, and gastrostomy when required;
- standard antiseizure medication selected by seizure type, with escalation through epilepsy specialists for drug-resistant epilepsy;
- orthopedic surveillance and management of hip instability, scoliosis/kyphosis, joint laxity, and mobility needs;
- sleep, dental, vision, and hearing management;
- educational accommodations and family/social support.

Suggested NCIt intervention concepts include **Physical Therapy**, **Occupational Therapy**, **Speech Therapy**, **Anticonvulsant Therapy**, **Nutritional Support**, **Gastrostomy**, **Orthopedic Surgery**, **Genetic Counseling**, **Whole Exome Sequencing**, and **Whole Genome Sequencing**. Exact NCIt codes should be validated against the release used by the knowledge base.

The discovery authors raised HDAC inhibition as a theoretical strategy but cautioned that whether treatment could halt or reverse developmental problems is unknown. Class IIa HDACs respond poorly to many conventional inhibitors, so an effective intervention might require HDAC4-selective inhibition or disruption of the HDAC4–MEF2 interaction. This is preclinical rationale, not a treatment recommendation. (wakeling2021missensesubstitutionsat pages 12-17)

## 13. Prevention

Primary prevention by lifestyle modification, vaccination, environmental control, or prophylactic medication is not applicable to a typically de novo Mendelian disorder. Secondary prevention consists of early molecular diagnosis, developmental intervention, seizure recognition, swallow-safety assessment, and orthopedic surveillance. Tertiary prevention aims to reduce aspiration, malnutrition, seizure injury, contractures, hip damage, and spinal deformity.

Genetic counseling should explain autosomal-dominant causation, the usually de novo origin, low but nonzero sibling recurrence risk due to possible germline mosaicism, and a 50% transmission risk for an affected individual if reproductive fitness permits. Once a familial pathogenic variant is known, prenatal diagnosis and preimplantation genetic testing are technically possible. Population carrier or newborn screening is not currently justified.

## 14. Other species and natural disease

No naturally occurring veterinary counterpart attributable to orthologous HDAC4 14-3-3-motif variants was identified. Relevant comparative species include **Homo sapiens** (NCBI Taxon 9606), **Mus musculus** (10090), and **Drosophila melanogaster** (7227); the motif is reported as evolutionarily invariant from humans to fruit flies. There is no zoonotic transmission. (wakeling2021missensesubstitutionsat pages 6-9)

## 15. Models and experimental systems

The direct disease-model evidence is limited:

- **HEK-293 cellular model:** transient expression of wild-type or variant HDAC4 plus 14-3-3β, followed by co-immunoprecipitation, demonstrated approximately twofold reduced binding for p.Thr244Lys and p.Glu247Gly. Strength: direct test of the initiating molecular defect. Limitation: transformed kidney-derived cells do not model developing neurons, chondrocytes, or whole-organism phenotypes. (wakeling2021missensesubstitutionsat pages 6-9, wakeling2021missensesubstitutionsat pages 9-12)
- **Mouse/chondrocyte evidence:** HDAC4 overexpression in proliferating mouse chondrocytes inhibited differentiation, phenocopying aspects of Runx2 loss of function and supporting the proposed skeletal pathway. This is mechanistic support rather than a knock-in model of NEDCHDF. (wakeling2021missensesubstitutionsat pages 9-12)
- **Constitutive-nuclear HDAC4 model:** attempts to generate mice with the three principal 14-3-3-site serines changed to alanine were reportedly unsuccessful, suggesting that large increases in nuclear HDAC4 activity may be developmentally intolerable. It does not reproduce the milder patient alleles. (wakeling2021missensesubstitutionsat pages 9-12)

No patient-derived iPSC neuron, cerebral organoid, zebrafish knock-in, Drosophila disease allele, CRISPR-engineered human neural progenitor, or faithful mouse knock-in model of p.Thr244Lys/p.Glu247Gly/p.Pro248 substitutions was identified. Such models are priorities for testing nuclear localization, cell-type-specific transcription, developmental timing, reversibility, and selective HDAC4/MEF2-targeted therapies.

## Evidence appraisal and recent research status

The principal limitation is that essentially all disease-specific clinical statistics derive from **seven patients in one 2021 report**. Recent 2023–2024 chromatinopathy research has reinforced the importance of HDAC-family dysfunction and sequencing-based diagnosis, but it has not yet supplied a larger NEDCHDF natural-history cohort, validated episignature, patient-derived multi-omics dataset, or clinical trial. Accordingly, the most authoritative interpretation remains that the syndrome is a motif-specific HDAC4 regulatory disorder with experimentally established impaired 14-3-3 binding and a strongly supported—but not fully demonstrated—nuclear gain-of-function mechanism. (OpenTargets Search: Neurodevelopmental disorder with central hypotonia and dysmorphic facies, wakeling2021missensesubstitutionsat pages 12-17, wakeling2021missensesubstitutionsat pages 9-12)

### Exact source quotations supporting central claims

- Discovery abstract: **“Here, we report seven unrelated individuals with a phenotype distinct from that of BDMR, all of whom have heterozygous de novo missense variants that affect a major regulatory site of HDAC4.”** (wakeling2021missensesubstitutionsat pages 1-6)
- Mechanism: **“both the p.Glu247Gly and p.Thr244Lys variants bound 14-3-3β with approximately two-fold reduced affinity compared to native HDAC4.”** (wakeling2021missensesubstitutionsat pages 9-12)
- Phenotype summary: **“This phenotype includes significant DD/ID, seizures, distinctive facial features, scoliosis, delayed closure of the anterior fontanelle and non-specific brain MRI anomalies.”** (wakeling2021missensesubstitutionsat pages 12-17)
- Mechanistic caution: whether reduced 14-3-3 interaction causes decreased RUNX2 and MEF2C signaling **“remains to be determined.”** (wakeling2021missensesubstitutionsat pages 12-17)

## Key references

1. Wakeling E, et al. *Missense substitutions at a conserved 14-3-3 binding site in HDAC4 cause a novel intellectual disability syndrome.* **Human Genetics and Genomics Advances. January 2021;2:100015.** PMID: **33537682**. DOI/URL: [10.1016/j.xhgg.2020.100015](https://doi.org/10.1016/j.xhgg.2020.100015). (OpenTargets Search: Neurodevelopmental disorder with central hypotonia and dysmorphic facies, wakeling2021missensesubstitutionsat pages 1-6)
2. Le TN, Williams SR, Alaimo JT, Elsea SH. *Genotype and phenotype correlation in 103 individuals with 2q37 deletion syndrome reveals incomplete penetrance and supports HDAC4 as the primary genetic contributor.* **American Journal of Medical Genetics Part A. March 2019;179:782–791.** DOI/URL: [10.1002/ajmg.a.61089](https://doi.org/10.1002/ajmg.a.61089). This is comparator evidence for HDAC4 haploinsufficiency/2q37 deletion syndrome, not the defining NEDCHDF cohort. (le2019genotypeandphenotype pages 6-7, le2019genotypeandphenotype pages 2-3)

References

1. (OpenTargets Search: Neurodevelopmental disorder with central hypotonia and dysmorphic facies): Open Targets Query (Neurodevelopmental disorder with central hypotonia and dysmorphic facies, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (wakeling2021missensesubstitutionsat pages 1-6): Emma Wakeling, Meriel McEntagart, Michael Bruccoleri, Charles Shaw-Smith, Karen L. Stals, Matthew Wakeling, Angela Barnicoat, Clare Beesley, Andrea K. Hanson-Kahn, Mary Kukolich, David A. Stevenson, Philippe M. Campeau, Sian Ellard, Sarah H. Elsea, Xiang-Jiao Yang, and Richard C. Caswell. Missense substitutions at a conserved 14-3-3 binding site in hdac4 cause a novel intellectual disability syndrome. Human Genetics and Genomics Advances, 2:100015, Jan 2021. URL: https://doi.org/10.1016/j.xhgg.2020.100015, doi:10.1016/j.xhgg.2020.100015. This article has 25 citations and is from a peer-reviewed journal.

3. (wakeling2021missensesubstitutionsat pages 12-17): Emma Wakeling, Meriel McEntagart, Michael Bruccoleri, Charles Shaw-Smith, Karen L. Stals, Matthew Wakeling, Angela Barnicoat, Clare Beesley, Andrea K. Hanson-Kahn, Mary Kukolich, David A. Stevenson, Philippe M. Campeau, Sian Ellard, Sarah H. Elsea, Xiang-Jiao Yang, and Richard C. Caswell. Missense substitutions at a conserved 14-3-3 binding site in hdac4 cause a novel intellectual disability syndrome. Human Genetics and Genomics Advances, 2:100015, Jan 2021. URL: https://doi.org/10.1016/j.xhgg.2020.100015, doi:10.1016/j.xhgg.2020.100015. This article has 25 citations and is from a peer-reviewed journal.

4. (wakeling2021missensesubstitutionsat pages 9-12): Emma Wakeling, Meriel McEntagart, Michael Bruccoleri, Charles Shaw-Smith, Karen L. Stals, Matthew Wakeling, Angela Barnicoat, Clare Beesley, Andrea K. Hanson-Kahn, Mary Kukolich, David A. Stevenson, Philippe M. Campeau, Sian Ellard, Sarah H. Elsea, Xiang-Jiao Yang, and Richard C. Caswell. Missense substitutions at a conserved 14-3-3 binding site in hdac4 cause a novel intellectual disability syndrome. Human Genetics and Genomics Advances, 2:100015, Jan 2021. URL: https://doi.org/10.1016/j.xhgg.2020.100015, doi:10.1016/j.xhgg.2020.100015. This article has 25 citations and is from a peer-reviewed journal.

5. (wakeling2021missensesubstitutionsat pages 6-9): Emma Wakeling, Meriel McEntagart, Michael Bruccoleri, Charles Shaw-Smith, Karen L. Stals, Matthew Wakeling, Angela Barnicoat, Clare Beesley, Andrea K. Hanson-Kahn, Mary Kukolich, David A. Stevenson, Philippe M. Campeau, Sian Ellard, Sarah H. Elsea, Xiang-Jiao Yang, and Richard C. Caswell. Missense substitutions at a conserved 14-3-3 binding site in hdac4 cause a novel intellectual disability syndrome. Human Genetics and Genomics Advances, 2:100015, Jan 2021. URL: https://doi.org/10.1016/j.xhgg.2020.100015, doi:10.1016/j.xhgg.2020.100015. This article has 25 citations and is from a peer-reviewed journal.

6. (le2019genotypeandphenotype pages 6-7): Trang N. Le, Stephen R. Williams, Joseph T. Alaimo, and Sarah H. Elsea. Genotype and phenotype correlation in 103 individuals with 2q37 deletion syndrome reveals incomplete penetrance and supports hdac4 as the primary genetic contributor. American Journal of Medical Genetics Part A, 179:782-791, Mar 2019. URL: https://doi.org/10.1002/ajmg.a.61089, doi:10.1002/ajmg.a.61089. This article has 42 citations.

7. (le2019genotypeandphenotype pages 2-3): Trang N. Le, Stephen R. Williams, Joseph T. Alaimo, and Sarah H. Elsea. Genotype and phenotype correlation in 103 individuals with 2q37 deletion syndrome reveals incomplete penetrance and supports hdac4 as the primary genetic contributor. American Journal of Medical Genetics Part A, 179:782-791, Mar 2019. URL: https://doi.org/10.1002/ajmg.a.61089, doi:10.1002/ajmg.a.61089. This article has 42 citations.

8. (wakeling2021missensesubstitutionsat pages 24-29): Emma Wakeling, Meriel McEntagart, Michael Bruccoleri, Charles Shaw-Smith, Karen L. Stals, Matthew Wakeling, Angela Barnicoat, Clare Beesley, Andrea K. Hanson-Kahn, Mary Kukolich, David A. Stevenson, Philippe M. Campeau, Sian Ellard, Sarah H. Elsea, Xiang-Jiao Yang, and Richard C. Caswell. Missense substitutions at a conserved 14-3-3 binding site in hdac4 cause a novel intellectual disability syndrome. Human Genetics and Genomics Advances, 2:100015, Jan 2021. URL: https://doi.org/10.1016/j.xhgg.2020.100015, doi:10.1016/j.xhgg.2020.100015. This article has 25 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Neurodevelopmental_Disorder_with_Central_Hypotonia_and_Dysmorphic_Facies-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 2 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |

All extracted references resolved successfully.