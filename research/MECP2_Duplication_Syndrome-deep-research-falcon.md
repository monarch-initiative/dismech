---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-09T11:37:58.038474'
end_time: '2026-05-09T11:54:46.571822'
duration_seconds: 1008.53
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: MECP2 Duplication Syndrome
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 22
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** MECP2 Duplication Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **MECP2 Duplication Syndrome** covering all of the
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
- **Disease Name:** MECP2 Duplication Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **MECP2 Duplication Syndrome** covering all of the
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


## MECP2 Duplication Syndrome (MDS) — Disease Characteristics Research Report

### Target Disease
- **Disease name:** MECP2 duplication syndrome (MDS)
- **Category:** Genetic; X-linked copy-number gain disorder
- **MONDO ID:** Not identified in the retrieved sources (will require lookup in MONDO/OLS outside this tool run).

### Executive overview (current understanding)
MECP2 duplication syndrome is a rare X-linked neurodevelopmental disorder caused by genomic copy-number gains spanning **MECP2** at **Xq28**, leading to increased MeCP2 dosage (and often duplication of adjacent genes such as **IRAK1**) and resulting in a severe developmental encephalopathy phenotype predominantly affecting males. Core manifestations include early hypotonia, global developmental delay/intellectual disability with minimal/absent speech, progressive spasticity, epilepsy (often refractory), recurrent respiratory infections (often aspiration-related), gastrointestinal dysmotility/constipation, and autonomic/vasomotor disturbances. (ta2022abriefhistory pages 1-2, pehlivan2024structuralvariantallelic pages 1-2, percy2023currentstatusof pages 11-15, ta2022medicalcomorbiditiesin pages 6-7)

Recent (2024) large-scale genotype–phenotype work emphasizes that **both MECP2 dosage level and the structural class of the rearrangement (duplication vs triplication and complex forms)** contribute to clinical severity and survival. (pehlivan2024structuralvariantallelic pages 1-2, pehlivan2024structuralvariantallelic media 2e1d3f3a, pehlivan2024structuralvariantallelic media 2a375656)

---

## 1. Disease Information

### What is the disease?
- **Definition:** A rare X-linked neurodevelopmental disorder caused by **duplication (or triplication) of a chromosomal region on Xq28 that includes MECP2**, producing MeCP2 overexpression and a characteristic syndromic phenotype. (ta2022abriefhistory pages 1-2, pehlivan2024structuralvariantallelic pages 1-2)

### Key identifiers (from retrieved literature)
- **Disease OMIM/MIM:** **300260** (MDS; also MRXSL). (ta2022abriefhistory pages 1-2, pehlivan2024structuralvariantallelic pages 1-2)
- **Gene OMIM (MECP2):** **300005**. (ta2022abriefhistory pages 1-2)
- **Orphanet / ICD-10 / ICD-11 / MeSH / MONDO:** Not explicitly stated in the retrieved full-text evidence; requires external ontology lookups (OMIM/Orphanet/MeSH/MONDO/ICD) beyond this run.

### Synonyms / alternative names
- **X-linked intellectual developmental disorder, Lubs type (MRXSL)** (explicitly stated). (pehlivan2024structuralvariantallelic pages 1-2)
- **MECP2 duplication disorder (MDD)** used in some reviews. (percy2023currentstatusof pages 11-15)

### Evidence type note
Evidence in this report derives from:
- Aggregated cohort resources/registries (e.g., International MECP2 Duplication Database; population epidemiology) (giudice‐nairn2019theincidenceprevalence pages 1-2, ta2022medicalcomorbiditiesin pages 6-7)
- Prospective/retrospective natural history and caregiver-reported surveys (percy2023currentstatusof pages 11-15, ak2022exploringthecharacteristics pages 1-2)
- Molecular/genomic cohort studies integrating omics and deep phenotyping (pehlivan2024structuralvariantallelic pages 1-2)
- Mechanistic model systems (mouse and iPSC-derived human neurons) (maino2024anirak1mecp2tandem pages 23-26, bajikar2024modelingantisenseoligonucleotide pages 1-2)

---

## 2. Etiology

### Disease causal factors
- **Primary cause:** Germline **copy-number gain** (duplication/triplication; often complex rearrangements) spanning **MECP2** at Xq28. (ta2022abriefhistory pages 1-2, pehlivan2024structuralvariantallelic pages 1-2)
- **Mechanistic principle (“Goldilocks” dosage paradigm):** Under-expression (loss-of-function) causes Rett syndrome, whereas over-expression causes MDS. (percy2023currentstatusof pages 11-15)

### Risk factors
- **Genetic:** Having an Xq28 MECP2 duplication/triplication; most affected males inherit the duplication from carrier mothers, though de novo events occur. (ta2022abriefhistory pages 2-4, giudice‐nairn2019theincidenceprevalence pages 1-2)
- **Sex:** Marked male predominance; females often asymptomatic due to skewed X-inactivation, but affected females exist. (ta2022abriefhistory pages 2-4, giudice‐nairn2019theincidenceprevalence pages 1-2)

### Protective factors
No validated genetic or environmental protective factors were identified in the retrieved corpus.

### Gene–environment interactions
Not specifically delineated in the retrieved evidence; respiratory infections and aspiration risk likely interact with hypotonia, dysphagia, reflux, and seizure severity as downstream clinical-pathophysiologic interactions rather than established etiologic GxE. (ta2022medicalcomorbiditiesin pages 6-7, lim2017expandingtheclinical pages 10-13)

---

## 3. Phenotypes (with quantitative data where available)

### Core neurodevelopmental phenotype
- **Early developmental delay:** In a US natural history cohort (n=69), **70%** had developmental delay in the first 6 months. (percy2023currentstatusof pages 11-15)
- **Hypotonia:** **88%** in the same cohort. (percy2023currentstatusof pages 11-15)
- **Speech:** Little-to-absent speech described as near-universal in reviews; specific quantified rates not extracted from the retrieved pages. (allison2024mecp2relateddisorderswhile pages 4-5)

**Suggested HPO terms** (examples):
- Global developmental delay (**HP:0001263**)
- Intellectual disability (**HP:0001249**)
- Hypotonia (**HP:0001252**)
- Absent speech (**HP:0001344**) / Severely impaired speech (**HP:0002465**)

### Epilepsy
- **Seizures:** In International MECP2 Duplication Database cohort, **>60% (90/148)** had seizures; median onset ~8 years in males and ~9.8 years in females. (ta2022medicalcomorbiditiesin pages 6-7)
- **Treatment refractoriness:** **69%** had treatment-refractory seizures; **31%** had status epilepticus; **25%** had Lennox–Gastaut syndrome. (ta2022medicalcomorbiditiesin pages 6-7)
- Caregiver survey study found epilepsy in **58.4%** of participants and **75% of those were drug-resistant**. (ak2022exploringthecharacteristics pages 1-2)

**Suggested HPO terms**:
- Seizures (**HP:0001250**)
- Epileptic encephalopathy (**HP:0200134**)
- Status epilepticus (**HP:0002133**)
- Lennox-Gastaut syndrome (**HP:0007180**)

### Respiratory infections / aspiration and pulmonary complications
- Australian childhood cohort: **~75% had a history of pneumonia**. (giudice‐nairn2019theincidenceprevalence pages 1-2)
- Registry cohort: aspiration is common—**55% (81/147)** aspirated occasionally/frequently; **23% (33/146)** aspirated into lungs in the past 12 months; **53% (78/146)** could not effectively clear chest secretions. (ta2022medicalcomorbiditiesin pages 6-7)
- Cardiac/pulmonary: pulmonary hypertension is described as a rare but life-threatening complication with reported early death; authors recommend early cardiac assessment and ongoing monitoring. (giudice‐nairn2019theincidenceprevalence pages 1-2)

**Suggested HPO terms**:
- Recurrent respiratory infections (**HP:0002205**)
- Pneumonia (**HP:0002090**)
- Aspiration (**HP:0002835**)
- Pulmonary hypertension (**HP:0002092**)

### Gastrointestinal and feeding phenotype
- Constipation common: in US cohort (n=69) **81% constipation**. (percy2023currentstatusof pages 11-15)
- Caregiver survey: **~85% constipation**, and ~1/3 required enemas/suppositories. (ak2022exploringthecharacteristics pages 1-2)
- GI dysfunction is highlighted as a major domain in MDS and a target for improving QoL. (lim2017expandingtheclinical pages 10-13, allison2024mecp2relateddisorderswhile pages 7-8)

**Suggested HPO terms**:
- Constipation (**HP:0002019**)
- Gastroesophageal reflux (**HP:0002020**)
- Intestinal dysmotility (**HP:0002572**)

### Autonomic/vasomotor and related features
- Registry cohort: **autonomic disturbance 81% (119/146)**; **cold peripheries 70%**, **temperature dysregulation 57%**, **breath holding 38%**, **hyperventilation 13%**. (ta2022medicalcomorbiditiesin pages 6-7)
- US cohort review reports **vasomotor disturbances 73%**. (percy2023currentstatusof pages 11-15)

**Suggested HPO terms**:
- Autonomic nervous system abnormality (**HP:0012332**)
- Cold extremities (**HP:0002046**)
- Breath-holding spells (**HP:0002598**)

### Sleep-disordered breathing and pain sensitivity
- Sleep apnoea: **43% (61/143)**. (ta2022medicalcomorbiditiesin pages 9-10)
- Abnormal pain sensitivity: **59% (85/143)**, with **decreased pain sensitivity 55% (79/143)**. (ta2022medicalcomorbiditiesin pages 9-10)

**Suggested HPO terms**:
- Sleep apnea (**HP:0010535**)
- Abnormality of pain sensation (**HP:0004305**)

### Musculoskeletal/bone health
- Bone fractures: **32% (46/142)**; osteopenia/osteoporosis **13% (19/143)**. (ta2022medicalcomorbiditiesin pages 9-10)

**Suggested HPO terms**:
- Osteopenia (**HP:0011002**)
- Fractures (**HP:0002659**)

### Quality of life impact
Higher clinical severity in MDS correlates with lower physical health QoL in the reviewed US natural history cohort analyses. (percy2023currentstatusof pages 11-15)

---

## 4. Genetic / Molecular Information

### Causal gene(s)
- **MECP2** (Xq28) dosage gain is the core driver. (ta2022abriefhistory pages 1-2, pehlivan2024structuralvariantallelic pages 1-2)
- A commonly implicated minimal duplicated region includes **MECP2 and IRAK1**, supporting potential multi-gene contributions to phenotype. (ta2022abriefhistory pages 2-4, maino2024anirak1mecp2tandem pages 1-5)

### Variant class / chromosomal abnormality
- **Structural class heterogeneity:** In a 2024 cohort (n=137), duplication sizes ranged **64.6 kb–16.5 Mb**, with tandem duplications **48%**, terminal duplications **22%**, inverted triplications **20%**, and other complex rearrangements **10%**. (pehlivan2024structuralvariantallelic pages 1-2)
- Terminal duplications often involve translocations (65%); de novo events enriched in terminal duplication group. (pehlivan2024structuralvariantallelic pages 1-2)

### Functional consequence
- Pathogenic mechanism is **increased MECP2 dosage** (gain of function via overexpression), with higher dosage (triplication) associated with greater severity/early lethality. (pehlivan2024structuralvariantallelic pages 1-2)

### Modifier genes
- Co-duplicated genes (e.g., **IRAK1**, **FLNA**, **HCFC1**, **GDI1**, **RAB39B**) have been associated with differences in severity in cohort analyses/reviews. (percy2023currentstatusof pages 11-15)

---

## 5. Environmental Information
No primary environmental toxins, lifestyle risks, or infectious agents as causal triggers were identified; infections are prominent complications in the disease course. (ta2022medicalcomorbiditiesin pages 6-7, lim2017expandingtheclinical pages 10-13)

---

## 6. Mechanism / Pathophysiology

### Molecular pathways and cellular processes (current model)
1. **Genomic duplication/triplication at Xq28** → increased **MECP2 transcript and protein** (supported by RNA/protein correlation in patient-derived lines). (pehlivan2024structuralvariantallelic pages 1-2)
2. **MeCP2 overabundance** (a methylated-DNA binding transcriptional regulator) perturbs neuronal transcription programs and synaptic function/plasticity. (pehlivan2024structuralvariantallelic pages 1-2, maino2024anirak1mecp2tandem pages 23-26)
3. System-level outcomes: neurodevelopmental impairment, epilepsy, progressive motor dysfunction/spasticity; additionally, immune dysregulation and infection susceptibility may be modified by co-duplication of **IRAK1** and MeCP2’s roles in T cell biology. (maino2024anirak1mecp2tandem pages 1-5, maino2024anirak1mecp2tandem pages 23-26)

### Key mechanistic data (2023–2024 emphasis)
- **Dose–biomolecule link:** MECP2 RNA correlates with MeCP2 protein (Pearson R=0.6) in lymphoblastoid lines; triplications show distinct transcript quantities vs duplications. (pehlivan2024structuralvariantallelic pages 1-2)
- **Genotype–phenotype gradient:** Severity (including survival) worsens across rearrangement classes; visual summary available in Pehlivan 2024 figures/tables. (pehlivan2024structuralvariantallelic media 2a375656, pehlivan2024structuralvariantallelic media 1eb0878d)
- **iPSC-derived neurons (human) and ASO response:** MDS neurons show “global transcriptional dysregulation,” and MECP2-targeting ASO partially modulates a disease gene signature and partially rescues abnormal neuronal morphology. (bajikar2024modelingantisenseoligonucleotide pages 1-2)
- **Mouse tandem-duplication model including Irak1:** Demonstrates neurobehavioral MDS-like phenotype plus an abnormal pro-inflammatory/Th1-skewed response to influenza, with quantified increases in BALF cytokines/chemokines (e.g., IFNγ 6.26-fold; TNFα 2.19-fold). (maino2024anirak1mecp2tandem pages 23-26)

### Suggested ontology mappings
- **GO Biological Process (examples):**
  - Regulation of transcription, DNA-templated (**GO:0006355**)
  - Synaptic plasticity (**GO:0048167**)
  - Long-term synaptic potentiation (**GO:0060291**)
  - T helper 1 type immune response (**GO:0042088**)
- **Cell Ontology (CL) (examples):**
  - Cortical neuron (**CL:0000540**) / pyramidal neuron (context dependent)
  - Hippocampal neuron (subclassing varies)
  - CD4-positive, alpha-beta T cell (**CL:0000624**)
- **UBERON (examples):** brain (**UBERON:0000955**), hippocampus (**UBERON:0001954**), lung (**UBERON:0002048**)

---

## 7. Anatomical Structures Affected
- **Primary system:** Central nervous system (brain; cortical/hippocampal circuits implicated by transcriptional and plasticity phenotypes). (maino2024anirak1mecp2tandem pages 23-26, pehlivan2024structuralvariantallelic pages 1-2)
- **Respiratory system:** recurrent LRTIs/aspiration; pulmonary hypertension risk. (giudice‐nairn2019theincidenceprevalence pages 1-2, ta2022medicalcomorbiditiesin pages 6-7)
- **Gastrointestinal tract:** constipation/dysmotility, reflux. (percy2023currentstatusof pages 11-15, lim2017expandingtheclinical pages 10-13)

---

## 8. Temporal Development
- **Onset:** often infancy (developmental delay in first 6 months, hypotonia early). (percy2023currentstatusof pages 11-15)
- **Epilepsy onset:** median ~8–10 years in registry cohort, with severe seizures often linked to regression. (ta2022medicalcomorbiditiesin pages 6-7, percy2023currentstatusof pages 11-15)
- **Progression:** progressive spasticity and later complications (respiratory morbidity, severe epilepsy) contribute to long-term burden and mortality risk. (ta2022abriefhistory pages 2-4, lim2017expandingtheclinical pages 10-13)

---

## 9. Inheritance and Population

### Inheritance
- **X-linked inheritance**, predominantly maternal transmission; review suggests ~**20% de novo**. (ta2022abriefhistory pages 2-4)
- Australian series: most males inherited from carrier mothers (13/15). (giudice‐nairn2019theincidenceprevalence pages 1-2)

### Epidemiology (recent best-available numbers from retrieved sources)
- **Australia birth prevalence:** **0.65/100,000 all live births** and **1/100,000 males**. (giudice‐nairn2019theincidenceprevalence pages 1-2)
- **Estimated live birth prevalence in males:** **1/150,000** (review estimate). (ta2022abriefhistory pages 1-2)
- **Diagnostic incidence in Australia:** **0.07/100,000 person-years overall**, **0.12/100,000 in males**. (giudice‐nairn2019theincidenceprevalence pages 1-2)

---

## 10. Diagnostics

### Recommended/used genetic tests
- **Chromosomal microarray / array-CGH:** recommended for children with undiagnosed intellectual disability/global developmental delay in the Australian cohort. (giudice‐nairn2019theincidenceprevalence pages 1-2)
- **qPCR:** used historically to detect duplications missed by earlier methods. (ta2022abriefhistory pages 2-4)
- **Karyotyping + WES + CNV-seq:** applied in a 2024 pedigree; CNV-seq confirmed a 14.45 Mb Xq27.1–q28 duplication. (zeng2024geneticanalysisof pages 1-2)
- **Advanced structural characterization + omics:** 2024 Genome Medicine study combined genomics with RNA-seq and deep HPO phenotyping. (pehlivan2024structuralvariantallelic pages 1-2)

### Clinical evaluations/monitoring highlighted
- **Cardiac assessment/monitoring** recommended due to pulmonary hypertension/CHD concerns in MDS cohorts. (giudice‐nairn2019theincidenceprevalence pages 1-2, ta2022medicalcomorbiditiesin pages 9-10)
- Respiratory aspiration risk assessment and airway clearance support frequently needed (aspiration and secretion clearance deficits common). (ta2022medicalcomorbiditiesin pages 6-7)

### Differential diagnosis
No formal differential diagnosis list was extracted from the retrieved sources; closely related disorders discussed in comparative reviews include **Rett syndrome (MECP2 loss-of-function)** and other developmental encephalopathies (CDKL5 deficiency, FOXG1 disorder). (percy2023currentstatusof pages 11-15)

---

## 11. Outcome / Prognosis
- Historical minimal-region cohort summarized in Ta 2022 review: **6/11** individuals died before age 25 in one series (indicative of elevated early mortality risk). (ta2022abriefhistory pages 2-4)
- 2024 genotype–phenotype analyses support that survival and severity worsen with increasing MECP2 dosage and certain rearrangement classes (triplication most severe). (pehlivan2024structuralvariantallelic pages 1-2, pehlivan2024structuralvariantallelic media 2a375656)

---

## 12. Treatment

### Current standard of care (real-world implementation)
Symptomatic/supportive, multidisciplinary care is standard: management of epilepsy, feeding/GI dysmotility (constipation, reflux), and proactive infection prevention/treatment. Supportive respiratory approaches include airway clearance devices and noninvasive ventilation in a subset. Vaccination and prompt antibiotics are emphasized, and immunoglobulin or prophylactic antibiotics may be used for recurrent infections in some patients. (allison2024mecp2relateddisorderswhile pages 7-8, ta2022medicalcomorbiditiesin pages 6-7)

**Suggested MAXO terms (examples):**
- Antiseizure therapy (**MAXO:0000465**) (term may vary)
- Airway clearance therapy (**MAXO:0000747**; check exact MAXO)
- Noninvasive ventilation (**MAXO:0000506**; check exact MAXO)
- Physical therapy (**MAXO:0000011**)

### Emerging disease-modifying therapies (2023–2024 focus)

#### Antisense oligonucleotide (ASO) MECP2-lowering strategies
- **Preclinical rationale:** Normalizing MECP2 dosage with ASOs rescues neurological phenotypes in MECP2 overexpression mouse models. (bajikar2024modelingantisenseoligonucleotide pages 1-2)
- **Human translational evidence (2024):** In MDS patient iPSC-derived neurons, ASO treatment partially rescues gene-expression programs and neuronal morphology. (bajikar2024modelingantisenseoligonucleotide pages 1-2)
- **Key safety concern (expert analysis):** MeCP2 is dose-sensitive—oversuppression risks inducing Rett-like insufficiency; ASOs’ repeat dosing enables titration. (allison2024mecp2relateddisorderswhile pages 7-8, percy2023currentstatusof pages 11-15)

#### Interventional clinical trials
- **ATTUNE — ION440 (Ionis):** Phase 1–2, randomized, double-blind, sham-controlled, multiple-ascending dose trial using **intrathecal bolus** administration; recruiting; start date **2024-10-21** (NCT06430385). (NCT06430385 chunk 1)

#### Biomarker/disease progression characterization (trial readiness)
- **Ionis observational biomarker study:** Terminated after meeting objectives; included CSF and blood collection (lumbar puncture), EEG/evoked potentials/pupillometry, and multiple clinical scales; primary endpoints included **change in MeCP2 in CSF** (NCT06014541). (NCT06014541 chunk 1)

#### Gene therapy and gene-based approaches (expert perspective)
Gene-based therapies must address MECP2’s narrow therapeutic window; experts caution that over-treatment could “convert” toward the opposite dosage disorder, and one-time gene replacement carries irreversibility risk compared with titratable approaches. (allison2024mecp2relateddisorderswhile pages 7-8)

---

## 13. Prevention
No primary prevention is available for a germline CNV disorder beyond **genetic counseling**, carrier testing, and prenatal/preimplantation options where legally/ethically appropriate. Maternal carrier transmission is common, supporting cascade testing in families. (giudice‐nairn2019theincidenceprevalence pages 1-2, ta2022abriefhistory pages 2-4)

---

## 14. Other Species / Natural Disease
No naturally occurring non-human veterinary syndrome was identified in the retrieved sources.

---

## 15. Model Organisms

### Mouse models
- **CRISPR Irak1–Mecp2 tandem duplication mouse (2024):** Designed to mimic patient-like tandem duplication including **Irak1**; shows neurobehavioral phenotypes and abnormal immune response to infection, enabling mechanistic and therapeutic studies. (maino2024anirak1mecp2tandem pages 1-5, maino2024anirak1mecp2tandem pages 23-26)

### Human cellular models
- **Patient iPSC-derived neurons (2024):** Used to evaluate MECP2-targeting ASO effects on transcriptional signatures and neuronal morphology. (bajikar2024modelingantisenseoligonucleotide pages 1-2)

---

## Recent developments and “latest research” highlights (2023–2024)
1. **Large 2024 cohort (n=137) integrating genomics + transcriptomics + deep HPO phenotyping** demonstrates graded severity across rearrangement classes and MECP2 RNA–protein correlation, improving genotype–phenotype resolution and informing trial stratification. (pehlivan2024structuralvariantallelic pages 1-2, pehlivan2024structuralvariantallelic media 1eb0878d)
2. **2024 human iPSC-neuron ASO modeling study** provides a translational bridge between mouse rescue data and human neuronal biology, identifying MeCP2-level-responsive gene programs. (bajikar2024modelingantisenseoligonucleotide pages 1-2)
3. **2024 CRISPR tandem-duplication mouse including Irak1** adds immune dysregulation biology absent from MECP2-only transgenic models, supporting multi-gene contributions to MDS. (maino2024anirak1mecp2tandem pages 1-5, maino2024anirak1mecp2tandem pages 23-26)
4. **Clinical translation (2024 onward):** an intrathecal ASO trial (ION440) has entered Phase 1–2 testing in MDS (NCT06430385), and a terminated observational biomarker study (NCT06014541) indicates active biomarker/trajectory definition by industry sponsors. (NCT06430385 chunk 1, NCT06014541 chunk 1)

---

## Visual evidence (genotype–phenotype)
Pehlivan et al. (Genome Medicine 2024) provide figure/table visual summaries of structural rearrangement classes and phenotype severity ordering across classes (tandem duplications through triplications). (pehlivan2024structuralvariantallelic media 2e1d3f3a, pehlivan2024structuralvariantallelic media 1eb0878d, pehlivan2024structuralvariantallelic media 2a375656)

---

## Notes on gaps / limitations of this tool run
- **Ontology identifiers (MONDO, Orphanet, MeSH, ICD-10/11)** were not present in the retrieved full text chunks and therefore are not asserted here.
- Some phenotype frequencies (e.g., pneumonia/bronchitis/GERD/scoliosis exact prevalence) were described qualitatively in the MDBase abstract, but complete numeric tables were not fully captured in retrieved excerpts; a direct full-text table extraction would improve completeness. (ta2022medicalcomorbiditiesin pages 1-2)
- The CRISPR RNA-editing interventional trial record (NCT06615206) was retrieved earlier but not present in the evidence chunks extracted here; therefore, it is not detailed in this report.




References

1. (ta2022abriefhistory pages 1-2): Daniel Ta, Jenny Downs, Gareth Baynam, Andrew Wilson, Peter Richmond, and Helen Leonard. A brief history of mecp2 duplication syndrome: 20-years of clinical understanding. Orphanet Journal of Rare Diseases, Mar 2022. URL: https://doi.org/10.1186/s13023-022-02278-w, doi:10.1186/s13023-022-02278-w. This article has 64 citations and is from a peer-reviewed journal.

2. (pehlivan2024structuralvariantallelic pages 1-2): Davut Pehlivan, Jesse D. Bengtsson, Sameer S. Bajikar, Christopher M. Grochowski, Ming Yin Lun, Mira Gandhi, Angad Jolly, Alexander J. Trostle, Holly K. Harris, Bernhard Suter, Sukru Aras, Melissa B. Ramocki, Haowei Du, Michele G. Mehaffey, KyungHee Park, Ellen Wilkey, Cemal Karakas, Jesper J. Eisfeldt, Maria Pettersson, Lynn Liu, Marwan S. Shinawi, Virginia E. Kimonis, Wojciech Wiszniewski, Kyle Mckenzie, Timo Roser, Angela M. Vianna-Morgante, Alberto S. Cornier, Ahmed Abdelmoity, James P. Hwang, Shalini N. Jhangiani, Donna M. Muzny, Tadahiro Mitani, Kazuhiro Muramatsu, Shin Nabatame, Daniel G. Glaze, Jawid M. Fatih, Richard A. Gibbs, Zhandong Liu, Anna Lindstrand, Fritz J. Sedlazeck, James R. Lupski, Huda Y. Zoghbi, and Claudia M. B. Carvalho. Structural variant allelic heterogeneity in mecp2 duplication syndrome provides insight into clinical severity and variability of disease expression. Genome Medicine, Dec 2024. URL: https://doi.org/10.1186/s13073-024-01411-7, doi:10.1186/s13073-024-01411-7. This article has 14 citations and is from a highest quality peer-reviewed journal.

3. (percy2023currentstatusof pages 11-15): Alan K. Percy, Jeffrey L. Neul, Sarika Peters, Knut Brockmann, Eric Marsh, and Tim Benke. Current status of developmental encephalopathies: rett syndrome, mecp2 duplication disorder, cdkl5 deficiency disorder and foxg1 disorder. Translational Science of Rare Diseases, 6:73-100, Jul 2023. URL: https://doi.org/10.3233/trd-220055, doi:10.3233/trd-220055. This article has 2 citations.

4. (ta2022medicalcomorbiditiesin pages 6-7): Daniel Ta, Jenny Downs, Gareth Baynam, Andrew Wilson, Peter Richmond, and Helen Leonard. Medical comorbidities in mecp2 duplication syndrome: results from the international mecp2 duplication database. Children, 9:633, Apr 2022. URL: https://doi.org/10.3390/children9050633, doi:10.3390/children9050633. This article has 14 citations.

5. (pehlivan2024structuralvariantallelic media 2e1d3f3a): Davut Pehlivan, Jesse D. Bengtsson, Sameer S. Bajikar, Christopher M. Grochowski, Ming Yin Lun, Mira Gandhi, Angad Jolly, Alexander J. Trostle, Holly K. Harris, Bernhard Suter, Sukru Aras, Melissa B. Ramocki, Haowei Du, Michele G. Mehaffey, KyungHee Park, Ellen Wilkey, Cemal Karakas, Jesper J. Eisfeldt, Maria Pettersson, Lynn Liu, Marwan S. Shinawi, Virginia E. Kimonis, Wojciech Wiszniewski, Kyle Mckenzie, Timo Roser, Angela M. Vianna-Morgante, Alberto S. Cornier, Ahmed Abdelmoity, James P. Hwang, Shalini N. Jhangiani, Donna M. Muzny, Tadahiro Mitani, Kazuhiro Muramatsu, Shin Nabatame, Daniel G. Glaze, Jawid M. Fatih, Richard A. Gibbs, Zhandong Liu, Anna Lindstrand, Fritz J. Sedlazeck, James R. Lupski, Huda Y. Zoghbi, and Claudia M. B. Carvalho. Structural variant allelic heterogeneity in mecp2 duplication syndrome provides insight into clinical severity and variability of disease expression. Genome Medicine, Dec 2024. URL: https://doi.org/10.1186/s13073-024-01411-7, doi:10.1186/s13073-024-01411-7. This article has 14 citations and is from a highest quality peer-reviewed journal.

6. (pehlivan2024structuralvariantallelic media 2a375656): Davut Pehlivan, Jesse D. Bengtsson, Sameer S. Bajikar, Christopher M. Grochowski, Ming Yin Lun, Mira Gandhi, Angad Jolly, Alexander J. Trostle, Holly K. Harris, Bernhard Suter, Sukru Aras, Melissa B. Ramocki, Haowei Du, Michele G. Mehaffey, KyungHee Park, Ellen Wilkey, Cemal Karakas, Jesper J. Eisfeldt, Maria Pettersson, Lynn Liu, Marwan S. Shinawi, Virginia E. Kimonis, Wojciech Wiszniewski, Kyle Mckenzie, Timo Roser, Angela M. Vianna-Morgante, Alberto S. Cornier, Ahmed Abdelmoity, James P. Hwang, Shalini N. Jhangiani, Donna M. Muzny, Tadahiro Mitani, Kazuhiro Muramatsu, Shin Nabatame, Daniel G. Glaze, Jawid M. Fatih, Richard A. Gibbs, Zhandong Liu, Anna Lindstrand, Fritz J. Sedlazeck, James R. Lupski, Huda Y. Zoghbi, and Claudia M. B. Carvalho. Structural variant allelic heterogeneity in mecp2 duplication syndrome provides insight into clinical severity and variability of disease expression. Genome Medicine, Dec 2024. URL: https://doi.org/10.1186/s13073-024-01411-7, doi:10.1186/s13073-024-01411-7. This article has 14 citations and is from a highest quality peer-reviewed journal.

7. (giudice‐nairn2019theincidenceprevalence pages 1-2): Peter Giudice‐Nairn, Jenny Downs, Kingsley Wong, Dylan Wilson, Daniel Ta, Michael Gattas, David Amor, Elizabeth Thompson, Cathy Kirrali‐Borri, Carolyn Ellaway, and Helen Leonard. The incidence, prevalence and clinical features of mecp2 duplication syndrome in australian children. Journal of Paediatrics and Child Health, 55:1315-1322, Nov 2019. URL: https://doi.org/10.1111/jpc.14399, doi:10.1111/jpc.14399. This article has 47 citations and is from a peer-reviewed journal.

8. (ak2022exploringthecharacteristics pages 1-2): Muharrem Ak, Bernhard Suter, Zekeriya Akturk, Holly Harris, Kristina Bowyer, Laurence Mignon, Sasidhar Pasupuleti, Daniel G. Glaze, and Davut Pehlivan. Exploring the characteristics and most bothersome symptoms in mecp2 duplication syndrome to pave the path toward developing parent‐oriented outcome measures. Molecular Genetics & Genomic Medicine, Jun 2022. URL: https://doi.org/10.1002/mgg3.1989, doi:10.1002/mgg3.1989. This article has 10 citations and is from a peer-reviewed journal.

9. (maino2024anirak1mecp2tandem pages 23-26): Eleonora Maino, Ori Scott, Samar Z. Rizvi, Shagana Visuvanathan, Youssif Ben Zablah, Hongbin Li, Ameet S. Sengar, Michael W. Salter, Zhengping Jia, Janet Rossant, Ronald D. Cohn, Bin Gu, and Evgueni A. Ivakine. An irak1-mecp2 tandem duplication mouse model for the study of mecp2 duplication syndrome. Disease Models & Mechanisms, Feb 2024. URL: https://doi.org/10.1101/2023.02.07.527511, doi:10.1101/2023.02.07.527511. This article has 1 citations and is from a domain leading peer-reviewed journal.

10. (bajikar2024modelingantisenseoligonucleotide pages 1-2): Sameer S Bajikar, Yehezkel Sztainberg, Alexander J Trostle, Harini P Tirumala, Ying-Wooi Wan, Caroline L Harrop, Jesse D Bengtsson, Claudia M B Carvalho, Davut Pehlivan, Bernhard Suter, Jeffrey L Neul, Zhandong Liu, Paymaan Jafar-Nejad, Frank Rigo, and Huda Y Zoghbi. Modeling antisense oligonucleotide therapy in <i>mecp2</i> duplication syndrome human ipsc-derived neurons reveals gene expression programs responsive to mecp2 levels. Human Molecular Genetics, 33:1986-2001, Sep 2024. URL: https://doi.org/10.1093/hmg/ddae135, doi:10.1093/hmg/ddae135. This article has 11 citations and is from a domain leading peer-reviewed journal.

11. (ta2022abriefhistory pages 2-4): Daniel Ta, Jenny Downs, Gareth Baynam, Andrew Wilson, Peter Richmond, and Helen Leonard. A brief history of mecp2 duplication syndrome: 20-years of clinical understanding. Orphanet Journal of Rare Diseases, Mar 2022. URL: https://doi.org/10.1186/s13023-022-02278-w, doi:10.1186/s13023-022-02278-w. This article has 64 citations and is from a peer-reviewed journal.

12. (lim2017expandingtheclinical pages 10-13): Zhan Lim, Jenny Downs, Jenny Downs, Kingsley Wong, C. Ellaway, C. Ellaway, and Helen Leonard. Expanding the clinical picture of the mecp2 duplication syndrome. Clinical Genetics, 91:557-563, Apr 2017. URL: https://doi.org/10.1111/cge.12814, doi:10.1111/cge.12814. This article has 67 citations and is from a peer-reviewed journal.

13. (allison2024mecp2relateddisorderswhile pages 4-5): Katherine Allison, Mirjana Maletic-Savatic, and Davut Pehlivan. Mecp2-related disorders while gene-based therapies are on the horizon. Frontiers in Genetics, Feb 2024. URL: https://doi.org/10.3389/fgene.2024.1332469, doi:10.3389/fgene.2024.1332469. This article has 14 citations and is from a peer-reviewed journal.

14. (allison2024mecp2relateddisorderswhile pages 7-8): Katherine Allison, Mirjana Maletic-Savatic, and Davut Pehlivan. Mecp2-related disorders while gene-based therapies are on the horizon. Frontiers in Genetics, Feb 2024. URL: https://doi.org/10.3389/fgene.2024.1332469, doi:10.3389/fgene.2024.1332469. This article has 14 citations and is from a peer-reviewed journal.

15. (ta2022medicalcomorbiditiesin pages 9-10): Daniel Ta, Jenny Downs, Gareth Baynam, Andrew Wilson, Peter Richmond, and Helen Leonard. Medical comorbidities in mecp2 duplication syndrome: results from the international mecp2 duplication database. Children, 9:633, Apr 2022. URL: https://doi.org/10.3390/children9050633, doi:10.3390/children9050633. This article has 14 citations.

16. (maino2024anirak1mecp2tandem pages 1-5): Eleonora Maino, Ori Scott, Samar Z. Rizvi, Shagana Visuvanathan, Youssif Ben Zablah, Hongbin Li, Ameet S. Sengar, Michael W. Salter, Zhengping Jia, Janet Rossant, Ronald D. Cohn, Bin Gu, and Evgueni A. Ivakine. An irak1-mecp2 tandem duplication mouse model for the study of mecp2 duplication syndrome. Disease Models & Mechanisms, Feb 2024. URL: https://doi.org/10.1101/2023.02.07.527511, doi:10.1101/2023.02.07.527511. This article has 1 citations and is from a domain leading peer-reviewed journal.

17. (pehlivan2024structuralvariantallelic media 1eb0878d): Davut Pehlivan, Jesse D. Bengtsson, Sameer S. Bajikar, Christopher M. Grochowski, Ming Yin Lun, Mira Gandhi, Angad Jolly, Alexander J. Trostle, Holly K. Harris, Bernhard Suter, Sukru Aras, Melissa B. Ramocki, Haowei Du, Michele G. Mehaffey, KyungHee Park, Ellen Wilkey, Cemal Karakas, Jesper J. Eisfeldt, Maria Pettersson, Lynn Liu, Marwan S. Shinawi, Virginia E. Kimonis, Wojciech Wiszniewski, Kyle Mckenzie, Timo Roser, Angela M. Vianna-Morgante, Alberto S. Cornier, Ahmed Abdelmoity, James P. Hwang, Shalini N. Jhangiani, Donna M. Muzny, Tadahiro Mitani, Kazuhiro Muramatsu, Shin Nabatame, Daniel G. Glaze, Jawid M. Fatih, Richard A. Gibbs, Zhandong Liu, Anna Lindstrand, Fritz J. Sedlazeck, James R. Lupski, Huda Y. Zoghbi, and Claudia M. B. Carvalho. Structural variant allelic heterogeneity in mecp2 duplication syndrome provides insight into clinical severity and variability of disease expression. Genome Medicine, Dec 2024. URL: https://doi.org/10.1186/s13073-024-01411-7, doi:10.1186/s13073-024-01411-7. This article has 14 citations and is from a highest quality peer-reviewed journal.

18. (zeng2024geneticanalysisof pages 1-2): Lan Zeng, Hui Zhu, Jin Wang, Qiyan Wang, Ying Pang, Zemin Luo, Ai Chen, Shengfang Qin, and Shuyao Zhu. Genetic analysis of a pedigree with mecp2 duplication syndrome in china. BMC Medical Genomics, Feb 2024. URL: https://doi.org/10.1186/s12920-024-01831-9, doi:10.1186/s12920-024-01831-9. This article has 0 citations and is from a peer-reviewed journal.

19. (NCT06430385 chunk 1):  ATTUNE: A Study to Evaluate the Safety, Tolerability, Pharmacokinetics, and Pharmacodynamics of Intrathecally-Administered ION440 in Participants With Methyl CpG Binding Protein 2 (MECP2) Duplication Syndrome (MDS). Ionis Pharmaceuticals, Inc.. 2024. ClinicalTrials.gov Identifier: NCT06430385

20. (NCT06014541 chunk 1):  Observational Study to Characterize Biomarkers and Disease Progression in Participants With Methyl CpG Binding Protein 2 (MECP2) Duplication Syndrome. Ionis Pharmaceuticals, Inc.. 2023. ClinicalTrials.gov Identifier: NCT06014541

21. (ta2022medicalcomorbiditiesin pages 1-2): Daniel Ta, Jenny Downs, Gareth Baynam, Andrew Wilson, Peter Richmond, and Helen Leonard. Medical comorbidities in mecp2 duplication syndrome: results from the international mecp2 duplication database. Children, 9:633, Apr 2022. URL: https://doi.org/10.3390/children9050633, doi:10.3390/children9050633. This article has 14 citations.
