---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-20T07:13:41.880908'
end_time: '2026-08-20T07:25:45.791095'
duration_seconds: 723.91
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Idiopathic Interstitial Pneumonia
  mondo_id: ''
  category: Respiratory Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 48
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 9
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Idiopathic_Interstitial_Pneumonia-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Idiopathic Interstitial Pneumonia
- **MONDO ID:**  (if available)
- **Category:** Respiratory Disease

## Research Objectives

Please provide a comprehensive research report on **Idiopathic Interstitial Pneumonia** covering all of the
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
- **Disease Name:** Idiopathic Interstitial Pneumonia
- **MONDO ID:**  (if available)
- **Category:** Respiratory Disease

## Research Objectives

Please provide a comprehensive research report on **Idiopathic Interstitial Pneumonia** covering all of the
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


# Idiopathic Interstitial Pneumonia: Disease-Characteristics Research Report

**Scope note.** *Idiopathic interstitial pneumonia* (IIP) is a **family of diffuse parenchymal lung diseases**, not a synonym for idiopathic pulmonary fibrosis (IPF). IPF is the best-studied, usually most severe chronic fibrotic IIP; consequently, most quantitative genetics, epidemiology, prognosis, and treatment evidence below is IPF-specific and is labeled accordingly.

## Executive summary

IIPs are defined by combinations of clinical presentation, high-resolution CT (HRCT), and histopathologic patterns after exclusion of connective-tissue disease, inhalational/occupational disease, drug toxicity, infection, and other known causes. Major entities include IPF, idiopathic nonspecific interstitial pneumonia (iNSIP), cryptogenic organizing pneumonia (COP), acute interstitial pneumonia (AIP), respiratory bronchiolitis–ILD (RB-ILD), desquamative interstitial pneumonia (DIP), lymphoid interstitial pneumonia (LIP), and pleuroparenchymal fibroelastosis (PPFE). Multidisciplinary discussion among pulmonology, radiology, pathology, and—when appropriate—rheumatology is the diagnostic standard. (kreuter2021thediagnosisand pages 1-2, senhaji2026idiopathicpulmonaryfibrosis pages 9-10, kreuter2021thediagnosisand pages 2-4)

The current IPF model is repeated alveolar epithelial injury in an aging, genetically susceptible lung, followed by abnormal repair, fibroblast/myofibroblast activation, extracellular-matrix (ECM) deposition, tissue stiffening, and self-sustaining fibrosis. Genetics includes the common **MUC5B rs35705950** susceptibility allele and rare pathogenic variants in telomere- and surfactant-related genes. Antifibrotics slow IPF progression but do not reverse established fibrosis; pulmonary rehabilitation, oxygen when hypoxemic, symptom-directed care, and timely transplant referral remain essential. (zhumagaliyeva2025geneticdeterminantsof pages 2-4, zuo2025idiopathicpulmonaryfibrosis pages 1-2, senhaji2026idiopathicpulmonaryfibrosis pages 2-4, viswanathan2024patientprofilebasedmanagement pages 17-18)

The following table provides an ontology-oriented synopsis.

| Domain | Knowledge-base summary | Suggested ontology terms |
|---|---|---|
| Scope / classification | **Idiopathic interstitial pneumonia (IIP)** is a **family of idiopathic diffuse parenchymal lung diseases**, not a single entity. **Idiopathic pulmonary fibrosis (IPF)** is one **major fibrotic subtype** within IIP. Major adult IIP subtypes commonly referenced in modern practice include IPF, idiopathic nonspecific interstitial pneumonia (iNSIP), cryptogenic organizing pneumonia (COP), acute interstitial pneumonia (AIP), respiratory bronchiolitis–ILD (RB-ILD), desquamative interstitial pneumonia (DIP), lymphoid interstitial pneumonia (LIP), and pleuroparenchymal fibroelastosis (PPFE); multidisciplinary clinico-radiologic-pathologic diagnosis is central. (kreuter2021thediagnosisand pages 1-2, kreuter2021thediagnosisand pages 2-4) | MONDO: **idiopathic interstitial pneumonia** (MONDO_0002429); EFO: **idiopathic pulmonary fibrosis** (EFO_0000768); disease labels: idiopathic NSIP, COP, AIP, RB-ILD, DIP, LIP, PPFE; imaging/pathology labels: UIP, NSIP, OP |
| Core phenotypes | Typical fibrotic IIP/IPF phenotype is **adult-onset progressive exertional dyspnea and chronic dry cough**, often with **bibasilar crackles** and **digital clubbing**; physiology usually shows a **restrictive ventilatory defect** with reduced **FVC** and **DLCO**. Clubbing is reported in roughly **25–50%** of IPF cases; cough burden can be substantial and QoL-limiting. (senhaji2026idiopathicpulmonaryfibrosis pages 1-2, senhaji2026idiopathicpulmonaryfibrosis pages 7-9, senhaji2026idiopathicpulmonaryfibrosis pages 16-18) | HPO: **Dyspnea**, **Cough**, **Clubbing**, **Abnormal respiratory crackles**, **Restrictive ventilatory defect**, **Decreased diffusing capacity of lung for carbon monoxide** |
| Anatomy / cells | Primary site is the **lung parenchyma**, especially **distal lung/alveolar regions** with subpleural-basal predominance in UIP/IPF. Key involved cell types include **alveolar type 2 epithelial cells (AT2)**, aberrant basaloid/bronchiolized epithelial cells, **fibroblasts/myofibroblasts**, **macrophages** (including SPP1-high), endothelial cells, and other stromal/immune populations. (zuo2025idiopathicpulmonaryfibrosis pages 1-2, zuo2025idiopathicpulmonaryfibrosis pages 2-2, senhaji2026idiopathicpulmonaryfibrosis pages 7-9) | UBERON: **lung**, **alveolus**, **lung interstitium**, **bronchiole**, **pleura**; CL: **alveolar type 2 epithelial cell**, **fibroblast**, **myofibroblast**, **macrophage**, **endothelial cell** |
| Genetic architecture | Genetic contribution spans **rare pathogenic variants** and **common susceptibility alleles**. Strongest common risk allele is **MUC5B promoter rs35705950**; rare high-effect variants occur in **telomere genes** (**TERT, TERC, RTEL1, PARN**) and **surfactant-related genes** (**SFTPA1, SFTPA2, SFTPC, ABCA3**). Familial pulmonary fibrosis often shows **autosomal dominant inheritance with incomplete, age-dependent penetrance** for rare telomere-pathway variants; common alleles also involve **DSP, FAM13A, TOLLIP, DPP9** and related loci. (zhumagaliyeva2025geneticdeterminantsof pages 2-4, zhumagaliyeva2025geneticdeterminantsof pages 1-2, zhumagaliyeva2025geneticdeterminantsof pages 7-8, cerri2024geneticriskfactors pages 2-4, OpenTargets Search: idiopathic pulmonary fibrosis) | Genes: **MUC5B, TERT, TERC, RTEL1, PARN, SFTPA1, SFTPA2, SFTPC, ABCA3, DSP, FAM13A, TOLLIP, DPP9**; variation labels: **pathogenic/likely pathogenic variant**, **susceptibility allele**, **autosomal dominant inheritance**, **incomplete penetrance** |
| Mechanism / pathophysiology | Current model emphasizes **repetitive alveolar epithelial injury** in a genetically susceptible, aging lung, followed by **aberrant repair**, **fibroblast expansion**, **myofibroblast differentiation**, **extracellular matrix accumulation**, increasing **tissue stiffness**, and feed-forward profibrotic signaling. Core pathways include **TGF-beta**, **Wnt/beta-catenin**, **Hippo/YAP-TAZ**, **Hedgehog**, epithelial ER stress, senescence/telomere dysfunction, and immune-metabolic remodeling. Single-cell/spatial studies highlight **IR-AT2**, **aberrant basaloid cells**, **CTHRC1+ fibroblasts**, meflin+ fibroblasts, and **SPP1hi macrophages** in spatial fibrotic niches. (zuo2025idiopathicpulmonaryfibrosis pages 1-2, senhaji2026idiopathicpulmonaryfibrosis pages 2-4, zuo2025idiopathicpulmonaryfibrosis pages 2-2, senhaji2026idiopathicpulmonaryfibrosis pages 4-5) | GO: **fibrotic process / fibrosis**, **transforming growth factor beta signaling pathway**, **extracellular matrix organization**, **epithelial to mesenchymal transition**, **cellular senescence**, **wound healing**, **collagen fibril organization**; CL: **alveolar type 2 epithelial cell**, **fibroblast**, **myofibroblast**, **macrophage** |
| Diagnostics | Diagnosis relies on **multidisciplinary discussion** integrating exposure/autoimmune history, serology, **HRCT**, PFTs, and sometimes tissue sampling. For IPF, HRCT showing **definite/probable UIP** with exclusion of alternative causes can establish diagnosis; biopsy/cryobiopsy is considered when imaging is indeterminate. Useful biomarker candidates include **KL-6**, **SP-A/SP-D**, and **MMP-7**, though broad routine implementation remains limited. Differential diagnosis includes CTD-ILD, hypersensitivity pneumonitis, asbestosis, drug-induced ILD, and non-IPF IIP subtypes. (senhaji2026idiopathicpulmonaryfibrosis pages 7-9, senhaji2026idiopathicpulmonaryfibrosis pages 9-10) | Imaging/pathology labels: **usual interstitial pneumonia (UIP)**, **probable UIP**, **indeterminate for UIP**, **NSIP pattern**, **organizing pneumonia pattern**; HPO: **Abnormality of pulmonary function test**; specimen terms: **surgical lung biopsy**, **transbronchial lung cryobiopsy** |
| Treatment | **Antifibrotics** are standard for IPF: **nintedanib** and **pirfenidone** slow FVC decline and reduce progression/exacerbation risk. Nonpharmacologic management includes **pulmonary rehabilitation**, **supplemental oxygen** when indicated, symptom-focused supportive/palliative care, vaccination and comorbidity management, and **lung transplantation** for appropriate candidates. Management differs across IIP subtypes: e.g., COP is typically corticosteroid-responsive, smoking-related RB-ILD/DIP emphasize smoking cessation, and non-IPF inflammatory phenotypes may involve immunomodulation rather than primary antifibrotic therapy. (kreuter2021thediagnosisand pages 1-2, viswanathan2024patientprofilebasedmanagement pages 17-18, senhaji2026idiopathicpulmonaryfibrosis pages 12-14, man2024acomparisonof pages 4-5) | NCIT/intervention labels: **Nintedanib**, **Pirfenidone**, **Pulmonary Rehabilitation**, **Oxygen Therapy**, **Lung Transplantation**, **Palliative Care**, **Corticosteroid Therapy**, **Smoking Cessation** |
| Models / other species | Human IIP/IPF is modeled mainly with **induced pulmonary fibrosis systems** rather than a fully faithful spontaneous animal disease. Common platforms include **bleomycin-induced fibrosis** (mouse and other species), xenograft models using human IPF fibroblasts, genetic/telomere-related models, and ex vivo/in vitro systems such as lung explants or organoid-like epithelial-fibroblast models. Naturally occurring canine pulmonary fibrosis, especially in **West Highland White Terriers**, shows similarities to human IPF but has limited utility because of low prevalence and incompletely defined pathogenesis; zoonotic transmission is not a feature. (frohlich2024animalsinrespiratory pages 17-18) | NCBI Taxon labels: **Homo sapiens**, **Mus musculus**, **Canis lupus familiaris**; model labels: **bleomycin-induced pulmonary fibrosis**, **xenograft model**, **genetic model**, **lung explant**, **organoid** |


*Table: This compact table organizes the key knowledge-base domains for idiopathic interstitial pneumonia, explicitly distinguishing the IIP family from IPF as a subtype. It also provides ontology-ready term suggestions to support structured disease annotation.*

## 1. Disease information

### Definition and classification

IIPs are idiopathic disorders involving the lung interstitium, alveoli, small airways, and—in PPFE—the pleura/subpleural lung. Classification is clinicoradiologic-pathologic:

- **Chronic fibrosing:** IPF/UIP, iNSIP; PPFE is a rare distinctive fibrosing entity.
- **Smoking-related:** RB-ILD and DIP.
- **Acute/subacute:** COP and AIP.
- **Rare lymphoid:** idiopathic LIP.
- **Unclassifiable IIP:** used when available clinical, imaging, or pathologic findings are discordant or insufficient.

UIP is a morphologic pattern and is **not automatically IPF**: it can occur with connective-tissue disease, chronic hypersensitivity pneumonitis, asbestosis, and other conditions. IPF requires an idiopathic clinical context plus a definite/probable UIP pattern and exclusion of alternatives. UIP pathology is temporally and spatially heterogeneous, with fibroblast foci, architectural destruction, and honeycomb change; NSIP is more temporally uniform. (drimus2025highresolutionctfindings pages 10-12, kreuter2021thediagnosisand pages 16-16, senhaji2026idiopathicpulmonaryfibrosis pages 9-10)

### Identifiers and synonyms

- **MONDO:** idiopathic interstitial pneumonia, **MONDO_0002429**.
- **IPF cross-resource identifier retrieved:** **EFO_0000768**.
- Common umbrella synonyms: *idiopathic interstitial pneumonias*, *idiopathic diffuse parenchymal lung diseases*.
- Historical terms should be mapped cautiously: *cryptogenic fibrosing alveolitis* generally maps to IPF, while *bronchiolitis obliterans organizing pneumonia* is an older term for COP.
- A reliable single OMIM or Orphanet entry does not represent the whole IIP family. Familial pulmonary fibrosis/telomere syndromes should be represented separately from sporadic IIP.
- ICD coding is jurisdiction/version dependent and often conflates morphologic patterns and diseases; **J84-series** codes are generally used for other interstitial pulmonary diseases. Exact ICD-10-CM/ICD-11 subtype mapping should be validated against the release deployed by the knowledge base rather than inferred from literature.

The information in this report is **aggregated disease-level evidence** from guidelines, reviews, trials, and cohorts—not individual-patient EHR data.

## 2. Etiology and risk/protective factors

### Causal framework

“Iidiopathic” means that no single external or systemic cause is demonstrable after evaluation; it does not mean absence of risk factors. In IPF, aging, inherited epithelial vulnerability, and repeated environmental microinjury interact. AIP is an idiopathic diffuse alveolar-damage syndrome; COP reflects idiopathic organizing injury; RB-ILD/DIP are strongly associated with tobacco smoke despite retaining historical IIP labels.

### Genetic factors

**Common susceptibility allele—not a Mendelian cause:**

- **MUC5B rs35705950**, a promoter variant, is the strongest common IPF susceptibility factor. Reported risk is approximately sixfold in heterozygotes and 20-fold in homozygotes, with about 34-fold higher expression in unaffected lung. Penetrance is incomplete, and carriers paradoxically tend to have better survival once IPF occurs. Minor-allele frequency is population dependent: approximately 0.11 in Europeans, 0.02 in African/African-American populations, and 0.007 in East Asians. (zhumagaliyeva2025geneticdeterminantsof pages 2-4, liu2025anoverviewof pages 1-3)
- Other common susceptibility loci include **DSP, FAM13A, TOLLIP, DPP9, ATP11A, SPPL2C**, and telomere-associated loci. A 2024 systematic review found 88 associated SNPs across 58 genes/loci; observed odds ratios ranged from 0.27 to 7.82, but functional relevance remained unknown for about half of implicated genes. (dhooria2024commonsinglenucleotide pages 12-13)

**Rare pathogenic/likely pathogenic variants:**

- Telomere maintenance: **TERT, TERC, RTEL1, PARN**, plus less frequent genes such as **NAF1**. These are generally germline loss-of-function or function-disrupting variants and can produce short-telomere syndromes with pulmonary fibrosis, bone-marrow failure, liver disease, premature graying, or related features.
- Surfactant/epithelial homeostasis: **SFTPA1, SFTPA2, SFTPC, ABCA3**. Missense variants may cause protein misfolding, ER stress, impaired surfactant processing, and epithelial apoptosis; **ABCA3** disease is often recessive, whereas adult familial disease involving SFTPC/SFTPA genes is commonly dominant.
- Rare telomere variants occur in roughly 20–30% of familial and 2–5% of sporadic pulmonary-fibrosis cases. One review estimated pathogenic variants with frequency below 0.1% in about one-quarter of familial pulmonary-fibrosis families. (zhumagaliyeva2025geneticdeterminantsof pages 2-4, zhumagaliyeva2025geneticdeterminantsof pages 7-8, cerri2024geneticriskfactors pages 2-4)
- Open Targets identifies evidence linking IIP/IPF to **TERT, PARN, RTEL1, SFTPA2, MUC5B**, and **DSP**, with supporting studies including PMIDs 25848748, 26116823, 23453664, 23959892, 19100526, 20502709, 21506741, and 26669357. (OpenTargets Search: idiopathic pulmonary fibrosis)

**Inheritance:** Familial pulmonary fibrosis is usually autosomal dominant with incomplete, age-dependent penetrance and variable expressivity. For TERT variants, penetrance after age 60 has been estimated at about 60% in men and 50% in women. Anticipation-like earlier disease may occur through inherited telomere shortening, but this is not a classical repeat-expansion disorder. Germline mosaicism, carrier frequency, and founder effects are variant/family specific; no general values are established for IIP. (zhumagaliyeva2025geneticdeterminantsof pages 1-2, zhumagaliyeva2025geneticdeterminantsof pages 7-8)

**Variant annotation caveat:** Pathogenicity, ACMG class, HGNC ID, exact consequence, and gnomAD frequency must be stored **per variant**, not assigned at gene level. MUC5B rs35705950 should be annotated as a common risk allele, not “pathogenic.” Chromosomal aneuploidy, recurrent translocation, mitochondrial inheritance, and repeat expansions are not established general causes of adult IIP.

### Environmental and lifestyle factors

Human epidemiologic evidence implicates cigarette smoke, metal/wood/stone/silica-containing dusts, farming and livestock exposures, air pollution, and possibly chronic microaspiration. Male sex and older age are strong demographic correlates. Increased airway bacterial burden/dysbiosis has been observed, but no bacterium or virus is established as the primary cause of IPF. Gastroesophageal reflux and microaspiration are plausible epithelial-injury amplifiers, not proven universal causes. (zhumagaliyeva2025geneticdeterminantsof pages 1-2, senhaji2026idiopathicpulmonaryfibrosis pages 4-5, senhaji2026idiopathicpulmonaryfibrosis pages 7-9)

### Gene–environment interaction and protective factors

A useful causal model is: **rare/common genetic susceptibility + aging → reduced epithelial resilience; smoking/dust/pollution/microaspiration → repeated injury; impaired repair → fibrosis**. Environmental exposures markedly raise disease likelihood in telomere-variant carriers. (zhumagaliyeva2025geneticdeterminantsof pages 1-2, zhumagaliyeva2025geneticdeterminantsof pages 7-8)

No genetic or dietary factor is validated as broadly protective. Smoking avoidance/cessation, occupational exposure control, and air-quality improvement are prudent risk-reduction measures, but direct evidence that they prevent idiopathic IPF is limited. The apparent survival advantage of MUC5B rs35705950 after diagnosis is prognostic and should not be interpreted as protective against disease onset. TOLLIP–N-acetylcysteine pharmacogenetic findings remain investigational. (zhumagaliyeva2025geneticdeterminantsof pages 2-4, senhaji2026idiopathicpulmonaryfibrosis pages 4-5)

## 3. Phenotypes

### Core IPF/fibrotic-IIP phenotype

- **Progressive exertional dyspnea:** adult/late-adult onset; initially exertional, ultimately severe and activity limiting. Suggested HPO: *Dyspnea*, *Exercise intolerance*.
- **Chronic usually dry cough:** progressive or persistent; reported in approximately 20–80% of IPF cohorts. Suggested HPO: *Cough*. (senhaji2026idiopathicpulmonaryfibrosis pages 16-18)
- **Fine bibasal inspiratory crackles:** common physical sign. Suggested HPO: *Abnormal respiratory crackles*.
- **Digital clubbing:** about 25–50% in IPF. Suggested HPO: *Clubbing*. (senhaji2026idiopathicpulmonaryfibrosis pages 7-9)
- **Restrictive physiology:** reduced FVC/TLC with reduced DLCO; severity varies and typically progresses. Suggested HPO: *Restrictive ventilatory defect*, *Decreased DLCO*.
- **Exertional hypoxemia and reduced six-minute-walk distance:** downstream gas-exchange and functional abnormalities; poor values predict worse outcome.
- **Fatigue, deconditioning, anxiety/depression:** important secondary manifestations; depression was reported in 22% of pharmaceutical-trial cohorts. (walters2025comorbiditiesinthe pages 3-4)

### Subtype variation

- **COP:** subacute cough, dyspnea, fever/malaise, patchy peripheral or peribronchovascular consolidation; often steroid responsive but may relapse.
- **AIP:** abrupt respiratory failure over days to weeks, bilateral opacities, diffuse alveolar damage; very severe.
- **iNSIP:** subacute/chronic dyspnea and cough, usually more uniform ground-glass/reticular disease; cellular forms may improve, fibrotic forms may progress.
- **RB-ILD/DIP:** smokers, cough/dyspnea and reduced DLCO; often mild-to-moderate but occasionally progressive.
- **LIP:** cough/dyspnea with diffuse ground glass, nodules, septal thickening, and cysts; autoimmune/immunodeficiency causes must be excluded.
- **PPFE:** upper-lobe pleural/subpleural fibrosis, reduced chest dimensions, low BMI, recurrent pneumothorax, and progressive restriction.

Robust phenotype frequencies for these rare subtypes are not consistently available. HPO terms should therefore be linked with evidence strength rather than assumed universal.

### Quality of life

Dyspnea, cough, oxygen dependence, fatigue, and loss of mobility substantially impair health-related quality of life; one molecular-profiling report described mobility-limiting dyspnea and quality of life lower than in many malignancies. Pulmonary rehabilitation improves walk distance, dyspnea, and quality of life over 12–16 weeks, although benefits may diminish after six months. (jiang2025exploringthecellular pages 1-2, senhaji2026idiopathicpulmonaryfibrosis pages 16-18)

## 4. Genetic and molecular information

### Gene/protein consequences

- **TERT/TERC/RTEL1/PARN:** deficient telomere maintenance → critically short telomeres → AT2-cell senescence/apoptosis and reduced regenerative capacity.
- **SFTPC/SFTPA1/SFTPA2/ABCA3:** aberrant surfactant synthesis/processing → misfolding, ER stress, unfolded-protein response, epithelial death.
- **MUC5B rs35705950:** excessive distal-airway MUC5B → impaired mucociliary clearance and altered epithelial microenvironment.
- **DSP:** compromised epithelial adhesion/barrier integrity.
- **TOLLIP:** altered innate immune signaling and possible treatment-response modification.

Telomere-variant carriers have aggressive disease: median transplant-free survival was reported as 4.2 years versus 7.2 years in noncarriers, with approximately 300 mL annual FVC decline and a 5.8-percentage-point annual DLCO decline. (zhumagaliyeva2025geneticdeterminantsof pages 7-8)

### Modifier and epigenetic information

Common polygenic background modifies susceptibility and outcome around rare variants. DNA methylation, histone changes, miR-21/miR-29 and other noncoding RNAs regulate TGF-β signaling, ECM production, epithelial transition states, and fibroblast activation. Approximately one-fifth of gene-expression differences in IPF fibroblasts have been associated with altered methylation, but causality and clinical utility remain unproven. (senhaji2026idiopathicpulmonaryfibrosis pages 2-4, cerri2024geneticriskfactors pages 2-4)

Somatic copy-number changes on chromosomes 16 and 19 have been reported in abnormal epithelial cells, but they are research observations—not routine diagnostic lesions. No recurrent large chromosomal abnormality defines IIP. (zuo2025idiopathicpulmonaryfibrosis pages 2-2)

## 5. Environmental information

Relevant non-genetic exposures include tobacco smoke, occupational inorganic/organic dust, ambient particulate pollution, and recurrent aspiration. They should be recorded with exposure intensity, duration, latency, protective-equipment use, and temporal relationship. A disease remains “idiopathic” only after plausible causal exposure syndromes—especially hypersensitivity pneumonitis, pneumoconiosis/asbestosis, and drug-induced ILD—are reasonably excluded.

Infection may trigger acute worsening, and altered communities enriched for organisms such as *Staphylococcus* and *Streptococcus* have been reported, but microbiome association does not establish infectious causation. No vaccine prevents IIP itself. (senhaji2026idiopathicpulmonaryfibrosis pages 7-9)

Suggested CHEBI-level exposure labels include nicotine/tobacco-smoke constituents, crystalline silica, asbestos fibers, and particulate matter where supported by a patient-specific exposure history; these are risk/exclusion annotations, not universal IIP causes.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream susceptibility:** aging, telomere shortening, surfactant/epithelial variants, MUC5B-associated mucociliary dysfunction, smoking/dust/pollution or aspiration.
2. **Initiating injury:** repeated AT1/AT2 epithelial injury, ER and oxidative stress, mitochondrial dysfunction, apoptosis/senescence, basement-membrane disruption.
3. **Aberrant repair:** AT2 regenerative failure and emergence of transitional/aberrant basaloid epithelium; TGF-β, PDGF, FGF, Wnt/β-catenin, Hedgehog, and Hippo/YAP–TAZ signaling become activated.
4. **Mesenchymal response:** fibroblast recruitment/proliferation and myofibroblast differentiation; collagen, fibronectin, and other ECM accumulate.
5. **Feed-forward fibrosis:** matrix stiffening further activates integrins and YAP/TAZ, maintaining TGF-β activity and fibroblast survival.
6. **Tissue/clinical outcome:** fibroblastic foci, traction bronchiectasis, honeycomb remodeling, reduced compliance and diffusion, hypoxemia, pulmonary hypertension, and respiratory failure. (senhaji2026idiopathicpulmonaryfibrosis pages 2-4, zuo2025idiopathicpulmonaryfibrosis pages 2-2)

### Cells, immunity, metabolism, and profiling

Single-cell/spatial studies identify **IPF-related AT2 cells, KRT5−/KRT17+ aberrant basaloid cells, CTHRC1+ collagen-producing fibroblasts, meflin+ fibroblasts, and SPP1-high macrophages**. These findings support disease as a spatially organized epithelial–mesenchymal–immune–vascular network rather than isolated fibroblast dysfunction. (zuo2025idiopathicpulmonaryfibrosis pages 1-2)

Immune cells provide profibrotic cytokines and metabolic signals; macrophage polarization changes as distal remodeling advances. Chronic inflammation is contributory, but IPF is no longer viewed primarily as an inflammatory disease. Altered glycolysis, lipid handling, mitochondrial energetics, iron homeostasis, and amino-acid metabolism are reported, but none is yet a routine biochemical diagnostic defect.

A recent multi-omics computational study identified **GREM1, UGT1A6, CDH2, TDO2, HS3ST1, ADGRF5, and MPO** and reported an AUC of 0.987; because protein-level and prospective validation are lacking, this should be stored as discovery-stage evidence. (jiang2025exploringthecellular pages 1-2)

Suggested annotations:

- **GO biological process:** extracellular matrix organization; collagen fibril organization; wound healing; TGF-β receptor signaling; epithelial-cell apoptosis; cellular senescence; response to oxidative stress; epithelial-to-mesenchymal transition.
- **GO cellular component:** extracellular matrix, endoplasmic reticulum, mitochondrion, telomere, basement membrane.
- **CL:** alveolar type 1 cell, alveolar type 2 cell, airway basal cell, fibroblast, myofibroblast, macrophage, endothelial cell, plasma cell.

## 7. Anatomical structures affected

- **Primary organ/system:** bilateral lungs; respiratory system.
- **Primary sites:** distal parenchyma, alveoli, interstitium, alveolar-capillary interface. UIP/IPF is predominantly basal and subpleural; PPFE is upper-lobe pleural/subpleural.
- **Tissues:** alveolar epithelium, basement membrane, interstitial connective tissue, pulmonary microvasculature, and distal airways.
- **Secondary effects:** pulmonary vasculature/right ventricle through pulmonary hypertension; systemic skeletal muscle through hypoxemia and deconditioning.
- **Lateralization:** generally bilateral, frequently heterogeneous and asymmetric in severity—not a unilateral disease.

Suggested UBERON labels: lung, pulmonary alveolus, lung interstitium, respiratory bronchiole, visceral pleura, pulmonary artery. Suggested GO-CC: extracellular matrix, basement membrane, endoplasmic reticulum, mitochondrion, telomere.

## 8. Temporal development

IPF usually begins insidiously after age 50, with a mean around 66 years in one review and male predominance. Symptoms evolve over months to years, followed by variable but usually irreversible progression. Some patients decline steadily, some remain temporarily stable, and others have stepwise loss from acute exacerbations. (senhaji2026idiopathicpulmonaryfibrosis pages 1-2, senhaji2026idiopathicpulmonaryfibrosis pages 7-9)

A practical stage model is:

- **Preclinical susceptibility/ILA:** incidental interstitial lung abnormalities; reported progression risk approximately 20% at two years and up to 50% by four to six years.
- **Early disease:** mild symptoms, preserved volumes but reduced DLCO, limited CT fibrosis.
- **Established progressive fibrosis:** worsening symptoms, FVC/DLCO decline, increasing traction bronchiectasis/honeycombing.
- **Advanced/end stage:** resting/exertional hypoxemia, pulmonary hypertension, respiratory failure, transplant or palliative-care needs. (senhaji2026idiopathicpulmonaryfibrosis pages 9-10)

For non-IPF fibrotic ILD, the 2022 PPF construct requires at least two of worsening symptoms, physiologic progression (absolute FVC decline ≥5% or DLCO decline ≥10%), and radiologic progression within one year, with no alternative explanation. Expert consensus also regards ≥10% FVC decline or unequivocal HRCT progression as sufficient evidence of clinically important progression. (senhaji2026idiopathicpulmonaryfibrosis pages 9-10)

COP and cellular NSIP may remit spontaneously or with corticosteroids; relapse can occur. AIP is acute and often fatal. IPF rarely remits, and current therapy slows rather than reverses it.

## 9. Inheritance and population epidemiology

### Epidemiology

IIP-family incidence is difficult to aggregate because definitions and coding vary. For **IPF**, a meta-analysis of 26 studies through November 7, 2023 estimated:

- Global incidence: **5.8/100,000/year**; Asia 4.4, Europe 5.1, North America 9.0.
- Global prevalence: **17.7/100,000**; Asia 14.8, Europe 14.6, North America 27.2.

The authors emphasized substantial heterogeneity from case algorithms, referral populations, diagnostic definitions, and regional exposures. (golchin2025incidenceandprevalence pages 1-2)

IPF predominantly affects older adults and men; a roughly 3:1 male:female ratio is reported in one pooled overview, though registry ratios vary. MUC5B frequency and IPF burden are higher in European-ancestry populations, but underdiagnosis and ascertainment differences complicate ethnic comparisons. (liu2025anoverviewof pages 1-3, golchin2025incidenceandprevalence pages 1-2)

### Familial disease

Familial pulmonary fibrosis accounts for approximately 5–20% of IPF/pulmonary-fibrosis presentations depending on definition and ascertainment. Inheritance is usually multifactorial/polygenic in sporadic disease and autosomal dominant with incomplete age-dependent penetrance in many rare-variant families. Consanguinity is particularly relevant to recessive surfactant disorders such as ABCA3 deficiency, but not to typical late-onset IPF. (zhumagaliyeva2025geneticdeterminantsof pages 1-2, liu2025anoverviewof pages 1-3)

## 10. Diagnostics

### Clinical workflow

1. Confirm ILD clinically and with **HRCT**.
2. Obtain detailed drug, occupational, environmental, avian/mold, smoking, aspiration, and family history.
3. Screen for connective-tissue disease using examination and targeted serology.
4. Perform spirometry, lung volumes, DLCO, resting/exertional oximetry, and six-minute walk testing.
5. Conduct multidisciplinary review.
6. Use BAL, cryobiopsy, or surgical biopsy selectively when the diagnosis remains uncertain and results would change management. (senhaji2026idiopathicpulmonaryfibrosis pages 7-9, senhaji2026idiopathicpulmonaryfibrosis pages 9-10, kreuter2021thediagnosisand pages 2-4)

### Imaging and pathology

**Definite UIP HRCT:** basal/subpleural reticulation, traction bronchiectasis/bronchiolectasis, and honeycombing without features suggesting another diagnosis. **Probable UIP:** similar distribution and traction change without honeycombing. NSIP is more uniform, commonly with ground-glass opacity, fine reticulation, and subpleural sparing. (drimus2025highresolutionctfindings pages 10-12, senhaji2026idiopathicpulmonaryfibrosis pages 7-9)

When tissue is needed, transbronchial cryobiopsy has reported diagnostic yields of 74–98% in selected experienced centers. Surgical lung-biopsy mortality is approximately 1.7% electively but 17% in nonelective procedures; reported complications include infection 6.5%, acute IPF exacerbation 6.4%, prolonged air leak 5.9%, and bleeding 0.8%. (senhaji2026idiopathicpulmonaryfibrosis pages 9-10)

### Biomarkers and omics

Candidate serum markers include **KL-6/MUC1, SP-A, SP-D, MMP-7, YKL-40, periostin**, and collagen-turnover products. KL-6 tracks epithelial activation and disease extent; MMP-7 correlates with fibrosis burden, FVC/DLCO decline, and mortality. None replaces multidisciplinary diagnosis, and standardized broad clinical implementation remains limited. (senhaji2026idiopathicpulmonaryfibrosis pages 9-10)

RNA-seq, proteomics, metabolomics, epigenomics, liquid biopsy, xenon MRI, radiomics, and machine learning remain investigational. They should not be represented as validated routine diagnostics.

### Genetic testing

Testing is most appropriate for familial pulmonary fibrosis, onset before approximately 50 years, syndromic short-telomere features, or suspected surfactant disorder. Recommended strategy is genetic counseling followed by a pulmonary-fibrosis panel including telomere and surfactant genes; WES/WGS can be used if panel testing is negative or phenotype is atypical. Telomere-length testing may support interpretation but is not gene specific. CMA, karyotyping, FISH, mitochondrial DNA testing, and repeat-expansion assays are not routine for typical IIP.

### Differential diagnosis

Exclude connective-tissue disease–ILD, fibrotic hypersensitivity pneumonitis, occupational pneumoconiosis/asbestosis, drug/radiation injury, sarcoidosis, infection, edema, aspiration, smoking-related disease, and other IIP subtypes. A UIP pattern alone does not settle etiology. (drimus2025highresolutionctfindings pages 10-12, senhaji2026idiopathicpulmonaryfibrosis pages 9-10)

### Screening

No population screening is recommended. First-degree relatives in familial pulmonary fibrosis may be offered genetic counseling, symptom/PFT assessment, and individualized HRCT surveillance in specialist programs. Incidental ILA warrants risk-based follow-up, not automatic labeling as IPF.

## 11. Outcome and prognosis

IPF median survival is approximately **3–5 years after diagnosis**, but individual trajectories vary. Telomere variants, older age, male sex, low or rapidly falling FVC/DLCO, reduced walk distance/desaturation, extensive HRCT fibrosis, pulmonary hypertension, and acute exacerbation predict worse outcome. (zhumagaliyeva2025geneticdeterminantsof pages 7-8, senhaji2026idiopathicpulmonaryfibrosis pages 1-2, golchin2025incidenceandprevalence pages 1-2)

Acute exacerbations occur in approximately **5–20% annually** and carry extremely poor outcomes—reported mortality near 80% and median survival of 3–4 months. Pulmonary hypertension affects approximately 8–15% at diagnosis and up to 86% in advanced disease. Combined pulmonary fibrosis/emphysema occurs in 8–51% of IPF series and has reported median survival of 25 months. (senhaji2026idiopathicpulmonaryfibrosis pages 16-18, senhaji2026idiopathicpulmonaryfibrosis pages 18-20)

IPF is associated with about a fivefold increased lung-cancer risk; one synthesis reported cumulative incidence of 3.3% at one year, 15.4% at five years, and 54.7% at ten years, although the highest estimate may reflect selected long-term cohorts and competing-risk methods. (senhaji2026idiopathicpulmonaryfibrosis pages 16-18)

Common trial-cohort comorbidities include gastroesophageal reflux 45%, hypertension 45%, hyperlipidemia 38%, ischemic heart disease 18%, diabetes 16%, and depression 22%. Trial populations generally underrepresent multimorbid real-world patients. (walters2025comorbiditiesinthe pages 3-4)

COP and cellular NSIP usually have substantially better prognosis than IPF; fibrotic NSIP, PPFE, and some DIP/LIP cases may develop progressive fibrosis. AIP has high short-term mortality. No universal five- or ten-year survival statistic is valid across the entire IIP family.

## 12. Treatment

### IPF pharmacotherapy

- **Nintedanib**—intracellular tyrosine-kinase inhibitor targeting VEGFR/FGFR/PDGFR signaling; NCIT suggestion: *Nintedanib Treatment*. In INPULSIS, annual FVC decline was −113.6 mL versus −207.3 mL with placebo. Another synthesis reported −124 versus −218 mL/year. Diarrhea occurred in 52.5% versus 16.1% with placebo; nausea, anorexia, weight loss, transaminase elevation, and bleeding risk also require monitoring. (viswanathan2024patientprofilebasedmanagement pages 17-18, man2024acomparisonof pages 4-5)
- **Pirfenidone**—antifibrotic with effects on TGF-β-associated signaling; NCIT suggestion: *Pirfenidone Treatment*. CAPACITY/ASCEND showed slower FVC decline and a pooled 48% relative reduction in risk of death in one review. Important adverse effects are nausea/dyspepsia, appetite/weight loss, photosensitivity/rash, and hepatotoxicity. (senhaji2026idiopathicpulmonaryfibrosis pages 12-14)

Neither therapy reverses fibrosis. Comparative evidence does not establish a universally superior agent; selection depends on comorbidities, interactions, adverse-effect profile, access, and patient preference. Routine prednisone/azathioprine/N-acetylcysteine combination therapy is inappropriate for IPF.

### Subtype-specific strategy

- **iNSIP:** identify occult autoimmune disease; corticosteroids with or without steroid-sparing immunomodulation for inflammatory disease; consider antifibrotic treatment if a progressive fibrotic phenotype emerges.
- **COP:** systemic corticosteroids are typical; observe selected mild cases and treat relapses individually.
- **AIP:** ICU supportive care, lung-protective ventilation; corticosteroids are often used despite weak evidence.
- **RB-ILD/DIP:** smoking cessation and exposure removal; corticosteroids for clinically important persistent disease.
- **LIP:** treat an identified autoimmune, immunodeficiency, or infectious driver; corticosteroids/immunomodulation in selected idiopathic cases.
- **PPFE:** no proven disease-modifying drug; manage complications and refer early for transplantation if progressive.

### Supportive and interventional care

Pulmonary rehabilitation, oxygen for resting/exertional hypoxemia, vaccination, nutrition, cough and dyspnea management, comorbidity treatment, advance-care planning, and palliative care are core components. Rehabilitation improves walk distance, dyspnea, and quality of life over 12–16 weeks. Lung transplantation is the only intervention capable of replacing the fibrotic lungs; approximately half of more than 4,600 annual lung transplants worldwide are performed for ILD. (senhaji2026idiopathicpulmonaryfibrosis pages 16-18)

Suggested NCIT interventions: oxygen therapy, pulmonary rehabilitation, lung transplantation, palliative care, smoking cessation, corticosteroid therapy.

### Emerging trials

ClinicalTrials.gov searches identified ongoing/recent phase II–III IPF studies including:

- **BMS-986278**, phase III, **NCT06003426**, approximately 1,255 participants; lysophosphatidic-acid receptor 1 antagonist.
- **SC1011**, phase II/III, **NCT06125327**, 210 participants.
- **Axatilimab**, phase II MAXPIRe, **NCT06132256**, 145 participants; CSF1R-directed monoclonal antibody.
- **DWN12088**, phase II, **NCT05389215**, 102 participants; prolyl-tRNA synthetase inhibitor.
- **LYT-100/deupirfenidone**, phase II, **NCT05321420**, 240 participants.
- **CAL101**, phase II, **NCT06736990**, 150 participants.

Trial status and enrollment change over time; these entries are experimental and should be refreshed directly from https://clinicaltrials.gov before operational use.

No approved gene, RNA, or cell therapy exists for IIP/IPF. Cell therapies, senolytics, integrin inhibitors, telomere-directed approaches, and epithelial regenerative strategies remain experimental.

## 13. Prevention

There is no proven primary prevention for idiopathic disease. Reasonable measures are smoking avoidance/cessation, control of occupational dust and fumes, respiratory protection, air-pollution mitigation, and avoidance of unnecessary pneumotoxic drugs. Vaccination against influenza, COVID-19, pneumococcus, and other age/risk-appropriate infections is **tertiary prevention** of infection-related morbidity, not prevention of IIP.

Secondary prevention consists of earlier recognition in symptomatic or high-risk familial individuals, specialist review of incidental ILA, and surveillance for physiologic/radiologic progression. Tertiary prevention includes antifibrotics for IPF, oxygen, rehabilitation, infection prevention, comorbidity management, early transplant referral, and advance-care planning.

For families with a pathogenic variant, genetic counseling should address autosomal-dominant, age-dependent risk, variable expressivity, cascade testing, reproductive options, and possible preimplantation/prenatal testing. Such counseling is not indicated merely because a patient carries the common MUC5B risk allele.

## 14. Other species and natural disease

Naturally occurring canine pulmonary fibrosis, particularly in **West Highland White Terriers** (*Canis lupus familiaris*, NCBI Taxon 9615), can resemble human IPF through subpleural/peribronchiolar fibrosis, alveolar epithelial changes, and ground-glass opacities. Its low prevalence and incompletely defined pathogenesis limit its utility as a standardized model. (frohlich2024animalsinrespiratory pages 17-18)

Pulmonary fibrosis also occurs in cats and other animals, but veterinary entities should not be assumed orthologous to human IIP without molecular validation. Conserved TGF-β, ECM, epithelial-injury, senescence, and telomere mechanisms support comparative research. IIP is noninfectious and has **no zoonotic transmission**.

No confidently validated VBO breed identifier or single orthologous causal gene for canine idiopathic pulmonary fibrosis was retrieved; these should be left unassigned rather than inferred.

## 15. Model organisms and experimental systems

- **Bleomycin-induced fibrosis:** most common mouse model; also produces fibrosis in nonhuman primates, dogs, and sheep. Strengths are reproducibility and utility for inflammatory/fibrotic pathways. Major limitation: injury is acute and often partially reversible, unlike heterogeneous, age-related, relentlessly progressive human IPF. (frohlich2024animalsinrespiratory pages 17-18)
- **Human-cell xenograft:** injection of IPF fibroblasts into immunodeficient mice can generate a fibrotic phenotype within 30–35 days; useful for human mesenchymal behavior but lacks an intact immune system. (frohlich2024animalsinrespiratory pages 17-18)
- **Genetic models:** telomerase/telomere, surfactant-processing, epithelial-injury, senescence, and TGF-β pathway perturbations dissect specific mechanisms but rarely recapitulate the full human disease.
- **Viral/aging models:** murine gammaherpesvirus-68 in aged mice models infection–aging interaction, not idiopathic disease itself.
- **In vitro/ex vivo:** primary AT2 cells, fibroblasts, precision-cut lung slices, air–liquid-interface cultures, organoids, iPSC-derived epithelium, and decellularized ECM permit human-specific perturbation and screening but lack whole-organ mechanics, circulation, and complete immunity.

No existing model reproduces the complete human phenotype. A translational strategy combining human tissue/single-cell data, organoid or explant systems, and more than one in-vivo model is preferable.

## Recent developments and expert interpretation

The most important 2023–2024 developments were: systematic consolidation of common IPF risk alleles; greater clinical attention to telomere/surfactant genetics; maturation of single-cell/spatial maps of epithelial, fibroblast, and macrophage niches; consensus operationalization of progressive pulmonary fibrosis; and expanded real-world guidance for antifibrotic and holistic care. The 2024 SNP review concluded that “**several common single nucleotide polymorphisms in over 50 genes have been found associated with susceptibility to idiopathic pulmonary fibrosis**,” while noting that the function of more than half remains unexplored. (dhooria2024commonsinglenucleotide pages 12-13)

A 2024 treatment position statement emphasized a “**multi-faceted approach to the management of IPF and progressive pulmonary fibrosis**,” reflecting expert consensus that drug therapy alone is insufficient. (viswanathan2024patientprofilebasedmanagement pages 17-18)

The evidence base has important gaps: subtype-specific IIP epidemiology and phenotype frequencies are sparse; no biomarker panel is sufficiently validated to replace multidisciplinary diagnosis; polygenic scores are not ready for population screening; spatial/single-cell signatures remain discovery tools; and the absence of a faithful progressive animal model continues to impede translation.

## Selected dated sources and URLs

- Dhooria et al. **July 2024**, *European Respiratory Review*, common IPF SNP systematic review: https://doi.org/10.1183/16000617.0018-2024. (dhooria2024commonsinglenucleotide pages 12-13)
- Cerri et al. **November 2024**, genetics/epigenetics of idiopathic and non-idiopathic ILD: https://doi.org/10.3390/medicina60121967. (cerri2024geneticriskfactors pages 2-4)
- Viswanathan et al. **September 2024**, nintedanib and real-world management: https://doi.org/10.1007/s41030-024-00271-1. (viswanathan2024patientprofilebasedmanagement pages 17-18)
- Man et al. **February 2024**, nintedanib versus pirfenidone systematic review: https://doi.org/10.7759/cureus.54268. (man2024acomparisonof pages 4-5)
- Fröhlich. **March 2024**, respiratory animal models: https://doi.org/10.3390/ijms25052903. (frohlich2024animalsinrespiratory pages 17-18)
- Wells et al. **December 2024**, expert consensus on progressive pulmonary fibrosis: https://doi.org/10.1186/s12931-024-03070-z.
- Golchin et al. **August 2025**, epidemiologic meta-analysis using studies through November 2023: https://doi.org/10.1186/s12890-025-03836-1. (golchin2025incidenceandprevalence pages 1-2)

**Evidence note:** Exact abstract quotations are included only where directly available from retrieved abstracts. Where no source supported an exact ontology ID, subtype frequency, variant-level ACMG class, or population allele frequency, the report intentionally provides a qualified label or records the field as unavailable rather than extrapolating.

References

1. (kreuter2021thediagnosisand pages 1-2): Michael Kreuter, Ulf Müller-Ladner, Ulrich Costabel, Danny Jonigk, and Claus Peter Heußel. The diagnosis and treatment of pulmonary fibrosis. Deutsches Arzteblatt international, Mar 2021. URL: https://doi.org/10.3238/arztebl.m2021.0018, doi:10.3238/arztebl.m2021.0018. This article has 72 citations and is from a peer-reviewed journal.

2. (senhaji2026idiopathicpulmonaryfibrosis pages 9-10): Lamiyae Senhaji, Nadia Senhaji, Meriame Abbassi, Mariem Karhate, Mounia Serraj, Mohammed El Biaze, Mohamed Chakib Benjelloun, Karim Ouldim, Laila Bouguenouch, and Bouchra Amara. Idiopathic pulmonary fibrosis: a comprehensive review of risk factors, genetics, diagnosis, and therapeutic approaches. Biomedicines, 14:90, Jan 2026. URL: https://doi.org/10.3390/biomedicines14010090, doi:10.3390/biomedicines14010090. This article has 8 citations.

3. (kreuter2021thediagnosisand pages 2-4): Michael Kreuter, Ulf Müller-Ladner, Ulrich Costabel, Danny Jonigk, and Claus Peter Heußel. The diagnosis and treatment of pulmonary fibrosis. Deutsches Arzteblatt international, Mar 2021. URL: https://doi.org/10.3238/arztebl.m2021.0018, doi:10.3238/arztebl.m2021.0018. This article has 72 citations and is from a peer-reviewed journal.

4. (zhumagaliyeva2025geneticdeterminantsof pages 2-4): Ardak Zhumagaliyeva, Joanna Chorostowska-Wynimko, and Aleksandra Jezela-Stanek. Genetic determinants of progressive pulmonary fibrosis: a comprehensive review. International Journal of Molecular Sciences, 26:11846, Dec 2025. URL: https://doi.org/10.3390/ijms262411846, doi:10.3390/ijms262411846. This article has 6 citations.

5. (zuo2025idiopathicpulmonaryfibrosis pages 1-2): Lin Zuo, Qiongliang Liu, Defeng Ye, Jiang Fan, and Liang Wu. Idiopathic pulmonary fibrosis: cellular heterogeneity, mechanisms, and therapeutic implications. MedComm, Dec 2025. URL: https://doi.org/10.1002/mco2.70521, doi:10.1002/mco2.70521. This article has 9 citations.

6. (senhaji2026idiopathicpulmonaryfibrosis pages 2-4): Lamiyae Senhaji, Nadia Senhaji, Meriame Abbassi, Mariem Karhate, Mounia Serraj, Mohammed El Biaze, Mohamed Chakib Benjelloun, Karim Ouldim, Laila Bouguenouch, and Bouchra Amara. Idiopathic pulmonary fibrosis: a comprehensive review of risk factors, genetics, diagnosis, and therapeutic approaches. Biomedicines, 14:90, Jan 2026. URL: https://doi.org/10.3390/biomedicines14010090, doi:10.3390/biomedicines14010090. This article has 8 citations.

7. (viswanathan2024patientprofilebasedmanagement pages 17-18): Vinod K. Viswanathan, Aloke G. Ghoshal, Anant Mohan, Ketaki Patil, Chaitanya Bhargave, Sanjay Choudhari, and Suyog Mehta. Patient profile-based management with nintedanib in patients with idiopathic pulmonary fibrosis. Pulmonary Therapy, 10:377-409, Sep 2024. URL: https://doi.org/10.1007/s41030-024-00271-1, doi:10.1007/s41030-024-00271-1. This article has 5 citations and is from a peer-reviewed journal.

8. (senhaji2026idiopathicpulmonaryfibrosis pages 1-2): Lamiyae Senhaji, Nadia Senhaji, Meriame Abbassi, Mariem Karhate, Mounia Serraj, Mohammed El Biaze, Mohamed Chakib Benjelloun, Karim Ouldim, Laila Bouguenouch, and Bouchra Amara. Idiopathic pulmonary fibrosis: a comprehensive review of risk factors, genetics, diagnosis, and therapeutic approaches. Biomedicines, 14:90, Jan 2026. URL: https://doi.org/10.3390/biomedicines14010090, doi:10.3390/biomedicines14010090. This article has 8 citations.

9. (senhaji2026idiopathicpulmonaryfibrosis pages 7-9): Lamiyae Senhaji, Nadia Senhaji, Meriame Abbassi, Mariem Karhate, Mounia Serraj, Mohammed El Biaze, Mohamed Chakib Benjelloun, Karim Ouldim, Laila Bouguenouch, and Bouchra Amara. Idiopathic pulmonary fibrosis: a comprehensive review of risk factors, genetics, diagnosis, and therapeutic approaches. Biomedicines, 14:90, Jan 2026. URL: https://doi.org/10.3390/biomedicines14010090, doi:10.3390/biomedicines14010090. This article has 8 citations.

10. (senhaji2026idiopathicpulmonaryfibrosis pages 16-18): Lamiyae Senhaji, Nadia Senhaji, Meriame Abbassi, Mariem Karhate, Mounia Serraj, Mohammed El Biaze, Mohamed Chakib Benjelloun, Karim Ouldim, Laila Bouguenouch, and Bouchra Amara. Idiopathic pulmonary fibrosis: a comprehensive review of risk factors, genetics, diagnosis, and therapeutic approaches. Biomedicines, 14:90, Jan 2026. URL: https://doi.org/10.3390/biomedicines14010090, doi:10.3390/biomedicines14010090. This article has 8 citations.

11. (zuo2025idiopathicpulmonaryfibrosis pages 2-2): Lin Zuo, Qiongliang Liu, Defeng Ye, Jiang Fan, and Liang Wu. Idiopathic pulmonary fibrosis: cellular heterogeneity, mechanisms, and therapeutic implications. MedComm, Dec 2025. URL: https://doi.org/10.1002/mco2.70521, doi:10.1002/mco2.70521. This article has 9 citations.

12. (zhumagaliyeva2025geneticdeterminantsof pages 1-2): Ardak Zhumagaliyeva, Joanna Chorostowska-Wynimko, and Aleksandra Jezela-Stanek. Genetic determinants of progressive pulmonary fibrosis: a comprehensive review. International Journal of Molecular Sciences, 26:11846, Dec 2025. URL: https://doi.org/10.3390/ijms262411846, doi:10.3390/ijms262411846. This article has 6 citations.

13. (zhumagaliyeva2025geneticdeterminantsof pages 7-8): Ardak Zhumagaliyeva, Joanna Chorostowska-Wynimko, and Aleksandra Jezela-Stanek. Genetic determinants of progressive pulmonary fibrosis: a comprehensive review. International Journal of Molecular Sciences, 26:11846, Dec 2025. URL: https://doi.org/10.3390/ijms262411846, doi:10.3390/ijms262411846. This article has 6 citations.

14. (cerri2024geneticriskfactors pages 2-4): Stefania Cerri, Elisa Manzini, Ottavia Nori, Lucia Pacchetti, Laura Rossi, Maria Giulia Turchiano, Anna Valeria Samarelli, Giulia Raineri, Dario Andrisani, Filippo Gozzi, Bianca Beghè, Enrico Clini, and Roberto Tonelli. Genetic risk factors in idiopathic and non-idiopathic interstitial lung disease: similarities and differences. Medicina, 60:1967, Nov 2024. URL: https://doi.org/10.3390/medicina60121967, doi:10.3390/medicina60121967. This article has 4 citations.

15. (OpenTargets Search: idiopathic pulmonary fibrosis): Open Targets Query (idiopathic pulmonary fibrosis, 32 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

16. (senhaji2026idiopathicpulmonaryfibrosis pages 4-5): Lamiyae Senhaji, Nadia Senhaji, Meriame Abbassi, Mariem Karhate, Mounia Serraj, Mohammed El Biaze, Mohamed Chakib Benjelloun, Karim Ouldim, Laila Bouguenouch, and Bouchra Amara. Idiopathic pulmonary fibrosis: a comprehensive review of risk factors, genetics, diagnosis, and therapeutic approaches. Biomedicines, 14:90, Jan 2026. URL: https://doi.org/10.3390/biomedicines14010090, doi:10.3390/biomedicines14010090. This article has 8 citations.

17. (senhaji2026idiopathicpulmonaryfibrosis pages 12-14): Lamiyae Senhaji, Nadia Senhaji, Meriame Abbassi, Mariem Karhate, Mounia Serraj, Mohammed El Biaze, Mohamed Chakib Benjelloun, Karim Ouldim, Laila Bouguenouch, and Bouchra Amara. Idiopathic pulmonary fibrosis: a comprehensive review of risk factors, genetics, diagnosis, and therapeutic approaches. Biomedicines, 14:90, Jan 2026. URL: https://doi.org/10.3390/biomedicines14010090, doi:10.3390/biomedicines14010090. This article has 8 citations.

18. (man2024acomparisonof pages 4-5): Ruzhual K Man, Amaresh Gogikar, Ankita Nanda, Lakshmi Sai Niharika Janga, Hembashima G Sambe, Mohamed Yasir, and Shivana Ramphall. A comparison of the effectiveness of nintedanib and pirfenidone in treating idiopathic pulmonary fibrosis: a systematic review. Cureus, Feb 2024. URL: https://doi.org/10.7759/cureus.54268, doi:10.7759/cureus.54268. This article has 57 citations.

19. (frohlich2024animalsinrespiratory pages 17-18): Eleonore Fröhlich. Animals in respiratory research. International Journal of Molecular Sciences, 25:2903, Mar 2024. URL: https://doi.org/10.3390/ijms25052903, doi:10.3390/ijms25052903. This article has 53 citations.

20. (drimus2025highresolutionctfindings pages 10-12): Janet Camelia Drimus, Robert Cristian Duma, Daniel Trăilă, Corina Delia Mogoșan, Diana Luminița Manolescu, and Ovidiu Fira-Mladinescu. High-resolution ct findings in interstitial lung disease associated with connective tissue diseases: differentiating patterns for clinical practice—a systematic review with meta-analysis. Journal of Clinical Medicine, 14:6164, Aug 2025. URL: https://doi.org/10.3390/jcm14176164, doi:10.3390/jcm14176164. This article has 20 citations.

21. (kreuter2021thediagnosisand pages 16-16): Michael Kreuter, Ulf Müller-Ladner, Ulrich Costabel, Danny Jonigk, and Claus Peter Heußel. The diagnosis and treatment of pulmonary fibrosis. Deutsches Arzteblatt international, Mar 2021. URL: https://doi.org/10.3238/arztebl.m2021.0018, doi:10.3238/arztebl.m2021.0018. This article has 72 citations and is from a peer-reviewed journal.

22. (liu2025anoverviewof pages 1-3): Jiahao Liu, Zihan Yi, Ting Chen, Yinghua Ying, and Yue Hu. An overview of the role of genetic factors in idiopathic pulmonary fibrosis: insights from epidemiology to prognosis. International Journal of Medical Sciences, 22:2992-3006, Jun 2025. URL: https://doi.org/10.7150/ijms.113226, doi:10.7150/ijms.113226. This article has 5 citations and is from a peer-reviewed journal.

23. (dhooria2024commonsinglenucleotide pages 12-13): Sahajal Dhooria, Riya Sharma, Amanjit Bal, Inderpaul Singh Sehgal, Dharambir Kashyap, Valliappan Muthu, Kuruswamy Thurai Prasad, Ritesh Agarwal, and Ashutosh Nath Aggarwal. Common single nucleotide polymorphisms associated with idiopathic pulmonary fibrosis: a systematic review. European Respiratory Review, 33:240018, Jul 2024. URL: https://doi.org/10.1183/16000617.0018-2024, doi:10.1183/16000617.0018-2024. This article has 9 citations and is from a peer-reviewed journal.

24. (walters2025comorbiditiesinthe pages 3-4): Tyson M. Walters, Marcus C.H. Leong, Sydney B. Montesi, Christopher J. Ryerson, and Yet H. Khor. Comorbidities in the idiopathic pulmonary fibrosis and progressive pulmonary fibrosis trial population: a systematic review and meta-analysis. European Respiratory Review, 34:240238, Jan 2025. URL: https://doi.org/10.1183/16000617.0238-2024, doi:10.1183/16000617.0238-2024. This article has 13 citations and is from a peer-reviewed journal.

25. (jiang2025exploringthecellular pages 1-2): Huanyu Jiang, Shujie Wang, Fanghui Zhong, and Tao Shen. Exploring the cellular and molecular landscape of idiopathic pulmonary fibrosis: integrative multi-omics and single-cell analysis. Biomedicines, 13:2135, Sep 2025. URL: https://doi.org/10.3390/biomedicines13092135, doi:10.3390/biomedicines13092135. This article has 4 citations.

26. (golchin2025incidenceandprevalence pages 1-2): N. Golchin, Aditya Patel, J. Scheuring, V. Wan, Kimberly Hofer, Jean-Paul Collet, B. Elpers, and T. Lesperance. Incidence and prevalence of idiopathic pulmonary fibrosis: a systematic literature review and meta-analysis. BMC Pulmonary Medicine, Aug 2025. URL: https://doi.org/10.1186/s12890-025-03836-1, doi:10.1186/s12890-025-03836-1. This article has 55 citations and is from a peer-reviewed journal.

27. (senhaji2026idiopathicpulmonaryfibrosis pages 18-20): Lamiyae Senhaji, Nadia Senhaji, Meriame Abbassi, Mariem Karhate, Mounia Serraj, Mohammed El Biaze, Mohamed Chakib Benjelloun, Karim Ouldim, Laila Bouguenouch, and Bouchra Amara. Idiopathic pulmonary fibrosis: a comprehensive review of risk factors, genetics, diagnosis, and therapeutic approaches. Biomedicines, 14:90, Jan 2026. URL: https://doi.org/10.3390/biomedicines14010090, doi:10.3390/biomedicines14010090. This article has 8 citations.

## Artifacts

- [Edison artifact artifact-00](Idiopathic_Interstitial_Pneumonia-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 9 |
| Off topic | 0 |

All extracted references resolved successfully.