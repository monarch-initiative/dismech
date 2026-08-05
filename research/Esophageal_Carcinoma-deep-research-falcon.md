---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-05T18:50:28.455153'
end_time: '2026-07-05T19:05:26.568101'
duration_seconds: 898.11
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Esophageal Carcinoma
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 57
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: Esophageal_Carcinoma-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Esophageal_Carcinoma-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Esophageal Carcinoma
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Esophageal Carcinoma** covering all of the
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
- **Disease Name:** Esophageal Carcinoma
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Esophageal Carcinoma** covering all of the
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


# Comprehensive Research Report: Esophageal Carcinoma

## 1. Disease Information

### Overview
Esophageal carcinoma (EC) is a highly aggressive malignancy of the esophagus and one of the most lethal cancers worldwide, with approximately 511,054 new cases and 445,391 deaths globally in 2022 (qi2024globalesophagealcancer pages 1-2). It is the seventh leading cause of cancer-related mortality globally, with 5-year survival rates of only 10–30% (zhang2026esophagealcancerfrom pages 1-2). EC encompasses two principal histological subtypes with distinct epidemiological, etiological, and molecular profiles: **esophageal squamous cell carcinoma (ESCC)**, accounting for approximately 80% of cases globally, and **esophageal adenocarcinoma (EAC)**, whose incidence is rising in Western countries (zhang2026esophagealcancerfrom pages 1-2, sheikh2023currentstatusand pages 15-16).

### Key Identifiers
- **ICD-10:** C15 (Malignant neoplasm of esophagus); C15.0–C15.9 for subsites
- **ICD-11:** 2B70 (Malignant neoplasms of oesophagus)
- **MeSH:** D004938 (Esophageal Neoplasms)
- **MONDO:** MONDO_0019086 (carcinoma of esophagus); MONDO_0005580 (esophageal squamous cell carcinoma); MONDO_0005028 (esophageal adenocarcinoma) (OpenTargets Search: esophageal carcinoma)
- **OMIM:** Not a single-gene Mendelian disorder; ESCC/EAC arise from complex multifactorial causes

### Common Synonyms
Esophageal cancer, oesophageal carcinoma, cancer of the esophagus, esophageal malignancy, gullet cancer.

### Data Sources
Information is derived from aggregated disease-level resources including GLOBOCAN, the Global Burden of Disease (GBD) Study, SEER, TCGA, and published clinical/epidemiological literature.

---

## 2. Etiology

### Disease Causal Factors
ESCC and EAC have distinct etiological pathways. ESCC develops through a multistep progression from normal squamous epithelium through basal cell hyperplasia and dysplasia to carcinoma, driven by chronic mucosal irritation. EAC evolves from Barrett's esophagus (BE) induced by chronic gastroesophageal reflux disease (GERD), following a stepwise progression: GERD → BE → low-grade dysplasia → high-grade dysplasia → adenocarcinoma (zhang2026esophagealcancerfrom pages 1-2, li2023molecularbiologyand pages 1-2).

### Risk Factors

#### Genetic Risk Factors
- **TP53 mutations** are the most frequently altered gene in ESCC (~90% of patients) and are prevalent in EAC, with 46% of BE progressors carrying TP53 mutations compared to 5% of nonprogressors (zhang2026esophagealcancerfrom pages 6-7).
- **CDKN2A** inactivation via promoter methylation is detected in nearly all individuals developing dysplasia (zhang2026esophagealcancerfrom pages 9-10).
- **ADH1B** polymorphisms (alcohol dehydrogenase 1B) modify acetaldehyde exposure and alcohol-related carcinogenic risk, representing a key genetic susceptibility marker (OpenTargets Search: esophageal carcinoma).
- Susceptibility loci include variants in **CTLA-4, SLC39A6, PLCE1, FOXF, BARX1,** and **ABCC5** (zhang2026esophagealcancerfrom pages 2-3, li2023molecularbiologyand pages 6-8).
- Hereditary conditions: **Tylosis** (focal non-epidermolytic palmoplantar keratoderma) is strongly associated with ESCC risk.

#### Environmental Risk Factors
- **ESCC:** Alcohol consumption, tobacco/opium smoking, dietary carcinogens (nitrosamines), hot beverages, micronutrient deficiencies, betel quid chewing, poor oral hygiene, low socioeconomic status (zhang2026esophagealcancerfrom pages 1-2, sheikh2023currentstatusand pages 15-16, liu2023epidemiologyofesophageal pages 8-9).
- **EAC:** Obesity, GERD, smoking, male sex, Caucasian ethnicity, high BMI (li2023molecularbiologyand pages 1-2, sheikh2023currentstatusand pages 15-16).
- In 2019, smoking accounted for 50.1% of DALYs for EC in males and 11.3% in females; alcohol use accounted for 29.6% in males and 5.1% in females; high BMI accounted for 18.8% in males and 19.3% in females (ilic2024globalburdenof pages 6-10).

### Protective Factors
- Diets rich in fruits and vegetables reduce risk: low-fruit diet accounted for 10.1–12.6% of DALYs (ilic2024globalburdenof pages 6-10).
- *Helicobacter pylori* infection has been paradoxically associated with reduced EAC risk.
- Aspirin and proton pump inhibitor use show chemoprevention potential for EAC (sheikh2023currentstatusand pages 15-16).

### Gene-Environment Interactions
ADH1B genetic variants interact with alcohol exposure to modulate acetaldehyde accumulation and carcinogenic risk, particularly in East Asian populations (OpenTargets Search: esophageal carcinoma). Tobacco smoke exposure combined with TP53 polymorphisms significantly increases ESCC risk (zhang2026esophagealcancerfrom pages 2-3).

---

## 3. Phenotypes

### Symptoms and Clinical Signs
- **Dysphagia** (progressive, initially to solids then liquids) — HP:0002015
- **Odynophagia** (painful swallowing) — HP:0200136
- **Unintended weight loss** — HP:0001824
- **Chest pain/retrosternal discomfort** — HP:0100749
- **Hoarseness** (recurrent laryngeal nerve involvement) — HP:0001609
- **Chronic cough** — HP:0012735
- **Hematemesis/melena** (GI bleeding) — HP:0002239
- **Fatigue** — HP:0012378
- **Iron deficiency anemia** — HP:0001891

### Phenotype Characteristics
- **Age of onset:** Predominantly adult-onset (>50 years), with peak incidence in the 60–70 age group (ilic2024globalburdenof pages 4-6).
- **Severity:** Generally severe; most patients present at advanced stages.
- **Progression:** Progressive; early-stage disease is often asymptomatic.
- **Frequency:** Dysphagia is present in >90% of symptomatic patients at diagnosis.

### Quality of Life Impact
EC significantly impairs quality of life through dysphagia, nutritional compromise, and treatment-related morbidity. The SANO trial demonstrated that active surveillance after complete clinical response to chemoradiotherapy showed noninferior overall survival and better short-term quality of life compared to surgery at 2 years (fick2024immunotherapyforresectable pages 9-10).

---

## 4. Genetic/Molecular Information

### Key Somatic Mutations (by subtype)
- **ESCC:** TP53 (~90%), NOTCH1, NFE2L2/KEAP1, KMT2D, PIK3CA, CDKN2A, FBXW7, EP300 (zhang2026esophagealcancerfrom pages 2-3, zhang2026esophagealcancerfrom pages 6-7).
- **EAC:** TP53, SMAD4, CDKN2A, ARID1A with frequent amplifications of ERBB2 (21.8%), CCNE1 (12.6%), GATA4 (10.3%), and KRAS (10.3%) (zhang2026esophagealcancerfrom pages 9-10, li2023molecularbiologyand pages 6-8).

### Pathogenic Variants
- **TP53** mutations are predominantly missense/nonsense, occurring throughout the DNA-binding domain; somatic origin in tumors; associated with genomic instability and impaired apoptosis (zhang2026esophagealcancerfrom pages 6-7).
- **CDKN2A** inactivation occurs through promoter hypermethylation, homozygous deletion, or LOH; detectable in nearly all dysplasia cases (zhang2026esophagealcancerfrom pages 9-10).
- **ERBB2** amplification in EAC (HER2+) occurs in 15–29% of cases and is an FDA-approved companion diagnostic for trastuzumab therapy (rai2023biomarkersforearly pages 8-9).
- Tumor mutation burden (TMB) in ESCC cell lines ranges from 48.7 to 70.4 mutations/Mb, with signature 3 (homologous recombination deficiency) being significantly enriched (zhang2025thegenomiclandscape pages 4-7).

### Epigenetic Information
- Genome-wide **hypomethylation** in cancer tissues and **promoter hypermethylation**-mediated silencing of tumor suppressor genes (CDKN2A, APC) are characteristic (zhang2026esophagealcancerfrom pages 8-9, zhang2026esophagealcancerfrom pages 9-10).
- APC promoter hypermethylation is observed in up to 92% of adenocarcinomas (zhang2026esophagealcancerfrom pages 9-10).
- MicroRNA dysregulation and DNA methylation patterns vary with each phase of BE, LGD, HGD, early EAC, and invasive EAC (li2023molecularbiologyand pages 16-17).
- RNA m6A demethylation affecting LINC00022 and DNMT1-microRNA126 circuits contribute to growth via ADAM9-EGFR-AKT signaling (zhang2026esophagealcancerfrom pages 30-31).
- A core gene regulatory network involving **TP63, SOX2, and KLF5** regulates chromatin accessibility in ESCC (zhang2026esophagealcancerfrom pages 9-10).

### Chromosomal Abnormalities
- Chromosomal instability (CIN) is a hallmark of both subtypes. Gene amplifications are frequent in 57% of EAC cases (zhang2026esophagealcancerfrom pages 9-10).
- Copy number variations affect SOX2, NFE2L2, and CDKN2A, progressively accumulating from early dysplasia stages (zhang2026esophagealcancerfrom pages 8-9).
- LOH at APC locus and structural variations affecting CDKN2A and NOTCH1 are recurrent (zhang2026esophagealcancerfrom pages 9-10).

The following table summarizes key disease-target associations from OpenTargets and literature:

| Target Gene Symbol | Disease Subtype (ESCC/EAC/Both) | Association Score | Key Role/Function | Therapeutic Relevance | Clinical Stage |
|---|---|---:|---|---|---|
| PDCD1 (PD-1) | Both; especially ESCC | 0.608 (carcinoma of esophagus); 0.607 (ESCC) | Immune checkpoint receptor on T cells; central mediator of T-cell exhaustion in the tumor microenvironment | Established biomarker/target for anti-PD-1 immunotherapy; anti-PD-1 plus platinum-based chemotherapy is standard first-line in advanced disease; adjuvant nivolumab improves DFS after neoadjuvant CRT and surgery | Approved (OpenTargets approval evidence; nivolumab/pembrolizumab clinical use) (OpenTargets Search: esophageal carcinoma, zhang2026esophagealcancerfrom pages 21-21, jazieh2024advancesinimmunotherapy pages 1-3) |
| TP53 | Both | 0.539 (carcinoma of esophagus); 0.422 (ESCC) | Master tumor suppressor controlling DNA-damage response, apoptosis, and genomic stability; most frequently altered driver in EC | Primarily prognostic/biologic rather than directly actionable; informs pathogenesis, progression, and resistance biology | Biomarker / investigational target (OpenTargets Search: esophageal carcinoma, zhang2026esophagealcancerfrom pages 6-7, zhang2026esophagealcancerfrom pages 2-3) |
| ADH1B | Mainly ESCC / susceptibility across carcinoma of esophagus | 0.530 (carcinoma of esophagus) | Alcohol metabolism enzyme; inherited variation modifies acetaldehyde exposure and alcohol-related carcinogenic risk | Risk stratification and prevention relevance rather than direct tumor targeting | Genetic susceptibility marker (OpenTargets Search: esophageal carcinoma, zhang2026esophagealcancerfrom pages 1-2) |
| NFE2L2 (NRF2) | Predominantly ESCC | 0.522 (carcinoma of esophagus) | Oxidative-stress transcriptional program; pathway activation supports survival, detoxification, and therapy resistance | Candidate target for resistant ESCC biology; pathway status may guide future precision strategies | Preclinical / investigational (OpenTargets Search: esophageal carcinoma, zhang2025thegenomiclandscape pages 4-7, zhang2026esophagealcancerfrom pages 6-7) |
| EGFR | Both; more emphasized in ESCC and subset of EAC | 0.512 (carcinoma of esophagus); 0.454 (ESCC) | Receptor tyrosine kinase driving proliferation, survival, and invasion | Overexpressed in a subset; cetuximab and EGFR-directed approaches studied, but clinical benefit has been inconsistent | Investigational / limited clinical utility (OpenTargets Search: esophageal carcinoma, rai2023biomarkersforearly pages 8-9) |
| FGFR1 | Predominantly ESCC / carcinoma of esophagus | 0.511 (carcinoma of esophagus) | RTK signaling contributor; copy-number gain/amplification in subsets | Potential actionable amplification in selected tumors; not standard of care | Investigational (OpenTargets Search: esophageal carcinoma) |
| ERBB2 (HER2) | Predominantly EAC | 0.503 (carcinoma of esophagus); 0.457 (EAC) | RTK amplified in a molecular subset of EAC; promotes oncogenic signaling and chromosomal-instability phenotype | Established predictive biomarker; trastuzumab-based therapy for HER2-positive disease; companion diagnostics required | Approved in HER2-positive adenocarcinoma (OpenTargets Search: esophageal carcinoma, rai2023biomarkersforearly pages 8-9, zhang2026esophagealcancerfrom pages 2-3) |
| MTOR | Both / carcinoma of esophagus | 0.499 (carcinoma of esophagus) | Central kinase in PI3K-AKT-mTOR signaling controlling growth, metabolism, and survival | Pathway is biologically important, but mTOR inhibitors are not standard therapy in EC | Investigational (OpenTargets Search: esophageal carcinoma, zhang2026esophagealcancerfrom pages 6-7) |
| CDKN2A | Both; especially Barrett's/EAC evolution and ESCC cell-cycle dysregulation | 0.696 (esophageal disorder) | Tumor suppressor controlling G1/S checkpoint; inactivation/loss is an early event in progression | Strong biomarker of progression biology; informs early carcinogenesis and possible prevention/risk models | Biomarker / investigational (OpenTargets Search: esophageal carcinoma, zhang2026esophagealcancerfrom pages 6-7, zhang2026esophagealcancerfrom pages 9-10) |
| PIK3CA | Both | 0.658 (esophageal disorder) | Catalytic PI3K subunit; activates PI3K-AKT signaling, promoting proliferation, survival, invasion, and metastasis | Actionable in principle; pathway inhibitors are relevant in basket/precision-oncology settings, but not routine EC standard | Investigational / precision-oncology candidate (OpenTargets Search: esophageal carcinoma, zhang2026esophagealcancerfrom pages 6-7) |
| NOTCH1 | Predominantly ESCC, but also implicated in EAC evolution | Not numerically listed in OpenTargets top rows here | Context-dependent driver in squamous epithelium; mutation/activation affects lineage fitness, angiogenesis, and tumor progression | Valuable biologic stratifier; no standard NOTCH-directed EC therapy | Investigational (zhang2026esophagealcancerfrom pages 6-7, zhang2026esophagealcancerfrom pages 8-9, zhang2025thegenomiclandscape pages 4-7) |
| SMAD4 | Predominantly EAC | 0.645 (esophageal disorder) | TGF-β pathway tumor suppressor; recurrently altered in EAC and linked to progression from Barrett's neoplasia | Biomarker of aggressive biology and progression; not yet a standard direct therapeutic target | Biomarker / investigational (OpenTargets Search: esophageal carcinoma, zhang2026esophagealcancerfrom pages 8-9, li2023molecularbiologyand pages 6-8) |
| CD274 (PD-L1) | Predominantly ESCC but relevant to both | 0.478 (ESCC) | Ligand for PD-1; key immune-evasion marker within inflamed tumors and myeloid-rich microenvironments | FDA-approved companion/selection biomarker for checkpoint blockade in some settings; expression associated with immunotherapy stratification | Approved companion biomarker / therapeutic axis (OpenTargets Search: esophageal carcinoma, rai2023biomarkersforearly pages 8-9, chen2025singlecellatlasof pages 5-6) |
| ARID1A | Mainly EAC / esophageal disorder | 0.622 (esophageal disorder) | Chromatin-remodeling tumor suppressor; contributes to epigenetic dysregulation and genomic instability | Emerging biomarker for molecular subclassification and synthetic-lethality concepts; not standard EC target | Investigational (OpenTargets Search: esophageal carcinoma, zhang2026esophagealcancerfrom pages 2-3) |


*Table: This table summarizes major disease-target associations for esophageal carcinoma by integrating OpenTargets association scores with recent literature on subtype biology and therapeutic relevance. It is useful for prioritizing biomarkers and targets across ESCC and EAC, including established immunotherapy and HER2-directed axes as well as investigational pathways.*

---

## 5. Environmental Information

### Environmental Factors
Environmental carcinogens include nitrosamines from dietary sources, air pollution, and occupational exposures. Chronic acid and bile reflux damage the esophageal epithelium, generating reactive oxygen species causing DNA double-strand breaks (maslenkina2023signalingpathwaysin pages 14-16). Nitrite exposure and high-fat diets are additional contributing factors (zhang2026esophagealcancerfrom pages 6-7).

### Lifestyle Factors
Tobacco smoking and alcohol consumption are the dominant modifiable risk factors for ESCC, causing ~90% of cases in the US and Western countries (jiang2023globaltrendsin pages 12-13). Obesity is a primary risk factor for EAC. Hot beverage consumption, poor oral hygiene, and sedentary lifestyle contribute to risk (liu2023epidemiologyofesophageal pages 8-9).

### Infectious Agents
- **HPV** (Human Papillomavirus): Circulating HPV DNA is associated with disease severity in some ESCC cohorts (rai2023biomarkersforearly pages 6-8).
- **EBV** (Epstein-Barr Virus): EBV status is under investigation as a biomarker for predicting immunotherapy response (fick2024immunotherapyforresectable pages 4-5).

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways
- **PI3K/AKT pathway:** Overactivation drives cell proliferation, survival, invasion, and metastasis (zhang2026esophagealcancerfrom pages 6-7).
- **Notch signaling:** NOTCH1 mutations provide competitive advantage in normal epithelium; overactivation in ESCC promotes angiogenesis through VEGF, ANGPT2, and CXCL1 upregulation (zhang2026esophagealcancerfrom pages 6-7, zhang2026esophagealcancerfrom pages 8-9). KEGG: hsa04330.
- **NRF2/KEAP1 pathway:** NRF2 pathway activation (42.9% mutation rate in ESCC cell lines) causes oxidative stress-related DNA damage in neighboring cells (zhang2025thegenomiclandscape pages 4-7, zhang2026esophagealcancerfrom pages 6-7). GO:0006979 (response to oxidative stress).
- **Hippo, RTK-Ras, and Wnt pathways** showed mutations across all ESCC cell lines analyzed (zhang2025thegenomiclandscape pages 4-7).
- **NF-κB signaling:** Activated by deoxycholic acid in Barrett's esophagus; **IL-6/STAT3 signaling** mediates apoptotic resistance (maslenkina2023signalingpathwaysin pages 14-16).
- **VEGF signaling:** Induces epithelial-to-mesenchymal transition (EMT) (maslenkina2023signalingpathwaysin pages 14-16).

### Cellular Processes
- **Apoptosis evasion:** TP53 loss impairs apoptotic signaling (GO:0006915).
- **Cell cycle dysregulation:** CDKN2A loss leads to loss of G1/S checkpoint and cell over-proliferation (GO:0007049) (zhang2026esophagealcancerfrom pages 6-7).
- **Epithelial-mesenchymal transition (EMT):** Key for invasion and metastasis (GO:0001837).
- **Angiogenesis:** NOTCH-mediated upregulation of VEGF and ANGPT2 (GO:0001525) (zhang2026esophagealcancerfrom pages 8-9).

### Immune System Involvement
The tumor microenvironment shifts from early immune surveillance dominated by CD8+ T cells and NK cells to later immunosuppressive conditions characterized by M2 tumor-associated macrophages, regulatory T cells, myeloid-derived suppressor cells (MDSCs), T-cell exhaustion, and cancer-associated fibroblast (CAF) formation (zhang2026esophagealcancerfrom pages 6-7). Single-cell RNA sequencing has identified CXCL13+CD8+ exhausted T cells as predictors of response to neoadjuvant immunochemotherapy (ji2024singlecellprofilingof pages 1-2). PD-L1+ tumor-associated macrophages correlate with clinical benefit from immunotherapy, and CD39-expressing tumor-infiltrating T cells are associated with improved survival and immunotherapy response (chen2025singlecellatlasof pages 5-6, chen2025singlecellatlasof pages 2-3). SPP1+ macrophages have been identified as key drivers of resistance to neoadjuvant chemoimmunotherapy (ji2024singlecellprofilingof pages 1-2).

### Advanced Technologies — Single-Cell and Spatial Transcriptomics
Mass cytometry analysis of over 10 million cells from 25 ESCC tumors revealed a compartmentalized immune landscape with reproducible paucity of CD4+ and CD8+ central memory T cells (TCM) in tumor sites (chen2025singlecellatlasof pages 2-3). Single-cell profiling identified 14 major cell subsets including cancer, immune, and stromal cells, with cancer cell differentiation status correlating with treatment response (ji2024singlecellprofilingof pages 1-2). Spatial transcriptomics revealed metastasis-related regions with surrounding vasculature, suggesting new blood vessel recruitment is essential for ESCC metastasis (guo2025singlecellrnasequencing pages 3-3). Two CAF subtypes were identified: extracellular matrix CAFs (eCAFs) and inflammatory CAFs (iCAFs) (yin2025singlecelltranscriptomicanalysis pages 1-2, yin2025singlecelltranscriptomicanalysis pages 14-15).

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary organ:** Esophagus (UBERON:0001043)
  - ESCC: Upper and middle esophagus
  - EAC: Lower/distal esophagus and gastroesophageal junction
- **Secondary involvement:** Lymph nodes (regional metastasis), liver, lung, kidney, adrenal gland (distant metastasis) (zhang2026esophagealcancerfrom pages 2-3)
- **Body systems:** Digestive system (UBERON:0001007)

### Tissue and Cell Level
- **ESCC:** Squamous epithelium (UBERON:0006914); squamous epithelial cells (CL:0000076)
- **EAC:** Columnar epithelium with intestinal metaplasia (Barrett's esophagus)
- **Cell types involved:** Epithelial cells, CD8+ T cells, CD4+ T cells, regulatory T cells (CL:0000815), NK cells, macrophages (CL:0000235), dendritic cells, CAFs, endothelial cells, pericytes, MDSCs (zhang2026esophagealcancerfrom pages 2-3, chen2025singlecellatlasof pages 2-3)

### Subcellular Level
- Nucleus (GO:0005634) — genomic instability and TP53 dysfunction
- Mitochondria — metabolic reprogramming
- Cell membrane — receptor tyrosine kinases (EGFR, HER2, FGFR)

---

## 8. Temporal Development

### Onset
- **Typical age:** Adult-onset, predominantly 50–70 years, with peak incidence in the 60–70 age group (ilic2024globalburdenof pages 4-6).
- **Onset pattern:** Insidious; early-stage disease is frequently asymptomatic.

### Progression
- **ESCC stages:** Normal epithelium → basal cell hyperplasia → low-grade intraepithelial neoplasia → high-grade intraepithelial neoplasia → invasive carcinoma (zhang2026esophagealcancerfrom pages 1-2).
- **EAC stages:** Normal → GERD → Barrett's esophagus → LGD → HGD → EAC (li2023molecularbiologyand pages 1-2).
- **Staging:** AJCC TNM staging system (8th edition) incorporating T (tumor depth), N (nodal status), M (metastasis), grade, and location.
- **Progression rate:** Variable; some Barrett's esophagus patients progress rapidly while others remain stable. TP53 mutations in BE progressors (46%) vs. nonprogressors (5%) serve as an early predictive marker (zhang2026esophagealcancerfrom pages 6-7).
- **Disease course:** Progressive without treatment; chronic, often fatal.

---

## 9. Inheritance and Population

### Epidemiology
The global epidemiological burden of esophageal cancer is summarized in the following table:

| Metric | Value | Year/Source |
|---|---:|---|
| Global new cases | 511,054 | 2022, GLOBOCAN (qi2024globalesophagealcancer pages 1-2) |
| Global deaths | 445,391 | 2022, GLOBOCAN (qi2024globalesophagealcancer pages 1-2) |
| Age-standardized incidence rate | 5.00 per 100,000 | 2022, GLOBOCAN (qi2024globalesophagealcancer pages 1-2) |
| Age-standardized mortality rate | 4.30 per 100,000 | 2022, GLOBOCAN (qi2024globalesophagealcancer pages 1-2) |
| Male-to-female ratio | Approximately 3:1 | 2019, GBD 2019; also male predominance across regions in 2022 GLOBOCAN (ilic2024globalburdenof pages 4-6, qi2024globalesophagealcancer pages 1-2) |
| 5-year survival rate | <20% | 2021, GBD 2021 / recent global reviews (zhang2025burdenofesophageal pages 1-2, sheikh2023currentstatusand pages 15-16) |
| China’s share of global cases | 43.8% | 2022, GLOBOCAN (qi2024globalesophagealcancer pages 1-2) |
| East Asia share of global cases | 53.2% | 2019, GBD 2019 (ilic2024globalburdenof pages 4-6, ilic2024globalburdenof pages 2-4) |
| Highest-risk regions | East Africa and East Asia: ASIR 7.60 per 100,000 | 2022, GLOBOCAN (qi2024globalesophagealcancer pages 1-2) |
| DALYs | 12,999,264 | 2021, GBD 2021 (zhang2025burdenofesophageal pages 1-2) |
| Projected cases by 2050 | +80.5% vs 2022 | 2050 projection from GLOBOCAN-based analysis (qi2024globalesophagealcancer pages 1-2) |
| Smoking attribution | 50.1% of DALYs in males | 2019, GBD 2019 (ilic2024globalburdenof pages 6-10) |
| Alcohol attribution | 29.6% of DALYs in males | 2019, GBD 2019 (ilic2024globalburdenof pages 6-10) |
| High BMI attribution | 18.8% of DALYs in males | 2019, GBD 2019 (ilic2024globalburdenof pages 6-10) |


*Table: This table summarizes the recent global epidemiological burden of esophageal cancer using GLOBOCAN 2022 and GBD 2019/2021 data. It highlights incidence, mortality, geographic concentration, sex disparity, survival, future projections, and major attributable risk factors.*

In 2019, there were 534,563 new cases globally (388,827 males, 145,736 females), with an age-standardized incidence rate of 6.5 per 100,000 (ilic2024globalburdenof pages 4-6). East Asia accounted for 53.2% of cases, with China representing 97.6% of those. The highest incidence rates (~17 per 100,000) occurred in Mongolia and Malawi (ilic2024globalburdenof pages 4-6). Age-standardized rates have been declining since 1990 (24.87% decrease in incidence by 2021), though absolute numbers continue to rise due to population growth and aging (zhang2025burdenofesophageal pages 1-2). By 2050, new cases are projected to increase by 80.5% and deaths by 85.4% compared to 2022 levels (qi2024globalesophagealcancer pages 1-2).

### Genetic Inheritance
EC is a complex, multifactorial disease with polygenic susceptibility. It does not follow a Mendelian inheritance pattern except in rare syndromes:
- **Tylosis** (Howel-Evans syndrome): Autosomal dominant; associated with RHBDF2 mutations; strongly predisposes to ESCC.
- GWAS have identified susceptibility loci including ADH1B, ALDH2, PLCE1, SLC39A6, and others (zhang2026esophagealcancerfrom pages 2-3, OpenTargets Search: esophageal carcinoma).

### Population Demographics
- **Sex ratio:** Males have approximately 3-fold higher incidence and mortality than females across all regions (zhang2026esophagealcancerfrom pages 2-3, ilic2024globalburdenof pages 4-6).
- **Geographic distribution:** ESCC is most prevalent in the "Asian esophageal cancer belt" (extending from northern Iran through Central Asia to northern China), and in East and Southern Africa. EAC is most common in Western Europe, North America, and Oceania (ilic2024globalburdenof pages 13-15, qi2024globalesophagealcancer pages 1-2).
- **Ethnic variation:** ESCC predominates in East Asian and Sub-Saharan African populations; EAC is more common in Caucasian populations (li2023molecularbiologyand pages 1-2).

---

## 10. Diagnostics

### Clinical Tests
- **Upper gastrointestinal endoscopy with biopsy** is the gold standard for diagnosis (sheikh2023currentstatusand pages 15-16). MAXO:0000130 (endoscopy).
- **Endoscopic ultrasound (EUS):** Standard technique for locoregional staging (sheikh2023currentstatusand pages 15-16).
- **Cross-sectional imaging:** CT, MRI, PET/CT for distant staging (rai2023biomarkersforearly pages 6-8).
- **Advanced endoscopy:** Chromoendoscopy, virtual chromoendoscopy, confocal laser endomicroscopy, volumetric laser endomicroscopy (rai2023biomarkersforearly pages 6-8).

### Biomarkers
- **HER2 (ERBB2):** Positive in 15–29% of EAC; FDA companion diagnostic for trastuzumab (rai2023biomarkersforearly pages 8-9).
- **PD-L1:** FDA-approved companion diagnostic for immunotherapy; present in ≤27% of EAC tumors (rai2023biomarkersforearly pages 8-9).
- **Microsatellite instability (MSI-H)/dMMR:** Enhanced sensitivity to immune checkpoint inhibitors (fick2024immunotherapyforresectable pages 7-7).
- **Tumor mutational burden (TMB):** FDA-approved companion diagnostic for pembrolizumab (rai2023biomarkersforearly pages 1-3).
- **Circulating tumor DNA (ctDNA):** Emerging prognostic biomarker detected via NGS (rai2023biomarkersforearly pages 6-8, fick2024immunotherapyforresectable pages 9-10).
- **DNA methylation markers:** Non-invasive approaches including blood cfDNA methylation and esophageal exfoliated cell-based DNA methylation analysis show promise for early detection (rai2023biomarkersforearly pages 6-8).
- **5-hydroxymethylcytosine (5hmC) signatures:** Combined with low-pass WGS, achieves AUC of 0.934 for ESCC detection with 82.4% sensitivity and 88.2% specificity.

### Screening
- **Endoscopy-based screening** in high-incidence regions (China, Japan) meets cost-effectiveness criteria and has demonstrated 43% reduction in SCC incidence and 45% reduction in mortality (liu2023epidemiologyofesophageal pages 6-7).
- **Cytosponge™:** Non-endoscopic swallowable device for Barrett's esophagus detection, combined with TFF3 biomarker immunohistochemistry (sheikh2023currentstatusand pages 15-16).
- **Liquid biopsy:** Blood, urine, and saliva-based non-invasive screening approaches under development (rai2023biomarkersforearly pages 1-3).

---

## 11. Outcome/Prognosis

### Survival and Mortality
- **5-year survival rate:** Less than 20% overall; as low as 15% in some populations (zhang2025burdenofesophageal pages 1-2, sheikh2023currentstatusand pages 15-16).
- **Early detection survival:** When detected early, endoscopic removal achieves 5-year survival rates up to 95% (zhang2026esophagealcancerfrom pages 2-3).
- **Advanced disease:** Metastatic disease treated with first-line chemotherapy achieves median survival of less than 1 year (jazieh2024advancesinimmunotherapy pages 1-3).
- **Mortality:** 445,391 deaths globally in 2022 with ASMR of 4.30 per 100,000; mortality-to-incidence ratio is high (qi2024globalesophagealcancer pages 1-2).

### Prognostic Factors
- Disease stage at diagnosis (most important)
- Histological subtype (ESCC vs. EAC)
- PD-L1 expression and MSI-H/dMMR status for immunotherapy response prediction
- Serum IL-6 levels: Higher levels predict worse prognosis and increased immune-related adverse events with immunotherapy
- CD39+ tumor-infiltrating T cells correlate with favorable prognosis (chen2025singlecellatlasof pages 2-3)
- CXCL13+CD8+ exhausted T cells predict improved response to neoadjuvant immunochemotherapy (ji2024singlecellprofilingof pages 1-2)

---

## 12. Treatment

### Pharmacotherapy

#### Chemotherapy
- **First-line regimens:** Fluorinated pyrimidine plus platinum agent (cisplatin or oxaliplatin) ± taxane (jazieh2024advancesinimmunotherapy pages 1-3).
- **Neoadjuvant regimens:** CROSS regimen (carboplatin/paclitaxel + radiotherapy); FLOT regimen (5-FU/leucovorin/oxaliplatin/docetaxel) for perioperative EAC treatment (li2023molecularbiologyand pages 1-2, fick2024immunotherapyforresectable pages 7-7).

#### Immunotherapy
- **Pembrolizumab (anti-PD-1):** FDA-approved (March 2021, KEYNOTE-590 trial) for first-line advanced EC combined with chemotherapy (rai2023biomarkersforearly pages 8-9, jazieh2024advancesinimmunotherapy pages 1-3). MAXO:0001287 (immune checkpoint inhibitor therapy).
- **Nivolumab (anti-PD-1):** FDA-approved for adjuvant use after neoadjuvant chemoradiotherapy and surgery in patients with residual disease (CheckMate 577); improved median DFS 22.4 vs. 11.0 months, particularly in ESCC (29.7 vs. 11.0 months) (fick2024immunotherapyforresectable pages 7-7, zhang2026esophagealcancerfrom pages 21-21).
- Anti-PD-1 plus platinum-based chemotherapy has replaced chemotherapy alone as the standard first-line treatment for most advanced EC patients (zhang2026esophagealcancerfrom pages 21-21).
- Pathologic complete response rates with ICI plus chemoradiotherapy reach up to 60% in early-phase trials, with highest rates in ESCC and dMMR tumors (fick2024immunotherapyforresectable pages 1-2).

#### Targeted Therapy
- **Trastuzumab:** HER2-directed therapy for HER2-positive EAC (15–29% of cases); FDA companion diagnostic required (rai2023biomarkersforearly pages 8-9). MAXO:0001298 (HER2 targeted therapy).
- **CLDN18.2-targeting therapies:** Zolbetuximab (anti-CLDN18.2 antibody) and AZD6422 (armored CAR-T targeting CLDN18.2) are in clinical development for CLDN18.2+ esophagogastric cancers.
- **EGFR inhibitors:** Cetuximab studied but has not significantly improved OS in meta-analyses despite EGFR overexpression in 20–50% of EAC tumors (rai2023biomarkersforearly pages 8-9).

### Surgical Interventions
- **Esophagectomy:** Radical resection remains a cornerstone for resectable disease, typically after neoadjuvant therapy. R0 resection rates with neoadjuvant immunotherapy approaches are high (up to 98%) (fick2024immunotherapyforresectable pages 4-5). MAXO:0000004 (surgical procedure).
- **Endoscopic treatments:** EMR (endoscopic mucosal resection) and ESD (endoscopic submucosal dissection) for early-stage disease without lymph node involvement (sheikh2023currentstatusand pages 15-16). MAXO:0000130 (endoscopy).

### Experimental Treatments
- **Neoadjuvant chemo-immunotherapy:** Phase III trials investigating perioperative ICI combinations ongoing (fick2024immunotherapyforresectable pages 1-2, fick2024immunotherapyforresectable pages 5-7).
- **CAR-T therapy:** Mesothelin-targeted (M28z1XXPD1DNR) CAR-T for peritoneal carcinomatosis (NCT06623396); CLDN18.2-targeting CAR-T (AZD6422) in clinical development.
- **Personalized neoantigen vaccines:** NCT05307835 investigating tumor-specific antigen vaccination (fick2024immunotherapyforresectable pages 9-10).
- **Anti-TIGIT combinations:** Multiple clinical trials combining TIGIT blockade with anti-PD-1 for esophagogastric cancers.

### Treatment Outcomes
- Neoadjuvant chemoradiotherapy with immunotherapy: pooled pCR rates of 31.4%, MPR rates of 48.9% (fick2024immunotherapyforresectable pages 5-7).
- Immunotherapy addition to chemoradiotherapy associated with higher pCR (29% vs. 21%), improved nodal downstaging (50% vs. 40%), and longer median OS (69.1 vs. 56.3 months) (fick2024immunotherapyforresectable pages 5-7).
- ICI response rates remain ≤30% overall, with immune-related adverse events in 17% of cases (Grade 3+) (rai2023biomarkersforearly pages 8-9).

---

## 13. Prevention

### Primary Prevention
- **Tobacco cessation** and **alcohol reduction** are the most impactful strategies, as smoking and alcohol account for ~90% of ESCC in Western countries (jiang2023globaltrendsin pages 12-13).
- **Dietary modification:** Increased intake of fresh fruits and vegetables; avoidance of moldy foods and nitrosamine-containing foods (qi2024globalesophagealcancer pages 1-2).
- **Weight management:** Reducing obesity to lower EAC risk (high BMI accounts for 18.8–19.3% of DALYs) (ilic2024globalburdenof pages 6-10).
- **GERD management:** Proton pump inhibitors and lifestyle modifications to prevent Barrett's esophagus progression (sheikh2023currentstatusand pages 15-16).

### Secondary Prevention (Screening and Early Detection)
- **Endoscopic screening** in high-incidence populations has demonstrated significant mortality reduction (45% in community-based Chinese studies) (liu2023epidemiologyofesophageal pages 6-7).
- **Cytosponge™** combined with biomarker assays for non-endoscopic Barrett's screening (sheikh2023currentstatusand pages 15-16).
- **Risk stratification** using genetic markers, clinical factors, and molecular biomarkers for targeted screening.
- Endoscopy-based early diagnosis in China and Japan has advanced endoscopic methods as definitive treatments with remarkable efficacy (zhang2026esophagealcancerfrom pages 1-2).

### Chemoprevention
- Aspirin and proton pump inhibitors have shown promising results in chemoprevention of EAC from Barrett's esophagus (sheikh2023currentstatusand pages 15-16).

---

## 14. Other Species / Natural Disease

Esophageal cancer naturally occurs in various animal species, though it is less extensively documented than in humans. The condition has been observed in:
- **Dogs (Canis lupus familiaris):** Esophageal carcinoma, though rare, has been documented; spirocercosis (*Spirocerca lupi*) infection is a known risk factor for esophageal sarcoma in dogs.
- **Cattle (Bos taurus):** Esophageal papillomas and carcinomas associated with bovine papillomavirus and bracken fern consumption.

---

## 15. Model Organisms

### Cell Lines
Extensively used ESCC cell lines include the **KYSE series** (KYSE-30, KYSE-150, KYSE-180, KYSE-450, KYSE-510), **TE-1**, **ECA-109**, and **KYSE-770**, with the normal epithelial line **Het-1a** as control. Whole exome and RNA sequencing have characterized their genomic landscape, revealing TMB ranging from 48.7 to 70.4 mut/MB, with mutations in Hippo, Notch, PI3K, RTK-Ras, and Wnt pathways across all cancer cell lines (zhang2025thegenomiclandscape pages 4-7). Human esophageal squamous cell lines KYSE140, KYSE150, KYSE450, KYSE510, KYSE30, KYSE70, and KYSE410 are widely used (liu2023spatialtranscriptomicsanalysis pages 16-17).

### Mouse Models
- **4-NQO (4-nitroquinoline-1-oxide)-induced spontaneous ESCC mouse model:** Chemical carcinogen administered in drinking water to induce ESCC, recapitulating the multistep carcinogenesis process. This model has been used to validate therapeutic targets including CCL18 blockade.
- **Xenograft models:** CB17 SCID immunodeficient mice used for subcutaneous and orthotopic tumor growth studies (liu2023spatialtranscriptomicsanalysis pages 16-17).
- **Patient-derived xenograft (PDX) models:** Preserve patient tumor features and are used for drug efficacy testing and personalized medicine approaches.

### Organoid Models
Patient-derived organoids (PDOs) maintain in Matrigel culture for 10–14 days and can be genetically modified via lentivirus-mediated transduction. PDOs have been used for coculture experiments to test T cell cytotoxicity (liu2023spatialtranscriptomicsanalysis pages 16-17, chen2025singlecellatlasof pages 3-5). Organoid models are increasingly used in the research and development of antitumor drugs and personalized medicine.

### Model Limitations
Cell line-derived xenograft models lack patient tumor heterogeneity and immune microenvironment characteristics. PDX and organoid models better preserve patient features but remain limited in recapitulating the full immune microenvironment, particularly the adaptive immune response.

---

## Summary

Esophageal carcinoma remains one of the most lethal and challenging cancers globally, with high mortality rates and poor overall prognosis. The two major subtypes, ESCC and EAC, exhibit distinct epidemiological patterns, risk factor profiles, molecular landscapes, and geographic distributions. Recent advances in single-cell and spatial transcriptomics have revealed unprecedented detail about the tumor microenvironment, identifying cell-type-specific mechanisms of immune evasion and treatment resistance. The integration of immune checkpoint inhibitors, particularly anti-PD-1 antibodies, into treatment paradigms has significantly improved outcomes for both subtypes, with adjuvant nivolumab and first-line pembrolizumab plus chemotherapy now established as standard-of-care options. Emerging therapeutic modalities including CAR-T cell therapy, personalized neoantigen vaccines, and novel checkpoint combinations hold promise for further improvements. Primary prevention through tobacco cessation, alcohol reduction, and dietary modification remains the most effective strategy for reducing the global burden of this disease, while advances in non-invasive screening technologies and liquid biopsy approaches may enable earlier detection and improved survival outcomes in the future.

References

1. (qi2024globalesophagealcancer pages 1-2): Ling Qi, Mengfei Sun, Weixin Liu, Xuefeng Zhang, Yongjun Yu, Ziqiang Tian, Zhiyu Ni, Rongshou Zheng, and Yong Li. Global esophageal cancer epidemiology in 2022 and predictions for 2050: a comprehensive analysis and projections based on globocan data. Chinese Medical Journal, 137:3108-3116, Dec 2024. URL: https://doi.org/10.1097/cm9.0000000000003420, doi:10.1097/cm9.0000000000003420. This article has 75 citations and is from a peer-reviewed journal.

2. (zhang2026esophagealcancerfrom pages 1-2): Shaosen Zhang, Yanrong Shen, Lingxuan Zhu, Yancheng Lai, Liang Zhu, Xinyi Xiao, Jiacheng Li, Wen Tan, Dongxin Lin, and Chen Wu. Esophageal cancer: from pathogenesis to precision therapies. Signal Transduction and Targeted Therapy, Apr 2026. URL: https://doi.org/10.1038/s41392-026-02614-7, doi:10.1038/s41392-026-02614-7. This article has 1 citations and is from a peer-reviewed journal.

3. (sheikh2023currentstatusand pages 15-16): Mahdi Sheikh, Gholamreza Roshandel, Valerie McCormack, and Reza Malekzadeh. Current status and future prospects for esophageal cancer. Cancers, 15:765, Jan 2023. URL: https://doi.org/10.3390/cancers15030765, doi:10.3390/cancers15030765. This article has 294 citations.

4. (OpenTargets Search: esophageal carcinoma): Open Targets Query (esophageal carcinoma, 40 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (li2023molecularbiologyand pages 1-2): Shulin Li, Sanne Johanna Maria Hoefnagel, and Kausilia Krishnawatie Krishnadath. Molecular biology and clinical management of esophageal adenocarcinoma. Cancers, 15:5410, Nov 2023. URL: https://doi.org/10.3390/cancers15225410, doi:10.3390/cancers15225410. This article has 24 citations.

6. (zhang2026esophagealcancerfrom pages 6-7): Shaosen Zhang, Yanrong Shen, Lingxuan Zhu, Yancheng Lai, Liang Zhu, Xinyi Xiao, Jiacheng Li, Wen Tan, Dongxin Lin, and Chen Wu. Esophageal cancer: from pathogenesis to precision therapies. Signal Transduction and Targeted Therapy, Apr 2026. URL: https://doi.org/10.1038/s41392-026-02614-7, doi:10.1038/s41392-026-02614-7. This article has 1 citations and is from a peer-reviewed journal.

7. (zhang2026esophagealcancerfrom pages 9-10): Shaosen Zhang, Yanrong Shen, Lingxuan Zhu, Yancheng Lai, Liang Zhu, Xinyi Xiao, Jiacheng Li, Wen Tan, Dongxin Lin, and Chen Wu. Esophageal cancer: from pathogenesis to precision therapies. Signal Transduction and Targeted Therapy, Apr 2026. URL: https://doi.org/10.1038/s41392-026-02614-7, doi:10.1038/s41392-026-02614-7. This article has 1 citations and is from a peer-reviewed journal.

8. (zhang2026esophagealcancerfrom pages 2-3): Shaosen Zhang, Yanrong Shen, Lingxuan Zhu, Yancheng Lai, Liang Zhu, Xinyi Xiao, Jiacheng Li, Wen Tan, Dongxin Lin, and Chen Wu. Esophageal cancer: from pathogenesis to precision therapies. Signal Transduction and Targeted Therapy, Apr 2026. URL: https://doi.org/10.1038/s41392-026-02614-7, doi:10.1038/s41392-026-02614-7. This article has 1 citations and is from a peer-reviewed journal.

9. (li2023molecularbiologyand pages 6-8): Shulin Li, Sanne Johanna Maria Hoefnagel, and Kausilia Krishnawatie Krishnadath. Molecular biology and clinical management of esophageal adenocarcinoma. Cancers, 15:5410, Nov 2023. URL: https://doi.org/10.3390/cancers15225410, doi:10.3390/cancers15225410. This article has 24 citations.

10. (liu2023epidemiologyofesophageal pages 8-9): Chun‐Quan Liu, Yun‐Lei Ma, Qi Qin, Pei‐Hao Wang, Yi Luo, Peng‐Fei Xu, and Yong Cui. Epidemiology of esophageal cancer in 2020 and projections to 2030 and 2040. Thoracic Cancer, 14:3-11, Dec 2023. URL: https://doi.org/10.1111/1759-7714.14745, doi:10.1111/1759-7714.14745. This article has 457 citations.

11. (ilic2024globalburdenof pages 6-10): Irena Ilic, Ivana Zivanovic Macuzic, Ana Ravic-Nikolic, Milena Ilic, and Vesna Milicic. Global burden of esophageal cancer and its risk factors: a systematic analysis of the global burden of disease study 2019. Life, 15:24, Dec 2024. URL: https://doi.org/10.3390/life15010024, doi:10.3390/life15010024. This article has 15 citations.

12. (ilic2024globalburdenof pages 4-6): Irena Ilic, Ivana Zivanovic Macuzic, Ana Ravic-Nikolic, Milena Ilic, and Vesna Milicic. Global burden of esophageal cancer and its risk factors: a systematic analysis of the global burden of disease study 2019. Life, 15:24, Dec 2024. URL: https://doi.org/10.3390/life15010024, doi:10.3390/life15010024. This article has 15 citations.

13. (fick2024immunotherapyforresectable pages 9-10): Cameron N. Fick, Elizabeth G. Dunne, Smita Sihag, Daniela Molena, Samuel L. Cytryn, Yelena Y. Janjigian, Abraham J. Wu, Stephanie G. Worrell, Wayne L. Hofstetter, David R. Jones, and Katherine D. Gray. Immunotherapy for resectable locally advanced esophageal carcinoma. The Annals of Thoracic Surgery, 118:130-140, Jul 2024. URL: https://doi.org/10.1016/j.athoracsur.2024.02.021, doi:10.1016/j.athoracsur.2024.02.021. This article has 18 citations.

14. (rai2023biomarkersforearly pages 8-9): Vikrant Rai, Joe Abdo, and Devendra K. Agrawal. Biomarkers for early detection, prognosis, and therapeutics of esophageal cancers. International Journal of Molecular Sciences, 24:3316, Feb 2023. URL: https://doi.org/10.3390/ijms24043316, doi:10.3390/ijms24043316. This article has 73 citations.

15. (zhang2025thegenomiclandscape pages 4-7): Chao Zhang, Chenghao Li, Jian Zhong Su, Kuaile Zhao, Longlong Shao, and Jiaying Deng. The genomic landscape of esophageal squamous cell carcinoma cell lines. Cancer Cell International, May 2025. URL: https://doi.org/10.1186/s12935-025-03686-1, doi:10.1186/s12935-025-03686-1. This article has 7 citations and is from a peer-reviewed journal.

16. (zhang2026esophagealcancerfrom pages 8-9): Shaosen Zhang, Yanrong Shen, Lingxuan Zhu, Yancheng Lai, Liang Zhu, Xinyi Xiao, Jiacheng Li, Wen Tan, Dongxin Lin, and Chen Wu. Esophageal cancer: from pathogenesis to precision therapies. Signal Transduction and Targeted Therapy, Apr 2026. URL: https://doi.org/10.1038/s41392-026-02614-7, doi:10.1038/s41392-026-02614-7. This article has 1 citations and is from a peer-reviewed journal.

17. (li2023molecularbiologyand pages 16-17): Shulin Li, Sanne Johanna Maria Hoefnagel, and Kausilia Krishnawatie Krishnadath. Molecular biology and clinical management of esophageal adenocarcinoma. Cancers, 15:5410, Nov 2023. URL: https://doi.org/10.3390/cancers15225410, doi:10.3390/cancers15225410. This article has 24 citations.

18. (zhang2026esophagealcancerfrom pages 30-31): Shaosen Zhang, Yanrong Shen, Lingxuan Zhu, Yancheng Lai, Liang Zhu, Xinyi Xiao, Jiacheng Li, Wen Tan, Dongxin Lin, and Chen Wu. Esophageal cancer: from pathogenesis to precision therapies. Signal Transduction and Targeted Therapy, Apr 2026. URL: https://doi.org/10.1038/s41392-026-02614-7, doi:10.1038/s41392-026-02614-7. This article has 1 citations and is from a peer-reviewed journal.

19. (zhang2026esophagealcancerfrom pages 21-21): Shaosen Zhang, Yanrong Shen, Lingxuan Zhu, Yancheng Lai, Liang Zhu, Xinyi Xiao, Jiacheng Li, Wen Tan, Dongxin Lin, and Chen Wu. Esophageal cancer: from pathogenesis to precision therapies. Signal Transduction and Targeted Therapy, Apr 2026. URL: https://doi.org/10.1038/s41392-026-02614-7, doi:10.1038/s41392-026-02614-7. This article has 1 citations and is from a peer-reviewed journal.

20. (jazieh2024advancesinimmunotherapy pages 1-3): Khalid Jazieh, Harry H Yoon, and Mojun Zhu. Advances in immunotherapy in esophagogastric cancer. Jun 2024. URL: https://doi.org/10.1016/j.hoc.2024.02.002, doi:10.1016/j.hoc.2024.02.002. This article has 1 citations.

21. (chen2025singlecellatlasof pages 5-6): Xiankai Chen, Yahui Zhao, Yuhao Wang, Xiliang Wang, Yuhao Liu, Zhihua Liu, and Yin Li. Single-cell atlas of the esophageal squamous cell carcinoma immune ecosystem to predict immunotherapy response. Signal Transduction and Targeted Therapy, Oct 2025. URL: https://doi.org/10.1038/s41392-025-02446-x, doi:10.1038/s41392-025-02446-x. This article has 8 citations and is from a peer-reviewed journal.

22. (maslenkina2023signalingpathwaysin pages 14-16): Ksenia Maslenkina, Liudmila Mikhaleva, Maxim Naumenko, Rositsa Vandysheva, Michail Gushchin, Dmitri Atiakshin, Igor Buchwalow, and Markus Tiemann. Signaling pathways in the pathogenesis of barrett’s esophagus and esophageal adenocarcinoma. International Journal of Molecular Sciences, May 2023. URL: https://doi.org/10.3390/ijms24119304, doi:10.3390/ijms24119304. This article has 26 citations.

23. (jiang2023globaltrendsin pages 12-13): Yu Jiang, Yuechun Lin, Yaokai Wen, Wenhai Fu, Rui Wang, Jiaxi He, Jianrong Zhang, Zhufeng Wang, Fan Ge, Zhenyu Huo, Runchen Wang, Haoxin Peng, Xiangrong Wu, Jianxing He, and Shuben Li. Global trends in the burden of esophageal cancer, 1990−2019: results from the global burden of disease study 2019. Journal of Thoracic Disease, 15:348-364, Feb 2023. URL: https://doi.org/10.21037/jtd-22-856, doi:10.21037/jtd-22-856. This article has 43 citations and is from a peer-reviewed journal.

24. (rai2023biomarkersforearly pages 6-8): Vikrant Rai, Joe Abdo, and Devendra K. Agrawal. Biomarkers for early detection, prognosis, and therapeutics of esophageal cancers. International Journal of Molecular Sciences, 24:3316, Feb 2023. URL: https://doi.org/10.3390/ijms24043316, doi:10.3390/ijms24043316. This article has 73 citations.

25. (fick2024immunotherapyforresectable pages 4-5): Cameron N. Fick, Elizabeth G. Dunne, Smita Sihag, Daniela Molena, Samuel L. Cytryn, Yelena Y. Janjigian, Abraham J. Wu, Stephanie G. Worrell, Wayne L. Hofstetter, David R. Jones, and Katherine D. Gray. Immunotherapy for resectable locally advanced esophageal carcinoma. The Annals of Thoracic Surgery, 118:130-140, Jul 2024. URL: https://doi.org/10.1016/j.athoracsur.2024.02.021, doi:10.1016/j.athoracsur.2024.02.021. This article has 18 citations.

26. (ji2024singlecellprofilingof pages 1-2): Gang Ji, Qi Yang, Song Wang, Xiaolong Yan, Qiuxiang Ou, Li Gong, Jinbo Zhao, Yongan Zhou, Feng Tian, Jie Lei, Xiaorong Mu, Jian Wang, Tao Wang, Xiaoping Wang, Jianyong Sun, Jipeng Zhang, Chenghui Jia, Tao Jiang, Ming-gao Zhao, and Qiang Lu. Single-cell profiling of response to neoadjuvant chemo-immunotherapy in surgically resectable esophageal squamous cell carcinoma. Genome Medicine, Apr 2024. URL: https://doi.org/10.1186/s13073-024-01320-9, doi:10.1186/s13073-024-01320-9. This article has 52 citations and is from a highest quality peer-reviewed journal.

27. (chen2025singlecellatlasof pages 2-3): Xiankai Chen, Yahui Zhao, Yuhao Wang, Xiliang Wang, Yuhao Liu, Zhihua Liu, and Yin Li. Single-cell atlas of the esophageal squamous cell carcinoma immune ecosystem to predict immunotherapy response. Signal Transduction and Targeted Therapy, Oct 2025. URL: https://doi.org/10.1038/s41392-025-02446-x, doi:10.1038/s41392-025-02446-x. This article has 8 citations and is from a peer-reviewed journal.

28. (guo2025singlecellrnasequencing pages 3-3): Wei Guo, Bolun Zhou, Lizhou Dou, Lei Guo, Yong Li, Jianjun Qin, Zhen Wang, Qilin Huai, Xuemin Xue, Yin Li, Jianming Ying, Qi Xue, Shugeng Gao, and Jie He. Single-cell rna sequencing and spatial transcriptomics of esophageal squamous cell carcinoma with lymph node metastases. Experimental & Molecular Medicine, 57:59-71, Jan 2025. URL: https://doi.org/10.1038/s12276-024-01369-x, doi:10.1038/s12276-024-01369-x. This article has 15 citations and is from a peer-reviewed journal.

29. (yin2025singlecelltranscriptomicanalysis pages 1-2): Xiaolei Yin, Xiaopeng Li, Lili Mi, Jiaojiao Hou, and Fei Yin. Single-cell transcriptomic analysis reveals epithelial and microenvironmental heterogeneity in small cell carcinoma of the esophagus. Frontiers in Immunology, Oct 2025. URL: https://doi.org/10.3389/fimmu.2025.1672587, doi:10.3389/fimmu.2025.1672587. This article has 1 citations and is from a peer-reviewed journal.

30. (yin2025singlecelltranscriptomicanalysis pages 14-15): Xiaolei Yin, Xiaopeng Li, Lili Mi, Jiaojiao Hou, and Fei Yin. Single-cell transcriptomic analysis reveals epithelial and microenvironmental heterogeneity in small cell carcinoma of the esophagus. Frontiers in Immunology, Oct 2025. URL: https://doi.org/10.3389/fimmu.2025.1672587, doi:10.3389/fimmu.2025.1672587. This article has 1 citations and is from a peer-reviewed journal.

31. (zhang2025burdenofesophageal pages 1-2): Chengcheng Zhang, Linzhi Chen, Yuqi Xiu, Hongling Zhang, Yuejuan Zhang, and Wenjuan Ying. Burden of esophageal cancer in global, regional and national regions from 1990 to 2021 and its projection until 2050: results from the gbd study 2021. Frontiers in Oncology, Jan 2025. URL: https://doi.org/10.3389/fonc.2024.1518567, doi:10.3389/fonc.2024.1518567. This article has 17 citations.

32. (ilic2024globalburdenof pages 2-4): Irena Ilic, Ivana Zivanovic Macuzic, Ana Ravic-Nikolic, Milena Ilic, and Vesna Milicic. Global burden of esophageal cancer and its risk factors: a systematic analysis of the global burden of disease study 2019. Life, 15:24, Dec 2024. URL: https://doi.org/10.3390/life15010024, doi:10.3390/life15010024. This article has 15 citations.

33. (ilic2024globalburdenof pages 13-15): Irena Ilic, Ivana Zivanovic Macuzic, Ana Ravic-Nikolic, Milena Ilic, and Vesna Milicic. Global burden of esophageal cancer and its risk factors: a systematic analysis of the global burden of disease study 2019. Life, 15:24, Dec 2024. URL: https://doi.org/10.3390/life15010024, doi:10.3390/life15010024. This article has 15 citations.

34. (fick2024immunotherapyforresectable pages 7-7): Cameron N. Fick, Elizabeth G. Dunne, Smita Sihag, Daniela Molena, Samuel L. Cytryn, Yelena Y. Janjigian, Abraham J. Wu, Stephanie G. Worrell, Wayne L. Hofstetter, David R. Jones, and Katherine D. Gray. Immunotherapy for resectable locally advanced esophageal carcinoma. The Annals of Thoracic Surgery, 118:130-140, Jul 2024. URL: https://doi.org/10.1016/j.athoracsur.2024.02.021, doi:10.1016/j.athoracsur.2024.02.021. This article has 18 citations.

35. (rai2023biomarkersforearly pages 1-3): Vikrant Rai, Joe Abdo, and Devendra K. Agrawal. Biomarkers for early detection, prognosis, and therapeutics of esophageal cancers. International Journal of Molecular Sciences, 24:3316, Feb 2023. URL: https://doi.org/10.3390/ijms24043316, doi:10.3390/ijms24043316. This article has 73 citations.

36. (liu2023epidemiologyofesophageal pages 6-7): Chun‐Quan Liu, Yun‐Lei Ma, Qi Qin, Pei‐Hao Wang, Yi Luo, Peng‐Fei Xu, and Yong Cui. Epidemiology of esophageal cancer in 2020 and projections to 2030 and 2040. Thoracic Cancer, 14:3-11, Dec 2023. URL: https://doi.org/10.1111/1759-7714.14745, doi:10.1111/1759-7714.14745. This article has 457 citations.

37. (fick2024immunotherapyforresectable pages 1-2): Cameron N. Fick, Elizabeth G. Dunne, Smita Sihag, Daniela Molena, Samuel L. Cytryn, Yelena Y. Janjigian, Abraham J. Wu, Stephanie G. Worrell, Wayne L. Hofstetter, David R. Jones, and Katherine D. Gray. Immunotherapy for resectable locally advanced esophageal carcinoma. The Annals of Thoracic Surgery, 118:130-140, Jul 2024. URL: https://doi.org/10.1016/j.athoracsur.2024.02.021, doi:10.1016/j.athoracsur.2024.02.021. This article has 18 citations.

38. (fick2024immunotherapyforresectable pages 5-7): Cameron N. Fick, Elizabeth G. Dunne, Smita Sihag, Daniela Molena, Samuel L. Cytryn, Yelena Y. Janjigian, Abraham J. Wu, Stephanie G. Worrell, Wayne L. Hofstetter, David R. Jones, and Katherine D. Gray. Immunotherapy for resectable locally advanced esophageal carcinoma. The Annals of Thoracic Surgery, 118:130-140, Jul 2024. URL: https://doi.org/10.1016/j.athoracsur.2024.02.021, doi:10.1016/j.athoracsur.2024.02.021. This article has 18 citations.

39. (liu2023spatialtranscriptomicsanalysis pages 16-17): Xuejiao Liu, Simin Zhao, Keke Wang, Liting Zhou, Ming Jiang, Yunfeng Gao, Ran Yang, Shiwen Yan, Wen Zhang, Bingbing Lu, Feifei Liu, Ran Zhao, Wenting Liu, Zihan Zhang, Kangdong Liu, Xiang Li, and Zigang Dong. Spatial transcriptomics analysis of esophageal squamous precancerous lesions and their progression to esophageal cancer. Nature Communications, Aug 2023. URL: https://doi.org/10.1038/s41467-023-40343-5, doi:10.1038/s41467-023-40343-5. This article has 62 citations and is from a highest quality peer-reviewed journal.

40. (chen2025singlecellatlasof pages 3-5): Xiankai Chen, Yahui Zhao, Yuhao Wang, Xiliang Wang, Yuhao Liu, Zhihua Liu, and Yin Li. Single-cell atlas of the esophageal squamous cell carcinoma immune ecosystem to predict immunotherapy response. Signal Transduction and Targeted Therapy, Oct 2025. URL: https://doi.org/10.1038/s41392-025-02446-x, doi:10.1038/s41392-025-02446-x. This article has 8 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Esophageal_Carcinoma-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Esophageal_Carcinoma-deep-research-falcon_artifacts/artifact-01.md)