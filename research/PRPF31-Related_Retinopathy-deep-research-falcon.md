---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-13T19:43:00.602076'
end_time: '2026-07-13T19:55:52.607751'
duration_seconds: 772.01
template_file: templates\disease_pathophysiology_research.md
template_variables:
  disease_name: PRPF31-Related Retinopathy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 27
artifact_count: 3
artifact_sources:
  edison_answer_artifacts: 3
artifacts:
- filename: artifact-00.md
  path: PRPF31-Related_Retinopathy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: PRPF31-Related_Retinopathy-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: PRPF31-Related_Retinopathy-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PRPF31-Related Retinopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PRPF31-Related Retinopathy** covering all of the
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
- **Disease Name:** PRPF31-Related Retinopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PRPF31-Related Retinopathy** covering all of the
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


# PRPF31-Related Retinopathy (Retinitis Pigmentosa 11, RP11): Disease Characteristics Research Report

## Executive summary
PRPF31-related retinopathy (commonly referred to as **retinitis pigmentosa 11; RP11**) is a **Mendelian autosomal-dominant inherited retinal dystrophy** caused by heterozygous pathogenic variants in **PRPF31**, a core spliceosomal tri-snRNP component. A defining clinical/genetic hallmark is **incomplete penetrance**: some variant carriers remain asymptomatic, strongly associated with **higher expression of the remaining wild-type PRPF31 allele** (haploinsufficiency threshold model). Disease typically follows a **rod-first degeneration** pattern with nyctalopia and peripheral field loss followed by cone involvement and reduced central vision. Multiple therapeutic strategies are under active development, including **intravitreal VP-001** (interventional clinical trials) and preclinical **AAV gene augmentation**, **splice-switching ASOs**, and supportive approaches such as **autophagy activation**. (rose2016varianthaploinsufficiencyand pages 1-2, grainok2024aprecisiontherapy pages 2-4, rodrigues2022modelingprpf31retinitis pages 1-2, NCT05902962 chunk 1)

---

## 1. Disease information
### 1.1 What is the disease?
PRPF31-related retinopathy is a **non-syndromic retinitis pigmentosa** caused by PRPF31 mutations, characterized by progressive retinal degeneration that begins with rod dysfunction (nyctalopia/night blindness and peripheral visual field constriction) and progresses to cone involvement with loss of central vision in later stages. (rose2016varianthaploinsufficiencyand pages 1-2, rodrigues2022modelingprpf31retinitis pages 1-2)

A mechanistic feature emphasized in patient-derived retinal models is that PRPF31 mutation causes **retina-specific disruption of alternative splicing programs**, including mis-splicing of genes involved in splicing itself and in ciliogenesis/adhesion, producing RPE and photoreceptor dysfunction despite ubiquitous PRPF31 expression. (buskin2018disruptedalternativesplicing pages 1-2, rodrigues2022modelingprpf31retinitis pages 1-2)

### 1.2 Key identifiers (OMIM, Orphanet, ICD, MeSH, MONDO)
The retrieved primary papers and clinical trial records consistently use the disease names **“PRPF31-associated retinitis pigmentosa,” “retinitis pigmentosa 11 (RP11),”** and **“PRPF31 mutation-associated retinal dystrophy.”** (grainok2024aprecisiontherapy pages 2-4, NCT05902962 chunk 1, NCT05573984 chunk 1)

**Limitation:** OMIM/Orphanet/ICD/MeSH/MONDO identifiers were not present in the available full-text snippets or ClinicalTrials.gov chunks retrieved here, so they cannot be asserted from this evidence set.

### 1.3 Synonyms / alternative names
Synonyms used across sources include:
- Retinitis pigmentosa 11 (RP11) (grainok2024aprecisiontherapy pages 2-4)
- PRPF31-associated retinitis pigmentosa (NCT06368375 chunk 1)
- PRPF31 mutation-associated retinal dystrophy (NCT05902962 chunk 1)

### 1.4 Evidence sources: aggregated vs individual
Evidence in this report comes from:
- **Primary experimental disease-model and mechanistic studies** (human iPSC-derived retinal organoids/RPE; mouse CRISPR/AAV models). (buskin2018disruptedalternativesplicing pages 1-2, georgiou2022activationofautophagy pages 1-3, xi2022geneaugmentationprevents pages 1-2)
- **Clinical/review synthesis and treatment landscape** sources (autosomal-dominant IRD treatment review). (varela2023genetictreatmentfor pages 6-9)
- **ClinicalTrials.gov registry records** for ongoing/completed observational and interventional studies. (NCT05902962 chunk 1, NCT05573984 chunk 1, NCT06368375 chunk 1)

| Disease name | Common synonyms | Inheritance | Causal gene | Key distinguishing features | Key sources (year; URL/DOI) |
|---|---|---|---|---|---|
| PRPF31-related retinopathy | Retinitis pigmentosa 11 (RP11); PRPF31-associated retinitis pigmentosa; PRPF31-associated autosomal dominant retinitis pigmentosa (PRPF31-associated adRP) | Autosomal dominant with incomplete/non-penetrance and variable expressivity (rose2016varianthaploinsufficiencyand pages 1-2, varela2023genetictreatmentfor pages 6-9, rodrigues2022modelingprpf31retinitis pages 1-2) | **PRPF31** (pre-mRNA processing factor 31), a core spliceosomal/tri-snRNP component (buskin2018disruptedalternativesplicing pages 1-2, georgiou2022activationofautophagy pages 1-3) | Retina-predominant degeneration despite ubiquitous gene expression; typical rod-first disease with nyctalopia/night blindness, progressive visual-field constriction, then secondary cone/central vision loss; hallmark **incomplete penetrance linked to PRPF31 expression level/haploinsufficiency**; low wild-type PRPF31 expression associates with disease, while higher expression can permit asymptomatic carrier status (rose2016varianthaploinsufficiencyand pages 1-2, grainok2024aprecisiontherapy pages 2-4, varela2023genetictreatmentfor pages 6-9, rodrigues2022modelingprpf31retinitis pages 1-2) | Buskin et al. 2018; https://doi.org/10.1038/s41467-018-06448-y (buskin2018disruptedalternativesplicing pages 1-2). Rose & Bhattacharya 2016; https://doi.org/10.1111/cge.12758 (rose2016varianthaploinsufficiencyand pages 1-2). Rodrigues et al. 2022; https://doi.org/10.1038/s41536-022-00235-6 (rodrigues2022modelingprpf31retinitis pages 1-2). Grainok et al. 2024; https://doi.org/10.3390/ijms25063391 (grainok2024aprecisiontherapy pages 2-4). Georgiou et al. 2022; https://doi.org/10.1002/ctm2.759 (georgiou2022activationofautophagy pages 1-3). Varela et al. 2023; https://doi.org/10.1136/bjo-2022-321903 (varela2023genetictreatmentfor pages 6-9) |
| Expression-penetrance note | Non-penetrant PRPF31 carriers; asymptomatic carriers | Same AD family transmission, but some heterozygous carriers remain unaffected (rose2016varianthaploinsufficiencyand pages 1-2, rodrigues2022modelingprpf31retinitis pages 1-2) | **PRPF31** | Example quantitative support: a truncating PRPF31 exon 12 variant showed ~46% reduced PRPF31 mRNA in affected fibroblasts versus controls, compared with ~34% reduction in a non-penetrant carrier; ASO-induced exon skipping increased PRPF31 mRNA ~1.7-fold toward a predicted therapeutic threshold (grainok2024aprecisiontherapy pages 2-4) | Grainok et al. 2024; https://doi.org/10.3390/ijms25063391 (grainok2024aprecisiontherapy pages 2-4). Lan et al. 2022; https://doi.org/10.3390/jcm11226682 (lan2022a69kb pages 9-12) |


*Table: This table summarizes core nomenclature, inheritance, causal gene, and the defining penetrance-related biology of PRPF31-related retinopathy. It is useful as a compact disease-identity reference for a knowledge base entry.*

---

## 2. Etiology
### 2.1 Disease causal factors
**Primary cause:** heterozygous pathogenic variants in **PRPF31** causing autosomal-dominant RP11. (rose2016varianthaploinsufficiencyand pages 1-2, rodrigues2022modelingprpf31retinitis pages 1-2)

**Molecular etiology (current understanding):** PRPF31 encodes a **core spliceosomal tri-snRNP** component; pathogenic variants commonly lead to **loss-of-function and reduced effective PRPF31 activity**, producing disrupted splicing programs in retinal cells. (buskin2018disruptedalternativesplicing pages 1-2, georgiou2022activationofautophagy pages 1-3)

### 2.2 Risk factors
- **Genetic:** carrying a PRPF31 pathogenic variant is the principal risk factor. (rose2016varianthaploinsufficiencyand pages 1-2)
- **Modifier/contextual genetic effects:** incomplete penetrance and variable expressivity are linked to **PRPF31 expression variability** and potential modifier loci; a proposed association with a **4-copy MSR1 repeat** has been discussed in the autosomal-dominant IRD treatment review. (varela2023genetictreatmentfor pages 6-9)

A large-deletion pedigree study reports differential PRPF31 expression among carriers and notes potential cooperative effects of other differentially expressed genes; it also highlights incomplete penetrance as a key family feature. (lan2022a69kb pages 9-12)

### 2.3 Protective factors
A practical “protective” factor in this disease is **higher expression of PRPF31** from the remaining normal allele, which can allow **asymptomatic carrier status** (non-penetrance). (grainok2024aprecisiontherapy pages 2-4, rodrigues2022modelingprpf31retinitis pages 1-2)

### 2.4 Gene–environment interactions
No specific environmental triggers or gene–environment interactions were identified in the retrieved evidence.

---

## 3. Phenotypes
Core clinical features include:
- **Nyctalopia/night blindness** and **progressive visual field constriction** as early manifestations (rod dysfunction/degeneration). (rose2016varianthaploinsufficiencyand pages 1-2)
- **Secondary cone degeneration** leading to central vision impairment later in disease. (rose2016varianthaploinsufficiencyand pages 1-2, rodrigues2022modelingprpf31retinitis pages 1-2)

Disease-course variability is notable; one review reports **age of onset variability from ~6 to 71 years**. (varela2023genetictreatmentfor pages 6-9)

A large PRPF31 deletion pedigree described very early onset (night blindness around age 3 in affected individuals) in that family, underscoring variable expressivity. (lan2022a69kb pages 9-12)

### HPO mappings
| Phenotype / clinical feature | Phenotype type | Suggested HPO term(s) | Typical onset / progression notes | Frequency / remarks | Supporting citations |
|---|---|---|---|---|---|
| Night blindness | Symptom | HP:0000662 Nyctalopia | Often an early manifestation due to primary rod dysfunction/degeneration; may begin in childhood or early adulthood, but onset is variable across families | Core RP11 feature repeatedly described in PRPF31-associated disease | (lan2022a69kb pages 9-12, rose2016varianthaploinsufficiencyand pages 1-2, rodrigues2022modelingprpf31retinitis pages 1-2) |
| Peripheral visual field loss / constriction | Clinical sign / symptom | HP:0001133 Constricted visual fields | Progressive over years to decades, usually following early rod involvement; kinetic visual field shows ongoing decline | One of the hallmark functional deficits in RP11 | (rose2016varianthaploinsufficiencyand pages 1-2, varela2023genetictreatmentfor pages 6-9) |
| Rod photoreceptor degeneration | Pathophysiologic/structural manifestation | HP:0000510 Rod-cone dystrophy; HP:0000548 Retinal degeneration | Rods are affected first, with degeneration beginning in the mid-peripheral retina and progressing centrally | Canonical disease pattern in PRPF31-RP11 | (buskin2018disruptedalternativesplicing pages 1-2, rodrigues2022modelingprpf31retinitis pages 1-2) |
| Secondary cone degeneration / central vision decline | Clinical sign / structural manifestation | HP:0000546 Blindness; HP:0001123 Visual field defect | Typically later than rod loss; progressive cone involvement contributes to reduced central acuity and disability in advanced disease | Represents later-stage disease burden | (rose2016varianthaploinsufficiencyand pages 1-2, rodrigues2022modelingprpf31retinitis pages 1-2) |
| Reduced visual acuity | Clinical sign | HP:0007663 Reduced visual acuity | Usually later-onset than nyctalopia/field loss; worsens progressively with cone and macular involvement | Common outcome measure in natural history and interventional studies | (buskin2018disruptedalternativesplicing pages 1-2, NCT05573984 chunk 1, NCT06368375 chunk 1) |
| Abnormal electroretinogram | Electrophysiology abnormality | HP:0001311 Abnormal electroretinogram | Progressive reduction in rod and cone responses; cone ERG decline has been described longitudinally | Used routinely in PRPF31 natural history/phenotyping studies | (varela2023genetictreatmentfor pages 6-9, NCT05573984 chunk 1, NCT06368375 chunk 1) |
| Retinal pigment epithelium dysfunction | Cellular / tissue manifestation | HP:0000556 Abnormality of the retinal pigment epithelium | Progressive; modeled in iPSC-RPE with impaired polarity, barrier function, phagocytosis, and cellular stress | May be a major early disease site in PRPF31-RP11 | (buskin2018disruptedalternativesplicing pages 1-2, rodrigues2022modelingprpf31retinitis pages 1-2, georgiou2022activationofautophagy pages 1-3) |
| Ciliary abnormalities in retinal cells | Cellular manifestation | HP:0100542 Abnormality of ciliogenesis | Linked to mis-splicing of ciliogenesis genes; associated with progressive photoreceptor/RPE dysfunction | Supports classification of PRPF31-RP as partly ciliopathy-like | (buskin2018disruptedalternativesplicing pages 1-2, varela2023genetictreatmentfor pages 6-9) |
| Retinal degeneration with variable age at onset | Disease course characteristic | HP:0000510 Rod-cone dystrophy; HP:0003674 Onset variability | Age at onset is highly variable, reported from about 6 to 71 years in review literature; progression is chronic and typically lifelong | Marked intra- and interfamilial variability is characteristic | (varela2023genetictreatmentfor pages 6-9, rose2016varianthaploinsufficiencyand pages 1-2) |
| Incomplete penetrance / asymptomatic carrier state | Inheritance / expressivity feature | HP:0003829 Incomplete penetrance | Some heterozygous carriers remain clinically unaffected, likely because higher wild-type PRPF31 expression remains above a disease threshold | Distinguishing hallmark of PRPF31-RP11 | (rose2016varianthaploinsufficiencyand pages 1-2, grainok2024aprecisiontherapy pages 2-4, rodrigues2022modelingprpf31retinitis pages 1-2) |
| Early-onset severe phenotype in some families | Course severity feature | HP:0003581 Childhood onset | Although many cases are later-onset, certain pedigrees show unusually early disease, including childhood nyctalopia and rapid structural change | Highlights variable expressivity and possible modifier effects | (lan2022a69kb pages 9-12) |


*Table: This table summarizes the main clinical features reported for PRPF31-related retinopathy (RP11), with suggested HPO mappings and notes on onset and progression. It is useful for structuring phenotype annotations in a disease knowledge base.*

Quality-of-life impacts are not directly quantified in the retrieved primary papers, but ClinicalTrials.gov natural history protocols include validated **patient-reported outcome instruments** (e.g., MRDQ, PGI-S, PGI-C), indicating recognized functional burden. (NCT05573984 chunk 1, NCT05573984a chunk 1)

---

## 4. Genetic / molecular information
### 4.1 Causal gene
- **Gene:** PRPF31 (pre-mRNA processing factor 31), spliceosome/tri-snRNP component. (buskin2018disruptedalternativesplicing pages 1-2, georgiou2022activationofautophagy pages 1-3)
- **Inheritance:** autosomal dominant, with incomplete penetrance. (rose2016varianthaploinsufficiencyand pages 1-2, rodrigues2022modelingprpf31retinitis pages 1-2)

### 4.2 Pathogenic variants and functional consequence
Multiple classes of PRPF31 variants are implicated (nonsense/truncating, deletions, etc.), generally consistent with **loss-of-function/haploinsufficiency**. (lan2022a69kb pages 9-12, grainok2024aprecisiontherapy pages 2-4, rodrigues2022modelingprpf31retinitis pages 1-2)

**Quantitative penetrance–expression link (example):** In a family with PRPF31 c.1205C>A (nonsense) variant, PRPF31 transcripts from the mutant allele were undetectable (consistent with nonsense-mediated decay), producing an observed **46% reduction** in PRPF31 mRNA versus controls in patient fibroblasts; a non-penetrant carrier with the same variant had a smaller reduction (~**34%**). (grainok2024aprecisiontherapy pages 2-4)

### 4.3 Modifier genes / modifiers of penetrance
- Review-level evidence notes association of non-penetrance with an **MSR1 repeat copy number** (4-copy MSR1 repeat). (varela2023genetictreatmentfor pages 6-9)
- A large-deletion pedigree study mentions expression variation and suggests cooperative effects of other genes, and notes modifiers (e.g., CNOT3 and MSR1) in discussion of penetrance variability. (lan2022a69kb pages 9-12)

### 4.4 Epigenetics and chromosomal abnormalities
A 69 kb deletion encompassing PRPF31 exon 1 and upstream genes is described in a large family; the deletion breakpoints are within Alu repeats, consistent with structural-variant mechanisms. (lan2022a69kb pages 9-12)

No specific DNA methylation/histone findings were available in the retrieved evidence.

---

## 5. Environmental information
No environmental, lifestyle, or infectious contributors were identified in the retrieved evidence. The disease is primarily genetic. (rose2016varianthaploinsufficiencyand pages 1-2, rodrigues2022modelingprpf31retinitis pages 1-2)

---

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (current model)
1. **Heterozygous PRPF31 loss-of-function** reduces effective PRPF31 availability (haploinsufficiency) in susceptible retinal cell types. (rodrigues2022modelingprpf31retinitis pages 1-2, georgiou2022activationofautophagy pages 1-3)
2. Retinal cells exhibit **disrupted alternative splicing programs**, including mis-splicing of genes involved in splicing and **ciliogenesis/cell adhesion**. (buskin2018disruptedalternativesplicing pages 1-2)
3. **RPE defects** occur, including disrupted apical–basal polarity, decreased barrier function (reduced transepithelial resistance), impaired phagocytosis, and ciliary abnormalities; photoreceptors show progressive degeneration and cellular stress. (buskin2018disruptedalternativesplicing pages 1-2)
4. In severe PRPF31-adRP iPSC-derived retinal/RPE models, mutant PRPF31 and other proteins accumulate as **cytoplasmic aggregates**, with associated defects in tri-snRNP assembly, altered nuclear speckles, reduced active spliceosome formation, and global splicing dysregulation; impaired waste disposal (autophagy/lysosome, proteostasis) exacerbates degeneration. (georgiou2022activationofautophagy pages 1-3)

### 6.2 Pathways / processes (ontology suggestions)
**GO Biological Process (suggested):**
- mRNA splicing via spliceosome
- cilium organization / ciliogenesis
- autophagy
- unfolded protein response
- phagocytosis
(grounded in observed splicing dysregulation, ciliary defects, aggregate clearance, and RPE phagocytic deficits) (buskin2018disruptedalternativesplicing pages 1-2, georgiou2022activationofautophagy pages 1-3)

**Cell types (CL terms; suggested):**
- Retinal pigment epithelial cell (RPE)
- Rod photoreceptor cell
- Cone photoreceptor cell
(central affected cell populations across iPSC and mouse studies) (buskin2018disruptedalternativesplicing pages 1-2, rodrigues2022modelingprpf31retinitis pages 1-2)

**Tissue/structure (UBERON; suggested):**
- Retina
- Retinal pigment epithelium
- Photoreceptor layer / outer nuclear layer
(paired with OCT/structural thinning described in mouse model) (xi2022geneaugmentationprevents pages 3-4)

### 6.3 Expert opinions / authoritative analyses
A 2023 British Journal of Ophthalmology review on autosomal-dominant IRD therapies emphasizes that dominant diseases such as PRPF31-associated adRP often require strategies beyond simple gene supplementation depending on mechanism, and highlights incomplete penetrance/variable expressivity and onset variability as key clinical considerations. (varela2023genetictreatmentfor pages 6-9)

### 6.4 Recent developments (2023–2024 prioritized)
- **Precision ASO splice-switching therapy (2024):** exon 12 skipping to restore an open reading frame for certain truncating variants, with quantified PRPF31 mRNA restoration toward a predicted therapeutic threshold (1.7-fold upregulation in patient fibroblasts). (grainok2024aprecisiontherapy pages 2-4)
- **Clinical translation via intravitreal investigational therapy VP-001** and dedicated multi-year natural history programs (initiated 2022; phase 1 trials initiated 2023/2024). (NCT05902962 chunk 1, NCT05573984 chunk 1)

**Direct abstract quote examples (for knowledge base evidence items):**
- Grainok et al. 2024: “Retinitis pigmentosa 11 is an untreatable, dominantly inherited retinal disease caused by heterozygous mutations in pre-mRNA processing factor 31 PRPF31. The expression level of PRPF31 is linked to incomplete penetrance in affected families; mutation carriers with higher PRPF31 expression can remain asymptomatic.” (grainok2024aprecisiontherapy pages 2-4)
- Buskin et al. 2018: “Mis-splicing of genes implicated in ciliogenesis and cellular adhesion was associated with severe RPE defects…” (buskin2018disruptedalternativesplicing pages 1-2)
- Xi et al. 2022: “AAV-mediated PRPF31 gene augmentation restored the retinal structure and function…” (xi2022geneaugmentationprevents pages 1-2)

---

## 7. Anatomical structures affected
- **Primary:** retina and retinal pigment epithelium (RPE). (buskin2018disruptedalternativesplicing pages 1-2, rodrigues2022modelingprpf31retinitis pages 1-2)
- **Layer-level:** outer retina including photoreceptor inner/outer segments and outer nuclear layer; thinning and loss are described in a Prpf31 KO mouse model. (xi2022geneaugmentationprevents pages 3-4)

---

## 8. Temporal development
- **Onset:** variable; review-level synthesis notes ~6–71 years, but some families show much earlier onset (e.g., childhood nyctalopia reported in one large deletion pedigree). (varela2023genetictreatmentfor pages 6-9, lan2022a69kb pages 9-12)
- **Progression:** chronic progressive degeneration with rod-first then cone involvement; consistent recapitulation of rod death followed by cone loss in retinal organoid models. (rodrigues2022modelingprpf31retinitis pages 1-2)

---

## 9. Inheritance and population
- **Inheritance:** autosomal dominant with incomplete penetrance / asymptomatic carriers common. (rose2016varianthaploinsufficiencyand pages 1-2, rodrigues2022modelingprpf31retinitis pages 1-2)
- **Population/epidemiology:** RP prevalence is reported as approximately **1 in 2500 births** and affecting “over 1 million people worldwide” in a foundational mechanistic paper; PRPF31 contributes a substantial subset of autosomal dominant RP. (buskin2018disruptedalternativesplicing pages 1-2)

Attribution estimates for PRPF31 among adRP vary by cohort and source: e.g., 5–8% of adRP cohorts (Rodrigues 2022) and 6–11.1% in another summary within a PRPF31 mouse model paper. (rodrigues2022modelingprpf31retinitis pages 1-2, xi2022geneaugmentationprevents pages 1-2)

---

## 10. Diagnostics
### 10.1 Clinical tests used in practice/research settings
Clinical phenotyping and monitoring in PRPF31 cohorts commonly uses:
- **BCVA** (ETDRS), **low luminance VA** (NCT05902962 chunk 1, NCT05573984 chunk 1)
- **Visual fields** (kinetic/static perimetry) (NCT06455826 chunk 1, NCT06368375 chunk 1)
- **SD-OCT** (retinal thickness; ellipsoid zone measures in natural history study) (NCT05573984 chunk 1)
- **Microperimetry** (retinal sensitivity) (NCT05902962 chunk 1, NCT05573984 chunk 1)
- **Full-field ERG** (NCT06368375 chunk 1)
- **Fundus photography** and **fundus autofluorescence**; ultra-widefield imaging is used in at least one cohort. (NCT06368375 chunk 1)

### 10.2 Genetic testing
ClinicalTrials.gov protocols require **genetic confirmation of PRPF31 mutation** for study inclusion in both observational and interventional programs, reflecting real-world use of genetic testing for diagnosis and trial eligibility. (NCT05902962 chunk 1, NCT05573984 chunk 1)

### 10.3 Differential diagnosis
Not directly enumerated in retrieved evidence; clinically, differential diagnosis would include other causes of autosomal dominant retinitis pigmentosa (e.g., RHO, RP1, other splicing-factor genes), but explicit differential lists were not in the retrieved sources.

---

## 11. Outcome / prognosis
The disease is progressive and can lead to severe visual disability. Longitudinal natural history protocols include structural (ellipsoid zone area/volume), electrophysiology, and mobility testing endpoints, reflecting clinically meaningful progression assessment. (NCT05573984 chunk 1, NCT05573984a chunk 1)

Mortality is not discussed and is not expected to be directly affected in non-syndromic RP11; no mortality data were present in retrieved evidence.

---

## 12. Treatment
### 12.1 Current standard care
No curative standard therapy is described in the retrieved evidence; management is centered on monitoring and supportive care, while disease-modifying therapies are investigational. (varela2023genetictreatmentfor pages 6-9)

### 12.2 Advanced therapeutics and experimental treatments (2023–2024 emphasis)
- **Intravitreal VP-001 clinical trials (PYC Therapeutics):**
  - Phase 1 SAD dose escalation (NCT05902962; started 2023-04-20; n=17). (NCT05902962 chunk 1)
  - Phase 1 MAD repeat-dose escalation (NCT06455826; started 2024-06-13; completed 2025-09-24; n=6; 30 μg and 75 μg; 3 injections 8 weeks apart). (NCT06455826a chunk 1, NCT06455826 chunk 1)
  - Repeat-dose safety/efficacy study listed (NCT06852963; Phase 1/2; n=17; details not available in retrieved chunk text). (NCT06455826a chunk 1)

- **Natural history studies supporting endpoint selection and trial readiness:** NCT05573984 (prospective, multi-center; started 2022-07-07; n=50; includes BCVA, LLVA, SD-OCT, ellipsoid zone metrics, microperimetry, ERG, FAF, mobility course, MRDQ, PGI scales). (NCT05573984 chunk 1, NCT05573984a chunk 1)

- **Preclinical PRPF31 gene augmentation:**
  - In a CRISPR/Cas9 AAV-induced Prpf31 KO mouse model, **AAV-mediated PRPF31 augmentation restored retinal structure and function**, supporting gene augmentation as a broadly applicable approach for haploinsufficiency. (xi2022geneaugmentationprevents pages 1-2)
  - In human iPSC-derived RPE and retinal organoids with PRPF31 mutations, **gene augmentation** and **CRISPR correction** rescued RPE and photoreceptor phenotypes. (rodrigues2022modelingprpf31retinitis pages 1-2)

- **Precision RNA therapy (ASO exon skipping; 2024):** exon 12 skipping increased PRPF31 mRNA **~1.7-fold** in patient fibroblasts and was proposed to meet a therapeutic expression threshold inferred from a non-penetrant carrier. (grainok2024aprecisiontherapy pages 2-4)

- **Supportive mechanistic therapy (autophagy activation):** rapamycin reduced aggregates and improved survival in patient-derived iPSC-RPE/retinal models, proposed as a combinable strategy with gene therapy. (georgiou2022activationofautophagy pages 1-3)

**MAXO (suggested) mappings:**
- Gene therapy / gene augmentation (e.g., AAV-mediated gene delivery)
- Antisense oligonucleotide therapy
- Intravitreal injection
- Supportive pharmacotherapy (autophagy induction)

| Strategy / study | Modality / intervention | Trial ID / evidence type | Phase / design | Enrollment | Dates | Key endpoints / findings | Supporting citations |
|---|---|---|---|---:|---|---|---|
| VP-001 single-ascending-dose study (“Platypus”) | Intravitreal VP-001 | NCT05902962 | Phase 1, open-label, single-arm dose-escalation | 17 | Started 2023-04-20; primary completion 2025-08-08 | Primary: incidence, severity, and relatedness of treatment-emergent ocular and serious adverse events over 24 and 48 weeks. Secondary/exploratory: fellow-eye and non-ocular adverse events; change in BCVA, low-luminance VA, visual field sensitivity, microperimetry, SD-OCT retinal thickness, ERG, autofluorescence, and patient-reported outcomes (PGI-C, PGI-S). (NCT05902962 chunk 1) | (NCT05902962 chunk 1) |
| VP-001 multiple-ascending-dose study (“Wallaby”) | Intravitreal VP-001, 3 repeat injections 8 weeks apart at 30 μg and 75 μg | NCT06455826 | Phase 1, open-label, multiple ascending dose | 6 | Started 2024-06-13; completed 2025-09-24 | Primary: safety/tolerability; incidence, severity, and relatedness of ocular and serious adverse events over 4-week and 52-week periods. Secondary: BCVA, low-luminance VA, kinetic/static perimetry, microperimetry, rod/cone-mediated function, SD-OCT retinal thickness, ffERG, fundus autofluorescence, fundus photography. (NCT06455826a chunk 1, NCT06455826 chunk 1) | (NCT06455826a chunk 1, NCT06455826 chunk 1) |
| VP-001 repeat-dose extension / efficacy study | Intravitreal VP-001 | NCT06852963 | Phase 1/2, open-label, two-arm safety and efficacy study | 17 | Active, not recruiting; detailed dates not available in retrieved context | Trial record indicates repeat-dose safety/efficacy evaluation in PRPF31 mutation-associated retinal dystrophy, including previously treated participants; detailed endpoint text not available in retrieved context. | (NCT06455826a chunk 1, NCT06455826 chunk 1) |
| PRPF31 natural history study (PYC) | No intervention; longitudinal phenotyping | NCT05573984 | Multi-center, prospective observational natural history study | 50 | Started 2022-07-07; estimated primary completion 2026-09-09; estimated final completion 2026-11-01 | Structural/functional progression measures: BCVA, LLVA, SD-OCT retinal thickness, ellipsoid zone area/volume, visual field sensitivity, macular sensitivity, fixation stability, full-field retinal sensitivity, ERG, fundus autofluorescence, mobility course, MRDQ, PGI-S, PGI-C. Visits every 16 weeks in year 1, then every 24 weeks. (NCT05573984 chunk 1, NCT05573984a chunk 1) | (NCT05573984 chunk 1, NCT05573984a chunk 1, NCT05573984a chunk 2, NCT05573984 chunk 2) |
| PRPF31 natural history study (Oslo) | No intervention; observational natural history | NCT04805658 | Observational | 30 | Active, not recruiting; dates/endpoints not available in retrieved context beyond title/registration summary | Registered natural history study of retinitis pigmentosa type 11; detailed endpoint text was not retrieved in the available context. | (NCT05573984 chunk 1) |
| PRPF31 clinical/genetic phenotyping cohort (Tübingen) | No intervention; retrospective cross-sectional characterization | NCT06368375 | Observational cohort, retrospective cross-sectional | 87 | Study period 2023-01-01 to 2023-06-30; source data from 2007-09 to 2022-01 | Primary goal: genotype–phenotype characterization in genetically confirmed PRPF31-associated inherited retinal dystrophy and asymptomatic carriers using BCVA, visual field testing, fundus photography, ultra-widefield imaging, FAF, OCT, and ffERG. (NCT06368375 chunk 1) | (NCT06368375 chunk 1) |
| AAV gene augmentation | AAV-mediated PRPF31 gene supplementation / augmentation | Preclinical mouse, retinal explant, iPSC-derived retinal models | Preclinical proof-of-concept | Not applicable | Key reports 2022 | In CRISPR/Cas9-based mouse models, AAV-mediated PRPF31 augmentation restored retinal structure and function; in human iPSC-derived RPE/organoids, gene augmentation rescued defective RPE and photoreceptor phenotypes, supporting translational development. (rodrigues2022modelingprpf31retinitis pages 1-2, buskin2018disruptedalternativesplicing pages 1-2) | (rodrigues2022modelingprpf31retinitis pages 1-2, buskin2018disruptedalternativesplicing pages 1-2) |
| Splice-switching antisense oligonucleotide exon skipping | ASO-mediated skipping of PRPF31 exon 12 to restore open reading frame | Preclinical cell-based precision therapy | Preclinical | Not applicable | 2024 report | In fibroblasts from a patient with PRPF31 c.1205C>A, mutant transcripts were undetectable because of NMD and total PRPF31 mRNA was reduced by 46% versus controls; ASO-induced exon 12 skipping increased PRPF31 mRNA 1.7-fold, reaching a predicted therapeutic threshold inferred from a non-penetrant carrier. (grainok2024aprecisiontherapy pages 2-4) | (grainok2024aprecisiontherapy pages 2-4) |
| Autophagy activation | Rapamycin to enhance autophagy and reduce aggregate burden | Preclinical iPSC-RPE / retinal organoid study | Preclinical | Not applicable | 2022 report | Rapamycin reduced progressive cytoplasmic aggregates containing mutant PRPF31 and ubiquitinated proteins and improved cell survival in patient-derived RPE, suggesting a combinable supportive strategy alongside gene therapy. (georgiou2022activationofautophagy pages 1-3) | (georgiou2022activationofautophagy pages 1-3) |


*Table: This table summarizes PRPF31-focused therapeutic development and clinical studies, including VP-001 interventional trials, observational natural history studies, and major preclinical strategies. It is useful for quickly comparing modality, development stage, enrollment, dates, and endpoints across the PRPF31-RP11 landscape.*

---

## 13. Prevention
Primary prevention is not currently feasible for a Mendelian autosomal dominant disease aside from reproductive options; the retrieved sources emphasize genetic diagnosis and natural history characterization rather than prevention interventions. (rose2016varianthaploinsufficiencyand pages 1-2, NCT05573984 chunk 1)

Secondary prevention in practice corresponds to early detection in at-risk relatives and longitudinal monitoring with structural/functional testing as used in natural history and clinical trial protocols. (NCT05573984 chunk 1, NCT06368375 chunk 1)

---

## 14. Other species / natural disease
No naturally occurring PRPF31-related retinopathy in non-human species was identified in the retrieved evidence.

---

## 15. Model organisms
### 15.1 In vitro human models
- **Patient-derived retinal organoids + RPE:** transcriptome profiling demonstrates retina-specific mis-splicing and RPE functional deficits, and gene editing can rescue key cellular phenotypes. (buskin2018disruptedalternativesplicing pages 1-2)
- **iPSC-RPE/retinal organoids:** recapitulate rod death followed by cone loss, with phenotypic rescue by gene augmentation and CRISPR correction; low PRPF31 expression correlates with disease phenotypes and is absent in asymptomatic carrier-derived cells. (rodrigues2022modelingprpf31retinitis pages 1-2)
- **Proteostasis/autophagy pathology in iPSC-derived RPE/retina:** aggregate accumulation and rapamycin responsiveness support autophagy involvement. (georgiou2022activationofautophagy pages 1-3)

### 15.2 In vivo animal models
- **AAV-CRISPR/Cas9-induced Prpf31 KO mouse:** achieves ~57% editing efficiency and produces progressive retinal degeneration with structural loss (IS/OS and ONL) and severely reduced ERG responses over weeks. (xi2022geneaugmentationprevents pages 3-4)
- **Gene augmentation in the mouse model:** AAV-mediated PRPF31 supplementation restored retinal structure and function (in vivo proof-of-concept). (xi2022geneaugmentationprevents pages 1-2)

---

## Data gaps and limitations of the current evidence set
- **Disease identifiers (OMIM/Orphanet/ICD/MeSH/MONDO)** and **PMIDs** were not available in the retrieved text snippets, so they cannot be provided as evidence-grounded fields here.
- Population-level **prevalence/incidence specifically for PRPF31-RP11** (as opposed to RP overall or PRPF31 share of adRP) was not retrieved.
- Detailed clinical guideline-based diagnostic algorithms and differential diagnosis lists were not present in retrieved sources.

---

## URLs and publication dates (selected key sources)
- Buskin et al., Nature Communications (2018-10). https://doi.org/10.1038/s41467-018-06448-y (buskin2018disruptedalternativesplicing pages 1-2)
- Rose & Bhattacharya, Clinical Genetics (2016-08). https://doi.org/10.1111/cge.12758 (rose2016varianthaploinsufficiencyand pages 1-2)
- Rodrigues et al., NPJ Regenerative Medicine (2022-08). https://doi.org/10.1038/s41536-022-00235-6 (rodrigues2022modelingprpf31retinitis pages 1-2)
- Georgiou et al., Clinical and Translational Medicine (2022-03). https://doi.org/10.1002/ctm2.759 (georgiou2022activationofautophagy pages 1-3)
- Xi et al., Nature Communications (2022-12). https://doi.org/10.1038/s41467-022-35361-8 (xi2022geneaugmentationprevents pages 1-2)
- Varela et al., British Journal of Ophthalmology (2023-08). https://doi.org/10.1136/bjo-2022-321903 (varela2023genetictreatmentfor pages 6-9)
- Grainok et al., International Journal of Molecular Sciences (2024-03). https://doi.org/10.3390/ijms25063391 (grainok2024aprecisiontherapy pages 2-4)
- ClinicalTrials.gov: NCT05902962 (2023; Platypus). https://clinicaltrials.gov/study/NCT05902962 (NCT05902962 chunk 1)
- ClinicalTrials.gov: NCT06455826 (2024; Wallaby). https://clinicaltrials.gov/study/NCT06455826 (NCT06455826a chunk 1)
- ClinicalTrials.gov: NCT05573984 (2022; natural history). https://clinicaltrials.gov/study/NCT05573984 (NCT05573984 chunk 1)
- ClinicalTrials.gov: NCT06368375 (2023; Tübingen phenotyping). https://clinicaltrials.gov/study/NCT06368375 (NCT06368375 chunk 1)


References

1. (rose2016varianthaploinsufficiencyand pages 1-2): A. M. Rose and Shomi S. Bhattacharya. Variant haploinsufficiency and phenotypic non‐penetrance in prpf31‐associated retinitis pigmentosa. Clinical Genetics, 90:118-126, Aug 2016. URL: https://doi.org/10.1111/cge.12758, doi:10.1111/cge.12758. This article has 86 citations and is from a peer-reviewed journal.

2. (grainok2024aprecisiontherapy pages 2-4): Janya Grainok, Ianthe L. Pitout, Fred K. Chen, Samuel McLenachan, Rachael C. Heath Jeffery, Chalermchai Mitrpant, and Sue Fletcher. A precision therapy approach for retinitis pigmentosa 11 using splice-switching antisense oligonucleotides to restore the open reading frame of prpf31. International Journal of Molecular Sciences, 25:3391, Mar 2024. URL: https://doi.org/10.3390/ijms25063391, doi:10.3390/ijms25063391. This article has 14 citations.

3. (rodrigues2022modelingprpf31retinitis pages 1-2): Amélie Rodrigues, Amélie Slembrouck-Brec, Céline Nanteau, Angélique Terray, Yelyzaveta Tymoshenko, Yvrick Zagar, Sacha Reichman, Zhouhuan Xi, José-Alain Sahel, Stéphane Fouquet, Gael Orieux, Emeline F. Nandrot, Leah C. Byrne, Isabelle Audo, Jérôme E. Roger, and Olivier Goureau. Modeling prpf31 retinitis pigmentosa using retinal pigment epithelium and organoids combined with gene augmentation rescue. NPJ Regenerative Medicine, Aug 2022. URL: https://doi.org/10.1038/s41536-022-00235-6, doi:10.1038/s41536-022-00235-6. This article has 71 citations and is from a peer-reviewed journal.

4. (NCT05902962 chunk 1):  SAD of IVT VP-001 in PRPF31 Mutation-Associated Retinal Dystrophy Subjects. PYC Therapeutics. 2023. ClinicalTrials.gov Identifier: NCT05902962

5. (buskin2018disruptedalternativesplicing pages 1-2): Adriana Buskin, Lili Zhu, Valeria Chichagova, Basudha Basu, Sina Mozaffari-Jovin, David Dolan, Alastair Droop, Joseph Collin, Revital Bronstein, Sudeep Mehrotra, Michael Farkas, Gerrit Hilgen, Kathryn White, Kuan-Ting Pan, Achim Treumann, Dean Hallam, Katarzyna Bialas, Git Chung, Carla Mellough, Yuchun Ding, Natalio Krasnogor, Stefan Przyborski, Simon Zwolinski, Jumana Al-Aama, Sameer Alharthi, Yaobo Xu, Gabrielle Wheway, Katarzyna Szymanska, Martin McKibbin, Chris F. Inglehearn, David J. Elliott, Susan Lindsay, Robin R. Ali, David H. Steel, Lyle Armstrong, Evelyne Sernagor, Henning Urlaub, Eric Pierce, Reinhard Lührmann, Sushma-Nagaraja Grellscheid, Colin A. Johnson, and Majlinda Lako. Disrupted alternative splicing for genes implicated in splicing and ciliogenesis causes prpf31 retinitis pigmentosa. Nature Communications, Oct 2018. URL: https://doi.org/10.1038/s41467-018-06448-y, doi:10.1038/s41467-018-06448-y. This article has 254 citations and is from a highest quality peer-reviewed journal.

6. (NCT05573984 chunk 1):  Natural History of PRPF31 Mutation-Associated Retinal Dystrophy. PYC Therapeutics. 2022. ClinicalTrials.gov Identifier: NCT05573984

7. (NCT06368375 chunk 1):  Clinical and Genetic Findings in Patients With PRPF31-associated Retinitis Pigmentosa. University Hospital Tuebingen. 2023. ClinicalTrials.gov Identifier: NCT06368375

8. (georgiou2022activationofautophagy pages 1-3): Maria Georgiou, Chunbo Yang, Robert Atkinson, Kuan‐Ting Pan, Adriana Buskin, Marina Moya Molina, Joseph Collin, Jumana Al‐Aama, Franziska Goertler, Sebastian E. J. Ludwig, Tracey Davey, Reinhard Lührmann, Sushma Nagaraja‐Grellscheid, Colin A. Johnson, Robin Ali, Lyle Armstrong, Viktor Korolchuk, Henning Urlaub, Sina Mozaffari‐Jovin, and Majlinda Lako. Activation of autophagy reverses progressive and deleterious protein aggregation in prpf31 patient‐induced pluripotent stem cell‐derived retinal pigment epithelium cells. Clinical and Translational Medicine, Mar 2022. URL: https://doi.org/10.1002/ctm2.759, doi:10.1002/ctm2.759. This article has 30 citations and is from a peer-reviewed journal.

9. (xi2022geneaugmentationprevents pages 1-2): Zhouhuan Xi, Abhishek Vats, José-Alain Sahel, Yuanyuan Chen, and Leah C. Byrne. Gene augmentation prevents retinal degeneration in a crispr/cas9-based mouse model of prpf31 retinitis pigmentosa. Nature Communications, Dec 2022. URL: https://doi.org/10.1038/s41467-022-35361-8, doi:10.1038/s41467-022-35361-8. This article has 42 citations and is from a highest quality peer-reviewed journal.

10. (varela2023genetictreatmentfor pages 6-9): Malena Daich Varela, Anastasios Georgiadis, and Michel Michaelides. Genetic treatment for autosomal dominant inherited retinal dystrophies: approaches, challenges and targeted genotypes. British Journal of Ophthalmology, 107:1223-1230, Aug 2023. URL: https://doi.org/10.1136/bjo-2022-321903, doi:10.1136/bjo-2022-321903. This article has 33 citations and is from a highest quality peer-reviewed journal.

11. (lan2022a69kb pages 9-12): Yuanzheng Lan, Yuhong Chen, Yunsheng Qiao, Qingdan Xu, Ruyi Zhai, Xinghuai Sun, Jihong Wu, and Xueli Chen. A 69 kb deletion in chr19q13.42 including prpf31 gene in a chinese family affected with autosomal dominant retinitis pigmentosa. Journal of Clinical Medicine, 11:6682, Nov 2022. URL: https://doi.org/10.3390/jcm11226682, doi:10.3390/jcm11226682. This article has 2 citations.

12. (NCT05573984a chunk 1):  Natural History of PRPF31 Mutation-Associated Retinal Dystrophy. PYC Therapeutics. 2022. ClinicalTrials.gov Identifier: NCT05573984

13. (xi2022geneaugmentationprevents pages 3-4): Zhouhuan Xi, Abhishek Vats, José-Alain Sahel, Yuanyuan Chen, and Leah C. Byrne. Gene augmentation prevents retinal degeneration in a crispr/cas9-based mouse model of prpf31 retinitis pigmentosa. Nature Communications, Dec 2022. URL: https://doi.org/10.1038/s41467-022-35361-8, doi:10.1038/s41467-022-35361-8. This article has 42 citations and is from a highest quality peer-reviewed journal.

14. (NCT06455826 chunk 1):  MAD of IVT VP-001 in PRPF31 Mutation-Associated Retinal Dystrophy Subjects (Wallaby). PYC Therapeutics. 2024. ClinicalTrials.gov Identifier: NCT06455826

15. (NCT06455826a chunk 1):  MAD of IVT VP-001 in PRPF31 Mutation-Associated Retinal Dystrophy Subjects (Wallaby). PYC Therapeutics. 2024. ClinicalTrials.gov Identifier: NCT06455826

16. (NCT05573984a chunk 2):  Natural History of PRPF31 Mutation-Associated Retinal Dystrophy. PYC Therapeutics. 2022. ClinicalTrials.gov Identifier: NCT05573984

17. (NCT05573984 chunk 2):  Natural History of PRPF31 Mutation-Associated Retinal Dystrophy. PYC Therapeutics. 2022. ClinicalTrials.gov Identifier: NCT05573984

## Artifacts

- [Edison artifact artifact-00](PRPF31-Related_Retinopathy-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](PRPF31-Related_Retinopathy-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](PRPF31-Related_Retinopathy-deep-research-falcon_artifacts/artifact-02.md)