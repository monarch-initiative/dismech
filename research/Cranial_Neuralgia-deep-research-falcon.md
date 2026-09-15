---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-28T22:48:11.723610'
end_time: '2026-08-28T22:55:39.217955'
duration_seconds: 447.49
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cranial Neuralgia
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 36
reference_validation:
  total_references: 14
  verified: 14
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 14
  on_topic: 6
  validator_version: 0.2.1
term_validation:
  total_terms: 1
  verified: 1
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 1
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Cranial_Neuralgia-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cranial Neuralgia
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Cranial Neuralgia** covering all of the
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
- **Disease Name:** Cranial Neuralgia
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Cranial Neuralgia** covering all of the
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


# Cranial Neuralgia: Disease-Characteristics Research Report

## Executive summary and scope

**Cranial neuralgia is an umbrella clinical category, not one etiologically uniform disease.** It denotes pain localized to the distribution of a cranial or cranio-cervical sensory nerve and includes, most importantly, trigeminal neuralgia (TN), glossopharyngeal neuralgia (GPN), occipital neuralgia (ON), and the very rare nervus intermedius neuralgia. These entities should be represented separately in a knowledge base because their nerves, triggers, secondary causes, epidemiology, and procedures differ. The strongest evidence concerns TN; evidence for ON and especially nervus intermedius neuralgia is much thinner. As Tepper’s authoritative review states, “The most frequently encountered primary neuralgias are trigeminal neuralgia, occipital neuralgia, and, rarely, glossopharyngeal neuralgia. Nervus intermedius neuralgia is even more rare.” (tepper2018cranialneuralgias pages 1-2)

The shared clinical pattern is usually severe, unilateral, brief, recurrent, shock-like pain, often provoked by innocuous stimulation. The best-supported upstream mechanism in classical TN and GPN is focal neurovascular compression near the brainstem root-entry zone, followed by myelin injury, abnormal excitability, ectopic firing/ephaptic transmission, and paroxysmal pain. Nevertheless, vascular contact is neither necessary nor sufficient in every patient, and secondary lesions must be actively excluded. Approximately 15% of TN cases in one review were associated with cerebellopontine-angle lesions, including neoplasms and demyelination. (tepper2018cranialneuralgias pages 1-2, stefano2019trigeminalneuralgiafrom pages 14-23, lafta2024genomicvalidationin pages 1-2)

| Entity | Nerve / anatomic distribution | Hallmark phenotype / triggers | Typical etiology | Epidemiology | Diagnostic emphasis | First-line treatment | Procedural options | Key recent evidence / statistics |
|---|---|---|---|---|---|---|---|---|
| **Cranial neuralgia (umbrella category)** | Pain in distributions of cranial nerves; major entities include trigeminal, occipital, glossopharyngeal, and nervus intermedius neuralgias (tepper2018cranialneuralgias pages 1-2, thomas2024autonomicfeaturesof pages 1-2) | Classically unilateral, paroxysmal, shock-like pain; some patients have continuous background pain; autonomic features may occur in a substantial minority (tepper2018cranialneuralgias pages 1-2, thomas2024autonomicfeaturesof pages 1-2) | Often neurovascular compression in primary/classical forms; secondary causes must be excluded (tumor, demyelination, vascular malformation, trauma, infection depending on subtype) (tepper2018cranialneuralgias pages 1-2, wu2023percutaneousradiofrequencythermocoagulation pages 1-2, peng2023fullyendoscopicmicrovascular pages 1-2) | **Umbrella-level gap:** no single robust prevalence/incidence estimate for all cranial neuralgias combined. In a 2024 meta-analysis, **40%** of patients with craniofacial neuralgias had ≥1 autonomic feature; excluding TN, autonomic features were reported in **28%** of pain events (95% CI **2–90%**) (thomas2024autonomicfeaturesof pages 1-2) | Clinical classification plus targeted exclusion of secondary causes; MRI/MRA emphasized for primary neuralgias, especially when neurovascular compression is suspected (tepper2018cranialneuralgias pages 1-2) | Drug therapy generally relies on antiepileptics, antidepressants, and baclofen; subtype-specific first-line choice varies (tepper2018cranialneuralgias pages 1-2) | Ablation, radiofrequency procedures, gamma knife/radiosurgery, neuromodulation, and microvascular decompression in selected refractory/compressive cases (tepper2018cranialneuralgias pages 1-2, NCT05491915 chunk 1) | 2024 systematic review quantified autonomic features hierarchy: lacrimation most common overall; ptosis and sweating least common (thomas2024autonomicfeaturesof pages 1-2) |
| **Trigeminal neuralgia (TN)** | CN V; one or more trigeminal divisions (V1/V2/V3), often unilateral facial distribution; right side may be more common in some series (stefano2019trigeminalneuralgiafrom pages 14-23, peng2023fullyendoscopicmicrovascular pages 1-2) | Brief recurrent electric shock-like or stabbing facial pain triggered by innocuous stimuli such as chewing, speaking, tooth-brushing, touch; some patients develop continuous pain superimposed on paroxysms (stefano2019trigeminalneuralgiafrom pages 14-23, kolakowski2024interdisciplinarystrategiesfor pages 9-9, wu2019botulinumtoxintype pages 1-2) | Classical TN: neurovascular compression with demyelination; secondary TN: multiple sclerosis, tumors, vascular malformations, ischemic/space-occupying lesions; idiopathic TN has no identified cause (stefano2019trigeminalneuralgiafrom pages 14-23, kolakowski2024interdisciplinarystrategiesfor pages 9-9, lafta2024genomicvalidationin pages 1-2, peng2023fullyendoscopicmicrovascular pages 1-2) | Annual incidence reported as **4.5–28.9/100,000**; lifetime prevalence about **0.3%** in one review; more common in middle-aged/older women; MS patients have markedly increased risk, with TN prevalence **1.9–4.9%** in MS and ~15–20-fold excess risk in reviews (gerwin2020chronicfacialpain pages 1-3, stefano2019trigeminalneuralgiafrom pages 14-23, peng2023fullyendoscopicmicrovascular pages 1-2) | Diagnosis is primarily clinical using ICHD-3 features; MRI/MRA used to detect neurovascular compression and rule out secondary causes; diagnostic confusion with dental/TMJ disorders and headache syndromes is common (tepper2018cranialneuralgias pages 1-2, kolakowski2024interdisciplinarystrategiesfor pages 9-9) | **Carbamazepine or oxcarbazepine** (voltage-gated sodium-channel blockers) are standard first-line therapy (stefano2019trigeminalneuralgiafrom pages 14-23, kolakowski2024interdisciplinarystrategiesfor pages 9-9, wu2019botulinumtoxintype pages 1-2) | Microvascular decompression (MVD); radiofrequency thermocoagulation/ablation; balloon compression; glycerol procedures; gamma knife; botulinum toxin in refractory disease; investigational peripheral nerve stimulation and imaging-guided RFT strategies (tepper2018cranialneuralgias pages 1-2, wu2019botulinumtoxintype pages 1-2, NCT06620172 chunk 1) | 2024 UK Biobank genetic study: **555** TN cases vs **6,245** controls; **C8B rs706484 OR 1.357 (1.158–1.590), p=0.00016** and **MFG-E8 rs2015495 OR 1.313 (1.134–1.521), p=0.00028**; both eQTLs (lafta2024genomicvalidationin pages 1-2). 2023 fully endoscopic MVD series: TN effective rate **98.9%** (105 complete, 5 significant, 4 partial relief) with **11 recurrences** over mean **18.6 ± 3.3 months** (peng2023fullyendoscopicmicrovascular pages 1-2). 2019 BTX-A cohort: **83.7%** success, **16.3%** mild side effects; age ≥50 predicted better response (wu2019botulinumtoxintype pages 1-2). 2024 review cites MVD meta-analytic pain-free rate **92.9% [89.1–96.8]** after 5 months to 5 years (han2022glossopharyngealneuralgiaepidemiology pages 11-12) |
| **Glossopharyngeal neuralgia (GPN)** | CN IX distribution: mandibular angle, ear, tonsillar fossa, posterior pharynx, base of tongue; may associate with vagal/cardiovascular symptoms in severe cases (wu2023percutaneousradiofrequencythermocoagulation pages 1-2, peng2023fullyendoscopicmicrovascular pages 1-2) | Transient stabbing pain triggered by **coughing, talking, swallowing, yawning** (wu2023percutaneousradiofrequencythermocoagulation pages 1-2) | Commonly neurovascular compression near brainstem root entry zone; also trauma, skull-base or posterior fossa tumors, infections, surgery (wu2023percutaneousradiofrequencythermocoagulation pages 1-2) | Annual incidence estimated **0.2–0.7/100,000** in one surgical review and **0.8/100,000/year** in another; tends to increase with age and most often occurs in adults **>50 years** (peng2023fullyendoscopicmicrovascular pages 1-2, wu2023percutaneousradiofrequencythermocoagulation pages 1-2) | Clinical diagnosis supported by anatomic pain distribution and trigger history; MRI evidence of compressing vessel may guide selection for MVD; secondary causes require exclusion (wu2023percutaneousradiofrequencythermocoagulation pages 1-2, peng2023fullyendoscopicmicrovascular pages 1-2) | **Carbamazepine**; alternatives include gabapentin and eslicarbazepine acetate per review literature (wu2023percutaneousradiofrequencythermocoagulation pages 1-2, han2022glossopharyngealneuralgiaepidemiology pages 11-12) | MVD, percutaneous radiofrequency thermocoagulation (PRT), pulsed radiofrequency, nerve blocks, rhizotomy, stereotactic radiation in selected reports (wu2023percutaneousradiofrequencythermocoagulation pages 1-2, han2022glossopharyngealneuralgiaepidemiology pages 11-12, peng2023fullyendoscopicmicrovascular pages 1-2) | 2023 comparative study found both PRT and MVD significantly reduced VAS and PSQI; at **48 weeks**, complete remission was significantly higher with **MVD** than PRT, while hospital stay, operative time, and cost were also higher with MVD; no significant adverse-event difference (wu2023percutaneousradiofrequencythermocoagulation pages 1-2). 2023 endoscopic MVD series reported GPN effective rate **100%** (**10/10** complete relief) (peng2023fullyendoscopicmicrovascular pages 1-2) |
| **Occipital neuralgia (ON)** | Typically greater/lesser/third occipital nerve distribution in posterior scalp/upper neck; often considered among common cranial/cervico-cranial neuralgias in practice (tepper2018cranialneuralgias pages 1-2, NCT05491915 chunk 1) | Paroxysmal occipital or upper-neck pain, often with tenderness over occipital nerves; may overlap with cervicogenic headache syndromes (**detailed phenotype data limited in gathered set**) (tepper2018cranialneuralgias pages 1-2, NCT05491915 chunk 1) | Heterogeneous; may involve nerve irritation/entrapment, trauma, or cervical pathology, but **umbrella-level gathered evidence here is limited** (tepper2018cranialneuralgias pages 1-2) | **Data gap in gathered evidence:** no robust contemporary incidence/prevalence figure retrieved in current evidence set | Primarily clinical; distinction from cervicogenic headache and other posterior head pain syndromes is important; interventional studies frequently use occipital nerve-targeted approaches (NCT05491915 chunk 1) | **Evidence gap in gathered set:** no single universally cited first-line drug regimen retrieved here | Occipital nerve block, pulsed radiofrequency/radiofrequency ablation, platelet-rich plasma, and peripheral nerve stimulation under study (clinical trials) (NCT05491915 chunk 1) | Current implementations/trials include SPRINT® occipital **peripheral nerve stimulation** case-series study, **NCT05491915**, active-not-recruiting, estimated **n=50**; primary outcomes include reduction in average pain/pain interference and adverse events through follow-up to 24 months (NCT05491915 chunk 1) |
| **Nervus intermedius neuralgia** | CN VII nervus intermedius / deep ear canal region (**specific detailed anatomic evidence limited in gathered set**) (tepper2018cranialneuralgias pages 1-2) | Very rare neuralgia; typically severe paroxysmal neuralgic pain in its sensory territory, but **detailed contemporary phenotype evidence not retrieved in current set** (tepper2018cranialneuralgias pages 1-2) | Often presumed compressive or secondary causes should be excluded, but **subtype-specific evidence sparse** in gathered sources (tepper2018cranialneuralgias pages 1-2) | **Major data gap:** no reliable incidence/prevalence estimate retrieved in current evidence set | Careful workup for secondary causes; diagnosis remains uncommon and literature sparse (tepper2018cranialneuralgias pages 1-2) | **No subtype-specific first-line evidence retrieved in current set**; management often extrapolated from other cranial neuralgias (tepper2018cranialneuralgias pages 1-2) | Case-based invasive strategies may be used, but **no robust contemporary procedural dataset retrieved here** | Key message is rarity and evidence scarcity rather than quantified outcomes in current gathered literature (tepper2018cranialneuralgias pages 1-2) |


*Table: This table summarizes the main cranial neuralgia subtypes using only already-gathered evidence, separating umbrella-level conclusions from subtype-specific findings. It highlights where evidence is strong for trigeminal and glossopharyngeal neuralgia and where important gaps remain for occipital and nervus intermedius neuralgia.*

## 1. Disease information

### Definition and classification

ICHD-3 places these disorders under **painful lesions of the cranial nerves and other facial pain**. ICD-11/IASP places trigeminal and other cranial/regional neuralgias and neuropathies under **chronic neuropathic orofacial pain**; ICOP largely follows ICHD-3. “Neuralgia” should not be conflated with all cranial neuropathic pain: classical neuralgias are predominantly paroxysmal, whereas painful post-traumatic neuropathy commonly includes sensory loss, dysesthesia, allodynia, or continuous pain. (fried2020animalmodelsof pages 1-2, thomas2024autonomicfeaturesof pages 1-2)

**Recommended knowledge-base strategy:** use subtype-specific MONDO/MeSH/ICD identifiers rather than assigning an uncertain umbrella MONDO ID. No single validated OMIM or Orphanet entry represents all cranial neuralgias, and most cases are sporadic/acquired rather than Mendelian. Relevant clinical labels and synonyms include **cranial nerve neuralgia**, **craniofacial neuralgia**, **facial neuralgia**, **trigeminal neuralgia/tic douloureux**, **glossopharyngeal neuralgia**, **occipital neuralgia**, and **nervus intermedius/geniculate neuralgia**. Exact ontology accessions should be resolved against the current release during ingestion because classification versions change.

**Data provenance:** this report summarizes aggregated disease-level resources, cohorts, reviews, trials, and experimental studies. It is not derived from a single patient’s EHR. UK Biobank associations used coded diagnoses and population genotypes; surgical reports used institutional clinical records. (lafta2024genomicvalidationin pages 1-2, wu2023percutaneousradiofrequencythermocoagulation pages 1-2, peng2023fullyendoscopicmicrovascular pages 1-2)

## 2. Etiology, risk, and protective factors

### Causal factors

1. **Neurovascular compression:** the principal recognized cause of classical TN and an important cause of GPN. In TN, the superior cerebellar artery is commonly implicated. Clinically meaningful “classical TN” requires compression with morphological nerve-root change, not incidental contact alone. (stefano2019trigeminalneuralgiafrom pages 14-23, lafta2024genomicvalidationin pages 1-2)
2. **Demyelinating disease:** multiple sclerosis markedly increases TN risk; prevalence in MS is reported as 1.9–4.9%, approximately 15–20-fold above the general population. Pontine plaques can combine central demyelination with peripheral neurovascular contact. (stefano2019trigeminalneuralgiafrom pages 14-23, gerwin2020chronicfacialpain pages 1-3)
3. **Structural/vascular disease:** cerebellopontine-angle or skull-base tumors, aneurysm or vascular malformation, brainstem ischemia, and other space-occupying lesions may produce secondary neuralgia. (tepper2018cranialneuralgias pages 1-2, kolakowski2024interdisciplinarystrategiesfor pages 9-9, wu2023percutaneousradiofrequencythermocoagulation pages 1-2)
4. **Trauma and iatrogenic injury:** facial trauma and dental, surgical, or anesthetic procedures can cause painful trigeminal neuropathy. This is clinically adjacent to, but mechanistically and diagnostically distinct from, classical TN.
5. **Infection/inflammation:** GPN may follow tonsillitis, pharyngitis, arachnoiditis, parapharyngeal abscess, or tuberculosis; inflammatory disease is also a recognized secondary TN category. (gerwin2020chronicfacialpain pages 1-3, wu2023percutaneousradiofrequencythermocoagulation pages 1-2)
6. **Idiopathic disease:** no cause is demonstrated despite appropriate imaging and clinical work-up.

### Demographic and genetic risk

TN and GPN incidence rises with age; TN is more frequent in women and generally begins after age 50. GPN is also most common after 50. Family history may matter, but familial TN constitutes only an estimated 2–11% of cases, and reported pedigrees are compatible with either dominant or recessive transmission. Familial cases may begin earlier. These observations do **not** establish one inheritance pattern. (gerwin2020chronicfacialpain pages 1-3, lafta2024genomicvalidationin pages 1-2, wu2023percutaneousradiofrequencythermocoagulation pages 1-2)

A 2024 UK Biobank candidate-gene analysis included 555 TN cases and 6,245 matched controls. Among 175 SNPs in 17 protein-linked genes, **C8B rs706484** was associated with TN at OR 1.357 (95% CI 1.158–1.590; p=0.00016), and **MFGE8 rs2015495** at OR 1.313 (1.134–1.521; p=0.00028). Both are eQTLs. C8B links to complement biology and MFGE8 to regulation of neuroinflammation. These are modest susceptibility associations from a candidate-gene study—not pathogenic variants, not diagnostic biomarkers, and not proof of causation. The paper was received July 12, accepted August 30, and published in 2024; DOI: https://doi.org/10.1007/s12031-024-02263-x. Its abstract states: “few candidate genes have been proposed to date.” (lafta2024genomicvalidationin pages 1-2)

### Environmental, lifestyle, and protective factors

No reproducible toxin, pollution, diet, smoking, alcohol, exercise, or occupational exposure has been established as a primary risk factor for classical cranial neuralgia. Mechanical triggers such as touching the face, chewing, speaking, swallowing, coughing, yawning, or brushing teeth **precipitate attacks but do not cause the disease**. No validated genetic protective allele, dietary factor, or prophylactic lifestyle intervention prevents primary TN/GPN/ON. Avoidance of unnecessary dental/craniofacial nerve injury is relevant to post-traumatic neuropathy, but not proven primary prevention for classical neuralgia.

**Gene–environment interaction:** evidence is preliminary. A plausible model is inherited excitability/inflammatory susceptibility plus acquired compression, demyelination, trauma, or infection. No replicated quantitative G×E model is currently suitable for clinical use.

## 3. Phenotypes

### Core phenotype

For TN, ICHD-3 defines recurrent unilateral pain in one or more trigeminal divisions, lasting from a fraction of a second to two minutes, severe, electric-shock/shooting/stabbing or sharp, and precipitated by innocuous stimuli. Trigger zones may be intraoral or facial; a brief refractory period can follow an attack. Some patients later develop continuous or near-continuous pain beneath the paroxysms. (stefano2019trigeminalneuralgiafrom pages 14-23, fried2020animalmodelsof pages 1-2)

GPN produces transient severe stabbing pain at the base of tongue, tonsillar fossa, posterior pharynx, ear, and mandibular angle, commonly triggered by swallowing, speaking, coughing, or yawning. Vagal activation may produce bradycardia or syncope and can make GPN medically dangerous despite its rarity. (wu2023percutaneousradiofrequencythermocoagulation pages 1-2, peng2023fullyendoscopicmicrovascular pages 1-2)

ON usually causes unilateral or bilateral stabbing/shooting posterior-scalp pain in greater, lesser, or third occipital nerve territories, with nerve tenderness and sometimes dysesthesia/allodynia. Nervus intermedius neuralgia causes very brief deep-ear pain, often with a trigger zone in the posterior auditory canal/periauricular region; robust frequency estimates are unavailable.

### Autonomic and functional manifestations

A 2024 PRISMA systematic review/meta-analysis found at least one autonomic feature in **40%** of craniofacial-neuralgia patients. Excluding TN, autonomic features occurred in 28% of pain events, but uncertainty was extreme (95% CI 2–90%). Lacrimation was most frequent, followed by conjunctival injection, nasal congestion, rhinorrhea, flushing, edema/swelling, salivation, ptosis, and sweating. The authors caution that much non-TN evidence consists of case reports and small cohorts. Published September 12, 2024; DOI: https://doi.org/10.22514/jofph.2024.023. (thomas2024autonomicfeaturesof pages 1-2)

Pain can impair eating, oral hygiene, speaking, sleep, work, exercise, and social participation and can cause anticipatory anxiety, depression, weight loss, and disability. GPN surgical studies show improvement in both pain and Pittsburgh Sleep Quality Index after intervention. TN is not usually life-shortening, but its recurrent severity markedly reduces quality of life. (kisielcybula2024trigeminalneuralgia pages 15-18, wu2023percutaneousradiofrequencythermocoagulation pages 1-2)

### Suggested HPO annotations

Use phenotype annotations rather than representing the umbrella as one phenotype:

- Neuralgic facial pain / facial pain: **HP:0012531 (Pain)** plus anatomy-specific qualifier.
- Paroxysmal pain; severe pain; electric-shock-like pain; allodynia; hyperalgesia; hypoesthesia; paresthesia/dysesthesia.
- Unilateral facial pain; occipital pain/headache; ear pain; throat pain; tongue-base pain.
- Triggered pain with mastication, tactile stimulation, speech, swallowing, coughing, or yawning.
- Lacrimation, conjunctival injection, rhinorrhea, nasal congestion, ptosis, flushing.
- Syncope and bradycardia for GPN when present.
- Anxiety, depressed mood, sleep disturbance, feeding difficulty, and weight loss as secondary impacts.

Where an exact HPO term does not exist, compose **Pain + UBERON anatomical site + episodic/severity/laterality qualifiers** rather than creating an unsupported disease-specific term.

## 4. Genetic and molecular information

No gene is established as a necessary and sufficient cause of ordinary cranial neuralgia; consequently, there is no standard OMIM causal-gene list, no validated diagnostic variant panel, and no established penetrance, carrier frequency, founder mutation, anticipation, or germline-mosaicism framework.

Candidate biology includes voltage-gated sodium and calcium channels, serotonin transport, purinergic signaling, complement, and inflammatory regulation. The best recent human evidence is the **C8B/MFGE8** association above. Variants rs706484 and rs2015495 are common regulatory susceptibility markers/eQTLs and should be annotated as **association evidence**, not ACMG pathogenic/likely pathogenic variants. Population allele frequencies, HGNC identifiers, and tissue-specific eQTL direction should be imported directly from current gnomAD/HGNC/GTEx releases before variant-level deployment. (lafta2024genomicvalidationin pages 1-2)

A 2024 study proposed **STIM1–ORAI1 store-operated Ca²⁺ entry (SOCE)** as an inflammatory mechanism. It integrated mouse GEO dataset GSE162284 (4 healthy and 8 injury-model samples), GeneCards and STRING analyses, then used rat injury models, trigeminal-ganglion assays, patch clamp, STIM1–ORAI1 colocalization, T-cell Western blot/ELISA, immunohistochemistry, and flow cytometry. STIM1 activity was linked to TNF-α, IL-1β, and IL-6 release. However, this is predominantly computational, in-vitro, and rodent evidence; the source dataset is mouse—not a human TN transcriptome—and the infraorbital-injury model may represent traumatic trigeminal neuropathy more closely than classical TN. Published June 19, 2024; DOI: https://doi.org/10.3389/fnmol.2024.1391189. (cheng2024novelinsightsinto pages 1-2)

No reproducible disease-defining methylation signature, chromosomal abnormality, somatic mutation, proteomic panel, metabolomic/lipidomic signature, single-cell atlas, spatial-transcriptomic signature, or clinical multi-omic classifier is established. Such fields should be marked **investigational/not available**, not negative.

## 5. Environmental information

The important non-genetic exposures are local and mechanistic rather than conventional environmental epidemiology: vascular contact, demyelinating disease, tumors, trauma, surgery/dentistry, infection, and cervical/occipital nerve irritation. GPN-associated infections include tonsillitis, pharyngitis, arachnoiditis, abscess, and tuberculosis. There is no evidence that cranial neuralgia is contagious or zoonotic. (wu2023percutaneousradiofrequencythermocoagulation pages 1-2)

## 6. Mechanism and pathophysiology

### Causal chain for classical TN/GPN

**Vascular loop/contact at root-entry zone → chronic pulsatile compression → focal oligodendrocyte/peripheral-myelin injury and axonal juxtaposition → altered ion-channel distribution and reduced firing threshold → ectopic activity plus ephaptic cross-excitation between tactile Aβ fibers and nociceptive pathways → synchronized high-frequency bursts → brief stimulus-evoked severe pain.** The “ignition hypothesis” explains triggerability, amplification, abrupt cessation, and refractory periods. Persistent pain likely adds ongoing axonal injury, peripheral sensitization, central sensitization, and altered brain pain networks. (stefano2019trigeminalneuralgiafrom pages 14-23, fried2020animalmodelsof pages 1-2)

### Secondary disease chains

- **MS plaque/brainstem lesion → central demyelination at trigeminal pathways → hyperexcitability/ephaptic activity → TN phenotype.**
- **Tumor/aneurysm/vascular malformation → compression or infiltration → demyelination/axonal injury → neuralgia ± sensory deficit.**
- **Trauma/dental injury → Wallerian injury and ectopic neuroma activity → macrophage/T-cell/glial activation and cytokines → peripheral and central sensitization → painful trigeminal neuropathy.**
- **STIM1–ORAI1 activation → SOCE in immune/neural cells → T-cell TNF-α/IL-1β/IL-6 release → neuroinflammation and excitability** is a 2024 experimental hypothesis, not yet a proven human causal pathway. (cheng2024novelinsightsinto pages 1-2)

### Suggested ontology annotations

**GO biological process:** nervous-system process; sensory perception of pain; detection of mechanical stimulus; action-potential initiation/propagation; regulation of membrane potential; myelination/demyelination; synaptic transmission; neuroinflammatory response; calcium-ion influx; store-operated calcium entry; cytokine production; T-cell activation; glial activation.

**GO cellular component:** axon, myelin sheath, node/paranode, neuronal cell body, plasma membrane, voltage-gated sodium-channel complex, ER membrane, STIM1–ORAI1 complex, synapse.

**Cell Ontology candidates:** sensory neuron; trigeminal ganglion neuron; pseudounipolar neuron; nociceptor; Schwann cell; oligodendrocyte; microglial cell; astrocyte; macrophage; T lymphocyte.

No consistent enzyme deficiency or systemic metabolic defect is known. Protein dysfunction is mainly functional—channel redistribution/hyperexcitability and altered myelin organization—not a demonstrated cranial-neuralgia-specific misfolding/aggregation disorder.

## 7. Anatomical structures affected

The primary system is the peripheral and central somatosensory nervous system.

- **TN:** CN V root-entry zone at the pons, trigeminal ganglion/Gasserian ganglion, and V1 ophthalmic, V2 maxillary, or V3 mandibular branches; secondary central involvement includes trigeminal nuclei, thalamus, and pain networks.
- **GPN:** CN IX rootlets near the medulla/cerebellopontine angle and sensory territory at the posterior tongue, tonsillar fossa, pharynx, middle/deep ear, and mandibular angle; vagal/cardiorespiratory reflex circuits may be recruited.
- **ON:** greater, lesser, and third occipital nerves; C2–C3 roots/dorsal rami; posterior scalp and upper cervical tissues.
- **Nervus intermedius:** sensory component of CN VII, geniculate region, and deep external auditory canal/periauricular territory.

Suggested UBERON mappings include trigeminal nerve, trigeminal ganglion, pons, cerebellopontine angle, glossopharyngeal nerve, medulla oblongata, tongue, palatine tonsil, pharynx, ear, cervical spinal cord C2–C3 region, occipital nerve, and scalp. Laterality is commonly unilateral; TN has been reported more often on the right, whereas GPN may be more often left-sided. Bilateral TN should increase suspicion for MS or another secondary process. (wu2023percutaneousradiofrequencythermocoagulation pages 1-2, peng2023fullyendoscopicmicrovascular pages 1-2)

## 8. Temporal development

Typical onset is adult or late adult, usually after 50; pediatric presentation is unusual and warrants careful secondary/genetic evaluation. Attacks begin abruptly, last seconds to two minutes in TN, recur in volleys, and may cluster over weeks or months. Spontaneous remissions can last months or years, but recurrence is characteristic. Some patients evolve from purely episodic paroxysms to paroxysms with continuous background pain. (stefano2019trigeminalneuralgiafrom pages 14-23, fried2020animalmodelsof pages 1-2)

There is no universal staging system. A practical trajectory is: **early triggerable paroxysms → recurrent active/remission cycles → medication-responsive disease → intolerance or pharmacoresistance → interventional/surgical disease**, with an additional “continuous-pain” phenotype. Critical opportunities are early recognition, exclusion of tumor/MS, prevention of unnecessary dental procedures, and cause-directed decompression before prolonged disability when appropriate.

## 9. Inheritance and population

Umbrella-level prevalence is not meaningful because subtypes differ. TN annual incidence has been reported at **4.5–28.9/100,000**, and lifetime prevalence near **0.3%**. Women are more often affected, with incidence concentrated in middle and older age. GPN incidence is approximately **0.2–0.8/100,000/year**, increasing after age 50. Reliable contemporary population estimates for ON and nervus intermedius neuralgia were not established in the retrieved evidence. (gerwin2020chronicfacialpain pages 1-3, wu2023percutaneousradiofrequencythermocoagulation pages 1-2, peng2023fullyendoscopicmicrovascular pages 1-2)

Most TN is sporadic and multifactorial. Familial clustering (estimated 2–11%) does not justify assigning a general AD or AR inheritance code. Penetrance and expressivity are unquantified; anticipation, founder effects, carrier frequency, consanguinity effects, and geographic variant distributions are not established. (lafta2024genomicvalidationin pages 1-2)

## 10. Diagnostics

### Clinical criteria and work-up

Diagnosis is clinical and phenotype-first. For TN, verify the ICHD-3 attack duration, severity, electric/shooting quality, trigeminal distribution, and innocuous triggers. Examine all cranial nerves and map touch, pinprick, temperature, and corneal reflexes. Objective sensory loss, bilateral disease, young onset, hearing change, vestibular signs, systemic cancer/infection, or poor carbamazepine response heighten concern for secondary disease. There is no validated blood, CSF, urine, tissue, or circulating biomarker. (tepper2018cranialneuralgias pages 1-2, stefano2019trigeminalneuralgiafrom pages 14-23)

Obtain **brain MRI with and without contrast plus high-resolution cranial-nerve sequences and MRA** to identify morphological neurovascular compression and exclude MS, tumor, aneurysm, vascular malformation, infarction, or inflammatory lesions. MRI supports etiologic classification and surgical planning; incidental vascular contact alone does not establish TN. CT is secondary when MRI is contraindicated or bone/skull-base pathology is suspected. (tepper2018cranialneuralgias pages 1-2)

Neurophysiological trigeminal reflexes and evoked potentials may support lesion localization in selected secondary cases but are not routine confirmatory tests. Diagnostic local-anesthetic blocks can support ON/GPN localization but false-positive responses are possible.

### Differential diagnosis

Exclude dental pulp/periodontal disease, temporomandibular disorder, persistent idiopathic facial pain, painful post-traumatic trigeminal neuropathy, postherpetic neuralgia, migraine, cluster headache and other trigeminal autonomic cephalalgias, SUNCT/SUNA, temporal arteritis, otitis/ENT disease, Eagle syndrome, cervical facet/radicular pain, tumors, and MS. Autonomic signs do not automatically imply a trigeminal autonomic cephalalgia: 40% of craniofacial-neuralgia patients in the 2024 meta-analysis had at least one. (thomas2024autonomicfeaturesof pages 1-2)

### Genetic/omics testing and screening

Routine WES, WGS, gene panels, single-gene tests, CMA, karyotype, FISH, mtDNA testing, and repeat-expansion testing are **not indicated** for typical sporadic neuralgia. Consider genetics only for unusual familial clustering, syndromic findings, childhood onset, or an independently suspected channelopathy/neuropathy. No asymptomatic population, newborn, carrier, or cascade screening program is recommended.

## 11. Outcome and prognosis

Cranial neuralgias generally do not reduce life expectancy. GPN-associated bradyarrhythmia/syncope and treatment complications are exceptions requiring urgent attention. Morbidity is driven by recurrent excruciating pain, impaired eating/speaking/hygiene, sleep disturbance, anxiety/depression, medication toxicity, and procedure-related sensory deficits. (kisielcybula2024trigeminalneuralgia pages 15-18, wu2023percutaneousradiofrequencythermocoagulation pages 1-2)

Prognosis varies by cause, presence of continuous pain, disease duration, structural compression, treatment tolerability, and procedure. In a 2023 fully endoscopic MVD case series, CPA area ratio, disease duration, and offending-vessel type were associated with recurrence. This is retrospective hypothesis-generating evidence, not a validated prognostic calculator. (peng2023fullyendoscopicmicrovascular pages 1-2)

## 12. Treatment and current implementation

### Pharmacotherapy

1. **Carbamazepine** and **oxcarbazepine** are first-line for TN and commonly GPN. They stabilize inactivated voltage-gated sodium channels and suppress high-frequency firing. Monitor sedation, dizziness, ataxia, hyponatremia, hepatic/hematologic toxicity, rash, and interactions. Carbamazepine pharmacogenomic screening for severe cutaneous-reaction risk is appropriate according to ancestry and local prescribing guidance, but it predicts toxicity—not neuralgia susceptibility. (stefano2019trigeminalneuralgiafrom pages 14-23, wu2023percutaneousradiofrequencythermocoagulation pages 1-2, wu2019botulinumtoxintype pages 1-2)
2. **Lamotrigine, baclofen, gabapentin/pregabalin**, and other anticonvulsant/neuropathic-pain agents are alternatives or add-ons when first-line treatment fails or is not tolerated. Combination therapy is generally considered after unsuccessful monotherapy. (tepper2018cranialneuralgias pages 1-2, kolakowski2024interdisciplinarystrategiesfor pages 9-9)
3. **Botulinum toxin A** is an off-label option for refractory TN. In a 104-patient retrospective cohort, 87 responded—41 complete and 46 adequate relief, **83.7% overall**; 17 patients (**16.3%**) reported mild adverse effects. Age ≥50 predicted success (OR 3.66, 95% CI 1.231–10.885). Published July 29, 2019; DOI: https://doi.org/10.2147/JPR.S205467. The study supports effectiveness but is not randomized. (wu2019botulinumtoxintype pages 1-2)

### Procedures and surgery

**Microvascular decompression (MVD)** is cause-directed and offers the longest medication-free relief for medically refractory classical TN/GPN with convincing compression and acceptable operative risk. It preserves the nerve but entails craniotomy and risks hearing loss, cranial neuropathy, CSF leak, stroke, infection, and rare death. A cited meta-analysis estimated a pain-free state in **92.9% (95% CI 89.1–96.8)** after 5 months–5 years. (stefano2019trigeminalneuralgiafrom pages 14-23, han2022glossopharyngealneuralgiaepidemiology pages 11-12)

A 2023 single-center retrospective endoscopic-MVD series included 115 TN and 10 GPN patients. TN effectiveness was reported as **98.9%** (105 complete, five significant, four partial responses), with 11 TN recurrences over 3–42 months (mean 18.6±3.3). All 10 GPN patients had complete relief. Across the whole neurovascular-compression cohort, temporary facial numbness occurred in four, temporary hearing loss in five, dizziness/nausea in eight, and headache in 12. The uncontrolled design, selection, and short follow-up limit generalization. Published October 2023; DOI: https://doi.org/10.1186/s12893-023-02214-0. (peng2023fullyendoscopicmicrovascular pages 1-2)

**Percutaneous procedures** include Gasserian-ganglion radiofrequency thermocoagulation, balloon compression, and glycerol rhizolysis. They are useful for older/high-risk patients or those preferring less invasive treatment, but trade pain control for facial numbness, dysesthesia, corneal anesthesia, masseter weakness, and rare anesthesia dolorosa. Stereotactic radiosurgery has delayed onset and recurrence risk but avoids open surgery.

For GPN, a 2023 retrospective comparison found both percutaneous radiofrequency thermocoagulation and MVD reduced pain and improved sleep through 48 weeks. Complete remission at 48 weeks was higher with MVD; adverse-event rates did not differ significantly, while hospital stay, operating time, and cost were higher. DOI: https://doi.org/10.1186/s12883-023-03415-z. (wu2023percutaneousradiofrequencythermocoagulation pages 1-2)

For ON, local anesthetic ± corticosteroid blocks, pulsed radiofrequency, ablation, and occipital peripheral-nerve stimulation are used after conservative treatment, but evidence quality is heterogeneous.

**Suggested NCIT intervention mappings:** anticonvulsant therapy; carbamazepine; oxcarbazepine; baclofen; botulinum toxin A injection; nerve block; radiofrequency ablation/thermocoagulation; stereotactic radiosurgery; microvascular decompression; peripheral nerve stimulation; neuromodulation. Exact NCIT accessions should be validated against the current release.

### Experimental/current trials

- **NCT06620172:** randomized, outcome-assessor-masked trial of CT-guided versus fluoroscopy-guided trigeminal-ganglion RFT for idiopathic TN; target n=60, recruiting in the retrieved November 2024 record, with NRS/VAS, medication use, and adverse events through six months. https://clinicaltrials.gov/study/NCT06620172 (NCT06620172 chunk 1)
- **NCT05491915 (MONARCH):** multicenter single-arm SPRINT 60-day occipital PNS study for ON/cervicogenic headache; estimated n=50, active but not recruiting in the latest retrieved record; assesses pain/interference, medication use, and adverse events. https://clinicaltrials.gov/study/NCT05491915 (NCT05491915 chunk 1)
- **NCT07013500:** nonrandomized retrospective comparison of conventional Gasserian thermal RFA with peripheral pulsed RFA, estimated n=60; first posted June 10, 2025 and therefore outside the requested 2023–2024 priority window. Its designation as “interventional/not yet recruiting” despite retrospective record review should be interpreted cautiously. https://clinicaltrials.gov/study/NCT07013500 (NCT07013500 chunk 1)

No established gene, cell, RNA, or immune therapy exists for cranial neuralgia. STIM1/SOCE inhibition, complement/neuroinflammation targeting, and advanced neuromodulation remain preclinical or exploratory.

## 13. Prevention

There is no proven primary prevention for idiopathic or neurovascular-compression neuralgia. Practical prevention is etiologic:

- minimize avoidable trigeminal injury during dental, implant, anesthetic, and craniofacial procedures;
- promptly treat relevant infections and investigate progressive cranial-nerve symptoms;
- in diagnosed disease, prevent disability through early accurate classification, MRI exclusion of secondary causes, medication monitoring, oral/nutritional support, and mental-health care;
- avoid repeated irreversible dental procedures when the phenotype is neuralgic.

Vaccination has no disease-specific preventive role, although routine zoster vaccination prevents herpes zoster and thereby some postherpetic cranial neuropathic pain—not classical TN. No prophylactic medication or preventive MVD is recommended for asymptomatic people.

## 14. Other species and natural disease

No well-established naturally occurring veterinary disease in dogs, cats, livestock, or wildlife has been shown to reproduce the full human syndrome of classical TN/GPN. “Trigeminal neuritis/neuropathy” in animals should not automatically be coded as human-like neuralgia. There is no transmission or zoonotic potential.

Human candidate genes have conserved mammalian orthologs, including **C8B, MFGE8, STIM1, and ORAI1**, but conservation alone does not establish an animal disease homolog. NCBI Taxon suggestions for experimental annotations are **Homo sapiens 9606**, **Mus musculus 10090**, and **Rattus norvegicus 10116**.

## 15. Model organisms

Rodent models include chronic constriction or chemical injury of the infraorbital nerve, trigeminal root-entry-zone compression, demyelination paradigms, and associated cell/tissue preparations. They measure facial mechanical allodynia, grooming, head withdrawal, neural excitability, myelin ultrastructure, glial/immune activation, and molecular pathways. Root-compression models better approximate classical compression; infraorbital injury better models painful post-traumatic trigeminal neuropathy.

The major expert caution is construct validity. Fried and Hansson identified at least 21 papers from 2016–2019 claiming an animal TN model and argued that mechanical infraorbital injury does not reproduce human triggerable, seconds-long paroxysms and refractory periods. Their conclusion is explicit: “Experimental damage to the infraorbital nerve as a model for TN is indeed questionable.” Published December 2020; DOI: https://doi.org/10.1177/1744806920980538. (fried2020animalmodelsof pages 1-2)

Accordingly, experimental annotations should specify **species, injury, nerve/site, behavioral endpoint, and whether the model represents classical TN or traumatic neuropathy**. Findings such as STIM1–SOCE/T-cell cytokine signaling should remain tagged as computational/animal/in-vitro until independently replicated in human nerve, CSF, or longitudinal clinical material. (cheng2024novelinsightsinto pages 1-2)

## Evidence assessment and principal gaps

The evidence hierarchy is strongest for TN clinical criteria, MRI work-up, sodium-channel-blocker therapy, and MVD. Recent 2024 advances suggest immune/inflammatory susceptibility through C8B/MFGE8 and STIM1–SOCE, but neither is ready for diagnosis or targeted therapy. Surgical response estimates are impressive but often derive from selected, retrospective single-center cohorts. ON and nervus intermedius neuralgia lack modern population cohorts, molecular profiling, validated biomarkers, and high-quality comparative trials. Protective factors, gene–environment interactions, epigenetic signatures, disease-specific multi-omics, natural animal disease, and genomic screening remain unavailable or investigational.

References

1. (tepper2018cranialneuralgias pages 1-2): Stewart J. Tepper. Cranial neuralgias. CONTINUUM: Lifelong Learning in Neurology, 24:1157–1178, Aug 2018. URL: https://doi.org/10.1212/con.0000000000000637, doi:10.1212/con.0000000000000637. This article has 40 citations.

2. (stefano2019trigeminalneuralgiafrom pages 14-23): G Di Stefano. Trigeminal neuralgia: from clinical characteristics to pathological mechanisms. Unknown journal, 2019.

3. (lafta2024genomicvalidationin pages 1-2): Muataz S. Lafta, Gull Rukh, Sami Abu Hamdeh, Yasmina Molero, Aleksandr V. Sokolov, Elham Rostami, and Helgi B. Schiöth. Genomic validation in the uk biobank cohort suggests a role of c8b and mfg-e8 in the pathogenesis of trigeminal neuralgia. Journal of Molecular Neuroscience, Oct 2024. URL: https://doi.org/10.1007/s12031-024-02263-x, doi:10.1007/s12031-024-02263-x. This article has 1 citations and is from a peer-reviewed journal.

4. (thomas2024autonomicfeaturesof pages 1-2): Davis C. Thomas, Priyanka Kodaganallur Pitchumani, Abdul Basir Barmak, Sandeep Talluri, and Weiran Jiang. Autonomic features of craniofacial neuralgias: a systematic review with meta-analysis. Journal of Oral & Facial Pain and Headache, 38:15-31, Sep 2024. URL: https://doi.org/10.22514/jofph.2024.023, doi:10.22514/jofph.2024.023. This article has 2 citations and is from a peer-reviewed journal.

5. (wu2023percutaneousradiofrequencythermocoagulation pages 1-2): Zeyu Wu, Yongming Zhao, Fan Wu, Yiyue Fan, and Ying Yang. Percutaneous radiofrequency thermocoagulation and microvascular decompression for treating glossopharyngeal neuralgia: a retrospective clinical study. BMC Neurology, Oct 2023. URL: https://doi.org/10.1186/s12883-023-03415-z, doi:10.1186/s12883-023-03415-z. This article has 11 citations and is from a peer-reviewed journal.

6. (peng2023fullyendoscopicmicrovascular pages 1-2): Weicheng Peng, Rui Zhao, Feng Guan, Xin Liang, Bei Jing, Guangtong Zhu, Beibei Mao, and Zhiqiang Hu. Fully endoscopic microvascular decompression for the treatment of hemifacial spasm, trigeminal neuralgia, and glossopharyngeal neuralgia: a retrospective study. BMC Surgery, Oct 2023. URL: https://doi.org/10.1186/s12893-023-02214-0, doi:10.1186/s12893-023-02214-0. This article has 33 citations and is from a peer-reviewed journal.

7. (NCT05491915 chunk 1):  The MONARCH Case Series Study: SPRINT® Peripheral Nerve Stimulation for the Treatment of Head Pain. SPR Therapeutics, Inc.. 2022. ClinicalTrials.gov Identifier: NCT05491915

8. (kolakowski2024interdisciplinarystrategiesfor pages 9-9): Lukasz Kolakowski, Heiko Pohl, Lennart Stieglitz, Anthony De Vere-Tyndall, Michael B. Soyka, Patrizia Räber-Jäggy, Julia Wagner, Constantina V. Marinescu, Michelle L. Brown, Michael Blumer, Günter T. Müller, and Susanne Wegener. Interdisciplinary strategies for diagnosis and treatment of trigeminal neuralgia. Swiss medical weekly, 154:3460, Jul 2024. URL: https://doi.org/10.57187/s.3460, doi:10.57187/s.3460. This article has 15 citations and is from a peer-reviewed journal.

9. (wu2019botulinumtoxintype pages 1-2): Shouyi Wu, Yajun Lian, Haifeng Zhang, Yuan Chen, Chuanjie Wu, Shuang Li, Yake Zheng, Yuhan Wang, Wenchao Cheng, and Zhi Huang. Botulinum toxin type a for refractory trigeminal neuralgia in older patients: a better therapeutic effect. Journal of Pain Research, 12:2177-2186, Jul 2019. URL: https://doi.org/10.2147/jpr.s205467, doi:10.2147/jpr.s205467. This article has 33 citations and is from a peer-reviewed journal.

10. (gerwin2020chronicfacialpain pages 1-3): Robert Gerwin. Chronic facial pain: trigeminal neuralgia, persistent idiopathic facial pain, and myofascial pain syndrome—an evidence-based narrative review and etiological hypothesis. Sep 2020. URL: https://doi.org/10.3390/ijerph17197012, doi:10.3390/ijerph17197012. This article has 88 citations.

11. (NCT06620172 chunk 1): Ahmed Awad Bessar. CT-guided vs Fluoroscopy-guided Trigeminal Ganglion Radiofrequency Thermocoagulation for Idiopathic Trigeminal Neuralgia. Zagazig University. 2024. ClinicalTrials.gov Identifier: NCT06620172

12. (han2022glossopharyngealneuralgiaepidemiology pages 11-12): Andrew Han, Carver Montgomery, Alexandra Zamora, Emilie Winder, Adam D. Kaye, Caroline Carroll, Alfonso Aquino, Juyeon Kakazu, and Alan D. Kaye. Glossopharyngeal neuralgia: epidemiology, risk factors, pathophysiology, differential diagnosis, and treatment options. Health psychology research, 10 3:36042, Jun 2022. URL: https://doi.org/10.52965/001c.36042, doi:10.52965/001c.36042. This article has 40 citations and is from a peer-reviewed journal.

13. (fried2020animalmodelsof pages 1-2): Kaj Fried and Per T Hansson. Animal models of trigeminal neuralgia: a commentary. Molecular Pain, Dec 2020. URL: https://doi.org/10.1177/1744806920980538, doi:10.1177/1744806920980538. This article has 16 citations and is from a peer-reviewed journal.

14. (kisielcybula2024trigeminalneuralgia pages 15-18): Ewelina Kisiel-Cybula, Irena Sionek-Wręga, Eliza Jakubowska, Julia Ślemp, Anita Pakuła, Krzysztof Kuźma, Karolina Bierć, Marcelina Grochowska, Ewa Hoppe-Mitera, and Jakub Wręga. Trigeminal neuralgia - impact on daily activities and sports, treatment options that enable a pain-free life. Journal of Education, Health and Sport, 75:55856, Dec 2024. URL: https://doi.org/10.12775/jehs.2024.75.55856, doi:10.12775/jehs.2024.75.55856. This article has 1 citations.

15. (cheng2024novelinsightsinto pages 1-2): Guangyu Cheng, Yu Zhao, Fujia Sun, and Qi Zhang. Novel insights into stim1's role in store-operated calcium entry and its implications for t-cell mediated inflammation in trigeminal neuralgia. Frontiers in Molecular Neuroscience, Jun 2024. URL: https://doi.org/10.3389/fnmol.2024.1391189, doi:10.3389/fnmol.2024.1391189. This article has 2 citations.

16. (NCT07013500 chunk 1): Mesut Bakır. Comparison of Two Types of Radiofrequency Treatment for Trigeminal Neuralgia. Mesut Bakır. 2025. ClinicalTrials.gov Identifier: NCT07013500

## Artifacts

- [Edison artifact artifact-00](Cranial_Neuralgia-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 14 |
| Resolved | 14 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 14 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 1 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 0 |

Every term resolved, and every label the report gave matched.