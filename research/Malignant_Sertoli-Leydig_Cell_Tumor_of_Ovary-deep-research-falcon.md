---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-20T15:38:50.901547'
end_time: '2026-08-20T15:49:22.930180'
duration_seconds: 632.03
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Malignant Sertoli-Leydig Cell Tumor of Ovary
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 35
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 5
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Malignant_Sertoli-Leydig_Cell_Tumor_of_Ovary-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Malignant Sertoli-Leydig Cell Tumor of Ovary
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Malignant Sertoli-Leydig Cell Tumor of Ovary** covering all of the
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
- **Disease Name:** Malignant Sertoli-Leydig Cell Tumor of Ovary
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Malignant Sertoli-Leydig Cell Tumor of Ovary** covering all of the
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


# Malignant Sertoli–Leydig Cell Tumor of the Ovary: Research Report

## Executive summary

Ovarian Sertoli–Leydig cell tumor (SLCT) is a rare sex cord–stromal neoplasm composed of cells showing Sertoli-like and Leydig-like differentiation. “Malignant SLCT” is not a wholly separate molecular entity: malignant potential varies principally with FIGO stage, degree of differentiation, retiform or heterologous components, and recurrence. The disease disproportionately affects adolescents and young adults and may present with an adnexal mass, abdominal pain, or androgen excess/virilization.

The dominant contemporary finding is the close relationship between moderately and poorly differentiated SLCT and **DICER1**. In a centrally reviewed international registry cohort, 36/37 sequenced SLCTs had a DICER1 RNase IIIb hotspot mutation; germline loss-of-function, mosaic, and tumor-limited alterations were all observed. This supports expert pathology review, paired tumor–germline testing, genetic counseling, and DICER1-family surveillance as central elements of care. Early-stage disease usually has an excellent outcome after fertility-sparing surgery, whereas advanced stage, poor differentiation, and recurrence confer substantially greater mortality. Evidence for systemic therapy remains extrapolated from pooled ovarian sex cord–stromal tumor studies rather than SLCT-specific randomized trials. (schultz2017dicer1relatedsertolileydigcell pages 5-7, schultz2017dicer1relatedsertolileydigcell pages 7-8, NCT01042522 chunk 1)

The following table provides compact knowledge-base annotations; uncertain ontology mappings are deliberately marked for curator validation.

| Domain | Key finding | Suggested ontology identifiers/terms | Evidence/qualification |
|---|---|---|---|
| Disease class | Rare ovarian sex cord-stromal tumor; malignant behavior is variable and linked to stage/differentiation. Likely maps to an ovarian Sertoli-Leydig cell tumor concept rather than a uniquely curated MONDO term for the malignant subset. | MONDO: curator validation needed; MeSH: Sertoli-Leydig Cell Tumor; NCIT: ovarian sex cord-stromal tumor / Sertoli-Leydig cell tumor concepts, curator validation needed | Registry-based cohort and reviews describe SLCT as an ovarian sex cord-stromal neoplasm, often in adolescents/young adults; exact MONDO term for the malignant ovarian subset was not confirmed from available context. (schultz2017dicer1relatedsertolileydigcell pages 1-3, schultz2017dicer1relatedsertolileydigcell pages 5-7) |
| Epidemiology | Very rare; occurs primarily in adolescents and young adult females. In the international registry, median age at diagnosis was 17 years (range 2–61). | HPO onset term suggestion: Juvenile onset / Adolescent onset / Young adult onset, curator validation needed | Best available cohort in context: 49 SLCTs with median age 17 years; disease-level population incidence remains sparse in available evidence. (schultz2017dicer1relatedsertolileydigcell pages 5-7, schultz2017dicer1relatedsertolileydigcell pages 12-13) |
| Phenotype | Abdominal/pelvic mass or pain at presentation is common for ovarian tumors, although exact frequency for this cohort was not captured in available excerpts. | HPO: Abdominal pain [HP:0002027]; Pelvic pain [HP:0012532]; Abdominal mass [HP:0012745] | Include as common ovarian tumor presentation, but frequency should be curator-confirmed from full-text clinical series. (schultz2017dicer1relatedsertolileydigcell pages 1-3) |
| Phenotype | Virilization/androgen excess is a characteristic presentation in a subset of SLCTs. | HPO: Virilization [HP:0000138]; Hyperandrogenism [curator validation needed] | Registry and pathology literature note hormonal symptoms as common; androgenic effects are a recognized feature of DICER1-mutant SLCT. (schultz2017dicer1relatedsertolileydigcell pages 5-7, schultz2017dicer1relatedsertolileydigcell pages 1-3) |
| Phenotype | Hirsutism may occur as part of androgen excess. | HPO: Hirsutism [HP:0001007] | Supported as a clinically plausible androgen-excess manifestation; exact frequency not available in current context. (schultz2017dicer1relatedsertolileydigcell pages 5-7) |
| Phenotype | Amenorrhea or irregular menstruation may occur due to androgen secretion. | HPO: Amenorrhea [HP:0000141]; Irregular menstruation [HP:0000858] | Commonly reported in SLCT case literature, but exact cohort frequency was not available in retrieved evidence excerpts. (schultz2017dicer1relatedsertolileydigcell pages 5-7) |
| Phenotype | Elevated testosterone can be a laboratory abnormality reflecting steroidogenic tumor activity. | HPO: Elevated circulating testosterone level [curator validation needed] | Use as a lab phenotype; available context supports hormone-related symptoms rather than exact hormone distributions. (schultz2017dicer1relatedsertolileydigcell pages 5-7, schultz2017dicer1relatedsertolileydigcell pages 1-3) |
| Phenotype | Precocious puberty is relevant particularly in pediatric cases with hormone-secreting tumors. | HPO: Precocious puberty [HP:0000826] | Applicable mainly to children; age range in registry extended to 2 years, supporting pediatric relevance. (schultz2017dicer1relatedsertolileydigcell pages 12-13) |
| Anatomy | Primary site is the ovary, arising from ovarian sex cord/stromal elements. | UBERON: ovary [UBERON:0000992]; ovarian stroma / sex cord-stromal tissue: curator validation needed | Disease is consistently classified as ovarian sex cord-stromal. (schultz2017dicer1relatedsertolileydigcell pages 1-3, schultz2017dicer1relatedsertolileydigcell pages 3-5) |
| Cell type | Tumor shows Sertoli-like and Leydig-like differentiation; exact Cell Ontology mappings may require curator review. | CL: Sertoli cell [curator validation for ovarian Sertoli-like tumor cell]; Leydig cell [curator validation for ovarian steroidogenic/Leydig-like tumor cell] | Histopathologic definition is based on Sertoli-Leydig differentiation, but exact neoplastic ovarian counterparts may not have direct CL terms. (schultz2017dicer1relatedsertolileydigcell pages 5-7) |
| Genetics | DICER1 is the major disease gene. Germline pathogenic loss-of-function variants predispose, often with a second somatic RNase IIIb hotspot mutation in tumor. | HGNC: DICER1 [HGNC:17098]; NCBI Gene: DICER1; cytoband 14q32.13 | Central mechanistic theme across SLCT cohorts and DICER1 syndrome literature. (schultz2017dicer1relatedsertolileydigcell pages 7-8, schultz2017dicer1relatedsertolileydigcell pages 5-7, cazzato2024dicer1tumorsyndrome pages 1-2) |
| Genetics | In the registry, 97% (36/37) of sequenced SLCTs carried DICER1 RNase IIIb hotspot mutations; 22 had germline LOF, 3 mosaic, and 11 tumor-limited mutations. | Sequence ontology terms: loss_of_function_variant, missense_variant, splice_region_variant; ACMG classes: pathogenic/likely pathogenic where curated | Strong primary cohort evidence for two-hit DICER1 architecture. (schultz2017dicer1relatedsertolileydigcell pages 5-7) |
| Genetics | Intronic germline DICER1 variants can be missed by conventional exon-focused testing; splicing analysis may be required. | DICER1 intronic/splicing variant testing; RNA/splice assay concepts, curator validation needed | 2023 report identified novel intronic variants interfering with normal splicing and recommended intron sequencing when clinical suspicion remains high. (fraire2023intronicgermlinedicer1 pages 1-2) |
| Mechanism | Upstream mechanism: DICER1 dysfunction alters pre-miRNA cleavage, especially 5p miRNA processing, leading to abnormal post-transcriptional gene regulation. | GO: pre-miRNA processing [GO:0031053]; gene silencing by miRNA [GO:0035195]; miRNA-mediated gene silencing [curator validation if separate term needed] | DICER1 encodes an RNase III endonuclease; RNase IIIb hotspot mutations disrupt miRNA processing and alter mRNA expression. (schultz2017dicer1relatedsertolileydigcell pages 1-3, schultz2017dicer1relatedsertolileydigcell pages 7-8) |
| Mechanism | Downstream consequence: dysregulated growth/signaling and lineage-specific tumorigenesis; DICER1-mutant and wild-type tumors show different mRNA expression profiles. | GO: regulation of cell proliferation [GO:0042127]; cell population proliferation [GO:0008283] | Molecular profiling supports biologic heterogeneity by DICER1 status and differentiation. (nemejcova2025amolecularand pages 11-12) |
| Mechanism | Endocrine phenotype likely reflects androgen biosynthesis by Leydig-like steroidogenic cells. | GO: androgen biosynthetic process [GO:0006703] | Functional link is clinically inferred from virilization/hyperandrogenic presentations; direct pathway assays were not available in current context. (schultz2017dicer1relatedsertolileydigcell pages 5-7) |
| Pathology/IHC | Diagnostic sex cord-stromal markers include SF1, inhibin A, calretinin, CD99, FOXL2, AR/ER/PR; morphology remains the gold standard. | NCIT/IHC terms: Steroidogenic factor 1, inhibin A, calretinin, FOXL2; exact NCIT IDs curator validation needed | 2025 molecular/IHC study found high expression of sex cord markers; broader gynecologic pathology review supports IHC adjunctive use. (nemejcova2025amolecularand pages 11-12) |
| Molecular pathology | Well-differentiated SLCT may be biologically distinct from moderately/poorly differentiated tumors; DICER1 mutations are characteristic of moderate/poor differentiation, FOXL2 mutations are uncommon and mutually exclusive in one recent study. | DICER1-mutant SLCT; FOXL2-mutant SLCT, curator validation needed | Recent profiling suggests subtype heterogeneity, but this evidence is from 2025 and should be integrated cautiously into current curation. (nemejcova2025amolecularand pages 11-12) |
| Diagnostic workflow | Recommended evaluation includes expert gynecologic pathology review, immunohistochemistry, tumor/germline DICER1 testing, and consideration of intronic sequencing/splicing analysis if exon testing is negative despite high suspicion. | NCIT: immunohistochemistry; molecular genetic testing; next-generation sequencing; RNA splicing analysis, curator validation needed | Central pathology review improved diagnostic concordance; DICER1 testing has familial implications. (schultz2017dicer1relatedsertolileydigcell pages 7-8, fraire2023intronicgermlinedicer1 pages 1-2) |
| Natural history | About 50% of registry cases were stage IA; all stage IA patients were free of disease at median 19-month follow-up in the 2017 cohort excerpt. | FIGO stage IA; HPO/NCIT stage terms as applicable | Early-stage disease has favorable outcomes with surgery-focused management. (schultz2017dicer1relatedsertolileydigcell pages 5-7) |
| Prognosis | Recurrence occurred in 16.3% (8/49); among recurrent cases, 50% died, with median death at 35.5 months. Poor differentiation and tumor-limited DICER1 mutation status were adverse features. | NCIT: disease recurrence; overall survival; recurrence-free survival | Best direct prognostic evidence in available context comes from the international registry. (schultz2017dicer1relatedsertolileydigcell pages 5-7, schultz2017dicer1relatedsertolileydigcell pages 7-8) |
| Prognosis | Predisposing germline/mosaic DICER1 variants were associated with better overall and recurrence-free survival than tumor-limited mutations. | NCIT: germline mutation, mosaicism, somatic mutation | Prognostic association requires cautious interpretation because of small numbers but is repeatedly emphasized in the registry evidence. (schultz2017dicer1relatedsertolileydigcell pages 7-8, schultz2017dicer1relatedsertolileydigcell pages 5-7) |
| Surgery | Fertility-sparing surgery is standard real-world management for many unilateral stage I tumors; unilateral salpingo-oophorectomy is commonly used. | NCIT: Unilateral salpingo-oophorectomy; Fertility-sparing surgery | Registry data show most stage IA cases treated with surgery alone; exact operative distributions require full-text confirmation. (schultz2017dicer1relatedsertolileydigcell pages 3-5) |
| Systemic therapy | BEP (bleomycin, etoposide, cisplatin) is a commonly used regimen, especially for advanced, recurrent, or poorly differentiated disease. | NCIT: Bleomycin; Etoposide; Cisplatin; BEP regimen | In the registry, BEP/cisplatin-etoposide-bleomycin was the most common chemotherapy regimen. (schultz2017dicer1relatedsertolileydigcell pages 3-5) |
| Systemic therapy | Carboplatin plus paclitaxel is an actively studied alternative regimen for advanced/recurrent sex cord-stromal tumors. | NCIT: Carboplatin; Paclitaxel | Phase II randomized GOG-0264 compares paclitaxel/carboplatin versus BEP in advanced or recurrent sex cord-stromal tumors including SLCT. (NCT01042522 chunk 1, NCT01042522 chunk 7) |
| Targeted/antiangiogenic therapy | Bevacizumab has been studied in recurrent ovarian sex cord-stromal tumors, including SLCT-relevant populations. | NCIT: Bevacizumab | Completed Phase II NCI study enrolled recurrent ovarian sex cord-stromal tumors; applicability to SLCT is indirect because histologies were pooled. (NCT00748657 chunk 1) |
| Prevention / surveillance | There is no established primary prevention for SLCT itself. In DICER1 syndrome, cascade testing and surveillance are important; pelvic ultrasound is used in surveillance frameworks. | NCIT: Genetic counseling; Cascade testing; Pelvic ultrasound | Surveillance is relevant mainly for DICER1 carriers and families rather than the general population. (cazzato2024dicer1tumorsyndrome pages 7-8, schultz2017dicer1relatedsertolileydigcell pages 12-13) |
| Inheritance | For DICER1-related predisposition, inheritance is autosomal dominant with reduced/incomplete penetrance. | MONDO/NCIT: DICER1 syndrome; autosomal dominant inheritance [curator validation needed] | Applies to the hereditary predisposition syndrome, not to every SLCT case because some are tumor-limited. (cazzato2024dicer1tumorsyndrome pages 1-2, cazzato2024dicer1tumorsyndrome pages 8-10) |
| Other species / models | Mouse evidence suggests biallelic Dicer1 alterations can drive lineage-specific gynecologic tract tumors, but SLCT-specific model details were not available in full in current context. | MGI/NCBI model annotations: curator validation needed | Mention as emerging mechanistic support only; not enough detail in available context for robust annotation. (nemejcova2025amolecularand pages 11-12) |
| Evidence gaps | Limited disease-specific randomized therapy evidence; incomplete population incidence/prevalence data; uncertain exact ontology mappings for malignant subset and ovarian Sertoli-/Leydig-like neoplastic cells; sparse epigenomic/proteomic/metabolomic evidence in available context. | Curator validation needed across MONDO, CL, some HPO lab terms, and NCIT procedure/drug IDs | Important to annotate uncertainty explicitly to avoid overclaiming in the knowledge base. (schultz2017dicer1relatedsertolileydigcell pages 5-7, nemejcova2025amolecularand pages 11-12, NCT00748657 chunk 1, NCT01042522 chunk 1) |


*Table: This table summarizes high-value knowledge-base annotations for malignant ovarian Sertoli-Leydig cell tumor, including ontology suggestions, core genetic and mechanistic findings, and clinically relevant evidence with uncertainty flags for curator review.*

## 1. Disease information

### Definition and category

SLCT is an **ovarian sex cord–stromal tumor** with variable proportions of Sertoli-type tubules/cords and steroidogenic Leydig-like cells. Tumors are conventionally classified as well, moderately/intermediately, or poorly differentiated, with recognition of retiform patterns and heterologous elements. The “malignant” designation is most clinically meaningful for moderately or poorly differentiated, extraovarian, recurrent, or otherwise aggressive tumors rather than all histologically diagnosed SLCTs.

**Category:** rare malignant ovarian neoplasm; non-epithelial ovarian cancer; sex cord–stromal tumor; endocrine-active tumor in a subset.

### Identifiers and synonyms

* **Preferred name:** ovarian Sertoli–Leydig cell tumor.
* **Synonyms:** Sertoli–Leydig tumor; Sertoli–Leydig cell tumour; androblastoma; arrhenoblastoma; ovarian androblastoma; mixed Sertoli–Leydig cell tumor. The older terms *arrhenoblastoma* and *androblastoma* should be retained as synonyms but not preferred labels.
* **MONDO:** a distinct, verified MONDO identifier specifically for the *malignant ovarian* subset was not established by the retrieved resources; map provisionally to the broader ovarian SLCT concept and validate against the current MONDO release.
* **MeSH:** *Sertoli-Leydig Cell Tumor*.
* **ICD-10-CM:** histology is not represented adequately by a unique code; malignant ovarian disease is generally site-coded under **C56.-**, with laterality-specific subcodes where used.
* **ICD-11:** use the malignant neoplasm of ovary site category with morphology captured separately in a cancer-registry/ICD-O field.
* **ICD-O-3:** morphology and behavior should be checked against the current WHO/IARC release rather than inferred from the site code.
* **OMIM/Orphanet:** DICER1 tumor-predisposition syndrome has disease-level entries, but SLCT itself is primarily represented in tumor/pathology ontologies rather than as a classic Mendelian disorder.

The evidence summarized here is **aggregated disease-level evidence** from registries, cohorts, reviews, pathology studies, and ClinicalTrials.gov—not individual EHR data. The principal human cohort enrolled 107 ovarian sex cord–stromal tumor participants and included 49 SLCTs with central pathology review. (schultz2017dicer1relatedsertolileydigcell pages 5-7, schultz2017dicer1relatedsertolileydigcell pages 1-3, schultz2017dicer1relatedsertolileydigcell pages 3-5)

## 2. Etiology, risk, and protective factors

### Causal factors

The best-established causal mechanism is **DICER1-driven tumorigenesis**. DICER1 syndrome is an autosomal-dominant, incompletely penetrant cancer-predisposition disorder caused by germline DICER1 pathogenic variants at 14q32.13. In associated SLCT, tumorigenesis usually follows an unusual two-hit pattern: one allele carries a loss-of-function alteration and the other a somatic missense hotspot alteration in the RNase IIIb domain. Tumor-limited biallelic disease and mosaicism also occur. (schultz2017dicer1relatedsertolileydigcell pages 7-8, schultz2017dicer1relatedsertolileydigcell pages 5-7, cazzato2024dicer1tumorsyndrome pages 1-2)

In the international registry, DICER1 RNase IIIb hotspot mutations were found in **36/37 tumors (97%)**; among these cases, 22 patients had germline loss-of-function variants, three were mosaic, and 11 had tumor-limited alterations. This very high estimate reflects central pathology review and enrichment for correctly classified moderately/poorly differentiated tumors; lower frequencies in unselected series may partly reflect inclusion of well-differentiated or misclassified lesions. (schultz2017dicer1relatedsertolileydigcell pages 5-7, schultz2017dicer1relatedsertolileydigcell pages 7-8)

### Genetic risk factors

* A germline pathogenic/likely pathogenic DICER1 loss-of-function variant is the principal inherited risk factor.
* Family history may include pleuropulmonary blastoma, thyroid nodular disease or carcinoma, cystic nephroma, renal tumors, nasal chondromesenchymal hamartoma, embryonal rhabdomyosarcoma, or ovarian SLCT.
* In the registry, 33% of SLCT/gynandroblastoma patients reported thyroid nodules and 11% thyroid carcinoma, although ascertainment and referral bias should be considered. (schultz2017dicer1relatedsertolileydigcell pages 5-7)
* Deep intronic splice-altering variants can escape routine exon-directed sequencing. A 2023 report described two patients in whom extended analysis identified novel intronic DICER1 variants after conventional testing was unrevealing. The authors’ abstract recommendation was: **“when no DICER1 pLOF variants or large deletions are discovered in exonic regions despite strong clinical suspicion, intron sequencing and splicing analysis should be performed.”** [Fraire et al., September 2023; DOI: https://doi.org/10.1200/PO.23.00189]. (fraire2023intronicgermlinedicer1 pages 1-2)

### Environmental, lifestyle, infectious, and protective factors

No reproducible toxin, radiation, occupation, infection, smoking, alcohol, dietary, obesity, reproductive, or medication exposure has been established as an SLCT-specific cause. Risk factors for common epithelial ovarian cancer should not be transferred to SLCT without evidence. Likewise, no genetic protective allele, diet, lifestyle intervention, vaccine, or chemopreventive agent is known to prevent SLCT. No established gene–environment interaction has been demonstrated. These are genuine evidence gaps, not evidence of absence.

## 3. Phenotypes

### Typical clinical manifestations

* **Pelvic/abdominal mass, distension, or pain:** mass-effect symptoms can be acute or subacute; torsion and rupture are uncommon but clinically important complications. Suggested HPO: Abdominal pain (**HP:0002027**), Pelvic pain (**HP:0012532**), Abdominal mass (**HP:0012745**).
* **Androgen excess:** elevated testosterone may cause hirsutism, acne, deepened voice, clitoromegaly, increased muscle mass, temporal hair recession, or other virilization. Suggested HPO: Virilization (**HP:0000138**), Hirsutism (**HP:0001007**), Abnormal circulating testosterone level—exact current HPO child term should be verified.
* **Menstrual/reproductive abnormalities:** oligomenorrhea, irregular menses, secondary amenorrhea, or anovulation. Suggested HPO: Amenorrhea (**HP:0000141**) and Irregular menstruation (**HP:0000858**).
* **Pediatric endocrine manifestations:** precocious puberty can occur in hormone-secreting tumors; HPO: Precocious puberty (**HP:0000826**).
* **Laboratory abnormalities:** testosterone and androstenedione may be elevated; AFP can rise when hepatocytic or other heterologous differentiation is present, but AFP is not a universal SLCT marker. Inhibin A/B and anti-Müllerian hormone can be informative in some sex cord–stromal tumors but lack SLCT-specific sensitivity sufficient for exclusion.

Hormonal symptoms were common in the international cohort, but the retrieved evidence did not provide reliable manifestation-specific percentages. Median diagnosis age was **17 years (range 2–61)**, illustrating pediatric through adult presentation but strong adolescent/young-adult concentration. (schultz2017dicer1relatedsertolileydigcell pages 5-7, schultz2017dicer1relatedsertolileydigcell pages 12-13)

### Severity, progression, and quality of life

Severity is variable. Localized tumors may be cured surgically, and endocrine manifestations can improve after resection. Advanced or recurrent disease can cause pain, bowel or urinary compression, endocrine changes, infertility, treatment toxicity, and death. Virilizing changes such as hirsutism and menstrual dysfunction may improve, whereas voice deepening or clitoromegaly may be incompletely reversible. No validated SLCT-specific EQ-5D, SF-36, or PROMIS dataset was identified.

## 4. Genetic and molecular information

### Principal gene and variant architecture

**DICER1** (HGNC:17098; chromosome 14q32.13) encodes a cytoplasmic RNase III endonuclease required for precursor-miRNA processing. Relevant variants include:

1. **Germline or mosaic first hits:** nonsense, frameshift, canonical splice-site, exon-level or larger deletion, and less commonly pathogenic missense variants, generally causing loss of function.
2. **Somatic second hits:** recurrent missense substitutions in metal-binding residues of the RNase IIIb domain. These impair processing of the 5p miRNA arm rather than simply eliminating all DICER1 activity.
3. **Tumor-limited biallelic alterations:** both alterations can be detectable only in neoplastic tissue.
4. **Deep intronic splice variants:** the 2023 study reported c.1752+213A>G and c.1509+16A>G in the transcript used by the authors; nomenclature must be normalized to the clinically reported transcript before database ingestion. (schultz2017dicer1relatedsertolileydigcell pages 7-8, fraire2023intronicgermlinedicer1 pages 1-2)

Population allele frequencies are variant-specific. A pathogenic germline loss-of-function variant is expected to be rare in gnomAD; no single founder variant or carrier frequency explains most SLCTs. Each variant should therefore be annotated directly from ClinVar/gnomAD using genome build and transcript-specific nomenclature rather than assigning one disease-wide frequency.

### Other genes and molecular classes

**FOXL2** mutation is uncommon in authentic SLCT and helps distinguish SLCT from adult granulosa-cell tumor, in which FOXL2 p.Cys134Trp is characteristic. A recent 37-case molecular/IHC study found DICER1 mutations in 54.5%, FOXL2 mutations in 6%, two TERT-promoter-mutant tumors, and mutually exclusive DICER1 and FOXL2 alterations in that series. DICER1-mutant tumors overexpressed CDK6, NOTCH2, and FGFR2, whereas DICER1-wild-type tumors showed increased PRKCA, HNF1A, LDLR, and MAP2K5 expression. These findings are hypothesis-generating and do not yet define validated therapeutic biomarkers. [Němejcová et al.; DOI online in 2024, journal issue November 2025: https://doi.org/10.1007/s00428-024-03984-5]. (nemejcova2025amolecularand pages 11-12)

No reproducible modifier gene, constitutional chromosomal abnormality, founder effect, epigenetic signature, or prognostic methylation classifier is established. Comprehensive copy-number, proteomic, metabolomic, and lipidomic datasets remain sparse.

## 5. Environmental information

No infectious agent causes SLCT, and the disease is not transmissible or zoonotic. There is no evidence supporting HPV, other viruses, pelvic inflammatory disease, endocrine-disrupting chemicals, occupational exposures, diet, alcohol, or tobacco as disease-specific triggers. The environmental component of DICER1 penetrance is currently poorly understood.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Predisposition/first hit:** constitutional or mosaic DICER1 loss of function—or an initial tumor-limited event—reduces normal DICER1 dosage.
2. **Lineage-specific second hit:** an ovarian sex cord–stromal progenitor acquires an RNase IIIb hotspot missense alteration.
3. **miRNA-processing bias:** abnormal cleavage depletes mature 5p miRNAs and distorts post-transcriptional repression.
4. **Transcriptomic dysregulation:** altered gene-expression programs affect differentiation, proliferation, and survival in Sertoli-/Leydig-like lineages.
5. **Tumor phenotype:** sex cord differentiation produces tubular/cord-like morphology, while Leydig-like steroidogenesis can generate androgen excess and virilization.
6. **Progression:** poor differentiation, sarcomatous or heterologous components, rupture, extraovarian spread, and treatment-resistant subclones contribute to recurrence and mortality. (schultz2017dicer1relatedsertolileydigcell pages 1-3, schultz2017dicer1relatedsertolileydigcell pages 7-8, nemejcova2025amolecularand pages 11-12)

Suggested GO terms include pre-miRNA processing (**GO:0031053**), gene silencing by miRNA (**GO:0035195**), regulation of cell-population proliferation (**GO:0042127**), cell population proliferation (**GO:0008283**), and androgen biosynthetic process (**GO:0006703**). Suggested cellular annotations are ovarian stromal/sex-cord progenitor, Sertoli-like tumor cell, and steroidogenic Leydig-like tumor cell; exact CL identifiers require validation because these neoplastic ovarian analogues may not map cleanly to normal testicular cell terms.

### Immune, metabolic, and multi-omic findings

The available evidence does not support a primary autoimmune or chronic-inflammatory pathogenesis. In the recent 37-case study, tumors were mismatch-repair proficient and HER2- and PD-L1-negative; CTLA4 staining occurred in 43%, but this is not a validated predictor of checkpoint-inhibitor benefit. Loss of PTEN expression occurred in 14%. No validated metabolomic or lipidomic signature exists. (nemejcova2025amolecularand pages 11-12)

## 7. Anatomical structures affected

The primary site is the **ovary** (UBERON:0000992), usually involving ovarian sex cord/stromal tissue. Tumors are generally unilateral at initial presentation; bilateral or metachronous contralateral tumors are uncommon but particularly relevant in germline DICER1 carriers. Three germline carriers in the registry developed metachronous SLCTs 5–14 years after the first diagnosis. (schultz2017dicer1relatedsertolileydigcell pages 7-8, schultz2017dicer1relatedsertolileydigcell pages 5-7)

Potential secondary sites include the contralateral ovary, peritoneum, omentum, pelvic/abdominal lymphatic regions, liver, and lung in advanced or recurrent disease. Subcellularly, the relevant compartment is primarily the cytoplasmic miRNA-processing machinery containing DICER1, with downstream effects on cytoplasmic mRNA regulation and nuclear transcriptional programs.

## 8. Temporal development and natural history

Onset is most often adolescent or young adult, but the observed range of 2–61 years precludes an absolute age boundary. Presentation may be acute with pain/torsion or insidious with progressive virilization, menstrual change, or abdominal enlargement. (schultz2017dicer1relatedsertolileydigcell pages 5-7)

Approximately half of the 49-case registry cohort had stage IA disease. Recurrence occurred in **8/49 (16.3%)**. Among recurrent cases, half died of disease, with a reported median of 35.5 months in the fatal recurrent group. All stage IA patients were disease-free at a median follow-up of 19 months, although that follow-up is too short to exclude late events. (schultz2017dicer1relatedsertolileydigcell pages 5-7)

A distinction is essential between **recurrence** and a **metachronous new primary contralateral SLCT**, the latter being possible years later in DICER1 carriers. Accordingly, surveillance should not cease solely because the initial tumor was stage IA. (schultz2017dicer1relatedsertolileydigcell pages 7-8)

## 9. Inheritance and population

### Epidemiology

SLCT is very rare; robust population incidence and prevalence per 100,000 are not available from the retrieved evidence. It occurs only in patients with ovarian tissue and is concentrated in adolescents and young women. In pediatric/adolescent ovarian neoplasia, sex cord–stromal tumors constitute a minority, while SLCT is one of the important DICER1-associated entities. Registry estimates should not be treated as population incidence because of referral enrichment. (schultz2017dicer1relatedsertolileydigcell pages 1-3)

### Inheritance

DICER1 predisposition is **autosomal dominant with reduced, age-dependent, and tumor-specific penetrance** and variable expressivity. The germline variant is inherited by offspring with a 50% probability, but an SLCT itself is not inherited. De novo variants, postzygotic mosaicism, and tumor-only mutations occur. Genetic anticipation is not established. Consanguinity is not a recognized risk factor. (cazzato2024dicer1tumorsyndrome pages 7-8, cazzato2024dicer1tumorsyndrome pages 1-2)

In the registry, predisposition-associated cases presented at a median age of 16 versus 21 years for tumor-limited cases; 82% of those with predisposing variants were diagnosed before 21. No consistent ethnic or geographic enrichment, founder effect, or population-specific sex ratio beyond the requirement for ovarian tissue has been demonstrated. (schultz2017dicer1relatedsertolileydigcell pages 5-7)

## 10. Diagnostics

### Clinical and imaging evaluation

Evaluation should include history of tempo of virilization, menstrual development, abdominal symptoms, personal/family DICER1-spectrum tumors, and physical examination. Laboratory assessment commonly includes total and free testosterone, SHBG, androstenedione, DHEAS, 17-hydroxyprogesterone, β-hCG, AFP, LDH, and selected inhibin A/B or AMH measurements. Rapidly progressive virilization with high testosterone and relatively non-elevated DHEAS favors an ovarian rather than adrenal source, but no blood marker rules SLCT in or out.

Pelvic ultrasound is first-line, with MRI useful for characterization and surgical planning; CT chest/abdomen/pelvis is appropriate when malignancy or spread is suspected. Imaging is not histologically specific.

### Histopathology and immunohistochemistry

Diagnosis requires resection or biopsy review by a gynecologic pathologist. Morphology may show Sertoli-cell tubules, cords, nests, primitive gonadal stroma, Leydig-cell clusters, retiform architecture, and heterologous mucinous, cartilaginous, skeletal-muscle, or sarcomatous elements. In the 49-case registry, 47% had heterologous elements and 22% sarcomatous features. (schultz2017dicer1relatedsertolileydigcell pages 5-7)

Useful positive markers include **SF1, inhibin, calretinin, WT1, CD99, FOXL2, and androgen receptor**, interpreted as a panel. Cytokeratin may highlight Sertoli-type epithelial differentiation. No individual marker is completely specific, and morphology remains the diagnostic foundation. (nemejcova2025amolecularand pages 11-12)

Important differentials include juvenile and adult granulosa-cell tumor, steroid-cell tumor, gynandroblastoma, endometrioid carcinoma with sex cord-like areas, carcinoid/neuroendocrine tumor, yolk-sac tumor, immature teratoma, and metastatic endocrine neoplasms. DICER1 RNase IIIb testing supports moderately/poorly differentiated SLCT, whereas FOXL2 p.Cys134Trp favors adult granulosa-cell tumor.

### Genetic testing workflow

1. Test tumor tissue with an NGS panel that covers the DICER1 RNase IIIb domain and detects small variants, copy-number changes, and ideally both hits.
2. Perform germline DICER1 sequencing plus deletion/duplication analysis for every confirmed SLCT, preferably with genetic counseling.
3. If blood is negative but tumor findings or phenotype strongly suggest DICER1 syndrome, assess mosaicism using high-depth sequencing and consider another normal tissue.
4. If exon-focused testing is negative, consider whole-gene intronic sequencing and RNA/splicing analysis.
5. WES/WGS can be useful after targeted testing is unrevealing, but conventional WES may inadequately cover deep introns. CMA, karyotyping, FISH, mitochondrial sequencing, and repeat-expansion testing are not routine diagnostic tests. (schultz2017dicer1relatedsertolileydigcell pages 7-8, fraire2023intronicgermlinedicer1 pages 1-2)

No population screening program is justified. Testing is targeted to patients and relatives in DICER1 families.

## 11. Outcome and prognosis

Stage and histologic differentiation are the strongest established clinical variables. Poor differentiation and tumor-limited DICER1 mutations were adverse in the registry, whereas germline/mosaic predisposition-associated cases had better overall and recurrence-free survival. This molecular association may be confounded by age, stage, biology, and ascertainment and should not replace stage-based risk assessment. (schultz2017dicer1relatedsertolileydigcell pages 5-7, schultz2017dicer1relatedsertolileydigcell pages 7-8)

Five- and ten-year SLCT-specific survival estimates vary across small retrospective series and were not reliably extractable from the retrieved full texts. The most defensible quantitative findings are the registry’s 16.3% recurrence rate, universal disease-free status among stage IA cases at median 19 months, and 50% disease-specific mortality among the eight recurrent cases. (schultz2017dicer1relatedsertolileydigcell pages 5-7)

Adverse features include extraovarian stage, rupture, poor differentiation, retiform pattern, heterologous/sarcomatous elements, residual disease, and recurrence. Morbidity includes infertility or reduced ovarian reserve, virilization, surgical menopause after bilateral surgery, platinum-related neuropathy/nephrotoxicity/ototoxicity, etoposide-associated marrow toxicity and rare secondary leukemia, and bleomycin pulmonary toxicity.

## 12. Treatment and real-world implementation

### Surgery

For a unilateral, apparently stage I tumor in a young patient, the preferred real-world approach is fertility-sparing **unilateral salpingo-oophorectomy with careful surgical staging**, preservation of the normal contralateral ovary and uterus, and avoidance of tumor rupture. Routine biopsy of a grossly normal contralateral ovary is generally avoided because it can impair fertility. Completion surgery is individualized rather than automatic.

In the registry, **82% of stage IA patients received surgery alone**. This supports observation for completely resected stage IA well/moderately differentiated tumors after expert review. Poorly differentiated stage IA disease is more controversial and may receive adjuvant chemotherapy. (schultz2017dicer1relatedsertolileydigcell pages 3-5)

Suggested NCIT intervention concepts: unilateral salpingo-oophorectomy, fertility-sparing surgery, ovarian cancer staging surgery, tumor resection.

### Chemotherapy

For advanced, ruptured, incompletely resected, poorly differentiated, or recurrent disease, **BEP—bleomycin, etoposide, and cisplatin—is the most established regimen by precedent**. It was the most frequent chemotherapy in the registry, used in 12 SLCT cases. Toxicity and fertility risks require age-appropriate counseling and baseline pulmonary, renal, auditory, and reproductive assessment. (schultz2017dicer1relatedsertolileydigcell pages 3-5)

GOG-0264/NCT01042522 randomized 63 patients with advanced or recurrent chemotherapy-naïve ovarian sex cord–stromal tumors between paclitaxel/carboplatin for six 21-day courses and BEP for four courses. The primary endpoint was progression-free survival, with overall survival, response, toxicity, inhibin biomarkers, and tissue collection as secondary/tertiary objectives. Because histologies were pooled, any result is indirect for SLCT. ClinicalTrials.gov URL: https://clinicaltrials.gov/study/NCT01042522. (NCT01042522 chunk 1, NCT01042522 chunk 7)

Suggested NCIT terms: BEP regimen; bleomycin; etoposide; cisplatin; carboplatin; paclitaxel.

### Targeted therapy and immunotherapy

There is no FDA-approved DICER1-directed, gene, RNA, or cell therapy for SLCT. NCT00748657 was a completed phase II study of IV bevacizumab every 21 days in 36 patients with recurrent ovarian sex cord–stromal tumors, measuring RECIST response, progression-free survival, overall survival, and toxicity. Its relevance to SLCT is indirect because histologies were pooled. ClinicalTrials.gov URL: https://clinicaltrials.gov/study/NCT00748657. (NCT00748657 chunk 1)

The recent finding that tumors were MMR-proficient and PD-L1-negative provides little biomarker rationale for routine checkpoint inhibition. HER2 negativity likewise argues against unselected HER2 therapy. Transcriptomic FGFR2, CDK6, NOTCH2, or MAPK-pathway signals remain investigational. (nemejcova2025amolecularand pages 11-12)

### Supportive care and personalization

Care should include fertility preservation counseling, reproductive endocrinology referral when time permits, management of endocrine manifestations, psychosocial support, pulmonary/renal/auditory monitoring during BEP, menopausal care after bilateral oophorectomy, and genetic counseling. Personalized management is currently based primarily on stage, differentiation, residual disease, age/fertility goals, and germline DICER1 status—not a validated pharmacogenomic algorithm.

## 13. Prevention and surveillance

There is no established primary prevention or vaccine. General-population ovarian screening is not indicated.

For confirmed DICER1 carriers, prevention is primarily **secondary prevention through surveillance and cascade testing**. Contemporary DICER1 frameworks include age-adapted chest imaging in childhood, thyroid examination/ultrasound, renal surveillance in younger children, and periodic pelvic ultrasound for gynecologic tumors. Exact intervals should follow the current DICER1/PPB Registry or genetics-clinic guideline because schedules evolve and depend on age and prior tumors. A 2024 review emphasized pelvic ultrasound, thyroid evaluation, family testing, and multidisciplinary genetic counseling. [Cazzato et al., July 2024; DOI: https://doi.org/10.3390/jmp5030019]. (cazzato2024dicer1tumorsyndrome pages 7-8, cazzato2024dicer1tumorsyndrome pages 8-10)

Testing an affected woman can benefit relatives: in the international registry, cascade screening following SLCT-associated DICER1 findings led to detection of pleuropulmonary blastoma in three children at an early, highly curable stage. (schultz2017dicer1relatedsertolileydigcell pages 12-13)

Tertiary prevention includes complete initial resection without rupture, risk-adapted chemotherapy, long-term clinical and pelvic surveillance, prompt evaluation of recurrent endocrine symptoms, and monitoring for metachronous contralateral disease.

## 14. Other species and natural disease

Sex cord–stromal tumors with Sertoli- and Leydig-cell differentiation occur naturally in veterinary species, including domestic animals, but the retrieved evidence did not establish a naturally occurring nonhuman syndrome that reliably models human ovarian DICER1-associated SLCT. These tumors are not infectious and have no zoonotic potential.

Relevant orthologues include mouse **Dicer1** and corresponding vertebrate DICER1 orthologues. Exact NCBI Taxonomy, breed-ontology, and veterinary gene identifiers should be populated from live NCBI/OMIA/VBO records rather than inferred. Comparative pathology is potentially useful, but spontaneous animal SLCTs should not automatically be assumed to share the human DICER1 two-hit mechanism.

## 15. Model organisms and experimental systems

A 2023 genetically engineered mouse study reported that biallelic Dicer1 alterations in the gynecologic tract drove lineage-specific DICER1-syndrome-associated cancers, providing experimental support for the two-hit and lineage-context model. However, the retrieved material did not provide sufficient SLCT-specific details to quantify penetrance, latency, histologic fidelity, or treatment response. Thus, it should be annotated as mechanistic support rather than a fully validated therapeutic SLCT model. (nemejcova2025amolecularand pages 11-12)

Potential systems include conditional Dicer1 loss-of-function plus RNase IIIb hotspot knock-in mice, primary tumor cultures, patient-derived organoids, xenografts, and engineered ovarian stromal cells. Major limitations are the rarity of specimens, uncertain fidelity of normal ovarian Sertoli-/Leydig-like lineage assignment, and lack of broadly distributed, genomically authenticated SLCT cell lines. No robust disease-specific CRISPR dependency screen was identified.

## Evidence hierarchy, recent developments, and limitations

**Highest-value human clinical evidence:** the International Ovarian and Testicular Stromal Tumor Registry cohort, with central pathology review, paired genetic analysis, and outcome tracking. Its key abstract-level conclusion is reflected by the finding that DICER1 RNase IIIb mutations occurred in 36/37 sequenced SLCTs and that germline or mosaic variants occurred in more than half. [Schultz et al., December 2017; DOI: https://doi.org/10.1016/j.ygyno.2017.09.034]. (schultz2017dicer1relatedsertolileydigcell pages 12-13, schultz2017dicer1relatedsertolileydigcell pages 10-12)

**Important 2023–2024 development:** conventional exon-focused germline testing can miss pathogenic intronic DICER1 variants, supporting extended intronic sequencing and functional splice analysis in strongly suggestive cases. [Fraire et al., September 2023; DOI: https://doi.org/10.1200/PO.23.00189]. (fraire2023intronicgermlinedicer1 pages 1-2)

**Recent molecular development:** a contemporary 37-case analysis supports molecular separation of well-differentiated, frequently DICER1-wild-type tumors from DICER1-characteristic moderately/poorly differentiated disease and provides initial RNA-expression and predictive-marker data. Its abstract states: **“DICER1MUT and DICER1WT tumors showed different mRNA expression profiles.”** [DOI registered 2024; journal publication November 2025: https://doi.org/10.1007/s00428-024-03984-5]. (nemejcova2025amolecularand pages 11-12)

**Major limitations:** rarity, referral bias, changing histopathologic classification, small retrospective cohorts, heterogeneous chemotherapy, short follow-up in some early-stage series, and pooling of SLCT with granulosa and other sex cord–stromal tumors in trials. Many requested domains—population incidence, quantitative quality of life, environmental risk, epigenomics, metabolomics, pharmacogenomics, and validated targeted therapies—lack disease-specific evidence. PMIDs were not present in the retrieved records and therefore are not fabricated here; DOI and ClinicalTrials.gov URLs are supplied for authoritative record linkage.

References

1. (schultz2017dicer1relatedsertolileydigcell pages 5-7): Kris Ann P. Schultz, Anne K. Harris, Michael Finch, Louis P. Dehner, Jubilee B. Brown, David M. Gershenson, Robert H. Young, Amanda Field, Weiying Yu, Joyce Turner, Nicholas G. Cost, Dominik T. Schneider, Douglas R. Stewart, A. Lindsay Frazier, Yoav Messinger, and D. Ashley Hill. Dicer1-related sertoli-leydig cell tumor and gynandroblastoma: clinical and genetic findings from the international ovarian and testicular stromal tumor registry. Gynecologic oncology, 147 3:521-527, Dec 2017. URL: https://doi.org/10.1016/j.ygyno.2017.09.034, doi:10.1016/j.ygyno.2017.09.034. This article has 151 citations and is from a domain leading peer-reviewed journal.

2. (schultz2017dicer1relatedsertolileydigcell pages 7-8): Kris Ann P. Schultz, Anne K. Harris, Michael Finch, Louis P. Dehner, Jubilee B. Brown, David M. Gershenson, Robert H. Young, Amanda Field, Weiying Yu, Joyce Turner, Nicholas G. Cost, Dominik T. Schneider, Douglas R. Stewart, A. Lindsay Frazier, Yoav Messinger, and D. Ashley Hill. Dicer1-related sertoli-leydig cell tumor and gynandroblastoma: clinical and genetic findings from the international ovarian and testicular stromal tumor registry. Gynecologic oncology, 147 3:521-527, Dec 2017. URL: https://doi.org/10.1016/j.ygyno.2017.09.034, doi:10.1016/j.ygyno.2017.09.034. This article has 151 citations and is from a domain leading peer-reviewed journal.

3. (NCT01042522 chunk 1):  Paclitaxel and Carboplatin or Bleomycin Sulfate, Etoposide Phosphate, and Cisplatin in Treating Patients With Advanced or Recurrent Sex Cord-Ovarian Stromal Tumors. GOG Foundation. 2010. ClinicalTrials.gov Identifier: NCT01042522

4. (schultz2017dicer1relatedsertolileydigcell pages 1-3): Kris Ann P. Schultz, Anne K. Harris, Michael Finch, Louis P. Dehner, Jubilee B. Brown, David M. Gershenson, Robert H. Young, Amanda Field, Weiying Yu, Joyce Turner, Nicholas G. Cost, Dominik T. Schneider, Douglas R. Stewart, A. Lindsay Frazier, Yoav Messinger, and D. Ashley Hill. Dicer1-related sertoli-leydig cell tumor and gynandroblastoma: clinical and genetic findings from the international ovarian and testicular stromal tumor registry. Gynecologic oncology, 147 3:521-527, Dec 2017. URL: https://doi.org/10.1016/j.ygyno.2017.09.034, doi:10.1016/j.ygyno.2017.09.034. This article has 151 citations and is from a domain leading peer-reviewed journal.

5. (schultz2017dicer1relatedsertolileydigcell pages 12-13): Kris Ann P. Schultz, Anne K. Harris, Michael Finch, Louis P. Dehner, Jubilee B. Brown, David M. Gershenson, Robert H. Young, Amanda Field, Weiying Yu, Joyce Turner, Nicholas G. Cost, Dominik T. Schneider, Douglas R. Stewart, A. Lindsay Frazier, Yoav Messinger, and D. Ashley Hill. Dicer1-related sertoli-leydig cell tumor and gynandroblastoma: clinical and genetic findings from the international ovarian and testicular stromal tumor registry. Gynecologic oncology, 147 3:521-527, Dec 2017. URL: https://doi.org/10.1016/j.ygyno.2017.09.034, doi:10.1016/j.ygyno.2017.09.034. This article has 151 citations and is from a domain leading peer-reviewed journal.

6. (schultz2017dicer1relatedsertolileydigcell pages 3-5): Kris Ann P. Schultz, Anne K. Harris, Michael Finch, Louis P. Dehner, Jubilee B. Brown, David M. Gershenson, Robert H. Young, Amanda Field, Weiying Yu, Joyce Turner, Nicholas G. Cost, Dominik T. Schneider, Douglas R. Stewart, A. Lindsay Frazier, Yoav Messinger, and D. Ashley Hill. Dicer1-related sertoli-leydig cell tumor and gynandroblastoma: clinical and genetic findings from the international ovarian and testicular stromal tumor registry. Gynecologic oncology, 147 3:521-527, Dec 2017. URL: https://doi.org/10.1016/j.ygyno.2017.09.034, doi:10.1016/j.ygyno.2017.09.034. This article has 151 citations and is from a domain leading peer-reviewed journal.

7. (cazzato2024dicer1tumorsyndrome pages 1-2): Gerardo Cazzato, Nadia Casatta, Carmelo Lupo, Giuseppe Ingravallo, and Domenico Ribatti. Dicer1 tumor syndrome: a retrospective review and future perspectives. Journal of Molecular Pathology, 5:264-275, Jul 2024. URL: https://doi.org/10.3390/jmp5030019, doi:10.3390/jmp5030019. This article has 6 citations.

8. (fraire2023intronicgermlinedicer1 pages 1-2): Claudette R. Fraire, Paige R. Mallinger, Jessica N. Hatton, Jung Kim, David S. Dickens, Peter A. Argenta, Samuel Milanovich, Taylor Hartshorne, David J. Carey, Jeremy S. Haley, Gretchen Urban, Jeon Lee, D. Ashley Hill, Douglas R. Stewart, Kris Ann P. Schultz, and Kenneth S. Chen. Intronic germline dicer1 variants in patients with sertoli-leydig cell tumor. JCO Precision Oncology, Sep 2023. URL: https://doi.org/10.1200/po.23.00189, doi:10.1200/po.23.00189. This article has 16 citations and is from a peer-reviewed journal.

9. (nemejcova2025amolecularand pages 11-12): Kristýna Němejcová, Nikola Hájková, Eva Krkavcová, Michaela Kendall Bártů, Romana Michálková, Adam Šafanda, Marián Švajdler, Tetiana Shatokhina, Jan Laco, Radoslav Matěj, Jitka Hausnerová, Jozef Škarda, Monika Náležinská, Tomáš Zima, and Pavel Dundr. A molecular and immunohistochemical study of 37 cases of ovarian sertoli–leydig cell tumor. Virchows Archiv, 487:127-140, Nov 2025. URL: https://doi.org/10.1007/s00428-024-03984-5, doi:10.1007/s00428-024-03984-5. This article has 16 citations and is from a peer-reviewed journal.

10. (NCT01042522 chunk 7):  Paclitaxel and Carboplatin or Bleomycin Sulfate, Etoposide Phosphate, and Cisplatin in Treating Patients With Advanced or Recurrent Sex Cord-Ovarian Stromal Tumors. GOG Foundation. 2010. ClinicalTrials.gov Identifier: NCT01042522

11. (NCT00748657 chunk 1):  Bevacizumab in Treating Patients With Recurrent Sex Cord-Stromal Tumors of the Ovary. National Cancer Institute (NCI). 2008. ClinicalTrials.gov Identifier: NCT00748657

12. (cazzato2024dicer1tumorsyndrome pages 7-8): Gerardo Cazzato, Nadia Casatta, Carmelo Lupo, Giuseppe Ingravallo, and Domenico Ribatti. Dicer1 tumor syndrome: a retrospective review and future perspectives. Journal of Molecular Pathology, 5:264-275, Jul 2024. URL: https://doi.org/10.3390/jmp5030019, doi:10.3390/jmp5030019. This article has 6 citations.

13. (cazzato2024dicer1tumorsyndrome pages 8-10): Gerardo Cazzato, Nadia Casatta, Carmelo Lupo, Giuseppe Ingravallo, and Domenico Ribatti. Dicer1 tumor syndrome: a retrospective review and future perspectives. Journal of Molecular Pathology, 5:264-275, Jul 2024. URL: https://doi.org/10.3390/jmp5030019, doi:10.3390/jmp5030019. This article has 6 citations.

14. (schultz2017dicer1relatedsertolileydigcell pages 10-12): Kris Ann P. Schultz, Anne K. Harris, Michael Finch, Louis P. Dehner, Jubilee B. Brown, David M. Gershenson, Robert H. Young, Amanda Field, Weiying Yu, Joyce Turner, Nicholas G. Cost, Dominik T. Schneider, Douglas R. Stewart, A. Lindsay Frazier, Yoav Messinger, and D. Ashley Hill. Dicer1-related sertoli-leydig cell tumor and gynandroblastoma: clinical and genetic findings from the international ovarian and testicular stromal tumor registry. Gynecologic oncology, 147 3:521-527, Dec 2017. URL: https://doi.org/10.1016/j.ygyno.2017.09.034, doi:10.1016/j.ygyno.2017.09.034. This article has 151 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Malignant_Sertoli-Leydig_Cell_Tumor_of_Ovary-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.