---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T13:57:36.604652'
end_time: '2026-04-04T14:02:49.141406'
duration_seconds: 312.54
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Foodborne trematodiases
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 26
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Foodborne trematodiases
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Foodborne trematodiases** covering all of the
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
- **Disease Name:** Foodborne trematodiases
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Foodborne trematodiases** covering all of the
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


# Comprehensive Research Report: Foodborne trematodiases (FBTs)

## Target disease
- **Disease name:** Foodborne trematodiases (FBTs) (liu2024globalregionaland pages 1-2, tidman2023globalprevalenceof pages 1-2)
- **Category:** Infectious disease (parasitic helminth infections; trematodes/flukes) (liu2024globalregionaland pages 1-2, tidman2023globalprevalenceof pages 1-2)
- **MONDO ID:** Not identified in the retrieved evidence (not all ontologies/IDs are consistently indexed in primary literature).

## Executive overview (current understanding)
Food-borne trematodiases are a grouped set of zoonotic trematode infections acquired by ingesting infective larval stages (metacercariae) in contaminated foods—principally freshwater fish (liver flukes), crustaceans (lung flukes), and aquatic plants/water (fascioliasis; and typically fasciolopsiasis) (liu2024globalregionaland pages 1-2, tidman2023globalprevalenceof pages 1-2, ortiz2024foodbornehelminthiasis pages 1-2). They are recognized by WHO as neglected tropical diseases (NTDs) and are a continuing public-health burden particularly in WHO Western Pacific and South‑East Asia regions (liu2024globalregionaland pages 1-2, tidman2023globalprevalenceof pages 1-2).

A 2024 GBD 2021-based analysis estimated **44,466,329 prevalent cases** (95% UI 40,017,217–50,034,921) and **998,028 DALYs** (95% UI 569,766–1,638,112) of food-borne trematodiases in 2021 (across 17 countries), with highest age-standardized prevalence and DALY rates in the Western Pacific region (liu2024globalregionaland pages 1-2). Major liver flukes (*Opisthorchis viverrini* and *Clonorchis sinensis*) are classified as carcinogenic to humans (IARC Group 1) and are linked to cholangiocarcinoma (CCA) risk (liu2024globalregionaland pages 1-2, qian2024clonorchiasisandopisthorchiasis pages 1-2).

## Summary table (high-yield)
| Scope / disease | Major causative trematodes | Key transmission / food vehicle | Main organ tropism / major complications | Diagnostics and treatment (2023–2025 literature) | Key quantitative burden / prevalence statistics |
|---|---|---|---|---|---|
| **Food-borne trematodiases (FBTs), overall** | Cluster including **clonorchiasis, opisthorchiasis, fascioliasis, fasciolopsiasis, paragonimiasis**; transmission via ingestion of larval stages in contaminated **fish, crustaceans, or aquatic plants**. WHO lists FBTs among neglected tropical diseases; major human pathology involves hepatobiliary, pulmonary, and intestinal systems. *At least 99 trematode species can infect humans* in broader human trematodiasis context (15 liver, 9 lung, 75 intestinal) (liu2024globalregionaland pages 1-2, tidman2023globalprevalenceof pages 1-2) | Raw/undercooked **freshwater fish** (clonorchiasis/opisthorchiasis), **crustaceans** (paragonimiasis), **aquatic plants/water** (fascioliasis), aquatic plants for fasciolopsiasis by lifecycle logic (liu2024globalregionaland pages 1-2, tidman2023globalprevalenceof pages 1-2, ortiz2024foodbornehelminthiasis pages 1-2) | Liver/bile ducts, lungs/pleura, intestines; severe outcomes include **fibrosis, biliary disease, cholangiocarcinoma**, chronic lung disease, and intestinal morbidity (liu2024globalregionaland pages 1-2, tidman2023globalprevalenceof pages 1-2, ortiz2024foodbornehelminthiasis pages 1-2) | Diagnostics across FBTs remain dominated by **faecal parasitology/stool microscopy**; sensitivity often limited. Species-specific serology, copro/urine antigen tests, and molecular assays are emerging. Main drugs: **praziquantel** for clonorchiasis/opisthorchiasis/paragonimiasis and **triclabendazole** for fascioliasis (tidman2023globalprevalenceof pages 1-2, tidman2023globalprevalenceof pages 9-10, qian2024clonorchiasisandopisthorchiasis pages 1-2) | **GBD 2021 / 2024 analysis:** **44,466,329 cases** and **998,028 DALYs** in 2021 across 17 countries; highest burden in Western Pacific; burden higher in males and peaks at 50–59 years; projected ASDR largely stable to 2030 (liu2024globalregionaland pages 1-2). **2024 review:** ~**75 million infected**, **750 million at risk** (ortiz2024foodbornehelminthiasis pages 1-2). **2023 scoping review:** 93/224 countries reported ≥1 FBT; 26 likely co-endemic for ≥2 FBTs (tidman2023globalprevalenceof pages 1-2) |
| **Clonorchiasis** | *Clonorchis sinensis* (qian2024clonorchiasisandopisthorchiasis pages 1-2, qian2024clonorchiasisandopisthorchiasis pages 2-4) | Consumption of **raw/undercooked freshwater fish** containing metacercariae (qian2024clonorchiasisandopisthorchiasis pages 1-2, qian2024clonorchiasisandopisthorchiasis pages 2-4) | **Intrahepatic bile ducts / hepatobiliary system**; chronic infection linked to **cholangitis, cholelithiasis, periductal fibrosis, and cholangiocarcinoma**; *C. sinensis* is a Group 1 carcinogen for human CCA (liu2024globalregionaland pages 1-2, qian2024clonorchiasisandopisthorchiasis pages 1-2) | **Stool microscopy** widely used; immunologic assays for screening; molecular methods for species differentiation. **Praziquantel** is mainstay; **tribendimidine** is a candidate alternative under development (qian2024clonorchiasisandopisthorchiasis pages 1-2, qian2024clonorchiasisandopisthorchiasis pages 2-4) | 2024 review estimated ~**13.24 million** *C. sinensis* infections, including ~**10.82 million in China** (2015 estimate cited in review) (qian2024clonorchiasisandopisthorchiasis pages 2-4). 2023 scoping review found study prevalence up to **59.6%** in Asia (tidman2023globalprevalenceof pages 1-2) |
| **Opisthorchiasis** | *Opisthorchis viverrini*, *O. felineus* (qian2024clonorchiasisandopisthorchiasis pages 1-2, qian2024clonorchiasisandopisthorchiasis pages 2-4) | Consumption of **raw/undercooked cyprinid freshwater fish** with metacercariae; culturally embedded fish dishes are major risk factor (qian2024clonorchiasisandopisthorchiasis pages 1-2, liau2023opisthorchisviverrini—currentunderstanding pages 6-7) | **Bile ducts / hepatobiliary tract**; complications include **cholangitis, cholecystitis, cholelithiasis, advanced periductal fibrosis, cholangiocarcinoma** (qian2024clonorchiasisandopisthorchiasis pages 1-2, liau2023opisthorchisviverrini—currentunderstanding pages 6-7) | Conventional gold standard remains **stool microscopy/FECT**. Newer diagnostics include **urine antigen ELISA**, gold-nanoparticle ELISA, smartphone fluorescent assay, immunochromatographic kits, and PCR assays (kopolrat2025largescaleepidemiologyof pages 1-2, kopolrat2025largescaleepidemiologyof pages 12-14, liau2023opisthorchisviverrini—currentunderstanding pages 6-7, kopolrat2025largescaleepidemiologyof pages 8-12). **Praziquantel** remains standard therapy (qian2024clonorchiasisandopisthorchiasis pages 1-2) | **2023 scoping review:** study prevalence range **0.66%–88.7%** in Asia (tidman2023globalprevalenceof pages 1-2). **Greater Mekong meta-analysis 2024:** pooled *O. viverrini* prevalence **21.11%** overall; **34.06%** in Laos, **18.19%** Thailand, **10.48%** Cambodia (qian2024clonorchiasisandopisthorchiasis pages 2-4). **Thailand 2025 survey:** urine ELISA prevalence **50.3%** vs stool FECT **12.2%**; urine ELISA sensitivity **91.6%** vs FECT **21.9%** against composite reference (kopolrat2025largescaleepidemiologyof pages 1-2, kopolrat2025largescaleepidemiologyof pages 12-14, kopolrat2025largescaleepidemiologyof pages 8-12). **One Health Thailand 2025:** human prevalence fell **14.1% → 0.9%**, reinfection **17.4% → 9.7%**, fish metacercariae **21.9% → 2.2%**, dogs/cats **21.3% → 3.8%**, raw fish consumption **52.4% → 12.3%**, toilet use **31.7% → 87.1%** (prakobwong2025onehealthintegrated pages 1-2) |
| **Fascioliasis** | *Fasciola hepatica*, *F. gigantica* (tidman2023globalprevalenceof pages 1-2, ortiz2024foodbornehelminthiasis pages 1-2) | Ingestion of contaminated **aquatic plants** and/or contaminated **water**; linked to poor sanitation and livestock-associated contamination (tidman2023globalprevalenceof pages 1-2, tidman2023globalprevalenceof pages 9-10) | **Liver and biliary tree**; acute migratory phase causes fever, abdominal pain/discomfort, nausea, diarrhoea, urticaria, cough; chronic disease causes **bile duct/gallbladder/liver inflammation, fibrosis, cholangitis, biliary obstruction**; ectopic CNS/ocular disease can occur (tidman2023globalprevalenceof pages 1-2, ortiz2024foodbornehelminthiasis pages 1-2, tidman2023globalprevalenceof pages 9-10) | Diagnostics: stool/coprological tests are common but have **low sensitivity** in acute or low-burden infection; serology is more sensitive but cannot reliably distinguish past vs active infection; combined parasitology + serology improves performance; coproantigen and PCR are newer options (tidman2023globalprevalenceof pages 9-10). Treatment: **triclabendazole** most reported, commonly **10 mg/kg single dose** or **10 mg/kg/day for 2 days**; **nitazoxanide** reported as alternative where needed (tidman2023globalprevalenceof pages 9-10) | **2023 global meta-analysis:** pooled prevalence **4.5%** overall; **9.0%** South America, **4.8%** Africa, **2.0%** Asia; highest country estimates **Bolivia 21%**, **Peru 11%**, **Egypt 6%** (tidman2023globalprevalenceof pages 1-2, tidman2023globalprevalenceof pages 9-10). **2023 scoping review:** highest reported study prevalence **24.77%** in the Americas (tidman2023globalprevalenceof pages 1-2) |
| **Fasciolopsiasis** | *Fasciolopsis buski* is part of FBT scope in GBD-based 2024 analysis, though recent 2023–2025 evidence in retrieved set was sparse (liu2024globalregionaland pages 1-2) | Typically food-borne via **aquatic plants** carrying metacercariae; recent retrieved evidence set provides limited disease-specific 2023–2025 detail (liu2024globalregionaland pages 1-2) | **Intestinal** tropism; recent retrieved evidence set contains limited disease-specific complication detail compared with liver and lung flukes (liu2024globalregionaland pages 1-2) | No robust disease-specific 2023–2025 diagnostic/treatment advances were captured in the retrieved evidence set; likely still reliant on stool parasitology and praziquantel in practice, but this was **not directly documented** in the available context IDs (liu2024globalregionaland pages 1-2) | Included in 2024 global FBT burden framework, but **specific 2023–2025 prevalence estimates were not available** in the retrieved context IDs (liu2024globalregionaland pages 1-2) |
| **Paragonimiasis** | *Paragonimus* spp. (including *P. westermani* in many Asian settings) (tidman2023globalprevalenceof pages 1-2, tenorio2021monstersinour pages 2-4) | Consumption of **raw/undercooked crab or other crustaceans** containing metacercariae (tidman2023globalprevalenceof pages 1-2, tidman2023globalprevalenceof pages 9-10, tenorio2021monstersinour pages 2-4) | **Lungs and pleura**; causes **chronic cough, hemoptysis/bloody sputum, chest pain, dyspnoea**, pleuritis/pneumonia/bronchitis; can be ectopic including **cerebral** disease and is often misdiagnosed as tuberculosis (tidman2023globalprevalenceof pages 1-2, tenorio2021monstersinour pages 2-4) | Diagnostics include **sputum and/or fecal egg examination**, serology, and intradermal testing; serology can be more sensitive due to intermittent egg shedding (tidman2023globalprevalenceof pages 9-10). **Praziquantel** is the main reported treatment (tidman2023globalprevalenceof pages 1-2) | **2023 scoping review:** least available data among WHO-targeted FBTs; highest reported study prevalence **14.9%** in Africa (tidman2023globalprevalenceof pages 1-2). Older burden summarized in 2024 foodborne helminth review notes ongoing underestimation due to poor diagnostics/surveillance (ortiz2024foodbornehelminthiasis pages 1-2) |


*Table: This table condenses the scope, causative parasites, transmission routes, organ tropism, diagnostics, treatment, and recent quantitative burden data for food-borne trematodiases. It highlights both global burden estimates and concrete implementation findings from recent Thailand diagnostic and One Health control studies.*

---

## 1. Disease information
### What is the disease?
FBTs are a **cluster of trematode infections** “mainly encompassing clonorchiasis, fascioliasis, fasciolopsiasis, opisthorchiasis, and paragonimiasis” (GBD-based framing) (liu2024globalregionaland pages 1-2). WHO’s NTD control framing emphasizes four key genera for control: **Fasciola spp., Paragonimus spp., Clonorchis spp., Opisthorchis spp.** (tidman2023globalprevalenceof pages 1-2).

### Common synonyms / alternative names
- **Food-borne trematodiases** / **foodborne trematodiases** (liu2024globalregionaland pages 1-2, tidman2023globalprevalenceof pages 1-2)
- Often discussed as **foodborne trematode infections** or grouped under **foodborne helminthiases** in broader reviews (ortiz2024foodbornehelminthiasis pages 1-2).

### Key identifiers (ICD/MeSH/OMIM/Orphanet/MONDO)
The retrieved primary/review literature did not provide explicit ICD-10/ICD-11/MeSH/MONDO mappings for the group entity “foodborne trematodiases.” Therefore, these identifiers cannot be reliably asserted from the current evidence set.

### Evidence source type
The characterization above is derived from aggregated disease-level sources: GBD analyses (population modeling) and systematic/scoping reviews (liu2024globalregionaland pages 1-2, tidman2023globalprevalenceof pages 1-2, ortiz2024foodbornehelminthiasis pages 1-2), plus large field epidemiology and implementation studies (kopolrat2025largescaleepidemiologyof pages 1-2, prakobwong2025onehealthintegrated pages 1-2).

---

## 2. Etiology
### Disease causal factors
- **Infectious cause:** Digenetic trematodes (flukes) infecting humans via complex lifecycles involving **snails as first intermediate hosts** and, for most targeted FBTs, **second intermediate hosts** (freshwater fish for *Clonorchis/Opisthorchis*; crustaceans for *Paragonimus*) (tidman2023globalprevalenceof pages 1-2, qian2024clonorchiasisandopisthorchiasis pages 1-2).
- **Food-borne exposure:** Infection occurs through consuming contaminated food containing larval stages (metacercariae), notably raw/undercooked fish or crab, or contaminated aquatic vegetation/water (tidman2023globalprevalenceof pages 1-2, ortiz2024foodbornehelminthiasis pages 1-2, qian2024clonorchiasisandopisthorchiasis pages 1-2).

### Risk factors (human)
Cross-cutting risk factors identified in a 2023 WHO-focused scoping review include:
- Proximity to rural/agricultural environments
- Consumption of raw contaminated food
- Limited water, hygiene and sanitation (WASH) (tidman2023globalprevalenceof pages 1-2)

In Thailand, a 2025 large-scale survey found individual-level infection risk correlated with demographic and behavioral factors (e.g., raw fish consumption was among predictive factors analyzed) (kopolrat2025largescaleepidemiologyof pages 1-2, kopolrat2025largescaleepidemiologyof pages 8-12).

### Protective factors
Reported protective interventions were primarily programmatic rather than individual genetic:
- Health education and awareness programs and preventive interventions that reduce raw-fish consumption and improve sanitation were associated with reduced transmission at community level (tidman2023globalprevalenceof pages 1-2, prakobwong2025onehealthintegrated pages 1-2).

### Genetic risk/protective factors; gene–environment interactions
No host genetic susceptibility loci or gene–environment interaction studies were captured in the retrieved evidence set; thus, this section cannot be populated with well-cited gene-level claims.

---

## 3. Phenotypes (clinical manifestations)
FBTs present heterogeneously depending on species and organ tropism.

### Hepatobiliary (liver flukes: clonorchiasis/opisthorchiasis; fascioliasis)
- Chronic *Clonorchis/Opisthorchis* infection is associated with **liver and biliary complications**, “most importantly cholangiocarcinoma” (qian2024clonorchiasisandopisthorchiasis pages 1-2).
- Fascioliasis can cause a spectrum from asymptomatic to severe disease; acute/early infection can include “fever, abdominal discomfort, anorexia, nausea, diarrhoea, urticaria and coughing” (ortiz2024foodbornehelminthiasis pages 1-2).

**Suggested HPO terms (examples)**
- Abdominal pain (HP:0002027)
- Fever (HP:0001945)
- Nausea (HP:0002018)
- Diarrhea (HP:0002014)
- Eosinophilia (HP:0001880) (not directly quantified in provided evidence, but common in helminth infections; not asserted beyond evidence here)
- Cholangitis (HP:0005214)
- Cholangiocarcinoma (HP:0002891)

### Pulmonary/pleural (paragonimiasis)
A 2023 scoping review summarized typical manifestations: “chronic cough with bloody sputum, chest pain, dyspnoea” (tidman2023globalprevalenceof pages 1-2).

**Suggested HPO terms (examples)**
- Cough (HP:0012735)
- Hemoptysis (HP:0002105)
- Chest pain (HP:0100749)
- Dyspnea (HP:0002094)

### Intestinal (fasciolopsiasis and other intestinal flukes)
Fasciolopsiasis is included within the FBT grouping in GBD-based analyses (liu2024globalregionaland pages 1-2), but disease-specific phenotype frequencies were not captured in the retrieved evidence set.

### Quality of life impact
The evidence set did not include disease-specific EQ‑5D/SF‑36/PROMIS statistics for FBTs. Burden is instead reflected in DALYs at population level in GBD analyses (liu2024globalregionaland pages 1-2).

---

## 4. Genetic / molecular information
### Causal genes and variants
Not applicable in the standard Mendelian sense: FBTs are infections caused by parasites rather than inherited human genetic disorders.

### Molecular profiling / biomarkers (recent developments)
Recent literature emphasizes improved diagnostic biomarkers for *Opisthorchis viverrini* infection:
- A 2025 Thailand survey used **urine antigen detection by monoclonal antibody ELISA** for mass screening and showed markedly higher apparent prevalence than stool egg detection (kopolrat2025largescaleepidemiologyof pages 1-2, kopolrat2025largescaleepidemiologyof pages 8-12).
- A 2023 review reports multiple novel assay formats (gold nanoparticle ELISA; smartphone fluorescent assay; immunochromatographic kit) with reported sensitivity/specificity in endemic settings (liau2023opisthorchisviverrini—currentunderstanding pages 6-7).

**Epigenetics (cancer-associated, fluke-related)**
The retrieved evidence set includes cancer association at the level of “carcinogenic to humans” classification and CCA link (liu2024globalregionaland pages 1-2, qian2024clonorchiasisandopisthorchiasis pages 1-2), but did not provide specific epigenetic loci for FBTs themselves.

---

## 5. Environmental information
### Environmental/lifestyle contributors
Environmental and societal drivers include sanitation, rural/agricultural proximity, and cultural consumption of raw/undercooked fish/crustaceans (tidman2023globalprevalenceof pages 1-2, qian2024clonorchiasisandopisthorchiasis pages 1-2).

### Infectious agents
Key etiologic agents highlighted in recent authoritative reviews include:
- Liver flukes: *Clonorchis sinensis*, *Opisthorchis viverrini*, *Opisthorchis felineus* (qian2024clonorchiasisandopisthorchiasis pages 1-2)
- Lung flukes: *Paragonimus* spp. (tidman2023globalprevalenceof pages 1-2)
- Liver flukes (fascioliasis): *Fasciola* spp. (tidman2023globalprevalenceof pages 1-2, ortiz2024foodbornehelminthiasis pages 1-2)

---

## 6. Mechanism / pathophysiology (causal chains)
### General causal chain
1. Ingestion of metacercariae (food vehicle varies by parasite) (tidman2023globalprevalenceof pages 1-2, qian2024clonorchiasisandopisthorchiasis pages 1-2)
2. Migration to target organ (bile ducts for opisthorchiids; lungs/pleura for paragonimiasis; liver/biliary system for fascioliasis) (ortiz2024foodbornehelminthiasis pages 1-2, qian2024clonorchiasisandopisthorchiasis pages 1-2)
3. Chronic inflammation and tissue remodeling (e.g., fibrosis; biliary pathology) leading to long-term morbidity and, for carcinogenic liver flukes, increased risk of CCA (liu2024globalregionaland pages 1-2, qian2024clonorchiasisandopisthorchiasis pages 1-2)

### Carcinogenesis link (expert consensus in authoritative sources)
A 2024 Clinical Microbiology Reviews article states chronic liver fluke infections are associated with liver/biliary complications “most importantly cholangiocarcinoma” (qian2024clonorchiasisandopisthorchiasis pages 1-2). A 2024 GBD-based paper notes *O. viverrini* and *C. sinensis* are “classified as carcinogenic to humans (IARC Group 1)” (liu2024globalregionaland pages 1-2).

**Suggested GO biological processes (examples)**
- Inflammatory response (GO:0006954)
- Fibrosis / extracellular matrix organization (GO:0030198)
- Epithelial cell proliferation (GO:0050673)

**Suggested cell types (Cell Ontology; examples)**
- Cholangiocyte / biliary epithelial cell (CL:1000488)
- Hepatocyte (CL:0000182)
- Macrophage (CL:0000235)

---

## 7. Anatomical structures affected
### Organ level (primary)
- **Hepatobiliary system (bile ducts, liver):** clonorchiasis/opisthorchiasis; fascioliasis (ortiz2024foodbornehelminthiasis pages 1-2, qian2024clonorchiasisandopisthorchiasis pages 1-2)
- **Lungs/pleura:** paragonimiasis (tidman2023globalprevalenceof pages 1-2)

**Suggested UBERON terms (examples)**
- Liver (UBERON:0002107)
- Intrahepatic bile duct (UBERON:0003707)
- Lung (UBERON:0002048)

### Subcellular level
Not specified in the retrieved evidence set.

---

## 8. Temporal development (natural history)
- **Chronicity:** Liver fluke infections can persist long-term; the 2024 Clinical Microbiology Reviews paper highlights chronic infections and their association with long-term hepatobiliary outcomes (qian2024clonorchiasisandopisthorchiasis pages 1-2).
- **Age pattern:** GBD 2021 analysis shows burden is higher in males and peaks at ages **50–59** years (liu2024globalregionaland pages 1-2).

---

## 9. Inheritance and population
### Epidemiology and burden (recent quantitative statistics)
- **Global (GBD 2021; published 2024):** 44,466,329 prevalent cases and 998,028 DALYs in 2021; Western Pacific region had highest ASPR and ASDR; burden greater in males, peaking at 50–59 years; projected ASDR in 2030: **13.10 (males)** and **8.40 (females)** (liu2024globalregionaland pages 1-2).
- **Prevalence ranges in literature (WHO-targeted scoping review; 2023):** study prevalence ranges up to **88.7%** for opisthorchiasis (Asia), **59.6%** for clonorchiasis (Asia), **24.77%** for fascioliasis (Americas), **14.9%** for paragonimiasis (Africa) (tidman2023globalprevalenceof pages 1-2).

### Population distribution
FBTs are concentrated in endemic areas shaped by ecology and food practices; the 2024 GBD analysis highlights Western Pacific and South-East Asia prominence (liu2024globalregionaland pages 1-2), and the 2024 liver fluke review emphasizes eastern Asia/southeastern Asia/eastern Europe distribution by species (qian2024clonorchiasisandopisthorchiasis pages 1-2).

### Genetic inheritance
Not applicable (infectious etiology).

---

## 10. Diagnostics (current practice and recent developments)
### Core clinical tests
- **Stool microscopy / faecal parasitological testing:** remains widely used for FBTs, including liver flukes (qian2024clonorchiasisandopisthorchiasis pages 1-2) and in broader FBT surveys (tidman2023globalprevalenceof pages 1-2). However, for fascioliasis, coprological tests often have “low sensitivity” due to low egg burdens, intermittent shedding, or acute infection (tidman2023globalprevalenceof pages 9-10).

### Novel / improved diagnostics (real-world implementation)
**Urine antigen ELISA for *Opisthorchis viverrini* (large-scale field implementation)**
A 2025 Thai cross-sectional survey (n=20,322 enrolled; 19,465 urine; 18,929 feces) reported:
- Prevalence by **urine antigen ELISA: 50.3%** vs **stool FECT: 12.2%** (kopolrat2025largescaleepidemiologyof pages 1-2, kopolrat2025largescaleepidemiologyof pages 8-12)
- Sensitivity vs composite reference: **urine ELISA 91.6%** vs **FECT 21.9%** (kopolrat2025largescaleepidemiologyof pages 1-2, kopolrat2025largescaleepidemiologyof pages 12-14)
This provides strong evidence that stool-only surveys can underestimate low-intensity infection prevalence in endemic settings (kopolrat2025largescaleepidemiologyof pages 1-2, kopolrat2025largescaleepidemiologyof pages 8-12).

**Point-of-care/portable approaches (reviewed 2023)**
A 2023 review summarizes emerging assays including:
- Gold nanoparticle–enhanced ELISA (reported sensitivity 93.81%, specificity 91.34%)
- Smartphone-based fluorescent assay (reported sensitivity 84.88%, specificity 89.66%, accuracy 86.14%)
- Immunochromatographic kit evaluated on sera (reported sensitivity 100%, specificity 98.3%) (liau2023opisthorchisviverrini—currentunderstanding pages 6-7)

### Differential diagnosis
Not systematically addressed in the retrieved evidence set. A practical implication noted in FBT literature is diagnostic underperformance and misclassification when relying solely on microscopy (tidman2023globalprevalenceof pages 9-10, kopolrat2025largescaleepidemiologyof pages 1-2).

---

## 11. Outcome / prognosis
Robust survival and mortality estimates specific to FBT infections were not captured in the retrieved evidence set. In the 2024 GBD analysis, DALYs were emphasized while recorded deaths were limited, indicating that modeled burden was dominated by disability rather than mortality in available data streams (liu2024globalregionaland pages 1-2).

For carcinogenic liver fluke infections, the major long-term adverse outcome is increased risk of cholangiocarcinoma (qian2024clonorchiasisandopisthorchiasis pages 1-2).

---

## 12. Treatment
### Standard pharmacotherapy
The 2023 WHO-focused scoping review summarizes commonly reported treatments:
- **Triclabendazole** for fascioliasis (often **10 mg/kg once**, or **10 mg/kg/day for 2 days**) (tidman2023globalprevalenceof pages 9-10)
- **Praziquantel** as primary treatment for **paragonimiasis, clonorchiasis, opisthorchiasis** (tidman2023globalprevalenceof pages 1-2)

A 2024 authoritative liver fluke review confirms: “The mainstay of control is preventive chemotherapy with praziquantel” (qian2024clonorchiasisandopisthorchiasis pages 1-2).

### New/experimental therapeutics
- **Tribendimidine** is highlighted as having potential against *C. sinensis* and *O. viverrini* and “warrants further clinical development” (qian2024clonorchiasisandopisthorchiasis pages 1-2).

### Suggested MAXO terms (examples)
- Anthelmintic therapy (MAXO:0000013)
- Praziquantel therapy (tidman2023globalprevalenceof pages 1-2, qian2024clonorchiasisandopisthorchiasis pages 1-2)
- Triclabendazole therapy (tidman2023globalprevalenceof pages 9-10)

---

## 13. Prevention
### Primary prevention (food safety and behavior)
- WHO-targeted evidence highlights **health education/awareness**, improved sanitation/WASH, and reduction in risky food consumption as common preventive factors (tidman2023globalprevalenceof pages 1-2, prakobwong2025onehealthintegrated pages 1-2).

### Integrated “One Health” prevention/control (real-world implementation)
A 2025 One Health program in rural Thailand (2016–2022) integrated human screening/treatment with animal reservoir management, snail control, sanitation, and fish production interventions, achieving large measurable reductions:
- Human prevalence **14.1% → 0.9%**
- Fish metacercariae **21.9% → 2.2%**
- Dogs/cats **21.3% → 3.8%**
- Raw fish consumption **52.4% → 12.3%**
- Toilet use **31.7% → 87.1%** (prakobwong2025onehealthintegrated pages 1-2)
This study is a concrete contemporary example of scalable control aligned with WHO road map priorities for integrated approaches (liu2024globalregionaland pages 1-2, prakobwong2025onehealthintegrated pages 1-2).

---

## 14. Other species / natural disease
FBTs are zoonoses with animal reservoirs and intermediate hosts:
- WHO scoping review: lifecycle involves a **snail intermediate host** and (except *Fasciola*) a **secondary intermediate host**; humans infected via contaminated food (tidman2023globalprevalenceof pages 1-2).
- A 2024 liver fluke review states life cycles involve “animal reservoirs” and two intermediate hosts (snails and fish) (qian2024clonorchiasisandopisthorchiasis pages 1-2).
- One Health implementation directly measured infection in **dogs/cats** and **cyprinoid fish** as reservoir/food-chain components (prakobwong2025onehealthintegrated pages 1-2).

(Explicit NCBI Taxon identifiers and species lists were not provided in the retrieved evidence set.)

---

## 15. Model organisms
The retrieved evidence set did not provide detailed descriptions of experimental model organisms for all FBTs. However, the strong evidence base for One Health control and for diagnostics includes population-scale human field studies (kopolrat2025largescaleepidemiologyof pages 1-2, prakobwong2025onehealthintegrated pages 1-2). (Laboratory animal model details would require additional targeted retrieval beyond this evidence set.)

---

# Recent developments (prioritizing 2023–2024)
1. **Updated global burden estimates and projections** using **GBD 2021** (published Dec 2024) provide contemporary prevalence/DALY estimates and 2030 projections (liu2024globalregionaland pages 1-2).
2. **WHO-targeted scoping synthesis (Mar 2023)** consolidated prevalence ranges and highlighted surveillance gaps, diagnostic sensitivity limitations, and programmatic prevention/treatment practices (tidman2023globalprevalenceof pages 1-2, tidman2023globalprevalenceof pages 9-10).
3. **Authoritative clinical synthesis for clonorchiasis/opisthorchiasis** in *Clinical Microbiology Reviews* (Jan 2024 publication date stated in the excerpt) details epidemiology, diagnosis, and control framework and identifies promising drugs and novel control avenues (qian2024clonorchiasisandopisthorchiasis pages 1-2).
4. **Recognition of diagnostic underestimation and improved antigen testing** is supported by: (i) review-level evidence (2023) of antigen and point-of-care diagnostics (liau2023opisthorchisviverrini—currentunderstanding pages 6-7) and (ii) large-scale field evidence (2025) demonstrating urine antigen ELISA detects substantially more infections than stool microscopy (kopolrat2025largescaleepidemiologyof pages 1-2, kopolrat2025largescaleepidemiologyof pages 12-14).

---

# Key quoted statements from abstracts (for knowledge base evidence items)
- **GBD 2021 burden (published 2024):** “In 2021, **44,466,329 FBTs cases**… and **998,028 DALYs**…” (liu2024globalregionaland pages 1-2).
- **WHO scoping review (published 2023):** “FBTs are zoonotic diseases, with a complex lifecycle involving a primary intermediate snail host…” (tidman2023globalprevalenceof pages 1-2).
- **Clinical Microbiology Reviews (published 2024):** “Chronic infections are associated with liver and biliary complications, most importantly **cholangiocarcinoma**.” (qian2024clonorchiasisandopisthorchiasis pages 1-2).
- **Thailand diagnostic study (published 2025):** “The urine antigen assay revealed an overall opisthorchiasis prevalence of **50.3%**, a fourfold increase over the **12.2%** prevalence detected by FECT… the urine ELISA yielded a diagnostic sensitivity of **91.6%**, compared with **21.9%** for FECT.” (kopolrat2025largescaleepidemiologyof pages 1-2).
- **Thailand One Health intervention (published 2025):** “...reduced O. viverrini prevalence in humans from **14.1%** in 2016 to **0.9%** in 2022…” with reductions in reservoir hosts and fish and improvements in sanitation and behaviors (prakobwong2025onehealthintegrated pages 1-2).

---

# Limitations of this evidence synthesis
- Group-level ontology identifiers (MONDO/MeSH/ICD) and many disease-specific phenotype frequencies were not present in the retrieved evidence set; they should be added from ontology databases (e.g., MeSH, ICD-11, MONDO) in a dedicated follow-on curation step.
- Host genetic susceptibility, detailed molecular mechanisms beyond the inflammation–fibrosis–cancer chain, and formal differential diagnosis algorithms were not comprehensively captured in the retrieved evidence subset.

# Key sources (URLs; publication dates in evidence)
- Liu et al. **Dec 2024**. *Infectious Diseases of Poverty*. “Global, regional and national disease burden of food-borne trematodiases…” https://doi.org/10.1186/s40249-024-01265-6 (liu2024globalregionaland pages 1-2)
- Tidman et al. **Mar 2023**. *PLOS Neglected Tropical Diseases*. “Global prevalence of 4 neglected foodborne trematodes targeted for control by WHO…” https://doi.org/10.1371/journal.pntd.0011073 (tidman2023globalprevalenceof pages 1-2)
- Qian et al. **Jan 2024 (as stated in excerpt)**. *Clinical Microbiology Reviews*. “Clonorchiasis and opisthorchiasis…” https://doi.org/10.1128/cmr.00009-23 (qian2024clonorchiasisandopisthorchiasis pages 1-2)
- Kopolrat et al. **Jul 2025**. *PLOS Neglected Tropical Diseases*. “Large-scale epidemiology… urine antigen assay…” https://doi.org/10.1371/journal.pntd.0013095 (kopolrat2025largescaleepidemiologyof pages 1-2)
- Prakobwong et al. **Jun 2025**. *Infectious Diseases of Poverty*. “One Health integrated strategies…” https://doi.org/10.1186/s40249-025-01315-7 (prakobwong2025onehealthintegrated pages 1-2)
- Ortiz et al. **Jul 2024**. *Current Clinical Microbiology Reports*. “Foodborne helminthiasis” https://doi.org/10.1007/s40588-024-00231-y (ortiz2024foodbornehelminthiasis pages 1-2)
- Liau et al. **Jun 2023**. *Pathogens*. “Opisthorchis viverrini—Current understanding…” https://doi.org/10.3390/pathogens12060795 (liau2023opisthorchisviverrini—currentunderstanding pages 6-7)

References

1. (liu2024globalregionaland pages 1-2): Lu Liu, Li-Dan Lu, Guo-Jing Yang, Men-Bao Qian, Kun Yang, Feng Tan, and Xiao-Nong Zhou. Global, regional and national disease burden of food-borne trematodiases: projections to 2030 based on the global burden of disease study 2021. Infectious Diseases of Poverty, Dec 2024. URL: https://doi.org/10.1186/s40249-024-01265-6, doi:10.1186/s40249-024-01265-6. This article has 18 citations and is from a domain leading peer-reviewed journal.

2. (tidman2023globalprevalenceof pages 1-2): Rachel Tidman, Kaushi S. T. Kanankege, Mathieu Bangert, and Bernadette Abela-Ridder. Global prevalence of 4 neglected foodborne trematodes targeted for control by who: a scoping review to highlight the gaps. PLOS Neglected Tropical Diseases, 17:e0011073, Mar 2023. URL: https://doi.org/10.1371/journal.pntd.0011073, doi:10.1371/journal.pntd.0011073. This article has 57 citations and is from a domain leading peer-reviewed journal.

3. (ortiz2024foodbornehelminthiasis pages 1-2): Javier Benito Ortiz, Matthys Uys, Alessandro Seguino, and Lian F. Thomas. Foodborne helminthiasis. Current Clinical Microbiology Reports, 11:153-165, Jul 2024. URL: https://doi.org/10.1007/s40588-024-00231-y, doi:10.1007/s40588-024-00231-y. This article has 13 citations.

4. (qian2024clonorchiasisandopisthorchiasis pages 1-2): Men-Bao Qian, Jennifer Keiser, Jürg Utzinger, and Xiao-Nong Zhou. Clonorchiasis and opisthorchiasis: epidemiology, transmission, clinical features, morbidity, diagnosis, treatment, and control. Clinical Microbiology Reviews, Mar 2024. URL: https://doi.org/10.1128/cmr.00009-23, doi:10.1128/cmr.00009-23. This article has 57 citations and is from a highest quality peer-reviewed journal.

5. (tidman2023globalprevalenceof pages 9-10): Rachel Tidman, Kaushi S. T. Kanankege, Mathieu Bangert, and Bernadette Abela-Ridder. Global prevalence of 4 neglected foodborne trematodes targeted for control by who: a scoping review to highlight the gaps. PLOS Neglected Tropical Diseases, 17:e0011073, Mar 2023. URL: https://doi.org/10.1371/journal.pntd.0011073, doi:10.1371/journal.pntd.0011073. This article has 57 citations and is from a domain leading peer-reviewed journal.

6. (qian2024clonorchiasisandopisthorchiasis pages 2-4): Men-Bao Qian, Jennifer Keiser, Jürg Utzinger, and Xiao-Nong Zhou. Clonorchiasis and opisthorchiasis: epidemiology, transmission, clinical features, morbidity, diagnosis, treatment, and control. Clinical Microbiology Reviews, Mar 2024. URL: https://doi.org/10.1128/cmr.00009-23, doi:10.1128/cmr.00009-23. This article has 57 citations and is from a highest quality peer-reviewed journal.

7. (liau2023opisthorchisviverrini—currentunderstanding pages 6-7): Matthias Yi Quan Liau, En Qi Toh, and Vishalkumar Girishchandra Shelat. Opisthorchis viverrini—current understanding of the neglected hepatobiliary parasite. Pathogens, 12:795, Jun 2023. URL: https://doi.org/10.3390/pathogens12060795, doi:10.3390/pathogens12060795. This article has 30 citations.

8. (kopolrat2025largescaleepidemiologyof pages 1-2): Kulthida Y. Kopolrat, Chanika Worasith, Phattharaphon Wongphutorn, Anchalee Techasen, Chatanun Eamudomkarn, Jiraporn Sithithaworn, Watcharin Loilome, Nisana Namwat, Attapol Titapun, Chaiwat Tawarungruang, Bandit Thinkhamrop, Samarn Futrakul, Simon D. Taylor-Robinson, Melissa R. Haswell, Narong Khuntikeo, Thomas Crellen, and Paiboon Sithithaworn. Large-scale epidemiology of opisthorchiasis in 21 provinces in thailand based on diagnosis by fecal egg examination and urine antigen assay and analysis of risk factors for infection. PLOS Neglected Tropical Diseases, 19:e0013095, Jul 2025. URL: https://doi.org/10.1371/journal.pntd.0013095, doi:10.1371/journal.pntd.0013095. This article has 2 citations and is from a domain leading peer-reviewed journal.

9. (kopolrat2025largescaleepidemiologyof pages 12-14): Kulthida Y. Kopolrat, Chanika Worasith, Phattharaphon Wongphutorn, Anchalee Techasen, Chatanun Eamudomkarn, Jiraporn Sithithaworn, Watcharin Loilome, Nisana Namwat, Attapol Titapun, Chaiwat Tawarungruang, Bandit Thinkhamrop, Samarn Futrakul, Simon D. Taylor-Robinson, Melissa R. Haswell, Narong Khuntikeo, Thomas Crellen, and Paiboon Sithithaworn. Large-scale epidemiology of opisthorchiasis in 21 provinces in thailand based on diagnosis by fecal egg examination and urine antigen assay and analysis of risk factors for infection. PLOS Neglected Tropical Diseases, 19:e0013095, Jul 2025. URL: https://doi.org/10.1371/journal.pntd.0013095, doi:10.1371/journal.pntd.0013095. This article has 2 citations and is from a domain leading peer-reviewed journal.

10. (kopolrat2025largescaleepidemiologyof pages 8-12): Kulthida Y. Kopolrat, Chanika Worasith, Phattharaphon Wongphutorn, Anchalee Techasen, Chatanun Eamudomkarn, Jiraporn Sithithaworn, Watcharin Loilome, Nisana Namwat, Attapol Titapun, Chaiwat Tawarungruang, Bandit Thinkhamrop, Samarn Futrakul, Simon D. Taylor-Robinson, Melissa R. Haswell, Narong Khuntikeo, Thomas Crellen, and Paiboon Sithithaworn. Large-scale epidemiology of opisthorchiasis in 21 provinces in thailand based on diagnosis by fecal egg examination and urine antigen assay and analysis of risk factors for infection. PLOS Neglected Tropical Diseases, 19:e0013095, Jul 2025. URL: https://doi.org/10.1371/journal.pntd.0013095, doi:10.1371/journal.pntd.0013095. This article has 2 citations and is from a domain leading peer-reviewed journal.

11. (prakobwong2025onehealthintegrated pages 1-2): Suksanti Prakobwong, Lakhanawan Charoensuk, Suwit Chaipibool, Kacha Chedtabud, Umawadee Laothong, Apiporn T. Suwannatrai, David Blair, and Somchai Pinlaor. One health integrated strategies for sustainable control of opisthorchis viverrini infections in rural endemic areas of thailand. Infectious Diseases of Poverty, Jun 2025. URL: https://doi.org/10.1186/s40249-025-01315-7, doi:10.1186/s40249-025-01315-7. This article has 5 citations and is from a domain leading peer-reviewed journal.

12. (tenorio2021monstersinour pages 2-4): JCB Tenorio and EC Molina. Monsters in our food: foodborne trematodiasis in the philippines and beyond: https://doi. org/10.12982/vis. 2021.038. Unknown journal, 2021.
