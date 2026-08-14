---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T04:59:42.925051'
end_time: '2026-07-31T05:10:34.413033'
duration_seconds: 651.49
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Congenital Myasthenic Syndrome 6
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 11
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Congenital_Myasthenic_Syndrome_6-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Myasthenic Syndrome 6
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Congenital Myasthenic Syndrome 6** covering all of the
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
- **Disease Name:** Congenital Myasthenic Syndrome 6
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Congenital Myasthenic Syndrome 6** covering all of the
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


# Congenital Myasthenic Syndrome 6: Comprehensive Disease-Characteristics Report

**Scope and nomenclature note.** In current disease-specific literature, **congenital myasthenic syndrome 6 (CMS6)** means **CHAT-associated congenital myasthenic syndrome with episodic apnea (CMS-EA)**. It should not be confused with **COLQ-related endplate acetylcholinesterase deficiency**, which has a different mechanism and treatment profile. The evidence base is exceptionally small—approximately 50 patients had been reported by 2024—and consists predominantly of families, case reports, and small case series rather than controlled trials. The findings below therefore describe reported cases, not population-level certainties. (pugliese2023presynapticcongenitalmyasthenic pages 7-9, murtazina2024mildphenotypeof pages 1-2)

The following table provides a knowledge-base-ready summary.

| domain | curated finding | quantitative evidence | suggested ontology terms |
|---|---|---:|---|
| Identity / identifiers | Congenital myasthenic syndrome 6 (CMS6) corresponds to **CHAT-associated congenital myasthenic syndrome with episodic apnea (CMS-EA)**; recent disease-specific literature explicitly states “CMS-EA, also known as CMS type 6.” MONDO for the exact subtype was not confirmed from available evidence; broader congenital myasthenic syndrome is MONDO_0018940. MeSH for the broader class: *Myasthenic Syndromes, Congenital* (D020294). (murtazina2024mildphenotypeof pages 1-2, NCT01203592 chunk 1, OpenTargets Search: congenital myasthenic syndrome-CHAT) | ~50 patients reported by 2024 (murtazina2024mildphenotypeof pages 1-2) | MONDO: congenital myasthenic syndrome (MONDO_0018940, broader); MeSH: D020294; disease synonym candidates: “CMS-EA”, “CHAT-associated CMS” |
| Gene / inheritance | Cause is biallelic pathogenic variants in **CHAT** encoding choline acetyltransferase; disorder is a **presynaptic** CMS and is **autosomal recessive**. Most known variants are missense. (murtazina2024mildphenotypeof pages 1-2, pugliese2023presynapticcongenitalmyasthenic pages 7-9, OpenTargets Search: congenital myasthenic syndrome-CHAT) | CHAT accounts for ~4–5% of all CMS cases (pugliese2023presynapticcongenitalmyasthenic pages 7-9) | HGNC gene: CHAT; GO: acetylcholine biosynthetic process (suggested), chemical synaptic transmission (suggested) |
| Molecular mechanism | ChAT catalyzes resynthesis of acetylcholine from choline and acetyl-CoA in the nerve terminal; impaired ChAT reduces presynaptic ACh resynthesis, causing failure of sustained neuromuscular transmission, especially under repetitive activity or stress. (ohno2023clinicalandpathologic pages 4-6, pugliese2023presynapticcongenitalmyasthenic pages 7-9, murtazina2024mildphenotypeof pages 1-2) | Qualitative; no disease-wide effect size available | GO: acetylcholine biosynthetic process; GO: synaptic vesicle cycle; GO: neuromuscular synaptic transmission; CL: motor neuron; UBERON: neuromuscular junction |
| Major phenotype: apneic crises / respiratory involvement | Classical CMS6 commonly presents in infancy with apnea, respiratory insufficiency, and episodic respiratory crises; crises may be severe or fatal. (pugliese2023presynapticcongenitalmyasthenic pages 7-9, murtazina2024mildphenotypeof pages 1-2) | Literature summary in CHAT cohort: apneic crises 86% (36/42), ventilation 63% (26/41), tracheostomy 25% (9/36), respiratory insufficiency 48% (20/42), apnea 28% (12/42) (murtazina2024mildphenotypeof pages 5-6) | HPO: Apnea; Respiratory insufficiency; Recurrent respiratory infections/crises (suggested) |
| Major phenotype: ocular / bulbar | Ocular findings and bulbar weakness are common in typical disease, though absent in the 2024 mild series. (murtazina2024mildphenotypeof pages 5-6, murtazina2024mildphenotypeof pages 1-2) | Ptosis 88% (36/41), strabismus/ophthalmoparesis 23% (9/39), bulbar weakness 28% (12/42) (murtazina2024mildphenotypeof pages 5-6) | HPO: Ptosis; Ophthalmoparesis; Strabismus; Dysphagia; Dysarthria |
| Major phenotype: limb weakness / fatigability | Generalized, proximal, or exercise-induced fatigable weakness is typical; a mild phenotype may present mainly with exercise intolerance and leg fatigability without apnea or ocular signs. (pugliese2023presynapticcongenitalmyasthenic pages 7-9, murtazina2024mildphenotypeof pages 1-2, murtazina2024mildphenotypeof pages 5-6) | General muscle weakness 45% (17/38), proximal weakness 67% (26/39), fatigable leg weakness 96% (27/28); in 2024 mild series 5/5 had leg fatigability and 0/5 had apnea or ptosis (murtazina2024mildphenotypeof pages 5-6, murtazina2024mildphenotypeof pages 1-2) | HPO: Muscle weakness; Proximal muscle weakness; Exercise intolerance; Fatigability |
| Neurodevelopment / CNS features | Some patients, especially severe early-onset cases, may have delayed motor milestones, intellectual disability, loss of consciousness, or seizures; recent mild cases had normal neurologic status aside from fatigability. (pugliese2023presynapticcongenitalmyasthenic pages 7-9, murtazina2024mildphenotypeof pages 1-2) | Psychomotor delay 57% (21/37) in summarized literature; 0/5 in 2024 mild cohort (murtazina2024mildphenotypeof pages 5-6) | HPO: Global developmental delay; Seizure; Loss of consciousness |
| Temporal development / course | Typical onset is birth or early infancy for severe disease; mild phenotype can begin at 1–2.5 years. Course is often fluctuating; the 2024 mild series showed no progression over several years. (pugliese2023presynapticcongenitalmyasthenic pages 7-9, murtazina2024mildphenotypeof pages 1-2, murtazina2024mildphenotypeof pages 5-6) | Mild cohort onset 1–2.5 years, 5/5 fluctuating without progression (murtazina2024mildphenotypeof pages 1-2, murtazina2024mildphenotypeof pages 5-6) | HPO: Infantile onset; Childhood onset; Fluctuating weakness |
| Triggers / gene-environment interaction | Infection, fever, and other stressful conditions can provoke sudden respiratory crises in infancy; cold may aggravate weakness; prolonged exertion unmasks fatigability. These are **triggers/modifiers**, not primary causes. (pugliese2023presynapticcongenitalmyasthenic pages 7-9, murtazina2024mildphenotypeof pages 5-6) | Qualitative; no pooled effect estimates available | HPO: Cold-induced myasthenic symptoms (suggested); Exercise-induced weakness |
| Pathogenic variants | 2024 mild series identified four novel missense SNVs and one recurrent severe-associated missense variant; example variants include **c.404C>G p.(Pro135Arg)** (likely pathogenic) and **c.1061C>T p.(Thr354Met)**. Three novel SNVs were VUS at publication. (murtazina2024mildphenotypeof pages 5-6) | 5 patients from 4 families; 4 novel missense SNVs; 1 recurrent severe-associated missense variant (murtazina2024mildphenotypeof pages 5-6) | Sequence Ontology: missense_variant; nonsense_variant (reported in one family context) |
| Diagnostics: electrophysiology | Standard low-frequency RNS may be normal; decrement often appears after prolonged high-frequency stimulation or exercise. In the pediatric mild series, modified 3 Hz peroneal RNS after 15–20 min exercise was informative. (pugliese2023presynapticcongenitalmyasthenic pages 7-9, murtazina2024mildphenotypeof pages 5-6, NCT01203592 chunk 1) | Standard 3 Hz decrement >10% in only a small percentage; prolonged 10 Hz for 5 min positive in 9/10; modified post-exercise 3 Hz showed 22–37% decrement improving after 3–4 min rest; in literature 44% (14/32) had increased decrement at 3 Hz after 20 s exercise (murtazina2024mildphenotypeof pages 5-6) | LOINC/SNOMED not confirmed; HPO: Abnormal repetitive nerve stimulation; MAXO: Electromyography |
| Diagnostics: genetic testing | Accurate diagnosis requires genetic testing because clinical/electrophysiologic features alone do not identify the defective molecule. Exome/genome sequencing captured CHAT variants in recent series; trial inclusion criteria for CMS required seronegativity to AChR and MuSK plus decremental EMG. (OpenTargets Search: congenital myasthenic syndrome-CHAT, murtazina2024mildphenotypeof pages 1-2, NCT01203592 chunk 1) | WES mean coverage ×76.1 in 2024 series; WGS average on-target coverage 30× (murtazina2024mildphenotypeof pages 1-2) | MAXO: Sequence analysis of gene panel / exome / genome (suggested); MeSH: Myasthenic Syndromes, Congenital |
| Differential diagnosis / distinction | Important distinction: **CMS6 is CHAT-related**, not COLQ-related endplate AChE deficiency. COLQ-CMS is the subtype where AChE inhibitors are usually contraindicated and β-adrenergic agonists often first-line; that treatment rule should not be misapplied to CMS6. (murtazina2024mildphenotypeof pages 1-2, ohno2023clinicalandpathologic pages 4-6) | Not quantitative | Differential terms: COLQ-related congenital myasthenic syndrome; autoimmune myasthenia gravis |
| Treatment | First-line therapy is usually **acetylcholinesterase inhibitors**; if response is limited/absent, **3,4-diaminopyridine** may be added, and some patients may receive **salbutamol/albuterol** combinations. Evidence is mainly case based. (murtazina2024mildphenotypeof pages 5-6, pugliese2023presynapticcongenitalmyasthenic pages 7-9) | Response to AChE inhibitors ~73% (27/37); response to 3,4-DAP 71% (5/7); in 2024 mild series, 2 children improved clearly on 3,4-DAP, 1 had only slight benefit on salbutamol+pyridostigmine, and 1 had severe adverse effects to 3,4-DAP (murtazina2024mildphenotypeof pages 5-6, murtazina2024mildphenotypeof pages 1-2) | CHEBI/drugs: pyridostigmine, amifampridine/3,4-diaminopyridine, salbutamol/albuterol; MAXO: Acetylcholinesterase inhibitor therapy; Adrenergic agonist therapy; Ventilatory support |
| Clinical trials / real-world implementation | Broad CMS interventional studies exist for albuterol and ephedrine, but they were not specific to CHAT/CMS6; ephedrine trial targeted COLQ-deficient kindred. Real-world use in CMS is genotype-guided. (NCT01203592 chunk 1, NCT00541216 chunk 1, ohno2023clinicalandpathologic pages 4-6) | Albuterol study NCT01203592 enrolled 21; ephedrine study NCT00541216 planned 15 and was COLQ-specific (NCT01203592 chunk 1, NCT00541216 chunk 1) | ClinicalTrials.gov: NCT01203592; NCT00541216 |
| Prognosis / outcomes | Prognosis is variable. Severe neonatal/infantile disease can be life-threatening, with fatal infancy cases reported; however, a mild non-apneic phenotype appears to have favorable medium-term outcome without progression. (pugliese2023presynapticcongenitalmyasthenic pages 7-9, murtazina2024mildphenotypeof pages 5-6) | Wheelchair dependency 25% (7/28) in summarized literature; 0/5 in 2024 mild cohort (murtazina2024mildphenotypeof pages 5-6) | HPO: Respiratory failure; Wheelchair dependence; Favorable prognosis (not an HPO term; narrative only) |
| Epidemiology / population | CMS overall is rare and likely underdiagnosed; pediatric prevalence estimates for all CMS vary by region. Subtype-specific prevalence for CMS6 was not available from retrieved sources. (ohno2023clinicalandpathologic pages 4-6, murtazina2024mildphenotypeof pages 1-2) | CMS prevalence under age 18: UK average 9.2/million (range 2.8–14.8), Brazil 1.8/million, Slovenia 22.2/million, Spain 1.8/million (ohno2023clinicalandpathologic pages 4-6) | MONDO: congenital myasthenic syndrome (broader); note: CMS6-specific prevalence unavailable |
| Anatomy / cell types | Primary site is the **presynaptic motor nerve terminal** at the **neuromuscular junction** of skeletal muscle; clinically affects ocular, bulbar, respiratory, axial, and limb muscles. Central nervous system expression of CHAT may help explain occasional CNS manifestations. (pugliese2023presynapticcongenitalmyasthenic pages 7-9, murtazina2024mildphenotypeof pages 1-2, ohno2023clinicalandpathologic pages 4-6) | Qualitative | UBERON: neuromuscular junction; skeletal muscle; diaphragm; extraocular muscle; CL: motor neuron; skeletal muscle fiber |
| Model organisms / natural disease | Models include Chat-targeted mouse knockout (heterozygotes normal; homozygous pups die at birth with flaccid paralysis and absent spontaneous/nerve-evoked postsynaptic potentials), zebrafish **bajan** and **chatatk64** mutants (reduced movement and synaptic responses), and a naturally occurring **Old Danish Pointing Dog** CHAT mutation causing exercise-induced fatigability. A 2024 AAV9 CHAT mouse gene therapy study was identified as emerging preclinical work, but detailed results were not available in retrieved text. (pugliese2023presynapticcongenitalmyasthenic pages 7-9) | Mouse homozygotes die at birth; zebrafish homozygotes show absent coiling and reduced touch response; affected dogs tolerate only ~5–30 min walking/running before weakness (pugliese2023presynapticcongenitalmyasthenic pages 7-9) | NCBI Taxon suggestions: Mus musculus, Danio rerio, Canis lupus familiaris; GO: neuromuscular synaptic transmission |
| Data provenance / evidence level | Evidence is derived from **aggregated disease-level resources**, **recent reviews**, **case series/case reports**, and **trial registry entries**, not EHR-only datasets. Many subtype-specific claims remain based on small case numbers. (OpenTargets Search: congenital myasthenic syndrome-CHAT, murtazina2024mildphenotypeof pages 1-2, NCT01203592 chunk 1, NCT00541216 chunk 1) | Highest disease-specific 2024 cohort size in retrieved evidence: n=5; historical total ~50 cases reported (murtazina2024mildphenotypeof pages 1-2) | Evidence type labels: human clinical, review, model organism, trial registry |


*Table: This table summarizes high-value, citable knowledge-base facts for Congenital Myasthenic Syndrome 6, resolved as CHAT-associated CMS with episodic apnea. It emphasizes disease identity, genotype-mechanism links, quantitative phenotypes, diagnostics, treatment, and model systems while clearly marking broader-class versus subtype-specific evidence.*

## 1. Disease information

CMS6 is an inherited **presynaptic neuromuscular-junction disorder** caused by biallelic pathogenic variants in **CHAT**, the gene encoding choline O-acetyltransferase (ChAT). Deficient acetylcholine resynthesis impairs sustained neuromuscular transmission. The classical phenotype comprises neonatal or infantile fatigable weakness with recurrent, potentially fatal apneic crises, although a non-apneic, childhood-onset phenotype is now well established. (pugliese2023presynapticcongenitalmyasthenic pages 7-9, murtazina2024mildphenotypeof pages 1-2)

**Names and identifiers**

- Preferred names: *congenital myasthenic syndrome 6*; *congenital myasthenic syndrome with episodic apnea*; *CMS-EA*; *CHAT-associated congenital myasthenic syndrome*; *presynaptic CMS due to choline acetyltransferase deficiency*.
- OMIM: commonly catalogued as **CMS with episodic apnea, 254210**; CHAT gene entry **118490**. These identifiers should be checked against the live OMIM release before database ingestion.
- MeSH: **D020294, Myasthenic Syndromes, Congenital**, a broader class explicitly used in ClinicalTrials.gov indexing. (NCT01203592 chunk 1)
- MONDO: the retrieved Open Targets record maps the broader disease to **MONDO:0018940, congenital myasthenic syndrome**. An exact CMS6 MONDO record was not resolved by the available search and should not be inferred from similarly numbered CMS subtypes. (OpenTargets Search: congenital myasthenic syndrome-CHAT)
- ICD-10/ICD-11: no retrieved evidence established a unique subtype code; coding generally falls under congenital/other specified myasthenic syndromes or neuromuscular-junction disorders. A local coding authority should verify the current national modification.
- Orphanet: an exact subtype identifier was not securely established in the retrieved evidence.

The evidence is principally **aggregated disease-level literature plus individual-patient case series**, not an EHR-derived cohort. The 2024 study used WES/WGS and detailed phenotyping of five individuals from four families. (murtazina2024mildphenotypeof pages 1-2)

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal factor

CMS6 is a monogenic, autosomal-recessive disorder caused by **germline biallelic CHAT variants**. Most reported variants are missense, although truncating and splice-altering alleles may occur. It is not caused by autoantibodies, infection, toxin exposure, diet, or lifestyle. (pugliese2023presynapticcongenitalmyasthenic pages 7-9, murtazina2024mildphenotypeof pages 1-2)

### Genetic risk

The principal risk is inheritance of two pathogenic or likely pathogenic CHAT alleles. Siblings of an affected person have, under standard autosomal-recessive assumptions, a 25% recurrence probability when both parents are heterozygous carriers. Consanguinity can increase the probability of homozygosity, but no CMS6-specific estimate was retrieved. Sex does not determine inheritance.

No validated modifier gene, protective allele, polygenic risk score, penetrance estimate, or CMS6-specific carrier frequency was found. Clinical variability—including mild and severe disease associated with the recurrent **c.1061C>T, p.(Thr354Met)** allele—indicates that genotype alone does not fully predict severity. (murtazina2024mildphenotypeof pages 5-6)

### Environmental and physiologic modifiers

Infection, fever, and other physiologic stress can precipitate acute respiratory or bulbar crises; cold may exacerbate weakness, and prolonged exercise can unmask a neuromuscular decrement. These are **phenotypic triggers**, not causes. (pugliese2023presynapticcongenitalmyasthenic pages 7-9, murtazina2024mildphenotypeof pages 5-6)

No established diet, exercise regimen, toxin avoidance measure, medication, or genetic factor prevents disease occurrence. Practical protection is instead directed toward preventing crises: prompt infection treatment, avoidance of unmonitored respiratory depressants or neuromuscular blockers, an emergency respiratory plan, and adherence to effective symptomatic therapy.

## 3. Phenotypes

Reported frequencies below derive from a literature aggregation of approximately 42 patients and have variable denominators; ascertainment was biased toward severe CMS-EA. (murtazina2024mildphenotypeof pages 5-6)

- **Apneic crises/respiratory disease:** apneic crises 36/42 (86%); ventilation 26/41 (63%); respiratory insufficiency 20/42 (48%); explicitly coded apnea 12/42 (28%); tracheostomy 9/36 (25%). Onset is usually neonatal or infantile; episodes fluctuate and can be infection-, fever-, or stress-provoked. Suggested HPO: *Apnea*, *Episodic respiratory distress*, *Respiratory insufficiency*, *Neonatal respiratory distress*. (pugliese2023presynapticcongenitalmyasthenic pages 7-9, murtazina2024mildphenotypeof pages 5-6)
- **Ocular disease:** ptosis 36/41 (88%); strabismus or ophthalmoparesis 9/39 (23%). Severity is variable and fluctuating. Suggested HPO: **HP:0000508 Ptosis**, *Ophthalmoparesis*, **HP:0000486 Strabismus**. (murtazina2024mildphenotypeof pages 5-6)
- **Muscle weakness/fatigability:** fatigable leg weakness 27/28 (96%), proximal weakness 26/39 (67%), and general weakness 17/38 (45%). The cardinal functional effect is reduced walking, running, stair-climbing, or sustained activity. Suggested HPO: **HP:0001324 Muscle weakness**, **HP:0003701 Proximal muscle weakness**, **HP:0003546 Exercise intolerance**, *Fatigability*. (murtazina2024mildphenotypeof pages 5-6)
- **Bulbar involvement:** 12/42 (28%), including swallowing or speech difficulty. Suggested HPO: **HP:0002015 Dysphagia**, **HP:0001260 Dysarthria**, *Bulbar weakness*. (pugliese2023presynapticcongenitalmyasthenic pages 7-9, murtazina2024mildphenotypeof pages 5-6)
- **Development/CNS:** psychomotor delay was reported in 21/37 (57%); severe cases may include impaired consciousness, tonic–clonic seizures, or intellectual disability. These findings may reflect CHAT expression in central cholinergic neurons, hypoxic injury during crises, or both; causality is not fully resolved. Suggested HPO: **HP:0001263 Global developmental delay**, **HP:0001250 Seizure**, *Loss of consciousness*. (pugliese2023presynapticcongenitalmyasthenic pages 7-9, murtazina2024mildphenotypeof pages 5-6)
- **Mobility:** wheelchair dependence occurred in 7/28 (25%) in historical reports. Suggested HPO: *Loss of ambulation* or *Wheelchair dependence*. (murtazina2024mildphenotypeof pages 5-6)

### Mild phenotype—2024 development

The 2024 case series described five patients whose onset was at 1–2.5 years and whose sole or initial manifestation was exercise-induced leg fatigability. All five lacked apnea, respiratory insufficiency, ptosis, and ophthalmoparesis and showed a fluctuating but non-progressive course over several years. The authors’ abstract states: **“we propose the existence of a mild phenotype characterized by the absence of apneic episodes.”** (murtazina2024mildphenotypeof pages 1-2)

No CMS6-specific EQ-5D, SF-36, PROMIS, or utility-weight study was found. Quality-of-life impairment should therefore be represented through respiratory risk, activity limitation, schooling/work effects, treatment burden, and possible ventilatory or wheelchair dependence rather than an unsupported numerical score.

## 4. Genetic and molecular information

**Causal gene:** **CHAT**, chromosome 10q11.23; protein: choline O-acetyltransferase. Open Targets identifies CHAT as **ENSG00000070748** and associates it with the broader congenital myasthenic syndrome category. (OpenTargets Search: congenital myasthenic syndrome-CHAT)

The 2024 series identified four novel missense SNVs. **c.404C>G, p.(Pro135Arg)** was classified as likely pathogenic because another missense substitution at the same residue had been reported; three other novel missense variants remained VUS pending stronger functional evidence. The recurrent **c.1061C>T, p.(Thr354Met)** variant had previously been associated with infantile onset and apneic crises, yet also occurred in milder families, underscoring incomplete genotype–phenotype predictability. (murtazina2024mildphenotypeof pages 5-6)

Variants are constitutional/germline, not somatic cancer mutations. The expected functional category is loss or reduction of ChAT expression, stability, catalytic activity, or substrate kinetics, producing inadequate acetylcholine resynthesis under sustained demand. Population allele frequencies were not available in the retrieved text and must be obtained variant-by-variant from the current gnomAD release. Likewise, ClinVar classifications should be recorded per accession and review status rather than generalized from publication assertions.

No reproducible modifier genes, disease-specific methylation signature, chromatin abnormality, aneuploidy, translocation, or recurrent pathogenic copy-number alteration has been established. A chromosomal microarray cannot exclude CMS6, although exon-level CNV analysis remains appropriate when sequencing finds only one pathogenic allele.

## 5. Environmental information

There is no environmental, occupational, lifestyle, toxic, or infectious etiology. Infection and fever are clinically important **crisis triggers**, cold may aggravate fatigability, and exertion reveals limited presynaptic acetylcholine reserve. Smoking, alcohol, diet, pollution, and radiation have no demonstrated causal role. Pathogens are therefore not disease agents, and the disorder is neither communicable nor zoonotic. (pugliese2023presynapticcongenitalmyasthenic pages 7-9, murtazina2024mildphenotypeof pages 5-6)

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic lesion:** biallelic CHAT loss-of-function or hypomorphic variants.
2. **Protein defect:** reduced ChAT quantity or catalytic function.
3. **Biochemical defect:** inadequate conversion of choline plus acetyl-CoA to acetylcholine in the motor-nerve terminal.
4. **Cellular defect:** acetylcholine stores and replenishment become insufficient during repeated motor-neuron firing.
5. **Synaptic defect:** quantal transmission falls below the postsynaptic safety margin, often only after sustained stimulation.
6. **Tissue/organ manifestations:** fatigable ocular, bulbar, limb, and respiratory-muscle weakness.
7. **Clinical crisis:** fever, infection, stress, or sustained activity raises demand and may trigger abrupt apnea, hypoxemia, loss of consciousness, seizures, or death. (ohno2023clinicalandpathologic pages 4-6, pugliese2023presynapticcongenitalmyasthenic pages 7-9)

The 2023 comprehensive review describes the normal step directly: **“Choline acetyltransferase (ChAT, CHAT) in the nerve terminal generates ACh from up taken choline and acetyl-CoA.”** (ohno2023clinicalandpathologic pages 4-6)

This is primarily a **neurotransmitter-biosynthesis and synaptic-transmission disorder**, not an inflammatory myopathy, autoimmune disease, primary mitochondrial disorder, degenerative motor-neuron disease, or structural ACh-receptor channelopathy. Secondary muscle atrophy, developmental delay, or hypoxic injury may occur downstream.

Suggested annotations include GO *acetylcholine biosynthetic process*, *neuromuscular synaptic transmission*, *chemical synaptic transmission*, *synaptic vesicle cycle*, and *regulation of neurotransmitter levels*; GO cellular components *presynaptic active zone*, *axon terminal*, *synaptic vesicle*, and *neuromuscular junction*; CL **motor neuron** and **skeletal muscle fiber**.

No validated CMS6-specific transcriptomic, proteomic, metabolomic, lipidomic, epigenomic, single-cell, spatial-transcriptomic, or integrated multi-omics signature is available. ChAT activity and electrophysiologic transmission are mechanistically relevant but are not validated circulating biomarkers.

## 7. Anatomical structures affected

The primary lesion is at cholinergic **motor-neuron presynaptic terminals** of the neuromuscular junction. Functionally affected tissues include skeletal muscle innervated by somatic motor neurons—especially the diaphragm and other respiratory muscles, extraocular and levator muscles, bulbar/pharyngeal musculature, proximal limb muscles, and distal leg muscles. Laterality is generally bilateral rather than focal. (pugliese2023presynapticcongenitalmyasthenic pages 7-9, murtazina2024mildphenotypeof pages 5-6)

Suggested UBERON concepts: *neuromuscular junction*, *skeletal muscle organ*, *diaphragm*, *extraocular muscle*, *pharyngeal muscle*, and *limb muscle*. Suggested GO cellular components are *presynaptic membrane*, *axon terminus*, *synaptic vesicle*, and *cytosol*, where ChAT catalysis occurs.

## 8. Temporal development

The classical severe form begins at birth or in early infancy, sometimes abruptly with apnea. The milder form may become evident in early childhood after sustained walking or exercise. Disease is chronic and lifelong, but manifestations fluctuate. Severe neonatal disease may cause fatal crises, whereas the five 2024 mild cases remained non-progressive for several years. (pugliese2023presynapticcongenitalmyasthenic pages 7-9, murtazina2024mildphenotypeof pages 5-6, murtazina2024mildphenotypeof pages 1-2)

There is no accepted staging system. Clinically useful states are: baseline compensated weakness; exertional deterioration; bulbar/respiratory exacerbation; and acute apneic crisis requiring ventilation. Early diagnosis is a critical intervention window because respiratory support and genotype-appropriate medication may prevent hypoxic injury or death. True spontaneous molecular remission is not expected, although symptom-free intervals and treatment-induced functional improvement occur.

## 9. Inheritance and population

Inheritance is **autosomal recessive**, with variable expressivity. Penetrance for individuals with two definitively pathogenic alleles is presumed high but has not been quantified. Anticipation is not expected. No CHAT-specific germline-mosaicism rate, founder allele, sex ratio, ethnic enrichment, or carrier-frequency estimate was established by the retrieved evidence. (pugliese2023presynapticcongenitalmyasthenic pages 7-9, murtazina2024mildphenotypeof pages 1-2)

CHAT-CMS represents approximately **4–5% of all CMS cases**, but only about 50 CMS-EA patients had been reported by 2024. (pugliese2023presynapticcongenitalmyasthenic pages 7-9, murtazina2024mildphenotypeof pages 1-2)

Subtype-specific incidence and prevalence are unknown. For context—not as a CMS6 estimate—the pediatric prevalence of all CMS was 9.2 per million in the UK, with regional estimates of 2.8–14.8 per million; published estimates were 1.8 per million in Brazil, 22.2 per million in Slovenia, and 1.8 per million in Spain. Investigators considered these underestimates because patients remain undiagnosed. (ohno2023clinicalandpathologic pages 4-6)

## 10. Diagnostics

### Clinical and electrophysiologic diagnosis

Suspect CMS6 in neonatal/infantile episodic apnea, especially with ptosis, ophthalmoparesis, bulbar weakness, hypotonia, or fatigability; also consider it in children with isolated exertional leg weakness. Standard 3-Hz repetitive nerve stimulation may be falsely normal. Prolonged 10-Hz stimulation for five minutes was positive in 9/10 reported patients. In the 2024 mild cohort, 3-Hz peroneal stimulation after 15 minutes of exercise produced a **22–37% CMAP decrement**, which improved after 3–4 minutes’ rest. (murtazina2024mildphenotypeof pages 5-6)

Single-fiber EMG can demonstrate increased jitter/blocking but may be difficult in children. Routine CK, imaging, muscle biopsy, and histopathology are not diagnostic and may be normal or nonspecific. Pulmonary-function testing, pulse oximetry, sleep/ventilation assessment, swallowing assessment, and ECG/cardiovascular review before sympathomimetic therapy are clinically useful.

### Genetic testing

A CMS/NMJ panel containing **CHAT** is efficient when the phenotype is recognizable. WES or WGS is appropriate when panel testing is negative, the presentation is atypical, or CNV/noncoding analysis is needed. The 2024 series used WES at mean ×76.1 coverage and WGS at approximately ×30 coverage. Pathogenicity assessment should incorporate phase, segregation, population frequency, computational evidence, RNA studies for splice variants, and functional ChAT assays where feasible. (murtazina2024mildphenotypeof pages 1-2)

CMA, karyotyping, FISH, mitochondrial testing, and repeat-expansion testing are not first-line for isolated CMS6. RNA sequencing may resolve splice variants but is not an established routine assay. Prenatal and preimplantation testing become possible after familial variants are established.

### Differential diagnosis

Major alternatives include other presynaptic CMS—especially **SLC5A7** and **SLC18A3** disorders—RAPSN-associated CMS, congenital AChR deficiency, DOK7-CMS, COLQ-CMS, congenital myopathies, spinal muscular atrophy, mitochondrial disease, infantile epilepsy or central apnea, botulism, and autoimmune myasthenia gravis. AChR/MuSK seronegativity supports congenital rather than autoimmune myasthenia but is not by itself diagnostic. The albuterol study required a typical history, AChR/MuSK seronegativity, and decremental EMG. (NCT01203592 chunk 1)

## 11. Outcome and prognosis

No reliable 5- or 10-year survival rate, life-expectancy estimate, or CMS6-specific mortality rate exists. Historical severe cases include death during infantile apneic crises; ventilation, tracheostomy, developmental disability, impaired mobility, and hypoxic complications drive morbidity. Conversely, mild non-apneic disease can remain stable for years with preserved routine neurologic function. (pugliese2023presynapticcongenitalmyasthenic pages 7-9, murtazina2024mildphenotypeof pages 5-6)

Likely adverse prognostic features are neonatal onset, recurrent apnea, need for early ventilation, severe bulbar weakness, delayed diagnosis, and poor drug response. Favorable features include isolated exertional fatigability, no respiratory events, and treatment responsiveness. These are clinical observations, not validated prediction-model variables or biomarkers.

## 12. Treatment

### Genotype-guided pharmacotherapy

**Pyridostigmine**, an acetylcholinesterase inhibitor, is generally first-line for CHAT-CMS because prolonging acetylcholine action can partly compensate for reduced synthesis. Historical response was reported in 27/37 patients (73%). If response is incomplete, **amifampridine/3,4-diaminopyridine**, which prolongs the presynaptic action potential and increases calcium-dependent acetylcholine release, may be added; 5/7 reported patients (71%) responded. (ohno2023clinicalandpathologic pages 4-6, murtazina2024mildphenotypeof pages 5-6)

In the 2024 mild series, two children improved clearly on 3,4-diaminopyridine, while one experienced severe adverse effects and later had slight benefit from salbutamol plus pyridostigmine. Treatment must therefore be initiated and titrated by a neuromuscular specialist, with cardiac and seizure-risk consideration for amifampridine and cardiovascular monitoring for β-agonists. (murtazina2024mildphenotypeof pages 1-2)

**Important subtype distinction:** acetylcholinesterase inhibitors are contraindicated or harmful in many **COLQ-CMS** patients, but this rule does **not** apply automatically to CHAT/CMS6. The recent CMS review explicitly reserves that contraindication for COLQ- and LAMB2-related disease. (ohno2023clinicalandpathologic pages 4-6)

### Acute and supportive management

Apneic crisis requires immediate airway support, bag-mask ventilation or mechanical ventilation as indicated, oxygenation and CO₂ monitoring, treatment of infection/fever, and avoidance of diagnostic delay. Families should have a written emergency plan and resuscitation training when recurrent apnea is a risk. Supportive care may include noninvasive ventilation, tracheostomy in refractory disease, feeding/swallowing support, physical and occupational therapy, and school/activity accommodations.

Suggested MAXO annotations include *genetic testing*, *electromyography*, *acetylcholinesterase inhibitor therapy*, *potassium-channel blocker therapy*, *adrenergic agonist therapy*, *noninvasive positive-pressure ventilation*, *mechanical ventilation*, *tracheostomy*, *physical therapy*, *occupational therapy*, and *genetic counseling*.

### Trials and emerging therapy

No controlled trial specific to CHAT-CMS6 was identified. **NCT01203592**, an open-label Phase 1 albuterol study, enrolled 21 heterogeneous CMS patients; it was not CHAT-specific. **NCT00541216** tested ephedrine in a COLQ-deficient kindred and should not be represented as CMS6 evidence. (NCT01203592 chunk 1, NCT00541216 chunk 1)

A 2024 report of **AAV9-mediated CHAT gene therapy in ChAT-deficient mice** represents an important preclinical development, not an approved or clinically validated treatment. No human gene-, RNA-, or cell-therapy implementation for CMS6 was identified.

## 13. Prevention

Primary prevention by lifestyle or vaccination is impossible because CMS6 is inherited. Reproductive prevention options after molecular diagnosis include carrier testing of relatives, partner testing, prenatal diagnosis, and preimplantation genetic testing. Population newborn screening is unavailable, but targeted neonatal testing is justified in an at-risk pregnancy or symptomatic neonate.

Secondary prevention comprises early molecular diagnosis, family cascade testing, respiratory monitoring, and early effective therapy. Tertiary prevention includes infection and fever management, crisis planning, vaccination according to routine schedules to reduce preventable respiratory illness, ventilatory/feeding support, rehabilitation, and avoidance of medications or anesthesia practices that may worsen neuromuscular transmission. Vaccines do not prevent the genetic disease itself.

## 14. Other species and natural disease

A naturally occurring CHAT-associated myasthenic disorder occurs in the **Old Danish Pointing Dog** (*Canis lupus familiaris*, NCBI Taxonomy 9615). Affected dogs carry a CHAT valine-to-methionine substitution and develop fore- and hind-limb fatigability after only 5–30 minutes of walking or running; prolonged 3-Hz stimulation induces a decrement. This provides strong comparative evidence for conserved activity-dependent failure of cholinergic transmission. (pugliese2023presynapticcongenitalmyasthenic pages 7-9)

There is no zoonotic transmission. Veterinary breed and VBO identifiers should be obtained from live VBO/OMIA records before ingestion.

## 15. Model organisms

- **Mouse (*Mus musculus*, Taxon 10090):** heterozygous Chat-targeted mice appear normal, whereas homozygous knockout pups die at birth with flaccid paralysis, absent spontaneous and nerve-evoked postsynaptic potentials, excessive nerve-terminal branching, altered synapse distribution, widened endplates, thin muscles, and prematurely enlarged AChR-rich sites. The null model captures severe transmission failure but is more lethal than most human hypomorphic disease. (pugliese2023presynapticcongenitalmyasthenic pages 7-9)
- **Zebrafish (*Danio rerio*, Taxon 7955):** *bajan* carries a Chat intron-2 splice-acceptor mutation; *chatatk64* carries p.Ser102Arg. Homozygotes lack normal coiling, have reduced touch responses, and show markedly reduced spontaneous and evoked synaptic currents. These models permit developmental imaging and rapid therapeutic screening. (pugliese2023presynapticcongenitalmyasthenic pages 7-9)
- **Drosophila:** reduced ChAT activity and impaired synaptic transmission at low temperature provide a mechanistic model for cold-sensitive weakness, although an invertebrate NMJ does not reproduce human respiratory crises directly. (murtazina2024mildphenotypeof pages 5-6)
- **Dog:** the natural Old Danish Pointing Dog disorder recapitulates exertional fatigability and activity-dependent electrophysiologic decrement, making it translationally relevant. (pugliese2023presynapticcongenitalmyasthenic pages 7-9)

## Evidence assessment and current research priorities

The most important 2023–2024 advance is recognition that “episodic apnea” is not obligatory: CHAT disease spans lethal neonatal apnea through isolated childhood exercise intolerance. The 2024 series also showed that exercise-conditioned RNS can reveal abnormalities missed by routine testing. These findings favor **phenotype expansion, exertion-provoked electrophysiology, and broad genetic testing** rather than exclusion of CHAT because apnea is absent. (murtazina2024mildphenotypeof pages 5-6, murtazina2024mildphenotypeof pages 1-2)

Major gaps are CMS6-specific prevalence, prospective natural history, standardized patient-reported outcomes, variant-level functional assays, validated prognostic markers, controlled comparative treatment trials, and human gene-therapy safety data. Expert reviews consequently emphasize genotype-guided treatment and molecular confirmation because clinical and electrophysiologic findings alone cannot reliably identify the affected CMS molecule. (ohno2023clinicalandpathologic pages 4-6)

### Key recent sources

1. Murtazina A, et al. **Mild phenotype of CHAT-associated congenital myasthenic syndrome: case series.** *Frontiers in Pediatrics*. Published **18 January 2024**. DOI/URL: https://doi.org/10.3389/fped.2024.1280394. (murtazina2024mildphenotypeof pages 5-6, murtazina2024mildphenotypeof pages 1-2)
2. Pugliese A, et al. **Presynaptic Congenital Myasthenic Syndromes: Understanding Clinical Phenotypes through In vivo Models.** *Journal of Neuromuscular Diseases*. Published **September 2023**. DOI/URL: https://doi.org/10.3233/JND-221646. (pugliese2023presynapticcongenitalmyasthenic pages 7-9)
3. Ohno K, et al. **Clinical and Pathologic Features of Congenital Myasthenic Syndromes Caused by 35 Genes—A Comprehensive Review.** *International Journal of Molecular Sciences*. Published **February 2023**. DOI/URL: https://doi.org/10.3390/ijms24043730. (ohno2023clinicalandpathologic pages 4-6)
4. ClinicalTrials.gov. **NCT01203592: Efficacy of Albuterol in the Treatment of Congenital Myasthenic Syndromes.** First posted **16 September 2010**; completed August 2013. https://clinicaltrials.gov/study/NCT01203592. (NCT01203592 chunk 1)

**Evidence-type labels:** Murtazina et al. is human clinical case-series evidence; Pugliese et al. and Ohno et al. are authoritative reviews integrating human, in vitro, and model-organism studies; the NCT records are trial-registry evidence. Exact PMID values were not exposed in the retrieved records and are therefore not supplied rather than risked as unverified identifiers.

References

1. (pugliese2023presynapticcongenitalmyasthenic pages 7-9): Alessia Pugliese, Stephen H. Holland, Carmelo Rodolico, Hanns Lochmüller, and Sally Spendiff. Presynaptic congenital myasthenic syndromes: understanding clinical phenotypes through in vivo models. Journal of Neuromuscular Diseases, 10:731-759, Sep 2023. URL: https://doi.org/10.3233/jnd-221646, doi:10.3233/jnd-221646. This article has 22 citations and is from a peer-reviewed journal.

2. (murtazina2024mildphenotypeof pages 1-2): Aysylu Murtazina, Artem Borovikov, Andrey Marakhonov, Artem Sharkov, Inna Sharkova, Alena Mirzoyan, Sviatlana Kulikova, Ralina Ganieva, Viktoriia Zabnenkova, Oksana Ryzhkova, Sergey Nikitin, Elena Dadali, and Sergey Kutsev. Mild phenotype of chat-associated congenital myasthenic syndrome: case series. Frontiers in Pediatrics, Jan 2024. URL: https://doi.org/10.3389/fped.2024.1280394, doi:10.3389/fped.2024.1280394. This article has 4 citations.

3. (NCT01203592 chunk 1): Andrew Engel. Efficacy of Albuterol in the Treatment of Congenital Myasthenic Syndromes. Mayo Clinic. 2010. ClinicalTrials.gov Identifier: NCT01203592

4. (OpenTargets Search: congenital myasthenic syndrome-CHAT): Open Targets Query (congenital myasthenic syndrome-CHAT, 4 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (ohno2023clinicalandpathologic pages 4-6): K. Ohno, B. Ohkawara, Xinming Shen, D. Selcen, and A. Engel. Clinical and pathologic features of congenital myasthenic syndromes caused by 35 genes—a comprehensive review. International Journal of Molecular Sciences, Feb 2023. URL: https://doi.org/10.3390/ijms24043730, doi:10.3390/ijms24043730. This article has 132 citations.

6. (murtazina2024mildphenotypeof pages 5-6): Aysylu Murtazina, Artem Borovikov, Andrey Marakhonov, Artem Sharkov, Inna Sharkova, Alena Mirzoyan, Sviatlana Kulikova, Ralina Ganieva, Viktoriia Zabnenkova, Oksana Ryzhkova, Sergey Nikitin, Elena Dadali, and Sergey Kutsev. Mild phenotype of chat-associated congenital myasthenic syndrome: case series. Frontiers in Pediatrics, Jan 2024. URL: https://doi.org/10.3389/fped.2024.1280394, doi:10.3389/fped.2024.1280394. This article has 4 citations.

7. (NCT00541216 chunk 1):  Ephedrine for the Treatment of Congenital Myasthenia. Hadassah Medical Organization. 2007. ClinicalTrials.gov Identifier: NCT00541216

## Artifacts

- [Edison artifact artifact-00](Congenital_Myasthenic_Syndrome_6-deep-research-falcon_artifacts/artifact-00.md)