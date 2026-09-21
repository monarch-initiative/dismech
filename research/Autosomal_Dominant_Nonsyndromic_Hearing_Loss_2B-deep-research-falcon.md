---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-28T19:01:28.256778'
end_time: '2026-08-28T19:09:06.099808'
duration_seconds: 457.84
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Dominant Nonsyndromic Hearing Loss 2B (DFNA2B, GJB3-related)
  mondo_id: MONDO:0012976
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 15
reference_validation:
  total_references: 9
  verified: 7
  not_found: 2
  unverifiable: 0
  confabulation_rate: 0.222
  relevance_assessed: 7
  on_topic: 3
  unresolved_references:
  - DOI:10.1002/(sici)1096-8628(19990924)89:3
  - DOI:10.1002/(sici
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 6
  verified: 6
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0012976
    reported_labels:
    - if available
    ontology_label: autosomal dominant nonsyndromic hearing loss 2B
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Autosomal_Dominant_Nonsyndromic_Hearing_Loss_2B-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Dominant Nonsyndromic Hearing Loss 2B (DFNA2B, GJB3-related)
- **MONDO ID:** MONDO:0012976 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Nonsyndromic Hearing Loss 2B (DFNA2B, GJB3-related)** covering all of the
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
- **Disease Name:** Autosomal Dominant Nonsyndromic Hearing Loss 2B (DFNA2B, GJB3-related)
- **MONDO ID:** MONDO:0012976 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Nonsyndromic Hearing Loss 2B (DFNA2B, GJB3-related)** covering all of the
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


# Autosomal Dominant Nonsyndromic Hearing Loss 2B (DFNA2B; historically GJB3-related)

## Executive summary and evidence qualification

DFNA2B is the historical designation for a rare, autosomal-dominant, nonsyndromic sensorineural hearing-loss phenotype attributed to heterozygous variants in **GJB3**, which encodes connexin-31 (Cx31). The reported phenotype is usually postlingual, bilateral, progressive, and greatest at high frequencies. A 2023 review places typical recognition in the fourth decade and reports milder loss in females. However, the underlying evidence consists principally of a few small families, and several observations weaken a simple monogenic interpretation: some purported variants occur at appreciable population frequencies, later families show multigenic ambiguity, DFNA2 is genetically heterogeneous, and **Gjb3-null mice have normal hearing**. Accordingly, a GJB3 result should not establish DFNA2B without rigorous ACMG/AMP classification, phenotype matching, segregation, population-frequency review, and exclusion of better-established hearing-loss genes. (dominguez2012geneticsofhearing pages 5-6, alde2023autosomaldominantnonsyndromic pages 2-3, chen2018gjb3gjb6screeningin pages 2-4, petersen2002non‐syndromicautosomal‐dominantdeafness pages 2-4, wingard2015cellularanddeafness pages 8-9)

| domain | strongest finding | evidence type | confidence/caveat |
|---|---|---|---|
| Historical gene-disease association | DFNA2B was historically attributed to **GJB3/connexin 31** based on **two small Chinese autosomal-dominant families** with high-frequency hearing loss; later reviews note the evidence base is limited and DFNA2 is genetically heterogeneous. (petersen2002non‐syndromicautosomal‐dominantdeafness pages 2-4, dominguez2012geneticsofhearing pages 5-6) | Human family reports summarized in reviews | **Low-moderate confidence** for a historical association; small pedigrees and later contradictory/heterogeneous DFNA2 data limit certainty. |
| Core phenotype | Reported DFNA2B phenotype is **adult-onset**, **progressive**, **sloping/high-frequency** sensorineural hearing loss; a 2023 review states hearing loss may be **milder in females**. (alde2023autosomaldominantnonsyndromic pages 2-3, laer1999autosomaldominantnonsyndromic pages 2-3, petersen2002non‐syndromicautosomal‐dominantdeafness pages 2-4) | Human clinical reviews | **Moderate confidence** for the broad audiophenotype; **low confidence** for sex effect because it is sparsely documented in secondary summaries. |
| Functional variant evidence | In vitro studies summarized in a mechanistic review report **V27M, V43M, and V84I** can reach the membrane yet show **loss of dye/ion coupling**, supporting impaired gap-junction function. (wingard2015cellularanddeafness pages 7-8) | In vitro cell-based functional assays (secondary summary) | **Moderate confidence** that these variants can disrupt coupling in cells; direct disease causality in humans remains less certain. |
| Trafficking mechanism | **V174M** was reported to **fail plasma-membrane targeting** and instead accumulate in **lysosomes**; it may also disturb wild-type Cx26 trafficking. (wingard2015cellularanddeafness pages 8-9) | In vitro transfected-cell study (secondary summary) | **Moderate confidence** for a trafficking-defect mechanism; relevance to penetrance and phenotype in vivo is unresolved. |
| Animal-model calibration | **Gjb3/Cx31-null mice do not show hearing impairment**, despite human variant-based disease claims. (wingard2015cellularanddeafness pages 8-9) | Mouse knockout model | **Important caveat / lowers confidence** in a simple haploinsufficiency model; dominant-negative, species-specific, or developmental-context mechanisms remain possible. |
| Cohort/population evidence | In a **2018 Chinese cohort** of 100 unrelated NSHI families, **one** putatively relevant **p.V84I** finding was detected; the paper estimated a very low allele frequency and interpreted the case as **digenic/tri-allelic GJB2/GJB3 ambiguity**, not clean monogenic proof. (chen2018gjb3gjb6screeningin pages 2-4) | Human cohort + segregation/NGS follow-up | **Low-moderate confidence** for contribution of p.V84I; the same study emphasizes ambiguity and possible additive rather than standalone causation. |
| Current therapy landscape | **No DFNA2B/GJB3-specific approved therapy** was identified; management follows general hereditary hearing-loss care (audiology, hearing aids/cochlear implantation as indicated, counseling). Recent precision-diagnostics literature supports broad NGS-based diagnosis rather than gene-specific treatment. (imizcoz2023nextgenerationsequencingimproves pages 1-2, alde2023autosomaldominantnonsyndromic pages 2-3) | Recent clinical review + diagnostic cohort | **High confidence** that no disease-specific therapy currently exists; treatment evidence is extrapolated from broader hereditary hearing-loss practice. |
| Trial/implementation status | The only retrieved GJB3-relevant registered study was **NCT06133946**, an **observational newborn deafness-gene screening cohort**, not an intervention trial; it includes a single GJB3 variant among screened targets. (NCT06133946 chunk 1) | ClinicalTrials.gov observational study | **High confidence** that current registered activity is screening/epidemiologic rather than therapeutic. |


*Table: This table summarizes the strongest currently retrievable evidence for the historical DFNA2B–GJB3 association, highlighting where support comes from human families, cell studies, mouse models, and modern screening data. It is useful because the evidence is mixed and requires careful confidence calibration rather than a simple yes/no interpretation.*

## 1. Disease information

### Definition

DFNA2B describes inherited nonsyndromic sensorineural hearing loss historically linked to **GJB3/Cx31** at chromosome **1p34.3**. “Nonsyndromic” means that hearing loss is the principal recognized manifestation; skin disease or peripheral neuropathy should prompt consideration of a distinct, syndromic GJB3-associated phenotype rather than DFNA2B. Historical reports also associated biallelic GJB3 variants with recessive hearing loss, but that is not DFNA2B. (petersen2002non‐syndromicautosomal‐dominantdeafness pages 2-4, alde2023autosomaldominantnonsyndromic pages 2-3)

### Identifiers and synonyms

- **Requested MONDO identifier:** MONDO:0012976. This identifier should be independently verified before database ingestion. The retrieved current Open Targets mapping did **not** reproduce it; instead, it returned GJB3 against “autosomal dominant nonsyndromic hearing loss 58,” MONDO:0014293, with only one low-scoring evidence item. This discordance is a material ontology-quality warning. (OpenTargets Search: autosomal dominant nonsyndromic hearing loss 2B-GJB3)
- **Common names:** DFNA2B; deafness, autosomal dominant 2B; autosomal dominant nonsyndromic hearing loss 2B; GJB3-related nonsyndromic hearing loss; connexin-31-related hearing loss.
- **Gene identifiers:** GJB3, *gap junction protein beta 3*; protein Cx31/connexin-31; Ensembl ENSG00000188910. (OpenTargets Search: autosomal dominant nonsyndromic hearing loss 2B-GJB3)
- **Cytogenetic location:** 1p34.3 in the 2023 review; older literature used the broader 1p33–p35 interval. (alde2023autosomaldominantnonsyndromic pages 2-3, petersen2002non‐syndromicautosomal‐dominantdeafness pages 2-4)
- **OMIM/Orphanet:** no disease-specific accession was securely recovered in the searched full text; these should be curated directly from the live databases rather than inferred.
- **ICD-10/ICD-11 and MeSH:** there is no established genotype-specific clinical code in the retrieved evidence. Use the appropriate bilateral sensorineural/genetic hearing-loss code plus molecular diagnosis; MeSH concepts include *Hearing Loss, Sensorineural* and *Hearing Loss, Hereditary*.

The evidence summarized here is aggregated disease-level literature, family studies, experimental models, and a trial registry—not individual EHR-derived data.

## 2. Etiology

### Causal and genetic factors

The proposed primary cause is a germline heterozygous GJB3 variant affecting connexin-31 gap-junction function. The original 1998 report described one missense and one nonsense change in two small Chinese families with autosomal-dominant high-frequency hearing loss (Xia et al., published December 1998, DOI: https://doi.org/10.1038/3845). Historical reviews subsequently assigned this association to DFNA2B. (petersen2002non‐syndromicautosomal‐dominantdeafness pages 2-4)

The association is not uniformly secure. DFNA2 also includes the well-established **KCNQ4/DFNA2A** disorder, and some pedigrees mapping to the region had no causal change in either GJB3 or KCNQ4. In the five-generation UCSF-99 family, sequence changes in both genes occurred in affected and unaffected relatives, arguing against either as causal in that family. These findings demonstrate locus and allelic heterogeneity and make broad use of “DFNA2” as a synonym for GJB3 disease incorrect. (dominguez2012geneticsofhearing pages 5-6)

### Risk factors

- A genuinely pathogenic germline allele and an affected parent are the principal proposed risks; for an established heterozygous autosomal-dominant allele, each child has a theoretical 50% transmission probability.
- Family history may appear negative because of late onset, reduced/age-dependent penetrance, mild expression, or a de novo event. These are general DFNA principles rather than quantified GJB3-specific observations. (alde2023autosomaldominantnonsyndromic pages 2-3)
- One 2018 Chinese cohort found GJB3 p.Val84Ile in 1/100 unrelated families with monoallelic GJB2 findings. The authors estimated a 0.5% cohort allele frequency, cited approximately 0.25% among Chinese NSHI cases and 0.0037 in 1000 Genomes, and interpreted the family as possibly digenic/tri-allelic **GJB2/GJB3**, not clean GJB3 monogenic disease. (chen2018gjb3gjb6screeningin pages 2-4)

### Environmental, protective, and gene–environment factors

No DFNA2B-specific toxin, infection, lifestyle factor, protective allele, diet, or validated modifier gene was identified. Noise and ototoxic drugs can independently damage hearing and plausibly add to inherited cochlear vulnerability, but a GJB3-specific interaction has not been demonstrated. General environmental causes—including congenital infection, postnatal infection, ototoxicity, and prematurity—account for a substantial fraction of pediatric hearing loss and must remain in the differential rather than being attributed to GJB3. (imizcoz2023nextgenerationsequencingimproves pages 1-2)

## 3. Phenotypes

The best-supported phenotype is **sensorineural hearing impairment**, initially affecting high frequencies, with a sloping audiogram and progressive postlingual course. Older summaries report similar audiograms among affected individuals and suggest that clinically evident loss occurred particularly in older male carriers; the 2023 review describes onset in adulthood, commonly the fourth decade, and milder loss in females. These sex and onset estimates derive from very small historical datasets and should not be treated as precise frequencies. (alde2023autosomaldominantnonsyndromic pages 2-3, laer1999autosomaldominantnonsyndromic pages 2-3)

Suggested HPO annotations are:

- Sensorineural hearing impairment — **HP:0000407**
- High-frequency hearing impairment — **HP:0005101**
- Progressive hearing impairment — **HP:0001730**
- Postlingual hearing impairment — use the current HPO postlingual-onset hearing-loss term after terminology validation
- Adult onset — **HP:0003581**
- Bilateral hearing impairment — apply the current HPO bilateral-hearing-loss term; bilateral disease is typical for DFNA generally but was not explicitly quantified in the original GJB3 families.

Severity ranges from mild or subclinical to moderate in the most specific GJB3 summaries. Profound congenital loss reported with p.Val84Ile occurred in a family also carrying biallelic GJB2 changes and therefore should not define monogenic DFNA2B. Peripheral neuropathy occurred with an in-frame three-base deletion in a Spanish family and is a **syndromic exclusion/red flag**, not a core DFNA2B feature. GJB3 variants also cause erythrokeratodermia variabilis; skin findings likewise argue against a nonsyndromic classification. (chen2018gjb3gjb6screeningin pages 2-4, petersen2002non‐syndromicautosomal‐dominantdeafness pages 2-4)

No disease-specific quality-of-life instrument has been reported. Expected burdens include impaired speech perception—especially in noise—communication difficulty, educational or occupational limitations, and social/emotional effects. General pediatric evidence indicates that early etiologic diagnosis and intervention improve language, cognitive, emotional, and social development. (imizcoz2023nextgenerationsequencingimproves pages 1-2)

## 4. Genetic and molecular information

**GJB3** encodes a connexin subunit. Six connexins oligomerize into a connexon/hemichannel; connexons in adjacent cells dock to create a gap-junction channel permitting intercellular passage of ions, metabolites, and second messengers. (laer1999autosomaldominantnonsyndromic pages 2-3)

Reported classes include missense, nonsense, and in-frame deletion variants. Functionally studied candidates include:

- **p.Val27Met, p.Val43Met, p.Val84Ile:** reached the plasma membrane and formed plaques in cell systems but showed loss of dye and ion permeability.
- **p.Val174Met:** failed normal membrane targeting, accumulated in lysosomes, and interfered with wild-type Cx26 trafficking while reportedly not altering wild-type Cx31 trafficking.
- **p.Val84Ile (c.250G>A; rs145751680):** computationally damaging and functionally abnormal in vitro, but sufficiently frequent and observed in a multigenic family, making standalone pathogenicity uncertain. (chen2018gjb3gjb6screeningin pages 2-4, wingard2015cellularanddeafness pages 7-8, wingard2015cellularanddeafness pages 8-9)

These assays support loss of channel coupling or abnormal trafficking but do not by themselves prove a variant causes dominant human hearing loss. A dominant-negative or altered heteromeric-channel mechanism is more compatible with normal hearing in Gjb3-null mice than simple haploinsufficiency, although this remains an inference. (wingard2015cellularanddeafness pages 8-9)

All reported inherited disease variants are germline; no somatic origin is relevant. No reproducible GJB3-specific modifier gene, epigenetic signature, pathogenic copy-number alteration, translocation, inversion, or other chromosomal abnormality was identified. GJB2 is a plausible interacting connexin in selected reports, but evidence for digenic causation is limited. (chen2018gjb3gjb6screeningin pages 2-4)

## 5. Environmental information

No infectious agent causes DFNA2B, and the disorder is not transmissible. Smoking, alcohol, exercise, diet, pollution, radiation, or occupational exposures have not been shown to determine GJB3 penetrance. Clinically, ordinary hearing-conservation measures remain prudent because noise and ototoxic exposure can independently worsen auditory function. Infection, prematurity, and ototoxicity should be evaluated as alternative or additional etiologies, especially when onset or progression does not fit the family phenotype. (imizcoz2023nextgenerationsequencingimproves pages 1-2)

## 6. Mechanism and pathophysiology

### Proposed causal chain

1. A GJB3 sequence variant alters Cx31 folding, trafficking, connexon assembly, docking, gating, or molecular permeability.
2. Gap-junctional transfer of ions and signaling/metabolic molecules among inner-ear nonsensory/supporting cells—or possibly auditory/peripheral nerve cells—is reduced or qualitatively changed.
3. Cochlear homeostasis and cellular coupling become less robust.
4. High-frequency auditory function is affected first, producing a sloping audiogram; dysfunction then progresses to lower frequencies.

Steps 1–2 have cell-based support for selected variants; steps 3–4 remain a biologically plausible but incompletely demonstrated bridge in GJB3 disease. Historical chicken data localized Cx31 to cells lining the scala media but not hair cells, while rat inner-ear expression was also reported. Human cochlear localization remains poorly defined. (laer1999autosomaldominantnonsyndromic pages 2-3, petersen2002non‐syndromicautosomal‐dominantdeafness pages 2-4, wingard2015cellularanddeafness pages 8-9)

The traditional “potassium recycling” account should not be stated as established for Cx31. Connexin channels also transmit metabolites, ATP/IP3-related signals, and calcium-wave information, and modern connexin work has challenged potassium-recycling failure as a universal explanation. No GJB3-specific immune, inflammatory, metabolic, lipidomic, metabolomic, or oxidative-stress signature has been established. (wingard2015cellularanddeafness pages 7-8, wingard2015cellularanddeafness pages 8-9)

Suggested annotations include:

- GO: gap junction assembly; gap-junction-mediated intercellular transport; cell–cell signaling; ion transmembrane transport; cellular homeostasis.
- GO cellular components: gap junction; connexin complex; plasma membrane; lysosome for trafficking-defective p.Val174Met.
- Candidate cell types: cochlear supporting/nonsensory epithelial cell; auditory-neuron/Schwann-cell populations only where demonstrated. Use exact CL identifiers after ontology validation.

No DFNA2B-specific single-cell, spatial-transcriptomic, multi-omic, CRISPR-screen, proteomic, metabolomic, or lipidomic study was identified through 2024.

## 7. Anatomical structures affected

The primary organ is the **inner ear/cochlea**, within the auditory system. Candidate sites include the scala-media-lining epithelium and auditory nerve, but direct human pathology is lacking. Hair cells themselves were excluded from Cx31 expression in the cited chicken work, so direct hair-cell expression should not be asserted. (laer1999autosomaldominantnonsyndromic pages 2-3)

Suggested anatomical terms include UBERON: inner ear; cochlea; scala media; organ of Corti; stria vascularis; spiral ligament; cochlear nerve. These are candidate knowledge-base annotations and not all are proven GJB3-expression sites. The clinical pattern is expected to be bilateral; no consistent asymmetry, vestibular-organ disease, or secondary-organ involvement is established for nonsyndromic DFNA2B. Peripheral nerve or skin involvement changes the classification to a syndromic GJB3 phenotype. (petersen2002non‐syndromicautosomal‐dominantdeafness pages 2-4)

## 8. Temporal development

The disease is chronic and generally insidious. Current secondary synthesis describes onset in the fourth decade, while older DFNA literature broadly places autosomal-dominant nonsyndromic loss in the second or third decade. Initial high-frequency impairment may be mild or subclinical and progressively involves more frequencies. There are no validated clinical stages, quantified annual threshold shifts, remission pattern, or spontaneous recovery. (alde2023autosomaldominantnonsyndromic pages 2-3, laer1999autosomaldominantnonsyndromic pages 2-3)

The practical intervention window begins before communication disability becomes substantial: identify at-risk relatives, establish baseline audiometry, and monitor serially. Childhood-onset or congenital profound hearing loss should trigger aggressive reassessment for other genes or acquired causes rather than automatic attribution to classic DFNA2B.

## 9. Inheritance and population

The historical model is autosomal dominant, affecting both sexes, with 50% transmission risk from a heterozygous parent. Expression appears variable and may be age- and sex-dependent; neither penetrance nor the male:female ratio has been quantified. Anticipation, germline mosaicism, founder effects, consanguinity effects, and carrier frequency have not been established. (alde2023autosomaldominantnonsyndromic pages 2-3, laer1999autosomaldominantnonsyndromic pages 2-3)

No reliable prevalence or incidence estimate exists for DFNA2B. The original evidence involved two small Chinese families; a Spanish family had hearing loss plus neuropathy. A later Chinese series found only one p.Val84Ile-positive family among 100 selected cases and did not establish monogenic GJB3 causation. Therefore, ethnicity-specific enrichment and geographic prevalence cannot currently be inferred. (chen2018gjb3gjb6screeningin pages 2-4, petersen2002non‐syndromicautosomal‐dominantdeafness pages 2-4)

For context only, disabling hearing loss affects over 5% of the global population, and hearing loss occurs in approximately 1–2 per 1,000 European newborns; these are not DFNA2B-specific estimates. (imizcoz2023nextgenerationsequencingimproves pages 1-2)

## 10. Diagnostics

Diagnosis should combine:

1. History: age at onset, progression, noise/ototoxic exposure, infections, and a three-generation pedigree.
2. Examination: otologic assessment plus targeted examination for skin disease and peripheral neuropathy.
3. Audiology: pure-tone thresholds, speech testing, tympanometry, otoacoustic emissions, and ABR/ASSR where age or phenotype warrants.
4. Molecular testing: a comprehensive hereditary-hearing-loss NGS panel with SNV/indel and CNV detection is preferable to GJB3-only testing. Confirm candidate variants orthogonally and perform segregation analysis.
5. Interpretation: ACMG/AMP classification, population-frequency review, phenotype concordance, and analysis of competing genes—especially **KCNQ4**, GJB2, GJB6, TECTA, WFS1, ACTG1, POU4F3, MYO6, and EYA4.

A 2023 Spanish study of a 171-nuclear/8-mitochondrial-gene panel produced a diagnosis in **52/155 (34%)** cases; 45/52 diagnoses were recessive, 6/52 dominant, 1/52 mitochondrial, and 3/52 involved pathogenic CNVs. Its abstract states that NGS panels “reduce the clinical diagnostic odyssey in hearing loss.” Published 22 September 2023; DOI: https://doi.org/10.3389/fgene.2023.1264899. This supports broad genomic testing, not the validity of any particular GJB3 allele. (imizcoz2023nextgenerationsequencingimproves pages 1-2)

WES or WGS is appropriate after a nondiagnostic panel or for complex/atypical families. CMA, karyotype, FISH, mitochondrial testing, and repeat-expansion testing are not routine DFNA2B tests unless another clinical indication exists. RNA-seq and other omics remain research tools.

Differential diagnoses include KCNQ4-related DFNA2A, other dominant nonsyndromic hearing losses, age-related and noise-induced hearing loss, ototoxicity, congenital infection, auditory neuropathy, and GJB3-associated neuropathy or erythrokeratodermia. Cascade testing is appropriate only after a familial variant has been convincingly classified.

## 11. Outcome and prognosis

DFNA2B is not known to shorten life expectancy or cause disease-specific mortality. Morbidity is auditory and communication-related. Hearing loss is generally permanent and progressive rather than episodic or remitting. Prognosis depends on baseline thresholds, rate of progression, speech discrimination, age, environmental exposures, and timely rehabilitation; no validated GJB3 molecular prognostic biomarker exists. (alde2023autosomaldominantnonsyndromic pages 2-3, laer1999autosomaldominantnonsyndromic pages 2-3)

Untreated loss can impair communication, education, work, and psychosocial well-being. Hearing technology can improve function but does not correct the molecular defect. Disease-specific hearing-aid or cochlear-implant response rates have not been published.

## 12. Treatment

There is no approved GJB3-directed drug, gene therapy, RNA therapy, cell therapy, or genome-editing treatment. Standard management is phenotype-directed:

- serial audiologic monitoring;
- properly fitted hearing aids for aidable loss;
- assistive listening devices and communication accommodations;
- auditory rehabilitation and speech/language support;
- cochlear-implant evaluation for severe-to-profound loss with inadequate aided speech recognition;
- treatment of unrelated middle-ear disease and avoidance of unnecessary ototoxic exposure.

Suggested NCIT concepts include Hearing Aid, Cochlear Implantation, Audiologic Evaluation, Speech Therapy, Rehabilitation Therapy, and Genetic Counseling; exact codes should be validated against the current NCIt release.

ClinicalTrials.gov **NCT06133946 (CODES)** is not a therapy trial. It is an observational Nantong newborn cohort enrolling 35,920 participants, screening 15 variants in GJB2, SLC26A4, MT-RNR1, and GJB3 (c.538C>T), with ABR/ASSR and developmental follow-up. Recruitment ran January 2016–December 2020; the record is active but not recruiting, with estimated completion in December 2028. (NCT06133946 chunk 1)

## 13. Prevention

Primary prevention of a germline disorder is not available. Risk reduction consists of genetic counseling and reproductive options after confirmation of a pathogenic familial allele: prenatal diagnosis or preimplantation genetic testing may be considered according to patient values and local regulations. Because GJB3 pathogenicity is frequently uncertain, reproductive testing should not be based on a VUS.

Secondary prevention includes cascade testing, baseline audiometry, periodic surveillance, newborn hearing screening, and prompt rehabilitation. Tertiary prevention includes hearing conservation, avoidance of unnecessary ototoxic drugs, communication support, and timely hearing aids or implantation. Vaccination does not prevent DFNA2B but routine immunization can reduce selected acquired infectious causes of hearing loss.

## 14. Other species and natural disease

Orthologous **Gjb3** exists in mouse and other vertebrates. No naturally occurring veterinary disorder convincingly equivalent to human DFNA2B was identified, and there is no zoonotic or cross-species transmission. Conserved connexin architecture makes vertebrates useful for comparative channel biology, but species differences are important: complete Cx31 deficiency in mice causes transient placental dysmorphogenesis without hearing impairment. (wingard2015cellularanddeafness pages 8-9)

Suggested taxonomy annotations include *Homo sapiens* (NCBI Taxon 9606), *Mus musculus* (10090), *Rattus norvegicus* (10116), and *Gallus gallus* (9031) for the expression evidence. No relevant VBO breed term is applicable.

## 15. Model organisms and experimental systems

### Mouse

The Gjb3/Cx31 knockout is the most important calibration model. It does **not** reproduce human hearing loss, although placental abnormalities occur transiently. Consequently, it argues against uncomplicated loss-of-function/haploinsufficiency as the universal human mechanism and limits its use as a faithful DFNA2B efficacy model. It remains useful for studying redundancy among connexins and extra-auditory biology. (wingard2015cellularanddeafness pages 8-9)

### Cellular systems

HEK293 and HeLa transfection systems have assessed localization, plaque formation, dye transfer, ionic coupling, and interactions with Cx26. They demonstrate functional abnormalities for selected variants, including defective permeability and lysosomal retention, but overexpression, noncochlear cellular context, and uncertain connexin stoichiometry limit translation. (chen2018gjb3gjb6screeningin pages 2-4, wingard2015cellularanddeafness pages 7-8, wingard2015cellularanddeafness pages 8-9)

No validated GJB3 patient-derived iPSC cochlear organoid, humanized knock-in mouse, zebrafish disease model, or CRISPR therapeutic model was identified. High-priority future work includes patient-derived cochlear-like cells, variant-specific knock-in models, allele-specific expression studies, direct human inner-ear localization, and large pedigree-based segregation with modern population databases.

## Recent-development assessment (2023–2024)

The principal recent advance is diagnostic rather than GJB3-specific: broad NGS/CNV pipelines are increasingly implemented for genetically heterogeneous hearing loss, with a 34% yield in one 2023 Spanish cohort. The 2023 DFNA review still lists GJB3/DFNA2B and describes fourth-decade, progressive, sloping hearing loss, but it does not resolve the sparse primary evidence or normal-hearing knockout contradiction. No 2023–2024 disease-specific natural-history cohort, validated prevalence study, therapy trial, single-cell atlas analysis, or variant-reclassification study was retrieved. (alde2023autosomaldominantnonsyndromic pages 2-3, imizcoz2023nextgenerationsequencingimproves pages 1-2, wingard2015cellularanddeafness pages 8-9)

## Knowledge-base recommendation

Represent DFNA2B as a **historical/provisional GJB3-associated dominant nonsyndromic hearing-loss entity with limited evidence**, not as an unequivocally established diagnosis for every rare GJB3 variant. Store variant-level assertions separately, record the evidence type, and flag p.Val84Ile and other incompletely segregating alleles for expert review. The highest-value missing data are modern ClinGen-style gene–disease curation, current ClinVar/gnomAD variant review, larger pedigrees, human inner-ear expression data, and variant-specific in-vivo models.

References

1. (dominguez2012geneticsofhearing pages 5-6): L. M. Dominguez and K. Dodson. Genetics of hearing loss: focus on dfna2. The Application of Clinical Genetics, 5:97-104, Oct 2012. URL: https://doi.org/10.2147/tacg.s35525, doi:10.2147/tacg.s35525. This article has 24 citations.

2. (alde2023autosomaldominantnonsyndromic pages 2-3): Mirko Aldè, Giovanna Cantarella, Diego Zanetti, Lorenzo Pignataro, Ignazio La Mantia, Luigi Maiolino, Salvatore Ferlito, Paola Di Mauro, Salvatore Cocuzza, Jérôme René Lechien, Giannicola Iannella, Francois Simon, and Antonino Maniaci. Autosomal dominant non-syndromic hearing loss (dfna): a comprehensive narrative review. Biomedicines, 11:1616, Jun 2023. URL: https://doi.org/10.3390/biomedicines11061616, doi:10.3390/biomedicines11061616. This article has 65 citations.

3. (chen2018gjb3gjb6screeningin pages 2-4): Kaitian Chen, Xuan Wu, Ling Zong, and Hongyan Jiang. Gjb3/gjb6 screening in gjb2 carriers with idiopathic hearing loss: is it necessary? Journal of Clinical Laboratory Analysis, Jun 2018. URL: https://doi.org/10.1002/jcla.22592, doi:10.1002/jcla.22592. This article has 12 citations and is from a peer-reviewed journal.

4. (petersen2002non‐syndromicautosomal‐dominantdeafness pages 2-4): MB Petersen. Non‐syndromic autosomal‐dominant deafness. Clinical Genetics, 62:1-13, Jul 2002. URL: https://doi.org/10.1034/j.1399-0004.2002.620101.x, doi:10.1034/j.1399-0004.2002.620101.x. This article has 117 citations and is from a peer-reviewed journal.

5. (wingard2015cellularanddeafness pages 8-9): Jeffrey C. Wingard and Hong-Bo Zhao. Cellular and deafness mechanisms underlying connexin mutation-induced hearing loss – a common hereditary deafness. Frontiers in Cellular Neuroscience, May 2015. URL: https://doi.org/10.3389/fncel.2015.00202, doi:10.3389/fncel.2015.00202. This article has 199 citations.

6. (laer1999autosomaldominantnonsyndromic pages 2-3): Lut Van Laer, Wyman T. McGuirt, Tao Yang, Richard J.H. Smith, and Guy Van Camp. Autosomal dominant nonsyndromic hearing impairment. American journal of medical genetics, 89 3:167-74, Sep 1999. URL: https://doi.org/10.1002/(sici)1096-8628(19990924)89:3<167::aid-ajmg7>3.0.co;2-v, doi:10.1002/(sici)1096-8628(19990924)89:3<167::aid-ajmg7>3.0.co;2-v. This article has 52 citations.

7. (wingard2015cellularanddeafness pages 7-8): Jeffrey C. Wingard and Hong-Bo Zhao. Cellular and deafness mechanisms underlying connexin mutation-induced hearing loss – a common hereditary deafness. Frontiers in Cellular Neuroscience, May 2015. URL: https://doi.org/10.3389/fncel.2015.00202, doi:10.3389/fncel.2015.00202. This article has 199 citations.

8. (imizcoz2023nextgenerationsequencingimproves pages 1-2): T. Imizcoz, C. Prieto-Matos, R. Manrique-Huarte, D. Calavia, A. Huarte, P. C. Pruneda, G. R. Ordoñez, E. Cañada-Higueras, A. Patiño-García, G. Alkorta-Aranburu, M. M. Rodríguez, Kelvin Yuen-Kwong, Chan, Sze Wing Cheng, and S. Taiber. Next-generation sequencing improves precision medicine in hearing loss. Frontiers in Genetics, Sep 2023. URL: https://doi.org/10.3389/fgene.2023.1264899, doi:10.3389/fgene.2023.1264899. This article has 15 citations and is from a peer-reviewed journal.

9. (NCT06133946 chunk 1): Gang Qin, MD, PhD. Cohort Of DEafness-gene Screening. Affiliated Hospital of Nantong University. 2016. ClinicalTrials.gov Identifier: NCT06133946

10. (OpenTargets Search: autosomal dominant nonsyndromic hearing loss 2B-GJB3): Open Targets Query (autosomal dominant nonsyndromic hearing loss 2B-GJB3, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

## Artifacts

- [Edison artifact artifact-00](Autosomal_Dominant_Nonsyndromic_Hearing_Loss_2B-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 2 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 3 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.1002/(sici)1096-8628(19990924)89:3` (2 mentions) - Identifier did not resolve to a record
- `DOI:10.1002/(sici` (1 mention) - Identifier did not resolve to a record

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0012976` (2 mentions) - the report calls it "if available"; MONDO calls it **autosomal dominant nonsyndromic hearing loss 2B**