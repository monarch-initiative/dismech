---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-28T19:02:20.462478'
end_time: '2026-08-28T19:11:23.017695'
duration_seconds: 542.56
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: combined immunodeficiency due to CD3gamma deficiency (CD3G deficiency,
    immunodeficiency 17)
  mondo_id: MONDO:0014276
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
  on_topic: 2
  validator_version: 0.2.1
term_validation:
  total_terms: 55
  verified: 55
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0014276
    reported_labels:
    - if available
    ontology_label: combined immunodeficiency due to CD3gamma deficiency
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Combined_Immunodeficiency_Due_To_CD3gamma_Deficiency-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** combined immunodeficiency due to CD3gamma deficiency (CD3G deficiency, immunodeficiency 17)
- **MONDO ID:** MONDO:0014276 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **combined immunodeficiency due to CD3gamma deficiency (CD3G deficiency, immunodeficiency 17)** covering all of the
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
- **Disease Name:** combined immunodeficiency due to CD3gamma deficiency (CD3G deficiency, immunodeficiency 17)
- **MONDO ID:** MONDO:0014276 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **combined immunodeficiency due to CD3gamma deficiency (CD3G deficiency, immunodeficiency 17)** covering all of the
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


# Combined immunodeficiency due to CD3γ deficiency

## Executive summary

**Combined immunodeficiency due to CD3γ deficiency** is an ultrarare, autosomal-recessive inborn error of immunity caused by biallelic loss-of-function variants in **CD3G**, encoding the γ chain of the T-cell receptor (TCR)–CD3 complex. Unlike complete CD3δ or CD3ε deficiency, it usually permits development of circulating, polyclonal T cells. These cells nevertheless express markedly less surface TCR/CD3, signal and proliferate inefficiently, and have abnormal repertoire selection. The resulting phenotype ranges from apparently isolated autoimmunity or adult CVID-like antibody deficiency to severe childhood combined immunodeficiency (CID) with opportunistic infection, enteropathy, and transplant requirement. Autoimmune thyroiditis, autoimmune cytopenias, and inflammatory bowel disease–like enteropathy are especially characteristic. Human evidence remains limited to small families and case reports; therefore, frequencies below are descriptive rather than population estimates. (rowe2018patientswithcd3g pages 9-13, rowe2018patientswithcd3g pages 1-6, rowe2018patientswithcd3g pages 6-9)

| domain | established finding | quantitative/patient evidence | evidence type | ontology suggestions |
|---|---|---|---|---|
| Gene / inheritance | CD3G deficiency is an ultrarare autosomal-recessive inborn error of immunity caused by biallelic CD3G variants; disease spectrum spans combined immunodeficiency with immune dysregulation rather than uniformly classic SCID. | 2019 review found 10 reported cases from 5 unrelated families; 2021 report noted 14 previously reported cases; later 2026 synthesis reported 18 total patients and explicitly called the disorder autosomal recessive (later than requested 2023-2024 window) (lee2019anovelcd3g pages 1-2, delmonte2021completeabsenceof pages 1-3, obeng2026expandingtheclinical pages 1-2) | Human case series/review | MONDO:0014276; CD3G (HGNC gene); HP:0000007 Autosomal recessive inheritance; NCIT: Inborn Error of Immunity |
| TCR-CD3 mechanism | CD3γ is required for optimal surface expression of the TCR/CD3 complex; deficiency lowers CD3ε and TCRαβ expression and weakens TCR signaling without abolishing polyclonal T-cell development in humans. | In 6 bi-allelic cases, all showed markedly reduced CD3ε/TCRαβ on T cells and impaired proliferation to PHA; anti-CD3/CD28 partly restored responses (rowe2018patientswithcd3g pages 6-9). Later 2026 cases also had reduced TCR/CD3 expression despite normal T-cell counts (obeng2026expandingtheclinical pages 5-6) | Human functional immunology | GO:0050852 T cell receptor signaling pathway; GO:0042102 positive regulation of T cell proliferation; CL:0000624 CD4-positive, alpha-beta T cell; CL:0000625 CD8-positive, alpha-beta T cell |
| Infections | Clinical infectious susceptibility is variable, from recurrent sinopulmonary infections to severe/opportunistic infections. | 2019 analysis: infections in 7 patients; 4/5 with sinopulmonary infections developed bronchiectasis; reported opportunistic infections included Candida, Giardia, and severe EBV; one patient had pneumonia by 6-9 months and EBV viremia 102,000 copies/mL (lee2019anovelcd3g pages 4-6, delmonte2021completeabsenceof pages 1-3) | Human case reports/review | HP:0002719 Recurrent infections; HP:0012735 Recurrent respiratory infections; HP:0002110 Bronchiectasis; NCBITaxon:10376 Epstein-Barr virus |
| Autoimmunity / immune dysregulation | Autoimmunity is a major and often dominant manifestation; autoimmune cytopenias, thyroiditis, enteropathy/IBD-like disease, vitiligo, hepatitis, and Evans syndrome are reported. | In one 2014 family series, 5/5 had autoimmune thyroiditis, 2/5 autoimmune hemolytic anemia, 1/5 immune thrombocytopenia, 1/5 autoimmune hepatitis, 1/5 vitiligo (gokturk2014cd3ggenedefects pages 1-2). In the 2018 cohort, all 6 patients had autoimmunity (rowe2018patientswithcd3g pages 6-9). Later 2026 adult cases highlighted Evans syndrome responsive to rituximab (later than requested window) (obeng2026expandingtheclinical pages 1-2) | Human case series | HP:0002716 Autoimmunity; HP:0001890 Autoimmune hemolytic anemia; HP:0001973 Autoimmune thrombocytopenia; HP:0000824 Autoimmune thyroiditis; HP:0002037 Inflammatory bowel disease; HP:0005603 Vitiligo |
| Laboratory phenotype | Typical immunophenotype includes reduced TCR/CD3 surface expression, reduced naïve T cells, variable CD4/CD8 lymphopenia, hypogammaglobulinemia, impaired vaccine responses, reduced switched memory B cells, and sometimes high IgE. | 2014 series: all 5 had low CD3+TCRαβ+ percentages; only 1 had overall lymphopenia; 3 had CD3+ T-cell lymphopenia; 3/5 had high IgE; 3/5 had ANA positivity (gokturk2014cd3ggenedefects pages 1-2). 2021 case: CD4 count 627/µL, IgG 338 mg/dL, impaired vaccination responses (delmonte2021completeabsenceof pages 1-3). 2019 case had decreased switched memory B cells and diminished CD40L expression (lee2019anovelcd3g pages 1-2) | Human laboratory/clinical | HP:0005403 Decreased alpha-beta T-cell count; HP:0002841 Hypogammaglobulinemia; HP:0010976 Reduced memory B-cell count; HP:0002910 Elevated IgE level; HP:0002720 Impaired vaccine response |
| Treg / tolerance mechanism | A leading mechanism of immune dysregulation is defective regulatory T-cell biology: reduced Treg proportion/diversity, restricted TCR repertoire, impaired suppressive function, and enrichment of self-reactive conventional T cells. | In the 2018 study, Treg cells from CD3G-mutated patients failed to suppress Teff proliferation at 1:2 ratios and showed reduced suppression at 1:1 ratios; 6 patients showed repertoire restriction and self-reactivity signatures (rowe2018patientswithcd3g pages 9-13, rowe2018patientswithcd3g pages 13-18) | Human mechanistic study | GO:0002507 tolerance induction; GO:0043029 T cell homeostasis; CL:0000815 regulatory T cell; HP:0002960 Autoimmune disease |
| B-cell / humoral involvement | Some patients show a CVID-like or predominant humoral phenotype, indicating downstream B-cell dysfunction despite the primary T-cell signaling defect. | 2019 Taiwanese adult case had recurrent sinopulmonary infections, hypogammaglobulinemia, decreased switched memory B cells, diminished CD40L expression, and 20 years of immunoglobulin replacement, yet no overt autoimmunity (lee2019anovelcd3g pages 1-2, lee2019anovelcd3g pages 2-3, lee2019anovelcd3g pages 4-6) | Human case report | HP:0002721 Immunoglobulin deficiency; HP:0010976 Reduced memory B-cell count; NCIT: Common Variable Immunodeficiency-like phenotype |
| Diagnosis | Diagnosis relies on clinical suspicion for CID/immune dysregulation plus flow cytometry showing reduced TCR/CD3 expression and confirmatory sequencing (targeted NGS, WES, or WGS). | 2024 Algerian flow-cytometry experience reported CD3γ deficiency diagnosed in 2 siblings presenting with recurrent infections; the paper emphasized FCM as a direct or highly informative IEI diagnostic tool (paper search summary). 2024 WES study from Türkiye supports molecular diagnosis in IEI cohorts though not CD3G-specific in the excerpt (obeng2026expandingtheclinical pages 5-6) | Human diagnostic practice / cohort | NCIT: Flow Cytometry; NCIT: Whole Exome Sequencing; NCIT: Whole Genome Sequencing; NCIT: Genetic Testing |
| Treatment | Management is individualized and case-based: immunoglobulin replacement, prophylactic/therapeutic antimicrobials, steroids, rituximab, sirolimus, and HSCT in severe cases. | 2019 patient received IVIG for ~20 years plus antibiotics/steroids (lee2019anovelcd3g pages 2-3). 2021 patient received immunoglobulin replacement, antibiotics, rituximab, sirolimus, steroids (delmonte2021completeabsenceof pages 1-3). Severe life-threatening infections requiring HSCT were associated with worse outcomes in 2019 analysis (lee2019anovelcd3g pages 1-2) | Human case reports/review | NCIT:C80687 Immunoglobulin Therapy; NCIT:C15543 Anti-Infective Therapy; NCIT:C1802 Rituximab; NCIT:C29457 Sirolimus; NCIT:C15206 Hematopoietic Stem Cell Transplantation |
| Prognosis | Prognosis is highly variable, from isolated autoimmune thyroiditis to fatal infantile disease; severe infections, opportunistic infections, IBD-like disease, and HSCT-related complications drive poorer outcomes. | 2019 review reported 3 deaths: severe infection at 31 months, post-transplant viral pneumonia at 17 months, and graft-versus-host disease at 47 months; worse prognosis associated with opportunistic infections (p=0.0124), severe life-threatening infections needing HSCT (p=0.01), and IBD-like diarrhea (p=0.0124); autoimmune thyroiditis associated with better prognosis (p=0.0124) (lee2019anovelcd3g pages 1-2, lee2019anovelcd3g pages 4-6) | Human case aggregation | HP:0003819 Death in infancy; HP:0006538 Chronic course; HP:0002583 Chronic diarrhea; NCIT: Prognosis |
| Epidemiology limits | No robust population prevalence, incidence, carrier-frequency, penetrance, or sex-ratio estimates were identified; evidence remains almost entirely from published families/case reports. | Disease totals in the literature remained in the low double digits across reports (10, 14, then 18 in later 2026 synthesis) (lee2019anovelcd3g pages 1-2, delmonte2021completeabsenceof pages 1-3, obeng2026expandingtheclinical pages 1-2) | Evidence-gap statement from literature scope | NCIT: Rare Disease; MONDO:0014276 |
| Environmental / infectious modifiers | No disease-specific environmental or lifestyle risk factors were identified; infectious exposures act mainly as complications or triggers that reveal the immune defect. | Reported pathogens/complications include H. influenzae, Pseudomonas aeruginosa, S. aureus cellulitis, E. coli epididymoorchitis, EBV viremia, Candida, Giardia, and H. pylori-associated gastric MALT lymphoma in a later 2026 report (later than requested window) (lee2019anovelcd3g pages 2-3, obeng2026expandingtheclinical pages 5-6) | Human case reports | NCBITaxon:727 Haemophilus influenzae; NCBITaxon:287 Pseudomonas aeruginosa; NCBITaxon:1280 Staphylococcus aureus; NCBITaxon:562 Escherichia coli; NCBITaxon:210 Helicobacter pylori |
| Model-organism limitations | Mouse CD3-chain knockout biology does not fully recapitulate human disease; no single CD3 subunit is absolutely required for murine T-cell maturation, limiting direct translation from knockout models. Human-CD3 replacement mice are useful for therapeutic studies but are not disease models of CD3G deficiency. | Review evidence notes fundamental mouse-human differences in CD3 subunit requirements (grunebaum2006humantcell pages 5-7). Human CD3E/D/G-replaced mice are immune competent and were developed to test human CD3-directed therapeutics, not to model CD3G deficiency pathogenesis (paper search summary for Ueda 2017) | Comparative/model evidence | NCBITaxon:10090 Mus musculus; GO:0046649 lymphocyte activation; NCIT: Disease Model |


*Table: This table condenses the strongest gathered evidence on combined immunodeficiency due to CD3G deficiency across genetics, mechanism, phenotype, diagnosis, treatment, prognosis, and model limitations. It is designed for rapid knowledge-base ingestion and flags where later 2026 evidence falls outside the user's preferred 2023-2024 priority window.*

## 1. Disease information

### Definition and nomenclature

The preferred name is **combined immunodeficiency due to CD3γ deficiency**. Common alternatives are **CD3-gamma deficiency**, **CD3G deficiency**, **immunodeficiency 17**, **T-cell receptor complex deficiency due to CD3γ deficiency**, and, in some reports, **CD3γ-deficient CID**. “SCID due to CD3G deficiency” should be used cautiously: even complete absence of CD3γ has produced residual polyclonal T-cell development and CID with autoimmunity rather than uniform classic SCID. (delmonte2021completeabsenceof pages 1-3)

Recommended identifiers are:

- **MONDO:** MONDO:0014276, as supplied in the disease template.
- **OMIM phenotype:** Immunodeficiency 17, commonly catalogued as **IMD17/615607**; gene entry **CD3G/186740**. These database identifiers should be validated against the current OMIM release before automated ingestion.
- **Gene:** CD3G; NCBI reference transcript used in recent case aggregation: **NM_000073.3**.
- **Orphanet:** typically represented within rare combined T- and B-cell immunodeficiencies/TCR-complex deficiencies; a stable disease-specific ORPHA number was not established from the retrieved primary texts.
- **ICD-10:** no specific code; usually coded under **D81.8, Other combined immunodeficiencies** or an appropriate national modification.
- **ICD-11:** no confidently verified disease-specific code in the retrieved evidence; use the relevant combined-immunodeficiency category.
- **MeSH:** no disease-specific descriptor identified; useful broader headings include *Combined Immunodeficiencies*, *Primary Immunodeficiency Diseases*, and *T-Cell Receptor-CD3 Complex*.

The evidence is **aggregated disease-level evidence derived from published individual patients and families**, not population EHR data. The 2019 analysis included ten cases from five unrelated families, whereas the 2021 report referred to 14 previously reported cases—illustrating the small and evolving evidence base. (lee2019anovelcd3g pages 1-2, delmonte2021completeabsenceof pages 1-3, lee2019anovelcd3g pages 10-11)

## 2. Etiology, risk, and protective factors

### Causal factor

The primary cause is **germline biallelic pathogenic loss-of-function CD3G variation**. Reported classes include splice-site, start-loss/missense, nonsense, and frameshift/deletion variants. The 2019 aggregation counted 20 disease alleles: 14 c.80-1G>C splice alleles, two c.1G>A alleles, two reported nonsense alleles, and two c.213 deletion alleles. Nomenclature differed between publications, so all legacy calls should be remapped to a single transcript and genome build before database loading. (lee2019anovelcd3g pages 1-2)

Reported variants include **c.80-1G>C**, **c.1A>G/p.(Met1Val)**, **c.205A>T/p.(Lys69Ter)**, **c.213del/p.(Lys71fs)**, and later **c.213dup/p.(Trp72Metfs*6)**. The frameshift around residue 71–72 disrupts or removes the cytoplasmic immunoreceptor tyrosine-based activation motif and can abolish detectable CD3γ protein. (lee2019anovelcd3g pages 2-3, obeng2026expandingtheclinical pages 8-9, obeng2026expandingtheclinical pages 7-8)

### Risk factors

- **Genetic:** two pathogenic alleles are the established risk factor. Consanguinity has been common in reported families but is not required. Family history of childhood infections, autoimmunity, unexplained cytopenias, hypogammaglobulinemia, or early deaths should increase suspicion.
- **Environmental/lifestyle:** no toxin, diet, smoking, alcohol, occupational, sex-specific, or age-related causal risk factor has been demonstrated.
- **Infectious exposure:** infection does not cause the Mendelian disorder, but exposure reveals impaired immunity and can accelerate organ damage.
- **Modifiers:** striking intrafamilial variability with the same c.80-1G>C genotype implies genetic, epigenetic, microbial, treatment, or stochastic modifiers, but no modifier gene has been validated. (gokturk2014cd3ggenedefects pages 1-2)

No reproducible **protective genetic variant** is known. Early diagnosis, infection avoidance, antimicrobial prophylaxis where indicated, immunoglobulin replacement in antibody-deficient patients, and avoidance of unsafe live vaccines are clinically protective measures rather than etiologic protective factors.

## 3. Phenotypes

### Clinical and laboratory spectrum

| Phenotype | Character, onset/course, frequency evidence | Suggested HPO term |
|---|---|---|
| Recurrent respiratory infection | Childhood or adolescent onset is common, but severity is variable. Infections occurred in 7 patients in the 2019 aggregation. | HP:0012735 Recurrent respiratory infections |
| Bronchiectasis | Progressive structural complication: 4 of 5 patients with sinopulmonary infection developed bronchiectasis. It may cause exertional dyspnea, clubbing, hospitalization, and impaired quality of life. | HP:0002110 Bronchiectasis |
| Opportunistic/severe infection | Candida, Giardia, severe EBV, viral pneumonia, and life-threatening bacterial disease have occurred; associated with poor lymphocyte proliferation and higher mortality. | HP:0002719 Recurrent infections; HP:0002721 Immunodeficiency |
| Autoimmune thyroiditis | May be an isolated or predominant manifestation. Five of five patients in one familial series had thyroiditis; six cases were counted in the 2019 review. | HP:0000824 Autoimmune thyroiditis |
| Autoimmune cytopenia | AIHA, immune thrombocytopenia, pancytopenia, and Evans syndrome occur from early childhood through adulthood and may be episodic/relapsing. | HP:0001890 AIHA; HP:0001973 Autoimmune thrombocytopenia |
| Enteropathy/IBD-like disease | Chronic diarrhea, autoimmune enteropathy, gastritis/colitis, or fistulizing IBD-like disease; potentially severe and associated with worse prognosis. | HP:0002037 Inflammatory bowel disease; HP:0002014 Diarrhea |
| Other autoimmunity | Autoimmune hepatitis, nephrotic syndrome, vitiligo, positive ANA, and inflammatory lung disease have been reported. | HP:0002716 Autoimmunity; HP:0005603 Vitiligo |
| T-cell abnormality | Reduced surface CD3/TCRαβ, reduced naïve T cells, variable CD4/CD8 lymphopenia, memory/TEMRA skewing, and impaired mitogen response. | HP:0005403 Decreased alpha-beta T-cell count; HP:0031392 Abnormal lymphocyte proliferation |
| Humoral abnormality | Hypogammaglobulinemia, low IgG/IgG2, impaired vaccine/polysaccharide response, and reduced switched-memory B cells; sometimes a CVID-like presentation. | HP:0004313 Decreased circulating antibody level; HP:0002720 Impaired vaccine response |
| Atopy/high IgE | Atopic eczema and elevated IgE occurred in 3/5 patients in one familial series. | HP:0000964 Eczema; HP:0002910 Elevated IgE |

The underlying datasets are too small for reliable penetrance estimates. In the 2014 five-patient series, autoimmune thyroiditis occurred in 100%, AIHA in 40%, and thrombocytopenia, autoimmune hepatitis, nephrotic syndrome, and vitiligo in 20% each; 60% had high IgE/eczema and 60% ANA positivity. These are family-series proportions, not general population frequencies. (gokturk2014cd3ggenedefects pages 1-2)

The broader 2019 aggregation found autoimmunity in nine patients—thyroiditis in six, IBD-like diarrhea in four, and hemolytic anemia in four. Four of five patients with sinopulmonary infections had bronchiectasis. (lee2019anovelcd3g pages 4-6)

**Quality of life:** no CD3G-specific EQ-5D, SF-36, PROMIS, disability-weight, or formal patient-reported outcome study was found. Case-level burdens include repeated hospitalization, chronic IVIG and antibiotic treatment, exercise limitation, obstructive sleep apnea, clubbing, chronic diarrhea, immunosuppressive toxicity, and transplant morbidity. One adult had received immunoglobulin for approximately 20 years and developed bronchiectasis and portal-hypertensive nodular regenerative hyperplasia. (lee2019anovelcd3g pages 2-3)

## 4. Genetic and molecular information

**Causal gene:** **CD3G**, encoding CD3γ, a transmembrane component of the TCR-CD3 complex. Recommended gene annotation: HGNC-approved symbol CD3G; transcript **NM_000073.3**. Variants are germline, usually homozygous in reported consanguineous families; compound heterozygosity is biologically possible.

**Functional class:** available disease alleles act predominantly through loss of function—abnormal splicing, absent translation, truncation, loss of the cytoplasmic signaling domain, reduced protein, or complete protein absence. There is no established gain-of-function or dominant-negative CD3G deficiency mechanism. (lee2019anovelcd3g pages 4-6, obeng2026expandingtheclinical pages 5-6)

**Variant interpretation:** classifications should be obtained from the current ClinVar submission and reassessed under ACMG/AMP criteria. Strong applicable evidence may include a null variant in a loss-of-function disease mechanism, extreme rarity, segregation in affected relatives, reduced/absent protein, reduced surface TCR/CD3, and functional T-cell defects. No trustworthy gnomAD/TOPMed allele-frequency values were present in the retrieved primary texts; do not infer carrier frequency from the case literature.

**Genotype–phenotype relationship:** no robust correlation is established. Identical c.80-1G>C alleles produced isolated thyroid autoimmunity, broader autoimmune disease, infection susceptibility, or severe CID. One c.213-deletion patient retained normal Treg suppression and lacked autoimmunity despite a CVID-like phenotype, whereas other patients showed profound Treg dysfunction. (gokturk2014cd3ggenedefects pages 1-2, lee2019anovelcd3g pages 4-6)

No validated disease-specific modifier gene, methylation signature, histone abnormality, recurrent copy-number variant, translocation, inversion, aneuploidy, or somatic CD3G mechanism was identified.

## 5. Environmental and infectious information

No non-genetic exposure causes CD3G deficiency. Documented infectious complications include *Haemophilus influenzae*, *Pseudomonas aeruginosa*, *Staphylococcus aureus*, *Escherichia coli*, Candida, Giardia, and EBV. In the Taiwanese adult, chronic respiratory infection led to bronchiectasis despite prophylaxis; other infections included preseptal staphylococcal cellulitis and *E. coli* epididymo-orchitis. (lee2019anovelcd3g pages 4-6, lee2019anovelcd3g pages 2-3)

A 2021 patient had EBV viremia of **102,000 copies/mL**, enteropathy, inflammatory lung disease, and recurrent respiratory infection. (delmonte2021completeabsenceof pages 1-3) No disease-specific association with pollution, radiation, diet, exercise, smoking, or alcohol is reported.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic lesion:** biallelic CD3G loss of function reduces or eliminates CD3γ.
2. **Complex-level defect:** TCR/CD3 assembly, stability, and surface expression fall; CD3ε and TCRαβ are markedly reduced on CD4, CD8, and regulatory T cells.
3. **Signal defect:** antigen-receptor signal strength and proliferative responses decline. In six patients, PHA responses showed reduced CFSE dilution, CD25, and Ki-67; CD3/CD28 costimulation partially rescued activation.
4. **Development/selection defect:** some thymic T-cell development persists, but selection is distorted. Naïve cells are reduced, memory/exhausted populations expand, and the repertoire becomes restricted and clonally skewed.
5. **Tolerance defect:** Treg proportion and repertoire diversity may fall; Tregs can have severely impaired suppressive function. Conventional CD4 cells are enriched for hydrophobic CDR3 features associated with self-reactivity.
6. **Clinical outputs:** weak antimicrobial responses produce recurrent/severe infection; defective central and peripheral tolerance produces thyroiditis, cytopenias, enteropathy, and other autoimmunity; inadequate T-cell help contributes to hypogammaglobulinemia, poor vaccine response, and reduced switched-memory B cells. (rowe2018patientswithcd3g pages 9-13, rowe2018patientswithcd3g pages 13-18, rowe2018patientswithcd3g pages 6-9)

An informative functional result was that patient Tregs “**completely failed to suppress T effector cell proliferation at 1:2 ratios**,” with reduced suppression even at 1:1, directly supporting loss of peripheral tolerance. (rowe2018patientswithcd3g pages 9-13) Conversely, the Taiwanese c.213 deletion case retained normal FOXP3-positive Treg number and suppression, demonstrating that Treg failure is important but not obligatory. (lee2019anovelcd3g pages 4-6)

Suggested annotations:

- **GO biological process:** GO:0050852 T-cell receptor signaling pathway; GO:0031295 T-cell costimulation; GO:0042110 T-cell activation; GO:0042098 T-cell proliferation; GO:0002507 tolerance induction; GO:0043029 T-cell homeostasis.
- **GO cellular component:** T-cell receptor complex; plasma membrane; immunological synapse.
- **Cell Ontology:** CL:0000084 T cell; CL:0000624 CD4-positive αβ T cell; CL:0000625 CD8-positive αβ T cell; CL:0000815 regulatory T cell; CL:0000785 mature B cell.
- **Metabolic/tissue-damage mechanisms:** no primary metabolic defect is established. Bronchiectasis and inflammatory enteropathy are downstream consequences of repeated infection and immune dysregulation rather than intrinsic epithelial disease.

No disease-specific single-cell, spatial-transcriptomic, proteomic, metabolomic, lipidomic, CRISPR-screen, or integrated multi-omic signature was identified. TCR repertoire sequencing is the best developed molecular-profiling application. (rowe2018patientswithcd3g pages 1-6)

## 7. Anatomical structures affected

The **primary biological sites** are hematopoietic/lymphoid tissues, especially developing thymocytes and peripheral T cells. Suggested locations are thymus (UBERON:0002370), blood (UBERON:0000178), bone marrow (UBERON:0002371), lymph node (UBERON:0000029), and spleen (UBERON:0002106).

Secondary clinical injury affects bilateral airways/lungs through recurrent infection and bronchiectasis; intestine through autoimmune enteropathy/IBD-like inflammation; thyroid through autoimmune thyroiditis; blood through immune destruction of erythrocytes and platelets; and occasionally liver, kidney, skin, and interstitial lung. No intrinsic lateralization is expected. At the subcellular level, the critical compartment is the **plasma-membrane TCR-CD3 complex and immunological synapse**. (lee2019anovelcd3g pages 2-3, delmonte2021completeabsenceof pages 1-3)

## 8. Temporal development

The molecular defect is congenital, but clinical onset is highly variable. Severe cases present in infancy with pneumonia, diarrhea, candidiasis, or cytopenias; one detailed patient developed pneumonia at 6–9 months and severe AIHA at age two. Other patients first present during childhood, adolescence, or adulthood with thyroiditis, antibody deficiency, or autoimmune cytopenia. Median diagnosis in the five-patient 2014 series was **11 years**, range **14 months–20 years**. (gokturk2014cd3ggenedefects pages 1-2, delmonte2021completeabsenceof pages 1-3)

Untreated disease is chronic and potentially progressive, but may be episodic: infections accumulate structural lung damage, while autoimmune cytopenias relapse and remit. There is no validated staging system. Critical intervention windows are before irreversible bronchiectasis, severe opportunistic infection, chronic enteropathy, or transplant-compromising organ injury.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. For two carrier parents, each pregnancy has an expected 25% affected, 50% carrier, and 25% non-carrier/non-affected probability. Anticipation is not expected. Germline mosaicism has not been documented but cannot be categorically excluded.

Reliable prevalence, incidence, carrier frequency, penetrance, sex ratio, and geographic rate estimates do not exist. Published patients include Turkish, Spanish, Taiwanese/Chinese, and other families; Turkish enrichment partly reflects ascertainment and consanguinity rather than a demonstrated population prevalence. The 2019 review found seven Turkish and two Spanish earlier patients plus the Taiwanese case. (lee2019anovelcd3g pages 1-2)

Heterozygous relatives with autoimmunity were reported in one family investigation, but this does not establish dominant CD3G disease or carrier penetrance and may reflect familial background risk. (gokturk2014cd3ggenedefects pages 1-2)

## 10. Diagnostics

### Recommended diagnostic pathway

1. **Clinical suspicion:** recurrent/severe infection, bronchiectasis, chronic diarrhea, autoimmune cytopenia or thyroiditis—especially when multiple features coexist or there is consanguinity/family history.
2. **Baseline tests:** CBC/differential; quantitative IgG, IgA, IgM, IgE and IgG subclasses; vaccine antibody responses; EBV/CMV testing when indicated.
3. **Flow cytometry:** CD3, CD4, CD8, CD19, NK cells; naïve/memory subsets; switched-memory B cells; and, critically, compare **surface CD3ε and TCRαβ mean fluorescence intensity** with age-matched controls. Normal total T-cell numbers do not exclude CD3G deficiency.
4. **Functional assays:** PHA/ConA proliferation, anti-CD3 and anti-CD3/CD28 responses; CD25/Ki-67 induction. Treg number/function and TCR repertoire sequencing are valuable in complex immune-dysregulation cases.
5. **Molecular confirmation:** an IEI/CID panel containing CD3G or WES; deletion/duplication analysis if sequencing is negative. WGS is appropriate for unresolved cases, splice/regulatory lesions, or structural variants. Confirm variants by orthogonal testing and parental segregation.
6. **Protein/RNA validation:** Western blot for CD3γ and RNA studies for splice variants can establish functional consequence. (rowe2018patientswithcd3g pages 6-9, obeng2026expandingtheclinical pages 5-6, lee2019anovelcd3g pages 1-2)

A 2024 Algerian diagnostic cohort reported two siblings with CD3γ deficiency and illustrates the real-world value of flow cytometry in resource-constrained IEI diagnosis, although sequencing remains necessary for definitive genotype assignment. More broadly, a 2024 Turkish multicenter WES study obtained likely diagnoses in 122/297 evaluable IEI patients (**41.1%**), supporting exome sequencing when phenotypes overlap; this statistic is not CD3G-specific.

**Differential diagnosis:** CD3D/CD3E/CD247 deficiency; partial RAG1/RAG2 defects; ZAP70, LCK, LAT, TRAC, CORO1A, MHC-II, IL7R, JAK3, and IL2RG defects; CTLA4 or LRBA deficiency; activated PI3Kδ syndrome; autoimmune lymphoproliferative syndrome; common variable immunodeficiency; secondary immunodeficiency; HIV; and immunosuppressive drug effects. Profoundly reduced TCR/CD3 intensity with residual T cells and biallelic CD3G variants is distinguishing.

CMA, routine karyotype, FISH, mitochondrial sequencing, and repeat-expansion testing are not first-line unless another phenotype suggests them. Imaging is complication-directed—high-resolution chest CT for bronchiectasis/interstitial disease; endoscopy/biopsy for enteropathy; liver evaluation for portal hypertension. No standardized disease-specific clinical diagnostic criteria exist.

Newborn TREC screening may detect severe lymphopenic cases but can miss CD3G-deficient infants with near-normal T-cell counts. Thus, a normal TREC result does not exclude later CID/immune dysregulation.

## 11. Outcome and prognosis

No actuarial survival curve, five-/ten-year survival, mortality rate, or life-expectancy estimate exists. In the 2019 ten-case aggregation, **three deaths** occurred: severe infection at 31 months, post-HSCT respiratory failure from viral pneumonia at 17 months, and graft-versus-host disease at 47 months. Opportunistic infection, life-threatening infection requiring HSCT, and IBD-like diarrhea were associated with higher mortality (respectively p=0.0124, p=0.01, p=0.0124); thyroiditis was associated with better prognosis (p=0.0124). These exploratory p-values derive from extremely small numbers and should not be treated as validated prognostic models. (lee2019anovelcd3g pages 1-2, lee2019anovelcd3g pages 4-6)

Major morbidity comprises bronchiectasis, chronic enteropathy, recurrent cytopenia, chronic lung inflammation, organ toxicity from infection or immune suppression, and HSCT complications. Favorable factors likely include preserved proliferation/Treg function, absence of opportunistic infection, early IVIG where indicated, infection control, and treatment before irreversible organ injury, but none is validated as a formal biomarker.

## 12. Treatment and current implementation

There is no approved CD3G-specific drug, RNA therapy, or gene therapy, and the clinical-trial search identified no disease-specific interventional trial.

- **Immunoglobulin replacement** for hypogammaglobulinemia or poor specific-antibody responses; the adult CVID-like patient received regular infusions for approximately 20 years. Suggested NCIT concept: immunoglobulin replacement therapy. (lee2019anovelcd3g pages 1-2, lee2019anovelcd3g pages 2-3)
- **Antimicrobials:** prompt pathogen-directed treatment and individualized antibacterial, antiviral, antifungal, or antiparasitic prophylaxis. Suggested NCIT: anti-infective therapy.
- **Autoimmunity:** corticosteroids and steroid-sparing therapy according to organ involvement. Rituximab treated severe cytopenias; sirolimus was used for immune dysregulation in the 2021 case. Suggested NCIT: Rituximab; Sirolimus; corticosteroid therapy. (delmonte2021completeabsenceof pages 1-3)
- **Pulmonary/gastrointestinal supportive care:** airway clearance, pulmonary monitoring, nutrition support, vaccination of household contacts, and specialist treatment of enteropathy, bronchiectasis, and portal hypertension.
- **Allogeneic HSCT:** potentially definitive immune reconstitution for severe/refractory CID, opportunistic infection, life-threatening autoimmunity, or progressive organ disease. Decisions require individualized risk assessment because reported deaths included viral pneumonia and graft-versus-host disease after transplantation. Suggested NCIT: allogeneic hematopoietic stem cell transplantation. (lee2019anovelcd3g pages 1-2)

Evidence does not support a single treatment algorithm. A pragmatic strategy is phenotype-guided: observe mild isolated autoimmunity with immunologic surveillance; add IVIG/prophylaxis for humoral or infectious disease; use targeted immunosuppression for organ-threatening autoimmunity; and refer early to an IEI transplant center when disease is severe or progressive. No CD3G-specific pharmacogenomic association is known.

## 13. Prevention

**Primary prevention of the genotype:** genetic counseling, carrier testing of relatives, and reproductive options—prenatal diagnosis or preimplantation genetic testing—after familial variants are established.

**Secondary prevention:** cascade testing; early immunologic evaluation of siblings; CBC, immunoglobulins, vaccine responses, and TCR/CD3 flow cytometry; periodic pulmonary assessment; and prompt genetic confirmation. Population carrier screening is not currently evidence-based.

**Tertiary prevention:** immunoglobulin replacement when indicated, antimicrobial prophylaxis, rapid fever/infection management, airway clearance, and surveillance for cytopenias, thyroid disease, enteropathy, chronic lung disease, EBV, and treatment toxicity.

Live-attenuated vaccines should be deferred in patients with significant T-cell dysfunction until evaluated by an immunologist. Inactivated vaccines are generally safer but may be poorly immunogenic; responses should be measured where clinically useful. Household and close-contact immunization helps reduce exposure. No lifestyle intervention prevents the inherited defect.

## 14. Other species and natural disease

No well-established naturally occurring veterinary CD3G-deficiency syndrome, breed predisposition, zoonotic transmission, or cross-species infectious transmission was identified. Relevant taxonomy includes **Homo sapiens** (NCBI Taxon 9606) and experimental **Mus musculus** (10090). CD3-complex biology is evolutionarily conserved, but chain-level redundancy differs materially between species.

## 15. Model organisms

CD3-chain knockout mice demonstrate reduced TCR/CD3 expression, impaired thymocyte maturation, and reduced lymphoid cellularity, but mouse models do not fully reproduce human CD3-chain disease. A key limitation is that no single CD3 subunit appears absolutely required for murine T-cell maturation, whereas human CD3δ/ε defects can block T-cell development and human CD3γ deficiency produces its own distinctive residual-T-cell/autoimmune phenotype. (grunebaum2006humantcell pages 5-7)

Human CD3E/CD3D/CD3G replacement mice are immune competent and useful for evaluating human CD3-directed antibodies or bispecific therapeutics, but they are not CD3G-deficiency models. Cellular systems—patient lymphocytes, immortalized T-cell lines, CD3G complementation, Treg suppression assays, and TCR-repertoire sequencing—currently provide the most disease-relevant functional evidence.

## Recent developments and evidence limitations

The most informative mechanistic study remains the 2018 *Blood* analysis, which linked reduced TCR signaling to restricted Treg diversity, defective suppression, and a self-reactive conventional repertoire (published May 2018; DOI [10.1182/blood-2018-02-835561](https://doi.org/10.1182/blood-2018-02-835561)). Its central conclusion was that CD3G mutations reveal “**a role for human CD3γ in Treg diversity and suppressive function**.” (rowe2018patientswithcd3g pages 9-13, rowe2018patientswithcd3g pages 1-6)

The 2019 genotype–phenotype analysis expanded the disease to a CVID-like adult presentation (published December 2019; DOI [10.3389/fimmu.2019.02833](https://doi.org/10.3389/fimmu.2019.02833)). Its abstract states that the patient had “**recurrent sinopulmonary infections without opportunistic infections**” and received immunoglobulin for over 20 years, emphasizing that infection-predominant disease without autoimmunity is possible. (lee2019anovelcd3g pages 1-2)

A 2021 report demonstrated that even “**complete absence of CD3γ protein expression**” can cause CID with autoimmunity rather than classic SCID (DOI [10.1007/s10875-020-00918-z](https://doi.org/10.1007/s10875-020-00918-z)). (delmonte2021completeabsenceof pages 1-3)

The principal 2024 advances are broader IEI sequencing and flow-cytometry implementation rather than a large CD3G-specific cohort. Disease-specific 2024 reports include Chinese cases with lupus-like disease/thyroiditis or recurrent thrombocytopenia, but their full primary data were not available in the retrieved corpus and therefore are not used for quantitative conclusions. A later 2026 synthesis—outside the requested priority window—reported 18 total cases, 9/18 with hypo-/dysgammaglobulinemia and two adult patients with Evans syndrome, reinforcing broad age range and absent genotype–phenotype correlation; it should be treated as an emerging update rather than 2023–2024 evidence. (obeng2026expandingtheclinical pages 5-6, obeng2026expandingtheclinical pages 1-2)

PMIDs were not printed in the retrieved full-text metadata, so DOI URLs are provided rather than potentially unreliable PMID reconstruction. The rarity, publication bias toward severe or unusual cases, inconsistent historical HGVS nomenclature, family clustering, and absence of prospective natural-history cohorts substantially limit estimates of frequency, penetrance, treatment response, and prognosis.

References

1. (rowe2018patientswithcd3g pages 9-13): Jared H. Rowe, Ottavia M. Delmonte, Sevgi Keles, Brian D. Stadinski, Adam K. Dobbs, Lauren A. Henderson, Yasuhiro Yamazaki, Luis M. Allende, Francisco A. Bonilla, Luis I. Gonzalez-Granado, Seyma Celikbilek Celik, Sukru N. Guner, Hasan Kapakli, Christina Yee, Sung-Yun Pai, Eric S. Huseby, Ismail Reisli, Jose R. Regueiro, and Luigi D. Notarangelo. Patients with cd3g mutations reveal a role for human cd3γ in treg diversity and suppressive function. Blood, 131 21:2335-2344, May 2018. URL: https://doi.org/10.1182/blood-2018-02-835561, doi:10.1182/blood-2018-02-835561. This article has 83 citations and is from a highest quality peer-reviewed journal.

2. (rowe2018patientswithcd3g pages 1-6): Jared H. Rowe, Ottavia M. Delmonte, Sevgi Keles, Brian D. Stadinski, Adam K. Dobbs, Lauren A. Henderson, Yasuhiro Yamazaki, Luis M. Allende, Francisco A. Bonilla, Luis I. Gonzalez-Granado, Seyma Celikbilek Celik, Sukru N. Guner, Hasan Kapakli, Christina Yee, Sung-Yun Pai, Eric S. Huseby, Ismail Reisli, Jose R. Regueiro, and Luigi D. Notarangelo. Patients with cd3g mutations reveal a role for human cd3γ in treg diversity and suppressive function. Blood, 131 21:2335-2344, May 2018. URL: https://doi.org/10.1182/blood-2018-02-835561, doi:10.1182/blood-2018-02-835561. This article has 83 citations and is from a highest quality peer-reviewed journal.

3. (rowe2018patientswithcd3g pages 6-9): Jared H. Rowe, Ottavia M. Delmonte, Sevgi Keles, Brian D. Stadinski, Adam K. Dobbs, Lauren A. Henderson, Yasuhiro Yamazaki, Luis M. Allende, Francisco A. Bonilla, Luis I. Gonzalez-Granado, Seyma Celikbilek Celik, Sukru N. Guner, Hasan Kapakli, Christina Yee, Sung-Yun Pai, Eric S. Huseby, Ismail Reisli, Jose R. Regueiro, and Luigi D. Notarangelo. Patients with cd3g mutations reveal a role for human cd3γ in treg diversity and suppressive function. Blood, 131 21:2335-2344, May 2018. URL: https://doi.org/10.1182/blood-2018-02-835561, doi:10.1182/blood-2018-02-835561. This article has 83 citations and is from a highest quality peer-reviewed journal.

4. (lee2019anovelcd3g pages 1-2): Wen-I Lee, Wen-Lang Fan, Chun-Hao Lu, Shih-Hsiang Chen, Ming-Ling Kuo, Syh-Jae Lin, Weng-Sheng Tsai, Tang-Her Jaing, Li-Chen Chen, Kuo-Wei Yeh, Tsung-Chieh Yao, and Jing-Long Huang. A novel cd3g mutation in a taiwanese patient with normal t regulatory function presenting with the cvid phenotype free of autoimmunity—analysis of all genotypes and phenotypes. Frontiers in Immunology, Dec 2019. URL: https://doi.org/10.3389/fimmu.2019.02833, doi:10.3389/fimmu.2019.02833. This article has 22 citations and is from a peer-reviewed journal.

5. (delmonte2021completeabsenceof pages 1-3): Ottavia M. Delmonte, Jared H. Rowe, Adam K. Dobbs, Boaz Palterer, Riccardo Castagnoli, and Luigi D. Notarangelo. Complete absence of cd3γ protein expression is responsible for combined immunodeficiency with autoimmunity rather than scid. Journal of Clinical Immunology, 41:482-485, Nov 2021. URL: https://doi.org/10.1007/s10875-020-00918-z, doi:10.1007/s10875-020-00918-z. This article has 6 citations and is from a domain leading peer-reviewed journal.

6. (obeng2026expandingtheclinical pages 1-2): Raphaela Obeng, Abdulwahab Elsayed, Amos Takyi, Sandra von Hardenberg, Faranaz Atschekzei, Torsten Witte, and Georgios Sogkas. Expanding the clinical spectrum of cd3γ deficiency: comprehensive characterization of adult-onset disease and integrated reevaluation of all reported patients. Frontiers in Immunology, Aug 2026. URL: https://doi.org/10.3389/fimmu.2026.1889169, doi:10.3389/fimmu.2026.1889169. This article has 0 citations and is from a peer-reviewed journal.

7. (obeng2026expandingtheclinical pages 5-6): Raphaela Obeng, Abdulwahab Elsayed, Amos Takyi, Sandra von Hardenberg, Faranaz Atschekzei, Torsten Witte, and Georgios Sogkas. Expanding the clinical spectrum of cd3γ deficiency: comprehensive characterization of adult-onset disease and integrated reevaluation of all reported patients. Frontiers in Immunology, Aug 2026. URL: https://doi.org/10.3389/fimmu.2026.1889169, doi:10.3389/fimmu.2026.1889169. This article has 0 citations and is from a peer-reviewed journal.

8. (lee2019anovelcd3g pages 4-6): Wen-I Lee, Wen-Lang Fan, Chun-Hao Lu, Shih-Hsiang Chen, Ming-Ling Kuo, Syh-Jae Lin, Weng-Sheng Tsai, Tang-Her Jaing, Li-Chen Chen, Kuo-Wei Yeh, Tsung-Chieh Yao, and Jing-Long Huang. A novel cd3g mutation in a taiwanese patient with normal t regulatory function presenting with the cvid phenotype free of autoimmunity—analysis of all genotypes and phenotypes. Frontiers in Immunology, Dec 2019. URL: https://doi.org/10.3389/fimmu.2019.02833, doi:10.3389/fimmu.2019.02833. This article has 22 citations and is from a peer-reviewed journal.

9. (gokturk2014cd3ggenedefects pages 1-2): Bahar Göktürk, S. Keleş, Mine Kiraç, H. Artaç, H. Tokgoz, Ş. Guner, Umran Caliskan, Z. Caliskaner, M.E.L. van der Burg, J. Dongen, Neil V. Morgan, and I. Reisli. Cd3g gene defects in familial autoimmune thyroiditis. Scandinavian Journal of Immunology, 80:354-361, Nov 2014. URL: https://doi.org/10.1111/sji.12200, doi:10.1111/sji.12200. This article has 38 citations and is from a peer-reviewed journal.

10. (rowe2018patientswithcd3g pages 13-18): Jared H. Rowe, Ottavia M. Delmonte, Sevgi Keles, Brian D. Stadinski, Adam K. Dobbs, Lauren A. Henderson, Yasuhiro Yamazaki, Luis M. Allende, Francisco A. Bonilla, Luis I. Gonzalez-Granado, Seyma Celikbilek Celik, Sukru N. Guner, Hasan Kapakli, Christina Yee, Sung-Yun Pai, Eric S. Huseby, Ismail Reisli, Jose R. Regueiro, and Luigi D. Notarangelo. Patients with cd3g mutations reveal a role for human cd3γ in treg diversity and suppressive function. Blood, 131 21:2335-2344, May 2018. URL: https://doi.org/10.1182/blood-2018-02-835561, doi:10.1182/blood-2018-02-835561. This article has 83 citations and is from a highest quality peer-reviewed journal.

11. (lee2019anovelcd3g pages 2-3): Wen-I Lee, Wen-Lang Fan, Chun-Hao Lu, Shih-Hsiang Chen, Ming-Ling Kuo, Syh-Jae Lin, Weng-Sheng Tsai, Tang-Her Jaing, Li-Chen Chen, Kuo-Wei Yeh, Tsung-Chieh Yao, and Jing-Long Huang. A novel cd3g mutation in a taiwanese patient with normal t regulatory function presenting with the cvid phenotype free of autoimmunity—analysis of all genotypes and phenotypes. Frontiers in Immunology, Dec 2019. URL: https://doi.org/10.3389/fimmu.2019.02833, doi:10.3389/fimmu.2019.02833. This article has 22 citations and is from a peer-reviewed journal.

12. (grunebaum2006humantcell pages 5-7): Eyal Grunebaum, Nigel Sharfe, and Chaim M. Roifman. Human t cell immunodeficiency. Immunologic Research, 35:117-125, Jan 2006. URL: https://doi.org/10.1385/ir:35:1:117, doi:10.1385/ir:35:1:117. This article has 28 citations and is from a peer-reviewed journal.

13. (lee2019anovelcd3g pages 10-11): Wen-I Lee, Wen-Lang Fan, Chun-Hao Lu, Shih-Hsiang Chen, Ming-Ling Kuo, Syh-Jae Lin, Weng-Sheng Tsai, Tang-Her Jaing, Li-Chen Chen, Kuo-Wei Yeh, Tsung-Chieh Yao, and Jing-Long Huang. A novel cd3g mutation in a taiwanese patient with normal t regulatory function presenting with the cvid phenotype free of autoimmunity—analysis of all genotypes and phenotypes. Frontiers in Immunology, Dec 2019. URL: https://doi.org/10.3389/fimmu.2019.02833, doi:10.3389/fimmu.2019.02833. This article has 22 citations and is from a peer-reviewed journal.

14. (obeng2026expandingtheclinical pages 8-9): Raphaela Obeng, Abdulwahab Elsayed, Amos Takyi, Sandra von Hardenberg, Faranaz Atschekzei, Torsten Witte, and Georgios Sogkas. Expanding the clinical spectrum of cd3γ deficiency: comprehensive characterization of adult-onset disease and integrated reevaluation of all reported patients. Frontiers in Immunology, Aug 2026. URL: https://doi.org/10.3389/fimmu.2026.1889169, doi:10.3389/fimmu.2026.1889169. This article has 0 citations and is from a peer-reviewed journal.

15. (obeng2026expandingtheclinical pages 7-8): Raphaela Obeng, Abdulwahab Elsayed, Amos Takyi, Sandra von Hardenberg, Faranaz Atschekzei, Torsten Witte, and Georgios Sogkas. Expanding the clinical spectrum of cd3γ deficiency: comprehensive characterization of adult-onset disease and integrated reevaluation of all reported patients. Frontiers in Immunology, Aug 2026. URL: https://doi.org/10.3389/fimmu.2026.1889169, doi:10.3389/fimmu.2026.1889169. This article has 0 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Combined_Immunodeficiency_Due_To_CD3gamma_Deficiency-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 55 |
| Resolved | 55 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014276` (4 mentions) - the report calls it "if available"; MONDO calls it **combined immunodeficiency due to CD3gamma deficiency**