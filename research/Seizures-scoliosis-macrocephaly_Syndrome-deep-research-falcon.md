---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-28T19:02:20.467109'
end_time: '2026-08-28T19:22:02.446501'
duration_seconds: 1181.98
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: seizures-scoliosis-macrocephaly syndrome (SSMS, biallelic EXT2 - the
    autosomal recessive phenotype, NOT dominant hereditary multiple exostoses)
  mondo_id: MONDO:0014731
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 25
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 5
  off_topic: 1
  off_topic_references:
  - DOI:10.1038/s41467-024-45419-4
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 54
  verified: 54
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0014731
    reported_labels:
    - if available
    ontology_label: seizures-scoliosis-macrocephaly syndrome
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Seizures-scoliosis-macrocephaly_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** seizures-scoliosis-macrocephaly syndrome (SSMS, biallelic EXT2 - the autosomal recessive phenotype, NOT dominant hereditary multiple exostoses)
- **MONDO ID:** MONDO:0014731 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **seizures-scoliosis-macrocephaly syndrome (SSMS, biallelic EXT2 - the autosomal recessive phenotype, NOT dominant hereditary multiple exostoses)** covering all of the
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
- **Disease Name:** seizures-scoliosis-macrocephaly syndrome (SSMS, biallelic EXT2 - the autosomal recessive phenotype, NOT dominant hereditary multiple exostoses)
- **MONDO ID:** MONDO:0014731 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **seizures-scoliosis-macrocephaly syndrome (SSMS, biallelic EXT2 - the autosomal recessive phenotype, NOT dominant hereditary multiple exostoses)** covering all of the
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


# Seizures–scoliosis–macrocephaly syndrome (SSMS)
## Biallelic **EXT2** / autosomal-recessive EXT2-related syndrome (AREXT2)

## Executive summary

SSMS is an ultra-rare, autosomal-recessive developmental disorder caused by **biallelic hypomorphic EXT2 variants**. It is characterized primarily by developmental/intellectual disability, epilepsy, abnormal head size, hypotonia, spinal deformity and dysmorphic features, with variable gastrointestinal, cardiac, renal, behavioral and growth abnormalities. “Autosomal-recessive EXT2-related syndrome” (**AREXT2**) is the broader and increasingly appropriate label because later families do not invariably have all three eponymous findings: microcephaly rather than macrocephaly and absence of scoliosis have both been reported. The defining distinction is from **autosomal-dominant hereditary multiple exostoses type 2**: osteochondromas are not a defining feature of AREXT2 and were specifically absent in the original family. (jaeken2020congenitaldisordersof pages 4-5, mizumoto2021congenitaldisordersof pages 12-13, gupta2019developmentaldelaycoarse pages 1-2, gupta2019developmentaldelaycoarse pages 2-4)

The evidence base remains exceptionally small. The foundational report was Farhan et al., published August 2015 (J Med Genet 52:666–675; PMID **26246518**; DOI/URL: https://doi.org/10.1136/jmedgenet-2015-103279). Subsequent informative reports include El-Bazzal et al. (2018; DOI: https://doi.org/10.1016/j.ejmg.2018.07.025), Gentile et al. (online 2018/issue 2019; DOI: https://doi.org/10.1111/cge.13458), Gupta et al. (accepted January 8, 2019; DOI: https://doi.org/10.1002/ccr3.2010), and Sabir et al. (2022; DOI: https://doi.org/10.1097/MCD.0000000000000406). No disease-specific clinical study published in 2023–2024 was identified in the searches performed for this report. The main relevant 2024 advance is structural work on the interacting HS-modification enzyme NDST1, not new SSMS natural-history or treatment evidence. (OpenTargets Search: seizures-scoliosis-macrocephaly syndrome-EXT2, gupta2019developmentaldelaycoarse pages 1-2, gupta2019developmentaldelaycoarse pages 5-6)

> **Key primary-source abstract quotation (Gupta et al., 2019):** “We report a patient with developmental delay, autism, epilepsy, macrocephaly, facial dysmorphism, gastrointestinal, and behavioral issues due to EXT2 compound heterozygous likely pathogenic variants.” (gupta2019developmentaldelaycoarse pages 1-2)

The available human cohorts and their evidentiary limitations are summarized below.

| Publication / cohort | Family / patients | EXT2 genotype | Key phenotype and onset | Major outcomes | Evidence caveats |
|---|---|---|---|---|---|
| Farhan et al., 2015; J Med Genet 52:666-675; PMID: 26246518; DOI: 10.1136/jmedgenet-2015-103279 | 1 Old Order Mennonite family; 4 affected siblings (3M, 1F), assessed ages reported in later summaries/thesis as ~10-19 years | Complex homozygous missense variants: p.Met87Arg and p.Arg95Cys; family segregated with recessive disease | Core SSMS phenotype: developmental delay/intellectual disability, hypotonia, seizures with onset ~2.5-5 years, macrocephaly, scoliosis/kyphosis, hypertelorism; additional renal/GI/cardiac findings in some; exostoses specifically absent (mizumoto2018defectsinbiosynthesis pages 13-14, mizumoto2021congenitaldisordersof pages 12-13, farhan2016genediscoveryin pages 110-114, farhan2016genediscoveryina pages 110-114) | Severe variable course: one patient died after status epilepticus at 17; one had prolonged seizure/status with hemiplegic stroke and wheelchair dependence; one had renal failure; patient fibroblasts showed reduced EXT2 protein/transcript and abolished NDST1 protein (farhan2016genediscoveryina pages 123-130, farhan2016genediscoveryin pages 110-114, farhan2016genediscoveryina pages 110-114) | Most granular clinical detail available from thesis/review excerpts rather than full 2015 paper text in retrieved context; some ages differ across excerpt types because thesis followed patients longer (farhan2016genediscoveryina pages 123-130, farhan2016genediscoveryina pages 131-135, farhan2016genediscoveryin pages 110-114, farhan2016genediscoveryina pages 110-114) |
| El-Bazzal et al., 2018; Eur J Med Genet, cited in Gupta 2019; DOI reported as 10.1016/j.ejmg.2018.07.025 | 1 family; 2 brothers | Homozygous p.Ser4Leu (c.11C>T) | Severe developmental delay, seizures, feeding difficulties, microcephaly rather than macrocephaly/normal head size in later AREXT2 spectrum summaries; facial flattening/coarse features summarized in comparison table; exostoses absent in AREXT2 framing (gupta2019developmentaldelaycoarse pages 4-5, gupta2019developmentaldelaycoarse pages 5-6) | Expanded phenotype toward more severe neurodevelopmental disease; both boys alive at reported ages 6 and 8 in comparison table (gupta2019developmentaldelaycoarse pages 4-5) | Direct article text was not retrieved; details come from Gupta 2019 comparison table/citation trail, so onset specifics and full systems review should be treated as second-hand summary (gupta2019developmentaldelaycoarse pages 4-5, gupta2019developmentaldelaycoarse pages 5-6) |
| Gentile et al., 2019; Clin Genet 95:165-171; DOI: 10.1111/cge.13458 | 1 family; 2 affected relatives/patients (F15, M21 in Gupta comparison table) | Compound heterozygous missense variants p.Asp227Asn and p.Tyr608Cys | Intellectual disability/developmental delay, seizures in one or both, macrocephaly reported as “high” head size in comparison table, facial dysmorphism; phenotype milder/variable compared with founder family; exostoses not reported as present in AREXT2 summaries (gupta2019developmentaldelaycoarse pages 4-5, gupta2019developmentaldelaycoarse pages 5-6) | Survived into adolescence/adulthood (15 and 21 years in comparison table), supporting variable severity and nonlethal course in some genotypes (gupta2019developmentaldelaycoarse pages 4-5) | Full paper not retrieved; patient-level details limited to secondary table excerpt and review mentions, so seizure onset/treatment/systemic findings cannot be stated with confidence here (gupta2019developmentaldelaycoarse pages 4-5, gupta2019developmentaldelaycoarse pages 5-6) |
| Gupta et al., 2019; Clin Case Rep 7:632-637; DOI: 10.1002/ccr3.2010 | 1 nonconsanguineous family; proband F14 plus mildly affected fraternal twin sister; unaffected brother carried only one paternal EXT2 variant | Compound heterozygous EXT2 p.Val373Asp (c.1118T>A) and p.Thr672Met (c.2015C>T); both sisters also carried heterozygous NDST1 p.Arg454Cys VUS | Proband: developmental delay during first 2 years, regression at 27 months, autism, macrocephaly, hypertelorism, long philtrum, strabismus, GI issues, behavioral issues, seizures at ~10 years; EEG abnormal with occipital/midline spike-wave; brain MRI normal; no scoliosis/hypotonia/decreased bone density documented. Twin: milder Asperger syndrome/motor-cognitive-speech delay (gupta2019developmentaldelaycoarse pages 1-2, gupta2019developmentaldelaycoarse pages 2-4, gupta2019developmentaldelaycoarse pages 5-6) | Demonstrates intrafamilial variability and possible modifier effect; low heparan sulfate measured in dried blood spot, serum, and urine in proband and unaffected parents; variants submitted to ClinVar; no exostoses reported (gupta2019developmentaldelaycoarse pages 1-2, gupta2019developmentaldelaycoarse pages 2-4, gupta2019developmentaldelaycoarse pages 5-6) | EXT2 variants were classified as likely pathogenic/clinical-interest in context of emerging AREXT2 literature, but authors noted NDST1 contribution remained uncertain; unaffected parents also had low heparan sulfate, limiting biomarker specificity (gupta2019developmentaldelaycoarse pages 2-4, gupta2019developmentaldelaycoarse pages 5-6) |
| Sabir et al., 2022; Clin Dysmorphol 31:84-90; DOI: 10.1097/MCD.0000000000000406 | Reported as a further case / extending phenotype | Not extractable from retrieved context | Not extractable from retrieved context | Not extractable from retrieved context | Mentioned only as an unobtainable paper in search results; because no supporting details were retrieved, it is intentionally not summarized beyond bibliographic mention to avoid inventing facts (gupta2019developmentaldelaycoarse pages 4-5) |


*Table: This table summarizes the main published human cohorts for autosomal recessive EXT2-related syndrome/SSMS, emphasizing genotype, core phenotype, outcomes, and limits of the available evidence. It is useful for quickly separating well-supported patient data from second-hand summaries and unretrieved reports.*

---

## 1. Disease information

### Definition and identifiers

* **Preferred disease name:** autosomal-recessive EXT2-related syndrome (AREXT2).
* **Historical/eponymous name:** seizures–scoliosis–macrocephaly syndrome (SSMS or SSM syndrome).
* **MONDO:** **MONDO:0014731**.
* **OMIM phenotype:** **616682**.
* **Causal gene:** **EXT2**, OMIM **608210**; Ensembl **ENSG00000151348**; approved name “exostosin glycosyltransferase 2.” Open Targets identifies EXT2 as the sole associated target for MONDO:0014731 and links the association to PMID 26246518 and subsequent literature. (OpenTargets Search: seizures-scoliosis-macrocephaly syndrome-EXT2)
* **Distinct dominant disorder:** multiple exostoses type 2, OMIM **133701**, caused by monoallelic pathogenic EXT2 variants. It must not be merged with SSMS/AREXT2. (gupta2019developmentaldelaycoarse pages 1-2, gupta2019developmentaldelaycoarse pages 2-4, farhan2016genediscoveryina pages 131-135)
* **Other nomenclature encountered:** EXT2-CDG and recessive EXT2 deficiency. Because the molecular defect involves glycosaminoglycan rather than classical N-linked glycoprotein biosynthesis, “EXT2-related glycosaminoglycan-biosynthesis disorder” is mechanistically precise.
* **Orphanet, ICD-10, ICD-11 and MeSH:** no retrieved evidence established a dedicated disorder-specific identifier. Coding therefore generally requires broader categories such as genetic neurodevelopmental disorder, epilepsy and scoliosis, rather than a unique SSMS code.

### Source granularity

Knowledge is derived mainly from **individual patients and multiplex families published as case reports/series**, then aggregated by OMIM/MONDO and reviews—not from EHR-scale cohorts, registries or population surveillance. The original report involved four siblings; subsequent publications added only small families or single cases. Accordingly, apparent frequencies are descriptive proportions among published cases and are highly vulnerable to ascertainment and publication bias. (gupta2019developmentaldelaycoarse pages 1-2, gupta2019developmentaldelaycoarse pages 4-5, farhan2016genediscoveryin pages 110-114)

---

## 2. Etiology

### Causal factor

The primary cause is **germline biallelic EXT2 variation**, usually missense alleles retaining partial function. In the original consanguineous Old Order Mennonite family, all affected siblings were homozygous for both **NM_000401.3:c.260T>G, p.(Met87Arg)** and **c.283C>T, p.(Arg95Cys)** on the same disease haplotype (“complex homozygosity”). Patient fibroblasts had significantly reduced EXT2 protein (P<0.001), modestly reduced transcript (P<0.05), and loss of detectable NDST1 protein despite preserved NDST1 transcript. Expression constructs showed that each variant reduced EXT2 abundance and that the combined changes had the greatest effect; p.Arg95Cys had the larger individual effect. This supports synergistic partial loss of protein stability/function rather than gain of function. (farhan2016genediscoveryina pages 123-130)

Other reported genotypes include homozygous **c.11C>T, p.(Ser4Leu)**; compound-heterozygous **c.679G>A, p.(Asp227Asn)** plus **c.1823A>G, p.(Tyr608Cys)**; and compound-heterozygous **c.1118T>A, p.(Val373Asp)** plus **c.2015C>T, p.(Thr672Met)**. The last pair was considered likely pathogenic by the authors under ACMG/AMP reasoning, although originally returned as VUSs in a gene with an emerging disease relationship. (gupta2019developmentaldelaycoarse pages 2-4, gupta2019developmentaldelaycoarse pages 4-5, gupta2019developmentaldelaycoarse pages 5-6)

### Genetic risk and modifiers

* **Major risk:** inheriting two disease-associated EXT2 alleles in trans, or the same pathogenic/hypomorphic haplotype from both parents.
* **Consanguinity/founder structure:** central in the original Mennonite family and compatible with homozygosity-by-descent. In local screening, p.Met87Arg had 3 heterozygotes among 78 persons (carrier frequency 3.85%), whereas no p.Arg95Cys carrier or double heterozygote was found. In 311 additional healthy Caucasian controls, neither allele was detected. Historical NHLBI ESP minor-allele frequencies were 0.054% and 0.015%, respectively; these are not contemporary ancestry-stratified carrier estimates. (farhan2016genediscoveryina pages 123-130)
* **Gupta-family allele frequencies:** p.Val373Asp occurred in 3/246,244 gnomAD alleles (0.001%; no homozygotes) and p.Thr672Met in 20/276,874 (0.007%; no homozygotes). (gupta2019developmentaldelaycoarse pages 2-4)
* **Potential modifier:** the Gupta proband and her more mildly affected twin also carried heterozygous **NDST1 c.1360C>T, p.(Arg454Cys)**, frequency 44/275,364 alleles (0.02%; no homozygotes). The authors explicitly considered an NDST1 modifier effect but concluded that evidence was insufficient. Neuronal voltage-gated-potassium-channel antibodies present in the more severely affected twin were another possible contributor to discordance, but not an established SSMS mechanism. (gupta2019developmentaldelaycoarse pages 2-4, gupta2019developmentaldelaycoarse pages 5-6)
* No validated protective EXT2 allele, modifier gene, polygenic score, anticipation, recurrent de novo mechanism or germline-mosaicism estimate has been reported.

### Environmental, infectious and gene–environment factors

No toxin, diet, lifestyle, occupational exposure, radiation or infectious agent is known to cause SSMS. No protective lifestyle factor or reproducible gene–environment interaction has been identified. Fever, sleep loss or medication nonadherence may trigger seizures in any epilepsy, but there is no SSMS-specific evidence. Family history and consanguinity alter the probability of inheriting the genotype, not its molecular action.

---

## 3. Phenotypes

### Core and variable manifestations

The original four siblings all had developmental delay/intellectual disability, seizures beginning at approximately 2.5–5 years, hypotonia, macrocephaly and scoliosis/kyphosis. They had minimal expressive speech with relatively preserved comprehension. Additional findings included coarse/dysmorphic facies, hypertelorism, long hypoplastic philtrum, cryptorchidism in males, ventricular septal defects, gastrointestinal dysmotility/reflux, and renal abnormalities. No exostoses were found. (farhan2016genediscoveryin pages 110-114, farhan2016genediscoveryina pages 110-114, farhan2016genediscoveryin pages 105-110)

Later cases broadened the spectrum to microcephaly, feeding difficulty, osteopenia, absent scoliosis, autism, behavioral dysregulation, sleep disturbance, normal brain MRI and later-onset focal epilepsy. The Gupta proband sat at 7–8 months, walked at 14 months, had language delay by age 2 and regression at 27 months; seizures began around age 10. EEG showed occipital-midline spike-and-wave discharges consistent with focal seizures, whereas MRI was normal. Her fraternal twin carrying the same EXT2 variants had much milder motor, speech and cognitive difficulties/Asperger syndrome. (gupta2019developmentaldelaycoarse pages 1-2, gupta2019developmentaldelaycoarse pages 2-4, gupta2019developmentaldelaycoarse pages 4-5)

### Suggested phenotype annotations

| Clinical domain | Character/course | Published frequency signal | Suggested HPO term |
|---|---|---:|---|
| Global developmental delay | Infancy/early childhood; variable, sometimes regression | Very common across reported cases | **HP:0001263** Global developmental delay |
| Intellectual disability | Mild to severe; lifelong | Very common | **HP:0001249** Intellectual disability |
| Speech/language delay | Often marked; minimal expressive speech in founder cohort | Common | **HP:0000750** Delayed speech and language development |
| Seizures/epilepsy | Usually childhood; generalized tonic–clonic, focal or status epilepticus | Very common; onset 2.5–5 years in all four founder cases, age 10 in Gupta proband | **HP:0001250** Seizure; **HP:0002069** Generalized tonic-clonic seizure; **HP:0002133** Status epilepticus |
| Hypotonia | Congenital or early childhood; variable | All four founder cases; absent in Gupta proband | **HP:0001252** Muscular hypotonia |
| Macrocephaly | Congenital/postnatal; nonprogressive status unclear | All four founder cases and Gupta proband; not universal | **HP:0000256** Macrocephaly |
| Microcephaly | Alternative head-size phenotype | Reported in the severe El-Bazzal family | **HP:0000252** Microcephaly |
| Scoliosis/kyphoscoliosis | Childhood, potentially progressive and function-limiting | All four founder cases; absent in Gupta proband | **HP:0002650** Scoliosis; **HP:0002751** Kyphoscoliosis |
| Facial dysmorphism | Coarse facies, hypertelorism, tall/prominent forehead, long philtrum, broad/bulbous nose | Common but variable | **HP:0000316** Hypertelorism; **HP:0000343** Long philtrum; **HP:0000280** Coarse facial features |
| Autism/behavioral abnormalities | Autism, stereotypies, aggression/self-injury, sleep difficulty | Variable | **HP:0000717** Autism; **HP:0000718** Aggressive behavior; **HP:0002360** Sleep disturbance |
| GI dysfunction | GERD, constipation/diarrhea, dysmotility; volvulus/malrotation in founder family | Variable | **HP:0002020** Gastroesophageal reflux; **HP:0002019** Constipation; **HP:0002566** Intestinal malrotation |
| Renal disease | Hematuria/proteinuria; renal failure in one founder sibling | Uncommon but clinically important | **HP:0000093** Proteinuria; **HP:0000790** Hematuria; **HP:0000083** Renal insufficiency |
| Cardiac defect | Ventricular septal defect in members of founder family | Variable | **HP:0001629** Ventricular septal defect |
| Cryptorchidism | Bilateral in affected males in founder family | Reported in founder males | **HP:0000028** Cryptorchidism |
| Strabismus | Surgically treated in Gupta proband | Variable | **HP:0000486** Strabismus |
| Osteopenia | Described in later severe cases | Variable | **HP:0000938** Osteopenia |
| Osteochondroma/exostoses | **Absent**, an important discriminator | Absent in original family and reported AREXT2 cases | **HP:0002859** Multiple exostoses—use as an excluded/negative phenotype |

These are suggested knowledge-base mappings, not a formally curated SSMS HPO disease model.

### Quality-of-life impact

No EQ-5D, SF-36, PROMIS or disease-specific quality-of-life study exists. Nevertheless, case data show major functional burden: severe communication limitation, lifelong supervision, epilepsy risk, orthopedic restriction and multisystem surveillance. One sibling became wheelchair-dependent after prolonged status epilepticus with hemiplegic stroke; another died after status epilepticus at 17. Scoliosis/kyphosis, gastrointestinal disease and renal failure add substantial morbidity. Conversely, the mildly affected Gupta twin illustrates that biallelic disease can permit much greater independence. (farhan2016genediscoveryin pages 110-114, farhan2016genediscoveryina pages 110-114)

---

## 4. Genetic and molecular information

### Gene/protein

* **Gene:** EXT2; HGNC-approved symbol **EXT2**; chromosome **11p11.2**; OMIM 608210.
* **Protein:** exostosin-2, a type-II membrane glycosyltransferase of the ER/Golgi secretory pathway.
* **Molecular function:** with EXT1, catalyzes heparan-sulfate backbone elongation by alternating addition of glucuronic acid (GlcA) and N-acetylglucosamine (GlcNAc) from UDP-GlcA and UDP-GlcNAc. The EXT1–EXT2 heterocomplex has substantially stronger polymerase activity than either protein alone. (mizumoto2021congenitaldisordersof pages 11-12, mizumoto2021congenitaldisordersof pages 12-13, jankun2017thestudyof pages 24-28)

Suggested GO annotations include **GO:0000139 Golgi membrane**, **GO:0005794 Golgi apparatus**, **GO:0005783 endoplasmic reticulum**, **GO:0015012 heparan sulfate proteoglycan biosynthetic process**, **GO:0008375 acetylglucosaminyltransferase activity**, and **GO:0008194 UDP-glycosyltransferase activity**.

### Variant table

| Variant(s) | State | Evidence/classification | Functional or population evidence |
|---|---|---|---|
| c.260T>G p.Met87Arg + c.283C>T p.Arg95Cys | Both homozygous on a complex allele/haplotype | Disease-associated in original family; functionally supported | Reduced EXT2 protein/transcript in fibroblasts; each construct reduced expression, combined strongest; historical ESP MAF 0.054% and 0.015% |
| c.11C>T p.Ser4Leu | Homozygous | Reported in severe AREXT2 family | Direct functional evidence not retrieved |
| c.679G>A p.Asp227Asn + c.1823A>G p.Tyr608Cys | Compound heterozygous | Reported AREXT2 missense pair | Direct assay not retrieved |
| c.1118T>A p.Val373Asp + c.2015C>T p.Thr672Met | Compound heterozygous | Authors’ final assessment: likely pathogenic collectively | gnomAD 3/246,244 and 20/276,874, respectively; no homozygotes; damaging in-silico predictions; segregation with two affected sisters |

All reported SSMS alleles are **germline**. No somatic SSMS mechanism is known. No recurrent pathogenic structural variant, aneuploidy, translocation or inversion defines SSMS. Heterozygous deletion of 11p11.2 including EXT2 instead produces Potocki–Shaffer syndrome, a distinct contiguous-gene condition. (mizumoto2021congenitaldisordersof pages 12-13, gupta2019developmentaldelaycoarse pages 2-4)

### Functional interpretation and caveats

The original alleles are best interpreted as **hypomorphic loss-of-function/protein-destabilizing missense changes**. Complete EXT2 loss is probably incompatible with normal embryogenesis, consistent with animal null lethality. Variant classification should be performed allele-by-allele using current ClinVar submissions, segregation, phase, rarity, phenotype and functional evidence. The Gupta variants have ClinVar submissions **SCV000782709** and **SCV000782708**; the NDST1 VUS was submitted as **SCV000782711**. (gupta2019developmentaldelaycoarse pages 2-4)

No SSMS-specific DNA-methylation signature, histone alteration, imprinting mechanism or epigenetic biomarker has been demonstrated. No transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial or multi-omic patient cohort exists.

---

## 5. Environmental information

SSMS is a constitutional Mendelian disorder. No environmental exposure, lifestyle practice or pathogen is necessary or sufficient to produce it, and none has been shown to alter penetrance. Routine healthy diet, exercise within orthopedic/neurologic limits, avoidance of smoking/alcohol and vaccination are general-health measures, not disease-specific interventions. Environmental seizure-safety measures can reduce injury but do not prevent the molecular disease.

---

## 6. Mechanism and pathophysiology

### Supported causal chain

1. **Trigger—biallelic hypomorphic EXT2 variants.** The founder variants reduce EXT2 transcript modestly and protein much more strongly, consistent with impaired stability/processing. (farhan2016genediscoveryina pages 123-130)
2. **Upstream biochemical defect—impaired EXT1–EXT2 copolymerase.** The Golgi complex normally elongates HS with repeating **[GlcA–GlcNAc]n** units. Reduced EXT2 lowers chain production/length and perturbs assembly of the HS-biosynthetic machinery. (mizumoto2021congenitaldisordersof pages 11-12, jankun2017thestudyof pages 24-28)
3. **Secondary biosynthetic defect—NDST1 instability and altered sulfation.** NDST1 protein was abolished in founder patient fibroblasts despite normal transcript, suggesting post-translational destabilization. NDST1 establishes N-sulfated domains needed for later HS modification and ligand binding. This is direct cellular evidence; the precise patient HS sequence/chain-length defect was not comprehensively profiled. (farhan2016genediscoveryina pages 123-130)
4. **Extracellular/cell-surface consequences.** HS proteoglycans organize extracellular matrix and act as co-receptors/reservoirs for morphogens, growth factors, cytokines and axon-guidance cues. Reduced or abnormally modified HS can impair ligand distribution and receptor activation. (mizumoto2021congenitaldisordersof pages 12-13)
5. **Downstream developmental signaling.** Zebrafish ext2/dackel studies support disrupted **FGF** and **Wnt** signaling, with less evidence for a primary Hedgehog defect. These pathways regulate neural patterning, axon guidance, cartilage organization, organogenesis and growth. Their role in human SSMS is biologically compelling but inferential rather than proven in patient neural tissue. (mizumoto2021congenitaldisordersof pages 12-13, jankun2017thestudyof pages 24-28)
6. **Clinical manifestations.** Abnormal neuronal specification/connectivity and network maturation plausibly produce developmental disability, macro-/microcephaly and epilepsy; defective chondrocyte organization and matrix signaling plausibly produce scoliosis/osteopenia; disturbed renal, cardiac and gastrointestinal morphogenesis or tissue maintenance plausibly explains variable systemic findings.

### Current structural insight

A 2024 cryo-EM study resolved human NDST1’s N-terminal, deacetylase and sulfotransferase architecture and proposed that substrate anchoring at the sulfotransferase domain initiates a catalytic cycle despite spatial separation of catalytic domains (Mycroft-West et al., published February 2024; DOI: https://doi.org/10.1038/s41467-024-45419-4). This refines understanding of the pathway downstream of EXT2 but did not study SSMS variants or patients.

> **2024 abstract wording:** “Mature HS polysaccharides contain complex, non-templated patterns of sulfation and epimerization, which mediate interactions with diverse protein partners.” This helps explain why simply supplying nonspecific heparan sulfate may not reproduce the missing developmental signal.

### Suggested mechanism annotations

* **GO biological processes:** heparan-sulfate proteoglycan biosynthesis; glycosaminoglycan biosynthesis; Golgi organization; extracellular-matrix organization (**GO:0030198**); nervous-system development (**GO:0007399**); axon guidance (**GO:0007411**); cartilage development (**GO:0051216**); regulation of FGF-receptor and Wnt signaling.
* **Cell types (suggested CL mappings):** neuron (**CL:0000540**), neural progenitor cell (**CL:0011020**), chondrocyte (**CL:0000138**), osteoblast (**CL:0000062**), fibroblast (**CL:0000057**), renal epithelial cell and cardiomyocyte. Only fibroblasts have been directly assayed from SSMS patients; the remaining cells are inferred from clinical anatomy/model biology.
* **Chemical entities:** heparan sulfate (**CHEBI:28815**), glucuronic acid/UDP-glucuronate, N-acetyl-D-glucosamine/UDP-GlcNAc, and proteoglycan. No disease-specific circulating chemical biomarker is validated.
* **Subcellular site:** ER/Golgi membrane and lumen for EXT1–EXT2 synthesis/assembly; plasma membrane and extracellular matrix for mature HS proteoglycans.

No primary immune, inflammatory, oxidative-stress, mitochondrial, autophagic or apoptotic mechanism has been demonstrated in SSMS. Immune abnormalities reported in other HS-biosynthesis disorders should not be transferred to EXT2 disease without evidence.

---

## 7. Anatomical structures affected

### Organ and system level

* **Primary:** central nervous system/brain; vertebral column and axial skeleton.
* **Variable secondary:** peripheral musculoskeletal system, heart (septum), kidneys, gastrointestinal tract, eyes and male reproductive tract.
* **Suggested UBERON terms:** brain (**UBERON:0000955**), cerebral cortex (**UBERON:0000956**), spinal cord (**UBERON:0002240**), vertebral column (**UBERON:0001130**), cartilage tissue (**UBERON:0002418**), kidney (**UBERON:0002113**), heart (**UBERON:0000948**), intestine (**UBERON:0000160**) and testis (**UBERON:0000473**).

No consistent lateralization is known. The hemiplegia in one patient followed a prolonged seizure/stroke and should be treated as an acquired complication, not a primary asymmetric malformation. Patient MRI can be normal, as in the Gupta proband; therefore normal structural imaging does not exclude the diagnosis. (gupta2019developmentaldelaycoarse pages 1-2)

---

## 8. Temporal development

SSMS is genetically present from conception, but clinical recognition is generally **infantile or early-childhood**. Hypotonia and motor delay may be evident in infancy; language delay appears in the first two years; seizures typically begin in early childhood but can emerge as late as approximately age 10. Spinal deformity may become more apparent with growth. (gupta2019developmentaldelaycoarse pages 1-2, gupta2019developmentaldelaycoarse pages 4-5, farhan2016genediscoveryin pages 105-110)

The course is **chronic and lifelong**, with markedly variable severity. Some developmental deficits are stable; regression, declining mobility and progressive orthopedic or renal morbidity can occur. Epilepsy is episodic and may include life-threatening status epilepticus. No recognized biochemical stages, remission pattern or validated critical-treatment window exists. Developmental biology suggests that prenatal/early-postnatal HS signaling is a critical period, but this remains an experimental inference. (farhan2016genediscoveryina pages 131-135)

---

## 9. Inheritance and population

* **Inheritance:** autosomal recessive.
* **Recurrence risk:** when both parents carry one disease-associated allele/haplotype, each pregnancy has a 25% affected, 50% carrier and 25% non-carrier probability, assuming conventional Mendelian segregation.
* **Penetrance:** likely high for clinically relevant biallelic genotypes, but cannot be quantified. The markedly discordant Gupta twins demonstrate variable expressivity and/or uncertain contribution from modifiers.
* **Anticipation:** not expected and not reported.
* **Sex ratio:** no credible estimate; both sexes are affected. The original cohort was 3 male/1 female, but published numbers are too small for inference. (farhan2016genediscoveryin pages 105-110)
* **Prevalence/incidence:** unknown; no cases-per-100,000 or annual incidence estimate exists. The total published population is only on the order of a dozen individuals, depending on inclusion of incompletely characterized “further cases.”
* **Geography/ancestry:** reported families include an Old Order Mennonite kindred and unrelated later families. No population-wide endemic distribution is established.
* **Carrier frequency:** unknown globally. The 3.85% local p.Met87Arg carrier observation was based on only 78 persons and did not include p.Arg95Cys double carriers; it must not be used as a general AREXT2 carrier rate. (farhan2016genediscoveryina pages 123-130)

---

## 10. Diagnostics

### Clinical suspicion

Consider AREXT2 in a child or adult with otherwise unexplained developmental/intellectual disability plus epilepsy, abnormal head circumference, hypotonia, scoliosis/osteopenia or characteristic coarse facial features—particularly with consanguinity, similarly affected siblings and **no osteochondromas**. The phenotype is not specific enough for clinical diagnosis alone. (mizumoto2021congenitaldisordersof pages 12-13, gupta2019developmentaldelaycoarse pages 2-4)

### Recommended evaluation

1. **Genetic confirmation:** sequence EXT2 with deletion/duplication coverage as part of a developmental-delay/epilepsy, congenital-glycosylation/GAG-biosynthesis or skeletal-dysplasia panel, or use trio/quad **WES/WGS**. Confirm candidate variants by orthogonal testing where required, establish phase, test parents and segregate within the family. Autozygosity mapping can help in consanguineous multiplex families, as demonstrated in the founder report. (farhan2016genediscoveryina pages 123-130, farhan2016genediscoveryina pages 131-135)
2. **Variant interpretation:** require biallelic variants compatible with recessive inheritance; assess rarity, conservation, protein domain, ClinVar evidence, phenotype and functional data. A single heterozygous EXT2 variant does not establish SSMS and instead raises dominant HME carrier/disease considerations.
3. **Neurology:** developmental assessment; EEG after seizures or suspicious episodes; MRI to assess alternative structural causes, recognizing that it may be normal. (gupta2019developmentaldelaycoarse pages 1-2)
4. **Musculoskeletal:** standing spine radiographs and orthopedic examination for scoliosis/kyphosis; bone-density assessment when clinically indicated. Skeletal survey can document absence of osteochondromas or investigate unexplained masses.
5. **Systemic baseline:** urinalysis, urine protein, serum creatinine/eGFR and blood pressure; echocardiography if murmur/congenital-heart concern; GI/nutritional assessment; ophthalmology; examination for cryptorchidism.

### Biomarkers and other tests

The Gupta proband had low HS in dried blood spot (12 nmol/L), serum (4.46 ng/mL) and urine (0.5 mg/mmol creatinine). However, her clinically unaffected parents also had low values, so HS measurement is neither validated nor sufficiently specific/sensitive for diagnosis. It may remain a research assay. Conventional karyotype, array CGH, Fragile-X testing and Rett/Angelman/Prader–Willi testing were normal in that patient. (gupta2019developmentaldelaycoarse pages 1-2, gupta2019developmentaldelaycoarse pages 2-4)

CMA is appropriate when copy-number disease remains in the differential, particularly Potocki–Shaffer syndrome, but it will not detect most missense AREXT2 genotypes. Karyotype/FISH, mitochondrial sequencing, repeat-expansion tests, biopsy, proteomics, metabolomics, epigenomics and liquid biopsy have no SSMS-specific indication unless another diagnosis is suspected.

### Differential diagnosis

* **Dominant EXT2-related hereditary multiple exostoses:** multiple osteochondromas, often short stature/limb deformity; typically monoallelic EXT2; neurodevelopmental SSMS constellation is not typical.
* **Potocki–Shaffer syndrome:** 11p11.2 deletion including EXT2 and adjacent genes; exostoses, biparietal foramina, intellectual disability and craniofacial anomalies.
* **Other HS-biosynthesis disorders:** NDST1-related intellectual disability, EXTL3-related neuro-immuno-skeletal dysplasia and HS2ST1-related neurofacioskeletal syndrome.
* **Mucopolysaccharidoses:** coarse facies, skeletal and neurodevelopmental disease, but caused by HS degradation/storage with elevated urinary GAG patterns rather than deficient synthesis.
* Other developmental epileptic encephalopathies, overgrowth/macrocephaly syndromes, congenital glycosylation disorders and syndromic scoliosis.

No standardized clinical diagnostic criteria or newborn-screening program exists.

---

## 11. Outcome and prognosis

No survival curve, median life expectancy, 5-/10-year survival, mortality rate or validated prognostic score exists. Published survival into adulthood—including age 21 and at least the mid/late twenties in follow-up—is compatible with long survival in some genotypes. Severe outcomes in the founder family included renal failure, loss of ambulation after status epilepticus with stroke, and death after status epilepticus at 17. (gupta2019developmentaldelaycoarse pages 4-5, farhan2016genediscoveryin pages 110-114, farhan2016genediscoveryin pages 105-110)

Likely prognostic factors, not formally validated, are epilepsy severity/status epilepticus, degree of developmental impairment and hypotonia, scoliosis progression, feeding/aspiration risk, renal involvement and congenital-heart disease. Neither HS concentration nor a molecular biomarker has been shown to predict course. Recovery of the underlying developmental phenotype is not documented, although skills, communication, seizure control and mobility may improve with supportive treatment.

---

## 12. Treatment

### Current standard: individualized symptomatic care

There is **no approved disease-modifying therapy and no SSMS-specific guideline**.

* **Epilepsy:** treat according to seizure type using standard antiseizure medication; prepare a rescue plan for prolonged seizures and status epilepticus. No drug has demonstrated SSMS-specific superiority, response rate or pharmacogenomic interaction. Given reported catastrophic status, caregiver education and emergency planning are high priorities. Suggested NCIt concepts: *Anticonvulsant Agent* and *Seizure Prophylaxis*.
* **Scoliosis/kyphosis:** serial orthopedic monitoring; physiotherapy, bracing and spinal surgery according to curve severity, progression, pulmonary impact and function. Bracing was used in the founder family. Suggested NCIt concepts: *Orthopedic Procedure*, *Spinal Fusion*, *Physical Therapy*. (farhan2016genediscoveryin pages 105-110)
* **Development:** early physical, occupational, speech/language and augmentative-communication therapy; individualized educational and behavioral support. Suggested NCIt concepts: *Physical Therapy*, *Occupational Therapy*, *Speech Therapy*.
* **Other systems:** feeding/nutrition and reflux/constipation treatment; nephrology for proteinuria/renal impairment; cardiology for congenital lesions; ophthalmologic treatment for strabismus; urology/surgery for cryptorchidism; mobility devices and bone-health management as indicated.

The Gupta proband showed some language/social improvement after immunotherapy directed at neuronal potassium-channel antibodies but tolerated it poorly and treatment was discontinued. This was treatment of a possible comorbidity, not evidence for immunotherapy in SSMS. (gupta2019developmentaldelaycoarse pages 1-2)

### Experimental concepts

Farhan and Gupta proposed raising HS levels through HS administration, enzyme replacement or gene replacement. These remain speculative: no animal efficacy study tailored to SSMS, dose, delivery strategy, safety dataset or human trial was identified. Farhan explicitly cautioned that nonspecific HS administration would be premature because genotype matters and toxicity from excess HS is unknown. Developmental timing and delivery across the blood–brain barrier are major obstacles. (gupta2019developmentaldelaycoarse pages 5-6, farhan2016genediscoveryina pages 131-135)

No relevant SSMS/AREXT2 interventional ClinicalTrials.gov study, gene therapy, cell therapy, RNA therapy, CRISPR trial, immunotherapy or targeted small molecule was identified. There are no treatment response percentages or SSMS-specific adverse-event datasets.

---

## 13. Prevention

The genotype cannot be prevented by lifestyle or vaccination.

* **Primary genetic prevention/family planning:** offer genetic counseling, parental carrier confirmation, cascade testing of adult relatives, partner testing where a familial founder allele is present, prenatal diagnosis by CVS/amniocentesis, and preimplantation genetic testing for monogenic disease after the familial alleles are established.
* **Secondary prevention:** early molecular diagnosis enables developmental therapy, seizure surveillance and renal/cardiac/orthopedic assessment before complications become advanced. Population newborn screening is not available or currently justified by evidence.
* **Tertiary prevention:** optimize seizure control and rescue planning; monitor scoliosis, mobility and bone health; detect proteinuria/renal dysfunction; manage feeding/reflux/aspiration and congenital heart disease; implement home and school seizure-safety measures.
* **Immunization/public health:** routine schedules apply; there is no SSMS-specific vaccine, prophylactic medication or environmental intervention.

---

## 14. Other species and natural disease

No naturally occurring companion-animal, livestock or wildlife syndrome convincingly homologous to human biallelic EXT2 SSMS was identified; no breed or VBO term can therefore be assigned. The disorder is not infectious and has no zoonotic or cross-species transmission potential.

Orthologous EXT-family function is highly conserved across **Mus musculus** (NCBI Taxon 10090), **Danio rerio** (7955), **Drosophila melanogaster** (7227) and **Caenorhabditis elegans** (6239). Conservation of HS-dependent morphogen signaling makes these species mechanistically relevant, but induced genetic phenotypes should not be represented as natural veterinary SSMS.

---

## 15. Model organisms

### Mouse

Complete Ext1/Ext2 deficiency markedly impairs HS synthesis, prevents normal gastrulation and causes embryonic death around E8.5; hypomorphic models survive longer and produce shorter HS chains. These models establish that residual activity is likely necessary for viability and support the classification of human missense alleles as hypomorphic. Heterozygous/truncating models can develop osteochondromas and are more directly models of dominant HME than of AREXT2. (farhan2016genediscoveryina pages 131-135)

**Application:** embryogenesis, neural patterning, HS chain length and skeletal growth. **Limitation:** complete-null lethality prevents recapitulation of the viable, chronic human syndrome; heterozygous tumor models emphasize exostoses absent from SSMS.

### Zebrafish

The **dackel/ext2** mutant has reduced, abnormally sulfated HS; disordered chondrocyte intercalation/stacking and pharyngeal-cartilage morphology; abnormal optic-tract axon organization; and disturbed FGF/Wnt-dependent development. These observations directly connect Ext2 to neural guidance and cartilage organization. (mizumoto2021congenitaldisordersof pages 12-13, jankun2017thestudyof pages 24-28)

**Application:** live developmental imaging, morphogen gradients, cartilage and axon guidance, rapid genetic/drug screens. **Limitation:** larval craniofacial/fin phenotypes do not reproduce human epilepsy, macrocephaly or chronic scoliosis, and strong mutant alleles may be more severe than human hypomorphs.

### Drosophila and C. elegans

Drosophila **sister of tout-velu (sotv; Ext2 ortholog)** and related HS-pathway mutants disrupt morphogen distribution and neuronal/dendritic development. Viable hypomorphic C. elegans **rib-1/rib-2** exostosin-pathway mutants markedly reduce HS and cause selective cell/axon-migration and morphogenetic abnormalities; cell-specific rescue indicates requirements in both migrating neurons and neighboring cells. These systems demonstrate conserved, partly non-cell-autonomous HS function. (farhan2016genediscoveryina pages 131-135)

**Application:** genetic interaction screens and cell-specific pathway dissection. **Limitation:** neither organism models vertebral scoliosis, mammalian brain anatomy or human epilepsy adequately.

### Missing model platforms

No retrieved publication described an SSMS-patient iPSC line, cerebral organoid, CRISPR knock-in of a human AREXT2 allele, or humanized mouse. Such isogenic hypomorphic models are a high-priority research need because they could measure variant-specific HS chain length/sulfation, neuronal network excitability and rescue by precisely timed gene or glycan-pathway correction.

---

## Evidence assessment and 2023–2024 research status

The most authoritative direct evidence remains the 2015 founder-family study and later small case reports. Reviews correctly emphasize that recessive EXT2 disease is “without exostoses and with an autosomal recessive inheritance” and that the EXT1/EXT2 complex catalyzes HS synthesis, but reviews cannot resolve penetrance or phenotype frequencies in such a small population. (jaeken2020congenitaldisordersof pages 4-5, mizumoto2021congenitaldisordersof pages 12-13)

Recent 2024 HS literature advances structural and systems-level understanding—particularly NDST1 architecture and HSPG-mediated signaling—but it does not yet supply new AREXT2 patients, prospective natural history, validated biomarkers or therapeutic data. Consequently, all epidemiologic rates, genotype–phenotype rules, surveillance intervals and treatment algorithms should be recorded as **unknown or expert-practice extrapolation**, not established evidence.

### Principal knowledge gaps

1. Complete contemporary case census and longitudinal natural history.
2. ClinGen-level gene–disease/variant curation and penetrance estimates.
3. Standardized HS chain-length and sulfation profiling in patient cells.
4. Brain-specific cellular models linking EXT2 deficiency to network hyperexcitability.
5. Genotype–phenotype explanation for macrocephaly versus microcephaly and severe versus mild twin/family presentations.
6. Evidence-based renal, cardiac and orthopedic surveillance schedules.
7. Variant-matched hypomorphic models and preclinical rescue studies.

**Bottom line:** SSMS/AREXT2 is a recessive, hypomorphic EXT2 glycosaminoglycan-biosynthesis disorder with a predominantly neurodevelopmental–epileptic phenotype and variable skeletal/multisystem involvement. The human evidence supports reduced EXT2 abundance and disturbed HS-pathway organization; downstream FGF/Wnt, axon-guidance and cartilage mechanisms are strongly supported by models but remain partly inferential in patients. Diagnosis is molecular, management is symptomatic and multidisciplinary, and prevention currently consists of genetic counseling and reproductive testing.

References

1. (jaeken2020congenitaldisordersof pages 4-5): Jaak Jaeken. Congenital disorders of glycosylation: a multi-genetic disease family with multiple subcellular locations. Journal of Mother and Child, 24:14-20, Jun 2020. URL: https://doi.org/10.34763/jmotherandchild.20202402si.2005.000004, doi:10.34763/jmotherandchild.20202402si.2005.000004. This article has 21 citations.

2. (mizumoto2021congenitaldisordersof pages 12-13): Shuji Mizumoto and Shuhei Yamada. Congenital disorders of deficiency in glycosaminoglycan biosynthesis. Frontiers in Genetics, Sep 2021. URL: https://doi.org/10.3389/fgene.2021.717535, doi:10.3389/fgene.2021.717535. This article has 60 citations and is from a peer-reviewed journal.

3. (gupta2019developmentaldelaycoarse pages 1-2): Aditi Gupta, Sarah A. Ewing, Deborah L. Renaud, Linda Hasadsri, Kimiyo M. Raymond, Eric W. Klee, and Ralitza H. Gavrilova. Developmental delay, coarse facial features, and epilepsy in a patient with ext2 gene variants. Clinical Case Reports, 7:632-637, Feb 2019. URL: https://doi.org/10.1002/ccr3.2010, doi:10.1002/ccr3.2010. This article has 9 citations.

4. (gupta2019developmentaldelaycoarse pages 2-4): Aditi Gupta, Sarah A. Ewing, Deborah L. Renaud, Linda Hasadsri, Kimiyo M. Raymond, Eric W. Klee, and Ralitza H. Gavrilova. Developmental delay, coarse facial features, and epilepsy in a patient with ext2 gene variants. Clinical Case Reports, 7:632-637, Feb 2019. URL: https://doi.org/10.1002/ccr3.2010, doi:10.1002/ccr3.2010. This article has 9 citations.

5. (OpenTargets Search: seizures-scoliosis-macrocephaly syndrome-EXT2): Open Targets Query (seizures-scoliosis-macrocephaly syndrome-EXT2, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (gupta2019developmentaldelaycoarse pages 5-6): Aditi Gupta, Sarah A. Ewing, Deborah L. Renaud, Linda Hasadsri, Kimiyo M. Raymond, Eric W. Klee, and Ralitza H. Gavrilova. Developmental delay, coarse facial features, and epilepsy in a patient with ext2 gene variants. Clinical Case Reports, 7:632-637, Feb 2019. URL: https://doi.org/10.1002/ccr3.2010, doi:10.1002/ccr3.2010. This article has 9 citations.

7. (mizumoto2018defectsinbiosynthesis pages 13-14): Shuji Mizumoto. Defects in biosynthesis of glycosaminoglycans cause hereditary bone, skin, heart, immune, and neurological disorders. Trends in Glycoscience and Glycotechnology, 30:E67-E89, May 2018. URL: https://doi.org/10.4052/tigg.1812.2e, doi:10.4052/tigg.1812.2e. This article has 14 citations and is from a peer-reviewed journal.

8. (farhan2016genediscoveryin pages 110-114): S Farhan. Gene discovery in mendelian and complex diseases. Unknown journal, 2016.

9. (farhan2016genediscoveryina pages 110-114): S Farhan. Gene discovery in mendelian and complex diseases. Unknown journal, 2016.

10. (farhan2016genediscoveryina pages 123-130): S Farhan. Gene discovery in mendelian and complex diseases. Unknown journal, 2016.

11. (farhan2016genediscoveryina pages 131-135): S Farhan. Gene discovery in mendelian and complex diseases. Unknown journal, 2016.

12. (gupta2019developmentaldelaycoarse pages 4-5): Aditi Gupta, Sarah A. Ewing, Deborah L. Renaud, Linda Hasadsri, Kimiyo M. Raymond, Eric W. Klee, and Ralitza H. Gavrilova. Developmental delay, coarse facial features, and epilepsy in a patient with ext2 gene variants. Clinical Case Reports, 7:632-637, Feb 2019. URL: https://doi.org/10.1002/ccr3.2010, doi:10.1002/ccr3.2010. This article has 9 citations.

13. (farhan2016genediscoveryin pages 105-110): S Farhan. Gene discovery in mendelian and complex diseases. Unknown journal, 2016.

14. (mizumoto2021congenitaldisordersof pages 11-12): Shuji Mizumoto and Shuhei Yamada. Congenital disorders of deficiency in glycosaminoglycan biosynthesis. Frontiers in Genetics, Sep 2021. URL: https://doi.org/10.3389/fgene.2021.717535, doi:10.3389/fgene.2021.717535. This article has 60 citations and is from a peer-reviewed journal.

15. (jankun2017thestudyof pages 24-28): P Jankun. The study of molecular interactions during zebrafish tail regeneration for use in glycotherapeutics. Unknown journal, 2017.

## Artifacts

- [Edison artifact artifact-00](Seizures-scoliosis-macrocephaly_Syndrome-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 5 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `DOI:10.1038/s41467-024-45419-4` (2 mentions) - Structural and mechanistic characterization of bifunctional heparan sulfate N-deacetylase-N-sulfotransferase 1
  - shared terms: human

Weighed against this report's own most characteristic terms: `disease`, `ext2`, `ssms`, `clinical`, `gene`, `phenotype`, `genetic`, `variant`, `developmental`, `human`, `scoliosis`, `epilepsy`, `model`, `affected`, `family`, `arext2`, `patient`, `gupta`, `seizure`, `syndrome`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 54 |
| Resolved | 54 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014731` (3 mentions) - the report calls it "if available"; MONDO calls it **seizures-scoliosis-macrocephaly syndrome**