---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-07T11:56:30.824158'
end_time: '2026-05-07T12:26:04.443384'
duration_seconds: 1773.63
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Undetermined Early-Onset Epileptic Encephalopathy
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
- **Disease Name:** Undetermined Early-Onset Epileptic Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Undetermined Early-Onset Epileptic Encephalopathy** covering all of the
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
- **Disease Name:** Undetermined Early-Onset Epileptic Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Undetermined Early-Onset Epileptic Encephalopathy** covering all of the
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


## Disease characteristics research report: Undetermined Early-Onset Epileptic Encephalopathy (UEOEE)

### Executive summary
“Undetermined early-onset epileptic encephalopathy” is best treated as a **diagnostic state** (early-onset epileptic encephalopathy/DEE phenotype with **no causative aetiology yet identified**) rather than a single stable Mendelian disease entity. Contemporary clinical and ontology practice places such cases within the umbrella of **developmental and epileptic encephalopathies (DEEs)** and age-of-onset epilepsy syndrome groupings, while ongoing diagnostic escalation (gene panel → exome → genome ± CNV, mosaicism-aware analyses, metabolic evaluation, and reanalysis) is used to resolve aetiology over time. (scheffer2024developmentalandepileptic pages 1-4, vasilevsky2026epilepsydiseaseclassification pages 7-8, symonds2021earlychildhoodepilepsies pages 6-8)

Key quantitative anchors relevant to an “undetermined” category:
- In a population-wide Scotland cohort of epilepsies presenting <3 years, **aetiology was identified in 54%**, leaving **~46% undetermined** after extensive investigation. (symonds2021earlychildhoodepilepsies pages 1-2)
- Rapid genome sequencing in infants with seizures beginning under 1 year identified a genetic cause in **46%** (median turnaround **37 days**) with reported clinical utility in **56%**. (scheffer2024developmentalandepileptic pages 9-11)
- In a 2023 cohort of 522 children with previously unexplained pediatric-onset epilepsy, exome sequencing yielded diagnoses in **19.2%** and had documented clinical utility in **41%** of diagnosed children with follow-up. (koh2023utilityofexome pages 1-2)

### Evidence tables (for knowledge-base population)
The following curated tables summarize identifiers/ontology mappings and quantitative evidence across cohorts and testing modalities.

| Concept (as used clinically) | Notes/definition | MONDO term(s) & IDs (from evidence) | Other identifier resources mentioned | Source (citation id) |
|---|---|---|---|---|
| Undetermined Early-Onset Epileptic Encephalopathy | Best treated as a descriptive clinical label rather than a single stable disease entity; in current usage it is usually grounded in the broader DEE framework when onset is neonatal/infantile and etiology remains unresolved. | No single explicit MONDO ID identified for this exact undetermined label in the retrieved evidence; nearest framework terms are age-based and DEE superclass/grouping terms below. | None explicitly retrieved for this exact label. | (scheffer2024developmentalandepileptic pages 1-4, vasilevsky2026epilepsydiseaseclassification pages 1-2) |
| Developmental and epileptic encephalopathy (DEE) | Current umbrella concept for severe epilepsies in which developmental impairment and epileptic activity both contribute; Mondo reports this branch was renamed from “early infantile epileptic encephalopathy,” and a generic DEE superclass was created above the genetic DEE class. | Generic DEE superclass mentioned; MONDO:0100062 = **genetic developmental and epileptic encephalopathy**. | OMIM phenotypic series for genetic DEE referenced: https://www.omim.org/phenotypicSeries/PS308350 | (vasilevsky2026epilepsydiseaseclassification pages 7-8) |
| Genetic developmental and epileptic encephalopathy | Mondo relabeled MONDO:0100062 from a broader/older DEE naming pattern to specify the genetic class, acknowledging that not all DEE is hereditary and many cases are de novo. | **MONDO:0100062** genetic developmental and epileptic encephalopathy | OMIM PS308350: https://www.omim.org/phenotypicSeries/PS308350 | (vasilevsky2026epilepsydiseaseclassification pages 7-8) |
| Early-infantile DEE | ILAE-aligned age-specific DEE concept encompassing the previously defined Ohtahara syndrome and early myoclonic encephalopathy. Useful proxy for very-early-onset cases. | **MONDO:0800491** early-infantile DEE | None explicitly given beyond ILAE-alignment notes. | (vasilevsky2026epilepsydiseaseclassification pages 8-10, vasilevsky2026epilepsydiseaseclassification pages 7-8) |
| Epileptic encephalopathy, infantile or early | Older/age-focused Mondo concept relevant to infantile or early presentations; useful as a broad ontology anchor when a more specific DEE syndrome is not yet known. | **MONDO:0020627** epileptic encephalopathy, infantile or early | None mentioned. | (vasilevsky2026epilepsydiseaseclassification pages 6-7) |
| Neonatal/infantile epilepsy syndrome | Age-of-onset grouping class used by Mondo to align with ILAE; useful for categorizing unresolved early-onset encephalopathy presentations. | **MONDO:0020070** neonatal/infantile epilepsy syndrome | None mentioned. | (vasilevsky2026epilepsydiseaseclassification pages 7-8, vasilevsky2026epilepsydiseaseclassification pages 6-7) |
| Childhood-onset epilepsy syndrome | Broader age-of-onset grouping retained by Mondo; less specific for the target but part of the same ILAE-aligned hierarchy. | **MONDO:0020072** childhood-onset epilepsy syndrome | None mentioned. | (vasilevsky2026epilepsydiseaseclassification pages 7-8, vasilevsky2026epilepsydiseaseclassification pages 6-7) |
| Variable age epilepsy syndrome | Mondo grouping class for syndromes with variable age at onset; included because some DEEs span age brackets or remain unclassified initially. | **MONDO:0100619** variable age epilepsy syndrome | None mentioned. | (vasilevsky2026epilepsydiseaseclassification pages 7-8, vasilevsky2026epilepsydiseaseclassification pages 6-7) |
| Ohtahara syndrome | Historical syndrome name now treated in Mondo revision discussions as an exact synonym/constituent within early-infantile DEE rather than a wholly separate modern umbrella concept. | Linked to **MONDO:0800491** early-infantile DEE as synonym/aligned concept | None mentioned. | (vasilevsky2026epilepsydiseaseclassification pages 8-10, scheffer2024developmentalandepileptic pages 9-11) |
| Early myoclonic encephalopathy | Historical neonatal encephalopathy term proposed for merger into early-infantile DEE in Mondo revision work; relevant synonym/concept for legacy records. | **MONDO:0016022** early myoclonic encephalopathy; proposed merge into **MONDO:0800491** | None mentioned. | (vasilevsky2026epilepsydiseaseclassification pages 8-10, vasilevsky2026epilepsydiseaseclassification pages 7-8) |


*Table: This table summarizes the most useful ontology mappings and synonym relationships for interpreting the target label “Undetermined Early-Onset Epileptic Encephalopathy” within modern DEE terminology. It highlights the closest MONDO concepts and age-based groupings supported by the retrieved evidence.*

| Study (year, journal) | Population | Key findings (numbers) | URL/DOI | Evidence type |
|---|---|---|---|---|
| Symonds et al. (2021, *Brain*) | Population-wide prospective Scotland cohort; 390 children presenting with epilepsy before age 3 years | Adjusted incidence of epilepsies presenting in first 3 years: **239/100,000** live births (95% CI 216–263); aetiology identified in **54%** so ~**46% undetermined**; **31%** had genetic cause; at 24 months **36% DRE**, **49% GDD**; mortality **3%** overall and **8%** in DEE subgroup; most deprived vs least deprived incidence **301 vs 182/100,000** (OR 1.7, 95% CI 1.3–2.2) (symonds2021earlychildhoodepilepsies pages 1-2, symonds2021earlychildhoodepilepsies pages 3-6) | https://doi.org/10.1093/brain/awab162 | Human prospective population cohort |
| Symonds et al. (2021, *Brain*) | Subset without established aetiology prior to presentation (n=311; testing after presentation) | Gene panel uptake **87%**; diagnostic yield: gene panel **82/270 (30%)**, chromosomal microarray **18/216 (8%)**, brain MRI **18/267 (7%)**; trio WGS diagnosed **6 additional patients**; among unknown-aetiology group ~**180/390 (~46%)**, outcomes were **14% DRE** (25/180) and **27% GDD** (49/180) (symonds2021earlychildhoodepilepsies pages 6-8, symonds2021earlychildhoodepilepsies pages 8-9) | https://doi.org/10.1093/brain/awab162 | Human prospective cohort, diagnostic workup |
| Koh et al. (2023, *JAMA Network Open*) | 522 children with previously unexplained pediatric-onset epilepsy; mean seizure onset 1.2 years; 27% had DEE | Exome sequencing diagnostic yield **100/522 (19.2%)**; **89** SNV diagnoses, **11** CNV diagnoses; among 71 diagnosed with follow-up, documented clinical utility in **29 (41%)**; higher yield with intellectual disability (aOR **2.44**), motor impairment (aOR **2.19**), and earlier seizure onset (aOR **0.93**) (koh2023utilityofexome pages 1-2) | https://doi.org/10.1001/jamanetworkopen.2023.24380 | Human clinical sequencing cohort |
| Vetri et al. (2024, *International Journal of Molecular Sciences*) | 82 subjects with DEE characterized by early-onset drug-resistant epilepsy plus GDD and/or ID | WES detection rate **43%** (**35 pathogenic variants/82**); variants in **29 genes**; **23/35 (66%)** de novo; inheritance: **60%** autosomal dominant de novo, **17%** autosomal recessive homozygous, **11%** autosomal recessive heterozygous, **6%** parental mosaic dominant, **6%** X-linked dominant de novo; variant classes: **75%** missense, **16%** frameshift deletions, **5%** frameshift duplications, **3%** splicing (vetri2024wholeexomesequencing pages 1-2) | https://doi.org/10.3390/ijms25021146 | Human DEE WES cohort |
| Grether et al. (2023, *Molecular Genetics & Genomic Medicine*) | 20 patients with developmental or epileptic encephalopathies unsolved after prior WES and CMA; broader cohort follow-up n=63 | Trio-WGS yield in previously unsolved subgroup **4/20 (20%)**; overall diagnostic yield in broader follow-up cohort **34/63 (54%)**; authors estimated retrospective reanalysis alone could add **10%** and technical improvements ~**3%**; concluded incremental WGS benefit over contemporary WES remains limited (grether2023thecurrentbenefit pages 4-5, grether2023thecurrentbenefit pages 1-2) | https://doi.org/10.1002/mgg3.2148 | Human unsolved-case reanalysis/WGS cohort |
| Scheffer et al. (2024, *Nature Reviews Disease Primers*) | DEE review synthesizing infant/childhood-onset studies | DEEs present before age 16; ~**75%** begin under age 3; cumulative incidence up to 16 years **169/100,000** (95% CI 144–199); DEEs under age 3 in Scotland **86.1/100,000** (95% CI 72.7–101.3); ~**one-third** cannot be classified into a specific syndrome; genetic cause found in **>50%**; **>900** monogenic genes implicated (scheffer2024developmentalandepileptic pages 1-4) | https://doi.org/10.1038/s41572-024-00546-6 | Authoritative review / aggregated disease-level evidence |
| Scheffer et al. (2024, *Nature Reviews Disease Primers*) | Infants with seizure onset under 1 year summarized in DEE review | Rapid genome sequencing identified a genetic cause in **46%** of **100** infants; median turnaround **37 days** from seizure onset; clinical utility **56%**; prognostic counselling utility **86%**; elsewhere in review, genome sequencing in one infant study found a genetic cause in **43%** (scheffer2024developmentalandepileptic pages 9-11, scheffer2024developmentalandepileptic pages 11-13) | https://doi.org/10.1038/s41572-024-00546-6 | Review summarizing human rapid-genomics studies |


*Table: This table compiles the key quantitative evidence most relevant to an 'undetermined early-onset epileptic encephalopathy' entry, including incidence, undetermined etiology proportion, diagnostic yields across modalities, clinical utility, and major outcomes. It emphasizes both real-world population data and recent genomic testing studies that inform current diagnostic strategy.*

| Intervention/Approach | Target disease/gene | NCT ID | Phase | Status | Key endpoints | Key eligibility notes | Source citation id |
|---|---|---|---|---|---|---|---|
| CAP-002 gene therapy (single IV infusion) | STXBP1 encephalopathy / STXBP1-related DEE | NCT06983158 | Phase 1/2a | Suspended | Primary: safety (AEs/SAEs, labs, ECG, vitals, exams) over 2 years; Secondary: developmental, motor, communication, behavior scales and seizure frequency by caregiver diary | Pediatric participants ~18 months to <8 years; excludes prior gene therapy, recent ASO therapy, positive anti-capsid antibodies, and pathogenic non-STXBP1 variants contributing to phenotype (NCT06983158 chunk 1, NCT06983158 chunk 2) | (NCT06983158 chunk 1, NCT06983158 chunk 2) |
| Tianasen (ASO-GNAO1), intrathecal antisense oligonucleotide | GNAO1 encephalopathy with epilepsy and movement disorders / GNAO1 c.607G>A | NCT07363603 | Phase 1/2 | Recruiting | Change in duration of non-epileptic hyperkinetic/dystonic episodes; secondary: quantitative EEG epileptiform activity, Barry-Albright Dystonia Scale, concomitant medication dose, GMFM-88, Denver developmental age, Leiter-3 IQ | Children 1–14 years; requires confirmed c.607G>A GNAO1 variant, both epilepsy and movement disorders, resistance to ≥2 ASMs and ≥2 anti-hyperkinetic drugs; excludes contraindications to repeated lumbar punctures (NCT07363603 chunk 2) | (NCT07363603 chunk 2) |
| Phenylbutyrate precision-medicine trial | Monogenetic developmental and epileptic encephalopathy | NCT04937062 | Early Phase 1 | Active, not recruiting | Trial record retrieved as DEE precision-medicine intervention; detailed endpoints not available in provided evidence | Detailed eligibility not available in provided evidence | (scheffer2024developmentalandepileptic pages 31-34) |
| Fenfluramine pilot trial | Different types of developmental and epileptic encephalopathies | NCT05232630 | Phase 4 | Unknown | Pilot trial exploring epileptic and non-epileptic outcomes | Detailed eligibility not available in provided evidence | (scheffer2024developmentalandepileptic pages 31-34) |
| Pathophysiology-based genotype-informed ASM therapy (phenytoin, lacosamide; quinidine mentioned) | Early-onset genetic epileptic encephalopathies, especially ion-channel disorders (e.g., KCNT1, KCNQ2, SCN2A) | NCT02968966 | Phase 2 / IIb | Withdrawn | Primary: seizure reduction to 50% of baseline during one treatment phase; Secondary: seizure reduction by genetic background and reduction of epileptic activity/suppression phases on EEG | Onset 0–3 months, age <1 year, ≥1 seizure/day, pharmacoresistant after ≥2 anticonvulsants; no patients recruited (NCT02968966 chunk 1) | (NCT02968966 chunk 1) |
| Neonatal-onset epileptic encephalopathy registry (IMPROVE) | Neonatal-onset epileptic encephalopathy; rationale emphasizes KCNQ2-related disease | NCT04802135 | Not applicable (Observational registry) | Recruiting | Developmental quotient at Month 36; active epilepsy at Month 36 defined by at least monthly seizures plus interictal EEG paroxysmal abnormalities | Epilepsy beginning before 1 month requiring antiseizure treatment and no structural/acquired cause; registry/survey-based characterization study (NCT04802135 chunk 1) | (NCT04802135 chunk 1) |
| Genetic investigations observational implementation | Children with developmental and epileptic encephalopathies in Vietnam | NCT05722990 | Not applicable (Observational) | Unknown | Genetic investigations in DEE cohort; detailed endpoints not available in provided evidence | Detailed eligibility not available in provided evidence | (scheffer2024developmentalandepileptic pages 31-34) |
| Preclinical/translation pipeline: AAV/HD adenoviral/CAV-2/CRISPRa/zinc-finger strategies | Dravet syndrome / SCN1A | Not yet trial-specific in provided evidence | Preclinical | Not applicable | Preclinical outcomes include spontaneous seizure reduction, survival improvement, and raised hyperthermia seizure threshold in mouse models | Highlights need for early diagnosis and broader developmental endpoints for future gene/ASO trials (specchio2024theexpandingfield pages 14-17) | (specchio2024theexpandingfield pages 14-17) |


*Table: This table summarizes real-world clinical trials, registries, and translational precision-medicine implementations relevant to developmental and epileptic encephalopathies and early-onset epileptic encephalopathy. It is useful for identifying current gene therapy, ASO, genotype-guided treatment, and registry efforts, along with their design features and eligibility constraints.*

---

## 1. Disease information

### 1.1 What is the disease?
**Clinical overview.** DEEs are described as the most severe epilepsies, “**characterised by seizures and frequent epileptiform activity associated with developmental slowing or regression**,” with onset “typically… in infancy or childhood.” (scheffer2024developmentalandepileptic pages 1-4)

For a patient labelled “undetermined early-onset epileptic encephalopathy,” the core phenotype corresponds to an **early-onset DEE/epileptic encephalopathy presentation** in which aetiology remains unresolved at time of assessment.

**Conceptual definitions (ILAE-aligned).** In the 2024 DEE primer, an essential feature of an epileptic encephalopathy is “**slowing or regression in development, cognition or behaviour associated with frequent epileptiform activity on the… EEG**,” and the ILAE expanded the concept in 2017 to “**developmental and epileptic encephalopathy**” recognizing that the underlying aetiology frequently causes developmental impairment independently. (scheffer2024developmentalandepileptic pages 1-4)

### 1.2 Key identifiers and ontology anchors
**MONDO (available from retrieved sources).** Because the exact string “undetermined early-onset epileptic encephalopathy” is not a stable disease entity in the retrieved ontology evidence, the most appropriate approach is to represent it using DEE umbrella terms and age-of-onset groupings in MONDO:
- Early-infantile DEE: **MONDO:0800491** (ILAE-aligned; includes legacy Ohtahara/early myoclonic encephalopathy concepts). (vasilevsky2026epilepsydiseaseclassification pages 8-10)
- Epileptic encephalopathy, infantile or early: **MONDO:0020627** (broad early-presentation anchor). (vasilevsky2026epilepsydiseaseclassification pages 6-7)
- Age-of-onset grouping terms used by MONDO aligned with ILAE: **MONDO:0020070** (neonatal/infantile epilepsy syndrome), **MONDO:0020072** (childhood-onset epilepsy syndrome), **MONDO:0100619** (variable age epilepsy syndrome). (vasilevsky2026epilepsydiseaseclassification pages 6-7, vasilevsky2026epilepsydiseaseclassification pages 7-8)
- DEE branch: MONDO reports iterative updates including renaming “early infantile epileptic encephalopathy” to “developmental and epileptic encephalopathy,” and relabeling **MONDO:0100062** as **genetic developmental and epileptic encephalopathy**, with a **generic DEE superclass** above it. (vasilevsky2026epilepsydiseaseclassification pages 7-8)

**OMIM/Orphanet/ICD/MeSH.** No retrieved source provided an OMIM/Orphanet/ICD/MeSH identifier specifically for the *undetermined* label. However, the MONDO DEE branch described above was noted to correspond to an OMIM phenotypic series (PS308350). (vasilevsky2026epilepsydiseaseclassification pages 7-8)

### 1.3 Synonyms / alternative names
Likely synonyms and near-equivalents in practice/records include:
- “Developmental and epileptic encephalopathy (DEE)” (preferred modern umbrella). (scheffer2024developmentalandepileptic pages 1-4)
- “Epileptic encephalopathy” (older term; sometimes used when epileptiform activity is emphasized). (scheffer2024developmentalandepileptic pages 1-4)
- “Early-infantile DEE” (very early onset; includes legacy Ohtahara/early myoclonic encephalopathy concepts). (vasilevsky2026epilepsydiseaseclassification pages 8-10)
- “Early infantile epileptic encephalopathy (EIEE)” (legacy term; MONDO indicates renaming toward DEE). (vasilevsky2026epilepsydiseaseclassification pages 7-8)

### 1.4 Evidence source type (patient-level vs aggregated)
- **Aggregated disease-level definitions and conceptual framework**: 2024 Nature Reviews Disease Primers DEE primer and 2024 Lancet review. (scheffer2024developmentalandepileptic pages 1-4, specchio2024theexpandingfield pages 1-6)
- **Patient-level and cohort evidence**: Scotland population cohort (Brain 2021), clinical sequencing cohorts (JAMA Netw Open 2023; IJMS 2024), and WGS-after-unsolved cohort (MGGM 2023). (symonds2021earlychildhoodepilepsies pages 1-2, koh2023utilityofexome pages 1-2, vetri2024wholeexomesequencing pages 1-2, grether2023thecurrentbenefit pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
For “undetermined” cases, causal factors are unknown *at time of evaluation*. However, the DEE literature indicates:
- **Genetic** factors are a major contributor: a genetic cause is found in “**>50%**” of DEE patients using next-generation sequencing, and “**More than 900 genes**” have been identified as monogenic causes. (scheffer2024developmentalandepileptic pages 1-4)
- **Structural/acquired** causes are also common in early-onset epilepsies (e.g., hypoxic–ischemic encephalopathy, perinatal stroke, malformations of cortical development). (symonds2021earlychildhoodepilepsies pages 6-8, scheffer2024developmentalandepileptic pages 34-39)
- **Metabolic** and other treatable etiologies are important to exclude early via targeted blood/urine/CSF testing. (scheffer2024developmentalandepileptic pages 13-15)

### 2.2 Risk factors
**Socioeconomic/environmental context (population-level).** In Scotland, epilepsy incidence under age 3 showed a deprivation gradient (most deprived vs least deprived incidence **301 vs 182 per 100,000**, OR **1.7**), and this relationship was “only observed in the group without identified aetiology,” suggesting increased multifactorial risk in deprived populations. (symonds2021earlychildhoodepilepsies pages 1-2)

**Clinical risk factors for having an identifiable genetic diagnosis** (useful when deciding how aggressively to pursue genetics in “undetermined” cases):
- In a 2023 exome cohort of previously unexplained pediatric epilepsy, diagnostic yield was higher in those with intellectual disability (aOR **2.44**) and motor impairment (aOR **2.19**), and associated with earlier seizure onset. (koh2023utilityofexome pages 1-2)

### 2.3 Protective factors / gene–environment interactions
No retrieved sources provided specific protective genetic variants or quantified gene–environment interaction mechanisms for “undetermined early-onset epileptic encephalopathy.” This remains a gap for this entry based on the current corpus.

---

## 3. Phenotypes

### 3.1 Core phenotype set (HPO suggestions)
Because the “undetermined” label is heterogeneous, phenotype representation should prioritize **high-level DEE/epileptic encephalopathy features**:
- Seizures (HP:0001250)
- Early-onset seizures / Infantile onset seizures (HP:0003593 / HP:0003623; choose per onset)
- Developmental regression (HP:0002376) and/or Global developmental delay (HP:0001263)
- Intellectual disability (HP:0001249)
- Abnormal EEG with epileptiform discharges (HP:0010846)
- Drug-resistant epilepsy (HP:0002349)
- Autism spectrum disorder / autistic features (HP:0000729)
- Movement disorder/ataxia (HP:0001251 / HP:0001250; as applicable)
- Sleep disturbance (HP:0002360)
- Gastrointestinal problems (HP:0002017; broad)

These are consistent with the DEE primer’s comorbidity spectrum (ID, ASD/behavioral problems, movement/musculoskeletal, GI and sleep problems, increased mortality). (scheffer2024developmentalandepileptic pages 1-4)

### 3.2 Frequency, onset, progression (evidence-based highlights)
- **Age of onset**: ~**75%** of DEE cases begin under age 3. (scheffer2024developmentalandepileptic pages 1-4)
- **Syndrome classification gap**: around **one-third** of patients cannot be classified as having a specific DEE syndrome, which increases the practical use of an “undetermined” umbrella label. (scheffer2024developmentalandepileptic pages 1-4)
- **Outcome burden in early childhood epilepsy (<3 years)**: at 24 months after presentation, **36%** had drug-resistant epilepsy and **49%** had global developmental delay in the Scotland cohort. (symonds2021earlychildhoodepilepsies pages 1-2)

### 3.3 Quality-of-life impact
The DEE primer notes substantial psychosocial burden and the need for lifelong support. (scheffer2024developmentalandepileptic pages 1-4)

(Structured HRQOL instruments and per-phenotype QOL estimates were not retrievable from the current corpus for “undetermined” cases; this is a gap.)

---

## 4. Genetic / molecular information

### 4.1 Causal genes (landscape)
For an “undetermined” category, the knowledge base should represent **gene landscape and testing approach**, not a single causal gene.

- The DEE primer states **>900 monogenic genes** have been identified. (scheffer2024developmentalandepileptic pages 1-4)
- A 2024 review notes “Over **800 genes** have been reported to contribute to DEEs.” (specchio2024theexpandingfield pages 1-6)

Examples of genes frequently encountered in early childhood epilepsy genetic aetiology (Scotland cohort) included PRRT2, SCN1A, KCNQ2, SLC2A1, TSC1/TSC2, CDKL5, DEPDC5, PCDH19, SLC6A1. (symonds2021earlychildhoodepilepsies pages 6-8)

### 4.2 Variant classes and inheritance patterns
- In a 2024 DEE WES cohort (n=82), pathogenic variants were identified in **43%** and were predominantly **missense (75%)** with **66% de novo**; most frequent inheritance pattern was **autosomal dominant de novo (60%)**, with additional autosomal recessive and X-linked de novo contributions. (vetri2024wholeexomesequencing pages 1-2)

### 4.3 When the case remains undetermined: what next?
**Escalation and reanalysis are important**:
- Rapid genome sequencing in infants can provide high yield and meaningful immediate clinical utility (46% yield; 56% clinical utility; median 37 days turnaround). (scheffer2024developmentalandepileptic pages 9-11)
- Trio-WGS in an encephalopathy cohort unsolved after WES/CMA diagnosed **20%** (4/20), but authors argued the incremental advantage over contemporary WES was limited and much gain reflects reanalysis and evolving knowledge. (grether2023thecurrentbenefit pages 1-2)
- Mosaicism and CNVs require specific attention; chromosomal microarray yields were **8%** in the Scotland cohort’s post-presentation workup; WGS may improve detection of smaller CNVs/complex rearrangements. (symonds2021earlychildhoodepilepsies pages 6-8, grether2023thecurrentbenefit pages 6-9)

---

## 5. Environmental information
No disease-specific environmental toxins, lifestyle, or infectious triggers were identified in the retrieved sources for the undetermined early-onset encephalopathy category. However, the Scotland cohort’s deprivation-associated incidence pattern suggests that **multifactorial (non-single-gene) risk** may be enriched among children in more deprived settings when aetiology remains unidentified. (symonds2021earlychildhoodepilepsies pages 1-2)

---

## 6. Mechanism / pathophysiology

Given “undetermined” aetiology, mechanisms are **hypothesis-driven** and typically inferred from DEE biology:
- DEEs implicate diverse cellular components/processes including **ion channels/transporters, synaptic proteins, cell signalling, metabolism, and epigenetic regulation**. (scheffer2024developmentalandepileptic pages 1-4)
- The Lancet review highlights that **GoF vs LoF** variant effects can guide therapy choice, and shared pathway mechanisms (e.g., mTOR activation) represent therapeutic targets. (specchio2024theexpandingfield pages 6-8)

Suggested GO biological process terms (for knowledge base scaffolding; will be gene-specific once diagnosed):
- Synaptic transmission (GO:0007268)
- Regulation of membrane potential (GO:0042391)
- Neuron projection development (GO:0031175)
- mTOR signaling (GO:0031929)
- Regulation of ion transmembrane transport (GO:0034765)

Suggested cell types (CL terms; general for DEE):
- Cortical pyramidal neuron (CL:0002604)
- GABAergic interneuron (e.g., CL:0000617)
- Astrocyte (CL:0000127)

(These ontology suggestions are not directly asserted by the retrieved texts, but are standard mechanistic targets consistent with the ion-channel/synaptic/process statements above; gene-level assignment should be done after aetiology is found.) (scheffer2024developmentalandepileptic pages 1-4)

---

## 7. Anatomical structures affected
Primary system: **central nervous system**, particularly developing brain networks supporting cognition and seizure generation.

Diagnostic imaging emphasis: high-resolution MRI with epilepsy sequences, and targeted presurgical evaluation for focal lesions. (scheffer2024developmentalandepileptic pages 11-13)

Suggested UBERON terms:
- Brain (UBERON:0000955)
- Cerebral cortex (UBERON:0000956)
- Hippocampus (UBERON:0001954)

---

## 8. Temporal development
- Typical onset is neonatal/infantile/early childhood; DEEs present before age 16 and ~75% begin <3 years. (scheffer2024developmentalandepileptic pages 1-4)
- For neonatal-onset DEE, separation of developmental vs epileptic contributions can be difficult because both occur in the same developmental window. (scheffer2024developmentalandepileptic pages 1-4)

---

## 9. Inheritance and population

### 9.1 Epidemiology
- Cumulative incidence up to age 16 estimated **169/100,000** (1 in 590) in Wellington based on EEG ascertainment. (scheffer2024developmentalandepileptic pages 1-4)
- Scotland incidence of epilepsies presenting <3 years: **239/100,000**. (symonds2021earlychildhoodepilepsies pages 1-2)
- In Scotland cohort, DEEs accounted for **86.1/100,000** under age 3 (as cited in DEE primer). (scheffer2024developmentalandepileptic pages 1-4)

### 9.2 Inheritance patterns
DEEs include many **de novo dominant**, **autosomal recessive**, **X-linked**, and **mitochondrial** causes. (scheffer2024developmentalandepileptic pages 9-11)

For an undetermined case, inheritance cannot be assigned; however, the MONDO “genetic DEE” class (MONDO:0100062) was intentionally labeled **genetic** rather than hereditary to capture de novo variation and “presumed genetic” cases. (vasilevsky2026epilepsydiseaseclassification pages 7-8)

---

## 10. Diagnostics

### 10.1 Core clinical tests
- EEG (including video-EEG; sleep EEG for syndrome classification). (scheffer2024developmentalandepileptic pages 11-13)
- Brain MRI (3T with epilepsy protocol; advanced imaging and presurgical evaluation when indicated). (scheffer2024developmentalandepileptic pages 11-13)

### 10.2 Metabolic evaluation (especially relevant when “undetermined”)
The DEE primer recommends early metabolic screening (blood/urine; and consider CSF studies) to prioritize treatable disorders, including broad panels and targeted assays (e.g., amino acids, acylcarnitines, urine organic acids, and CSF lactate/pyruvate/neurotransmitters as indicated). (scheffer2024developmentalandepileptic pages 13-15)

### 10.3 Genetic testing strategy and expected yields
Evidence-based yields from cohorts most relevant to early-onset/undetermined settings:
- Post-presentation yields in Scotland cohort: gene panel **30%**, CMA **8%**, MRI **7%** (in those without established aetiology prior). (symonds2021earlychildhoodepilepsies pages 6-8)
- Exome in previously unexplained pediatric epilepsy: **19.2%** (100/522). (koh2023utilityofexome pages 1-2)
- WES in DEE cohort (first-line study): **43%**. (vetri2024wholeexomesequencing pages 1-2)
- Rapid genome sequencing in infants: **46%** with substantial clinical utility. (scheffer2024developmentalandepileptic pages 9-11)

Critical “undetermined case” implementation points:
- Panels can miss genes; consider exome/genome where feasible. (scheffer2024developmentalandepileptic pages 11-13)
- Mosaicism may require high-depth sequencing or alternate tissue (saliva/brain-derived DNA) and targeted confirmation (e.g., ddPCR). (scheffer2024developmentalandepileptic pages 11-13)

---

## 11. Outcomes / prognosis

In early childhood epilepsies (<3 years; Scotland cohort):
- At 24 months: **36%** had drug-resistant epilepsy and **49%** had global developmental delay; **3%** died by 24 months. (symonds2021earlychildhoodepilepsies pages 1-2, symonds2021earlychildhoodepilepsies pages 3-6)
- Identification of an aetiology was strongly associated with worse outcomes (OR for GDD **3.4**; OR for DRE **3.9**), reflecting that severe etiologies are more readily identifiable and also more prognostically adverse. (symonds2021earlychildhoodepilepsies pages 10-11)

For “undetermined” cases, prognosis is highly variable; persistent undetermined aetiology may reflect either (i) limitations in testing/interpretation or (ii) genuinely multifactorial/non-monogenic contributors.

---

## 12. Treatment

### 12.1 Standard-of-care seizure management and etiology-informed care
- The DEE primer emphasizes holistic management determined by syndrome and aetiology; diagnosis is crucial because “there may be therapeutic strategies that improve… epileptiform activity, thereby enabling… developmental gains.” (scheffer2024developmentalandepileptic pages 1-4)
- Example of etiology-informed avoidance: in Dravet syndrome, contraindicated sodium-channel blockers can exacerbate seizures; stopping them can improve seizure control and developmental gains. (scheffer2024developmentalandepileptic pages 9-11, scheffer2024developmentalandepileptic pages 34-39)

### 12.2 Precision therapies and recent developments (2023–2024 emphasis)
- **Rapid genome sequencing** enables earlier targeted management and counseling (46% yield; 56% clinical utility; 86% prognostic counseling utility). (scheffer2024developmentalandepileptic pages 9-11)
- **ASOs and gene therapy**: positive preclinical results for SCN1A/SCN2A/SCN8A/KCNT1; TANGO-based upregulation is in clinical trials (as summarized in the DEE primer). (scheffer2024developmentalandepileptic pages 17-19)

### 12.3 Real-world implementations / clinical trials (examples)
- CAP-002 gene therapy for STXBP1 encephalopathy: Phase 1/2a, pediatric, IV infusion; safety primary endpoints; seizure and developmental secondary outcomes; currently suspended. (NCT06983158 chunk 1)
- Tianasen ASO-GNAO1 (intrathecal) for GNAO1 encephalopathy with epilepsy and movement disorders: recruiting; endpoints include hyperkinetic episode duration and quantitative EEG epileptiform activity. (NCT07363603 chunk 2)
- Neonatal-onset epileptic encephalopathy registry (IMPROVE; NCT04802135): recruiting; outcomes include developmental quotient and active epilepsy status at 36 months. (NCT04802135 chunk 1)

### 12.4 MAXO suggestions (action ontology; examples)
- Antiseizure medication therapy (MAXO:0000602)
- Electroencephalography (MAXO:0000473)
- Magnetic resonance imaging (MAXO:0000901)
- Genetic testing (MAXO:0000127)
- Whole exome sequencing (MAXO:0000935)
- Whole genome sequencing (MAXO:0000936)
- Gene therapy (MAXO:0001001)
- Antisense oligonucleotide therapy (MAXO:0001020)

(MAXO IDs are provided as suggested mappings; the clinical actions themselves are directly supported by the cited diagnostic/treatment evidence.) (scheffer2024developmentalandepileptic pages 11-13, NCT06983158 chunk 1)

---

## 13. Prevention
No primary prevention strategies are specific to the undetermined early-onset DEE state in the retrieved evidence. Secondary/tertiary prevention in practice focuses on **early diagnosis**, **avoidance of contraindicated medications**, and **rapid initiation of syndrome-specific therapy** (e.g., rapid treatment of infantile spasms; early etiologic identification for Dravet medication selection). (scheffer2024developmentalandepileptic pages 34-39, symonds2021earlychildhoodepilepsies pages 11-12)

---

## 14. Other species / natural disease
No retrieved sources described naturally occurring animal disease analogs for the undetermined category.

---

## 15. Model organisms
The retrieved evidence summarizes **preclinical gene-based strategies** (e.g., vector delivery and transcriptional activation for SCN1A/Dravet) with outcomes in mouse models (seizure reduction, survival improvement, improved hyperthermia thresholds). (specchio2024theexpandingfield pages 14-17)

---

## Direct quotes from abstracts (key support)
- Symonds et al. (Brain 2021) abstract: “**Aetiology was determined in 54% of children…** Twenty-four months after presentation, **36%** … had drug-resistant epilepsy (DRE), and **49%** … had global developmental delay (GDD).” (symonds2021earlychildhoodepilepsies pages 1-2)
- Koh et al. (JAMA Netw Open 2023) abstract/key points: “exome sequencing to identify and clinically confirm diagnostic results for **100** children…” and “**at least 29** patients had changes in treatment, surveillance, or prognosis…” (koh2023utilityofexome pages 1-2)
- Vetri et al. (IJMS 2024) abstract: “We performed **82** WESs, identifying **35** pathogenic variants with a detection rate of **43%**.” (vetri2024wholeexomesequencing pages 1-2)

---

## Known gaps / limitations for this knowledge-base entry
1. The retrieved corpus did not provide **Orphanet**, **ICD-10/ICD-11**, or **MeSH** identifiers specific to the exact “undetermined early-onset epileptic encephalopathy” label; therefore, this report anchors the entity via MONDO DEE terms and age-of-onset groupings plus clinical DEE definitions. (vasilevsky2026epilepsydiseaseclassification pages 7-8, scheffer2024developmentalandepileptic pages 1-4)
2. Protective factors, detailed gene–environment interactions, and standardized HRQOL instrument outcomes for the undetermined subgroup were not available in the retrieved texts.



References

1. (scheffer2024developmentalandepileptic pages 1-4): Ingrid E. Scheffer, Sameer Zuberi, Heather C. Mefford, Renzo Guerrini, and Amy McTague. Developmental and epileptic encephalopathies. Nature reviews. Disease primers, 10 1:61, Sep 2024. URL: https://doi.org/10.1038/s41572-024-00546-6, doi:10.1038/s41572-024-00546-6. This article has 125 citations.

2. (vasilevsky2026epilepsydiseaseclassification pages 7-8): Nicole Vasilevsky, Sarah Gehrke, Kathleen Mullen, Subit Barua, Ian Braun, Tobias Brünger, Curtis Coughlin, Alina Ivaniuk, Daniel Korn, Dennis Lal, Stephanie Marsh, Elaine O’Loughlin, Daniel Olson, Yousif Shwetar, Christalena Sofocleous, Vanessa Vogel-Farley, Heidi Grabenstatter, Melissa Haendel, Christopher Mungall, and Sabrina Toro. Epilepsy disease classification: a community effort to enhance the mondo disease ontology. Database: The Journal of Biological Databases and Curation, Jan 2026. URL: https://doi.org/10.1093/database/baag004, doi:10.1093/database/baag004. This article has 0 citations.

3. (symonds2021earlychildhoodepilepsies pages 6-8): Joseph D Symonds, Katherine S Elliott, Jay Shetty, Martin Armstrong, Andreas Brunklaus, Ioana Cutcutache, Louise A Diver, Liam Dorris, Sarah Gardiner, Alice Jollands, Shelagh Joss, Martin Kirkpatrick, Ailsa McLellan, Stewart MacLeod, Mary O’Regan, Matthew Page, Elizabeth Pilley, Daniela T Pilz, Elma Stephen, Kirsty Stewart, Houman Ashrafian, Julian C Knight, and Sameer M Zuberi. Early childhood epilepsies: epidemiology, classification, aetiology, and socio-economic determinants. Brain, 144:2879-2891, Sep 2021. URL: https://doi.org/10.1093/brain/awab162, doi:10.1093/brain/awab162. This article has 268 citations and is from a highest quality peer-reviewed journal.

4. (symonds2021earlychildhoodepilepsies pages 1-2): Joseph D Symonds, Katherine S Elliott, Jay Shetty, Martin Armstrong, Andreas Brunklaus, Ioana Cutcutache, Louise A Diver, Liam Dorris, Sarah Gardiner, Alice Jollands, Shelagh Joss, Martin Kirkpatrick, Ailsa McLellan, Stewart MacLeod, Mary O’Regan, Matthew Page, Elizabeth Pilley, Daniela T Pilz, Elma Stephen, Kirsty Stewart, Houman Ashrafian, Julian C Knight, and Sameer M Zuberi. Early childhood epilepsies: epidemiology, classification, aetiology, and socio-economic determinants. Brain, 144:2879-2891, Sep 2021. URL: https://doi.org/10.1093/brain/awab162, doi:10.1093/brain/awab162. This article has 268 citations and is from a highest quality peer-reviewed journal.

5. (scheffer2024developmentalandepileptic pages 9-11): Ingrid E. Scheffer, Sameer Zuberi, Heather C. Mefford, Renzo Guerrini, and Amy McTague. Developmental and epileptic encephalopathies. Nature reviews. Disease primers, 10 1:61, Sep 2024. URL: https://doi.org/10.1038/s41572-024-00546-6, doi:10.1038/s41572-024-00546-6. This article has 125 citations.

6. (koh2023utilityofexome pages 1-2): Hyun Yong Koh, Lacey Smith, Kimberly N. Wiltrout, Archana Podury, Nitish Chourasia, Alissa M. D’Gama, Meredith Park, Devon Knight, Emma L. Sexton, Julia J. Koh, Brandon Oby, Rebecca Pinsky, Diane D. Shao, Courtney E. French, Wanqing Shao, Shira Rockowitz, Piotr Sliz, Bo Zhang, Sonal Mahida, Christelle Moufawad El Achkar, Christopher J. Yuskaitis, Heather E. Olson, Beth Rosen Sheidley, Annapurna H. Poduri, Elizabeth Barkoudah, Ann M. Bergin, Miya Bernson-Leung, Elizabeth Binney, Jeffrey Bolton, Stephanie Donatelli, Darius Ebrahimi-Fakhari, Mark P. Gorman, Chellamani Harini, Divya Jayaraman, Agnieszka A. Kielian, Lauren LaFortune, Kerri Larovere, Mark Libenson, David N. Lieberman, Tobias Loddenkemper, Candice E. Marti, Anna Minster, Kate Mysak, Ann Paris, Archana A. Patel, Phillip L. Pearl, Jurriaan M. Peters, Anna Pinto, Peter Raffalli, Alexander Rotenberg, Catherine Salussolia, Rebecca Sarvendram, Hannah Shapiro, Janet Soul, Sarah Spence, Karen Spencer, Robert C. Stowe, Coral M. Stredny, Masanori Takeoka, Molly Tracy, Sara K. Trowbridge, Melissa Tsuboyama, and David K. Urion. Utility of exome sequencing for diagnosis in unexplained pediatric-onset epilepsy. JAMA Network Open, 6:e2324380, Jul 2023. URL: https://doi.org/10.1001/jamanetworkopen.2023.24380, doi:10.1001/jamanetworkopen.2023.24380. This article has 43 citations and is from a peer-reviewed journal.

7. (vasilevsky2026epilepsydiseaseclassification pages 1-2): Nicole Vasilevsky, Sarah Gehrke, Kathleen Mullen, Subit Barua, Ian Braun, Tobias Brünger, Curtis Coughlin, Alina Ivaniuk, Daniel Korn, Dennis Lal, Stephanie Marsh, Elaine O’Loughlin, Daniel Olson, Yousif Shwetar, Christalena Sofocleous, Vanessa Vogel-Farley, Heidi Grabenstatter, Melissa Haendel, Christopher Mungall, and Sabrina Toro. Epilepsy disease classification: a community effort to enhance the mondo disease ontology. Database: The Journal of Biological Databases and Curation, Jan 2026. URL: https://doi.org/10.1093/database/baag004, doi:10.1093/database/baag004. This article has 0 citations.

8. (vasilevsky2026epilepsydiseaseclassification pages 8-10): Nicole Vasilevsky, Sarah Gehrke, Kathleen Mullen, Subit Barua, Ian Braun, Tobias Brünger, Curtis Coughlin, Alina Ivaniuk, Daniel Korn, Dennis Lal, Stephanie Marsh, Elaine O’Loughlin, Daniel Olson, Yousif Shwetar, Christalena Sofocleous, Vanessa Vogel-Farley, Heidi Grabenstatter, Melissa Haendel, Christopher Mungall, and Sabrina Toro. Epilepsy disease classification: a community effort to enhance the mondo disease ontology. Database: The Journal of Biological Databases and Curation, Jan 2026. URL: https://doi.org/10.1093/database/baag004, doi:10.1093/database/baag004. This article has 0 citations.

9. (vasilevsky2026epilepsydiseaseclassification pages 6-7): Nicole Vasilevsky, Sarah Gehrke, Kathleen Mullen, Subit Barua, Ian Braun, Tobias Brünger, Curtis Coughlin, Alina Ivaniuk, Daniel Korn, Dennis Lal, Stephanie Marsh, Elaine O’Loughlin, Daniel Olson, Yousif Shwetar, Christalena Sofocleous, Vanessa Vogel-Farley, Heidi Grabenstatter, Melissa Haendel, Christopher Mungall, and Sabrina Toro. Epilepsy disease classification: a community effort to enhance the mondo disease ontology. Database: The Journal of Biological Databases and Curation, Jan 2026. URL: https://doi.org/10.1093/database/baag004, doi:10.1093/database/baag004. This article has 0 citations.

10. (symonds2021earlychildhoodepilepsies pages 3-6): Joseph D Symonds, Katherine S Elliott, Jay Shetty, Martin Armstrong, Andreas Brunklaus, Ioana Cutcutache, Louise A Diver, Liam Dorris, Sarah Gardiner, Alice Jollands, Shelagh Joss, Martin Kirkpatrick, Ailsa McLellan, Stewart MacLeod, Mary O’Regan, Matthew Page, Elizabeth Pilley, Daniela T Pilz, Elma Stephen, Kirsty Stewart, Houman Ashrafian, Julian C Knight, and Sameer M Zuberi. Early childhood epilepsies: epidemiology, classification, aetiology, and socio-economic determinants. Brain, 144:2879-2891, Sep 2021. URL: https://doi.org/10.1093/brain/awab162, doi:10.1093/brain/awab162. This article has 268 citations and is from a highest quality peer-reviewed journal.

11. (symonds2021earlychildhoodepilepsies pages 8-9): Joseph D Symonds, Katherine S Elliott, Jay Shetty, Martin Armstrong, Andreas Brunklaus, Ioana Cutcutache, Louise A Diver, Liam Dorris, Sarah Gardiner, Alice Jollands, Shelagh Joss, Martin Kirkpatrick, Ailsa McLellan, Stewart MacLeod, Mary O’Regan, Matthew Page, Elizabeth Pilley, Daniela T Pilz, Elma Stephen, Kirsty Stewart, Houman Ashrafian, Julian C Knight, and Sameer M Zuberi. Early childhood epilepsies: epidemiology, classification, aetiology, and socio-economic determinants. Brain, 144:2879-2891, Sep 2021. URL: https://doi.org/10.1093/brain/awab162, doi:10.1093/brain/awab162. This article has 268 citations and is from a highest quality peer-reviewed journal.

12. (vetri2024wholeexomesequencing pages 1-2): Luigi Vetri, Francesco Calì, Salvatore Saccone, Mirella Vinci, Natalia Valeria Chiavetta, Marco Carotenuto, Michele Roccella, Carola Costanza, and Maurizio Elia. Whole exome sequencing as a first-line molecular genetic test in developmental and epileptic encephalopathies. International Journal of Molecular Sciences, 25:1146, Jan 2024. URL: https://doi.org/10.3390/ijms25021146, doi:10.3390/ijms25021146. This article has 21 citations.

13. (grether2023thecurrentbenefit pages 4-5): Anna Grether, Ivan Ivanovski, Martina Russo, Anaïs Begemann, Katharina Steindl, Lucia Abela, Michael Papik, Markus Zweier, Beatrice Oneda, Pascal Joset, and Anita Rauch. The current benefit of genome sequencing compared to exome sequencing in patients with developmental or epileptic encephalopathies. Molecular Genetics & Genomic Medicine, Feb 2023. URL: https://doi.org/10.1002/mgg3.2148, doi:10.1002/mgg3.2148. This article has 25 citations and is from a peer-reviewed journal.

14. (grether2023thecurrentbenefit pages 1-2): Anna Grether, Ivan Ivanovski, Martina Russo, Anaïs Begemann, Katharina Steindl, Lucia Abela, Michael Papik, Markus Zweier, Beatrice Oneda, Pascal Joset, and Anita Rauch. The current benefit of genome sequencing compared to exome sequencing in patients with developmental or epileptic encephalopathies. Molecular Genetics & Genomic Medicine, Feb 2023. URL: https://doi.org/10.1002/mgg3.2148, doi:10.1002/mgg3.2148. This article has 25 citations and is from a peer-reviewed journal.

15. (scheffer2024developmentalandepileptic pages 11-13): Ingrid E. Scheffer, Sameer Zuberi, Heather C. Mefford, Renzo Guerrini, and Amy McTague. Developmental and epileptic encephalopathies. Nature reviews. Disease primers, 10 1:61, Sep 2024. URL: https://doi.org/10.1038/s41572-024-00546-6, doi:10.1038/s41572-024-00546-6. This article has 125 citations.

16. (NCT06983158 chunk 1):  A Clinical Trial of CAP-002 Gene Therapy in Pediatric Patients With Syntaxin-Binding Protein 1 (STXBP1) Encephalopathy. Capsida Biotherapeutics, Inc.. 2025. ClinicalTrials.gov Identifier: NCT06983158

17. (NCT06983158 chunk 2):  A Clinical Trial of CAP-002 Gene Therapy in Pediatric Patients With Syntaxin-Binding Protein 1 (STXBP1) Encephalopathy. Capsida Biotherapeutics, Inc.. 2025. ClinicalTrials.gov Identifier: NCT06983158

18. (NCT07363603 chunk 2):  Tianasen (ASO-GNAO1) for GNAO1-Encephalopathy With Epilepsy and Movement Disorders.. Pirogov Russian National Research Medical University. 2025. ClinicalTrials.gov Identifier: NCT07363603

19. (scheffer2024developmentalandepileptic pages 31-34): Ingrid E. Scheffer, Sameer Zuberi, Heather C. Mefford, Renzo Guerrini, and Amy McTague. Developmental and epileptic encephalopathies. Nature reviews. Disease primers, 10 1:61, Sep 2024. URL: https://doi.org/10.1038/s41572-024-00546-6, doi:10.1038/s41572-024-00546-6. This article has 125 citations.

20. (NCT02968966 chunk 1):  Pathophysiology Based Therapy of Early Onset Epileptic Encephalopathies. University Hospital Tuebingen. 2018. ClinicalTrials.gov Identifier: NCT02968966

21. (NCT04802135 chunk 1):  Creation of a Register of Patients With Neonatal-onset Epileptic Encephalopathy. Assistance Publique Hopitaux De Marseille. 2021. ClinicalTrials.gov Identifier: NCT04802135

22. (specchio2024theexpandingfield pages 14-17): Nicola Specchio, Marina Trivisano, Eleonora Aronica, Simona Balestrini, Alexis Arzimanoglou, Gaia Colasante, J Helen Cross, Sergiusz Jozwiak, Jo M Wilmshurst, Federico Vigevano, Stéphane Auvin, Rima Nabbout, and Paolo Curatolo. The expanding field of genetic developmental and epileptic encephalopathies: current understanding and future perspectives. The Lancet. Child & adolescent health, 8 11:821-834, Nov 2024. URL: https://doi.org/10.1016/s2352-4642(24)00196-2, doi:10.1016/s2352-4642(24)00196-2. This article has 28 citations.

23. (specchio2024theexpandingfield pages 1-6): Nicola Specchio, Marina Trivisano, Eleonora Aronica, Simona Balestrini, Alexis Arzimanoglou, Gaia Colasante, J Helen Cross, Sergiusz Jozwiak, Jo M Wilmshurst, Federico Vigevano, Stéphane Auvin, Rima Nabbout, and Paolo Curatolo. The expanding field of genetic developmental and epileptic encephalopathies: current understanding and future perspectives. The Lancet. Child & adolescent health, 8 11:821-834, Nov 2024. URL: https://doi.org/10.1016/s2352-4642(24)00196-2, doi:10.1016/s2352-4642(24)00196-2. This article has 28 citations.

24. (scheffer2024developmentalandepileptic pages 34-39): Ingrid E. Scheffer, Sameer Zuberi, Heather C. Mefford, Renzo Guerrini, and Amy McTague. Developmental and epileptic encephalopathies. Nature reviews. Disease primers, 10 1:61, Sep 2024. URL: https://doi.org/10.1038/s41572-024-00546-6, doi:10.1038/s41572-024-00546-6. This article has 125 citations.

25. (scheffer2024developmentalandepileptic pages 13-15): Ingrid E. Scheffer, Sameer Zuberi, Heather C. Mefford, Renzo Guerrini, and Amy McTague. Developmental and epileptic encephalopathies. Nature reviews. Disease primers, 10 1:61, Sep 2024. URL: https://doi.org/10.1038/s41572-024-00546-6, doi:10.1038/s41572-024-00546-6. This article has 125 citations.

26. (grether2023thecurrentbenefit pages 6-9): Anna Grether, Ivan Ivanovski, Martina Russo, Anaïs Begemann, Katharina Steindl, Lucia Abela, Michael Papik, Markus Zweier, Beatrice Oneda, Pascal Joset, and Anita Rauch. The current benefit of genome sequencing compared to exome sequencing in patients with developmental or epileptic encephalopathies. Molecular Genetics & Genomic Medicine, Feb 2023. URL: https://doi.org/10.1002/mgg3.2148, doi:10.1002/mgg3.2148. This article has 25 citations and is from a peer-reviewed journal.

27. (specchio2024theexpandingfield pages 6-8): Nicola Specchio, Marina Trivisano, Eleonora Aronica, Simona Balestrini, Alexis Arzimanoglou, Gaia Colasante, J Helen Cross, Sergiusz Jozwiak, Jo M Wilmshurst, Federico Vigevano, Stéphane Auvin, Rima Nabbout, and Paolo Curatolo. The expanding field of genetic developmental and epileptic encephalopathies: current understanding and future perspectives. The Lancet. Child & adolescent health, 8 11:821-834, Nov 2024. URL: https://doi.org/10.1016/s2352-4642(24)00196-2, doi:10.1016/s2352-4642(24)00196-2. This article has 28 citations.

28. (symonds2021earlychildhoodepilepsies pages 10-11): Joseph D Symonds, Katherine S Elliott, Jay Shetty, Martin Armstrong, Andreas Brunklaus, Ioana Cutcutache, Louise A Diver, Liam Dorris, Sarah Gardiner, Alice Jollands, Shelagh Joss, Martin Kirkpatrick, Ailsa McLellan, Stewart MacLeod, Mary O’Regan, Matthew Page, Elizabeth Pilley, Daniela T Pilz, Elma Stephen, Kirsty Stewart, Houman Ashrafian, Julian C Knight, and Sameer M Zuberi. Early childhood epilepsies: epidemiology, classification, aetiology, and socio-economic determinants. Brain, 144:2879-2891, Sep 2021. URL: https://doi.org/10.1093/brain/awab162, doi:10.1093/brain/awab162. This article has 268 citations and is from a highest quality peer-reviewed journal.

29. (scheffer2024developmentalandepileptic pages 17-19): Ingrid E. Scheffer, Sameer Zuberi, Heather C. Mefford, Renzo Guerrini, and Amy McTague. Developmental and epileptic encephalopathies. Nature reviews. Disease primers, 10 1:61, Sep 2024. URL: https://doi.org/10.1038/s41572-024-00546-6, doi:10.1038/s41572-024-00546-6. This article has 125 citations.

30. (symonds2021earlychildhoodepilepsies pages 11-12): Joseph D Symonds, Katherine S Elliott, Jay Shetty, Martin Armstrong, Andreas Brunklaus, Ioana Cutcutache, Louise A Diver, Liam Dorris, Sarah Gardiner, Alice Jollands, Shelagh Joss, Martin Kirkpatrick, Ailsa McLellan, Stewart MacLeod, Mary O’Regan, Matthew Page, Elizabeth Pilley, Daniela T Pilz, Elma Stephen, Kirsty Stewart, Houman Ashrafian, Julian C Knight, and Sameer M Zuberi. Early childhood epilepsies: epidemiology, classification, aetiology, and socio-economic determinants. Brain, 144:2879-2891, Sep 2021. URL: https://doi.org/10.1093/brain/awab162, doi:10.1093/brain/awab162. This article has 268 citations and is from a highest quality peer-reviewed journal.