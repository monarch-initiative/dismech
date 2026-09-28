---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-28T22:54:00.107138'
end_time: '2026-08-28T23:02:47.440117'
duration_seconds: 527.33
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Lethal Congenital Contracture Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 30
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 9
  off_topic: 1
  off_topic_references:
  - DOI:10.1038/s41467-021-23599-7
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 32
  verified: 32
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 6
  labels_matching: 3
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Lethal_Congenital_Contracture_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Lethal Congenital Contracture Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Lethal Congenital Contracture Syndrome** covering all of the
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
- **Disease Name:** Lethal Congenital Contracture Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Lethal Congenital Contracture Syndrome** covering all of the
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


# Lethal Congenital Contracture Syndrome: Research Report

## Executive summary

**Lethal congenital contracture syndromes (LCCSs)** are a genetically heterogeneous group of predominantly autosomal-recessive fetal-akinesia disorders. Reduced or absent fetal movement causes congenital contractures and secondary deformation—pulmonary hypoplasia, craniofacial abnormalities, growth restriction, polyhydramnios, and sometimes hydrops. “Arthrogryposis” is a descriptive finding rather than a single diagnosis; LCCS overlaps clinically with arthrogryposis multiplex congenita (AMC), fetal akinesia deformation sequence (FADS), and Pena–Shokeir syndrome type I. AMC overall occurs in approximately 1/3,000–1/5,000 births, but each molecular LCCS subtype is much rarer, usually represented by only a few families. (potrony2022lethalcongenitalcontracture pages 1-2, wambach2017survivalamongchildren pages 1-3)

The best-established molecular forms in the retrieved evidence involve **GLE1, ERBB3, PIP5K1C, ZBTB42, CNTNAP1, ADCY6, NEK9,** and **GLDN**. These converge on failure of the fetal motor unit or musculoskeletal development through RNA metabolism, motor-neuron survival, axon–glial organization, nodal conduction, phosphoinositide/cAMP signaling, mitosis, and ciliogenesis. The label “lethal” is not absolute: especially in **GLDN-related LCCS11**, survival into childhood or adolescence is possible with intensive respiratory and nutritional support. (beecroft2018geneticsofneuromuscular pages 3-4, wambach2017survivalamongchildren pages 1-3)

| Subtype | OMIM disease ID | Gene | Molecular role / mechanism | Hallmark distinguishing findings | Lethality / survival | Key evidence / date |
|---|---:|---|---|---|---|---|
| LCCS1 | 253310 | GLE1 | Regulates mRNA export and translation; GLE1-related fetal motor neuron disease with anterior horn involvement (trabacca2024updateoninherited pages 11-12, nousiainen2011molecularbackgroundofa pages 24-26) | Complete fetal immobility, severe hydrops, intrauterine growth restriction; flexion contractures, knee hyperextension, pulmonary hypoplasia, micrognathia; fetal death often before 32 weeks (nousiainen2011molecularbackgroundofa pages 24-26, trabacca2024updateoninherited pages 11-12) | Usually prenatal lethal / fetal death before 32 weeks (trabacca2024updateoninherited pages 11-12, nousiainen2011molecularbackgroundofa pages 24-26) | Nousiainen thesis evidence summarized in retrieved text; Trabacca review 2024 (nousiainen2011molecularbackgroundofa pages 24-26, trabacca2024updateoninherited pages 11-12) |
| LCCS2 | not established from retrieved evidence | ERBB3 | Gene assignment supported in review-level retrieved evidence; detailed molecular mechanism not established from primary retrieved text (trabacca2024updateoninherited pages 11-12) | Cranial and ocular abnormalities, enlarged bladder with hydronephrosis, cystic kidney changes (trabacca2024updateoninherited pages 11-12) | Usually fatal shortly after birth (trabacca2024updateoninherited pages 11-12) | Trabacca review 2024; pediatric motor neuron review evidence in conversation (trabacca2024updateoninherited pages 11-12) |
| LCCS3 | 611369 | PIP5K1C | Phosphatidylinositol-4-phosphate 5-kinase; synthesizes PIP2; reported disease mechanism is haploinsufficiency / truncating loss of function in retrieved evidence (zhang2024novelpip5k1cvariant pages 1-2, zhang2024novelpip5k1cvariant pages 2-5) | Small gestational age, severe multiple joint contractures, muscle atrophy, respiratory failure; detailed fetal findings include talipes equinovarus, extended knees, closed hands/overlapping fingers; possible bilateral dilated lateral ventricles in one fetus (zhang2024novelpip5k1cvariant pages 1-2, zhang2024novelpip5k1cvariant pages 2-5) | Early death due to respiratory failure; prior five reported individuals all died in summarized table, plus two Chinese fetuses described (zhang2024novelpip5k1cvariant pages 1-2, zhang2024novelpip5k1cvariant pages 2-5) | Zhang et al., BMC Pediatrics, 2024; novel c.949_952dup p.S318Ifs*28 plus c.688_689del p.G230Qfs*114 (zhang2024novelpip5k1cvariant pages 1-2, zhang2024novelpip5k1cvariant pages 2-5) |
| LCCS6 | 613915 | ZBTB42 | Not established from retrieved evidence beyond subtype-gene association mention in review evidence (beecroft2018geneticsofneuromuscular pages 3-3) | Not established from retrieved evidence | Not established from retrieved evidence | Mentioned in Beecroft review 2018 as LCCS6/ZBTB42 association (beecroft2018geneticsofneuromuscular pages 3-3) |
| LCCS7 | inconsistent in retrieved evidence: 616286 vs 607598 | CNTNAP1 | CASPR; essential node of Ranvier component for saltatory conduction; severe axoglial / myelinated axon abnormalities with very low motor nerve conduction velocity (laquerriere2014mutationsincntnap1 pages 1-2, beecroft2018geneticsofneuromuscular pages 3-4) | Severe arthrogryposis / fetal akinesia with peripheral nerve axoglial defects; marked reduction in motor nerve conduction velocity (<10 m/s) (laquerriere2014mutationsincntnap1 pages 1-2) | In review summary, 5 of 7 patients died within 2 months; exact survival spectrum not fully established here (beecroft2018geneticsofneuromuscular pages 3-4) | Laquerriere et al., Hum Mol Genet, 2014; Beecroft review 2018 notes OMIM inconsistency in retrieved evidence (laquerriere2014mutationsincntnap1 pages 1-2, beecroft2018geneticsofneuromuscular pages 3-4) |
| LCCS8 | 616287 | ADCY6 | Adenylyl cyclase type 6; membrane-associated enzyme catalyzing cAMP formation; associated with lack of PNS myelin / hypomyelinating neuropathy in reported cases (agolini2020expandingtheclinical pages 1-6, laquerriere2014mutationsincntnap1 pages 1-2) | Distal joint contractures, severe hypotonia, lack of swallowing, absent autonomous respiratory function and deep tendon reflexes; may include hydrocephalus, severe muscle loss, hypomyelinating neuropathy (agolini2020expandingtheclinical pages 1-6) | Original reported siblings died within first 3 months; additional patient died at 36 months after intensive support (agolini2020expandingtheclinical pages 1-6, beecroft2018geneticsofneuromuscular pages 3-4) | Agolini et al., Clin Genet, 2020; Laquerriere et al., 2014 discovery paper (agolini2020expandingtheclinical pages 1-6, laquerriere2014mutationsincntnap1 pages 1-2) |
| LCCS10 | 617022 | NEK9 | NIMA-related serine/threonine kinase; mitotic spindle / centrosome functions; linked to defective primary cilia formation, with broader cilia/autophagy evidence from NEK9 biology (liu2023novelvariantsof pages 1-2, yamamoto2021nek9regulatesprimary pages 1-2) | Multiple joint contractures / arthrogryposis; severe cases reported with shortened limbs in literature summaries; neonatal cases included camptodactyly, stiff neck, pyloric stenosis, heart defects (liu2023novelvariantsof pages 1-2, liu2023novelvariantsof pages 2-5) | Historically described as lethal fetal form, but 2023 report expands to neonatal survivors/discharges; full survival range not established from retrieved evidence (liu2023novelvariantsof pages 1-2, liu2023novelvariantsof pages 2-5) | Liu et al., Front Genet, 2023; novel variants c.717C>A, c.2824delA, c.61G>T not in ClinVar/HGMD/gnomAD (liu2023novelvariantsof pages 1-2, liu2023novelvariantsof pages 2-5) |
| LCCS11 | 617194 | GLDN | Gliomedin; required for nodes of Ranvier formation and peripheral nervous system development; GLDN variants disrupt nodal interactions and can be framed as FADS-spectrum nodopathy (potrony2022lethalcongenitalcontracture pages 1-2, mis2020thelatestfads pages 1-2) | Hydrops, short long bones, fixed limb joints, absent fetal movements, polyhydramnios, growth restriction, pulmonary hypoplasia, retrognathia; distal arthrogryposis (potrony2022lethalcongenitalcontracture pages 1-2) | Not invariably lethal: 4/6 additional patients in 2017 survived beyond neonatal period with intensive chronic respiratory/nutritional support; condition may extend into childhood/adolescence (wambach2017survivalamongchildren pages 1-3, mis2020thelatestfads pages 1-2) | Wambach et al., Hum Mutat, 2017; Potrony et al., J Clin Med, 2022; Mis et al., AJMG A, 2020 (wambach2017survivalamongchildren pages 1-3, potrony2022lethalcongenitalcontracture pages 1-2, mis2020thelatestfads pages 1-2) |


*Table: This table summarizes lethal congenital contracture syndrome subtypes supported by evidence retrieved in the conversation. It highlights subtype-gene relationships, distinguishing findings, survival patterns, and places where the evidence base is incomplete or internally inconsistent.*

## 1. Disease information

### Definition and scope

LCCS is characterized by prenatal-onset hypokinesia or akinesia, multiple fixed joint contractures, and severe neuromuscular or skeletal developmental disease. Contractures are generally non-progressive structural consequences of impaired fetal movement, although respiratory, nutritional, and neurologic morbidity may evolve after birth in survivors. Secondary deformation can include pulmonary hypoplasia, micrognathia/retrognathia, short neck, pterygia, shortened umbilical cord, polyhydramnios, impaired gut motility, and growth restriction. (nousiainen2011molecularbackgroundofa pages 24-26, potrony2022lethalcongenitalcontracture pages 1-2)

**Synonyms/overlap terms:** multiple congenital contractures; arthrogryposis multiplex congenita; fetal akinesia deformation sequence; Pena–Shokeir syndrome type I; for LCCS1, multiple contracture syndrome, Finnish type or Herva disease. GLE1-related lethal arthrogryposis with anterior horn-cell disease (LAAHD/CAAHD) is allelic and clinically overlapping but often distinguished from classic LCCS1. (nousiainen2011molecularbackgroundofa pages 24-26, potrony2022lethalcongenitalcontracture pages 1-2, trabacca2024updateoninherited pages 11-12)

### Identifiers

The umbrella disorder does not have one reliably verified identifier in the retrieved literature; subtype-specific OMIM records are preferable. Verified examples are **LCCS1, OMIM 253310; LCCS3, 611369; LCCS6, 613915; LCCS8, 616287; LCCS10, 617022; and LCCS11, 617194**. Retrieved sources conflicted for LCCS7 (616286 versus 607598), so an operational knowledge base should resolve this directly against the current OMIM release before ingestion. No umbrella MONDO ID, dedicated ICD-10/ICD-11 code, or MeSH heading was verified here; clinically, cases are usually coded under arthrogryposis/multiple congenital malformations plus molecular diagnosis. (beecroft2018geneticsofneuromuscular pages 3-3, beecroft2018geneticsofneuromuscular pages 3-4, liu2023novelvariantsof pages 1-2, zhang2024novelpip5k1cvariant pages 1-2)

The evidence is **aggregated disease-level literature**, principally family reports, fetal/neonatal case series, molecular studies, and reviews—not patient-level EHR data.

## 2. Etiology and risk/protective factors

The primary cause is **biallelic germline pathogenic variation**. Most reported variants are homozygous in consanguineous/founder populations or compound heterozygous in unrelated parents. Disease mechanisms are commonly loss of function, including nonsense, frameshift, splice-disrupting, or damaging missense alleles. (liu2023novelvariantsof pages 1-2, zhang2024novelpip5k1cvariant pages 1-2, agolini2020expandingtheclinical pages 1-6)

The principal risk factors are parental carrier status, consanguinity, ancestry-specific founder alleles, and an affected pregnancy or sibling. The classic GLE1 LCCS1 allele is enriched in the Finnish disease heritage; the early PIP5K1C LCCS3 series involved an Israeli Bedouin kindred. A 2024 population analysis used 125,748 exomes and 15,708 genomes from gnomAD to estimate recessive neuromuscular carrier burdens, but it did not provide a sufficiently supported LCCS-specific prevalence estimate in the retrieved text. (beecroft2018geneticsofneuromuscular pages 3-4, choi2024globalcarrierfrequency pages 6-8, zhang2024novelpip5k1cvariant pages 2-5)

No reproducible environmental, lifestyle, infectious, sex-specific, or age-related risk factor is established for molecular LCCS. Likewise, no protective allele, modifier gene, protective exposure, or validated gene–environment interaction has been demonstrated. Maternal infection, oligohydramnios, uterine constraint, autoimmune disease, and teratogens are important **alternative causes of fetal akinesia/arthrogryposis**, not established causes of genetically confirmed LCCS. (illes2024heterogenicgeneticbackground pages 1-2)

## 3. Phenotypes

Core ontology-ready phenotypes include:

- **Decreased/absent fetal movement**—prenatal, severe, causally upstream; *HP:0001558 Decreased fetal movement* or *HP:0001989 Fetal akinesia*.
- **Multiple congenital joint contractures/arthrogryposis**—congenital, usually severe and structurally stable; *HP:0002804 Arthrogryposis multiplex congenita* and *HP:0012453 Arthrogryposis*.
- **Talipes equinovarus**—often bilateral; *HP:0001762*.
- **Camptodactyly/overlapping fingers/closed hands**—*HP:0012385*, *HP:0010557*.
- **Knee hyperextension or fixed flexion**, elbow/wrist/hip contractures—joint-specific contracture terms.
- **Muscle hypoplasia/atrophy and hypotonia**—*HP:0003202*, *HP:0001252*; neurogenic denervation may be present.
- **Areflexia**—*HP:0001284*.
- **Pulmonary hypoplasia and respiratory failure**—*HP:0002089*, *HP:0002878*; major determinants of mortality.
- **Polyhydramnios**—*HP:0001561*, often reflecting impaired swallowing.
- **Hydrops fetalis**—*HP:0001789*, particularly prominent in LCCS1 and some LCCS11 fetuses.
- **Intrauterine growth restriction**—*HP:0001511*.
- **Micrognathia/retrognathia and short neck**—*HP:0000347/HP:0000278*, *HP:0000470*.
- **Pterygia**—*HP:0001059*.
- **Feeding/swallowing difficulty**—*HP:0011968/HP:0002015*.

Subtype-enriched findings include renal/urinary abnormalities and cranio-ocular anomalies in ERBB3-related LCCS2; hypomyelinating neuropathy and vocal-cord paralysis in ADCY6-related LCCS8; pyloric stenosis and cardiac defects in some NEK9 patients; and possible ventriculomegaly in PIP5K1C LCCS3. In the 2024 PIP5K1C report, all seven detailed patients had dyskinesia and contractures; all five original Bedouin patients and one Chinese fetus died from respiratory insufficiency. Ventriculomegaly occurred in only one of two genetically identical Chinese fetuses and therefore remains a provisional association. (trabacca2024updateoninherited pages 11-12, liu2023novelvariantsof pages 2-5, zhang2024novelpip5k1cvariant pages 2-5, agolini2020expandingtheclinical pages 1-6)

Formal EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life data are unavailable. Functional burden in survivors is nevertheless profound: ventilation, tracheostomy, gastrostomy, mobility impairment, rehabilitation, and recurrent hospitalization may be required. Some GLDN survivors have preserved cognition and developmental progress despite severe neonatal disease. (mis2020thelatestfads pages 1-2, wambach2017survivalamongchildren pages 1-3)

## 4. Genetic and molecular information

All established LCCS alleles are **constitutional/germline**, not somatic. Representative variants include:

- **PIP5K1C/LCCS3:** homozygous c.757G>A (p.Asp253Asn) in five Bedouin patients; compound-heterozygous c.688_689del (p.G230Qfs*114) and novel c.949_952dup (p.S318Ifs*28) in two Chinese fetuses. The latter pair was classified pathogenic under ACMG/AMP criteria **PVS1+PM2+PP1+PP4**; both predict truncation, and p.S318Ifs*28 was considered unlikely to escape nonsense-mediated decay. All known variants summarized in that study localized to the PIPK domain. (zhang2024novelpip5k1cvariant pages 1-2, zhang2024novelpip5k1cvariant pages 2-5)
- **NEK9/LCCS10 spectrum:** c.717C>A, c.2824delA, and c.61G>T were reported in two neonates as compound-heterozygous truncating variants; none was present in ClinVar, HGMD, or gnomAD at publication. The report emphasizes mutation-dependent phenotypic breadth from lethal fetal disease to neonatal arthrogryposis. (liu2023novelvariantsof pages 1-2, liu2023novelvariantsof pages 2-5)
- **ADCY6/LCCS8:** compound-heterozygous c.1535+1G>A and c.3007G>A (p.Glu1003Lys) were identified in a severely affected girl; p.Glu1003Lys was absent from gnomAD. Earlier families carried homozygous missense alleles. (agolini2020expandingtheclinical pages 1-6)
- **CNTNAP1/LCCS7:** four unrelated families had homozygous frameshift variants causing severe axoglial disease. (laquerriere2014mutationsincntnap1 pages 1-2)
- **GLDN/LCCS11:** both homozygous and compound-heterozygous variants are established; p.Leu365Phe and p.Arg393Lys have functional evidence in a surviving patient. (mis2020thelatestfads pages 1-2, wambach2017survivalamongchildren pages 1-3)

No validated modifier genes, disease-specific methylation signature, recurrent pathogenic chromosomal rearrangement, or epigenetic mechanism is established. Normal karyotype/CMA in affected fetuses is common and does not exclude LCCS. (potrony2022lethalcongenitalcontracture pages 1-2, zhang2024novelpip5k1cvariant pages 1-2)

## 5. Environmental information

No toxin, radiation exposure, pollutant, occupation, diet, smoking, alcohol, exercise pattern, or infectious agent has been shown to cause or modify genetically confirmed LCCS. These variables matter chiefly in the differential diagnosis of fetal akinesia. LCCS is neither infectious nor transmissible.

## 6. Mechanism and pathophysiology

### Unifying causal chain

**Biallelic gene dysfunction → impaired motor-neuron development/survival, axonal conduction, neuromuscular signaling, or skeletal/ciliary development → reduced fetal muscle contraction → fetal akinesia → persistent joint positioning and connective-tissue fixation → multiple contractures; impaired breathing/swallowing movements → pulmonary hypoplasia, polyhydramnios, respiratory and feeding failure.** (illes2024heterogenicgeneticbackground pages 1-2, potrony2022lethalcongenitalcontracture pages 1-2)

### Gene-specific mechanisms

- **GLE1:** defective regulation of nuclear mRNA export and translation initiation/termination is associated with anterior-horn motor-neuron loss and severe skeletal-muscle atrophy. Suggested GO terms: *mRNA export from nucleus* (GO:0006406), *translation initiation* (GO:0006413), *translation termination* (GO:0006415), *motor neuron development* (GO:0021675). (trabacca2024updateoninherited pages 11-12)
- **CNTNAP1/CASPR:** disruption of axon–glial paranodal architecture impairs saltatory conduction. Patients had motor nerve conduction velocities below 10 m/s and severe abnormalities of nodes of Ranvier and myelinated axons. Suggested GO: *node of Ranvier assembly* and *myelination*; CL: motor neuron, Schwann cell. (laquerriere2014mutationsincntnap1 pages 1-2)
- **GLDN/gliomedin:** gliomedin interacts with NF186 and NrCAM to cluster sodium channels at peripheral nodes of Ranvier. Loss produces a developmental nodopathy, fetal hypomotility, and respiratory dysfunction. Suggested GO: *node of Ranvier assembly*, *sodium-channel clustering*; GO-CC: node of Ranvier; CL: Schwann cell and peripheral sensory/motor neuron. (mis2020thelatestfads pages 1-2, wambach2017survivalamongchildren pages 1-3)
- **ADCY6:** adenylyl cyclase 6 generates cAMP downstream of GPCR signaling. Biallelic dysfunction is associated with absent or deficient peripheral myelin, severe neurogenic damage, hypotonia, and areflexia. Suggested GO: *cAMP biosynthetic process* (GO:0006171), *G protein-coupled receptor signaling pathway*; CHEBI: cyclic AMP (CHEBI:17489). (laquerriere2014mutationsincntnap1 pages 1-2, agolini2020expandingtheclinical pages 1-6)
- **PIP5K1C:** the lipid kinase converts PI4P to phosphatidylinositol-4,5-bisphosphate (PIP2), supporting calcium signaling, actin dynamics, endocytosis/exocytosis, and synaptic function. Pip5k1c-null mice show approximately 50% lower brain PIP2 and impaired depolarization-dependent PIP2 synthesis at nerve terminals. Suggested GO: *phosphatidylinositol phosphorylation*, *synaptic vesicle exocytosis*, *actin cytoskeleton organization*; CHEBI: PI4P and PI(4,5)P2. (zhang2024novelpip5k1cvariant pages 1-2, zhang2024novelpip5k1cvariant pages 2-5)
- **NEK9:** this serine/threonine kinase participates in spindle assembly, centrosome separation, mitosis, and primary-cilium formation. Cell/mouse experiments show NEK9 acts as a selective-autophagy adaptor for MYH9; loss causes MYH9 accumulation, actin stabilization, and impaired ciliogenesis, while MYH9 depletion rescues ciliogenesis in mutant cells. Suggested GO: *mitotic spindle organization*, *centrosome separation*, *cilium assembly* (GO:0060271), *selective autophagy*; GO-CC: centrosome, primary cilium, autophagosome. (yamamoto2021nek9regulatesprimary pages 1-2, liu2023novelvariantsof pages 1-2)

Immune dysregulation, chronic inflammation, and a disease-specific metabolomic/lipidomic signature are not established. Beyond gene-focused experiments, no mature LCCS single-cell, spatial-transcriptomic, clinical proteomic, or integrated multi-omic atlas was identified.

## 7. Anatomical structures affected

Primary involvement is in the **fetal neuromuscular system**: spinal anterior-horn motor neurons, peripheral nerves and myelin, nodes/paranodes of Ranvier, neuromuscular unit, and skeletal muscle. Secondary deformation affects limb joints, hands, feet, jaw, neck, thorax, and lungs. Kidneys/urinary tract are particularly relevant in LCCS2; brain anomalies occur variably rather than universally. (nousiainen2011molecularbackgroundofa pages 24-26, trabacca2024updateoninherited pages 11-12, laquerriere2014mutationsincntnap1 pages 1-2)

Suggested UBERON annotations include spinal cord (UBERON:0002240), peripheral nervous system (UBERON:0000010), skeletal muscle tissue (UBERON:0001134), lung (UBERON:0002048), limb joint, hand, foot, mandible, kidney, and urinary bladder. Laterality is generally **bilateral/symmetric**, especially talipes and limb contractures, but asymmetry can occur.

## 8. Temporal development

Onset is prenatal, often detectable in the late first or second trimester through reduced movement and abnormal limb positioning. Classic LCCS1 can be recognized ultrasonographically around 11–12 weeks and commonly ends in fetal death before 32 weeks. Other forms may present at birth with respiratory failure, hypotonia, areflexia, feeding failure, or fixed contractures. (nousiainen2011molecularbackgroundofa pages 24-26, trabacca2024updateoninherited pages 11-12)

There are no validated disease stages or remission patterns. The mechanistic injury occurs during a critical fetal-development window; established contractures do not spontaneously reverse. In survivors, respiratory dependence may improve—one GLDN patient was weaned from respiratory support by 14 months—but feeding, mobility, and orthopedic needs may persist. (mis2020thelatestfads pages 1-2)

## 9. Inheritance and population

Inheritance is usually **autosomal recessive**. For two carrier parents, the Mendelian recurrence risk is 25% affected, 50% carrier, and 25% unaffected/non-carrier in each pregnancy. Penetrance appears high for clearly pathogenic biallelic alleles, but expressivity and lethality vary by gene and allele. Anticipation is not expected. Germline mosaicism has not been quantified; it remains a residual consideration when apparently de novo findings are encountered.

Consanguinity has played a major role in gene discovery. GLE1 LCCS1 is strongly associated with Finland and a founder allele; PIP5K1C LCCS3 was initially described in Bedouin patients. Outside founder groups, compound heterozygosity is common. No reliable sex bias exists because autosomal-recessive disease should affect both sexes equally. Subtype-specific incidence and carrier frequency remain unknown. (beecroft2018geneticsofneuromuscular pages 3-4, zhang2024novelpip5k1cvariant pages 1-2, zhang2024novelpip5k1cvariant pages 2-5)

## 10. Diagnostics

### Prenatal and clinical evaluation

Serial expert ultrasound should assess fetal movement, limb position, hands/feet, jaw, growth, amniotic fluid, hydrops, lung/thoracic development, kidneys/bladder, and CNS. Fetal MRI may clarify brain, spinal, pulmonary, or muscular abnormalities. Postmortem fetal examination remains valuable after pregnancy loss; classic LCCS1 may show profound anterior-horn and skeletal-muscle atrophy despite a macroscopically normal brain. (nousiainen2011molecularbackgroundofa pages 24-26, potrony2022lethalcongenitalcontracture pages 1-2)

In liveborn infants, useful tests include blood chemistry and creatine kinase, echocardiography, renal imaging, brain/spinal MRI, EMG and nerve-conduction studies, swallow/respiratory evaluation, and selected muscle/nerve biopsy. These tests characterize the affected compartment but are not individually diagnostic. ADCY6 disease may show chronic neurogenic EMG/biopsy abnormalities; CNTNAP1 disease can produce motor conduction below 10 m/s. (laquerriere2014mutationsincntnap1 pages 1-2, agolini2020expandingtheclinical pages 1-6)

### Genetic-testing algorithm

1. Confirm fetal akinesia/AMC phenotype and construct a three-generation pedigree.
2. Perform karyotype or chromosomal microarray when structural anomalies are present.
3. Use rapid **trio WES or WGS**, preferably with CNV and splice-aware analysis. A comprehensive fetal-akinesia/arthrogryposis panel should include the established LCCS genes plus broader motor-neuron, peripheral-nerve, neuromuscular-junction, myopathy, skeletal-dysplasia, and congenital-glycosylation genes.
4. Confirm candidate variants and phase by Sanger sequencing or orthogonal methods; apply ACMG/AMP classification and phenotype segregation.
5. Reanalyze negative exomes and consider genome/RNA sequencing where a splice, structural, deep-intronic, or poorly covered variant is suspected.

WES has achieved diagnostic rates up to approximately **60% in arthrogryposis cohorts**, although this is not an LCCS-specific sensitivity. In recurrent fetal structural anomalies, a separate meta-analysis reported a 40% incremental exome yield, illustrating the utility of trio sequencing in comparable prenatal settings. (potrony2022lethalcongenitalcontracture pages 1-2)

### Differential diagnosis

Major alternatives include SMN1-related SMA, congenital myopathies and muscular dystrophies, congenital myasthenic syndromes, CNTN1/NFASC nodopathies, multiple-pterygium syndromes, cerebro-oculo-facio-skeletal disorders, skeletal dysplasias, chromosomal disease, mitochondrial disorders, congenital infection, maternal myasthenia/antibody-mediated fetal akinesia, oligohydramnios, uterine constraint, and teratogen exposure. Recent sequencing continues to expand the differential: biallelic **KIF21A** loss of function was identified in severe fetal akinesia with arthrogryposis and pulmonary hypoplasia in a 2023 study. (falb2023bialleliclossoffunctionvariants pages 9-9, illes2024heterogenicgeneticbackground pages 1-2)

## 11. Outcome and prognosis

Mortality is driven principally by pulmonary hypoplasia, respiratory muscle/diaphragm dysfunction, aspiration, and infection. Classic LCCS1 is usually prenatally lethal; LCCS2 is generally fatal shortly after birth; reported PIP5K1C LCCS3 patients died from respiratory insufficiency. ADCY6 cases died from infancy to 36 months in the available series. (trabacca2024updateoninherited pages 11-12, zhang2024novelpip5k1cvariant pages 2-5, agolini2020expandingtheclinical pages 1-6)

GLDN disease demonstrates why genotype-specific counseling is essential. Wambach et al. reported six patients from four families, of whom **four survived beyond the neonatal period into infancy, childhood, or late adolescence** with intensive care and chronic respiratory/nutritional support. Thus, there are no defensible universal 5- or 10-year survival estimates, and “lethal” should not be interpreted as invariant neonatal death. (wambach2017survivalamongchildren pages 1-3)

No validated prognostic biomarker exists. Likely clinical predictors include severity of fetal akinesia, pulmonary hypoplasia, autonomous respiratory capacity, swallowing ability, extent of denervation/hypomyelination, and the residual function of the causal allele.

## 12. Treatment and current applications

There is **no approved disease-modifying pharmacotherapy, gene therapy, cell therapy, RNA therapy, or genotype-directed drug** for LCCS, and the ClinicalTrials.gov search identified no relevant LCCS interventional trial. A 2024 pediatric motor-neuron review likewise reported no disease-modifying treatment for congenital SMA/arthrogryposis conditions. (trabacca2024updateoninherited pages 11-12)

Management is supportive and individualized:

- neonatal resuscitation and invasive/noninvasive ventilation;
- tracheostomy, airway-clearance/cough-assist, sleep and gas-exchange monitoring;
- swallow assessment, aspiration prevention, nasogastric or gastrostomy feeding;
- physical and occupational therapy, splinting, positioning, and contracture management;
- orthopedic surgery only when expected benefits exceed anesthetic and respiratory risks;
- treatment of hydrocephalus, cardiac, renal, gastrointestinal, and infectious complications;
- palliative-care involvement for uniformly severe prenatal/neonatal presentations.

Suggested NCIt intervention concepts include **Mechanical Ventilation**, **Tracheostomy**, **Gastrostomy**, **Physical Therapy**, **Occupational Therapy**, **Orthopedic Surgery**, **Genetic Counseling**, and **Palliative Care**. GLDN and ADCY6 survivor reports provide real-world evidence for chronic ventilation, gastrostomy, rehabilitation, and multidisciplinary follow-up rather than molecular therapy. (mis2020thelatestfads pages 1-2, wambach2017survivalamongchildren pages 1-3, agolini2020expandingtheclinical pages 1-6)

## 13. Prevention

There is no vaccine, lifestyle intervention, environmental remediation, or prophylactic drug that prevents a pathogenic biallelic genotype. Prevention is reproductive:

- cascade carrier testing after a molecular diagnosis;
- ancestry- or family-history-informed preconception carrier screening;
- partner testing;
- preimplantation genetic testing for monogenic disease;
- targeted chorionic-villus or amniotic-fluid testing;
- early expert ultrasound and, where appropriate, rapid prenatal trio sequencing.

For a known familial genotype, targeted molecular testing is more definitive than ultrasound, because fetal movement abnormalities may emerge after the optimal window for reproductive decision-making. Genetic counseling should address the 25% recurrence risk, variable survival in some subtypes, reproductive options, and residual risks including assay limitations.

## 14. Other species and natural disease

No well-established naturally occurring veterinary counterpart or zoonotic transmission was identified. The relevant proteins and developmental processes are evolutionarily conserved, but most comparative evidence comes from induced laboratory models rather than natural disease. Suggested taxa include **Mus musculus** (NCBI Taxon 10090) and **Danio rerio** (7955).

## 15. Model organisms and experimental systems

- **CNTNAP1/ADCY6 zebrafish knockdown:** morpholino experiments were used in the original human genetics study to support developmental neuromuscular effects. Limitations include transient knockdown and imperfect equivalence to human biallelic alleles. (laquerriere2014mutationsincntnap1 pages 1-2)
- **Pip5k1c-null mouse:** reduced brain PIP2 by approximately 50% and impaired nerve-terminal PIP2 synthesis/synaptic function, supporting phosphoinositide and presynaptic mechanisms. The model is useful mechanistically but does not by itself establish every human fetal phenotype. (zhang2024novelpip5k1cvariant pages 2-5)
- **Nek9 models:** homozygous knockout is embryonic lethal. LIR-mutant mice show impaired kidney ciliogenesis; cultured mutant cells accumulate MYH9, and MYH9 depletion rescues ciliogenesis. These models distinguish NEK9’s autophagy/ciliary role but do not fully reproduce human contracture syndrome. (yamamoto2021nek9regulatesprimary pages 1-2)
- **Patient fibroblasts:** NEK9 LCCS10 fibroblasts have shown defective primary-cilium formation. (yamamoto2021nek9regulatesprimary pages 1-2)
- **GLDN variant assays:** functional testing of p.Leu365Phe, p.Arg393Lys, and other patient variants strengthens pathogenic classification and nodal-mechanism inference. (mis2020thelatestfads pages 1-2)

No validated LCCS organoid, iPSC-derived neuromuscular-junction platform, or therapeutic CRISPR screen was identified in the 2023–2024 evidence set.

## Recent developments and expert assessment, 2023–2024

1. **PIP5K1C/LCCS3 expansion (published March 2024):** two affected Chinese fetuses increased the detailed published count from five to seven. The study added pathogenic c.949_952dup (p.S318Ifs*28), documented compound heterozygosity with c.688_689del, and proposed ventriculomegaly as a possible but unconfirmed phenotype. DOI: https://doi.org/10.1186/s12887-024-04674-6. The authors’ abstract states: “These findings expanded the genetic variant spectrum of PIP5K1C and enriched the clinical features of LCCS3.” (zhang2024novelpip5k1cvariant pages 1-2, zhang2024novelpip5k1cvariant pages 2-5)
2. **NEK9 phenotype expansion (published 4 January 2023):** two premature neonates carried three novel truncating alleles, broadening NEK9 disease beyond a uniformly lethal fetal skeletal phenotype. DOI: https://doi.org/10.3389/fgene.2022.989215. The abstract concludes that “different types of mutations in NEK9 lead to different phenotypes.” (liu2023novelvariantsof pages 1-2, liu2023novelvariantsof pages 2-5)
3. **Broader fetal-akinesia gene discovery (2023):** biallelic KIF21A loss of function was reported in five fetuses from two families with severe neurogenic fetal akinesia, arthrogryposis, pulmonary hypoplasia, and facial dysmorphism. DOI: https://doi.org/10.1136/jmedgenet-2021-108064. This reinforces expert recommendations for broad trio-exome/genome analysis rather than narrow sequential single-gene testing. (falb2023bialleliclossoffunctionvariants pages 9-9)
4. **Current expert interpretation (October 2024):** inherited pediatric motor-neuron disease remains genetically heterogeneous, with LCCS1 viewed as a severe GLE1-related RNA-metabolism/anterior-horn disease and LCCS2 as ERBB3-related multisystem fetal akinesia. Evidence remains dominated by case reports, and no disease-modifying therapy is available. DOI: https://doi.org/10.3390/genes15101346. (trabacca2024updateoninherited pages 11-12)

## Evidence limitations

The LCCS literature consists mainly of very small, ancestry-enriched families, fetal pathology series, and survivor case reports. Consequently, phenotype percentages, penetrance, allele frequencies, incidence, survival curves, quality-of-life scores, treatment-response rates, and genotype–phenotype correlations are generally unavailable or unstable. Several older subtype assignments and identifiers vary across secondary sources. Database ingestion should therefore retain **gene and OMIM subtype provenance**, publication date, evidence type (human/model/in vitro), and uncertainty rather than treating “LCCS” as one homogeneous disorder.

References

1. (potrony2022lethalcongenitalcontracture pages 1-2): Miriam Potrony, Antoni Borrell, Narcís Masoller, Alfons Nadal, Leonardo Rodriguez-Carunchio, Karmele Saez de Gordoa Elizalde, Juan Francisco Quesada-Espinosa, Jose Luis Villanueva-Cañas, Montse Pauta, Meritxell Jodar, Irene Madrigal, Celia Badenas, Maria Isabel Alvarez-Mora, and Laia Rodriguez-Revenga. Lethal congenital contracture syndrome 11: a case report and literature review. Journal of Clinical Medicine, 11:3570, Jun 2022. URL: https://doi.org/10.3390/jcm11133570, doi:10.3390/jcm11133570. This article has 7 citations.

2. (wambach2017survivalamongchildren pages 1-3): Jennifer A. Wambach, Georg M. Stettner, Tobias B. Haack, Karin Writzl, Andreja Škofljanec, Aleš Maver, Francina Munell, Stephan Ossowski, Mattia Bosio, Daniel J. Wegner, Marwan Shinawi, Dustin Baldridge, Bader Alhaddad, Tim M. Strom, Dorothy K. Grange, Ekkehard Wilichowski, Robin Troxell, James Collins, Barbara B. Warner, Robert E. Schmidt, Alan Pestronk, F. Sessions Cole, and Robert Steinfeld. Survival among children with “lethal” congenital contracture syndrome 11 caused by novel mutations in the gliomedin gene (gldn). Human Mutation, 38:1477-1484, Nov 2017. URL: https://doi.org/10.1002/humu.23297, doi:10.1002/humu.23297. This article has 24 citations and is from a domain leading peer-reviewed journal.

3. (beecroft2018geneticsofneuromuscular pages 3-4): Sarah Jane Beecroft, Marcus Lombard, David Mowat, Catriona McLean, Anita Cairns, Mark Davis, Nigel G Laing, and Gianina Ravenscroft. Genetics of neuromuscular fetal akinesia in the genomics era. Journal of Medical Genetics, 55:505-514, Jun 2018. URL: https://doi.org/10.1136/jmedgenet-2018-105266, doi:10.1136/jmedgenet-2018-105266. This article has 50 citations and is from a domain leading peer-reviewed journal.

4. (trabacca2024updateoninherited pages 11-12): Antonio Trabacca, Camilla Ferrante, Maria Carmela Oliva, Isabella Fanizza, Ivana Gallo, and Marta De Rinaldis. Update on inherited pediatric motor neuron diseases: clinical features and outcome. Oct 2024. URL: https://doi.org/10.3390/genes15101346, doi:10.3390/genes15101346. This article has 12 citations.

5. (nousiainen2011molecularbackgroundofa pages 24-26): H Nousiainen. Molecular background of three lethal fetal syndromes. Unknown journal, 2011.

6. (zhang2024novelpip5k1cvariant pages 1-2): Fang Zhang, Hongmei Guo, Xinlong Zhou, Zhengxi Deng, Qiuhong Xu, Qingming Wang, Haiming Yuan, and Jianhua Luo. Novel pip5k1c variant identified in a chinese pedigree with lethal congenital contractural syndrome 3. BMC Pediatrics, Mar 2024. URL: https://doi.org/10.1186/s12887-024-04674-6, doi:10.1186/s12887-024-04674-6. This article has 3 citations and is from a peer-reviewed journal.

7. (zhang2024novelpip5k1cvariant pages 2-5): Fang Zhang, Hongmei Guo, Xinlong Zhou, Zhengxi Deng, Qiuhong Xu, Qingming Wang, Haiming Yuan, and Jianhua Luo. Novel pip5k1c variant identified in a chinese pedigree with lethal congenital contractural syndrome 3. BMC Pediatrics, Mar 2024. URL: https://doi.org/10.1186/s12887-024-04674-6, doi:10.1186/s12887-024-04674-6. This article has 3 citations and is from a peer-reviewed journal.

8. (beecroft2018geneticsofneuromuscular pages 3-3): Sarah Jane Beecroft, Marcus Lombard, David Mowat, Catriona McLean, Anita Cairns, Mark Davis, Nigel G Laing, and Gianina Ravenscroft. Genetics of neuromuscular fetal akinesia in the genomics era. Journal of Medical Genetics, 55:505-514, Jun 2018. URL: https://doi.org/10.1136/jmedgenet-2018-105266, doi:10.1136/jmedgenet-2018-105266. This article has 50 citations and is from a domain leading peer-reviewed journal.

9. (laquerriere2014mutationsincntnap1 pages 1-2): A. Laquérriere, J. Maluenda, Adrien Camus, Laura Fontenas, K. Dieterich, F. Nolent, Jie Zhou, N. Monnier, P. Latour, D. Gentil, D. Heron, I. Desguerres, P. Landrieu, C. Bénéteau, Benoit Delaporte, C. Bellesme, C. Baumann, Y. Capri, A. Goldenberg, S. Lyonnet, D. Bonneau, B. Estournet, S. Quijano-roy, C. Francannet, S. Odent, Marie-Hélène Saint-Frison, S. Sigaudy, D. Figarella-Branger, A. Gelot, J. Mussini, C. Lacroix, V. Drouin‐Garraud, M. Malinge, T. Attié-Bitach, B. Bessières, M. Bonnière, F. Encha-Razavi, A. Beaufrère, S. Khung-Savatovsky, M. Perez, A. Vasiljevic, S. Mercier, J. Roume, L. Trestard, P. Saugier-Veber, M. Cordier, V. Layet, M. Legendre, A. Vigouroux-Castera, J. Lunardi, M. Bayés, P. Jouk, L. Rigonnot, M. Granier, D. Sternberg, J. Warszawski, I. Gut, M. Gonzalès, Marcel Tawk, and J. Melki. Mutations in cntnap1 and adcy6 are responsible for severe arthrogryposis multiplex congenita with axoglial defects. Human molecular genetics, 23 9:2279-89, May 2014. URL: https://doi.org/10.1093/hmg/ddt618, doi:10.1093/hmg/ddt618. This article has 135 citations and is from a domain leading peer-reviewed journal.

10. (agolini2020expandingtheclinical pages 1-6): Emanuele Agolini, Claudio Cherchi, Emanuele Bellacchio, Diego Martinelli, Dario Cocciadiferro, Renato Cutrera, Maria B. Chiarini Testa, Chiara Barone, Sebastiano Bianca, and Antonio Novelli. Expanding the clinical and molecular spectrum of lethal congenital contracture syndrome 8 associated with biallelic variants <i>of adcy6</i>. Feb 2020. URL: https://doi.org/10.1111/cge.13691, doi:10.1111/cge.13691. This article has 11 citations and is from a peer-reviewed journal.

11. (liu2023novelvariantsof pages 1-2): Fang Liu, Liying Dai, Zhi Li, and Xiaowei Yin’s. Novel variants of nek9 associated with neonatal arthrogryposis: two case reports and a literature review. Frontiers in Genetics, Jan 2023. URL: https://doi.org/10.3389/fgene.2022.989215, doi:10.3389/fgene.2022.989215. This article has 4 citations and is from a peer-reviewed journal.

12. (yamamoto2021nek9regulatesprimary pages 1-2): Yasuhiro Yamamoto, Haruka Chino, Satoshi Tsukamoto, Koji L. Ode, Hiroki R. Ueda, and Noboru Mizushima. Nek9 regulates primary cilia formation by acting as a selective autophagy adaptor for myh9/myosin iia. Nature Communications, Jun 2021. URL: https://doi.org/10.1038/s41467-021-23599-7, doi:10.1038/s41467-021-23599-7. This article has 65 citations and is from a highest quality peer-reviewed journal.

13. (liu2023novelvariantsof pages 2-5): Fang Liu, Liying Dai, Zhi Li, and Xiaowei Yin’s. Novel variants of nek9 associated with neonatal arthrogryposis: two case reports and a literature review. Frontiers in Genetics, Jan 2023. URL: https://doi.org/10.3389/fgene.2022.989215, doi:10.3389/fgene.2022.989215. This article has 4 citations and is from a peer-reviewed journal.

14. (mis2020thelatestfads pages 1-2): Emily K. Mis, Samir Al‐Ali, Weizhen Ji, Michele Spencer‐Manzon, Monica Konstantino, Mustafa K. Khokha, Lauren Jeffries, and Saquib A. Lakhani. The latest fads: functional analysis of gldn patient variants and classification of gldn‐associated amc as a type of viable fetal akinesia deformation sequence. American Journal of Medical Genetics Part A, 182:2291-2296, Aug 2020. URL: https://doi.org/10.1002/ajmg.a.61783, doi:10.1002/ajmg.a.61783. This article has 9 citations.

15. (choi2024globalcarrierfrequency pages 6-8): Won-Jun Choi, Soo-Hyun Kim, Sung Rok Lee, Seung-Hun Oh, Seung Woo Kim, Ha Young Shin, and Hyung Jun Park. Global carrier frequency and predicted genetic prevalence of patients with pathogenic sequence variants in autosomal recessive genetic neuromuscular diseases. Scientific Reports, Feb 2024. URL: https://doi.org/10.1038/s41598-024-54413-1, doi:10.1038/s41598-024-54413-1. This article has 11 citations and is from a peer-reviewed journal.

16. (illes2024heterogenicgeneticbackground pages 1-2): Anett Illés, Henriett Pikó, Virág Bartek, Olívia Szepesi, Gábor Rudas, Zsófia Benkő, Ágnes Harmath, János Pál Kósa, and Artúr Beke. Heterogenic genetic background of distal arthrogryposis—review of the literature and case report. Jul 2024. URL: https://doi.org/10.3390/children11070861, doi:10.3390/children11070861. This article has 5 citations.

17. (falb2023bialleliclossoffunctionvariants pages 9-9): Ruth J Falb, Amelie J Müller, Wolfram Klein, Mona Grimmel, Ute Grasshoff, Stephanie Spranger, Petra Stöbe, Darja Gauck, Alma Kuechler, Nicola Dikow, Eva M C Schwaibold, Christoph Schmidt, Luisa Averdunk, Rebecca Buchert, Tilman Heinrich, Natalia Prodan, Joohyun Park, Martin Kehrer, Marc Sturm, Olga Kelemen, Silke Hartmann, Denise Horn, Dirk Emmerich, Nina Hirt, Armin Neumann, Glen Kristiansen, Ulrich Gembruch, Susanne Haen, Reiner Siebert, Sabine Hentze, Markus Hoopmann, Stephan Ossowski, Stephan Waldmüller, Stefanie Beck-Wödl, Dieter Gläser, Ismail Tekesin, Felix Distelmaier, Olaf Riess, Karl-Oliver Kagan, Andreas Dufke, and Tobias B Haack. Bi-allelic loss-of-function variants in kif21a cause severe fetal akinesia with arthrogryposis multiplex. Journal of Medical Genetics, 60:48-56, Nov 2023. URL: https://doi.org/10.1136/jmedgenet-2021-108064, doi:10.1136/jmedgenet-2021-108064. This article has 48 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Lethal_Congenital_Contracture_Syndrome-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 9 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `DOI:10.1038/s41467-021-23599-7` (3 mentions) - NEK9 regulates primary cilia formation by acting as a selective autophagy adaptor for MYH9/myosin IIA
  - shared terms: none

Weighed against this report's own most characteristic terms: `disease`, `fetal`, `gene`, `clinical`, `genetic`, `include`, `variant`, `contracture`, `type`, `arthrogryposis`, `congenital`, `molecular`, `akinesia`, `affected`, `function`, `severe`, `lethal`, `respiratory`, `patient`, `lccs`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 32 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 6 |
| Terms named correctly | 3 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 3 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `GO:0006413` (1 mention) - the report calls it "translation initiation"; GO calls it **translational initiation**, and lists "translation initiation" among its other names
- `GO:0006415` (1 mention) - the report calls it "translation termination"; GO calls it **translational termination**, and lists "translation termination" among its other names
- `GO:0021675` (1 mention) - the report calls it "motor neuron development"; GO calls it **nerve development**

Every term resolved, and every label the report gave matched.