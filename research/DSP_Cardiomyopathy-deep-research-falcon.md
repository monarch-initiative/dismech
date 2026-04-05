---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T12:24:54.240597'
end_time: '2026-04-04T12:31:57.372490'
duration_seconds: 423.13
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: DSP Cardiomyopathy
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 42
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** DSP Cardiomyopathy
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **DSP Cardiomyopathy** covering all of the
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
- **Disease Name:** DSP Cardiomyopathy
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **DSP Cardiomyopathy** covering all of the
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


## DSP Cardiomyopathy (DSP-associated Arrhythmogenic Cardiomyopathy) — Disease Characteristics Research Report

### Executive summary
DSP cardiomyopathy is an inherited, desmosome-related arrhythmogenic cardiomyopathy typically characterized by **left-ventricular (LV)–predominant myocardial scarring (often subepicardial LGE on CMR), episodic “myocarditis-like” myocardial injury (“hot phases”), and a high burden of ventricular arrhythmias and heart-failure outcomes**. The disorder is increasingly conceptualized within the spectrum of **“scarring/arrhythmogenic cardiomyopathy”**, where non-ischemic scar is the central arrhythmogenic substrate, and modern diagnostic criteria explicitly incorporate LV phenotypes and CMR tissue characterization (Padua 2020; European Task Force 2023) (smith2020desmoplakincardiomyopathya pages 1-3, wang2022clinicalcharacteristicsand pages 1-2, brandao2023desmoplakincardiomyopathycomprehensive pages 2-4, graziano2024the2023european pages 1-2, corrado2023scarringarrhythmogeniccardiomyopathy pages 1-2).

| Domain | Key points (1-3 bullets) | Key quantitative stats (if any) | Key sources (first author year journal) with PMID if known | URL |
|---|---|---|---|---|
| Definition/Concept | - Distinct inherited arrhythmogenic cardiomyopathy centered on **DSP** (desmoplakin) with frequent **left-ventricular-predominant** disease, extensive fibrosis, high arrhythmic risk, and recurrent myocarditis-like/“hot phase” myocardial injury episodes.<br>- Increasingly framed within **scarring/arrhythmogenic cardiomyopathy (S/ACM)**, where non-ischemic scar is the core substrate for ventricular arrhythmias.<br>- Disease definition and recognition improved after LV-inclusive criteria and broader use of CMR/genetics. (brandao2023desmoplakincardiomyopathycomprehensive pages 2-4, graziano2024the2023european pages 1-2, brandao2023desmoplakincardiomyopathycomprehensive pages 1-2) | - P/LP DSP variants found in a large proportion of ALVC patients: **~57%** in review-cited data. (brandao2023desmoplakincardiomyopathycomprehensive pages 1-2) | **Brandão 2023 J Clin Med**; **Graziano 2024 Rev Cardiovasc Med**; **Corrado 2023 Eur Heart J Suppl**; **Smith 2020 Circulation** | https://doi.org/10.3390/jcm12072660 ; https://doi.org/10.31083/j.rcm2509348 ; https://doi.org/10.1093/eurheartjsupp/suad017 ; https://doi.org/10.1161/CIRCULATIONAHA.119.044934 |
| Key phenotypes | - LV-predominant, biventricular, and less often RV-predominant phenotypes occur; DSP disease is characteristically **left-sided** compared with classic PKP2-ARVC.<br>- Recurrent **myocardial injury / myocarditis-like episodes**: chest pain, troponin rise, normal coronaries.<br>- Frequent ventricular ectopy/arrhythmias; some patients also have **curly/woolly hair** and **palmoplantar keratoderma**. (smith2020desmoplakincardiomyopathya pages 4-6, wang2022clinicalcharacteristicsand pages 1-2, brandao2023desmoplakincardiomyopathycomprehensive pages 2-4) | - LV-predominant disease: **55%** in 2020 multicenter DSP cohort; RV-predominant **14%**. (smith2020desmoplakincardiomyopathya pages 1-3)<br>- In 2022 cohort: left-predominant **28%**, biventricular **15%**, right-predominant **6%**. (wang2022clinicalcharacteristicsand pages 1-2)<br>- Myocardial injury episodes: **15%** (2020 cohort) and **22%** (2022 cohort). (smith2020desmoplakincardiomyopathya pages 1-3, wang2022clinicalcharacteristicsand pages 1-2) | **Smith 2020 Circulation**; **Wang 2022 Europace**; **Brandão 2023 J Clin Med** | https://doi.org/10.1161/CIRCULATIONAHA.119.044934 ; https://doi.org/10.1093/europace/euab183 ; https://doi.org/10.3390/jcm12072660 |
| Imaging/CMR | - **CMR is the imaging modality of choice** for ACM spectrum disease because it combines biventricular morpho-functional assessment with tissue characterization.<br>- DSP cardiomyopathy typically shows **subepicardial LV LGE**, often inferolateral/posterolateral and sometimes ring-like; scar may precede overt systolic dysfunction.<br>- LV LGE can be disproportionate to LV dysfunction and helps distinguish DSP disease from generic DCM, though myocarditis/sarcoid remain key differentials. (cipriani2023cardiacmagneticresonance pages 1-2, smith2020desmoplakincardiomyopathya pages 4-6, brandao2023desmoplakincardiomyopathycomprehensive pages 2-4) | - LV LGE in DSP cohort: **40%** overall among those with MRI; **74%** of LV-predominant cases had LV LGE. (smith2020desmoplakincardiomyopathya pages 4-6)<br>- LGE without LV systolic dysfunction: **26%** in one summary; **35%** of LGE cases in 2020 cohort. (smith2020desmoplakincardiomyopathya pages 4-6, smith2020desmoplakincardiomyopathya pages 1-3)<br>- Among myocardial injury cases, LV LGE association **~90%**. (smith2020desmoplakincardiomyopathya pages 1-3) | **Cipriani 2023 Eur Radiol**; **Galizia 2024 RadioGraphics**; **Augusto 2020 Eur Heart J Cardiovasc Imaging**; **Smith 2020 Circulation** | https://doi.org/10.1007/s00330-022-08958-2 ; https://doi.org/10.1148/rg.230154 ; https://doi.org/10.1093/ehjci/jez188 ; https://doi.org/10.1161/CIRCULATIONAHA.119.044934 |
| Genetics/inheritance | - Caused by **germline pathogenic/likely pathogenic DSP variants**; disease is usually **autosomal dominant** with **variable penetrance/expressivity**.<br>- Variants are predominantly **truncating/non-missense**, while missense variants may cluster in functional binding domains.<br>- DSP is a desmosomal gene; testing is especially informative in LV-dominant ACM/DCM overlap and recurrent myocarditis-like presentations. (smith2020desmoplakincardiomyopathya pages 8-10, chua2023understandingarrhythmogeniccardiomyopathy pages 1-3, wang2022clinicalcharacteristicsand pages 2-3) | - DSP variants reported in **3–15%** of ARVC patients. (wang2022clinicalcharacteristicsand pages 2-3)<br>- In the 2020 cohort, DSP mutations were predominantly truncating: **105/107** patients. (smith2020desmoplakincardiomyopathya pages 4-6) | **Smith 2020 Circulation**; **Wang 2022 Europace**; **Chua 2023 Genes** | https://doi.org/10.1161/CIRCULATIONAHA.119.044934 ; https://doi.org/10.1093/europace/euab183 ; https://doi.org/10.3390/genes14101864 |
| Mechanism/pathophysiology | - Upstream lesion: **desmosomal dysfunction** at intercalated discs impairs cardiomyocyte adhesion under mechanical stress.<br>- Proposed causal chain: defective desmosomal linkage → myocyte detachment/injury/death → inflammation and recurrent “hot phases” → fibrous/fibrofatty scar formation → ventricular dysfunction and scar-related arrhythmias.<br>- Exercise may accelerate phenotypic expression in susceptible carriers; inflammation can mimic myocarditis or sarcoidosis. (corrado2023scarringarrhythmogeniccardiomyopathy pages 1-2, smith2020desmoplakincardiomyopathya pages 8-10, chua2023understandingarrhythmogeniccardiomyopathy pages 1-3) | - Desmosomal genes account for **~30–50%** of ACM overall. (chua2023understandingarrhythmogeniccardiomyopathy pages 1-3, chua2023understandingarrhythmogeniccardiomyopathy pages 3-4) | **Corrado 2023 Eur Heart J Suppl**; **Chua 2023 Genes**; **Smith 2020 Circulation** | https://doi.org/10.1093/eurheartjsupp/suad017 ; https://doi.org/10.3390/genes14101864 ; https://doi.org/10.1161/CIRCULATIONAHA.119.044934 |
| Diagnostics | - Diagnosis should be **multiparametric**: ECG/Holter, echocardiography, **CMR with LGE**, arrhythmia assessment, family history, and **genetic testing**.<br>- The older 2010 ARVC Task Force Criteria under-detect DSP disease, especially **LV-dominant** forms; CMR and genetics materially improve detection.<br>- Cascade evaluation of relatives is recommended in inherited cardiomyopathy practice. (wang2022clinicalcharacteristicsand pages 8-9, cipriani2023cardiacmagneticresonance pages 1-2, mauriello2024arrhythmogenicleftventricular pages 1-2) | - Sensitivity of 2010 TFC for left-dominant DSP disease: **0.73**; **23%** of patients with sustained arrhythmias in one cohort did not meet criteria. (wang2022clinicalcharacteristicsand pages 1-2)<br>- Only **34%** met definite ARVC criteria in 2020 DSP cohort. (smith2020desmoplakincardiomyopathya pages 4-6) | **Wang 2022 Europace**; **Cipriani 2023 Eur Radiol**; **Mauriello 2024 J Clin Med**; **Korthals 2023 Herzschr Elektrophysiol** | https://doi.org/10.1093/europace/euab183 ; https://doi.org/10.1007/s00330-022-08958-2 ; https://doi.org/10.3390/jcm13071835 ; https://doi.org/10.1007/s00399-023-00975-y |
| Outcomes/statistics | - DSP cardiomyopathy carries substantial risk of **sustained ventricular arrhythmia**, **heart failure**, transplant, and SCD.<br>- Myocardial injury/hot-phase presentations are associated with worse subsequent outcomes in cohort data.<br>- Arrhythmic risk may occur even when LVEF is only mildly reduced, so standard low-EF thresholds can miss risk. (wang2022clinicalcharacteristicsand pages 1-2, smith2020desmoplakincardiomyopathya pages 8-10) | - Severe ventricular arrhythmia composite in 2020 DSP cohort: **28% (30/107)**. (smith2020desmoplakincardiomyopathya pages 8-10)<br>- Incidence rates in 2022 cohort: sustained ventricular arrhythmia **5.9/100 person-years**; heart failure **6.7/100 person-years**. (wang2022clinicalcharacteristicsand pages 1-2)<br>- Myocardial injury associated with sustained ventricular arrhythmia **HR 2.53** and heart failure **HR 7.53** (univariate). (wang2022clinicalcharacteristicsand pages 1-2) | **Smith 2020 Circulation**; **Wang 2022 Europace** | https://doi.org/10.1161/CIRCULATIONAHA.119.044934 ; https://doi.org/10.1093/europace/euab183 |
| Management/applications | - Real-world management includes **guideline-directed HF therapy**, arrhythmia surveillance, and **ICD** placement for selected high-risk patients; ICD is the only proven life-saving therapy in ACM broadly.<br>- Management is increasingly **genotype- and phenotype-informed**, considering fibrosis burden, ventricular function, arrhythmic history, and progression.<br>- In recurrent inflammatory/hot-phase presentations, case literature reports individualized use of **immunosuppression**, but evidence remains limited. (corrado2023scarringarrhythmogeniccardiomyopathy pages 1-2, fatrous2025desmoplakincardiomyopathymyocarditislike pages 5-6, brandao2023desmoplakincardiomyopathycomprehensive pages 9-11) | - High device utilization reported in a genotype-first DSP series: **68%** underwent primary/secondary prevention ICD implantation; **16%** underwent VT ablation; **11%** reached transplant. (reza2022cardiovascularcharacteristicsof pages 2-4) | **Corrado 2023 Eur Heart J Suppl**; **Korthals 2023 Herzschr Elektrophysiol**; **Reza 2022 Cardiogenetics**; **Fatrous 2025 Cureus** | https://doi.org/10.1093/eurheartjsupp/suad017 ; https://doi.org/10.1007/s00399-023-00975-y ; https://doi.org/10.3390/cardiogenetics12010003 ; https://doi.org/10.7759/cureus.87311 |
| Recent criteria/guidelines | - **2020 Padua criteria** and subsequent **2023 European Task Force criteria** explicitly incorporate LV phenotypes and CMR tissue characterization, addressing historic under-recognition of left-dominant disease.<br>- **2023 ESC cardiomyopathy guidance** emphasizes multimodal imaging, genetic testing, individualized etiology-focused management, and patient pathways from presentation to diagnosis.<br>- These changes are especially relevant for DSP cardiomyopathy because of its LV scar-predominant phenotype. (graziano2024the2023european pages 1-2, cipriani2023cardiacmagneticresonance pages 1-2, mauriello2024arrhythmogenicleftventricular pages 1-2) | - In review-cited DSP cohorts, definite diagnosis improved from **~42–51%** by older ITF criteria to **~67%** using Padua criteria. (brandao2023desmoplakincardiomyopathycomprehensive pages 2-4) | **Graziano 2024 Rev Cardiovasc Med**; **Cipriani 2023 Eur Radiol**; **Korthals 2023 Herzschr Elektrophysiol**; **Brandão 2023 J Clin Med** | https://doi.org/10.31083/j.rcm2509348 ; https://doi.org/10.1007/s00330-022-08958-2 ; https://doi.org/10.1007/s00399-023-00975-y ; https://doi.org/10.3390/jcm12072660 |
| Models | - **hiPSC-derived cardiomyocytes** are a leading 2023 model platform for desmosomal ACM, enabling mechanistic studies and drug screening in human cells.<br>- Animal models support desmosomal disease biology, showing myocardial injury, inflammation, fibrosis/fibrofatty remodeling, and structural degeneration under desmosomal perturbation.<br>- DSP-specific human mechanistic modeling remains less mature than PKP2-focused work, but the framework is directly relevant. (chua2023understandingarrhythmogeniccardiomyopathy pages 1-3, chua2023understandingarrhythmogeniccardiomyopathy pages 3-4, corrado2023scarringarrhythmogeniccardiomyopathy pages 1-2) | - No DSP-specific quantitative model benchmark reported in the extracted passages. | **Chua 2023 Genes**; **Corrado 2023 Eur Heart J Suppl** | https://doi.org/10.3390/genes14101864 ; https://doi.org/10.1093/eurheartjsupp/suad017 |


*Table: This table condenses the main disease-characteristic domains for DSP cardiomyopathy for knowledge-base use. It prioritizes 2023-2024 conceptual and criteria updates while retaining landmark 2020-2022 cohort statistics for phenotype and outcome estimates.*

---

## 1. Disease information

### 1.1 What is the disease?
DSP cardiomyopathy (also called desmoplakin cardiomyopathy) is a **genetic arrhythmogenic cardiomyopathy** caused by pathogenic/likely pathogenic (P/LP) variants in **DSP (desmoplakin)**, with a phenotype that is often **LV-dominant** and marked by **fibrosis/scar that can precede overt systolic dysfunction**, recurrent **myocardial injury episodes**, and substantial ventricular arrhythmia risk (smith2020desmoplakincardiomyopathya pages 1-3, wang2022clinicalcharacteristicsand pages 1-2, brandao2023desmoplakincardiomyopathycomprehensive pages 2-4).

A landmark cohort study explicitly described it as **“a fibrotic and inflammatory form of cardiomyopathy distinct from typical dilated or arrhythmogenic right ventricular cardiomyopathy”** (Circulation, Jun 2020) (smith2020desmoplakincardiomyopathya pages 4-6).

### 1.2 Key identifiers (OMIM, Orphanet, ICD, MeSH, MONDO)
*Within the retrieved full-text evidence set for this run, explicit OMIM/Orphanet/ICD-10/ICD-11/MeSH/MONDO identifiers for “DSP cardiomyopathy” were not present.* Therefore, these identifiers cannot be reliably populated from the tool-retrieved sources alone.

### 1.3 Synonyms / alternative names
Commonly used labels in the literature include:
- **Desmoplakin cardiomyopathy** (brandao2023desmoplakincardiomyopathycomprehensive pages 2-4)
- **DSP cardiomyopathy** / **DSP-related cardiomyopathy** (wang2022clinicalcharacteristicsand pages 1-2, wang2022clinicalcharacteristicsand pages 2-3)
- **DSP-associated arrhythmogenic cardiomyopathy** / **left-dominant arrhythmogenic cardiomyopathy (ALVC) due to DSP** (brandao2023desmoplakincardiomyopathycomprehensive pages 1-2)
- Conceptually grouped under **scarring/arrhythmogenic cardiomyopathy (S/ACM)** (corrado2023scarringarrhythmogeniccardiomyopathy pages 1-2)

### 1.4 Evidence source type
Most disease-characteristic claims in this report are derived from **aggregated disease-level resources** (systematic reviews and diagnostic-criteria reviews) plus **observational human cohorts** of DSP P/LP variant carriers with longitudinal outcomes and imaging correlations (smith2020desmoplakincardiomyopathya pages 1-3, wang2022clinicalcharacteristicsand pages 1-2, brandao2023desmoplakincardiomyopathycomprehensive pages 2-4, corrado2023scarringarrhythmogeniccardiomyopathy pages 1-2).

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** Germline **P/LP DSP variants** affecting desmoplakin, a desmosomal protein that anchors intermediate filaments at the cardiomyocyte intercalated disc (wang2022clinicalcharacteristicsand pages 2-3).

A DSP cohort study highlighted that variants were predominantly truncating in that cohort, and that disease is frequently LV-predominant with fibrotic/inflammatory features (smith2020desmoplakincardiomyopathya pages 4-6, smith2020desmoplakincardiomyopathya pages 1-3).

### 2.2 Risk factors
#### Genetic risk factors
- **DSP P/LP variants** are causal; P/LP DSP variants are reported among arrhythmogenic cardiomyopathy patients and are particularly enriched in LV-dominant phenotypes (wang2022clinicalcharacteristicsand pages 2-3, brandao2023desmoplakincardiomyopathycomprehensive pages 1-2).
- In one cohort/review context, DSP P/LP variants were reported as present in a large proportion of ALVC patients (review-cited estimate **57%**) (brandao2023desmoplakincardiomyopathycomprehensive pages 1-2).

#### Environmental / lifestyle risk factors
- **Physical exercise/mechanical stress** is described as a trigger that can worsen desmosomal adhesion disruption and accelerate phenotypic expression in arrhythmogenic cardiomyopathy (conceptualized as episodic “hot phases”) (corrado2023scarringarrhythmogeniccardiomyopathy pages 1-2).

### 2.3 Protective factors
No protective genetic or environmental factors were explicitly identified in the retrieved evidence set.

### 2.4 Gene–environment interactions
A proposed interaction is **genetically defective desmosomal adhesion + mechanical stress (e.g., exercise)** → cardiomyocyte detachment/injury → scar formation and arrhythmic substrate (corrado2023scarringarrhythmogeniccardiomyopathy pages 1-2). However, specific quantitative GxE estimates were not present in the retrieved sources.

---

## 3. Phenotypes

### 3.1 Core cardiac phenotypes (with suggested HPO terms)
Below, frequencies/statistics are from human cohorts when available.

1) **Myocardial injury / myocarditis-like (“hot phase”) episodes**
- Phenotype type: symptom complex (chest pain) + lab abnormality (troponin elevation) with non-obstructive coronaries; can mimic acute myocarditis or ACS (smith2020desmoplakincardiomyopathya pages 1-3, wang2022clinicalcharacteristicsand pages 1-2).
- Frequency: **15%** in a 107-patient DSP cohort (Circulation 2020) (smith2020desmoplakincardiomyopathya pages 1-3); **22%** in a 91-person cohort (Europace 2022) (wang2022clinicalcharacteristicsand pages 1-2).
- Characteristics: may occur even with normal systolic function; strongly associated with LV scar/LGE (smith2020desmoplakincardiomyopathya pages 1-3).
- Suggested HPO terms: Chest pain (HP:0100749); Elevated cardiac troponin I (HP:0033427) / Elevated cardiac troponin T (HP:0033428).

2) **Ventricular arrhythmias / high ectopic burden**
- Phenotype type: electrophysiologic abnormality.
- Data: In a 2020 DSP cohort, frequent PVCs were common (Holter subset) and severe ventricular arrhythmia composite occurred in **28%** (smith2020desmoplakincardiomyopathya pages 4-6, smith2020desmoplakincardiomyopathya pages 8-10).
- Suggested HPO terms: Ventricular tachycardia (HP:0004756); Premature ventricular contractions (HP:0006689); Sudden cardiac death (HP:0001645).

3) **LV-dominant or biventricular cardiomyopathy with fibrosis/scar**
- Phenotype type: structural cardiac abnormality.
- Frequencies: In a 2020 cohort, LV-predominant cardiomyopathy **55%** and RV-predominant **14%** (smith2020desmoplakincardiomyopathya pages 1-3). In a 2022 cohort, left-predominant **28%**, biventricular **15%**, right-predominant **6%** (wang2022clinicalcharacteristicsand pages 1-2).
- Suggested HPO terms: Cardiomyopathy (HP:0001638); Left ventricular dysfunction (HP:0025169) (or reduced ejection fraction term if needed).

4) **Cutaneous features in a subset (cardiocutaneous overlap)**
- Curly/woolly hair and palmoplantar keratoderma are reported in DSP cohorts/reviews (smith2020desmoplakincardiomyopathya pages 4-6, brandao2023desmoplakincardiomyopathycomprehensive pages 1-2).
- Suggested HPO terms: Palmoplantar keratoderma (HP:0000972); Woolly hair (HP:0002217).

### 3.2 Imaging-linked phenotype expressions
- LV LGE may occur **before** systolic dysfunction and can be present with preserved LV function (smith2020desmoplakincardiomyopathya pages 1-3).

### 3.3 Quality of life impact
QoL instruments (e.g., SF-36, EQ-5D, PROMIS) and quantitative QoL outcomes were not reported in the retrieved evidence set.

---

## 4. Genetic / molecular information

### 4.1 Causal gene(s)
- **DSP (desmoplakin)** is the causal gene; it encodes a desmosomal protein critical for cardiomyocyte cohesion (brandao2023desmoplakincardiomyopathycomprehensive pages 2-4, chua2023understandingarrhythmogeniccardiomyopathy pages 1-3).

### 4.2 Pathogenic variant classes (as represented in cohorts)
- In a 107-patient DSP cohort, variants were predominantly truncating (105/107 in that cohort summary) (smith2020desmoplakincardiomyopathya pages 4-6).
- Missense variants may cluster in specific binding domains (plakophilin/plakoglobin and desmin-binding domains) in cohort analyses (smith2020desmoplakincardiomyopathya pages 8-10).

### 4.3 Inheritance, penetrance, expressivity
- Desmosome-related arrhythmogenic cardiomyopathy is commonly **autosomal dominant** with **low/variable penetrance**, modified by additional factors such as age/exercise/stress (chua2023understandingarrhythmogeniccardiomyopathy pages 1-3).
- Within DSP-specific cohorts, variable ventricular involvement patterns (LV-dominant, biventricular, RV-dominant) support variable expressivity (wang2022clinicalcharacteristicsand pages 1-2).

### 4.4 Modifier genes / epigenetics
No DSP-specific modifier loci or epigenetic mechanisms were directly evidenced in the retrieved texts. However, a clinical trial explicitly investigates feasibility of **epigenetic analysis** of desmosomal genes including DSP from cardiomyocyte-derived DNA (NCT03177018) (NCT03177018 chunk 1).

---

## 5. Environmental information

### 5.1 Environmental and lifestyle factors
- Exercise/mechanical stress is discussed as an exacerbating trigger in arrhythmogenic cardiomyopathy pathobiology, particularly during episodic “hot phases” (corrado2023scarringarrhythmogeniccardiomyopathy pages 1-2).

### 5.2 Infectious agents
DSP cardiomyopathy can **mimic** infectious myocarditis clinically, but no specific pathogen etiologies were assigned in the retrieved evidence.

---

## 6. Mechanism / pathophysiology

### 6.1 Current mechanistic understanding (causal chain)
A synthesis supported by authoritative reviews and cohort observations:
1) **DSP variant → desmosomal dysfunction**: defective desmosomal proteins impair cardiomyocyte cell–cell adhesion at intercalated discs (corrado2023scarringarrhythmogeniccardiomyopathy pages 1-2, chua2023understandingarrhythmogeniccardiomyopathy pages 1-3).
2) **Mechanical stress/exercise → cardiomyocyte detachment and injury/death**: impaired cohesion under stress promotes myocyte detachment/necrosis (corrado2023scarringarrhythmogeniccardiomyopathy pages 1-2).
3) **Inflammation and “hot phases”**: episodic inflammatory flares can manifest with chest pain and troponin release and can be misdiagnosed as myocarditis/sarcoidosis; FDG-PET and limited histology in DSP cohorts support myocardial inflammation during injury episodes (smith2020desmoplakincardiomyopathya pages 1-3, smith2020desmoplakincardiomyopathya pages 8-10).
4) **Fibrous/fibrofatty replacement (scar)**: myocyte loss is followed by fibrous or fibro-fatty replacement, forming the arrhythmogenic substrate (corrado2023scarringarrhythmogeniccardiomyopathy pages 1-2).
5) **Clinical consequences**: scar predisposes to ventricular arrhythmias/sudden death and contributes to systolic dysfunction/heart failure (corrado2023scarringarrhythmogeniccardiomyopathy pages 1-2, wang2022clinicalcharacteristicsand pages 1-2).

### 6.2 Pathways and processes (suggested GO terms)
Evidence-backed processes include:
- Cell–cell adhesion and intercalated-disc integrity disruption (mechanistic framing in S/ACM and desmosomal ACM reviews) (corrado2023scarringarrhythmogeniccardiomyopathy pages 1-2, chua2023understandingarrhythmogeniccardiomyopathy pages 1-3).
- Inflammatory response during hot phases (smith2020desmoplakincardiomyopathya pages 1-3, corrado2023scarringarrhythmogeniccardiomyopathy pages 1-2).
- Fibrosis/scar formation (corrado2023scarringarrhythmogeniccardiomyopathy pages 1-2).

Suggested GO Biological Process terms (examples):
- Cell–cell adhesion (GO:0098609)
- Inflammatory response (GO:0006954)
- Extracellular matrix organization (GO:0030198)
- Cardiac muscle cell death (e.g., apoptosis/necrosis-related terms, depending on curation level)

### 6.3 Cell types involved (suggested CL terms)
- Cardiomyocytes are the primary affected cells in desmosomal dysfunction (corrado2023scarringarrhythmogeniccardiomyopathy pages 1-2, chua2023understandingarrhythmogeniccardiomyopathy pages 1-3).
- Suggested CL terms: cardiomyocyte (CL:0000746); cardiac fibroblast (CL:0002548) (fibrosis context).

### 6.4 Molecular profiling (transcriptomics/proteomics/metabolomics)
No DSP-specific omics signatures were present in the retrieved texts.

---

## 7. Anatomical structures affected

### 7.1 Organ/system level
- Primary organ: **heart** (cardiovascular system), with prominent **left ventricle** involvement in many DSP carriers (smith2020desmoplakincardiomyopathya pages 1-3, wang2022clinicalcharacteristicsand pages 1-2).

Suggested UBERON terms:
- Heart (UBERON:0000948)
- Left ventricle (UBERON:0002084)
- Right ventricle (UBERON:0002080)

### 7.2 Subcellular localization
Desmosomal dysfunction at the intercalated disc is central (desmosome/intercalated disc context in desmosomal ACM reviews) (chua2023understandingarrhythmogeniccardiomyopathy pages 1-3).

Suggested GO Cellular Component terms:
- Desmosome (GO:0030057)
- Intercalated disc (GO:0014704)

---

## 8. Temporal development

### 8.1 Onset and course
- Many cohorts emphasize **young to mid-adult** presentations; myocarditis-like episodes can occur early and may precede ventricular dysfunction (wang2022clinicalcharacteristicsand pages 1-2).
- Disease may progress episodically with “hot phases” that can be clinically silent or symptomatic (corrado2023scarringarrhythmogeniccardiomyopathy pages 1-2).

### 8.2 Disease staging
A four-phase conceptual model of desmosomal arrhythmogenic cardiomyopathy progression (concealed → overt electrical → structural fibrofatty → end-stage HF) is described in desmosomal ACM modeling reviews (chua2023understandingarrhythmogeniccardiomyopathy pages 3-4).

---

## 9. Inheritance and population

### 9.1 Epidemiology
Population prevalence/incidence for DSP cardiomyopathy was not provided in the retrieved evidence.

### 9.2 Variant frequency in ACM
DSP P/LP variants are reported in **3–15% of ARVC patients** (note: ARVC-focused estimate, not population prevalence) (wang2022clinicalcharacteristicsand pages 2-3).

### 9.3 Sex/age distributions
- A 2020 DSP cohort had a female predominance (reported as 69% female in cohort summary) (smith2020desmoplakincardiomyopathya pages 4-6).
- Broader desmosome-related ACM literature often cites male predominance and variable penetrance overall, highlighting heterogeneity across genes and cohorts (chua2023understandingarrhythmogeniccardiomyopathy pages 1-3).

---

## 10. Diagnostics

### 10.1 Clinical evaluation and testing
A diagnostic approach supported by cohort evidence and criteria reviews includes:
- **ECG and ambulatory monitoring** (PVCs/VT burden) (smith2020desmoplakincardiomyopathya pages 4-6).
- **Echocardiography** for ventricular size/function; used as first-line in LV arrhythmogenic cardiomyopathy reviews (mauriello2024arrhythmogenicleftventricular pages 1-2).
- **Cardiac magnetic resonance (CMR)** for tissue characterization, scar detection (LGE), and biventricular assessment; repeatedly emphasized as imaging of choice in ACM (cipriani2023cardiacmagneticresonance pages 1-2).
- **Genetic testing** for desmosomal genes including DSP, particularly in LV-dominant scarring phenotypes or recurrent myocarditis-like presentations (smith2020desmoplakincardiomyopathya pages 1-3, wang2022clinicalcharacteristicsand pages 1-2).

### 10.2 Diagnostic criteria evolution (recent developments)
- Earlier 2010 Task Force criteria focused on RV disease and under-detected LV-dominant phenotypes (graziano2024the2023european pages 1-2).
- The **2020 Padua criteria** introduced explicit LV criteria and emphasized CMR tissue characterization (graziano2024the2023european pages 1-2, cipriani2023cardiacmagneticresonance pages 1-2).
- The **2023 European Task Force criteria** refined this evolution and are discussed as part of a conceptual shift toward “scarring/arrhythmogenic cardiomyopathy” (graziano2024the2023european pages 1-2).

### 10.3 Differential diagnosis
LV-dominant arrhythmogenic cardiomyopathy can mimic **myocarditis** and should be distinguished from **sarcoidosis** and **dilated cardiomyopathy** using imaging patterning, multimodal evaluation, and genetics (smith2020desmoplakincardiomyopathya pages 1-3, mauriello2024arrhythmogenicleftventricular pages 1-2).

### 10.4 Screening (asymptomatic carriers)
Evidence in this run supports cascade screening practices in genotype-first DSP cohorts and broader genetic cardiomyopathy surveillance strategies (reza2022cardiovascularcharacteristicsof pages 2-4, NCT06446271 chunk 1).

---

## 11. Outcome / prognosis

### 11.1 Key outcome statistics from DSP cohorts
- Severe ventricular arrhythmia composite (sustained VT/SCD/appropriate ICD therapy) occurred in **28% (30/107)** of DSP patients in a multicenter Circulation cohort (Jun 2020) (smith2020desmoplakincardiomyopathya pages 8-10).
- In a Europace cohort (Aug 2022), incidence rates were **5.9/100 person-years** for sustained ventricular arrhythmia and **6.7/100 person-years** for heart failure (wang2022clinicalcharacteristicsand pages 1-2).
- Myocardial injury episodes were associated with worse outcomes (univariate HR **2.53** for sustained ventricular arrhythmia and HR **7.53** for heart failure) (wang2022clinicalcharacteristicsand pages 1-2).

### 11.2 Prognostic factors
- LV function thresholds: LVEF <55% was associated with severe arrhythmias in DSP cohorts; relying only on very low EF cutoffs may miss risk (smith2020desmoplakincardiomyopathya pages 1-3).
- Myocardial injury episodes are prognostic for heart failure outcomes in cohort analyses (wang2022clinicalcharacteristicsand pages 1-2).

---

## 12. Treatment

### 12.1 Standard management (real-world implementation)
- **ICD therapy** is described in authoritative S/ACM reviews as the **only proven life-saving treatment** for prevention of sudden death, while acknowledging morbidity related to devices and challenges in selecting recipients (corrado2023scarringarrhythmogeniccardiomyopathy pages 1-2).
- **Medical therapy** for ventricular arrhythmias and heart failure is described as crucial in S/ACM (corrado2023scarringarrhythmogeniccardiomyopathy pages 1-2).
- Case-based evidence indicates use of guideline-directed heart failure therapy (e.g., ACE inhibitor and beta-blocker) and ICD placement for primary prevention in selected DSP cardiomyopathy patients, aligned with contemporary ESC cardiomyopathy guidance (fatrous2025desmoplakincardiomyopathymyocarditislike pages 5-6).

### 12.2 Hot-phase / inflammatory episodes
Limited case literature reports the use of immunosuppressive strategies in selected recurrent myocarditis-like DSP presentations; however, high-quality evidence for standardized immunosuppression is not established in the retrieved DSP-specific evidence set (fatrous2025desmoplakincardiomyopathymyocarditislike pages 5-6).

### 12.3 Treatment ontology suggestions (MAXO)
Suggested MAXO terms for curation (examples):
- Implantable cardioverter-defibrillator implantation
- Beta-blocker therapy
- ACE inhibitor therapy
- Catheter ablation of ventricular tachycardia (not directly supported by retrieved primary text here; included only as a general ACM action type)

---

## 13. Prevention

### 13.1 Primary/secondary/tertiary prevention
- **Secondary prevention:** ICD implantation in individuals at high arrhythmic risk is central to preventing sudden death (corrado2023scarringarrhythmogeniccardiomyopathy pages 1-2).
- **Secondary prevention via screening:** genetic testing with cascade evaluation of relatives and multimodal surveillance aims to identify disease early and prevent catastrophic arrhythmic events (NCT06446271 chunk 1).
- Exercise restriction as formal prevention guidance was not explicitly quoted in the retrieved sources; only mechanistic/exacerbation framing via stress/exercise was captured (corrado2023scarringarrhythmogeniccardiomyopathy pages 1-2).

---

## 14. Other species / natural disease
No naturally occurring DSP cardiomyopathy in non-human species (e.g., companion animals) was identified in the retrieved evidence.

---

## 15. Model organisms / model systems

### 15.1 Human cellular models (2023 development highlight)
Human induced pluripotent stem cell (hiPSC)-derived cardiomyocytes are emphasized as a **reproducible and scalable** platform to model desmosome-related arrhythmogenic cardiomyopathy (including DSP as a causal gene), supporting mechanistic studies and drug screening in human cells (Sep 2023) (chua2023understandingarrhythmogeniccardiomyopathy pages 1-3, chua2023understandingarrhythmogeniccardiomyopathy pages 3-4).

### 15.2 Animal models
Authoritative S/ACM review literature discusses animal-model evidence of early cardiomyocyte injury features (e.g., sarcolemmal disruption, mitochondrial swelling, cardiomyocyte necrosis) in a transgenic mouse model context, supporting the injury → scar concept (corrado2023scarringarrhythmogeniccardiomyopathy pages 1-2).

---

## Recent developments and latest research (2023–2024 emphasis)
Key 2023–2024 themes captured by tool-retrieved sources:
1) **Formalization of “scarring/arrhythmogenic cardiomyopathy”**: Emphasis on non-ischemic scar as the diagnostic and arrhythmogenic core substrate (Apr 2023) (corrado2023scarringarrhythmogeniccardiomyopathy pages 1-2).
2) **Criteria modernization for LV phenotypes**: Reviews of evolving criteria highlight the shift from 2010 RV-centered criteria toward Padua (2020) and European Task Force (2023) LV-inclusive frameworks (Sep 2024) (graziano2024the2023european pages 1-2).
3) **CMR centrality**: 2023 imaging reviews consolidate CMR as the imaging technique of choice for tissue characterization across ACM phenotypes, particularly LV variants (Jul 2023) (cipriani2023cardiacmagneticresonance pages 1-2).
4) **hiPSC modeling**: 2023 methodological progress highlights hiPSC-CM platforms for desmosomal ACM mechanistic and therapeutic discovery, relevant to DSP disease-modification research (Sep 2023) (chua2023understandingarrhythmogeniccardiomyopathy pages 1-3).

---

## Clinical trials and real-world research infrastructure relevant to DSP cardiomyopathy

1) **Hybrid PET-MR characterization of genetic arrhythmogenic cardiomyopathies (CharACTPET-MR)**
- NCT: **NCT05450783**; recruiting (last update posted 2024-12-02).
- Includes gene carriers with pathogenic/likely pathogenic variants in multiple genes including **DSP**.
- Primary aim: characterize LV PET-MRI patterns combining LGE and FDG-PET uptake, and correlate with outcomes (death, transplant, resuscitated SCD, unstable VT, HF hospitalization, myocarditis) (NCT05450783 chunk 1).
- ClinicalTrials.gov URL: https://clinicaltrials.gov/study/NCT05450783 (NCT05450783 chunk 1).

2) **DNA analysis from isolated cardiomyocytes for molecular diagnosis of ARVC/ACM**
- NCT: **NCT03177018**; completed.
- Includes exploration of somatic mosaicism and feasibility of epigenetic analyses for PKP2/DSP/DSG2 from cardiomyocyte DNA (NCT03177018 chunk 1).
- ClinicalTrials.gov URL: https://clinicaltrials.gov/study/NCT03177018 (NCT03177018 chunk 1).

3) **Biomarkers in Scotland Cardiomyopathy Registry (Bio-SCOTCH)**
- NCT: **NCT06446271**; recruiting (first posted 2024-06-06).
- Enrolls participants with TTN, MYBPC3, LMNA, FLNC, or **DSP** variants; aims to develop blood/urine/ECG/imaging biomarkers to detect preclinical disease and predict progression (NCT06446271 chunk 1).
- ClinicalTrials.gov URL: https://clinicaltrials.gov/study/NCT06446271 (NCT06446271 chunk 1).

---

## Direct quotes from abstracts (high-value statements)
- Circulation cohort definition: DSP cardiomyopathy described as **“a fibrotic and inflammatory form of cardiomyopathy distinct from typical dilated or arrhythmogenic right ventricular cardiomyopathy”** (Jun 2020) (smith2020desmoplakincardiomyopathya pages 4-6).
- 2023 criteria evolution review abstract: ACM is “**featured by non-ischemic myocardial scarring linked to ventricular electrical instability**” and criteria evolved to incorporate LV variants and CMR (Sep 2024) (graziano2024the2023european pages 1-2).

---

## Data gaps and limitations of this tool-based evidence set
- **Disease identifiers** (OMIM, Orphanet, ICD-10/11, MeSH, MONDO) were not present in retrieved full text and cannot be asserted without additional database retrieval beyond the current tool outputs.
- Many clinically important areas (precise penetrance by age/sex, population prevalence/incidence, standardized hot-phase immunosuppression evidence, QoL metrics, and DSP-specific omics signatures) were not available in the retrieved documents and therefore are not included as definitive statements.

---

## Key references (with URLs and publication dates as captured)
- Smith ED et al. *Circulation* (Jun 2020). https://doi.org/10.1161/CIRCULATIONAHA.119.044934 (smith2020desmoplakincardiomyopathya pages 1-3)
- Wang W et al. *Europace* (Aug 2022). https://doi.org/10.1093/europace/euab183 (wang2022clinicalcharacteristicsand pages 1-2)
- Brandão M et al. *Journal of Clinical Medicine* (Apr 2023). https://doi.org/10.3390/jcm12072660 (brandao2023desmoplakincardiomyopathycomprehensive pages 2-4)
- Corrado D et al. *European Heart Journal Supplements* (Apr 2023). https://doi.org/10.1093/eurheartjsupp/suad017 (corrado2023scarringarrhythmogeniccardiomyopathy pages 1-2)
- Cipriani A et al. *European Radiology* (Jul 2023). https://doi.org/10.1007/s00330-022-08958-2 (cipriani2023cardiacmagneticresonance pages 1-2)
- Chua CJ et al. *Genes* (Sep 2023). https://doi.org/10.3390/genes14101864 (chua2023understandingarrhythmogeniccardiomyopathy pages 1-3)
- Mauriello A et al. *Journal of Clinical Medicine* (Mar 2024). https://doi.org/10.3390/jcm13071835 (mauriello2024arrhythmogenicleftventricular pages 1-2)
- Graziano F et al. *Reviews in Cardiovascular Medicine* (Sep 2024). https://doi.org/10.31083/j.rcm2509348 (graziano2024the2023european pages 1-2)


References

1. (smith2020desmoplakincardiomyopathya pages 1-3): Eric D. Smith, Neal K. Lakdawala, Nikolaos Papoutsidakis, Gregory Aubert, Andrea Mazzanti, Anthony C. McCanta, Prachi P. Agarwal, Patricia Arscott, Lisa M. Dellefave-Castillo, Esther E. Vorovich, Kavitha Nutakki, Lisa D. Wilsbacher, Silvia G. Priori, Daniel L. Jacoby, Elizabeth M. McNally, and Adam S. Helms. Desmoplakin cardiomyopathy, a fibrotic and inflammatory form of cardiomyopathy distinct from typical dilated or arrhythmogenic right ventricular cardiomyopathy. Circulation, 141:1872-1884, Jun 2020. URL: https://doi.org/10.1161/circulationaha.119.044934, doi:10.1161/circulationaha.119.044934. This article has 498 citations and is from a highest quality peer-reviewed journal.

2. (wang2022clinicalcharacteristicsand pages 1-2): Weijia Wang, Brittney Murray, Crystal Tichnell, Nisha A Gilotra, Stefan L Zimmerman, Alessio Gasperetti, Paul Scheel, Harikrishna Tandri, Hugh Calkins, and Cynthia A James. Clinical characteristics and risk stratification of desmoplakin cardiomyopathy. Europace, 24:268-277, Aug 2022. URL: https://doi.org/10.1093/europace/euab183, doi:10.1093/europace/euab183. This article has 106 citations and is from a domain leading peer-reviewed journal.

3. (brandao2023desmoplakincardiomyopathycomprehensive pages 2-4): Mariana Brandão, Riccardo Bariani, Ilaria Rigato, and Barbara Bauce. Desmoplakin cardiomyopathy: comprehensive review of an increasingly recognized entity. Journal of Clinical Medicine, 12:2660, Apr 2023. URL: https://doi.org/10.3390/jcm12072660, doi:10.3390/jcm12072660. This article has 50 citations.

4. (graziano2024the2023european pages 1-2): Francesca Graziano, Alessandro Zorzi, Simone Ungaro, Barbara Bauce, Ilaria Rigato, Alberto Cipriani, Martina Perazzolo Marra, Kalliopi Pilichou, Cristina Basso, and Domenico Corrado. The 2023 european task force criteria for diagnosis of arrhythmogenic cardiomyopathy: historical background and review of main changes. Reviews in Cardiovascular Medicine, Sep 2024. URL: https://doi.org/10.31083/j.rcm2509348, doi:10.31083/j.rcm2509348. This article has 9 citations and is from a peer-reviewed journal.

5. (corrado2023scarringarrhythmogeniccardiomyopathy pages 1-2): Domenico Corrado, Alessandro Zorzi, Alberto Cipriani, Barbara Bauce, Riccardo Bariani, Giulia Brunetti, Francesca Graziano, Manuel De Lazzari, Giulia Mattesi, Federico Migliore, Kalliopi Pilichou, Ilaria Rigato, Stefania Rizzo, Gaetano Thiene, Martina Perazzolo Marra, and Cristina Basso. Scarring/arrhythmogenic cardiomyopathy. European Heart Journal Supplements : Journal of the European Society of Cardiology, 25:C144-C154, Apr 2023. URL: https://doi.org/10.1093/eurheartjsupp/suad017, doi:10.1093/eurheartjsupp/suad017. This article has 35 citations.

6. (brandao2023desmoplakincardiomyopathycomprehensive pages 1-2): Mariana Brandão, Riccardo Bariani, Ilaria Rigato, and Barbara Bauce. Desmoplakin cardiomyopathy: comprehensive review of an increasingly recognized entity. Journal of Clinical Medicine, 12:2660, Apr 2023. URL: https://doi.org/10.3390/jcm12072660, doi:10.3390/jcm12072660. This article has 50 citations.

7. (smith2020desmoplakincardiomyopathya pages 4-6): Eric D. Smith, Neal K. Lakdawala, Nikolaos Papoutsidakis, Gregory Aubert, Andrea Mazzanti, Anthony C. McCanta, Prachi P. Agarwal, Patricia Arscott, Lisa M. Dellefave-Castillo, Esther E. Vorovich, Kavitha Nutakki, Lisa D. Wilsbacher, Silvia G. Priori, Daniel L. Jacoby, Elizabeth M. McNally, and Adam S. Helms. Desmoplakin cardiomyopathy, a fibrotic and inflammatory form of cardiomyopathy distinct from typical dilated or arrhythmogenic right ventricular cardiomyopathy. Circulation, 141:1872-1884, Jun 2020. URL: https://doi.org/10.1161/circulationaha.119.044934, doi:10.1161/circulationaha.119.044934. This article has 498 citations and is from a highest quality peer-reviewed journal.

8. (cipriani2023cardiacmagneticresonance pages 1-2): Alberto Cipriani, Giulia Mattesi, Riccardo Bariani, Annagrazia Cecere, Nicolò Martini, Laura De Michieli, Stefano Da Pozzo, Simone Corradin, Giorgio De Conti, Alessandro Zorzi, Raffaella Motta, Manuel De Lazzari, Barbara Bauce, Sabino Iliceto, Cristina Basso, Domenico Corrado, and Martina Perazzolo Marra. Cardiac magnetic resonance imaging of arrhythmogenic cardiomyopathy: evolving diagnostic perspectives. European Radiology, 33:270-282, Jul 2023. URL: https://doi.org/10.1007/s00330-022-08958-2, doi:10.1007/s00330-022-08958-2. This article has 53 citations and is from a domain leading peer-reviewed journal.

9. (smith2020desmoplakincardiomyopathya pages 8-10): Eric D. Smith, Neal K. Lakdawala, Nikolaos Papoutsidakis, Gregory Aubert, Andrea Mazzanti, Anthony C. McCanta, Prachi P. Agarwal, Patricia Arscott, Lisa M. Dellefave-Castillo, Esther E. Vorovich, Kavitha Nutakki, Lisa D. Wilsbacher, Silvia G. Priori, Daniel L. Jacoby, Elizabeth M. McNally, and Adam S. Helms. Desmoplakin cardiomyopathy, a fibrotic and inflammatory form of cardiomyopathy distinct from typical dilated or arrhythmogenic right ventricular cardiomyopathy. Circulation, 141:1872-1884, Jun 2020. URL: https://doi.org/10.1161/circulationaha.119.044934, doi:10.1161/circulationaha.119.044934. This article has 498 citations and is from a highest quality peer-reviewed journal.

10. (chua2023understandingarrhythmogeniccardiomyopathy pages 1-3): Christianne J. Chua, Justin Morrissette-McAlmon, Leslie Tung, and Kenneth R. Boheler. Understanding arrhythmogenic cardiomyopathy: advances through the use of human pluripotent stem cell models. Genes, 14:1864, Sep 2023. URL: https://doi.org/10.3390/genes14101864, doi:10.3390/genes14101864. This article has 19 citations.

11. (wang2022clinicalcharacteristicsand pages 2-3): Weijia Wang, Brittney Murray, Crystal Tichnell, Nisha A Gilotra, Stefan L Zimmerman, Alessio Gasperetti, Paul Scheel, Harikrishna Tandri, Hugh Calkins, and Cynthia A James. Clinical characteristics and risk stratification of desmoplakin cardiomyopathy. Europace, 24:268-277, Aug 2022. URL: https://doi.org/10.1093/europace/euab183, doi:10.1093/europace/euab183. This article has 106 citations and is from a domain leading peer-reviewed journal.

12. (chua2023understandingarrhythmogeniccardiomyopathy pages 3-4): Christianne J. Chua, Justin Morrissette-McAlmon, Leslie Tung, and Kenneth R. Boheler. Understanding arrhythmogenic cardiomyopathy: advances through the use of human pluripotent stem cell models. Genes, 14:1864, Sep 2023. URL: https://doi.org/10.3390/genes14101864, doi:10.3390/genes14101864. This article has 19 citations.

13. (wang2022clinicalcharacteristicsand pages 8-9): Weijia Wang, Brittney Murray, Crystal Tichnell, Nisha A Gilotra, Stefan L Zimmerman, Alessio Gasperetti, Paul Scheel, Harikrishna Tandri, Hugh Calkins, and Cynthia A James. Clinical characteristics and risk stratification of desmoplakin cardiomyopathy. Europace, 24:268-277, Aug 2022. URL: https://doi.org/10.1093/europace/euab183, doi:10.1093/europace/euab183. This article has 106 citations and is from a domain leading peer-reviewed journal.

14. (mauriello2024arrhythmogenicleftventricular pages 1-2): Alfredo Mauriello, Anna Selvaggia Roma, Antonia Ascrizzi, Riccardo Molinari, Francesco S. Loffredo, Antonello D’Andrea, and Vincenzo Russo. Arrhythmogenic left ventricular cardiomyopathy: from diagnosis to risk management. Journal of Clinical Medicine, 13:1835, Mar 2024. URL: https://doi.org/10.3390/jcm13071835, doi:10.3390/jcm13071835. This article has 4 citations.

15. (fatrous2025desmoplakincardiomyopathymyocarditislike pages 5-6): Tarek Fatrous, Sara Ibzea, and Sharafath Hussain Zahir Hussain. Desmoplakin cardiomyopathy: myocarditis-like episodes. Cureus, Jul 2025. URL: https://doi.org/10.7759/cureus.87311, doi:10.7759/cureus.87311. This article has 1 citations.

16. (brandao2023desmoplakincardiomyopathycomprehensive pages 9-11): Mariana Brandão, Riccardo Bariani, Ilaria Rigato, and Barbara Bauce. Desmoplakin cardiomyopathy: comprehensive review of an increasingly recognized entity. Journal of Clinical Medicine, 12:2660, Apr 2023. URL: https://doi.org/10.3390/jcm12072660, doi:10.3390/jcm12072660. This article has 50 citations.

17. (reza2022cardiovascularcharacteristicsof pages 2-4): Nosheen Reza, Alejandro de Feria, Jessica L. Chowns, Lily Hoffman-Andrews, Laura Vann, Jessica Kim, Amy Marzolf, and Anjali Tiku Owens. Cardiovascular characteristics of patients with genetic variation in desmoplakin (dsp). Cardiogenetics, 12:24-36, Jan 2022. URL: https://doi.org/10.3390/cardiogenetics12010003, doi:10.3390/cardiogenetics12010003. This article has 15 citations.

18. (NCT03177018 chunk 1):  DNA Analysis From Isolated Cardiomyocytes in the Molecular Diagnosis of Arrhythmogenic Right Ventricular Cardiomyopathy/Dysplasia. University Hospital, Toulouse. 2016. ClinicalTrials.gov Identifier: NCT03177018

19. (NCT06446271 chunk 1):  Biomarkers in SCOTland CardiomyopatHy Registry (Bio-SCOTCH). NHS Greater Glasgow and Clyde. 2024. ClinicalTrials.gov Identifier: NCT06446271

20. (NCT05450783 chunk 1):  Tissue and Metabolic Characterization of Arrhythmogenic Cardiomyopathies by Hybrid PET-MRI Imaging, Impact of the Observed Profiles on the Phenotype and on the Evolution of Cardiomyopathy. Nantes University Hospital. 2022. ClinicalTrials.gov Identifier: NCT05450783