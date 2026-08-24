---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-19T21:00:13.075795'
end_time: '2026-08-19T21:08:15.215738'
duration_seconds: 482.14
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Brain Abnormalities, Neurodegeneration, and Dysosteosclerosis
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 20
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 5
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Brain_Abnormalities_Neurodegeneration_and_Dysosteosclerosis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Brain Abnormalities, Neurodegeneration, and Dysosteosclerosis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Brain Abnormalities, Neurodegeneration, and Dysosteosclerosis** covering all of the
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
- **Disease Name:** Brain Abnormalities, Neurodegeneration, and Dysosteosclerosis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Brain Abnormalities, Neurodegeneration, and Dysosteosclerosis** covering all of the
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


# Brain Abnormalities, Neurodegeneration, and Dysosteosclerosis (BANDDOS): Disease-Characteristics Report

## Executive summary

BANDDOS is an exceptionally rare, usually congenital or childhood-onset **autosomal-recessive microgliopathy and skeletal dysplasia caused by biallelic loss-of-function variants in `CSF1R`**. It combines developmental brain malformations, progressive white-matter degeneration, cerebral calcification, severe neurologic disability, and osteosclerotic skeletal abnormalities. The largest disease-specific analysis, published in June 2023, aggregated only **19 patients**, so every frequency estimate remains vulnerable to ascertainment bias and incomplete reporting. Seventeen patients were homozygous and two compound heterozygous; most arose in consanguineous families. (dulski2023brainabnormalitiesneurodegeneration pages 1-2, dulski2023brainabnormalitiesneurodegeneration pages 2-5)

The central causal model is failure of CSF1R signaling in mononuclear-phagocyte lineages: deficient microglial development compromises brain development and white-matter homeostasis, while deficient osteoclast differentiation/resorption causes dysosteosclerosis. There is no approved BANDDOS-specific disease-modifying treatment. Hematopoietic stem-cell transplantation (HSCT) and microglial replacement are biologically plausible but remain extrapolations from dominant CSF1R-related leukoencephalopathy and preclinical models, not established BANDDOS therapies. (chadarevian2024therapeuticpotentialof pages 23-24, dulski2023brainabnormalitiesneurodegeneration pages 7-9, dulski2023brainabnormalitiesneurodegeneration pages 2-5)

| Domain | Finding / statistic | Ontology suggestions | Evidence type / source |
|---|---|---|---|
| Disease identity | Brain abnormalities, neurodegeneration, and dysosteosclerosis (BANDDOS); OMIM 618476; Open Targets disease entity also indexed as EFO_0010268 | MONDO: not confirmed from available sources; EFO_0010268; MeSH/Orphanet: not confirmed from available sources | Aggregated disease-level resources and literature synthesis (chitu2022modelingcsf‐1receptor pages 1-2, OpenTargets Search: brain abnormalities, neurodegeneration, and dysosteosclerosis-CSF1R, dulski2023brainabnormalitiesneurodegeneration pages 1-2) |
| Synonyms / disease framing | Pediatric-onset CSF1R-related disorder; autosomal-recessive CSF1R disorder; part of the CSF1R-related disorder continuum, distinct from dominant CSF1R-ALSP | NCIT: disease concept not confirmed; related concept suggestion: leukodystrophy / osteosclerosis terms as applicable | Review and systematic review (chitu2022modelingcsf‐1receptor pages 1-2, dulski2023brainabnormalitiesneurodegeneration pages 1-2) |
| Causal gene / inheritance | Biallelic CSF1R pathogenic variants; autosomal recessive inheritance; 17/19 homozygous and 2/19 compound heterozygous reported cases | HGNC gene: **CSF1R**; GO-linked process suggestions: microglia development, osteoclast differentiation | Human clinical genetics/systematic review (dulski2023brainabnormalitiesneurodegeneration pages 2-5, dulski2023brainabnormalitiesneurodegeneration pages 1-2) |
| Variant spectrum | 11 distinct CSF1R variants in 19 patients: splice (n=3), missense (n=3), nonsense (n=2), intronic (n=2), in-frame deletion (n=1); all disrupted the tyrosine kinase domain or led to nonsense-mediated decay | Sequence ontology suggestions: missense_variant, splice_donor/acceptor_variant, stop_gained, intron_variant, inframe_deletion | Systematic review of reported patients (dulski2023brainabnormalitiesneurodegeneration pages 1-2, dulski2023brainabnormalitiesneurodegeneration pages 9-11) |
| Onset / course | First symptoms: perinatal n=5, infancy n=2, childhood n=5, adulthood n=1; severe, usually progressive neurodevelopmental/neurodegenerative course | HPO: HP:0003577 Congenital onset; HP:0003593 Infantile onset; HP:0012758 Neurodevelopmental abnormality; HP:0002063 Rigidity | Systematic review/natural history synthesis (dulski2023brainabnormalitiesneurodegeneration pages 1-2, chitu2022modelingcsf‐1receptor pages 1-2, dulski2023brainabnormalitiesneurodegeneration pages 5-6) |
| Neurologic phenotype frequency | Speech disturbance 13/15; cognitive decline 12/14; spasticity/rigidity 12/15; hyperreflexia 11/14; pathologic reflexes 8/11; seizures 9/16; dysphagia 9/12; developmental delay 7/14; infantile hypotonia 3/11; optic nerve atrophy 2/7 | HPO suggestions: HP:0002463 Language developmental delay / speech disturbance; HP:0001263 Global developmental delay; HP:0001250 Seizure; HP:0001257 Spasticity; HP:0001347 Hyperreflexia; HP:0002015 Dysphagia; HP:0001252 Hypotonia; HP:0000648 Optic atrophy | Human case aggregation (dulski2023brainabnormalitiesneurodegeneration pages 1-2, dulski2023brainabnormalitiesneurodegeneration pages 2-5, dulski2023brainabnormalitiesneurodegeneration pages 7-9) |
| Skeletal phenotype frequency | Skeletal deformities in 13/17; phenotype described within the dysosteosclerosis–Pyle disease spectrum | HPO suggestions: HP:0000925 Abnormality of the vertebral column; HP:0000938 Osteosclerosis; HP:0010669 Metaphyseal widening; UBERON: skeleton | Human case aggregation/review (dulski2023brainabnormalitiesneurodegeneration pages 1-2, dulski2023brainabnormalitiesneurodegeneration pages 2-5) |
| Neuroimaging frequency | White-matter changes 19/19; calcifications 15/18; agenesis/abnormality of corpus callosum 12/16; ventriculomegaly 13/19; Dandy-Walker complex 7/19; cortical abnormalities 4/10 | HPO suggestions: HP:0007256 Agenesis of corpus callosum; HP:0002119 Ventriculomegaly; HP:0001272 Cerebral calcification; HP:0002500 Abnormal cerebral white matter morphology; UBERON: corpus callosum, cerebral white matter, cerebellum | Human imaging synthesis (dulski2023brainabnormalitiesneurodegeneration pages 1-2, dulski2023brainabnormalitiesneurodegeneration pages 2-5, dulski2023brainabnormalitiesneurodegeneration pages 5-6) |
| Pathology | Single autopsy showed absence of corpus callosum, absence of microglia, severe white-matter atrophy with axonal spheroids, gliosis, and numerous dystrophic calcifications | CL suggestion: microglial cell; GO/CC: myelin sheath, axon; HPO: HP:0002500 Abnormal cerebral white matter morphology | Human neuropathology (dulski2023brainabnormalitiesneurodegeneration pages 1-2, dulski2023brainabnormalitiesneurodegeneration pages 9-11) |
| Mortality / prognosis | At least 6 reported deaths among 19 compiled cases: 3 in infancy, 2 in childhood, 1 at unspecified age; prognosis generally poor with high early-life morbidity and mortality | HPO suggestion: HP:0003819 Childhood death / mortality-related annotation as local schema permits | Human case aggregation (dulski2023brainabnormalitiesneurodegeneration pages 1-2, dulski2023brainabnormalitiesneurodegeneration pages 2-5) |
| Core mechanism | Loss of CSF1R signaling impairs mononuclear-phagocyte lineage development, especially microglia and osteoclasts, linking congenital brain malformation/white-matter degeneration with dysosteosclerosis | GO suggestions: microglia development, osteoclast differentiation, receptor tyrosine kinase signaling, myeloid cell differentiation; CL: microglial cell, osteoclast | Human + model-organism convergence (dulski2023brainabnormalitiesneurodegeneration pages 7-9, chitu2022modelingcsf‐1receptor pages 1-2, chadarevian2024therapeuticpotentialof pages 23-24) |
| Cellular / tissue mechanism | Upstream: CSF1R kinase-domain dysfunction or NMD; intermediate: deficient microglia and osteoclast development/function; downstream: white-matter degeneration, calcifications, ventriculomegaly/brain malformations, osteosclerosis | GO suggestions: colony-stimulating factor receptor signaling pathway, CNS development, bone resorption; UBERON: brain, cerebral white matter, bone | Mechanistic interpretation from human pathology and models (daghagh2022homozygousmutationin pages 6-7, dulski2023brainabnormalitiesneurodegeneration pages 7-9, chitu2022modelingcsf‐1receptor pages 1-2) |
| Diagnosis | Diagnosis relies on clinical phenotype plus neuroimaging and confirmation of biallelic CSF1R variants by sequencing; reported methods include targeted NGS/panel testing and prenatal CVS-based family testing in one family | HPO panel terms above; LOINC/SNOMED not confirmed from available sources | Human case report and review (daghagh2022homozygousmutationin pages 2-4, daghagh2022homozygousmutationin pages 1-2, dulski2023brainabnormalitiesneurodegeneration pages 1-2) |
| Differential diagnosis | Should be distinguished from dominant CSF1R-ALSP and from other genetic dysosteosclerosis/osteopetrosis entities such as **SLC29A3**-related dysosteosclerosis and **TNFRSF11A**-related osteoclast-poor dysosteosclerosis | Suggested disease neighbors for curation: CSF1R-related leukoencephalopathy, dysosteosclerosis, osteopetrosis | Expert review/systematic review (dulski2023brainabnormalitiesneurodegeneration pages 1-2, chitu2022modelingcsf‐1receptor pages 1-2) |
| Recent developments (2023–2024) | 2023 systematic review expanded the cohort to 19 patients and formalized overlap with CSF1R-ALSP; 2024 translational work in CSF1R disorders advanced microglia disease modeling and microglia-replacement concepts, but not BANDDOS-specific therapy | GO/CL suggestions as above | Recent review and translational studies (dulski2023brainabnormalitiesneurodegeneration pages 1-2, chadarevian2024therapeuticpotentialof pages 23-24) |
| Treatment status | No BANDDOS-specific approved disease-modifying therapy identified. Management is supportive. Authors propose a potential “window of opportunity” to adapt therapies used in CSF1R-ALSP, especially HSCT, but direct BANDDOS efficacy data are lacking; no relevant BANDDOS interventional trial was identified in the retrieved evidence | NCIT suggestions: Supportive care; Hematopoietic Stem Cell Transplantation (as extrapolative/experimental concept) | Expert opinion/systematic review plus related-disease treatment literature (dulski2023brainabnormalitiesneurodegeneration pages 1-2, dulski2023brainabnormalitiesneurodegeneration pages 2-5) |
| Evidence base caveat | Evidence is derived from individual case reports/series aggregated into disease-level review; denominators vary by phenotype because not all features were reported in every patient | Evidence code suggestion: human clinical case report, systematic review, model organism | Methodological note from systematic review (dulski2023brainabnormalitiesneurodegeneration pages 1-2, dulski2023brainabnormalitiesneurodegeneration pages 2-5) |


*Table: This table condenses the most actionable disease-characteristic evidence for BANDDOS, emphasizing reported denominators, mechanistic interpretation, and current treatment limitations. It is useful as a compact knowledge-base population aid anchored to the available human and translational evidence.*

## 1. Disease information

**Definition.** BANDDOS—**brain abnormalities, neurodegeneration, and dysosteosclerosis**—is a syndromic CSF1R deficiency disorder characterized by congenital brain abnormalities, pediatric leukoencephalopathy/neurodegeneration, and a dysosteosclerosis–Pyle disease skeletal phenotype. It belongs to the CSF1R-related disorder continuum but is genetically and clinically distinguished from usually adult-onset, autosomal-dominant CSF1R-related leukoencephalopathy with axonal spheroids and pigmented glia (CSF1R-ALSP). (dulski2023brainabnormalitiesneurodegeneration pages 7-9, dulski2023brainabnormalitiesneurodegeneration pages 1-2)

**Identifiers and terminology.** Confirmed identifiers are **OMIM/MIM 618476** and **EFO:0010268**. Open Targets associates EFO:0010268 specifically with `CSF1R` (Ensembl ENSG00000182578), supported by five evidence records and foundational PubMed records including **PMID 30982609** and **PMID 30982608**. A disease-specific MONDO, Orphanet, MeSH, ICD-10, or ICD-11 code was not established in the retrieved evidence; generic osteopetrosis or leukodystrophy codes should not be treated as exact BANDDOS identifiers. (chitu2022modelingcsf‐1receptor pages 1-2, OpenTargets Search: brain abnormalities, neurodegeneration, and dysosteosclerosis-CSF1R)

**Synonyms/alternative framing:** BANDDOS; autosomal-recessive CSF1R disorder; biallelic CSF1R-related pediatric leukoencephalopathy; pediatric-onset CSF1R-related disorder; CSF1R-related dysosteosclerosis with neurodegeneration.

**Evidence provenance.** Available knowledge originates from individual pedigrees, case reports, imaging and one autopsy, subsequently aggregated at disease level. It is not derived from population-scale EHR cohorts. The 2023 review combined 16 previously published patients with three new patients. (dulski2023brainabnormalitiesneurodegeneration pages 1-2)

## 2. Etiology, risk, and protective factors

### Causal factor

The established cause is **biallelic germline pathogenic or likely pathogenic variation in `CSF1R`**, encoding colony-stimulating factor-1 receptor, a transmembrane receptor tyrosine kinase activated by CSF1 and IL-34. Pathogenic alleles disrupt the intracellular tyrosine-kinase domain or cause transcript degradation through nonsense-mediated decay. (dulski2023brainabnormalitiesneurodegeneration pages 7-9, dulski2023brainabnormalitiesneurodegeneration pages 1-2)

### Risk factors

* **Genetic:** two pathogenic `CSF1R` alleles; parental consanguinity increases the probability of homozygosity. Family history compatible with autosomal-recessive inheritance is important.
* **Variant severity:** truncation/NMD and profound kinase-domain disruption appear associated with early severe disease, although the cohort is too small for a validated genotype–phenotype model. (dulski2023brainabnormalitiesneurodegeneration pages 9-11)
* **Environmental, infectious, lifestyle, age, or sex risks:** none established. The observed 19-patient sex distribution—10 female, seven male, two unknown—does not establish sex-specific susceptibility. (dulski2023brainabnormalitiesneurodegeneration pages 2-5)

No validated protective variant, modifier gene, protective exposure, or gene–environment interaction has been reported. Apparent phenotypic variability may reflect residual kinase activity, background genetic modifiers, and ascertainment, but these remain hypotheses. Heterozygous relatives in one family carrying `c.2498C>T (p.Thr833Met)` were clinically unaffected, supporting recessive inheritance rather than a protective effect. (daghagh2022homozygousmutationin pages 1-2, daghagh2022homozygousmutationin pages 2-4)

## 3. Phenotypes

Reported frequencies use only patients with sufficient documentation; they are not population prevalence estimates.

* **Speech disturbance:** 13/15 (87%), often dysarthria; progressive and functionally disabling. Suggested HPO: speech abnormality, dysarthria.
* **Cognitive decline/impairment:** 12/14 (86%); developmental impairment may precede regression. HPO: cognitive impairment, developmental regression.
* **Spasticity or rigidity:** 12/15 (80%); **hyperreflexia** 11/14; **pathologic reflexes** 8/11. HPO: HP:0001257 Spasticity; HP:0001347 Hyperreflexia; pyramidal sign.
* **Seizures:** 9/16 (56%), generally childhood onset and potentially recurrent. HPO: HP:0001250 Seizure.
* **Dysphagia:** 9/12 (75%), with aspiration and nutritional implications. HPO: HP:0002015 Dysphagia.
* **Developmental delay:** 7/14 (50%); **infantile hypotonia:** 3/11; **optic atrophy:** 2/7. Suggested HPO: HP:0001263 Global developmental delay; HP:0001252 Hypotonia; HP:0000648 Optic atrophy.
* **Dysmorphism:** 7/17 (41%).
* **Skeletal deformity/dysplasia:** 13/17 (76%), spanning dysosteosclerosis and Pyle-like metaphyseal abnormalities; findings may include osteosclerosis, long-bone modeling defects, kyphosis, and optic-canal narrowing. Suggested HPO: HP:0000938 Osteosclerosis, metaphyseal widening, abnormal long-bone morphology, kyphosis. (dulski2023brainabnormalitiesneurodegeneration pages 1-2, dulski2023brainabnormalitiesneurodegeneration pages 7-9, chitu2022modelingcsf‐1receptor pages 1-2)

**Imaging phenotypes:** white-matter abnormalities 19/19; intracranial calcifications 15/18; corpus-callosum agenesis/abnormality 12/16; ventriculomegaly 13/19; Dandy–Walker complex 7/19; cortical abnormalities 4/10. Calcifications can be congenital and have a characteristic “stepping-stone” distribution. Suggested HPO: abnormal cerebral white-matter morphology, HP:0001272 cerebral calcification, HP:0007256 agenesis of corpus callosum, HP:0002119 ventriculomegaly, Dandy–Walker malformation. (dulski2023brainabnormalitiesneurodegeneration pages 1-2, dulski2023brainabnormalitiesneurodegeneration pages 5-6)

**Quality of life.** No BANDDOS-specific EQ-5D, SF-36, PROMIS, or caregiver-burden study exists. Severe motor impairment, cognitive and speech loss, seizures, dysphagia, visual impairment, skeletal deformity, and respiratory aspiration collectively imply profound dependence and caregiver burden. This is clinical inference rather than instrument-derived evidence. (dulski2023brainabnormalitiesneurodegeneration pages 7-9)

## 4. Genetic and molecular information

**Causal gene:** `CSF1R`; approved name *colony stimulating factor 1 receptor*; Ensembl ENSG00000182578. The protein has 972 amino acids and includes extracellular immunoglobulin-like domains, a transmembrane segment, juxtamembrane regulatory region, and intracellular split tyrosine-kinase domain. (dulski2023brainabnormalitiesneurodegeneration pages 7-9, OpenTargets Search: brain abnormalities, neurodegeneration, and dysosteosclerosis-CSF1R)

In the 19-patient 2023 series, 11 distinct variants comprised three splice variants, three missense variants, two nonsense variants, two intronic variants, and one in-frame deletion. Nine of 11 affected the kinase domain; the remainder caused or were predicted to cause NMD. Classifications ranged from likely pathogenic to pathogenic under ACMG/AMP interpretation. All are germline; no somatic BANDDOS mechanism is known. (dulski2023brainabnormalitiesneurodegeneration pages 9-11, dulski2023brainabnormalitiesneurodegeneration pages 1-2)

Examples include:

* `c.2498C>T (p.Thr833Met)`, homozygous, exon 19/kinase domain. It was predicted damaging, highly conserved, and segregated with disease, but lacked direct in-vitro functional validation; consequently, computational evidence should not be overstated. (daghagh2022homozygousmutationin pages 2-4, daghagh2022homozygousmutationin pages 4-6)
* `c.1754G>T (p.Gly585Val)`, homozygous in three Brazilian siblings and predicted pathogenic. (dulski2023brainabnormalitiesneurodegeneration pages 2-5)

Population allele frequencies were not reliably reported in the retrieved evidence. These causal alleles are expected to be very rare, but a numerical gnomAD frequency should be added only after transcript- and genome-build-specific database verification. No established modifier genes, epigenetic signature, recurrent chromosomal abnormality, or structural-variant mechanism is known.

## 5. Environmental information

BANDDOS is a monogenic developmental disorder. No toxin, radiation, pollution, occupational exposure, diet, smoking, alcohol use, exercise pattern, or infectious agent has been shown to cause or modify it. Infectious and aspiration complications may worsen clinical outcome but are downstream complications, not etiology. Consequently, CHEBI annotations are not appropriate for a causal exposure at present.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic lesion:** biallelic kinase-domain disruption, abnormal splicing, truncation, or NMD reduces functional CSF1R.
2. **Signaling failure:** inadequate CSF1/IL-34-induced receptor autophosphorylation impairs survival, proliferation, differentiation, and function of mononuclear-phagocyte lineages.
3. **Microglial deficiency:** failed embryonic/postnatal microglial development removes critical support for CNS morphogenesis, myelin/axon homeostasis, phagocytosis, and tissue repair.
4. **CNS consequences:** congenital malformations, ventriculomegaly, callosal agenesis and Dandy–Walker complex are followed or accompanied by white-matter atrophy, axonal spheroids, gliosis, calcification, spasticity, seizures, cognitive decline, and dysphagia.
5. **Osteoclast deficiency/dysfunction:** impaired differentiation and survival of bone-resorbing osteoclasts causes defective remodeling, osteosclerosis, abnormal metaphyseal modeling, skeletal deformity, and possible foraminal narrowing. (daghagh2022homozygousmutationin pages 6-7, dulski2023brainabnormalitiesneurodegeneration pages 7-9, chitu2022modelingcsf‐1receptor pages 1-2)

A single human autopsy showed **near-complete/complete absence of microglia**, absent corpus callosum, severe white-matter atrophy with axonal spheroids, gliosis, and numerous dystrophic calcifications—direct human tissue support for the microglial-deficiency model. (dulski2023brainabnormalitiesneurodegeneration pages 1-2, dulski2023brainabnormalitiesneurodegeneration pages 9-11)

Suggested annotations include **GO:** receptor tyrosine-kinase signaling, macrophage differentiation, microglial-cell development, osteoclast differentiation, bone resorption, CNS development, phagocytosis, myelination, and axon maintenance; **CL:** microglial cell, osteoclast, monocyte/macrophage progenitor, astrocyte, oligodendrocyte; **GO cellular components:** plasma membrane, receptor complex, cytoplasmic kinase domain, axon, and myelin sheath.

No BANDDOS-specific human transcriptomic, proteomic, metabolomic, lipidomic, spatial-transcriptomic, single-cell, or epigenomic signature has been established. Work in broader CSF1R disease suggests altered microglial and compensatory astrocytic states, but this should not be represented as directly measured BANDDOS molecular profiling. (chadarevian2024therapeuticpotentialof pages 23-24)

## 7. Anatomical structures affected

**Primary systems:** CNS and skeleton. CNS sites include bilateral cerebral/periventricular white matter, corpus callosum, corticospinal/pyramidal tracts, cerebral cortex, basal ganglia, cerebellum and posterior fossa, ventricles, and optic nerves. Skeletal involvement includes long bones, metaphyses, vertebral column, ribs/chest, skull, and optic canals. Involvement is generally bilateral/systemic rather than unilateral. (daghagh2022homozygousmutationin pages 1-2, dulski2023brainabnormalitiesneurodegeneration pages 7-9)

Suggested **UBERON** concepts: brain, cerebral white matter, corpus callosum, cerebral cortex, basal ganglion, cerebellum, ventricular system of brain, optic nerve, bone tissue, long bone, metaphysis, vertebral column, skull. At tissue/cell level, nervous tissue, white matter, myelinated axon, microglia, astrocytes, oligodendrocytes, bone, and osteoclasts are most relevant.

## 8. Temporal development

Onset was perinatal in five patients, infancy in two, childhood in five, and adulthood in one among those with adequate data. Early disease may present with congenital hydrocephalus/ventriculomegaly, hypotonia, seizures, or developmental delay; later-onset cases can first develop normally and then lose language, cognition, and motor function. (dulski2023brainabnormalitiesneurodegeneration pages 1-2, chitu2022modelingcsf‐1receptor pages 1-2)

The usual course is chronic, progressive, lifelong, and often severe. A representative `p.Thr833Met` patient had visual problems at one month, progressive cognitive decline, gait disturbance and seizures after age two, and died at nine years. No spontaneous remission is documented. Because microglia participate in prenatal brain development, the prenatal/perinatal period is likely a critical mechanistic window; whether intervention after congenital malformation can reverse deficits is unknown. (daghagh2022homozygousmutationin pages 1-2)

## 9. Inheritance and population

Inheritance is **autosomal recessive**. In the 2023 compilation, 17/19 patients were homozygous and 2/19 compound heterozygous. Consanguinity was common. Reported ancestries/geographies included Chaldean, Brazilian, Arab, Turkish, Indian, Japanese, and Native American families, indicating worldwide occurrence rather than a single endemic population. No validated founder allele, carrier frequency, prevalence per 100,000, annual incidence, penetrance estimate, anticipation, or germline-mosaicism rate is available. (dulski2023brainabnormalitiesneurodegeneration pages 2-5)

Observed sex counts—10 female, seven male, two unknown—are compatible with autosomal inheritance and do not demonstrate sex bias. For two carrier parents, the conventional per-pregnancy risks are 25% affected, 50% heterozygous carrier, and 25% unaffected/non-carrier, assuming both parental alleles are pathogenic and no unusual reproductive mechanism.

## 10. Diagnostics

### Recommended approach

1. Recognize the combination of early developmental regression/leukoencephalopathy, calcification or congenital brain malformation, and osteosclerotic/modeling abnormalities.
2. Obtain **brain MRI**, including T1/T2/FLAIR and diffusion sequences, to define white-matter loss, callosal abnormalities, ventriculomegaly, posterior-fossa and cortical malformations.
3. Obtain **noncontrast head CT**, which is more sensitive for calcification.
4. Perform a skeletal survey or targeted radiographs/CT where clinically indicated.
5. Confirm **biallelic `CSF1R` variants** by sequencing and parental segregation. WES/WGS is appropriate when phenotype is atypical; a leukodystrophy, cerebral-calcification, osteopetrosis, or skeletal-dysplasia panel should include `CSF1R`.
6. Assess swallowing/aspiration, EEG for seizures, vision/optic nerves, developmental status, mobility, nutrition, respiratory status, and orthopedic complications. (daghagh2022homozygousmutationin pages 1-2, daghagh2022homozygousmutationin pages 2-4)

Targeted NGS identified `p.Thr833Met`, and chorionic-villus sampling enabled prenatal family testing. CMA, karyotyping, FISH, mitochondrial DNA testing, and repeat-expansion testing are not first-line tests for a classic sequence-level BANDDOS presentation, although WGS can detect copy-number or noncoding alleles missed by routine panels. No validated blood, CSF, proteomic, metabolomic, or liquid-biopsy biomarker exists.

**Differential diagnosis:** dominant CSF1R-ALSP; Aicardi–Goutières/interferonopathy and congenital-infection mimics of intracranial calcification; osteopetrosis due to `TCIRG1`, `CLCN7`, `OSTM1`, `TNFSF11`, or `TNFRSF11A`; `SLC29A3`-related dysosteosclerosis; Pyle disease; Nasu–Hakola disease (`TREM2`/`TYROBP`); and other genetic leukodystrophies. Importantly, “dysosteosclerosis” is genetically heterogeneous and is not synonymous with BANDDOS. (dulski2023brainabnormalitiesneurodegeneration pages 1-2, chitu2022modelingcsf‐1receptor pages 1-2)

## 11. Outcome and prognosis

At least six deaths were documented among the 19 compiled patients: three in infancy, two in childhood, and one at an unspecified age. This incomplete, heavily censored case series cannot support formal survival curves, life expectancy, or 5-/10-year survival estimates. (dulski2023brainabnormalitiesneurodegeneration pages 1-2, dulski2023brainabnormalitiesneurodegeneration pages 2-5)

Morbidity is often profound: developmental and cognitive disability, progressive speech and motor loss, spasticity, seizures, dysphagia/aspiration, impaired vision, skeletal deformity, and dependence in activities of daily living. Established individual prognostic biomarkers do not exist. Earlier onset, severe congenital malformations, profound microglial deficiency, truncating/NMD alleles, dysphagia, and respiratory complications are plausible adverse indicators, but none has been validated in a sufficiently large cohort.

## 12. Treatment and current applications

There is **no approved or evidence-based BANDDOS-specific pharmacotherapy, gene therapy, RNA therapy, cell therapy, or surgical cure**. Clinical care is multidisciplinary and supportive:

* antiseizure medication individualized to seizure type;
* speech/communication, physical and occupational therapy;
* tone management and orthopedic surveillance;
* formal swallowing evaluation, texture modification, aspiration precautions, and enteral feeding when needed;
* respiratory care, vaccination, and prompt infection treatment;
* visual, dental, hearing, nutritional, and developmental support;
* mobility aids, pain control, and palliative-care involvement in severe disease.

Suggested **NCIT** concepts include Supportive Care, Physical Therapy, Occupational Therapy, Speech Therapy, Anticonvulsant Therapy, Enteral Nutrition, Gastrostomy, and Hematopoietic Stem Cell Transplantation; HSCT must be flagged **experimental/extrapolative for BANDDOS**.

The 2023 expert review concluded that BANDDOS and CSF1R-ALSP form a continuum and proposed a possible therapeutic window for adapting ALSP-directed therapy. However, evidence that allogeneic HSCT can stabilize dominant CSF1R-ALSP does not demonstrate efficacy in children with congenital microglial absence and established malformations. Risks include conditioning toxicity, infection, graft-versus-host disease, and uncertain donor-cell entry/repopulation of the developing brain. No relevant BANDDOS-specific interventional trial was identified. (dulski2023brainabnormalitiesneurodegeneration pages 1-2, dulski2023brainabnormalitiesneurodegeneration pages 2-5)

A major 2024 translational development was human microglia transplantation in a chimeric CSF1R-related leukoencephalopathy model. This supports cell replacement as a research direction, not current clinical care for BANDDOS. (chadarevian2024therapeuticpotentialof pages 23-24)

## 13. Prevention

There is no lifestyle, vaccine, medication, or environmental intervention that prevents the molecular disease. **Primary reproductive prevention** consists of genetic counseling, carrier testing of relatives, partner testing where appropriate, preimplantation genetic testing for monogenic disease, and prenatal diagnosis once familial variants are known. One family underwent chorionic-villus testing of a fetus. (daghagh2022homozygousmutationin pages 2-4)

**Secondary prevention** means early molecular diagnosis and surveillance for seizures, aspiration, visual compromise, respiratory disease, and skeletal complications. Population newborn screening is not established. **Tertiary prevention** includes aspiration precautions, nutrition support, contracture prevention, rehabilitation, fracture/orthopedic management, and infection prevention. Cascade testing is appropriate for adult relatives, with careful counseling that heterozygous `CSF1R` variant interpretation may depend on the specific allele and its known dominant versus recessive effect.

## 14. Other species and natural disease

No naturally occurring veterinary disease precisely equivalent to human BANDDOS was established in the retrieved literature, and there is no zoonotic or cross-species transmission. `CSF1R` function is evolutionarily conserved in mammals and fish. Mouse (**NCBI Taxon 10090**), rat (**10116**), and zebrafish (**7955**) ortholog studies reproduce central elements of CSF1R deficiency—microglial/macrophage depletion, osteoclast defects, osteopetrosis, growth/developmental abnormalities, and brain pathology. Species differ in viability, paralog structure, genetic-background sensitivity, and degree of skeletal/CNS disease, limiting direct phenotypic equivalence. (chadarevian2024therapeuticpotentialof pages 23-24, chitu2022modelingcsf‐1receptor pages 1-2)

## 15. Model organisms and advanced research platforms

**Mouse and rat:** `Csf1r` null, kinase-dead, hypomorphic, and regulatory-element mutant models demonstrate dependence of tissue macrophages, microglia, and osteoclasts on CSF1R. Phenotypic severity is strongly background-dependent, an important limitation and a potential clue to human modifiers. (chitu2022modelingcsf‐1receptor pages 1-2)

**Zebrafish:** `csf1r`-deficient models permit live developmental analysis. They show arrested macrophage development, systemic macrophage/microglial depletion, and altered astrocytic responses. Zebrafish possess duplicated receptor genes, so dosage and paralog compensation complicate translation to humans. (chadarevian2024therapeuticpotentialof pages 23-24)

**Human cellular systems:** iPSC-derived microglia, CRISPR-edited isogenic lines, cerebral organoids, and microglia–organoid coculture are relevant for testing kinase activity, survival, migration, phagocytosis, inflammatory signaling, myelin handling, and cell-replacement strategies. As of 2024, advanced iPSC work principally modeled dominant ALSP rather than biallelic BANDDOS; a dedicated patient-derived BANDDOS isogenic model remains a major unmet need.

## Recent authoritative synthesis and evidence limitations

The pivotal recent source is Dulski et al., *Orphanet Journal of Rare Diseases*, published **June 2023**, DOI: [10.1186/s13023-023-02772-9](https://doi.org/10.1186/s13023-023-02772-9). Its abstract states: **“We identified 19 patients with BANDDOS”** and concludes that the disorder has **“a devastating course with congenital brain abnormalities, developmental delay, neurological deficits, osteopetrosis, and dysmorphic features.”** (dulski2023brainabnormalitiesneurodegeneration pages 1-2)

The 2022 case report by Daghagh et al., DOI: [10.34172/bi.2022.23528](https://doi.org/10.34172/bi.2022.23528), reported a novel homozygous `p.Thr833Met` allele; its abstract explicitly notes that heterozygous relatives had no disease manifestations and that the allele lies in the functionally essential protein-tyrosine-kinase domain. (daghagh2022homozygousmutationin pages 1-2)

The 2024 transplantation study, DOI: [10.1016/j.neuron.2024.05.023](https://doi.org/10.1016/j.neuron.2024.05.023), provides high-quality preclinical support for human microglial replacement in CSF1R-related disease, but not clinical BANDDOS efficacy. (chadarevian2024therapeuticpotentialof pages 23-24)

Overall certainty is **high** for the gene–disease relationship, recessive inheritance, microglial/osteoclast mechanism, and core imaging phenotype; **moderate to low** for individual phenotype frequencies and genotype–phenotype associations; and **very low/absent** for epidemiology, quality-of-life metrics, validated biomarkers, natural-history staging, and treatment efficacy. These gaps should be represented explicitly in a disease knowledge base rather than filled by extrapolation.

References

1. (dulski2023brainabnormalitiesneurodegeneration pages 1-2): Jarosław Dulski, Josiane Souza, Mara Lúcia Santos, and Zbigniew K. Wszolek. Brain abnormalities, neurodegeneration, and dysosteosclerosis (banddos): new cases, systematic literature review, and associations with csf1r-alsp. Orphanet Journal of Rare Diseases, Jun 2023. URL: https://doi.org/10.1186/s13023-023-02772-9, doi:10.1186/s13023-023-02772-9. This article has 26 citations and is from a peer-reviewed journal.

2. (dulski2023brainabnormalitiesneurodegeneration pages 2-5): Jarosław Dulski, Josiane Souza, Mara Lúcia Santos, and Zbigniew K. Wszolek. Brain abnormalities, neurodegeneration, and dysosteosclerosis (banddos): new cases, systematic literature review, and associations with csf1r-alsp. Orphanet Journal of Rare Diseases, Jun 2023. URL: https://doi.org/10.1186/s13023-023-02772-9, doi:10.1186/s13023-023-02772-9. This article has 26 citations and is from a peer-reviewed journal.

3. (chadarevian2024therapeuticpotentialof pages 23-24): Jean Paul Chadarevian, Jonathan Hasselmann, Alina Lahian, Joia K. Capocchi, Adrian Escobar, Tau En Lim, Lauren Le, Christina Tu, Jasmine Nguyen, Sepideh Kiani Shabestari, William Carlen-Jones, Sunil Gandhi, Guojun Bu, David A. Hume, Clare Pridans, Zbigniew K. Wszolek, Robert C. Spitale, Hayk Davtyan, and Mathew Blurton-Jones. Therapeutic potential of human microglia transplantation in a chimeric model of csf1r-related leukoencephalopathy. Aug 2024. URL: https://doi.org/10.1016/j.neuron.2024.05.023, doi:10.1016/j.neuron.2024.05.023. This article has 85 citations and is from a highest quality peer-reviewed journal.

4. (dulski2023brainabnormalitiesneurodegeneration pages 7-9): Jarosław Dulski, Josiane Souza, Mara Lúcia Santos, and Zbigniew K. Wszolek. Brain abnormalities, neurodegeneration, and dysosteosclerosis (banddos): new cases, systematic literature review, and associations with csf1r-alsp. Orphanet Journal of Rare Diseases, Jun 2023. URL: https://doi.org/10.1186/s13023-023-02772-9, doi:10.1186/s13023-023-02772-9. This article has 26 citations and is from a peer-reviewed journal.

5. (chitu2022modelingcsf‐1receptor pages 1-2): Violeta Chitu, Şölen Gökhan, and E. Richard Stanley. Modeling csf‐1 receptor deficiency diseases – how close are we? Jul 2022. URL: https://doi.org/10.1111/febs.16085, doi:10.1111/febs.16085. This article has 55 citations.

6. (OpenTargets Search: brain abnormalities, neurodegeneration, and dysosteosclerosis-CSF1R): Open Targets Query (brain abnormalities, neurodegeneration, and dysosteosclerosis-CSF1R, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

7. (dulski2023brainabnormalitiesneurodegeneration pages 9-11): Jarosław Dulski, Josiane Souza, Mara Lúcia Santos, and Zbigniew K. Wszolek. Brain abnormalities, neurodegeneration, and dysosteosclerosis (banddos): new cases, systematic literature review, and associations with csf1r-alsp. Orphanet Journal of Rare Diseases, Jun 2023. URL: https://doi.org/10.1186/s13023-023-02772-9, doi:10.1186/s13023-023-02772-9. This article has 26 citations and is from a peer-reviewed journal.

8. (dulski2023brainabnormalitiesneurodegeneration pages 5-6): Jarosław Dulski, Josiane Souza, Mara Lúcia Santos, and Zbigniew K. Wszolek. Brain abnormalities, neurodegeneration, and dysosteosclerosis (banddos): new cases, systematic literature review, and associations with csf1r-alsp. Orphanet Journal of Rare Diseases, Jun 2023. URL: https://doi.org/10.1186/s13023-023-02772-9, doi:10.1186/s13023-023-02772-9. This article has 26 citations and is from a peer-reviewed journal.

9. (daghagh2022homozygousmutationin pages 6-7): Hossein Daghagh, Haniyeh Rahbar Kafshboran, Yousef Daneshmandpour, Maryam Nasiri Aghdam, Shahrzad Talebian, Jafar Nouri Nojadeh, Hamid Hamzeiy, Saskia Biskup, and Ebrahim Sakhinia. Homozygous mutation in csf1r causes brain abnormalities, neurodegeneration, and dysosteosclerosis (banddos). BioImpacts : BI, 13:183-190, Nov 2022. URL: https://doi.org/10.34172/bi.2022.23528, doi:10.34172/bi.2022.23528. This article has 7 citations.

10. (daghagh2022homozygousmutationin pages 2-4): Hossein Daghagh, Haniyeh Rahbar Kafshboran, Yousef Daneshmandpour, Maryam Nasiri Aghdam, Shahrzad Talebian, Jafar Nouri Nojadeh, Hamid Hamzeiy, Saskia Biskup, and Ebrahim Sakhinia. Homozygous mutation in csf1r causes brain abnormalities, neurodegeneration, and dysosteosclerosis (banddos). BioImpacts : BI, 13:183-190, Nov 2022. URL: https://doi.org/10.34172/bi.2022.23528, doi:10.34172/bi.2022.23528. This article has 7 citations.

11. (daghagh2022homozygousmutationin pages 1-2): Hossein Daghagh, Haniyeh Rahbar Kafshboran, Yousef Daneshmandpour, Maryam Nasiri Aghdam, Shahrzad Talebian, Jafar Nouri Nojadeh, Hamid Hamzeiy, Saskia Biskup, and Ebrahim Sakhinia. Homozygous mutation in csf1r causes brain abnormalities, neurodegeneration, and dysosteosclerosis (banddos). BioImpacts : BI, 13:183-190, Nov 2022. URL: https://doi.org/10.34172/bi.2022.23528, doi:10.34172/bi.2022.23528. This article has 7 citations.

12. (daghagh2022homozygousmutationin pages 4-6): Hossein Daghagh, Haniyeh Rahbar Kafshboran, Yousef Daneshmandpour, Maryam Nasiri Aghdam, Shahrzad Talebian, Jafar Nouri Nojadeh, Hamid Hamzeiy, Saskia Biskup, and Ebrahim Sakhinia. Homozygous mutation in csf1r causes brain abnormalities, neurodegeneration, and dysosteosclerosis (banddos). BioImpacts : BI, 13:183-190, Nov 2022. URL: https://doi.org/10.34172/bi.2022.23528, doi:10.34172/bi.2022.23528. This article has 7 citations.

## Artifacts

- [Edison artifact artifact-00](Brain_Abnormalities_Neurodegeneration_and_Dysosteosclerosis-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.