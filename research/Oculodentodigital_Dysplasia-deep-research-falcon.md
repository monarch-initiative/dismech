---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T12:42:52.262661'
end_time: '2026-04-04T12:51:36.510634'
duration_seconds: 524.25
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Oculodentodigital Dysplasia
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Oculodentodigital Dysplasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Oculodentodigital Dysplasia** covering all of the
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
- **Disease Name:** Oculodentodigital Dysplasia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Oculodentodigital Dysplasia** covering all of the
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


# Oculodentodigital Dysplasia (ODDD) — Comprehensive Disease Characteristics Report

## Executive summary
Oculodentodigital dysplasia (ODDD) is a rare, predominantly autosomal dominant, pleiotropic developmental disorder characterized by a core triad of ocular, dental, and digital anomalies and caused most commonly by pathogenic variants in **GJA1**, encoding **connexin 43 (Cx43)**, a gap-junction/hemichannel protein essential for intercellular communication. (hindu2023oculodentodigitaldysplasiaa pages 8-8, paznekas2003connexin43(gja1) pages 1-3)

A major 2009 genotype–phenotype synthesis of 54 genotyped families (177 affected individuals) quantified high but variable involvement of facial (92% of families), ocular (68%), dental (70%), and digital (80%) features and documented neurologic manifestations in ~30% of families. (paznekas2009gja1mutationsvariants pages 5-6)

Recent research has refined mechanistic understanding by solving a high-resolution cryo-EM structure of human Cx43 in a **putative closed state** (2023) and by describing additional CNS-heavy phenotypes including **mosaic de novo GJA1** variants with delayed myelination and seizures (2024), emphasizing allelic and tissue-mosaic effects. (qi2023structureofthe pages 1-2, shimomura2024raremosaicvariant pages 1-2)

---

## 1. Disease information
### 1.1 Definition/overview
ODDD is a congenital/early-onset multisystem disorder involving craniofacial, ocular, dental, and limb development with variable neurologic involvement. A defining description in the recent dental literature is that: **“ODDD is an autosomal dominant genetic disorder, which is characterized by abnormal ocular, dental, and digital findings. It is caused by a mutation in GJA1 gene encoding Cx43.”** (BDJ Open, 2023) (hindu2023oculodentodigitaldysplasiaa pages 8-8).

A foundational genetics paper identified ODDD as a highly penetrant autosomal dominant disorder and reported the synonym **“oculodentoosseous dysplasia”**. (paznekas2003connexin43(gja1) pages 1-3)

### 1.2 Key identifiers (from retrieved evidence)
- **MONDO:** **MONDO_0008111** (Open Targets disease entry) (kumar2020oculodentodigitaldysplasiaa pages 1-2)
- **OMIM/MIM:** **164200** (explicitly stated in multiple sources) (paznekas2003connexin43(gja1) pages 1-3, kumar2020oculodentodigitaldysplasiaa pages 1-2)
- **Orphanet / MeSH / ICD-10 / ICD-11:** not found in the retrieved evidence corpus for this run (gap noted).

### 1.3 Synonyms/alternative names
- Oculo-dento-digital dysplasia / oculodentodigital dysplasia / oculodentodigital syndrome (hindu2023oculodentodigitaldysplasiaa pages 8-8, kumar2020oculodentodigitaldysplasiaa pages 1-2)
- **Oculodentoosseous dysplasia** (synonym stated in Paznekas 2003) (paznekas2003connexin43(gja1) pages 1-3)

### 1.4 Evidence source types in this report
- Human clinical genetics / family studies and case series (paznekas2003connexin43(gja1) pages 1-3, paznekas2009gja1mutationsvariants pages 5-6, saintval2019gja1variantscause pages 2-4)
- Systematic reviews of published cases (ocular-focused) (kumar2020oculodentodigitaldysplasiaa pages 2-3)
- Dental case reports + systematic dental literature synthesis (hindu2023oculodentodigitaldysplasiaa pages 1-3)
- Model organism (mouse) disease models (flenniken2005agja1missense pages 4-5, tong2009oogenesisdefectsin pages 1-2)
- Structural biology and mechanistic reviews (qi2023structureofthe pages 1-2, leybaert2023connexinhemichannelsas pages 1-2)

---

## 2. Etiology
### 2.1 Primary causal factors
**Genetic:** Pathogenic variants in **GJA1** (connexin 43) are the established primary cause of ODDD. In a 17-family cohort, investigators reported: **“we found mutations in 100% of the individuals studied who were affected with ODDD.”** (AJHG, 2003; DOI: https://doi.org/10.1086/346090) (paznekas2003connexin43(gja1) pages 3-4).

### 2.2 Risk factors
- **Genetic risk:** carrying a pathogenic **GJA1** variant (most often heterozygous, autosomal dominant). (paznekas2009gja1mutationsvariants pages 5-6, kumar2020oculodentodigitaldysplasiaa pages 1-2)
- **De novo variants:** a substantial fraction of cases are sporadic; in the 54-family dataset, 39% were sporadic. (paznekas2009gja1mutationsvariants pages 5-6)

**Environmental risk factors:** not identified in retrieved evidence (ODDD is primarily Mendelian). 

### 2.3 Protective factors
No protective genetic or environmental factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
Not identified in retrieved evidence.

---

## 3. Phenotypes (clinical features)
ODDD shows high variability (variable expressivity; some features absent in subsets of families), but commonly involves multiple systems.

### 3.1 Core craniofacial/face phenotype
- Characteristic ODDD facies reported in 92% of families in a 54-family series. (paznekas2009gja1mutationsvariants pages 5-6)
- Examples include a thin/narrow nose with hypoplastic alae and prominent columella. (kumar2020oculodentodigitaldysplasiaa pages 1-2, paznekas2009gja1mutationsvariants pages 5-6)

**Suggested HPO terms (non-exhaustive):**
- Narrow nose (HP:0003196)
- Hypoplastic alae nasi (HP:0000430)
- Prominent columella (HP:0009924)

### 3.2 Ocular phenotypes
**Frequency/statistics:**
- In the 54-family synthesis: ocular (microphthalmia and/or microcornea) in **68% of families**; among 177 individuals, microphthalmia 22% and microcornea 27%. (paznekas2009gja1mutationsvariants pages 5-6)
- In an ocular-focused review of **295 reported cases**: the most common eye findings across mutations were **microcornea (n=111)**, **microphthalmia (n=110)**, **short palpebral fissures (n=56)**, and **glaucoma (n=51)**. (Kumar 2020; published Apr 2020; DOI: https://doi.org/10.1155/2020/6535974) (kumar2020oculodentodigitaldysplasiaa pages 2-3)

**Suggested HPO terms:**
- Microcornea (HP:0000482)
- Microphthalmia (HP:0000568)
- Short palpebral fissures (HP:0012745)
- Glaucoma (HP:0000501)

**QoL impact:** glaucoma may cause severe visual impairment/blindness in a subset (glaucoma-related blindness noted in several individuals). (paznekas2009gja1mutationsvariants pages 5-6)

### 3.3 Dental/oral phenotypes
**Frequency/statistics:**
- In the 54-family synthesis: dental anomalies present in **70% of families**; among 177 individuals enamel hypoplasia **40%** and microdontia **21%**. (paznekas2009gja1mutationsvariants pages 5-6)
- A 2023 dental systematic analysis summarized “common dental findings” including **enamel hypoplasia/hypomineralization, microdontia, pulp stones, curved roots, and taurodontism** and reports pooled frequencies from prior literature such as hypoplastic enamel ~40% and microdontia 21%. (Hindu & Umer 2023; BDJ Open; DOI: https://doi.org/10.1038/s41405-023-00139-7) (hindu2023oculodentodigitaldysplasiaa pages 1-3)

**Suggested HPO terms:**
- Enamel hypoplasia (HP:0006297)
- Microdontia (HP:0000691)
- Hypodontia (HP:0000668)
- Pulp stones (HP:0000706) (term availability may vary; include as dental pulp calcification)
- Taurodontia (HP:0000679)
- Dental caries (HP:0000670)

**QoL impact:** tooth pain, pulpitis, abscesses, and early tooth loss affect mastication and psychosocial well-being; dental care aims explicitly include maintaining function and esthetics. (hindu2023oculodentodigitaldysplasiaa pages 8-9)

### 3.4 Digital/limb phenotypes
**Frequency/statistics:**
- In the 54-family synthesis: digital (syndactyly of 4th/5th fingers) present in **80% of families** and **72% of 177 individuals**, with **43%** showing bilateral 4–5 syndactyly. (paznekas2009gja1mutationsvariants pages 5-6)

**Suggested HPO terms:**
- 4-5 finger syndactyly (HP:0006101)
- Syndactyly (HP:0001159)
- Camptodactyly (HP:0012385)
- Clinodactyly (HP:0030084)

### 3.5 Neurologic/CNS phenotypes
Neurologic manifestations are prominent in a subset and may emerge later (often adolescence/adulthood in spastic paraplegia presentations).

- In the 54-family synthesis: neurologic manifestations present in **~30% of families**, with urinary incontinence **12%**, bowel incontinence **2%**, and abnormal MRI findings **6%** among 177 individuals. (paznekas2009gja1mutationsvariants pages 7-8, paznekas2009gja1mutationsvariants pages 5-6)
- A neuroradiology series of 8 patients with GJA1 variants presenting with hereditary spastic paraplegia reported brain MRI findings consistent with hypomyelination and basal ganglia abnormalities; onset ranged from **14–50 years** and disability stages ranged **1–6**. (Saint-Val 2019; AJNR; DOI: https://doi.org/10.3174/ajnr.a6036) (saintval2019gja1variantscause pages 2-4)
- A 2024 report highlights mosaic de novo GJA1 (p.P88L) with severe neurodevelopmental delay, seizures, and delayed myelination, and notes mosaicism may explain mild limb anomalies but severe CNS disease. (Shimomura 2024; Human Genome Variation; DOI: https://doi.org/10.1038/s41439-023-00262-9) (shimomura2024raremosaicvariant pages 1-2)

**Suggested HPO terms:**
- Spastic paraplegia (HP:0001258)
- Hyperreflexia (HP:0001347)
- Seizures (HP:0001250)
- Hypomyelination (HP:0003429)
- Neurogenic bladder (HP:0000011)

---

## 4. Genetic / molecular information
### 4.1 Causal gene(s)
- **GJA1** (HGNC symbol: GJA1) encodes **connexin 43 (Cx43)**, a gap junction/hemichannel protein central to ODDD pathogenesis. (hindu2023oculodentodigitaldysplasiaa pages 8-8, paznekas2003connexin43(gja1) pages 1-3)

### 4.2 Pathogenic variant spectrum (high-level)
- In a major 2020 review of 295 cases, 73 distinct GJA1 mutations were reported across 165 molecularly confirmed individuals; the most frequent were **p.R202H (11%)**, **p.I130T (10%)**, **p.A40V (10%)**. (kumar2020oculodentodigitaldysplasiaa pages 2-3)
- The 2009 synthesis reported **48 different Cx43 mutations** across 54 families. (paznekas2009gja1mutationsvariants pages 5-6)

**Variant classes and functional consequences:**
- Missense variants dominate reported disease-causing changes; additional frameshift/truncating variants are rarer. (choi2018oculodentodigitaldysplasiawith pages 4-5)
- Functional effects are heterogeneous and can include reduced junctional conductance, altered localization/trafficking, dominant-negative effects, and altered hemichannel vs gap junction behavior. (paznekas2009gja1mutationsvariants pages 7-8, flenniken2005agja1missense pages 9-10)

**Somatic vs germline:**
- Most reported ODDD is germline heterozygous; mosaic pathogenic variants can cause atypical/severe neurodevelopmental phenotypes. (shimomura2024raremosaicvariant pages 1-2)

**Population frequency:**
- A C-terminal variant A253V was noted as present at ~1–2% in Europeans in the 2009 discussion, illustrating that not all protein-altering variants are necessarily pathogenic. (paznekas2009gja1mutationsvariants pages 4-5)

### 4.3 Modifier genes / genetic modifiers
Direct modifier genes are not established in the retrieved evidence, but the 2009 synthesis emphasizes that variability may reflect regulatory/noncoding variation and modifier effects; it discusses SNPs and possible modifying alleles. (paznekas2009gja1mutationsvariants pages 7-8)

### 4.4 Epigenetics / chromosomal abnormalities
Not identified in retrieved evidence.

---

## 5. Environmental information
No specific environmental, lifestyle, or infectious contributors were identified in the retrieved evidence; ODDD is primarily a Mendelian disorder driven by GJA1 variants. (paznekas2003connexin43(gja1) pages 1-3, paznekas2009gja1mutationsvariants pages 5-6)

---

## 6. Mechanism / pathophysiology
### 6.1 Key concept definitions (current understanding)
- **Gap junction channel:** intercellular channel formed by docking of two connexin hemichannels, enabling direct diffusion of ions and small metabolites.
- **Hemichannel:** undocked connexin hexamer at the plasma membrane that can open under pathological conditions and allow solute exchange with extracellular space.

ODDD is best conceptualized as a **Cx43 connexinopathy/channelopathy** in which tissue-specific disruption of gap junctional intercellular communication (and/or aberrant hemichannel activity) perturbs development and maintenance of ocular structures, dentition, digits, and sometimes CNS myelin/basal ganglia integrity. (bock2013neurologicalmanifestationsof pages 1-2, flenniken2005agja1missense pages 9-10)

### 6.2 Causal chain (representative, multi-tissue)
1. **Trigger:** germline (or mosaic) pathogenic variant in **GJA1** → mutant Cx43 protein. (paznekas2003connexin43(gja1) pages 3-4, shimomura2024raremosaicvariant pages 1-2)
2. **Molecular dysfunction:** altered Cx43 assembly/trafficking/docking and reduced or abnormal permeability of gap junction channels; some mutants act **dominant-negative**, reducing functional channel formation below haploinsufficiency expectations. (flenniken2005agja1missense pages 9-10, tong2009oogenesisdefectsin pages 1-2)
3. **Cellular consequence:** impaired intercellular coupling and altered signaling homeostasis in critical developmental cell populations (e.g., craniofacial mesenchyme, odontogenic tissues, ocular anterior segment tissues; astrocyte networks and astrocyte–oligodendrocyte coupling in CNS). (bock2013neurologicalmanifestationsof pages 1-2, saintval2019gja1variantscause pages 2-4)
4. **Tissue/organ pathology:** developmental anomalies (microcornea/microphthalmia; enamel hypoplasia; syndactyly) and in some individuals progressive neurologic involvement with spastic paraplegia and imaging patterns of hypomyelination and basal ganglia abnormalities. (paznekas2009gja1mutationsvariants pages 5-6, saintval2019gja1variantscause pages 2-4)

### 6.3 CNS-specific mechanistic interpretation
Cx43 is emphasized as an astrocytic gap junction protein involved in coordinated Ca2+ waves, K+ buffering, and glucose distribution; hemichannels can release signaling molecules and contribute to neuroglial inflammation. A mechanistic review frames ODDD neurologic disease as potentially arising from altered Cx43 gap junction/hemichannel function in glia, though links from specific channel defects to symptoms remain incompletely resolved. (bock2013neurologicalmanifestationsof pages 1-2)

### 6.4 Recent developments (2023–2024): structural and mechanistic advances
**High-resolution Cx43 structure (2023):** A major advance was the cryo-EM structure of human Cx43 gap junction channels at **2.26 Å**, capturing a **putative closed state**, revealing lipid-like densities in the pore and a cytosolic gating conformation involving the N-terminal domain and TM2. (Qi et al., eLife, Aug 2023; DOI: https://doi.org/10.7554/elife.87616.3) (qi2023structureofthe pages 1-2, qi2023structureofthe pages 2-4)

This structural work explicitly maps ODDD-linked mutations and suggests lipid binding may influence gating: **“binding of a lipid could directly influence the conformation of the gating elements of the protein (such as NTD)”** and notes ODDD mutations in the extracellular domain. (qi2023structureofthe pages 9-11)

**Therapeutic targeting concept (2023):** In cardiovascular contexts, selective inhibition of Cx43 hemichannels without blocking gap junctions (e.g., Gap19 peptide) is discussed as enabling a “double-edged” approach: preventing pathological hemichannel opening while preserving gap junctional function—conceptually relevant for connexinopathies even though disease-specific evidence in ODDD remains limited. (Leybaert et al., JCI, Mar 2023; DOI: https://doi.org/10.1172/jci168117) (leybaert2023connexinhemichannelsas pages 1-2)

**Phenotypic expansion / mosaicism (2024):** Mosaic de novo GJA1 variants can yield disproportionate CNS involvement (seizures, delayed myelination) with only mild limb features, suggesting tissue mosaic ratios can shape phenotype severity. (shimomura2024raremosaicvariant pages 1-2)

### 6.5 Suggested ontology terms for mechanisms
**GO Biological Process (suggestions):**
- Gap junction assembly (GO:1902723)
- Cell–cell communication (GO:0007154)
- Regulation of membrane permeability (GO:0043269)
- Myelination (GO:0042552)

**CL cell types (suggestions):**
- Astrocyte (CL:0000127) (supported mechanistically by astroglial Cx43 emphasis) (bock2013neurologicalmanifestationsof pages 1-2)
- Oligodendrocyte (CL:0000128) (astrocyte–oligodendrocyte coupling implicated in hypomyelination) (saintval2019gja1variantscause pages 2-4)
- Odontoblast (CL:0000031) / ameloblast (CL:0000138) (as relevant dental cell types; direct evidence not detailed in retrieved texts)

---

## 7. Anatomical structures affected
### 7.1 Organ level / systems
Primary systems repeatedly affected include:
- Eye/anterior segment and globe development (microcornea, microphthalmia, glaucoma). (kumar2020oculodentodigitaldysplasiaa pages 2-3, paznekas2009gja1mutationsvariants pages 5-6)
- Teeth and oral cavity (enamel hypoplasia, microdontia, caries, taurodontism). (hindu2023oculodentodigitaldysplasiaa pages 1-3)
- Hands/feet digits (4–5 syndactyly). (paznekas2009gja1mutationsvariants pages 5-6)
- CNS white matter and basal ganglia in neurologically affected patients (hypomyelination; calcifications). (saintval2019gja1variantscause pages 2-4, shimomura2024raremosaicvariant pages 1-2)

**Suggested UBERON terms (examples):**
- Eye (UBERON:0000970)
- Tooth (UBERON:0001091)
- Hand (UBERON:0002389) / digit (UBERON:0002544)
- Cerebral white matter (UBERON:0002312)
- Basal ganglion (UBERON:0002435)

---

## 8. Temporal development
### 8.1 Onset
- Many craniofacial/digital/dental anomalies are congenital or evident in childhood. (kumar2020oculodentodigitaldysplasiaa pages 1-2, paznekas2009gja1mutationsvariants pages 5-6)
- Neurologic manifestations may present later; the 8-patient spastic paraplegia series reported onset from adolescence to adulthood (14–50 years). (saintval2019gja1variantscause pages 2-4)

### 8.2 Progression
- Neurologic manifestations can be progressive, with variable disability and imaging patterns suggesting neurodegenerative involvement of myelin and basal ganglia. (saintval2019gja1variantscause pages 1-2, saintval2019gja1variantscause pages 2-4)

---

## 9. Inheritance and population
### 9.1 Inheritance
- Predominantly **autosomal dominant**; both familial and de novo/sporadic cases are common; rare **autosomal recessive** families reported. (paznekas2009gja1mutationsvariants pages 5-6, kumar2020oculodentodigitaldysplasiaa pages 1-2)

### 9.2 Penetrance / expressivity
- High penetrance is described in foundational reports, but with substantial intra- and interfamilial variability across organ systems. (paznekas2003connexin43(gja1) pages 1-3, park2017oculodentodigitaldysplasiapresenting pages 3-4)
- In the 54-family dataset, 22% of families lacked ocular abnormalities and 15% lacked abnormal dentition, illustrating variable expressivity. (paznekas2009gja1mutationsvariants pages 5-6)

### 9.3 Epidemiology
- A movement-disorders case review reports prevalence **“less than 1/1,000,000.”** (park2017oculodentodigitaldysplasiapresenting pages 3-4)
- A 2020 ocular review identified 295 reported cases in 91 publications (1963–2019), consistent with extreme rarity and publication-based ascertainment. (kumar2020oculodentodigitaldysplasiaa pages 2-3)

---

## 10. Diagnostics
### 10.1 Clinical recognition
Diagnosis is typically suspected based on the combined ocular–dental–digital phenotype and characteristic facial features and/or neurologic features. (paznekas2009gja1mutationsvariants pages 5-6, kumar2020oculodentodigitaldysplasiaa pages 1-2)

### 10.2 Genetic testing (current real-world implementation)
- **Single-gene testing / targeted sequencing of GJA1** is a common confirmatory approach; an ocular case report used targeted sequencing of **GJA1** plus array CGH to assess copy-number changes. (kumar2020oculodentodigitaldysplasiaa pages 1-2)
- **Targeted gene panels** are useful when differential diagnoses are broad; authors emphasize that “targeted gene panel sequencing” can assist in differentiating ODDD from overlapping syndromes with similar craniofacial/dental features. (choi2018oculodentodigitaldysplasiawith pages 5-6)

### 10.3 Differential diagnosis
Differential diagnoses noted in the clinical genetics/dental literature include amelogenesis imperfecta, oral-facial-digital syndrome, Hallermann–Streiff syndrome, and Saethre–Chotzen syndrome; the presence of syndactyly and typical facial gestalt can support ODDD. (choi2018oculodentodigitaldysplasiawith pages 4-5, hindu2023oculodentodigitaldysplasiaa pages 8-8)

### 10.4 Biomarkers / imaging
No validated circulating biomarkers were identified in the retrieved evidence; imaging is relevant mainly for ocular evaluation (glaucoma/anterior segment) and for neurologic phenotypes where MRI can show hypomyelination and basal ganglia signal changes/calcifications. (saintval2019gja1variantscause pages 2-4, shimomura2024raremosaicvariant pages 1-2)

---

## 11. Outcome / prognosis
Evidence in the retrieved set suggests prognosis is dominated by: 
- **Visual outcomes** (risk of glaucoma and potential blindness in a minority) (paznekas2009gja1mutationsvariants pages 5-6)
- **Dental morbidity** (caries, tooth wear, abscesses; need for lifelong preventive care) (hindu2023oculodentodigitaldysplasiaa pages 8-9)
- **Neurologic disability** (variable severity; spastic paraplegia disability staging reported in neurologic series) (saintval2019gja1variantscause pages 2-4)

Quantitative survival/life expectancy data were not identified in the retrieved evidence.

---

## 12. Treatment
No disease-modifying pharmacotherapy is established for ODDD in the retrieved evidence; management is multidisciplinary and supportive.

### 12.1 Dental management (real-world implementation)
Dental care recommendations from a 2023 systematic analysis emphasize immediate treatment of active oral disease and longer-term prevention of tooth wear and maintenance of occlusion. (hindu2023oculodentodigitaldysplasiaa pages 1-3)

Specific interventions compiled from published cases include:
- Sealants and early restoration of caries; avoidance of extractions when possible to preserve alveolar bone. (hindu2023oculodentodigitaldysplasiaa pages 8-9)
- Endodontic treatments (pulpotomy/pulpectomy, root canal therapy, apexification) and full-coverage restorations where needed. (hindu2023oculodentodigitaldysplasiaa pages 7-8)
- Regular surveillance every ~3 months in some reported dental protocols. (hindu2023oculodentodigitaldysplasiaa pages 7-8)

**Suggested MAXO terms (examples):**
- Dental restoration procedure (MAXO:0000900) (term may vary)
- Pit and fissure sealant application (MAXO:0000526) (term may vary)
- Endodontic therapy (MAXO:0000104) (term may vary)

### 12.2 Ophthalmic care
Given high frequency of microcornea/microphthalmia and non-trivial glaucoma burden, ophthalmic monitoring and glaucoma management are key practical interventions (treatment details not elaborated in retrieved excerpts). (kumar2020oculodentodigitaldysplasiaa pages 2-3)

### 12.3 Neurologic symptomatic care
Neurologic manifestations (e.g., spasticity, seizures) are treated symptomatically in practice; disease-specific controlled evidence was not identified in the retrieved corpus. (shimomura2024raremosaicvariant pages 1-2)

### 12.4 Experimental / emerging approaches
Targeted modulation of Cx43 hemichannel activity (e.g., selective inhibitors that spare gap junctions) is an active area in other diseases and provides a mechanistic rationale for future connexin-based therapies, but ODDD-specific clinical trials were not identified in the clinical-trial search results for this run. (leybaert2023connexinhemichannelsas pages 1-2)

---

## 13. Prevention
Primary prevention is not applicable in the classic public-health sense for a Mendelian disorder; prevention focuses on reproductive and familial risk management.

- **Genetic counseling and cascade testing** are strongly implied by the predominance of autosomal dominant inheritance and frequent de novo cases, but explicit guideline statements were not retrieved in this run. (paznekas2009gja1mutationsvariants pages 5-6)

---

## 14. Other species / natural disease
No naturally occurring (non-model) animal disease analogs were identified in the retrieved evidence.

---

## 15. Model organisms
### 15.1 Mouse models (key resources)
Multiple mouse models recapitulate core ODDD features and are widely used for mechanistic work:
- **Gja1Jrt/+ (Cx43 G60S)** ENU-derived dominant model recapitulating syndactyly, enamel hypoplasia, craniofacial dysmorphology, ocular anomalies, and cardiac conduction abnormalities; evidence supports a dominant-negative mechanism and reduced Cx43 plaques/levels. (Flenniken 2005; Development; DOI: https://doi.org/10.1242/dev.02011) (flenniken2005agja1missense pages 4-5, flenniken2005agja1missense pages 9-10)
- **Knock-in models (I130T, G138R)** recapitulate ODDD-like traits; reproductive and cardiac phenotypes and prenatal death effects are reported across strains. (tong2009oogenesisdefectsin pages 7-8)
- **Cx43 knockout (Gja1−/−)** demonstrates severe developmental and reproductive defects, emphasizing the essential role of Cx43-mediated coupling. (tong2009oogenesisdefectsin pages 1-2)

### 15.2 Phenotype recapitulation and limitations
The Jrt/+ model reproduces many canonical traits but does not capture all variably penetrant human symptoms, highlighting allele- and tissue-specific differences. (flenniken2005agja1missense pages 10-11)

---

## Key resource artifact
| Disease name | Abbreviation | MONDO ID | OMIM/MIM | Common synonyms | Causal gene | Inheritance | Key references (year; DOI/URL) | Evidence |
|---|---|---|---|---|---|---|---|---|
| Oculodentodigital dysplasia | ODDD | MONDO_0008111 | OMIM/MIM #164200 | oculo-dento-digital dysplasia; oculo-dento-digital syndrome; oculodentoosseous dysplasia | **GJA1** (connexin 43, Cx43) | Mostly autosomal dominant; rare autosomal recessive cases reported | Paznekas et al., 2003; https://doi.org/10.1086/346090 • Paznekas et al., 2009; https://doi.org/10.1002/humu.20958 • Kumar et al., 2020; https://doi.org/10.1155/2020/6535974 • Hindu & Umer, 2023; https://doi.org/10.1038/s41405-023-00139-7 | (paznekas2003connexin43(gja1) pages 1-3, paznekas2009gja1mutationsvariants pages 5-6, kumar2020oculodentodigitaldysplasiaa pages 1-2, hindu2023oculodentodigitaldysplasiaa pages 8-8) |
| Standard ontology/classification note | — | MONDO_0008111 | #164200 | not found in retrieved sources beyond above synonyms | **GJA1** | Autosomal dominant form most frequently reported | Open Targets disease-target association lists oculodentodigital dysplasia under MONDO_0008111 and associates **GJA1** | (kumar2020oculodentodigitaldysplasiaa pages 1-2) |
| Other identifiers | — | not found in retrieved sources | not found beyond OMIM/MIM #164200 | not found in retrieved sources | not found beyond **GJA1/Cx43** | not found beyond AD/rare AR | Orphanet, MeSH, ICD-10/ICD-11 were not explicitly retrieved in the gathered evidence | (paznekas2003connexin43(gja1) pages 1-3, kumar2020oculodentodigitaldysplasiaa pages 1-2, hindu2023oculodentodigitaldysplasiaa pages 8-8) |


*Table: This table summarizes the core disease naming and identifier information retrieved for oculodentodigital dysplasia, including supported ontology IDs, synonyms, causal gene, inheritance, and anchor references. It is useful as a compact normalization artifact for a disease knowledge base entry.*

---

## Notes on evidence gaps (important for knowledge-base curation)
- Orphanet ID, MeSH ID, ICD-10/ICD-11 codes were not present in the retrieved evidence for this run and should be added from OMIM/Orphanet/MeSH lookups in a subsequent curation step.
- Quantitative survival/life expectancy and formal clinical diagnostic criteria/guidelines were not retrieved.
- ODDD-specific clinical trials and disease-modifying therapies were not identified in the clinical trial search results for this run.



References

1. (hindu2023oculodentodigitaldysplasiaa pages 8-8): Karshma Devi Hindu and Fahad Umer. Oculo-dento-digital dysplasia: a systematic analysis of published dental literature. BDJ Open, Mar 2023. URL: https://doi.org/10.1038/s41405-023-00139-7, doi:10.1038/s41405-023-00139-7. This article has 3 citations and is from a peer-reviewed journal.

2. (paznekas2003connexin43(gja1) pages 1-3): William A. Paznekas, Simeon A. Boyadjiev, Robert E. Shapiro, Otto Daniels, Bernd Wollnik, Catherine E. Keegan, Jeffrey W. Innis, Mary Beth Dinulos, Cathy Christian, Mark C. Hannibal, and Ethylin Wang Jabs. Connexin 43 (gja1) mutations cause the pleiotropic phenotype of oculodentodigital dysplasia. American journal of human genetics, 72 2:408-18, Feb 2003. URL: https://doi.org/10.1086/346090, doi:10.1086/346090. This article has 756 citations and is from a highest quality peer-reviewed journal.

3. (paznekas2009gja1mutationsvariants pages 5-6): William A. Paznekas, Barbara Karczeski, Sascha Vermeer, R. Brian Lowry, Martin Delatycki, Faivre Laurence, Pasi A. Koivisto, Lionel Van Maldergem, Simeon A. Boyadjiev, Joann N. Bodurtha, and Ethylin Wang Jabs. Gja1 mutations, variants, and connexin 43 dysfunction as it relates to the oculodentodigital dysplasia phenotype. Human Mutation, 30:724-733, May 2009. URL: https://doi.org/10.1002/humu.20958, doi:10.1002/humu.20958. This article has 312 citations and is from a domain leading peer-reviewed journal.

4. (qi2023structureofthe pages 1-2): Chao Qi, Silvia Acosta Gutierrez, Pia Lavriha, Alaa Othman, Diego Lopez-Pigozzi, Erva Bayraktar, Dina Schuster, Paola Picotti, Nicola Zamboni, Mario Bortolozzi, Francesco Luigi Gervasio, and Volodymyr M Korkhov. Structure of the connexin-43 gap junction channel in a putative closed state. eLife, Aug 2023. URL: https://doi.org/10.7554/elife.87616.3, doi:10.7554/elife.87616.3. This article has 44 citations and is from a domain leading peer-reviewed journal.

5. (shimomura2024raremosaicvariant pages 1-2): Rina Shimomura, Tomoe Yanagishita, Kumiko Ishiguro, Minobu Shichiji, Takatoshi Sato, Keiko Shimojima Yamamoto, Miho Nagata, Yasuki Ishihara, Yohei Miyashita, Keiko Ishigaki, Satoru Nagata, Yoshihiro Asano, and Toshiyuki Yamamoto. Rare mosaic variant of gja1 in a patient with a neurodevelopmental disorder. Human Genome Variation, Jan 2024. URL: https://doi.org/10.1038/s41439-023-00262-9, doi:10.1038/s41439-023-00262-9. This article has 3 citations.

6. (kumar2020oculodentodigitaldysplasiaa pages 1-2): Virang Kumar, Natario L. Couser, and Arti Pandya. Oculodentodigital dysplasia: a case report and major review of the eye and ocular adnexa features of 295 reported cases. Case Reports in Ophthalmological Medicine, 2020:1-16, Apr 2020. URL: https://doi.org/10.1155/2020/6535974, doi:10.1155/2020/6535974. This article has 12 citations.

7. (saintval2019gja1variantscause pages 2-4): L. Saint-Val, T. Courtin, P. Charles, C. Verny, M. Catala, R. Schiffmann, O. Boespflug-Tanguy, and F. Mochel. Gja1 variants cause spastic paraplegia associated with cerebral hypomyelination. American Journal of Neuroradiology, 40:788-791, Apr 2019. URL: https://doi.org/10.3174/ajnr.a6036, doi:10.3174/ajnr.a6036. This article has 8 citations and is from a peer-reviewed journal.

8. (kumar2020oculodentodigitaldysplasiaa pages 2-3): Virang Kumar, Natario L. Couser, and Arti Pandya. Oculodentodigital dysplasia: a case report and major review of the eye and ocular adnexa features of 295 reported cases. Case Reports in Ophthalmological Medicine, 2020:1-16, Apr 2020. URL: https://doi.org/10.1155/2020/6535974, doi:10.1155/2020/6535974. This article has 12 citations.

9. (hindu2023oculodentodigitaldysplasiaa pages 1-3): Karshma Devi Hindu and Fahad Umer. Oculo-dento-digital dysplasia: a systematic analysis of published dental literature. BDJ Open, Mar 2023. URL: https://doi.org/10.1038/s41405-023-00139-7, doi:10.1038/s41405-023-00139-7. This article has 3 citations and is from a peer-reviewed journal.

10. (flenniken2005agja1missense pages 4-5): Ann M. Flenniken, Lucy R. Osborne, Nicole Anderson, Nadia Ciliberti, Craig Fleming, Joanne E. I. Gittens, Xiang-Qun Gong, Lois B. Kelsey, Crystal Lounsbury, Luisa Moreno, Brian J. Nieman, Katie Peterson, Dawei Qu, Wendi Roscoe, Qing Shao, Dan Tong, Gregory I. L. Veitch, Irina Voronina, Igor Vukobradovic, Geoffrey A. Wood, Yonghong Zhu, Ralph A. Zirngibl, Jane E. Aubin, Donglin Bai, Benoit G. Bruneau, Marc Grynpas, Janet E. Henderson, R. Mark Henkelman, Colin McKerlie, John G. Sled, William L. Stanford, Dale W. Laird, Gerald M. Kidder, S. Lee Adamson, and Janet Rossant. A gja1 missense mutation in a mouse model of oculodentodigital dysplasia. Development, 132:4375-4386, Oct 2005. URL: https://doi.org/10.1242/dev.02011, doi:10.1242/dev.02011. This article has 275 citations and is from a domain leading peer-reviewed journal.

11. (tong2009oogenesisdefectsin pages 1-2): Dan Tong, Deanne Colley, Renee Thoo, Tony Y. Li, Isabelle Plante, Dale W. Laird, Donglin Bai, and Gerald M. Kidder. Oogenesis defects in a mutant mouse model of oculodentodigital dysplasia. Disease Models & Mechanisms, 2:157-167, Mar 2009. URL: https://doi.org/10.1242/dmm.000935, doi:10.1242/dmm.000935. This article has 22 citations and is from a domain leading peer-reviewed journal.

12. (leybaert2023connexinhemichannelsas pages 1-2): Luc Leybaert, Maarten A.J. De Smet, Alessio Lissoni, Rosalie Allewaert, H. Llewelyn Roderick, Geert Bultynck, Mario Delmar, Karin R. Sipido, and Katja Witschas. Connexin hemichannels as candidate targets for cardioprotective and anti-arrhythmic treatments. The Journal of Clinical Investigation, Mar 2023. URL: https://doi.org/10.1172/jci168117, doi:10.1172/jci168117. This article has 54 citations.

13. (paznekas2003connexin43(gja1) pages 3-4): William A. Paznekas, Simeon A. Boyadjiev, Robert E. Shapiro, Otto Daniels, Bernd Wollnik, Catherine E. Keegan, Jeffrey W. Innis, Mary Beth Dinulos, Cathy Christian, Mark C. Hannibal, and Ethylin Wang Jabs. Connexin 43 (gja1) mutations cause the pleiotropic phenotype of oculodentodigital dysplasia. American journal of human genetics, 72 2:408-18, Feb 2003. URL: https://doi.org/10.1086/346090, doi:10.1086/346090. This article has 756 citations and is from a highest quality peer-reviewed journal.

14. (hindu2023oculodentodigitaldysplasiaa pages 8-9): Karshma Devi Hindu and Fahad Umer. Oculo-dento-digital dysplasia: a systematic analysis of published dental literature. BDJ Open, Mar 2023. URL: https://doi.org/10.1038/s41405-023-00139-7, doi:10.1038/s41405-023-00139-7. This article has 3 citations and is from a peer-reviewed journal.

15. (paznekas2009gja1mutationsvariants pages 7-8): William A. Paznekas, Barbara Karczeski, Sascha Vermeer, R. Brian Lowry, Martin Delatycki, Faivre Laurence, Pasi A. Koivisto, Lionel Van Maldergem, Simeon A. Boyadjiev, Joann N. Bodurtha, and Ethylin Wang Jabs. Gja1 mutations, variants, and connexin 43 dysfunction as it relates to the oculodentodigital dysplasia phenotype. Human Mutation, 30:724-733, May 2009. URL: https://doi.org/10.1002/humu.20958, doi:10.1002/humu.20958. This article has 312 citations and is from a domain leading peer-reviewed journal.

16. (choi2018oculodentodigitaldysplasiawith pages 4-5): J Choi, AramYang, A Song, M Lim, and J Kim. Oculodentodigital dysplasia with a novel mutation in gja1 diagnosed by targeted gene panel sequencing: a case report and literature review. Unknown journal, 2018.

17. (flenniken2005agja1missense pages 9-10): Ann M. Flenniken, Lucy R. Osborne, Nicole Anderson, Nadia Ciliberti, Craig Fleming, Joanne E. I. Gittens, Xiang-Qun Gong, Lois B. Kelsey, Crystal Lounsbury, Luisa Moreno, Brian J. Nieman, Katie Peterson, Dawei Qu, Wendi Roscoe, Qing Shao, Dan Tong, Gregory I. L. Veitch, Irina Voronina, Igor Vukobradovic, Geoffrey A. Wood, Yonghong Zhu, Ralph A. Zirngibl, Jane E. Aubin, Donglin Bai, Benoit G. Bruneau, Marc Grynpas, Janet E. Henderson, R. Mark Henkelman, Colin McKerlie, John G. Sled, William L. Stanford, Dale W. Laird, Gerald M. Kidder, S. Lee Adamson, and Janet Rossant. A gja1 missense mutation in a mouse model of oculodentodigital dysplasia. Development, 132:4375-4386, Oct 2005. URL: https://doi.org/10.1242/dev.02011, doi:10.1242/dev.02011. This article has 275 citations and is from a domain leading peer-reviewed journal.

18. (paznekas2009gja1mutationsvariants pages 4-5): William A. Paznekas, Barbara Karczeski, Sascha Vermeer, R. Brian Lowry, Martin Delatycki, Faivre Laurence, Pasi A. Koivisto, Lionel Van Maldergem, Simeon A. Boyadjiev, Joann N. Bodurtha, and Ethylin Wang Jabs. Gja1 mutations, variants, and connexin 43 dysfunction as it relates to the oculodentodigital dysplasia phenotype. Human Mutation, 30:724-733, May 2009. URL: https://doi.org/10.1002/humu.20958, doi:10.1002/humu.20958. This article has 312 citations and is from a domain leading peer-reviewed journal.

19. (bock2013neurologicalmanifestationsof pages 1-2): Marijke De Bock, Marianne Kerrebrouck, Nan Wang, and Luc Leybaert. Neurological manifestations of oculodentodigital dysplasia: a cx43 channelopathy of the central nervous system? Frontiers in Pharmacology, Jun 2013. URL: https://doi.org/10.3389/fphar.2013.00120, doi:10.3389/fphar.2013.00120. This article has 76 citations.

20. (qi2023structureofthe pages 2-4): Chao Qi, Silvia Acosta Gutierrez, Pia Lavriha, Alaa Othman, Diego Lopez-Pigozzi, Erva Bayraktar, Dina Schuster, Paola Picotti, Nicola Zamboni, Mario Bortolozzi, Francesco Luigi Gervasio, and Volodymyr M Korkhov. Structure of the connexin-43 gap junction channel in a putative closed state. eLife, Aug 2023. URL: https://doi.org/10.7554/elife.87616.3, doi:10.7554/elife.87616.3. This article has 44 citations and is from a domain leading peer-reviewed journal.

21. (qi2023structureofthe pages 9-11): Chao Qi, Silvia Acosta Gutierrez, Pia Lavriha, Alaa Othman, Diego Lopez-Pigozzi, Erva Bayraktar, Dina Schuster, Paola Picotti, Nicola Zamboni, Mario Bortolozzi, Francesco Luigi Gervasio, and Volodymyr M Korkhov. Structure of the connexin-43 gap junction channel in a putative closed state. eLife, Aug 2023. URL: https://doi.org/10.7554/elife.87616.3, doi:10.7554/elife.87616.3. This article has 44 citations and is from a domain leading peer-reviewed journal.

22. (saintval2019gja1variantscause pages 1-2): L. Saint-Val, T. Courtin, P. Charles, C. Verny, M. Catala, R. Schiffmann, O. Boespflug-Tanguy, and F. Mochel. Gja1 variants cause spastic paraplegia associated with cerebral hypomyelination. American Journal of Neuroradiology, 40:788-791, Apr 2019. URL: https://doi.org/10.3174/ajnr.a6036, doi:10.3174/ajnr.a6036. This article has 8 citations and is from a peer-reviewed journal.

23. (park2017oculodentodigitaldysplasiapresenting pages 3-4): Kye Won Park, Ho-Sung Ryu, Juyeon Kim, and Sun Ju Chung. Oculodentodigital dysplasia presenting as spastic paraparesis: the first genetically confirmed korean case and a literature review. Journal of Movement Disorders, 10:149-153, Sep 2017. URL: https://doi.org/10.14802/jmd.17050, doi:10.14802/jmd.17050. This article has 10 citations and is from a peer-reviewed journal.

24. (choi2018oculodentodigitaldysplasiawith pages 5-6): J Choi, AramYang, A Song, M Lim, and J Kim. Oculodentodigital dysplasia with a novel mutation in gja1 diagnosed by targeted gene panel sequencing: a case report and literature review. Unknown journal, 2018.

25. (hindu2023oculodentodigitaldysplasiaa pages 7-8): Karshma Devi Hindu and Fahad Umer. Oculo-dento-digital dysplasia: a systematic analysis of published dental literature. BDJ Open, Mar 2023. URL: https://doi.org/10.1038/s41405-023-00139-7, doi:10.1038/s41405-023-00139-7. This article has 3 citations and is from a peer-reviewed journal.

26. (tong2009oogenesisdefectsin pages 7-8): Dan Tong, Deanne Colley, Renee Thoo, Tony Y. Li, Isabelle Plante, Dale W. Laird, Donglin Bai, and Gerald M. Kidder. Oogenesis defects in a mutant mouse model of oculodentodigital dysplasia. Disease Models & Mechanisms, 2:157-167, Mar 2009. URL: https://doi.org/10.1242/dmm.000935, doi:10.1242/dmm.000935. This article has 22 citations and is from a domain leading peer-reviewed journal.

27. (flenniken2005agja1missense pages 10-11): Ann M. Flenniken, Lucy R. Osborne, Nicole Anderson, Nadia Ciliberti, Craig Fleming, Joanne E. I. Gittens, Xiang-Qun Gong, Lois B. Kelsey, Crystal Lounsbury, Luisa Moreno, Brian J. Nieman, Katie Peterson, Dawei Qu, Wendi Roscoe, Qing Shao, Dan Tong, Gregory I. L. Veitch, Irina Voronina, Igor Vukobradovic, Geoffrey A. Wood, Yonghong Zhu, Ralph A. Zirngibl, Jane E. Aubin, Donglin Bai, Benoit G. Bruneau, Marc Grynpas, Janet E. Henderson, R. Mark Henkelman, Colin McKerlie, John G. Sled, William L. Stanford, Dale W. Laird, Gerald M. Kidder, S. Lee Adamson, and Janet Rossant. A gja1 missense mutation in a mouse model of oculodentodigital dysplasia. Development, 132:4375-4386, Oct 2005. URL: https://doi.org/10.1242/dev.02011, doi:10.1242/dev.02011. This article has 275 citations and is from a domain leading peer-reviewed journal.