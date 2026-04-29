---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-23T18:35:12.165975'
end_time: '2026-04-23T18:53:32.420779'
duration_seconds: 1100.25
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Spasticity-Ataxia-Gait Anomalies Syndrome
  mondo_id: ''
  category: Neurological Disorder
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 25
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spasticity-Ataxia-Gait Anomalies Syndrome
- **MONDO ID:**  (if available)
- **Category:** Neurological Disorder

## Research Objectives

Please provide a comprehensive research report on **Spasticity-Ataxia-Gait Anomalies Syndrome** covering all of the
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
- **Disease Name:** Spasticity-Ataxia-Gait Anomalies Syndrome
- **MONDO ID:**  (if available)
- **Category:** Neurological Disorder

## Research Objectives

Please provide a comprehensive research report on **Spasticity-Ataxia-Gait Anomalies Syndrome** covering all of the
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


## Comprehensive Research Report: “Spasticity–Ataxia–Gait Anomalies Syndrome” (mapped to **Spastic Ataxia / SPAX phenotype**)

### Executive summary
The string **“Spasticity-Ataxia-Gait Anomalies Syndrome”** is not a standardized disease name in the peer‑reviewed sources retrieved here. The most evidence-supported mapping is to the **spastic ataxia (SPAX) phenotype**—a clinical syndrome defined by **cerebellar ataxia plus spasticity/pyramidal signs**, which can arise from multiple gene-defined disorders (e.g., **ARSACS/SACS**, **SPG7/SPG7**, **SPAX3/MARS2**, **SPAX4/MTPAP**, **SPAX5/AFG3L2**) (bot2012reviewingthegenetic pages 4-5, scaravilli2024anmrievaluation pages 1-2).

| Proposed standardized concept | Key synonyms/labels | Causal gene(s) | Inheritance | Key distinguishing features | Key citations with year/URL |
|---|---|---|---|---|---|
| Spastic ataxia (SPAX) phenotype | Spastic ataxia; SPAX; cerebellar ataxia with spasticity/pyramidal features | Phenotype-level umbrella; includes multiple genes/disorders | Mixed, depends on underlying disorder | Literature defines SPAX as a clinical phenotype characterized by cerebellar ataxia plus spasticity and other pyramidal features; useful highest-level mapping for the user label “Spasticity-Ataxia-Gait Anomalies Syndrome” (scaravilli2024anmrievaluation pages 1-2) | Scaravilli et al., 2024, *J Neurol* https://doi.org/10.1007/s00415-024-12505-y (scaravilli2024anmrievaluation pages 1-2) |
| ARSACS | Autosomal recessive spastic ataxia of Charlevoix-Saguenay; paradigmatic SPAX | **SACS** | Autosomal recessive | Early-onset spastic ataxia with severe white-matter involvement on diffusion MRI; in PROSPAX, ARSACS showed reduced global WM volume and altered microstructural metrics, with WM damage correlating with SARA scores; clinically often used as a core SPAX disorder and is the population targeted in rehabilitation trial NCT06261424 (scaravilli2024anmrievaluation pages 1-2, scaravilli2024anmrievaluation pages 2-4, NCT06261424 chunk 1) | Scaravilli et al., 2024, https://doi.org/10.1007/s00415-024-12505-y; Duchesne, NCT06261424, 2024, ClinicalTrials.gov (scaravilli2024anmrievaluation pages 1-2, scaravilli2024anmrievaluation pages 2-4, NCT06261424 chunk 1) |
| SPG7-associated spastic ataxia | SPG7; hereditary spastic paraplegia type 7; paradigmatic SPAX | **SPG7** | Usually autosomal recessive | Frequently presents with combined ataxia and spasticity; in PROSPAX, SPG7 had milder mean WM microstructural damage than ARSACS; NCT06261424 enrolls genetically confirmed SPG7 alongside ARSACS for supervised rehabilitation (scaravilli2024anmrievaluation pages 1-2, scaravilli2024anmrievaluation pages 2-4, NCT06261424 chunk 1) | Scaravilli et al., 2024, https://doi.org/10.1007/s00415-024-12505-y; Duchesne, NCT06261424, 2024, ClinicalTrials.gov (scaravilli2024anmrievaluation pages 1-2, scaravilli2024anmrievaluation pages 2-4, NCT06261424 chunk 1) |
| SPAX3 | Autosomal recessive spastic ataxia 3; spastic ataxia with leukoencephalopathy; ARSAL | **MARS2** | Autosomal recessive | Described as spastic-ataxia with periventricular white-matter changes and cerebellar atrophy; age at onset reported from 2 to 59 years; strong match when gait abnormality co-occurs with leukodystrophy/leukoencephalopathy features (bot2012reviewingthegenetic pages 4-5) | de Bot et al., 2012, *Neurology* https://doi.org/10.1212/WNL.0b013e31826d5fb0 (bot2012reviewingthegenetic pages 4-5) |
| SPAX4 | Autosomal recessive spastic ataxia 4 | **MTPAP** | Autosomal recessive | Childhood-onset spastic paraparesis with cerebellar ataxia and dysarthria; additional features may include optic atrophy, delayed walking/speech, learning difficulties, emotional lability, and later areflexia—important when the user label implies developmental gait anomalies (bot2012reviewingthegenetic pages 4-5) | de Bot et al., 2012, *Neurology* https://doi.org/10.1212/WNL.0b013e31826d5fb0 (bot2012reviewingthegenetic pages 4-5) |
| SPAX5 | Autosomal recessive spastic ataxia 5; AFG3L2-associated spastic-ataxia-neuropathy syndrome | **AFG3L2** | Autosomal recessive | Early-onset spastic-ataxic syndrome with neuropathy, cerebellar atrophy, oculomotor apraxia, dystonia, and mitochondrial features; mechanistically linked to AFG3L2 loss causing mitochondrial proteotoxicity, OMA1-DELE1-HRI integrated stress response activation, and potential therapeutic response to Sephin-1 in models (bot2012reviewingthegenetic pages 5-6, franchino2024sustainedoma1mediatedintegrated pages 1-2, franchino2024sustainedoma1mediatedintegrated pages 10-13) | de Bot et al., 2012, https://doi.org/10.1212/WNL.0b013e31826d5fb0; Franchino et al., 2024, *Brain* https://doi.org/10.1093/brain/awad340 (bot2012reviewingthegenetic pages 5-6, franchino2024sustainedoma1mediatedintegrated pages 1-2, franchino2024sustainedoma1mediatedintegrated pages 10-13) |
| SPAX1 | Spastic ataxia 1 | Locus on chromosome 12p13; gene not established in cited context | Autosomal dominant | Progressive spastic-ataxia reported in Newfoundland families, usually before age 20; useful historical SPAX mapping term, but less actionable clinically because gene was not established in the cited review (bot2012reviewingthegenetic pages 4-5) | de Bot et al., 2012, *Neurology* https://doi.org/10.1212/WNL.0b013e31826d5fb0 (bot2012reviewingthegenetic pages 4-5) |
| SPAX2 | Spastic ataxia 2 | Locus on chromosome 17p13; gene not established in cited context | Autosomal recessive | Family described with dysarthria and gait ataxia around age 14, later mild spasticity with amyotrophy/fasciculations; relevant if the user label is interpreted as a descriptive rather than gene-specific syndrome (bot2012reviewingthegenetic pages 4-5) | de Bot et al., 2012, *Neurology* https://doi.org/10.1212/WNL.0b013e31826d5fb0 (bot2012reviewingthegenetic pages 4-5) |


*Table: This table maps the nonstandard label “Spasticity-Ataxia-Gait Anomalies Syndrome” to standardized spastic-ataxia concepts used in the literature. It helps anchor the user’s query to phenotype-level and gene-defined entities that are actually described in current research and clinical studies.*

---

## 1. Disease information

### 1.1 What is the disease?
**Current understanding:** “Spastic ataxia (SPAX)” is used in contemporary neurology as a **phenotype-level umbrella**: **cerebellar ataxia with spasticity and other pyramidal features** (scaravilli2024anmrievaluation pages 1-2). This umbrella includes multiple genetic conditions; two “paradigmatic” forms that are frequently studied are **ARSACS** and **SPG7-associated spastic ataxia** (scaravilli2024anmrievaluation pages 1-2, scaravilli2024anmrievaluation pages 2-4).

### 1.2 Key identifiers (OMIM/Orphanet/ICD/MeSH/MONDO)
* **OMIM (MIM) identifiers available from a classic spastic-ataxia review:**
  * **SPAX1**: *Spastic ataxia 1* (MIM **%108600**) (bot2012reviewingthegenetic pages 4-5)
  * **SPAX2**: *Spastic ataxia 2* (MIM **%611302**) (bot2012reviewingthegenetic pages 4-5)
  * **SPAX3/ARSAL**: *Autosomal recessive spastic ataxia 3* (MIM **\*609728**) (bot2012reviewingthegenetic pages 4-5)
  * **SPAX4**: *Autosomal recessive spastic ataxia 4* (MIM **#613672**) (bot2012reviewingthegenetic pages 4-5)
  * **SPAX5**: associated with **AFG3L2**; condition listed as MIM **#614487**; AFG3L2 gene MIM **\*604581** (bot2012reviewingthegenetic pages 5-6)
* **MONDO / Orphanet / ICD / MeSH:** Not found in the retrieved evidence context for the exact user-provided label; mapping will depend on which **gene-defined entity** is intended.

### 1.3 Synonyms and alternative names (evidence-based)
* “**Spastic ataxia**” / “**SPAX**” phenotype (scaravilli2024anmrievaluation pages 1-2)
* “**Autosomal recessive spastic ataxia of Charlevoix–Saguenay (ARSACS)**” (scaravilli2024anmrievaluation pages 1-2, argenziano2024vestibularhypofunctionin pages 1-3)
* “**Spastic paraplegia type 7 (SPG7)**” with a spastic-ataxic phenotype (scaravilli2024anmrievaluation pages 1-2)
* “**Spastic ataxia with leukoencephalopathy**” / “**ARSAL**” for SPAX3 (bot2012reviewingthegenetic pages 4-5)

### 1.4 Evidence source type
The information synthesized here is primarily from:
* Aggregated resources (systematic reviews/meta-analyses, mechanistic reviews, multicenter imaging studies) (scaravilli2024anmrievaluation pages 1-2, fereshtehnejad2023movementdisordersin pages 1-2, damiani2024pluripotentstemcells pages 14-15)
* Primary observational genetics studies (families/cohorts) (azeem2024investigatingthegenetic pages 4-5)
* Primary mechanistic disease-model work (patient fibroblasts and mouse/Purkinje neuron models) (franchino2024sustainedoma1mediatedintegrated pages 10-13)
* ClinicalTrials.gov registry data for real-world trial implementation (NCT06261424 chunk 1)

---

## 2. Etiology

### 2.1 Disease causal factors
**Genetic causes predominate** in the SPAX phenotype. A reference spastic-ataxia genetic review enumerates multiple Mendelian entities; for several SPAX subtypes, causal genes are established:
* **SPAX3/ARSAL** caused by **MARS2** mutations; phenotype includes spastic-ataxia plus white matter changes and cerebellar atrophy, with onset ranging **2–59 years** (bot2012reviewingthegenetic pages 4-5).
* **SPAX4** caused by homozygous **MTPAP** mutations; childhood-onset spastic paraparesis with cerebellar ataxia and additional features (e.g., optic atrophy, learning difficulties) (bot2012reviewingthegenetic pages 4-5).
* **SPAX5** associated with **AFG3L2** mutations (bot2012reviewingthegenetic pages 5-6, franchino2024sustainedoma1mediatedintegrated pages 1-2).
* **ARSACS** due to **SACS** variants (argenziano2024vestibularhypofunctionin pages 1-3).
* **SPG7-associated spastic ataxia** due to biallelic **SPG7** variants (scaravilli2024anmrievaluation pages 1-2).

### 2.2 Risk factors
* **Consanguinity/endogamy** is a recurrent risk factor for autosomal recessive neurogenetic disorders in affected families, and is explicitly highlighted as common in a 2024 Pakistani-family study of HSP/HCA with spastic-ataxia overlap (azeem2024investigatingthegenetic pages 4-5).

### 2.3 Protective factors / gene–environment interactions
No protective factors or gene–environment interactions specific to “spasticity–ataxia–gait anomalies syndrome” were identified in the retrieved evidence.

---

## 3. Phenotypes

### 3.1 Core phenotype elements (SPAX concept)
* **Spasticity/pyramidal signs** and **cerebellar ataxia** with **gait disturbance** are the defining clinical combination (scaravilli2024anmrievaluation pages 1-2).

### 3.2 Phenotype characteristics from recent/authoritative sources
* **ARSACS (SACS):** described as early-onset ataxia characterized by **cerebellar dysfunction, spasticity, and sensory-motor polyneuropathy** (argenziano2024vestibularhypofunctionin pages 1-3). In a 2024 case report, exam showed **“spastic-ataxic gait”**, dysarthria, four-limb ataxia, and spastic hypertonia with lower-limb hyperreflexia (argenziano2024vestibularhypofunctionin pages 1-3).
* **SPG7 vs SPG11 (genotype–phenotype statistics, 2023 IPD meta-analysis):** In HSP cases with movement disorders, **SPG7** and **SPG11** were the most frequent genotypes (**31.2%** and **23.8%**) (fereshtehnejad2023movementdisordersin pages 1-2). Compared to SPG11, SPG7 cases had higher frequency of adult onset (82.9% vs 8.5%) and stronger association with **ataxia** (OR **12.6**) and extraocular movement disturbances (OR **3.4**) (fereshtehnejad2023movementdisordersin pages 1-2).
* **Disease course/variability:** A 2024 ARSACS vestibular paper emphasizes variable expression in ARSACS (absence of some “defining” features may occur), underscoring that SPAX disorders may show incomplete/variable phenotypes (argenziano2024vestibularhypofunctionin pages 3-4).

### 3.3 Vestibular/oculomotor phenotypes (important for differential diagnosis)
ARSACS may show vestibular hypofunction, potentially mimicking CANVAS; in the reported ARSACS case, vHIT showed **bilateral, symmetrical vestibulo-ocular reflex (VOR) impairment** across semicircular canals and gaze-evoked/rebound nystagmus and saccadic pursuit abnormalities (argenziano2024vestibularhypofunctionin pages 1-3, argenziano2024vestibularhypofunctionin pages 3-4).

### 3.4 Suggested HPO terms (non-exhaustive; for knowledge base curation)
* Spasticity (**HP:0001257**)
* Hyperreflexia (**HP:0001347**)
* Cerebellar ataxia (**HP:0001251**)
* Gait ataxia (**HP:0002066**)
* Spastic gait (**HP:0002064**)
* Dysarthria (**HP:0001260**)
* Peripheral neuropathy (**HP:0009830**)
* Optic atrophy (**HP:0000648**) (noted in SPAX4 description) (bot2012reviewingthegenetic pages 4-5)
* Cerebellar atrophy (**HP:0001272**) (noted across spastic ataxia entities; e.g., ARSACS/SPAX3) (bot2012reviewingthegenetic pages 4-5, scaravilli2024anmrievaluation pages 1-2)

(Where phenotype-level statements are evidence-based: see citations above.)

---

## 4. Genetic / molecular information

### 4.1 Causal genes highlighted in evidence
Key causal genes for spastic-ataxia entities in the retrieved sources include **MARS2 (SPAX3/ARSAL)**, **MTPAP (SPAX4)**, **AFG3L2 (SPAX5)**, **SACS (ARSACS)**, and **SPG7 (SPG7 spastic ataxia phenotype)** (bot2012reviewingthegenetic pages 4-5, bot2012reviewingthegenetic pages 5-6, scaravilli2024anmrievaluation pages 1-2, argenziano2024vestibularhypofunctionin pages 1-3).

### 4.2 Examples of pathogenic variants (recent cohort data)
A 2024 Pakistani-family WES study reported pathogenic variants segregating with HSP/HCA phenotypes (including spasticity/ataxia/gait phenotypes) in **5/8 families (62.5%)**, all consistent with autosomal recessive inheritance; onset ranged **1–14 years** (mean **6.23**, SD **3.96**) (azeem2024investigatingthegenetic pages 4-5). Reported variants included:
* **SACS**: c.2182C>T p.(Arg728*); c.2229del p.(Phe743Leufs*8)
* **FA2H**: c.159_176del p.(Arg53_Ile58del)
* **ZFYVE26**: c.1926_1941del p.(Tyr643Metfs*2)
* **SPG11**: c.2146C>T p.(Gln716*) (azeem2024investigatingthegenetic pages 1-2, azeem2024investigatingthegenetic pages 4-5)

### 4.3 Functional consequences and pathways (mechanistic evidence)
**SPAX5 (AFG3L2) mechanism (2024, Brain):** SPAX5 results from biallelic **AFG3L2** mutations; mechanistic work shows AFG3L2 loss/mutation leads to mitochondrial proteotoxic stress with activation of the stress-sensitive protease **OMA1**, engagement of an **OMA1–DELE1–HRI** axis, increased **eIF2α phosphorylation**, increased **ATF4**, and upregulation of ISR target genes (including Chop, Chac1, Ppp1r15a, Fgf21) in patient fibroblasts and Afg3l2−/− mouse cerebellum (franchino2024sustainedoma1mediatedintegrated pages 1-2, franchino2024sustainedoma1mediatedintegrated pages 10-13). Pharmacologic potentiation of the ISR with **Sephin‑1** improved multiple cellular/neuron readouts and extended survival in Afg3l2−/− mice (franchino2024sustainedoma1mediatedintegrated pages 10-13).

**SPG7 mitochondrial quality control (cell models):** An iPSC-model review summarizes that SPG7/paraplegin is an inner-mitochondrial-membrane protease involved in mitochondrial protein quality control and biogenesis; patient-derived models show fragmented mitochondria, reduced respiration/ATP-linked oxygen consumption, increased ROS, and reduced neurite complexity (damiani2024pluripotentstemcells pages 14-15).

### 4.4 Suggested GO / pathway terms
* Mitochondrial protein quality control / proteostasis (e.g., GO: mitochondrial protein processing)
* Integrated stress response / eIF2α phosphorylation / ATF4 signaling
* Mitochondrial fragmentation / OPA1 processing

(Evidence for these mechanisms in SPAX5 is direct; see citations above.) (franchino2024sustainedoma1mediatedintegrated pages 1-2, franchino2024sustainedoma1mediatedintegrated pages 10-13).

---

## 5. Environmental information
No specific environmental toxic, infectious, or lifestyle contributors were identified in the retrieved evidence for genetically defined spastic ataxias; the evidence base here is primarily neurogenetic.

---

## 6. Mechanism / pathophysiology (causal chains)

### 6.1 SPAX5 (AFG3L2) causal chain (primary mechanistic evidence)
**Trigger:** biallelic AFG3L2 loss-of-function (SPAX5) → **mitochondrial proteotoxicity** (accumulation of mitochondria-encoded proteins) → **OMA1 overactivation** → downstream signaling via **DELE1–HRI** → **ISR activation** (P-eIF2α/ATF4 and downstream targets) → neuronal dysfunction and cerebellar pathology; ISR potentiation can be protective in model systems (franchino2024sustainedoma1mediatedintegrated pages 1-2, franchino2024sustainedoma1mediatedintegrated pages 10-13).

### 6.2 ARSACS/SPAX white matter involvement (2024 PROSPAX dMRI)
In a multicenter diffusion-MRI study of paradigmatic SPAX forms, **ARSACS** demonstrated **severe white matter involvement** (reduced WM volume and broad microstructural metric changes), while **SPG7** showed only mild mean microstructural damage vs controls (scaravilli2024anmrievaluation pages 1-2). In ARSACS, microstructural damage correlated with **SARA** (ataxia severity) (scaravilli2024anmrievaluation pages 1-2).

---

## 7. Anatomical structures affected

### 7.1 Organ/system level
* **Central nervous system**: cerebellum and long motor pathways (pyramidal tracts) are implicated by the defining phenotype and neuroimaging/neuropathologic framing of HSP/SPAX conditions (scaravilli2024anmrievaluation pages 1-2, damiani2024pluripotentstemcells pages 14-15).

### 7.2 Tissue/cell level (suggested)
* **Purkinje neurons** (cerebellar cortex) are directly studied as a vulnerable neuronal type in SPAX5 Afg3l2−/− models; Sephin‑1 improved survival/arborization ex vivo (franchino2024sustainedoma1mediatedintegrated pages 10-13).

Suggested CL term: Purkinje cell (**CL:0000121**).

### 7.3 Subcellular localization
* **Mitochondrial inner membrane**: AFG3L2 is an inner mitochondrial membrane protease; AFG3L2 loss triggers OMA1/OPA1-related mitochondrial dynamics changes (franchino2024sustainedoma1mediatedintegrated pages 1-2, franchino2024sustainedoma1mediatedintegrated pages 10-13).

Suggested GO CC terms: mitochondrion (**GO:0005739**), mitochondrial inner membrane (**GO:0005743**).

---

## 8. Temporal development

### 8.1 Onset
* **SPAX3/ARSAL (MARS2):** onset reported **2–59 years** (bot2012reviewingthegenetic pages 4-5).
* **ARSACS:** typically **childhood/early-onset**; case example onset at **age 2** with slow progression (argenziano2024vestibularhypofunctionin pages 1-3).
* **WES family series (Pakistan):** onset range **1–14 years** (mean 6.23) across families with HSP/HCA phenotypes (azeem2024investigatingthegenetic pages 4-5).

### 8.2 Progression
Available evidence indicates progressive neurodegeneration for many spastic ataxia entities, but detailed stage models and longitudinal rates were not captured in the retrieved excerpts.

---

## 9. Inheritance and population

### 9.1 Inheritance
* Many SPAX entities are **autosomal recessive**, including SPAX3 (MARS2), SPAX4 (MTPAP), SPAX5 (AFG3L2), ARSACS (SACS), and typical SPG7 spastic-ataxia presentations (bot2012reviewingthegenetic pages 4-5, bot2012reviewingthegenetic pages 5-6, NCT06261424 chunk 1).
* SPAX1 is described as **autosomal dominant locus** in Newfoundland families (bot2012reviewingthegenetic pages 4-5).

### 9.2 Epidemiology
Disease-specific prevalence/incidence were not identified in the retrieved evidence for the nonstandard label. However, for HSP with movement disorders, an IPD meta-analysis aggregated **1,413** HSP cases across 192 manuscripts (fereshtehnejad2023movementdisordersin pages 1-2).

---

## 10. Diagnostics

### 10.1 Clinical and imaging
* **Diffusion MRI** can quantify white matter macro/microstructural involvement in SPAX; PROSPAX used harmonized 3T dMRI and found marked WM abnormalities in ARSACS compared to SPG7 and controls (scaravilli2024anmrievaluation pages 1-2, scaravilli2024anmrievaluation pages 2-4).
* **Vestibular testing (vHIT)** may uncover vestibular hypofunction in ARSACS and can complicate differential diagnosis with CANVAS (argenziano2024vestibularhypofunctionin pages 1-3, argenziano2024vestibularhypofunctionin pages 3-4).

### 10.2 Genetic testing (real-world implementation)
* In a Pakistani cohort study, **WES + segregation testing** achieved a genetic diagnosis in **62.5%** of families with hereditary spastic paraplegia / cerebellar ataxia phenotypes (azeem2024investigatingthegenetic pages 4-5).
* In a specialized “CoQ10 deficiency” referral cohort of undiagnosed cerebellar ataxia, **WES** identified a definite genetic etiology in **8/16 (50%)**, including **SPG7** among identified genes (monfrini2023wholeexomesequencingstudy pages 1-2).

---

## 11. Outcomes / prognosis
The retrieved evidence does not provide disease-specific survival or life expectancy for the umbrella SPAX phenotype. For SPAX5, a severe mouse model (Afg3l2−/−) shows early lethality that can be modestly improved with Sephin‑1, but extrapolation to human prognosis is not established (franchino2024sustainedoma1mediatedintegrated pages 10-13).

---

## 12. Treatment

### 12.1 Disease-modifying / mechanism-based (emerging)
**SPAX5 (preclinical):** ISR potentiation with **Sephin‑1** improved growth and mitochondrial measures in SPAX5 fibroblasts and improved Purkinje neuron survival/arborization ex vivo; in vivo it improved mitochondrial ultrastructure/ATP and extended survival in Afg3l2−/− mice (franchino2024sustainedoma1mediatedintegrated pages 10-13). This is preclinical and not yet a standard human therapy.

### 12.2 Symptomatic and rehabilitative care (current applications)
**Clinical trial implementation (2024–ongoing):** ClinicalTrials.gov **NCT06261424** (Laval University) is a multicenter, randomized, rater-blinded trial of a 12‑week supervised rehabilitation program (**IMPACT**) for genetically confirmed **ARSACS** and **SPG7**, enrolling ~84 participants, with primary endpoint **SARA** over a 64‑week timeframe; start date listed as **2024-02-01** (NCT06261424 chunk 1, NCT06261424 chunk 2). This represents a real-world implementation of structured rehabilitation for spastic ataxias.

### 12.3 Treatable mimics / targeted metabolic supplementation (selected patients)
**CoQ10 supplementation rationale:** In a 2023 Neurology Genetics study of patients referred for suspected CoQ10 deficiency, authors emphasize that diagnosing CoQ10 deficiency matters because patients may respond to **CoQ10 supplementation**, and they hypothesize a link between **SPG7 mutations and secondary CoQ10 deficiency** when CoQ10 was significantly decreased in SPG7 patient fibroblasts (monfrini2023wholeexomesequencingstudy pages 5-6, monfrini2023wholeexomesequencingstudy pages 1-2).

### 12.4 Suggested MAXO terms (examples)
* Physical therapy / rehabilitation program
* Genetic testing (WES/WGS)
* Coenzyme Q10 supplementation
* Deep brain stimulation (DBS) for selected movement-disorder phenotypes (not SPAX-specific, but reported as beneficial in VPS13D tremor and in selected HSP dystonia contexts; not fully extracted here)

---

## 13. Prevention
No primary prevention strategies were identified for Mendelian spastic ataxias beyond **genetic counseling** and family-based testing in appropriate settings.

---

## 14. Other species / natural disease
Not identified in the retrieved evidence.

---

## 15. Model organisms / experimental models
* **SPAX5:** Afg3l2−/− mice, primary Purkinje neuron cultures, and patient-derived fibroblasts are used to study disease mechanisms and test therapeutic hypotheses (Sephin‑1) (franchino2024sustainedoma1mediatedintegrated pages 10-13).
* **SPG7/HSP:** patient-derived iPSC neuronal models are described as platforms to reproduce mitochondrial phenotypes and to support drug discovery/repurposing (damiani2024pluripotentstemcells pages 14-15).

---

## Expert opinions and analysis (authoritative, evidence-backed)
1. **Phenotype-first framing:** Contemporary imaging work explicitly treats “SPAX” as a phenotype: “presence of cerebellar ataxia along with spasticity and other pyramidal features,” supporting use of phenotype-level diagnostic reasoning before gene resolution (scaravilli2024anmrievaluation pages 1-2).
2. **Diagnostic utility of genotype–phenotype patterns:** The 2023 IPD meta-analysis concludes that genotype–phenotype differences (e.g., SPG7’s association with ataxia and adult onset vs SPG11’s association with neuropathy/cognitive dysfunction) are clinically useful and “can possibly facilitate diagnosis in resource-limited settings” (fereshtehnejad2023movementdisordersin pages 1-2).
3. **Mechanism-informed therapy direction:** The 2024 Brain SPAX5 study argues that pharmacologic tuning of the integrated stress response is a plausible future therapeutic strategy for mitochondrial-proteostasis-driven cerebellar disorders (franchino2024sustainedoma1mediatedintegrated pages 10-13).

---

## Evidence gaps and limitations (for knowledge-base curation)
* The user-provided disease name is not standardized in the evidence retrieved; the safest approach is to **curate the entry as a phenotype umbrella** (SPAX) with **linked gene-defined child entities** (ARSACS, SPG7, SPAX3/4/5, etc.).
* MONDO/Orphanet/ICD/MeSH identifiers were not captured in the retrieved context; they should be added by direct lookup once the intended gene-defined entity is confirmed.
* Many phenotype frequencies (percent affected) and long-term prognosis measures are gene- and cohort-dependent and were not available in the excerpts retrieved here.


References

1. (bot2012reviewingthegenetic pages 4-5): Susanne T. de Bot, Michel A.A.P. Willemsen, Sascha Vermeer, Hubertus P.H. Kremer, and Bart P.C. van de Warrenburg. Reviewing the genetic causes of spastic-ataxias. Neurology, 79:1507-1514, Oct 2012. URL: https://doi.org/10.1212/wnl.0b013e31826d5fb0, doi:10.1212/wnl.0b013e31826d5fb0. This article has 90 citations and is from a highest quality peer-reviewed journal.

2. (scaravilli2024anmrievaluation pages 1-2): Alessandra Scaravilli, Ilaria Gabusi, Gaia Mari, Matteo Battocchio, Sara Bosticardo, Simona Schiavi, Benjamin Bender, Christoph Kessler, Bernard Brais, Roberta La Piana, Bart P. van de Warrenburg, Mirco Cosottini, Dagmar Timmann, Alessandro Daducci, Rebecca Schüle, Matthis Synofzik, Filippo Maria Santorelli, and Sirio Cocozza. An mri evaluation of white matter involvement in paradigmatic forms of spastic ataxia: results from the multi-center prospax study. Journal of Neurology, 271:5468-5477, Jun 2024. URL: https://doi.org/10.1007/s00415-024-12505-y, doi:10.1007/s00415-024-12505-y. This article has 4 citations and is from a domain leading peer-reviewed journal.

3. (scaravilli2024anmrievaluation pages 2-4): Alessandra Scaravilli, Ilaria Gabusi, Gaia Mari, Matteo Battocchio, Sara Bosticardo, Simona Schiavi, Benjamin Bender, Christoph Kessler, Bernard Brais, Roberta La Piana, Bart P. van de Warrenburg, Mirco Cosottini, Dagmar Timmann, Alessandro Daducci, Rebecca Schüle, Matthis Synofzik, Filippo Maria Santorelli, and Sirio Cocozza. An mri evaluation of white matter involvement in paradigmatic forms of spastic ataxia: results from the multi-center prospax study. Journal of Neurology, 271:5468-5477, Jun 2024. URL: https://doi.org/10.1007/s00415-024-12505-y, doi:10.1007/s00415-024-12505-y. This article has 4 citations and is from a domain leading peer-reviewed journal.

4. (NCT06261424 chunk 1): Elise Duchesne. Effects of a Supervised Rehabilitation Program on Disease Severity in Spastic Ataxias. Laval University. 2024. ClinicalTrials.gov Identifier: NCT06261424

5. (bot2012reviewingthegenetic pages 5-6): Susanne T. de Bot, Michel A.A.P. Willemsen, Sascha Vermeer, Hubertus P.H. Kremer, and Bart P.C. van de Warrenburg. Reviewing the genetic causes of spastic-ataxias. Neurology, 79:1507-1514, Oct 2012. URL: https://doi.org/10.1212/wnl.0b013e31826d5fb0, doi:10.1212/wnl.0b013e31826d5fb0. This article has 90 citations and is from a highest quality peer-reviewed journal.

6. (franchino2024sustainedoma1mediatedintegrated pages 1-2): Camilla Aurora Franchino, Martina Brughera, Valentina Baderna, Daniele De Ritis, Alessandra Rocco, Sara Seneca, Luc Regal, Paola Podini, Maurizio D’Antonio, Camilo Toro, Angelo Quattrini, Emmanuel Scalais, and Francesca Maltecca. Sustained oma1-mediated integrated stress response is beneficial for spastic ataxia type 5. Brain, 147:1043-1056, Oct 2024. URL: https://doi.org/10.1093/brain/awad340, doi:10.1093/brain/awad340. This article has 17 citations and is from a highest quality peer-reviewed journal.

7. (franchino2024sustainedoma1mediatedintegrated pages 10-13): Camilla Aurora Franchino, Martina Brughera, Valentina Baderna, Daniele De Ritis, Alessandra Rocco, Sara Seneca, Luc Regal, Paola Podini, Maurizio D’Antonio, Camilo Toro, Angelo Quattrini, Emmanuel Scalais, and Francesca Maltecca. Sustained oma1-mediated integrated stress response is beneficial for spastic ataxia type 5. Brain, 147:1043-1056, Oct 2024. URL: https://doi.org/10.1093/brain/awad340, doi:10.1093/brain/awad340. This article has 17 citations and is from a highest quality peer-reviewed journal.

8. (argenziano2024vestibularhypofunctionin pages 1-3): Giacomo Argenziano, Francesco Cavallieri, Andrea Castellucci, Valentina Fioravanti, Giulia Di Rauso, Annalisa Gessani, Isabella Campanini, Andrea Merlo, Manuela Napoli, Sara Grisanti, Jessica Rossi, Giulia Toschi, Chiara Zini, Angelo Ghidini, and Franco Valzania. Vestibular hypofunction in arsacs syndrome: a possible pitfall in the differential diagnosis of recessive cerebellar and afferent ataxias. Neurology. Clinical practice, 14 1:e200239, Feb 2024. URL: https://doi.org/10.1212/cpj.0000000000200239, doi:10.1212/cpj.0000000000200239. This article has 1 citations.

9. (fereshtehnejad2023movementdisordersin pages 1-2): Seyed-Mohammad Fereshtehnejad, Philip A. Saleh, Lais M. Oliveira, Neha Patel, Suvorit Bhowmick, Gerard Saranza, and Lorraine V. Kalia. Movement disorders in hereditary spastic paraplegia (hsp): a systematic review and individual participant data meta-analysis. Neurological Sciences, 44:947-959, Nov 2023. URL: https://doi.org/10.1007/s10072-022-06516-8, doi:10.1007/s10072-022-06516-8. This article has 17 citations and is from a peer-reviewed journal.

10. (damiani2024pluripotentstemcells pages 14-15): Devid Damiani, Matteo Baggiani, Stefania Della Vecchia, Valentina Naef, and Filippo Maria Santorelli. Pluripotent stem cells as a preclinical cellular model for studying hereditary spastic paraplegias. International Journal of Molecular Sciences, 25:2615, Feb 2024. URL: https://doi.org/10.3390/ijms25052615, doi:10.3390/ijms25052615. This article has 10 citations.

11. (azeem2024investigatingthegenetic pages 4-5): Arfa Azeem, Asif Naveed Ahmed, Niamat Khan, Nikol Voutsina, Irfan Ullah, Nishanka Ubeyratna, Muhammad Yasin, Emma L. Baple, Andrew H. Crosby, Lettie E. Rawlins, and Shamim Saleha. Investigating the genetic basis of hereditary spastic paraplegia and cerebellar ataxia in pakistani families. BMC Neurology, Sep 2024. URL: https://doi.org/10.1186/s12883-024-03855-1, doi:10.1186/s12883-024-03855-1. This article has 3 citations and is from a peer-reviewed journal.

12. (argenziano2024vestibularhypofunctionin pages 3-4): Giacomo Argenziano, Francesco Cavallieri, Andrea Castellucci, Valentina Fioravanti, Giulia Di Rauso, Annalisa Gessani, Isabella Campanini, Andrea Merlo, Manuela Napoli, Sara Grisanti, Jessica Rossi, Giulia Toschi, Chiara Zini, Angelo Ghidini, and Franco Valzania. Vestibular hypofunction in arsacs syndrome: a possible pitfall in the differential diagnosis of recessive cerebellar and afferent ataxias. Neurology. Clinical practice, 14 1:e200239, Feb 2024. URL: https://doi.org/10.1212/cpj.0000000000200239, doi:10.1212/cpj.0000000000200239. This article has 1 citations.

13. (azeem2024investigatingthegenetic pages 1-2): Arfa Azeem, Asif Naveed Ahmed, Niamat Khan, Nikol Voutsina, Irfan Ullah, Nishanka Ubeyratna, Muhammad Yasin, Emma L. Baple, Andrew H. Crosby, Lettie E. Rawlins, and Shamim Saleha. Investigating the genetic basis of hereditary spastic paraplegia and cerebellar ataxia in pakistani families. BMC Neurology, Sep 2024. URL: https://doi.org/10.1186/s12883-024-03855-1, doi:10.1186/s12883-024-03855-1. This article has 3 citations and is from a peer-reviewed journal.

14. (monfrini2023wholeexomesequencingstudy pages 1-2): Edoardo Monfrini, Alba Pesini, Fabio Biella, Claudia F.R. Sobreira, Valentina Emmanuele, Gloria Brescia, Luis Carlos Lopez, Saba Tadesse, Michio Hirano, Giacomo P. Comi, Catarina Maria Quinzii, and Alessio Di Fonzo. Whole-exome sequencing study of fibroblasts derived from patients with cerebellar ataxia referred to investigate coq10 deficiency. Neurology Genetics, Apr 2023. URL: https://doi.org/10.1212/nxg.0000000000200058, doi:10.1212/nxg.0000000000200058. This article has 3 citations.

15. (NCT06261424 chunk 2): Elise Duchesne. Effects of a Supervised Rehabilitation Program on Disease Severity in Spastic Ataxias. Laval University. 2024. ClinicalTrials.gov Identifier: NCT06261424

16. (monfrini2023wholeexomesequencingstudy pages 5-6): Edoardo Monfrini, Alba Pesini, Fabio Biella, Claudia F.R. Sobreira, Valentina Emmanuele, Gloria Brescia, Luis Carlos Lopez, Saba Tadesse, Michio Hirano, Giacomo P. Comi, Catarina Maria Quinzii, and Alessio Di Fonzo. Whole-exome sequencing study of fibroblasts derived from patients with cerebellar ataxia referred to investigate coq10 deficiency. Neurology Genetics, Apr 2023. URL: https://doi.org/10.1212/nxg.0000000000200058, doi:10.1212/nxg.0000000000200058. This article has 3 citations.