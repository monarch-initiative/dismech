---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-10T16:15:39.117697'
end_time: '2026-05-10T16:26:56.917849'
duration_seconds: 677.8
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Idiopathic Phalangeal Acro-osteolysis
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 21
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Idiopathic Phalangeal Acro-osteolysis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Idiopathic Phalangeal Acro-osteolysis** covering all of the
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
- **Disease Name:** Idiopathic Phalangeal Acro-osteolysis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Idiopathic Phalangeal Acro-osteolysis** covering all of the
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


## Comprehensive Disease Characteristics Report: Idiopathic Phalangeal Acro-osteolysis (IPAO)

### Executive summary
Idiopathic phalangeal acro-osteolysis (IPAO) is an *exclusion diagnosis* characterized by progressive radiographic resorption of distal phalanges (fingers and/or toes) without an identifiable secondary cause (e.g., systemic sclerosis, inflammatory arthritis, hyperparathyroidism, neuropathy, toxin exposure, trauma, infection) or a recognizable genetic/syndromic osteolysis disorder. Contemporary reviews emphasize classifying acro-osteolysis by radiographic pattern (terminal tuft vs band/midshaft) and by etiology (primary/genetic vs secondary/acquired vs idiopathic), because the *same radiographic sign* occurs across many diseases and exposures. (bailey2023acroosteolysisimagingdifferential pages 1-2, limenis2021lostbonesdifferential pages 1-2, shrestha2023idiopathicacroosteolysisa pages 2-3)

---

## 1. Disease information

### 1.1 Definition and current understanding
*Acro-osteolysis* is defined as radiographic bone resorption of the distal phalanges. (limenis2021lostbonesdifferential pages 1-2, botou2017acroosteolysis pages 1-2)

In a 2023 radiology disposition review, acro-osteolysis is defined as “osseous destruction of the distal phalanges” and categorized by pattern (terminal tuft, midshaft/band, mixed). (bailey2023acroosteolysisimagingdifferential pages 1-2)

In idiopathic forms, the osteolysis is described as a rare, heterogeneous group of disorders of unknown cause, often confined to digits and associated with nail and cutaneous changes. (todd1994idiopathicphalangealosteolysis. pages 3-4, todd1994idiopathicphalangealosteolysis. pages 1-2)

### 1.2 Key identifiers (OMIM, Orphanet, ICD-10/11, MeSH, MONDO)
**Not found in the retrieved primary/clinical sources for the idiopathic entity.** The documents retrieved that focus on idiopathic acro-osteolysis/idiopathic phalangeal osteolysis did **not** provide OMIM/Orphanet/ICD/MeSH/MONDO identifiers for IPAO. (shrestha2023idiopathicacroosteolysisa pages 2-3, bailey2023acroosteolysisimagingdifferential pages 1-2, todd1994idiopathicphalangealosteolysis. pages 3-4, gray2019nailchangesin pages 1-3)

*Note:* Retrieved sources **do** provide identifiers for *Hajdu–Cheney syndrome* (a genetic differential that includes acro-osteolysis), but this is not IPAO. (shrestha2023idiopathicacroosteolysisa pages 2-3)

### 1.3 Synonyms and alternative names (as used in literature)
Synonyms used across case reports/reviews include:
- “Idiopathic acroosteolysis” / “idiopathic acro-osteolysis” (shrestha2023idiopathicacroosteolysisa pages 2-3)
- “Idiopathic phalangeal osteolysis” (todd1994idiopathicphalangealosteolysis. pages 1-2)
- “Idiopathic non-familial acro-osteolysis” (shrestha2023idiopathicacroosteolysisa pages 2-3)
- “Adult-onset … idiopathic progressive acro-osteolysis” (tanikawa2004adultonsetidiopathicprogressive pages 1-3)

### 1.4 Evidence provenance
The IPAO evidence base in the retrieved corpus is primarily **individual patient case reports** and **review articles** aggregating heterogeneous causes of acro-osteolysis, rather than large cohorts of idiopathic disease. (bailey2023acroosteolysisimagingdifferential pages 1-2, todd1994idiopathicphalangealosteolysis. pages 3-4, shrestha2023idiopathicacroosteolysisa pages 2-3)

---

## 2. Etiology

### 2.1 Disease causal factors
For IPAO, by definition, the cause is **unknown** after evaluation. Idiopathic acro-osteolysis is described as “rare” and categorized alongside familial/genetic, occupational, and secondary forms. (shrestha2023idiopathicacroosteolysisa pages 2-3)

A 2023 radiology review emphasizes that “idiopathic” is often assigned only after an appropriate medical and imaging work-up, underscoring the exclusion-based etiology framework. (bailey2023acroosteolysisimagingdifferential pages 1-2)

### 2.2 Risk factors
**No validated risk factors specific to IPAO** were identified in the retrieved evidence. Case reports stress the *absence* of common secondary drivers (e.g., Raynaud phenomenon, psoriasis, frostbite, vinyl chloride exposure). (shrestha2023idiopathicacroosteolysisa pages 2-3, todd1994idiopathicphalangealosteolysis. pages 1-2)

For acro-osteolysis broadly (not idiopathic), reviews identify major associated conditions (systemic sclerosis, psoriatic arthritis, hyperparathyroidism, neuropathy, trauma/thermal injury, etc.) as key *etiologic contexts to exclude*. (limenis2021lostbonesdifferential pages 1-2, ahmed2025acaseof pages 10-11)

### 2.3 Protective factors
No protective factors (genetic or environmental) specific to IPAO were identified in the retrieved evidence.

### 2.4 Gene–environment interactions
No gene–environment interaction evidence specific to IPAO was identified in the retrieved evidence.

---

## 3. Phenotypes (with HPO suggestions)

### 3.1 Core phenotype: distal phalanx resorption
- **Type:** radiographic sign / skeletal manifestation
- **Description:** resorption/attenuation and shortening of distal/terminal phalanges; may involve multiple digits (hands and/or feet). (limenis2021lostbonesdifferential pages 1-2, shrestha2023idiopathicacroosteolysisa pages 2-3, todd1994idiopathicphalangealosteolysis. pages 1-2)
- **HPO suggestions:** Acro-osteolysis (HP:0006061), Short fingers (brachydactyly) (HP:0001156), Short toes (HP:0001845)

### 3.2 Nail abnormalities (frequent in idiopathic case reports)
- **Type:** physical manifestation
- **Reported findings:** generalized nail dystrophy, brachyonychia, longitudinal ridging, pterygium formation; “racket nail” / “nail en raquette”; nail atrophy. (todd1994idiopathicphalangealosteolysis. pages 3-4, tanikawa2004adultonsetidiopathicprogressive pages 1-3, gray2019nailchangesin pages 1-3)
- **Functional impact:** difficulty holding a pen (occupational limitation) in a pediatric case. (gray2019nailchangesin pages 1-3)
- **HPO suggestions:** Abnormality of the nails (HP:0001597), Nail dystrophy (HP:0001810)

### 3.3 Pain, swelling, stiffness, contractures
- **Type:** symptoms/signs
- **Reported findings:** fingertip pain and swelling; morning stiffness; reduced flexion and contractures at distal interphalangeal joints; rigid/inflexible PIP joints in an adult-onset case. (tanikawa2004adultonsetidiopathicprogressive pages 1-3, gray2019nailchangesin pages 1-3)
- **HPO suggestions:** Arthralgia (HP:0002829), Joint stiffness (HP:0001387), Flexion contracture (HP:0001371), Swelling of digits (HP:0001167)

### 3.4 Cutaneous changes (“split sign”)
A 2023 pediatric toe case report described a distinct transverse/circumferential boundary between normal proximal skin and crusted distal skin overlying osteolysis, proposed as a novel early sign (“split sign”). (shrestha2023idiopathicacroosteolysisa pages 2-3, shrestha2023idiopathicacroosteolysisa media 5f9e537a)
- **HPO suggestions:** Abnormality of the skin (HP:0000951), Hyperkeratosis (HP:0000962), Skin crusting (HP:0025115)

**Direct abstract quote supporting the sign and the diagnostic framing:** the authors state, “The clinical features, radiology findings, and a workup that helped rule out conditions associated with AO (secondary AO) helped establish the diagnosis of IAO in our patient.” (March 2023; URL: https://doi.org/10.1159/000529727) (shrestha2023idiopathicacroosteolysisa pages 2-3)

---

## 4. Genetic / molecular information

### 4.1 Causal genes
**No causal gene(s) for idiopathic phalangeal acro-osteolysis** were identified in the retrieved evidence.

A dermatology review/case series notes genetic heterogeneity of “idiopathic osteolytic disorders,” including familial autosomal dominant and autosomal recessive forms, but does not identify a specific locus and notes that prenatal diagnosis is not currently possible (as of that report). (todd1994idiopathicphalangealosteolysis. pages 3-4)

### 4.2 Pathogenic variants
No IPAO-specific pathogenic variants were identified in the retrieved evidence.

### 4.3 Key genetic differentials (important for exclusion)
The idiopathic workup in case reports explicitly considers or excludes syndromic/genetic entities (e.g., Hajdu–Cheney syndrome, Haim-Munk syndrome, lysosomal storage disorders) based on clinical features and broader evaluation. (shrestha2023idiopathicacroosteolysisa pages 2-3)

---

## 5. Environmental information
No consistent environmental trigger is established for IPAO. Case reports of idiopathic disease emphasize absent exposure histories (e.g., no vinyl chloride/PVC exposure). (shrestha2023idiopathicacroosteolysisa pages 2-3, todd1994idiopathicphalangealosteolysis. pages 1-2)

---

## 6. Mechanism / pathophysiology

### 6.1 Current mechanistic understanding (limited; largely inferential)
For idiopathic cases, mechanistic evidence is sparse and often indirect. A pediatric idiopathic case with prominent nail involvement showed dermal fibrosis on nail biopsy and absent demonstrable flow in digital arteries on Doppler despite normal radial/ulnar flow, raising a hypothesis of microvascular involvement but without serologic/clinical vasculopathy. (gray2019nailchangesin pages 1-3)

Because acro-osteolysis occurs across ischemic and neuropathic contexts, broader mechanistic hypotheses for acro-osteolysis include:
- chronic microvascular ischemia/hypoxia potentially accelerating osteoclast-mediated resorption;
- hypoxia-driven VEGF effects on osteoclast survival;
- inflammatory mediators (TNF-α) and osteoclastogenic pathways (RANKL, M-CSF);
- neuropathy with repetitive microtrauma. (ahmed2025acaseof pages 10-11)

These mechanisms are best supported for secondary acro-osteolysis and are **not proven for idiopathic disease**, but they inform diagnostic evaluation and plausibility. (ahmed2025acaseof pages 10-11)

### 6.2 Proposed ontology terms
- **GO biological process suggestions:** osteoclast differentiation (GO:0030316), bone resorption (GO:0045453), angiogenesis (GO:0001525), response to hypoxia (GO:0001666)
- **Cell type (CL) suggestions:** osteoclast (CL:0000092), osteoblast (CL:0000062), osteocyte (CL:0000132), vascular endothelial cell (CL:0000115)

---

## 7. Anatomical structures affected

### 7.1 Organ/tissue localization
Primary involvement is the **distal phalanges** of hands and/or feet; idiopathic cases may involve multiple toes and/or fingers with variable symmetry. (shrestha2023idiopathicacroosteolysisa pages 2-3, todd1994idiopathicphalangealosteolysis. pages 1-2)

- **UBERON suggestions:** distal phalanx of hand (UBERON:0004390), distal phalanx of foot (UBERON:0009400), nail (UBERON:0001709), skin of digit (UBERON:0003340)

### 7.2 Imaging localization example (idiopathic case)
Radiographs in the 2023 toe case show partial and complete resorption involving middle and terminal phalanges of multiple toes. (shrestha2023idiopathicacroosteolysisa pages 2-3, shrestha2023idiopathicacroosteolysisa media ffe12cea)

---

## 8. Temporal development

### 8.1 Onset
Onset in idiopathic cases is described as variable:
- often early childhood/adolescence/early adulthood in review discussion; (shrestha2023idiopathicacroosteolysisa pages 2-3)
- childhood presentation (10-year-old with nail dystrophy); (gray2019nailchangesin pages 1-3)
- adult-onset non-congenital case with onset of toe symptoms at age 36 and subsequent hand involvement. (tanikawa2004adultonsetidiopathicprogressive pages 1-3)

### 8.2 Progression
Idiopathic cases typically show gradual progression over years with increasing shortening/deformity, though the process may remain confined to distal phalanges without systemic disease. (todd1994idiopathicphalangealosteolysis. pages 1-2)

---

## 9. Inheritance and population

### 9.1 Epidemiology
No prevalence/incidence estimates for IPAO were identified in the retrieved evidence; the literature repeatedly describes idiopathic acro-osteolysis as **rare**. (shrestha2023idiopathicacroosteolysisa pages 2-3, tanikawa2004adultonsetidiopathicprogressive pages 1-3)

### 9.2 Inheritance
Non-familial idiopathic cases are reported, while other “primary idiopathic osteolysis” entities include familial AD and AR forms; however, causal loci are not established in the retrieved idiopathic-focused sources. (todd1994idiopathicphalangealosteolysis. pages 3-4, todd1994idiopathicphalangealosteolysis. pages 2-3)

---

## 10. Diagnostics

### 10.1 Imaging and radiographic patterns (key diagnostic concept)
Plain radiographs are repeatedly described as the **gold standard** for detecting acro-osteolysis. (limenis2021lostbonesdifferential pages 1-2, botou2017acroosteolysis pages 1-2)

A contemporary imaging review classifies patterns as:
- **terminal tuft** (distal-to-proximal tuft resorption)
- **midshaft / band** (central resorptive band with intact terminal tuft)
- **mixed** (both patterns). (Aug 2023; URL: https://doi.org/10.1007/s00256-022-04145-y) (bailey2023acroosteolysisimagingdifferential pages 1-2)

A pediatric rheumatology differential review notes that pattern can suggest etiologies: tuft pattern more often with systemic sclerosis/ischemia/hyperparathyroidism/neurologic disorders; transverse/band pattern more often with inflammatory/psoriatic arthritis. (limenis2021lostbonesdifferential pages 1-2)

### 10.2 Diagnostic principle for idiopathic disease: exclusion
Idiopathic acro-osteolysis is generally assigned as a diagnosis of exclusion after targeted medical and imaging work-up. (bailey2023acroosteolysisimagingdifferential pages 1-2, limenis2021lostbonesdifferential pages 1-2)

**Examples of exclusion workup reported in idiopathic case literature**
- Pediatric toe case (2023): normal CBC, renal/liver tests, parathyroid hormone, ANA, rheumatoid factor, anti-CCP, CRP, fasting glucose, calcium, phosphate, albumin, thyroid tests; clinical exclusion of syndromic/storage disorders. (shrestha2023idiopathicacroosteolysisa pages 2-3)
- Pediatric nail-dominant case (2019): normal inflammatory and metabolic labs with reported values (e.g., CRP 1 mg/L; ESR 5 mm/h; calcium 2.41 mmol/L; phosphate 1.54 mmol/L; PTH 1.6 pmol/L), negative autoantibodies; Doppler: normal radial/ulnar flow but absent demonstrable digital arterial flow; biopsy: dermal fibrosis without inflammation. (Dec 2019; URL: https://doi.org/10.1016/j.jdcr.2019.09.016) (gray2019nailchangesin pages 1-3)
- Adult-onset case (2004): normal inflammatory/systemic labs and normal karyotype; bone resorption markers slightly increased and improved with therapy. (Jan 2004; URL: https://doi.org/10.1359/jbmr.0301210) (tanikawa2004adultonsetidiopathicprogressive pages 1-3)

### 10.3 Differential diagnosis (must be ruled out)
Key categories summarized in recent differential-focused reviews include:
- Rheumatic/autoimmune: systemic sclerosis, psoriatic arthritis, rheumatoid arthritis
- Endocrine/metabolic: hyperparathyroidism
- Neurologic/neuropathy
- Trauma/thermal injury
- Infection (e.g., osteomyelitis)
- Genetic/syndromic osteolysis disorders (e.g., Hajdu–Cheney syndrome, lysosomal storage disorders). (limenis2021lostbonesdifferential pages 1-2, ahmed2025acaseof pages 10-11)

### 10.4 Ontology term suggestions for diagnostics
- **LOINC (suggestions):** parathyroid hormone, calcium, phosphate, CRP, ESR, ANA, RF, anti-CCP
- **RadLex (suggestions):** acro-osteolysis; distal phalanx resorption; terminal tuft resorption

---

## 11. Outcome / prognosis
No dedicated longitudinal cohort outcomes for IPAO were identified in the retrieved evidence. Case reports suggest variable progression with potential functional impairment (pain, stiffness, contractures, difficulty with fine motor tasks), but preserved overall systemic health in many idiopathic cases. (gray2019nailchangesin pages 1-3, todd1994idiopathicphalangealosteolysis. pages 1-2)

---

## 12. Treatment
No disease-specific, evidence-based pharmacotherapy exists for IPAO in the retrieved evidence.

### 12.1 Supportive and rehabilitative care (real-world implementation)
- Occupational therapy referral and multidisciplinary follow-up were used in a pediatric idiopathic case with functional difficulty. (gray2019nailchangesin pages 1-3)
  - **MAXO suggestions:** occupational therapy (MAXO:0000325), multidisciplinary care (MAXO:0000747), pain management (MAXO:0000154)

### 12.2 Anti-resorptive therapy (limited evidence)
A 2004 adult-onset idiopathic progressive acro-osteolysis case reported symptomatic improvement and normalization of resorption markers after **cyclic etidronate** (bisphosphonate) for 1.5 years, with the authors implying bisphosphonate potential in idiopathic osteolysis. (tanikawa2004adultonsetidiopathicprogressive pages 1-3)
- **MAXO suggestions:** bisphosphonate therapy (MAXO:0001520)

**Evidence gap:** Other idiopathic cases note that “No medical treatment could be offered,” indicating lack of established therapies. (gray2019nailchangesin pages 1-3)

### 12.3 Experimental/clinical trials
No IPAO-specific interventional clinical trials were identified in the retrieved clinicaltrials.gov search results (the retrieved trial was in systemic sclerosis context rather than idiopathic disease). (bailey2023acroosteolysisimagingdifferential pages 1-2)

---

## 13. Prevention
No primary prevention strategies specific to IPAO are supported by the retrieved evidence. Practical prevention in clinical care centers on **preventing misdiagnosis** and **preventing complications** via early identification and appropriate exclusion of treatable secondary causes (e.g., hyperparathyroidism, inflammatory arthritis, infection, toxin exposure). (limenis2021lostbonesdifferential pages 1-2)

---

## 14. Other species / natural disease
No naturally occurring IPAO analogs in other species were identified in the retrieved evidence.

---

## 15. Model organisms
No model organisms specific to idiopathic phalangeal acro-osteolysis were identified in the retrieved evidence.

---

## Evidence synthesis artifact
The following table summarizes naming, defining features, imaging patterns, and the exclusion-based diagnostic approach for IPAO.

| Disease naming / scope | Key synonyms in retrieved literature | Defining feature | Typical onset / course | Characteristic imaging patterns and what they suggest | How idiopathic diagnosis is established (examples) |
|---|---|---|---|---|---|
| Idiopathic phalangeal acro-osteolysis (IPAO): rare primary/idiopathic resorption confined mainly to distal phalanges/digits; generally treated as a diagnosis of exclusion rather than a well-standardized ontology entity in retrieved sources (bailey2023acroosteolysisimagingdifferential pages 1-2, todd1994idiopathicphalangealosteolysis. pages 3-4, todd1994idiopathicphalangealosteolysis. pages 2-3) | “Idiopathic acro-osteolysis,” “idiopathic phalangeal osteolysis,” “idiopathic non-familial acro-osteolysis,” “non-congenital idiopathic acro-osteolysis,” and isolated idiopathic acro-osteolysis/acro-osteolysis as an isolated idiopathic feature (tanikawa2004adultonsetidiopathicprogressive pages 1-3, todd1994idiopathicphalangealosteolysis. pages 3-4, shrestha2023idiopathicacroosteolysisa pages 2-3, todd1994idiopathicphalangealosteolysis. pages 2-3, limenis2021lostbonesdifferential pages 1-2) | Radiographic bone resorption/osteolysis of distal phalanges of fingers and/or toes, often with shortening/attenuation of terminal phalanges; may have associated nail dystrophy, digital swelling, contractures, or cutaneous changes (limenis2021lostbonesdifferential pages 1-2, todd1994idiopathicphalangealosteolysis. pages 3-4, gray2019nailchangesin pages 1-3, todd1994idiopathicphalangealosteolysis. pages 1-2) | Reported onset is variable: early childhood in classic non-familial cases, childhood in a 10-year-old case, early childhood/adolescence/early adulthood in review literature, and rare adult-onset cases; course is usually gradual/progressive over years (shrestha2023idiopathicacroosteolysisa pages 2-3, tanikawa2004adultonsetidiopathicprogressive pages 1-3, gray2019nailchangesin pages 1-3, todd1994idiopathicphalangealosteolysis. pages 1-2) | Terminal tuft/distal tuft resorption = more common pattern; often linked broadly with systemic sclerosis, ischemia, hyperparathyroidism, neurologic disorders. Band/transverse (midshaft) pattern = destruction through distal phalanx shaft, more often linked with inflammatory/psoriatic arthritis. Longitudinal resorption is also described in idiopathic cases; confluent/mixed patterns may occur in advanced disease (bailey2023acroosteolysisimagingdifferential pages 1-2, limenis2021lostbonesdifferential pages 1-2, botou2017acroosteolysis pages 1-2, shrestha2023idiopathicacroosteolysisa pages 2-3) | Diagnosis is by exclusion after targeted history, examination, imaging, and laboratory evaluation. Example exclusions in idiopathic reports: no trauma, Raynaud phenomenon, psoriasis, frostbite, vinyl chloride/PVC exposure, systemic illness, or family history; normal CBC, renal/liver tests, inflammatory markers, calcium/phosphate/PTH, thyroid tests, ANA, RF, anti-CCP; additional workup may include Doppler/vascular assessment and imaging to exclude secondary causes or syndromic disease (shrestha2023idiopathicacroosteolysisa pages 2-3, bailey2023acroosteolysisimagingdifferential pages 1-2, tanikawa2004adultonsetidiopathicprogressive pages 1-3, gray2019nailchangesin pages 1-3, todd1994idiopathicphalangealosteolysis. pages 1-2) |
| Scope boundary: important to distinguish IPAO from genetic/syndromic acro-osteolysis and secondary/acquired acro-osteolysis (shrestha2023idiopathicacroosteolysisa pages 2-3, ahmed2025acaseof pages 10-11, limenis2021lostbonesdifferential pages 1-2) | Genetic/syndromic differentials mentioned in retrieved literature include Hajdu-Cheney syndrome, Haim-Munk syndrome, lysosomal storage disorders, pycnodysostosis, hereditary multicentric carpotarsal osteolysis, and hereditary sensory/autonomic neuropathies; secondary causes include systemic sclerosis, psoriatic arthritis, rheumatoid arthritis, hyperparathyroidism, neuropathy, trauma, thermal injury, spinal dysraphism, infection, and occupational toxins (shrestha2023idiopathicacroosteolysisa pages 2-3, ahmed2025acaseof pages 10-11, gray2019nailchangesin pages 1-3) | In idiopathic cases, disease may remain largely limited to digits with otherwise normal remainder of skeleton or no obvious systemic inflammatory disease; however, some reports note associated nail or skin findings and occasional mandibular osteolysis in hand-predominant cases (todd1994idiopathicphalangealosteolysis. pages 3-4, gray2019nailchangesin pages 1-3, shrestha2023idiopathicacroosteolysisa pages 2-3, todd1994idiopathicphalangealosteolysis. pages 2-3) | Functional impact can emerge gradually: pain, swelling, stiffness, reduced flexion, difficulty holding a pen/handling objects, shortening of digits, and progressive deformity/contractures (tanikawa2004adultonsetidiopathicprogressive pages 1-3, gray2019nailchangesin pages 1-3, todd1994idiopathicphalangealosteolysis. pages 1-2) | Practical reading of patterns: plain radiographs are the gold standard; pattern recognition helps prioritize differential diagnosis but does not itself prove idiopathic disease. Idiopathic case reports have shown diffuse longitudinal resorption and partial/complete terminal phalanx loss in multiple toes/fingers (limenis2021lostbonesdifferential pages 1-2, gray2019nailchangesin pages 1-3, shrestha2023idiopathicacroosteolysisa pages 2-3) | Example workup from pediatric idiopathic case: normal CBC, renal/liver function, PTH, ANA, RF, anti-CCP, CRP, glucose, calcium, phosphate, albumin, thyroid tests; clinical exclusion of Haim-Munk/Hajdu-Cheney and storage disease features (shrestha2023idiopathicacroosteolysisa pages 2-3). Example adult case: normal urinalysis, blood counts, electrolytes, renal/liver function, CRP, ESR, RF, malignancy screen, and normal karyotype/G-banding (tanikawa2004adultonsetidiopathicprogressive pages 1-3). Example pediatric nail-dominant case: negative autoantibodies, normal ESR/CRP and mineral metabolism; Doppler showed absent demonstrable digital arterial flow despite normal larger-vessel flow (gray2019nailchangesin pages 1-3) |


*Table: This table summarizes how idiopathic phalangeal acro-osteolysis is named and scoped in the retrieved literature, along with defining features, onset/course, imaging patterns, and the exclusion-based diagnostic approach. It is useful for distinguishing idiopathic cases from syndromic and secondary acro-osteolysis.*

---

## Key recent developments (prioritizing 2023–2024)
1. **Imaging-centric diagnostic frameworks (2023):** A Skeletal Radiology review (Aug 2023) emphasizes systematic categorization by radiographic pattern (terminal tuft vs band vs mixed) and highlights that idiopathic osteolysis is often a diagnosis of exclusion after appropriate work-up. (bailey2023acroosteolysisimagingdifferential pages 1-2)
2. **New cutaneous sign proposal for idiopathic disease (2023):** The “split sign” was reported as a potential early cutaneous indicator preceding/overlying toe osteolysis in idiopathic acro-osteolysis, supported by clinical photo and radiographs. (Mar 2023; https://doi.org/10.1159/000529727) (shrestha2023idiopathicacroosteolysisa pages 2-3, shrestha2023idiopathicacroosteolysisa media 5f9e537a, shrestha2023idiopathicacroosteolysisa media ffe12cea)
3. **Quantitative differential-context statistics (2024; not idiopathic-specific):** In systemic sclerosis (a major secondary cause to exclude), a retrospective cohort reported an incidence of progressive acro-osteolysis progression of **9.8 per 100 person-years** in early disease, emphasizing why careful etiologic assignment matters when acro-osteolysis is detected. (Mar 2024; https://doi.org/10.1038/s41598-024-55877-x) (ahmed2025acaseof pages 5-10)

---

## Limitations of this report (evidence gaps)
- **Ontology identifiers (MONDO/MeSH/ICD/Orphanet/OMIM) for IPAO** were not found in the retrieved primary sources; the idiopathic entity may be inconsistently represented across disease ontologies or embedded under broader acro-osteolysis/idiopathic osteolysis categories. (todd1994idiopathicphalangealosteolysis. pages 3-4, shrestha2023idiopathicacroosteolysisa pages 2-3)
- Most mechanistic and treatment data for IPAO are from **single-case reports**; generalization is limited. (gray2019nailchangesin pages 1-3, tanikawa2004adultonsetidiopathicprogressive pages 1-3)
- No epidemiologic estimates specific to idiopathic phalangeal disease were found in the retrieved evidence.


References

1. (bailey2023acroosteolysisimagingdifferential pages 1-2): Christopher T. Bailey, Rainel Zelaya, Orest O. Kayder, and Nathan D. Cecava. Acro-osteolysis: imaging, differential diagnosis, and disposition review. Skeletal Radiology, 52:9-22, Aug 2023. URL: https://doi.org/10.1007/s00256-022-04145-y, doi:10.1007/s00256-022-04145-y. This article has 12 citations and is from a peer-reviewed journal.

2. (limenis2021lostbonesdifferential pages 1-2): Elizaveta Limenis, Jennifer Stimec, Peter Kannu, and Ronald M. Laxer. Lost bones: differential diagnosis of acro-osteolysis seen by the pediatric rheumatologist. Pediatric Rheumatology Online Journal, Jul 2021. URL: https://doi.org/10.1186/s12969-021-00596-0, doi:10.1186/s12969-021-00596-0. This article has 21 citations.

3. (shrestha2023idiopathicacroosteolysisa pages 2-3): Samir Shrestha, Bashant Regmi, Raksha Pathak, and George Kroumpouzos. Idiopathic acroosteolysis: a novel cutaneous sign can help identify the condition early. Case Reports in Dermatology, 15:51-55, Mar 2023. URL: https://doi.org/10.1159/000529727, doi:10.1159/000529727. This article has 1 citations.

4. (botou2017acroosteolysis pages 1-2): Anna Botou, Athanasios Bangeas, Ioannis Alexiou, and Lazaros I. Sakkas. Acro-osteolysis. Clinical Rheumatology, 36:9-14, Oct 2017. URL: https://doi.org/10.1007/s10067-016-3459-7, doi:10.1007/s10067-016-3459-7. This article has 50 citations and is from a peer-reviewed journal.

5. (todd1994idiopathicphalangealosteolysis. pages 3-4): Gail Todd and Norma Saxe. Idiopathic phalangeal osteolysis. Archives of dermatology, 130 6:759-62, Jun 1994. URL: https://doi.org/10.1001/archderm.1994.01690060089011, doi:10.1001/archderm.1994.01690060089011. This article has 19 citations.

6. (todd1994idiopathicphalangealosteolysis. pages 1-2): Gail Todd and Norma Saxe. Idiopathic phalangeal osteolysis. Archives of dermatology, 130 6:759-62, Jun 1994. URL: https://doi.org/10.1001/archderm.1994.01690060089011, doi:10.1001/archderm.1994.01690060089011. This article has 19 citations.

7. (gray2019nailchangesin pages 1-3): Nicola Anne Gray, Christiaan Scott, Reginald Mzudumile Ngwanya, Komala Pillay, and Thuraya Isaacs. Nail changes in acro-osteolysis: a case report and review of the literature. JAAD Case Reports, 5:1033-1036, Dec 2019. URL: https://doi.org/10.1016/j.jdcr.2019.09.016, doi:10.1016/j.jdcr.2019.09.016. This article has 7 citations.

8. (tanikawa2004adultonsetidiopathicprogressive pages 1-3): Takahisa Tanikawa, Yosuke Okada, Taeko Azuma, Ayumi Fukushima, Chie Kawahara, and Yoshiya Tanaka. Adult-onset idiopathic progressive acro-osteolysis with proximal symphalangism. Journal of Bone and Mineral Research, 19:165-167, Jan 2004. URL: https://doi.org/10.1359/jbmr.0301210, doi:10.1359/jbmr.0301210. This article has 7 citations and is from a highest quality peer-reviewed journal.

9. (ahmed2025acaseof pages 10-11): Mohamed F Ahmed, Sohaib Eladl, Ee Tienne Ong, and Portia N Mzezewa. A case of bilateral acro-osteolysis following osteomyelitis in a patient with type 2 diabetes mellitus and a literature review on acro-osteolysis. Cureus, Apr 2025. URL: https://doi.org/10.7759/cureus.83071, doi:10.7759/cureus.83071. This article has 0 citations.

10. (shrestha2023idiopathicacroosteolysisa media 5f9e537a): Samir Shrestha, Bashant Regmi, Raksha Pathak, and George Kroumpouzos. Idiopathic acroosteolysis: a novel cutaneous sign can help identify the condition early. Case Reports in Dermatology, 15:51-55, Mar 2023. URL: https://doi.org/10.1159/000529727, doi:10.1159/000529727. This article has 1 citations.

11. (shrestha2023idiopathicacroosteolysisa media ffe12cea): Samir Shrestha, Bashant Regmi, Raksha Pathak, and George Kroumpouzos. Idiopathic acroosteolysis: a novel cutaneous sign can help identify the condition early. Case Reports in Dermatology, 15:51-55, Mar 2023. URL: https://doi.org/10.1159/000529727, doi:10.1159/000529727. This article has 1 citations.

12. (todd1994idiopathicphalangealosteolysis. pages 2-3): Gail Todd and Norma Saxe. Idiopathic phalangeal osteolysis. Archives of dermatology, 130 6:759-62, Jun 1994. URL: https://doi.org/10.1001/archderm.1994.01690060089011, doi:10.1001/archderm.1994.01690060089011. This article has 19 citations.

13. (ahmed2025acaseof pages 5-10): Mohamed F Ahmed, Sohaib Eladl, Ee Tienne Ong, and Portia N Mzezewa. A case of bilateral acro-osteolysis following osteomyelitis in a patient with type 2 diabetes mellitus and a literature review on acro-osteolysis. Cureus, Apr 2025. URL: https://doi.org/10.7759/cureus.83071, doi:10.7759/cureus.83071. This article has 0 citations.