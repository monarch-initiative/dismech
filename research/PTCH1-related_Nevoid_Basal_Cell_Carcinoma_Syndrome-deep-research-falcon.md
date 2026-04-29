---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-05T20:59:31.858223'
end_time: '2026-04-05T21:09:53.022192'
duration_seconds: 621.16
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: PTCH1-related nevoid basal cell carcinoma syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 40
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** PTCH1-related nevoid basal cell carcinoma syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PTCH1-related nevoid basal cell carcinoma syndrome** covering all of the
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
- **Disease Name:** PTCH1-related nevoid basal cell carcinoma syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **PTCH1-related nevoid basal cell carcinoma syndrome** covering all of the
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


# PTCH1-related nevoid basal cell carcinoma syndrome (NBCCS/Gorlin syndrome): comprehensive disease characteristics report

## 1. Disease information

### Overview
PTCH1-related nevoid basal cell carcinoma syndrome (NBCCS), commonly called Gorlin syndrome (also Gorlin–Goltz syndrome; basal cell nevus syndrome), is an autosomal-dominant, multisystem cancer-predisposition/developmental disorder characterized by early-onset, often multiple basal cell carcinomas (BCCs), odontogenic keratocysts of the jaws, and characteristic skeletal and craniofacial findings, with additional tumor risks (e.g., medulloblastoma, ovarian/cardiac fibromas). (murgia2024gorlinsyndromeassociatedbasal pages 1-2, bresler2016nevoidbasalcell pages 1-3)

Recent summaries continue to emphasize variable expressivity and the importance of multidisciplinary surveillance because individuals may require “dozens or even hundreds of surgical procedures in their lifetime” for BCC management. (murgia2024gorlinsyndromeassociatedbasal pages 1-2)

### Key identifiers
A concise normalization table is provided below.

| Item | Value | Notes/Source |
|---|---|---|
| Disease name | PTCH1-related nevoid basal cell carcinoma syndrome | Also referred to clinically as Gorlin syndrome / basal cell nevus syndrome; PTCH1 is the major causal gene in most molecularly solved cases (murgia2024gorlinsyndromeassociatedbasal pages 1-2, kolkiran2024furtherexpandingthe pages 1-2, moramarco2019ocularmanifestationsin pages 1-2) |
| MONDO ID | MONDO:0007187 | Open Targets disease association entry for nevoid basal cell carcinoma syndrome mapped this disease to MONDO_0007187 (from tool output in prior evidence summary) (murgia2024gorlinsyndromeassociatedbasal pages 1-2) |
| OMIM (NBCCS) | OMIM:109400 | NBCCS / Gorlin syndrome reported as OMIM #109400 in multiple sources; one 2024 paper listed OMIM #606593, which appears inconsistent with the broader literature and should be interpreted cautiously (kammoun2024theoralfacialmanifestations pages 17-25, alonso2018novelclinicaland pages 1-5, kolkiran2024furtherexpandingthe pages 1-2) |
| Key synonyms | Gorlin syndrome; Gorlin-Goltz syndrome; basal cell nevus syndrome (BCNS); nevoid basal cell carcinoma syndrome (NBCCS); multiple nevoid basal-cell carcinoma syndrome; jaw cyst-basal cell tumor-skeletal anomaly syndrome; fifth phacomatosis | Synonyms compiled from reviews and case literature (murgia2024gorlinsyndromeassociatedbasal pages 1-2, kammoun2024theoralfacialmanifestations pages 17-25, thalakoti2015basalcellnevus pages 1-2) |
| Inheritance | Autosomal dominant | Repeatedly described as autosomal dominant, often with complete or near-complete penetrance and variable expressivity (moramarco2019ocularmanifestationsin pages 1-2, murgia2024gorlinsyndromeassociatedbasal pages 1-2, alonso2018novelclinicaland pages 1-5, thalakoti2015basalcellnevus pages 1-2) |
| Main causal gene (PTCH1) | PTCH1 | PTCH1 loss-of-function is the principal cause; literature states PTCH1 accounts for ~85% to 90% of known-etiology cases and encodes a Sonic Hedgehog pathway receptor/tumor suppressor (moramarco2019ocularmanifestationsin pages 1-2, kolkiran2024furtherexpandingthe pages 1-2) |
| Other genes | SUFU; PTCH2 (contested) | SUFU is an established alternative cause with distinct phenotype/tumor-risk profile; PTCH2 has been reported in some patients but its causal role is questioned/contested in the literature (moramarco2019ocularmanifestationsin pages 1-2, akbari2018basalcellnevus pages 4-4) |
| Prevalence range | Approximately 1 in 31,000 to 1 in 256,000 | Reported ranges vary by cohort/review; commonly cited estimates also include ~1:57,000 and 1:30,827 to 1:164,000 (moramarco2019ocularmanifestationsin pages 1-2, murgia2024gorlinsyndromeassociatedbasal pages 1-2, kolkiran2024furtherexpandingthe pages 1-2, thalakoti2015basalcellnevus pages 1-2) |
| De novo rate | Approximately 20% to 30% | Multiple sources state that about 20–30% of cases arise de novo; familial cases account for the remainder in most series (murgia2024gorlinsyndromeassociatedbasal pages 1-2, moramarco2019ocularmanifestationsin pages 1-2) |
| Penetrance / expressivity | Complete or high penetrance with variable expressivity | Sources consistently describe complete/high penetrance but marked intrafamilial and interfamilial variability in severity and manifestations (moramarco2019ocularmanifestationsin pages 1-2, alonso2018novelclinicaland pages 1-5, thalakoti2015basalcellnevus pages 1-2, bresler2016nevoidbasalcell pages 1-3) |


*Table: This table summarizes core identifiers, naming conventions, inheritance, and high-level genetic epidemiology for PTCH1-related nevoid basal cell carcinoma syndrome using only the cited evidence gathered in the session. It is useful as a compact normalization reference for a disease knowledge base entry.*

*Evidence gaps for identifiers in this run.* Orphanet IDs, ICD-10/ICD-11 codes, and MeSH IDs were not present in the retrieved full texts; these should be added from Orphanet/WHO/NLM resources in a follow-on curation step.

### Information source types
Evidence here is aggregated from peer-reviewed cohort/case-series studies, consensus surveillance recommendations, and systematic/ narrative reviews; several sources also include individual case reports (useful for rare manifestations). (murgia2024gorlinsyndromeassociatedbasal pages 1-2, wescott2023sustainedsuppressionof pages 1-2, kolkiran2024furtherexpandingthe pages 1-2)


## 2. Etiology

### Disease causal factors
**Primary cause (genetic).** PTCH1-related NBCCS is typically caused by heterozygous loss-of-function (tumor suppressor) variants in *PTCH1*, a core negative regulator of Sonic Hedgehog (SHH) signaling. A 2024 cohort paper states: “heterozygous pathogenic variants in *PTCH1* are responsible for 90% of Gorlin syndrome cases,” and that these variants “cause overstimulation of the sonic hedgehog signaling pathway.” (kolkiran2024furtherexpandingthe pages 1-2)

**Other genetic causes / locus heterogeneity.** *SUFU* is a well-established alternative cause of Gorlin syndrome with a distinct tumor-risk profile, particularly higher early-childhood medulloblastoma risk. (guerrinirousseau2021currentrecommendationsfor pages 5-6, guerrinirousseau2021currentrecommendationsfor pages 4-5)

**PTCH2 uncertainty.** Some literature reports *PTCH2* variants in NBCCS-like presentations, but at least one genetics-focused study questions whether *PTCH2* is truly causal: reporting a healthy individual homozygous for a frameshift variant and concluding that this “question[s] whether variants in PTCH2 are associated with NBCCS.” (kolkiran2024furtherexpandingthe pages 1-2)

### Risk factors
**Environmental—UV radiation and ionizing radiation.** BCC development is strongly modulated by UV exposure and skin type in hedgehog-driven BCC. A molecular genetics review notes that “the molecular basis of BCC involves an interplay of inherited genetic susceptibility and somatic mutations, commonly induced by exposure to UV radiation.” (kilgour2021reviewofthe pages 2-4) Somatic *PTCH1* mutations in BCC frequently show UV-signature changes (e.g., ~50% of *PTCH1* mutations). (kilgour2021reviewofthe pages 9-12)

**Radiation sensitivity and second malignancy risk.** Surveillance guidelines emphasize long-term follow-up after radiotherapy due to risk of secondary malignancies in Gorlin syndrome. (guerrinirousseau2021currentrecommendationsfor pages 1-2)

**Genotype as a risk stratifier.** Tumor risks differ substantially by gene: in PTCH1-related GS, odontogenic keratocysts are frequent and appear largely restricted to PTCH1 disease, whereas SUFU carriers have higher medulloblastoma penetrance and lower BCC/OKC rates. (guerrinirousseau2021currentrecommendationsfor pages 5-6, guerrinirousseau2021currentrecommendationsfor pages 2-4, guerrinirousseau2018germlinesufumutation pages 12-14)

### Protective factors
Direct evidence for protective germline variants or specific protective exposures in PTCH1-related NBCCS was not identified in the retrieved corpus. However, consensus guidance recommends sun protection and avoidance of unnecessary ionizing radiation, implying these are modifiable protective behaviors against BCC burden. (hansford2024updateoncancer pages 2-3)

### Gene–environment interaction
A standard model is **germline *PTCH1* loss-of-function + somatic second hit**, often attributable to UV exposure, yielding constitutive Hedgehog activity and BCC tumorigenesis. (kilgour2021reviewofthe pages 2-4, kilgour2021reviewofthe pages 9-12)


## 3. Phenotypes (clinical spectrum)

### Core diagnostic criteria and phenotypic domains
Major and minor clinical criteria remain central for diagnosis and for structuring phenotype capture.

A 2024 clinical series reiterates a combinatorial diagnostic rule: “When a patient meets two major diagnostic criteria and one minor diagnostic criteria, or one major diagnostic criteria and three minor diagnostic criteria, a diagnosis of GS is established.” (murgia2024gorlinsyndromeassociatedbasal pages 1-2)

A 2024 genetics paper lists major criteria including early-onset/multiple BCCs, odontogenic keratocysts before age 20, palmar-plantar pits, lamellar falx cerebri calcification, desmoplastic medulloblastoma, and a first-degree affected relative; it also enumerates minor criteria including rib anomalies, macrocephaly, cleft lip/palate, ovarian/cardiac fibromas, lymphomesenteric cysts, and ocular anomalies (e.g., strabismus/hypertelorism/congenital cataracts/coloboma). (kolkiran2024furtherexpandingthe pages 1-2)

### Phenotype-by-phenotype (with suggested HPO terms)
Below are common features with typical onset patterns and frequencies when available.

1) **Basal cell carcinomas (BCCs)** (clinical sign/tumor)
- Typical onset: often adolescence/young adulthood; can occur earlier. (bresler2016nevoidbasalcell pages 1-3, moramarco2019ocularmanifestationsin pages 1-2)
- Burden/progression: can be numerous; one review notes BCCs “may number up to 500 in a lifetime.” (bresler2016nevoidbasalcell pages 1-3)
- Suggested HPO: Basal cell carcinoma (HP:0002671).

2) **Odontogenic keratocysts (OKCs) / keratocystic odontogenic tumors** (clinical sign)
- Often present in childhood/second decade; a surveillance guideline notes OKCs “have been described in 75–89% of patients” and appear “restricted to PTCH1 associated GS.” (guerrinirousseau2021currentrecommendationsfor pages 2-4)
- Suggested HPO: Odontogenic keratocyst (HP:0000684); Jaw cyst (HP:0000673).

3) **Falx cerebri calcification** (imaging sign)
- A 2024 cohort reports: “By the age of 20, over 90% of individuals develop ectopic calcification of the falx cerebri.” (murgia2024gorlinsyndromeassociatedbasal pages 1-2)
- Suggested HPO: Calcification of the falx cerebri (HP:0005462).

4) **Palmoplantar pits** (cutaneous sign)
- Often develop in the second decade; described as “2–3 mm in diameter” and “1–3 mm in depth.” (murgia2024gorlinsyndromeassociatedbasal pages 1-2)
- Suggested HPO: Palmoplantar pits (HP:0000977).

5) **Macrocephaly / craniofacial anomalies** (physical manifestation)
- A 2024 clinical series indicates ~60% have macrocephaly/frontal bossing/facial dysmorphism. (murgia2024gorlinsyndromeassociatedbasal pages 1-2)
- Suggested HPO: Macrocephaly (HP:0000256); Frontal bossing (HP:0002007); Cleft palate (HP:0000175).

6) **Skeletal anomalies (e.g., bifid ribs, vertebral anomalies)** (imaging/physical)
- Included among diagnostic criteria; commonly reported in cohorts. (kolkiran2024furtherexpandingthe pages 1-2, bresler2016nevoidbasalcell pages 1-3)
- Suggested HPO: Bifid rib (HP:0000892); Vertebral segmentation defect (HP:0003420).

7) **Medulloblastoma risk** (tumor)
- Particularly associated with SUFU-related disease; a surveillance review reports “approximately 5%” develop medulloblastoma, with mean onset ~2 years and 97% by age 5, and recommends early-life MRI in SUFU carriers. (salvador2017cancersurveillancein pages 1-2)
- Suggested HPO: Medulloblastoma (HP:0002885).

8) **Ovarian fibroma/fibrothecoma** (tumor)
- Included in minor criteria; cohort data show ovarian fibromas detected by pelvic ultrasound and can be clinically subtle. (guerrinirousseau2021currentrecommendationsfor pages 2-4)
- Suggested HPO: Ovarian fibroma (HP:0000131).

9) **Ocular manifestations** (clinical signs)
- An Orphanet Journal of Rare Diseases cohort quantifies multiple ocular findings: hypertelorism 45.5%, congenital cataract 18%, nystagmus 9%, colobomas 9%; additionally, the study “highlights strabismus (63% of the patients), epiretinal membranes (36%) and myelinated optic nerve fiber layers (36%) as the most frequent ophthalmological findings.” (moramarco2019ocularmanifestationsin pages 1-2)
- Suggested HPO: Strabismus (HP:0000486); Hypertelorism (HP:0000316); Congenital cataract (HP:0000519); Coloboma (HP:0000589).

### Quality of life impact
Direct QoL instrument data (e.g., SF-36/EQ-5D) were not available in the retrieved texts. However, treatment series emphasize a large lifelong surgical burden and disfigurement risk from repeated BCC excisions, supporting high QoL impact. (murgia2024gorlinsyndromeassociatedbasal pages 1-2)


## 4. Genetic / molecular information

### Causal genes
- **Primary:** *PTCH1* (tumor suppressor; Hedgehog receptor/negative regulator). (kolkiran2024furtherexpandingthe pages 1-2, alonso2018novelclinicaland pages 1-5)
- **Other established:** *SUFU* (negative regulator of Hedgehog signaling). (guerrinirousseau2021currentrecommendationsfor pages 5-6, guerrinirousseau2018germlinesufumutation pages 12-14)

### Pathogenic variant spectrum (PTCH1)
**Variant classes.** In a 22-patient Spanish cohort, PTCH1 sequencing identified numerous truncating variants; the authors report “Most of them produce a truncated protein which is unable to supress Smoothened protein and continuously activates the downstream pathway,” and that “Most of the mutations found were frameshift (52.2%).” (alonso2018novelclinicaland pages 1-5, alonso2018novelclinicaland pages 5-9)

**CNVs and mosaicism (recent development, 2024).** A 2024 methods paper highlights postzygotic mosaic PTCH1 CNVs and the need for sensitive quantification. It reports ddPCR detected a PTCH1 CNV duplication and quantified mosaicism that MLPA missed in blood, supporting ddPCR as an adjunct for low-grade mosaic cases and recurrence-risk counseling. (roemen2024detectionofptch1 pages 5-7)

**De novo rate.** Multiple sources estimate de novo variants account for ~20–30% of cases. (moramarco2019ocularmanifestationsin pages 1-2)

### Somatic vs germline; functional consequences
PTCH1 pathogenic germline variants act as loss-of-function in a tumor suppressor pathway; tumorigenesis is consistent with Knudson’s two-hit model, where somatic inactivation of the remaining allele in target tissues leads to clonal expansion and tumor formation. (bresler2016nevoidbasalcell pages 1-3, kilgour2021reviewofthe pages 2-4)

### Modifier genes
Clinical series suggest modifier genes and environment contribute to variable expressivity; one 2024 paper explicitly notes expressivity “may be attributed to modifier genes (SUFU and PTCH2) and environmental exposure.” (murgia2024gorlinsyndromeassociatedbasal pages 1-2)

### Epigenetic information
Direct NBCCS-specific methylation/histone datasets were not retrieved here. Related oncologic research shows that Hedgehog pathway transcriptional output can be epigenetically regulated through BET bromodomain proteins (e.g., BRD4 occupancy at GLI promoters), which has therapeutic implications in Hedgehog-driven tumors including BCC and medulloblastoma. ()


## 5. Environmental information

- **UV radiation** is a major contributor to BCC mutagenesis, including UV-signature mutations affecting *PTCH1* in BCC. (kilgour2021reviewofthe pages 9-12)
- **Ionizing radiation** is generally avoided where possible because of secondary malignancy risk; pediatric surveillance guidance explicitly advises avoidance unless necessary. (hansford2024updateoncancer pages 2-3)
- Lifestyle factors beyond photoprotection were not specifically quantified in the retrieved sources.


## 6. Mechanism / pathophysiology

### Key pathway: Sonic Hedgehog (SHH) signaling dysregulation
**Core concept.** PTCH1 normally suppresses SMO activity. A pathology review states: “PTCH1… maintains smoothened (SMO) in its inactive/unphosphorylated state,” and PTCH1 loss leads to constitutive Hedgehog pathway activation with GLI transcription factor activity. (bresler2016nevoidbasalcell pages 1-3)

**Causal chain (simplified).**
1) Germline PTCH1 loss-of-function → reduced repression of SMO. (bresler2016nevoidbasalcell pages 1-3, alonso2018novelclinicaland pages 1-5)
2) SMO activation → GLI transcriptional activation (e.g., GLI1) → increased expression of genes involved in proliferation/survival/angiogenesis and altered differentiation. (kilgour2021reviewofthe pages 2-4, kammoun2024theoralfacialmanifestations pages 34-38)
3) Somatic second hit (often UV-driven) in target tissue → biallelic PTCH1 inactivation → clonal expansion → BCC/OKC and other neoplasms. (kilgour2021reviewofthe pages 2-4, kilgour2021reviewofthe pages 9-12)

**UV mechanism integration.** A molecular genetics review reports that somatic *PTCH1* mutations occur in up to ~75% of BCCs and that overall HH-pathway alterations occur in ~90% of tumors; importantly, ~50% of *PTCH1* mutations have UV-signature changes, aligning UV with the “second hit” mechanism. (kilgour2021reviewofthe pages 9-12)

### Cellular processes and tissue context
- **Cell cycle regulation:** HH activation increases transcription of cyclins D/E and proliferation programs mediated by GLI1. (kammoun2024theoralfacialmanifestations pages 34-38)
- **Developmental patterning / craniofacial and skeletal development:** Hedgehog signaling is essential for embryonic development; dysregulation produces developmental anomalies (e.g., craniofacial/skeletal) characteristic of NBCCS. (kolkiran2024furtherexpandingthe pages 1-2, onodera2020gorlinsyndromerecent pages 6-8)

### Suggested ontology terms
- **GO biological process:** Hedgehog signaling pathway (GO:0007224); regulation of transcription by RNA polymerase II (GO:0006357); cell proliferation (GO:0008283); DNA damage response (GO:0006974).
- **Cell Ontology (CL) candidate cell types:** basal keratinocyte (CL:0000313); hair follicle stem cell (CL terms vary by ontology release); osteoblast (CL:0000062); odontogenic epithelial cell (not always directly available as CL term).


## 7. Anatomical structures affected

**Primary organs/tissues**
- Skin (cutaneous BCCs; palmar/plantar pits). (bresler2016nevoidbasalcell pages 1-3, murgia2024gorlinsyndromeassociatedbasal pages 1-2)
- Jaw/maxillofacial tissues (odontogenic keratocysts). (guerrinirousseau2021currentrecommendationsfor pages 2-4)
- Cranial meninges/brain (falx calcification; medulloblastoma risk in subsets; meningioma risk particularly in SUFU carriers). (guerrinirousseau2021currentrecommendationsfor pages 5-6, guerrinirousseau2021currentrecommendationsfor pages 4-5)
- Gonads (ovarian fibromas/fibrothecomas). (guerrinirousseau2021currentrecommendationsfor pages 5-6, hansford2024updateoncancer pages 2-3)

**UBERON suggestions**
- Skin of body (UBERON:0002097)
- Mandible (UBERON:0001684); Maxilla (UBERON:0000166)
- Cerebellum (UBERON:0002037)
- Ovary (UBERON:0000992)


## 8. Temporal development

- **Onset pattern:** developmental anomalies can be congenital/childhood; BCCs often begin around puberty/young adulthood; jaw cysts often arise in childhood/adolescence; falx calcification is common by age 20 (>90%). (murgia2024gorlinsyndromeassociatedbasal pages 1-2, bresler2016nevoidbasalcell pages 1-3)
- **Course:** lifelong predisposition with episodic emergence of new BCCs and cysts; tumor surveillance needs to be longitudinal. (guerrinirousseau2021currentrecommendationsfor pages 1-2)


## 9. Inheritance and population

### Inheritance
Autosomal dominant inheritance with high/complete penetrance and variable expressivity is repeatedly reported in the clinical literature. (moramarco2019ocularmanifestationsin pages 1-2, thalakoti2015basalcellnevus pages 1-2)

### Epidemiology (recently restated)
Prevalence estimates vary by population and ascertainment. A 2024 clinical study notes a commonly cited prevalence of 1:57,000 and a theoretical range of 1:30,827 to 1:164,000. (murgia2024gorlinsyndromeassociatedbasal pages 1-2) Other literature quotes ranges up to 1 in 256,000. (moramarco2019ocularmanifestationsin pages 1-2, kolkiran2024furtherexpandingthe pages 1-2)

### De novo and familial proportions
A 2024 review/series reports “About 20–30% of GS cases are caused by a de novo pathogenetic variation, whereas 70–80% of cases have a relevant family history.” (murgia2024gorlinsyndromeassociatedbasal pages 1-2)

### Genotype-specific tumor risks (key statistics)
- **Medulloblastoma:** PTCH1 carriers likely have low risk “probably under 2%,” whereas SUFU carriers have risk “around 8–9%” and are recommended intensive early-childhood MRI screening. (guerrinirousseau2021currentrecommendationsfor pages 5-6)
- **OKCs:** described in “75–89%” and “restricted to PTCH1 associated GS.” (guerrinirousseau2021currentrecommendationsfor pages 2-4)


## 10. Diagnostics

### Clinical diagnostic criteria
Diagnosis may be made using combinations of major/minor criteria; one cohort provides an explicit rule set: diagnosis can be established by “(1) one major criteria and genetic confirmation; or (2) two major criteria; or (3) one major and two minor criteria.” (kolkiran2024furtherexpandingthe pages 1-2)

### Genetic testing (recommended approach)
Given locus heterogeneity and CNVs/mosaicism, evidence supports:
- PTCH1 sequencing plus CNV detection (e.g., MLPA), and consideration of more sensitive quantitative methods (ddPCR) when mosaicism is suspected. (roemen2024detectionofptch1 pages 5-7)
- If PTCH1 is negative in a clinically compatible case, consider SUFU (and cautiously PTCH2) testing. (akbari2018basalcellnevus pages 4-4)

### Differential diagnosis (high-level)
- SUFU-related Gorlin syndrome (higher medulloblastoma/meningioma risk; fewer OKCs and BCCs). (guerrinirousseau2021currentrecommendationsfor pages 5-6, guerrinirousseau2018germlinesufumutation pages 12-14)
- PTCH1/SUFU-negative “Gorlin-like” phenotypes; emerging discussion exists around other genes, but robust evidence for causality is limited in the retrieved set. ()


## 11. Outcome / prognosis

Mortality is typically driven by malignancies (rare metastatic BCC; medulloblastoma/other tumors) rather than the developmental features themselves. Treatment series emphasize long-term morbidity from high BCC burden and repeated procedures. (murgia2024gorlinsyndromeassociatedbasal pages 1-2, wescott2023sustainedsuppressionof pages 1-2)

For SUFU-associated medulloblastoma, a Neuro-Oncology cohort reports 5-year DFS/OS of 37.5%/67.0% in their series and notes additional second malignancies, reinforcing the need for dedicated surveillance and treatment planning. (guerrinirousseau2018germlinesufumutation pages 12-14)


## 12. Treatment

### Standard of care (real-world)
**Cutaneous BCC management** remains anchored in lesion-directed dermatologic therapies (surgery, destructive modalities), but systemic hedgehog pathway inhibitors (HHIs) have become critical for high-burden disease.

### Hedgehog pathway inhibitors (HHIs): vismodegib and sonidegib
**Real-world effectiveness (2023 case series).** In 10 Gorlin patients treated with HHIs, “All patients achieved a complete remission,” and treatment reduced new BCCs from “28.3 ± 24.6 prior to treatment” to “1.4 ± 2.0 during treatment (p = 0.0048)” with a median time to new BCC of 47.3 months. (wescott2023sustainedsuppressionof pages 1-2)

**Comparative effectiveness/safety (2024 retrospective cohort).** In a 16-patient cohort, sonidegib had higher 4-month clinical remission (61.5%) than vismodegib (16.7%), and fewer patients had side effects (57.9% vs 100%). (murgia2024gorlinsyndromeassociatedbasal pages 5-7)

**Adverse events.** Common class adverse effects include dysgeusia, fatigue, alopecia, muscle spasms, and weight loss. (murgia2024gorlinsyndromeassociatedbasal pages 2-4)

**Implementation detail: schedule modification.** Both 2023 and 2024 series report dose/schedule adjustments (interruptions/holidays) to improve tolerability without obvious loss of efficacy, enabling longer-term treatment. (wescott2023sustainedsuppressionof pages 9-10, murgia2024gorlinsyndromeassociatedbasal pages 1-2)

### Topical hedgehog inhibition and trials (real-world development)
ClinicalTrials.gov records include multiple trials of topical patidegib gel in Gorlin syndrome, including a completed phase 3 trial (NCT03703310) and an active phase 3 trial (NCT06050122). (hansford2024updateoncancer media d17aac4b)

### Treatment ontology (MAXO suggestions)
- Hedgehog pathway inhibitor therapy (e.g., vismodegib/sonidegib) — MAXO term may map to “targeted molecular therapy” / “SMO inhibitor therapy” (exact MAXO identifier to be assigned during ontology curation).
- Dermatologic surveillance and excision — “surgical excision,” “dermatologic examination.”
- Genetic counseling — “genetic counseling.”


## 13. Prevention

Consensus pediatric cancer predisposition guidance includes behavioral and exposure avoidance: individuals “should be counseled on sun protection and avoidance of ionizing irradiation unless absolutely necessary.” (hansford2024updateoncancer pages 2-3)


## 14. Other species / natural disease
Natural disease analogs in companion animals were not identified in the retrieved sources for this run.


## 15. Model organisms and experimental systems

**Mouse models.** Ptch1-deficient mice are central NBCCS models. A 2020 review summarizes that Ptch1 mutant mouse lines are “prone to tumor development and skeletal abnormalities and exhibited increased susceptibility to irradiation.” (onodera2020gorlinsyndromerecent pages 6-8)

**iPSC and cellular models.** Patient-derived iPSCs and stromal cell models capture pathway and differentiation phenotypes; for example, reduced conversion of full-length Gli3 to its repressor form was observed in Ptch1+/− mice and GS iPS cells, linking Hedgehog dysregulation to osteogenic programs. (onodera2020gorlinsyndromerecent pages 6-8)

**Cross-species developmental genetics.** Drosophila patched/hedgehog mutants and mammalian GLI1 transfection models provide mechanistic evidence connecting HH/GLI activation to proliferative phenotypes relevant to tumorigenesis. (kammoun2024theoralfacialmanifestations pages 34-38)


## Current applications / real-world implementations (summary)

1) **Genotype-stratified surveillance** is implemented in expert recommendations and summarized in 2024 guidance (skin exams, dental imaging for PTCH1; intensive early-life brain MRI for SUFU). (hansford2024updateoncancer pages 2-3, hansford2024updateoncancer media d17aac4b)

2) **Long-term systemic HHI therapy** (vismodegib/sonidegib) is used to reduce surgical burden and suppress new lesion formation, with real-world cohorts reporting dramatic reductions in incident BCCs and frequent need for tolerability-driven schedule modification. (wescott2023sustainedsuppressionof pages 1-2, murgia2024gorlinsyndromeassociatedbasal pages 5-7)

3) **Improved molecular diagnostics for mosaicism/CNVs** (ddPCR) are emerging as practical clinical tools to avoid missed diagnoses and better estimate recurrence risk in families. (roemen2024detectionofptch1 pages 5-7)


## Visual evidence: surveillance recommendations table
The following extracted table image summarizes surveillance recommendations stratified by PTCH1 vs SUFU (skin exams, dental orthopantomogram, brain MRI schedules, and pelvic ultrasound). (hansford2024updateoncancer media d17aac4b)


## Notes on limitations of this report
- Orphanet/ICD/MeSH identifiers were not retrievable from the available full texts in this run and should be added from dedicated disease-ontology resources.
- Some sources labeled as “Unknown journal” may reflect ingestion limitations; key clinical/statistical claims were preferentially supported by peer-reviewed journal articles and consensus statements.


References

1. (murgia2024gorlinsyndromeassociatedbasal pages 1-2): Giulia Murgia, Luca Valtellini, Nerina Denaro, Gianluca Nazzaro, Paolo Bortoluzzi, Valentina Benzecry, Emanuela Passoni, and Angelo Valerio Marzano. Gorlin syndrome-associated basal cell carcinomas treated with vismodegib or sonidegib: a retrospective study. Cancers, 16:2166, Jun 2024. URL: https://doi.org/10.3390/cancers16122166, doi:10.3390/cancers16122166. This article has 15 citations.

2. (bresler2016nevoidbasalcell pages 1-3): Scott C. Bresler, Bonnie L. Padwa, and Scott R. Granter. Nevoid basal cell carcinoma syndrome (gorlin syndrome). Head and Neck Pathology, 10:119-124, Mar 2016. URL: https://doi.org/10.1007/s12105-016-0706-9, doi:10.1007/s12105-016-0706-9. This article has 219 citations and is from a peer-reviewed journal.

3. (kolkiran2024furtherexpandingthe pages 1-2): Abdulkerim Kolkiran, Pelin Özlem Şimşek-Kiper, Göknur Topaloğlu Yasan, Beren Karaosmanoğlu, Ekim Taşkıran, Gülen Eda Utine, Hakan H. Tüz, and Koray Boduroğlu. Further expanding the mutational spectrum of gorlin syndrome in three unrelated families. Molecular Syndromology, 15:175-184, Jan 2024. URL: https://doi.org/10.1159/000535407, doi:10.1159/000535407. This article has 3 citations and is from a peer-reviewed journal.

4. (moramarco2019ocularmanifestationsin pages 1-2): Antonietta Moramarco, Ehud Himmelblau, Emanuele Miraglia, Fabiana Mallone, Vincenzo Roberti, Federica Franzone, Chiara Iacovino, Sandra Giustini, and Alessandro Lambiase. Ocular manifestations in gorlin-goltz syndrome. Orphanet Journal of Rare Diseases, Sep 2019. URL: https://doi.org/10.1186/s13023-019-1190-6, doi:10.1186/s13023-019-1190-6. This article has 43 citations and is from a peer-reviewed journal.

5. (kammoun2024theoralfacialmanifestations pages 17-25): K Kammoun. The oral-facial manifestations of gorlin syndrome. Unknown journal, 2024.

6. (alonso2018novelclinicaland pages 1-5): N. Alonso, N. Alonso, Javier Cañueto, S. Círia, Elena Bueno, I. Palacios‐Álvarez, M. Alegre, C. Badenas, A. Barreiro, L. Pena, C. Maldonado, M. Nespeira‐Jato, C. Peña-penabad, A. Azon, M. Gavrilova, I. Ferrer, O. Sanmartín, L. Robles, Á. Hernández-Martín, Miguel Urioste, S. Puig, Lluís Puig, and Rogelio González-Sarmiento. Novel clinical and molecular findings in spanish patients with naevoid basal cell carcinoma syndrome. British Journal of Dermatology, 178:198-206, Jan 2018. URL: https://doi.org/10.1111/bjd.15835, doi:10.1111/bjd.15835. This article has 10 citations and is from a highest quality peer-reviewed journal.

7. (thalakoti2015basalcellnevus pages 1-2): Srikanth Thalakoti and Thomas Geller. Basal cell nevus syndrome or gorlin syndrome. Handbook of clinical neurology, 132:119-28, Jan 2015. URL: https://doi.org/10.1016/b978-0-444-62702-5.00008-1, doi:10.1016/b978-0-444-62702-5.00008-1. This article has 49 citations.

8. (akbari2018basalcellnevus pages 4-4): Maryam Akbari, Harold Chen, Grace Guo, Zachary Legan, and Ghali Ghali. Basal cell nevus syndrome (gorlin syndrome): genetic insights, diagnostic challenges, and unmet milestones. Pathophysiology : the official journal of the International Society for Pathophysiology, 25 2:77-82, Jun 2018. URL: https://doi.org/10.1016/j.pathophys.2017.12.004, doi:10.1016/j.pathophys.2017.12.004. This article has 53 citations.

9. (wescott2023sustainedsuppressionof pages 1-2): Raquel Wescott and Wolfram Samlowski. Sustained suppression of gorlin syndrome-associated basal cell carcinomas with vismodegib or sonidegib: a case series. Current Oncology, 30:9156-9167, Oct 2023. URL: https://doi.org/10.3390/curroncol30100661, doi:10.3390/curroncol30100661. This article has 7 citations.

10. (guerrinirousseau2021currentrecommendationsfor pages 5-6): L. Guerrini-Rousseau, M. J. Smith, C. P. Kratz, B. Doergeloh, S. Hirsch, S. M. J. Hopman, M. Jorgensen, M. Kuhlen, O. Michaeli, T. Milde, V. Ridola, A. Russo, H. Salvador, N. Waespe, B. Claret, L. Brugieres, and D. G. Evans. Current recommendations for cancer surveillance in gorlin syndrome: a report from the siope host genome working group (siope hgwg). Familial Cancer, 20:317-325, Apr 2021. URL: https://doi.org/10.1007/s10689-021-00247-z, doi:10.1007/s10689-021-00247-z. This article has 51 citations and is from a peer-reviewed journal.

11. (guerrinirousseau2021currentrecommendationsfor pages 4-5): L. Guerrini-Rousseau, M. J. Smith, C. P. Kratz, B. Doergeloh, S. Hirsch, S. M. J. Hopman, M. Jorgensen, M. Kuhlen, O. Michaeli, T. Milde, V. Ridola, A. Russo, H. Salvador, N. Waespe, B. Claret, L. Brugieres, and D. G. Evans. Current recommendations for cancer surveillance in gorlin syndrome: a report from the siope host genome working group (siope hgwg). Familial Cancer, 20:317-325, Apr 2021. URL: https://doi.org/10.1007/s10689-021-00247-z, doi:10.1007/s10689-021-00247-z. This article has 51 citations and is from a peer-reviewed journal.

12. (kilgour2021reviewofthe pages 2-4): James M. Kilgour, Justin L. Jia, and Kavita Y. Sarin. Review of the molecular genetics of basal cell carcinoma; inherited susceptibility, somatic mutations, and targeted therapeutics. Cancers, 13:3870, Jul 2021. URL: https://doi.org/10.3390/cancers13153870, doi:10.3390/cancers13153870. This article has 43 citations.

13. (kilgour2021reviewofthe pages 9-12): James M. Kilgour, Justin L. Jia, and Kavita Y. Sarin. Review of the molecular genetics of basal cell carcinoma; inherited susceptibility, somatic mutations, and targeted therapeutics. Cancers, 13:3870, Jul 2021. URL: https://doi.org/10.3390/cancers13153870, doi:10.3390/cancers13153870. This article has 43 citations.

14. (guerrinirousseau2021currentrecommendationsfor pages 1-2): L. Guerrini-Rousseau, M. J. Smith, C. P. Kratz, B. Doergeloh, S. Hirsch, S. M. J. Hopman, M. Jorgensen, M. Kuhlen, O. Michaeli, T. Milde, V. Ridola, A. Russo, H. Salvador, N. Waespe, B. Claret, L. Brugieres, and D. G. Evans. Current recommendations for cancer surveillance in gorlin syndrome: a report from the siope host genome working group (siope hgwg). Familial Cancer, 20:317-325, Apr 2021. URL: https://doi.org/10.1007/s10689-021-00247-z, doi:10.1007/s10689-021-00247-z. This article has 51 citations and is from a peer-reviewed journal.

15. (guerrinirousseau2021currentrecommendationsfor pages 2-4): L. Guerrini-Rousseau, M. J. Smith, C. P. Kratz, B. Doergeloh, S. Hirsch, S. M. J. Hopman, M. Jorgensen, M. Kuhlen, O. Michaeli, T. Milde, V. Ridola, A. Russo, H. Salvador, N. Waespe, B. Claret, L. Brugieres, and D. G. Evans. Current recommendations for cancer surveillance in gorlin syndrome: a report from the siope host genome working group (siope hgwg). Familial Cancer, 20:317-325, Apr 2021. URL: https://doi.org/10.1007/s10689-021-00247-z, doi:10.1007/s10689-021-00247-z. This article has 51 citations and is from a peer-reviewed journal.

16. (guerrinirousseau2018germlinesufumutation pages 12-14): Léa Guerrini-Rousseau, Christelle Dufour, Pascale Varlet, Julien Masliah-Planchon, Franck Bourdeaut, Marine Guillaud-Bataille, Rachid Abbas, Anne-Isabelle Bertozzi, Fanny Fouyssac, Sophie Huybrechts, Stéphanie Puget, Brigitte Bressac-De Paillerets, Olivier Caron, Nicolas Sevenet, Marina Dimaria, Sophie Villebasse, Olivier Delattre, Dominique Valteau-Couanet, Jacques Grill, and Laurence Brugières. Germline sufu mutation carriers and medulloblastoma: clinical characteristics, cancer risk, and prognosis. Neuro-Oncology, 20:1122–1132, Jul 2018. URL: https://doi.org/10.1093/neuonc/nox228, doi:10.1093/neuonc/nox228. This article has 85 citations and is from a domain leading peer-reviewed journal.

17. (hansford2024updateoncancer pages 2-3): Jordan R. Hansford, Anirban Das, Rose B. McGee, Yoshiko Nakano, Jack Brzezinski, Sarah R. Scollon, Surya P. Rednam, Jaclyn Schienda, Orli Michaeli, Sun Young Kim, Mary-Louise C. Greer, Rosanna Weksberg, Douglas R. Stewart, William D. Foulkes, Uri Tabori, Kristian W. Pajtler, Stefan M. Pfister, Garrett M. Brodeur, and Junne Kamihara. Update on cancer predisposition syndromes and surveillance guidelines for childhood brain tumors. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:2342-2350, Apr 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-4033, doi:10.1158/1078-0432.ccr-23-4033. This article has 49 citations.

18. (salvador2017cancersurveillancein pages 1-2): H. Salvador, Vivian Y. Chang, A. Erez, S. Voss, H. Scott, S. Plon, H. Druker, W. Foulkes, J. Kamihara, D. Evans, Laurence Brugi, G. Brodeur, K. Janeway, W. Kohlmann, K. Nathanson, J. Schiffman, L. Doros, J. Wilmott, H. Rizos, R. Scolyer, L. Marcus, and P. Keegan. Cancer surveillance in gorlin syndrome and rhabdoid tumor predisposition syndrome. Clinical Cancer Research, 23:e62-e67, Jun 2017. URL: https://doi.org/10.1158/1078-0432.ccr-17-0595, doi:10.1158/1078-0432.ccr-17-0595. This article has 223 citations and is from a highest quality peer-reviewed journal.

19. (alonso2018novelclinicaland pages 5-9): N. Alonso, N. Alonso, Javier Cañueto, S. Círia, Elena Bueno, I. Palacios‐Álvarez, M. Alegre, C. Badenas, A. Barreiro, L. Pena, C. Maldonado, M. Nespeira‐Jato, C. Peña-penabad, A. Azon, M. Gavrilova, I. Ferrer, O. Sanmartín, L. Robles, Á. Hernández-Martín, Miguel Urioste, S. Puig, Lluís Puig, and Rogelio González-Sarmiento. Novel clinical and molecular findings in spanish patients with naevoid basal cell carcinoma syndrome. British Journal of Dermatology, 178:198-206, Jan 2018. URL: https://doi.org/10.1111/bjd.15835, doi:10.1111/bjd.15835. This article has 10 citations and is from a highest quality peer-reviewed journal.

20. (roemen2024detectionofptch1 pages 5-7): Guido M. J. M. Roemen, Tom E. J. Theunissen, Ward W. J. Hoezen, Anja R. M. Steyls, Aimee D. C. Paulussen, Klara Mosterd, Elisa Rahikkala, Axel zur Hausen, Ernst Jan M. Speel, and Michel van Geel. Detection of ptch1 copy-number variants in mosaic basal cell nevus syndrome. Biomedicines, 12:330, Jan 2024. URL: https://doi.org/10.3390/biomedicines12020330, doi:10.3390/biomedicines12020330. This article has 1 citations.

21. (kammoun2024theoralfacialmanifestations pages 34-38): K Kammoun. The oral-facial manifestations of gorlin syndrome. Unknown journal, 2024.

22. (onodera2020gorlinsyndromerecent pages 6-8): Shoko Onodera, Yuriko Nakamura, and Toshifumi Azuma. Gorlin syndrome: recent advances in genetic testing and molecular and cellular biological research. International Journal of Molecular Sciences, 21:7559, Oct 2020. URL: https://doi.org/10.3390/ijms21207559, doi:10.3390/ijms21207559. This article has 84 citations.

23. (murgia2024gorlinsyndromeassociatedbasal pages 5-7): Giulia Murgia, Luca Valtellini, Nerina Denaro, Gianluca Nazzaro, Paolo Bortoluzzi, Valentina Benzecry, Emanuela Passoni, and Angelo Valerio Marzano. Gorlin syndrome-associated basal cell carcinomas treated with vismodegib or sonidegib: a retrospective study. Cancers, 16:2166, Jun 2024. URL: https://doi.org/10.3390/cancers16122166, doi:10.3390/cancers16122166. This article has 15 citations.

24. (murgia2024gorlinsyndromeassociatedbasal pages 2-4): Giulia Murgia, Luca Valtellini, Nerina Denaro, Gianluca Nazzaro, Paolo Bortoluzzi, Valentina Benzecry, Emanuela Passoni, and Angelo Valerio Marzano. Gorlin syndrome-associated basal cell carcinomas treated with vismodegib or sonidegib: a retrospective study. Cancers, 16:2166, Jun 2024. URL: https://doi.org/10.3390/cancers16122166, doi:10.3390/cancers16122166. This article has 15 citations.

25. (wescott2023sustainedsuppressionof pages 9-10): Raquel Wescott and Wolfram Samlowski. Sustained suppression of gorlin syndrome-associated basal cell carcinomas with vismodegib or sonidegib: a case series. Current Oncology, 30:9156-9167, Oct 2023. URL: https://doi.org/10.3390/curroncol30100661, doi:10.3390/curroncol30100661. This article has 7 citations.

26. (hansford2024updateoncancer media d17aac4b): Jordan R. Hansford, Anirban Das, Rose B. McGee, Yoshiko Nakano, Jack Brzezinski, Sarah R. Scollon, Surya P. Rednam, Jaclyn Schienda, Orli Michaeli, Sun Young Kim, Mary-Louise C. Greer, Rosanna Weksberg, Douglas R. Stewart, William D. Foulkes, Uri Tabori, Kristian W. Pajtler, Stefan M. Pfister, Garrett M. Brodeur, and Junne Kamihara. Update on cancer predisposition syndromes and surveillance guidelines for childhood brain tumors. Clinical cancer research : an official journal of the American Association for Cancer Research, 30:2342-2350, Apr 2024. URL: https://doi.org/10.1158/1078-0432.ccr-23-4033, doi:10.1158/1078-0432.ccr-23-4033. This article has 49 citations.
