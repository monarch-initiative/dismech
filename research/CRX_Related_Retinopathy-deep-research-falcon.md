---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-07T10:28:07.685785'
end_time: '2026-07-07T10:51:42.402194'
duration_seconds: 1414.72
template_file: templates\disease_pathophysiology_research.md
template_variables:
  disease_name: CRX-Related Retinopathy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 32
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: CRX_Related_Retinopathy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: CRX_Related_Retinopathy-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CRX-Related Retinopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CRX-Related Retinopathy** covering all of the
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
- **Disease Name:** CRX-Related Retinopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CRX-Related Retinopathy** covering all of the
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


# Comprehensive Research Report: CRX-Related Retinopathy

---

## 1. Disease Information

### Overview
CRX-related retinopathy encompasses a spectrum of inherited retinal diseases caused by mutations in the *CRX* (Cone-Rod Homeobox) gene, located on chromosome 19q13.33. CRX encodes a 299 amino acid homeodomain transcription factor essential for photoreceptor development, function, and maintenance (sun2023geneaugmentationfor pages 1-3, zheng2024transcriptionalprecisionin pages 1-2). CRX is the only gene known to be associated with all three major forms of inherited retinal degeneration: Leber congenital amaurosis (LCA), cone-rod dystrophy (CoRD), and retinitis pigmentosa (RP) (zheng2024transcriptionalprecisionin pages 1-2). The clinical spectrum ranges from mild adult-onset macular dystrophy to severe congenital blindness (sun2023geneaugmentationfor pages 1-3).

### Key Identifiers
- **OMIM:** Leber Congenital Amaurosis 7 (LCA7, OMIM #602225); Cone-Rod Dystrophy 2 (CoRD2, OMIM #120970); CRX Gene (OMIM *602225)
- **Orphanet:** ORPHA:71965 (LCA); ORPHA:1872 (Cone-rod dystrophy)
- **ICD-10:** H35.5 (Hereditary retinal dystrophy)
- **Chromosomal location:** 19q13.33
- **Gene:** CRX (HGNC:2383; NCBI Gene: 1406)

### Synonyms
- CRX-associated retinal dystrophy
- CRX-associated retinopathy
- Leber congenital amaurosis type 7 (LCA7)
- Cone-rod dystrophy type 2 (CoRD2, CORD2)
- CRX-related cone-rod dystrophy
- CRX-related macular dystrophy

---

## 2. Etiology

### Disease Causal Factors
CRX-related retinopathy is a Mendelian genetic disease caused by mutations in the *CRX* gene. To date, 93 disease-causing CRX mutations have been identified, and the ClinVar database documents 338 total CRX coding variants, of which 80 are classified as pathogenic or likely pathogenic, 192 as variants of uncertain significance, and 77 as benign or likely benign (sun2023geneaugmentationfor pages 1-3, zheng2024transcriptionalprecisionin pages 4-6).

### Genetic Risk Factors
The primary risk factor is inheritance of a pathogenic CRX variant. Most CRX disease variants arise de novo and are completely penetrant in heterozygotes, causing autosomal dominant disease (zheng2024transcriptionalprecisionin pages 4-6). Rare recessive presentations have also been documented, particularly with the R90W variant in homozygous state causing LCA (sun2023diseasecausingmutationsin pages 5-7, loukovitis2021areviewof pages 9-11). The de novo mutation rate for CRX has been estimated at approximately 10.34% among inherited eye disease trios, making it one of the top 10 genes with the highest de novo mutation burden (zheng2024transcriptionalprecisionin pages 4-6).

### Environmental and Protective Factors
No specific environmental risk factors or protective factors have been identified for CRX-related retinopathy. As a purely monogenic disorder, environmental contributions to disease onset are not established. However, genetic background and modifier genes may influence expressivity, as significant phenotypic variability has been observed even within families sharing the same CRX variant (zheng2024transcriptionalprecisionin pages 4-6, loukovitis2021areviewof pages 9-11).

---

## 3. Phenotypes

### Clinical Presentations
CRX-related retinopathy presents with considerable phenotypic variability, encompassing several distinct clinical entities (sun2023geneaugmentationfor pages 1-3, lin2025bifocalretinaldegeneration pages 2-4):

**Leber Congenital Amaurosis (LCA7)**
- Age of onset: Birth to early infancy (congenital/neonatal)
- Severity: Severe; poor visual acuity starting within the first year of life
- Phenotype: Severe early-onset blindness with cone-led retinal dystrophy; hyperopia is common
- HPO terms: HP:0000510 (Rod-cone dystrophy), HP:0000548 (Cone-rod dystrophy), HP:0001103 (Abnormal macular morphology), HP:0000505 (Visual impairment)
- Frequency: CRX accounts for 0.6–2.35% of LCA cases (winkler2020largeanimalmodels pages 12-14)

**Cone-Rod Dystrophy (CoRD2)**
- Age of onset: Variable (childhood to late adult onset depending on variant)
- Severity: Variable; ranges from mild macular dysfunction to severe bilateral visual loss
- Progression: Progressive; cone degeneration typically precedes rod degeneration
- HPO terms: HP:0000548 (Cone-rod dystrophy), HP:0007754 (Macular dystrophy), HP:0000572 (Visual loss)

**Retinitis Pigmentosa (RP)**
- Age of onset: Variable (typically later onset than LCA)
- Severity: Variable
- HPO terms: HP:0000510 (Rod-cone dystrophy), HP:0000546 (Retinal degeneration)

**Macular Dystrophy**
- Age of onset: Typically adult-onset
- Severity: Mild to moderate
- HPO terms: HP:0007754 (Macular dystrophy)

### Distinctive Phenotypic Features
A recent study of 60 patients with molecularly confirmed CRX-associated retinopathy identified a distinctive **bifocal retinal degeneration pattern** in approximately 12% of cases (all male), characterized by central retinal degeneration combined with a discrete non-contiguous area of altered autofluorescence in the nasal periphery (lin2025bifocalretinaldegeneration pages 2-4, lin2025bifocalretinaldegeneration pages 6-7). This bifocal pattern is not typically seen in other forms of inherited retinal disease and can serve as a diagnostic clue (lin2025bifocalretinaldegeneration pages 6-7).

### Electrophysiological Phenotype
All patients with bifocal degeneration demonstrated bilaterally subnormal PERG P50 responses indicating severe macular dysfunction. Full-field ERG patterns showed either pure cone dysfunction (2/6 cases), cone greater than rod dysfunction (3/6), or similar cone-rod involvement (1/6), with markedly delayed b-waves in most cases, consistent with a post-phototransduction locus of dysfunction (lin2025bifocalretinaldegeneration pages 2-4).

---

## 4. Genetic/Molecular Information

### Causal Gene: CRX
- **Gene symbol:** CRX
- **HGNC ID:** HGNC:2383
- **Chromosomal location:** 19q13.33
- **Gene structure:** 4 exons (loukovitis2021areviewof pages 9-11)
- **Protein:** 299 amino acids, containing three major functional domains (sun2023diseasecausingmutationsin pages 4-5):
  - **Homeodomain (residues 39–99):** Helix-turn-helix DNA binding domain recognizing the 5′-TAAT-3′ core motif (zheng2024transcriptionalprecisionin pages 8-10)
  - **Transcription effector/activation domain (residues 113–284):** Contains binding sites for transcriptional coregulators (sun2023diseasecausingmutationsin pages 4-5)
  - **OTX tail domain (residues 284–295):** Conserved C-terminal domain important for protein-protein interactions (zheng2024transcriptionalprecisionin pages 6-7)

### Pathogenic Variant Classification
CRX disease variants have been systematically classified into four major classes based on their functional impacts, as detailed in the following table (zheng2024transcriptionalprecisionin pages 6-7, zheng2024transcriptionalprecisionin pages 8-10, zheng2024transcriptionalprecisionin pages 7-8):

| Variant class | Representative variant(s) | ClinVar ID / identifier | Primary molecular mechanism | Effect on CRX protein function | Mouse / model phenotype | Associated human phenotype(s) |
|---|---|---|---|---|---|---|
| Truncated effector-domain variants | E168d2; human c.503_504del (p.Glu168fs) | VCV000099609 for E168d2 | Premature termination in the C-terminal transcription effector domain; mutant transcript/protein overexpression increases mutant:wild-type ratio, producing a dominant-negative effect in which mutant CRX outcompetes WT CRX at cognate regulatory sites (zheng2024transcriptionalprecisionin pages 6-7) | DNA-binding domain remains intact, but transcriptional activation is defective/incompetent because the effector domain is truncated; downstream photoreceptor gene activation is impaired (sun2023diseasecausingmutationsin pages 5-7, zheng2024transcriptionalprecisionin pages 6-7) | E168d2/+ mice have 6-8 ONL rows by 3 months, no detectable cone function, severely impaired rod function by 1 month, and complete rod function loss by 3 months; E168d2/d2 mice retain only 3-4 ONL rows by 1 month and never develop visual function (zheng2024transcriptionalprecisionin pages 6-7) | Dominant Leber congenital amaurosis (LCA7); severe early-onset retinal degeneration (sun2023diseasecausingmutationsin pages 5-7, zheng2024transcriptionalprecisionin pages 6-7) |
| Extended effector-domain variants | CrxRip; spontaneous c.763del (p.Gly255Alafs*133) | No ClinVar ID stated in gathered evidence | Frameshift creates an elongated mutant CRX with partial effector domain plus non-homologous C-terminal extension; altered residue composition likely perturbs recruitment specificity/affinity for transcriptional cofactors and mediators, causing genome-wide misregulation (zheng2024transcriptionalprecisionin pages 6-7, zheng2024transcriptionalprecisionin pages 7-8) | DNA-binding domain is preserved, but the altered/extended effector domain disrupts transcriptional regulation; proposed loss of OTX tail function and abnormal cofactor recruitment antagonize WT CRX (zheng2024transcriptionalprecisionin pages 6-7, zheng2024transcriptionalprecisionin pages 7-8) | Rip/+ mice are completely blind at 1 month, yet ONL thickness is largely preserved up to at least 18 months, indicating profound functional impairment and incomplete differentiation without rapid structural degeneration (zheng2024transcriptionalprecisionin pages 6-7) | Congenital blindness / LCA-like CRX-associated retinopathy; class exemplifies severe functional deficit with relatively preserved retinal thickness early on (sun2023geneaugmentationfor pages 3-4, zheng2024transcriptionalprecisionin pages 6-7) |
| Hypomorphic missense variants reducing DNA-binding affinity | R90W (p.Arg90Trp); also R40, R41, R43 class variants | VCV000007422 for R90W | Reduced homeodomain DNA-binding affinity lowers CRX target-gene activation; severity generally tracks with the degree of deviation from wild-type DNA binding strength (zheng2024transcriptionalprecisionin pages 8-10, zheng2024transcriptionalprecisionin pages 7-8) | CRX binds cognate DNA poorly and transactivates photoreceptor promoters weakly; R90 contributes structural stabilization of the HD-DNA complex rather than direct base contact (zheng2024transcriptionalprecisionin pages 8-10, zheng2024transcriptionalprecisionin pages 7-8) | CrxR90W/W mice resemble Crx knockout photoreceptor degeneration phenotypes; loss of photoreceptor differentiation/function is consistent with markedly reduced DNA binding (zheng2024transcriptionalprecisionin pages 7-8) | Recessive LCA and mild late-onset dominant cone-rod dystrophy; R40/R41/R43 variants are linked to more severe dominant retinal dystrophies (sun2023diseasecausingmutationsin pages 5-7, zheng2024transcriptionalprecisionin pages 7-8) |
| Antimorphic missense variants altering DNA-binding specificity / selectivity | E80A (p.Glu80Ala); K88N (p.Lys88Asn) | VCV000007416 for E80A; no ClinVar ID stated here for K88N | Gain-of-function / antimorphic mechanisms. E80A preserves preference for CRX sites but reduces selectivity, promoting promiscuous binding and hyperactivation of early target genes; K88N alters DNA-binding specificity, redirecting CRX to ectopic non-cognate sites (zheng2024transcriptionalprecisionin pages 8-10, zheng2024transcriptionalprecisionin pages 10-11) | E80A causes elevated transactivation at WT and suboptimal motifs; K88N changes preferred DNA sequence recognition from canonical CRX motifs toward alternative motifs, severely perturbing gene-expression programs (zheng2024transcriptionalprecisionin pages 8-10, zheng2024transcriptionalprecisionin pages 10-11) | E80A/+ mice show no detectable cone-mediated responses, defective rod-mediated responses at 1 month, shortened/disorganized outer segments and ONL disorganization, but no obvious early photoreceptor degeneration; knock-in studies of E80A and K88N demonstrate severe dominant retinopathy through distinct gain-of-function mechanisms (zheng2024transcriptionalprecisionin pages 8-10, winkler2020largeanimalmodels pages 12-14) | Severe early-onset dominant cone-rod dystrophy for E80A; severe dominant retinopathies including LCA/CoRD spectrum for E80A and K88N (sun2023geneaugmentationfor pages 1-3, sun2023diseasecausingmutationsin pages 5-7, winkler2020largeanimalmodels pages 12-14) |


*Table: This table summarizes the four major CRX pathogenic variant classes described in recent literature, linking representative mutations to molecular mechanisms, functional consequences, model phenotypes, and human disease presentations. It is useful for understanding genotype-mechanism-phenotype relationships across CRX-associated retinopathies.*

### Key Pathogenic Variants
Representative pathogenic variants include:
- **p.Glu168fs (c.503_504del; ClinVar VCV000099609):** Truncated effector domain; dominant LCA (zheng2024transcriptionalprecisionin pages 6-7)
- **p.Gly255Alafs*133 (c.763del):** Extended effector domain (CrxRip); congenital blindness (zheng2024transcriptionalprecisionin pages 6-7)
- **p.Arg90Trp (c.268C>T; ClinVar VCV000007422):** Hypomorphic; recessive LCA / mild dominant CoRD (zheng2024transcriptionalprecisionin pages 7-8)
- **p.Glu80Ala (c.239A>C; ClinVar VCV000007416):** Antimorphic gain-of-function; severe dominant CoRD (zheng2024transcriptionalprecisionin pages 7-8)
- **p.Lys88Asn:** Antimorphic altered specificity; severe dominant retinopathy (zheng2024transcriptionalprecisionin pages 8-10)
- **p.Gln228Ter (c.682C>T):** Nonsense; autosomal dominant CoRD with late onset and severe macular atrophy
- **p.Arg98Ter:** Nonsense; associated with variable RP presentations (zheng2024transcriptionalprecisionin pages 15-15)

### Inheritance Pattern
- Predominantly **autosomal dominant** (most disease-causing variants)
- Rare **autosomal recessive** forms (particularly homozygous R90W causing LCA) (sun2023diseasecausingmutationsin pages 5-7, loukovitis2021areviewof pages 9-11)
- High rate of **de novo** mutations (~10.34%) (zheng2024transcriptionalprecisionin pages 4-6)
- Most variants appear **completely penetrant** in heterozygotes, though some putative null variants show unexpected tolerance in carriers (zheng2024transcriptionalprecisionin pages 4-6)
- **Variable expressivity** is well documented, even within families sharing the same variant (lin2025bifocalretinaldegeneration pages 2-4, loukovitis2021areviewof pages 9-11)

### Functional Consequences
The ratio of mutant to wildtype CRX protein directly correlates with disease severity (sun2023diseasecausingmutationsin pages 5-7). Frameshift mutations in the last exon escape nonsense-mediated decay (NMD), leading to allelic-specific overexpression of mutant transcripts and accumulation of non-functional truncated proteins—a mechanism that increases the mutant-to-WT ratio and drives dominant-negative pathogenesis (zheng2024transcriptionalprecisionin pages 6-7).

---

## 5. Environmental Information

CRX-related retinopathy is a purely genetic condition with no established environmental risk factors, lifestyle contributors, or infectious agents. No gene-environment interactions have been described. The disease is determined entirely by the nature and functional impact of the CRX mutation.

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways
CRX operates as a master transcriptional regulator within the photoreceptor gene regulatory network. It belongs to the orthodenticle (OTX) gene family and is activated by OTX2 in photoreceptor precursors after cell cycle exit (sun2023diseasecausingmutationsin pages 1-2). CRX regulates gene expression through:
- **Chromatin remodeling:** CRX binding capacity depends on nucleosome interactions and chromatin accessibility (zheng2024transcriptionalprecisionin pages 3-4)
- **Synergistic interaction with NRL:** CRX and NRL co-occupancy of binding sites deforms DNA and facilitates transcriptional machinery access for rod-specific gene expression (zheng2024transcriptionalprecisionin pages 4-6)
- **Phase-separation capacity:** CRX activates genes through phase-separation of its activation domains (zheng2024transcriptionalprecisionin pages 11-12)
- **Interaction with BCOR:** The co-repressor BCOR modulates CRX/OTX2 transcriptional activity, reducing their ability to activate photoreceptor gene promoters (langouet2022mutationsinbcora pages 1-2)

**GO terms:** GO:0006355 (regulation of transcription, DNA-templated), GO:0007601 (visual perception), GO:0042462 (eye photoreceptor cell development), GO:0046530 (photoreceptor cell differentiation)

### Cellular Processes
CRX dysfunction results in failure of photoreceptor terminal differentiation. In CRX-deficient retinas, photoreceptor cells are produced normally but phototransduction gene expression is reduced, leading to progressive degeneration (langouet2022mutationsinbcora pages 1-2). Disease progression characteristically shows cone photoreceptor degeneration preceding rod degeneration, with rods initially functional but progressively degenerating (sun2023diseasecausingmutationsin pages 5-7).

### Pathogenic Mechanisms (Four Classes)
1. **Truncated effector domain variants** (e.g., E168d2): Dominant-negative mechanism via overexpression of transcriptionally incompetent mutant CRX that outcompetes WT CRX at cognate DNA binding sites (zheng2024transcriptionalprecisionin pages 6-7)
2. **Extended effector domain variants** (e.g., CrxRip): Altered amino acid composition of the effector domain disrupts recruitment specificity for transcriptional cofactors, causing genome-wide gene misregulation (zheng2024transcriptionalprecisionin pages 7-8)
3. **Hypomorphic missense variants** (e.g., R90W): Reduced DNA binding affinity diminishes CRX-mediated transactivation; severity correlates with binding affinity deviation from WT (zheng2024transcriptionalprecisionin pages 8-10, zheng2024transcriptionalprecisionin pages 7-8)
4. **Antimorphic missense variants** (e.g., E80A, K88N): Gain-of-function mechanisms—E80A reduces DNA binding selectivity causing hyperactivation and developmental asynchrony; K88N alters DNA binding specificity redirecting CRX to ectopic sites (zheng2024transcriptionalprecisionin pages 8-10, zheng2024transcriptionalprecisionin pages 10-11)

### Protein Dysfunction
The CRX homeodomain's N-terminal residues make specific contacts with DNA bases in the minor groove to recognize the 5′-TAAT-3′ core motif (zheng2024transcriptionalprecisionin pages 8-10). The consensus binding motif is 5′-TAATCC-3′ (zheng2024transcriptionalprecisionin pages 10-11). Mutations at different positions produce fundamentally different pathogenic effects—R90 stabilizes the DNA-binding structure through intramolecular interactions rather than direct DNA contact, while K88 and E80 contribute to binding selectivity and specificity (zheng2024transcriptionalprecisionin pages 8-10, zheng2024transcriptionalprecisionin pages 7-8).

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary organ:** Eye (retina)
- **Body system:** Visual/nervous system
- **UBERON terms:** UBERON:0000966 (retina), UBERON:0001773 (macula lutea), UBERON:0001782 (photoreceptor layer)

### Tissue and Cell Level
- **Photoreceptor cells** (both rods and cones): Primary cell type affected
  - Cone photoreceptors (CL:0000573) are typically affected before rod photoreceptors (CL:0000604) (sun2023diseasecausingmutationsin pages 5-7)
  - **CL terms:** CL:0000210 (photoreceptor cell), CL:0000573 (cone cell), CL:0000604 (rod cell)
- **Retinal pigment epithelium (RPE):** May be secondarily affected
- **Outer nuclear layer (ONL):** Progressive thinning observed in most severe forms (sun2023geneaugmentationfor pages 3-4)
- **Photoreceptor outer segments:** Failure of outer segment formation is a hallmark feature (sun2023diseasecausingmutationsin pages 5-7)

### Subcellular Level
- **Nucleus:** CRX functions as a nuclear transcription factor
- **Photoreceptor outer segments:** Failure to form properly in severe variants
- **GO Cellular Component terms:** GO:0005634 (nucleus), GO:0001750 (photoreceptor outer segment)

### Localization
- Bilateral involvement is the rule
- Central retina/macula predominantly affected in macular dystrophy and CoRD presentations
- Bifocal pattern (central + nasal peripheral) observed in ~12% of cases (lin2025bifocalretinaldegeneration pages 2-4, lin2025bifocalretinaldegeneration pages 6-7)

---

## 8. Temporal Development

### Onset
- **LCA7:** Congenital/neonatal onset; poor visual acuity within the first year of life (loukovitis2021areviewof pages 9-11)
- **CoRD2:** Variable; may present in childhood to early adulthood
- **RP:** Typically later onset
- **Macular dystrophy:** Adult-onset, may be mild (sun2023geneaugmentationfor pages 1-3)

### Progression
- Generally **progressive** retinal degeneration
- Disease course: **Chronic, lifelong**
- Cone degeneration typically precedes rod degeneration (sun2023diseasecausingmutationsin pages 5-7)
- Rate of progression is variable and depends on the specific CRX variant class
- Truncating effector-domain variants (e.g., E168d2) show relatively rapid photoreceptor degeneration, while extended-domain variants (e.g., CrxRip) may show preserved retinal structure despite severe functional impairment for prolonged periods (zheng2024transcriptionalprecisionin pages 6-7)

### Critical Periods
- Photoreceptor terminal differentiation during retinal development represents a critical window
- Photoreceptors retain some neuroplasticity for therapeutic intervention, though rescue effects remain partial in preclinical models (sun2023geneaugmentationfor pages 3-4)

---

## 9. Inheritance and Population

### Epidemiology
- CRX mutations account for **0.6–2.35% of LCA cases** (winkler2020largeanimalmodels pages 12-14)
- CRX is described as a common cone-rod dystrophy (CRD) causative gene (loukovitis2021areviewof pages 9-11)
- Inherited retinal diseases as a group affect approximately 1 in 2,000 to 1 in 4,000 people globally
- The overall prevalence of CRX-specific retinopathy is ultra-rare, though precise population-based prevalence data are not available

### Inheritance
- **Autosomal dominant** (predominant pattern) (zheng2024transcriptionalprecisionin pages 4-6)
- **Autosomal recessive** (rare; e.g., homozygous R90W) (sun2023diseasecausingmutationsin pages 5-7)
- **De novo** mutations are frequent (~10.34% of CRX disease cases) (zheng2024transcriptionalprecisionin pages 4-6)
- **Penetrance:** Most variants are completely penetrant, though some putative null variants show unexpected tolerance in heterozygous carriers (zheng2024transcriptionalprecisionin pages 4-6)
- **Variable expressivity:** Well documented; considerable phenotypic variability even within families (lin2025bifocalretinaldegeneration pages 2-4, loukovitis2021areviewof pages 9-11)

### Population Demographics
- CRX mutations have been reported across diverse ethnic populations including Caucasian, Japanese, Chinese, Korean, Mexican, Pakistani, and Indian populations
- No clear ethnic predilection has been established
- Male predominance was noted in the bifocal degeneration subset (6/6 cases male in Lin et al. 2025) (lin2025bifocalretinaldegeneration pages 2-4)

---

## 10. Diagnostics

### Clinical Tests
**Electrophysiology (MAXO:0000932):**
- Full-field ERG (ISCEV standard): Reveals cone or cone-rod dysfunction patterns; markedly delayed b-waves in many cases with a post-phototransduction locus (lin2025bifocalretinaldegeneration pages 2-4)
- Pattern ERG (PERG): Bilaterally subnormal P50 responses indicating macular dysfunction (lin2025bifocalretinaldegeneration pages 2-4)

**Imaging:**
- **SD-OCT:** Demonstrates central outer retinal disruption, thinning of the outer nuclear layer, and retinal disorganization (lin2025bifocalretinaldegeneration pages 4-6)
- **Ultra-widefield fundus autofluorescence (FAF):** Identifies patterns of retinal degeneration including the distinctive bifocal pattern; more sensitive than clinical examination for detecting nasal peripheral degeneration (lin2025bifocalretinaldegeneration pages 4-6, lin2025bifocalretinaldegeneration pages 2-4)
- **Fundus photography:** Shows macular atrophy, pigmentary changes, and peripheral retinal abnormalities

### Genetic Testing
- **Recommended approach:** Targeted gene panels for inherited retinal diseases (IRDs) including CRX, or whole-exome sequencing (WES) (lin2025bifocalretinaldegeneration pages 4-6)
- **Whole-exome sequencing (WES):** Effective first-line approach; diagnostic yield for IRDs approximately 50–73% across cohorts
- **Gene panels:** CRX is included in standard IRD gene panels (typically 200–350+ genes)
- **Single gene testing:** Available for CRX (Sanger sequencing)
- **Genomic initiatives:** The 100,000 Genomes Project and NHS Genomic Medicine Service have facilitated molecular diagnosis (lin2025bifocalretinaldegeneration pages 4-6)
- **Diagnostic challenge:** 40–50% of IRD cases remain molecularly unresolved (lin2025bifocalretinaldegeneration pages 4-6, lin2025bifocalretinaldegeneration pages 6-7)

### Differential Diagnosis
- Other forms of LCA (LCA1-LCA19, caused by GUCY2D, RPE65, CRB1, CEP290, etc.)
- Other forms of cone-rod dystrophy (caused by ABCA4, GUCY2D, RPGR, etc.)
- Retinitis pigmentosa (>80 causative genes)
- Distinguishing features: Bifocal nasal degeneration pattern, specific ERG profile, and autosomal dominant inheritance help direct genetic testing toward CRX (lin2025bifocalretinaldegeneration pages 6-7)

---

## 11. Outcome/Prognosis

### Visual Outcomes
- **LCA7:** Severe visual impairment from birth/early infancy; poor visual acuity starting within the first year of life (loukovitis2021areviewof pages 9-11)
- **CoRD2:** Progressive visual loss; rate depends on variant class
- **Macular dystrophy:** May preserve peripheral vision longer

### Prognostic Factors
- **Variant class** is the strongest prognostic factor: antimorphic and truncating variants cause more severe disease than hypomorphic variants
- **Mutant-to-wildtype CRX protein ratio** correlates directly with disease severity (sun2023diseasecausingmutationsin pages 5-7)
- **C-terminus truncation length** positively correlates with degree of allelic imbalance and onset of photoreceptor degeneration (zheng2024transcriptionalprecisionin pages 6-7)
- The disease is **not life-threatening** but causes significant visual morbidity
- CRX-related retinopathy does not affect life expectancy

### Complications
- Legal blindness (particularly in LCA7 and severe CoRD)
- Photophobia and nystagmus (in LCA presentations)
- Progressive visual field loss
- Impaired color vision (early cone dysfunction)

---

## 12. Treatment

### Current Management
No approved pharmacological or gene therapy treatments exist specifically for CRX-related retinopathy. Current management is **supportive** (MAXO:0000016):
- Low vision aids and rehabilitation
- Orientation and mobility training
- Educational accommodations
- Genetic counseling for family planning (MAXO:0000127)
- Regular ophthalmological monitoring

### Gene Therapy Approaches (Preclinical)
**Gene augmentation (MAXO:0001001):**
- A Tet-On-hCRX inducible system has been developed for proof-of-concept gene augmentation in CRX-null mouse retinas, demonstrating that CRX expression can be induced and that photoreceptors retain neuroplasticity for therapeutic intervention, though rescue effects remain partial (sun2023geneaugmentationfor pages 3-4, sun2023geneaugmentationfor pages 4-6)
- **AAV2/5-mediated gene augmentation** has been tested using photoreceptor-specific promoters (CRX or GRK promoters) with efficient transduction in neonatal mice (sun2023geneaugmentationfor pages 4-6)
- AAV-mediated gene therapy has been tested in patient iPSC-derived retinal organoids for dominant CRX-LCA, demonstrating feasibility of rescue in human tissue models (agarwal2026retinalorganoidscurrent pages 42-44)

**Gene editing:**
- CRISPR/Cas9-based approaches for knocking out mutant CRX alleles are under investigation (sun2023geneaugmentationfor pages 4-6)
- Suppression-and-replacement strategies may be applicable for dominant-negative variants

**Combination therapies:**
- Anti-apoptotic and neuroprotective agents have been explored as adjunctive therapies (sun2023geneaugmentationfor pages 4-6)
- Nr2e3 gene therapy has been investigated as a broad-spectrum approach that resets transcription factor networks including CRX-regulated genes in multiple RP models

### Challenges for Gene Therapy
- CRX is an early photoreceptor transcription factor; timing of intervention relative to photoreceptor differentiation is critical (sun2023geneaugmentationfor pages 4-6)
- For dominant-negative variants, simple gene augmentation may be insufficient; suppression of the mutant allele may also be required
- Different variant classes require different therapeutic approaches, necessitating precision medicine strategies (sun2023geneaugmentationfor pages 1-3, sun2023diseasecausingmutationsin pages 5-7)

### Clinical Trials
No active clinical trials specifically targeting CRX-related retinopathy were identified in ClinicalTrials.gov searches. Treatment development remains at the **preclinical stage**.

---

## 13. Prevention

### Primary Prevention
- No primary prevention measures exist for this genetic condition
- **Genetic counseling** (MAXO:0000127) is essential given the autosomal dominant inheritance and high de novo mutation rate

### Secondary Prevention (Screening)
- **Cascade genetic testing** of family members when a pathogenic CRX variant is identified in a proband
- **Prenatal genetic testing** and **preimplantation genetic diagnosis (PGD)** are available for families with known CRX mutations
- Recognizing distinctive phenotypic patterns (e.g., bifocal nasal degeneration) can expedite molecular diagnosis (lin2025bifocalretinaldegeneration pages 6-7)

### Tertiary Prevention
- Regular ophthalmological monitoring to track disease progression
- Low vision rehabilitation to optimize remaining visual function
- Psychosocial support

---

## 14. Other Species / Natural Disease

### Naturally Occurring Animal Models
- **CrxRdy cat** (*Felis catus*): A spontaneously occurring model carrying a heterozygous 1-bp deletion in CRX causing a Class III antimorphic frameshift/nonsense mutation. Heterozygous CrxRdy/+ cats exhibit severe cone-led retinal dystrophy modeling early childhood-onset blindness. This is the earliest documented large animal model for CRX-associated disease (winkler2020largeanimalmodels pages 12-14). The feline retina provides translational advantages over rodent models due to its cone-rich region analogous to the human macula.
- **OMIA:** CRX-related retinal degeneration is catalogued in Online Mendelian Inheritance in Animals

---

## 15. Model Organisms

A comprehensive set of animal and cellular models has been developed to study distinct CRX pathogenic mechanisms:

| Model name/type | Species | Genetic modification / mutation | Phenotype recapitulation (key features) | Disease modeled | Key findings | References |
|---|---|---|---|---|---|---|
| CrxE168d2 knock-in mouse | Mouse (*Mus musculus*) | Knock-in of human-equivalent **c.503_504del (p.Glu168fs)** truncating effector-domain variant | Heterozygotes retain only **6–8 ONL rows by 3 months**, have **no detectable cone function**, **severely impaired rod function by 1 month**, and complete rod function loss by 3 months; homozygotes have **3–4 ONL rows by 1 month** and never develop visual function | Dominant **LCA7** / severe early-onset CRX retinopathy | Demonstrated that C-terminal truncating variants act largely through **dominant-negative effects** with **allelic overexpression** of mutant transcript/protein, increasing mutant:WT ratio and disrupting downstream photoreceptor gene regulation | (zheng2024transcriptionalprecisionin pages 6-7) |
| CrxRip mouse | Mouse (*Mus musculus*) | Spontaneous **c.763del (p.Gly255Alafs*133)** frameshift causing extended non-homologous C-terminus | **Completely blind at 1 month**, but **ONL thickness largely preserved up to at least 18 months**; incomplete photoreceptor differentiation and severe functional loss without rapid structural degeneration | Congenital blindness / **LCA-like** CRX-associated retinopathy | Showed that extended effector-domain variants can cause severe dysfunction by altering **cofactor recruitment** and transcriptional regulation, distinct from rapid-degeneration truncation models | (zheng2024transcriptionalprecisionin pages 6-7, zheng2024transcriptionalprecisionin pages 7-8) |
| CrxR90W knock-in mouse | Mouse (*Mus musculus*) | Knock-in **p.Arg90Trp** homeodomain missense variant | Phenotype similar to **Crx-null** retina in homozygotes, with major photoreceptor dysfunction/degeneration due to failure of normal terminal differentiation | Recessive **LCA** and mild late-onset dominant **CoRD** | Established a **hypomorphic** mechanism: markedly reduced DNA-binding affinity and weak transactivation of photoreceptor promoters; severity tracks with loss of DNA-binding strength | (zheng2024transcriptionalprecisionin pages 8-10, zheng2024transcriptionalprecisionin pages 7-8) |
| CrxE80A knock-in mouse | Mouse (*Mus musculus*) | Knock-in **p.Glu80Ala** homeodomain missense variant | **No detectable cone-mediated responses**, defective rod-mediated responses at 1 month, **shortened outer segments**, ONL disorganization, but **no obvious early photoreceptor degeneration** | Severe early-onset dominant **cone-rod dystrophy** | Demonstrated a **gain-of-function / antimorphic** mechanism in which CRX retains target preference but loses selectivity, causing promiscuous binding and **hyperactivation** of early target genes with developmental asynchrony | (zheng2024transcriptionalprecisionin pages 8-10, zheng2024transcriptionalprecisionin pages 7-8) |
| CrxK88N knock-in mouse | Mouse (*Mus musculus*) | Knock-in **p.Lys88Asn** homeodomain missense variant | Severe dominant retinopathy phenotype in knock-in models; mechanistically distinct from hypomorphic variants | Severe dominant **CoRD/LCA-spectrum** retinopathy | Showed that some homeodomain mutants alter **DNA-binding specificity** rather than merely affinity, redirecting CRX to ectopic non-cognate sites and severely perturbing the photoreceptor gene network | (zheng2024transcriptionalprecisionin pages 8-10, zheng2024transcriptionalprecisionin pages 10-11, zheng2024transcriptionalprecisionin pages 13-13) |
| Crx knockout mouse | Mouse (*Mus musculus*) | **Crx null / deletion** | Photoreceptors are produced, but phototransduction gene expression is reduced; heterozygous deletion produces only **very mild phenotypes** | Loss-of-function reference model for CRX deficiency | Important comparator showing that **haploinsufficiency alone is usually insufficient** to explain severe dominant CRX disease; therefore not an ideal model for dominant CRX retinopathies | (langouet2022mutationsinbcora pages 1-2, zheng2024transcriptionalprecisionin pages 6-7) |
| CrxRdy cat (spontaneous model) | Cat (*Felis catus*) | Spontaneous **1-bp deletion** causing truncating Class III CRX mutation with intact DNA-binding domain but defective transactivation | **Severe cone-led retinal dystrophy** / early childhood-onset blindness analog; documented as a spontaneous large-animal model | **LCA7** / severe CRX-associated retinal degeneration | Earliest documented large-animal CRX model; supported **allelic overexpression** and truncation-based pathogenicity, and provides translational advantages because feline retina better approximates human cone-rich specializations than rodent retina | (winkler2020largeanimalmodels pages 12-14, zheng2024transcriptionalprecisionin pages 6-7) |
| CRX monoallelic knockout retinal organoids | Human retinal organoids | **Monoallelic CRX knockout / haploinsufficiency** in hESC-derived retinal organoids | **Delayed ONL stratification**, **thinner ONL**, major **loss of outer segments**, downregulation of phototransduction and inner/outer-segment genes; **arrested translocation** of CRX+ precursors and actomyosin over-tension during early differentiation | Dominant CRX-associated retinopathy due to **haploinsufficiency** | Provided direct human-model evidence that **CRX haploinsufficiency can impair precursor translocation and differentiation**, revealing a pathogenic mechanism not fully captured in mouse systems | (sun2023geneaugmentationfor pages 3-4, zheng2024transcriptionalprecisionin pages 1-2) |
| CRX-LCA patient iPSC-derived retinal organoids | Human iPSC-derived retinal organoids | Patient-derived organoids carrying dominant **CRX-LCA** mutation(s) | Retinal organoid phenotypes used to assess rescue of photoreceptor development/function in a human context | Dominant **CRX-LCA** | Demonstrated feasibility of testing **AAV-mediated gene therapy** in patient stem-cell-derived retinal tissue; supports organoids as a precision preclinical platform for CRX therapeutic development | (zheng2024transcriptionalprecisionin pages 13-13, agarwal2026retinalorganoidscurrent pages 42-44) |
| Tet-On-hCRX transgenic augmentation model | Mouse (*Mus musculus*) | Inducible **human CRX transgene** under Tet-On control for augmentation in mutant/null CRX backgrounds | Allows **quantitative and temporal control** of augmented CRX during the developmental window; CRX expression inducible in null retinae | Preclinical therapeutic model for CRX-associated retinopathies | Proof-of-concept model showing photoreceptors retain **neuroplasticity** and can respond to CRX augmentation, though rescue is **partial**; informed development of **AAV2/5** photoreceptor-directed augmentation strategies | (sun2023geneaugmentationfor pages 3-4, sun2023geneaugmentationfor pages 4-6, sun2023geneaugmentationfor pages 7-10) |


*Table: This table summarizes the principal animal and cellular models used to study CRX-related retinopathy, spanning mouse, cat, and human organoid systems. It highlights how each model captures distinct mechanisms such as haploinsufficiency, dominant-negative truncation, and altered DNA-binding specificity, and why these models are useful for therapeutic development.*

### Key Findings from Models
- The **Crx knockout mouse** demonstrates that haploinsufficiency alone produces only very mild phenotypes, confirming that dominant-negative or gain-of-function mechanisms drive severe disease (langouet2022mutationsinbcora pages 1-2, zheng2024transcriptionalprecisionin pages 6-7)
- **Human retinal organoids** with monoallelic CRX knockout revealed delayed ONL stratification, thinner ONL, loss of outer segments, and arrested translocation of CRX+ precursors—confirming haploinsufficiency as a contributing mechanism in human tissue and revealing a novel role for CRX in regulating postmitotic photoreceptor precursor translocation (sun2023geneaugmentationfor pages 3-4)
- CRX **ChIP-seq** studies have mapped the cis-regulatory architecture of mouse photoreceptors, revealing where CRX binds genome-wide to regulate photoreceptor gene expression (zheng2024transcriptionalprecisionin pages 11-12)
- **Tet-On-hCRX transgenic mice** demonstrated that photoreceptors retain neuroplasticity amenable to gene augmentation, providing critical proof-of-concept for future therapeutic approaches (sun2023geneaugmentationfor pages 3-4, sun2023geneaugmentationfor pages 4-6)

---

## Summary

CRX-related retinopathy is a clinically heterogeneous group of inherited retinal dystrophies caused by mutations in the *CRX* transcription factor gene. Over 25 years of research have established four distinct pathogenic variant classes, each with well-characterized molecular mechanisms ranging from dominant-negative effects through altered DNA binding specificity to haploinsufficiency. The disease spectrum encompasses LCA7, CoRD2, RP, and macular dystrophy, with most cases following autosomal dominant inheritance with frequent de novo occurrence. Diagnosis relies on electrophysiology (ERG, PERG), multimodal retinal imaging (OCT, ultra-widefield autofluorescence), and molecular genetic testing. No approved treatments exist, but preclinical gene augmentation and gene editing approaches show promise, with AAV-mediated delivery and CRISPR-based strategies under active investigation. The development of multiple knock-in mouse models, the CrxRdy cat model, and human retinal organoid systems continues to advance understanding of disease mechanisms and therapeutic development. Systems biology approaches integrating CRX intrinsic activities, protein interactions, and chromatin environment are expected to accelerate precision medicine for CRX-linked diseases (zheng2024transcriptionalprecisionin pages 8-10, zheng2024transcriptionalprecisionin pages 1-2, zheng2024transcriptionalprecisionin pages 10-11).

References

1. (sun2023geneaugmentationfor pages 1-3): Chi Sun and Shiming Chen. Gene augmentation for autosomal dominant crx-associated retinopathies. Advances in experimental medicine and biology, 1415:135-141, Jan 2023. URL: https://doi.org/10.1007/978-3-031-27681-1\_21, doi:10.1007/978-3-031-27681-1\_21. This article has 8 citations and is from a peer-reviewed journal.

2. (zheng2024transcriptionalprecisionin pages 1-2): Yiqiao Zheng and Shiming Chen. Transcriptional precision in photoreceptor development and diseases – lessons from 25 years of crx research. Frontiers in Cellular Neuroscience, Feb 2024. URL: https://doi.org/10.3389/fncel.2024.1347436, doi:10.3389/fncel.2024.1347436. This article has 9 citations.

3. (zheng2024transcriptionalprecisionin pages 4-6): Yiqiao Zheng and Shiming Chen. Transcriptional precision in photoreceptor development and diseases – lessons from 25 years of crx research. Frontiers in Cellular Neuroscience, Feb 2024. URL: https://doi.org/10.3389/fncel.2024.1347436, doi:10.3389/fncel.2024.1347436. This article has 9 citations.

4. (sun2023diseasecausingmutationsin pages 5-7): Chi Sun and Shiming Chen. Disease-causing mutations in genes encoding transcription factors critical for photoreceptor development. Frontiers in Molecular Neuroscience, Apr 2023. URL: https://doi.org/10.3389/fnmol.2023.1134839, doi:10.3389/fnmol.2023.1134839. This article has 18 citations.

5. (loukovitis2021areviewof pages 9-11): Eleftherios Loukovitis, Stoimeni Anastasia, Paris Tranos, Miltos Balidis, Solon Asteriadis, Vakalis Thanos, Sousouras Thanos, and George Anogeianakis. A review of recent developments in retinitis pigmentosa genetics, its clinical features, and natural course. Medical Hypothesis, Discovery & Innovation in Ophthalmology, Feb 2021. URL: https://doi.org/10.51329/mehdiophthal1410, doi:10.51329/mehdiophthal1410. This article has 11 citations.

6. (lin2025bifocalretinaldegeneration pages 2-4): Siying Lin, Gavin Arno, Anthony G. Robson, Elena R. Schiff, Moin D. Mohamed, Michel Michaelides, Andrew R. Webster, and Omar A. Mahroo. Bifocal retinal degeneration observed on ultra-widefield autofluorescence in some cases of crx-associated retinopathy. Eye, 39:951-957, Dec 2025. URL: https://doi.org/10.1038/s41433-024-03522-2, doi:10.1038/s41433-024-03522-2. This article has 3 citations and is from a peer-reviewed journal.

7. (winkler2020largeanimalmodels pages 12-14): Paige A. Winkler, Laurence M. Occelli, and Simon M. Petersen-Jones. Large animal models of inherited retinal degenerations: a review. Cells, 9:882, Apr 2020. URL: https://doi.org/10.3390/cells9040882, doi:10.3390/cells9040882. This article has 94 citations.

8. (lin2025bifocalretinaldegeneration pages 6-7): Siying Lin, Gavin Arno, Anthony G. Robson, Elena R. Schiff, Moin D. Mohamed, Michel Michaelides, Andrew R. Webster, and Omar A. Mahroo. Bifocal retinal degeneration observed on ultra-widefield autofluorescence in some cases of crx-associated retinopathy. Eye, 39:951-957, Dec 2025. URL: https://doi.org/10.1038/s41433-024-03522-2, doi:10.1038/s41433-024-03522-2. This article has 3 citations and is from a peer-reviewed journal.

9. (sun2023diseasecausingmutationsin pages 4-5): Chi Sun and Shiming Chen. Disease-causing mutations in genes encoding transcription factors critical for photoreceptor development. Frontiers in Molecular Neuroscience, Apr 2023. URL: https://doi.org/10.3389/fnmol.2023.1134839, doi:10.3389/fnmol.2023.1134839. This article has 18 citations.

10. (zheng2024transcriptionalprecisionin pages 8-10): Yiqiao Zheng and Shiming Chen. Transcriptional precision in photoreceptor development and diseases – lessons from 25 years of crx research. Frontiers in Cellular Neuroscience, Feb 2024. URL: https://doi.org/10.3389/fncel.2024.1347436, doi:10.3389/fncel.2024.1347436. This article has 9 citations.

11. (zheng2024transcriptionalprecisionin pages 6-7): Yiqiao Zheng and Shiming Chen. Transcriptional precision in photoreceptor development and diseases – lessons from 25 years of crx research. Frontiers in Cellular Neuroscience, Feb 2024. URL: https://doi.org/10.3389/fncel.2024.1347436, doi:10.3389/fncel.2024.1347436. This article has 9 citations.

12. (zheng2024transcriptionalprecisionin pages 7-8): Yiqiao Zheng and Shiming Chen. Transcriptional precision in photoreceptor development and diseases – lessons from 25 years of crx research. Frontiers in Cellular Neuroscience, Feb 2024. URL: https://doi.org/10.3389/fncel.2024.1347436, doi:10.3389/fncel.2024.1347436. This article has 9 citations.

13. (sun2023geneaugmentationfor pages 3-4): Chi Sun and Shiming Chen. Gene augmentation for autosomal dominant crx-associated retinopathies. Advances in experimental medicine and biology, 1415:135-141, Jan 2023. URL: https://doi.org/10.1007/978-3-031-27681-1\_21, doi:10.1007/978-3-031-27681-1\_21. This article has 8 citations and is from a peer-reviewed journal.

14. (zheng2024transcriptionalprecisionin pages 10-11): Yiqiao Zheng and Shiming Chen. Transcriptional precision in photoreceptor development and diseases – lessons from 25 years of crx research. Frontiers in Cellular Neuroscience, Feb 2024. URL: https://doi.org/10.3389/fncel.2024.1347436, doi:10.3389/fncel.2024.1347436. This article has 9 citations.

15. (zheng2024transcriptionalprecisionin pages 15-15): Yiqiao Zheng and Shiming Chen. Transcriptional precision in photoreceptor development and diseases – lessons from 25 years of crx research. Frontiers in Cellular Neuroscience, Feb 2024. URL: https://doi.org/10.3389/fncel.2024.1347436, doi:10.3389/fncel.2024.1347436. This article has 9 citations.

16. (sun2023diseasecausingmutationsin pages 1-2): Chi Sun and Shiming Chen. Disease-causing mutations in genes encoding transcription factors critical for photoreceptor development. Frontiers in Molecular Neuroscience, Apr 2023. URL: https://doi.org/10.3389/fnmol.2023.1134839, doi:10.3389/fnmol.2023.1134839. This article has 18 citations.

17. (zheng2024transcriptionalprecisionin pages 3-4): Yiqiao Zheng and Shiming Chen. Transcriptional precision in photoreceptor development and diseases – lessons from 25 years of crx research. Frontiers in Cellular Neuroscience, Feb 2024. URL: https://doi.org/10.3389/fncel.2024.1347436, doi:10.3389/fncel.2024.1347436. This article has 9 citations.

18. (zheng2024transcriptionalprecisionin pages 11-12): Yiqiao Zheng and Shiming Chen. Transcriptional precision in photoreceptor development and diseases – lessons from 25 years of crx research. Frontiers in Cellular Neuroscience, Feb 2024. URL: https://doi.org/10.3389/fncel.2024.1347436, doi:10.3389/fncel.2024.1347436. This article has 9 citations.

19. (langouet2022mutationsinbcora pages 1-2): Maéva Langouët, Christine Jolicoeur, Awais Javed, Pierre Mattar, Micah D. Gearhart, Stephen P. Daiger, Mette Bertelsen, Lisbeth Tranebjærg, Nanna D. Rendtorff, Karen Grønskov, Catherine Jespersgaard, Rui Chen, Zixi Sun, Hui Li, Najmeh Alirezaie, Jacek Majewski, Vivian J. Bardwell, Ruifang Sui, Robert K. Koenekoop, and Michel Cayouette. Mutations in<i>bcor</i>, a co-repressor of<i>crx/otx2</i>, are associated with early-onset retinal degeneration. Sep 2022. URL: https://doi.org/10.1126/sciadv.abh2868, doi:10.1126/sciadv.abh2868. This article has 13 citations and is from a highest quality peer-reviewed journal.

20. (lin2025bifocalretinaldegeneration pages 4-6): Siying Lin, Gavin Arno, Anthony G. Robson, Elena R. Schiff, Moin D. Mohamed, Michel Michaelides, Andrew R. Webster, and Omar A. Mahroo. Bifocal retinal degeneration observed on ultra-widefield autofluorescence in some cases of crx-associated retinopathy. Eye, 39:951-957, Dec 2025. URL: https://doi.org/10.1038/s41433-024-03522-2, doi:10.1038/s41433-024-03522-2. This article has 3 citations and is from a peer-reviewed journal.

21. (sun2023geneaugmentationfor pages 4-6): Chi Sun and Shiming Chen. Gene augmentation for autosomal dominant crx-associated retinopathies. Advances in experimental medicine and biology, 1415:135-141, Jan 2023. URL: https://doi.org/10.1007/978-3-031-27681-1\_21, doi:10.1007/978-3-031-27681-1\_21. This article has 8 citations and is from a peer-reviewed journal.

22. (agarwal2026retinalorganoidscurrent pages 42-44): Renu Agarwal, Igor Iezhitsa, Jose R. Hombrebueno, and Puneet Agarwal. Retinal organoids: current status of development and new avenues for application in disease modeling, drug discovery and therapeutics. International Journal of Retina and Vitreous, May 2026. URL: https://doi.org/10.1186/s40942-026-00846-x, doi:10.1186/s40942-026-00846-x. This article has 1 citations.

23. (zheng2024transcriptionalprecisionin pages 13-13): Yiqiao Zheng and Shiming Chen. Transcriptional precision in photoreceptor development and diseases – lessons from 25 years of crx research. Frontiers in Cellular Neuroscience, Feb 2024. URL: https://doi.org/10.3389/fncel.2024.1347436, doi:10.3389/fncel.2024.1347436. This article has 9 citations.

24. (sun2023geneaugmentationfor pages 7-10): Chi Sun and Shiming Chen. Gene augmentation for autosomal dominant crx-associated retinopathies. Advances in experimental medicine and biology, 1415:135-141, Jan 2023. URL: https://doi.org/10.1007/978-3-031-27681-1\_21, doi:10.1007/978-3-031-27681-1\_21. This article has 8 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](CRX_Related_Retinopathy-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](CRX_Related_Retinopathy-deep-research-falcon_artifacts/artifact-01.md)