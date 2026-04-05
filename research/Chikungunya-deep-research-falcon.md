---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T13:03:03.004133'
end_time: '2026-04-04T13:14:56.619870'
duration_seconds: 713.62
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Chikungunya
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 41
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Chikungunya
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Chikungunya** covering all of the
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
- **Disease Name:** Chikungunya
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Chikungunya** covering all of the
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


## Comprehensive Research Report: Chikungunya (Chikungunya fever)

### Target disease
- **Disease name:** Chikungunya (often “chikungunya fever”) (weber2024chikungunyavirusvaccines pages 1-2, NCT04603131 chunk 2)
- **Category:** Infectious disease (arboviral; alphavirus infection) (NCT04603131 chunk 2)

### 1) Disease information
**Overview/definition.** Chikungunya is a mosquito-borne viral disease caused by chikungunya virus (CHIKV), an alphavirus, classically presenting with acute fever and prominent arthralgia/arthritis, with a substantial fraction developing persistent arthralgia lasting months to years (“chronic chikungunya”). (weber2024chikungunyavirusvaccines pages 1-2, rama2024clinicaloutcomesof pages 8-11)

**Key identifiers and controlled vocabularies (available from retrieved evidence).**
- **MeSH heading:** *Chikungunya Fever*; **MeSH ID:** **D065632** (ClinicalTrials.gov metadata) (NCT04603131 chunk 2, NCT06973772 chunk 3)
- **MeSH ancestors (examples):** Alphavirus Infections; Arbovirus Infections; Mosquito-Borne Diseases; Togaviridae Infections; RNA Virus Infections (NCT04603131 chunk 2)

**Synonyms/alternative names in the retrieved sources.**
- “Chikungunya”, “Chikungunya fever”, “Chikungunya disease” (NCT04603131 chunk 2, rama2024clinicaloutcomesof pages 1-2)
- Abbreviations: “CHIK” (disease), “CHIKV” (virus) (weber2024chikungunyavirusvaccines pages 1-2, rama2024clinicaloutcomesof pages 1-2)
- Chronic forms described as “chronic chikungunya disease (CCD)” and “chikungunya arthritis” (maurer2025comprehensiveassessmentof pages 29-29)

**Identifiers not recovered in the tool-retrieved texts.** ICD-10/ICD-11, MONDO, and Orphanet IDs were not present in the retrieved full text excerpts; therefore they are not asserted here from primary evidence. (weber2024chikungunyavirusvaccines pages 1-2, rama2024clinicaloutcomesof pages 1-2)

**Evidence source type.** This report synthesizes aggregated disease-level resources (systematic reviews/meta-analyses, cohort studies, diagnostic validation studies, regulatory/vaccine development reviews, and ClinicalTrials.gov records), rather than individual EHR-only patient data. (rama2024clinicaloutcomesof pages 8-11, lazari2023clinicalmarkersof pages 1-2, pereira2023performanceevaluationof pages 1-2, chen2024frombenchto pages 2-3, NCT05072080 chunk 2)

### 2) Etiology
**Causal factor.** Infection with CHIKV transmitted by Aedes mosquitoes (notably *Aedes aegypti* and *Aedes albopictus*) is the proximate cause of chikungunya. (weber2024chikungunyavirusvaccines pages 1-2)

**Risk factors (host/clinical).**
- **Female sex** increases risk of progression to chronic inflammatory joint disease in a prospective Brazilian cohort (RR 1.52, 95% CI 1.15–1.99). (lazari2023clinicalmarkersof pages 1-2)
- **Subacute persistence of symptoms (Day 21)** and especially **articular edema** are predictors of chronification beyond 3 months (examples: reported edema RR 3.61; small-joint edema RR 4.22). (lazari2023clinicalmarkersof pages 1-2)
- Reviews highlight **older age (>35 years)** and **obesity** as correlates of severe/atypical disease presentations. (weber2024chikungunyavirusvaccines pages 1-2)

**Protective factors / genetic factors.** No robust human protective variants or definitive genetic susceptibility loci were identified in the retrieved evidence set. Mechanistic reviews discuss antiviral interferon responses as protective at the pathway level (see pathophysiology), but not as specific human protective genotypes. (ma2026pathogenesisofchronic pages 6-7, silveirafreitas2024longchikungunya?an pages 2-4)

### 3) Phenotypes (clinical features)
#### 3.1 Acute chikungunya (typical clinical picture and frequency)
A recent systematic review/meta-analysis (published **June 2024**) quantified pooled symptom prevalences: arthralgia ~89.7%, fever ~87.8%, myalgia ~62.9%, rash ~44%, and headache ~49.5%; hospitalization during the acute phase was ~17%. (rama2024clinicaloutcomesof pages 8-11, rama2024clinicaloutcomesof media e50a84dc)

**Suggested HPO mappings (examples).**
- Fever: **HP:0001945**
- Arthralgia: **HP:0002829**
- Arthritis (inflammatory joint disease): **HP:0001369**
- Myalgia: **HP:0003326**
- Rash (maculopapular): **HP:0000980** (or **HP:0001050** for generalized rash)
- Headache: **HP:0002315**
- Joint swelling/edema: **HP:0001382**
- Fatigue: **HP:0012378**

(Phenotype names and frequencies supported by meta-analysis; HPO IDs are standard ontology suggestions for knowledge-base normalization.) (rama2024clinicaloutcomesof pages 8-11)

#### 3.2 Post-acute and chronic chikungunya (arthralgia/arthritis and QoL)
**Persistence/chronicity rates (pooled).** Symptom persistence declines over time but remains substantial: 43.9% at 3 months, 34.4% at 6 months, and 31.9% at 12 months in pooled estimates. (rama2024clinicaloutcomesof pages 8-11, rama2024clinicaloutcomesof media 900f64f8)

**Cohort-based chronic inflammatory joint disease and imaging.** In a prospective Brazilian cohort (PLOS NTD; **Jan 2023**), 45.3% (39/86) of those completing follow-up met criteria for post-chikungunya chronic inflammatory joint disease (pCHIKV-CIJD); among those examined by ultrasound, 90.6% had abnormal findings, with synovitis (65.5%) and joint effusion (58.6%) common. (lazari2023clinicalmarkersof pages 1-2)

**Quality-of-life and fatigue impacts.** A Colombia cohort study (published **Oct 2024**) assessed adults seven years after infection: 14.1% had post-CHIKV chronic rheumatism, and chronic fatigue prevalence was 54.6% in that chronic rheumatism group (vs 8.6% in those without rheumatic disease); QoL was significantly worse in groups with chronic rheumatologic/non-inflammatory pain than those without rheumatic disease. (lozanoparra2024chronicrheumatologicdisease pages 1-2)

**Suggested HPO mappings for chronic disease.**
- Synovitis: **HP:0100765**
- Joint effusion: **HP:0002203**
- Morning stiffness: **HP:0030833**
- Chronic fatigue: **HP:0012432**

(pCHIKV-CIJD imaging and chronic fatigue/QoL supported by cohort studies; HPO IDs are standard ontology suggestions.) (lazari2023clinicalmarkersof pages 1-2, lozanoparra2024chronicrheumatologicdisease pages 1-2)

### 4) Genetic / molecular information
Chikungunya is not a monogenic inherited disease; **host genetics** may influence severity/chronicity, but specific causal variants were not retrieved in the current evidence set. (ma2026pathogenesisofchronic pages 7-9)

### 5) Environmental information
The primary environmental determinant is exposure to competent mosquito vectors (*Aedes* spp.), with public-health relevance heightened in settings with co-circulating arboviruses (e.g., dengue, Zika) that overlap clinically and diagnostically. (pereira2023performanceevaluationof pages 1-2)

### 6) Mechanism / pathophysiology (current understanding)
Persistent musculoskeletal disease is widely interpreted as an **immunopathologic sequel** driven by tissue tropism, inflammatory signaling, and persistence of viral antigen/RNA in joint-related compartments.

**Causal chain (high-level):**
1) **Acute infection and tissue tropism:** CHIKV shows tropism for monocytes/macrophages and joint-associated cells (including fibroblasts/synoviocytes), triggering robust innate cytokine and chemokine responses (e.g., IL-6, IL-1β, IL-8, IL-17; CCL2; CXCL9/10). (silveirafreitas2024longchikungunya?an pages 4-5)
2) **Innate antiviral pathways and evasion:** Type I interferon responses help control replication; CHIKV nonstructural proteins can antagonize interferon signaling, which may contribute to persistence and worse chronic outcomes. (ma2026pathogenesisofchronic pages 6-7)
3) **Antigen persistence and macrophage-centered chronic inflammation:** Mechanistic synthesis proposes that **viral antigens persist post-infection** and sustain activation of synovial macrophages, including via **SLAMF7**, promoting recruitment/infiltration of **CD4+ T cells** and chronic local cytokine production. (silveirafreitas2024longchikungunya?an pages 1-2)
4) **Th17 axis and bone/cartilage injury:** Expansion of **Th17 responses** and **IL-17** signaling promotes **RANKL** upregulation, osteoclastogenesis, bone resorption, and matrix remodeling; persistent proinflammatory cytokines (IL-6/MCP-1) and MMP activation contribute to cartilage extracellular matrix degradation. (silveirafreitas2024longchikungunya?an pages 4-5, lozanoparra2024acuteimmunologicalprofile pages 8-10)

**Suggested Cell Ontology (CL) terms (examples).**
- Macrophage: **CL:0000235**
- Monocyte: **CL:0000576**
- CD4-positive, alpha-beta T cell: **CL:0000624**
- T helper 17 cell: **CL:0000899**

**Suggested GO Biological Process terms (examples).**
- Type I interferon signaling pathway
- Inflammatory response
- Positive regulation of cytokine production
- Osteoclast differentiation
- Extracellular matrix disassembly

(Mechanistic claims supported by 2024 immunopathology review and 2024 systematic review of immunologic biomarkers; terms are ontology suggestions for knowledge-base normalization.) (silveirafreitas2024longchikungunya?an pages 1-2, lozanoparra2024acuteimmunologicalprofile pages 8-10)

### 7) Anatomical structures affected
Primary morbidity is musculoskeletal/joint involvement (synovium and peri-articular tissues) with imaging evidence of synovitis and effusion in chronic inflammatory joint disease. (lazari2023clinicalmarkersof pages 1-2)

**Suggested UBERON terms (examples).**
- Synovial membrane: **UBERON:0002390**
- Joint: **UBERON:0000982**

### 8) Temporal development (onset and progression)
Chikungunya is typically **acute onset**, with prominent symptoms during the first 7–10 days, but a substantial fraction progress to **persistent/chronic arthralgia** over months to years. Pooled chronicity at 3–12 months remains ~32–44%. (rama2024clinicaloutcomesof pages 8-11, rama2024clinicaloutcomesof media 900f64f8)

### 9) Inheritance and population (epidemiology)
#### 9.1 Global and regional burden (recent)
A worldwide observational study estimating 2024 autochthonous burden reported **696,564 cases globally** (incidence 11.13/100,000) and that the **Americas** carried the largest burden (**431,305 cases; 43.90/100,000**). (wang2026globalandregional pages 4-5)

#### 9.2 2023–2024 outbreak examples and surveillance gaps
- **Brazil (Minas Gerais, 2023):** Excess-mortality analysis estimated **890 excess deaths** attributable to chikungunya in a ~2.5 million population area (mortality rate **35.1/100,000**), compared with only **15 confirmed deaths** in surveillance in that area—suggesting major under-ascertainment. (freitas2024excessmortalityassociated pages 1-2)
- **Argentina (2023):** 2,314 confirmed cases (EW1–43) with genomic evidence of ECSA lineage predominance, representing lineage shift compared with earlier Asian-lineage circulation (2016). (fabbri2024tracingtheevolution pages 1-2)
- **Europe (2007–2023 surveillance summary):** 4,730 cases documented in 2007–2022 across mainland Europe, and **no cases reported in 2023**; most historical cases were travel-related. (liu2025chikungunyavirusin pages 1-2)

### 10) Diagnostics
#### 10.1 Recommended diagnostic windows (molecular vs serology)
Guidance summarized in a 2023 international evaluation study supports:
- **rRT-PCR within the first week of illness** (confirmatory), with **rRT-PCR alone days 0–5**, and **rRT-PCR ± IgM days 5–7**; after day 7, serology becomes central. (pereira2023performanceevaluationof pages 2-3)
- After day 7, **IgM positivity is presumptive**, and **paired sera IgG seroconversion or ≥4-fold rise** confirms active infection; IgG may persist for years. (pereira2023performanceevaluationof pages 2-3)

#### 10.2 Performance data (recent)
- Automated VIDAS® assays showed high agreement with comparator ELISA (97.5–100%), with IgM positive detection **88.2–100% ≥5 days** post symptom onset and IgG detection **100% ≥11 days**; analytical cross-reactivity was low (≤2.9% overall). (pereira2023performanceevaluationof pages 15-16)
- Antigen-detection methods (reviewed 2023) can perform well early: antigen detection sensitivity reported ~85% overall and up to ~95% in the first 5 days in some evaluations; selected rapid tests reported sensitivity/specificity around 89.4%/94.4%. (simo2023chikungunyavirusdiagnosis pages 4-6)
- Longitudinal cohort evidence (2025) demonstrates that IgM can persist far beyond typical expectations: among patients with chronic arthralgia, **33%** remained IgM-positive **>720 days** post symptom onset, complicating surveillance and interpretation of single-sample IgM. (jacobnascimento2025longtermpersistenceof pages 5-7)

**Differential diagnosis.** Because clinical presentation overlaps with dengue and Zika (especially during co-circulation), diagnostic algorithms emphasize early RT-PCR and careful interpretation of serology. (pereira2023performanceevaluationof pages 1-2)

### 11) Outcome / prognosis
**Chronic morbidity.** Pooled chronicity rates are substantial at 3–12 months (43.9% → 31.9%), with cohort evidence of chronic inflammatory arthritis syndromes and QoL impairment. (rama2024clinicaloutcomesof pages 8-11, lazari2023clinicalmarkersof pages 1-2)

**Mortality.** Meta-analysis estimated overall mortality around **0.32%** in general/low-risk populations, but much higher mortality estimates in hospitalized/elderly/high-risk subgroups. (rama2024clinicaloutcomesof pages 8-11, rama2024clinicaloutcomesof media 3fb5798c)

**Surveillance under-ascertainment of death.** Excess mortality analysis in Brazil (2023) indicates routine surveillance may severely underestimate chikungunya-attributable mortality during epidemics. (freitas2024excessmortalityassociated pages 1-2)

### 12) Treatment
**No specific antivirals.** Multiple reviews note there is **no FDA-approved CHIKV-specific antiviral medication**, and clinical management is primarily supportive/symptomatic. (irfan2024advancementsinchikungunya pages 1-2, maurer2025comprehensiveassessmentof pages 1-2)

**Acute symptomatic management (real-world).** Supportive care includes rest, hydration, analgesics and NSAIDs. (weber2024chikungunyavirusvaccines pages 1-2)

**Chronic inflammatory arthritis management (real-world).** For persistent inflammatory manifestations, treatments include NSAIDs and corticosteroids; DMARDs such as methotrexate, sulfasalazine, leflunomide, and hydroxychloroquine are used when disease resembles RA-like inflammatory arthritis, with TNF inhibitors (e.g., etanercept) reported for refractory cases. (silveirafreitas2024longchikungunya?an pages 2-4)

**Suggested MAXO mappings (examples).**
- Vaccination: **MAXO:0000102** (immunization/vaccination)
- NSAID therapy: (MAXO class “drug therapy” + NSAID)
- Corticosteroid therapy: (MAXO class “drug therapy” + glucocorticoid)
- DMARD therapy (methotrexate/sulfasalazine/leflunomide/hydroxychloroquine): (MAXO class “drug therapy”)
- TNF inhibitor therapy: (MAXO class “biologic therapy”)

(MAXO IDs can vary by release; the above are suggested mapping categories for knowledge-base annotation.)

### 13) Prevention
#### 13.1 Vaccine-based prevention (major 2023–2024 development)
**IXCHIQ (VLA1553) approvals.** The live-attenuated single-dose vaccine **IXCHIQ** was approved by the **US FDA (Nov 2023)**, **Health Canada (Jun 2024)**, and the **European Commission (Jul 2024)**. (weber2024chikungunyavirusvaccines pages 1-2)

**IXCHIQ immunogenicity (phase 3, surrogate endpoint).** A Journal of Travel Medicine development review (published/accepted in 2024) reports seroresponse of **98.9% at Day 28** and durable seroconversion at 6 months (**98.3%**). (chen2024frombenchto pages 2-3)

**IXCHIQ safety/reactogenicity (pooled trial evidence).** Solicited systemic events were common but mostly short-lived: fever 13.5%, arthralgia 17.2%, myalgia 23.9%, fatigue 28.5%, headache 31.6%. Broad-definition AESIs were 11.7% in vaccine vs 0.6% placebo; prolonged AESIs (≥30 days) occurred in 0.5% and severe cases in 1.6% of vaccine recipients in the cited pooled analysis. (maurer2025comprehensiveassessmentof pages 1-2)

#### 13.2 Vector control and bite avoidance
When vaccines are unavailable or for broader population control, prevention relies on reducing mosquito breeding sites and avoiding bites (repellents, protective clothing, screens). (weber2024chikungunyavirusvaccines pages 1-2)

### 14) Other species / natural disease
The retrieved evidence set did not provide primary data on naturally occurring disease in non-human vertebrate species beyond experimental models; thus, non-human natural-host epidemiology is not asserted here. (chen2024frombenchto pages 2-3)

### 15) Model organisms
Vaccine and pathogenesis research commonly uses:
- **Mouse models** (immunogenicity, viremia, clinical signs) (weber2024chikungunyavirusvaccines pages 2-4)
- **Non-human primates** (e.g., cynomolgus macaques) for immunogenicity, challenge protection, and establishing a serological surrogate of protection used for accelerated vaccine development. (chen2024frombenchto pages 2-3)

### Recent developments and real-world implementations (2023–2024 emphasis)
- 2024 meta-analysis consolidated pooled estimates of acute symptom frequencies, chronicity at 3–12 months, hospitalization, and mortality, providing a quantitative baseline for burden estimation and policy. (rama2024clinicaloutcomesof pages 8-11, rama2024clinicaloutcomesof media e50a84dc)
- 2023–2024 marks transition from “no licensed vaccines” to **first approved vaccine (IXCHIQ)** and active late-stage development of VLP vaccines. (weber2024chikungunyavirusvaccines pages 1-2, NCT05072080 chunk 2)
- 2024 excess-mortality analyses underscore that chikungunya mortality may be substantially underestimated during epidemics, influencing prioritization for vaccination and surveillance strengthening. (freitas2024excessmortalityassociated pages 1-2)

### Clinical trials snapshot (real-world pipeline)
- **PXVX0317 (VLP vaccine), Phase 3:** **NCT05072080** (Bavarian Nordic). (NCT05072080 chunk 2)
- **PXVX0317, Phase 2:** **NCT03992872**, open-label, alum-adjuvanted VLP vaccine; results posted 2024-10-16. (NCT03992872 chunk 1)
- **Dengue + chikungunya co-administration, Phase 3b:** **NCT06973772** (Butantan Institute), planned start 2026-03-31; evaluates coadministration of Butantan-DV and live-attenuated chikungunya vaccine. (NCT06973772 chunk 1)

## Evidence table (key statistics)
| Metric | Value | Population/Context | Source (DOI + month/year) | Notes |
|---|---:|---|---|---|
| Acute arthralgia prevalence | 89.7% | Pooled symptomatic chikungunya cases in systematic review/meta-analysis | 10.1371/journal.pntd.0012254, Jun 2024 (rama2024clinicaloutcomesof pages 8-11) | Acute hallmark symptom |
| Acute fever prevalence | 87.8% | Pooled symptomatic chikungunya cases | 10.1371/journal.pntd.0012254, Jun 2024 (rama2024clinicaloutcomesof pages 8-11) | Common early presentation |
| Acute myalgia prevalence | 62.9% | Pooled symptomatic chikungunya cases | 10.1371/journal.pntd.0012254, Jun 2024 (rama2024clinicaloutcomesof pages 8-11) | Often accompanies fever/arthralgia |
| Acute rash prevalence | ~44% | Pooled symptomatic chikungunya cases | 10.1371/journal.pntd.0012254, Jun 2024 (rama2024clinicaloutcomesof pages 8-11) | Maculopapular rash commonly reported |
| Acute headache prevalence | ~49.5% | Pooled symptomatic chikungunya cases | 10.1371/journal.pntd.0012254, Jun 2024 (rama2024clinicaloutcomesof pages 8-11) | Non-specific but frequent |
| Hospitalization rate | ~17% | Acute-phase chikungunya cases | 10.1371/journal.pntd.0012254, Jun 2024 (rama2024clinicaloutcomesof pages 8-11) | Heterogeneous across studies |
| Chronicity at 3 months | 43.9% | Post-acute/chronic symptom persistence | 10.1371/journal.pntd.0012254, Jun 2024 (rama2024clinicaloutcomesof pages 8-11) | Chronic arthralgia declines over time |
| Chronicity at 6 months | 34.4% | Post-acute/chronic symptom persistence | 10.1371/journal.pntd.0012254, Jun 2024 (rama2024clinicaloutcomesof pages 8-11) | Persistent burden remains substantial |
| Chronicity at 12 months | 31.9% | Post-acute/chronic symptom persistence | 10.1371/journal.pntd.0012254, Jun 2024 (rama2024clinicaloutcomesof pages 8-11) | Consistent with long-term sequelae burden |
| Mortality rate | 0.32% | General/low-risk pooled estimate | 10.1371/journal.pntd.0012254, Jun 2024 (rama2024clinicaloutcomesof pages 8-11) | Higher in hospitalized/elderly/high-risk groups |
| 2023 Brazil excess mortality estimate | 890 excess deaths; 35.1/100,000 | North and Northeast macroregions of Minas Gerais, Brazil; 2023 epidemic | 10.3389/fitd.2024.1466207, Oct 2024 (freitas2024excessmortalityassociated pages 1-2, freitas2024excessmortalityassociated pages 5-7) | ~60-fold above deaths captured by surveillance in study region |
| 2024 global burden | 696,564 autochthonous cases; 11.13/100,000 incidence | Global | 10.7189/jogh.16.04055, Feb 2026 (wang2026globalandregional pages 4-5) | Americas: 431,305 cases; 43.90/100,000 |
| 2023 Argentina outbreak | 2,314 confirmed cases; ECSA genotype predominated | Argentina, EW1–43 2023 | 10.1080/22221751.2024.2362941, Jun 2024 (fabbri2024tracingtheevolution pages 1-2) | 2016 epidemic had Asian lineage; 2023 shifted to ECSA |
| 2023 Europe cases | 0 cases reported in 2023; 4,730 total in 2007–2022 | Mainland Europe surveillance | 10.1371/journal.pntd.0012904, Mar 2025 (liu2025chikungunyavirusin pages 1-2) | Most historic European cases were travel-related |
| Diagnostic timing: RT-PCR vs serology | RT-PCR ≤7 days; RT-PCR alone days 0–5; RT-PCR ± IgM days 5–7; serology after day 7 | Laboratory diagnosis of acute vs later infection | 10.3390/diagnostics13132306, Jul 2023 (pereira2023performanceevaluationof pages 2-3, pereira2023performanceevaluationof pages 15-16) | Paired IgG seroconversion or ≥4-fold rise confirms active infection after day 7 |
| VIDAS IgM detection window | 88.2–100.0% positive at ≥5 days post-symptom onset | Proven CHIKV infection | 10.3390/diagnostics13132306, Jul 2023 (pereira2023performanceevaluationof pages 15-16, pereira2023performanceevaluationof pages 1-2) | Agreement with ELISA 97.5–100% |
| VIDAS IgG detection window | 100.0% positive at ≥11 days post-symptom onset | Proven CHIKV infection | 10.3390/diagnostics13132306, Jul 2023 (pereira2023performanceevaluationof pages 15-16, pereira2023performanceevaluationof pages 1-2) | Useful for later diagnosis/surveillance |
| IgM persistence >2 years | 33% (7/21) remained IgM-positive >720 DPSO | Patients with chronic arthralgia | 10.1186/s12985-025-02721-x, Apr 2025 (jacobnascimento2025longtermpersistenceof pages 1-2, jacobnascimento2025longtermpersistenceof pages 5-7) | Positive IgM may not indicate recent infection |
| IXCHIQ approval dates | US FDA: Nov 2023; Health Canada: Jun 2024; European Commission: Jul 2024 | Regulatory approvals for VLA1553/IXCHIQ | 10.1007/s40259-024-00677-y, Sep 2024 (weber2024chikungunyavirusvaccines pages 1-2); 10.1007/s40259-024-00677-y, Sep 2024 (weber2024chikungunyavirusvaccines pages 1-2) | First licensed chikungunya vaccine |
| IXCHIQ phase 3 seroresponse | 98.9% at Day 28; 98.3% maintained seroconversion at 6 months | Pivotal phase 3, n=4,128 | 10.1093/jtm/taae123, Sep 2024 (chen2024frombenchto pages 2-3) | Immune responses similar in older adults |
| IXCHIQ reactogenicity | Fever 13.5%; arthralgia 17.2%; myalgia 23.9%; fatigue 28.5%; headache 31.6% | Pooled VLA1553 clinical-trial safety data | 10.3390/vaccines13060576, May 2025 (maurer2025comprehensiveassessmentof pages 1-2) | Broad AESIs 11.7%; prolonged AESIs 0.5%; severe cases 1.6% |
| PXVX0317 phase 3 trial | NCT05072080 | VLP-based chikungunya vaccine, sponsor Bavarian Nordic | ClinicalTrials.gov, 2021 entry (NCT05072080 chunk 2) | Phase 3 placebo-controlled study with immunogenicity endpoints at Days 8, 15, 22, 183 |


*Table: This table compiles the most important quantitative clinical, epidemiologic, diagnostic, and vaccine-development metrics for chikungunya from the gathered evidence. It is useful as a quick-reference summary for populating a disease knowledge base or supporting a narrative research report.*

## Visual evidence from meta-analysis
Key pooled estimates and forest plots for chronicity, mortality, and symptomatic rate are presented in the meta-analysis Table/Figures. (rama2024clinicaloutcomesof media e50a84dc, rama2024clinicaloutcomesof media 900f64f8, rama2024clinicaloutcomesof media 3fb5798c, rama2024clinicaloutcomesof media 32d1ac79)

## Abstract quotes supporting key claims (verbatim from retrieved abstracts)
- “Upon employing broader inclusion criteria, the overall symptomatic rate was 75% (95% CI: 63–84%), the chronicity rate was 44% (95% CI: 31–57%), and the mortality rate was 0.3% (95% CI: 0.1–0.7%).” (PLOS NTD meta-analysis; published Jun 2024) (rama2024clinicaloutcomesof pages 1-2)
- “In 2023, a major chikungunya epidemic occurred in Minas Gerais… During the epidemic, there were 890 excess deaths attributed to chikungunya, translating into a mortality rate of 35.1/100,000 inhabitants.” (Frontiers in Tropical Diseases; Oct 2024) (freitas2024excessmortalityassociated pages 1-2)
- “In November 2023, the US Food and Drug Administration (FDA) approved the VLA1553 live-attenuated vaccine, which is marketed as IXCHIQ.” (BioDrugs review; Sep 2024) (weber2024chikungunyavirusvaccines pages 1-2)

## Notes on evidence limitations for knowledge-base curation
- This evidence set supports MeSH normalization (D065632) but did not contain ICD-10/ICD-11/MONDO/Orphanet IDs in accessible text; adding those identifiers requires consultation of coding/ontology resources beyond the retrieved papers. (NCT04603131 chunk 2, weber2024chikungunyavirusvaccines pages 1-2)
- Human genetic susceptibility or protective variants were not identified in the retrieved corpus; mechanistic susceptibility is supported at pathway/cell-type level rather than variant level. (ma2026pathogenesisofchronic pages 6-7, silveirafreitas2024longchikungunya?an pages 2-4)

References

1. (weber2024chikungunyavirusvaccines pages 1-2): Whitney C. Weber, Daniel N. Streblow, and Lark L. Coffey. Chikungunya virus vaccines: a review of ixchiq and pxvx0317 from pre-clinical evaluation to licensure. Biodrugs, 38:727-742, Sep 2024. URL: https://doi.org/10.1007/s40259-024-00677-y, doi:10.1007/s40259-024-00677-y. This article has 49 citations and is from a peer-reviewed journal.

2. (NCT04603131 chunk 2):  Clinical Trial to Evaluate the Immunogenicity of Chikungunya Vaccine. Bharat Biotech International Limited. 2017. ClinicalTrials.gov Identifier: NCT04603131

3. (rama2024clinicaloutcomesof pages 8-11): Kris Rama, Adrianne M. de Roo, Timon Louwsma, Hinko S. Hofstra, Gabriel S. Gurgel do Amaral, Gerard T. Vondeling, Maarten J. Postma, and Roel D. Freriks. Clinical outcomes of chikungunya: a systematic literature review and meta-analysis. PLOS Neglected Tropical Diseases, 18:e0012254, Jun 2024. URL: https://doi.org/10.1371/journal.pntd.0012254, doi:10.1371/journal.pntd.0012254. This article has 68 citations and is from a domain leading peer-reviewed journal.

4. (NCT06973772 chunk 3):  Trial to Evaluate the Immunogenicity and Safety of the Co-administration of Live Attenuated Dengue and Chikungunya Vaccines Compared to Separate Administration in Adults Aged 18 to 59 Years.. Butantan Institute. 2026. ClinicalTrials.gov Identifier: NCT06973772

5. (rama2024clinicaloutcomesof pages 1-2): Kris Rama, Adrianne M. de Roo, Timon Louwsma, Hinko S. Hofstra, Gabriel S. Gurgel do Amaral, Gerard T. Vondeling, Maarten J. Postma, and Roel D. Freriks. Clinical outcomes of chikungunya: a systematic literature review and meta-analysis. PLOS Neglected Tropical Diseases, 18:e0012254, Jun 2024. URL: https://doi.org/10.1371/journal.pntd.0012254, doi:10.1371/journal.pntd.0012254. This article has 68 citations and is from a domain leading peer-reviewed journal.

6. (maurer2025comprehensiveassessmentof pages 29-29): Gabriele Maurer, Vera Buerger, Julian Larcher-Senn, Florian Erlsbacher, Stéphanie Meyer, Susanne Eder-Lingelbach, and Juan Carlos Jaramillo. Comprehensive assessment of reactogenicity and safety of the live-attenuated chikungunya vaccine (ixchiq®). Vaccines, 13:576, May 2025. URL: https://doi.org/10.3390/vaccines13060576, doi:10.3390/vaccines13060576. This article has 6 citations.

7. (lazari2023clinicalmarkersof pages 1-2): Carolina dos Santos Lázari, Mariana Severo Ramundo, Felipe ten-Caten, Clarisse S. Bressan, Ana Maria Bispo de Filippis, Erika Regina Manuli, Isabella de Moraes, Geovana Maria Pereira, Marina Farrel Côrtes, Darlan da Silva Candido, Alexandra L. Gerber, Ana Paula Guimarães, Nuno Rodrigues Faria, Helder I. Nakaya, Ana Tereza R. Vasconcelos, Patrícia Brasil, Gláucia Paranhos-Baccalà, and Ester Cerdeira Sabino. Clinical markers of post-chikungunya chronic inflammatory joint disease: a brazilian cohort. PLOS Neglected Tropical Diseases, 17:e0011037, Jan 2023. URL: https://doi.org/10.1371/journal.pntd.0011037, doi:10.1371/journal.pntd.0011037. This article has 19 citations and is from a domain leading peer-reviewed journal.

8. (pereira2023performanceevaluationof pages 1-2): Geovana M. Pereira, Erika R. Manuli, Laurie Coulon, Marina F. Côrtes, Mariana S. Ramundo, Loïc Dromenq, Audrey Larue-Triolet, Frédérique Raymond, Carole Tourneur, Carolina dos Santos Lázari, Patricia Brasil, Ana Maria Bispo de Filippis, Glaucia Paranhos-Baccalà, Alice Banz, and Ester C. Sabino. Performance evaluation of vidas® diagnostic assays detecting anti-chikungunya virus igm and igg antibodies: an international study. Diagnostics, 13:2306, Jul 2023. URL: https://doi.org/10.3390/diagnostics13132306, doi:10.3390/diagnostics13132306. This article has 4 citations.

9. (chen2024frombenchto pages 2-3): Lin H Chen, Andrea Fritzer, Romana Hochreiter, Katrin Dubischar, and Stéphanie Meyer. From bench to clinic: the development of vla1553/ixchiq, a live-attenuated chikungunya vaccine. Journal of Travel Medicine, Sep 2024. URL: https://doi.org/10.1093/jtm/taae123, doi:10.1093/jtm/taae123. This article has 38 citations and is from a domain leading peer-reviewed journal.

10. (NCT05072080 chunk 2):  A Phase 3 Trial of the VLP-Based Chikungunya Vaccine PXVX0317 (CHIKV VLP Vaccine). Bavarian Nordic. 2021. ClinicalTrials.gov Identifier: NCT05072080

11. (ma2026pathogenesisofchronic pages 6-7): Mengye Ma, Leyi Li, Hao Sun, and Xiaochao Zhang. Pathogenesis of chronic arthritis due to chikungunya virus and advances in vaccine development. Viruses, 18:428, Apr 2026. URL: https://doi.org/10.3390/v18040428, doi:10.3390/v18040428. This article has 0 citations.

12. (silveirafreitas2024longchikungunya?an pages 2-4): Jayme Euclydes Picasky Silveira-Freitas, Maria Luiza Campagnolo, Mariana dos Santos Cortez, Fabrício Freire de Melo, Ana Carla Zarpelon-Schutz, and Kádima Nayara Teixeira. Long chikungunya? an overview to immunopathology of persistent arthralgia. World Journal of Virology, Jun 2024. URL: https://doi.org/10.5501/wjv.v13.i2.89985, doi:10.5501/wjv.v13.i2.89985. This article has 11 citations.

13. (rama2024clinicaloutcomesof media e50a84dc): Kris Rama, Adrianne M. de Roo, Timon Louwsma, Hinko S. Hofstra, Gabriel S. Gurgel do Amaral, Gerard T. Vondeling, Maarten J. Postma, and Roel D. Freriks. Clinical outcomes of chikungunya: a systematic literature review and meta-analysis. PLOS Neglected Tropical Diseases, 18:e0012254, Jun 2024. URL: https://doi.org/10.1371/journal.pntd.0012254, doi:10.1371/journal.pntd.0012254. This article has 68 citations and is from a domain leading peer-reviewed journal.

14. (rama2024clinicaloutcomesof media 900f64f8): Kris Rama, Adrianne M. de Roo, Timon Louwsma, Hinko S. Hofstra, Gabriel S. Gurgel do Amaral, Gerard T. Vondeling, Maarten J. Postma, and Roel D. Freriks. Clinical outcomes of chikungunya: a systematic literature review and meta-analysis. PLOS Neglected Tropical Diseases, 18:e0012254, Jun 2024. URL: https://doi.org/10.1371/journal.pntd.0012254, doi:10.1371/journal.pntd.0012254. This article has 68 citations and is from a domain leading peer-reviewed journal.

15. (lozanoparra2024chronicrheumatologicdisease pages 1-2): Anyela Lozano-Parra, Víctor Herrera, Carlos Calderón, Reynaldo Badillo, Rosa Margarita Gélvez Ramírez, María Isabel Estupiñán Cárdenas, José Fernando Lozano Jiménez, Luis Ángel Villar, and Elsa Marina Rojas Garrido. Chronic rheumatologic disease in chikungunya virus fever: results from a cohort study conducted in piedecuesta, colombia. Tropical Medicine and Infectious Disease, Oct 2024. URL: https://doi.org/10.3390/tropicalmed9100247, doi:10.3390/tropicalmed9100247. This article has 9 citations.

16. (ma2026pathogenesisofchronic pages 7-9): Mengye Ma, Leyi Li, Hao Sun, and Xiaochao Zhang. Pathogenesis of chronic arthritis due to chikungunya virus and advances in vaccine development. Viruses, 18:428, Apr 2026. URL: https://doi.org/10.3390/v18040428, doi:10.3390/v18040428. This article has 0 citations.

17. (silveirafreitas2024longchikungunya?an pages 4-5): Jayme Euclydes Picasky Silveira-Freitas, Maria Luiza Campagnolo, Mariana dos Santos Cortez, Fabrício Freire de Melo, Ana Carla Zarpelon-Schutz, and Kádima Nayara Teixeira. Long chikungunya? an overview to immunopathology of persistent arthralgia. World Journal of Virology, Jun 2024. URL: https://doi.org/10.5501/wjv.v13.i2.89985, doi:10.5501/wjv.v13.i2.89985. This article has 11 citations.

18. (silveirafreitas2024longchikungunya?an pages 1-2): Jayme Euclydes Picasky Silveira-Freitas, Maria Luiza Campagnolo, Mariana dos Santos Cortez, Fabrício Freire de Melo, Ana Carla Zarpelon-Schutz, and Kádima Nayara Teixeira. Long chikungunya? an overview to immunopathology of persistent arthralgia. World Journal of Virology, Jun 2024. URL: https://doi.org/10.5501/wjv.v13.i2.89985, doi:10.5501/wjv.v13.i2.89985. This article has 11 citations.

19. (lozanoparra2024acuteimmunologicalprofile pages 8-10): Anyela Lozano-Parra, Víctor Herrera, Silvio Urcuqui-Inchima, Rosa Margarita Gélvez Ramírez, and Luis Ángel Villar. Acute immunological profile and prognostic biomarkers of persistent joint pain in chikungunya fever: a systematic review. The Yale Journal of Biology and Medicine, 97:473-489, Dec 2024. URL: https://doi.org/10.59249/rqyj3197, doi:10.59249/rqyj3197. This article has 8 citations.

20. (wang2026globalandregional pages 4-5): Sijia Wang, Yutong Liu, Yaping Wang, Liyan Zhou, and Jue Liu. Global and regional burden of chikungunya from 2004 to 2024: a worldwide observational study. Journal of Global Health, Feb 2026. URL: https://doi.org/10.7189/jogh.16.04055, doi:10.7189/jogh.16.04055. This article has 0 citations and is from a peer-reviewed journal.

21. (freitas2024excessmortalityassociated pages 1-2): André Ricardo Ribas Freitas, Antonio Silva Lima Neto, Rosana Rodrigues, Erneson Alves de Oliveira, José S. Andrade, and Luciano P. G. Cavalcanti. Excess mortality associated with chikungunya epidemic in southeast brazil, 2023. Frontiers in Tropical Diseases, Oct 2024. URL: https://doi.org/10.3389/fitd.2024.1466207, doi:10.3389/fitd.2024.1466207. This article has 13 citations.

22. (fabbri2024tracingtheevolution pages 1-2): Cintia Fabbri, Marta Giovanetti, Victoria Luppo, Vagner Fonseca, Jorge Garcia, Cintia Barulli, Mariel Feroci, Sofia Perrone, Doraldina Casoni, Sergio Giamperetti, Maria Cristina Alvarez Lopez, Maria Delia Foussal, Mauricio Figueredo, Karina Salvatierra, Sergio Lejona, Natalia Ruiz Diaz, Gonzalo Castro, Gabriela Bravo, Noelia Jackel, Carina Sen, Tomás Poklepovich Caride, Leticia Franco, Carlos Giovachini, Jairo Mendez Rico, Luiz Carlos Junior Alcantara, and Maria Alejandra Morales. Tracing the evolution of the chikungunya virus in argentina, 2016-2023: independent introductions and prominence of latin american lineages. Emerging Microbes &amp; Infections, Jun 2024. URL: https://doi.org/10.1080/22221751.2024.2362941, doi:10.1080/22221751.2024.2362941. This article has 7 citations and is from a domain leading peer-reviewed journal.

23. (liu2025chikungunyavirusin pages 1-2): Qian Liu, Hong Shen, Li Gu, Hui Yuan, and Wentao Zhu. Chikungunya virus in europe: a retrospective epidemiology study from 2007 to 2023. PLOS Neglected Tropical Diseases, 19:e0012904, Mar 2025. URL: https://doi.org/10.1371/journal.pntd.0012904, doi:10.1371/journal.pntd.0012904. This article has 27 citations and is from a domain leading peer-reviewed journal.

24. (pereira2023performanceevaluationof pages 2-3): Geovana M. Pereira, Erika R. Manuli, Laurie Coulon, Marina F. Côrtes, Mariana S. Ramundo, Loïc Dromenq, Audrey Larue-Triolet, Frédérique Raymond, Carole Tourneur, Carolina dos Santos Lázari, Patricia Brasil, Ana Maria Bispo de Filippis, Glaucia Paranhos-Baccalà, Alice Banz, and Ester C. Sabino. Performance evaluation of vidas® diagnostic assays detecting anti-chikungunya virus igm and igg antibodies: an international study. Diagnostics, 13:2306, Jul 2023. URL: https://doi.org/10.3390/diagnostics13132306, doi:10.3390/diagnostics13132306. This article has 4 citations.

25. (pereira2023performanceevaluationof pages 15-16): Geovana M. Pereira, Erika R. Manuli, Laurie Coulon, Marina F. Côrtes, Mariana S. Ramundo, Loïc Dromenq, Audrey Larue-Triolet, Frédérique Raymond, Carole Tourneur, Carolina dos Santos Lázari, Patricia Brasil, Ana Maria Bispo de Filippis, Glaucia Paranhos-Baccalà, Alice Banz, and Ester C. Sabino. Performance evaluation of vidas® diagnostic assays detecting anti-chikungunya virus igm and igg antibodies: an international study. Diagnostics, 13:2306, Jul 2023. URL: https://doi.org/10.3390/diagnostics13132306, doi:10.3390/diagnostics13132306. This article has 4 citations.

26. (simo2023chikungunyavirusdiagnosis pages 4-6): Fredy Brice Nemg Simo, Felicity Jane Burt, and Nigel Aminake Makoah. Chikungunya virus diagnosis: a review of current antigen detection methods. Tropical Medicine and Infectious Disease, 8:365, Jul 2023. URL: https://doi.org/10.3390/tropicalmed8070365, doi:10.3390/tropicalmed8070365. This article has 32 citations.

27. (jacobnascimento2025longtermpersistenceof pages 5-7): Leile Camila Jacob-Nascimento, Rosângela O. Anjos, Moyra M. Portilho, Viviane M. Cavalcanti, Adriane S. Paz, Lorena G. Santos, Moisés S. Sousa, Julia G. Costa, Mariane R. Silva, Patrícia S. S. Moreira, Uriel Kitron, Scott C. Weaver, Mittermayer B. Santiago, Mitermayer G. Reis, and Guilherme S. Ribeiro. Long-term persistence of serum igm antibodies against chikungunya virus in patients with chronic arthralgia. Virology Journal, Apr 2025. URL: https://doi.org/10.1186/s12985-025-02721-x, doi:10.1186/s12985-025-02721-x. This article has 6 citations and is from a peer-reviewed journal.

28. (rama2024clinicaloutcomesof media 3fb5798c): Kris Rama, Adrianne M. de Roo, Timon Louwsma, Hinko S. Hofstra, Gabriel S. Gurgel do Amaral, Gerard T. Vondeling, Maarten J. Postma, and Roel D. Freriks. Clinical outcomes of chikungunya: a systematic literature review and meta-analysis. PLOS Neglected Tropical Diseases, 18:e0012254, Jun 2024. URL: https://doi.org/10.1371/journal.pntd.0012254, doi:10.1371/journal.pntd.0012254. This article has 68 citations and is from a domain leading peer-reviewed journal.

29. (irfan2024advancementsinchikungunya pages 1-2): Hamza Irfan and Aliza Ahmed. Advancements in chikungunya virus management: fda approval of ixchiq vaccine and global perspectives. Health Science Reports, Jun 2024. URL: https://doi.org/10.1002/hsr2.2183, doi:10.1002/hsr2.2183. This article has 9 citations and is from a peer-reviewed journal.

30. (maurer2025comprehensiveassessmentof pages 1-2): Gabriele Maurer, Vera Buerger, Julian Larcher-Senn, Florian Erlsbacher, Stéphanie Meyer, Susanne Eder-Lingelbach, and Juan Carlos Jaramillo. Comprehensive assessment of reactogenicity and safety of the live-attenuated chikungunya vaccine (ixchiq®). Vaccines, 13:576, May 2025. URL: https://doi.org/10.3390/vaccines13060576, doi:10.3390/vaccines13060576. This article has 6 citations.

31. (weber2024chikungunyavirusvaccines pages 2-4): Whitney C. Weber, Daniel N. Streblow, and Lark L. Coffey. Chikungunya virus vaccines: a review of ixchiq and pxvx0317 from pre-clinical evaluation to licensure. Biodrugs, 38:727-742, Sep 2024. URL: https://doi.org/10.1007/s40259-024-00677-y, doi:10.1007/s40259-024-00677-y. This article has 49 citations and is from a peer-reviewed journal.

32. (NCT03992872 chunk 1):  Phase 2 Open-label Study of Alum-adjuvanted Chikungunya Virus-like Particle Vaccine (PXVX0317). Bavarian Nordic. 2019. ClinicalTrials.gov Identifier: NCT03992872

33. (NCT06973772 chunk 1):  Trial to Evaluate the Immunogenicity and Safety of the Co-administration of Live Attenuated Dengue and Chikungunya Vaccines Compared to Separate Administration in Adults Aged 18 to 59 Years.. Butantan Institute. 2026. ClinicalTrials.gov Identifier: NCT06973772

34. (freitas2024excessmortalityassociated pages 5-7): André Ricardo Ribas Freitas, Antonio Silva Lima Neto, Rosana Rodrigues, Erneson Alves de Oliveira, José S. Andrade, and Luciano P. G. Cavalcanti. Excess mortality associated with chikungunya epidemic in southeast brazil, 2023. Frontiers in Tropical Diseases, Oct 2024. URL: https://doi.org/10.3389/fitd.2024.1466207, doi:10.3389/fitd.2024.1466207. This article has 13 citations.

35. (jacobnascimento2025longtermpersistenceof pages 1-2): Leile Camila Jacob-Nascimento, Rosângela O. Anjos, Moyra M. Portilho, Viviane M. Cavalcanti, Adriane S. Paz, Lorena G. Santos, Moisés S. Sousa, Julia G. Costa, Mariane R. Silva, Patrícia S. S. Moreira, Uriel Kitron, Scott C. Weaver, Mittermayer B. Santiago, Mitermayer G. Reis, and Guilherme S. Ribeiro. Long-term persistence of serum igm antibodies against chikungunya virus in patients with chronic arthralgia. Virology Journal, Apr 2025. URL: https://doi.org/10.1186/s12985-025-02721-x, doi:10.1186/s12985-025-02721-x. This article has 6 citations and is from a peer-reviewed journal.

36. (rama2024clinicaloutcomesof media 32d1ac79): Kris Rama, Adrianne M. de Roo, Timon Louwsma, Hinko S. Hofstra, Gabriel S. Gurgel do Amaral, Gerard T. Vondeling, Maarten J. Postma, and Roel D. Freriks. Clinical outcomes of chikungunya: a systematic literature review and meta-analysis. PLOS Neglected Tropical Diseases, 18:e0012254, Jun 2024. URL: https://doi.org/10.1371/journal.pntd.0012254, doi:10.1371/journal.pntd.0012254. This article has 68 citations and is from a domain leading peer-reviewed journal.
