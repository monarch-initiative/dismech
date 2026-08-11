---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-05T18:48:16.633465'
end_time: '2026-07-05T19:04:40.063697'
duration_seconds: 983.43
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Acetaminophen Hepatotoxicity
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 38
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: Acetaminophen_Hepatotoxicity-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Acetaminophen_Hepatotoxicity-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: Acetaminophen_Hepatotoxicity-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acetaminophen Hepatotoxicity
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Acetaminophen Hepatotoxicity** covering all of the
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
- **Disease Name:** Acetaminophen Hepatotoxicity
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Acetaminophen Hepatotoxicity** covering all of the
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


# Comprehensive Research Report: Acetaminophen Hepatotoxicity

## 1. Disease Information

### Overview
Acetaminophen (APAP) hepatotoxicity is a dose-dependent, predictable form of drug-induced liver injury (DILI) caused by overdose of acetaminophen (paracetamol), the world's most widely used analgesic/antipyretic. It represents the clinically most relevant drug hepatotoxicity in Western countries and is the leading cause of acute liver failure (ALF) in the United States and the United Kingdom (jaeschke2024acetaminophenhepatotoxicityparadigm pages 1-3). The condition results from the excessive generation of the reactive metabolite N-acetyl-p-benzoquinone imine (NAPQI) by cytochrome P450 enzymes, primarily CYP2E1, which overwhelms hepatic glutathione (GSH) detoxification capacity and triggers a cascade of mitochondrial dysfunction, oxidant stress, and programmed necrotic cell death in centrilobular hepatocytes (jaeschke2024acetaminophenhepatotoxicityparadigm pages 27-29, jaeschke2024acetaminophenhepatotoxicityparadigm pages 1-3).

### Key Identifiers and Synonyms
The following table summarizes core disease identifiers:

| Disease Name | Common Synonyms | ICD-10 | ICD-11 | MeSH ID | MONDO ID | Disease Category | Primary Cause | Key Molecular Target / Mediators | Primary Affected Organ / Cells | Key Epidemiological Data |
|---|---|---|---|---|---|---|---|---|---|---|
| Acetaminophen hepatotoxicity | Paracetamol hepatotoxicity; acetaminophen-induced liver injury; paracetamol-induced liver injury; APAP hepatotoxicity; APAP-induced acute liver injury; acetaminophen overdose liver injury | **T39.1** Poisoning by 4-aminophenol derivatives | **NEEDS CURATION**: ICD-11 poisoning/toxic liver injury terms are applicable, but a single disease-specific ICD-11 identifier for “acetaminophen hepatotoxicity” was not confirmed from retrieved sources | **D056486** | **Not established from retrieved sources** | Complex; drug-induced liver injury; toxic liver disease; acute liver injury / acute liver failure subtype | Acetaminophen/paracetamol overdose, including intentional self-poisoning and unintentional supratherapeutic ingestion | **CYP2E1**-mediated bioactivation to **NAPQI**; glutathione depletion; mitochondrial protein adducts; JNK pathway activation (jaeschke2024acetaminophenhepatotoxicityparadigm pages 27-29, jaeschke2024acetaminophenhepatotoxicityparadigm pages 1-3, jaeschke2024acetaminophenhepatotoxicityparadigm pages 16-17) | Liver, especially **centrilobular/pericentral hepatocytes** with centrilobular necrosis (umbaugh2024biomarkerdiscoveryin pages 3-4, fernandez2024acuteliverfailure pages 5-7) | Leading cause of acute liver failure in developed countries; ~**46%** of ALF cases in the US and **60%** in the UK are paracetamol-related; overall ALF incidence in developed countries is **1–6 cases per million/year**; APAP overdose is the leading ALF cause in the US and UK (jaeschke2024acetaminophenhepatotoxicityparadigm pages 1-3, fernandez2024acuteliverfailure pages 2-3, fernandez2024acuteliverfailure pages 1-2) |


*Table: This table summarizes core identifiers, synonyms, mechanistic hallmarks, affected anatomy, and high-yield epidemiology for acetaminophen hepatotoxicity. It is useful as a compact knowledge-base entry scaffold anchored to retrieved evidence.*

**Common Synonyms:** Paracetamol hepatotoxicity, acetaminophen-induced liver injury (AILI), paracetamol-induced liver injury, APAP hepatotoxicity, APAP-induced acute liver failure, acetaminophen overdose hepatotoxicity, paracetamol poisoning liver damage.

**Key Identifiers:**
- **ICD-10:** T39.1 (Poisoning by 4-aminophenol derivatives)
- **MeSH:** D056486 (Drug-Induced Liver Injury)
- **MONDO:** MONDO:0005359 (drug-induced liver injury); specific APAP hepatotoxicity sub-ID not established in MONDO at this time
- **CHEBI:** CHEBI:46195 (acetaminophen/paracetamol)

The information in this report is derived from aggregated disease-level resources including clinical registries (Acute Liver Failure Study Group), systematic reviews, mechanistic studies in animal models, and clinical cohorts.

---

## 2. Etiology

### Disease Causal Factors
Acetaminophen hepatotoxicity is caused directly by supratherapeutic doses of acetaminophen. The primary mechanism is metabolic bioactivation: CYP2E1 (and to a lesser extent CYP1A2 and CYP3A4) converts APAP to the highly reactive metabolite NAPQI, which at therapeutic doses is efficiently scavenged by hepatic glutathione (jaeschke2024acetaminophenhepatotoxicityparadigm pages 1-3). At overdose levels, rapid generation of large amounts of NAPQI overwhelms glutathione reserves, causing NAPQI to react with cysteine residues on cellular proteins forming protein adducts, particularly on mitochondrial proteins (jaeschke2024acetaminophenhepatotoxicityparadigm pages 27-29). Approximately half of APAP overdoses are unintentional, often resulting from opioid-acetaminophen drug combinations, while many others represent intentional acts of self-harm (jaeschke2024acetaminophenhepatotoxicityparadigm pages 1-3).

### Risk Factors

**Environmental and Clinical Risk Factors:**
- **Chronic alcohol abuse:** Induces CYP2E1 activity, increasing NAPQI formation (begriche2023acetaminopheninducedhepatotoxicityin pages 3-4)
- **Prolonged fasting and malnutrition:** Depletes hepatic glutathione stores, reducing detoxification capacity (begriche2023acetaminopheninducedhepatotoxicityin pages 3-4)
- **Obesity and NAFLD:** NAFLD patients hospitalized for APAP overdose have a 4–7 fold higher prevalence of acute liver injury compared to those without NAFLD. Obesity-related CYP2E1 induction promotes excessive NAPQI generation and oxidative stress (begriche2023acetaminopheninducedhepatotoxicityin pages 3-4, begriche2023acetaminopheninducedhepatotoxicityin pages 8-9)
- **Older age:** Identified as a predisposing factor (begriche2023acetaminopheninducedhepatotoxicityin pages 3-4)
- **Comedications:** Antituberculosis and antiepileptic drugs can induce CYP enzymes (begriche2023acetaminopheninducedhepatotoxicityin pages 3-4)
- **Diabetes (types 1 and 2):** Associated with altered CYP2E1 activity and metabolic homeostasis (begriche2023acetaminopheninducedhepatotoxicityin pages 3-4)
- **Low basal glutathione levels:** Reduce detoxification capacity for NAPQI (begriche2023acetaminopheninducedhepatotoxicityin pages 8-9)
- **Concomitant hepatitis C infection:** Among APAP overdose patients, those with chronic HCV had higher 3-week mortality (31% vs 17%, p = 0.01) (OpenTargets Search: toxic liver disease)
- **Bariatric surgery:** May predispose to ALF after APAP overdose through rapid weight loss and malnutrition (begriche2023acetaminopheninducedhepatotoxicityin pages 9-11)

**Genetic Susceptibility Factors:**
- **UGT1A polymorphisms:** The UGT1A c.2042C>G polymorphism is associated with increased glucuronidation capacity and paradoxically decreased risk of unintentional APAP-induced ALF, representing a protective genetic factor (begriche2023acetaminopheninducedhepatotoxicityin pages 14-15, begriche2023acetaminopheninducedhepatotoxicityin pages 12-14)
- **CYP2E1 expression/activity variation:** Although CYP2E1 is the primary enzyme generating NAPQI, genetic polymorphisms contributing to inter-individual variation in CYP2E1 activity have been implicated in variable susceptibility (begriche2023acetaminopheninducedhepatotoxicityin pages 6-8)

### Protective Factors
- **Increased volume of distribution** (in obesity): Lowers plasma APAP concentrations (begriche2023acetaminopheninducedhepatotoxicityin pages 1-3, begriche2023acetaminopheninducedhepatotoxicityin pages 9-11)
- **Higher hepatic glucuronidation** (mediated through UGT1A9): Diverts APAP away from toxic oxidative metabolism (begriche2023acetaminopheninducedhepatotoxicityin pages 9-11)
- **Reduced CYP3A4 and CYP1A2 activity** (observed in some obese/NAFLD patients): Decreases NAPQI generation (begriche2023acetaminopheninducedhepatotoxicityin pages 6-8, begriche2023acetaminopheninducedhepatotoxicityin pages 9-11)
- **n-3 polyunsaturated fatty acids:** Provide hepatoprotection through anti-inflammatory and antioxidant properties (begriche2023acetaminopheninducedhepatotoxicityin pages 9-11)
- **Nrf2 antioxidant response pathway activation:** NAPQI directly activates Nrf2, promoting adaptive antioxidant gene expression (jaeschke2024acetaminophenhepatotoxicityparadigm pages 4-6)

### Gene-Environment Interactions
The occurrence and severity of APAP-induced liver injury in an individual depends on a delicate balance between metabolic factors that augment NAPQI generation (CYP2E1 induction by alcohol, obesity, certain drugs) and those that mitigate hepatotoxicity (increased glucuronidation, reduced CYP3A4 activity, higher volume of distribution) (begriche2023acetaminopheninducedhepatotoxicityin pages 1-3). Conditions such as obesity and NAFLD do not uniformly increase APAP hepatotoxicity risk because some metabolic alterations favor toxicity while others limit it (begriche2023acetaminopheninducedhepatotoxicityin pages 6-8).

---

## 3. Phenotypes

### Symptoms and Clinical Signs
- **Early phase (0–24 hours):** Nausea, vomiting, malaise, diaphoresis; patients may be asymptomatic
  - HPO: HP:0002013 (Vomiting); HP:0002018 (Nausea)
- **Hepatic injury phase (24–72 hours):** Right upper quadrant pain, progressive elevation of transaminases (ALT, AST)
  - HPO: HP:0003155 (Elevated alkaline phosphatase); HP:0002910 (Elevated hepatic transaminases)
- **Peak injury/hepatic failure phase (72–96 hours):** Jaundice, coagulopathy (elevated INR ≥ 1.5), hepatic encephalopathy (any degree of mental status alteration), metabolic acidosis, acute kidney injury
  - HPO: HP:0000952 (Jaundice); HP:0001399 (Hepatic failure); HP:0002480 (Hepatic encephalopathy); HP:0001289 (Confusion); HP:0003256 (Coagulopathy)

### Laboratory Abnormalities
- **Alanine aminotransferase (ALT) and aspartate aminotransferase (AST):** Markedly elevated, often >1000 IU/L; notably, at therapeutic doses, up to one-third of healthy volunteers can develop ALT elevations of 3–14 fold after 3 days of treatment (NCT03602274 chunk 1)
  - LOINC: 1742-6 (ALT); 1920-8 (AST)
- **INR (International Normalized Ratio):** Elevated ≥ 1.5, defining ALF when combined with encephalopathy (fernandez2024acuteliverfailure pages 2-3, fernandez2024acuteliverfailure pages 5-7)
- **Serum acetaminophen concentration:** Used for risk stratification via the Rumack-Matthew nomogram
- **APAP-protein adducts (APAP-CYS):** Correlate with peak aminotransferase levels and can be detected up to 12 days post-ingestion, representing specific biomarkers of toxic metabolite exposure (NCT03602274 chunk 1)
- **Metabolic acidosis, elevated lactate, elevated bilirubin, elevated creatinine** (in severe cases with renal involvement)

### Characteristic Pathological Finding
Centrilobular (pericentral) hepatocyte necrosis is the hallmark histological finding, presenting as coagulative confluent hepatocellular necrosis in centrilobular areas (umbaugh2024biomarkerdiscoveryin pages 3-4, fernandez2024acuteliverfailure pages 5-7).

### Quality of Life Impact
Severe APAP hepatotoxicity leading to ALF requires intensive care unit admission, frequently with encephalopathy and multiorgan failure, severely impacting quality of life. Survivors of ALF may experience prolonged recovery. Liver transplant recipients require lifelong immunosuppression.

---

## 4. Genetic/Molecular Information

### Key Genes and Enzymes
- **CYP2E1** (HGNC:2631): Primary cytochrome P450 enzyme responsible for APAP bioactivation to NAPQI. Located at chromosome 10q26.3. CYP2E1 induction by alcohol, obesity, and diabetes is a major determinant of hepatotoxicity severity (jaeschke2024acetaminophenhepatotoxicityparadigm pages 27-29, begriche2023acetaminopheninducedhepatotoxicityin pages 3-4, begriche2023acetaminopheninducedhepatotoxicityin pages 6-8)
- **CYP1A2** (HGNC:2596): Secondary enzyme contributing to NAPQI formation
- **CYP3A4** (HGNC:2637): Another CYP involved in APAP oxidation; reduced activity in some obese patients is protective (begriche2023acetaminopheninducedhepatotoxicityin pages 9-11)
- **UGT1A** (HGNC:12530): UDP-glucuronosyltransferases responsible for APAP glucuronidation (detoxification pathway). The c.2042C>G polymorphism increases glucuronidation capacity and is protective (begriche2023acetaminopheninducedhepatotoxicityin pages 14-15, begriche2023acetaminopheninducedhepatotoxicityin pages 12-14)
- **GCLC** (HGNC:4311): Glutamate-cysteine ligase catalytic subunit, the rate-limiting enzyme for glutathione synthesis. JNK-mediated degradation of GCLC impairs GSH recovery during APAP toxicity (jaeschke2024acetaminophenhepatotoxicityparadigm pages 4-6)
- **GSS** (HGNC:4624): Glutathione synthetase involved in GSH biosynthesis
- **JNK/MAPK8** (HGNC:6881): c-Jun N-terminal kinase, a central signaling kinase whose mitochondrial translocation amplifies APAP-induced hepatocyte death (jaeschke2024acetaminophenhepatotoxicityparadigm pages 6-7, jaeschke2024acetaminophenhepatotoxicityparadigm pages 4-6)

### Pharmacogenomics
Genetic variation in phase I (CYP2E1, CYP1A2, CYP3A4) and phase II (UGT1A, SULT) enzymes contributes to inter-individual variability in APAP metabolism and susceptibility to hepatotoxicity (begriche2023acetaminopheninducedhepatotoxicityin pages 14-15, begriche2023acetaminopheninducedhepatotoxicityin pages 3-4). The UGT1A c.2042C>G polymorphism is the most clearly demonstrated protective genetic variant, associated with decreased risk of unintentional APAP-induced ALF (begriche2023acetaminopheninducedhepatotoxicityin pages 12-14).

### Epigenetic Information
No specific epigenetic changes (DNA methylation, histone modifications) have been definitively established as major determinants of APAP hepatotoxicity susceptibility in current literature, though gene expression regulation through Nrf2 and other transcription factors plays a role in adaptive responses (jaeschke2024acetaminophenhepatotoxicityparadigm pages 4-6).

---

## 5. Environmental Information

### Environmental and Lifestyle Factors
- **Alcohol consumption:** Chronic alcohol use induces CYP2E1, increasing NAPQI production. Alcohol-acetaminophen interactions represent a well-documented adverse drug interaction (begriche2023acetaminopheninducedhepatotoxicityin pages 3-4)
- **Fasting/malnutrition:** Depletes hepatic glutathione, reducing the threshold for APAP toxicity (begriche2023acetaminopheninducedhepatotoxicityin pages 3-4)
- **Diet composition:** Saturated fatty acids (e.g., from butter) increase APAP cytotoxicity more than polyunsaturated fatty acids. n-3 PUFAs may provide hepatoprotection (begriche2023acetaminopheninducedhepatotoxicityin pages 5-6, begriche2023acetaminopheninducedhepatotoxicityin pages 9-11)
- **Polypharmacy:** Combination opioid-APAP products increase risk of unintentional overdose (jaeschke2024acetaminophenhepatotoxicityparadigm pages 1-3)

### Infectious Agents
Chronic hepatitis C infection contributes to worse outcomes in APAP overdose patients (OpenTargets Search: toxic liver disease). No infectious agent directly causes APAP hepatotoxicity; however, pre-existing liver infection/inflammation may lower the threshold for toxicity.

---

## 6. Mechanism/Pathophysiology

The molecular pathogenesis of acetaminophen hepatotoxicity follows a well-characterized cascade, established primarily in mouse models with confirmed translational relevance to human pathophysiology:

| Step Number | Molecular Event | Key Molecules/Proteins Involved | Cellular Location | Timing (in mouse model) | Ontology Terms (GO/CHEBI) |
|---|---|---|---|---|---|
| 1 | CYP2E1-mediated bioactivation of acetaminophen to the reactive metabolite NAPQI | Acetaminophen (APAP), CYP2E1, CYP1A2, CYP3A4, NAPQI | Smooth ER / microsomes of centrilobular hepatocytes | Earliest initiating event; minutes after overdose | GO: xenobiotic metabolic process; GO: monooxygenase activity; CHEBI: acetaminophen; CHEBI: N-acetyl-p-benzoquinone imine (jaeschke2024acetaminophenhepatotoxicityparadigm pages 27-29, jaeschke2024acetaminophenhepatotoxicityparadigm pages 1-3) |
| 2 | Rapid depletion of hepatic glutathione (GSH), reducing detoxification capacity | Glutathione, NAPQI, GCLC | Cytosol and mitochondria | ~30 min | GO: glutathione metabolic process; GO: cellular detoxification; CHEBI: glutathione (jaeschke2024acetaminophenhepatotoxicityparadigm pages 6-7, umbaugh2024biomarkerdiscoveryin pages 3-4) |
| 3 | Covalent protein adduct formation, especially on mitochondrial proteins | NAPQI-protein adducts, cysteine residues on mitochondrial proteins | Mitochondria, especially pericentral hepatocytes | Begins early; adducts detectable by ~2 h | GO: protein alkylation; GO: mitochondrial protein-containing complex; CHEBI: protein adduct (jaeschke2024acetaminophenhepatotoxicityparadigm pages 27-29, umbaugh2024biomarkerdiscoveryin pages 14-15, umbaugh2024biomarkerdiscoveryin pages 3-4) |
| 4 | Mitochondrial oxidant stress initiated by superoxide release from respiratory complex III | Respiratory complex III, superoxide, mitochondrial adducted proteins | Mitochondrial inner membrane / intermembrane space | Early after adduct formation; within first few hours | GO: mitochondrial electron transport, ubiquinol to cytochrome c; GO: superoxide metabolic process; CHEBI: superoxide (jaeschke2024acetaminophenhepatotoxicityparadigm pages 27-29, jaeschke2024acetaminophenhepatotoxicityparadigm pages 4-6) |
| 5 | Redox-sensitive MAPK signaling cascade activates JNK | ASK1, MKK4, JNK, oxidant stress | Cytosol | JNK phosphorylation by ~1–2 h | GO: MAPK cascade; GO: response to oxidative stress; GO: protein phosphorylation (jaeschke2024acetaminophenhepatotoxicityparadigm pages 6-7, jaeschke2024acetaminophenhepatotoxicityparadigm pages 4-6, umbaugh2024biomarkerdiscoveryin pages 3-4) |
| 6 | Phospho-JNK translocates to mitochondria and binds Sab, amplifying dysfunction | p-JNK, Sab (SH3BP5), p-Src, Bax, 14-3-3 | Outer mitochondrial membrane | Peaks around ~6 h; sustained in severe injury | GO: protein targeting to mitochondrion; GO: regulation of mitochondrial membrane permeability; GO: intrinsic apoptotic signaling pathway in response to oxidative stress (jaeschke2024acetaminophenhepatotoxicityparadigm pages 6-7, jaeschke2024acetaminophenhepatotoxicityparadigm pages 4-6, jaeschke2024acetaminophenhepatotoxicityparadigm pages 7-9) |
| 7 | Amplified ROS from complex I and formation of peroxynitrite | Complex I, superoxide, nitric oxide, peroxynitrite, nitrotyrosine | Mitochondrial matrix / inner membrane | First several hours; downstream of JNK mitochondrial signaling | GO: reactive oxygen species metabolic process; GO: nitric oxide metabolic process; GO: protein nitration; CHEBI: nitric oxide; CHEBI: peroxynitrite (jaeschke2024acetaminophenhepatotoxicityparadigm pages 27-29, jaeschke2024acetaminophenhepatotoxicityparadigm pages 6-7, jaeschke2024acetaminophenhepatotoxicityparadigm pages 16-17) |
| 8 | Mitochondrial permeability transition (MPT) and complete membrane depolarization | Cyclophilin D, MPT pore, loss of membrane potential | Mitochondria | After sustained oxidant/peroxynitrite stress; several hours | GO: mitochondrial permeability transition pore complex; GO: regulation of mitochondrial membrane potential; GO: mitochondrial depolarization (jaeschke2024acetaminophenhepatotoxicityparadigm pages 27-29, jaeschke2024acetaminophenhepatotoxicityparadigm pages 7-9) |
| 9 | Release and nuclear translocation of endonucleases causing DNA fragmentation, the “point of no return” | Endonuclease G, AIF, nuclear DNA | Mitochondria to nucleus | Downstream of MPT; several hours, preceding terminal cell death | GO: DNA fragmentation; GO: nuclear DNA catabolic process; GO: protein localization to nucleus (jaeschke2024acetaminophenhepatotoxicityparadigm pages 27-29, jaeschke2024acetaminophenhepatotoxicityparadigm pages 1-3, jaeschke2024acetaminophenhepatotoxicityparadigm pages 7-9) |
| 10 | Programmed oncotic necrosis of hepatocytes | Necrotic hepatocytes, ATP depletion, mitochondrial failure | Centrilobular/pericentral hepatocytes | Major injury phase within ~6–24 h | GO: necrotic cell death; GO: programmed necrotic cell death; GO: loss of plasma membrane integrity (jaeschke2024acetaminophenhepatotoxicityparadigm pages 1-3, jaeschke2024acetaminophenhepatotoxicityparadigm pages 7-9) |
| 11 | Release of DAMPs from necrotic cells | HMGB1, ATP, mitochondrial DNA, nuclear DNA, histones, uric acid | Extracellular space / hepatic sinusoids | Follows necrosis; prominent by ~6–24 h | GO: release of sequestered calcium ion into cytosol; GO: inflammatory response; GO: pattern recognition receptor signaling pathway; CHEBI: ATP; CHEBI: uric acid (jaeschke2024acetaminophenhepatotoxicityparadigm pages 11-12, umbaugh2024biomarkerdiscoveryin pages 6-7) |
| 12 | Sterile inflammation and regenerative response | Kupffer cells, neutrophils, monocyte-derived macrophages, CCL2/MCP-1, CXCL2/MIP-2, IL-10, complement, hepatocyte proliferative programs | Liver sinusoids, necrotic interface, peri-necrotic zones | Neutrophils peak ~24 h; macrophages increase later during repair; regeneration over ~24–96 h | GO: sterile inflammatory response; GO: neutrophil chemotaxis; GO: monocyte chemotaxis; GO: phagocytosis; GO: liver regeneration (jaeschke2024acetaminophenhepatotoxicityparadigm pages 11-12, jaeschke2024acetaminophenhepatotoxicityparadigm pages 12-14, umbaugh2024biomarkerdiscoveryin pages 6-7) |


*Table: This table summarizes the accepted mechanistic sequence of acetaminophen hepatotoxicity from metabolic activation through mitochondrial failure, necrotic death, DAMP release, and inflammatory repair. It is useful for mapping disease biology to ontology terms and timing relationships in the standard mouse model.*

### Detailed Mechanistic Description

**Initiation — Metabolic Bioactivation:** At overdose levels, CYP2E1 in centrilobular hepatocytes metabolizes APAP to the reactive metabolite NAPQI. While therapeutic doses produce small amounts of NAPQI efficiently scavenged by hepatic GSH, overdose levels rapidly deplete GSH stores (within ~30 minutes in mice), allowing NAPQI to form covalent protein adducts, particularly on mitochondrial proteins (jaeschke2024acetaminophenhepatotoxicityparadigm pages 27-29, jaeschke2024acetaminophenhepatotoxicityparadigm pages 1-3, umbaugh2024biomarkerdiscoveryin pages 3-4).

**Amplification — Mitochondrial Dysfunction and JNK Signaling:** Protein adducts on mitochondrial proteins trigger superoxide release from respiratory complex III, directed toward the cytosol. This cytosolic oxidant stress activates the redox-sensitive kinase ASK1, which activates downstream kinases MKK4 and JNK (jaeschke2024acetaminophenhepatotoxicityparadigm pages 4-6). Activated JNK translocates to the mitochondrial outer membrane and binds the scaffold protein Sab (SH3BP5), leading to inactivation of p-Src on the inner membrane, which inhibits electron transport and increases ROS release from respiratory complex I (jaeschke2024acetaminophenhepatotoxicityparadigm pages 6-7). JNK also phosphorylates 14-3-3 proteins, releasing Bax to translocate to mitochondria, and degrades GCLC enzyme, impairing glutathione resynthesis and preventing GSH recovery (jaeschke2024acetaminophenhepatotoxicityparadigm pages 4-6).

**Point of No Return — DNA Fragmentation:** Superoxide radicals from complex I react with nitric oxide to form peroxynitrite, which nitrates mitochondrial proteins and causes irreversible mitochondrial damage (jaeschke2024acetaminophenhepatotoxicityparadigm pages 27-29, jaeschke2024acetaminophenhepatotoxicityparadigm pages 6-7). Persistent peroxynitrite formation combined with loss of mitochondrial membrane potential activates the mitochondrial permeability transition (MPT), regulated by cyclophilin D (jaeschke2024acetaminophenhepatotoxicityparadigm pages 7-9). MPT opening causes mitochondrial swelling and release of intermembrane proteins—endonuclease G and apoptosis-inducing factor (AIF)—which translocate to the nucleus and cause DNA fragmentation, representing the point of no return for cell death (jaeschke2024acetaminophenhepatotoxicityparadigm pages 27-29, jaeschke2024acetaminophenhepatotoxicityparadigm pages 7-9).

**Cell Death Mode:** Despite release of cytochrome c and Smac, apoptosis is not the primary mode of cell death, potentially due to nitrotyrosine modification of these proteins impairing their pro-apoptotic function. The predominant cell death is characterized as programmed oncotic necrosis, with partial overlap of signaling events with apoptosis, ferroptosis, and pyroptosis (jaeschke2024acetaminophenhepatotoxicityparadigm pages 1-3, jaeschke2024acetaminophenhepatotoxicityparadigm pages 7-9).

**Sterile Inflammation and Regeneration:** Necrotic hepatocytes release damage-associated molecular patterns (DAMPs) including HMGB1, mitochondrial DNA, nuclear DNA, ATP, histones, and uric acid, which bind pattern recognition receptors (TLRs, RAGE) on macrophages, triggering cytokine and chemokine expression (jaeschke2024acetaminophenhepatotoxicityparadigm pages 11-12, umbaugh2024biomarkerdiscoveryin pages 6-7). Kupffer cells generate CCL2/MCP-1 to recruit monocytes and produce IL-10 to limit pro-inflammatory responses (jaeschke2024acetaminophenhepatotoxicityparadigm pages 12-14). At moderate overdose doses, neutrophils do not worsen injury but rather promote beneficial conversion of macrophage phenotypes supporting recovery; however, at higher doses, enhanced CXCL2 levels lead to earlier, more severe neutrophil recruitment that aggravates liver injury (jaeschke2024acetaminophenhepatotoxicityparadigm pages 11-12). Monocyte-derived macrophages transition to pro-regenerative phenotypes critical for phagocytic removal of necrotic debris and hepatocyte proliferation (jaeschke2024acetaminophenhepatotoxicityparadigm pages 12-14).

### Key Molecular Pathways
- MAPK/JNK signaling cascade (GO:0000165)
- Glutathione metabolic process (GO:0006749)
- Xenobiotic metabolic process (GO:0006805)
- Mitochondrial permeability transition (GO:0035794)
- Necrotic cell death (GO:0070265)
- Sterile inflammatory response (GO:0002526)
- Liver regeneration (GO:0097421)

### Key Cell Types
- Pericentral/centrilobular hepatocytes (CL:0000182 — hepatocyte)
- Kupffer cells (CL:0000091 — Kupffer cell)
- Hepatic stellate cells
- Neutrophils (CL:0000775)
- Monocyte-derived macrophages (CL:0000860)
- ANXA2+ migratory hepatocytes (novel subpopulation identified in regeneration)

### Advanced Technologies — Single-Cell and Spatial Transcriptomics
Recent single-cell RNA sequencing (scRNA-seq) and spatial transcriptomics studies have provided unprecedented insights into APAP hepatotoxicity. A landmark Nature study by Matchett et al. (2024) used paired snRNA-seq and spatial profiling of healthy and ALF explant human livers to generate the first single-cell, pan-lineage atlas of human liver regeneration, discovering a novel ANXA2+ migratory hepatocyte subpopulation that mediates wound closure following APAP-induced liver injury (OpenTargets Search: toxic liver disease). scRNA-seq has also revealed that p21+ perinecrotic hepatocytes produce CXCL14 after severe APAP overdose, promoting hepatocyte injury and delaying regeneration (OpenTargets Search: toxic liver disease). Single-cell transcriptomics of human 2D and 3D liver microtissues exposed to APAP has revealed dynamic interplay between oxygen availability and drug metabolism, with hypoxic hepatocytes displaying elevated CYP450 expression while conjugation enzymes declined with increasing dose (OpenTargets Search: toxic liver disease).

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary organ:** Liver (UBERON:0002107)
- **Secondary organ involvement:** Kidney (acute kidney injury in severe cases), brain (hepatic encephalopathy)
- **Body systems:** Digestive/hepatobiliary system, urinary system, nervous system (in ALF)

### Tissue and Cell Level
- **Primary tissue:** Hepatic parenchyma, specifically centrilobular (zone 3) hepatocytes (UBERON:0001281 — hepatic lobule)
- **Target cells:** Pericentral hepatocytes (CL:0000182), expressing highest levels of CYP2E1
- **Immune cells involved:** Kupffer cells (CL:0000091), neutrophils (CL:0000775), monocyte-derived macrophages (CL:0000860)
- **Supporting cells:** Hepatic stellate cells, liver sinusoidal endothelial cells

### Subcellular Level
- **Mitochondria** (GO:0005739): Central site of NAPQI-protein adduct formation, oxidant stress, JNK translocation, MPT, and release of endonucleases
- **Endoplasmic reticulum** (GO:0005783): Site of CYP450-mediated bioactivation
- **Nucleus** (GO:0005634): Target of endonuclease G and AIF causing DNA fragmentation
- **Cytosol** (GO:0005829): Site of JNK activation cascade

### Localization
- Centrilobular/pericentral zone (zone 3) of the hepatic lobule (UBERON:0001281)
- Bilateral involvement
- No lateralization

---

## 8. Temporal Development

### Onset
- **Typical age of onset:** Any age; most common in young to middle-aged adults (mean age ~30–40 years in overdose cohorts)
- **Onset pattern:** Acute; typically hyperacute course with rapid progression over 24–72 hours (fernandez2024acuteliverfailure pages 2-3)

### Progression
APAP hepatotoxicity follows a well-defined temporal progression:

**Phase I (0–24 hours):** Anorexia, nausea, vomiting, malaise; patients may appear well. GSH depletion occurs within 30 minutes in mice, with APAP-protein adducts detectable in plasma by 2 hours (preceding ALT elevation) (umbaugh2024biomarkerdiscoveryin pages 3-4).

**Phase II (24–72 hours):** Right upper quadrant pain; progressive rise in ALT/AST; initial coagulopathy.

**Phase III (72–96 hours):** Peak hepatic injury with maximum transaminase elevations (often >10,000 IU/L); hepatic encephalopathy; coagulopathy; metabolic acidosis; risk of multiorgan failure. Maximum abnormalities of liver function are delayed for 3 days or more after overdose (OpenTargets Search: toxic liver disease).

**Phase IV (96 hours–2 weeks):** Resolution or progression to death/transplantation. ALT and necrotic area decline starting at 24 hours (in mice) and return to baseline by 72–96 hours in recoverable cases (umbaugh2024biomarkerdiscoveryin pages 3-4).

### Disease Duration
Self-limited in the majority of cases with early treatment. Progression to ALF occurs in a minority of patients but can be fatal without liver transplantation.

---

## 9. Inheritance and Population

### Epidemiology
- **Incidence of ALF:** 1–6 cases per million population per year in developed countries (fernandez2024acuteliverfailure pages 1-2)
- **APAP as cause of ALF:** Approximately 46% of ALF cases in the US and 60% in the UK (fernandez2024acuteliverfailure pages 2-3)
- **Mortality:** 28% mortality rate for APAP-related ALF (NCT03602274 chunk 1)
- **Only 8% of all emergency liver transplants** for ALF were related to paracetamol overdose, reflecting that most patients recover with appropriate treatment (fernandez2024acuteliverfailure pages 2-3)
- Approximately half of APAP overdoses are unintentional (jaeschke2024acetaminophenhepatotoxicityparadigm pages 1-3)
- Accidental overdoses typically result in more severe injury and are more frequently associated with fatal outcomes compared to intentional cases (jaeschke2024acetaminophenhepatotoxicityparadigm pages 1-3)

### Inheritance Pattern
APAP hepatotoxicity is not a Mendelian genetic disease. It is a complex, multifactorial condition with susceptibility influenced by polygenic variation in drug-metabolizing enzymes (CYP2E1, UGT1A, SULT1A1) interacting with environmental and behavioral factors (begriche2023acetaminopheninducedhepatotoxicityin pages 14-15, begriche2023acetaminopheninducedhepatotoxicityin pages 3-4).

### Population Demographics
- **Geographic distribution:** Most common in developed countries where APAP is widely available; highest rates in the US, UK, Australia, and Northern Europe
- **Sex ratio:** Both sexes affected; some sex-dependent differences in inflammatory responses have been noted in animal models (jaeschke2024acetaminophenhepatotoxicityparadigm pages 24-25)
- The persistence of APAP overdose as a major cause of liver injury is attributed to its widespread availability and presence in numerous combination medications (jaeschke2024acetaminophenhepatotoxicityparadigm pages 1-3)

---

## 10. Diagnostics

### Clinical Tests
- **Serum acetaminophen concentration:** Measured at ≥4 hours post-ingestion; used with the Rumack-Matthew nomogram to stratify risk. The nomogram allows stratification into high-risk (above 300 mg/L at 4 hours) and standard-risk (above 150 mg/L at 4 hours, or >100 mg/L in UK protocols) groups and guides NAC treatment decisions (NCT03602274 chunk 1, OpenTargets Search: toxic liver disease)
- **Serum transaminases (ALT/AST):** Dramatically elevated in hepatotoxicity; maximum values typically delayed 3+ days post-ingestion
- **INR/Prothrombin time:** Elevated INR ≥ 1.5 (with encephalopathy defines ALF)
- **Arterial blood gas and lactate:** Metabolic acidosis with elevated lactate
- **Serum creatinine:** Elevated with concomitant acute kidney injury
- **Serum bilirubin:** Relatively low in hyperacute paracetamol-related ALF compared to other ALF etiologies (fernandez2024acuteliverfailure pages 2-3)

### Biomarkers
- **APAP-protein adducts (APAP-CYS):** Specific biomarkers of toxic APAP metabolite exposure; correlate with peak aminotransferase levels; detectable up to 12 days post-ingestion; point-of-care immunoassays developed (NCT03602274 chunk 1, prescott2024paracetamol(acetaminophen)poisoning pages 6-6)
- **CXCL14:** Novel early prognostic biomarker for poor outcome. In two independent cohorts, circulating CXCL14 concentration outperformed or equaled MELD score for discriminating nonsurvivors from survivors, with AUROC of 0.821 vs 0.787 for MELD; combining MELD and CXCL14 yielded the best AUROC of 0.860 (OpenTargets Search: toxic liver disease)
- **Glutamate dehydrogenase (GDH):** Mitochondrial marker of hepatocyte necrosis (umbaugh2024biomarkerdiscoveryin pages 3-4)
- **HMGB1:** Nuclear/extracellular DAMP marker released from necrotic hepatocytes (prescott2024paracetamol(acetaminophen)poisoning pages 6-6)
- **Keratin-18 (K18):** Sensitive biomarker of hepatocyte injury (prescott2024paracetamol(acetaminophen)poisoning pages 6-6)
- **microRNAs:** miRNA signatures for cell death and regeneration under investigation (prescott2024paracetamol(acetaminophen)poisoning pages 6-6)
- **Carbamoyl phosphate synthetase 1 (CPS1):** Mitochondrial enzyme released during hepatocyte necrosis (umbaugh2024biomarkerdiscoveryin pages 3-4)
- **FABP1, LDH, hepcidin:** Additional biomarkers being evaluated (OpenTargets Search: toxic liver disease)

### Clinical Criteria
- **Rumack-Matthew nomogram:** Standard risk stratification tool for acute single-ingestion APAP overdose, plotting serum APAP concentration vs. time post-ingestion. Not applicable after 24 hours or for chronic/repeated supratherapeutic ingestions (NCT03602274 chunk 1)
- **King's College Criteria:** Prognostic criteria for determining need for liver transplantation in ALF (OpenTargets Search: toxic liver disease)
- **MELD score:** Used for prognostication alongside newer biomarkers

### Histopathology
Coagulative confluent hepatocellular necrosis in centrilobular (zone 3) areas, with relative sparing of periportal hepatocytes (fernandez2024acuteliverfailure pages 5-7).

---

## 11. Outcome/Prognosis

### Survival and Mortality
- Overall mortality rate for APAP-related ALF: approximately 28% (NCT03602274 chunk 1)
- With early NAC treatment (within 8–10 hours of ingestion), hepatotoxicity and death are largely preventable (jaeschke2024acetaminophenhepatotoxicityparadigm pages 14-16)
- Patients with APAP-induced ALF are more likely to die while on the liver transplant waiting list than those with other causes of ALF (OpenTargets Search: toxic liver disease)
- Among ALF patients on transplant waitlists, 28% of deaths were due to cerebral edema complications and the remainder due to multiorgan failure (fernandez2024acuteliverfailure pages 1-2)

### Prognostic Factors
- **Time to treatment:** Early NAC administration within 10 hours is highly effective; efficacy decreases with delayed presentation (jaeschke2024acetaminophenhepatotoxicityparadigm pages 14-16, jaeschke2024acetaminophenhepatotoxicityparadigm pages 27-29)
- **APAP serum concentration relative to nomogram:** Patients above the 300 mg/L line at 4 hours represent high-risk cases requiring intensified treatment (OpenTargets Search: toxic liver disease)
- **Intentional vs. unintentional overdose:** Accidental overdoses are associated with worse outcomes (jaeschke2024acetaminophenhepatotoxicityparadigm pages 1-3)
- **CXCL14 levels:** Higher levels predict poor outcomes (AUROC 0.821) (OpenTargets Search: toxic liver disease)
- **MELD score:** Standard prognostic tool
- **Pre-existing liver disease:** Chronic HCV with APAP overdose had 31% vs 17% 3-week mortality (OpenTargets Search: toxic liver disease)
- **Hepatocyte regeneration markers:** Alpha-fetoprotein (AFP) and osteopontin (OPN) associated with regenerative capacity (umbaugh2024biomarkerdiscoveryin pages 3-4)

### Disease Course
Most patients with appropriate early treatment recover fully. The liver has remarkable regenerative capacity, with hepatocyte proliferation and wound closure restoring liver architecture. A novel ANXA2+ migratory hepatocyte subpopulation mediates necrotic wound closure, which precedes hepatocyte proliferation during regeneration (OpenTargets Search: toxic liver disease).

---

## 12. Treatment

The following table summarizes established and emerging therapeutic options:

| Treatment | Mechanism of Action | Dosing Protocol | Timing/Window | Clinical Status | Key Evidence |
|---|---|---|---|---|---|
| N-acetylcysteine (NAC), IV traditional 3-bag | Replenishes cysteine for hepatic glutathione synthesis; supports detoxification of NAPQI; also scavenges mitochondrial oxidants/peroxynitrite and supports bioenergetics | 150 mg/kg over 15 min to 1 h, then 50 mg/kg over 4 h, then 100 mg/kg over 16 h (total 300 mg/kg over ~20.25–21 h) | Most effective when started within 8–10 h of overdose; may be extended or intensified in massive ingestion, delayed presentation, or persistent toxicity | Standard of care; approved/established antidote | (rumack2025acetylcysteinetreatmentof pages 13-15, rumack2025acetylcysteinetreatmentof pages 10-13, jaeschke2024acetaminophenhepatotoxicityparadigm pages 14-16, rumack2025acetylcysteinetreatmentof pages 7-9) |
| N-acetylcysteine (NAC), IV 2-bag | Same core mechanism as above, with simplified infusion design intended to reduce adverse reactions and streamline delivery | 200 mg/kg over 4 h, then 100 mg/kg over 16 h | Early treatment preferred; considered an alternative simplified IV regimen | Established clinical alternative in some protocols | (rumack2025acetylcysteinetreatmentof pages 10-13, jaeschke2024acetaminophenhepatotoxicityparadigm pages 14-16) |
| N-acetylcysteine (NAC), IV SNAP-style regimen | Same antidotal mechanism; shorter regimen designed to reduce adverse drug reactions while preserving efficacy | 300 mg/kg over 12 h | Early treatment; may support treatment intensification strategies in very large overdoses | Implemented/clinically studied protocol variation | (rumack2025acetylcysteinetreatmentof pages 13-15, rumack2025acetylcysteinetreatmentof pages 10-13, bateman2023largeparacetamoloverdose—higher pages 5-5) |
| N-acetylcysteine (NAC), oral 72-hour regimen | Replenishes glutathione precursors and limits progression of NAPQI-mediated injury | 140 mg/kg loading dose, then 70 mg/kg every 4 h for 17 doses (total 72 h) | Highly effective when begun early; still used where oral therapy is feasible | Established/legacy standard regimen | (rumack2025acetylcysteinetreatmentof pages 10-13, jaeschke2024acetaminophenhepatotoxicityparadigm pages 14-16, rumack2025acetylcysteinetreatmentof pages 7-9) |
| Fomepizole (4-methylpyrazole) | Inhibits CYP2E1-mediated NAPQI formation; also inhibits JNK activation, offering mechanistically distinct protection from NAC | No universally established APAP-specific standard dose from retrieved evidence; used as adjunct with NAC in selected high-risk cases | Considered especially for massive ingestion, delayed presentation, renal injury, or patients above high-risk nomogram lines | Experimental/adjunctive; promising but not standard universal care | (rumack2025acetylcysteinetreatmentof pages 15-17, rumack2025acetylcysteinetreatmentof pages 13-15, jaeschke2024acetaminophenhepatotoxicityparadigm pages 27-29, prescott2024paracetamol(acetaminophen)poisoning pages 6-7) |
| Activated charcoal | Gastrointestinal decontamination to reduce acetaminophen absorption from the gut | Standard toxicology use after recent ingestion; exact dosing not provided in retrieved evidence | Best soon after ingestion, before full absorption | Established supportive intervention in overdose management | (bateman2023largeparacetamoloverdose—higher pages 5-5) |
| Liver transplantation | Replaces failed liver in patients progressing to acute liver failure despite antidotal/supportive care | No dose; candidacy generally based on prognostic criteria such as King's College Criteria | Reserved for fulminant hepatic failure / poor prognosis cases, often late presenters or nonresponders | Established rescue therapy | (prescott2024paracetamol(acetaminophen)poisoning pages 6-7, fernandez2024acuteliverfailure pages 2-3, NCT03602274 chunk 1) |
| Calmangafodipir | Superoxide dismutase mimetic targeting mitochondrial oxidant stress | Investigational; specific dosing not provided in retrieved evidence | Intended for patients at risk of ongoing mitochondrial injury despite NAC | Experimental / clinical investigation | (rumack2025acetylcysteinetreatmentof pages 15-17, bateman2023largeparacetamoloverdose—higher pages 5-5, prescott2024paracetamol(acetaminophen)poisoning pages 6-7) |
| PEG-TPO (thrombopoietin mimetic peptide) | Promotes liver recovery/regeneration in late injury settings when NAC is less effective | Experimental; specific dosing not provided in retrieved evidence | Proposed benefit around ~24 h after overdose in preclinical work | Experimental / preclinical | (rumack2025acetylcysteinetreatmentof pages 15-17) |
| Wharton's Jelly mesenchymal stem cells (MSCs) | Reported to protect mitochondrial function and support hepatic repair/regeneration | Experimental cell therapy; dosing not provided in retrieved evidence | Investigational, likely for delayed/severe injury rather than early detoxification | Experimental / preclinical | (rumack2025acetylcysteinetreatmentof pages 15-17) |


*Table: This table summarizes established and emerging treatments for acetaminophen hepatotoxicity, including mechanisms, dosing frameworks, treatment windows, and evidence status. It is useful for comparing standard antidotal care with adjunctive and experimental strategies.*

### Standard of Care: N-Acetylcysteine (NAC)
NAC is the only clinically approved antidote and remains the standard of care (jaeschke2024acetaminophenhepatotoxicityparadigm pages 14-16). Its mechanism involves providing cysteine for hepatic glutathione resynthesis to scavenge NAPQI and peroxynitrite inside mitochondria, supporting mitochondrial bioenergetics rather than directly reacting with NAPQI (jaeschke2024acetaminophenhepatotoxicityparadigm pages 14-16, jaeschke2024acetaminophenhepatotoxicityparadigm pages 16-17). Early administration within 8–10 hours of overdose is highly effective (jaeschke2024acetaminophenhepatotoxicityparadigm pages 14-16). Multiple IV protocols exist including the traditional three-bag regimen (150 mg/kg over 15 min to 1 hour, then 50 mg/kg over 4 hours, then 100 mg/kg over 16 hours; total 300 mg/kg over ~21 hours) and the SNAP trial protocol (300 mg/kg over 12 hours) (rumack2025acetylcysteinetreatmentof pages 13-15, rumack2025acetylcysteinetreatmentof pages 10-13). The oral protocol consists of 140 mg/kg loading dose followed by 70 mg/kg every 4 hours for 17 additional doses over 72 hours (total 1330 mg/kg) (rumack2025acetylcysteinetreatmentof pages 10-13, rumack2025acetylcysteinetreatmentof pages 7-9). NAC treatment stopping criteria include acetaminophen concentration <10 µg/mL, INR <2.0, normalized or decreasing transaminases, and clinical improvement (rumack2025acetylcysteinetreatmentof pages 13-15). MAXO terms: MAXO:0010033 (drug therapy).

### Fomepizole (4-Methylpyrazole)
Fomepizole offers a mechanistically distinct benefit from NAC by inhibiting CYP2E1-mediated NAPQI formation and preventing JNK activation, making it particularly useful for massive ingestions, delayed presentations, or patients with renal injury where NAC is ineffective (rumack2025acetylcysteinetreatmentof pages 15-17, rumack2025acetylcysteinetreatmentof pages 13-15, jaeschke2024acetaminophenhepatotoxicityparadigm pages 27-29, prescott2024paracetamol(acetaminophen)poisoning pages 6-7). A Phase 2 clinical trial (NCT05517668) was initiated to evaluate fomepizole efficacy in acetaminophen overdose, though it was terminated. MAXO terms: MAXO:0010033 (drug therapy).

### Liver Transplantation
Emergency liver transplantation remains the only curative option for patients with fulminant hepatic failure who do not respond to medical therapy. Candidacy is typically determined by prognostic criteria such as the King's College Criteria (prescott2024paracetamol(acetaminophen)poisoning pages 6-7, fernandez2024acuteliverfailure pages 2-3). MAXO terms: MAXO:0001175 (organ transplantation).

### Experimental Therapies
- **Calmangafodipir:** A superoxide dismutase mimetic targeting mitochondrial oxidant stress, tested alongside NAC in the POP clinical trial (rumack2025acetylcysteinetreatmentof pages 15-17, bateman2023largeparacetamoloverdose—higher pages 5-5, prescott2024paracetamol(acetaminophen)poisoning pages 6-7)
- **PEG-TPO (thrombopoietin mimetic peptide):** Promotes liver recovery at 24 hours when NAC is less effective (rumack2025acetylcysteinetreatmentof pages 15-17)
- **Adenosine A2B receptor activators:** Decrease necrosis and enhance reparative macrophage infiltration (rumack2025acetylcysteinetreatmentof pages 15-17)
- **Wharton's Jelly mesenchymal stem cells:** Protect mitochondrial function (rumack2025acetylcysteinetreatmentof pages 15-17)
- **Lipid-nanoparticle-encapsulated mRNA of growth factors (HGF/EGF):** For enhancing hepatic regeneration in late presentation (rumack2025acetylcysteinetreatmentof pages 15-17, jaeschke2024acetaminophenhepatotoxicityparadigm pages 27-29)

---

## 13. Prevention

### Primary Prevention
- **Dose limitation:** FDA mandate limiting acetaminophen in prescription combination opioid products to 325 mg per dosage unit (OpenTargets Search: toxic liver disease)
- **Package size restrictions:** UK legislation limiting pack sizes of paracetamol sold over the counter
- **Public education:** Awareness campaigns about APAP content in combination medications to prevent unintentional overdose (jaeschke2024acetaminophenhepatotoxicityparadigm pages 1-3)
- **Labeling requirements:** Clear labeling of APAP-containing products
- MAXO terms: MAXO:0000058 (health education)

### Secondary Prevention
- **Early recognition and NAC administration:** The Rumack-Matthew nomogram enables risk stratification within 4 hours of presentation, guiding timely antidote administration (NCT03602274 chunk 1)
- **Novel biomarkers for early detection:** APAP-protein adducts, CXCL14, and K18 offer promise for earlier identification of patients at risk of liver injury (NCT03602274 chunk 1, prescott2024paracetamol(acetaminophen)poisoning pages 6-6, OpenTargets Search: toxic liver disease)
- **Activated charcoal:** GI decontamination within 1–2 hours of ingestion reduces absorption

### Tertiary Prevention
- **Extended NAC treatment:** For patients with persistent toxicity markers
- **Intensified NAC dosing:** Higher doses for patients above the 300 mg/L nomogram treatment line (OpenTargets Search: toxic liver disease)
- **Monitoring for complications:** Serial assessment of hepatic function, coagulation, renal function, and neurological status

---

## 14. Other Species / Natural Disease

### Veterinary Relevance
Acetaminophen hepatotoxicity occurs naturally in several animal species, with particular veterinary importance:
- **Cats** (NCBI Taxon:9685): Extremely sensitive due to deficiency in UGT1A6 (glucuronidation), leading to accumulation of NAPQI; methemoglobinemia is a prominent feature
- **Dogs** (NCBI Taxon:9615): Susceptible to hepatotoxicity at supratherapeutic doses
- **Pigs** (NCBI Taxon:9823): Used as large animal models

### Comparative Biology
The metabolic pathways (CYP2E1-mediated bioactivation, glutathione conjugation, glucuronidation, sulfation) are highly conserved across mammalian species, though relative contributions of individual pathways vary, explaining species-specific susceptibility patterns. Rats are notably less sensitive than mice to APAP hepatotoxicity due to differences in CYP enzyme expression and metabolic capacity.

---

## 15. Model Organisms

### Mouse Models
The mouse is the primary model organism for studying APAP hepatotoxicity, with demonstrated translational relevance to human pathophysiology (jaeschke2024acetaminophenhepatotoxicityparadigm pages 17-19).

**Dose Models:**
- **300 mg/kg APAP (C57Bl/6 mice):** Represents a moderate overdose producing a uniform sequence of pathophysiological events including GSH depletion, JNK phosphorylation, centrilobular necrosis, sterile inflammation, and recovery. Models patients who recover with supportive care (umbaugh2024biomarkerdiscoveryin pages 12-14, umbaugh2024biomarkerdiscoveryin pages 4-6, umbaugh2024biomarkerdiscoveryin pages 3-4)
- **600 mg/kg APAP:** Represents a severe overdose with prolonged injury, decreased hepatocyte proliferation, increased cell cycle arrest, and reduced survival. May better represent patients progressing to ALF (umbaugh2024biomarkerdiscoveryin pages 4-6, umbaugh2024biomarkerdiscoveryin pages 3-4)

**Mouse Strains Used:**
- C57Bl/6, C57Bl/6J, C57Bl/6N (standard strains) (begriche2023acetaminopheninducedhepatotoxicityin pages 5-6)
- FVB/N mice (begriche2023acetaminopheninducedhepatotoxicityin pages 5-6)
- Genetically obese models: db/db, ob/ob mice (begriche2023acetaminopheninducedhepatotoxicityin pages 5-6, begriche2023acetaminopheninducedhepatotoxicityin pages 14-15)
- KK-A(y) diabetic mice (begriche2023acetaminopheninducedhepatotoxicityin pages 14-15)

**Phenotype Recapitulation:**
- Conserved injury mechanisms: APAP bioactivation to NAPQI, mitochondrial toxicity, centrilobular necrosis, and necrosis as the primary cell death mode are all recapitulated (umbaugh2024biomarkerdiscoveryin pages 12-14)
- Biomarkers identified in mice (GDH, mtDNA, nuclear DNA, CPS1, APAP-protein adducts) correlate with human pathology (umbaugh2024biomarkerdiscoveryin pages 12-14)

**Limitations:**
- Significant temporal differences: key events occur much faster in mice than in humans. For example, NAC loses efficacy by 3–6 hours in mice but remains effective up to 8–10 hours in human patients (umbaugh2024biomarkerdiscoveryin pages 4-6)
- Higher APAP doses used relative to human toxic doses
- Some immune responses may differ between species (jaeschke2024acetaminophenhepatotoxicityparadigm pages 24-25)

### Other Models
- **Rat models:** Zucker fa/fa rats, diet-induced NAFLD models; rats are generally less sensitive to APAP hepatotoxicity than mice (begriche2023acetaminopheninducedhepatotoxicityin pages 5-6)
- **In vitro systems:** Primary human hepatocytes, HepaRG cells, L02 cells, hepatocyte-like organoids (HL-ICOs), and 3D spheroid models composed of primary human hepatocytes, Kupffer cells, and liver endothelial cells (begriche2023acetaminopheninducedhepatotoxicityin pages 5-6, OpenTargets Search: toxic liver disease)
- **Resources:** MGI (Mouse Genome Informatics), IMPC (International Mouse Phenotyping Consortium)

---

## Summary

Acetaminophen hepatotoxicity remains a major global public health challenge as the leading cause of drug-induced acute liver failure in developed countries. The pathophysiology is among the most thoroughly understood of any drug toxicity, with a well-defined cascade from CYP2E1-mediated NAPQI formation through mitochondrial dysfunction, JNK-mediated amplification, and programmed necrotic cell death (jaeschke2024acetaminophenhepatotoxicityparadigm pages 27-29, jaeschke2024acetaminophenhepatotoxicityparadigm pages 1-3). N-acetylcysteine remains the standard antidote when administered early, with fomepizole emerging as a promising adjunct for high-risk cases (jaeschke2024acetaminophenhepatotoxicityparadigm pages 14-16, jaeschke2024acetaminophenhepatotoxicityparadigm pages 27-29). Recent advances in single-cell transcriptomics and spatial profiling have uncovered novel aspects of liver regeneration including ANXA2+ migratory hepatocytes and have identified new prognostic biomarkers such as CXCL14 (OpenTargets Search: toxic liver disease). Multiple experimental therapies targeting mitochondrial protection and liver regeneration are under investigation (rumack2025acetylcysteinetreatmentof pages 15-17). The translational relevance of mouse models has been a cornerstone of mechanistic discovery, though important temporal and quantitative differences exist between species (umbaugh2024biomarkerdiscoveryin pages 4-6, jaeschke2024acetaminophenhepatotoxicityparadigm pages 17-19). Prevention strategies including dose limitations, package size restrictions, public education, and early clinical risk stratification via the Rumack-Matthew nomogram remain critical to reducing the burden of this preventable form of liver injury.

References

1. (jaeschke2024acetaminophenhepatotoxicityparadigm pages 1-3): Hartmut Jaeschke and Anup Ramachandran. Acetaminophen hepatotoxicity: paradigm for understanding mechanisms of drug-induced liver injury. Annual review of pathology, 19:453-478, Jan 2024. URL: https://doi.org/10.1146/annurev-pathmechdis-051122-094016, doi:10.1146/annurev-pathmechdis-051122-094016. This article has 250 citations and is from a domain leading peer-reviewed journal.

2. (jaeschke2024acetaminophenhepatotoxicityparadigm pages 27-29): Hartmut Jaeschke and Anup Ramachandran. Acetaminophen hepatotoxicity: paradigm for understanding mechanisms of drug-induced liver injury. Annual review of pathology, 19:453-478, Jan 2024. URL: https://doi.org/10.1146/annurev-pathmechdis-051122-094016, doi:10.1146/annurev-pathmechdis-051122-094016. This article has 250 citations and is from a domain leading peer-reviewed journal.

3. (jaeschke2024acetaminophenhepatotoxicityparadigm pages 16-17): Hartmut Jaeschke and Anup Ramachandran. Acetaminophen hepatotoxicity: paradigm for understanding mechanisms of drug-induced liver injury. Annual review of pathology, 19:453-478, Jan 2024. URL: https://doi.org/10.1146/annurev-pathmechdis-051122-094016, doi:10.1146/annurev-pathmechdis-051122-094016. This article has 250 citations and is from a domain leading peer-reviewed journal.

4. (umbaugh2024biomarkerdiscoveryin pages 3-4): David S Umbaugh and Hartmut Jaeschke. Biomarker discovery in acetaminophen hepatotoxicity: leveraging single-cell transcriptomics and mechanistic insight. Expert Review of Clinical Pharmacology, 17:143-155, Jan 2024. URL: https://doi.org/10.1080/17512433.2024.2306219, doi:10.1080/17512433.2024.2306219. This article has 5 citations and is from a peer-reviewed journal.

5. (fernandez2024acuteliverfailure pages 5-7): Javier Fernández, Octavi Bassegoda, David Toapanta, and William Bernal. Acute liver failure: a practical update. JHEP Reports, 6:101131, Sep 2024. URL: https://doi.org/10.1016/j.jhepr.2024.101131, doi:10.1016/j.jhepr.2024.101131. This article has 80 citations and is from a peer-reviewed journal.

6. (fernandez2024acuteliverfailure pages 2-3): Javier Fernández, Octavi Bassegoda, David Toapanta, and William Bernal. Acute liver failure: a practical update. JHEP Reports, 6:101131, Sep 2024. URL: https://doi.org/10.1016/j.jhepr.2024.101131, doi:10.1016/j.jhepr.2024.101131. This article has 80 citations and is from a peer-reviewed journal.

7. (fernandez2024acuteliverfailure pages 1-2): Javier Fernández, Octavi Bassegoda, David Toapanta, and William Bernal. Acute liver failure: a practical update. JHEP Reports, 6:101131, Sep 2024. URL: https://doi.org/10.1016/j.jhepr.2024.101131, doi:10.1016/j.jhepr.2024.101131. This article has 80 citations and is from a peer-reviewed journal.

8. (begriche2023acetaminopheninducedhepatotoxicityin pages 3-4): Karima Begriche, Clémence Penhoat, Pénélope Bernabeu-Gentey, Julie Massart, and Bernard Fromenty. Acetaminophen-induced hepatotoxicity in obesity and nonalcoholic fatty liver disease: a critical review. Livers, 3:33-53, Jan 2023. URL: https://doi.org/10.3390/livers3010003, doi:10.3390/livers3010003. This article has 36 citations.

9. (begriche2023acetaminopheninducedhepatotoxicityin pages 8-9): Karima Begriche, Clémence Penhoat, Pénélope Bernabeu-Gentey, Julie Massart, and Bernard Fromenty. Acetaminophen-induced hepatotoxicity in obesity and nonalcoholic fatty liver disease: a critical review. Livers, 3:33-53, Jan 2023. URL: https://doi.org/10.3390/livers3010003, doi:10.3390/livers3010003. This article has 36 citations.

10. (OpenTargets Search: toxic liver disease): Open Targets Query (toxic liver disease, 28 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

11. (begriche2023acetaminopheninducedhepatotoxicityin pages 9-11): Karima Begriche, Clémence Penhoat, Pénélope Bernabeu-Gentey, Julie Massart, and Bernard Fromenty. Acetaminophen-induced hepatotoxicity in obesity and nonalcoholic fatty liver disease: a critical review. Livers, 3:33-53, Jan 2023. URL: https://doi.org/10.3390/livers3010003, doi:10.3390/livers3010003. This article has 36 citations.

12. (begriche2023acetaminopheninducedhepatotoxicityin pages 14-15): Karima Begriche, Clémence Penhoat, Pénélope Bernabeu-Gentey, Julie Massart, and Bernard Fromenty. Acetaminophen-induced hepatotoxicity in obesity and nonalcoholic fatty liver disease: a critical review. Livers, 3:33-53, Jan 2023. URL: https://doi.org/10.3390/livers3010003, doi:10.3390/livers3010003. This article has 36 citations.

13. (begriche2023acetaminopheninducedhepatotoxicityin pages 12-14): Karima Begriche, Clémence Penhoat, Pénélope Bernabeu-Gentey, Julie Massart, and Bernard Fromenty. Acetaminophen-induced hepatotoxicity in obesity and nonalcoholic fatty liver disease: a critical review. Livers, 3:33-53, Jan 2023. URL: https://doi.org/10.3390/livers3010003, doi:10.3390/livers3010003. This article has 36 citations.

14. (begriche2023acetaminopheninducedhepatotoxicityin pages 6-8): Karima Begriche, Clémence Penhoat, Pénélope Bernabeu-Gentey, Julie Massart, and Bernard Fromenty. Acetaminophen-induced hepatotoxicity in obesity and nonalcoholic fatty liver disease: a critical review. Livers, 3:33-53, Jan 2023. URL: https://doi.org/10.3390/livers3010003, doi:10.3390/livers3010003. This article has 36 citations.

15. (begriche2023acetaminopheninducedhepatotoxicityin pages 1-3): Karima Begriche, Clémence Penhoat, Pénélope Bernabeu-Gentey, Julie Massart, and Bernard Fromenty. Acetaminophen-induced hepatotoxicity in obesity and nonalcoholic fatty liver disease: a critical review. Livers, 3:33-53, Jan 2023. URL: https://doi.org/10.3390/livers3010003, doi:10.3390/livers3010003. This article has 36 citations.

16. (jaeschke2024acetaminophenhepatotoxicityparadigm pages 4-6): Hartmut Jaeschke and Anup Ramachandran. Acetaminophen hepatotoxicity: paradigm for understanding mechanisms of drug-induced liver injury. Annual review of pathology, 19:453-478, Jan 2024. URL: https://doi.org/10.1146/annurev-pathmechdis-051122-094016, doi:10.1146/annurev-pathmechdis-051122-094016. This article has 250 citations and is from a domain leading peer-reviewed journal.

17. (NCT03602274 chunk 1): Caroline Samer. APAP Hepatotoxicity After Therapeutic Doses. University Hospital, Geneva. 2015. ClinicalTrials.gov Identifier: NCT03602274

18. (jaeschke2024acetaminophenhepatotoxicityparadigm pages 6-7): Hartmut Jaeschke and Anup Ramachandran. Acetaminophen hepatotoxicity: paradigm for understanding mechanisms of drug-induced liver injury. Annual review of pathology, 19:453-478, Jan 2024. URL: https://doi.org/10.1146/annurev-pathmechdis-051122-094016, doi:10.1146/annurev-pathmechdis-051122-094016. This article has 250 citations and is from a domain leading peer-reviewed journal.

19. (begriche2023acetaminopheninducedhepatotoxicityin pages 5-6): Karima Begriche, Clémence Penhoat, Pénélope Bernabeu-Gentey, Julie Massart, and Bernard Fromenty. Acetaminophen-induced hepatotoxicity in obesity and nonalcoholic fatty liver disease: a critical review. Livers, 3:33-53, Jan 2023. URL: https://doi.org/10.3390/livers3010003, doi:10.3390/livers3010003. This article has 36 citations.

20. (umbaugh2024biomarkerdiscoveryin pages 14-15): David S Umbaugh and Hartmut Jaeschke. Biomarker discovery in acetaminophen hepatotoxicity: leveraging single-cell transcriptomics and mechanistic insight. Expert Review of Clinical Pharmacology, 17:143-155, Jan 2024. URL: https://doi.org/10.1080/17512433.2024.2306219, doi:10.1080/17512433.2024.2306219. This article has 5 citations and is from a peer-reviewed journal.

21. (jaeschke2024acetaminophenhepatotoxicityparadigm pages 7-9): Hartmut Jaeschke and Anup Ramachandran. Acetaminophen hepatotoxicity: paradigm for understanding mechanisms of drug-induced liver injury. Annual review of pathology, 19:453-478, Jan 2024. URL: https://doi.org/10.1146/annurev-pathmechdis-051122-094016, doi:10.1146/annurev-pathmechdis-051122-094016. This article has 250 citations and is from a domain leading peer-reviewed journal.

22. (jaeschke2024acetaminophenhepatotoxicityparadigm pages 11-12): Hartmut Jaeschke and Anup Ramachandran. Acetaminophen hepatotoxicity: paradigm for understanding mechanisms of drug-induced liver injury. Annual review of pathology, 19:453-478, Jan 2024. URL: https://doi.org/10.1146/annurev-pathmechdis-051122-094016, doi:10.1146/annurev-pathmechdis-051122-094016. This article has 250 citations and is from a domain leading peer-reviewed journal.

23. (umbaugh2024biomarkerdiscoveryin pages 6-7): David S Umbaugh and Hartmut Jaeschke. Biomarker discovery in acetaminophen hepatotoxicity: leveraging single-cell transcriptomics and mechanistic insight. Expert Review of Clinical Pharmacology, 17:143-155, Jan 2024. URL: https://doi.org/10.1080/17512433.2024.2306219, doi:10.1080/17512433.2024.2306219. This article has 5 citations and is from a peer-reviewed journal.

24. (jaeschke2024acetaminophenhepatotoxicityparadigm pages 12-14): Hartmut Jaeschke and Anup Ramachandran. Acetaminophen hepatotoxicity: paradigm for understanding mechanisms of drug-induced liver injury. Annual review of pathology, 19:453-478, Jan 2024. URL: https://doi.org/10.1146/annurev-pathmechdis-051122-094016, doi:10.1146/annurev-pathmechdis-051122-094016. This article has 250 citations and is from a domain leading peer-reviewed journal.

25. (jaeschke2024acetaminophenhepatotoxicityparadigm pages 24-25): Hartmut Jaeschke and Anup Ramachandran. Acetaminophen hepatotoxicity: paradigm for understanding mechanisms of drug-induced liver injury. Annual review of pathology, 19:453-478, Jan 2024. URL: https://doi.org/10.1146/annurev-pathmechdis-051122-094016, doi:10.1146/annurev-pathmechdis-051122-094016. This article has 250 citations and is from a domain leading peer-reviewed journal.

26. (prescott2024paracetamol(acetaminophen)poisoning pages 6-6): Laurie F. Prescott. Paracetamol (acetaminophen) poisoning: the early years. British Journal of Clinical Pharmacology, 90:127-134, Sep 2024. URL: https://doi.org/10.1111/bcp.15903, doi:10.1111/bcp.15903. This article has 43 citations and is from a domain leading peer-reviewed journal.

27. (jaeschke2024acetaminophenhepatotoxicityparadigm pages 14-16): Hartmut Jaeschke and Anup Ramachandran. Acetaminophen hepatotoxicity: paradigm for understanding mechanisms of drug-induced liver injury. Annual review of pathology, 19:453-478, Jan 2024. URL: https://doi.org/10.1146/annurev-pathmechdis-051122-094016, doi:10.1146/annurev-pathmechdis-051122-094016. This article has 250 citations and is from a domain leading peer-reviewed journal.

28. (rumack2025acetylcysteinetreatmentof pages 13-15): Barry H. Rumack. Acetylcysteine treatment of acetaminophen overdose: foundational and clinical development. Livers, 5:20, Apr 2025. URL: https://doi.org/10.3390/livers5020020, doi:10.3390/livers5020020. This article has 2 citations.

29. (rumack2025acetylcysteinetreatmentof pages 10-13): Barry H. Rumack. Acetylcysteine treatment of acetaminophen overdose: foundational and clinical development. Livers, 5:20, Apr 2025. URL: https://doi.org/10.3390/livers5020020, doi:10.3390/livers5020020. This article has 2 citations.

30. (rumack2025acetylcysteinetreatmentof pages 7-9): Barry H. Rumack. Acetylcysteine treatment of acetaminophen overdose: foundational and clinical development. Livers, 5:20, Apr 2025. URL: https://doi.org/10.3390/livers5020020, doi:10.3390/livers5020020. This article has 2 citations.

31. (bateman2023largeparacetamoloverdose—higher pages 5-5): D. Nicholas Bateman. Large paracetamol overdose—higher dose acetylcysteine is required. British Journal of Clinical Pharmacology, 89:34-38, Feb 2023. URL: https://doi.org/10.1111/bcp.15201, doi:10.1111/bcp.15201. This article has 11 citations and is from a domain leading peer-reviewed journal.

32. (rumack2025acetylcysteinetreatmentof pages 15-17): Barry H. Rumack. Acetylcysteine treatment of acetaminophen overdose: foundational and clinical development. Livers, 5:20, Apr 2025. URL: https://doi.org/10.3390/livers5020020, doi:10.3390/livers5020020. This article has 2 citations.

33. (prescott2024paracetamol(acetaminophen)poisoning pages 6-7): Laurie F. Prescott. Paracetamol (acetaminophen) poisoning: the early years. British Journal of Clinical Pharmacology, 90:127-134, Sep 2024. URL: https://doi.org/10.1111/bcp.15903, doi:10.1111/bcp.15903. This article has 43 citations and is from a domain leading peer-reviewed journal.

34. (jaeschke2024acetaminophenhepatotoxicityparadigm pages 17-19): Hartmut Jaeschke and Anup Ramachandran. Acetaminophen hepatotoxicity: paradigm for understanding mechanisms of drug-induced liver injury. Annual review of pathology, 19:453-478, Jan 2024. URL: https://doi.org/10.1146/annurev-pathmechdis-051122-094016, doi:10.1146/annurev-pathmechdis-051122-094016. This article has 250 citations and is from a domain leading peer-reviewed journal.

35. (umbaugh2024biomarkerdiscoveryin pages 12-14): David S Umbaugh and Hartmut Jaeschke. Biomarker discovery in acetaminophen hepatotoxicity: leveraging single-cell transcriptomics and mechanistic insight. Expert Review of Clinical Pharmacology, 17:143-155, Jan 2024. URL: https://doi.org/10.1080/17512433.2024.2306219, doi:10.1080/17512433.2024.2306219. This article has 5 citations and is from a peer-reviewed journal.

36. (umbaugh2024biomarkerdiscoveryin pages 4-6): David S Umbaugh and Hartmut Jaeschke. Biomarker discovery in acetaminophen hepatotoxicity: leveraging single-cell transcriptomics and mechanistic insight. Expert Review of Clinical Pharmacology, 17:143-155, Jan 2024. URL: https://doi.org/10.1080/17512433.2024.2306219, doi:10.1080/17512433.2024.2306219. This article has 5 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Acetaminophen_Hepatotoxicity-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Acetaminophen_Hepatotoxicity-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](Acetaminophen_Hepatotoxicity-deep-research-falcon_artifacts/artifact-02.md)