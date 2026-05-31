---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T07:24:59.049043'
end_time: '2026-05-10T07:45:29.769680'
duration_seconds: 1230.72
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Okur-Chung Neurodevelopmental Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 43
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Okur-Chung Neurodevelopmental Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Okur-Chung Neurodevelopmental Syndrome** covering all of the
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
- **Disease Name:** Okur-Chung Neurodevelopmental Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Okur-Chung Neurodevelopmental Syndrome** covering all of the
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


## Comprehensive Disease Characteristics Report: Okur-Chung Neurodevelopmental Syndrome (OCNDS)

### Target disease
Okur-Chung neurodevelopmental syndrome (OCNDS) is an ultra-rare, predominantly pediatric-onset neurodevelopmental disorder characterized by global developmental delay (language disproportionately affected), mild-to-moderate intellectual disability, hypotonia, behavioral differences (including autism spectrum disorder), variable dysmorphic features, and multisystem involvement including growth impairment, sleep/circadian disruption, seizures/epilepsy in a subset, and occasional congenital anomalies (notably cardiac). (chung2022okurchungneurodevelopmentalsyndrome pages 1-3, chung2022okurchungneurodevelopmentalsyndrome pages 3-6, rushing2024patientorganizationperspective pages 1-2)

A 2024 patient-organization perspective summarizes: “Okur-Chung neurodevelopmental syndrome (OCNDS) is an ultra-rare disorder caused by variants in the CSNK2A1 gene… studies suggest a loss of function or altered substrate specificity. There are no approved treatments for OCNDS, and current treatments focus on symptom management… [and] in ~25% of cases, epilepsy.” (Therapeutic Advances in Rare Disease; received 2023-12-26; accepted 2024-04-05; published 2024-01; https://doi.org/10.1177/26330040241249763) (rushing2024patientorganizationperspective pages 1-2)

### Core identifiers and nomenclature
| Disease name | Synonyms / alternative names | OMIM disease number | Causal gene | OMIM gene number | MONDO ID | Key references (publication date; URL) |
|---|---|---|---|---|---|---|
| Okur-Chung neurodevelopmental syndrome | OCNDS; CSNK2A1-Related Neurodevelopmental Syndrome (blanc2024patientwitha pages 1-2, chung2022okurchungneurodevelopmentalsyndrome pages 1-3) | OMIM #617062 (blanc2024patientwitha pages 1-2, chung2022okurchungneurodevelopmentalsyndrome pages 1-3) | CSNK2A1 (casein kinase II subunit alpha / casein kinase 2 alpha 1) (blanc2024patientwitha pages 1-2, chung2022okurchungneurodevelopmentalsyndrome pages 1-3) | OMIM *115440 (blanc2024patientwitha pages 1-2) | MONDO:0014893 / MONDO_0014893 (OpenTargets Search: Okur-Chung neurodevelopmental syndrome-CSNK2A1) | GeneReviews: *Okur-Chung Neurodevelopmental Syndrome* (created 2022-06-09), https://www.ncbi.nlm.nih.gov/books/ (chung2022okurchungneurodevelopmentalsyndrome pages 1-3); Blanc et al., *Patient with a heterozygous pathogenic variant in CSNK2A1 gene: A new case to update the Okur–Chung neurodevelopmental syndrome* (2024-05), https://doi.org/10.1002/ajmg.a.63642 (blanc2024patientwitha pages 1-2); OpenTargets disease-target association entry for Okur-Chung neurodevelopmental syndrome / CSNK2A1, https://platform.opentargets.org/ (OpenTargets Search: Okur-Chung neurodevelopmental syndrome-CSNK2A1) |


*Table: This table summarizes the core nomenclature and database identifiers for Okur-Chung neurodevelopmental syndrome, including OMIM, MONDO, and the causal gene. It is useful as a standardized reference for disease knowledge base curation and cross-database mapping.*

**Notes on missing identifiers:** ICD-10/ICD-11, Orphanet (ORPHA), and MeSH identifiers were not present in the retrieved full texts; only OMIM, MONDO, and the GeneReviews entry were directly available in this tool run. (chung2022okurchungneurodevelopmentalsyndrome pages 1-3, OpenTargets Search: Okur-Chung neurodevelopmental syndrome-CSNK2A1)

---

## 1. Disease Information

### What is the disease? (concise overview)
OCNDS is a Mendelian neurodevelopmental syndrome caused by heterozygous pathogenic variants in **CSNK2A1** (encoding the catalytic α subunit of protein kinase CK2). It is typically de novo but can be inherited in an autosomal dominant pattern. Clinical diagnosis is supported by characteristic neurodevelopmental features, but the definitive diagnosis requires molecular genetic testing demonstrating a heterozygous pathogenic/likely pathogenic CSNK2A1 variant. (chung2022okurchungneurodevelopmentalsyndrome pages 1-3, belnap2023inheritedcsnk2a1variants pages 1-2)

### Synonyms
GeneReviews explicitly lists the synonym “CSNK2A1-Related Neurodevelopmental Syndrome.” (chung2022okurchungneurodevelopmentalsyndrome pages 1-3)

### Evidence source type
Most current clinical knowledge is derived from aggregated literature (GeneReviews synthesis of published cases) supplemented by individual case reports, family series, and patient-registry/family-survey data (CSNK2A1 Foundation, Simons Searchlight). (chung2022okurchungneurodevelopmentalsyndrome pages 1-3, belnap2023inheritedcsnk2a1variants pages 1-2, rushing2024patientorganizationperspective pages 1-2)

---

## 2. Etiology

### Disease causal factors
**Primary causal factor:** Germline **heterozygous pathogenic variants in CSNK2A1** (casein kinase 2 alpha 1), affecting CK2 function in neural development and other cellular processes. (chung2022okurchungneurodevelopmentalsyndrome pages 1-3, rushing2024patientorganizationperspective pages 1-2)

### Risk factors
For OCNDS (a monogenic disorder), “risk factors” are primarily genetic:
- **De novo CSNK2A1 variants** account for most probands. (chung2022okurchungneurodevelopmentalsyndrome pages 1-3, rushing2024patientorganizationperspective pages 2-4)
- **Familial (inherited) CSNK2A1 variants** are now documented, shifting counseling from a purely de novo paradigm. (belnap2023inheritedcsnk2a1variants pages 1-2, nan2024okur‐chungneurodevelopmentalsyndrome pages 1-2)

No environmental or infectious risk factors were identified in the retrieved evidence.

### Protective factors / gene–environment interaction
No genetic protective alleles, protective environmental factors, or gene–environment interactions were identified in the retrieved evidence.

---

## 3. Phenotypes

### Phenotype spectrum with frequency/statistics (and HPO suggestions)
| Clinical feature / developmental metric | Frequency / statistic | Cohort / source note | Suggested HPO term(s) | Citation |
|---|---:|---|---|---|
| Developmental delay / intellectual disability | 35/35 (100%) with developmental delay / ID; ID reported in about three quarters overall | GeneReviews Table 2 summarized from 36 clinically described individuals; language generally more affected than gross motor | HP:0001263 Developmental delay; HP:0001249 Intellectual disability | (chung2022okurchungneurodevelopmentalsyndrome pages 3-6, chung2022okurchungneurodevelopmentalsyndrome pages 1-3) |
| Dysmorphic facial features | 29/36 (80.6%) | Often round face and short, broad nasal tip; nonspecific facial dysmorphism | HP:0001999 Facial dysmorphism; HP:0000311 Round face; HP:0012805 Broad nose | (chung2022okurchungneurodevelopmentalsyndrome pages 3-6) |
| Behavioral issues | 27/36 (75.0%) | Includes stereotypies, autism spectrum disorder, tantrums/aggression, ADHD | HP:0000729 Autistic behavior; HP:0000733 Stereotypy; HP:0007018 Attention deficit hyperactivity disorder | (chung2022okurchungneurodevelopmentalsyndrome pages 3-6) |
| Hypotonia | 22/36 (61.1%); described as about two thirds | Usually mild, beginning in infancy/childhood | HP:0001252 Muscular hypotonia | (chung2022okurchungneurodevelopmentalsyndrome pages 3-6) |
| Brain MRI abnormalities | 11/20 (55.0%) | Nonspecific; examples include delayed myelination, thin corpus callosum, small anterior pituitary | HP:0012444 Abnormal brain MRI; HP:0001273 Corpus callosum hypoplasia; HP:0012447 Delayed myelination | (chung2022okurchungneurodevelopmentalsyndrome pages 3-6) |
| Musculoskeletal findings | 15/36 (41.7%) | Kyphoscoliosis, loose joints, hernia | HP:0002650 Scoliosis; HP:0001382 Joint hypermobility; HP:0001537 Umbilical hernia | (chung2022okurchungneurodevelopmentalsyndrome pages 3-6) |
| Feeding difficulties | 14/36 (38.9%) | From infancy to childhood; can include poor suck / difficulty with solids | HP:0011968 Feeding difficulties; HP:0002033 Dysphagia | (chung2022okurchungneurodevelopmentalsyndrome pages 3-6) |
| Postnatal short stature | 14/36 (38.9%) | Generally 2–3 SD below mean | HP:0004322 Short stature | (chung2022okurchungneurodevelopmentalsyndrome pages 3-6) |
| Difficulty gaining weight / failure to thrive | 13/36 (36.1%) | Growth impairment common | HP:0001508 Failure to thrive; HP:0002028 Poor weight gain | (chung2022okurchungneurodevelopmentalsyndrome pages 3-6) |
| Sleep issues | 13/36 (36.1%) in GeneReviews cohort; 77% families reporting sleep-related disruptions in 2022 Simons Searchlight survey | Likely related to disrupted circadian rhythm; family-reported burden may exceed literature-derived frequency | HP:0002360 Sleep disturbance; HP:0002363 Circadian rhythm sleep disorder | (chung2022okurchungneurodevelopmentalsyndrome pages 3-6, rushing2024patientorganizationperspective pages 2-4, rushing2024patientorganizationperspective pages 1-2) |
| Microcephaly / smaller head size | 12/36 (33.3%) | Usually postnatal or relative; congenital microcephaly uncommon | HP:0000252 Microcephaly | (chung2022okurchungneurodevelopmentalsyndrome pages 3-6) |
| Seizures / epilepsy | 11/36 (30.6%) in GeneReviews cohort; approximately 25% in 2024 overview | Seizure prevalence may be underreported; some events may occur during sleep | HP:0001250 Seizure; HP:0001251 Ataxia if associated neurologic issues present | (chung2022okurchungneurodevelopmentalsyndrome pages 3-6, rushing2024patientorganizationperspective pages 2-4, rushing2024patientorganizationperspective pages 1-2) |
| Ataxia / gait difficulties / poor coordination | 9/36 (25.0%) | Variable motor coordination deficits | HP:0001251 Ataxia; HP:0001288 Gait disturbance; HP:0002370 Poor coordination | (chung2022okurchungneurodevelopmentalsyndrome pages 3-6) |
| Autism spectrum disorder | ~1/4 affected individuals | Subset of behavioral phenotype | HP:0000729 Autistic behavior | (chung2022okurchungneurodevelopmentalsyndrome pages 3-6) |
| Stereotypic movements | ~1/3 affected individuals | Common behavioral manifestation | HP:0000733 Stereotypy | (chung2022okurchungneurodevelopmentalsyndrome pages 3-6) |
| ADHD | ~1/5 affected individuals | Attention and hyperactivity phenotype | HP:0007018 Attention deficit hyperactivity disorder | (chung2022okurchungneurodevelopmentalsyndrome pages 3-6) |
| Congenital heart abnormalities | About one-third in Blanc review; atrial septal defect reported in 3 unrelated individuals in GeneReviews | Cardiac involvement is variable and not universal | HP:0001627 Abnormality of the cardiovascular system; HP:0001631 Atrial septal defect | (blanc2024patientwitha pages 4-5, chung2022okurchungneurodevelopmentalsyndrome pages 3-6) |
| Average age: sitting independently | 11 months | Early developmental milestone average | HP:0001270 Delayed ability to sit | (chung2022okurchungneurodevelopmentalsyndrome pages 3-6) |
| Average age: walking independently | 28.8 months | Gross motor milestone average | HP:0001270 Motor delay; HP:0001288 Gait disturbance | (chung2022okurchungneurodevelopmentalsyndrome pages 3-6) |
| Average age: first meaningful words | 38.3 months | Language milestone average; language more impaired than gross motor | HP:0000750 Delayed speech and language development | (chung2022okurchungneurodevelopmentalsyndrome pages 3-6) |


*Table: This table summarizes the most consistently reported clinical features and developmental milestones for Okur-Chung neurodevelopmental syndrome, integrating GeneReviews 2022 frequency data with newer 2024 patient-organization survey statistics for sleep and seizure burden. It is useful for phenotype curation, HPO mapping, and quick comparison of literature-based versus family-reported symptom prevalence.*

### Additional 2023–2024 phenotype expansion highlights
- A 2024 case report (AJMG-A) notes that **“congenital heart abnormalities have been reported in about one-third of patients”** in the literature it reviewed. (Published 2024-05; https://doi.org/10.1002/ajmg.a.63642) (blanc2024patientwitha pages 4-5)
- The 2024 roadmap/perspective emphasizes that seizures may be **under-ascertained**, noting that EEG notes and parent reports suggest nocturnal epileptiform activity and that extended EEG recordings may be lacking. (rushing2024patientorganizationperspective pages 2-4, rushing2024patientorganizationperspective pages 1-2)

### Quality of life impact
Direct standardized QoL instruments (e.g., EQ-5D, SF-36, PROMIS) were not reported in the retrieved texts. However, a 2022 Simons Searchlight family survey (summarized in 2024) ranked the top reported issues as: (1) intellectual disability/developmental delay, (2) language delay/inability to speak, and (3) sleep issues, with **“77% of families reporting sleep-related disruptions.”** (rushing2024patientorganizationperspective pages 2-4)

---

## 4. Genetic / Molecular Information

### Causal gene
- **CSNK2A1** encodes CK2α, a serine/threonine kinase catalytic subunit. (rushing2024patientorganizationperspective pages 1-2, chung2022okurchungneurodevelopmentalsyndrome pages 1-3)

### Inheritance
- Typically **autosomal dominant**, usually de novo; rare inherited cases and low-level parental mosaicism are described. (chung2022okurchungneurodevelopmentalsyndrome pages 1-3, belnap2023inheritedcsnk2a1variants pages 1-2)

### Variant spectrum (representative) and mechanistic interpretations
| Variant / class | Evidence type | Inheritance | Key phenotype / cohort note | Molecular / mechanistic interpretation | ACMG / classification note | Publication date | URL | Citation |
|---|---|---|---|---|---|---|---|---|
| p.Lys198Arg (K198R), recurrent missense | Familial clinical series; also noted as the most frequently reported de novo pathogenic variant | Both inherited and previously reported de novo | In 3 families with inherited OCNDS, common manifestations across 8 individuals included DD/ID (8/8), speech delay (7/8), behavioral problems (4/8), hypotonia (3/8), dysmorphic facial features (5/8); marked inter- and intra-familial variability | Not consistent with simple loss of function; K198R causes a “rewiring” of CK2 specificity with decreased +1 acidic preference, decreased threonine phosphorylation, increased tyrosine phosphorylation, and altered tyrosine motif preference | Not specified in retrieved familial/mechanistic excerpts | 2023-07; 2022-04 | https://doi.org/10.1111/cge.14408; https://doi.org/10.3389/fmolb.2022.850661 | (belnap2023inheritedcsnk2a1variants pages 1-2, belnap2023inheritedcsnk2a1variants pages 2-2, caefer2022theokurchungneurodevelopmental pages 1-2) |
| p.Glu27Lys, missense | Familial clinical series | Inherited (maternal transmission) | Reported in Family 3 with two affected sons; supports preserved fertility and autosomal dominant transmission in OCNDS | No variant-specific biochemical assay in retrieved evidence; supports variable expressivity rather than obligate severe de novo-only disease | Not specified in retrieved excerpt | 2023-07 | https://doi.org/10.1111/cge.14408 | (belnap2023inheritedcsnk2a1variants pages 1-2, belnap2023inheritedcsnk2a1variants pages 2-2) |
| p.Arg47Gln, missense | Case report with literature review | Heterozygous pathogenic variant; inheritance not specified in retrieved excerpt | Patient had DD, ID, generalized hypotonia, speech delay, short stature, microcephaly, dysmorphic features; lacked sleep disturbance, seizures, and gait difficulty | Falls in/near ATP/GTP-binding loop region implicated in broader phenotypic range; ATP/GTP-loop variants are reported to cause the widest range of phenotypes | Described as pathogenic in case report context; no ACMG criteria quoted in retrieved excerpt | 2024-05 | https://doi.org/10.1002/ajmg.a.63642 | (blanc2024patientwitha pages 1-2, blanc2024patientwitha pages 4-5, blanc2024patientwitha pages 4-4) |
| p.Met381GlyfsTer32, frameshift | Turkish case report | De novo | Hypotonia, developmental delay, dysmorphic features, abnormal MRI with mildly underdeveloped myelination and ventricular changes | First reported OCNDS-associated frameshift in retrieved evidence; predicted elongated C-terminal mutant protein may be nonfunctional and may disrupt CK2α interactions/depolymerization | Classified as likely pathogenic under ACMG-2015; PS2 and PM2 explicitly noted | 2024-05 (online first 2023-05-26) | https://doi.org/10.1159/000530585 | (zhuri2024acaseof pages 3-6, zhuri2024acaseof pages 1-3, zhuri2024acaseof pages 6-7) |
| p.Tyr323Leufs*16, truncating frameshift | Familial Chinese case report with RNA studies | Inherited (proband and mother) | Proband had recurrent generalized tonic-clonic seizures, language impairment, ID; mother had postnatal hernias, splenomegaly, infection predisposition, but no major DD/ID, illustrating variable expressivity | Transcript with frameshift variant was not detected and total CSNK2A1 product was reduced by ~50%, supporting nonsense-mediated decay and haploinsufficiency; authors suggest null variants may produce milder phenotypes than missense variants | No ACMG wording quoted in retrieved excerpt | 2024-03 | https://doi.org/10.1002/mgg3.2398 | (nan2024okur‐chungneurodevelopmentalsyndrome pages 1-2, nan2024okur‐chungneurodevelopmentalsyndrome pages 2-5) |
| p.Arg191Ter (R191X), truncating/nonsense | Zebrafish functional model | Experimental model (not patient inheritance) | Produced among the most severe and consistent zebrafish phenotypes, including enlarged head, reduced body size, yolk sac defects, and spinal curvature | Co-injection of wild-type CSNK2A1 mRNA significantly rescued R191X-induced abnormalities; together with CK2 inhibitor phenocopy, this supports CK2 dysfunction and is compatible with dominant-negative effects for some mutants | Not applicable | 2024-01-11 | https://doi.org/10.1101/2024.01.09.574075 | (hassett2024characterizingcsnk2a1mutantinduced pages 7-9, hassett2024characterizingcsnk2a1mutantinduced pages 1-4, hassett2024characterizingcsnk2a1mutantinduced pages 4-7) |
| p.Tyr50Cys (Y50C), missense | Human case report/review and zebrafish model | De novo in reported human case | Human OCNDS with DD/short stature/ID; in zebrafish, Y50C caused severe morphological abnormalities | Located in ATP/GTP-binding loop; structural analyses suggest impaired protein activation and destabilization of CK2 heterotetramer; wild-type co-injection attenuated zebrafish phenotype, again suggesting mutant interference with CK2 function in at least some contexts | Human case classified pathogenic by ACMG in 2025 review excerpt (PS2 + PS4_Moderate + PM2_Supporting + PP2 + PP3), but not from 2023-2024 sources | 2024-01-11; 2025-12 | https://doi.org/10.1101/2024.01.09.574075; https://doi.org/10.1002/mgg3.70166 | (hassett2024characterizingcsnk2a1mutantinduced pages 7-9, hassett2024characterizingcsnk2a1mutantinduced pages 4-7, li2025acaseof pages 1-2, li2025acaseof pages 3-4) |
| OCNDS-associated missense variants overall | Review / mechanistic synthesis | Mostly de novo, but inherited cases now established | Most OCNDS variants are missense and cluster in functional regions of the kinase domain; registry data reported 82 distinct variants and 22 deletions | Mechanisms are heterogeneous and likely variant-dependent: reduced activity for many variants, altered substrate specificity for K198R, haploinsufficiency/NMD for truncating alleles, and possible dominant-negative effects suggested by zebrafish rescue experiments and variant-specific localization differences | Variant-specific ACMG status varies; no single classification applies | 2024-01; 2022-04; 2024-03 | https://doi.org/10.1177/26330040241249763; https://doi.org/10.3389/fmolb.2022.850661; https://doi.org/10.1002/mgg3.2398 | (rushing2024patientorganizationperspective pages 2-4, rushing2024patientorganizationperspective pages 1-2, caefer2022theokurchungneurodevelopmental pages 1-2, nan2024okur‐chungneurodevelopmentalsyndrome pages 1-2) |


*Table: This table summarizes representative CSNK2A1 variants reported in Okur-Chung neurodevelopmental syndrome, their inheritance patterns, associated phenotypes, and currently supported molecular mechanisms. It is useful for linking specific variant classes to pathogenic models such as altered substrate specificity, haploinsufficiency, or possible dominant-negative effects.*

Key 2023–2024 updates:
- **Inherited OCNDS**: Belnap et al. (Clinical Genetics; accepted 2023-07-16; https://doi.org/10.1111/cge.14408) report three families with inherited CSNK2A1 variants, supporting preserved fertility and variable expressivity. (belnap2023inheritedcsnk2a1variants pages 1-2)
- **Frameshift/truncating alleles**: Nan et al. (Mol Genet Genomic Med; accepted 2024-01-31; https://doi.org/10.1002/mgg3.2398) present a familial frameshift with RNA evidence consistent with nonsense-mediated decay (NMD) and haploinsufficiency (∼50% decreased CSNK2A1 product). (nan2024okur‐chungneurodevelopmentalsyndrome pages 1-2, nan2024okur‐chungneurodevelopmentalsyndrome pages 2-5)
- **Frameshift case report**: Zhuri et al. (Molecular Syndromology; 2024-05; https://doi.org/10.1159/000530585) report a novel, de novo CSNK2A1 frameshift classified as likely pathogenic per ACMG criteria. (zhuri2024acaseof pages 1-3, zhuri2024acaseof pages 3-6)

### Modifier genes / epigenetics / chromosomal abnormalities
No validated modifier genes or disease-specific epigenetic signatures were identified in the retrieved evidence.

However, registry data indicate that **deletions** (structural variants) are present among individuals with OCNDS (recorded as “22 distinct deletions” in the CSNK2A1 Foundation registry). (rushing2024patientorganizationperspective pages 2-4)

---

## 5. Environmental Information
No specific environmental, lifestyle, or infectious contributors were reported for OCNDS in the retrieved evidence; OCNDS is best characterized as a Mendelian CSNK2A1-associated condition. (chung2022okurchungneurodevelopmentalsyndrome pages 1-3, rushing2024patientorganizationperspective pages 1-2)

---

## 6. Mechanism / Pathophysiology

### Current understanding (key concepts)
OCNDS pathophysiology is **variant-dependent**, with evidence supporting multiple (not mutually exclusive) molecular mechanisms:
- **Altered kinase substrate specificity (neomorphic/rewiring)**: For the common K198R variant, Caefer et al. report: “Contrary to prior speculation, the mutation does not result in a loss of function, but rather shifts the substrate specificity of the kinase,” including increased tyrosine phosphorylation preference and motif changes. (Frontiers in Molecular Biosciences; 2022-04; https://doi.org/10.3389/fmolb.2022.850661) (caefer2022theokurchungneurodevelopmental pages 1-2)
- **Loss-of-function / haploinsufficiency for truncating alleles**: Nan et al. report that in a familial frameshift, “the transcript with the frameshift variant was not detected” and there was “A ∼50% decrease in the CSNK2A1 product,” supporting NMD and haploinsufficiency. (Mol Genet Genomic Med; 2024-03; https://doi.org/10.1002/mgg3.2398) (nan2024okur‐chungneurodevelopmentalsyndrome pages 2-5, nan2024okur‐chungneurodevelopmentalsyndrome pages 1-2)
- **Dominant-negative or interference effects for some mutants**: Zebrafish mutant-expression phenotypes can be rescued by co-injection of wild-type CSNK2A1 mRNA; the authors interpret this as consistent with mutant interference with CK2 function. (bioRxiv; posted 2024-01-11; https://doi.org/10.1101/2024.01.09.574075) (hassett2024characterizingcsnk2a1mutantinduced pages 7-9, hassett2024characterizingcsnk2a1mutantinduced pages 4-7)

### Cilia biology as a mechanistic bridge (authoritative experimental evidence)
Loukil et al. provide cell-biological evidence connecting CSNK2A1 to ciliogenesis and showing that OCNDS-linked variants can cause ciliary defects:
- CSNK2A1 identified “as an important modulator of TTBK2 function in cilia trafficking.” (PNAS; 2021-04; https://doi.org/10.1073/pnas.2018740118) (loukil2021acomplexof pages 1-2)
- “CSNK2A1 is a centrosomal protein concentrated at the mother centriole and associated with the distal appendages.” (loukil2021acomplexof pages 1-2)
- “Overexpression of Csnk2a1 variants associated with OCNDS causes ciliary structural abnormalities.” (loukil2021acomplexof pages 1-2)

### Circadian rhythm / sleep disturbance
Sleep disturbance is common clinically and is often framed as circadian disruption. The 2024 roadmap/perspective connects CK2 to circadian regulation, noting CK2 modulates PER2 and that a Drosophila dominant-negative CK2 mutant induced marked circadian period lengthening (~33 h). (rushing2024patientorganizationperspective pages 2-4)

### Suggested ontology terms (mechanisms)
- **GO (biological process) suggestions**: protein phosphorylation (GO:0006468); regulation of protein phosphorylation (GO:0001932); cilium organization (GO:0044782); cilium assembly (GO:0060271); regulation of circadian rhythm (GO:0042752); synaptic signaling (GO:0099536); regulation of membrane potential (GO:0042391).
- **GO (cellular component) suggestions**: centrosome (GO:0005813); centriole (GO:0005814); cilium (GO:0005929).
- **CL (cell type) suggestions**: neurons (CL:0000540); glutamatergic neuron (CL:0000679); GABAergic neuron (CL:0000617).

---

## 7. Anatomical Structures Affected

### Organ/system level
The dominant affected system is the **nervous system** (neurodevelopmental delay/ID, seizures, hypotonia, behavior). Secondary involvement can include **growth/endocrine** issues (short stature; occasional partial growth hormone deficiency), **gastrointestinal/nutrition** (feeding difficulties), **musculoskeletal** (scoliosis/kyphosis, hypermobility, hernias), and occasionally **cardiovascular** congenital defects. (chung2022okurchungneurodevelopmentalsyndrome pages 3-6, chung2022okurchungneurodevelopmentalsyndrome pages 1-3, blanc2024patientwitha pages 4-5)

### Tissue/cell level and subcellular localization
Experimental and review evidence highlights CK2α abundance in brain and CSNK2A1 localization to centrosomal/distal appendage regions relevant to cilia. (rushing2024patientorganizationperspective pages 2-4, loukil2021acomplexof pages 1-2)

**UBERON suggestions** (non-exhaustive): brain (UBERON:0000955); cerebral cortex (UBERON:0000956); hippocampus (UBERON:0001954); heart (UBERON:0000948).

---

## 8. Temporal Development (onset and progression)

### Onset
Typically manifests in **infancy/early childhood** with hypotonia, feeding issues, speech and motor delay, and developmental delay. (chung2022okurchungneurodevelopmentalsyndrome pages 1-3, chung2022okurchungneurodevelopmentalsyndrome pages 3-6)

### Developmental trajectory / natural history indicators
GeneReviews provides milestone averages (sitting ~11 months; walking ~28.8 months; first meaningful words ~38.3 months). (chung2022okurchungneurodevelopmentalsyndrome pages 3-6)

Atypical later diagnosis/milder phenotypes exist; a 2024 report includes an affected 31-year-old proband with relatively mild early history and later functional outcomes (graduated technical secondary school, worked as cashier), illustrating variable expressivity. (nan2024okur‐chungneurodevelopmentalsyndrome pages 1-2)

Robust staging frameworks and long-term survival statistics were not available in the retrieved evidence.

---

## 9. Inheritance and Population

### Inheritance pattern
Autosomal dominant; most cases are de novo, but inherited familial cases are established, and low-level parental mosaicism is recognized. (chung2022okurchungneurodevelopmentalsyndrome pages 1-3, belnap2023inheritedcsnk2a1variants pages 1-2)

### Case counts and rarity (recent statistics)
- GeneReviews (2022-06-09) summarized **51** identified individuals with pathogenic CSNK2A1 variants at that time. (chung2022okurchungneurodevelopmentalsyndrome pages 3-6)
- Blanc et al. (AJMG-A; 2024-05; https://doi.org/10.1002/ajmg.a.63642) state: “To date, **160** patients have been diagnosed worldwide.” (blanc2024patientwitha pages 1-2)
- Rushing & Sills (2024-01; https://doi.org/10.1177/26330040241249763) report **>200 registered patients** in the CSNK2A1 Foundation registry, with **~40** additional known globally. (rushing2024patientorganizationperspective pages 2-4)

### Sex ratio
A 2022 literature review notes that early female predominance was not sustained as more cases were reported, with an approximate male:female ratio ~1:1. (khamirani2022clinicalfeaturesof pages 5-6)

### Prevalence/incidence
No population prevalence or incidence estimates were present in the retrieved evidence.

---

## 10. Diagnostics

### Clinical tests and imaging
No OCNDS-specific laboratory biomarkers are established; brain MRI abnormalities are nonspecific and present in ~55% (11/20) of those imaged in the GeneReviews-derived cohort. (chung2022okurchungneurodevelopmentalsyndrome pages 3-6)

### Genetic testing approach (real-world implementation)
| Domain | Recommendation / finding | Details / implementation notes | Suggested MAXO term(s) | Citation |
|---|---|---|---|---|
| Diagnostic framework | No formal consensus clinical diagnostic criteria published | Diagnosis is established in a proband with suggestive findings plus a heterozygous pathogenic/likely pathogenic CSNK2A1 variant | MAXO:0000000 Not applicable | (chung2022okurchungneurodevelopmentalsyndrome pages 1-3) |
| Suggestive clinical findings | Core phenotype prompting evaluation | Mild-to-moderate developmental delay or intellectual disability, generalized hypotonia in infancy/childhood, speech delay, plus infant feeding difficulties, seizures, behavioral findings, slow growth/failure to thrive, or nonspecific dysmorphic features | MAXO:0000000 Not applicable | (chung2022okurchungneurodevelopmentalsyndrome pages 1-3) |
| First-line genetic workup | Chromosomal microarray (CMA) may be an initial test in DD/ID evaluation | GeneReviews notes molecular testing in a child with DD or older person with ID may begin with CMA; useful before or alongside broader sequencing workflows | MAXO:0000127 Genetic testing | (chung2022okurchungneurodevelopmentalsyndrome pages 1-3) |
| Targeted sequencing strategy | Intellectual disability / neurodevelopmental multigene panel including CSNK2A1 | Useful after nondiagnostic CMA; panel composition varies by lab and some ID panels may omit CSNK2A1 because OCNDS is rare | MAXO:0000127 Genetic testing | (chung2022okurchungneurodevelopmentalsyndrome pages 1-3) |
| Preferred broad sequencing | Exome sequencing (ES/WES) is most commonly used | GeneReviews states ES is most commonly used; 2024 and 2023 reports repeatedly used WES/trio-WES in real-world diagnosis of simplex and familial cases | MAXO:0000127 Genetic testing | (chung2022okurchungneurodevelopmentalsyndrome pages 1-3, belnap2023inheritedcsnk2a1variants pages 1-2, nan2024okur‐chungneurodevelopmentalsyndrome pages 1-2, blanc2024patientwitha pages 1-2, zhuri2024acaseof pages 3-6) |
| Genome sequencing | Genome sequencing (GS/WGS) is also possible and increasingly important | Blanc et al. note diagnoses are likely to rise with growing use of exome and genome sequencing | MAXO:0000127 Genetic testing | (chung2022okurchungneurodevelopmentalsyndrome pages 1-3, blanc2024patientwitha pages 1-2) |
| Single-gene testing | Usually not recommended as routine first choice | GeneReviews: single-gene CSNK2A1 testing is rarely useful and typically not recommended for undifferentiated DD/ID | MAXO:0000127 Genetic testing | (chung2022okurchungneurodevelopmentalsyndrome pages 1-3) |
| Segregation testing | Confirm inheritance status with parental studies | Recent reports used Sanger/co-segregation to show de novo or inherited variants, informing counseling and recurrence risk | MAXO:0000127 Genetic testing | (nan2024okur‐chungneurodevelopmentalsyndrome pages 1-2, belnap2023inheritedcsnk2a1variants pages 1-2, zhuri2024acaseof pages 3-6) |
| RNA studies for truncating variants | Consider transcript analysis when variant mechanism is uncertain | In a 2024 familial truncating case, RT-PCR/qRT-PCR showed absent mutant transcript and ~50% reduction in CSNK2A1 product, supporting NMD/haploinsufficiency | MAXO:0000127 Genetic testing | (nan2024okur‐chungneurodevelopmentalsyndrome pages 1-2, nan2024okur‐chungneurodevelopmentalsyndrome pages 2-5) |
| Feeding management | Feeding therapy | Recommended for persistent feeding issues and difficulty transitioning feeds | MAXO:0001327 Feeding therapy | (chung2022okurchungneurodevelopmentalsyndrome pages 1-3) |
| Nutritional support | Consider gastrostomy tube placement | For persistent feeding/swallowing problems or poor growth | MAXO:0001108 Gastrostomy tube placement | (chung2022okurchungneurodevelopmentalsyndrome pages 1-3, chung2022okurchungneurodevelopmentalsyndrome pages 3-6) |
| Short stature management | Consider growth hormone therapy when endocrinology evaluation supports partial GH deficiency | GeneReviews specifies use when indicated by an endocrinologist; partial GH deficiency has been reported in OCNDS | MAXO:0000122 Hormone replacement therapy | (chung2022okurchungneurodevelopmentalsyndrome pages 1-3, chung2022okurchungneurodevelopmentalsyndrome pages 3-6) |
| Seizure management | Standard anti-seizure medication under neurology care | Used for epilepsy/seizures ranging from single events to intractable epilepsy | NCIT:C15986 Anticonvulsant therapy | (chung2022okurchungneurodevelopmentalsyndrome pages 1-3, chung2022okurchungneurodevelopmentalsyndrome pages 3-6) |
| Immunologic management | Consider intravenous immune globulin (IVIG) for demonstrated hypogammaglobulinemia | GeneReviews recommends immunologist-directed IVIG where IgG deficiency is documented | MAXO:0000079 Immunoglobulin therapy | (chung2022okurchungneurodevelopmentalsyndrome pages 1-3, chung2022okurchungneurodevelopmentalsyndrome pages 3-6) |
| Motor rehabilitation | Physical therapy / rehabilitation medicine | For hypotonia, motor coordination problems, and gait issues | MAXO:0000011 Physical therapy | (chung2022okurchungneurodevelopmentalsyndrome pages 1-3) |
| Functional rehabilitation | Occupational therapy | Standard supportive developmental therapy for function and daily living skills | MAXO:0000012 Occupational therapy | (chung2022okurchungneurodevelopmentalsyndrome pages 1-3) |
| Communication therapy | Speech/language therapy | Important because language is often more impaired than gross motor development | MAXO:0000013 Speech therapy | (chung2022okurchungneurodevelopmentalsyndrome pages 1-3, chung2022okurchungneurodevelopmentalsyndrome pages 3-6) |
| Sleep management | Monitor and treat sleep disturbance symptomatically | Sleep issues are common, often related to circadian rhythm disturbance; 77% of families in a 2022 survey reported sleep-related disruptions | MAXO:0000184 Sleep management | (chung2022okurchungneurodevelopmentalsyndrome pages 1-3, chung2022okurchungneurodevelopmentalsyndrome pages 3-6, rushing2024patientorganizationperspective pages 2-4, rushing2024patientorganizationperspective pages 1-2) |
| Cardiac/other organ management | Standard care for associated comorbidities | Includes scoliosis, constipation, congenital heart defects, renal anomalies/pelviectasis, and sleep disorders | MAXO:0000000 Supportive care | (chung2022okurchungneurodevelopmentalsyndrome pages 1-3) |
| Surveillance at each visit | Growth, nutrition, feeding safety, constipation, neurologic review, development/behavior, infections, sleep | GeneReviews recommends repeated assessment of growth parameters, feeding/oral safety, seizures/tone/movement disorders/coordination, developmental progress, behavior, unusual infections, and sleep disturbance | MAXO:0000400 Clinical monitoring | (chung2022okurchungneurodevelopmentalsyndrome pages 1-3) |
| Periodic surveillance | Ophthalmology evaluation every 1-3 years | Because ophthalmologic findings can occur, though usually nonspecific/infrequent | MAXO:0000400 Clinical monitoring | (chung2022okurchungneurodevelopmentalsyndrome pages 1-3, chung2022okurchungneurodevelopmentalsyndrome pages 3-6) |
| Genetic counseling | Counsel as autosomal dominant, usually de novo but occasionally inherited or due to parental mosaicism | Once a familial pathogenic variant is known, prenatal testing and preimplantation genetic testing are possible | MAXO:0000154 Genetic counseling | (chung2022okurchungneurodevelopmentalsyndrome pages 1-3, belnap2023inheritedcsnk2a1variants pages 1-2) |
| Real-world implementation update | Molecular testing remains the only diagnostic method currently available | 2024 roadmap article states there are no approved disease-specific treatments and diagnosis currently relies on molecular genetic testing; registry and research infrastructure are being expanded | MAXO:0000127 Genetic testing; MAXO:0000000 Supportive care | (rushing2024patientorganizationperspective pages 2-4, rushing2024patientorganizationperspective pages 1-2) |


*Table: This table summarizes practical diagnostic and management recommendations for Okur-Chung neurodevelopmental syndrome, combining the GeneReviews 2022 care framework with key 2023-2024 updates on real-world genomic diagnosis and symptom burden. It is useful for rapid clinical curation and for mapping interventions to suggested MAXO terms.*

Key implementation data points:
- GeneReviews: “Exome sequencing is most commonly used,” and single-gene testing is “typically NOT recommended” for undifferentiated DD/ID. (chung2022okurchungneurodevelopmentalsyndrome pages 1-3)
- Case series/case reports (2023–2024) show routine **WES/trio-WES** plus **Sanger segregation** for inherited vs de novo determination, and **RNA studies** to support NMD for truncating variants. (belnap2023inheritedcsnk2a1variants pages 1-2, nan2024okur‐chungneurodevelopmentalsyndrome pages 1-2, zhuri2024acaseof pages 3-6)

### Differential diagnosis
A structured differential diagnosis list was not included in the retrieved excerpts. GeneReviews notes that CSNK2A1 can be part of broader ID multigene panels and that panels may include other genes of interest (implying a broad neurodevelopmental differential). (chung2022okurchungneurodevelopmentalsyndrome pages 1-3)

---

## 11. Outcome / Prognosis

Quantitative survival, mortality, and life expectancy data were not identified in the retrieved corpus. Available evidence supports substantial **phenotypic heterogeneity** including mild adult presentations (familial null variant case), and variable seizure burden with possible underrecognition. (nan2024okur‐chungneurodevelopmentalsyndrome pages 1-2, rushing2024patientorganizationperspective pages 2-4)

---

## 12. Treatment

### Current standard of care (symptom-directed)
There are **no approved disease-modifying treatments**; management is supportive and targeted to manifestations. (rushing2024patientorganizationperspective pages 1-2, chung2022okurchungneurodevelopmentalsyndrome pages 1-3)

Key interventions and MAXO mappings are summarized in Artifact-03 (feeding therapy, gastrostomy, GH therapy when indicated, antiseizure medications, IVIG for hypogammaglobulinemia, PT/OT/speech, sleep management, and surveillance). (chung2022okurchungneurodevelopmentalsyndrome pages 1-3)

### Experimental/clinical trials
No interventional OCNDS-specific trials were identified in the retrieved clinical-trials search, but there is major **observational natural history infrastructure** (Simons Searchlight) that includes CSNK2A1. (NCT01238250 chunk 1)

---

## 13. Prevention

Primary prevention of de novo cases is not currently feasible. Prevention is primarily via **genetic counseling and reproductive options**:
- GeneReviews states that once a familial CSNK2A1 pathogenic variant is identified, **prenatal testing and preimplantation genetic testing** are possible. (chung2022okurchungneurodevelopmentalsyndrome pages 1-3)

---

## 14. Other Species / Natural Disease
No naturally occurring veterinary disease analogs were identified in the retrieved evidence.

---

## 15. Model Organisms and Research Infrastructure (applications and real-world implementations)

| Resource / model | Type | Key design / scope | Main findings / utility | Publication / status date | URL | Citation |
|---|---|---|---|---|---|---|
| Zebrafish CSNK2A1 overexpression model | In vivo model organism | Human wild-type or mutant **CSNK2A1** mRNAs injected at the single-cell stage in zebrafish; variants tested included **D156E, K198R, R47G/R47Q, Y50C, R191X** | Mutant overexpression caused variant-specific developmental defects including aberrant yolk sac, enlarged head, reduced body size, and curved spine; wild-type overexpression alone did not cause phenotype, supporting specificity | Posted 2024-01-11 | https://doi.org/10.1101/2024.01.09.574075 | (hassett2024characterizingcsnk2a1mutantinduced pages 7-9, hassett2024characterizingcsnk2a1mutantinduced pages 1-4, hassett2024characterizingcsnk2a1mutantinduced pages 4-7) |
| Zebrafish rescue experiments | Functional rescue assay | Co-injection of mutant and wild-type **CSNK2A1** mRNA (e.g., **R191X** with WT at 1:2; equal WT with **Y50C**) | Wild-type co-expression significantly rescued or attenuated mutant-induced abnormalities, supporting direct causal effects of CSNK2A1 dysfunction and therapeutic relevance of restoring WT function | Posted 2024-01-11 | https://doi.org/10.1101/2024.01.09.574075 | (hassett2024characterizingcsnk2a1mutantinduced pages 7-9, hassett2024characterizingcsnk2a1mutantinduced pages 1-4, hassett2024characterizingcsnk2a1mutantinduced pages 4-7) |
| Zebrafish CK2 inhibitor phenocopy | Pharmacologic perturbation model | Embryos treated with **CX-4945** (CK2 inhibitor) in dose-response experiments | CK2 inhibition caused dose-dependent mortality and abnormal morphology, phenocopying developmental disruption from CSNK2A1 mutant expression and implicating CK2 pathway dysfunction | Posted 2024-01-11 | https://doi.org/10.1101/2024.01.09.574075 | (hassett2024characterizingcsnk2a1mutantinduced pages 7-9, hassett2024characterizingcsnk2a1mutantinduced pages 4-7, hassett2024characterizingcsnk2a1mutantinduced pages 12-18) |
| CSNK2A1 cilia / centrosome cell biology model | Cell biology / mechanistic model | BioID, CRISPR screening, GFP pulldown, and superresolution microscopy used to study **CSNK2A1** localization and function in cilia biology | **CSNK2A1** identified as a centrosomal protein concentrated at the mother centriole/distal appendages; modulates **TTBK2** function in ciliary trafficking; mutant cilia were longer and unstable at the tip | Published 2021-04 | https://doi.org/10.1073/pnas.2018740118 | (loukil2021acomplexof pages 1-2, loukil2021acomplexof pages 2-3) |
| OCNDS-associated variant cilia defect assay | Variant-expression cell assay | Overexpression of OCNDS-associated **CSNK2A1** variants in wild-type cells | OCNDS-linked variants caused ciliary structural abnormalities, providing a mechanistic bridge from genotype to developmental cell-biology defects | Published 2021-04 | https://doi.org/10.1073/pnas.2018740118 | (loukil2021acomplexof pages 1-2) |
| CSNK2A1 Foundation registry / research infrastructure | Patient registry / natural history / advocacy infrastructure | Foundation-established OCNDS registry with patient enrollment, variant tracking, grant support, and research-roadmap development | Registry includes **>200 registered patients** with **~40 additional known globally**; foundation reported **82 distinct variants** and **22 distinct deletions**; supports natural history, biomarker development, toolbox expansion, and therapeutic planning | Published 2024-01 | https://doi.org/10.1177/26330040241249763 | (rushing2024patientorganizationperspective pages 2-4, rushing2024patientorganizationperspective pages 1-2) |
| Simons Searchlight | Observational natural history study / research platform | International, prospective, family-based online observational study for rare neurodevelopmental genetic conditions, explicitly including **CSNK2A1** | Collects medical, behavioral, learning, developmental, and biospecimen data longitudinally to improve clinical care and treatment research; useful real-world infrastructure for OCNDS natural history and outcome tracking | Study first posted 2010-11-10; recruiting; last update posted 2025-06-06 | https://clinicaltrials.gov/study/NCT01238250 | (NCT01238250 chunk 1) |
| Simons Searchlight OCNDS family survey | Patient-reported outcomes infrastructure | 2022 family survey within Simons Searchlight | Identified top family concerns in OCNDS as intellectual disability/developmental delay, language delay/inability to speak, and sleep issues; **77%** of families reported sleep-related disruptions | Reported in 2024 perspective | https://doi.org/10.1177/26330040241249763 | (rushing2024patientorganizationperspective pages 2-4, rushing2024patientorganizationperspective pages 1-2) |


*Table: This table summarizes the main experimental models and real-world research infrastructure currently supporting OCNDS/CSNK2A1 research. It highlights how zebrafish and cell-biology systems inform mechanism, while registries and observational studies enable natural-history and translational work.*

**Interpretation and expert analysis (authoritative synthesis):**
- 2024 patient-organization and research-roadmap work explicitly frames OCNDS mechanism as unresolved and likely heterogeneous across variants (“loss of function or altered substrate specificity”), and emphasizes the translational need for biomarkers and therapeutic testing pipelines, including drug repurposing and gene therapy. (rushing2024patientorganizationperspective pages 1-2, rushing2024patientorganizationperspective pages 2-4)
- The combination of (i) substrate-specificity “rewiring” for K198R, (ii) NMD/haploinsufficiency for null variants, and (iii) cilia structural defects from OCNDS variant expression provides a coherent mechanistic landscape in which **different CSNK2A1 variants may cause disease via distinct biochemical routes**, converging on neurodevelopmental phenotypes. (caefer2022theokurchungneurodevelopmental pages 1-2, nan2024okur‐chungneurodevelopmentalsyndrome pages 1-2, loukil2021acomplexof pages 1-2)

---

## Evidence gaps and limitations (explicit)
1. **ICD/Orphanet/MeSH identifiers** were not present in retrieved evidence; thus only OMIM, MONDO, and GeneReviews identifiers are reported here. (chung2022okurchungneurodevelopmentalsyndrome pages 1-3, OpenTargets Search: Okur-Chung neurodevelopmental syndrome-CSNK2A1)
2. **Population prevalence/incidence**, penetrance estimates, and formal survival statistics were not available in the retrieved corpus. (khamirani2022clinicalfeaturesof pages 5-6, rushing2024patientorganizationperspective pages 2-4)
3. Several mechanistic and cohort-wide quantitative claims (e.g., kinase activity reductions across many variants) are referenced in the 2024 perspective but the underlying primary paper is not available in this tool run, so the report prioritizes direct evidence we could retrieve (Caefer 2022; Loukil 2021; Nan 2024). (rushing2024patientorganizationperspective pages 2-4, caefer2022theokurchungneurodevelopmental pages 1-2, loukil2021acomplexof pages 1-2, nan2024okur‐chungneurodevelopmentalsyndrome pages 1-2)



References

1. (chung2022okurchungneurodevelopmentalsyndrome pages 1-3): W Chung and V Okur. Okur-chung neurodevelopmental syndrome. Unknown journal, 2022.

2. (chung2022okurchungneurodevelopmentalsyndrome pages 3-6): W Chung and V Okur. Okur-chung neurodevelopmental syndrome. Unknown journal, 2022.

3. (rushing2024patientorganizationperspective pages 1-2): Gabrielle V. Rushing and Jennifer Sills. Patient organization perspective: a research roadmap for okur-chung neurodevelopmental syndrome. Therapeutic Advances in Rare Disease, Jan 2024. URL: https://doi.org/10.1177/26330040241249763, doi:10.1177/26330040241249763. This article has 2 citations.

4. (blanc2024patientwitha pages 1-2): Albin Blanc, Céline Bonnet, Marion Wandzel, Virginie Roth, Yannis Duffourd, Hanna Safraou, Bruno Leheup, Florence Muller, Julie D Colne, François Feillet, Emmanuelle Schmitt, Matheus Castro, Jullian Savatt, Adriano Burcheri, Christophe Nemos, Christophe Philippe, and Laëtitia Lambert. Patient with a heterozygous pathogenic variant in csnk2a1 gene: a new case to update the okur–chung neurodevelopmental syndrome. American Journal of Medical Genetics Part A, May 2024. URL: https://doi.org/10.1002/ajmg.a.63642, doi:10.1002/ajmg.a.63642. This article has 3 citations.

5. (OpenTargets Search: Okur-Chung neurodevelopmental syndrome-CSNK2A1): Open Targets Query (Okur-Chung neurodevelopmental syndrome-CSNK2A1, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (belnap2023inheritedcsnk2a1variants pages 1-2): Newell Belnap, Aiai Price‐Smith, Keri Ramsey, Kamawela Leka, Anna Abraham, Emma Lieberman, Katie Hassett, Sai Potu, Natasha Rudy, Kirstin Smith, Fady M. Mikhail, Kirstin G. Monaghan, Andrea Hendershot, Jeroen Mourmans, Maria Descartes, Matthew J. Huentelman, Jennifer Sills, Sampath Rangasamy, and Vinodh Narayanan. Inherited csnk2a1 variants in families with okur‐chung neurodevelopmental syndrome. Clinical Genetics, 104:607-609, Jul 2023. URL: https://doi.org/10.1111/cge.14408, doi:10.1111/cge.14408. This article has 8 citations and is from a peer-reviewed journal.

7. (rushing2024patientorganizationperspective pages 2-4): Gabrielle V. Rushing and Jennifer Sills. Patient organization perspective: a research roadmap for okur-chung neurodevelopmental syndrome. Therapeutic Advances in Rare Disease, Jan 2024. URL: https://doi.org/10.1177/26330040241249763, doi:10.1177/26330040241249763. This article has 2 citations.

8. (nan2024okur‐chungneurodevelopmentalsyndrome pages 1-2): Haitian Nan, Min-Liang Chu, Jing Zhang, Deming Jiang, Yihao Wang, and Liyong Wu. Okur‐chung neurodevelopmental syndrome: implications for phenotype and genotype expansion. Molecular Genetics & Genomic Medicine, Mar 2024. URL: https://doi.org/10.1002/mgg3.2398, doi:10.1002/mgg3.2398. This article has 9 citations and is from a peer-reviewed journal.

9. (blanc2024patientwitha pages 4-5): Albin Blanc, Céline Bonnet, Marion Wandzel, Virginie Roth, Yannis Duffourd, Hanna Safraou, Bruno Leheup, Florence Muller, Julie D Colne, François Feillet, Emmanuelle Schmitt, Matheus Castro, Jullian Savatt, Adriano Burcheri, Christophe Nemos, Christophe Philippe, and Laëtitia Lambert. Patient with a heterozygous pathogenic variant in csnk2a1 gene: a new case to update the okur–chung neurodevelopmental syndrome. American Journal of Medical Genetics Part A, May 2024. URL: https://doi.org/10.1002/ajmg.a.63642, doi:10.1002/ajmg.a.63642. This article has 3 citations.

10. (belnap2023inheritedcsnk2a1variants pages 2-2): Newell Belnap, Aiai Price‐Smith, Keri Ramsey, Kamawela Leka, Anna Abraham, Emma Lieberman, Katie Hassett, Sai Potu, Natasha Rudy, Kirstin Smith, Fady M. Mikhail, Kirstin G. Monaghan, Andrea Hendershot, Jeroen Mourmans, Maria Descartes, Matthew J. Huentelman, Jennifer Sills, Sampath Rangasamy, and Vinodh Narayanan. Inherited csnk2a1 variants in families with okur‐chung neurodevelopmental syndrome. Clinical Genetics, 104:607-609, Jul 2023. URL: https://doi.org/10.1111/cge.14408, doi:10.1111/cge.14408. This article has 8 citations and is from a peer-reviewed journal.

11. (caefer2022theokurchungneurodevelopmental pages 1-2): Danielle M. Caefer, Nhat Q. Phan, Jennifer C. Liddle, Jeremy L. Balsbaugh, Joseph P. O’Shea, Anastasios V. Tzingounis, and Daniel Schwartz. The okur-chung neurodevelopmental syndrome mutation ck2k198r leads to a rewiring of kinase specificity. Frontiers in Molecular Biosciences, Apr 2022. URL: https://doi.org/10.3389/fmolb.2022.850661, doi:10.3389/fmolb.2022.850661. This article has 14 citations.

12. (blanc2024patientwitha pages 4-4): Albin Blanc, Céline Bonnet, Marion Wandzel, Virginie Roth, Yannis Duffourd, Hanna Safraou, Bruno Leheup, Florence Muller, Julie D Colne, François Feillet, Emmanuelle Schmitt, Matheus Castro, Jullian Savatt, Adriano Burcheri, Christophe Nemos, Christophe Philippe, and Laëtitia Lambert. Patient with a heterozygous pathogenic variant in csnk2a1 gene: a new case to update the okur–chung neurodevelopmental syndrome. American Journal of Medical Genetics Part A, May 2024. URL: https://doi.org/10.1002/ajmg.a.63642, doi:10.1002/ajmg.a.63642. This article has 3 citations.

13. (zhuri2024acaseof pages 3-6): Drenushe Zhuri, Fulya Dusenkalkan, Guzin Tunca Alparslan, and Hakan Gurkan. A case of okur-chung neurodevelopmental syndrome with a novel, de novo variant on the csnk2a1 gene in a turkish patient. Molecular Syndromology, 15:43-50, May 2024. URL: https://doi.org/10.1159/000530585, doi:10.1159/000530585. This article has 5 citations and is from a peer-reviewed journal.

14. (zhuri2024acaseof pages 1-3): Drenushe Zhuri, Fulya Dusenkalkan, Guzin Tunca Alparslan, and Hakan Gurkan. A case of okur-chung neurodevelopmental syndrome with a novel, de novo variant on the csnk2a1 gene in a turkish patient. Molecular Syndromology, 15:43-50, May 2024. URL: https://doi.org/10.1159/000530585, doi:10.1159/000530585. This article has 5 citations and is from a peer-reviewed journal.

15. (zhuri2024acaseof pages 6-7): Drenushe Zhuri, Fulya Dusenkalkan, Guzin Tunca Alparslan, and Hakan Gurkan. A case of okur-chung neurodevelopmental syndrome with a novel, de novo variant on the csnk2a1 gene in a turkish patient. Molecular Syndromology, 15:43-50, May 2024. URL: https://doi.org/10.1159/000530585, doi:10.1159/000530585. This article has 5 citations and is from a peer-reviewed journal.

16. (nan2024okur‐chungneurodevelopmentalsyndrome pages 2-5): Haitian Nan, Min-Liang Chu, Jing Zhang, Deming Jiang, Yihao Wang, and Liyong Wu. Okur‐chung neurodevelopmental syndrome: implications for phenotype and genotype expansion. Molecular Genetics & Genomic Medicine, Mar 2024. URL: https://doi.org/10.1002/mgg3.2398, doi:10.1002/mgg3.2398. This article has 9 citations and is from a peer-reviewed journal.

17. (hassett2024characterizingcsnk2a1mutantinduced pages 7-9): Katie Hassett, Sai Srihaas Potu, Aravind Sankaramoorthy, Sukanniya Kaneshamoorthy, Kamawela Leka, Matthew J. Huentelman, Vinodh Narayanan, and Sampath Rangasamy. Characterizing csnk2a1 mutant-induced morphological phenotypes in zebrafish (danio rerio): insights into okur-chung neurodevelopmental syndrome (ocnds). bioRxiv, Jan 2024. URL: https://doi.org/10.1101/2024.01.09.574075, doi:10.1101/2024.01.09.574075. This article has 0 citations.

18. (hassett2024characterizingcsnk2a1mutantinduced pages 1-4): Katie Hassett, Sai Srihaas Potu, Aravind Sankaramoorthy, Sukanniya Kaneshamoorthy, Kamawela Leka, Matthew J. Huentelman, Vinodh Narayanan, and Sampath Rangasamy. Characterizing csnk2a1 mutant-induced morphological phenotypes in zebrafish (danio rerio): insights into okur-chung neurodevelopmental syndrome (ocnds). bioRxiv, Jan 2024. URL: https://doi.org/10.1101/2024.01.09.574075, doi:10.1101/2024.01.09.574075. This article has 0 citations.

19. (hassett2024characterizingcsnk2a1mutantinduced pages 4-7): Katie Hassett, Sai Srihaas Potu, Aravind Sankaramoorthy, Sukanniya Kaneshamoorthy, Kamawela Leka, Matthew J. Huentelman, Vinodh Narayanan, and Sampath Rangasamy. Characterizing csnk2a1 mutant-induced morphological phenotypes in zebrafish (danio rerio): insights into okur-chung neurodevelopmental syndrome (ocnds). bioRxiv, Jan 2024. URL: https://doi.org/10.1101/2024.01.09.574075, doi:10.1101/2024.01.09.574075. This article has 0 citations.

20. (li2025acaseof pages 1-2): Xin Li, Shuping Wang, Xin Liu, Zhenjing Wang, Na Lv, Shaoting Wang, and Wentao Yang. A case of <scp> <i>csnk2a1</i> </scp> gene variant causing okur‐chung syndrome and analysis of the clinical phenotypic spectrum. Molecular Genetics &amp; Genomic Medicine, Dec 2025. URL: https://doi.org/10.1002/mgg3.70166, doi:10.1002/mgg3.70166. This article has 0 citations and is from a peer-reviewed journal.

21. (li2025acaseof pages 3-4): Xin Li, Shuping Wang, Xin Liu, Zhenjing Wang, Na Lv, Shaoting Wang, and Wentao Yang. A case of <scp> <i>csnk2a1</i> </scp> gene variant causing okur‐chung syndrome and analysis of the clinical phenotypic spectrum. Molecular Genetics &amp; Genomic Medicine, Dec 2025. URL: https://doi.org/10.1002/mgg3.70166, doi:10.1002/mgg3.70166. This article has 0 citations and is from a peer-reviewed journal.

22. (loukil2021acomplexof pages 1-2): Abdelhalim Loukil, Chloe Barrington, and Sarah C. Goetz. A complex of distal appendage–associated kinases linked to human disease regulates ciliary trafficking and stability. Proceedings of the National Academy of Sciences, Apr 2021. URL: https://doi.org/10.1073/pnas.2018740118, doi:10.1073/pnas.2018740118. This article has 33 citations and is from a highest quality peer-reviewed journal.

23. (khamirani2022clinicalfeaturesof pages 5-6): Hossein Jafari Khamirani, Sina Zoghi, Ali Motealleh, Mehdi Dianatpour, Seyed Mohammad Bagher Tabei, Sanaz Mohammadi, and Seyed Alireza Dastgheib. Clinical features of okur-chung neurodevelopmental syndrome: case report and literature review. Molecular Syndromology, 13:381-388, Mar 2022. URL: https://doi.org/10.1159/000522353, doi:10.1159/000522353. This article has 18 citations and is from a peer-reviewed journal.

24. (NCT01238250 chunk 1):  Online Study of People Who Have Genetic Changes and Features of Autism: Simons Searchlight. Simons Searchlight. 2010. ClinicalTrials.gov Identifier: NCT01238250

25. (hassett2024characterizingcsnk2a1mutantinduced pages 12-18): Katie Hassett, Sai Srihaas Potu, Aravind Sankaramoorthy, Sukanniya Kaneshamoorthy, Kamawela Leka, Matthew J. Huentelman, Vinodh Narayanan, and Sampath Rangasamy. Characterizing csnk2a1 mutant-induced morphological phenotypes in zebrafish (danio rerio): insights into okur-chung neurodevelopmental syndrome (ocnds). bioRxiv, Jan 2024. URL: https://doi.org/10.1101/2024.01.09.574075, doi:10.1101/2024.01.09.574075. This article has 0 citations.

26. (loukil2021acomplexof pages 2-3): Abdelhalim Loukil, Chloe Barrington, and Sarah C. Goetz. A complex of distal appendage–associated kinases linked to human disease regulates ciliary trafficking and stability. Proceedings of the National Academy of Sciences, Apr 2021. URL: https://doi.org/10.1073/pnas.2018740118, doi:10.1073/pnas.2018740118. This article has 33 citations and is from a highest quality peer-reviewed journal.
