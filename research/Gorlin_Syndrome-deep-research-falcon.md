---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T19:57:00.823994'
end_time: '2026-05-08T20:11:39.859165'
duration_seconds: 879.04
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Gorlin Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 24
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Gorlin Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Gorlin Syndrome** covering all of the
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
- **Disease Name:** Gorlin Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Gorlin Syndrome** covering all of the
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


# Gorlin Syndrome (Nevoid Basal Cell Carcinoma Syndrome; NBCCS) — Disease Characteristics Research Report

## Target Disease
- **Disease name:** Gorlin syndrome
- **Category:** Mendelian (autosomal dominant tumor predisposition)
- **MONDO ID:** Not available in the retrieved source set (explicit MONDO identifier not found).

## Evidence base and scope
This report synthesizes the retrieved 2023–2024 primary/review literature and ClinicalTrials.gov records. Several authoritative guideline-level recommendations come from an AACR Cancer Predisposition Working Group publication in *Clinical Cancer Research* (Apr 2024) and real-world safety data from the NISSO post-authorization study in *BMC Cancer* (Nov 2024). Where specific controlled vocabulary identifiers (e.g., ICD-10/11, Orphanet, MONDO) or PMIDs were not present in the retrieved texts, this is explicitly noted.

## Structured summary table
The following table is optimized for disease knowledge-base ingestion.

| Category | Key facts | Best supporting citations |
|---|---|---|
| Identifiers/Synonyms | Gorlin syndrome is also called nevoid basal cell carcinoma syndrome (NBCCS), Gorlin-Goltz syndrome, basal cell nevus syndrome (BCNS), multiple basal cell carcinoma syndrome, jaw cyst-basal cell tumor-skeletal anomaly syndrome, and fifth phacomatosis. OMIM disease identifier reported as **#109400**; MeSH term in a Gorlin trial record is **Basal Cell Nevus Syndrome (D001478)**. | (kammoun2024theoralfacialmanifestations pages 17-25, murgia2024gorlinsyndromeassociatedbasal pages 1-2, NCT03703310 chunk 3) |
| Genetics | Rare **autosomal dominant** tumor-predisposition syndrome caused primarily by **loss-of-function PTCH1** variants; **SUFU** and occasionally **PTCH2** are also implicated. About **70–80%** of cases have a family history and **20–30%** are **de novo**. PTCH1 variants account for most cases; one review excerpt states PTCH1 variants are responsible for ~90% of cases and another that germline PTCH1 mutation is present in up to 85% of NBCCS patients. | (murgia2024gorlinsyndromeassociatedbasal pages 1-2, wescott2023sustainedsuppressionof pages 1-2, onodera2023hedgehogrelatedmutationcauses pages 2-4, kammoun2024theoralfacialmanifestations pages 30-34, wescott2023sustainedsuppressionof pages 2-4) |
| Core clinical features | Common manifestations include **multiple basal cell carcinomas (BCCs)**, **odontogenic keratocysts (OKCs)**, **palmar/plantar pits**, **falx cerebri calcification**, macrocephaly, rib/vertebral anomalies, and craniofacial dysmorphism. Frequency estimates reported in a 2023 review excerpt: **BCC** prevalence varies by ancestry (**15.2% Koreans; 38% African Americans; 80% Caucasians; 76% Australians**) with mean onset ~**20.3 years**; **OKC 75%** (mean onset **15.5 years**); **palmar/plantar pits 87%**. | (onodera2023hedgehogrelatedmutationcauses pages 2-4, kammoun2024theoralfacialmanifestations pages 17-25, murgia2024gorlinsyndromeassociatedbasal pages 1-2) |
| Tumor risks | Tumor spectrum includes **BCC**, **medulloblastoma**, **ovarian fibroma**, and **cardiac fibroma/fibroelastoma**. Medulloblastoma occurs in up to **5%** overall in one review excerpt, with much higher risk in **SUFU** carriers than **PTCH1** carriers; the 2024 AACR surveillance paper gives absolute SHH-medulloblastoma risks of about **7–9.2% for SUFU** and **0.37–1.1% for PTCH1**. **Ovarian fibromas** occur in **15–25%** of patients and are often bilateral (~**75%** bilateral). | (onodera2023hedgehogrelatedmutationcauses pages 2-4, hansford2024updateoncancer pages 3-4, zhu2023bilateralovarianfibromas pages 1-4, murgia2024gorlinsyndromeassociatedbasal pages 1-2) |
| Diagnostic criteria | Clinical diagnosis is typically based on **major/minor criteria**. Major criteria summarized across 2023–2024 sources include: **multiple BCCs (>5) or BCC at young age**, **jaw/odontogenic keratocysts**, **palmar/plantar pits**, **lamellar falx calcification**, **medulloblastoma**, and/or an **affected first-degree relative**. One 2024 study states diagnosis can be made with **two major + one minor** or **one major + three minor** criteria; molecular confirmation with heterozygous germline **PTCH1** or **SUFU** pathogenic variants can establish the diagnosis when clinical findings are inconclusive. | (murgia2024gorlinsyndromeassociatedbasal pages 1-2, wescott2023sustainedsuppressionof pages 1-2, wescott2023sustainedsuppressionof pages 2-4, kammoun2024theoralfacialmanifestations pages 17-25) |
| Surveillance | 2024 AACR childhood brain tumor predisposition guidance recommends **gene-specific surveillance**. For **SUFU** carriers: neurologic exam/head circumference in infancy and diagnosis with checks every **3–4 months until age 5**; **brain MRI every 3–4 months until age 3, then every 6 months until age 5**. For **PTCH1** carriers: routine MRI is generally **not** recommended; surveillance emphasizes clinical neurologic vigilance. Additional screening includes dermatologic exams with sun protection counseling, **echocardiogram in infancy** for cardiac fibroma, and **ovarian ultrasound** (PTCH1 once at age 18; SUFU every 3 years in the cited table). PTCH1-focused dental surveillance includes **annual orthopantomogram/MRI**. | (hansford2024updateoncancer pages 3-4, hansford2024updateoncancer pages 2-3, hansford2024updateoncancer media cb459877, kammoun2024theoralfacialmanifestations pages 30-34) |
| Treatments | Standard care includes repeated surgery for BCCs/OKCs and multidisciplinary surveillance; for high BCC burden, **hedgehog pathway inhibitors** (**vismodegib**, **sonidegib**) are used. In a 10-patient 2023 Gorlin case series, **all patients achieved complete remission**, and new BCCs fell from mean **28.3 before treatment to 1.4 during treatment**; median time to a new BCC was **47.3 months**. A 2024 retrospective Gorlin cohort found sustained HHI treatment suppressed both new and existing BCCs, with **sonidegib** appearing more effective and better tolerated than vismodegib; schedule adjustment improved tolerability without obvious loss of efficacy. | (wescott2023sustainedsuppressionof pages 1-2, murgia2024gorlinsyndromeassociatedbasal pages 1-2, wescott2023sustainedsuppressionof pages 2-4) |
| Clinical trials | Key Gorlin-specific interventional studies include **NCT06050122** (Phase 3, topical **patidegib gel 2%** vs vehicle; active, not recruiting; primary endpoint: number of new facial BCCs at Month 12), **NCT03703310** (Phase 3, patidegib topical gel 2%; completed), **NCT02762084** (Phase 2, topical patidegib 2%/4% vs vehicle; completed), **NCT01350115** (Phase 2, **oral sonidegib/LDE225**; completed), and **NCT00961896** (Phase 2, **topical LDE225**; completed). | (NCT06050122 chunk 1, NCT02762084 chunk 1, NCT01350115 chunk 1, NCT00961896 chunk 1) |
| Epidemiology | Prevalence estimates cluster around **1:57,000**, with published ranges of roughly **1:30,827 to 1:164,000**; another review gives a broader estimate of **1 in 50,000 to 256,000**. Reported sex distribution is similar in males and females, consistent with autosomal dominant inheritance. | (murgia2024gorlinsyndromeassociatedbasal pages 1-2, wescott2023sustainedsuppressionof pages 1-2, kammoun2024theoralfacialmanifestations pages 17-25, zhu2023bilateralovarianfibromas pages 1-4) |
| Treatment safety / real-world implementation | In the multinational **NISSO** real-world sonidegib safety study (**321** laBCC patients; **12.2%** with Gorlin syndrome), median exposure was **8.8 months**. **88.5%** had ≥1 TEAE; common TEAEs were **muscle spasms 43.9%**, **dysgeusia 37.1%**, and **alopecia 30.2%**. TEAEs led to **discontinuation in 18.4%**, **dose reduction in 22.7%**, and **interruption in 30.5%**; serious drug-related TEAEs occurred in **4.1%**. | (gutzmer2024interimanalysisof pages 1-2, gutzmer2024interimanalysisof pages 2-4) |


*Table: This table summarizes high-value knowledge-base facts for Gorlin syndrome, including identifiers, genetics, phenotypes, risks, surveillance, treatments, trials, and epidemiology. It emphasizes quantitative findings and recent evidence useful for structured disease annotation.*

---

## 1. Disease Information

### 1.1 Overview (definition; current understanding)
Gorlin syndrome—also called **nevoid basal cell carcinoma syndrome (NBCCS)**—is a **rare autosomal dominant** multisystem disorder characterized by developmental anomalies and a strong predisposition to tumors, especially **multiple basal cell carcinomas (BCCs)** and **odontogenic keratocysts (OKCs)**, with additional risks for **medulloblastoma**, **ovarian fibroma**, and **cardiac fibroma**. (murgia2024gorlinsyndromeassociatedbasal pages 1-2, onodera2023hedgehogrelatedmutationcauses pages 2-4, zhu2023bilateralovarianfibromas pages 1-4)

**Recent expert framing (2024):** A 2024 retrospective cohort paper defines NBCCS/GS as “a genetic disorder characterized by the development of multiple cutaneous BCCs due to mutations in the hedgehog signaling pathway.” (*Cancers*, published online 2024-06-07; DOI URL below). (murgia2024gorlinsyndromeassociatedbasal pages 1-2)

### 1.2 Key identifiers
- **OMIM (disease):** **#109400** (explicitly listed). (kammoun2024theoralfacialmanifestations pages 17-25)
- **MeSH (disease term used in ClinicalTrials.gov):** “Basal Cell Nevus Syndrome” **D001478** (ClinicalTrials.gov record metadata). (NCT03703310 chunk 3)
- **Other identifiers (Orphanet, ICD-10/ICD-11, MONDO):** Not present in the retrieved evidence snippets; therefore not reported here.

### 1.3 Synonyms and alternative names
Common synonyms include:
- Nevoid basal cell carcinoma syndrome (NBCCS)
- Basal cell nevus syndrome (BCNS)
- Gorlin–Goltz syndrome
- Multiple basal cell carcinoma syndrome
- Jaw cyst–basal cell tumor–skeletal anomaly syndrome
- Fifth phacomatosis (kammoun2024theoralfacialmanifestations pages 17-25, murgia2024gorlinsyndromeassociatedbasal pages 1-2)

### 1.4 Source type
Information summarized here is drawn from **aggregated disease-level resources** (reviews/guidelines) and **clinical cohorts/case series** (including real-world observational safety data) rather than EHR-derived phenotyping. (hansford2024updateoncancer pages 3-4, gutzmer2024interimanalysisof pages 2-4, wescott2023sustainedsuppressionof pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause:** germline pathogenic variants in **Hedgehog (Hh) pathway** negative regulators—most commonly **PTCH1**, and less commonly **SUFU** and **PTCH2**—leading to pathway hyperactivation with developmental anomalies and tumor predisposition. (onodera2023hedgehogrelatedmutationcauses pages 2-4, murgia2024gorlinsyndromeassociatedbasal pages 1-2)

**Inheritance:** autosomal dominant; a large fraction arises de novo (20–30% in multiple reports). (murgia2024gorlinsyndromeassociatedbasal pages 1-2, wescott2023sustainedsuppressionof pages 1-2)

### 2.2 Risk factors

#### Genetic risk factors
- **PTCH1 loss-of-function** is the dominant genetic driver in most cases (one 2024 cohort states PTCH1 LoF as primary cause; a 2023 review describes PTCH1 as the most common causal gene and notes PTCH2/SUFU involvement). (murgia2024gorlinsyndromeassociatedbasal pages 1-2, onodera2023hedgehogrelatedmutationcauses pages 2-4)
- **Gene-specific medulloblastoma risk differs strongly:** SUFU carriers have substantially higher absolute SHH-medulloblastoma risks than PTCH1 carriers (see §9 and §11 for surveillance implications). (hansford2024updateoncancer pages 3-4)

#### Environmental/medical exposure risk factors
- **Ionizing radiation should be avoided** when feasible due to tumor induction concerns in NBCCS; this is emphasized in pediatric surveillance guidance (sun protection counseling and avoidance of ionizing radiation are explicitly noted). (hansford2024updateoncancer pages 2-3)

### 2.3 Protective factors / gene–environment interactions
No explicit protective genetic variants or quantified gene–environment interaction models were found in the retrieved evidence set. Risk mitigation is primarily via exposure avoidance (radiation, UV) and surveillance. (hansford2024updateoncancer pages 2-3)

---

## 3. Phenotypes (clinical features)

### 3.1 High-frequency phenotypes and reported frequencies
A 2023 review focusing on Hedgehog-related skeletal/tumor disorders provides quantitative phenotype frequencies for Gorlin syndrome:
- **Palmar/plantar pits:** ~**87%** (onodera2023hedgehogrelatedmutationcauses pages 2-4)
- **Odontogenic keratocysts (OKC):** ~**75%**, mean onset ~**15.5 years** (onodera2023hedgehogrelatedmutationcauses pages 2-4)
- **Basal cell carcinoma (BCC):** frequency varies by ancestry (reported values: **15.2% Koreans; 38% African Americans; 80% Caucasians; 76% Australians**) with mean onset ~**20.3 years** (onodera2023hedgehogrelatedmutationcauses pages 2-4)
- **Medulloblastoma:** “up to **5%** in the first 2 years of life” in the cited review summary (onodera2023hedgehogrelatedmutationcauses pages 2-4)

Other commonly described manifestations across 2023–2024 clinical series/reviews include macrocephaly, craniofacial dysmorphism, rib/vertebral anomalies, falx cerebri calcification, and multiple BCCs (often dozens to hundreds over a lifetime). (wescott2023sustainedsuppressionof pages 1-2, kammoun2024theoralfacialmanifestations pages 17-25, murgia2024gorlinsyndromeassociatedbasal pages 1-2)

### 3.2 Example phenotype-to-HPO suggestions (non-exhaustive)
The retrieved texts did not include formal HPO mappings; below are suggested HPO-aligned phenotype labels for knowledge-base normalization (term IDs should be resolved against the HPO release used in your KB pipeline):
- Multiple basal cell carcinomas → *Basal cell carcinoma*
- Odontogenic keratocysts → *Odontogenic keratocyst*
- Palmar/plantar pits → *Palmar pits*, *Plantar pits*
- Macrocephaly → *Macrocephaly*
- Falx cerebri calcification → *Intracranial calcification* / *Falx cerebri calcification*
- Rib anomalies (e.g., bifid ribs) → *Bifid rib* / *Rib anomaly*
- Medulloblastoma (SHH-activated) → *Medulloblastoma*
- Ovarian fibroma → *Ovarian fibroma*
- Cardiac fibroma → *Cardiac fibroma*

### 3.3 Quality of life impact
High BCC burden can lead to repeated procedures and disfigurement; a 2024 cohort describes that patients “may need dozens or even hundreds of surgical procedures in their lifetime,” which can be severely scarring/disfiguring, motivating systemic pathway-targeted therapies. (murgia2024gorlinsyndromeassociatedbasal pages 1-2)

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes
- **PTCH1** (primary; tumor suppressor; Hh receptor) (onodera2023hedgehogrelatedmutationcauses pages 2-4, murgia2024gorlinsyndromeassociatedbasal pages 1-2)
- **SUFU** (negative regulator of GLI; high SHH-medulloblastoma risk subgroup) (hansford2024updateoncancer pages 3-4)
- **PTCH2** (less common; occasionally implicated) (onodera2023hedgehogrelatedmutationcauses pages 2-4, wescott2023sustainedsuppressionof pages 2-4)

### 4.2 Pathogenic variant types and functional consequences
**Mechanistic class:** typically **loss-of-function** of pathway repressors → constitutive pathway signaling. In PTCH1-associated disease, PTCH1 normally represses SMO; loss leads to downstream GLI activation. (onodera2023hedgehogrelatedmutationcauses pages 2-4)

**Hard-to-detect variant class (2024 development):** Mochizuki et al. describe a **germline mobile-element insertion** in PTCH1 (Alu insertion) that standard panel and genome sequencing did not initially detect, requiring manual review and RNA-seq confirmation:
- Variant: **PTCH1 c.361_362insAlu** (molecular confirmation via clinical RNA sequencing) (mochizuki2024germlineptch1c.361362insalu pages 1-2, mochizuki2024germlineptch1c.361362insalu pages 3-4)
- Clinical implication: supports integrating RNA-seq with DNA testing for cryptic splicing/insertion events when phenotype is strong. (mochizuki2024germlineptch1c.361362insalu pages 2-3)

**Direct abstract quote (diagnostic genomics; 2024):** “Clinical RNA sequencing further demonstrated an Alu insertion at this region (PTCH1: c.361_362insAlu), providing molecular confirmation of Gorlin syndrome.” (Mochizuki et al., *Am J Med Genet A*, Jun 2024; https://doi.org/10.1002/ajmg.a.63788). (mochizuki2024germlineptch1c.361362insalu pages 1-2)

### 4.3 Modifier genes / epigenetics / chromosomal abnormalities
The retrieved evidence mentions SUFU/PTCH2 as contributors/modifiers of expressivity but does not provide specific validated modifier loci, epigenetic signatures, or recurrent chromosomal abnormalities. (murgia2024gorlinsyndromeassociatedbasal pages 1-2)

---

## 5. Environmental Information

### 5.1 Environmental/lifestyle factors
The retrieved 2024 pediatric surveillance guideline emphasizes **sun protection counseling** and avoidance of **ionizing radiation** due to tumor risks in NBCCS. (hansford2024updateoncancer pages 2-3)

No additional quantified toxin/occupational exposure associations were present in the retrieved evidence set.

---

## 6. Mechanism / Pathophysiology

### 6.1 Core pathway: Hedgehog signaling dysregulation
A 2023 mechanistic review describes Gorlin syndrome as involving mutations in negative regulators (**PTCH1/PTCH2/SUFU**) of the Hedgehog pathway. PTCH1 encodes a multipass transmembrane receptor for SHH/IHH/DHH ligands and represses SMO; **PTCH1 loss leads to constitutive SMO activation and aberrant activation of GLI transcription factors**, driving developmental anomalies and tumorigenesis. (onodera2023hedgehogrelatedmutationcauses pages 2-4)

### 6.2 Causal chain (gene → pathway → cell behavior → phenotype)
- **Upstream trigger:** germline loss-of-function variant in PTCH1 (or SUFU/PTCH2) (onodera2023hedgehogrelatedmutationcauses pages 2-4, murgia2024gorlinsyndromeassociatedbasal pages 1-2)
- **Pathway effect:** disinhibition of SMO → GLI activation (onodera2023hedgehogrelatedmutationcauses pages 2-4)
- **Cellular processes:** dysregulated proliferation/differentiation in skin adnexal/epithelial lineages and craniofacial/bone development programs (inferred from pathway’s role in development and tumorigenesis as described) (onodera2023hedgehogrelatedmutationcauses pages 2-4)
- **Clinical manifestations:** multiple BCCs, odontogenic cysts, skeletal anomalies, and early childhood SHH-medulloblastoma in high-risk genotypes (onodera2023hedgehogrelatedmutationcauses pages 2-4, hansford2024updateoncancer pages 3-4)

### 6.3 Suggested GO / CL annotations (for KB normalization)
The retrieved sources do not provide explicit GO/CL terms; plausible normalizations consistent with described biology include:
- **GO biological process (suggestions):** Hedgehog signaling pathway; regulation of cell proliferation; embryonic skeletal system development; epithelial cell proliferation.
- **CL cell types (suggestions):** basal keratinocyte; hair follicle epithelial cell; odontogenic epithelial cell; cerebellar granule neuron precursor (relevant to SHH-medulloblastoma).

---

## 7. Anatomical Structures Affected

### 7.1 Organ/tissue systems (high-confidence from retrieved evidence)
- **Skin:** multiple basal cell carcinomas (onodera2023hedgehogrelatedmutationcauses pages 2-4, wescott2023sustainedsuppressionof pages 1-2)
- **Jaw/maxillofacial tissues:** odontogenic keratocysts (onodera2023hedgehogrelatedmutationcauses pages 2-4, kammoun2024theoralfacialmanifestations pages 17-25)
- **Central nervous system:** SHH-medulloblastoma risk (especially SUFU) (hansford2024updateoncancer pages 3-4)
- **Ovary:** ovarian fibromas (often bilateral) (zhu2023bilateralovarianfibromas pages 1-4)
- **Heart:** cardiac fibroma (screened in infancy per guideline) (hansford2024updateoncancer pages 2-3)

### 7.2 Suggested UBERON mappings (labels)
- Skin; jaw; cerebellum/brain; ovary; heart.

---

## 8. Temporal Development (natural history)

### 8.1 Onset patterns
- **OKCs:** mean onset ~15.5 years (childhood/adolescence). (onodera2023hedgehogrelatedmutationcauses pages 2-4)
- **BCCs:** mean onset ~20.3 years with strong ancestry-dependent penetrance estimates in the cited review. (onodera2023hedgehogrelatedmutationcauses pages 2-4)
- **Medulloblastoma:** concentrated in **infancy/early childhood**; surveillance recommendations focus on the first 5 years (SUFU subgroup). (hansford2024updateoncancer pages 3-4, hansford2024updateoncancer pages 2-3)

### 8.2 Progression/course
The disease course is lifelong with repeated tumor occurrence (particularly BCCs), often requiring repeated local treatments or systemic pathway inhibition when burden is high. (wescott2023sustainedsuppressionof pages 1-2, murgia2024gorlinsyndromeassociatedbasal pages 1-2)

---

## 9. Inheritance and Population

### 9.1 Inheritance
Autosomal dominant. (kammoun2024theoralfacialmanifestations pages 30-34, murgia2024gorlinsyndromeassociatedbasal pages 1-2)

### 9.2 De novo rate
Across 2023–2024 sources, **~20–30%** of cases are attributed to **de novo pathogenic variation**, with **~70–80%** having family history. (murgia2024gorlinsyndromeassociatedbasal pages 1-2, wescott2023sustainedsuppressionof pages 1-2)

### 9.3 Epidemiology (prevalence)
Prevalence estimates in the retrieved sources cluster around:
- **~1:57,000** with a reported range **1:30,827–1:164,000** (northwest England estimate cited in 2024 cohort and 2023 case series). (murgia2024gorlinsyndromeassociatedbasal pages 1-2, wescott2023sustainedsuppressionof pages 1-2)
- A broader estimate of **1 in 50,000 to 256,000** is also reported in a 2024 review excerpt. (kammoun2024theoralfacialmanifestations pages 17-25)

### 9.4 Sex ratio
Similar rates in males and females are expected/observed given autosomal dominant inheritance (explicitly stated in a 2023 case-series excerpt). (wescott2023sustainedsuppressionof pages 1-2)

---

## 10. Diagnostics

### 10.1 Clinical diagnostic criteria (major/minor)
Across 2023–2024 sources, diagnosis is described as based on combinations of major/minor criteria.

**Major criteria (commonly listed):**
- Multiple BCCs or early-onset BCC burden (e.g., >5 or BCC at young age)
- Jaw odontogenic keratocysts
- Palmar/plantar pits
- Lamellar calcification of the falx cerebri
- Medulloblastoma
- First-degree relative with NBCCS (murgia2024gorlinsyndromeassociatedbasal pages 1-2, wescott2023sustainedsuppressionof pages 1-2)

**Rule-based diagnosis (example reported in 2024 cohort):** “two major + one minor, or one major + three minor criteria.” (murgia2024gorlinsyndromeassociatedbasal pages 1-2)

### 10.2 Molecular diagnosis and genetic testing strategy
**Key concept:** Molecular confirmation with heterozygous germline **PTCH1 or SUFU** pathogenic variants can establish diagnosis when clinical features are incomplete. (wescott2023sustainedsuppressionof pages 2-4)

**2024 development (DNA+RNA sequencing):** Mochizuki et al. show that standard clinical DNA approaches (panel/GS) may miss mobile-element insertions; paired tumor/normal exome plus RNA-seq can provide confirmation (PTCH1 c.361_362insAlu). (mochizuki2024germlineptch1c.361362insalu pages 1-2, mochizuki2024germlineptch1c.361362insalu pages 3-4)

### 10.3 Imaging and other testing
- **Dental imaging** (orthopantomogram) is explicitly included in surveillance/diagnostic workflows for PTCH1 carriers; MRI can substitute in some guidance. (hansford2024updateoncancer pages 2-3, hansford2024updateoncancer media cb459877)
- **Brain MRI** for medulloblastoma surveillance is recommended in SUFU carriers in early childhood (see §11). (hansford2024updateoncancer pages 2-3)

### 10.4 Differential diagnosis
No explicit differential diagnosis list was present in the retrieved evidence snippets.

---

## 11. Outcome / Prognosis

### 11.1 Tumor risks and prognostic stratification (gene-specific)
A key 2024 guideline update provides **absolute SHH-medulloblastoma risks**:
- **SUFU:** ~**7%–9.2%**
- **PTCH1:** ~**0.37%–1.1%** (hansford2024updateoncancer pages 3-4)

This genotype risk stratification drives surveillance intensity (SUFU vs PTCH1; see below). (hansford2024updateoncancer pages 3-4, hansford2024updateoncancer pages 2-3)

### 11.2 Morbidity and burden
The principal morbidity in many patients stems from repeated BCC occurrence and associated procedural burden/disfigurement, motivating systemic therapies when local therapy becomes impractical. (murgia2024gorlinsyndromeassociatedbasal pages 1-2, wescott2023sustainedsuppressionof pages 1-2)

---

## 12. Treatment

### 12.1 Local/surgical management (current practice)
Patients frequently undergo repeated excisions or other local therapies for BCCs and management of OKCs; the 2024 cohort emphasizes high lifetime procedural burden (“dozens or even hundreds of surgical procedures”). (murgia2024gorlinsyndromeassociatedbasal pages 1-2)

### 12.2 Targeted pharmacotherapy: Hedgehog pathway inhibitors (HHIs)
**Agents:** vismodegib and sonidegib (SMO inhibitors) are used to suppress BCC development in high-burden NBCCS patients. (wescott2023sustainedsuppressionof pages 1-2, murgia2024gorlinsyndromeassociatedbasal pages 1-2)

**Effectiveness in Gorlin syndrome cohorts (2023–2024):**
- In a 10-patient case series (published 2023-10; *Current Oncology*; https://doi.org/10.3390/curroncol30100661), “All patients achieved a complete remission,” and mean new tumors decreased from **28.3** before treatment to **1.4** during treatment (p=0.0048); median time to a new BCC was **47.3 months**. (wescott2023sustainedsuppressionof pages 1-2)
- In a 16-patient retrospective series (published 2024-06-07; *Cancers*; https://doi.org/10.3390/cancers16122166), sustained HHI therapy suppressed both new and existing BCCs, and **sonidegib** was reported as having superior efficacy and safety vs vismodegib, with schedule adjustments improving tolerability. (murgia2024gorlinsyndromeassociatedbasal pages 1-2)

**Adverse effects (class effects):** muscle cramps/spasms, taste changes (dysgeusia), alopecia, fatigue/asthenia are commonly noted. (wescott2023sustainedsuppressionof pages 1-2, wescott2023sustainedsuppressionof pages 2-4)

### 12.3 Real-world implementation and safety (2024 post-authorization data)
The NISSO non-interventional post-authorization sonidegib study (published 2024-11; *BMC Cancer*; https://doi.org/10.1186/s12885-024-13101-z) enrolled **321** laBCC patients (median age 77), including **12.2% (n=39) with Gorlin syndrome**. (gutzmer2024interimanalysisof pages 2-4)

Key safety statistics:
- ≥1 TEAE: **88.5%**
- Most common TEAEs: muscle spasms **43.9%**, dysgeusia **37.1%**, alopecia **30.2%**
- TEAE-related: discontinuation **18.4%**, dose reduction **22.7%**, interruption **30.5%**
- Serious drug-related TEAEs: **4.1%** (gutzmer2024interimanalysisof pages 2-4)

### 12.4 MAXO suggestions (treatment actions)
Suggested MAXO-normalizations (labels) consistent with described management:
- Hedgehog pathway inhibitor therapy
- Dermatologic surveillance
- Surgical excision of basal cell carcinoma
- Dental/maxillofacial surgery for odontogenic keratocysts
- Genetic counseling

---

## 13. Prevention

### 13.1 Primary/secondary prevention
Guideline-level prevention focuses on:
- **Sun protection counseling**
- **Avoidance of ionizing radiation when feasible**
- **Surveillance** to detect medulloblastoma and other tumors early (gene-specific) (hansford2024updateoncancer pages 2-3)

### 13.2 Surveillance (gene-specific; 2024 AACR guidance)
The 2024 AACR working group recommends gene-tailored surveillance, particularly for early childhood SHH-medulloblastoma. (hansford2024updateoncancer pages 3-4)

Key surveillance elements for Gorlin syndrome (from Table 1):
- **SUFU carriers:** brain MRI **q3–4 months until age 3**, then **q6 months until age 5**; neurologic exam/head circumference checks **q3–4 months until age 5**. (hansford2024updateoncancer pages 2-3, hansford2024updateoncancer media cb459877)
- **PTCH1 carriers:** routine neuroimaging generally not recommended; emphasize clinical vigilance; dental and jaw surveillance using orthopantomogram or MRI. (hansford2024updateoncancer pages 3-4, hansford2024updateoncancer media cb459877)
- **Echocardiogram:** baseline in infancy (<6 months) to evaluate cardiac fibroma. (hansford2024updateoncancer pages 2-3, hansford2024updateoncancer media cb459877)
- **Ovarian ultrasound:** per Table 1, PTCH1 “once at 18 years,” SUFU “every 3 years starting at 5 years” (and MRI substitution if ultrasound not feasible). (hansford2024updateoncancer pages 2-3, hansford2024updateoncancer media cb459877)

**Visual evidence:** the extracted Table 1 image segment containing these intervals is provided in the cited figure. (hansford2024updateoncancer media cb459877)

---

## 14. Other Species / Natural Disease
No evidence for naturally occurring Gorlin syndrome analogs in non-human species was found in the retrieved sources.

---

## 15. Model Organisms
The retrieved 2023–2024 evidence set did not include explicit descriptions of specific named engineered animal models (e.g., Ptch1+/− mice) or in vitro models, beyond general statements that Hedgehog signaling is essential in development and tumorigenesis. This is an evidence gap in the current retrieval and should be filled by targeted searches of model organism databases (MGI/IMPC) if required for your KB. (onodera2023hedgehogrelatedmutationcauses pages 2-4)

---

## Recent developments (2023–2024 highlights)
1. **Gene-specific surveillance refined for childhood SHH-medulloblastoma risk:** SUFU carriers receive routine MRI surveillance in early childhood, while PTCH1 carriers generally do not, reflecting the large absolute risk differential. (*Clin Cancer Res*, 2024-04; https://doi.org/10.1158/1078-0432.ccr-23-4033). (hansford2024updateoncancer pages 3-4, hansford2024updateoncancer pages 2-3)
2. **Diagnostics advancing beyond standard DNA panels:** 2024 evidence shows RNA sequencing can confirm cryptic mobile-element insertions in PTCH1 missed by routine testing, supporting DNA+RNA workflows in strong clinical suspicion cases. (*Am J Med Genet A*, 2024-06; https://doi.org/10.1002/ajmg.a.63788). (mochizuki2024germlineptch1c.361362insalu pages 1-2, mochizuki2024germlineptch1c.361362insalu pages 3-4)
3. **Real-world HHI tolerability quantified in routine practice (including Gorlin subgroup):** NISSO provides contemporary AE/discontinuation rates for sonidegib, with 12.2% Gorlin patients. (*BMC Cancer*, 2024-11; https://doi.org/10.1186/s12885-024-13101-z). (gutzmer2024interimanalysisof pages 2-4)
4. **New prevention-focused topical Hh inhibitor trials ongoing:** Phase 3 topical patidegib (2%) prevention trial active (not recruiting) targeting reduction of new facial BCCs in PTCH1-confirmed Gorlin syndrome. (ClinicalTrials.gov NCT06050122; start 2024-03-17). (NCT06050122 chunk 1)

---

## Key URLs and publication dates (selected)
- Hansford et al. *Clinical Cancer Research* (2024-04): https://doi.org/10.1158/1078-0432.ccr-23-4033 (hansford2024updateoncancer pages 3-4)
- Gutzmer et al. *BMC Cancer* (2024-11): https://doi.org/10.1186/s12885-024-13101-z (gutzmer2024interimanalysisof pages 1-2)
- Murgia et al. *Cancers* (2024-06-07): https://doi.org/10.3390/cancers16122166 (murgia2024gorlinsyndromeassociatedbasal pages 1-2)
- Mochizuki et al. *Am J Med Genet A* (2024-06): https://doi.org/10.1002/ajmg.a.63788 (mochizuki2024germlineptch1c.361362insalu pages 1-2)
- Wescott & Samlowski *Current Oncology* (2023-10-16): https://doi.org/10.3390/curroncol30100661 (wescott2023sustainedsuppressionof pages 1-2)
- Zhu et al. *Diagnostic Pathology* (2023-10): https://doi.org/10.1186/s13000-023-01406-9 (zhu2023bilateralovarianfibromas pages 1-4)
- ClinicalTrials.gov NCT06050122 (patidegib gel 2% Phase 3; started 2024-03-17): evidence extracted from trial record (NCT06050122 chunk 1)

---

## Limitations of this report (due to retrieved evidence)
- **PMIDs** were not present in the retrieved tool excerpts; DOIs and ClinicalTrials.gov identifiers are provided instead.
- **ICD-10/ICD-11, Orphanet, and MONDO** identifiers were not found in the retrieved texts.
- Model organism evidence was not directly retrieved; additional targeted searches are required for that section.


References

1. (kammoun2024theoralfacialmanifestations pages 17-25): K Kammoun. The oral-facial manifestations of gorlin syndrome. Unknown journal, 2024.

2. (murgia2024gorlinsyndromeassociatedbasal pages 1-2): Giulia Murgia, Luca Valtellini, Nerina Denaro, Gianluca Nazzaro, Paolo Bortoluzzi, Valentina Benzecry, Emanuela Passoni, and Angelo Valerio Marzano. Gorlin syndrome-associated basal cell carcinomas treated with vismodegib or sonidegib: a retrospective study. Cancers, 16:2166, Jun 2024. URL: https://doi.org/10.3390/cancers16122166, doi:10.3390/cancers16122166. This article has 15 citations.

3. (NCT03703310 chunk 3):  Study of Patidegib Topical Gel, 2%, for the Reduction of Disease Burden of Persistently Developing Basal Cell Carcinomas (BCCs) in Subjects With Basal Cell Nevus Syndrome (Gorlin Syndrome). Sol-Gel Technologies, Ltd.. 2019. ClinicalTrials.gov Identifier: NCT03703310

4. (wescott2023sustainedsuppressionof pages 1-2): Raquel Wescott and Wolfram Samlowski. Sustained suppression of gorlin syndrome-associated basal cell carcinomas with vismodegib or sonidegib: a case series. Current Oncology, 30:9156-9167, Oct 2023. URL: https://doi.org/10.3390/curroncol30100661, doi:10.3390/curroncol30100661. This article has 7 citations.

5. (onodera2023hedgehogrelatedmutationcauses pages 2-4): Shoko Onodera and Toshifumi Azuma. Hedgehog-related mutation causes bone malformations with or without hereditary gene mutations. International Journal of Molecular Sciences, 24:12903, Aug 2023. URL: https://doi.org/10.3390/ijms241612903, doi:10.3390/ijms241612903. This article has 10 citations.

6. (kammoun2024theoralfacialmanifestations pages 30-34): K Kammoun. The oral-facial manifestations of gorlin syndrome. Unknown journal, 2024.

7. (wescott2023sustainedsuppressionof pages 2-4): Raquel Wescott and Wolfram Samlowski. Sustained suppression of gorlin syndrome-associated basal cell carcinomas with vismodegib or sonidegib: a case series. Current Oncology, 30:9156-9167, Oct 2023. URL: https://doi.org/10.3390/curroncol30100661, doi:10.3390/curroncol30100661. This article has 7 citations.

8. (hansford2024updateoncancer pages 3-4): Jordan R. Hansford, Anirban Das, Rose B. McGee, Yoshiko Nakano, Jack Brzezinski, Sarah R. Scollon, Surya P. Rednam, Jaclyn Schienda, Orli Michaeli, Sun Young Kim, Mary-Louise C. Greer, Rosanna Weksberg, Douglas R. Stewart, William D. Foulkes, Uri Tabori, Kristian W. Pajtler, Stefan M. Pfister, Garrett M. Brodeur, and Junne Kamihara. Update on cancer predisposition syndromes and surveillance guidelines for childhood brain tumors. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:2342-2350, Apr 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-4033, doi:10.1158/1078-0432.ccr-23-4033. This article has 51 citations.

9. (zhu2023bilateralovarianfibromas pages 1-4): Menghan Zhu, Jun Li, Jie Duan, Jing Yang, Weiyong Gu, and Wei Jiang. Bilateral ovarian fibromas as the sole manifestation of gorlin syndrome in a 22-year-old woman: a case report and literature review. Diagnostic Pathology, Oct 2023. URL: https://doi.org/10.1186/s13000-023-01406-9, doi:10.1186/s13000-023-01406-9. This article has 3 citations and is from a peer-reviewed journal.

10. (hansford2024updateoncancer pages 2-3): Jordan R. Hansford, Anirban Das, Rose B. McGee, Yoshiko Nakano, Jack Brzezinski, Sarah R. Scollon, Surya P. Rednam, Jaclyn Schienda, Orli Michaeli, Sun Young Kim, Mary-Louise C. Greer, Rosanna Weksberg, Douglas R. Stewart, William D. Foulkes, Uri Tabori, Kristian W. Pajtler, Stefan M. Pfister, Garrett M. Brodeur, and Junne Kamihara. Update on cancer predisposition syndromes and surveillance guidelines for childhood brain tumors. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:2342-2350, Apr 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-4033, doi:10.1158/1078-0432.ccr-23-4033. This article has 51 citations.

11. (hansford2024updateoncancer media cb459877): Jordan R. Hansford, Anirban Das, Rose B. McGee, Yoshiko Nakano, Jack Brzezinski, Sarah R. Scollon, Surya P. Rednam, Jaclyn Schienda, Orli Michaeli, Sun Young Kim, Mary-Louise C. Greer, Rosanna Weksberg, Douglas R. Stewart, William D. Foulkes, Uri Tabori, Kristian W. Pajtler, Stefan M. Pfister, Garrett M. Brodeur, and Junne Kamihara. Update on cancer predisposition syndromes and surveillance guidelines for childhood brain tumors. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:2342-2350, Apr 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-4033, doi:10.1158/1078-0432.ccr-23-4033. This article has 51 citations.

12. (NCT06050122 chunk 1):  Efficacy and Safety of Patidegib Gel 2% for Preventing Basal Cell Carcinomas on the Face of Adults With Gorlin Syndrome. Sol-Gel Technologies, Ltd.. 2024. ClinicalTrials.gov Identifier: NCT06050122

13. (NCT02762084 chunk 1):  Trial of Patidegib Gel 2%, 4%, and Vehicle to Decrease the Number of Surgically Eligible Basal Cell Carcinomas in Gorlin Syndrome Patients. PellePharm, Inc.. 2016. ClinicalTrials.gov Identifier: NCT02762084

14. (NCT01350115 chunk 1):  Efficacy, Safety and Pharmacokinetics of Oral LDE225 in Treatment of Patients With Nevoid Basal Cell Carcinoma Syndrome (NBCCS). Novartis Pharmaceuticals. 2011. ClinicalTrials.gov Identifier: NCT01350115

15. (NCT00961896 chunk 1):  A Trial to Evaluate the Safety, Local Tolerability, Pharmacokinetics and Pharmacodynamics of LDE225 on Skin Basal Cell Carcinomas in Gorlin Syndrome Patients. Novartis Pharmaceuticals. 2009. ClinicalTrials.gov Identifier: NCT00961896

16. (gutzmer2024interimanalysisof pages 1-2): Ralf Gutzmer, Ulrike Leiter, Peter Mohr, Katharina C. Kähler, Paolo Antonio Ascierto, Massimiliano Scalvenzi, Ketty Peris, Gemma María Pérez-Pastor, Ricardo Fernández-de-Misa, Rafael Botella-Estrada, Robert E. Hunger, Serena Martelli, Nur Güneli, Ramon Arntz, and Axel Hauschild. Interim analysis of the multinational, post-authorization safety study (nisso) to assess the long-term safety of sonidegib in patients with locally advanced basal cell carcinoma. BMC Cancer, Nov 2024. URL: https://doi.org/10.1186/s12885-024-13101-z, doi:10.1186/s12885-024-13101-z. This article has 11 citations and is from a peer-reviewed journal.

17. (gutzmer2024interimanalysisof pages 2-4): Ralf Gutzmer, Ulrike Leiter, Peter Mohr, Katharina C. Kähler, Paolo Antonio Ascierto, Massimiliano Scalvenzi, Ketty Peris, Gemma María Pérez-Pastor, Ricardo Fernández-de-Misa, Rafael Botella-Estrada, Robert E. Hunger, Serena Martelli, Nur Güneli, Ramon Arntz, and Axel Hauschild. Interim analysis of the multinational, post-authorization safety study (nisso) to assess the long-term safety of sonidegib in patients with locally advanced basal cell carcinoma. BMC Cancer, Nov 2024. URL: https://doi.org/10.1186/s12885-024-13101-z, doi:10.1186/s12885-024-13101-z. This article has 11 citations and is from a peer-reviewed journal.

18. (mochizuki2024germlineptch1c.361362insalu pages 1-2): Aaron Y. Mochizuki, Chinmayee B. Nagaraj, Douglas Depoorter, Kathleen M. Schieffer, and Sun Young Kim. Germline ptch1: c.361_362insalu alteration identified by comprehensive exome and rna sequencing in a patient with gorlin syndrome. American Journal of Medical Genetics Part A, Jun 2024. URL: https://doi.org/10.1002/ajmg.a.63788, doi:10.1002/ajmg.a.63788. This article has 1 citations.

19. (mochizuki2024germlineptch1c.361362insalu pages 3-4): Aaron Y. Mochizuki, Chinmayee B. Nagaraj, Douglas Depoorter, Kathleen M. Schieffer, and Sun Young Kim. Germline ptch1: c.361_362insalu alteration identified by comprehensive exome and rna sequencing in a patient with gorlin syndrome. American Journal of Medical Genetics Part A, Jun 2024. URL: https://doi.org/10.1002/ajmg.a.63788, doi:10.1002/ajmg.a.63788. This article has 1 citations.

20. (mochizuki2024germlineptch1c.361362insalu pages 2-3): Aaron Y. Mochizuki, Chinmayee B. Nagaraj, Douglas Depoorter, Kathleen M. Schieffer, and Sun Young Kim. Germline ptch1: c.361_362insalu alteration identified by comprehensive exome and rna sequencing in a patient with gorlin syndrome. American Journal of Medical Genetics Part A, Jun 2024. URL: https://doi.org/10.1002/ajmg.a.63788, doi:10.1002/ajmg.a.63788. This article has 1 citations.
