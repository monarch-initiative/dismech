---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T11:21:22.948920'
end_time: '2026-05-08T11:34:53.137864'
duration_seconds: 810.19
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: CN-Related Developmental and Epileptic Encephalopathy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 19
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CN-Related Developmental and Epileptic Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CN-Related Developmental and Epileptic Encephalopathy** covering all of the
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
- **Disease Name:** CN-Related Developmental and Epileptic Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CN-Related Developmental and Epileptic Encephalopathy** covering all of the
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


# CN-Related Developmental and Epileptic Encephalopathy (interpreted as **CNNM2-related DEE end of spectrum**) — Comprehensive Research Report

## Executive interpretation / scope note
The query term **“CN-related developmental and epileptic encephalopathy”** is not a standard disease label in the retrieved sources. Based on the best-matching, directly evidenced literature, this report treats the target as **CNNM2-related hypomagnesemia with seizures and neurodevelopmental impairment**, in which **biallelic (autosomal recessive) CNNM2 variants** can present as **severe developmental and epileptic encephalopathy (DEE) with brain malformations** (accogli2019cnnm2homozygousmutations pages 1-2, zhang2021cnnm2relateddisordersphenotype pages 5-6, arjona2014cnnm2mutationscause pages 7-9). Where the evidence discusses the broader CNNM2 spectrum (including milder autosomal dominant forms), this is explicitly noted.

---

## 1. Disease Information
### 1.1 Disease overview
**CNNM2-related hypomagnesemia with seizures and neurodevelopmental impairment** is a Mendelian disorder caused by pathogenic variants in **CNNM2 (cyclin M2)**, a protein implicated in **renal magnesium handling** and brain development/function. The phenotype spans:
- **Autosomal dominant (AD), often de novo heterozygous** variants with hypomagnesemia and variable seizures and developmental delay/intellectual disability.
- **Autosomal recessive (AR), biallelic** variants with **neonatal-onset refractory seizures**, severe developmental impairment, and **structural brain abnormalities**, consistent with a DEE phenotype (zhang2021cnnm2relateddisordersphenotype pages 1-2, zhang2021cnnm2relateddisordersphenotype pages 5-6, arjona2014cnnm2mutationscause pages 7-9).

### 1.2 Key identifiers
From primary literature:
- **HSMR syndrome** (“hypomagnesemia, seizures, and intellectual disability syndrome”), **MIM# 616418** (franken2021thephenotypicand pages 1-4).
- **HOMG6** (“autosomal dominant renal hypomagnesemia 6”), **MIM# 613882** (petrakis2022thep.pro482alavariant pages 1-2).
- The term **HOMGSMR1** (“Hypomagnesemia, seizures, and impaired intellectual development 1”) is used in recent literature (li2025twonovelvariants pages 1-2).
- **Gene**: **CNNM2** (OMIM gene entry **MIM 607803**) (arjona2014cnnm2mutationscause pages 1-2); also noted as previously known as **ACDP2** (zhang2021cnnm2relateddisordersphenotype pages 1-2).

Not found in retrieved full texts during this run: **MONDO, Orphanet, MeSH, ICD-10/ICD-11** codes/IDs.

### 1.3 Synonyms / alternative names
- Hypomagnesemia, seizures, and intellectual disability syndrome (**HSMR**, **HSMR1**) (franken2021thephenotypicand pages 1-4, petrakis2022thep.pro482alavariant pages 1-2, tseng2022novelcnnm2mutation pages 1-2).
- Hypomagnesemia, seizures, and impaired intellectual development 1 (**HOMGSMR1**) (li2025twonovelvariants pages 1-2).
- Autosomal dominant renal hypomagnesemia 6 (**HOMG6**) (petrakis2022thep.pro482alavariant pages 1-2).
- “CNNM2-related disorders” (umbrella term used in cohort synthesis) (zhang2021cnnm2relateddisordersphenotype pages 1-2).

### 1.4 Evidence provenance
The disease characterization here is derived from **aggregated disease-level resources in the primary literature** (case series + literature reviews) and **individual patient case reports** (zhang2021cnnm2relateddisordersphenotype pages 1-2, franken2021thephenotypicand pages 10-12, arjona2014cnnm2mutationscause pages 1-2, accogli2019cnnm2homozygousmutations pages 1-2).

---

## 2. Etiology
### 2.1 Disease causal factors
**Primary cause: genetic** — pathogenic variants in **CNNM2**.
- A foundational report identified CNNM2 mutations in families with “mental retardation, seizures, and hypomagnesemia,” including both **de novo heterozygous** and **recessive** inheritance (arjona2014cnnm2mutationscause pages 1-2).
- Severe DEE presentations are enriched in **biallelic/homozygous** cases, described as “severe refractory hypomagnesemia, epileptic encephalopathy and brain malformations” (accogli2019cnnm2homozygousmutations pages 1-2).

**Mechanistic cause (proximal physiology): renal magnesium wasting / dysregulated Mg2+ handling** with downstream neurodevelopmental dysfunction (arjona2014cnnm2mutationscause pages 1-2, arjona2014cnnm2mutationscause pages 7-9, bosman2024hypomagnesaemiawithvarying pages 1-2).

### 2.2 Risk factors
- **Genetic risk**: carrying heterozygous or biallelic pathogenic variants in CNNM2; severity correlates with allelic state and domain (DUF21 vs CBS2 associations) (zhang2021cnnm2relateddisordersphenotype pages 1-2, zhang2021cnnm2relateddisordersphenotype pages 5-6, bosman2024hypomagnesaemiawithvarying pages 1-2).
- **Non-genetic/environmental risk factors** were not clearly specified for CNNM2-DEE in the retrieved evidence.

### 2.3 Protective factors
No protective variants or protective environmental factors were identified in the retrieved primary texts.

### 2.4 Gene–environment interactions
No direct CNNM2-specific gene–environment interaction evidence was found in the retrieved literature.

---

## 3. Phenotypes (human)
### 3.1 Core phenotypes and suggested HPO terms
**Neurologic (DEE-relevant)**
- Seizures (**HP:0001250**) (zhang2021cnnm2relateddisordersphenotype pages 5-6, arjona2014cnnm2mutationscause pages 7-9)
- Developmental delay / global developmental delay (**HP:0001263**) and Intellectual disability (**HP:0001249**) (zhang2021cnnm2relateddisordersphenotype pages 5-6, franken2021thephenotypicand pages 10-12)
- Speech delay (**HP:0000750**) (franken2021thephenotypicand pages 10-12)
- Hypotonia (**HP:0001252**) (reported in severe cases) (accogli2019cnnm2homozygousmutations pages 1-2, zhang2021cnnm2relateddisordersphenotype pages 4-4)
- Microcephaly (**HP:0000252**) (zhang2021cnnm2relateddisordersphenotype pages 4-4, accogli2019cnnm2homozygousmutations pages 1-2)
- Autism / autistic features (**HP:0000729**) in some patients (arjona2014cnnm2mutationscause pages 2-4, franken2021thephenotypicand pages 10-12)

**Biochemical**
- Hypomagnesemia (**HP:0002917**) typically with renal wasting (arjona2014cnnm2mutationscause pages 2-4, bosman2024hypomagnesaemiawithvarying pages 1-2)

**Growth/other**
- Obesity (**HP:0001513**) is common in heterozygous cohorts (franken2021thephenotypicand pages 10-12)

### 3.2 Phenotype characteristics (onset, severity, progression)
**Seizure onset and severity stratified by inheritance**
- **AR/biallelic (DEE end of spectrum):** neonatal onset **1–6 days** with **refractory seizures**, including myoclonic and generalized tonic–clonic seizures and possible status epilepticus; associated with severe ID/DD and MRI abnormalities (zhang2021cnnm2relateddisordersphenotype pages 5-6, zhang2021cnnm2relateddisordersphenotype pages 4-4).
- **AD/heterozygous:** onset is typically **infancy** (often 4 months–1 year), with seizures frequently responsive to ASMs and sometimes remitting over time; developmental impairment tends to be milder than AR cases (zhang2021cnnm2relateddisordersphenotype pages 5-6, franken2021thephenotypicand pages 8-10).

**Quantitative frequency/statistics from cohorts**
- In a 14-patient heterozygous cohort, the majority experienced seizures and neurodevelopmental impairment, and severe obesity was very frequent (franken2021thephenotypicand pages 10-12).
- In a synthesis of **23 cases**, the most common phenotype class (type 2, AD hypomagnesemia + epilepsy + ID/DD) had **86.7% (13/15) seizures** and **93.3% (14/15) ID/DD**; AR cases (3/23) were the most severe (zhang2021cnnm2relateddisordersphenotype pages 5-6).

### 3.3 Quality of life / functional impact
Direct QoL instrument results (e.g., EQ-5D/SF-36) were not found in the retrieved evidence. However, severe AR/DEE cases include profound disability (nonverbal, severe developmental impairment) (zhang2021cnnm2relateddisordersphenotype pages 5-6), and AD cases can include persistent ID/speech impairment and obesity (franken2021thephenotypicand pages 10-12).

---

## 4. Genetic / Molecular Information
### 4.1 Causal gene
- **CNNM2** (cyclin M2; previously **ACDP2**) (zhang2021cnnm2relateddisordersphenotype pages 1-2, arjona2014cnnm2mutationscause pages 1-2).

### 4.2 Pathogenic variant classes and functional consequences
**Variant classes reported across cohorts/case series** include missense variants, nonsense/premature stop variants, small deletions/frameshift variants, and larger deletions (zhang2021cnnm2relateddisordersphenotype pages 4-4, franken2021thephenotypicand pages 8-10).

**Functional consequence:** predominantly **loss-of-function / impaired CNNM2-mediated Mg2+ handling**.
- Mutant CNNM2 proteins failed to augment Mg2+ uptake in cell-based assays and showed trafficking defects in some alleles, consistent with LoF (arjona2014cnnm2mutationscause pages 7-9).

**Example variants (illustrative; not exhaustive)**
- Severe AR/DEE-associated examples include homozygous **c.1642G>A (p.Val548Met)** (accogli2019cnnm2homozygousmutations pages 1-2, zhang2021cnnm2relateddisordersphenotype pages 4-4) and recessive **p.Glu122Lys** (arjona2014cnnm2mutationscause pages 7-9).
- AD/heterozygous examples in aggregated tables include variants such as **p.Leu48Pro**, **p.Tyr314***, **p.Leu321del**, **p.Val324Met**, **p.Leu418Pro**, **p.Ser795Leu**, **p.Arg797*** (zhang2021cnnm2relateddisordersphenotype pages 4-4, li2021casereportcnnm2 pages 5-6).
- In two de novo infant cases, variants were classified as **likely pathogenic** per ACMG and identified by trio-WES: **c.814T>C (p.Phe272Leu)** and **c.976G>C (p.Val326Leu)** (zhang2021cnnm2relateddisordersphenotype pages 2-4).

### 4.3 Modifier genes / protective alleles
No specific modifier genes or protective alleles were established in the retrieved evidence, though variable expressivity is emphasized.

### 4.4 Epigenetic information
No CNNM2-DEE–specific epigenetic signatures were found in the retrieved evidence.

### 4.5 Chromosomal abnormalities
Not a focus of the retrieved core CNNM2-HSMR/DEE literature in this run.

---

## 5. Environmental Information
CNNM2-related DEE/HSMR is primarily genetic. No consistent toxins, lifestyle factors, or infectious triggers were described in the retrieved CNNM2-focused sources.

---

## 6. Mechanism / Pathophysiology
### 6.1 Current understanding (molecular-to-clinical causal chain)
1. **CNNM2 dysfunction** (often LoF or impaired membrane expression/transport activity) (arjona2014cnnm2mutationscause pages 7-9, franken2021thephenotypicand pages 1-4).
2. **Renal magnesium handling impairment** → persistent **hypomagnesemia** that may be only partially correctable (zhang2021cnnm2relateddisordersphenotype pages 5-6, arjona2014cnnm2mutationscause pages 2-4).
3. **Neurodevelopmental dysfunction and epilepsy**: seizures and developmental impairment can persist even when magnesium improves, and severe biallelic disease includes structural brain abnormalities consistent with a DEE phenotype (arjona2014cnnm2mutationscause pages 7-9, zhang2021cnnm2relateddisordersphenotype pages 5-6).

### 6.2 Molecular pathways / processes and suggested ontology terms
**Key processes (GO Biological Process suggestions)**
- Magnesium ion homeostasis (GO:0006874)
- Divalent metal ion transport (broad; gene-specific evidence indicates Mg2+ handling) (arjona2014cnnm2mutationscause pages 7-9)
- Nervous system development (GO:0007399) (supported by zebrafish/mouse developmental phenotypes) (arjona2014cnnm2mutationscause pages 1-2, bosman2024hypomagnesaemiawithvarying pages 1-2)

**Key cell types (Cell Ontology suggestions; inferred from tissue localization statements in evidence)**
- Distal convoluted tubule epithelial cell (kidney; DCT localization emphasized) (bosman2024hypomagnesaemiawithvarying pages 1-2)
- Neuron / cortical neuron (brain expression emphasized, though specific neuronal subtype evidence for CNNM2-DEE is limited in retrieved sources) (bosman2024hypomagnesaemiawithvarying pages 1-2)

### 6.3 Protein dysfunction
CNNM2 variants can impair Mg2+ transport-related function and/or membrane localization, consistent with LoF mechanisms (arjona2014cnnm2mutationscause pages 7-9, franken2021thephenotypicand pages 1-4).

### 6.4 Recent developments (2024)
A 2024 genotype–phenotype/functional study emphasizes variability and potential modifiers: **“Variants in the CNNM2 gene are causative for hypomagnesaemia, seizures and intellectual disability, although the phenotypes can be variable”**, and in their dataset **“seizures and intellectual disability are absent in 4 out of 7 cases”** despite functionally affected variants (bosman2024hypomagnesaemiawithvarying pages 1-2). This strengthens the view that hypomagnesemia alone does not fully explain neurologic outcomes and supports variant-specific effects and/or additional modifiers (bosman2024hypomagnesaemiawithvarying pages 1-2).

---

## 7. Anatomical Structures Affected
### 7.1 Organ/system level
- **Nervous system (brain):** epilepsy/DEE, developmental impairment; severe AR cases include structural brain abnormalities (zhang2021cnnm2relateddisordersphenotype pages 5-6, zhang2021cnnm2relateddisordersphenotype pages 4-4).
- **Kidney (renal tubule/DCT):** CNNM2 is highlighted as important for distal tubular Mg handling and renal-origin hypomagnesemia (bosman2024hypomagnesaemiawithvarying pages 1-2, arjona2014cnnm2mutationscause pages 1-2).

### 7.2 Tissue/cell level (suggested UBERON/CL)
- Kidney distal convoluted tubule (UBERON:0001285; DCT) (bosman2024hypomagnesaemiawithvarying pages 1-2)
- Cerebral cortex (UBERON:0000956) / developing brain (inferred from malformations and developmental phenotypes) (zhang2021cnnm2relateddisordersphenotype pages 5-6, arjona2014cnnm2mutationscause pages 7-9)

### 7.3 Subcellular level (GO Cellular Component suggestions)
- Plasma membrane (GO:0005886) — impaired membrane expression/trafficking is reported in functional work (franken2021thephenotypicand pages 1-4).

---

## 8. Temporal Development
### 8.1 Onset
- **AR/DEE:** neonatal onset **1–6 days** (zhang2021cnnm2relateddisordersphenotype pages 5-6).
- **AD/heterozygous:** typically infancy (4–12 months common in aggregated data) (arjona2014cnnm2mutationscause pages 2-4, zhang2021cnnm2relateddisordersphenotype pages 5-6).

### 8.2 Progression/course
- **AR/DEE:** refractory epilepsy and severe developmental impairment; MRI abnormalities can include progressive cortical atrophy (zhang2021cnnm2relateddisordersphenotype pages 5-6).
- **AD/heterozygous:** seizures often respond to ASMs and may remit; neurodevelopmental issues and obesity may persist (franken2021thephenotypicand pages 8-10, franken2021thephenotypicand pages 10-12).

---

## 9. Inheritance and Population
### 9.1 Inheritance pattern
- Both **autosomal dominant** (including de novo) and **autosomal recessive** inheritance are documented, with **AR/biallelic** disease being more severe and more DEE-like (zhang2021cnnm2relateddisordersphenotype pages 1-2, zhang2021cnnm2relateddisordersphenotype pages 5-6, arjona2014cnnm2mutationscause pages 7-9).

### 9.2 Epidemiology
No population prevalence or incidence estimates were found in the retrieved sources. Available data are case-based aggregations (e.g., 23 cases synthesized in one report; multiple variant catalogs) (zhang2021cnnm2relateddisordersphenotype pages 5-6, bosman2024hypomagnesaemiawithvarying pages 1-2).

---

## 10. Diagnostics
### 10.1 Clinical and laboratory evaluation
- **Serum magnesium**: typically low (hypomagnesemia) with renal wasting; supplementation often partially effective but not normalizing (zhang2021cnnm2relateddisordersphenotype pages 5-6, arjona2014cnnm2mutationscause pages 2-4, bosman2024hypomagnesaemiawithvarying pages 1-2).
- **EEG**: can show focal onset in some heterozygous cases (zhang2021cnnm2relateddisordersphenotype pages 2-4).
- **Neuroimaging (MRI)**: severe AR cases show consistent abnormalities (dysmyelination, cortical atrophy, other malformations); heterozygous cases may have normal MRI (zhang2021cnnm2relateddisordersphenotype pages 5-6, zhang2021cnnm2relateddisordersphenotype pages 2-4).

### 10.2 Genetic testing
- Trio **whole-exome sequencing (WES)** was used to diagnose de novo cases and variants were classified using ACMG criteria (zhang2021cnnm2relateddisordersphenotype pages 2-4).

### 10.3 Differential diagnosis
Not systematically addressed in retrieved CNNM2-focused evidence; clinically, differential diagnosis overlaps with other genetic DEEs and renal tubulopathies causing electrolyte disturbances.

---

## 11. Outcome / Prognosis
- **AD/heterozygous:** seizures are frequently manageable and may remit; developmental outcomes vary from mild–moderate ID to more significant impairment; obesity is common in at least one large cohort (franken2021thephenotypicand pages 10-12, franken2021thephenotypicand pages 8-10).
- **AR/biallelic (DEE):** severe refractory epilepsy with profound developmental impairment and brain malformations (accogli2019cnnm2homozygousmutations pages 1-2, zhang2021cnnm2relateddisordersphenotype pages 5-6).

Mortality rates and life expectancy were not available in the retrieved evidence.

---

## 12. Treatment
### 12.1 Pharmacotherapy and supportive care
**Magnesium supplementation**
- Oral/IV magnesium is standard but frequently fails to normalize serum magnesium and may not rescue neurologic phenotypes in severe cases (arjona2014cnnm2mutationscause pages 7-9, zhang2021cnnm2relateddisordersphenotype pages 5-6).

**Antiseizure medications (ASMs)**
- In a 23-case synthesis, AD/type-2 patients often respond to ASMs; reported effective options include **phenobarbital, valproic acid, clobazam, levetiracetam, lacosamide** (zhang2021cnnm2relateddisordersphenotype pages 5-6).
- Severe AR/type-3 seizures are often refractory; multiple ASMs may decrease frequency (valproate, levetiracetam, lamotrigine, topiramate), but outcomes are poor (zhang2021cnnm2relateddisordersphenotype pages 5-6).

**Other / adjunct**
- A 2022 report describes CNNM2-related hypomagnesemia “amenable to treatment with spironolactone” in a family with a CNNM2 CBS-domain variant, suggesting a possible adjunct strategy for renal magnesium wasting in some cases (petrakis2022thep.pro482alavariant pages 1-2).

### 12.2 Experimental therapies / clinical trials
ClinicalTrials.gov searches performed in this run did not yield a clearly CNNM2-HSMR/DEE–specific interventional trial record suitable for citation; no NCT IDs are therefore provided.

### 12.3 Suggested MAXO terms (treatment actions)
- Magnesium supplementation therapy (MAXO:0000784; concept-level)
- Antiepileptic drug therapy (MAXO:0000749; concept-level)
- Genetic counseling (MAXO:0000071; concept-level)

---

## 13. Prevention
Primary prevention is not applicable for a highly penetrant Mendelian disorder except via **reproductive options**:
- **Genetic counseling** for families, including discussion of inheritance (AD vs AR), recurrence risk, and testing options (zhang2021cnnm2relateddisordersphenotype pages 1-2, li2025twonovelvariants pages 1-2).

---

## 14. Other Species / Natural Disease
No naturally occurring veterinary CNNM2-DEE syndromes were identified in the retrieved evidence.

---

## 15. Model Organisms
**Zebrafish**
- cnnm2 knockdown causes disturbed brain development and abnormal behavior; phenotypes are rescued by wild-type but not mutant cnnm2 constructs, supporting causality and providing a platform for mechanistic and therapeutic testing (arjona2014cnnm2mutationscause pages 1-2).

**Mouse**
- Cnnm2 heterozygous mice show hypomagnesemia consistent with a role in magnesium homeostasis; full knockout is reported as perinatally lethal with developmental defects/brain malformations in referenced summaries (bosman2024hypomagnesaemiawithvarying pages 1-2).

**In vitro**
- HEK293 and renal tubule cell assays support impaired Mg2+ uptake/transport and trafficking defects for pathogenic variants (arjona2014cnnm2mutationscause pages 7-9, franken2021thephenotypicand pages 1-4).

---

## Structured summary table
| Entity / synonym (OMIM/MIM) | Inheritance / allelic state | Core features (HPO terms) | Typical seizure onset & seizure features | Key neuroimaging findings | Key variants / examples | Mechanistic insights | Management / treatment notes | Key references |
|---|---|---|---|---|---|---|---|---|
| **CNNM2-related disorder**; **HSMR syndrome** = hypomagnesemia, seizures, and intellectual disability syndrome (**MIM 616418**); related milder entity **autosomal dominant renal hypomagnesemia 6 / HOMG6** (**MIM 613882**); newer synonym **HOMGSMR1**; causal gene **CNNM2 / cyclin M2** (**gene MIM 607803**) | Spectrum includes **AD/de novo heterozygous** disease and rarer **AR homozygous/biallelic** disease; severity correlates with inheritance, with **AR most severe** (franken2021thephenotypicand pages 1-4, petrakis2022thep.pro482alavariant pages 1-2, li2025twonovelvariants pages 1-2, zhang2021cnnm2relateddisordersphenotype pages 1-2, accogli2019cnnm2homozygousmutations pages 1-2) | Hypomagnesemia **HP:0002917**; Seizure **HP:0001250**; Intellectual disability / global developmental delay **HP:0001249 / HP:0001263**; Speech delay **HP:0000750**; Motor delay **HP:0001270**; Hypotonia **HP:0001252** or hypertonia in some reports; Microcephaly **HP:0000252**; Obesity **HP:0001513**; Autism / autistic features **HP:0000729** in some patients (franken2021thephenotypicand pages 10-12, franken2021thephenotypicand pages 8-10, zhang2021cnnm2relateddisordersphenotype pages 4-4, arjona2014cnnm2mutationscause pages 2-4) | Across the spectrum, seizures are common but variable. In heterozygous HSMR, onset is usually **infancy** (often **4 months–1 year**; median onset reported **1.54 years**, range birth–16 years in one cohort) and may be generalized or focal; many are ASM-responsive or remit over time. At the severe DEE end, **biallelic/AR** cases show **neonatal onset (1–6 days)**, refractory seizures, myoclonic and generalized tonic-clonic seizures, and sometimes **status epilepticus** (franken2021thephenotypicand pages 8-10, zhang2021cnnm2relateddisordersphenotype pages 5-6, zhang2021cnnm2relateddisordersphenotype pages 1-2, arjona2014cnnm2mutationscause pages 2-4) | Mild/moderate heterozygous cases often have **normal MRI** or mild nonspecific white-matter change. Severe AR/DEE cases show **brain malformations** including **dysmyelination / reduced myelination**, **failure of opercularization**, **microcephaly**, **progressive cortical atrophy**, widened extra-axial / CSF spaces, reduced white matter, and reported basal ganglia calcification (accogli2019cnnm2homozygousmutations pages 1-2, zhang2021cnnm2relateddisordersphenotype pages 5-6, zhang2021cnnm2relateddisordersphenotype pages 4-4, arjona2014cnnm2mutationscause pages 2-4, arjona2014cnnm2mutationscause pages 7-9) | Heterozygous examples: **p.Ser269Trp, p.Glu357Lys, p.Thr568Ile, p.Leu48Pro, p.Tyr314\*, p.Leu321del, p.Val324Met, p.Leu418Pro, p.Ser795Leu, p.Arg797\***; de novo likely pathogenic examples **c.814T>C (p.Phe272Leu)** and **c.976G>C (p.Val326Leu)**. Severe AR examples include **p.Glu122Lys** and homozygous **c.1642G>A (p.Val548Met)** (zhang2021cnnm2relateddisordersphenotype pages 5-6, accogli2019cnnm2homozygousmutations pages 1-2, zhang2021cnnm2relateddisordersphenotype pages 4-4, arjona2014cnnm2mutationscause pages 2-4, arjona2014cnnm2mutationscause pages 7-9, zhang2021cnnm2relateddisordersphenotype pages 2-4) | Predominantly **loss-of-function / haploinsufficiency** with impaired **CNNM2-mediated Mg²⁺ transport**; several variants reduce plasma-membrane trafficking/expression. CNNM2 is highly expressed in **distal convoluted tubule** and **brain**; hypomagnesemia is typically renal. Functional studies showed mutant CNNM2 fails to enhance Mg²⁺ uptake and zebrafish knockdown causes impaired brain development/abnormal motor behavior; mouse models support a developmental CNS role and perinatal lethality/brain malformations in full knockout. DUF21 variants are linked more strongly to CNS phenotypes; CBS2 variants may produce lower serum Mg²⁺ (zhang2021cnnm2relateddisordersphenotype pages 1-2, franken2021thephenotypicand pages 10-12, arjona2014cnnm2mutationscause pages 1-2, arjona2014cnnm2mutationscause pages 7-9, bosman2024hypomagnesaemiawithvarying pages 1-2) | **Magnesium supplementation** (oral and sometimes IV) usually raises serum Mg²⁺ only partially and often does **not normalize** it; neurologic benefit is limited. Heterozygous cases may respond to **phenobarbital, valproate, clobazam, levetiracetam, lacosamide**; some seizures remit over time. Severe AR/DEE cases are often **drug-refractory**, though **valproate, levetiracetam, lamotrigine, topiramate** may reduce frequency. A recent case report suggested **spironolactone** may alleviate hypomagnesemia in a milder CNNM2 disorder. No CNNM2-specific clinical trials were identified in the gathered evidence (franken2021thephenotypicand pages 10-12, zhang2021cnnm2relateddisordersphenotype pages 5-6, zhang2021cnnm2relateddisordersphenotype pages 1-2, arjona2014cnnm2mutationscause pages 2-4, petrakis2022thep.pro482alavariant pages 1-2) | Arjona et al., 2014, PLoS Genet. DOI: https://doi.org/10.1371/journal.pgen.1004267 (arjona2014cnnm2mutationscause pages 1-2, arjona2014cnnm2mutationscause pages 2-4, arjona2014cnnm2mutationscause pages 7-9); Accogli et al., 2019, Eur J Med Genet. DOI: https://doi.org/10.1016/j.ejmg.2018.07.014 (accogli2019cnnm2homozygousmutations pages 1-2); Franken et al., 2021, Hum Mutat. DOI: https://doi.org/10.1002/humu.24182 (franken2021thephenotypicand pages 10-12, franken2021thephenotypicand pages 8-10, franken2021thephenotypicand pages 1-4); Zhang et al., 2021, Front Pediatr. DOI: https://doi.org/10.3389/fped.2021.699568 (zhang2021cnnm2relateddisordersphenotype pages 1-2, zhang2021cnnm2relateddisordersphenotype pages 5-6, zhang2021cnnm2relateddisordersphenotype pages 2-4); Bosman et al., 2024, Sci Rep. DOI: https://doi.org/10.1038/s41598-024-57061-7 (bosman2024hypomagnesaemiawithvarying pages 1-2) |


*Table: This table summarizes CNNM2-related HSMR/HOMGSMR1 across the clinical spectrum, highlighting the severe developmental and epileptic encephalopathy end associated with biallelic disease. It compiles inheritance, phenotypes, imaging, representative variants, mechanisms, and management points supported by the gathered evidence.*

---

## Key statistics and quotable abstract statements (as captured in evidence snippets)
- Bosman et al. (2024-03, *Scientific Reports*): **“Variants in the CNNM2 gene are causative for hypomagnesaemia, seizures and intellectual disability, although the phenotypes can be variable.”** They also note serum Mg in prior reports **0.33–0.74 mmol/L (normal 0.7–1.05 mmol/L)** and that **“seizures and intellectual disability are absent in 4 out of 7 cases”** in their dataset (bosman2024hypomagnesaemiawithvarying pages 1-2). URL: https://doi.org/10.1038/s41598-024-57061-7
- Franken et al. (2021-03, *Human Mutation*): HSMR is defined as **“Hypomagnesemia, seizures, and intellectual disability (HSMR) syndrome”** with **MIM#616418**, and in their cohort severe obesity was very common (reported as **89%**) (franken2021thephenotypicand pages 1-4, franken2021thephenotypicand pages 10-12). URL: https://doi.org/10.1002/humu.24182
- Accogli et al. (2019-03, *European Journal of Medical Genetics*): explicitly frames homozygous CNNM2 mutations as causing **“severe refractory hypomagnesemia, epileptic encephalopathy and brain malformations”** (accogli2019cnnm2homozygousmutations pages 1-2). URL: https://doi.org/10.1016/j.ejmg.2018.07.014

---

## Evidence gaps / limitations of this run
- **MONDO / Orphanet / MeSH / ICD** identifiers were not available in the retrieved full texts.
- Robust **prevalence/incidence** estimates were not found.
- Population allele frequencies (e.g., gnomAD) and validated modifier genes were not captured in the retrieved sources.



References

1. (accogli2019cnnm2homozygousmutations pages 1-2): Andrea Accogli, Marcello Scala, Annalisa Calcagno, Flavia Napoli, Natascia Di Iorgi, Serena Arrigo, Maria Margherita Mancardi, Giulia Prato, Livia Pisciotta, Mato Nagel, Mariasavina Severino, and Valeria Capra. Cnnm2 homozygous mutations cause severe refractory hypomagnesemia, epileptic encephalopathy and brain malformations. European journal of medical genetics, 62 3:198-203, Mar 2019. URL: https://doi.org/10.1016/j.ejmg.2018.07.014, doi:10.1016/j.ejmg.2018.07.014. This article has 41 citations and is from a peer-reviewed journal.

2. (zhang2021cnnm2relateddisordersphenotype pages 5-6): Han Zhang, Ye Wu, and Yuwu Jiang. Cnnm2-related disorders: phenotype and its severity were associated with the mode of inheritance. Frontiers in Pediatrics, Sep 2021. URL: https://doi.org/10.3389/fped.2021.699568, doi:10.3389/fped.2021.699568. This article has 9 citations.

3. (arjona2014cnnm2mutationscause pages 7-9): Francisco J. Arjona, Jeroen H. F. de Baaij, Karl P. Schlingmann, Anke L. L. Lameris, Erwin van Wijk, Gert Flik, Sabrina Regele, G. Christoph Korenke, Birgit Neophytou, Stephan Rust, Nadine Reintjes, Martin Konrad, René J. M. Bindels, and Joost G. J. Hoenderop. Cnnm2 mutations cause impaired brain development and seizures in patients with hypomagnesemia. PLoS Genetics, 10:e1004267, Apr 2014. URL: https://doi.org/10.1371/journal.pgen.1004267, doi:10.1371/journal.pgen.1004267. This article has 164 citations and is from a domain leading peer-reviewed journal.

4. (zhang2021cnnm2relateddisordersphenotype pages 1-2): Han Zhang, Ye Wu, and Yuwu Jiang. Cnnm2-related disorders: phenotype and its severity were associated with the mode of inheritance. Frontiers in Pediatrics, Sep 2021. URL: https://doi.org/10.3389/fped.2021.699568, doi:10.3389/fped.2021.699568. This article has 9 citations.

5. (franken2021thephenotypicand pages 1-4): Gijs A. C. Franken, Dominik Müller, Cyril Mignot, Boris Keren, Jonathan Lévy, Anne‐Claude Tabet, David Germanaud, María‐Isabel Tejada, Hester Y. Kroes, Rutger A. J. Nievelstein, Elise Brimble, Maria Ruzhnikov, Felix Claverie‐Martin, Maria Szczepańska, Martin Ćuk, Femke Latta, Martin Konrad, Luis A. Martínez‐Cruz, René J. M. Bindels, Joost G. J. Hoenderop, Karl‐Peter Schlingmann, and Jeroen H. F. Baaij. The phenotypic and genetic spectrum of patients with heterozygous mutations in cyclin m2 (cnnm2). Human Mutation, 42:473-486, Mar 2021. URL: https://doi.org/10.1002/humu.24182, doi:10.1002/humu.24182. This article has 28 citations and is from a domain leading peer-reviewed journal.

6. (petrakis2022thep.pro482alavariant pages 1-2): Ioannis Petrakis, Eleni Drosataki, Ioanna Stavrakaki, Kleio Dermitzaki, Dimitra Lygerou, Myrto Konidaki, Christos Pleros, Nikolaos Kroustalakis, Sevasti Maragkou, Ariadni Androvitsanea, Ioannis Stylianou, Ioannis Zaganas, and Kostas Stylianou. The p.pro482ala variant in the cnnm2 gene causes severe hypomagnesemia amenable to treatment with spironolactone. International Journal of Molecular Sciences, 23:7284, Jun 2022. URL: https://doi.org/10.3390/ijms23137284, doi:10.3390/ijms23137284. This article has 7 citations.

7. (li2025twonovelvariants pages 1-2): Huijuan Li, Jing Liu, Yingdi Liu, Yaning Liu, Kehui Lu, Juan Wen, Huimin Zhu, Desheng Liang, Zhuo Li, and Lingqian Wu. Two novel variants in cnnm2 disrupts magnesium efflux leading to neurodevelopmental disorders. Frontiers in Genetics, Jun 2025. URL: https://doi.org/10.3389/fgene.2025.1600877, doi:10.3389/fgene.2025.1600877. This article has 0 citations and is from a peer-reviewed journal.

8. (arjona2014cnnm2mutationscause pages 1-2): Francisco J. Arjona, Jeroen H. F. de Baaij, Karl P. Schlingmann, Anke L. L. Lameris, Erwin van Wijk, Gert Flik, Sabrina Regele, G. Christoph Korenke, Birgit Neophytou, Stephan Rust, Nadine Reintjes, Martin Konrad, René J. M. Bindels, and Joost G. J. Hoenderop. Cnnm2 mutations cause impaired brain development and seizures in patients with hypomagnesemia. PLoS Genetics, 10:e1004267, Apr 2014. URL: https://doi.org/10.1371/journal.pgen.1004267, doi:10.1371/journal.pgen.1004267. This article has 164 citations and is from a domain leading peer-reviewed journal.

9. (tseng2022novelcnnm2mutation pages 1-2): Min-Hua Tseng, Sung-Sen Yang, Chih-Chien Sung, Jhao-Jhuang Ding, Yu-Juei Hsu, Shih-Ming Chu, and Shih-Hua Lin. Novel cnnm2 mutation responsible for autosomal-dominant hypomagnesemia with seizure. Frontiers in Genetics, Jun 2022. URL: https://doi.org/10.3389/fgene.2022.875013, doi:10.3389/fgene.2022.875013. This article has 11 citations and is from a peer-reviewed journal.

10. (franken2021thephenotypicand pages 10-12): Gijs A. C. Franken, Dominik Müller, Cyril Mignot, Boris Keren, Jonathan Lévy, Anne‐Claude Tabet, David Germanaud, María‐Isabel Tejada, Hester Y. Kroes, Rutger A. J. Nievelstein, Elise Brimble, Maria Ruzhnikov, Felix Claverie‐Martin, Maria Szczepańska, Martin Ćuk, Femke Latta, Martin Konrad, Luis A. Martínez‐Cruz, René J. M. Bindels, Joost G. J. Hoenderop, Karl‐Peter Schlingmann, and Jeroen H. F. Baaij. The phenotypic and genetic spectrum of patients with heterozygous mutations in cyclin m2 (cnnm2). Human Mutation, 42:473-486, Mar 2021. URL: https://doi.org/10.1002/humu.24182, doi:10.1002/humu.24182. This article has 28 citations and is from a domain leading peer-reviewed journal.

11. (bosman2024hypomagnesaemiawithvarying pages 1-2): Willem Bosman, Gijs A. C. Franken, Javier de las Heras, Leire Madariaga, Tahsin Stefan Barakat, Rianne Oostenbrink, Marjon van Slegtenhorst, Ana Perdomo-Ramírez, Félix Claverie-Martín, Albertien M. van Eerde, Rosa Vargas-Poussou, Laurence Derain Dubourg, Irene González-Recio, Luis Alfonso Martínez-Cruz, Jeroen H. F. de Baaij, and Joost G. J. Hoenderop. Hypomagnesaemia with varying degrees of extrarenal symptoms as a consequence of heterozygous cnnm2 variants. Scientific Reports, Mar 2024. URL: https://doi.org/10.1038/s41598-024-57061-7, doi:10.1038/s41598-024-57061-7. This article has 2 citations and is from a peer-reviewed journal.

12. (zhang2021cnnm2relateddisordersphenotype pages 4-4): Han Zhang, Ye Wu, and Yuwu Jiang. Cnnm2-related disorders: phenotype and its severity were associated with the mode of inheritance. Frontiers in Pediatrics, Sep 2021. URL: https://doi.org/10.3389/fped.2021.699568, doi:10.3389/fped.2021.699568. This article has 9 citations.

13. (arjona2014cnnm2mutationscause pages 2-4): Francisco J. Arjona, Jeroen H. F. de Baaij, Karl P. Schlingmann, Anke L. L. Lameris, Erwin van Wijk, Gert Flik, Sabrina Regele, G. Christoph Korenke, Birgit Neophytou, Stephan Rust, Nadine Reintjes, Martin Konrad, René J. M. Bindels, and Joost G. J. Hoenderop. Cnnm2 mutations cause impaired brain development and seizures in patients with hypomagnesemia. PLoS Genetics, 10:e1004267, Apr 2014. URL: https://doi.org/10.1371/journal.pgen.1004267, doi:10.1371/journal.pgen.1004267. This article has 164 citations and is from a domain leading peer-reviewed journal.

14. (franken2021thephenotypicand pages 8-10): Gijs A. C. Franken, Dominik Müller, Cyril Mignot, Boris Keren, Jonathan Lévy, Anne‐Claude Tabet, David Germanaud, María‐Isabel Tejada, Hester Y. Kroes, Rutger A. J. Nievelstein, Elise Brimble, Maria Ruzhnikov, Felix Claverie‐Martin, Maria Szczepańska, Martin Ćuk, Femke Latta, Martin Konrad, Luis A. Martínez‐Cruz, René J. M. Bindels, Joost G. J. Hoenderop, Karl‐Peter Schlingmann, and Jeroen H. F. Baaij. The phenotypic and genetic spectrum of patients with heterozygous mutations in cyclin m2 (cnnm2). Human Mutation, 42:473-486, Mar 2021. URL: https://doi.org/10.1002/humu.24182, doi:10.1002/humu.24182. This article has 28 citations and is from a domain leading peer-reviewed journal.

15. (li2021casereportcnnm2 pages 5-6): Xiucui Li, Shijia Bao, Wei Wang, Xulai Shi, Ying Hu, Feng Li, Qianlei Zhao, Feixia Zheng, and Zhongdong Lin. Case report: cnnm2 mutations cause damaged brain development and intractable epilepsy in a patient without hypomagnesemia. Frontiers in Genetics, Aug 2021. URL: https://doi.org/10.3389/fgene.2021.705734, doi:10.3389/fgene.2021.705734. This article has 11 citations and is from a peer-reviewed journal.

16. (zhang2021cnnm2relateddisordersphenotype pages 2-4): Han Zhang, Ye Wu, and Yuwu Jiang. Cnnm2-related disorders: phenotype and its severity were associated with the mode of inheritance. Frontiers in Pediatrics, Sep 2021. URL: https://doi.org/10.3389/fped.2021.699568, doi:10.3389/fped.2021.699568. This article has 9 citations.
