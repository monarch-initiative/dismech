---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-14T15:41:16.108195'
end_time: '2026-07-14T16:12:02.934383'
duration_seconds: 1846.83
template_file: templates\disease_pathophysiology_research.md
template_variables:
  disease_name: Hypertensive Retinopathy
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 39
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Hypertensive_Retinopathy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypertensive Retinopathy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Hypertensive Retinopathy** covering all of the
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
- **Disease Name:** Hypertensive Retinopathy
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Hypertensive Retinopathy** covering all of the
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


## Comprehensive Disease Characteristics Report: Hypertensive Retinopathy (HR)

### Scope and evidence types used
This report synthesizes (i) clinical guidance/position statements, (ii) systematic reviews, (iii) observational imaging studies (including OCTA), and (iv) ClinicalTrials.gov registry records. Priority is given to 2023–2024 sources where available; several core phenotype/classification descriptions rely on a 2022 synthesis review and classic pathogenesis literature because many diagnostic concepts are stable and still referenced by recent guidance.

---

## 1. Disease Information

### 1.1 Concise overview (current understanding)
**Hypertensive retinopathy (HR)** is commonly defined as **retinal microvascular signs that develop in response to raised blood pressure**, representing ocular end-organ involvement of hypertension. A widely used clinical framework is the **Keith–Wagener–Barker (KWB)** grading system, where severe grades reflect accelerated/malignant hypertensive states and worse prognosis. (marco2022aliteraturereview pages 2-4, kulkarni2023managementofhypertensive pages 2-3)

A key pathogenetic clarification—particularly relevant in malignant hypertension—is that fundus lesions can be separated into **(1) hypertensive retinopathy, (2) hypertensive choroidopathy, and (3) hypertensive optic neuropathy**; notably, **optic disc edema**, historically included within hypertensive retinopathy, is better considered **hypertensive optic neuropathy**. (kim2023hypertensiveretinopathy pages 1-2)

### 1.2 Key identifiers (ontology/terminology)
* **ICD-10/ICD-11, MeSH, MONDO, OMIM, Orphanet:** These identifiers were **not present in the retrieved full-text evidence** in this run; therefore they cannot be asserted here with primary citations.
* **Clinical grading systems used in current practice/literature:** Keith–Wagener–Barker (KWB) grades 1–4; other grading systems (Scheie; Wong–Mitchell) are referenced in synthesis literature. (marco2022aliteraturereview pages 4-6)

### 1.3 Synonyms and alternative names
Historical terminology includes “albuminuric retinitis,” “angiospastic retinopathy,” and “hypertensive neuroretinopathy,” reflecting early descriptions linking severe hypertension and renal disease. (kim2023hypertensiveretinopathy pages 1-2)

### 1.4 Evidence source type
Evidence is primarily from **aggregated disease-level resources** (cohorts, systematic reviews, imaging studies, clinical guidance). The retinopathy/choroidopathy/optic-neuropathy separation is grounded in pathogenetic clinical research and clinicopathologic interpretation. (kim2023hypertensiveretinopathy pages 1-2, marco2022aliteraturereview pages 2-4)

---

## 2. Etiology

### 2.1 Causal factors
**Primary causal driver:** systemic arterial hypertension (sustained or acutely severe) producing retinal microvascular autoregulatory stress, endothelial injury, and (in severe states) blood–retina barrier disruption. (marco2022aliteraturereview pages 2-4, kim2023hypertensiveretinopathy pages 2-3)

**Secondary/mediating mechanisms emphasized in recent mechanistic/imaging work:**
* **Autoregulation failure** when BP rises beyond autoregulatory thresholds, associated with endothelial injury and vascular permeability changes. (kim2023hypertensiveretinopathy pages 2-3)
* **Renin–angiotensin–aldosterone system (RAAS) activation** and excess **angiotensin II** (particularly in renal/secondary hypertension) driving vasoconstriction/vasospasm, arterial stiffness, reduced retinal perfusion, and reduced OCTA-measured vascular density. (wang2024octaevaluateschanges pages 6-7, wang2024octaevaluateschanges pages 9-10)

### 2.2 Risk factors (representative)
* **Degree and duration of hypertension** (epidemiology difficult to quantify precisely due to confounding retinal vascular diseases, but incidence rises with severity and duration). (marco2022aliteraturereview pages 1-2)
* **Chronic kidney disease / renal hypertension** as a systemic context with high burden of hypertensive retinal microvascular abnormalities and reduced OCTA vessel density. (wang2024octaevaluateschanges pages 9-10)
* **Ethnicity/sex effect modification:** BIHS position paper notes that while hypertension/retinopathy are overall more prevalent in Afro-Caribbeans than Europeans, the relationship between hypertension and retinopathy prevalence is stronger in Europeans (particularly women) and weaker in Afro-Caribbeans (especially women). (kulkarni2023managementofhypertensive pages 2-3)

### 2.3 Protective factors
No evidence for specific genetic or environmental protective factors was identified in the retrieved set.

### 2.4 Gene–environment interactions
No hypertensive-retinopathy-specific gene–environment interaction evidence was identified.

---

## 3. Phenotypes

### 3.1 Classic fundus signs
A synthesis review describes classic HR signs: generalized or focal arteriolar narrowing, arteriovenous (AV) nicking, copper/silver wiring, flame-shaped and dot-blot hemorrhages, hard exudates, cotton-wool spots, and microaneurysms; malignant disease may include papilledema, congested veins, and macular star. (marco2022aliteraturereview pages 2-4, marco2022aliteraturereview pages 4-6)

**KWB grading (explicit features from 2023 BIHS):**
* Grade 1: mild narrowing/sclerosis of retinal arterioles
* Grade 2: moderate–severe arteriolar changes + venous compression at AV crossings + exaggerated arterial light reflex
* Grade 3: flame/dot hemorrhages, cotton-wool spots, hard exudates, microaneurysms
* Grade 4: bilateral papilloedema (optic disc swelling)
(kulkarni2023managementofhypertensive pages 2-3)

### 3.2 Retinal layers/structural phenotypes (OCT/OCTA era)
Cotton-wool spots correspond to ischemic lesions with **RNFL involvement**, and structural sequelae may persist with **RNFL thinning** and inner retinal layer changes (e.g., ganglion cell-inner plexiform layer complex). (marco2022aliteraturereview pages 6-7)

### 3.3 Distinguishing related entities (malignant hypertension)
Fundus lesions in malignant hypertension can be separated into hypertensive retinopathy vs choroidopathy vs optic neuropathy; optic disc edema maps to optic neuropathy rather than retinopathy. (kim2023hypertensiveretinopathy pages 1-2, marco2022aliteraturereview pages 4-6)

### Suggested HPO term mappings (ontology suggestions; not evidence-asserted)
* Retinal hemorrhage; cotton-wool spots (retinal nerve fiber layer infarcts); hard exudates; papilledema; macular edema; abnormal retinal vasculature/arteriolar narrowing/AV nicking.

---

## 4. Genetic/Molecular Information

### 4.1 Causal genes and pathogenic variants
HR is best characterized as a **complex phenotype/end-organ manifestation** of systemic hypertension rather than a monogenic disorder; no HR-specific causal genes or pathogenic variants were identified in the retrieved evidence.

### 4.2 Molecular mediators and pathways
Key mediators include endothelial dysfunction and barrier breakdown in severe states (kim2023hypertensiveretinopathy pages 2-3), and RAAS/angiotensin II-associated vasoconstriction/vasospasm with downstream vascular dysfunction in renal hypertension (wang2024octaevaluateschanges pages 6-7, wang2024octaevaluateschanges pages 9-10). A synthesis review also highlights angiotensin II–VEGF connections in HR pathophysiology. (marco2022aliteraturereview pages 2-4)

No omics (transcriptomic/proteomic/metabolomic/epigenomic) profiling evidence was identified.

---

## 5. Environmental Information
HR is driven primarily by systemic BP exposure and systemic vascular risk context. No toxin/pathogen causal triggers were identified in this run.

---

## 6. Mechanism / Pathophysiology (causal chain)

A useful mechanistic framework (synthesis review) divides HR into phases:

1. **Vasoconstrictive phase (acute BP elevation):** autoregulatory vasoconstriction/vasospasm → generalized/focal retinal arteriolar narrowing. (marco2022aliteraturereview pages 2-4)
2. **Sclerotic phase (chronic hypertension):** endothelial injury, intimal thickening, medial hyperplasia, hyaline degeneration → AV nicking and copper/silver wiring. (marco2022aliteraturereview pages 2-4)
3. **Exudative phase (severe/accelerated hypertension):** blood–retina barrier disruption and permeability → hemorrhages, hard exudates, cotton-wool spots, microaneurysms. (marco2022aliteraturereview pages 2-4)

In renal hypertension, RAAS activation and angiotensin II excess are emphasized as drivers of vasoconstriction/vasospasm and reduced retinal perfusion/vascular density on OCTA. (wang2024octaevaluateschanges pages 6-7, wang2024octaevaluateschanges pages 9-10)

Suggested GO/CL terms (ontology suggestions): endothelial cell dysfunction; regulation of blood vessel diameter; regulation of vascular permeability; oxidative stress response; retinal ganglion cell injury; pericyte/endothelial involvement.

---

## 7. Anatomical Structures Affected

* Retina and retinal microvasculature (arterioles/capillaries/venules) with inner retinal layer effects (RNFL, ganglion cell complex). (marco2022aliteraturereview pages 2-4, marco2022aliteraturereview pages 6-7)
* Choroid/RPE in hypertensive choroidopathy (choroidal ischemia/RPE lesions). (marco2022aliteraturereview pages 4-6, kim2023hypertensiveretinopathy pages 2-3)
* Optic nerve head in hypertensive optic neuropathy (disc hemorrhage/papilledema). (marco2022aliteraturereview pages 4-6, kim2023hypertensiveretinopathy pages 1-2)

---

## 8. Temporal Development

* Chronic course with remodeling signs (arteriolar narrowing, AV nicking, wiring) vs acute/severe presentations with exudative lesions and disc edema. (marco2022aliteraturereview pages 2-4, kulkarni2023managementofhypertensive pages 2-3)
* Staging via KWB grades 1–4. (kulkarni2023managementofhypertensive pages 2-3)
* OCTA-based 3-stage capillary sparsity/nonperfusion patterns proposed as staging surrogates in synthesis literature. (marco2022aliteraturereview pages 6-7)

---

## 9. Inheritance and Population

HR is complex/multifactorial; inheritance is not Mendelian in this evidence set.

### Epidemiology (recent quantitative evidence prioritized)
* **6–15%** prevalence in non-diabetic adults ≥40 years (noted as potentially underestimated). (wang2024octaevaluateschanges pages 6-7)
* In a CKD+hypertension cohort context, HR reported in **>70%** of non-diabetic hypertensive patients with CKD, with CKD severity linked to progression. (wang2024octaevaluateschanges pages 9-10)

### Malignant hypertension prevalence (related severe phenotype)
BIHS position document reports malignant hypertension prevalence approximately **1–2/100,000** in Caucasian populations and **7.3/100,000** in African American populations. (kulkarni2023managementofhypertensive pages 2-3)

---

## 10. Diagnostics

### 10.1 Ophthalmoscopy / fundus photography
Traditional grading systems (e.g., KWB; Wong–Mitchell) are limited by **subjectivity and interobserver variability**. (marco2022aliteraturereview pages 1-2, pinto2022arterialhypertensionand pages 2-3)

### 10.2 Quantitative retinal vascular metrics (photo-based)
Computer-based analysis improves reproducibility and enables follow-up using standardized measures such as **CRAE, CRVE, and AVR** from digital photographs. (pinto2022arterialhypertensionand pages 2-3)

### 10.3 OCT and OCTA
Synthesis literature highlights OCT as a **reproducible technique** for vessel measurements and OCTA as a rapid, noninvasive method for detecting microvascular changes (vessel density/perfusion density/FAZ changes) even without overt clinical HR. (marco2022aliteraturereview pages 4-6, marco2022aliteraturereview pages 6-7)

A 2024 renal-hypertension OCTA study illustrates practical OCTA implementation: SVP/DVP density differences across segmentation approaches and potential for early detection and progression monitoring. (wang2024octaevaluateschanges pages 1-2, wang2024octaevaluateschanges pages 9-10)

### 10.4 Standardization and QC (key implementation issue)
* **OSCAR-MP** (2023) provides consensus QC criteria for OCTA artifacts/quality and achieved high interrater agreement for rejecting poor-quality scans. (wicklein2023theoscarmpconsensus pages 1-2)
* A 2024 systematic review/meta-analysis emphasizes massive heterogeneity of OCTA analysis approaches and calls for standardized reporting and minimum datasets (e.g., parafoveal vessel density and FAZ area). (courtie2024opticalcoherencetomography pages 34-35)

---

## 11. Outcome / Prognosis

### Stroke/CVD associations (recent systematic review)
A 2024 systematic review of retinal imaging biomarkers for stroke risk reports that **retinopathy presence** is strongly associated with increased stroke risk; meta-analysis reports **HR 2.70 (p<0.0001)** for “retinopathy of any type.” (girach2024retinalimagingfor pages 7-8, girach2024retinalimagingfor pages 1-2)

BIHS notes severe retinal changes (KWB grades 3–4) reflect severe vascular permeability and poor prognosis in malignant hypertension contexts. (kulkarni2023managementofhypertensive pages 2-3)

---

## 12. Treatment

### 12.1 Core management
Primary therapy is **systemic blood pressure reduction and vascular risk management**, coordinated with primary care/internal medicine; fundus findings can guide intensity/urgency. (marco2022aliteraturereview pages 11-14)

The 2022 synthesis review states that grade III/IV retinopathy should be managed urgently and that fundus exam should be performed in suspected hypertensive emergencies to guide treatment intensity. (marco2022aliteraturereview pages 11-14)

### 12.2 Hypertensive crisis / malignant hypertension guidance (2023 BIHS)
BIHS emphasizes careful BP lowering to avoid hypoperfusion and ischemic complications; for uncomplicated malignant hypertension with eye changes alone, targets include: <200/120 mmHg within 24 h, <160/100 mmHg within 1 week, and <140/90 mmHg within 6–12 weeks. (kulkarni2023managementofhypertensive pages 7-8)

General emergency principle: reduce MAP no more than ~20–25% in first 6–24 hours. (kulkarni2023managementofhypertensive pages 7-8, kulkarni2023managementofhypertensive pages 5-7)

### 12.3 Ocular-directed adjuncts
The 2022 synthesis review notes intravitreal anti-VEGF antibodies have been reported to reduce macular edema/hemorrhages, but are not widely established as standard HR therapy. (marco2022aliteraturereview pages 11-14)

Suggested MAXO terms (ontology suggestions): antihypertensive therapy; emergency BP management; intensive monitoring/admission; fundus photography; OCT; OCTA; intravitreal anti-VEGF therapy (selected cases).

---

## 13. Prevention

* **Primary prevention:** prevent HR by controlling hypertension and improving medication adherence/escalation. (kulkarni2023managementofhypertensive pages 3-3)
* **Secondary prevention:** retinal imaging as a window for hypertension-mediated organ damage assessment; quantitative methods may support earlier detection than subjective grading. (pinto2022arterialhypertensionand pages 1-2, pinto2022arterialhypertensionand pages 2-3)

---

## 14. Other Species / Natural Disease
No comparative/veterinary HR evidence was identified in the retrieved set.

---

## 15. Model Organisms
No model organism resources specific to HR were identified in the retrieved set.

---

# Recent Developments and Real-World Implementations (2023–2024 emphasis)

## AI/ML applications
A 2024 IEEE Access review describes expanding use of CNN-based ML/DL methods for automated analysis of diabetic and hypertensive retinopathy, emphasizing improved accessibility and screening potential (with particular relevance to resource-limited settings). (urinatriana2024machinelearningand pages 16-17)

## Clinical trial implementations (real-world grading/measurement)
* **RetinAIcheck (CNN) for HR grading** (ClinicalTrials.gov NCT07471971; observational): trained on 30,000 specialist-relabeled fundus photographs; tested in 729 patients (1,401 eyes); grades HR by KWB classification; online resource: https://retinaai.sechenov.ru/. (NCT07471971 chunk 1)
* **Retinal blood flow measurement in HR** (ClinicalTrials.gov NCT01753648): stage 2–3 HR vs matched controls; endpoints include total retinal blood flow, vessel diameter, velocities, and oxygen saturation using Dynamic Vessel Analyzer and Fourier-domain OCT methods. (NCT01753648 chunk 1)

---

## Summary table (grading, mechanisms, key statistics)
| Domain | Subcategory | Finding / summary | Quantitative detail | Citation |
|---|---|---|---|---|
| Grading/signs | Keith-Wagener-Barker grade 3 | Severe hypertensive retinopathy with flame- or dot-shaped retinal hemorrhages, cotton-wool spots, hard exudates, and microaneurysms | Grade-defining lesion set | (kulkarni2023managementofhypertensive pages 2-3) |
| Grading/signs | Keith-Wagener-Barker grade 4 | Grade 3 changes plus bilateral papilledema; reflects malignant/severe hypertensive eye involvement | Grade 4 = papilledema added to grade 3 signs | (kulkarni2023managementofhypertensive pages 2-3) |
| Grading/signs | Classic chronic vascular signs | Generalized/focal arteriolar narrowing, arteriovenous nicking, and copper/silver wiring are classic hypertensive retinal vascular signs | Descriptive clinical signs | (marco2022aliteraturereview pages 2-4) |
| Grading/signs | Other classic retinal lesions | Flame-shaped and dot-blot hemorrhages, hard exudates, cotton-wool spots, and microaneurysms are repeatedly described as classic HR findings | Descriptive clinical signs | (marco2022aliteraturereview pages 2-4) |
| Mechanistic phases | Vasoconstrictive phase | Acute BP elevation triggers localized vasospasm and autoregulatory arteriolar constriction; clinically seen as generalized or focal arteriolar narrowing | Acute/early phase | (marco2022aliteraturereview pages 2-4, kim2023hypertensiveretinopathy pages 2-3) |
| Mechanistic phases | Sclerotic phase | Chronic hypertension causes endothelial injury, intimal thickening, medial hyperplasia, and hyaline degeneration; clinically maps to AV nicking and copper/silver wiring | Chronic structural remodeling phase | (marco2022aliteraturereview pages 2-4) |
| Mechanistic phases | Exudative phase | Severe hypertension disrupts the blood-retina barrier and increases vascular permeability, producing hemorrhages, hard exudates, cotton-wool spots, and microaneurysms | Advanced/severe phase | (marco2022aliteraturereview pages 2-4, kim2023hypertensiveretinopathy pages 2-3) |
| Mechanistic phases | Ischemic tissue injury | Retinal ischemia can persist after the edematous phase and is associated with inner retinal/RNFL thinning and microcirculatory dysfunction | Persistent structural injury after ischemic lesions | (marco2022aliteraturereview pages 6-7) |
| Mechanistic phases | RAAS-related mechanism | In renal hypertension, RAAS activation and excess angiotensin II promote vasoconstriction/vasospasm, arterial stiffness, reduced perfusion, and lower retinal vascular density | Mechanistic link to reduced OCTA vessel density | (wang2024octaevaluateschanges pages 6-7, wang2024octaevaluateschanges pages 9-10) |
| Quantitative data | HR prevalence in CKD + hypertension | In non-diabetic patients with CKD and hypertension, hypertensive retinopathy was reported in over 70% | >70% prevalence | (wang2024octaevaluateschanges pages 9-10) |
| Quantitative data | Malignant hypertension prevalence by ancestry | Position document reports malignant hypertension prevalence around 1–2/100,000 in Caucasian populations and 7.3/100,000 in African American populations | 1–2/100,000 vs 7.3/100,000 | (kulkarni2023managementofhypertensive pages 2-3) |
| Quantitative data | Stroke risk with retinopathy (any type) | Systematic review/meta-analysis found retinopathy presence strongly associated with future stroke risk | HR 2.70, p<0.0001 | (girach2024retinalimagingfor pages 7-8) |
| Quantitative data | Additional stroke-linked retinal features | Wider retinal venules, lower fractal dimension, increased arteriolar tortuosity, retinal emboli, and retinopathy were supported as stroke-risk markers; AV nicking/microaneurysms had weaker evidence | Qualitative strength-of-evidence summary | (girach2024retinalimagingfor pages 1-2) |


*Table: This table condenses the most useful disease-characteristic facts for hypertensive retinopathy: classic grading/signs, mechanism-to-phenotype mapping, and recent quantitative prognostic and epidemiologic data. It is useful as a quick reference for building a structured knowledge-base entry.*

---

## Direct abstract-supported statements (quotes)
* “Retinal imaging allows non-invasive assessment of the microvasculature.” (2024 stroke-risk systematic review) (girach2024retinalimagingfor pages 7-8)
* “To date, there are no validated consensus criteria for quality control (QC) of OCTA.” (2023 OSCAR-MP paper) (wicklein2023theoscarmpconsensus pages 1-2)
* “Patients with hypertensive emergencies, malignant hypertension and acute severe hypertension are managed heterogeneously in clinical practice.” (2023 BIHS position paper) (kulkarni2023managementofhypertensive pages 2-3)

---

## Gaps / limitations of this run
1. **ICD/MeSH/MONDO/OMIM/Orphanet IDs** were not available in the retrieved evidence texts; identifiers are therefore not asserted.
2. **Image retrieval:** attempts to retrieve and cite a cropped figure/table failed due to tool access errors; thus, no image citations are included.
3. **Genetic/omics:** no HR-specific GWAS/omics/epigenetic profiling evidence was identified in the retrieved set.

---

## Key URLs and publication dates (subset of cited sources)
* Kulkarni et al. *Journal of Human Hypertension* (Nov 2023): https://doi.org/10.1038/s41371-022-00776-9 (kulkarni2023managementofhypertensive pages 2-3)
* Wang et al. *Scientific Reports* (Nov 2024): https://doi.org/10.1038/s41598-024-68690-3 (wang2024octaevaluateschanges pages 9-10)
* Girach et al. *Journal of Neurology* (Mar 2024): https://doi.org/10.1007/s00415-023-12171-6 (girach2024retinalimagingfor pages 7-8)
* Wicklein et al. *Neurol Neuroimmunol Neuroinflamm* (Nov 2023): https://doi.org/10.1212/nxi.0000000000200169 (wicklein2023theoscarmpconsensus pages 1-2)
* Courtie et al. *Scientific Reports* (Apr 2024): https://doi.org/10.1038/s41598-024-54306-3 (courtie2024opticalcoherencetomography pages 34-35)
* Del Pinto et al. *Nutrients* (May 2022): https://doi.org/10.3390/nu14112200 (pinto2022arterialhypertensionand pages 1-2)
* Di Marco et al. *Eur Rev Med Pharmacol Sci* (Sep 2022): https://doi.org/10.26355/eurrev_202209_29742 (marco2022aliteraturereview pages 2-4)
* ClinicalTrials.gov NCT07471971 (resource): https://retinaai.sechenov.ru/ (NCT07471971 chunk 1)


References

1. (marco2022aliteraturereview pages 2-4): E. Di Marco, F. Aiello, M. Lombardo, M. Di Marino, F. Missiroli, R. Mancino, F. Ricci, C. Nucci, A. Noce, N. Di Daniele, and M. Cesareo. A literature review of hypertensive retinopathy: systemic correlations and new technologies. European review for medical and pharmacological sciences, 26 18:6424-6443, Sep 2022. URL: https://doi.org/10.26355/eurrev\_202209\_29742, doi:10.26355/eurrev\_202209\_29742. This article has 67 citations.

2. (kulkarni2023managementofhypertensive pages 2-3): Spoorthy Kulkarni, Mark Glover, Vikas Kapil, S. M. L. Abrams, Sarah Partridge, Terry McCormack, Peter Sever, Christian Delles, and Ian B. Wilkinson. Management of hypertensive crisis: british and irish hypertension society position document. Journal of Human Hypertension, 37:863-879, Nov 2023. URL: https://doi.org/10.1038/s41371-022-00776-9, doi:10.1038/s41371-022-00776-9. This article has 119 citations and is from a peer-reviewed journal.

3. (kim2023hypertensiveretinopathy pages 1-2): Ophthalmologica and Sohan Singh. Hypertensive retinopathy. Definitions, Jan 2020. URL: https://doi.org/10.1159/000309997, doi:10.1159/000309997. This article has 383 citations.

4. (marco2022aliteraturereview pages 4-6): E. Di Marco, F. Aiello, M. Lombardo, M. Di Marino, F. Missiroli, R. Mancino, F. Ricci, C. Nucci, A. Noce, N. Di Daniele, and M. Cesareo. A literature review of hypertensive retinopathy: systemic correlations and new technologies. European review for medical and pharmacological sciences, 26 18:6424-6443, Sep 2022. URL: https://doi.org/10.26355/eurrev\_202209\_29742, doi:10.26355/eurrev\_202209\_29742. This article has 67 citations.

5. (kim2023hypertensiveretinopathy pages 2-3): Ophthalmologica and Sohan Singh. Hypertensive retinopathy. Definitions, Jan 2020. URL: https://doi.org/10.1159/000309997, doi:10.1159/000309997. This article has 383 citations.

6. (wang2024octaevaluateschanges pages 6-7): Le Wang, Jun-Yi Wang, Cheng Chen, Min Kang, San-Hua Xu, Hong Wei, Qian Ling, Liang-Qi He, Jie Zou, Xu Chen, Ping Ying, Hui Huang, and Yi Shao. Octa evaluates changes in retinal microvasculature in renal hypertension patients. Scientific Reports, Nov 2024. URL: https://doi.org/10.1038/s41598-024-68690-3, doi:10.1038/s41598-024-68690-3. This article has 11 citations and is from a peer-reviewed journal.

7. (wang2024octaevaluateschanges pages 9-10): Le Wang, Jun-Yi Wang, Cheng Chen, Min Kang, San-Hua Xu, Hong Wei, Qian Ling, Liang-Qi He, Jie Zou, Xu Chen, Ping Ying, Hui Huang, and Yi Shao. Octa evaluates changes in retinal microvasculature in renal hypertension patients. Scientific Reports, Nov 2024. URL: https://doi.org/10.1038/s41598-024-68690-3, doi:10.1038/s41598-024-68690-3. This article has 11 citations and is from a peer-reviewed journal.

8. (marco2022aliteraturereview pages 1-2): E. Di Marco, F. Aiello, M. Lombardo, M. Di Marino, F. Missiroli, R. Mancino, F. Ricci, C. Nucci, A. Noce, N. Di Daniele, and M. Cesareo. A literature review of hypertensive retinopathy: systemic correlations and new technologies. European review for medical and pharmacological sciences, 26 18:6424-6443, Sep 2022. URL: https://doi.org/10.26355/eurrev\_202209\_29742, doi:10.26355/eurrev\_202209\_29742. This article has 67 citations.

9. (marco2022aliteraturereview pages 6-7): E. Di Marco, F. Aiello, M. Lombardo, M. Di Marino, F. Missiroli, R. Mancino, F. Ricci, C. Nucci, A. Noce, N. Di Daniele, and M. Cesareo. A literature review of hypertensive retinopathy: systemic correlations and new technologies. European review for medical and pharmacological sciences, 26 18:6424-6443, Sep 2022. URL: https://doi.org/10.26355/eurrev\_202209\_29742, doi:10.26355/eurrev\_202209\_29742. This article has 67 citations.

10. (pinto2022arterialhypertensionand pages 2-3): Rita Del Pinto, Giuseppe Mulè, Maria Vadalà, Caterina Carollo, Santina Cottone, Claudia Agabiti Rosei, Carolina De Ciuceis, Damiano Rizzoni, Claudio Ferri, and Maria Lorenza Muiesan. Arterial hypertension and the hidden disease of the eye: diagnostic tools and therapeutic strategies. Nutrients, 14:2200, May 2022. URL: https://doi.org/10.3390/nu14112200, doi:10.3390/nu14112200. This article has 31 citations.

11. (wang2024octaevaluateschanges pages 1-2): Le Wang, Jun-Yi Wang, Cheng Chen, Min Kang, San-Hua Xu, Hong Wei, Qian Ling, Liang-Qi He, Jie Zou, Xu Chen, Ping Ying, Hui Huang, and Yi Shao. Octa evaluates changes in retinal microvasculature in renal hypertension patients. Scientific Reports, Nov 2024. URL: https://doi.org/10.1038/s41598-024-68690-3, doi:10.1038/s41598-024-68690-3. This article has 11 citations and is from a peer-reviewed journal.

12. (wicklein2023theoscarmpconsensus pages 1-2): Rebecca Wicklein, Charmaine Yam, Christina Noll, Lilian Aly, Nicolas Banze, Eva Feodora Romahn, Elisabeth Wolf, Bernhard Hemmer, Frederike C. Oertel, Hanna Zimmermann, Philipp Albrecht, Marius Ringelstein, Carmen Baumann, Nikolaus Feucht, Josef Penkava, Joachim Havla, Jonathan A. Gernert, Christian Mardin, Eleni S. Vasileiou, Anneke Van Der Walt, Omar Al-Louzi, Sergio Cabello, Angela Vidal-Jordana, Julia Krämer, Heinz Wiendl, Jana Lizrova Preiningerova, Olga Ciccarelli, Elena Garcia-Martin, Veronika Kana, Peter A. Calabresi, Friedemann Paul, Shiv Saidha, Axel Petzold, Ahmed T. Toosy, and Benjamin Knier. The oscar-mp consensus criteria for quality assessment of retinal optical coherence tomography angiography. Neurology Neuroimmunology &amp; Neuroinflammation, Nov 2023. URL: https://doi.org/10.1212/nxi.0000000000200169, doi:10.1212/nxi.0000000000200169. This article has 35 citations.

13. (courtie2024opticalcoherencetomography pages 34-35): Ella Courtie, James Robert Moore Kirkpatrick, Matthew Taylor, Livia Faes, Xiaoxuan Liu, Ann Logan, Tonny Veenith, Alastair K. Denniston, and Richard J. Blanch. Optical coherence tomography angiography analysis methods: a systematic review and meta-analysis. Scientific Reports, Apr 2024. URL: https://doi.org/10.1038/s41598-024-54306-3, doi:10.1038/s41598-024-54306-3. This article has 18 citations and is from a peer-reviewed journal.

14. (girach2024retinalimagingfor pages 7-8): Zain Girach, Arni Sarian, Cynthia Maldonado-García, Nishant Ravikumar, Panagiotis I. Sergouniotis, Peter M. Rothwell, Alejandro F. Frangi, and Thomas H. Julian. Retinal imaging for the assessment of stroke risk: a systematic review. Journal of neurology, 271:2285-2297, Mar 2024. URL: https://doi.org/10.1007/s00415-023-12171-6, doi:10.1007/s00415-023-12171-6. This article has 40 citations and is from a domain leading peer-reviewed journal.

15. (girach2024retinalimagingfor pages 1-2): Zain Girach, Arni Sarian, Cynthia Maldonado-García, Nishant Ravikumar, Panagiotis I. Sergouniotis, Peter M. Rothwell, Alejandro F. Frangi, and Thomas H. Julian. Retinal imaging for the assessment of stroke risk: a systematic review. Journal of neurology, 271:2285-2297, Mar 2024. URL: https://doi.org/10.1007/s00415-023-12171-6, doi:10.1007/s00415-023-12171-6. This article has 40 citations and is from a domain leading peer-reviewed journal.

16. (marco2022aliteraturereview pages 11-14): E. Di Marco, F. Aiello, M. Lombardo, M. Di Marino, F. Missiroli, R. Mancino, F. Ricci, C. Nucci, A. Noce, N. Di Daniele, and M. Cesareo. A literature review of hypertensive retinopathy: systemic correlations and new technologies. European review for medical and pharmacological sciences, 26 18:6424-6443, Sep 2022. URL: https://doi.org/10.26355/eurrev\_202209\_29742, doi:10.26355/eurrev\_202209\_29742. This article has 67 citations.

17. (kulkarni2023managementofhypertensive pages 7-8): Spoorthy Kulkarni, Mark Glover, Vikas Kapil, S. M. L. Abrams, Sarah Partridge, Terry McCormack, Peter Sever, Christian Delles, and Ian B. Wilkinson. Management of hypertensive crisis: british and irish hypertension society position document. Journal of Human Hypertension, 37:863-879, Nov 2023. URL: https://doi.org/10.1038/s41371-022-00776-9, doi:10.1038/s41371-022-00776-9. This article has 119 citations and is from a peer-reviewed journal.

18. (kulkarni2023managementofhypertensive pages 5-7): Spoorthy Kulkarni, Mark Glover, Vikas Kapil, S. M. L. Abrams, Sarah Partridge, Terry McCormack, Peter Sever, Christian Delles, and Ian B. Wilkinson. Management of hypertensive crisis: british and irish hypertension society position document. Journal of Human Hypertension, 37:863-879, Nov 2023. URL: https://doi.org/10.1038/s41371-022-00776-9, doi:10.1038/s41371-022-00776-9. This article has 119 citations and is from a peer-reviewed journal.

19. (kulkarni2023managementofhypertensive pages 3-3): Spoorthy Kulkarni, Mark Glover, Vikas Kapil, S. M. L. Abrams, Sarah Partridge, Terry McCormack, Peter Sever, Christian Delles, and Ian B. Wilkinson. Management of hypertensive crisis: british and irish hypertension society position document. Journal of Human Hypertension, 37:863-879, Nov 2023. URL: https://doi.org/10.1038/s41371-022-00776-9, doi:10.1038/s41371-022-00776-9. This article has 119 citations and is from a peer-reviewed journal.

20. (pinto2022arterialhypertensionand pages 1-2): Rita Del Pinto, Giuseppe Mulè, Maria Vadalà, Caterina Carollo, Santina Cottone, Claudia Agabiti Rosei, Carolina De Ciuceis, Damiano Rizzoni, Claudio Ferri, and Maria Lorenza Muiesan. Arterial hypertension and the hidden disease of the eye: diagnostic tools and therapeutic strategies. Nutrients, 14:2200, May 2022. URL: https://doi.org/10.3390/nu14112200, doi:10.3390/nu14112200. This article has 31 citations.

21. (urinatriana2024machinelearningand pages 16-17): Miguel Alberto Urina-Triana, Marlon Alberto Piñeres-Melo, Mirary Mantilla-Morrón, Shariq Butt-Aziz, Luisa Galeano-Muñoz, Sumera Naz, and Paola Patricia Ariza-Colpas. Machine learning and ai approaches for analyzing diabetic and hypertensive retinopathy in ocular images: a literature review. IEEE Access, 12:54590-54607, Jan 2024. URL: https://doi.org/10.1109/access.2024.3378277, doi:10.1109/access.2024.3378277. This article has 31 citations and is from a peer-reviewed journal.

22. (NCT07471971 chunk 1):  Assessment of Hypertensive Retinopathy Using Convolutional Neural Network "RetinAIcheck". I.M. Sechenov First Moscow State Medical University. 2021. ClinicalTrials.gov Identifier: NCT07471971

23. (NCT01753648 chunk 1): Gerhard Garhofer. Non-invasive Measurement of Retinal Blood Flow Based on Vessel Analysis and Fourier Domain Optical Coherence Tomography in Patients With Hypertensive Retinopathy. Medical University of Vienna. 2015. ClinicalTrials.gov Identifier: NCT01753648

## Artifacts

- [Edison artifact artifact-00](Hypertensive_Retinopathy-deep-research-falcon_artifacts/artifact-00.md)