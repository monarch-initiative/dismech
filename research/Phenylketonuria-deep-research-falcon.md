---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-25T22:15:47.850192'
end_time: '2026-04-25T22:29:02.069035'
duration_seconds: 794.22
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Phenylketonuria
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 33
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Phenylketonuria
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Phenylketonuria** covering all of the
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
- **Disease Name:** Phenylketonuria
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Phenylketonuria** covering all of the
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


# Phenylketonuria (PKU) — Disease Characteristics Research Report (Genetic)

## Executive summary
Phenylketonuria (PKU) is an autosomal recessive inborn error of metabolism most commonly caused by biallelic pathogenic variants in **PAH** (phenylalanine hydroxylase), leading to reduced conversion of phenylalanine (Phe) to tyrosine (Tyr) and consequent hyperphenylalaninemia with neurotoxicity if untreated. Newborn screening (NBS) plus early initiation of therapy largely prevents severe intellectual disability, but many adolescents/adults have difficulty maintaining recommended blood Phe targets with diet alone, with persistent neurocognitive, psychiatric, and somatic comorbidity burdens motivating pharmacologic and emerging gene-therapy approaches. (pinto2024bloodphenylalaninelevels pages 2-3, spronsen2017keyeuropeanguidelines pages 1-1, martinez2024state‐of‐the‐art2023on pages 1-3)

| Domain | Key details | Source (author/year) | URL/DOI |
|---|---|---|---|
| Definition / etiology | Phenylketonuria (PKU) is a rare autosomal recessive inborn error of phenylalanine metabolism caused by biallelic **PAH** variants leading to deficient hepatic phenylalanine hydroxylase activity; PAH normally converts phenylalanine to tyrosine using tetrahydrobiopterin (BH4). Untreated elevation of blood/brain phenylalanine causes severe neurocognitive injury. (pinto2024bloodphenylalaninelevels pages 2-3, spronsen2017keyeuropeanguidelines pages 1-1, martinez2024state‐of‐the‐art2023on pages 1-3) | van Spronsen et al./2017; Pinto et al./2024; Martinez et al./2024 | https://doi.org/10.1016/S2213-8587(16)30320-5; https://doi.org/10.3390/nu16132064; https://doi.org/10.1002/jimd.12651 |
| Key identifiers | **OMIM: 261600**; common labels/synonyms in recent literature include **phenylketonuria**, **PAH deficiency**, and **phenylalanine hydroxylase deficiency**. OMIM 261600 is explicitly cited in recent PKU guideline/update and QoL papers. (cunningham2023nutritionmanagementof pages 1-2, maissenabgottspon2023healthrelatedqualityof pages 1-2) | Cunningham et al./2023; Maissen-Abgottspon et al./2023 | https://doi.org/10.1186/s13023-023-02751-0; https://doi.org/10.1186/s13023-023-02917-w |
| European 2017 blood Phe targets | European guideline targets: **120–360 µmol/L** for ages **0–12 years** and for **maternal PKU**; **120–600 µmol/L** for **non-pregnant individuals >12 years**. Blood phenylalanine is the principal treatment biomarker. (pinto2024bloodphenylalaninelevels pages 2-3, spronsen2017keyeuropeanguidelines pages 1-1, spronsen2017keyeuropeanguidelines pages 4-5) | van Spronsen et al./2017; Pinto et al./2024 | https://doi.org/10.1016/S2213-8587(16)30320-5; https://doi.org/10.3390/nu16132064 |
| European 2017 treatment thresholds | European 2017 guidance: **no treatment if untreated Phe <360 µmol/L**; **treat up to age 12** when untreated Phe is **360–600 µmol/L**; **lifelong treatment recommended if untreated Phe >600 µmol/L**. (spronsen2017keyeuropeanguidelines pages 1-1) | van Spronsen et al./2017 | https://doi.org/10.1016/S2213-8587(16)30320-5 |
| Main treatment: diet | Cornerstone therapy is lifelong **phenylalanine-restricted diet** with **Phe-free/low-Phe protein substitutes/medical foods** and low-protein specialty foods to maintain blood Phe in target range while supporting nutrition. Long-term effectiveness is limited by high treatment burden and declining adherence with age. (rocha2023expertconsensuson pages 1-2, cunningham2023nutritionmanagementof pages 1-2, rocha2023expertconsensuson pages 4-5) | Rocha et al./2023; Cunningham et al./2023 | https://doi.org/10.3390/nu15183940; https://doi.org/10.1186/s13023-023-02751-0 |
| Main treatment: sapropterin | **Sapropterin dihydrochloride (BH4 analogue)** increases residual PAH activity in responsive patients; recent reviews report benefit mainly in milder/responsive phenotypes, with about **20–50%** responsive in broad summaries and lower response in severe disease. In the 2024 Europe cohort, sapropterin-treated patients had mean Phe **391 ± 334 µmol/L** and **84 ± 39%** measurements within target vs diet-only **406 ± 334 µmol/L** and **73 ± 41%**. (pinto2024bloodphenylalaninelevels pages 2-3, martinez2024state‐of‐the‐art2023on pages 1-3) | Pinto et al./2024; Martinez et al./2024 | https://doi.org/10.3390/nu16132064; https://doi.org/10.1002/jimd.12651 |
| Main treatment: pegvaliase | **Pegvaliase (PALYNZIQ)** is an injectable phenylalanine ammonia lyase enzyme substitution therapy that lowers blood Phe independently of PAH. Approval years noted in recent guideline update: **FDA 2018** and **EMA 2019**. It can enable substantial diet liberalization or even unrestricted diet in responders, but early treatment is associated with immune-mediated hypersensitivity adverse events. (cunningham2023nutritionmanagementof pages 1-2, martinez2024state‐of‐the‐art2023on pages 10-12, rocha2023expertconsensuson pages 4-5) | Cunningham et al./2023; Martinez et al./2024; Rocha et al./2023 | https://doi.org/10.1186/s13023-023-02751-0; https://doi.org/10.1002/jimd.12651; https://doi.org/10.3390/nu15183940 |
| 2024 Europe cohort: control by age | In a 9-centre European/Turkish cohort (**n=1323**, age 1–57 y), the percentage of blood Phe values within target declined with age: **<2 y 89%**, **2–5 y 84%**, **6–12 y 73%**, **13–18 y 85%**, **19–30 y 64%**, **31–40 y 59%**, **≥41 y 40%**. Control was best in HPA and poorest in classical PKU. (pinto2024bloodphenylalaninelevels pages 2-3) | Pinto et al./2024 | https://doi.org/10.3390/nu16132064 |
| 2024 Europe cohort: monitoring frequency | More frequent blood Phe monitoring was associated with better control: **weekly** sampling mean Phe **271 ± 204 µmol/L** with **81%** within target; **every 2 weeks** **376 ± 262 µmol/L** with **78%** within target; **every 4 weeks** **426 ± 282 µmol/L** with **71%** within target; **less than monthly** **534 ± 468 µmol/L** with **70%** within target. (pinto2024bloodphenylalaninelevels pages 2-3) | Pinto et al./2024 | https://doi.org/10.3390/nu16132064 |


*Table: This table condenses the most actionable PKU facts from the gathered evidence, including definition, identifiers, European guideline blood phenylalanine targets, core treatments, and 2024 real-world cohort statistics. It is useful as a quick reference for disease knowledge base curation and evidence-backed summarization.*

---

## 1. Disease Information

### 1.1 What is the disease?
PKU is defined in authoritative guideline and review literature as an autosomal recessive defect of phenylalanine metabolism due to **phenylalanine hydroxylase (PAH) deficiency**, causing elevated Phe in blood/brain and (if untreated) severe neurodevelopmental sequelae. (spronsen2017keyeuropeanguidelines pages 1-1, martinez2024state‐of‐the‐art2023on pages 1-3)

**Direct abstract quote (European guideline):** “Phenylketonuria (PKU) is an autosomal recessive inborn error of phenylalanine metabolism caused by deficiency in the enzyme phenylalanine hydroxylase that converts phenylalanine into tyrosine.” (spronsen2017keyeuropeanguidelines pages 1-1)

### 1.2 Key identifiers (requested: OMIM, Orphanet, ICD-10/ICD-11, MeSH, MONDO)
* **OMIM:** **261600** (explicitly cited as “PKU, OMIM 261600” in recent clinical literature). (cunningham2023nutritionmanagementof pages 1-2, maissenabgottspon2023healthrelatedqualityof pages 1-2)
* **Orphanet / ICD / MeSH / MONDO:** Not directly extractable from the currently retrieved full texts; additional direct database queries (e.g., Orphanet, MONDO, MeSH Browser, ICD-11) would be required for authoritative IDs.

### 1.3 Synonyms and alternative names
Frequently used equivalents include:
* **PAH deficiency** / **phenylalanine hydroxylase deficiency** (common in guidelines and mechanistic reviews). (spronsen2017keyeuropeanguidelines pages 1-1, martinez2024state‐of‐the‐art2023on pages 1-3)
* **Hyperphenylalaninemia (HPA)** is often used as an umbrella phenotype category; PKU is typically reserved for higher untreated Phe ranges or clinically significant disease requiring treatment. (pinto2024bloodphenylalaninelevels pages 2-3, hofman2018dietaryadherencein pages 41-45)

### 1.4 Evidence sources: individual vs aggregated resources
Most core disease knowledge (definition, targets, thresholds) is derived from aggregated guideline and consensus processes (systematic evidence grading plus Delphi methods) as in the European guidelines. (spronsen2017keyeuropeanguidelines pages 1-1)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause (genetic/mechanistic):** biallelic PAH variants → reduced PAH enzyme activity → increased Phe and altered Tyr availability; PAH uses **tetrahydrobiopterin (BH4)** as a cofactor. (pinto2024bloodphenylalaninelevels pages 2-3, spronsen2017keyeuropeanguidelines pages 1-1)

### 2.2 Risk factors
* **Genetic:** pathogenic PAH variants (many alleles; an example allele specifically noted in a recent European cohort paper is **c.1222C>T (p.Arg408Trp)**). (pinto2024bloodphenylalaninelevels pages 2-3)
* **Environmental / behavioral:** the dominant modifiable “risk factor” for clinical deterioration is **chronic exposure to elevated blood Phe**, largely driven by difficulty adhering to restrictive diet over time. Age-related deterioration of metabolic control is documented in large European real-world data. (pinto2024bloodphenylalaninelevels pages 2-3)

### 2.3 Protective factors
* **Early detection by NBS and early treatment** is protective against the classic severe neurodevelopmental phenotype. (spronsen2017keyeuropeanguidelines pages 1-1)
* **More frequent blood Phe monitoring** is associated with better control (likely enabling faster dietary/therapy adjustments). (pinto2024bloodphenylalaninelevels pages 2-3)

### 2.4 Gene–environment interaction
PKU is a canonical gene–environment interaction disease: the **genotype (residual PAH function; BH4 responsiveness)** interacts with **dietary Phe exposure** to determine blood Phe and outcomes; guideline targets are operationalized as blood Phe thresholds for lifelong management. (spronsen2017keyeuropeanguidelines pages 1-1, spronsen2017keyeuropeanguidelines pages 4-5)

---

## 3. Phenotypes (clinical spectrum)

### 3.1 Phenotype spectrum and laboratory phenotype categories
A commonly used severity schema (based on untreated Phe) includes:
* **Mild hyperphenylalaninemia:** ~120–600 µmol/L
* **Classic PKU:** often >1200 µmol/L
These categorical thresholds are summarized in recent literature and reviews. (alfadhel2024firstsuccessfuloutcomes pages 1-2, yu2025advancinggenetherapy pages 2-4)

### 3.2 Major clinical manifestations (with suggested HPO terms)
**Untreated/late-treated PKU** is associated with severe neurodevelopmental outcomes (intellectual disability, seizures/epilepsy, behavioral problems). (spronsen2017keyeuropeanguidelines pages 1-1)

**Early-treated PKU (lifelong care):** subtle but clinically relevant outcomes can persist, especially with higher Phe exposure:
* **Executive dysfunction** (HP:0000726)
* **Attention deficit** (HP:0007018)
* **Memory impairment** (HP:0002354)
* **Anxiety** (HP:0000739)
* **Depressive mood** (HP:0000716)
* **Ataxia** (HP:0001251) / tremor (HP:0001337)
These associations are emphasized in cohort and guideline discussions linking blood Phe to neuropsychological and neurological outcomes. (pinto2024bloodphenylalaninelevels pages 2-3, spronsen2017keyeuropeanguidelines pages 4-5)

### 3.3 Age of onset, progression, and frequency
* **Onset:** congenital; clinically silent at birth; adverse outcomes emerge with sustained feeding/accumulation without treatment (hence NBS importance). (spronsen2017keyeuropeanguidelines pages 1-1)
* **Progression:** metabolic control commonly deteriorates after childhood/adolescence and into adulthood, with a clear age gradient in real-world data. (pinto2024bloodphenylalaninelevels pages 2-3)

### 3.4 Quality of life (QoL) impact (recent primary data)
In a cross-sectional European study of **124 adults with early-treated classical PKU**, most QoL domains showed “little or no impact,” and “more than three-quarters” rated their health status as good/very good/excellent; however, fatigue (“tiredness”), guilt about dietary non-adherence, and pregnancy-related Phe concerns were salient. (maissenabgottspon2023healthrelatedqualityof pages 1-2)

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes
* **PAH** is the principal causal gene for classic PKU / PAH deficiency. (spronsen2017keyeuropeanguidelines pages 1-1, martinez2024state‐of‐the‐art2023on pages 1-3)

### 4.2 Pathogenic variants (current understanding)
A comprehensive variant catalogue is not present in the retrieved texts, but recent gene-therapy-oriented reviews note very large allelic heterogeneity (thousands of reported PAH variants) and population-specific common alleles; example common alleles are listed (e.g., R408W). (yu2025advancinggenetherapy pages 2-4)

### 4.3 BH4 responsiveness (therapeutic stratifier)
BH4 responsiveness is central to precision management:
* European guidelines note that “some patients benefit from tetrahydrobiopterin (BH4).” (spronsen2017keyeuropeanguidelines pages 1-1)
* Expert consensus highlights substantial non-responsiveness in more severe phenotypes; one expert consensus summary states “about 50–80% of patients, especially those with a more severe disease phenotype, are unresponsive to sapropterin.” (rocha2023expertconsensuson pages 1-2)

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
Not extractable from the currently retrieved texts.

---

## 5. Environmental Information
The dominant environmental determinant of phenotype severity is **dietary phenylalanine exposure** (and adherence to medical nutrition therapy), rather than exogenous toxins or infections. Restrictive dietary therapy itself can influence broader physiology (e.g., nutrient status), motivating ongoing monitoring and therapy optimization. (rocha2023expertconsensuson pages 1-2, pinto2024bloodphenylalaninelevels pages 2-3)

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (upstream → downstream)
1. **PAH deficiency** reduces hepatic conversion of **Phe → Tyr** (BH4-dependent). (spronsen2017keyeuropeanguidelines pages 1-1, pinto2024bloodphenylalaninelevels pages 2-3)
2. **Elevated blood Phe** and altered amino-acid balance leads to brain exposure.
3. **Neurotoxicity mechanisms** include reduced transport of other large neutral amino acids across the blood–brain barrier and downstream neurotransmitter synthesis disruption.

Guidelines explicitly note that high Phe causes neurocognitive impairment via “reduced LNAA transport and decreases in neurotransmitter synthesis (↓Trp→↓serotonin; ↓Tyr→↓dopamine).” (spronsen2017keyeuropeanguidelines pages 4-5)

### 6.2 Neuroimaging/brain structure outcomes (recent studies)
**Adult treated PKU still shows structural brain differences** in contemporary cohorts:
* In a neurodevelopmental disorders study (PKU n=35; controls n=22), adults with PKU had lower Full Scale IQ and reduced volumes in pallidum, hippocampus, amygdala, brainstem, and total cerebral white matter; blood Phe correlated negatively with pallidum and brainstem volumes. (pinto2024bloodphenylalaninelevels pages 2-3)

### 6.3 Suggested ontology terms
* **GO biological processes:** phenylalanine catabolic process; aromatic amino acid family metabolic process; neurotransmitter biosynthetic process.
* **UBERON anatomical sites:** liver (primary metabolic defect), brain/white matter/subcortical structures (major affected targets).
* **CHEBI:** phenylalanine; tyrosine; tetrahydrobiopterin.

(These ontology mappings are consistent with the mechanistic chain described in guidelines and cohort papers, though explicit ontology annotations are not contained in the retrieved texts.) (pinto2024bloodphenylalaninelevels pages 2-3, spronsen2017keyeuropeanguidelines pages 4-5)

---

## 7. Anatomical Structures Affected
* **Primary organ (disease origin):** liver (hepatic PAH deficiency). (spronsen2017keyeuropeanguidelines pages 1-1)
* **Primary target organ (toxicity):** brain (white matter and subcortical structures) with correlations to blood Phe. (pinto2024bloodphenylalaninelevels pages 2-3)

---

## 8. Temporal Development
* **Congenital onset** with potential for severe outcomes if untreated.
* **Lifelong course**: guideline targets are lifelong, and real-world data show deterioration of metabolic control with age, implying ongoing vulnerability across the lifespan. (pinto2024bloodphenylalaninelevels pages 2-3, spronsen2017keyeuropeanguidelines pages 1-1)

---

## 9. Inheritance and Population

### 9.1 Inheritance
Autosomal recessive inheritance is consistently stated in guidelines and contemporary reviews. (spronsen2017keyeuropeanguidelines pages 1-1, martinez2024state‐of‐the‐art2023on pages 1-3)

### 9.2 Epidemiology / prevalence / incidence
Not extractable from the currently retrieved texts.

### 9.3 Real-world metabolic-control statistics (Europe 2012–2018)
A 9-centre European/Turkish retrospective study of **1323** patients (age 1–57 years) reported that the **percentage of Phe values within target** declined with increasing age, with a particularly low proportion in older adults (≥41 years: 40%). (pinto2024bloodphenylalaninelevels pages 2-3)

---

## 10. Diagnostics

### 10.1 Screening
**Newborn screening** is the standard population screening approach for early identification and prevention of severe sequelae. (spronsen2017keyeuropeanguidelines pages 1-1)

### 10.2 Key diagnostic biomarker and targets
**Blood phenylalanine (Phe)** is the core biomarker for diagnosis and management. (spronsen2017keyeuropeanguidelines pages 1-1, pinto2024bloodphenylalaninelevels pages 2-3)

European 2017 guideline targets and treatment thresholds:
* Targets: **120–360 µmol/L** (0–12 years and maternal PKU) and **120–600 µmol/L** (>12 years, non-pregnant). (spronsen2017keyeuropeanguidelines pages 1-1, spronsen2017keyeuropeanguidelines pages 4-5)
* Threshold logic: **no intervention if untreated Phe <360 µmol/L**; **treat to age 12** when untreated Phe is **360–600 µmol/L**; **lifelong treatment** if untreated Phe **>600 µmol/L**. (spronsen2017keyeuropeanguidelines pages 1-1)

---

## 11. Outcome / Prognosis

### 11.1 Prognostic factors
Blood Phe exposure is repeatedly emphasized as the key modifiable prognostic factor; higher Phe is associated with worse neurocognitive and some structural brain outcomes. (pinto2024bloodphenylalaninelevels pages 2-3, spronsen2017keyeuropeanguidelines pages 4-5)

### 11.2 Maternal PKU (teratogenic risk)
European guidelines specify tighter pregnancy targets (120–360 µmol/L) and note that women with untreated Phe <360 µmol/L may not require lowering for pregnancy, reflecting the established fetal risk from elevated maternal Phe. (spronsen2017keyeuropeanguidelines pages 4-5)

---

## 12. Treatment (current practice, 2023–2024 developments)

### 12.1 Medical nutrition therapy (MNT)
MNT (low-Phe diet + protein substitutes/medical foods) remains foundational. Expert consensus in adults (Delphi panel) concluded MNT has **limited long-term effectiveness**, is associated with **high treatment burden**, and many adults cannot achieve adequate metabolic control on diet alone—supporting an “unmet need” in adult PKU. (rocha2023expertconsensuson pages 1-2)

**Expert opinion signal:** The same consensus notes an 85% agreement statement that adults should be offered pharmacologic options when available. (rocha2023expertconsensuson pages 4-5)

### 12.2 Sapropterin (BH4 analogue)
Sapropterin (BH4) is used for responsive patients with residual PAH activity. In the European cohort (n=1323), sapropterin-treated patients (n=222) had statistically lower mean Phe and higher proportion within target than diet-only, though the mean difference was modest. (pinto2024bloodphenylalaninelevels pages 2-3)

### 12.3 Pegvaliase (enzyme substitution therapy)
A 2023 update of the web-based GMDI/SERN PKU nutrition management guideline incorporated pegvaliase implementation and monitoring, noting regulatory approvals (FDA 2018; EMA 2019) and the possibility of substantial diet liberalization with successful therapy. (cunningham2023nutritionmanagementof pages 1-2)

**Quantitative efficacy and safety (PAL-003 extension):** In a long-term phase 2 extension (n=68 entering extension), mean Phe decreased ~59% to ~542 µmol/L at Week 48; thresholds ≤120, ≤360, and ≤600 µmol/L were achieved by ~79–83% of participants. Injection-site reactions, erythema, headache, and arthralgia were common; most AEs were mild/moderate. (longo2018longtermsafetyand pages 1-2)

### 12.4 Emerging therapies (2024–2026 clinical development)

#### JNT-517 (oral small-molecule; Otsuka) — clinical trials
* **NCT06971731** (Phase 3 adults; n≈120): randomized placebo-controlled trial with primary endpoint percent change in plasma Phe at Weeks 2/4/6 for 150 mg BID; includes responder thresholds such as <600, <360, <120 µmol/L. (NCT06971731 chunk 1)
* **NCT06637514** (Phase 2 adolescents 12–<18; n≈10): primary objectives safety/tolerability/PK; secondary outcomes include changes in plasma and urinary Phe. (NCT06637514 chunk 1)
* **NCT05781399** (First-in-human, healthy + PKU adults): includes urinary amino-acid change measures and PK comparisons. (NCT05781399 chunk 2)
* **NCT06628128** (Phase 3 open-label extension): long-term safety (TEAEs) and metabolic outcomes (plasma/urinary Phe; dietary intake). (NCT06628128 chunk 1)

#### AAV gene therapy (liver-directed PAH gene addition) — clinical trials
* **BMN 307 (BioMarin) — NCT04480567** (Phase 1/2; open-label; dose escalation; n≈100): primary outcome is change from baseline in mean plasma Phe at Week 12; secondary outcomes include Phe and dietary protein intake at Week 96 and TEAEs up to 5 years. (NCT04480567 chunk 1)
* Reviews of gene therapy note ongoing/terminated AAV programs and highlight safety concerns (e.g., transaminase elevations) and challenges for long-term expression, particularly in younger patients. (martinez2024state‐of‐the‐art2023on pages 10-12, yu2025advancinggenetherapy pages 11-12)

### 12.5 Suggested MAXO terms (examples)
* Dietary phenylalanine restriction / medical nutrition therapy (MAXO: dietary therapy)
* Sapropterin pharmacotherapy (MAXO: pharmacotherapy)
* Pegvaliase enzyme therapy (MAXO: enzyme replacement/enzyme substitution therapy)
* AAV-based gene transfer (MAXO: gene therapy)

(Explicit MAXO identifiers were not present in retrieved texts; these are conceptual mappings.)

---

## 13. Prevention
* **Secondary prevention:** NBS + early treatment initiation prevents severe irreversible neurodevelopmental injury. (spronsen2017keyeuropeanguidelines pages 1-1)
* **Tertiary prevention:** lifelong metabolic monitoring and maintaining target Phe ranges; more frequent monitoring is associated with improved control. (pinto2024bloodphenylalaninelevels pages 2-3)
* **Maternal PKU prevention:** pregnancy target Phe 120–360 µmol/L per European guidelines. (spronsen2017keyeuropeanguidelines pages 4-5)

---

## 14. Other species / natural disease
Not addressed in the retrieved evidence.

---

## 15. Model organisms
A 2024 gene-therapy review notes that murine models replicate key aspects of human pathology and are extensively used for liver-directed gene therapy proof-of-principle, including multiple vector/editing approaches; a classic model referenced is the homozygous **enu2/2 mouse**. (martinez2024state‐of‐the‐art2023on pages 10-12)

---

## Recent developments (prioritizing 2023–2024)
1. **Guideline/practice update for pegvaliase nutrition management** (Jun 2023) with implementation toolkits for initiation, monitoring, and special populations. URL: https://doi.org/10.1186/s13023-023-02751-0 (cunningham2023nutritionmanagementof pages 1-2)
2. **Delphi expert consensus (Sep 2023)** highlighting limitations/burden of lifelong diet therapy in adults and recommending pharmacologic options when available. URL: https://doi.org/10.3390/nu15183940 (rocha2023expertconsensuson pages 4-5)
3. **Large multi-centre real-world European dataset (Jun 2024)** quantifying age-associated deterioration in metabolic control and association of monitoring frequency with control. URL: https://doi.org/10.3390/nu16132064 (pinto2024bloodphenylalaninelevels pages 2-3)
4. **Gene therapy state-of-the-art (Aug 2024)** summarizing AAV, lentiviral, and nonviral/LNP mRNA approaches and the translational barriers. URL: https://doi.org/10.1002/jimd.12651 (martinez2024state‐of‐the‐art2023on pages 1-3)

---

## Data gaps vs requested template
Several template elements could not be completed from the currently retrieved texts, notably: MONDO/MeSH/Orphanet/ICD identifiers; prevalence/incidence and carrier frequencies; detailed PAH variant spectra with ClinVar/gnomAD frequencies; modifier genes/epigenetics; comprehensive organ-system comorbidity statistics from the 2024 somatic comorbidity SLR (full numeric extraction was not available in the retrieved snippets); and detailed cross-species natural disease information. Where these items are essential for a knowledge base entry, direct database retrieval (Orphanet/MONDO/MeSH/ICD; ClinVar; gnomAD; registry epidemiology sources) and full-text extraction of the SLR’s included primary studies would be required. (whitehall2024systematicliteraturereview pages 49-49)


References

1. (pinto2024bloodphenylalaninelevels pages 2-3): Alex Pinto, Kirsten Ahring, Manuela Ferreira Almeida, Catherine Ashmore, Amaya Bélanger-Quintana, Alberto Burlina, Turgay Coşkun, Anne Daly, Esther van Dam, Ali Dursun, Sharon Evans, François Feillet, Maria Giżewska, Hulya Gökmen-Özel, Mary Hickson, Yteke Hoekstra, Fatma Ilgaz, Richard Jackson, Alicja Leśniak, Christian Loro, Katarzyna Malicka, Michał Patalan, Júlio César Rocha, Serap Sivri, Iris Rodenburg, Francjan van Spronsen, Kamilla Strączek, Ayşegül Tokatli, and Anita MacDonald. Blood phenylalanine levels in patients with phenylketonuria from europe between 2012 and 2018: is it a changing landscape? Nutrients, 16:2064, Jun 2024. URL: https://doi.org/10.3390/nu16132064, doi:10.3390/nu16132064. This article has 14 citations.

2. (spronsen2017keyeuropeanguidelines pages 1-1): Francjan J van Spronsen, Annemiek MJ van Wegberg, Kirsten Ahring, Amaya Bélanger-Quintana, Nenad Blau, Annet M Bosch, Alberto Burlina, Jaime Campistol, Francois Feillet, Maria Giżewska, Stephan C Huijbregts, Shauna Kearney, Vincenzo Leuzzi, Francois Maillot, Ania C Muntau, Fritz K Trefz, Margreet van Rijn, John H Walter, and Anita MacDonald. Key european guidelines for the diagnosis and management of patients with phenylketonuria. The Lancet Diabetes &amp; Endocrinology, 5:743-756, Sep 2017. URL: https://doi.org/10.1016/s2213-8587(16)30320-5, doi:10.1016/s2213-8587(16)30320-5. This article has 551 citations and is from a highest quality peer-reviewed journal.

3. (martinez2024state‐of‐the‐art2023on pages 1-3): Michael Martinez, Cary O. Harding, Gerald Schwank, and Beat Thöny. State‐of‐the‐art 2023 on gene therapy for phenylketonuria. Journal of Inherited Metabolic Disease, 47:80-92, Aug 2024. URL: https://doi.org/10.1002/jimd.12651, doi:10.1002/jimd.12651. This article has 43 citations and is from a peer-reviewed journal.

4. (cunningham2023nutritionmanagementof pages 1-2): Amy Cunningham, Fran Rohr, Patricia Splett, Shideh Mofidi, Heather Bausell, Adrya Stembridge, Aileen Kenneson, and Rani H. Singh. Nutrition management of pku with pegvaliase therapy: update of the web-based pku nutrition management guideline recommendations. Orphanet Journal of Rare Diseases, Jun 2023. URL: https://doi.org/10.1186/s13023-023-02751-0, doi:10.1186/s13023-023-02751-0. This article has 32 citations and is from a peer-reviewed journal.

5. (maissenabgottspon2023healthrelatedqualityof pages 1-2): Stephanie Maissen-Abgottspon, Raphaela Muri, Michel Hochuli, Péter Reismann, András Gellért Barta, Ismail Mucahit Alptekin, Álvaro Hermida-Ameijeiras, Alessandro P. Burlina, Alberto B. Burlina, Chiara Cazzorla, Jessica Carretta, Roman Trepp, and Regula Everts. Health-related quality of life in a european sample of adults with early-treated classical pku. Orphanet Journal of Rare Diseases, Sep 2023. URL: https://doi.org/10.1186/s13023-023-02917-w, doi:10.1186/s13023-023-02917-w. This article has 14 citations and is from a peer-reviewed journal.

6. (spronsen2017keyeuropeanguidelines pages 4-5): Francjan J van Spronsen, Annemiek MJ van Wegberg, Kirsten Ahring, Amaya Bélanger-Quintana, Nenad Blau, Annet M Bosch, Alberto Burlina, Jaime Campistol, Francois Feillet, Maria Giżewska, Stephan C Huijbregts, Shauna Kearney, Vincenzo Leuzzi, Francois Maillot, Ania C Muntau, Fritz K Trefz, Margreet van Rijn, John H Walter, and Anita MacDonald. Key european guidelines for the diagnosis and management of patients with phenylketonuria. The Lancet Diabetes &amp; Endocrinology, 5:743-756, Sep 2017. URL: https://doi.org/10.1016/s2213-8587(16)30320-5, doi:10.1016/s2213-8587(16)30320-5. This article has 551 citations and is from a highest quality peer-reviewed journal.

7. (rocha2023expertconsensuson pages 1-2): Júlio César Rocha, Kirsten K. Ahring, Heather Bausell, Deborah A. Bilder, Cary O. Harding, Anita Inwood, Nicola Longo, Ania C. Muntau, André L. Santos Pessoa, Fran Rohr, Serap Sivri, and Álvaro Hermida. Expert consensus on the long-term effectiveness of medical nutrition therapy and its impact on the outcomes of adults with phenylketonuria. Nutrients, 15:3940, Sep 2023. URL: https://doi.org/10.3390/nu15183940, doi:10.3390/nu15183940. This article has 15 citations.

8. (rocha2023expertconsensuson pages 4-5): Júlio César Rocha, Kirsten K. Ahring, Heather Bausell, Deborah A. Bilder, Cary O. Harding, Anita Inwood, Nicola Longo, Ania C. Muntau, André L. Santos Pessoa, Fran Rohr, Serap Sivri, and Álvaro Hermida. Expert consensus on the long-term effectiveness of medical nutrition therapy and its impact on the outcomes of adults with phenylketonuria. Nutrients, 15:3940, Sep 2023. URL: https://doi.org/10.3390/nu15183940, doi:10.3390/nu15183940. This article has 15 citations.

9. (martinez2024state‐of‐the‐art2023on pages 10-12): Michael Martinez, Cary O. Harding, Gerald Schwank, and Beat Thöny. State‐of‐the‐art 2023 on gene therapy for phenylketonuria. Journal of Inherited Metabolic Disease, 47:80-92, Aug 2024. URL: https://doi.org/10.1002/jimd.12651, doi:10.1002/jimd.12651. This article has 43 citations and is from a peer-reviewed journal.

10. (hofman2018dietaryadherencein pages 41-45): DL Hofman. Dietary adherence in phenylketonuria (pku) and effects on cognitive function and quality of life. Unknown journal, 2018.

11. (alfadhel2024firstsuccessfuloutcomes pages 1-2): Majid Alfadhel and Rayyan Albarakati. First successful outcomes of pegvaliase (palynziq) in children. BMC Medical Genomics, Mar 2024. URL: https://doi.org/10.1186/s12920-024-01847-1, doi:10.1186/s12920-024-01847-1. This article has 3 citations and is from a peer-reviewed journal.

12. (yu2025advancinggenetherapy pages 2-4): In-sun Yu and Jaemin Jeong. Advancing gene therapy for phenylketonuria: from precision editing to clinical translation. International Journal of Molecular Sciences, 26:8722, Sep 2025. URL: https://doi.org/10.3390/ijms26178722, doi:10.3390/ijms26178722. This article has 3 citations.

13. (longo2018longtermsafetyand pages 1-2): Nicola Longo, Roberto Zori, Melissa P. Wasserstein, Jerry Vockley, Barbara K. Burton, Celeste Decker, Mingjin Li, Kelly Lau, Joy Jiang, Kevin Larimore, and Janet A. Thomas. Long-term safety and efficacy of pegvaliase for the treatment of phenylketonuria in adults: combined phase 2 outcomes through pal-003 extension study. Orphanet Journal of Rare Diseases, Jul 2018. URL: https://doi.org/10.1186/s13023-018-0858-7, doi:10.1186/s13023-018-0858-7. This article has 37 citations and is from a peer-reviewed journal.

14. (NCT06971731 chunk 1):  A Study to Evaluate the Safety and Efficacy of JNT-517 in Participants With Phenylketonuria (PKU). Otsuka Pharmaceutical Development & Commercialization, Inc.. 2025. ClinicalTrials.gov Identifier: NCT06971731

15. (NCT06637514 chunk 1):  A Phase 2 Study of JNT-517 in Adolescent Participants With Phenylketonuria. Otsuka Pharmaceutical Development & Commercialization, Inc.. 2025. ClinicalTrials.gov Identifier: NCT06637514

16. (NCT05781399 chunk 2):  First-in-Human, Multiple Part Clinical Study of JNT-517 in Healthy Participants and in Participants With Phenylketonuria. Otsuka Pharmaceutical Development & Commercialization, Inc.. 2022. ClinicalTrials.gov Identifier: NCT05781399

17. (NCT06628128 chunk 1):  A Study to Evaluate the Long-Term Safety and Efficacy of JNT-517 in Participants With Phenylketonuria. Otsuka Pharmaceutical Development & Commercialization, Inc.. 2025. ClinicalTrials.gov Identifier: NCT06628128

18. (NCT04480567 chunk 1):  AAV Gene Therapy Study for Subjects with PKU. BioMarin Pharmaceutical. 2020. ClinicalTrials.gov Identifier: NCT04480567

19. (yu2025advancinggenetherapy pages 11-12): In-sun Yu and Jaemin Jeong. Advancing gene therapy for phenylketonuria: from precision editing to clinical translation. International Journal of Molecular Sciences, 26:8722, Sep 2025. URL: https://doi.org/10.3390/ijms26178722, doi:10.3390/ijms26178722. This article has 3 citations.

20. (whitehall2024systematicliteraturereview pages 49-49): Kaleigh B. Whitehall, Sarah Rose, Gillian E. Clague, Kirsten K. Ahring, Deborah A. Bilder, Cary O. Harding, Álvaro Hermida, Anita Inwood, Nicola Longo, François Maillot, Ania C. Muntau, André L. S. Pessoa, Júlio C. Rocha, Fran Rohr, Serap Sivri, Jack Said, Sheun Oshinbolu, and Gillian C. Sibbring. Systematic literature review of the somatic comorbidities experienced by adults with phenylketonuria. Orphanet Journal of Rare Diseases, Aug 2024. URL: https://doi.org/10.1186/s13023-024-03203-z, doi:10.1186/s13023-024-03203-z. This article has 12 citations and is from a peer-reviewed journal.
