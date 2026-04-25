---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T17:27:10.019150'
end_time: '2026-04-04T17:33:15.329926'
duration_seconds: 365.31
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Yaws
  mondo_id: ''
  category: Infectious Disease
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
- **Disease Name:** Yaws
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Yaws** covering all of the
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
- **Disease Name:** Yaws
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Yaws** covering all of the
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


## Comprehensive Disease Characteristics Report: Yaws (Infectious Disease)

### Executive summary
Yaws is a non-venereal endemic treponematosis caused by *Treponema pallidum* subsp. *pertenue* (TPE), transmitted primarily by skin-to-skin contact with infectious lesions and disproportionately affecting children in tropical, resource-limited settings. (barton2024theeffectof pages 1-3, beiras2024knowledgeattitudesand pages 1-2)

A 2024–2025 evidence base highlights (i) operational progress and limitations of azithromycin-based mass drug administration (MDA)/Total Community Treatment (TCT), (ii) increasing use of point-of-care serology plus molecular diagnostics to address misclassification of “yaws-like” ulcers, (iii) genomic epidemiology showing local persistence/re-emergence after MDA and documenting azithromycin resistance associated with 23S rRNA mutations, and (iv) strong genomic evidence that nonhuman primates can harbor TPE strains genomically indistinguishable from human strains, complicating true eradication. (tabah2024themorgesstrategy pages 1-5, barton2024theeffectof pages 1-3, medappa2024lowgeneticdiversitya pages 1-2, janeckova2023thegenomesof pages 1-2)

| Topic | Key findings (with quantitative values) | Source (first author year, journal) | PMID/DOI | URL | Evidence type |
|---|---|---|---|---|---|
| Definition / etiology | Yaws is a neglected tropical disease caused by *Treponema pallidum* subsp. *pertenue* (TPE); transmission is by skin-to-skin contact with infectious ulcers. It primarily affects children in tropical rural settings; ~75% of new cases occur in those aged <15 years. Historical first eradication campaign reduced prevalence by ~95% (vicar2025yawsinafrica pages 1-2, barton2024theeffectof pages 1-3, beiras2024knowledgeattitudesand pages 1-2) | Vicar 2025, *Diseases*; Barton 2024, *medRxiv*; Beiras 2024, *PLoS Negl Trop Dis* | 10.3390/diseases13010014; 10.1101/2024.10.27.24316187; 10.1371/journal.pntd.0012224 | https://doi.org/10.3390/diseases13010014; https://doi.org/10.1101/2024.10.27.24316187; https://doi.org/10.1371/journal.pntd.0012224 | Human clinical / implementation |
| Epidemiology | Yaws is currently reported/endemic in at least 13-15 countries depending on source framing; one 2025 guidance article states that in 2023, 222,652 suspected yaws cases were reported to WHO from 13 countries. In Africa, reported prevalence across reviewed studies ranged from 0.50% to 43.0% (vicar2025yawsinafrica pages 1-2, vicar2025yawsinafrica pages 2-4) | Vicar 2025, *Diseases*; Mitjà 2025, *PLoS Negl Trop Dis* | 10.3390/diseases13010014; 10.1371/journal.pntd.0012899 | https://doi.org/10.3390/diseases13010014; https://doi.org/10.1371/journal.pntd.0012899 | Epidemiology / implementation |
| Clinical stages / onset timeline | Primary stage: incubation 10-90 days (mean ~3 weeks), often “mother yaw” papule. Primary lesions may heal in 3-6 months. Secondary stage may occur up to ~2 years after primary and can involve skin and bone. Latent stage: seroreactive without symptoms. Tertiary stage is noninfectious, may occur in ~10% within 5-10 years and causes destructive tissue/bone disease (barton2024theeffectof pages 1-3, irawan2024comparisonofthe pages 1-2, vicar2025yawsinafrica pages 1-2) | Barton 2024, *medRxiv*; Irawan 2024, *J Infect Dev Ctries*; Vicar 2025, *Diseases* | 10.1101/2024.10.27.24316187; 10.3855/jidc.17753; 10.3390/diseases13010014 | https://doi.org/10.1101/2024.10.27.24316187; https://doi.org/10.3855/jidc.17753; https://doi.org/10.3390/diseases13010014 | Human clinical |
| Diagnostics: serology / DPP / RPR / TPHA | Diagnosis relies on clinical findings plus serology: treponemal and non-treponemal tests used together (e.g., TPHA/TPPA with RPR/VDRL); DPP point-of-care testing is used for combined treponemal/non-treponemal screening. In the Ashanti (Ghana) study, DPP seroprevalence was 17.3% in yaws-like lesions and 10.8% in syphilis-like lesions (vicar2025yawsinafrica pages 7-8, boaitey2024prevalenceofyaws pages 7-8, boaitey2024prevalenceofyaws pages 2-4) | Vicar 2025, *Diseases*; Boaitey 2024, *PLoS ONE* | 10.3390/diseases13010014; 10.1371/journal.pone.0295088 | https://doi.org/10.3390/diseases13010014; https://doi.org/10.1371/journal.pone.0295088 | Human clinical |
| Diagnostics: molecular / differential diagnosis | Multiplex PCR improves specificity and identifies non-treponemal causes of yaws-like ulcers. In Ashanti, among 110 yaws-like lesions, PCR detected *Haemophilus ducreyi* in 9.1% (10/110), HSV-1 in 1.8% (2/110), and *T. pallidum* in 0.9% (1/110); among 46 syphilis-like lesions, HSV-2 was detected in 28.3% (13/46). One yaws-like lesion was DPP-negative but PCR-positive for *T. pallidum*, consistent with early disease (boaitey2024prevalenceofyaws pages 1-2, boaitey2024prevalenceofyaws pages 7-8, boaitey2024prevalenceofyaws pages 10-11) | Boaitey 2024, *PLoS ONE* | 10.1371/journal.pone.0295088 | https://doi.org/10.1371/journal.pone.0295088 | Human clinical |
| Diagnostics: RDT performance | In 195 Indonesian children aged 2-15 years, 116 had clinical symptoms but only 13 were serologically positive. Standard Q Syphilis Ab RDT performance: versus TPHA sensitivity 93.3%, specificity 99.4%; versus RPR sensitivity 100%, specificity 98.4%. Authors concluded it is suitable for screening, with RPR still needed for confirmation in unusual cases (irawan2024comparisonofthe pages 1-2) | Irawan 2024, *J Infect Dev Ctries* | 10.3855/jidc.17753 | https://doi.org/10.3855/jidc.17753 | Human clinical |
| Genomic typing / MLST | In Papua New Guinea (2018-2019), 1,081 ulcer swabs were collected; 302/1,081 (28.5%) were TPE PCR-positive and 255/302 (84.4%) were fully typed using a new MLST scheme. Low diversity was observed with three genotypes (JE11, SE22, TE13). PCR positivity was higher in younger patients, single ulcers, first episodes, and ulcers <6 months (medappa2024lowgeneticdiversitya pages 1-2) | Medappa 2024, journal not specified in context | 10.1371/journal.pntd.0011831 | https://doi.org/10.1371/journal.pntd.0011831 | Genomic / human clinical |
| Treatment | Single-dose oral azithromycin (30 mg/kg) was shown non-inferior/equally efficacious to single-dose intramuscular benzathine penicillin and became WHO-preferred therapy. Historical penicillin campaigns treated >50 million of ~300 million screened and reduced prevalence by ~95%-98% (tabah2024themorgesstrategy pages 1-5, vicar2025yawsinafrica pages 1-2, vicar2025yawsinafrica pages 7-8) | Tabah 2024, *medRxiv*; Vicar 2025, *Diseases* | 10.1101/2024.11.07.24316738; 10.3390/diseases13010014 | https://doi.org/10.1101/2024.11.07.24316738; https://doi.org/10.3390/diseases13010014 | Human clinical / implementation |
| Eradication strategy / Morges / TCT | WHO Morges strategy uses total community treatment (TCT) with azithromycin followed by surveillance and targeted treatment. In the Congo-Basin implementation, 17 health districts across 3 countries targeted 1,530,014 people; first-round coverage was 95.21% overall (Cameroon 92.92%, CAR 96.21%, Congo 96.96%). In Cameroon, a second round reached 95.73%. Active yaws prevalence fell overall from 6.5% to 0.4% (Cameroon 6.31% to 0.23%; CAR 2.4% to 0.8%; Congo 10.8% to 3.7%) (tabah2024themorgesstrategy pages 1-5) | Tabah 2024, *medRxiv* | 10.1101/2024.11.07.24316738 | https://doi.org/10.1101/2024.11.07.24316738 | Implementation |
| Repeated MDA outcomes | In a cluster-randomized PNG trial population of 56,676 people, three rounds of MDA gave greater suppression than one MDA plus targeted treatment: active cases were reduced 11-fold versus three-fold. WGS on 263 swabs recovered 222 genomes and identified 29 fine-scale sub-lineages; 10 were eliminated by MDA, while multiple pre-existing local sub-lineages drove re-emergence (barton2024theeffectof pages 1-3, barton2024theeffectof pages 12-14) | Barton 2024, *medRxiv* | 10.1101/2024.10.27.24316187 | https://doi.org/10.1101/2024.10.27.24316187 | Implementation / genomic |
| Resistance | Macrolide resistance is linked to 23S rRNA mutations. Prior and current PNG genomic studies identified azithromycin resistance mutations including A2058G and A2059G. In one 2024 PNG typing study, A2058G was found in three JE11 isolates; in the repeated-MDA genomic study, macrolide resistance emerged/spread to three children (barton2024theeffectof pages 1-3, medappa2024lowgeneticdiversitya pages 1-2, vicar2025yawsinafrica pages 11-11) | Barton 2024, *medRxiv*; Medappa 2024, journal not specified in context | 10.1101/2024.10.27.24316187; 10.1371/journal.pntd.0011831 | https://doi.org/10.1101/2024.10.27.24316187; https://doi.org/10.1371/journal.pntd.0011831 | Genomic |
| Reservoirs | Finished whole-genome comparisons showed TPE strains from nonhuman primates and humans are genomically indistinguishable, indicating that nonhuman primates can harbor the yaws bacterium. Authors note spillover evidence is limited, but surveillance is important in areas where NHPs are naturally infected even after human elimination (janeckova2023thegenomesof pages 9-10) | Janečková 2023, *PLoS Negl Trop Dis* | 10.1371/journal.pntd.0011602 | https://doi.org/10.1371/journal.pntd.0011602 | Genomic |


*Table: This table consolidates disease definition, epidemiology, staging, diagnostics, treatment, eradication strategy, resistance, and reservoir evidence for yaws using only the provided tool context. It is useful as a compact knowledge-base-ready summary with quantitative values, source metadata, and evidence types.*

---

## 1. Disease Information

### 1.1 Overview (current understanding)
Yaws is a neglected tropical disease and endemic treponematosis caused by the spirochete *Treponema pallidum* subsp. *pertenue* (TPE). It is clinically characterized by early contagious skin lesions and, in a subset of untreated infections, late destructive disease affecting cartilage and bone. (tabah2024themorgesstrategy pages 1-5, barton2024theeffectof pages 1-3)

Direct abstract support (examples):
- “Yaws… remains a significant public health concern… primarily affecting children in remote areas with limited access to hygiene and sanitation.” (Beiras et al., published 2024-06-20; https://doi.org/10.1371/journal.pntd.0012224) (beiras2024knowledgeattitudesand pages 1-2)
- “Yaws is targeted for eradication by 2030.” (Tabah et al., posted 2024-11; https://doi.org/10.1101/2024.11.07.24316738) (tabah2024themorgesstrategy pages 1-5)

### 1.2 Key identifiers (ICD/MeSH/MONDO/Orphanet)
In the retrieved full-text corpus for this run, formal ICD-10/ICD-11 codes, MeSH IDs, Orphanet IDs, and MONDO IDs were not explicitly stated; therefore, they cannot be reliably asserted here without introducing uncited information. (boaitey2024prevalenceofyaws pages 1-2, beiras2024knowledgeattitudesand pages 1-2)

### 1.3 Synonyms and alternative names
- “Endemic treponematoses” (used in a recent implementation paper describing yaws within this group). (tabah2024themorgesstrategy pages 1-5)
- “Treponematosis/treponematoses” used in contemporary epidemiologic/differential-diagnosis framing. (vicar2025yawsinafrica pages 2-4, boaitey2024prevalenceofyaws pages 1-2)

### 1.4 Evidence source type
The information in this report is derived from aggregated disease-level resources (reviews, implementation reports, genomic epidemiology studies) and population-based studies rather than individual EHR-only observations. (barton2024theeffectof pages 1-3, tabah2024themorgesstrategy pages 1-5)

---

## 2. Etiology

### 2.1 Disease causal factors
**Infectious agent (primary cause):**
- *Treponema pallidum* subsp. *pertenue* (TPE). (barton2024theeffectof pages 1-3, janeckova2023thegenomesof pages 1-2)

**Transmission mechanism (proximal cause):**
- Non-venereal, largely via **direct skin-to-skin contact** with exudate from infectious lesions/ulcers. (tabah2024themorgesstrategy pages 1-5, beiras2024knowledgeattitudesand pages 1-2)

### 2.2 Risk factors (host/environment)
Evidence in the retrieved sources emphasizes contextual risk:
- Tropical settings with limited access to hygiene/sanitation and remote communities. (beiras2024knowledgeattitudesand pages 1-2)
- Overcrowding and poor personal/environmental hygiene facilitating spread. (tabah2024themorgesstrategy pages 1-5)
- Age: majority of cases occur in children <15 years (e.g., “75% of new cases in those aged below 15 years”). (barton2024theeffectof pages 1-3)

### 2.3 Protective factors
The retrieved corpus does not provide genetic protective variants or quantified environmental protective factors for yaws; prevention appears dominated by interruption of transmission via MDA/TCT and surveillance rather than host-genetic protection. (tabah2024themorgesstrategy pages 1-5)

### 2.4 Gene–environment interactions
No direct gene–environment interaction evidence (human host genetics interacting with exposure) was present in the retrieved texts. (barton2024theeffectof pages 1-3)

---

## 3. Phenotypes

### 3.1 Core clinical phenotypes and staging
**Staging (with timing):**
- Incubation: 10–90 days (mean ~3 weeks) before primary lesions. (irawan2024comparisonofthe pages 1-2)
- Primary lesions: often heal in ~3–6 months (but may become latent). (barton2024theeffectof pages 1-3, irawan2024comparisonofthe pages 1-2)
- Secondary disease: disseminated lesions; can occur up to ~2 years after primary lesion onset; may involve systemic symptoms and infectious exudative lesions. (irawan2024comparisonofthe pages 1-2)
- Latent stage: seroreactive without symptoms. (irawan2024comparisonofthe pages 1-2)
- Tertiary: described as non-infectious, occurring in ~10% within 5–10 years with tissue damage and persistent bone deformities. (irawan2024comparisonofthe pages 1-2)

**Skin and bone involvement:** contemporary sources frame yaws as affecting “mainly… the skin and bones” and describe late destructive bone lesions. (irawan2024comparisonofthe pages 1-2, barton2024theeffectof pages 1-3)

### 3.2 Differential diagnosis phenotypes (yaws-like ulcers are not always treponemal)
A 2024 Ghana study illustrates frequent alternative etiologies in clinically similar lesions:
- In yaws-like lesions (n=110), multiplex PCR found **9.1% *Haemophilus ducreyi***, **1.8% HSV-1**, and **0.9% *T. pallidum***. (Boaitey et al., published 2024-05-22; https://doi.org/10.1371/journal.pone.0295088) (boaitey2024prevalenceofyaws pages 1-2)
- In syphilis-like lesions (n=46), **28.3% HSV-2** was detected. (boaitey2024prevalenceofyaws pages 1-2)

This supports a key operational concept: syndromic “skin ulcer” programs must consider non-treponemal pathogens to avoid over-attribution to yaws and to ensure appropriate antivirals (for HSV) where relevant. (boaitey2024prevalenceofyaws pages 1-2)

### 3.3 Suggested HPO term mappings (curated suggestions; not explicitly asserted by sources)
Based on described phenotypes:
- Skin ulcer: HP:0001056
- Skin papule: HP:0000980
- Hyperkeratosis (palms/soles): HP:0000962 (or palmoplantar keratoderma HP:0000982)
- Osteitis / periostitis / bone pain (bone involvement noted across clinical descriptions): HP:0002754 (osteitis), HP:0002716 (periostitis), HP:0002653 (bone pain)
- Lymphadenopathy (secondary stage described): HP:0002716 is periostitis; for lymphadenopathy use HP:0002716? (avoid mislabel); suggested: HP:0002716 is incorrect; instead **HP:0002716 lymphadenopathy** is not correct; therefore no HPO ID is asserted here.

(These are ontology suggestions to aid knowledge-base mapping; the retrieved texts did not provide explicit ontology IDs.) (irawan2024comparisonofthe pages 1-2)

---

## 4. Genetic/Molecular Information

### 4.1 Causal genes and pathogenic variants (human)
Not applicable as a primary genetic disease: yaws is infectious. No human germline causal genes/variants were provided in retrieved sources. (barton2024theeffectof pages 1-3)

### 4.2 Pathogen genomics (TPE)
**Low genetic diversity and typing in Papua New Guinea (PNG):**
- 1,081 ulcer swabs collected during an MDA study; **302/1,081 (28.5%) TPE PCR-positive**; **255/302 (84.4%) fully typed** by MLST. (medappa2024lowgeneticdiversitya pages 1-2)
- Low diversity with three genotypes (JE11, SE22, TE13). (medappa2024lowgeneticdiversitya pages 1-2)

**Whole-genome sequencing during repeated MDA trial:**
- WGS on 263 swabs recovered 222 good-quality TPE genomes; identified 29 fine-scale sub-lineages, with differential elimination/persistence across study arms. (barton2024theeffectof pages 1-3)

### 4.3 Antimicrobial resistance mechanisms (pathogen)
**Macrolide (azithromycin) resistance is associated with 23S rRNA mutations**:
- In the repeated-MDA genomic epidemiology study, “Repeated rounds of MDA… led to emergence and spread of azithromycin resistance to three children.” (Barton et al., posted 2024-10; https://doi.org/10.1101/2024.10.27.24316187) (barton2024theeffectof pages 1-3)
- A 2018–2019 PNG cluster-randomized trial summary in the same preprint notes “three epidemiologically linked cases harbouring the 23S rRNA A2058G” mutation. (barton2024theeffectof pages 1-3)
- In the PNG typing study, an A2058G mutation was found in three JE11 isolates. (medappa2024lowgeneticdiversitya pages 1-2)

**Additional genomic signals under selection during MDA:**
- Persistent sub-lineages with nonsynonymous mutations in penicillin-binding proteins were observed in the repeated-MDA study. (barton2024theeffectof pages 1-3)

---

## 5. Environmental Information

### 5.1 Environmental and lifestyle factors
The retrieved evidence frames yaws as associated with poverty-linked environmental conditions (limited hygiene/sanitation, overcrowding) rather than specific toxins or lifestyle exposures. (tabah2024themorgesstrategy pages 1-5, beiras2024knowledgeattitudesand pages 1-2)

### 5.2 Infectious agents (differential/coinfections in ulcer syndromes)
- *Haemophilus ducreyi* and HSV-1/HSV-2 can cause yaws-like/syphilis-like lesions and were detected by PCR in Ghana (see Section 3.2). (boaitey2024prevalenceofyaws pages 1-2)

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (high-level, evidence-aligned)
1) Exposure to lesion exudate via skin-to-skin contact leads to inoculation with TPE. (tabah2024themorgesstrategy pages 1-5)
2) Primary infection manifests as early skin lesions; a portion resolves or becomes latent. (irawan2024comparisonofthe pages 1-2)
3) Secondary dissemination affects skin and bones; late tertiary disease can produce destructive bone lesions and deformities in a subset of untreated cases. (barton2024theeffectof pages 1-3, irawan2024comparisonofthe pages 1-2)
4) Programmatically, asymptomatic/latent infection contributes to persistence and re-emergence after MDA, consistent with genomic evidence that re-emergence is largely local and driven by pre-existing sub-lineages. (barton2024theeffectof pages 1-3)

### 6.2 Suggested GO biological process terms (inferred mapping suggestions)
The retrieved sources do not provide mechanistic pathway-level data (e.g., cytokine signatures). For knowledge-base mapping, plausible GO terms consistent with infectious skin/bone pathology include:
- GO:0006954 inflammatory response
- GO:0009615 response to virus (for HSV differential in ulcers)
- GO:0007155 cell adhesion / GO:0006955 immune response (broad)

These are suggestions only; explicit molecular pathway profiling was not present in the retrieved texts. (boaitey2024prevalenceofyaws pages 1-2)

### 6.3 Suggested Cell Ontology (CL) terms (inferred)
Not directly provided. For mapping inflammatory skin lesions and ulcer exudate, candidate CL terms may include:
- CL:0000623 neutrophil
- CL:0000542 lymphocyte
- CL:0000235 macrophage

(Again, suggestions only; not explicitly measured in sources.) (irawan2024comparisonofthe pages 1-2)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/tissue level
- Skin (primary/secondary lesions): repeatedly emphasized. (barton2024theeffectof pages 1-3, irawan2024comparisonofthe pages 1-2)
- Bone and cartilage (late destructive lesions; “severe bone lesions” / bone deformities). (barton2024theeffectof pages 1-3, tabah2024themorgesstrategy pages 1-5)

### 7.2 Suggested UBERON mappings (inferred)
- Skin: UBERON:0002097
- Bone tissue: UBERON:0001474
- Cartilage: UBERON:0002418

Not explicitly provided in sources; included as mapping suggestions. (tabah2024themorgesstrategy pages 1-5)

---

## 8. Temporal Development

- Typical onset: childhood in endemic settings; 75% of new cases in those <15 years. (barton2024theeffectof pages 1-3)
- Incubation: 10–90 days (mean ~3 weeks). (irawan2024comparisonofthe pages 1-2)
- Natural history: primary lesions heal in months; tertiary disease (subset) within 5–10 years. (irawan2024comparisonofthe pages 1-2)

---

## 9. Inheritance and Population

### 9.1 Epidemiology (recent statistics)
- Ghana (Ashanti region): among people with yaws-like lesions, seroprevalence of *T. pallidum* antibodies by point-of-care testing was **17.2%** (reported in abstract) and 17.3% (in body excerpt), indicating substantial background treponemal seroreactivity in clinically suspected cases. (boaitey2024prevalenceofyaws pages 1-2, boaitey2024prevalenceofyaws pages 7-8)
- In Indonesia RDT evaluation context: “An estimated 75% of new cases were found in children under 15.” (irawan2024comparisonofthe pages 1-2)

The retrieved corpus for this run does not include a GBD-style global incidence estimate specific to 2023–2024; a modeling burden estimate in a 2024 preprint states: “Without an eradication campaign, yaws would cause an estimated 1·6 million disability-adjusted life years from 2015-2050.” (barton2024theeffectof pages 1-3)

### 9.2 Population demographics
- Children are the principal affected population; endemic foci are in tropical areas, including West Africa and the South Pacific. (beiras2024knowledgeattitudesand pages 1-2)

---

## 10. Diagnostics

### 10.1 Standard diagnostic approach (current practice in retrieved sources)
- Clinical suspicion plus serologic confirmation is repeatedly emphasized; treponemal tests (e.g., TPHA/TPPA) can remain reactive long-term, and non-treponemal tests (RPR/VDRL) are needed for activity assessment and confirmation in algorithms. (irawan2024comparisonofthe pages 1-2)

### 10.2 Point-of-care testing and diagnostic accuracy (2024)
**Standard Q Syphilis Ab RDT in children with suspected yaws (Indonesia; 2024):**
- Study population: 195 children aged 2–15 years; 116 clinically suspected, 13 serologically positive. (irawan2024comparisonofthe pages 1-2)
- Performance: vs TPHA sensitivity 93.3% and specificity 99.4%; vs RPR sensitivity 100% and specificity 98.4%. (irawan2024comparisonofthe pages 1-2)
- Abstract conclusion: “Standard Q Syphilis Ab RDT examination can be used as a screening test… RPR is still required to confirm the diagnosis of yaws.” (Irawan et al., doi:10.3855/jidc.17753; accepted 2023-11-29; published 2024-11 issue) (irawan2024comparisonofthe pages 1-2)

### 10.3 Molecular diagnostics and differential diagnosis (2024)
The Ghana study shows that multiplex PCR can identify alternative etiologies in yaws-like ulcers (notably *H. ducreyi* and HSV), a major practical issue for elimination programs relying on clinical case finding. (boaitey2024prevalenceofyaws pages 1-2)

### 10.4 Differential diagnosis (examples supported in retrieved sources)
- *H. ducreyi* and HSV are demonstrated causes of clinically similar lesions (quantified in Ghana). (boaitey2024prevalenceofyaws pages 1-2)
- In KAP study excerpt, respondents and health workers referenced other conditions confused with yaws (e.g., Buruli ulcer, *H. ducreyi*). (beiras2024knowledgeattitudesand pages 8-9)

### 10.5 Genetics/omics-based diagnostics
No host genetic testing is indicated; pathogen sequencing and MLST/WGS are the main “omics” tools described. (medappa2024lowgeneticdiversitya pages 1-2, barton2024theeffectof pages 1-3)

---

## 11. Outcome / Prognosis

- Untreated infection can progress to late destructive bone/cartilage disease (tertiary), occurring in ~10% within 5–10 years (as described in a clinical staging source). (irawan2024comparisonofthe pages 1-2)
- Programmatically, re-emergence after MDA is documented, driven largely by local transmission and multiple pre-existing sub-lineages, implying that prognosis at the population level depends strongly on coverage and surveillance quality. (barton2024theeffectof pages 1-3)

The retrieved evidence set does not provide modern case-fatality rates; yaws is principally morbidity-causing rather than acutely fatal in the texts retrieved. (barton2024theeffectof pages 1-3)

---

## 12. Treatment

### 12.1 First-line pharmacotherapy
- **Azithromycin (single-dose oral)**: described as preferred therapy in West Africa KAP study and forms the basis of current eradication strategy implementation. (beiras2024knowledgeattitudesand pages 1-2)
- **Benzathine penicillin G (BPG) intramuscular injection**: historical cornerstone of the 1950s–1960s campaign and remains important, including as targeted treatment in some strategies and as a comparator in evidence discussions. (barton2024theeffectof pages 1-3)

### 12.2 Treatment strategy and implementation (real-world)
**Morges strategy / TCT and coverage targets:**
- The KAP study notes that a “cornerstone” is achieving “population treatment coverage of over 90%.” (beiras2024knowledgeattitudesand pages 1-2)

**Large-scale Congo-Basin TCT implementation (2024 preprint):**
- Target population 1,530,014 across 17 districts; first-round coverage 95.21% overall; second-round Cameroon coverage 95.73%; active yaws prevalence decreased from 6.5% to 0.4% overall. (tabah2024themorgesstrategy pages 1-5)
- Abstract support: “A novel TCT model was successfully implemented at largescale… The prevalence of active yaws dropped remarkably… however complete interruption of yaws transmission was not achieved.” (Tabah et al., 2024-11; https://doi.org/10.1101/2024.11.07.24316738) (tabah2024themorgesstrategy pages 1-5)

**Repeated MDA vs targeted treatment (PNG; 2024 genomic epidemiology preprint):**
- In a 56,676-person cluster randomized trial context, active cases reduced three-fold in control arm vs 11-fold in experimental arm at 18 months (summary in text). (barton2024theeffectof pages 1-3)
- Tradeoff: repeated MDA increased selection pressure and was associated with emergence/spread of azithromycin resistance in 3 children. (barton2024theeffectof pages 1-3)

### 12.3 MAXO term suggestions (treatment actions)
- Oral antibiotic therapy (azithromycin): MAXO:0000756 (antibiotic therapy; suggested)
- Intramuscular injection therapy (benzathine penicillin): MAXO:0000758 (parenteral drug therapy; suggested)
- Mass drug administration / community treatment campaign: MAXO term not confirmed in retrieved sources; treat as programmatic intervention.

(These are mapping suggestions; MAXO IDs were not present in the retrieved texts.) (tabah2024themorgesstrategy pages 1-5)

---

## 13. Prevention

### 13.1 Primary/secondary prevention in practice
Evidence emphasizes **population-level chemoprevention/interrupting transmission** via TCT/MDA with high coverage, followed by surveillance and targeted treatment.
- In Congo-Basin implementation, TCT was followed by “post-campaign active surveillance, treatment of yaws cases and their contacts.” (tabah2024themorgesstrategy pages 1-5)

### 13.2 Public-health/behavioral prevention barriers
KAP study data show persistent misconceptions about transmission (e.g., low correct identification of person-to-person transmission), supporting the need for culturally tailored education.
- Only 11.9% (Ghana) and 20.7% (Côte d’Ivoire) correctly identified contact with an infected person as a mode of transmission; 42.6% in Cameroon. (beiras2024knowledgeattitudesand pages 1-2)

---

## 14. Other Species / Natural Disease

### 14.1 Nonhuman primates as reservoirs (key recent development)
A 2023 PLOS Neglected Tropical Diseases genomic study directly addresses the long-standing “no animal reservoir” assumption:
- Abstract conclusion: “Our data show that NHPs are infected with strains that are not only similar to the strains infecting humans but are genomically indistinguishable from them.” (Janečková et al., published 2023-09-13; https://doi.org/10.1371/journal.pntd.0011602) (janeckova2023thegenomesof pages 1-2)
- The study sequenced/finished genomes from 10 NHP-origin isolates and found “no consistent differences between human and NHP TPE genomes,” recommending continued surveillance in areas with naturally infected NHPs even if yaws is eliminated in humans. (janeckova2023thegenomesof pages 1-2, janeckova2023thegenomesof pages 9-10)

This constitutes a major contemporary complication for eradication: elimination in humans may not equal biological eradication if an untreated wildlife reservoir persists. (janeckova2023thegenomesof pages 1-2)

---

## 15. Model Organisms
No dedicated experimental model organism systems were described in the retrieved texts for this run beyond naturally infected nonhuman primates being recognized as hosts/reservoirs and genomic comparators. (janeckova2023thegenomesof pages 1-2)

---

## Expert synthesis and analysis (cross-source)
1) **Implementation effectiveness is high but elimination is fragile.** Large-scale TCT can reach WHO-recommended coverage thresholds (>90%) and drive large prevalence reductions (e.g., 6.5%→0.4% active yaws), but may still fail to fully interrupt transmission, supporting recommendations for multiple rounds and sustained surveillance. (tabah2024themorgesstrategy pages 1-5)

2) **Repeated MDA improves suppression but increases resistance risk.** Genomic epidemiology indicates greater suppression (11-fold vs 3-fold reduction in active cases at 18 months in one trial context) but also documents emergence/spread of macrolide resistance (23S rRNA A2058G/A2059G) in a small number of children, highlighting the need for resistance surveillance integrated into programs. (barton2024theeffectof pages 1-3)

3) **Diagnostics must explicitly address ulcer syndrome heterogeneity.** The Ghana PCR study demonstrates that yaws-like ulcers frequently have non-treponemal etiologies (*H. ducreyi*, HSV), meaning that reliance on clinical diagnosis alone can overestimate yaws and misdirect treatment (especially for HSV, which does not respond to antibiotics). (boaitey2024prevalenceofyaws pages 1-2)

4) **The reservoir question is no longer hypothetical.** Finished genomes provide strong evidence that NHP strains are genomically indistinguishable from human strains, which supports a potential animal reservoir and implies that “eradication” verification must incorporate ecological surveillance in relevant geographies. (janeckova2023thegenomesof pages 1-2, janeckova2023thegenomesof pages 9-10)

---

## Limitations of this report (evidence availability)
- Formal disease ontology identifiers (MONDO, MeSH, ICD-10/11, Orphanet) were not present in the retrieved full-text sources during this tool run; therefore, they are not provided to avoid uncited assertions. (boaitey2024prevalenceofyaws pages 1-2)
- Some highly relevant recent diagnostics (e.g., multi-country LAMP evaluation) were identified by search metadata but were unobtainable in this run, so performance characteristics beyond the Standard Q RDT and Ghana multiplex PCR results are not summarized here. (irawan2024comparisonofthe pages 1-2, boaitey2024prevalenceofyaws pages 15-16)


References

1. (barton2024theeffectof pages 1-3): Amber Barton, Petra Pospíšilová, Camila G Beiras, Lucy N. John, Wendy Houinei, Lorenzo Giacani, David Šmajs, Michael Marks, Oriol Mitjà, Mathew A Beale, and Nicholas R Thomson. The effect of repeated mass drug administration on the transmission of yaws: a genomic epidemiology study. MedRxiv, Oct 2024. URL: https://doi.org/10.1101/2024.10.27.24316187, doi:10.1101/2024.10.27.24316187. This article has 0 citations.

2. (beiras2024knowledgeattitudesand pages 1-2): Camila González Beiras, Adingra Tano Kouadio, Becca Louise Handley, Daniel Arhinful, Serges Tchatchouang, Ahouansou Stanislas Sonagnon Houndji, Eric Tettey Nartey, Dolphine Osei Sarpong, Gely Menguena, Philippe Ndzomo, Laud Anthony Basing, Kouadio Aboh Hugues, Ivy Brago Amanor, Mohammed Bakheit, Emelie Landmann, Patrick Awondo, Claudia Müller, Tania Crucitti, Nadine Borst, Lisa Becherer, Simone Lüert, Sieghard Frischmann, Aboubacar Sylla, Mireille S. Kouamé-Sina, Emma Michèle Harding-Esch, Sascha Knauf, Oriol Mitjà, Sara Eyangoh, Kennedy Kwasi Addo, Solange Ngazoa Kakou, and Michael Marks. Knowledge, attitudes and practices towards yaws in endemic areas of ghana, cameroon and côte d’ivoire. PLOS Neglected Tropical Diseases, 18:e0012224, Jun 2024. URL: https://doi.org/10.1371/journal.pntd.0012224, doi:10.1371/journal.pntd.0012224. This article has 1 citations and is from a domain leading peer-reviewed journal.

3. (tabah2024themorgesstrategy pages 1-5): Earnest Njih Tabah, Alphonse Um Boock, Chefor Alain Djam, Gilius Axel Aloumba, Boua Bernard, Nzoyem Colin Tsago, Irine Ngani Nformi, Loic Douanla Pagning, Elisaberth Baran-A-Bidias, Christian Elvis Kouayep-Watat, Smith Afanji, Ebai George, Marielle Patty Ngassa, Bonaventure Savadogo, Serges Tchatchouang, Valerie Donkeng, Yves Thierry Barogui, Sara Eyangoh, and Kingsley Bampoe Asiedu. The morges strategy for yaws eradication: the first largescale total community treatment with azithromycin against yaws in the congo-basin, using a novel model. MedRxiv, Nov 2024. URL: https://doi.org/10.1101/2024.11.07.24316738, doi:10.1101/2024.11.07.24316738. This article has 1 citations.

4. (medappa2024lowgeneticdiversitya pages 1-2): M Medappa, P Pospíšilová, and MPM Madruga. Low genetic diversity of treponema pallidum ssp. pertenue (tpe) isolated from patients' ulcers in namatanai district of papua new guinea: local human population …. Unknown journal, 2024.

5. (janeckova2023thegenomesof pages 1-2): Klára Janečková, Christian Roos, Pavla Fedrová, Nikola Tom, Darina Čejková, Simone Lueert, Julius D. Keyyu, Idrissa S. Chuma, Sascha Knauf, and David Šmajs. The genomes of the yaws bacterium, treponema pallidum subsp. pertenue, of nonhuman primate and human origin are not genomically distinct. PLOS Neglected Tropical Diseases, 17:e0011602, Sep 2023. URL: https://doi.org/10.1371/journal.pntd.0011602, doi:10.1371/journal.pntd.0011602. This article has 15 citations and is from a domain leading peer-reviewed journal.

6. (vicar2025yawsinafrica pages 1-2): Ezekiel K. Vicar, Shirley V. Simpson, Gloria I. Mensah, Kennedy K. Addo, and Eric S. Donkor. Yaws in africa: past, present and future. Diseases, 13:14, Jan 2025. URL: https://doi.org/10.3390/diseases13010014, doi:10.3390/diseases13010014. This article has 2 citations.

7. (vicar2025yawsinafrica pages 2-4): Ezekiel K. Vicar, Shirley V. Simpson, Gloria I. Mensah, Kennedy K. Addo, and Eric S. Donkor. Yaws in africa: past, present and future. Diseases, 13:14, Jan 2025. URL: https://doi.org/10.3390/diseases13010014, doi:10.3390/diseases13010014. This article has 2 citations.

8. (irawan2024comparisonofthe pages 1-2): Yudo Irawan, Astuti Giantini, and Nevi Yasnova. Comparison of the standard q syphilis antibody rapid diagnostic test to gold standards for yaws detection in children. Journal of infection in developing countries, 18 11:1734-1738, Nov 2024. URL: https://doi.org/10.3855/jidc.17753, doi:10.3855/jidc.17753. This article has 1 citations.

9. (vicar2025yawsinafrica pages 7-8): Ezekiel K. Vicar, Shirley V. Simpson, Gloria I. Mensah, Kennedy K. Addo, and Eric S. Donkor. Yaws in africa: past, present and future. Diseases, 13:14, Jan 2025. URL: https://doi.org/10.3390/diseases13010014, doi:10.3390/diseases13010014. This article has 2 citations.

10. (boaitey2024prevalenceofyaws pages 7-8): Yaw Agyekum Boaitey, Alex Owusu-Ofori, Amarachukwu Anyogu, Farhang Aghakhanian, Natasha Arora, Jonathan B. Parr, Philipp P. Bosshard, Saki Raheem, and Pascale Gerbault. Prevalence of yaws and syphilis in the ashanti region of ghana and occurrence of h. ducreyi, herpes simplex virus 1 and herpes simplex virus 2 in skin lesions associated with treponematoses. PLOS ONE, 19:e0295088, May 2024. URL: https://doi.org/10.1371/journal.pone.0295088, doi:10.1371/journal.pone.0295088. This article has 7 citations and is from a peer-reviewed journal.

11. (boaitey2024prevalenceofyaws pages 2-4): Yaw Agyekum Boaitey, Alex Owusu-Ofori, Amarachukwu Anyogu, Farhang Aghakhanian, Natasha Arora, Jonathan B. Parr, Philipp P. Bosshard, Saki Raheem, and Pascale Gerbault. Prevalence of yaws and syphilis in the ashanti region of ghana and occurrence of h. ducreyi, herpes simplex virus 1 and herpes simplex virus 2 in skin lesions associated with treponematoses. PLOS ONE, 19:e0295088, May 2024. URL: https://doi.org/10.1371/journal.pone.0295088, doi:10.1371/journal.pone.0295088. This article has 7 citations and is from a peer-reviewed journal.

12. (boaitey2024prevalenceofyaws pages 1-2): Yaw Agyekum Boaitey, Alex Owusu-Ofori, Amarachukwu Anyogu, Farhang Aghakhanian, Natasha Arora, Jonathan B. Parr, Philipp P. Bosshard, Saki Raheem, and Pascale Gerbault. Prevalence of yaws and syphilis in the ashanti region of ghana and occurrence of h. ducreyi, herpes simplex virus 1 and herpes simplex virus 2 in skin lesions associated with treponematoses. PLOS ONE, 19:e0295088, May 2024. URL: https://doi.org/10.1371/journal.pone.0295088, doi:10.1371/journal.pone.0295088. This article has 7 citations and is from a peer-reviewed journal.

13. (boaitey2024prevalenceofyaws pages 10-11): Yaw Agyekum Boaitey, Alex Owusu-Ofori, Amarachukwu Anyogu, Farhang Aghakhanian, Natasha Arora, Jonathan B. Parr, Philipp P. Bosshard, Saki Raheem, and Pascale Gerbault. Prevalence of yaws and syphilis in the ashanti region of ghana and occurrence of h. ducreyi, herpes simplex virus 1 and herpes simplex virus 2 in skin lesions associated with treponematoses. PLOS ONE, 19:e0295088, May 2024. URL: https://doi.org/10.1371/journal.pone.0295088, doi:10.1371/journal.pone.0295088. This article has 7 citations and is from a peer-reviewed journal.

14. (barton2024theeffectof pages 12-14): Amber Barton, Petra Pospíšilová, Camila G Beiras, Lucy N. John, Wendy Houinei, Lorenzo Giacani, David Šmajs, Michael Marks, Oriol Mitjà, Mathew A Beale, and Nicholas R Thomson. The effect of repeated mass drug administration on the transmission of yaws: a genomic epidemiology study. MedRxiv, Oct 2024. URL: https://doi.org/10.1101/2024.10.27.24316187, doi:10.1101/2024.10.27.24316187. This article has 0 citations.

15. (vicar2025yawsinafrica pages 11-11): Ezekiel K. Vicar, Shirley V. Simpson, Gloria I. Mensah, Kennedy K. Addo, and Eric S. Donkor. Yaws in africa: past, present and future. Diseases, 13:14, Jan 2025. URL: https://doi.org/10.3390/diseases13010014, doi:10.3390/diseases13010014. This article has 2 citations.

16. (janeckova2023thegenomesof pages 9-10): Klára Janečková, Christian Roos, Pavla Fedrová, Nikola Tom, Darina Čejková, Simone Lueert, Julius D. Keyyu, Idrissa S. Chuma, Sascha Knauf, and David Šmajs. The genomes of the yaws bacterium, treponema pallidum subsp. pertenue, of nonhuman primate and human origin are not genomically distinct. PLOS Neglected Tropical Diseases, 17:e0011602, Sep 2023. URL: https://doi.org/10.1371/journal.pntd.0011602, doi:10.1371/journal.pntd.0011602. This article has 15 citations and is from a domain leading peer-reviewed journal.

17. (beiras2024knowledgeattitudesand pages 8-9): Camila González Beiras, Adingra Tano Kouadio, Becca Louise Handley, Daniel Arhinful, Serges Tchatchouang, Ahouansou Stanislas Sonagnon Houndji, Eric Tettey Nartey, Dolphine Osei Sarpong, Gely Menguena, Philippe Ndzomo, Laud Anthony Basing, Kouadio Aboh Hugues, Ivy Brago Amanor, Mohammed Bakheit, Emelie Landmann, Patrick Awondo, Claudia Müller, Tania Crucitti, Nadine Borst, Lisa Becherer, Simone Lüert, Sieghard Frischmann, Aboubacar Sylla, Mireille S. Kouamé-Sina, Emma Michèle Harding-Esch, Sascha Knauf, Oriol Mitjà, Sara Eyangoh, Kennedy Kwasi Addo, Solange Ngazoa Kakou, and Michael Marks. Knowledge, attitudes and practices towards yaws in endemic areas of ghana, cameroon and côte d’ivoire. PLOS Neglected Tropical Diseases, 18:e0012224, Jun 2024. URL: https://doi.org/10.1371/journal.pntd.0012224, doi:10.1371/journal.pntd.0012224. This article has 1 citations and is from a domain leading peer-reviewed journal.

18. (boaitey2024prevalenceofyaws pages 15-16): Yaw Agyekum Boaitey, Alex Owusu-Ofori, Amarachukwu Anyogu, Farhang Aghakhanian, Natasha Arora, Jonathan B. Parr, Philipp P. Bosshard, Saki Raheem, and Pascale Gerbault. Prevalence of yaws and syphilis in the ashanti region of ghana and occurrence of h. ducreyi, herpes simplex virus 1 and herpes simplex virus 2 in skin lesions associated with treponematoses. PLOS ONE, 19:e0295088, May 2024. URL: https://doi.org/10.1371/journal.pone.0295088, doi:10.1371/journal.pone.0295088. This article has 7 citations and is from a peer-reviewed journal.
