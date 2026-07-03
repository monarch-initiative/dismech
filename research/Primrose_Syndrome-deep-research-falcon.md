---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-04T15:23:58.644029'
end_time: '2026-06-04T15:49:47.129826'
duration_seconds: 1548.49
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Primrose Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 41
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: Primrose_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Primrose_Syndrome-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Primrose Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Primrose Syndrome** covering all of the
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
- **Disease Name:** Primrose Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Primrose Syndrome** covering all of the
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


## Comprehensive Research Report: Primrose Syndrome (Mendelian)

### Target disease
- **Disease name:** Primrose syndrome (PS)
- **Category:** Mendelian / monogenic neurodevelopmental syndrome
- **MONDO ID:** **MONDO:0009798** (as curated in OpenTargets) (OpenTargets Search: Primrose syndrome-ZBTB20)

---

## 1. Disease Information

### 1.1 Concise overview
Primrose syndrome is a rare, typically **de novo autosomal dominant** multisystem disorder characterized by **neurodevelopmental impairment** (developmental delay, intellectual disability, behavioral abnormalities including autism), **postnatal macrocephaly**, characteristic facial features, and a progressive component with **calcification/ossification of the external ears**, **distal muscle wasting**, **contractures**, skeletal abnormalities, and **metabolic/endocrine disturbances** (including altered glucose metabolism/diabetes and thyroid dysfunction). (melis2020primrosesyndromecharacterization pages 2-4, arora2021primrosesyndrome pages 1-3, melis2020primrosesyndromecharacterization pages 1-2)

### 1.2 Key identifiers (with notes on availability)
- **OMIM disease:** **259050** (Primrose syndrome) (arora2021primrosesyndrome pages 10-13, sogukpınar2024anovelzbtb20 pages 1-2)
- **Causal gene OMIM:** **606025** (ZBTB20) (arora2021primrosesyndrome pages 10-13, sogukpınar2024anovelzbtb20 pages 1-2)
- **MONDO:** **MONDO_0009798** (Primrose syndrome) (OpenTargets Search: Primrose syndrome-ZBTB20)
- **Orphanet cross-mapped entity/name used in resources:** **Orphanet_3042** (“Intellectual disability - cataracts - calcified pinnae - myopathy”) (OpenTargets Search: Primrose syndrome-ZBTB20)
- **ICD / MeSH:** not explicitly provided in the retrieved excerpts; would require direct consultation of ICD/MeSH registries (not available in current tool outputs).

### 1.3 Synonyms / alternative names
A commonly used resource synonym is **“Intellectual disability - cataracts - calcified pinnae - myopathy”** (Orphanet_3042), reflecting the characteristic clinical tetrad in some individuals. (OpenTargets Search: Primrose syndrome-ZBTB20)

### 1.4 Evidence provenance
Most knowledge is derived from **aggregated disease-level resources and cohorts** (notably a 42-patient series), plus **individual case reports**—including multiple 2023–2024 publications that expand early-life phenotypes and management experience. (melis2020primrosesyndromecharacterization pages 2-4, li2024noveldenovo pages 1-2, tugci2024cochlearimplantationin pages 2-4)

---

## 2. Etiology

### 2.1 Primary causal factor
Primrose syndrome is caused by heterozygous pathogenic (or likely pathogenic) variants in **ZBTB20**, encoding a BTB–zinc finger transcriptional repressor. (arora2021primrosesyndrome pages 10-13, sogukpınar2024anovelzbtb20 pages 1-2)

### 2.2 Risk factors
- **Genetic:** presence of a pathogenic ZBTB20 variant; most reported cases are **de novo**. (arora2021primrosesyndrome pages 10-13, long2023aninfantwith pages 1-2)
- **Non-genetic/environmental:** no established environmental risk factors were identified in the retrieved literature excerpts.

### 2.3 Protective factors / gene–environment interactions
No protective factors or gene–environment interactions specific to Primrose syndrome were identified in the retrieved evidence.

---

## 3. Phenotypes

### 3.1 Key phenotypic spectrum and frequencies (cohort-based)
The largest consolidated cohort evidence in the retrieved texts is the **42-patient phenotype series**, which provides frequencies for multiple core findings. Examples include:
- Macrocephaly: **29/38 (76%)** (melis2020primrosesyndromecharacterization pages 2-4)
- Moderate–severe intellectual disability: **33/39 (85%)** (melis2020primrosesyndromecharacterization pages 2-4)
- Autism: **20/33 (61%)** (melis2020primrosesyndromecharacterization pages 2-4)
- Hypotonia: **26/34 (76%)** (melis2020primrosesyndromecharacterization pages 2-4)
- External ear calcification: **14/28 (50%) overall**, but **12/12 adults (100%)** where assessed (melis2020primrosesyndromecharacterization pages 2-4)

Phenotypes with strong age-dependence (often emerging in adolescence) include ear calcification, cystic bone lesions, muscle wasting, and contractures. (melis2020primrosesyndromecharacterization pages 1-2)

### 3.2 Age of onset, progression, and severity
A consistent theme across cohort and review sources is **progressive somatic involvement**:
- Cardinal features such as calcification of the external ears, cystic bone lesions, muscle wasting, and contractures **“typically develop between 10 and 16 years of age.”** (melis2020primrosesyndromecharacterization pages 1-2)
- Muscle wasting may first be noticed around **11 years**, and contractures around **10 years**, with progression over time. (melis2020primrosesyndromecharacterization pages 4-7)

### 3.3 Quality of life / functional impact (inferred from clinical course)
Functional impairment can become substantial due to musculoskeletal progression; GeneReviews-style content notes walking difficulty and **eventual wheelchair dependence** in some individuals due to distal wasting and contractures. (arora2021primrosesyndromea pages 6-8)

### 3.4 Suggested HPO terms
A phenotype-to-HPO mapping (including onset and frequency where available) is provided in Artifact 01.

| Phenotype | Suggested HPO term(s) | Onset/course | Frequency/evidence |
|---|---|---|---|
| Macrocephaly / macrocrania | HP:0000256 Macrocephaly | Usually postnatal overgrowth; non-progressive overgrowth pattern recognized from infancy/childhood | 29/38 (76%) in 42-patient cohort; GeneReviews notes postnatal macrocephaly common (melis2020primrosesyndromecharacterization pages 2-4, melis2020primrosesyndromecharacterization pages 8-10, arora2021primrosesyndrome pages 1-3) |
| Intellectual disability | HP:0001249 Intellectual disability | Developmental onset; cognition appears relatively stable, with no clear evidence of decline over time | Moderate-severe ID in 33/39 (85%); mild 16%, moderate-severe 84% in cohort summaries (melis2020primrosesyndromecharacterization pages 2-4, melis2020primrosesyndromecharacterization pages 8-10, melis2020primrosesyndromecharacterization pages 1-2) |
| Developmental delay / psychomotor delay | HP:0001263 Global developmental delay; HP:0011344 Severe global developmental delay (if severe) | Early childhood onset; persistent | All 57 patients in comparative review had ID and/or psychomotor delay; GeneReviews highlights early developmental delay and expressive speech delay (juven2020primrosesyndromea pages 1-2, arora2021primrosesyndrome pages 1-3) |
| Expressive speech delay | HP:0002474 Expressive language delay | Early childhood; major developmental concern requiring early therapy | Frequent, but no firm cohort percentage in extracted text; specifically emphasized in GeneReviews-style management summary (arora2021primrosesyndrome pages 1-3, arora2021primrosesyndrome pages 6-8) |
| Autism spectrum / autistic behavior | HP:0000729 Autism | Childhood onset; behavioral severity variable | Autism in 20/33 (61%) in cohort (melis2020primrosesyndromecharacterization pages 2-4) |
| Hypotonia | HP:0001252 Hypotonia | Typically infancy/childhood; may contribute to motor delay | 26/34 (76%) in cohort (melis2020primrosesyndromecharacterization pages 2-4) |
| Ptosis | HP:0000508 Ptosis | Congenital/childhood, part of characteristic facial gestalt | 20/28 (71%) in cohort (melis2020primrosesyndromecharacterization pages 2-4) |
| Deep-set eyes / characteristic facies | HP:0000490 Deeply set eye; HP:0001999 Facial asymmetry not specifically supported; HP:0000007 Autosomal dominant inheritance not phenotype | Present from childhood; recognizable facial pattern becomes more evident with age | Frequent descriptive feature in recent case reports and GeneReviews summary; no exact percentage in extracted cohort text (sogukpınar2024anovelzbtb20 pages 1-2, arora2021primrosesyndrome pages 1-3) |
| Downslanting palpebral fissures | HP:0000494 Downslanted palpebral fissures | Childhood; part of craniofacial pattern | Common descriptive feature; no exact percentage in extracted text (sogukpınar2024anovelzbtb20 pages 1-2, arora2021primrosesyndrome pages 1-3) |
| Sensorineural hearing loss | HP:0000407 Sensorineural hearing impairment | Often prelingual; may become more evident over time; enriched in missense-variant cases | Hearing loss common: 21/27 children and 12/13 adults in GeneReviews summary; significantly more frequent with missense variants vs deletions/truncating variants (arora2021primrosesyndromea pages 6-8, juven2020primrosesyndromea pages 1-2, tugci2024cochlearimplantationin pages 2-4) |
| Calcification/ossification of external ears | HP:0008608 Calcification of pinna; HP:0011397 Abnormal external ear cartilage (broader fallback) | Typically develops in later childhood/adolescence; one of the hallmark progressive signs | 14/28 (50%) overall and 12/12 (100%) adults in cohort; cardinal features usually emerge between 10-16 years (melis2020primrosesyndromecharacterization pages 2-4, melis2020primrosesyndromecharacterization pages 1-2) |
| Distal muscle wasting / distal amyotrophy | HP:0003699 Amyotrophy; HP:0008947 Distal amyotrophy | Usually first noticed around age 11; progressive with age | Progressive; clear age-related increase in cohort, first noticed around age 11 (melis2020primrosesyndromecharacterization pages 4-7) |
| Joint contractures | HP:0001371 Flexion contracture; HP:0002829 Arthrogryposis multiplex congenita not supported | Typically begins around age 10; progressive | Appears in later childhood/adolescence; worsens with age (melis2020primrosesyndromecharacterization pages 4-7) |
| Ataxia / gait difficulty | HP:0001251 Ataxia; HP:0001288 Gait disturbance | Rare; may be progressive in some individuals | Reported in subset only; GeneReviews notes progressive musculoskeletal impairment can lead to walking difficulty and eventual wheelchair dependence (arora2021primrosesyndrome pages 6-8, arora2021primrosesyndromea pages 6-8) |
| Seizures | HP:0001250 Seizure | Variable onset; monitor clinically for new seizures | 6/29 (21%) in cohort (melis2020primrosesyndromecharacterization pages 2-4) |
| Corpus callosum anomaly / dysgenesis | HP:0001273 Agenesis of corpus callosum; HP:0006989 Dysgenesis of corpus callosum | Congenital/early neuroimaging finding | More frequent in missense SNV group; ~20% reported in recent review/case synthesis (juven2020primrosesyndromea pages 1-2, li2024noveldenovo pages 5-7, long2023aninfantwith pages 1-2) |
| Cataract | HP:0000518 Cataract | Often later-onset; may become apparent in puberty/adulthood | Adult-enriched feature; included among age-related manifestations in cohort and reviews (melis2020primrosesyndromecharacterization pages 1-2, melis2020primrosesyndromecharacterization pages 8-10, arora2021primrosesyndromea pages 6-8) |
| Disturbed glucose metabolism / diabetes mellitus | HP:0003074 Hyperglycemia; HP:0000819 Diabetes mellitus | Usually later childhood/adulthood; progressive metabolic monitoring recommended | Considered a cardinal biochemical feature; adults may require oral hypoglycemics and/or insulin (melis2020primrosesyndromecharacterization pages 8-10, arora2021primrosesyndromea pages 6-8, arora2021primrosesyndromea pages 10-13) |
| Elevated alpha-fetoprotein | HP:0005914 Increased circulating alpha-fetoprotein level | Can be elevated from infancy and may persist without clear age-related trend in some individuals | 9/18 (50%) overall in cohort; 4/11 and 5/7 in subgroups (melis2020primrosesyndromecharacterization pages 4-7) |
| Anemia | HP:0001903 Anemia | Variable; part of biochemical phenotype, may warrant repeated monitoring | 5/21 (24%) overall in cohort (melis2020primrosesyndromecharacterization pages 4-7, melis2020primrosesyndromecharacterization pages 1-2) |
| Sparse body hair | HP:0008070 Sparse body hair | More recognizable with age/adulthood | Described as characteristic adult feature; no exact percentage in extracted text (melis2020primrosesyndromecharacterization pages 1-2, arora2021primrosesyndromea pages 6-8) |
| Cryptorchidism | HP:0000028 Cryptorchidism | Congenital/childhood in affected males | About half of affected males in GeneReviews summary (sogukpınar2024anovelzbtb20 pages 1-2, arora2021primrosesyndromea pages 6-8) |
| Hypothyroidism | HP:0000821 Hypothyroidism | Congenital or childhood-onset in subset; endocrine surveillance recommended | Rare overall but enriched in missense-variant group in comparative study; several cases reported in recent review (juven2020primrosesyndromea pages 1-2, li2024noveldenovo pages 1-2, arora2021primrosesyndromea pages 6-8) |
| Behavioral dysregulation / aggression / self-injury | HP:0000708 Behavioral abnormality; HP:0000734 Stereotypy; HP:0000742 Self-injurious behavior | Childhood to adolescence; variable severity | Common behavioral phenotype in GeneReviews; severe case showed response to sertraline in 2024 report (arora2021primrosesyndrome pages 1-3, moon2024resolutionofsevere pages 1-2) |


*Table: This table maps major Primrose syndrome manifestations to suggested HPO terms with onset/progression notes and frequency data where available, mainly from the 42-patient cohort and GeneReviews-style summary. It is useful for disease knowledge base curation and phenotype annotation.*

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene
- **ZBTB20** (BTB-ZF transcriptional repressor). (arora2021primrosesyndrome pages 10-13, stellacci2018clinicalandfunctional pages 13-16)

### 4.2 Pathogenic variants (classes and location)
Across case reports and cohort summaries, most disease-causing ZBTB20 variants are reported as **de novo** and frequently **missense variants in C-terminal C2H2 zinc-finger motifs**, consistent with disruption of DNA binding and/or dominant-negative behavior. (sogukpınar2024anovelzbtb20 pages 1-2, juven2020primrosesyndromea pages 1-2)

Recent variant examples (2023–2024):
- **c.1916G>A (p.Cys639Tyr)** (de novo) in a 2024 behavioral-treatment case. (moon2024resolutionofsevere pages 1-2)
- **c.1948A>C (p.Asn650His)** (de novo) in an early-childhood presentation. (sogukpınar2024anovelzbtb20 pages 1-2)
- **c.1927T>A (p.Phe643Ile)** (de novo), classified **ACMG “likely pathogenic”** with PS2 + PM2_supporting + PP3 + PP4. (li2024noveldenovo pages 5-7)
- A reported **frameshift/truncating** variant **c.1038dup (p.Ile347AspfsTer23)** identified by fetal exome sequencing in a prenatal diagnosis report, illustrating that non-missense loss-of-function alleles can also occur in published cases (though classic Primrose syndrome is enriched for missense ZnF variants). (long2023aninfantwith pages 1-2)

### 4.3 Variant mechanism (dominant-negative vs haploinsufficiency)
Multiple sources suggest that a **dominant-negative mechanism** is plausible/likely for many missense zinc-finger variants:
- A GeneReviews-style summary explicitly states: **“A dominant-negative mechanism has been proposed.”** (arora2021primrosesyndrome pages 10-13)
- Functional work showed mutant ZBTB20 proteins localize to the nucleus but are not stably chromatin bound and **reduce DNA binding even when co-expressed with wild-type**, supporting interference with normal function. (stellacci2018clinicalandfunctional pages 13-16)
- Genotype–phenotype comparisons report that missense SNVs are associated with more progressive multisystem involvement (hearing loss, ectopic calcifications, muscle wasting/contractures) than 3q13.31 deletions/truncating variants, consistent with stronger dominant-negative effects for some missense alleles. (juven2020primrosesyndromea pages 1-2)

### 4.4 Epigenetics, chromosomal abnormalities, modifier genes
- **Chromosomal abnormality context:** 3q13.31 microdeletions that include ZBTB20 can produce overlapping phenotypes and are used in differential diagnosis comparisons. (juven2020primrosesyndromea pages 1-2, long2023aninfantwith pages 6-7)
- No Primrose syndrome–specific modifier genes or epigenetic disease drivers were identified in the retrieved evidence.

---

## 5. Environmental Information
No disease-specific environmental, lifestyle, or infectious triggers were identified in the retrieved evidence; Primrose syndrome is primarily genetic in etiology. (arora2021primrosesyndrome pages 10-13, sogukpınar2024anovelzbtb20 pages 1-2)

---

## 6. Mechanism / Pathophysiology

### 6.1 Molecular function and upstream lesion
ZBTB20 is a **BTB-ZF transcriptional repressor** with an N-terminal BTB domain (protein–protein interactions) and C-terminal C2H2 zinc fingers (DNA binding). (arora2021primrosesyndrome pages 10-13, arora2021primrosesyndromea pages 10-13)

### 6.2 AFP dysregulation (liver transcriptional repression)
A proposed mechanism for a characteristic biomarker is that ZBTB20 normally represses AFP expression in liver; ZBTB20 dysfunction **“leads to the unblocking of AFP synthesis in the liver (normally, the gene acts as a repressor)”** leading to elevated serum AFP in Primrose syndrome. (głowskaciemny2023roleofalphafetoprotein pages 3-4, głowskaciemny2023roleofalphafetoprotein pages 4-6)

### 6.3 Neurodevelopmental mechanisms
Neurodevelopmental disorder mechanisms are supported by animal and cellular neurobiology work:
- ZBTB20 perturbation affects hippocampal development and CA1 pyramidal neuron maturation; RNAi downregulation in mouse hippocampus reduces apical dendritic arborization, and genetic models show hippocampal circuit defects. (jones2018neurodevelopmentaldisorderassociatedzbtb20 pages 1-2)
- Cultured neuron experiments show ZBTB20 variants can alter dendritic spine morphology and dendritic arborization/length, providing a plausible substrate for cognition/behavior phenotypes. (jones2018neurodevelopmentaldisorderassociatedzbtb20 pages 1-2)

### 6.4 Metabolic mechanisms
Clinical biochemical patterns and mechanistic studies link ZBTB20 to metabolic homeostasis:
- Clinically, “unexplained anemia, disturbed glucose metabolism, and increased AFP levels are cardinal features of PS,” and metabolic investigations suggest disturbed mitochondrial fatty-acid oxidation with abnormal acylcarnitines and urine organic acids in a subset. (melis2020primrosesyndromecharacterization pages 8-10, melis2020primrosesyndromecharacterization pages 4-7)
- Functional and review evidence links ZBTB20 to regulation of metabolic genes and β-cell function relevant to glucose homeostasis. (stellacci2018clinicalandfunctional pages 13-16)

### 6.5 Dominant-negative functional evidence
Functional assays in a Primrose-syndrome–relevant context found that ZnF-region substitutions can disrupt DNA contacts (loss of a DNA-backbone hydrogen bond) and reduce chromatin binding/DNA binding to an AFP promoter oligo, consistent with a transcriptional dysregulation mechanism and dominant-negative interference with wild-type protein. (stellacci2018clinicalandfunctional pages 13-16)

### 6.6 Suggested ontology terms
- **GO biological processes (suggested):** regulation of transcription by RNA polymerase II; neurogenesis; regulation of neuron differentiation; regulation of glucose metabolic process; lipid metabolic process.
- **CL cell types (suggested):** cortical pyramidal neuron; hippocampal CA1 pyramidal neuron; astrocyte; pancreatic beta cell; hepatocyte.

(These ontology suggestions are aligned with functional roles reported in mechanistic evidence but are not explicitly enumerated in the retrieved excerpts.) (stellacci2018clinicalandfunctional pages 13-16, jones2018neurodevelopmentaldisorderassociatedzbtb20 pages 1-2)

---

## 7. Anatomical Structures Affected

### 7.1 Organ systems (high-confidence)
- **Central nervous system:** neurodevelopmental impairment, corpus callosum anomalies, seizures in a subset. (melis2020primrosesyndromecharacterization pages 2-4, long2023aninfantwith pages 1-2)
- **Auditory system:** sensorineural hearing loss; cochlear implantation has been performed in at least one reported patient. (tugci2024cochlearimplantationin pages 2-4)
- **Musculoskeletal system:** distal muscle wasting, contractures, skeletal abnormalities; potential wheelchair dependence. (arora2021primrosesyndromea pages 6-8, melis2020primrosesyndromecharacterization pages 4-7)
- **Endocrine/metabolic:** disturbed glucose metabolism/diabetes; hypothyroidism in some cases. (melis2020primrosesyndromecharacterization pages 8-10, arora2021primrosesyndromea pages 6-8)
- **Liver (biomarker biology):** AFP dysregulation plausibly arises from hepatic transcriptional derepression. (głowskaciemny2023roleofalphafetoprotein pages 3-4)

### 7.2 Suggested UBERON terms (examples)
- Hippocampus, cerebral cortex, corpus callosum, cochlea/inner ear, skeletal muscle, testis, liver, pancreas.

---

## 8. Temporal Development

- **Early/childhood:** macrocephaly, developmental delay, hypotonia, facial gestalt, early hearing loss. (melis2020primrosesyndromecharacterization pages 2-4, arora2021primrosesyndromea pages 6-8)
- **Puberty/adolescence:** hallmark progression—ear calcification, cystic bone lesions, muscle wasting, contractures—often emerges 10–16 years. (melis2020primrosesyndromecharacterization pages 1-2)
- **Adulthood:** cataracts, diabetes, sparse body hair, testicular tumor risk may become relevant; recognition is often easier in adults. (melis2020primrosesyndromecharacterization pages 8-10, melis2020primrosesyndromecharacterization pages 10-11)

---

## 9. Inheritance and Population

### 9.1 Inheritance
Primrose syndrome is **autosomal dominant**, and most reported probands are **de novo**. (arora2021primrosesyndrome pages 10-13, long2023aninfantwith pages 1-2)

### 9.2 Recurrence risk / mosaicism
If the pathogenic variant is present in an affected parent, recurrence risk to sibs is 50%; if parental leukocyte testing is negative, sib recurrence risk is estimated ~1% due to possible germline mosaicism. (arora2021primrosesyndrome pages 10-13, arora2021primrosesyndromea pages 10-13)

### 9.3 Epidemiology
Robust incidence/prevalence data are not available from the extracted primary cohort excerpts; one review-style AFP paper cites a rough prevalence of ~1:1,000,000 births. (głowskaciemny2023roleofalphafetoprotein pages 3-4)

---

## 10. Diagnostics

### 10.1 Clinical recognition and key supportive findings
Clinical suspicion is raised by the combination of neurodevelopmental impairment, macrocephaly/overgrowth, hearing loss, progressive ear calcification and muscle wasting/contractures, and supportive biochemical features (AFP elevation, anemia, glucose dysregulation, occasional metabolic profiling abnormalities). (melis2020primrosesyndromecharacterization pages 2-4, melis2020primrosesyndromecharacterization pages 8-10)

### 10.2 Genetic testing strategy (recommended approaches)
A GeneReviews-style diagnostic workflow includes:
- **Single-gene testing** of **ZBTB20** (sequence analysis), followed by **deletion/duplication analysis** if negative.
- Alternatively, **multigene panels** for intellectual disability that include ZBTB20, or **exome/genome sequencing** when the phenotype is nonspecific.
- ACMG/AMP interpretation: **pathogenic/likely pathogenic** variants are diagnostic; **VUS** does not establish/exclude diagnosis. (arora2021primrosesyndrome pages 1-3)

Recent real-world implementations include trio whole-exome sequencing with Sanger confirmation and CNV testing (CNV-seq). (li2024noveldenovo pages 5-7)

### 10.3 Differential diagnosis
Differentials explicitly mentioned include **3q13.31 microdeletion syndrome** (including ZBTB20), **Fragile X syndrome**, and **DiGeorge syndrome**, reflecting overlapping neurodevelopmental phenotypes. (long2023aninfantwith pages 6-7)

---

## 11. Outcome / Prognosis

### 11.1 Overall course
Primrose syndrome is progressive for many somatic features (muscle wasting, contractures, calcifications), but available cohort evidence suggests no clear progressive cognitive decline: cognition “does not seem to decline with age,” though detailed longitudinal testing is limited. (melis2020primrosesyndromecharacterization pages 8-10)

### 11.2 Longevity / life expectancy
Longitudinal outcome data are limited; the **oldest reported individual is 53 years** in GeneReviews-style and case report summaries. (arora2021primrosesyndromea pages 6-8, long2023aninfantwith pages 6-7)

### 11.3 Complications impacting prognosis
- **Mobility disability:** progressive distal muscle wasting and contractures can lead to walking difficulty and eventual wheelchair dependence. (arora2021primrosesyndromea pages 6-8)
- **Tumors:** testicular tumors have been reported in adult males; tumor-related mortality occurred in the cohort (“the two males with PS who developed testicular tumors have died because of their tumors”). (melis2020primrosesyndromecharacterization pages 8-10)

### 11.4 Quality of life proxy outcomes from interventions
A 2024 case report indicates substantial sustained improvement in severe neurobehavioral symptoms with sertraline (resolution within 2 weeks; persisted >2 years), enabling better participation in therapy and schooling (functional benefit). (moon2024resolutionofsevere pages 2-2)

---

## 12. Treatment

### 12.1 Current standard of care (supportive)
No disorder-specific disease-modifying treatment is established; management is **multidisciplinary supportive care**, including early intervention (speech/OT/PT), educational planning, behavioral assessment, seizure monitoring and standard ASM use when indicated, orthopedics/rehabilitation for musculoskeletal complications, audiology monitoring and hearing aids, and endocrine surveillance/management (glucose/HbA1c beginning ~age 7; thyroid monitoring). (arora2021primrosesyndrome pages 8-10, arora2021primrosesyndromea pages 10-13)

### 12.2 Real-world implementations (2024)
- **SSRI for neurobehavioral symptoms:** A single-case report described resolution of severe aggression/irritability/mood lability with **sertraline** (started 25 mg daily; improvement in 2 weeks; later increased to 50 mg; sustained benefit >2 years). (moon2024resolutionofsevere pages 2-2, moon2024resolutionofsevere pages 1-2)
- **Cochlear implantation:** A child underwent unilateral cochlear implantation (Nucleus CI422) after unsuccessful hearing-aid trial, with 3-month post-op PTA ~40 dB and emerging 1–3 word sentences. (tugci2024cochlearimplantationin pages 2-4)

### 12.3 MAXO suggestions (examples)
- Hearing evaluation; hearing aid therapy; cochlear implantation; speech therapy; occupational therapy; physical therapy; behavioral therapy; SSRI pharmacotherapy; endocrine monitoring; diabetes pharmacotherapy.

(These MAXO suggestions are based on interventions described in the clinical evidence and are provided for knowledge base mapping.) (arora2021primrosesyndrome pages 8-10, tugci2024cochlearimplantationin pages 2-4, moon2024resolutionofsevere pages 2-2)

### 12.4 Clinical trials
A clinical trials search returned no clearly Primrose syndrome/ZBTB20-targeted interventional trials in the retrieved set; listed trials were unrelated false positives (e.g., “primrose oil”).

---

## 13. Prevention
Primrose syndrome is genetic; therefore prevention is primarily **reproductive/genetic**:
- **Genetic counseling** with recurrence risk assessment.
- **Prenatal and preimplantation genetic testing** are possible once the familial ZBTB20 pathogenic variant is known. (arora2021primrosesyndrome pages 10-13, arora2021primrosesyndromea pages 10-13)

Secondary/tertiary prevention focuses on anticipatory surveillance: audiology, glucose/HbA1c, thyroid function, musculoskeletal monitoring, and in adult males consideration of testicular tumor vigilance (though no standardized TGCT surveillance protocol exists). (arora2021primrosesyndromea pages 10-13, melis2020primrosesyndromecharacterization pages 8-10)

---

## 14. Other Species / Natural Disease
No naturally occurring veterinary/other-species disease equivalent was identified in the retrieved evidence; however, multiple **mouse experimental models** of Zbtb20 perturbation exist that inform neurodevelopmental mechanisms. (jones2018neurodevelopmentaldisorderassociatedzbtb20 pages 1-2)

---

## 15. Model Organisms
Experimental evidence relevant to Primrose syndrome mechanisms includes:
- **Mouse genetic perturbation / transgenic expression:** Zbtb20 deletion or ectopic expression affects hippocampal development and cortical lamination; CA1 pyramidal neuron maturation is sensitive to Zbtb20 downregulation. (jones2018neurodevelopmentaldisorderassociatedzbtb20 pages 1-2)
- **In vitro/cell-based functional assays:** mutant ZBTB20 proteins show impaired chromatin/DNA binding and interference with wild-type binding, supporting dominant-negative effects. (stellacci2018clinicalandfunctional pages 13-16)

---

## Recent developments and “latest research” emphasis (2023–2024)
The most clinically actionable 2023–2024 developments in the retrieved literature are:
1. **Medication response report:** sertraline leading to sustained resolution of severe neurobehavioral symptoms (2024). (moon2024resolutionofsevere pages 2-2)
2. **Device-based intervention:** first reported cochlear implantation experience in Primrose syndrome with short-term audiologic/language gains (2024). (tugci2024cochlearimplantationin pages 2-4)
3. **Expanded early-life recognition and prenatal diagnosis:** fetal exome sequencing with prenatal imaging features and novel truncating variant (2023), and additional infant/toddler cases with early features before classic adolescence-onset signs (2024). (long2023aninfantwith pages 1-2, sogukpınar2024anovelzbtb20 pages 1-2)
4. **Variant spectrum and ACMG-coded interpretation:** first Chinese case with de novo p.F643I, classified likely pathogenic with explicit ACMG evidence codes (2024). (li2024noveldenovo pages 5-7)

---

## High-yield summary table (identifiers, phenotypes, biomarkers, and 2023–2024 cases)

| Category | Item | Details/statistics | Key sources (author-year) | URL/DOI if available |
|---|---|---|---|---|
| Identifiers / synonyms | Primrose syndrome | Rare autosomal dominant multisystem neurodevelopmental syndrome caused by **ZBTB20** variants; major identifiers include **OMIM 259050** and **MONDO: MONDO_0009798** (arora2021primrosesyndrome pages 10-13, OpenTargets Search: Primrose syndrome-ZBTB20) | Arora 2021; OpenTargets | OMIM: https://omim.org/entry/259050 |
| Identifiers / synonyms | Causal gene | **ZBTB20** (**OMIM 606025**), BTB-zinc finger transcriptional repressor; disease-target association supported in curated disease resources (arora2021primrosesyndrome pages 10-13, OpenTargets Search: Primrose syndrome-ZBTB20) | Arora 2021; OpenTargets | OMIM: https://omim.org/entry/606025 |
| Identifiers / synonyms | Synonym / Orphanet-linked label | Orphanet-linked disease name: **Intellectual disability - cataracts - calcified pinnae - myopathy**; OpenTargets maps this to **Orphanet_3042** and Primrose syndrome to MONDO_0009798 (OpenTargets Search: Primrose syndrome-ZBTB20) | OpenTargets | https://platform.opentargets.org |
| Epidemiology | Reported rarity | Review source cites prevalence around **~1:1,000,000 births**; evidence base remains sparse and largely case-report/cohort-based (głowskaciemny2023roleofalphafetoprotein pages 3-4) | Głowska-Ciemny 2023 | https://doi.org/10.3390/cancers15174302 |
| Core phenotype | Macrocephaly / head circumference >2 SD | **29/38 (76%)** in 42-patient cohort; often postnatal overgrowth pattern (melis2020primrosesyndromecharacterization pages 2-4) | Melis 2020 | https://doi.org/10.1111/cge.13749 |
| Core phenotype | Intellectual disability | Moderate-severe ID in **33/39 (85%)**; overall literature review also notes all 57 compared patients had ID and/or psychomotor delay (melis2020primrosesyndromecharacterization pages 2-4, juven2020primrosesyndromea pages 1-2) | Melis 2020; Juven 2020 | https://doi.org/10.1111/cge.13749 ; https://doi.org/10.1038/s41431-020-0582-3 |
| Core phenotype | Autism / behavioral abnormalities | Autism reported in **20/33 (61%)**; severe neurobehavioral dysregulation can occur in adolescence (melis2020primrosesyndromecharacterization pages 2-4, moon2024resolutionofsevere pages 1-2) | Melis 2020; Moon 2024 | https://doi.org/10.1111/cge.13749 ; https://doi.org/10.1002/ajmg.a.63610 |
| Core phenotype | Hypotonia | **26/34 (76%)** in cohort, typically early-life/childhood manifestation (melis2020primrosesyndromecharacterization pages 2-4) | Melis 2020 | https://doi.org/10.1111/cge.13749 |
| Core phenotype | Ptosis / facial gestalt | Ptosis in **20/28 (71%)**; characteristic face includes deep-set eyes, ptosis, narrow/downslanting palpebral fissures, depressed nasal bridge (melis2020primrosesyndromecharacterization pages 2-4, sogukpınar2024anovelzbtb20 pages 1-2) | Melis 2020; Soğukpınar 2024 | https://doi.org/10.1111/cge.13749 ; https://doi.org/10.1159/000537952 |
| Core phenotype | Hearing loss | Common and often prelingual; GeneReviews-style summary: **21/27 children** and **12/13 adults** affected; missense cases more frequently affected than deletion/truncating groups (arora2021primrosesyndromea pages 6-8, juven2020primrosesyndromea pages 1-2) | Arora 2021; Juven 2020 | GeneReviews chapter; https://doi.org/10.1038/s41431-020-0582-3 |
| Core phenotype | External ear calcification | **14/28 (50%)** overall, but **12/12 (100%) adults** in cohort where assessed; highly age-dependent (melis2020primrosesyndromecharacterization pages 2-4) | Melis 2020 | https://doi.org/10.1111/cge.13749 |
| Core phenotype | Seizures | **6/29 (21%)** in cohort (melis2020primrosesyndromecharacterization pages 2-4) | Melis 2020 | https://doi.org/10.1111/cge.13749 |
| Age of onset / progression | Cardinal progressive features | Calcified ears, cystic bone lesions, muscle wasting, and contractures typically emerge **between 10 and 16 years**; syndrome is progressive somatically but cognition does not clearly worsen (melis2020primrosesyndromecharacterization pages 1-2) | Melis 2020 | https://doi.org/10.1111/cge.13749 |
| Age of onset / progression | Muscle wasting / contractures | Muscle wasting first noted around **11 years** and contractures around **10 years**, both increasing with age (melis2020primrosesyndromecharacterization pages 4-7) | Melis 2020 | https://doi.org/10.1111/cge.13749 |
| Biochemical markers | Elevated alpha-fetoprotein (AFP) | Elevated in **9/18 (50%)** overall; subgroup breakdown **4/11 (36%)** and **5/7 (71%)**; reported as often persistent over time (melis2020primrosesyndromecharacterization pages 4-7) | Melis 2020 | https://doi.org/10.1111/cge.13749 |
| Biochemical markers | AFP mechanism | Proposed mechanism: **ZBTB20 normally represses hepatic AFP transcription**; loss/dysfunction may “unblock” AFP synthesis (głowskaciemny2023roleofalphafetoprotein pages 3-4) | Głowska-Ciemny 2023 | https://doi.org/10.3390/cancers15174302 |
| Biochemical markers | Anemia | **5/21 (24%)** overall; subgroup counts **4/16 (25%)** and **1/5 (20%)** (melis2020primrosesyndromecharacterization pages 4-7) | Melis 2020 | https://doi.org/10.1111/cge.13749 |
| Biochemical markers | Glucose dysregulation | Disturbed glucose metabolism is a cardinal biochemical feature; adults may develop diabetes requiring oral agents and/or insulin (melis2020primrosesyndromecharacterization pages 8-10, arora2021primrosesyndromea pages 6-8) | Melis 2020; Arora 2021 | https://doi.org/10.1111/cge.13749 ; GeneReviews chapter |
| Biochemical markers | Metabolic profiling / FAO signature | Abnormal acylcarnitines and urine organic acids reported in some patients, suggesting **disturbed mitochondrial fatty-acid oxidation** (melis2020primrosesyndromecharacterization pages 4-7, melis2020primrosesyndromecharacterization pages 1-2) | Melis 2020 | https://doi.org/10.1111/cge.13749 |
| Recent case report (2023) | Prenatal diagnosis with novel truncating variant | Fetal US/MRI showed corpus callosum agenesis/colpocephaly; fetal exome identified **heterozygous c.1038dup (p.Ile347AspfsTer23)**, de novo/likely pathogenic; highlights prenatal genomic diagnosis (long2023aninfantwith pages 1-2) | Long 2023 | https://doi.org/10.7759/cureus.46546 |
| Recent case report (2024) | Sertraline for severe neurobehavioral symptoms | 17-year-old with de novo **c.1916G>A (p.C639Y)** had aggression, irritability, mood lability refractory to guanfacine/aripiprazole; **sertraline 25 mg/day** led to marked resolution within **2 weeks**, later increased to 50 mg/day, with benefit persisting **>2 years** (moon2024resolutionofsevere pages 2-2, moon2024resolutionofsevere pages 1-2) | Moon 2024 | https://doi.org/10.1002/ajmg.a.63610 |
| Recent case report (2024) | Cochlear implantation | Child with Primrose syndrome and bilateral sensorineural hearing loss underwent unilateral **Nucleus CI422** implantation at age 2 after failed 6-month hearing-aid trial; at **3 months** post-op free-field PTA **40 dB**, basic 1–3 word sentences, near-continuous device use (tugci2024cochlearimplantationin pages 2-4) | Tuğci 2024 | https://doi.org/10.4274/tao.2023.2023-4-5 |
| Recent case report (2024) | Novel infant presentation | 14-month-old girl with de novo **c.1948A>C (p.Asn650His)**; hearing loss and neurodevelopmental findings present before classic later-onset features such as ear calcification or muscle atrophy (sogukpınar2024anovelzbtb20 pages 1-2) | Soğukpınar 2024 | https://doi.org/10.1159/000537952 |
| Recent case report (2024) | First Chinese case / ACMG-classified variant | 5-year-old boy with agenesis of corpus callosum, macrocephaly, motor/speech delay, mild ID, autistic behavior; trio WES found de novo **c.1927T>A (p.F643I)** in Zn-finger domain, ACMG **likely pathogenic** (PS2+PM2_supporting+PP3+PP4) (li2024noveldenovo pages 1-2, li2024noveldenovo pages 5-7) | Li 2024 | https://doi.org/10.1002/mgg3.2304 |
| Management / surveillance | Standard care model | Multidisciplinary supportive care: speech/OT/PT, developmental services, annual audiology, annual fasting/postprandial glucose and HbA1c (starting ~age 7 or earlier if indicated), thyroid assessment, seizure and musculoskeletal monitoring; no disorder-specific guidelines yet (arora2021primrosesyndrome pages 8-10, arora2021primrosesyndromea pages 10-13) | Arora 2021 | GeneReviews chapter |


*Table: This table condenses high-yield identifiers, phenotype frequencies, biochemical markers, and recent 2023-2024 case reports for Primrose syndrome. It is designed as a quick-reference artifact for knowledge base curation and evidence-backed clinical summary writing.*

---

## Notes on evidence gaps
- ICD/MeSH identifiers were not present in the retrieved full-text excerpts.
- Many “statistics” beyond the 42-patient cohort are limited by rarity and publication bias (case reports).
- No disease-modifying therapy trials were identified in the clinical trial query results.

---

## Key source URLs (publication dates)
- Melis et al., *Clinical Genetics* (Apr 2020): https://doi.org/10.1111/cge.13749 (melis2020primrosesyndromecharacterization pages 2-4)
- Juven et al., *Eur J Hum Genet* (Feb 2020): https://doi.org/10.1038/s41431-020-0582-3 (juven2020primrosesyndromea pages 1-2)
- Arora et al., GeneReviews-style chapter (2021): (URL not provided in retrieved excerpt) (arora2021primrosesyndrome pages 10-13)
- Long et al., *Cureus* (Oct 2023): https://doi.org/10.7759/cureus.46546 (long2023aninfantwith pages 1-2)
- Głowska-Ciemny et al., *Cancers* (Aug 2023): https://doi.org/10.3390/cancers15174302 (głowskaciemny2023roleofalphafetoprotein pages 3-4)
- Moon et al., *Am J Med Genet A* (Mar 2024): https://doi.org/10.1002/ajmg.a.63610 (moon2024resolutionofsevere pages 1-2)
- Soğukpınar et al., *Molecular Syndromology* (Mar 2024): https://doi.org/10.1159/000537952 (sogukpınar2024anovelzbtb20 pages 1-2)
- Tuğci et al., *Turkish Archives of Otorhinolaryngology* (Dec 2024): https://doi.org/10.4274/tao.2023.2023-4-5 (tugci2024cochlearimplantationin pages 2-4)
- Li et al., *Molecular Genetics & Genomic Medicine* (Dec 2024): https://doi.org/10.1002/mgg3.2304 (li2024noveldenovo pages 1-2)



References

1. (OpenTargets Search: Primrose syndrome-ZBTB20): Open Targets Query (Primrose syndrome-ZBTB20, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (melis2020primrosesyndromecharacterization pages 2-4): Daniela Melis, Daniel Carvalho, Tina Barbaro‐Dieber, Alberto J. Espay, Michael J. Gambello, Blanca Gener, Erica Gerkes, Marrit M. Hitzert, Hanne B. Hove, Sandra Jansen, Petr E. Jira, Katherine Lachlan, Leonie A. Menke, Vinodh Narayanan, Damara Ortiz, Eline Overwater, Renata Posmyk, Keri Ramsey, Alessandro Rossi, Renata Lazari Sandoval, Constance Stumpel, Kyra E. Stuurman, Viviana Cordeddu, Peter Turnpenny, Pietro Strisciuglio, Marco Tartaglia, Sheela Unger, Todd Waters, Clare Turnbull, and Raoul C. Hennekam. Primrose syndrome: characterization of the phenotype in 42 patients. Clinical Genetics, 97:890-901, Apr 2020. URL: https://doi.org/10.1111/cge.13749, doi:10.1111/cge.13749. This article has 38 citations and is from a peer-reviewed journal.

3. (arora2021primrosesyndrome pages 1-3): V Arora, CR Ferreira, RD Puri, and IC Verma. Primrose syndrome. Unknown journal, 2021.

4. (melis2020primrosesyndromecharacterization pages 1-2): Daniela Melis, Daniel Carvalho, Tina Barbaro‐Dieber, Alberto J. Espay, Michael J. Gambello, Blanca Gener, Erica Gerkes, Marrit M. Hitzert, Hanne B. Hove, Sandra Jansen, Petr E. Jira, Katherine Lachlan, Leonie A. Menke, Vinodh Narayanan, Damara Ortiz, Eline Overwater, Renata Posmyk, Keri Ramsey, Alessandro Rossi, Renata Lazari Sandoval, Constance Stumpel, Kyra E. Stuurman, Viviana Cordeddu, Peter Turnpenny, Pietro Strisciuglio, Marco Tartaglia, Sheela Unger, Todd Waters, Clare Turnbull, and Raoul C. Hennekam. Primrose syndrome: characterization of the phenotype in 42 patients. Clinical Genetics, 97:890-901, Apr 2020. URL: https://doi.org/10.1111/cge.13749, doi:10.1111/cge.13749. This article has 38 citations and is from a peer-reviewed journal.

5. (arora2021primrosesyndrome pages 10-13): V Arora, CR Ferreira, RD Puri, and IC Verma. Primrose syndrome. Unknown journal, 2021.

6. (sogukpınar2024anovelzbtb20 pages 1-2): Merve Soğukpınar, Beren Karaosmanoğlu, Gülen Eda Utine, Koray Boduroğlu, and Pelin Özlem Şimşek-Kiper. A novel zbtb20 variant in a patient with primrose syndrome: a rare clinical entity with distinctive features. Molecular Syndromology, 15:347-354, Mar 2024. URL: https://doi.org/10.1159/000537952, doi:10.1159/000537952. This article has 0 citations and is from a peer-reviewed journal.

7. (li2024noveldenovo pages 1-2): Jiayi Li, Chuan Zhang, Xinyuan Tian, Bingbo Zhou, Xue Chen, Yupei Wang, Shengju Hao, Ling Hui, and Zhaoyan Meng. Novel de novo mutation in zbtb20 in a chinese primrose syndrome family and a review of the literature. Molecular Genetics & Genomic Medicine, Dec 2024. URL: https://doi.org/10.1002/mgg3.2304, doi:10.1002/mgg3.2304. This article has 1 citations and is from a peer-reviewed journal.

8. (tugci2024cochlearimplantationin pages 2-4): Burak Anıl Tuğci, Alper Gezdirici, Can Berk Aşaroğlu, Ercan Atasoy, İbrahim Sayın, and Zahide Mine Yazıcı. Cochlear implantation in primrose syndrome with a novel zbtb20 gene variant. Turkish Archives of Otorhinolaryngology, 61:192-200, Dec 2024. URL: https://doi.org/10.4274/tao.2023.2023-4-5, doi:10.4274/tao.2023.2023-4-5. This article has 0 citations.

9. (long2023aninfantwith pages 1-2): Calista Long, Barry DeRose, Anthony B Lal, and Elizabeth Imboden. An infant with primrose syndrome: a case report. Cureus, Oct 2023. URL: https://doi.org/10.7759/cureus.46546, doi:10.7759/cureus.46546. This article has 2 citations.

10. (melis2020primrosesyndromecharacterization pages 4-7): Daniela Melis, Daniel Carvalho, Tina Barbaro‐Dieber, Alberto J. Espay, Michael J. Gambello, Blanca Gener, Erica Gerkes, Marrit M. Hitzert, Hanne B. Hove, Sandra Jansen, Petr E. Jira, Katherine Lachlan, Leonie A. Menke, Vinodh Narayanan, Damara Ortiz, Eline Overwater, Renata Posmyk, Keri Ramsey, Alessandro Rossi, Renata Lazari Sandoval, Constance Stumpel, Kyra E. Stuurman, Viviana Cordeddu, Peter Turnpenny, Pietro Strisciuglio, Marco Tartaglia, Sheela Unger, Todd Waters, Clare Turnbull, and Raoul C. Hennekam. Primrose syndrome: characterization of the phenotype in 42 patients. Clinical Genetics, 97:890-901, Apr 2020. URL: https://doi.org/10.1111/cge.13749, doi:10.1111/cge.13749. This article has 38 citations and is from a peer-reviewed journal.

11. (arora2021primrosesyndromea pages 6-8): V Arora, CR Ferreira, RD Puri, and IC Verma. Primrose syndrome. Unknown journal, 2021.

12. (melis2020primrosesyndromecharacterization pages 8-10): Daniela Melis, Daniel Carvalho, Tina Barbaro‐Dieber, Alberto J. Espay, Michael J. Gambello, Blanca Gener, Erica Gerkes, Marrit M. Hitzert, Hanne B. Hove, Sandra Jansen, Petr E. Jira, Katherine Lachlan, Leonie A. Menke, Vinodh Narayanan, Damara Ortiz, Eline Overwater, Renata Posmyk, Keri Ramsey, Alessandro Rossi, Renata Lazari Sandoval, Constance Stumpel, Kyra E. Stuurman, Viviana Cordeddu, Peter Turnpenny, Pietro Strisciuglio, Marco Tartaglia, Sheela Unger, Todd Waters, Clare Turnbull, and Raoul C. Hennekam. Primrose syndrome: characterization of the phenotype in 42 patients. Clinical Genetics, 97:890-901, Apr 2020. URL: https://doi.org/10.1111/cge.13749, doi:10.1111/cge.13749. This article has 38 citations and is from a peer-reviewed journal.

13. (juven2020primrosesyndromea pages 1-2): Aurélien Juven, Sophie Nambot, Amélie Piton, Nolwenn Jean-Marçais, Alice Masurel, Patrick Callier, Nathalie Marle, Anne-Laure Mosca-Boidron, Paul Kuentz, Christophe Philippe, Martin Chevarin, Yannis Duffourd, Elodie Gautier, Arnold Munnich, Marlène Rio, Sophie Rondeau, Salima El Chehadeh, Élise Schaefer, Bénédicte Gérard, Sonia Bouquillon, Catherine Vincent Delorme, Christine Francannet, Fanny Laffargue, Laetitia Gouas, Bertrand Isidor, Marie Vincent, Sophie Blesson, Fabienne Giuliano, Olivier Pichon, Cédric Le Caignec, Hubert Journel, Laurence Perrin-Sabourin, Jennifer Fabre-Teste, Dominique Martin, Gaelle Vieville, Klaus Dieterich, Didier Lacombe, Anne-Sophie Denommé-Pichon, Christel Thauvin-Robinet, and Laurence Faivre. Primrose syndrome: a phenotypic comparison of patients with a zbtb20 missense variant versus a 3q13.31 microdeletion including zbtb20. European Journal of Human Genetics, 28:1044-1055, Feb 2020. URL: https://doi.org/10.1038/s41431-020-0582-3, doi:10.1038/s41431-020-0582-3. This article has 21 citations and is from a domain leading peer-reviewed journal.

14. (arora2021primrosesyndrome pages 6-8): V Arora, CR Ferreira, RD Puri, and IC Verma. Primrose syndrome. Unknown journal, 2021.

15. (li2024noveldenovo pages 5-7): Jiayi Li, Chuan Zhang, Xinyuan Tian, Bingbo Zhou, Xue Chen, Yupei Wang, Shengju Hao, Ling Hui, and Zhaoyan Meng. Novel de novo mutation in zbtb20 in a chinese primrose syndrome family and a review of the literature. Molecular Genetics & Genomic Medicine, Dec 2024. URL: https://doi.org/10.1002/mgg3.2304, doi:10.1002/mgg3.2304. This article has 1 citations and is from a peer-reviewed journal.

16. (arora2021primrosesyndromea pages 10-13): V Arora, CR Ferreira, RD Puri, and IC Verma. Primrose syndrome. Unknown journal, 2021.

17. (moon2024resolutionofsevere pages 1-2): Young Min Moon, Sa Eun Park, Constance Smith‐Hicks, and Aaron Hauptman. Resolution of severe neurobehavioral difficulties in an individual with primrose syndrome with sertraline. American Journal of Medical Genetics Part A, Mar 2024. URL: https://doi.org/10.1002/ajmg.a.63610, doi:10.1002/ajmg.a.63610. This article has 1 citations.

18. (stellacci2018clinicalandfunctional pages 13-16): Emilia Stellacci, Katharina Steindl, Pascal Joset, Laura Mercurio, Massimiliano Anselmi, Serena Cecchetti, Laura Gogoll, Markus Zweier, Annette Hackenberg, Gianfranco Bocchinfuso, Lorenzo Stella, Marco Tartaglia, and Anita Rauch. Clinical and functional characterization of two novel zbtb20 mutations causing primrose syndrome. Human Mutation, 39:959-964, Jul 2018. URL: https://doi.org/10.1002/humu.23546, doi:10.1002/humu.23546. This article has 21 citations and is from a domain leading peer-reviewed journal.

19. (long2023aninfantwith pages 6-7): Calista Long, Barry DeRose, Anthony B Lal, and Elizabeth Imboden. An infant with primrose syndrome: a case report. Cureus, Oct 2023. URL: https://doi.org/10.7759/cureus.46546, doi:10.7759/cureus.46546. This article has 2 citations.

20. (głowskaciemny2023roleofalphafetoprotein pages 3-4): Joanna Głowska-Ciemny, Marcin Szymanski, Agata Kuszerska, Rafał Rzepka, Constantin S. von Kaisenberg, and Rafał Kocyłowski. Role of alpha-fetoprotein (afp) in diagnosing childhood cancers and genetic-related chronic diseases. Cancers, 15:4302, Aug 2023. URL: https://doi.org/10.3390/cancers15174302, doi:10.3390/cancers15174302. This article has 34 citations.

21. (głowskaciemny2023roleofalphafetoprotein pages 4-6): Joanna Głowska-Ciemny, Marcin Szymanski, Agata Kuszerska, Rafał Rzepka, Constantin S. von Kaisenberg, and Rafał Kocyłowski. Role of alpha-fetoprotein (afp) in diagnosing childhood cancers and genetic-related chronic diseases. Cancers, 15:4302, Aug 2023. URL: https://doi.org/10.3390/cancers15174302, doi:10.3390/cancers15174302. This article has 34 citations.

22. (jones2018neurodevelopmentaldisorderassociatedzbtb20 pages 1-2): Kelly A. Jones, Yue Luo, Lynn Dukes-Rimsky, Deepak P. Srivastava, Richa Koul-Tewari, Theron A. Russell, Lauren P. Shapiro, Anand K. Srivastava, and Peter Penzes. Neurodevelopmental disorder-associated zbtb20 gene variants affect dendritic and synaptic structure. PLoS ONE, 13:e0203760, Oct 2018. URL: https://doi.org/10.1371/journal.pone.0203760, doi:10.1371/journal.pone.0203760. This article has 38 citations and is from a peer-reviewed journal.

23. (melis2020primrosesyndromecharacterization pages 10-11): Daniela Melis, Daniel Carvalho, Tina Barbaro‐Dieber, Alberto J. Espay, Michael J. Gambello, Blanca Gener, Erica Gerkes, Marrit M. Hitzert, Hanne B. Hove, Sandra Jansen, Petr E. Jira, Katherine Lachlan, Leonie A. Menke, Vinodh Narayanan, Damara Ortiz, Eline Overwater, Renata Posmyk, Keri Ramsey, Alessandro Rossi, Renata Lazari Sandoval, Constance Stumpel, Kyra E. Stuurman, Viviana Cordeddu, Peter Turnpenny, Pietro Strisciuglio, Marco Tartaglia, Sheela Unger, Todd Waters, Clare Turnbull, and Raoul C. Hennekam. Primrose syndrome: characterization of the phenotype in 42 patients. Clinical Genetics, 97:890-901, Apr 2020. URL: https://doi.org/10.1111/cge.13749, doi:10.1111/cge.13749. This article has 38 citations and is from a peer-reviewed journal.

24. (moon2024resolutionofsevere pages 2-2): Young Min Moon, Sa Eun Park, Constance Smith‐Hicks, and Aaron Hauptman. Resolution of severe neurobehavioral difficulties in an individual with primrose syndrome with sertraline. American Journal of Medical Genetics Part A, Mar 2024. URL: https://doi.org/10.1002/ajmg.a.63610, doi:10.1002/ajmg.a.63610. This article has 1 citations.

25. (arora2021primrosesyndrome pages 8-10): V Arora, CR Ferreira, RD Puri, and IC Verma. Primrose syndrome. Unknown journal, 2021.

## Artifacts

- [Edison artifact artifact-00](Primrose_Syndrome-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Primrose_Syndrome-deep-research-falcon_artifacts/artifact-01.md)