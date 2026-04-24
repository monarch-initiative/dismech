---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-23T18:35:12.164816'
end_time: '2026-04-23T18:55:40.028191'
duration_seconds: 1227.86
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Pyruvate Carboxylase Deficiency Disease
  mondo_id: ''
  category: Metabolic Disorder
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 37
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Pyruvate Carboxylase Deficiency Disease
- **MONDO ID:**  (if available)
- **Category:** Metabolic Disorder

## Research Objectives

Please provide a comprehensive research report on **Pyruvate Carboxylase Deficiency Disease** covering all of the
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
- **Disease Name:** Pyruvate Carboxylase Deficiency Disease
- **MONDO ID:**  (if available)
- **Category:** Metabolic Disorder

## Research Objectives

Please provide a comprehensive research report on **Pyruvate Carboxylase Deficiency Disease** covering all of the
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


# Pyruvate Carboxylase Deficiency Disease (PCD) — Comprehensive Research Report

## Executive summary
Pyruvate carboxylase deficiency (PCD) is an ultra-rare, autosomal recessive mitochondrial neurometabolic disorder caused by biallelic pathogenic variants in **PC** (pyruvate carboxylase; EC 6.4.1.1) that impair conversion of pyruvate to oxaloacetate, disrupting **anaplerosis** and **gluconeogenesis** and leading to lactic acidosis, hypoglycemia, neurodevelopmental impairment, and characteristic neuroimaging abnormalities (lasio2023clinicalbiochemicaland pages 1-3, marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2, bernhardt2024pyruvatecarboxylasedeficiency pages 1-2). Contemporary (2023–2024) case reports and the largest available treatment cohort (n=12) underscore (i) severe neonatal mortality in type B disease, (ii) genotype- and phenotype-dependent variability, and (iii) mixed outcomes for anaplerotic therapy with triheptanoin, with a notable apparent benefit in a type C patient (xue2023casereportprenatal pages 1-2, jasinge2024clinicalbiochemicaland pages 2-4, lasio2023clinicalbiochemicaland pages 9-11, bernhardt2024pyruvatecarboxylasedeficiency pages 1-2).

## Key identifiers and nomenclature (disease information)
**What is the disease?** A disorder of intermediary metabolism in which deficiency of the mitochondrial biotin-dependent enzyme pyruvate carboxylase limits formation of oxaloacetate from pyruvate, causing multiorgan metabolic imbalance dominated by lactic acidemia/acidosis and early neurologic dysfunction (marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2, mochel2005pyruvatecarboxylasedeficiency pages 1-2).

**Identifiers available in retrieved evidence**
- **OMIM:** 266150 (PCD) (xue2023casereportprenatal pages 1-2, lasio2023clinicalbiochemicaland pages 1-3, wang2008themolecularbasis pages 1-2)
- **MONDO:**
  - MONDO_0018141 (infantile form)
  - MONDO_0018142 (severe neonatal type)
  - MONDO_0018143 (benign type)
  (from OpenTargets disease-target associations evidence) (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2)
- **MeSH term present in ClinicalTrials.gov record:** “Pyruvate Carboxylase Deficiency Disease” (NCT01461304 chunk 1)

**Not found in accessible full-text evidence for this run:** Orphanet/ORPHAcode, ICD-10/ICD-11, and a curated MONDO ID for the umbrella disease beyond subtype MONDO terms.

**Common synonyms / alternative names (from literature usage)**
- “Pyruvate carboxylase (PC) deficiency” (lasio2023clinicalbiochemicaland pages 1-3, wang2008themolecularbasis pages 1-2)
- “PCD type A / infantile / North American form” (xue2023casereportprenatal pages 1-2, lasio2023clinicalbiochemicaland pages 1-3, wang2008themolecularbasis pages 1-2)
- “PCD type B / severe neonatal / French form” (xue2023casereportprenatal pages 1-2, mochel2005pyruvatecarboxylasedeficiency pages 1-2, wang2008themolecularbasis pages 1-2)
- “PCD type C / intermittent / benign form” (xue2023casereportprenatal pages 1-2, bernhardt2024pyruvatecarboxylasedeficiency pages 1-2, wang2008themolecularbasis pages 1-2)

**Evidence provenance:** For this rare disease, much of the clinical description derives from *individual cases and small series* rather than large registries; a notable aggregated cohort is the 12-patient triheptanoin-treated series (lasio2023clinicalbiochemicaland pages 1-3, lasio2023clinicalbiochemicaland pages 9-11).

### Artifact: identifiers and subtype snapshot
| Disease | MONDO ID(s) in evidence | OMIM | Inheritance | Clinical subtype | Typical onset | Hallmark biochemical features | Hallmark clinical features | Quantitative epidemiology | Key recent source(s) 2023–2024 |
|---|---|---|---|---|---|---|---|---|---|
| Pyruvate carboxylase deficiency (PCD) / pyruvate carboxylase deficiency disease | MONDO_0018141 = pyruvate carboxylase deficiency, infantile form; MONDO_0018142 = pyruvate carboxylase deficiency, severe neonatal type; MONDO_0018143 = pyruvate carboxylase deficiency, benign type; disease-level association also noted as EFO_1001142 “pyruvate carboxylase deficiency disease” (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2) | 266150 (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2, xue2023casereportprenatal pages 1-2, lasio2023clinicalbiochemicaland pages 1-3, habarou2015pyruvatecarboxylasedeficiency pages 1-2, wang2008themolecularbasis pages 1-2, marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2) | Autosomal recessive; caused by biallelic/bi-allelic PC variants (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2, xue2023casereportprenatal pages 1-2, lasio2023clinicalbiochemicaland pages 1-3, habarou2015pyruvatecarboxylasedeficiency pages 1-2, wang2008themolecularbasis pages 1-2, marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2) | Disease-level summary | Congenital to infancy; variable by subtype (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2, lasio2023clinicalbiochemicaland pages 1-3, marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2) | Lactic acidosis/hyperlactataemia, ketonuria or ketoacidosis, elevated alanine; severe forms may show hyperammonemia, hypercitrullinemia, elevated lysine/proline, abnormal lactate:pyruvate and acetoacetate:β-hydroxybutyrate ratios (lasio2023clinicalbiochemicaland pages 3-4, xue2023casereportprenatal pages 1-2, lasio2023clinicalbiochemicaland pages 1-3, marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2, mochel2005pyruvatecarboxylasedeficiency pages 1-2) | Neurometabolic disorder with hypotonia, seizures, developmental delay, failure to thrive, encephalopathy; MRI may show delayed myelination/white-matter abnormalities/cysts (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2, lasio2023clinicalbiochemicaland pages 3-4, xue2023casereportprenatal pages 1-2, xue2023casereportprenatal pages 5-7, lasio2023clinicalbiochemicaland pages 1-3) | Estimated incidence/prevalence reported as ~1 in 250,000 live births/births (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2, xue2023casereportprenatal pages 1-2, lasio2023clinicalbiochemicaland pages 1-3, habarou2015pyruvatecarboxylasedeficiency pages 1-2, marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2, tsygankova2022expandingthegenetic pages 1-2, jasinge2024clinicalbiochemicaland pages 1-2) | Lasio et al., Mol Genet Metab, Jun 2023, DOI 10.1016/j.ymgme.2023.107605, https://doi.org/10.1016/j.ymgme.2023.107605 (lasio2023clinicalbiochemicaland pages 3-4, lasio2023clinicalbiochemicaland pages 1-3); Xue, Front Endocrinol, Jul 2023, DOI 10.3389/fendo.2023.1199590, https://doi.org/10.3389/fendo.2023.1199590 (xue2023casereportprenatal pages 1-2, xue2023casereportprenatal pages 5-7); Maryami et al., Iran Biomed J, Sep 2023, DOI 10.61186/ibj.27.5.307, https://doi.org/10.61186/ibj.27.5.307 (maryami2023insilicoanalysis pages 1-2, maryami2023insilicoanalysis pages 2-4); Jasinge et al., Adv Lab Med, Jan 2024, DOI 10.1515/almed-2023-0102, https://doi.org/10.1515/almed-2023-0102 (jasinge2024clinicalbiochemicaland pages 1-2, jasinge2024clinicalbiochemicaland pages 2-4, jasinge2024clinicalbiochemicaland pages 5-7); Bernhardt et al., JIMD Rep, Dec 2024, DOI 10.1002/jmd2.12405, https://doi.org/10.1002/jmd2.12405 (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2) |
| PCD type A (infantile / North American form) | MONDO_0018141 (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2) | 266150 (lasio2023clinicalbiochemicaland pages 1-3, marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2, xue2023casereportprenatal pages 1-2) | Autosomal recessive (lasio2023clinicalbiochemicaland pages 1-3, marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2, xue2023casereportprenatal pages 1-2) | Type A | Infancy; can present after neonatal period, but neonatal overlap reported (lasio2023clinicalbiochemicaland pages 1-3, marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2, bernhardt2024pyruvatecarboxylasedeficiency pages 1-2, xue2023casereportprenatal pages 1-2, jasinge2024clinicalbiochemicaland pages 1-2) | Lactic acidosis/hyperlactataemia, ketosis, hyperalaninemia, hyperprolinemia; generally less severe than type B; citrulline may be normal in A/C (lasio2023clinicalbiochemicaland pages 1-3, marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2, jasinge2024clinicalbiochemicaland pages 1-2, jasinge2024clinicalbiochemicaland pages 2-4) | Developmental delay, hypotonia, seizures, failure to thrive; often death in infancy/early childhood, though survival is longer than type B (lasio2023clinicalbiochemicaland pages 1-3, marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2, xue2023casereportprenatal pages 1-2, jasinge2024clinicalbiochemicaland pages 1-2) | Included within overall estimate ~1 in 250,000; no subtype-specific rate available in evidence (marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2, lasio2023clinicalbiochemicaland pages 1-3, jasinge2024clinicalbiochemicaland pages 1-2) | Jasinge et al., Jan 2024: one proband with moderate lactate, normal citrulline/lysine, paraventricular cystic lesions, novel homozygous c.2746G>C p.Asp916His, biochemically favoring type A, DOI/URL above (jasinge2024clinicalbiochemicaland pages 1-2, jasinge2024clinicalbiochemicaland pages 2-4) |
| PCD type B (severe neonatal / French form) | MONDO_0018142 (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2) | 266150 (xue2023casereportprenatal pages 1-2, lasio2023clinicalbiochemicaland pages 1-3, marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2, wang2008themolecularbasis pages 1-2) | Autosomal recessive (xue2023casereportprenatal pages 1-2, lasio2023clinicalbiochemicaland pages 1-3, marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2, wang2008themolecularbasis pages 1-2) | Type B | Neonatal, often within first 72 h or first hours of life (xue2023casereportprenatal pages 1-2, lasio2023clinicalbiochemicaland pages 1-3, marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2, mochel2005pyruvatecarboxylasedeficiency pages 1-2, jasinge2024clinicalbiochemicaland pages 1-2, jasinge2024clinicalbiochemicaland pages 2-4, maryami2023insilicoanalysis pages 2-4) | Severe lactic acidosis, ketoacidosis, hyperammonemia, hypercitrullinemia, elevated alanine/proline/lysine, abnormal redox ratios; high plasma lactate often >10 mmol/L (lasio2023clinicalbiochemicaland pages 3-4, xue2023casereportprenatal pages 1-2, lasio2023clinicalbiochemicaland pages 1-3, marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2, mochel2005pyruvatecarboxylasedeficiency pages 1-2, jasinge2024clinicalbiochemicaland pages 1-2, jasinge2024clinicalbiochemicaland pages 2-4, maryami2023insilicoanalysis pages 2-4) | Tachypnea/respiratory distress, truncal hypotonia, seizures, abnormal movements, liver failure/hepatomegaly, severe encephalopathy; usually early death, often within weeks to months (xue2023casereportprenatal pages 1-2, xue2023casereportprenatal pages 5-7, lasio2023clinicalbiochemicaland pages 1-3, marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2, mochel2005pyruvatecarboxylasedeficiency pages 1-2, jasinge2024clinicalbiochemicaland pages 1-2, jasinge2024clinicalbiochemicaland pages 2-4, maryami2023insilicoanalysis pages 2-4) | No subtype-specific population rate; prognosis poor with survival often <3 months in reports/reviews (xue2023casereportprenatal pages 1-2, mochel2005pyruvatecarboxylasedeficiency pages 1-2) | Xue, Jul 2023: first reported Chinese type B case, compound heterozygous c.1154_1155del and c.152G>A, death at 26 days, DOI/URL above (xue2023casereportprenatal pages 1-2); Maryami et al., Sep 2023: novel p.G303Afs*40 and p.R156P associated with severe/type B disease, DOI/URL above (maryami2023insilicoanalysis pages 1-2, maryami2023insilicoanalysis pages 2-4); Jasinge et al., Jan 2024: two siblings with typical type B biochemical findings, truncating c.2514G>A p.Trp838*, DOI/URL above (jasinge2024clinicalbiochemicaland pages 1-2, jasinge2024clinicalbiochemicaland pages 2-4, jasinge2024clinicalbiochemicaland pages 5-7) |
| PCD type C (benign / intermittent form) | MONDO_0018143 (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2) | 266150 (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2, marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2) | Autosomal recessive (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2, marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2) | Type C | Later onset or intermittent; reported from infancy to childhood (e.g., 2 years) with episodic crises (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2, marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2) | Episodic hyperlactataemia, ketoacidosis, hypoglycaemia; milder/intermittent biochemical abnormalities (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2, lasio2023clinicalbiochemicaland pages 3-4, marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2) | Relatively favorable prognosis, mild developmental delay, exercise intolerance, recurrent hospitalizations during illness; MRI may show delayed myelination or mild volume loss (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2) | Only 11 type C patients reported, 7 molecularly confirmed, in Bernhardt et al. 2024 (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2) | Bernhardt et al., Dec 2024: 2 new type C cases; triheptanoin up-titrated to 35 mL/day (~25% daily energy) in one patient was associated with fewer hospitalizations, resolution of post-exertional hyperlactataemia, improved exercise tolerance, and improved myelination over 18 months to 2 years, DOI/URL above (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2) |


*Table: This table summarizes core disease identifiers, inheritance, subtype-defining features, epidemiology, and recent 2023–2024 primary literature for pyruvate carboxylase deficiency. It is designed as a compact reference for rapid evidence-grounded review.*

## Etiology
### Disease causal factors
**Genetic cause:** Biallelic pathogenic variants in **PC** cause PCD (autosomal recessive) (lasio2023clinicalbiochemicaland pages 1-3, wang2008themolecularbasis pages 1-2, bernhardt2024pyruvatecarboxylasedeficiency pages 1-2).

**Molecular function:** PC catalyzes the ATP-dependent carboxylation of pyruvate to oxaloacetate (OAA), supporting gluconeogenesis and replenishing tricarboxylic acid (TCA) cycle intermediates (anaplerosis) (mochel2005pyruvatecarboxylasedeficiency pages 1-2, marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2).

### Risk factors
- **Family history / autosomal recessive inheritance** (lasio2023clinicalbiochemicaland pages 1-3, wang2008themolecularbasis pages 1-2)
- **Consanguinity** is highlighted in recent neonatal series from Sri Lanka (two consanguineous families) (jasinge2024clinicalbiochemicaland pages 2-4).

### Protective factors
No validated genetic “protective variants” or environmental protective factors were identified in the retrieved evidence.

### Gene–environment interactions
No direct gene–environment interaction studies were retrieved; however, metabolic stress/infections can precipitate decompensation episodes in infantile forms (wang2008themolecularbasis pages 1-2).

## Phenotypes (clinical spectrum)
PCD is classically divided into three overlapping phenotypes (A/B/C) (xue2023casereportprenatal pages 1-2, wang2008themolecularbasis pages 1-2, marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2).

### Type B (severe neonatal) — high mortality
- **Onset:** within hours to first 72 hours of life (xue2023casereportprenatal pages 1-2, jasinge2024clinicalbiochemicaland pages 2-4).
- **Key manifestations:** severe lactic acidosis with metabolic acidosis, hyperammonemia and hypercitrullinemia, hypotonia, seizures, abnormal movements, and frequent early death (xue2023casereportprenatal pages 1-2, wang2008themolecularbasis pages 1-2, jasinge2024clinicalbiochemicaland pages 2-4).
- **Quantitative examples:**
  - In the Chinese type B case: arterial **pH 7.24**, **HCO3− 5.2 mM**, urine lactic acid **7262 nmol/mg creatinine**, urine pyruvate **1416.8 nmol/mg creatinine**, urine 3-hydroxybutyrate **1725.3 nmol/mg creatinine** (xue2023casereportprenatal pages 1-2).
  - In the Sri Lankan neonatal series: example **lactate 18.75 mmol/L**, **pH 7.12**, **HCO3− 4.2 mmol/L**, **glucose 38 mg/dL** (jasinge2024clinicalbiochemicaland pages 2-4).

### Type A (infantile)
- **Onset:** infancy; neonatal overlap reported (lasio2023clinicalbiochemicaland pages 1-3, jasinge2024clinicalbiochemicaland pages 1-2).
- **Key manifestations:** lactic acidosis/hyperlactataemia, ketosis, hypotonia, seizures, developmental delay; death often in infancy/early childhood (lasio2023clinicalbiochemicaland pages 1-3, wang2008themolecularbasis pages 1-2).

### Type C (intermittent/benign/attenuated)
- **Onset/course:** episodic metabolic decompensation; comparatively favorable prognosis (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2).
- **Clinical pattern:** episodic hyperlactataemia and ketoacidosis with milder developmental delay and variable myelination changes (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2).
- **Quantitative example:** persistent lactate 4.1–5.9 mmol/L with lactate:pyruvate ratio 24–29 (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2).

### Suggested HPO terms (non-exhaustive; based on phenotypes repeatedly described)
- **Metabolic/biochemical:** Lactic acidosis (HP:0003128), Metabolic acidosis (HP:0001942), Hypoglycemia (HP:0001943), Hyperammonemia (HP:0001987), Ketonuria (HP:0002919), Ketoacidosis (HP:0001993)
- **Neurologic:** Hypotonia (HP:0001252), Seizures (HP:0001250), Developmental delay (HP:0001263), Encephalopathy (HP:0001298), Abnormal movement (HP:0001270)
- **Respiratory:** Tachypnea/Respiratory distress (HP:0002094/HP:0002098)
- **Neuroimaging:** Delayed myelination (HP:0003429), Ventriculomegaly (HP:0002119), Subependymal cysts (HP:0010629) (supported by case descriptions) (xue2023casereportprenatal pages 1-2, bernhardt2024pyruvatecarboxylasedeficiency pages 1-2).

## Genetic / molecular information
### Causal gene
- **PC** (pyruvate carboxylase), nuclear-encoded mitochondrial enzyme; gene maps to 11q13 region and encodes a ~125 kDa protein; multiple transcripts exist (wang2008themolecularbasis pages 1-2).

### Pathogenic variant spectrum (classes and recent examples)
Variant classes include missense, nonsense/frameshift, small deletions/insertions, splice-site variants, and (importantly for diagnostics) deep intronic and structural variants (reciprocal translocation disrupting PC) (tsygankova2022expandingthegenetic pages 1-2, wang2008themolecularbasis pages 1-2).

**Recent (2023–2024) examples**
- **Type B:** compound heterozygous variants c.1154_1155del and c.152G>A (China case report) (xue2023casereportprenatal pages 1-2).
- **Type B:** homozygous frameshift c.908delG:p.G303Afs*40 (likely pathogenic) and homozygous missense p.R156P (VUS in paper but argued damaging by in silico modeling) (maryami2023insilicoanalysis pages 1-2, maryami2023insilicoanalysis pages 2-4).
- **Sri Lankan neonates:** homozygous nonsense c.2514G>A (p.Trp838*) in one proband; novel homozygous missense c.2746G>C (p.Asp916His) in another (jasinge2024clinicalbiochemicaland pages 2-4, jasinge2024clinicalbiochemicaland pages 1-2).

**Deep intronic / structural findings (diagnostic expansion)**
- Homozygous deep intronic c.1983-116C>T caused exonization (residual WT transcript present) (tsygankova2022expandingthegenetic pages 1-2).
- Reciprocal translocation disrupting PC discovered by WGS and validated by FISH/Sanger (tsygankova2022expandingthegenetic pages 1-2).

**Variant counts (HGMD snapshot as of 2022-06-12)**
A 2022 report states 62 PC variants in HGMD, with distribution: 42 missense/nonsense, 7 splicing, 7 small deletions, 5 small insertions, 1 small duplication; and noted that large structural or deep intronic variants had not been reported *at that time*—their paper then contributed such variant classes (tsygankova2022expandingthegenetic pages 1-2).

### Modifier-like genetic factors
**Somatic mosaicism:** In an 8-patient molecular series (1 type A, 5 type B, 2 type C), mosaicism was found in 5 cases and 4 had prolonged survival; authors concluded survival correlated better with mosaicism than with classical phenotype labels or residual protein (wang2008themolecularbasis pages 1-2).

## Environmental information
No specific environmental toxins, lifestyle factors, or infectious agents as causal contributors were identified. Intercurrent infections/illnesses are repeatedly described as triggers for metabolic decompensation (e.g., type C and type A/B overlap cases) (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2, wang2008themolecularbasis pages 1-2).

## Mechanism / pathophysiology
### Core biochemical lesion and causal chain
1. **PC loss-of-function** reduces conversion of pyruvate → oxaloacetate (OAA) in mitochondria (mochel2005pyruvatecarboxylasedeficiency pages 1-2, marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2).
2. **OAA deficit** impairs replenishment of TCA intermediates (**anaplerosis**) and compromises gluconeogenesis (mochel2005pyruvatecarboxylasedeficiency pages 1-2, marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2).
3. Energy failure and redox imbalance promote **lactic acidosis** (often severe in type B) and can lead to **hypoglycemia** (marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2, bernhardt2024pyruvatecarboxylasedeficiency pages 1-2, jasinge2024clinicalbiochemicaland pages 2-4).
4. Disruption of aspartate/OAA-dependent processes contributes to **urea-cycle perturbation**, manifesting as **hypercitrullinemia** and **hyperammonemia** in severe neonatal disease (wang2008themolecularbasis pages 1-2, xue2023casereportprenatal pages 1-2).
5. CNS vulnerability: PC activity is robust in glia but absent in neurons; glial anaplerosis supports glutamine supply for neuronal glutamate/GABA, providing a mechanistic basis for neurologic dysfunction and encephalopathy (marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2).

### Pathways and ontology suggestions
- **Pathways:** TCA cycle / Krebs cycle; gluconeogenesis; anaplerotic reactions (marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2, mochel2005pyruvatecarboxylasedeficiency pages 1-2).
- **GO biological process (suggested):** anaplerotic reaction; gluconeogenesis; tricarboxylic acid cycle; regulation of cellular redox homeostasis.
- **GO molecular function (suggested):** pyruvate carboxylase activity.
- **Cell types (CL suggested):** astrocyte (glial PC activity emphasized) (marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2).
- **Anatomy (UBERON suggested):** liver, brain, kidney, pancreatic islet (high PC activity tissues) (marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2, wang2008themolecularbasis pages 1-2).
- **CHEBI suggested:** pyruvate, oxaloacetate, lactate, alanine, citrate, aspartate, ammonia.

## Anatomical structures affected
- **Primary systems/organs:** CNS/brain (encephalopathy, seizures, myelination abnormalities), liver (hepatic failure in severe neonatal cases), metabolic homeostasis broadly (mochel2005pyruvatecarboxylasedeficiency pages 1-2, bernhardt2024pyruvatecarboxylasedeficiency pages 1-2, jasinge2024clinicalbiochemicaland pages 2-4).
- **Neuroimaging localizations:** delayed cerebral myelination and cystic white matter/ventricular abnormalities have been documented, including prenatal onset as early as 22w5d gestation (xue2023casereportprenatal pages 1-2, bernhardt2024pyruvatecarboxylasedeficiency pages 1-2).
- **Subcellular (GO cellular component suggested):** mitochondrial matrix (PC localization) (tsygankova2022expandingthegenetic pages 1-2).

## Temporal development
- **Type B:** acute neonatal presentation; often death within weeks to months. A specific case died at 26 days (xue2023casereportprenatal pages 1-2). A 2024 series notes two neonates died within the first six weeks (jasinge2024clinicalbiochemicaland pages 2-4).
- **Type A:** onset in infancy with variable course; death often in infancy/early childhood (lasio2023clinicalbiochemicaland pages 1-3, wang2008themolecularbasis pages 1-2).
- **Type C:** episodic course with comparatively favorable prognosis and longer survival; symptomatic crises can be triggered by illness/exertion (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2).

## Inheritance and population
- **Inheritance:** autosomal recessive (lasio2023clinicalbiochemicaland pages 1-3, wang2008themolecularbasis pages 1-2).
- **Epidemiology:** multiple sources cite an estimate of ~**1 in 250,000** live births/births (lasio2023clinicalbiochemicaland pages 1-3, xue2023casereportprenatal pages 1-2, bernhardt2024pyruvatecarboxylasedeficiency pages 1-2, marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2, tsygankova2022expandingthegenetic pages 1-2).
- **Population clusters:** 2010 review notes higher reporting in specific groups (Algonquian-speaking Amerindians and Arabs) (marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2).

## Diagnostics
### Biochemical testing (core real-world implementation)
- **Blood gases / lactate:** PCD often presents with lactic acidemia; mechanistic review gives typical lactic acid >5 mmol/L and bicarbonate <18 mmol/L (marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2). Severe type B often has lactate >10 mmol/L (jasinge2024clinicalbiochemicaland pages 1-2, mochel2005pyruvatecarboxylasedeficiency pages 1-2).
- **Redox ratios:** elevated lactate:pyruvate and altered ketone ratios (acetoacetate:β-hydroxybutyrate; 3-hydroxybutyrate:acetoacetate) described as characteristic, especially in type B (lasio2023clinicalbiochemicaland pages 1-3, wang2008themolecularbasis pages 1-2).
- **Plasma amino acids:** elevations can include alanine, citrulline, proline, lysine (especially type B) (lasio2023clinicalbiochemicaland pages 1-3, wang2008themolecularbasis pages 1-2, jasinge2024clinicalbiochemicaland pages 2-4).
- **Urine organic acids:** elevated lactate and ketone bodies; some reports describe reduced excretion of TCA intermediates (jasinge2024clinicalbiochemicaland pages 2-4, mochel2005pyruvatecarboxylasedeficiency pages 1-2).

### Imaging
- Brain MRI features include delayed myelination/hypomyelination and cystic/ventricular abnormalities; prenatal imaging abnormalities can occur (xue2023casereportprenatal pages 1-2, bernhardt2024pyruvatecarboxylasedeficiency pages 1-2).

### Enzyme assays
- Definitive diagnosis may require enzymatic assay; a 2010 review states enzymatic assay is “still often required” (marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2).
- Enzyme activity can be assessed in **cultured fibroblasts** (also referenced as a definitive approach in 2022 genetic paper) (tsygankova2022expandingthegenetic pages 1-2, habarou2015pyruvatecarboxylasedeficiency pages 2-3).
- Prenatal confirmation can include PC activity measurement in chorionic villi or cultured amniotic fluid cells (xue2023casereportprenatal pages 5-7).

### Genetic testing approach
- **WES** used in multiple recent cases (China type B report; Maryami 2023; Tsygankova 2022) (xue2023casereportprenatal pages 1-2, maryami2023insilicoanalysis pages 2-4, tsygankova2022expandingthegenetic pages 1-2).
- **WGS with deep analysis** is recommended when standard testing yields 0–1 pathogenic allele, as deep intronic and structural variants can be missed (tsygankova2022expandingthegenetic pages 1-2).

### Differential diagnosis
Several disorders can overlap with lactic acidosis and neurologic dysfunction (e.g., other disorders of pyruvate metabolism/TCA cycle, mitochondrial respiratory chain disorders); misdiagnosis as respiratory chain defect has been documented (habarou2015pyruvatecarboxylasedeficiency pages 1-2).

### Screening
No evidence in the retrieved corpus supports routine newborn screening for PCD.

## Outcome / prognosis
- Mechanistic review: “There is no effective treatment… most, except those affected by the benign form, die in early life” (marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2).
- Type B neonatal cases frequently die early despite supportive care (e.g., death at 26 days) (xue2023casereportprenatal pages 1-2).
- **Prognostic modifier:** somatic mosaicism correlates with prolonged survival (wang2008themolecularbasis pages 1-2).

## Treatment
### Acute management (real-world implementation)
- Anti-catabolic therapy (e.g., dextrose-containing IV fluids) and correction of acidosis (bicarbonate) are repeatedly used in severe neonatal presentations and reviews (lasio2023clinicalbiochemicaland pages 3-4, bernhardt2024pyruvatecarboxylasedeficiency pages 1-2, xue2023casereportprenatal pages 1-2, jasinge2024clinicalbiochemicaland pages 2-4).

### Cofactors / supplements (supportive)
- **Biotin** is frequently trialed (minimal effect in A/B; occasional benefit reported in C) (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2).
- Thiamine, riboflavin, carnitine, CoQ10 and other supportive measures are commonly administered in case management (xue2023casereportprenatal pages 1-2, mochel2005pyruvatecarboxylasedeficiency pages 1-2, habarou2015pyruvatecarboxylasedeficiency pages 2-3, jasinge2024clinicalbiochemicaland pages 2-4).
- **Citrate/aspartate** supplementation may stabilize systemic biochemical derangements but may not normalize CSF abnormalities or neurologic outcome (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2).

### Anaplerotic therapy: triheptanoin
**Concept:** triheptanoin (odd-chain triglyceride) yields acetyl-CoA and propionyl-CoA; propionyl-CoA → succinyl-CoA replenishes TCA intermediates (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2).

**Evidence and outcomes**
- **Largest cohort (n=12; 2023):** overall trend toward lactate reduction in 4 of 6 analyzable subjects; only one approached statistical significance; HRQoL outcomes were mixed (lasio2023clinicalbiochemicaland pages 9-11). Authors propose possible genotype-dependent response patterns (lasio2023clinicalbiochemicaland pages 9-11).
- **Type C case with apparent benefit (2024):** triheptanoin up-titrated to **35 mL/day (~25% daily energy)** was associated with fewer hospitalizations, resolution of post-exertional hyperlactataemia, improved exercise tolerance, and improved myelination on repeat MRI at 18 months, with apparent efficacy over 2 years (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2).
- **Severe neonatal report (2005):** a type B infant showed “immediate reversal (less than 48 h) of major hepatic failure” on triheptanoin-based anaplerotic management, but later died from severe infection (mochel2005pyruvatecarboxylasedeficiency pages 1-2).

### Transplantation
Liver transplantation is referenced in the triheptanoin cohort paper as having produced partial biochemical improvement in some reports, but detailed outcomes were not extractable in the provided excerpt (lasio2023clinicalbiochemicaland pages 3-4).

### Clinical trials / expanded access
**ClinicalTrials.gov expanded access:** NCT01461304 (“Compassionate Use of Triheptanoin (C7) for Inherited Disorders of Energy Metabolism”) explicitly includes PCD as an eligible condition. Key operational details from the record include:
- First posted: 2011-10-28; last update posted: 2021-12-10 (NCT01461304 chunk 1).
- Dosing described as up to **2 g/kg/24 h** (up to **4 g/kg/24 h** in cardiomyopathy), divided doses, with 12-month period and extension option (NCT01461304 chunk 1).

### MAXO term suggestions (treatments/interventions)
- Intravenous glucose administration; correction of metabolic acidosis; dietary management; triheptanoin supplementation (anaplerotic therapy); biotin supplementation; genetic counseling; prenatal diagnosis.

## Prevention
- **Primary prevention:** not applicable beyond carrier screening strategies.
- **Secondary/tertiary prevention:** rapid recognition and early metabolic management in tachypneic neonates with metabolic acidosis is emphasized (jasinge2024clinicalbiochemicaland pages 1-2).
- **Genetic counseling and prenatal diagnosis:** strongly emphasized; prenatal neuroradiologic abnormalities can be detected early (22w5d) and prenatal molecular testing (amniotic fluid sequencing) is feasible (xue2023casereportprenatal pages 1-2, xue2023casereportprenatal pages 5-7).

## Other species / natural disease
No naturally occurring veterinary cases were retrieved in the available evidence.

## Model organisms and experimental models
No PCD-specific animal model papers were retrieved in this run. Human cellular models used for diagnosis/research include **patient-derived skin fibroblasts** (enzyme activity assays; expression studies) and prenatal cell sources (chorionic villi/amniocytes) (marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2, tsygankova2022expandingthegenetic pages 1-2, xue2023casereportprenatal pages 5-7).

## Recent developments (2023–2024 highlights)
1. **Largest treated cohort to date (2023):** long-term triheptanoin treatment in 12 PCD patients suggests high inter-individual variability and possible genotype-dependent response, but limited statistical signal overall (lasio2023clinicalbiochemicaland pages 1-3, lasio2023clinicalbiochemicaland pages 9-11).
2. **Prenatal onset documented (2023):** neuroradiologic phenotype detected as early as 22w5d gestation in a genetically confirmed type B case, reinforcing prenatal diagnostic value (xue2023casereportprenatal pages 1-2).
3. **New neonatal genotypes (2023–2024):** multiple novel PC variants (frameshift, nonsense, missense) reported across diverse populations (Iran; Sri Lanka; China) (maryami2023insilicoanalysis pages 1-2, jasinge2024clinicalbiochemicaland pages 2-4, xue2023casereportprenatal pages 1-2).
4. **Type C triheptanoin response (2024):** first reported type C triheptanoin response with reduced hospitalizations and improved myelination (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2).

### Artifact: variants and diagnostic hallmarks with example values
| Section | Study / case | Year | Phenotype | Variant class / hallmark | cDNA | Protein | Zygosity | Example quantitative / descriptive findings | DOI / URL | Citation |
|---|---|---:|---|---|---|---|---|---|---|---|
| Variant | Xue case report, first reported Chinese type B case | 2023 | Type B | Compound heterozygous deletion + missense | c.1154_1155del; c.152G>A | NA | Compound heterozygous | Prenatal neuroradiologic abnormalities from 22w5d; infant died at 26 days | 10.3389/fendo.2023.1199590 / https://doi.org/10.3389/fendo.2023.1199590 | (xue2023casereportprenatal pages 1-2) |
| Variant | Maryami et al., neonate 1 | 2023 | Type B / severe form | Frameshift | c.908delG | p.G303Afs*40 | Homozygous | Classified likely pathogenic (ACMG); associated with acute early-onset metabolic derangement and neonatal death | 10.61186/ibj.27.5.307 / https://doi.org/10.61186/ibj.27.5.307 | (maryami2023insilicoanalysis pages 1-2, maryami2023insilicoanalysis pages 2-4) |
| Variant | Maryami et al., neonate 2 | 2023 | Type B / severe form | Missense | NA | p.R156P | Homozygous | Classified VUS by ACMG in paper, but authors concluded pathogenicity supported by in silico/ATP-binding destabilization | 10.61186/ibj.27.5.307 / https://doi.org/10.61186/ibj.27.5.307 | (maryami2023insilicoanalysis pages 1-2, maryami2023insilicoanalysis pages 2-4) |
| Variant | Jasinge et al., Sri Lankan proband | 2024 | Type A-favoring overlap | Missense | c.2746G>C | p.Asp916His | Homozygous | Novel variant in neonate with normal citrulline/lysine, moderate lactate, paraventricular cystic lesions, bony deformities | 10.1515/almed-2023-0102 / https://doi.org/10.1515/almed-2023-0102 | (jasinge2024clinicalbiochemicaland pages 1-2, jasinge2024clinicalbiochemicaland pages 2-4, jasinge2024clinicalbiochemicaland pages 5-7) |
| Variant | Jasinge et al., affected siblings | 2024 | Type B | Nonsense / truncating | c.2514G>A | p.Trp838* | Homozygous | Severe neonatal presentation; two affected neonates died in first six weeks of life in series | 10.1515/almed-2023-0102 / https://doi.org/10.1515/almed-2023-0102 | (jasinge2024clinicalbiochemicaland pages 2-4, jasinge2024clinicalbiochemicaland pages 5-7) |
| Variant | Tsygankova et al., Patient 1 | 2022 | Type A | Missense + structural rearrangement | c.1372A>G | p.Asn458Asp | Heterozygous plus reciprocal translocation disrupting PC | WGS found discordant reads mapped to chr11/chr1; diagnosis required structural variant analysis | 10.1016/j.ymgmr.2022.100889 / https://doi.org/10.1016/j.ymgmr.2022.100889 | (tsygankova2022expandingthegenetic pages 1-2) |
| Variant | Tsygankova et al., Patient 2 | 2022 | Type C | Deep intronic splice-altering | c.1983-116C>T | NA | Homozygous | mRNA analysis showed exonization of intron 16 sequences with residual WT transcript | 10.1016/j.ymgmr.2022.100889 / https://doi.org/10.1016/j.ymgmr.2022.100889 | (tsygankova2022expandingthegenetic pages 1-2) |
| Variant | Tsygankova et al., additional patients | 2022 | Type A / Type B | Missense | c.1876C>T; c.2606G>C; c.2435C>A | p.Arg626Trp; p.Gly869Ala; p.Ala812Asp | Compound heterozygous or homozygous | Reported in more severe disease; exact patient-level assignment not fully extractable from available evidence | 10.1016/j.ymgmr.2022.100889 / https://doi.org/10.1016/j.ymgmr.2022.100889 | (tsygankova2022expandingthegenetic pages 1-2) |
| Variant | Wang et al., eight-patient molecular series | 2008 | Types A/B/C | Mixed classes: missense, deletions, splice-site, nonsense | NA | NA | Includes mosaic and non-mosaic cases | Eight novel complex mutations in 8 cases; somatic mosaicism in 5 cases, 4 with prolonged survival | 10.1016/j.ymgme.2008.06.006 / https://doi.org/10.1016/j.ymgme.2008.06.006 | (wang2008themolecularbasis pages 1-2) |
| Biochemical hallmark | General type B pattern from reviews/series | 2005-2024 | Type B | Plasma lactate | NA | NA | NA | Often high and severe; “high plasma lactate often >10 mmol/L” in type B | NA | (mochel2005pyruvatecarboxylasedeficiency pages 1-2, jasinge2024clinicalbiochemicaland pages 1-2) |
| Biochemical hallmark | Xue case report | 2023 | Type B | Plasma / blood gas | NA | NA | NA | Arterial pH 7.24; HCO3− 5.2 mM | 10.3389/fendo.2023.1199590 / https://doi.org/10.3389/fendo.2023.1199590 | (xue2023casereportprenatal pages 1-2) |
| Biochemical hallmark | Xue case report | 2023 | Type B | Plasma amino acids | NA | NA | NA | Citrulline 109.4 mM; tyrosine 223.4 mM; alanine 408.5 mM | 10.3389/fendo.2023.1199590 / https://doi.org/10.3389/fendo.2023.1199590 | (xue2023casereportprenatal pages 1-2) |
| Biochemical hallmark | Xue case report | 2023 | Type B | Urine organic acids | NA | NA | NA | Lactic acid 7262 nmol/mg creatinine; pyruvate 1416.8 nmol/mg creatinine; 3-hydroxybutyric acid 1725.3 nmol/mg creatinine | 10.3389/fendo.2023.1199590 / https://doi.org/10.3389/fendo.2023.1199590 | (xue2023casereportprenatal pages 1-2) |
| Biochemical hallmark | Xue case report | 2023 | Type B | MRI / fetal imaging | NA | NA | NA | Widened posterior horns of lateral ventricles, huge subependymal cysts, increased biparietal diameter and head circumference | 10.3389/fendo.2023.1199590 / https://doi.org/10.3389/fendo.2023.1199590 | (xue2023casereportprenatal pages 1-2, xue2023casereportprenatal pages 5-7) |
| Biochemical hallmark | Jasinge et al., Patient 1 example | 2024 | Type B | Lactate / acid-base / glucose | NA | NA | NA | Plasma lactate 18.75 mmol/L; pH 7.12; HCO3− 4.2 mmol/L; capillary glucose 38 mg/dL | 10.1515/almed-2023-0102 / https://doi.org/10.1515/almed-2023-0102 | (jasinge2024clinicalbiochemicaland pages 2-4) |
| Biochemical hallmark | Jasinge et al. | 2024 | Type B | Plasma amino acids | NA | NA | NA | Markedly elevated citrulline, alanine, lysine, and tyrosine | 10.1515/almed-2023-0102 / https://doi.org/10.1515/almed-2023-0102 | (jasinge2024clinicalbiochemicaland pages 2-4) |
| Biochemical hallmark | Jasinge et al. | 2024 | Type A/B overlap | Urine organic acids | NA | NA | NA | Very high lactate and ketone bodies (3-hydroxybutyrate, acetoacetate); reduced urinary TCA intermediates including alpha-ketoglutarate, fumarate, oxaloacetate, malate | 10.1515/almed-2023-0102 / https://doi.org/10.1515/almed-2023-0102 | (jasinge2024clinicalbiochemicaland pages 2-4, jasinge2024clinicalbiochemicaland pages 5-7) |
| Biochemical hallmark | Jasinge et al. | 2024 | Type A/B overlap | Neuroimaging | NA | NA | NA | Porencephalic cysts, paraventricular cystic lesions, microcephaly; recurrent infections precipitated refractory metabolic acidosis | 10.1515/almed-2023-0102 / https://doi.org/10.1515/almed-2023-0102 | (jasinge2024clinicalbiochemicaland pages 1-2, jasinge2024clinicalbiochemicaland pages 5-7) |
| Biochemical hallmark | Bernhardt et al., Patient 1 | 2024 | Type C | Lactate / lactate:pyruvate | NA | NA | NA | Persistent hyperlactataemia 4.1–5.9 mmol/L; lactate:pyruvate ratio 24–29 (normal <25) | 10.1002/jmd2.12405 / https://doi.org/10.1002/jmd2.12405 | (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2) |
| Biochemical hallmark | Bernhardt et al., Patient 1 | 2024 | Type C | Glucose / ammonia | NA | NA | NA | Severe neonatal lactic acidosis and hypoglycaemia without hyperammonaemia | 10.1002/jmd2.12405 / https://doi.org/10.1002/jmd2.12405 | (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2) |
| Biochemical hallmark | Bernhardt et al. | 2024 | Type C | MRI | NA | NA | NA | Delayed cerebral myelination with improvement on follow-up after triheptanoin | 10.1002/jmd2.12405 / https://doi.org/10.1002/jmd2.12405 | (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2) |
| Biochemical hallmark | Hidalgo review/case summary | 2021 | Types A/B/C | Lactate and lactate:pyruvate ranges | NA | NA | NA | Type A lactate 2–10 mmol/L; Type B >10 mmol/L; Type C 2–5 mmol/L; lactate:pyruvate ratio usually >20 in type B and <20 in types A/C | 10.7759/cureus.15042 / https://doi.org/10.7759/cureus.15042 | (hidalgo2021auniquecase pages 4-5) |
| Biochemical hallmark | Lasio et al. review of phenotype | 2023 | Types A/B/C | Signature abnormalities | NA | NA | NA | Type B: severe neonatal lactic acidosis, ketoacidosis, hyperammonemia, elevated alanine/citrulline/proline/lysine, elevated lactate:pyruvate and acetoacetate:β-hydroxybutyrate; Type A: lactic acidosis, ketosis, hyperalaninemia, hyperprolinemia | 10.1016/j.ymgme.2023.107605 / https://doi.org/10.1016/j.ymgme.2023.107605 | (lasio2023clinicalbiochemicaland pages 3-4, lasio2023clinicalbiochemicaland pages 1-3) |


*Table: This table compiles representative PC variants and core diagnostic biochemical/imaging features for pyruvate carboxylase deficiency using only evidence available in the conversation. It is useful as a quick-reference artifact linking genotype classes to phenotype subtypes and concrete diagnostic values from recent case reports and series.*

## Evidence-based expert interpretation (authoritative analysis)
- The field consensus remains that **disease-modifying therapy is lacking** and supportive care predominates, especially for types A/B where early mortality is common (marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2, bernhardt2024pyruvatecarboxylasedeficiency pages 1-2).
- Anaplerotic therapy is mechanistically attractive because the “primary result of the defect is a major deficit of oxaloacetate for the CAC,” but real-world outcomes are heterogeneous and may depend on genotype/domain effects and phenotype severity (mochel2005pyruvatecarboxylasedeficiency pages 1-2, lasio2023clinicalbiochemicaland pages 9-11).
- Diagnostic practice is shifting toward **genome-wide sequencing plus structural/deep intronic variant analysis**, because standard exon-focused approaches can miss causative alleles (tsygankova2022expandingthegenetic pages 1-2).

## References (URLs and publication dates where available)
The report citations above include DOI URLs and months/years extracted from the retrieved full texts and records, including:
- Lasio et al., *Molecular Genetics and Metabolism* (Jun 2023): https://doi.org/10.1016/j.ymgme.2023.107605 (lasio2023clinicalbiochemicaland pages 1-3)
- Xue, *Frontiers in Endocrinology* (Jul 2023): https://doi.org/10.3389/fendo.2023.1199590 (xue2023casereportprenatal pages 1-2)
- Maryami et al., *Iranian Biomedical Journal* (Sep 2023): https://doi.org/10.61186/ibj.27.5.307 (maryami2023insilicoanalysis pages 1-2)
- Jasinge et al., *Advances in Laboratory Medicine* (Jan 2024): https://doi.org/10.1515/almed-2023-0102 (jasinge2024clinicalbiochemicaland pages 1-2)
- Bernhardt et al., *JIMD Reports* (published 2024; accepted 2023-12-05; Dec 2024 issue listed): https://doi.org/10.1002/jmd2.12405 (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2)
- NCT01461304 (posted 2011-10-28; updated 2021-12-10): ClinicalTrials.gov record as retrieved (NCT01461304 chunk 1)



References

1. (lasio2023clinicalbiochemicaland pages 1-3): M. Laura Duque Lasio, Angela C. Leshinski, Nicole H. Ducich, Leigh Anne Flore, April Lehman, Natasha Shur, Parul B. Jayakar, Bryan E. Hainline, Alice A. Basinger, William G. Wilson, George A. Diaz, Richard W. Erbe, Dwight D. Koeberl, Jerry Vockley, and Jirair K. Bedoyan. Clinical, biochemical and molecular characterization of 12 patients with pyruvate carboxylase deficiency treated with triheptanoin. Molecular Genetics and Metabolism, 139:107605, Jun 2023. URL: https://doi.org/10.1016/j.ymgme.2023.107605, doi:10.1016/j.ymgme.2023.107605. This article has 5 citations and is from a peer-reviewed journal.

2. (marinvalencia2010pyruvatecarboxylasedeficiency pages 1-2): Isaac Marin-Valencia, Charles R. Roe, and Juan M. Pascual. Pyruvate carboxylase deficiency: mechanisms, mimics and anaplerosis. Molecular genetics and metabolism, 101 1:9-17, Sep 2010. URL: https://doi.org/10.1016/j.ymgme.2010.05.004, doi:10.1016/j.ymgme.2010.05.004. This article has 150 citations and is from a peer-reviewed journal.

3. (bernhardt2024pyruvatecarboxylasedeficiency pages 1-2): I. Bernhardt, L. Van Dorp, M. Dixon, M. McSweeney, C. Gan, J. Baruteau, and A. Chakrapani. Pyruvate carboxylase deficiency type c; variable presentation and beneficial effect of triheptanoin. JIMD Reports, 65:10-16, Dec 2024. URL: https://doi.org/10.1002/jmd2.12405, doi:10.1002/jmd2.12405. This article has 3 citations and is from a peer-reviewed journal.

4. (xue2023casereportprenatal pages 1-2): Mei Xue. Case report: prenatal neurological injury in a neonate with pyruvate carboxylase deficiency type b. Frontiers in Endocrinology, Jul 2023. URL: https://doi.org/10.3389/fendo.2023.1199590, doi:10.3389/fendo.2023.1199590. This article has 5 citations.

5. (jasinge2024clinicalbiochemicaland pages 2-4): Eresha Jasinge, Mihika Fernando, Neluwa-Liyanage Ruwan Indika, Pyara Dilani Ratnayake, Nalin Gamaathige, Ratnanathan Ratnaranjith, Sabine Schroeder, Patricia Jones, Skrahina Volha, Subhashinie Jayasena, Anusha Varuni Gunaratna, Asitha Niroshana Bandara Ekanayake, and Arndt Rolfs. Clinical, biochemical, and molecular profiles of three sri lankan neonates with pyruvate carboxylase deficiency. Advances in Laboratory Medicine, 5:205-212, Jan 2024. URL: https://doi.org/10.1515/almed-2023-0102, doi:10.1515/almed-2023-0102. This article has 0 citations.

6. (lasio2023clinicalbiochemicaland pages 9-11): M. Laura Duque Lasio, Angela C. Leshinski, Nicole H. Ducich, Leigh Anne Flore, April Lehman, Natasha Shur, Parul B. Jayakar, Bryan E. Hainline, Alice A. Basinger, William G. Wilson, George A. Diaz, Richard W. Erbe, Dwight D. Koeberl, Jerry Vockley, and Jirair K. Bedoyan. Clinical, biochemical and molecular characterization of 12 patients with pyruvate carboxylase deficiency treated with triheptanoin. Molecular Genetics and Metabolism, 139:107605, Jun 2023. URL: https://doi.org/10.1016/j.ymgme.2023.107605, doi:10.1016/j.ymgme.2023.107605. This article has 5 citations and is from a peer-reviewed journal.

7. (mochel2005pyruvatecarboxylasedeficiency pages 1-2): Fanny Mochel, Pascale DeLonlay, Guy Touati, Henri Brunengraber, Renee P. Kinman, Daniel Rabier, Charles R. Roe, and Jean-Marie Saudubray. Pyruvate carboxylase deficiency: clinical and biochemical response to anaplerotic diet therapy. Molecular genetics and metabolism, 84 4:305-12, Apr 2005. URL: https://doi.org/10.1016/j.ymgme.2004.09.007, doi:10.1016/j.ymgme.2004.09.007. This article has 178 citations and is from a peer-reviewed journal.

8. (wang2008themolecularbasis pages 1-2): Dong Wang, Hong Yang, Kevin C. De Braganca, Jiesheng Lu, Ling Yu Shih, Paz Briones, Tim Lang, and Darryl C. De Vivo. The molecular basis of pyruvate carboxylase deficiency: mosaicism correlates with prolonged survival. Molecular genetics and metabolism, 95 1-2:31-8, Sep 2008. URL: https://doi.org/10.1016/j.ymgme.2008.06.006, doi:10.1016/j.ymgme.2008.06.006. This article has 51 citations and is from a peer-reviewed journal.

9. (NCT01461304 chunk 1): Jerry Vockley, MD, PhD. Compassionate Use of Triheptanoin (C7) for Inherited Disorders of Energy Metabolism. Jerry Vockley, MD, PhD. ClinicalTrials.gov Identifier: NCT01461304

10. (habarou2015pyruvatecarboxylasedeficiency pages 1-2): F. Habarou, A. Brassier, M. Rio, D. Chrétien, S. Monnot, V. Barbier, R. Barouki, J.P. Bonnefont, N. Boddaert, B. Chadefaux-Vekemans, L. Le Moyec, J. Bastin, C. Ottolenghi, and P. de Lonlay. Pyruvate carboxylase deficiency: an underestimated cause of lactic acidosis. Molecular Genetics and Metabolism Reports, 2:25-31, Mar 2015. URL: https://doi.org/10.1016/j.ymgmr.2014.11.001, doi:10.1016/j.ymgmr.2014.11.001. This article has 32 citations.

11. (lasio2023clinicalbiochemicaland pages 3-4): M. Laura Duque Lasio, Angela C. Leshinski, Nicole H. Ducich, Leigh Anne Flore, April Lehman, Natasha Shur, Parul B. Jayakar, Bryan E. Hainline, Alice A. Basinger, William G. Wilson, George A. Diaz, Richard W. Erbe, Dwight D. Koeberl, Jerry Vockley, and Jirair K. Bedoyan. Clinical, biochemical and molecular characterization of 12 patients with pyruvate carboxylase deficiency treated with triheptanoin. Molecular Genetics and Metabolism, 139:107605, Jun 2023. URL: https://doi.org/10.1016/j.ymgme.2023.107605, doi:10.1016/j.ymgme.2023.107605. This article has 5 citations and is from a peer-reviewed journal.

12. (xue2023casereportprenatal pages 5-7): Mei Xue. Case report: prenatal neurological injury in a neonate with pyruvate carboxylase deficiency type b. Frontiers in Endocrinology, Jul 2023. URL: https://doi.org/10.3389/fendo.2023.1199590, doi:10.3389/fendo.2023.1199590. This article has 5 citations.

13. (tsygankova2022expandingthegenetic pages 1-2): Polina Tsygankova, Igor Bychkov, Marina Minzhenkova, Natalia Pechatnikova, Lyudmila Bessonova, Galina Buyanova, Irina Naumchik, Nikita Beskorovainiy, Vyacheslav Tabakov, Yulia Itkis, Nadezhda Shilova, and Ekaterina Zakharova. Expanding the genetic spectrum of the pyruvate carboxylase deficiency with novel missense, deep intronic and structural variants. Molecular Genetics and Metabolism Reports, 32:100889, Sep 2022. URL: https://doi.org/10.1016/j.ymgmr.2022.100889, doi:10.1016/j.ymgmr.2022.100889. This article has 3 citations.

14. (jasinge2024clinicalbiochemicaland pages 1-2): Eresha Jasinge, Mihika Fernando, Neluwa-Liyanage Ruwan Indika, Pyara Dilani Ratnayake, Nalin Gamaathige, Ratnanathan Ratnaranjith, Sabine Schroeder, Patricia Jones, Skrahina Volha, Subhashinie Jayasena, Anusha Varuni Gunaratna, Asitha Niroshana Bandara Ekanayake, and Arndt Rolfs. Clinical, biochemical, and molecular profiles of three sri lankan neonates with pyruvate carboxylase deficiency. Advances in Laboratory Medicine, 5:205-212, Jan 2024. URL: https://doi.org/10.1515/almed-2023-0102, doi:10.1515/almed-2023-0102. This article has 0 citations.

15. (maryami2023insilicoanalysis pages 1-2): Fereshteh Maryami, Elham Rismani, Elham Davoudi-Dehaghani, Nasrin Khalesi, Saeed Talebi, Reza Mahdian, and Sirous Zeinali. In silico analysis of two novel variants in the pyruvate carboxylase (pc) gene associated with the severe form of pc deficiency. Iranian Biomedical Journal, 27:307-319, Sep 2023. URL: https://doi.org/10.61186/ibj.27.5.307, doi:10.61186/ibj.27.5.307. This article has 3 citations.

16. (maryami2023insilicoanalysis pages 2-4): Fereshteh Maryami, Elham Rismani, Elham Davoudi-Dehaghani, Nasrin Khalesi, Saeed Talebi, Reza Mahdian, and Sirous Zeinali. In silico analysis of two novel variants in the pyruvate carboxylase (pc) gene associated with the severe form of pc deficiency. Iranian Biomedical Journal, 27:307-319, Sep 2023. URL: https://doi.org/10.61186/ibj.27.5.307, doi:10.61186/ibj.27.5.307. This article has 3 citations.

17. (jasinge2024clinicalbiochemicaland pages 5-7): Eresha Jasinge, Mihika Fernando, Neluwa-Liyanage Ruwan Indika, Pyara Dilani Ratnayake, Nalin Gamaathige, Ratnanathan Ratnaranjith, Sabine Schroeder, Patricia Jones, Skrahina Volha, Subhashinie Jayasena, Anusha Varuni Gunaratna, Asitha Niroshana Bandara Ekanayake, and Arndt Rolfs. Clinical, biochemical, and molecular profiles of three sri lankan neonates with pyruvate carboxylase deficiency. Advances in Laboratory Medicine, 5:205-212, Jan 2024. URL: https://doi.org/10.1515/almed-2023-0102, doi:10.1515/almed-2023-0102. This article has 0 citations.

18. (habarou2015pyruvatecarboxylasedeficiency pages 2-3): F. Habarou, A. Brassier, M. Rio, D. Chrétien, S. Monnot, V. Barbier, R. Barouki, J.P. Bonnefont, N. Boddaert, B. Chadefaux-Vekemans, L. Le Moyec, J. Bastin, C. Ottolenghi, and P. de Lonlay. Pyruvate carboxylase deficiency: an underestimated cause of lactic acidosis. Molecular Genetics and Metabolism Reports, 2:25-31, Mar 2015. URL: https://doi.org/10.1016/j.ymgmr.2014.11.001, doi:10.1016/j.ymgmr.2014.11.001. This article has 32 citations.

19. (hidalgo2021auniquecase pages 4-5): Jessica Hidalgo, Leticia Campoverde, Juan Fernando Ortiz, Samir Ruxmohan, and Ahmed Eissa-Garcés. A unique case of pyruvate carboxylase deficiency. Cureus, May 2021. URL: https://doi.org/10.7759/cureus.15042, doi:10.7759/cureus.15042. This article has 10 citations.