---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-04T10:57:14.308286'
end_time: '2026-06-04T11:08:26.503922'
duration_seconds: 672.2
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Infantile Parkinsonism-Dystonia
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 34
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Infantile_Parkinsonism-Dystonia-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Infantile Parkinsonism-Dystonia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Infantile Parkinsonism-Dystonia** covering all of the
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
- **Disease Name:** Infantile Parkinsonism-Dystonia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Infantile Parkinsonism-Dystonia** covering all of the
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


# Comprehensive Research Report: Infantile Parkinsonism–Dystonia (Mendelian)

## Target Disease
**Disease name (clinical umbrella):** *Infantile parkinsonism–dystonia* (IPD)

### Current concept/definition
In the contemporary literature, “infantile parkinsonism–dystonia” is most often used as a severe, early-onset (typically infancy) combined movement disorder phenotype characterized by dystonia with evolving parkinsonism (bradykinesia/rigidity/hypomimia), often accompanied by oculogyric crises, autonomic dysfunction, and global neurodevelopmental impairment. A major, well-defined Mendelian cause is **dopamine transporter deficiency syndrome (DTDS)** due to **biallelic loss-of-function SLC6A3** variants (also cited as OMIM #613135). (ng2023dopaminetransporterdeficiency pages 2-3, ng2023dopaminetransporterdeficiency pages 1-2)

**Recent gene discovery** expands the concept beyond SLC6A3 transportopathy to include receptor/signaling defects (e.g., **DRD1**) and vesicular monoamine transport disorders (e.g., **SLC18A2/VMAT2**, “parkinsonism-dystonia-2”/PKDYS2), which can present with overlapping infantile dystonia–parkinsonism phenotypes. (reid2023lossoffunctionvariantsin pages 1-2, kaasalainen2024novelslc18a2variant pages 1-2)

### Key identifiers (from retrieved evidence)
- **OMIM:** *Infantile parkinsonism-dystonia* / DTDS reported as **OMIM #613135** in recent case literature. (ng2023dopaminetransporterdeficiency pages 2-3)
- **MONDO / Orphanet / MeSH / ICD-10/ICD-11:** Not found in the currently retrieved full-text evidence; therefore not reliably reportable here.

### Common synonyms and alternative names
- **Dopamine transporter deficiency syndrome (DTDS)** (SLC6A3-related) (ng2023dopaminetransporterdeficiency pages 2-3, ng2023dopaminetransporterdeficiency pages 1-2)
- “Infantile parkinsonism-dystonia” (often used for the DTDS phenotype) (ng2023dopaminetransporterdeficiency pages 2-3)
- Related/overlapping infantile dystonia-parkinsonism entities in recent literature:
  - **Infantile dystonia-parkinsonism type 2 / PKDYS2 / parkinsonism-dystonia-2** (SLC18A2) (kaasalainen2024novelslc18a2variant pages 1-2, almutair2026casereporttwo pages 2-4)
  - **Infantile parkinsonism-dystonia due to DRD1 loss-of-function** (reid2023lossoffunctionvariantsin pages 1-2)

### Evidence source type
The detailed clinical understanding is largely derived from **aggregated disease-level reviews** of published cases (notably DTDS) plus **individual case reports/series** and **preclinical mechanistic model systems** (iPSC-derived neurons, mouse, Drosophila). (ng2023dopaminetransporterdeficiency pages 2-3, ng2021genetherapyrestores pages 1-3, aguilar2021psychomotorimpairmentsand pages 1-2)

---

## 1. Disease Information (Overview)
**DTDS as the prototypic infantile parkinsonism–dystonia:** A 2023 review explicitly states: *“Infantile parkinsonism-dystonia due to dopamine transporter deficiency syndrome (DTDS) is an ultrarare childhood movement disorder caused by biallelic loss-of-function mutations in the SLC6A3 gene.”* (Published Jun 2023; https://doi.org/10.3390/cells12131737). (ng2023dopaminetransporterdeficiency pages 1-2)

**Newly described cause (DRD1):** A 2023 report describes a proband with “severe infantile parkinsonism-dystonia…frequent oculogyric crises, dysautonomia and global neurodevelopmental impairment,” and identifies a homozygous loss-of-function **DRD1** variant. (Published Mar 2023; https://doi.org/10.3390/cells12071046). (reid2023lossoffunctionvariantsin pages 1-2)

**SLC18A2/PKDYS2 overlap:** A 2024 PKDYS2 case report describes infantile-onset dystonia-parkinsonism due to **SLC18A2** with oculogyric crises, hypotonia, and severe disability, underscoring overlap with the infantile parkinsonism-dystonia clinical space. (Published Apr 2024; https://doi.org/10.1155/2024/4767647). (kaasalainen2024novelslc18a2variant pages 1-2, kaasalainen2024novelslc18a2variant pages 2-3)

---

## 2. Etiology

### 2.1 Disease causal factors (primary)
**Genetic (Mendelian) etiologies supported by retrieved evidence:**
1) **SLC6A3 (DAT) loss of function → DTDS** (autosomal recessive; also atypical forms may include dominant-negative mechanisms per review text) (ng2023dopaminetransporterdeficiency pages 1-2, thalib2025acomparativeexploration pages 3-4)
2) **DRD1 loss of function** (recessive, currently single-family evidence in 2023 report) (reid2023lossoffunctionvariantsin pages 1-2)
3) **SLC18A2 (VMAT2) loss of function → PKDYS2/parkinsonism-dystonia-2** (autosomal recessive) (kaasalainen2024novelslc18a2variant pages 1-2, almutair2026casereporttwo pages 2-4)

### 2.2 Risk factors
- **Genetic risk factors:** biallelic pathogenic variants in the causal genes above; consanguinity is highlighted for the DRD1 case (consanguineous parents) and in PKDYS2 sibling cases. (reid2023lossoffunctionvariantsin pages 6-8, almutair2026casereporttwo pages 2-4)
- **Environmental risk factors:** No specific environmental risk factors were identified in the retrieved evidence for infantile parkinsonism–dystonia as a Mendelian disorder.

### 2.3 Protective factors / gene–environment interactions
No protective factors or gene–environment interactions were identified in the retrieved evidence.

---

## 3. Phenotypes (Clinical Spectrum)

### 3.1 Core phenotype domains (DTDS-focused)
A 2023 DTDS review describes early-onset nonspecific symptoms evolving to mixed hyper/hypokinetic movement disorder and parkinsonism-dystonia:
- Infantile onset features: irritability, feeding difficulties, hypotonia, delayed motor development (ng2023dopaminetransporterdeficiency pages 2-3)
- Hyperkinetic movements: chorea, dystonia, ballismus, orolingual dyskinesia (ng2023dopaminetransporterdeficiency pages 2-3)
- Progression to parkinsonism-dystonia: dystonic posturing, bradykinesia, tremor, rigidity, akinesia (ng2023dopaminetransporterdeficiency pages 2-3)
- Episodic crises: status dystonicus; eye movement disorders including **oculogyric crisis** (ng2023dopaminetransporterdeficiency pages 2-3)

**Age of onset:** For DTDS, a comparative review notes typical presentation “within the first 6 months of life.” (thalib2025acomparativeexploration pages 3-4)

### 3.2 Phenotypes in DRD1-associated infantile parkinsonism-dystonia
The 2023 DRD1 report provides a granular infantile-onset phenotype including:
- Global developmental delay with failure of gross motor and vocal milestones (e.g., never sitting/rolling/babbling) (reid2023lossoffunctionvariantsin pages 6-8)
- Recurrent generalized dystonia with oculogyric crises (reid2023lossoffunctionvariantsin pages 6-8)
- Feeding impairment requiring enteral nutrition; gastrointestinal dysmotility symptoms (reflux/constipation) (reid2023lossoffunctionvariantsin pages 6-8)
- **Dysautonomia**/autonomic-type features: excessive sweating and chronic nasal congestion described (reid2023lossoffunctionvariantsin pages 6-8)

### 3.3 Phenotypes in SLC18A2 (PKDYS2)
The 2024 PKDYS2 report describes:
- Early abnormalities in infancy (first noted at 2 months in the case report) with oculogyric crises, hypotonia, delayed psychomotor development and recurrent generalized dystonic episodes (kaasalainen2024novelslc18a2variant pages 1-2)
- Severe functional disability by later childhood with dependence for all activities (kaasalainen2024novelslc18a2variant pages 2-3)

### 3.4 Suggested HPO terms (based on reported clinical features)
Examples (non-exhaustive; align to the evidence above):
- Dystonia (HP:0001332) (ng2023dopaminetransporterdeficiency pages 2-3, reid2023lossoffunctionvariantsin pages 6-8)
- Parkinsonism (HP:0001300) (ng2023dopaminetransporterdeficiency pages 2-3)
- Bradykinesia (HP:0002067) (ng2023dopaminetransporterdeficiency pages 2-3)
- Rigidity (HP:0002063) (ng2023dopaminetransporterdeficiency pages 2-3)
- Oculogyric crisis (HP:0002179) (ng2023dopaminetransporterdeficiency pages 2-3, reid2023lossoffunctionvariantsin pages 6-8, kaasalainen2024novelslc18a2variant pages 1-2)
- Hypotonia (HP:0001252) (ng2023dopaminetransporterdeficiency pages 2-3, reid2023lossoffunctionvariantsin pages 6-8, kaasalainen2024novelslc18a2variant pages 1-2)
- Global developmental delay (HP:0001263) (reid2023lossoffunctionvariantsin pages 1-2, reid2023lossoffunctionvariantsin pages 6-8, kaasalainen2024novelslc18a2variant pages 2-3)
- Feeding difficulties (HP:0011968) / Dysphagia (HP:0002015) (ng2023dopaminetransporterdeficiency pages 2-3, reid2023lossoffunctionvariantsin pages 6-8, kaasalainen2024novelslc18a2variant pages 2-3)
- Autonomic dysfunction (HP:0002311) / Hyperhidrosis (HP:0000975) (reid2023lossoffunctionvariantsin pages 1-2, reid2023lossoffunctionvariantsin pages 6-8)

### 3.5 Quality of life impact
The DTDS review notes high care burden (e.g., many require gastrostomy feeding) and severe disability, implying profound quality-of-life impairment for patients and caregivers. (ng2023dopaminetransporterdeficiency pages 2-3)

### 3.6 Differential diagnosis (high-level, evidence-supported)
DTDS/infantile parkinsonism-dystonia can phenotypically resemble other monoamine neurotransmitter disorders (including disorders of dopamine synthesis/metabolism and vesicular transport). The DRD1 case explicitly notes similarity to monoamine disorders such as AADC deficiency. (reid2023lossoffunctionvariantsin pages 10-12)

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes and inheritance (supported here)
- **SLC6A3 (DAT)**: DTDS; primarily biallelic loss-of-function (autosomal recessive), with mention of heterozygous dominant-negative SLC6A3 variants in atypical DTDS in a comparative review. (ng2023dopaminetransporterdeficiency pages 1-2, thalib2025acomparativeexploration pages 3-4)
- **DRD1 (dopamine receptor D1)**: homozygous missense **c.110C>A (p.T37K)** with in vitro loss-of-function in a consanguineous family; proposed as a new disease gene. (reid2023lossoffunctionvariantsin pages 1-2)
- **SLC18A2 (VMAT2)**: PKDYS2/parkinsonism-dystonia-2; autosomal recessive. Example variant in 2024 case: **NM_003054.4:c.1107dup, p.(Val370Serfs*91)**. (kaasalainen2024novelslc18a2variant pages 1-2)

### 4.2 Pathogenic variant classes and functional consequences
**SLC6A3 (reviewed in 2023):** Pathogenic variants include protein-truncating variants (nonsense, splice-site, deletions) and missense substitutions, with functional consequences including reduced transporter activity, impaired dopamine binding, reduced cell-surface expression, and impaired glycosylation. (ng2023dopaminetransporterdeficiency pages 1-2)

**DRD1 p.T37K (2023):** In vitro and modeling indicate loss of receptor function (reduced cAMP response; reduced ligand binding). (reid2023lossoffunctionvariantsin pages 1-2, reid2023lossoffunctionvariantsin pages 10-12)

**SLC18A2 PKDYS2 (2024):** frameshift variant consistent with loss-of-function mechanism; clinical presentation consistent with severe infantile dystonia-parkinsonism. (kaasalainen2024novelslc18a2variant pages 1-2)

### 4.3 Genotype–phenotype / case counts (DTDS)
The DTDS review summarizes published case numbers: “thirty-one DTDS patients reported in the literature,” plus “a further unpublished twenty patients reported to our centre.” (ng2023dopaminetransporterdeficiency pages 2-3)

---

## 5. Environmental Information
No disease-relevant environmental or lifestyle contributors were identified in the retrieved evidence; the disorders discussed are primarily genetic neurotransmitter/transportopathies.

---

## 6. Mechanism / Pathophysiology

### 6.1 DTDS (SLC6A3) mechanistic chain (integrated from multiple evidence sources)
**Upstream trigger:** loss-of-function in DAT (SLC6A3) reduces dopamine reuptake capacity (ng2023dopaminetransporterdeficiency pages 1-2)

**Biochemical consequence (CSF):** elevated dopamine catabolism marker HVA with normal 5-HIAA; elevated HVA:5-HIAA ratio (often 5.0–13.0; normal 1.0–4.0). (ng2023dopaminetransporterdeficiency pages 2-3)

**Cellular consequences:** patient iPSC-derived midbrain dopaminergic neurons show impaired DAT activity with dopamine toxicity, oxidative/carbonyl stress, inflammation-associated apoptosis, and dopaminergic neurodegeneration. (ng2021genetherapyrestores pages 4-6, ng2021genetherapyrestores pages 1-3, ng2021genetherapyrestores pages 17-25)

**Circuit/organ consequences:** DTDS knockout mice exhibit tremor, bradykinesia, and premature death; gene replacement rescues motor phenotype and neurodegeneration in vivo, supporting a causal link between transporter loss and progressive neurological dysfunction. (ng2021genetherapyrestores pages 1-3, ng2021genetherapyrestores pages 6-8)

### 6.2 DAT variant mechanism (example: R445C) and “pharmacological rescue” concept
A DTDS-associated DAT substitution **R445C** disrupts a conserved intracellular gating interaction network, producing compromised transporter function and reduced expression/trafficking; Drosophila expressing hDAT R445C show motor coordination defects, and dietary **chloroquine** (lysosomal inhibitor) improves a flight-initiation phenotype, consistent with partially restoring DAT maturation/availability. (aguilar2021psychomotorimpairmentsand pages 1-2, aguilar2021psychomotorimpairmentsand pages 14-16)

### 6.3 DRD1 mechanism
The DRD1 p.T37K variant is predicted and shown to reduce ligand binding and downstream receptor signaling (cAMP response), yielding an infantile parkinsonism–dystonia phenotype despite unexpectedly normal CSF neurotransmitter measures, suggesting postsynaptic dopamine signaling failure can phenocopy presynaptic dopamine deficiency syndromes. (reid2023lossoffunctionvariantsin pages 1-2, reid2023lossoffunctionvariantsin pages 10-12)

### 6.4 Suggested GO biological process terms (examples)
- Dopamine transport (GO:0015872) (aligned to DTDS/SLC6A3 mechanism) (ng2023dopaminetransporterdeficiency pages 1-2)
- Dopamine uptake involved in synaptic transmission (GO:0051583) (ng2023dopaminetransporterdeficiency pages 1-2)
- Regulation of dopamine secretion (GO:0014043) (relevant to vesicular transport, SLC18A2) (kaasalainen2024novelslc18a2variant pages 1-2)
- Neuronal apoptotic process (GO:0051402) (supported by iPSC apoptosis findings) (ng2021genetherapyrestores pages 4-6)
- Neuroinflammatory response (GO:0150076) (supported by TNFα-mediated inflammation in iPSC model) (ng2021genetherapyrestores pages 1-3)

### 6.5 Suggested CL (cell types) and UBERON (anatomy) terms
**Cell types (CL):**
- Midbrain dopaminergic neuron (CL:2000091) (supported by iPSC mDA neuron modeling) (ng2021genetherapyrestores pages 1-3)
- Striatal medium spiny neuron (CL:0000540) (electrophysiological/circuit consequences discussed in DTDS models) (ng2021genetherapyrestores pages 8-9)

**Anatomy (UBERON):**
- Substantia nigra (UBERON:0002038) and striatum (UBERON:0002435), targeted/affected in DTDS gene therapy studies (ng2021genetherapyrestores pages 6-8)

---

## 7. Anatomical Structures Affected
Evidence from DTDS modeling and therapeutic targeting implicates the **nigrostriatal dopaminergic system**, including substantia nigra and striatum, as critical affected/targeted structures (demonstrated by targeted AAV2.SLC6A3 delivery to substantia nigra with anterograde transport to striatum and motor rescue). (ng2021genetherapyrestores pages 8-9, ng2021genetherapyrestores pages 6-8)

---

## 8. Temporal Development
- **DTDS onset:** typically early infancy; review states presentation “within the first 6 months of life.” (thalib2025acomparativeexploration pages 3-4)
- **Progression:** DTDS is described as progressive with transition from early hyperkinesia to severe childhood parkinsonism-dystonia. (ng2023dopaminetransporterdeficiency pages 2-3)

---

## 9. Inheritance and Population

### 9.1 Inheritance patterns
- DTDS: primarily autosomal recessive biallelic SLC6A3 loss-of-function; atypical forms may include dominant-negative mechanisms (as described in a comparative review). (ng2023dopaminetransporterdeficiency pages 1-2, thalib2025acomparativeexploration pages 3-4)
- DRD1: autosomal recessive in the reported family (homozygous variant in proband; heterozygous parents). (reid2023lossoffunctionvariantsin pages 6-8)
- PKDYS2 (SLC18A2): autosomal recessive. (kaasalainen2024novelslc18a2variant pages 1-2, almutair2026casereporttwo pages 2-4)

### 9.2 Epidemiology / frequency
DTDS is described as **ultrarare**; a 2023 review summarizes a published case count (~31 in the literature) plus additional unpublished cases known to a specialist center, and reports deaths in childhood with mean reported age of death 10.4 years (see Prognosis below). (ng2023dopaminetransporterdeficiency pages 2-3)

Robust prevalence/incidence rates were not present in the retrieved evidence.

---

## 10. Diagnostics

### 10.1 Key biochemical and imaging findings (DTDS)
- **CSF neurotransmitter metabolites:** raised HVA with normal 5-HIAA; HVA:5-HIAA ratio typically **5.0–13.0** (normal 1.0–4.0). (ng2023dopaminetransporterdeficiency pages 2-3)
- **Functional presynaptic dopaminergic imaging:** SPECT with 123I-ioflupane (DaTScan) shows “absent or significantly reduced tracer uptake in the basal nuclei” in DTDS. (ng2023dopaminetransporterdeficiency pages 2-3)
- **Brain MRI:** may be normal or show nonspecific abnormalities (e.g., mild delayed myelination, white matter abnormalities, prominence of external frontotemporal spaces). (ng2023dopaminetransporterdeficiency pages 2-3)

### 10.2 Genetic testing approach
A comparative review states that DTDS diagnosis is confirmed by pathogenic SLC6A3 variants and that the “diagnostic test of choice is a genetic panel such as whole exome sequencing (WES).” (thalib2025acomparativeexploration pages 3-4)

**Recent real-world implementation examples:**
- DRD1 case used trio WGS (30×) and Sanger segregation confirmation. (reid2023lossoffunctionvariantsin pages 2-4)
- PKDYS2 case used WES to identify a homozygous SLC18A2 frameshift variant. (kaasalainen2024novelslc18a2variant pages 1-2)

### 10.3 Differential diagnosis considerations
IPD/DTDS can be confused with other early-onset neurogenetic or neurotransmitter disorders; DRD1 report emphasizes phenotypic similarity to monoamine disorders (e.g., AADC deficiency). (reid2023lossoffunctionvariantsin pages 10-12)

---

## 11. Outcome / Prognosis
A 2023 DTDS review reports severe outcomes including childhood death: “eight children have died… mean age of death of 10.4 years.” (ng2023dopaminetransporterdeficiency pages 2-3)

Longitudinal functional outcomes in PKDYS2 include severe disability with need for assistance for all activities (case report by age 9). (kaasalainen2024novelslc18a2variant pages 2-3)

---

## 12. Treatment

### 12.1 Symptomatic pharmacotherapy (DTDS)
The 2023 DTDS review states there is “limited response to standard pharmacotherapies,” with symptomatic approaches including:
- tetrabenazine and benzodiazepines for chorea/dyskinesia (ng2023dopaminetransporterdeficiency pages 2-3)
- dopamine agonists (e.g., pramipexole, ropinirole) (ng2023dopaminetransporterdeficiency pages 2-3)
- gabapentin for stiffness in some cases (ng2023dopaminetransporterdeficiency pages 2-3)
- levodopa: “limited or no response to levodopa treatment.” (ng2023dopaminetransporterdeficiency pages 2-3)

**MAXO suggestions (examples):**
- Dopamine agonist therapy (MAXO:0001027)
- Levodopa therapy (MAXO:0000746)
- Tetrabenazine therapy / monoamine depletion therapy (MAXO term may vary by ontology version; treat as “vesicular monoamine transporter inhibitor therapy”)
- Benzodiazepine therapy (MAXO:0000558)

### 12.2 Treatment response in DRD1 infantile parkinsonism-dystonia
- No response to levodopa up to 10 mg/kg/day; dopaminergic therapy ineffective, consistent with in vitro failure of D1 agonists to rescue receptor defect. (reid2023lossoffunctionvariantsin pages 12-13, reid2023lossoffunctionvariantsin pages 6-8)
- Modest benefit reported from some tone-modifying agents and transdermal clonidine. (reid2023lossoffunctionvariantsin pages 6-8)

### 12.3 Treatment response in PKDYS2 (SLC18A2)
The 2024 PKDYS2 case report describes trials including valproate, levodopa-carbidopa, pramipexole, amantadine, methylphenidate with variable/limited benefit and frequent adverse effects; it also notes that levodopa in PKDYS2 “almost always worsens” in prior reports, with dopamine agonists variably beneficial. (kaasalainen2024novelslc18a2variant pages 1-2, kaasalainen2024novelslc18a2variant pages 2-3)

### 12.4 Advanced therapeutics and experimental approaches (DTDS)
**Gene therapy as a major translational direction:**
- A 2021 Science Translational Medicine study demonstrates that viral gene transfer of wild-type SLC6A3 restores DAT activity and prevents neurodegeneration in patient-derived iPSC midbrain dopaminergic neurons, and that AAV delivery improves motor phenotype, lifespan, and neuronal survival in DTDS mouse models, with dose-related off-target toxicity at high doses and improved safety with targeted midbrain AAV2.SLC6A3 delivery. (Published May 2021; https://doi.org/10.1126/scitranslmed.aaw1564). (ng2021genetherapyrestores pages 1-3, ng2021genetherapyrestores pages 6-8)

**Expert/authoritative perspective on translation (2023):**
A 2023 Movement Disorders review frames a regulatory and translational landscape for dopamine gene therapies, noting approval of Upstaza (AADC deficiency) as an “important land-mark” while emphasizing that “numerous challenges remain,” including defining the “optimal therapeutic window,” durability of effect, and improved brain targeting—issues directly relevant to DTDS translation. (Published May 2023; https://doi.org/10.1002/mds.29416). (ng2023genetherapyfor pages 1-2)

---

## 13. Prevention
No primary prevention is applicable for these Mendelian disorders beyond genetic counseling and reproductive options.

**Secondary/tertiary prevention concept:** early molecular diagnosis (WES/WGS) may reduce diagnostic delay and avoid ineffective treatments; emphasized in PKDYS2 sibling case conclusions and DTDS diagnostic summaries. (almutair2026casereporttwo pages 2-4, thalib2025acomparativeexploration pages 3-4)

---

## 14. Other Species / Natural Disease
No naturally occurring (non-experimental) animal disease analogs were identified in the retrieved evidence.

---

## 15. Model Organisms
Evidence-supported models include:

1) **Patient-derived iPSC midbrain dopaminergic neurons (DTDS/SLC6A3):** show impaired DAT activity, apoptotic neurodegeneration, TNFα-mediated inflammation, and dopamine toxicity; enable testing of pharmacochaperones and viral gene replacement. (ng2021genetherapyrestores pages 1-3, ng2021genetherapyrestores pages 17-25)

2) **DAT knockout mouse (DTDS/SLC6A3):** recapitulates tremor, bradykinesia, and premature death; used for AAV2.SLC6A3 dose-ranging, motor rescue, survival outcomes, and targeting strategy development. (ng2021genetherapyrestores pages 1-3, ng2021genetherapyrestores pages 8-9)

3) **Drosophila DAT variant model (hDAT R445C):** demonstrates impaired DAT activity, dopamine dysfunction, motor coordination phenotypes (including flight coordination), and pharmacologic rescue by chloroquine via increased DAT maturation/expression. (aguilar2021psychomotorimpairmentsand pages 1-2, aguilar2021psychomotorimpairmentsand pages 14-16)

---

## Recent developments and latest research (prioritizing 2023–2024)
1) **New disease gene for infantile parkinsonism-dystonia (DRD1):** 2023 Cells report nominates DRD1 as a new disease-associated gene with recessive loss-of-function and severe infantile phenotype, with normal CSF neurotransmitter analysis and poor response to dopaminergic therapy. (Mar 2023; https://doi.org/10.3390/cells12071046). (reid2023lossoffunctionvariantsin pages 1-2, reid2023lossoffunctionvariantsin pages 6-8)

2) **DTDS precision medicine framing (2023 Cells review):** summarizes expanding phenotype, typical diagnostic findings (CSF ratio, DaTScan), case counts, limited levodopa response, and highlights pharmacochaperones and gene therapy in development. (Jun 2023; https://doi.org/10.3390/cells12131737). (ng2023dopaminetransporterdeficiency pages 2-3)

3) **SLC18A2 PKDYS2 case expansion (2024):** reports a novel frameshift variant diagnosed via WES with extensive medication trials documenting limited or transient responses and adverse effects. (Apr 2024; https://doi.org/10.1155/2024/4767647). (kaasalainen2024novelslc18a2variant pages 1-2, kaasalainen2024novelslc18a2variant pages 2-3)

4) **Gene therapy translation analysis (2023 Movement Disorders):** emphasizes therapeutic window, targeting specificity, and durability as key unresolved questions across dopamine gene therapies (relevant to DTDS). (May 2023; https://doi.org/10.1002/mds.29416). (ng2023genetherapyfor pages 1-2, ng2023genetherapyfor pages 9-11)

---

## Summary Table (evidence-backed)
The following table consolidates key Mendelian causes and distinguishing diagnostic/treatment features captured in the retrieved evidence.

| Disease label used in papers | Causal gene | Inheritance | Key distinguishing clinical features | Key diagnostic tests/findings | Typical treatment response notes | Key recent references |
|---|---|---|---|---|---|---|
| Dopamine transporter deficiency syndrome (DTDS); infantile parkinsonism-dystonia | **SLC6A3** | Usually autosomal recessive due to biallelic loss-of-function variants; review also notes heterozygous dominant-negative **SLC6A3** variants in atypical DTDS (thalib2025acomparativeexploration pages 3-4, ng2023dopaminetransporterdeficiency pages 1-2) | Infantile onset, often within first 6 months; irritability, feeding difficulties, hypotonia, delayed motor milestones; hyperkinetic movements (chorea, dystonia, ballismus, orolingual dyskinesia) progressing to parkinsonism-dystonia with bradykinesia, tremor, rigidity, akinesia; oculogyric crises/status dystonicus; dysautonomia and severe disability in many cases (ng2023dopaminetransporterdeficiency pages 2-3, thalib2025acomparativeexploration pages 1-3) | CSF: raised HVA with normal 5-HIAA; HVA:5-HIAA ratio typically **5.0–13.0** (normal 1.0–4.0), or practical cutoff **>4**; DaTScan/SPECT: absent or markedly reduced basal nuclei uptake; MRI may be normal or show mild delayed myelination/white-matter abnormalities/prominent frontotemporal spaces; diagnosis confirmed by WES/gene panel/WGS showing pathogenic **SLC6A3** variants (ng2023dopaminetransporterdeficiency pages 2-3, thalib2025acomparativeexploration pages 3-4) | Limited response to standard pharmacotherapy; tetrabenazine and benzodiazepines used for chorea/dyskinesia; dopamine agonists such as pramipexole/ropinirole sometimes used; gabapentin may help stiffness; limited or no response to levodopa; DBS and intrathecal baclofen reported with limited benefit; preclinical gene therapy and pharmacochaperone approaches under development (ng2023dopaminetransporterdeficiency pages 2-3, ng2021genetherapyrestores pages 1-3, ng2023genetherapyfor pages 1-2) | Ng et al., 2023, https://doi.org/10.3390/cells12131737; Ng et al., 2023, https://doi.org/10.1002/mds.29416 (ng2023dopaminetransporterdeficiency pages 2-3, ng2023genetherapyfor pages 1-2) |
| Infantile parkinsonism-dystonia due to **DRD1** loss of function | **DRD1** | Autosomal recessive in reported case (homozygous variant) (reid2023lossoffunctionvariantsin pages 12-13, reid2023lossoffunctionvariantsin pages 1-2) | Severe infantile parkinsonism-dystonia with frequent oculogyric crises, dysautonomia, global neurodevelopmental impairment; paucity of spontaneous movement, hypomimia, truncal hypotonia with variable limb tone, prolonged generalized dystonia, feeding impairment, reflux, constipation, sweating, chronic nasal congestion; failed to sit/roll/babble (reid2023lossoffunctionvariantsin pages 1-2, reid2023lossoffunctionvariantsin pages 6-8) | Trio WGS identified homozygous **DRD1** c.110C>A (p.T37K), absent from gnomAD; CSF neurotransmitters/AADC activity were normal, with slight increase in HVA:5-HIAA noted in supplementary data; MRI referenced in supplementary materials; functional assays showed markedly reduced D1 receptor signaling/ligand binding (reid2023lossoffunctionvariantsin pages 12-13, reid2023lossoffunctionvariantsin pages 1-2, reid2023lossoffunctionvariantsin pages 6-8, reid2023lossoffunctionvariantsin pages 8-10) | No clinical response to levodopa up to 10 mg/kg/day; numerous D1 agonists failed to rescue the cellular defect, matching lack of dopaminergic benefit clinically; modest benefit from some tone-modifying agents and transdermal clonidine reported (reid2023lossoffunctionvariantsin pages 12-13, reid2023lossoffunctionvariantsin pages 6-8, reid2023lossoffunctionvariantsin pages 10-12) | Reid et al., 2023, https://doi.org/10.3390/cells12071046 (reid2023lossoffunctionvariantsin pages 1-2, reid2023lossoffunctionvariantsin pages 12-13) |
| Infantile dystonia-parkinsonism type 2 (PKDYS2); parkinsonism-dystonia-2; brain dopamine-serotonin vesicular transport disease | **SLC18A2** | Autosomal recessive (reported homozygous variants) (kaasalainen2024novelslc18a2variant pages 1-2, almutair2026casereporttwo pages 2-4) | Onset in early infancy; global developmental delay, generalized hypotonia, hyperkinetic movements/dystonia, parkinsonism, oculogyric crises, temperature instability/autonomic features, severe speech and motor impairment, feeding/swallowing problems; many remain nonambulatory and dependent for all activities (kaasalainen2024novelslc18a2variant pages 1-2, kaasalainen2024novelslc18a2variant pages 2-3, kaasalainen2024novelslc18a2variant pages 3-4, almutair2026casereporttwo pages 2-4) | WES identified homozygous **SLC18A2** variants including frameshift **c.1107dup p.(Val370Serfs*91)** and splice-site **c.1122+2T>C**; EEG may show no epileptiform activity; brain MRI can be unremarkable/normal; CSF testing was planned but not available in one 2026 report (kaasalainen2024novelslc18a2variant pages 1-2, kaasalainen2024novelslc18a2variant pages 2-3, almutair2026casereporttwo pages 2-4) | Levodopa often ineffective or may worsen symptoms; pramipexole can give partial/initial benefit (head support, swallowing, breathing, reduced dystonic episodes) but adverse effects may limit use; valproate mild or unclear benefit; amantadine no clear benefit; methylphenidate may transiently improve alertness/head support but can worsen dystonia/side effects (kaasalainen2024novelslc18a2variant pages 1-2, kaasalainen2024novelslc18a2variant pages 2-3, almutair2026casereporttwo pages 2-4) | Kaasalainen et al., 2024, https://doi.org/10.1155/2024/4767647 (kaasalainen2024novelslc18a2variant pages 1-2, kaasalainen2024novelslc18a2variant pages 2-3) |


*Table: This table summarizes Mendelian causes discussed in the retrieved evidence for infantile parkinsonism-dystonia and related infantile dystonia-parkinsonism disorders. It compares genes, inheritance, distinguishing clinical features, diagnostic findings, treatment response patterns, and recent references supported by the available evidence snippets.*

---

## Limitations of this report (due to available tool evidence)
- Several required identifiers (MONDO, Orphanet, MeSH, ICD codes) and population-level prevalence/incidence were not present in the retrieved full-text snippets; they are therefore not reported to avoid uncited or inaccurate assertions.
- Many classic DTDS primary series (e.g., earliest cohorts) are referenced within reviews but were not directly available as full text in the retrieved evidence set for direct PMID-quoting.



References

1. (ng2023dopaminetransporterdeficiency pages 2-3): Joanne Ng, Serena Barral, Simon N. Waddington, and Manju A. Kurian. Dopamine transporter deficiency syndrome (dtds): expanding the clinical phenotype and precision medicine approaches. Cells, 12:1737, Jun 2023. URL: https://doi.org/10.3390/cells12131737, doi:10.3390/cells12131737. This article has 27 citations.

2. (ng2023dopaminetransporterdeficiency pages 1-2): Joanne Ng, Serena Barral, Simon N. Waddington, and Manju A. Kurian. Dopamine transporter deficiency syndrome (dtds): expanding the clinical phenotype and precision medicine approaches. Cells, 12:1737, Jun 2023. URL: https://doi.org/10.3390/cells12131737, doi:10.3390/cells12131737. This article has 27 citations.

3. (reid2023lossoffunctionvariantsin pages 1-2): Genomics England Research, Kimberley M Reid, D. Steel, Sanjana Nair, S. Bhate, L. Biassoni, S. Sudhakar, M. Heys, Elizabeth A Burke, E. Kamsteeg, Genomics England, Research Consortium, B. Hameed, M. Zech, N. Mencacci, Katy Barwick, M. Topf, and M. Kurian. Loss-of-function variants in drd1 in infantile parkinsonism-dystonia. Cells, 12:1046, Mar 2023. URL: https://doi.org/10.3390/cells12071046, doi:10.3390/cells12071046. This article has 15 citations.

4. (kaasalainen2024novelslc18a2variant pages 1-2): Sakari Kaasalainen, Harri Arikka, Mika H. Martikainen, and Valtteri Kaasinen. Novel slc18a2 variant in infantile dystonia-parkinsonism type 2. Case Reports in Neurological Medicine, Apr 2024. URL: https://doi.org/10.1155/2024/4767647, doi:10.1155/2024/4767647. This article has 3 citations and is from a peer-reviewed journal.

5. (almutair2026casereporttwo pages 2-4): Meshal Almutair and Wejdan S. Hakami. Case report: two siblings with a novel homozygous slc18a2 variant causing parkinsonism-dystonia-2: a case series from saudi arabia. Frontiers in Genetics, May 2026. URL: https://doi.org/10.3389/fgene.2026.1812336, doi:10.3389/fgene.2026.1812336. This article has 0 citations and is from a peer-reviewed journal.

6. (ng2021genetherapyrestores pages 1-3): Joanne Ng, Serena Barral, Carmen De La Fuente Barrigon, Gabriele Lignani, Fatma A. Erdem, Rebecca Wallings, Riccardo Privolizzi, Giada Rossignoli, Haya Alrashidi, Sonja Heasman, Esther Meyer, Adeline Ngoh, Simon Pope, Rajvinder Karda, Dany Perocheau, Julien Baruteau, Natalie Suff, Juan Antinao Diaz, Stephanie Schorge, Jane Vowles, Lucy R. Marshall, Sally A. Cowley, Sonja Sucic, Michael Freissmuth, John R. Counsell, Richard Wade-Martins, Simon J. R. Heales, Ahad A. Rahim, Maximilien Bencze, Simon N. Waddington, and Manju A. Kurian. Gene therapy restores dopamine transporter expression and ameliorates pathology in ipsc and mouse models of infantile parkinsonism. Science Translational Medicine, May 2021. URL: https://doi.org/10.1126/scitranslmed.aaw1564, doi:10.1126/scitranslmed.aaw1564. This article has 59 citations and is from a highest quality peer-reviewed journal.

7. (aguilar2021psychomotorimpairmentsand pages 1-2): Jenny I Aguilar, Mary Hongying Cheng, Josep Font, Alexandra C Schwartz, Kaitlyn Ledwitch, Amanda Duran, Samuel J Mabry, Andrea N Belovich, Yanqi Zhu, Angela M Carter, Lei Shi, Manju A Kurian, Cristina Fenollar-Ferrer, Jens Meiler, Renae Monique Ryan, Hassane S Mchaourab, Ivet Bahar, Heinrich JG Matthies, and Aurelio Galli. Psychomotor impairments and therapeutic implications revealed by a mutation associated with infantile parkinsonism-dystonia. May 2021. URL: https://doi.org/10.7554/elife.68039, doi:10.7554/elife.68039. This article has 24 citations and is from a domain leading peer-reviewed journal.

8. (kaasalainen2024novelslc18a2variant pages 2-3): Sakari Kaasalainen, Harri Arikka, Mika H. Martikainen, and Valtteri Kaasinen. Novel slc18a2 variant in infantile dystonia-parkinsonism type 2. Case Reports in Neurological Medicine, Apr 2024. URL: https://doi.org/10.1155/2024/4767647, doi:10.1155/2024/4767647. This article has 3 citations and is from a peer-reviewed journal.

9. (thalib2025acomparativeexploration pages 3-4): Husna Irfan Thalib, Rand Redwan Al Sari, Syeda Sobiah Imad, Sariya Khan, Shyma Haidar, Bayan Mohammed Khair Al Zoabi, Sahar Hamed Fadda, Samratul Fuadah, Hassan Abu Alwan, and Abdullah Alghobaishi. A comparative exploration of monoamine neurotransmitter transport disorders: mechanisms, clinical manifestations, and therapeutic approaches. Journal of Medicine and Life, 18:188-195, Mar 2025. URL: https://doi.org/10.25122/jml-2024-0398, doi:10.25122/jml-2024-0398. This article has 3 citations.

10. (reid2023lossoffunctionvariantsin pages 6-8): Genomics England Research, Kimberley M Reid, D. Steel, Sanjana Nair, S. Bhate, L. Biassoni, S. Sudhakar, M. Heys, Elizabeth A Burke, E. Kamsteeg, Genomics England, Research Consortium, B. Hameed, M. Zech, N. Mencacci, Katy Barwick, M. Topf, and M. Kurian. Loss-of-function variants in drd1 in infantile parkinsonism-dystonia. Cells, 12:1046, Mar 2023. URL: https://doi.org/10.3390/cells12071046, doi:10.3390/cells12071046. This article has 15 citations.

11. (reid2023lossoffunctionvariantsin pages 10-12): Genomics England Research, Kimberley M Reid, D. Steel, Sanjana Nair, S. Bhate, L. Biassoni, S. Sudhakar, M. Heys, Elizabeth A Burke, E. Kamsteeg, Genomics England, Research Consortium, B. Hameed, M. Zech, N. Mencacci, Katy Barwick, M. Topf, and M. Kurian. Loss-of-function variants in drd1 in infantile parkinsonism-dystonia. Cells, 12:1046, Mar 2023. URL: https://doi.org/10.3390/cells12071046, doi:10.3390/cells12071046. This article has 15 citations.

12. (ng2021genetherapyrestores pages 4-6): Joanne Ng, Serena Barral, Carmen De La Fuente Barrigon, Gabriele Lignani, Fatma A. Erdem, Rebecca Wallings, Riccardo Privolizzi, Giada Rossignoli, Haya Alrashidi, Sonja Heasman, Esther Meyer, Adeline Ngoh, Simon Pope, Rajvinder Karda, Dany Perocheau, Julien Baruteau, Natalie Suff, Juan Antinao Diaz, Stephanie Schorge, Jane Vowles, Lucy R. Marshall, Sally A. Cowley, Sonja Sucic, Michael Freissmuth, John R. Counsell, Richard Wade-Martins, Simon J. R. Heales, Ahad A. Rahim, Maximilien Bencze, Simon N. Waddington, and Manju A. Kurian. Gene therapy restores dopamine transporter expression and ameliorates pathology in ipsc and mouse models of infantile parkinsonism. Science Translational Medicine, May 2021. URL: https://doi.org/10.1126/scitranslmed.aaw1564, doi:10.1126/scitranslmed.aaw1564. This article has 59 citations and is from a highest quality peer-reviewed journal.

13. (ng2021genetherapyrestores pages 17-25): Joanne Ng, Serena Barral, Carmen De La Fuente Barrigon, Gabriele Lignani, Fatma A. Erdem, Rebecca Wallings, Riccardo Privolizzi, Giada Rossignoli, Haya Alrashidi, Sonja Heasman, Esther Meyer, Adeline Ngoh, Simon Pope, Rajvinder Karda, Dany Perocheau, Julien Baruteau, Natalie Suff, Juan Antinao Diaz, Stephanie Schorge, Jane Vowles, Lucy R. Marshall, Sally A. Cowley, Sonja Sucic, Michael Freissmuth, John R. Counsell, Richard Wade-Martins, Simon J. R. Heales, Ahad A. Rahim, Maximilien Bencze, Simon N. Waddington, and Manju A. Kurian. Gene therapy restores dopamine transporter expression and ameliorates pathology in ipsc and mouse models of infantile parkinsonism. Science Translational Medicine, May 2021. URL: https://doi.org/10.1126/scitranslmed.aaw1564, doi:10.1126/scitranslmed.aaw1564. This article has 59 citations and is from a highest quality peer-reviewed journal.

14. (ng2021genetherapyrestores pages 6-8): Joanne Ng, Serena Barral, Carmen De La Fuente Barrigon, Gabriele Lignani, Fatma A. Erdem, Rebecca Wallings, Riccardo Privolizzi, Giada Rossignoli, Haya Alrashidi, Sonja Heasman, Esther Meyer, Adeline Ngoh, Simon Pope, Rajvinder Karda, Dany Perocheau, Julien Baruteau, Natalie Suff, Juan Antinao Diaz, Stephanie Schorge, Jane Vowles, Lucy R. Marshall, Sally A. Cowley, Sonja Sucic, Michael Freissmuth, John R. Counsell, Richard Wade-Martins, Simon J. R. Heales, Ahad A. Rahim, Maximilien Bencze, Simon N. Waddington, and Manju A. Kurian. Gene therapy restores dopamine transporter expression and ameliorates pathology in ipsc and mouse models of infantile parkinsonism. Science Translational Medicine, May 2021. URL: https://doi.org/10.1126/scitranslmed.aaw1564, doi:10.1126/scitranslmed.aaw1564. This article has 59 citations and is from a highest quality peer-reviewed journal.

15. (aguilar2021psychomotorimpairmentsand pages 14-16): Jenny I Aguilar, Mary Hongying Cheng, Josep Font, Alexandra C Schwartz, Kaitlyn Ledwitch, Amanda Duran, Samuel J Mabry, Andrea N Belovich, Yanqi Zhu, Angela M Carter, Lei Shi, Manju A Kurian, Cristina Fenollar-Ferrer, Jens Meiler, Renae Monique Ryan, Hassane S Mchaourab, Ivet Bahar, Heinrich JG Matthies, and Aurelio Galli. Psychomotor impairments and therapeutic implications revealed by a mutation associated with infantile parkinsonism-dystonia. May 2021. URL: https://doi.org/10.7554/elife.68039, doi:10.7554/elife.68039. This article has 24 citations and is from a domain leading peer-reviewed journal.

16. (ng2021genetherapyrestores pages 8-9): Joanne Ng, Serena Barral, Carmen De La Fuente Barrigon, Gabriele Lignani, Fatma A. Erdem, Rebecca Wallings, Riccardo Privolizzi, Giada Rossignoli, Haya Alrashidi, Sonja Heasman, Esther Meyer, Adeline Ngoh, Simon Pope, Rajvinder Karda, Dany Perocheau, Julien Baruteau, Natalie Suff, Juan Antinao Diaz, Stephanie Schorge, Jane Vowles, Lucy R. Marshall, Sally A. Cowley, Sonja Sucic, Michael Freissmuth, John R. Counsell, Richard Wade-Martins, Simon J. R. Heales, Ahad A. Rahim, Maximilien Bencze, Simon N. Waddington, and Manju A. Kurian. Gene therapy restores dopamine transporter expression and ameliorates pathology in ipsc and mouse models of infantile parkinsonism. Science Translational Medicine, May 2021. URL: https://doi.org/10.1126/scitranslmed.aaw1564, doi:10.1126/scitranslmed.aaw1564. This article has 59 citations and is from a highest quality peer-reviewed journal.

17. (reid2023lossoffunctionvariantsin pages 2-4): Genomics England Research, Kimberley M Reid, D. Steel, Sanjana Nair, S. Bhate, L. Biassoni, S. Sudhakar, M. Heys, Elizabeth A Burke, E. Kamsteeg, Genomics England, Research Consortium, B. Hameed, M. Zech, N. Mencacci, Katy Barwick, M. Topf, and M. Kurian. Loss-of-function variants in drd1 in infantile parkinsonism-dystonia. Cells, 12:1046, Mar 2023. URL: https://doi.org/10.3390/cells12071046, doi:10.3390/cells12071046. This article has 15 citations.

18. (reid2023lossoffunctionvariantsin pages 12-13): Genomics England Research, Kimberley M Reid, D. Steel, Sanjana Nair, S. Bhate, L. Biassoni, S. Sudhakar, M. Heys, Elizabeth A Burke, E. Kamsteeg, Genomics England, Research Consortium, B. Hameed, M. Zech, N. Mencacci, Katy Barwick, M. Topf, and M. Kurian. Loss-of-function variants in drd1 in infantile parkinsonism-dystonia. Cells, 12:1046, Mar 2023. URL: https://doi.org/10.3390/cells12071046, doi:10.3390/cells12071046. This article has 15 citations.

19. (ng2023genetherapyfor pages 1-2): Joanne Ng, Serena Barral, Simon N. Waddington, and Manju A. Kurian. Gene therapy for dopamine dyshomeostasis: from parkinson's to primary neurotransmitter diseases. Movement Disorders, 38:924-936, May 2023. URL: https://doi.org/10.1002/mds.29416, doi:10.1002/mds.29416. This article has 23 citations and is from a highest quality peer-reviewed journal.

20. (ng2023genetherapyfor pages 9-11): Joanne Ng, Serena Barral, Simon N. Waddington, and Manju A. Kurian. Gene therapy for dopamine dyshomeostasis: from parkinson's to primary neurotransmitter diseases. Movement Disorders, 38:924-936, May 2023. URL: https://doi.org/10.1002/mds.29416, doi:10.1002/mds.29416. This article has 23 citations and is from a highest quality peer-reviewed journal.

21. (thalib2025acomparativeexploration pages 1-3): Husna Irfan Thalib, Rand Redwan Al Sari, Syeda Sobiah Imad, Sariya Khan, Shyma Haidar, Bayan Mohammed Khair Al Zoabi, Sahar Hamed Fadda, Samratul Fuadah, Hassan Abu Alwan, and Abdullah Alghobaishi. A comparative exploration of monoamine neurotransmitter transport disorders: mechanisms, clinical manifestations, and therapeutic approaches. Journal of Medicine and Life, 18:188-195, Mar 2025. URL: https://doi.org/10.25122/jml-2024-0398, doi:10.25122/jml-2024-0398. This article has 3 citations.

22. (reid2023lossoffunctionvariantsin pages 8-10): Genomics England Research, Kimberley M Reid, D. Steel, Sanjana Nair, S. Bhate, L. Biassoni, S. Sudhakar, M. Heys, Elizabeth A Burke, E. Kamsteeg, Genomics England, Research Consortium, B. Hameed, M. Zech, N. Mencacci, Katy Barwick, M. Topf, and M. Kurian. Loss-of-function variants in drd1 in infantile parkinsonism-dystonia. Cells, 12:1046, Mar 2023. URL: https://doi.org/10.3390/cells12071046, doi:10.3390/cells12071046. This article has 15 citations.

23. (kaasalainen2024novelslc18a2variant pages 3-4): Sakari Kaasalainen, Harri Arikka, Mika H. Martikainen, and Valtteri Kaasinen. Novel slc18a2 variant in infantile dystonia-parkinsonism type 2. Case Reports in Neurological Medicine, Apr 2024. URL: https://doi.org/10.1155/2024/4767647, doi:10.1155/2024/4767647. This article has 3 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Infantile_Parkinsonism-Dystonia-deep-research-falcon_artifacts/artifact-00.md)