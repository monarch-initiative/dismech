---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-19T09:08:15.616633'
end_time: '2026-08-19T09:18:14.398529'
duration_seconds: 598.78
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Cardiac Sarcoidosis
  mondo_id: ''
  category: Immune
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 26
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 3
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Cardiac_Sarcoidosis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Cardiac Sarcoidosis
- **MONDO ID:**  (if available)
- **Category:** Immune

## Research Objectives

Please provide a comprehensive research report on **Cardiac Sarcoidosis** covering all of the
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
- **Disease Name:** Cardiac Sarcoidosis
- **MONDO ID:**  (if available)
- **Category:** Immune

## Research Objectives

Please provide a comprehensive research report on **Cardiac Sarcoidosis** covering all of the
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


# Cardiac Sarcoidosis: Disease-Characteristics Research Report

## Executive summary

Cardiac sarcoidosis (CS; **MONDO:0001707**) is an immune-mediated, non-necrotizing granulomatous myocarditis that may accompany systemic sarcoidosis or occur as apparently isolated cardiac disease. Active granulomatous inflammation and later replacement fibrosis injure the conduction system and myocardium, producing atrioventricular (AV) block, ventricular arrhythmias, heart failure, and sudden cardiac death. Clinical cardiac involvement is recognized in approximately 2–5% of sarcoidosis cases, whereas imaging and autopsy studies suggest much more frequent occult involvement. No single biomarker, gene, or test establishes the diagnosis; contemporary practice integrates clinical phenotype, extracardiac histology, cardiac magnetic resonance (CMR), fluorodeoxyglucose positron-emission tomography (FDG-PET), and selectively targeted endomyocardial biopsy (EMB). (sivalokanathan2024exploringtherole pages 5-7, sivalokanathan2024exploringtherole pages 1-2, trivieri2020challengesincardiac pages 1-3)

The evidence base remains limited. Glucocorticoids are first-line therapy, but randomized evidence defining dose, duration, mortality benefit, or optimal steroid-sparing treatment is lacking. The strongest observational evidence supports recovery of AV conduction and preservation of ventricular function. Recent research emphasizes multimodality imaging, macrophage-directed imaging, IL-1 and JAK inhibition, preclinical inflammatory biomarkers, and genetics-informed phenotype classification. (trivieri2020challengesincardiac pages 4-6, trivieri2020challengesincardiac pages 12-14, NCT06868381 chunk 1, NCT07159074 chunk 1, NCT06660732 chunk 1)

| Domain | Key evidence/data | Suggested ontology terms | Evidence type/limitations |
|---|---|---|---|
| Definition / identifier | Immune-mediated granulomatous myocarditis occurring in systemic sarcoidosis or as isolated cardiac disease; MONDO:0001707 | MONDO:0001707; MeSH: Sarcoidosis; NCIT: Granuloma | Disease-level aggregated literature/resources; no single universally accepted molecular definition (OpenTargets Search: cardiac sarcoidosis, sivalokanathan2024exploringtherole pages 5-7, trivieri2020challengesincardiac pages 1-3) |
| Epidemiology | Clinically recognized cardiac involvement occurs in a minority of sarcoidosis cases, while occult involvement is substantially higher on imaging/autopsy; higher burden reported in Black patients and Northern European populations; adult-onset predominates | HP:0001627 Abnormality of the cardiovascular system; PATO: adult onset | Estimates vary widely by ascertainment method and geography; underdiagnosis is common (sivalokanathan2024exploringtherole pages 5-7, sivalokanathan2024exploringtherole pages 1-2, trivieri2020challengesincardiac pages 1-3, sivalokanathan2024exploringtherole pages 4-5, poyhonen202430yeartrendsin pages 11-11) |
| Etiology / genetics | Multifactorial disease with immune, environmental, and genetic contributions; familial clustering reported; HLA and non-HLA susceptibility associations implicated, but no established monogenic causal gene for cardiac sarcoidosis | GO:0001817 regulation of cytokine production; HP:0000007 Autosomal recessive inheritance not established; HP:0012275 Multifactorial inheritance | Mostly association data and extrapolation from systemic sarcoidosis; gene-level target evidence remains sparse (OpenTargets Search: cardiac sarcoidosis, sivalokanathan2024exploringtherole pages 5-7, trivieri2020challengesincardiac pages 4-6, zoppa2024phenotypesandserum pages 9-11, kullberg2024unravelinggeneticmysteries pages 1-5) |
| Phenotypes | Common presentations include atrioventricular block, bundle branch block, ventricular arrhythmias, premature ventricular complexes, heart failure, reduced LVEF, syncope, and sudden cardiac death; isolated and systemic forms both occur | HP:0011710 Atrioventricular block; HP:0001644 Dilated cardiomyopathy; HP:0001663 Ventricular arrhythmia; HP:0001279 Syncope; HP:0001645 Sudden cardiac death | Phenotype frequencies depend on referral cohort and diagnostic pathway; many cases are subclinical (sivalokanathan2024exploringtherole pages 5-7, sivalokanathan2024exploringtherole pages 1-2, trivieri2020challengesincardiac pages 20-21, sivalokanathan2024exploringtherole pages 4-5) |
| Immune mechanism | Non-necrotizing granulomas composed of macrophages/epithelioid cells and CD4+ T cells; Th1-skewed cytokines (IL-2, TNF, IFN-γ) promote granulomatous inflammation, with downstream fibrosis and electrical instability | GO:0006954 inflammatory response; GO:0001816 cytokine production; CL:0000623 natural killer cell; CL:0000863 inflammatory macrophage; CL:0000624 CD4-positive, alpha-beta T cell | Mechanistic model derived largely from systemic sarcoidosis plus cardiac clinicopathologic correlation; causative antigen(s) unresolved (sivalokanathan2024exploringtherole pages 5-7, trivieri2020challengesincardiac pages 1-3, trivieri2020challengesincardiac pages 4-6) |
| Anatomy | Primary site is myocardium, especially ventricular myocardium and conduction system; right ventricular involvement can occur; downstream effects include scar/fibrosis and ventricular dysfunction | UBERON:0002084 heart; UBERON:0002349 myocardium; UBERON:0002405 cardiac ventricle; UBERON:0010000 cardiac conduction system | Imaging-pathology concordance is strong, but lesion distribution is patchy (trivieri2020challengesincardiac pages 20-21, trivieri2020challengesincardiac pages 9-11) |
| Diagnostics | EMB is highly specific but insensitive because of patchy disease; reported EMB sensitivity ~20–30% (unguided yield ~25%, up to ~50% with image/voltage guidance). CMR with LGE: sensitivity ~91–99% and specificity ~98–100% in one review; extracardiac-screening studies report sensitivity 75–100% and specificity 76–78%. FDG-PET: sensitivity ~71–91% and specificity ~74–89%; meta-analytic benchmark often cited near 89%/78% | NCIT: Endomyocardial Biopsy; NCIT: Cardiac Magnetic Resonance Imaging; NCIT: Positron Emission Tomography; HP:0030972 Late gadolinium enhancement | Performance varies by preparation protocol, case definition, and cohort enrichment; HRS/WASOG/JCS criteria are not fully concordant (nagai2026thediagnosisand pages 4-6, trivieri2020challengesincardiac pages 9-11) |
| Prognosis | Major risks are ventricular tachyarrhythmia, heart failure progression, conduction disease, and sudden death; combined perfusion defect plus abnormal FDG uptake linked to ~4-fold higher annual VT/death rates; RV FDG uptake linked to ~5-fold higher event rates | HP:0001644 Dilated cardiomyopathy; HP:0004756 Ventricular tachycardia; HP:0001635 Congestive heart failure; HP:0001645 Sudden cardiac death | Prognosis is strongly imaging-dependent; survival estimates vary and recent nationwide numeric survival data were not fully extractable here (sivalokanathan2024exploringtherole pages 5-7, trivieri2020challengesincardiac pages 9-11) |
| Treatment response | First-line therapy is glucocorticoids; reasonable initial prednisone dose often 30–40 mg/day. In systematic review, AV conduction improved in 76/178 (42.7%) treated patients versus 0/21 untreated; combined steroid plus steroid-sparing therapy may reduce relapse compared with steroids alone | NCIT: Prednisone; NCIT: Methotrexate; NCIT: Azathioprine; NCIT: Mycophenolate Mofetil; NCIT: Infliximab; NCIT: Implantable Cardioverter-Defibrillator | No randomized standard-of-care trials for most agents; evidence mostly observational, with stronger support for AV block and LVEF stabilization than for mortality reduction (trivieri2020challengesincardiac pages 12-14) |
| Active experimental trials | Phase 2/2a studies are testing IL-1 and JAK-axis inhibition and new imaging approaches: rilonacept (REPAIR-CS), baricitinib, Tc-99m tilmanocept SPECT/CT, 64Cu-DOTATATE macrophage PET/CT, SGLT1/2-assisted myocardial glucose suppression for FDG-PET, PET/MRI prognostic studies, diagnostic-criteria and biomaterial registries, and a cardiac sarcoidosis QoL tool study | NCIT: Rilonacept; NCIT: Baricitinib; NCIT: Anakinra; NCIT: Single Photon Emission Computed Tomography; NCIT: Positron Emission Tomography/Magnetic Resonance Imaging | Most are early-phase, small, single-center, and without posted results yet; endpoints are commonly imaging-based rather than hard outcomes (NCT06868381 chunk 1, NCT07159074 chunk 1, NCT06660732 chunk 1, NCT04017936 chunk 2) |


*Table: This compact table summarizes the main knowledge-base domains for cardiac sarcoidosis, including disease definition, pathobiology, diagnostics, prognosis, treatment response, and ongoing trials. It is designed as a concise scaffold for a fuller cited report.*

## 1. Disease information

### Definition and scope

CS is best defined as **granulomatous inflammation of the myocardium**, with or without clinically evident extracardiac sarcoidosis. Histology shows compact, non-necrotizing granulomas containing macrophages/epithelioid histiocytes, multinucleated giant cells, and predominantly CD4-positive T lymphocytes. This finding is characteristic but not pathognomonic; infectious and other inflammatory causes must be excluded. A useful exact statement from a 2024 review is: **“Sarcoidosis is a multifaceted and multisystemic inflammatory disorder, the etiology of which remains unknown.”** [Sivalokanathan, June 2024; DOI URL: https://doi.org/10.3390/cardiogenetics14020009]. (sivalokanathan2024exploringtherole pages 5-7, sivalokanathan2024exploringtherole pages 1-2, trivieri2020challengesincardiac pages 1-3)

### Identifiers and synonyms

- **MONDO:** MONDO:0001707, cardiac sarcoidosis. Open Targets recognizes this entity but returned no curated disease–target associations, consistent with the absence of an established single therapeutic target or causal gene. (OpenTargets Search: cardiac sarcoidosis)
- **MeSH:** *Sarcoidosis* and *Heart Diseases* are generally combined; a unique cardiac-sarcoidosis MeSH descriptor was not established in the retrieved evidence.
- **ICD-10-CM:** D86.85, sarcoid myocarditis, is the most specific commonly used code; coding systems may also use D86.9 plus a cardiac-manifestation code.
- **ICD-11, OMIM, Orphanet:** no confidently verified disease-specific identifier was recovered. CS is not an established Mendelian OMIM disorder.
- **Synonyms:** sarcoid myocarditis, myocardial sarcoidosis, cardiac involvement in sarcoidosis, isolated cardiac sarcoidosis, sarcoid cardiomyopathy.
- **Data provenance:** the report concerns **aggregated disease-level evidence**, not individual EHR records. Cohort statistics may nevertheless originate from registries, imaging databases, pathology series, or administrative health records.

## 2. Etiology, risk, and protective factors

### Causal model

The cause is unknown and is probably multifactorial: genetically susceptible individuals encounter one or more environmental or microbial antigens, develop persistent antigen presentation and Th1-skewed cellular immunity, form granulomas, and subsequently develop myocardial injury and fibrosis. This is susceptibility rather than classical Mendelian causation. (sivalokanathan2024exploringtherole pages 5-7, trivieri2020challengesincardiac pages 1-3, trivieri2020challengesincardiac pages 4-6)

### Genetic susceptibility

Familial clustering is reported in approximately 3.6–9.6% of sarcoidosis, monozygotic twins have markedly elevated risk, and first-degree relatives of affected Black patients have approximately threefold higher risk. A 2024 review cites an approximately 80-fold twin risk, although that estimate pertains to sarcoidosis broadly rather than specifically to cardiac involvement. HLA and non-HLA alleles influence susceptibility and phenotype; reported cardiac associations include **HLA-DQB1*06:01**, but replication and ancestry-specific interpretation are required. (sivalokanathan2024exploringtherole pages 5-7)

Recent systemic-sarcoidosis studies provide candidate phenotype modifiers rather than CS-causal genes. An ocular-cardio-cutaneous-CNS phenotype was associated with **LOC102723568** and **TLR3** variants; other extrapulmonary associations included **CCL18, RAB23,** and **ZNF451**. A December 2024 preprint found chronicity associations at rs3135356 (OR 3.13), rs2395162 (OR 2.34), and rs1049550 (OR 0.68), with gene-based signals at **CLIC1** and **ANXA11**. These findings are not validated CS diagnostic variants. (zoppa2024phenotypesandserum pages 9-11, kullberg2024unravelinggeneticmysteries pages 1-5)

**Knowledge-base conclusion:** no established causal gene, pathogenic germline variant, somatic variant, chromosomal abnormality, inheritance pattern, penetrance estimate, carrier frequency, founder mutation, or clinically actionable modifier gene exists for CS. Accordingly, ClinVar-style pathogenic-variant classification, gnomAD carrier frequencies, cascade genetic testing, and genotype-directed treatment are **not applicable at present**. Open Targets likewise returned zero associated targets for MONDO:0001707. (OpenTargets Search: cardiac sarcoidosis)

### Environment, occupation, lifestyle, and infection

Reported sarcoidosis associations include musty odors, pine pollen, insecticides, and occupational exposure to metals, talc, or silica. These are epidemiological signals, not proven CS-specific causes. Putative microbial antigens—particularly *Cutibacterium acnes* and mycobacterial antigens—remain hypotheses; sarcoidosis is not considered contagious, and no infectious agent fulfills causal criteria. Smoking, alcohol, diet, and exercise have no validated CS-specific causal or protective effect. (sivalokanathan2024exploringtherole pages 5-7)

### Protective factors and gene–environment interaction

No reproducible genetic protective variant or environmental protective intervention has been established for CS. The leading interaction model is HLA-dependent antigen presentation after exposure, followed by persistent macrophage–T-cell activation. This model is biologically plausible but has not yielded a validated individual risk calculator.

## 3. Phenotypes

CS is predominantly adult-onset, often insidious, but may present abruptly with high-grade AV block, sustained ventricular tachycardia (VT), or cardiac arrest. Severity and progression are highly variable; silent inflammation, episodic activity, chronic scar, and progressive cardiomyopathy can coexist. (sivalokanathan2024exploringtherole pages 1-2, sivalokanathan2024exploringtherole pages 4-5)

| Phenotype | Characteristics and impact | Suggested HPO term |
|---|---|---|
| AV/conduction block | Common sentinel presentation, especially unexplained high-grade block in a younger or middle-aged adult; may cause presyncope, syncope, fatigue, or sudden death | HP:0011710 Atrioventricular block; HP:0031546 Complete heart block |
| Bundle-branch/intraventricular conduction delay | Reflects septal or conduction-system disease; variable and potentially progressive | HP:0011711 Abnormality of cardiac conduction |
| Premature ventricular complexes/VT/VF | Episodic palpitations or syncope through sustained VT, ventricular fibrillation, and arrest; major QoL and mortality burden | HP:0004308 Ventricular premature beat; HP:0004756 Ventricular tachycardia; HP:0001663 Ventricular arrhythmia |
| Heart failure/reduced LVEF | Dyspnea, exercise intolerance, edema, and advanced pump failure; severity ranges from mild dysfunction to transplantation | HP:0001635 Congestive heart failure; HP:0001644 Dilated cardiomyopathy; HP:0012664 Reduced ejection fraction |
| Sudden cardiac death | May be the first recognized manifestation; one review cites rates up to 14% in selected CS populations | HP:0001645 Sudden cardiac death (sivalokanathan2024exploringtherole pages 5-7) |
| Syncope/presyncope | Usually secondary to bradyarrhythmia or tachyarrhythmia and materially restricts driving and employment | HP:0001279 Syncope |
| Atrial arrhythmia | Atrial fibrillation and other supraventricular arrhythmias occur but are less specific | HP:0005110 Atrial fibrillation |
| Pericardial involvement/chest pain | Less frequent; may mimic ischemia or myocarditis | HP:0001698 Pericardial effusion; HP:0100749 Chest pain |
| Subclinical myocardial inflammation/scar | Abnormal CMR or PET despite absent cardiac symptoms; approximately 20–25% of pulmonary/systemic cases may harbor silent cardiac disease in some series | HP:0030972 Late gadolinium enhancement (sivalokanathan2024exploringtherole pages 4-5) |

Formal per-phenotype prevalence estimates are difficult to generalize because referral, diagnostic, and device cohorts differ markedly. Sarcoidosis overall can remit spontaneously, but scar-mediated CS may remain arrhythmogenic after inflammation resolves. A completed 130-participant study, NCT05145023, was designed to develop and validate a CS-specific health-related QoL instrument, reflecting a recognized gap in disease-specific patient-reported outcomes.

## 4. Genetic and molecular information

CS is **polygenic/multifactorial**, not a monogenic cardiomyopathy. There is therefore no recommended “CS gene panel.” In an apparent isolated inflammatory/arrhythmogenic cardiomyopathy, a hereditary cardiomyopathy panel or exome/genome sequencing may instead identify a phenocopy—such as desmosomal arrhythmogenic cardiomyopathy, LMNA-related cardiomyopathy, or other inherited disease—but does not confirm sarcoidosis.

Candidate pathways include HLA class II antigen presentation, **TNF/NF-κB**, interferon signaling, Toll-like receptor signaling, chemokine axes such as CXCL9/CXCL10–CXCR3, and possibly mTOR-related macrophage persistence. Systemic-sarcoidosis network analysis identified 493 viral-defense/innate-immunity genes and 684 genes related to noncoding-RNA processes; these remain research-level observations rather than clinical molecular diagnostics. (zoppa2024phenotypesandserum pages 9-11)

Epigenetic, cardiac single-cell, spatial-transcriptomic, proteomic, metabolomic, and lipidomic data remain sparse. Spatial transcriptomics and mass-spectrometry imaging are emerging methods for mapping sarcoid granulomas, but no clinically validated CS molecular signature has resulted. Absence of a curated Open Targets association further argues against assigning a single causal protein. (OpenTargets Search: cardiac sarcoidosis)

## 5. Environmental information

Organic and inorganic exposures may initiate disease in susceptible hosts, but no exposure is necessary or sufficient. Occupational histories should document metal work, mineral/silica or talc exposure, insecticides, mold/musty environments, and relevant infectious risks because these also inform the differential diagnosis. There is no evidence-based dietary or exercise intervention that prevents granuloma formation. Exercise prescriptions should instead be individualized after arrhythmia and ventricular-function assessment. (sivalokanathan2024exploringtherole pages 5-7)

Immunosuppressed patients require ordinary infection-risk mitigation, vaccination review, and latent tuberculosis/hepatitis screening before biologic therapy. These measures prevent treatment complications, not CS itself.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream susceptibility and trigger:** HLA/non-HLA background plus unidentified inhaled, occupational, or microbial antigen.
2. **Antigen presentation:** recruited monocytes differentiate into macrophages/antigen-presenting cells and activate CD4-positive T cells.
3. **Granuloma formation:** Th1 cytokines—IL-2, TNF-α, and IFN-γ—maintain macrophage activation. Macrophages release IL-1, IL-6, IL-8, IL-12, IL-15, IL-18, and TNF-α. (trivieri2020challengesincardiac pages 4-6)
4. **Active myocardial injury:** patchy edema and inflammatory-cell infiltration injure cardiomyocytes and conduction tissue; glucose-avid immune cells produce focal FDG uptake.
5. **Downstream remodeling:** granulomas resolve, persist, or evolve into replacement fibrosis. Scar causes conduction slowing, re-entry VT, wall-motion abnormalities, reduced LVEF, and heart failure.
6. **Clinical manifestations:** AV block, VT/VF, syncope, heart failure, or sudden death. Continued arrhythmia after PET normalization can reflect fixed scar rather than active inflammation.

A possible Th1-to-Th2 transition may favor fibrosis in chronic disease. No protein misfolding, enzyme deficiency, ion-channel mutation, or primary metabolic block defines CS. Metabolic imaging instead exploits increased glucose consumption by activated inflammatory cells. (trivieri2020challengesincardiac pages 4-6)

**Suggested GO biological-process terms:** GO:0006954 inflammatory response; GO:0071222 cellular response to lipopolysaccharide/antigenic stimulus where contextually justified; GO:0001816 cytokine production; GO:0042110 T-cell activation; GO:0006955 immune response; GO:0002376 immune system process; GO:0001525 angiogenesis; GO:0042060 wound healing; GO:0030198 extracellular-matrix organization; GO:0062023 collagen-containing extracellular matrix.

**Suggested Cell Ontology terms:** CL:0000235 macrophage; CL:0000863 inflammatory macrophage; CL:0000624 CD4-positive alpha-beta T cell; CL:0000813 memory T cell; CL:0000576 monocyte; CL:0000182 hepatocyte-like “epithelioid” is inappropriate—use macrophage lineage plus pathology annotation; CL:0000746 cardiac muscle cell; CL:0000057 fibroblast.

## 7. Anatomical structures affected

- **Primary organ:** heart, particularly patchy ventricular myocardium and the conduction system. Suggested terms: UBERON:0000948 heart, UBERON:0002349 myocardium, UBERON:0002084 cardiac muscle tissue, UBERON:0002405 cardiac ventricle.
- **Common sites:** basal interventricular septum, left-ventricular subepicardial/mid-wall myocardium, papillary muscles, and right ventricle. Distribution is often multifocal and asymmetric rather than lateralized.
- **Cells/tissues:** cardiomyocytes are injured secondarily; macrophages, giant cells, lymphocytes, fibroblasts, and collagenous scar dominate lesions.
- **Subcellular level:** no disease-specific organelle lesion is established. Nuclear transcriptional programs, macrophage lysosomal/phagocytic compartments, mitochondria under inflammatory stress, and extracellular matrix are relevant but nonspecific.
- **Secondary organs:** lungs and thoracic lymph nodes are most frequent systemic sites; skin, eyes, nervous system, liver, and other organs may provide safer biopsy targets. More than 90% of systemic sarcoidosis patients may have an abnormal chest radiograph, with bilateral hilar adenopathy in 50–85% and parenchymal opacity in 20–65%. (sivalokanathan2024exploringtherole pages 1-2)

## 8. Temporal development

Typical onset is adult, commonly between 25 and 45 years for sarcoidosis broadly, although later presentation occurs. Disease may be acute—e.g., sudden AV block or VT—or chronic and insidious. Systemic sarcoidosis is often categorized as acute (≤2 years) or chronic/persistent (approximately ≥3–5 years), but this staging does not map cleanly onto cardiac activity. (sivalokanathan2024exploringtherole pages 4-5)

A practical cardiac sequence is: subclinical inflammation → clinically active granulomatous myocarditis → mixed inflammation and fibrosis → scar-dominant cardiomyopathy. Activity fluctuates, and relapse may follow immunosuppression withdrawal. Early immunosuppression before marked LVEF decline appears more effective; treatment within six months was associated with LVEF improvement, whereas delay beyond six months predicted poorer response in observational data. (trivieri2020challengesincardiac pages 12-14)

For sarcoidosis overall, 30–50% or more may remit spontaneously, but cardiac involvement is not safely managed by extrapolating pulmonary remission rates. A 2024 Swedish nested case–control study found 44 inflammatory plasma proteins elevated before diagnosis among 152 cases and 341 controls; mean lead time was 13.4 years, and 27 remained associated ≥10 years before diagnosis. This supports a preclinical inflammatory phase, although it was not CS-specific. [Arkema et al., September 2024; https://doi.org/10.1183/13993003.00277-2024].

## 9. Inheritance and population

Sarcoidosis prevalence estimates vary from approximately 1–40 per 100,000 globally to 141–160 per 100,000 in selected northern-latitude populations; incidence estimates span approximately 1–36 per 100,000/year. Clinical CS occurs in about 2–5% of sarcoidosis, whereas imaging or autopsy detects myocardial involvement in approximately 20–25% and, in selected postmortem series, 25–58%. These ranges must not be conflated: they reflect different case definitions and ascertainment. (sivalokanathan2024exploringtherole pages 5-7, sivalokanathan2024exploringtherole pages 1-2, trivieri2020challengesincardiac pages 1-3, sivalokanathan2024exploringtherole pages 4-5, zoppa2024phenotypesandserum pages 1-2)

Black/African-American and Northern European populations have a higher systemic burden; African-American patients may present roughly a decade earlier and with more severe disease. Japanese cohorts have historically shown a disproportionate cardiac contribution to sarcoidosis mortality. Sex estimates vary by cohort, but systemic sarcoidosis generally shows modest female predominance, approximately 1.2–1.5:1 in a recent review. (trivieri2020challengesincardiac pages 1-3, zoppa2024phenotypesandserum pages 1-2)

A 2024 Finnish nationwide study documented increasing recognized CS incidence over 30 years, likely reflecting heightened awareness and advanced imaging as well as possible true change. Precise cohort estimates were not recoverable from the available excerpt and should not be inferred. [Pöyhönen et al., August 2024; https://doi.org/10.1016/j.jacadv.2024.101102]. (poyhonen202430yeartrendsin pages 11-11)

Classical inheritance concepts—autosomal dominant/recessive transmission, penetrance, anticipation, germline mosaicism, carrier frequency, and consanguinity—are not applicable.

## 10. Diagnostics

### Diagnostic criteria

Three major frameworks coexist:

1. **2014 Heart Rhythm Society (HRS):** either myocardial histology or a clinical pathway requiring histologically proven extracardiac sarcoidosis plus compatible cardiac findings after exclusion of alternatives.
2. **WASOG:** grades probability of organ involvement and emphasizes granulomatous evidence.
3. **Japanese Circulation Society/JMHW revisions:** major/minor criteria, with a pathway for isolated CS and greater reliance on CMR and FDG-PET.

HRS and WASOG show relatively high concordance, whereas agreement with JCS is lower. Thus, a knowledge-base entry should preserve the criterion set and year used rather than treating all “clinical CS” labels as equivalent. (nagai2026thediagnosisand pages 4-6, trivieri2020challengesincardiac pages 9-11)

### Recommended evaluation

- **History/examination:** palpitations, syncope, exertional dyspnea, chest pain, family history, extracardiac symptoms, exposure/infection history.
- **ECG and ambulatory monitoring:** AV block, bundle-branch block, ventricular ectopy, nonsustained/sustained VT, pathological Q waves, or repolarization abnormalities.
- **Echocardiography:** LVEF, regional wall motion, septal thinning/thickening, aneurysm, RV function, and strain. A normal echocardiogram does not exclude CS.
- **CMR:** LGE identifies necrosis/fibrosis, often in nonischemic subepicardial or mid-myocardial patterns; T1/T2 mapping can support active injury. One recent review reports sensitivity 91–99% and specificity 98–100%, whereas screening studies report sensitivity 75–100% and specificity 76–78%, illustrating strong spectrum and reference-standard effects. (nagai2026thediagnosisand pages 4-6, trivieri2020challengesincardiac pages 9-11)
- **FDG-PET plus perfusion imaging:** identifies metabolically active inflammation and helps monitor treatment. Reported sensitivity is 71–91% and specificity 74–89%; a commonly cited pooled benchmark is approximately 89%/78%. High-fat/low-carbohydrate preparation and prolonged fasting are essential to suppress physiological myocardial uptake. (nagai2026thediagnosisand pages 4-6, trivieri2020challengesincardiac pages 9-11)
- **Biopsy:** extracardiac tissue is preferred when available. EMB is highly specific but has only approximately 20–30% sensitivity or ~25% unguided yield because lesions are patchy. Imaging- or voltage-guided biopsy may raise yield toward 50%. A negative EMB does not exclude CS. (nagai2026thediagnosisand pages 4-6, trivieri2020challengesincardiac pages 9-11)

### Biomarkers

Troponin and BNP/NT-proBNP measure myocardial injury and hemodynamic stress; elevated high-sensitivity troponin correlates with active FDG uptake. ACE, soluble IL-2 receptor, CRP/ESR, calcium, liver tests, and blood counts characterize systemic disease or treatment safety but are insufficiently specific for diagnosis. No validated serum biomarker independently establishes CS. miR-126 and miR-223 have been reported higher in CS than controls but remain investigational. (trivieri2020challengesincardiac pages 4-6)

Systemic-sarcoidosis estimates include sIL-2R thresholds of 4,700 U/L for chronicity prediction and 482 U/mL with 84.2% sensitivity/53.6% specificity in a separate context; these assay- and cohort-specific cutoffs should **not** be adopted as CS diagnostic thresholds. (zoppa2024phenotypesandserum pages 9-11)

### Differential diagnosis

Key exclusions are ischemic cardiomyopathy, lymphocytic/viral myocarditis, giant-cell myocarditis, arrhythmogenic cardiomyopathy, LMNA and other genetic cardiomyopathies, hypertrophic or dilated cardiomyopathy, cardiac amyloidosis, Chagas disease where epidemiologically relevant, tuberculosis/fungal granulomatous disease, hypersensitivity myocarditis, and cardiac lymphoma. Coronary-territory scar favors ischemia; diffuse subendocardial LGE favors amyloid; desmosomal variants and characteristic structural patterns favor inherited arrhythmogenic cardiomyopathy. Histology and microbiology are essential when infection or giant-cell myocarditis is possible.

### Screening and genetic testing

Patients with extracardiac sarcoidosis should undergo symptom review and ECG; many centers add echocardiography. Abnormal symptoms, ECG, Holter, or echo warrant CMR and/or FDG-PET. Universal advanced-imaging screening of all asymptomatic patients remains controversial. No newborn, population, carrier, prenatal, or cascade-genetic screening is recommended. WES/WGS, CMA, karyotyping, FISH, mitochondrial testing, and repeat-expansion testing have no routine role unless evaluating an alternative inherited cardiomyopathy.

## 11. Outcome and prognosis

Major adverse outcomes are sustained VT/VF, complete heart block, progressive biventricular failure, device shocks, transplantation, and sudden death. Morbidity includes exercise limitation, fatigue, anxiety over arrhythmias/device therapy, inability to drive or work, and cumulative immunosuppressive toxicity. Heart failure and ventricular arrhythmias account for most CS morbidity and mortality. (trivieri2020challengesincardiac pages 1-3)

Strong adverse markers include reduced LVEF or RV function, extensive CMR LGE, RV involvement, active FDG uptake, perfusion defects, prior VT, syncope, and high-grade AV block. Combined perfusion defect plus abnormal FDG uptake was associated with approximately fourfold higher annual VT/death rates, and RV FDG uptake with approximately fivefold higher event rates. CMR scar burden may outperform PET activity for long-term major-event prediction because fixed fibrosis remains arrhythmogenic after inflammation subsides. (trivieri2020challengesincardiac pages 9-11)

Selected reviews cite sudden-death rates up to 14%, but universal 5- and 10-year survival figures cannot be given reliably because outcomes vary by era, diagnostic criteria, phenotype, and referral setting. Modern imaging, ICD use, immunosuppression, and heart-failure treatment have improved outcomes, yet robust treatment-versus-no-treatment life-expectancy estimates are unavailable. (sivalokanathan2024exploringtherole pages 5-7)

## 12. Treatment

### Immunosuppression

**Glucocorticoids** are first-line for clinically active CS. Prednisone 30–40 mg/day is a commonly proposed initial regimen, followed by gradual taper guided by symptoms, ventricular function, arrhythmias, biomarkers, and PET activity; no universally validated dose or duration exists. Earlier treatment, before advanced ventricular dysfunction and fibrosis, appears more effective. (trivieri2020challengesincardiac pages 12-14)

Steroid-sparing agents include **methotrexate**, azathioprine, mycophenolate mofetil, and leflunomide; cyclophosphamide is reserved for selected refractory severe disease. TNF-α inhibitors—particularly infliximab—are used in refractory disease after infection screening and careful heart-failure assessment. Evidence is predominantly retrospective and should not be interpreted as regulatory approval specifically for CS.

A systematic review of 34 reports encompassing 1,297 patients found no randomized trials and only two good-quality studies. Among 178 treated patients with AV conduction disease, 76 (42.7%) improved, versus 0 of 21 untreated patients. Treatment was associated with prevention of LVEF deterioration, but evidence was inadequate to conclude a ventricular-arrhythmia or mortality benefit. The authors’ exact conclusion was: **“The data quality is too limited to draw conclusions for ventricular arrhythmias and mortality.”** [Fazelpour et al., September 2021; https://doi.org/10.1161/JAHA.121.021183]. Combination immunosuppression reduced relapse from 46% to 17% in one observational comparison, and prednisone plus methotrexate showed persistent five-year benefit over prednisone alone in another. (trivieri2020challengesincardiac pages 12-14)

### Cardiac and interventional management

- Treat HFrEF with guideline-directed therapy as tolerated.
- Pacemaker implantation is indicated for clinically important bradycardia/AV block, but an **ICD is often favored** because future VT/VF risk may persist even if conduction recovers.
- Antiarrhythmics, commonly amiodarone or sotalol, may be used with specialist oversight.
- Catheter ablation treats recurrent scar-mediated VT but recurrence is common when inflammation remains active or the substrate is extensive.
- Cardiac resynchronization is appropriate under standard criteria.
- Mechanical circulatory support and heart transplantation are options for refractory end-stage disease; recurrence in the graft is reported but uncommon.

Suggested NCIT intervention concepts include Prednisone, Methotrexate, Azathioprine, Mycophenolate Mofetil, Infliximab, Anakinra, Rilonacept, Baricitinib, Implantable Cardioverter-Defibrillator, Cardiac Pacemaker, Catheter Ablation, Cardiac Resynchronization Therapy, and Heart Transplantation.

### Experimental and recent trials

- **REPAIR-CS, NCT06660732:** recruiting Phase II randomized trial, 60 participants; rilonacept 320-mg loading dose then 160 mg weekly added to standard treatment. Primary endpoint is change in FDG-positive myocardial segments through 24 weeks; started March 5, 2025, with no posted results. (NCT06660732 chunk 1)
- **NCT06868381:** Phase IIa open-label baricitinib 4 mg/day, planned enrollment 10, not yet recruiting; estimated start April 1, 2026. Primary endpoint is resolution of cardiac FDG uptake; QoL and ACE, hs-troponin I, NT-proBNP, ESR, and CRP are secondary measures. No results posted. (NCT06868381 chunk 1)
- **MAGiC-ART, NCT04017936:** completed 17-participant pilot of anakinra/IL-1 blockade; results were published in May 2023, but the retrieved record did not provide sufficient quantitative efficacy data for reliable extraction. (NCT04017936 chunk 2)
- **NCT07159074:** recruiting Phase II diagnostic study of Tc-99m tilmanocept SPECT/CT, 15 participants, correlating macrophage-directed uptake with FDG-PET and CMR; started September 17, 2025. No results posted. (NCT07159074 chunk 1)
- Other registered research includes **64Cu-DOTATATE macrophage PET/CT** (NCT06131112; recruiting, n=76), **PET/MRI prognosis** (NCT05954507; recruiting, n=180), **SGLT1/2-assisted myocardial glucose suppression** (NCT06510894; recruiting, n=40), diagnostic-criteria validation (NCT04737317; recruiting, n=100), and biomaterial collection (NCT05793398; planned, n=100).

No gene, cell, RNA, or CRISPR therapy is established or in routine clinical development for CS. Pharmacogenomic dosing is not standard; ordinary drug-specific safety monitoring remains essential.

## 13. Prevention

**Primary prevention:** none is proven because the causal antigen is unknown. There is no CS vaccine, prophylactic drug, validated exposure-avoidance program, or genetic reproductive intervention.

**Secondary prevention:** recognize occult cardiac disease in systemic sarcoidosis through symptom review, ECG, and selected ambulatory monitoring/echocardiography, followed by CMR/PET when abnormalities or high clinical suspicion exist. Evaluate unexplained high-grade AV block or VT for CS before labeling it idiopathic.

**Tertiary prevention:** suppress active inflammation; monitor ventricular function, rhythm, and PET activity; use ICD/pacing where indicated; apply guideline-directed heart-failure therapy; manage osteoporosis, diabetes, infection, and other immunosuppression toxicities; and provide vaccination and rehabilitation advice. Genetic counseling may explain familial aggregation and multifactorial risk, but predictive family genetic testing is not available.

## 14. Other species and natural disease

Naturally occurring systemic granulomatous disease and granulomatous myocarditis occur in animals, but a well-validated spontaneous veterinary analogue of human CS—with comparable epidemiology, genetics, and diagnostic criteria—was not identified. Consequently, no reliable NCBI Taxon/VBO breed association, orthologous causal gene, zoonotic transmission pathway, or cross-species carrier state can be assigned. Human sarcoidosis is not considered zoonotic or transmissible.

## 15. Model organisms and experimental systems

No single model reproduces the full human syndrome of patchy cardiac granulomas, relapsing inflammation, fibrosis, conduction block, and VT. Experimental sarcoidosis models include antigen- or *C. acnes*-induced murine granulomas, mycobacterial-protein models, macrophage/T-cell cultures, and human tissue imaging. Most primarily model pulmonary granuloma biology rather than cardiac electrophysiology. Their value lies in studying antigen presentation, macrophage persistence, TNF/IFN signaling, and fibrosis; their limitations are uncertain initiating antigen, strain dependence, noncardiac predominance, and incomplete chronic scar/arrhythmia phenotypes.

Human explanted hearts, EMB material, extracardiac granulomas, and induced-pluripotent-stem-cell cardiomyocytes exposed to inflammatory mediators can address cell injury but do not recreate multicellular granuloma architecture. Emerging spatial transcriptomics and matrix-assisted laser-desorption/ionization imaging can map cell neighborhoods and molecular gradients in human granulomas, but remain discovery tools rather than validated models or diagnostics.

## Evidence appraisal and knowledge-base cautions

1. **Human clinical evidence:** strongest for imaging diagnosis/risk stratification, device-based prevention, and observational improvement in AV conduction/LVEF with immunosuppression.
2. **Mechanistic evidence:** principally extrapolated from systemic sarcoidosis, pathology, and immune profiling; the initiating antigen remains unknown.
3. **Genetic evidence:** association-level and phenotype-modifying, not Mendelian or clinically diagnostic.
4. **Model-organism evidence:** sparse for cardiac-specific disease and weaker than human clinicopathologic evidence.
5. **Direct-quote limitation:** exact short quotations were included only where supported by retrieved text. PMID values were not consistently available in the retrieved records; DOI URLs and publication dates are therefore supplied rather than inventing PMIDs.
6. **Critical implementation rule:** retain the diagnostic framework, imaging-preparation protocol, ancestry, ascertainment method, and evidence type with every knowledge-base assertion. Clinical, autopsy, and imaging prevalence estimates are not interchangeable.

References

1. (sivalokanathan2024exploringtherole pages 5-7): Sanjay Sivalokanathan. Exploring the role of genetics in sarcoidosis and its impact on the development of cardiac sarcoidosis. Cardiogenetics, 14:106-121, Jun 2024. URL: https://doi.org/10.3390/cardiogenetics14020009, doi:10.3390/cardiogenetics14020009. This article has 5 citations.

2. (sivalokanathan2024exploringtherole pages 1-2): Sanjay Sivalokanathan. Exploring the role of genetics in sarcoidosis and its impact on the development of cardiac sarcoidosis. Cardiogenetics, 14:106-121, Jun 2024. URL: https://doi.org/10.3390/cardiogenetics14020009, doi:10.3390/cardiogenetics14020009. This article has 5 citations.

3. (trivieri2020challengesincardiac pages 1-3): Maria Giovanna Trivieri, Paolo Spagnolo, David Birnie, Peter Liu, Wonder Drake, Jason C. Kovacic, Robert Baughman, Zahi A. Fayad, and Marc A. Judson. Challenges in cardiac and pulmonary sarcoidosis: jacc state-of-the-art review. Journal of the American College of Cardiology, 76 16:1878-1901, Oct 2020. URL: https://doi.org/10.1016/j.jacc.2020.08.042, doi:10.1016/j.jacc.2020.08.042. This article has 254 citations and is from a highest quality peer-reviewed journal.

4. (trivieri2020challengesincardiac pages 4-6): Maria Giovanna Trivieri, Paolo Spagnolo, David Birnie, Peter Liu, Wonder Drake, Jason C. Kovacic, Robert Baughman, Zahi A. Fayad, and Marc A. Judson. Challenges in cardiac and pulmonary sarcoidosis: jacc state-of-the-art review. Journal of the American College of Cardiology, 76 16:1878-1901, Oct 2020. URL: https://doi.org/10.1016/j.jacc.2020.08.042, doi:10.1016/j.jacc.2020.08.042. This article has 254 citations and is from a highest quality peer-reviewed journal.

5. (trivieri2020challengesincardiac pages 12-14): Maria Giovanna Trivieri, Paolo Spagnolo, David Birnie, Peter Liu, Wonder Drake, Jason C. Kovacic, Robert Baughman, Zahi A. Fayad, and Marc A. Judson. Challenges in cardiac and pulmonary sarcoidosis: jacc state-of-the-art review. Journal of the American College of Cardiology, 76 16:1878-1901, Oct 2020. URL: https://doi.org/10.1016/j.jacc.2020.08.042, doi:10.1016/j.jacc.2020.08.042. This article has 254 citations and is from a highest quality peer-reviewed journal.

6. (NCT06868381 chunk 1): Matthew C. Baker. A Trial of Baricitinib in Patients With Cardiac Sarcoidosis. Stanford University. 2026. ClinicalTrials.gov Identifier: NCT06868381

7. (NCT07159074 chunk 1):  Repurposing Tilmanocept for Cardiac Sarcoidosis. Duke University. 2025. ClinicalTrials.gov Identifier: NCT07159074

8. (NCT06660732 chunk 1): Andrew N Rosenbaum. Rilonacept in Subjects With Cardiac Sarcoidosis. Mayo Clinic. 2025. ClinicalTrials.gov Identifier: NCT06660732

9. (OpenTargets Search: cardiac sarcoidosis): Open Targets Query (cardiac sarcoidosis, 0 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

10. (sivalokanathan2024exploringtherole pages 4-5): Sanjay Sivalokanathan. Exploring the role of genetics in sarcoidosis and its impact on the development of cardiac sarcoidosis. Cardiogenetics, 14:106-121, Jun 2024. URL: https://doi.org/10.3390/cardiogenetics14020009, doi:10.3390/cardiogenetics14020009. This article has 5 citations.

11. (poyhonen202430yeartrendsin pages 11-11): Pauli Pöyhönen, Jukka Lehtonen, Diana Velikanova, Piia Simonen, Valtteri Uusitalo, Henriikka Mälkönen, Hanna-Kaisa Nordenswan, Tapani Vihinen, Kari Kaikkonen, Petri Haataja, Tuomas Kerola, Tuomas T. Rissanen, Ville Vepsäläinen, Aleksi Alatalo, Päivi Pietilä-Effati, and Markku Kupari. 30-year trends in the incidence, characteristics, and outcome of cardiac sarcoidosis in a nationwide cohort. Aug 2024. URL: https://doi.org/10.1016/j.jacadv.2024.101102, doi:10.1016/j.jacadv.2024.101102. This article has 13 citations.

12. (zoppa2024phenotypesandserum pages 9-11): Matteo Della Zoppa, Francesco Rocco Bertuccio, Ilaria Campo, Fady Tousa, Mariachiara Crescenzi, Sara Lettieri, Francesca Mariani, Angelo Guido Corsico, Davide Piloni, and Giulia Maria Stella. Phenotypes and serum biomarkers in sarcoidosis. Diagnostics, 14:709, Mar 2024. URL: https://doi.org/10.3390/diagnostics14070709, doi:10.3390/diagnostics14070709. This article has 18 citations.

13. (kullberg2024unravelinggeneticmysteries pages 1-5): Susanna Kullberg, Pernilla Darlington, David Ellinghaus, Antje Prasse, Tomoko Iseda, Olga Chuquimia, Anders Eklund, Stefan Schreiber, Joachim Müller-Quernheim, Ingrid Kockum, Åsa Wheelock, Leonid Padyukov, Mehdi S. Mirsaeidi, Paolo Spagnolo, and Natalia V. Rivera. Unraveling genetic mysteries: phenotype-shaping profiles in chronic sarcoidosis. MedRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.29.24319750, doi:10.1101/2024.12.29.24319750. This article has 2 citations.

14. (trivieri2020challengesincardiac pages 20-21): Maria Giovanna Trivieri, Paolo Spagnolo, David Birnie, Peter Liu, Wonder Drake, Jason C. Kovacic, Robert Baughman, Zahi A. Fayad, and Marc A. Judson. Challenges in cardiac and pulmonary sarcoidosis: jacc state-of-the-art review. Journal of the American College of Cardiology, 76 16:1878-1901, Oct 2020. URL: https://doi.org/10.1016/j.jacc.2020.08.042, doi:10.1016/j.jacc.2020.08.042. This article has 254 citations and is from a highest quality peer-reviewed journal.

15. (trivieri2020challengesincardiac pages 9-11): Maria Giovanna Trivieri, Paolo Spagnolo, David Birnie, Peter Liu, Wonder Drake, Jason C. Kovacic, Robert Baughman, Zahi A. Fayad, and Marc A. Judson. Challenges in cardiac and pulmonary sarcoidosis: jacc state-of-the-art review. Journal of the American College of Cardiology, 76 16:1878-1901, Oct 2020. URL: https://doi.org/10.1016/j.jacc.2020.08.042, doi:10.1016/j.jacc.2020.08.042. This article has 254 citations and is from a highest quality peer-reviewed journal.

16. (nagai2026thediagnosisand pages 4-6): Toshiyuki Nagai, Toshifumi Tamura, and Toshihisa Anzai. The diagnosis and management of cardiac sarcoidosis. Internal Medicine, Jan 2026. URL: https://doi.org/10.2169/internalmedicine.7161-26, doi:10.2169/internalmedicine.7161-26. This article has 2 citations and is from a peer-reviewed journal.

17. (NCT04017936 chunk 2):  Interleukin-1 Blockade for Treatment of Cardiac Sarcoidosis. Virginia Commonwealth University. 2020. ClinicalTrials.gov Identifier: NCT04017936

18. (zoppa2024phenotypesandserum pages 1-2): Matteo Della Zoppa, Francesco Rocco Bertuccio, Ilaria Campo, Fady Tousa, Mariachiara Crescenzi, Sara Lettieri, Francesca Mariani, Angelo Guido Corsico, Davide Piloni, and Giulia Maria Stella. Phenotypes and serum biomarkers in sarcoidosis. Diagnostics, 14:709, Mar 2024. URL: https://doi.org/10.3390/diagnostics14070709, doi:10.3390/diagnostics14070709. This article has 18 citations.

## Artifacts

- [Edison artifact artifact-00](Cardiac_Sarcoidosis-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.