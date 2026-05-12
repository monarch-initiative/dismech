---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-12T14:33:42.181158'
end_time: '2026-05-12T14:54:12.027090'
duration_seconds: 1229.85
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Acute Lymphoblastic Leukemia
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 58
artifact_count: 1
artifacts:
- filename: artifact-00.md
  path: Acute_Lymphoblastic_Leukemia-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Acute Lymphoblastic Leukemia
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Acute Lymphoblastic Leukemia** covering all of the
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
- **Disease Name:** Acute Lymphoblastic Leukemia
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Acute Lymphoblastic Leukemia** covering all of the
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


## Acute Lymphoblastic Leukemia (ALL): Comprehensive Disease Characteristics Report (2023–2024 prioritized)

### Target Disease
- **Disease name:** Acute lymphoblastic leukemia (ALL)
- **Category:** Hematologic malignancy; acute leukemia of lymphoid precursors (B‑ or T‑lineage)
- **MONDO / MeSH / ICD / Orphanet / OMIM identifiers:** Not retrievable from the provided full-text evidence corpus; these codes should be populated from authoritative ontology/coding browsers (e.g., MONDO, MeSH, ICD-10/11, Orphanet) during knowledge-base curation. (shah2024acutelymphoblasticleukemia pages 1-2)

---

## 1. Disease Information

### 1.1 Concise overview
Acute lymphoblastic leukemia/lymphoma (ALL) is an aggressive neoplasm of **precursor B‑ or precursor T‑lymphoid cells** (B‑ALL and T‑ALL) that typically arises in the bone marrow but can involve extramedullary sites. (duffield2023internationalconsensusclassification pages 1-3, kansal2023diagnosisandmolecular pages 1-2)

**Modern classification is genetics-forward.** WHO 2022 (WHO‑HAEM5) and the International Consensus Classification (ICC) incorporate molecular/cytogenetic entities and transcriptome-defined subgroups to refine diagnosis and risk stratification. (kansal2023diagnosisandmolecular pages 5-7, duffield2023internationalconsensusclassification pages 1-3, yoon2024diagnosticandtherapeutic pages 1-2)

### 1.2 Synonyms / alternative names
- Acute lymphocytic leukemia (older/common)
- B‑lymphoblastic leukemia/lymphoma (B‑ALL/LBL)
- T‑lymphoblastic leukemia/lymphoma (T‑ALL/LBL)
- “Precursor B/T lymphoblastic leukemia/lymphoma” (older WHO terminology) (kansal2023diagnosisandmolecular pages 5-7, kansal2023diagnosisandmolecular pages 4-5)

### 1.3 Evidence provenance
The report primarily synthesizes **aggregated disease-level resources** (2024 ELN recommendations; 2024 NCCN guideline excerpt; 2023 ICC classification paper; 2024 population studies and clinical trials) plus selected **human cohort/clinical trial primary studies** (SEER analyses; prospective phase 2; JCO trial update). (gokbuget2024managementofall pages 1-2, shah2024acutelymphoblasticleukemia pages 1-2, duffield2023internationalconsensusclassification pages 1-3, liu2024epidemiologicalcharacteristicsand pages 1-3, lu2024reduceddosechemotherapyand pages 1-2, kantarjian2024resultsofthe pages 1-3)

---

## 2. Etiology

### 2.1 Disease causal factors (current understanding)
ALL is initiated and driven by **acquired genetic lesions** in lymphoid precursors (e.g., chromosomal rearrangements creating oncogenic fusions; aneuploidy; activating kinase lesions), with additional cooperating mutations and epigenetic remodeling. WHO‑HAEM5/ICC increasingly define ALL entities by such genomic features, including transcriptome-defined classes for previously “B‑other” cases. (kansal2023diagnosisandmolecular pages 5-7, duffield2023internationalconsensusclassification pages 1-3)

### 2.2 Risk factors

#### Genetic susceptibility / predisposition
A 2023 pediatric-focused review summarizes that germline susceptibility includes common loci (e.g., **ARID5B, CEBPE, BMI1, CDKN2A/2B**) and rare inherited mutations in hematopoietic genes (**ETV6, PAX5, IKZF1**). It reports **~4.4%** of children/adolescents with ALL carry pathogenic germline mutations in known cancer genes, and that **Down syndrome confers ~20‑fold increased risk**. (ekpa2023areviewof pages 2-3)

#### Environmental and demographic risk factors
- **Ionizing radiation, male sex, high birth weight** are cited as recognized/established risk factors in a 2024 SEER-based ecological analysis context. (little2024solarultravioletradiation pages 1-2)
- **Ambient solar ultraviolet radiation (UVR):** A 2024 SEER-based population study reported a statistically significant association between higher ambient UVR irradiance and childhood ALL incidence (**RR = 1.200 per mW/cm²; p = 0.004**), and a borderline trend for cumulative radiant exposure (**RR = 1.444 per MJ/cm²; p = 0.0865**), with stronger effects in ages **0–3** and among **Hispanic** children. The authors conclude the finding “is not clear-cut, and in need of replication.” (little2024solarultravioletradiation pages 1-2, little2024solarultravioletradiation pages 8-9)

**Visual evidence (RR vs UVR):** Figure showing the RR relationship used in this analysis is provided in (little2024solarultravioletradiation media 5ae23b8e).

- **Obesity (prognostic/biologic determinant in adults):** A 2024 adult cohort study found higher BMI at diagnosis was independently associated with worse overall survival (OS) (HR **10.3**, 95% CI 2.56–41.5), and was associated with higher frequency of BCR::ABL1 (Ph+) (OR **7.64**, 95% CI 1.17–49.9). (johnston2024socioeconomicdeterminantsof pages 1-2)

### 2.3 Protective factors
No specific protective genetic variants or protective exposures were directly extractable from the retrieved evidence set. The UVR literature is mixed (some prior work suggests protection with higher solar exposure, but the 2024 US SEER ecological study reported the opposite direction for ALL). (little2024solarultravioletradiation pages 8-9)

### 2.4 Gene–environment interactions
Direct GxE analyses were not present in the retrieved corpus. However, a 2023 pediatric review highlights **maternal exposures (tobacco smoke, air pollution, BMI)** being associated with neonatal DNA methylation changes, suggesting a plausible epigenetic mediation pathway for environmental effects on leukemia risk. (ekpa2023areviewof pages 2-3)

---

## 3. Phenotypes

### 3.1 Common presenting symptoms/signs (human clinical)
A 223-case pediatric clinicopathological series provides concrete presentation frequencies:
- **Pallor/anemia:** 93.3% (208/223)
- **Fever:** 89.7% (200/223)
- **Hepatomegaly:** 89.2% (199/223)
- **Splenomegaly:** 74.9% (167/223)
- **Lymphadenopathy:** 63.7% (142/223)
- **Bony tenderness/bone pain:** 50.7% (113/223)
- **Bleeding manifestations:** 35.9%
- **Joint involvement/arthritis-like:** 25.6%
- **CNS involvement at diagnosis:** ~1.3%
- **Testicular enlargement:** ~0.44% (karim2023diagnosticclueof pages 2-4)

A 2024 musculoskeletal-mimic report/review context also emphasizes that **15–30%** of ALL cases may present with isolated, persistent osteo‑articular complaints that can delay diagnosis and can be masked by corticosteroids. (talukder2024acutelymphoblasticleukemia pages 1-3, karim2023diagnosticclueof pages 5-6)

### 3.2 Laboratory abnormalities (human clinical)
From the same 223-case series:
- **Leukocytosis:** 49.4% (including WBC >50,000/µL in 24.2%; WBC >100,000/µL in 15.2%)
- **Leukopenia:** 18.8%
- **Pancytopenia at diagnosis:** 18.8%
- **Decreased age-adjusted neutrophil percentage:** 93.7% (karim2023diagnosticclueof pages 2-4, karim2023diagnosticclueof pages 1-2)

### 3.3 Suggested HPO terms (examples)
(Provide as starting points; exact mapping may be adjusted during ontology curation.)
- Fever **HP:0001945**
- Pallor **HP:0000980**
- Anemia **HP:0001903**
- Thrombocytopenia **HP:0001873**; Bleeding tendency **HP:0001892**
- Neutropenia **HP:0001875**; Leukocytosis **HP:0001974**; Leukopenia **HP:0001882**; Pancytopenia **HP:0001876**
- Hepatomegaly **HP:0002240**; Splenomegaly **HP:0001744**
- Lymphadenopathy **HP:0002716**
- Bone pain **HP:0002653**; Bone tenderness **HP:0030830**
- Arthritis/Joint pain **HP:0001369**
- CNS involvement can manifest as headache **HP:0002315**, cranial nerve palsy **HP:0001291** (clinical term selection depends on documentation). (karim2023diagnosticclueof pages 2-4)

### 3.4 Quality of life impact
While the retrieved evidence set did not include formal QoL instrument outcomes, the phenotype spectrum above implies substantial functional impact via fatigue, pain, infection risk, and bleeding risk, and treatment is associated with significant toxicity; ELN 2024 explicitly includes supportive care and late effects in its scope. (gokbuget2024managementofall pages 1-2)

---

## 4. Genetic / Molecular Information

### 4.1 Core disease genes and recurrent abnormalities (somatic)
WHO‑HAEM5/ICC classify many ALL entities by recurrent genetic lesions. Examples explicitly discussed in the retrieved evidence include:
- **BCR::ABL1 (Philadelphia chromosome) / Ph+ ALL** and BCR::ABL1‑like (“Ph‑like”) (yoon2024diagnosticandtherapeutic pages 1-2, kansal2023diagnosisandmolecular pages 5-7)
- **ETV6::RUNX1**, **TCF3::PBX1**, **KMT2A (MLL) rearrangements**, aneuploidy classes (**high hyperdiploidy**, **hypodiploidy**), and newer entities derived from genomic/transcriptome profiling previously within “B‑other”. (kansal2023diagnosisandmolecular pages 5-7, kansal2023diagnosisandmolecular pages 4-5)

The ICC 2022 framework further subdivides BCR::ABL1+ cases (lymphoid-only vs multilineage) and introduces multiple new genetic categories and provisional gene-expression-defined entities. (duffield2023internationalconsensusclassification pages 1-3)

### 4.2 Germline predisposition genes (examples)
- **ETV6, PAX5, IKZF1** (rare inherited mutations) and common susceptibility loci (e.g., **ARID5B**) are summarized in the 2023 pediatric review. (ekpa2023areviewof pages 2-3)

### 4.3 Epigenetics
The 2023 pediatric review highlights epigenome-wide associations of maternal exposures (e.g., smoking) with neonatal methylation changes (e.g., AHRR CpG cg05575921), consistent with epigenetic mediation hypotheses for leukemia risk. (ekpa2023areviewof pages 2-3)

---

## 5. Environmental Information

### 5.1 Environmental factors
- **Ionizing radiation** is cited as a recognized risk factor in recent epidemiology context. (little2024solarultravioletradiation pages 1-2)
- **Ambient UVR** is under active investigation; a large 2024 ecological analysis suggests increased childhood ALL risk with higher ambient UVR (RR effect sizes above). (little2024solarultravioletradiation pages 1-2, little2024solarultravioletradiation media 5ae23b8e)

### 5.2 Lifestyle factors
- **Obesity** emerges as a prognostic/biologic determinant of adverse OS in adults with ALL in a 2024 center cohort. (johnston2024socioeconomicdeterminantsof pages 1-2)

### 5.3 Infectious agents
Direct pathogen causation is not established for ALL in general; infection-related hypotheses (population mixing/delayed infection) are discussed as etiologic theories in pediatric literature. (ekpa2023areviewof pages 2-3, little2024solarultravioletradiation pages 11-11)

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (high-level)
1) **Initiating lesions** (chromosomal rearrangements/aneuploidy/kinase activation) occur in developing lymphoid precursors. (kansal2023diagnosisandmolecular pages 5-7, duffield2023internationalconsensusclassification pages 1-3)
2) **Differentiation arrest** and **uncontrolled proliferation** yield expanding lymphoblast clones in marrow and/or extramedullary sites. A 2024 adult review describes ALL as “marked by abnormal clones with arrested differentiation and uncontrolled proliferation in bone marrow and extramedullary sites.” (yoon2024diagnosticandtherapeutic pages 1-2)
3) **Marrow failure** causes cytopenias (anemia → pallor/fatigue; thrombocytopenia → bleeding; neutropenia → infection/fever) and may coexist with leukocytosis and circulating blasts. (karim2023diagnosticclueof pages 2-4)
4) **Tissue infiltration** produces hepatosplenomegaly, lymphadenopathy, bone pain/periosteal involvement, and less commonly CNS/testicular disease. (karim2023diagnosticclueof pages 2-4)

### 6.2 Pathway-level themes (from subtype concepts)
The retrieved WHO‑HAEM5/ICC sources emphasize that subtypes are increasingly organized around:
- **Kinase signaling activation** (e.g., BCR::ABL1 and Ph‑like lesions), affecting therapy selection (TKIs; immunotherapy-based regimens) and risk. (yoon2024diagnosticandtherapeutic pages 1-2, kantarjian2024ponatinib‐reviewofhistorical pages 10-11)
- **Transcription factor and developmental programs** identified by gene-expression clustering (ICC) that refine biologic taxonomy beyond classical cytogenetics. (duffield2023internationalconsensusclassification pages 1-3)

### 6.3 Suggested GO / CL terms (examples)
- GO biological processes: 
  - **GO:0007049** cell cycle; **GO:0008283** cell population proliferation; **GO:0006915** apoptotic process; **GO:0042127** regulation of cell population proliferation.
- CL cell types:
  - **CL:0000816** B cell; **CL:0000542** lymphocyte; **CL:0000792** T cell.
  - For leukemia blasts: “lymphoblast” is not always a CL term; practical annotation may use precursor B/T cell terms plus “neoplastic cell”.

---

## 7. Anatomical Structures Affected

### 7.1 Organ/tissue level
Primary site is the **bone marrow** with systemic hematopoietic involvement; common secondary involvement includes **liver, spleen, lymph nodes**, and **bone** (pain/tenderness). Less commonly at diagnosis: **CNS** and **testis**. (karim2023diagnosticclueof pages 2-4)

### 7.2 Suggested UBERON terms (examples)
- Bone marrow **UBERON:0002371**
- Liver **UBERON:0002107**
- Spleen **UBERON:0002106**
- Lymph node **UBERON:0000029**
- Central nervous system **UBERON:0001016**
- Testis **UBERON:0000473** (karim2023diagnosticclueof pages 2-4)

---

## 8. Temporal Development

### 8.1 Onset
ALL has a strong pediatric incidence peak but occurs across the lifespan. Median age at diagnosis in the US is **17 years**, with **53.5%** diagnosed before age 20. (shah2024acutelymphoblasticleukemia pages 1-2)

### 8.2 Progression and course
Clinically acute presentation is typical; untreated disease progresses rapidly with complications from cytopenias and infiltration. Response and relapse risk are strongly influenced by molecular subtype and depth of remission measured by MRD. (gokbuget2024managementofall pages 6-6)

---

## 9. Inheritance and Population

### 9.1 Epidemiology (recent statistics)
- **US incidence:** age-adjusted incidence **1.8 per 100,000 per year**; estimated **6,550** new cases and **1,330** deaths in 2024 (NCCN excerpt). (shah2024acutelymphoblasticleukemia pages 1-2)
- **Age distribution:** 53.5% diagnosed <20; 29.6% ≥45; 13.7% ≥65. (shah2024acutelymphoblasticleukemia pages 1-2)
- **SEER trend analysis:** From 2000–2016, childhood/adolescent ALL incidence APC **1.5%** (95% CI 1.1–1.8); adult ALL incidence APC **2.5%** (95% CI 2.0–3.1). (liu2024epidemiologicalcharacteristicsand pages 1-3)

### 9.2 Heritability/inheritance
Most ALL is sporadic (somatic). A minority reflects germline predisposition syndromes/variants (e.g., Down syndrome and inherited variants in ETV6/PAX5/IKZF1). (ekpa2023areviewof pages 2-3)

---

## 10. Diagnostics

### 10.1 Core diagnostic modalities
- **Morphology plus immunophenotyping** (flow cytometry or immunohistochemistry) to establish lymphoblastic lineage. (kansal2023diagnosisandmolecular pages 4-5)
- **Cytogenetic and molecular profiling** to assign WHO‑HAEM5/ICC genetic subtype (e.g., BCR::ABL1, aneuploidy classes, fusion-defined entities; transcriptome-defined subtypes). (kansal2023diagnosisandmolecular pages 5-7, duffield2023internationalconsensusclassification pages 1-3)

### 10.2 MRD (measurable/minimal residual disease): methods, thresholds, timing
MRD is central to prognosis and therapeutic decision-making in adult ALL.
- **Threshold commonly used:** **0.01% (10−4)**, aligned to typical assay sensitivity; ELN notes each log increase in MRD shortens time to hematologic relapse. (gokbuget2024managementofall pages 6-6)
- **Method performance:** 
  - Expert review: RQ‑PCR sensitivity ~10−5; multiparametric flow cytometry ~10−4; PCR/HTS may reach ~10−6 depending on input. (sebastian2024howitreat pages 1-2, yoon2024diagnosticandtherapeutic pages 6-8)
- **Timing:** ELN emphasizes early vs later MRD timepoints (often ~2–3 months) to guide escalation/de‑escalation. (gokbuget2024managementofall pages 6-6)

### 10.3 Guideline risk criteria examples
NCCN excerpt includes traditional high-risk features in one trial framework: age ≥35 years, time to CR >4 weeks, or high WBC (>30×10^9/L for B-lineage; >100×10^9/L for T-lineage). (shah2024acutelymphoblasticleukemia pages 3-5)

---

## 11. Outcome / Prognosis

### 11.1 Survival highlights (recent/referenced)
- Pediatric outcomes are substantially better than adult outcomes overall. A 2024 SEER-based analysis states pediatric survival is ~90% while older adult survival (55–70 years) is ~30–40% (contextual summary). (ghosh2024incidenceandsurvivability pages 1-3)
- ELN/MRD: MRD-positive status is associated with markedly higher relapse risk; one 2024 review reports 5‑year hematologic relapse 56–100% if MRD+ vs 18–33% if MRD−. (stelljes2024ph−allimmunotherapy pages 1-2)

### 11.2 Prognostic factors (examples)
- **MRD level and kinetics** are among the strongest predictors and guide allo-HCT selection. (gokbuget2024managementofall pages 6-6)
- **Age and obesity** are independent adverse predictors of OS in an adult cohort; higher BMI also associated with BCR::ABL1 positivity. (johnston2024socioeconomicdeterminantsof pages 1-2)

---

## 12. Treatment

### 12.1 Current applications and real-world implementation (2024 consensus)
The 2024 European LeukemiaNet (ELN) recommendations emphasize **risk-adapted adult ALL management** driven by baseline prognostic factors and **MRD** to determine intensity, incorporation of immunotherapies, and transplant indications. (gokbuget2024managementofall pages 1-2)

### 12.2 Key modalities, evidence, and 2024 trial statistics

| Modality/agent | Target or mechanism | Key use-case | Selected 2024 efficacy/statistics | Key toxicities / implementation notes | Key 2024 sources with URL and pub month/year |
|---|---|---|---|---|---|
| Pediatric-inspired multi-agent chemotherapy (adult AYA/fit adults); e.g., pediatric-inspired regimens, Hyper-CVAD variants | Multi-agent cytotoxic therapy targeting proliferating lymphoblasts; often includes asparaginase, vincristine, steroids, anthracycline, methotrexate/6-MP phases | Standard frontline backbone for Ph-negative ALL in younger/fit adults; adapted intensity by age/fitness | ELN 2024: pediatric-based regimens are standard up to ~45–55 years and adult Ph-negative ALL CR rates are ~90% in many groups; expert review notes ~20% 5-year OS benefit in AYA with pediatric-inspired regimens vs traditional adult regimens (gokbuget2024managementofall pages 1-2, sebastian2024howitreat pages 1-2) | Age/fitness constrained; asparaginase toxicity, infections, hepatic/pancreatic toxicity, thrombosis; obesity adversely affects OS in adults and may shape supportive-care intensity (sebastian2024howitreat pages 1-2, johnston2024socioeconomicdeterminantsof pages 1-2) | Gökbuget et al., *Blood* (May 2024) https://doi.org/10.1182/blood.2023023568 (gokbuget2024managementofall pages 1-2); Sebastian, *Clin Hematol Int* (May 2024) https://doi.org/10.46989/001c.117026 (sebastian2024howitreat pages 1-2); Johnston et al., *Blood Adv* (Dec 2024) https://doi.org/10.1182/bloodadvances.2023011862 (johnston2024socioeconomicdeterminantsof pages 1-2) |
| TKIs for Ph+ ALL (imatinib, dasatinib, ponatinib) | Inhibit BCR::ABL1 kinase signaling; ponatinib active against T315I and other resistant mutants | Frontline Ph+ ALL; often with reduced-intensity chemo or with blinatumomab; salvage/bridge contexts also used | Ponatinib review: PONALFIL post-induction CMR 47% rising to 71% in consolidation; 3-year OS 97%, EFS 70%; PhALLCON MRD-negative CR 34.4% with ponatinib vs 16.7% imatinib, and in age ≥60 years 40.0% vs 10.3%, median PFS 22.5 vs 8.3 months (kantarjian2024ponatinib‐reviewofhistorical pages 10-11) | Cardiovascular/arterial occlusive risk with ponatinib; pancreatitis reported; TKI selection depends on mutation profile, age, comorbidities, CNS strategy, transplant plan (kantarjian2024ponatinib‐reviewofhistorical pages 10-11, sebastian2024howitreat pages 5-7) | Kantarjian et al., *Am J Hematol* (May 2024) https://doi.org/10.1002/ajh.27355 (kantarjian2024ponatinib‐reviewofhistorical pages 10-11); Sebastian, *Clin Hematol Int* (May 2024) https://doi.org/10.46989/001c.117026 (sebastian2024howitreat pages 5-7) |
| Blinatumomab | CD19xCD3 bispecific T-cell engager; redirects T cells to lyse CD19+ B-ALL cells | MRD-positive B-ALL; R/R B-ALL; increasingly frontline consolidation/low-intensity induction component in Ph-negative and Ph+ disease | Frontline Ph-negative phase 2 (reduced-dose chemo → blinatumomab): CRc 94% after 2 weeks blina, MRD-negative 86%; with up to 4 weeks, CR 100% and MRD-negative 89%; 1-year OS 97.1%, PFS 82.2% (NCT05557110) (lu2024reduceddosechemotherapyand pages 1-2). Review/guideline: MRD response ~80% and hematologic relapse-free survival 61% in MRD-directed setting; survival benefit also emerging in MRD-negative frontline consolidation (stelljes2024ph−allimmunotherapy pages 1-2) | Continuous IV infusion standard; CRS and neurotoxicity/ICANS require monitoring; in Lu 2024 ICANS 14% (all grade 1), grade ≥3 CRS 9% (lu2024reduceddosechemotherapyand pages 1-2) | Lu et al., *J Hematol Oncol* (Sep 2024) https://doi.org/10.1186/s13045-024-01597-8 (lu2024reduceddosechemotherapyand pages 1-2); Stelljes, *Hematology* (Dec 2024) https://doi.org/10.1182/hematology.2024000531 (stelljes2024ph−allimmunotherapy pages 1-2); Gökbuget et al., *Blood* (May 2024) https://doi.org/10.1182/blood.2023023568 (gokbuget2024managementofall pages 1-2) |
| Inotuzumab ozogamicin | Anti-CD22 antibody-drug conjugate delivering calicheamicin | Approved for R/R CD22+ B-ALL; increasingly used in frontline low-intensity regimens in older/unfit adults; MRD eradication / bridge to HSCT / sequencing with CAR-T | 2024 reviews summarize strong efficacy in R/R disease and promising frontline combinations with low-intensity chemotherapy or blinatumomab; used to eliminate MRD and bridge to HSCT/CAR-T, but article excerpt does not provide one uniform 2024 pooled ORR/OS estimate across settings (kantarjian2024inotuzumabozogamicinin pages 15-17, gokbuget2024managementofall pages 21-22) | Key risk is veno-occlusive disease/sinusoidal obstruction syndrome, especially pre-HSCT; fractionated dosing and transplant timing matter (kantarjian2024inotuzumabozogamicinin pages 15-17) | Kantarjian et al., *Cancer* (Aug 2024) https://doi.org/10.1002/cncr.35505 (kantarjian2024inotuzumabozogamicinin pages 15-17); Gökbuget et al., *Blood* (May 2024) https://doi.org/10.1182/blood.2023023568 (gokbuget2024managementofall pages 21-22) |
| Chemo-free / near chemo-free TKI + blinatumomab for Ph+ ALL (e.g., ponatinib + blinatumomab; dasatinib + blinatumomab) | Dual targeting of BCR::ABL1 signaling plus CD19-directed T-cell cytotoxicity | Frontline Ph+ ALL; increasingly used to reduce/avoid conventional chemotherapy and sometimes HSCT | Ponatinib + blinatumomab (JCO 2024): CMR 83% overall (67% after course 1), NGS-MRD negativity 98%, only 2/60 underwent HSCT, 3-year OS 91%, EFS 77%, median follow-up 24 months (kantarjian2024resultsofthe pages 1-3, kantarjian2024resultsofthe pages 3-4). D-ALBA long-term: 4-year/approximately 53-month DFS 75.8%, OS 80.7%, early molecular responders had no events (kantarjian2024ponatinib‐reviewofhistorical pages 10-11) | CNS relapse remains an issue in chemo-free Ph+ regimens; ponatinib vascular toxicities; blinatumomab CRS/neurotoxicity; transplant role becoming more selective (kantarjian2024resultsofthe pages 3-4, kantarjian2024ponatinib‐reviewofhistorical pages 10-11) | Kantarjian et al., *J Clin Oncol* (Dec 2024) https://doi.org/10.1200/jco.24.00272 (kantarjian2024resultsofthe pages 1-3); Foà et al., *J Clin Oncol* (Mar 2024) https://doi.org/10.1200/jco.23.01075 (kantarjian2024ponatinib‐reviewofhistorical pages 10-11) |
| CAR-T cell therapy (CD19-directed; pediatric and adult B-ALL) | Autologous engineered T cells targeting CD19 on B lymphoblasts | Standard for selected R/R B-ALL; bridge or alternative to HSCT; pediatric/young adult use especially established | 2024 treatment reviews state CAR-T is standard in R/R BCP-ALL and has demonstrated major efficacy, but the provided contexts here do not include a single 2024 trial with reportable ORR/OS figures for inclusion (stelljes2024ph−allimmunotherapy pages 1-2, kantarjian2024inotuzumabozogamicinin pages 15-17) | CRS, ICANS, prolonged cytopenias, hypogammaglobulinemia; manufacturing/access/logistics and disease burden at infusion are major real-world constraints; often sequenced with blinatumomab/inotuzumab/HSCT (kantarjian2024inotuzumabozogamicinin pages 15-17, stelljes2024ph−allimmunotherapy pages 1-2) | Stelljes, *Hematology* (Dec 2024) https://doi.org/10.1182/hematology.2024000531 (stelljes2024ph−allimmunotherapy pages 1-2); Kantarjian et al., *Cancer* (Aug 2024) https://doi.org/10.1002/cncr.35505 (kantarjian2024inotuzumabozogamicinin pages 15-17) |
| Allogeneic hematopoietic cell transplantation (allo-HCT) | Graft-versus-leukemia effect after myeloablative or reduced-intensity conditioning | Consolidation for high-risk disease, persistent/recurrent MRD, poor-risk genomics, or selected R/R patients in remission | ELN/expert reviews: MRD is central to transplant selection; poor MRD response supports SCT, whereas deeper MRD responses with TKI/blinatumomab regimens are reducing HSCT use in some Ph+ patients. In ponatinib+blinatumomab 2024 study, only 2 patients underwent HSCT despite 3-year OS 91% (gokbuget2024managementofall pages 6-6, kantarjian2024resultsofthe pages 3-4, gokbuget2024managementofall pages 1-2) | Transplant-related mortality, GVHD, infection, conditioning toxicity; pre-HSCT MRD level strongly predicts relapse; post-inotuzumab VOD/SOS risk requires mitigation (gokbuget2024managementofall pages 6-6, kantarjian2024inotuzumabozogamicinin pages 15-17) | Gökbuget et al., *Blood* (May 2024) https://doi.org/10.1182/blood.2023023568 (gokbuget2024managementofall pages 6-6); Kantarjian et al., *J Clin Oncol* (Dec 2024) https://doi.org/10.1200/jco.24.00272 (kantarjian2024resultsofthe pages 3-4) |
| MRD-directed therapy / response-adapted management | Uses highly sensitive residual leukemia detection (MFC, PCR, NGS) to escalate/de-escalate therapy and determine HSCT need | Cross-cutting strategy in frontline, MRD+, pre-/post-HSCT, and salvage settings | ELN 2024: threshold commonly 0.01% (10^-4); each log MRD increase worsens relapse risk; persistent/recurrent MRD should trigger therapy change; blinatumomab is the pivotal MRD-clearing agent. Review: MFC sensitivity ~10^-5; PCR/HTS up to 10^-6; key timepoints often 6–8 and 10–12 weeks (gokbuget2024managementofall pages 6-6, yoon2024diagnosticandtherapeutic pages 6-8) | Requires experienced reference labs; assay choice affects classification; marrow regeneration can confound flow; MRD does not capture extramedullary disease; low-level MRD may be intermediate-risk and still actionable (gokbuget2024managementofall pages 6-6, yoon2024diagnosticandtherapeutic pages 6-8) | Gökbuget et al., *Blood* (May 2024) https://doi.org/10.1182/blood.2023023568 (gokbuget2024managementofall pages 6-6); Yoon & Lee, *Korean J Intern Med* (Jan 2024) https://doi.org/10.3904/kjim.2023.407 (yoon2024diagnosticandtherapeutic pages 6-8) |


*Table: This table summarizes major modern treatment modalities for acute lymphoblastic leukemia, including frontline, MRD-directed, relapsed/refractory, and transplant strategies. It highlights 2024 efficacy data, implementation considerations, and key sources for rapid evidence-based comparison.*

#### Chemo-free Ph+ ALL: ponatinib + blinatumomab (JCO 2024)
A 2024 JCO trial update reports deep molecular responses with minimal HSCT use:
- CMR by RT‑PCR **83%** overall; MRD negativity by clono‑sequencing **98%** overall; **3‑year OS 91%** and EFS **77%**; only **2** patients underwent HSCT; median follow-up **24 months**. (kantarjian2024resultsofthe pages 1-3, kantarjian2024resultsofthe pages 3-4)

**Direct abstract quote:** “At a median follow-up of 24 months, the complete molecular response rate … was 83% … and the rate of measurable residual disease negativity … was 98% … The estimated 3-year overall survival rate was 91% and event-free survival rate was 77%.” (kantarjian2024resultsofthe pages 3-4)

#### Reduced-intensity induction for Ph-negative BCP‑ALL: reduced-dose chemotherapy + blinatumomab (J Hematol Oncol 2024)
Prospective multicenter phase 2 (NCT05557110) results:
- After 2 weeks of blinatumomab: CRc **94%**, MRD-negative **86%**.
- With up to 4 weeks: CR **100%**, MRD-negative **89%**.
- 1‑year OS **97.1%**, 1‑year PFS **82.2%**; follow-up 11.5 months. (lu2024reduceddosechemotherapyand pages 1-2)

**Direct abstract quote:** “From September 2022 to December 2023, we conducted … (NCT05557110) … 33 (94%) achieved CRc … 30 (86%) achieving measurable residual disease (MRD) negativity … estimated 1-year overall survival and 1-year progression-free survival rates were 97.1% and 82.2%.” (lu2024reduceddosechemotherapyand pages 1-2)

### 12.3 MRD-directed therapy
ELN 2024 notes persistent/recurrent MRD should prompt therapy change; **blinatumomab** is highlighted as the pivotal agent tested in a major MRD trial, often converting to molecular remission; many groups use MRD to decide on allo‑HCT. (gokbuget2024managementofall pages 6-6)

### 12.4 Pharmacogenomics (implementation-relevant)
A 2024 pharmacogenetics review lists key genotype-toxicity associations:
- For **6‑mercaptopurine (6‑MP)**: TPMT (e.g., **TPMT*2 238G>C; TPMT*3B 460G>A; TPMT*3C 719A>G**), **NUDT15 c.415C>T**, and **ITPA** (94C>A; IVS2+21A>C). (graiqevciuka2024implementationofpharmacogenetics pages 5-7, graiqevciuka2024implementationofpharmacogenetics pages 1-3)
- For **methotrexate (MTX)**: **MTHFR C677T** and **A1298C** variants are discussed, though the review notes evidence for some MTX markers is inconsistent and highlights **SLCO1B1** as a more reliable MTX handling gene in cited literature. (graiqevciuka2024implementationofpharmacogenetics pages 5-7)

### 12.5 Suggested MAXO terms (examples)
- Antineoplastic chemotherapy **MAXO:0000746** (approximate; verify exact MAXO ID)
- Allogeneic hematopoietic stem cell transplantation **MAXO:0000748** (verify)
- CAR T-cell therapy **MAXO:0001097** (verify)
- Targeted therapy / tyrosine kinase inhibitor therapy (verify appropriate MAXO term)
- MRD monitoring (diagnostic procedure; may map better to OBI rather than MAXO). (gokbuget2024managementofall pages 6-6)

---

## 13. Prevention

### 13.1 Primary prevention
Because most ALL risk is not attributable to modifiable exposures, there is no established population-level primary prevention strategy. Nevertheless, risk literature motivates research into prenatal/early-life exposures and broader public health reduction of known hazards (e.g., ionizing radiation). (little2024solarultravioletradiation pages 1-2, ekpa2023areviewof pages 2-3)

### 13.2 Secondary prevention
No general population screening is established. High-risk groups (e.g., strong germline predisposition syndromes) may benefit from specialist surveillance in genetic counseling frameworks; specifics require syndrome-level guidelines (not present in retrieved corpus). (ekpa2023areviewof pages 2-3)

---

## 14. Other Species / Natural Disease
Not assessed in the retrieved evidence set.

---

## 15. Model Organisms
Not assessed in the retrieved evidence set.

---

## Recent developments and expert analysis (2023–2024)

1) **Classification shift to genomics/transcriptomics:** ICC and WHO‑HAEM5 explicitly expand genetically and expression-defined entities (including formerly “B‑other”) to improve risk stratification and treatment selection. (duffield2023internationalconsensusclassification pages 1-3, kansal2023diagnosisandmolecular pages 5-7)

2) **MRD as a decision engine:** ELN 2024 formalizes MRD timing and threshold concepts (commonly 10−4) and embeds MRD into transplant and immunotherapy decisions. (gokbuget2024managementofall pages 6-6, gokbuget2024managementofall pages 1-2)

3) **Frontline immunotherapy integration and chemotherapy de-escalation:** 2024 trials and reviews show movement of blinatumomab into upfront settings and successful chemo-free Ph+ strategies with high molecular response rates and reduced HSCT utilization. (lu2024reduceddosechemotherapyand pages 1-2, kantarjian2024resultsofthe pages 1-3, sebastian2024howitreat pages 1-2)

---

## Key figure supporting environmental-risk discussion
The relationship between UVR and ALL incidence reported in the 2024 British Journal of Cancer SEER ecological analysis is visually summarized in the retrieved figure. (little2024solarultravioletradiation media 5ae23b8e)


References

1. (shah2024acutelymphoblasticleukemia pages 1-2): Bijal Shah, Ryan J. Mattison, Ramzi Abboud, Peter Abdelmessieh, Ibrahim Aldoss, Patrick W. Burke, Daniel J. DeAngelo, Shira Dinner, Amir T. Fathi, Jordan Gauthier, Michael Haddadin, Nitin Jain, Brian Jonas, Suzanne Kirby, Michaela Liedtke, Mark Litzow, Aaron Logan, Meixiao Long, Selina Luger, James K. Mangan, Stephanie Massaro, William May, Olalekan Oluwole, Jae Park, Amanda Przespolewski, Sravanti Rangaraju, Caner Saygin, Marc Schwartz, Paul Shami, Benjamin Tomlinson, Jonathan Webster, Ajibola Awotiwon, and Katie Stehman. Acute lymphoblastic leukemia, version 2.2024, nccn clinical practice guidelines in oncology. Journal of the National Comprehensive Cancer Network : JNCCN, 22 8:563-576, Oct 2024. URL: https://doi.org/10.6004/jnccn.2024.0051, doi:10.6004/jnccn.2024.0051. This article has 75 citations.

2. (duffield2023internationalconsensusclassification pages 1-3): Amy S. Duffield, Charles G. Mullighan, and Michael J. Borowitz. International consensus classification of acute lymphoblastic leukemia/lymphoma. Virchows Archiv, 482:11-26, Nov 2023. URL: https://doi.org/10.1007/s00428-022-03448-8, doi:10.1007/s00428-022-03448-8. This article has 226 citations and is from a peer-reviewed journal.

3. (kansal2023diagnosisandmolecular pages 1-2): Rina Kansal. Diagnosis and molecular pathology of lymphoblastic leukemias and lymphomas in the era of genomics and precision medicine: historical evolution and current concepts—part 2: b-/t-cell acute lymphoblastic leukemias. Lymphatics, 1:118-154, Jul 2023. URL: https://doi.org/10.3390/lymphatics1020011, doi:10.3390/lymphatics1020011. This article has 12 citations.

4. (kansal2023diagnosisandmolecular pages 5-7): Rina Kansal. Diagnosis and molecular pathology of lymphoblastic leukemias and lymphomas in the era of genomics and precision medicine: historical evolution and current concepts—part 2: b-/t-cell acute lymphoblastic leukemias. Lymphatics, 1:118-154, Jul 2023. URL: https://doi.org/10.3390/lymphatics1020011, doi:10.3390/lymphatics1020011. This article has 12 citations.

5. (yoon2024diagnosticandtherapeutic pages 1-2): Jae-Ho Yoon and Seok Lee. Diagnostic and therapeutic advances in adults with acute lymphoblastic leukemia in the era of gene analysis and targeted immunotherapy. The Korean Journal of Internal Medicine, 39:34-56, Jan 2024. URL: https://doi.org/10.3904/kjim.2023.407, doi:10.3904/kjim.2023.407. This article has 12 citations and is from a peer-reviewed journal.

6. (kansal2023diagnosisandmolecular pages 4-5): Rina Kansal. Diagnosis and molecular pathology of lymphoblastic leukemias and lymphomas in the era of genomics and precision medicine: historical evolution and current concepts—part 2: b-/t-cell acute lymphoblastic leukemias. Lymphatics, 1:118-154, Jul 2023. URL: https://doi.org/10.3390/lymphatics1020011, doi:10.3390/lymphatics1020011. This article has 12 citations.

7. (gokbuget2024managementofall pages 1-2): Nicola Gökbuget, Nicolas Boissel, Sabina Chiaretti, Hervé Dombret, Michael Doubek, Adele Fielding, Robin Foà, Sebastian Giebel, Dieter Hoelzer, Mathilde Hunault, David I. Marks, Giovanni Martinelli, Oliver Ottmann, Anita Rijneveld, Philippe Rousselot, Josep Ribera, and Renato Bassan. Management of all in adults: 2024 eln recommendations from a european expert panel. Blood, 143:1903-1930, May 2024. URL: https://doi.org/10.1182/blood.2023023568, doi:10.1182/blood.2023023568. This article has 133 citations and is from a highest quality peer-reviewed journal.

8. (liu2024epidemiologicalcharacteristicsand pages 1-3): Shuojie Liu, Bin Hu, and Jiaqin Zhang. Epidemiological characteristics and influencing factors of acute leukemia in children and adolescents and adults: a large population-based study. Hematology, Apr 2024. URL: https://doi.org/10.1080/16078454.2024.2327916, doi:10.1080/16078454.2024.2327916. This article has 19 citations and is from a peer-reviewed journal.

9. (lu2024reduceddosechemotherapyand pages 1-2): Jing Lu, Huiying Qiu, Ying Wang, Xin Zhou, Haiping Dai, Xuzhang Lu, Xiaofei Yang, Bin Gu, Ming Hong, Miao Miao, Ruinan Lu, Jun Wang, Qian Wu, Mengxing Xue, Yun Wang, Ailing Deng, Yaoyao Shen, Yin Liu, Xueqing Dou, Yutian Lei, Depei Wu, Yu Zhu, and Suning Chen. Reduced-dose chemotherapy and blinatumomab as induction treatment for newly diagnosed ph-negative b-cell precursor acute lymphoblastic leukemia: a phase 2 trial. Journal of Hematology & Oncology, Sep 2024. URL: https://doi.org/10.1186/s13045-024-01597-8, doi:10.1186/s13045-024-01597-8. This article has 17 citations and is from a domain leading peer-reviewed journal.

10. (kantarjian2024resultsofthe pages 1-3): Hagop Kantarjian, Nicholas J. Short, Fadi G. Haddad, Nitin Jain, Xuelin Huang, Guillermo Montalban-Bravo, Rashmi Kanagal-Shamanna, Tapan M. Kadia, Naval Daver, Kelly Chien, Yesid Alvarado, Guillermo Garcia-Manero, Ghayas C. Issa, Rebecca Garris, Cedric Nasnas, Lewis Nasr, Farhad Ravandi, and Elias Jabbour. Results of the simultaneous combination of ponatinib and blinatumomab in philadelphia chromosome-positive all. Journal of Clinical Oncology, 42:4246-4251, Dec 2024. URL: https://doi.org/10.1200/jco.24.00272, doi:10.1200/jco.24.00272. This article has 80 citations and is from a highest quality peer-reviewed journal.

11. (ekpa2023areviewof pages 2-3): Queen L Ekpa, Prince C Akahara, Alexis M Anderson, Omowunmi O Adekoya, Olamide O Ajayi, Peace O Alabi, Okelue E Okobi, Oluwadamilola Jaiyeola, and Medara S Ekanem. A review of acute lymphocytic leukemia (all) in the pediatric population: evaluating current trends and changes in guidelines in the past decade. Cureus, Dec 2023. URL: https://doi.org/10.7759/cureus.49930, doi:10.7759/cureus.49930. This article has 49 citations.

12. (little2024solarultravioletradiation pages 1-2): Mark P. Little, Jim Z. Mai, Michelle Fang, Pavel Chernyavskiy, Victoria Kennerley, Elizabeth K. Cahoon, Myles G. Cockburn, Gerald M. Kendall, and Michael G. Kimlin. Solar ultraviolet radiation exposure, and incidence of childhood acute lymphocytic leukaemia and non-hodgkin lymphoma in a us population-based dataset. British Journal of Cancer, 130:1441-1452, Feb 2024. URL: https://doi.org/10.1038/s41416-024-02629-3, doi:10.1038/s41416-024-02629-3. This article has 15 citations and is from a domain leading peer-reviewed journal.

13. (little2024solarultravioletradiation pages 8-9): Mark P. Little, Jim Z. Mai, Michelle Fang, Pavel Chernyavskiy, Victoria Kennerley, Elizabeth K. Cahoon, Myles G. Cockburn, Gerald M. Kendall, and Michael G. Kimlin. Solar ultraviolet radiation exposure, and incidence of childhood acute lymphocytic leukaemia and non-hodgkin lymphoma in a us population-based dataset. British Journal of Cancer, 130:1441-1452, Feb 2024. URL: https://doi.org/10.1038/s41416-024-02629-3, doi:10.1038/s41416-024-02629-3. This article has 15 citations and is from a domain leading peer-reviewed journal.

14. (little2024solarultravioletradiation media 5ae23b8e): Mark P. Little, Jim Z. Mai, Michelle Fang, Pavel Chernyavskiy, Victoria Kennerley, Elizabeth K. Cahoon, Myles G. Cockburn, Gerald M. Kendall, and Michael G. Kimlin. Solar ultraviolet radiation exposure, and incidence of childhood acute lymphocytic leukaemia and non-hodgkin lymphoma in a us population-based dataset. British Journal of Cancer, 130:1441-1452, Feb 2024. URL: https://doi.org/10.1038/s41416-024-02629-3, doi:10.1038/s41416-024-02629-3. This article has 15 citations and is from a domain leading peer-reviewed journal.

15. (johnston2024socioeconomicdeterminantsof pages 1-2): Hannah Johnston, Hamed Rahmani Youshanlouei, Clinton Osei, Anand A. Patel, Adam DuVall, Peng Wang, Pankhuri Wanjari, Jeremy Segal, Girish Venkataraman, Jason X. Cheng, Sandeep Gurbuxani, Angela Lager, Carrie Fitzpatrick, Michael Thirman, Mariam Nawas, Hongtao Liu, Michael Drazer, Olatoyosi Odenike, Richard Larson, Wendy Stock, and Caner Saygin. Socioeconomic determinants of the biology and outcomes of acute lymphoblastic leukemia in adults. Blood Advances, 8:164-171, Dec 2024. URL: https://doi.org/10.1182/bloodadvances.2023011862, doi:10.1182/bloodadvances.2023011862. This article has 11 citations and is from a peer-reviewed journal.

16. (karim2023diagnosticclueof pages 2-4): MA Karim, N Yesmin, and M Begum. Diagnostic clue of acute lymphoblastic leukemia for frontline clinicians from clinicopathological features: study of 223 cases of in a tertiary care hospital from …. Unknown journal, 2023.

17. (talukder2024acutelymphoblasticleukemia pages 1-3): Manik Kumar Talukder, Kamrul Laila, Md. Arif Hossain, Md. Shafiqul Islam, Md. Zahidul Islam, Kalyan Benjamin Gomes, Mujammel Haque, Md. Mahbubul Islam, and Md. Imnul Islam. Acute lymphoblastic leukemia presenting as systemic juvenile idiopathic arthritis: experience from bangladesh. Open Journal of Rheumatology and Autoimmune Diseases, 14:1-12, Jan 2024. URL: https://doi.org/10.4236/ojra.2024.141001, doi:10.4236/ojra.2024.141001. This article has 1 citations.

18. (karim2023diagnosticclueof pages 5-6): MA Karim, N Yesmin, and M Begum. Diagnostic clue of acute lymphoblastic leukemia for frontline clinicians from clinicopathological features: study of 223 cases of in a tertiary care hospital from …. Unknown journal, 2023.

19. (karim2023diagnosticclueof pages 1-2): MA Karim, N Yesmin, and M Begum. Diagnostic clue of acute lymphoblastic leukemia for frontline clinicians from clinicopathological features: study of 223 cases of in a tertiary care hospital from …. Unknown journal, 2023.

20. (little2024solarultravioletradiation pages 11-11): Mark P. Little, Jim Z. Mai, Michelle Fang, Pavel Chernyavskiy, Victoria Kennerley, Elizabeth K. Cahoon, Myles G. Cockburn, Gerald M. Kendall, and Michael G. Kimlin. Solar ultraviolet radiation exposure, and incidence of childhood acute lymphocytic leukaemia and non-hodgkin lymphoma in a us population-based dataset. British Journal of Cancer, 130:1441-1452, Feb 2024. URL: https://doi.org/10.1038/s41416-024-02629-3, doi:10.1038/s41416-024-02629-3. This article has 15 citations and is from a domain leading peer-reviewed journal.

21. (kantarjian2024ponatinib‐reviewofhistorical pages 10-11): Hagop M. Kantarjian, Helen T. Chifotides, Fadi G. Haddad, Nicholas J. Short, Sanam Loghavi, and Elias Jabbour. Ponatinib‐review of historical development, current status, and future research. American Journal of Hematology, 99:1576-1585, May 2024. URL: https://doi.org/10.1002/ajh.27355, doi:10.1002/ajh.27355. This article has 25 citations and is from a domain leading peer-reviewed journal.

22. (gokbuget2024managementofall pages 6-6): Nicola Gökbuget, Nicolas Boissel, Sabina Chiaretti, Hervé Dombret, Michael Doubek, Adele Fielding, Robin Foà, Sebastian Giebel, Dieter Hoelzer, Mathilde Hunault, David I. Marks, Giovanni Martinelli, Oliver Ottmann, Anita Rijneveld, Philippe Rousselot, Josep Ribera, and Renato Bassan. Management of all in adults: 2024 eln recommendations from a european expert panel. Blood, 143:1903-1930, May 2024. URL: https://doi.org/10.1182/blood.2023023568, doi:10.1182/blood.2023023568. This article has 133 citations and is from a highest quality peer-reviewed journal.

23. (sebastian2024howitreat pages 1-2): Giebel Sebastian. How i treat newly diagnosed acute lymphoblastic leukemia. Clinical Hematology International, 6:51-61, May 2024. URL: https://doi.org/10.46989/001c.117026, doi:10.46989/001c.117026. This article has 8 citations.

24. (yoon2024diagnosticandtherapeutic pages 6-8): Jae-Ho Yoon and Seok Lee. Diagnostic and therapeutic advances in adults with acute lymphoblastic leukemia in the era of gene analysis and targeted immunotherapy. The Korean Journal of Internal Medicine, 39:34-56, Jan 2024. URL: https://doi.org/10.3904/kjim.2023.407, doi:10.3904/kjim.2023.407. This article has 12 citations and is from a peer-reviewed journal.

25. (shah2024acutelymphoblasticleukemia pages 3-5): Bijal Shah, Ryan J. Mattison, Ramzi Abboud, Peter Abdelmessieh, Ibrahim Aldoss, Patrick W. Burke, Daniel J. DeAngelo, Shira Dinner, Amir T. Fathi, Jordan Gauthier, Michael Haddadin, Nitin Jain, Brian Jonas, Suzanne Kirby, Michaela Liedtke, Mark Litzow, Aaron Logan, Meixiao Long, Selina Luger, James K. Mangan, Stephanie Massaro, William May, Olalekan Oluwole, Jae Park, Amanda Przespolewski, Sravanti Rangaraju, Caner Saygin, Marc Schwartz, Paul Shami, Benjamin Tomlinson, Jonathan Webster, Ajibola Awotiwon, and Katie Stehman. Acute lymphoblastic leukemia, version 2.2024, nccn clinical practice guidelines in oncology. Journal of the National Comprehensive Cancer Network : JNCCN, 22 8:563-576, Oct 2024. URL: https://doi.org/10.6004/jnccn.2024.0051, doi:10.6004/jnccn.2024.0051. This article has 75 citations.

26. (ghosh2024incidenceandsurvivability pages 1-3): Ishan Ghosh and Sudipto Mukherjee. Incidence and survivability of acute lymphocytic leukemia patients in the united states: analysis of seer data set from 2000-2019. Journal of Cancer Therapy, 15:141-163, Jan 2024. URL: https://doi.org/10.4236/jct.2024.154014, doi:10.4236/jct.2024.154014. This article has 0 citations.

27. (stelljes2024ph−allimmunotherapy pages 1-2): Matthias Stelljes. Ph− all: immunotherapy in upfront treatment. Hematology, 2024:86-92, Dec 2024. URL: https://doi.org/10.1182/hematology.2024000531, doi:10.1182/hematology.2024000531. This article has 1 citations and is from a peer-reviewed journal.

28. (sebastian2024howitreat pages 5-7): Giebel Sebastian. How i treat newly diagnosed acute lymphoblastic leukemia. Clinical Hematology International, 6:51-61, May 2024. URL: https://doi.org/10.46989/001c.117026, doi:10.46989/001c.117026. This article has 8 citations.

29. (kantarjian2024inotuzumabozogamicinin pages 15-17): Hagop M. Kantarjian, Nicolas Boissel, Cristina Papayannidis, Marlise R. Luskin, Matthias Stelljes, Anjali S. Advani, Elias J. Jabbour, Josep‐Maria Ribera, and David I. Marks. Inotuzumab ozogamicin in adult acute lymphoblastic leukemia: development, current status, and future directions. Cancer, 130:3631-3646, Aug 2024. URL: https://doi.org/10.1002/cncr.35505, doi:10.1002/cncr.35505. This article has 16 citations and is from a domain leading peer-reviewed journal.

30. (gokbuget2024managementofall pages 21-22): Nicola Gökbuget, Nicolas Boissel, Sabina Chiaretti, Hervé Dombret, Michael Doubek, Adele Fielding, Robin Foà, Sebastian Giebel, Dieter Hoelzer, Mathilde Hunault, David I. Marks, Giovanni Martinelli, Oliver Ottmann, Anita Rijneveld, Philippe Rousselot, Josep Ribera, and Renato Bassan. Management of all in adults: 2024 eln recommendations from a european expert panel. Blood, 143:1903-1930, May 2024. URL: https://doi.org/10.1182/blood.2023023568, doi:10.1182/blood.2023023568. This article has 133 citations and is from a highest quality peer-reviewed journal.

31. (kantarjian2024resultsofthe pages 3-4): Hagop Kantarjian, Nicholas J. Short, Fadi G. Haddad, Nitin Jain, Xuelin Huang, Guillermo Montalban-Bravo, Rashmi Kanagal-Shamanna, Tapan M. Kadia, Naval Daver, Kelly Chien, Yesid Alvarado, Guillermo Garcia-Manero, Ghayas C. Issa, Rebecca Garris, Cedric Nasnas, Lewis Nasr, Farhad Ravandi, and Elias Jabbour. Results of the simultaneous combination of ponatinib and blinatumomab in philadelphia chromosome-positive all. Journal of Clinical Oncology, 42:4246-4251, Dec 2024. URL: https://doi.org/10.1200/jco.24.00272, doi:10.1200/jco.24.00272. This article has 80 citations and is from a highest quality peer-reviewed journal.

32. (graiqevciuka2024implementationofpharmacogenetics pages 5-7): Violeta Graiqevci-Uka, Emir Behluli, Rifat Hadziselimovic, Thomas Liehr, and Gazmend Temaj. Implementation of pharmacogenetics for treatment of patients with acute lymphoblastic leukemia. Research Results in Pharmacology, 10:27-39, Jun 2024. URL: https://doi.org/10.18413/rrpharmacology.10.382, doi:10.18413/rrpharmacology.10.382. This article has 2 citations.

33. (graiqevciuka2024implementationofpharmacogenetics pages 1-3): Violeta Graiqevci-Uka, Emir Behluli, Rifat Hadziselimovic, Thomas Liehr, and Gazmend Temaj. Implementation of pharmacogenetics for treatment of patients with acute lymphoblastic leukemia. Research Results in Pharmacology, 10:27-39, Jun 2024. URL: https://doi.org/10.18413/rrpharmacology.10.382, doi:10.18413/rrpharmacology.10.382. This article has 2 citations.

## Artifacts

- [Edison artifact artifact-00](Acute_Lymphoblastic_Leukemia-deep-research-falcon_artifacts/artifact-00.md)