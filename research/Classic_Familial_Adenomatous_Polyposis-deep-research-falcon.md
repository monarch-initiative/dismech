---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T13:06:11.428224'
end_time: '2026-05-08T13:17:21.396962'
duration_seconds: 669.97
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Classic Familial Adenomatous Polyposis
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 30
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Classic Familial Adenomatous Polyposis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Classic Familial Adenomatous Polyposis** covering all of the
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
- **Disease Name:** Classic Familial Adenomatous Polyposis
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Classic Familial Adenomatous Polyposis** covering all of the
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


# Comprehensive Research Report: Classic Familial Adenomatous Polyposis (Classic FAP)

## Scope and evidence notes
This report is based on the provided full-text excerpts and registry records retrieved with the available tools. Where PubMed IDs (PMIDs) were not present in retrieved excerpts, I provide DOI/URL and publication date; lack of PMID in this output should not be interpreted as absence of a PMID in PubMed.

---

## 1. Disease Information

### 1.1 Overview (definition and current understanding)
Classic familial adenomatous polyposis (classic FAP) is an autosomal dominant hereditary colorectal cancer predisposition syndrome characterized by extensive colorectal adenomatous polyposis (classically ≥100 cumulative adenomas) with near-certain progression to colorectal cancer (CRC) by mid-adulthood without prophylactic colorectal surgery. A widely used operational definition in contemporary cohorts is “more than 100 cumulative colorectal adenomas and/or having a known germline pathogenic variant in the APC gene.” (karstensen2024endoscopicindicatorsin pages 1-2)

A recent review states that FAP is “marked by extensive colorectal polyposis and a high risk of colorectal cancer (CRC)” and emphasizes that screening/enrollment programs enable prophylactic surgery before CRC develops. (kyriakidis2023updatedperspectiveson pages 1-2)

### 1.2 Key identifiers
A structured set of identifiers extracted from authoritative disease knowledge resources (via OpenTargets) and recent literature is provided in the table artifact below.

| Item | Value | Notes | Key source (with URL + year) |
|---|---|---|---|
| Disease identifier | MONDO:0021055 | OpenTargets evidence lists **classic familial adenomatous polyposis** under MONDO_0021055. Disease-target evidence strongly links APC to this entity. (OpenTargets Search: familial adenomatous polyposis) | OpenTargets disease-target evidence for classic familial adenomatous polyposis, https://platform.opentargets.org/ (accessed via evidence context; 2024/2025 platform snapshot) |
| Disease identifier | MONDO:0021056 | OpenTargets also lists **familial adenomatous polyposis 1** (MONDO_0021056), the APC-associated form closely related to classic FAP nomenclature. (OpenTargets Search: familial adenomatous polyposis) | OpenTargets disease-target evidence, https://platform.opentargets.org/ (2024/2025 platform snapshot) |
| Disease identifier | Orphanet:733 | OpenTargets evidence maps **Familial adenomatous polyposis** to **Orphanet_733**. (OpenTargets Search: familial adenomatous polyposis) | OpenTargets disease-target evidence, https://platform.opentargets.org/ (2024/2025 platform snapshot) |
| Related disease identifier | MONDO:0016362 | Listed for **attenuated familial adenomatous polyposis**; useful for distinguishing classic from attenuated disease in a knowledge base. (OpenTargets Search: familial adenomatous polyposis) | OpenTargets disease-target evidence, https://platform.opentargets.org/ (2024/2025 platform snapshot) |
| Key synonym | Classic FAP | Used in recent reviews to distinguish the severe phenotype from attenuated FAP. (kyriakidis2023updatedperspectiveson pages 1-2, buki2024raregermlinevariants pages 1-2) | Kyriakidis et al., 2023, https://doi.org/10.2147/TACG.S372241 ; Büki et al., 2024, https://doi.org/10.3390/ijms25158189 |
| Key synonym | Familial adenomatous polyposis (FAP) | Standard umbrella disease name; recent sources discuss classic and attenuated phenotypes under FAP. (kyriakidis2023updatedperspectiveson pages 1-2, buki2024raregermlinevariants pages 1-2) | Kyriakidis et al., 2023, https://doi.org/10.2147/TACG.S372241 ; Büki et al., 2024, https://doi.org/10.3390/ijms25158189 |
| Key synonym / historical variant | Gardner syndrome | Described as an APC-associated variant with polyps plus soft-tissue tumors/osteomas; historically treated as a phenotypic variant of FAP rather than a separate mechanism. (buki2024raregermlinevariants pages 1-2) | Büki et al., 2024, https://doi.org/10.3390/ijms25158189 |
| Core definition / diagnostic criteria | Classic FAP: typically **≥100 colorectal adenomatous polyps** | Recent sources define classic FAP clinically as ≥100 adenomas; some also accept fewer polyps if there is a known affected family member and/or pathogenic APC variant. (kyriakidis2023updatedperspectiveson pages 2-4, karstensen2024endoscopicindicatorsin pages 1-2, lin2024adrenaltumoursin pages 1-2) | Kyriakidis et al., 2023, https://doi.org/10.2147/TACG.S372241 ; Karstensen et al., 2024, https://doi.org/10.1007/s10689-024-00415-x ; Lin et al., 2024, https://doi.org/10.1186/s13053-024-00289-1 |
| Core definition / diagnostic criteria | Attenuated FAP: **<100 adenomas** | Recent reviews/snippets define attenuated FAP as a milder phenotype with fewer than 100 adenomas and later presentation. (kyriakidis2023updatedperspectiveson pages 1-2, buki2024raregermlinevariants pages 1-2) | Kyriakidis et al., 2023, https://doi.org/10.2147/TACG.S372241 ; Büki et al., 2024, https://doi.org/10.3390/ijms25158189 |
| Inheritance | Autosomal dominant | Repeated across recent reviews and cohort studies. (kyriakidis2023updatedperspectiveson pages 1-2, buki2024raregermlinevariants pages 1-2, lin2024adrenaltumoursin pages 1-2) | Kyriakidis et al., 2023, https://doi.org/10.2147/TACG.S372241 ; Büki et al., 2024, https://doi.org/10.3390/ijms25158189 ; Lin et al., 2024, https://doi.org/10.1186/s13053-024-00289-1 |
| Causal gene | APC | APC is the principal causal gene for classic FAP; APC pathogenic germline variants define the APC-associated form. (kyriakidis2023updatedperspectiveson pages 2-4, kyriakidis2023updatedperspectiveson pages 1-2, OpenTargets Search: familial adenomatous polyposis) | Kyriakidis et al., 2023, https://doi.org/10.2147/TACG.S372241 ; OpenTargets APC association, https://platform.opentargets.org/ |
| Epidemiology | Prevalence **2.29–3.2 per 100,000** | Reported in a 2023 review as population prevalence for FAP. (kyriakidis2023updatedperspectiveson pages 1-2) | Kyriakidis et al., 2023, https://doi.org/10.2147/TACG.S372241 |
| Epidemiology | Prevalence **~1 in 8,000–18,000** | Reported in a 2024 review; consistent with rare-disease frequency estimates. (buki2024raregermlinevariants pages 1-2) | Büki et al., 2024, https://doi.org/10.3390/ijms25158189 |
| Epidemiology | Incidence **1 in 8,300 births** | Reported by a 2024 retrospective APC cohort citing a UK genetic study. (lin2024adrenaltumoursin pages 1-2) | Lin et al., 2024, https://doi.org/10.1186/s13053-024-00289-1 |
| Epidemiology / cancer contribution | Accounts for **~0.5–1% of colorectal cancers** | Useful disease-burden context from recent review literature. (kyriakidis2023updatedperspectiveson pages 1-2) | Kyriakidis et al., 2023, https://doi.org/10.2147/TACG.S372241 |


*Table: This table summarizes core identifiers, terminology, diagnostic thresholds, inheritance, causal gene, and recent epidemiology figures for classic familial adenomatous polyposis. It is designed to support structured disease knowledge base curation using only evidence available in the current context.*

**Key identifier highlights (evidence-backed):**
- **MONDO:** classic FAP = **MONDO:0021055**; related entities include **familial adenomatous polyposis 1 (MONDO:0021056)** and **attenuated FAP (MONDO:0016362)**. (OpenTargets Search: familial adenomatous polyposis)
- **Orphanet:** Familial adenomatous polyposis = **Orphanet:733**. (OpenTargets Search: familial adenomatous polyposis)

### 1.3 Synonyms / alternative names
Common names in current use include:
- Familial adenomatous polyposis (FAP) / classic FAP (kyriakidis2023updatedperspectiveson pages 1-2, buki2024raregermlinevariants pages 1-2)
- APC-associated polyposis (genotype-first framing) (kyriakidis2023updatedperspectiveson pages 2-4)
- Gardner syndrome is described as an APC-associated variant with polyps plus osteomas and soft-tissue tumors. (buki2024raregermlinevariants pages 1-2)

### 1.4 Evidence provenance
The information in this report is derived from aggregated disease-level resources (OpenTargets) and aggregated research sources (reviews, cohort studies, trials) rather than EHR-only patient-level data, except for select case reports and institutional cohorts that were retrieved but not relied upon for core definitions. (OpenTargets Search: familial adenomatous polyposis, kyriakidis2023updatedperspectiveson pages 1-2, lin2024adrenaltumoursin pages 1-2)

---

## 2. Etiology

### 2.1 Disease causal factors
**Primary cause (genetic):** Germline loss-of-function variants in **APC** (adenomatous polyposis coli; tumor suppressor; regulator of β-catenin/Wnt signaling) are the major cause of classic FAP. (buki2024raregermlinevariants pages 1-2, kyriakidis2023updatedperspectiveson pages 1-2)

A recent review explicitly describes APC as a tumor suppressor that “regulates β-catenin and Wnt signaling.” (kyriakidis2023updatedperspectiveson pages 1-2)

### 2.2 Risk factors
#### Genetic risk factors
- **APC pathogenic variants** (germline) are the causal risk factor for classic FAP; genotype–phenotype associations exist for some extracolonic features (not universally consistent across studies). (kyriakidis2023updatedperspectiveson pages 2-4, kyriakidis2023updatedperspectiveson pages 1-2)
- **Post-zygotic/somatic mosaicism** is an important diagnostic consideration in polyposis evaluation; one nationwide study used WGS and “screening for mosaicism in blood and/or adenomas” to improve detection of APC structural variants and mosaic APC pathogenic variants. (kyriakidis2023updatedperspectiveson pages 2-4)
- **Risk modifiers (example: desmoid tumors):** A review notes markedly increased desmoid risk for certain APC regions (e.g., “mutations beyond codon 1309 and 1444” associated with ~17-fold and ~12-fold higher desmoid risk). (kyriakidis2023updatedperspectiveson pages 2-4)

#### Environmental / iatrogenic risk factors
- **Surgical/traumatic triggers for desmoids:** desmoid tumor risk factors include “trauma” and “estrogens,” and distal APC variants/family history. (kumamoto2023recentadvancesand pages 1-2)

### 2.3 Protective factors
No robust, broadly accepted protective genetic variants or environmental protective factors specific to classic FAP were supported in the retrieved excerpts. Chemoprevention remains an active area of investigation with heterogeneous adoption and variable/limited efficacy. (kyriakidis2023updatedperspectiveson pages 10-12, aelvoet2023personalizedendoscopicsurveillance pages 1-2)

### 2.4 Gene–environment interactions
Direct gene–environment interaction evidence specific to classic FAP was limited in the retrieved excerpts, but desmoid tumor risk being influenced by trauma/surgery and estrogen exposure in the context of APC pathogenic variants is a clinically relevant example of interaction. (kumamoto2023recentadvancesand pages 1-2)

---

## 3. Phenotypes

### 3.1 Core gastrointestinal phenotype (classic)
**Colorectal adenomatous polyposis**
- Phenotype type: clinical sign/endoscopic finding.
- Typical onset: adolescence/young adulthood. One review notes polyps develop with a mean age around adolescence and diagnosis often occurs in early adulthood. (buki2024raregermlinevariants pages 1-2, kyriakidis2023updatedperspectiveson pages 1-2)
- Diagnostic threshold: typically ≥100 cumulative adenomas. (karstensen2024endoscopicindicatorsin pages 1-2, lin2024adrenaltumoursin pages 1-2)

**Suggested HPO terms (examples):**
- Colonic polyposis: *Intestinal polyposis* (HP:0005220)
- Colonic adenomas: *Colonic adenomatous polyposis* (commonly modeled; exact HPO label may vary by version)

### 3.2 Upper GI phenotypes (duodenum, stomach)
**Duodenal adenomas / duodenal polyposis**
- A nationwide Danish cohort found that among those who underwent EGD, “59.2% presented with detectable duodenal adenomas.” (karstensen2024endoscopicindicatorsin pages 1-2)
- In that cohort, duodenal adenocarcinoma developed in 3.4% (17/500), and 47% of those cancers were advanced at diagnosis. (karstensen2024endoscopicindicatorsin pages 1-2)

**Suggested HPO terms:**
- Duodenal polyposis: *Duodenal polyposis* (HPO term availability depends on version)
- Duodenal adenocarcinoma: *Duodenal carcinoma* (HPO term availability depends on version)

### 3.3 Extraintestinal manifestations (selected; frequencies from recent review excerpts)
A 2023 review summarizes several extracolonic manifestations with approximate frequencies/risks:
- **Congenital hypertrophy of retinal pigment epithelium (CHRPE):** 60% (kyriakidis2023updatedperspectiveson pages 1-2)
- **Desmoid tumors:** 20% (kyriakidis2023updatedperspectiveson pages 1-2); a dedicated desmoid review cites approximately **10–25%** prevalence. (kumamoto2023recentadvancesand pages 1-2)
- **Thyroid papillary carcinoma:** 1–2% (kyriakidis2023updatedperspectiveson pages 1-2)
- **Medulloblastoma and hepatoblastoma:** ~1–2% each (kyriakidis2023updatedperspectiveson pages 1-2)
- **Osteomas:** 20% (kyriakidis2023updatedperspectiveson pages 1-2)
- **Dental and osseous anomalies** can precede intestinal polyposis; a 2024 review emphasizes early-detection relevance for dentistry. (buki2024raregermlinevariants pages 1-2)

**Suggested HPO terms (examples):**
- Desmoid tumor: *Desmoid tumor* (HP term availability depends on version)
- CHRPE: *Congenital hypertrophy of retinal pigment epithelium* (HP:0007754)
- Osteoma: *Osteoma* (HP:0011007)
- Supernumerary teeth: *Supernumerary teeth* (HP:0011060)

### 3.4 Quality-of-life impact
- A systematic review/meta-analysis of NSAID chemoprevention emphasizes that prophylactic colectomy/proctocolectomy is standard but has “major quality-of-life impacts.” (farooq2023nonsteroidalantiinflammatorydrugs pages 1-2)
- Real-world, post-surgical surveillance compliance and QoL measurement is reported in a 2024 institutional study (Saudi Arabia) using SF-36 and EORTC instruments; mean SF-36 domain scores were >60, but surveillance adherence was poor for multiple modalities. (OpenTargets Search: familial adenomatous polyposis)

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene(s)
- **APC** (HGNC symbol: APC) is the principal causal gene for classic FAP. (buki2024raregermlinevariants pages 1-2, kyriakidis2023updatedperspectiveson pages 1-2)

**OpenTargets disease–target association:** APC is strongly associated with classic FAP and FAP in OpenTargets. (OpenTargets Search: familial adenomatous polyposis)

### 4.2 Pathogenic variants and classes (high-level)
- Typical pathogenic mechanism is **loss of function** (truncating/frameshift/nonsense/splice/large deletions). (buki2024raregermlinevariants pages 1-2)
- One review reports **de novo** mutations ~25% and **large deletions** ~15% (for APC-associated disease spectrum). (buki2024raregermlinevariants pages 1-2)

**Variant class suggestions (for knowledge base):**
- Nonsense_variant (SO:0001587)
- Frameshift_variant (SO:0001589)
- Splice_donor/acceptor_variant (SO:0001575/0001574)
- Structural variants (deletions/duplications)
- Mosaic APC variants (post-zygotic)

### 4.3 Modifier genes / genetic heterogeneity
Clinical polyposis can be APC-negative and due to other genes; a 2023 review of APC-mutation–negative colorectal adenomatous polyposis highlights recessive contributors (e.g., MUTYH, NTHL1, MMR genes) and dominant contributors (POLE/POLD1, AXIN2). (zhu2023; retrieved but not used as core classic FAP evidence)

For classic FAP specifically, mosaicism and structural variants are important to consider when standard testing is negative. (kyriakidis2023updatedperspectiveson pages 2-4)

### 4.4 Epigenetics / chromosomal abnormalities
No disease-specific epigenetic signature for classic FAP was directly supported by the retrieved excerpts; however, APC loss leads to downstream transcriptional program changes via Wnt/β-catenin signaling. (kyriakidis2023updatedperspectiveson pages 1-2)

---

## 5. Environmental Information

Classic FAP is primarily genetic; however, important non-genetic contributors include:
- **Trauma/surgery as a risk factor for desmoid tumors** in APC pathogenic variant carriers. (kumamoto2023recentadvancesand pages 1-2)
- **Estrogen exposure** as a risk factor for desmoids (suggesting sex-hormone modulation of phenotype). (kumamoto2023recentadvancesand pages 1-2)

No specific infectious agents were supported as triggers in the retrieved excerpts.

---

## 6. Mechanism / Pathophysiology

### 6.1 Core molecular pathway (APC → Wnt/β-catenin dysregulation)
APC functions as a tumor suppressor regulating β-catenin and Wnt signaling; loss-of-function germline variants predispose intestinal epithelial cells to adenoma initiation, with subsequent somatic events driving adenoma–carcinoma progression. (kyriakidis2023updatedperspectiveson pages 1-2)

A review also frames FAP tumorigenesis as a multistep process, noting that carcinogenesis “typically follows APC mutation then KRAS and TP53 mutations.” (kyriakidis2023updatedperspectiveson pages 2-4)

### 6.2 Causal chain (conceptual)
1) **Germline APC loss-of-function** (one allele) establishes susceptibility in intestinal stem/crypt compartments. (kyriakidis2023updatedperspectiveson pages 1-2)
2) **Second hit** in APC (somatic) leads to β-catenin accumulation and transcriptional activation of proliferative programs (adenoma initiation). (kyriakidis2023updatedperspectiveson pages 1-2, kumamoto2023recentadvancesand pages 1-2)
3) **Progression** occurs with additional pathway alterations (e.g., KRAS/TP53), increasing dysplasia and malignant potential. (kyriakidis2023updatedperspectiveson pages 2-4)
4) **Organ-specific extracolonic disease** arises via tissue-context effects (e.g., desmoid fibroproliferation; upper GI adenomas). (kumamoto2023recentadvancesand pages 1-2, karstensen2024endoscopicindicatorsin pages 1-2)

### 6.3 Cellular processes and cell types
**Suggested GO biological process terms (examples):**
- Wnt signaling pathway (GO:0016055)
- Regulation of cell proliferation (GO:0042127)
- Epithelial cell proliferation (GO:0050673)

**Suggested Cell Ontology (CL) terms (examples):**
- Intestinal epithelial cell (CL:0000066)
- Intestinal stem cell (CL term depends on ontology version)
- Fibroblast (for desmoid tumors; CL:0000057)

---

## 7. Anatomical Structures Affected

### 7.1 Organ level
- **Colon and rectum** (primary; colorectal adenomatous polyposis). (karstensen2024endoscopicindicatorsin pages 1-2, kyriakidis2023updatedperspectiveson pages 1-2)
- **Duodenum** (major post-colectomy cancer morbidity; high prevalence of duodenal adenomas). (karstensen2024endoscopicindicatorsin pages 1-2)
- **Stomach** (fundic gland polyposis and gastric adenomas/cancer are an area of increasing concern; targeted endoscopic strategies proposed). (aelvoet2023personalizedendoscopicsurveillance pages 2-3, aelvoet2023personalizedendoscopicsurveillance pages 3-5)
- **Mesentery/abdomen (desmoid tumors)**. (kumamoto2023recentadvancesand pages 1-2)
- **Thyroid** (papillary carcinoma risk). (kyriakidis2023updatedperspectiveson pages 1-2)
- **Adrenal glands** (increased adrenal mass prevalence in APC-pathogenic cohorts). (lin2024adrenaltumoursin pages 1-2)

**Suggested UBERON terms (examples):**
- Colon (UBERON:0001155)
- Rectum (UBERON:0001052)
- Duodenum (UBERON:0002114)
- Stomach (UBERON:0000945)
- Thyroid gland (UBERON:0002046)
- Adrenal gland (UBERON:0002369)

### 7.2 Subcellular level
APC/β-catenin signaling involves cytoplasmic and nuclear β-catenin dynamics (conceptually supported by Wnt pathway role). (kyriakidis2023updatedperspectiveson pages 1-2)

---

## 8. Temporal Development

- **Onset:** polyps typically develop in adolescence; classic FAP features “hundreds to thousands of colorectal adenomatous polyps” from adolescence. (kyriakidis2023updatedperspectiveson pages 1-2)
- **Progression:** Without prophylactic surgery, CRC risk approaches certainty by age ~50 in classic FAP (review statement). (kyriakidis2023updatedperspectiveson pages 1-2)
- **Upper GI progression:** A Japanese retrospective cohort study showed marked worsening over time for duodenal adenomas, with stage progression in 71% and strong increases in HGD/large polyps/Spigelman IV over follow-up; endoscopic intervention prevented invasive cancer during observation. (nakahira2023; retrieved but not extracted as evidence ID here)

---

## 9. Inheritance and Population

### 9.1 Inheritance
- Autosomal dominant inheritance is consistently described across reviews and cohorts. (kyriakidis2023updatedperspectiveson pages 1-2, lin2024adrenaltumoursin pages 1-2)

### 9.2 Epidemiology
Recent sources report broadly concordant estimates:
- **Prevalence:** 2.29–3.2 per 100,000 (review). (kyriakidis2023updatedperspectiveson pages 1-2)
- **Prevalence:** ~1 in 8,000–18,000 (review). (buki2024raregermlinevariants pages 1-2)
- **Incidence:** 1 in 8,300 births (cited UK study within adrenal cohort paper). (lin2024adrenaltumoursin pages 1-2)

### 9.3 Penetrance/expressivity and mosaicism
- Phenotypic spectrum exists (classic vs attenuated; extracolonic manifestations). (kyriakidis2023updatedperspectiveson pages 1-2, buki2024raregermlinevariants pages 1-2)
- Mosaicism and structural variants can explain previously “unknown etiology” polyposis families; WGS and mosaic screening improved detection in a nationwide registry setting. (kyriakidis2023updatedperspectiveson pages 2-4)

---

## 10. Diagnostics

### 10.1 Clinical criteria
- Classic clinical threshold: **>100 colorectal adenomas** is repeatedly used to define classic FAP clinically. (karstensen2024endoscopicindicatorsin pages 1-2, lin2024adrenaltumoursin pages 1-2)

### 10.2 Endoscopic evaluation and staging
- Upper GI disease is commonly staged with **Spigelman**, but limitations are highlighted: “Spigelman stage IV is an imperfect predictor for duodenal cancer and poor predictor for ampullary cancer,” and modern endoscopy may inflate stage without corresponding risk. (aelvoet2023personalizedendoscopicsurveillance pages 1-2)

### 10.3 Genetic testing strategy (current practice direction)
A 2023 review summarizes practical recommendations:
- If the familial APC pathogenic/likely pathogenic variant is known, targeted single-site testing is appropriate.
- If no familial variant is known, multi-gene panels are preferred; consider evaluation for mosaicism using tissues beyond blood (e.g., polyps). (kyriakidis2023updatedperspectiveson pages 2-4)

### 10.4 Differential diagnosis
The diagnostic differential for adenomatous polyposis includes APC-associated classic/attenuated FAP and other hereditary polyposis syndromes (e.g., MUTYH-associated polyposis, polymerase proofreading-associated polyposis). While not fully enumerated in the classic-FAP excerpts, this heterogeneity is emphasized in clinical genetics discussions and OpenTargets associations. (OpenTargets Search: familial adenomatous polyposis, kyriakidis2023updatedperspectiveson pages 2-4)

---

## 11. Outcome / Prognosis

### 11.1 Cancer risks (selected quantitative estimates)
A 2023 review provides quantitative extracolonic cancer risks and frequencies:
- Duodenal cancer described as a leading post-colectomy cause of death; reported “cumulative risk ~4.5% at 57 and 18% at 75.” (kyriakidis2023updatedperspectiveson pages 1-2)
- Thyroid papillary carcinoma frequency 1–2%. (kyriakidis2023updatedperspectiveson pages 1-2)

### 11.2 Desmoid tumors as a major morbidity/mortality driver
A 2023 desmoid-focused review states desmoid tumor is “a major complication that occurs in approximately 10%–25% of familial adenomatous polyposis (FAP) patients” and notes it has been considered “the leading cause of death in patients undergoing colectomy.” (kumamoto2023recentadvancesand pages 1-2)

### 11.3 Upper GI outcomes (registry data)
In a nationwide cohort (Denmark), 3.4% developed duodenal adenocarcinoma and nearly half of those were advanced at diagnosis, reinforcing the importance of structured surveillance and effective endoscopic intervention pathways. (karstensen2024endoscopicindicatorsin pages 1-2)

---

## 12. Treatment

### 12.1 Surgical and interventional management (real-world implementation)
- **Risk-reducing colorectal surgery**: A 2023 review notes “the gold-standard treatment to reduce this risk is prophylactic colectomy, typically by the age of 40.” (kyriakidis2023updatedperspectiveson pages 1-2)
- **Persistent extracolonic risk**: colectomy “constitutes an ineffective way at preventing extra-colonic disease manifestations” such as desmoids/thyroid/duodenal polyposis. (kyriakidis2023updatedperspectiveson pages 1-2)

**Suggested MAXO terms (examples):**
- Colectomy (MAXO term; label depends on MAXO version)
- Proctocolectomy
- Endoscopic polypectomy
- Endoscopic mucosal resection (EMR)

### 12.2 Endoscopic surveillance and endoscopic therapy protocols (European FAP Consortium, 2023)
A consensus-based strategy proposes personalized surveillance intervals and explicit thresholds for endoscopic resection across the GI tract:
- Existing guidelines commonly recommend “1-, 2- or 3-yearly endoscopic surveillance of the rectum and pouch with polypectomy of adenomas >5 mm.” (aelvoet2023personalizedendoscopicsurveillance pages 2-3)
- The European FAP Consortium strategy defines personalized intervals “from 3–6 months up to 2 years,” driven by dysplasia grade, resection completeness, and residual adenoma burden. (aelvoet2023personalizedendoscopicsurveillance pages 2-3)
- Upper-GI intervention thresholds include duodenal adenoma ≥10 mm, gastric adenoma ≥5 mm, ampullary adenoma ≥10 mm or rapidly progressive, and optical suspicion of high-grade dysplasia; in heavy-burden duodenal disease, polypectomy for ≥5 mm lesions may be considered. (aelvoet2023personalizedendoscopicsurveillance pages 3-5)

**Visual evidence (flowcharts):** The retrieved figures show the proposed lower- and upper-GI surveillance algorithms and thresholds. (aelvoet2023personalizedendoscopicsurveillance media a5ca449c, aelvoet2023personalizedendoscopicsurveillance media 73b6a57e)

### 12.3 Pharmacotherapy / chemoprevention
#### NSAIDs (systematic review/meta-analysis; 2023)
A 2023 meta-analysis of 8 RCTs (279 patients) reported that NSAID therapy (mean ~6.4 months) reduced:
- polyp number by **17.4%** (95% CI 26.41% to 8.29%; low certainty)
- polyp size by **15.9%** (95% CI 24.98% to 6.73%; very low certainty)
with GI adverse events including stomatitis, diarrhea, and abdominal pain. (farooq2023nonsteroidalantiinflammatorydrugs pages 1-2)

#### EGFR inhibition (erlotinib) for duodenal polyposis (Gut, 2023)
A Phase II trial of weekly erlotinib (350 mg once weekly for 6 months) reported:
- mean duodenal polyp burden change **−29.6%** (95% CI −39.6% to −19.7%; p<0.0001)
- Spigelman downstaging in **12%**
- grade 2–3 adverse events in **71.7%**; most common was acneiform rash (56.5%)
- trial registration **NCT02961374**
(samadder2023phaseiitrial pages 1-2, samadder2023phaseiitrial pages 4-5)

Direct abstract-supported quotes include: “Duodenal polyp burden was significantly reduced after 6 months… with a mean per cent change of −29.6% (95% CI, −39.6% to −19.7%; p<0.0001)” and “Grade 2 or 3 AEs were reported in 71.7% of subjects.” (samadder2023phaseiitrial pages 1-2)

#### Eflornithine + sulindac (NEJM, 2020; Phase III)
A Phase III RCT (cited in ClinicalTrials.gov record NCT01483144) found disease progression was not significantly lower with combination therapy versus monotherapy; the registry record explicitly ties NCT01483144 to the NEJM paper (PMID listed in OpenTargets evidence as 32905675). (NCT01483144 chunk 2, OpenTargets Search: familial adenomatous polyposis)

#### Ongoing / recent trial activity (example)
A recruiting Phase III study is listed for “celecoxib and metformin” in FAP (NCT06545526). (clinical trial registry record retrieved; evidence details not fully extracted from chunks in this run) (OpenTargets Search: familial adenomatous polyposis)

### 12.4 Expert opinion / analysis (authoritative sources)
- A 2023 review concludes that despite many tested agents, “there has not yet been a chemoprevention agent” that meets desired criteria for long-term safety and clinically meaningful durable effect. (kyriakidis2023updatedperspectiveson pages 1-2)
- An international practice survey shows heterogeneous real-world chemoprevention adoption: “Sixty-nine percent… offer chemoprevention for FAP,” with sulindac and aspirin commonly selected, but substantial variability across experts. (mraz2023; retrieved but not evidence-extracted here)

---

## 13. Prevention

### 13.1 Primary/secondary/tertiary prevention in classic FAP
- **Secondary prevention** is central: early identification of at-risk relatives (cascade testing) and initiation of colonoscopic surveillance in adolescence/early adulthood is emphasized in reviews; one review notes pediatric at-risk testing/surveillance typically begins at **age 10–15**. (kyriakidis2023updatedperspectiveson pages 2-4)
- **Tertiary prevention** includes prophylactic colorectal surgery plus lifelong surveillance of retained rectum/pouch and upper-GI organs, because surgery does not eliminate extracolonic risk. (kyriakidis2023updatedperspectiveson pages 1-2)

### 13.2 Surveillance as prevention (European FAP Consortium)
The European FAP Consortium provides a prevention-oriented surveillance and intervention framework (individualized intervals 3–6 months to 2 years; explicit size thresholds for resections), intended to reduce cancer incidence while limiting unnecessary surgery. (aelvoet2023personalizedendoscopicsurveillance pages 2-3, aelvoet2023personalizedendoscopicsurveillance pages 3-5, aelvoet2023personalizedendoscopicsurveillance media a5ca449c, aelvoet2023personalizedendoscopicsurveillance media 73b6a57e)

---

## 14. Other Species / Natural Disease

The retrieved evidence in this run did not include naturally occurring veterinary FAP analogs (OMIA/VetCompass) or explicit cross-species natural disease reports.

---

## 15. Model Organisms

The weekly-erlotinib trial paper references preclinical ApcMin/+ mouse evidence (e.g., “greater than 85% decrease” in microadenoma progression in ApcMin/+ mice), indicating ongoing reliance on classic APC-driven mouse models for chemoprevention and mechanistic studies. (samadder2023phaseiitrial pages 5-6)

**Commonly used model systems (supported at least at mention level in retrieved evidence):**
- **ApcMin/+ mouse** for intestinal adenoma biology and preclinical chemoprevention. (samadder2023phaseiitrial pages 5-6)

(Additional detailed model-organism characterization—organoids, conditional Apc alleles, limitations—was not captured in the extracted evidence set of this run.)

---

# Recent Developments (2023–2024 emphasis): synthesis

1) **Shift toward personalized endoscopic management**: The European FAP Consortium proposed explicit polypectomy thresholds and individualized surveillance intervals (3–6 months to 2 years), addressing limitations of guideline vagueness and Spigelman staging. (aelvoet2023personalizedendoscopicsurveillance pages 2-3, aelvoet2023personalizedendoscopicsurveillance pages 3-5, aelvoet2023personalizedendoscopicsurveillance media a5ca449c, aelvoet2023personalizedendoscopicsurveillance media 73b6a57e)

2) **Duodenal disease burden quantified in national registers**: In Denmark, 59.2% of scoped patients had duodenal adenomas; 3.4% developed duodenal adenocarcinoma, with 47% advanced at diagnosis, highlighting ongoing unmet needs in upper-GI surveillance and intervention. (karstensen2024endoscopicindicatorsin pages 1-2)

3) **Chemoprevention evidence remains mixed**:
- NSAIDs show modest reductions in polyp number/size in meta-analysis, with low/very-low certainty and heterogeneity. (farooq2023nonsteroidalantiinflammatorydrugs pages 1-2)
- Targeted EGFR inhibition (weekly erlotinib) demonstrated a ~30% reduction in duodenal polyp burden but with frequent (mostly grade 2) adverse events. (samadder2023phaseiitrial pages 1-2, samadder2023phaseiitrial pages 4-5)

4) **Extracolonic phenotype expansion in contemporary cohorts**: Increased recognition of adrenal masses in APC-pathogenic cohorts (26.7% prevalence in one series) underscores broader surveillance considerations beyond classic organs. (lin2024adrenaltumoursin pages 1-2)

---

# URLs and publication dates (key sources used)
- OpenTargets (disease–target associations; includes MONDO/Orphanet IDs): https://platform.opentargets.org/ (platform snapshot in evidence context) (OpenTargets Search: familial adenomatous polyposis)
- Kyriakidis et al. “Updated Perspectives…” (Aug 2023): https://doi.org/10.2147/TACG.S372241 (kyriakidis2023updatedperspectiveson pages 1-2)
- Aelvoet et al. European FAP Consortium strategy (Jan 2023): https://doi.org/10.1055/a-2011-1933 (aelvoet2023personalizedendoscopicsurveillance pages 1-2)
- Samadder et al. weekly erlotinib Phase II (May 2023): https://doi.org/10.1136/gutjnl-2021-326532 (samadder2023phaseiitrial pages 1-2)
- Karstensen et al. Danish cohort duodenal indicators (Jul 2024): https://doi.org/10.1007/s10689-024-00415-x (karstensen2024endoscopicindicatorsin pages 1-2)
- Büki et al. APC variants and dental/osseous anomalies (Jul 2024): https://doi.org/10.3390/ijms25158189 (buki2024raregermlinevariants pages 1-2)
- Lin et al. Adrenal tumors in APC carriers (Sep 2024): https://doi.org/10.1186/s13053-024-00289-1 (lin2024adrenaltumoursin pages 1-2)
- Farooq et al. NSAID chemoprevention meta-analysis (Jun 2023): https://doi.org/10.1016/j.gastha.2023.05.009 (farooq2023nonsteroidalantiinflammatorydrugs pages 1-2)

---

## Appendix: Trial identifiers mentioned
- NCT02961374 (weekly erlotinib Phase II; Gut 2023) (samadder2023phaseiitrial pages 1-2)
- NCT01483144 (eflornithine + sulindac Phase III; ClinicalTrials.gov record) (NCT01483144 chunk 2)

---

## Included visual evidence
- European FAP Consortium flowcharts (lower GI and upper GI surveillance/thresholds): (aelvoet2023personalizedendoscopicsurveillance media a5ca449c, aelvoet2023personalizedendoscopicsurveillance media 73b6a57e)

References

1. (karstensen2024endoscopicindicatorsin pages 1-2): JG Karstensen, MD Wewer, S. Bülow, TVO Hansen, H. Højen, AM Jelsig, TP Kuhlmann, J. Burisch, and HC Pommergaard. Endoscopic indicators in patients with familial adenomatous polyposis undergoing duodenal resections – a nationwide danish cohort study with long-term follow-up. Familial Cancer, 23:607-615, Jul 2024. URL: https://doi.org/10.1007/s10689-024-00415-x, doi:10.1007/s10689-024-00415-x. This article has 0 citations and is from a peer-reviewed journal.

2. (kyriakidis2023updatedperspectiveson pages 1-2): Filippos Kyriakidis, Dionysios Kogias, Theodora Maria Venou, Eleni Karlafti, and Daniel Paramythiotis. Updated perspectives on the diagnosis and management of familial adenomatous polyposis. The Application of Clinical Genetics, 16:139-153, Aug 2023. URL: https://doi.org/10.2147/tacg.s372241, doi:10.2147/tacg.s372241. This article has 22 citations.

3. (OpenTargets Search: familial adenomatous polyposis): Open Targets Query (familial adenomatous polyposis, 19 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

4. (buki2024raregermlinevariants pages 1-2): Gergely Büki, Gréta Antal, and Judit Bene. Rare germline variants in the adenomatous polyposis coli gene associated with dental and osseous anomalies. International Journal of Molecular Sciences, 25:8189, Jul 2024. URL: https://doi.org/10.3390/ijms25158189, doi:10.3390/ijms25158189. This article has 7 citations.

5. (kyriakidis2023updatedperspectiveson pages 2-4): Filippos Kyriakidis, Dionysios Kogias, Theodora Maria Venou, Eleni Karlafti, and Daniel Paramythiotis. Updated perspectives on the diagnosis and management of familial adenomatous polyposis. The Application of Clinical Genetics, 16:139-153, Aug 2023. URL: https://doi.org/10.2147/tacg.s372241, doi:10.2147/tacg.s372241. This article has 22 citations.

6. (lin2024adrenaltumoursin pages 1-2): Lyman Lin, Victoria Beshay, and Finlay Macrae. Adrenal tumours in patients with pathogenic apc mutations: a retrospective study. Hereditary Cancer in Clinical Practice, Sep 2024. URL: https://doi.org/10.1186/s13053-024-00289-1, doi:10.1186/s13053-024-00289-1. This article has 5 citations and is from a peer-reviewed journal.

7. (kumamoto2023recentadvancesand pages 1-2): Kensuke Kumamoto, Hideyuki Ishida, and Naohiro Tomita. Recent advances and current management for desmoid tumor associated with familial adenomatous polyposis. Journal of the Anus, Rectum and Colon, 7:38-51, Apr 2023. URL: https://doi.org/10.23922/jarc.2022-074, doi:10.23922/jarc.2022-074. This article has 11 citations.

8. (kyriakidis2023updatedperspectiveson pages 10-12): Filippos Kyriakidis, Dionysios Kogias, Theodora Maria Venou, Eleni Karlafti, and Daniel Paramythiotis. Updated perspectives on the diagnosis and management of familial adenomatous polyposis. The Application of Clinical Genetics, 16:139-153, Aug 2023. URL: https://doi.org/10.2147/tacg.s372241, doi:10.2147/tacg.s372241. This article has 22 citations.

9. (aelvoet2023personalizedendoscopicsurveillance pages 1-2): Arthur S. Aelvoet, Maria Pellisé, Barbara A.J. Bastiaansen, Monique E. van Leerdam, Rodrigo Jover, Francesc Balaguer, Michal F. Kaminski, John G. Karstensen, Jean-Christophe Saurin, Roel Hompes, Patrick M.M. Bossuyt, Luigi Ricciardiello, Andrew Latchford, and Evelien Dekker. Personalized endoscopic surveillance and intervention protocols for patients with familial adenomatous polyposis: the european fap consortium strategy. Endoscopy International Open, 11:E386-E393, Jan 2023. URL: https://doi.org/10.1055/a-2011-1933, doi:10.1055/a-2011-1933. This article has 26 citations and is from a peer-reviewed journal.

10. (farooq2023nonsteroidalantiinflammatorydrugs pages 1-2): Umer Farooq, Abdallah El Alayli, Abhiram Duvvuri, Razan Mansour, Ravi Teja Pasam, Sahithi Malireddy, Reem A. Mustafa, and Ajay Bansal. Nonsteroidal anti-inflammatory drugs for chemoprevention in patients with familial adenomatous polyposis: a systematic review and meta-analysis. Gastro Hep Advances, 2:1005-1013, Jun 2023. URL: https://doi.org/10.1016/j.gastha.2023.05.009, doi:10.1016/j.gastha.2023.05.009. This article has 6 citations and is from a peer-reviewed journal.

11. (aelvoet2023personalizedendoscopicsurveillance pages 2-3): Arthur S. Aelvoet, Maria Pellisé, Barbara A.J. Bastiaansen, Monique E. van Leerdam, Rodrigo Jover, Francesc Balaguer, Michal F. Kaminski, John G. Karstensen, Jean-Christophe Saurin, Roel Hompes, Patrick M.M. Bossuyt, Luigi Ricciardiello, Andrew Latchford, and Evelien Dekker. Personalized endoscopic surveillance and intervention protocols for patients with familial adenomatous polyposis: the european fap consortium strategy. Endoscopy International Open, 11:E386-E393, Jan 2023. URL: https://doi.org/10.1055/a-2011-1933, doi:10.1055/a-2011-1933. This article has 26 citations and is from a peer-reviewed journal.

12. (aelvoet2023personalizedendoscopicsurveillance pages 3-5): Arthur S. Aelvoet, Maria Pellisé, Barbara A.J. Bastiaansen, Monique E. van Leerdam, Rodrigo Jover, Francesc Balaguer, Michal F. Kaminski, John G. Karstensen, Jean-Christophe Saurin, Roel Hompes, Patrick M.M. Bossuyt, Luigi Ricciardiello, Andrew Latchford, and Evelien Dekker. Personalized endoscopic surveillance and intervention protocols for patients with familial adenomatous polyposis: the european fap consortium strategy. Endoscopy International Open, 11:E386-E393, Jan 2023. URL: https://doi.org/10.1055/a-2011-1933, doi:10.1055/a-2011-1933. This article has 26 citations and is from a peer-reviewed journal.

13. (aelvoet2023personalizedendoscopicsurveillance media a5ca449c): Arthur S. Aelvoet, Maria Pellisé, Barbara A.J. Bastiaansen, Monique E. van Leerdam, Rodrigo Jover, Francesc Balaguer, Michal F. Kaminski, John G. Karstensen, Jean-Christophe Saurin, Roel Hompes, Patrick M.M. Bossuyt, Luigi Ricciardiello, Andrew Latchford, and Evelien Dekker. Personalized endoscopic surveillance and intervention protocols for patients with familial adenomatous polyposis: the european fap consortium strategy. Endoscopy International Open, 11:E386-E393, Jan 2023. URL: https://doi.org/10.1055/a-2011-1933, doi:10.1055/a-2011-1933. This article has 26 citations and is from a peer-reviewed journal.

14. (aelvoet2023personalizedendoscopicsurveillance media 73b6a57e): Arthur S. Aelvoet, Maria Pellisé, Barbara A.J. Bastiaansen, Monique E. van Leerdam, Rodrigo Jover, Francesc Balaguer, Michal F. Kaminski, John G. Karstensen, Jean-Christophe Saurin, Roel Hompes, Patrick M.M. Bossuyt, Luigi Ricciardiello, Andrew Latchford, and Evelien Dekker. Personalized endoscopic surveillance and intervention protocols for patients with familial adenomatous polyposis: the european fap consortium strategy. Endoscopy International Open, 11:E386-E393, Jan 2023. URL: https://doi.org/10.1055/a-2011-1933, doi:10.1055/a-2011-1933. This article has 26 citations and is from a peer-reviewed journal.

15. (samadder2023phaseiitrial pages 1-2): N Jewel Samadder, Nathan Foster, Ryan P McMurray, Carol A Burke, Elena Stoffel, Priyanka Kanth, Rohit Das, Marcia Cruz-Correa, E Vilar, Gautam Mankaney, Navtej Buttar, Selvi Thirumurthi, Danielle K Turgeon, Michael Sossenheimer, Michelle Westover, Ellen Richmond, Asad Umar, Gary Della'Zanna, Luz M Rodriguez, Eva Szabo, David Zahrieh, and Paul J Limburg. Phase ii trial of weekly erlotinib dosing to reduce duodenal polyp burden associated with familial adenomatous polyposis. Gut, 72:256-263, May 2023. URL: https://doi.org/10.1136/gutjnl-2021-326532, doi:10.1136/gutjnl-2021-326532. This article has 24 citations and is from a highest quality peer-reviewed journal.

16. (samadder2023phaseiitrial pages 4-5): N Jewel Samadder, Nathan Foster, Ryan P McMurray, Carol A Burke, Elena Stoffel, Priyanka Kanth, Rohit Das, Marcia Cruz-Correa, E Vilar, Gautam Mankaney, Navtej Buttar, Selvi Thirumurthi, Danielle K Turgeon, Michael Sossenheimer, Michelle Westover, Ellen Richmond, Asad Umar, Gary Della'Zanna, Luz M Rodriguez, Eva Szabo, David Zahrieh, and Paul J Limburg. Phase ii trial of weekly erlotinib dosing to reduce duodenal polyp burden associated with familial adenomatous polyposis. Gut, 72:256-263, May 2023. URL: https://doi.org/10.1136/gutjnl-2021-326532, doi:10.1136/gutjnl-2021-326532. This article has 24 citations and is from a highest quality peer-reviewed journal.

17. (NCT01483144 chunk 2):  Trial of Eflornithine Plus Sulindac in Patients With Familial Adenomatous Polyposis (FAP). Cancer Prevention Pharmaceuticals, Inc.. 2013. ClinicalTrials.gov Identifier: NCT01483144

18. (samadder2023phaseiitrial pages 5-6): N Jewel Samadder, Nathan Foster, Ryan P McMurray, Carol A Burke, Elena Stoffel, Priyanka Kanth, Rohit Das, Marcia Cruz-Correa, E Vilar, Gautam Mankaney, Navtej Buttar, Selvi Thirumurthi, Danielle K Turgeon, Michael Sossenheimer, Michelle Westover, Ellen Richmond, Asad Umar, Gary Della'Zanna, Luz M Rodriguez, Eva Szabo, David Zahrieh, and Paul J Limburg. Phase ii trial of weekly erlotinib dosing to reduce duodenal polyp burden associated with familial adenomatous polyposis. Gut, 72:256-263, May 2023. URL: https://doi.org/10.1136/gutjnl-2021-326532, doi:10.1136/gutjnl-2021-326532. This article has 24 citations and is from a highest quality peer-reviewed journal.
