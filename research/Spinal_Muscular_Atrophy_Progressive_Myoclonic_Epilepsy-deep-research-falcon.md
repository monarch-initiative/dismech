---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-13T17:59:36.642203'
end_time: '2026-06-13T18:07:45.480026'
duration_seconds: 488.84
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Spinal Muscular Atrophy-Progressive Myoclonic Epilepsy Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 33
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Spinal_Muscular_Atrophy_Progressive_Myoclonic_Epilepsy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spinal Muscular Atrophy-Progressive Myoclonic Epilepsy Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spinal Muscular Atrophy-Progressive Myoclonic Epilepsy Syndrome** covering all of the
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
- **Disease Name:** Spinal Muscular Atrophy-Progressive Myoclonic Epilepsy Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Spinal Muscular Atrophy-Progressive Myoclonic Epilepsy Syndrome** covering all of the
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


# Comprehensive Research Report: Spinal Muscular Atrophy–Progressive Myoclonic Epilepsy Syndrome (SMA‑PME; ASAH1-related)

## 1. Disease Information

### 1.1 Concise overview (current understanding)
Spinal muscular atrophy with progressive myoclonic epilepsy (SMA‑PME) is an ultra-rare, **autosomal recessive**, non‑5q spinal muscular atrophy phenotype characterized by **lower motor neuron degeneration (anterior horn cell disease) with progressive muscle weakness** plus **progressive myoclonic epilepsy** and neurologic deterioration. It is caused by **biallelic loss‑of‑function variants in ASAH1**, encoding lysosomal **acid ceramidase (ACDase)**, and is allelic to **Farber disease** (acid ceramidase deficiency spectrum). (cuinat2025acidceramidasedeficiency pages 1-2, najafi2023spinalmuscularatrophy pages 1-2)

Direct abstract quotes supporting the definition include:
- “Spinal muscular atrophy with progressive myoclonic epilepsy (SMA‑PME) due to acid ceramidase deficiency is a rare disorder, allelic with Farber disease, resulting from recessive ASAH1 variants.” (Cuinat et al., 2025-04; https://doi.org/10.1212/nxg.0000000000200243) (cuinat2025acidceramidasedeficiency pages 1-2)
- “Patients present in early childhood with muscle weakness due to anterior horn degeneration and/or progressive drug-resistant myoclonic epilepsy.” (Cuinat et al., 2025-04; https://doi.org/10.1212/nxg.0000000000200243) (cuinat2025acidceramidasedeficiency pages 1-2)

### 1.2 Key identifiers and nomenclature
- **OMIM/MIM**: SMA‑PME **MIM#159950**; Farber disease **MIM#228000** (cuinat2025acidceramidasedeficiency pages 1-2)
- **ASAH1 gene**: encodes **acid ceramidase / N-acylsphingosine amidohydrolase 1**; reported locus wording includes **8p22** (Najafi 2023) and **8p23.3–p21.3** (Nishio 2024 review) (najafi2023spinalmuscularatrophy pages 1-2, nishio2024clinicalandgenetic pages 19-21)
- **MONDO / Orphanet / MeSH / ICD‑10/ICD‑11**: Not explicitly provided in the retrieved sources used here; therefore not asserted (cuinat2025acidceramidasedeficiency pages 1-2)

### 1.3 Synonyms / alternative names
- “Spinal muscular atrophy with progressive myoclonic epilepsy” (SMA‑PME) (cuinat2025acidceramidasedeficiency pages 1-2, najafi2023spinalmuscularatrophy pages 1-2)
- “Acid ceramidase deficiency” (as the umbrella ASAH1 disorder encompassing Farber disease and SMA‑PME) (cuinat2025acidceramidasedeficiency pages 1-2)

### 1.4 Evidence source type
The retrieved evidence is derived from **aggregated disease resources**: case reports/series, mutational spectrum reviews, natural history synthesis, and clinical trial registry entries—not from EHR-only sources in this retrieval set. (cuinat2025acidceramidasedeficiency pages 1-2, najafi2023spinalmuscularatrophy pages 2-4, NCT03233841 chunk 1)

| Concept (disease/gene/enzyme) | Identifier type | Identifier/value | Notes/synonyms | Evidence snippet (short quote) | Source (authors year, URL) |
|---|---|---|---|---|---|
| Disease | Preferred name | Spinal muscular atrophy with progressive myoclonic epilepsy (SMA-PME) | Also written as “spinal muscular atrophy with progressive myoclonic epilepsy”; ASAH1-related acid ceramidase deficiency phenotype | “Spinal muscular atrophy with progressive myoclonic epilepsy (SMA-PME)” (cuinat2025acidceramidasedeficiency pages 1-2, najafi2023spinalmuscularatrophy pages 1-2) | Cuinat et al. 2025, https://doi.org/10.1212/nxg.0000000000200243; Najafi et al. 2023, https://doi.org/10.1186/s13052-023-01474-z |
| Disease | OMIM/MIM | MIM #159950 | Explicitly given for SMA-PME | “SMA-PME (MIM#159950)” (cuinat2025acidceramidasedeficiency pages 1-2) | Cuinat et al. 2025, https://doi.org/10.1212/nxg.0000000000200243 |
| Disease | Disease classification / related disorder | Acid ceramidase deficiency | SMA-PME is described as an ASAH1-related acid ceramidase deficiency disorder allelic with Farber disease | “SMA-PME due to acid ceramidase deficiency is a rare disorder, allelic with Farber disease” (cuinat2025acidceramidasedeficiency pages 1-2) | Cuinat et al. 2025, https://doi.org/10.1212/nxg.0000000000200243 |
| Disease | Related disease OMIM/MIM | Farber disease (FD; MIM #228000) | Allelic disorder within ASAH1 deficiency spectrum | “Farber disease (FD; MIM#228000) and SMA-PME (MIM#159950)” (cuinat2025acidceramidasedeficiency pages 1-2) | Cuinat et al. 2025, https://doi.org/10.1212/nxg.0000000000200243 |
| Disease | MONDO | Not in retrieved sources | No MONDO identifier explicitly stated in retrieved evidence | “The excerpt does not provide Orphanet, MONDO, MeSH, or ICD codes.” (cuinat2025acidceramidasedeficiency pages 1-2) | Cuinat et al. 2025, https://doi.org/10.1212/nxg.0000000000200243 |
| Disease | Orphanet | Not in retrieved sources | No Orphanet identifier explicitly stated in retrieved evidence | “The excerpt does not provide Orphanet, MONDO, MeSH, or ICD codes.” (cuinat2025acidceramidasedeficiency pages 1-2) | Cuinat et al. 2025, https://doi.org/10.1212/nxg.0000000000200243 |
| Disease | MeSH | Not in retrieved sources | No MeSH identifier explicitly stated in retrieved evidence | “The excerpt does not provide Orphanet, MONDO, MeSH, or ICD codes.” (cuinat2025acidceramidasedeficiency pages 1-2) | Cuinat et al. 2025, https://doi.org/10.1212/nxg.0000000000200243 |
| Disease | ICD-10/ICD-11 | Not in retrieved sources | No ICD code explicitly stated in retrieved evidence | “The excerpt does not provide Orphanet, MONDO, MeSH, or ICD codes.” (cuinat2025acidceramidasedeficiency pages 1-2) | Cuinat et al. 2025, https://doi.org/10.1212/nxg.0000000000200243 |
| Gene | Gene symbol | ASAH1 | Causative gene for SMA-PME; recessive biallelic pathogenic variants | “biallelic pathogenic variants in ASAH1 gene” (najafi2023spinalmuscularatrophy pages 1-2) | Najafi et al. 2023, https://doi.org/10.1186/s13052-023-01474-z |
| Gene | Full gene/protein name | N-acylsphingosine amidohydrolase 1 (ASAH1) | Gene encodes lysosomal acid ceramidase | “encodes N-Acylsphingosine Amidohydrolase 1 (ASAH1)” (nishio2024clinicalandgenetic pages 19-21, nishio2024clinicalandgenetic pages 21-22) | Nishio et al. 2024, https://doi.org/10.3390/genes15101294 |
| Gene | Chromosomal location | 8p22 | Explicitly stated in retrieved evidence | “ASAH1 (14 exons, located at 8p22)” (najafi2023spinalmuscularatrophy pages 1-2) | Najafi et al. 2023, https://doi.org/10.1186/s13052-023-01474-z |
| Gene | Alternative cytogenetic location wording | 8p23.3–p21.3 | Alternate location wording reported in review | “mapped to chromosome 8p23.3–p21.3” (nishio2024clinicalandgenetic pages 19-21) | Nishio et al. 2024, https://doi.org/10.3390/genes15101294 |
| Enzyme/protein | Enzyme name | Acid ceramidase (ACDase; aCDase) | Lysosomal hydrolase encoded by ASAH1; synonyms ACDase/aCDase | “ASAH1 encodes acid ceramidase (aCDase)” (najafi2023spinalmuscularatrophy pages 1-2); “ACDase (acid ceramidase)” (cuinat2025acidceramidasedeficiency pages 1-2) | Najafi et al. 2023, https://doi.org/10.1186/s13052-023-01474-z; Cuinat et al. 2025, https://doi.org/10.1212/nxg.0000000000200243 |
| Disease information source type | Evidence provenance | Aggregated disease-level literature/case series; not EHR-derived in retrieved sources | Retrieved evidence consists of case reports, case series, reviews, and a natural history study | “we present the detailed history of 9 patients… Based on a comprehensive literature review” (cuinat2025acidceramidasedeficiency pages 1-2); “three new cases and review of the mutational spectrum” (najafi2023spinalmuscularatrophy pages 2-4) | Cuinat et al. 2025, https://doi.org/10.1212/nxg.0000000000200243; Najafi et al. 2023, https://doi.org/10.1186/s13052-023-01474-z |


*Table: This table summarizes the explicitly stated disease, gene, and enzyme identifiers and nomenclature retrieved for ASAH1-related spinal muscular atrophy with progressive myoclonic epilepsy. It is useful for normalization of disease knowledge base entries while clearly marking identifiers that were not available in the retrieved evidence.*

## 2. Etiology

### 2.1 Primary causes
SMA‑PME is caused by **biallelic pathogenic variants in ASAH1**, producing **acid ceramidase deficiency** with downstream **ceramide accumulation**. (cuinat2025acidceramidasedeficiency pages 1-2, najafi2023spinalmuscularatrophy pages 1-2)

Mechanistic definition quote:
- Acid ceramidase “catalyzes the degradation of ceramides into fatty acids and sphingosine inside the lysosome.” (Cuinat et al., 2025-04; https://doi.org/10.1212/nxg.0000000000200243) (cuinat2025acidceramidasedeficiency pages 1-2)

### 2.2 Risk factors
- **Genetic risk factor**: recessive inheritance with biallelic ASAH1 variants. A large literature synthesis reported homozygous variants in **55%** of SMA‑PME patients, concordant with **consanguinity reported in 42%**. (cuinat2025acidceramidasedeficiency pages 8-10)
- **Environmental risk factors / protective factors / gene–environment interactions**: No disease-specific evidence was retrieved here; none are asserted.

## 3. Phenotypes (clinical spectrum)

### 3.1 Core phenotype domains (human)
Across recent case series/reviews, core manifestations include:
- **Motor neuron disease / SMA phenotype**: progressive proximal weakness, gait loss, muscle atrophy, tremor; attributed to **anterior horn degeneration**. (cuinat2025acidceramidasedeficiency pages 1-2, najafi2023spinalmuscularatrophy pages 2-4)
- **Progressive myoclonic epilepsy**: myoclonus and generalized seizures (including tonic‑clonic, absences, drop attacks), often progressively drug‑resistant. (cuinat2025acidceramidasedeficiency pages 2-3, najafi2023spinalmuscularatrophy pages 2-4)
- **Neurodevelopment/cognition**: cognitive impairment and psychomotor regression can appear later in disease in a subset (e.g., cognitive impairment 4/9; psychomotor regression 3/9 in one cohort). (cuinat2025acidceramidasedeficiency pages 3-4)
- **Sensorineural hearing loss**: reported frequently in one cohort (5/9). (cuinat2025acidceramidasedeficiency pages 2-3)

Recent natural history statistics (Cuinat et al. 2025; 9 new patients + literature review):
- “A total of 44 patients from 37 families.” (cuinat2025acidceramidasedeficiency pages 2-3)
- “Age at onset ranged from 2.5 to 16 years” and epilepsy onset typically “5 to 14 years.” (cuinat2025acidceramidasedeficiency pages 8-10)
- In the 9-patient cohort: weakness in **8/9** (mean ~10 years), loss of ambulation **5/9** (mean ~12.6 years), epilepsy **7/9** (mean ~9.7 years), drug resistance **4/7** occurring ~1.1 years after onset. (cuinat2025acidceramidasedeficiency pages 2-3)
- Mortality: “50% of patients died before 18 years” and death “at around 17 years of age,” typically from respiratory complications or status epilepticus. (cuinat2025acidceramidasedeficiency pages 8-10, cuinat2025acidceramidasedeficiency pages 1-2)

### 3.2 Example HPO term suggestions (non-exhaustive)
(ontology mappings suggested for knowledge-base use)
- Proximal muscle weakness (HP:0008994)
- Muscle atrophy (HP:0003202)
- Lower motor neuron dysfunction / neurogenic muscle weakness (HP:0007340, motor neuron phenotype terms)
- Myoclonic seizures (HP:0002123)
- Generalized tonic-clonic seizures (HP:0002069)
- Progressive myoclonic epilepsy (HP:0007256)
- Drug-resistant epilepsy (HP:0002340)
- Tremor (HP:0001337)
- Loss of ambulation (HP:0031936)
- Sensorineural hearing impairment (HP:0000407)
- Cognitive impairment (HP:0100543)
- Developmental regression (HP:0002376)

### 3.3 Quality-of-life impact
While formal QoL instruments were not reported in the retrieved papers, the progressive loss of gait/ambulation, drug-resistant epilepsy, and cognitive regression imply major functional impairment. Motor scales (MFM‑32; GMFC‑MLD) were used in prospective follow-up in SMA‑PME, indicating clinically meaningful monitoring of function. (cuinat2025acidceramidasedeficiency pages 1-2)

## 4. Genetic / Molecular Information

### 4.1 Causal gene
- **ASAH1** encodes lysosomal **acid ceramidase (ACDase/aCDase)**; biallelic variants cause SMA‑PME and Farber disease (allelic spectrum). (cuinat2025acidceramidasedeficiency pages 1-2, najafi2023spinalmuscularatrophy pages 1-2)

### 4.2 Pathogenic variants and genotype–phenotype considerations
- SMA‑PME is described as arising from “biallelic pathogenic variants in ASAH1 gene.” (Najafi et al., 2023-06; https://doi.org/10.1186/s13052-023-01474-z) (najafi2023spinalmuscularatrophy pages 2-4)
- Example variants reported in new SMA‑PME cases include exon 2 missense variants **c.109C>A (p.Pro37Thr)** and **c.125C>T (p.Thr42Met)**. (najafi2023spinalmuscularatrophy pages 2-4)
- Functional activity example: c.125C>T (p.Thr42Met) was reported to yield “only 32% of normal acid ceramidase activity” in transfected cells in cited work summarized by Nishio et al. (nishio2024clinicalandgenetic pages 21-22)

Genotype–phenotype signals (from compiled case analysis):
- Two variants recur in the literature synthesis (e.g., p.(Thr42Met) and p.(Lys152Asn)) and were associated with differences in onset; the 2025 natural history study reports a “genotype-phenotype correlation for the 2 main variants and the disease onset.” (cuinat2025acidceramidasedeficiency pages 1-2)
- Variant distribution across ACDase subunits: Farber-associated mutations cluster more in the β-subunit, whereas “a larger number of mutations in SMA‑PME have been identified within the alpha-subunit.” (nishio2024clinicalandgenetic pages 19-21, nishio2024clinicalandgenetic pages 21-22)
- “Residual levels of acid ceramidase activity may determine the phenotype of the ASAH1-related disorders.” (nishio2024clinicalandgenetic pages 21-22)

### 4.3 Inheritance, penetrance, expressivity
- **Inheritance**: autosomal recessive / recessive ASAH1 variants. (cuinat2025acidceramidasedeficiency pages 1-2, najafi2023spinalmuscularatrophy pages 2-4)
- **Expressivity**: variable; SMA‑PME and Farber disease form a continuum and presentations can be atypical (e.g., ASAH1 biallelic variants causing a “pure motor phenotype without epileptic myoclonic seizures” in a non‑5q SMA cohort). (theuriet2024geneticcharacterizationof pages 5-6, theuriet2024geneticcharacterizationof pages 6-7)

### 4.4 Modifier genes / epigenetics
No SMA‑PME-specific human modifier-gene or epigenetic evidence was retrieved in the current tool run.

## 5. Environmental Information
No SMA‑PME-specific environmental, lifestyle, or infectious contributing factors were identified in the retrieved evidence; this disorder is primarily Mendelian (ASAH1). (cuinat2025acidceramidasedeficiency pages 1-2, najafi2023spinalmuscularatrophy pages 1-2)

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (high-level)
**ASAH1 loss of function → reduced lysosomal acid ceramidase activity → ceramide accumulation in tissues (CNS and peripheral organs) → inflammatory responses and neurodegeneration/motor neuron pathology → progressive weakness (SMA phenotype) and progressive myoclonic epilepsy.** (cuinat2025acidceramidasedeficiency pages 1-2, derome2024[therapeuticperspectivesfor pages 2-3)

Mechanistic tissue distribution quote (French review):
- “Cette mutation empêche l’adressage de l’ACDase au lysosome, réduit son activité enzymatique et entraîne une accumulation de céramides dans le cerveau et les organes périphériques…” (Derome et al., 2024-11; https://doi.org/10.1051/medsci/2024162) (derome2024[therapeuticperspectivesfor pages 2-3)
- “Les niveaux de céramides sont élevés dans le SNC, de manière plus importante dans la moelle épinière que dans le cerveau.” (derome2024[therapeuticperspectivesfor pages 2-3)

Neuroinflammation hypothesis (review):
- “Accumulation of ceramide may also cause an imbalanced activation of pathways and mediators in microglia, leading to neurodegeneration and neuroinflammation.” (Nishio et al., 2024-09; https://doi.org/10.3390/genes15101294) (nishio2024clinicalandgenetic pages 19-21)

### 6.2 Pathways and ontology suggestions
- **GO biological process**: ceramide catabolic process; sphingolipid metabolic process; lysosomal lumen processes; neuroinflammatory response; microglial activation.
- **Cell types (CL)**: spinal motor neuron (CL:0000099), microglial cell (CL:0000129).
- **Pathway resources (conceptual)**: lysosomal sphingolipid metabolism / ceramide–sphingosine axis.

### 6.3 Model organism evidence (selected)
A 2024 review summarizes zebrafish ASAH1 knockdown phenotypes: “marked loss of motor-neuron axonal branching and increased spinal-cord apoptosis,” supporting motor neuron vulnerability to ASAH1 deficiency. (nishio2024clinicalandgenetic pages 21-22)

Mouse model survival statistics (therapeutic perspectives review):
- Asah1P361R/P361R (Farber-like) median survival “autour de 50 jours” and a milder line with median survival “145 jours.” (derome2024[therapeuticperspectivesfor pages 2-3)

## 7. Anatomical Structures Affected

### 7.1 Organ/system level
- **Primary**: nervous system (spinal anterior horn; epilepsy network), neuromuscular system. (cuinat2025acidceramidasedeficiency pages 1-2)
- **Secondary/variable**: respiratory system (respiratory complications contribute to death), and in the broader ASAH1 spectrum peripheral organs including liver/spleen/lungs/kidneys can show ceramide accumulation. (cuinat2025acidceramidasedeficiency pages 1-2, derome2024[therapeuticperspectivesfor pages 2-3)

### 7.2 Ontology suggestions
- **UBERON**: spinal cord (UBERON:0002240), anterior horn region (UBERON spinal cord gray matter subdivisions), skeletal muscle (UBERON:0001134), brain (UBERON:0000955), liver/spleen/lung/kidney.
- **GO cellular component**: lysosome (GO:0005764), lysosomal lumen (GO:0043202).

## 8. Temporal Development

### 8.1 Onset
- Early childhood onset is typical: “Patients present in early childhood…” (cuinat2025acidceramidasedeficiency pages 1-2)
- Quantified onset range: “Age at onset ranged from 2.5 to 16 years.” (cuinat2025acidceramidasedeficiency pages 8-10)

### 8.2 Progression and course
The 2025 natural history synthesis describes a progressive course with development of weakness and epilepsy, loss of ambulation, later cognitive decline in some, and adolescent mortality in many. (cuinat2025acidceramidasedeficiency pages 8-10, cuinat2025acidceramidasedeficiency pages 2-3, cuinat2025acidceramidasedeficiency pages 1-2)

## 9. Inheritance and Population

### 9.1 Epidemiology
Disease prevalence is not robustly established in the retrieved primary sources. A 2024 French-language review states ASAH1 deficiency prevalence is “<1/1,000,000.” (derome2024[therapeuticperspectivesfor pages 1-2)

### 9.2 Population and family structure
Consanguinity and homozygosity are prominent in reported cases (55% homozygous variants; 42% parental consanguinity reported). (cuinat2025acidceramidasedeficiency pages 8-10)

## 10. Diagnostics

### 10.1 Diagnostic approach (current practice)
- Rule out 5q SMA: Najafi et al. used MLPA to exclude SMN1/SMN2 copy-number abnormalities alongside exome sequencing. (najafi2023spinalmuscularatrophy pages 2-4)
- Confirm ASAH1: via WES/WGS/panels; non‑5q SMA reviews emphasize that “DNA analysis … [is] essential for accurate diagnosis” and that WES/WGS are key tools (while diagnostic yield remains limited). (nishio2024clinicalandgenetic pages 1-2)

Testing-strategy evidence in non‑5q SMA cohorts (actionable for SMA‑PME differential):
- Theuriet et al. recommend “a large NGS panel should be the first choice, before performing WES or WGS,” and note ASAH1 was missed because it was not included in the panel: “the ASAH1 variant could not have been detected by the NGS panel, because this gene is currently not included,” prompting the recommendation to update panels to include ASAH1. (Theuriet et al., 2024-06; https://doi.org/10.1038/s41431-023-01407-8) (theuriet2024geneticcharacterizationof pages 6-7)

### 10.2 Electrophysiology and clinical findings
SMA‑PME is associated with EEG abnormalities (e.g., generalized spikes and slow waves; generalized SW/PSW complexes), and neurogenic changes on muscle biopsy/EMG consistent with denervation in cited case series summarized in the 2024 non‑5q SMA review. (nishio2024clinicalandgenetic pages 19-21, nishio2024clinicalandgenetic pages 21-22)

### 10.3 Biochemical / molecular biomarkers
Key laboratory measures in recent natural-history work include:
- **ACDase activity in leukocytes**: profoundly decreased (e.g., “1.5%–8.3% of control values” in one cohort). (cuinat2025acidceramidasedeficiency pages 2-3)
- **C26‑ceramide on dried blood spots (DBS)** by LC‑MS/MS: evaluated as a candidate biomarker; authors note limited reliability for longitudinal follow-up in SMA‑PME (moderate accumulation; variable trajectories). (cuinat2025acidceramidasedeficiency pages 12-13)
- **In-cell ceramide degradation assay** in living skin fibroblasts: proposed as a more reliable measure of residual enzymatic activity and a potential pharmacodynamic readout for therapy. (cuinat2025acidceramidasedeficiency pages 1-2)

## 11. Outcome / Prognosis
SMA‑PME has a poor prognosis with progressive neurologic decline. In compiled analyses, death is often in adolescence, frequently due to respiratory complications or status epilepticus; one synthesis reports that “50% of patients died before 18 years” and death “at around 17 years of age.” (cuinat2025acidceramidasedeficiency pages 8-10, cuinat2025acidceramidasedeficiency pages 1-2)

## 12. Treatment

### 12.1 Current standard of care
No disease-modifying or curative treatment is established in the retrieved evidence; management is largely supportive and symptomatic.
- Najafi et al. state that “No successful disease-modifying treatments have been reported; management is symptomatic and multidisciplinary.” (najafi2023spinalmuscularatrophy pages 2-4)
- A 2024 therapeutic perspectives review states: “À ce jour, il n’y a pas de traitement spécifique ou curatif disponible.” (Derome et al., 2024-11; https://doi.org/10.1051/medsci/2024162) (derome2024[therapeuticperspectivesfor pages 1-2)

### 12.2 Experimental / translational approaches (expert synthesis)
Because SMA‑PME is on the ASAH1 (acid ceramidase deficiency) spectrum, therapeutic concepts often derive from Farber disease and lysosomal storage disease strategies:
- **Hematopoietic stem cell transplantation (HSCT)**: reported to correct peripheral inflammatory signs but not neurologic progression in acid ceramidase deficiency: “correction complète et persistante des signes inflammatoires… mais n’empêche pas la progression de la maladie neurologique.” (derome2024[therapeuticperspectivesfor pages 2-3)
- **Enzyme replacement therapy (ERT; rhACDase)**: preclinical ERT lowers ceramide accumulation and inflammatory markers in Asah1 mutant mice; a key limitation is CNS penetration (“does not yet have the full capacity to penetrate the blood–brain barrier”). (Kleynerman et al., 2023-02; https://doi.org/10.3390/biom13020274) (kleynerman2023acidceramidasedeficiency pages 14-15)
- **Gene therapy / gene-based approaches**: discussed conceptually as promising for sphingolipid metabolic disorders and acid ceramidase deficiency in expert reviews; AAV-based delivery and lentiviral HSC gene therapy frameworks are described as potential strategies. (derome2024[therapeuticperspectivesfor pages 2-3, kleynerman2023acidceramidasedeficiency pages 14-15)

### 12.3 Real-world implementations (clinical studies)
While no SMA‑PME interventional trials were retrieved in this run, Farber disease (same ASAH1/ACDase deficiency spectrum) has structured observational studies relevant to biomarker and outcome development:
- **Farber Disease Natural History Study (NCT03233841; completed; enrollment 45; first posted 2017)**: collects clinical/functional outcomes (6MWT, PFTs), PROs, imaging, inflammatory markers, and exploratory “specific ceramide levels” and “cytokines/chemokines” in blood; confirmatory diagnosis includes acid ceramidase activity <30% of control. https://clinicaltrials.gov/study/NCT03233841 (NCT03233841 chunk 1)
- **BioFarber biomarker study (NCT02298634; withdrawn; first posted 2018)**: planned NGS confirmation of ASAH1 and mass‑spectrometry biomarker discovery from DBS. https://clinicaltrials.gov/study/NCT02298634 (NCT02298634 chunk 1)

### 12.4 MAXO term suggestions (non-exhaustive)
- Antiseizure medication therapy; epilepsy management
- Physical therapy; occupational therapy; respiratory supportive care
- Genetic counseling
- Hematopoietic stem cell transplantation (experimental/selected phenotypes)
- Enzyme replacement therapy (investigational)
- Gene therapy (investigational)

## 13. Prevention
Primary prevention is not applicable in the traditional (environmental) sense for a recessive Mendelian disorder, but **genetic counseling** and **carrier testing** in affected families are central.

Given recessive inheritance and high consanguinity fraction reported, preventive strategies include cascade testing and reproductive counseling. (cuinat2025acidceramidasedeficiency pages 8-10)

## 14. Other Species / Natural Disease
No naturally occurring veterinary disease analogs were retrieved in the current evidence set.

## 15. Model Organisms
Model-organism work is substantial for acid ceramidase deficiency broadly:
- Mouse models (e.g., Asah1P361R/P361R) recapitulate systemic ceramide accumulation, inflammation, and early mortality (median survival ~50 days in one model; 145 days in a milder line). (derome2024[therapeuticperspectivesfor pages 2-3)
- Zebrafish knockdown evidence suggests motor neuron axonal branching defects and spinal cord apoptosis. (nishio2024clinicalandgenetic pages 21-22)

## Recent developments (2023–2024 emphasis)
- **2023**: A comprehensive review connects **clinical presentation, mouse models, and therapeutic concepts** for acid ceramidase deficiency (including SMA‑PME) and emphasizes barriers such as BBB penetration for ERT. (Kleynerman et al., 2023-02; https://doi.org/10.3390/biom13020274) (kleynerman2023acidceramidasedeficiency pages 14-15, kleynerman2023acidceramidasedeficiency pages 1-2)
- **2023**: New SMA‑PME cases with ASAH1 variants and an updated mutational spectrum were reported, reinforcing WES-based diagnosis and the phenotypic heterogeneity. (Najafi et al., 2023-06; https://doi.org/10.1186/s13052-023-01474-z) (najafi2023spinalmuscularatrophy pages 2-4)
- **2024**: Non‑5q SMA diagnostic strategy studies emphasize **large gene panels first**, updating panels to include **ASAH1**, with WES/WGS reserved for specific scenarios. (Theuriet et al., 2024-06; https://doi.org/10.1038/s41431-023-01407-8) (theuriet2024geneticcharacterizationof pages 6-7)
- **2024**: A therapeutic perspectives review (French) consolidates mechanistic and model data and reiterates absence of curative therapy while describing HSCT and gene-therapy frameworks. (Derome et al., 2024-11; https://doi.org/10.1051/medsci/2024162) (derome2024[therapeuticperspectivesfor pages 2-3, derome2024[therapeuticperspectivesfor pages 1-2)

## Evidence limitations (important for knowledge base curation)
- Formal cross-ontology disease identifiers (MONDO, Orphanet, MeSH, ICD‑10/11) were not present in the retrieved excerpts and are therefore not reported here. (cuinat2025acidceramidasedeficiency pages 1-2)
- Several quantitative clinical features (e.g., seizure semiology distribution, standardized QoL) remain incompletely characterized in the 2023–2024 literature retrieved, and the most detailed natural history and biomarker evaluation in this run comes from 2025. (cuinat2025acidceramidasedeficiency pages 2-3, cuinat2025acidceramidasedeficiency pages 1-2)


References

1. (cuinat2025acidceramidasedeficiency pages 1-2): Silvestre Cuinat, Paul Rollier, Katheryn Grand, Pedro A. Sanchez-Lara, Michelle Allen-Sharpley, Thierry Levade, Marie T. Vanier, Laurence Lion Francois, Nicole Chemaly, Capucine de Lattre, Camille Moreau, Adrien Paquot, Terence Beghyn, Servane de Masfrand, Stéphane Bézieau, Sandra Mercier, and Odile Boespflug-Tanguy. Acid ceramidase deficiency. Apr 2025. URL: https://doi.org/10.1212/nxg.0000000000200243, doi:10.1212/nxg.0000000000200243. This article has 2 citations.

2. (najafi2023spinalmuscularatrophy pages 1-2): Ali Najafi, Behnoosh Tasharrofi, Farshid Zandsalimi, Maryam Rasulinezhad, Masood Ghahvechi Akbari, Gholamreza Zamani, Mahmoud Reza Ashrafi, and Morteza Heidari. Spinal muscular atrophy with progressive myoclonic epilepsy (sma-pme): three new cases and review of the mutational spectrum. Italian Journal of Pediatrics, Jun 2023. URL: https://doi.org/10.1186/s13052-023-01474-z, doi:10.1186/s13052-023-01474-z. This article has 13 citations and is from a peer-reviewed journal.

3. (nishio2024clinicalandgenetic pages 19-21): Hisahide Nishio, Emma Niba, Toshio Saito, Kentaro Okamoto, Tomoko Lee, Yasuhiro Takeshima, Hiroyuki Awano, and Poh-San Lai. Clinical and genetic profiles of 5q- and non-5q-spinal muscular atrophy diseases in pediatric patients. Genes, 15:1294, Sep 2024. URL: https://doi.org/10.3390/genes15101294, doi:10.3390/genes15101294. This article has 14 citations.

4. (najafi2023spinalmuscularatrophy pages 2-4): Ali Najafi, Behnoosh Tasharrofi, Farshid Zandsalimi, Maryam Rasulinezhad, Masood Ghahvechi Akbari, Gholamreza Zamani, Mahmoud Reza Ashrafi, and Morteza Heidari. Spinal muscular atrophy with progressive myoclonic epilepsy (sma-pme): three new cases and review of the mutational spectrum. Italian Journal of Pediatrics, Jun 2023. URL: https://doi.org/10.1186/s13052-023-01474-z, doi:10.1186/s13052-023-01474-z. This article has 13 citations and is from a peer-reviewed journal.

5. (NCT03233841 chunk 1):  Farber Disease Natural History Study. Sumitomo Pharma Switzerland GmbH. 2017. ClinicalTrials.gov Identifier: NCT03233841

6. (nishio2024clinicalandgenetic pages 21-22): Hisahide Nishio, Emma Niba, Toshio Saito, Kentaro Okamoto, Tomoko Lee, Yasuhiro Takeshima, Hiroyuki Awano, and Poh-San Lai. Clinical and genetic profiles of 5q- and non-5q-spinal muscular atrophy diseases in pediatric patients. Genes, 15:1294, Sep 2024. URL: https://doi.org/10.3390/genes15101294, doi:10.3390/genes15101294. This article has 14 citations.

7. (cuinat2025acidceramidasedeficiency pages 8-10): Silvestre Cuinat, Paul Rollier, Katheryn Grand, Pedro A. Sanchez-Lara, Michelle Allen-Sharpley, Thierry Levade, Marie T. Vanier, Laurence Lion Francois, Nicole Chemaly, Capucine de Lattre, Camille Moreau, Adrien Paquot, Terence Beghyn, Servane de Masfrand, Stéphane Bézieau, Sandra Mercier, and Odile Boespflug-Tanguy. Acid ceramidase deficiency. Apr 2025. URL: https://doi.org/10.1212/nxg.0000000000200243, doi:10.1212/nxg.0000000000200243. This article has 2 citations.

8. (cuinat2025acidceramidasedeficiency pages 2-3): Silvestre Cuinat, Paul Rollier, Katheryn Grand, Pedro A. Sanchez-Lara, Michelle Allen-Sharpley, Thierry Levade, Marie T. Vanier, Laurence Lion Francois, Nicole Chemaly, Capucine de Lattre, Camille Moreau, Adrien Paquot, Terence Beghyn, Servane de Masfrand, Stéphane Bézieau, Sandra Mercier, and Odile Boespflug-Tanguy. Acid ceramidase deficiency. Apr 2025. URL: https://doi.org/10.1212/nxg.0000000000200243, doi:10.1212/nxg.0000000000200243. This article has 2 citations.

9. (cuinat2025acidceramidasedeficiency pages 3-4): Silvestre Cuinat, Paul Rollier, Katheryn Grand, Pedro A. Sanchez-Lara, Michelle Allen-Sharpley, Thierry Levade, Marie T. Vanier, Laurence Lion Francois, Nicole Chemaly, Capucine de Lattre, Camille Moreau, Adrien Paquot, Terence Beghyn, Servane de Masfrand, Stéphane Bézieau, Sandra Mercier, and Odile Boespflug-Tanguy. Acid ceramidase deficiency. Apr 2025. URL: https://doi.org/10.1212/nxg.0000000000200243, doi:10.1212/nxg.0000000000200243. This article has 2 citations.

10. (theuriet2024geneticcharacterizationof pages 5-6): Julian Theuriet, Gorka Fernandez-Eulate, Philippe Latour, Tanya Stojkovic, Marion Masingue, Léo Vidoni, Emilien Bernard, Arnaud Jacquier, Laurent Schaeffer, Emmanuelle Salort-Campana, Jean-Baptiste Chanson, Aleksandra Nadaj Pakleza, Anne-Laure Kaminsky, Juliette Svahn, Véronique Manel, Françoise Bouhour, and Antoine Pegat. Genetic characterization of non-5q proximal spinal muscular atrophy in a french cohort: the place of whole exome sequencing. European Journal of Human Genetics, 32:37-43, Jun 2024. URL: https://doi.org/10.1038/s41431-023-01407-8, doi:10.1038/s41431-023-01407-8. This article has 8 citations and is from a domain leading peer-reviewed journal.

11. (theuriet2024geneticcharacterizationof pages 6-7): Julian Theuriet, Gorka Fernandez-Eulate, Philippe Latour, Tanya Stojkovic, Marion Masingue, Léo Vidoni, Emilien Bernard, Arnaud Jacquier, Laurent Schaeffer, Emmanuelle Salort-Campana, Jean-Baptiste Chanson, Aleksandra Nadaj Pakleza, Anne-Laure Kaminsky, Juliette Svahn, Véronique Manel, Françoise Bouhour, and Antoine Pegat. Genetic characterization of non-5q proximal spinal muscular atrophy in a french cohort: the place of whole exome sequencing. European Journal of Human Genetics, 32:37-43, Jun 2024. URL: https://doi.org/10.1038/s41431-023-01407-8, doi:10.1038/s41431-023-01407-8. This article has 8 citations and is from a domain leading peer-reviewed journal.

12. (derome2024[therapeuticperspectivesfor pages 2-3): Marion Derome, Jérôme Denard, Martina Marinello, Thierry Levade, Odile Boespflug-Tanguy, and Ana Buj-Bello. [therapeutic perspectives for lysosomal storage disorders caused by acid ceramidase deficiency]. Medecine sciences : M/S, 40 Hors série n° 1:52-55, Nov 2024. URL: https://doi.org/10.1051/medsci/2024162, doi:10.1051/medsci/2024162. This article has 0 citations.

13. (derome2024[therapeuticperspectivesfor pages 1-2): Marion Derome, Jérôme Denard, Martina Marinello, Thierry Levade, Odile Boespflug-Tanguy, and Ana Buj-Bello. [therapeutic perspectives for lysosomal storage disorders caused by acid ceramidase deficiency]. Medecine sciences : M/S, 40 Hors série n° 1:52-55, Nov 2024. URL: https://doi.org/10.1051/medsci/2024162, doi:10.1051/medsci/2024162. This article has 0 citations.

14. (nishio2024clinicalandgenetic pages 1-2): Hisahide Nishio, Emma Niba, Toshio Saito, Kentaro Okamoto, Tomoko Lee, Yasuhiro Takeshima, Hiroyuki Awano, and Poh-San Lai. Clinical and genetic profiles of 5q- and non-5q-spinal muscular atrophy diseases in pediatric patients. Genes, 15:1294, Sep 2024. URL: https://doi.org/10.3390/genes15101294, doi:10.3390/genes15101294. This article has 14 citations.

15. (cuinat2025acidceramidasedeficiency pages 12-13): Silvestre Cuinat, Paul Rollier, Katheryn Grand, Pedro A. Sanchez-Lara, Michelle Allen-Sharpley, Thierry Levade, Marie T. Vanier, Laurence Lion Francois, Nicole Chemaly, Capucine de Lattre, Camille Moreau, Adrien Paquot, Terence Beghyn, Servane de Masfrand, Stéphane Bézieau, Sandra Mercier, and Odile Boespflug-Tanguy. Acid ceramidase deficiency. Apr 2025. URL: https://doi.org/10.1212/nxg.0000000000200243, doi:10.1212/nxg.0000000000200243. This article has 2 citations.

16. (kleynerman2023acidceramidasedeficiency pages 14-15): Annie Kleynerman, Jitka Rybova, Mary L. Faber, William M. McKillop, Thierry Levade, and Jeffrey A. Medin. Acid ceramidase deficiency: bridging gaps between clinical presentation, mouse models, and future therapeutic interventions. Biomolecules, 13:274, Feb 2023. URL: https://doi.org/10.3390/biom13020274, doi:10.3390/biom13020274. This article has 26 citations.

17. (NCT02298634 chunk 1):  Biomarker for Farber Disease (BioFarber). CENTOGENE GmbH Rostock. 2018. ClinicalTrials.gov Identifier: NCT02298634

18. (kleynerman2023acidceramidasedeficiency pages 1-2): Annie Kleynerman, Jitka Rybova, Mary L. Faber, William M. McKillop, Thierry Levade, and Jeffrey A. Medin. Acid ceramidase deficiency: bridging gaps between clinical presentation, mouse models, and future therapeutic interventions. Biomolecules, 13:274, Feb 2023. URL: https://doi.org/10.3390/biom13020274, doi:10.3390/biom13020274. This article has 26 citations.

## Artifacts

- [Edison artifact artifact-00](Spinal_Muscular_Atrophy_Progressive_Myoclonic_Epilepsy-deep-research-falcon_artifacts/artifact-00.md)