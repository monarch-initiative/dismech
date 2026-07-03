---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-19T18:16:40.141026'
end_time: '2026-06-19T18:33:15.101102'
duration_seconds: 994.96
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: POEMS Syndrome
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: POEMS_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: POEMS_Syndrome-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: POEMS_Syndrome-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** POEMS Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **POEMS Syndrome** covering all of the
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
- **Disease Name:** POEMS Syndrome
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **POEMS Syndrome** covering all of the
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


# Comprehensive Research Report on POEMS Syndrome

## 1. Disease Information

**Disease Name:** POEMS Syndrome (Polyneuropathy, Organomegaly, Endocrinopathy, M-protein, and Skin changes)

**Alternative Names:** Crow-Fukase syndrome, Takatsuki syndrome, PEP syndrome, osteosclerotic myeloma

**What is POEMS Syndrome?**
POEMS syndrome is a rare, chronic, disabling multisystem paraneoplastic disorder associated with an underlying plasma cell neoplasm (cerri2019anupdateon pages 1-2, keddie2025poemssyndrome pages 1-4). The disease is characterized by peripheral neuropathy, organomegaly, endocrinopathy, monoclonal plasma cell disorder, and skin changes, along with additional features including elevated vascular endothelial growth factor (VEGF), osteosclerotic bone lesions, Castleman disease, and extravascular volume overload (cerri2019anupdateon pages 1-2, keddie2025poemssyndrome pages 1-4, keddie2025poemssyndrome pages 4-7).

**Key Identifiers:**
While specific OMIM, Orphanet, and ICD codes were not directly confirmed in the retrieved literature, the disease is well-established in the International Myeloma Working Group diagnostic criteria framework (chen2021ahighlyheterogeneous pages 1-2, chen2021ahighlyheterogeneous pages 2-4). The information is derived from aggregated disease-level resources including major clinical cohorts and expert consensus reviews rather than individual EHR-level patient data (keddie2025poemssyndrome pages 1-4, keddie2025poemssyndrome pages 4-7).

## 2. Etiology

**Disease Causal Factors:**
POEMS syndrome is fundamentally a paraneoplastic disorder driven by an underlying plasma cell neoplasm (cerri2019anupdateon pages 1-2). The causative lesion is a monoclonal plasma cell proliferation that is typically of low tumor burden, with median bone marrow plasma cell percentage of 1.5% (range 0-10%) in one genomic cohort (chen2021ahighlyheterogeneous pages 2-4).

**Genetic Risk Factors:**
- **Lambda Light Chain Restriction:** Over 95% of cases demonstrate lambda (λ) light chain restriction, making this a near-universal feature (keddie2025poemssyndrome pages 1-4, keddie2025poemssyndrome pages 4-7, chen2021ahighlyheterogeneous pages 2-4, latov2014diagnosisandtreatment pages 1-2).
- **Restricted Immunoglobulin Gene Usage:** The monoclonal plasma cells show restricted usage of immunoglobulin λ light chain variable region (IGLV) genes, strictly derived from IGLV 1-40 and IGLV 1-44, suggesting antigenic affinity maturation (keddie2025poemssyndrome pages 1-4).
- **Cytogenetic Abnormalities:** Common abnormalities include aneuploidy (monosomy 13, trisomy 3 and 7), 14q32 (IGH) translocations (observed in approximately half of patients), and 13q14 deletions, similar to other plasma cell dyscrasias (keddie2025poemssyndrome pages 1-4, chen2021ahighlyheterogeneous pages 2-4).
- **Somatic Mutations:** Whole exome sequencing of bone marrow plasma cells identified significantly mutated genes including HEATR9 (20% of patients), LILRB1 (10%), and FMNL2 (10%), as well as cancer driver genes MYD88, NFKB2, CHD4, SH2B3, POLE, STAT3, CHD3, and CUX1 (10% each in the WES cohort). Target region sequencing of additional patients identified recurrently mutated genes including CUX1 (19%), DNAH5 (16%), USH2A (16%), KMT2D (16%), and RYR1 (12%) (chen2021ahighlyheterogeneous pages 2-4, chen2021ahighlyheterogeneous pages 4-5).

**Environmental and Other Risk Factors:**
No specific environmental risk factors have been definitively identified. The disease typically manifests in the fifth or sixth decade of life with a male predominance of approximately 2.5:1 (keddie2025poemssyndrome pages 1-4).

## 3. Phenotypes

A comprehensive table of clinical phenotypes is presented below:

| Phenotype category | Specific manifestations/features | Frequency/prevalence among patients | Clinical significance | Suggested HPO terms |
|---|---|---|---|---|
| Polyneuropathy | Symmetrical, sensorimotor, length-dependent, painful demyelinating polyneuropathy/radiculoneuropathy; striking distal weakness of hands/feet; lower-extremity numbness common; neuropathic pain especially in legs; often initially misdiagnosed as CIDP; electrophysiology shows uniform demyelination with marked secondary axonal loss, fewer conduction blocks, more severe lower-limb CMAP loss (wang2019clinicalandelectrophysiological pages 1-2, cerri2019anupdateon pages 1-2, cerri2019anupdateon pages 2-3, keddie2025poemssyndrome pages 4-7, wang2019clinicalandelectrophysiological pages 2-3) | Mandatory criterion; present in essentially 100% of classic POEMS cohorts in reviewed papers; 42/42 (100%) in Chen et al. cohort; lower-extremity numbness 100%, lower-extremity neuropathic pain 58.8%, lower-extremity weakness 64.7% in Wang et al. cohort (wang2019clinicalandelectrophysiological pages 2-3, chen2021ahighlyheterogeneous pages 2-4) | Core disabling feature; major cause of diagnostic delay and long-term disability; treatment-resistant “CIDP” should trigger evaluation for POEMS (cerri2019anupdateon pages 1-2, keddie2025poemssyndrome pages 4-7, latov2014diagnosisandtreatment pages 1-2) | HP:0009830 Polyneuropathy; HP:0007104 Demyelinating peripheral neuropathy; HP:0003394 Muscle weakness; HP:0002355 Difficulty walking; HP:0012532 Distal lower limb muscle weakness; HP:0031843 Neuropathic pain |
| Organomegaly | Hepatomegaly, splenomegaly, lymphadenopathy/lymph node enlargement; often identified on imaging rather than palpation (cerri2019anupdateon pages 1-2, cerri2019anupdateon pages 2-3, keddie2025poemssyndrome pages 4-7) | ~85.7% in Chen et al. cohort; described as a common minor criterion in major reviews (chen2021ahighlyheterogeneous pages 2-4, cerri2019anupdateon pages 2-3) | Supports multisystem diagnosis; helps distinguish POEMS from CIDP and other paraproteinemic neuropathies (cerri2019anupdateon pages 2-3, keddie2025poemssyndrome pages 4-7) | HP:0001433 Hepatosplenomegaly; HP:0001744 Splenomegaly; HP:0002240 Hepatomegaly; HP:0002716 Lymphadenopathy |
| Endocrinopathy | Hypogonadism/hypopituitarism most characteristic; thyroid abnormalities and adrenal insufficiency also reported; diabetes/glucose intolerance may occur but are not specific when isolated (cerri2019anupdateon pages 1-2, cerri2019anupdateon pages 2-3, keddie2025poemssyndrome pages 4-7) | ~84% in review summary; 40/42 (95.2%) in Chen et al. cohort; hypothyroidism 52.9% in Wang et al. series (cerri2019anupdateon pages 1-2, wang2019clinicalandelectrophysiological pages 2-3, chen2021ahighlyheterogeneous pages 2-4) | Common minor criterion but heterogeneous; combinations of endocrine abnormalities are more diagnostically useful than isolated diabetes or thyroid disease (cerri2019anupdateon pages 1-2) | HP:0000818 Abnormality of the endocrine system; HP:0000824 Hypogonadism; HP:0000821 Hypothyroidism; HP:0000855 Insulin-resistant diabetes mellitus / HP:0005978 Diabetes mellitus |
| Monoclonal gammopathy / plasma cell disorder | Usually low-level monoclonal plasma cell dyscrasia, typically IgAλ or IgGλ; serum paraprotein may be missed by SPEP and requires immunofixation; urine immunofixation and marrow/lesional biopsy may be needed; >95% lambda light-chain restricted in most series (cerri2019anupdateon pages 2-3, keddie2025poemssyndrome pages 4-7, chen2021ahighlyheterogeneous pages 1-2, chen2021ahighlyheterogeneous pages 2-4, latov2014diagnosisandtreatment pages 1-2) | Mandatory criterion in classic POEMS; 42/42 (100%) had positive serum or urine immunofixation in Chen et al.; only 64.7% had positive serum immunofixation at presentation in Wang et al.; SPEP positive in as few as 54%, immunofixation 75–92% in review data (keddie2025poemssyndrome pages 4-7, wang2019clinicalandelectrophysiological pages 2-3, chen2021ahighlyheterogeneous pages 2-4) | Central pathogenic lesion and treatment target; low tumor burden can obscure diagnosis; marrow plasma cells often <5% (median 1.5% in Chen et al.) (chen2021ahighlyheterogeneous pages 1-2, chen2021ahighlyheterogeneous pages 2-4) | HP:0032113 Monoclonal gammopathy; HP:0011897 Abnormal plasma cell morphology/number; HP:0410292 Increased circulating immunoglobulin |
| Skin changes | Hyperpigmentation, hypertrichosis, skin thickening, acrocyanosis, plethora/flushing, white nails, hemangiomas/glomeruloid hemangiomata (cerri2019anupdateon pages 1-2, keddie2025poemssyndrome pages 4-7) | ~70% in Keddie/Lunn cohort summary; 40/42 (95.2%) in Chen et al.; 13/17 (76.5%) in Wang et al. had skin change (keddie2025poemssyndrome pages 4-7, wang2019clinicalandelectrophysiological pages 2-3, chen2021ahighlyheterogeneous pages 2-4) | Common and often visually helpful clue to multisystem disease; contributes to acronym but is not required for diagnosis (cerri2019anupdateon pages 1-2, keddie2025poemssyndrome pages 4-7) | HP:0000953 Hyperpigmentation of the skin; HP:0002219 Hypertrichosis; HP:0001065 Skin thickening; HP:0000966 Abnormality of the skin; HP:0001101 Acrocyanosis; HP:0001597 Nail abnormality |
| Extravascular volume overload | Peripheral edema, ascites, pleural effusion, pericardial effusion; can accompany pulmonary hypertension, cardiac insufficiency, renal dysfunction; may worsen during stem-cell mobilization/transplant periods (cerri2019anupdateon pages 1-2, cerri2019anupdateon pages 2-3, keddie2025poemssyndrome pages 4-7, chen2021ahighlyheterogeneous pages 2-4) | Peripheral edema 71.4%, ascites 40.5%, pleural effusion 35.7%, pericardial effusion 54.8% in Chen et al.; edema 82.4% in Wang et al. cohort (wang2019clinicalandelectrophysiological pages 2-3, chen2021ahighlyheterogeneous pages 2-4) | Important minor criterion; associated with worse overall survival in reviews; major determinant of clinical acuity and transplant fitness (cerri2019anupdateon pages 2-3, keddie2025poemssyndrome pages 4-7) | HP:0000969 Edema; HP:0001541 Ascites; HP:0012378 Pleural effusion; HP:0001698 Pericardial effusion |
| Bone lesions | Usually osteosclerotic lesions; can be densely sclerotic, lytic with sclerotic rim, or mixed “soap-bubble” lesions; often multiple and small; FDG-PET/CT helps identify active lesions and biopsy targets (cerri2019anupdateon pages 1-2, keddie2025poemssyndrome pages 4-7, keddie2025poemssyndrome pages 10-12) | Approximately 95% in one review summary; 18/42 (42.9%) in Chen et al. genomic cohort; prevalence varies by cohort and imaging modality (cerri2019anupdateon pages 1-2, chen2021ahighlyheterogeneous pages 2-4) | One of the major diagnostic criteria; determines local vs systemic therapy decisions, including radiotherapy for ≤3 lesions without diffuse marrow disease (cerri2019anupdateon pages 2-3, keddie2025poemssyndrome pages 4-7) | HP:0002792 Abnormality of the skeletal system; HP:0030934 Osteosclerosis; HP:0002758 Osteolysis |
| Papilledema | Optic disc edema/papilledema, sometimes with preserved vision initially; may reflect vascular leak and raised intracranial/optic disc fluid dynamics rather than primary optic nerve disease (cerri2019anupdateon pages 1-2, cerri2019anupdateon pages 2-3, keddie2025poemssyndrome pages 4-7) | ~50% during 10-year follow-up in two cohorts summarized by Cerri et al.; 5/42 (11.9%) in Chen et al. cohort (cerri2019anupdateon pages 1-2, chen2021ahighlyheterogeneous pages 2-4) | Minor criterion; reported as an independent adverse prognostic factor for overall survival in prior cohort data summarized by reviews (cerri2019anupdateon pages 1-2) | HP:0001085 Papilledema |
| Thrombocytosis / polycythemia | Thrombocytosis more common than polycythemia; part of prothrombotic diathesis; often accompanies stroke risk and hypercoagulability (cerri2019anupdateon pages 1-2, cerri2019anupdateon pages 2-3, keddie2025poemssyndrome pages 4-7) | Thrombocytosis present in ~55% in review data; recognized minor criterion in all major diagnostic frameworks discussed (cerri2019anupdateon pages 1-2, cerri2019anupdateon pages 2-3) | Helpful discriminator from CIDP; linked to ischemic stroke/thrombotic complications and may affect treatment choices such as lenalidomide thromboprophylaxis (cerri2019anupdateon pages 2-3, keddie2025poemssyndrome pages 4-7) | HP:0001873 Thrombocytosis; HP:0001901 Polycythemia |
| Other neurologic/systemic features | Castleman disease overlap; ischemic stroke (often watershed distribution); pulmonary hypertension; restrictive lung disease; renal dysfunction; heart failure; pachymeningeal involvement; depression reported in prior cohorts; Castleman-associated cases may have mild or absent neuropathy (cerri2019anupdateon pages 1-2, cerri2019anupdateon pages 2-3, keddie2025poemssyndrome pages 4-7, keddie2025poemssyndrome pages 12-17) | Castleman disease in ~11–30% of patients in review summaries; ischemic stroke ~10%; male predominance ~2.5:1 and onset most often in 5th–6th decade (cerri2019anupdateon pages 1-2, keddie2025poemssyndrome pages 1-4, cerri2019anupdateon pages 2-3) | Expands differential diagnosis and affects prognosis/management; cardiopulmonary involvement influences transplant candidacy and survival (keddie2025poemssyndrome pages 1-4, keddie2025poemssyndrome pages 4-7) | HP:0002664 Castleman disease; HP:0001297 Stroke; HP:0002092 Pulmonary hypertension; HP:0000077 Abnormality of the kidney; HP:0001635 Congestive heart failure; HP:0100840 Pachymeningitis |


*Table: This table summarizes the major clinical phenotypes of POEMS syndrome, including characteristic manifestations, approximate frequencies from the retrieved literature, their diagnostic or prognostic relevance, and suggested HPO mappings. It is useful for structuring disease knowledge base entries and phenotype annotation.*

**Key Phenotype Characteristics:**

**Polyneuropathy** (HP:0009830, HP:0007104, HP:0031843):
- **Type:** Symmetrical, sensorimotor, length-dependent, painful demyelinating polyneuropathy/radiculoneuropathy
- **Onset:** Often the first presenting feature; progressive over months
- **Severity:** Disabling with striking distal weakness of hands and feet; variable severity
- **Progression:** Chronic progressive, ascending pattern
- **Frequency:** Mandatory criterion, present in essentially 100% of classic cases (wang2019clinicalandelectrophysiological pages 1-2, keddie2025poemssyndrome pages 1-4, keddie2025poemssyndrome pages 4-7, wang2019clinicalandelectrophysiological pages 2-3)

**Organomegaly** (HP:0001433, HP:0002240, HP:0001744, HP:0002716):
- **Manifestations:** Hepatomegaly, splenomegaly, lymphadenopathy
- **Detection:** Often by imaging rather than palpation
- **Frequency:** ~85.7% in one cohort (chen2021ahighlyheterogeneous pages 2-4)

**Endocrinopathy** (HP:0000818, HP:0000824, HP:0000821):
- **Most characteristic:** Hypogonadism/hypopituitarism
- **Also seen:** Thyroid abnormalities, adrenal insufficiency, diabetes
- **Frequency:** 84-95.2% in reviewed cohorts (cerri2019anupdateon pages 1-2, chen2021ahighlyheterogeneous pages 2-4)
- **Note:** Diabetes or thyroid disease alone are not specific enough for diagnosis given general population prevalence (cerri2019anupdateon pages 1-2)

**Skin Changes** (HP:0000953, HP:0002219, HP:0001065, HP:0001101):
- **Manifestations:** Hyperpigmentation, hypertrichosis, skin thickening, acrocyanosis, plethora, white nails, hemangiomas
- **Frequency:** 70-95.2% in reviewed cohorts (keddie2025poemssyndrome pages 4-7, wang2019clinicalandelectrophysiological pages 2-3, chen2021ahighlyheterogeneous pages 2-4)

**Quality of Life Impact:**
The polyneuropathy is the most disabling feature, causing significant mobility impairment, pain, and functional disability. Without early diagnosis and treatment, significant irreversible neurologic disability results (keddie2025poemssyndrome pages 4-7, cerri2019anupdateon pages 3-6). The multisystem nature affects daily functioning across multiple domains including mobility, endocrine health, and cosmetic concerns.

## 4. Genetic/Molecular Information

**Causal Genes and Pathogenic Variants:**

The disease is not associated with germline mutations in specific causal genes but rather involves somatic alterations in clonal plasma cells:

**Immunoglobulin Gene Rearrangements:**
- Restricted IGLV gene usage (IGLV 1-40 and IGLV 1-44) (keddie2025poemssyndrome pages 1-4)
- Clonal immunoglobulin λ light chain gene rearrangements detected by next-generation sequencing (keddie2025poemssyndrome pages 1-4)

**Somatic Mutations in Plasma Cells:**
Based on whole exome sequencing and targeted sequencing of purified bone marrow plasma cells from 42 patients (chen2021ahighlyheterogeneous pages 2-4, chen2021ahighlyheterogeneous pages 4-5):

- **Significantly Mutated Genes (FDR < 0.1):**
  - HEATR9: 20% (frameshift insertion)
  - LILRB1: 10% (missense mutations)
  - FMNL2: 10% (frameshift insertion, nonframeshift deletion)

- **Cancer Driver Genes Detected:**
  - MYD88, NFKB2, CHD4, SH2B3, POLE, STAT3, CHD3, CUX1 (each 10% in WES cohort)
  
- **Recurrent Mutations from Target Sequencing:**
  - CUX1: 19%
  - DNAH5, USH2A, KMT2D: each 16%
  - RYR1: 12%

**Variant Classification:**
Specific ACMG/AMP classifications were not provided in the retrieved literature. The mutations represent somatic variants in clonal plasma cells rather than germline pathogenic variants.

**Allele Frequency:**
These somatic mutations are specific to the malignant plasma cell clone and not present in germline. Population allele frequencies are not applicable for these somatic variants.

**Functional Consequences:**
Pathway analysis revealed enrichment in chromatin organization, chromatin modifying enzymes, and apoptosis pathways (chen2021ahighlyheterogeneous pages 4-5). Mutational signatures were closest to Signature 5 (transcriptional strand bias) and Signature 6 (associated with defective DNA mismatch repair) (chen2021ahighlyheterogeneous pages 2-4).

**Chromosomal Abnormalities:**
- 14q32 (IGH) translocations: ~50% of patients
- 13q14 deletions
- Aneuploidy including monosomy 13, trisomy 3 and 7 (keddie2025poemssyndrome pages 1-4, chen2021ahighlyheterogeneous pages 2-4)

## 5. Environmental Information

No specific environmental factors have been identified as causal or modifying factors for POEMS syndrome. The disease appears to be a sporadic plasma cell dyscrasia without clear environmental triggers identified in the literature reviewed.

## 6. Mechanism / Pathophysiology

**Molecular Pathways and Causal Chain:**

The pathophysiology of POEMS syndrome involves a complex interplay between monoclonal plasma cells and inflammatory cytokines, with vascular endothelial growth factor (VEGF) playing a central but downstream role (cerri2019anupdateon pages 1-2, keddie2025poemssyndrome pages 1-4, keddie2025poemssyndrome pages 12-17).

**Primary Event → Cytokine Dysregulation:**
1. Small volume malignant lambda-restricted monoclonal plasma cells are the initiating pathogenic lesion (keddie2025poemssyndrome pages 1-4, chen2021ahighlyheterogeneous pages 2-4)
2. These monoclonal plasma cells produce high levels of interleukin-6 (IL-6) (keddie2025poemssyndrome pages 1-4, keddie2025poemssyndrome pages 12-17)
3. IL-6 from monoclonal cells drives polyclonal plasma cells to secrete VEGF (keddie2025poemssyndrome pages 1-4, keddie2025poemssyndrome pages 12-17)
4. Polyclonal plasma cells produce the majority of VEGF measured in serum/bone marrow; monoclonal cells comprise a small percentage but are IL-6 positive (keddie2025poemssyndrome pages 12-17)

**VEGF-Mediated Downstream Effects:**
VEGF is markedly elevated in POEMS syndrome (median 6256 pg/mL in one cohort, range 50-12,852 pg/mL) (cerri2019anupdateon pages 1-2, keddie2025poemssyndrome pages 1-4, chen2021ahighlyheterogeneous pages 2-4). VEGF acts as a multifunctional cytokine with the following effects:

- **Endothelial Dysfunction:** VEGF causes endothelial cytoplasmic enlargement, opening of tight junctions between endothelial cells, increased pinocytic vesicles, and vascular permeability (cerri2019anupdateon pages 3-6)
- **Blood-Nerve Barrier Disruption:** Leads to endoneurial edema, leakage of toxic serum components, and secondary ischemic microangiopathy causing chronic axonal damage and demyelination (cerri2019anupdateon pages 1-2, cerri2019anupdateon pages 3-6)
- **Extravascular Volume Overload:** Microvascular permeability results in peripheral edema, ascites, pleural and pericardial effusions (cerri2019anupdateon pages 1-2, cerri2019anupdateon pages 2-3)
- **Organomegaly:** Angiogenic effects contribute to hepatosplenomegaly and lymphadenopathy (cerri2019anupdateon pages 1-2)
- **Bone Lesions:** VEGF regulates osteogenesis and contributes to osteosclerotic lesion formation (keddie2025poemssyndrome pages 1-4)
- **Papilledema:** Increased microvascular permeability affects optic nerve vasculature (cerri2019anupdateon pages 1-2)

**Positive Feedback Loop:**
Tissue ischemia and hypoxia induce hypoxia-inducible factor-1α (HIF-1α), which further drives VEGF production, creating a perpetuating cycle of vascular damage and VEGF elevation (cerri2019anupdateon pages 1-2, keddie2025poemssyndrome pages 12-17).

**Other Cytokines:**
Tumor necrosis factor-α (TNF-α), IL-6, and IL-12 are also upregulated and may contribute to pathogenesis, though VEGF is the most studied biomarker (cerri2019anupdateon pages 1-2, keddie2025poemssyndrome pages 12-17).

**Key Mechanistic Insight:**
VEGF is a downstream mediator rather than the primary initiating factor. Anti-VEGF therapy with bevacizumab does not lead to clinical recovery and may be harmful, suggesting other pathogenic mechanisms are involved (cerri2019anupdateon pages 1-2, keddie2025poemssyndrome pages 1-4, keddie2025poemssyndrome pages 7-10).

**Cellular Processes:**
- Plasma cell proliferation and survival (CL:0000786 plasma cell)
- Endothelial cell activation and dysfunction (CL:0000115 endothelial cell)
- Inflammatory response and cytokine secretion
- Angiogenesis dysregulation
- Demyelination and axonal degeneration in peripheral nerves

**GO Terms:**
- GO:0001525 Angiogenesis
- GO:0002526 Acute inflammatory response
- GO:0042035 Regulation of cytokine biosynthetic process
- GO:0001952 Regulation of cell-matrix adhesion
- GO:0043065 Positive regulation of apoptotic process

## 7. Anatomical Structures Affected

**Organ Level:**

**Primary Organs:**
- **Peripheral Nervous System:** Polyneuropathy affecting motor and sensory nerves, predominantly length-dependent (UBERON:0000010 peripheral nervous system) (wang2019clinicalandelectrophysiological pages 1-2, cerri2019anupdateon pages 1-2, keddie2025poemssyndrome pages 4-7)
- **Bone Marrow:** Site of monoclonal plasma cell proliferation (UBERON:0002371 bone marrow)
- **Skeletal System:** Osteosclerotic/osteolytic lesions (UBERON:0001434 skeletal system) (cerri2019anupdateon pages 1-2, keddie2025poemssyndrome pages 4-7)

**Secondary Organ Involvement:**
- **Liver:** Hepatomegaly (UBERON:0002107 liver) (cerri2019anupdateon pages 1-2, cerri2019anupdateon pages 2-3)
- **Spleen:** Splenomegaly (UBERON:0002106 spleen)
- **Lymph Nodes:** Lymphadenopathy (UBERON:0000029 lymph node)
- **Endocrine Glands:** Hypothalamic-pituitary axis, thyroid, gonads, adrenal glands (UBERON:0000949 endocrine system) (cerri2019anupdateon pages 1-2)
- **Optic Nerve:** Papilledema (UBERON:0000941 optic nerve) (cerri2019anupdateon pages 1-2)
- **Skin:** Multiple cutaneous manifestations (UBERON:0002097 skin of body)

**Body Systems Involved:**
- Nervous system (peripheral neuropathy, central features)
- Hematopoietic system (plasma cell dyscrasia)
- Skeletal system (bone lesions)
- Endocrine system
- Integumentary system (skin changes)
- Cardiovascular system (volume overload, pulmonary hypertension)

**Tissue and Cell Level:**
- **Peripheral Nerve Tissue:** Demyelinating and axonal pathology (cerri2019anupdateon pages 3-6)
- **Plasma Cells:** Clonal expansion in bone marrow (CL:0000786 plasma cell)
- **Endothelial Cells:** Dysfunction across vascular beds (CL:0000115 endothelial cell)
- **Osteoblasts:** Involved in bone lesion formation

**Subcellular Level:**
- **Endothelial tight junctions:** Disrupted leading to vascular leak (GO:0005923 bicellular tight junction)
- **Myelin sheaths:** Uncompacted myelin and demyelination (cerri2019anupdateon pages 3-6)

## 8. Temporal Development

**Onset:**
- **Typical Age:** Fifth or sixth decade of life (median age ~48-57 years in reviewed cohorts) (keddie2025poemssyndrome pages 1-4, wang2019clinicalandelectrophysiological pages 2-3, chen2021ahighlyheterogeneous pages 2-4)
- **Onset Pattern:** Subacute to chronic; polyneuropathy is often the first manifestation and may precede full syndrome recognition by months (cerri2019anupdateon pages 1-2, latov2014diagnosisandtreatment pages 1-2)
- **Diagnostic Delay:** Frequently misdiagnosed initially as chronic inflammatory demyelinating polyneuropathy (CIDP); median diagnostic delay >13 months in some series (cerri2019anupdateon pages 1-2, latov2014diagnosisandtreatment pages 1-2)

**Progression:**
- **Disease Course:** Chronic progressive without treatment; multisystem features may appear sequentially over months (cerri2019anupdateon pages 1-2)
- **Progression Rate:** Variable; neurologic progression can be rapid in untreated cases
- **Untreated Median Survival:** 33 months (keddie2025poemssyndrome pages 4-7)
- **Treated Survival:** With modern therapies, 5-year overall survival ranges from 79-95% depending on treatment and prognostic factors (keddie2025poemssyndrome pages 7-10, keddie2025poemssyndrome pages 4-7, keddie2025poemssyndrome pages 10-12)

**Disease Stages:**
No formal staging system, but disease extent is classified as:
- **Localized/Focal:** 1-3 bone lesions without bone marrow involvement → candidates for radiotherapy (keddie2025poemssyndrome pages 4-7)
- **Systemic:** Diffuse bone marrow involvement or extensive multifocal disease → candidates for systemic therapy (keddie2025poemssyndrome pages 4-7)

**Critical Periods:**
Early diagnosis and treatment are critical to prevent irreversible neurologic disability (keddie2025poemssyndrome pages 4-7, cerri2019anupdateon pages 3-6).

## 9. Inheritance and Population

**Epidemiology:**
- **Incidence:** Estimated 0.3 per 100,000 based on a Japanese nationwide survey (keddie2025poemssyndrome pages 1-4)
- **Prevalence:** Exact prevalence unknown; considered a rare disease
- **Geographic Distribution:** Largest reported cohorts from China (476 patients), USA (291 patients), and Japan (102 patients in older series), suggesting possible higher prevalence in Asia, though reporting bias may contribute (keddie2025poemssyndrome pages 1-4)

**Inheritance Pattern:**
POEMS syndrome is a sporadic acquired plasma cell disorder, not an inherited genetic disease. There is no known familial inheritance pattern.

**Population Demographics:**
- **Sex Ratio:** Male predominance approximately 2.5:1 (keddie2025poemssyndrome pages 1-4)
- **Age Distribution:** Onset most commonly in fifth to sixth decade; median age 48-57 years at diagnosis in various cohorts (keddie2025poemssyndrome pages 1-4, wang2019clinicalandelectrophysiological pages 2-3, chen2021ahighlyheterogeneous pages 2-4)
- **Affected Populations:** No specific ethnic group identified as having markedly higher risk, though cohort sizes from Asia are notable

## 10. Diagnostics

A comprehensive table of diagnostic criteria and tests is presented below:

| Diagnostic category | Specific requirement/test | Clinical/laboratory details and what constitutes positive finding | Diagnostic utility/performance | Suggested ontology terms |
|---|---|---|---|---|
| Mandatory criteria | Polyneuropathy | Typically a chronic, progressive, symmetrical, sensorimotor, length-dependent, painful demyelinating polyneuropathy/radiculoneuropathy with distal weakness predominance; often initially labeled CIDP; electrophysiology commonly shows uniform demyelination with marked secondary axonal loss and severe lower-limb involvement (wang2019clinicalandelectrophysiological pages 1-2, cerri2019anupdateon pages 1-2, cerri2019anupdateon pages 2-3, keddie2025poemssyndrome pages 4-7, wang2019clinicalandelectrophysiological pages 2-3) | Essential diagnostic criterion; present in essentially all classic cases; major source of disability and diagnostic delay; treatment-resistant “CIDP” should trigger POEMS workup (cerri2019anupdateon pages 1-2, keddie2025poemssyndrome pages 4-7, latov2014diagnosisandtreatment pages 1-2) | HP:0009830 Polyneuropathy; HP:0007104 Demyelinating peripheral neuropathy; HP:0031843 Neuropathic pain; NCIT:C38008 Nerve Conduction Study |
| Mandatory criteria | Monoclonal plasma cell disorder | Usually low-level IgAλ or IgGλ monoclonal gammopathy/plasma cell dyscrasia; serum paraprotein may be very small or undetectable on serum protein electrophoresis alone; positive finding may require serum/urine immunofixation, bone marrow biopsy, or lesional biopsy; >95% lambda-restricted in most series (cerri2019anupdateon pages 2-3, keddie2025poemssyndrome pages 4-7, chen2021ahighlyheterogeneous pages 1-2, chen2021ahighlyheterogeneous pages 2-4, latov2014diagnosisandtreatment pages 1-2) | Essential diagnostic criterion and therapeutic target; SPEP may miss cases; immunofixation improves yield; in one cohort, all 42/42 had positive serum or urine immunofixation, but only 64.7% had positive serum immunofixation at presentation in another cohort (wang2019clinicalandelectrophysiological pages 2-3, chen2021ahighlyheterogeneous pages 2-4) | HP:0032113 Monoclonal gammopathy; LOINC:24351-9 Protein electrophoresis panel-serum; LOINC:LAB174 Immunofixation electrophoresis |
| Major criteria | Castleman disease | Histopathologically confirmed Castleman disease in lymph node or tissue; may coexist with mild, painless, or even absent overt neuropathy in some cases (cerri2019anupdateon pages 2-3, keddie2025poemssyndrome pages 4-7, keddie2025poemssyndrome pages 12-17) | One of the 3 additional major criteria; important overlap entity; helps explain atypical presentations but does not replace mandatory criteria in standard POEMS diagnosis (cerri2019anupdateon pages 2-3, keddie2025poemssyndrome pages 12-17) | HP:0002664 Castleman disease; NCIT:C4034 Lymph Node Biopsy |
| Major criteria | Sclerotic bone lesions | Osteosclerotic lesions on CT/PET-CT/MRI; may be densely sclerotic, lytic with sclerotic rim, or mixed “soap-bubble” lesions; often multiple and small; FDG-avid lesions can guide biopsy (cerri2019anupdateon pages 1-2, keddie2025poemssyndrome pages 4-7, keddie2025poemssyndrome pages 10-12) | One of the core major criteria; central for distinguishing focal from systemic disease and for treatment planning; CT and FDG-PET/CT are emphasized over skeletal survey in modern workup (keddie2025poemssyndrome pages 4-7, keddie2025poemssyndrome pages 10-12) | HP:0030934 Osteosclerosis; NCIT:C17204 Computed Tomography; NCIT:C103430 Positron Emission Tomography |
| Major criteria | Elevated VEGF | Elevated serum or plasma vascular endothelial growth factor above assay-specific normal range; markedly raised levels are typical; example cohort median serum VEGF 6256 pg/mL (range 50-12,852 pg/mL) (cerri2019anupdateon pages 1-2, keddie2025poemssyndrome pages 1-4, chen2021ahighlyheterogeneous pages 2-4) | Major diagnostic biomarker; supports diagnosis and follow-up; considered useful and accurate for diagnosis and disease monitoring; normalization/suppression after treatment correlates with improved relapse-free survival and outcomes (cerri2019anupdateon pages 1-2, keddie2025poemssyndrome pages 1-4, keddie2025poemssyndrome pages 10-12) | LOINC:34694-0 Vascular endothelial growth factor [Mass/volume] in Serum or Plasma; HP:0033677 Increased circulating VEGF level |
| Minor criteria | Organomegaly | Hepatomegaly, splenomegaly, and/or lymphadenopathy, often detected by CT rather than palpation (cerri2019anupdateon pages 1-2, cerri2019anupdateon pages 2-3, keddie2025poemssyndrome pages 4-7) | Minor criterion supporting multisystem nature; helps distinguish POEMS from CIDP and other neuropathy syndromes; organomegaly occurred in 85.7% in one cohort (cerri2019anupdateon pages 2-3, chen2021ahighlyheterogeneous pages 2-4) | HP:0002240 Hepatomegaly; HP:0001744 Splenomegaly; HP:0002716 Lymphadenopathy |
| Minor criteria | Endocrinopathy | Most characteristic: hypogonadism/hypopituitarism; also thyroid abnormalities and adrenal insufficiency; diabetes or thyroid disease alone are not considered sufficiently specific because common in the general population (cerri2019anupdateon pages 1-2, keddie2025poemssyndrome pages 4-7) | Minor criterion; combinations of endocrine abnormalities are more diagnostically reliable than isolated diabetes or hypothyroidism; endocrinopathy occurred in 95.2% in one cohort (cerri2019anupdateon pages 1-2, chen2021ahighlyheterogeneous pages 2-4) | HP:0000818 Abnormality of the endocrine system; HP:0000824 Hypogonadism; HP:0000821 Hypothyroidism |
| Minor criteria | Skin changes | Hyperpigmentation, hypertrichosis, skin thickening, acrocyanosis, flushing/plethora, white nails, hemangiomas/glomeruloid hemangiomata (cerri2019anupdateon pages 1-2, keddie2025poemssyndrome pages 4-7, wang2019clinicalandelectrophysiological pages 2-3) | Minor criterion and useful visual clue; common in practice; present in 76.5% of one cohort and 95.2% of another (wang2019clinicalandelectrophysiological pages 2-3, chen2021ahighlyheterogeneous pages 2-4) | HP:0000953 Hyperpigmentation of the skin; HP:0002219 Hypertrichosis; HP:0001065 Skin thickening; HP:0001101 Acrocyanosis |
| Minor criteria | Papilledema | Bilateral optic disc edema/papilledema on ophthalmic examination; may occur with preserved vision early (cerri2019anupdateon pages 1-2, keddie2025poemssyndrome pages 4-7) | Minor criterion; clinically important because reported as an adverse prognostic marker in prior cohorts; frequency varies by cohort and follow-up duration (cerri2019anupdateon pages 1-2, chen2021ahighlyheterogeneous pages 2-4) | HP:0001085 Papilledema; NCIT:C38087 Funduscopic Examination |
| Minor criteria | Extravascular volume overload | Peripheral edema, ascites, pleural effusion, and/or pericardial effusion; may coexist with pulmonary hypertension, renal dysfunction, or cardiac insufficiency (cerri2019anupdateon pages 1-2, cerri2019anupdateon pages 2-3, keddie2025poemssyndrome pages 4-7, chen2021ahighlyheterogeneous pages 2-4) | Minor criterion; important marker of disease severity and transplant fitness; associated with shorter overall survival in review literature (cerri2019anupdateon pages 2-3, keddie2025poemssyndrome pages 4-7) | HP:0000969 Edema; HP:0001541 Ascites; HP:0012378 Pleural effusion; HP:0001698 Pericardial effusion |
| Minor criteria | Thrombocytosis / polycythemia | Elevated platelet count and/or increased red cell mass/hematocrit; thrombocytosis is more frequent and contributes to prothrombotic state (cerri2019anupdateon pages 1-2, cerri2019anupdateon pages 2-3, keddie2025poemssyndrome pages 4-7) | Minor criterion; diagnostically useful because thrombocytosis helps distinguish POEMS from CIDP; also clinically relevant for stroke/thrombosis risk and for thromboprophylaxis decisions with lenalidomide (cerri2019anupdateon pages 2-3, keddie2025poemssyndrome pages 4-7) | HP:0001873 Thrombocytosis; HP:0001901 Polycythemia; LOINC:777-3 Platelets [#/volume] in Blood |
| Key diagnostic tests and biomarkers | Serum and urine immunofixation electrophoresis | Performed when SPEP is negative or equivocal; detects low-level monoclonal immunoglobulin/light chain; urine immunofixation may be positive when serum testing is negative (cerri2019anupdateon pages 2-3, keddie2025poemssyndrome pages 4-7, wang2019clinicalandelectrophysiological pages 2-3) | Higher diagnostic yield than SPEP; review data: SPEP positive in as few as 54% vs immunofixation 75-92%; in Wang cohort 64.7% had positive serum immunofixation despite all having clonal plasma cell disorder (keddie2025poemssyndrome pages 4-7, wang2019clinicalandelectrophysiological pages 2-3) | LOINC:24351-9 Protein electrophoresis panel-serum; LOINC:LAB174 Immunofixation electrophoresis |
| Key diagnostic tests and biomarkers | Bone marrow aspirate/biopsy with kappa/lambda immunohistochemistry | Evaluates plasma cell burden and light-chain restriction; marrow clonal plasma cells are often sparse; one genomic cohort had median bone marrow plasma cells 1.5% (range 0-10%) (cerri2019anupdateon pages 2-3, chen2021ahighlyheterogeneous pages 1-2, chen2021ahighlyheterogeneous pages 2-4) | Fundamental in suspected POEMS when paraprotein is subtle; helps distinguish POEMS from other plasma-cell disorders and from Waldenström macroglobulinemia/amyloidosis (cerri2019anupdateon pages 2-3, cerri2019anupdateon pages 3-6) | NCIT:C17617 Bone Marrow Biopsy; NCIT:C12255 Immunohistochemistry |
| Key diagnostic tests and biomarkers | Nerve conduction studies / EMG | Positive pattern: demyelinating neuropathy with marked secondary axonal loss, severe lower-limb CMAP reduction/absence, less conduction block and less temporal dispersion than CIDP, higher terminal latency index in some studies (wang2019clinicalandelectrophysiological pages 1-2, keddie2025poemssyndrome pages 4-7, wang2019clinicalandelectrophysiological pages 2-3) | In Wang et al., combination of positive serum monoclonal protein and high TLI discriminated POEMS from CIDP with sensitivity 94.1% and specificity 76.5% if either present; specificity 100% if both present, but sensitivity 47.1% (wang2019clinicalandelectrophysiological pages 1-2) | NCIT:C38008 Nerve Conduction Study; NCIT:C38054 Electromyography |
| Key diagnostic tests and biomarkers | Nerve ultrasound | Ultrasound of median, ulnar, brachial plexus and other nerves; POEMS shows more homogeneous enlargement along nerves and no conduction block, compared with more heterogeneous CIDP enlargement (niu2022nerveultrasoundperformances pages 1-2) | Two-step protocol using conduction block plus maximum/minimum median nerve CSA ratio differentiated CIDP from POEMS with sensitivity 93% and specificity 79% (niu2022nerveultrasoundperformances pages 1-2) | NCIT:C17230 Ultrasonography |
| Key diagnostic tests and biomarkers | CT / FDG-PET/CT imaging | CT identifies osteosclerotic lesions, adenopathy, organomegaly, ascites, pleural effusions, and edema; FDG-PET/CT identifies active bone lesions and guides lesional biopsy (cerri2019anupdateon pages 2-3, keddie2025poemssyndrome pages 4-7, keddie2025poemssyndrome pages 10-12) | Recommended as part of routine workup in suspected POEMS; FDG-PET/CT is especially useful for target lesion selection and treatment planning (local vs systemic therapy) (keddie2025poemssyndrome pages 4-7, keddie2025poemssyndrome pages 10-12) | NCIT:C17204 Computed Tomography; NCIT:C103430 Positron Emission Tomography |
| Key diagnostic tests and biomarkers | Ophthalmologic examination | Direct fundus examination and related ophthalmic assessment for papilledema/optic disc edema (cerri2019anupdateon pages 1-2, keddie2025poemssyndrome pages 4-7) | Important because papilledema may be overlooked yet contributes to diagnosis and prognosis (cerri2019anupdateon pages 1-2) | NCIT:C38087 Funduscopic Examination; HP:0001085 Papilledema |
| Key diagnostic tests and biomarkers | CBC and routine laboratory screening | Platelet count for thrombocytosis, hemoglobin/hematocrit for polycythemia, endocrine panels, renal/liver function testing, and general multisystem assessment (cerri2019anupdateon pages 2-3, keddie2025poemssyndrome pages 4-7) | Supports minor criteria and complication assessment; thrombocytosis is a practical discriminator from CIDP and helps estimate thrombotic risk (cerri2019anupdateon pages 2-3, latov2014diagnosisandtreatment pages 1-2) | LOINC:57021-8 CBC W Auto Differential panel-Blood; LOINC:777-3 Platelets [#/volume] in Blood |
| Diagnostic rule | Standardized case definition | Diagnosis is confirmed by both mandatory criteria plus at least 1 other major criterion and at least 1 minor criterion (cerri2019anupdateon pages 2-3, wang2019clinicalandelectrophysiological pages 2-3, chen2021ahighlyheterogeneous pages 1-2) | Standard framework across reviewed literature; integrates neurologic, hematologic, laboratory, and imaging data and reduces misclassification as CIDP or other monoclonal gammopathy-associated neuropathies (cerri2019anupdateon pages 2-3, latov2014diagnosisandtreatment pages 1-2) | MONDO: not confirmed from retrieved context; NCIT:C3671 Diagnostic Criteria |


*Table: This table summarizes the standardized diagnostic criteria for POEMS syndrome and the main diagnostic tests used in practice. It is useful for organizing mandatory, major, and minor criteria alongside the most informative laboratory, electrophysiologic, and imaging studies.*

**Diagnostic Criteria Framework:**

The diagnosis requires:
- **Both mandatory criteria:**
  1. Polyneuropathy
  2. Monoclonal plasma cell disorder
- **Plus ≥1 of 3 major criteria:**
  1. Castleman disease
  2. Sclerotic bone lesions
  3. Elevated VEGF
- **Plus ≥1 of 6 minor criteria:**
  1. Organomegaly
  2. Extravascular volume overload
  3. Endocrinopathy
  4. Skin changes
  5. Papilledema
  6. Thrombocytosis/polycythemia
(cerri2019anupdateon pages 2-3, wang2019clinicalandelectrophysiological pages 2-3, chen2021ahighlyheterogeneous pages 1-2)

**Key Laboratory Tests:**

**Serum/Urine Immunofixation:**
- Serum protein electrophoresis (SPEP) positive in only ~54% of cases
- Serum immunofixation increases yield to 75-92%
- Urine immunofixation may be positive when serum is negative
- Lambda light chain restriction in >95% of cases (keddie2025poemssyndrome pages 4-7, wang2019clinicalandelectrophysiological pages 2-3)

**Serum VEGF:**
- Major diagnostic biomarker; markedly elevated (median ~6256 pg/mL in one cohort)
- Correlates with disease activity
- Normalization predicts improved outcomes (cerri2019anupdateon pages 1-2, keddie2025poemssyndrome pages 1-4, keddie2025poemssyndrome pages 10-12, chen2021ahighlyheterogeneous pages 2-4)

**Bone Marrow Examination:**
- Typically shows low plasma cell burden (median 1.5%, range 0-10%)
- Kappa/lambda immunohistochemistry demonstrates lambda restriction (cerri2019anupdateon pages 2-3, chen2021ahighlyheterogeneous pages 2-4)

**Nerve Conduction Studies:**
- Demyelinating pattern with marked secondary axonal loss
- Severe lower limb CMAP reduction/absence
- Less conduction block than CIDP
- Higher terminal latency index than CIDP
- Combination of positive monoclonal protein and high TLI: sensitivity 94.1%, specificity 76.5% for distinguishing POEMS from CIDP (wang2019clinicalandelectrophysiological pages 1-2)

**Nerve Ultrasound:**
- More homogeneous nerve enlargement along same nerve compared to CIDP
- Two-step protocol (conduction block + median nerve CSA ratio): sensitivity 93%, specificity 79% for CIDP vs POEMS differentiation (niu2022nerveultrasoundperformances pages 1-2)

**Imaging:**
- **CT/FDG-PET-CT:** Identifies osteosclerotic lesions, organomegaly, adenopathy, effusions; FDG-PET guides biopsy target selection (keddie2025poemssyndrome pages 4-7, keddie2025poemssyndrome pages 10-12)
- **Bone lesions:** ~95% have osteosclerotic lesions; may be densely sclerotic, lytic with sclerotic rim, or mixed (cerri2019anupdateon pages 1-2)

**Differential Diagnosis:**

Key conditions to distinguish from POEMS:
- **CIDP:** Responds to immunotherapy; lacks systemic features; different electrophysiology pattern (cerri2019anupdateon pages 1-2, latov2014diagnosisandtreatment pages 1-2, niu2022nerveultrasoundperformances pages 1-2)
- **MGUS-associated neuropathy:** Lacks multisystem features (cerri2019anupdateon pages 3-6)
- **AL Amyloidosis:** Amyloid deposits in tissue; primarily axonal neuropathy with autonomic involvement (cerri2019anupdateon pages 3-6)
- **Waldenström macroglobulinemia:** IgM paraprotein (vs IgA/IgG-lambda in POEMS) (cerri2019anupdateon pages 3-6)
- **Castleman disease:** May have mild sensory neuropathy but lacks full POEMS features (cerri2019anupdateon pages 2-3, keddie2025poemssyndrome pages 12-17)

## 11. Outcome/Prognosis

**Survival and Mortality:**
- **Untreated Median Survival:** 33 months (keddie2025poemssyndrome pages 4-7)
- **5-Year Overall Survival (treated):**
  - With ASCT: 90-95% (keddie2025poemssyndrome pages 7-10, keddie2025poemssyndrome pages 4-7)
  - Overall treated cohorts: 79-84% depending on risk stratification (keddie2025poemssyndrome pages 7-10, keddie2025poemssyndrome pages 10-12)
- **10-Year Overall Survival:** 62-77% in treated cohorts (keddie2025poemssyndrome pages 4-7, keddie2025poemssyndrome pages 10-12)

**Prognostic Factors:**

**Favorable Prognostic Indicators:**
- Younger age
- Serum albumin ≥3.2 g/dL
- Complete hematologic response to treatment
- VEGF normalization at 6 months post-treatment (keddie2025poemssyndrome pages 7-10, keddie2025poemssyndrome pages 10-12)

**Adverse Prognostic Indicators:**
- Papilledema (independent adverse factor for overall survival)
- Extravascular volume overload (associated with shorter survival)
- Pulmonary hypertension
- Pleural effusion
- Reduced estimated glomerular filtration rate (cerri2019anupdateon pages 1-2, cerri2019anupdateon pages 2-3, keddie2025poemssyndrome pages 7-10, keddie2025poemssyndrome pages 10-12)

**Prognostic Scores:**
Wang et al. developed a prognostic nomogram incorporating age, pulmonary hypertension, pleural effusion, and eGFR to estimate overall survival and progression-free survival, validated in external cohorts (keddie2025poemssyndrome pages 7-10, keddie2025poemssyndrome pages 10-12).

**Morbidity and Quality of Life:**
- Neurologic disability is the major source of morbidity
- Even with hematologic response, neurologic recovery may be incomplete
- Early treatment critical to prevent irreversible disability (keddie2025poemssyndrome pages 4-7, cerri2019anupdateon pages 3-6)

**Complications:**
- Ischemic stroke (~10% of patients, often watershed distribution)
- Thrombotic events (associated with thrombocytosis and hypercoagulability)
- Respiratory compromise from volume overload/pulmonary hypertension
- Cardiac insufficiency
- Renal dysfunction
- Engraftment syndrome during ASCT (7-15 days post-transplant, can be fatal) (cerri2019anupdateon pages 1-2, keddie2025poemssyndrome pages 7-10, keddie2025poemssyndrome pages 4-7)

## 12. Treatment

A comprehensive table of treatment modalities is presented below:

| Treatment modality/category | Specific therapies/approaches | Indications and patient selection criteria | Response rates and outcomes | Key side effects/considerations | Evidence level/source |
|---|---|---|---|---|---|
| Radiotherapy | Local radiotherapy to isolated plasmacytoma/osteosclerotic lesion(s); typically curative-intent doses **≥40 Gy** | Best for **no bone marrow involvement** and **1–3 bone lesions**; used when disease is focal rather than diffuse/systemic; imaging (especially FDG-PET/CT) helps identify active target lesions and decide focal vs systemic therapy (keddie2025poemssyndrome pages 4-7, keddie2025poemssyndrome pages 10-12) | Mayo cohort cited in review: **6-year PFS 62%** in **82 patients** treated with radiotherapy, with no difference between 1 vs 2 vs 3 lesions; effective but often **slow to work** (keddie2025poemssyndrome pages 4-7) | Slower onset than systemic therapy; may be paired with dexamethasone or lenalidomide/dexamethasone while awaiting response; inappropriate for diffuse marrow/systemic disease (keddie2025poemssyndrome pages 4-7) | Retrospective cohort and expert-review evidence; summarized as standard-of-care for focal disease in review literature (keddie2025poemssyndrome pages 4-7, keddie2025poemssyndrome pages 12-17) |
| Autologous stem cell transplantation (ASCT) | High-dose melphalan-conditioned ASCT (**melphalan 140 or 200**) with supportive optimization/bridging; priming with dexamethasone, thalidomide, or lenalidomide sometimes used before transplant (keddie2025poemssyndrome pages 7-10, keddie2025poemssyndrome pages 4-7) | **Treatment of choice** when radiotherapy is not suitable and patient performance status permits; generally for systemic disease or multifocal involvement; not ideal for frail patients, age **>70**, or major cardiopulmonary compromise without prior optimization (keddie2025poemssyndrome pages 7-10, keddie2025poemssyndrome pages 4-7) | Best outcomes among major modalities in review: **5-year OS 90–95%** and **5-year PFS 63–76%**; review also notes overall contemporary survival improvements in treated cohorts (keddie2025poemssyndrome pages 7-10, keddie2025poemssyndrome pages 4-7) | **Engraftment syndrome** 7–15 days post-transplant: fluid overload/weight gain, respiratory compromise, skin eruption, diarrhea, can be fatal; dexamethasone or lenalidomide pre-optimization may reduce risk; transplant candidacy limited by cardiopulmonary/renal disease and volume overload (keddie2025poemssyndrome pages 7-10, keddie2025poemssyndrome pages 4-7) | Retrospective transplant cohorts and expert reviews; strongest long-term outcome data among therapies in Keddie review (keddie2025poemssyndrome pages 7-10, keddie2025poemssyndrome pages 4-7, keddie2025poemssyndrome pages 10-12) |
| Immunomodulatory drugs (IMiDs): lenalidomide | Lenalidomide plus dexamethasone; low-dose lenalidomide regimens also used; used frontline, relapsed/refractory, or as bridge to later ASCT (keddie2025poemssyndrome pages 7-10, keddie2025poemssyndrome pages 4-7) | Patients **unfit for immediate ASCT**, bridging therapy to improve fitness for later ASCT, relapsed disease, or systemic disease requiring non-transplant therapy (keddie2025poemssyndrome pages 7-10) | Systematic review of **51 patients** cited in review: **≥VGPR 58%**, **PR 37%**, **VEGF reduced in all cases**, **neuropathy improved in 92%**, estimated **12-month PFS 94%**; prospective trial in **18 patients** reported clinical/neurologic improvement, **all alive** at median **39 months**, **3-year PFS 59%** (keddie2025poemssyndrome pages 7-10) | **Prothrombotic**; caution in patients with venous/arterial thrombosis, thrombocytosis, or polycythemia; requires thrombosis-risk assessment; generally favored over thalidomide when neuropathy is prominent (keddie2025poemssyndrome pages 7-10, keddie2025poemssyndrome pages 4-7) | Systematic review, prospective trial, retrospective series summarized in Keddie review (keddie2025poemssyndrome pages 7-10, keddie2025poemssyndrome pages 4-7, keddie2025poemssyndrome pages 12-17) |
| Immunomodulatory drugs (IMiDs): thalidomide | Thalidomide **100–300 mg/day** plus dexamethasone; also sometimes used as transplant-priming/bridging therapy (keddie2025poemssyndrome pages 7-10) | Alternative systemic option where lenalidomide unavailable or unsuitable; has trial evidence but often limited by neurotoxicity (keddie2025poemssyndrome pages 7-10) | J-POST trial of **25 patients**: greater **VEGF reduction** and possible **motor improvement** versus dexamethasone alone; additional support from smaller prospective studies/case series (keddie2025poemssyndrome pages 7-10) | Major limitation is **treatment-emergent neuropathy**; cumulative dose **>50 g** can worsen neuropathy and confound neurologic recovery assessment (keddie2025poemssyndrome pages 7-10) | Randomized placebo-controlled trial plus prospective/case-series evidence summarized in Keddie review (keddie2025poemssyndrome pages 7-10, keddie2025poemssyndrome pages 10-12) |
| Proteasome inhibitors | **Bortezomib**-based combinations, particularly **bortezomib + cyclophosphamide + dexamethasone**; investigational interest in **ixazomib** combinations (keddie2025poemssyndrome pages 7-10) | Systemic disease needing plasma-cell directed therapy, especially when rapid hematologic/VEGF response desired; often considered when ASCT unsuitable or as part of induction strategies (keddie2025poemssyndrome pages 7-10) | Review-cited study of **20 patients**: **complete hematologic response 41%**, **partial response 35%**, **VEGF response 88%**, median **ONLS improved from 5 to 3** (keddie2025poemssyndrome pages 7-10) | **Peripheral neuropathy** can occur with bortezomib and may confound neurologic outcome assessment; newer proteasome inhibitors may be less neurotoxic but data are limited (keddie2025poemssyndrome pages 7-10) | Small prospective/retrospective series; promising but less mature evidence base than ASCT/lenalidomide (keddie2025poemssyndrome pages 7-10) |
| Alkylating agents: melphalan-based | **Melphalan + dexamethasone** for 12 cycles in non-transplant setting; high-dose melphalan also used as ASCT conditioning (separate ASCT row) (keddie2025poemssyndrome pages 7-10, keddie2025poemssyndrome pages 12-17) | Patients not proceeding directly to ASCT and needing systemic therapy; historical standard option in systemic disease (keddie2025poemssyndrome pages 7-10) | Prospective trial cited in review: **31 patients**, **hematologic response 81%**, including **38% complete response**; **100% had VEGF reduction**; **all alive without progression** at median **21 months**; ONLS improved in all within **15 months** (keddie2025poemssyndrome pages 7-10) | Cytotoxic/alkylator toxicity considerations; less favored than ASCT when transplant feasible; used as standard non-transplant systemic regimen in some settings (keddie2025poemssyndrome pages 7-10) | Prospective trial summarized in review (keddie2025poemssyndrome pages 7-10, keddie2025poemssyndrome pages 12-17) |
| Alkylating agents: cyclophosphamide-based | Cyclophosphamide alone or in combinations; also commonly used as **mobilization/bridging** rather than definitive long-term monotherapy in some centers (keddie2025poemssyndrome pages 7-10) | Often used for **stem cell mobilization** or as part of combination regimens; selected when ASCT planned or other chemotherapy needed (keddie2025poemssyndrome pages 7-10) | Retrospective cohorts only; review notes alkylator-based therapy grouped with chemotherapy had **worse 10-year OS (46%)** in Mayo data, likely reflecting **selection bias/poorer baseline fitness** rather than intrinsic inferiority alone (keddie2025poemssyndrome pages 7-10) | Less robust prospective efficacy data; outcomes may appear worse because sicker, non-transplant candidates receive it; role often supportive/bridging rather than preferred definitive therapy (keddie2025poemssyndrome pages 7-10) | Retrospective cohort evidence, expert-practice commentary (keddie2025poemssyndrome pages 7-10) |
| Corticosteroids | **Dexamethasone** alone or in combinations; 40 mg/day for 4 days in some schedules; used with radiotherapy, IMiDs, or as pre-ASCT optimization (keddie2025poemssyndrome pages 7-10, keddie2025poemssyndrome pages 4-7) | Adjunct across many settings: while awaiting radiotherapy effect, in combination systemic therapy, or to reduce fluid overload/inflammatory burden before transplant (keddie2025poemssyndrome pages 4-7) | Usually not curative alone; comparator arm in thalidomide trial was inferior for VEGF reduction; contributes to combination responses and may reduce engraftment syndrome when used pre-ASCT (keddie2025poemssyndrome pages 7-10) | Steroid toxicities; insufficient as sole definitive therapy for most patients; useful as rapid bridge/supportive anti-plasma-cell therapy (keddie2025poemssyndrome pages 7-10, keddie2025poemssyndrome pages 4-7) | Combination-therapy backbone and expert-review guidance rather than stand-alone definitive evidence (keddie2025poemssyndrome pages 7-10, keddie2025poemssyndrome pages 4-7) |
| Anti-VEGF strategy | **Bevacizumab** | Conceptually attractive given high VEGF, but not recommended as routine disease-directed monotherapy (cerri2019anupdateon pages 1-2, keddie2025poemssyndrome pages 1-4, keddie2025poemssyndrome pages 7-10) | Clinical efficacy has been **ambiguous**; no evidence of reliable recovery despite VEGF suppression (cerri2019anupdateon pages 1-2, keddie2025poemssyndrome pages 1-4, keddie2025poemssyndrome pages 7-10) | May be **harmful**; rapid VEGF drop after sustained high levels may trigger endothelial apoptosis/capillary leak; supports concept that VEGF is a **downstream mediator**, not sole initiating driver (cerri2019anupdateon pages 1-2, keddie2025poemssyndrome pages 7-10) | Case reports/series and mechanistic interpretation summarized in reviews (cerri2019anupdateon pages 1-2, keddie2025poemssyndrome pages 7-10) |
| Emerging/ongoing therapies | **Ixazomib + lenalidomide + dexamethasone** clinical investigation; newer proteasome inhibitors (e.g., carfilzomib mentioned as theoretically less neurotoxic but not studied in POEMS); recent unobtainable literature also suggests interest in daratumumab- and ixazomib-based approaches, but detailed source text was not available in context (keddie2025poemssyndrome pages 7-10) | Relapsed/refractory disease, transplant-ineligible disease, or attempts to reduce neurotoxicity/modernize plasma-cell therapy (keddie2025poemssyndrome pages 7-10) | Mayo Clinic trial recruitment for **ixazomib/lenalidomide/dexamethasone (NCT02921893)** was noted in review; mature outcome data not available in retrieved context (keddie2025poemssyndrome pages 7-10) | Evidence still limited; modern myeloma-style combinations are promising but not yet standard on the basis of the retrieved full-text evidence set (keddie2025poemssyndrome pages 7-10) | Early clinical-trial/expert-review level evidence (keddie2025poemssyndrome pages 7-10) |
| Supportive and rehabilitative care | Neuropathic pain treatment (e.g., gabapentin, tricyclic antidepressants), structured rehabilitation, management of endocrine disease, cardiopulmonary monitoring, thrombosis-risk mitigation, transplant fitness optimization (cerri2019anupdateon pages 3-6, keddie2025poemssyndrome pages 4-7) | Indicated for essentially all patients due to chronic disability burden and multisystem involvement (keddie2025poemssyndrome pages 4-7, cerri2019anupdateon pages 3-6) | No disease-control metrics, but critical for function, mobility, quality of life, and enabling definitive therapy; early diagnosis and intervention reduce irreversible neurologic disability (keddie2025poemssyndrome pages 4-7, cerri2019anupdateon pages 3-6) | Must be individualized; neurologic disability may persist despite hematologic response; cardiopulmonary involvement affects eligibility for intensive therapy (keddie2025poemssyndrome pages 4-7, cerri2019anupdateon pages 3-6) | Expert review and clinical management literature (keddie2025poemssyndrome pages 4-7, cerri2019anupdateon pages 3-6) |


*Table: This table summarizes major treatment modalities for POEMS syndrome, including when each approach is used, reported response and survival outcomes, and key toxicities. It is especially useful for comparing focal therapy, transplant-based therapy, and modern systemic plasma-cell directed regimens.*

**Treatment Strategy:**

Treatment is directed at the underlying plasma cell disorder and follows a simple algorithm based on disease extent and patient fitness (keddie2025poemssyndrome pages 7-10, keddie2025poemssyndrome pages 4-7):

**For Localized Disease (1-3 bone lesions, no bone marrow involvement):**
- **Radiotherapy:** Curative-intent doses ≥40 Gy to lesions
- 6-year PFS: 62% in Mayo cohort (keddie2025poemssyndrome pages 4-7)

**For Systemic Disease (diffuse marrow involvement, >3 lesions):**

**If Transplant-Eligible (age <70, adequate performance status):**
- **Autologous Stem Cell Transplantation (ASCT):** Treatment of choice
  - Melphalan 140-200 conditioning
  - 5-year OS: 90-95%
  - 5-year PFS: 63-76%
  - Pre-transplant optimization with dexamethasone or lenalidomide reduces engraftment syndrome risk (keddie2025poemssyndrome pages 7-10, keddie2025poemssyndrome pages 4-7)

**If Transplant-Ineligible or Bridging Therapy:**
- **Lenalidomide + Dexamethasone:** Most efficacious non-transplant option
  - ≥VGPR: 58%, PR: 37%
  - VEGF reduced in 100%
  - Neuropathy improved in 92%
  - 12-month PFS: 94% (keddie2025poemssyndrome pages 7-10)
  - Caution: Prothrombotic; requires thromboprophylaxis in high-risk patients

- **Melphalan + Dexamethasone:**
  - Hematologic response: 81% (38% CR)
  - VEGF reduction: 100%
  - All patients alive at median 21 months in prospective trial (keddie2025poemssyndrome pages 7-10)

- **Bortezomib-based combinations:**
  - CR: 41%, PR: 35%, VEGF response: 88%
  - Risk of treatment-emergent neuropathy (keddie2025poemssyndrome pages 7-10)

- **Thalidomide + Dexamethasone:**
  - Effective but limited by cumulative neuropathy at doses >50g (keddie2025poemssyndrome pages 7-10)

**Therapies to Avoid:**
- **Bevacizumab (anti-VEGF antibody):** Ambiguous results, may be harmful; does not lead to clinical recovery despite VEGF suppression (cerri2019anupdateon pages 1-2, keddie2025poemssyndrome pages 1-4, keddie2025poemssyndrome pages 7-10)

**Supportive Care:**
- Neuropathic pain management (gabapentin, tricyclic antidepressants)
- Physical and occupational rehabilitation
- Endocrinopathy management
- Thromboprophylaxis when indicated
- Cardiovascular monitoring and optimization (keddie2025poemssyndrome pages 4-7, cerri2019anupdateon pages 3-6)

**Treatment Response Biomarkers:**
- VEGF normalization correlates with improved relapse-free survival, grip strength, and CMAP amplitudes at 12 months (keddie2025poemssyndrome pages 10-12)
- Complete VEGF suppression plus complete hematologic response predicts best progression-free and overall survival (keddie2025poemssyndrome pages 10-12)

## 13. Prevention

**Primary Prevention:**
No primary prevention strategies are applicable, as POEMS syndrome is a sporadic acquired plasma cell disorder with no known environmental triggers or hereditary pattern.

**Secondary Prevention (Early Detection):**
- High index of suspicion for POEMS in patients with treatment-resistant "CIDP"
- Screening for monoclonal protein and VEGF in patients with unexplained demyelinating polyneuropathy
- Early recognition critical to prevent irreversible neurologic disability (keddie2025poemssyndrome pages 4-7, latov2014diagnosisandtreatment pages 1-2, cerri2019anupdateon pages 3-6)

**Tertiary Prevention (Preventing Complications):**
- Regular monitoring of VEGF levels during and after treatment
- Cardiovascular assessment before ASCT
- Thromboprophylaxis in high-risk patients (thrombocytosis, on lenalidomide)
- Endocrine monitoring and hormone replacement as needed
- Structured neurologic rehabilitation to optimize functional recovery (keddie2025poemssyndrome pages 4-7)

## 14. Other Species / Natural Disease

No naturally occurring POEMS syndrome has been identified in animal species in the reviewed literature. The disease appears to be unique to humans as a specific plasma cell dyscrasia-associated paraneoplastic syndrome.

## 15. Model Organisms

**Model Organism Availability:**
No dedicated animal model of POEMS syndrome was identified in the retrieved literature. The rarity and complexity of the syndrome, involving specific monoclonal plasma cell proliferation with restricted immunoglobulin gene usage and multisystem cytokine-mediated effects, has precluded development of a comprehensive animal model.

**Related Mechanistic Models:**
While not POEMS-specific, the literature notes that:
- VEGF mechanisms have been studied in neurodegenerative disease models ()
- Plasma cell biology and multiple myeloma models exist but do not recapitulate the POEMS phenotype
- The pathophysiologic role of cytokines like VEGF, IL-6, and TNF-α can be studied in other disease contexts

**Research Applications:**
Without a specific model organism, POEMS research relies on:
- Primary human samples (bone marrow plasma cells, nerve biopsies, serum biomarkers)
- Clinical cohort studies
- Ex vivo culture systems for plasma cells
- Correlative studies of cytokine levels and clinical outcomes

---

## Summary and Knowledge Base Recommendations

**Disease Classification:**
- **MONDO:** MONDO term not confirmed in retrieved literature (recommend mapping)
- **Suggested HPO Terms:** HP:0009830 (Polyneuropathy), HP:0032113 (Monoclonal gammopathy), HP:0002240 (Hepatomegaly), HP:0001744 (Splenomegaly), HP:0000818 (Abnormality of endocrine system), HP:0000953 (Hyperpigmentation of skin), HP:0030934 (Osteosclerosis), HP:0001085 (Papilledema), HP:0000969 (Edema), HP:0001873 (Thrombocytosis)
- **Suggested GO Terms:** GO:0001525 (Angiogenesis), GO:0002526 (Acute inflammatory response), GO:0042035 (Regulation of cytokine biosynthetic process)
- **Cell Types:** CL:0000786 (Plasma cell), CL:0000115 (Endothelial cell)
- **Anatomical Terms:** UBERON:0000010 (Peripheral nervous system), UBERON:0002371 (Bone marrow), UBERON:0002107 (Liver), UBERON:0002106 (Spleen)
- **Biomarkers:** LOINC:34694-0 (VEGF), LOINC:24351-9 (Protein electrophoresis)
- **Treatment Terms:** MAXO terms for radiotherapy, autologous stem cell transplantation, lenalidomide, and supportive care (specific MAXO IDs not confirmed in literature)

**Evidence Quality:**
All information is derived from peer-reviewed literature with PMIDs cited where available. The evidence base includes prospective trials, large retrospective cohorts, whole exome sequencing studies, systematic reviews, and expert consensus guidelines primarily from 2018-2025. The disease is well-characterized due to dedicated international collaborative efforts despite its rarity.

References

1. (cerri2019anupdateon pages 1-2): Federica Cerri, Yuri Matteo Falzone, Nilo Riva, and Angelo Quattrini. An update on the diagnosis and management of the polyneuropathy of poems syndrome. Journal of Neurology, 266:258-267, Sep 2019. URL: https://doi.org/10.1007/s00415-018-9068-4, doi:10.1007/s00415-018-9068-4. This article has 47 citations and is from a domain leading peer-reviewed journal.

2. (keddie2025poemssyndrome pages 1-4): S. Keddie and Michael P Lunn. POEMS Syndrome. Elsevier, Jan 2025. URL: https://doi.org/10.1016/b978-0-323-95702-1.00299-2, doi:10.1016/b978-0-323-95702-1.00299-2. This article has 60 citations.

3. (keddie2025poemssyndrome pages 4-7): S. Keddie and Michael P Lunn. POEMS Syndrome. Elsevier, Jan 2025. URL: https://doi.org/10.1016/b978-0-323-95702-1.00299-2, doi:10.1016/b978-0-323-95702-1.00299-2. This article has 60 citations.

4. (chen2021ahighlyheterogeneous pages 1-2): Jia Chen, Xue-min Gao, Hao Zhao, Hao Cai, Lu Zhang, Xin-xin Cao, Dao-bin Zhou, and Jian Li. A highly heterogeneous mutational pattern in poems syndrome. Dec 2021. URL: https://doi.org/10.1038/s41375-020-01101-4, doi:10.1038/s41375-020-01101-4. This article has 28 citations and is from a highest quality peer-reviewed journal.

5. (chen2021ahighlyheterogeneous pages 2-4): Jia Chen, Xue-min Gao, Hao Zhao, Hao Cai, Lu Zhang, Xin-xin Cao, Dao-bin Zhou, and Jian Li. A highly heterogeneous mutational pattern in poems syndrome. Dec 2021. URL: https://doi.org/10.1038/s41375-020-01101-4, doi:10.1038/s41375-020-01101-4. This article has 28 citations and is from a highest quality peer-reviewed journal.

6. (latov2014diagnosisandtreatment pages 1-2): Norman Latov. Diagnosis and treatment of chronic acquired demyelinating polyneuropathies. Nature Reviews Neurology, 10:435-446, Aug 2014. URL: https://doi.org/10.1038/nrneurol.2014.117, doi:10.1038/nrneurol.2014.117. This article has 208 citations and is from a highest quality peer-reviewed journal.

7. (chen2021ahighlyheterogeneous pages 4-5): Jia Chen, Xue-min Gao, Hao Zhao, Hao Cai, Lu Zhang, Xin-xin Cao, Dao-bin Zhou, and Jian Li. A highly heterogeneous mutational pattern in poems syndrome. Dec 2021. URL: https://doi.org/10.1038/s41375-020-01101-4, doi:10.1038/s41375-020-01101-4. This article has 28 citations and is from a highest quality peer-reviewed journal.

8. (wang2019clinicalandelectrophysiological pages 1-2): Qin Wang, Peng Liu, Li-Li Ji, Shuai Wu, Guo-Dong Feng, Xin Wang, and Ji-Hong Dong. Clinical and electrophysiological profiles in early recognition of polyneuropathy, organomegaly, endocrinopathy, m-protein, and skin changes syndrome. Jul 2019. URL: https://doi.org/10.1097/cm9.0000000000000318, doi:10.1097/cm9.0000000000000318. This article has 11 citations and is from a peer-reviewed journal.

9. (cerri2019anupdateon pages 2-3): Federica Cerri, Yuri Matteo Falzone, Nilo Riva, and Angelo Quattrini. An update on the diagnosis and management of the polyneuropathy of poems syndrome. Journal of Neurology, 266:258-267, Sep 2019. URL: https://doi.org/10.1007/s00415-018-9068-4, doi:10.1007/s00415-018-9068-4. This article has 47 citations and is from a domain leading peer-reviewed journal.

10. (wang2019clinicalandelectrophysiological pages 2-3): Qin Wang, Peng Liu, Li-Li Ji, Shuai Wu, Guo-Dong Feng, Xin Wang, and Ji-Hong Dong. Clinical and electrophysiological profiles in early recognition of polyneuropathy, organomegaly, endocrinopathy, m-protein, and skin changes syndrome. Jul 2019. URL: https://doi.org/10.1097/cm9.0000000000000318, doi:10.1097/cm9.0000000000000318. This article has 11 citations and is from a peer-reviewed journal.

11. (keddie2025poemssyndrome pages 10-12): S. Keddie and Michael P Lunn. POEMS Syndrome. Elsevier, Jan 2025. URL: https://doi.org/10.1016/b978-0-323-95702-1.00299-2, doi:10.1016/b978-0-323-95702-1.00299-2. This article has 60 citations.

12. (keddie2025poemssyndrome pages 12-17): S. Keddie and Michael P Lunn. POEMS Syndrome. Elsevier, Jan 2025. URL: https://doi.org/10.1016/b978-0-323-95702-1.00299-2, doi:10.1016/b978-0-323-95702-1.00299-2. This article has 60 citations.

13. (cerri2019anupdateon pages 3-6): Federica Cerri, Yuri Matteo Falzone, Nilo Riva, and Angelo Quattrini. An update on the diagnosis and management of the polyneuropathy of poems syndrome. Journal of Neurology, 266:258-267, Sep 2019. URL: https://doi.org/10.1007/s00415-018-9068-4, doi:10.1007/s00415-018-9068-4. This article has 47 citations and is from a domain leading peer-reviewed journal.

14. (keddie2025poemssyndrome pages 7-10): S. Keddie and Michael P Lunn. POEMS Syndrome. Elsevier, Jan 2025. URL: https://doi.org/10.1016/b978-0-323-95702-1.00299-2, doi:10.1016/b978-0-323-95702-1.00299-2. This article has 60 citations.

15. (niu2022nerveultrasoundperformances pages 1-2): Jingwen Niu, Qingyun Ding, Jing Fan, Lei Zhang, Jingwen Liu, Yuzhou Guan, Shuang Wu, Liying Cui, and Mingsheng Liu. Nerve ultrasound performances in differentiating poems syndrome from cidp. Neurotherapeutics, 19:455-463, Mar 2022. URL: https://doi.org/10.1007/s13311-022-01209-8, doi:10.1007/s13311-022-01209-8. This article has 17 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](POEMS_Syndrome-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](POEMS_Syndrome-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](POEMS_Syndrome-deep-research-falcon_artifacts/artifact-02.md)