---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-04-04T13:50:43.006166'
end_time: '2026-04-04T13:57:19.375511'
duration_seconds: 396.37
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Dracunculiasis
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 29
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dracunculiasis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Dracunculiasis** covering all of the
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
- **Disease Name:** Dracunculiasis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Dracunculiasis** covering all of the
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


# Dracunculiasis (Guinea Worm Disease): Disease Characteristics Research Report

**Target disease:** Dracunculiasis  
**Category:** Infectious disease (helminthic nematode infection)  
**Primary agent:** *Dracunculus medinensis* (nematode) (hopkins2024progresstowardglobal pages 1-2, cairncross2002dracunculiasis(guineaworm pages 1-3)

## Executive summary (current understanding and key 2023–2024 updates)
Dracunculiasis is a water- and food-associated parasitic infection in which a gravid female *D. medinensis* migrates to the skin and emerges—typically ~10–14 months after infection—causing painful blistering/ulceration and frequent secondary bacterial complications. (hopkins2024progresstowardglobal pages 1-2, simonetti2023thecurrentstate pages 1-2, pellegrino2022guineawormdisease pages 2-5). The eradication program reduced global incidence from an estimated **3.5 million cases/year (1986)** to **13 cases (2022)**, but elimination is increasingly constrained by **animal infections (especially dogs) and probable food-borne/paratenic transmission**, motivating a One Health “endgame” research agenda (2024) and new requirements for demonstrating absence of animal infections during certification. (hopkins2024progresstowardglobal pages 2-3, delea2024slayingtheserpent pages 1-2, hopkins2024progresstowardglobal pages 6-7).

As of **June 2024**, dracunculiasis remained endemic in **five countries (Angola, Chad, Ethiopia, Mali, South Sudan)**. In **2023**, there were **14 human cases** and **886 animal infections** worldwide; during **January–June 2024**, **3 human cases** and **297 animal infections** were reported. (hopkins2024progresstowardglobal pages 1-2, hopkins2024progresstowardglobal pages 2-3).

A key 2024 research development is the use of **ensemble machine-learning ecological niche/suitability modeling** in Chad using **2010–2022 surveillance data** and remotely sensed covariates to proactively target surveillance and intervention resources; the most important correlates included proximity to permanent surface water, precipitation, farmland/cropland, and land-surface temperature, with clustering along the Chari River. (eneanya2024predictingtheenvironmental pages 1-1, eneanya2024predictingtheenvironmental pages 4-6, eneanya2024predictingtheenvironmental pages 1-3).

## Compact evidence map
| Aspect | Current best-supported details | Notes on source type | Key citations |
|---|---|---|---|
| Definition / agent | Dracunculiasis (Guinea worm disease) is a neglected tropical helminthiasis caused by the nematode *Dracunculus medinensis*; adult gravid females migrate through subcutaneous tissues and emerge through skin, usually in the lower limbs. | MMWR + peer-reviewed reviews | (hopkins2024progresstowardglobal pages 1-2, simonetti2023thecurrentstate pages 1-2, cairncross2002dracunculiasis(guineaworm pages 1-3) |
| Incubation / timing | Incubation is typically about 10-14 months (~1 year) from infection to worm emergence; patients are often asymptomatic until emergence. | MMWR + peer-reviewed reviews | (hopkins2024progresstowardglobal pages 1-2, hopkins2024progresstowardglobal pages 2-3, pellegrino2022guineawormdisease pages 2-5, cairncross2002dracunculiasis(guineaworm pages 1-3) |
| Transmission routes | Classical route: drinking water containing infected copepods. Current understanding also supports food-borne transmission via inadequately cooked aquatic animals and/or paratenic/transport hosts such as frogs and fish, especially relevant in Chad. | MMWR + peer-reviewed reviews | (hopkins2024progresstowardglobal pages 1-2, simonetti2023thecurrentstate pages 2-4, simonetti2023thecurrentstate pages 1-2, hopkins2024progresstowardglobal pages 6-7) |
| Endemic countries as of June 2024 | As of June 2024, dracunculiasis remained endemic in 5 countries: Angola, Chad, Ethiopia, Mali, and South Sudan. WHO certification now also requires absence of indigenous animal infections. | MMWR + research agenda paper | (hopkins2024progresstowardglobal pages 1-2, hopkins2024progresstowardglobal pages 2-3, delea2024slayingtheserpent pages 1-2, hopkins2024progresstowardglobal pages 6-7) |
| Human cases: 2022, 2023, Jan-Jun 2024 | Global human cases fell to 13 in 2022, increased slightly to 14 in 2023, and 3 cases were reported during Jan-Jun 2024 (same as Jan-Jun 2023). Long-run decline is from ~3.5 million estimated annual cases in 1986. | MMWR primary program surveillance | (hopkins2024progresstowardglobal pages 2-3, hopkins2024progresstowardglobal pages 6-7, hopkins2023progresstowarderadication pages 1-2, hopkins2023progresstowarderadication pages 2-3) |
| Animal infections: 2022, 2023, Jan-Jun 2024 | Animal infections were 686 in 2022, 886 in 2023, and 297 during Jan-Jun 2024. In 2023, Chad reported 407 infected dogs and Cameroon 248 infected dogs; Chad had 496 total animal infections in 2023 (407 dogs, 89 cats). | MMWR primary program surveillance | (hopkins2024progresstowardglobal pages 1-2, hopkins2024progresstowardglobal pages 2-3, hopkins2024progresstowardglobal pages 6-7, hopkins2023progresstowarderadication pages 1-2) |
| Key animal hosts | Dogs are now the dominant animal host affecting eradication; cats and baboons are also involved, and a wild-caught genet was reported in South Sudan in 2023. Infections in animals have surpassed human cases since 2012. | MMWR + peer-reviewed review + research agenda | (hopkins2024progresstowardglobal pages 2-3, delea2024slayingtheserpent pages 1-2, hopkins2024progresstowardglobal pages 6-7, hopkins2023progresstowarderadication pages 1-2) |
| Major interventions | Core interventions are case containment, prevention of water contamination, cloth/pipe filtration of drinking water, treatment of unsafe water with temephos (Abate), provision of safe water, health education, safe cooking of aquatic animals, safe disposal of fish entrails, active village surveillance, cash rewards, and tethering of infected dogs. | MMWR + peer-reviewed reviews | (hopkins2024progresstowardglobal pages 1-2, hopkins2024progresstowardglobal pages 5-6, hopkins2023progresstowarderadication pages 6-7, hopkins2023progresstowarderadication pages 1-2, agua2025comparativeanalysisof pages 67-71) |
| Key challenges | Main endgame obstacles are animal reservoirs (especially dogs), possible food-borne/paratenic transmission, insecurity/civil unrest limiting access (notably Mali and parts of South Sudan/CAR border areas), under-detection, and lack of vaccines, therapeutics, or validated prepatent diagnostics. | MMWR + end-stage challenge/research agenda papers | (delea2024slayingtheserpent pages 1-2, hopkins2024progresstowardglobal pages 6-7, hopkins2023progresstowarderadication pages 6-7, tutu2023stoppingandtracing pages 1-3) |
| Recent development: One Health agenda (2024) | A 2024 research agenda proposed a systems-informed One Health approach to accelerate eradication, prioritizing tools for animal reservoir investigation, environmental surveillance, diagnostics, and intervention development aligned with a 2030 certification target. | Peer-reviewed 2024 research agenda | (delea2024slayingtheserpent pages 1-2) |
| Recent development: environmental suitability modeling (2024) | Ensemble machine-learning mapping in Chad (2010-2022 surveillance data) identified clustering along the Chari River and linked suitability to proximity to permanent rivers/inland lakes, farmlands, land-surface temperature, and precipitation to help target surveillance and interventions. | Peer-reviewed 2024 modeling study | (cairncross2002dracunculiasis(guineaworm pages 1-1) |
| Recent development: diagnostics / qPCR | Recent reviews note that conventional PCR is slow, while a Guinea worm qPCR has high sensitivity/specificity for confirming adult female infections in humans and animals; however, no widely implemented test yet detects prepatent infection for routine field control. | Peer-reviewed review + research agenda | (simonetti2023thecurrentstate pages 2-4, delea2024slayingtheserpent pages 1-2) |


*Table: This table summarizes the most current, best-supported facts about dracunculiasis, emphasizing 2022-2024 epidemiology, animal reservoirs, interventions, and recent research. It is useful as a compact evidence map for a disease knowledge base or briefing document.*

## 1. Disease information
### 1.1 What is the disease?
Dracunculiasis (Guinea worm disease) is a neglected tropical parasitic disease caused by the nematode *Dracunculus medinensis*. Humans (and now multiple animal hosts) are infected primarily through exposure associated with contaminated freshwater sources; clinical disease manifests when the adult gravid female migrates subcutaneously and emerges through the skin, producing a painful blister/ulcer and disability. (hopkins2024progresstowardglobal pages 1-2, simonetti2023thecurrentstate pages 1-2, cairncross2002dracunculiasis(guineaworm pages 1-3).

### 1.2 Key identifiers and synonyms
- **Synonyms/alternative names:** Guinea worm disease; dracunculosis (cairncross2002dracunculiasis(guineaworm pages 1-1, cairncross2002dracunculiasis(guineaworm pages 1-3).  
- **Key identifiers:** the accessible source corpus did **not** contain ontology or coding crosswalks (MONDO, MeSH, ICD-10/11, Orphanet, OMIM). Therefore, these identifiers cannot be tool-cited here and should be filled from authoritative coding resources (e.g., WHO ICD and NLM MeSH browsers).

### 1.3 Evidence provenance (patient-level vs aggregated)
Most current “disease status” information is **aggregated program surveillance** (national Guinea Worm Eradication Programs; compiled in CDC MMWR). (hopkins2024progresstowardglobal pages 1-2, hopkins2024progresstowardglobal pages 2-3). Clinical descriptions and pathophysiology are from **peer-reviewed narrative and systematic reviews**. (simonetti2023thecurrentstate pages 1-2, pellegrino2022guineawormdisease pages 2-5).

## 2. Etiology
### 2.1 Primary cause
The etiologic agent is the parasitic nematode *Dracunculus medinensis*. (hopkins2024progresstowardglobal pages 1-2, cairncross2002dracunculiasis(guineaworm pages 1-3).

### 2.2 Risk factors (environmental/exposure)
**Core exposure risk:** ingesting contaminated drinking water containing infected copepods (Cyclops and related genera) carrying infective larvae. (cairncross2002dracunculiasis(guineaworm pages 1-3).

**Emerging/expanded exposure hypotheses (major recent theme):** food-borne infection through ingestion of aquatic animals functioning as transport or paratenic hosts (fish/frogs) and/or inadequately cooked aquatic animals, which is emphasized as relevant to Chad’s epidemiology and to increasing dog infections. (simonetti2023thecurrentstate pages 2-4, simonetti2023thecurrentstate pages 1-2, hopkins2024progresstowardglobal pages 6-7).

**Environmental correlates (Chad, 2010–2022 surveillance; 2024 modeling):** proximity to permanent surface waters (rivers/inland lakes), precipitation patterns (including rainy season effects and temporary ponds), farmland/cropland, and land-surface temperature were major correlates of predicted suitability. (eneanya2024predictingtheenvironmental pages 1-1, eneanya2024predictingtheenvironmental pages 4-6, eneanya2024predictingtheenvironmental pages 1-3).

### 2.3 Protective factors
Protective factors are primarily **behavioral and environmental interventions**: filtering drinking water, provision of copepod-free/safe water sources, larviciding unsafe water sources with temephos, health education to prevent contaminated water exposure, adequate cooking of aquatic animals, and safe disposal of fish entrails (reducing dog exposure). (hopkins2024progresstowardglobal pages 1-2, hopkins2023progresstowarderadication pages 1-2).

### 2.4 Gene–environment interactions
No human genetic susceptibility or protective variants are established in the accessible evidence base for this disease; risk is dominated by exposure ecology and behavior. (hopkins2024progresstowardglobal pages 1-2, simonetti2023thecurrentstate pages 1-2).

## 3. Phenotypes
### 3.1 Clinical presentation (signs/symptoms)
Typical clinical course is characterized by a long asymptomatic incubation followed by localized inflammatory skin lesions that permit worm emergence.
- **Latency:** patients are often asymptomatic for ~1 year after infection. (pellegrino2022guineawormdisease pages 2-5).  
- **Lesion evolution:** painful papule enlarges to blister; blister ruptures to ulcer; gravid female emerges and releases larvae if lesion contacts water. (simonetti2023thecurrentstate pages 1-2, cairncross2002dracunculiasis(guineaworm pages 1-3).  
- **Anatomic distribution:** typically distal extremities, commonly lower limbs (below knees). (pellegrino2022guineawormdisease pages 2-5, cairncross2002dracunculiasis(guineaworm pages 1-3).

**Complications:** frequent secondary bacterial infection (reported as common and >50% of lesions in a recent review), cellulitis, abscesses, sepsis, pyogenic arthritis/septic arthritis, and tetanus are described as important complications. (simonetti2023thecurrentstate pages 2-4, pellegrino2022guineawormdisease pages 2-5).

### 3.2 Suggested HPO terms (examples; to be verified in HPO)
Because ontology identifiers were not retrieved directly from HPO in this run, below are suggested phenotype concepts for mapping:
- Painful blister/skin ulceration at extremities (blistering; skin ulcer; limb pain) (simonetti2023thecurrentstate pages 1-2, pellegrino2022guineawormdisease pages 2-5)  
- Cellulitis / abscess (simonetti2023thecurrentstate pages 2-4, pellegrino2022guineawormdisease pages 2-5)  
- Septic arthritis / arthritis (simonetti2023thecurrentstate pages 2-4, pellegrino2022guineawormdisease pages 2-5)  
- Fever / rash / nausea (systemic symptoms around emergence) (pellegrino2022guineawormdisease pages 2-5)  
- Sepsis (simonetti2023thecurrentstate pages 2-4)

### 3.3 Onset and progression
- **Onset:** delayed onset, usually ~10–14 months after infection. (hopkins2024progresstowardglobal pages 1-2, hopkins2024progresstowardglobal pages 2-3).  
- **Course:** emergence is painful and disabling; individuals may immerse limbs in water for relief, which facilitates transmission by larval release. (pellegrino2022guineawormdisease pages 2-5, cairncross2002dracunculiasis(guineaworm pages 1-3).

## 4. Genetic / molecular information
### 4.1 Human genetics
Dracunculiasis is not a Mendelian genetic disorder; no causal human gene is required for diagnosis. No human pathogenic variants were identified in the accessible sources. (hopkins2024progresstowardglobal pages 1-2, simonetti2023thecurrentstate pages 1-2).

### 4.2 Pathogen genetics and molecular tools
- **Species confirmation across hosts:** genetic studies used by eradication programs confirm that worms emerging from animals are *D. medinensis*, supporting that animal infections are part of the same eradication problem. (hopkins2023progresstowarderadication pages 1-2).  
- **Molecular diagnostics:** a narrative review reports that serology has limited diagnostic value; conventional PCR turnaround can be slow, whereas a Guinea worm qPCR is described as having high sensitivity/specificity for confirming adult female infections in humans and animals. (simonetti2023thecurrentstate pages 2-4).  
- **Immunologic correlates reported in active infection:** elevated parasite-specific IgG1/IgG4 with relatively low IgE and depressed IFN-γ have been described, though these are not currently positioned as routine biomarkers for field control. (simonetti2023thecurrentstate pages 2-4).

## 5. Environmental information
### 5.1 Environmental and lifestyle factors
Transmission is tightly linked to **freshwater ecology**, where copepods can host infective larvae and where human water procurement and aquatic food practices create exposure routes. (cairncross2002dracunculiasis(guineaworm pages 1-3, hopkins2024progresstowardglobal pages 6-7). Farming/fishing contexts and proximity to major rivers (e.g., Chari River basin in Chad) are highlighted as important correlates of suitability. (eneanya2024predictingtheenvironmental pages 1-1, eneanya2024predictingtheenvironmental pages 1-3).

### 5.2 Infectious agent taxonomy
The causative agent is *Dracunculus medinensis* (nematode; family Dracunculidae). (simonetti2023thecurrentstate pages 1-2, cairncross2002dracunculiasis(guineaworm pages 1-3).

## 6. Mechanism / pathophysiology
### 6.1 Causal chain (trigger → mechanism → manifestation)
1. **Exposure:** ingestion of infected copepods in drinking water (classical) and/or ingestion of infected aquatic animals (suspected/important in Chad). (cairncross2002dracunculiasis(guineaworm pages 1-3, hopkins2024progresstowardglobal pages 6-7).  
2. **Larval migration/maturation:** larvae penetrate the intestinal wall and migrate through connective tissues; adults mature and mate over months. (simonetti2023thecurrentstate pages 1-2, cairncross2002dracunculiasis(guineaworm pages 1-3).  
3. **Delayed clinical disease:** after ~10–14 months, the gravid female migrates subcutaneously to distal sites, provoking a painful blister/ulcer. (hopkins2024progresstowardglobal pages 1-2, cairncross2002dracunculiasis(guineaworm pages 1-3).  
4. **Transmission event:** contact with water induces larval release, perpetuating the cycle via copepods. (cairncross2002dracunculiasis(guineaworm pages 1-3).

### 6.2 Biological processes and cell types (ontology suggestions)
Direct GO/CL IDs were not retrieved in the accessible corpus; suggested mappings include:
- **GO (process concepts):** inflammatory response; wound healing; leukocyte-mediated immunity; response to parasite. (simonetti2023thecurrentstate pages 2-4, simonetti2023thecurrentstate pages 1-2).  
- **CL (cell concepts):** neutrophils/monocytes/macrophages involved in blister fluid inflammatory infiltrates (conceptual; review-level). (simonetti2023thecurrentstate pages 1-2).

### 6.3 Recent mechanistic research directions (2024)
A 2024 eradication “research agenda” emphasizes that eradication progressed largely without vaccines/therapeutics/early diagnostics, and it prioritizes development of new interventions, diagnostics (including prepatent detection), and environmental surveillance tools within a One Health framework. (delea2024slayingtheserpent pages 1-2).

## 7. Anatomical structures affected
### 7.1 Organ/tissue level
Primary pathology is in **skin and subcutaneous connective tissue** of distal extremities (often lower limbs), with secondary involvement of soft tissues and joints due to bacterial complications (cellulitis, abscess, septic arthritis). (simonetti2023thecurrentstate pages 2-4, pellegrino2022guineawormdisease pages 2-5, cairncross2002dracunculiasis(guineaworm pages 1-3).

### 7.2 Suggested UBERON mapping (concepts)
Not directly retrievable from Uberon in this run; suggested sites include lower limb (leg/foot), skin, subcutaneous tissue, and synovial joints (for septic arthritis). (pellegrino2022guineawormdisease pages 2-5, cairncross2002dracunculiasis(guineaworm pages 1-3).

## 8. Temporal development
- **Incubation period:** ~10–14 months (hopkins2024progresstowardglobal pages 1-2, hopkins2024progresstowardglobal pages 2-3).  
- **Seasonality (programmatic relevance):** rainy season and related water-body dynamics influence suitability and predicted risk in Chad; peaks are associated with rainfall/temporary pond formation and river-associated fishing practices. (eneanya2024predictingtheenvironmental pages 8-9, eneanya2024predictingtheenvironmental pages 1-1).

## 9. Inheritance and population
### 9.1 Epidemiology (recent statistics)
- **Endemic countries (June 2024):** Angola, Chad, Ethiopia, Mali, South Sudan. (hopkins2024progresstowardglobal pages 1-2).  
- **Global human cases:** 13 (2022) → 14 (2023) → 3 (Jan–Jun 2024). (hopkins2024progresstowardglobal pages 2-3, hopkins2023progresstowarderadication pages 2-3).  
- **Global animal infections:** 686 (2022) → 886 (2023) → 297 (Jan–Jun 2024). (hopkins2024progresstowardglobal pages 2-3, hopkins2023progresstowarderadication pages 1-2).  
- **Animal infections dominate:** animal infections have surpassed human cases since 2012, constituting the principal “endgame” challenge. (hopkins2023progresstowarderadication pages 1-2, hopkins2024progresstowardglobal pages 6-7).

### 9.2 Geographic distribution and hotspots
Chad accounts for a large share of remaining infections, and transmission is described as linked to aquatic animal consumption. (hopkins2024progresstowardglobal pages 2-3, hopkins2024progresstowardglobal pages 6-7). In Chad, suitability modeling shows clustering in southern regions along the Chari River and predicted suitability near borders with Cameroon and the Central African Republic. (eneanya2024predictingtheenvironmental pages 1-1, eneanya2024predictingtheenvironmental pages 1-3).

### 9.3 Demographics
The accessible sources do not provide robust sex ratio or age distribution estimates; where case examples are given (e.g., a 47-year-old woman in CAR), these are anecdotal and not population distributions. (sudan2024datefebruary26 pages 3-5).

## 10. Diagnostics
### 10.1 Clinical/laboratory diagnosis
- **Case definition used in eradication surveillance:** a person with skin lesion(s) from which one or more worms emerge, with laboratory confirmation at CDC as *D. medinensis*. (hopkins2024progresstowardglobal pages 2-3).  
- **Specimen confirmation:** specimens requiring confirmation are sent to CDC, and national programs rely on village-based reporting and supervisory verification. (hopkins2024progresstowardglobal pages 1-2, hopkins2023progresstowarderadication pages 1-2).  
- **Serology:** described as of limited value in a 2023 narrative review. (simonetti2023thecurrentstate pages 2-4).  
- **PCR/qPCR:** conventional PCR described as slow; qPCR described as sensitive/specific for confirming adult female infections. (simonetti2023thecurrentstate pages 2-4).

### 10.2 Surveillance and certification diagnostics (public health implementation)
- **Active village-based surveillance:** includes daily household searches by trained volunteers and monthly reporting systems; “rumor” reporting and investigations are used operationally. (hopkins2024progresstowardglobal pages 1-2, hopkins2023progresstowarderadication pages 2-3).  
- **WHO certification standard:** at least **3 consecutive years** of adequate nationwide surveillance with **no indigenous human case or animal infection** is required. (hopkins2024progresstowardglobal pages 2-3, hopkins2023progresstowarderadication pages 1-2).

### 10.3 Differential diagnosis
Differentials are not enumerated in the accessible text excerpts; clinically, any blistering ulcerative lesion with secondary infection could mimic other causes, but definitive diagnosis is often direct observation of an emerging worm. (hopkins2024progresstowardglobal pages 2-3, pellegrino2022guineawormdisease pages 2-5).

## 11. Outcome / prognosis
The disease is typically not described as high-mortality in the accessible corpus, but it produces substantial morbidity through pain, disability, and complications such as cellulitis, sepsis, destructive joint disease, and tetanus. (simonetti2023thecurrentstate pages 2-4, pellegrino2022guineawormdisease pages 2-5). Quantitative survival or long-term disability statistics were not present in the retrieved excerpts.

## 12. Treatment
### 12.1 Pharmacotherapy / vaccines
No vaccine or drug treatment exists for dracunculiasis in current eradication program descriptions. (hopkins2024progresstowardglobal pages 1-2).

### 12.2 Supportive and interventional care
Clinical management is primarily supportive: careful extraction/management of emerging worms, wound care, and treatment/prevention of secondary bacterial infection and tetanus complications (not quantified in the accessible excerpts). (pellegrino2022guineawormdisease pages 2-5, simonetti2023thecurrentstate pages 2-4).

### 12.3 Candidate MAXO terms (conceptual)
MAXO identifiers were not retrieved directly; suggested actions include wound care, antiparasitic removal/extraction procedure, antibiotic therapy for secondary infection, tetanus prophylaxis, safe water provision, water filtration, larvicide application, health education, and animal tethering. (hopkins2024progresstowardglobal pages 1-2, hopkins2023progresstowarderadication pages 1-2).

## 13. Prevention
Prevention is the cornerstone of eradication and includes multiple complementary community-based interventions:
- **Water safety:** filtration of drinking water; provision of safe (copepod-free) drinking water sources. (hopkins2024progresstowardglobal pages 1-2, hopkins2023progresstowarderadication pages 1-2).  
- **Vector control:** treatment of unsafe water sources with temephos (Abate). (hopkins2023progresstowarderadication pages 1-2, agua2025comparativeanalysisof pages 67-71).  
- **Transmission interruption/case containment:** prevent infected humans and animals from entering water sources; structured containment criteria are used operationally. (hopkins2024progresstowardglobal pages 1-2).  
- **Food-related interventions:** adequate cooking of aquatic animals and safe disposal of fish entrails to reduce transmission to dogs. (hopkins2024progresstowardglobal pages 1-2).  
- **Behavior change and incentives:** health education and cash rewards for reporting; rewards have been increased in some settings to enhance detection. (hopkins2024progresstowardglobal pages 5-6, hopkins2024progresstowardglobal pages 6-7).

## 14. Other species / natural disease (One Health)
### 14.1 Non-human hosts and eradication impact
Since 2012, infections have been detected in domesticated dogs (first detected in Chad), and later in cats and baboons; animal infections now constitute the dominant remaining burden and complicate eradication. (delea2024slayingtheserpent pages 1-2, hopkins2023progresstowarderadication pages 1-2). A wild-caught genet infection was reported for the first time in South Sudan in 2023 (hopkins2024progresstowardglobal pages 6-7). A WHO/CDC wrap-up notes additional animal surveillance events, including an infected donkey detected in Mali (Dec 2023) and inspection of dead/trapped baboons in Ethiopia. (sudan2024datefebruary26 pages 3-5).

### 14.2 Zoonotic framing
The current eradication challenge resembles a One Health problem (human–animal–environment transmission). The 2024 research agenda explicitly adopts a systems-informed One Health approach to tool development and evidence generation for certification. (delea2024slayingtheserpent pages 1-2).

## 15. Model organisms / experimental systems
The accessible corpus did not include laboratory animal model descriptions for *D. medinensis* infection in a way that supports structured annotation. Current work emphasized is field surveillance, ecological modeling, and development of diagnostics and interventions rather than experimental model systems. (delea2024slayingtheserpent pages 1-2, eneanya2024predictingtheenvironmental pages 1-1).

## Recent developments and expert analysis (prioritizing 2023–2024)
### 2023: Updated clinical synthesis and diagnostic discussion
A 2023 narrative review emphasizes an evolving transmission paradigm: in addition to classical waterborne copepod infection, ingestion of frogs (paratenic) or fish (transport) hosts may contribute to current epidemiology and increasing animal infections, and it notes qPCR improvements for confirmatory testing alongside limited serologic utility. (simonetti2023thecurrentstate pages 2-4, simonetti2023thecurrentstate pages 1-2).

### 2024: CDC MMWR eradication update (programmatic “ground truth”)
The 2024 MMWR provides primary surveillance statistics (2022–mid-2024), highlights animal infections as the main constraint to near-term eradication, and documents real-world intervention implementation (temephos, filtration, tethering, cooking guidance, rewards, village surveillance, and WHO certification criteria). (hopkins2024progresstowardglobal pages 1-2, hopkins2024progresstowardglobal pages 2-3, hopkins2024progresstowardglobal pages 6-7).

### 2024: Research agenda for endgame tool development
The 2024 “Slaying the Serpent” agenda argues that eradication is being pursued despite the absence of vaccines/therapeutics/prepatent diagnostics and proposes prioritized work streams (diagnostics, surveillance, intervention development) coordinated to a 2030 certification target, explicitly motivated by the emergence of animal infections since 2012. (delea2024slayingtheserpent pages 1-2).

### 2024: Environmental suitability mapping as an operational tool
Eneanya et al. (published online **July 9, 2024**) used 2010–2022 village-level infection records (dominated by dog records) and ensemble modeling to generate 1 km² suitability surfaces and identify major covariates (surface water proximity, precipitation, farmland, LST), intended to optimize surveillance and intervention allocation as Chad approaches elimination. (eneanya2024predictingtheenvironmental pages 1-3, eneanya2024predictingtheenvironmental pages 4-6, eneanya2024predictingtheenvironmental pages 9-10).

## Limitations of this tool-based report (important for knowledge-base curation)
1. **ICD/MeSH/MONDO/Orphanet/OMIM identifiers** were not present in the retrieved full-text evidence and therefore cannot be provided with tool-citations here; these should be sourced directly from ICD and MeSH browsers and MONDO/Orphanet portals during curation.  
2. **PMIDs** were not available in the retrieved text snippets/metadata for the key 2023–2024 papers in this run; URLs/DOIs and publication months/years are provided instead.  
3. Several template elements (e.g., QoL instruments, prevalence/incidence per 100,000, robust demographic distributions, detailed differential diagnosis lists, experimental model organism phenotyping) were not available in the accessible excerpts and are flagged as gaps.

## Key sources (with URLs and publication dates)
- Hopkins DR et al. **“Progress Toward Global Dracunculiasis (Guinea Worm Disease) Eradication, January 2023–June 2024.”** *MMWR*, **Nov 2024**. https://doi.org/10.15585/mmwr.mm7344a1 (hopkins2024progresstowardglobal pages 1-2, hopkins2024progresstowardglobal pages 2-3).  
- Delea MG et al. **“Slaying the Serpent: A Research Agenda to Expand Intervention Development and Accelerate Guinea Worm Eradication Efforts.”** *Am J Trop Med Hyg*, **Sep 2024**. https://doi.org/10.4269/ajtmh.23-0889 (delea2024slayingtheserpent pages 1-2).  
- Eneanya OA et al. **“Predicting the Environmental Suitability and Identifying Climate and Sociodemographic Correlates of Guinea Worm (Dracunculus medinensis) in Chad.”** *Am J Trop Med Hyg*, online **Jul 9, 2024**; issue **Sep 2024**. https://doi.org/10.4269/ajtmh.23-0681 (eneanya2024predictingtheenvironmental pages 1-1, eneanya2024predictingtheenvironmental pages 4-6, eneanya2024predictingtheenvironmental pages 9-10).  
- Simonetti O et al. **“The current state of knowledge on dracunculiasis: a narrative review of a rare neglected disease.”** *Le infezioni in medicina*, **Dec 2023**. https://doi.org/10.53854/liim-3104-9 (simonetti2023thecurrentstate pages 1-2, simonetti2023thecurrentstate pages 2-4).  
- Cairncross S et al. **“Dracunculiasis (Guinea Worm Disease) and the Eradication Initiative.”** *Clinical Microbiology Reviews*, **Apr 2002**. https://doi.org/10.1128/cmr.15.2.223-246.2002 (cairncross2002dracunculiasis(guineaworm pages 1-3).


References

1. (hopkins2024progresstowardglobal pages 1-2): Donald R. Hopkins, Adam J. Weiss, Sarah Yerian, Yujing Zhao, Sarah G.H. Sapp, and Vitaliano A. Cama. Progress toward global dracunculiasis (guinea worm disease) eradication, january 2023–june 2024. Morbidity and Mortality Weekly Report, 73:991-998, Nov 2024. URL: https://doi.org/10.15585/mmwr.mm7344a1, doi:10.15585/mmwr.mm7344a1. This article has 14 citations.

2. (cairncross2002dracunculiasis(guineaworm pages 1-3): Sandy Cairncross, Ralph Muller, and Nevio Zagaria. Dracunculiasis (guinea worm disease) and the eradication initiative. Clinical Microbiology Reviews, 15:223-246, Apr 2002. URL: https://doi.org/10.1128/cmr.15.2.223-246.2002, doi:10.1128/cmr.15.2.223-246.2002. This article has 237 citations and is from a highest quality peer-reviewed journal.

3. (simonetti2023thecurrentstate pages 1-2): Omar Simonetti, V. Zerbato, C. Maurel, Lavinia Cosimi, Stella Babich, Fabio Cavalli, Stefano Di Bella, D. Pavia, C. Pesaresi, and Roberto Luzzati. The current state of knowledge on dracunculiasis: a narrative review of a rare neglected disease. Le infezioni in medicina, 31 4:500-508, Dec 2023. URL: https://doi.org/10.53854/liim-3104-9, doi:10.53854/liim-3104-9. This article has 6 citations.

4. (pellegrino2022guineawormdisease pages 2-5): Carmen Pellegrino, Giulia Patti, Michele Camporeale, Alessandra Belati, Roberta Novara, Roberta Papagni, Luisa Frallonardo, Lucia Diella, Giacomo Guido, Elda De Vita, Valentina Totaro, Francesco Vladimiro Segala, Nicola Veronese, Sergio Cotugno, Davide Fiore Bavaro, Giovanni Putoto, Nazario Bevilacqua, Chiara Castellani, Emanuele Nicastri, Annalisa Saracino, and Francesco Di Gennaro. Guinea worm disease: a neglected diseases on the verge of eradication. Tropical Medicine and Infectious Disease, 7:366, Nov 2022. URL: https://doi.org/10.3390/tropicalmed7110366, doi:10.3390/tropicalmed7110366. This article has 19 citations.

5. (hopkins2024progresstowardglobal pages 2-3): Donald R. Hopkins, Adam J. Weiss, Sarah Yerian, Yujing Zhao, Sarah G.H. Sapp, and Vitaliano A. Cama. Progress toward global dracunculiasis (guinea worm disease) eradication, january 2023–june 2024. Morbidity and Mortality Weekly Report, 73:991-998, Nov 2024. URL: https://doi.org/10.15585/mmwr.mm7344a1, doi:10.15585/mmwr.mm7344a1. This article has 14 citations.

6. (delea2024slayingtheserpent pages 1-2): Maryann G. Delea, Alexandra Sack, Obiora A. Eneanya, Elizabeth Thiele, Sharon L. Roy, Dieudonne Sankara, Kashef Ijaz, Donald R. Hopkins, and Adam J. Weiss. Slaying the serpent: a research agenda to expand intervention development and accelerate guinea worm eradication efforts. The American Journal of Tropical Medicine and Hygiene, 111:12-25, Sep 2024. URL: https://doi.org/10.4269/ajtmh.23-0889, doi:10.4269/ajtmh.23-0889. This article has 5 citations.

7. (hopkins2024progresstowardglobal pages 6-7): Donald R. Hopkins, Adam J. Weiss, Sarah Yerian, Yujing Zhao, Sarah G.H. Sapp, and Vitaliano A. Cama. Progress toward global dracunculiasis (guinea worm disease) eradication, january 2023–june 2024. Morbidity and Mortality Weekly Report, 73:991-998, Nov 2024. URL: https://doi.org/10.15585/mmwr.mm7344a1, doi:10.15585/mmwr.mm7344a1. This article has 14 citations.

8. (eneanya2024predictingtheenvironmental pages 1-1): Obiora A. Eneanya, Maryann G. Delea, Jorge Cano, Philip Ouakou Tchindebet, Robert L. Richards, Yujing Zhao, Abdalla Meftuh, Karmen Unterwegner, Sarah Anne J. Guagliardo, Donald R. Hopkins, and Adam Weiss. Predicting the environmental suitability and identifying climate and sociodemographic correlates of guinea worm (dracunculus medinensis) in chad. The American Journal of Tropical Medicine and Hygiene, 111:26-35, Sep 2024. URL: https://doi.org/10.4269/ajtmh.23-0681, doi:10.4269/ajtmh.23-0681. This article has 4 citations.

9. (eneanya2024predictingtheenvironmental pages 4-6): Obiora A. Eneanya, Maryann G. Delea, Jorge Cano, Philip Ouakou Tchindebet, Robert L. Richards, Yujing Zhao, Abdalla Meftuh, Karmen Unterwegner, Sarah Anne J. Guagliardo, Donald R. Hopkins, and Adam Weiss. Predicting the environmental suitability and identifying climate and sociodemographic correlates of guinea worm (dracunculus medinensis) in chad. The American Journal of Tropical Medicine and Hygiene, 111:26-35, Sep 2024. URL: https://doi.org/10.4269/ajtmh.23-0681, doi:10.4269/ajtmh.23-0681. This article has 4 citations.

10. (eneanya2024predictingtheenvironmental pages 1-3): Obiora A. Eneanya, Maryann G. Delea, Jorge Cano, Philip Ouakou Tchindebet, Robert L. Richards, Yujing Zhao, Abdalla Meftuh, Karmen Unterwegner, Sarah Anne J. Guagliardo, Donald R. Hopkins, and Adam Weiss. Predicting the environmental suitability and identifying climate and sociodemographic correlates of guinea worm (dracunculus medinensis) in chad. The American Journal of Tropical Medicine and Hygiene, 111:26-35, Sep 2024. URL: https://doi.org/10.4269/ajtmh.23-0681, doi:10.4269/ajtmh.23-0681. This article has 4 citations.

11. (simonetti2023thecurrentstate pages 2-4): Omar Simonetti, V. Zerbato, C. Maurel, Lavinia Cosimi, Stella Babich, Fabio Cavalli, Stefano Di Bella, D. Pavia, C. Pesaresi, and Roberto Luzzati. The current state of knowledge on dracunculiasis: a narrative review of a rare neglected disease. Le infezioni in medicina, 31 4:500-508, Dec 2023. URL: https://doi.org/10.53854/liim-3104-9, doi:10.53854/liim-3104-9. This article has 6 citations.

12. (hopkins2023progresstowarderadication pages 1-2): DR Hopkins. Progress toward eradication of dracunculiasis—worldwide, january 2022–june 2023. Unknown journal, 2023.

13. (hopkins2023progresstowarderadication pages 2-3): DR Hopkins. Progress toward eradication of dracunculiasis—worldwide, january 2022–june 2023. Unknown journal, 2023.

14. (hopkins2024progresstowardglobal pages 5-6): Donald R. Hopkins, Adam J. Weiss, Sarah Yerian, Yujing Zhao, Sarah G.H. Sapp, and Vitaliano A. Cama. Progress toward global dracunculiasis (guinea worm disease) eradication, january 2023–june 2024. Morbidity and Mortality Weekly Report, 73:991-998, Nov 2024. URL: https://doi.org/10.15585/mmwr.mm7344a1, doi:10.15585/mmwr.mm7344a1. This article has 14 citations.

15. (hopkins2023progresstowarderadication pages 6-7): DR Hopkins. Progress toward eradication of dracunculiasis—worldwide, january 2022–june 2023. Unknown journal, 2023.

16. (agua2025comparativeanalysisof pages 67-71): J Agua. Comparative analysis of risk factors associated with guinea worm disease in five endemic countries. Unknown journal, 2025.

17. (tutu2023stoppingandtracing pages 1-3): D Tutu. Stopping and tracing guinea worm transmission in 2023. Unknown journal, 2023.

18. (cairncross2002dracunculiasis(guineaworm pages 1-1): Sandy Cairncross, Ralph Muller, and Nevio Zagaria. Dracunculiasis (guinea worm disease) and the eradication initiative. Clinical Microbiology Reviews, 15:223-246, Apr 2002. URL: https://doi.org/10.1128/cmr.15.2.223-246.2002, doi:10.1128/cmr.15.2.223-246.2002. This article has 237 citations and is from a highest quality peer-reviewed journal.

19. (eneanya2024predictingtheenvironmental pages 8-9): Obiora A. Eneanya, Maryann G. Delea, Jorge Cano, Philip Ouakou Tchindebet, Robert L. Richards, Yujing Zhao, Abdalla Meftuh, Karmen Unterwegner, Sarah Anne J. Guagliardo, Donald R. Hopkins, and Adam Weiss. Predicting the environmental suitability and identifying climate and sociodemographic correlates of guinea worm (dracunculus medinensis) in chad. The American Journal of Tropical Medicine and Hygiene, 111:26-35, Sep 2024. URL: https://doi.org/10.4269/ajtmh.23-0681, doi:10.4269/ajtmh.23-0681. This article has 4 citations.

20. (sudan2024datefebruary26 pages 3-5): S Sudan. Date: february 26, 2024 from: who collaborating center for dracunculiasis eradication, cdc subject: guinea worm wrap-up# 306 to: addressees. Unknown journal, 2024.

21. (eneanya2024predictingtheenvironmental pages 9-10): Obiora A. Eneanya, Maryann G. Delea, Jorge Cano, Philip Ouakou Tchindebet, Robert L. Richards, Yujing Zhao, Abdalla Meftuh, Karmen Unterwegner, Sarah Anne J. Guagliardo, Donald R. Hopkins, and Adam Weiss. Predicting the environmental suitability and identifying climate and sociodemographic correlates of guinea worm (dracunculus medinensis) in chad. The American Journal of Tropical Medicine and Hygiene, 111:26-35, Sep 2024. URL: https://doi.org/10.4269/ajtmh.23-0681, doi:10.4269/ajtmh.23-0681. This article has 4 citations.
