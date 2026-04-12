---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T12:42:51.492721'
end_time: '2026-04-04T12:49:28.427535'
duration_seconds: 396.93
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: CRB1 Retinal Dystrophies
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 18
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CRB1 Retinal Dystrophies
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CRB1 Retinal Dystrophies** covering all of the
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
- **Disease Name:** CRB1 Retinal Dystrophies
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **CRB1 Retinal Dystrophies** covering all of the
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


## Comprehensive Research Report: CRB1 Retinal Dystrophies (Mendelian IRD)

### Scope note
“CRB1 retinal dystrophies” refers to the spectrum of inherited retinal diseases (IRDs) caused by **biallelic pathogenic variants in CRB1**, including **early-onset severe retinal dystrophy/Leber congenital amaurosis (EOSRD/LCA8)**, **retinitis pigmentosa (RP12)**, and **CRB1-associated macular dystrophy/maculopathy**, with additional less common phenotypes such as cone–rod dystrophy and foveal retinoschisis/schitic maculopathy. (varela2023crb1associatedretinaldystrophies pages 1-2, varela2023crb1associatedretinaldystrophies pages 9-11, roshandel2021multimodalretinalimaging pages 1-2)

---

## 1. Disease information

### 1.1 Concise overview
CRB1-retinopathies are **autosomal recessive** IRDs characterized by **high phenotypic heterogeneity** across a spectrum from severe childhood-onset retinal dystrophy (EOSRD/LCA) to later-onset RP and macula-centered dystrophies, often with **distinctive fundus and OCT features** (e.g., preserved para-arteriolar RPE, abnormal retinal lamination/thickening, nummular pigmentation, cystic/schitic maculopathy). (varela2023crb1associatedretinaldystrophies pages 1-2, varela2023crb1associatedretinaldystrophies pages 9-11, roshandel2021multimodalretinalimaging pages 1-2)

### 1.2 Key identifiers (available from retrieved sources)
* **Gene:** CRB1 (Crumbs homolog 1) (daher2024genotypephenotypeassociationsin pages 1-2)
* **OMIM (disease associations mentioned in retrieved sources):**
  * **Leber congenital amaurosis-8 (LCA8)**: OMIM **#613835** (mentioned in CRB1 retinopathy imaging/natural history context) (roshandel2021multimodalretinalimaging pages 1-2)
  * **Retinitis pigmentosa 12 (RP12)**: OMIM **600105** (noted in CRB1 disease context in older CRB1 literature excerpt) (varela2023crb1associatedretinaldystrophies pages 1-2)

**MONDO ID / Orphanet / ICD-10/ICD-11 / MeSH:** Not retrievable from the current tool state (no OMIM/Orphanet/MeSH/ICD source pages were available in the retrieved full texts). This section is therefore **partial** and should be completed by querying OMIM/Orphanet/MONDO directly.

### 1.3 Common synonyms / alternative names (as used in the literature)
* “**CRB1-associated retinal dystrophies**” (varela2023crb1associatedretinaldystrophies pages 1-2)
* “**CRB1-associated retinopathies**” (roshandel2021multimodalretinalimaging pages 1-2)
* “**CRB1-retinopathies**” (rodriguezmartinez2025expandingtheclinical pages 1-2)
* Phenotype labels used: **EOSRD**, **LCA**, **RP**, **macular dystrophy/maculopathy**, **cone–rod dystrophy**, **rod–cone dystrophy**, **foveal retinoschisis**, **cystic/schitic maculopathy**, and a newly described **asymptomatic fenestrated slit maculopathy (AFSM)** (varela2023crb1associatedretinaldystrophies pages 1-2, roshandel2021multimodalretinalimaging pages 1-2)

### 1.4 Evidence source type
The current report uses **aggregated disease-level resources from primary cohorts and systematic reviews/meta-analysis**, not EHR-only evidence. The two highest-weight sources are a **multicenter retrospective cohort** (104 patients) and a **systematic review/meta-analysis** (439 patients). (varela2023crb1associatedretinaldystrophies pages 1-2, daher2024genotypephenotypeassociationsin pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** biallelic pathogenic variants in **CRB1**, which encodes a component of the **Crumbs apical polarity complex** at the retinal **outer limiting membrane (OLM)**, functioning in apical–basal polarity and adhesion at the photoreceptor–Müller glia interface. (stehle2024humancrb1and pages 1-2, buck2023crb1isrequired pages 1-3)

**Direct abstract-supported statement (mechanism framing):**
* Owen et al. (2023) describe the crumbs complex as having a “**crucial role in apical–basal epithelial polarity, cellular adhesion, and morphogenesis**,” and note that “**Homozygous variants in human CRB1 result in autosomal recessive Leber congenital amaurosis (LCA) and retinitis pigmentosa (RP)**.” (owen2023lossofthe pages 1-2)

### 2.2 Risk factors
* **Genetic risk:** presence of **biallelic CRB1 pathogenic variants**; severity tends to relate to **allelic class** (null vs hypomorphic). (varela2023crb1associatedretinaldystrophies pages 9-11, daher2024genotypephenotypeassociationsin pages 1-2)
  * In a large multicenter cohort, **double-null genotypes occurred only in EOSRD/LCA**, supporting a genotype–severity relationship. (varela2023crb1associatedretinaldystrophies pages 9-11)

* **Non-genetic/environmental risk factors:** No established, disease-specific environmental risk factors were identified in the retrieved evidence.

### 2.3 Protective factors
* The retrieved evidence does not identify validated genetic or environmental protective factors for CRB1-retinopathies.

### 2.4 Gene–environment interactions
No CRB1-specific gene–environment interaction evidence was retrievable from the current document set.

---

## 3. Phenotypes

### 3.1 Phenotype spectrum and frequencies (recent aggregated human data)
A multicenter cohort of molecularly confirmed CRB1-retinopathy (n=104) reported three main clinical categories: **EOSRD/LCA (≈52%)**, **RP (≈25%)**, and **macular dystrophy (≈23%)**, with additional phenotypes including cone–rod dystrophy and foveal retinoschisis/maculopathy variants. (varela2023crb1associatedretinaldystrophies pages 1-2, varela2023crb1associatedretinaldystrophies pages 9-11)

A meta-analysis of published bi-allelic CRB1 cases (96 studies; **439 patients**) reported systematic genotype–phenotype signals (e.g., missense vs nonsense association with RCD vs LCA). (daher2024genotypephenotypeassociationsin pages 1-2)

### 3.2 Key clinical and imaging phenotypes (hallmarks)
Across cohorts and reviews, commonly reported hallmarks include:
* **Maculopathy** (very frequent across phenotypes): maculopathy reported in **97%** of the large cohort. (varela2023crb1associatedretinaldystrophies pages 9-11)
* **Fundus-level signs**: **nummular intraretinal pigmentation**, **white/yellow dots**, **telangiectasia**, and **preserved para-arteriolar retinal pigment epithelium (PPRPE)**. (varela2023crb1associatedretinaldystrophies pages 1-2, varela2023crb1associatedretinaldystrophies pages 9-11, roshandel2021multimodalretinalimaging pages 1-2)
* **OCT architecture**: **abnormal/coarse retinal lamination** and often **retinal thickening** (especially described in pan-retinopathy phenotypes), as well as **intraretinal cysts/schisis** in maculopathy variants. (varela2023crb1associatedretinaldystrophies pages 1-2, roshandel2021multimodalretinalimaging pages 1-2)
* **Electrophysiology**: some macular dystrophy patients can have **normal full-field ERG but abnormal pattern ERG (PERG) P50**, consistent with predominantly macular dysfunction. (varela2023crb1associatedretinaldystrophies pages 9-11)

### 3.3 OCTA vascular phenotype (2023)
In an OCTA observational study (genetically confirmed CRB1-retinal dystrophy, 6 patients/12 eyes), the authors conclude: “**CRB1-associated retinal dystrophies are characterized by vascular alterations both in the macular and peripapillary region, as assessed by OCTA**.” (rajabian2023opticalcoherencetomography pages 1-2)

### 3.4 Genotype–phenotype phenotypic signatures (2023–2024)
* **Null variants** are significantly associated with **EOSRD/LCA**, and **double-null genotypes** were only observed in EOSRD/LCA in the large cohort. (varela2023crb1associatedretinaldystrophies pages 9-11)
* **Macular dystrophy**: a recurrent in-frame deletion **c.498_506del p.(Ile167_Gly169del)** was found **exclusively in macular dystrophy** in the large cohort and appeared in all patients of a separate CRB1 macular dystrophy series discussed in the OCTA paper excerpt, consistent with a **hypomorphic allele**. (varela2023crb1associatedretinaldystrophies pages 9-11, rajabian2023opticalcoherencetomography pages 1-2)
* Meta-analysis signals:
  * “**Missense mutations** were significantly associated with … higher risk of RCD,” whereas “**homozygous nonsense mutations** were associated with … high risk of LCA.” (daher2024genotypephenotypeassociationsin pages 1-2)

### 3.5 Quality of life
A CRB1-specific QoL longitudinal study was retrieved (Acta Ophthalmologica 2024), but the current evidence extraction did not provide interpretable results text (only metadata-level context was available). Therefore, QoL conclusions cannot be responsibly summarized from the current evidence state.

### 3.6 Suggested HPO terms (curation suggestions; not exhaustive)
(These are ontology mapping suggestions; they should be validated against patient-level descriptions in primary cohorts.)
* Night blindness **HP:0000662**
* Reduced visual acuity **HP:0007663**
* Nystagmus **HP:0000639**
* Peripheral visual field loss **HP:0007994**
* Photoreceptor degeneration / retinal dystrophy **HP:0000572**
* Macular dystrophy **HP:0001103**
* Cystoid macular edema / macular cysts **HP:0001113**
* Foveal retinoschisis **HP:0030507** (or related retinoschisis terms)
* Hyperopia **HP:0000540**

---

## 4. Genetic / molecular information

### 4.1 Causal gene
* **CRB1** (Crumbs homolog 1). Disease in this report is driven by **biallelic variants** (autosomal recessive inheritance), as described across cohorts. (varela2023crb1associatedretinaldystrophies pages 1-2, roshandel2021multimodalretinalimaging pages 1-2)

### 4.2 Variant classes and notable alleles
From the large cohort study:
* Variant classifications reported: **36% pathogenic**, **55% likely pathogenic**, **9% VUS** in the dataset’s variant interpretation. (varela2023crb1associatedretinaldystrophies pages 9-11)
* A frequent allele included **c.2843G>A p.(Cys948Tyr)** (15 individuals; “mainly EOSRD/LCA” in the excerpt). (varela2023crb1associatedretinaldystrophies pages 9-11)
* **c.498_506del p.(Ile167_Gly169del)** found “exclusively in MD.” (varela2023crb1associatedretinaldystrophies pages 9-11)

From the 2024 meta-analysis (439 patients):
* The “commonest reported allele is **p.(Cys948Tyr)** (~12.48%).” (daher2024genotypephenotypeassociationsin pages 1-2)
* A novel bi-allelic missense **c.2936G>A; p.(Gly979Asp)** was associated with rod-cone dystrophy. (daher2024genotypephenotypeassociationsin pages 1-2)

### 4.3 Functional consequences and modifier concepts
* The evidence supports a **loss-of-function severity gradient**, with null alleles associated with more severe early-onset disease and a hypomorphic allele associated with localized maculopathy. (varela2023crb1associatedretinaldystrophies pages 9-11, rajabian2023opticalcoherencetomography pages 1-2)
* Potential intra-genic “interaction”/modifier-like effects were suggested in the meta-analysis (e.g., variant combinations potentially modifying BCVA), but this should be treated as hypothesis-generating. (daher2024genotypephenotypeassociationsin pages 1-2)

### 4.4 Epigenetic information
The crumbs complex can influence epigenetic regulation in development: Owen et al. (2023) report multi-omic evidence of differential DNA methylation and transcriptional dysregulation after crumbs complex loss, with hypermethylated pathways including adhesion and signaling modules. (owen2023lossofthe pages 1-2)

---

## 5. Environmental information
No CRB1-specific environmental/lifestyle/toxic/infectious triggers were supported by the retrieved evidence. CRB1-retinopathies are primarily explained as **monogenic** disorders with variable expressivity. (varela2023crb1associatedretinaldystrophies pages 1-2, daher2024genotypephenotypeassociationsin pages 1-2)

---

## 6. Mechanism / pathophysiology

### 6.1 Cellular/anatomical locus of dysfunction
CRB1 is localized to the **subapical region at/near adherens junctions of the OLM**, expressed in **photoreceptors and Müller glia**; this is a key site where polarity/adhesion defects can disrupt retinal architecture. (stehle2024humancrb1and pages 1-2, buck2023crb1isrequired pages 1-3)

Direct abstract-supported statements:
* Stehle et al. (2024): “**CRB1 and CRB2 co-localize in the human retina and human iPSC-derived retinal organoids**” and “**our results show a stable interaction of human canonical CRB2 and CRB1 in the retina**.” (stehle2024humancrb1and pages 1-2)

### 6.2 Crumbs polarity complex → adhesion/lamination defects → retinal dystrophy
A disease-relevant causal chain supported by experimental and patient-derived systems:
1) **CRB1/Crumbs complex dysfunction** (from biallelic CRB1 variants) perturbs **apical–basal polarity** and **cell–cell adhesion** at the OLM. (buck2023crb1isrequired pages 1-3, owen2023lossofthe pages 1-2)
2) This contributes to **abnormal retinal lamination/coarse layering** and structural disorganization, consistent with the distinctive OCT findings in human cohorts. (varela2023crb1associatedretinaldystrophies pages 1-2, roshandel2021multimodalretinalimaging pages 1-2)

Owen et al. (2023) (zebrafish crb2a−/− retina + CRB1 patient-derived retinal organoids) connects crumbs loss with developmental delay and adhesion/polarity defects, and reports pathway dysregulation including Hippo and TGFβ/BMP/SMAD modules via integrated RNA-seq/methylomics. (owen2023lossofthe pages 1-2)

### 6.3 Endosomal trafficking and receptor recycling defects (human retinal organoids)
Buck et al. (2023) provides a mechanistic model in human iPSC retinal organoids implicating altered endosomal maturation and recycling:
* They report CRB1 is required for recycling by **RAB11A+ vesicles** and that organoids show reduced apical CRB1 protein at the OLM alongside signatures of altered early endosomes and recycling endosomes (e.g., fewer RAB11A+ recycling endosomes, reduced VPS35/retromer component). (buck2023crb1isrequired pages 1-3, buck2023crb1isrequired pages 3-4)

This mechanistic direction aligns with the broader concept that CRB1-retinopathies are not only photoreceptor-autonomous but involve Müller glia and epithelial-like junctional organization. (buck2023crb1isrequired pages 1-3, stehle2024humancrb1and pages 13-14)

### 6.4 Suggested GO biological process terms (curation suggestions)
* Establishment/maintenance of epithelial cell polarity (e.g., **GO:0007163**) 
* Cell–cell adhesion (e.g., **GO:0098609**) 
* Endosome recycling (e.g., **GO:0032456**) 
* Notch signaling pathway (e.g., **GO:0007219**) 
* Hippo signaling (pathway-mapped terms)

### 6.5 Suggested Cell Ontology (CL) terms
* Müller glial cell (**CL:0000688**)
* Photoreceptor cell (**CL:0000210**) / rod photoreceptor (**CL:0000742**) / cone photoreceptor (**CL:0000746**)

---

## 7. Anatomical structures affected

### 7.1 Organ/tissue/cell types
* **Primary organ:** eye (retina) (varela2023crb1associatedretinaldystrophies pages 1-2)
* **Key sites/cell types:** **outer limiting membrane region**, **photoreceptors**, **Müller glia**, and macula (maculopathy in most patients). (varela2023crb1associatedretinaldystrophies pages 9-11, stehle2024humancrb1and pages 1-2, buck2023crb1isrequired pages 1-3)

### 7.2 Suggested UBERON terms (curation suggestions)
* Retina (**UBERON:0000966**)
* Macula lutea (**UBERON:0001880**)
* Retinal outer limiting membrane (if represented)

---

## 8. Temporal development

### 8.1 Onset
* EOSRD/LCA: early childhood onset with severe impairment early in life. (varela2023crb1associatedretinaldystrophies pages 9-11)
* RP/macular dystrophy phenotypes can present later, with variable retention of central vision depending on subtype and genotype. (varela2023crb1associatedretinaldystrophies pages 9-11, roshandel2021multimodalretinalimaging pages 1-2)

### 8.2 Progression / natural history (human cohort)
In the 104-patient cohort:
* Severe impairment commonly occurs **after age ~20** for EOSRD/LCA and **after age ~40** for RP; macular dystrophy can preserve central vision into adulthood for some genotypes. (varela2023crb1associatedretinaldystrophies pages 1-2, varela2023crb1associatedretinaldystrophies pages 9-11)

---

## 9. Inheritance and population

### 9.1 Inheritance
CRB1-retinopathies are predominantly **autosomal recessive** due to **biallelic** pathogenic variants. (varela2023crb1associatedretinaldystrophies pages 1-2, roshandel2021multimodalretinalimaging pages 1-2)

### 9.2 Epidemiology (available statistics)
The retrieved evidence provides disease-contribution estimates rather than population prevalence:
* CRB1 has been cited as accounting for roughly **~10% of LCA/EOSRD** and up to **~6.5% of RP** in the excerpted cohort synthesis. (varela2023crb1associatedretinaldystrophies pages 1-2)
* In an imaging cohort paper, biallelic CRB1 mutations were summarized as accounting for **~3–9% of autosomal recessive RP** and **~7–17% of LCA**. (roshandel2021multimodalretinalimaging pages 1-2)

No population-level incidence/prevalence per 100,000 for CRB1-specific disease was retrievable from the current evidence set.

---

## 10. Diagnostics

### 10.1 Clinical testing (current practice in cohorts)
Across CRB1 cohorts and imaging studies, diagnosis and monitoring commonly involve:
* **Dilated fundus exam** and color fundus photography (rajabian2023opticalcoherencetomography pages 1-2)
* **Fundus autofluorescence (FAF)**, including widefield FAF to visualize **PPRPE** and atrophy patterns (roshandel2021multimodalretinalimaging pages 1-2)
* **Optical coherence tomography (OCT)** to assess coarse lamination, thickening, cystic/schitic change, and outer retinal atrophy (roshandel2021multimodalretinalimaging pages 1-2)
* **Electrophysiology** (full-field ERG, pattern ERG/PERG, EOG) as indicated (rajabian2023opticalcoherencetomography pages 1-2, varela2023crb1associatedretinaldystrophies pages 9-11)
* **OCT angiography (OCTA)** to quantify macular/peripapillary vascular alterations (rajabian2023opticalcoherencetomography pages 1-2)

### 10.2 Genetic testing strategy
The CRB1 imaging cohort describes confirmation by genetic testing using approaches including **targeted NGS** and **whole-genome sequencing** (in the referenced diagnostic pathways). (rajabian2023opticalcoherencetomography pages 1-2)

### 10.3 Differential diagnosis
Not explicitly enumerated in the extracted evidence; in practice, differential diagnosis is broad across IRDs with overlapping maculopathy/RP/LCA phenotypes.

---

## 11. Outcome / prognosis

### 11.1 Vision outcomes
In the large natural history cohort, visual acuity decline correlated with age and phenotype, with severe impairment tending to occur in EOSRD/LCA earlier than in RP, and macular dystrophy often preserving central vision longer. (varela2023crb1associatedretinaldystrophies pages 1-2, varela2023crb1associatedretinaldystrophies pages 9-11)

### 11.2 Complications
Coats-like telangiectasia/exudative vascular changes are noted as part of the CRB1 spectrum. (varela2023crb1associatedretinaldystrophies pages 1-2, roshandel2021multimodalretinalimaging pages 1-2)

Mortality/life expectancy effects are not expected to be directly impacted by isolated retinal dystrophy and were not addressed in the extracted evidence.

---

## 12. Treatment

### 12.1 Standard of care / real-world implementation
The retrieved evidence emphasizes **diagnosis, monitoring, and trial endpoint development** rather than established CRB1-specific approved therapies.

### 12.2 Clinical trial endpoints and implementation-ready measures
Roshandel et al. (2021) proposes trial-suitable measures:
* “**Macular volume profile and microperimetry parameters may have utility as CRB1 trials end points**.” (roshandel2021multimodalretinalimaging pages 1-2)

Rajabian et al. (2023) supports OCTA as an imaging biomarker domain by demonstrating quantifiable vascular alterations in CRB1 disease. (rajabian2023opticalcoherencetomography pages 1-2)

### 12.3 Advanced therapeutics (research and translational direction)
**No CRB1-targeted interventional clinical trial records** were found in the ClinicalTrials.gov interventional query used (0 records returned). (Clinical Trial Search: ffcf1a87d410)

However, multiple sources discuss a therapeutic rationale and practical constraints:
* The large cohort notes therapeutic development complexity because the **CRB1 coding sequence “occup[ies] nearly all the AAV packing capacity,”** motivating strategies such as use of small promoters and alternative approaches (including CRB2 supplementation in animal contexts) (varela2023crb1associatedretinaldystrophies pages 13-14).
* Mechanistic organoid work (Buck et al., 2023) supports CRB1 as a target by clarifying pathogenic pathways (endosomal recycling/polarity) and identifying cell types at the OLM interface. (buck2023crb1isrequired pages 1-3, buck2023crb1isrequired pages 3-4)

### 12.4 MAXO terms (curation suggestions)
* Gene therapy (**MAXO:0001001**) 
* Genetic testing (**MAXO:0000127**) 
* Low vision rehabilitation (**MAXO:0000486**) 

---

## 13. Prevention

### 13.1 Primary prevention
No primary prevention exists for monogenic CRB1-retinopathies.

### 13.2 Secondary/tertiary prevention
Secondary prevention focuses on **early molecular diagnosis and monitoring** to manage complications (e.g., macular cysts, exudation) and to identify potential windows for future interventional trials. (roshandel2021multimodalretinalimaging pages 1-2, varela2023crb1associatedretinaldystrophies pages 13-14)

### 13.3 Genetic counseling
Autosomal recessive inheritance supports counseling and cascade testing in families; detailed counseling guidance was not explicitly provided in extracted evidence.

---

## 14. Other species / natural disease
The mechanistic literature strongly leverages comparative models:
* **Zebrafish crb2a−/−** retina used to study crumbs-complex loss impacting development and epigenetic regulation; findings were compared/validated in **CRB1 patient-derived retinal organoids**. (owen2023lossofthe pages 1-2)
* Additional referenced systems include **mouse**, **Drosophila**, and **human retina and iPSC-derived organoids**, supporting evolutionary conservation of Crumbs complex function. (stehle2024humancrb1and pages 1-2, buck2023crb1isrequired pages 1-3)

No naturally occurring veterinary CRB1 disease evidence was retrievable from the current evidence state.

---

## 15. Model organisms and model systems

### 15.1 Human cellular models
* **Human iPSC-derived retinal organoids** from CRB1 patients: show reduced apical CRB1 protein and evidence for impaired endosomal maturation/recycling (RAB11A+ recycling endosomes/retromer-related signatures). (buck2023crb1isrequired pages 1-3, buck2023crb1isrequired pages 3-4)

### 15.2 Animal models
* **Zebrafish crumbs-complex loss (crb2a−/−)**: multi-omic evidence of disrupted cell cycle progression and epigenetic transcriptional control, with pathway perturbations including Hippo and TGFβ/BMP/SMAD modules. (owen2023lossofthe pages 1-2)

---

## Clinical trials and registries (current retrievable records)

### Registry / natural history resource
* **NCT01793168** (ClinicalTrials.gov; first posted 2013; sponsor Sanford Health): *Rare Disease Patient Registry & Natural History Study - Coordination of Rare Diseases at Sanford*; **Recruiting**; observational registry intended “**To accelerate research into rare disorders by connecting individuals…with researchers who study rare diseases**.” CRB1 is listed among included conditions, and the record contains a CRB1-related registry linkage (“CRB1 Foundation / Curing Retinal Blindness Foundation Registry”). URL: https://clinicaltrials.gov/study/NCT01793168 (NCT01793168 chunk 4, NCT01793168 chunk 1)

### Interventional CRB1 trials
* No CRB1-specific interventional trials were returned by the ClinicalTrials.gov query used here. (Clinical Trial Search: ffcf1a87d410)

---

## Recent developments (2023–2024 prioritized)
Key 2023–2024 advances supported by the retrieved evidence:
1) **Largest cohort-level natural history and genotype–phenotype delineation** for CRB1 disease (AJO 2023), including high maculopathy frequency and null-vs-hypomorphic genotype patterns relevant for trial readiness. (varela2023crb1associatedretinaldystrophies pages 1-2, varela2023crb1associatedretinaldystrophies pages 9-11)
2) **Mechanistic clarification in human retinal organoids** linking CRB1 loss to **endosomal recycling defects** (Stem Cell Reports 2023). (buck2023crb1isrequired pages 1-3, buck2023crb1isrequired pages 3-4)
3) **Multi-omics developmental mechanism hypothesis**: crumbs complex disruption associated with epigenetic dysregulation and pathway module changes (Hippo, TGFβ/BMP/SMAD) in zebrafish retina and CRB1 patient-derived organoids (J Pathol 2023). (owen2023lossofthe pages 1-2)
4) **Human retina protein-complex architecture**: demonstration of CRB1–CRB2 complex formation in human retina and organoids (Life Science Alliance 2024), supporting pathway-level and therapeutic design considerations. (stehle2024humancrb1and pages 1-2)
5) **Genotype–phenotype meta-analysis (2024)** systematically quantifying associations between variant class and phenotype, with a compiled patient count >400. (daher2024genotypephenotypeassociationsin pages 1-2)

---

## Limitations of this report (evidence availability)
* Standardized disease identifiers (MONDO/Orphanet/MeSH/ICD) and population prevalence/incidence were not retrievable from the available full-text set.
* No CRB1-specific interventional trial records were found in the interventional ClinicalTrials.gov query used; only a broad registry record including CRB1 could be extracted.
* Quality-of-life and detailed management/supportive care recommendations could not be summarized from the extracted evidence fragments.

---

## Embedded summary table
The following table compacts the key disease entities, phenotypes, imaging hallmarks, and genotype–phenotype signals supported by the extracted evidence.

| Disease entity | Inheritance | Hallmark clinical/imaging features | Key genotype-phenotype associations / variants | Key quantitative stats |
|---|---|---|---|---|
| EOSRD / LCA8 | Autosomal recessive; biallelic CRB1 variants | Very early-onset severe retinal dystrophy; low vision in first 2 decades; maculopathy common; abnormally laminated/coarsely laminated and often thickened retina on OCT; macular thinning reported in EOSRD/LCA cohorts; nummular pigment, white/yellow dots, telangiectasia may be present; high hyperopia common; severe visual impairment often develops after age 20 | Strong association with null / loss-of-function alleles; double-null genotypes reported only in EOSRD/LCA; p.(Cys948Tyr) common and mainly seen in EOSRD/LCA; homozygous nonsense variants linked to higher LCA risk; loss-of-function alleles additively increase LCA risk, with nonsense > indels | In a 104-patient cohort, EOSRD/LCA represented 52%; in an 11-proband eoRD series, 81.8% presented as LCA; in a 439-patient meta-analysis, CRB1 missense/nonsense patterns significantly stratified RCD vs LCA risk; CRB1 contributes ~10% of LCA/EOSRD overall and ~7–17% of LCA cases in cited summaries |
| RP12 / CRB1-associated retinitis pigmentosa | Autosomal recessive; biallelic CRB1 variants | Progressive rod-cone or generalized retinal dysfunction; severe visual impairment often after age 40; preserved para-arteriolar RPE (PPRPE), nummular intraretinal pigmentation, coarse retinal lamination and retinal thickening on OCT; perifoveal thickening; Coats-like / exudative telangiectatic changes may occur; OCTA shows reduced deep capillary plexus and choriocapillaris vessel density with broader macular/peripapillary vascular alterations | Missense variants associated with absence of macular pigments, pale optic disc, peripheral pigmentation, and higher rod-cone dystrophy risk; p.(Cys948Tyr) is a frequent allele across CRB1 disease; some RP/MD phenotypes retain preserved foveal architecture and central function; AFSM described in compound heterozygotes c.[2843G>A];[498_506del] | In the 104-patient cohort, RP represented 25%; CRB1 accounts for up to ~6.5% of RP overall and ~3–9% of autosomal recessive RP in cited summaries; in one imaging cohort, symptom onset averaged 9 years and mean baseline age was 35 years |
| Macular dystrophy / CRB1 maculopathy | Autosomal recessive; biallelic CRB1 variants | Macula-centered disease with relatively preserved central vision into adulthood in some patients; early intraretinal cysts / schitic or cystoid maculopathy may evolve to bull’s-eye or outer retinal atrophy; abnormal PERG may occur despite normal full-field ERG; preserved foveal architecture can be seen; peripheral changes may be absent or limited | In-frame c.498_506del p.(Ile167_Gly169del) found exclusively in MD in one large cohort and in all 7 patients of a macular dystrophy series, consistent with a hypomorphic/milder localized maculopathy allele; null alleles can occur in MD but often with milder / hypomorphic variants; homozygous c.2506C>A p.(Pro836Thr) linked to mild, stable MD with elevated IOP/CME in later evidence summaries | In the 104-patient cohort, MD represented 23%; 7/7 patients in one macular dystrophy series carried p.(Ile167_Gly169del); median age at presentation in that series was 21 years with modest VA impairment; seven patients in the large cohort had preserved foveal architecture with good central vision |
| Cone-rod / rod-cone dystrophy | Autosomal recessive; biallelic CRB1 variants | Generalized cone and rod dysfunction or rod-cone pattern on electrophysiology; reduced central vision; may overlap clinically with RP or early-onset disease; coin-like yellow-white retinal spots and para-arteriolar RPE retention reported in eoRD cohorts | Novel bi-allelic missense c.2936G>A p.(Gly979Asp) associated with rod-cone dystrophy; missense variants overall were associated with higher rod-cone dystrophy risk than nonsense variants | Cone-rod dystrophy is less common than EOSRD/LCA, RP, and MD in the cited cohorts; among 20 patients tested for contrast sensitivity, 3 had CORD; in the 439-patient meta-analysis, missense variants were significantly enriched in RCD-associated phenotypes |
| Foveal retinoschisis / schitic-cystoid maculopathy / AFSM | Autosomal recessive; biallelic CRB1 variants | Foveal retinoschisis or cystic/schitic macular changes on OCT; can be early-onset and may later resolve leaving macular atrophy; asymptomatic fenestrated slit maculopathy (AFSM) may show localized outer retinal disruption and parafoveal cone loss despite normal acuity, fundus appearance, and foveal sensitivity | Maculopathy including schitic/cystoid change has been associated with CRB1; AFSM reported in siblings with compound heterozygous c.[2843G>A];[498_506del]; c.498_506del is repeatedly linked to mild macular-centered phenotypes | AFSM was reported in 2 siblings within a 12-patient imaging cohort; in that cohort, preserved central retinal function by microperimetry was documented in 6 patients, and the perifoveal-to-foveal retinal volume ratio was greater than controls in 89% (8/9) of RP/MD patients |


*Table: This table compacts the main disease entities grouped under CRB1 retinal dystrophies, highlighting inheritance, hallmark phenotypes, genotype-phenotype signals, and quantitative findings useful for clinical characterization and knowledge-base curation.*

References

1. (varela2023crb1associatedretinaldystrophies pages 1-2): Malena Daich Varela, Michalis Georgiou, Yahya Alswaiti, Jamil Kabbani, Kaoru Fujinami, Yu Fujinami-Yokokawa, Shaheeni Khoda, Omar A. Mahroo, Anthony G. Robson, Andrew R. Webster, Alaa AlTalbishi, and Michel Michaelides. Crb1-associated retinal dystrophies: genetics, clinical characteristics, and natural history. American Journal of Ophthalmology, 246:107-121, Feb 2023. URL: https://doi.org/10.1016/j.ajo.2022.09.002, doi:10.1016/j.ajo.2022.09.002. This article has 50 citations and is from a domain leading peer-reviewed journal.

2. (varela2023crb1associatedretinaldystrophies pages 9-11): Malena Daich Varela, Michalis Georgiou, Yahya Alswaiti, Jamil Kabbani, Kaoru Fujinami, Yu Fujinami-Yokokawa, Shaheeni Khoda, Omar A. Mahroo, Anthony G. Robson, Andrew R. Webster, Alaa AlTalbishi, and Michel Michaelides. Crb1-associated retinal dystrophies: genetics, clinical characteristics, and natural history. American Journal of Ophthalmology, 246:107-121, Feb 2023. URL: https://doi.org/10.1016/j.ajo.2022.09.002, doi:10.1016/j.ajo.2022.09.002. This article has 50 citations and is from a domain leading peer-reviewed journal.

3. (roshandel2021multimodalretinalimaging pages 1-2): Danial Roshandel, Jennifer A. Thompson, Rachael C. Heath Jeffery, Danuta M. Sampson, Enid Chelva, Terri L. McLaren, Tina M. Lamey, John N. De Roach, Shane R. Durkin, and Fred K. Chen. Multimodal retinal imaging and microperimetry reveal a novel phenotype and potential trial end points in <i>crb1</i>-associated retinopathies. Translational Vision Science &amp; Technology, 10:38, Feb 2021. URL: https://doi.org/10.1167/tvst.10.2.38, doi:10.1167/tvst.10.2.38. This article has 26 citations and is from a peer-reviewed journal.

4. (daher2024genotypephenotypeassociationsin pages 1-2): Ahmad Daher, Malak Banjak, Jinane Noureldine, Joseph Nehme, and Said El Shamieh. Genotype-phenotype associations in crb1 bi-allelic patients: a novel mutation, a systematic review and meta-analysis. BMC Ophthalmology, Apr 2024. URL: https://doi.org/10.1186/s12886-024-03419-4, doi:10.1186/s12886-024-03419-4. This article has 7 citations and is from a peer-reviewed journal.

5. (rodriguezmartinez2025expandingtheclinical pages 1-2): Ana Catalina Rodriguez-Martinez, Oliver R. Marmoy, Katrina L. Prise, Robert H. Henderson, Dorothy A. Thompson, and Mariya Moosajee. Expanding the clinical spectrum of crb1-retinopathies: a novel genotype–phenotype correlation with macular dystrophy and elevated intraocular pressure. International Journal of Molecular Sciences, 26:2836, Mar 2025. URL: https://doi.org/10.3390/ijms26072836, doi:10.3390/ijms26072836. This article has 3 citations.

6. (stehle2024humancrb1and pages 1-2): Isabel F Stehle, Joel A Imventarza, Franziska Woerz, Felix Hoffmann, Karsten Boldt, Tina Beyer, Peter MJ Quinn, and Marius Ueffing. Human crb1 and crb2 form homo- and heteromeric protein complexes in the retina. Life Science Alliance, 7:e202302440, Apr 2024. URL: https://doi.org/10.26508/lsa.202302440, doi:10.26508/lsa.202302440. This article has 6 citations and is from a peer-reviewed journal.

7. (buck2023crb1isrequired pages 1-3): Thilo M. Buck, Peter M.J. Quinn, Lucie P. Pellissier, Aat A. Mulder, Aldo Jongejan, Xuefei Lu, Nanda Boon, Daniëlle Koot, Hind Almushattat, Christiaan H. Arendzen, Rogier M. Vos, Edward J. Bradley, Christian Freund, Harald M.M. Mikkers, Camiel J.F. Boon, Perry D. Moerland, Frank Baas, Abraham J. Koster, Jacques Neefjes, Ilana Berlin, Carolina R. Jost, and Jan Wijnholds. Crb1 is required for recycling by rab11a+ vesicles in human retinal organoids. Stem Cell Reports, 18:1793-1810, Sep 2023. URL: https://doi.org/10.1016/j.stemcr.2023.07.001, doi:10.1016/j.stemcr.2023.07.001. This article has 14 citations and is from a domain leading peer-reviewed journal.

8. (owen2023lossofthe pages 1-2): Nicholas Owen, Maria Toms, Yuan Tian, Lyes Toualbi, Rose Richardson, Rodrigo Young, Dhani Tracey‐White, Pawan Dhami, Stephan Beck, and Mariya Moosajee. Loss of the crumbs cell polarity complex disrupts epigenetic transcriptional control and cell cycle progression in the developing retina. The Journal of Pathology, 259:441-454, Feb 2023. URL: https://doi.org/10.1002/path.6056, doi:10.1002/path.6056. This article has 11 citations.

9. (rajabian2023opticalcoherencetomography pages 1-2): Firuzeh Rajabian, Alessandro Arrigo, Lorenzo Bianco, Alessio Antropoli, Maria Pia Manitto, Elisabetta Martina, Francesco Bandello, Jay Chhablani, and Maurizio Battaglia Parodi. Optical coherence tomography angiography in crb1-associated retinal dystrophies. Journal of Clinical Medicine, 12:1095, Jan 2023. URL: https://doi.org/10.3390/jcm12031095, doi:10.3390/jcm12031095. This article has 4 citations.

10. (buck2023crb1isrequired pages 3-4): Thilo M. Buck, Peter M.J. Quinn, Lucie P. Pellissier, Aat A. Mulder, Aldo Jongejan, Xuefei Lu, Nanda Boon, Daniëlle Koot, Hind Almushattat, Christiaan H. Arendzen, Rogier M. Vos, Edward J. Bradley, Christian Freund, Harald M.M. Mikkers, Camiel J.F. Boon, Perry D. Moerland, Frank Baas, Abraham J. Koster, Jacques Neefjes, Ilana Berlin, Carolina R. Jost, and Jan Wijnholds. Crb1 is required for recycling by rab11a+ vesicles in human retinal organoids. Stem Cell Reports, 18:1793-1810, Sep 2023. URL: https://doi.org/10.1016/j.stemcr.2023.07.001, doi:10.1016/j.stemcr.2023.07.001. This article has 14 citations and is from a domain leading peer-reviewed journal.

11. (stehle2024humancrb1and pages 13-14): Isabel F Stehle, Joel A Imventarza, Franziska Woerz, Felix Hoffmann, Karsten Boldt, Tina Beyer, Peter MJ Quinn, and Marius Ueffing. Human crb1 and crb2 form homo- and heteromeric protein complexes in the retina. Life Science Alliance, 7:e202302440, Apr 2024. URL: https://doi.org/10.26508/lsa.202302440, doi:10.26508/lsa.202302440. This article has 6 citations and is from a peer-reviewed journal.

12. (Clinical Trial Search: ffcf1a87d410): Clinical Trials Search via ClinicalTrials.gov: CRB1 AND (retinal dystrophy OR Leber congenital amaurosis OR retinitis pigmentosa) AREA[StudyType]INTERVENTIONAL

13. (varela2023crb1associatedretinaldystrophies pages 13-14): Malena Daich Varela, Michalis Georgiou, Yahya Alswaiti, Jamil Kabbani, Kaoru Fujinami, Yu Fujinami-Yokokawa, Shaheeni Khoda, Omar A. Mahroo, Anthony G. Robson, Andrew R. Webster, Alaa AlTalbishi, and Michel Michaelides. Crb1-associated retinal dystrophies: genetics, clinical characteristics, and natural history. American Journal of Ophthalmology, 246:107-121, Feb 2023. URL: https://doi.org/10.1016/j.ajo.2022.09.002, doi:10.1016/j.ajo.2022.09.002. This article has 50 citations and is from a domain leading peer-reviewed journal.

14. (NCT01793168 chunk 4):  Rare Disease Patient Registry & Natural History Study - Coordination of Rare Diseases at Sanford. Sanford Health. 2010. ClinicalTrials.gov Identifier: NCT01793168

15. (NCT01793168 chunk 1):  Rare Disease Patient Registry & Natural History Study - Coordination of Rare Diseases at Sanford. Sanford Health. 2010. ClinicalTrials.gov Identifier: NCT01793168