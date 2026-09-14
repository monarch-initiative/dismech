---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-28T15:08:12.544624'
end_time: '2026-08-28T15:21:15.593843'
duration_seconds: 783.05
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Aspergillosis
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 21
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 24
  verified: 24
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 11
  labels_matching: 8
  labels_variant: 3
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Aspergillosis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Aspergillosis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Aspergillosis** covering all of the
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
- **Disease Name:** Aspergillosis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Aspergillosis** covering all of the
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


# Aspergillosis: comprehensive disease-characteristics report

## Executive summary and evidence scope

Aspergillosis is a family of diseases caused by *Aspergillus* spp., principally *A. fumigatus*, after inhalation of ubiquitous airborne conidia. Clinical expression is governed less by exposure alone than by the interaction among fungal strain, lung architecture, and host immunity: immune overactivity produces allergic disease; structural lung damage favors chronic infection and fungal balls; profound immune dysfunction permits tissue-invasive and disseminated disease. A 2024 European Respiratory Journal review identifies sensitization, allergic bronchopulmonary aspergillosis (ABPA), aspergilloma, chronic pulmonary aspergillosis (CPA), and invasive pulmonary aspergillosis (IPA) as the major pulmonary phenotypes (jaggi2024fungallungdisease pages 3-4, jaggi2024fungallungdisease pages 1-3).

The evidence below is chiefly aggregated disease-level evidence from guidelines, reviews, clinical cohorts, functional experiments, and trial registries—not individual-level EHR data. Exact PMIDs were not exposed for most retrieved 2023–2024 papers; DOI URLs and dates are therefore supplied rather than inventing PMID values. Proposed ontology mappings should be verified against the current ontology release before production ingestion.

The principal clinical spectrum is summarized here:

| Form | Dominant host state/risk | Mechanism | Hallmark phenotype/imaging/biomarker | Typical course | Core treatment |
|---|---|---|---|---|---|
| ABPA | Asthma or cystic fibrosis; also reported with COPD/bronchiectasis | Allergic/type-2 immune reaction to Aspergillus colonization/sensitization | A. fumigatus-specific IgE ≥0.35 kUA/L; total IgE ≥500 IU/mL; often eosinophils ≥500/µL; suggestive CT findings and/or mucus plugging/bronchiectasis | Relapsing exacerbations; can progress to bronchiectasis or pleuropulmonary fibrosis | Oral prednisolone or itraconazole monotherapy for acute disease; combination prednisolone+itraconazole for recurrent exacerbations; biologics/nebulized amphotericin in selected cases |
| Aspergillus bronchitis / sensitization | Chronic airway disease, especially severe asthma or cystic fibrosis; risk increased by inhaled corticosteroids, antibiotics, prior exacerbations | Persistent superficial airway infection or immune sensitization without invasive tissue disease | Sensitization: fungus-specific IgE ≥0.35 kUA/L; bronchitis: positive sputum/BAL culture or PCR with elevated Aspergillus IgG | Chronic or recurrent airway symptoms | Itraconazole-based antifungal therapy in selected bronchitis; airway-disease optimization |
| Aspergilloma / CPA | Structural lung disease, especially pulmonary cavitation; COPD, prior TB or other chronic lung damage | Chronic colonization/infection of cavities with local tissue destruction but no deep invasion | CT cavitary disease or fungal ball; Aspergillus IgG positive; hemoptysis common (∼50%) | Chronic, progressive over months to years; high long-term mortality | Oral azoles first line (itraconazole/voriconazole; alternatives posaconazole/isavuconazole) with prolonged therapy >6 months and often ≥12 months; surgery for localized/simple aspergilloma; bronchial artery embolization for major hemoptysis |
| Invasive pulmonary aspergillosis | Prolonged severe neutropenia, graft-versus-host disease, hematologic malignancy, transplant, prolonged corticosteroids/immunosuppressants; also severe viral critical illness | Inhaled conidia germinate to hyphae with tissue invasion, angioinvasion, thrombosis, necrosis, and hemorrhage | CT dense well-circumscribed lesion ± halo sign, air-crescent sign, cavity, or wedge-shaped consolidation; serum or BAL galactomannan ≥1.0; Aspergillus PCR positivity; culture/microscopy supportive | Acute/subacute, rapidly progressive, high mortality if delayed diagnosis | Triazoles first choice, individualized (voriconazole or isavuconazole commonly used); adjunctive immune optimization/immunomodulation when feasible |
| Extrapulmonary / disseminated aspergillosis | Usually profoundly immunocompromised patients following pulmonary invasion and hematogenous spread | Dissemination from a primary focus with organ invasion outside lung | Evidence of Aspergillus in extrapulmonary tissue or compatible multisite disease; no single universal biomarker threshold established here | Acute, severe, often life-threatening | Systemic antifungal therapy centered on triazoles; organ-directed management and reduction of immunosuppression when possible |


*Table: This table summarizes the major clinical forms of aspergillosis across host states, mechanisms, hallmark findings, course, and core treatments. It is useful as a quick disease-spectrum reference built only from gathered evidence. (jaggi2024fungallungdisease pages 8-9, tashiro2024chronicpulmonaryaspergillosis pages 1-2, heylen2024acuteinvasivepulmonary pages 1-2, jaggi2024fungallungdisease pages 4-5, jaggi2024fungallungdisease pages 5-7, heylen2024acuteinvasivepulmonary pages 6-7)*

## 1. Disease information

### Definition and forms

* **Aspergillosis:** infection, colonization-associated disease, or hypersensitivity caused by *Aspergillus*.
* **Allergic disease:** *Aspergillus* sensitization and ABPA, generally complicating asthma, cystic fibrosis (CF), bronchiectasis, or COPD.
* **Airway disease:** *Aspergillus* bronchitis or tracheobronchitis.
* **Chronic disease:** simple aspergilloma, chronic cavitary pulmonary aspergillosis, chronic fibrosing pulmonary aspergillosis, and subacute invasive aspergillosis.
* **Invasive disease:** acute IPA, invasive tracheobronchial disease, extrapulmonary focal infection, or hematogenously disseminated aspergillosis.

### Identifiers and synonyms

* **MONDO:** aspergillosis **MONDO:0005657**; ABPA **MONDO:0015243**; pulmonary aspergilloma **MONDO:0000266** (OpenTargets Search: aspergillosis).
* **MeSH:** *Aspergillosis*; subordinate concepts include pulmonary, allergic bronchopulmonary, and invasive forms.
* **ICD-10-CM:** B44 family—B44.0 invasive pulmonary, B44.1 other pulmonary, B44.2 tonsillar, B44.7 disseminated, B44.81 ABPA, B44.89 other, B44.9 unspecified. Coding should be checked against the jurisdictional release.
* **ICD-11:** fungal-disease chapter contains aspergillosis and clinical extensions; the precise current URI/code should be resolved directly from the ICD-11 release.
* **OMIM/Orphanet:** no single Mendelian disease entry appropriately represents all aspergillosis. Host immunodeficiencies predisposing to disease have separate entries.
* **Synonyms:** aspergillus infection; invasive aspergillosis; IPA; chronic pulmonary aspergillosis/CPA; aspergilloma or fungus ball; ABPA; invasive fungal tracheobronchitis.

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal agent and exposure

The immediate cause is exposure to viable conidia followed by fungal persistence, germination, or antigen-driven inflammation. Humans may inhale roughly 100–1,000 conidia daily. Normal mucociliary and innate defenses usually remove them; failed clearance permits germination into hyphae (heylen2024acuteinvasivepulmonary pages 1-2).

Important species are *A. fumigatus* worldwide, with *A. flavus*, *A. terreus*, *A. niger*, and cryptic species contributing regionally. *A. flavus* may be relatively prominent in hot/arid regions and was particularly common in one pediatric hematology cohort. Geography, climate, environment, fungal genotype, and host comorbidities materially alter disease distribution (jaggi2024fungallungdisease pages 3-4, jaggi2024fungallungdisease pages 4-5).

### Clinical risk factors

* **IPA:** neutrophils below 0.5×10⁹/L for more than 10 days; acute leukemia; hematopoietic-cell or solid-organ transplantation; graft-versus-host disease; inherited severe immunodeficiency; T- or B-cell immunosuppressants; corticosteroids at approximately ≥0.3 mg/kg/day for ≥3 weeks in the preceding 60 days; and critical illness with severe influenza or COVID-19 (heylen2024acuteinvasivepulmonary pages 1-2, heylen2024acuteinvasivepulmonary pages 6-7).
* **CPA:** a pre-existing cavity is the strongest anatomical risk. Prior tuberculosis or nontuberculous mycobacterial disease, COPD/emphysema, bronchiectasis, sarcoidosis, lung cancer, and previous thoracic procedures are typical substrates (tashiro2024chronicpulmonaryaspergillosis pages 1-2).
* **ABPA:** asthma and CF are classical; bronchiectasis and COPD are now recognized predisposing conditions. Repeated fungal exposure, impaired mucociliary clearance, inhaled corticosteroids, and antibiotic-associated airway-ecology changes may contribute (jaggi2024fungallungdisease pages 8-9, jaggi2024fungallungdisease pages 4-5).
* **Other:** diabetes, prolonged ICU care, chemotherapy/radiotherapy, and systemic immunosuppression increase risk (harliza2024diagnosisandtreatment pages 1-2).

### Genetic susceptibility and protection

Aspergillosis itself is **not a single-gene inherited disorder**. Reported host susceptibility involves CFTR dysfunction and variants affecting epithelial recognition, Toll-like receptors, surfactant proteins, mannose-binding lectin, MHC, IL4R, and IL13/type-2 signaling. These are susceptibility or modifier associations, not sufficient causes of disease (jaggi2024fungallungdisease pages 5-7, jaggi2024fungallungdisease pages 17-18).

Rare primary immunodeficiencies—especially chronic granulomatous disease and defects of antifungal innate immunity—can confer large risks, but penetrance is exposure- and treatment-dependent. No clinically validated universal “protective variant,” carrier frequency, anticipation, founder effect, or germline-mosaicism framework exists for aspergillosis. Population allele frequencies and ACMG classifications should therefore be attached to the underlying immunodeficiency, not to aspergillosis as though it were Mendelian.

### Protective factors

Effective mucociliary clearance, intact alveolar macrophages and neutrophils, avoidance of unnecessary immunosuppression, control of structural lung disease, HEPA-filtered protective environments during profound neutropenia, and indicated mold-active prophylaxis reduce risk. Evidence does not support a specific protective diet or routine population supplement. Vitamin D has been investigated in ABPA, but it is not an established preventive intervention.

### Gene–environment interaction

The clearest interaction is **ubiquitous inhalational exposure × host defense phenotype**. CFTR/mucus-clearance defects increase airway residence time; innate-recognition variants alter fungal sensing; corticosteroids suppress phagocyte and lymphocyte function; and cavities furnish an ecological niche. Agricultural azole fungicides select resistant environmental *A. fumigatus*, allowing azole-naïve people to inhale resistant conidia—an important One Health interaction.

## 3. Phenotypes

| Phenotype | Type, course, and approximate frequency | Suggested HPO term |
|---|---|---|
| Cough, sputum | Symptom; chronic in CPA/bronchitis, episodic in ABPA, acute in IPA | Cough (HP:0012735); productive cough |
| Dyspnea/wheeze | Symptom; fluctuating in ABPA/asthma, progressive in CPA/IPA | Dyspnea (HP:0002094); wheezing |
| Fever | Symptom; common but nonspecific in IPA, especially neutropenic disease | Fever (HP:0001945) |
| Hemoptysis | Symptom; about 50% in CPA and may be life-threatening | Hemoptysis (HP:0002105) |
| Fatigue/weight loss | Symptoms; common in chronic or disseminated disease | Fatigue (HP:0012378); weight loss (HP:0001824) |
| Bronchiectasis | Structural sign; central/proximal pattern supports ABPA; chronic | Bronchiectasis (HP:0002110) |
| Pulmonary cavity/fungal ball | Imaging sign; hallmark of CPA/aspergilloma | Pulmonary cavity; abnormal lung morphology |
| Halo sign, wedge-shaped consolidation, air-crescent sign | CT signs of IPA/angioinvasion; evolve over days to weeks | Abnormal pulmonary imaging finding |
| Eosinophilia | Laboratory abnormality in ABPA; threshold commonly ≥500 cells/µL | Eosinophilia (HP:0001880) |
| Elevated total and fungus-specific IgE | Laboratory abnormality in ABPA | Increased circulating IgE (HP:0003212) |
| Cerebral, sinus, ocular, cutaneous, bone, or cardiac invasion | Extrapulmonary signs, usually severe | Map to organ-specific infection/lesion terms |

ABPA severity is variable and relapsing; untreated recurrent mucus impaction can lead to bronchiectasis and chronic pleuropulmonary fibrosis. CPA progresses over months or years. IPA can progress over days and may be muted in neutropenia. Quality-of-life effects include breathlessness, fatigue, reduced exercise capacity, recurrent hospitalization, treatment toxicity, anxiety related to hemoptysis, and impaired work/daily function. Robust phenotype-specific EQ-5D or SF-36 frequencies were not available in the retrieved evidence.

## 4. Genetic and molecular information

### Human genetics

There is no universal causal human gene, chromosome abnormality, somatic driver, or diagnostic pathogenic-variant panel for aspergillosis. Genetic testing is appropriate when unusually early, recurrent, refractory, or disseminated disease suggests an underlying immunodeficiency. Candidate testing can include genes responsible for chronic granulomatous disease and other phagocyte, CARD9/lectin-pathway, or combined-immunodeficiency disorders; interpretation must be tied to that syndrome.

OpenTargets identifies **NR3C1**, the glucocorticoid receptor, as a treatment-associated target for aspergillosis/ABPA. This reflects corticosteroid pharmacology rather than proof that NR3C1 mutations cause aspergillosis (OpenTargets Search: aspergillosis).

### Pathogen genetics and resistance

Azoles inhibit fungal lanosterol 14α-demethylase, encoded principally by **cyp51A**. Promoter tandem repeats and coding substitutions can cause resistance; environmental and patient-selected routes both occur. Susceptibility testing is clinically important because resistant invasive disease carries poorer outcomes. These are **fungal**, not human, variants and are not classified under human ACMG/AMP criteria.

### Functional genomics and epigenetic regulation

* In combined A549 human epithelial-cell and RAW264.7 murine-macrophage transcriptomics, 140 fungal genes were commonly upregulated; 13 remained concordant with an in-vivo dataset. Disrupting fungal **maiA**, part of phenylalanine degradation, increased pyomelanin, reduced cell-wall β-glucan, dampened macrophage inflammation, and reduced virulence in neutropenic mice (published January 2024; DOI: https://doi.org/10.3389/fcimb.2024.1327299) (guruceaga2024theaspergillusfumigatus pages 1-2).
* The fungal deacetylase **SirE** regulates histone/non-histone acetylation, cell-wall integrity, thermotolerance, secondary metabolism, and virulence. Deletion attenuated disease in murine and *Galleria mellonella* models, making fungal epigenetic enzymes experimental drug targets.
* **CotA–SsdA** couples host-relevant carbon-source sensing to hyphal morphogenesis and invasive growth, illustrating pathogen metabolic plasticity.
* These are experimental pathogen targets; none currently constitutes a validated human diagnostic or approved therapeutic biomarker.

## 5. Environmental and infectious-agent information

*Aspergillus* is ubiquitous in soil, compost, decaying vegetation, dust, stored grain, construction aerosols, and indoor/outdoor air. Exposure is principally airborne and environmental; routine person-to-person transmission is not characteristic. Construction, gardening/compost handling, agriculture, grain/poultry work, and heavily contaminated buildings can raise inoculum.

Smoking is not a direct infectious cause but promotes COPD, emphysema, cavitation, and impaired airway clearance. Broad antibiotics and corticosteroids alter airway ecology or host immunity. Agricultural/horticultural triazole fungicides are a major environmental selection pressure for medical azole resistance. Environmental control should therefore combine occupational protection, hospital engineering, antifungal stewardship, and agricultural One Health surveillance.

**Agent taxonomy:** genus *Aspergillus*; major pathogen *A. fumigatus* (NCBI Taxonomy ID 746128 for the commonly referenced species entry; verify strain-level IDs), followed by *A. flavus*, *A. terreus*, and *A. niger* complex.

## 6. Mechanism and pathophysiology

### Causal chains

1. **Invasive disease:** inhaled conidium → deposition in terminal airway/alveolus → failed macrophage killing → germination → neutrophil failure permits hyphal extension → epithelial/endothelial penetration → angioinvasion → thrombosis, ischemic infarction, necrosis, hemorrhage → pulmonary failure or hematogenous dissemination (heylen2024acuteinvasivepulmonary pages 1-2).
2. **CPA:** damaged lung/cavity → persistent fungal growth and biofilm/fungal ball → chronic local inflammation and progressive cavitation/fibrosis → vessel erosion and hemoptysis. Deep angioinvasion is generally absent from classic CPA (tashiro2024chronicpulmonaryaspergillosis pages 1-2).
3. **ABPA:** impaired clearance and persistent airway antigen → epithelial/innate sensing → Th2/IL-4/IL-5/IL-13 signaling → fungus-specific IgE, mast-cell activation, eosinophilia and mucus hypersecretion → mucus plugs, exacerbations and bronchiectasis (jaggi2024fungallungdisease pages 5-7).

### Cells, pathways, and ontology suggestions

* **Alveolar macrophage** (CL:0000583): conidial uptake; GO suggestions—phagocytosis (GO:0006909), innate immune response (GO:0045087).
* **Neutrophil** (CL:0000775): hyphal damage, oxidative burst and extracellular traps; GO—respiratory burst (GO:0045730), neutrophil activation (GO:0042119).
* **Airway/alveolar epithelial cells:** mucociliary clearance, barrier and cytokine signaling; GO—epithelial barrier establishment and response to fungus.
* **Eosinophil** (CL:0000771), mast cell (CL:0000097), type-2 helper T cell: ABPA inflammation; GO—type 2 immune response and cytokine production.
* **Endothelial cells:** targets of hyphal invasion; GO—blood coagulation, cell death, response to hypoxia.
* **NK cell** (CL:0000623): human CD56 binds fungal galactosaminogalactan (GAG), inducing activation, degranulation, chemokines and cytotoxic effectors; conditioned supernatants enhance polymorphonuclear antifungal activity (published June 2024; DOI: https://doi.org/10.1371/journal.ppat.1012315) (heilig2024cd56mediatedactivationof pages 1-2).

### Cellular, metabolic, and molecular profiling

Key processes include cell-wall remodeling, thermotolerance, iron acquisition, hypoxia adaptation, oxidative-stress resistance, secondary metabolites, nutritional plasticity, biofilm matrix production, autophagy/stress responses, and host immunometabolism. Current RNA-seq, dual-transcriptomic, proteomic, metabolomic, and CRISPR studies have identified candidate fungal vulnerabilities, but none has replaced culture, antigen detection, PCR, imaging, or histopathology in routine diagnosis. Single-cell and spatial methods are promising for resolving macrophage, neutrophil, epithelial, and lymphocyte heterogeneity, but remain research technologies.

## 7. Anatomical structures affected

**Primary:** respiratory tract—nasal/paranasal sinuses, tracheobronchial tree, bronchi, bronchioles, alveoli, lung parenchyma, pleura, and pre-existing cavities. Suggested UBERON concepts include lung (UBERON:0002048), bronchus (UBERON:0002185), alveolus of lung, trachea (UBERON:0003126), and paranasal sinus.

**Secondary/disseminated:** brain/CNS, eye/orbit, skin/subcutis, bone, heart/endocardium, kidney, liver, and gastrointestinal tract. Pulmonary lesions are usually multifocal rather than consistently lateralized; aspergilloma can be unilateral or bilateral according to cavity distribution.

**Tissue/cell:** respiratory epithelium, alveolar interstitium, vascular endothelium, macrophages, neutrophils, eosinophils, lymphocytes, and fibroblasts. **Subcellular fungal targets** include cell wall, plasma membrane/ergosterol pathway, nucleus/chromatin, mitochondria, and secretory machinery; proposed GO cellular-component terms include fungal-type cell wall and plasma membrane.

## 8. Temporal development

* **ABPA:** often begins in adolescents or adults with asthma and in children/adults with CF. It is episodic or relapsing; stages include acute disease, treatment response, remission, exacerbation, treatment-dependent disease, and advanced bronchiectatic/fibrotic disease.
* **CPA:** generally adult or older-adult onset, insidious and chronic. Diagnostic frameworks require compatible disease over months; progression ranges from stable simple aspergilloma to enlarging cavities and chronic fibrosis. Relapse after stopping azoles is common.
* **IPA:** acute or subacute, often developing during neutropenia, transplantation, high-dose steroid exposure, or severe viral critical illness. Early CT/biomarker detection is a critical intervention window; delay increases mortality.
* **Remission:** ABPA commonly achieves treatment-induced remission but can relapse. CPA may stabilize on prolonged therapy; localized aspergilloma may be cured surgically. IPA recovery requires rapid antifungal therapy plus immune recovery where feasible.

## 9. Epidemiology, inheritance, and population

Global estimates are uncertain because diagnostics and surveillance are uneven. A 2024 synthesis reported approximately **1.84 million annual CPA cases** in a 2020 model and about **340,000 first-year deaths**; earlier modeling estimated 372,000 cases. CPA mortality ranges were 7–32% at one year and 38–52% at five years (tashiro2024chronicpulmonaryaspergillosis pages 1-2). These are modeled estimates rather than complete case registries.

Disease burden varies with tuberculosis prevalence, COPD, asthma/CF, hematologic malignancy, transplantation, intensive-care populations, access to diagnostics, and azole resistance. Invasive-disease incidence is therefore best reported within a risk cohort rather than as one general-population rate. Age is not causal but a 2024 meta-analysis of 55 retrospective studies and 13,983 patients found patients with IA averaged about 2.5 years older than controls; residual confounding is likely.

No fixed male:female ratio exists. A 2024 CPA cohort of 106 patients had mean age 60.3 years and 69.8% were male, probably reflecting underlying smoking-related and structural lung disease rather than sex-linked inheritance. Aspergillosis has no Mendelian inheritance pattern, anticipation, carrier state, or routine reproductive genetic-screening indication.

## 10. Diagnostics

### Invasive aspergillosis

Diagnosis integrates **host factors + compatible imaging/clinical disease + mycological evidence**. Proven disease requires histopathologic demonstration of tissue invasion and/or recovery from a normally sterile site. Probable disease uses validated consensus combinations; these definitions were developed principally for research and should not delay treatment.

* **CT:** dense circumscribed nodule/lesion with or without halo; wedge-shaped consolidation; cavity; later air-crescent sign. Findings are host- and timing-dependent.
* **Microscopy/histopathology:** acute-angle branching, septate hyphae with tissue or vascular invasion; morphology is not completely species-specific.
* **Culture:** enables identification and susceptibility testing but lacks sensitivity and may represent colonization in respiratory specimens.
* **Galactomannan (GM):** EORTC/MSGERC-compatible thresholds include serum/plasma index ≥1.0 and BAL index ≥1.0 in appropriate hosts; interpretation varies with prophylaxis and population (heylen2024acuteinvasivepulmonary pages 6-7).
* **PCR:** repeated blood positivity or duplicate BAL positivity can satisfy mycological criteria. Standardization led to inclusion of blood and respiratory *Aspergillus* PCR in revised EORTC/MSGERC definitions.
* **β-D-glucan:** supports invasive fungal disease but is not *Aspergillus*-specific.
* **Pediatric cohort performance:** among 100 hematologic-malignancy patients, serum GM at 0.67 yielded sensitivity 82.3%, specificity 97.4%, PPV 98.1%, and NPV 77.1%; at 0.5, sensitivity was 87.1% and NPV 80.5%. These estimates are cohort-specific, not universal.

### CPA and aspergilloma

Diagnosis requires compatible chronic symptoms/radiology, exclusion of alternatives, and microbiological or immunological evidence. Chest CT plus serum *Aspergillus* IgG are central; sputum culture/PCR and histology increase specificity (tashiro2024chronicpulmonaryaspergillosis pages 1-2). Differential diagnoses include recurrent/active tuberculosis, nontuberculous mycobacterial disease, lung cancer, bacterial abscess, endemic mycoses, cavitating vasculitis, and other fungal balls.

### ABPA

The 2024 ISHAM guideline recommends diagnosis in a predisposing condition or compatible clinico-radiological presentation with mandatory fungal sensitization and **total IgE ≥500 IU/mL**, plus at least two of fungus-specific IgG, eosinophilia, or suggestive imaging. *A. fumigatus*-specific IgE ≥0.35 kUA/L and eosinophils ≥500/µL are commonly used thresholds (jaggi2024fungallungdisease pages 8-9, jaggi2024fungallungdisease pages 5-7, serpa2024allergicbronchopulmonaryaspergillosis pages 19-21). The guideline’s abstract states: “We do not routinely recommend treating asymptomatic ABPA patients” and recommends prednisolone or itraconazole monotherapy for acute ABPA.

### Genetic and omics testing

WES/WGS, immunodeficiency panels, single-gene testing, or functional neutrophil assays are indicated only when the phenotype suggests inherited immune dysfunction. CMA, karyotype, FISH, mitochondrial testing, and repeat-expansion testing have no routine role. mNGS may detect fungi missed by culture but requires contamination-aware interpretation; it remains adjunctive rather than a stand-alone criterion (jaggi2024fungallungdisease pages 1-3).

No population screening program exists. Targeted surveillance—serial GM/PCR and prompt CT—is used in selected high-risk hematology/transplant settings.

## 11. Outcome and prognosis

IPA remains highly lethal; a 2024 diagnostic review reported mortality up to 70%, while early diagnosis may reduce mortality by as much as 30%. Rates depend strongly on host, certainty category, species/resistance, dissemination, and immune recovery. One multicenter AML population cited approximately 30% mortality (heylen2024acuteinvasivepulmonary pages 1-2).

CPA has approximately 38–52% five-year mortality. Poor prognostic factors include advanced age/frailty, low BMI or albumin, extensive bilateral/cavitary disease, COPD/emphysema, lung cancer, nontuberculous mycobacterial coinfection, azole resistance, and inability to tolerate therapy. In a 106-patient cohort, emphysema had adjusted HR 4.107 and lung cancer HR 8.511 for mortality; three-year survival with versus without emphysema was 64.9% versus 85.9%.

ABPA is seldom directly fatal but causes repeated exacerbations, mucus plugging, bronchiectasis, loss of lung function, steroid toxicity, and occasionally chronic fibrosis. Prognosis improves with early recognition, control of type-2 inflammation, reduced fungal burden, and prevention of recurrent exacerbations.

## 12. Treatment and current applications

### IPA

* **First line:** systemic mold-active triazole, commonly voriconazole or isavuconazole; selection depends on susceptibility, hepatic function, QT effects, interactions, CNS involvement, and prior prophylaxis (heylen2024acuteinvasivepulmonary pages 1-2).
* **Alternatives/salvage:** liposomal amphotericin B; posaconazole or another active triazole; echinocandin-containing combinations in selected refractory or resistant cases. Echinocandin monotherapy is generally not preferred initially.
* **Support:** reduce immunosuppression where feasible, recover neutrophils, manage drug interactions, perform therapeutic drug monitoring (especially voriconazole/itraconazole/posaconazole), and surgically control selected focal lesions or hemorrhage.
* **Duration:** individualized, usually at least 6–12 weeks and longer until clinical/radiographic improvement and reversal of immunosuppression.

Suggested NCIT concepts: Voriconazole, Isavuconazole, Liposomal Amphotericin B, Posaconazole, Antifungal Therapy, Therapeutic Drug Monitoring, Surgical Resection.

### CPA/aspergilloma

Itraconazole or voriconazole with drug monitoring is first-line; posaconazole or isavuconazole are alternatives. At least 6 months is recommended, while 12 months or longer produces better control and fewer relapses (tashiro2024chronicpulmonaryaspergillosis pages 1-2, jaggi2024fungallungdisease pages 8-9). Reported response ranges are itraconazole 43–76%, voriconazole 32–80%, posaconazole 44–61%, isavuconazole 82.7%, echinocandins 42–77%, and liposomal amphotericin B 52–73%; cross-study comparisons are confounded by differing populations and endpoints (tashiro2024chronicpulmonaryaspergillosis pages 1-2).

Localized simple aspergilloma may be cured by resection: postoperative mortality is 0–5%, although complications range from 11–63%. Bronchial-artery embolization controls major hemoptysis in 64–100%, but approximately 50% recur (tashiro2024chronicpulmonaryaspergillosis pages 1-2).

### ABPA

The 2024 ISHAM experts recommend oral prednisolone **or** itraconazole monotherapy for newly diagnosed acute disease or an exacerbation, generally over about four months; combination prednisolone plus itraconazole is reserved for recurrent exacerbations. Asymptomatic disease is not routinely treated (jaggi2024fungallungdisease pages 5-7). Omalizumab, mepolizumab/benralizumab, and dupilumab are steroid-sparing options in treatment-dependent or severe type-2 disease, but evidence remains less mature than for steroids/azoles. Airway clearance, asthma/CF therapy, bronchodilators, and treatment of bacterial coinfection are important.

### Pharmacology and adverse effects

* **Azoles:** inhibit ergosterol biosynthesis; risks include hepatotoxicity, interactions through CYP enzymes, variable exposure, neuropathy/phototoxicity with prolonged voriconazole, and QT effects. Isavuconazole shortens rather than prolongs QT.
* **Polyenes:** bind ergosterol; nephrotoxicity and electrolyte loss remain important, reduced with liposomal formulation.
* **Echinocandins:** inhibit β-1,3-glucan synthesis; generally intravenous and relatively well tolerated.
* **Glucocorticoids:** suppress ABPA inflammation but increase infection, diabetes, osteoporosis, adrenal suppression, and IPA risk. Up to 30% of CPA patients experience azole adverse effects (jaggi2024fungallungdisease pages 8-9).

No universally accepted host pharmacogenomic dosing algorithm replaces therapeutic drug monitoring. CYP2C19 genotype affects voriconazole exposure, but implementation is institution- and guideline-dependent.

### Trials and emerging treatment

* **NCT05653193:** adjunctive interferon-γ for CPA; randomized phase II feasibility study, 50 participants, active but not recruiting at retrieval.
* **NCT00531479:** voriconazole plus anidulafungin versus voriconazole; phase III, 459 participants, completed.
* **NCT00263315:** weekly inhaled liposomal amphotericin B prophylaxis in neutropenic hematology patients; randomized phase II/III, 320 participants, completed. The trial targeted reduction in IPA from about 7% to 1% and used twice-weekly serum GM plus CT for persistent fever (NCT00263315 chunk 1).
* New agents in development include olorofim, fosmanogepix, ibrexafungerp, and inhaled triazoles such as opelconazole/PC945. Their roles in resistant, refractory, or localized pulmonary disease remain investigational.

## 13. Prevention

**Primary:** no licensed human vaccine exists. Minimize unnecessary corticosteroids and antibiotics; optimize asthma/CF/COPD and cavity-producing diseases; use respirators or avoid compost, construction dust, soil, and renovation aerosols during profound immunosuppression. Hospitals should use HEPA filtration, positive-pressure protective rooms, dust barriers, and construction-risk controls for high-risk units.

**Secondary:** stratify AML/HCT and other high-risk patients; use mold-active prophylaxis according to specialty guidelines and local resistance; monitor with symptom assessment, biomarkers, and early CT where appropriate. The preventive-amphotericin trial illustrates targeted rather than population prophylaxis (NCT00263315 chunk 1).

**Tertiary:** therapeutic drug monitoring, susceptibility testing, adherence support, serial CT/IgG or IgE monitoring as syndrome-appropriate, embolization for bleeding, surgery for selected localized lesions, and pulmonary rehabilitation prevent progression and complications.

Public-health priorities are improved mycology laboratories, resistance surveillance, antifungal stewardship, regulation/stewardship of agricultural azoles, and One Health linkage of environmental, veterinary, and clinical isolates. Genetic counseling is relevant only for an identified underlying inherited immunodeficiency, not for routine aspergillosis.

## 14. Other species and natural disease

Natural aspergillosis occurs widely in birds and mammals. Birds—poultry, raptors, waterfowl, penguins, parrots, and other captive/wild species—are especially susceptible to respiratory disease involving air sacs and lungs. Young birds are often at higher risk. Mammalian manifestations include sinonasal/orbital disease in dogs and cats, guttural-pouch mycosis and keratitis in horses, and pneumonia, mastitis, or rhinitis in sheep and goats.

A 2023 household study in Kazakhstan found median incidence risk/fatality of 39%/26% in chickens, 42%/22% in turkeys, and 37%/33% in geese; egg production fell a median 58.3%. These data demonstrate substantial veterinary and economic impact but should not be generalized globally.

Human aspergillosis is ordinarily acquired from the shared environment rather than directly from diseased animals. Thus, conventional zoonotic transmission is not a dominant mechanism. Birds may nevertheless disperse environmental and azole-resistant strains, making avian disease a potential sentinel in One Health surveillance.

Suggested taxonomy includes domestic chicken *Gallus gallus* (NCBI Taxon 9031), turkey *Meleagris gallopavo* (9103), goose *Anser anser* (8843), dog *Canis lupus familiaris* (9615), cat *Felis catus* (9685), and horse *Equus caballus* (9796). Breed-specific VBO susceptibility is insufficiently established.

## 15. Model organisms and experimental systems

* **Mouse IPA models:** immunosuppression is induced with cyclophosphamide/neutropenia, corticosteroids, or targeted genetic defects, followed by intranasal/intratracheal conidia. They reproduce germination, lung invasion, inflammation, angioinvasion, fungal burden, and mortality. Limitations include artificial immune suppression, inoculum, route, murine pharmacokinetics, and immune differences.
* **Chronic/allergic mouse models:** repeated airway challenge can reproduce eosinophilia, IgE, mucus and airway remodeling, but not the full decades-long human history or structural lung disease.
* ***Galleria mellonella*:** inexpensive, high-throughput innate-immunity model used for fungal virulence and drug screening; lacks adaptive immunity and mammalian lung anatomy.
* **Zebrafish/larval systems:** permit live imaging of phagocyte–fungus interactions, but temperature and organ differences constrain translation.
* **Cell systems:** A549 epithelial cells, primary airway/alveolar cells, RAW264.7 or primary macrophages, neutrophils, NK cells, air–liquid-interface cultures, organoids, and lung-on-chip models isolate cell-specific mechanisms. They omit systemic immunity and full tissue architecture.
* **Fungal CRISPR/knockout models:** deletion of **maiA**, **sirE**, or components of the **CotA–SsdA** axis links genotype to cell-wall/metabolic adaptation and virulence. The maiA evidence combines in-vitro transcriptomics with a neutropenic mouse model, providing stronger causal support than expression alone (guruceaga2024theaspergillusfumigatus pages 1-2).

### Evidence-quality interpretation

Human guidelines and clinical cohorts most directly support diagnostic and treatment recommendations. Mouse, insect, and cell studies establish biological plausibility and target function but do not establish clinical efficacy. Computational/global burden estimates are essential where surveillance is absent but carry substantial uncertainty. The authoritative 2024 position is therefore that rapid syndrome-specific diagnosis, local resistance knowledge, antifungal exposure optimization, and correction of the host defect remain more clinically actionable than any single emerging omics marker (jaggi2024fungallungdisease pages 3-4, heylen2024acuteinvasivepulmonary pages 1-2, jaggi2024fungallungdisease pages 8-9).

References

1. (jaggi2024fungallungdisease pages 3-4): Tavleen Kaur Jaggi, Ritesh Agarwal, Pei Yee Tiew, Anand Shah, Emily C. Lydon, Chadi A. Hage, Grant W. Waterer, Charles R. Langelier, Laurence Delhaes, and Sanjay H. Chotirmall. Fungal lung disease. The European Respiratory Journal, 64:2400803, Oct 2024. URL: https://doi.org/10.1183/13993003.00803-2024, doi:10.1183/13993003.00803-2024. This article has 56 citations.

2. (jaggi2024fungallungdisease pages 1-3): Tavleen Kaur Jaggi, Ritesh Agarwal, Pei Yee Tiew, Anand Shah, Emily C. Lydon, Chadi A. Hage, Grant W. Waterer, Charles R. Langelier, Laurence Delhaes, and Sanjay H. Chotirmall. Fungal lung disease. The European Respiratory Journal, 64:2400803, Oct 2024. URL: https://doi.org/10.1183/13993003.00803-2024, doi:10.1183/13993003.00803-2024. This article has 56 citations.

3. (jaggi2024fungallungdisease pages 8-9): Tavleen Kaur Jaggi, Ritesh Agarwal, Pei Yee Tiew, Anand Shah, Emily C. Lydon, Chadi A. Hage, Grant W. Waterer, Charles R. Langelier, Laurence Delhaes, and Sanjay H. Chotirmall. Fungal lung disease. The European Respiratory Journal, 64:2400803, Oct 2024. URL: https://doi.org/10.1183/13993003.00803-2024, doi:10.1183/13993003.00803-2024. This article has 56 citations.

4. (tashiro2024chronicpulmonaryaspergillosis pages 1-2): Masato Tashiro, Takahiro Takazono, and Koichi Izumikawa. Chronic pulmonary aspergillosis: comprehensive insights into epidemiology, treatment, and unresolved challenges. Therapeutic Advances in Infectious Disease, Jan 2024. URL: https://doi.org/10.1177/20499361241253751, doi:10.1177/20499361241253751. This article has 59 citations.

5. (heylen2024acuteinvasivepulmonary pages 1-2): Jannes Heylen, Yuri Vanbiervliet, Johan Maertens, Bart Rijnders, and Joost Wauters. Acute invasive pulmonary aspergillosis: clinical presentation and treatment. Seminars in Respiratory and Critical Care Medicine, 45:069-087, Jan 2024. URL: https://doi.org/10.1055/s-0043-1777769, doi:10.1055/s-0043-1777769. This article has 49 citations and is from a peer-reviewed journal.

6. (jaggi2024fungallungdisease pages 4-5): Tavleen Kaur Jaggi, Ritesh Agarwal, Pei Yee Tiew, Anand Shah, Emily C. Lydon, Chadi A. Hage, Grant W. Waterer, Charles R. Langelier, Laurence Delhaes, and Sanjay H. Chotirmall. Fungal lung disease. The European Respiratory Journal, 64:2400803, Oct 2024. URL: https://doi.org/10.1183/13993003.00803-2024, doi:10.1183/13993003.00803-2024. This article has 56 citations.

7. (jaggi2024fungallungdisease pages 5-7): Tavleen Kaur Jaggi, Ritesh Agarwal, Pei Yee Tiew, Anand Shah, Emily C. Lydon, Chadi A. Hage, Grant W. Waterer, Charles R. Langelier, Laurence Delhaes, and Sanjay H. Chotirmall. Fungal lung disease. The European Respiratory Journal, 64:2400803, Oct 2024. URL: https://doi.org/10.1183/13993003.00803-2024, doi:10.1183/13993003.00803-2024. This article has 56 citations.

8. (heylen2024acuteinvasivepulmonary pages 6-7): Jannes Heylen, Yuri Vanbiervliet, Johan Maertens, Bart Rijnders, and Joost Wauters. Acute invasive pulmonary aspergillosis: clinical presentation and treatment. Seminars in Respiratory and Critical Care Medicine, 45:069-087, Jan 2024. URL: https://doi.org/10.1055/s-0043-1777769, doi:10.1055/s-0043-1777769. This article has 49 citations and is from a peer-reviewed journal.

9. (OpenTargets Search: aspergillosis): Open Targets Query (aspergillosis, 4 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

10. (harliza2024diagnosisandtreatment pages 1-2): Baiq Fanindya Harliza and Prima Belia Fathana. Diagnosis and treatment of aspergillosis. Jurnal Biologi Tropis, 24:386-392, Oct 2024. URL: https://doi.org/10.29303/jbt.v24i4.7682, doi:10.29303/jbt.v24i4.7682. This article has 4 citations.

11. (jaggi2024fungallungdisease pages 17-18): Tavleen Kaur Jaggi, Ritesh Agarwal, Pei Yee Tiew, Anand Shah, Emily C. Lydon, Chadi A. Hage, Grant W. Waterer, Charles R. Langelier, Laurence Delhaes, and Sanjay H. Chotirmall. Fungal lung disease. The European Respiratory Journal, 64:2400803, Oct 2024. URL: https://doi.org/10.1183/13993003.00803-2024, doi:10.1183/13993003.00803-2024. This article has 56 citations.

12. (guruceaga2024theaspergillusfumigatus pages 1-2): Xabier Guruceaga, Uxue Perez-Cuesta, Adela Martin-Vicente, Eduardo Pelegri-Martinez, Harrison I. Thorn, Saioa Cendon-Sanchez, Jinhong Xie, Ashley V. Nywening, Andoni Ramirez-Garcia, Jarrod R. Fortwendel, and Aitor Rementeria. The aspergillus fumigatus maia gene contributes to cell wall homeostasis and fungal virulence. Frontiers in Cellular and Infection Microbiology, Jan 2024. URL: https://doi.org/10.3389/fcimb.2024.1327299, doi:10.3389/fcimb.2024.1327299. This article has 7 citations.

13. (heilig2024cd56mediatedactivationof pages 1-2): Linda Heilig, Fariha Natasha, Nora Trinks, Vishukumar Aimanianda, Sarah Sze Wah Wong, Thierry Fontaine, Ulrich Terpitz, Lea Strobel, François Le Mauff, Donald C. Sheppard, Sascha Schäuble, Oliver Kurzai, Kerstin Hünniger, Esther Weiss, Mario Vargas, P. Lynne Howell, Gianni Panagiotou, Sebastian Wurster, Hermann Einsele, and Juergen Loeffler. Cd56-mediated activation of human natural killer cells is triggered by aspergillus fumigatus galactosaminogalactan. Jun 2024. URL: https://doi.org/10.1371/journal.ppat.1012315, doi:10.1371/journal.ppat.1012315. This article has 17 citations and is from a highest quality peer-reviewed journal.

14. (serpa2024allergicbronchopulmonaryaspergillosis pages 19-21): Faradiba Sarquis Serpa, Gustavo Falbo Wandalsen, Solange Oliveira Rodrigues Valle, Adelmir Souza Machado, Alfeu Tavares França, Álvaro Augusto Cruz, Antonio Carlos Pastorino, José Angelo Rizzo, José Elabras-Filho, Luane Marques de-Mello, Patricia Polles de Oliveira Jorge, Pedro Giavina-Bianchi, Ekaterini Simões Goudoris, and Fabio Chigres Kuschnir. Allergic bronchopulmonary aspergillosis: brazilian association of allergy and immunology guidelines for diagnosis and management. Jan 2024. URL: https://doi.org/10.5935/2526-5393.20240033-en, doi:10.5935/2526-5393.20240033-en. This article has 0 citations.

15. (NCT00263315 chunk 1):  Inhalation of Liposomal Amphotericin B to Prevent Invasive Aspergillosis. Erasmus Medical Center. 2000. ClinicalTrials.gov Identifier: NCT00263315

## Artifacts

- [Edison artifact artifact-00](Aspergillosis-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 24 |
| Resolved | 24 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 11 |
| Terms named correctly | 8 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 3 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `HP:0001880` (1 mention) - the report calls it "Eosinophilia"; HP calls it **Increased total eosinophil count**, and lists "Eosinophilia" among its other names
- `HP:0003212` (1 mention) - the report calls it "Increased circulating IgE"; HP calls it **Increased circulating IgE concentration**, and lists "Increased circulating IgE level" among its other names
- `CL:0000623` (1 mention) - the report calls it "NK cell"; CL calls it **natural killer cell**, and lists "NK cell" among its other names

Every term resolved, and every label the report gave matched.