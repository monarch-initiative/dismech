---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-17T13:44:33.888336'
end_time: '2026-08-17T13:50:46.970072'
duration_seconds: 373.08
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: HOXC13-Related Pure Hair-Nail Ectodermal Dysplasia
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 19
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: HOXC13_Ectodermal_Dysplasia-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** HOXC13-Related Pure Hair-Nail Ectodermal Dysplasia
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **HOXC13-Related Pure Hair-Nail Ectodermal Dysplasia** covering all of the
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
- **Disease Name:** HOXC13-Related Pure Hair-Nail Ectodermal Dysplasia
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **HOXC13-Related Pure Hair-Nail Ectodermal Dysplasia** covering all of the
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


# HOXC13-Related Pure Hair–Nail Ectodermal Dysplasia

## Executive summary

HOXC13-related pure hair–nail ectodermal dysplasia is an ultra-rare, congenital, usually autosomal-recessive genodermatosis in which biallelic **HOXC13** variants disrupt terminal differentiation of hair follicles and nail-forming epithelium. The characteristic combination is generalized hypotrichosis or complete alopecia plus dystrophy/hypoplasia of all fingernails and toenails, with teeth, sweating, skeleton, and neurodevelopment generally spared. This restricted distribution distinguishes the disorder from multisystem ectodermal dysplasias. The evidence base consists chiefly of individual families and experimental models; there are no reliable prevalence estimates, formal clinical guidelines, disease-modifying treatments, or registered disease-specific interventional trials in the retrieved evidence. (lin2012lossoffunctionmutationsin pages 1-2, khan2017anovelmutation pages 3-5, li2017anovelhomozygous pages 1-3)

| domain | best-supported finding | evidence type | key citation metadata (author/year/PMID/DOI) | evidence limitation |
|---|---|---|---|---|
| Disease identity | HOXC13-related pure hair-nail ectodermal dysplasia corresponds to ectodermal dysplasia 9 (ECTD9/PHNED), a congenital disorder primarily affecting hair and nails. (lin2012lossoffunctionmutationsin pages 1-2, khan2017anovelmutation pages 3-5, li2017anovelhomozygous pages 1-3) | Human clinical genetics | Lin et al., 2012, PMID 23063621, DOI: 10.1016/j.ajhg.2012.08.029; Khan et al., 2017, PMID 28403827, DOI: 10.1186/s12881-017-0402-y; Li et al., 2017, PMID not provided in context, DOI: 10.1111/pde.13074 | Context does not provide MONDO/Orphanet/ICD identifiers; disease nomenclature varies across papers. |
| Core phenotype | The most consistent phenotype is congenital hypotrichosis to complete alopecia with dystrophy of finger- and toenails, while teeth, sweating, skeleton, and nervous system are typically normal. (lin2012lossoffunctionmutationsin pages 1-2, khan2017anovelmutation pages 3-5, li2017anovelhomozygous pages 1-3) | Human clinical observations | Lin et al., 2012, PMID 23063621, DOI: 10.1016/j.ajhg.2012.08.029; Khan et al., 2017, PMID 28403827, DOI: 10.1186/s12881-017-0402-y; Li et al., 2017, PMID not provided in context, DOI: 10.1111/pde.13074 | Small number of reported families; severity range across cases is not well quantified. |
| Variant: c.390C>A (p.Tyr130*) | A homozygous nonsense HOXC13 variant c.390C>A (p.Tyr130*) was identified in affected individuals and supports loss of function. (lin2012lossoffunctionmutationsin pages 1-2) | Human molecular genetics | Lin et al., 2012, PMID 23063621, DOI: 10.1016/j.ajhg.2012.08.029 | Family-level evidence; allele frequency and ClinVar classification are not given in context. |
| Variant: 27.6-kb deletion | A homozygous 27.6-kb microdeletion involving HOXC13 exon 1/intron 1 was reported in an affected family, consistent with a null allele. (lin2012lossoffunctionmutationsin pages 3-4) | Human molecular genetics | Lin et al., 2012, PMID 23063621, DOI: 10.1016/j.ajhg.2012.08.029 | Exact HGVS genomic nomenclature beyond coordinates is not fully standardized in the context. |
| Variant: c.812A>G (p.Gln271Arg) | A homozygous missense variant c.812A>G (p.Gln271Arg) in the DNA-binding domain was reported in a North American/Hispanic proband with classic PHNED. (li2017anovelhomozygous pages 1-3) | Human clinical genetics | Li et al., 2017, PMID not provided in context, DOI: 10.1111/pde.13074 | Single-family report; functional assay data are limited in the context to in silico predictions. |
| Variant: c.929A>C (p.Asn310Thr) | A homozygous missense variant c.929A>C (p.Asn310Thr) in the homeobox DNA-binding domain was identified in a consanguineous Pakistani family. (khan2017anovelmutation pages 3-5) | Human clinical genetics + computational structural analysis | Khan et al., 2017, PMID 28403827, DOI: 10.1186/s12881-017-0402-y | Functional evidence is primarily bioinformatic/modeling in the cited context. |
| Inheritance | Reported human HOXC13-related PHNED cases are best supported as autosomal recessive, often in consanguineous families; heterozygous carriers are generally unaffected in human reports. (lin2012lossoffunctionmutationsin pages 1-2, khan2017anovelmutation pages 3-5, perez2022naked(n)mutant pages 13-14) | Human pedigree analysis | Lin et al., 2012, PMID 23063621, DOI: 10.1016/j.ajhg.2012.08.029; Khan et al., 2017, PMID 28403827, DOI: 10.1186/s12881-017-0402-y; Perez et al., 2022, PMID not provided in context, DOI: 10.1111/exd.14469 | Mouse data suggest possible semi-dominant effects for a specific mutant allele, which may not generalize to humans. |
| Mechanism/targets | HOXC13 acts as a transcription factor required for hair/nail differentiation; reported downstream or associated targets include hair keratins (e.g., KRT35, KRT85), FOXN1, DSG4, CRISP1, and FOXQ1, with reduced expression in HOXC13-deficient tissue. (lin2012lossoffunctionmutationsin pages 3-4, khan2017anovelmutation pages 3-5, perez2022naked(n)mutant pages 11-13) | Human tissue expression, mouse functional studies, in vitro/in silico interpretation | Lin et al., 2012, PMID 23063621, DOI: 10.1016/j.ajhg.2012.08.029; Khan et al., 2017, PMID 28403827, DOI: 10.1186/s12881-017-0402-y; Perez et al., 2022, PMID not provided in context, DOI: 10.1111/exd.14469 | Direct target status is stronger for some genes than others; pathway map remains incomplete. |
| Model organisms | Hoxc13-deficient or mutant mice show alopecia and nail defects; additional engineered pig and rabbit knockout models recapitulate major hair/nail abnormalities and support conserved function. (perez2022naked(n)mutant pages 9-11, perez2022naked(n)mutant pages 13-14, perez2022naked(n)mutant pages 11-13) | Mouse, pig, rabbit models | Perez et al., 2022, PMID not provided in context, DOI: 10.1111/exd.14469; supporting cited models in Perez et al.: Han et al., 2017, PMID 28011715; Deng et al., 2019, PMID 30125135 | Animal models may show extra phenotypes (e.g., short lifespan, vertebral findings) not typical of reported human disease. |
| Epidemiology | The disorder is ultra-rare and described through a small number of families from multiple ancestries; robust prevalence or incidence estimates are not available in the retrieved evidence. (lin2012lossoffunctionmutationsin pages 1-2, khan2017anovelmutation pages 3-5, li2017anovelhomozygous pages 1-3) | Aggregated inference from case reports | Lin et al., 2012, PMID 23063621, DOI: 10.1016/j.ajhg.2012.08.029; Khan et al., 2017, PMID 28403827, DOI: 10.1186/s12881-017-0402-y; Li et al., 2017, PMID not provided in context, DOI: 10.1111/pde.13074 | No population-based registries or denominator-based studies were identified in context. |
| Diagnostics | Diagnosis is primarily clinical suspicion based on congenital hair/nail findings followed by confirmatory genetic testing of HOXC13; sequencing and deletion analysis are both relevant because both SNVs and a multi-kb deletion have been reported. (lin2012lossoffunctionmutationsin pages 1-2, lin2012lossoffunctionmutationsin pages 3-4, khan2017anovelmutation pages 3-5, li2017anovelhomozygous pages 1-3) | Human diagnostic genetics | Lin et al., 2012, PMID 23063621, DOI: 10.1016/j.ajhg.2012.08.029; Khan et al., 2017, PMID 28403827, DOI: 10.1186/s12881-017-0402-y; Li et al., 2017, PMID not provided in context, DOI: 10.1111/pde.13074 | No disease-specific formal diagnostic guideline or validated biomarker beyond genotype was identified. |
| Treatment/trial status | No disease-modifying therapy or disease-specific interventional clinical trial was identified in the retrieved evidence; management appears supportive/cosmetic and genetics-based counseling is relevant. (khan2017anovelmutation pages 3-5, li2017anovelhomozygous pages 1-3) | Evidence gap from literature/trial search | Khan et al., 2017, PMID 28403827, DOI: 10.1186/s12881-017-0402-y; Li et al., 2017, PMID not provided in context, DOI: 10.1111/pde.13074 | Absence of evidence is not proof of absence globally; no trial identifiers were available in context. |


*Table: This table summarizes the strongest available evidence for HOXC13-related pure hair-nail ectodermal dysplasia across disease definition, variants, mechanism, models, diagnostics, and treatment gaps. It is designed as a compact reference for building a disease knowledge base entry without overstating unavailable epidemiology or therapeutic evidence.*

## 1. Disease information

### Definition and nomenclature

The preferred knowledge-base label is **HOXC13-related pure hair–nail ectodermal dysplasia**. Common names include:

- Pure hair and nail ectodermal dysplasia, HOXC13-related
- Pure hair–nail ectodermal dysplasia, autosomal recessive
- Ectodermal dysplasia 9, hair/nail type
- **ECTD9**
- **PHNED**

The phenotype belongs to the genetically heterogeneous PHNED group: similar hair–nail disease can also arise from genes such as **KRT74** and **KRT85**, so “PHNED” alone does not specify HOXC13 etiology. (lin2012lossoffunctionmutationsin pages 3-4, lin2012lossoffunctionmutationsin pages 4-6)

### Identifiers

- **OMIM phenotype:** Ectodermal dysplasia 9, hair/nail type, **MIM 614931** is used in the HOXC13-specific literature; the broader PHNED phenotype has also been cited as **MIM 602032**. These identifiers should not be treated as interchangeable without checking the current OMIM record. (lin2012lossoffunctionmutationsin pages 1-2, li2017anovelhomozygous pages 1-3)
- **HOXC13 gene:** OMIM **142976** is reported in the literature.
- **MONDO:** a dedicated HOXC13-specific MONDO identifier was not verified from the retrieved primary sources; it should be curated directly from the current MONDO release rather than inferred.
- **Orphanet, MeSH, ICD-10, ICD-11:** no specific code was established by the retrieved evidence. In routine coding, the disorder may be grouped under ectodermal dysplasia or congenital hair/nail abnormalities, but a broad code loses molecular specificity.

The source evidence is mostly **patient/family-level primary literature**, supplemented by aggregated disease nomenclature and experimental animal work—not EHR-derived population data.

## 2. Etiology

### Causal factor

The established cause is a **biallelic germline pathogenic or likely pathogenic variant in HOXC13**, encoding a homeobox transcription factor required for hair-shaft and nail differentiation. Nonsense, frameshift, missense, and deletion alleles have been reported. The strongest mechanistic class is loss of function through absent transcript/protein, impaired DNA binding, or reduced protein stability. (lin2012lossoffunctionmutationsin pages 1-2, lin2012lossoffunctionmutationsin pages 3-4, khan2017anovelmutation pages 3-5, perez2022naked(n)mutant pages 13-14)

### Risk factors

- **Genetic:** having two pathogenic HOXC13 alleles is the primary risk determinant.
- **Family history/consanguinity:** several reported families were consanguineous, increasing the probability that both parents carry the same rare allele. A Pakistani report described three affected siblings born to healthy first-cousin parents. (khan2017anovelmutation pages 3-5)
- **Sex:** both males and females are affected; no credible sex-specific risk has been demonstrated.
- **Environmental, lifestyle, infectious, occupational, or age-related risk:** none is established.

### Protective factors and gene–environment interaction

No protective HOXC13 alleles, modifier genes, diets, exposures, or validated gene–environment interactions have been reported. Heterozygosity for conventional human loss-of-function alleles appears clinically protective because carriers in the foundational families had normal hair and nails, but this is carrier status rather than a true protective factor. (lin2012lossoffunctionmutationsin pages 1-2)

## 3. Phenotypes

The available literature is too small and ascertainment-biased for defensible percentages. “Typical,” “reported,” and “variable” below therefore refer to repeated case observations, not population frequencies.

### Core manifestations

1. **Congenital generalized hypotrichosis or alopecia**—often complete absence of scalp and body hair, including eyebrows, eyelashes, beard, axillary hair, and pubic hair. Onset is congenital/neonatal, severity ranges from sparse/brittle hair to complete alopecia, and the condition is chronic. Suggested HPO terms: **Hypotrichosis (HP:0001006)**, **Alopecia (HP:0001596)**, **Sparse scalp hair (HP:000 hair-subterm; verify current identifier)**, **Sparse eyebrows (HP:0045075)**, and **Sparse eyelashes (HP:0000653)**. (lin2012lossoffunctionmutationsin pages 1-2, khan2017anovelmutation pages 3-5, li2017anovelhomozygous pages 1-3)

2. **Nail dystrophy involving fingers and toes**—reported findings include micronychia, hypoplastic or irregular nails, brittleness, and distal onycholysis. It is congenital or evident in infancy, persistent, and may be severe across all 20 nails. Suggested HPO terms: **Nail dystrophy (HP:0008404)**, **Micronychia (HP:0001800)**, **Hypoplastic nails (HP:0001803)**, and **Onycholysis (HP:0001806; verify current HPO release)**. (lin2012lossoffunctionmutationsin pages 1-2, khan2017anovelmutation pages 3-5, li2017anovelhomozygous pages 1-3)

3. **Hair-shaft differentiation abnormality**—histologic/mechanistic evidence suggests abnormal shafts may fail to emerge through the epidermis. Suggested HPO: **Abnormality of hair texture (HP:0010719)** or a more specific hair-shaft term after microscopic confirmation. (lin2012lossoffunctionmutationsin pages 3-4)

### Usually absent findings

Reported patients generally had normal teeth, sweat glands, nervous system, skeleton, eyes, and sebaceous glands. These negative findings are diagnostically important because they support a “pure” hair–nail phenotype. (lin2012lossoffunctionmutationsin pages 1-2, khan2017anovelmutation pages 3-5, li2017anovelhomozygous pages 1-3)

A lacrimal-duct obstruction phenotype has been reported in association with an insertion allele in the broader literature, but the retrieved full-text evidence was insufficient to establish its frequency or whether it is a reproducible HOXC13 manifestation. It should be represented as a **single-report phenotypic expansion**, not a defining feature.

### Quality of life

No disease-specific EQ-5D, SF-36, PROMIS, or validated dermatologic quality-of-life series was found. Likely burdens include cosmetic visibility, stigma, psychosocial distress, difficulty protecting the scalp, and functional/cosmetic effects of fragile nails. These are clinically plausible consequences but have not been quantified specifically for HOXC13-related disease.

## 4. Genetic and molecular information

### Gene

- **Gene:** HOXC13, homeobox C13
- **Location:** chromosome 12q13 region; one report gives 12q13.13.
- **Protein:** a 330-amino-acid nuclear homeobox transcription factor; its C-terminal homeodomain mediates sequence-specific DNA binding. (khan2017anovelmutation pages 3-5)
- Suggested annotations: **GO:0003677 DNA binding**, **GO:0003700 DNA-binding transcription-factor activity**, **GO:0006355 regulation of DNA-templated transcription**, and **GO:0005634 nucleus**.

### Reported pathogenic variants

- **c.390C>A (p.Tyr130\*)**, homozygous nonsense: associated with nonsense-mediated decay, markedly reduced HOXC13 RNA, absent protein, and reduced target-gene expression. (lin2012lossoffunctionmutationsin pages 1-2)
- **27.6-kb homozygous deletion**, reported at approximately chr12:54,308,194–54,335,815 in the source assembly, involving exon 1 and part of intron 1: a predicted null allele. Coordinates must be remapped before use in a current reference build. (lin2012lossoffunctionmutationsin pages 3-4)
- **c.812A>G (p.Gln271Arg)**, homozygous missense in the DNA-binding domain: found in a 5-month-old Hispanic boy; both consanguineous parents were heterozygous. PolyPhen-2 and SIFT predicted severe functional impact, but those predictions are not substitutes for a direct functional assay. (li2017anovelhomozygous pages 1-3)
- **c.929A>C (p.Asn310Thr)**, homozygous missense in the homeodomain: segregated with disease in three Pakistani siblings, was absent from 102 ethnically matched controls and referenced databases, and computational modeling predicted altered hydrogen bonding and stability. (khan2017anovelmutation pages 3-5)
- Additional human frameshift and consanguineous-family alleles are documented in the literature: Farooq et al. 2013, **PMID 23315978**, and Ali et al. 2013, **PMID 23461661**. (perez2022naked(n)mutant pages 13-14)

All are reported as **germline**. No somatic HOXC13 etiology is established for this disorder. Current ClinVar assertions, ACMG classifications, dbSNP identifiers, transcript accession numbers, and gnomAD/TOPMed allele frequencies should be rechecked variant by variant against the current genome build; the retrieved sources do not support assigning exact contemporary frequencies. Given the severe recessive phenotype and rarity, causative alleles are expected to be absent or exceptionally rare in population databases, but that expectation is not itself frequency evidence.

### Modifiers, epigenetics, and structural abnormalities

No validated human modifier gene, disease-specific methylation signature, pathogenic chromatin state, aneuploidy, or recurrent translocation has been identified. Mammalian-specific enhancers upstream of the HoxC cluster regulate Hoxc expression in developing hair and nail ectoderm in mice, showing that quantitative cis-regulation is biologically important, but no human enhancer variant has yet been established as a cause of ECTD9. The enhancer study is indexed by **PMID 33199643**. (perez2022naked(n)mutant pages 13-14)

## 5. Environmental information

This is a monogenic developmental disorder. No toxin, radiation exposure, pollutant, occupation, smoking pattern, diet, exercise behavior, alcohol exposure, or infectious agent is known to initiate it. Environmental measures may protect exposed scalp or dystrophic nails from secondary injury, but they do not alter the underlying molecular defect. The disease is not contagious or zoonotic.

## 6. Mechanism and pathophysiology

### Causal chain

**Upstream:** biallelic HOXC13 loss-of-function or function-impairing missense variant → reduced transcript/protein, reduced protein stability, or impaired homeodomain-mediated DNA binding.

**Intermediate:** failure to activate the terminal differentiation program of hair- and nail-forming keratinocytes. Reported direct or downstream targets include **KRT35, KRT85, FOXN1, DSG4, CRISP1,** and **FOXQ1**. Human affected follicles showed sharply reduced or absent expression of several targets. (lin2012lossoffunctionmutationsin pages 3-4, khan2017anovelmutation pages 3-5)

**Downstream:** defective keratin/intermediate-filament and adhesion programs → malformed hair shafts that break or fail to emerge, plus defective nail-plate formation → congenital hypotrichosis/alopecia and nail dystrophy. (lin2012lossoffunctionmutationsin pages 1-2, lin2012lossoffunctionmutationsin pages 3-4)

A useful expert interpretation is that ECTD9 is principally a **terminal epithelial differentiation disorder**, not an inflammatory alopecia, metabolic disease, or generalized ectodysplasin-signaling syndrome. HOXC13 has also been linked experimentally to FOXN1 and hair-cycle/TGF-β–SMAD2 regulation, but the relative importance of these branches in human ECTD9 has not been quantified. (perez2022naked(n)mutant pages 9-11, perez2022naked(n)mutant pages 11-13)

### Cells and ontology suggestions

Affected populations are differentiating epithelial cells of the hair follicle and nail unit:

- Hair matrix/cortical-medullary lineage keratinocytes—suggested **CL:0000312 keratinocyte**, with a more specific follicular keratinocyte term if available.
- Inner and outer root-sheath epithelial cells—CL mapping should be verified because granularity varies.
- Nail-matrix keratinocytes—suggested **CL:0000312** plus anatomical context.

Suggested biological-process terms include **GO:0031069 hair follicle morphogenesis**, **GO:0042633 hair cycle**, **GO:0008544 epidermis development**, **GO:0030216 keratinocyte differentiation**, and **GO:0031424 keratinization**. Suggested cellular components are **GO:0005634 nucleus**, **GO:0005882 intermediate filament**, and **GO:0045095 keratin filament**.

### Omics and advanced technologies

The foundational human work used targeted expression analysis rather than modern disease-scale multi-omics. No validated ECTD9 transcriptomic signature, proteomic biomarker, metabolomic/lipidomic profile, patient single-cell atlas, spatial-transcriptomic study, or patient-derived CRISPR screen was found. A 2023 integrated single-cell scalp study provides a general reference atlas but was not retrieved as direct evidence from ECTD9 patients. Therefore, such data should not be represented as disease-specific.

### Abstract-supported statements

The 2017 BMC study states: **“Affected members exhibited PHNED phenotypes with involvement of complete hair loss and nail dysplasia.”** It further reports: **“Mutation screening revealed a novel missense mutation (c.929A > C; p.Asn310Thr) in homeobox DNA binding domain of HOXC13 gene.”** These are human family and computational-structural evidence, respectively—not randomized or population-level findings. (khan2017anovelmutation pages 3-5)

## 7. Anatomical structures affected

### Primary sites

- Hair follicle and hair shaft—suggested **UBERON:0002073 hair follicle**; verify exact current UBERON term.
- Scalp hair and body hair, including eyebrow, eyelash, beard, axillary, and pubic hair.
- Nail matrix, nail bed, nail plate, and hyponychium of all digits—use current UBERON terms for **nail**, **nail matrix**, and **nail bed** after ontology validation.
- System: integumentary system; tissue class: keratinized stratified squamous epithelium.

HOXC13 expression has been localized to postnatal follicular bulb, medulla, cortex, cuticle, and parts of the root sheath. (lin2012lossoffunctionmutationsin pages 3-4, lin2012lossoffunctionmutationsin pages 4-6)

### Secondary involvement and lateralization

No consistent internal-organ involvement is established. Findings are generalized and bilateral rather than unilateral. Reported skeletal, neural, dental, ocular, and sweat-gland sparing argues against a systemic developmental syndrome in typical cases. (lin2012lossoffunctionmutationsin pages 1-2)

## 8. Temporal development

The condition is **congenital**, with absent/sparse hair and abnormal nails evident at birth or in early infancy. It follows a chronic lifelong course. Hair growth may remain absent or severely impaired; nail dystrophy persists. No accepted stage system, episodic pattern, remission phenotype, or spontaneous recovery rate exists. The biologically critical period is embryonic/postnatal differentiation of hair and nail ectoderm, although diagnosis and family counseling remain useful at any age. (lin2012lossoffunctionmutationsin pages 1-2, li2017anovelhomozygous pages 1-3)

## 9. Inheritance and population

### Inheritance

The established human pattern is **autosomal recessive**. For two heterozygous parents, each pregnancy has a theoretical 25% probability of an affected child, 50% probability of a heterozygous carrier, and 25% probability of an unaffected non-carrier. Reported heterozygous human carriers were generally clinically normal. (lin2012lossoffunctionmutationsin pages 1-2, khan2017anovelmutation pages 3-5)

Penetrance among reported biallelic individuals appears high, but it cannot be estimated precisely. Expressivity varies from sparse/brittle hair to complete alopecia and from nail hypoplasia to severe dystrophy. There is no evidence of anticipation. Germline mosaicism has not been documented but cannot be excluded in apparently de novo cases. Consanguinity is recurrent in reports; no single global founder allele is established.

### Epidemiology

No prevalence, incidence, carrier-frequency, or sex-ratio estimate based on a population denominator was found. Cases have been reported in Chinese Hui, Afghan, Pakistani, Syrian, Hispanic/North American, and other families, indicating multi-ancestry distribution rather than a single endemic region. The published sample is too small to infer ancestry-specific risk. (lin2012lossoffunctionmutationsin pages 1-2, khan2017anovelmutation pages 3-5, li2017anovelhomozygous pages 1-3, perez2022naked(n)mutant pages 13-14)

## 10. Diagnostics

### Clinical recognition

Suspect HOXC13-related disease when congenital generalized hypotrichosis/alopecia co-occurs with dystrophy or hypoplasia of most or all nails while teeth and sweating are normal. Examination should document scalp/body-hair distribution, eyebrows/eyelashes, all 20 nails, teeth, sweating, skin, eyes/lacrimal symptoms, and developmental/skeletal findings.

No diagnostic blood chemistry, circulating protein, metabolite, imaging study, electrophysiologic test, or enzyme assay is established. Hair microscopy or skin biopsy may show abnormal follicular differentiation, but neither is specific enough to replace molecular testing.

### Genetic testing strategy

1. Use a hereditary hypotrichosis/ectodermal-dysplasia panel containing **HOXC13, KRT74, KRT85**, and other phenotype-overlapping genes.
2. Alternatively, sequence **HOXC13** when the phenotype is highly specific.
3. Include exon-level copy-number analysis because a 27.6-kb deletion has been reported; sequence-only assays may miss it. (lin2012lossoffunctionmutationsin pages 3-4)
4. If panel testing is negative, use trio or family-based exome/genome sequencing with CNV and noncoding review.
5. Confirm the variant and segregation by an orthogonal method where appropriate.

CMA has low expected yield unless the causal deletion is large enough and probe coverage is adequate. Karyotyping and FISH are not first-line. Mitochondrial DNA and repeat-expansion testing are not indicated by the known mechanism. RNA analysis may help resolve splice or suspected loss-of-function alleles but is not a standard diagnostic requirement.

### Differential diagnosis

Major alternatives include **KRT74- or KRT85-related PHNED**, other hereditary hypotrichoses, hidrotic ectodermal dysplasia, hypohidrotic ectodermal dysplasia, isolated nail disorders such as RSPO4-related anonychia, and acquired alopecias. Normal teeth and sweating, congenital onset, generalized hair involvement, and biallelic HOXC13 findings favor ECTD9. (lin2012lossoffunctionmutationsin pages 3-4, lin2012lossoffunctionmutationsin pages 4-6)

### Screening

There is no population or newborn screening program. Appropriate strategies are cascade testing of relatives, targeted carrier testing for a known familial variant, prenatal diagnosis, and preimplantation genetic testing after molecular confirmation in the family.

## 11. Outcome and prognosis

Human disease appears to affect morbidity and appearance rather than survival. No reduction in life expectancy, disease-specific mortality, internal-organ failure, or malignant transformation has been established. There are no 5- or 10-year survival statistics. Functional burdens may include nail fragility, secondary trauma/infection, scalp exposure, and psychosocial impact, but formal disability and quality-of-life measures are absent.

The phenotype does not ordinarily recover because the causal developmental/transcriptional defect persists. Prognostic biomarkers beyond genotype are unknown, and genotype–severity correlations remain too weak for individual prediction. Short lifespan observed in some Hoxc13-null or mutant animals should not be extrapolated to humans. (perez2022naked(n)mutant pages 9-11)

## 12. Treatment

### Current management

There is no approved disease-modifying pharmacotherapy. Management is individualized and supportive:

- Wigs, hair prostheses, eyebrow/eyelash cosmetics, and psychological support.
- Sun, cold, and mechanical protection for exposed scalp.
- Nail trimming, emollients, protective gloves/footwear, and prompt treatment of secondary bacterial or fungal infection.
- Dermatology, clinical genetics, and genetic-counseling follow-up.
- Assessment of lacrimal symptoms if present.

Potential NCIt intervention concepts include **Supportive Care**, **Genetic Counseling**, **Prosthetic Device**, and **Psychosocial Intervention**; exact NCIt codes should be validated against the current release.

No evidence supports minoxidil, immunosuppressants, biologics, keratin supplements, surgery, stem-cell treatment, RNA therapy, gene replacement, or CRISPR editing for this disorder. Because the defect acts during specialized epithelial differentiation and likely throughout follicular cycling, durable gene restoration would require safe delivery to relevant follicular and nail progenitors. This remains preclinical speculation.

The clinical-trial search found no disease-specific interventional study or NCT identifier. Consequently, response rates, treatment-related adverse-event data, pharmacogenomic guidance, and combination-treatment algorithms are unavailable.

## 13. Prevention

The genotype cannot be prevented by lifestyle or vaccination. Appropriate prevention is genetic and complication-focused:

- **Primary/reproductive:** carrier testing in at-risk relatives, genetic counseling, preimplantation testing, and prenatal diagnosis where desired.
- **Secondary:** early molecular diagnosis avoids inappropriate immune-directed alopecia treatment and enables family testing.
- **Tertiary:** protect exposed scalp and fragile nails; monitor for trauma or infection; provide psychosocial support.

For a known familial biallelic condition, risk assessment follows autosomal-recessive inheritance. No prophylactic drug, vaccine, environmental intervention, or population screening program is indicated.

## 14. Other species and natural disease

HOXC13 function is evolutionarily conserved across mammals. Experimental loss or mutation affects pelage/wool and related keratinized appendages:

- **Mouse, Mus musculus (NCBI Taxon 10090):** spontaneous Naked and engineered Hoxc13 alleles cause generalized or partial alopecia and abnormal nails. A p.Ser298Ter-like truncation escaped nonsense-mediated decay and behaved semi-dominantly/dominant-negatively in mice, unlike the predominantly recessive human pattern. (perez2022naked(n)mutant pages 9-11, perez2022naked(n)mutant pages 11-13)
- **Pig, Sus scrofa (Taxon 9823):** engineered knockout animals showed complete hair loss, abnormal nails, reduced follicles, and abnormal hair sheaths; relevant report **PMID 28011715**. (perez2022naked(n)mutant pages 9-11, perez2022naked(n)mutant pages 13-14)
- **Rabbit, Oryctolagus cuniculus (Taxon 9986):** engineered knockout produced regional hair loss, reduced follicles, approximately 15% survival to adulthood, and increased caudal vertebrae; report **PMID 30125135**. These extra findings limit direct human extrapolation. (perez2022naked(n)mutant pages 9-11, perez2022naked(n)mutant pages 13-14)
- **Sheep, Ovis aries (Taxon 9940):** a 2024 study found Hoxc13 expression in dermal papillae and inner/outer root sheaths during anagen and catagen; genotypes/haplotypes associated with wool length, supporting conserved control of fiber production rather than documenting an exact natural counterpart of human ECTD9. Published January 2024, DOI: https://doi.org/10.3390/ijms25031594. (sun2024moleculargeneticcharacteristics pages 13-14)

No zoonotic transmission is possible because this is a genetic disorder.

## 15. Model organisms

### Principal models

1. **Hoxc13-null mouse:** reproduces alopecia and nail abnormalities and demonstrates reduced hair-keratin/FOXN1 pathway activity. Strength: extensive molecular tools and close phenotypic match. Limitation: some null mice have low viability or additional features absent from humans. (lin2012lossoffunctionmutationsin pages 1-2, lin2012lossoffunctionmutationsin pages 4-6)
2. **Naked mouse:** spontaneous **Hoxc13S298X** truncation; CRISPR recreation reproduced the phenotype, strongly confirming causality. Heterozygotes can be affected, making it especially useful for studying dominant-negative action but less representative of typical recessive human ECTD9. Published October 2022, DOI: https://doi.org/10.1111/exd.14469. (perez2022naked(n)mutant pages 9-11, perez2022naked(n)mutant pages 11-13)
3. **Knockout pig:** closely models human hair/nail anatomy and recapitulates major appendage abnormalities; useful for delivery and translational studies, but expensive and less genetically tractable. (perez2022naked(n)mutant pages 9-11, perez2022naked(n)mutant pages 13-14)
4. **Knockout rabbit:** useful for follicle–sebaceous-gland balance and hair-pattern studies, although incomplete spatial recapitulation, high mortality, and vertebral findings complicate interpretation. (perez2022naked(n)mutant pages 9-11)

No validated patient-derived organoid, iPSC, or standardized HOXC13-deficient human nail model was found. Such systems would be valuable for separating primary epithelial effects from species-specific systemic phenotypes and for testing allele-specific rescue.

## Recent developments and evidence assessment

The most directly relevant 2023–2024 development is a 2024 report that a homozygous HOXC13 variant causes PHNED through reduced protein stability; however, the retrievable source record did not provide sufficient full-text variant and assay detail for independent extraction, so it should be curated from the original article before database deposition. The 2024 sheep study further refined the conserved spatiotemporal expression of Hoxc13 and related expression to wool length, but it is comparative biology—not human therapeutic evidence. (sun2024moleculargeneticcharacteristics pages 13-14)

Overall, expert interpretation remains anchored in the 2012 human loss-of-function study and subsequent family reports. The evidence is compelling for gene–disease causality and the HOXC13→FOXN1/keratin differentiation axis, but weak for phenotype frequencies, genotype–phenotype correlations, epidemiology, prognosis metrics, and treatment efficacy.

## Key primary references

1. Lin Z et al. **Loss-of-function mutations in HOXC13 cause pure hair and nail ectodermal dysplasia.** *American Journal of Human Genetics*. Published November 2012. PMID **23063621**. DOI/URL: https://doi.org/10.1016/j.ajhg.2012.08.029. (lin2012lossoffunctionmutationsin pages 1-2, lin2012lossoffunctionmutationsin pages 3-4)
2. Farooq M et al. Homozygous HOXC13 frameshift report. Published 2013. PMID **23315978**. (perez2022naked(n)mutant pages 13-14)
3. Ali RH et al. **Novel mutations in HOXC13 underlying pure hair and nail ectodermal dysplasia in consanguineous families.** Published August 2013. PMID **23461661**. DOI/URL: https://doi.org/10.1111/bjd.12302. (perez2022naked(n)mutant pages 13-14)
4. Li X et al. **A novel homozygous missense mutation in HOXC13 leads to autosomal recessive pure hair and nail ectodermal dysplasia.** *Pediatric Dermatology*. Published March 2017. PMID **28297138**. DOI/URL: https://doi.org/10.1111/pde.13074. (li2017anovelhomozygous pages 1-3, perez2022naked(n)mutant pages 13-14)
5. Khan AK et al. **A novel mutation in homeobox DNA binding domain of HOXC13 gene underlies pure hair and nail ectodermal dysplasia (ECTD9) in a Pakistani family.** *BMC Medical Genetics*. Published April 2017. PMID **28403827**. DOI/URL: https://doi.org/10.1186/s12881-017-0402-y. (khan2017anovelmutation pages 3-5)
6. Potter CS et al. **The nude mutant gene Foxn1 is a HOXC13 regulatory target during hair follicle and nail differentiation.** *Journal of Investigative Dermatology*. Published April 2011. DOI/URL: https://doi.org/10.1038/jid.2010.391. (perez2022naked(n)mutant pages 11-13)
7. Fernandez-Guerrero M et al. **Mammalian-specific ectodermal enhancers control the expression of Hoxc genes in developing nails and hair follicles.** *PNAS*. Published November 2020. PMID **33199643**. DOI/URL: https://doi.org/10.1073/pnas.2011078117. (perez2022naked(n)mutant pages 13-14)
8. Perez CJ et al. **Naked (N) mutant mice carry a nonsense mutation in the homeobox of Hoxc13.** *Experimental Dermatology*. Published October 2022. DOI/URL: https://doi.org/10.1111/exd.14469. (perez2022naked(n)mutant pages 9-11, perez2022naked(n)mutant pages 11-13)
9. Sun H et al. **Molecular Genetic Characteristics of the Hoxc13 Gene and Association Analysis of Wool Traits.** *International Journal of Molecular Sciences*. Published January 2024. DOI/URL: https://doi.org/10.3390/ijms25031594. (sun2024moleculargeneticcharacteristics pages 13-14)

**Knowledge-base caution:** ontology identifiers marked for verification, contemporary ClinVar classifications, transcript-specific HGVS nomenclature, genome-build coordinates, and population allele frequencies should be checked against live ontology and genomic databases before production import. The primary literature securely supports the disease concept, congenital hair/nail phenotype, autosomal-recessive inheritance, and HOXC13 loss-of-function mechanism, but not precise epidemiologic or treatment estimates.

References

1. (lin2012lossoffunctionmutationsin pages 1-2): Zhimiao Lin, Quan Chen, Lei Shi, Mingyang Lee, Kathrin A. Giehl, Zhanli Tang, Huijun Wang, Jie Zhang, Jinghua Yin, Lingshen Wu, Ruo Xiao, Xuanzhu Liu, Lanlan Dai, Xuejun Zhu, Ruoyu Li, Regina C. Betz, Xue Zhang, and Yong Yang. Loss-of-function mutations in hoxc13 cause pure hair and nail ectodermal dysplasia. American journal of human genetics, 91 5:906-11, Nov 2012. URL: https://doi.org/10.1016/j.ajhg.2012.08.029, doi:10.1016/j.ajhg.2012.08.029. This article has 88 citations and is from a highest quality peer-reviewed journal.

2. (khan2017anovelmutation pages 3-5): Anwar Kamal Khan, Noor Muhammad, Abdul Aziz, Sher Alam Khan, Khadim Shah, Abdul Nasir, Muzammil Ahmad Khan, and Saadullah Khan. A novel mutation in homeobox dna binding domain of hoxc13 gene underlies pure hair and nail ectodermal dysplasia (ectd9) in a pakistani family. BMC Medical Genetics, Apr 2017. URL: https://doi.org/10.1186/s12881-017-0402-y, doi:10.1186/s12881-017-0402-y. This article has 17 citations and is from a peer-reviewed journal.

3. (li2017anovelhomozygous pages 1-3): Xiaoxiao Li, Meredith Lee Orseth, J. Michael Smith, Mary Abigail Brehm, Nnenna Gebechi Agim, and Donald Alexander Glass. A novel homozygous missense mutation in hoxc13 leads to autosomal recessive pure hair and nail ectodermal dysplasia. Pediatric Dermatology, 34:172-175, Mar 2017. URL: https://doi.org/10.1111/pde.13074, doi:10.1111/pde.13074. This article has 10 citations and is from a peer-reviewed journal.

4. (lin2012lossoffunctionmutationsin pages 3-4): Zhimiao Lin, Quan Chen, Lei Shi, Mingyang Lee, Kathrin A. Giehl, Zhanli Tang, Huijun Wang, Jie Zhang, Jinghua Yin, Lingshen Wu, Ruo Xiao, Xuanzhu Liu, Lanlan Dai, Xuejun Zhu, Ruoyu Li, Regina C. Betz, Xue Zhang, and Yong Yang. Loss-of-function mutations in hoxc13 cause pure hair and nail ectodermal dysplasia. American journal of human genetics, 91 5:906-11, Nov 2012. URL: https://doi.org/10.1016/j.ajhg.2012.08.029, doi:10.1016/j.ajhg.2012.08.029. This article has 88 citations and is from a highest quality peer-reviewed journal.

5. (perez2022naked(n)mutant pages 13-14): Carlos J. Perez, Lars Mecklenburg, Almudena Fernandez, Marta Cantero, Tiago Antonio de Souza, Kevin Lin, Sharon Y. R. Dent, Lluis Montoliu, Alexander Awgulewitsch, and Fernando Benavides. Naked (n) mutant mice carry a nonsense mutation in the homeobox of <i>hoxc13</i>. Oct 2022. URL: https://doi.org/10.1111/exd.14469, doi:10.1111/exd.14469. This article has 3 citations and is from a domain leading peer-reviewed journal.

6. (perez2022naked(n)mutant pages 11-13): Carlos J. Perez, Lars Mecklenburg, Almudena Fernandez, Marta Cantero, Tiago Antonio de Souza, Kevin Lin, Sharon Y. R. Dent, Lluis Montoliu, Alexander Awgulewitsch, and Fernando Benavides. Naked (n) mutant mice carry a nonsense mutation in the homeobox of <i>hoxc13</i>. Oct 2022. URL: https://doi.org/10.1111/exd.14469, doi:10.1111/exd.14469. This article has 3 citations and is from a domain leading peer-reviewed journal.

7. (perez2022naked(n)mutant pages 9-11): Carlos J. Perez, Lars Mecklenburg, Almudena Fernandez, Marta Cantero, Tiago Antonio de Souza, Kevin Lin, Sharon Y. R. Dent, Lluis Montoliu, Alexander Awgulewitsch, and Fernando Benavides. Naked (n) mutant mice carry a nonsense mutation in the homeobox of <i>hoxc13</i>. Oct 2022. URL: https://doi.org/10.1111/exd.14469, doi:10.1111/exd.14469. This article has 3 citations and is from a domain leading peer-reviewed journal.

8. (lin2012lossoffunctionmutationsin pages 4-6): Zhimiao Lin, Quan Chen, Lei Shi, Mingyang Lee, Kathrin A. Giehl, Zhanli Tang, Huijun Wang, Jie Zhang, Jinghua Yin, Lingshen Wu, Ruo Xiao, Xuanzhu Liu, Lanlan Dai, Xuejun Zhu, Ruoyu Li, Regina C. Betz, Xue Zhang, and Yong Yang. Loss-of-function mutations in hoxc13 cause pure hair and nail ectodermal dysplasia. American journal of human genetics, 91 5:906-11, Nov 2012. URL: https://doi.org/10.1016/j.ajhg.2012.08.029, doi:10.1016/j.ajhg.2012.08.029. This article has 88 citations and is from a highest quality peer-reviewed journal.

9. (sun2024moleculargeneticcharacteristics pages 13-14): Hongxian Sun, Zhaohua He, Fangfang Zhao, Jiang Hu, Jiqing Wang, Xiu Liu, Zhidong Zhao, Mingna Li, Yuzhu Luo, and Shaobin Li. Molecular genetic characteristics of the hoxc13 gene and association analysis of wool traits. International Journal of Molecular Sciences, 25:1594, Jan 2024. URL: https://doi.org/10.3390/ijms25031594, doi:10.3390/ijms25031594. This article has 3 citations.

## Artifacts

- [Edison artifact artifact-00](HOXC13_Ectodermal_Dysplasia-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |

All extracted references resolved successfully.