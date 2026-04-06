---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T12:24:56.915090'
end_time: '2026-04-04T12:31:28.559228'
duration_seconds: 391.64
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: SHH Holoprosencephaly Spectrum
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** SHH Holoprosencephaly Spectrum
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **SHH Holoprosencephaly Spectrum** covering all of the
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
- **Disease Name:** SHH Holoprosencephaly Spectrum
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **SHH Holoprosencephaly Spectrum** covering all of the
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


## Comprehensive Research Report: SHH Holoprosencephaly Spectrum (HPE3)

### Target disease
- **Disease name:** SHH Holoprosencephaly Spectrum (SHH-related holoprosencephaly; HPE3)
- **Category:** Genetic congenital malformation / neurodevelopmental disorder
- **MONDO ID:** Not retrieved in the available evidence (not inferable from the current tool context).

---

## 1. Disease information

### Overview (what is the disease?)
Holoprosencephaly (HPE) is a congenital forebrain malformation caused by **inadequate or absent midline division of the prosencephalon/forebrain into cerebral hemispheres**, frequently accompanied by midline craniofacial defects. SHH holoprosencephaly spectrum refers to the subset of HPE attributable to pathogenic variation affecting **Sonic hedgehog (*SHH*) signaling** and its dosage. (petryk2015holoprosencephalysignalinginteractions pages 1-3, lavillaureix2023aspectsgénétiquesdu pages 167-172)

Developmentally, HPE arises early in embryogenesis; one review places the critical window for failed cleavage at roughly **gestational days 18–28**. (lavillaureix2023aspectsgénétiquesdu pages 167-172)

### Key identifiers and controlled vocabularies
- **HPE locus name:** **HPE3**, corresponding to the **SHH** gene (singh2009sonichedgehogmutations pages 1-2)
- **Causal gene:** **SHH**; **location 7q36** (castro2021newshhand pages 1-2, singh2009sonichedgehogmutations pages 1-2)
- **MeSH term (clinicaltrials.gov browse):** **Holoprosencephaly** (MeSH **D016142**) (NCT04691414 chunk 1)

### Synonyms / alternative names
- SHH-related holoprosencephaly
- Sonic hedgehog-related holoprosencephaly
- Holoprosencephaly 3 (HPE3)
- SHH-deficiency (SHH-D) spectrum / SHH-dosage disorders (used in some research contexts) (NCT04691414 chunk 1, lavillaureix2023aspectsgénétiquesdu pages 167-172)

### Evidence source type
This entry is derived from **aggregated disease-level resources** (reviews) plus **primary research** (human genetics papers, mouse model studies) and **clinicaltrials.gov registry** descriptions (observational genetics studies). (petryk2015holoprosencephalysignalinginteractions pages 1-3, malta2023holoprosencephalyreviewof pages 9-11, kim2019integratedclinicaland pages 1-2, NCT04691414 chunk 1)

A compact scaffold of the key identifiers, definition, inheritance, and epidemiology is provided in the artifact table below.

| Disease / synonyms | Key identifiers | Brief definition / overview | Inheritance / penetrance / expressivity | Epidemiology |
|---|---|---|---|---|
| **SHH-related holoprosencephaly spectrum**; **holoprosencephaly 3 (HPE3)**; **Sonic hedgehog-related holoprosencephaly**; **SHH-associated holoprosencephaly** | **Locus:** HPE3; **gene:** *SHH*; **chromosomal location:** 7q36; *SHH* was identified as the gene corresponding to the HPE3 locus (singh2009sonichedgehogmutations pages 1-2, castro2021newshhand pages 1-2) | Congenital forebrain malformation caused by incomplete midline division of the prosencephalon, typically arising between gestational days 18–28; part of a broad spectrum from severe alobar forms with major craniofacial anomalies to mild microforms (lavillaureix2023aspectsgénétiquesdu pages 167-172, petryk2015holoprosencephalysignalinginteractions pages 1-3, chafiq2024alobarholoprosencephalyin pages 1-3) | Usually **autosomal dominant** for *SHH* pathogenic variants, but with **incomplete penetrance** and **variable expressivity**; some cases are sporadic, and oligogenic/modifier effects are increasingly recognized. One review notes that only about **37% of human carriers of SHH mutations develop HPE** (petryk2015holoprosencephalysignalinginteractions pages 1-3, roessler2018commongeneticcauses pages 1-5, kim2019integratedclinicaland pages 1-2) | HPE overall occurs in about **1 in 250 conceptuses/fetuses** and about **1 in 10,000 live births/live-born infants** (petryk2015holoprosencephalysignalinginteractions pages 1-3, roessler2018commongeneticcauses pages 1-5, lavillaureix2023aspectsgénétiquesdu pages 175-177) |


*Table: This table summarizes core disease-level facts for SHH-related holoprosencephaly spectrum, including naming, identifiers, overview, inheritance, and headline epidemiology. It is useful as a compact knowledge-base entry scaffold grounded only in the cited evidence contexts.*

---

## 2. Etiology

### Disease causal factors
**Primary cause (genetic):** Pathogenic variants affecting *SHH* and SHH-pathway genes reduce effective SHH signaling, producing a midline patterning defect of brain and face. *SHH* is repeatedly described as a major and historically first-identified gene in non-chromosomal HPE, with HPE3 mapping to *SHH*. (castro2021newshhand pages 1-2, singh2009sonichedgehogmutations pages 1-2, lavillaureix2023aspectsgénétiquesdu pages 167-172)

**Mechanistic framing:** Disruption of SHH signaling is described as a central pathophysiologic mechanism underlying HPE. (malta2023holoprosencephalyreviewof pages 9-11)

### Risk factors
**Genetic risk factors (driver and modifier genes):**
- Reviews emphasize that HPE commonly shows **incomplete penetrance and variable expressivity**, and that **modifier effects/oligogenic inheritance** contribute to phenotypic variability and diagnostic complexity. (petryk2015holoprosencephalysignalinginteractions pages 1-3, kim2019integratedclinicaland pages 1-2, lavillaureix2023aspectsgénétiquesdu pages 175-177)
- In a large NGS study, Roessler et al. propose a “**simple autosomal dominant with modifier pattern accounting for 25% of the molecular pathology**” of HPE, while noting persistent unexplained incomplete penetrance/variable expressivity. (roessler2018commongeneticcauses pages 1-5)
- In an integrative omics analysis under an oligogenic model, Kim et al. report variants of clinical interest across many genes enriched for pathways including **SHH and primary cilia**, and oligogenic events enriched in cases vs controls (P=10^-9). (kim2019integratedclinicaland pages 1-2)

**Environmental/teratogenic risk factors (gene–environment interaction context):**
HPE has both genetic and environmental etiologies, and developmental biology reviews explicitly list examples such as **maternal diabetes, ethanol, and retinoic acid** as environmental causes/risks, with HPE often used as a model for multifactorial etiology. (petryk2015holoprosencephalysignalinginteractions pages 1-3)

### Protective factors
Evidence for protective factors in the retrieved corpus is limited. One 2023 clinical review reports an association suggesting **folic acid may be protective**, citing a **73% risk reduction** when taken in the first month in one study (details of the underlying study are not provided in the extracted text). (malta2023holoprosencephalyreviewof pages 9-11)

### Gene–environment interactions
Direct experimental evidence that genetic lesions in the Hedgehog pathway can **sensitize** embryos to environmental teratogens is provided by mouse work in which heterozygous **Gli2** variants increased penetrance/severity of HPE after low-dose exposure, supporting a mechanistic model where “normally silent genetic and environmental factors can interact to produce severe outcomes.” (petryk2015holoprosencephalysignalinginteractions pages 1-3)

---

## 3. Phenotypes

### Conceptualization: “HPE spectrum” and SHH-specific variability
HPE is widely described as a **nearly continuous spectrum**, from severe malformations (e.g., alobar HPE with cyclopia) to **mild microforms** (e.g., solitary median maxillary central incisor, hypotelorism) that may occur with subtle or absent classic brain non-separation on imaging. (petryk2015holoprosencephalysignalinginteractions pages 1-3, lavillaureix2023aspectsgénétiquesdu pages 167-172, malta2023holoprosencephalyreviewof pages 2-4)

A key clinical point relevant for SHH-related disease is that **facial severity often correlates with brain malformation severity**, although exceptions exist by gene and mechanism. (lavillaureix2023aspectsgénétiquesdu pages 167-172, malta2023holoprosencephalyreviewof pages 2-4)

### Radiologic/clinical subtypes (and a visual summary)
The 2023 clinical review provides a structured classification of HPE including alobar, semilobar, lobar, middle interhemispheric variant (MIH/syntelencephaly), and microforms/minimal forms. (malta2023holoprosencephalyreviewof pages 2-4)

The same review includes a classification table summarizing major radiologic and clinical features across the spectrum (Table 1 shown in the retrieved image). (malta2023holoprosencephalyreviewof media b1f62008)

### Common clinical features and complications (selected)
From the 2023 review and a 2024 case review:
- **Hydrocephalus:** reported frequency **16–40%**; may require shunting. (malta2023holoprosencephalyreviewof pages 4-6)
- **Seizures/epilepsy:** approximately **~50%**. (malta2023holoprosencephalyreviewof pages 4-6)
- **Feeding/oromotor difficulties:** common, including issues related to midline clefting. (malta2023holoprosencephalyreviewof pages 4-6)
- **Endocrine/hypothalamic–pituitary dysfunction:** diabetes insipidus, adrenal hypoplasia, hypogonadism, thyroid hypoplasia, growth hormone deficiency are noted as common in some clinical summaries of HPE. (chafiq2024alobarholoprosencephalyin pages 1-3)

### Suggested HPO terms (non-exhaustive; for knowledge base mapping)
The following HPO mappings are consistent with phenotypes described in the retrieved evidence:
- Holoprosencephaly: **HP:0001360**
- Alobar holoprosencephaly: **HP:0002506**
- Semilobar holoprosencephaly: **HP:0002510**
- Lobar holoprosencephaly: **HP:0002508**
- Hypotelorism: **HP:0000601** (petryk2015holoprosencephalysignalinginteractions pages 1-3, lavillaureix2023aspectsgénétiquesdu pages 167-172)
- Cleft lip and/or palate: **HP:0000204 / HP:0000175** (lavillaureix2023aspectsgénétiquesdu pages 167-172, malta2023holoprosencephalyreviewof pages 4-6)
- Solitary median maxillary central incisor (SMMCI): **HP:0006313** (petryk2015holoprosencephalysignalinginteractions pages 1-3, galeotti2024useofan pages 1-2)
- Congenital nasal pyriform aperture stenosis (CNPAS): **HP:0012722** (galeotti2024useofan pages 1-2)
- Seizures: **HP:0001250** (malta2023holoprosencephalyreviewof pages 4-6)
- Hydrocephalus: **HP:0000238** (malta2023holoprosencephalyreviewof pages 4-6)

Note: HPO IDs are provided for ontology mapping convenience; the underlying phenotype assertions are supported by the cited sources.

---

## 4. Genetic / molecular information

### Causal gene
- **SHH (Sonic Hedgehog)** is the defining causal gene for HPE3/SHH-related holoprosencephaly spectrum. (castro2021newshhand pages 1-2, singh2009sonichedgehogmutations pages 1-2)

### Pathogenic variant concepts
The retrieved evidence supports a range of mechanistic classes for reduced SHH signaling in HPE:
- **Haploinsufficiency / reduced effective dosage** with **incomplete penetrance and variable expressivity** is emphasized in human families with heterozygous variants. (petryk2015holoprosencephalysignalinginteractions pages 1-3, castro2021newshhand pages 1-2)
- Functional molecular work indicates SHH variants can disrupt distinct steps of SHH biogenesis to attenuate activity to different levels, and can also act in dominant-negative ways in some contexts (mechanistic summary in review-level extract). (singh2009sonichedgehogmutations pages 1-2)

### Penetrance and expressivity (quantitative)
A developmental biology review reports that **“Only about 37% of human carriers of SHH mutations develop HPE”**, emphasizing incomplete penetrance. (petryk2015holoprosencephalysignalinginteractions pages 1-3)

### Modifier genes / oligogenic inheritance
Multiple sources describe oligogenic inheritance and modifier effects:
- An integrative clinical/omics approach found enrichment of variants across genes linked to forebrain development pathways including SHH and primary cilia, consistent with complex inheritance. (kim2019integratedclinicaland pages 1-2)
- A 2023 genetics thesis-style review notes that many SHH-dosage cases remain genetically unsolved and highlights oligogenic inheritance and modifiers as contributors to variability. (lavillaureix2023aspectsgénétiquesdu pages 175-177)

### Epigenetic information
No SHH-HPE-specific epigenetic (methylation/histone/chromatin) mechanisms were directly extracted in the retrieved evidence.

### Chromosomal abnormalities
Although SHH-HPE is monogenic, HPE overall frequently includes chromosomal etiologies; recent case-based and review evidence notes that **25–50%** of HPE may have chromosomal abnormalities (commonly trisomy 13). (galeotti2024useofan pages 1-2)

---

## 5. Environmental information

HPE etiology includes environmental/teratogenic contributors; reviews list maternal diabetes, ethanol, and retinoic acid among examples discussed in the context of multifactorial causation and gene–environment interactions. (petryk2015holoprosencephalysignalinginteractions pages 1-3)

The retrieved evidence did not provide quantified attributable risk fractions for specific exposures in SHH-variant carriers.

---

## 6. Mechanism / pathophysiology

### Key pathway (current understanding)
The canonical SHH pathway (ligand processing and downstream transduction via PTCH/SMO/GLI) is central to ventral midline patterning of the forebrain and craniofacial development; impaired activity is repeatedly described as causal for HPE phenotypes. (singh2009sonichedgehogmutations pages 1-2, malta2023holoprosencephalyreviewof pages 9-11)

### Molecular causal chain (from trigger to phenotype)
1. **Trigger:** Germline pathogenic variation affecting *SHH* dosage/activity (or combined variants in SHH-pathway/modifier genes), sometimes combined with environmental exposures. (petryk2015holoprosencephalysignalinginteractions pages 1-3, kim2019integratedclinicaland pages 1-2)
2. **Molecular consequence:** Reduced effective SHH ligand activity. Mechanistically, SHH is produced as a preprotein that is cleaved into N- and C-terminal domains; the C-terminal domain mediates cholesterol modification of the N-terminal ligand, and the ligand is further palmitoylated, affecting secretion and signaling potency. (singh2009sonichedgehogmutations pages 1-2)
3. **Signal transduction disruption:** Altered activation of the Hedgehog signaling cascade involving PTCH/SMO and GLI transcription factors, reducing downstream transcriptional programs needed for ventral forebrain specification and midline craniofacial morphogenesis. (singh2009sonichedgehogmutations pages 1-2)
4. **Developmental outcome:** Failed or incomplete midline cleavage of the forebrain with a correlated craniofacial midline defect spectrum, yielding alobar/semilobar/lobar HPE and microforms. (malta2023holoprosencephalyreviewof pages 2-4, lavillaureix2023aspectsgénétiquesdu pages 167-172)

### Upstream vs downstream
- **Upstream:** SHH ligand biogenesis (cleavage, lipid modification), secretion and dosage regulation; modifier genes that tune pathway strength; environmental factors that reduce pathway signaling below developmental thresholds. (singh2009sonichedgehogmutations pages 1-2, petryk2015holoprosencephalysignalinginteractions pages 1-3)
- **Downstream:** Reduced pathway-driven transcriptional patterning programs (GLI-dependent) leading to morphogenetic defects in brain and face. (singh2009sonichedgehogmutations pages 1-2, lavillaureix2023aspectsgénétiquesdu pages 167-172)

### Gene–environment mechanism (example)
A mouse model demonstrates that **Gli2 dosage-dependent attenuation** of Hedgehog responsiveness can convert a “normally silent” predisposition into severe HPE outcomes when combined with a low-dose teratogen exposure, supporting a threshold model for pathway failure. (petryk2015holoprosencephalysignalinginteractions pages 1-3)

### Suggested ontology terms
**GO biological process (examples):**
- Hedgehog signaling pathway: **GO:0007224**
- Forebrain development: **GO:0030900**
- Craniofacial development: **GO:0060322**

**Cell types (CL; examples likely involved):**
- Neuroepithelial cell / neural progenitor (ventral forebrain progenitors)
- Cranial neural crest cell (relevant to craniofacial midline development)

**Pathway resources:** Mechanistic details align with canonical Hedgehog signaling represented in major pathway databases; however, pathway-database URLs were not retrieved in the current tool context.

---

## 7. Anatomical structures affected

**Primary affected structures:**
- Forebrain/prosencephalon and midline brain structures (petryk2015holoprosencephalysignalinginteractions pages 1-3, malta2023holoprosencephalyreviewof pages 2-4)
- Craniofacial midline (including nasal and oral structures) (lavillaureix2023aspectsgénétiquesdu pages 167-172, galeotti2024useofan pages 1-2)

**Representative UBERON suggestions:**
- Forebrain: **UBERON:0001890**
- Prosencephalon: **UBERON:0001891**
- Face: **UBERON:0001456**
- Maxilla: **UBERON:0002397**

---

## 8. Temporal development

- **Onset:** Congenital; critical early embryonic window for prosencephalon cleavage is during early gestation (days ~18–28 in one summary). (lavillaureix2023aspectsgénétiquesdu pages 167-172)
- **Progression/course:** Structural malformation is non-progressive, but clinical course depends on severity and complications (hydrocephalus, seizures, endocrine dysfunction, feeding impairment), requiring long-term multidisciplinary care in survivors. (malta2023holoprosencephalyreviewof pages 4-6)

---

## 9. Inheritance and population

### Epidemiology
HPE overall is commonly reported as occurring in approximately **1:250 conceptuses/fetuses** and **~1:10,000 live births/live-born infants**. (petryk2015holoprosencephalysignalinginteractions pages 1-3, roessler2018commongeneticcauses pages 1-5, lavillaureix2023aspectsgénétiquesdu pages 175-177)

### Inheritance (SHH-related)
- Typically **autosomal dominant** with **incomplete penetrance** and **variable expressivity**. (petryk2015holoprosencephalysignalinginteractions pages 1-3, castro2021newshhand pages 1-2)
- Penetrance estimate reported in a review: **~37%** of SHH mutation carriers develop HPE. (petryk2015holoprosencephalysignalinginteractions pages 1-3)

### Genetic counseling implications
Because penetrance is incomplete and expressivity is variable, recurrence risk may be substantial when a pathogenic variant is present in a parent; one 2023 clinical review provides a general example of **up to 50% recurrence risk** when a parent carries a mutation with incomplete penetrance (not SHH-specific but relevant to autosomal-dominant HPE genes including SHH). (malta2023holoprosencephalyreviewof pages 9-11)

---

## 10. Diagnostics

### Imaging
- **Prenatal ultrasound:** Severe forms can be detected in the first trimester; milder forms can be missed. (malta2023holoprosencephalyreviewof pages 9-11)
- **Fetal MRI:** recommended as a **second-line prenatal study**. (malta2023holoprosencephalyreviewof pages 9-11)
- **Postnatal MRI:** described as the **imaging modality of choice** for HPE diagnosis. (malta2023holoprosencephalyreviewof pages 9-11)

The 2024 case report/review also illustrates real-world practice: prenatal ultrasound diagnosis followed by postnatal brain MRI confirmation. (chafiq2024alobarholoprosencephalyin pages 1-3)

### Genetic testing strategy (real-world implementation)
A 2023 clinical review proposes a stepwise approach:
1. Start with **chromosomal analysis**; if aneuploidy suspected use **karyotype**, otherwise **chromosomal microarray (CMA)** as first-line. (malta2023holoprosencephalyreviewof pages 9-11)
2. If unrevealing and/or syndromic, proceed to **targeted gene panels** or **exome sequencing**; the review reports **~22% yield** for exome in a mixed cohort. (malta2023holoprosencephalyreviewof pages 9-11)

### Clinical research implementations (NGS to improve counseling)
- **NCT04691414 (EXOMEDIANE; Rennes University Hospital):** retrospective NGS on biobanked DNA to improve genetic counseling for craniofacial midline defects/HPE, noting that “**70% of cases … do not have a molecular diagnosis**” in their summary rationale. Posted 2020-12-31; completed 2021-12-06. URL: https://clinicaltrials.gov/study/NCT04691414 (NCT04691414 chunk 1)
- **NCT00645645 (NIH NHGRI):** long-running observational cohort emphasizing mutational analysis of HPE genes; the registry summary states: “**Mutations in one such gene, Sonic Hedgehog, have been shown by us to be responsible for approximately one quarter of familial cases of HPE.**” First posted 2008-03-28; updated 2021-12-14. URL: https://clinicaltrials.gov/study/NCT00645645 (NCT00645645 chunk 1)

### Differential diagnosis
The retrieved evidence emphasizes that HPE has heterogeneous etiologies including chromosomal anomalies and other monogenic syndromes; a structured differential diagnosis list was not directly extracted in the available snippets. (malta2023holoprosencephalyreviewof pages 9-11, galeotti2024useofan pages 1-2)

---

## 11. Outcome / prognosis

### Survival and mortality (statistics)
A 2024 case review and the 2023 clinical review provide quantitative survival statistics for severe HPE (particularly alobar):
- **~33%** die within the first **24 hours**
- **~58%** die within the first **month**
- **~29%** survive to **1 year** (chafiq2024alobarholoprosencephalyin pages 4-5, malta2023holoprosencephalyreviewof pages 4-6)

### Morbidity
Survivors frequently require long-term multidisciplinary care due to neurologic disability, seizures, feeding difficulties, endocrine dysfunction, and complications such as hydrocephalus. (chafiq2024alobarholoprosencephalyin pages 1-3, malta2023holoprosencephalyreviewof pages 4-6)

---

## 12. Treatment

### Disease-modifying therapy
No disease-modifying pharmacotherapy for congenital SHH-related HPE was identified in the retrieved evidence. Management is described as **supportive** and multidisciplinary. (petryk2015holoprosencephalysignalinginteractions pages 1-3, malta2023holoprosencephalyreviewof pages 4-6)

### Supportive and interventional care (real-world implementations)
- **Hydrocephalus management:** shunt placement when needed (hydrocephalus frequency 16–40%). (malta2023holoprosencephalyreviewof pages 4-6)
- **Seizure management:** antiepileptic treatment guided by clinical neurology (seizures ~50%). (malta2023holoprosencephalyreviewof pages 4-6)
- **Feeding support:** addressing feeding difficulties, sometimes related to clefts. (malta2023holoprosencephalyreviewof pages 4-6)
- **Endocrine management:** addressing diabetes insipidus and pituitary hormone deficiencies in affected individuals. (chafiq2024alobarholoprosencephalyin pages 1-3)

**Example of implemented craniofacial/airway management in mild-spectrum HPE:**
- In an infant with mild HPE features (SMMCI) and **congenital nasal pyriform aperture stenosis (CNPAS)**, a combined ENT–orthodontic approach used **balloon dilation** and a **neonatal palatal expander plate** to improve airway patency and sucking/swallowing. (May 2024; https://doi.org/10.3390/children11050554) (galeotti2024useofan pages 1-2)

### Suggested MAXO terms (examples)
- Genetic counseling: **MAXO:0000077** (term label may vary across MAXO versions)
- Magnetic resonance imaging: **MAXO:0000715** (imaging procedure term; label may vary)
- Ventriculoperitoneal shunt placement / CSF shunting: surgical intervention term
- Feeding support / enteral feeding: supportive care term

(MAXO IDs are suggested for mapping; specific MAXO identifiers should be validated against the version used in your KB.)

---

## 13. Prevention

### Primary prevention
No specific primary prevention is established for SHH-variant carriers in the retrieved evidence. One review states “Currently, there are no effective preventive methods for HPE,” emphasizing the need for deeper mechanistic understanding for prevention. (petryk2015holoprosencephalysignalinginteractions pages 1-3)

### Secondary prevention / early detection
- Prenatal screening/diagnosis via ultrasound and fetal MRI facilitates counseling and perinatal planning. (malta2023holoprosencephalyreviewof pages 9-11, chafiq2024alobarholoprosencephalyin pages 1-3)

### Counseling and reproductive options
The 2023 clinical review emphasizes balanced prognostic counseling and involving genetics professionals for recurrence estimation; prenatal genetic testing via amniotic fluid is possible. (malta2023holoprosencephalyreviewof pages 9-11)

---

## 14. Other species / natural disease

The retrieved evidence did not provide naturally occurring veterinary cases for SHH-related HPE. However, experimental developmental biology literature highlights conserved SHH function across vertebrates, and the phenotype is commonly modeled in mice. (petryk2015holoprosencephalysignalinginteractions pages 1-3)

---

## 15. Model organisms

### Key models and what they show
- **Shh-null mouse embryos:** described as having **fully penetrant** severe HPE, supporting a strong causal role for SHH in midline development and providing a baseline for understanding incomplete penetrance in humans. (petryk2015holoprosencephalysignalinginteractions pages 1-3)
- **Gli2 gene–environment interaction mouse model:** heterozygous Gli2 variants increase penetrance/severity after low-dose teratogen exposure, demonstrating a mechanistic basis for variable expressivity and prevention-focused research framing. (petryk2015holoprosencephalysignalinginteractions pages 1-3)

### Model limitations
Mouse Shh-null is fully penetrant and typically much more severe than the human heterozygous state, limiting direct translation to human incomplete penetrance scenarios but enabling mechanistic dissection of pathway thresholds and modifier effects. (petryk2015holoprosencephalysignalinginteractions pages 1-3)

---

## Recent developments and latest research emphasis (2023–2024)

1. **Updated, clinically oriented synthesis (2023):** Malta et al. (Mar 2023; https://doi.org/10.3390/children10040647) consolidates classification, imaging-based diagnosis, genetic testing strategy (CMA→panel/exome), complication rates (e.g., hydrocephalus 16–40%, seizures ~50%), and survival statistics, reflecting current clinical workflows. (malta2023holoprosencephalyreviewof pages 4-6, malta2023holoprosencephalyreviewof pages 9-11)
2. **Implementation-level multidisciplinary care reports (2024):** case reports describe integrated surgical/orthodontic airway management for CNPAS in mild-spectrum HPE, demonstrating real-world interventions for survivable sub-phenotypes. (May 2024; https://doi.org/10.3390/children11050554) (galeotti2024useofan pages 1-2)
3. **Improving diagnostic yield and counseling via NGS (ongoing/registry evidence):** EXOMEDIANE (NCT04691414) and NIH cohort protocols (NCT00645645) indicate continuing efforts to use sequencing to improve gene discovery and counseling, reflecting the recognized gap that many cases remain molecularly unsolved. (NCT04691414 chunk 1, NCT00645645 chunk 1)

---

## Expert opinion / analysis (from authoritative sources in the retrieved evidence)

- **Incomplete penetrance and variable expressivity are fundamental to SHH-related HPE** and remain partially unexplained despite large-scale sequencing, supporting continued work on modifier genes and gene–environment interactions. (roessler2018commongeneticcauses pages 1-5, petryk2015holoprosencephalysignalinginteractions pages 1-3)
- The current best-supported clinical approach prioritizes **imaging for diagnosis/severity stratification** and uses a **tiered genetic testing strategy** (chromosomal analysis → sequencing), aligning with the heterogeneity of causes. (malta2023holoprosencephalyreviewof pages 9-11)

---

## Notes on gaps / limitations of this report
- Formal mapping to **MONDO, Orphanet, ICD-10/ICD-11** identifiers and *SHH* OMIM IDs was not retrievable from the current tool evidence; these should be added from OMIM/Orphanet in a subsequent pass.
- Variant-level details (HGVS, ClinVar frequencies, gnomAD allele frequencies) were not directly accessible in the retrieved text snippets; therefore, variant cataloging is limited to conceptual classes rather than enumerated variants.

---

## Key citations (URLs and dates where available)
- Malta M, et al. *Children*. **2023-03**. “Holoprosencephaly: Review of Embryology, Clinical Phenotypes, Etiology and Management.” https://doi.org/10.3390/children10040647 (malta2023holoprosencephalyreviewof pages 4-6, malta2023holoprosencephalyreviewof pages 9-11)
- Chafiq K, et al. *Cureus*. **2024-11**. “Alobar Holoprosencephaly in a Newborn: A Case Report…” https://doi.org/10.7759/cureus.74462 (chafiq2024alobarholoprosencephalyin pages 4-5, chafiq2024alobarholoprosencephalyin pages 1-3)
- Petryk A, et al. *WIREs Dev Biol*. **2015-10**. https://doi.org/10.1002/wdev.161 (petryk2015holoprosencephalysignalinginteractions pages 1-3)
- Roessler E, et al. *Hum Mutat*. **2018-07**. https://doi.org/10.1002/humu.23590 (roessler2018commongeneticcauses pages 1-5)
- Kim A, et al. *Brain*. **2019-11**. https://doi.org/10.1093/brain/awy290 (kim2019integratedclinicaland pages 1-2)
- de Castro VF, et al. *Molecular Syndromology*. **2021-06**. https://doi.org/10.1159/000515044 (castro2021newshhand pages 1-2)
- Singh S, et al. *Hum Genet*. **2009-12**. https://doi.org/10.1007/s00439-008-0599-0 (singh2009sonichedgehogmutations pages 1-2)
- ClinicalTrials.gov NCT04691414 (EXOMEDIANE). First posted **2020-12-31**; completed **2021-12-06**. https://clinicaltrials.gov/study/NCT04691414 (NCT04691414 chunk 1)
- ClinicalTrials.gov NCT00645645. First posted **2008-03-28**; updated **2021-12-14**. https://clinicaltrials.gov/study/NCT00645645 (NCT00645645 chunk 1)


References

1. (petryk2015holoprosencephalysignalinginteractions pages 1-3): Anna Petryk, Daniel Graf, and Ralph Marcucio. Holoprosencephaly: signaling interactions between the brain and the face, the environment and the genes, and the phenotypic variability in animal models and humans. Wiley Interdisciplinary Reviews: Developmental Biology, 4:17-32, Oct 2015. URL: https://doi.org/10.1002/wdev.161, doi:10.1002/wdev.161. This article has 132 citations.

2. (lavillaureix2023aspectsgénétiquesdu pages 167-172): A Lavillaureix. Aspects génétiques du développement cérébral, holoprosencéphalie et élargissement du spectre phénotypique aux pathologies liées à la voie de signalisation shh. Unknown journal, 2023.

3. (singh2009sonichedgehogmutations pages 1-2): Samer Singh, Robert Tokhunts, Valerie Baubet, John A. Goetz, Zhen Jane Huang, Neal S. Schilling, Kendall E. Black, Todd A. MacKenzie, Nadia Dahmane, and David J. Robbins. Sonic hedgehog mutations identified in holoprosencephaly patients can act in a dominant negative manner. Human Genetics, 125:95-103, Dec 2009. URL: https://doi.org/10.1007/s00439-008-0599-0, doi:10.1007/s00439-008-0599-0. This article has 44 citations and is from a peer-reviewed journal.

4. (castro2021newshhand pages 1-2): Viviane Freitas de Castro, Daniel Mattos, Flavia Martinez de Carvalho, Denise Pontes Cavalcanti, Milagros M. Duenas-Roque, Juan Llerena Jr, Viviana Raquel Cosentino, Rachel Sayuri Honjo, Julio Cesar Loguercio Leite, Maria Teresa Sanseverino, Márcia Pereira Alves de Souza, Pricila Bernardi, Ana Maria Bolognese, Luiz Carlos Santana da Silva, Pablo Barbero, Patricia Santana Correia, Larissa Souza Mario Bueno, Clarice Pagani Savastano, and Iêda Maria Orioli. New shh and known six3 variants in a series of latin american patients with holoprosencephaly. Molecular Syndromology, 12:219-233, Jun 2021. URL: https://doi.org/10.1159/000515044, doi:10.1159/000515044. This article has 3 citations and is from a peer-reviewed journal.

5. (NCT04691414 chunk 1):  Retrospective Study Using Next Generation Sequencing (NGS) on Biological Samples to Improve Genetic Counseling for Patients With Previously Explored Craniofacial Midline Defects.. Rennes University Hospital. 2021. ClinicalTrials.gov Identifier: NCT04691414

6. (malta2023holoprosencephalyreviewof pages 9-11): Maísa Malta, Rowim AlMutiri, Christine Saint Martin, and Myriam Srour. Holoprosencephaly: review of embryology, clinical phenotypes, etiology and management. Children, 10:647, Mar 2023. URL: https://doi.org/10.3390/children10040647, doi:10.3390/children10040647. This article has 37 citations.

7. (kim2019integratedclinicaland pages 1-2): Artem Kim, Clara Savary, Christèle Dubourg, Wilfrid Carré, Charlotte Mouden, Houda Hamdi-Rozé, Hélène Guyodo, Jerome Le Douce, Emmanuelle Génin, Dominique Campion, Jean-François Dartigues, Jean-François Deleuze, Jean-Charles Lambert, Richard Redon, Thomas Ludwig, Benjamin Grenier-Boley, Sébastien Letort, Pierre Lindenbaum, Vincent Meyer, Olivier Quenez, Christian Dina, Céline Bellenguez, Camille Charbonnier-Le Clézio, Joanna Giemza, Stéphanie Chatel, Claude Férec, Hervé Le Marec, Luc Letenneur, Gaël Nicolas, Karen Rouault, Delphine Bacq, Anne Boland, Doris Lechner, Cisca Wijmenga, Morris A Swertz, P Eline Slagboom, Gert-Jan B van Ommen, Cornelia M van Duijn, Dorret I Boomsma, Paul I W de Bakker, Jasper A Bovenberg, P Eline Slagboom, Anton J M de Craen, Marian Beekman, Albert Hofman, Dorret I Boomsma, Gonneke Willemsen, Bruce Wolffenbuttel, Mathieu Platteel, Yuanping Du, Ruoyan Chen, Hongzhi Cao, Rui Cao, Yushen Sun, Jeremy Sujie Cao, Morris A Swertz, Freerk van Dijk, Pieter B T Neerincx, Patrick Deelen, Martijn Dijkstra, George Byelas, Alexandros Kanterakis, Jan Bot, Kai Ye, Eric-Wubbo Lameijer, Martijn Vermaat, Jeroen F J Laros, Johan T den Dunnen, Peter de Knijff, Lennart C Karssen, Elisa M van Leeuwen, Najaf Amin, Vyacheslav Koval, Fernando Rivadeneira, Karol Estrada, Jayne Y Hehir-Kwa, Joep de Ligt, Abdel Abdellaoui, Jouke-Jan Hottenga, V Mathijs Kattenberg, David van Enckevort, Hailiang Mei, Mark Santcroos, Barbera D C van Schaik, Robert E Handsaker, Steven A McCarroll, Evan E Eichler, Arthur Ko, Peter Sudmant, Laurent C Francioli, Wigard P Kloosterman, Isaac J Nijman, Victor Guryev, Paul I W de Bakker, Laurent Pasquier, Elisabeth Flori, Marie Gonzales, Claire Bénéteau, Odile Boute, Tania Attié-Bitach, Joelle Roume, Louise Goujon, Linda Akloul, Sylvie Odent, Erwan Watrin, Valérie Dupé, Marie de Tayrac, and Véronique David. Integrated clinical and omics approach to rare diseases: novel genes and oligogenic inheritance in holoprosencephaly. Brain, 142:35-49, Nov 2019. URL: https://doi.org/10.1093/brain/awy290, doi:10.1093/brain/awy290. This article has 60 citations and is from a highest quality peer-reviewed journal.

8. (chafiq2024alobarholoprosencephalyin pages 1-3): Kamal Chafiq, Khalil Toumi, Fatima Ezzahra Khayi, and Abdellatif Daoudi. Alobar holoprosencephaly in a newborn: a case report of prenatal diagnosis and a review of the literature. Cureus, Nov 2024. URL: https://doi.org/10.7759/cureus.74462, doi:10.7759/cureus.74462. This article has 4 citations.

9. (roessler2018commongeneticcauses pages 1-5): E. Roessler, P. Hu, Juliana Marino, Sungkook Hong, R. Hart, Seth I. Berger, Ariel F. Martinez, Yu Abe, P. Kruszka, James W. Thomas, J. Mullikin, Nisc Comparative Sequencing Program, Yupeng Wang, Wendy S. W. Wong, J. Niederhuber, Benjamin D. Solomon, Benjamin D. Solomon, A. Richieri‐Costa, L. Ribeiro-Bicudo, and M. Muenke. Common genetic causes of holoprosencephaly are limited to a small set of evolutionarily conserved driver genes of midline development coordinated by tgf‐β, hedgehog, and fgf signaling. Human Mutation, 39:1416-1427, Jul 2018. URL: https://doi.org/10.1002/humu.23590, doi:10.1002/humu.23590. This article has 31 citations and is from a domain leading peer-reviewed journal.

10. (lavillaureix2023aspectsgénétiquesdu pages 175-177): A Lavillaureix. Aspects génétiques du développement cérébral, holoprosencéphalie et élargissement du spectre phénotypique aux pathologies liées à la voie de signalisation shh. Unknown journal, 2023.

11. (malta2023holoprosencephalyreviewof pages 2-4): Maísa Malta, Rowim AlMutiri, Christine Saint Martin, and Myriam Srour. Holoprosencephaly: review of embryology, clinical phenotypes, etiology and management. Children, 10:647, Mar 2023. URL: https://doi.org/10.3390/children10040647, doi:10.3390/children10040647. This article has 37 citations.

12. (malta2023holoprosencephalyreviewof media b1f62008): Maísa Malta, Rowim AlMutiri, Christine Saint Martin, and Myriam Srour. Holoprosencephaly: review of embryology, clinical phenotypes, etiology and management. Children, 10:647, Mar 2023. URL: https://doi.org/10.3390/children10040647, doi:10.3390/children10040647. This article has 37 citations.

13. (malta2023holoprosencephalyreviewof pages 4-6): Maísa Malta, Rowim AlMutiri, Christine Saint Martin, and Myriam Srour. Holoprosencephaly: review of embryology, clinical phenotypes, etiology and management. Children, 10:647, Mar 2023. URL: https://doi.org/10.3390/children10040647, doi:10.3390/children10040647. This article has 37 citations.

14. (galeotti2024useofan pages 1-2): Angela Galeotti, Giovanni Carlo De Vincentiis, Emanuela Sitzia, Giuseppe Marzo, Wanda Maldonato, Gaia Bompiani, Maria Beatrice Chiarini Testa, Alessandra Putrino, Andrea Bartuli, and Paola Festa. Use of an orthodontic and otolaryngological approach in an infant with holoprosencephaly. Children, 11:554, May 2024. URL: https://doi.org/10.3390/children11050554, doi:10.3390/children11050554. This article has 6 citations.

15. (NCT00645645 chunk 1):  A Study of the Genetic Analysis of Brain Disorders. National Human Genome Research Institute (NHGRI). 2008. ClinicalTrials.gov Identifier: NCT00645645

16. (chafiq2024alobarholoprosencephalyin pages 4-5): Kamal Chafiq, Khalil Toumi, Fatima Ezzahra Khayi, and Abdellatif Daoudi. Alobar holoprosencephaly in a newborn: a case report of prenatal diagnosis and a review of the literature. Cureus, Nov 2024. URL: https://doi.org/10.7759/cureus.74462, doi:10.7759/cureus.74462. This article has 4 citations.