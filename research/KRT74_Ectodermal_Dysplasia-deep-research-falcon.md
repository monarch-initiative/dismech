---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-17T13:45:02.026198'
end_time: '2026-08-17T13:54:00.916543'
duration_seconds: 538.89
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: KRT74-Related Pure Hair-Nail Ectodermal Dysplasia
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 7
reference_validation:
  total_references: 1
  verified: 1
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: KRT74_Ectodermal_Dysplasia-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** KRT74-Related Pure Hair-Nail Ectodermal Dysplasia
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **KRT74-Related Pure Hair-Nail Ectodermal Dysplasia** covering all of the
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
- **Disease Name:** KRT74-Related Pure Hair-Nail Ectodermal Dysplasia
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **KRT74-Related Pure Hair-Nail Ectodermal Dysplasia** covering all of the
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


# KRT74-Related Pure Hair–Nail Ectodermal Dysplasia

## Executive summary and evidence boundary

KRT74-related pure hair–nail ectodermal dysplasia is an exceptionally rare, congenital, autosomal-recessive keratin disorder in which abnormalities are restricted principally to hair and nails. The disease-specific evidence located is a single 2014 report of one consanguineous Pakistani family containing four affected siblings. All were homozygous for **KRT74 NM_175053:c.821T>C (p.Phe274Ser)**; unaffected relatives were heterozygous or wild type. The phenotype comprised congenital hypotrichosis with sparse, brittle, shaggy hair and spoon-shaped dystrophic nails with mild micronychia and distal onycholysis. Skin, teeth, sweating, and general health were reported as normal. Consequently, frequencies such as “4/4” below describe this ascertainment family and must not be interpreted as population estimates. (raykova2014autosomalrecessivetransmission pages 4-5, raykova2014autosomalrecessivetransmission pages 1-2, raykova2014autosomalrecessivetransmission pages 2-4)

No additional disease-specific primary study from 2023–2024, natural-history cohort, validated therapy, or relevant registered clinical trial was identified. The absence of recent publications is itself an important result: current understanding still rests primarily on the 2014 discovery paper.

## 1. Disease information

**Definition.** Pure hair–nail ectodermal dysplasia (PHNED) denotes hereditary disorders affecting hair and nails without the dental, sweat-gland, or broader systemic abnormalities typical of many ectodermal dysplasias. The KRT74-related subtype is the recessive phenotype caused by biallelic KRT74 dysfunction. It is allelic but clinically distinct from heterozygous KRT74-associated autosomal-dominant woolly hair/hypotrichosis, in which nail disease is generally absent. (raykova2014autosomalrecessivetransmission pages 5-6, raykova2014autosomalrecessivetransmission pages 1-2)

**Identifiers and terminology.** The discovery paper assigns **OMIM 614929** to the KRT74-associated recessive PHNED entity. Useful names include “KRT74-related pure hair and nail ectodermal dysplasia,” “autosomal recessive pure hair–nail ectodermal dysplasia,” and “hair and nail ectodermal dysplasia caused by KRT74.” A disease-specific MONDO, Orphanet, MeSH, ICD-10, or ICD-11 identifier could not be verified from the retrieved primary literature; these should not be inferred from broader ectodermal-dysplasia records. Generic ICD coding would be less specific than the molecular diagnosis. (raykova2014autosomalrecessivetransmission pages 1-2)

This report synthesizes **aggregated publication-level evidence**, not individual EHR records. However, the aggregate itself derives from four individually described relatives in one pedigree.

**Key primary source:** Raykova et al., *PLoS ONE*, April 2014, DOI/URL: https://doi.org/10.1371/journal.pone.0093607. A directly supporting abstract statement is: “Whole exome sequencing of affected individuals revealed homozygosity for a rare c.821T>C variant (p.Phe274Ser) in the KRT74 gene that segregates AR PHNED in the family.” (raykova2014autosomalrecessivetransmission pages 1-2)

## 2. Etiology, risk, protective factors, and environment

The primary cause is **germline biallelic KRT74 variation**. In the reported family, consanguinity increased the probability that both parents transmitted the same rare allele; it is a reproductive/genetic risk context, not a biological cause independent of the variant. Each child of two heterozygous carriers has the standard autosomal-recessive theoretical probabilities of 25% affected, 50% carrier, and 25% unaffected/non-carrier per pregnancy.

The only established disease allele is p.Phe274Ser in the disease-specific evidence retrieved. Family history and parental relatedness are therefore the principal recognizable risk indicators. Sex, age, diet, smoking, occupation, toxins, infection, and other exposures have not been shown to alter occurrence. There are no established susceptibility loci, modifier genes, protective variants, protective environmental factors, or gene–environment interactions. Hair grooming and mechanical/chemical trauma may plausibly worsen breakage or onycholysis but do not cause the congenital disorder; this is supportive-care inference rather than KRT74-specific trial evidence.

The allele was reported at approximately 0.0002 in the historical Exome Variant Server, absent from 350 in-house, 200 Swedish, and 200 Pakistani control exomes, and not observed homozygously. These are older databases and must be rechecked against current gnomAD before clinical reporting. The paper’s approximate “one per million” calculation was Hardy–Weinberg extrapolation from that allele frequency, not measured prevalence. (raykova2014autosomalrecessivetransmission pages 5-6, raykova2014autosomalrecessivetransmission pages 2-4)

## 3. Phenotypes

All reported manifestations were congenital. No standardized severity scale, longitudinal progression measurement, patient-reported outcome, EQ-5D, SF-36, or disease-specific quality-of-life study was found.

* **Hypotrichosis/sparse hair:** 4/4 reported siblings; scalp hair was sparse, brittle, and shaggy, with eyebrow and eyelash involvement. Suggested HPO: **HP:0001006 Hypotrichosis**, plus current HPO terms for sparse scalp hair, brittle hair, sparse eyebrows, and sparse eyelashes after ontology validation. The principal impact is likely cosmetic, grooming-related, and psychosocial, but this has not been quantified in KRT74-PHNED. (raykova2014autosomalrecessivetransmission pages 4-5, raykova2014autosomalrecessivetransmission pages 1-2, raykova2014autosomalrecessivetransmission pages 2-4)
* **Nail dystrophy/koilonychia-like spooning:** 4/4; nails were dystrophic and spoon-shaped. Suggested HPO: onychodystrophy and koilonychia terms, with current IDs validated before ingestion. (raykova2014autosomalrecessivetransmission pages 4-5, raykova2014autosomalrecessivetransmission pages 2-4)
* **Distal onycholysis:** 4/4 in the family description. Suggested HPO: **HP:0012203 Onycholysis**. It can interfere with fine manipulation and predispose to traumatic separation, although disease-specific disability data are unavailable. (raykova2014autosomalrecessivetransmission pages 1-2, raykova2014autosomalrecessivetransmission pages 2-4)
* **Micronychia:** mild in affected relatives. Suggested HPO: **HP:0001813 Micronychia**. (raykova2014autosomalrecessivetransmission pages 4-5, raykova2014autosomalrecessivetransmission pages 1-2)
* **Important negative findings:** normal skin, dentition, and sweating; affected individuals were otherwise healthy. These negatives help distinguish “pure” hair–nail disease from hypohidrotic or multisystem ectodermal dysplasias. (raykova2014autosomalrecessivetransmission pages 1-2, raykova2014autosomalrecessivetransmission pages 2-4)

Frequency estimates are not generalizable because n=4 and all affected persons were siblings. Behavioral, neurodevelopmental, metabolic, hematologic, and immune abnormalities have not been reported.

## 4. Genetic and molecular information

**Gene.** **KRT74** encodes keratin 74, a type II basic keratin in the chromosome 12 keratin cluster. The disease paper used transcript **NM_175053**. Gene-level HGNC and current NCBI Gene identifiers should be imported directly from HGNC/NCBI rather than inferred from the paper.

**Variant.** The reported allele is **NM_175053:c.821T>C; p.(Phe274Ser), rs147962513**, a germline missense substitution in exon 4 and the conserved coil 1B rod domain. Four affected siblings were homozygous; parents and unaffected siblings were carriers or wild type. Phe274 was completely conserved among species with available KRT74 sequences and in 25 of 26 human type II keratins. Historical computational prediction called it probably damaging. (raykova2014autosomalrecessivetransmission pages 4-5, raykova2014autosomalrecessivetransmission pages 2-4)

The segregation, rarity, conservation, phenotype specificity, and loss of keratin-74 immunostaining constitute strong case-level pathogenic evidence. Nevertheless, a current ClinVar assertion and a formal contemporary ACMG/AMP classification were not established in the retrieved evidence; a diagnostic laboratory should independently classify the variant using current population and functional data.

**Functional consequence.** Replacement of hydrophobic phenylalanine by polar serine is predicted to impair long-range keratin dimerization and intermediate-filament stability. Patient hair follicles and epidermis lacked detectable keratin-74 staining, supporting protein loss or degradation. This is consistent with loss of function, but no direct filament-assembly assay established the exact biochemical step. (raykova2014autosomalrecessivetransmission pages 5-6, raykova2014autosomalrecessivetransmission pages 2-4, raykova2014autosomalrecessivetransmission pages 4-5)

No validated modifier genes, epigenetic disease signature, pathogenic structural rearrangement, somatic event, methylation abnormality, or chromosomal anomaly has been reported.

## 5. Environmental information

No toxin, radiation, pollutant, occupation, lifestyle behavior, diet, medication, or infectious agent is known to cause or trigger KRT74-PHNED. It is not infectious and has no zoonotic transmission. Environmental factors may affect the condition of already fragile hair or nails but do not alter the underlying genotype. There are no disease-specific CTD-style chemical associations supported by human evidence.

## 6. Mechanism and pathophysiology

The best-supported causal chain is:

**biallelic p.Phe274Ser → disruption of conserved coil 1B keratin interactions → impaired dimer/intermediate-filament stability and loss of detectable keratin-74 → defective mechanical differentiation/support in the hair-follicle inner root sheath and nail-forming epithelia → malformed, fragile hair shafts and dystrophic small nails with onycholysis.** (raykova2014autosomalrecessivetransmission pages 5-6, raykova2014autosomalrecessivetransmission pages 2-4, raykova2014autosomalrecessivetransmission pages 4-5)

The **upstream event** is the germline missense variant. The **proximal molecular defect** is impaired keratin assembly/protein stability. **Downstream effects** are appendage-specific structural failure and the clinical hair/nail phenotype. Unlike EDA–NF-κB ectodermal dysplasias, no evidence implicates Wnt, MAPK, mTOR, PI3K–AKT, inflammation, autoimmunity, or metabolic deficiency as the primary pathway here.

Suggested GO annotations include **keratin filament**, **intermediate filament organization**, **keratinization**, **epithelial cell differentiation**, and **structural constituent of cytoskeleton**; exact current IDs should be validated through GO. Suggested cell types are hair-follicle inner-root-sheath keratinocytes and nail-matrix/nail-bed keratinocytes; corresponding CL terms require validation because specialized appendage keratinocytes may not have granular standalone CL entries.

No disease-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, multi-omic, CRISPR-screen, RNAi-screen, or patient-derived organoid/iPSC study was found. The immunohistochemistry is tissue-level protein-localization evidence, not comprehensive proteomics.

## 7. Anatomical structures affected

At organ/system level, involvement is confined to the **integumentary system**, principally hair follicles and nail units. Sites described include scalp hair, eyebrows, eyelashes, fingernails, and toenails. No lateralization or consistent asymmetry was reported. (raykova2014autosomalrecessivetransmission pages 1-2, raykova2014autosomalrecessivetransmission pages 2-4)

At tissue level, keratin-74 is expressed in the **hair-follicle inner root sheath**, **nail matrix**, **nail bed**, and **hyponychium**. Mouse distal-digit immunohistochemistry supported the nail localization, while normal human follicles supported hair localization. Suggested UBERON concepts are hair follicle, inner root sheath, nail, nail matrix, nail bed, and hyponychium, with exact IDs validated before entry. (raykova2014autosomalrecessivetransmission pages 5-6, raykova2014autosomalrecessivetransmission pages 4-5)

At subcellular level, the relevant structure is the cytoplasmic keratin intermediate-filament network. “Keratin filament” and “intermediate filament cytoskeleton” are appropriate GO cellular-component concepts. No primary nuclear, mitochondrial, lysosomal, ER, vascular, neural, or immune compartment abnormality has been demonstrated.

## 8. Temporal development

Onset was **congenital/present from birth**. The disorder should be considered chronic and lifelong because it reflects formation of repeatedly regenerated appendages from genetically altered epithelia. However, the publication did not provide serial measurements, defined stages, progression rates, remission, age-dependent penetrance, or critical treatment windows. (raykova2014autosomalrecessivetransmission pages 1-2, raykova2014autosomalrecessivetransmission pages 2-4)

There is no evidence for episodic attacks, spontaneous remission, relapsing–remitting behavior, or genetic anticipation. The developmental period of hair-shaft and nail-plate formation is mechanistically relevant, but no intervention window has been tested.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. Within the reported pedigree, segregation was consistent and heterozygous relatives had normal hair and nails, suggesting complete penetrance for homozygotes in that family and no phenotype from this allele in heterozygotes. Population-wide penetrance and expressivity remain unknown. (raykova2014autosomalrecessivetransmission pages 5-6, raykova2014autosomalrecessivetransmission pages 4-5)

The only disease family reported in the retrieved evidence was consanguineous and Pakistani. This does not establish ethnic susceptibility, geographic endemicity, or a founder effect. Both sexes can theoretically be affected equally; no valid sex ratio can be calculated from four siblings. Incidence, measured prevalence, carrier frequency, mosaicism rate, and age distribution are unknown. Germline mosaicism has not been reported but cannot be excluded generically.

The historical allele-frequency extrapolation of approximately one affected person per million is not epidemiologic observation and assumes random mating, equilibrium, full penetrance, and that p.Phe274Ser alone represents disease burden. It is particularly unreliable in consanguineous populations. (raykova2014autosomalrecessivetransmission pages 5-6)

## 10. Diagnostics

Diagnosis begins with congenital hypotrichosis plus nail dystrophy, careful examination of scalp hair, eyebrows, eyelashes, all nails, skin, teeth, and sweating, and a three-generation pedigree. Trichoscopy and light microscopy may document shaft fragility or shape but no KRT74-specific pattern has been validated. Routine blood chemistry, imaging, electrophysiology, and organ-function testing are not diagnostic.

**Genetic testing strategy:**

1. Use a hereditary hypotrichosis/ectodermal-dysplasia panel containing **KRT74, KRT85, HOXC13**, and phenotype-overlap genes, or exome sequencing when the phenotype is nonspecific.
2. Confirm candidate variants and phase/segregation in parents and relatives; diagnosis requires two pathogenic/likely pathogenic KRT74 alleles in trans for this recessive entity.
3. WGS is reasonable after negative panel/WES testing to assess poorly covered, intronic, or structural variants, but its incremental yield is unknown.
4. Single-gene KRT74 sequencing is efficient when phenotype and family structure are strongly suggestive.
5. CMA, karyotyping, FISH, mitochondrial sequencing, repeat-expansion testing, RNA sequencing, proteomics, metabolomics, epigenomics, and liquid biopsy are not first-line tests absent additional indications.

The discovery family was resolved by whole-exome sequencing followed by segregation testing. Skin/hair biopsy and keratin-74 immunohistochemistry demonstrated loss of staining, but IHC is research-supportive rather than a standardized clinical biomarker. (raykova2014autosomalrecessivetransmission pages 1-2, raykova2014autosomalrecessivetransmission pages 2-4)

**Differential diagnosis:** KRT85- and HOXC13-related PHNED; dominant KRT74 woolly hair/hypotrichosis; other isolated woolly-hair/hypotrichosis genes; nonsyndromic nail dysplasias; and syndromic ectodermal dysplasias. Normal teeth and sweating favor pure PHNED. Dominant KRT74 disease is distinguished by vertical transmission/heterozygosity and predominantly hair-only disease, whereas the p.Phe274Ser recessive phenotype includes nails. (raykova2014autosomalrecessivetransmission pages 5-6, raykova2014autosomalrecessivetransmission pages 1-2)

No consensus clinical criteria or population/newborn screening program exists. Cascade testing of relatives is appropriate once a familial variant is established.

## 11. Outcome and prognosis

No deaths, systemic complications, or shortened survival were reported; affected relatives were otherwise healthy. The available phenotype therefore suggests normal life expectancy, but this is an inference from four individuals rather than survival analysis. (raykova2014autosomalrecessivetransmission pages 1-2, raykova2014autosomalrecessivetransmission pages 2-4)

Expected morbidity is primarily cosmetic/psychosocial and functional inconvenience from hair fragility and dystrophic nails. Possible secondary issues include traumatic nail separation and local infection, but no complication rate has been measured. There are no 5- or 10-year survival statistics, mortality rates, disability scores, quality-of-life instruments, prognostic models, or prognostic biomarkers. Genotype may predict phenotype broadly—biallelic p.Phe274Ser produced hair+nail disease, while other heterozygous KRT74 alleles cause dominant hair disease—but robust variant-specific prognostication is impossible. (raykova2014autosomalrecessivetransmission pages 5-6, raykova2014autosomalrecessivetransmission pages 4-5)

## 12. Treatment and applications

There is no disease-modifying or approved KRT74-specific therapy. Current implementation is supportive:

* gentle hair care; avoidance of traction, harsh chemicals, excessive heat, and traumatic grooming;
* cosmetic hair replacement or camouflage where desired;
* regular conservative nail care, protection from trauma and prolonged moisture, and treatment of proven bacterial/fungal superinfection according to standard dermatologic practice;
* dermatology follow-up and psychosocial support;
* genetic counseling and genotype-informed family testing.

Potential NCIt intervention concepts include **Genetic Counseling**, **Genetic Testing**, **Supportive Care**, and prosthetic/cosmetic hair replacement terms, subject to current NCIt validation. No disease-specific drug, pharmacogenomic guidance, surgery, rehabilitation protocol, gene therapy, cell therapy, ASO/siRNA/mRNA treatment, CRISPR intervention, immunotherapy, or combination regimen has been evaluated. Minoxidil cannot be recommended as a mechanism-correcting therapy because this is a structural keratin defect, and no KRT74-PHNED response data were found.

The ClinicalTrials.gov search produced no relevant KRT74/PHNED study; therefore, there are no applicable NCT identifiers, response rates, or adverse-event datasets.

## 13. Prevention

The phenotype cannot presently be prevented in an individual who inherits two causal alleles. There is no vaccine, medication prophylaxis, lifestyle program, or environmental intervention.

Primary reproductive prevention options after molecular confirmation include carrier testing, partner testing, genetic counseling, preimplantation genetic testing for monogenic disease, and targeted prenatal diagnosis, subject to local law and family preferences. Secondary prevention consists of early molecular diagnosis and cascade testing, avoiding repeated diagnostic procedures. Tertiary prevention consists of reducing hair/nail trauma and promptly managing complications. Population-wide or newborn screening is not justified by current evidence and no public-health program exists.

## 14. Other species and natural disease

The 2014 study used **mouse (*Mus musculus*; NCBI Taxonomy 10090)** nail tissues for normal keratin-74 localization in nail matrix, bed, and hyponychium. This was comparative expression evidence, not a naturally affected animal or a disease model. (raykova2014autosomalrecessivetransmission pages 5-6, raykova2014autosomalrecessivetransmission pages 4-5)

KRT74 orthologues and hair keratin biology are evolutionarily conserved across mammals, consistent with the cross-species conservation of Phe274. Nevertheless, no naturally occurring veterinary disorder that exactly reproduces biallelic human KRT74 hair–nail dysplasia was established in the retrieved evidence. There is no zoonotic or cross-species transmission because this is a germline structural-protein disorder.

## 15. Model organisms

No Krt74 p.Phe274Ser knock-in, Krt74-null animal, patient-derived organoid, iPSC model, or validated cellular filament-assembly model specific to this disease was identified. The available experimental systems are limited to human patient tissue IHC and normal mouse distal-digit IHC. Their strength is anatomically concordant localization; their limitation is that they do not directly quantify filament assembly, nail biomechanics, longitudinal progression, or therapeutic rescue. (raykova2014autosomalrecessivetransmission pages 5-6, raykova2014autosomalrecessivetransmission pages 2-4)

A disease-specific knock-in mouse or differentiated hair-follicle/nail keratinocyte model would be valuable for testing protein stability, keratin-pair interactions, filament architecture, appendage biomechanics, and allele-specific rescue.

## Ontology-ready summary

The following table separates direct evidence from candidate ontology mappings that require validation against current releases.

| domain | finding | suggested ontology term(s)/identifier(s) | evidence strength/limitations |
|---|---|---|---|
| Disease entity | KRT74-related pure hair-nail ectodermal dysplasia; autosomal recessive hair/nail ectodermal dysplasia caused by biallelic KRT74 variation; reported as PHNED/ectodermal dysplasia hair and nail type | OMIM: 614929; MONDO: candidate requiring ontology validation; synonym candidates: pure hair and nail ectodermal dysplasia, ectodermal dysplasia hair/nail type, KRT74-related PHNED | Strong for existence of a distinct KRT74-associated entity, but evidence is limited to n=4 affected siblings from one consanguineous Pakistani family (raykova2014autosomalrecessivetransmission pages 1-2, raykova2014autosomalrecessivetransmission pages 2-4) |
| Causal gene/protein | KRT74 encodes keratin-74, a type II keratin involved in hair/nail epithelial appendages | KRT74; candidate HGNC/NCBI identifiers require ontology validation; protein: Keratin-74 | Strong gene-disease association within the single family; broader literature supports KRT74 as a hair keratin, but disease-specific evidence remains sparse (raykova2014autosomalrecessivetransmission pages 2-4, raykova2014autosomalrecessivetransmission pages 1-2, raykova2014autosomalrecessivetransmission pages 6-7) |
| Inheritance | Autosomal recessive segregation with unaffected heterozygous parents/siblings and homozygous affected siblings | HP:0000007 Autosomal recessive inheritance | Strong segregation evidence in one pedigree only; penetrance beyond this family is unknown (raykova2014autosomalrecessivetransmission pages 4-5, raykova2014autosomalrecessivetransmission pages 2-4) |
| Pathogenic variant | Homozygous NM_175053:c.821T>C, p.Phe274Ser in KRT74; missense in coil 1B domain; rs147962513 reported | HGVS: NM_175053:c.821T>C; p.Phe274Ser; dbSNP: rs147962513; ACMG class: candidate pathogenic/likely pathogenic requiring current database re-validation | Strong family-level causal evidence plus conservation and IHC support; formal contemporary ACMG/ClinVar status was not established here and should be rechecked (raykova2014autosomalrecessivetransmission pages 5-6, raykova2014autosomalrecessivetransmission pages 2-4) |
| Onset | Hair and nail abnormalities present since birth; congenital onset | HP:0003577 Congenital onset; candidate HPO term requiring validation if more specific onset term desired | Strong within reported family; no longitudinal natural history cohorts (raykova2014autosomalrecessivetransmission pages 1-2, raykova2014autosomalrecessivetransmission pages 2-4) |
| Hair phenotype | Congenital hypotrichosis with sparse, brittle, shaggy scalp hair; involvement of eyebrows and eyelashes | HP:0001006 Hypotrichosis; candidate HPO terms requiring validation: sparse scalp hair, brittle hair, abnormal eyebrow hair, sparse eyelashes | Strong descriptive evidence in n=4; exact standardized HPO mapping for “shaggy” hair and eyebrow/eyelash involvement should be ontology-validated (raykova2014autosomalrecessivetransmission pages 4-5, raykova2014autosomalrecessivetransmission pages 1-2, raykova2014autosomalrecessivetransmission pages 2-4) |
| Nail phenotype | Spoon-shaped dystrophic nails with onychodystrophy, distal onycholysis, and mild micronychia | HP:0012203 Onycholysis; HP:0001813 Micronychia; candidate HPO terms requiring validation: spoon-shaped nails, nail dystrophy/onychodystrophy | Strong descriptive evidence in n=4; some nail morphology terms need validation against current HPO nomenclature (raykova2014autosomalrecessivetransmission pages 4-5, raykova2014autosomalrecessivetransmission pages 1-2, raykova2014autosomalrecessivetransmission pages 2-4) |
| Negative ectodermal/systemic findings | Otherwise healthy; no skin abnormalities; dentition and sweating reported as normal | Candidate HPO negatives requiring validation: normal skin morphology, normal dentition, normal sweating | Useful for differential diagnosis, but negative findings are only from the single family report and were not deeply phenotyped by standardized instruments (raykova2014autosomalrecessivetransmission pages 1-2, raykova2014autosomalrecessivetransmission pages 2-4) |
| Primary anatomy | Hair follicle and nail unit are the principal affected structures | UBERON candidate terms requiring validation: hair follicle, nail unit, scalp hair, eyebrow, eyelash | Strong clinicopathologic concordance; disease appears appendage-restricted in available evidence (raykova2014autosomalrecessivetransmission pages 1-2, raykova2014autosomalrecessivetransmission pages 2-4) |
| Tissue/cell localization | Keratin-74 expression demonstrated in hair follicle inner root sheath and in nail matrix, nail bed, and hyponychium | UBERON/CL candidates requiring validation: hair follicle inner root sheath, nail matrix, nail bed, hyponychium; CL candidate: hair follicle keratinocyte | Strong localization evidence by immunohistochemistry, including mouse distal digit/nail tissues and normal human hair follicles; cell ontology mapping needs validation (raykova2014autosomalrecessivetransmission pages 5-6, raykova2014autosomalrecessivetransmission pages 4-5, raykova2014autosomalrecessivetransmission pages 2-4) |
| Molecular function/pathway | Conserved Phe274 in coil 1B domain is predicted to be required for keratin long-range dimerization and intermediate filament stability; disease mechanism consistent with keratinization/intermediate filament defect | GO candidate terms requiring validation: intermediate filament organization, keratin filament, keratinization, structural constituent of cytoskeleton | Moderate mechanistic strength: supported by domain/conservation analysis and loss of staining, but no direct biochemical filament-assembly assay in patient cells was reported (raykova2014autosomalrecessivetransmission pages 5-6, raykova2014autosomalrecessivetransmission pages 2-4, raykova2014autosomalrecessivetransmission pages 4-5) |
| Functional consequence | Affected hair follicles/epidermis stained negative for keratin-74, supporting loss of function/protein degradation | GO candidate: loss of protein expression requiring validation | Moderate evidence from IHC; absence of signal supports loss of function but does not fully resolve whether degradation, failed translation, or epitope loss predominates (raykova2014autosomalrecessivetransmission pages 5-6, raykova2014autosomalrecessivetransmission pages 2-4) |
| Population data | Variant reported as extremely rare; present heterozygously at very low frequency in older population resources and not observed homozygously | Population resource annotation candidates requiring re-validation in current gnomAD/dbSNP | Weak-to-moderate because frequency estimates cited are from older EVS/dbSNP-era resources; modern population frequency should be rechecked (raykova2014autosomalrecessivetransmission pages 5-6, raykova2014autosomalrecessivetransmission pages 2-4) |
| Differential diagnosis | Distinguish from KRT85-related PHNED, HOXC13-related PHNED, and dominant KRT74-associated woolly hair/hypotrichosis without nail disease | OMIM candidates requiring validation for differential entities; HPO pattern: hair+nail ectodermal dysplasia versus isolated woolly hair/hypotrichosis | Strong conceptual differential, but comparative phenotypic granularity is limited by few cases and literature availability (raykova2014autosomalrecessivetransmission pages 5-6, raykova2014autosomalrecessivetransmission pages 1-2, raykova2014autosomalrecessivetransmission pages 4-5) |
| Evidence scope | Human evidence base consists of one published family with four affected full siblings; no dedicated clinical trial, biomarker study, or natural history cohort identified | Evidence annotation candidate: single-family case series | Critical limitation for all downstream assertions; ontology entry should flag very low case count and need for replication (raykova2014autosomalrecessivetransmission pages 4-5, raykova2014autosomalrecessivetransmission pages 1-2, raykova2014autosomalrecessivetransmission pages 2-4) |


*Table: This table summarizes ontology-ready disease, phenotype, anatomy, and mechanism annotations for KRT74-related pure hair-nail ectodermal dysplasia. It emphasizes the narrow evidence base: four affected individuals from a single family, with several ontology IDs marked as candidates requiring validation.*

## Evidence assessment and current research priorities

The strongest evidence is **human genetic segregation plus tissue-level IHC**: four homozygous affected siblings, unaffected heterozygotes, an evolutionarily conserved rod-domain substitution, extreme rarity, and loss of detectable protein in relevant tissue. The authors summarized the central mechanistic conclusion as: “The transition alters the highly conserved Phe274 residue in the coil 1B domain required for long-range dimerization of keratins, suggesting that the mutation compromises the stability of intermediate filaments.” (raykova2014autosomalrecessivetransmission pages 5-6, raykova2014autosomalrecessivetransmission pages 1-2)

Major unresolved questions are whether additional biallelic KRT74 alleles produce the same phenotype, the true penetrance and prevalence, the natural history of nail and hair changes, current population frequency of p.Phe274Ser, the exact keratin-binding/filament defect, quality-of-life burden, and whether appendage-targeted gene or RNA correction is technically feasible. For a knowledge base, the disease should therefore be represented as a valid but **very-low-case-count gene–disease entity**, with all frequency and prognostic assertions tagged as limited or unknown.

References

1. (raykova2014autosomalrecessivetransmission pages 4-5): Doroteya Raykova, Joakim Klar, Aysha Azhar, Tahir Naeem Khan, Naveed Altaf Malik, Muhammad Iqbal, Muhammad Tariq, Shahid Mahmood Baig, and Niklas Dahl. Autosomal recessive transmission of a rare krt74 variant causes hair and nail ectodermal dysplasia: allelism with dominant woolly hair/hypotrichosis. PLoS ONE, 9:e93607, Apr 2014. URL: https://doi.org/10.1371/journal.pone.0093607, doi:10.1371/journal.pone.0093607. This article has 20 citations and is from a peer-reviewed journal.

2. (raykova2014autosomalrecessivetransmission pages 1-2): Doroteya Raykova, Joakim Klar, Aysha Azhar, Tahir Naeem Khan, Naveed Altaf Malik, Muhammad Iqbal, Muhammad Tariq, Shahid Mahmood Baig, and Niklas Dahl. Autosomal recessive transmission of a rare krt74 variant causes hair and nail ectodermal dysplasia: allelism with dominant woolly hair/hypotrichosis. PLoS ONE, 9:e93607, Apr 2014. URL: https://doi.org/10.1371/journal.pone.0093607, doi:10.1371/journal.pone.0093607. This article has 20 citations and is from a peer-reviewed journal.

3. (raykova2014autosomalrecessivetransmission pages 2-4): Doroteya Raykova, Joakim Klar, Aysha Azhar, Tahir Naeem Khan, Naveed Altaf Malik, Muhammad Iqbal, Muhammad Tariq, Shahid Mahmood Baig, and Niklas Dahl. Autosomal recessive transmission of a rare krt74 variant causes hair and nail ectodermal dysplasia: allelism with dominant woolly hair/hypotrichosis. PLoS ONE, 9:e93607, Apr 2014. URL: https://doi.org/10.1371/journal.pone.0093607, doi:10.1371/journal.pone.0093607. This article has 20 citations and is from a peer-reviewed journal.

4. (raykova2014autosomalrecessivetransmission pages 5-6): Doroteya Raykova, Joakim Klar, Aysha Azhar, Tahir Naeem Khan, Naveed Altaf Malik, Muhammad Iqbal, Muhammad Tariq, Shahid Mahmood Baig, and Niklas Dahl. Autosomal recessive transmission of a rare krt74 variant causes hair and nail ectodermal dysplasia: allelism with dominant woolly hair/hypotrichosis. PLoS ONE, 9:e93607, Apr 2014. URL: https://doi.org/10.1371/journal.pone.0093607, doi:10.1371/journal.pone.0093607. This article has 20 citations and is from a peer-reviewed journal.

5. (raykova2014autosomalrecessivetransmission pages 6-7): Doroteya Raykova, Joakim Klar, Aysha Azhar, Tahir Naeem Khan, Naveed Altaf Malik, Muhammad Iqbal, Muhammad Tariq, Shahid Mahmood Baig, and Niklas Dahl. Autosomal recessive transmission of a rare krt74 variant causes hair and nail ectodermal dysplasia: allelism with dominant woolly hair/hypotrichosis. PLoS ONE, 9:e93607, Apr 2014. URL: https://doi.org/10.1371/journal.pone.0093607, doi:10.1371/journal.pone.0093607. This article has 20 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](KRT74_Ectodermal_Dysplasia-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 1 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |

All extracted references resolved successfully.