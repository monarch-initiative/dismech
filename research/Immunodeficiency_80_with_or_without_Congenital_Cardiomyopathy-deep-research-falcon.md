---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-17T21:23:56.611570'
end_time: '2026-08-17T21:38:16.492574'
duration_seconds: 859.88
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Immunodeficiency 80 with or without Congenital Cardiomyopathy
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
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 4
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Immunodeficiency_80_with_or_without_Congenital_Cardiomyopathy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 80 with or without Congenital Cardiomyopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 80 with or without Congenital Cardiomyopathy** covering all of the
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
- **Disease Name:** Immunodeficiency 80 with or without Congenital Cardiomyopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 80 with or without Congenital Cardiomyopathy** covering all of the
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


# Comprehensive research report: Immunodeficiency 80 with or without congenital cardiomyopathy

## Executive summary and evidence limitations

**Immunodeficiency 80 with or without congenital cardiomyopathy** is an ultra-rare, autosomal-recessive **MCM10-related DNA-replication disorder**. Its best-established postnatal presentation is developmental natural-killer-cell deficiency (NKD), with near-absent circulating NK cells, failure of terminal NK-cell maturation, and potentially fatal herpesvirus infection. A more severe allelic presentation has been associated with prenatal restrictive/congenital cardiomyopathy, fetal demise, and underdevelopment of lymphoid organs. Open Targets identifies MCM10 as the sole associated target and maps the disease to **MONDO:0030266**. (OpenTargets Search: Immunodeficiency 80 with or without congenital cardiomyopathy, schmit2024acriticalthreshold pages 9-10)

The evidence base is exceptionally small: the detailed immune phenotype rests principally on **one child**, whereas the cardiomyopathy association comes from a separate fetal family and later summaries. Consequently, phenotype frequencies, penetrance, survival rates, and treatment-response estimates cannot be calculated reliably. Claims below are labeled as direct human, experimental-model, or expert-review evidence.

| evidence domain | direct observation/model | key quantitative finding | evidence level | source/date |
|---|---|---:|---|---|
| Disease/entity identifiers | Disease resolved as **immunodeficiency 80 with or without congenital cardiomyopathy**; causal gene **MCM10**; MONDO **MONDO:0030266**; Open Targets disease-target association links only **MCM10** to this disease | 1 target associated in Open Targets evidence set | Curated disease database + literature linkage | Open Targets context (OpenTargets Search: Immunodeficiency 80 with or without congenital cardiomyopathy) |
| Clinical presentation 1: postnatal immune phenotype | Single male proband with classical NK-cell deficiency presenting at **16 months** with fever, organomegaly, diarrhea, and **CMV 2×10^6 copies/mL**; died at **24 months** | Age at presentation 16 mo; CMV viral load 2×10^6 copies/mL; death at 24 mo | Direct human case | J Clin Invest 2020, published 2020-08-31 (mace2020humannkcell pages 2-3, mace2020humannkcell pages 1-2) |
| Clinical presentation 2: fetal cardiomyopathy | Separate family/fetal presentation cited in later reviews and WGS study: severe **restrictive/congenital cardiomyopathy** with fetal demise/intrauterine death attributed to biallelic **MCM10** loss; underdeveloped thymus/spleen also cited in 2024 mechanistic discussion | Quantitative details not recoverable from available primary text; existence of fetal cardiomyopathy presentation repeatedly cited | Indirect human evidence from secondary sources summarizing prior family | Genome Med 2023; reviews 2021-2024 (schmit2024acriticalthreshold pages 9-10, schmit2021congenitaldiseasesof pages 14-16) |
| Postnatal causal variants | Compound heterozygous **MCM10** variants in proband: paternal missense **NM_018518.5:c.1276C>T (p.Arg426Cys)** and maternal nonsense **NM_018518.5:c.1744C>T (p.Arg582Ter)**; segregated with autosomal-recessive disease | Missense seen at extremely low frequency: ExAC **4.12×10^-5**, gnomAD **2.5×10^-5**; nonsense absent from ExAC/gnomAD in cited analysis | Direct human genetics | J Clin Invest 2020 (mace2020humannkcell pages 4-6, mace2020humannkcell pages 3-4) |
| Immune laboratory phenotype | Profound NK-cell lymphopenia with broader mild lymphopenia/hypogammaglobulinemia | **CD56+CD3- 1/μL** (ref 100-1400); **CD3+ 1250** (1400-8000); **CD4+ 770** (900-5500); **CD8+ 280** (400-2300); **CD19+ 210** (600-3100); **IgG 2.22 g/L** (3-13.2); **IgM 0.45 g/L** (0.48-2.1) | Direct human case | J Clin Invest 2020 (mace2020humannkcell pages 3-4, mace2020humannkcell pages 2-3) |
| Hyperinflammation/HLH-like features | Workup considered HLH during CMV illness | **Ferritin 33,150 μg/L** (15-100); **triglycerides 1.7 mmol/L** (0.4-1.6); **fibrinogen 0.5 g/L** (2-4) | Direct human case | J Clin Invest 2020 (mace2020humannkcell pages 3-4, mace2020humannkcell pages 2-3) |
| NK subset phenotype | Peripheral blood and modeled systems showed near absence of NK cells with relative overrepresentation of immature **CD56bright** cells and reduced mature **CD56dim** cells | NK frequency **<1%** in peripheral blood; about **50%** of residual NK cells CD56bright in clinical assessment | Direct human case + model recapitulation | J Clin Invest 2020 (mace2020humannkcell pages 10-11, mace2020humannkcell pages 2-3, mace2020humannkcell pages 9-10) |
| Molecular consequence of p.Arg582Ter | Premature stop predicted to undergo nonsense-mediated decay; if expressed, truncation impairs nuclear localization | Endogenous truncated protein not detected; heterozygous engineered lines showed ~**50%** reduction in MCM10 protein expression | Direct human cells + engineered human cells | J Clin Invest 2020 (mace2020humannkcell pages 4-6) |
| Molecular consequence of p.Arg426Cys | Missense does not abolish replisome assembly but impairs growth/chromatin dynamics and contributes to replication stress in compound state | Homozygous engineered line retained ~**80%** growth vs WT; variant associated with increased chromatin retention of MCM10 | Engineered human cell evidence linked to patient allele | J Clin Invest 2020 (mace2020humannkcell pages 4-6, mace2020humannkcell pages 6-7) |
| Replication-stress phenotype | Patient fibroblasts and MCM10-deficient NK-line models showed S-phase accumulation, enlarged nuclei, and increased DNA damage signaling | Increased **γH2AX** foci and nuclear area; significant excess early **S phase** with reduced **G2/M**; patient-vs-control γH2AX comparisons reported **P<0.0001** | Direct patient cells + engineered cell models | J Clin Invest 2020 (mace2020humannkcell pages 6-7, mace2020humannkcell pages 10-11, mace2020humannkcell pages 1-2) |
| 2024 iPSC genomic-instability findings | **MCM10+/-** iPSC lines used to model developmental threshold effects during NK differentiation | Micronuclei markedly enriched for telomeric fragments: **83%** of micronuclei in clone 10 contained telomeric foci; **17%** also contained centromeric foci | Experimental human iPSC model | Open Biology 2024 (schmit2024acriticalthreshold pages 5-6, schmit2024acriticalthreshold pages 9-10) |
| 2024 iPSC telomere/NK differentiation findings | Reduced MCM10 caused impaired clonogenic survival, telomere erosion, reduced HSC output, and failure to form mature NK cells | Disease model failed to generate mature **stage 5 NK cells**; telomere shortening/significant signal-free ends increased during LP→NK transition | Experimental human iPSC model | Open Biology 2024 (schmit2024acriticalthreshold pages 1-2, schmit2024acriticalthreshold pages 8-9) |
| Additional mechanistic profiling | Independent replication-timing study of cells from a patient with MCM10 mutations | Replication timing variability across **46% of genome**, with replication delays and initiation-site gains/losses | Experimental functional genomics in patient-derived cells | Hum Mol Genet 2022 (caballero2021comprehensiveanalysisof pages 1-3) |
| Diagnostic approach | Clinical immunophenotyping plus trio exome/genome-style rare disease sequencing; disease also highlighted by broader WGS literature as a diagnosis that can be missed without comprehensive genomic analysis | Trio-based WES identified recessive MCM10 variants in index case; broader WGS cohort reported overall diagnostic yield **35%** and **39%** when novel candidates included | Direct case + broader rare-disease genomics evidence | J Clin Invest 2020; Genome Med 2023 (mace2020humannkcell pages 2-3, pagnamenta2023structuralandnoncoding pages 20-21) |
| Treatment evidence | Only direct disease-specific treatment evidence is supportive care followed by **bone marrow transplantation/HSCT** in the index child; no approved targeted therapy identified | Transplant performed, but patient **succumbed to overwhelming preexisting CMV** | Direct human case | J Clin Invest 2020 (mace2020humannkcell pages 2-3) |
| Prevention/surveillance implications | No disease-specific prevention trials; by analogy to NKD/IEI, early recognition of herpesvirus susceptibility and genetic diagnosis is emphasized in expert review literature | No disease-specific quantitative surveillance data | Expert review inference | J Clin Immunol 2023; J Hum Immunity 2025 (guilz2023unwindingtherole pages 1-2, guilz2023unwindingtherole pages 9-11) |
| Major evidence gaps | Extremely few known patients/families; no prevalence/incidence, penetrance, sex ratio, standardized criteria, biomarker validation, natural-history cohort, or interventional trial specific to MCM10 disease | Postnatal phenotype supported mainly by **1** well-described child; cardiomyopathy details incompletely recoverable from available primary text | Evidence-gap assessment | Synthesized from available contexts (mace2020humannkcell pages 2-3, schmit2024acriticalthreshold pages 9-10, pagnamenta2023structuralandnoncoding pages 20-21) |


*Table: This table compiles compact knowledge-base evidence for MCM10-associated immunodeficiency 80 with or without congenital cardiomyopathy. It separates direct human observations from model-based findings and highlights both established facts and major evidence gaps.*

## 1. Disease information

### Definition and classification

The disease is an **inborn error of immunity caused by biallelic partial loss-of-function MCM10 variants**. MCM10 encodes minichromosome-maintenance protein 10, an essential regulator of eukaryotic replisome assembly, activation, origin firing, replication-fork progression, and genome stability. In the postnatal phenotype, insufficient MCM10 selectively compromises proliferative transitions required to generate mature CD56^dim NK cells. (mace2020humannkcell pages 2-3, mace2020humannkcell pages 1-2, guilz2023unwindingtherole pages 1-2)

**Suggested identifiers and names**

- **MONDO:** MONDO:0030266.
- **Causal gene:** *MCM10*; Ensembl ENSG00000065328.
- **Disease name:** Immunodeficiency 80 with or without congenital cardiomyopathy.
- **Common alternatives:** MCM10 deficiency; MCM10-related NK-cell deficiency; MCM10-associated natural-killer-cell deficiency; NKD due to MCM10 deficiency.
- **OMIM:** commonly represented as immunodeficiency 80; the exact OMIM accession was not independently recoverable from the retrieved primary texts and should be verified directly in OMIM before database ingestion.
- **Orphanet, MeSH, ICD-10/ICD-11:** no dedicated disease-specific entries were established from the available evidence. Broader codes for primary immunodeficiency/NK-cell deficiency or cardiomyopathy would lose molecular specificity.

The principal evidence is **aggregated disease-level literature derived from individual patients and families**, not EHR-scale population data. The postnatal paper reports one child and experimental derivatives of his cells. (mace2020humannkcell pages 1-2)

## 2. Etiology, risk, protective factors, and gene–environment interaction

### Causal factor

The primary cause is **germline biallelic MCM10 dysfunction**. In the postnatal proband, the paternal allele was **NM_018518.5:c.1276C>T, p.(Arg426Cys)** and the maternal allele was **NM_018518.5:c.1744C>T, p.(Arg582Ter)**. The variants segregated as an autosomal-recessive trait. The stop-gain allele undergoes or is strongly predicted to undergo nonsense-mediated decay; experimentally expressed truncated protein also lacked effective nuclear localization. The missense allele retained protein expression and replisome interactions but impaired growth and chromatin dynamics, making the compound state hypomorphic rather than a complete null. (mace2020humannkcell pages 3-4, mace2020humannkcell pages 4-6)

The p.Arg582Ter allele was absent from ExAC and gnomAD in the cited analysis. p.Arg426Cys was extremely rare—approximately **4.12×10^-5 in ExAC** and **2.5×10^-5 in gnomAD**, with no reported homozygotes—and had CADD 24.3, PolyPhen-2 1.0, and MutationTaster 0.99 in the original study. These are supporting, not independently sufficient, pathogenicity data. (mace2020humannkcell pages 3-4)

### Risk and protective factors

- **Established genetic risk:** inheriting two functionally damaging MCM10 alleles in trans.
- **Family history/consanguinity:** the index child’s parents were healthy and nonconsanguineous; consanguinity is not required. (mace2020humannkcell pages 2-3)
- **Modifier genes, founder alleles, anticipation, or germline mosaicism:** not established.
- **Sex, ancestry, age, lifestyle, toxin, dietary, or occupational risks:** no evidence of causal effects.
- **Protective genetic or environmental factors:** none identified.

### Gene–environment interaction

Infection does not cause the Mendelian disorder, but viral exposure reveals the immune defect. NK-cell failure particularly compromises early control of herpesviruses; the index child developed overwhelming CMV. Thus, the defensible causal chain is **MCM10 hypomorphism → defective NK maturation → impaired antiviral cellular defense → severe CMV disease**, with infection acting as a clinical trigger rather than a genetic modifier. (mace2020humannkcell pages 10-11, guilz2023unwindingtherole pages 1-2, mace2020humannkcell pages 2-3)

## 3. Phenotypes

### Direct postnatal human phenotype

The male proband was apparently well until **16 months**, when he presented with fever, organomegaly, diarrhea, and CMV at **2×10^6 copies/mL**. He had profound NK lymphopenia: CD56+CD3− cells were **1/µL** versus a reference interval of 100–1,400. NK cells constituted less than 1% of peripheral blood lymphocytes; approximately half of the very small residual population appeared CD56^bright, indicating relative loss of terminally mature CD56^dim cells. (mace2020humannkcell pages 10-11, mace2020humannkcell pages 2-3)

Other abnormalities were milder: CD3 1,250/µL, CD4 770/µL, CD8 280/µL, CD19 210/µL, IgG 2.22 g/L, and IgM 0.45 g/L. T-cell activation to phytohemagglutinin was reduced, whereas responses to PMA and CD3 stimulation were normal. Ferritin was **33,150 µg/L**, triglycerides 1.7 mmol/L, and fibrinogen 0.5 g/L, producing an HLH-like inflammatory picture during CMV infection. (mace2020humannkcell pages 2-3, mace2020humannkcell pages 3-4)

The child received bone-marrow transplantation but died at **24 months** from overwhelming pre-existing CMV. This establishes severe early-childhood morbidity and mortality but does not provide a population survival estimate. (mace2020humannkcell pages 2-3)

### Prenatal/cardiac phenotype

Later literature describes a separate, more severe biallelic MCM10 presentation with fetal restrictive/congenital cardiomyopathy, intrauterine death, and underdeveloped thymus and spleen. The available excerpts do not permit reliable extraction of the complete pedigree, exact fetal phenotype frequencies, or all variant nomenclature; these details should therefore remain provisional. (schmit2024acriticalthreshold pages 9-10)

### Suggested phenotype ontology mappings

- Natural killer cell deficiency — **HP:0002846** (verify current HPO label/version).
- Lymphopenia — **HP:0001888**.
- Hypogammaglobulinemia — **HP:0004313**.
- Recurrent/severe viral infection or recurrent herpesvirus infection — use the most specific current HPO viral-infection term available.
- Cytomegalovirus infection — map to an HPO infectious-disease term where available; otherwise SNOMED CT/NCBI Taxonomy **Human betaherpesvirus 5, Taxon 10359**.
- Fever — **HP:0001945**.
- Hepatosplenomegaly/organomegaly — **HP:0001433** or organ-specific terms if documented.
- Diarrhea — **HP:0002014**.
- Hyperferritinemia — **HP:0003281**.
- Hypofibrinogenemia — **HP:0011900**.
- Restrictive cardiomyopathy — **HP:0001723**.
- Intrauterine fetal demise — use the current HPO fetal-death term.

Because only one postnatal patient is deeply characterized, frequencies should be entered as **1/1 observed**, not “100% of patients.” No validated disease-specific quality-of-life instruments or scores have been reported. Severe infection, hospitalization, transplantation, and death imply profound functional impact.

## 4. Genetic and molecular information

### Gene and variants

*MCM10* encodes a nonredundant replisome factor that binds MCM2–7, CDC45, and DNA and supports replication initiation and elongation. Complete loss is generally incompatible with cell viability or embryonic development, explaining why surviving human disease alleles are likely hypomorphic. (mace2020humannkcell pages 2-3, mace2020humannkcell pages 4-6, mace2020humannkcell pages 10-11)

The postnatal alleles are **germline**, not somatic:

1. **c.1276C>T, p.Arg426Cys:** rare missense allele; stable and nuclear but associated with impaired proliferation and excessive chromatin retention. An engineered homozygous line retained approximately 80% of wild-type growth.
2. **c.1744C>T, p.Arg582Ter:** nonsense allele; endogenous truncated protein was not detected, consistent with nonsense-mediated decay. Engineered heterozygous cells showed approximately 50% MCM10 reduction and 50% reduced growth. (mace2020humannkcell pages 3-4, mace2020humannkcell pages 4-6)

The functional consequence is best described as **compound partial loss of function**. The original publication supplied strong functional evidence, but contemporary ClinVar classifications and review status should be checked directly before assigning a final ACMG/AMP category. No dominant-negative or gain-of-function mechanism has been demonstrated.

No validated modifier gene, disease-specific epigenetic signature, recurrent chromosomal abnormality, or somatic second hit is known. Increased chromosome breakage/translocations in deficient cells are downstream consequences of replication stress, not the inherited cause. (schmit2021congenitaldiseasesof pages 14-16)

## 5. Environmental and infectious information

No toxin, radiation, pollution, smoking, alcohol, diet, or exercise exposure is known to initiate MCM10 disease. The clinically important exposure class is **viral infection**, especially herpesviruses. Reviews of CMG-helicase NKD emphasize susceptibility to CMV, VZV, and EBV; only CMV is directly documented in the MCM10 index child. (guilz2023unwindingtherole pages 1-2, mace2020humannkcell pages 2-3)

There is no zoonotic or person-to-person transmission of the genetic disorder. Ordinary viral transmission remains relevant because the host defect magnifies disease severity.

## 6. Mechanism and pathophysiology

### Upstream molecular defect

MCM10 participates in activating and stabilizing the CDC45–MCM2-7–GINS replicative helicase and supports origin firing and replication-fork processivity. The two patient alleles lower the quantity and quality of functional nuclear MCM10. (mace2020humannkcell pages 2-3, mace2020humannkcell pages 4-6)

### Causal chain

**Biallelic MCM10 hypomorphism → defective origin activation/fork progression → prolonged early S phase and replication stress → γH2AX activation, micronuclei, fragile-site instability, and telomere erosion → poor survival/output of hematopoietic stem/progenitor cells and failure of late NK-cell maturation → profound loss of CD56^dim NK cells → severe herpesvirus susceptibility.** In more severe allelic combinations, the same replication threshold may be crossed during cardiac and lymphoid-organ development, producing prenatal cardiomyopathy and fetal death. (mace2020humannkcell pages 6-7, mace2020humannkcell pages 10-11, schmit2024acriticalthreshold pages 9-10, schmit2024acriticalthreshold pages 1-2)

Patient fibroblasts had increased nuclear area, more γH2AX signal, increased S-phase accumulation, reduced G2/M representation, and excessive MCM10 chromatin association. Patient-derived or knockdown NK models reproduced impaired terminal maturation. (mace2020humannkcell pages 6-7, mace2020humannkcell pages 10-11, mace2020humannkcell pages 9-10)

### Recent 2024 development

The 2024 iPSC study refined this mechanism by demonstrating a **dose-dependent MCM10 threshold**. MCM10+/− iPSCs had impaired clonogenic survival, micronuclei, and telomere erosion. **Eighty-three percent of micronuclei** in one clone contained telomeric foci, and 17% also contained centromeric foci. Mutant cells generated fewer HSCs; lymphoid progenitors formed but failed to produce mature stage-5 NK cells. Telomere signal-free ends increased during the lymphoid-progenitor-to-NK transition. Residual stage-4 cells could retain degranulation/cytokine competence, indicating that deficient cell number and maturation, rather than universal intrinsic cytotoxic failure, is central. (schmit2024acriticalthreshold pages 1-2, schmit2024acriticalthreshold pages 5-6, schmit2024acriticalthreshold pages 9-10)

A replication-timing analysis found variability across **46% of the genome** in MCM10-mutant cells, dominated by replication delays and gains/losses of initiation sites. This supports a genome-wide initiation defect, although it derives from cells from a single patient and is not a clinical biomarker. (caballero2021comprehensiveanalysisof pages 1-3)

### Suggested ontology annotations

**GO biological process:** DNA replication initiation; DNA replication; DNA-dependent DNA replication maintenance; replication-fork progression; DNA-damage response; cell-cycle S-phase transition; telomere maintenance; chromosome segregation; hematopoietic stem-cell differentiation; NK-cell differentiation; antiviral immune response.

**GO cellular component:** nucleus; chromatin; replication fork; replisome; CMG complex; chromosome/telomere.

**Cell Ontology:** natural killer cell **CL:0000623**; CD56-bright NK cell and CD56-dim NK cell subtypes where supported by the current CL release; hematopoietic stem cell **CL:0000037**; lymphoid progenitor cell; dermal fibroblast; cardiomyocyte.

No disease-specific metabolomic, lipidomic, proteomic, spatial-transcriptomic, or patient single-cell atlas was found. The strongest “multi-omic” evidence is functional genomics/replication timing plus telomere cytogenetics.

## 7. Anatomical structures affected

- **Primary immune sites:** peripheral blood NK compartment, bone marrow/hematopoietic progenitor compartment, and—based on fetal observations—thymus and spleen.
- **Cardiovascular:** myocardium in the congenital/restrictive-cardiomyopathy presentation.
- **Secondary sites during infection:** gastrointestinal tract and reticuloendothelial organs, reflected by diarrhea and organomegaly during CMV disease.
- **Subcellular:** nucleus, chromatin-bound replisome, replication forks, chromosomes, and telomeres.

Suggested UBERON mappings include blood **UBERON:0000178**, bone marrow **UBERON:0002371**, spleen **UBERON:0002106**, thymus **UBERON:0002370**, heart **UBERON:0000948**, and myocardium **UBERON:0002349**. There is no relevant lateralization.

## 8. Temporal development

The disease begins molecularly in embryonic development, but clinical timing is allele-dependent:

- **Severe prenatal form:** congenital cardiomyopathy with fetal demise.
- **Surviving postnatal form:** apparently delayed recognition until severe infection at 16 months, followed by rapid deterioration and death at 24 months.

The genetic and NK-development defects are lifelong. Infectious manifestations may be episodic, but uncontrolled CMV can be progressive and fatal. No accepted disease stages, remission pattern, or longitudinal progression rate exists. The critical intervention window is likely **before acquisition or dissemination of a major herpesvirus**, because transplantation did not rescue the child from established overwhelming CMV. This is biologically and clinically plausible but supported by only one direct case. (mace2020humannkcell pages 2-3)

## 9. Inheritance and population

Inheritance is **autosomal recessive**. Healthy heterozygous parents transmitted one allele each to the index child. For two carrier parents, standard Mendelian counseling gives a 25% affected, 50% carrier, and 25% unaffected/noncarrier probability for each pregnancy, assuming both variants are truly pathogenic and no unusual reproductive mechanism. (mace2020humannkcell pages 2-3, mace2020humannkcell pages 4-6)

Prevalence and incidence per 100,000, carrier frequency, penetrance, sex ratio, geographic distribution, founder effects, and ancestry enrichment are unknown. The observed cohort is too small to assess variable expressivity formally, although the immune-versus-prenatal-cardiac presentations strongly suggest **allelic severity and/or tissue-specific threshold effects**. Anticipation is not expected for this variant class and has not been reported.

## 10. Diagnostics

### Clinical and laboratory evaluation

In a child with severe or unusual herpesvirus disease, test:

1. CBC with differential and lymphocyte subsets.
2. Flow cytometry for CD3, CD4, CD8, CD19, and CD3−CD56+ NK cells.
3. NK subsets, especially CD56^bright/CD56^dim distribution and maturation markers such as CD16.
4. NK cytotoxicity/degranulation where available, recognizing that residual immature cells may retain some function.
5. Quantitative immunoglobulins, vaccine responses, T-cell proliferation, and broader IEI assessment.
6. CMV/EBV viral-load PCR and organ-specific evaluation.
7. Ferritin, triglycerides, fibrinogen, soluble IL-2 receptor, and marrow/HLH work-up when hyperinflammation is suspected.
8. ECG and echocardiography; consider cardiac MRI if the phenotype or family history suggests cardiomyopathy.

The index child’s HLH differential was supported by extreme ferritin and hypofibrinogenemia, but SAP, XIAP, MHC-I/MHC-II, and CD3ζ testing was normal. (mace2020humannkcell pages 2-3)

### Genetic testing

A practical approach is an IEI/NKD panel containing *MCM10*, *MCM4*, *GINS1*, *GINS4*, *IRF8*, *GATA2*, *RTEL1*, *POLE1*, and *POLE2*, or trio WES/WGS when the presentation is syndromic or panel-negative. The index diagnosis was made by trio WES. Sanger or orthogonal confirmation, parental phasing, copy-number analysis, and transcript studies for splice/nonsense alleles are appropriate. (mace2020humannkcell pages 2-3)

WGS is useful when coding analysis is unrevealing because it can detect structural, intronic, and splice-altering variants. In a broader rare-disease cohort, comprehensive WGS achieved 35% confirmed diagnostic yield, or 39% including novel candidates; structural/splice/deep-intronic variants made substantial contributions. These percentages are **not MCM10-specific**. (pagnamenta2023structuralandnoncoding pages 20-21)

CMA, karyotyping, FISH, mitochondrial sequencing, and repeat-expansion testing are not first-line tests for this single-gene recessive disorder unless another diagnosis is suspected. RNA sequencing may help establish aberrant splicing or nonsense-mediated decay but is not a validated stand-alone diagnostic.

### Differential diagnosis

Key alternatives include MCM4-, GINS1-, or GINS4-related NKD; GATA2 and IRF8 deficiency; RTEL1/telomere disorders; POLE1/POLE2 replication disorders; familial HLH; XLP1/SH2D1A; XIAP deficiency; severe combined or combined immunodeficiency; and congenital CMV infection. Congenital cardiomyopathy additionally requires exclusion of sarcomeric, mitochondrial, storage, and other DNA-replication disorders. Relative preservation/overrepresentation of CD56^bright cells with loss of CD56^dim cells points toward a CMG-replisome maturation defect. (mace2020humannkcell pages 2-3, guilz2023unwindingtherole pages 7-8)

No newborn screening assay or standardized diagnostic criteria are available. Cascade molecular testing is appropriate after a familial genotype is established.

## 11. Outcome and prognosis

The only deeply characterized postnatal patient died at age two, despite transplantation, from pre-existing CMV. Therefore, five- and ten-year survival, life expectancy, mortality rate, disability outcomes, and validated quality-of-life measures are unavailable. (mace2020humannkcell pages 2-3)

Probable adverse prognostic factors are severe early herpesvirus infection, extremely low NK count, inability to clear viremia before transplantation, HLH-like hyperinflammation, and variants producing a lower residual MCM10 level. The last factor is supported mechanistically by dose-dependent iPSC phenotypes rather than a human prognostic cohort. (schmit2024acriticalthreshold pages 5-6, schmit2024acriticalthreshold pages 1-2)

Long-term malignancy risk is biologically plausible because MCM10 deficiency causes genome instability and NK cells contribute to tumor surveillance; however, no MCM10-specific cancer-incidence estimate exists, and the tiny cohort precludes inference. (guilz2023unwindingtherole pages 9-11)

## 12. Treatment

There is **no approved MCM10-targeted pharmacotherapy, gene therapy, RNA therapy, or genotype-specific drug**.

### Current clinical management

- Prompt specialist management of CMV or other herpesvirus infection using pathogen-appropriate antivirals and quantitative PCR monitoring.
- Immunoglobulin replacement when clinically significant hypogammaglobulinemia or poor antibody responses are present.
- Antimicrobial prophylaxis individualized to immune phenotype and infection history.
- HLH-directed treatment if formal criteria are met; evidence is extrapolated rather than MCM10-specific.
- Cardiomyopathy-directed therapy according to pediatric cardiology standards, including heart-failure and arrhythmia management when applicable.
- **Allogeneic hematopoietic stem-cell transplantation (HSCT)** is biologically capable of replacing defective hematopoiesis, but direct evidence consists of one unsuccessful case in which overwhelming CMV was already present. It cannot currently be assigned a response rate. (mace2020humannkcell pages 2-3)

Suggested NCIT intervention mappings include **Hematopoietic Stem Cell Transplantation**, **Antiviral Therapy**, **Immunoglobulin Replacement Therapy**, and supportive/palliative care terms in the current NCIT release. Specific antiviral CHEBI/NCIT terms should be selected based on the drug actually administered; the source did not provide a recoverable antiviral regimen.

No disease-specific ClinicalTrials.gov interventional study was identified. Experimental correction of MCM10 in autologous HSCs is conceptually possible but faces a narrow dosage window: too little MCM10 impairs replication, while uncontrolled alteration of an essential genome-stability protein could be unsafe.

## 13. Prevention

### Primary prevention

The inherited defect cannot be prevented by lifestyle change. Reproductive options after molecular diagnosis include carrier testing, cascade testing, prenatal diagnosis, and preimplantation genetic testing for monogenic disease. Genetic counseling should discuss the 25% recurrence risk for two confirmed carriers.

### Secondary and tertiary prevention

Early molecular diagnosis, baseline viral screening, rapid PCR testing during febrile illness, avoidance of unmonitored live vaccines until immune competence is defined, and individualized prophylaxis may reduce infectious morbidity. Household contacts should follow routine immunization guidance, and CMV-safe blood products should be considered under applicable immunocompromised-patient standards. These are expert-practice extrapolations; no MCM10-specific prevention trial exists.

The index case suggests that controlling active CMV before HSCT is critical, although one observation cannot define an algorithm. Regular immune, infectious-disease, and cardiac surveillance is prudent. (mace2020humannkcell pages 2-3)

## 14. Other species and natural disease

- **Human:** *Homo sapiens*, NCBI Taxon **9606**.
- **Mouse:** *Mus musculus*, Taxon **10090**; complete *Mcm10* deletion is embryonic lethal, limiting disease recapitulation. Heterozygous mice do not reproduce the compound hypomorphic human syndrome reliably. (mace2020humannkcell pages 10-11, schmit2024acriticalthreshold pages 8-9)
- **Zebrafish:** *Danio rerio*, Taxon **7955**; experimental work supports an evolutionarily conserved requirement for *mcm10* in hematopoietic-stem-cell emergence. (schmit2024acriticalthreshold pages 9-10)

No naturally occurring veterinary MCM10 immunodeficiency/cardiomyopathy syndrome, breed association, or zoonotic potential was identified. Animal evidence is experimentally induced, not a transmissible natural disease.

## 15. Model organisms and experimental systems

### Human cellular models

Patient dermal fibroblasts directly demonstrated S-phase dysregulation, γH2AX accumulation, enlarged nuclei, and abnormal chromatin retention. Engineered hTERT-RPE1 and 293T cells separated the effects of p.Arg426Cys and p.Arg582Ter; CRISPR-reduced NK92 cells demonstrated impaired cell-cycle progression. (mace2020humannkcell pages 6-7, mace2020humannkcell pages 4-6)

### Developmental models

MCM10-knockdown CD34+ precursors accumulated at early NK developmental stages and generated fewer mature stage-4/5 cells. Patient-derived iPSCs were differentiated to CD34+ precursors and transplanted into NSG mice; all four patient-derived humanized mice showed excess CD56^bright cells and increased γH2AX, recapitulating the human maturation phenotype. (mace2020humannkcell pages 8-9, mace2020humannkcell pages 9-10)

The 2024 heterozygous iPSC system enables dose-response analysis and identifies telomere erosion during HSC/NK differentiation as a major bottleneck. Its limitation is that engineered MCM10+/− clones do not exactly reproduce every compound-heterozygous patient allele or the cardiac phenotype. (schmit2024acriticalthreshold pages 1-2)

### Animal-model limitations

Complete mouse knockout is embryonic lethal, while a single null allele is insufficient to model the human compound-hypomorphic state. NSG humanized mice model human NK development but not a complete immune system or congenital cardiomyopathy. Zebrafish support conserved hematopoietic biology but have not yet established full phenotypic equivalence to the human disorder. (mace2020humannkcell pages 10-11, schmit2024acriticalthreshold pages 9-10, schmit2024acriticalthreshold pages 8-9)

## Key verbatim evidence excerpts

From Mace et al., published **31 August 2020**, *Journal of Clinical Investigation*, DOI [10.1172/JCI134966](https://doi.org/10.1172/JCI134966), PMID **32865517**:

> “Here, we report a cause of NKD resulting from compound heterozygous mutations in minichromosomal maintenance complex member 10 (MCM10) that impaired NK cell maturation in a child with fatal susceptibility to CMV.” (mace2020humannkcell pages 1-2)

> “Together, these data define MCM10 as an NKD gene and provide biological insight into the requirement for the DNA replisome in human NK cell maturation and function.” (mace2020humannkcell pages 1-2)

From Schmit et al., published **January 2024**, *Open Biology*, DOI [10.1098/rsob.230407](https://doi.org/10.1098/rsob.230407):

> “The lack of mature NK cells coincided with telomere erosion, suggesting that NKD caused by these MCM10 variants arose from the accumulation of genomic instability including degradation of chromosome ends.” (schmit2024acriticalthreshold pages 1-2)

From Guilz et al., published **February 2023**, *Journal of Clinical Immunology*, DOI [10.1007/s10875-023-01437-3](https://doi.org/10.1007/s10875-023-01437-3): the expert review concludes that CMG-helicase variants unexpectedly produce NK-cell-focused inborn errors of immunity and emphasizes that the reason for NK-cell-selective vulnerability remains incompletely resolved. (guilz2023unwindingtherole pages 9-11, guilz2023unwindingtherole pages 1-2)

## Knowledge-base conclusion

The highest-confidence entry is: **biallelic hypomorphic MCM10 variants cause an autosomal-recessive replisome disorder characterized by defective terminal NK-cell maturation, profound NK lymphopenia, and severe herpesvirus susceptibility; more severe alleles can produce prenatal restrictive cardiomyopathy and fetal lethality.** The mechanistic evidence is strong across patient cells, engineered lines, iPSC differentiation, and humanized mice, but clinical evidence remains too sparse for reliable phenotype frequencies, epidemiology, penetrance, prognosis, or treatment-effect estimates. Future priorities are additional case ascertainment, direct characterization of the fetal cardiomyopathy alleles, standardized NK phenotyping, longitudinal viral and cardiac surveillance, and preclinical evaluation of safely dosage-controlled hematopoietic correction.

References

1. (OpenTargets Search: Immunodeficiency 80 with or without congenital cardiomyopathy): Open Targets Query (Immunodeficiency 80 with or without congenital cardiomyopathy, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (schmit2024acriticalthreshold pages 9-10): Megan M. Schmit, Ryan M. Baxley, Liangjun Wang, Peter Hinderlie, Marissa Kaufman, Emily Simon, Anjali Raju, Jeffrey S. Miller, and Anja-Katrin Bielinsky. A critical threshold of mcm10 is required to maintain genome stability during differentiation of induced pluripotent stem cells into natural killer cells. Open Biology, Jan 2024. URL: https://doi.org/10.1098/rsob.230407, doi:10.1098/rsob.230407. This article has 9 citations and is from a peer-reviewed journal.

3. (mace2020humannkcell pages 2-3): Emily M. Mace, Silke Paust, Matilde I. Conte, Ryan M. Baxley, Megan M. Schmit, Sagar L. Patil, Nicole C. Guilz, Malini Mukherjee, Ashley E. Pezzi, Jolanta Chmielowiec, Swetha Tatineni, Ivan K. Chinn, Zeynep Coban Akdemir, Shalini N. Jhangiani, Donna M. Muzny, Asbjørg Stray-Pedersen, Rachel E. Bradley, Mo Moody, Philip P. Connor, Adrian G. Heaps, Colin Steward, Pinaki P. Banerjee, Richard A. Gibbs, Malgorzata Borowiak, James R. Lupski, Stephen Jolles, Anja K. Bielinsky, and Jordan S. Orange. Human nk cell deficiency as a result of biallelic mutations in mcm10. Journal of Clinical Investigation, 130:5272-5286, Aug 2020. URL: https://doi.org/10.1172/jci134966, doi:10.1172/jci134966. This article has 79 citations and is from a highest quality peer-reviewed journal.

4. (mace2020humannkcell pages 1-2): Emily M. Mace, Silke Paust, Matilde I. Conte, Ryan M. Baxley, Megan M. Schmit, Sagar L. Patil, Nicole C. Guilz, Malini Mukherjee, Ashley E. Pezzi, Jolanta Chmielowiec, Swetha Tatineni, Ivan K. Chinn, Zeynep Coban Akdemir, Shalini N. Jhangiani, Donna M. Muzny, Asbjørg Stray-Pedersen, Rachel E. Bradley, Mo Moody, Philip P. Connor, Adrian G. Heaps, Colin Steward, Pinaki P. Banerjee, Richard A. Gibbs, Malgorzata Borowiak, James R. Lupski, Stephen Jolles, Anja K. Bielinsky, and Jordan S. Orange. Human nk cell deficiency as a result of biallelic mutations in mcm10. Journal of Clinical Investigation, 130:5272-5286, Aug 2020. URL: https://doi.org/10.1172/jci134966, doi:10.1172/jci134966. This article has 79 citations and is from a highest quality peer-reviewed journal.

5. (schmit2021congenitaldiseasesof pages 14-16): Megan Schmit and Anja-Katrin Bielinsky. Congenital diseases of dna replication: clinical phenotypes and molecular mechanisms. International Journal of Molecular Sciences, 22:911, Jan 2021. URL: https://doi.org/10.3390/ijms22020911, doi:10.3390/ijms22020911. This article has 45 citations.

6. (mace2020humannkcell pages 4-6): Emily M. Mace, Silke Paust, Matilde I. Conte, Ryan M. Baxley, Megan M. Schmit, Sagar L. Patil, Nicole C. Guilz, Malini Mukherjee, Ashley E. Pezzi, Jolanta Chmielowiec, Swetha Tatineni, Ivan K. Chinn, Zeynep Coban Akdemir, Shalini N. Jhangiani, Donna M. Muzny, Asbjørg Stray-Pedersen, Rachel E. Bradley, Mo Moody, Philip P. Connor, Adrian G. Heaps, Colin Steward, Pinaki P. Banerjee, Richard A. Gibbs, Malgorzata Borowiak, James R. Lupski, Stephen Jolles, Anja K. Bielinsky, and Jordan S. Orange. Human nk cell deficiency as a result of biallelic mutations in mcm10. Journal of Clinical Investigation, 130:5272-5286, Aug 2020. URL: https://doi.org/10.1172/jci134966, doi:10.1172/jci134966. This article has 79 citations and is from a highest quality peer-reviewed journal.

7. (mace2020humannkcell pages 3-4): Emily M. Mace, Silke Paust, Matilde I. Conte, Ryan M. Baxley, Megan M. Schmit, Sagar L. Patil, Nicole C. Guilz, Malini Mukherjee, Ashley E. Pezzi, Jolanta Chmielowiec, Swetha Tatineni, Ivan K. Chinn, Zeynep Coban Akdemir, Shalini N. Jhangiani, Donna M. Muzny, Asbjørg Stray-Pedersen, Rachel E. Bradley, Mo Moody, Philip P. Connor, Adrian G. Heaps, Colin Steward, Pinaki P. Banerjee, Richard A. Gibbs, Malgorzata Borowiak, James R. Lupski, Stephen Jolles, Anja K. Bielinsky, and Jordan S. Orange. Human nk cell deficiency as a result of biallelic mutations in mcm10. Journal of Clinical Investigation, 130:5272-5286, Aug 2020. URL: https://doi.org/10.1172/jci134966, doi:10.1172/jci134966. This article has 79 citations and is from a highest quality peer-reviewed journal.

8. (mace2020humannkcell pages 10-11): Emily M. Mace, Silke Paust, Matilde I. Conte, Ryan M. Baxley, Megan M. Schmit, Sagar L. Patil, Nicole C. Guilz, Malini Mukherjee, Ashley E. Pezzi, Jolanta Chmielowiec, Swetha Tatineni, Ivan K. Chinn, Zeynep Coban Akdemir, Shalini N. Jhangiani, Donna M. Muzny, Asbjørg Stray-Pedersen, Rachel E. Bradley, Mo Moody, Philip P. Connor, Adrian G. Heaps, Colin Steward, Pinaki P. Banerjee, Richard A. Gibbs, Malgorzata Borowiak, James R. Lupski, Stephen Jolles, Anja K. Bielinsky, and Jordan S. Orange. Human nk cell deficiency as a result of biallelic mutations in mcm10. Journal of Clinical Investigation, 130:5272-5286, Aug 2020. URL: https://doi.org/10.1172/jci134966, doi:10.1172/jci134966. This article has 79 citations and is from a highest quality peer-reviewed journal.

9. (mace2020humannkcell pages 9-10): Emily M. Mace, Silke Paust, Matilde I. Conte, Ryan M. Baxley, Megan M. Schmit, Sagar L. Patil, Nicole C. Guilz, Malini Mukherjee, Ashley E. Pezzi, Jolanta Chmielowiec, Swetha Tatineni, Ivan K. Chinn, Zeynep Coban Akdemir, Shalini N. Jhangiani, Donna M. Muzny, Asbjørg Stray-Pedersen, Rachel E. Bradley, Mo Moody, Philip P. Connor, Adrian G. Heaps, Colin Steward, Pinaki P. Banerjee, Richard A. Gibbs, Malgorzata Borowiak, James R. Lupski, Stephen Jolles, Anja K. Bielinsky, and Jordan S. Orange. Human nk cell deficiency as a result of biallelic mutations in mcm10. Journal of Clinical Investigation, 130:5272-5286, Aug 2020. URL: https://doi.org/10.1172/jci134966, doi:10.1172/jci134966. This article has 79 citations and is from a highest quality peer-reviewed journal.

10. (mace2020humannkcell pages 6-7): Emily M. Mace, Silke Paust, Matilde I. Conte, Ryan M. Baxley, Megan M. Schmit, Sagar L. Patil, Nicole C. Guilz, Malini Mukherjee, Ashley E. Pezzi, Jolanta Chmielowiec, Swetha Tatineni, Ivan K. Chinn, Zeynep Coban Akdemir, Shalini N. Jhangiani, Donna M. Muzny, Asbjørg Stray-Pedersen, Rachel E. Bradley, Mo Moody, Philip P. Connor, Adrian G. Heaps, Colin Steward, Pinaki P. Banerjee, Richard A. Gibbs, Malgorzata Borowiak, James R. Lupski, Stephen Jolles, Anja K. Bielinsky, and Jordan S. Orange. Human nk cell deficiency as a result of biallelic mutations in mcm10. Journal of Clinical Investigation, 130:5272-5286, Aug 2020. URL: https://doi.org/10.1172/jci134966, doi:10.1172/jci134966. This article has 79 citations and is from a highest quality peer-reviewed journal.

11. (schmit2024acriticalthreshold pages 5-6): Megan M. Schmit, Ryan M. Baxley, Liangjun Wang, Peter Hinderlie, Marissa Kaufman, Emily Simon, Anjali Raju, Jeffrey S. Miller, and Anja-Katrin Bielinsky. A critical threshold of mcm10 is required to maintain genome stability during differentiation of induced pluripotent stem cells into natural killer cells. Open Biology, Jan 2024. URL: https://doi.org/10.1098/rsob.230407, doi:10.1098/rsob.230407. This article has 9 citations and is from a peer-reviewed journal.

12. (schmit2024acriticalthreshold pages 1-2): Megan M. Schmit, Ryan M. Baxley, Liangjun Wang, Peter Hinderlie, Marissa Kaufman, Emily Simon, Anjali Raju, Jeffrey S. Miller, and Anja-Katrin Bielinsky. A critical threshold of mcm10 is required to maintain genome stability during differentiation of induced pluripotent stem cells into natural killer cells. Open Biology, Jan 2024. URL: https://doi.org/10.1098/rsob.230407, doi:10.1098/rsob.230407. This article has 9 citations and is from a peer-reviewed journal.

13. (schmit2024acriticalthreshold pages 8-9): Megan M. Schmit, Ryan M. Baxley, Liangjun Wang, Peter Hinderlie, Marissa Kaufman, Emily Simon, Anjali Raju, Jeffrey S. Miller, and Anja-Katrin Bielinsky. A critical threshold of mcm10 is required to maintain genome stability during differentiation of induced pluripotent stem cells into natural killer cells. Open Biology, Jan 2024. URL: https://doi.org/10.1098/rsob.230407, doi:10.1098/rsob.230407. This article has 9 citations and is from a peer-reviewed journal.

14. (caballero2021comprehensiveanalysisof pages 1-3): Madison Caballero, Tiffany Ge, Ana Rita Rebelo, Seungmae Seo, Sean Kim, Kayla Brooks, Michael Zuccaro, Radhakrishnan Kanagaraj, Dan Vershkov, Dongsung Kim, Agata Smogorzewska, Marcus Smolka, Nissim Benvenisty, Stephen C West, Dieter Egli, Emily M Mace, and Amnon Koren. Comprehensive analysis of dna replication timing in genetic diseases and gene knockouts identifies mcm10 as a novel regulator of the replication program. bioRxiv, Sep 2021. URL: https://doi.org/10.1101/2021.09.08.459433, doi:10.1101/2021.09.08.459433. This article has 1 citations.

15. (pagnamenta2023structuralandnoncoding pages 20-21): Alistair T. Pagnamenta, Carme Camps, Edoardo Giacopuzzi, John M. Taylor, Mona Hashim, Eduardo Calpena, Pamela J. Kaisaki, Akiko Hashimoto, Jing Yu, Edward Sanders, Ron Schwessinger, Jim R. Hughes, Gerton Lunter, Helene Dreau, Matteo Ferla, Lukas Lange, Yesim Kesim, Vassilis Ragoussis, Dimitrios V. Vavoulis, Holger Allroggen, Olaf Ansorge, Christian Babbs, Siddharth Banka, Benito Baños-Piñero, David Beeson, Tal Ben-Ami, David L. Bennett, Celeste Bento, Edward Blair, Charlotte Brasch-Andersen, Katherine R. Bull, Holger Cario, Deirdre Cilliers, Valerio Conti, E. Graham Davies, Fatima Dhalla, Beatriz Diez Dacal, Yin Dong, James E. Dunford, Renzo Guerrini, Adrian L. Harris, Jane Hartley, Georg Hollander, Kassim Javaid, Maureen Kane, Deirdre Kelly, Dominic Kelly, Samantha J. L. Knight, Alexandra Y. Kreins, Erika M. Kvikstad, Craig B. Langman, Tracy Lester, Kate E. Lines, Simon R. Lord, Xin Lu, Sahar Mansour, Adnan Manzur, Reza Maroofian, Brian Marsden, Joanne Mason, Simon J. McGowan, Davide Mei, Hana Mlcochova, Yoshiko Murakami, Andrea H. Németh, Steven Okoli, Elizabeth Ormondroyd, Lilian Bomme Ousager, Jacqueline Palace, Smita Y. Patel, Melissa M. Pentony, Chris Pugh, Aboulfazl Rad, Archana Ramesh, Simone G. Riva, Irene Roberts, Noémi Roy, Outi Salminen, Kyleen D. Schilling, Caroline Scott, Arjune Sen, Conrad Smith, Mark Stevenson, Rajesh V. Thakker, Stephen R. F. Twigg, Holm H. Uhlig, Richard van Wijk, Barbara Vona, Steven Wall, Jing Wang, Hugh Watkins, Jaroslav Zak, Anna H. Schuh, Usha Kini, Andrew O. M. Wilkie, Niko Popitsch, and Jenny C. Taylor. Structural and non-coding variants increase the diagnostic yield of clinical whole genome sequencing for rare diseases. Genome Medicine, Nov 2023. URL: https://doi.org/10.1186/s13073-023-01240-0, doi:10.1186/s13073-023-01240-0. This article has 82 citations and is from a highest quality peer-reviewed journal.

16. (guilz2023unwindingtherole pages 1-2): Nicole C. Guilz, Yong-Oon Ahn, Seungmae Seo, and Emily M. Mace. Unwinding the role of the cmg helicase in inborn errors of immunity. Journal of Clinical Immunology, pages 1-15, Feb 2023. URL: https://doi.org/10.1007/s10875-023-01437-3, doi:10.1007/s10875-023-01437-3. This article has 13 citations and is from a domain leading peer-reviewed journal.

17. (guilz2023unwindingtherole pages 9-11): Nicole C. Guilz, Yong-Oon Ahn, Seungmae Seo, and Emily M. Mace. Unwinding the role of the cmg helicase in inborn errors of immunity. Journal of Clinical Immunology, pages 1-15, Feb 2023. URL: https://doi.org/10.1007/s10875-023-01437-3, doi:10.1007/s10875-023-01437-3. This article has 13 citations and is from a domain leading peer-reviewed journal.

18. (guilz2023unwindingtherole pages 7-8): Nicole C. Guilz, Yong-Oon Ahn, Seungmae Seo, and Emily M. Mace. Unwinding the role of the cmg helicase in inborn errors of immunity. Journal of Clinical Immunology, pages 1-15, Feb 2023. URL: https://doi.org/10.1007/s10875-023-01437-3, doi:10.1007/s10875-023-01437-3. This article has 13 citations and is from a domain leading peer-reviewed journal.

19. (mace2020humannkcell pages 8-9): Emily M. Mace, Silke Paust, Matilde I. Conte, Ryan M. Baxley, Megan M. Schmit, Sagar L. Patil, Nicole C. Guilz, Malini Mukherjee, Ashley E. Pezzi, Jolanta Chmielowiec, Swetha Tatineni, Ivan K. Chinn, Zeynep Coban Akdemir, Shalini N. Jhangiani, Donna M. Muzny, Asbjørg Stray-Pedersen, Rachel E. Bradley, Mo Moody, Philip P. Connor, Adrian G. Heaps, Colin Steward, Pinaki P. Banerjee, Richard A. Gibbs, Malgorzata Borowiak, James R. Lupski, Stephen Jolles, Anja K. Bielinsky, and Jordan S. Orange. Human nk cell deficiency as a result of biallelic mutations in mcm10. Journal of Clinical Investigation, 130:5272-5286, Aug 2020. URL: https://doi.org/10.1172/jci134966, doi:10.1172/jci134966. This article has 79 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Immunodeficiency_80_with_or_without_Congenital_Cardiomyopathy-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.