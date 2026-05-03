---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-26T20:01:54.893976'
end_time: '2026-04-26T20:22:58.757876'
duration_seconds: 1263.86
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Wolf-Hirschhorn syndrome
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 46
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Wolf-Hirschhorn syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Wolf-Hirschhorn syndrome** covering all of the
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
- **Disease Name:** Wolf-Hirschhorn syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Wolf-Hirschhorn syndrome** covering all of the
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


# Wolf–Hirschhorn syndrome (WHS): Disease Characteristics Research Report

**Target disease:** Wolf–Hirschhorn syndrome (genetic contiguous gene deletion disorder; distal 4p deletion). (nevado2020internationalmeetingon pages 3-4, zollino2008onthenosology pages 1-2)

## Executive summary (current understanding)
Wolf–Hirschhorn syndrome (WHS) is a *contiguous gene deletion syndrome* caused by loss of genetic material from the distal short arm of chromosome 4 (4p16.3). It is clinically characterized by a recognizable core phenotype comprising typical craniofacial dysmorphism (“Greek warrior helmet” gestalt), prenatal/postnatal growth deficiency, developmental delay/intellectual disability, and seizures/EEG abnormalities. (nevado2020internationalmeetingon pages 3-4, berrocoso2020copingwithwolfhirschhorna pages 1-2, zollino2008onthenosology pages 1-2)

Recent large-cohort work (Spain/Latin America, n=140; collected 2013–2023) underscores that epilepsy is highly prevalent (92%), begins in infancy (mean onset ~9.8 months), and is frequently severe (status epilepticus 58.4%), with substantial treatment burden (polytherapy common). (blancolago2025epilepsyinwolf–hirschhorn pages 2-4, blancolago2025epilepsyinwolf–hirschhorn pages 1-2)

A major mechanistic advance over the last decade is the refinement of a *terminal 4p seizure susceptibility region* to an ~197 kb interval near the telomere (hg19/GRCh37 chr4:367,691–564,593), containing **PIGG** and **ZNF721** (and ABCA11P), suggesting that seizure risk is driven by haploinsufficiency of telomeric genes beyond the historically emphasized **LETM1** region in at least some individuals. (ho2016chromosomalmicroarraytesting pages 1-1, ho2016chromosomalmicroarraytesting media f15f4c0a)

## 1. Disease information

### 1.1 Definition/overview
WHS is a chromosomal disorder caused by distal 4p deletions (usually 4p16.3), producing a multisystem developmental syndrome with characteristic facial features, growth delay, intellectual disability/developmental delay, and seizures. (nevado2020internationalmeetingon pages 3-4, zollino2008onthenosology pages 1-2)

### 1.2 Key identifiers
- **OMIM:** **#194190** (explicitly stated in WHS nosology/meeting proceedings). (nevado2020internationalmeetingon pages 2-2)
- **MONDO / MeSH / ICD-10 / ICD-11 / Orphanet ORPHAcode:** *Not retrievable from the tool-accessible full-text corpus in this run.* (see Limitations). 

### 1.3 Common synonyms / alternative names
- “**4p- syndrome**”, “**deletion 4p**”, “terminal 4p deletion” (terminology used across prenatal and clinical genetics literature). (sifakis2012prenataldiagnosisof pages 1-2, nevado2020internationalmeetingon pages 3-4)

### 1.4 Source type (individual vs aggregated)
Evidence in this report derives from:
- **Aggregated cohorts and registries** (e.g., epidemiology cohort n=159; epilepsy cohort n=140; prenatal cohort n=18). (shannon2001anepidemiologicalstudy pages 1-2, blancolago2025epilepsyinwolf–hirschhorn pages 2-4, simonini2022prenatalsonographicfindings pages 1-2)
- **Curated clinical genetics guidance** (clinical utility gene card). (battaglia2011clinicalutilitygene pages 1-2)
- **Model organism and developmental biology studies/reviews** supporting mechanistic hypotheses. (, )

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** hemizygous deletion of the distal short arm of chromosome 4 (4p16.3), with variable deletion size and complexity, producing a contiguous gene haploinsufficiency syndrome. (zollino2008onthenosology pages 1-2, nevado2020internationalmeetingon pages 3-4)

**Rearrangement classes reported** include:
- terminal deletions (most common),
- interstitial 4p deletions,
- unbalanced translocations (including recurrent 4p;8p events),
- ring chromosome 4,
- inverted duplications/complex rearrangements. (ho2016chromosomalmicroarraytesting pages 1-1, nevado2020internationalmeetingon pages 4-4, simonini2022prenatalsonographicfindings pages 5-7)

### 2.2 Risk factors
**Genetic risk factors:** Presence of a *parental balanced translocation* involving 4p can raise recurrence risk for offspring with an unbalanced rearrangement; thus parental cytogenetic testing is relevant for counseling. (simonini2022prenatalsonographicfindings pages 5-7, xing2018prenataldiagnosisof pages 5-7)

**Environmental risk factors:** Not supported in the retrieved evidence; WHS is primarily genetic due to structural chromosome abnormalities. (nevado2020internationalmeetingon pages 3-4, zollino2008onthenosology pages 1-2)

### 2.3 Protective factors
No validated genetic or environmental protective factors were identified in the retrieved literature.

### 2.4 Gene–environment interactions
No WHS-specific gene–environment interactions were identified in the retrieved literature.

## 3. Phenotypes (clinical spectrum)

### 3.1 Core phenotype (postnatal)
The consensus “core WHS phenotype” includes typical facial dysmorphism, growth delay, intellectual disability/developmental delay, and seizures (or EEG abnormalities). (nevado2020internationalmeetingon pages 3-4)

A large cohort (n=140) quantified high frequencies of major features:
- **Psychomotor developmental delay:** ~98.9% 
- **Craniofacial features:** ~97.8%
- **Hypotonia:** ~89%
- **IUGR/postnatal growth restriction:** ~94.2%
- **Cardiac defects:** ~44.5%
- **Renal/urological anomalies:** ~53%
(these are cohort-derived rates reported in the epilepsy-focused cohort paper). (blancolago2025epilepsyinwolf–hirschhorn pages 1-2)

### 3.2 Epilepsy phenotype (key quantitative data)
In the same n=140 cohort, epilepsy burden was high and early-onset:
- **Epilepsy prevalence:** **92% (126/137)** 
- **Mean seizure onset:** **9.8 months** (range **3 days–36 months**)
- **Seizure types (proportions):** generalized tonic-clonic 55.9%, absence/atypical absence 51.8%, focal 26.9%, tonic 24.3%, myoclonic 20.4%, epileptic spasms 12.4%
- **Status epilepticus:** **58.4%** 
- **Febrile-triggered seizures:** **68.6%**
- **Treatment burden:** 85.9% treated with antiseizure medications; 42.2% had used ≥3 ASMs; commonly used ASMs were **valproic acid** and **levetiracetam**
- **Genotype–phenotype:** larger deletions (>9 Mb) associated with more severe epilepsy and poorer developmental outcomes
(pediatric cohort with standardized caregiver questionnaires). (blancolago2025epilepsyinwolf–hirschhorn pages 2-4, blancolago2025epilepsyinwolf–hirschhorn pages 1-2)

**Suggested HPO terms (examples):**
- Seizures **HP:0001250**; Epileptic spasms **HP:0011097**; Status epilepticus **HP:0002133**; Febrile seizures **HP:0002373**; Developmental delay **HP:0001263**; Intellectual disability **HP:0001249**; Hypotonia **HP:0001252**; Intrauterine growth restriction **HP:0001511**; Failure to thrive **HP:0001508**; Microcephaly **HP:0000252**; Congenital heart defect **HP:0001627**; Renal anomaly **HP:0000077**.

### 3.3 Prenatal phenotype (ultrasound; frequencies)
In a retrospective prenatal cohort of **18 confirmed** WHS cases (3 tertiary centers in Germany), the most frequent ultrasound findings were:
- **Facial abnormalities:** **94.4% (17/18)**
- **Symmetric IUGR:** **83.3% (15/18)**
- **Microcephaly:** **72.2% (13/18)**
- **Cardiac anomalies:** **50.0% (9/18)**
A particularly characteristic combination was **microcephaly + hypoplastic nasal bone**; growth restriction was present in all fetuses assessed after 20 weeks. (simonini2022prenatalsonographicfindings pages 1-2, simonini2022prenatalsonographicfindings pages 5-7)

A broader prenatal review (10 new + 37 literature cases) reported **severe IUGR 97.7%** and **typical facial appearance 82.9%**, with **cardiac malformations 29.8%** and **renal hypoplasia 36.2%**. (xing2018prenataldiagnosisof pages 1-2)

**Suggested prenatal HPO terms (examples):** IUGR **HP:0001511**; Hypoplastic nasal bone **HP:0012745**; Abnormal facial shape **HP:0001999**; Micrognathia **HP:0000347**.

### 3.4 Quality of life impact
A study of **22 Spanish caregivers** evaluated psychosocial profile and caregiver quality of life (QoL) and found that the syndrome’s severe, lifelong care needs (growth issues, seizures, developmental disability) can impact parental QoL; problem-focused coping and social support were associated with improved psychological QoL. (berrocoso2020copingwithwolfhirschhorna pages 1-2)

## 4. Genetic / molecular information

### 4.1 Causal genomic lesion and critical regions
WHS is caused by deletions of 4p16.3 with broad size variation; meeting proceedings and genotype–phenotype analyses emphasize variability from <2 Mb up to ~30 Mb or more. (nevado2020internationalmeetingon pages 3-4)

Historically defined WHS “critical regions” include:
- **WHSCR:** a ~**165 kb** interval ~2 Mb from the telomere, containing **WHSC1/NSD2** and **WHSC2/NELFA**. (nevado2020internationalmeetingon pages 4-4)
- **WHSCR-2:** an adjacent **300–600 kb** interval including **LETM1** (a long-discussed seizure candidate) and part of **WHSC1/NSD2**. (ho2016chromosomalmicroarraytesting pages 1-1)

### 4.2 Genotype–phenotype correlations (deletion size)
Multiple sources define broad severity bands:
- **Mild:** deletions **≤3.5 Mb**
- **Typical/classic:** **~5–18 Mb**
- **Severe:** **~22–25 Mb or more**
(Prenatal and postnatal sources concordantly report this pattern). (zollino2008onthenosology pages 1-2, luo2023prenataldiagnosisand pages 2-3, simonini2022prenatalsonographicfindings pages 5-7)

### 4.3 Seizure susceptibility region (recent mapping)
A chromosomal microarray mapping study (n=48) identified a strong association between **interstitial deletions that exclude the distal terminal segment** and **absence of seizures**, and refined a **terminal seizure susceptibility region** to **~197 kb** beginning ~368 kb from the 4p terminus. (ho2016chromosomalmicroarraytesting pages 1-1)

Figure-based coordinates and genes in this interval (hg19/GRCh37 chr4:367,691–564,593) include **PIGG** and **ZNF721** (and ABCA11P). (ho2016chromosomalmicroarraytesting media f15f4c0a)

### 4.4 Inheritance and origin
WHS rearrangements are often **de novo**, but familial recurrence can occur via parental balanced translocations. In a UK epidemiologic cohort (n=159): **72.3% de novo deletions**, **20.1% translocations**, **7.5% other rearrangements**. (shannon2001anepidemiologicalstudy pages 1-2)

In the prenatal literature, approximate etiologic fractions are described as ~55% de novo deletions, ~40–45% unbalanced translocations, and ~5% complex rearrangements. (simonini2022prenatalsonographicfindings pages 5-7)

### 4.5 Epigenetics / modifiers
Phenotypic severity is not strictly linear with deletion size; meeting proceedings discuss that **LETM1 haploinsufficiency alone is not sufficient** for seizures, implying additional telomeric dosage-sensitive genes and/or modifier effects. (nevado2020internationalmeetingon pages 4-5)

## 5. Environmental information
No WHS-specific environmental toxins, lifestyle risk factors, or infectious triggers causing WHS were identified in retrieved evidence. WHS is primarily a structural genomic disorder. (nevado2020internationalmeetingon pages 3-4, zollino2008onthenosology pages 1-2)

## 6. Mechanism / pathophysiology

### 6.1 Causal chain (conceptual)
**Upstream trigger:** hemizygous deletion of distal 4p (4p16.3) → **haploinsufficiency** of multiple developmental genes (including NSD2/WHSC1, NELFA/WHSC2, LETM1, and telomeric genes such as PIGG/ZNF721) → disruption of transcriptional regulation, neuronal excitability balance and developmental programs → downstream neurodevelopmental impairment, growth delay, craniofacial malformations, congenital anomalies, and epilepsy (often early-onset and severe). (zollino2008onthenosology pages 1-2, ho2016chromosomalmicroarraytesting pages 1-1, nevado2020internationalmeetingon pages 4-5)

### 6.2 Seizure biology (regional genetics)
The CMA mapping work supports a model in which **deletion of a small terminal region** can be sufficient for seizure susceptibility in WHS, refining the mechanistic focus beyond LETM1 alone. (ho2016chromosomalmicroarraytesting pages 1-1, ho2016chromosomalmicroarraytesting media f15f4c0a)

### 6.3 Developmental mechanisms: neural crest hypothesis (model-organism evidence)
A Xenopus-focused primary study supports the hypothesis that WHS craniofacial and related defects may arise from perturbation of cranial neural crest biology: WHS-associated genes (**whsc1, whsc2, letm1, tacc3**) show enrichment in migratory neural crest and influence craniofacial patterning/cartilage formation and neural crest motility when depleted. ()

**Suggested GO Biological Process terms (examples):**
- cranial neural crest cell migration (GO:0002302),
- regulation of transcription, DNA-templated (GO:0006355),
- nervous system development (GO:0007399),
- synaptic signaling (GO:0099536),
- mitochondrial calcium ion homeostasis (candidate for LETM1-related mechanisms).

**Suggested CL cell-type terms (examples):**
- neural crest cell (CL:0000134),
- excitatory neuron (CL:0000127),
- inhibitory interneuron (CL:0000099).

## 7. Anatomical structures affected
Based on the multisystem phenotype described in cohorts:
- **Nervous system:** epilepsy, developmental delay (UBERON:0001016 “nervous system”; brain UBERON:0000955). (blancolago2025epilepsyinwolf–hirschhorn pages 2-4)
- **Craniofacial structures:** characteristic facial gestalt; craniofacial developmental defects (UBERON:0001136 “facial skeleton”). (berrocoso2020copingwithwolfhirschhorna pages 1-2)
- **Cardiovascular system:** congenital heart defects (~44.5% in a large cohort; 50% in prenatal series). (blancolago2025epilepsyinwolf–hirschhorn pages 1-2, simonini2022prenatalsonographicfindings pages 1-2)
- **Urinary system/kidney:** renal/urologic anomalies (~53% in large cohort; renal hypoplasia often reported prenatally). (blancolago2025epilepsyinwolf–hirschhorn pages 1-2, xing2018prenataldiagnosisof pages 1-2)

## 8. Temporal development
- **Onset:** congenital; many features are prenatal (IUGR, microcephaly, facial anomalies) and postnatal developmental delay is universal/near-universal in cohorts. (simonini2022prenatalsonographicfindings pages 1-2, blancolago2025epilepsyinwolf–hirschhorn pages 1-2)
- **Epilepsy onset:** typically within the first year; mean onset ~9.8 months. (blancolago2025epilepsyinwolf–hirschhorn pages 2-4)
- **Course:** high early-childhood morbidity and mortality; survival improves after age 2, with some individuals surviving into adulthood (documented up to mid-30s in UK cohort, and to 55 years in adult natural history series). (shannon2001anepidemiologicalstudy pages 1-2, shannon2001anepidemiologicalstudy pages 1-1)

## 9. Inheritance and population

### 9.1 Epidemiology
- Minimum UK birth incidence (1989–1998): **1 in 95,896**. (shannon2001anepidemiologicalstudy pages 1-2, shannon2001anepidemiologicalstudy pages 1-1)
- Commonly cited incidence/prevalence in clinical literature: **~1/20,000–1/50,000 births**, with **female predominance ~2:1**. (berrocoso2020copingwithwolfhirschhorna pages 1-2, nevado2025clinicianbasedfunctionalscoring pages 1-2)

### 9.2 Inheritance pattern
WHS is typically **sporadic/de novo** as a chromosomal deletion syndrome; familial recurrence risk depends on parental chromosomal rearrangements (balanced translocation carriers). (shannon2001anepidemiologicalstudy pages 1-2, simonini2022prenatalsonographicfindings pages 5-7)

## 10. Diagnostics

### 10.1 Clinical suspicion
- Prenatal: symmetric IUGR + microcephaly + hypoplastic nasal bone + facial anomalies should raise suspicion. (simonini2022prenatalsonographicfindings pages 1-2)
- Postnatal: characteristic facial gestalt + growth restriction + neurodevelopmental delay + seizures/EEG abnormalities. (nevado2020internationalmeetingon pages 3-4, berrocoso2020copingwithwolfhirschhorna pages 1-2)

### 10.2 Genetic testing strategy (real-world implementation)
- **Chromosomal microarray (CMA)** is highlighted as the **method of choice** for diagnosis, particularly to detect **small deletions (<3 Mb)** and complex rearrangements. (simonini2022prenatalsonographicfindings pages 1-2, simonini2022prenatalsonographicfindings pages 5-7)
- **Routine karyotype** detection ~**50–60%**; **FISH** sensitivity ~**95%** in prenatal review. (simonini2022prenatalsonographicfindings pages 1-2)
- **Clinical utility gene card:** appropriately designed **FISH or genomic microarray** targeting at least portions of **LETM1** and **WHSC1** should yield **>99% clinical sensitivity**; standard chromosome studies may have only ~50–60% sensitivity and can miss microdeletions. (battaglia2011clinicalutilitygene pages 1-2)

### 10.3 Differential diagnosis
A formal differential diagnosis list was not available in retrieved full texts. In practice, WHS overlaps with other chromosomal deletion syndromes presenting with growth restriction, dysmorphism, and epilepsy; confirmation requires molecular cytogenetics (CMA/FISH/karyotype). (battaglia2011clinicalutilitygene pages 1-2, nevado2020internationalmeetingon pages 3-4)

## 11. Outcomes / prognosis

### 11.1 Survival and mortality (key statistics)
In the UK epidemiologic cohort:
- **Infant mortality:** **17.4% (23/132)**
- **Two-year mortality:** **21% (28/132)**
- **Timing:** 63.9% of deaths in the first year; 77.8% within the first two years
- **Deletion size prognostic factor:** large deletions had 51.5% deaths vs 9.7% for small deletions; adjusted OR 5.7 (95% CI 1.7–19.9)
(published Oct 2001). (shannon2001anepidemiologicalstudy pages 3-4)

Among deaths with known cause (n=32):
- lower respiratory tract infection 25% (8/32),
- multiple congenital anomalies 15.6% (5/32),
- sudden unexplained death 15.6% (5/32),
- congenital heart disease 15.6% (5/32).
(published Oct 2001). (shannon2001anepidemiologicalstudy pages 4-5)

### 11.2 Prognostic factors
- **Deletion size and complexity** (large deletions, complex rearrangements). (shannon2001anepidemiologicalstudy pages 3-4)
- **Epilepsy severity and seizure pattern**, emphasized as major determinants of neurodevelopmental outcome. (nevado2020internationalmeetingon pages 3-4, blancolago2025epilepsyinwolf–hirschhorn pages 2-4)

## 12. Treatment

### 12.1 Pharmacotherapy (epilepsy)
In a large WHS cohort, commonly used antiseizure medications were **valproic acid** and **levetiracetam**, and many individuals required polytherapy; status epilepticus was frequent and likely contributes to developmental burden. (blancolago2025epilepsyinwolf–hirschhorn pages 1-2, blancolago2025epilepsyinwolf–hirschhorn pages 2-4)

**Suggested MAXO terms (examples):**
- antiseizure therapy (MAXO:0000474),
- status epilepticus management (MAXO term to map under emergency seizure management),
- chromosomal microarray analysis (diagnostic procedure term),
- genetic counseling (MAXO:0000072),
- early intervention therapy / neurodevelopmental therapy (MAXO mapping under rehabilitation).

### 12.2 Supportive / rehabilitative care
Consensus and cohort interpretations emphasize multidisciplinary management (developmental therapies, monitoring for comorbidities such as cardiac/renal problems, and family support). (berrocoso2020copingwithwolfhirschhorna pages 1-2, shannon2001anepidemiologicalstudy pages 6-6)

### 12.3 Experimental / trials
A precise ClinicalTrials.gov condition search for “Wolf-Hirschhorn syndrome” did not retrieve disease-specific interventional trials in this tool run; earlier broad “WHS” queries primarily matched unrelated acronym uses (e.g., Women’s Health Study). (nevado2020internationalmeetingon pages 11-11)

## 13. Prevention
Primary “prevention” for WHS is **reproductive/genetic**:
- **Genetic counseling** for affected families,
- **Prenatal diagnosis** using ultrasound plus confirmatory **CMA/karyotype/FISH**,
- **Parental karyotyping** to detect balanced translocations that elevate recurrence risk.
(simonini2022prenatalsonographicfindings pages 5-7, battaglia2011clinicalutilitygene pages 1-2)

## 14. Other species / natural disease
No naturally occurring veterinary analogs were identified in retrieved evidence.

## 15. Model organisms
Mechanistic studies in vertebrate models support developmental hypotheses:
- **Xenopus laevis:** WHS-associated genes are enriched in migratory neural crest cells; depletion affects craniofacial development and neural crest motility. ()
- Additional vertebrate resources were retrieved for **zebrafish** WHSC1/NSD2 homolog biology, supporting in vivo functional studies of WHS candidate genes. ()

## Recent developments (prioritizing 2023–2024 where available)
- **2024:** A familial terminal 4p16.3 microdeletion not causing classical WHS supports refinement of critical regions and highlights interpretive complexity for small telomeric CNVs. (Osundiji 2024; publication date Nov 2024; Chromosome Research). (osundiji2024afamilialchromosome pages 7-8)
- **2024:** Basic mechanistic enzymology work expanded the substrate landscape of **NSD2 (WHSC1)**, relevant to understanding pleiotropy of NSD2 haploinsufficiency in development and disease (not WHS-specific clinical study, but mechanistically relevant). (Weirich 2024; Communications Biology; Jun 2024). ()

## Key quantitative findings (quick reference)
| Topic | Key findings (with numbers) | Source (first author year) | URL/DOI |
|---|---|---|---|
| Birth incidence / prevalence and sex ratio | Minimum UK birth incidence 1 in 95,896; broader literature estimates 1 in 50,000 births and ~1 in 20,000–1 in 50,000 births; female predominance about 2:1; 2025 WHS cohort female proportion 67.9% (Blanco-Lago cohort) (shannon2001anepidemiologicalstudy pages 1-2, shannon2001anepidemiologicalstudy pages 1-1, berrocoso2020copingwithwolfhirschhorna pages 1-2, blancolago2025epilepsyinwolf–hirschhorn pages 2-4) | Shannon 2001; Berrocoso 2020; Corrêa 2018; Blanco-Lago 2025 | https://doi.org/10.1136/jmg.38.10.674; https://doi.org/10.1186/s13023-020-01476-8; https://doi.org/10.1155/2018/5436187; https://doi.org/10.3390/jcm14228044 |
| Mortality rates and leading causes of death | Among 132 live births, infant mortality 17.4% (23/132) and 2-year mortality 21% (28/132); 63.9% of deaths in first year and 77.8% within first 2 years; large deletions had 51.5% deaths vs 9.7% for small deletions (age-adjusted OR 5.7, 95% CI 1.7–19.9); leading causes among known causes: lower respiratory tract infection 25% (8/32), multiple congenital anomalies 15.6% (5/32), sudden unexplained death 15.6% (5/32), congenital heart disease 15.6% (5/32) (shannon2001anepidemiologicalstudy pages 3-4, shannon2001anepidemiologicalstudy pages 4-5, shannon2001anepidemiologicalstudy pages 5-6) | Shannon 2001 | https://doi.org/10.1136/jmg.38.10.674 |
| Epilepsy burden | Epilepsy in 92% (126/137); mean seizure onset 9.8 months (range 3 days–36 months), typically before 12 months; seizure frequencies: generalized tonic-clonic 55.9%, absence/atypical absence 51.8%, focal 26.9%, tonic 24.3%, myoclonic 20.4%, epileptic spasms 12.4%; status epilepticus 58.4%; febrile-triggered seizures 68.6%; 85.9% on ASMs, 42.2% had used ≥3 ASMs; common ASMs valproic acid and levetiracetam; larger deletions (>9 Mb) associated with more severe epilepsy/poorer outcomes (blancolago2025epilepsyinwolf–hirschhorn pages 2-4, blancolago2025epilepsyinwolf–hirschhorn pages 1-2, blancolago2025epilepsyinwolf–hirschhorn pages 9-11) | Blanco-Lago 2025 | https://doi.org/10.3390/jcm14228044 |
| Prenatal ultrasound frequencies and diagnostic recommendations | In 18 confirmed prenatal cases: facial abnormalities 94.4% (17/18), symmetric IUGR 83.3% (15/18), microcephaly 72.2% (13/18), cardiac anomalies 50.0% (9/18); growth restriction present in all fetuses examined after 20 weeks; characteristic combination: microcephaly + hypoplastic nasal bone; pooled review data: severe IUGR 97.7% and typical facial appearance 82.9%, cardiac malformations 29.8%; CMA/SNP-array strongly recommended when WHS is suspected prenatally (simonini2022prenatalsonographicfindings pages 1-2, simonini2022prenatalsonographicfindings pages 5-7, xing2018prenataldiagnosisof pages 1-2, xing2018prenataldiagnosisof pages 3-5) | Simonini 2022; Xing 2018 | https://doi.org/10.1186/s12884-022-04665-4; https://doi.org/10.1007/s00404-018-4798-1 |
| Genetic testing sensitivity guidance | Routine karyotype detects ~50–60% of cases; FISH sensitivity reported ~95%; gene card states appropriately designed FISH or genomic microarray targeting LETM1/WHSC1 region should provide >99% clinical sensitivity; CMA is current method of choice because small deletions (<3 Mb) and complex rearrangements may be missed by karyotype/FISH; parental studies recommended when translocation suspected (battaglia2011clinicalutilitygene pages 1-2, simonini2022prenatalsonographicfindings pages 1-2, simonini2022prenatalsonographicfindings pages 5-7, xing2018prenataldiagnosisof pages 5-7) | Battaglia 2011; Simonini 2022 | https://doi.org/10.1038/ejhg.2010.186; https://doi.org/10.1186/s12884-022-04665-4 |
| Seizure susceptibility region coordinates / genes | CMA study mapped terminal seizure susceptibility region to ~197 kb starting ~368 kb from 4p terminus; figure-based coordinates hg19/GRCh37 chr4:367,691–564,593; region contains PIGG, ZNF721, and pseudogene ABCA11P; lack of inclusion of distal terminal 751 kb associated with absence of seizures in several interstitial deletion cases (ho2016chromosomalmicroarraytesting pages 1-1, ho2016chromosomalmicroarraytesting media 365127d8, ho2016chromosomalmicroarraytesting media f15f4c0a) | Ho 2016 | https://doi.org/10.1136/jmedgenet-2015-103626 |


*Table: This table compiles the most implementation-relevant quantitative findings for Wolf-Hirschhorn syndrome, including epidemiology, mortality, epilepsy burden, prenatal detection, testing performance, and the mapped seizure-susceptibility region. It is designed for quick reference in clinical or knowledge-base curation workflows.*

## Visual evidence (genotype–seizure mapping)
The seizure susceptibility region on terminal 4p and the gene content of the refined ~197 kb interval are illustrated in the CMA mapping figures (Figure 2/3) from Ho et al. 2016. (ho2016chromosomalmicroarraytesting media 365127d8, ho2016chromosomalmicroarraytesting media f15f4c0a)

## Limitations of this report (tooling constraints)
- The tool-accessible corpus did **not** yield primary sources explicitly listing **MONDO ID**, **Orphanet ORPHAcode**, **MeSH descriptor ID**, or **ICD-10/ICD-11 codes** for WHS; therefore these identifiers are not asserted here.
- Several clinically important areas (formal differential diagnosis lists; standardized QoL instruments for affected individuals) were not available in retrieved texts and may require additional targeted retrieval beyond the current run.


References

1. (nevado2020internationalmeetingon pages 3-4): Julián Nevado, Karen S. Ho, Marcella Zollino, Raquel Blanco, César Cobaleda, Christelle Golzio, Isabelle Beaudry‐Bellefeuille, Sarah Berrocoso, Jacobo Limeres, Pilar Barrúz, Candela Serrano‐Martín, Concetta Cafiero, Ignacio Málaga, Giuseppe Marangi, Elena Campos‐Sánchez, Tania Moriyón‐Iglesias, Sorangui Márquez, Leah Markham, Hope Twede, Amanda Lortz, Lenora Olson, Xiaoming Sheng, Cindy Weng, Edward Robert Wassman, Tara Newcomb, Edward Robert Wassman, John C. Carey, Agatino Battaglia, Eduardo López‐Granados, Damien Douglas, and Pablo Lapunzina. International meeting on wolf‐hirschhorn syndrome: update on the nosology and new insights on the pathogenic mechanisms for seizures and growth delay. American Journal of Medical Genetics Part A, 182:257-267, Nov 2020. URL: https://doi.org/10.1002/ajmg.a.61406, doi:10.1002/ajmg.a.61406. This article has 31 citations.

2. (zollino2008onthenosology pages 1-2): Marcella Zollino, Marina Murdolo, Giuseppe Marangi, Vanna Pecile, Cinzia Galasso, Laura Mazzanti, and Giovanni Neri. On the nosology and pathogenesis of wolf–hirschhorn syndrome: genotype–phenotype correlation analysis of 80 patients and literature review. American Journal of Medical Genetics Part C: Seminars in Medical Genetics, 148C:257-269, Nov 2008. URL: https://doi.org/10.1002/ajmg.c.30190, doi:10.1002/ajmg.c.30190. This article has 216 citations.

3. (berrocoso2020copingwithwolfhirschhorna pages 1-2): Sarah Berrocoso, Imanol Amayra, Esther Lázaro, Oscar Martínez, Juan Francisco López-Paz, Maitane García, Manuel Pérez, Mohammad Al-Rashaida, Alicia Aurora Rodríguez, Paula Maria Luna, Paula Pérez-Núñez, Raquel Blanco, and Julián Nevado. Coping with wolf-hirschhorn syndrome: quality of life and psychosocial features of family carers. Orphanet Journal of Rare Diseases, Oct 2020. URL: https://doi.org/10.1186/s13023-020-01476-8, doi:10.1186/s13023-020-01476-8. This article has 29 citations and is from a peer-reviewed journal.

4. (blancolago2025epilepsyinwolf–hirschhorn pages 2-4): Raquel Blanco-Lago, Ignacio Málaga, Jair Antonio Tenorio-Castaño, Nelly Álvarez-Álvarez, Pablo Lapunzina, and Julián Nevado. Epilepsy in wolf–hirschhorn syndrome: clinical insights from a pediatric cohort and a review of the literature. Journal of Clinical Medicine, 14:8044, Nov 2025. URL: https://doi.org/10.3390/jcm14228044, doi:10.3390/jcm14228044. This article has 0 citations.

5. (blancolago2025epilepsyinwolf–hirschhorn pages 1-2): Raquel Blanco-Lago, Ignacio Málaga, Jair Antonio Tenorio-Castaño, Nelly Álvarez-Álvarez, Pablo Lapunzina, and Julián Nevado. Epilepsy in wolf–hirschhorn syndrome: clinical insights from a pediatric cohort and a review of the literature. Journal of Clinical Medicine, 14:8044, Nov 2025. URL: https://doi.org/10.3390/jcm14228044, doi:10.3390/jcm14228044. This article has 0 citations.

6. (ho2016chromosomalmicroarraytesting pages 1-1): Karen S Ho, Sarah T South, Amanda Lortz, Charles H Hensel, Mallory R Sdano, Rena J Vanzo, Megan M Martin, Andreas Peiffer, Christophe G Lambert, Amy Calhoun, John C Carey, and Agatino Battaglia. Chromosomal microarray testing identifies a 4p terminal region associated with seizures in wolf–hirschhorn syndrome. Journal of Medical Genetics, 53:256-263, Jan 2016. URL: https://doi.org/10.1136/jmedgenet-2015-103626, doi:10.1136/jmedgenet-2015-103626. This article has 59 citations and is from a domain leading peer-reviewed journal.

7. (ho2016chromosomalmicroarraytesting media f15f4c0a): Karen S Ho, Sarah T South, Amanda Lortz, Charles H Hensel, Mallory R Sdano, Rena J Vanzo, Megan M Martin, Andreas Peiffer, Christophe G Lambert, Amy Calhoun, John C Carey, and Agatino Battaglia. Chromosomal microarray testing identifies a 4p terminal region associated with seizures in wolf–hirschhorn syndrome. Journal of Medical Genetics, 53:256-263, Jan 2016. URL: https://doi.org/10.1136/jmedgenet-2015-103626, doi:10.1136/jmedgenet-2015-103626. This article has 59 citations and is from a domain leading peer-reviewed journal.

8. (nevado2020internationalmeetingon pages 2-2): Julián Nevado, Karen S. Ho, Marcella Zollino, Raquel Blanco, César Cobaleda, Christelle Golzio, Isabelle Beaudry‐Bellefeuille, Sarah Berrocoso, Jacobo Limeres, Pilar Barrúz, Candela Serrano‐Martín, Concetta Cafiero, Ignacio Málaga, Giuseppe Marangi, Elena Campos‐Sánchez, Tania Moriyón‐Iglesias, Sorangui Márquez, Leah Markham, Hope Twede, Amanda Lortz, Lenora Olson, Xiaoming Sheng, Cindy Weng, Edward Robert Wassman, Tara Newcomb, Edward Robert Wassman, John C. Carey, Agatino Battaglia, Eduardo López‐Granados, Damien Douglas, and Pablo Lapunzina. International meeting on wolf‐hirschhorn syndrome: update on the nosology and new insights on the pathogenic mechanisms for seizures and growth delay. American Journal of Medical Genetics Part A, 182:257-267, Nov 2020. URL: https://doi.org/10.1002/ajmg.a.61406, doi:10.1002/ajmg.a.61406. This article has 31 citations.

9. (sifakis2012prenataldiagnosisof pages 1-2): Stavros Sifakis, Emmanouil Manolakos, Annalisa Vetro, Dimitra Kappou, Panagiotis Peitsidis, Maria Kontodiou, Antonios Garas, Nikolaos Vrachnis, Anastasia Konstandinidou, Orsetta Zuffardi, Sandro Orru, and Ioannis Papoulidis. Prenatal diagnosis of wolf-hirschhorn syndrome confirmed by comparative genomic hybridization array: report of two cases and review of the literature. Molecular Cytogenetics, 5:12-12, Feb 2012. URL: https://doi.org/10.1186/1755-8166-5-12, doi:10.1186/1755-8166-5-12. This article has 35 citations and is from a peer-reviewed journal.

10. (shannon2001anepidemiologicalstudy pages 1-2): N. Shannon, E. Maltby, A. Rigby, and O. Quarrell. An epidemiological study of wolf-hirschhorn syndrome: life expectancy and cause of mortality. Journal of Medical Genetics, 38:674-679, Oct 2001. URL: https://doi.org/10.1136/jmg.38.10.674, doi:10.1136/jmg.38.10.674. This article has 138 citations and is from a domain leading peer-reviewed journal.

11. (simonini2022prenatalsonographicfindings pages 1-2): Corinna Simonini, Markus Hoopmann, Karl Oliver Kagan, Torsten Schröder, Ulrich Gembruch, and Annegret Geipel. Prenatal sonographic findings in confirmed cases of wolf-hirschhorn syndrome. BMC Pregnancy and Childbirth, Apr 2022. URL: https://doi.org/10.1186/s12884-022-04665-4, doi:10.1186/s12884-022-04665-4. This article has 13 citations and is from a peer-reviewed journal.

12. (battaglia2011clinicalutilitygene pages 1-2): Agatino Battaglia, Sarah South, and John C Carey. Clinical utility gene card for: wolf–hirschhorn (4p-) syndrome. European Journal of Human Genetics, 19:-, Apr 2011. URL: https://doi.org/10.1038/ejhg.2010.186, doi:10.1038/ejhg.2010.186. This article has 23 citations and is from a domain leading peer-reviewed journal.

13. (nevado2020internationalmeetingon pages 4-4): Julián Nevado, Karen S. Ho, Marcella Zollino, Raquel Blanco, César Cobaleda, Christelle Golzio, Isabelle Beaudry‐Bellefeuille, Sarah Berrocoso, Jacobo Limeres, Pilar Barrúz, Candela Serrano‐Martín, Concetta Cafiero, Ignacio Málaga, Giuseppe Marangi, Elena Campos‐Sánchez, Tania Moriyón‐Iglesias, Sorangui Márquez, Leah Markham, Hope Twede, Amanda Lortz, Lenora Olson, Xiaoming Sheng, Cindy Weng, Edward Robert Wassman, Tara Newcomb, Edward Robert Wassman, John C. Carey, Agatino Battaglia, Eduardo López‐Granados, Damien Douglas, and Pablo Lapunzina. International meeting on wolf‐hirschhorn syndrome: update on the nosology and new insights on the pathogenic mechanisms for seizures and growth delay. American Journal of Medical Genetics Part A, 182:257-267, Nov 2020. URL: https://doi.org/10.1002/ajmg.a.61406, doi:10.1002/ajmg.a.61406. This article has 31 citations.

14. (simonini2022prenatalsonographicfindings pages 5-7): Corinna Simonini, Markus Hoopmann, Karl Oliver Kagan, Torsten Schröder, Ulrich Gembruch, and Annegret Geipel. Prenatal sonographic findings in confirmed cases of wolf-hirschhorn syndrome. BMC Pregnancy and Childbirth, Apr 2022. URL: https://doi.org/10.1186/s12884-022-04665-4, doi:10.1186/s12884-022-04665-4. This article has 13 citations and is from a peer-reviewed journal.

15. (xing2018prenataldiagnosisof pages 5-7): Ya Xing, Jimmy Lloyd Holder, Yong Liu, Meizhen Yuan, Qi Sun, Xiaoxing Qu, Linbei Deng, Jia Zhou, Yingjun Yang, Ming Guo, Sau-Wai Cheung, and Luming Sun. Prenatal diagnosis of wolf–hirschhorn syndrome: from ultrasound findings, diagnostic technology to genetic counseling. Archives of Gynecology and Obstetrics, 298:289-295, May 2018. URL: https://doi.org/10.1007/s00404-018-4798-1, doi:10.1007/s00404-018-4798-1. This article has 36 citations and is from a peer-reviewed journal.

16. (xing2018prenataldiagnosisof pages 1-2): Ya Xing, Jimmy Lloyd Holder, Yong Liu, Meizhen Yuan, Qi Sun, Xiaoxing Qu, Linbei Deng, Jia Zhou, Yingjun Yang, Ming Guo, Sau-Wai Cheung, and Luming Sun. Prenatal diagnosis of wolf–hirschhorn syndrome: from ultrasound findings, diagnostic technology to genetic counseling. Archives of Gynecology and Obstetrics, 298:289-295, May 2018. URL: https://doi.org/10.1007/s00404-018-4798-1, doi:10.1007/s00404-018-4798-1. This article has 36 citations and is from a peer-reviewed journal.

17. (luo2023prenataldiagnosisand pages 2-3): H Luo, R Chang, F Liu, and X Gao. Prenatal diagnosis and molecular cytogenetic analyses of a de novo deletion on chromosome 4p16. 3p15. 33. Unknown journal, 2023.

18. (nevado2020internationalmeetingon pages 4-5): Julián Nevado, Karen S. Ho, Marcella Zollino, Raquel Blanco, César Cobaleda, Christelle Golzio, Isabelle Beaudry‐Bellefeuille, Sarah Berrocoso, Jacobo Limeres, Pilar Barrúz, Candela Serrano‐Martín, Concetta Cafiero, Ignacio Málaga, Giuseppe Marangi, Elena Campos‐Sánchez, Tania Moriyón‐Iglesias, Sorangui Márquez, Leah Markham, Hope Twede, Amanda Lortz, Lenora Olson, Xiaoming Sheng, Cindy Weng, Edward Robert Wassman, Tara Newcomb, Edward Robert Wassman, John C. Carey, Agatino Battaglia, Eduardo López‐Granados, Damien Douglas, and Pablo Lapunzina. International meeting on wolf‐hirschhorn syndrome: update on the nosology and new insights on the pathogenic mechanisms for seizures and growth delay. American Journal of Medical Genetics Part A, 182:257-267, Nov 2020. URL: https://doi.org/10.1002/ajmg.a.61406, doi:10.1002/ajmg.a.61406. This article has 31 citations.

19. (shannon2001anepidemiologicalstudy pages 1-1): N. Shannon, E. Maltby, A. Rigby, and O. Quarrell. An epidemiological study of wolf-hirschhorn syndrome: life expectancy and cause of mortality. Journal of Medical Genetics, 38:674-679, Oct 2001. URL: https://doi.org/10.1136/jmg.38.10.674, doi:10.1136/jmg.38.10.674. This article has 138 citations and is from a domain leading peer-reviewed journal.

20. (nevado2025clinicianbasedfunctionalscoring pages 1-2): Julián Nevado, Raquel Blanco-Lago, Cristina Bel-Fenellós, Adolfo Hernández, María A. Mori-Álvarez, Chantal Biencinto-López, Ignacio Málaga, Harry Pachajoa, Elena Mansilla, Fe A. García-Santiago, Pilar Barrúz, Jair A. Tenorio-Castaño, Yolanda Muñoz-GªPorrero, Isabel Vallcorba, and Pablo Lapunzina. Clinician-based functional scoring and genomic insights for prognostic stratification in wolf–hirschhorn syndrome. Genes, 16:820, Jul 2025. URL: https://doi.org/10.3390/genes16070820, doi:10.3390/genes16070820. This article has 1 citations.

21. (shannon2001anepidemiologicalstudy pages 3-4): N. Shannon, E. Maltby, A. Rigby, and O. Quarrell. An epidemiological study of wolf-hirschhorn syndrome: life expectancy and cause of mortality. Journal of Medical Genetics, 38:674-679, Oct 2001. URL: https://doi.org/10.1136/jmg.38.10.674, doi:10.1136/jmg.38.10.674. This article has 138 citations and is from a domain leading peer-reviewed journal.

22. (shannon2001anepidemiologicalstudy pages 4-5): N. Shannon, E. Maltby, A. Rigby, and O. Quarrell. An epidemiological study of wolf-hirschhorn syndrome: life expectancy and cause of mortality. Journal of Medical Genetics, 38:674-679, Oct 2001. URL: https://doi.org/10.1136/jmg.38.10.674, doi:10.1136/jmg.38.10.674. This article has 138 citations and is from a domain leading peer-reviewed journal.

23. (shannon2001anepidemiologicalstudy pages 6-6): N. Shannon, E. Maltby, A. Rigby, and O. Quarrell. An epidemiological study of wolf-hirschhorn syndrome: life expectancy and cause of mortality. Journal of Medical Genetics, 38:674-679, Oct 2001. URL: https://doi.org/10.1136/jmg.38.10.674, doi:10.1136/jmg.38.10.674. This article has 138 citations and is from a domain leading peer-reviewed journal.

24. (nevado2020internationalmeetingon pages 11-11): Julián Nevado, Karen S. Ho, Marcella Zollino, Raquel Blanco, César Cobaleda, Christelle Golzio, Isabelle Beaudry‐Bellefeuille, Sarah Berrocoso, Jacobo Limeres, Pilar Barrúz, Candela Serrano‐Martín, Concetta Cafiero, Ignacio Málaga, Giuseppe Marangi, Elena Campos‐Sánchez, Tania Moriyón‐Iglesias, Sorangui Márquez, Leah Markham, Hope Twede, Amanda Lortz, Lenora Olson, Xiaoming Sheng, Cindy Weng, Edward Robert Wassman, Tara Newcomb, Edward Robert Wassman, John C. Carey, Agatino Battaglia, Eduardo López‐Granados, Damien Douglas, and Pablo Lapunzina. International meeting on wolf‐hirschhorn syndrome: update on the nosology and new insights on the pathogenic mechanisms for seizures and growth delay. American Journal of Medical Genetics Part A, 182:257-267, Nov 2020. URL: https://doi.org/10.1002/ajmg.a.61406, doi:10.1002/ajmg.a.61406. This article has 31 citations.

25. (osundiji2024afamilialchromosome pages 7-8): Mayowa Azeez Osundiji, Eva Kahn, and Brendan Lanpher. A familial chromosome 4p16.3 terminal microdeletion that does not cause wolf-hirschhorn (4p-) syndrome. Chromosome research : an international journal on the molecular, supramolecular and evolutionary aspects of chromosome biology, 32 4:13, Nov 2024. URL: https://doi.org/10.1007/s10577-024-09757-9, doi:10.1007/s10577-024-09757-9. This article has 0 citations.

26. (shannon2001anepidemiologicalstudy pages 5-6): N. Shannon, E. Maltby, A. Rigby, and O. Quarrell. An epidemiological study of wolf-hirschhorn syndrome: life expectancy and cause of mortality. Journal of Medical Genetics, 38:674-679, Oct 2001. URL: https://doi.org/10.1136/jmg.38.10.674, doi:10.1136/jmg.38.10.674. This article has 138 citations and is from a domain leading peer-reviewed journal.

27. (blancolago2025epilepsyinwolf–hirschhorn pages 9-11): Raquel Blanco-Lago, Ignacio Málaga, Jair Antonio Tenorio-Castaño, Nelly Álvarez-Álvarez, Pablo Lapunzina, and Julián Nevado. Epilepsy in wolf–hirschhorn syndrome: clinical insights from a pediatric cohort and a review of the literature. Journal of Clinical Medicine, 14:8044, Nov 2025. URL: https://doi.org/10.3390/jcm14228044, doi:10.3390/jcm14228044. This article has 0 citations.

28. (xing2018prenataldiagnosisof pages 3-5): Ya Xing, Jimmy Lloyd Holder, Yong Liu, Meizhen Yuan, Qi Sun, Xiaoxing Qu, Linbei Deng, Jia Zhou, Yingjun Yang, Ming Guo, Sau-Wai Cheung, and Luming Sun. Prenatal diagnosis of wolf–hirschhorn syndrome: from ultrasound findings, diagnostic technology to genetic counseling. Archives of Gynecology and Obstetrics, 298:289-295, May 2018. URL: https://doi.org/10.1007/s00404-018-4798-1, doi:10.1007/s00404-018-4798-1. This article has 36 citations and is from a peer-reviewed journal.

29. (ho2016chromosomalmicroarraytesting media 365127d8): Karen S Ho, Sarah T South, Amanda Lortz, Charles H Hensel, Mallory R Sdano, Rena J Vanzo, Megan M Martin, Andreas Peiffer, Christophe G Lambert, Amy Calhoun, John C Carey, and Agatino Battaglia. Chromosomal microarray testing identifies a 4p terminal region associated with seizures in wolf–hirschhorn syndrome. Journal of Medical Genetics, 53:256-263, Jan 2016. URL: https://doi.org/10.1136/jmedgenet-2015-103626, doi:10.1136/jmedgenet-2015-103626. This article has 59 citations and is from a domain leading peer-reviewed journal.