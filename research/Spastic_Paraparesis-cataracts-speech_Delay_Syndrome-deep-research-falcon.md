---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-28T11:31:27.192518'
end_time: '2026-08-28T11:42:16.735387'
duration_seconds: 649.54
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Spastic paraparesis-cataracts-speech delay syndrome (monoallelic FAR1
    gain-of-function, fatty acyl-CoA reductase 1 superactivity)
  mondo_id: MONDO:0036212
  category: Metabolic Disorders
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 1
  validator_version: 0.2.1
term_validation:
  total_terms: 7
  verified: 7
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0036212
    reported_labels:
    - if available
    ontology_label: spastic paraparesis-cataracts-speech delay syndrome
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Spastic_Paraparesis-cataracts-speech_Delay_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spastic paraparesis-cataracts-speech delay syndrome (monoallelic FAR1 gain-of-function, fatty acyl-CoA reductase 1 superactivity)
- **MONDO ID:** MONDO:0036212 (if available)
- **Category:** Metabolic Disorders

## Research Objectives

Please provide a comprehensive research report on **Spastic paraparesis-cataracts-speech delay syndrome (monoallelic FAR1 gain-of-function, fatty acyl-CoA reductase 1 superactivity)** covering all of the
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
- **Disease Name:** Spastic paraparesis-cataracts-speech delay syndrome (monoallelic FAR1 gain-of-function, fatty acyl-CoA reductase 1 superactivity)
- **MONDO ID:** MONDO:0036212 (if available)
- **Category:** Metabolic Disorders

## Research Objectives

Please provide a comprehensive research report on **Spastic paraparesis-cataracts-speech delay syndrome (monoallelic FAR1 gain-of-function, fatty acyl-CoA reductase 1 superactivity)** covering all of the
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


# Spastic paraparesis–cataracts–speech delay syndrome
## Monoallelic **FAR1** gain-of-function / fatty acyl-CoA reductase 1 superactivity

## Executive summary

This is an ultra-rare, childhood-onset neuro-ophthalmic ether-lipid disorder caused by heterozygous, usually de novo missense variants affecting **Arg480 of FAR1**. Its defining combination is bilateral congenital or juvenile cataracts and pyramidal lower-limb disease—spastic diparesis/paraparesis—often accompanied by speech and gross-motor delay, truncal hypotonia, and early-life seizures. Unlike autosomal-recessive FAR1 deficiency, which decreases plasmalogens, dominant Arg480 disease prevents normal plasmalogen-triggered degradation of FAR1 and therefore causes **excess fatty-alcohol/ether-lipid synthesis** and elevated plasmalogens. The detailed human evidence remains dominated by one 12-patient cohort; consequently, prevalence, lifetime prognosis, penetrance, and treatment-effect estimates are not established. (ferdinandusse2021anautosomaldominant pages 1-2, ferdinandusse2021anautosomaldominant pages 4-5, ferdinandusse2021anautosomaldominant pages 6-7)

The foundational evidence is Ferdinandusse et al., *Genetics in Medicine*, received July 24, 2020 and published in volume 23 in April 2021, DOI [10.1038/s41436-020-01027-3](https://doi.org/10.1038/s41436-020-01027-3). Its abstract states: **“Heterozygous de novo variants affecting the Arg480 residue of FAR1 lead to an autosomal dominant disorder with a different disease mechanism than that of recessive FAR1 deficiency and a diametrically opposed biochemical phenotype.”** (ferdinandusse2021anautosomaldominant pages 1-2)

| Domain | Finding | Quantitative detail | Evidence type/strength |
|---|---|---|---|
| Cohort size / age | Foundational dominant FAR1 cohort comprised 12 affected individuals evaluated clinically and functionally | Ages at study: 2-19 years; all had neurological symptoms in the first years of life (ferdinandusse2021anautosomaldominant pages 4-5) | Human clinical cohort with patient-derived fibroblast functional studies; strongest direct evidence available (ferdinandusse2021anautosomaldominant pages 4-5, ferdinandusse2021anautosomaldominant pages 1-2) |
| Variant spectrum | All reported pathogenic dominant variants in the foundational cohort altered Arg480 | p.Arg480Cys: 7/12; p.Arg480His: 4/12; p.Arg480Leu: 1/12 (ferdinandusse2021anautosomaldominant pages 3-4) | Human genetic evidence from de novo recurrent missense variants; strong (ferdinandusse2021anautosomaldominant pages 3-4) |
| Inheritance | Disease mechanism is monoallelic, autosomal dominant, arising through de novo variants | 12/12 reported as de novo heterozygous FAR1 variants (ferdinandusse2021anautosomaldominant pages 4-5, ferdinandusse2021anautosomaldominant pages 3-4) | Human trio/exome-based evidence; strong (ferdinandusse2021anautosomaldominant pages 4-5, ferdinandusse2021anautosomaldominant pages 6-7) |
| Cardinal neurologic phenotype | Spastic paraparesis / pyramidal tract dysfunction is the core neurologic feature | 12/12; described with lower-limb hypertonia, truncal hypotonia in 6/12, and ankle clonus (ferdinandusse2021anautosomaldominant pages 4-5) | Human clinical cohort; strong (ferdinandusse2021anautosomaldominant pages 4-5) |
| Ocular phenotype | Bilateral cataracts are universal in the foundational cohort | 12/12 total; congenital in 5/12 and acquired/juvenile in 7/12 (ferdinandusse2021anautosomaldominant pages 4-5) | Human clinical cohort; strong (ferdinandusse2021anautosomaldominant pages 4-5) |
| Developmental phenotype | Speech and motor delay are common; intellectual disability is less frequent | Speech delay 10/12; gross motor developmental delay reported in most; cognitive delay / intellectual disability 3/12 (ferdinandusse2021anautosomaldominant pages 4-5) | Human clinical cohort; moderate-to-strong (ferdinandusse2021anautosomaldominant pages 4-5, ferdinandusse2021anautosomaldominant pages 6-7) |
| Seizures / treatment outcome | Early-life seizures were common and often treatment-responsive | Seizures in 8/12, mainly in the first months of life; treated with barbiturates, levetiracetam, and/or oxcarbazepine; antiepileptics discontinued without recurrence in 4/8 (ferdinandusse2021anautosomaldominant pages 4-5) | Human clinical cohort with follow-up; moderate-to-strong (ferdinandusse2021anautosomaldominant pages 4-5) |
| Neuroimaging | Brain MRI usually non-diagnostic or normal | Normal in 10/12; 1 had abnormal temporal lobe morphology with ventricular prominence and normal white matter; 1 had benign enlargement of subarachnoid spaces (ferdinandusse2021anautosomaldominant pages 4-5) | Human clinical cohort; strong for available sample (ferdinandusse2021anautosomaldominant pages 4-5) |
| Biochemical finding | Dominant disease shows elevated plasmalogens, opposite to recessive FAR1 deficiency | Untreated patient fibroblasts had mean C16:0-plasmalogen levels about twofold higher than controls; FAR1 protein levels were threefold higher than HDG-treated controls (ferdinandusse2021anautosomaldominant pages 4-5) | Patient fibroblast biochemistry/immunoblot; strong mechanistic evidence (ferdinandusse2021anautosomaldominant pages 4-5) |
| Enzyme / localization | FAR1 catalytic function and peroxisomal localization are preserved | FAR1 enzyme activity preserved; mutant FAR1 localized normally to peroxisomes in patient fibroblasts (ferdinandusse2021anautosomaldominant pages 6-7) | Patient-derived cell functional assays and immunofluorescence; strong (ferdinandusse2021anautosomaldominant pages 6-7) |
| Lipidomics | Ether lipids accumulate with reciprocal depletion of corresponding nonether lipids | Increased PC[O], PE[O], DG[O], TG[O]; examples in figure summary include PE[O] about 2.5x, DG[O] about 3.3x, TG[O] about 5.8x versus controls; PUFA-rich PC[O] species particularly increased (ferdinandusse2021anautosomaldominant pages 8-9, ferdinandusse2021anautosomaldominant pages 9-10) | Patient fibroblast lipidomics in 3 analyzed patients vs 3 controls; strong for cellular biochemical phenotype (ferdinandusse2021anautosomaldominant pages 8-9, ferdinandusse2021anautosomaldominant pages 9-10) |
| Flux evidence | Ether lipid synthesis from exogenous substrate is increased | C17:0-alcohol incorporation into LPC(O-17:0) was fourfold higher in patients; C17:0-acid incorporation into nonether LPC(17:0) was comparable between patients and controls (ferdinandusse2021anautosomaldominant pages 9-10) | Patient fibroblast metabolic labeling; strong direct functional evidence (ferdinandusse2021anautosomaldominant pages 9-10) |
| Mechanism | Arg480 variants disrupt plasmalogen-dependent negative feedback on FAR1 stability, causing uncontrolled ether lipid synthesis | Arg480 lies in the transmembrane region (aa 466-483); elevated plasmalogens failed to lower FAR1 protein in patient cells after HDG treatment, unlike controls (ferdinandusse2021anautosomaldominant pages 8-9, ferdinandusse2021anautosomaldominant pages 4-5, ferdinandusse2021anautosomaldominant pages 2-3) | Human patient-derived mechanistic cell biology supported by review synthesis; strong (ferdinandusse2021anautosomaldominant pages 8-9, honsho2023regulationofplasmalogen pages 1-3) |
| Diagnostic implications | FAR1 should be considered in patients with spastic paraparesis plus bilateral cataracts; plasmalogens can support functional interpretation | Authors recommend adding FAR1 to hereditary spastic paraplegia, cerebral palsy, and juvenile cataract panels; erythrocyte plasmalogen measurement may be informative because both high and low values can indicate FAR1-related pathology (ferdinandusse2021anautosomaldominant pages 4-5, ferdinandusse2021anautosomaldominant pages 9-10) | Expert recommendation grounded in cohort and functional data; moderate-to-strong (ferdinandusse2021anautosomaldominant pages 4-5, ferdinandusse2021anautosomaldominant pages 9-10) |
| Evidence limitations | Evidence base remains very small and recent follow-up/expansion papers were not fully retrievable in this tool environment | Direct detailed extraction currently rests mainly on one 12-patient cohort; additional 2022-2024 reports were identified by metadata but not fully available here for verification (ferdinandusse2021anautosomaldominant pages 1-2, honsho2023regulationofplasmalogen pages 1-3) | Limitation statement based on available retrieved sources; important caution for knowledge-base use (ferdinandusse2021anautosomaldominant pages 1-2, honsho2023regulationofplasmalogen pages 1-3) |


*Table: This table summarizes the strongest directly retrievable evidence for monoallelic FAR1 gain-of-function syndrome, focusing on recurrent Arg480 variants, phenotype frequencies, biochemical mechanism, and diagnostic implications. It is useful as a compact evidence map for knowledge-base extraction while clearly flagging current evidence limitations.*

## 1. Disease information

### Definition and scope

The disorder is a monogenic metabolic/neurodevelopmental syndrome in which increased stability of peroxisomal FAR1 dysregulates ether-glycerophospholipid homeostasis. It should not be conflated with **autosomal-recessive FAR1 deficiency**, despite overlap in cataracts, spasticity, and seizures: recessive deficiency causes low plasmalogens, profound developmental impairment, growth failure, microcephaly, and dysmorphism, whereas dominant Arg480 disease generally has elevated plasmalogens, normal growth, no characteristic dysmorphism, and usually normal MRI. (ferdinandusse2021anautosomaldominant pages 6-7)

### Names and identifiers

- Preferred name supplied for this report: **spastic paraparesis–cataracts–speech delay syndrome**.
- Mechanistic synonyms: **autosomal-dominant FAR1-related disorder**, **dominant FAR1 gain-of-function disorder**, **FAR1 superactivity**, and **FAR1-related uncontrolled ether-lipid synthesis**.
- **MONDO:** MONDO:0036212, as supplied in the query; this identifier was not independently verified in the retrieved literature.
- **OMIM/Orphanet:** no independently verified disorder-specific number was available in the retrieved texts. The gene is **FAR1**; database identifiers should be checked directly before production ingestion.
- **ICD-10/ICD-11 and MeSH:** no syndrome-specific code or heading was found. Coding will generally require component or broader categories—for example hereditary spastic paraplegia/spastic diplegia, congenital or juvenile cataract, developmental disorder, and inborn error of lipid metabolism.

The principal report is an **aggregated, deeply phenotyped 12-patient research cohort**, assembled through clinical exome analysis, GeneMatcher, and undiagnosed-disease collaborations—not an EHR-derived population study. Eight cases were found after review of 42,983 exome trios plus 9,205 exome-based targeted-list trios, with further international matching. This ascertainment strategy cannot yield prevalence or unbiased phenotype-frequency estimates. (ferdinandusse2021anautosomaldominant pages 6-7)

## 2. Etiology, risks, and protective factors

### Causal factor

The demonstrated cause is a **germline heterozygous missense substitution at FAR1 residue Arg480**. In the original cohort, all were de novo: c.1438C>T (p.Arg480Cys), 7/12; c.1439G>A (p.Arg480His), 4/12; and c.1439G>T (p.Arg480Leu), 1/12. Arg480 lies within the predicted membrane-spanning segment, amino acids 466–483. (ferdinandusse2021anautosomaldominant pages 3-4, ferdinandusse2021anautosomaldominant pages 8-9)

These are not ordinary haploinsufficient alleles. Mutant protein retains catalytic function and normal peroxisomal localization but escapes plasmalogen-dependent downregulation, producing a gain-of-function phenotype through excess protein abundance and metabolic flux. (ferdinandusse2021anautosomaldominant pages 6-7)

### Risk, protective, and gene–environment factors

- **Genetic risk:** carrying a pathogenic Arg480 allele is the only established risk factor.
- **Family history:** often absent because all foundational cases were de novo. An affected individual would theoretically transmit the allele with a 50% probability per conception, although reproductive fitness and multigenerational penetrance have not been characterized.
- **Modifiers, protective alleles, founder effects, anticipation, carrier frequency, consanguinity effects, and germline-mosaicism frequency:** unknown.
- **Environmental, dietary, toxic, occupational, infectious, lifestyle, sex, or age-related acquisition risks:** none established. This is congenital genetic disease, not an acquired exposure disorder.
- **Protective factors and gene–environment interactions:** none demonstrated. The 2023 review notes that erythrocyte plasmalogen levels in vegans do not differ from those on a normal diet, supporting endogenous synthesis rather than ordinary dietary supply as the principal determinant; this does not prove diet has no modifying effect in FAR1 gain-of-function disease. (honsho2023regulationofplasmalogen pages 1-3)

## 3. Phenotypes

Frequencies below come from the foundational 12-patient series, ages 2–19 years, and therefore may change with ascertainment of milder adults or additional variants. All developed neurologic manifestations in the first years of life. (ferdinandusse2021anautosomaldominant pages 4-5)

- **Spastic diparesis/paraparesis—12/12 (100%)**: pyramidal tract dysfunction, lower-limb hypertonia, ankle clonus, gait impairment, and variable need for braces, walkers, crutches, or wheelchairs. Childhood onset; chronic and functionally important. Suggested HPO: **Spastic paraplegia (HP:0001258)**, lower-limb hypertonia, ankle clonus, abnormal gait, impaired ambulation. (ferdinandusse2021anautosomaldominant pages 4-5)
- **Bilateral cataracts—12/12 (100%)**: congenital in 5/12 (42%) and acquired/juvenile in 7/12 (58%). Suggested HPO: **Cataract (HP:0000518)**, congenital cataract, juvenile cataract, bilateral cataract. Visual impairment and cataract surgery can materially affect development and daily functioning. (ferdinandusse2021anautosomaldominant pages 4-5)
- **Speech/language delay—10/12 (83%)**: receptive language exceeded expressive language in three patients. Suggested HPO: **Delayed speech and language development (HP:0000750)** and expressive-language delay. (ferdinandusse2021anautosomaldominant pages 4-5)
- **Seizures—8/12 (67%)**: mainly began during the first months of life and were generally treatment-responsive. Suggested HPO: **Seizure (HP:0001250)**, infantile-onset seizure, generalized tonic-clonic seizure where individually documented. (ferdinandusse2021anautosomaldominant pages 4-5)
- **Truncal/axial hypotonia—6/12 (50%)**, coexisting with lower-limb spasticity. Suggested HPO: **Axial hypotonia (HP:0008936)**. (ferdinandusse2021anautosomaldominant pages 4-5)
- **Cognitive delay/intellectual disability—3/12 (25%)**: less frequent than speech and motor delay, indicating that language or motor disability should not automatically be interpreted as global intellectual disability. Suggested HPO: global developmental delay and intellectual disability, only when clinically established. (ferdinandusse2021anautosomaldominant pages 4-5)
- **Gross-motor delay:** reported in most, but a precise numerator was not extractable. Suggested HPO: **Gross motor development delay (HP:0002194)**.
- **Macrocephaly—2/12**; growth delay occurred in only one. No consistent dysmorphism was observed. (ferdinandusse2021anautosomaldominant pages 4-5)
- **MRI:** normal in 10/12; one patient had abnormal temporal-lobe morphology and ventricular prominence with normal white matter, while one had benign enlargement of subarachnoid spaces. A normal MRI therefore does not argue against the diagnosis. (ferdinandusse2021anautosomaldominant pages 4-5)

No disease-specific EQ-5D, SF-36, PROMIS, caregiver-burden, or formal quality-of-life study was found. Likely burdens—impaired mobility, communication, vision, school participation, self-care, and seizure monitoring—are clinically plausible but have not been quantified.

## 4. Genetic and molecular information

### Gene and variants

**FAR1** encodes fatty acyl-CoA reductase 1, a peroxisomal membrane protein and rate-limiting supplier of long-chain fatty alcohols for ether-lipid biosynthesis. Suggested gene records include HGNC/NCBI Gene/Ensembl/UniProt entries for **FAR1**; exact accession numbers should be programmatically verified rather than inferred from the disease article.

The three foundational variants are recurrent germline missense alleles at one residue:

1. **NM transcript-dependent c.1438C>T, p.Arg480Cys**—7 patients.
2. **c.1439G>A, p.Arg480His**—4 patients.
3. **c.1439G>T, p.Arg480Leu**—1 patient. (ferdinandusse2021anautosomaldominant pages 3-4)

They were absent from parents in the reported cases and functionally validated. The study predates or does not provide a uniform current ClinVar ACMG classification in the retrieved text; nevertheless, recurrent de novo occurrence, highly specific phenotype, residue clustering, and strong patient-cell functional evidence support pathogenicity. Transcript and genome-build normalization, current ClinVar assertions, and gnomAD frequencies should be verified for each record before database loading. Population frequency was not given in the retrieved full text; the recurrence as de novo alleles and ultra-rare phenotype imply rarity but do not substitute for a gnomAD query.

No causal structural variant, chromosomal abnormality, somatic variant, repeat expansion, mitochondrial variant, modifier gene, or disease-associated epigenetic signature has been established. There is no evidence for a dominant-negative mechanism.

## 5. Environmental information

No toxin, radiation, pollution, occupational exposure, smoking, alcohol, diet, exercise pattern, or infectious agent is known to cause or trigger the syndrome. Environmental entries should therefore be represented as **not established**, rather than “protective” or “risk-free.” Plasmalogen metabolism can respond to cellular state in experimental systems, but no clinically validated environmental modifier of Arg480 disease exists. (honsho2023regulationofplasmalogen pages 1-3)

## 6. Mechanism and pathophysiology

### Normal pathway

Ether-lipid synthesis begins in the peroxisome. GNPAT generates acyl-DHAP; AGPS replaces the acyl group with a long-chain fatty alcohol; downstream reactions continue outside the peroxisome and ultimately generate plasmanyl and plasmenyl phospholipids. FAR1 reduces fatty acyl-CoA to fatty alcohol and is rate-limiting. At high plasmalogen abundance, FAR1 protein is normally degraded without requiring reduced FAR1 transcription, establishing negative feedback. (ferdinandusse2021anautosomaldominant pages 1-2, honsho2023regulationofplasmalogen pages 1-3)

Suggested annotations include:

- GO biological process: **ether lipid biosynthetic process**, **plasmalogen biosynthetic process**, **fatty alcohol biosynthetic process**, cellular-lipid homeostasis, glycerophospholipid metabolism, and negative regulation of biosynthesis.
- GO molecular function: fatty-acyl-CoA reductase activity / oxidoreductase activity acting on the CH–OH group with NAD(P)+-related annotation as curated for FAR1.
- GO cellular component: **peroxisomal membrane**, peroxisome, and membrane-spanning region.
- Chemicals: fatty acyl-CoA, long-chain fatty alcohol, plasmalogen, phosphatidylcholine, phosphatidylethanolamine, diacylglycerol, triacylglycerol, docosahexaenoic acid, and arachidonic acid; precise CHEBI identifiers should be retrieved from CHEBI.

### Causal chain

**De novo Arg480 substitution → defective plasmalogen-dependent destabilization of FAR1 → persistently elevated FAR1 protein despite high plasmalogens → excess conversion of fatty acyl-CoA to fatty alcohol → increased ether-lipid flux → accumulation of ether phospholipids and neutral ether lipids, reciprocal reduction of corresponding nonether species, and PUFA redistribution → altered membrane composition/homeostasis in vulnerable neural, myelin, muscle, and lens tissues → spastic paraparesis, developmental manifestations, seizures, and cataracts.** The first five links are experimentally supported; the precise link from altered lipid composition to specific tissue injury remains unresolved. (ferdinandusse2021anautosomaldominant pages 8-9, ferdinandusse2021anautosomaldominant pages 4-5, ferdinandusse2021anautosomaldominant pages 9-10)

### Direct biochemical evidence

In untreated patient fibroblasts, mean C16:0 plasmalogen was approximately twice the control level. After alkylglycerol/HDG loading, controls increased C16:0 plasmalogen by 199–291% and lowered FAR1 protein by 31–47%; patient cells increased plasmalogen by 130–224% but showed no consistent reduction in FAR1 protein. Patient FAR1 remained normally localized to peroxisomes. (ferdinandusse2021anautosomaldominant pages 4-5, ferdinandusse2021anautosomaldominant pages 6-7)

Metabolic labeling showed fourfold greater incorporation of C17:0 alcohol into ether-linked LPC(O-17:0), while incorporation of C17:0 acid into nonether LPC(17:0) was comparable. Lipidomics in three patient and three control fibroblast lines demonstrated increased PC[O], PE[O], DG[O], and TG[O], decreased nonether PC and (lyso)PE, and preferential accumulation of PUFA-rich ether-PC species. Some aggregate classes increased approximately 2.5-, 3.3-, or 5.8-fold. (ferdinandusse2021anautosomaldominant pages 8-9, ferdinandusse2021anautosomaldominant pages 9-10)

The authors conclude that **“both fatty alcohol and ether lipid levels need to be tightly regulated, because an imbalance leads to disease.”** They also emphasize that both ether-lipid shortage and excess can produce neurologic and ocular pathology. (ferdinandusse2021anautosomaldominant pages 9-10)

### Tissue biology and uncertainties

Plasmalogens account for about 20% of human phospholipids and are particularly abundant in central nervous system, heart, kidney, and white blood cells. They influence membrane dynamics, signaling, and possibly antioxidative functions. (ferdinandusse2021anautosomaldominant pages 1-2)

A 2023 review proposed that brain plasmalogens are predominantly synthesized locally rather than imported from blood and noted that both deficient and elevated plasmalogen states suppress cholesterol synthesis. It hypothesized that disturbed cholesterol/plasmalogen homeostasis could contribute to shared neurologic phenotypes, but this remains indirect—not demonstrated in Arg480 patient brain tissue. (honsho2023regulationofplasmalogen pages 1-3, honsho2023regulationofplasmalogen pages 3-5)

No validated immune, inflammatory, apoptotic, autophagic, ferroptotic, or epigenetic disease mechanism has been shown in these patients. No single-cell, spatial-transcriptomic, CRISPR-screen, or integrated human multi-omics dataset was retrievable. A 2024 paper, Della Marina et al., “Lipid and protein imbalances in muscle of a FAR1-patient with a heterozygous de novo variant,” *Journal of Neuropathology & Experimental Neurology* 83:979–983, July 2024, DOI [10.1093/jnen/nlae071](https://doi.org/10.1093/jnen/nlae071), was identified, but its full text was unavailable to the tool; detailed molecular claims from it are therefore not reproduced.

## 7. Anatomical structures affected

### Directly affected systems

- **Nervous system:** corticospinal/pyramidal motor system, with lower-limb-predominant spasticity; possible broader motor-development and seizure networks. Suggested UBERON: brain, cerebral cortex, spinal cord, corticospinal tract, peripheral nervous system; use only phenotype-supported sites.
- **Eye:** bilateral crystalline lens. Suggested UBERON: eye and lens; HPO cataract terms are better supported than finer anatomical localization.
- **Musculoskeletal system:** secondary muscle stiffness, weakness/disuse, contracture risk, and mobility impairment; direct primary muscle pathology remains less established.

Potential cell types include **upper motor neuron**, neuron, oligodendrocyte, Schwann cell, skeletal-muscle fiber, and lens fiber cell. These are mechanistically reasonable CL terms, but patient-cell evidence directly demonstrates abnormality only in cultured dermal fibroblasts. The subcellular compartment with strongest direct evidence is the **peroxisomal membrane**. (ferdinandusse2021anautosomaldominant pages 6-7)

Cataracts are bilateral; the motor phenotype is generally bilateral lower-limb disease. No consistent cerebral lesion or lateralization is reported.

## 8. Temporal development

The disorder is congenital or early pediatric and chronic. Neurologic symptoms appeared within the first years; seizures often started in the first months. Cataracts may be present at birth or develop during childhood. Spastic paraparesis and developmental impairment appear persistent, but the small, cross-sectional cohort does not define standardized early/intermediate/advanced stages or a reliable progression rate. (ferdinandusse2021anautosomaldominant pages 4-5)

Seizures may remit: antiseizure medication was stopped without recurrence in 4 of 8 affected patients. No remission of the underlying genetic/metabolic disorder is documented. Critical windows probably include early ophthalmologic treatment to avoid deprivation amblyopia and early developmental/physical therapy, but FAR1-specific intervention windows have not been studied. (ferdinandusse2021anautosomaldominant pages 4-5)

## 9. Inheritance and population

Inheritance is **autosomal dominant**, with all 12 foundational cases arising de novo. Penetrance appeared high for cataracts and spastic paraparesis among ascertained Arg480 carriers, but this cohort was selected through symptomatic testing; population penetrance cannot be inferred. Expressivity is variable for cataract timing, seizures, language/motor delay, cognition, hypotonia, and mobility. (ferdinandusse2021anautosomaldominant pages 3-4, ferdinandusse2021anautosomaldominant pages 4-5)

No incidence, prevalence per 100,000, carrier frequency, sex ratio estimate, ethnic enrichment, regional clustering, or founder effect is available. The original cohort included 6 females and 6 males, but n=12 is too small to establish a 1:1 population ratio. Consanguinity is not etiologically relevant to the dominant de novo mechanism, although it may complicate individual pedigrees. Anticipation has not been reported. Parental germline mosaicism remains theoretically possible in any apparently de novo disorder, but no FAR1-specific recurrence estimate exists.

Recent literature identified by metadata includes Almuqbil et al., “Milder presentation of autosomal dominant fatty acyl CoA reductase 1-related syndrome,” *Clinical Case Reports*, October 2022, DOI [10.1002/ccr3.6307](https://doi.org/10.1002/ccr3.6307), and Westenberger et al., “Spectrum of FAR1 variants and related neurological conditions,” *Movement Disorders* 38:502–504, February 2023, DOI [10.1002/mds.29323](https://doi.org/10.1002/mds.29323). Their full texts were not retrievable here, so variant-level expansion and revised frequencies could not be independently extracted.

## 10. Diagnostics

### Clinical recognition

Suspect dominant FAR1 disease in a child with **bilateral congenital/juvenile cataracts plus spastic diparesis/paraparesis**, especially with speech/gross-motor delay, axial hypotonia, clonus, or infantile seizures. The investigators explicitly recommend adding FAR1 to panels for hereditary spastic paraplegia, cerebral palsy, and juvenile cataract. (ferdinandusse2021anautosomaldominant pages 1-2, ferdinandusse2021anautosomaldominant pages 9-10)

### Testing strategy

1. **Phenotyping:** pediatric neurologic examination, gait/GMFCS-style functional assessment, developmental and speech evaluation, complete ophthalmologic examination, and seizure history.
2. **Molecular testing:** trio-based WES or WGS is preferred in a sporadic child because it identifies the allele and confirms de novo status. A hereditary-spastic-paraplegia, cerebral-palsy, cataract, or peroxisomal/ether-lipid panel must include full **FAR1** coding coverage, particularly codon 480. Sanger confirmation and parental testing are appropriate.
3. **Biochemical support:** quantitative erythrocyte plasmalogens or validated lipidomics. The authors specifically propose erythrocyte plasmalogens as a functional readout because both unusually high and unusually low levels can indicate FAR1 pathology. Normal routine peroxisomal studies or assuming that only low plasmalogens matter could miss the dominant disorder. (ferdinandusse2021anautosomaldominant pages 9-10)
4. **Functional resolution of uncertain variants:** patient fibroblast plasmalogens, FAR1 abundance and response to plasmalogen/alkylglycerol loading, fatty-acyl-CoA reductase flux, peroxisomal localization, and lipidomics. These remain specialized research assays. (ferdinandusse2021anautosomaldominant pages 1-2, ferdinandusse2021anautosomaldominant pages 4-5)
5. **Ancillary tests:** brain MRI to assess alternatives, despite usually normal imaging; EEG when seizures are suspected; vision assessment; and physiotherapy/orthopedic evaluation. EMG, nerve conduction, biopsy, proteomics, and muscle MRI are not established routine diagnostic criteria.

CMA, karyotyping, FISH, mtDNA sequencing, and repeat-expansion testing are not targeted tests for this condition but may be used when phenotype or first-line sequencing suggests an alternative. There are no standardized clinical criteria, newborn screen, or population-carrier screen.

### Differential diagnosis

Important alternatives include recessive FAR1 deficiency; rhizomelic chondrodysplasia punctata and other peroxisomal ether-lipid deficiencies; **ALDH18A1**, **GBA2**, and other complicated hereditary spastic paraplegias with cataracts; cerebral palsy; congenital-cataract syndromes; **SELENOI/EPT1**, **PCYT2**, and **ALDH3A2/Sjögren–Larsson syndrome** disorders. Elevated rather than deficient plasmalogens, absence of rhizomelia/growth failure/dysmorphism, usually normal white matter, and a heterozygous Arg480 FAR1 variant favor dominant FAR1 superactivity. (ferdinandusse2021anautosomaldominant pages 6-7, ferdinandusse2021anautosomaldominant pages 9-10)

## 11. Outcome and prognosis

There are no survival curves, mortality rates, disease-specific deaths, life-expectancy estimates, or validated prognostic models. No early mortality signal was reported through ages 2–19, but the cohort is too young and small to infer normal lifespan. (ferdinandusse2021anautosomaldominant pages 4-5)

Morbidity is driven by lifelong motor disability, cataract-related visual impairment, developmental/communication limitations, and seizures. Mobility ranged from walking with aids to inability to walk in the cohort table. Intellectual disability is not universal, and seizure remission is possible. The most defensible favorable indicators are preserved cognition in many patients, mostly normal MRI, normal growth, and treatment-responsive seizures; however, none has been formally validated as prognostic. No prognostic biomarker beyond the diagnostic lipid phenotype exists.

## 12. Treatment and current applications

### Disease-modifying therapy

No approved pharmacologic, gene, RNA, enzyme, cell, or dietary therapy corrects FAR1 gain-of-function. The ClinicalTrials.gov search found no relevant registered interventional study. Because the disease involves **excess**, not deficiency, plasmalogen or alkylglycerol replacement strategies developed for plasmalogen-deficient disorders are mechanistically inappropriate outside research and could theoretically aggravate the biochemical imbalance. The 2023 review discusses replacement only for deficient models and emphasizes that small molecules regulating plasmalogen homeostasis remain to be developed. (honsho2023regulationofplasmalogen pages 5-7, honsho2023regulationofplasmalogen pages 3-5)

Potential future approaches—selective FAR1 inhibition, restoration of mutant-protein degradation, allele-selective siRNA/ASO, or editing of the mutant allele—are conceptual. None has been tested in a disease model, and systemic suppression carries a risk of converting excess into deficiency.

### Symptomatic and supportive management

- **Seizures:** barbiturates, levetiracetam, and/or oxcarbazepine were used; medication could be withdrawn without recurrence in 4/8 patients. Treatment and withdrawal should follow pediatric epilepsy standards and EEG/clinical review. NCIT concepts: anticonvulsant therapy; levetiracetam; oxcarbazepine. (ferdinandusse2021anautosomaldominant pages 4-5)
- **Cataracts:** pediatric ophthalmology, refraction and amblyopia prevention; cataract extraction and lens rehabilitation when visually significant. FAR1-specific surgical outcomes have not been published. NCIT: cataract surgery/ophthalmologic procedure.
- **Spasticity and mobility:** individualized physiotherapy, stretching, orthoses, walkers/wheelchairs, occupational therapy, orthopedic surveillance, and conventional antispasticity treatment when indicated. No FAR1-specific comparative outcomes exist. NCIT: physical therapy, occupational therapy, rehabilitation therapy.
- **Communication/development:** early speech-language therapy, augmentative communication where needed, educational support, and neuropsychological assessment.
- **Surveillance:** serial ophthalmology, neurologic/seizure review, mobility/contracture and hip/spine assessment, nutrition, and psychosocial support.

No pharmacogenomic guidance, response-rate dataset, adverse-event registry, or genotype-guided treatment algorithm is available.

## 13. Prevention

Primary lifestyle or vaccine prevention is not applicable. Secondary prevention means early recognition of cataracts, seizures, developmental delay, and spasticity—not prevention of the genotype. Tertiary prevention includes amblyopia treatment, seizure control, contracture prevention, mobility support, and communication intervention.

Genetic counseling should explain the usually de novo autosomal-dominant mechanism, theoretical 50% transmission risk from an affected individual, low but nonzero recurrence possibility from parental germline mosaicism, and reproductive options after the familial variant is known: prenatal diagnosis and preimplantation genetic testing. Cascade testing is most relevant to biological parents and offspring; broad population screening is unsupported.

## 14. Other species and natural disease

No naturally occurring FAR1 Arg480-equivalent syndrome in companion animals, livestock, or wildlife was found, and there is no zoonotic or cross-species transmission. FAR1 orthologs and ether-lipid biology are evolutionarily conserved across animals; plasmalogens occur in vertebrates, invertebrates, and anaerobic bacteria but generally not plants or fungi. Exact NCBI Taxon, ortholog-gene, and VBO identifiers should be imported from taxonomy/model-organism databases rather than inferred here. (honsho2023regulationofplasmalogen pages 1-3)

## 15. Model organisms and experimental systems

### Direct model

The strongest disease model is **patient-derived cultured skin fibroblasts** carrying p.Arg480His or p.Arg480Cys. These cells reproduce the defining biochemical phenotype: preserved peroxisomal localization and enzymatic function, defective feedback degradation, elevated plasmalogens, increased ether-lipid flux, and broad lipidomic remodeling. They are suitable for testing FAR1 stability, allele-selective suppression, metabolic flux, and candidate inhibitors. Their limitation is that fibroblasts do not model upper motor neurons, developing lens, myelin, or neural circuits. (ferdinandusse2021anautosomaldominant pages 4-5, ferdinandusse2021anautosomaldominant pages 6-7, ferdinandusse2021anautosomaldominant pages 9-10)

### Indirect models

Pex7-, Gnpat-, and Pex14-deficient mice and other plasmalogen-deficient systems demonstrate feedback elevation of FAR1 and establish the importance of plasmalogens for myelination and lens biology. However, they model **low ether lipids**, the biochemical opposite of dominant FAR1 superactivity, and cannot be assumed to reproduce its disease mechanism. The 2023 review reports impaired myelination and reduced MBP in deficient models and notes local brain synthesis and difficulty delivering plasmalogens to brain. These models are useful for defining a safe therapeutic window, not for claiming efficacy in Arg480 disease. (honsho2023regulationofplasmalogen pages 1-3, honsho2023regulationofplasmalogen pages 3-5)

No validated FAR1-Arg480 knock-in mouse, rat, zebrafish, Drosophila, *C. elegans*, organoid, iPSC-derived motor-neuron, or lens-organoid model was identified. Developing an isogenic Arg480 knock-in model is a high-priority need because it would permit longitudinal neurologic and ocular phenotyping and preclinical testing without confusing gain- and loss-of-function biology.

## Evidence appraisal and knowledge gaps

The association is compelling because of recurrent de novo variants at one residue, a highly coherent phenotype, and multiple orthogonal assays in patient cells. The main weakness is scale: phenotype percentages derive from only 12 ascertainment-enriched children, and detailed biochemical work used three patient fibroblast lines. Population prevalence, adult natural history, penetrance, variant spectrum beyond Arg480, variant-specific severity, fertility, lifespan, optimal surveillance, and treatment outcomes remain unknown. (ferdinandusse2021anautosomaldominant pages 3-4, ferdinandusse2021anautosomaldominant pages 8-9, ferdinandusse2021anautosomaldominant pages 4-5)

The most authoritative recent mechanistic synthesis is Honsho and Fujiki, “Regulation of plasmalogen biosynthesis in mammalian cells and tissues,” *Brain Research Bulletin* 194:118–123, published March 2023, DOI [10.1016/j.brainresbull.2023.01.011](https://doi.org/10.1016/j.brainresbull.2023.01.011). It concludes that regulation of plasmalogen sensing, signaling, FAR1 degradation, and tissue homeostasis remains incompletely understood—an important caution against overstating downstream pathogenesis or proposing untested supplementation. (honsho2023regulationofplasmalogen pages 1-3, honsho2023regulationofplasmalogen pages 5-7)

References

1. (ferdinandusse2021anautosomaldominant pages 1-2): Sacha Ferdinandusse, Kirsty McWalter, Heleen te Brinke, Lodewijk IJlst, Petra M. Mooijer, Jos P.N. Ruiter, Alida E.M. van Lint, Mia Pras-Raves, Eric Wever, Francisca Millan, Maria J. Guillen Sacoto, Amber Begtrup, Mark Tarnopolsky, Lauren Brady, Roger L. Ladda, Susan L. Sell, Catherine B. Nowak, Jessica Douglas, Cuixia Tian, Elizabeth Ulm, Seth Perlman, Arlene V. Drack, Karen Chong, Nicole Martin, Jennifer Brault, Elly Brokamp, Camilo Toro, William A. Gahl, Ellen F. Macnamara, Lynne Wolfe, Mercedes E. Alejandro, Mahshid S. Azamian, Carlos A. Bacino, Ashok Balasubramanyam, Lindsay C. Burrage, Hsiao-Tuan Chao, Gary D. Clark, William J. Craigen, Hongzheng Dai, Shweta U. Dhar, Lisa T. Emrick, Alica M. Goldman, Neil A. Hanchard, Fariha Jamal, Lefkothea Karaviti, Seema R. Lalani, Brendan H. Lee, Richard A. Lewis, Ronit Marom, Paolo M. Moretti, David R. Murdock, Sarah K. Nicholas, James P. Orengo, Jennifer E. Posey, Lorraine Potocki, Jill A. Rosenfeld, Susan L. Samson, Daryl A. Scott, Alyssa A. Tran, Tiphanie P. Vogel, Michael F. Wangler, Shinya Yamamoto, Christine M. Eng, Pengfei Liu, Patricia A. Ward, Edward Behrens, Matthew Deardorff, Marni Falk, Kelly Hassey, Kathleen Sullivan, Adeline Vanderver, David B. Goldstein, Heidi Cope, Allyn McConkie-Rosell, Kelly Schoch, Vandana Shashi, Edward C. Smith, Rebecca C. Spillmann, Jennifer A. Sullivan, Queenie K.-G. Tan, Nicole M. Walley, Pankaj B. Agrawal, Alan H. Beggs, Gerard T. Berry, Lauren C. Briere, Laurel A. Cobban, Matthew Coggins, Cynthia M. Cooper, Elizabeth L. Fieg, Frances High, Ingrid A. Holm, Susan Korrick, Joel B. Krier, Sharyn A. Lincoln, Joseph Loscalzo, Richard L. Maas, Calum A. MacRae, J. Carl Pallais, Deepak A. Rao, Lance H. Rodan, Edwin K. Silverman, Joan M. Stoler, David A. Sweetser, Melissa Walker, Chris A. Walsh, Cecilia Esteves, Emily G. Kelley, Isaac S. Kohane, Kimberly LeBlanc, Alexa T. McCray, Anna Nagy, Surendra Dasari, Brendan C. Lanpher, Ian R. Lanza, Eva Morava, Devin Oglesbee, Guney Bademci, Deborah Barbouth, Stephanie Bivona, Olveen Carrasquillo, Ta Chen Peter Chang, Irman Forghani, Alana Grajewski, Rosario Isasi, Byron Lam, Roy Levitt, Xue Zhong Liu, Jacob McCauley, Ralph Sacco, Mario Saporta, Judy Schaechter, Mustafa Tekin, Fred Telischi, Willa Thorson, Stephan Zuchner, Heather A. Colley, Jyoti G. Dayal, David J. Eckstein, Laurie C. Findley, Donna M. Krasnewich, Laura A. Mamounas, Teri A. Manolio, John J. Mulvihill, Grace L. LaMoure, Madison P. Goldrich, Tiina K. Urv, Argenia L. Doss, Maria T. Acosta, Carsten Bonnenmann, Precilla D’Souza, David D. Draper, Carlos Ferreira, Rena A. Godfrey, Catherine A. Groden, Ellen F. Macnamara, Valerie V. Maduro, Thomas C. Markello, Avi Nath, Donna Novacic, Barbara N. Pusey, Camilo Toro, Colleen E. Wahl, Eva Baker, Elizabeth A. Burke, David R. Adams, William A. Gahl, May Christine V. Malicdan, Cynthia J. Tifft, Lynne A. Wolfe, John Yang, Bradley Power, Bernadette Gochuico, Laryssa Huryn, Lea Latham, Joie Davis, Deborah Mosbrook-Davis, Francis Rossignol, Ben Solomon, John MacDowall, Audrey Thurm, Wadih Zein, Muhammad Yousef, Margaret Adam, Laura Amendola, Michael Bamshad, Anita Beck, Jimmy Bennett, Beverly Berg-Rood, Elizabeth Blue, Brenna Boyd, Peter Byers, Sirisak Chanprasert, Michael Cunningham, Katrina Dipple, Daniel Doherty, Dawn Earl, Ian Glass, Katie Golden-Grant, Sihoun Hahn, Anne Hing, Fuki M. Hisama, Martha Horike-Pyne, Gail P. Jarvik, Jeffrey Jarvik, Suman Jayadev, Christina Lam, Kenneth Maravilla, Heather Mefford, J. Lawrence Merritt, Ghayda Mirzaa, Deborah Nickerson, Wendy Raskind, Natalie Rosenwasser, C. Ron Scott, Angela Sun, Virginia Sybert, Stephanie Wallace, Mark Wener, Tara Wenger, Euan A. Ashley, Gill Bejerano, Jonathan A. Bernstein, Devon Bonner, Terra R. Coakley, Liliana Fernandez, Paul G. Fisher, Laure Fresard, Jason Hom, Yong Huang, Jennefer N. Kohler, Elijah Kravets, Marta M. Majcherska, Beth A. Martin, Shruti Marwaha, Colleen E. McCormack, Archana N. Raja, Chloe M. Reuter, Maura Ruzhnikov, Jacinda B. Sampson, Kevin S. Smith, Shirley Sutton, Holly K. Tabor, Brianna M. Tucker, Matthew T. Wheeler, Diane B. Zastrow, Chunli Zhao, William E. Byrd, Andrew B. Crouse, Matthew Might, Mariko Nakano-Okuno, Jordan Whitlock, Gabrielle Brown, Manish J. Butte, Esteban C. Dell’Angelica, Naghmeh Dorrani, Emilie D. Douine, Brent L. Fogel, Irma Gutierrez, Alden Huang, Deborah Krakow, Hane Lee, Sandra K. Loo, Bryan C. Mak, Martin G. Martin, Julian A. Martínez-Agosto, Elisabeth McGee, Stanley F. Nelson, Shirley Nieves-Rodriguez, Christina G.S. Palmer, Jeanette C. Papp, Neil H. Parker, Genecee Renteria, Rebecca H. Signer, Janet S. Sinsheimer, Jijun Wan, Lee-kai Wang, Katherine Wesseling Perry, Jeremy D. Woods, Justin Alvey, Ashley Andrews, Jim Bale, John Bohnsack, Lorenzo Botto, John Carey, Laura Pace, Nicola Longo, Gabor Marth, Paolo Moretti, Aaron Quinlan, Matt Velinder, Dave Viskochil, Pinar Bayrak-Toydemir, Rong Mao, Monte Westerfield, Anna Bican, Elly Brokamp, Laura Duncan, Rizwan Hamid, Jennifer Kennedy, Mary Kozuira, John H. Newman, John A. Phillips, Lynette Rives, Amy K. Robertson, Emily Solem, Joy D. Cogan, F. Sessions Cole, Nichole Hayes, Dana Kiley, Kathy Sisco, Jennifer Wambach, Daniel Wegner, Dustin Baldridge, Stephen Pak, Timothy Schedl, Jimann Shin, Lilianna Solnica-Krezel, Quinten Waisfisz, Petra J.G. Zwijnenburg, Alban Ziegler, Magalie Barth, Rosemarie Smith, Sara Ellingwood, Deborah Gaebler-Spira, Somayeh Bakhtiari, Michael C. Kruer, Antoine H.C. van Kampen, Ronald J.A. Wanders, Hans R. Waterham, David Cassiman, and Frédéric M. Vaz. An autosomal dominant neurological disorder caused by de novo variants in far1 resulting in uncontrolled synthesis of ether lipids. Apr 2021. URL: https://doi.org/10.1038/s41436-020-01027-3, doi:10.1038/s41436-020-01027-3. This article has 50 citations and is from a highest quality peer-reviewed journal.

2. (ferdinandusse2021anautosomaldominant pages 4-5): Sacha Ferdinandusse, Kirsty McWalter, Heleen te Brinke, Lodewijk IJlst, Petra M. Mooijer, Jos P.N. Ruiter, Alida E.M. van Lint, Mia Pras-Raves, Eric Wever, Francisca Millan, Maria J. Guillen Sacoto, Amber Begtrup, Mark Tarnopolsky, Lauren Brady, Roger L. Ladda, Susan L. Sell, Catherine B. Nowak, Jessica Douglas, Cuixia Tian, Elizabeth Ulm, Seth Perlman, Arlene V. Drack, Karen Chong, Nicole Martin, Jennifer Brault, Elly Brokamp, Camilo Toro, William A. Gahl, Ellen F. Macnamara, Lynne Wolfe, Mercedes E. Alejandro, Mahshid S. Azamian, Carlos A. Bacino, Ashok Balasubramanyam, Lindsay C. Burrage, Hsiao-Tuan Chao, Gary D. Clark, William J. Craigen, Hongzheng Dai, Shweta U. Dhar, Lisa T. Emrick, Alica M. Goldman, Neil A. Hanchard, Fariha Jamal, Lefkothea Karaviti, Seema R. Lalani, Brendan H. Lee, Richard A. Lewis, Ronit Marom, Paolo M. Moretti, David R. Murdock, Sarah K. Nicholas, James P. Orengo, Jennifer E. Posey, Lorraine Potocki, Jill A. Rosenfeld, Susan L. Samson, Daryl A. Scott, Alyssa A. Tran, Tiphanie P. Vogel, Michael F. Wangler, Shinya Yamamoto, Christine M. Eng, Pengfei Liu, Patricia A. Ward, Edward Behrens, Matthew Deardorff, Marni Falk, Kelly Hassey, Kathleen Sullivan, Adeline Vanderver, David B. Goldstein, Heidi Cope, Allyn McConkie-Rosell, Kelly Schoch, Vandana Shashi, Edward C. Smith, Rebecca C. Spillmann, Jennifer A. Sullivan, Queenie K.-G. Tan, Nicole M. Walley, Pankaj B. Agrawal, Alan H. Beggs, Gerard T. Berry, Lauren C. Briere, Laurel A. Cobban, Matthew Coggins, Cynthia M. Cooper, Elizabeth L. Fieg, Frances High, Ingrid A. Holm, Susan Korrick, Joel B. Krier, Sharyn A. Lincoln, Joseph Loscalzo, Richard L. Maas, Calum A. MacRae, J. Carl Pallais, Deepak A. Rao, Lance H. Rodan, Edwin K. Silverman, Joan M. Stoler, David A. Sweetser, Melissa Walker, Chris A. Walsh, Cecilia Esteves, Emily G. Kelley, Isaac S. Kohane, Kimberly LeBlanc, Alexa T. McCray, Anna Nagy, Surendra Dasari, Brendan C. Lanpher, Ian R. Lanza, Eva Morava, Devin Oglesbee, Guney Bademci, Deborah Barbouth, Stephanie Bivona, Olveen Carrasquillo, Ta Chen Peter Chang, Irman Forghani, Alana Grajewski, Rosario Isasi, Byron Lam, Roy Levitt, Xue Zhong Liu, Jacob McCauley, Ralph Sacco, Mario Saporta, Judy Schaechter, Mustafa Tekin, Fred Telischi, Willa Thorson, Stephan Zuchner, Heather A. Colley, Jyoti G. Dayal, David J. Eckstein, Laurie C. Findley, Donna M. Krasnewich, Laura A. Mamounas, Teri A. Manolio, John J. Mulvihill, Grace L. LaMoure, Madison P. Goldrich, Tiina K. Urv, Argenia L. Doss, Maria T. Acosta, Carsten Bonnenmann, Precilla D’Souza, David D. Draper, Carlos Ferreira, Rena A. Godfrey, Catherine A. Groden, Ellen F. Macnamara, Valerie V. Maduro, Thomas C. Markello, Avi Nath, Donna Novacic, Barbara N. Pusey, Camilo Toro, Colleen E. Wahl, Eva Baker, Elizabeth A. Burke, David R. Adams, William A. Gahl, May Christine V. Malicdan, Cynthia J. Tifft, Lynne A. Wolfe, John Yang, Bradley Power, Bernadette Gochuico, Laryssa Huryn, Lea Latham, Joie Davis, Deborah Mosbrook-Davis, Francis Rossignol, Ben Solomon, John MacDowall, Audrey Thurm, Wadih Zein, Muhammad Yousef, Margaret Adam, Laura Amendola, Michael Bamshad, Anita Beck, Jimmy Bennett, Beverly Berg-Rood, Elizabeth Blue, Brenna Boyd, Peter Byers, Sirisak Chanprasert, Michael Cunningham, Katrina Dipple, Daniel Doherty, Dawn Earl, Ian Glass, Katie Golden-Grant, Sihoun Hahn, Anne Hing, Fuki M. Hisama, Martha Horike-Pyne, Gail P. Jarvik, Jeffrey Jarvik, Suman Jayadev, Christina Lam, Kenneth Maravilla, Heather Mefford, J. Lawrence Merritt, Ghayda Mirzaa, Deborah Nickerson, Wendy Raskind, Natalie Rosenwasser, C. Ron Scott, Angela Sun, Virginia Sybert, Stephanie Wallace, Mark Wener, Tara Wenger, Euan A. Ashley, Gill Bejerano, Jonathan A. Bernstein, Devon Bonner, Terra R. Coakley, Liliana Fernandez, Paul G. Fisher, Laure Fresard, Jason Hom, Yong Huang, Jennefer N. Kohler, Elijah Kravets, Marta M. Majcherska, Beth A. Martin, Shruti Marwaha, Colleen E. McCormack, Archana N. Raja, Chloe M. Reuter, Maura Ruzhnikov, Jacinda B. Sampson, Kevin S. Smith, Shirley Sutton, Holly K. Tabor, Brianna M. Tucker, Matthew T. Wheeler, Diane B. Zastrow, Chunli Zhao, William E. Byrd, Andrew B. Crouse, Matthew Might, Mariko Nakano-Okuno, Jordan Whitlock, Gabrielle Brown, Manish J. Butte, Esteban C. Dell’Angelica, Naghmeh Dorrani, Emilie D. Douine, Brent L. Fogel, Irma Gutierrez, Alden Huang, Deborah Krakow, Hane Lee, Sandra K. Loo, Bryan C. Mak, Martin G. Martin, Julian A. Martínez-Agosto, Elisabeth McGee, Stanley F. Nelson, Shirley Nieves-Rodriguez, Christina G.S. Palmer, Jeanette C. Papp, Neil H. Parker, Genecee Renteria, Rebecca H. Signer, Janet S. Sinsheimer, Jijun Wan, Lee-kai Wang, Katherine Wesseling Perry, Jeremy D. Woods, Justin Alvey, Ashley Andrews, Jim Bale, John Bohnsack, Lorenzo Botto, John Carey, Laura Pace, Nicola Longo, Gabor Marth, Paolo Moretti, Aaron Quinlan, Matt Velinder, Dave Viskochil, Pinar Bayrak-Toydemir, Rong Mao, Monte Westerfield, Anna Bican, Elly Brokamp, Laura Duncan, Rizwan Hamid, Jennifer Kennedy, Mary Kozuira, John H. Newman, John A. Phillips, Lynette Rives, Amy K. Robertson, Emily Solem, Joy D. Cogan, F. Sessions Cole, Nichole Hayes, Dana Kiley, Kathy Sisco, Jennifer Wambach, Daniel Wegner, Dustin Baldridge, Stephen Pak, Timothy Schedl, Jimann Shin, Lilianna Solnica-Krezel, Quinten Waisfisz, Petra J.G. Zwijnenburg, Alban Ziegler, Magalie Barth, Rosemarie Smith, Sara Ellingwood, Deborah Gaebler-Spira, Somayeh Bakhtiari, Michael C. Kruer, Antoine H.C. van Kampen, Ronald J.A. Wanders, Hans R. Waterham, David Cassiman, and Frédéric M. Vaz. An autosomal dominant neurological disorder caused by de novo variants in far1 resulting in uncontrolled synthesis of ether lipids. Apr 2021. URL: https://doi.org/10.1038/s41436-020-01027-3, doi:10.1038/s41436-020-01027-3. This article has 50 citations and is from a highest quality peer-reviewed journal.

3. (ferdinandusse2021anautosomaldominant pages 6-7): Sacha Ferdinandusse, Kirsty McWalter, Heleen te Brinke, Lodewijk IJlst, Petra M. Mooijer, Jos P.N. Ruiter, Alida E.M. van Lint, Mia Pras-Raves, Eric Wever, Francisca Millan, Maria J. Guillen Sacoto, Amber Begtrup, Mark Tarnopolsky, Lauren Brady, Roger L. Ladda, Susan L. Sell, Catherine B. Nowak, Jessica Douglas, Cuixia Tian, Elizabeth Ulm, Seth Perlman, Arlene V. Drack, Karen Chong, Nicole Martin, Jennifer Brault, Elly Brokamp, Camilo Toro, William A. Gahl, Ellen F. Macnamara, Lynne Wolfe, Mercedes E. Alejandro, Mahshid S. Azamian, Carlos A. Bacino, Ashok Balasubramanyam, Lindsay C. Burrage, Hsiao-Tuan Chao, Gary D. Clark, William J. Craigen, Hongzheng Dai, Shweta U. Dhar, Lisa T. Emrick, Alica M. Goldman, Neil A. Hanchard, Fariha Jamal, Lefkothea Karaviti, Seema R. Lalani, Brendan H. Lee, Richard A. Lewis, Ronit Marom, Paolo M. Moretti, David R. Murdock, Sarah K. Nicholas, James P. Orengo, Jennifer E. Posey, Lorraine Potocki, Jill A. Rosenfeld, Susan L. Samson, Daryl A. Scott, Alyssa A. Tran, Tiphanie P. Vogel, Michael F. Wangler, Shinya Yamamoto, Christine M. Eng, Pengfei Liu, Patricia A. Ward, Edward Behrens, Matthew Deardorff, Marni Falk, Kelly Hassey, Kathleen Sullivan, Adeline Vanderver, David B. Goldstein, Heidi Cope, Allyn McConkie-Rosell, Kelly Schoch, Vandana Shashi, Edward C. Smith, Rebecca C. Spillmann, Jennifer A. Sullivan, Queenie K.-G. Tan, Nicole M. Walley, Pankaj B. Agrawal, Alan H. Beggs, Gerard T. Berry, Lauren C. Briere, Laurel A. Cobban, Matthew Coggins, Cynthia M. Cooper, Elizabeth L. Fieg, Frances High, Ingrid A. Holm, Susan Korrick, Joel B. Krier, Sharyn A. Lincoln, Joseph Loscalzo, Richard L. Maas, Calum A. MacRae, J. Carl Pallais, Deepak A. Rao, Lance H. Rodan, Edwin K. Silverman, Joan M. Stoler, David A. Sweetser, Melissa Walker, Chris A. Walsh, Cecilia Esteves, Emily G. Kelley, Isaac S. Kohane, Kimberly LeBlanc, Alexa T. McCray, Anna Nagy, Surendra Dasari, Brendan C. Lanpher, Ian R. Lanza, Eva Morava, Devin Oglesbee, Guney Bademci, Deborah Barbouth, Stephanie Bivona, Olveen Carrasquillo, Ta Chen Peter Chang, Irman Forghani, Alana Grajewski, Rosario Isasi, Byron Lam, Roy Levitt, Xue Zhong Liu, Jacob McCauley, Ralph Sacco, Mario Saporta, Judy Schaechter, Mustafa Tekin, Fred Telischi, Willa Thorson, Stephan Zuchner, Heather A. Colley, Jyoti G. Dayal, David J. Eckstein, Laurie C. Findley, Donna M. Krasnewich, Laura A. Mamounas, Teri A. Manolio, John J. Mulvihill, Grace L. LaMoure, Madison P. Goldrich, Tiina K. Urv, Argenia L. Doss, Maria T. Acosta, Carsten Bonnenmann, Precilla D’Souza, David D. Draper, Carlos Ferreira, Rena A. Godfrey, Catherine A. Groden, Ellen F. Macnamara, Valerie V. Maduro, Thomas C. Markello, Avi Nath, Donna Novacic, Barbara N. Pusey, Camilo Toro, Colleen E. Wahl, Eva Baker, Elizabeth A. Burke, David R. Adams, William A. Gahl, May Christine V. Malicdan, Cynthia J. Tifft, Lynne A. Wolfe, John Yang, Bradley Power, Bernadette Gochuico, Laryssa Huryn, Lea Latham, Joie Davis, Deborah Mosbrook-Davis, Francis Rossignol, Ben Solomon, John MacDowall, Audrey Thurm, Wadih Zein, Muhammad Yousef, Margaret Adam, Laura Amendola, Michael Bamshad, Anita Beck, Jimmy Bennett, Beverly Berg-Rood, Elizabeth Blue, Brenna Boyd, Peter Byers, Sirisak Chanprasert, Michael Cunningham, Katrina Dipple, Daniel Doherty, Dawn Earl, Ian Glass, Katie Golden-Grant, Sihoun Hahn, Anne Hing, Fuki M. Hisama, Martha Horike-Pyne, Gail P. Jarvik, Jeffrey Jarvik, Suman Jayadev, Christina Lam, Kenneth Maravilla, Heather Mefford, J. Lawrence Merritt, Ghayda Mirzaa, Deborah Nickerson, Wendy Raskind, Natalie Rosenwasser, C. Ron Scott, Angela Sun, Virginia Sybert, Stephanie Wallace, Mark Wener, Tara Wenger, Euan A. Ashley, Gill Bejerano, Jonathan A. Bernstein, Devon Bonner, Terra R. Coakley, Liliana Fernandez, Paul G. Fisher, Laure Fresard, Jason Hom, Yong Huang, Jennefer N. Kohler, Elijah Kravets, Marta M. Majcherska, Beth A. Martin, Shruti Marwaha, Colleen E. McCormack, Archana N. Raja, Chloe M. Reuter, Maura Ruzhnikov, Jacinda B. Sampson, Kevin S. Smith, Shirley Sutton, Holly K. Tabor, Brianna M. Tucker, Matthew T. Wheeler, Diane B. Zastrow, Chunli Zhao, William E. Byrd, Andrew B. Crouse, Matthew Might, Mariko Nakano-Okuno, Jordan Whitlock, Gabrielle Brown, Manish J. Butte, Esteban C. Dell’Angelica, Naghmeh Dorrani, Emilie D. Douine, Brent L. Fogel, Irma Gutierrez, Alden Huang, Deborah Krakow, Hane Lee, Sandra K. Loo, Bryan C. Mak, Martin G. Martin, Julian A. Martínez-Agosto, Elisabeth McGee, Stanley F. Nelson, Shirley Nieves-Rodriguez, Christina G.S. Palmer, Jeanette C. Papp, Neil H. Parker, Genecee Renteria, Rebecca H. Signer, Janet S. Sinsheimer, Jijun Wan, Lee-kai Wang, Katherine Wesseling Perry, Jeremy D. Woods, Justin Alvey, Ashley Andrews, Jim Bale, John Bohnsack, Lorenzo Botto, John Carey, Laura Pace, Nicola Longo, Gabor Marth, Paolo Moretti, Aaron Quinlan, Matt Velinder, Dave Viskochil, Pinar Bayrak-Toydemir, Rong Mao, Monte Westerfield, Anna Bican, Elly Brokamp, Laura Duncan, Rizwan Hamid, Jennifer Kennedy, Mary Kozuira, John H. Newman, John A. Phillips, Lynette Rives, Amy K. Robertson, Emily Solem, Joy D. Cogan, F. Sessions Cole, Nichole Hayes, Dana Kiley, Kathy Sisco, Jennifer Wambach, Daniel Wegner, Dustin Baldridge, Stephen Pak, Timothy Schedl, Jimann Shin, Lilianna Solnica-Krezel, Quinten Waisfisz, Petra J.G. Zwijnenburg, Alban Ziegler, Magalie Barth, Rosemarie Smith, Sara Ellingwood, Deborah Gaebler-Spira, Somayeh Bakhtiari, Michael C. Kruer, Antoine H.C. van Kampen, Ronald J.A. Wanders, Hans R. Waterham, David Cassiman, and Frédéric M. Vaz. An autosomal dominant neurological disorder caused by de novo variants in far1 resulting in uncontrolled synthesis of ether lipids. Apr 2021. URL: https://doi.org/10.1038/s41436-020-01027-3, doi:10.1038/s41436-020-01027-3. This article has 50 citations and is from a highest quality peer-reviewed journal.

4. (ferdinandusse2021anautosomaldominant pages 3-4): Sacha Ferdinandusse, Kirsty McWalter, Heleen te Brinke, Lodewijk IJlst, Petra M. Mooijer, Jos P.N. Ruiter, Alida E.M. van Lint, Mia Pras-Raves, Eric Wever, Francisca Millan, Maria J. Guillen Sacoto, Amber Begtrup, Mark Tarnopolsky, Lauren Brady, Roger L. Ladda, Susan L. Sell, Catherine B. Nowak, Jessica Douglas, Cuixia Tian, Elizabeth Ulm, Seth Perlman, Arlene V. Drack, Karen Chong, Nicole Martin, Jennifer Brault, Elly Brokamp, Camilo Toro, William A. Gahl, Ellen F. Macnamara, Lynne Wolfe, Mercedes E. Alejandro, Mahshid S. Azamian, Carlos A. Bacino, Ashok Balasubramanyam, Lindsay C. Burrage, Hsiao-Tuan Chao, Gary D. Clark, William J. Craigen, Hongzheng Dai, Shweta U. Dhar, Lisa T. Emrick, Alica M. Goldman, Neil A. Hanchard, Fariha Jamal, Lefkothea Karaviti, Seema R. Lalani, Brendan H. Lee, Richard A. Lewis, Ronit Marom, Paolo M. Moretti, David R. Murdock, Sarah K. Nicholas, James P. Orengo, Jennifer E. Posey, Lorraine Potocki, Jill A. Rosenfeld, Susan L. Samson, Daryl A. Scott, Alyssa A. Tran, Tiphanie P. Vogel, Michael F. Wangler, Shinya Yamamoto, Christine M. Eng, Pengfei Liu, Patricia A. Ward, Edward Behrens, Matthew Deardorff, Marni Falk, Kelly Hassey, Kathleen Sullivan, Adeline Vanderver, David B. Goldstein, Heidi Cope, Allyn McConkie-Rosell, Kelly Schoch, Vandana Shashi, Edward C. Smith, Rebecca C. Spillmann, Jennifer A. Sullivan, Queenie K.-G. Tan, Nicole M. Walley, Pankaj B. Agrawal, Alan H. Beggs, Gerard T. Berry, Lauren C. Briere, Laurel A. Cobban, Matthew Coggins, Cynthia M. Cooper, Elizabeth L. Fieg, Frances High, Ingrid A. Holm, Susan Korrick, Joel B. Krier, Sharyn A. Lincoln, Joseph Loscalzo, Richard L. Maas, Calum A. MacRae, J. Carl Pallais, Deepak A. Rao, Lance H. Rodan, Edwin K. Silverman, Joan M. Stoler, David A. Sweetser, Melissa Walker, Chris A. Walsh, Cecilia Esteves, Emily G. Kelley, Isaac S. Kohane, Kimberly LeBlanc, Alexa T. McCray, Anna Nagy, Surendra Dasari, Brendan C. Lanpher, Ian R. Lanza, Eva Morava, Devin Oglesbee, Guney Bademci, Deborah Barbouth, Stephanie Bivona, Olveen Carrasquillo, Ta Chen Peter Chang, Irman Forghani, Alana Grajewski, Rosario Isasi, Byron Lam, Roy Levitt, Xue Zhong Liu, Jacob McCauley, Ralph Sacco, Mario Saporta, Judy Schaechter, Mustafa Tekin, Fred Telischi, Willa Thorson, Stephan Zuchner, Heather A. Colley, Jyoti G. Dayal, David J. Eckstein, Laurie C. Findley, Donna M. Krasnewich, Laura A. Mamounas, Teri A. Manolio, John J. Mulvihill, Grace L. LaMoure, Madison P. Goldrich, Tiina K. Urv, Argenia L. Doss, Maria T. Acosta, Carsten Bonnenmann, Precilla D’Souza, David D. Draper, Carlos Ferreira, Rena A. Godfrey, Catherine A. Groden, Ellen F. Macnamara, Valerie V. Maduro, Thomas C. Markello, Avi Nath, Donna Novacic, Barbara N. Pusey, Camilo Toro, Colleen E. Wahl, Eva Baker, Elizabeth A. Burke, David R. Adams, William A. Gahl, May Christine V. Malicdan, Cynthia J. Tifft, Lynne A. Wolfe, John Yang, Bradley Power, Bernadette Gochuico, Laryssa Huryn, Lea Latham, Joie Davis, Deborah Mosbrook-Davis, Francis Rossignol, Ben Solomon, John MacDowall, Audrey Thurm, Wadih Zein, Muhammad Yousef, Margaret Adam, Laura Amendola, Michael Bamshad, Anita Beck, Jimmy Bennett, Beverly Berg-Rood, Elizabeth Blue, Brenna Boyd, Peter Byers, Sirisak Chanprasert, Michael Cunningham, Katrina Dipple, Daniel Doherty, Dawn Earl, Ian Glass, Katie Golden-Grant, Sihoun Hahn, Anne Hing, Fuki M. Hisama, Martha Horike-Pyne, Gail P. Jarvik, Jeffrey Jarvik, Suman Jayadev, Christina Lam, Kenneth Maravilla, Heather Mefford, J. Lawrence Merritt, Ghayda Mirzaa, Deborah Nickerson, Wendy Raskind, Natalie Rosenwasser, C. Ron Scott, Angela Sun, Virginia Sybert, Stephanie Wallace, Mark Wener, Tara Wenger, Euan A. Ashley, Gill Bejerano, Jonathan A. Bernstein, Devon Bonner, Terra R. Coakley, Liliana Fernandez, Paul G. Fisher, Laure Fresard, Jason Hom, Yong Huang, Jennefer N. Kohler, Elijah Kravets, Marta M. Majcherska, Beth A. Martin, Shruti Marwaha, Colleen E. McCormack, Archana N. Raja, Chloe M. Reuter, Maura Ruzhnikov, Jacinda B. Sampson, Kevin S. Smith, Shirley Sutton, Holly K. Tabor, Brianna M. Tucker, Matthew T. Wheeler, Diane B. Zastrow, Chunli Zhao, William E. Byrd, Andrew B. Crouse, Matthew Might, Mariko Nakano-Okuno, Jordan Whitlock, Gabrielle Brown, Manish J. Butte, Esteban C. Dell’Angelica, Naghmeh Dorrani, Emilie D. Douine, Brent L. Fogel, Irma Gutierrez, Alden Huang, Deborah Krakow, Hane Lee, Sandra K. Loo, Bryan C. Mak, Martin G. Martin, Julian A. Martínez-Agosto, Elisabeth McGee, Stanley F. Nelson, Shirley Nieves-Rodriguez, Christina G.S. Palmer, Jeanette C. Papp, Neil H. Parker, Genecee Renteria, Rebecca H. Signer, Janet S. Sinsheimer, Jijun Wan, Lee-kai Wang, Katherine Wesseling Perry, Jeremy D. Woods, Justin Alvey, Ashley Andrews, Jim Bale, John Bohnsack, Lorenzo Botto, John Carey, Laura Pace, Nicola Longo, Gabor Marth, Paolo Moretti, Aaron Quinlan, Matt Velinder, Dave Viskochil, Pinar Bayrak-Toydemir, Rong Mao, Monte Westerfield, Anna Bican, Elly Brokamp, Laura Duncan, Rizwan Hamid, Jennifer Kennedy, Mary Kozuira, John H. Newman, John A. Phillips, Lynette Rives, Amy K. Robertson, Emily Solem, Joy D. Cogan, F. Sessions Cole, Nichole Hayes, Dana Kiley, Kathy Sisco, Jennifer Wambach, Daniel Wegner, Dustin Baldridge, Stephen Pak, Timothy Schedl, Jimann Shin, Lilianna Solnica-Krezel, Quinten Waisfisz, Petra J.G. Zwijnenburg, Alban Ziegler, Magalie Barth, Rosemarie Smith, Sara Ellingwood, Deborah Gaebler-Spira, Somayeh Bakhtiari, Michael C. Kruer, Antoine H.C. van Kampen, Ronald J.A. Wanders, Hans R. Waterham, David Cassiman, and Frédéric M. Vaz. An autosomal dominant neurological disorder caused by de novo variants in far1 resulting in uncontrolled synthesis of ether lipids. Apr 2021. URL: https://doi.org/10.1038/s41436-020-01027-3, doi:10.1038/s41436-020-01027-3. This article has 50 citations and is from a highest quality peer-reviewed journal.

5. (ferdinandusse2021anautosomaldominant pages 8-9): Sacha Ferdinandusse, Kirsty McWalter, Heleen te Brinke, Lodewijk IJlst, Petra M. Mooijer, Jos P.N. Ruiter, Alida E.M. van Lint, Mia Pras-Raves, Eric Wever, Francisca Millan, Maria J. Guillen Sacoto, Amber Begtrup, Mark Tarnopolsky, Lauren Brady, Roger L. Ladda, Susan L. Sell, Catherine B. Nowak, Jessica Douglas, Cuixia Tian, Elizabeth Ulm, Seth Perlman, Arlene V. Drack, Karen Chong, Nicole Martin, Jennifer Brault, Elly Brokamp, Camilo Toro, William A. Gahl, Ellen F. Macnamara, Lynne Wolfe, Mercedes E. Alejandro, Mahshid S. Azamian, Carlos A. Bacino, Ashok Balasubramanyam, Lindsay C. Burrage, Hsiao-Tuan Chao, Gary D. Clark, William J. Craigen, Hongzheng Dai, Shweta U. Dhar, Lisa T. Emrick, Alica M. Goldman, Neil A. Hanchard, Fariha Jamal, Lefkothea Karaviti, Seema R. Lalani, Brendan H. Lee, Richard A. Lewis, Ronit Marom, Paolo M. Moretti, David R. Murdock, Sarah K. Nicholas, James P. Orengo, Jennifer E. Posey, Lorraine Potocki, Jill A. Rosenfeld, Susan L. Samson, Daryl A. Scott, Alyssa A. Tran, Tiphanie P. Vogel, Michael F. Wangler, Shinya Yamamoto, Christine M. Eng, Pengfei Liu, Patricia A. Ward, Edward Behrens, Matthew Deardorff, Marni Falk, Kelly Hassey, Kathleen Sullivan, Adeline Vanderver, David B. Goldstein, Heidi Cope, Allyn McConkie-Rosell, Kelly Schoch, Vandana Shashi, Edward C. Smith, Rebecca C. Spillmann, Jennifer A. Sullivan, Queenie K.-G. Tan, Nicole M. Walley, Pankaj B. Agrawal, Alan H. Beggs, Gerard T. Berry, Lauren C. Briere, Laurel A. Cobban, Matthew Coggins, Cynthia M. Cooper, Elizabeth L. Fieg, Frances High, Ingrid A. Holm, Susan Korrick, Joel B. Krier, Sharyn A. Lincoln, Joseph Loscalzo, Richard L. Maas, Calum A. MacRae, J. Carl Pallais, Deepak A. Rao, Lance H. Rodan, Edwin K. Silverman, Joan M. Stoler, David A. Sweetser, Melissa Walker, Chris A. Walsh, Cecilia Esteves, Emily G. Kelley, Isaac S. Kohane, Kimberly LeBlanc, Alexa T. McCray, Anna Nagy, Surendra Dasari, Brendan C. Lanpher, Ian R. Lanza, Eva Morava, Devin Oglesbee, Guney Bademci, Deborah Barbouth, Stephanie Bivona, Olveen Carrasquillo, Ta Chen Peter Chang, Irman Forghani, Alana Grajewski, Rosario Isasi, Byron Lam, Roy Levitt, Xue Zhong Liu, Jacob McCauley, Ralph Sacco, Mario Saporta, Judy Schaechter, Mustafa Tekin, Fred Telischi, Willa Thorson, Stephan Zuchner, Heather A. Colley, Jyoti G. Dayal, David J. Eckstein, Laurie C. Findley, Donna M. Krasnewich, Laura A. Mamounas, Teri A. Manolio, John J. Mulvihill, Grace L. LaMoure, Madison P. Goldrich, Tiina K. Urv, Argenia L. Doss, Maria T. Acosta, Carsten Bonnenmann, Precilla D’Souza, David D. Draper, Carlos Ferreira, Rena A. Godfrey, Catherine A. Groden, Ellen F. Macnamara, Valerie V. Maduro, Thomas C. Markello, Avi Nath, Donna Novacic, Barbara N. Pusey, Camilo Toro, Colleen E. Wahl, Eva Baker, Elizabeth A. Burke, David R. Adams, William A. Gahl, May Christine V. Malicdan, Cynthia J. Tifft, Lynne A. Wolfe, John Yang, Bradley Power, Bernadette Gochuico, Laryssa Huryn, Lea Latham, Joie Davis, Deborah Mosbrook-Davis, Francis Rossignol, Ben Solomon, John MacDowall, Audrey Thurm, Wadih Zein, Muhammad Yousef, Margaret Adam, Laura Amendola, Michael Bamshad, Anita Beck, Jimmy Bennett, Beverly Berg-Rood, Elizabeth Blue, Brenna Boyd, Peter Byers, Sirisak Chanprasert, Michael Cunningham, Katrina Dipple, Daniel Doherty, Dawn Earl, Ian Glass, Katie Golden-Grant, Sihoun Hahn, Anne Hing, Fuki M. Hisama, Martha Horike-Pyne, Gail P. Jarvik, Jeffrey Jarvik, Suman Jayadev, Christina Lam, Kenneth Maravilla, Heather Mefford, J. Lawrence Merritt, Ghayda Mirzaa, Deborah Nickerson, Wendy Raskind, Natalie Rosenwasser, C. Ron Scott, Angela Sun, Virginia Sybert, Stephanie Wallace, Mark Wener, Tara Wenger, Euan A. Ashley, Gill Bejerano, Jonathan A. Bernstein, Devon Bonner, Terra R. Coakley, Liliana Fernandez, Paul G. Fisher, Laure Fresard, Jason Hom, Yong Huang, Jennefer N. Kohler, Elijah Kravets, Marta M. Majcherska, Beth A. Martin, Shruti Marwaha, Colleen E. McCormack, Archana N. Raja, Chloe M. Reuter, Maura Ruzhnikov, Jacinda B. Sampson, Kevin S. Smith, Shirley Sutton, Holly K. Tabor, Brianna M. Tucker, Matthew T. Wheeler, Diane B. Zastrow, Chunli Zhao, William E. Byrd, Andrew B. Crouse, Matthew Might, Mariko Nakano-Okuno, Jordan Whitlock, Gabrielle Brown, Manish J. Butte, Esteban C. Dell’Angelica, Naghmeh Dorrani, Emilie D. Douine, Brent L. Fogel, Irma Gutierrez, Alden Huang, Deborah Krakow, Hane Lee, Sandra K. Loo, Bryan C. Mak, Martin G. Martin, Julian A. Martínez-Agosto, Elisabeth McGee, Stanley F. Nelson, Shirley Nieves-Rodriguez, Christina G.S. Palmer, Jeanette C. Papp, Neil H. Parker, Genecee Renteria, Rebecca H. Signer, Janet S. Sinsheimer, Jijun Wan, Lee-kai Wang, Katherine Wesseling Perry, Jeremy D. Woods, Justin Alvey, Ashley Andrews, Jim Bale, John Bohnsack, Lorenzo Botto, John Carey, Laura Pace, Nicola Longo, Gabor Marth, Paolo Moretti, Aaron Quinlan, Matt Velinder, Dave Viskochil, Pinar Bayrak-Toydemir, Rong Mao, Monte Westerfield, Anna Bican, Elly Brokamp, Laura Duncan, Rizwan Hamid, Jennifer Kennedy, Mary Kozuira, John H. Newman, John A. Phillips, Lynette Rives, Amy K. Robertson, Emily Solem, Joy D. Cogan, F. Sessions Cole, Nichole Hayes, Dana Kiley, Kathy Sisco, Jennifer Wambach, Daniel Wegner, Dustin Baldridge, Stephen Pak, Timothy Schedl, Jimann Shin, Lilianna Solnica-Krezel, Quinten Waisfisz, Petra J.G. Zwijnenburg, Alban Ziegler, Magalie Barth, Rosemarie Smith, Sara Ellingwood, Deborah Gaebler-Spira, Somayeh Bakhtiari, Michael C. Kruer, Antoine H.C. van Kampen, Ronald J.A. Wanders, Hans R. Waterham, David Cassiman, and Frédéric M. Vaz. An autosomal dominant neurological disorder caused by de novo variants in far1 resulting in uncontrolled synthesis of ether lipids. Apr 2021. URL: https://doi.org/10.1038/s41436-020-01027-3, doi:10.1038/s41436-020-01027-3. This article has 50 citations and is from a highest quality peer-reviewed journal.

6. (ferdinandusse2021anautosomaldominant pages 9-10): Sacha Ferdinandusse, Kirsty McWalter, Heleen te Brinke, Lodewijk IJlst, Petra M. Mooijer, Jos P.N. Ruiter, Alida E.M. van Lint, Mia Pras-Raves, Eric Wever, Francisca Millan, Maria J. Guillen Sacoto, Amber Begtrup, Mark Tarnopolsky, Lauren Brady, Roger L. Ladda, Susan L. Sell, Catherine B. Nowak, Jessica Douglas, Cuixia Tian, Elizabeth Ulm, Seth Perlman, Arlene V. Drack, Karen Chong, Nicole Martin, Jennifer Brault, Elly Brokamp, Camilo Toro, William A. Gahl, Ellen F. Macnamara, Lynne Wolfe, Mercedes E. Alejandro, Mahshid S. Azamian, Carlos A. Bacino, Ashok Balasubramanyam, Lindsay C. Burrage, Hsiao-Tuan Chao, Gary D. Clark, William J. Craigen, Hongzheng Dai, Shweta U. Dhar, Lisa T. Emrick, Alica M. Goldman, Neil A. Hanchard, Fariha Jamal, Lefkothea Karaviti, Seema R. Lalani, Brendan H. Lee, Richard A. Lewis, Ronit Marom, Paolo M. Moretti, David R. Murdock, Sarah K. Nicholas, James P. Orengo, Jennifer E. Posey, Lorraine Potocki, Jill A. Rosenfeld, Susan L. Samson, Daryl A. Scott, Alyssa A. Tran, Tiphanie P. Vogel, Michael F. Wangler, Shinya Yamamoto, Christine M. Eng, Pengfei Liu, Patricia A. Ward, Edward Behrens, Matthew Deardorff, Marni Falk, Kelly Hassey, Kathleen Sullivan, Adeline Vanderver, David B. Goldstein, Heidi Cope, Allyn McConkie-Rosell, Kelly Schoch, Vandana Shashi, Edward C. Smith, Rebecca C. Spillmann, Jennifer A. Sullivan, Queenie K.-G. Tan, Nicole M. Walley, Pankaj B. Agrawal, Alan H. Beggs, Gerard T. Berry, Lauren C. Briere, Laurel A. Cobban, Matthew Coggins, Cynthia M. Cooper, Elizabeth L. Fieg, Frances High, Ingrid A. Holm, Susan Korrick, Joel B. Krier, Sharyn A. Lincoln, Joseph Loscalzo, Richard L. Maas, Calum A. MacRae, J. Carl Pallais, Deepak A. Rao, Lance H. Rodan, Edwin K. Silverman, Joan M. Stoler, David A. Sweetser, Melissa Walker, Chris A. Walsh, Cecilia Esteves, Emily G. Kelley, Isaac S. Kohane, Kimberly LeBlanc, Alexa T. McCray, Anna Nagy, Surendra Dasari, Brendan C. Lanpher, Ian R. Lanza, Eva Morava, Devin Oglesbee, Guney Bademci, Deborah Barbouth, Stephanie Bivona, Olveen Carrasquillo, Ta Chen Peter Chang, Irman Forghani, Alana Grajewski, Rosario Isasi, Byron Lam, Roy Levitt, Xue Zhong Liu, Jacob McCauley, Ralph Sacco, Mario Saporta, Judy Schaechter, Mustafa Tekin, Fred Telischi, Willa Thorson, Stephan Zuchner, Heather A. Colley, Jyoti G. Dayal, David J. Eckstein, Laurie C. Findley, Donna M. Krasnewich, Laura A. Mamounas, Teri A. Manolio, John J. Mulvihill, Grace L. LaMoure, Madison P. Goldrich, Tiina K. Urv, Argenia L. Doss, Maria T. Acosta, Carsten Bonnenmann, Precilla D’Souza, David D. Draper, Carlos Ferreira, Rena A. Godfrey, Catherine A. Groden, Ellen F. Macnamara, Valerie V. Maduro, Thomas C. Markello, Avi Nath, Donna Novacic, Barbara N. Pusey, Camilo Toro, Colleen E. Wahl, Eva Baker, Elizabeth A. Burke, David R. Adams, William A. Gahl, May Christine V. Malicdan, Cynthia J. Tifft, Lynne A. Wolfe, John Yang, Bradley Power, Bernadette Gochuico, Laryssa Huryn, Lea Latham, Joie Davis, Deborah Mosbrook-Davis, Francis Rossignol, Ben Solomon, John MacDowall, Audrey Thurm, Wadih Zein, Muhammad Yousef, Margaret Adam, Laura Amendola, Michael Bamshad, Anita Beck, Jimmy Bennett, Beverly Berg-Rood, Elizabeth Blue, Brenna Boyd, Peter Byers, Sirisak Chanprasert, Michael Cunningham, Katrina Dipple, Daniel Doherty, Dawn Earl, Ian Glass, Katie Golden-Grant, Sihoun Hahn, Anne Hing, Fuki M. Hisama, Martha Horike-Pyne, Gail P. Jarvik, Jeffrey Jarvik, Suman Jayadev, Christina Lam, Kenneth Maravilla, Heather Mefford, J. Lawrence Merritt, Ghayda Mirzaa, Deborah Nickerson, Wendy Raskind, Natalie Rosenwasser, C. Ron Scott, Angela Sun, Virginia Sybert, Stephanie Wallace, Mark Wener, Tara Wenger, Euan A. Ashley, Gill Bejerano, Jonathan A. Bernstein, Devon Bonner, Terra R. Coakley, Liliana Fernandez, Paul G. Fisher, Laure Fresard, Jason Hom, Yong Huang, Jennefer N. Kohler, Elijah Kravets, Marta M. Majcherska, Beth A. Martin, Shruti Marwaha, Colleen E. McCormack, Archana N. Raja, Chloe M. Reuter, Maura Ruzhnikov, Jacinda B. Sampson, Kevin S. Smith, Shirley Sutton, Holly K. Tabor, Brianna M. Tucker, Matthew T. Wheeler, Diane B. Zastrow, Chunli Zhao, William E. Byrd, Andrew B. Crouse, Matthew Might, Mariko Nakano-Okuno, Jordan Whitlock, Gabrielle Brown, Manish J. Butte, Esteban C. Dell’Angelica, Naghmeh Dorrani, Emilie D. Douine, Brent L. Fogel, Irma Gutierrez, Alden Huang, Deborah Krakow, Hane Lee, Sandra K. Loo, Bryan C. Mak, Martin G. Martin, Julian A. Martínez-Agosto, Elisabeth McGee, Stanley F. Nelson, Shirley Nieves-Rodriguez, Christina G.S. Palmer, Jeanette C. Papp, Neil H. Parker, Genecee Renteria, Rebecca H. Signer, Janet S. Sinsheimer, Jijun Wan, Lee-kai Wang, Katherine Wesseling Perry, Jeremy D. Woods, Justin Alvey, Ashley Andrews, Jim Bale, John Bohnsack, Lorenzo Botto, John Carey, Laura Pace, Nicola Longo, Gabor Marth, Paolo Moretti, Aaron Quinlan, Matt Velinder, Dave Viskochil, Pinar Bayrak-Toydemir, Rong Mao, Monte Westerfield, Anna Bican, Elly Brokamp, Laura Duncan, Rizwan Hamid, Jennifer Kennedy, Mary Kozuira, John H. Newman, John A. Phillips, Lynette Rives, Amy K. Robertson, Emily Solem, Joy D. Cogan, F. Sessions Cole, Nichole Hayes, Dana Kiley, Kathy Sisco, Jennifer Wambach, Daniel Wegner, Dustin Baldridge, Stephen Pak, Timothy Schedl, Jimann Shin, Lilianna Solnica-Krezel, Quinten Waisfisz, Petra J.G. Zwijnenburg, Alban Ziegler, Magalie Barth, Rosemarie Smith, Sara Ellingwood, Deborah Gaebler-Spira, Somayeh Bakhtiari, Michael C. Kruer, Antoine H.C. van Kampen, Ronald J.A. Wanders, Hans R. Waterham, David Cassiman, and Frédéric M. Vaz. An autosomal dominant neurological disorder caused by de novo variants in far1 resulting in uncontrolled synthesis of ether lipids. Apr 2021. URL: https://doi.org/10.1038/s41436-020-01027-3, doi:10.1038/s41436-020-01027-3. This article has 50 citations and is from a highest quality peer-reviewed journal.

7. (ferdinandusse2021anautosomaldominant pages 2-3): Sacha Ferdinandusse, Kirsty McWalter, Heleen te Brinke, Lodewijk IJlst, Petra M. Mooijer, Jos P.N. Ruiter, Alida E.M. van Lint, Mia Pras-Raves, Eric Wever, Francisca Millan, Maria J. Guillen Sacoto, Amber Begtrup, Mark Tarnopolsky, Lauren Brady, Roger L. Ladda, Susan L. Sell, Catherine B. Nowak, Jessica Douglas, Cuixia Tian, Elizabeth Ulm, Seth Perlman, Arlene V. Drack, Karen Chong, Nicole Martin, Jennifer Brault, Elly Brokamp, Camilo Toro, William A. Gahl, Ellen F. Macnamara, Lynne Wolfe, Mercedes E. Alejandro, Mahshid S. Azamian, Carlos A. Bacino, Ashok Balasubramanyam, Lindsay C. Burrage, Hsiao-Tuan Chao, Gary D. Clark, William J. Craigen, Hongzheng Dai, Shweta U. Dhar, Lisa T. Emrick, Alica M. Goldman, Neil A. Hanchard, Fariha Jamal, Lefkothea Karaviti, Seema R. Lalani, Brendan H. Lee, Richard A. Lewis, Ronit Marom, Paolo M. Moretti, David R. Murdock, Sarah K. Nicholas, James P. Orengo, Jennifer E. Posey, Lorraine Potocki, Jill A. Rosenfeld, Susan L. Samson, Daryl A. Scott, Alyssa A. Tran, Tiphanie P. Vogel, Michael F. Wangler, Shinya Yamamoto, Christine M. Eng, Pengfei Liu, Patricia A. Ward, Edward Behrens, Matthew Deardorff, Marni Falk, Kelly Hassey, Kathleen Sullivan, Adeline Vanderver, David B. Goldstein, Heidi Cope, Allyn McConkie-Rosell, Kelly Schoch, Vandana Shashi, Edward C. Smith, Rebecca C. Spillmann, Jennifer A. Sullivan, Queenie K.-G. Tan, Nicole M. Walley, Pankaj B. Agrawal, Alan H. Beggs, Gerard T. Berry, Lauren C. Briere, Laurel A. Cobban, Matthew Coggins, Cynthia M. Cooper, Elizabeth L. Fieg, Frances High, Ingrid A. Holm, Susan Korrick, Joel B. Krier, Sharyn A. Lincoln, Joseph Loscalzo, Richard L. Maas, Calum A. MacRae, J. Carl Pallais, Deepak A. Rao, Lance H. Rodan, Edwin K. Silverman, Joan M. Stoler, David A. Sweetser, Melissa Walker, Chris A. Walsh, Cecilia Esteves, Emily G. Kelley, Isaac S. Kohane, Kimberly LeBlanc, Alexa T. McCray, Anna Nagy, Surendra Dasari, Brendan C. Lanpher, Ian R. Lanza, Eva Morava, Devin Oglesbee, Guney Bademci, Deborah Barbouth, Stephanie Bivona, Olveen Carrasquillo, Ta Chen Peter Chang, Irman Forghani, Alana Grajewski, Rosario Isasi, Byron Lam, Roy Levitt, Xue Zhong Liu, Jacob McCauley, Ralph Sacco, Mario Saporta, Judy Schaechter, Mustafa Tekin, Fred Telischi, Willa Thorson, Stephan Zuchner, Heather A. Colley, Jyoti G. Dayal, David J. Eckstein, Laurie C. Findley, Donna M. Krasnewich, Laura A. Mamounas, Teri A. Manolio, John J. Mulvihill, Grace L. LaMoure, Madison P. Goldrich, Tiina K. Urv, Argenia L. Doss, Maria T. Acosta, Carsten Bonnenmann, Precilla D’Souza, David D. Draper, Carlos Ferreira, Rena A. Godfrey, Catherine A. Groden, Ellen F. Macnamara, Valerie V. Maduro, Thomas C. Markello, Avi Nath, Donna Novacic, Barbara N. Pusey, Camilo Toro, Colleen E. Wahl, Eva Baker, Elizabeth A. Burke, David R. Adams, William A. Gahl, May Christine V. Malicdan, Cynthia J. Tifft, Lynne A. Wolfe, John Yang, Bradley Power, Bernadette Gochuico, Laryssa Huryn, Lea Latham, Joie Davis, Deborah Mosbrook-Davis, Francis Rossignol, Ben Solomon, John MacDowall, Audrey Thurm, Wadih Zein, Muhammad Yousef, Margaret Adam, Laura Amendola, Michael Bamshad, Anita Beck, Jimmy Bennett, Beverly Berg-Rood, Elizabeth Blue, Brenna Boyd, Peter Byers, Sirisak Chanprasert, Michael Cunningham, Katrina Dipple, Daniel Doherty, Dawn Earl, Ian Glass, Katie Golden-Grant, Sihoun Hahn, Anne Hing, Fuki M. Hisama, Martha Horike-Pyne, Gail P. Jarvik, Jeffrey Jarvik, Suman Jayadev, Christina Lam, Kenneth Maravilla, Heather Mefford, J. Lawrence Merritt, Ghayda Mirzaa, Deborah Nickerson, Wendy Raskind, Natalie Rosenwasser, C. Ron Scott, Angela Sun, Virginia Sybert, Stephanie Wallace, Mark Wener, Tara Wenger, Euan A. Ashley, Gill Bejerano, Jonathan A. Bernstein, Devon Bonner, Terra R. Coakley, Liliana Fernandez, Paul G. Fisher, Laure Fresard, Jason Hom, Yong Huang, Jennefer N. Kohler, Elijah Kravets, Marta M. Majcherska, Beth A. Martin, Shruti Marwaha, Colleen E. McCormack, Archana N. Raja, Chloe M. Reuter, Maura Ruzhnikov, Jacinda B. Sampson, Kevin S. Smith, Shirley Sutton, Holly K. Tabor, Brianna M. Tucker, Matthew T. Wheeler, Diane B. Zastrow, Chunli Zhao, William E. Byrd, Andrew B. Crouse, Matthew Might, Mariko Nakano-Okuno, Jordan Whitlock, Gabrielle Brown, Manish J. Butte, Esteban C. Dell’Angelica, Naghmeh Dorrani, Emilie D. Douine, Brent L. Fogel, Irma Gutierrez, Alden Huang, Deborah Krakow, Hane Lee, Sandra K. Loo, Bryan C. Mak, Martin G. Martin, Julian A. Martínez-Agosto, Elisabeth McGee, Stanley F. Nelson, Shirley Nieves-Rodriguez, Christina G.S. Palmer, Jeanette C. Papp, Neil H. Parker, Genecee Renteria, Rebecca H. Signer, Janet S. Sinsheimer, Jijun Wan, Lee-kai Wang, Katherine Wesseling Perry, Jeremy D. Woods, Justin Alvey, Ashley Andrews, Jim Bale, John Bohnsack, Lorenzo Botto, John Carey, Laura Pace, Nicola Longo, Gabor Marth, Paolo Moretti, Aaron Quinlan, Matt Velinder, Dave Viskochil, Pinar Bayrak-Toydemir, Rong Mao, Monte Westerfield, Anna Bican, Elly Brokamp, Laura Duncan, Rizwan Hamid, Jennifer Kennedy, Mary Kozuira, John H. Newman, John A. Phillips, Lynette Rives, Amy K. Robertson, Emily Solem, Joy D. Cogan, F. Sessions Cole, Nichole Hayes, Dana Kiley, Kathy Sisco, Jennifer Wambach, Daniel Wegner, Dustin Baldridge, Stephen Pak, Timothy Schedl, Jimann Shin, Lilianna Solnica-Krezel, Quinten Waisfisz, Petra J.G. Zwijnenburg, Alban Ziegler, Magalie Barth, Rosemarie Smith, Sara Ellingwood, Deborah Gaebler-Spira, Somayeh Bakhtiari, Michael C. Kruer, Antoine H.C. van Kampen, Ronald J.A. Wanders, Hans R. Waterham, David Cassiman, and Frédéric M. Vaz. An autosomal dominant neurological disorder caused by de novo variants in far1 resulting in uncontrolled synthesis of ether lipids. Apr 2021. URL: https://doi.org/10.1038/s41436-020-01027-3, doi:10.1038/s41436-020-01027-3. This article has 50 citations and is from a highest quality peer-reviewed journal.

8. (honsho2023regulationofplasmalogen pages 1-3): Masanori Honsho and Yukio Fujiki. Regulation of plasmalogen biosynthesis in mammalian cells and tissues. Mar 2023. URL: https://doi.org/10.1016/j.brainresbull.2023.01.011, doi:10.1016/j.brainresbull.2023.01.011. This article has 38 citations and is from a peer-reviewed journal.

9. (honsho2023regulationofplasmalogen pages 3-5): Masanori Honsho and Yukio Fujiki. Regulation of plasmalogen biosynthesis in mammalian cells and tissues. Mar 2023. URL: https://doi.org/10.1016/j.brainresbull.2023.01.011, doi:10.1016/j.brainresbull.2023.01.011. This article has 38 citations and is from a peer-reviewed journal.

10. (honsho2023regulationofplasmalogen pages 5-7): Masanori Honsho and Yukio Fujiki. Regulation of plasmalogen biosynthesis in mammalian cells and tissues. Mar 2023. URL: https://doi.org/10.1016/j.brainresbull.2023.01.011, doi:10.1016/j.brainresbull.2023.01.011. This article has 38 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Spastic_Paraparesis-cataracts-speech_Delay_Syndrome-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 1 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0036212` (2 mentions) - the report calls it "if available"; MONDO calls it **spastic paraparesis-cataracts-speech delay syndrome**