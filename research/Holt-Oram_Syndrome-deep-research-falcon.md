---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T22:30:53.193722'
end_time: '2026-05-09T22:46:37.066173'
duration_seconds: 943.87
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Holt-Oram syndrome
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 32
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Holt-Oram syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Holt-Oram syndrome** covering all of the
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
- **Disease Name:** Holt-Oram syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Holt-Oram syndrome** covering all of the
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


# Holt–Oram syndrome (HOS) — Disease Characteristics Research Report (Genetic)

## Executive summary
Holt–Oram syndrome (HOS) is an autosomal dominant “heart–hand” syndrome defined by congenital upper-limb (classically preaxial/radial-ray) malformations together with congenital heart disease (especially septal defects) and/or cardiac conduction/rhythm abnormalities, most often caused by pathogenic variants in **TBX5** (12q24) (vanlerberghe2019holtoramsyndromeclinical pages 1-2, atlas2024whentheheart pages 1-3). Disease burden and mortality risk are primarily driven by the cardiac phenotype, while skeletal anomalies dominate functional impairment (atlas2024whentheheart pages 1-3, dmowski2025holtoramsyndromewhen pages 8-12).

## 1. Disease information
### 1.1 What is the disease?
HOS is a congenital malformation syndrome in which **upper-limb radial/preaxial anomalies** co-occur with **congenital heart defects (CHD)** (most commonly ASD/VSD) and **conduction/rhythm disturbances** (vanlerberghe2019holtoramsyndromeclinical pages 1-2, vanlerberghe2019holtoramsyndromeclinical pages 4-5). A 2024 case report summarizes: “Holt–Oram syndrome is a rare genetic disorder caused by a mutation in the TBX5 gene, combining skeletal and cardiac malformations” (published 2024-09-xx; URL: https://doi.org/10.1186/s43044-024-00549-4) (atlas2024whentheheart pages 1-3).

### 1.2 Key identifiers (and gaps)
* **OMIM disease**: **Holt–Oram syndrome (MIM/OMIM #142900)** (vanlerberghe2019holtoramsyndromeclinical pages 1-2, economou2025firstlivebirth pages 1-3, ouwerkerk2022patientspecifictbx5g125rvariant pages 1-2).
* **TBX5 gene**: cited with **OMIM ID 601620** in TBX5/HOS literature ().
* **Orphanet / ICD-10 / ICD-11 / MeSH / MONDO**: not directly retrievable from the currently available full-text evidence set used here; therefore not reported with primary citations.

### 1.3 Synonyms and alternative names
* **Heart–hand syndrome** / **hand–heart syndrome** (ouwerkerk2022patientspecifictbx5g125rvariant pages 1-2).
* **Atrio-digital syndrome** (used in clinical literature) (liu2026experiencewithpatients pages 1-2).

### 1.4 Evidence source type
This report integrates:
* **Aggregated disease-level evidence** from cohort studies and mechanistic model studies (e.g., Vanlerberghe 2019; Bosada 2023; van Ouwerkerk 2022) (vanlerberghe2019holtoramsyndromeclinical pages 1-2, bosada2023anatrialfibrillationassociated pages 1-2, ouwerkerk2022patientspecifictbx5g125rvariant pages 1-2).
* **Individual patient evidence** from case reports and implementation reports (Atlas 2024; Economou 2025) (atlas2024whentheheart pages 1-3, economou2025firstlivebirth pages 1-3).

## 2. Etiology
### 2.1 Disease causal factors
**Primary cause:** germline pathogenic variants affecting **TBX5**, a T-box transcription factor required for cardiac septation, conduction system development, and forelimb initiation/patterning (vanlerberghe2019holtoramsyndromeclinical pages 1-2, dmowski2025holtoramsyndromewhen pages 5-8).

**Inheritance:** autosomal dominant (vanlerberghe2019holtoramsyndromeclinical pages 1-2, atlas2024whentheheart pages 1-3).

**De novo occurrence:** many cases are sporadic; a recent retrospective series states “roughly 85% are reported as de novo mutations” (liu2026experiencewithpatients pages 4-6).

### 2.2 Risk factors
**Genetic risk factor (causal):** heterozygous pathogenic TBX5 variants (loss-of-function predominates) (vanlerberghe2019holtoramsyndromeclinical pages 2-4, vanlerberghe2019holtoramsyndromeclinical pages 1-2).

**Variant classes (2019 largest molecular series of TBX5-positive patients):** among TBX5-positive probands, point variants were ~87% with many truncating (nonsense 37%, frameshift 26%, splice-site 10%); intragenic deletions 8% and duplications 4% detected by MLPA (vanlerberghe2019holtoramsyndromeclinical pages 2-4).

**Reduced penetrance/mosaicism:** asymptomatic carrier parents were documented, and one father showed somatic mosaicism (~10% in blood), complicating family-history-based risk inference (vanlerberghe2019holtoramsyndromeclinical pages 2-4).

Environmental/lifestyle risk factors are **not established** for this primarily monogenic developmental disorder in the evidence set.

### 2.3 Protective factors
No validated protective genetic or environmental factors were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
No direct gene–environment interaction evidence specific to HOS was identified in the retrieved evidence.

## 3. Phenotypes
### 3.1 Core phenotype domains
HOS is characterized by:
1) **Upper limb radial/preaxial malformations** (thumb/thenar/radius/forearm),
2) **Congenital heart defects** (especially septal defects), and
3) **Conduction/rhythm abnormalities**, sometimes independent of structural CHD (dmowski2025holtoramsyndromewhen pages 5-8, vanlerberghe2019holtoramsyndromeclinical pages 4-5).

### 3.2 Quantitative phenotype frequencies (key recent data)
The largest molecular cohort in this evidence set (Vanlerberghe et al., *Eur J Hum Genet*, accepted 2018-10-25; URL: https://doi.org/10.1038/s41431-018-0303-3; published 2019) reports (probands with TBX5 variants):
* **Any CHD**: 91% (vanlerberghe2019holtoramsyndromeclinical pages 1-2).
* **ASD**: 61.5%; **VSD**: 34.6% (vanlerberghe2019holtoramsyndromeclinical pages 4-5).
* **Conduction disturbances**: isolated 4.2%, and with CHD 25.3% (including sinus bradycardia 8.5%, AV block 2.8%, RBBB 7%) (vanlerberghe2019holtoramsyndromeclinical pages 4-5).
* Common limb findings include thenar hypoplasia (~26–28%), thumb hypoplasia (~30–33%), thumb agenesis (~22–32%), and I–II syndactyly (~14–15%) (vanlerberghe2019holtoramsyndromeclinical pages 4-5).

A structured comparison table is provided below.

| Domain | Finding | Frequency/Statistic | Study/Cohort | Notes |
|---|---|---|---|---|
| Clinical features | Congenital heart disease (CHD) overall | 91% (71/78) | Vanlerberghe 2019; 78 TBX5-variant probands | Molecularly confirmed TBX5 cohort; septal defects dominated the cardiac spectrum (vanlerberghe2019holtoramsyndromeclinical pages 1-2, vanlerberghe2019holtoramsyndromeclinical pages 4-5) |
| Clinical features | Atrial septal defect (ASD) | 61.5% (48/78) | Vanlerberghe 2019; 78 TBX5-variant probands | Most common structural lesion; includes ostium secundum ASD predominance in HOS literature (vanlerberghe2019holtoramsyndromeclinical pages 4-5, vanlerberghe2019holtoramsyndromeclinical pages 1-2) |
| Clinical features | Ventricular septal defect (VSD) | 34.6% (27/78) | Vanlerberghe 2019; 78 TBX5-variant probands | Other CHD such as PDA, coarctation, and pulmonary stenosis were less common (vanlerberghe2019holtoramsyndromeclinical pages 4-5) |
| Clinical features | Rhythm or conduction disturbance overall | ~29.6% (21/71 total evaluable) | Vanlerberghe 2019; 71 evaluable for rhythm data | Composed of 25.3% with CHD (18/71) plus 4.2% isolated (3/71); included sinus bradycardia, AV block, RBBB, junctional tachycardia, and rare long QT (vanlerberghe2019holtoramsyndromeclinical pages 4-5) |
| Clinical features | Thumb hypoplasia | Right 29.5% (23/78); Left 33.3% (26/78) | Vanlerberghe 2019; 78 TBX5-variant probands | Representative preaxial/radial-ray anomaly; bilateral involvement common in cohort (vanlerberghe2019holtoramsyndromeclinical pages 4-5, vanlerberghe2019holtoramsyndromeclinical pages 5-7) |
| Clinical features | Thumb agenesis | Right 21.8% (17/78); Left 32.1% (25/78) | Vanlerberghe 2019; 78 TBX5-variant probands | Left side often more severely affected (vanlerberghe2019holtoramsyndromeclinical pages 4-5, vanlerberghe2019holtoramsyndromeclinical pages 1-2) |
| Clinical features | Triphalangeal thumb | ~21% to 27% | Vanlerberghe 2019; 78 TBX5-variant probands | Frequency reported as a range across sides and summary text (vanlerberghe2019holtoramsyndromeclinical pages 5-7) |
| Clinical features | Thenar hypoplasia | ~25% to 28% | Vanlerberghe 2019; 78 TBX5-variant probands | Common subtle hand finding relevant to diagnosis (vanlerberghe2019holtoramsyndromeclinical pages 4-5, vanlerberghe2019holtoramsyndromeclinical pages 5-7) |
| Clinical features | I to II syndactyly | ~13% to 15% | Vanlerberghe 2019; 78 TBX5-variant probands | Less frequent but recurrent upper-limb feature (vanlerberghe2019holtoramsyndromeclinical pages 4-5, vanlerberghe2019holtoramsyndromeclinical pages 5-7) |
| Clinical features | Radial hypoplasia or agenesis | ~20% hypoplasia; ~4% to 10% agenesis | Vanlerberghe 2019; 78 TBX5-variant probands | Supports radial-ray disease pattern in HOS (vanlerberghe2019holtoramsyndromeclinical pages 5-7) |
| Clinical features | CHD overall | 10/11 (90.9%) | Liu 2026; 11 clinically suspected or diagnosed patients | Single-center retrospective series; 1/11 had isolated arrhythmia without structural CHD (liu2026experiencewithpatients pages 2-4) |
| Clinical features | Atrial septal defect (ASD) | 8/10 CHD cases (~80% of CHD cases) | Liu 2026; 11 patients | Secundum ASD was most frequent subtype; article text also describes ASD as 80% in series summaries (liu2026experiencewithpatients pages 2-4, liu2026experiencewithpatients pages 1-2) |
| Clinical features | Ventricular septal defect (VSD) | 2/11 (18.2%) | Liu 2026; 11 patients | PDA in 4/11 also reported; complex CHD such as TOF, pulmonary atresia, and Ebstein anomaly occurred (liu2026experiencewithpatients pages 2-4) |
| Clinical features | ECG abnormality or conduction-arrhythmia overall | 10/11 (90.9%) | Liu 2026; 11 patients | Very high ECG abnormality burden in this referral cohort; included SVT, sinus tachycardia, AV block, bundle branch block, and atrial fibrillation (liu2026experiencewithpatients pages 4-6) |
| Clinical features | Supraventricular tachycardia (SVT) | 4/11 (36.4%) | Liu 2026; 11 patients | Atrial fibrillation and first-degree AV block also documented; median follow-up was 7.2 years (liu2026experiencewithpatients pages 4-6) |
| Clinical features | Triphalangeal thumb | 8/10 with limb-detail available (80%) | Liu 2026; 11 patients | Most frequent specific limb anomaly highlighted by authors (liu2026experiencewithpatients pages 1-2) |
| Clinical features | Upper-limb malformations overall | 11/11 (100%) | Liu 2026; 11 patients | Mostly hand-limited; examples included absent or floating thumb, syndactyly, polydactyly, and radial defects (liu2026experiencewithpatients pages 2-4, liu2026experiencewithpatients pages 1-2) |
| Genetics or testing | TBX5 testing yield in referred suspected HOS cohort | 58% (78/212) | Vanlerberghe 2019; 212 referred for TBX5 screening | Yield increased to 70% in subgroup with bilateral anterior upper-limb defect plus CHD (vanlerberghe2019holtoramsyndromeclinical pages 2-4, vanlerberghe2019holtoramsyndromeclinical pages 1-2) |
| Genetics or testing | Variant class: point variants overall | 87% of TBX5-positive probands | Vanlerberghe 2019; 78 TBX5-variant probands | Majority of pathogenic findings were sequence-level variants (vanlerberghe2019holtoramsyndromeclinical pages 2-4) |
| Genetics or testing | Variant class: nonsense | 37% | Vanlerberghe 2019; 78 TBX5-variant probands | Truncating variants predominated (vanlerberghe2019holtoramsyndromeclinical pages 2-4, vanlerberghe2019holtoramsyndromeclinical pages 5-7) |
| Genetics or testing | Variant class: frameshift | 26% | Vanlerberghe 2019; 78 TBX5-variant probands | Supports haploinsufficiency as major mechanism (vanlerberghe2019holtoramsyndromeclinical pages 2-4) |
| Genetics or testing | Variant class: splice-site | 10% | Vanlerberghe 2019; 78 TBX5-variant probands | Includes functionally important noncanonical splice effects in broader literature (vanlerberghe2019holtoramsyndromeclinical pages 2-4) |
| Genetics or testing | Variant class: missense | ~14% | Vanlerberghe 2019; 78 TBX5-variant probands | Some missense variants were de novo and functionally validated (vanlerberghe2019holtoramsyndromeclinical pages 2-4) |
| Genetics or testing | Copy-number variants: intragenic deletions | 8% | Vanlerberghe 2019; 78 TBX5-variant probands | Detected by MLPA; supports CNV analysis in diagnostics (vanlerberghe2019holtoramsyndromeclinical pages 2-4) |
| Genetics or testing | Copy-number variants: intragenic duplications | 4% | Vanlerberghe 2019; 78 TBX5-variant probands | Important atypical mechanism; argues for dosage-sensitive disease biology (vanlerberghe2019holtoramsyndromeclinical pages 2-4, bosada2023anatrialfibrillationassociated pages 23-24) |
| Genetics or testing | Reduced penetrance or mosaicism | 4 asymptomatic carrier parents; 1 father with ~10% somatic mosaicism in blood | Vanlerberghe 2019; familial cases within cohort | Important for counseling and interpretation of negative or atypical family histories (vanlerberghe2019holtoramsyndromeclinical pages 2-4) |


*Table: This table compiles core clinical frequencies and genetic testing findings for Holt-Oram syndrome from the largest 2019 TBX5-positive cohort and a recent single-center clinical series. It is useful for quickly comparing phenotype prevalence, arrhythmia burden, and the distribution of TBX5 variant classes relevant to diagnosis and counseling.*

### 3.3 Age of onset, severity, progression
* **Onset** is congenital (structural limb/cardiac malformations); however, **arrhythmias and conduction disease may appear “over the course of life”** (vanlerberghe2019holtoramsyndromeclinical pages 1-2).
* Adult presentation can occur; a 49-year-old presented with de novo congestive heart failure and atrial flutter plus ASD (Atlas 2024; URL: https://doi.org/10.1186/s43044-024-00549-4) (atlas2024whentheheart pages 1-3).
* Conduction abnormalities may be evident at birth and can progress unpredictably toward advanced block; arrhythmias (including AF, WPW) are described (dmowski2025holtoramsyndromewhen pages 5-8).

### 3.4 Quality-of-life impact
Direct QoL instrument data (e.g., SF-36/EQ-5D) were not found in the retrieved evidence. Functional impact is inferred from the frequency of mobility limitation and need for orthopedic surgery (e.g., orthopaedic surgery reported in ~25% in one cohort) (vanlerberghe2019holtoramsyndromeclinical pages 4-5).

### 3.5 Suggested HPO terms (examples)
**Skeletal/limb:**
* Abnormality of the thumb (HP:0009601)
* Triphalangeal thumb (HP:0001199)
* Thenar hypoplasia (HP:0001182)
* Radial ray defect (HP:0002980)
* Abnormal forearm pronation/supination (HP:0004046)
* Upper limb reduction defect (HP:0009828)

**Cardiac structural:**
* Atrial septal defect (HP:0001631)
* Ventricular septal defect (HP:0001629)

**Conduction/rhythm:**
* Atrial fibrillation (HP:0005110)
* Atrial flutter (HP:0001658)
* Atrioventricular block (HP:0001678)
* Sinus bradycardia (HP:0001688)

(These suggestions are consistent with phenotypes described in cohorts/cases) (vanlerberghe2019holtoramsyndromeclinical pages 4-5, dmowski2025holtoramsyndromewhen pages 5-8, atlas2024whentheheart pages 1-3).

## 4. Genetic / molecular information
### 4.1 Causal gene
* **TBX5** is the principal causal gene (chromosome 12q24) encoding a T-box transcription factor essential for heart and forelimb development (vanlerberghe2019holtoramsyndromeclinical pages 1-2, dmowski2025holtoramsyndromewhen pages 5-8).

### 4.2 Pathogenic variant spectrum and interpretation
**Testing yield and heterogeneity:** among patients referred for suspected HOS and screened for TBX5, detection yields vary; one large referral series reported 58% overall yield (and higher in clinically “classic” subgroups) (vanlerberghe2019holtoramsyndromeclinical pages 2-4).

**Variant types:** truncating variants are common; CNVs (intragenic deletions/duplications) occur and should be explicitly assayed (vanlerberghe2019holtoramsyndromeclinical pages 2-4).

**Functional consequence:** haploinsufficiency is widely supported as a dominant mechanism; reviews and cohorts explicitly refer to TBX5 haploinsufficiency (dmowski2025holtoramsyndromewhen pages 5-8).

### 4.3 Modifier genes
No validated modifier genes specific to HOS severity were identified in the retrieved evidence; however, TBX5 interacts functionally with other cardiac regulators (see Mechanism).

### 4.4 Epigenetic/regulatory mechanisms relevant to disease expression
Noncoding regulatory changes can modulate TBX5 dosage and phenotype risk. In a 2023 eLife paper (published 2023-01-30; URL: https://doi.org/10.7554/eLife.80317), the authors note TBX5 is dosage-sensitive and show that deletion of AF-associated regulatory regions near Tbx5 causes a modest ~30% atrial increase in Tbx5 and increases arrhythmia susceptibility (bosada2023anatrialfibrillationassociated pages 1-2).

### 4.5 Chromosomal abnormalities
Intragenic deletions/duplications in TBX5 are documented by MLPA in HOS cohorts (vanlerberghe2019holtoramsyndromeclinical pages 2-4). A microdeletion spanning TBX5/TBX3 is also described in a Spanish-language series (cruz2026síndromedeholtoram pages 50-54).

## 5. Environmental information
No infectious, lifestyle, or toxic environmental causes of HOS were identified in the retrieved evidence; HOS is best supported as a genetic developmental disorder.

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (developmental biology to clinical disease)
1) **Primary trigger:** germline TBX5 dosage/function change (often loss-of-function; sometimes dosage increase or missense with altered binding/cooperativity) (vanlerberghe2019holtoramsyndromeclinical pages 2-4, bosada2023anatrialfibrillationassociated pages 1-2).
2) **Upstream developmental disruption:** impaired transcriptional control of cardiogenesis and forelimb initiation/patterning; TBX5 is required for septation and conduction system development and is forelimb-specific during limb development (vanlerberghe2019holtoramsyndromeclinical pages 1-2).
3) **Downstream tissue outcomes:** septal CHD (ASD/VSD), conduction system dysfunction/arrhythmias, and radial-ray limb malformations (vanlerberghe2019holtoramsyndromeclinical pages 4-5, dmowski2025holtoramsyndromewhen pages 5-8).

### 6.2 Recent mechanistic developments (prioritizing 2023–2024)
**(i) Small TBX5 dosage increases from noncoding variation can be arrhythmogenic (2023).**
Bosada et al. (*eLife*, published 2023-01-30; https://doi.org/10.7554/eLife.80317) state: “Heart development and rhythm control are highly Tbx5 dosage-sensitive. TBX5 haploinsufficiency causes congenital conduction disorders…” and show that deleting two AF-associated regulatory regions causes a “modest (30%) increase of Tbx5 in the postnatal atria” with “increased susceptibility to atrial arrhythmias” and “increased action potential duration” (bosada2023anatrialfibrillationassociated pages 1-2).

**(ii) TBX5 enhancer-network regulation maintains atrial identity (2023).**
A 2023 study in *Nature Cardiovascular Research* (Sweat et al., Oct 2023; https://doi.org/10.1038/s44161-023-00334-7) investigated TBX5 function with multi-omic profiling (scRNA/ATAC and chromatin interaction mapping) and provides direct support that atrial TBX5 regulates atrial-specific enhancer networks in postnatal cardiomyocytes (sweat2023tbx5maintainsatrial pages 1-2).

### 6.3 Expert/authoritative interpretation (high-quality sources)
A mechanistically detailed example of how a specific TBX5 missense variant can rewire the atrial regulatory network is provided by van Ouwerkerk et al. (*Circulation*, published 2022-02-22; https://doi.org/10.1161/circulationaha.121.054347). In their abstract they report: “We discovered high incidence of atrial extra systoles and atrioventricular conduction disturbances in Holt–Oram syndrome patients” and that atrial transcriptional profiling identified “over a thousand coding and noncoding transcripts” differentially expressed, with “thousands” of variant-sensitive regulatory elements gaining accessibility (ouwerkerk2022patientspecifictbx5g125rvariant pages 1-2).

### 6.4 Pathways, cellular processes, and suggested ontology terms
**Representative GO Biological Process terms (suggested):**
* heart development; cardiac septum development; regulation of transcription by RNA polymerase II; cardiac conduction; limb development.

**Representative cell types (Cell Ontology; suggested):**
* cardiomyocyte; cardiac conduction system cell; cardiac fibroblast (relevant in multi-cell-type profiling, though effects were strongest in cardiomyocytes in the TBX5-G125R model) (ouwerkerk2022patientspecifictbx5g125rvariant pages 1-2).

## 7. Anatomical structures affected
**Primary organ systems:**
* **Heart** (septum; conduction system; atria) (vanlerberghe2019holtoramsyndromeclinical pages 4-5, bosada2023anatrialfibrillationassociated pages 1-2).
* **Upper limbs** (thumb/thenar/carpal/radius/forearm) (vanlerberghe2019holtoramsyndromeclinical pages 4-5, dmowski2025holtoramsyndromewhen pages 5-8).

**Suggested UBERON (examples):** heart (UBERON:0000948), atrial septum, ventricular septum; forelimb/upper limb (UBERON:0001460), radius (UBERON:0001423), thumb (UBERON:0002398).

## 8. Temporal development
**Onset pattern:** congenital structural anomalies; arrhythmias/conduction disease may be detected at birth or emerge later (dmowski2025holtoramsyndromewhen pages 5-8, vanlerberghe2019holtoramsyndromeclinical pages 1-2).

**Course:** lifelong condition requiring continued cardiac surveillance; progression to heart failure/pulmonary hypertension/arrhythmia complications is described in clinical reviews (dmowski2025holtoramsyndromewhen pages 8-12).

## 9. Inheritance and population
### 9.1 Epidemiology
* **Prevalence/incidence:** estimated around **1 in 100,000 births** (Vanlerberghe 2019) (vanlerberghe2019holtoramsyndromeclinical pages 1-2). A review cites ~**0.95 per 100,000 births** from a single population study in Hungary (dmowski2025holtoramsyndromewhen pages 1-5).
* **Sex/ancestry distribution:** one review states equal frequency between males and females and across racial/ethnic groups, while noting limited population-based data (dmowski2025holtoramsyndromewhen pages 1-5).

### 9.2 Inheritance pattern, penetrance, expressivity
* **Autosomal dominant** inheritance (vanlerberghe2019holtoramsyndromeclinical pages 1-2).
* **High penetrance** with **variable expressivity** is emphasized in GeneReviews-like summaries and cohorts; reduced penetrance is documented by asymptomatic carriers and mosaicism (vanlerberghe2019holtoramsyndromeclinical pages 2-4, vanlerberghe2019holtoramsyndromeclinical pages 1-2).

## 10. Diagnostics
### 10.1 Clinical criteria and diagnostic approach
A practical criteria set used in cohort work requires **preaxial/radial upper-limb defect (uni/bilateral) plus personal/family history of CHD and/or rhythm disturbance**, and the diagnosis can be challenging due to overlap with Okihiro, TAR, and Fanconi anemia (vanlerberghe2019holtoramsyndromeclinical pages 1-2).

### 10.2 Testing modalities (real-world)
**Cardiac:** ECG and echocardiography are central; ECG is required because conduction disease can occur without structural heart disease (dmowski2025holtoramsyndromewhen pages 5-8). Echo identifies septal defects and other CHD (vanlerberghe2019holtoramsyndromeclinical pages 4-5).

**Skeletal:** clinical limb exam plus radiography; subtle cases may show only delayed carpal maturation, motivating wrist radiographs (dmowski2025holtoramsyndromewhen pages 8-12).

**Genetic testing:**
* TBX5 sequencing of coding exons and splice junctions plus **copy-number analysis** (e.g., MLPA) is supported by the documented CNV fraction (vanlerberghe2019holtoramsyndromeclinical pages 2-4).

### 10.3 Differential diagnosis
Key differentials include Okihiro (SALL4), TAR syndrome, Fanconi anemia, teratogen exposure (thalidomide, valproate), and other heart–hand / radial ray syndromes (dmowski2025holtoramsyndromewhen pages 5-8, atlas2024whentheheart pages 5-6).

### 10.4 Screening (prenatal)
Prenatal imaging windows cited include visibility of radius/ulna by ~13–16 weeks and many cardiac defects by ~18–20 weeks (dmowski2025holtoramsyndromewhen pages 8-12). Molecular confirmation can inform pregnancy decision-making and neonatal delivery planning (dmowski2025holtoramsyndromewhen pages 8-12).

## 11. Outcome / prognosis
Prognosis is largely determined by cardiac involvement. Atlas 2024 states “Vital prognosis depends essentially on cardiac involvement, while skeletal malformations determine functional prognosis” (atlas2024whentheheart pages 1-3). Heart failure and arrhythmias can occur, and clinical reviews cite risks including sudden cardiac death, supporting lifelong surveillance (dmowski2025holtoramsyndromewhen pages 8-12).

## 12. Treatment
### 12.1 Standard of care (symptom-directed)
There is no disease-specific curative therapy; management is individualized and multidisciplinary (genetics, cardiology, orthopedics/hand surgery, rehabilitation) (dmowski2025holtoramsyndromewhen pages 8-12).

**Cardiac structural defects:** many patients require ASD/VSD repair in childhood (dmowski2025holtoramsyndromewhen pages 8-12).

**Arrhythmia/conduction disease:** may require medications, electrophysiology procedures, or pacemaker implantation; a review notes absence of specific pacing guidelines and reports individualized physiological His-bundle pacing in a symptomatic bradycardia case (dmowski2025holtoramsyndromewhen pages 8-12).

**Heart failure therapy (real-world example, 2024):** in an adult case, guideline-based pharmacologic therapy (diuretics, ACE inhibitor, beta-blocker, MRA, SGLT2 inhibitor) was used with short-term clinical improvement (atlas2024whentheheart pages 3-5).

**Supportive/rehab:** physiotherapy and occupational therapy are frequently used for functional impairment (dmowski2025holtoramsyndromewhen pages 8-12).

**Suggested MAXO terms (examples):** surgical repair of atrial septal defect; cardiac electrophysiological ablation; pacemaker implantation; physical therapy; genetic counseling.

### 12.2 Experimental / clinical trials
No interventional HOS-specific therapeutic trials were identified in the retrieved ClinicalTrials.gov set; retrieved studies were observational and not clearly HOS-targeted.

## 13. Prevention
### 13.1 Genetic counseling and reproductive prevention
A concrete real-world implementation is **PGT-M** for a familial TBX5 pathogenic variant. Economou et al. (Hellenic J Obstet Gynecol, published 2025-01; https://doi.org/10.33574/hjog.0584) report: “Preimplantation genetic testing for monogenic/single-gene defects (PGT-M) is a well established tool in assisted reproduction” and screened **10 embryos**, identifying **4 unaffected embryos**, leading to a live birth after transfer of an unaffected blastocyst (economou2025firstlivebirth pages 1-3).

### 13.2 Secondary/tertiary prevention
Lifelong rhythm and structural surveillance (ECG/echo-based monitoring) is emphasized in clinical reviews to prevent or mitigate arrhythmia and heart failure complications (dmowski2025holtoramsyndromewhen pages 8-12).

## 14. Other species / natural disease
No naturally occurring veterinary HOS analogs were identified in the retrieved evidence.

## 15. Model organisms
### 15.1 Mouse models (key recent examples)
* **Noncoding regulatory element deletion models (2023):** deletion of AF-associated regulatory regions near Tbx5 modestly increased atrial Tbx5 expression (~30%) and increased atrial arrhythmia susceptibility, linking cis-regulatory variation to electrophysiology phenotypes (Bosada et al., eLife 2023-01-30; https://doi.org/10.7554/eLife.80317) (bosada2023anatrialfibrillationassociated pages 1-2).

* **Patient-specific missense knock-in model (2022):** Tbx5G125R/+ mice recapitulate atrial ectopy and AF susceptibility and show large-scale transcriptional/epigenetic perturbations (van Ouwerkerk et al., Circulation 2022-02-22; https://doi.org/10.1161/circulationaha.121.054347) (ouwerkerk2022patientspecifictbx5g125rvariant pages 1-2).

### 15.2 Patient-derived iPSC models
A 2023 report describes single-cell RNA-seq comparison of cardiac progenitor cells from an HOS patient iPSC line and an isogenic CRISPR-corrected line, indicating an emerging platform for mechanism and therapeutic exploration; however, detailed results were not available in the excerpted text (dressen2023comparativesinglecellrnaseq pages 1-2).

## Key data points (quick list)
* Prevalence ~**1/100,000 births** (vanlerberghe2019holtoramsyndromeclinical pages 1-2).
* In TBX5-confirmed cohort (n=78 probands): **ASD 61.5%**, **VSD 34.6%**, conduction disturbances **~29.6%** among evaluable patients (vanlerberghe2019holtoramsyndromeclinical pages 4-5).
* Variant spectrum in TBX5-positive probands: truncating variants predominate (nonsense 37%, frameshift 26%, splice-site 10%); CNVs (deletions 8%, duplications 4%) support including CNV testing (vanlerberghe2019holtoramsyndromeclinical pages 2-4).
* 2023 mechanistic advance: modest (~30%) atrial TBX5 increase from noncoding regulatory perturbation increases arrhythmia susceptibility (bosada2023anatrialfibrillationassociated pages 1-2).

## Notes on missing identifiers (knowledge base population)
The evidence retrieved here did not include Orphanet, ICD-10/11, MeSH, or MONDO identifiers in citable text; these should be added by querying the corresponding databases directly.


References

1. (vanlerberghe2019holtoramsyndromeclinical pages 1-2): Clémence Vanlerberghe, Anne-Sophie Jourdain, Jamal Ghoumid, Frédéric Frenois, Aurélie Mezel, Guy Vaksmann, Bruno Lenne, Bruno Delobel, Nicole Porchet, Valérie Cormier-Daire, Thomas Smol, Fabienne Escande, Sylvie Manouvrier-Hanu, and Florence Petit. Holt-oram syndrome: clinical and molecular description of 78 patients with tbx5 variants. European Journal of Human Genetics, 27:360-368, Dec 2019. URL: https://doi.org/10.1038/s41431-018-0303-3, doi:10.1038/s41431-018-0303-3. This article has 67 citations and is from a domain leading peer-reviewed journal.

2. (atlas2024whentheheart pages 1-3): Ilyas Atlas, Soukaina Zagdan, Mohamed Megzari, Salim Arous, and Abdenasser Drighil. When the heart and hands tell a story: an intriguing case of holt–oram syndrome. The Egyptian Heart Journal, Sep 2024. URL: https://doi.org/10.1186/s43044-024-00549-4, doi:10.1186/s43044-024-00549-4. This article has 2 citations.

3. (dmowski2025holtoramsyndromewhen pages 8-12): Daniel Dmowski, Michał Świda, Jakub Bazarewicz, Cezary Kubuj, Grzegorz Adaśko, Urszula Mazur, Marcin Siwik, Anna Michalska, Paulina Ogonowska, and Julia Waszak. Holt-oram syndrome: when hand deformity leads to diagnosis of congenital heart disease. Quality in Sport, 45:66549, Nov 2025. URL: https://doi.org/10.12775/qs.2025.45.66549, doi:10.12775/qs.2025.45.66549. This article has 0 citations.

4. (vanlerberghe2019holtoramsyndromeclinical pages 4-5): Clémence Vanlerberghe, Anne-Sophie Jourdain, Jamal Ghoumid, Frédéric Frenois, Aurélie Mezel, Guy Vaksmann, Bruno Lenne, Bruno Delobel, Nicole Porchet, Valérie Cormier-Daire, Thomas Smol, Fabienne Escande, Sylvie Manouvrier-Hanu, and Florence Petit. Holt-oram syndrome: clinical and molecular description of 78 patients with tbx5 variants. European Journal of Human Genetics, 27:360-368, Dec 2019. URL: https://doi.org/10.1038/s41431-018-0303-3, doi:10.1038/s41431-018-0303-3. This article has 67 citations and is from a domain leading peer-reviewed journal.

5. (economou2025firstlivebirth pages 1-3): Konstantinos A. Economou, Chrysanthi Bili, Lina Florentin, Fotios Thymis, and Dimitrios Papanicolaou. First live birth in greece after blastocyst trophectoderm biopsy and preimplantation genetic testing for holt-oram syndrome. Hellenic Journal of Obstetrics and Gynecology, 24:55-61, Jan 2025. URL: https://doi.org/10.33574/hjog.0584, doi:10.33574/hjog.0584. This article has 0 citations.

6. (ouwerkerk2022patientspecifictbx5g125rvariant pages 1-2): Antoinette F. van Ouwerkerk, Fernanda M. Bosada, Karel van Duijvenboden, Arjan C. Houweling, Koen T. Scholman, Vincent Wakker, Cornelis P. Allaart, Jae-Sun Uhm, Inge B. Mathijssen, Ton Baartscheer, Alex V. Postma, Phil Barnett, Arie O. Verkerk, Bastiaan J. Boukens, and Vincent M. Christoffels. Patient-specific tbx5-g125r variant induces profound transcriptional deregulation and atrial dysfunction. Circulation, 145:606-619, Feb 2022. URL: https://doi.org/10.1161/circulationaha.121.054347, doi:10.1161/circulationaha.121.054347. This article has 40 citations and is from a highest quality peer-reviewed journal.

7. (liu2026experiencewithpatients pages 1-2): Xuechen Liu, Lei Yang, Jian Cui, Mengqian Liao, Zonghui Hou, Mengqi Zhao, and Lianyi Wang. Experience with patients presenting with the clinical features of holt-oram syndrome: a single center retrospective study. Journal of Cardiothoracic Surgery, Mar 2026. URL: https://doi.org/10.1186/s13019-026-03913-4, doi:10.1186/s13019-026-03913-4. This article has 0 citations and is from a peer-reviewed journal.

8. (bosada2023anatrialfibrillationassociated pages 1-2): Fernanda M Bosada, Karel van Duijvenboden, Alexandra E Giovou, Mathilde R Rivaud, Jae-Sun Uhm, Arie O Verkerk, Bastiaan J Boukens, and Vincent M Christoffels. An atrial fibrillation-associated regulatory region modulates cardiac tbx5 levels and arrhythmia susceptibility. eLife, Jan 2023. URL: https://doi.org/10.7554/elife.80317, doi:10.7554/elife.80317. This article has 14 citations and is from a domain leading peer-reviewed journal.

9. (dmowski2025holtoramsyndromewhen pages 5-8): Daniel Dmowski, Michał Świda, Jakub Bazarewicz, Cezary Kubuj, Grzegorz Adaśko, Urszula Mazur, Marcin Siwik, Anna Michalska, Paulina Ogonowska, and Julia Waszak. Holt-oram syndrome: when hand deformity leads to diagnosis of congenital heart disease. Quality in Sport, 45:66549, Nov 2025. URL: https://doi.org/10.12775/qs.2025.45.66549, doi:10.12775/qs.2025.45.66549. This article has 0 citations.

10. (liu2026experiencewithpatients pages 4-6): Xuechen Liu, Lei Yang, Jian Cui, Mengqian Liao, Zonghui Hou, Mengqi Zhao, and Lianyi Wang. Experience with patients presenting with the clinical features of holt-oram syndrome: a single center retrospective study. Journal of Cardiothoracic Surgery, Mar 2026. URL: https://doi.org/10.1186/s13019-026-03913-4, doi:10.1186/s13019-026-03913-4. This article has 0 citations and is from a peer-reviewed journal.

11. (vanlerberghe2019holtoramsyndromeclinical pages 2-4): Clémence Vanlerberghe, Anne-Sophie Jourdain, Jamal Ghoumid, Frédéric Frenois, Aurélie Mezel, Guy Vaksmann, Bruno Lenne, Bruno Delobel, Nicole Porchet, Valérie Cormier-Daire, Thomas Smol, Fabienne Escande, Sylvie Manouvrier-Hanu, and Florence Petit. Holt-oram syndrome: clinical and molecular description of 78 patients with tbx5 variants. European Journal of Human Genetics, 27:360-368, Dec 2019. URL: https://doi.org/10.1038/s41431-018-0303-3, doi:10.1038/s41431-018-0303-3. This article has 67 citations and is from a domain leading peer-reviewed journal.

12. (vanlerberghe2019holtoramsyndromeclinical pages 5-7): Clémence Vanlerberghe, Anne-Sophie Jourdain, Jamal Ghoumid, Frédéric Frenois, Aurélie Mezel, Guy Vaksmann, Bruno Lenne, Bruno Delobel, Nicole Porchet, Valérie Cormier-Daire, Thomas Smol, Fabienne Escande, Sylvie Manouvrier-Hanu, and Florence Petit. Holt-oram syndrome: clinical and molecular description of 78 patients with tbx5 variants. European Journal of Human Genetics, 27:360-368, Dec 2019. URL: https://doi.org/10.1038/s41431-018-0303-3, doi:10.1038/s41431-018-0303-3. This article has 67 citations and is from a domain leading peer-reviewed journal.

13. (liu2026experiencewithpatients pages 2-4): Xuechen Liu, Lei Yang, Jian Cui, Mengqian Liao, Zonghui Hou, Mengqi Zhao, and Lianyi Wang. Experience with patients presenting with the clinical features of holt-oram syndrome: a single center retrospective study. Journal of Cardiothoracic Surgery, Mar 2026. URL: https://doi.org/10.1186/s13019-026-03913-4, doi:10.1186/s13019-026-03913-4. This article has 0 citations and is from a peer-reviewed journal.

14. (bosada2023anatrialfibrillationassociated pages 23-24): Fernanda M Bosada, Karel van Duijvenboden, Alexandra E Giovou, Mathilde R Rivaud, Jae-Sun Uhm, Arie O Verkerk, Bastiaan J Boukens, and Vincent M Christoffels. An atrial fibrillation-associated regulatory region modulates cardiac tbx5 levels and arrhythmia susceptibility. eLife, Jan 2023. URL: https://doi.org/10.7554/elife.80317, doi:10.7554/elife.80317. This article has 14 citations and is from a domain leading peer-reviewed journal.

15. (cruz2026síndromedeholtoram pages 50-54): MC CRUZ. Síndrome de holt-oram: descripción clínica y molecular en un grupo de pacientes con defectos en miembros superiores asociados a cardiopatía congénita. Unknown journal, 2026.

16. (sweat2023tbx5maintainsatrial pages 1-2): Mason E. Sweat, Yangpo Cao, Xiaoran Zhang, Ozanna Burnicka-Turek, Carlos Perez-Cervantes, Arulsamy Kulandaisamy, Fujian Lu, Erin M. Keating, Brynn N. Akerberg, Qing Ma, Hiroko Wakimoto, Joshua M. Gorham, Lauren D. Hill, Mi Kyoung Song, Michael A. Trembley, Peizhe Wang, Matteo Gianeselli, Maksymilian Prondzynski, Raul H. Bortolin, Vassilios J. Bezzerides, Kaifu Chen, Jonathan G. Seidman, Christine E. Seidman, Ivan P. Moskowitz, and William T. Pu. Tbx5 maintains atrial identity in postnatal cardiomyocytes by regulating an atrial-specific enhancer network. Nature Cardiovascular Research, 2:881-898, Oct 2023. URL: https://doi.org/10.1038/s44161-023-00334-7, doi:10.1038/s44161-023-00334-7. This article has 33 citations and is from a peer-reviewed journal.

17. (dmowski2025holtoramsyndromewhen pages 1-5): Daniel Dmowski, Michał Świda, Jakub Bazarewicz, Cezary Kubuj, Grzegorz Adaśko, Urszula Mazur, Marcin Siwik, Anna Michalska, Paulina Ogonowska, and Julia Waszak. Holt-oram syndrome: when hand deformity leads to diagnosis of congenital heart disease. Quality in Sport, 45:66549, Nov 2025. URL: https://doi.org/10.12775/qs.2025.45.66549, doi:10.12775/qs.2025.45.66549. This article has 0 citations.

18. (atlas2024whentheheart pages 5-6): Ilyas Atlas, Soukaina Zagdan, Mohamed Megzari, Salim Arous, and Abdenasser Drighil. When the heart and hands tell a story: an intriguing case of holt–oram syndrome. The Egyptian Heart Journal, Sep 2024. URL: https://doi.org/10.1186/s43044-024-00549-4, doi:10.1186/s43044-024-00549-4. This article has 2 citations.

19. (atlas2024whentheheart pages 3-5): Ilyas Atlas, Soukaina Zagdan, Mohamed Megzari, Salim Arous, and Abdenasser Drighil. When the heart and hands tell a story: an intriguing case of holt–oram syndrome. The Egyptian Heart Journal, Sep 2024. URL: https://doi.org/10.1186/s43044-024-00549-4, doi:10.1186/s43044-024-00549-4. This article has 2 citations.

20. (dressen2023comparativesinglecellrnaseq pages 1-2): M. Dreßen, H. Lahm, F. Wirth, I. Neb, C. Abou-Ajram, E. Dzilic, S. Doppler, and R. Lange. Comparative single-cell rnaseq analysis of cardiac progenitor cells from a holt-oram syndrome patient ips line and the crispr/cas9 corrected isogenic ips line. The Thoracic and Cardiovascular Surgeon, Jan 2023. URL: https://doi.org/10.1055/s-0043-1761827, doi:10.1055/s-0043-1761827. This article has 0 citations.
