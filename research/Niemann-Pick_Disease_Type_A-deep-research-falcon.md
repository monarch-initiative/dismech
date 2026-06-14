---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-13T13:12:59.911710'
end_time: '2026-06-13T13:23:12.215986'
duration_seconds: 612.3
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Niemann-Pick Disease Type A
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 38
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Niemann-Pick_Disease_Type_A-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Niemann-Pick Disease Type A
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Niemann-Pick Disease Type A** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
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
- **Disease Name:** Niemann-Pick Disease Type A
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Niemann-Pick Disease Type A** covering all of the
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

For each treatment, suggest MAXO (Medical Action Ontology) terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, MAXO, MONDO) where applicable
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
- Treatment annotations (MAXO terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


## Comprehensive Research Report: Niemann–Pick Disease Type A (Infantile Neurovisceral ASMD)

### Executive summary
Niemann–Pick disease type A (NPD-A) is the severe, infantile neurovisceral end of **acid sphingomyelinase deficiency (ASMD)**, a rare **autosomal recessive** lysosomal storage disorder caused by **biallelic loss-of-function variants in SMPD1**, resulting in profound **acid sphingomyelinase (ASM)** deficiency and lysosomal accumulation of sphingomyelin with downstream cellular and organ dysfunction. NPD-A typically presents in early infancy with hepatosplenomegaly and rapidly progressive neurodegeneration, with death usually in early childhood. Recent (2023–2024) developments relevant to real-world care include (i) publication of international consensus clinical management guidelines (2023), (ii) broader real-world implementation of **olipudase alfa** enzyme replacement therapy for **non-CNS manifestations** of ASMD (not curative for NPD-A neurodegeneration), and (iii) accelerating newborn screening pilots/algorithms incorporating **DBS ASM activity + LysoSM second-tier testing + SMPD1 sequencing**, with higher-than-clinically-recognized incidence estimates in some settings. (geberhiwot2023consensusclinicalmanagement pages 1-2, mauhin2024acidsphingomyelinasedeficiency pages 11-11, gragnaniello2024newbornscreeningfor pages 3-5, gragnaniello2024newbornscreeningfor pages 1-2)

| Domain | Key details | Evidence/source (with year) |
|---|---|---|
| Disease name / classification | Niemann–Pick disease type A = infantile neurovisceral acid sphingomyelinase deficiency (ASMD); severe neuronopathic end of the ASMD spectrum | 2023 consensus guidelines; 2024 pediatric ASMD review (geberhiwot2023consensusclinicalmanagement pages 1-2, geberhiwot2023consensusclinicalmanagement pages 2-4, lipinski2024chronicacidsphingomyelinase pages 1-2) |
| Identifiers | MONDO: MONDO:0009756 (Niemann-Pick disease type A); OMIM numbers cited in 2023 guidelines header for ASMD/Niemann–Pick types A/B: 257200 and 607616 | Open Targets disease mapping; 2023 guidelines (OpenTargets Search: Niemann-Pick disease type A-SMPD1, geberhiwot2023consensusclinicalmanagement pages 1-2) |
| Causative gene | SMPD1 (sphingomyelin phosphodiesterase 1); loss-of-function variants cause acid sphingomyelinase deficiency | 2023 guidelines; 2017 review (geberhiwot2023consensusclinicalmanagement pages 2-4, schuchman2017typesaand pages 1-3) |
| Inheritance | Autosomal recessive; biallelic pathogenic SMPD1 variants | 2023 guidelines; 2024 pediatric ASMD review (geberhiwot2023consensusclinicalmanagement pages 1-2, lipinski2024chronicacidsphingomyelinase pages 1-2) |
| Core biochemical defect | Deficient lysosomal acid sphingomyelinase (ASM) activity causes sphingomyelin accumulation with secondary lipid accumulation including cholesterol | 2023 guidelines; 2024 review (geberhiwot2023consensusclinicalmanagement pages 4-5, tirelli2024thegeneticbasis pages 1-3) |
| Hallmark early visceral features | Hepatosplenomegaly in early infancy; often presents at 2–4 months; splenomegaly is a key clue | 2017 burden review; 2023 guidelines (mcgovern2017diseasemanifestationsand pages 2-3, geberhiwot2023consensusclinicalmanagement pages 4-5) |
| Hallmark neurologic course / onset | Development may be initially normal, then psychomotor delay/regression begins in the first year; neurologic symptoms median ~7 months; regression often noted in the second 6 months of life | 2017 burden review; 2024 pediatric ASMD review (mcgovern2017diseasemanifestationsand pages 2-3, lipinski2024chronicacidsphingomyelinase pages 1-2) |
| Other common features | Cherry-red macula often present by 12 months; hypotonia, growth failure/failure to thrive, rapidly progressive neurodegeneration, respiratory involvement | 2017 burden review; 2024 review (mcgovern2017diseasemanifestationsand pages 2-3, tirelli2024thegeneticbasis pages 1-3) |
| Prognosis | Uniformly severe, rapidly progressive infantile disorder; patients rarely survive beyond 2–3 years | 2017 review; 2023 guidelines (schuchman2017typesaand pages 1-3, geberhiwot2023consensusclinicalmanagement pages 2-4) |
| Survival statistics (French cohort, 2024) | Type A cohort n=15; median age at symptom onset 6.0 months (3.0–18.0), diagnosis 8.0 months (1.0–18.0), death 1 year (0–3.6); median survival from birth 2.0 years (95% CI 1.8–2.7); mortality 14/15 (93.3%) at study cut-off | Mauhin et al., Orphanet J Rare Dis 2024 (mauhin2024acidsphingomyelinasedeficiency pages 1-2, mauhin2024acidsphingomyelinasedeficiency pages 3-5) |
| Population genetics / founder effect | Ashkenazi Jewish carrier frequency reported around 1:100–1:200, with estimated disease prevalence 1:40,000–1:200,000 in that population | 2023 guidelines (geberhiwot2023consensusclinicalmanagement pages 4-5) |
| Diagnostic enzyme testing | ASM activity can be measured in peripheral blood leukocytes/lymphocytes, cultured skin fibroblasts, or dried blood spots; marked deficiency supports diagnosis | 2017 review; 2024 review/guidance (mcgovern2017diseasemanifestationsand pages 2-3, alagia2024acidsphingomyelinasedeficiencya pages 26-27) |
| Diagnostic molecular testing | Confirmatory SMPD1 sequencing; NGS/Sanger used, with MLPA/WGS considered if needed | 2017 review; 2024 review/guidance (mcgovern2017diseasemanifestationsand pages 2-3, alagia2024acidsphingomyelinasedeficiency pages 26-27) |
| Biomarkers | Lyso-sphingomyelin (LysoSM) and LysoSM-509 are useful ASMD biomarkers; elevated in DBS and plasma and useful for screening/triage | 2024 Polish update; 2024 review/guidance (lipinski2024chronicacidsphingomyelinase pages 1-2, alagia2024acidsphingomyelinasedeficiencya pages 26-27) |
| Newborn screening algorithm (Italy) | First-tier DBS ASM activity by LC-MS/MS; monthly recalculated 0.2 MoM cutoff; second-tier LysoSM on same DBS; abnormal samples undergo SMPD1 genotyping | Gragnaniello et al., 2024 (gragnaniello2024newbornscreeningfor pages 3-5, gragnaniello2024newbornscreeningfor pages 5-6) |
| Newborn screening cutoff / abnormal biomarker | Italian NBS used LysoSM > 51.68 nmol/L as abnormal in second-tier testing | Gragnaniello et al., 2024 (gragnaniello2024newbornscreeningfor pages 3-5) |
| Newborn screening performance (Italy) | 275,011 newborns screened; 2 screen-positive/confirmed cases; estimated incidence 1:137,506; reported PPV 100% in study summary/table | Gragnaniello et al., 2024 (gragnaniello2024newbornscreeningfor pages 2-3, gragnaniello2024newbornscreeningfor pages 1-2) |
| 2023 care standard | First international consensus management guidelines published for ASMD, addressing diagnosis, multidisciplinary care, and standard-of-care gaps | Geberhiwot et al., 2023 (geberhiwot2023consensusclinicalmanagement pages 1-2) |
| Approved disease-modifying therapy | Olipudase alfa (Xenpozyme) is the first approved disease-modifying therapy for ASMD, but only for non-CNS manifestations; supportive care remains the mainstay for type A | 2024 review; 2023 guidelines; Mauhin 2024 reference summary (tirelli2024thegeneticbasis pages 1-3, geberhiwot2023consensusclinicalmanagement pages 1-2, mauhin2024acidsphingomyelinasedeficiency pages 11-11) |
| Why olipudase alfa is limited in type A | Enzyme replacement improves visceral disease but is limited by lack of meaningful CNS penetration/blood–brain barrier barrier, so infantile neurovisceral type A is not adequately addressed | 2024 reviews (naffadi2024neimannpickdiseasesbeyonda pages 6-7, naffadi2024neimannpickdiseasesbeyond pages 6-7) |
| Expanded access / real-world implementation | Compassionate-use olipudase alfa program for chronic ASMD: NCT04877132; excludes infantile-onset/genotype-compatible type A and includes type A/B or B patients with chronic disease | ClinicalTrials.gov expanded access (NCT04877132 chunk 1) |
| Pivotal adult olipudase trial | ASCEND trial NCT02004691: phase 2/3 randomized placebo-controlled adult study; 36 participants; primary endpoints included spleen volume by MRI and DLCO | ClinicalTrials.gov; 2024 review (NCT02004691 chunk 1, alagia2024acidsphingomyelinasedeficiencya pages 27-29) |
| Pediatric olipudase development | ASCEND-Peds / NCT02292654: phase 1/2 pediatric repeat-dose olipudase study; 20 participants | ClinicalTrials.gov registry summary (alagia2024acidsphingomyelinasedeficiencya pages 27-29) |
| Real-world early access study | OPERA France / NCT05359276: observational real-world cohort (n=40) evaluating lung, spleen, liver outcomes, safety, immunogenicity, biomarkers, and treatment-use patterns with olipudase alfa | ClinicalTrials.gov (NCT05359276 chunk 1) |
| Infant/toddler post-approval study | NCT06192576: real-world long-term safety and immunogenicity study of olipudase alfa in pediatric patients <2 years with ASMD | ClinicalTrials.gov (NCT06192576 chunk 2) |
| Research pipeline beyond ERT | Gene therapy is under active preclinical/early clinical investigation for ASMD because current ERT does not solve CNS disease in type A | 2024 reviews (naffadi2024neimannpickdiseasesbeyond pages 6-7) |


*Table: This table summarizes the most actionable disease-characteristics facts for Niemann–Pick disease type A, including identifiers, genetics, phenotype, prognosis, diagnostics, and 2023–2024 therapeutic/screening developments. It is designed for rapid knowledge-base population with source-linked evidence.*

---

## 1. Disease information

### 1.1 Definition and current understanding
**Niemann–Pick disease type A (NPD-A)** is historically one of the “Niemann–Pick types A and B,” but is now more precisely classified within **acid sphingomyelinase deficiency (ASMD)** because both type A and type B are caused by pathogenic variants in **SMPD1** encoding ASM. (schuchman2017typesaand pages 1-3)

Clinically, NPD-A represents a “fatal infantile neurovisceral disorder” on a continuum of ASMD phenotypes. (geberhiwot2023consensusclinicalmanagement pages 1-2)

### 1.2 Key identifiers and synonyms
- **Preferred umbrella term:** Acid sphingomyelinase deficiency (ASMD) (schuchman2017typesaand pages 1-3, geberhiwot2023consensusclinicalmanagement pages 1-2)
- **Synonyms/alternative names:** Niemann–Pick disease type A; infantile neurovisceral ASMD; acid sphingomyelinase deficiency type A (geberhiwot2023consensusclinicalmanagement pages 2-4, geberhiwot2023consensusclinicalmanagement pages 4-5)
- **MONDO ID:** **MONDO:0009756** (Open Targets mapping for “Niemann-Pick disease type A”) (OpenTargets Search: Niemann-Pick disease type A-SMPD1)
- **OMIM IDs:** The 2023 consensus guideline header cites **OMIM 257200 and 607616** for the ASMD/Niemann–Pick A/B disease spectrum. (geberhiwot2023consensusclinicalmanagement pages 1-2)

**Not found in the retrieved full-text evidence:** ICD-10/ICD-11 codes, MeSH identifiers, and Orphanet disease IDs were not explicitly extractable from the available excerpts; therefore, they are not asserted here.

### 1.3 Evidence source type
Most disease-level statements here derive from aggregated resources (international consensus guidelines, cohort studies, and reviews) rather than single EHR records. (geberhiwot2023consensusclinicalmanagement pages 1-2, mauhin2024acidsphingomyelinasedeficiency pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause (genetic/mechanistic):** NPD-A is caused by **biallelic pathogenic variants in SMPD1**, leading to severe deficiency of lysosomal **acid sphingomyelinase** activity. (geberhiwot2023consensusclinicalmanagement pages 2-4, geberhiwot2023consensusclinicalmanagement pages 4-5)

**Quote (guidelines):** ASMD is “a rare autosomal recessive disorder caused by pathogenic variants/mutations in the SMPD1 gene.” (geberhiwot2023consensusclinicalmanagement pages 1-2)

### 2.2 Risk factors
- **Genetic:** Carrier status for pathogenic SMPD1 variants; specific founder mutations drive higher population frequency in certain ancestries (see §9). (geberhiwot2023consensusclinicalmanagement pages 4-5)
- **Environmental:** No established environmental risk factors were identified in the retrieved evidence; NPD-A is a Mendelian, enzyme-deficiency disorder. (geberhiwot2023consensusclinicalmanagement pages 1-2)

### 2.3 Protective factors / gene–environment interactions
No validated protective factors or gene–environment interactions for NPD-A were identified in the retrieved 2023–2024 evidence.

---

## 3. Phenotypes (clinical features) with ontology suggestions

### 3.1 Core phenotype and onset
NPD-A is characterized by early visceral disease followed by rapidly progressive neurodegeneration in infancy.

**Early visceral presentation:** In a synthesis of ASMD manifestations, NPD-A infants “presented with hepatosplenomegaly at 2–4 months of age.” (mcgovern2017diseasemanifestationsand pages 2-3)

**Neurologic onset/progression:** Neurologic symptoms were reported as first detected around “a median age of 7 months,” with severe progressive neurodegeneration in the first year of life. (mcgovern2017diseasemanifestationsand pages 2-3)

**Ophthalmologic:** “Macular cherry-red spots were detectable in all infants by 12 months.” (mcgovern2017diseasemanifestationsand pages 2-3)

### 3.2 Suggested HPO terms (non-exhaustive)
(These are ontology mappings for knowledge-base structure; they are not claims of frequency unless stated.)
- Hepatosplenomegaly: **HP:0001433**
- Splenomegaly: **HP:0001744**
- Hepatomegaly: **HP:0002240**
- Failure to thrive: **HP:0001508**
- Developmental regression: **HP:0002376**
- Hypotonia: **HP:0001252**
- Cherry-red spot of the macula: **HP:0001103**
- Neurodegeneration: **HP:0002180**

### 3.3 Quality-of-life impact
The retrieved evidence emphasizes profound disability and rapid neurodegenerative decline in type A (fatal infantile course), implying major impact on feeding, respiration, neurodevelopment, and caregiver burden, though standardized QoL instruments were not found in the provided excerpts. (mcgovern2017diseasemanifestationsand pages 2-3, geberhiwot2023consensusclinicalmanagement pages 2-4)

---

## 4. Genetic / molecular information

### 4.1 Causal gene(s)
- **SMPD1** (sphingomyelin phosphodiesterase 1) is the causal gene; all types A and B “have mutations in the gene encoding ASM (SMPD1), and thus the disease is more accurately referred to as ASM deficiency (ASMD).” (schuchman2017typesaand pages 1-3)

### 4.2 Variant spectrum
The 2023 consensus guidelines note a large allelic heterogeneity with “over 250 SMPD1 variants” reported across ASMD. (geberhiwot2023consensusclinicalmanagement pages 2-4)

### 4.3 Functional consequence
The mechanistic consequence is loss of ASM enzymatic activity leading to storage of sphingomyelin and secondary lipids in lysosomes, with prominent involvement of monocyte/macrophage-lineage cells (lipid-laden macrophages) in organs such as liver and spleen. (geberhiwot2023consensusclinicalmanagement pages 4-5)

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
No specific modifier genes, epigenetic mechanisms, or large chromosomal abnormalities were extractable from the retrieved evidence excerpts.

---

## 5. Environmental information
NPD-A is not primarily driven by environmental or infectious causes in the retrieved evidence; it is an inherited lysosomal enzyme deficiency. (geberhiwot2023consensusclinicalmanagement pages 1-2)

---

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (upstream → downstream)
1) **Upstream trigger:** Biallelic SMPD1 loss-of-function variants (geberhiwot2023consensusclinicalmanagement pages 2-4)
2) **Primary biochemical defect:** Severe deficiency of lysosomal acid sphingomyelinase activity (geberhiwot2023consensusclinicalmanagement pages 4-5)
3) **Storage pathology:** Lysosomal accumulation of sphingomyelin and “secondary lipids (notably cholesterol)” (geberhiwot2023consensusclinicalmanagement pages 4-5)
4) **Cellular/tissue effects:** Lipid-laden “foam cells” and macrophage storage pathology across organs (mcgovern2017diseasemanifestationsand pages 2-3, geberhiwot2023consensusclinicalmanagement pages 4-5)
5) **Clinical manifestations:** Early hepatosplenomegaly (months), progressive neurologic deterioration (infancy), respiratory complications and early childhood mortality (mcgovern2017diseasemanifestationsand pages 2-3, geberhiwot2023consensusclinicalmanagement pages 2-4)

### 6.2 Cellular processes and suggested ontology terms
- Key subcellular compartment: **lysosome** (GO Cellular Component: GO:0005764)
- Key biological processes (suggested GO): **sphingomyelin catabolic process**, **lysosomal lipid catabolic process**, **macroautophagy/lysosomal stress responses** (ontology suggestions; mechanistic direction supported broadly by lysosomal storage biology referenced in ASMD reviews/guidelines). (geberhiwot2023consensusclinicalmanagement pages 4-5)
- Relevant cell types (suggested Cell Ontology, CL): **macrophage (CL:0000235)**, consistent with prominent storage in monocyte/macrophage-lineage cells described in guidelines. (geberhiwot2023consensusclinicalmanagement pages 4-5)

### 6.3 Why current ERT does not resolve neurologic disease
Recent reviews emphasize that enzyme replacement therapy can improve visceral storage but is limited by inadequate CNS delivery: “overcoming the blood brain barrier to ensure sufficient enzyme penetration remains a hurdle.” (naffadi2024neimannpickdiseasesbeyonda pages 6-7)

---

## 7. Anatomical structures affected

### 7.1 Organ-level involvement
Commonly involved organs in ASMD (including type A) include liver, spleen, lungs, bone marrow, and (in severe cases) neurons/CNS. (mcgovern2017diseasemanifestationsand pages 2-3, geberhiwot2023consensusclinicalmanagement pages 4-5)

### 7.2 Suggested UBERON terms (non-exhaustive)
- Liver: **UBERON:0002107**
- Spleen: **UBERON:0002106**
- Lung: **UBERON:0002048**
- Brain: **UBERON:0000955**

### 7.3 Subcellular localization
Primary pathological compartment: lysosomes (GO:0005764). (geberhiwot2023consensusclinicalmanagement pages 4-5)

---

## 8. Temporal development (natural history)

### 8.1 Onset
NPD-A onset is in infancy with early visceromegaly; symptom onset in the French cohort was median 6.0 months. (mauhin2024acidsphingomyelinasedeficiency pages 3-5)

### 8.2 Progression
Progression is rapidly neurodegenerative. The 2023 consensus describes type A as “rapidly progressive and neurodegenerative,” with deaths often by ~3 years. (geberhiwot2023consensusclinicalmanagement pages 2-4)

---

## 9. Inheritance and population

### 9.1 Inheritance
ASMD/NPD-A is **autosomal recessive**. (geberhiwot2023consensusclinicalmanagement pages 1-2, lipinski2024chronicacidsphingomyelinase pages 1-2)

### 9.2 Prevalence / incidence estimates
- The 2023 consensus guidelines cite an estimated global prevalence on the order of **~1:100,000–1,000,000 births** (broad range reflecting rarity and ascertainment limitations). (geberhiwot2023consensusclinicalmanagement pages 2-4)
- **Newborn screening incidence estimate (Italy, 2015–2024):** 275,011 newborns screened; **2** biochemically and genetically supported cases; estimated incidence **1 in 137,506**. (gragnaniello2024newbornscreeningfor pages 1-2)

### 9.3 Founder effects / population-specific frequencies
- **Ashkenazi Jewish population:** 2023 consensus excerpt cites carrier frequency “~1:100–1:200” with estimated disease prevalence “~1:40,000–1:200,000.” (geberhiwot2023consensusclinicalmanagement pages 4-5)
- **Japan (genome-resource-based estimates, 2024):** Estimated carrier frequency **1/180** and estimated disease occurrence frequency **1/128,191** in Japanese individuals based on 54KJPN (jMorp; 54,302 individuals) and gnomAD v4.0.0 comparisons. (sako2024allelefrequencyof pages 1-2)

**Quote (Japan underdiagnosis interpretation):** “Our data also suggest that there are more patients with a milder form of ASMD and nonspeciﬁc clinical ﬁndings who have not yet been diagnosed.” (sako2024allelefrequencyof pages 1-2)

---

## 10. Diagnostics

### 10.1 Core diagnostic tests
1) **Enzyme assay:** ASM activity measurement in leukocytes/lymphocytes or cultured fibroblasts; ASM activity can also be measured in dried blood spots (DBS). (mcgovern2017diseasemanifestationsand pages 2-3, alagia2024acidsphingomyelinasedeficiencya pages 26-27)
2) **Molecular confirmation:** SMPD1 sequencing; guidelines and reviews emphasize genetic confirmation. (mcgovern2017diseasemanifestationsand pages 2-3, alagia2024acidsphingomyelinasedeficiency pages 26-27)
3) **Biomarkers:** Lyso-sphingomyelin (LysoSM) and LysoSM-509 elevated in DBS/plasma; used as screening and monitoring biomarkers. (lipinski2024chronicacidsphingomyelinase pages 1-2, alagia2024acidsphingomyelinasedeficiencya pages 26-27)

### 10.2 Screening and newborn screening algorithms (recent)
**Italy newborn screening protocol (publication date Dec 2024; https://doi.org/10.3390/ijns10040079):**
- First-tier: DBS ASM activity by LC–MS/MS (NeoLSD® assay), cutoff recalculated monthly (0.2 MoM). (gragnaniello2024newbornscreeningfor pages 3-5)
- Second-tier: LysoSM quantification on the same DBS; “LysoSM > 51.68 nmol/L considered abnormal.” (gragnaniello2024newbornscreeningfor pages 3-5)
- Third-tier/confirmation: SMPD1 genotyping via NGS of exons and exon–intron boundaries. (gragnaniello2024newbornscreeningfor pages 3-5)

### 10.3 Differential diagnosis
The retrieved excerpts emphasize that ASMD can be misdiagnosed/delayed due to heterogeneity and overlap with other causes of hepatosplenomegaly and storage pathology, but specific differential diagnosis lists were not extractable from the available guideline pages. (geberhiwot2023consensusclinicalmanagement pages 1-2)

---

## 11. Outcomes / prognosis

### 11.1 Survival statistics (recent cohort data)
**France retrospective survival study (Orphanet J Rare Dis; Aug 2024; https://doi.org/10.1186/s13023-024-03234-6):**
- Type A sample: **n=15** medical records. (mauhin2024acidsphingomyelinasedeficiency pages 1-2)
- “Median [range] age at diagnosis was **8.0 [1.0–18.0] months (type A)**.” (mauhin2024acidsphingomyelinasedeficiency pages 1-2)
- “The median [range] age at death for patients with ASMD type A (n = 14) was **1 [0–3.6] year**.” (mauhin2024acidsphingomyelinasedeficiency pages 1-2)
- “The median [95% CI] survival age from birth in patients with ASMD type A… was **2.0 [1.8–2.7] years**.” (mauhin2024acidsphingomyelinasedeficiency pages 1-2)
- Mortality burden: **14/15 (93.3%)** at study cut-off. (mauhin2024acidsphingomyelinasedeficiency pages 3-5)

These statistics are consistent with earlier aggregated summaries that NPD-A “rarely survive beyond 2–3 years of age.” (schuchman2017typesaand pages 1-3)

---

## 12. Treatment

### 12.1 Supportive care (current standard for NPD-A)
The 2023 consensus guidelines emphasize that **supportive symptomatic care remains the mainstay** of management “definitely in those with type A,” reflecting the lack of disease-modifying CNS-directed therapy. (geberhiwot2023consensusclinicalmanagement pages 1-2)

Suggested MAXO terms (supportive care concepts; non-exhaustive): nutritional support, respiratory support, palliative care, physical therapy.

### 12.2 Enzyme replacement therapy (ERT): olipudase alfa (Xenpozyme)
**State of the art (2023–2024):** Olipudase alfa is described as the **first approved disease-modifying therapy for ASMD**, but approvals and clinical trials primarily address **non-CNS manifestations** (visceral/lung). (tirelli2024thegeneticbasis pages 1-3, mauhin2024acidsphingomyelinasedeficiency pages 11-11)

**Real-world implementations / programs and trials (ClinicalTrials.gov):**
- **ASCEND pivotal adult trial:** NCT02004691 (Phase 2/3; randomized placebo-controlled; 36 adults; endpoints included spleen volume by MRI and DLCO; results posted 2022-05-24). (NCT02004691 chunk 1)
- **Expanded access / compassionate use:** NCT04877132 (first posted 2021-05-07; last update 2022-09-19). Notably, it **excludes** “infantile-onset ASMD (genotype compatible with ASMD type A)” and targets chronic disease populations. (NCT04877132 chunk 1)
- **Real-world early access cohort (France):** NCT05359276 (OPERA; observational; enrolled 40; start 2022-06-10; primary outcomes include change in DLCO, spleen size, liver size at 24 months; includes biomarkers such as lysosphingomyelin). (NCT05359276 chunk 1)
- **Post-approval very young pediatrics:** NCT06192576 (real-world long-term safety and immunogenicity in ASMD patients <2 years; Sanofi; data access via Vivli). (NCT06192576 chunk 2)

### 12.3 Why ERT is not a complete solution for NPD-A
The major limitation for NPD-A is CNS disease, because systemic enzyme does not adequately cross the blood–brain barrier; recent reviews highlight that BBB penetration “remains a hurdle.” (naffadi2024neimannpickdiseasesbeyonda pages 6-7)

### 12.4 Emerging/experimental approaches
Recent reviews emphasize active investigation of **gene therapy** approaches (preclinical and early clinical efforts) as a potential strategy to address limitations of systemic ERT for neuronopathic disease. (naffadi2024neimannpickdiseasesbeyond pages 6-7)

---

## 13. Prevention
For autosomal recessive Mendelian disorders such as NPD-A, prevention is primarily through **carrier detection and reproductive options** (e.g., prenatal diagnosis). Prenatal diagnosis is referenced in ASMD clinical literature as feasible via enzymatic and molecular analysis (e.g., chorionic villi approaches are discussed in ASMD diagnostic context). (mcgovern2017diseasemanifestationsand pages 2-3)

---

## 14. Other species / natural disease
No naturally occurring veterinary NPD-A evidence was extractable from the retrieved evidence excerpts.

---

## 15. Model organisms
The retrieved evidence excerpts did not provide detailed, citable descriptions of specific ASMD/NPD-A animal models (e.g., Smpd1 knockout mouse phenotypes) beyond general statements that gene therapy is being investigated in animals. (naffadi2024neimannpickdiseasesbeyond pages 6-7)

---

## Recent developments and expert analysis (prioritizing 2023–2024)

1) **International consensus guidelines (2023):** First international consensus clinical management guidelines for ASMD were developed using systematic review and structured guideline methods (AGREE II / GRADE/Delphi), explicitly aiming to reduce misdiagnosis and standardize multidisciplinary care. This is a key authoritative source for “expert opinion” statements in an ultra-rare disease with limited RCT evidence. (geberhiwot2023consensusclinicalmanagement pages 1-2, geberhiwot2023consensusclinicalmanagement pages 2-4)

2) **New survival data (2024):** The French retrospective survival study quantifies NPD-A mortality and survival distribution in a national multi-hospital sample, including median survival from birth of ~2 years. (mauhin2024acidsphingomyelinasedeficiency pages 1-2)

3) **Newborn screening evidence (2024):** The Italian NBS study demonstrates feasibility of a two-tier biochemical algorithm (ASM activity + LysoSM) plus SMPD1 sequencing, yielding an estimated incidence (1:137,506) that the authors interpret as potentially higher than clinically reported. (gragnaniello2024newbornscreeningfor pages 1-2)

4) **Population-genetic incidence estimates (2024):** Japanese genome-resource aggregation suggests higher-than-expected carrier frequency and predicted disease frequency, supporting the expert view that ASMD may be underdiagnosed, particularly in milder phenotypes. (sako2024allelefrequencyof pages 1-2)

5) **Therapeutic era shift (2023–2024):** Olipudase alfa implementation has moved beyond pivotal trials into expanded access and real-world cohorts, focusing on visceral/lung endpoints and immunogenicity monitoring—while consensus documents still emphasize supportive care for NPD-A due to CNS limitations. (geberhiwot2023consensusclinicalmanagement pages 1-2, NCT05359276 chunk 1, NCT04877132 chunk 1)

---

## Reference URLs and dates (from retrieved sources)
- Geberhiwot et al. “Consensus clinical management guidelines for acid sphingomyelinase deficiency…” **Orphanet Journal of Rare Diseases**, **Apr 2023**. https://doi.org/10.1186/s13023-023-02686-6 (geberhiwot2023consensusclinicalmanagement pages 1-2)
- Mauhin et al. “Acid sphingomyelinase deficiency in France: a retrospective survival study” **Orphanet Journal of Rare Diseases**, **Aug 2024**. https://doi.org/10.1186/s13023-024-03234-6 (mauhin2024acidsphingomyelinasedeficiency pages 1-2)
- Gragnaniello et al. “Newborn Screening for Acid Sphingomyelinase Deficiency…” **International Journal of Neonatal Screening**, **Dec 2024**. https://doi.org/10.3390/ijns10040079 (gragnaniello2024newbornscreeningfor pages 1-2)
- Sako et al. “Allele frequency of pathogenic variants causing acid sphingomyelinase deficiency…” **Human Genome Variation**, **Jun 2024**. https://doi.org/10.1038/s41439-024-00282-z (sako2024allelefrequencyof pages 1-2)
- ClinicalTrials.gov records: NCT02004691, NCT04877132, NCT05359276, NCT06192576. https://clinicaltrials.gov/ (NCT02004691 chunk 1, NCT04877132 chunk 1, NCT05359276 chunk 1, NCT06192576 chunk 2)

---

## Limitations of this report (evidence availability)
Several template fields (ICD-10/ICD-11/MeSH/Orphanet IDs, comprehensive differential diagnosis lists, detailed model-organism phenotypes, and a structured treatment algorithm specific to type A beyond supportive care) were not explicitly present in the retrieved full-text excerpts; they are therefore not asserted beyond what is directly supported by citations above. (geberhiwot2023consensusclinicalmanagement pages 1-2)

References

1. (geberhiwot2023consensusclinicalmanagement pages 1-2): Tarekegn Geberhiwot, Melissa Wasserstein, Subadra Wanninayake, Shaun Christopher Bolton, Andrea Dardis, Anna Lehman, Olivier Lidove, Charlotte Dawson, Roberto Giugliani, Jackie Imrie, Justin Hopkin, James Green, Daniel de Vicente Corbeira, Shyam Madathil, Eugen Mengel, Fatih Ezgü, Magali Pettazzoni, Barbara Sjouke, Carla Hollak, Marie T. Vanier, Margaret McGovern, and Edward Schuchman. Consensus clinical management guidelines for acid sphingomyelinase deficiency (niemann–pick disease types a, b and a/b). Orphanet Journal of Rare Diseases, Apr 2023. URL: https://doi.org/10.1186/s13023-023-02686-6, doi:10.1186/s13023-023-02686-6. This article has 105 citations and is from a peer-reviewed journal.

2. (mauhin2024acidsphingomyelinasedeficiency pages 11-11): Wladimir Mauhin, Nathalie Guffon, Marie T. Vanier, Roseline Froissart, Aline Cano, Claire Douillard, Christian Lavigne, Bénédicte Héron, Nadia Belmatoug, Yurdagül Uzunhan, Didier Lacombe, Thierry Levade, Aymeric Duvivier, Ruth Pulikottil-Jacob, Fernando Laredo, Samia Pichard, Olivier Lidove, Marie-Thérèse Abi-Wardé, Marc Berger, Emilie Berthoux, Aurélie Cabannes-Hamy, Fabrice Camou, Pascal Cathebras, Vincent Grobost, Jérémy Keraen, Alice Kuster, Bertrand Lioger, Anas Mehdaoui, Claire Merlot, Martin Michaud, Martine-Louise Reynaud-Gaubert, Fréderic Schlemmer, Amélie Servettaz, Chloé Stavris, and Sébastien Trouillier. Acid sphingomyelinase deficiency in france: a retrospective survival study. Orphanet Journal of Rare Diseases, Aug 2024. URL: https://doi.org/10.1186/s13023-024-03234-6, doi:10.1186/s13023-024-03234-6. This article has 10 citations and is from a peer-reviewed journal.

3. (gragnaniello2024newbornscreeningfor pages 3-5): Vincenza Gragnaniello, Chiara Cazzorla, Daniela Gueraldi, Christian Loro, Elena Porcù, Leonardo Salviati, Alessandro P. Burlina, and Alberto B. Burlina. Newborn screening for acid sphingomyelinase deficiency: prevalence and genotypic findings in italy. International Journal of Neonatal Screening, 10:79, Dec 2024. URL: https://doi.org/10.3390/ijns10040079, doi:10.3390/ijns10040079. This article has 4 citations.

4. (gragnaniello2024newbornscreeningfor pages 1-2): Vincenza Gragnaniello, Chiara Cazzorla, Daniela Gueraldi, Christian Loro, Elena Porcù, Leonardo Salviati, Alessandro P. Burlina, and Alberto B. Burlina. Newborn screening for acid sphingomyelinase deficiency: prevalence and genotypic findings in italy. International Journal of Neonatal Screening, 10:79, Dec 2024. URL: https://doi.org/10.3390/ijns10040079, doi:10.3390/ijns10040079. This article has 4 citations.

5. (geberhiwot2023consensusclinicalmanagement pages 2-4): Tarekegn Geberhiwot, Melissa Wasserstein, Subadra Wanninayake, Shaun Christopher Bolton, Andrea Dardis, Anna Lehman, Olivier Lidove, Charlotte Dawson, Roberto Giugliani, Jackie Imrie, Justin Hopkin, James Green, Daniel de Vicente Corbeira, Shyam Madathil, Eugen Mengel, Fatih Ezgü, Magali Pettazzoni, Barbara Sjouke, Carla Hollak, Marie T. Vanier, Margaret McGovern, and Edward Schuchman. Consensus clinical management guidelines for acid sphingomyelinase deficiency (niemann–pick disease types a, b and a/b). Orphanet Journal of Rare Diseases, Apr 2023. URL: https://doi.org/10.1186/s13023-023-02686-6, doi:10.1186/s13023-023-02686-6. This article has 105 citations and is from a peer-reviewed journal.

6. (lipinski2024chronicacidsphingomyelinase pages 1-2): Patryk Lipiński, Agnieszka Ługowska, and Anna Tylki-Szymańska. Chronic acid sphingomyelinase deficiency diagnosed in infancy/childhood in polish patients: 2024 update. Advances in clinical and experimental medicine : official organ Wroclaw Medical University, 33:1163-1168, Oct 2024. URL: https://doi.org/10.17219/acem/193696, doi:10.17219/acem/193696. This article has 1 citations.

7. (OpenTargets Search: Niemann-Pick disease type A-SMPD1): Open Targets Query (Niemann-Pick disease type A-SMPD1, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

8. (schuchman2017typesaand pages 1-3): Edward H. Schuchman and Robert J. Desnick. Types a and b niemann-pick disease. Molecular genetics and metabolism, 120 1-2:27-33, Jan 2017. URL: https://doi.org/10.1016/j.ymgme.2016.12.008, doi:10.1016/j.ymgme.2016.12.008. This article has 412 citations and is from a peer-reviewed journal.

9. (geberhiwot2023consensusclinicalmanagement pages 4-5): Tarekegn Geberhiwot, Melissa Wasserstein, Subadra Wanninayake, Shaun Christopher Bolton, Andrea Dardis, Anna Lehman, Olivier Lidove, Charlotte Dawson, Roberto Giugliani, Jackie Imrie, Justin Hopkin, James Green, Daniel de Vicente Corbeira, Shyam Madathil, Eugen Mengel, Fatih Ezgü, Magali Pettazzoni, Barbara Sjouke, Carla Hollak, Marie T. Vanier, Margaret McGovern, and Edward Schuchman. Consensus clinical management guidelines for acid sphingomyelinase deficiency (niemann–pick disease types a, b and a/b). Orphanet Journal of Rare Diseases, Apr 2023. URL: https://doi.org/10.1186/s13023-023-02686-6, doi:10.1186/s13023-023-02686-6. This article has 105 citations and is from a peer-reviewed journal.

10. (tirelli2024thegeneticbasis pages 1-3): Claudio Tirelli, Ornella Rondinone, Marta Italia, Sabrina Mira, Luca Alessandro Belmonte, Mauro De Grassi, Gabriele Guido, Sara Maggioni, Michele Mondoni, Monica Rosa Miozzo, and Stefano Centanni. The genetic basis, lung involvement, and therapeutic options in niemann–pick disease: a comprehensive review. Biomolecules, 14:211, Feb 2024. URL: https://doi.org/10.3390/biom14020211, doi:10.3390/biom14020211. This article has 35 citations.

11. (mcgovern2017diseasemanifestationsand pages 2-3): Margaret M. McGovern, Ruzan Avetisyan, Bernd-Jan Sanson, and Olivier Lidove. Disease manifestations and burden of illness in patients with acid sphingomyelinase deficiency (asmd). Orphanet Journal of Rare Diseases, Feb 2017. URL: https://doi.org/10.1186/s13023-017-0572-x, doi:10.1186/s13023-017-0572-x. This article has 220 citations and is from a peer-reviewed journal.

12. (mauhin2024acidsphingomyelinasedeficiency pages 1-2): Wladimir Mauhin, Nathalie Guffon, Marie T. Vanier, Roseline Froissart, Aline Cano, Claire Douillard, Christian Lavigne, Bénédicte Héron, Nadia Belmatoug, Yurdagül Uzunhan, Didier Lacombe, Thierry Levade, Aymeric Duvivier, Ruth Pulikottil-Jacob, Fernando Laredo, Samia Pichard, Olivier Lidove, Marie-Thérèse Abi-Wardé, Marc Berger, Emilie Berthoux, Aurélie Cabannes-Hamy, Fabrice Camou, Pascal Cathebras, Vincent Grobost, Jérémy Keraen, Alice Kuster, Bertrand Lioger, Anas Mehdaoui, Claire Merlot, Martin Michaud, Martine-Louise Reynaud-Gaubert, Fréderic Schlemmer, Amélie Servettaz, Chloé Stavris, and Sébastien Trouillier. Acid sphingomyelinase deficiency in france: a retrospective survival study. Orphanet Journal of Rare Diseases, Aug 2024. URL: https://doi.org/10.1186/s13023-024-03234-6, doi:10.1186/s13023-024-03234-6. This article has 10 citations and is from a peer-reviewed journal.

13. (mauhin2024acidsphingomyelinasedeficiency pages 3-5): Wladimir Mauhin, Nathalie Guffon, Marie T. Vanier, Roseline Froissart, Aline Cano, Claire Douillard, Christian Lavigne, Bénédicte Héron, Nadia Belmatoug, Yurdagül Uzunhan, Didier Lacombe, Thierry Levade, Aymeric Duvivier, Ruth Pulikottil-Jacob, Fernando Laredo, Samia Pichard, Olivier Lidove, Marie-Thérèse Abi-Wardé, Marc Berger, Emilie Berthoux, Aurélie Cabannes-Hamy, Fabrice Camou, Pascal Cathebras, Vincent Grobost, Jérémy Keraen, Alice Kuster, Bertrand Lioger, Anas Mehdaoui, Claire Merlot, Martin Michaud, Martine-Louise Reynaud-Gaubert, Fréderic Schlemmer, Amélie Servettaz, Chloé Stavris, and Sébastien Trouillier. Acid sphingomyelinase deficiency in france: a retrospective survival study. Orphanet Journal of Rare Diseases, Aug 2024. URL: https://doi.org/10.1186/s13023-024-03234-6, doi:10.1186/s13023-024-03234-6. This article has 10 citations and is from a peer-reviewed journal.

14. (alagia2024acidsphingomyelinasedeficiencya pages 26-27): M ALAGIA, E CIRILLO, and A TARALLO. Acid sphingomyelinase deficiency: a complex and rare disorder that needs clinicians'awareness. Unknown journal, 2024.

15. (alagia2024acidsphingomyelinasedeficiency pages 26-27): M ALAGIA, E CIRILLO, and A TARALLO. Acid sphingomyelinase deficiency: a complex and rare disorder that needs clinicians'awareness. Unknown journal, 2024.

16. (gragnaniello2024newbornscreeningfor pages 5-6): Vincenza Gragnaniello, Chiara Cazzorla, Daniela Gueraldi, Christian Loro, Elena Porcù, Leonardo Salviati, Alessandro P. Burlina, and Alberto B. Burlina. Newborn screening for acid sphingomyelinase deficiency: prevalence and genotypic findings in italy. International Journal of Neonatal Screening, 10:79, Dec 2024. URL: https://doi.org/10.3390/ijns10040079, doi:10.3390/ijns10040079. This article has 4 citations.

17. (gragnaniello2024newbornscreeningfor pages 2-3): Vincenza Gragnaniello, Chiara Cazzorla, Daniela Gueraldi, Christian Loro, Elena Porcù, Leonardo Salviati, Alessandro P. Burlina, and Alberto B. Burlina. Newborn screening for acid sphingomyelinase deficiency: prevalence and genotypic findings in italy. International Journal of Neonatal Screening, 10:79, Dec 2024. URL: https://doi.org/10.3390/ijns10040079, doi:10.3390/ijns10040079. This article has 4 citations.

18. (naffadi2024neimannpickdiseasesbeyonda pages 6-7): HM Naffadi. Neimann-pick diseases: beyond lipid accumulation–genetic, diagnostics, and therapeutic strategies. Unknown journal, 2024.

19. (naffadi2024neimannpickdiseasesbeyond pages 6-7): HM Naffadi. Neimann-pick diseases: beyond lipid accumulation–genetic, diagnostics, and therapeutic strategies. Unknown journal, 2024.

20. (NCT04877132 chunk 1):  Compassionate Use Program for Olipudase Alfa Enzyme Replacement Therapy for Patients With Chronic Acid Sphingomyelinase Deficiency (ASMD). Sanofi. ClinicalTrials.gov Identifier: NCT04877132

21. (NCT02004691 chunk 1):  Efficacy, Safety, Pharmacodynamic, and Pharmacokinetics Study of Olipudase Alfa in Patients With Acid Sphingomyelinase Deficiency. Genzyme, a Sanofi Company. 2015. ClinicalTrials.gov Identifier: NCT02004691

22. (alagia2024acidsphingomyelinasedeficiencya pages 27-29): M ALAGIA, E CIRILLO, and A TARALLO. Acid sphingomyelinase deficiency: a complex and rare disorder that needs clinicians'awareness. Unknown journal, 2024.

23. (NCT05359276 chunk 1):  Data Analysis of Adult and Pediatric Participants With Acid Sphingomyelinase Deficiency (ASMD) on Early Access to Olipudase Alfa in France. Sanofi. 2022. ClinicalTrials.gov Identifier: NCT05359276

24. (NCT06192576 chunk 2):  A Real-world Long-term Safety and Immunogenicity Study of Olipudase Alfa Therapy in Pediatric Patients Less Than 2 Years of Age With Acid Sphingomyelinase Deficiency (ASMD). Sanofi. 2024. ClinicalTrials.gov Identifier: NCT06192576

25. (sako2024allelefrequencyof pages 1-2): Shuhei Sako, Kimihiko Oishi, Hiroyuki Ida, and Eri Imagawa. Allele frequency of pathogenic variants causing acid sphingomyelinase deficiency and gaucher disease in the general japanese population. Human Genome Variation, Jun 2024. URL: https://doi.org/10.1038/s41439-024-00282-z, doi:10.1038/s41439-024-00282-z. This article has 3 citations.

## Artifacts

- [Edison artifact artifact-00](Niemann-Pick_Disease_Type_A-deep-research-falcon_artifacts/artifact-00.md)