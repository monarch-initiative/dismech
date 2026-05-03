---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-26T20:00:28.065062'
end_time: '2026-04-26T20:14:20.584203'
duration_seconds: 832.52
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Van Buchem Disease
  mondo_id: MONDO:0009395
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 34
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Van Buchem Disease
- **MONDO ID:** MONDO:0009395 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Van Buchem Disease** covering all of the
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
- **Disease Name:** Van Buchem Disease
- **MONDO ID:** MONDO:0009395 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Van Buchem Disease** covering all of the
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


# Van Buchem Disease (hyperostosis corticalis generalisata; MONDO:0009395) — Disease Characteristics Research Report

## Executive summary
Van Buchem disease (VBD) is a very rare, autosomal recessive, high-bone-mass craniotubular hyperostosis caused not by a coding mutation but by a biallelic ~52-kb **noncoding deletion** downstream of **SOST** that removes a bone enhancer and decreases expression of the osteocyte-derived Wnt antagonist **sclerostin**. Clinically it is characterized by progressive skull/mandibular hyperostosis and cranial-nerve entrapment (notably recurrent facial palsy and hearing loss), extremely elevated DXA Z-scores, and generally normal life expectancy with stabilization after early adulthood. Key quantitative datasets are available from a Dutch cohort (n=15 patients, n=28 carriers) including BMD, serum sclerostin, and bone turnover markers. (balemans2002identificationofa pages 1-2, loots2005genomicdeletionof pages 3-4, lierop2013vanbuchemdisease pages 1-2)

---

## 1. Disease information
### 1.1 Definition and overview
VBD is a severe sclerosing bone dysplasia/craniotubular hyperostosis with generalized cortical and endosteal bone overgrowth, most prominent in the skull and mandible, which can lead to cranial nerve entrapment (facial palsy, hearing loss, visual loss) and occasionally increased intracranial pressure. (balemans2002identificationofa pages 1-2, appelmandijkstra2026sclerosingbonedysplasias pages 1-3)

### 1.2 Key identifiers
- **MONDO:** MONDO:0009395 (hyperostosis corticalis generalisata) (appelmandijkstra2026sclerosingbonedysplasias pages 17-18, staehling‐hampton2002a52kbdeletion pages 9-9)
- **OMIM:** **239100** (Van Buchem disease) (staehling‐hampton2002a52kbdeletion pages 9-9)

**Not retrieved in the sourced full texts during this tool run:** Orphanet ID, ICD-10/ICD-11 codes, and MeSH ID. (appelmandijkstra2026sclerosingbonedysplasias pages 1-3)

### 1.3 Synonyms / alternative names
- **Hyperostosis corticalis generalisata** (most common synonym in modern and historical literature) (balemans2002identificationofa pages 1-2, appelmandijkstra2026sclerosingbonedysplasias pages 8-9)
- **Hyperostosis corticalis generalisata familiaris** (older terminology) (dixon1982twocasesof pages 1-3)
- **SOST-related endosteal hyperostosis, van Buchem type** (modern descriptive label used in recent reference text) (appelmandijkstra2026sclerosingbonedysplasias pages 1-3)

### 1.4 Evidence type (patient-level vs aggregated)
Evidence for VBD in this report comes from:
- **Aggregated cohorts/case series** (e.g., Dutch cohort with 15 patients and 28 carriers) (lierop2013vanbuchemdisease pages 1-2, lierop2013vanbuchemdisease pages 2-3)
- **Individual case reports/series** describing neurosurgical decompression and long-term outcomes (dixon1982twocasesof pages 1-3, dixon1982twocasesof pages 3-5)
- **Molecular genetics and functional genomics** defining the causal deletion and enhancer mechanism (balemans2002identificationofa pages 1-2, loots2005genomicdeletionof pages 3-4)

**Structured reference artifacts**
| Identifier system | ID/value | Label | Notes/synonyms | Primary citation |
|---|---|---|---|---|
| MONDO | MONDO:0009395 | hyperostosis corticalis generalisata | MONDO target disease in the prompt; corresponds to Van Buchem disease / hyperostosis corticalis generalisata | (staehling‐hampton2002a52kbdeletion pages 9-9, appelmandijkstra2026sclerosingbonedysplasias pages 17-18) |
| OMIM | 239100 | Van Buchem disease | OMIM entry explicitly cited for Van Buchem disease; synonym in sourced texts: hyperostosis corticalis generalisata | (staehling‐hampton2002a52kbdeletion pages 9-9, loots2005genomicdeletionof pages 3-4) |
| Orphanet | Not retrieved in sourced texts | Van Buchem disease | Orphanet identifier was requested but was not present in the retrieved evidence excerpts; disease described as very rare and mainly reported in the Netherlands | (appelmandijkstra2026sclerosingbonedysplasias pages 8-9, appelmandijkstra2026sclerosingbonedysplasias pages 1-3) |
| ICD-10 | Not retrieved in sourced texts | Van Buchem disease | No ICD-10 code was present in the sourced texts reviewed | (appelmandijkstra2026sclerosingbonedysplasias pages 1-3) |
| ICD-11 | Not retrieved in sourced texts | Van Buchem disease | No ICD-11 code was present in the sourced texts reviewed | (appelmandijkstra2026sclerosingbonedysplasias pages 1-3) |
| MeSH | Not retrieved in sourced texts | Van Buchem disease | No MeSH identifier was present in the sourced texts reviewed | (appelmandijkstra2026sclerosingbonedysplasias pages 1-3) |
| Disease name / preferred term | Van Buchem disease | Van Buchem disease | Rare autosomal recessive sclerosing bone dysplasia caused by a biallelic 52-kb deletion downstream of SOST; often presented as milder than sclerosteosis | (balemans2002identificationofa pages 1-2, appelmandijkstra2026sclerosingbonedysplasias pages 1-3, loots2005genomicdeletionof pages 3-4) |
| Historical/radiologic synonym | hyperostosis corticalis generalisata | hyperostosis corticalis generalisata | Recurrent synonym in primary and review literature; also described as hyperostosis corticalis generalisata familiaris in older reports | (balemans2002identificationofa pages 1-2, appelmandijkstra2026sclerosingbonedysplasias pages 8-9, dixon1982twocasesof pages 1-3) |
| Mechanistic/nosologic synonym | SOST-related endosteal hyperostosis, van Buchem type | SOST-related endosteal hyperostosis, van Buchem type | Modern descriptive label emphasizing SOST regulatory etiology and distinction from SOST coding-loss sclerosteosis | (appelmandijkstra2026sclerosingbonedysplasias pages 1-3) |


*Table: This table summarizes the key identifiers and nomenclature for Van Buchem disease from the retrieved evidence. It includes supported MONDO and OMIM identifiers and clearly marks identifier systems not retrieved in the sourced texts.*

---

## 2. Etiology
### 2.1 Primary causal factors
**Genetic cause (Mendelian):** VBD is caused by a **homozygous ~51.7–52 kb deletion** located ~35 kb downstream of **SOST** within the **SOST–MEOX1 intergenic region on 17q12–q21**; the deletion contains no coding gene and is hypothesized (and functionally supported) to remove a cis-regulatory enhancer required for bone expression of SOST. (balemans2002identificationofa pages 1-2, staehling‐hampton2002a52kbdeletion pages 4-5, loots2005genomicdeletionof pages 3-4)

**Mechanistic causal chain:**
1) Biallelic downstream deletion removes bone enhancer(s) (including ECR5) → 2) reduced SOST transcription/sclerostin production in bone → 3) reduced inhibition of canonical Wnt signaling at osteoblast lineage cells → 4) increased bone formation and high bone mass with progressive hyperostosis → 5) cranial nerve entrapment and craniofacial complications. (loots2005genomicdeletionof pages 3-4, lierop2013vanbuchemdisease pages 1-2)

### 2.2 Risk factors
- **Genetic:** biallelic 52-kb deletion downstream of SOST (pathogenic) (balemans2002identificationofa pages 1-2, lierop2013vanbuchemdisease pages 2-3)
- **Population/founder risk:** strong association with the Netherlands and a historically described small Dutch village cluster. (lierop2013vanbuchemdisease pages 1-2, lierop2012theroleof pages 66-73)

No environmental, infectious, or lifestyle risk factors were identified in the sourced texts; the disorder is primarily determined by genotype. (balemans2002identificationofa pages 1-2)

### 2.3 Protective factors
No specific genetic or environmental protective factors were identified in the retrieved VBD-focused sources.

### 2.4 Gene–environment interactions
Not established for VBD in the retrieved literature; given the single major causal CNV and consistent phenotype, gene–environment interaction evidence appears limited/absent in these sources.

---

## 3. Phenotypes
### 3.1 Core phenotype spectrum (with onset, frequency, and progression)
A well-characterized Dutch cohort (15/18 known Dutch patients) reported:
- **Facial palsy:** 15/15 (100%); median age at first occurrence 2.5 years; decompression surgery performed in 6/15. (lierop2013vanbuchemdisease pages 2-3)
- **Hearing impairment:** 14/15 (93%); external auditory canal exostoses in 10/15, sometimes severe narrowing. (lierop2013vanbuchemdisease pages 2-3)
- **Raised intracranial pressure:** documented in ~20%. (lierop2013vanbuchemdisease pages 1-2, lierop2012theroleof pages 82-85)
- **Very high BMD:** femoral neck mean 2.16 g/cm² (Z 8.7 ±2.1) and lumbar spine mean 2.13 g/cm² (Z 9.5 ±1.9). (lierop2013vanbuchemdisease pages 2-3)

Natural history from reviews and cohort data suggests progression in childhood/young adulthood with **stabilization after ~third decade** and **normal life expectancy**. (appelmandijkstra2026sclerosingbonedysplasias pages 6-8, lierop2012theroleof pages 82-85)

### 3.2 Quality-of-life impact
The most impactful manifestations are neurologic/sensory complications (facial palsy, hearing loss, visual compromise, pain/neuralgia), which can require repeated specialist evaluations and surgical interventions. (appelmandijkstra2026sclerosingbonedysplasias pages 1-3, appelmandijkstra2026sclerosingbonedysplasias pages 9-11)

### 3.3 Suggested HPO terms
A focused phenotype-to-HPO mapping for major features is provided in the artifact below.

| Phenotype (plain language) | Suggested HPO term(s) | Typical onset | Frequency/quant data (percentages or stats) | Progression/natural history | Key citations |
|---|---|---|---|---|---|
| Facial palsy / recurrent facial nerve compression | HP:0010628 Facial palsy; HP:0001303 Facial nerve paralysis | Usually childhood; median first episode 2.5 years in one Dutch cohort; can be present at birth | 100% (15/15) had past episodes of facial palsy in the 2013 Dutch cohort; broader comparison reported facial palsy in 89% of Van Buchem cases vs 93% in sclerosteosis | Often recurrent; may require decompression in selected cases; complications tend to stabilize after the third decade/adulthood | (lierop2013vanbuchemdisease pages 2-3, appelmandijkstra2026sclerosingbonedysplasias pages 3-6, lierop2012theroleof pages 82-85) |
| Hearing loss, often conductive first and later sensorineural | HP:0000365 Hearing impairment; HP:0000405 Conductive hearing impairment; HP:0000407 Sensorineural hearing impairment | Childhood onset | 14/15 (93%) had hearing impairment in the 2013 cohort; review notes childhood-onset conductive hearing loss with later sensorineural involvement; comparative review estimated hearing loss in 78% of Van Buchem disease vs 94% in sclerosteosis | Progressive cranial hyperostosis narrows canals/affects ossicles and cranial nerve VIII; hearing complications may stabilize in adulthood | (lierop2013vanbuchemdisease pages 2-3, appelmandijkstra2026sclerosingbonedysplasias pages 1-3, appelmandijkstra2026sclerosingbonedysplasias pages 6-8, appelmandijkstra2026sclerosingbonedysplasias pages 3-6) |
| Cranial nerve entrapment syndrome (VII, VIII, optic and other cranial nerves) | HP:0001291 Cranial nerve palsy; HP:0000648 Optic atrophy; HP:0000516 Visual impairment; HP:0000458 Facial asymmetry | Childhood to young adulthood, depending on site | Common disease-defining feature; includes facial palsy, hearing loss, visual loss/optic neuropathy, neuralgia/anosmia; external auditory canal exostoses in 10/15 and severe canal narrowing in some patients | Progressive skull/skull-base hyperostosis causes nerve compression; disease often becomes less progressive/stabilizes in adulthood | (appelmandijkstra2026sclerosingbonedysplasias pages 1-3, appelmandijkstra2026sclerosingbonedysplasias pages 6-8, lierop2013vanbuchemdisease pages 2-3, sebastian2018geneticsofsostsost pages 7-11) |
| Mandibular overgrowth and facial distortion (frontal bossing, enlarged jaw, proptosis) | HP:0000280 Coarse facial features; HP:0000347 Micrognathia/retrognathia not appropriate; suggested instead HP:0010800 Abnormal mandible morphology; HP:0002007 Frontal bossing; HP:0000520 Proptosis | Usually young adulthood for mandibular prominence; craniofacial changes accumulate over time | In adults, nearly all had facial distortion; 11/12 adults had large high forehead and 10/12 enlarged mandible in one cohort; comparative review reported cranial hyperostosis/facial distortion in 68% of Van Buchem cases | Progressive during growth/early adulthood; mandibular overgrowth most apparent in young adulthood; tends to stabilize in adulthood | (lierop2013vanbuchemdisease pages 2-3, appelmandijkstra2026sclerosingbonedysplasias pages 1-3, appelmandijkstra2026sclerosingbonedysplasias pages 6-8, sebastian2018geneticsofsostsost pages 1-7) |
| Markedly increased bone mineral density / generalized skeletal hyperostosis | HP:0005684 Increased bone mineral density; HP:0003014 Hyperostosis; HP:0000923 Generalized osteosclerosis | Detectable in childhood, increases with age | DXA in review: spine Z-scores about +5.4 to +12.3 and hip Z-scores about +5.2 to +12.1; 2013 cohort mean femoral neck Z-score 8.7 ± 2.1 and spine Z-score 9.5 ± 1.9; skeleton described as ~3–4 times heavier than normal in older review literature | BMD rises with age and tends to plateau/stabilize in late adulthood; fracture risk not reported as increased | (appelmandijkstra2026sclerosingbonedysplasias pages 6-8, lierop2013vanbuchemdisease pages 1-2, lierop2012theroleof pages 66-73, sebastian2018geneticsofsostsost pages 1-7) |
| Increased intracranial pressure | HP:0002516 Increased intracranial pressure | Usually later childhood to adulthood; severe cases | About 20% in the Dutch cohort/review; comparative review reported 16% in Van Buchem disease vs 71% in sclerosteosis | Uncommon but serious complication of cranial hyperostosis; rare in Van Buchem disease relative to sclerosteosis; can necessitate decompressive procedures or shunting in severe cases | (lierop2013vanbuchemdisease pages 1-2, lierop2012theroleof pages 82-85, appelmandijkstra2026sclerosingbonedysplasias pages 3-6, appelmandijkstra2026sclerosingbonedysplasias pages 9-11) |


*Table: This table summarizes the core clinical phenotypes of Van Buchem disease with suggested HPO mappings, typical onset, quantitative frequency data, and natural history. It is useful for knowledge-base curation and phenotype annotation.*

---

## 4. Genetic / molecular information
### 4.1 Causal gene(s) and locus
- **Primary causal locus:** SOST regulatory landscape (downstream deletion), chromosome **17q12–q21** in the **SOST–MEOX1 intergenic region**. (balemans2002identificationofa pages 1-2, staehling‐hampton2002a52kbdeletion pages 4-5)
- **Gene implicated mechanistically:** **SOST** (encodes sclerostin), an osteocyte-derived inhibitor of bone formation via antagonism of canonical Wnt signaling. (loots2005genomicdeletionof pages 3-4, charoenngam2022hereditarymetabolicbone pages 11-13)

### 4.2 Pathogenic variants
**Canonical pathogenic lesion:** biallelic ~52-kb downstream deletion (noncoding CNV). (balemans2002identificationofa pages 1-2, lierop2013vanbuchemdisease pages 2-3)

**Breakpoint mechanism:** endpoints within Alu repeats; likely Alu-mediated homologous recombination. (staehling‐hampton2002a52kbdeletion pages 4-5)

**Variant class:** germline, structural variant (deletion), noncoding regulatory. (balemans2002identificationofa pages 1-2, staehling‐hampton2002a52kbdeletion pages 4-5)

### 4.3 Functional consequences
Loots et al. functionally linked the deletion to loss of a distant bone enhancer. As described in the abstract, they concluded: “Only the SOST(wt) allele faithfully expressed high levels of human SOST in the adult bone… consistent with the model that the VB noncoding deletion removes a SOST-specific regulatory element.” (Genome Research, 2005-06; DOI: 10.1101/gr.3437105) (loots2005genomicdeletionof pages 3-4)

### 4.4 Modifier genes / epigenetics
No specific modifier genes or epigenetic mechanisms for VBD severity were identified in the retrieved sources.

### 4.5 Variant frequency in population databases
Allele frequencies (e.g., gnomAD) were not reported in the sourced texts.

**Genetics artifact**
| Gene/locus | Variant type | Canonical lesion description | Mechanism | Inheritance | Founder/population notes | Key primary references |
|---|---|---|---|---|---|---|
| **SOST regulatory region** | Structural variant; biallelic noncoding deletion | Recurrent **~52-kb homozygous deletion** located **~35 kb downstream of SOST** on **17q12-q21** | Removes a distal **bone-specific cis-regulatory enhancer**, causing reduced **SOST/sclerostin** expression and excess bone formation (balemans2002identificationofa pages 1-2, loots2005genomicdeletionof pages 3-4) | **Autosomal recessive** (balemans2002identificationofa pages 1-2, appelmandijkstra2026sclerosingbonedysplasias pages 1-3) | Classic Dutch Van Buchem families; strong clustering in the **Netherlands**, especially a small founder village/population (staehling‐hampton2002a52kbdeletion pages 4-5, lierop2013vanbuchemdisease pages 1-2, lierop2012theroleof pages 66-73) | Balemans et al., 2002, *J Med Genet* DOI: 10.1136/jmg.39.2.91; Staehling-Hampton et al., 2002, *Am J Med Genet* DOI: 10.1002/ajmg.10401 (balemans2002identificationofa pages 7-8, staehling‐hampton2002a52kbdeletion pages 4-5) |
| **SOST–MEOX1 intergenic region** | Intergenic deletion breakpoint-defined CNV | Deletion lies in the **SOST–MEOX1 intergenic region**; endpoints are normally **51.7 kb apart** and likely arose through **Alu-mediated homologous recombination** (staehling‐hampton2002a52kbdeletion pages 4-5) | Pathogenicity is regulatory rather than coding: neighboring **SOST** and **MEOX1** coding regions remain intact, supporting a **position effect / enhancer loss** model (staehling‐hampton2002a52kbdeletion pages 4-5, staehling‐hampton2002a52kbdeletion pages 8-9) | **Autosomal recessive** disease requires biallelic deletion (appelmandijkstra2026sclerosingbonedysplasias pages 1-3, appelmandijkstra2026sclerosingbonedysplasias pages 3-6) | All **15/15** Dutch patients in the 2002 series were homozygous for the deletion (staehling‐hampton2002a52kbdeletion pages 4-5); 2013 Dutch cohort confirmed deletion in **15/18 known Dutch patients** studied (lierop2013vanbuchemdisease pages 2-3) | Staehling-Hampton et al., 2002, *Am J Med Genet* DOI: 10.1002/ajmg.10401; van Lierop et al., 2013, *JBMR* DOI: 10.1002/jbmr.1794 (staehling‐hampton2002a52kbdeletion pages 4-5, lierop2013vanbuchemdisease pages 2-3) |
| **ECR5 within downstream SOST regulatory landscape** | Deleted enhancer element within noncoding interval | Comparative/in vivo functional studies localized a candidate enhancer, **ECR5**, **within the 52-kb deleted interval** downstream of **SOST** (loots2005genomicdeletionof pages 3-4, loots2005genomicdeletionof media ef8ab351) | **Loss of ECR5** abolishes normal osteoblast-lineage / bone expression control of **SOST**, yielding a **hypomorphic sclerostin-deficiency state** relative to sclerosteosis (loots2005genomicdeletionof pages 3-4) | Consistent with recessive disease due to markedly reduced but not absent sclerostin expression (staehling‐hampton2002a52kbdeletion pages 8-9, appelmandijkstra2026sclerosingbonedysplasias pages 6-8) | Explains why Van Buchem disease is usually **milder than sclerosteosis** and lacks typical syndactyly (loots2005genomicdeletionof pages 3-4, appelmandijkstra2026sclerosingbonedysplasias pages 3-6) | Loots et al., 2005, *Genome Research* DOI: 10.1101/gr.3437105 (loots2005genomicdeletionof pages 3-4, loots2005genomicdeletionof media ef8ab351) |
| **SOST (coding region)** | No causal coding variant in classic Van Buchem disease | In classic Van Buchem disease, **SOST coding mutations were not found**; this distinguishes it from **sclerosteosis**, where pathogenic **SOST loss-of-function coding variants** occur (balemans2002identificationofa pages 1-2, staehling‐hampton2002a52kbdeletion pages 8-9) | Disease results from **reduced transcription** of normal SOST protein rather than altered protein sequence (balemans2002identificationofa pages 1-2, loots2005genomicdeletionof pages 3-4) | Recessive | Important diagnostic implication: routine **single-gene sequencing of SOST may miss Van Buchem disease** if deletion analysis is not performed (appelmandijkstra2026sclerosingbonedysplasias pages 3-6) | Balemans et al., 2002, *J Med Genet* DOI: 10.1136/jmg.39.2.91; Loots et al., 2005, *Genome Research* DOI: 10.1101/gr.3437105 (balemans2002identificationofa pages 1-2, loots2005genomicdeletionof pages 3-4, appelmandijkstra2026sclerosingbonedysplasias pages 3-6) |
| **Cytogenetic/molecular testing target** | Targeted deletion analysis | Recommended lesion to test: **biallelic 52-kb deletion downstream of SOST**; methods reported/recommended include **qPCR, long-range PCR, MLPA, or gene-targeted microarray** because routine sequencing may not detect the lesion (appelmandijkstra2026sclerosingbonedysplasias pages 3-6) | Confirms molecular diagnosis and distinguishes Van Buchem disease from other high-bone-mass disorders and from SOST coding-variant sclerosteosis (appelmandijkstra2026sclerosingbonedysplasias pages 1-3, appelmandijkstra2026sclerosingbonedysplasias pages 3-6) | Recessive | Most informative in patients with compatible craniotubular hyperostosis, especially with Dutch ancestry/family history (appelmandijkstra2026sclerosingbonedysplasias pages 1-3, lierop2013vanbuchemdisease pages 1-2) | Appelman-Dijkstra & van Lierop review citing established molecular diagnosis; primary deletion papers as basis (appelmandijkstra2026sclerosingbonedysplasias pages 1-3, appelmandijkstra2026sclerosingbonedysplasias pages 3-6, balemans2002identificationofa pages 7-8, staehling‐hampton2002a52kbdeletion pages 4-5) |


*Table: This table summarizes the canonical molecular lesion in Van Buchem disease: a recessive 52-kb noncoding deletion downstream of SOST in the SOST–MEOX1 intergenic region. It highlights the enhancer-loss mechanism, founder context, and the primary studies that established the diagnosis.*

---

## 5. Environmental information
VBD is a Mendelian disorder driven by a specific recessive CNV; the retrieved sources did not provide evidence for environmental, lifestyle, or infectious contributors to disease risk or severity. (balemans2002identificationofa pages 1-2, lierop2013vanbuchemdisease pages 1-2)

---

## 6. Mechanism / pathophysiology
### 6.1 Molecular pathways
- **Canonical Wnt/β-catenin signaling** (increased activity secondary to reduced sclerostin inhibition) is central. Loss of SOST activity produces high bone mass and craniofacial hyperostosis. (loots2005genomicdeletionof pages 3-4, charoenngam2022hereditarymetabolicbone pages 11-13)

### 6.2 Cellular processes
- **Increased osteoblast-mediated bone formation** with relatively normal/decreased osteoclastic resorption; histology in reviews emphasizes increased cortical/trabecular thickness without abnormal mineralization. (appelmandijkstra2026sclerosingbonedysplasias pages 6-8, charoenngam2022hereditarymetabolicbone pages 11-13)

### 6.3 Key tissue/cell types and ontology suggestions
- **Primary cell type:** osteocyte (sclerostin is osteocyte-derived) and osteoblast lineage. Suggested CL terms (approximate):
  - **CL:0000132 osteocyte**
  - **CL:0000062 osteoblast**

Suggested GO Biological Process terms (examples aligned to mechanism):
- **GO:0001503 ossification**
- **GO:0045773 positive regulation of bone mineralization**
- **GO:0030282 bone mineralization**
- **GO:0044338 canonical Wnt signaling pathway**

### 6.4 Quantitative biomarker/statistics supporting mechanism
In the Dutch cohort:
- Serum sclerostin (patients) mean **8.0 pg/mL** (95% CI 4.9–11.0) vs carriers 28.7 and controls ~40.0; sclerostin inversely correlated with BMD (lumbar spine r = −0.78). (lierop2013vanbuchemdisease pages 1-2, lierop2012theroleof pages 66-73)
- Bone formation marker P1NP (adult patients) mean **96.0 ng/mL**, higher than carriers and controls. (lierop2013vanbuchemdisease pages 1-2)

### 6.5 Recent developments (2023–2024)
Direct 2023–2024 VBD-specific clinical cohorts were not retrieved in this run; however, there are relevant mechanistic advances in the broader “high bone mass from increased Wnt signaling” space:
- A 2023 mouse study demonstrated that **chemical inhibition of porcupine (Wnt secretion)** reduces both trabecular and cortical bone mass in multiple high-bone-mass models, including **Sost loss-of-function** (used as a sclerosteosis model), supporting that continued Wnt ligand production sustains the high-bone-mass state and providing a plausible conceptual strategy for symptomatic relief in related disorders. (Bone Research, 2023-08; DOI: 10.1038/s41413-023-00278-5) ()

**Visual evidence (SOST locus and deleted enhancer interval)**
The following figure panels document the downstream SOST deletion interval and conserved enhancer element(s) implicated in VBD.
(loots2005genomicdeletionof media ef8ab351, loots2005genomicdeletionof media 6d141620)

---

## 7. Anatomical structures affected
### 7.1 Organ/system level
Primary system: **skeletal system**, especially craniofacial and tubular bone cortices.
- Skull/calvarium/skull base: hyperostosis and sclerosis (appelmandijkstra2026sclerosingbonedysplasias pages 1-3, dixon1982twocasesof pages 1-3)
- Mandible: overgrowth (appelmandijkstra2026sclerosingbonedysplasias pages 1-3, lierop2013vanbuchemdisease pages 2-3)
- Temporal bone/external auditory canal/internal auditory canal: narrowing/exostoses contributing to hearing loss (lierop2013vanbuchemdisease pages 2-3, dixon1982twocasesof pages 1-3)
- Long bone diaphyses, ribs, clavicles: cortical thickening/hyperostosis (appelmandijkstra2026sclerosingbonedysplasias pages 1-3, dixon1982twocasesof pages 3-5)

Suggested UBERON terms (examples):
- **UBERON:0003129 calvaria**
- **UBERON:0001712 mandible**
- **UBERON:0001846 temporal bone**
- **UBERON:0002101 femur** (diaphysis emphasis)

### 7.2 Subcellular localization
Key dysfunctional molecule is secreted sclerostin (extracellular). Suggested GO Cellular Component:
- **GO:0005576 extracellular region**

---

## 8. Temporal development
- **Onset:** often **childhood** (facial palsy median 2.5 years; childhood hearing loss) (lierop2013vanbuchemdisease pages 2-3, appelmandijkstra2026sclerosingbonedysplasias pages 6-8)
- **Course:** progressive hyperostosis through growth/early adulthood with **stabilization after ~third decade** (sebastian2018geneticsofsostsost pages 1-7, lierop2012theroleof pages 82-85)
- **Duration:** lifelong, chronic; life expectancy appears normal in modern reviews and older surgical case follow-up into old age. (appelmandijkstra2026sclerosingbonedysplasias pages 6-8, dixon1982twocasesof pages 1-3)

---

## 9. Inheritance and population
- **Inheritance:** **autosomal recessive** (balemans2002identificationofa pages 1-2, dixon1982twocasesof pages 1-3)
- **Geography/population:** strong Dutch founder association; a cluster was described in a small Dutch village (13 cases) and later Dutch cohorts captured most known national cases. (lierop2013vanbuchemdisease pages 1-2, lierop2013vanbuchemdisease pages 2-3)

**Epidemiology statistics in retrieved sources:**
- “Approximately 30” described cases (review-level statement) (lierop2012theroleof pages 77-82)
- A modern reference text cites ~31 reported individuals mainly from the Netherlands/Germany (appelmandijkstra2026sclerosingbonedysplasias pages 8-9)
- Dutch cohort included 15 of 18 known Dutch patients at the time. (lierop2013vanbuchemdisease pages 2-3)

Prevalence/incidence and carrier frequency specific to VBD were not retrieved from Orphanet or population datasets in the sourced texts.

---

## 10. Diagnostics
### 10.1 Clinical and imaging diagnosis
Diagnosis relies on characteristic craniotubular hyperostosis with cranial-nerve entrapment symptoms, plus radiographic and densitometric confirmation of marked hyperostosis and very high BMD. (appelmandijkstra2026sclerosingbonedysplasias pages 1-3, lierop2013vanbuchemdisease pages 2-3)

### 10.2 Genetic testing approach
Because the causal lesion is a **noncoding deletion**, **SOST sequencing can be negative**; recommended molecular confirmation requires **targeted deletion/CNV testing** (e.g., qPCR, long-range PCR, MLPA, targeted microarray). (appelmandijkstra2026sclerosingbonedysplasias pages 3-6, staehling‐hampton2002a52kbdeletion pages 4-5)

### 10.3 Differential diagnosis (key distinctions)
- **Sclerosteosis (SOST coding loss-of-function):** typically more severe; syndactyly and tall stature may help distinguish it from VBD (VBD typically lacks syndactyly and has normal stature). (appelmandijkstra2026sclerosingbonedysplasias pages 3-6, appelmandijkstra2026sclerosingbonedysplasias pages 6-8)
- Other craniotubular hyperostoses (e.g., craniometaphyseal dysplasia, Camurati–Engelmann disease) require imaging/genetic differentiation; explicit differentials were not comprehensively retrieved in this run.

---

## 11. Outcome / prognosis
- **Life expectancy:** appears normal; cases followed into old age and modern reviews state life expectancy is generally normal. (appelmandijkstra2026sclerosingbonedysplasias pages 6-8, dixon1982twocasesof pages 1-3)
- **Stabilization:** clinical complications and BMD tend to stabilize after the third decade; P1NP declines with age in cohorts, consistent with reduced progression later. (lierop2012theroleof pages 82-85)
- **Major morbidity drivers:** cranial nerve compression (facial palsy, hearing loss, visual compromise), and occasional intracranial hypertension or spinal stenosis. (lierop2013vanbuchemdisease pages 2-3, lierop2012theroleof pages 77-82, dixon1982twocasesof pages 3-5)

---

## 12. Treatment
### 12.1 Current real-world management
No established disease-modifying therapy exists in the retrieved VBD-focused clinical literature; management is predominantly symptomatic and surgical.

Examples reported/recommended:
- **Hearing interventions:** hearing aids, middle ear surgery, cochlear implants (appelmandijkstra2026sclerosingbonedysplasias pages 1-3, appelmandijkstra2026sclerosingbonedysplasias pages 9-11)
- **Facial nerve decompression:** performed in 6/15 in one cohort (lierop2013vanbuchemdisease pages 2-3)
- **Orbital decompression, mandibular reduction, and decompressive cranial surgery/VP shunting** for selected severe complications (appelmandijkstra2026sclerosingbonedysplasias pages 1-3, appelmandijkstra2026sclerosingbonedysplasias pages 9-11)

Older neurosurgical case series demonstrate feasibility of partial/bilateral craniectomy with symptom relief and long survival, though later neurologic complications from progressive bony encroachment can occur. (dixon1982twocasesof pages 1-3, dixon1982twocasesof pages 3-5)

### 12.2 Medical therapy (limited/experimental)
A case-level report described **prednisone** associated with a “dramatic decrease in bone formation” and no further increase in spine/hip BMD during therapy, with biochemical markers tracking dose, suggesting glucocorticoids might be explored as a medical alternative when surgery is difficult; evidence is limited and not sufficient to establish standard care. (lierop2012theroleof pages 97-100)

### 12.3 Emerging/experimental direction (mechanism-driven)
Because VBD is driven by **increased Wnt signaling** secondary to reduced sclerostin, the most conceptually aligned disease-modifying approach would be to **reduce Wnt pathway output**; a 2023 preclinical study showed **porcupine inhibition** reduced high bone mass in Sost-loss mouse models. Translation to VBD has not been established. ()

**Treatment/diagnostics artifact with MAXO mappings**
| Domain | Test/intervention | What it shows / goal | Real-world implementation notes | Suggested MAXO term(s) | Key citations |
|---|---|---|---|---|---|
| Imaging | DXA (spine, hip/femoral neck) | Quantifies markedly elevated bone mineral density; supports diagnosis and follow-up | In Dutch cohort, mean femoral neck BMD 2.16 g/cm² (Z-score 8.7 ± 2.1) and spine BMD 2.13 g/cm² (Z-score 9.5 ± 1.9); review reports spine Z-scores ~+5.4 to +12.3 and hip ~+5.2 to +12.1; serial BMD may help document stabilization in adulthood, though frequent testing may have limited management impact | MAXO: measurement of bone mineral density | (lierop2013vanbuchemdisease pages 2-3, appelmandijkstra2026sclerosingbonedysplasias pages 6-8, appelmandijkstra2026sclerosingbonedysplasias pages 9-11) |
| Imaging | Plain radiographs | Demonstrate endosteal hyperostosis and altered bone contours | Typical findings include calvarial/skull-base widening and sclerosis, hyperostosis of tubular bone shafts, broad dense clavicles and ribs, sclerosis of scapulae/pelvis, narrowing of medullary cavity; useful for differential diagnosis versus osteopetrosis and other craniotubular dysplasias | MAXO: radiography | (appelmandijkstra2026sclerosingbonedysplasias pages 1-3, charoenngam2022hereditarymetabolicbone pages 11-13, dixon1982twocasesof pages 1-3, dixon1982twocasesof pages 3-5) |
| Imaging | CT of skull/temporal bones | Defines skull thickness, foraminal/canal narrowing, cranial nerve entrapment, surgical anatomy | CT shows marked cranial vault and skull-base thickening, petrous bone involvement, occipital exostoses, mastoid/internal auditory canal narrowing; used when hearing loss, facial palsy, visual symptoms, or raised ICP are suspected | MAXO: computed tomography imaging | (appelmandijkstra2026sclerosingbonedysplasias pages 1-3, lierop2012theroleof pages 77-82, dixon1982twocasesof pages 1-3, sebastian2018geneticsofsostsost pages 7-11) |
| Functional assessment | Audiology assessment | Detects conductive and sensorineural hearing loss and guides hearing intervention | Hearing impairment reported in 14/15 patients in one cohort; childhood-onset conductive loss may progress to sensorineural involvement; recommended for surveillance and treatment planning | MAXO: audiologic evaluation | (lierop2013vanbuchemdisease pages 2-3, appelmandijkstra2026sclerosingbonedysplasias pages 6-8, appelmandijkstra2026sclerosingbonedysplasias pages 1-3, appelmandijkstra2026sclerosingbonedysplasias pages 9-11) |
| Functional assessment | Ophthalmology assessment | Evaluates optic neuropathy, proptosis, papilledema, vision loss, signs of raised ICP | Recommended regularly because cranial hyperostosis can compromise optic canals and orbit; may trigger orbital decompression or ICP-directed procedures | MAXO: ophthalmologic examination | (appelmandijkstra2026sclerosingbonedysplasias pages 1-3, appelmandijkstra2026sclerosingbonedysplasias pages 9-11) |
| Functional assessment | Neurologic / cranial nerve assessment | Detects facial palsy, neuralgia, anosmia, myelopathy, and signs of intracranial hypertension | Facial palsy occurred in 100% of patients in one Dutch cohort, median first occurrence age 2.5 years; neurologic follow-up is central to timing decompression procedures | MAXO: neurologic examination | (lierop2013vanbuchemdisease pages 2-3, appelmandijkstra2026sclerosingbonedysplasias pages 6-8, appelmandijkstra2026sclerosingbonedysplasias pages 1-3, appelmandijkstra2026sclerosingbonedysplasias pages 9-11) |
| Labs | Bone turnover markers (P1NP, alkaline phosphatase, osteocalcin, CTX) | Reflect increased bone formation and age-related change in turnover | Adult patients had mean P1NP 96.0 ng/mL vs 47.8 in carriers and 37.8 in controls; CTX may be increased in childhood then decline toward low-normal adulthood; routine Ca/P/PTH often not consistently abnormal | MAXO: laboratory test; MAXO: measurement of bone turnover biomarker | (lierop2013vanbuchemdisease pages 1-2, appelmandijkstra2026sclerosingbonedysplasias pages 6-8, charoenngam2022hereditarymetabolicbone pages 11-13) |
| Labs | Serum sclerostin | Mechanistic biomarker showing reduced but usually detectable sclerostin | Mean serum sclerostin ~8.0 pg/mL in patients vs 28.7 in carriers and ~40.0 in controls; lower than normal but typically detectable, unlike sclerosteosis where it may be undetectable | MAXO: measurement of circulating biomarker | (lierop2013vanbuchemdisease pages 1-2, appelmandijkstra2026sclerosingbonedysplasias pages 6-8, lierop2012theroleof pages 66-73) |
| Genetics | Targeted deletion testing for the 52-kb downstream SOST lesion (qPCR, long-range PCR, MLPA, targeted microarray) | Confirms diagnosis by identifying the canonical biallelic pathogenic noncoding deletion in the SOST–MEOX1 intergenic region at 17q12-q21 | Important because routine single-gene SOST sequencing may miss the pathogenic regulatory deletion; deletion testing is specifically recommended when phenotype suggests Van Buchem disease | MAXO: genetic testing; MAXO: copy number variation analysis | (appelmandijkstra2026sclerosingbonedysplasias pages 3-6, appelmandijkstra2026sclerosingbonedysplasias pages 1-3, balemans2002identificationofa pages 1-2, staehling‐hampton2002a52kbdeletion pages 4-5) |
| Genetics | Sequence analysis of SOST coding region | Mainly differential diagnosis with sclerosteosis rather than primary test for classic Van Buchem disease | Van Buchem disease usually lacks SOST coding mutations; negative sequencing does not exclude disease because the canonical lesion is noncoding | MAXO: sequence analysis | (balemans2002identificationofa pages 1-2, loots2005genomicdeletionof pages 3-4, appelmandijkstra2026sclerosingbonedysplasias pages 3-6) |
| Surgery | Facial nerve decompression | Relieves recurrent or progressive facial nerve entrapment/palsy | Performed in 6/15 patients in one cohort; used for clinically significant recurrent palsy or nerve compression; literature suggests pediatric cases may also require decompression | MAXO: nerve decompression surgery | (lierop2013vanbuchemdisease pages 2-3, appelmandijkstra2026sclerosingbonedysplasias pages 1-3, appelmandijkstra2026sclerosingbonedysplasias pages 9-11) |
| Supportive / surgical | Hearing aids, middle ear surgery, cochlear implantation | Improves functional hearing in conductive or mixed hearing loss | Review recommends hearing aids or middle ear surgery; cochlear implant considered when canal obliteration or auditory nerve damage limits conventional options | MAXO: hearing aid provision; MAXO: cochlear implantation; MAXO: otologic surgery | (appelmandijkstra2026sclerosingbonedysplasias pages 1-3, appelmandijkstra2026sclerosingbonedysplasias pages 9-11) |
| Surgery | Orbital decompression | Relieves proptosis and optic/orbital compression | Considered for severe orbital crowding or visual compromise due to cranial hyperostosis | MAXO: orbital decompression surgery | (appelmandijkstra2026sclerosingbonedysplasias pages 1-3, appelmandijkstra2026sclerosingbonedysplasias pages 9-11) |
| Surgery | Mandibular reduction / corrective craniofacial surgery | Addresses mandibular overgrowth and facial distortion; may improve function/cosmesis | Mandibular enlargement is common in adulthood; one cohort noted corrective mandibular surgery in 1 patient; technically challenging because bone is very thick and dense | MAXO: mandibular reduction surgery; MAXO: craniofacial reconstructive surgery | (appelmandijkstra2026sclerosingbonedysplasias pages 1-3, lierop2013vanbuchemdisease pages 2-3, appelmandijkstra2026sclerosingbonedysplasias pages 9-11) |
| Surgery | Craniectomy / cranial decompression | Treats raised intracranial pressure and restricted intracranial volume | Used in severe cases; older case reports describe partial/bilateral craniectomies with recovery from early symptoms and long survival, though later neurologic morbidity can still occur; review notes ICP is less common in Van Buchem disease than in sclerosteosis | MAXO: craniectomy; MAXO: cranial decompression surgery | (dixon1982twocasesof pages 1-3, dixon1982twocasesof pages 3-5, appelmandijkstra2026sclerosingbonedysplasias pages 1-3, lierop2012theroleof pages 82-85) |
| Surgery | Ventriculoperitoneal shunt | CSF diversion for raised intracranial pressure / hydrocephalus-like presentation | Recommended when ICP increases and decompression alone is not sufficient or appropriate; especially relevant in severe cranial involvement | MAXO: ventriculoperitoneal shunt placement | (appelmandijkstra2026sclerosingbonedysplasias pages 1-3, appelmandijkstra2026sclerosingbonedysplasias pages 9-11) |
| Supportive | Dental / orthodontic care | Manages facial skeletal changes and occlusal/oral complications | Included in multidisciplinary surveillance because mandibular overgrowth and craniofacial remodeling can affect dentofacial function even when teeth are often relatively spared | MAXO: dental management; MAXO: orthodontic treatment | (appelmandijkstra2026sclerosingbonedysplasias pages 1-3, appelmandijkstra2026sclerosingbonedysplasias pages 9-11, appelmandijkstra2026sclerosingbonedysplasias pages 6-8) |
| Medical (experimental/limited evidence) | Glucocorticoids (prednisone) | Attempt to suppress excessive bone turnover and slow further BMD increase | Evidence limited to case-level experience: prednisone decreased formation/resorption markers and prevented further spine/hip BMD increase in one patient, but broader review notes little clinical benefit in two children and repeat surgeries may still be needed; not established standard therapy | MAXO: glucocorticoid therapy | (lierop2012theroleof pages 97-100, appelmandijkstra2026sclerosingbonedysplasias pages 9-11) |
| Care model | Multidisciplinary surveillance | Early detection of hearing, visual, dental, cranial nerve, and ICP complications | Suggested follow-up includes periodic DXA/biochemistry, audiology, ophthalmology, neurology, dental assessment, and genetic counseling; recommendations are expert-opinion based because formal clinical guidelines are lacking | MAXO: clinical surveillance; MAXO: genetic counseling | (appelmandijkstra2026sclerosingbonedysplasias pages 1-3, appelmandijkstra2026sclerosingbonedysplasias pages 9-11, appelmandijkstra2026sclerosingbonedysplasias pages 8-9) |


*Table: This table summarizes the main diagnostic evaluations and current management approaches for Van Buchem disease, emphasizing what each test or intervention is used for in practice. It is useful for translating the literature into a structured clinical workflow, including targeted genetic testing and symptom-directed surgical care.*

---

## 13. Prevention
Primary prevention is genetic (carrier detection and reproductive counseling) rather than environmental.
- **Genetic counseling** and **cascade testing** in families from high-risk founder contexts are the most relevant prevention strategies, given autosomal recessive inheritance and a recurrent deletion. (appelmandijkstra2026sclerosingbonedysplasias pages 3-6, lierop2013vanbuchemdisease pages 2-3)

No newborn screening or population screening programs were identified in retrieved sources.

---

## 14. Other species / natural disease
No naturally occurring non-human (“spontaneous”) animal disease analogs for VBD were identified in the retrieved sources.

---

## 15. Model organisms
Although VBD itself is caused by a regulatory deletion, experimental **Sost loss-of-function** and **Sost enhancer perturbation** models are widely used to study sclerostin biology.
- Functional dissection of the VBD deletion interval identified bone enhancer activity (ECR5) in vivo and in vitro. (loots2005genomicdeletionof pages 3-4)
- A 2023 study used Sost loss-of-function high-bone-mass mice to demonstrate porcupine inhibition reduces bone mass, supporting the Wnt-dependence of the phenotype. ()

---

## Recent (2023–2024) literature emphasis (what was found vs not found)
- **Found (2023):** mechanistic preclinical study on Wnt secretion inhibition in Sost LOF high-bone-mass mice, relevant to the VBD pathway. ()
- **Not retrieved in this run:** 2023–2024 primary clinical series specifically on VBD; Orphanet and ICD/MeSH identifier pages; variant population frequencies from gnomAD; VBD-specific clinical trials.

---

## Key primary references with URLs and publication dates (from retrieved texts)
- Balemans W, et al. **“Identification of a 52 kb deletion downstream of the SOST gene in patients with van Buchem disease”** *J Med Genet* (2002-02). https://doi.org/10.1136/jmg.39.2.91 (balemans2002identificationofa pages 1-2)
- Staehling-Hampton K, et al. **“A 52-kb deletion in the SOST–MEOX1 intergenic region… associated with van Buchem disease”** *Am J Med Genet* (2002-06). https://doi.org/10.1002/ajmg.10401 (staehling‐hampton2002a52kbdeletion pages 4-5)
- Loots GG, et al. **“Genomic deletion of a long-range bone enhancer misregulates sclerostin in Van Buchem disease”** *Genome Research* (2005-06). https://doi.org/10.1101/gr.3437105 (loots2005genomicdeletionof pages 3-4)
- van Lierop AH, et al. **“Van Buchem disease: Clinical, biochemical, and densitometric features of patients and disease carriers”** *JBMR* (2013-04). https://doi.org/10.1002/jbmr.1794 (lierop2013vanbuchemdisease pages 1-2)
- Dixon JM, et al. **“Two cases of Van Buchem’s disease”** *J Neurol Neurosurg Psychiatry* (1982-10). https://doi.org/10.1136/jnnp.45.10.913 (dixon1982twocasesof pages 1-3)
- Diegel CR, et al. **“Inhibiting WNT secretion reduces high bone mass caused by Sost loss-of-function…”** *Bone Research* (2023-08). https://doi.org/10.1038/s41413-023-00278-5 ()


References

1. (balemans2002identificationofa pages 1-2): W. Balemans, Neela M. Patel, M. Ebeling, E. Hul, W. Wuyts, C. Lacza, M. Dioszegi, F. Dikkers, P. Hildering, P. Willems, J. Verheij, K. Lindpaintner, B. Vickery, D. Foernzler, and W. Hul. Identification of a 52 kb deletion downstream of the sost gene in patients with van buchem disease. Journal of Medical Genetics, 39:91-97, Feb 2002. URL: https://doi.org/10.1136/jmg.39.2.91, doi:10.1136/jmg.39.2.91. This article has 834 citations and is from a domain leading peer-reviewed journal.

2. (loots2005genomicdeletionof pages 3-4): Gabriela G. Loots, Michaela Kneissel, Hansjoerg Keller, Myma Baptist, Jessie Chang, Nicole M. Collette, Dmitriy Ovcharenko, Ingrid Plajzer-Frick, and Edward M. Rubin. Genomic deletion of a long-range bone enhancer misregulates sclerostin in van buchem disease. Genome Research, 15:928-935, Jun 2005. URL: https://doi.org/10.1101/gr.3437105, doi:10.1101/gr.3437105. This article has 541 citations and is from a highest quality peer-reviewed journal.

3. (lierop2013vanbuchemdisease pages 1-2): Antoon H van Lierop, Neveen AT Hamdy, Martje E van Egmond, Egbert Bakker, Freek G Dikkers, and Socrates E Papapoulos. Van buchem disease: clinical, biochemical, and densitometric features of patients and disease carriers. Journal of Bone and Mineral Research, 28:848-854, Apr 2013. URL: https://doi.org/10.1002/jbmr.1794, doi:10.1002/jbmr.1794. This article has 156 citations and is from a highest quality peer-reviewed journal.

4. (appelmandijkstra2026sclerosingbonedysplasias pages 1-3): N Appelman-Dijkstra and A Van Lierop. Sclerosing bone dysplasias. Genetics of Bone Biology and Skeletal Disease, pages 651-668, Jan 2026. URL: https://doi.org/10.1016/b978-0-443-13683-2.00039-6, doi:10.1016/b978-0-443-13683-2.00039-6. This article has 17 citations.

5. (appelmandijkstra2026sclerosingbonedysplasias pages 17-18): N Appelman-Dijkstra and A Van Lierop. Sclerosing bone dysplasias. Genetics of Bone Biology and Skeletal Disease, pages 651-668, Jan 2026. URL: https://doi.org/10.1016/b978-0-443-13683-2.00039-6, doi:10.1016/b978-0-443-13683-2.00039-6. This article has 17 citations.

6. (staehling‐hampton2002a52kbdeletion pages 9-9): Karen Staehling‐Hampton, Sean Proll, Bryan W. Paeper, Lei Zhao, Patrick Charmley, Analisa Brown, Jessica C. Gardner, David Galas, Randall C. Schatzman, Peter Beighton, Socrates Papapoulos, Herman Hamersma, and Mary E. Brunkow. A 52-kb deletion in the sost-meox1 intergenic region on 17q12-q21 is associated with van buchem disease in the dutch population. American journal of medical genetics, 110 2:144-52, Jun 2002. URL: https://doi.org/10.1002/ajmg.10401, doi:10.1002/ajmg.10401. This article has 354 citations.

7. (appelmandijkstra2026sclerosingbonedysplasias pages 8-9): N Appelman-Dijkstra and A Van Lierop. Sclerosing bone dysplasias. Genetics of Bone Biology and Skeletal Disease, pages 651-668, Jan 2026. URL: https://doi.org/10.1016/b978-0-443-13683-2.00039-6, doi:10.1016/b978-0-443-13683-2.00039-6. This article has 17 citations.

8. (dixon1982twocasesof pages 1-3): J M Dixon, R E Cull, and P Gamble. Two cases of van buchem's disease. Journal of Neurology, Neurosurgery & Psychiatry, 45:913-918, Oct 1982. URL: https://doi.org/10.1136/jnnp.45.10.913, doi:10.1136/jnnp.45.10.913. This article has 45 citations.

9. (lierop2013vanbuchemdisease pages 2-3): Antoon H van Lierop, Neveen AT Hamdy, Martje E van Egmond, Egbert Bakker, Freek G Dikkers, and Socrates E Papapoulos. Van buchem disease: clinical, biochemical, and densitometric features of patients and disease carriers. Journal of Bone and Mineral Research, 28:848-854, Apr 2013. URL: https://doi.org/10.1002/jbmr.1794, doi:10.1002/jbmr.1794. This article has 156 citations and is from a highest quality peer-reviewed journal.

10. (dixon1982twocasesof pages 3-5): J M Dixon, R E Cull, and P Gamble. Two cases of van buchem's disease. Journal of Neurology, Neurosurgery & Psychiatry, 45:913-918, Oct 1982. URL: https://doi.org/10.1136/jnnp.45.10.913, doi:10.1136/jnnp.45.10.913. This article has 45 citations.

11. (staehling‐hampton2002a52kbdeletion pages 4-5): Karen Staehling‐Hampton, Sean Proll, Bryan W. Paeper, Lei Zhao, Patrick Charmley, Analisa Brown, Jessica C. Gardner, David Galas, Randall C. Schatzman, Peter Beighton, Socrates Papapoulos, Herman Hamersma, and Mary E. Brunkow. A 52-kb deletion in the sost-meox1 intergenic region on 17q12-q21 is associated with van buchem disease in the dutch population. American journal of medical genetics, 110 2:144-52, Jun 2002. URL: https://doi.org/10.1002/ajmg.10401, doi:10.1002/ajmg.10401. This article has 354 citations.

12. (lierop2012theroleof pages 66-73): A. H. van Lierop, N. A. T. Hamdy, R. L. van Bezooijen, C. W. Löwik, and S. E. Papapoulos. The role of sclerostin in the pathophysiology of sclerosing bone dysplasias. Clinical Reviews in Bone and Mineral Metabolism, 10:108-116, Jun 2012. URL: https://doi.org/10.1007/s12018-011-9123-5, doi:10.1007/s12018-011-9123-5. This article has 22 citations.

13. (lierop2012theroleof pages 82-85): A. H. van Lierop, N. A. T. Hamdy, R. L. van Bezooijen, C. W. Löwik, and S. E. Papapoulos. The role of sclerostin in the pathophysiology of sclerosing bone dysplasias. Clinical Reviews in Bone and Mineral Metabolism, 10:108-116, Jun 2012. URL: https://doi.org/10.1007/s12018-011-9123-5, doi:10.1007/s12018-011-9123-5. This article has 22 citations.

14. (appelmandijkstra2026sclerosingbonedysplasias pages 6-8): N Appelman-Dijkstra and A Van Lierop. Sclerosing bone dysplasias. Genetics of Bone Biology and Skeletal Disease, pages 651-668, Jan 2026. URL: https://doi.org/10.1016/b978-0-443-13683-2.00039-6, doi:10.1016/b978-0-443-13683-2.00039-6. This article has 17 citations.

15. (appelmandijkstra2026sclerosingbonedysplasias pages 9-11): N Appelman-Dijkstra and A Van Lierop. Sclerosing bone dysplasias. Genetics of Bone Biology and Skeletal Disease, pages 651-668, Jan 2026. URL: https://doi.org/10.1016/b978-0-443-13683-2.00039-6, doi:10.1016/b978-0-443-13683-2.00039-6. This article has 17 citations.

16. (appelmandijkstra2026sclerosingbonedysplasias pages 3-6): N Appelman-Dijkstra and A Van Lierop. Sclerosing bone dysplasias. Genetics of Bone Biology and Skeletal Disease, pages 651-668, Jan 2026. URL: https://doi.org/10.1016/b978-0-443-13683-2.00039-6, doi:10.1016/b978-0-443-13683-2.00039-6. This article has 17 citations.

17. (sebastian2018geneticsofsostsost pages 7-11): Aimy Sebastian and Gabriela G. Loots. Genetics of sost/sost in sclerosteosis and van buchem disease animal models. Metabolism, 80:38-47, Mar 2018. URL: https://doi.org/10.1016/j.metabol.2017.10.005, doi:10.1016/j.metabol.2017.10.005. This article has 105 citations.

18. (sebastian2018geneticsofsostsost pages 1-7): Aimy Sebastian and Gabriela G. Loots. Genetics of sost/sost in sclerosteosis and van buchem disease animal models. Metabolism, 80:38-47, Mar 2018. URL: https://doi.org/10.1016/j.metabol.2017.10.005, doi:10.1016/j.metabol.2017.10.005. This article has 105 citations.

19. (charoenngam2022hereditarymetabolicbone pages 11-13): N Charoenngam, A Nasr, A Shirvani, and MF Holick. Hereditary metabolic bone diseases: a review of pathogenesis, diagnosis and management. genes 2022; 13: 1880. Unknown journal, 2022.

20. (balemans2002identificationofa pages 7-8): W. Balemans, Neela M. Patel, M. Ebeling, E. Hul, W. Wuyts, C. Lacza, M. Dioszegi, F. Dikkers, P. Hildering, P. Willems, J. Verheij, K. Lindpaintner, B. Vickery, D. Foernzler, and W. Hul. Identification of a 52 kb deletion downstream of the sost gene in patients with van buchem disease. Journal of Medical Genetics, 39:91-97, Feb 2002. URL: https://doi.org/10.1136/jmg.39.2.91, doi:10.1136/jmg.39.2.91. This article has 834 citations and is from a domain leading peer-reviewed journal.

21. (staehling‐hampton2002a52kbdeletion pages 8-9): Karen Staehling‐Hampton, Sean Proll, Bryan W. Paeper, Lei Zhao, Patrick Charmley, Analisa Brown, Jessica C. Gardner, David Galas, Randall C. Schatzman, Peter Beighton, Socrates Papapoulos, Herman Hamersma, and Mary E. Brunkow. A 52-kb deletion in the sost-meox1 intergenic region on 17q12-q21 is associated with van buchem disease in the dutch population. American journal of medical genetics, 110 2:144-52, Jun 2002. URL: https://doi.org/10.1002/ajmg.10401, doi:10.1002/ajmg.10401. This article has 354 citations.

22. (loots2005genomicdeletionof media ef8ab351): Gabriela G. Loots, Michaela Kneissel, Hansjoerg Keller, Myma Baptist, Jessie Chang, Nicole M. Collette, Dmitriy Ovcharenko, Ingrid Plajzer-Frick, and Edward M. Rubin. Genomic deletion of a long-range bone enhancer misregulates sclerostin in van buchem disease. Genome Research, 15:928-935, Jun 2005. URL: https://doi.org/10.1101/gr.3437105, doi:10.1101/gr.3437105. This article has 541 citations and is from a highest quality peer-reviewed journal.

23. (loots2005genomicdeletionof media 6d141620): Gabriela G. Loots, Michaela Kneissel, Hansjoerg Keller, Myma Baptist, Jessie Chang, Nicole M. Collette, Dmitriy Ovcharenko, Ingrid Plajzer-Frick, and Edward M. Rubin. Genomic deletion of a long-range bone enhancer misregulates sclerostin in van buchem disease. Genome Research, 15:928-935, Jun 2005. URL: https://doi.org/10.1101/gr.3437105, doi:10.1101/gr.3437105. This article has 541 citations and is from a highest quality peer-reviewed journal.

24. (lierop2012theroleof pages 77-82): A. H. van Lierop, N. A. T. Hamdy, R. L. van Bezooijen, C. W. Löwik, and S. E. Papapoulos. The role of sclerostin in the pathophysiology of sclerosing bone dysplasias. Clinical Reviews in Bone and Mineral Metabolism, 10:108-116, Jun 2012. URL: https://doi.org/10.1007/s12018-011-9123-5, doi:10.1007/s12018-011-9123-5. This article has 22 citations.

25. (lierop2012theroleof pages 97-100): A. H. van Lierop, N. A. T. Hamdy, R. L. van Bezooijen, C. W. Löwik, and S. E. Papapoulos. The role of sclerostin in the pathophysiology of sclerosing bone dysplasias. Clinical Reviews in Bone and Mineral Metabolism, 10:108-116, Jun 2012. URL: https://doi.org/10.1007/s12018-011-9123-5, doi:10.1007/s12018-011-9123-5. This article has 22 citations.