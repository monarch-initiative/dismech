---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-19T11:45:54.659338'
end_time: '2026-06-19T12:03:57.404053'
duration_seconds: 1082.74
template_file: templates\disease_pathophysiology_research.md
template_variables:
  disease_name: Autoimmune Retinopathy
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 15
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: Autoimmune_Retinopathy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Autoimmune_Retinopathy-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: Autoimmune_Retinopathy-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autoimmune Retinopathy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Autoimmune Retinopathy** covering all of the
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
- **Disease Name:** Autoimmune Retinopathy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Autoimmune Retinopathy** covering all of the
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


# Comprehensive Research Report: Autoimmune Retinopathy

## 1. Disease Information

### Overview
Autoimmune retinopathy (AIR) refers to a cluster of rare autoimmune disorders that lead to progressive retinal degeneration characterized by rapid and progressive deterioration of vision linked to the presence of circulating anti-retinal autoantibodies (ARAs) (kalogeropoulos2025diagnosisandtreatment pages 1-2). "AIR comprises a group of rare autoimmune disorders causing retinal degeneration, characterized by rapid vision deterioration linked to circulating anti-retinal autoantibodies (ARAs)" (kalogeropoulos2025diagnosisandtreatment pages 1-2). The disease accounts for less than 1% of all cases managed at tertiary referral centers (kalogeropoulos2025diagnosisandtreatment pages 2-4).

### Classification and Synonyms
AIR can be categorized into paraneoplastic (pAIR) and non-paraneoplastic (npAIR) forms (kalogeropoulos2025diagnosisandtreatment pages 1-2). The paraneoplastic category comprises:
- **Cancer-associated retinopathy (CAR)**: Associated with non-melanoma malignancies
- **Melanoma-associated retinopathy (MAR)**: Specifically associated with melanoma

The non-paraneoplastic form (npAIR) occurs in the absence of malignancy and is diagnosed by ruling out other possible etiologies (kalogeropoulos2025diagnosisandtreatment pages 1-2, kalogeropoulos2025diagnosisandtreatment pages 2-4).

**Alternative names**: Paraneoplastic retinopathy, autoimmune retinitis

### Key Identifiers
Currently no OMIM, Orphanet, or MONDO IDs were identified in the available literature. The disease lacks standardized international diagnostic codes, which contributes to challenges in epidemiological tracking (kalogeropoulos2025diagnosisandtreatment pages 20-22).

### Historical Perspective
The first case of CAR was reported in 1976 by Sawyer et al. in three females with bronchial carcinoma who developed vision loss due to photoreceptor degeneration (kalogeropoulos2025diagnosisandtreatment pages 2-4). In 1987, Thirkill et al. discovered a 23-kDa retinal antigen (later identified as recoverin) targeted by antibodies in CAR patients (kalogeropoulos2025diagnosisandtreatment pages 2-4). The term "paraneoplastic retinopathy" was introduced by Klingele et al. in 1984, and the first case of MAR was described by Gass in 1984 (kalogeropoulos2025diagnosisandtreatment pages 1-2, kalogeropoulos2025diagnosisandtreatment pages 2-4). The first cases of AIR without underlying neoplasia (npAIR) were recorded in 1997 (kalogeropoulos2025diagnosisandtreatment pages 2-4).

### Data Sources
Information is derived from disease-level resources including case series, retrospective studies, and comprehensive literature reviews published between 2020-2025 (kalogeropoulos2025diagnosisandtreatment pages 1-2, beuzit2025paraneoplasticocularsyndromes pages 1-2, chen2025autoimmuneretinopathyin pages 1-2, kalogeropoulos2025diagnosisandtreatment pages 2-4).

## 2. Etiology

### Disease Causal Factors

**Primary Mechanisms**:
1. **Autoimmune/Immunological**: The core mechanism involves the production of antiretinal autoantibodies (ARAs) that target specific retinal proteins, leading to retinal cell death through various pathways including apoptosis and inflammation (kalogeropoulos2025diagnosisandtreatment pages 2-4, kalogeropoulos2025diagnosisandtreatment pages 4-5).

2. **Paraneoplastic (for CAR/MAR)**: Malignant and benign cancers elicit an immune response where tumoral antigens exposed to antigen-presenting cells induce the production of ARAs against epitopes that cross-react with retinal proteins through molecular mimicry (kalogeropoulos2025diagnosisandtreatment pages 4-5).

3. **Molecular Mimicry**: Similarity between proteins present in pathogens and the retina can lead to autoantibody production. An example occurs in the glycolytic pathway, which plays crucial metabolic roles in both microbial and retinal cells (kalogeropoulos2025diagnosisandtreatment pages 4-5).

4. **Retinal Injury-Induced**: Various factors including trauma, inflammation, vascular disorders, and degenerative diseases may induce cellular stress in photoreceptors, leading to apoptosis and generation of metabolic debris that contributes to autoimmunization (kalogeropoulos2025diagnosisandtreatment pages 4-5).

### Risk Factors

**Genetic Risk Factors**:
- HLA-DRB1-03 and HLA-DRB1-15 associations: A study of 24 npAIR patients found substantial correlation with these HLA alleles (kalogeropoulos2025diagnosisandtreatment pages 5-7)
- No specific Mendelian inheritance pattern has been identified

**Environmental and Clinical Risk Factors**:
- **Malignancy** (for pAIR):
  - Lung cancer: 16% of CAR/MAR cases
  - Breast cancer: 16%
  - Melanoma: 16%
  - Hematological malignancies: 15%
  - Gynecological cancers: 9%
  - Prostate cancer: 7%
  - Colon cancer: 6%
  (kalogeropoulos2025diagnosisandtreatment pages 2-4)

- **Autoimmune Disease History**: 66.7% (16/24) of npAIR patients had a history of autoimmune disorder, most frequently hypothyroidism (kalogeropoulos2025diagnosisandtreatment pages 2-4)

- **Female Sex**: Higher prevalence in women (62.5-79.2% of npAIR patients are female) (kalogeropoulos2025diagnosisandtreatment pages 2-4)

- **Age**: Middle-aged to older adults most affected (mean age 47-62 years depending on subtype) (kalogeropoulos2025diagnosisandtreatment pages 2-4, kalogeropoulos2025diagnosisandtreatment pages 9-10)

### Protective Factors
No specific protective factors have been identified in the literature reviewed.

### Gene-Environment Interactions
The development of pAIR appears to involve gene-environment interactions where tumor antigens (environmental trigger) in genetically susceptible individuals lead to cross-reactive autoantibody production through molecular mimicry (kalogeropoulos2025diagnosisandtreatment pages 4-5). The interaction between HLA risk alleles and environmental triggers (cancer, infections) may determine disease susceptibility, though this mechanism requires further study (kalogeropoulos2025diagnosisandtreatment pages 5-7).

## 3. Phenotypes

### Clinical Phenotype Overview
| Characteristic | CAR | MAR | npAIR |
|---|---|---|---|
| Age at onset | Mean age for paraneoplastic AIR (CAR/MAR combined) is ~55 years, range 18–88; CAR patients tend to be older than npAIR patients (kalogeropoulos2025diagnosisandtreatment pages 2-4, kalogeropoulos2025diagnosisandtreatment pages 9-10) | Typically middle-aged to older adults, often 40–70 years (kalogeropoulos2025diagnosisandtreatment pages 9-10) | Younger than paraneoplastic AIR on average; reported mean 47–55.9 years, median 47 years, range 11–88 (kalogeropoulos2025diagnosisandtreatment pages 2-4, kalogeropoulos2025diagnosisandtreatment pages 9-10) |
| Sex predilection | Female predominance overall in AIR/paraneoplastic cohorts, though CAR can affect both sexes (kalogeropoulos2025diagnosisandtreatment pages 2-4) | Slight male predominance reported, consistent with melanoma demographics (kalogeropoulos2025diagnosisandtreatment pages 9-10) | Predominantly female; 62.5%–79.2% female in reported series (kalogeropoulos2025diagnosisandtreatment pages 2-4) |
| Associated conditions | Systemic malignancy, especially lung cancer, breast cancer, gynecologic malignancy, hematologic malignancy, and other solid tumors (kalogeropoulos2025diagnosisandtreatment pages 2-4, beuzit2025paraneoplasticocularsyndromes pages 1-2) | Cutaneous or metastatic melanoma; may signal immune response to metastasis (kalogeropoulos2025diagnosisandtreatment pages 1-2, kalogeropoulos2025diagnosisandtreatment pages 10-13) | No malignancy; often associated with personal/family autoimmune history, especially thyroid disease/hypothyroidism and other autoimmune disorders (kalogeropoulos2025diagnosisandtreatment pages 2-4, kalogeropoulos2025diagnosisandtreatment pages 20-22) |
| Primary symptoms | Progressive, painless, bilateral or asymmetric vision loss; photosensitivity, glare, flickering/shimmering lights, central scotoma, night blindness, impaired dark adaptation, peripheral field defects (kalogeropoulos2025diagnosisandtreatment pages 9-10) | Night blindness, photopsia, visual field defects; central/paracentral scotomas common, VA often relatively preserved early (kalogeropoulos2025diagnosisandtreatment pages 9-10) | Gradual or subacute painless bilateral vision loss with photopsias and scotomas; may show visual field loss and color vision impairment (chen2025autoimmuneretinopathyin pages 3-4, kalogeropoulos2025diagnosisandtreatment pages 9-10) |
| Photoreceptor involvement | Often cone-predominant or mixed cone-rod dysfunction; simultaneous rod and cone involvement common, especially with anti-recoverin antibodies (kalogeropoulos2025diagnosisandtreatment pages 9-10) | Classically ON-bipolar cell dysfunction rather than primary photoreceptor loss, though broader retinal dysfunction may occur (kalogeropoulos2025diagnosisandtreatment pages 4-5, kalogeropoulos2025diagnosisandtreatment pages 9-10) | Variable cone, rod, or mixed photoreceptor dysfunction; progressive outer retinal degeneration is typical (chen2025autoimmuneretinopathyin pages 1-2, kalogeropoulos2025diagnosisandtreatment pages 9-10) |
| Fundus findings | Often initially normal despite severe symptoms; later retinal arteriole attenuation, waxy optic disc pallor, RPE changes; occasional iritis/vitritis (kalogeropoulos2025diagnosisandtreatment pages 9-10, kalogeropoulos2025diagnosisandtreatment pages 10-13) | Fundus may be normal or show optic disc pallor, vascular attenuation, RPE change, and vitreous cells/inflammation (kalogeropoulos2025diagnosisandtreatment pages 9-10, kalogeropoulos2025diagnosisandtreatment pages 10-13) | Fundus may be normal early; can develop diffuse pigmentary retinopathy, retinal atrophy, RPE change, disc pallor, and hypo/hyper-autofluorescent abnormalities (chen2025autoimmuneretinopathyin pages 1-2, kalogeropoulos2025diagnosisandtreatment pages 10-13) |
| ERG findings | Abnormal ERG is a core diagnostic feature; mixed cone/rod and isolated rod responses may be markedly attenuated (kalogeropoulos2025diagnosisandtreatment pages 10-13, kalogeropoulos2025diagnosisandtreatment pages 20-22) | Typically electronegative ERG/ON-bipolar dysfunction pattern; negative ERG is characteristic of MAR (kalogeropoulos2025diagnosisandtreatment pages 4-5) | Abnormal ERG required/supportive for diagnosis; rod and cone dysfunction common, often reduced responses on full-field ERG (chen2025autoimmuneretinopathyin pages 1-2, kalogeropoulos2025diagnosisandtreatment pages 20-22) |
| Common antibodies | Anti-recoverin, anti-α-enolase, anti-CAII, anti-transducin; anti-recoverin is the classic CAR antibody (kalogeropoulos2025diagnosisandtreatment pages 2-4, kalogeropoulos2025diagnosisandtreatment pages 4-5) | Anti-TRPM1 is the best-characterized MAR antibody; anti-transducin also reported (kalogeropoulos2025diagnosisandtreatment pages 4-5) | Anti-recoverin, anti-α-enolase, anti-CAII, anti-arrestin, anti-IRBP, anti-TULP1, anti-TRPM1 and others; serology is heterogeneous (kalogeropoulos2025diagnosisandtreatment pages 4-5, chen2025autoimmuneretinopathyin pages 3-4) |
| Prognosis | Often poor visual prognosis; can progress to blindness over days to years; 49.1% worsened in a recent paraneoplastic ocular syndrome review, but early oncologic diagnosis (<6 months) improved outcomes (beuzit2025paraneoplasticocularsyndromes pages 1-2, kalogeropoulos2025diagnosisandtreatment pages 10-13) | Variable; limited follow-up suggests ~half have unilateral or bilateral moderate-to-severe vision loss at last follow-up (kalogeropoulos2025diagnosisandtreatment pages 9-10) | Variable and heterogeneous; may stabilize or improve with immunosuppression, but chronic progressive loss and CME-associated worse outcomes are recognized (kalogeropoulos2025diagnosisandtreatment pages 9-10, kalogeropoulos2025diagnosisandtreatment pages 22-23) |


*Table: This table compares the three principal autoimmune retinopathy subtypes across demographics, associated conditions, symptoms, retinal physiology, antibodies, and prognosis. It is useful for quickly distinguishing paraneoplastic from non-paraneoplastic disease patterns.*

### Symptoms and Clinical Signs

**Common Symptoms**:
- **Progressive bilateral vision loss**: Painless, subacute to chronic (days to years)
- **Photopsia**: Flickering, shimmering lights, or flashes
- **Scotomas**: Central, paracentral, or ring scotomas
- **Night blindness (nyctalopia)**: Particularly in rod-predominant disease
- **Photosensitivity and glare**
- **Impaired dark adaptation**
- **Color vision defects**
- **Peripheral visual field constriction**
(kalogeropoulos2025diagnosisandtreatment pages 1-2, chen2025autoimmuneretinopathyin pages 1-2, chen2025autoimmuneretinopathyin pages 3-4, kalogeropoulos2025diagnosisandtreatment pages 9-10, kalogeropoulos2025diagnosisandtreatment pages 10-13)

**HPO Terms (Suggested)**:
- HP:0000572: Visual loss
- HP:0000505: Visual impairment
- HP:0000529: Progressive visual loss
- HP:0012372: Abnormal cone/rod electroretinogram
- HP:0000662: Nyctalopia (night blindness)
- HP:0000613: Photophobia
- HP:0030453: Abnormal visual field
- HP:0007994: Peripheral visual field loss
- HP:0007973: Abnormal retinal morphology

### Phenotype Characteristics

**Age of Onset**:
- CAR/MAR: Mean 55 years (range 18-88 years) (kalogeropoulos2025diagnosisandtreatment pages 2-4, kalogeropoulos2025diagnosisandtreatment pages 9-10)
- npAIR: Younger, mean 47-55.9 years, median 47 years (range 11-88 years) (kalogeropoulos2025diagnosisandtreatment pages 2-4)

**Symptom Severity**: Variable, ranging from mild visual disturbance to complete blindness. CAR has particularly poor prognosis with 49.1% experiencing worsening vision (beuzit2025paraneoplasticocularsyndromes pages 1-2, kalogeropoulos2025diagnosisandtreatment pages 10-13).

**Symptom Progression**:
- **Progressive**: Most cases show relentless progression without treatment
- **Time Course**: Can progress from days to years
- **Pattern**: Bilateral but often asymmetric initially; may involve both rods and cones or be photoreceptor-subtype selective

**Frequency**:
- Bilateral involvement: >90% of cases eventually bilateral (beuzit2025paraneoplasticocularsyndromes pages 1-2)
- Mixed rod-cone dysfunction: Common, especially with anti-recoverin antibodies (kalogeropoulos2025diagnosisandtreatment pages 9-10)
- Cystoid macular edema (CME): Frequent complication, present in significant proportion of npAIR patients and associated with worse outcomes (kalogeropoulos2025diagnosisandtreatment pages 9-10, kalogeropoulos2025diagnosisandtreatment pages 10-13)

### Fundus and Structural Findings
- Often normal initially despite severe symptoms (kalogeropoulos2025diagnosisandtreatment pages 9-10, kalogeropoulos2025diagnosisandtreatment pages 10-13)
- Retinal arteriole attenuation
- Waxy optic disc pallor
- RPE changes: pigmentary abnormalities, atrophy
- Diffuse pigmentary retinopathy (in advanced disease)
- Vitreous cells (inflammation, especially MAR)
- Occasional iritis/vitritis (kalogeropoulos2025diagnosisandtreatment pages 9-10, kalogeropoulos2025diagnosisandtreatment pages 10-13)

### Quality of Life Impact
Visual disability from AIR significantly impacts daily functioning and quality of life. CME is a biomarker of more severe and more progressive disease and is associated with rapid ellipsoid zone loss, worse visual acuity, and poorer visual outcomes (kalogeropoulos2025diagnosisandtreatment pages 9-10, kalogeropoulos2025diagnosisandtreatment pages 10-13). The disease causes preventable blindness and substantial psychosocial burden due to progressive, often irreversible vision loss affecting working-age adults (kalogeropoulos2025diagnosisandtreatment pages 2-4).

## 4. Genetic/Molecular Information

### Causal Genes and Pathogenic Antigens
AIR is not caused by mutations in specific genes but rather by autoantibodies targeting retinal proteins. The disease involves humoral autoimmunity rather than traditional Mendelian genetic causation.

### Pathogenic Autoantibodies and Target Antigens
| Antibody name | Molecular weight (kDa) | Target antigen | Cell types affected | Mechanism of action / pathogenic effect | Association (CAR/MAR/npAIR) |
|---|---:|---|---|---|---|
| Anti-recoverin | 23 | Recoverin, a photoreceptor calcium-binding protein | Photoreceptors (rods and cones) | Antibody binding is associated with intracellular calcium dysregulation and caspase-mediated apoptosis, causing photoreceptor degeneration and vision loss; among the best-studied pathogenic AIR antibodies (kalogeropoulos2025diagnosisandtreatment pages 4-5, kalogeropoulos2025diagnosisandtreatment pages 5-7) | CAR, npAIR; also reported broadly across AIR spectrum (kalogeropoulos2025diagnosisandtreatment pages 4-5) |
| Anti-α-enolase | 46 | α-Enolase, a glycolytic enzyme | Ganglion cells, Müller cells, rods, cones | Inhibits enolase catalytic function, leading to ATP depletion, increased intracellular calcium, and apoptotic retinal cell death (kalogeropoulos2025diagnosisandtreatment pages 4-5) | CAR, MAR, npAIR (kalogeropoulos2025diagnosisandtreatment pages 4-5) |
| Anti-rod transducin | 38 | Rod transducin (phototransduction G-protein) | Rod photoreceptors | Disrupts phototransduction signaling; abnormal antigen expression in cancer cells may trigger cross-reactive autoimmunity, with downstream calcium imbalance and apoptosis proposed (kalogeropoulos2025diagnosisandtreatment pages 4-5) | CAR, MAR, npAIR (kalogeropoulos2025diagnosisandtreatment pages 4-5) |
| Anti-arrestin (S-antigen) | 48 | Arrestin / S-antigen | Retinal cells, especially photoreceptor-associated pathways | Interferes with phototransduction regulation; recognized as a recurrent npAIR antigen, but direct pathogenic evidence is less developed than for recoverin/enolase (kalogeropoulos2025diagnosisandtreatment pages 4-5) | Primarily npAIR (kalogeropoulos2025diagnosisandtreatment pages 4-5) |
| Anti-carbonic anhydrase II (CA-II) | 30 | Carbonic anhydrase II | Retinal cells | Impairs CA-II catalytic activity, decreases intracellular pH, increases intracellular calcium, and reduces retinal cell viability, contributing to retinal degeneration (kalogeropoulos2025diagnosisandtreatment pages 4-5) | CAR and AIR without cancer / npAIR (kalogeropoulos2025diagnosisandtreatment pages 4-5) |
| Anti-IRBP | 141 | Interphotoreceptor retinoid-binding protein (IRBP) | Photoreceptor-retinoid interface / interphotoreceptor matrix | Disrupts retinoid transport and photoreceptor homeostasis; listed as a recurrent npAIR target, with pathogenic relevance suggested but less directly proven than recoverin/enolase (kalogeropoulos2025diagnosisandtreatment pages 4-5, kalogeropoulos2025diagnosisandtreatment pages 7-8) | Primarily npAIR (kalogeropoulos2025diagnosisandtreatment pages 4-5, kalogeropoulos2025diagnosisandtreatment pages 7-8) |
| Anti-TRPM1 | 182 | TRPM1 cation channel | Retinal ON-bipolar cells | In animal transfer experiments, anti-TRPM1 antibodies altered ERG responses and induced acute ON-bipolar cell death, explaining electronegative ERG/ON-bipolar dysfunction typical of MAR-like disease (kalogeropoulos2025diagnosisandtreatment pages 4-5) | MAR; also paraneoplastic retinopathy more broadly (kalogeropoulos2025diagnosisandtreatment pages 4-5) |
| Anti-TULP1 | 64 | Tubby-like protein 1 (TULP1) | Photoreceptors | Associated with photoreceptor dysfunction/degeneration; reported as a candidate AIR autoantigen, but pathogenic mechanism remains less well established than canonical antibodies (kalogeropoulos2025diagnosisandtreatment pages 4-5, kalogeropoulos2025diagnosisandtreatment pages 7-8) | Reported in npAIR / broader AIR spectrum (kalogeropoulos2025diagnosisandtreatment pages 4-5, kalogeropoulos2025diagnosisandtreatment pages 7-8) |


*Table: This table summarizes the principal antiretinal autoantibodies implicated in autoimmune retinopathy, including their molecular targets, affected retinal cell types, proposed pathogenic mechanisms, and disease associations across CAR, MAR, and non-paraneoplastic AIR.*

Key autoantibodies include:

1. **Anti-recoverin (23 kDa)**: Targets photoreceptor calcium-binding protein; causes calcium dysregulation, caspase-mediated apoptosis, and photoreceptor degeneration (kalogeropoulos2025diagnosisandtreatment pages 4-5, kalogeropoulos2025diagnosisandtreatment pages 5-7)

2. **Anti-α-enolase (46 kDa)**: Targets glycolytic enzyme; inhibits catalytic function leading to ATP depletion, increased intracellular calcium, and apoptosis (kalogeropoulos2025diagnosisandtreatment pages 4-5)

3. **Anti-TRPM1 (182 kDa)**: Targets cation channel in ON-bipolar cells; animal studies show it alters ERG and induces acute bipolar cell death, characteristic of MAR (kalogeropoulos2025diagnosisandtreatment pages 4-5)

4. **Anti-carbonic anhydrase II (30 kDa)**: Impairs catalytic activity, decreases intracellular pH, increases calcium, reduces cell viability (kalogeropoulos2025diagnosisandtreatment pages 4-5)

5. **Anti-rod transducin (38 kDa)**: Disrupts phototransduction; abnormal expression in cancer triggers cross-reactivity (kalogeropoulos2025diagnosisandtreatment pages 4-5)

6. **Anti-arrestin/S-antigen (48 kDa)**: Interferes with phototransduction regulation; common in npAIR (kalogeropoulos2025diagnosisandtreatment pages 4-5)

7. **Anti-IRBP (141 kDa)**: Disrupts retinoid transport and photoreceptor homeostasis (kalogeropoulos2025diagnosisandtreatment pages 4-5, kalogeropoulos2025diagnosisandtreatment pages 7-8)

8. **Anti-TULP1 (64 kDa)**: Associated with photoreceptor dysfunction (kalogeropoulos2025diagnosisandtreatment pages 4-5, kalogeropoulos2025diagnosisandtreatment pages 7-8)

### Modifier Genes
HLA-DRB1-03 and HLA-DRB1-15 appear to modify disease susceptibility in npAIR, with substantial correlation noted in affected patients (kalogeropoulos2025diagnosisandtreatment pages 5-7).

### Functional Consequences and Molecular Profiling
**Mechanisms of Retinal Cell Death**:
- **Calcium Dysregulation**: Anti-recoverin and anti-enolase antibodies increase intracellular calcium levels, triggering apoptosis (kalogeropoulos2025diagnosisandtreatment pages 4-5, kalogeropoulos2025diagnosisandtreatment pages 5-7)
- **ATP Depletion**: Anti-enolase inhibits glycolysis, depleting cellular energy (kalogeropoulos2025diagnosisandtreatment pages 4-5)
- **Caspase Activation**: Multiple antibodies trigger caspase-mediated apoptotic pathways (kalogeropoulos2025diagnosisandtreatment pages 4-5, kalogeropoulos2025diagnosisandtreatment pages 5-7)
- **pH Disruption**: Anti-CAII causes intracellular acidification (kalogeropoulos2025diagnosisandtreatment pages 4-5)
- **Phototransduction Disruption**: Multiple antibodies interfere with visual signal transduction (kalogeropoulos2025diagnosisandtreatment pages 4-5)

**Epigenetic Information**: No specific epigenetic changes have been characterized in AIR.

**Chromosomal Abnormalities**: Not applicable; AIR is not caused by chromosomal abnormalities.

## 5. Environmental Information

### Environmental Factors
**Malignancy as Environmental Trigger**: The presence of cancer acts as the primary environmental trigger in pAIR. Tumor cells expressing retinal-like antigens initiate cross-reactive immune responses (kalogeropoulos2025diagnosisandtreatment pages 2-4, kalogeropoulos2025diagnosisandtreatment pages 4-5).

**Infectious Agents**: Molecular mimicry between retinal antigens and proteins present in pathogens (bacteria or viruses) may trigger npAIR through cross-reactive antibody production (kalogeropoulos2025diagnosisandtreatment pages 4-5).

### Lifestyle Factors
No specific lifestyle factors (smoking, diet, exercise, alcohol) have been definitively linked to AIR risk.

## 6. Mechanism/Pathophysiology

### Overview of Pathogenic Process
"Although the presence of ARAs in the patients' serum is confirmed, their precise role remains uncertain. It is likely that these ARAs are produced due to an overly aggressive immune response to antigens in the retina" (kalogeropoulos2025diagnosisandtreatment pages 2-4).

### Molecular Pathways

**Apoptotic Pathways**: Multiple ARAs trigger apoptosis through:
- Caspase-3 activation (kalogeropoulos2025diagnosisandtreatment pages 4-5, kalogeropoulos2025diagnosisandtreatment pages 5-7)
- Cytochrome c release (kalogeropoulos2025diagnosisandtreatment pages 5-7)
- Balance shift toward pro-apoptotic proteins (kalogeropoulos2025diagnosisandtreatment pages 5-7)

**Calcium Signaling**: Disrupted calcium homeostasis is a central mechanism. "Exposure to these antibodies increased intracellular calcium levels, which could be suppressed by a calcium channel blocker called nifedipine" (kalogeropoulos2025diagnosisandtreatment pages 5-7), suggesting calcium channel involvement in pathogenesis.

**Metabolic Dysfunction**: Anti-enolase "inhibited enolase's catalytic function, leading to ATP depletion, increased intracellular calcium levels, and apoptotic cell death" (kalogeropoulos2025diagnosisandtreatment pages 4-5).

**Inflammatory Pathways**: Blood-retinal barrier disruption, upregulation of MCP-1 (CCL2) chemokine, and attraction of macrophages/microglia contribute to photoreceptor damage (kalogeropoulos2025diagnosisandtreatment pages 5-7).

### Cellular Processes
- **Apoptosis**: Photoreceptor and bipolar cell death via multiple pathways (kalogeropoulos2025diagnosisandtreatment pages 4-5, kalogeropoulos2025diagnosisandtreatment pages 5-7)
- **Inflammation**: Chronic low-grade inflammation with immune cell infiltration (kalogeropoulos2025diagnosisandtreatment pages 5-7)
- **Blood-Retinal Barrier Breakdown**: ARAs disrupt barrier integrity, allowing further antibody access (kalogeropoulos2025diagnosisandtreatment pages 5-7)

**GO Terms (Suggested)**:
- GO:0006915: apoptotic process
- GO:0006954: inflammatory response
- GO:0006816: calcium ion transport
- GO:0006096: glycolytic process
- GO:0007601: visual perception
- GO:0009416: response to light stimulus
- GO:0007602: phototransduction

### Protein Dysfunction
ARAs cause protein dysfunction through:
- **Loss of Function**: Enzyme inhibition (enolase, CAII)
- **Dominant Negative Effect**: Antibody binding preventing normal protein function
- **Conformational Changes**: Antibody-induced structural alterations

### Immune System Involvement
**Autoimmune Mechanism**: AIR involves breakdown of ocular immune privilege with generation of pathogenic autoantibodies against retinal self-antigens (kalogeropoulos2025diagnosisandtreatment pages 2-4, kalogeropoulos2025diagnosisandtreatment pages 4-5). The thymus-retina connection is important: "The retina contains numerous proteins expressed also in the thymus, as well as other secondary lymphoid tissues. In the thymus, the process of negative selection plays a crucial role in establishing self-tolerance" (kalogeropoulos2025diagnosisandtreatment pages 2-4).

**Cell Types Involved** (CL Terms Suggested):
- CL:0000573: retinal cone cell
- CL:0000604: retinal rod cell
- CL:0000748: retinal bipolar neuron
- CL:0000129: microglial cell
- CL:0000235: macrophage
- CL:0000236: B cell

### Tissue Damage Mechanisms
- **Oxidative Stress**: Contributes to photoreceptor degeneration
- **Ischemia**: Not a primary mechanism
- **Inflammation**: Chronic inflammatory processes damage retinal architecture
- **Apoptosis**: Primary mechanism of cell loss

## 7. Anatomical Structures Affected

### Organ Level
**Primary Organ**: Eye - specifically the retina (UBERON:0000966)

**Body System**: 
- Sensory system (visual system)
- UBERON:0002104 (visual system)

### Tissue and Cell Level
**Tissues Affected**:
- Neural retina (UBERON:0000966)
- Retinal pigment epithelium (UBERON:0001782)
- Photoreceptor layer (UBERON:0001791)

**Cell Populations Targeted**:
- Photoreceptors (rods: CL:0000604, cones: CL:0000573)
- Retinal bipolar neurons (CL:0000748) - especially in MAR
- Retinal ganglion cells (CL:0000740)
- Müller cells (CL:0000636)

### Subcellular Level
**Cellular Compartments** (GO Cellular Component Terms):
- GO:0001750: photoreceptor outer segment
- GO:0042995: cell projection
- GO:0005886: plasma membrane
- GO:0005739: mitochondrion (metabolic dysfunction site)
- GO:0005737: cytoplasm (site of glycolytic enzyme disruption)

### Localization
**Anatomical Sites**:
- Posterior pole (macula)
- Peripheral retina
- Parafoveal and perifoveal regions

**Lateralization**: Bilateral but often asymmetric initially; eventually bilateral in >90% (beuzit2025paraneoplasticocularsyndromes pages 1-2, kalogeropoulos2025diagnosisandtreatment pages 9-10)

## 8. Temporal Development

### Onset
**Typical Age of Onset**:
- pAIR (CAR/MAR): Mean 55 years (range 18-88)
- npAIR: Mean 47-55.9 years (range 11-88)
- Predominantly adult-onset (kalogeropoulos2025diagnosisandtreatment pages 2-4, kalogeropoulos2025diagnosisandtreatment pages 9-10)

**Onset Pattern**: Subacute to chronic; painless progression over days to years (kalogeropoulos2025diagnosisandtreatment pages 9-10, kalogeropoulos2025diagnosisandtreatment pages 10-13)

### Progression
**Disease Stages**: Not formally staged, but progression includes:
- Early: Symptoms with normal-appearing fundus
- Intermediate: Detectable retinal changes on imaging (FAF, OCT, ERG abnormalities)
- Advanced: Visible fundus changes, severe vision loss, widespread retinal atrophy

**Progression Rate**: Variable; can be rapid (days to weeks) or slow (months to years). Latency between cancer diagnosis and retinopathy onset: weeks to months for lung cancers and lymphomas; years for breast and prostate cancers (kalogeropoulos2025diagnosisandtreatment pages 2-4).

**Disease Course Pattern**: 
- Progressive in most untreated cases
- Relapsing-remitting pattern not typical
- Chronic course leading to irreversible retinal damage

**Disease Duration**: Chronic, lifelong once established

### Patterns
**Remission**: Spontaneous remission is not characteristic. Treatment-induced stabilization or improvement may occur with immunosuppression (kalogeropoulos2025diagnosisandtreatment pages 9-10, kalogeropoulos2025diagnosisandtreatment pages 22-23).

**Critical Periods**: Early diagnosis is critical as retinal damage becomes irreversible. In CAR, early oncologic diagnosis (within 6 months after symptom onset) was significantly associated with favorable visual outcome (p = 0.03) (beuzit2025paraneoplasticocularsyndromes pages 1-2).

## 9. Inheritance and Population

### Epidemiology
**Prevalence**: Extremely rare; accounts for less than 1% of cases at tertiary referral centers (kalogeropoulos2025diagnosisandtreatment pages 2-4). No population-based prevalence data available.

**Incidence**: Not reported in available literature.

### Genetic Patterns
**Inheritance Pattern**: Not a Mendelian inherited disorder. AIR is an acquired autoimmune condition. No evidence of familial clustering or traditional inheritance patterns.

**HLA Associations**: Substantial correlation with HLA-DRB1-03 and HLA-DRB1-15 in npAIR (kalogeropoulos2025diagnosisandtreatment pages 5-7).

### Population Demographics

**Affected Populations**:
- Female predominance (62.5-79.2% in npAIR; female predominance also in pAIR) (kalogeropoulos2025diagnosisandtreatment pages 2-4)
- Middle-aged to older adults most affected

**Cancer Associations in pAIR**:
- Lung: 16%
- Breast: 16%
- Melanoma: 16%
- Hematological: 15%
- Gynecological: 9%
- Prostate: 7%
- Colon: 6%
(kalogeropoulos2025diagnosisandtreatment pages 2-4)

**Geographic Distribution**: No specific geographic clustering reported. Disease described worldwide in literature from multiple countries (kalogeropoulos2025diagnosisandtreatment pages 1-2, beuzit2025paraneoplasticocularsyndromes pages 1-2, chen2025autoimmuneretinopathyin pages 1-2).

**Sex Ratio**: Predominantly female (approximately 2-3:1 female:male ratio in npAIR) (kalogeropoulos2025diagnosisandtreatment pages 2-4).

**Age Distribution**: Peak incidence in middle to older adulthood (40-70 years) (kalogeropoulos2025diagnosisandtreatment pages 2-4, kalogeropoulos2025diagnosisandtreatment pages 9-10).

## 10. Diagnostics

### Clinical Tests

**Laboratory Tests**:
- **Serum antiretinal antibody (ARA) testing**: Essential but not always positive. Methods include immunohistochemistry (IHC), Western blotting (WB), and ELISA. "It is recommended to employ two techniques simultaneously to enhance both sensitivity and specificity" (kalogeropoulos2025diagnosisandtreatment pages 20-22).
- Less than half (47.1%, 111/193) of clinically diagnosed AIR patients tested positive for ARAs (kalogeropoulos2025diagnosisandtreatment pages 5-7)

**Biomarkers**:
- Circulating ARAs (recoverin, enolase, TRPM1, etc.)
- CME on OCT as biomarker of disease severity and progression (kalogeropoulos2025diagnosisandtreatment pages 9-10, kalogeropoulos2025diagnosisandtreatment pages 10-13)

**Imaging Studies**:
- **Optical Coherence Tomography (OCT)**: Shows outer retinal layer atrophy, ellipsoid zone disruption, CME, retinal thinning (kalogeropoulos2025diagnosisandtreatment pages 10-13)
- **Fundus Autofluorescence (FAF)**: Granular hyperautofluorescence in posterior pole, macular/peripapillary regions; large areas of peripheral hyperautofluorescence creating demarcation lines (kalogeropoulos2025diagnosisandtreatment pages 10-13)
- **Fluorescein Angiography (FA)**: May show retinal vascular leakage
- **Fundus Photography**: Documents pigmentary changes, vascular attenuation, disc pallor

**Functional Tests**:
- **Electroretinography (ERG)**: Abnormal ERG is a core diagnostic feature. Shows:
  - Reduced or absent mixed cone-rod responses
  - Attenuated isolated rod responses
  - Electronegative ERG pattern in MAR (characteristic ON-bipolar dysfunction)
  (kalogeropoulos2025diagnosisandtreatment pages 10-13, kalogeropoulos2025diagnosisandtreatment pages 20-22)
- **Visual Field Testing**: Demonstrates central scotomas, ring scotomas, peripheral field loss (kalogeropoulos2025diagnosisandtreatment pages 10-13)
- **Color Vision Testing**: Impaired color discrimination

**Pathology Findings**: Histopathology rarely performed; when available, shows photoreceptor loss, RPE atrophy, inflammatory infiltrates.

### Genetic Testing
Not applicable for diagnosis. Genetic testing may be used to rule out inherited retinal dystrophies in the differential diagnosis (kalogeropoulos2025diagnosisandtreatment pages 20-22).

**Differential Diagnosis Genetic Testing**:
- Screening for retinitis pigmentosa genes
- Cone-rod dystrophy gene panels
- Necessary to distinguish npAIR from inherited retinal diseases (IRDs) (kalogeropoulos2025diagnosisandtreatment pages 20-22)

### Clinical Criteria
**Diagnostic Criteria** (2016 consensus, though no international consensus exists):
- Absence of other identifiable causes of visual function abnormalities
- Abnormal ERG results
- Presence of serum ARAs
- Absence of significant intraocular inflammation
(kalogeropoulos2025diagnosisandtreatment pages 10-13)

**Supportive Criteria**:
- Personal/family history of autoimmune disease
- Signs/symptoms of photoreceptor dysfunction
- Rapid onset of vision changes
(kalogeropoulos2025diagnosisandtreatment pages 10-13)

**Differential Diagnosis**:
- White Dot Syndrome spectrum (AZOOR, MEWDS)
- Inherited retinal dystrophies (retinitis pigmentosa, cone-rod dystrophy)
- Infectious/non-infectious uveitis
- Paraneoplastic conditions affecting RPE (BDUMP)
- Drug toxicity (hydroxychloroquine)
- Pseudo-retinitis pigmentosa (syphilis)
(kalogeropoulos2025diagnosisandtreatment pages 20-22, kalogeropoulos2025diagnosisandtreatment pages 10-13)

### Screening
**Cancer Screening in pAIR**: Comprehensive oncological workup essential. Imaging (CT, PET-CT), tumor markers, and targeted screening based on age/sex (beuzit2025paraneoplasticocularsyndromes pages 1-2, kalogeropoulos2025diagnosisandtreatment pages 10-13).

**At-Risk Population Monitoring**: Patients with known autoimmune diseases should be monitored for visual symptoms (kalogeropoulos2025diagnosisandtreatment pages 2-4).

## 11. Outcome/Prognosis

### Survival and Mortality
AIR itself is not directly life-threatening, but associated malignancies in pAIR significantly impact survival. The visual prognosis is generally poor to guarded.

### Morbidity and Function
**Visual Outcomes**:
- CAR: Poor prognosis; 49.1% of patients experienced worsening vision in systematic review (beuzit2025paraneoplasticocularsyndromes pages 1-2)
- Early oncologic diagnosis (<6 months from symptom onset) significantly associated with favorable visual outcome in CAR (p = 0.03) (beuzit2025paraneoplasticocularsyndromes pages 1-2)
- MAR: Variable; approximately half had moderate to severe vision loss at last follow-up (kalogeropoulos2025diagnosisandtreatment pages 9-10)
- npAIR: Variable; may stabilize with treatment but CME predicts worse outcomes (kalogeropoulos2025diagnosisandtreatment pages 9-10, kalogeropoulos2025diagnosisandtreatment pages 10-13)

**Disability**: Progressive vision loss leading to legal blindness; significant impact on activities of daily living, employment, and quality of life.

**Quality of Life**: "CME is a biomarker of more severe and more progressive disease in npAIR and is associated with visual disability and impact productivity and quality of life" (kalogeropoulos2025diagnosisandtreatment pages 9-10, kalogeropoulos2025diagnosisandtreatment pages 10-13).

### Disease Course
**Complications**:
- Cystoid macular edema (CME) - persistent despite treatment in some cases
- Progressive ellipsoid zone loss
- Retinal atrophy
- Complete vision loss/blindness
- Vitreous inflammation
(kalogeropoulos2025diagnosisandtreatment pages 9-10, kalogeropoulos2025diagnosisandtreatment pages 10-13)

**Recovery Potential**: Generally poor without treatment. Immunosuppression may stabilize or improve some cases, but irreversible photoreceptor loss limits recovery potential (kalogeropoulos2025diagnosisandtreatment pages 9-10, kalogeropoulos2025diagnosisandtreatment pages 22-23).

### Prediction
**Prognostic Factors**:
- Time to cancer diagnosis (earlier better in CAR) (beuzit2025paraneoplasticocularsyndromes pages 1-2)
- Presence of CME (worse prognosis) (kalogeropoulos2025diagnosisandtreatment pages 9-10, kalogeropoulos2025diagnosisandtreatment pages 10-13)
- Shorter ellipsoid zone length (worse prognosis)
- Specific antibody profile (mixed evidence)
- Age (older may be worse)
- Disease duration before treatment initiation

**Prognostic Biomarkers**:
- CME on OCT
- Ellipsoid zone length on OCT
- ERG amplitude decline
- Persistent/rising ARA titers

## 12. Treatment

| Treatment category | Specific agents/approaches | Mechanism of action | Evidence level / response rates | Key references / notes |
|---|---|---|---|---|
| Corticosteroids (systemic) | Oral prednisone 60–80 mg/day; intravenous methylprednisolone induction | Broad anti-inflammatory and immunosuppressive effects; suppress autoimmune retinal injury | Evidence mainly from retrospective series and case reports; no standardized regimen; IV methylprednisolone reported to have better outcomes than oral prednisone in some reports (kalogeropoulos2025diagnosisandtreatment pages 22-23) | Common first-line therapy after excluding/treating underlying malignancy or systemic disease; early treatment considered important to limit irreversible retinal damage; no randomized controlled trials (kalogeropoulos2025diagnosisandtreatment pages 20-22, kalogeropoulos2025diagnosisandtreatment pages 22-23) |
| Corticosteroids (local) | Intravitreal triamcinolone; sub-Tenon triamcinolone; intravitreal sustained-release fluocinolone acetonide implant; topical/depot steroids | Local suppression of ocular inflammation with reduced systemic exposure | Brief intravitreal/sub-Tenon steroid trial has been proposed diagnostically/therapeutically; case reports describe restoration of retinal anatomy and vision improvement in CAR and benefit in MAR with fluocinolone implant; evidence limited to case reports/series (kalogeropoulos2025diagnosisandtreatment pages 22-23) | Suggested by some authors before prolonged systemic steroids to verify steroid responsiveness; used for CME and local disease control; protocol not standardized (kalogeropoulos2025diagnosisandtreatment pages 22-23) |
| Immunomodulators / steroid-sparing agents | Azathioprine, cyclosporine, mycophenolate mofetil, infliximab, methotrexate | Reduce adaptive immune activation and autoantibody-associated inflammation; steroid-sparing maintenance therapy | Retrospective triple-therapy series (cyclosporine + azathioprine + prednisone) in 30 patients reported overall response in 70%; among npAIR, 54% without CME and 73% with CME responded, but study limitations were substantial (kalogeropoulos2025diagnosisandtreatment pages 22-23) | Frequently used when corticosteroids are insufficient or not tolerated; evidence is heterogeneous and vulnerable to publication bias; successful methotrexate use is not well documented in npAIR (kalogeropoulos2025diagnosisandtreatment pages 20-22, kalogeropoulos2025diagnosisandtreatment pages 22-23) |
| Biologic agents | Rituximab; tocilizumab; sarilumab; alemtuzumab; ipilimumab | Rituximab depletes CD20+ B cells and pro-inflammatory CD3+CD20+ T cells; IL-6 blockade (tocilizumab/sarilumab) may reduce refractory CME/inflammation; ipilimumab augments anti-tumor immunity in melanoma-associated disease | Rituximab has the strongest biologic signal in AIR from retrospective series and case reports; one 16-patient series reported stable or improved visual outcomes in 77% of eyes with rituximab-based combinations; anti-IL-6 therapies reported complete resolution of refractory CME in isolated case reports (kalogeropoulos2025diagnosisandtreatment pages 22-23) | Biologics are generally used for refractory disease; evidence remains low-level and non-comparative; recent reviews emphasize lack of prospective trials and no standard treatment protocol (kalogeropoulos2025diagnosisandtreatment pages 1-2, kalogeropoulos2025diagnosisandtreatment pages 20-22, kalogeropoulos2025diagnosisandtreatment pages 22-23) |
| IVIG | Intravenous immunoglobulin | Immunomodulation via Fc-mediated immune regulation, neutralization of pathogenic antibodies, and altered B/T-cell signaling | Evidence limited to case reports/small series; sometimes used in combination with steroids or other immunosuppressants; no robust response-rate estimate available (kalogeropoulos2025diagnosisandtreatment pages 22-23) | Considered an option in refractory AIR, especially when humoral autoimmunity is suspected; included among available therapies in recent review tables (kalogeropoulos2025diagnosisandtreatment pages 22-23) |
| Plasmapheresis / plasma exchange | Therapeutic plasma exchange, often combined with systemic immunosuppression | Removes circulating antiretinal autoantibodies and immune mediators | Evidence limited to case reports and small series; no standardized schedule or comparative efficacy data available (kalogeropoulos2025diagnosisandtreatment pages 22-23) | Mechanistically attractive for antibody-mediated disease, but current support is anecdotal; should be interpreted cautiously due to absence of controlled trials (kalogeropoulos2025diagnosisandtreatment pages 20-22, kalogeropoulos2025diagnosisandtreatment pages 22-23) |
| Tumor-directed therapies (paraneoplastic AIR) | Surgical cytoreduction, chemotherapy, radiotherapy; treatment of underlying malignancy before ocular immunosuppression | Reduces tumor antigen burden that may drive molecular mimicry and autoantibody production | Evidence indirect but clinically important; early oncologic diagnosis in CAR was associated with better visual outcomes in a recent paraneoplastic review; treatment of malignancy is foundational in pAIR (beuzit2025paraneoplasticocularsyndromes pages 1-2, kalogeropoulos2025diagnosisandtreatment pages 22-23) | Recommended first in pAIR/CAR/MAR before or alongside ocular immunosuppression; MAR may indicate immune response to melanoma metastasis, and immunosuppression can theoretically worsen tumor control (beuzit2025paraneoplasticocularsyndromes pages 1-2, kalogeropoulos2025diagnosisandtreatment pages 10-13, kalogeropoulos2025diagnosisandtreatment pages 22-23) |
| Overall treatment strategy / evidence gap | Multidisciplinary individualized care; combine oncology, ophthalmology, rheumatology/immunology; monitor ERG, OCT, FAF, visual fields | Tailors therapy to subtype (CAR, MAR, npAIR), systemic disease, and structural/functional progression | No international standard treatment protocol; evidence base is dominated by retrospective series and case reports; prospective randomized placebo-controlled trials are explicitly needed (kalogeropoulos2025diagnosisandtreatment pages 1-2, kalogeropoulos2025diagnosisandtreatment pages 20-22, kalogeropoulos2025diagnosisandtreatment pages 22-23) | Current management is empirical; early diagnosis is repeatedly emphasized because retinal damage may become irreversible and pAIR can precede cancer detection (kalogeropoulos2025diagnosisandtreatment pages 1-2, kalogeropoulos2025diagnosisandtreatment pages 20-22, kalogeropoulos2025diagnosisandtreatment pages 22-23) |


*Table: This table summarizes the main currently reported treatment approaches for autoimmune retinopathy, their rationale, and the level of supporting evidence. It is useful because AIR management remains non-standardized and is based largely on retrospective series and case reports rather than prospective trials.*

### Pharmacotherapy

**Corticosteroids**:
- **Systemic**: Prednisone 60-80 mg/day orally; IV methylprednisolone for induction (kalogeropoulos2025diagnosisandtreatment pages 22-23)
- **Local**: Intravitreal triamcinolone (40-80 mg), sub-Tenon triamcinolone, sustained-release fluocinolone implant (kalogeropoulos2025diagnosisandtreatment pages 22-23)
- Mechanism: Broad immunosuppression and anti-inflammatory effects
- Evidence: Case series and retrospective studies; no RCTs (kalogeropoulos2025diagnosisandtreatment pages 20-22, kalogeropoulos2025diagnosisandtreatment pages 22-23)

**Immunomodulators**:
- Azathioprine, cyclosporine, mycophenolate mofetil, methotrexate
- Mechanism: Steroid-sparing agents; reduce adaptive immune activation
- Evidence: Retrospective triple-therapy series (cyclosporine + azathioprine + prednisone) showed 70% overall response (kalogeropoulos2025diagnosisandtreatment pages 22-23)
- MAXO terms: MAXO:0000882 (immunosuppressive therapy)

### Advanced Therapeutics

**Biologic Agents**:
- **Rituximab**: Most extensively studied biologic; CD20+ B-cell depletion
  - Evidence: Multiple case series; 83.5% positive response in uveitis review; 77% stable/improved visual outcomes in AIR series (kalogeropoulos2025diagnosisandtreatment pages 22-23)
  - MAXO: MAXO:0001298 (rituximab therapy)

- **IL-6 Blockade**: Tocilizumab, sarilumab
  - Evidence: Case reports showing complete resolution of refractory CME (kalogeropoulos2025diagnosisandtreatment pages 22-23)

- **Ipilimumab**: For melanoma-associated MAR refractory to other treatments (kalogeropoulos2025diagnosisandtreatment pages 22-23)

**Immunotherapies**: IVIG mechanism includes Fc-mediated immune regulation and antibody neutralization; evidence limited to case reports (kalogeropoulos2025diagnosisandtreatment pages 22-23).

### Surgical and Interventional
**Tumor-Directed Surgery**: Essential first-line in pAIR; cytoreduction, resection of primary malignancy (beuzit2025paraneoplasticocularsyndromes pages 1-2, kalogeropoulos2025diagnosisandtreatment pages 22-23).

### Supportive and Rehabilitative
- Low vision rehabilitation
- Occupational therapy
- Psychological support for chronic vision loss

### Experimental
- Plasmapheresis/plasma exchange: Removes circulating antibodies; limited case report evidence (kalogeropoulos2025diagnosisandtreatment pages 22-23)
- Anti-cytokine therapies under investigation
- No active registered clinical trials identified in literature review

### Treatment Outcomes
**Response Rates**:
- Corticosteroids: Variable responses; no standardized efficacy data
- Triple immunosuppression: 70% overall response (kalogeropoulos2025diagnosisandtreatment pages 22-23)
- Rituximab: 83.5% positive response in non-infectious uveitis; 77% in AIR series (kalogeropoulos2025diagnosisandtreatment pages 22-23)

**Adverse Events**:
- Corticosteroids: Systemic side effects (osteoporosis, weight gain, hyperglycemia, infection)
- Rituximab: Infusion reactions most common (31.4% of adverse events); well-tolerated overall (kalogeropoulos2025diagnosisandtreatment pages 22-23)
- Immunosuppressants: Infection risk, hepatotoxicity, bone marrow suppression

### Treatment Strategy
**No Standard Protocol**: "Currently, there is no standard treatment protocol for AIRs" (kalogeropoulos2025diagnosisandtreatment pages 20-22). Management is individualized based on:
- Subtype (CAR, MAR, npAIR)
- Presence of underlying malignancy
- Disease severity and progression
- Response to initial therapy

**Typical Approach**:
1. In pAIR: Address malignancy first (surgery, chemotherapy, radiotherapy)
2. Initiate corticosteroids (systemic ± local)
3. Add steroid-sparing immunomodulators if needed
4. Consider biologics (especially rituximab) for refractory disease
5. Multidisciplinary care (ophthalmology, oncology, rheumatology)
(kalogeropoulos2025diagnosisandtreatment pages 20-22, kalogeropoulos2025diagnosisandtreatment pages 22-23)

**Need for RCTs**: "A prospective randomized placebo-controlled clinical trial could provide important insights on this topic" (kalogeropoulos2025diagnosisandtreatment pages 22-23).

## 13. Prevention

### Prevention Levels

**Primary Prevention**: No specific primary prevention strategies exist as AIR is an acquired autoimmune condition with unclear triggering factors.

**Secondary Prevention**:
- **Cancer Screening in pAIR**: Early detection of malignancy improves visual outcomes. "Early oncologic diagnosis (within 6 months after symptom onset) was significantly associated with a favorable visual outcome (p = 0.03)" in CAR (beuzit2025paraneoplasticocularsyndromes pages 1-2)
- **Monitoring High-Risk Populations**: Patients with known autoimmune diseases should be monitored for visual symptoms (kalogeropoulos2025diagnosisandtreatment pages 2-4)

**Tertiary Prevention**:
- Early immunosuppressive therapy to prevent further retinal damage
- Regular monitoring (ERG, OCT, visual fields) to detect progression
- Management of CME to prevent further vision loss

### Screening and Early Detection
**Cancer Screening**: Comprehensive oncological workup in all suspected pAIR cases, including:
- Imaging (CT chest/abdomen/pelvis, PET-CT)
- Tumor markers
- Dermatologic examination for melanoma
- Age/sex-appropriate cancer screening
(beuzit2025paraneoplasticocularsyndromes pages 1-2, kalogeropoulos2025diagnosisandtreatment pages 10-13)

**Genetic Screening**: Not applicable; AIR is not Mendelian inherited.

**Risk Stratification**: Patients with autoimmune disease history should be counseled about visual symptoms warranting ophthalmologic evaluation (kalogeropoulos2025diagnosisandtreatment pages 2-4).

### Counseling
**Genetic Counseling**: Not required; AIR is not inherited.

**Patient Education**: Importance of reporting visual symptoms; compliance with immunosuppression; cancer surveillance in pAIR.

### Public Health
No specific public health interventions applicable to this rare condition.

### Prophylaxis
No preventive medications or procedures recommended for at-risk individuals.

## 14. Other Species/Natural Disease

### Taxonomy and Natural Disease
No naturally occurring autoimmune retinopathy has been well-documented in non-human species in the reviewed literature.

### Comparative Biology
Not applicable due to lack of natural animal disease models.

## 15. Model Organisms

### Model Types

**Experimental Autoimmune Uveitis (EAU) Models**:
- **Mammalian Models**: Mice, rats, rabbits
- **Induction Methods**: Immunization with retinal antigens (recoverin, IRBP, retinal S-antigen)

**Specific Models**:

1. **Recoverin-Induced EAU in Rabbits**:
   - "Photoreceptor Ca2+/Zn2+-sensor protein recoverin is a uveoretinal antigen in albino rabbits provoking typical autoimmune chorioretinitis 2–4 weeks after immunization"
   - Features: Lymphocytic infiltration, Dalen-Fuchs nodules, retinal atrophy, decreased ERG a-wave amplitude, retinal vascular changes, subretinal hemorrhages
   - Biochemical changes: Increased TNF-α and IL-6, decreased IL-10, decreased antioxidant activity
   - Metabolomic/lipidomic changes: High lactate, low ascorbic acid, increased PGE2, TXB2, 11-HETE, Lyso-PAF
   (kalogeropoulos2025diagnosisandtreatment pages 20-22)

2. **IRBP-Induced EAU in Mice**:
   - Chronic progressive model showing sustained disease up to 28 weeks
   - Used to test therapeutic interventions (kalogeropoulos2025diagnosisandtreatment pages 20-22)

3. **ROS-Deficient (Ncf1−/−) Mice**:
   - "ROS-deficient (Ncf1−/−) mice... EAU disease scores of Ncf1−/− mice were significantly lower than those of wild-type mice"
   - Demonstrates role of oxidative stress in pathogenesis

### Model Characteristics

**Phenotype Recapitulation**:
- Retinal inflammation
- Photoreceptor dysfunction (ERG abnormalities)
- Immune cell infiltration
- Cytokine/chemokine elevation
- Retinal structural damage

**Model Limitations**:
- Does not fully replicate human AIR heterogeneity
- Antibody-mediated mechanisms less studied than T-cell mechanisms in EAU
- Acute/subacute models may not reflect chronic human disease course

### Applications
- Testing immunomodulatory therapies
- Understanding inflammatory and oxidative stress mechanisms
- Evaluating antioxidant interventions
- Characterizing cellular and molecular pathways

**Example**: "Application of mitochondria-targeted antioxidant therapy impeded EAU progression by maintaining local antioxidant activity and suppressing TNF-α, IL-6 and PGE2 signaling" (kalogeropoulos2025diagnosisandtreatment pages 20-22).

### Resources
Model organism databases: MGI (Mouse Genome Informatics), RGD (Rat Genome Database) for accessing EAU models.

---

## Summary and Current Gaps

Autoimmune retinopathy remains an enigmatic and challenging condition. Despite decades of research, several critical gaps persist:

1. **Diagnostic Standardization**: "There is currently no international consensus on diagnostic criteria or treatment protocols" (kalogeropoulos2025diagnosisandtreatment pages 1-2, kalogeropoulos2025diagnosisandtreatment pages 20-22)

2. **Pathogenic Role of Antibodies**: "It is still unclear whether the presence of antibodies serves as a causative factor or arises as a consequential outcome" (kalogeropoulos2025diagnosisandtreatment pages 1-2)

3. **Treatment Evidence**: Evidence base dominated by retrospective case series; "prospective randomized placebo-controlled clinical trials are explicitly needed" (kalogeropoulos2025diagnosisandtreatment pages 20-22, kalogeropoulos2025diagnosisandtreatment pages 22-23)

4. **Epidemiology**: No population-based prevalence/incidence data available

5. **Predictive Biomarkers**: Limited validated biomarkers for prognosis and treatment response

Future research should focus on prospective clinical trials, standardized diagnostic criteria, identification of pathogenic versus bystander antibodies, and development of targeted immunotherapies based on mechanistic understanding of antibody-mediated retinal damage.

References

1. (kalogeropoulos2025diagnosisandtreatment pages 1-2): Dimitrios Kalogeropoulos, Andrew John Lotery, Carlos Pavesio, Chris Kalogeropoulos, Panagiotis Kanavaros, Farid Afshar, Fatima Shawkat, and Gabriella De Salvo. Diagnosis and treatment of autoimmune retinopathy: review of current approaches. International ophthalmology, 45 1:341, Aug 2025. URL: https://doi.org/10.1007/s10792-025-03696-y, doi:10.1007/s10792-025-03696-y. This article has 7 citations and is from a peer-reviewed journal.

2. (kalogeropoulos2025diagnosisandtreatment pages 2-4): Dimitrios Kalogeropoulos, Andrew John Lotery, Carlos Pavesio, Chris Kalogeropoulos, Panagiotis Kanavaros, Farid Afshar, Fatima Shawkat, and Gabriella De Salvo. Diagnosis and treatment of autoimmune retinopathy: review of current approaches. International ophthalmology, 45 1:341, Aug 2025. URL: https://doi.org/10.1007/s10792-025-03696-y, doi:10.1007/s10792-025-03696-y. This article has 7 citations and is from a peer-reviewed journal.

3. (kalogeropoulos2025diagnosisandtreatment pages 20-22): Dimitrios Kalogeropoulos, Andrew John Lotery, Carlos Pavesio, Chris Kalogeropoulos, Panagiotis Kanavaros, Farid Afshar, Fatima Shawkat, and Gabriella De Salvo. Diagnosis and treatment of autoimmune retinopathy: review of current approaches. International ophthalmology, 45 1:341, Aug 2025. URL: https://doi.org/10.1007/s10792-025-03696-y, doi:10.1007/s10792-025-03696-y. This article has 7 citations and is from a peer-reviewed journal.

4. (beuzit2025paraneoplasticocularsyndromes pages 1-2): Solweig Beuzit, Aude Méal, Mathieu Delplanque, Jean-Christophe Ianotto, Béatrice Cochener-Lamard, Claire de Moreuil, and Bénédicte Rouvière. Paraneoplastic ocular syndromes: a systematic review of epidemiology, diagnosis and outcomes (2010–2023). Journal of Ophthalmic Inflammation and Infection, Sep 2025. URL: https://doi.org/10.1186/s12348-025-00534-1, doi:10.1186/s12348-025-00534-1. This article has 3 citations and is from a peer-reviewed journal.

5. (chen2025autoimmuneretinopathyin pages 1-2): Yiqiao Chen, Yexin Zhang, Jiaojiao Luo, Miaomiao Liu, Min Lin, Wenhua Zhu, Wenjun Xiong, Peiquan Zhao, Jianying Xi, and P. Fei. Autoimmune retinopathy in patients with myasthenia gravis: cases series and literature review. BMC Ophthalmology, Sep 2025. URL: https://doi.org/10.1186/s12886-025-04357-5, doi:10.1186/s12886-025-04357-5. This article has 0 citations and is from a peer-reviewed journal.

6. (kalogeropoulos2025diagnosisandtreatment pages 4-5): Dimitrios Kalogeropoulos, Andrew John Lotery, Carlos Pavesio, Chris Kalogeropoulos, Panagiotis Kanavaros, Farid Afshar, Fatima Shawkat, and Gabriella De Salvo. Diagnosis and treatment of autoimmune retinopathy: review of current approaches. International ophthalmology, 45 1:341, Aug 2025. URL: https://doi.org/10.1007/s10792-025-03696-y, doi:10.1007/s10792-025-03696-y. This article has 7 citations and is from a peer-reviewed journal.

7. (kalogeropoulos2025diagnosisandtreatment pages 5-7): Dimitrios Kalogeropoulos, Andrew John Lotery, Carlos Pavesio, Chris Kalogeropoulos, Panagiotis Kanavaros, Farid Afshar, Fatima Shawkat, and Gabriella De Salvo. Diagnosis and treatment of autoimmune retinopathy: review of current approaches. International ophthalmology, 45 1:341, Aug 2025. URL: https://doi.org/10.1007/s10792-025-03696-y, doi:10.1007/s10792-025-03696-y. This article has 7 citations and is from a peer-reviewed journal.

8. (kalogeropoulos2025diagnosisandtreatment pages 9-10): Dimitrios Kalogeropoulos, Andrew John Lotery, Carlos Pavesio, Chris Kalogeropoulos, Panagiotis Kanavaros, Farid Afshar, Fatima Shawkat, and Gabriella De Salvo. Diagnosis and treatment of autoimmune retinopathy: review of current approaches. International ophthalmology, 45 1:341, Aug 2025. URL: https://doi.org/10.1007/s10792-025-03696-y, doi:10.1007/s10792-025-03696-y. This article has 7 citations and is from a peer-reviewed journal.

9. (kalogeropoulos2025diagnosisandtreatment pages 10-13): Dimitrios Kalogeropoulos, Andrew John Lotery, Carlos Pavesio, Chris Kalogeropoulos, Panagiotis Kanavaros, Farid Afshar, Fatima Shawkat, and Gabriella De Salvo. Diagnosis and treatment of autoimmune retinopathy: review of current approaches. International ophthalmology, 45 1:341, Aug 2025. URL: https://doi.org/10.1007/s10792-025-03696-y, doi:10.1007/s10792-025-03696-y. This article has 7 citations and is from a peer-reviewed journal.

10. (chen2025autoimmuneretinopathyin pages 3-4): Yiqiao Chen, Yexin Zhang, Jiaojiao Luo, Miaomiao Liu, Min Lin, Wenhua Zhu, Wenjun Xiong, Peiquan Zhao, Jianying Xi, and P. Fei. Autoimmune retinopathy in patients with myasthenia gravis: cases series and literature review. BMC Ophthalmology, Sep 2025. URL: https://doi.org/10.1186/s12886-025-04357-5, doi:10.1186/s12886-025-04357-5. This article has 0 citations and is from a peer-reviewed journal.

11. (kalogeropoulos2025diagnosisandtreatment pages 22-23): Dimitrios Kalogeropoulos, Andrew John Lotery, Carlos Pavesio, Chris Kalogeropoulos, Panagiotis Kanavaros, Farid Afshar, Fatima Shawkat, and Gabriella De Salvo. Diagnosis and treatment of autoimmune retinopathy: review of current approaches. International ophthalmology, 45 1:341, Aug 2025. URL: https://doi.org/10.1007/s10792-025-03696-y, doi:10.1007/s10792-025-03696-y. This article has 7 citations and is from a peer-reviewed journal.

12. (kalogeropoulos2025diagnosisandtreatment pages 7-8): Dimitrios Kalogeropoulos, Andrew John Lotery, Carlos Pavesio, Chris Kalogeropoulos, Panagiotis Kanavaros, Farid Afshar, Fatima Shawkat, and Gabriella De Salvo. Diagnosis and treatment of autoimmune retinopathy: review of current approaches. International ophthalmology, 45 1:341, Aug 2025. URL: https://doi.org/10.1007/s10792-025-03696-y, doi:10.1007/s10792-025-03696-y. This article has 7 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Autoimmune_Retinopathy-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Autoimmune_Retinopathy-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](Autoimmune_Retinopathy-deep-research-falcon_artifacts/artifact-02.md)