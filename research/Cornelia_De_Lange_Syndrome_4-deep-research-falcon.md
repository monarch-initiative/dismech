---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-01T10:07:29.307338'
end_time: '2026-09-01T10:22:39.301571'
duration_seconds: 909.99
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cornelia de Lange syndrome 4 (CDLS4, RAD21-related Cornelia de Lange
    syndrome)
  mondo_id: MONDO:0013864
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 47
reference_validation:
  total_references: 12
  verified: 12
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 12
  on_topic: 4
  validator_version: 0.2.1
term_validation:
  total_terms: 47
  verified: 47
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0013864
    reported_labels:
    - if available
    ontology_label: Cornelia de Lange syndrome 4
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Cornelia_De_Lange_Syndrome_4-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cornelia de Lange syndrome 4 (CDLS4, RAD21-related Cornelia de Lange syndrome)
- **MONDO ID:** MONDO:0013864 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Cornelia de Lange syndrome 4 (CDLS4, RAD21-related Cornelia de Lange syndrome)** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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
- **Disease Name:** Cornelia de Lange syndrome 4 (CDLS4, RAD21-related Cornelia de Lange syndrome)
- **MONDO ID:** MONDO:0013864 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Cornelia de Lange syndrome 4 (CDLS4, RAD21-related Cornelia de Lange syndrome)** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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


# Cornelia de Lange syndrome 4 (CDLS4): comprehensive disease-characteristics report

## Executive summary and evidence scope

Cornelia de Lange syndrome 4 (CDLS4) is an ultra-rare, usually autosomal-dominant developmental **cohesinopathy** caused by heterozygous pathogenic variants or deletions involving **RAD21**. Compared with classic NIPBL-related Cornelia de Lange syndrome (CdLS), RAD21-related disease is generally attenuated—especially for cognition, behavior, facial gestalt, and major limb reduction defects—but expressivity is strikingly variable, including within families. The strongest phenotype study comprises 49 individuals from 33 families, of whom 29 were comprehensively phenotyped. Recent 2023 reports expanded the spectrum to prenatal growth restriction, congenital cardiac defects, cleft palate, laryngomalacia, polydactyly, and Müllerian anomalies. (krab2020delineationofphenotypes pages 1-2, falco2023anovelvariant pages 4-7, abarcabarriga2023corneliadelange pages 1-2)

This report distinguishes **CDLS4-specific evidence** from evidence applying to CdLS generally. Most management recommendations and epidemiological estimates come from pan-CdLS cohorts because no RAD21-specific natural-history registry or guideline exists.

| Domain | Best current finding | Evidence type/strength | Key source/date |
|---|---|---|---|
| Disease/gene & inheritance | RAD21-related Cornelia de Lange syndrome is an ultra-rare cohesinopathy with an attenuated but variable CdLS phenotype; inheritance is typically autosomal dominant, with both de novo and familial heterozygous variants reported, plus rare biallelic RAD21 disease outside classic CDLS4 framing | Human cohort + landmark discovery; strong for causality | Deardorff et al., *Am J Hum Genet* 2012; Krab et al., *Hum Genet* 2020 (deardorff2012rad21mutationscause pages 1-2, krab2020delineationofphenotypes pages 1-2) |
| Phenotype cohort | Best delineation includes 49 individuals from 33 families with RAD21 alterations; 29 had full clinical information | Human multicenter cohort; strongest phenotype source | Krab et al., *Hum Genet* 2020 (krab2020delineationofphenotypes pages 1-2) |
| Key phenotype frequencies | Among fully phenotyped RAD21 cases: 55% had normal or mildly impaired cognition; affected behavioral domains in 56%; anxiety 53%; ASD-like features 35%; ADHD/hyperactivity 35%; aggression and self-injury each 6% where assessed | Human cohort; moderate-strong, but behavior often based on clinical report rather than formal testing | Krab et al., *Hum Genet* 2020 (krab2020delineationofphenotypes pages 9-10, krab2020delineationofphenotypes pages 6-7, krab2020delineationofphenotypes pages 12-14) |
| 2023 variant reports | Novel de novo RAD21 c.1722_1723delTG (p.Gly575SerfsTer2) caused classic-scoring CDLS4 with PDA/VSD, cleft palate, laryngomalacia, prenatal growth retardation; separate 13-year-old girl had de novo heterozygous intragenic deletion of RAD21 exons 9-14 detected by high-resolution CMA, without reported neurodevelopmental disorder at diagnosis | Human case reports; useful expansion of spectrum, limited n | De Falco et al., *Genes* 2023; Abarca-Barriga et al., *Genes* 2023 (falco2023anovelvariant pages 4-7, abarcabarriga2023corneliadelange pages 1-2, abarcabarriga2023corneliadelange pages 2-6) |
| Diagnostic yield | In 716 CdLS probands, 422/716 (~59%) received a molecular diagnosis; RAD21 accounted for 6/422 solved cases (~1%) | Large human genomic cohort; strong for relative contribution | Kaur et al., *Am J Med Genet A* 2023 (kaur2023genomicanalysesin pages 5-5) |
| Mechanism | Pathogenic RAD21 variants alter cohesin interfaces, perturb chromatin organization/transcription, impair DNA-damage response/repair, and in models disrupt zygotic genome activation, neural crest migration, and mesoderm/NMP development | Mixed human cell + zebrafish functional evidence; moderate-strong but partly inferred for human developmental pathology | Deardorff et al. 2012; Meier et al. 2018; Schuster et al. 2015; Labudina et al. 2024 (deardorff2012rad21mutationscause pages 6-7, deardorff2012rad21mutationscause pages 7-8, meier2018cohesinfacilitateszygotic pages 14-17, schuster2015aneuralcrest pages 12-13, labudina2024cohesincompositionand pages 6-9) |
| Diagnosis | CdLS diagnosis remains clinical first, using consensus scoring; RAD21 cases often fall in non-classic/milder range. Molecular workup should include multigene sequencing plus CNV analysis; if negative and suspicion remains, test for mosaicism in non-blood tissue and consider broader sequencing | International consensus + cohort data; strong for practice | Kline et al. 2018 consensus; Kaur et al. 2023; Gruca-Stryjak et al. 2024 (kline2018diagnosisandmanagement pages 5-6, kline2018diagnosisandmanagement pages 6-7, kaur2023genomicanalysesin pages 5-5, grucastryjak2024advancingtheclinical pages 14-15) |
| Treatment/trials | No approved RAD21-specific or disease-modifying therapy. Care is multidisciplinary/supportive. Current CdLS trials target broader CdLS populations and are not RAD21-specific; examples include lithium, behavioral intervention, NAC, and autonomic assessment studies | Consensus care + registry/trial evidence; weak for RAD21-targeted efficacy | ClinicalTrials.gov entries NCT06789783, NCT05829668, NCT04381897, NCT03113877 (NCT06789783 chunk 3, NCT05829668 chunk 1, NCT03113877 chunk 1, NCT04381897 chunk 2) |
| Major evidence gaps | No robust subtype-specific prevalence, incidence, survival, penetrance, or natural-history estimates; limited formal QoL data; no validated biomarkers; no RAD21-specific interventional trials; epigenomic/multi-omic data in CDLS4 remain sparse | Evidence-gap summary from available literature | Krab et al. 2020; Kaur et al. 2023; 2024 review/trials landscape (krab2020delineationofphenotypes pages 1-2, kaur2023genomicanalysesin pages 5-5, grucastryjak2024advancingtheclinical pages 14-15, grucastryjak2024advancingtheclinical pages 15-17) |


*Table: This table summarizes the highest-yield current evidence for RAD21-related Cornelia de Lange syndrome, emphasizing cohort size, phenotype frequencies, recent 2023 variant reports, mechanisms, diagnostics, and the absence of subtype-specific therapies. It is useful as a compact reference for knowledge-base population and evidence grading.*

---

## 1. Disease information

### Definition

CDLS4 is a congenital, lifelong, multisystem Mendelian developmental disorder resulting from impaired RAD21/cohesin function. Typical findings include postnatal growth restriction, microcephaly, recognizable but often subtle craniofacial features, minor skeletal or limb anomalies, variable developmental delay—particularly speech—and occasional congenital heart, palatal, gastrointestinal, genitourinary, hearing, or behavioral abnormalities. The original description emphasized “growth retardation, minor skeletal anomalies, and facial features” overlapping CdLS, with substantially milder cognition than classical CdLS. (deardorff2012rad21mutationscause pages 1-2)

### Identifiers and synonyms

- **MONDO:** MONDO:0013864, as supplied in the request; database mapping should be revalidated at ingestion.
- **OMIM phenotype:** **#614701**, Cornelia de Lange syndrome 4.
- **Causal gene:** **RAD21**, chromosome 8q24.11; HGNC symbol RAD21. The gene contains 14 exons and encodes a 631-amino-acid cohesin kleisin subunit. (abarcabarriga2023corneliadelange pages 1-2)
- **Synonyms:** RAD21-related Cornelia de Lange syndrome; RAD21-related cohesinopathy; Cornelia de Lange syndrome type 4; CDLS4; CdLS4.
- **Orphanet:** CdLS has an Orphanet entry, but a separately validated CDLS4-specific ORPHA identifier was not established from the retrieved evidence.
- **ICD-10/ICD-11 and MeSH:** no subtype-specific CDLS4 code was identified. Coding generally occurs under congenital-malformation/genetic-syndrome or broader CdLS categories; a local terminology service should verify the applicable jurisdictional code.

The evidence is principally **aggregated disease-level literature**—multicenter cohorts, case series, consensus guidance, and experimental studies—not EHR-derived individual-level data. The 2023 papers are individual clinical reports. (krab2020delineationofphenotypes pages 1-2, falco2023anovelvariant pages 2-4)

### Key abstract quotation

Krab et al. reported: “We gathered a series of 49 individuals from 33 families with RAD21 alterations… Full clinical information was available for 29 individuals. Their phenotype is an attenuated CdLS phenotype.” Publication: March 2020; DOI: https://doi.org/10.1007/s00439-020-02138-2. (krab2020delineationofphenotypes pages 1-2)

---

## 2. Etiology

### Causal factors

The primary cause is a **germline pathogenic heterozygous RAD21 variant**—missense, frameshift, nonsense/splice-disrupting or intragenic/contiguous deletion—leading to reduced dosage or altered cohesin-complex interactions. The original study identified six affected individuals, including overlapping 8q24.1 deletions and de novo missense variants c.1127C>G (p.Pro376Arg) and c.1753T>C (p.Cys585Arg). (deardorff2012rad21mutationscause pages 3-4)

Pathogenic mechanisms vary by allele:

- **Haploinsufficiency:** RAD21 deletion produced approximately half-normal RNA.
- **Altered protein interaction/dominant dysfunction:** p.Pro376Arg increased interaction with STAG1/STAG2 and produced unusually tight sister-chromatid cohesion; p.Cys585Arg disrupted the RAD21–SMC1A interface.
- **C-terminal truncation:** p.Gly575SerfsTer2 and deletion of exons 9–14 remove structures needed for SMC1A/STAG interaction and cohesin stability. (deardorff2012rad21mutationscause pages 4-6, deardorff2012rad21mutationscause pages 6-7, abarcabarriga2023corneliadelange pages 2-6, falco2023anovelvariant pages 4-7)

### Risk factors

- **Genetic:** carrying a pathogenic RAD21 allele is the dominant risk factor. Both de novo and inherited variants occur. Familial transmission is unusually important relative to classic CdLS: 5/12 evaluable cases in one analysis were familial, and clinically mild or apparently unaffected transmitting parents occur. (krab2020delineationofphenotypes pages 9-10, krab2020delineationofphenotypes pages 12-14)
- **Family history:** increases risk where a parent carries the variant; phenotype cannot be predicted reliably because of intrafamilial variability.
- **Environmental, infectious, lifestyle, age, or sex risks:** none are established as causes or susceptibility factors for CDLS4.
- **Somatic RAD21 variants:** occur in cancers but are biologically distinct from germline CDLS4 and should not be used to diagnose it. (chin2020cohesinmutationsare pages 1-2)

### Protective factors and gene–environment interaction

No validated protective allele, diet, lifestyle, medication, or exposure reduces disease occurrence. Modifier genes, isoforms, epigenetic state, and environmental influences have been proposed to explain variable expression, but none is clinically validated. The neurologically normal individual with a large exons 9–14 deletion illustrates probable modification but does not identify the modifier. (krab2020delineationofphenotypes pages 12-14, abarcabarriga2023corneliadelange pages 1-2)

---

## 3. Phenotypes

Phenotypes are congenital or begin in early childhood. Structural anomalies are stable; growth restriction may become progressively apparent postnatally; development is delayed but generally continues; behavior can evolve with age. Frequencies below are CDLS4-specific where available.

### Growth, head, and development

- **Short stature/growth restriction** — often mild, commonly postnatal and slowly progressive; prenatal restriction is possible. Suggested HPO: **HP:0004322 Short stature**, **HP:0001510 Growth delay**, **HP:0001511 Intrauterine growth retardation**. Approximately half of the well-characterized cohort had progressive impairment of height or head growth. (krab2020delineationofphenotypes pages 9-10, falco2023anovelvariant pages 4-7)
- **Microcephaly** — congenital or emerging postnatally, variable. HPO: **HP:0000252 Microcephaly**.
- **Developmental delay**, predominantly speech — usually mild-to-moderate; all assessed individuals aged ≥3 years used some words. HPO: **HP:0012758 Neurodevelopmental delay**, **HP:0000750 Delayed speech and language development**. (krab2020delineationofphenotypes pages 6-7)
- **Intellectual function** — 16/29 (55%) had normal or only mildly impaired cognition, substantially more favorable than comparison NIPBL (7%) and SMC1A (32%) groups. Formal neuropsychological testing was inconsistent, limiting precision. HPO: **HP:0001249 Intellectual disability** or explicitly record normal cognition when appropriate. (krab2020delineationofphenotypes pages 6-7)

### Craniofacial and ectodermal findings

Typical signs include thick/highly arched eyebrows, synophrys, short nose, long or smooth philtrum, thin upper lip, micrognathia, long eyelashes, sparse temporal scalp hair, and variable hypertrichosis. Across 31 compiled CDLS4 cases, reported frequencies included short nose **89%**, thick eyebrows **84%**, synophrys **69%**, and developmental delay **76%**. (falco2023anovelvariant pages 7-8)

Suggested HPO: **HP:0000574 Thick eyebrow**, **HP:0000664 Synophrys**, **HP:0003196 Short nose**, **HP:0000343 Long philtrum**, **HP:0000219 Thin upper lip vermilion**, **HP:0000347 Micrognathia**, **HP:0000505 Visual impairment** where present, and **HP:0002235 Hypertrichosis**.

### Musculoskeletal and limb findings

Minor anomalies—small hands, clinodactyly, radial-head abnormalities, limited pronation/supination, vertebral anomalies, overlapping toes—are more typical than severe reduction defects. Major limb malformations were absent in the central 29-person cohort, although preaxial polydactyly was reported in 2023. HPO suggestions: **HP:0200055 Small hand**, **HP:0004209 Clinodactyly of the fifth finger**, **HP:0002827 Limited elbow movement**, **HP:0001161 Hand polydactyly**, **HP:0002943 Thoracic scoliosis/vertebral anomaly as anatomically appropriate**. (krabUnknownyearphenotypesandgenotypes pages 1-2, abarcabarriga2023corneliadelange pages 1-2, abarcabarriga2023corneliadelange pages 7-8)

### Behavioral and psychiatric phenotype

Among individuals with available data: any behavioral domain 14/25 (**56%**), anxiety 10/19 (**53%**), autistic-like features 7/20 (**35%**), ADHD/hyperactivity 8/23 (**35%**), obsessive-compulsive behavior 6/19 (**32%**), self-injury 1/18 (**6%**), and aggression 1/16 (**6%**). These were mostly clinician reports rather than standardized testing. Suggested HPO: **HP:0000739 Anxiety**, **HP:0000729 Autistic behavior**, **HP:0007018 Attention deficit hyperactivity disorder**, **HP:0000722 Obsessive-compulsive behavior**, **HP:0100716 Self-injurious behavior**, **HP:0000718 Aggressive behavior**. (krab2020delineationofphenotypes pages 12-14)

These manifestations can affect education, communication, independence, family burden, and social participation. Nevertheless, most reported RAD21-affected individuals attended mainstream or mild-support education, indicating generally better function than classic CdLS. CDLS4-specific EQ-5D, PROMIS, or SF-36 data are unavailable. (krab2020delineationofphenotypes pages 9-10)

### Other systems

- **Hearing:** hearing loss in approximately one-third in the 2020 clinical summary; HPO **HP:0000365 Hearing impairment**.
- **Vision:** usually normal, but optic-disc pallor and other abnormalities have been reported; HPO **HP:0000648 Optic atrophy** only when confirmed.
- **Cardiac:** congenital heart defects can include PDA, VSD, and tetralogy of Fallot; HPO **HP:0001643 Patent ductus arteriosus**, **HP:0001629 Ventricular septal defect**, **HP:0001636 Tetralogy of Fallot**. (deardorff2012rad21mutationscause pages 4-6, falco2023anovelvariant pages 4-7)
- **Palate/airway:** cleft palate and laryngomalacia; HPO **HP:0000175 Cleft palate**, **HP:0001601 Laryngomalacia**.
- **Gastrointestinal:** usually mild gastroesophageal reflux in early childhood, but gastrointestinal abnormalities occur; HPO **HP:0002020 Gastroesophageal reflux**.
- **Genitourinary:** renal/uterine anomalies are possible; an anomalous uterus was newly reported. HPO **HP:0000130 Abnormality of the uterus**. (krabUnknownyearphenotypesandgenotypes pages 1-2, abarcabarriga2023corneliadelange pages 1-2)

---

## 4. Genetic and molecular information

### Gene and protein

**RAD21** encodes the mitotic α-kleisin subunit that closes the cohesin ring with SMC1A and SMC3 and binds STAG1/STAG2. Relevant functions include sister-chromatid cohesion, chromosome segregation, DNA repair, replication, loop extrusion, enhancer–promoter communication, and transcriptional organization. Suggested annotations include GO biological processes **sister chromatid cohesion**, **chromosome segregation**, **DNA double-strand break repair**, **chromatin organization**, and **regulation of transcription by RNA polymerase II**; cellular components include **cohesin complex**, **chromosome**, and **nucleus**. (chin2020cohesinmutationsare pages 1-2, labudina2023cohesinmediatedcontrolof pages 19-23)

### Variant spectrum and classification

The 2020 series contained 24 different intragenic variants and seven unique microdeletions among 49 individuals. Variants were often private; missense changes tended to cluster near protein-binding interfaces. Microdeletions trended toward higher CdLS scores and greater growth impairment, but no robust difference in major malformations, cognition, or behavior was demonstrated. (krab2020delineationofphenotypes pages 1-2, krab2020delineationofphenotypes pages 6-7)

Illustrative variants:

- **c.1127C>G, p.Pro376Arg:** de novo missense; absent from >600 control chromosomes; altered STAG binding, cohesion, aneuploidy, and cell-cycle progression.
- **c.1753T>C, p.Cys585Arg:** de novo missense affecting the SMC1A interface.
- **c.1722_1723delTG, p.Gly575SerfsTer2:** de novo, likely pathogenic under ACMG/AMP PVS1+PM2; CADD 35; absent from gnomAD and 1000 Genomes; predicted C-terminal truncation, possibly escaping nonsense-mediated decay. (deardorff2012rad21mutationscause pages 6-7, falco2023anovelvariant pages 4-7)
- **8q24.11 deletion g.(116845458_116854956)x1, exons 9–14:** de novo 9,499-bp heterozygous deletion; removes STAG/SMC1-interacting C-terminal regions. RAD21 constraint metrics reported were LOEUF 0.26 and pLI 1. (abarcabarriga2023corneliadelange pages 2-6)

Pathogenic CDLS4 variants are germline constitutional variants. A VUS should not establish diagnosis without segregation, phenotype concordance, population rarity, computational/structural evidence, RNA studies, or functional validation.

### Chromosomal and epigenetic findings

Contiguous 8q24.1 deletions encompassing RAD21 can cause CDLS4-like phenotypes; neighboring genes can modify presentation. CMA is therefore complementary to sequence testing. No recurrent aneuploidy, balanced rearrangement, founder allele, or CDLS4-specific constitutional methylation signature is established. EpiSign-like methylation profiling is promising for cohesinopathies generally—a study cited in the 2024 review included 129 affected individuals—but it is not a validated standalone RAD21 test. (deardorff2012rad21mutationscause pages 4-6, grucastryjak2024advancingtheclinical pages 14-15)

No confirmed modifier gene or protective allele is available for clinical use.

---

## 5. Environmental information

CDLS4 is not caused by toxins, radiation, pollution, occupation, smoking, alcohol, diet, exercise, or an infectious agent. Such factors can affect general health or pregnancy but have no demonstrated etiologic role. There is no zoonotic or communicable component. Environmental and lifestyle modification cannot prevent a constitutional pathogenic RAD21 allele.

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A heterozygous pathogenic **RAD21** sequence variant or deletion **leads to** reduced RAD21 dosage or an abnormal RAD21 interaction surface.
2. Abnormal RAD21 **leads to** defective assembly, residence, or regulated opening of the SMC1A–SMC3–RAD21–STAG cohesin ring.
3. Altered cohesin **results in** abnormal sister-chromatid cohesion, chromosome segregation, DNA-damage signaling/repair, and three-dimensional chromatin organization; the relative contribution is allele-dependent. (deardorff2012rad21mutationscause pages 6-7, deardorff2012rad21mutationscause pages 7-8)
4. Disordered loop extrusion and nuclear organization **lead to** mistimed or quantitatively altered transcription, including delayed zygotic genome activation, abnormal RNA-polymerase-II foci, and disturbed ribosome/translation programs in zebrafish; extrapolation to human embryos is strongly plausible but partly inferred. (meier2018cohesinfacilitateszygotic pages 14-17, meier2018cohesinfacilitateszygotic pages 1-5)
5. **Branch A:** transcriptional disruption in neural-crest programs—including Wnt/BMP, chemokine, cadherin, adhesion and guidance genes—**leads to** impaired cardiac neural-crest migration and **results in** outflow/looping, valve, and cardiac structural defects in zebrafish; the corresponding human causal path is inferred. (schuster2015aneuralcrest pages 13-15, schuster2015aneuralcrest pages 1-3)
6. **Branch B:** altered cohesin dosage **leads to** disturbed mesoderm induction, neuromesodermal-progenitor differentiation, runx1 regulation, and cell-cycle-gene expression, **resulting in** axial, skeletal, hematopoietic, and growth abnormalities in models; specific mapping to each human phenotype remains inferred. (labudina2024cohesincompositionand pages 6-9, labudina2024cohesincompositionand pages 1-4)
7. **Branch C:** impaired DNA repair and chromosome segregation **lead to** micronuclei, nucleoplasmic bridges, aneuploidy, and cell-cycle delay in patient-derived cells, potentially contributing to developmental cell loss or dysfunction; direct tissue-level causation in CDLS4 is not proven. (deardorff2012rad21mutationscause pages 6-7, deardorff2012rad21mutationscause pages 7-8)
8. The combined developmental transcription, genome-stability, and cell-fate defects **result in** the variable craniofacial, growth, neurodevelopmental, limb, cardiac, palatal, and organ phenotype of CDLS4.

### Experimental detail

**Human lymphoblastoid cells:** p.Pro376Arg cells showed closed chromosome arms in 76% versus 5% of controls and aneuploidy in 39% versus 7%. RAD21-mutant cells showed elevated basal DNA damage, increased micronuclei/nucleoplasmic bridges, sensitivity to ionizing radiation, and delayed repair. These findings demonstrate cellular dysfunction but do not prove that chromosome instability is the dominant cause of every congenital feature. (deardorff2012rad21mutationscause pages 6-7, deardorff2012rad21mutationscause pages 7-8)

**Zebrafish embryogenesis:** RAD21 depletion delays zygotic genome activation, redistributes cohesin toward active genes, disrupts nucleoli and RNA-polymerase-II transcription foci, and alters ribosome assembly, RNA processing, and translation. Suggested GO terms include **GO:0006351 DNA-templated transcription**, **GO:0042254 ribosome biogenesis**, **GO:0006412 translation**, **GO:0007049 cell cycle**, and **GO:0006281 DNA repair**. (meier2018cohesinfacilitateszygotic pages 14-17, meier2018cohesinfacilitateszygotic pages 1-5)

**2024 development/single-cell work:** rad21 mutants altered mesoderm induction and cell-cycle gene expression. RAD21 deficiency blocked neuromesodermal-progenitor differentiation; by contrast, STAG2 loss reduced Wnt signaling and EMT, demonstrating that different cohesin lesions are not mechanistically interchangeable. (labudina2024cohesincompositionand pages 6-9, labudina2024cohesincompositionand pages 1-4)

Relevant cell types and suggested CL terms are **neural crest cell (CL:0000333)**, **neuron (CL:0000540)**, **cardiomyocyte (CL:0000746)**, **mesodermal cell**, **neuromesodermal progenitor**, **hematopoietic stem cell (CL:0000037)**, fibroblast, and lymphoblast. Some specialized progenitor terms may require ontology-version validation.

No CDLS4-specific human metabolomic, lipidomic, spatial-transcriptomic, organoid, or validated single-cell atlas has been reported. Immune dysregulation is not an established defining mechanism. The best-supported molecular framing is a **developmental transcriptomopathy superimposed on allele-dependent genome-maintenance defects**.

---

## 7. Anatomical structures affected

- **Central nervous system:** brain development, head growth, speech/cognitive and behavioral networks; CNS imaging is symptom-driven. UBERON suggestions: **UBERON:0000955 brain**, cerebral cortex, cerebellum.
- **Craniofacial complex:** facial skeleton, palate, mandible, nose, eyebrows/hair follicles. UBERON: **head**, **palate**, **mandible**.
- **Cardiovascular system:** heart, septa, valves, outflow tract and great vessels. UBERON: **UBERON:0000948 heart**.
- **Musculoskeletal system:** upper limbs, radius/radial head, hands/digits, vertebral column. UBERON: upper limb, hand, radius, vertebral column.
- **Gastrointestinal/airway:** esophagus/stomach in reflux, palate/larynx in feeding and airway disease. UBERON: esophagus, stomach, larynx.
- **Auditory/visual systems:** inner/middle ear or auditory pathways; eye/optic nerve when affected.
- **Genitourinary system:** kidneys and female reproductive tract in a minority.

Subcellular localization is principally the **nucleus**, chromosomal chromatin, cohesin complex, and DNA-repair foci. Abnormalities are generally bilateral/systemic rather than consistently lateralized; individual limb or organ malformations can be asymmetric.

---

## 8. Temporal development

CDLS4 begins during embryogenesis. Facial, palatal, cardiac, limb, and organ malformations are congenital. Growth restriction can be prenatal, but in many RAD21 cases short stature and microcephaly become more evident postnatally. Development is slow rather than degenerative, with speech especially affected. Mild gastroesophageal reflux may be concentrated in infancy/early childhood. (krab2020delineationofphenotypes pages 9-10, krabUnknownyearphenotypesandgenotypes pages 1-2, falco2023anovelvariant pages 4-7)

There are no validated stages, remissions, relapsing episodes, or end-stage classification. The disease is lifelong; structural anomalies are stable after formation, whereas functional consequences and behavior change with development. The critical biological period is prenatal organogenesis, although early postnatal hearing, feeding, developmental, cardiac, and educational intervention offers the clearest practical opportunity.

---

## 9. Inheritance and population

### Inheritance

CDLS4 is predominantly **autosomal dominant**. Cases can be de novo or inherited from a mildly affected parent. Penetrance is not reliably quantified and may be incomplete for individual features; expressivity is highly variable. There is no evidence for anticipation, consanguinity dependence, or a founder effect. Rare **biallelic RAD21** variants have been associated with Mungan syndrome and should not be conflated with dominant CDLS4. (krab2020delineationofphenotypes pages 9-10, krab2020delineationofphenotypes pages 1-2)

If a parent carries a pathogenic variant, the transmission probability is **50% per pregnancy**, but severity cannot be predicted. If neither parent has the variant in tested tissue, recurrence is low but not zero because of gonadal mosaicism. Pan-CdLS consensus cites gonadal mosaicism around **0.89%**; this is not RAD21-specific. (kline2018diagnosisandmanagement pages 5-6)

### Epidemiology

CdLS overall is often estimated at approximately 1/10,000–1/30,000 live births, but this must not be assigned directly to CDLS4. (grucastryjak2024advancingtheclinical pages 1-2)

In a 2023 cohort of 716 CdLS probands, 422 (59%) received a molecular diagnosis and only six—approximately 1% of solved cases and 0.8% of the total cohort—had RAD21 findings. In an earlier 163-person cohort, RAD21 accounted for 1 case (0.6%). These are diagnostic-cohort proportions, not population prevalence. (kaur2023genomicanalysesin pages 5-5)

No robust CDLS4-specific prevalence, annual incidence, carrier frequency, sex ratio, age distribution, ethnic enrichment, or geographic clustering is available. Both sexes and multiple ancestries are affected.

---

## 10. Diagnostics

### Clinical criteria

The international CdLS score assigns two points to cardinal and one to suggestive features. **≥11 with ≥3 cardinal features** supports classic CdLS; **9–10 with ≥2 cardinal features** supports non-classic CdLS; **4–8 with ≥1 cardinal feature** warrants molecular testing. Because RAD21 disease is often attenuated, a low/non-classic score does not exclude CDLS4. (grucastryjak2024advancingtheclinical pages 1-2, kline2018diagnosisandmanagement pages 5-6)

### Recommended molecular strategy

1. **Multigene NGS panel** including at minimum RAD21, NIPBL, SMC1A, SMC3, HDAC8 and other contemporary CdLS/CdLS-like genes, with validated CNV calling.
2. **Deletion/duplication analysis** by MLPA or high-resolution CMA if sequence testing is negative or a CNV is suspected.
3. **Trio WES/WGS** for unsolved or atypical cases. In 178 previously negative probands, genome sequencing identified a cause in 60 (34%): 23 in known cohesin genes and 37 in overlapping-disorder genes. (kaur2023genomicanalysesin pages 10-11)
4. **Mosaicism assessment** using deep sequencing and, when suspicion persists, non-blood tissue such as uncultured skin fibroblasts or buccal cells. The 15–20% mosaic-NIPBL estimate is pan-CdLS rather than RAD21-specific. (kline2018diagnosisandmanagement pages 6-7, kline2018diagnosisandmanagement pages 5-6)
5. **RNA studies** for suspected splice/deep-intronic variants; parental segregation for every candidate variant.

The 2023 exons 9–14 deletion demonstrates that sequence-only analysis can miss pathogenic intragenic CNVs and that CMA/NGS are complementary. (abarcabarriga2023corneliadelange pages 2-6, abarcabarriga2023corneliadelange pages 7-8)

### Baseline clinical evaluation

At diagnosis: growth/head circumference, feeding and reflux, developmental and behavioral assessment, audiology, ophthalmology, echocardiography, renal ultrasound, musculoskeletal examination, and palate/airway evaluation. CNS MRI, EEG, GI studies, or other imaging are indication-driven. Pan-CdLS consensus reports cardiac anomalies in about 25% and renal malformations in about 10%; these percentages are not validated for CDLS4. (kline2018diagnosisandmanagement pages 6-7)

### Differential diagnosis

Consider NIPBL-, SMC1A-, SMC3-, and HDAC8-related CdLS; Wiedemann–Steiner syndrome; Coffin–Siris spectrum; KBG syndrome/ANKRD11; Rubinstein–Taybi syndrome; CHOPS/AFF4-related disease; BRD4-, EP300-, TAF1-, and other transcriptional-regulation disorders; and RAD21-associated holoprosencephaly or biallelic Mungan syndrome. (grucastryjak2024advancingtheclinical pages 14-15, krab2020delineationofphenotypes pages 1-2, kaur2023genomicanalysesin pages 3-4)

Population newborn screening, biochemical biomarkers, liquid biopsy, repeat-expansion testing, and mitochondrial testing are not indicated. Cascade testing is appropriate after a familial pathogenic variant is identified.

---

## 11. Outcome and prognosis

CDLS4-specific survival curves, mortality rates, and life-expectancy estimates do not exist. Applying pan-CdLS claims—such as a 10–20-year reduction in life expectancy—to RAD21 disease is uncertain, particularly because RAD21 phenotypes are often mild. (bahari2024anineyearoldgirl pages 4-5)

Long-term morbidity is driven by developmental/speech limitations, growth restriction, anxiety/ADHD/autistic traits, hearing loss, reflux/feeding problems, orthopedic restrictions, and congenital organ defects. Prognosis is generally more favorable than NIPBL-related classic CdLS: 55% of the comprehensively characterized RAD21 cohort had normal or only mildly impaired cognition, all assessed children ≥3 years used words, and most attended mainstream or mildly supported education. (krab2020delineationofphenotypes pages 9-10, krab2020delineationofphenotypes pages 6-7)

Poorer function may accompany major cardiac/palatal anomalies, marked growth restriction, hearing loss, or more disruptive alleles, but no validated prognostic biomarker exists. Variant class alone is insufficient because large deletions can coexist with normal cognition and family members carrying the same allele may differ substantially. (krab2020delineationofphenotypes pages 6-7, abarcabarriga2023corneliadelange pages 1-2)

---

## 12. Treatment

### Standard care

There is **no approved disease-modifying or RAD21-specific therapy**. Management is multidisciplinary and phenotype-directed:

- nutrition and feeding therapy; reflux treatment using standard pediatric approaches;
- speech/language therapy, augmentative communication where needed;
- physical and occupational therapy;
- individualized education and behavioral therapy;
- audiologic amplification/cochlear or ENT management as indicated;
- ophthalmic and dental care;
- standard cardiology, renal, orthopedic, cleft-palate, airway, and surgical management;
- treatment of anxiety, ADHD, sleep disturbance, aggression, or self-injury according to symptoms and specialist assessment.

Suggested NCIT intervention concepts include **Genetic Counseling**, **Physical Therapy**, **Occupational Therapy**, **Speech Therapy**, **Behavior Therapy**, **Nutritional Support**, **Hearing Aid**, **Cardiac Surgery**, and **Cleft Palate Repair**; exact NCIT identifiers should be terminology-service validated.

Anesthesia teams should anticipate airway difficulty: the consensus reported difficult intubation in approximately 50% of intubated CdLS children and possible adverse responses to midazolam. This is pan-CdLS evidence, not a CDLS4-specific rate. (kline2018diagnosisandmanagement pages 6-7)

### Trials and experimental treatment

- **NCT05829668:** recruiting children aged 3–15 years; function-based behavioral assessment, treatment, and parent training; target ≥80% reduction in problem behavior. Not genotype-specific. (NCT05829668 chunk 1)
- **NCT04381897:** NAC for repetitive/self-injurious behavior in ages 13–35; planned efficacy threshold includes ≥35% reduction on relevant ABC measures. Not RAD21-specific. (NCT04381897 chunk 2)
- **NCT06789783:** lithium carbonate, approximately 10 mg/kg twice daily for 52 weeks, with behavioral, cognitive, sleep, adaptive, quality-of-life and biomarker outcomes. Registry excerpts conflict on whether enrollment is restricted to NIPBL; the detailed eligibility excerpt specifies NIPBL, so it should not be represented as a CDLS4 trial without registry confirmation. (NCT06789783 chunk 3, NCT06789783 chunk 1)
- **NCT03113877:** autonomic-function observational pilot; terminated after one enrollee. (NCT03113877 chunk 1)

**Preclinical only:** L-leucine or α-ketoisocaproate stimulated mTOR-dependent translation and partially rescued rRNA/protein synthesis and craniofacial development in rad21-deficient zebrafish. Approximately 240 morphants and 60 transgenic mutants were analyzed per treatment group. This does **not** justify clinical supplementation outside research. (xu2015lleucinepartiallyrescues pages 1-2, xu2015lleucinepartiallyrescues pages 4-5)

No gene replacement, CRISPR, ASO, siRNA, mRNA, cell therapy, or pharmacogenomic dosing strategy has demonstrated clinical efficacy in CDLS4.

---

## 13. Prevention

### Primary prevention

There is no lifestyle, vaccine, environmental, or drug intervention that prevents a de novo RAD21 variant. Reproductive prevention options after variant identification include genetic counseling, parental testing, prenatal diagnosis using chorionic-villus or amniotic-fluid DNA, and preimplantation genetic testing for monogenic disease. Prenatal ultrasound may detect growth restriction, limb anomalies, facial profile, cardiac disease, or diaphragmatic hernia, but mild CDLS4 can evade sonographic detection. Pan-CdLS prenatal data found symmetric IUGR in 80%, limb anomalies in 66%, and abnormal facial profile in 50% of 73 cases; these figures should not be treated as RAD21-specific. (kline2018diagnosisandmanagement pages 5-6)

### Secondary and tertiary prevention

Early molecular diagnosis and baseline echocardiography, renal ultrasound, hearing/vision assessment, feeding evaluation, and developmental screening can prevent avoidable complications. Tertiary prevention consists of reflux/aspiration control, nutrition, cardiac and airway treatment, hearing correction, dental care, therapies, educational support, behavioral monitoring, and anesthesia planning. Routine childhood immunization applies; no disease-specific vaccine or prophylactic medicine exists.

---

## 14. Other species and natural disease

No well-established naturally occurring veterinary counterpart of human CDLS4, breed predisposition, zoonotic transmission, or cross-species infectious susceptibility was identified. RAD21 and cohesin function are deeply conserved across vertebrates and invertebrates, supporting comparative modeling, but experimentally engineered or depleted animals are **models**, not documented natural veterinary CDLS4.

Relevant taxa include **Homo sapiens (NCBI Taxon 9606)**, **Mus musculus (10090)**, **Danio rerio (7955)**, and **Drosophila melanogaster (7227)**. Species-specific RAD21 ortholog identifiers should be fetched directly from NCBI Gene/Alliance at database-ingestion time.

---

## 15. Model organisms

### Zebrafish

Zebrafish rad21 mutants, morphants, and partial-depletion models are the most informative CDLS4 systems.

- **Cardiac/neural crest model:** 70–80% Rad21 depletion caused small, poorly looping hearts, valve defects and reduced ejection. Cardiac neural-crest cells reached myocardium in 87% of controls versus 38% and 16% at increasing morpholino doses; 0/5 homozygous mutants had cardiac neural-crest cells. RNA-seq found 236 upregulated and 322 downregulated genes at FDR <0.05. (schuster2015aneuralcrest pages 12-13, schuster2015aneuralcrest pages 13-15, schuster2015aneuralcrest pages 1-3)
- **Zygotic-genome-activation model:** RAD21 depletion delayed ZGA and disrupted nucleoli, RNA-polymerase-II foci, and developmental transcription. (meier2018cohesinfacilitateszygotic pages 14-17, meier2018cohesinfacilitateszygotic pages 1-5)
- **2024 dosage/composition model:** heterozygous and homozygous rad21 mutations altered cell-cycle expression and mesoderm development; complete functional loss produced mitotic catastrophe and embryonic lethality. This study cautions against extrapolating mechanisms between RAD21 and STAG2 lesions. (labudina2024cohesincompositionand pages 6-9, labudina2024cohesincompositionand pages 1-4)
- **Therapeutic-screen model:** leucine/α-KIC partially rescued mTOR-dependent translation and morphology, but no human efficacy is established. (xu2015lleucinepartiallyrescues pages 1-2)

**Limitations:** morpholino dosage may exceed human haploinsufficiency; homozygous loss is lethal; zebrafish anatomy and developmental timing differ from humans; rescue of embryonic morphology is not equivalent to correction of lifelong neurodevelopment.

### Mouse and cellular models

Conditional cohesin models are useful because complete loss is embryonic lethal. RAD21-deficient patient lymphoblastoid cells model cohesion, aneuploidy, cell cycle, and DNA repair; isogenic human cell lines model chromatin/Wnt vulnerabilities. However, cancer-cell synthetic lethality with Wnt activation is not a treatment rationale for germline CDLS4. (deardorff2012rad21mutationscause pages 6-7, deardorff2012rad21mutationscause pages 7-8, chin2020cohesinmutationsare pages 1-2)

A mature CDLS4-specific human iPSC, organoid, spatial-transcriptomic, or knock-in mouse natural-history platform was not established in the retrieved evidence. Priority models should preserve heterozygosity and patient-specific alleles, compare haploinsufficient with interface-disrupting variants, and measure cell-type-specific transcription and chromatin architecture.

---

## Recent developments and expert interpretation

1. **2023 clinical expansion:** p.Gly575SerfsTer2 established that C-terminal truncation can produce classic-scoring disease with prenatal growth restriction, PDA/VSD, cleft palate and laryngomalacia; a separate exons 9–14 deletion case showed polydactyly and uterine anomaly but no recognized neurodevelopmental disorder, reinforcing poor predictability from deletion size alone. Publications: January and December 2023; URLs https://doi.org/10.3390/genes14010119 and https://doi.org/10.3390/genes14122212. (falco2023anovelvariant pages 4-7, abarcabarriga2023corneliadelange pages 1-2)
2. **2023 genomic implementation:** among 716 probands, molecular yield was 59%; RAD21 accounted for only six solved cases. Genome sequencing solved 34% of a previously negative 178-proband subset, supporting broad analysis after panel/CNV testing. Publication: June 2023; https://doi.org/10.1002/ajmg.a.63247. (kaur2023genomicanalysesin pages 5-5, kaur2023genomicanalysesin pages 10-11)
3. **2024 mechanism:** zebrafish work showed that cohesin **dosage** and **composition** have separable developmental effects; Wnt stimulation rescued STAG2 but not RAD21 mutants, arguing against treating “cohesinopathy” as one uniform pathway. Publication: June 2024; DOI link reported as https://doi.org/10.1101/2023.11.21.568176. (labudina2024cohesincompositionand pages 6-9, labudina2024cohesincompositionand pages 1-4)
4. **Expert synthesis:** current evidence favors a transcription/chromatin-development model, while patient-cell DNA-repair and segregation abnormalities show that RAD21 alleles can additionally perturb canonical cohesin functions. Which component dominates human organ pathology remains unresolved. (deardorff2012rad21mutationscause pages 7-8, meier2018cohesinfacilitateszygotic pages 14-17)

## Evidence gaps for knowledge-base annotation

- No reliable CDLS4 prevalence, incidence, penetrance, sex ratio, carrier frequency, survival curve, or formal natural-history staging.
- Phenotype frequencies derive from small, variably assessed cohorts; denominators must accompany every percentage.
- No validated circulating, biochemical, imaging, methylation, transcriptomic, proteomic, metabolomic, or prognostic biomarker specific to RAD21 disease.
- No established protective factor, modifier gene, gene–environment interaction, pharmacogenomic recommendation, or RAD21-specific clinical trial.
- No evidence of infectious, autoimmune, metabolic-enzyme, mitochondrial, or primary inflammatory etiology.
- PMID values were not consistently exposed in the retrieved records; DOI URLs and publication dates are therefore supplied rather than risking incorrect PMID assignment.

References

1. (krab2020delineationofphenotypes pages 1-2): Lianne C. Krab, Iñigo Marcos-Alcalde, Melissa Assaf, Meena Balasubramanian, Janne Bayer Andersen, Anne-Marie Bisgaard, David R. Fitzpatrick, Sanna Gudmundsson, Sylvia A. Huisman, Tugba Kalayci, Saskia M. Maas, Francisco Martinez, Shane McKee, Leonie A. Menke, Paul A. Mulder, Oliver D. Murch, Michael Parker, Juan Pie, Feliciano J. Ramos, Claudine Rieubland, Jill A. Rosenfeld Mokry, Emanuela Scarano, Marwan Shinawi, Paulino Gómez-Puertas, Zeynep Tümer, and Raoul C. Hennekam. Delineation of phenotypes and genotypes related to cohesin structural protein rad21. Human Genetics, 139:575-592, Mar 2020. URL: https://doi.org/10.1007/s00439-020-02138-2, doi:10.1007/s00439-020-02138-2. This article has 57 citations and is from a peer-reviewed journal.

2. (falco2023anovelvariant pages 4-7): Alessandro De Falco, Daniele De Brasi, Matteo Della Monica, Claudia Cesario, Stefano Petrocchi, Antonio Novelli, Giuseppe D’Alterio, Achille Iolascon, Mario Capasso, and Carmelo Piscopo. A novel variant in rad21 in cornelia de lange syndrome type 4: case report and bioinformatic analysis. Genes, 14:119, Jan 2023. URL: https://doi.org/10.3390/genes14010119, doi:10.3390/genes14010119. This article has 8 citations.

3. (abarcabarriga2023corneliadelange pages 1-2): Hugo H. Abarca-Barriga, Renzo Punil Luciano, and Flor Vásquez Sotomayor. Cornelia de lange syndrome caused by an intragenic heterozygous deletion in rad21 detected through very-high-resolution chromosomal microarray analysis. Genes, 14(12):2212, Dec 2023. URL: https://doi.org/10.3390/genes14122212, doi:10.3390/genes14122212. This article has 3 citations.

4. (deardorff2012rad21mutationscause pages 1-2): Matthew A. Deardorff, Jonathan J. Wilde, Melanie Albrecht, Emma Dickinson, Stephanie Tennstedt, Diana Braunholz, Maren Mönnich, Yuqian Yan, Weizhen Xu, María Concepcion Gil-Rodríguez, Dinah Clark, Hakon Hakonarson, Sara Halbach, Laura Daniela Michelis, Abhinav Rampuria, Eva Rossier, Stephanie Spranger, Lionel Van Maldergem, Sally Ann Lynch, Gabriele Gillessen-Kaesbach, Hermann-Josef Lüdecke, Robert G. Ramsay, Michael J. McKay, Ian D. Krantz, Huiling Xu, Julia A. Horsfield, and Frank J. Kaiser. Rad21 mutations cause a human cohesinopathy. American journal of human genetics, 90 6:1014-27, Jun 2012. URL: https://doi.org/10.1016/j.ajhg.2012.04.019, doi:10.1016/j.ajhg.2012.04.019. This article has 357 citations and is from a highest quality peer-reviewed journal.

5. (krab2020delineationofphenotypes pages 9-10): Lianne C. Krab, Iñigo Marcos-Alcalde, Melissa Assaf, Meena Balasubramanian, Janne Bayer Andersen, Anne-Marie Bisgaard, David R. Fitzpatrick, Sanna Gudmundsson, Sylvia A. Huisman, Tugba Kalayci, Saskia M. Maas, Francisco Martinez, Shane McKee, Leonie A. Menke, Paul A. Mulder, Oliver D. Murch, Michael Parker, Juan Pie, Feliciano J. Ramos, Claudine Rieubland, Jill A. Rosenfeld Mokry, Emanuela Scarano, Marwan Shinawi, Paulino Gómez-Puertas, Zeynep Tümer, and Raoul C. Hennekam. Delineation of phenotypes and genotypes related to cohesin structural protein rad21. Human Genetics, 139:575-592, Mar 2020. URL: https://doi.org/10.1007/s00439-020-02138-2, doi:10.1007/s00439-020-02138-2. This article has 57 citations and is from a peer-reviewed journal.

6. (krab2020delineationofphenotypes pages 6-7): Lianne C. Krab, Iñigo Marcos-Alcalde, Melissa Assaf, Meena Balasubramanian, Janne Bayer Andersen, Anne-Marie Bisgaard, David R. Fitzpatrick, Sanna Gudmundsson, Sylvia A. Huisman, Tugba Kalayci, Saskia M. Maas, Francisco Martinez, Shane McKee, Leonie A. Menke, Paul A. Mulder, Oliver D. Murch, Michael Parker, Juan Pie, Feliciano J. Ramos, Claudine Rieubland, Jill A. Rosenfeld Mokry, Emanuela Scarano, Marwan Shinawi, Paulino Gómez-Puertas, Zeynep Tümer, and Raoul C. Hennekam. Delineation of phenotypes and genotypes related to cohesin structural protein rad21. Human Genetics, 139:575-592, Mar 2020. URL: https://doi.org/10.1007/s00439-020-02138-2, doi:10.1007/s00439-020-02138-2. This article has 57 citations and is from a peer-reviewed journal.

7. (krab2020delineationofphenotypes pages 12-14): Lianne C. Krab, Iñigo Marcos-Alcalde, Melissa Assaf, Meena Balasubramanian, Janne Bayer Andersen, Anne-Marie Bisgaard, David R. Fitzpatrick, Sanna Gudmundsson, Sylvia A. Huisman, Tugba Kalayci, Saskia M. Maas, Francisco Martinez, Shane McKee, Leonie A. Menke, Paul A. Mulder, Oliver D. Murch, Michael Parker, Juan Pie, Feliciano J. Ramos, Claudine Rieubland, Jill A. Rosenfeld Mokry, Emanuela Scarano, Marwan Shinawi, Paulino Gómez-Puertas, Zeynep Tümer, and Raoul C. Hennekam. Delineation of phenotypes and genotypes related to cohesin structural protein rad21. Human Genetics, 139:575-592, Mar 2020. URL: https://doi.org/10.1007/s00439-020-02138-2, doi:10.1007/s00439-020-02138-2. This article has 57 citations and is from a peer-reviewed journal.

8. (abarcabarriga2023corneliadelange pages 2-6): Hugo H. Abarca-Barriga, Renzo Punil Luciano, and Flor Vásquez Sotomayor. Cornelia de lange syndrome caused by an intragenic heterozygous deletion in rad21 detected through very-high-resolution chromosomal microarray analysis. Genes, 14(12):2212, Dec 2023. URL: https://doi.org/10.3390/genes14122212, doi:10.3390/genes14122212. This article has 3 citations.

9. (kaur2023genomicanalysesin pages 5-5): Maninder Kaur, Justin Blair, Batsal Devkota, Sierra Fortunato, Dinah Clark, Audrey Lawrence, Jiwoo Kim, Wonwook Do, Benjamin Semeo, Olivia Katz, Devanshi Mehta, Nobuko Yamamoto, Emma Schindler, Zayd Al Rawi, Nina Wallace, Jonathan J. Wilde, Jennifer McCallum, Jinglan Liu, Dongbin Xu, Marie Jackson, Stefan Rentas, Ahmad Abou Tayoun, Zhang Zhe, Omar Abdul‐Rahman, Bill Allen, Moris A. Angula, Kwame Anyane‐Yeboa, Jesús Argente, Pamela H. Arn, Linlea Armstrong, Lina Basel‐Salmon, Gareth Baynam, Lynne M. Bird, Daniel Bruegger, Gaik‐Siew Ch'ng, David Chitayat, Robin Clark, Gerald F. Cox, Usha Dave, Elfrede DeBaere, Michael Field, John M. Graham Jr, Karen W. Gripp, Robert Greenstein, Neerja Gupta, Randy Heidenreich, Jodi Hoffman, Robert J. Hopkin, Kenneth L. Jones, Marilyn C. Jones, Ariana Kariminejad, Jillene Kogan, Baiba Lace, Julian Leroy, Sally Ann Lynch, Marie McDonald, Kirsten Meagher, Nancy Mendelsohn, Ieva Micule, John Moeschler, Sheela Nampoothiri, Kaoru Ohashi, Cynthia M. Powell, Subhadra Ramanathan, Salmo Raskin, Elizabeth Roeder, Marlene Rio, Alan F. Rope, Karan Sangha, Angela E. Scheuerle, Adele Schneider, Stavit Shalev, Victoria Siu, Rosemarie Smith, Cathy Stevens, Tinatin Tkemaladze, John Toimie, Helga Toriello, Anne Turner, Patricia G. Wheeler, Susan M. White, Terri Young, Kathleen M. Loomes, Mary Pipan, Ann Tokay Harrington, Elaine Zackai, Ramakrishnan Rajagopalan, Laura Conlin, Matthew A. Deardorff, Deborah McEldrew, Juan Pie, Feliciano Ramos, Antonio Musio, Antonie D. Kline, Kosuke Izumi, Sarah E. Raible, and Ian D. Krantz. Genomic analyses in cornelia de lange syndrome and related diagnoses: novel candidate genes, genotype–phenotype correlations and common mechanisms. American Journal of Medical Genetics Part A, 191:2113-2131, Jun 2023. URL: https://doi.org/10.1002/ajmg.a.63247, doi:10.1002/ajmg.a.63247. This article has 58 citations.

10. (deardorff2012rad21mutationscause pages 6-7): Matthew A. Deardorff, Jonathan J. Wilde, Melanie Albrecht, Emma Dickinson, Stephanie Tennstedt, Diana Braunholz, Maren Mönnich, Yuqian Yan, Weizhen Xu, María Concepcion Gil-Rodríguez, Dinah Clark, Hakon Hakonarson, Sara Halbach, Laura Daniela Michelis, Abhinav Rampuria, Eva Rossier, Stephanie Spranger, Lionel Van Maldergem, Sally Ann Lynch, Gabriele Gillessen-Kaesbach, Hermann-Josef Lüdecke, Robert G. Ramsay, Michael J. McKay, Ian D. Krantz, Huiling Xu, Julia A. Horsfield, and Frank J. Kaiser. Rad21 mutations cause a human cohesinopathy. American journal of human genetics, 90 6:1014-27, Jun 2012. URL: https://doi.org/10.1016/j.ajhg.2012.04.019, doi:10.1016/j.ajhg.2012.04.019. This article has 357 citations and is from a highest quality peer-reviewed journal.

11. (deardorff2012rad21mutationscause pages 7-8): Matthew A. Deardorff, Jonathan J. Wilde, Melanie Albrecht, Emma Dickinson, Stephanie Tennstedt, Diana Braunholz, Maren Mönnich, Yuqian Yan, Weizhen Xu, María Concepcion Gil-Rodríguez, Dinah Clark, Hakon Hakonarson, Sara Halbach, Laura Daniela Michelis, Abhinav Rampuria, Eva Rossier, Stephanie Spranger, Lionel Van Maldergem, Sally Ann Lynch, Gabriele Gillessen-Kaesbach, Hermann-Josef Lüdecke, Robert G. Ramsay, Michael J. McKay, Ian D. Krantz, Huiling Xu, Julia A. Horsfield, and Frank J. Kaiser. Rad21 mutations cause a human cohesinopathy. American journal of human genetics, 90 6:1014-27, Jun 2012. URL: https://doi.org/10.1016/j.ajhg.2012.04.019, doi:10.1016/j.ajhg.2012.04.019. This article has 357 citations and is from a highest quality peer-reviewed journal.

12. (meier2018cohesinfacilitateszygotic pages 14-17): Michael Meier, Jenny Grant, Amy Dowdle, Amarni Thomas, Jennifer E. Gerton, Philippe Collas, Justin M. O'Sullivan, and Julia A. Horsfield. Cohesin facilitates zygotic genome activation in zebrafish. Development, Jan 2018. URL: https://doi.org/10.1242/dev.156521, doi:10.1242/dev.156521. This article has 77 citations and is from a domain leading peer-reviewed journal.

13. (schuster2015aneuralcrest pages 12-13): Kevin Schuster, Bryony Leeke, Michael Meier, Yizhou Wang, Trent Newman, Sean Burgess, and Julia A. Horsfield. A neural crest origin for cohesinopathy heart defects. Human molecular genetics, 24 24:7005-16, Dec 2015. URL: https://doi.org/10.1093/hmg/ddv402, doi:10.1093/hmg/ddv402. This article has 47 citations and is from a domain leading peer-reviewed journal.

14. (labudina2024cohesincompositionand pages 6-9): Anastasia A. Labudina, Michael Meier, Gregory Gimenez, David Tatarakis, Sarada Ketharnathan, Bridget Mackie, Thomas F. Schilling, Jisha Antony, and Julia A. Horsfield. Cohesin composition and dosage independently affect early development in zebrafish. Development (Cambridge, England), Jun 2024. URL: https://doi.org/10.1101/2023.11.21.568176, doi:10.1101/2023.11.21.568176. This article has 5 citations.

15. (kline2018diagnosisandmanagement pages 5-6): AD Kline, JF Moss, A Selicorni, and AM Bisgaard. Diagnosis and management of cornelia de lange syndrome: first international consensus statement: expert consensus document. Unknown journal, 2018.

16. (kline2018diagnosisandmanagement pages 6-7): AD Kline, JF Moss, A Selicorni, and AM Bisgaard. Diagnosis and management of cornelia de lange syndrome: first international consensus statement: expert consensus document. Unknown journal, 2018.

17. (grucastryjak2024advancingtheclinical pages 14-15): Karolina Gruca-Stryjak, Emilia Doda-Nowak, Julia Dzierla, Karolina Wróbel, Marta Szymankiewicz-Bręborowicz, and Jan Mazela. Advancing the clinical and molecular understanding of cornelia de lange syndrome: a multidisciplinary pediatric case series and review of the literature. Apr 2024. URL: https://doi.org/10.3390/jcm13082423, doi:10.3390/jcm13082423. This article has 6 citations.

18. (NCT06789783 chunk 3): Aglaia Vignoli. Cornelia De Lange Syndrome: Assessing Positive Effects of Lithium Treatment. University of Milan. 2024. ClinicalTrials.gov Identifier: NCT06789783

19. (NCT05829668 chunk 1): Patricia Kurtz. Behavioral Assessment and Treatment of Problem Behavior in Children With Cornelia de Lange Syndrome. Hugo W. Moser Research Institute at Kennedy Krieger, Inc.. 2023. ClinicalTrials.gov Identifier: NCT05829668

20. (NCT03113877 chunk 1): Amie E. Jones, M.D.. Evaluation of Autonomic Function in Individuals With Cornelia de Lange Syndrome (CdLS). Mayo Clinic. 2016. ClinicalTrials.gov Identifier: NCT03113877

21. (NCT04381897 chunk 2):  Use of N-Acetylcysteine in the Treatment of Repetitive and Self-Injurious Behaviors in Cornelia de Lange Syndrome. Johns Hopkins University. 2026. ClinicalTrials.gov Identifier: NCT04381897

22. (grucastryjak2024advancingtheclinical pages 15-17): Karolina Gruca-Stryjak, Emilia Doda-Nowak, Julia Dzierla, Karolina Wróbel, Marta Szymankiewicz-Bręborowicz, and Jan Mazela. Advancing the clinical and molecular understanding of cornelia de lange syndrome: a multidisciplinary pediatric case series and review of the literature. Apr 2024. URL: https://doi.org/10.3390/jcm13082423, doi:10.3390/jcm13082423. This article has 6 citations.

23. (falco2023anovelvariant pages 2-4): Alessandro De Falco, Daniele De Brasi, Matteo Della Monica, Claudia Cesario, Stefano Petrocchi, Antonio Novelli, Giuseppe D’Alterio, Achille Iolascon, Mario Capasso, and Carmelo Piscopo. A novel variant in rad21 in cornelia de lange syndrome type 4: case report and bioinformatic analysis. Genes, 14:119, Jan 2023. URL: https://doi.org/10.3390/genes14010119, doi:10.3390/genes14010119. This article has 8 citations.

24. (deardorff2012rad21mutationscause pages 3-4): Matthew A. Deardorff, Jonathan J. Wilde, Melanie Albrecht, Emma Dickinson, Stephanie Tennstedt, Diana Braunholz, Maren Mönnich, Yuqian Yan, Weizhen Xu, María Concepcion Gil-Rodríguez, Dinah Clark, Hakon Hakonarson, Sara Halbach, Laura Daniela Michelis, Abhinav Rampuria, Eva Rossier, Stephanie Spranger, Lionel Van Maldergem, Sally Ann Lynch, Gabriele Gillessen-Kaesbach, Hermann-Josef Lüdecke, Robert G. Ramsay, Michael J. McKay, Ian D. Krantz, Huiling Xu, Julia A. Horsfield, and Frank J. Kaiser. Rad21 mutations cause a human cohesinopathy. American journal of human genetics, 90 6:1014-27, Jun 2012. URL: https://doi.org/10.1016/j.ajhg.2012.04.019, doi:10.1016/j.ajhg.2012.04.019. This article has 357 citations and is from a highest quality peer-reviewed journal.

25. (deardorff2012rad21mutationscause pages 4-6): Matthew A. Deardorff, Jonathan J. Wilde, Melanie Albrecht, Emma Dickinson, Stephanie Tennstedt, Diana Braunholz, Maren Mönnich, Yuqian Yan, Weizhen Xu, María Concepcion Gil-Rodríguez, Dinah Clark, Hakon Hakonarson, Sara Halbach, Laura Daniela Michelis, Abhinav Rampuria, Eva Rossier, Stephanie Spranger, Lionel Van Maldergem, Sally Ann Lynch, Gabriele Gillessen-Kaesbach, Hermann-Josef Lüdecke, Robert G. Ramsay, Michael J. McKay, Ian D. Krantz, Huiling Xu, Julia A. Horsfield, and Frank J. Kaiser. Rad21 mutations cause a human cohesinopathy. American journal of human genetics, 90 6:1014-27, Jun 2012. URL: https://doi.org/10.1016/j.ajhg.2012.04.019, doi:10.1016/j.ajhg.2012.04.019. This article has 357 citations and is from a highest quality peer-reviewed journal.

26. (chin2020cohesinmutationsare pages 1-2): Chue Vin Chin, Jisha Antony, Sarada Ketharnathan, Anastasia Labudina, Gregory Gimenez, Kate M Parsons, Jinshu He, Amee J George, Maria Michela Pallotta, Antonio Musio, Antony Braithwaite, Parry Guilford, Ross D Hannan, and Julia A Horsfield. Cohesin mutations are synthetic lethal with stimulation of wnt signaling. Dec 2020. URL: https://doi.org/10.7554/elife.61405, doi:10.7554/elife.61405. This article has 31 citations and is from a domain leading peer-reviewed journal.

27. (falco2023anovelvariant pages 7-8): Alessandro De Falco, Daniele De Brasi, Matteo Della Monica, Claudia Cesario, Stefano Petrocchi, Antonio Novelli, Giuseppe D’Alterio, Achille Iolascon, Mario Capasso, and Carmelo Piscopo. A novel variant in rad21 in cornelia de lange syndrome type 4: case report and bioinformatic analysis. Genes, 14:119, Jan 2023. URL: https://doi.org/10.3390/genes14010119, doi:10.3390/genes14010119. This article has 8 citations.

28. (krabUnknownyearphenotypesandgenotypes pages 1-2): LC Krab and SA Huisman. Phenotypes and genotypes of individuals with rad21 variants. Unknown journal, Unknown year.

29. (abarcabarriga2023corneliadelange pages 7-8): Hugo H. Abarca-Barriga, Renzo Punil Luciano, and Flor Vásquez Sotomayor. Cornelia de lange syndrome caused by an intragenic heterozygous deletion in rad21 detected through very-high-resolution chromosomal microarray analysis. Genes, 14(12):2212, Dec 2023. URL: https://doi.org/10.3390/genes14122212, doi:10.3390/genes14122212. This article has 3 citations.

30. (labudina2023cohesinmediatedcontrolof pages 19-23): A Labudina. Cohesin-mediated control of cell fate determination in zebrafish development. Unknown journal, 2023.

31. (meier2018cohesinfacilitateszygotic pages 1-5): Michael Meier, Jenny Grant, Amy Dowdle, Amarni Thomas, Jennifer E. Gerton, Philippe Collas, Justin M. O'Sullivan, and Julia A. Horsfield. Cohesin facilitates zygotic genome activation in zebrafish. Development, Jan 2018. URL: https://doi.org/10.1242/dev.156521, doi:10.1242/dev.156521. This article has 77 citations and is from a domain leading peer-reviewed journal.

32. (schuster2015aneuralcrest pages 13-15): Kevin Schuster, Bryony Leeke, Michael Meier, Yizhou Wang, Trent Newman, Sean Burgess, and Julia A. Horsfield. A neural crest origin for cohesinopathy heart defects. Human molecular genetics, 24 24:7005-16, Dec 2015. URL: https://doi.org/10.1093/hmg/ddv402, doi:10.1093/hmg/ddv402. This article has 47 citations and is from a domain leading peer-reviewed journal.

33. (schuster2015aneuralcrest pages 1-3): Kevin Schuster, Bryony Leeke, Michael Meier, Yizhou Wang, Trent Newman, Sean Burgess, and Julia A. Horsfield. A neural crest origin for cohesinopathy heart defects. Human molecular genetics, 24 24:7005-16, Dec 2015. URL: https://doi.org/10.1093/hmg/ddv402, doi:10.1093/hmg/ddv402. This article has 47 citations and is from a domain leading peer-reviewed journal.

34. (labudina2024cohesincompositionand pages 1-4): Anastasia A. Labudina, Michael Meier, Gregory Gimenez, David Tatarakis, Sarada Ketharnathan, Bridget Mackie, Thomas F. Schilling, Jisha Antony, and Julia A. Horsfield. Cohesin composition and dosage independently affect early development in zebrafish. Development (Cambridge, England), Jun 2024. URL: https://doi.org/10.1101/2023.11.21.568176, doi:10.1101/2023.11.21.568176. This article has 5 citations.

35. (grucastryjak2024advancingtheclinical pages 1-2): Karolina Gruca-Stryjak, Emilia Doda-Nowak, Julia Dzierla, Karolina Wróbel, Marta Szymankiewicz-Bręborowicz, and Jan Mazela. Advancing the clinical and molecular understanding of cornelia de lange syndrome: a multidisciplinary pediatric case series and review of the literature. Apr 2024. URL: https://doi.org/10.3390/jcm13082423, doi:10.3390/jcm13082423. This article has 6 citations.

36. (kaur2023genomicanalysesin pages 10-11): Maninder Kaur, Justin Blair, Batsal Devkota, Sierra Fortunato, Dinah Clark, Audrey Lawrence, Jiwoo Kim, Wonwook Do, Benjamin Semeo, Olivia Katz, Devanshi Mehta, Nobuko Yamamoto, Emma Schindler, Zayd Al Rawi, Nina Wallace, Jonathan J. Wilde, Jennifer McCallum, Jinglan Liu, Dongbin Xu, Marie Jackson, Stefan Rentas, Ahmad Abou Tayoun, Zhang Zhe, Omar Abdul‐Rahman, Bill Allen, Moris A. Angula, Kwame Anyane‐Yeboa, Jesús Argente, Pamela H. Arn, Linlea Armstrong, Lina Basel‐Salmon, Gareth Baynam, Lynne M. Bird, Daniel Bruegger, Gaik‐Siew Ch'ng, David Chitayat, Robin Clark, Gerald F. Cox, Usha Dave, Elfrede DeBaere, Michael Field, John M. Graham Jr, Karen W. Gripp, Robert Greenstein, Neerja Gupta, Randy Heidenreich, Jodi Hoffman, Robert J. Hopkin, Kenneth L. Jones, Marilyn C. Jones, Ariana Kariminejad, Jillene Kogan, Baiba Lace, Julian Leroy, Sally Ann Lynch, Marie McDonald, Kirsten Meagher, Nancy Mendelsohn, Ieva Micule, John Moeschler, Sheela Nampoothiri, Kaoru Ohashi, Cynthia M. Powell, Subhadra Ramanathan, Salmo Raskin, Elizabeth Roeder, Marlene Rio, Alan F. Rope, Karan Sangha, Angela E. Scheuerle, Adele Schneider, Stavit Shalev, Victoria Siu, Rosemarie Smith, Cathy Stevens, Tinatin Tkemaladze, John Toimie, Helga Toriello, Anne Turner, Patricia G. Wheeler, Susan M. White, Terri Young, Kathleen M. Loomes, Mary Pipan, Ann Tokay Harrington, Elaine Zackai, Ramakrishnan Rajagopalan, Laura Conlin, Matthew A. Deardorff, Deborah McEldrew, Juan Pie, Feliciano Ramos, Antonio Musio, Antonie D. Kline, Kosuke Izumi, Sarah E. Raible, and Ian D. Krantz. Genomic analyses in cornelia de lange syndrome and related diagnoses: novel candidate genes, genotype–phenotype correlations and common mechanisms. American Journal of Medical Genetics Part A, 191:2113-2131, Jun 2023. URL: https://doi.org/10.1002/ajmg.a.63247, doi:10.1002/ajmg.a.63247. This article has 58 citations.

37. (kaur2023genomicanalysesin pages 3-4): Maninder Kaur, Justin Blair, Batsal Devkota, Sierra Fortunato, Dinah Clark, Audrey Lawrence, Jiwoo Kim, Wonwook Do, Benjamin Semeo, Olivia Katz, Devanshi Mehta, Nobuko Yamamoto, Emma Schindler, Zayd Al Rawi, Nina Wallace, Jonathan J. Wilde, Jennifer McCallum, Jinglan Liu, Dongbin Xu, Marie Jackson, Stefan Rentas, Ahmad Abou Tayoun, Zhang Zhe, Omar Abdul‐Rahman, Bill Allen, Moris A. Angula, Kwame Anyane‐Yeboa, Jesús Argente, Pamela H. Arn, Linlea Armstrong, Lina Basel‐Salmon, Gareth Baynam, Lynne M. Bird, Daniel Bruegger, Gaik‐Siew Ch'ng, David Chitayat, Robin Clark, Gerald F. Cox, Usha Dave, Elfrede DeBaere, Michael Field, John M. Graham Jr, Karen W. Gripp, Robert Greenstein, Neerja Gupta, Randy Heidenreich, Jodi Hoffman, Robert J. Hopkin, Kenneth L. Jones, Marilyn C. Jones, Ariana Kariminejad, Jillene Kogan, Baiba Lace, Julian Leroy, Sally Ann Lynch, Marie McDonald, Kirsten Meagher, Nancy Mendelsohn, Ieva Micule, John Moeschler, Sheela Nampoothiri, Kaoru Ohashi, Cynthia M. Powell, Subhadra Ramanathan, Salmo Raskin, Elizabeth Roeder, Marlene Rio, Alan F. Rope, Karan Sangha, Angela E. Scheuerle, Adele Schneider, Stavit Shalev, Victoria Siu, Rosemarie Smith, Cathy Stevens, Tinatin Tkemaladze, John Toimie, Helga Toriello, Anne Turner, Patricia G. Wheeler, Susan M. White, Terri Young, Kathleen M. Loomes, Mary Pipan, Ann Tokay Harrington, Elaine Zackai, Ramakrishnan Rajagopalan, Laura Conlin, Matthew A. Deardorff, Deborah McEldrew, Juan Pie, Feliciano Ramos, Antonio Musio, Antonie D. Kline, Kosuke Izumi, Sarah E. Raible, and Ian D. Krantz. Genomic analyses in cornelia de lange syndrome and related diagnoses: novel candidate genes, genotype–phenotype correlations and common mechanisms. American Journal of Medical Genetics Part A, 191:2113-2131, Jun 2023. URL: https://doi.org/10.1002/ajmg.a.63247, doi:10.1002/ajmg.a.63247. This article has 58 citations.

38. (bahari2024anineyearoldgirl pages 4-5): Hanae Bahari, Hind Zahiri, Aziza Elouali, Maria Rkain, and Abdeladim Babakhouya. A nine-year-old girl with cornelia de lange syndrome: a case report and review of the literature. Nov 2024. URL: https://doi.org/10.7759/cureus.74007, doi:10.7759/cureus.74007. This article has 0 citations.

39. (NCT06789783 chunk 1): Aglaia Vignoli. Cornelia De Lange Syndrome: Assessing Positive Effects of Lithium Treatment. University of Milan. 2024. ClinicalTrials.gov Identifier: NCT06789783

40. (xu2015lleucinepartiallyrescues pages 1-2): Baoshan Xu, Nenja Sowa, Maria E. Cardenas, and Jennifer L. Gerton. L-leucine partially rescues translational and developmental defects associated with zebrafish models of cornelia de lange syndrome. Human Molecular Genetics, 24:1540-1555, Nov 2015. URL: https://doi.org/10.1093/hmg/ddu565, doi:10.1093/hmg/ddu565. This article has 47 citations and is from a domain leading peer-reviewed journal.

41. (xu2015lleucinepartiallyrescues pages 4-5): Baoshan Xu, Nenja Sowa, Maria E. Cardenas, and Jennifer L. Gerton. L-leucine partially rescues translational and developmental defects associated with zebrafish models of cornelia de lange syndrome. Human Molecular Genetics, 24:1540-1555, Nov 2015. URL: https://doi.org/10.1093/hmg/ddu565, doi:10.1093/hmg/ddu565. This article has 47 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Cornelia_De_Lange_Syndrome_4-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 12 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 47 |
| Resolved | 47 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013864` (2 mentions) - the report calls it "if available"; MONDO calls it **Cornelia de Lange syndrome 4**