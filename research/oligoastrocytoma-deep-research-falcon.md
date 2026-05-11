---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-11T09:01:02.096172'
end_time: '2026-05-11T09:28:00.999244'
duration_seconds: 1618.9
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Oligoastrocytoma
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 57
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Oligoastrocytoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Oligoastrocytoma** covering all of the
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
- **Disease Name:** Oligoastrocytoma
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Oligoastrocytoma** covering all of the
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


## Comprehensive Disease Characteristics Report: Oligoastrocytoma

### Executive summary (current understanding)
Oligoastrocytoma is a historical, morphology-based “mixed” diffuse glioma diagnosis that has been largely eliminated from routine classification because tumors with mixed oligodendroglial/astrocytic histology typically segregate into either **astrocytoma, IDH-mutant** or **oligodendroglioma, IDH-mutant and 1p/19q-codeleted** when molecular testing is performed. WHO CNS5 (2021) explicitly emphasizes molecular diagnostics to reassign “poorly defined entities (eg, oligoastrocytomas …) to more objectively defined types” and lists only three adult-type diffuse glioma types (astrocytoma IDH-mutant; oligodendroglioma IDH-mutant/1p19q-codeleted; glioblastoma IDH-wildtype). (louis2021the2021who pages 15-16, horbinski2022clinicalimplicationsof pages 2-3)

| Entity / concept | WHO 2016/2021 status | Defining molecular features | Prognosis / epidemiology highlights | Standard treatment / 2023–2024 advance |
|---|---|---|---|---|
| **Oligoastrocytoma (historical mixed glioma)** | Historically used for diffuse gliomas with mixed astrocytic/oligodendroglial morphology; WHO 2016 largely removed it, retaining the term only for rare unresolved cases; WHO 2021 adult diffuse gliomas are instead assigned to molecularly defined entities, with NOS/NEC labels if workup is incomplete or unclassifiable (horbinski2022clinicalimplicationsof pages 1-2, louis2021the2021who pages 15-16, horbinski2022clinicalimplicationsof pages 2-3) | Mixed histology alone is no longer sufficient; molecular testing is required to reassign most tumors to **astrocytoma, IDH-mutant** or **oligodendroglioma, IDH-mutant and 1p/19q-codeleted** (reuss2023updatesonthe pages 1-2, perez2021theevolvingclassification pages 1-2, horbinski2022clinicalimplicationsof pages 2-3) | Historical survival statistics are hard to interpret because many legacy “oligoastrocytomas” are now redistributed into molecular classes; contemporary population statistics should therefore be read via reclassified astrocytoma/oligodendroglioma cohorts rather than the old label (louis2021the2021who pages 15-16, pinson2024epidemiologyandsurvival pages 2-3) | No modern disease-specific regimen because the entity is obsolete in routine classification; management follows the reassigned molecular entity (horbinski2022clinicalimplicationsof pages 1-2, horbinski2022clinicalimplicationsof pages 2-3) |
| **Astrocytoma, IDH-mutant** | One of the 3 WHO 2021 adult-type diffuse glioma types; all IDH-mutant diffuse astrocytic tumors are grouped into a single type and graded CNS WHO 2–4 (louis2021the2021who pages 15-16, antonelli2022adulttypediffuse pages 1-2) | **IDH1/2 mutation** with **no whole-arm 1p/19q codeletion**; typically **ATRX loss** and **TP53 alteration**; **CDKN2A/B homozygous deletion** upgrades to grade 4; TERT promoter mutation uncommon (~9.2% in one 2024 cohort) (whitfield2022classificationofadult‐type pages 4-6, martin2023fromtheoryto pages 2-4, antonelli2022adulttypediffuse pages 2-4, lee2024prognosticimpactof pages 1-2) | Belgium registry 2017–2019: 3-year survival **86.0%** for grade 2 and **75.7%** for grade 3 IDH-mutant astrocytoma; grade 4 IDH-mutant astrocytoma median OS **25.9 months** (pinson2024epidemiologyandsurvival pages 1-2). TERTp mutation was not prognostic within A-IDHm alone in a 2024 cohort (p=0.268) (lee2024prognosticimpactof pages 1-2) | Maximal safe resection; observation may be reasonable for selected low-risk grade 2 cases after gross total resection; otherwise postoperative radiochemotherapy. For grade 2 disease, **RT+PCV** is standard based on RTOG 9802; temozolomide alone appears probably inferior to RT in IDH-mutant astrocytoma. For grade 3 disease, **RT followed by 12 cycles TMZ** is standard (CATNON). Progressive disease remains difficult, with limited clearly effective options beyond re-operation, re-irradiation, and chemotherapy (kessler2023conventionalandemerging pages 2-4, kessler2023conventionalandemerging pages 6-7, segura2023seomgeinoclinicalguidelines pages 4-5, vazsalgado2024seomgeinoclinicalguidelines pages 4-5) |
| **Oligodendroglioma, IDH-mutant and 1p/19q-codeleted** | One of the 3 WHO 2021 adult-type diffuse glioma types; replaces most tumors historically called oligodendroglioma or mixed oligoastrocytoma when molecularly confirmed (louis2021the2021who pages 15-16, horbinski2022clinicalimplicationsof pages 2-3, antonelli2022adulttypediffuse pages 1-2) | **IDH1/2 mutation + whole-arm 1p/19q codeletion** is defining; usually **ATRX retained**, **TP53 wild-type pattern**, frequent **TERT promoter mutation** (~94.1% in a 2024 cohort), recurrent **CIC** and **FUBP1** mutations; NOTCH1 mutation may worsen OS (li2024clinicalsequencingreveals pages 1-2, whitfield2022classificationofadult‐type pages 4-6, martin2023fromtheoryto pages 4-6, lee2024prognosticimpactof pages 1-2) | Belgium registry 2017–2019: oligodendroglioma incidence about **0.52/100,000 person-years**; 3-year survival **93.4%** for grade 2 and **64.2%** for grade 3, with median survival not reached in available follow-up (pinson2024epidemiologyandsurvival pages 3-4). CBTRUS 2017–2021: oligodendroglioma 5-year relative survival **96.0%** overall and 10-year relative survival **92.9%** overall (price2024cbtrusstatisticalreport pages 70-72) | Maximal safe resection plus risk-adapted adjuvant therapy. For grade 2/high-risk disease, **RT+PCV** is standard; for grade 3 disease, randomized trials (RTOG 9402, EORTC 26951) support **RT+PCV**, approximately doubling OS in codeleted tumors. Temozolomide is easier to administer but has not proven equivalent to PCV in this setting (kessler2023conventionalandemerging pages 2-4, kessler2023conventionalandemerging pages 6-7, segura2023seomgeinoclinicalguidelines pages 4-5, horbinski2022clinicalimplicationsof pages 4-5) |
| **Key registry-level epidemiology context** | Modern epidemiology increasingly depends on molecular reclassification rather than legacy histology (pinson2024epidemiologyandsurvival pages 2-3, pinson2024epidemiologyandsurvival pages 1-2) | Belgium registry reclassified 2,233 adult diffuse gliomas by WHO 2021 molecular scheme; full molecular status available for **67.1%** of cases (pinson2024epidemiologyandsurvival pages 1-2) | Belgium 2017–2019: overall adult diffuse glioma age-standardized incidence **8.55/100,000 person-years**; grade 4 lesions **6.72/100,000** (pinson2024epidemiologyandsurvival pages 1-2). CBTRUS 2017–2021: all primary malignant + nonmalignant CNS tumors **25.34/100,000**, malignant tumors **6.89/100,000**; malignant brain/CNS tumor 5-year relative survival **35.7%** overall (price2024cbtrusstatisticalreport pages 70-72) | These data are most useful for contextualizing how rare modern oligodendroglioma/IDH-mutant astrocytoma subsets sit within the broader diffuse glioma burden (price2024cbtrusstatisticalreport pages 70-72, pinson2024epidemiologyandsurvival pages 1-2) |
| **Notable 2023–2024 targeted advance: vorasidenib (INDIGO)** | Not specific to historical oligoastrocytoma, but highly relevant to the IDH-mutant diffuse gliomas that replaced it (mellinghoff2023vorasidenibinidh1 pages 1-3) | Oral, brain-penetrant dual **mutant IDH1/2 inhibitor**; trial enrolled residual/recurrent grade 2 IDH-mutant astrocytoma or oligodendroglioma after surgery only (mellinghoff2023vorasidenibinidh1 pages 1-3, mellinghoff2023vorasidenibinidh1 pages 3-5) | INDIGO phase 3 (NCT04164901): median PFS **27.7 vs 11.1 months** for vorasidenib vs placebo; HR for progression/death **0.39**; HR for time to next intervention **0.26**. Grade ≥3 ALT elevation occurred in **9.6%** vs **0%** with placebo; grade ≥3 adverse events were more frequent with vorasidenib overall (mellinghoff2023vorasidenibinidh1 pages 1-3, mellinghoff2023vorasidenibinidh1 pages 6-8) | Provides the first major targeted systemic option that can delay radiotherapy/chemotherapy in selected untreated grade 2 IDH-mutant glioma. Guidelines now recognize IDH inhibitors as emerging/important additions, while open questions remain for higher-grade or previously treated disease (mellinghoff2023vorasidenibinidh1 pages 1-3, vazsalgado2024seomgeinoclinicalguidelines pages 1-3) |


*Table: This table summarizes how the historical diagnosis oligoastrocytoma has been replaced by molecularly defined adult diffuse glioma entities, with key molecular markers, prognosis, epidemiology, and treatment implications. It is useful for translating legacy terminology into current WHO 2021 clinical and research practice.*

### 1. Disease information

#### 1.1 What is the disease?
- **Historical definition:** “Oligoastrocytoma” referred to diffusely infiltrating gliomas with mixed oligodendroglial and astrocytic morphologic features. (horbinski2022clinicalimplicationsof pages 1-2, horbinski2022clinicalimplicationsof pages 2-3)
- **Current concept:** Modern WHO-aligned practice treats “oligoastrocytoma” as largely obsolete; mixed-appearing tumors are expected to be molecularly classifiable as either IDH-mutant astrocytoma (typically IDH+TP53+ATRX constellation) or oligodendroglioma (IDH mutation + whole-arm 1p/19q codeletion, often with TERT promoter mutation). (reuss2023updatesonthe pages 1-2, horbinski2022clinicalimplicationsof pages 1-2, horbinski2022clinicalimplicationsof pages 2-3)

#### 1.2 Key identifiers (what is available in the evidence)
Because WHO now discourages use of “oligoastrocytoma” as a distinct biological entity, contemporary resources increasingly encode the disease under molecularly defined entities rather than a standalone diagnosis. Nonetheless, registry coding and pathology datasets still contain oligoastrocytoma codes:
- **ICD-O morphology code (dataset table):** “Oligoastrocytoma, NOS” and “Anaplastic oligoastrocytoma, NOS” listed with **ICD-O 9382/3** in a CNS tumor reporting dataset. (brandner2020standardsanddatasets pages 25-27)
- **SEER/registry recode context:** an updated SEER histology recode aligned to WHO 2016-era changes includes a “mixed glioma/oligoastrocytoma” mapping consistent with **ICD-O-3 9421/3** in the excerpted table; and notes the recode reflects WHO 2016 and was effective in registry analyses beginning ~2018. (forjaz2021anupdatedhistology pages 4-4)

**Not available from retrieved evidence:** MONDO ID, MeSH unique identifier, ICD-10/ICD-11 code, OMIM, Orphanet identifier.

#### 1.3 Common synonyms / alternative names
- Mixed glioma; mixed oligodendroglial–astrocytic tumor; oligoastrocytoma NOS; anaplastic oligoastrocytoma (historical). (horbinski2022clinicalimplicationsof pages 1-2, brandner2020standardsanddatasets pages 25-27)

#### 1.4 Evidence provenance
- Classification statements are derived from **aggregated disease-level resources** (WHO CNS5 summary; Nature Reviews Neurology implications review). (louis2021the2021who pages 15-16, horbinski2022clinicalimplicationsof pages 1-2)
- Epidemiology/survival statements include **population-based registry resources** (Belgian Cancer Registry; CBTRUS). (pinson2024epidemiologyandsurvival pages 1-2, price2024cbtrusstatisticalreport pages 70-72)

### 2. Etiology

#### 2.1 Disease causal factors (mechanistic; molecular drivers)
In contemporary practice, tumors historically labeled oligoastrocytoma are reclassified into causal/molecular categories:
- **Astrocytoma, IDH-mutant:** typically shows an “IDH/TP53/ATRX” molecular constellation. (reuss2023updatesonthe pages 1-2, whitfield2022classificationofadult‐type pages 4-6)
- **Oligodendroglioma, IDH-mutant and 1p/19q-codeleted:** defined by **IDH mutation plus whole-arm 1p/19q codeletion**; frequently has **TERT promoter mutation** and recurrent **CIC** and **FUBP1** alterations. (whitfield2022classificationofadult‐type pages 4-6, li2024clinicalsequencingreveals pages 1-2, martin2023fromtheoryto pages 4-6)

#### 2.2 Risk factors (human epidemiology)
Evidence in the retrieved corpus is strongest at the “general glioma/malignant brain tumor” level rather than oligoastrocytoma-specific:
- **Ionizing radiation:** A 2023 JAMA review states that “Prior exposure to ionizing radiation to the CNS… is a risk factor for brain tumors.” (schaff2023glioblastomaandother pages 3-4)
- **Atopy/allergies and infections (associations):** The same JAMA review reports that “A history of atopic conditions… and a history of varicella-zoster virus infection are associated with lower glioma risk.” (schaff2023glioblastomaandother pages 3-4)
- **Lifestyle/metabolic factors (recent prospective evidence):** In a large prospective Norwegian cohort (CONOR; 160,938 participants; 2,877,646 person-years; 319 incident gliomas), there were no associations between glioma risk and physical activity, alcohol, smoking, marital status, diabetes, hypertension, or metabolic syndrome; LDL showed an inverse association in men (HR per category 0.84; 95% CI 0.74–0.96). (gheorghiu2024lifestyleandmetabolic pages 1-2, gheorghiu2024lifestyleandmetabolic pages 3-5)

#### 2.3 Protective factors
- Evidence in this retrieval suggests **atopic conditions** and **varicella-zoster virus infection** are associated with **lower glioma risk** (observational association). (schaff2023glioblastomaandother pages 3-4)

#### 2.4 Gene–environment interactions
Not specifically identified for oligoastrocytoma in the retrieved evidence. Current etiologic understanding for diffuse glioma emphasizes molecular drivers and immune-related epidemiologic associations rather than established GxE mechanisms. (schaff2023glioblastomaandother pages 3-4)

### 3. Phenotypes

#### 3.1 Common clinical phenotypes (glioma-level; applicable to tumors historically labeled oligoastrocytoma)
A 2023 JAMA review provides symptom frequencies for malignant brain tumors:
- “Symptoms of malignant brain tumors include **headache (50%)**, **seizures (20%–50%)**, **neurocognitive impairment (30%–40%)**, and **focal neurologic deficits (10%–40%)**.” (schaff2023glioblastomaandother pages 1-3)
- It further notes: “Up to **74% of patients with lower-grade gliomas** present with seizures.” (schaff2023glioblastomaandother pages 3-4)

**Suggested HPO terms (examples):**
- Seizures: HP:0001250
- Headache: HP:0002315
- Cognitive impairment: HP:0100543
- Focal neurological deficit (broad): HP:0007325 (Focal neurological sign)

#### 3.2 Age of onset, severity, progression, frequency
- These diffuse gliomas are typically adult tumors; registry cohorts show diagnosis in adulthood with substantial survival differences by molecular subtype (see Outcomes/Prognosis). (pinson2024epidemiologyandsurvival pages 1-2)

#### 3.3 Quality-of-life impact
- Quality-of-life impact is implied by high seizure burden and neurocognitive impairment frequencies in malignant brain tumors, but QoL instrument-specific statistics (EQ-5D/SF-36/PROMIS) were not retrieved. (schaff2023glioblastomaandother pages 1-3)

### 4. Genetic / molecular information

#### 4.1 Causal genes / defining alterations
- **IDH1/IDH2** mutations define IDH-mutant diffuse gliomas and are central to classification; IDH1 R132H is the most common IDH mutation and detectable by IHC; noncanonical variants also occur. (martin2023fromtheoryto pages 2-4, antonelli2022adulttypediffuse pages 2-4)
- **1p/19q codeletion** (whole-arm) defines oligodendroglioma when co-occurring with IDH mutation. (whitfield2022classificationofadult‐type pages 4-6, martin2023fromtheoryto pages 4-6)
- **ATRX** loss and **TP53** alterations strongly support astrocytoma IDH-mutant and can obviate 1p/19q testing in many settings. (whitfield2022classificationofadult‐type pages 4-6, martin2023fromtheoryto pages 2-4)
- **CDKN2A/B homozygous deletion** is a molecular grading criterion upgrading IDH-mutant astrocytoma to grade 4 regardless of histology. (whitfield2022classificationofadult‐type pages 4-6, martin2023fromtheoryto pages 2-4)
- **TERT promoter** mutation: in a 2024 cohort (n=528 adult-type diffuse gliomas) TERTp mutations were found in **94.1%** of oligodendrogliomas, **66.3%** of IDH-wildtype glioblastomas, and **9.2%** of IDH-mutant astrocytomas. (lee2024prognosticimpactof pages 1-2)
- **CIC, FUBP1, NOTCH1**: oligodendrogliomas are characterized by alterations in CIC, TERTp, FUBP1, and NOTCH1; NOTCH1 mutations were associated with worse OS in one sequencing cohort. (li2024clinicalsequencingreveals pages 1-2)

#### 4.2 Somatic vs germline
- The defining alterations described above are characteristic **somatic tumor** alterations used for integrated diagnosis in neuropathology. (martin2023fromtheoryto pages 2-4, whitfield2022classificationofadult‐type pages 4-6)

#### 4.3 Epigenetics
- The retrieved evidence supports epigenetic relevance indirectly through IDH mutation’s diagnostic role and use of methylation profiling in modern classification, but detailed, oligoastrocytoma-specific methylation signatures were not retrieved. (reuss2023updatesonthe pages 1-2)

### 5. Environmental information
- No oligoastrocytoma-specific environmental exposures were retrieved.
- For gliomas/malignant brain tumors broadly, the best-supported environmental risk factor in this evidence set is **prior ionizing radiation exposure to the CNS**. (schaff2023glioblastomaandother pages 3-4)

### 6. Mechanism / pathophysiology (integrated causal chain)
Because “oligoastrocytoma” is not a modern biological entity, mechanisms are best described for the two molecularly defined replacement entities.

#### 6.1 Replacement-mechanism framework
1. **Initiating oncogenic event (upstream):** IDH1/2 mutation establishes an IDH-mutant diffuse glioma lineage. (reuss2023updatesonthe pages 1-2)
2. **Lineage specification (midstream):**
   - **Astrocytic lineage:** IDH + TP53 + ATRX molecular constellation. (reuss2023updatesonthe pages 1-2)
   - **Oligodendroglial lineage:** IDH + 1p/19q whole-arm codeletion (often + TERTp). (reuss2023updatesonthe pages 1-2)
3. **Grade progression (downstream):** additional molecular events can drive more aggressive behavior; for example, CDKN2A/B homozygous deletion supports grade 4 assignment in IDH-mutant astrocytoma. (whitfield2022classificationofadult‐type pages 4-6)
4. **Clinical manifestations:** seizures, headache, cognitive impairment, and focal deficits result from cortical involvement and infiltrative growth. (schaff2023glioblastomaandother pages 1-3)

**Suggested GO biological process terms (examples):**
- Regulation of cell proliferation: GO:0042127
- DNA repair (broad): GO:0006281
- Cell differentiation: GO:0030154

**Suggested Cell Ontology (CL) terms (examples; likely involved cell types):**
- Astrocyte: CL:0000127
- Oligodendrocyte precursor cell: CL:0002453 (often hypothesized as cells-of-origin for some gliomas; not directly evidenced here)
- Microglial cell: CL:0000129 (tumor microenvironment; not directly evidenced here)

### 7. Anatomical structures affected
- Primary organ/system: **central nervous system**, especially the brain (adult-type diffuse gliomas). (louis2021the2021who pages 15-16)

**Suggested UBERON terms (examples):**
- Brain: UBERON:0000955
- Cerebral cortex: UBERON:0000956

### 8. Temporal development
- Course is typically chronic/progressive for diffuse gliomas; grade and molecular subtype strongly influence progression and survival in real-world registries. (pinson2024epidemiologyandsurvival pages 1-2)

### 9. Inheritance and population

#### 9.1 Epidemiology (recent registry statistics)
**United States (CBTRUS; publication Oct 2024; diagnoses 2017–2021):**
- “Between 2017 and 2021, the average annual age-adjusted incidence rate (AAAIR) of all primary malignant and non-malignant brain and other CNS tumors was **25.34 per 100,000** (malignant AAAIR **6.89** and non-malignant AAAIR **18.46**).” (price2024cbtrusstatisticalreport pages 70-72)
- Gliomas accounted for **22.9%** of all tumors in CBTRUS (histology-based grouping). (price2024cbtrusstatisticalreport pages 70-72)
- For oligodendroglioma (histology grouping), 5-year relative survival **96.0%** overall; 10-year relative survival **92.9%** overall. (price2024cbtrusstatisticalreport pages 70-72)

**Belgium (Belgian Cancer Registry; publication Aug 2024; incidence window 2017–2019; reclassified to WHO 2021 molecular scheme):**
- Age-standardized incidence rate: **8.55 per 100,000 person-years** for adult-type diffuse glioma; **6.72 per 100,000 person-years** for grade 4 lesions. (pinson2024epidemiologyandsurvival pages 1-2)
- Estimated incidence (ESR): grade 2 astrocytoma **0.60/100,000**; grade 3 astrocytoma **0.48/100,000**; oligodendroglioma **~0.52/100,000**. (pinson2024epidemiologyandsurvival pages 3-4)

#### 9.2 Demographics
- In Belgium registry diffuse gliomas (2017–2019), median age ~64 and ~40% female (contextual registry description). (pinson2024epidemiologyandsurvival pages 4-6)

#### 9.3 Genetic inheritance
- For malignant brain tumors broadly, fewer than 5% report family history/predisposition syndromes in the JAMA review. (schaff2023glioblastomaandother pages 3-4)

### 10. Diagnostics

#### 10.1 Diagnostic approach (WHO CNS5 integrated diagnosis)
Core tests for reclassifying “mixed” diffuse gliomas include:
- **IDH mutation testing** (IHC for IDH1 R132H plus sequencing when needed). (martin2023fromtheoryto pages 2-4)
- **ATRX IHC** (loss supports astrocytoma, IDH-mutant). (whitfield2022classificationofadult‐type pages 4-6)
- **1p/19q codeletion testing** (required to define oligodendroglioma with IDH mutation; performed if ATRX is retained). (martin2023fromtheoryto pages 2-4)
- **Additional molecular grading markers** such as **CDKN2A/B homozygous deletion**. (whitfield2022classificationofadult‐type pages 4-6)

**WHO CNS5 adult diffuse glioma diagnostic algorithm (visual):** see the retrieved figure integrating morphology with IDH/ATRX/1p19q and grade-defining features. (martin2023fromtheoryto media fe0dadc9)

#### 10.2 NOS/NEC usage
Where molecular workup is incomplete/unavailable, WHO encourages NOS/NEC qualifiers rather than defaulting to obsolete mixed categories. (horbinski2022clinicalimplicationsof pages 2-3)

### 11. Outcome / prognosis

#### 11.1 Real-world survival (Belgium registry; 2017–2019; publication 2024)
- IDH-wildtype glioblastoma median OS **9.3 months** vs grade 4 IDH-mutant astrocytoma median OS **25.9 months**. (pinson2024epidemiologyandsurvival pages 1-2)
- 3-year survival probabilities:
  - IDH-mutant astrocytoma grade 2: **86.0%**; grade 3: **75.7%**. (pinson2024epidemiologyandsurvival pages 1-2)
  - Oligodendroglioma (IDH-mutant/1p19q-codeleted): grade 2 **93.4%**; grade 3 **64.2%**. (pinson2024epidemiologyandsurvival pages 3-4)

#### 11.2 Prognostic molecular markers (recent cohort data)
- TERT promoter mutations are frequent in oligodendroglioma but were not prognostic within oligodendroglioma in one study due to near ubiquity; in a combined astrocytic-tumor grouping, TERTp was an adverse prognostic factor, but not within IDH-mutant astrocytoma alone. (lee2024prognosticimpactof pages 1-2)
- CDKN2A/B homozygous deletion is associated with worse outcome and is a WHO CNS5 grade-defining event in IDH-mutant astrocytoma. (whitfield2022classificationofadult‐type pages 4-6)

### 12. Treatment

#### 12.1 Standard-of-care (current real-world implementations)
Across modern guidelines and reviews, treatment is determined by the reassigned molecular entity (astrocytoma IDH-mutant vs oligodendroglioma IDH-mutant/1p19q-codeleted) and grade:
- **Maximal safe resection** is a foundational step but is not curative in grade 2 diffuse gliomas; “grade 2 gliomas are incurable by surgery and complementary treatments are vital to improving prognosis.” (SEOM-GEINO; publication Apr 2024). (vazsalgado2024seomgeinoclinicalguidelines pages 1-3)
- **Radiotherapy + chemotherapy** are guideline-based standards:
  - RT + **PCV** has become a standard for appropriate patients (e.g., RTOG 9802 evidence base) and is considered standard-of-care in modern reviews. (kessler2023conventionalandemerging pages 2-4, vazsalgado2024seomgeinoclinicalguidelines pages 4-5)
  - For grade 3 IDH-mutant astrocytoma: RT followed by maintenance temozolomide is guideline-supported standard-of-care; for grade 3 oligodendroglioma: RT + PCV is standard based on randomized trials. (segura2023seomgeinoclinicalguidelines pages 4-5)
- **Limited options at progression:** despite standard multimodality therapy, progressive disease remains difficult to treat with limited clearly effective strategies beyond re-operation, re-irradiation, and additional chemotherapy. (kessler2023conventionalandemerging pages 1-2, kessler2023conventionalandemerging pages 6-7)

**Suggested MAXO terms (examples):**
- Surgical resection: MAXO:0000010
- Radiation therapy: MAXO:0000127
- Chemotherapy: MAXO:0000647

#### 12.2 Targeted therapy advance (prioritize 2023–2024): Vorasidenib (INDIGO)
A major late-2023 development was the phase 3 INDIGO trial of the oral brain-penetrant mutant IDH1/2 inhibitor **vorasidenib** for grade 2 IDH-mutant glioma after surgery only.

**Direct abstract quote (NEJM, publication Aug 2023):**
- “Progression-free survival was significantly improved in the vorasidenib group as compared with the placebo group (**median progression-free survival, 27.7 months vs. 11.1 months; hazard ratio … 0.39 … P<0.001**).” (mellinghoff2023vorasidenibinidh1 pages 1-3)

Key results:
- Population: residual/recurrent grade 2 IDH-mutant glioma; no prior RT/chemotherapy; n=331. (mellinghoff2023vorasidenibinidh1 pages 1-3)
- PFS: 27.7 vs 11.1 months; HR 0.39 (95% CI 0.27–0.56). (mellinghoff2023vorasidenibinidh1 pages 1-3, mellinghoff2023vorasidenibinidh1 pages 6-8)
- Time to next intervention: HR 0.26 (95% CI 0.15–0.43). (mellinghoff2023vorasidenibinidh1 pages 1-3, mellinghoff2023vorasidenibinidh1 pages 6-8)
- Safety: grade ≥3 ALT increase ~9.6% (vorasidenib) vs 0% (placebo). (mellinghoff2023vorasidenibinidh1 pages 1-3)
- Trial registry: **NCT04164901**. (mellinghoff2023vorasidenibinidh1 pages 1-3)

Clinical implementation (2024 guideline context): SEOM-GEINO grade 2 glioma guidelines describe IDH inhibitors as new treatments showing significant efficacy in grade 2 gliomas without prior RT/chemotherapy and reference vorasidenib in this setting. (vazsalgado2024seomgeinoclinicalguidelines pages 1-3, vazsalgado2024seomgeinoclinicalguidelines pages 4-5)

### 13. Prevention
There are no established primary-prevention interventions specific to oligoastrocytoma, and “modifiable” risk factor evidence for glioma is generally weak.
- Recent prospective evidence supports that common lifestyle/metabolic factors largely do not materially alter glioma risk (CONOR cohort). (gheorghiu2024lifestyleandmetabolic pages 1-2, gheorghiu2024lifestyleandmetabolic pages 3-5)
- The most established preventable exposure in this evidence is **therapeutic/medical ionizing radiation** to the CNS; prevention therefore focuses on minimizing unnecessary radiation exposure consistent with general radiological safety principles. (schaff2023glioblastomaandother pages 3-4)

### 14. Other species / natural disease
Not retrieved in the current evidence corpus for oligoastrocytoma specifically.

### 15. Model organisms / model systems
Because oligoastrocytoma is obsolete as a molecular category, model systems are typically aligned to glioblastoma or to IDH-mutant astrocytoma/oligodendroglioma biology.

A 2024 systematic review of glioma stem cell (GSC) models provides quantitative data on commonly used in vitro systems:
- Included 65 studies; most common model cell lines: **U87 (20 studies; 32.0%)**, **U251 (13; 20.0%)**, **A172 (4; 6.2%)**, **T98G (2; 3.17%)**. (agosti2024gliomastemcells pages 1-2)
- The review notes GSCs can “recapitulat[e] the heterogeneity of the original tumor when transplanted into immunocompromised mice,” indicating frequent **xenograft** use. (agosti2024gliomastemcells pages 1-2)
- It also emphasizes a field shift toward more representative **patient-derived xenografts (PDXs)** and **primary glioma cell lines** because highly passaged lines like U87 do not capture tumor heterogeneity. (agosti2024gliomastemcells pages 15-17)

---

## URLs and publication dates (selected high-authority sources used)
- WHO CNS5 summary (Neuro-Oncology): https://doi.org/10.1093/neuonc/noab106 (published Jun 2021). (louis2021the2021who pages 15-16)
- WHO CNS5 clinical implications review (Nat Rev Neurol): https://doi.org/10.1038/s41582-022-00679-w (published Jun 2022). (horbinski2022clinicalimplicationsof pages 1-2)
- Belgian Cancer Registry molecular-era epidemiology (Neuro-Oncology): https://doi.org/10.1093/neuonc/noad158 (published Aug 2024). (pinson2024epidemiologyandsurvival pages 1-2)
- CBTRUS 2017–2021 statistical report (Neuro-Oncology): https://doi.org/10.1093/neuonc/noae145 (published Oct 2024). (price2024cbtrusstatisticalreport pages 70-72)
- Vorasidenib INDIGO phase 3 (NEJM): https://doi.org/10.1056/NEJMoa2304194 (published Aug 2023). (mellinghoff2023vorasidenibinidh1 pages 1-3)
- SEOM-GEINO grade 2 glioma guideline (Clin Transl Oncol): https://doi.org/10.1007/s12094-024-03456-x (published Apr 2024). (vazsalgado2024seomgeinoclinicalguidelines pages 1-3)
- Adult malignant brain tumor clinical review (JAMA): https://doi.org/10.1001/jama.2023.0023 (published Feb 2023). (schaff2023glioblastomaandother pages 1-3)

## Key limitations of this report (evidence gaps)
- A **MONDO ID**, **MeSH identifier**, **ICD-10/ICD-11 codes**, **OMIM**, and **Orphanet** identifiers for oligoastrocytoma were not found in the retrieved documents.
- PMIDs were not available in the retrieved text chunks (DOIs/URLs provided instead).
- Several requested detailed subsections (e.g., comprehensive differential diagnosis lists; detailed methylome classes; multi-omics signatures; validated QoL instrument statistics; natural disease in other species) were not available in the retrieved evidence and would require additional targeted retrieval from specialized databases and primary cohort publications.


References

1. (louis2021the2021who pages 15-16): David N Louis, Arie Perry, Pieter Wesseling, Daniel J Brat, Ian A Cree, Dominique Figarella-Branger, Cynthia Hawkins, H K Ng, Stefan M Pfister, Guido Reifenberger, Riccardo Soffietti, Andreas von Deimling, and David W Ellison. The 2021 who classification of tumors of the central nervous system: a summary. Neuro-oncology, 23:1231-1251, Jun 2021. URL: https://doi.org/10.1093/neuonc/noab106, doi:10.1093/neuonc/noab106. This article has 13436 citations and is from a domain leading peer-reviewed journal.

2. (horbinski2022clinicalimplicationsof pages 2-3): Craig Horbinski, Tamar Berger, Roger J. Packer, and Patrick Y. Wen. Clinical implications of the 2021 edition of the who classification of central nervous system tumours. Nature Reviews Neurology, 18:515-529, Jun 2022. URL: https://doi.org/10.1038/s41582-022-00679-w, doi:10.1038/s41582-022-00679-w. This article has 346 citations and is from a highest quality peer-reviewed journal.

3. (horbinski2022clinicalimplicationsof pages 1-2): Craig Horbinski, Tamar Berger, Roger J. Packer, and Patrick Y. Wen. Clinical implications of the 2021 edition of the who classification of central nervous system tumours. Nature Reviews Neurology, 18:515-529, Jun 2022. URL: https://doi.org/10.1038/s41582-022-00679-w, doi:10.1038/s41582-022-00679-w. This article has 346 citations and is from a highest quality peer-reviewed journal.

4. (reuss2023updatesonthe pages 1-2): David.E. Reuss. Updates on the who diagnosis of idh-mutant glioma. Journal of Neuro-Oncology, 162:461-469, Jan 2023. URL: https://doi.org/10.1007/s11060-023-04250-5, doi:10.1007/s11060-023-04250-5. This article has 75 citations and is from a peer-reviewed journal.

5. (perez2021theevolvingclassification pages 1-2): Alejandro Perez and Jason T. Huse. The evolving classification of diffuse gliomas: world health organization updates for 2021. Current Neurology and Neuroscience Reports, Nov 2021. URL: https://doi.org/10.1007/s11910-021-01153-8, doi:10.1007/s11910-021-01153-8. This article has 76 citations and is from a domain leading peer-reviewed journal.

6. (pinson2024epidemiologyandsurvival pages 2-3): Harry Pinson, Geert Silversmit, Dimitri Vanhauwaert, Katrijn Vanschoenbeek, Jean-Pierre Kalala Okito, Steven De Vleeschouwer, Tom Boterberg, and Cindy De Gendt. Epidemiology and survival of adult-type diffuse glioma in belgium during the molecular era. Neuro-oncology, 26:191-202, Aug 2024. URL: https://doi.org/10.1093/neuonc/noad158, doi:10.1093/neuonc/noad158. This article has 28 citations and is from a domain leading peer-reviewed journal.

7. (antonelli2022adulttypediffuse pages 1-2): Manila Antonelli and Pietro Luigi Poliani. Adult type diffuse gliomas in the new 2021 who classification. Pathologica, 114:397-409, Dec 2022. URL: https://doi.org/10.32074/1591-951x-823, doi:10.32074/1591-951x-823. This article has 72 citations.

8. (whitfield2022classificationofadult‐type pages 4-6): Benjamin T. Whitfield and Jason T. Huse. Classification of adult‐type diffuse gliomas: impact of the world health organization 2021 update. Brain Pathology, Mar 2022. URL: https://doi.org/10.1111/bpa.13062, doi:10.1111/bpa.13062. This article has 199 citations and is from a domain leading peer-reviewed journal.

9. (martin2023fromtheoryto pages 2-4): Karina Chornenka Martin, Crystal Ma, and Stephen Yip. From theory to practice: implementing the who 2021 classification of adult diffuse gliomas in neuropathology diagnosis. Brain Sciences, May 2023. URL: https://doi.org/10.3390/brainsci13050817, doi:10.3390/brainsci13050817. This article has 25 citations.

10. (antonelli2022adulttypediffuse pages 2-4): Manila Antonelli and Pietro Luigi Poliani. Adult type diffuse gliomas in the new 2021 who classification. Pathologica, 114:397-409, Dec 2022. URL: https://doi.org/10.32074/1591-951x-823, doi:10.32074/1591-951x-823. This article has 72 citations.

11. (lee2024prognosticimpactof pages 1-2): Yujin Lee, Chul-Kee Park, and Sung-Hye Park. Prognostic impact of tert promoter mutations in adult-type diffuse gliomas based on who2021 criteria. Cancers, 16:2032, May 2024. URL: https://doi.org/10.3390/cancers16112032, doi:10.3390/cancers16112032. This article has 11 citations.

12. (pinson2024epidemiologyandsurvival pages 1-2): Harry Pinson, Geert Silversmit, Dimitri Vanhauwaert, Katrijn Vanschoenbeek, Jean-Pierre Kalala Okito, Steven De Vleeschouwer, Tom Boterberg, and Cindy De Gendt. Epidemiology and survival of adult-type diffuse glioma in belgium during the molecular era. Neuro-oncology, 26:191-202, Aug 2024. URL: https://doi.org/10.1093/neuonc/noad158, doi:10.1093/neuonc/noad158. This article has 28 citations and is from a domain leading peer-reviewed journal.

13. (kessler2023conventionalandemerging pages 2-4): Tobias Kessler, Jakob Ito, Wolfgang Wick, and Antje Wick. Conventional and emerging treatments of astrocytomas and oligodendrogliomas. Journal of Neuro-Oncology, 162:471-478, Dec 2023. URL: https://doi.org/10.1007/s11060-022-04216-z, doi:10.1007/s11060-022-04216-z. This article has 26 citations and is from a peer-reviewed journal.

14. (kessler2023conventionalandemerging pages 6-7): Tobias Kessler, Jakob Ito, Wolfgang Wick, and Antje Wick. Conventional and emerging treatments of astrocytomas and oligodendrogliomas. Journal of Neuro-Oncology, 162:471-478, Dec 2023. URL: https://doi.org/10.1007/s11060-022-04216-z, doi:10.1007/s11060-022-04216-z. This article has 26 citations and is from a peer-reviewed journal.

15. (segura2023seomgeinoclinicalguidelines pages 4-5): Pedro Pérez Segura, Noelia Vilariño Quintela, María Martínez García, Sonia del Barco Berrón, Regina Gironés Sarrió, Jesús García Gómez, Almudena García Castaño, Luis Miguel Navarro Martín, Oscar Gallego Rubio, and Estela Pineda Losada. Seom-geino clinical guidelines for high-grade gliomas of adulthood (2022). Clinical & Translational Oncology, 25:2634-2646, Aug 2023. URL: https://doi.org/10.1007/s12094-023-03245-y, doi:10.1007/s12094-023-03245-y. This article has 43 citations and is from a peer-reviewed journal.

16. (vazsalgado2024seomgeinoclinicalguidelines pages 4-5): María Ángeles Vaz-Salgado, Belén Cigarral García, Isaura Fernández Pérez, Beatriz Jiménez Munárriz, Paula Sampedro Domarco, Ainhoa Hernández González, María Vieito Villar, Raquel Luque Caro, María Luisa Villamayor Delgado, and Juan Manuel Sepúlveda Sánchez. Seom-geino clinical guidelines for grade 2 gliomas (2023). Clinical and Translational Oncology, 26:2856-2865, Apr 2024. URL: https://doi.org/10.1007/s12094-024-03456-x, doi:10.1007/s12094-024-03456-x. This article has 5 citations and is from a peer-reviewed journal.

17. (li2024clinicalsequencingreveals pages 1-2): Zhenyan Li, Zhenghao Deng, Fangkun Liu, Chuntao Li, Kui Yang, Xuan Gong, Songshan Feng, Yu Zeng, Hongshu Zhou, Fan Fan, Chengke Luo, Zhixiong Liu, and Mingyu Zhang. Clinical sequencing reveals diagnostic, therapeutic, and prognostic biomarkers for adult-type diffuse gliomas. Heliyon, 10:e37712, Sep 2024. URL: https://doi.org/10.1016/j.heliyon.2024.e37712, doi:10.1016/j.heliyon.2024.e37712. This article has 4 citations.

18. (martin2023fromtheoryto pages 4-6): Karina Chornenka Martin, Crystal Ma, and Stephen Yip. From theory to practice: implementing the who 2021 classification of adult diffuse gliomas in neuropathology diagnosis. Brain Sciences, May 2023. URL: https://doi.org/10.3390/brainsci13050817, doi:10.3390/brainsci13050817. This article has 25 citations.

19. (pinson2024epidemiologyandsurvival pages 3-4): Harry Pinson, Geert Silversmit, Dimitri Vanhauwaert, Katrijn Vanschoenbeek, Jean-Pierre Kalala Okito, Steven De Vleeschouwer, Tom Boterberg, and Cindy De Gendt. Epidemiology and survival of adult-type diffuse glioma in belgium during the molecular era. Neuro-oncology, 26:191-202, Aug 2024. URL: https://doi.org/10.1093/neuonc/noad158, doi:10.1093/neuonc/noad158. This article has 28 citations and is from a domain leading peer-reviewed journal.

20. (price2024cbtrusstatisticalreport pages 70-72): Mackenzie Price, Christine Ballard, Julia Benedetti, Corey Neff, Gino Cioffi, Kristin A Waite, Carol Kruchko, Jill S Barnholtz-Sloan, and Quinn T Ostrom. Cbtrus statistical report: primary brain and other central nervous system tumors diagnosed in the united states in 2017-2021. Neuro-oncology, 26 Supplement_6:vi1-vi85, Oct 2024. URL: https://doi.org/10.1093/neuonc/noae145, doi:10.1093/neuonc/noae145. This article has 489 citations and is from a domain leading peer-reviewed journal.

21. (horbinski2022clinicalimplicationsof pages 4-5): Craig Horbinski, Tamar Berger, Roger J. Packer, and Patrick Y. Wen. Clinical implications of the 2021 edition of the who classification of central nervous system tumours. Nature Reviews Neurology, 18:515-529, Jun 2022. URL: https://doi.org/10.1038/s41582-022-00679-w, doi:10.1038/s41582-022-00679-w. This article has 346 citations and is from a highest quality peer-reviewed journal.

22. (mellinghoff2023vorasidenibinidh1 pages 1-3): Ingo K. Mellinghoff, Martin J. van den Bent, Deborah T. Blumenthal, Mehdi Touat, Katherine B. Peters, Jennifer Clarke, Joe Mendez, Shlomit Yust-Katz, Liam Welsh, Warren P. Mason, François Ducray, Yoshie Umemura, Burt Nabors, Matthias Holdhoff, Andreas F. Hottinger, Yoshiki Arakawa, Juan M. Sepulveda, Wolfgang Wick, Riccardo Soffietti, James R. Perry, Pierre Giglio, Macarena de la Fuente, Elizabeth A. Maher, Steven Schoenfeld, Dan Zhao, Shuchi S. Pandya, Lori Steelman, Islam Hassan, Patrick Y. Wen, and Timothy F. Cloughesy. Vorasidenib in idh1- or idh2-mutant low-grade glioma. New England Journal of Medicine, 389:589-601, Aug 2023. URL: https://doi.org/10.1056/nejmoa2304194, doi:10.1056/nejmoa2304194. This article has 822 citations and is from a highest quality peer-reviewed journal.

23. (mellinghoff2023vorasidenibinidh1 pages 3-5): Ingo K. Mellinghoff, Martin J. van den Bent, Deborah T. Blumenthal, Mehdi Touat, Katherine B. Peters, Jennifer Clarke, Joe Mendez, Shlomit Yust-Katz, Liam Welsh, Warren P. Mason, François Ducray, Yoshie Umemura, Burt Nabors, Matthias Holdhoff, Andreas F. Hottinger, Yoshiki Arakawa, Juan M. Sepulveda, Wolfgang Wick, Riccardo Soffietti, James R. Perry, Pierre Giglio, Macarena de la Fuente, Elizabeth A. Maher, Steven Schoenfeld, Dan Zhao, Shuchi S. Pandya, Lori Steelman, Islam Hassan, Patrick Y. Wen, and Timothy F. Cloughesy. Vorasidenib in idh1- or idh2-mutant low-grade glioma. New England Journal of Medicine, 389:589-601, Aug 2023. URL: https://doi.org/10.1056/nejmoa2304194, doi:10.1056/nejmoa2304194. This article has 822 citations and is from a highest quality peer-reviewed journal.

24. (mellinghoff2023vorasidenibinidh1 pages 6-8): Ingo K. Mellinghoff, Martin J. van den Bent, Deborah T. Blumenthal, Mehdi Touat, Katherine B. Peters, Jennifer Clarke, Joe Mendez, Shlomit Yust-Katz, Liam Welsh, Warren P. Mason, François Ducray, Yoshie Umemura, Burt Nabors, Matthias Holdhoff, Andreas F. Hottinger, Yoshiki Arakawa, Juan M. Sepulveda, Wolfgang Wick, Riccardo Soffietti, James R. Perry, Pierre Giglio, Macarena de la Fuente, Elizabeth A. Maher, Steven Schoenfeld, Dan Zhao, Shuchi S. Pandya, Lori Steelman, Islam Hassan, Patrick Y. Wen, and Timothy F. Cloughesy. Vorasidenib in idh1- or idh2-mutant low-grade glioma. New England Journal of Medicine, 389:589-601, Aug 2023. URL: https://doi.org/10.1056/nejmoa2304194, doi:10.1056/nejmoa2304194. This article has 822 citations and is from a highest quality peer-reviewed journal.

25. (vazsalgado2024seomgeinoclinicalguidelines pages 1-3): María Ángeles Vaz-Salgado, Belén Cigarral García, Isaura Fernández Pérez, Beatriz Jiménez Munárriz, Paula Sampedro Domarco, Ainhoa Hernández González, María Vieito Villar, Raquel Luque Caro, María Luisa Villamayor Delgado, and Juan Manuel Sepúlveda Sánchez. Seom-geino clinical guidelines for grade 2 gliomas (2023). Clinical and Translational Oncology, 26:2856-2865, Apr 2024. URL: https://doi.org/10.1007/s12094-024-03456-x, doi:10.1007/s12094-024-03456-x. This article has 5 citations and is from a peer-reviewed journal.

26. (brandner2020standardsanddatasets pages 25-27): S Brandner, Z Jaunmuktane, F Roncaroli, and SR NHSFT. Standards and datasets for reporting cancers dataset for histopathological reporting of tumours of the central nervous system in adults, including the pituitary …. Unknown journal, 2020.

27. (forjaz2021anupdatedhistology pages 4-4): Gonçalo Forjaz, Jill S Barnholtz-Sloan, Carol Kruchko, Rebecca Siegel, Serban Negoita, Quinn T Ostrom, Lois Dickie, Jennifer Ruhl, Alison Van Dyke, Nirav Patil, Gino Cioffi, Kimberly D Miller, Kristin Waite, and Angela B Mariotto. An updated histology recode for the analysis of primary malignant and nonmalignant brain and other central nervous system tumors in the surveillance, epidemiology, and end results program. Neuro-Oncology Advances, Dec 2021. URL: https://doi.org/10.1093/noajnl/vdaa175, doi:10.1093/noajnl/vdaa175. This article has 38 citations and is from a peer-reviewed journal.

28. (schaff2023glioblastomaandother pages 3-4): Lauren R. Schaff and Ingo K. Mellinghoff. Glioblastoma and other primary brain malignancies in adults: a review. JAMA, 329 7:574-587, Feb 2023. URL: https://doi.org/10.1001/jama.2023.0023, doi:10.1001/jama.2023.0023. This article has 1288 citations.

29. (gheorghiu2024lifestyleandmetabolic pages 1-2): Anamaria Gheorghiu, Cathrine Brunborg, Tom B. Johannesen, Eirik Helseth, John-Anker Zwart, and Markus K. H. Wiedmann. Life-style and metabolic factors do not affect risk for glioma: a prospective population-based study (the cohort of norway). Frontiers in Oncology, Dec 2024. URL: https://doi.org/10.3389/fonc.2024.1471733, doi:10.3389/fonc.2024.1471733. This article has 5 citations.

30. (gheorghiu2024lifestyleandmetabolic pages 3-5): Anamaria Gheorghiu, Cathrine Brunborg, Tom B. Johannesen, Eirik Helseth, John-Anker Zwart, and Markus K. H. Wiedmann. Life-style and metabolic factors do not affect risk for glioma: a prospective population-based study (the cohort of norway). Frontiers in Oncology, Dec 2024. URL: https://doi.org/10.3389/fonc.2024.1471733, doi:10.3389/fonc.2024.1471733. This article has 5 citations.

31. (schaff2023glioblastomaandother pages 1-3): Lauren R. Schaff and Ingo K. Mellinghoff. Glioblastoma and other primary brain malignancies in adults: a review. JAMA, 329 7:574-587, Feb 2023. URL: https://doi.org/10.1001/jama.2023.0023, doi:10.1001/jama.2023.0023. This article has 1288 citations.

32. (pinson2024epidemiologyandsurvival pages 4-6): Harry Pinson, Geert Silversmit, Dimitri Vanhauwaert, Katrijn Vanschoenbeek, Jean-Pierre Kalala Okito, Steven De Vleeschouwer, Tom Boterberg, and Cindy De Gendt. Epidemiology and survival of adult-type diffuse glioma in belgium during the molecular era. Neuro-oncology, 26:191-202, Aug 2024. URL: https://doi.org/10.1093/neuonc/noad158, doi:10.1093/neuonc/noad158. This article has 28 citations and is from a domain leading peer-reviewed journal.

33. (martin2023fromtheoryto media fe0dadc9): Karina Chornenka Martin, Crystal Ma, and Stephen Yip. From theory to practice: implementing the who 2021 classification of adult diffuse gliomas in neuropathology diagnosis. Brain Sciences, May 2023. URL: https://doi.org/10.3390/brainsci13050817, doi:10.3390/brainsci13050817. This article has 25 citations.

34. (kessler2023conventionalandemerging pages 1-2): Tobias Kessler, Jakob Ito, Wolfgang Wick, and Antje Wick. Conventional and emerging treatments of astrocytomas and oligodendrogliomas. Journal of Neuro-Oncology, 162:471-478, Dec 2023. URL: https://doi.org/10.1007/s11060-022-04216-z, doi:10.1007/s11060-022-04216-z. This article has 26 citations and is from a peer-reviewed journal.

35. (agosti2024gliomastemcells pages 1-2): Edoardo Agosti, Sara Antonietti, Tamara Ius, Marco Maria Fontanella, Marco Zeppieri, and Pier Paolo Panciani. Glioma stem cells as promoter of glioma progression: a systematic review of molecular pathways and targeted therapies. International Journal of Molecular Sciences, 25:7979, Jul 2024. URL: https://doi.org/10.3390/ijms25147979, doi:10.3390/ijms25147979. This article has 47 citations.

36. (agosti2024gliomastemcells pages 15-17): Edoardo Agosti, Sara Antonietti, Tamara Ius, Marco Maria Fontanella, Marco Zeppieri, and Pier Paolo Panciani. Glioma stem cells as promoter of glioma progression: a systematic review of molecular pathways and targeted therapies. International Journal of Molecular Sciences, 25:7979, Jul 2024. URL: https://doi.org/10.3390/ijms25147979, doi:10.3390/ijms25147979. This article has 47 citations.