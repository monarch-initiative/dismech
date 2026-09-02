---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-27T11:37:45.770331'
end_time: '2026-08-27T11:46:56.406696'
duration_seconds: 550.64
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Restrictive Cardiomyopathy
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 25
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 1
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Restrictive_Cardiomyopathy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Restrictive Cardiomyopathy
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Restrictive Cardiomyopathy** covering all of the
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
- **Disease Name:** Restrictive Cardiomyopathy
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Restrictive Cardiomyopathy** covering all of the
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


# Restrictive Cardiomyopathy: Disease-Characteristics Research Report

**Scope.** This report treats *restrictive cardiomyopathy* (RCM) as a **phenotype**, while emphasizing **primary/familial genetic RCM**. Amyloidosis, storage disease, iron overload, eosinophilic disease, radiation injury, and other acquired disorders can produce the same physiology but are etiologically distinct. Evidence is labeled as human, database, animal, in-vitro, or trial-registry evidence. Literature was prioritized through 2024; robust RCM-specific data remain limited because the disease is rare.

## Executive summary

RCM is myocardial stiffness and impaired ventricular relaxation causing high filling pressures, usually with nondilated, nonhypertrophied ventricles, preserved ejection fraction early, and marked biatrial enlargement. Pediatric RCM represents approximately **2.5–5% of childhood cardiomyopathy**, about **30%** of pediatric patients have a positive family history, and nearly half reportedly die or undergo transplantation within three years. Familial primary RCM is usually autosomal dominant and is most convincingly associated with **TNNI3, TNNT2, FLNC, MYH7, and MYPN**, although phenotype overlap and variable expressivity are substantial. A 2023 patient-specific FLNC iPSC/engineered-tissue study and a 2024 pediatric FLNC study are the most notable recent mechanistic advances. There is no approved molecular therapy for primary genetic RCM; management remains careful congestion control, arrhythmia/thromboembolism management, cause-specific therapy for phenocopies, and early transplant evaluation for progressive disease. (kim2021geneticsofcardiomyopathy pages 22-23, schubert2018theuseof pages 17-21, dong2024novelflncvariants pages 1-2, wang2023engineeredcardiactissue pages 1-3)

| domain | key finding/statistic | evidence type (human clinical/database/in vitro/mouse/trial registry) | key gene/variant or intervention | source year/DOI or NCT |
|---|---|---|---|---|
| Disease identifier | Restrictive cardiomyopathy mapped to MONDO_0005201; pediatric mutation-analysis registry also indexed MeSH term D002313 | database | MONDO_0005201 / MeSH D002313 | Open Targets disease mapping; ClinicalTrials.gov-derived browse term (OpenTargets Search: restrictive cardiomyopathy, NCT02432092 chunk 1) |
| Definition/phenotype | RCM is defined by increased myocardial stiffness, impaired diastolic relaxation, elevated filling pressures, preserved or near-preserved systolic function early, and biatrial enlargement | human clinical / in vitro disease-model paper | Phenotypic definition | 2023; DOI: 10.1016/j.xcrm.2023.100976 (wang2023engineeredcardiactissue pages 1-3) |
| Pediatric frequency | In children, RCM accounts for approximately 2.5–5% of all cardiomyopathies | human clinical review | Pediatric RCM | 2018 review summarizing pediatric literature (schubert2018theuseof pages 17-21) |
| Pediatric prognosis | Nearly half of pediatric patients die or require heart transplantation within 3 years of diagnosis | human clinical review | Pediatric RCM natural history | 2018 review summarizing pediatric literature (schubert2018theuseof pages 17-21) |
| Adult/combined outcome burden | In an RCM cohort with TNNI3-linked disease spectrum, composite outcome of mortality, cardiac transplantation, or ICD discharge was 56% | human clinical | TNNI3 / MYH7-associated RCM | 2021; DOI: 10.4070/kcj.2021.0154 (kim2021geneticsofcardiomyopathy pages 4-5) |
| Core genes | Highest-confidence recurrent genes include TNNI3, TNNT2, FLNC, MYPN; additional evidence for TTN and CRYAB; disease databases also capture secondary/metabolic phenocopy genes such as GAA, GBA1, TTR | database / human genetic literature | TNNI3, TNNT2, FLNC, MYPN, TTN, CRYAB, GAA, GBA1, TTR | Open Targets association evidence and cardiomyopathy genetics reviews (OpenTargets Search: restrictive cardiomyopathy, kim2021geneticsofcardiomyopathy pages 22-23) |
| Inheritance | Familial primary RCM is usually autosomal dominant; de novo sarcomeric variants are associated with severe pediatric disease and premature death/transplant | human clinical/genetic review | Sarcomeric and cytoskeletal variants | 2021; DOI: 10.4070/kcj.2021.0154 (kim2021geneticsofcardiomyopathy pages 22-23) |
| 2024 variant report | In 58 pediatric cardiovascular cases, novel heterozygous FLNC variants c.3962A>T (p.Glu1321Val) and c.7543C>T (p.Leu2515Phe) were identified; mixed restrictive/hypertrophic phenotype seen with p.Leu2515Phe | human clinical/genetic | FLNC c.3962A>T; FLNC c.7543C>T | 2024; DOI: 10.1186/s40246-024-00683-9 (dong2024novelflncvariants pages 1-2, dong2024novelflncvariants pages 4-6) |
| 2024 functional interpretation | FLNC c.3962A>T disrupted canonical splicing in a minigene assay, producing c.3961_3964del / p.Glu1321Alafs*23; both reported variants were de novo, absent from gnomAD, and classified likely pathogenic | human genetic / in vitro | FLNC c.3962A>T splicing defect | 2024; DOI: 10.1186/s40246-024-00683-9 (dong2024novelflncvariants pages 1-2, dong2024novelflncvariants pages 4-6) |
| 2023 disease model | A de novo FLNC in-frame deletion c.7416_7418delGAA (p.Glu2472_Asn2473delinsAsp) in a child with RCM was modeled in patient-specific iPSC-cardiomyocytes and 3D engineered cardiac tissue; mutant tissues showed increased passive tension and impaired relaxation velocity | in vitro | FLNC c.7416_7418delGAA | 2023; DOI: 10.1016/j.xcrm.2023.100976 (wang2023engineeredcardiactissue pages 3-4, wang2023engineeredcardiactissue pages 1-3) |
| 2023 therapeutic screen | High-throughput screening of 2,185 compounds identified PDE3 inhibition (trequinsin) as a lead; trequinsin reduced calcium-relaxation tau by ~50% and improved passive tension/relaxation without detected arrhythmic signal at tested conditions | in vitro | Trequinsin / PDE3 inhibition | 2023; DOI: 10.1016/j.xcrm.2023.100976 (wang2023engineeredcardiactissue pages 4-7, wang2023engineeredcardiactissue pages 3-4) |
| Troponin mechanism | Troponin I C-terminal RCM mutations cause impaired relaxation via marked myofibril Ca2+ hypersensitivity; severe variants include K178E and R192H | mouse / in vitro / human genetic literature | TNNI3 mutations (e.g., R145W, K178E, R192H) | 2016; DOI: 10.3389/fphys.2016.00629 (liu2016restrictivecardiomyopathycaused pages 2-3, liu2016restrictivecardiomyopathycaused pages 1-2) |
| Mouse rescue evidence | In transgenic mouse models, crossing cTnI193His RCM mice with cTnI-ND mice induced calcium desensitization and rescued diastolic dysfunction/RCM phenotype | mouse | TNNI3 (cTnI193His) rescue via cTnI-ND | 2016; DOI: 10.3389/fphys.2016.00629 (liu2016restrictivecardiomyopathycaused pages 2-3) |
| Trial/registry | PCM GENES enrolled 544 participants to study genotype-phenotype associations in pediatric dilated, hypertrophic, and restrictive cardiomyopathy with exome-based tiered testing | trial registry | Observational genomics cohort | NCT01873963 (NCT01873963 chunk 1) |
| Trial/registry | Pediatric Cardiomyopathy Mutation Analysis is a recruiting family-based observational cohort estimating 300 participants, including restrictive cardiomyopathy | trial registry | Molecular genetics / family study | NCT02432092 (NCT02432092 chunk 1) |
| Trial/registry | EARLY-MYO-RARE is a multimodal imaging-guided interventional rare-cardiomyopathy cohort (estimated n=300) including restrictive cardiomyopathy, using biomarker/imaging risk stratification and optimized HF care | trial registry | Multimodal imaging, HF pharmacotherapy, rehabilitation guidance | NCT06794710 (NCT06794710 chunk 1) |


*Table: This table summarizes the most decision-relevant evidence for restrictive cardiomyopathy across identifiers, epidemiology, genetics, mechanisms, models, and active clinical studies. It prioritizes human clinical and 2023-2024 translational findings while separating preclinical and registry evidence.*

## 1. Disease information

### Definition and classification

RCM is defined physiologically by **increased myocardial stiffness and impaired diastolic relaxation leading to elevated ventricular filling pressures**. The classic phenotype comprises normal or reduced ventricular volumes, normal or near-normal wall thickness, severe diastolic dysfunction, biatrial enlargement, and initially preserved systolic ejection fraction. Doppler commonly shows rapid early filling and a high E/A ratio. A frequently used genetic-RCM “gray-zone” definition is maximum LV wall thickness **≤13 mm** plus severe diastolic dysfunction. (kim2021geneticsofcardiomyopathy pages 22-23, kim2021geneticsofcardiomyopathy pages 4-5, wang2023engineeredcardiactissue pages 1-3)

Exact abstract-level wording from Wang *et al.* (published **21 March 2023**) is: **“Restrictive cardiomyopathy (RCM) is defined as increased myocardial stiffness and impaired diastolic relaxation leading to elevated ventricular filling pressures.”** DOI: [10.1016/j.xcrm.2023.100976](https://doi.org/10.1016/j.xcrm.2023.100976). (wang2023engineeredcardiactissue pages 1-3)

### Identifiers and synonyms

- **MONDO:** **MONDO:0005201**, restrictive cardiomyopathy. Familial RCM is separately represented as **MONDO:0016340**; TNNI3-associated familial RCM1 as **MONDO:0007270**; TNNT2-associated familial RCM3 as **MONDO:0012900**. (OpenTargets Search: restrictive cardiomyopathy)
- **MeSH:** **D002313**, Cardiomyopathy, Restrictive. (NCT02432092 chunk 1)
- **ICD-10-CM:** **I42.5**, Other restrictive cardiomyopathy. ICD coding does not reliably separate primary genetic RCM from amyloid, endomyocardial, or other restrictive phenocopies.
- Common names: *restrictive cardiomyopathy*, *primary restrictive cardiomyopathy*, *idiopathic restrictive cardiomyopathy*, *familial restrictive cardiomyopathy*, and *familial isolated restrictive cardiomyopathy*.
- OMIM uses gene-specific familial RCM entities rather than one etiologically uniform disorder; current OMIM cross-references should be checked during database ingestion because phenotype-series mappings change.

The information summarized here is **aggregated disease-level evidence** from publications, curated associations, and trial registries. Individual case data are used only where explicitly described; no EHR-derived patient-level dataset was accessed.

## 2. Etiology

### Causal factors

**Primary genetic RCM** most often arises from germline variants affecting sarcomere calcium regulation or cytoskeletal/Z-disc integrity. Established or repeatedly implicated genes include **TNNI3, TNNT2, FLNC, MYH7, MYPN**, and less consistently **ACTC1, MYBPC3, MYL2, MYL3, TTN, CRYAB, DES, and BAG3**. Curated Open Targets evidence particularly supports TNNI3 (PMID **12531876**), TNNT2 (PMID **16651346**), MYPN (PMIDs **22286171**, **25541130**), and FLNC (including PMIDs **26666891**, **27908349**, **29858533**, **31924696**, **33060286**). (OpenTargets Search: restrictive cardiomyopathy, kim2021geneticsofcardiomyopathy pages 22-23)

**Secondary genetic/systemic causes** include hereditary transthyretin amyloidosis (**TTR**), Fabry disease (**GLA**), Pompe disease (**GAA**), Gaucher disease (**GBA1**), and hereditary hemochromatosis (**HFE**). Acquired causes include AL amyloidosis, sarcoidosis, hypereosinophilic/Löffler endocardial disease, iron overload, radiation, drug toxicity, and endomyocardial fibrosis. These should be encoded as etiologic diseases causing an RCM phenotype, not collapsed into familial isolated RCM. (OpenTargets Search: restrictive cardiomyopathy, kim2021geneticsofcardiomyopathy pages 22-23, wang2023engineeredcardiactissue pages 1-3)

### Risk, protective factors, and gene–environment interaction

- **Strongest risk factors:** a pathogenic familial variant, an affected first-degree relative, or a de novo pathogenic variant. De novo sarcomeric variants are associated with severe childhood disease and premature death or transplantation. (kim2021geneticsofcardiomyopathy pages 22-23)
- **Environmental contributors:** radiation, iron overload, cardiotoxic drugs, eosinophilic inflammation, and systemic infiltrative disease can independently create restrictive physiology. Ordinary diet, smoking, obesity, and exercise are not established causes of monogenic primary RCM.
- A 2024 FLNC series noted infectious contexts in both pediatric cases and considered myocarditis a possible contributor; improvement after infection treatment in one child suggested a potentially reversible inflammatory component superimposed on persistent genetically mediated structural disease. This is hypothesis-generating, not proof of a reproducible FLNC–infection interaction. (dong2024novelflncvariants pages 4-6)
- **Protective variants or validated environmental protective factors:** none established. Calcium desensitization is protective in experimental TNNI3 models but is not a proven human preventive factor. (liu2016restrictivecardiomyopathycaused pages 2-3)
- **Modifiers:** variable RCM/HCM/near-normal expression within the same TNNI3 genotype strongly implies genetic or environmental modifiers, but no reproducible modifier gene is ready for clinical annotation. (kim2021geneticsofcardiomyopathy pages 4-5)

## 3. Phenotypes

| Phenotype | Typical characteristics | Suggested HPO term |
|---|---|---|
| Restrictive ventricular filling | Defining sign; chronic/progressive; may precede systolic failure | **HP:0011663**, Restrictive cardiomyopathy |
| Diastolic dysfunction | Severe; elevated end-diastolic pressures, impaired relaxation | **HP:0005117**, Elevated left ventricular end-diastolic pressure; verify current HPO label/version |
| Biatrial enlargement | Frequent/classic; consequence of chronically high filling pressure | **HP:0005120**, Abnormality of cardiac atrium; use specific left/right atrial enlargement children where available |
| Dyspnea/exercise intolerance | Common symptoms; progressive and quality-of-life limiting | **HP:0002094**, Dyspnea; **HP:0003546**, Exercise intolerance |
| Congestive heart failure | Advanced manifestation; right-, left-, or biventricular | **HP:0001635**, Congestive heart failure |
| Pulmonary hypertension | Secondary to high left-sided filling pressure; severity variable | **HP:0002092**, Pulmonary arterial hypertension |
| Hepatomegaly/peripheral edema/ascites | Systemic venous congestion | **HP:0002240**, Hepatomegaly; **HP:0012398**, Peripheral edema; **HP:0001541**, Ascites |
| Atrial/ventricular arrhythmia | Variable; can cause syncope, ICD therapy, or sudden death | **HP:0011675**, Arrhythmia; **HP:0001645**, Sudden cardiac death |
| Preserved EF early | Systolic function initially normal despite severe filling abnormality | Encode as clinical measurement rather than disease-defining HPO abnormality |
| Later systolic dysfunction | Progressive subset | **HP:0001723**, Restrictive cardiomyopathy may be paired with reduced EF measurement |

Onset ranges from infancy to late adulthood. Primary sarcomeric/FLNC disease often presents in childhood or early adulthood; TTR amyloidosis is generally later onset. Severity and progression are highly variable, but childhood-onset disease is frequently severe. A 2024 FLNC report documented preserved EF, dilated atria, pulmonary hypertension, valvular regurgitation, congestion/hepatomegaly, elevated BNP, and reduced activity tolerance in an affected child. (schubert2018theuseof pages 17-21, dong2024novelflncvariants pages 4-6)

RCM reduces exertional capacity and daily functioning through dyspnea, fatigue, edema, repeated hospitalization, arrhythmia surveillance, and transplant evaluation. No validated RCM-specific patient-reported outcome instrument or robust EQ-5D/SF-36 reference distribution was identified.

## 4. Genetic and molecular information

### Principal genes and variant mechanisms

- **TNNI3**—cardiac troponin I; classic RCM variants include **p.Leu144Gln, p.Arg145Trp, p.Ala171Thr, p.Lys178Glu, p.Asp190Gly, and p.Arg192His**. Most are heterozygous missense variants with dominant inheritance; increased myofilament Ca²⁺ sensitivity and impaired relaxation are central effects. PMID **12531876** is the landmark human association. (OpenTargets Search: restrictive cardiomyopathy, liu2016restrictivecardiomyopathycaused pages 2-3, kim2021geneticsofcardiomyopathy pages 4-5)
- **TNNT2**—cardiac troponin T; heterozygous sarcomeric variants can cause familial isolated RCM or overlapping HCM/RCM. PMID **16651346** supports association. (OpenTargets Search: restrictive cardiomyopathy)
- **FLNC**—filamin C, localized to Z-discs/intercalated discs and involved in actin cross-linking, structural integrity, and mechanotransduction. Missense/in-frame variants, especially in ROD2, occur in HCM/RCM; truncating variants more often cause dilated/arrhythmogenic disease through haploinsufficiency and are associated with fibrosis and arrhythmia. (dong2024novelflncvariants pages 1-2, wang2023engineeredcardiactissue pages 1-3)
- **MYH7/MYPN**—thick-filament/Z-disc genes with RCM and overlap phenotypes. MYH7 or TNNI3 pathogenic variants were found in approximately half of probands in one RCM series summarized in a 2021 review. (kim2021geneticsofcardiomyopathy pages 4-5)

### Recent variant-level findings

Dong *et al.* (**October 2024**) studied 58 pediatric cardiovascular patients and found two de novo heterozygous **FLNC** variants: **c.3962A>T (p.Glu1321Val)** and **c.7543C>T (p.Leu2515Phe)**; the latter occurred with mixed restrictive/hypertrophic cardiomyopathy. Both were absent from gnomAD and classified **likely pathogenic** using ACMG evidence PS2 + PM2-supporting + PP3. The c.3962A>T substitution disrupted canonical splicing in a minigene assay, producing **c.3961_3964del, p.Glu1321Alafs*23** and a predicted 1,342-aa truncated protein. DOI: [10.1186/s40246-024-00683-9](https://doi.org/10.1186/s40246-024-00683-9). (dong2024novelflncvariants pages 1-2, dong2024novelflncvariants pages 4-6)

Exact abstract quote: **“The c.3962A > T variant disrupted normal splicing, as demonstrated through the splicing prediction tool and minigene studies.”** (dong2024novelflncvariants pages 1-2)

Wang *et al.* identified de novo **FLNC c.7416_7418delGAA, p.Glu2472_Asn2473delinsAsp**, a pathogenic in-frame ROD2 deletion in a three-year-old with RCM. Patient iPSC cardiomyocytes and CRISPR-corrected controls established functional pathogenicity. (wang2023engineeredcardiactissue pages 3-4, wang2023engineeredcardiactissue pages 1-3)

Primary RCM variants are generally **germline**. Somatic variants are not an established causal class. Large chromosomal abnormalities, recurrent copy-number changes, repeat expansions, and disease-specific epigenetic signatures have not been established. Pathogenic alleles are expected to be absent or extremely rare in population databases; variant-specific gnomAD frequency and ClinVar status must be recorded rather than assigning one disease-wide frequency.

## 5. Environmental information

No infectious organism is a recognized direct cause of familial RCM. Infection or myocarditis may unmask genetically susceptible myocardium, but evidence is preliminary. Relevant acquired exposures include mediastinal radiation, cardiotoxic drugs, heavy metals/iron overload, and inflammatory or eosinophilic injury. Lifestyle changes support general cardiovascular health but have not been shown to prevent penetrance of a pathogenic sarcomeric/FLNC allele. Excessive preload depletion may worsen output after disease develops; this is a management issue, not an etiologic risk factor. (dong2024novelflncvariants pages 4-6, wang2023engineeredcardiactissue pages 1-3)

## 6. Mechanism and pathophysiology

### Causal chains

1. **Troponin pathway:** TNNI3/TNNT2 variant → altered troponin–actin–tropomyosin regulation → excessive myofilament Ca²⁺ sensitivity → persistent tension during diastole → impaired relaxation and elevated end-diastolic pressure → atrial dilation, pulmonary venous hypertension, congestion, arrhythmia, and heart failure. Strong Ca²⁺ sensitization tends toward HCM/RCM, whereas reduced sensitivity can produce DCM. (kim2021geneticsofcardiomyopathy pages 4-5, liu2016restrictivecardiomyopathycaused pages 1-2)
2. **FLNC pathway:** altered filamin-C structure/splicing → defective Z-disc/intercalated-disc mechanotransduction and sarcomere organization, sometimes impaired autophagic/lysosomal flux → contractile-relaxation uncoupling and increased passive tension → restrictive filling. Patient-specific tissue showed increased calcium-transient decay time, reduced active force, increased passive tension, and slower relaxation. (wang2023engineeredcardiactissue pages 4-7, wang2023engineeredcardiactissue pages 3-4)
3. **Downstream remodeling:** persistent pressure and mechanical stress → fibroblast/ECM remodeling and fibrosis → still lower compliance. FLNC is also expressed in fibroblasts; the 2023 cardiomyocyte-only system could not model this non-myocyte contribution. (wang2023engineeredcardiactissue pages 8-9)
4. **Infiltrative/storage phenocopies:** extracellular amyloid, intracellular storage, iron, granulomas, or endomyocardial fibrosis → myocardial/endocardial stiffening → the same hemodynamic syndrome through a different upstream mechanism. (kim2021geneticsofcardiomyopathy pages 22-23)

Suggested ontology annotations include **GO:0006936 muscle contraction**, **GO:0060048 cardiac muscle contraction**, **GO:0055001 muscle-cell development**, **GO:0007015 actin-filament organization**, **GO:0006874 intracellular calcium-ion homeostasis**, **GO:0030198 extracellular-matrix organization**, and **GO:0048771 tissue remodeling**. Principal cells are **cardiac muscle cell/cardiomyocyte (CL:0000746)** and **fibroblast (CL:0000057)**; endothelial, conduction-system, and immune cells are secondary/context-dependent.

No reproducible RCM-specific bulk transcriptomic, proteomic, metabolomic, lipidomic, single-cell, or spatial signature is clinically validated. The most advanced disease-specific platform is patient-derived iPSC cardiomyocytes combined with CRISPR isogenic controls and 3D engineered cardiac tissue. (wang2023engineeredcardiactissue pages 3-4, wang2023engineeredcardiactissue pages 1-3)

## 7. Anatomical structures affected

The primary organ is the **heart (UBERON:0000948)**, particularly **myocardium (UBERON:0002349)** of both ventricles. The left and right atria enlarge secondarily; pulmonary vasculature develops post-capillary hypertension, and liver, kidneys, and peripheral tissues can be affected by congestion or reduced output. Disease is generally bilateral/biventricular rather than lateralized. Relevant subcellular structures include **sarcomere (GO:0030017)**, **Z disc (GO:0030018)**, **myofibril (GO:0030016)**, **actin cytoskeleton (GO:0015629)**, intercalated disc, sarcoplasmic reticulum, lysosome, and autophagosome. (dong2024novelflncvariants pages 1-2, wang2023engineeredcardiactissue pages 3-4)

## 8. Temporal development

Onset is usually insidious and chronic but ranges from congenital/infantile to late adult. Early disease may show isolated diastolic dysfunction and atrial enlargement with preserved EF. Intermediate disease adds exertional symptoms, congestion, pulmonary hypertension, atrial arrhythmia, and thromboembolic risk. Advanced disease includes low output, progressive systolic dysfunction, ventricular arrhythmia, transplant, or death. Spontaneous durable remission of primary genetic RCM is not established; temporary improvement may follow treatment of a superimposed infection or reversible secondary cause. Childhood onset, severe pulmonary hypertension, and de novo variants warrant early specialist/transplant assessment. (schubert2018theuseof pages 17-21, dong2024novelflncvariants pages 4-6)

## 9. Inheritance and population

Primary familial RCM is usually **autosomal dominant**, with age-dependent/incomplete penetrance and markedly variable expressivity. Recessive disease can occur in syndromic/metabolic conditions and rare biallelic cardiomyopathy genotypes. Germline mosaicism is biologically possible after an apparently de novo result but is not quantitatively defined; anticipation is not established. No robust founder allele, carrier-frequency estimate, sex bias, or ancestry-specific prevalence is established for primary RCM. (kim2021geneticsofcardiomyopathy pages 22-23, kim2021geneticsofcardiomyopathy pages 4-5)

RCM constitutes approximately **2.5–5%** of pediatric cardiomyopathies, and around **30%** of affected children reportedly have a positive family history. Population prevalence and incidence per 100,000 remain undefined. Typical RCM physiology was found in **1.5% of more than 1,200 familial HCM patients**, illustrating phenotype overlap rather than general-population prevalence. (schubert2018theuseof pages 17-21, kim2021geneticsofcardiomyopathy pages 4-5)

## 10. Diagnostics

### Clinical workflow

1. **Phenotype:** history, three-generation pedigree, examination, ECG/Holter, BNP or NT-proBNP, troponin when injury is suspected, renal/hepatic indices, and echocardiography.
2. **Echocardiography:** nondilated ventricles, little/no hypertrophy, severe restrictive filling, low tissue-Doppler velocities, biatrial enlargement, valve regurgitation, pulmonary-pressure estimates, and initially preserved EF. (wang2023engineeredcardiactissue pages 3-4, liu2016restrictivecardiomyopathycaused pages 2-3)
3. **CMR:** ventricular volumes/function, atrial size, edema, late gadolinium enhancement, T1/T2 mapping and extracellular volume; especially valuable for amyloid, iron, inflammation, endomyocardial disease, and fibrosis.
4. **Catheterization:** confirms elevated filling pressures, restrictive pressure contours, pulmonary vascular resistance, and low output when noninvasive findings are uncertain or transplant assessment requires it.
5. **Biopsy:** not routine for every familial case; use when amyloid, myocarditis, storage disease, sarcoid, eosinophilic disease, or another tissue diagnosis would change treatment. Sarcomeric RCM may show myofibrillar disarray but this is not gene-specific. (kim2021geneticsofcardiomyopathy pages 4-5)

The principal differential is **constrictive pericarditis**, distinguished using tissue Doppler, respiratory ventricular interdependence, CT/CMR pericardial assessment, and catheterization. Other differentials include HCM with restrictive physiology, pulmonary hypertension, valvular disease, congenital heart disease, amyloidosis, Fabry/storage disease, hemochromatosis, sarcoidosis, and endomyocardial fibrosis.

### Genetic testing

Use a curated cardiomyopathy panel including at minimum **TNNI3, TNNT2, FLNC, MYH7, MYPN, ACTC1, MYBPC3, MYL2, MYL3, TTN, DES, CRYAB, and BAG3**, plus phenotype-driven phenocopy genes such as **TTR, GLA, GAA, GBA1, and HFE**. Trio testing is particularly useful in severe pediatric cases. CNV analysis should accompany sequencing. WES/WGS is reasonable after a negative panel, syndromic presentation, or suspected novel gene; RNA/minigene studies can resolve splice effects, as shown for FLNC c.3962A>T. CMA, karyotype, FISH, repeat-expansion testing, and mtDNA sequencing are phenotype-driven rather than routine. A VUS is not diagnostic and should not direct predictive testing. (dong2024novelflncvariants pages 1-2, dong2024novelflncvariants pages 4-6)

Screen first-degree relatives with history, examination, ECG, and echocardiography; offer cascade testing only after identifying a pathogenic/likely pathogenic familial variant. The completed **PCM GENES** prospective cohort enrolled **544** participants and used tiered exome analysis to correlate genotype with death/transplant outcomes. (NCT01873963 chunk 1)

## 11. Outcome and prognosis

RCM has one of the poorest cardiomyopathy prognoses. Nearly **50% of pediatric patients reportedly die or require transplantation within three years**. One genetic/overlap cohort had a **56% composite outcome of death, transplantation, or appropriate ICD discharge**. Sudden cardiac death, progressive heart failure, atrial and ventricular arrhythmias, thromboembolism, pulmonary hypertension, hepatic congestion, and multiorgan dysfunction are major complications. (schubert2018theuseof pages 17-21, kim2021geneticsofcardiomyopathy pages 4-5)

Adverse prognostic features include early onset, de novo pathogenic variants, worsening symptoms, pulmonary hypertension/high pulmonary vascular resistance, declining EF, fibrosis, arrhythmias, syncope, rising natriuretic peptides, and end-organ dysfunction. Reliable disease-wide 5- or 10-year survival, life expectancy, and standardized quality-of-life statistics are unavailable because cohorts are small and etiologically mixed.

## 12. Treatment

### Current real-world management

- **Congestion:** cautious loop diuretics, sometimes mineralocorticoid-receptor antagonists; avoid excessive preload reduction because the stiff ventricle is filling-dependent.
- **Arrhythmias:** rhythm/rate management, cardioversion or ablation when appropriate; pacemaker for clinically important conduction disease. ICD decisions are individualized because RCM-specific primary-prevention evidence is sparse.
- **Thromboembolism:** anticoagulation for atrial fibrillation, intracardiac thrombus, or other standard indications.
- **Heart-failure drugs:** ACE inhibitor/ARB/ARNI, beta blocker, MRA, and SGLT2 inhibitor may be used for conventional indications, hypertension, or systolic dysfunction, but none has proven disease-modifying efficacy in primary RCM with preserved EF.
- **Cause-directed treatment:** treat AL/ATTR amyloidosis, Fabry disease, iron overload, sarcoid/eosinophilic inflammation, or storage disease according to the underlying disorder.
- **Transplantation:** definitive therapy for refractory primary RCM. Early referral is important; severe pulmonary vascular disease can preclude isolated heart transplant and occasionally necessitate heart–lung transplantation. (schubert2018theuseof pages 17-21, wang2023engineeredcardiactissue pages 1-3)

Suggested NCIT concepts include **Diuretic Therapy**, **Antiarrhythmic Therapy**, **Anticoagulation Therapy**, **Pacemaker Implantation**, **Implantable Cardioverter-Defibrillator Placement**, **Cardiac Transplantation**, **Genetic Counseling**, and **Cardiac Rehabilitation**; terminology IDs should be version-validated at ingestion.

### Experimental therapy and recent development

Wang *et al.* screened **2,185 compounds** in FLNC-mutant iPSC cardiomyocytes. The PDE3 inhibitor **trequinsin** reduced calcium-relaxation tau by approximately **50%**, reduced passive tension, and improved relaxation/contraction kinetics in engineered tissue; no increased after-depolarization or LDH cytotoxicity was detected under the tested conditions. This is **preclinical genotype-specific evidence**, not justification for clinical PDE3 therapy; chronic PDE3 inhibition has recognized arrhythmic and mortality concerns. (wang2023engineeredcardiactissue pages 4-7, wang2023engineeredcardiactissue pages 3-4)

### Relevant studies

- **NCT01873963, PCM GENES:** completed, prospective observational cohort, actual enrollment **544**; pediatric DCM/HCM/RCM genotype–phenotype analysis. [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT01873963). (NCT01873963 chunk 1)
- **NCT02432092:** recruiting family-based Pediatric Cardiomyopathy Mutation Analysis, estimated **300** participants. [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT02432092). (NCT02432092 chunk 1)
- **NCT06794710, EARLY-MYO-RARE:** posted **27 January 2025**, not yet recruiting in the retrieved record; randomized multimodal-imaging/risk-guided management study, estimated **300**, including RCM. It is not a genotype-specific RCM drug trial. [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT06794710). (NCT06794710 chunk 1)

No approved gene, cell, RNA, or CRISPR therapy for primary RCM was identified, and no RCM-specific pharmacogenomic guideline is established.

## 13. Prevention

Primary prevention of a de novo or inherited allele is not currently possible. Secondary prevention consists of genetic counseling, cascade testing, serial ECG/echo surveillance, early evaluation of symptoms, and reproductive options such as preimplantation genetic testing or prenatal diagnosis after a familial pathogenic variant is established. Tertiary prevention includes congestion control, arrhythmia and thromboembolism surveillance, avoiding cardiotoxic exposures, vaccination/general infection prevention appropriate to heart-failure patients, and timely transplant referral. There is no RCM-specific vaccine, newborn-screening program, prophylactic drug, or population screening recommendation. (kim2021geneticsofcardiomyopathy pages 22-23, NCT01873963 chunk 1)

## 14. Other species and natural disease

RCM-like disease occurs clinically in companion animals, but the retrieved evidence did not establish a well-validated naturally occurring breed-specific orthologous genetic RCM suitable for confident VBO/OMIA annotation. There is no zoonotic or transmissible component. Orthologous sarcomeric and FLNC pathways are deeply conserved, which supports engineered mouse models, but experimental models should not be mislabeled as natural veterinary disease.

## 15. Model organisms and experimental systems

### Mouse models

Transgenic mice expressing human-equivalent **TNNI3 p.Arg192His** (mouse cTnI p.Arg193His) or **p.Lys178Glu** (mouse p.Lys179Glu) reproduce impaired relaxation and biatrial enlargement without ventricular hypertrophy. The causal mechanism is marked myofibrillar Ca²⁺ hypersensitivity. Crossing p.Arg193His mice with an N-terminally deleted cTnI line that lowers Ca²⁺ sensitivity rescued diastolic dysfunction and the restrictive phenotype, providing target-validation evidence for calcium desensitization. DOI: [10.3389/fphys.2016.00629](https://doi.org/10.3389/fphys.2016.00629), published **19 December 2016**. (liu2016restrictivecardiomyopathycaused pages 2-3, liu2016restrictivecardiomyopathycaused pages 1-2)

Exact abstract quote: **“the deficiency of cTnI or mutations in cTnI … results in diastolic dysfunction (impaired relaxation) due to an increased myofibril sensitivity to calcium.”** (liu2016restrictivecardiomyopathycaused pages 1-2)

### Human cellular and engineered-tissue model

Patient-derived **FLNC c.7416_7418delGAA** iPSCs, a CRISPR-corrected isogenic control, a CRISPR knock-in reporter line, and fibrin-based 3D engineered cardiac tissues reproduced reduced active force, sarcomere disorganization, increased passive tension, slowed contraction/relaxation, and abnormal calcium decay. The platform enabled the trequinsin screen and is currently the clearest precision-model implementation for primary RCM. Limitations include immature iPSC cardiomyocytes, short experimental times, a single genotype, and failure to model fibroblast, vascular, immune, neurohumoral, and whole-organ hemodynamic contributions. (wang2023engineeredcardiactissue pages 8-9, wang2023engineeredcardiactissue pages 4-7, wang2023engineeredcardiactissue pages 3-4, wang2023engineeredcardiactissue pages 1-3)

## Evidence-quality assessment and knowledge gaps

The strongest evidence consists of human familial segregation/de novo data, functional assays with isogenic controls, and consistent RCM physiology in TNNI3 mice. Most clinical statistics derive from small pediatric or genetically enriched cohorts, not population surveillance. Disease databases may mix primary RCM with metabolic/infiltrative causes; therefore, gene–disease validity should be assessed at the specific etiologic-entity level. Major gaps are population prevalence/incidence, ancestry-specific penetrance, validated modifiers, RCM-specific patient-reported outcomes, prospective risk models, and controlled disease-specific therapy trials. The 2023–2024 FLNC studies materially advance mechanism and variant interpretation but do not yet alter standard treatment. (OpenTargets Search: restrictive cardiomyopathy, dong2024novelflncvariants pages 1-2, wang2023engineeredcardiactissue pages 4-7)

References

1. (kim2021geneticsofcardiomyopathy pages 22-23): Kyung-Hee Kim and Naveen L. Pereira. Genetics of cardiomyopathy: clinical and mechanistic implications for heart failure. Korean Circulation Journal, 51:797-836, Jul 2021. URL: https://doi.org/10.4070/kcj.2021.0154, doi:10.4070/kcj.2021.0154. This article has 66 citations and is from a peer-reviewed journal.

2. (schubert2018theuseof pages 17-21): JA Schubert. The use of genetic analyses and functional assays for the interpretation of rare variants in pediatric heart disease. Unknown journal, 2018.

3. (dong2024novelflncvariants pages 1-2): Rui Dong, Xin Zhou, Haiyan Zhang, Bingyi Shi, Guohua Liu, and Yi Liu. Novel flnc variants in pediatric cardiomyopathy: an insight into disease mechanisms. Human Genomics, Oct 2024. URL: https://doi.org/10.1186/s40246-024-00683-9, doi:10.1186/s40246-024-00683-9. This article has 3 citations and is from a peer-reviewed journal.

4. (wang2023engineeredcardiactissue pages 1-3): Bryan Z. Wang, Trevor R. Nash, Xiaokan Zhang, Jenny Rao, Laura Abriola, Youngbin Kim, Sergey Zakharov, Michael Kim, Lori J. Luo, Margaretha Morsink, Bohao Liu, Roberta I. Lock, Sharon Fleischer, Manuel A. Tamargo, Michael Bohnen, Carrie L. Welch, Wendy K. Chung, Steven O. Marx, Yulia V. Surovtseva, Gordana Vunjak-Novakovic, and Barry M. Fine. Engineered cardiac tissue model of restrictive cardiomyopathy for drug discovery. Cell Reports Medicine, 4:100976, Mar 2023. URL: https://doi.org/10.1016/j.xcrm.2023.100976, doi:10.1016/j.xcrm.2023.100976. This article has 35 citations and is from a peer-reviewed journal.

5. (OpenTargets Search: restrictive cardiomyopathy): Open Targets Query (restrictive cardiomyopathy, 28 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (NCT02432092 chunk 1): Stephanie Ware. Pediatric Cardiomyopathy Mutation Analysis. Indiana University. 2014. ClinicalTrials.gov Identifier: NCT02432092

7. (kim2021geneticsofcardiomyopathy pages 4-5): Kyung-Hee Kim and Naveen L. Pereira. Genetics of cardiomyopathy: clinical and mechanistic implications for heart failure. Korean Circulation Journal, 51:797-836, Jul 2021. URL: https://doi.org/10.4070/kcj.2021.0154, doi:10.4070/kcj.2021.0154. This article has 66 citations and is from a peer-reviewed journal.

8. (dong2024novelflncvariants pages 4-6): Rui Dong, Xin Zhou, Haiyan Zhang, Bingyi Shi, Guohua Liu, and Yi Liu. Novel flnc variants in pediatric cardiomyopathy: an insight into disease mechanisms. Human Genomics, Oct 2024. URL: https://doi.org/10.1186/s40246-024-00683-9, doi:10.1186/s40246-024-00683-9. This article has 3 citations and is from a peer-reviewed journal.

9. (wang2023engineeredcardiactissue pages 3-4): Bryan Z. Wang, Trevor R. Nash, Xiaokan Zhang, Jenny Rao, Laura Abriola, Youngbin Kim, Sergey Zakharov, Michael Kim, Lori J. Luo, Margaretha Morsink, Bohao Liu, Roberta I. Lock, Sharon Fleischer, Manuel A. Tamargo, Michael Bohnen, Carrie L. Welch, Wendy K. Chung, Steven O. Marx, Yulia V. Surovtseva, Gordana Vunjak-Novakovic, and Barry M. Fine. Engineered cardiac tissue model of restrictive cardiomyopathy for drug discovery. Cell Reports Medicine, 4:100976, Mar 2023. URL: https://doi.org/10.1016/j.xcrm.2023.100976, doi:10.1016/j.xcrm.2023.100976. This article has 35 citations and is from a peer-reviewed journal.

10. (wang2023engineeredcardiactissue pages 4-7): Bryan Z. Wang, Trevor R. Nash, Xiaokan Zhang, Jenny Rao, Laura Abriola, Youngbin Kim, Sergey Zakharov, Michael Kim, Lori J. Luo, Margaretha Morsink, Bohao Liu, Roberta I. Lock, Sharon Fleischer, Manuel A. Tamargo, Michael Bohnen, Carrie L. Welch, Wendy K. Chung, Steven O. Marx, Yulia V. Surovtseva, Gordana Vunjak-Novakovic, and Barry M. Fine. Engineered cardiac tissue model of restrictive cardiomyopathy for drug discovery. Cell Reports Medicine, 4:100976, Mar 2023. URL: https://doi.org/10.1016/j.xcrm.2023.100976, doi:10.1016/j.xcrm.2023.100976. This article has 35 citations and is from a peer-reviewed journal.

11. (liu2016restrictivecardiomyopathycaused pages 2-3): Xiaoyan Liu, Lei Zhang, Daniel Pacciulli, Jianquan Zhao, Changlong Nan, Wen Shen, Junjun Quan, Jie Tian, and Xupei Huang. Restrictive cardiomyopathy caused by troponin mutations: application of disease animal models in translational studies. Frontiers in Physiology, Dec 2016. URL: https://doi.org/10.3389/fphys.2016.00629, doi:10.3389/fphys.2016.00629. This article has 26 citations.

12. (liu2016restrictivecardiomyopathycaused pages 1-2): Xiaoyan Liu, Lei Zhang, Daniel Pacciulli, Jianquan Zhao, Changlong Nan, Wen Shen, Junjun Quan, Jie Tian, and Xupei Huang. Restrictive cardiomyopathy caused by troponin mutations: application of disease animal models in translational studies. Frontiers in Physiology, Dec 2016. URL: https://doi.org/10.3389/fphys.2016.00629, doi:10.3389/fphys.2016.00629. This article has 26 citations.

13. (NCT01873963 chunk 1): Steve Lipshultz. Genotype-Phenotype Associations in Pediatric Cardiomyopathy (PCM GENES). Wayne State University. 2013. ClinicalTrials.gov Identifier: NCT01873963

14. (NCT06794710 chunk 1):  Early Identification and Treatment of Rare Cardiomyopathy Cohorts. RenJi Hospital. 2025. ClinicalTrials.gov Identifier: NCT06794710

15. (wang2023engineeredcardiactissue pages 8-9): Bryan Z. Wang, Trevor R. Nash, Xiaokan Zhang, Jenny Rao, Laura Abriola, Youngbin Kim, Sergey Zakharov, Michael Kim, Lori J. Luo, Margaretha Morsink, Bohao Liu, Roberta I. Lock, Sharon Fleischer, Manuel A. Tamargo, Michael Bohnen, Carrie L. Welch, Wendy K. Chung, Steven O. Marx, Yulia V. Surovtseva, Gordana Vunjak-Novakovic, and Barry M. Fine. Engineered cardiac tissue model of restrictive cardiomyopathy for drug discovery. Cell Reports Medicine, 4:100976, Mar 2023. URL: https://doi.org/10.1016/j.xcrm.2023.100976, doi:10.1016/j.xcrm.2023.100976. This article has 35 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Restrictive_Cardiomyopathy-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 1 |
| Off topic | 0 |

All extracted references resolved successfully.