---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T21:09:45.057147'
end_time: '2026-06-17T21:23:35.828224'
duration_seconds: 830.77
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Gastroenteropancreatic Neuroendocrine Neoplasm
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 43
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 1
  edison_message_content: 1
artifacts:
- filename: artifact-00.md
  path: Gastroenteropancreatic_Neuroendocrine_Neoplasm-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: image-1.png
  path: Gastroenteropancreatic_Neuroendocrine_Neoplasm-deep-research-falcon_artifacts/image-1.png
  media_type: image/png
  source: edison_message_content
  data_storage_id: null
  description: '## Context ID: pqac-00000027 The requested tables showing the detection
    ratio (DR) for [18F]AlF-OC and [68Ga]Ga-DOTATATE are Table 3 and Table 4. Table
    3 compar'
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Gastroenteropancreatic Neuroendocrine Neoplasm
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Gastroenteropancreatic Neuroendocrine Neoplasm** covering all of the
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
- **Disease Name:** Gastroenteropancreatic Neuroendocrine Neoplasm
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Gastroenteropancreatic Neuroendocrine Neoplasm** covering all of the
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


## Comprehensive Research Report: Gastroenteropancreatic Neuroendocrine Neoplasm (GEP‑NEN)

### Target disease
- **Disease name:** Gastroenteropancreatic neuroendocrine neoplasm (GEP‑NEN)
- **Category:** Neoplasm/cancer of the gastroenteropancreatic (digestive) neuroendocrine system.
- **MONDO:** A closely aligned ontology entry supported in OpenTargets is **“digestive system neuroendocrine neoplasm” (MONDO_0024503)** (OpenTargets Search: gastroenteropancreatic neuroendocrine neoplasm,pancreatic neuroendocrine tumor,neuroendocrine carcinoma). *(A GEP‑NEN‑specific MONDO identifier was not retrieved in the available tool context.)*

---

## 1) Disease information (definitions, identifiers, synonyms)

### 1.1 What is the disease?
GEP‑NENs are **heterogeneous neoplasms arising from the diffuse neuroendocrine system** within the gastrointestinal tract and pancreas, spanning indolent well‑differentiated neuroendocrine tumors (NETs) to aggressive poorly differentiated neuroendocrine carcinomas (NECs) (pellegrino2023diagnosticmanagementof pages 1-2, castillon2023seomgetneclinicalguidelines pages 1-2).

### 1.2 Classification (current understanding)
Across major contemporary sources, digestive NENs are organized by **differentiation and proliferation**, using mitotic rate and **Ki‑67** proliferation index to grade tumors. WHO‑aligned frameworks distinguish:
- **Well‑differentiated NETs** graded **G1–G3** by Ki‑67/mitoses, and
- **Poorly differentiated NECs** (high‑grade, typically G3) (castillon2023seomgetneclinicalguidelines pages 1-2, qasim2026neuroendocrineneoplasmsof pages 2-3, qasim2026neuroendocrineneoplasmsof pages 7-8).

Quantitative Ki‑67 grading thresholds cited in recent reviews include **G1 <3%, G2 3–20%, G3 >20%** (qasim2026neuroendocrineneoplasmsof pages 7-8, tan2024gastroenteropancreaticneuroendocrineneoplasms pages 1-2).

### 1.3 Synonyms / alternative names
Commonly used equivalents in the retrieved literature include:
- “GEP‑NEN”, “gastro‑entero‑pancreatic neuroendocrine neoplasm” (pellegrino2023diagnosticmanagementof pages 1-2, castillon2023seomgetneclinicalguidelines pages 1-2)
- “GEP‑NET” (often used when focusing on well‑differentiated tumors) (peshin2025currentclinicaltrial pages 4-6, peshin2025currentclinicaltrial pages 1-3)
- “Digestive high‑grade NEN”, “NET G3”, “NEC” in high‑grade contexts (sorbye2025characteristicsandtreatment pages 1-2, elvebakken2024treatmentoutcomeaccording pages 1-2).

### 1.4 Evidence source type
Most information in this report is derived from **aggregated disease‑level resources** (clinical guidelines, registry studies, systematic reviews) plus selected **human clinical cohorts** and **prospective imaging trials** (castillon2023seomgetneclinicalguidelines pages 1-2, uhlig2024epidemiologytreatmentand pages 1-2, taherifard2024efficacyandsafety pages 1-3, boeckxstaens2023prospectivecomparisonof pages 1-2).

---

## 2) Etiology (causal factors, risk factors, protective factors)

### 2.1 Primary causal factors (genetic/mechanistic)
Most GEP‑NENs are described as **sporadic**, with a minority occurring in **hereditary cancer predisposition syndromes** (castillon2023seomgetneclinicalguidelines pages 1-2, andersen2024welldifferentiatedg1and pages 1-2).

### 2.2 Genetic risk factors / hereditary syndromes
Guideline‑level estimates indicate **~5%** of NETs are associated with hereditary syndromes such as **MEN1** (castillon2023seomgetneclinicalguidelines pages 1-2). A 2024 epidemiology review reports hereditary syndromes accounting for **~10% of NENs**, listing **MEN1, von Hippel–Lindau (VHL), and neurofibromatosis type 1 (NF1)** (tan2024gastroenteropancreaticneuroendocrineneoplasms pages 1-2). In a 2024 systematic review/meta‑analysis of well‑differentiated G1/G2 pancreatic NETs, **13.3% (30/225)** were categorized as hereditary tumors (andersen2024welldifferentiatedg1and pages 1-2).

**Somatic molecular etiologic drivers** differ by differentiation/grade and site:
- Pancreatic well‑differentiated NETs commonly harbor **MEN1, DAXX, ATRX** and **mTOR‑pathway** alterations (uhlig2024epidemiologytreatmentand pages 1-2, andersen2024welldifferentiatedg1and pages 1-2).
- Pancreatic NECs more often show **TP53** and **RB1** pathway alterations (uhlig2024epidemiologytreatmentand pages 1-2, qasim2026neuroendocrineneoplasmsof pages 7-8, castillon2023seomgetneclinicalguidelines pages 1-2).

### 2.3 Environmental risk factors, protective factors, and GxE
No robust environmental or protective factors (nor gene‑environment interactions) were retrieved in the current tool evidence. This is an evidence gap relative to the requested template.

---

## 3) Phenotypes (clinical presentation, HPO terms, QoL)

### 3.1 Functional vs nonfunctional disease
GEP‑NENs are often divided clinically into:
- **Nonfunctioning tumors**, and
- **Functioning tumors** that secrete bioactive hormones producing distinct clinical syndromes.

A radiology review states **most (60–80%) are nonfunctioning**, while **20–30%** are hormone‑secreting, citing examples such as **insulinomas, gastrinomas, glucagonomas, VIPomas, and somatostatinomas** (pellegrino2023diagnosticmanagementof pages 1-2). A separate epidemiology review reports **30–40% of pancreatic NETs are functioning** (tan2024gastroenteropancreaticneuroendocrineneoplasms pages 1-2).

### 3.2 Key symptoms / manifestations
From the imaging review: functioning syndromes include **hypoglycemia** (insulinoma), **watery diarrhea** (VIPoma), and **carcinoid syndrome manifestations** such as **watery diarrhea, flushing, bronchospasm, and right‑sided heart disease** (pellegrino2023diagnosticmanagementof pages 1-2).

### 3.3 Suggested HPO terms (examples)
*(HPO IDs were not retrieved directly via tools; suggested terms reflect standard HPO naming.)*
- Flushing → **HP:0031284 (Flushing)** *(suggested)*
- Diarrhea (including watery diarrhea) → **HP:0002014 (Diarrhea)** *(suggested)*
- Hypoglycemia → **HP:0001943 (Hypoglycemia)** *(suggested)*
- Bronchospasm/wheezing → **HP:0002094 (Wheezing)** *(suggested)*
- Carcinoid heart disease/right heart involvement → **HP:0001708 (Right ventricular hypertrophy)** *(suggested)*

### 3.4 Quality of life (QoL)
QoL endpoints were not directly retrieved in the tool evidence. Symptom burden and need for multidisciplinary care are emphasized in guideline/review contexts (pellegrino2023diagnosticmanagementof pages 1-2, castillon2023seomgetneclinicalguidelines pages 1-2).

---

## 4) Genetic / molecular information

### 4.1 Key genes and molecular features
**Well‑differentiated pancreatic NET (PanNET) mutation frequencies (G1/G2; meta‑analysis)**:
- **MEN1 altered in 42% (95/225)**
- **DAXX altered in 16% (37/225)**
- **ATRX altered in 12% (27/225)**
DAXX mutations were more frequent in tumors with MEN1 mutations (p<0.05) (andersen2024welldifferentiatedg1and pages 1-2).

**High‑grade GEP‑NEN genomic landscape (NET G3 vs NEC; cohort study)**:
High‑grade gastro‑entero‑pancreatic neoplasms had frequent alterations in **TP53 (26%)**, **APC (20%)**, **KRAS (11%)**, and **MEN1 (11%)**, with **NET G3 enriched in MEN1** and NEC enriched in TP53/APC/KRAS; histologic type and **Rb1 loss** were independent prognostic factors (elvebakken2024treatmentoutcomeaccording pages 1-2).

### 4.2 Somatic vs germline
The 2024 PanNET meta‑analysis explicitly partitions tumors into sporadic vs hereditary groups and provides hereditary syndrome gene examples (e.g., MEN1, VHL, PTEN, CDKN1B, BRCA2) (andersen2024welldifferentiatedg1and pages 1-2).

### 4.3 Epigenetic / transcriptomic / ctDNA (emerging)
A 2024 systematic review emphasizes growing interest in **liquid biopsy** modalities—CTCs, **ctDNA**, miRNA, and mRNA signatures (NETest)—for diagnosis, prognostication, monitoring, and recurrence detection, while highlighting lack of standardization and need for prospective validation (almeida2024theroleof pages 1-2).

**Suggested GO biological process terms (examples)** *(not tool‑retrieved; ontology suggestions)*:
- Neuroendocrine cell differentiation → **GO:0048666 (neuron development)** *(suggested proxy)*
- Cell proliferation → **GO:0008283 (cell population proliferation)** *(suggested)*
- mTOR signaling → **GO:0031929 (TOR signaling)** *(suggested)*

---

## 5) Environmental information
No specific toxins, lifestyle factors, or infectious causes were retrieved in the current evidence set. (Evidence gap.)

---

## 6) Mechanism / pathophysiology

### 6.1 Differentiation‑linked biology and clinical behavior
A central mechanistic concept is that **differentiation and proliferative index (Ki‑67)** correlate strongly with behavior and prognosis, with well‑differentiated G1/G2 generally more indolent than high‑grade G3 and NEC (pellegrino2023diagnosticmanagementof pages 1-2, castillon2023seomgetneclinicalguidelines pages 1-2, sorbye2025characteristicsandtreatment pages 1-2).

### 6.2 High‑grade disease mechanisms (TP53/RB1 axis)
High‑grade digestive NENs show clinically and molecularly distinct categories (NET G3 vs NEC), with outcomes and treatment responses differing by subtype and biomarkers such as Ki‑67 and tumor suppressor alterations (sorbye2025characteristicsandtreatment pages 1-2, elvebakken2024treatmentoutcomeaccording pages 1-2).

---

## 7) Anatomical structures affected

### 7.1 Primary sites and metastasis
GEP‑NENs arise in **gastrointestinal tract** and **pancreas**; a 2024 review notes that at diagnosis **>50% have lymph node metastases**, and the **liver** is the predominant metastatic site (**82%**) (tan2024gastroenteropancreaticneuroendocrineneoplasms pages 1-2).

**Suggested UBERON terms (examples)** *(suggested; not tool‑retrieved)*:
- Pancreas → **UBERON:0001264** *(suggested)*
- Small intestine → **UBERON:0002108** *(suggested)*
- Liver (metastasis) → **UBERON:0002107** *(suggested)*

---

## 8) Temporal development (onset and progression)
Median age at diagnosis is approximately **~60 years** in guideline summaries (castillon2023seomgetneclinicalguidelines pages 1-2). High‑grade digestive NENs can show rapid progression with poor survival in advanced disease compared with NET G3 (sorbye2025characteristicsandtreatment pages 1-2).

---

## 9) Inheritance and population

### 9.1 Epidemiology (incidence/prevalence)
- Guideline incidence estimate for GEP‑NEN: **3.56 per 100,000**; prevalence increased from **0.006% (1993)** to **0.048% (2012)** (castillon2023seomgetneclinicalguidelines pages 1-2).
- U.S. NCDB analysis: **86,324** GEP‑NEN patients; annual cases increased from **4,010 (2004)** to **9,379 (2016)**, driven largely by low‑stage/low‑grade disease (uhlig2024epidemiologytreatmentand pages 1-2).
- A 2024 review cites a **6.4‑fold rise** in U.S. NEN incidence from 1973–2012 (tan2024gastroenteropancreaticneuroendocrineneoplasms pages 1-2).

### 9.2 Heritability
Hereditary syndromes contribute a minority of cases (see §2), with pooled hereditary classification **13.3%** in one PanNET sequencing meta‑analysis dataset (andersen2024welldifferentiatedg1and pages 1-2).

---

## 10) Diagnostics

### 10.1 Pathology and immunohistochemistry (IHC)
Minimum recommended confirmation of neuroendocrine phenotype includes **synaptophysin** and **chromogranin A** immunostaining (castillon2023seomgetneclinicalguidelines pages 1-2). **INSM1** is highlighted as a promising sensitive/specific nuclear marker (castillon2023seomgetneclinicalguidelines pages 1-2).

Ki‑67 grading: reviews cite **G1 <3%, G2 3–20%, G3 >20%** and note technical requirements such as counting **500–2,000 tumor cells** in “hot spot” areas (qasim2026neuroendocrineneoplasmsof pages 7-8, tan2024gastroenteropancreaticneuroendocrineneoplasms pages 1-2).

### 10.2 Imaging (real‑world implementation)
A 2023 imaging review describes a combined approach using:
- **Morphologic imaging**: contrast‑enhanced CT (ENETS‑aligned) and contrast‑enhanced MRI with DWI for liver/pancreas/bone assessment (pellegrino2023diagnosticmanagementof pages 1-2).
- **Functional imaging**: FDG PET‑CT for more aggressive/nonfunctioning lesions and **somatostatin receptor (SSTR) PET** for receptor‑expressing disease; identifying heterogeneity in SSTR expression is clinically important for therapy planning (pellegrino2023diagnosticmanagementof pages 1-2).

### 10.3 Recent development (2023–2024): next‑generation SSTR PET tracer
A prospective comparison study reported improved lesion detection using **[^18F]AlF‑NOTA‑octreotide (18F‑AlF‑OC)** versus **[^68Ga]Ga‑DOTATATE**. Key abstract‑level metrics include:
- “**195 unique lesions** were detected: **167 with [^68Ga]Ga‑DOTATATE and 193 with [^18F]AlF‑OC**.”
- “The **DR for [^18F]AlF‑OC was 99.1% versus 91.4% for [^68Ga]Ga‑DOTATATE**…”
- “…of **33** incremental lesions… **91% were confirmed by MRI**…”
Trial registration: **ClinicalTrials.gov NCT04552847** (registered 17 Sep 2020) (boeckxstaens2023prospectivecomparisonof pages 1-2). Tables with DR comparisons are visible in the extracted images (boeckxstaens2023prospectivecomparisonof media b98f7885, boeckxstaens2023prospectivecomparisonof media be4d67f8, boeckxstaens2023prospectivecomparisonof media 4b687989).

---

## 11) Outcomes / prognosis

### 11.1 Stage‑based survival
Guideline‑level 5‑year overall survival (OS) estimates vary strongly by stage:
- **Localized:** **83–97%**
- **Regional:** **67–84%**
- **Metastatic:** **28–50%**
For NEC, 5‑year OS is substantially worse (e.g., metastatic around **10%**) (castillon2023seomgetneclinicalguidelines pages 1-2).

### 11.2 Prognosis in advanced high‑grade disease (recent registry)
The prospective NORDIC NEC 2 cohort reported for advanced digestive high‑grade NENs:
- Immediate progression: **41% (NEC)** vs **24% (NET G3)**
- Median PFS: **3.4 months (NEC)** vs **7.4 months (NET G3)**
- Median OS: **7.4 months (NEC)** vs **21.8 months (NET G3)**
and identified adverse prognostic factors including **Ki‑67 >55%** and performance status (sorbye2025characteristicsandtreatment pages 1-2).

---

## 12) Treatment (standard of care + recent developments)

### 12.1 Core treatment modalities in current practice
An NCDB analysis found most patients received surgery: **72.9%** surgery alone and **4.9%** surgery plus systemic therapy; surgical resection was associated with the longest OS in that dataset (uhlig2024epidemiologytreatmentand pages 1-2).

Systemic and locoregional modalities referenced across guideline/review evidence include: surgery, liver‑directed therapy, somatostatin analogues (SSAs), PRRT, cytotoxic chemotherapy, and targeted therapies (castillon2023seomgetneclinicalguidelines pages 1-2).

### 12.2 Somatostatin analogues (SSAs)
SSAs are used as antiproliferative therapy in well‑differentiated, SSTR‑expressing disease; PROMID and CLARINET trial metrics are summarized in recent evidence syntheses (peshin2025currentclinicaltrial pages 4-6, hernandezfelix2025emergingdiagnosticsand pages 5-6).

### 12.3 PRRT (177Lu‑DOTATATE) and theranostics
PRRT is a key real‑world implementation for SSTR‑positive GEP‑NETs, supported by trials summarized in recent critical reviews (hernandezfelix2025emergingdiagnosticsand pages 5-6). The same body of evidence emphasizes that modern SSTR‑PET imaging has become central for selecting candidates for PRRT and other SSTR‑targeted approaches (pellegrino2023diagnosticmanagementof pages 1-2, hernandezfelix2025emergingdiagnosticsand pages 5-6).

### 12.4 Targeted therapies (everolimus, sunitinib) and sequencing
Recent evidence syntheses summarize PFS benefit from mTOR inhibition and TKIs in NET populations, and emphasize that therapy sequencing is increasingly individualized (hernandezfelix2025emergingdiagnosticsand pages 5-6, peshin2025currentclinicaltrial pages 4-6).

### 12.5 Alkylator chemotherapy (temozolomide; CAPTEM)
A 2024 systematic review/meta‑analysis of temozolomide‑based regimens in advanced pancreatic NETs pooled **14 studies (441 patients)** and reported:
- ORR **41.2%** (95% CI 32.4–50.6)
- DCR **85.3%** (95% CI 74.9–91.9)
- ≥50% chromogranin A decrease **44.9%**
- Serious adverse events **23.7%**
(registered PROSPERO **CRD42023409280**) (taherifard2024efficacyandsafety pages 1-3).

### 12.6 High‑grade NEC chemotherapy and biomarkers
For digestive high‑grade NEN treated with platinum/etoposide, a 2024 BJC study found **TP53 mutation predicted inferior response rate** in multivariate analysis (p=0.009), and observed additional subtype‑specific associations (e.g., RB1 deletions in small‑cell NEC) (elvebakken2024treatmentoutcomeaccording pages 1-2).

### 12.7 Recent development: Cabozantinib phase III (CABINET)
A major recent development is the CABINET phase 3 trial of **cabozantinib** in previously treated progressive NETs:
- Extra‑pancreatic NET: median PFS **8.4 vs 3.9 months** (HR 0.38; p<0.001)
- Pancreatic NET: median PFS **13.8 vs 4.4 months** (HR 0.23; p<0.001)
- Confirmed ORR: **5% (epNET)** and **19% (pNET)** vs **0%** with placebo
- Grade ≥3 adverse events: **62–65%** with cabozantinib vs **23–27%** with placebo
(published Feb 2025; URL in citation) (chan2025phase3trial pages 1-3).

**Suggested MAXO terms (examples; suggested)**
- Surgical resection → **MAXO:0000004 (surgery)** *(suggested)*
- Somatostatin analogue therapy → **MAXO:0000037 (pharmacotherapy)** *(suggested)*
- PRRT → **MAXO:0000533 (radiotherapy)** *(suggested)*
- Tyrosine kinase inhibitor therapy → **MAXO:0000037 (pharmacotherapy)** *(suggested)*
- Chemotherapy (CAPTEM; platinum‑etoposide) → **MAXO:0000037 (pharmacotherapy)** *(suggested)*

---

## 13) Prevention
No primary prevention strategies or population screening programs were retrieved in the available evidence. Secondary prevention in practice mainly reflects improved detection via modern imaging/endoscopy (uhlig2024epidemiologytreatmentand pages 1-2, pellegrino2023diagnosticmanagementof pages 1-2).

---

## 14) Other species / natural disease
Not retrieved in current evidence.

---

## 15) Model organisms
Not sufficiently retrieved in current evidence. *(Although preclinical model work exists, including genetically engineered mouse models of PanNET, it was not gathered into citeable context in this run.)*

---

## Expert opinion and analysis (synthesis from authoritative sources)
Recent guideline and high‑impact trial evidence supports several converging expert‑level themes:
1) **Classification matters clinically**: NET G3 and NEC differ in molecular profile and prognosis, requiring nuanced pathology with Ki‑67, morphology, and marker patterns (castillon2023seomgetneclinicalguidelines pages 1-2, sorbye2025characteristicsandtreatment pages 1-2, elvebakken2024treatmentoutcomeaccording pages 1-2).
2) **Theranostics is central to real‑world implementation**: SSTR expression assessment with modern PET is pivotal for treatment planning (SSA/PRRT), and newer tracers such as **18F‑AlF‑OC** may improve lesion detection and logistics over 68Ga agents (pellegrino2023diagnosticmanagementof pages 1-2, boeckxstaens2023prospectivecomparisonof pages 1-2, boeckxstaens2023prospectivecomparisonof media b98f7885).
3) **Therapy options are expanding in 2023–2025**: systematic review evidence supports CAPTEM/temozolomide efficacy in pNET, and CABINET provides phase III evidence for cabozantinib in progressive NETs (taherifard2024efficacyandsafety pages 1-3, chan2025phase3trial pages 1-3).
4) **Liquid biopsy is promising but not standardized**: ctDNA and transcriptomic assays (e.g., NETest) show potential for diagnosis/monitoring, especially in higher grade disease, but require prospective validation and harmonization before routine adoption (almeida2024theroleof pages 1-2).

---

## Structured summary table
| Domain | Key knowledge-base facts |
|---|---|
| Definition / classification | Digestive-system NENs are classified into well-differentiated NET and poorly differentiated NEC; WHO/consensus grading uses Ki-67 and mitotic count. NET grades: G1 **<3%**, G2 **3–20%**, G3 **>20%**; NECs are biologically high-grade and typically G3. WHO 2022/current framework also recognizes MiNEN and separates **NET G3** from NEC (qasim2026neuroendocrineneoplasmsof pages 2-3, qasim2026neuroendocrineneoplasmsof pages 7-8, castillon2023seomgetneclinicalguidelines pages 1-2, tan2024gastroenteropancreaticneuroendocrineneoplasms pages 1-2) |
| Epidemiology | GEP-NEN incidence reported at **3.56/100,000**; prevalence increased from **0.006% (1993)** to **0.048% (2012)**. In NCDB, annual GEP-NEN cases increased from **4,010 to 9,379 (2004–2016)**; **86,324** patients represented **6.33%** of all GEP malignancies. U.S. SEER data cited a **6.4-fold** rise in NEN incidence from 1973–2012 (castillon2023seomgetneclinicalguidelines pages 1-2, uhlig2024epidemiologytreatmentand pages 1-2, tan2024gastroenteropancreaticneuroendocrineneoplasms pages 1-2) |
| Hereditary syndromes / risk | About **~5%** of NETs are associated with hereditary syndromes in guideline summaries; broader reviews estimate hereditary syndromes in **~5–10%** of PanNETs / **~10%** of NENs overall. Key syndromes: **MEN1, VHL, NF1**; pooled sequencing of G1/G2 PanNETs found **13.3% hereditary** tumors (30/225) (castillon2023seomgetneclinicalguidelines pages 1-2, tan2024gastroenteropancreaticneuroendocrineneoplasms pages 1-2, andersen2024welldifferentiatedg1and pages 1-2) |
| Key molecular alterations | In pooled G1/G2 PanNET sequencing, **MEN1 42% (95/225)**, **DAXX 16% (37/225)**, **ATRX 12% (27/225)**; nonfunctioning PanNETs showed recurrent PI3K/Wnt/NOTCH/RTK-Ras pathway alterations. High-grade GEP-NENs: **TP53 26%**, **APC 20%**, **KRAS 11%**, **MEN1 11%**; NET G3 enriched for **MEN1**, NEC enriched for **TP53/APC/KRAS**; Rb1 loss independently prognostic. Pancreatic WDNETs commonly harbor **DAXX/ATRX, MEN1, mTOR-pathway** alterations, whereas pancreatic NECs show **RB1, TP53, CDKN2A** changes (andersen2024welldifferentiatedg1and pages 1-2, uhlig2024epidemiologytreatmentand pages 1-2, qasim2026neuroendocrineneoplasmsof pages 7-8, elvebakken2024treatmentoutcomeaccording pages 1-2) |
| Core diagnostics | Histopathology should demonstrate neuroendocrine phenotype with at minimum **synaptophysin** and **chromogranin A**; **INSM1** is highlighted as a sensitive/specific nuclear marker. Site-of-origin IHC may include **CDX2** (intestinal), **Islet-1/PAX6** (pancreas), **TTF-1** (lung). Ki-67 grading cutoffs: **<3%, 3–20%, >20%**; WHO 2022 guidance recommends counting **500–2,000** cells in hotspot areas (castillon2023seomgetneclinicalguidelines pages 1-2, qasim2026neuroendocrineneoplasmsof pages 7-8, tan2024gastroenteropancreaticneuroendocrineneoplasms pages 1-2) |
| Imaging | Morphologic workup: contrast-enhanced **CT** recommended; contrast-enhanced **MRI with DWI** used for liver/pancreas/brain/bone. Functional imaging: **SSTR PET** for receptor-positive disease and **FDG PET-CT** for more aggressive/nonfunctioning lesions; heterogeneity of SSTR expression helps treatment selection. In prospective comparison of **18F-AlF-NOTA-octreotide vs 68Ga-DOTATATE**, unique lesions **193 vs 167**, detection ratio **99.1% vs 91.4%**, and **33** incremental 18F lesions with **91%** MRI confirmation; trial **NCT04552847** (pellegrino2023diagnosticmanagementof pages 1-2, boeckxstaens2023prospectivecomparisonof pages 1-2, boeckxstaens2023prospectivecomparisonof pages 8-9) |
| Prognosis | Five-year OS by stage for GEP-NENs: localized **83–97%**, regional **67–84%**, metastatic **28–50%**; for NECs, localized **25–60%**, regional **9.2–28.5%**, metastatic about **10%**. In NORDIC NEC 2 high-grade digestive NENs, first-line palliative therapy showed immediate progression **41% NEC vs 24% NET G3**, median PFS **3.4 vs 7.4 mo**, OS **7.4 vs 21.8 mo**; adverse prognostic factors included **Ki-67 >55%**, PS, ALP, age (castillon2023seomgetneclinicalguidelines pages 1-2, sorbye2025characteristicsandtreatment pages 1-2) |
| Treatments | Surgery remains main curative option; most NCDB patients underwent surgery (**72.9%** alone). SSAs: PROMID TTP **14.3 vs 6 mo**; CLARINET median PFS **NR/32.8 vs 18 mo**. PRRT: NETTER-1 median PFS **NR vs 8.4 mo**, ORR **18% vs 3%**; NETTER-2 PFS **22.8 vs 8.5 mo**. Everolimus: RADIANT-3 PFS **11.0 vs 4.6 mo**; sunitinib: **11.4 vs 5.5 mo**. Temozolomide-based therapy meta-analysis: ORR **41.2%**, DCR **85.3%**. Platinum-etoposide remains first-line backbone for NEC, but immediate progression can be **~30–41%**. CABINET phase 3: cabozantinib improved PFS in epNET **8.4 vs 3.9 mo (HR 0.38)** and pNET **13.8 vs 4.4 mo (HR 0.23)**; ORR **5% epNET / 19% pNET** (uhlig2024epidemiologytreatmentand pages 1-2, hernandezfelix2025emergingdiagnosticsand pages 5-6, taherifard2024efficacyandsafety pages 1-3, elvebakken2024treatmentoutcomeaccording pages 1-2, chan2025phase3trial pages 1-3) |
| Liquid biopsy | Liquid biopsy review analyzed **65** articles. **ctDNA** appears more informative in **high-grade** tumors; **CTCs** are limited by low shedding. **NETest**/other mRNA-miRNA assays are described as having high sensitivity/specificity and may outperform chromogranin A; one review cites about **~91%** diagnostic accuracy for NETest, but standardization and prospective validation remain limiting (almeida2024theroleof pages 1-2, peshin2025currentclinicaltrial pages 4-6) |


*Table: This table condenses high-yield disease characteristics, diagnostics, molecular features, prognosis, and treatment outcomes for gastroenteropancreatic neuroendocrine neoplasms. It is designed for rapid knowledge-base population using evidence-backed quantitative facts and context citations.*

---

## Key sources (URLs and publication dates as retrieved)
- SEOM‑GETNE guideline for diagnosis/treatment of GEP and bronchial NENs. **May 2023**. https://doi.org/10.1007/s12094-023-03205-6 (castillon2023seomgetneclinicalguidelines pages 1-2)
- Diagnostic imaging review for GEP‑NENs. **Jan 2023**. https://doi.org/10.3390/tomography9010018 (pellegrino2023diagnosticmanagementof pages 1-2)
- NCDB epidemiology/treatment/outcomes of GEP‑NENs. **Dec 2024**. https://doi.org/10.1038/s41598-024-81518-4 (uhlig2024epidemiologytreatmentand pages 1-2)
- PanNET sequencing meta‑analysis (G1/G2). **May 2024**. https://doi.org/10.3389/fendo.2024.1351624 (andersen2024welldifferentiatedg1and pages 1-2)
- Liquid biopsy systematic review in GEP‑NENs. **Sep 2024**. https://doi.org/10.3390/cancers16193349 (almeida2024theroleof pages 1-2)
- Prospective SSTR PET comparison (18F‑AlF‑OC vs 68Ga‑DOTATATE). **Jun 2023**. https://doi.org/10.1186/s13550-023-01003-3; NCT04552847 (boeckxstaens2023prospectivecomparisonof pages 1-2)
- Temozolomide‑based regimens meta‑analysis (advanced pNET). **Feb 2024**. https://doi.org/10.1186/s12885-024-11926-2; PROSPERO CRD42023409280 (taherifard2024efficacyandsafety pages 1-3)
- High‑grade digestive NEN chemo outcomes and genetics. **Jun 2024**. https://doi.org/10.1038/s41416-024-02773-w (elvebakken2024treatmentoutcomeaccording pages 1-2)
- NORDIC NEC 2 prospective cohort (advanced high‑grade digestive NENs). **May 2025**. https://doi.org/10.1038/s41416-025-03054-w (sorbye2025characteristicsandtreatment pages 1-2)
- CABINET phase III cabozantinib. **Feb 2025**. https://doi.org/10.1056/NEJMoa2403991 (chan2025phase3trial pages 1-3)

---

## Limitations of this extraction
- **ICD‑10/ICD‑11, MeSH, Orphanet, OMIM identifiers** were not retrieved in the current tool context; thus, only MONDO support from OpenTargets is provided (OpenTargets Search: gastroenteropancreatic neuroendocrine neoplasm,pancreatic neuroendocrine tumor,neuroendocrine carcinoma).
- Many sources in this run provide DOIs but do not expose **PMIDs** in the extracted text; therefore, PMID‑level citations could not be consistently supplied.
- Environmental risk/protective factors, QoL instruments, prevention, non‑human disease, and model organism details were not sufficiently captured in the retrieved evidence.


References

1. (OpenTargets Search: gastroenteropancreatic neuroendocrine neoplasm,pancreatic neuroendocrine tumor,neuroendocrine carcinoma): Open Targets Query (gastroenteropancreatic neuroendocrine neoplasm,pancreatic neuroendocrine tumor,neuroendocrine carcinoma, 36 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (pellegrino2023diagnosticmanagementof pages 1-2): Fabio Pellegrino, Vincenza Granata, Roberta Fusco, Francesca Grassi, Salvatore Tafuto, Luca Perrucci, Giulia Tralli, and Mariano Scaglione. Diagnostic management of gastroenteropancreatic neuroendocrine neoplasms: technique optimization and tips and tricks for radiologists. Tomography, 9:217-246, Jan 2023. URL: https://doi.org/10.3390/tomography9010018, doi:10.3390/tomography9010018. This article has 24 citations.

3. (castillon2023seomgetneclinicalguidelines pages 1-2): Jaume Capdevila Castillón, Teresa Alonso Gordoa, Alberto Carmona Bayonas, Ana Custodio Carretero, Rocío García-Carbonero, Enrique Grande Pulido, Paula Jiménez Fonseca, Angela Lamarca Lete, Angel Segura Huerta, and Javier Gallego Plazas. Seom-getne clinical guidelines for the diagnosis and treatment of gastroenteropancreatic and bronchial neuroendocrine neoplasms (nens) (2022). Clinical & Translational Oncology, 25:2692-2706, May 2023. URL: https://doi.org/10.1007/s12094-023-03205-6, doi:10.1007/s12094-023-03205-6. This article has 16 citations and is from a peer-reviewed journal.

4. (qasim2026neuroendocrineneoplasmsof pages 2-3): Hussein Qasim, Shaima' Dibian, Mohammad Abu Shugaer, Karis Khattab, Mudhaffer Touqan, Matteo Luigi Giuseppe Leoni, and Giustino Varrassi. Neuroendocrine neoplasms of the gastrointestinal tract: morphology, who 2022 grading, and prognostic perspectives. Cureus, Jan 2026. URL: https://doi.org/10.7759/cureus.100913, doi:10.7759/cureus.100913. This article has 0 citations.

5. (qasim2026neuroendocrineneoplasmsof pages 7-8): Hussein Qasim, Shaima' Dibian, Mohammad Abu Shugaer, Karis Khattab, Mudhaffer Touqan, Matteo Luigi Giuseppe Leoni, and Giustino Varrassi. Neuroendocrine neoplasms of the gastrointestinal tract: morphology, who 2022 grading, and prognostic perspectives. Cureus, Jan 2026. URL: https://doi.org/10.7759/cureus.100913, doi:10.7759/cureus.100913. This article has 0 citations.

6. (tan2024gastroenteropancreaticneuroendocrineneoplasms pages 1-2): Baizhou Tan, Beiyu Zhang, and Hongping Chen. Gastroenteropancreatic neuroendocrine neoplasms: epidemiology, genetics, and treatment. Frontiers in Endocrinology, Sep 2024. URL: https://doi.org/10.3389/fendo.2024.1424839, doi:10.3389/fendo.2024.1424839. This article has 28 citations.

7. (peshin2025currentclinicaltrial pages 4-6): Supriya Peshin, Shivani Modi, Rodrick Babakhanlou, and Junaid Arshad. Current clinical trial landscape of gastroenteropancreatic neuroendocrine tumors: a new era of landmark trials. Journal of Clinical Medicine, 14:6522, Sep 2025. URL: https://doi.org/10.3390/jcm14186522, doi:10.3390/jcm14186522. This article has 3 citations.

8. (peshin2025currentclinicaltrial pages 1-3): Supriya Peshin, Shivani Modi, Rodrick Babakhanlou, and Junaid Arshad. Current clinical trial landscape of gastroenteropancreatic neuroendocrine tumors: a new era of landmark trials. Journal of Clinical Medicine, 14:6522, Sep 2025. URL: https://doi.org/10.3390/jcm14186522, doi:10.3390/jcm14186522. This article has 3 citations.

9. (sorbye2025characteristicsandtreatment pages 1-2): Halfdan Sorbye, Geir Olav Hjortland, Lene Weber Vestermark, Morten Ladekarl, Johanna Svensson, Anna Sundlöv, Eva Tiensuu Janson, Herish Garresori, Eva Hofsli, Christian Kersten, Hege Elvebakken, Per Pfeiffer, Siren Morken, Jorg Assmus, Inger Marie Bowitz Lothe, Elizaveta Tabaksblat, Ulrich Knigge, Anne Couvelard, Aurel Perren, and Seppo W. Langer. Characteristics and treatment outcome in a prospective cohort of 639 advanced high-grade digestive neuroendocrine neoplasms (net g3 and nec). the nordic nec 2 study. British Journal of Cancer, 133:316-324, May 2025. URL: https://doi.org/10.1038/s41416-025-03054-w, doi:10.1038/s41416-025-03054-w. This article has 34 citations and is from a domain leading peer-reviewed journal.

10. (elvebakken2024treatmentoutcomeaccording pages 1-2): Hege Elvebakken, Andreas Venizelos, Aurel Perren, Anne Couvelard, Inger Marie B. Lothe, Geir O. Hjortland, Tor Å. Myklebust, Johanna Svensson, Herish Garresori, Christian Kersten, Eva Hofsli, Sönke Detlefsen, Lene W. Vestermark, Stian Knappskog, and Halfdan Sorbye. Treatment outcome according to genetic tumour alterations and clinical characteristics in digestive high-grade neuroendocrine neoplasms. British Journal of Cancer, 131:676-684, Jun 2024. URL: https://doi.org/10.1038/s41416-024-02773-w, doi:10.1038/s41416-024-02773-w. This article has 9 citations and is from a domain leading peer-reviewed journal.

11. (uhlig2024epidemiologytreatmentand pages 1-2): Johannes Uhlig, James Nie, Joanna Gibson, Michael Cecchini, Stacey Stein, Jill Lacy, Pamela L. Kunz, and Hyun S. Kim. Epidemiology, treatment and outcomes of gastroenteropancreatic neuroendocrine neoplasms. Scientific Reports, Dec 2024. URL: https://doi.org/10.1038/s41598-024-81518-4, doi:10.1038/s41598-024-81518-4. This article has 23 citations and is from a peer-reviewed journal.

12. (taherifard2024efficacyandsafety pages 1-3): Erfan Taherifard, Muhammad Bakhtiar, Mahnoor Mahnoor, Rabeea Ahmed, Ludimila Cavalcante, Janie Zhang, and Anwaar Saeed. Efficacy and safety of temozolomide-based regimens in advanced pancreatic neuroendocrine tumors: a systematic review and meta-analysis. BMC Cancer, Feb 2024. URL: https://doi.org/10.1186/s12885-024-11926-2, doi:10.1186/s12885-024-11926-2. This article has 10 citations and is from a peer-reviewed journal.

13. (boeckxstaens2023prospectivecomparisonof pages 1-2): Lennert Boeckxstaens, Elin Pauwels, Vincent Vandecaveye, Wies Deckers, Frederik Cleeren, Jeroen Dekervel, Timon Vandamme, Kim Serdons, Michel Koole, Guy Bormans, Annouschka Laenen, Paul M. Clement, Karen Geboes, Eric Van Cutsem, Kristiaan Nackaerts, Sigrid Stroobants, Chris Verslype, Koen Van Laere, and Christophe M. Deroose. Prospective comparison of [18f]alf-nota-octreotide pet/mri to [68ga]ga-dotatate pet/ct in neuroendocrine tumor patients. EJNMMI Research, Jun 2023. URL: https://doi.org/10.1186/s13550-023-01003-3, doi:10.1186/s13550-023-01003-3. This article has 24 citations and is from a peer-reviewed journal.

14. (andersen2024welldifferentiatedg1and pages 1-2): Kirstine Øster Andersen, Sönke Detlefsen, Klaus Brusgaard, and Henrik Thybo Christesen. Well-differentiated g1 and g2 pancreatic neuroendocrine tumors: a meta-analysis of published expanded dna sequencing data. Frontiers in Endocrinology, May 2024. URL: https://doi.org/10.3389/fendo.2024.1351624, doi:10.3389/fendo.2024.1351624. This article has 11 citations.

15. (almeida2024theroleof pages 1-2): Catarina Almeida, Lorenzo Gervaso, Gianmaria Frigè, Francesca Spada, Lavinia Benini, Chiara Alessandra Cella, Luca Mazzarella, and Nicola Fazio. The role of liquid biopsy in gastroenteropancreatic neuroendocrine neoplasms. Cancers, 16:3349, Sep 2024. URL: https://doi.org/10.3390/cancers16193349, doi:10.3390/cancers16193349. This article has 7 citations.

16. (boeckxstaens2023prospectivecomparisonof media b98f7885): Lennert Boeckxstaens, Elin Pauwels, Vincent Vandecaveye, Wies Deckers, Frederik Cleeren, Jeroen Dekervel, Timon Vandamme, Kim Serdons, Michel Koole, Guy Bormans, Annouschka Laenen, Paul M. Clement, Karen Geboes, Eric Van Cutsem, Kristiaan Nackaerts, Sigrid Stroobants, Chris Verslype, Koen Van Laere, and Christophe M. Deroose. Prospective comparison of [18f]alf-nota-octreotide pet/mri to [68ga]ga-dotatate pet/ct in neuroendocrine tumor patients. EJNMMI Research, Jun 2023. URL: https://doi.org/10.1186/s13550-023-01003-3, doi:10.1186/s13550-023-01003-3. This article has 24 citations and is from a peer-reviewed journal.

17. (boeckxstaens2023prospectivecomparisonof media be4d67f8): Lennert Boeckxstaens, Elin Pauwels, Vincent Vandecaveye, Wies Deckers, Frederik Cleeren, Jeroen Dekervel, Timon Vandamme, Kim Serdons, Michel Koole, Guy Bormans, Annouschka Laenen, Paul M. Clement, Karen Geboes, Eric Van Cutsem, Kristiaan Nackaerts, Sigrid Stroobants, Chris Verslype, Koen Van Laere, and Christophe M. Deroose. Prospective comparison of [18f]alf-nota-octreotide pet/mri to [68ga]ga-dotatate pet/ct in neuroendocrine tumor patients. EJNMMI Research, Jun 2023. URL: https://doi.org/10.1186/s13550-023-01003-3, doi:10.1186/s13550-023-01003-3. This article has 24 citations and is from a peer-reviewed journal.

18. (boeckxstaens2023prospectivecomparisonof media 4b687989): Lennert Boeckxstaens, Elin Pauwels, Vincent Vandecaveye, Wies Deckers, Frederik Cleeren, Jeroen Dekervel, Timon Vandamme, Kim Serdons, Michel Koole, Guy Bormans, Annouschka Laenen, Paul M. Clement, Karen Geboes, Eric Van Cutsem, Kristiaan Nackaerts, Sigrid Stroobants, Chris Verslype, Koen Van Laere, and Christophe M. Deroose. Prospective comparison of [18f]alf-nota-octreotide pet/mri to [68ga]ga-dotatate pet/ct in neuroendocrine tumor patients. EJNMMI Research, Jun 2023. URL: https://doi.org/10.1186/s13550-023-01003-3, doi:10.1186/s13550-023-01003-3. This article has 24 citations and is from a peer-reviewed journal.

19. (hernandezfelix2025emergingdiagnosticsand pages 5-6): Jorge H. Hernandez-Felix, Monica Isabel Meneses-Medina, Rachel Riechelmann, Jonathan Strosberg, Rocio Garcia-Carbonero, and Jaydira del Rivero. Emerging diagnostics and therapies in neuroendocrine neoplasms: a critical review. Cancers, 17:3632, Nov 2025. URL: https://doi.org/10.3390/cancers17223632, doi:10.3390/cancers17223632. This article has 4 citations.

20. (chan2025phase3trial pages 1-3): Jennifer A. Chan, Susan Geyer, Tyler Zemla, Michael V. Knopp, Spencer Behr, Sydney Pulsipher, Fang-Shu Ou, Amylou C. Dueck, Jared Acoba, Ardaman Shergill, Edward M. Wolin, Thorvardur R. Halfdanarson, Bhavana Konda, Nikolaos A. Trikalinos, Bernard Tawfik, Nitya Raj, Shagufta Shaheen, Namrata Vijayvergia, Arvind Dasari, Jonathan R. Strosberg, Elise C. Kohn, Matthew H. Kulke, Eileen M. O’Reilly, and Jeffrey A. Meyerhardt. Phase 3 trial of cabozantinib to treat advanced neuroendocrine tumors. New England Journal of Medicine, 392:653-665, Feb 2025. URL: https://doi.org/10.1056/nejmoa2403991, doi:10.1056/nejmoa2403991. This article has 172 citations and is from a highest quality peer-reviewed journal.

21. (boeckxstaens2023prospectivecomparisonof pages 8-9): Lennert Boeckxstaens, Elin Pauwels, Vincent Vandecaveye, Wies Deckers, Frederik Cleeren, Jeroen Dekervel, Timon Vandamme, Kim Serdons, Michel Koole, Guy Bormans, Annouschka Laenen, Paul M. Clement, Karen Geboes, Eric Van Cutsem, Kristiaan Nackaerts, Sigrid Stroobants, Chris Verslype, Koen Van Laere, and Christophe M. Deroose. Prospective comparison of [18f]alf-nota-octreotide pet/mri to [68ga]ga-dotatate pet/ct in neuroendocrine tumor patients. EJNMMI Research, Jun 2023. URL: https://doi.org/10.1186/s13550-023-01003-3, doi:10.1186/s13550-023-01003-3. This article has 24 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Gastroenteropancreatic_Neuroendocrine_Neoplasm-deep-research-falcon_artifacts/artifact-00.md)
![## Context ID: pqac-00000027 The requested tables showing the detection ratio (DR) for [18F]AlF-OC and [68Ga]Ga-DOTATATE are Table 3 and Table 4. Table 3 compar](Gastroenteropancreatic_Neuroendocrine_Neoplasm-deep-research-falcon_artifacts/image-1.png)