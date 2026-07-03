---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-16T17:12:54.462446'
end_time: '2026-06-16T17:25:16.196120'
duration_seconds: 741.73
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Central Areolar Choroidal Dystrophy
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
  path: Central_Areolar_Choroidal_Dystrophy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Central Areolar Choroidal Dystrophy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Central Areolar Choroidal Dystrophy** covering all of the
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
- **Disease Name:** Central Areolar Choroidal Dystrophy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Central Areolar Choroidal Dystrophy** covering all of the
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


## Comprehensive Disease Characteristics Report: Central Areolar Choroidal Dystrophy (CACD)

### Target Disease
- **Disease name:** Central areolar choroidal dystrophy (CACD)
- **Category:** Mendelian inherited retinal disease / macular dystrophy
- **Primary evidence base used here:** Aggregated disease-level reviews and cohort studies plus patient/family studies and model organism work (not EHR-only). (camargo2022newinsightson pages 1-2, jeffery2024retinaldystrophiesassociated pages 1-2, seddon2024clinicalandimaging pages 1-2)

| Category | Finding | Details | Evidence |
|---|---|---|---|
| Disease name | Central areolar choroidal dystrophy | Rare hereditary macular dystrophy with bilateral, symmetrical, well-circumscribed loss of choroidal and retinal tissue causing progressive visual loss (camargo2022newinsightson pages 1-2) | (camargo2022newinsightson pages 1-2) |
| Identifier | OMIM | CACD cited as OMIM/MIM 215500 in disease/genetics literature (abeshi2017genetictestingfor pages 3-3, chiang2023electrophysiologicalevaluationof pages 18-18) | (abeshi2017genetictestingfor pages 3-3, chiang2023electrophysiologicalevaluationof pages 18-18) |
| Identifier | Phenotype-specific OMIM subtype | CACD phenotype within PRPH2-associated disease cited as OMIM #613105 in the 2024 PRPH2 cohort paper (jeffery2024retinaldystrophiesassociated pages 2-3) | (jeffery2024retinaldystrophiesassociated pages 2-3) |
| Synonyms/alternate labels | CACD; central areolar chorioretinal dystrophy | 2024 longitudinal PRPH2 cohort describes diffuse RPE atrophy “consistent with central areolar chorioretinal dystrophy (CACD)” (seddon2024clinicalandimaging pages 1-2) | (seddon2024clinicalandimaging pages 1-2) |
| Data source type | Aggregated disease-level resources and patient-level studies | Evidence here derives from systematic review/disease overviews plus family studies, multicenter cohorts, and longitudinal imaging/genetics studies rather than EHR-only sources (camargo2022newinsightson pages 1-2, jeffery2024retinaldystrophiesassociated pages 1-2, seddon2024clinicalandimaging pages 1-2) | (camargo2022newinsightson pages 1-2, jeffery2024retinaldystrophiesassociated pages 1-2, seddon2024clinicalandimaging pages 1-2) |
| Inheritance | Usually autosomal dominant; rare autosomal recessive cases reported | Reviews/testing summaries state CACD is mostly autosomal dominant, with rare recessive inheritance (camargo2022newinsightson pages 1-2, abeshi2017genetictestingfor pages 3-3) | (camargo2022newinsightson pages 1-2, abeshi2017genetictestingfor pages 3-3) |
| Key genes | PRPH2 | Main gene in most published CACD studies; PRPH2 variants are usually implicated in CACD and related macular dystrophies (camargo2022newinsightson pages 6-8, camargo2022newinsightson pages 8-9) | (camargo2022newinsightson pages 6-8, camargo2022newinsightson pages 8-9) |
| Key genes | GUCY2D | Reported CACD gene; example pathogenic missense variant p.Val933Ala / V933A in a Northern Irish family (camargo2022newinsightson pages 6-8, abeshi2017genetictestingfor pages 3-3) | (camargo2022newinsightson pages 6-8, abeshi2017genetictestingfor pages 3-3) |
| Key genes | GUCA1A | Included among CACD-implicated genes; variants such as p.Arg120Leu linked to severe maculopathy including CACD spectrum (camargo2022newinsightson pages 8-9, chen2017guca1amutationcauses pages 9-10) | (camargo2022newinsightson pages 8-9, chen2017guca1amutationcauses pages 9-10) |
| Key genes | CDHR1, ABCA4, TTLL5 | Listed in the 2022 systematic review/network analysis as additional CACD-implicated genes/candidates, though evidence strength varies and ABCA4 attribution was noted as needing validation (camargo2022newinsightson pages 1-2, camargo2022newinsightson pages 8-9) | (camargo2022newinsightson pages 1-2, camargo2022newinsightson pages 8-9) |
| Representative PRPH2 variants | Missense/splice variants linked to CACD | Arg195Leu, Arg172Trp, Arg203Pro, c.828+3A>T; Jeffery et al. note CACD reported with missense changes at codons Arg142, Arg172, Arg195, Ile196, Arg203, Gly208 (camargo2022newinsightson pages 15-16, jeffery2024retinaldystrophiesassociated pages 2-3, seddon2024clinicalandimaging pages 1-2) | (camargo2022newinsightson pages 15-16, jeffery2024retinaldystrophiesassociated pages 2-3, seddon2024clinicalandimaging pages 1-2) |
| Age at onset | Typical disease overview | Onset typically between the 3rd and 5th decades (camargo2022newinsightson pages 1-2) | (camargo2022newinsightson pages 1-2) |
| Age at onset | PRPH2 cohort | Median age at symptom onset across 241 PRPH2 patients was 40 years (range 4–78) (jeffery2024retinaldystrophiesassociated pages 1-2) | (jeffery2024retinaldystrophiesassociated pages 1-2) |
| Clinical course | Progressive | Disease progresses through early parafoveal RPE changes to well-demarcated atrophy and eventual foveal involvement with marked visual loss (camargo2022newinsightson pages 1-2) | (camargo2022newinsightson pages 1-2) |
| Staging | Four clinical stages | Stage 1 parafoveal RPE changes; stage 2 oval/round mildly atrophic hypopigmented area with speckled FAF; stage 3 well-demarcated RPE atrophy outside fovea; stage 4 foveal involvement with severe VA loss, commonly <20/200 (camargo2022newinsightson pages 1-2) | (camargo2022newinsightson pages 1-2) |
| Key clinical features | Macular/RPE/choriocapillaris atrophy | Bilateral central macular atrophy with RPE and choriocapillaris loss; pathology likely photoreceptor-first with secondary RPE/choriocapillaris involvement (camargo2022newinsightson pages 1-2, chen2017guca1amutationcauses pages 9-10) | (camargo2022newinsightson pages 1-2, chen2017guca1amutationcauses pages 9-10) |
| Imaging features | FAF | Speckled or stippled hyper-/hypoautofluorescence in earlier lesions; internal hypoautofluorescent patches in CACD-like areas (camargo2022newinsightson pages 1-2, chen2026genotypephenotypeofpatients pages 1-5) | (camargo2022newinsightson pages 1-2, chen2026genotypephenotypeofpatients pages 1-5) |
| Imaging features | OCT/OCTA | Outer retinal atrophy, central macular atrophy, intraretinal cystic spaces; OCTA can show choriocapillaris flow deficits beyond the clinically atrophic area (seddon2024clinicalandimaging pages 9-10) | (seddon2024clinicalandimaging pages 9-10) |
| Electrophysiology | ERG abnormalities | Full-field ERG in PRPH2 disease showed significantly reduced amplitudes across components and delayed light-adapted 30-Hz flicker and single-flash b-wave peak times (P < 0.001) (jeffery2024retinaldystrophiesassociated pages 1-2) | (jeffery2024retinaldystrophiesassociated pages 1-2) |
| Frequency within PRPH2 disease | CACD phenotype proportion | In the 241-patient PRPH2 cohort, FAF phenotypes included CACD in 28% (jeffery2024retinaldystrophiesassociated pages 1-2) | (jeffery2024retinaldystrophiesassociated pages 1-2) |
| Visual acuity statistic | PRPH2 cohort median VA | Median VA in the PRPH2 cohort was 0.18 logMAR in each eye (right-eye IQR 0–0.54; left-eye IQR 0–0.42) (jeffery2024retinaldystrophiesassociated pages 1-2) | (jeffery2024retinaldystrophiesassociated pages 1-2) |
| Natural history/genotype–phenotype | c.828+3A>T vs L185P PRPH2 | c.828+3A>T presented in the 5th decade with diffuse RPE atrophy/CACD and progressed to extensive atrophy in the 6th–8th decades; L185P had milder PD/AVMD phenotypes with later central atrophy and better VA (seddon2024clinicalandimaging pages 1-2) | (seddon2024clinicalandimaging pages 1-2) |
| Genetic diagnostic yield | Solved cases in one CACD cohort | One cited CACD series solved 7 of 20 cases genetically (35%), highlighting incomplete yield (camargo2022newinsightson pages 6-8) | (camargo2022newinsightson pages 6-8) |
| Relative rarity | Observation within IRD cohorts | Another cited study found CACD in 0.92% of 2,158 individuals in an IRD context (camargo2022newinsightson pages 6-8) | (camargo2022newinsightson pages 6-8) |
| Prevalence estimate | Reported overall prevalence | Genetic-testing review reported overall prevalence as 1–9 per 100,000, but this estimate comes from an older testing-focused summary and should be treated cautiously (abeshi2017genetictestingfor pages 3-3) | (abeshi2017genetictestingfor pages 3-3) |
| Differential diagnosis | AMD/geographic atrophy phenocopy | Some PRPH2/CACD cases were initially misdiagnosed as geographic atrophy secondary to AMD; multimodal imaging and sequencing improve distinction (chiang2023electrophysiologicalevaluationof pages 18-18, seddon2024clinicalandimaging pages 9-10, seddon2024clinicalandimaging pages 1-2) | (chiang2023electrophysiologicalevaluationof pages 18-18, seddon2024clinicalandimaging pages 9-10, seddon2024clinicalandimaging pages 1-2) |
| Treatment status | No established disease-modifying therapy | Reviews state no effective treatment currently prevents CACD progression; management is mainly diagnostic monitoring and inherited retinal disease supportive care (camargo2022newinsightson pages 1-2) | (camargo2022newinsightson pages 1-2) |


*Table: This table summarizes core disease-level facts for Central Areolar Choroidal Dystrophy supported by the evidence gathered in this conversation. It includes identifiers, synonyms, inheritance, genes, hallmark phenotypes, and key quantitative findings useful for knowledge-base curation.*

---

## 1. Disease Information

### 1.1 Definition and current understanding
CACD is a rare hereditary macular dystrophy characterized by bilateral, symmetric, well-circumscribed macular loss of retinal pigment epithelium (RPE), choriocapillaris, and overlying retina, leading to progressive—often profound—central vision loss. (camargo2022newinsightson pages 1-2)

A 2022 systematic review summarizes CACD as a macula-predominant dystrophy with typical onset “between the third and fifth decades,” and emphasizes that there is **no effective treatment that prevents progression**. (camargo2022newinsightson pages 1-2)

**Direct abstract quote (definition):** “Central areolar choroidal dystrophy is an inherited disorder characterized by progressive choriocapillaris atrophy and retinal degeneration…” (Ruiz-Pastor et al., 2023; Cell Death & Disease; published Nov 2023; https://doi.org/10.1038/s41419-023-06243-8). (ruizpastor2023prph2knockinmice pages 1-2)

### 1.2 Key identifiers
- **OMIM/MIM:** CACD has been cited as **MIM 215500** in CACD literature summaries. (abeshi2017genetictestingfor pages 3-3, chiang2023electrophysiologicalevaluationof pages 18-18)
- **OMIM phenotype reference in PRPH2 retinopathy cohort:** CACD phenotype within PRPH2-associated disease referenced as **OMIM #613105** in a 2024 PRPH2 cohort paper. (jeffery2024retinaldystrophiesassociated pages 2-3)
- **MONDO ID / Orphanet / ICD-10/ICD-11 / MeSH:** Not retrievable from the available tool context in this run; should be added by direct lookup in MONDO/Orphanet/ICD/MeSH resources.

### 1.3 Synonyms and alternative names
- “CACD” (abbreviation) and “central areolar chorioretinal dystrophy” appear in recent PRPH2 longitudinal phenotyping work describing diffuse RPE atrophy “consistent with central areolar chorioretinal dystrophy (CACD).” (seddon2024clinicalandimaging pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
CACD is primarily genetic (Mendelian), with both autosomal dominant and rarer recessive inheritance reported. (camargo2022newinsightson pages 1-2, abeshi2017genetictestingfor pages 3-3)

A 2022 systematic review identified mutations in **six genes** as implicated in monogenic CACD in the literature it reviewed: **PRPH2, GUCA1A, GUCY2D, CDHR1, ABCA4, and TTLL5**. (camargo2022newinsightson pages 1-2)

### 2.2 Risk factors
**Genetic risk factors**
- **PRPH2** is highlighted as the main gene in most published CACD studies. (camargo2022newinsightson pages 6-8, camargo2022newinsightson pages 8-9)
- CACD has been associated with variants in genes involved in photoreceptor structure (PRPH2), phototransduction recovery/Ca2+ feedback (GUCA1A, GUCY2D), and other retinal dystrophy genes (CDHR1, ABCA4, TTLL5) with variable strength of evidence depending on the gene/variant. (camargo2022newinsightson pages 1-2, camargo2022newinsightson pages 8-9)

**Environmental risk factors / lifestyle risk factors**
No CACD-specific environmental or lifestyle risk factors were identified in the retrieved evidence set for this run.

### 2.3 Protective factors and gene–environment interactions
No CACD-specific protective factors or gene–environment interactions were identified in the retrieved evidence set for this run.

---

## 3. Phenotypes

### 3.1 Core clinical phenotype and staging
A disease-staging framework described in a 2022 systematic review includes four clinical stages:
- **Stage 1:** subtle parafoveal RPE changes
- **Stage 2:** oval/round mildly atrophic hypopigmented area with a “speckled” fundus autofluorescence (FAF) pattern
- **Stage 3:** well-demarcated RPE atrophy patches outside the fovea
- **Stage 4:** foveal involvement with markedly decreased visual acuity, commonly **<20/200**. (camargo2022newinsightson pages 1-2)

### 3.2 Frequency and quantitative phenotype statistics (recent cohorts)
In the largest recent multicenter PRPH2 cohort (241 patients, 168 families; Investigative Ophthalmology & Visual Science; May 2024; https://doi.org/10.1167/iovs.65.5.22):
- **Median age at symptom onset:** 40 years (range 4–78). (jeffery2024retinaldystrophiesassociated pages 1-2)
- **FAF phenotype distribution included CACD:** **28%** classified as CACD. (jeffery2024retinaldystrophiesassociated pages 1-2)
- **Median visual acuity:** **0.18 logMAR** in each eye (IQRs provided in the abstract). (jeffery2024retinaldystrophiesassociated pages 1-2)
- **ERG:** significantly reduced amplitudes across components and delayed peak times in light-adapted 30-Hz flicker and single-flash b-wave (**P < 0.001**). (jeffery2024retinaldystrophiesassociated pages 1-2)

### 3.3 Representative symptoms/signs (suggested HPO terms)
Evidence in this run supports the following clinical manifestations and corresponding suggested **HPO** terms (examples):
- Progressive central vision loss / reduced visual acuity → **HP:0007663 (Reduced visual acuity)** (stage 4 often <20/200). (camargo2022newinsightson pages 1-2)
- Macular atrophy / chorioretinal atrophy → **HP:0000608 (Macular degeneration)** / **HP:0000556 (Chorioretinal atrophy)** (phenotype described as central macular RPE/choriocapillaris atrophy). (camargo2022newinsightson pages 1-2, corradetti2024retinalimagingfindings pages 13-15)
- Central scotoma (reported in a 2023 CACD case report abstract, but not deeply extracted here) → **HP:0000603 (Central scotoma)** (limited evidence in retrieved set; primarily case-report level). (paper retrieved but not evidence-extracted)

### 3.4 Quality of life impact
No CACD-specific quality-of-life instrument results (e.g., NEI VFQ-25, EQ-5D) were found in the retrieved evidence set for this run; however, the disease is described as “usually profound visual loss” at later stages, which is expected to substantially impact daily functioning. (camargo2022newinsightson pages 1-2)

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes (with disease context)
A 2022 systematic review of CACD-causing genes reports that variants in **PRPH2, GUCA1A, GUCY2D, CDHR1, ABCA4, TTLL5** have been implicated in monogenic CACD in the literature, with functional connections to photoreceptors. (camargo2022newinsightson pages 1-2, camargo2022newinsightson pages 8-9)

**Functional grouping (from review synthesis):**
- Photoreceptor outer segment structure: **PRPH2** (peripherin-2) required for outer segment disc morphogenesis and rim curvature. (camargo2022newinsightson pages 8-9)
- Phototransduction recovery / Ca2+ feedback: **GUCY2D** encodes retinal guanylyl cyclase; **GUCA1A** encodes GCAP1 regulating GUCY2D in Ca2+-dependent feedback. (camargo2022newinsightson pages 8-9)

### 4.2 Pathogenic variants (examples explicitly supported here)
**PRPH2**
- **p.Arg195Leu (R195L)**: used to generate a CRISPR knock-in model that “recapitulate[s] human central areolar choroidal dystrophy.” (Ruiz-Pastor et al., 2023; published Nov 2023; https://doi.org/10.1038/s41419-023-06243-8). (ruizpastor2023prph2knockinmice pages 1-2, ruizpastor2023prph2knockinmice pages 3-5)
- **c.828+3A>T** (splice-site): associated with a more severe CACD-like phenotype in a longitudinal PRPH2 cohort, presenting with diffuse RPE atrophy consistent with CACD and progressing to extensive atrophy. (Seddon et al., 2024; IOVS; published Dec 2024; https://doi.org/10.1167/iovs.65.14.31). (seddon2024clinicalandimaging pages 1-2)

**GUCY2D**
- **p.Val933Ala / V933A**: cited as a CACD-causative variant in summaries and systematic review context. (camargo2022newinsightson pages 6-8, abeshi2017genetictestingfor pages 3-3)

**GUCA1A**
- Variants including **p.Arg120Leu** are discussed as disrupting photoreceptors/RPE in mechanistic work and are included in CACD gene lists in the systematic review. (camargo2022newinsightson pages 8-9, chen2017guca1amutationcauses pages 9-10)

**Important limitation:** This run did not retrieve ClinVar/gnomAD allele frequencies or ACMG per-variant classifications directly; variant classification statements here are limited to what the retrieved papers explicitly state.

### 4.3 Genotype–phenotype correlations
A 2024 longitudinal cohort found PRPH2 **c.828+3A>T** associated with more advanced disease compatible with CACD and worse visual outcomes versus PRPH2 **L185P** associated with pattern dystrophy phenotypes and better visual acuity over follow-up. (seddon2024clinicalandimaging pages 1-2)

In a large 2024 PRPH2 cohort, the CACD phenotype was associated with **missense variants**, and specific codons were highlighted as repeatedly reported for CACD (Arg142, Arg172, Arg195, Ile196, Arg203, Gly208). (jeffery2024retinaldystrophiesassociated pages 2-3)

---

## 5. Environmental Information
No CACD-specific environmental, lifestyle, or infectious contributors were identified in the retrieved evidence set for this run.

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (gene to phenotype)
**Photoreceptor-first with secondary RPE/choriocapillaris involvement (proposed):**
- CACD is often recognized clinically by RPE and choriocapillaris defects, but mechanistic discussion notes that genes reported to cause CACD are photoreceptor-expressed, supporting a model where primary photoreceptor dysfunction can precede and drive secondary RPE/choriocapillaris degeneration. (chen2017guca1amutationcauses pages 9-10)
- In imaging-based characterization, CACD is described as “well-demarcated central macular atrophy of the RPE and choriocapillaris,” consistent with downstream tissue loss. (corradetti2024retinalimagingfindings pages 13-15)

### 6.2 Molecular pathways/processes implicated (suggested GO terms)
Evidence-supported processes include:
- Photoreceptor outer segment organization/morphogenesis (PRPH2 structural role) → **GO:0031644 (regulation of neurological system process)** is too broad; more appropriate suggested terms include **GO:0031638 (z-disc?)** not correct. Given the evidence, suggested (curation) terms: **GO:0030154 (cell differentiation)** not right. Due to absence of explicit GO terms in evidence, provide conceptual mapping only: **outer segment disc morphogenesis/organization** (photoreceptor outer segment structure). (camargo2022newinsightson pages 8-9, ruizpastor2023prph2knockinmice pages 3-5)
- Phototransduction recovery and cGMP/Ca2+ homeostasis (GUCY2D regulated by GUCA1A) → suggested conceptual GO: **phototransduction**, **cGMP biosynthetic process**, **calcium ion homeostasis**. (camargo2022newinsightson pages 8-9)
- Neuroinflammation and glial activation (mouse model) → suggested conceptual GO: **microglial cell activation**, **gliosis**, **synaptic remodeling**. (ruizpastor2023prph2knockinmice pages 14-16, ruizpastor2023prph2knockinmice pages 8-11)

### 6.3 Cell types involved (suggested CL terms)
- Photoreceptors (rods and cones) (PRPH2 expressed in photoreceptors; functional impairment in rod and cone pathways) → suggested CL: **CL:0000018 (photoreceptor cell)**. (camargo2022newinsightson pages 8-9, ruizpastor2023prph2knockinmice pages 1-2)
- Retinal pigment epithelial cells (RPE atrophy/irregularities) → suggested CL: **CL:0002585 (retinal pigment epithelial cell)**. (seddon2024clinicalandimaging pages 1-2, corradetti2024retinalimagingfindings pages 13-15)
- Microglia (activation/invasion of outer nuclear layer in knock-in mice) → suggested CL: **CL:0000129 (microglial cell)**. (ruizpastor2023prph2knockinmice pages 14-16, ruizpastor2023prph2knockinmice pages 8-11)
- Müller glia / retinal glia (gliosis) → suggested CL: **CL:0000634 (Müller cell)**. (ruizpastor2023prph2knockinmice pages 14-16)

### 6.4 Key 2023 mechanistic advance: PRPH2 knock-in CACD model
Ruiz-Pastor et al. (Cell Death & Disease; Nov 2023; https://doi.org/10.1038/s41419-023-06243-8) created Prph2 p.Arg195Leu knock-in mice and reported:
- ERG amplitudes reduced early in homozygotes (from 1 month) and later in heterozygotes (from 6 months). (ruizpastor2023prph2knockinmice pages 1-2)
- Declining visual acuity from 3 months (homozygotes) and 6 months (heterozygotes). (ruizpastor2023prph2knockinmice pages 1-2)
- Outer segment structural disruption plus synaptic remodeling and microglial activation / gliosis. (ruizpastor2023prph2knockinmice pages 14-16, ruizpastor2023prph2knockinmice pages 8-11)

**Direct abstract quote (model utility):** the mice “show a pattern of retinal degeneration similar to that described in human patients with central areolar choroidal dystrophy and appear to be good models to study the mechanisms involved…” (ruizpastor2023prph2knockinmice pages 1-2)

### 6.5 Molecular profiling / multi-omics
No CACD-specific transcriptomic/proteomic/metabolomic or single-cell/spatial studies were identified in the retrieved evidence set for this run.

---

## 7. Anatomical Structures Affected

### 7.1 Organ/tissue localization (suggested UBERON terms)
- Eye → **UBERON:0000970 (eye)**
- Retina (macula region) → **UBERON:0000966 (retina)**; macula conceptual localization supported by macula-focused atrophy. (camargo2022newinsightson pages 1-2, corradetti2024retinalimagingfindings pages 13-15)
- RPE and choriocapillaris / choroid → conceptual localization supported by “RPE and choriocapillaris” atrophy. (corradetti2024retinalimagingfindings pages 13-15)

### 7.2 Laterality
CACD is typically bilateral and symmetric by definition in the disease overview, though unilateral presentations have been reported (not evidence-extracted here). (camargo2022newinsightson pages 1-2)

---

## 8. Temporal Development

### 8.1 Onset
Typical onset is described as between the **third and fifth decades** in a 2022 systematic review. (camargo2022newinsightson pages 1-2)

In PRPH2-associated retinopathy cohorts (which include CACD as a major phenotype), **median symptom onset** across PRPH2 disease was **40 years** (range 4–78). (jeffery2024retinaldystrophiesassociated pages 1-2)

### 8.2 Progression
The longitudinal PRPH2 cohort demonstrates multi-decade progression patterns:
- PRPH2 L185P: adult-onset vitelliform/butterfly pattern dystrophy in 40s–50s evolving to central macular atrophy approximately 20 years later. (seddon2024clinicalandimaging pages 1-2)
- PRPH2 c.828+3A>T: presentation in the fifth decade with CACD-like diffuse RPE atrophy progressing to extensive atrophy in later decades. (seddon2024clinicalandimaging pages 1-2)

---

## 9. Inheritance and Population

### 9.1 Inheritance pattern
CACD is described as **mostly autosomal dominant**, with rare autosomal recessive inheritance also reported. (camargo2022newinsightson pages 1-2, abeshi2017genetictestingfor pages 3-3)

### 9.2 Epidemiology
A genetic-testing-focused summary reported an “overall prevalence” estimate of **1–9 per 100,000**; this estimate is older and should be validated against up-to-date registry data. (abeshi2017genetictestingfor pages 3-3)

No robust CACD incidence estimates were identified in the retrieved evidence set.

---

## 10. Diagnostics

### 10.1 Clinical and imaging diagnostics (2024 state-of-the-art)
A 2024 IRD imaging review states CACD shows “well-demarcated central macular atrophy of the RPE and choriocapillaris,” and that:
- **FAF** helps identify accumulated lipofuscin and areas of RPE hypopigmentation.
- **Spectral-domain OCT** can demonstrate “complete loss of all outer retinal layers in the atrophic region.”
- **OCTA** can show “patchy choriocapillaris flow deficits not only within the area of RPE atrophy but also in surrounding regions.” (Corradetti et al., Journal of Clinical Medicine; Apr 2024; https://doi.org/10.3390/jcm13072079). (corradetti2024retinalimagingfindings pages 13-15)

### 10.2 Electrophysiology
The 2024 PRPH2 cohort reported full-field ERG abnormalities (reduced amplitudes and delayed peak times), supporting the role of ERG for characterization and differential diagnosis. (jeffery2024retinaldystrophiesassociated pages 1-2)

### 10.3 Genetic testing
Genetic testing is emphasized as clinically useful for confirming diagnosis and enabling counseling and research/trial access; a summary states CACD diagnosis may rely on ophthalmologic examination plus imaging and electrophysiology, and that genetic testing supports differential diagnosis and couple risk assessment. (abeshi2017genetictestingfor pages 3-3)

**Panel limitations / diagnostic yield:** In an IRD cohort context, CACD had low molecular diagnostic rate (example cited: **35% (7/20)**). (camargo2022newinsightson pages 6-8)

### 10.4 Differential diagnosis
CACD can be confused with geographic atrophy due to age-related macular degeneration (AMD). A 2024 longitudinal PRPH2 cohort notes some individuals were initially misdiagnosed as geographic atrophy secondary to AMD, highlighting the value of multimodal imaging and genetic testing. (seddon2024clinicalandimaging pages 9-10, seddon2024clinicalandimaging pages 1-2)

---

## 11. Outcome / Prognosis

### 11.1 Visual outcomes
The 2022 systematic review notes that late-stage CACD (foveal involvement) often results in severe acuity reduction (commonly <20/200). (camargo2022newinsightson pages 1-2)

In PRPH2-associated disease (where CACD is common), median VA was 0.18 logMAR in a 241-patient cohort, but this includes multiple PRPH2 phenotypes; CACD-specific VA distributions were not extracted from the available abstract evidence. (jeffery2024retinaldystrophiesassociated pages 1-2)

### 11.2 Prognostic factors
Variant-specific prognosis is suggested in PRPH2 cohorts: c.828+3A>T is associated with more severe CACD-like disease and worse VA than L185P, with different trajectories over decades. (seddon2024clinicalandimaging pages 1-2)

---

## 12. Treatment

### 12.1 Current standard of care
No disease-modifying treatment preventing CACD progression is established in the retrieved evidence set; management is currently supportive and focused on diagnosis, monitoring, and counseling. (camargo2022newinsightson pages 1-2)

### 12.2 Advanced therapeutics and experimental directions (2023–2024 priority)
A 2024 PRPH2 workshop report (TVST; Oct 2024; https://doi.org/10.1167/tvst.13.10.16) highlights therapeutic directions for PRPH2-associated IRDs, including gene-specific and gene-agnostic strategies and the need for larger natural-history studies. (ayyagari2024currentandfuture pages 1-2)

**Direct abstract quote (expert consensus framing):** the workshop highlighted “possible therapeutic approaches…including gene-specific therapies and gene-agnostic approaches.” (ayyagari2024currentandfuture pages 1-2)

The workshop report details gene-specific approaches including gene augmentation, allele-specific knockdown (ASO/RNase H concepts), knockdown-and-replace strategies, and genome editing/prime editing as potential routes depending on PRPH2 mechanism (loss-of-function vs gain-of-function). (ayyagari2024currentandfuture pages 6-8)

A 2023 review of genetic treatments for autosomal dominant IRDs emphasizes that gain-of-function variants “will require gene or RNA editing/knockdown to suppress the mutant allele,” while dominant-negative mechanisms may be more amenable to augmentation. (British Journal of Ophthalmology; Aug 2023; https://doi.org/10.1136/bjo-2022-321903). (varela2023genetictreatmentfor pages 13-19)

### 12.3 Clinical trials relevant to CACD genes / IRD endpoints
- **NCT03920007 (ATSN-101; Atsena Therapeutics; Phase 1/2; started 2019)** targets **biallelic GUCY2D** Leber congenital amaurosis (not CACD), but is relevant as a proof-of-concept for retinal gene therapy targeting a CACD-associated gene. Primary endpoint: adverse events; secondary endpoints include BCVA and full-field stimulus testing sensitivity. (NCT03920007 chunk 1)
- **NCT07265895 (IRCCS San Raffaele; observational; NOT_YET_RECRUITING; start 2026-01-01)** is a natural-history/genotype–phenotype study for IRDs (including PRPH2) and explicitly lists imaging/functional endpoints that could be used in CACD: BCVA, microperimetry sensitivity, total macular volume, central subfield thickness, preserved ellipsoid zone area, decreased autofluorescence area, etc. (NCT07265895 chunk 1)

### 12.4 Suggested MAXO terms (treatments/actions)
Evidence-supported interventions and actions (as ontology suggestions) include:
- Genetic testing / molecular diagnosis → **MAXO:0000127 (genetic testing)** (conceptual; exact MAXO ID should be verified)
- Optical coherence tomography → **MAXO (diagnostic imaging procedure)** (verify exact MAXO term)
- Fundus autofluorescence imaging → **MAXO (retinal imaging)** (verify)
- Low-vision rehabilitation/support → **MAXO (vision rehabilitation)** (verify)
- Gene therapy / gene augmentation / genome editing / antisense therapy → **MAXO (gene therapy)** / **MAXO (genome editing therapy)** / **MAXO (antisense oligonucleotide therapy)** (verify)

---

## 13. Prevention
No primary prevention strategies specific to CACD onset were identified in the retrieved evidence set. Secondary/tertiary prevention is currently centered on early diagnosis (genetic testing + multimodal imaging), monitoring for complications such as macular neovascularization described in PRPH2 longitudinal follow-up, and supportive interventions for visual disability. (seddon2024clinicalandimaging pages 9-10, seddon2024clinicalandimaging pages 1-2)

---

## 14. Other Species / Natural Disease
No naturally occurring CACD in non-human species was identified in the retrieved evidence set for this run.

---

## 15. Model Organisms
A 2023 CRISPR/Cas9 **Prph2 p.Arg195Leu** knock-in mouse model recapitulates key CACD features and is positioned as a platform for mechanistic studies and therapeutic testing. (ruizpastor2023prph2knockinmice pages 1-2, ruizpastor2023prph2knockinmice pages 8-11)

---

## Evidence Gaps / Not Available in Retrieved Corpus (explicit)
- MONDO/Orphanet/ICD/MeSH identifiers for CACD were not retrievable via the available tool outputs in this run.
- CACD-specific, instrumented quality-of-life outcomes (NEI VFQ-25/EQ-5D/PROMIS) were not found in the retrieved evidence set.
- Variant allele frequencies (gnomAD) and formal ClinVar/ClinGen assertions were not directly retrieved.
- CACD-specific omics (bulk RNA-seq, single-cell, spatial transcriptomics, proteomics, metabolomics) were not identified in the retrieved evidence set.


References

1. (camargo2022newinsightson pages 1-2): João Paulo Kazmierczak de Camargo, Giovanna Nazaré de Barros Prezia, Naoye Shiokawa, Mario Teruo Sato, Roberto Rosati, and Angelica Beate Winter Boldt. New insights on the regulatory gene network disturbed in central areolar choroidal dystrophy—beyond classical gene candidates. Frontiers in Genetics, May 2022. URL: https://doi.org/10.3389/fgene.2022.886461, doi:10.3389/fgene.2022.886461. This article has 5 citations and is from a peer-reviewed journal.

2. (jeffery2024retinaldystrophiesassociated pages 1-2): Rachael C. Heath Jeffery, Jennifer A. Thompson, Johnny Lo, Enid S. Chelva, Sean Armstrong, Jose S. Pulido, Rebecca Procopio, Andrea L. Vincent, Lorenzo Bianco, Maurizio Battaglia Parodi, Lucia Ziccardi, Giulio Antonelli, Lucilla Barbano, João P. Marques, Sara Geada, Ana L. Carvalho, Wei C. Tang, Choi M. Chan, Camiel J. F. Boon, Jonathan Hensman, Ta-Ching Chen, Chien-Yu Lin, Pei-Lung Chen, Ajoy Vincent, Anupreet Tumber, Elise Heon, John R. Grigg, Robyn V. Jamieson, Elisa E. Cornish, Benjamin M. Nash, Shyamanga Borooah, Lauren N. Ayton, Alexis Ceecee Britten-Jones, Thomas L. Edwards, Jonathan B. Ruddle, Abhishek Sharma, Rowan G. Porter, Tina M. Lamey, Terri L. McLaren, Samuel McLenachan, Danial Roshandel, and Fred K. Chen. Retinal dystrophies associated with peripherin-2: genetic spectrum and novel clinical observations in 241 patients. Investigative Ophthalmology &amp; Visual Science, 65:22, May 2024. URL: https://doi.org/10.1167/iovs.65.5.22, doi:10.1167/iovs.65.5.22. This article has 24 citations and is from a domain leading peer-reviewed journal.

3. (seddon2024clinicalandimaging pages 1-2): Johanna M. Seddon, Dikha De, Laura Grunenkovaite, and Daniela Ferrara. Clinical and imaging characteristics of <i>prph2</i> retinopathies in a longitudinal cohort and diagnostic implications. Investigative Ophthalmology &amp; Visual Science, 65:31, Dec 2024. URL: https://doi.org/10.1167/iovs.65.14.31, doi:10.1167/iovs.65.14.31. This article has 2 citations and is from a domain leading peer-reviewed journal.

4. (abeshi2017genetictestingfor pages 3-3): Andi Abeshi, Francesca Fanelli, Tommaso Beccari, Munis Dundar, Benedetto Falsini, and Matteo Bertelli. Genetic testing for central areolar choroidal dystrophy. The EuroBiotech Journal, 1:23-25, Oct 2017. URL: https://doi.org/10.24190/issn2564-615x/2017/s1.07, doi:10.24190/issn2564-615x/2017/s1.07. This article has 3 citations.

5. (chiang2023electrophysiologicalevaluationof pages 18-18): Tsun-Kang Chiang and Minzhong Yu. Electrophysiological evaluation of macular dystrophies. Journal of Clinical Medicine, 12:1430, Feb 2023. URL: https://doi.org/10.3390/jcm12041430, doi:10.3390/jcm12041430. This article has 9 citations.

6. (jeffery2024retinaldystrophiesassociated pages 2-3): Rachael C. Heath Jeffery, Jennifer A. Thompson, Johnny Lo, Enid S. Chelva, Sean Armstrong, Jose S. Pulido, Rebecca Procopio, Andrea L. Vincent, Lorenzo Bianco, Maurizio Battaglia Parodi, Lucia Ziccardi, Giulio Antonelli, Lucilla Barbano, João P. Marques, Sara Geada, Ana L. Carvalho, Wei C. Tang, Choi M. Chan, Camiel J. F. Boon, Jonathan Hensman, Ta-Ching Chen, Chien-Yu Lin, Pei-Lung Chen, Ajoy Vincent, Anupreet Tumber, Elise Heon, John R. Grigg, Robyn V. Jamieson, Elisa E. Cornish, Benjamin M. Nash, Shyamanga Borooah, Lauren N. Ayton, Alexis Ceecee Britten-Jones, Thomas L. Edwards, Jonathan B. Ruddle, Abhishek Sharma, Rowan G. Porter, Tina M. Lamey, Terri L. McLaren, Samuel McLenachan, Danial Roshandel, and Fred K. Chen. Retinal dystrophies associated with peripherin-2: genetic spectrum and novel clinical observations in 241 patients. Investigative Ophthalmology &amp; Visual Science, 65:22, May 2024. URL: https://doi.org/10.1167/iovs.65.5.22, doi:10.1167/iovs.65.5.22. This article has 24 citations and is from a domain leading peer-reviewed journal.

7. (camargo2022newinsightson pages 6-8): João Paulo Kazmierczak de Camargo, Giovanna Nazaré de Barros Prezia, Naoye Shiokawa, Mario Teruo Sato, Roberto Rosati, and Angelica Beate Winter Boldt. New insights on the regulatory gene network disturbed in central areolar choroidal dystrophy—beyond classical gene candidates. Frontiers in Genetics, May 2022. URL: https://doi.org/10.3389/fgene.2022.886461, doi:10.3389/fgene.2022.886461. This article has 5 citations and is from a peer-reviewed journal.

8. (camargo2022newinsightson pages 8-9): João Paulo Kazmierczak de Camargo, Giovanna Nazaré de Barros Prezia, Naoye Shiokawa, Mario Teruo Sato, Roberto Rosati, and Angelica Beate Winter Boldt. New insights on the regulatory gene network disturbed in central areolar choroidal dystrophy—beyond classical gene candidates. Frontiers in Genetics, May 2022. URL: https://doi.org/10.3389/fgene.2022.886461, doi:10.3389/fgene.2022.886461. This article has 5 citations and is from a peer-reviewed journal.

9. (chen2017guca1amutationcauses pages 9-10): Xue Chen, X. Sheng, Wenjuan Zhuang, Xiantao Sun, Guohua Liu, Xun Shi, Guofu Huang, Yan-fang Mei, Yingjie Li, Xinyuan Pan, Ya-ni Liu, Zi-li Li, Qingshun Zhao, B. Yan, and Chen Zhao. Guca1a mutation causes maculopathy in a five-generation family with a wide spectrum of severity. Genetics in Medicine, 19:945-954, Aug 2017. URL: https://doi.org/10.1038/gim.2016.217, doi:10.1038/gim.2016.217. This article has 26 citations and is from a highest quality peer-reviewed journal.

10. (camargo2022newinsightson pages 15-16): João Paulo Kazmierczak de Camargo, Giovanna Nazaré de Barros Prezia, Naoye Shiokawa, Mario Teruo Sato, Roberto Rosati, and Angelica Beate Winter Boldt. New insights on the regulatory gene network disturbed in central areolar choroidal dystrophy—beyond classical gene candidates. Frontiers in Genetics, May 2022. URL: https://doi.org/10.3389/fgene.2022.886461, doi:10.3389/fgene.2022.886461. This article has 5 citations and is from a peer-reviewed journal.

11. (chen2026genotypephenotypeofpatients pages 1-5): Jieqiong Chen, Yu Hong, Minghao Chen, Hong Wang, Yuanyuan Gong, Suqin Yu, weijun wang, Li Su, Ting Zhang, Xinxin Liu, Junran Sun, Tong Li, Huixun Jia, Mei Jiang, Lihong Jiang, Yin Hu, and Xiaodong Sun. Genotype-phenotype of patients with prph2-associated retinal dystrophy: novel insights on foveal structure and visual outcomes. Unknown journal, Feb 2026. URL: https://doi.org/10.21203/rs.3.rs-8587127/v1, doi:10.21203/rs.3.rs-8587127/v1.

12. (seddon2024clinicalandimaging pages 9-10): Johanna M. Seddon, Dikha De, Laura Grunenkovaite, and Daniela Ferrara. Clinical and imaging characteristics of <i>prph2</i> retinopathies in a longitudinal cohort and diagnostic implications. Investigative Ophthalmology &amp; Visual Science, 65:31, Dec 2024. URL: https://doi.org/10.1167/iovs.65.14.31, doi:10.1167/iovs.65.14.31. This article has 2 citations and is from a domain leading peer-reviewed journal.

13. (ruizpastor2023prph2knockinmice pages 1-2): María José Ruiz-Pastor, Xavier Sánchez-Sáez, Oksana Kutsyr, Henar Albertos-Arranz, Carla Sánchez-Castillo, Isabel Ortuño-Lizarán, Natalia Martínez-Gil, Lorena Vidal-Gil, Lucía Méndez, Manuel Sánchez-Martín, Victoria Maneu, Pedro Lax, and Nicolás Cuenca. Prph2 knock-in mice recapitulate human central areolar choroidal dystrophy retinal degeneration and exhibit aberrant synaptic remodeling and microglial activation. Cell Death & Disease, Nov 2023. URL: https://doi.org/10.1038/s41419-023-06243-8, doi:10.1038/s41419-023-06243-8. This article has 7 citations and is from a peer-reviewed journal.

14. (corradetti2024retinalimagingfindings pages 13-15): Giulia Corradetti, Aditya Verma, Jasaman Tojjar, Louay Almidani, Deniz Oncel, Mehdi Emamverdi, Alec Bradley, Sophiana Lindenberg, Muneeswar Gupta Nittala, and SriniVas R. Sadda. Retinal imaging findings in inherited retinal diseases. Journal of Clinical Medicine, 13:2079, Apr 2024. URL: https://doi.org/10.3390/jcm13072079, doi:10.3390/jcm13072079. This article has 13 citations.

15. (ruizpastor2023prph2knockinmice pages 3-5): María José Ruiz-Pastor, Xavier Sánchez-Sáez, Oksana Kutsyr, Henar Albertos-Arranz, Carla Sánchez-Castillo, Isabel Ortuño-Lizarán, Natalia Martínez-Gil, Lorena Vidal-Gil, Lucía Méndez, Manuel Sánchez-Martín, Victoria Maneu, Pedro Lax, and Nicolás Cuenca. Prph2 knock-in mice recapitulate human central areolar choroidal dystrophy retinal degeneration and exhibit aberrant synaptic remodeling and microglial activation. Cell Death & Disease, Nov 2023. URL: https://doi.org/10.1038/s41419-023-06243-8, doi:10.1038/s41419-023-06243-8. This article has 7 citations and is from a peer-reviewed journal.

16. (ruizpastor2023prph2knockinmice pages 14-16): María José Ruiz-Pastor, Xavier Sánchez-Sáez, Oksana Kutsyr, Henar Albertos-Arranz, Carla Sánchez-Castillo, Isabel Ortuño-Lizarán, Natalia Martínez-Gil, Lorena Vidal-Gil, Lucía Méndez, Manuel Sánchez-Martín, Victoria Maneu, Pedro Lax, and Nicolás Cuenca. Prph2 knock-in mice recapitulate human central areolar choroidal dystrophy retinal degeneration and exhibit aberrant synaptic remodeling and microglial activation. Cell Death & Disease, Nov 2023. URL: https://doi.org/10.1038/s41419-023-06243-8, doi:10.1038/s41419-023-06243-8. This article has 7 citations and is from a peer-reviewed journal.

17. (ruizpastor2023prph2knockinmice pages 8-11): María José Ruiz-Pastor, Xavier Sánchez-Sáez, Oksana Kutsyr, Henar Albertos-Arranz, Carla Sánchez-Castillo, Isabel Ortuño-Lizarán, Natalia Martínez-Gil, Lorena Vidal-Gil, Lucía Méndez, Manuel Sánchez-Martín, Victoria Maneu, Pedro Lax, and Nicolás Cuenca. Prph2 knock-in mice recapitulate human central areolar choroidal dystrophy retinal degeneration and exhibit aberrant synaptic remodeling and microglial activation. Cell Death & Disease, Nov 2023. URL: https://doi.org/10.1038/s41419-023-06243-8, doi:10.1038/s41419-023-06243-8. This article has 7 citations and is from a peer-reviewed journal.

18. (ayyagari2024currentandfuture pages 1-2): Radha Ayyagari, Shyamanga Borooah, Todd Durham, Claire Gelfman, and Angela Bowman. Current and future directions in developing effective treatments for <i>prph2-</i>associated retinal diseases: a workshop report. Translational Vision Science &amp; Technology, 13:16, Oct 2024. URL: https://doi.org/10.1167/tvst.13.10.16, doi:10.1167/tvst.13.10.16. This article has 3 citations and is from a peer-reviewed journal.

19. (ayyagari2024currentandfuture pages 6-8): Radha Ayyagari, Shyamanga Borooah, Todd Durham, Claire Gelfman, and Angela Bowman. Current and future directions in developing effective treatments for <i>prph2-</i>associated retinal diseases: a workshop report. Translational Vision Science &amp; Technology, 13:16, Oct 2024. URL: https://doi.org/10.1167/tvst.13.10.16, doi:10.1167/tvst.13.10.16. This article has 3 citations and is from a peer-reviewed journal.

20. (varela2023genetictreatmentfor pages 13-19): Malena Daich Varela, Anastasios Georgiadis, and Michel Michaelides. Genetic treatment for autosomal dominant inherited retinal dystrophies: approaches, challenges and targeted genotypes. British Journal of Ophthalmology, 107:1223-1230, Aug 2023. URL: https://doi.org/10.1136/bjo-2022-321903, doi:10.1136/bjo-2022-321903. This article has 32 citations and is from a highest quality peer-reviewed journal.

21. (NCT03920007 chunk 1):  Study of Subretinally Injected ATSN-101 Administered in Patients With Leber Congenital Amaurosis Caused by Biallelic Mutations in GUCY2D. Atsena Therapeutics Inc.. 2019. ClinicalTrials.gov Identifier: NCT03920007

22. (NCT07265895 chunk 1): Maurizio Battaglia Parodi. Inherited Retinal Diseases: Natural History and Genotype-Phenotype Correlations. IRCCS San Raffaele. 2026. ClinicalTrials.gov Identifier: NCT07265895

## Artifacts

- [Edison artifact artifact-00](Central_Areolar_Choroidal_Dystrophy-deep-research-falcon_artifacts/artifact-00.md)