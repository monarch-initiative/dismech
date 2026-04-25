---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T16:24:24.524702'
end_time: '2026-04-04T16:35:04.760747'
duration_seconds: 640.24
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Schistosomiasis
  mondo_id: ''
  category: Infectious Disease
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
- **Disease Name:** Schistosomiasis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Schistosomiasis** covering all of the
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
- **Disease Name:** Schistosomiasis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Schistosomiasis** covering all of the
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


# Schistosomiasis — Disease Characteristics Research Report (2023–2024 prioritized)

## Executive summary
Schistosomiasis is a neglected tropical disease (NTD) caused by trematodes of the genus *Schistosoma*. Human infection occurs when cercariae released from freshwater snails penetrate the skin during water contact, followed by maturation of worms in the vasculature and egg deposition in tissues; much of the morbidity is driven by egg-induced inflammation and granulomatous pathology. Recent 2024 reviews and meta-analyses emphasize (i) the persistent global burden (≈250M people needing preventive therapy), (ii) the diagnostic transition needed for elimination (antigen and molecular tests outperform egg microscopy in low-intensity settings), and (iii) expansion of preventive chemotherapy (praziquantel) strategies, including development of a pediatric formulation (arpraziquantel) and programs to address female genital schistosomiasis (FGS). (ponzo2024insightsintothe pages 1-2, ponzo2024insightsintothe pages 2-3, chatterji2024arecentadvance pages 2-3, vaillant2024diagnostictestsfor pages 4-4, alemu2024efficacyandsafety pages 1-2, masaku2024communitypreferreddrug pages 1-2)


| Domain | Key finding (with quantitative values) | Population/Setting | Year | Source (first author) | URL/DOI |
|---|---|---|---|---|---|
| Epidemiology/Transmission | Schistosomiasis is transmitted when eggs shed in urine/feces hatch to miracidia that infect freshwater snails; released cercariae penetrate human skin. Review states the disease affects “more than 250 million people” and causes “approximately 70 million DALYs.” (ponzo2024insightsintothe pages 1-2, ponzo2024insightsintothe pages 2-3) | Global overview; Africa, South America, Asia | 2024 | Ponzo | https://doi.org/10.1556/1886.2024.00013 |
| Epidemiology/Transmission | Review reports that “globally in 2021, schistosomiasis affected around 251.4 million individuals who are in requirement of preventive therapy,” with 75.3 million treated; COVID-19 disruptions caused “a 27% decrease in treatment coverage.” (chatterji2024arecentadvance pages 2-3) | Global WHO-era control context | 2024 | Chatterji | https://doi.org/10.3390/tropicalmed9100243 |
| Diagnostics | Systematic review/meta-analysis: for *S. mansoni*, CCA1 pooled sensitivity 95% (95% CrI 88–99) and specificity 74% (63–83); CAA pooled sensitivity 90% (86–93) and specificity 95% (91–98). (vaillant2024diagnostictestsfor pages 4-4) | Multi-study latent-class/meta-analysis across endemic settings | 2024 | Vaillant | https://doi.org/10.1016/S2666-5247(23)00377-4 |
| Treatment/Control | In 110 school-aged children completing follow-up, praziquantel cure rate (CR) by Kato-Katz was 88.2% (95% CI 82.7–93.6) and egg reduction rate (ERR) 93.5% (85.4–98.5); POC-CCA-based CR was 70.9% or 75.5% depending on trace interpretation. At least one adverse event occurred in 23.6%; abdominal pain 10.0%, nausea 7.3%, headache 5.5%, anorexia 2.7%; all mild. (alemu2024efficacyandsafety pages 1-2) | School-aged children with *S. mansoni*, Amhara Region, Ethiopia | 2024 | Alemu | https://doi.org/10.1371/journal.pone.0298332 |
| Treatment/Control | Prospective cohort of 512 infected schoolchildren: overall praziquantel cure rates were 89.1% at week 4 and 87.5% at week 8; ERRs were 93.5% and 91.3%, respectively. At least one MDA-associated adverse event occurred in 17.0% (95% CI 13.8–20.5%); abdominal pain, headache, and vomiting were most common. (gebreyesus2023efficacyandsafety pages 1-2) | *S. mansoni*-infected schoolchildren, Southern Ethiopia | 2023 | Gebreyesus | https://doi.org/10.3389/fphar.2023.968106 |
| Treatment/Control | Mixed-methods implementation study found community-based MDA (cMDA) was preferred by 598/690 participants (86.7%), followed by health facility/fixed points 398/690 (57.7%); respondents were mostly women 594/690 (86.1%). Preference for cMDA reflected trust in community health volunteers and convenience of home delivery. (masaku2024communitypreferreddrug pages 1-2) | Parents/guardians of preschool-aged children in 8 villages, two endemic counties, Kenya | 2024 | Masaku | https://doi.org/10.1371/journal.pgph.0003221 |
| Treatment/Control | Qualitative study in hard-to-reach island/fishing communities found main risk factors were lake water exposure and open defecation; barriers included health-system, population-level, and geographic inaccessibility. Door-to-door distribution by community health promoters was identified as the most feasible arpraziquantel delivery platform. (isaiah2024contextualfactorsinfluencing pages 1-2) | Fishermen and island populations, Homa Bay County, Kenya | 2024 | Isaiah | https://doi.org/10.1371/journal.pgph.0004035 |
| FGS | Phase 2 randomized trial: 116 women (58 repeated-dose, 58 single-dose); 95 included in per-protocol analysis. There was a minor, non-significant reduction in cervical lesions in both arms at week 15; CAA positivity and mean CAA fell significantly in both groups, more so with repeated dosing. Mild-to-moderate adverse events occurred in equal proportions. ClinicalTrials.gov identifier NCT04115072. (arenholt2024repeatedversussingle pages 1-2) | Women aged 15–34 with FGS-associated cervical lesions, northern Madagascar | 2024 | Arenholt | https://doi.org/10.3389/fitd.2024.1322652 |
| FGS | Cross-sectional Malawi study: visual-FGS prevalence 26.9% (260/967), molecular-FGS prevalence 8.2% (78/942), and egg-patent urinary infection 6.5% (38/584). Molecular-FGS associated with visual-FGS (AOR 2.9, 95% CI 1.7–5.0) and egg-patent infection (AOR 7.5, 95% CI 3.27–17.2). (lamberti2024femalegenitalschistosomiasis pages 1-2) | Sexually active women aged 15–65 in two *S. haematobium*-endemic districts, Southern Malawi | 2024 | Lamberti | https://doi.org/10.1371/journal.pntd.0012102 |


*Table: This table compiles high-yield 2023–2024 evidence across epidemiology, diagnostics, treatment/control, and female genital schistosomiasis. It is useful as a quick-reference summary of quantitative findings and implementation-relevant results with traceable citations.*

## 1. Disease information
### 1.1 What is schistosomiasis?
Schistosomiasis is a parasitic disease caused by blood-dwelling flukes of the genus *Schistosoma* (trematodes). A 2024 review describes it as “a neglected tropical disease” prevalent in low- and middle-income countries and caused by trematodes of the genus *Schistosoma*. (ponzo2024insightsintothe pages 1-2)

**Transmission cycle (current understanding):** Eggs shed in urine or feces hatch into miracidia that infect freshwater snails (intermediate hosts). Infected snails release cercariae, which penetrate human skin during freshwater exposure; schistosomula migrate and mature, and adults produce eggs that drive pathology and sustain transmission. (ponzo2024insightsintothe pages 1-2, ponzo2024insightsintothe pages 2-3, chatterji2024arecentadvance pages 2-3)

**Clinical forms:** disease is commonly described as intestinal/hepatic versus urogenital schistosomiasis, with acute manifestations (e.g., cercarial dermatitis; Katayama syndrome) and chronic, egg-driven granulomatous disease leading to fibrosis and organ damage. (ponzo2024insightsintothe pages 2-3, chatterji2024arecentadvance pages 5-8, chatterji2024arecentadvance pages 3-5)

### 1.2 Key identifiers (requested)
Curated ontology/terminology identifiers (MONDO ID, MeSH descriptor ID, ICD-10/ICD-11 codes, Orphanet ID, OMIM) were **not retrievable from the current tool evidence** in this run; therefore they are **not reported here** to avoid uncited assertions.

### 1.3 Synonyms / alternative names
Commonly used synonym: **bilharzia / bilharziasis** (used in contemporary literature describing human schistosomiasis). (hameister2023prevalenceofschistosoma pages 10-14)

### 1.4 Evidence provenance (individual vs aggregated)
This report is derived from **aggregated disease-level resources** (reviews and systematic reviews/meta-analyses), **programmatic studies**, and **clinical/field studies** in endemic settings. (chatterji2024arecentadvance pages 2-3, vaillant2024diagnostictestsfor pages 4-4, alemu2024efficacyandsafety pages 1-2, masaku2024communitypreferreddrug pages 1-2)


## 2. Etiology
### 2.1 Disease causal factors
**Causal agent:** infection with *Schistosoma* spp. trematodes; major human species include *S. haematobium*, *S. mansoni*, and *S. japonicum* (with additional human-infecting species in some regions). (ponzo2024insightsintothe pages 1-2, alemu2024efficacyandsafety pages 1-2)

**Mechanistic cause of pathology:** egg trapping in tissues, causing inflammatory/granulomatous responses and subsequent fibrosis (central for chronic hepatosplenic and urogenital complications). (chatterji2024arecentadvance pages 5-8)

### 2.2 Risk factors (human, environmental, behavioral)
**Freshwater exposure** in endemic settings (e.g., bathing, swimming, washing, fishing) and **poor sanitation** drive transmission by enabling eggs to reach freshwater and infect snail hosts. (ponzo2024insightsintothe pages 1-2, chatterji2024arecentadvance pages 2-3)

**Hard-to-reach, lake-associated communities:** a 2024 qualitative study in Homa Bay County (Lake Victoria islands/fishing communities) reports “Lake water and open defecation were the main predisposing factors to infection,” with additional barriers of “inaccessibility of quality healthcare services” due to health system, population-level, and geographic factors. (isaiah2024contextualfactorsinfluencing pages 1-2)

### 2.3 Protective factors
No specific genetic protective variants or quantified protective environmental factors were identified in the retrieved evidence during this run; key protective strategies described in 2023–2024 sources focus on **integrated public health interventions** (preventive chemotherapy plus WASH, snail control, and education). (menezes2023fioschisto’sexpertperspective pages 1-2)

### 2.4 Gene–environment interactions
Human host genetic susceptibility/protection and explicit gene–environment interactions were **not captured** in the retrieved evidence.


## 3. Phenotypes
Schistosomiasis phenotypes depend on infecting species, worm burden, tissue egg deposition sites, and duration of infection.

### 3.1 Acute schistosomiasis
A 2024 review describes acute manifestations including cercarial dermatitis and Katayama syndrome with systemic and gastrointestinal/urogenital symptoms (e.g., fever, abdominal pain/diarrhea, myalgia, haematuria). (ponzo2024insightsintothe pages 2-3)

**Suggested HPO terms (non-exhaustive):**
- Fever (HP:0001945)
- Abdominal pain (HP:0002027)
- Diarrhea (HP:0002014)
- Myalgia (HP:0003326)
- Hematuria (HP:0000790)

### 3.2 Chronic intestinal/hepatosplenic schistosomiasis
A 2024 review notes chronic egg-driven complications including hepatic fibrosis and portal hypertension with organomegaly and intestinal manifestations (abdominal pain, diarrhea, blood in stool). (ponzo2024insightsintothe pages 2-3, strachinaru2024schistosomiasisinthe pages 7-8)

**Suggested HPO terms (non-exhaustive):**
- Hepatic fibrosis (HP:0001395)
- Portal hypertension (HP:0001404)
- Hepatomegaly (HP:0002240)
- Splenomegaly (HP:0001744)
- Gastrointestinal hemorrhage / blood in stool (e.g., HP:0002242 for melena; context-specific)

### 3.3 Chronic urogenital schistosomiasis
Urogenital disease includes haematuria, bladder fibrosis, kidney damage, and increased bladder cancer risk; a 2024 review also notes WHO/IARC carcinogenic classification context for *S. haematobium*. (ponzo2024insightsintothe pages 1-2, ponzo2024insightsintothe pages 2-3)

**Suggested HPO terms (non-exhaustive):**
- Hematuria (HP:0000790)
- Dysuria (HP:0100511)
- Hydronephrosis / kidney damage (HP:0000126 for hydronephrosis; depending on manifestation)

### 3.4 Female genital schistosomiasis (FGS)
FGS is a chronic manifestation of *S. haematobium* egg deposition in the genital tract and may mimic STIs and cervical cancer.

- A 2024 WHO-atlas co-design paper states: “Up to 56 million young and adult women of African origin suffer from Female Genital Schistosomiasis (FGS)” and “There is currently no gold standard for FGS diagnosis.” (martinez2024thewhoatlas pages 1-2)
- In Southern Malawi, visual-FGS prevalence was 26.9% (260/967) and molecular-FGS 8.2% (78/942); egg-patent urinary infection was 6.5% (38/584), illustrating that genital disease burden can be substantial even when urinary egg-patency is low. (lamberti2024femalegenitalschistosomiasis pages 1-2)

**Suggested HPO terms (non-exhaustive; symptom overlap with STI syndromes is common):**
- Pelvic pain (HP:0002027 used for abdominal pain; pelvic pain specific term may be used if available in HPO)
- Postcoital bleeding (term availability may vary)
- Vaginal discharge (HP:0031648)


## 4. Genetic / molecular information
### 4.1 Causal genes
Schistosomiasis is **not a monogenic human disorder**; it is an infectious disease. No human causal genes (OMIM-style) are applicable.

### 4.2 Parasite molecular targets relevant to treatment (mechanistic anchor)
A 2024 review notes that praziquantel’s long-uncertain target has recently been clarified, highlighting a parasite TRPM ion channel (TRPM\_PZQ) as a therapeutic target. (isaiah2024contextualfactorsinfluencing pages 1-2)

### 4.3 Epigenetic information / chromosomal abnormalities
No human epigenetic or chromosomal abnormality evidence was retrieved; parasite omics and non-coding RNAs were outside the scope of the extracted evidence in this run.


## 5. Environmental information
Key environmental determinants are those enabling snail habitats and human freshwater contact.

- Freshwater bodies supporting intermediate host snails are essential for transmission; cercariae released from snails infect humans via skin penetration. (ponzo2024insightsintothe pages 1-2, ponzo2024insightsintothe pages 2-3)
- In lake-shore/island settings, open defecation and routine lake water contact were highlighted as predisposing factors. (isaiah2024contextualfactorsinfluencing pages 1-2)


## 6. Mechanism / pathophysiology
### 6.1 Causal chain (upstream → downstream)
1. **Exposure:** cercariae released by infected freshwater snails in endemic waters. (ponzo2024insightsintothe pages 1-2, ponzo2024insightsintothe pages 2-3)
2. **Entry:** cercariae penetrate human skin during water contact. (ponzo2024insightsintothe pages 1-2, ponzo2024insightsintothe pages 2-3)
3. **Maturation:** schistosomula migrate and mature to adult worms in the vasculature. (ponzo2024insightsintothe pages 2-3, chatterji2024arecentadvance pages 5-8)
4. **Egg deposition:** adults lay eggs; some are excreted to continue lifecycle, others become trapped in tissues. (chatterji2024arecentadvance pages 5-8, strachinaru2024schistosomiasisinthe pages 7-8)
5. **Immunopathology:** trapped eggs provoke inflammation and granulomas; chronicity drives fibrosis (e.g., periportal fibrosis, portal hypertension; bladder/genital tract fibrosis). (ponzo2024insightsintothe pages 2-3, strachinaru2024schistosomiasisinthe pages 7-8)

### 6.2 Immune involvement (high-level)
A 2024 modelling-focused review summarizes stage-dependent T-helper polarization (Th1/Th17-like responses early vs Th2-dominant responses to ova in chronic infection). (chatterji2024arecentadvance pages 2-3)

**Suggested GO biological process terms (examples):**
- Inflammatory response (GO:0006954)
- Granuloma formation (not always a GO term; can be represented via immune/inflammatory processes)
- Collagen fibril organization (GO:0030199)
- Extracellular matrix organization (GO:0030198)

**Suggested Cell Ontology (CL) cell types (examples):**
- Macrophage (CL:0000235)
- CD4-positive, alpha-beta T cell (CL:0000624)
- Eosinophil (CL:0000771)

### 6.3 Tissue damage mechanisms
Chronic disease is described as egg-induced “inflammatory and granulomatous responses” leading to organ fibrosis and complications (e.g., portal hypertension; urogenital fibrosis). (ponzo2024insightsintothe pages 2-3)


## 7. Anatomical structures affected
### 7.1 Organ level (major)
- **Intestinal/hepatic system:** liver, portal vasculature; hepatosplenic complications with fibrosis/portal hypertension. (ponzo2024insightsintothe pages 2-3, strachinaru2024schistosomiasisinthe pages 7-8)
- **Urogenital system:** bladder, urinary tract; kidney damage; increased bladder cancer risk. (ponzo2024insightsintothe pages 1-2)
- **Female genital tract (FGS):** cervix/vaginal tissues with characteristic lesions; clinical overlap with cervical cancer/STIs. (arenholt2024repeatedversussingle pages 1-2, martinez2024thewhoatlas pages 1-2)

**Suggested UBERON terms (examples):**
- Liver (UBERON:0002107)
- Spleen (UBERON:0002106)
- Urinary bladder (UBERON:0001255)
- Uterine cervix (UBERON:0000002)


## 8. Temporal development
- **Onset pattern:** exposure-related; acute symptoms can occur after infection (e.g., Katayama syndrome), while chronic disease develops over years with repeated exposure and egg-driven fibrosis. (ponzo2024insightsintothe pages 2-3, chatterji2024arecentadvance pages 3-5)
- **FGS lesion persistence:** a 2024 randomized trial suggests established FGS-associated cervical lesions may be refractory to praziquantel even with repeated dosing, supporting the importance of early-life prevention. (arenholt2024repeatedversussingle pages 1-2)


## 9. Inheritance and population
### 9.1 Epidemiology and burden (recently cited)
- A 2024 review states schistosomiasis affects “more than 250 million people” and “approximately 70 million DALYs.” (ponzo2024insightsintothe pages 1-2)
- A 2024 review reports that “globally in 2021, schistosomiasis affected around 251.4 million individuals who are in requirement of preventive therapy,” with 75.3 million treated and a “27% decrease in treatment coverage” during COVID-19 disruptions. (chatterji2024arecentadvance pages 2-3)

**Geographic distribution:** burden concentrated in Africa, South America, and Asia in contemporary reviews. (ponzo2024insightsintothe pages 1-2)

### 9.2 Genetic inheritance (not applicable)
Schistosomiasis is an infectious disease and does not follow Mendelian inheritance.


## 10. Diagnostics (2023–2024 emphasis)
### 10.1 Standard parasitology (gold standard but sensitivity-limited)
Microscopy-based egg detection remains widely used (Kato–Katz for stool; urine filtration for urogenital schistosomiasis) but has low sensitivity in low-intensity infections, which becomes limiting for elimination programs. (ally2024schistosomiasisdiagnosischallenges pages 4-6, ally2024schistosomiasisdiagnosischallenges pages 3-4)

### 10.2 Antigen detection (CCA/CAA) — major recent development
A 2024 systematic review/meta-analysis provides quantitative performance estimates:
- **CCA1 (POC-CCA) for *S. mansoni*:** pooled sensitivity 95% (95% CrI 88–99) and specificity 74% (63–83) in latent-class analysis. (vaillant2024diagnostictestsfor pages 4-4)
- **CAA:** sensitivity 90% (86–93) and specificity 95% (91–98) versus Kato–Katz. (vaillant2024diagnostictestsfor pages 4-4)

**Programmatic interpretation caution:** In a 2024 Ethiopia cohort, praziquantel cure rate differed markedly by test: 88.2% by Kato–Katz vs 70.9–75.5% by POC-CCA depending on interpretation of “trace” results, underscoring the operational importance of test choice and result interpretation. (alemu2024efficacyandsafety pages 1-2)

### 10.3 Molecular tests (PCR / cfDNA) and REASSURED direction
A 2024 review summarizes expanding use of NAATs (PCR, qPCR, LAMP/RPA) for low-burden settings, but notes constraints including equipment and workflow complexity. (ally2024schistosomiasisdiagnosischallenges pages 4-6, ally2024schistosomiasisdiagnosischallenges pages 6-7)

### 10.4 FGS diagnosis (no gold standard)
A 2024 WHO-atlas paper emphasizes diagnostic uncertainty and misclassification risk: “There is currently no gold standard for FGS diagnosis,” and misdiagnosis may lead to “wrong treatment” and reproductive health harms. (martinez2024thewhoatlas pages 1-2)


## 11. Outcome / prognosis
Quantitative survival/life expectancy estimates were not retrieved in this run. However, reviewed sources emphasize that chronic infection can lead to irreversible organ damage (hepatic fibrosis/portal hypertension; urinary tract damage; cancer risk) and substantial disability burden. (ponzo2024insightsintothe pages 1-2, ponzo2024insightsintothe pages 2-3)


## 12. Treatment
### 12.1 Pharmacotherapy: praziquantel (PZQ)
Praziquantel remains the cornerstone of preventive chemotherapy and case management.

**Recent efficacy and safety data (human cohorts):**
- Ethiopia (2023 prospective cohort, *S. mansoni*, n=512): cure rates 89.1% (week 4) and 87.5% (week 8); ERR 93.5% and 91.3%; adverse events in 17.0% (95% CI 13.8–20.5%), mostly mild-to-moderate, with abdominal pain/headache/vomiting common. (gebreyesus2023efficacyandsafety pages 1-2)
- Ethiopia (2024 cohort, n=110 completing follow-up): cure rate 88.2% and ERR 93.5% by Kato–Katz; adverse events in 23.6% and all mild (abdominal pain 10.0%, nausea 7.3%, headache 5.5%, anorexia 2.7%). (alemu2024efficacyandsafety pages 1-2)

**MAXO (suggested):**
- Anthelmintic therapy (MAXO term concept)
- Mass drug administration / preventive chemotherapy (MAXO term concept)

**CHEBI (suggested):**
- Praziquantel (CHEBI identifier not retrieved in this run; not asserted)

### 12.2 Pediatric formulation: arpraziquantel (arPZQ) and implementation science
**Rationale:** a 2024 Kenya study states that treating preschool-aged children has been challenging “due to lack of a pediatric formulation,” and describes a consortium-developed novel pediatric treatment option. (masaku2024communitypreferreddrug pages 1-2)

**Preferred delivery platforms (Kenya, 2024 mixed methods):**
- Community-based MDA (cMDA) preferred by 86.7% (598/690)
- Health facility/fixed points preferred by 57.7% (398/690)
Trust in community health volunteers (CHVs) and convenience of home delivery were key drivers; understaffing/overcrowding concerns were noted for facility delivery. (masaku2024communitypreferreddrug pages 1-2)

**Hard-to-reach settings:** In Lake Victoria island/fishing communities, door-to-door distribution by community health promoters was proposed as “the most promising platform” to deliver arPZQ, given barriers to health access and risk factors (lake water exposure, open defecation). (isaiah2024contextualfactorsinfluencing pages 1-2)

### 12.3 FGS treatment: repeated vs single-dose praziquantel (recent RCT)
A 2024 phase 2 randomized trial in northern Madagascar (ClinicalTrials.gov **NCT04115072**) compared repeated-dose vs single-dose praziquantel in women 15–34 with FGS-associated cervical lesions:
- Primary outcome: “A minor and insignificant reduction in cervical lesions” in both arms at week 15.
- Biomarkers: “The reduction in number of women testing positive for CAA and mean CAA values was significant in both arms but less so in the single-dose arm.”
- Safety: “Mild to moderate adverse events of equal proportions” in both arms.
- Conclusion emphasizes early-life initiation to prevent lesion establishment: “FGS-associated cervical lesions appear refractory to PZQ treatment even when this is administered in a repeated-dosing regimen.” (arenholt2024repeatedversussingle pages 1-2)


## 13. Prevention
### 13.1 Integrated control strategy (current consensus)
A 2023 expert perspective on implementing WHO guidelines emphasizes that elimination requires integrated interventions beyond chemotherapy. It states: “In Brazil, the provision of safe water and sanitation should be the key action to achieve schistosomiasis elimination goals,” and notes that MDA should be integrated with water/sanitation, education/communication (IEC), and snail control; praziquantel should be administered under medical supervision at the primary care level. (menezes2023fioschisto’sexpertperspective pages 1-2)

### 13.2 Primary prevention
- Reduce freshwater exposure to cercariae; improve water and sanitation to prevent egg contamination of freshwater. (ponzo2024insightsintothe pages 1-2, menezes2023fioschisto’sexpertperspective pages 1-2)

### 13.3 Secondary prevention
- Surveillance and screening using more sensitive diagnostics (CAA/CCA, molecular tools) to identify ongoing transmission, particularly in low-intensity settings. (vaillant2024diagnostictestsfor pages 4-4, ally2024schistosomiasisdiagnosischallenges pages 4-6)

### 13.4 Tertiary prevention
- Maintain preventive chemotherapy coverage and integrate with WASH/IEC/snail control to reduce reinfection and chronic sequelae. (vere2024effectsofpaediatric pages 15-17, menezes2023fioschisto’sexpertperspective pages 1-2)


## 14. Other species / natural disease
Zoonotic/hybrid schistosomes were referenced as emerging concerns in recent literature, but detailed taxonomy/reservoir statistics were not extracted in the evidence set for this run.


## 15. Model organisms
The retrieved evidence did not include detailed descriptions of laboratory model organisms; however, mechanistic and vaccine development pipelines commonly use murine and other experimental systems (not specifically cited in the extracted passages).


## Expert opinions and authoritative analysis (2023–2024)
- **WHO/implementation-focused expert consensus:** FioSchisto (Fiocruz) argues that safe water/sanitation and intersectoral action are central to elimination; MDA should be integrated and used selectively, with improved surveillance (two-stage immunological + molecular testing) to verify transmission interruption. (menezes2023fioschisto’sexpertperspective pages 1-2)
- **FGS clinical/public health expertise:** WHO-endorsed tools (Pocket Atlas, digital supports, e-learning) were co-designed to transfer scarce expert diagnostic knowledge for FGS into low-resource health systems, acknowledging lack of gold standard and risk of misdiagnosis with cervical cancer/STI syndromes. (martinez2024thewhoatlas pages 1-2)


## Real-world implementations and applications (examples from recent evidence)
- **School-based praziquantel MDA** is implemented nationally in Ethiopia since 2015; recent cohort studies evaluate efficacy/safety and highlight diagnostic-dependent cure-rate interpretation. (alemu2024efficacyandsafety pages 1-2)
- **Kenya implementation planning for pediatric arPZQ** is actively informed by community-preference studies (cMDA vs facility delivery) and hard-to-reach platform assessments (door-to-door). (isaiah2024contextualfactorsinfluencing pages 1-2, masaku2024communitypreferreddrug pages 1-2)
- **FGS clinical trials** are evaluating dosing strategies and biomarker endpoints (CAA, cervicovaginal DNA), with implications for prevention timing. (arenholt2024repeatedversussingle pages 1-2)


## Key statistics (recent)
- “More than 250 million people” infected (review-level estimate). (ponzo2024insightsintothe pages 1-2)
- “Globally in 2021… 251.4 million individuals… in requirement of preventive therapy” and 75.3 million treated; “27% decrease in treatment coverage” during COVID-19 disruptions. (chatterji2024arecentadvance pages 2-3)
- Diagnostic performance (meta-analysis): CCA1 sensitivity 95% / specificity 74% (for *S. mansoni*); CAA sensitivity 90% / specificity 95%. (vaillant2024diagnostictestsfor pages 4-4)
- PZQ efficacy (Ethiopia cohorts): cure ≈88–89%, ERR ≈91–94%; adverse events ≈17–24% (mostly mild/transient). (alemu2024efficacyandsafety pages 1-2, gebreyesus2023efficacyandsafety pages 1-2)
- Kenya pediatric delivery preference: cMDA preferred by 86.7% (598/690). (masaku2024communitypreferreddrug pages 1-2)
- Malawi FGS burden: visual-FGS 26.9% vs molecular-FGS 8.2% in adult women. (lamberti2024femalegenitalschistosomiasis pages 1-2)


## Notes on evidence limitations for knowledge base population
Several requested items (formal ontology IDs, granular phenotype frequencies across all organ systems, host genetic susceptibility loci, and model organism details) were not available in the retrieved tool evidence. They should be added via additional targeted retrieval from authoritative terminologies (MONDO, MeSH, ICD-11 browser, Orphanet) and host genetics resources.


References

1. (ponzo2024insightsintothe pages 1-2): Elena Ponzo, Angelina Midiri, Andrea Manno, Martina Pastorello, Carmelo Biondo, and Giuseppe Mancuso. Insights into the epidemiology, pathogenesis, and differential diagnosis of schistosomiasis. European Journal of Microbiology and Immunology, 14:86-96, May 2024. URL: https://doi.org/10.1556/1886.2024.00013, doi:10.1556/1886.2024.00013. This article has 45 citations.

2. (ponzo2024insightsintothe pages 2-3): Elena Ponzo, Angelina Midiri, Andrea Manno, Martina Pastorello, Carmelo Biondo, and Giuseppe Mancuso. Insights into the epidemiology, pathogenesis, and differential diagnosis of schistosomiasis. European Journal of Microbiology and Immunology, 14:86-96, May 2024. URL: https://doi.org/10.1556/1886.2024.00013, doi:10.1556/1886.2024.00013. This article has 45 citations.

3. (chatterji2024arecentadvance pages 2-3): Tanushri Chatterji, Namrata Khanna, Saad Alghamdi, Tanya Bhagat, Nishant Gupta, Mohammad Othman Alkurbi, Manodeep Sen, Saeed Mardy Alghamdi, Ghazi A. Bamagous, Dipak Kumar Sahoo, Ashish Patel, Pankaj Kumar, and Virendra Kumar Yadav. A recent advance in the diagnosis, treatment, and vaccine development for human schistosomiasis. Tropical Medicine and Infectious Disease, 9:243, Oct 2024. URL: https://doi.org/10.3390/tropicalmed9100243, doi:10.3390/tropicalmed9100243. This article has 12 citations.

4. (vaillant2024diagnostictestsfor pages 4-4): Michel T Vaillant, Fred Philippy, Anouk Neven, Jessica Barré, Dmitry Bulaev, Piero L Olliaro, Jürg Utzinger, Jennifer Keiser, and Amadou T Garba. Diagnostic tests for human schistosoma mansoni and schistosoma haematobium infection: a systematic review and meta-analysis. The Lancet Microbe, 5:e366-e378, Apr 2024. URL: https://doi.org/10.1016/s2666-5247(23)00377-4, doi:10.1016/s2666-5247(23)00377-4. This article has 52 citations.

5. (alemu2024efficacyandsafety pages 1-2): Getaneh Alemu, Arancha Amor, Endalkachew Nibret, Abaineh Munshea, and Melaku Anegagrie. Efficacy and safety of prazequantel for the treatment of schistosoma mansoni infection across different transmission settings in amhara regional state, northwest ethiopia. PLOS ONE, 19:e0298332, Mar 2024. URL: https://doi.org/10.1371/journal.pone.0298332, doi:10.1371/journal.pone.0298332. This article has 5 citations and is from a peer-reviewed journal.

6. (masaku2024communitypreferreddrug pages 1-2): Janet Masaku, John M. Gachohi, Alice Sinkeet, Mary Maghanga, Florence Wakesho, Wyckliff Omondi, Nora Monnier, Peter Steinmann, Lisa Sophie Reigl, Isabelle L. Lange, Andrea S. Winkler, Sammy M. Njenga, and Mary Amuyunzu-Nyamongo. Community preferred drug delivery approaches for pilot roll-out of a potential novel paediatric schistosomiasis treatment option in two endemic counties of kenya: a mixed methods study. PLOS Global Public Health, 4:e0003221, May 2024. URL: https://doi.org/10.1371/journal.pgph.0003221, doi:10.1371/journal.pgph.0003221. This article has 5 citations and is from a peer-reviewed journal.

7. (gebreyesus2023efficacyandsafety pages 1-2): Tigist Dires Gebreyesus, Eyasu Makonnen, Tafesse Tadele, Kalkidan Mekete, Habtamu Gashaw, Heran Gerba, and Eleni Aklillu. Efficacy and safety of praziquantel preventive chemotherapy in schistosoma mansoni infected school children in southern ethiopia: a prospective cohort study. Frontiers in Pharmacology, Mar 2023. URL: https://doi.org/10.3389/fphar.2023.968106, doi:10.3389/fphar.2023.968106. This article has 17 citations.

8. (isaiah2024contextualfactorsinfluencing pages 1-2): Phyllis Munyiva Isaiah, Doris Osei Afriyie, Mary Maghanga, Donna Obare Ogeto, Mary Amuyunzu Nyamongo, and Peter Steinmann. Contextual factors influencing schistosomiasis treatment and identification of delivery platforms for arpraziquantel in hard-to-reach areas and populations in homa bay county, kenya. PLOS Global Public Health, 4:e0004035, Dec 2024. URL: https://doi.org/10.1371/journal.pgph.0004035, doi:10.1371/journal.pgph.0004035. This article has 0 citations and is from a peer-reviewed journal.

9. (arenholt2024repeatedversussingle pages 1-2): Louise Thomsen Schmidt Arenholt, Bodo Sahondra Randrianasolo, Tiana Onintsoa Oliva Rabozakandraina, Charles Emile Ramarokoto, Karoline Jøker, Katrina Kæstel Aarøe, Dorthe Brønnum, Caspar Bundgaard Nielsen, Suzette Sørensen, Mads Lumholdt, Martin Jensen, Søren Lundbye-Christensen, Jørgen Skov Jensen, Paul Corstjens, Pytsje Hoekstra, Govert J van Dam, Noriko Kobayashi, Shinjiro Hamano, and Peter Derek Christian Leutscher. Repeated versus single praziquantel dosing regimen in treatment of female genital schistosomiasis: a phase 2 randomised controlled trial showing no difference in efficacy. Frontiers in Tropical Diseases, Aug 2024. URL: https://doi.org/10.3389/fitd.2024.1322652, doi:10.3389/fitd.2024.1322652. This article has 12 citations.

10. (lamberti2024femalegenitalschistosomiasis pages 1-2): Olimpia Lamberti, Sekeleghe Kayuni, Dingase Kumwenda, Bagrey Ngwira, Varsha Singh, Veena Moktali, Neerav Dhanani, Els Wessels, Lisette Van Lieshout, Fiona M. Fleming, Themba Mzilahowa, and Amaya L. Bustinduy. Female genital schistosomiasis burden and risk factors in two endemic areas in malawi nested in the morbidity operational research for bilharziasis implementation decisions (morbid) cross-sectional study. PLOS Neglected Tropical Diseases, 18:e0012102, May 2024. URL: https://doi.org/10.1371/journal.pntd.0012102, doi:10.1371/journal.pntd.0012102. This article has 16 citations and is from a domain leading peer-reviewed journal.

11. (chatterji2024arecentadvance pages 5-8): Tanushri Chatterji, Namrata Khanna, Saad Alghamdi, Tanya Bhagat, Nishant Gupta, Mohammad Othman Alkurbi, Manodeep Sen, Saeed Mardy Alghamdi, Ghazi A. Bamagous, Dipak Kumar Sahoo, Ashish Patel, Pankaj Kumar, and Virendra Kumar Yadav. A recent advance in the diagnosis, treatment, and vaccine development for human schistosomiasis. Tropical Medicine and Infectious Disease, 9:243, Oct 2024. URL: https://doi.org/10.3390/tropicalmed9100243, doi:10.3390/tropicalmed9100243. This article has 12 citations.

12. (chatterji2024arecentadvance pages 3-5): Tanushri Chatterji, Namrata Khanna, Saad Alghamdi, Tanya Bhagat, Nishant Gupta, Mohammad Othman Alkurbi, Manodeep Sen, Saeed Mardy Alghamdi, Ghazi A. Bamagous, Dipak Kumar Sahoo, Ashish Patel, Pankaj Kumar, and Virendra Kumar Yadav. A recent advance in the diagnosis, treatment, and vaccine development for human schistosomiasis. Tropical Medicine and Infectious Disease, 9:243, Oct 2024. URL: https://doi.org/10.3390/tropicalmed9100243, doi:10.3390/tropicalmed9100243. This article has 12 citations.

13. (hameister2023prevalenceofschistosoma pages 10-14): JR Hameister. Prevalence of schistosoma mansoni among children under one year in the central highlands of madagascar. Unknown journal, 2023.

14. (menezes2023fioschisto’sexpertperspective pages 1-2): Camilla Almeida Menezes, Langia Colli Montresor, Soraya Torres Gaze Jangola, Aline Carvalho de Mattos, Ana Lúcia Coutinho Domingues, Arnaldo Maldonado Júnior, Clélia Christina Mello Silva, Constança Simões Barbosa, Cristiane Lafetá Furtado de Mendonça, Cristiano Lara Massara, Cristina Toscano Fonseca, Edward José de Oliveira, Elainne Christine de Souza Gomes, Elizângela Feitosa da Silva, Fernando Schemelzer de Moraes Bezerra, Floriano Paes Silva-Jr, Isadora Cristina de Siqueira, José Roberto Machado e Silva, Leo Heller, Leonardo Paiva Farias, Lilian C. Nobrega Holsbach Beck, Mariana Cristina Silva Santos, Mariana Gomes Lima, Marina de Moraes Mourão, Martin Johannes Enk, Monica Ammon Fernandez, Naftale Katz, Omar dos Santos Carvalho, Patrícia Martins Parreiras, Renata Heisler Neves, Sandra Grossi Gava, Sheilla Andrade de Oliveira, Silvana Carvalho Thiengo, Tereza Cristina Favre, Carlos Graeff-Teixeira, Otávio Sarmento Pieri, Roberta Lima Caldeira, Rosiane A. da Silva-Pereira, Roberto Sena Rocha, and Ricardo Riccio Oliveira. Fioschisto’s expert perspective on implementing who guidelines for schistosomiasis control and transmission elimination in brazil. Frontiers in Immunology, Dec 2023. URL: https://doi.org/10.3389/fimmu.2023.1268998, doi:10.3389/fimmu.2023.1268998. This article has 22 citations and is from a peer-reviewed journal.

15. (strachinaru2024schistosomiasisinthe pages 7-8): Diana Isabela Costescu Strachinaru, Jemima Nyaboke Nyandwaro, Anke Stoefs, Eric Dooms, Peter Vanbrabant, Pierre-Michel François, Mihai Strachinaru, Marjan Van Esbroeck, Emmanuel Bottieau, and Patrick Soentjens. Schistosomiasis in the military—a narrative review. Tropical Medicine and Infectious Disease, 9:221, Sep 2024. URL: https://doi.org/10.3390/tropicalmed9090221, doi:10.3390/tropicalmed9090221. This article has 1 citations.

16. (martinez2024thewhoatlas pages 1-2): Santiago Gil Martinez, Pamela S. Mbabazi, Motshedisi H. Sebitloane, Bellington Vwalika, Sibone Mocumbi, Hashini N. Galaphaththi-Arachchige, Sigve D. Holmen, Bodo Randrianasolo, Borghild Roald, Femi Olowookorun, Francis Hyera, Sheila Mabote, Takalani G. Nemungadi, Thembinkosi V. Ngcobo, Tsakani Furumele, Patricia D. Ndhlovu, Martin W. Gerdes, Svein G. Gundersen, Zilungile L. Mkhize-Kwitshana, Myra Taylor, Roland E. E. Mhlanga, and Eyrun F. Kjetland. The who atlas for female-genital schistosomiasis: co-design of a practicable diagnostic guide, digital support and training. PLOS Global Public Health, 4:e0002249, Mar 2024. URL: https://doi.org/10.1371/journal.pgph.0002249, doi:10.1371/journal.pgph.0002249. This article has 13 citations and is from a peer-reviewed journal.

17. (ally2024schistosomiasisdiagnosischallenges pages 4-6): Ombeni Ally, Bernard N. Kanoi, Lucy Ochola, Steven Ger Nyanjom, Clement Shiluli, Gerald Misinzo, and Jesse Gitaka. Schistosomiasis diagnosis: challenges and opportunities for elimination. PLOS Neglected Tropical Diseases, 18:e0012282, Jul 2024. URL: https://doi.org/10.1371/journal.pntd.0012282, doi:10.1371/journal.pntd.0012282. This article has 39 citations and is from a domain leading peer-reviewed journal.

18. (ally2024schistosomiasisdiagnosischallenges pages 3-4): Ombeni Ally, Bernard N. Kanoi, Lucy Ochola, Steven Ger Nyanjom, Clement Shiluli, Gerald Misinzo, and Jesse Gitaka. Schistosomiasis diagnosis: challenges and opportunities for elimination. PLOS Neglected Tropical Diseases, 18:e0012282, Jul 2024. URL: https://doi.org/10.1371/journal.pntd.0012282, doi:10.1371/journal.pntd.0012282. This article has 39 citations and is from a domain leading peer-reviewed journal.

19. (ally2024schistosomiasisdiagnosischallenges pages 6-7): Ombeni Ally, Bernard N. Kanoi, Lucy Ochola, Steven Ger Nyanjom, Clement Shiluli, Gerald Misinzo, and Jesse Gitaka. Schistosomiasis diagnosis: challenges and opportunities for elimination. PLOS Neglected Tropical Diseases, 18:e0012282, Jul 2024. URL: https://doi.org/10.1371/journal.pntd.0012282, doi:10.1371/journal.pntd.0012282. This article has 39 citations and is from a domain leading peer-reviewed journal.

20. (vere2024effectsofpaediatric pages 15-17): Maryline Vere, Wilma ten Ham-Baloyi, and Paula Ezinne Melariri. Effects of paediatric schistosomiasis control programmes in sub-saharan africa: a systematic review. PLOS ONE, 19:e0301464, May 2024. URL: https://doi.org/10.1371/journal.pone.0301464, doi:10.1371/journal.pone.0301464. This article has 2 citations and is from a peer-reviewed journal.
