---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-14T04:18:51.298651'
end_time: '2026-08-14T04:26:11.042014'
duration_seconds: 439.74
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Multiple Congenital Anomalies-Hypotonia-Seizures Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 22
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Multiple_Congenital_Anomalies-Hypotonia-Seizures_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Multiple Congenital Anomalies-Hypotonia-Seizures Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Multiple Congenital Anomalies-Hypotonia-Seizures Syndrome** covering all of the
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
- **Disease Name:** Multiple Congenital Anomalies-Hypotonia-Seizures Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Multiple Congenital Anomalies-Hypotonia-Seizures Syndrome** covering all of the
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


# Multiple Congenital Anomalies–Hypotonia–Seizures Syndrome (MCAHS)

## Executive summary and scope

Multiple congenital anomalies–hypotonia–seizures syndrome is not a single-gene disorder but a severe subgroup of **inherited glycosylphosphatidylinositol-anchor deficiencies (IGDs)**, themselves classified among congenital disorders of glycosylation. The umbrella term conventionally includes **MCAHS1/PIGN-related disease, MCAHS2/PIGA-related disease, and MCAHS3/PIGT-related disease**. These genes act at different stages of GPI-anchor synthesis or attachment, but their disruption converges on reduced or structurally abnormal GPI-anchored proteins at the cell surface. The result is a congenital, multisystem developmental disorder dominated by hypotonia, developmental impairment, and early epilepsy, often with structural malformations and progressive cerebral or cerebellar abnormalities. The umbrella identifier supported by current disease-target resources is **MONDO:0100247**; **MCAHS1 is MONDO:0013563**. (OpenTargets Search: Multiple congenital anomalies-hypotonia-seizures syndrome, murakami2024gpianchorand pages 1-2)

The evidence base remains small. Most knowledge comes from molecularly defined case reports and case series rather than registries, electronic-health-record cohorts, randomized trials, or population studies. A 2022 systematic review assembled 337 patients with all forms of GPI-biosynthesis defects from 77 publications, but subtype-specific denominators remained only 27 for PIGN, 81 for PIGA, and 38 for PIGT. Consequently, reported frequencies are subject to ascertainment and publication bias and should not be interpreted as population prevalence. (paprocka2022spectrumofneurological pages 3-5)

| Subtype | Umbrella/subtype MONDO where evidenced | Causal gene | Inheritance | Molecular role | Hallmark human phenotype / counts from 337-case systematic review | Representative variants | Diagnostic functional assay |
|---|---|---|---|---|---|---|---|
| MCAHS (umbrella) | MONDO:0100247 umbrella evidenced; subtype MONDOs only partly evidenced in gathered data (OpenTargets Search: Multiple congenital anomalies-hypotonia-seizures syndrome) | PIGN, PIGA, PIGT (OpenTargets Search: Multiple congenital anomalies-hypotonia-seizures syndrome) | Mixed by subtype: AR for PIGN and PIGT; X-linked for PIGA germline disease context; umbrella-level inheritance NR (lam2015expandingtheclinical pages 1-3, paprocka2022spectrumofneurological pages 3-5) | Inherited GPI-anchor biosynthesis defects causing reduced/abnormal GPI-anchored proteins on cell surfaces (murakami2024gpianchorand pages 1-2) | Severe neurodevelopmental disease with seizures, hypotonia, developmental delay/intellectual disability; review states MCAHS caused by PIGA/PIGN/PIGT is among the more severe GPIBD phenotypes (paprocka2022spectrumofneurological pages 3-5) | NR at umbrella level | Flow-cytometric assessment of GPI-anchored proteins / FLAER-based assays in blood cells or fibroblasts are used across GPI deficiencies (johnstone2020investigationofnovel pages 44-49, murakami2024gpianchorand pages 1-2) |
| MCAHS1 | MONDO:0013563 evidenced for “multiple congenital anomalies-hypotonia-seizures syndrome 1” (OpenTargets Search: Multiple congenital anomalies-hypotonia-seizures syndrome) | PIGN (OpenTargets Search: Multiple congenital anomalies-hypotonia-seizures syndrome) | Autosomal recessive (inherited GPI deficiency context; biallelic disease) (OpenTargets Search: Multiple congenital anomalies-hypotonia-seizures syndrome) | PIGN mediates ethanolamine phosphate transfer during GPI-anchor biosynthesis in the ER (murakami2024gpianchorand pages 1-2) | PIGN cases in review: n=27; seizures 23; delayed motor development 7; developmental delay/intellectual disability 23; hypotonia 22 (paprocka2022spectrumofneurological pages 3-5) | Specific PIGN variants NR in gathered evidence | Reduced GPI-anchored protein expression by flow cytometry is the relevant functional assay class for GPIBD; subtype-specific PIGN assay details NR in gathered evidence (murakami2024gpianchorand pages 1-2) |
| MCAHS2 | Umbrella MONDO:0100247 evidenced; subtype-specific MONDO for MCAHS2 NR in gathered evidence (OpenTargets Search: Multiple congenital anomalies-hypotonia-seizures syndrome) | PIGA (OpenTargets Search: Multiple congenital anomalies-hypotonia-seizures syndrome) | X-linked (germline PIGA disease context) (OpenTargets Search: Multiple congenital anomalies-hypotonia-seizures syndrome, paprocka2022spectrumofneurological pages 3-5) | PIGA is part of the GPI-N-acetylglucosaminyltransferase complex catalyzing the first step of GPI-anchor biosynthesis in the ER (murakami2024gpianchorand pages 1-2) | PIGA cases in review: n=81; seizures 76; delayed motor development 61; developmental delay/intellectual disability 70; hypotonia 55; cerebellar atrophy 19 (paprocka2022spectrumofneurological pages 3-5) | Specific PIGA variants NR in gathered evidence | Flow cytometry of GPI-anchored proteins / granulocyte CD16b-type screening is relevant for GPI deficiencies; subtype-specific PIGA functional assay details NR in gathered evidence (murakami2024gpianchorand pages 1-2) |
| MCAHS3 | Umbrella MONDO:0100247 evidenced; subtype-specific MONDO for MCAHS3 NR in gathered evidence (OpenTargets Search: Multiple congenital anomalies-hypotonia-seizures syndrome) | PIGT (OpenTargets Search: Multiple congenital anomalies-hypotonia-seizures syndrome, lam2015expandingtheclinical pages 1-3) | Autosomal recessive; affected siblings with compound heterozygous variants reported (lam2015expandingtheclinical pages 1-3) | PIGT encodes a subunit of the heteropentameric GPI transamidase complex that attaches GPI anchors to proteins (lam2015expandingtheclinical pages 1-3, murakami2024gpianchorand pages 1-2) | PIGT cases in review: n=38; seizures 33; delayed motor development 31; developmental delay/intellectual disability 34; hypotonia 17; cerebellar atrophy 15 (paprocka2022spectrumofneurological pages 3-5) | c.918dupC (frameshift), c.1342C>T (missense) (lam2015expandingtheclinical pages 1-3) | Flow cytometry showing decreased surface expression of GPI-anchored proteins on granulocytes; proposed screening approach because standard CDT/N-glycan CDG screens may miss PIGT-CDG (lam2015expandingtheclinical pages 1-3, lam2015expandingtheclinical pages 13-17) |


*Table: This table summarizes the MCAHS umbrella disorder and its key molecular subtypes using only gathered evidence. It highlights subtype-specific genes, inheritance, molecular function, systematic-review phenotype counts, representative variants where available, and the main functional diagnostic assays.*

## 1. Disease information and identifiers

**Definition.** MCAHS is a genetically heterogeneous developmental encephalopathy caused by deficient GPI-anchor biosynthesis or attachment. GPI anchors tether more than 150 functionally diverse proteins—including enzymes, receptors, adhesion molecules, protease inhibitors, and complement regulators—to the extracellular leaflet of the plasma membrane. Loss of this post-translational system explains the combination of neurologic, craniofacial, skeletal, ocular, cardiac, gastrointestinal, and other congenital abnormalities. (johnstone2020investigationofnovel pages 44-49, murakami2024gpianchorand pages 1-2, ilkovski2015mutationsinpigy pages 9-9)

**Principal names and synonyms:**

- multiple congenital anomalies–hypotonia–seizures syndrome; MCAHS;
- inherited GPI-anchor deficiency associated with MCAHS;
- GPI-anchor biosynthesis defect/congenital disorder of glycosylation;
- **MCAHS1 / PIGN-CDG / PIGN-related GPI deficiency**;
- **MCAHS2 / PIGA-CDG / germline PIGA-related developmental and epileptic encephalopathy**;
- **MCAHS3 / PIGT-CDG / PIGT-related GPI deficiency**.

**Identifiers.** MONDO:0100247 identifies the umbrella disorder and MONDO:0013563 MCAHS1. OpenTargets associates PIGN, PIGA, and PIGT with the umbrella disease and cites foundational PubMed records including PMID **21493957** for PIGN, **22305531** for PIGA, and **23636107/24906948** for PIGT. (OpenTargets Search: Multiple congenital anomalies-hypotonia-seizures syndrome) Subtype-specific OMIM, Orphanet, ICD-10/ICD-11, and MeSH identifiers were not independently verified in the retrieved evidence and should therefore be curated directly from those databases rather than inferred. ICD generally lacks a uniquely granular MCAHS code; practical coding commonly falls under congenital malformation, developmental encephalopathy, epilepsy, or congenital glycosylation-disorder categories.

## 2. Etiology, risk, and protective factors

### Genetic causes

- **PIGN-related MCAHS1:** usually biallelic germline variants; autosomal-recessive inheritance. PIGN adds an ethanolamine-phosphate side branch during ER GPI-anchor assembly.
- **PIGA-related MCAHS2:** pathogenic germline variants in the X-chromosomal PIGA gene. PIGA is a catalytic component of the multisubunit GPI-N-acetylglucosaminyltransferase complex initiating GPI biosynthesis. Hemizygous males usually dominate severe presentations; female disease may reflect skewed X-inactivation or other unusual allelic circumstances. This germline disorder must not be confused with acquired somatic PIGA variants causing paroxysmal nocturnal hemoglobinuria.
- **PIGT-related MCAHS3:** biallelic germline variants; autosomal-recessive inheritance. PIGT is part of the five-subunit GPI transamidase that attaches a completed GPI anchor to a protein’s C terminus. (lam2015expandingtheclinical pages 1-3, murakami2024gpianchorand pages 1-2)

Pathogenic alleles include missense, nonsense, frameshift, splice-altering, and potentially regulatory variants. In one primary PIGT-CDG family, compound heterozygous **c.918dupC (p.Val307Argfs*13)** and **c.1342C>T** alleles reduced granulocyte GPI-anchored-protein expression. (lam2015expandingtheclinical pages 1-3, lam2015expandingtheclinical pages 13-17) Variants reported in affected families are expected to be absent or extremely rare in population databases, but exact gnomAD frequencies and ACMG classifications must be checked transcript-by-transcript in ClinVar/gnomAD; they were not established by the retrieved papers.

### Non-genetic risk and protection

No toxin, infection, diet, behavior, occupation, parental age, or lifestyle exposure is established as a cause of MCAHS. It is a Mendelian developmental disorder. Consanguinity increases the probability that both parents carry the same recessive PIGN or PIGT allele but is not itself a biological cause. No validated protective allele, modifier gene, epigenetic signature, or gene–environment interaction has been demonstrated. Nutrition and antiseizure management may modify complications but do not prevent the underlying molecular defect.

## 3. Phenotypes

The best quantitative summary is the 337-case IGD systematic review. In the relevant molecular groups:

- **PIGA (n=81):** seizures 76/81 (93.8%), developmental delay/intellectual disability 70/81 (86.4%), delayed motor development 61/81 (75.3%), hypotonia 55/81 (67.9%), and cerebellar atrophy 19/81 (23.5%).
- **PIGN (n=27):** seizures 23/27 (85.2%), developmental delay/intellectual disability 23/27 (85.2%), hypotonia 22/27 (81.5%), and documented delayed motor development 7/27 (25.9%). The low motor-delay count likely reflects missing reporting rather than preserved development.
- **PIGT (n=38):** seizures 33/38 (86.8%), developmental delay/intellectual disability 34/38 (89.5%), delayed motor development 31/38 (81.6%), hypotonia 17/38 (44.7%), and cerebellar atrophy 15/38 (39.5%). (paprocka2022spectrumofneurological pages 3-5)

### Core clinical features and suggested HPO terms

- **Congenital or infantile hypotonia** — generally persistent and severe; HP:0001252.
- **Early-onset epilepsy/developmental and epileptic encephalopathy** — focal, generalized, tonic, clonic, tonic-clonic, myoclonic seizures, spasms, or mixed patterns; often treatment resistant; HP:0001250, HP:0007359, HP:0002123.
- **Global developmental delay and intellectual disability** — usually severe-to-profound, lifelong; HP:0001263, HP:0001249.
- **Delayed motor development/non-ambulation** — HP:0001270; feeding and communication dependence are common functional consequences.
- **Microcephaly, cerebral/cerebellar atrophy, delayed myelination, thin/hypoplastic corpus callosum, and widened CSF spaces** — HP:0000252, HP:0002059, HP:0001272, HP:0007370, HP:0002079. GPI-deficiency neuroimaging can show white-matter abnormalities, cerebral or cerebellar atrophy, and callosal hypoplasia. (mario2023epilepsyphenotypesof pages 4-6, murakami2024gpianchorand pages 1-2)
- **Congenital anomalies/dysmorphism** — variable facial, distal-limb/nail, skeletal, cardiac, gastrointestinal, genitourinary, ocular, and auditory abnormalities. Suggested terms should be assigned at the patient level rather than treating every anomaly as universal.
- **Laboratory abnormality:** serum alkaline phosphatase can be increased in some IGDs because improperly anchored ALP is released, but values can be normal or low depending on the biosynthetic step and assay. Hyperphosphatasia is therefore supportive, not required.

Seizure onset is generally neonatal or infantile, although the broader B6-responsive GPI-deficiency literature reports onset commonly after the immediate neonatal period. Across all molecularly confirmed vitamin-B6-dependent epilepsies—not MCAHS alone—67.8% began in the first month; this statistic must not be assigned directly to MCAHS. (mario2023epilepsyphenotypesof pages 4-6)

No validated MCAHS-specific EQ-5D, SF-36, PROMIS, behavioral, or caregiver-burden study was identified. Nevertheless, profound motor, cognitive, feeding, communication, and seizure burdens imply major lifelong effects on patients and caregivers.

## 4. Genetic and molecular information

The three proteins occupy distinct pathway positions:

1. **PIGA—upstream initiation:** transfers GlcNAc to phosphatidylinositol as part of the ER GPI-N-acetylglucosaminyltransferase complex.
2. **PIGN—intermediate anchor assembly:** contributes ethanolamine phosphate modification after mannose incorporation.
3. **PIGT—downstream protein attachment:** acts within the PIGK–PIGT–PIGS–PIGU–GPAA1 transamidase complex to transfer completed GPI to precursor proteins. (murakami2024gpianchorand pages 1-2)

The usual disease mechanism is **partial loss of function**. Complete loss of essential GPI-biosynthesis activity is presumed incompatible with normal embryonic development; surviving patients generally retain residual function. Functional support includes decreased GPI-anchored proteins on patient granulocytes or fibroblasts and restoration after wild-type-gene complementation, an approach well established across IGDs. Relevant markers include CD16/CD16b, CD24, CD55, CD59, and FLAER. (johnstone2020investigationofnovel pages 44-49, nguyen2018mutationsinpigs pages 4-6, lam2015expandingtheclinical pages 1-3)

No reproducible MCAHS modifier gene, disease-specific methylation episignature, somatic driver mechanism, recurrent pathogenic chromosomal rearrangement, repeat expansion, or mitochondrial-genome cause is established. Large deletions encompassing a causal gene remain theoretically detectable by copy-number analysis but are not the canonical mechanism.

## 5. Environmental and infectious information

Environmental toxins, radiation, pollution, smoking, alcohol, exercise, diet, and infectious agents have no established etiologic role. MCAHS is not contagious, infectious, immune-mediated, or zoonotic. Intercurrent illness, fever, fasting, or medication nonadherence may exacerbate seizures in an affected child, but this is clinical triggering rather than disease causation.

## 6. Mechanism and pathophysiology

### Causal chain

**Germline pathogenic variant → deficient GPI biosynthesis/attachment in the ER → reduced or structurally abnormal GPI-anchored proteins at the plasma membrane → disruption of neuronal signaling, adhesion, neurogenesis, folate/B6 handling, complement regulation, and embryonic tissue patterning → congenital malformations, hypotonia, developmental impairment, epilepsy, and progressive brain abnormalities.** Approximately 30 gene products participate in human GPI synthesis and remodeling. (johnstone2020investigationofnovel pages 44-49, murakami2024gpianchorand pages 1-2)

A clinically important downstream mechanism involves **tissue-nonspecific alkaline phosphatase (TNSALP/ALPL)**, itself a GPI-anchored ectoenzyme. Reduced membrane ALP can impair extracellular dephosphorylation of pyridoxal-5′-phosphate, limiting transport of vitamin B6 species into neurons and reducing PLP-dependent neurotransmitter synthesis, including inhibitory GABA production. This provides a mechanistic rationale for B6-responsive seizures in a subset of IGD patients. Impaired localization of the GPI-anchored folate receptor FOLR1 may likewise disturb cerebral folate delivery. (murakami2024gpianchorand pages 1-2)

Suggested ontology annotations include **GO:0006506 GPI-anchor biosynthetic process**, **GO:0016255 attachment of GPI anchor to protein**, **GO:0005783 endoplasmic reticulum**, **GO:0005886 plasma membrane**, and broader terms for protein post-translational modification, neurogenesis, synaptic signaling, and embryonic morphogenesis. Candidate affected cell types include neurons (CL:0000540), neural progenitor cells, oligodendrocytes, skeletal myocytes, cardiomyocytes, and diverse embryonic epithelial/mesenchymal populations; direct cell-type-resolved human evidence is limited.

No disease-specific single-cell atlas, spatial transcriptomic study, proteome, metabolome, lipidome, or integrated multi-omics signature was identified. The strongest molecular profiling remains cell-surface GPI-AP phenotyping and gene-complementation assays.

## 7. Anatomical structures affected

The **central nervous system** is primary: cerebral cortex, white matter, corpus callosum, cerebellum, and brainstem may be involved. Suggested UBERON annotations include brain (UBERON:0000955), cerebral cortex, cerebellum (UBERON:0002037), corpus callosum, and white matter. Secondary or congenital involvement may affect eye, ear, craniofacial structures, skeleton and distal limbs, heart, diaphragm, gastrointestinal tract, kidney/urinary tract, and genital structures. PIGT-CDG case descriptions included ophthalmologic, hearing, skeletal, endocrine, and cardiac abnormalities. (lam2015expandingtheclinical pages 1-3)

At the subcellular level, the critical sites are the **endoplasmic-reticulum membrane**, where GPI is assembled and transferred, and the **plasma membrane**, where GPI-anchored proteins normally function. Lateralization is not characteristic; brain and systemic involvement is generally bilateral or diffuse.

## 8. Temporal development and natural history

Molecular pathology begins prenatally. Structural anomalies and fetal akinesia can occur at the severe end, whereas hypotonia, feeding problems, dysmorphism, and seizures usually become apparent at birth or in infancy. Developmental delay is chronic and typically severe. Epilepsy may remain refractory or fluctuate with treatment. Cerebral and particularly cerebellar atrophy may emerge or progress on serial MRI, showing that the phenotype is not exclusively a static malformation syndrome. (paprocka2022spectrumofneurological pages 3-5, mario2023epilepsyphenotypesof pages 4-6)

There is no validated staging system, predictable remission pattern, or quantified median progression rate. The prenatal and first-year developmental windows are critical for diagnosis, seizure control, nutrition, hearing/vision assessment, and early therapy. Lifelong surveillance is required.

## 9. Inheritance and population

PIGN- and PIGT-related disease are autosomal recessive: each pregnancy of two confirmed heterozygous parents has a 25% probability of an affected child, 50% probability of a carrier child, and 25% probability of a child inheriting neither familial allele. PIGA-related MCAHS is X-linked; recurrence depends on maternal carrier status, X-inactivation, and whether the variant is inherited or de novo.

Penetrance for clearly damaging biallelic/hemizygous variants appears high, but expressivity is broad and residual activity likely influences severity. No anticipation is expected. Parental germline mosaicism is possible, particularly after an apparently de novo event, but its frequency is unknown. No robust carrier frequency, founder effect, prevalence, incidence, sex ratio, ethnic enrichment, or geographic distribution has been established. The disorder is ultra-rare and reported internationally. Apparent male enrichment in PIGA disease follows X-linked biology; PIGN and PIGT should affect both sexes comparably.

## 10. Diagnostics

### Recommended approach

1. **Clinical recognition:** congenital anomalies plus hypotonia, severe developmental delay, and infantile epilepsy; obtain three-generation pedigree and detailed dysmorphology examination.
2. **Routine assessment:** EEG; brain MRI; serum alkaline phosphatase with age-specific reference range; CBC, metabolic profile, liver tests, calcium/phosphate, vitamin D, and nutrition assessment. Add echocardiography, renal ultrasound, hearing, ophthalmologic, orthopedic, and feeding/swallowing evaluations according to phenotype.
3. **Genomic testing:** trio exome or genome sequencing is preferred because IGDs are genetically heterogeneous. An epilepsy/congenital-anomaly/CDG panel should include PIGN, PIGA, PIGT and other PIG/PGAP genes. WGS is useful when WES is negative because it better captures noncoding, structural, and poorly covered variants. A separate mitochondrial or repeat-expansion test is not routinely indicated unless the phenotype suggests another diagnosis.
4. **Variant confirmation:** Sanger confirmation and segregation; deletion/duplication analysis if read-depth suggests copy-number change.
5. **Functional confirmation:** flow cytometry of granulocytes or fibroblasts for GPI-APs—especially CD16b, CD55, CD59 and/or FLAER—with specialist-laboratory complementation when needed. Standard carbohydrate-deficient transferrin or N-glycan screening may be normal and cannot exclude PIGT-CDG or other anchor defects. (lam2015expandingtheclinical pages 1-3, lam2015expandingtheclinical pages 13-17, murakami2024gpianchorand pages 1-2)

There are no universally accepted clinical diagnostic criteria; molecular confirmation is central. Differential diagnoses include other inherited GPI deficiencies, non-GPI congenital disorders of glycosylation, pyridoxine-dependent epilepsy (ALDH7A1), PNPO or PLPBP deficiency, hypophosphatasia, mitochondrial disease, chromosomal syndromes, and other developmental and epileptic encephalopathies.

Population newborn screening is unavailable. Cascade testing of relatives and targeted prenatal or preimplantation testing are feasible after familial variants are known.

## 11. Outcomes and prognosis

Severity ranges from fetal/neonatal lethality to survival into childhood or adulthood with profound disability. Poor prognostic indicators plausibly include major congenital malformations, fetal akinesia, early refractory seizures, severe feeding/respiratory dysfunction, and progressive brain atrophy, but no validated prognostic model exists. Long-term morbidity includes severe intellectual and motor disability, communication impairment, aspiration and undernutrition, orthopedic complications, sensory impairment, and medication-related adverse effects.

No reliable 5- or 10-year survival, life-expectancy, disease-specific mortality, recovery rate, or standardized quality-of-life statistic is available. Early death has been documented in severe IGDs, but extrapolation across genes is unsafe. (ilkovski2015mutationsinpigy pages 1-2)

## 12. Treatment and current implementation

There is no approved therapy that repairs PIGN, PIGA, or PIGT function. Management is multidisciplinary and phenotype directed:

- **Epilepsy:** individualized antiseizure medication based on seizure type and EEG; rescue plan for prolonged seizures; ketogenic diet may be considered for drug-resistant epilepsy under specialist supervision, although MCAHS evidence is limited to reports rather than controlled trials.
- **Vitamin B6 trial:** because some GPI-anchor defects reduce neuronal PLP availability, a monitored pyridoxine or pyridoxal-5′-phosphate trial is biologically justified in refractory early epilepsy. The broader B6-dependent epilepsy literature describes acute **100 mg IV pyridoxine** and maintenance **100–400 mg/day or approximately 20–30 mg/kg/day**, but these are class-level data, not an MCAHS-specific dosing guideline. IV administration can cause apnea and must occur with cardiorespiratory monitoring; chronic high doses require neuropathy surveillance. (mario2023epilepsyphenotypesof pages 4-6)
- **Folinic acid:** may be considered when cerebral folate disturbance is demonstrated or strongly suspected, but MCAHS-specific response rates are unavailable.
- **Support:** gastrostomy or feeding therapy when necessary; aspiration precautions; physical, occupational, speech/augmentative-communication and respiratory therapy; orthopedic management; hearing and vision aids; cardiac, renal, endocrine, and skeletal surveillance.
- **Surgery:** anomaly-specific procedures or gastrostomy; epilepsy surgery is rarely appropriate for diffuse genetic encephalopathy unless a clearly resectable focus exists.

Suggested NCIt intervention concepts include anticonvulsant therapy, ketogenic diet, pyridoxine, pyridoxal phosphate, folinic acid, physical therapy, occupational therapy, speech therapy, nutritional support, gastrostomy, genetic counseling, prenatal diagnosis, and preimplantation genetic testing. Suggested chemical annotations include pyridoxine (CHEBI:16709), pyridoxal 5′-phosphate, and folinic acid; database identifiers should be validated during curation.

No relevant disease-specific interventional ClinicalTrials.gov study, gene therapy, CRISPR therapy, ASO, siRNA, cell therapy, immunotherapy, or approved targeted molecule was identified. Therefore, treatment-response percentages and comparative adverse-event rates cannot presently be supplied.

## 13. Prevention

Primary lifestyle or environmental prevention is not possible. The meaningful preventive measures are reproductive: carrier testing, cascade testing, genetic counseling, targeted prenatal diagnosis by chorionic-villus sampling/amniocentesis, and preimplantation genetic testing for a known familial variant. Secondary prevention consists of rapid genomic diagnosis, EEG surveillance, specialist-supervised B6 testing when appropriate, and early nutrition/hearing/vision/cardiac assessment. Tertiary prevention addresses status epilepticus, aspiration, contractures, malnutrition, scoliosis, respiratory infection, and caregiver burden. Vaccination follows routine schedules unless an individual contraindication exists; no MCAHS-specific vaccine or prophylactic drug applies.

## 14. Other species and natural disease

PIGN, PIGA, and PIGT and the broader GPI pathway are evolutionarily conserved in vertebrates. However, no well-established naturally occurring veterinary syndrome demonstrably equivalent to human MCAHS was identified in the retrieved literature. There is no zoonotic potential or cross-species transmission because this is a germline genetic disorder. NCBI Taxon and ortholog Gene IDs should be retrieved directly for each intended species rather than inferred.

## 15. Model organisms and experimental systems

The most directly informative models are **patient-derived fibroblasts or blood granulocytes**, gene-deficient cultured cells, and complementation assays. Flow cytometry quantifies CD16, CD24, CD55, CD59, or FLAER binding; rescue by wild-type cDNA supports variant causality. Related IGD experiments show that mutant constructs may only partially restore cell-surface GPI-APs, linking residual biochemical activity to phenotypic severity. (johnstone2020investigationofnovel pages 44-49, nguyen2018mutationsinpigs pages 4-6, ilkovski2015mutationsinpigy pages 9-9)

Whole-animal GPI-pathway knockouts often face embryonic lethality or phenotypes more severe than surviving human hypomorphic disease, limiting direct translation. No sufficiently characterized MCAHS1/2/3-specific mouse, rat, zebrafish, Drosophila, organoid, or iPSC model with quantitative human-phenotype recapitulation was available in the retrieved corpus. Priorities include conditional neural Pign/Piga/Pigt models, patient iPSC-derived neurons and cerebral organoids, and rescue studies measuring GPI-AP localization, PLP-dependent neurotransmission, network excitability, myelination, and cerebellar development.

## Recent developments and evidence assessment

The most important recent advances are conceptual rather than therapeutic. A 2023 genotype–phenotype study broadened PIGN-related disease from lethal Fryns-like presentations through classic MCAHS to milder neurologic phenotypes, reinforcing a residual-function continuum. A 2024 expert review formalized the positions of PIGA, PIGN, and PIGT within the approximately 30-component GPI pathway and highlighted CD16b flow cytometry and ALP/B6 biology. Recent 2023–2024 vitamin-metabolism research also treats GPI-anchor deficiency as a potentially B6-responsive epilepsy subgroup, while emphasizing that biomarker-guided, monitored trials are preferable to assuming universal responsiveness. (mario2023epilepsyphenotypesof pages 4-6, murakami2024gpianchorand pages 1-2)

The systematic review’s central conclusion is that GPI defects should be considered in children with early seizures and developmental delay; its abstract reports that **337 cases from 77 articles** met inclusion criteria. (paprocka2022spectrumofneurological pages 3-5) A primary PIGT study further demonstrates why biochemical screening alone is insufficient: decreased granulocyte GPI-AP expression was detectable by flow cytometry even though conventional CDG screening may miss the disorder. (lam2015expandingtheclinical pages 1-3, lam2015expandingtheclinical pages 13-17)

## Key evidence gaps

Reliable epidemiology, prospective natural history, standardized seizure and developmental outcomes, patient-reported quality of life, variant-level penetrance, population allele frequencies, pharmacogenomics, validated prognostic biomarkers, subtype-specific treatment response, and disease-specific interventional trials are absent. Likewise, there are no established immune, epigenetic, transcriptomic, single-cell, spatial, proteomic, metabolomic, or lipidomic signatures. These omissions should be encoded as **unknown/not available**, not as negative findings.

## Selected source details

- Paprocka J, et al. *Spectrum of Neurological Symptoms in Glycosylphosphatidylinositol Biosynthesis Defects: Systematic Review.* **Frontiers in Neurology**, published January 2022. DOI/URL: https://doi.org/10.3389/fneur.2021.758899. (paprocka2022spectrumofneurological pages 3-5)
- Lam C, et al. *Expanding the clinical and molecular characteristics of PIGT-CDG, a disorder of glycosylphosphatidylinositol anchors.* **Molecular Genetics and Metabolism**, June 2015. DOI/URL: https://doi.org/10.1016/j.ymgme.2015.04.007. (lam2015expandingtheclinical pages 1-3)
- Murakami Y, Kinoshita T. *GPI Anchor and Its Deficiency.* **Trends in Glycoscience and Glycotechnology**, January 2024. DOI/URL: https://doi.org/10.4052/tigg.2331.1e. (murakami2024gpianchorand pages 1-2)
- Mastrangelo M, et al. *Epilepsy Phenotypes of Vitamin B6-Dependent Diseases: An Updated Systematic Review.* **Children**, March 2023. DOI/URL: https://doi.org/10.3390/children10030553. (mario2023epilepsyphenotypesof pages 4-6)
- Nguyen TTM, et al. *Mutations in PIGS, Encoding a GPI Transamidase, Cause a Neurological Syndrome Ranging from Fetal Akinesia to Epileptic Encephalopathy.* **American Journal of Human Genetics**, October 2018. DOI/URL: https://doi.org/10.1016/j.ajhg.2018.08.014. This is supporting pathway/comparator evidence rather than MCAHS-subtype evidence. (nguyen2018mutationsinpigs pages 4-6)
- Ilkovski B, et al. *Mutations in PIGY: expanding the phenotype of inherited glycosylphosphatidylinositol deficiencies.* **Human Molecular Genetics**, August 2015. DOI/URL: https://doi.org/10.1093/hmg/ddv331. This is supporting residual-function and cellular-assay evidence rather than a canonical MCAHS subtype. (ilkovski2015mutationsinpigy pages 1-2, ilkovski2015mutationsinpigy pages 9-9)

References

1. (OpenTargets Search: Multiple congenital anomalies-hypotonia-seizures syndrome): Open Targets Query (Multiple congenital anomalies-hypotonia-seizures syndrome, 4 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (murakami2024gpianchorand pages 1-2): Yoshiko Murakami and Taroh Kinoshita. Gpi anchor and its deficiency. Trends in Glycoscience and Glycotechnology, 36:E1-E5, Jan 2024. URL: https://doi.org/10.4052/tigg.2331.1e, doi:10.4052/tigg.2331.1e. This article has 1 citations and is from a peer-reviewed journal.

3. (paprocka2022spectrumofneurological pages 3-5): Justyna Paprocka, Michał Hutny, Jagoda Hofman, Agnieszka Tokarska, Magdalena Kłaniewska, Krzysztof Szczałuba, Agnieszka Stembalska, Aleksandra Jezela-Stanek, and Robert Śmigiel. Spectrum of neurological symptoms in glycosylphosphatidylinositol biosynthesis defects: systematic review. Frontiers in Neurology, Jan 2022. URL: https://doi.org/10.3389/fneur.2021.758899, doi:10.3389/fneur.2021.758899. This article has 18 citations and is from a peer-reviewed journal.

4. (lam2015expandingtheclinical pages 1-3): Christina Lam, Gretchen A. Golas, Mariska Davids, Marjan Huizing, Megan S. Kane, Donna M. Krasnewich, May Christine V. Malicdan, David R. Adams, Thomas C. Markello, Wadih M. Zein, Andrea L. Gropman, Maya B. Lodish, Constantine A. Stratakis, Irina Maric, Sergio D. Rosenzweig, Eva H. Baker, Carlos R. Ferreira, Noelle R. Danylchuk, Stephen Kahler, Adolfo D. Garnica, G. Bradley Schaefer, Cornelius F. Boerkoel, William A. Gahl, and Lynne A. Wolfe. Expanding the clinical and molecular characteristics of pigt-cdg, a disorder of glycosylphosphatidylinositol anchors. Molecular genetics and metabolism, 115 2-3:128-140, Jun 2015. URL: https://doi.org/10.1016/j.ymgme.2015.04.007, doi:10.1016/j.ymgme.2015.04.007. This article has 60 citations and is from a peer-reviewed journal.

5. (johnstone2020investigationofnovel pages 44-49): Devon Johnstone. Investigation of novel genetic causes of early infantile epileptic encephalopathies using next generation sequencing and zebrafish and cellular modelling. ArXiv, Aug 2020. URL: https://doi.org/10.20381/ruor-25104, doi:10.20381/ruor-25104. This article has 1 citations.

6. (lam2015expandingtheclinical pages 13-17): Christina Lam, Gretchen A. Golas, Mariska Davids, Marjan Huizing, Megan S. Kane, Donna M. Krasnewich, May Christine V. Malicdan, David R. Adams, Thomas C. Markello, Wadih M. Zein, Andrea L. Gropman, Maya B. Lodish, Constantine A. Stratakis, Irina Maric, Sergio D. Rosenzweig, Eva H. Baker, Carlos R. Ferreira, Noelle R. Danylchuk, Stephen Kahler, Adolfo D. Garnica, G. Bradley Schaefer, Cornelius F. Boerkoel, William A. Gahl, and Lynne A. Wolfe. Expanding the clinical and molecular characteristics of pigt-cdg, a disorder of glycosylphosphatidylinositol anchors. Molecular genetics and metabolism, 115 2-3:128-140, Jun 2015. URL: https://doi.org/10.1016/j.ymgme.2015.04.007, doi:10.1016/j.ymgme.2015.04.007. This article has 60 citations and is from a peer-reviewed journal.

7. (ilkovski2015mutationsinpigy pages 9-9): Biljana Ilkovski, Alistair T. Pagnamenta, Gina L. O'Grady, Taroh Kinoshita, Malcolm F. Howard, Monkol Lek, Brett Thomas, Anne Turner, John Christodoulou, David Sillence, Samantha J.L. Knight, Niko Popitsch, David A. Keays, Consuelo Anzilotti, Anne Goriely, Leigh B. Waddell, Fabienne Brilot, Kathryn N. North, Noriyuki Kanzawa, Daniel G. Macarthur, Jenny C. Taylor, Usha Kini, Yoshiko Murakami, and Nigel F. Clarke. Mutations in pigy: expanding the phenotype of inherited glycosylphosphatidylinositol deficiencies. Human Molecular Genetics, 24:6146-6159, Aug 2015. URL: https://doi.org/10.1093/hmg/ddv331, doi:10.1093/hmg/ddv331. This article has 93 citations and is from a domain leading peer-reviewed journal.

8. (mario2023epilepsyphenotypesof pages 4-6): Mario Mastrangelo, Valentina Gasparri, Katerina Bernardi, Silvia Foglietta, Georgia Ramantani, and Francesco Pisani. Epilepsy phenotypes of vitamin b6-dependent diseases: an updated systematic review. Children, Mar 2023. URL: https://doi.org/10.3390/children10030553, doi:10.3390/children10030553. This article has 33 citations.

9. (nguyen2018mutationsinpigs pages 4-6): Thi Tuyet Mai Nguyen, Yoshiko Murakami, Kristen M. Wigby, Nissan V. Baratang, Justine Rousseau, Anik St-Denis, Jill A. Rosenfeld, Stephanie C. Laniewski, Julie Jones, Alejandro D. Iglesias, Marilyn C. Jones, Diane Masser-Frye, Angela E. Scheuerle, Denise L. Perry, Ryan J. Taft, Françoise Le Deist, Miles Thompson, Taroh Kinoshita, and Philippe M. Campeau. Mutations in pigs, encoding a gpi transamidase, cause a neurological syndrome ranging from fetal akinesia to epileptic encephalopathy. American journal of human genetics, 103 4:602-611, Oct 2018. URL: https://doi.org/10.1016/j.ajhg.2018.08.014, doi:10.1016/j.ajhg.2018.08.014. This article has 67 citations and is from a highest quality peer-reviewed journal.

10. (ilkovski2015mutationsinpigy pages 1-2): Biljana Ilkovski, Alistair T. Pagnamenta, Gina L. O'Grady, Taroh Kinoshita, Malcolm F. Howard, Monkol Lek, Brett Thomas, Anne Turner, John Christodoulou, David Sillence, Samantha J.L. Knight, Niko Popitsch, David A. Keays, Consuelo Anzilotti, Anne Goriely, Leigh B. Waddell, Fabienne Brilot, Kathryn N. North, Noriyuki Kanzawa, Daniel G. Macarthur, Jenny C. Taylor, Usha Kini, Yoshiko Murakami, and Nigel F. Clarke. Mutations in pigy: expanding the phenotype of inherited glycosylphosphatidylinositol deficiencies. Human Molecular Genetics, 24:6146-6159, Aug 2015. URL: https://doi.org/10.1093/hmg/ddv331, doi:10.1093/hmg/ddv331. This article has 93 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Multiple_Congenital_Anomalies-Hypotonia-Seizures_Syndrome-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |

All extracted references resolved successfully.