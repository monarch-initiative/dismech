---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-08T09:20:19.553388'
end_time: '2026-05-08T09:28:55.328650'
duration_seconds: 515.78
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Oculogastrointestinal-neurodevelopmental syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 12
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Oculogastrointestinal-neurodevelopmental syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Oculogastrointestinal-neurodevelopmental syndrome** covering all of the
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
- **Disease Name:** Oculogastrointestinal-neurodevelopmental syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Oculogastrointestinal-neurodevelopmental syndrome** covering all of the
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


## Comprehensive Research Report: Oculogastrointestinal-neurodevelopmental syndrome (CAPN15-related)

### Target disease
- **Disease name:** Oculogastrointestinal-neurodevelopmental syndrome (OGN)
- **Category:** Mendelian (autosomal recessive)
- **Causal gene:** **CAPN15**

| Disease name | Synonyms | OMIM | Causal gene | Inheritance | Key publications | Reported case counts | Key novel finding |
|---|---|---|---|---|---|---|---|
| Oculogastrointestinal-neurodevelopmental syndrome | Oculogastrointestinal neurodevelopmental syndrome; CAPN15-related oculogastrointestinal-neurodevelopmental syndrome | 619318 | **CAPN15** | Autosomal recessive (biallelic pathogenic variants) | **Beaman et al.** *Am J Med Genet A* (Aug 2023). DOI: https://doi.org/10.1002/ajmg.a.63363; **Zucco et al.** *J Hum Genet* (Mar 2024). DOI: https://doi.org/10.1038/s10038-024-01237-6 | 7 previously published individuals + 6 new molecularly confirmed individuals reported by Beaman et al. = **13 total** reported individuals at that time; Zucco 2024 summarizes the disorder as described in **<10 published individuals** prior to newer case additions (beaman2023novelassociationof pages 1-3, zucco2024abird’seye pages 9-10) | **Dandy–Walker malformation** added to the phenotype spectrum in Beaman et al. 2023, including the classical triad in 4 affected individuals (hypoplastic vermis, fourth ventricle enlargement, torcular elevation) (beaman2023novelassociationof pages 1-3, beaman2023novelassociationof pages 3-5) |
| Publication detail | — | — | — | — | Beaman et al.: publication date **Aug 2023**, URL https://doi.org/10.1002/ajmg.a.63363 (beaman2023novelassociationof pages 1-3); Zucco et al.: publication date **Mar 2024**, URL https://doi.org/10.1038/s10038-024-01237-6 (zucco2024abird’seye pages 9-10) | — | — |


*Table: This table summarizes the core identifiers, inheritance, causal gene, key literature, case counts, and the major 2023 phenotype expansion for oculogastrointestinal-neurodevelopmental syndrome. It is useful as a compact reference for disease knowledge base curation.*

## 1. Disease information

### Overview / definition
Oculogastrointestinal-neurodevelopmental syndrome is an **ultra-rare, autosomal-recessive, multisystem congenital disorder** caused by **biallelic pathogenic variants in CAPN15**, characterized by **congenital ocular malformations**, **gastrointestinal/anorectal anomalies**, and **neurodevelopmental impairment**, with expanding evidence for **hindbrain malformations including Dandy–Walker malformation**. (beaman2023novelassociationof pages 1-3, zucco2024abird’seye pages 9-10)

### Key identifiers
- **OMIM:** **#619318** (listed for oculogastrointestinal neurodevelopmental syndrome in a 2023 primary case series) (beaman2023novelassociationof pages 1-3)
- **Other identifiers (Orphanet, MONDO, MeSH, ICD-10/ICD-11):** Not located in the retrieved sources; additional targeted database lookups would be required.

### Synonyms / alternative names
- **Oculogastrointestinal neurodevelopmental syndrome** (OGN) (beaman2023novelassociationof pages 1-3)
- **Oculogastrointestinal-neurodevelopmental syndrome** (hyphenated form used in 2024 review) (zucco2024abird’seye pages 9-10)
- **CAPN15-related oculogastrointestinal-neurodevelopmental syndrome** (gene-based synonym used in the literature context) (zucco2024abird’seye pages 9-10)

### Evidence base type
The available evidence is derived primarily from **individual/family case reports and case series** with molecular confirmation, with supportive **animal model** and **in vitro patient-fibroblast** functional studies in at least one 2023 report. (beaman2023novelassociationof pages 5-6, beaman2023novelassociationof pages 6-8)

## 2. Etiology

### Disease causal factors
- **Primary cause:** **Biallelic pathogenic variants in CAPN15** (autosomal recessive). (beaman2023novelassociationof pages 1-3, zucco2024abird’seye pages 9-10)

**Abstract quote (primary literature, 2023):** The 2023 case series states the syndrome “**has been described in seven previously published individuals who harbor biallelic pathogenic variants in the CAPN15 gene**” and reports additional molecularly confirmed individuals. (beaman2023novelassociationof pages 1-3)

### Risk factors
- **Genetic risk factor:** Having **biallelic deleterious CAPN15 variants**; several reported families include **consanguinity**, consistent with enrichment of homozygous rare alleles in such pedigrees. (beaman2023novelassociationof pages 5-6)
- **Environmental risk factors:** No evidence found in retrieved sources; for a Mendelian congenital syndrome, environmental risk factors are not currently established.

### Protective factors / gene–environment interactions
No protective factors or gene–environment interactions were identified in the retrieved sources.

## 3. Phenotypes

### Core phenotype domains (human)
The reported phenotype spans ocular, gastrointestinal/anorectal, neurologic/neurodevelopmental, growth, and multi-organ congenital anomalies.

#### Ocular phenotypes (congenital)
Examples reported include **microphthalmia**, **coloboma**, **corneal clouding**, **iridocorneal adhesions**, and strabismus-related findings. (beaman2023novelassociationof pages 6-8, zucco2024abird’seye pages 9-10)

Suggested HPO terms (non-exhaustive, based on reported features):
- Microphthalmia (HP:0000568)
- Coloboma (HP:0000589)
- Corneal opacity / clouding (HP:0007957)
- Anterior segment dysgenesis / iridocorneal adhesions (HP:0007830 or related ASD terms)
- Strabismus (HP:0000486)

#### Gastrointestinal/anorectal phenotypes
Reported congenital GI/anorectal anomalies include **anal atresia** and **rectovestibular fistula**. (beaman2023novelassociationof pages 6-8, beaman2023novelassociationof pages 3-5)

Suggested HPO terms:
- Anal atresia (HP:0002023)
- Rectovaginal/rectovestibular fistula (HPO term selection depends on exact anatomy; rectovaginal fistula HP:0000141 may be used as a nearest term if rectovestibular-specific is unavailable)

#### Neurodevelopmental / neurologic phenotypes
Neurodevelopmental involvement is common. In a 2023 series, **10/10 individuals who underwent neurodevelopmental evaluation** were reported to have neurodevelopmental issues. (beaman2023novelassociationof pages 6-8)

Additional neurologic features include **seizures/abnormal neurologic activity** in more severe cases. (beaman2023novelassociationof pages 1-3, beaman2023novelassociationof pages 6-8)

Suggested HPO terms:
- Global developmental delay (HP:0001263)
- Intellectual disability (HP:0001249)
- Seizures (HP:0001250)
- Autism spectrum disorder (HP:0000729) (reported as part of milder missense-associated presentations) (beaman2023novelassociationof pages 8-10)

#### Brain malformations (key recent expansion)
A major 2023 expansion is the association with **Dandy–Walker malformation**, with radiographic evidence of the **classic triad** (hypoplastic vermis, enlarged fourth ventricle, torcular elevation) in **4 affected individuals** (and in the series, 4/5 imaged individuals showed the classical triad). (beaman2023novelassociationof pages 1-3, beaman2023novelassociationof pages 5-6)

Suggested HPO terms:
- Dandy–Walker malformation (HP:0001305) (explicitly referenced) (beaman2023novelassociationof pages 3-5)
- Hydrocephalus / ventriculomegaly (HP:0000238 / HP:0002119) (beaman2023novelassociationof pages 6-8)

#### Multi-organ congenital anomalies
More severe presentations (often associated with loss-of-function CAPN15 variants) include **microcephaly**, **craniofacial anomalies**, **cardiac malformations**, and **genitourinary malformations**. (beaman2023novelassociationof pages 1-3, zucco2024abird’seye pages 9-10)

Suggested HPO terms:
- Microcephaly (HP:0000252)
- Congenital heart defect (HP:0001627)
- Abnormality of the genitourinary system (HP:0000119)

### Age of onset / progression
The phenotype is predominantly **congenital** (ocular and structural anomalies) with **early-life manifestations** of neurodevelopmental delay and possible progressive complications such as hydrocephalus requiring monitoring. (beaman2023novelassociationof pages 6-8, beaman2023novelassociationof pages 5-6)

### Quality-of-life impact
Direct quality-of-life instruments (e.g., PedsQL, PROMIS) were not reported in the retrieved sources; however, the combination of congenital ocular impairment, neurodevelopmental disability, seizures, and major congenital malformations implies substantial lifelong functional impact. (beaman2023novelassociationof pages 6-8, zucco2024abird’seye pages 9-10)

## 4. Genetic / molecular information

### Causal gene
- **CAPN15** (also referenced as CAPN15/SOLH in the 2023 report). (beaman2023novelassociationof pages 3-5, beaman2023novelassociationof pages 13-18)

### Inheritance
- **Autosomal recessive** with **biallelic pathogenic variants**, including homozygous and compound heterozygous states; heterozygous carriers may be unaffected. (beaman2023novelassociationof pages 1-3, beaman2023novelassociationof pages 13-18)

### Pathogenic variant types and genotype–phenotype correlation
A consistent theme is variant-class correlation:
- **Biallelic missense variants**: tend to be associated with **milder phenotypes**, prominently **ocular anomalies** and **developmental delay**. (beaman2023novelassociationof pages 1-3, zucco2024abird’seye pages 9-10, beaman2023novelassociationof pages 8-10)
- **Biallelic loss-of-function variants** (frameshift, exon-skipping leading to frameshift, whole-gene deletion): associated with **more severe syndromic disease**, including **microcephaly**, **craniofacial/cardiac/genitourinary anomalies**, and **abnormal neurologic activity**, and in 2023 were associated with **Dandy–Walker malformation/cerebellar pathology**. (beaman2023novelassociationof pages 1-3, beaman2023novelassociationof pages 5-6, beaman2023novelassociationof pages 8-10)

Examples of variant classes mentioned in the 2023 report include **frameshift** variants (e.g., c.2164delC; c.754dupC) and a **missense** variant **p.Leu865Pro** sometimes in trans with a **whole-gene deletion**. (beaman2023novelassociationof pages 5-6, beaman2023novelassociationof pages 3-5, beaman2023novelassociationof pages 8-10)

### Allele frequency / population databases
At least one deleterious missense variant (p.Leu865Pro) is reported as absent from **gnomAD**, supporting rarity. (beaman2023novelassociationof pages 6-8)

### Functional consequences
Evidence from patient-derived cells and protein modeling supports **loss of transcript/protein** for truncating alleles and **protein destabilization** for at least one missense allele:
- Patient fibroblast assays (RT-PCR/Western blot) showed reduced mRNA and/or loss of full-length protein depending on allele class. (beaman2023novelassociationof pages 5-6, beaman2023novelassociationof pages 13-18)
- Structural modeling (AlphaFold-based) and in silico predictions supported deleterious impact of p.Leu865Pro. (beaman2023novelassociationof pages 6-8, beaman2023novelassociationof pages 13-18)

### Protein features and current understanding
CAPN15 is described as a **non-classical calpain protease** with **N-terminal RanBP2-type zinc fingers**, a **calpain protease domain**, and a distinctive **C-terminal SOLH-like domain**; the overall biological function remains **poorly understood**, but is implicated in development. (beaman2023novelassociationof pages 1-3, beaman2023novelassociationof pages 3-5)

### Modifier genes / epigenetics / chromosomal abnormalities
No modifier genes or epigenetic signatures were identified in retrieved sources. Some cases include **copy-number variation** (whole-gene deletion) as part of the biallelic pathogenic state, detected via CNV analysis. (beaman2023novelassociationof pages 8-10)

## 5. Environmental information
No non-genetic environmental contributors, lifestyle risks, or infectious triggers were identified in retrieved sources; the condition is currently understood as a primarily genetic congenital disorder. (beaman2023novelassociationof pages 1-3, zucco2024abird’seye pages 9-10)

## 6. Mechanism / pathophysiology

### Proposed causal chain (current evidence-based model)
1. **Biallelic CAPN15 pathogenic variation** → reduced CAPN15 mRNA/protein abundance or destabilized protein (functional assays/in silico modeling). (beaman2023novelassociationof pages 5-6, beaman2023novelassociationof pages 6-8)
2. Impaired CAPN15 function during development → abnormalities in **ocular development** and **brain development**, supported by cross-species evidence.
   - Drosophila CAPN15 homolog (**Sol**) is required for **optic tract neuron maintenance**, suggesting a role in neural development/maintenance. (beaman2023novelassociationof pages 3-5)
   - Mouse data demonstrate CAPN15/SOLH expression in the cerebellum, including in **Purkinje cells**, supporting a role in cerebellar maturation and plausibly relating to Dandy–Walker spectrum malformations. (beaman2023novelassociationof pages 8-10, beaman2023novelassociationof pages 18-20)
3. Developmental disruption manifests as the clinical triad: ocular anomalies + GI/anorectal malformations + neurodevelopmental disorder, with severity depending on the degree of CAPN15 functional loss (missense vs LoF). (beaman2023novelassociationof pages 1-3, zucco2024abird’seye pages 9-10)

### Pathways and processes (evidence level: hypothesis-supporting)
The 2023 case series notes predicted binding partners implicating ubiquitin/proteasome and cell-division roles; however, direct pathway proof in human tissue is not established in the retrieved evidence. (beaman2023novelassociationof pages 8-10)

Suggested GO biological process terms (hypothesis-driven, to be validated):
- Nervous system development
- Cerebellum development
- Eye development
- Proteolysis

Suggested CL cell types:
- Purkinje cell (CL:0000121) (supported by expression in calbindin+ Purkinje-associated layers) (beaman2023novelassociationof pages 8-10)

## 7. Anatomical structures affected
Based on reported clinical and imaging features, affected systems include:
- **Eye** (UBERON:0000970) (beaman2023novelassociationof pages 6-8, zucco2024abird’seye pages 9-10)
- **Cerebellum / hindbrain** (UBERON:0002037 / UBERON:0005291) including vermis and posterior fossa structures in Dandy–Walker malformation (beaman2023novelassociationof pages 1-3, beaman2023novelassociationof pages 6-8)
- **Anorectal region / hindgut** (UBERON:0001052 or relevant hindgut/anus terms) (beaman2023novelassociationof pages 6-8)
- Possible **heart** and **kidney/genitourinary system** involvement in severe presentations (beaman2023novelassociationof pages 1-3, zucco2024abird’seye pages 9-10)

Subcellular localization/compartments were not established in retrieved sources.

## 8. Temporal development
- **Onset:** Predominantly **congenital** structural anomalies (ocular and GI/anorectal), with **infant/childhood** emergence/recognition of neurodevelopmental delay and seizures in some. (beaman2023novelassociationof pages 6-8, beaman2023novelassociationof pages 1-3)
- **Course:** Appears **chronic/lifelong**, with neurodevelopmental disability a persistent feature; complications such as ventriculomegaly/hydrocephalus may evolve and require follow-up. (beaman2023novelassociationof pages 6-8)

## 9. Inheritance and population

### Rarity and reported cases (statistics)
- A 2024 review describes the syndrome as **“ultra-rare”** and “described in **less than ten published individuals**” (context: summarizing the disorder). (zucco2024abird’seye pages 9-10)
- A 2023 case series states that **7 individuals** had been previously published and reports **6 additional** molecularly confirmed individuals (bringing the total to approximately **13 reported** by that time, assuming no overlap). (beaman2023novelassociationof pages 1-3)

### Prevalence/incidence
No prevalence or incidence estimates were found in the retrieved sources.

### Inheritance
Autosomal recessive with biallelic variants; consanguinity was present in some pedigrees. (beaman2023novelassociationof pages 5-6)

## 10. Diagnostics

### Clinical recognition
Suspicion should arise from the combination of:
- Congenital ocular malformations (e.g., microphthalmia/coloboma)
- Anorectal/GI malformations
- Neurodevelopmental impairment and/or seizures
- Brain malformation such as Dandy–Walker spectrum features on imaging
(beaman2023novelassociationof pages 6-8, beaman2023novelassociationof pages 1-3)

### Genetic testing and real-world implementation
- **Whole exome sequencing (WES)** and **rapid whole genome sequencing (WGS)** were used to establish molecular diagnoses in the 2023 series, and WES is highlighted as enabling diagnosis of OGN among rare congenital ophthalmic disorders. (beaman2023novelassociationof pages 3-5, zucco2024abird’seye pages 9-10)
- **Chromosomal microarray** may be **non-diagnostic** in some cases. (beaman2023novelassociationof pages 5-6)
- Analysis/interpretation approaches reported include phenotype-driven prioritization (Phevor), population filtering (gnomAD), in silico pathogenicity scores (e.g., CADD/REVEL), ACMG/AMP classification, and Sanger confirmation/segregation. (beaman2023novelassociationof pages 3-5)

### Imaging
Neuroimaging may show Dandy–Walker features including hypoplastic vermis, fourth ventricle enlargement, torcular elevation, posterior fossa cysts, and hydrocephalus/ventriculomegaly. (beaman2023novelassociationof pages 1-3, beaman2023novelassociationof pages 6-8)

### Differential diagnosis
No structured differential diagnosis list was available in retrieved sources; based on phenotype, overlaps likely include other syndromic microphthalmia/coloboma disorders and syndromic anorectal malformation conditions.

## 11. Outcome / prognosis
No formal survival, mortality, or life expectancy statistics were available in retrieved sources. Available evidence suggests morbidity is driven by the severity of congenital malformations, degree of visual impairment, neurodevelopmental disability, epilepsy, and possible hydrocephalus. (beaman2023novelassociationof pages 6-8, zucco2024abird’seye pages 9-10)

## 12. Treatment

### Current management (evidence limitations)
No disease-specific targeted therapies were identified in the retrieved sources. Management is therefore best described as **supportive and multidisciplinary**, tailored to organ involvement:
- Ophthalmologic management for ocular anomalies
- Surgical management of anorectal malformations
- Neurodevelopmental therapies (PT/OT/speech) and educational support
- Antiseizure treatment if epilepsy is present
- Monitoring/management of hydrocephalus and associated neurosurgical needs
(beaman2023novelassociationof pages 6-8, zucco2024abird’seye pages 9-10)

### Clinical trials
A ClinicalTrials.gov-style search for “CAPN15” or “oculogastrointestinal(-neurodevelopmental)” retrieved **no clearly relevant interventional trials** in the current tool output. (clinical trial search tool result; no citable NCTs returned)

Suggested MAXO terms (management-oriented):
- Surgical repair of anorectal malformation
- Vision care / ophthalmologic management
- Seizure management
- Developmental therapy

## 13. Prevention
Because OGN is a rare autosomal-recessive disorder, prevention is primarily genetic:
- **Carrier testing** and **genetic counseling** in affected families
- **Prenatal** or **preimplantation genetic testing** when familial pathogenic variants are known
No environmental primary prevention measures were identified.

## 14. Other species / natural disease
No naturally occurring veterinary analogs were identified in retrieved sources. However, **Drosophila** and **mouse** provide functional evidence relevant to developmental roles of CAPN15. (beaman2023novelassociationof pages 3-5, beaman2023novelassociationof pages 8-10)

## 15. Model organisms
- **Drosophila:** CAPN15 homolog (**Sol**) required for optic tract neuron maintenance; mutants show neurodegeneration/reduced brain volume, supporting neuro-ocular relevance. (beaman2023novelassociationof pages 3-5)
- **Mouse:** Capn15 knockout and expression studies support roles in brain development/plasticity; cerebellar expression is seen in postnatal development with enrichment in Purkinje-associated layers and persistence into adulthood, supporting plausibility for cerebellar malformation phenotypes in humans. (beaman2023novelassociationof pages 8-10, beaman2023novelassociationof pages 18-20)

## 2023–2024 highlights (latest research and applications)
- **Phenotype expansion and case accrual (2023):** Beaman et al. (Aug 2023; https://doi.org/10.1002/ajmg.a.63363) added **six molecularly confirmed individuals** and established an association with **Dandy–Walker malformation**, with classical triad in **4 affected individuals**, supported by mouse cerebellar expression data. (beaman2023novelassociationof pages 1-3, beaman2023novelassociationof pages 5-6)
- **Diagnostic implementation (2024):** Zucco et al. (Mar 2024; https://doi.org/10.1038/s10038-024-01237-6) emphasizes **WES** as pivotal for diagnosing rare congenital ocular dysgenesis conditions, explicitly including OGN, and summarizes that severity differs for loss-of-function vs missense CAPN15 variants. (zucco2024abird’seye pages 9-10)

## Key evidence gaps / limitations of this report
- **Identifiers** beyond OMIM (Orphanet, MONDO, MeSH, ICD) were not captured from the retrieved sources.
- **PMIDs** were not available in the tool-provided excerpts/metadata; this report therefore cites the retrieved full-text evidence context IDs and provides DOIs/URLs and publication months/years.
- Detailed **variant-by-variant frequencies**, formal **natural history**, **quality-of-life metrics**, and **treatment outcomes** were not available in the retrieved evidence.

## Key references (with publication dates and URLs)
- Beaman MM et al. *American Journal of Medical Genetics Part A* **Aug 2023**. “Novel association of Dandy–Walker malformation with CAPN15 variants expands the phenotype of oculogastrointestinal neurodevelopmental syndrome.” https://doi.org/10.1002/ajmg.a.63363 (beaman2023novelassociationof pages 1-3)
- Zucco J et al. *Journal of Human Genetics* **Mar 2024**. “A bird’s eye view on the use of whole exome sequencing in rare congenital ophthalmic diseases.” https://doi.org/10.1038/s10038-024-01237-6 (zucco2024abird’seye pages 9-10)


References

1. (beaman2023novelassociationof pages 1-3): M. Makenzie Beaman, Lucia Guidugli, Monia Hammer, Chelsea Barrows, Anne Gregor, Sangmoon Lee, Kristen L. Deak, Marie T. McDonald, Courtney Jensen, Maha S. Zaki, Amira T. Masri, Charlotte A. Hobbs, Joseph G. Gleeson, and Jennifer L. Cohen. Novel association of dandy–walker malformation with capn15 variants expands the phenotype of oculogastrointestinal neurodevelopmental syndrome. American Journal of Medical Genetics Part A, 191:2757-2767, Aug 2023. URL: https://doi.org/10.1002/ajmg.a.63363, doi:10.1002/ajmg.a.63363. This article has 18 citations.

2. (zucco2024abird’seye pages 9-10): Jessica Zucco, Federica Baldan, Lorenzo Allegri, Elisa Bregant, Nadia Passon, Alessandra Franzoni, Angela Valentina D’Elia, Flavio Faletra, Giuseppe Damante, and Catia Mio. A bird’s eye view on the use of whole exome sequencing in rare congenital ophthalmic diseases. Journal of Human Genetics, 69:271-282, Mar 2024. URL: https://doi.org/10.1038/s10038-024-01237-6, doi:10.1038/s10038-024-01237-6. This article has 9 citations and is from a peer-reviewed journal.

3. (beaman2023novelassociationof pages 3-5): M. Makenzie Beaman, Lucia Guidugli, Monia Hammer, Chelsea Barrows, Anne Gregor, Sangmoon Lee, Kristen L. Deak, Marie T. McDonald, Courtney Jensen, Maha S. Zaki, Amira T. Masri, Charlotte A. Hobbs, Joseph G. Gleeson, and Jennifer L. Cohen. Novel association of dandy–walker malformation with capn15 variants expands the phenotype of oculogastrointestinal neurodevelopmental syndrome. American Journal of Medical Genetics Part A, 191:2757-2767, Aug 2023. URL: https://doi.org/10.1002/ajmg.a.63363, doi:10.1002/ajmg.a.63363. This article has 18 citations.

4. (beaman2023novelassociationof pages 5-6): M. Makenzie Beaman, Lucia Guidugli, Monia Hammer, Chelsea Barrows, Anne Gregor, Sangmoon Lee, Kristen L. Deak, Marie T. McDonald, Courtney Jensen, Maha S. Zaki, Amira T. Masri, Charlotte A. Hobbs, Joseph G. Gleeson, and Jennifer L. Cohen. Novel association of dandy–walker malformation with capn15 variants expands the phenotype of oculogastrointestinal neurodevelopmental syndrome. American Journal of Medical Genetics Part A, 191:2757-2767, Aug 2023. URL: https://doi.org/10.1002/ajmg.a.63363, doi:10.1002/ajmg.a.63363. This article has 18 citations.

5. (beaman2023novelassociationof pages 6-8): M. Makenzie Beaman, Lucia Guidugli, Monia Hammer, Chelsea Barrows, Anne Gregor, Sangmoon Lee, Kristen L. Deak, Marie T. McDonald, Courtney Jensen, Maha S. Zaki, Amira T. Masri, Charlotte A. Hobbs, Joseph G. Gleeson, and Jennifer L. Cohen. Novel association of dandy–walker malformation with capn15 variants expands the phenotype of oculogastrointestinal neurodevelopmental syndrome. American Journal of Medical Genetics Part A, 191:2757-2767, Aug 2023. URL: https://doi.org/10.1002/ajmg.a.63363, doi:10.1002/ajmg.a.63363. This article has 18 citations.

6. (beaman2023novelassociationof pages 8-10): M. Makenzie Beaman, Lucia Guidugli, Monia Hammer, Chelsea Barrows, Anne Gregor, Sangmoon Lee, Kristen L. Deak, Marie T. McDonald, Courtney Jensen, Maha S. Zaki, Amira T. Masri, Charlotte A. Hobbs, Joseph G. Gleeson, and Jennifer L. Cohen. Novel association of dandy–walker malformation with capn15 variants expands the phenotype of oculogastrointestinal neurodevelopmental syndrome. American Journal of Medical Genetics Part A, 191:2757-2767, Aug 2023. URL: https://doi.org/10.1002/ajmg.a.63363, doi:10.1002/ajmg.a.63363. This article has 18 citations.

7. (beaman2023novelassociationof pages 13-18): M. Makenzie Beaman, Lucia Guidugli, Monia Hammer, Chelsea Barrows, Anne Gregor, Sangmoon Lee, Kristen L. Deak, Marie T. McDonald, Courtney Jensen, Maha S. Zaki, Amira T. Masri, Charlotte A. Hobbs, Joseph G. Gleeson, and Jennifer L. Cohen. Novel association of dandy–walker malformation with capn15 variants expands the phenotype of oculogastrointestinal neurodevelopmental syndrome. American Journal of Medical Genetics Part A, 191:2757-2767, Aug 2023. URL: https://doi.org/10.1002/ajmg.a.63363, doi:10.1002/ajmg.a.63363. This article has 18 citations.

8. (beaman2023novelassociationof pages 18-20): M. Makenzie Beaman, Lucia Guidugli, Monia Hammer, Chelsea Barrows, Anne Gregor, Sangmoon Lee, Kristen L. Deak, Marie T. McDonald, Courtney Jensen, Maha S. Zaki, Amira T. Masri, Charlotte A. Hobbs, Joseph G. Gleeson, and Jennifer L. Cohen. Novel association of dandy–walker malformation with capn15 variants expands the phenotype of oculogastrointestinal neurodevelopmental syndrome. American Journal of Medical Genetics Part A, 191:2757-2767, Aug 2023. URL: https://doi.org/10.1002/ajmg.a.63363, doi:10.1002/ajmg.a.63363. This article has 18 citations.