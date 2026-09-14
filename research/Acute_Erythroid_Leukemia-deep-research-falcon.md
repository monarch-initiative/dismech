---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-26T16:27:37.452760'
end_time: '2026-08-26T16:39:26.180666'
duration_seconds: 708.73
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Acute Erythroid Leukemia
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 22
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 2
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Acute_Erythroid_Leukemia-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acute Erythroid Leukemia
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Acute Erythroid Leukemia** covering all of the
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
- **Disease Name:** Acute Erythroid Leukemia
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Acute Erythroid Leukemia** covering all of the
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


# Acute Erythroid Leukemia: Disease Characteristics Research Report

**Evidence cutoff:** literature prioritized through 2024. Because acute erythroid leukemia (AEL) is exceptionally rare and its definition has repeatedly changed, most clinical evidence consists of retrospective cohorts, registry studies, case series, and mechanistic models rather than prospective AEL-specific trials. Numerical comparisons across historical studies must therefore be interpreted cautiously.

## Executive summary

AEL is a rare, rapidly progressive erythroid-lineage acute leukemia centered in bone marrow. The **WHO 2022/WHO-HAEM5** morphologic entity requires **≥80% erythroid precursors and ≥30% proerythroblasts** in marrow. By contrast, the **2022 International Consensus Classification (ICC)** generally subsumes the corresponding TP53-mutated disease under **AML with mutated TP53**, requiring a somatic TP53 variant allele fraction (VAF) >10% and the applicable blast/PEL criterion. Thus, “AEL,” “pure erythroid leukemia,” and historical “AML-M6” are not perfectly interchangeable across datasets. A 2024 expert review summarizes the current biology directly: **“This type of leukemia is typically associated with biallelic TP53 mutations and a complex karyotype, specifically 5q and 7q deletions.”** [Fernandes et al., published 6 June 2024, DOI: https://doi.org/10.3390/ijms25116256] (fernandes2024acuteerythroidleukemia pages 2-4, fernandes2024acuteerythroidleukemia pages 1-2)

The disease primarily affects older adults, produces severe marrow failure, and has a median survival commonly measured in months. Intensive AML chemotherapy or hypomethylating agents may induce remission, but allogeneic hematopoietic-cell transplantation (allo-HCT) is the only established potentially curative strategy. TP53 loss, complex/monosomal cytogenetics, and erythroid-state BCL-XL dependence help explain chemotherapy resistance and possible relative resistance to venetoclax. No AEL-specific approved molecular therapy or prevention program exists. (fernandes2024acuteerythroidleukemia pages 1-2, fernandes2024acuteerythroidleukemia pages 12-14, fernandes2024acuteerythroidleukemia pages 11-12)

## 1. Disease information

### Definition and classification

* **Category:** rare hematologic malignancy; acute myeloid/erythroid-lineage leukemia.
* **MONDO:** **MONDO:0017858** (acute erythroid leukemia). OpenTargets recognizes this disease entity but returned no curated disease-specific target associations, illustrating the limited structured evidence base. (OpenTargets Search: acute erythroid leukemia)
* **Current WHO definition:** marrow with ≥80% immature erythroid cells/erythroid precursors, including ≥30% proerythroblasts. (fernandes2024acuteerythroidleukemia pages 2-4, fernandes2024acuteerythroidleukemia pages 1-2)
* **ICC 2022:** corresponding cases are generally classified as **AML with mutated TP53** when there are ≥20% blood or marrow blasts—or pure erythroid leukemia morphology—and a somatic TP53 mutation with VAF >10%. (fernandes2024acuteerythroidleukemia pages 2-4, ohan2024anunusualcase pages 3-4)
* **Historical terminology:** Di Guglielmo disease/erythroleukemia; FAB **AML-M6**; M6a erythroid/myeloid leukemia; M6b or **pure erythroid leukemia (PEL)**. “Acute erythroleukemia” is also used, but older M6 cohorts include cases that would now be MDS or another genetically defined AML. (fernandes2024acuteerythroidleukemia pages 1-2)

A rare TP53-wild-type exception illustrates why morphology and genetics must both be recorded: a 2024 PEL-like case had normal 46,XY cytogenetics with **NPM1** and **NRAS**, but no TP53 mutation; under modern systems it may instead be an NPM1-mutated myeloid neoplasm with erythroid predominance. [Ohan et al., July 2024, DOI: https://doi.org/10.1007/s12308-024-00588-5] (ohan2024anunusualcase pages 3-4)

**Other identifiers:** a unique OMIM disease entry is not established because AEL is predominantly an acquired somatic cancer, not a Mendelian disorder. ICD-10-CM generally places it within AML codes rather than a robust AEL-specific code; ICD-11 and MeSH similarly require classification under acute myeloid/erythroid leukemia concepts. Local coding should retain both the edition and morphology/genotype.

**Evidence provenance:** the report uses aggregated disease-level literature, registries, cohorts, and experimental studies—not individual EHR records. Case reports are identified as such.

## 2. Etiology, risk, and protective factors

AEL is usually an **acquired clonal disease**. Its proximal cause is accumulation of somatic genomic lesions in hematopoietic stem/progenitor cells, most characteristically multi-hit TP53 disruption plus chromosomal instability and erythroid differentiation/signaling abnormalities. It may arise de novo, after MDS or an MPN, or following cytotoxic chemotherapy/radiotherapy. Therapy-related and antecedent-MDS disease have especially short reported median survivals—approximately 2.3 and 2.6 months versus 3.9 months for de novo disease in one synthesis. (fernandes2024acuteerythroidleukemia pages 2-4)

### Risk factors

* **Age:** median diagnosis age approximately 67 years; reported distribution is bimodal, around ages 20 and 70. Older age likely reflects clonal hematopoiesis, accumulated mutations, antecedent myeloid disease, and treatment exposure. (fernandes2024acuteerythroidleukemia pages 2-4)
* **Sex:** reported male:female ratio approximately **2.4:1**. (fernandes2024acuteerythroidleukemia pages 2-4)
* **Antecedent disease:** MDS, MPN, and other myeloid neoplasms are important clinical contexts.
* **Iatrogenic/environmental:** previous alkylating agents, topoisomerase-II inhibitors, radiation, and benzene are plausible AML/AEL risks; AEL-specific attributable fractions are unavailable. (fernandes2024acuteerythroidleukemia pages 1-2)
* **Genetic susceptibility:** no recurrent germline variant is established as a specific inherited cause. Germline TP53 cancer predisposition and inherited marrow-failure/AML-predisposition genes should be considered when age, phenotype, or family history is suggestive, but most TP53 lesions in AEL are somatic.

No validated **genetic or lifestyle protective factor** is known. Avoiding benzene and unnecessary ionizing radiation reduces general AML risk, but no study demonstrates AEL-specific prevention. There is also no established AEL-specific gene–environment interaction; a plausible model is that genotoxic exposure selects or generates TP53-defective clones, after which cooperating signaling/chromatin lesions impose erythroid lineage bias.

## 3. Phenotypes

The onset is generally acute or subacute and severe. Marrow replacement and ineffective erythropoiesis cause progressive cytopenias and constitutional symptoms.

* **Anemia**—usually severe and nearly universal clinically; fatigue, exertional intolerance, dyspnea, and pallor follow. One review reports a median hemoglobin of 7.5, although the stated unit “g/L” is almost certainly a source/unit error and should not be propagated without checking the underlying cohort. Suggested HPO: **HP:0001903**. (fernandes2024acuteerythroidleukemia pages 2-4)
* **Thrombocytopenia**—bleeding, bruising, or petechiae; HPO **HP:0001873**.
* **Neutropenia/pancytopenia**—infection risk and fever; pancytopenia HPO **HP:0001876**, fever **HP:0001945**.
* **Pallor**—HPO **HP:0000980**; largely downstream of anemia.
* **Hepatomegaly/splenomegaly**—variable extramedullary erythroid/leukemic involvement; use separate HPO hepatomegaly and splenomegaly terms after identifier validation.
* **Hemolysis laboratory evidence**—variable; possible increased bilirubin/LDH and reduced haptoglobin, but AEL-specific frequencies are not well quantified.
* **Marrow abnormalities**—marked hypercellularity, erythroid predominance, dyserythropoiesis, and numerous immature proerythroblasts. Higher proerythroblast proportion is associated with poorer outcome. (fernandes2024acuteerythroidleukemia pages 2-4)

Symptoms progress rather than fluctuate without effective treatment. Quantitative phenotype penetrance and AEL-specific EQ-5D/SF-36 data are unavailable. Quality of life is severely affected through transfusion dependence, fatigue, bleeding/infection risk, repeated hospitalization, chemotherapy toxicity, and limited survival.

## 4. Genetic and molecular information

### Core lesions

**TP53** is the defining molecular hallmark of modern AEL/PEL. Reported mutation frequency varies dramatically with historical definitions—43.5% in a 92-patient cohort and 36.3% in a 58-patient cohort, but **100%** in recent Mayo (41 cases) and MD Anderson (21 cases) series applying modern 2016–2022 concepts. The common multi-hit configuration is one mutated allele plus deletion/loss of the other, producing biallelic loss of function. These are somatic SNVs/indels and/or 17p deletion/copy-neutral LOH; population allele frequency is therefore not meaningfully represented by germline gnomAD frequency. (fernandes2024acuteerythroidleukemia pages 7-8)

Complex karyotype—at least three abnormalities—is nearly uniform in modern PEL cohorts. Recurrent lesions include **−5/del(5q), −7/del(7q), trisomy 8, and 17p13/TP53 abnormalities**. Complex and monosomal genomes reflect p53-deficient tolerance of DNA damage and mitotic errors. (fernandes2024acuteerythroidleukemia pages 4-5, fernandes2024acuteerythroidleukemia pages 2-4)

Additional recurrent/cooperating genes and lesions include:

* **EPOR/JAK2/STAT signaling:** EPOR overexpression or amplification, JAK2 gain/JAK2V617F, and occasional EPOR/JAK2/ERG copy gains; one synthesis reports JAK2 variants in 30%, although estimates are strongly cohort-dependent. (fernandes2024acuteerythroidleukemia pages 4-5)
* **RAS/MAPK:** NRAS, KRAS, PTPN11, NF1; one older cohort found NRAS/KRAS/FLT3 lesions in only 3/92 cases, demonstrating heterogeneity. (fernandes2024acuteerythroidleukemia pages 4-5, fagnan2021molecularlandscapesand pages 1-2)
* **Erythroid/transcriptional regulation:** GATA1-pathway abnormalities in >25% in one analysis; **GATA2, CEBPA, ERG, FLI1, CDX4**, and rare **NFIA::ETO2**. (fernandes2024acuteerythroidleukemia pages 7-8, fernandes2024acuteerythroidleukemia pages 4-5)
* **Epigenetic/chromatin:** **TET2, DNMT3A, ASXL1, IDH2, BCOR/BCORL1**. One cohort found epigenetic-regulator lesions in 33.3%, including eight TET2 nonsense and five DNMT3A mutations. (fernandes2024acuteerythroidleukemia pages 7-8)
* **Pediatric disease:** NUP98 fusions appear enriched; one analysis reported 31.8% in the AEL category versus 6.7% in other pediatric AML, although the AEL denominator was very small. (fernandes2024acuteerythroidleukemia pages 8-10)
* **Rare actionable exceptions:** NTRK1 alterations and NPM1/NRAS-mutated TP53-wild-type disease are reported, but these are not typical. (ohan2024anunusualcase pages 3-4, fagnan2021molecularlandscapesand pages 7-8)

ACMG germline labels should not be automatically applied to these tumor variants. Somatic clinical interpretation should use AMP/ASCO/CAP, ClinGen Somatic, OncoKB, or equivalent cancer frameworks. Paired normal testing is indicated when germline predisposition is suspected.

### Epigenetics and modifiers

BCOR/BCORL1 loss disrupts noncanonical PRC1.1: the chromatin-targeting component remains localized but becomes uncoupled from the RING–PCGF repressive core, causing loss of repression, transcriptional activation of oncogenic targets, and treatment resistance. This is mechanistically supported in leukemia systems, although it is not unique to AEL. [Schaefer et al., published March 2022, DOI: https://doi.org/10.1158/2643-3230.BCD-21-0115] (fernandes2024acuteerythroidleukemia pages 7-8)

No validated modifier allele reliably predicts severity specifically within AEL. TP53 allelic state, complex karyotype, antecedent disease, age, and transplant eligibility currently carry more clinical value than individual secondary variants.

## 5. Environmental information

There is no infectious cause and no zoonotic or transmissible component. General myeloid-neoplasm exposures—benzene, ionizing radiation, tobacco-associated benzene, and previous leukemogenic chemotherapy—are relevant, but AEL-specific dose–response statistics are unavailable. Smoking cessation, occupational exposure controls, and radiation minimization are prudent general AML prevention measures, not proven AEL-specific interventions. (fernandes2024acuteerythroidleukemia pages 1-2)

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream clonal initiation:** an HSPC acquires TP53 dysfunction, frequently followed by loss of the second allele. This permits survival after genotoxic stress, defective apoptosis/checkpoint control, and chromosomal instability.
2. **Cooperating lineage/signaling lesions:** gains or mutations involving EPOR/JAK2/STAT, RAS/MAPK, ERG, GATA1/GATA2/CEBPA, or BCOR/DNMT3A remodel growth signaling and lineage programs.
3. **Erythroid commitment with maturation arrest:** GATA1/KLF1/ZFPM1-centered chromatin and transcription programs become distorted; immature erythroid progenitors proliferate but fail terminal differentiation.
4. **Leukemic expansion:** EPOR activates JAK2–STAT, PI3K–AKT, and ERK pathways, promoting survival and proliferation. RAS12V can block EPO-induced differentiation in murine erythroleukemia cells. (fernandes2024acuteerythroidleukemia pages 7-8, fernandes2024acuteerythroidleukemia pages 4-5)
5. **Clinical injury:** marrow replacement and ineffective hematopoiesis cause anemia, thrombocytopenia, neutropenia, infection, bleeding, hypoxia/fatigue, and occasionally hepatic/splenic infiltration.
6. **Resistance/relapse:** multi-hit TP53, complex cytogenetics, chromatin dysregulation, and an erythroid BCL-XL survival state reduce chemotherapy durability and may blunt BCL2-selective venetoclax activity. (fernandes2024acuteerythroidleukemia pages 12-14, fernandes2024acuteerythroidleukemia pages 16-18)

### Functional and multi-omics findings

Transcriptomic studies separate signaling/TP53/chromatin-associated groups, but no single-cell or spatial atlas is sufficiently validated for routine AEL classification. GATA2 plus biallelic CEBPA lesions increase accessibility at erythroid GATA1/ZFPM1/KLF1 motifs and decrease myeloid-motif accessibility in models. EPOR/JAK2/ERG amplification and high BCL-XL expression identify potential dependencies. AEL-specific proteomics, metabolomics, and lipidomics remain major evidence gaps. (fernandes2024acuteerythroidleukemia pages 4-5, fagnan2021molecularlandscapesand pages 6-7, fernandes2024acuteerythroidleukemia pages 12-14)

Suggested annotations include GO:0030218 erythrocyte differentiation, GO:0008283 cell proliferation, GO:0097190 apoptotic signaling, GO:0007259 JAK–STAT cascade, GO:0006325 chromatin organization; CL proerythroblast/erythroid progenitor and hematopoietic stem/progenitor cell terms.

## 7. Anatomical structures affected

The **bone marrow (UBERON:0002371)** is primary; **blood (UBERON:0000178)** reflects cytopenias and circulating blasts. Secondary involvement may include **spleen (UBERON:0002106)** and **liver (UBERON:0002107)**, producing hepatosplenomegaly. There is no lateralization. At tissue/cell level, malignant proerythroblasts and erythroid progenitors displace normal erythroid, myeloid, and megakaryocytic hematopoiesis. At subcellular level, the nucleus/chromatin, transcriptional machinery, cytokine receptors/plasma membrane, and downstream cytoplasmic kinase cascades are central.

## 8. Temporal development

Typical onset is acute/subacute in late adulthood, although pediatric and young-adult peaks occur. Untreated disease progresses rapidly to profound marrow failure. There is no AJCC solid-tumor staging system; clinically relevant states are newly diagnosed, refractory, remission/MRD-positive or negative, relapsed, and post-transplant. Spontaneous durable remission is not expected. The principal intervention window is rapid diagnostic work-up followed by remission induction and, in eligible responders, prompt allo-HCT.

## 9. Inheritance and population

AEL represents approximately **2% of AML** in historical estimates, but its true incidence cannot be reliably inferred because modern WHO/ICC reclassify many old M6 cases. Median age is about 67 years and males predominate approximately 2.4:1. No robust ethnic, founder, consanguinity, carrier-frequency, or geographic effect has been established. (fernandes2024acuteerythroidleukemia pages 1-2, fernandes2024acuteerythroidleukemia pages 2-4)

AEL is **not ordinarily inherited**; therefore penetrance, anticipation, carrier state, and germline mosaicism are not generally applicable. If constitutional TP53 or another predisposition syndrome is demonstrated, inheritance and counseling follow that syndrome rather than AEL itself.

## 10. Diagnostics

### Recommended workflow

1. **CBC, differential, reticulocytes, blood smear:** define anemia, thrombocytopenia, neutropenia, and circulating abnormal erythroblasts; add coagulation, CMP, LDH, uric acid, bilirubin, haptoglobin, type-and-screen, viral serologies, and infection cultures as clinically indicated.
2. **Bone-marrow aspirate and core biopsy:** quantify total erythroid precursors and proerythroblasts; assess dyserythropoiesis, fibrosis, and nonerythroid blasts. A dry or hemodilute aspirate makes the core and immunohistochemistry especially important.
3. **Flow cytometry/IHC:** immature erythroid cells are typically strongly **CD71** positive and may express E-cadherin, CD36, CD68, Gerbich antigen, dim glycophorin A/hemoglobin, and spectrin. They are generally MPO-, HLA-DR-, and CD33-negative. Early proerythroblasts can lack mature glycophorin A, so a negative single erythroid marker does not exclude AEL. (fernandes2024acuteerythroidleukemia pages 2-4)
4. **Cytogenetics:** conventional karyotype plus targeted FISH/CNV testing for chromosomes 5, 7, 8, 17p/TP53 and other suspected rearrangements.
5. **Molecular testing:** rapid myeloid NGS including TP53 with VAF and copy-number/LOH assessment; NPM1, FLT3, CEBPA, RUNX1, ASXL1, BCOR/BCORL1, DNMT3A, TET2, IDH1/2, NRAS/KRAS, JAK2, GATA2, and fusion-capable RNA sequencing. Determining **TP53 allelic state** is more informative than reporting mutation presence alone. (fernandes2024acuteerythroidleukemia pages 12-14, fernandes2024acuteerythroidleukemia pages 7-8)
6. **Germline assessment:** cultured skin fibroblast or another nonhematopoietic source when age/family history, variant pattern, or transplant planning raises hereditary-predisposition concern.

WES/WGS can identify unusual structural or noncoding lesions but does not replace rapid karyotype, FISH, RNA fusion testing, and clinically validated myeloid panels. Chromosomal microarray can refine copy-number/LOH, while mitochondrial and repeat-expansion testing have no routine role. Imaging is used for symptoms, infection, or organ involvement—not primary diagnosis. No population screening test exists.

### Differential diagnosis

Important alternatives are MDS with erythroid predominance, AML with myelodysplasia-related genetics, TP53-mutated AML without AEL morphology, NPM1-mutated AML with erythroid predominance, acute megakaryoblastic leukemia, acute undifferentiated leukemia, B-ALL, reactive erythroid hyperplasia after hemolysis/EPO therapy, megaloblastic anemia, parvovirus-related giant pronormoblasts, and metastatic nonhematopoietic malignancy. Integrated morphology, broad IHC/flow, cytogenetics, and sequencing are required because proerythroblasts may mimic lymphoblasts or megakaryoblasts. (fernandes2024acuteerythroidleukemia pages 12-14, ohan2024anunusualcase pages 3-4)

## 11. Outcome and prognosis

Recent-definition AEL has a typical median survival of **3–9 months**. A 41-patient TP53-mutated cohort had mean OS of approximately **3.3 months**. In an international pooled historical cohort of 217 patients, median OS was 11.1 months, PFS 7.1 months, and one-year survival 49%; this more favorable estimate likely reflects older definitions and selection. (fernandes2024acuteerythroidleukemia pages 1-2, fernandes2024acuteerythroidleukemia pages 10-11, fernandes2024acuteerythroidleukemia pages 8-10)

Age strongly modifies outcome. Historical registry data found median OS of 69 months and five-year survival of 55.01% among 50 treated children, versus median OS around five months among 918 adults. These pediatric figures should not be generalized to WHO-2022 TP53-driven adult AEL. (fernandes2024acuteerythroidleukemia pages 10-11)

Adverse factors include older age, multi-hit TP53, complex/monosomal karyotype, greater proerythroblast burden, therapy-related or antecedent-MDS disease, refractory disease, poor performance status, and inability to undergo allo-HCT. Transplant data are strongly selected but clinically important: one cohort reported median OS **89 months with HCT versus five months without HCT** (p=0.003). (fernandes2024acuteerythroidleukemia pages 11-12, fernandes2024acuteerythroidleukemia pages 10-11)

Major morbidity and mortality arise from progressive leukemia, infection/sepsis, bleeding, severe anemia, organ infiltration, treatment toxicity, relapse, and transplant complications. Validated AEL-specific patient-reported outcome or long-term disability datasets are lacking.

## 12. Treatment and current implementation

Treatment should occur at an AML/transplant center with pathology review because classification determines both risk and trial eligibility.

### Established approaches

* **Fit patient:** AML-style intensive induction, commonly cytarabine plus an anthracycline, followed by consolidation and rapid evaluation for allo-HCT. In a historical 122-patient analysis, intensive chemotherapy produced **72% overall response and 66% complete remission**; median OS was 10.5 months and one-year survival 46.7%. These results predate current definitions. (fernandes2024acuteerythroidleukemia pages 11-12, fernandes2024acuteerythroidleukemia pages 10-11)
* **Older/unfit patient:** azacitidine or decitabine, often following contemporary AML practice with venetoclax. In historical AEL cohorts, HMA therapy showed median OS around 13.7 months and first-line PFS 9.4 months versus 3.4 months when used later. However, erythroid/megakaryocytic differentiation can create BCL-XL rather than BCL2 dependence, potentially limiting venetoclax benefit. (fernandes2024acuteerythroidleukemia pages 11-12, fernandes2024acuteerythroidleukemia pages 10-11)
* **Allo-HCT:** only established potentially curative modality; pursue in remission when feasible, acknowledging high relapse and nonrelapse mortality. (fernandes2024acuteerythroidleukemia pages 1-2, fernandes2024acuteerythroidleukemia pages 11-12)
* **Genotype-directed AML drugs:** FLT3, IDH1, or IDH2 inhibitors are reasonable only when the corresponding actionable lesion is present; such variants are uncommon in prototypic AEL.
* **Supportive care:** irradiated/leukoreduced red-cell and platelet transfusions, antimicrobial treatment/prophylaxis according to neutropenia and regimen, tumor-lysis prevention, bleeding management, growth-factor use when appropriate, nutrition, palliative care, and transplant support.

Suggested NCIT concepts: Acute Myeloid Leukemia Chemotherapy, Cytarabine, Daunorubicin/Idarubicin, Azacitidine, Decitabine, Venetoclax, Allogeneic Hematopoietic Stem Cell Transplantation, Blood Product Transfusion, and Best Supportive Care; exact NCIT identifiers should be validated during curation.

### Experimental approaches

Preclinical vulnerabilities include EPOR/JAK2 inhibition with **ruxolitinib**, PARP inhibition with **talazoparib**, combined BCL-XL/JAK2 blockade, and CDK7/CDK9 inhibition. Larotrectinib prevented disease beyond 100 days in an NTRK1/TP53-comutant mouse transplant model, but this applies only to rare NTRK-driven disease. (fernandes2024acuteerythroidleukemia pages 4-5, fagnan2021molecularlandscapesand pages 7-8, fernandes2024acuteerythroidleukemia pages 12-14)

A phase-I decitabine–talazoparib study in 25 relapsed/refractory AML patients—not an AEL-specific cohort—reported 8% CR/CRi and 12% hematologic improvement. This is hypothesis-generating, not evidence of AEL efficacy. CAR-T, gene therapy, RNA therapy, and checkpoint blockade remain investigational without established AEL-specific benefit. (fernandes2024acuteerythroidleukemia pages 12-14)

**ClinicalTrials.gov:** **NCT02861651**, “Molecular Characterization of Acute Erythroid Leukemia (M6-AML) Using Targeted Next-generation Sequencing,” was a completed observational study with planned enrollment of 40. No contemporary randomized interventional trial dedicated specifically to WHO-2022 AEL was identified.

Surgery and radiotherapy have no routine leukemia-directed role. Pharmacogenomic dosing follows the drugs used rather than an AEL-specific rule.

## 13. Prevention

There is no vaccine, chemoprevention, newborn screen, carrier screen, or population-based AEL screening program. Primary prevention is limited to general reduction of benzene, tobacco smoke, unnecessary radiation, and avoidable leukemogenic exposure. Secondary prevention consists of monitoring individuals with MDS/MPN, therapy-related risk, unexplained cytopenias, or recognized germline predisposition; routine screening of asymptomatic average-risk people is unsupported. Tertiary prevention includes infection and bleeding prophylaxis, transfusion support, relapse/MRD surveillance where a trackable molecular marker exists, and transplant-related prophylaxis. Genetic counseling is appropriate only when constitutional predisposition is suspected or confirmed.

## 14. Other species and natural disease

No well-established, naturally occurring veterinary disease is recognized as a standardized homolog of human WHO-defined AEL. Sporadic erythroid leukemias can occur in animals, but breed-specific incidence, VBO mappings, and conserved initiating variants are not adequately established. There is no zoonotic potential or cross-species transmission. Comparative relevance derives mainly from induced **Mus musculus** models (NCBI Taxonomy **10090**), not natural disease.

## 15. Model organisms and experimental systems

Genetically engineered or transplant mouse models reproduce major features:

* **JAK2V617F + TP53 loss:** serially transplantable CD71+/Ter119− erythroid leukemia with anemia and hepatosplenomegaly.
* **ERG overexpression + mutant TP53:** fatal erythroleukemia within approximately 60 days after transplantation.
* **NFIA::ETO2 + TP53R248Q:** fully penetrant, transplantable disease with anemia, thrombocytopenia, hepatosplenomegaly, and circulating erythroid progenitors.
* **Biallelic CEBPA + GATA2 mutation:** erythroleukemia in about 40% of triple-transgenic mice, with erythroid-biased chromatin accessibility.
* **BCOR/DNMT3A or multiplex TP53/BCOR/DNMT3A lesions:** models epigenetic cooperation and provides platforms for PARP, CDK, and signaling-inhibitor testing. (fernandes2024acuteerythroidleukemia pages 7-8, fagnan2021molecularlandscapesand pages 7-8, fagnan2021molecularlandscapesand pages 6-7)

Cellular systems include murine SKT6 erythroleukemia cells, human AML/erythroid leukemia cell lines, primary patient cells, and xenografts. Their strengths are controlled causal testing and rapid drug evaluation. Limitations include engineered lesion combinations, murine erythroid markers and cytokine biology, incomplete human marrow/immune microenvironments, and failure to reproduce the full genomic complexity and age-related clonal evolution of human AEL.

## Curated ontology and knowledge-base mapping

The following compact table consolidates recommended disease, phenotype, anatomy, cell, pathway, gene, and intervention annotations. Entries marked for verification should be checked against the current ontology release before database ingestion.

| Domain | Recommended term/identifier | AEL evidence/meaning | Confidence or caveat |
|---|---|---|---|
| Disease ontology | Acute erythroid leukemia — MONDO:00017858 / MONDO_0017858 | Current disease-level identifier for AEL; useful anchor because classification has shifted between WHO and ICC systems (fernandes2024acuteerythroidleukemia pages 1-2, OpenTargets Search: acute erythroid leukemia) | High confidence for MONDO mapping; formatting may vary by source |
| Disease terminology | Acute erythroid leukemia (AEL) | Rare, aggressive AML subtype centered on marrow erythroid precursor predominance (fernandes2024acuteerythroidleukemia pages 1-2) | High confidence |
| Historical synonym | AML-M6 | Historical FAB terminology for acute erythroleukemia/erythroid leukemia (fernandes2024acuteerythroidleukemia pages 1-2) | High confidence; historical, not preferred current label |
| Historical synonym | Pure erythroid leukemia (PEL) | Historic subtype term; in current frameworks often absorbed differently, especially under TP53-mutated AML concepts in ICC (fernandes2024acuteerythroidleukemia pages 1-2, ohan2024anunusualcase pages 3-4) | High confidence; classification caveat important |
| Classification note | WHO 2022 AEL definition | WHO 2022 uses marrow morphology with ≥30% proerythroblasts and ≥80% erythroid precursors/cellularity (fernandes2024acuteerythroidleukemia pages 2-4, fernandes2024acuteerythroidleukemia pages 1-2) | High confidence |
| Classification note | ICC 2022: AML with mutated TP53 | ICC framework places many former PEL/AEL cases under AML with mutated TP53 when criteria are met (fernandes2024acuteerythroidleukemia pages 2-4, ohan2024anunusualcase pages 3-4) | High confidence; not identical to WHO morphology-based entity |
| HPO phenotype | Anemia — HP:0001903 | Common presentation; severe anemia is a hallmark laboratory/clinical abnormality in AEL (fernandes2024acuteerythroidleukemia pages 2-4) | High confidence |
| HPO phenotype | Thrombocytopenia — HP:0001873 | Common cytopenia in AEL and in experimental models recapitulating disease (fagnan2021molecularlandscapesand pages 7-8) | High confidence |
| HPO phenotype | Fever — HP:0001945 | Reported presenting symptom in clinical cohorts (fernandes2024acuteerythroidleukemia pages 2-4) | High confidence |
| HPO phenotype | Pallor — HP:0000980 | Reported clinical sign, usually secondary to profound anemia (fernandes2024acuteerythroidleukemia pages 2-4) | Moderate confidence; ID should be verified in implementation |
| HPO phenotype | Hepatosplenomegaly — term only, ID verification required | Reported in clinical cohorts and several mouse/transplant models (fernandes2024acuteerythroidleukemia pages 2-4, fagnan2021molecularlandscapesand pages 7-8, fagnan2021molecularlandscapesand pages 6-7) | Concept confident; exact HPO ID not asserted here |
| HPO phenotype | Pancytopenia — HP:0001876 | Can be present at diagnosis; reflects marrow failure from leukemic erythroid replacement | Moderate confidence; exact AEL citation indirect, ID should be verified locally |
| HPO phenotype | Hemolysis — term only, ID verification required | Evidence of hemolysis described in clinical presentation summaries (fernandes2024acuteerythroidleukemia pages 2-4) | Concept confident; exact HPO ID not asserted here |
| Cell ontology | Proerythroblast / erythroid progenitor — CL term, ID verification required | Central malignant population in WHO-defined AEL; CD71-high immature erythroid precursors dominate marrow (fernandes2024acuteerythroidleukemia pages 2-4) | Cell concept high confidence; precise CL mapping requires verification |
| Cell ontology | Hematopoietic stem/progenitor cell — CL term, ID verification required | Likely disease-propagating compartment in experimental systems; TP53-mutant HSPCs plus cooperating lesions can generate erythroleukemia (fernandes2024acuteerythroidleukemia pages 7-8, fagnan2021molecularlandscapesand pages 6-7) | Concept high confidence; exact CL ID verify |
| Anatomy | Bone marrow — UBERON:0002371 | Primary disease site; biopsy-based diagnosis and dominant erythroid hypercellularity (fernandes2024acuteerythroidleukemia pages 2-4, fernandes2024acuteerythroidleukemia pages 12-14) | High confidence |
| Anatomy | Blood — UBERON:0000178 | Peripheral blasts/cytopenias can support diagnosis and monitoring (fernandes2024acuteerythroidleukemia pages 2-4) | High confidence |
| Anatomy | Spleen — UBERON:0002106 | Splenomegaly/erythroid infiltration reported in patients and mouse models (fernandes2024acuteerythroidleukemia pages 2-4, fagnan2021molecularlandscapesand pages 6-7) | High confidence |
| Anatomy | Liver — UBERON:0002107 | Hepatomegaly or liver involvement may occur in aggressive erythroid disease/model systems (fernandes2024acuteerythroidleukemia pages 2-4, fagnan2021molecularlandscapesand pages 7-8) | High confidence |
| GO biological process | Erythrocyte differentiation — GO:0030218 | Core disrupted process; leukemic cells show erythroid lineage commitment with terminal maturation block (fernandes2024acuteerythroidleukemia pages 4-5, fagnan2021molecularlandscapesand pages 1-2) | High confidence |
| GO biological process | Cell proliferation — GO:0008283 | Unchecked expansion of immature erythroid progenitors is central to pathogenesis (fernandes2024acuteerythroidleukemia pages 1-2, fagnan2021molecularlandscapesand pages 1-2) | High confidence |
| GO biological process | Apoptotic signaling pathway — GO:0097190 | TP53 dysfunction alters apoptosis control and contributes to treatment resistance (fernandes2024acuteerythroidleukemia pages 7-8, fernandes2024acuteerythroidleukemia pages 1-2) | Moderate confidence; broad process mapping |
| GO biological process | JAK-STAT cascade / signaling — GO:0007259 | EPOR/JAK2/STAT signaling is recurrently implicated, especially in EPOR/JAK2-gain cases (fernandes2024acuteerythroidleukemia pages 4-5, fernandes2024acuteerythroidleukemia pages 12-14) | High confidence |
| GO biological process | Chromatin organization — GO:0006325 | BCOR/PRC1.1 and epigenetic regulator mutations support chromatin dysregulation in AEL biology (fernandes2024acuteerythroidleukemia pages 7-8, fernandes2024acuteerythroidleukemia pages 12-14) | High confidence |
| GO cellular component | Nucleus — GO:0005634 | Many driver lesions affect nuclear transcription/chromatin regulators (TP53, GATA factors, BCOR, DNMT3A, TET2) (fernandes2024acuteerythroidleukemia pages 7-8, fernandes2024acuteerythroidleukemia pages 12-14) | High confidence |
| GO cellular component | Chromatin — GO:0000785 | Relevant compartment for PRC1.1/BCOR and transcription factor dysregulation (fernandes2024acuteerythroidleukemia pages 7-8, fernandes2024acuteerythroidleukemia pages 12-14) | High confidence |
| Gene | TP53 | Dominant molecular hallmark; often biallelically inactivated and linked to complex karyotype, poor prognosis (fernandes2024acuteerythroidleukemia pages 7-8, fernandes2024acuteerythroidleukemia pages 1-2) | High confidence |
| Gene | EPOR | Upregulated/amplified in subset; supports erythroid growth signaling (fernandes2024acuteerythroidleukemia pages 4-5, fernandes2024acuteerythroidleukemia pages 12-14) | Moderate-high confidence |
| Gene | JAK2 | Recurrent signaling lesion; JAK2V617F and EPOR/JAK2 pathway activation implicated; preclinical ruxolitinib sensitivity reported (fernandes2024acuteerythroidleukemia pages 4-5, fagnan2021molecularlandscapesand pages 6-7, fernandes2024acuteerythroidleukemia pages 12-14) | High confidence |
| Gene | GATA1 | Master erythroid regulator; dysregulation contributes to failed maturation (fernandes2024acuteerythroidleukemia pages 4-5, fernandes2024acuteerythroidleukemia pages 1-2) | High confidence |
| Gene | CEBPA | Recurrent/cooperating transcription-factor alteration; with GATA2 can drive erythroid leukemia phenotypes in models (fernandes2024acuteerythroidleukemia pages 7-8, fagnan2021molecularlandscapesand pages 6-7) | Moderate-high confidence |
| Gene | GATA2 | Recurrent in exome studies and cooperating lesion in erythroid leukemogenesis (fernandes2024acuteerythroidleukemia pages 7-8, fagnan2021molecularlandscapesand pages 6-7) | Moderate-high confidence |
| Gene | BCOR | Epigenetic/chromatin regulator; cooperating driver in models and part of PRC1.1 dysfunction axis (fernandes2024acuteerythroidleukemia pages 12-14) | High confidence |
| Gene | DNMT3A | Recurrent epigenetic regulator mutation; cooperates with BCOR in mouse AEL models (fernandes2024acuteerythroidleukemia pages 7-8, fernandes2024acuteerythroidleukemia pages 12-14) | High confidence |
| Gene | TET2 | Recurrent epigenetic regulator mutation in clinical cohorts (fernandes2024acuteerythroidleukemia pages 7-8, fernandes2024acuteerythroidleukemia pages 8-10) | High confidence |
| Gene | ERG | Gain/upregulation cooperates with TP53-mutant HSPCs to induce erythroleukemia in mice (fernandes2024acuteerythroidleukemia pages 7-8, fernandes2024acuteerythroidleukemia pages 4-5) | Moderate-high confidence |
| Gene family | RAS pathway (KRAS, NRAS) | Recurrent cooperating signaling lesions; can combine with TP53 loss and impair erythroid differentiation (fernandes2024acuteerythroidleukemia pages 7-8, fernandes2024acuteerythroidleukemia pages 4-5) | High confidence for pathway-level mapping |
| NCIT intervention | Intensive AML chemotherapy — NCIT concept, ID verification required | Real-world AEL treatment backbone; retrospective cohorts show ORR/CR but short median OS (fernandes2024acuteerythroidleukemia pages 11-12, fernandes2024acuteerythroidleukemia pages 10-11) | Concept confident; exact NCIT code verify |
| NCIT intervention | Azacitidine — NCIT concept, ID verification required | Used as HMA frontline/low-intensity therapy; some cohorts suggest longer OS/PFS than expected historical controls (fernandes2024acuteerythroidleukemia pages 10-11, fernandes2024acuteerythroidleukemia pages 8-10) | Concept confident; AEL-specific evidence retrospective |
| NCIT intervention | Decitabine — NCIT concept, ID verification required | Used in AML/MDS-style therapy and in experimental combinations such as with talazoparib (fernandes2024acuteerythroidleukemia pages 12-14) | Concept confident; direct AEL-specific efficacy limited |
| NCIT intervention | Venetoclax — NCIT concept, ID verification required | Used by AML extrapolation; efficacy may be limited in erythroid/megakaryocytic states with BCL-XL dependence (fernandes2024acuteerythroidleukemia pages 11-12, fernandes2024acuteerythroidleukemia pages 16-18) | Moderate confidence; disease-specific resistance caveat important |
| NCIT intervention | Allogeneic hematopoietic stem cell transplantation — NCIT concept, ID verification required | Only potentially curative modality; major survival advantage in retrospective AEL cohorts (fernandes2024acuteerythroidleukemia pages 11-12, fernandes2024acuteerythroidleukemia pages 10-11) | High confidence for concept; selection bias caveat |
| NCIT intervention | Ruxolitinib — NCIT concept, ID verification required | Preclinical sensitivity in EPOR/JAK2-driven AEL models/xenografts (fernandes2024acuteerythroidleukemia pages 4-5, fernandes2024acuteerythroidleukemia pages 12-14) | Moderate confidence; investigational for AEL |
| NCIT intervention | Talazoparib — NCIT concept, ID verification required | PARP inhibitor with preclinical rationale in TP53-mutant AEL; early AML trial data not AEL-specific (fagnan2021molecularlandscapesand pages 7-8, fernandes2024acuteerythroidleukemia pages 12-14) | Moderate confidence; not established standard |
| NCIT intervention | Transfusion/supportive care — NCIT concept, ID verification required | Important because severe cytopenias, infection risk, and frailty are common; usually implemented as AML supportive management | High confidence for standard supportive role; direct AEL-specific trial data sparse |


*Table: This table maps acute erythroid leukemia to practical ontology, anatomy, cell-type, pathway, gene, phenotype, and intervention concepts for knowledge-base use. It highlights where current evidence is strong and where identifier verification is still needed because AEL classification and reporting remain heterogeneous.*

## Evidence appraisal and major gaps

The strongest conclusions are the current WHO morphologic definition, ICC TP53 framework, association with multi-hit TP53 and complex 5/7/17p cytogenetics, marrow-failure phenotype, extremely poor adult prognosis, and the potential curative role of allo-HCT. Less certain are exact incidence, mutation frequencies outside TP53, comparative efficacy of intensive chemotherapy versus HMA–venetoclax, and purported targeted dependencies. Most treatment statistics derive from historical “AML-M6/AEL” populations that do not map cleanly onto WHO-2022 disease. Priority research needs are prospective WHO/ICC-annotated registries, AEL-specific single-cell/multi-omic profiling, functional studies using primary human cells, and molecularly stratified trials addressing TP53, EPOR/JAK2, BCL-XL, chromatin, and DNA-repair vulnerabilities. (fernandes2024acuteerythroidleukemia pages 12-14, fernandes2024acuteerythroidleukemia pages 4-5)

References

1. (fernandes2024acuteerythroidleukemia pages 2-4): Priyanka Fernandes, Natalie Waldron, Theodora Chatzilygeroudi, Nour Sabiha Naji, and Theodoros Karantanos. Acute erythroid leukemia: from molecular biology to clinical outcomes. International Journal of Molecular Sciences, 25:6256, Jun 2024. URL: https://doi.org/10.3390/ijms25116256, doi:10.3390/ijms25116256. This article has 18 citations.

2. (fernandes2024acuteerythroidleukemia pages 1-2): Priyanka Fernandes, Natalie Waldron, Theodora Chatzilygeroudi, Nour Sabiha Naji, and Theodoros Karantanos. Acute erythroid leukemia: from molecular biology to clinical outcomes. International Journal of Molecular Sciences, 25:6256, Jun 2024. URL: https://doi.org/10.3390/ijms25116256, doi:10.3390/ijms25116256. This article has 18 citations.

3. (fernandes2024acuteerythroidleukemia pages 12-14): Priyanka Fernandes, Natalie Waldron, Theodora Chatzilygeroudi, Nour Sabiha Naji, and Theodoros Karantanos. Acute erythroid leukemia: from molecular biology to clinical outcomes. International Journal of Molecular Sciences, 25:6256, Jun 2024. URL: https://doi.org/10.3390/ijms25116256, doi:10.3390/ijms25116256. This article has 18 citations.

4. (fernandes2024acuteerythroidleukemia pages 11-12): Priyanka Fernandes, Natalie Waldron, Theodora Chatzilygeroudi, Nour Sabiha Naji, and Theodoros Karantanos. Acute erythroid leukemia: from molecular biology to clinical outcomes. International Journal of Molecular Sciences, 25:6256, Jun 2024. URL: https://doi.org/10.3390/ijms25116256, doi:10.3390/ijms25116256. This article has 18 citations.

5. (OpenTargets Search: acute erythroid leukemia): Open Targets Query (acute erythroid leukemia, 40 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (ohan2024anunusualcase pages 3-4): Hovsep Ohan, Juan Gomez-Gelvez, Yulei Shen, Sharmila Ghosh, John Carey, Kedar Inamdar, and Wei Liu. An unusual case of pure erythroid leukemia with normal karyotype and npm1 mutation. Journal of hematopathology, 17:163-166, Jul 2024. URL: https://doi.org/10.1007/s12308-024-00588-5, doi:10.1007/s12308-024-00588-5. This article has 0 citations.

7. (fernandes2024acuteerythroidleukemia pages 7-8): Priyanka Fernandes, Natalie Waldron, Theodora Chatzilygeroudi, Nour Sabiha Naji, and Theodoros Karantanos. Acute erythroid leukemia: from molecular biology to clinical outcomes. International Journal of Molecular Sciences, 25:6256, Jun 2024. URL: https://doi.org/10.3390/ijms25116256, doi:10.3390/ijms25116256. This article has 18 citations.

8. (fernandes2024acuteerythroidleukemia pages 4-5): Priyanka Fernandes, Natalie Waldron, Theodora Chatzilygeroudi, Nour Sabiha Naji, and Theodoros Karantanos. Acute erythroid leukemia: from molecular biology to clinical outcomes. International Journal of Molecular Sciences, 25:6256, Jun 2024. URL: https://doi.org/10.3390/ijms25116256, doi:10.3390/ijms25116256. This article has 18 citations.

9. (fagnan2021molecularlandscapesand pages 1-2): Alexandre Fagnan, Maria-Riera Piqué-Borràs, Samantha Tauchmann, Thomas Mercher, and Juerg Schwaller. Molecular landscapes and models of acute erythroleukemia. HemaSphere, 5:e558, Apr 2021. URL: https://doi.org/10.1097/hs9.0000000000000558, doi:10.1097/hs9.0000000000000558. This article has 14 citations and is from a peer-reviewed journal.

10. (fernandes2024acuteerythroidleukemia pages 8-10): Priyanka Fernandes, Natalie Waldron, Theodora Chatzilygeroudi, Nour Sabiha Naji, and Theodoros Karantanos. Acute erythroid leukemia: from molecular biology to clinical outcomes. International Journal of Molecular Sciences, 25:6256, Jun 2024. URL: https://doi.org/10.3390/ijms25116256, doi:10.3390/ijms25116256. This article has 18 citations.

11. (fagnan2021molecularlandscapesand pages 7-8): Alexandre Fagnan, Maria-Riera Piqué-Borràs, Samantha Tauchmann, Thomas Mercher, and Juerg Schwaller. Molecular landscapes and models of acute erythroleukemia. HemaSphere, 5:e558, Apr 2021. URL: https://doi.org/10.1097/hs9.0000000000000558, doi:10.1097/hs9.0000000000000558. This article has 14 citations and is from a peer-reviewed journal.

12. (fernandes2024acuteerythroidleukemia pages 16-18): Priyanka Fernandes, Natalie Waldron, Theodora Chatzilygeroudi, Nour Sabiha Naji, and Theodoros Karantanos. Acute erythroid leukemia: from molecular biology to clinical outcomes. International Journal of Molecular Sciences, 25:6256, Jun 2024. URL: https://doi.org/10.3390/ijms25116256, doi:10.3390/ijms25116256. This article has 18 citations.

13. (fagnan2021molecularlandscapesand pages 6-7): Alexandre Fagnan, Maria-Riera Piqué-Borràs, Samantha Tauchmann, Thomas Mercher, and Juerg Schwaller. Molecular landscapes and models of acute erythroleukemia. HemaSphere, 5:e558, Apr 2021. URL: https://doi.org/10.1097/hs9.0000000000000558, doi:10.1097/hs9.0000000000000558. This article has 14 citations and is from a peer-reviewed journal.

14. (fernandes2024acuteerythroidleukemia pages 10-11): Priyanka Fernandes, Natalie Waldron, Theodora Chatzilygeroudi, Nour Sabiha Naji, and Theodoros Karantanos. Acute erythroid leukemia: from molecular biology to clinical outcomes. International Journal of Molecular Sciences, 25:6256, Jun 2024. URL: https://doi.org/10.3390/ijms25116256, doi:10.3390/ijms25116256. This article has 18 citations.

## Artifacts

- [Edison artifact artifact-00](Acute_Erythroid_Leukemia-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.