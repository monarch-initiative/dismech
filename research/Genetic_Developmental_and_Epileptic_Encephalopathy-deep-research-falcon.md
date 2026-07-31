---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T00:13:52.650384'
end_time: '2026-07-31T00:22:59.674007'
duration_seconds: 547.02
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Genetic Developmental and Epileptic Encephalopathy
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 28
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Genetic_Developmental_and_Epileptic_Encephalopathy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Genetic Developmental and Epileptic Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Genetic Developmental and Epileptic Encephalopathy** covering all of the
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
- **Disease Name:** Genetic Developmental and Epileptic Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Genetic Developmental and Epileptic Encephalopathy** covering all of the
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


# Genetic Developmental and Epileptic Encephalopathy

## Executive summary and scope

Genetic developmental and epileptic encephalopathies (genetic DEEs) are not one molecular disease but an etiologically heterogeneous family of severe neurodevelopmental epilepsies. The defining concept is that **both** the underlying developmental disorder and epileptic activity contribute—independently and additively—to cognitive, behavioral, and neurological impairment. They usually begin in infancy or childhood with seizures, abundant epileptiform EEG activity, developmental slowing or regression, and multiple non-seizure comorbidities. The International League Against Epilepsy (ILAE) introduced the combined term in 2017 to distinguish DEE from a purely “epileptic encephalopathy,” in which epileptic activity is assumed to be the principal cause of developmental deterioration. (scheffer2024developmentalandepileptic pages 1-4, chang2023genetictestingin pages 4-6)

A 2024 expert review describes DEEs as the most severe epilepsy group and emphasizes that management must address seizures, development, behavior, movement, sleep, feeding, respiratory health, and family burden—not seizure counts alone. More than 800–900 genes have been associated with monogenic DEEs, although gene validity and phenotype specificity vary and the number continues to expand. (specchio2024theexpandingfield pages 1-6, scheffer2024developmentalandepileptic pages 9-11, scheffer2024developmentalandepileptic pages 19-21)

**Evidence boundary:** statistics from Dravet syndrome, CDKL5 deficiency disorder, STXBP1 encephalopathy, infantile epileptic spasms syndrome, or another named DEE must not automatically be generalized to all genetic DEEs.

## 1. Disease information

### Definition, names, and identifiers

Common names include **developmental and epileptic encephalopathy**, **DEE**, **genetic DEE**, **developmental epileptic encephalopathy**, and the older terms **epileptic encephalopathy** and **early infantile epileptic encephalopathy**. Named syndromes within the umbrella include Dravet syndrome, early-infantile DEE, epilepsy of infancy with migrating focal seizures, infantile epileptic spasms syndrome, and Lennox–Gastaut syndrome; some are genetically homogeneous, whereas others have structural, metabolic, infectious, or unknown causes. (scheffer2024developmentalandepileptic pages 9-11, scheffer2024developmentalandepileptic pages 1-4)

There is **no single universal OMIM number**, because OMIM generally assigns entries to individual gene-defined disorders such as SCN1A-, KCNQ2-, STXBP1-, or CDKL5-related encephalopathy. The same limitation applies to Orphanet and MONDO: individual syndromes have specific identifiers, while the umbrella concept is represented hierarchically and database mappings can change. For production use, the current MONDO/Orphanet release should therefore be queried rather than assigning one unverified umbrella identifier. ICD-10-CM usually requires epilepsy/syndrome and intellectual-disability codes rather than a unique genetic-DEE code; ICD-11 provides more granular developmental/epileptic encephalopathy categories. MeSH concepts include *Epileptic Encephalopathies* and individual syndromes.

The evidence summarized here is primarily **aggregated disease-level evidence** from reviews, cohorts, registries, and trials. It is not an extraction from individual EHRs, although several cohorts were assembled by retrospective medical-record and EEG review.

## 2. Etiology, risk, protective factors, and gene–environment interaction

### Causal factors

Genetic DEEs arise from germline or post-zygotic pathogenic variants affecting neuronal excitability, synaptic transmission, neurotransmitter receptors, cortical development, intracellular signaling, metabolism, organelle function, and chromatin/transcriptional regulation. Representative genes include:

- **Ion channels:** *SCN1A, SCN2A, SCN8A, KCNQ2, KCNT1, KCNH5, CACNA1A*.
- **Synaptic release/signaling:** *STXBP1, SYNGAP1, PCDH19, NBEA*.
- **Receptors:** *GRIN* family genes.
- **mTOR/cortical development:** *TSC1, TSC2, MTOR, DEPDC5*.
- **Chromatin/transcription/RNA regulation:** *CHD2, HNRNPU, KMT2A, CDKL5*.
- **Metabolic/transport pathways:** *SLC2A1, GLDC* and numerous mitochondrial or vitamin-responsive disorders.

In a 2024 early-onset cohort, ion-channel genes were the largest functional class, accounting for 36/104 monogenic cases; *SCN1A* and *KCNQ2* were the leading channel genes. (cavirani2024geneticepilepsiesand pages 2-4, cavirani2024geneticepilepsiesand pages 4-6)

### Genetic risk and inheritance

Most diagnosed severe early-onset cases involve highly penetrant rare variants rather than common polygenic susceptibility. De novo autosomal-dominant variants are prominent, but autosomal-recessive, X-linked, mitochondrial, inherited dominant, and parental-mosaic mechanisms occur. A 2024 Italian survey of 1,568 molecularly diagnosed patients found 77% involving autosomal-dominant genes, 17% X-linked genes, and 6% autosomal-recessive genes; *SCN1A* accounted for 16%, *KCNQ2* 5.6%, and *SCN2A* 5%. These figures reflect diagnosed cases and testing practice, not unbiased population frequencies.

Recurrence risk is variant-specific. A confirmed de novo variant usually implies low—but not zero—recurrence because parental germline mosaicism is possible. Recessive disease creates a 25% recurrence risk for each pregnancy when both parents are carriers. X-linked recurrence depends on maternal carrier or mosaic status. Variable expressivity and incomplete penetrance occur in several genes, particularly familial channel, synaptic, and mTOR-pathway disorders. Genetic anticipation is not a general DEE feature.

Pathogenic variants are usually absent or extremely rare in population databases such as gnomAD; a numerical allele-frequency threshold cannot be assigned across the umbrella. Classification must follow ACMG/AMP criteria using segregation, population frequency, phenotype match, computational data, and functional evidence. Missense, nonsense, frameshift, splice, copy-number, structural, regulatory, mitochondrial, and mosaic variants all occur. A VUS is **not diagnostic** and should not independently direct irreversible therapy. Exome studies can report VUS rates of 25.3–86%, illustrating the interpretation burden. (chang2023genetictestingin pages 4-6)

### Environmental and protective factors

There is no evidence that smoking, diet, pollution, occupation, or an infectious agent is a primary cause of **genetic** DEE. Fever, infection, sleep loss, and elevated temperature can trigger seizures in susceptible genotypes, especially SCN1A-related Dravet syndrome; inflammation may worsen SCN1A channel dysfunction and seizure severity. This is trigger modulation, not causation. Routine vaccination does not create the underlying genetic disorder, although fever temporally associated with vaccination can unmask fever-sensitive seizures. (specchio2024theexpandingfield pages 14-17)

No broadly validated environmental or genetic protective factor prevents genetic DEE. Prompt fever management, avoidance of known individual triggers, medication adherence, nocturnal supervision where appropriate, and early syndrome-specific treatment may reduce complications. Ketogenic dietary therapy can improve seizures in subsets but is treatment, not primary prevention. Model-organism observations such as estrogen-mediated suppression of CNTNAP2-associated behaviors are hypothesis-generating and not established human protective factors. (sun2024strategiesfordissecting pages 14-15)

## 3. Phenotypes

Core and associated phenotypes vary by gene and age:

- **Recurrent seizures**—often neonatal or infantile onset, multiple types, prolonged, and drug-resistant. Suggested HPO: *Seizure* (HP:0001250), *Neonatal-onset seizures*, *Infantile-onset seizures*, *Status epilepticus*, *Epileptic spasm*.
- **Abnormal EEG**—multifocal or generalized epileptiform discharges; syndrome-dependent hypsarrhythmia, burst suppression, slow spike-wave, or migrating focal activity. HPO: *EEG abnormality* (HP:0002353), *Hypsarrhythmia*.
- **Global developmental delay/intellectual disability**, frequently severe or profound; development may be delayed before seizures and may stagnate or regress after seizure onset. HPO: HP:0001263, HP:0001249, *Developmental regression* (HP:0002376).
- **Speech/language impairment**, sometimes minimal or absent speech. HPO: *Delayed speech and language development* (HP:0000750), *Absent speech*.
- **Motor abnormalities:** hypotonia, spasticity, ataxia, gait impairment, dystonia, stereotypies, tremor, and myoclonus. HPO: HP:0001252, HP:0001257, HP:0001251, HP:0001332, HP:0002072.
- **Behavioral/psychiatric features:** autism traits, ADHD, irritability, anxiety, and sleep disturbance. HPO: HP:0000729, HP:0007018, HP:0002360.
- **Systemic morbidity:** feeding/swallowing and gastrointestinal problems, respiratory vulnerability, orthopedic complications, visual impairment, and growth abnormalities, depending on genotype. (scheffer2024developmentalandepileptic pages 9-11, scheffer2024developmentalandepileptic pages 1-4)

In a 2024 multicenter monogenic cohort, developmental delay/intellectual disability occurred in 84/104 (80.7%), abnormal neurological examination in 74/104 (71%), autistic features in 12/104 (11.5%), ADHD in 4/104 (3.8%), and other behavioral disorders in 15/104 (14.4%). These are cohort—not universal—frequencies. Seizures began at a mean 11 months, with generalized onset in 37.5% and focal onset in 31%. (cavirani2024geneticepilepsiesand pages 2-4, cavirani2024geneticepilepsiesand pages 4-6)

Among 77 patients selected for movement disorders, stereotypies occurred in 48%, dystonia in 44%, chorea in 23%, myoclonus in 18%, ataxia in 12%, tremor in 9%, and hypokinesia in 8%; 47% had more than one movement disorder. Selection makes these inappropriate as general DEE prevalence estimates.

Quality of life is substantially impaired by seizures, medication adverse effects, mobility, communication limitations, behavior, sleep, and dependence in activities of daily living. Cross-sectional studies show worse health-related quality of life than both the general population and unselected childhood epilepsy cohorts. Caregiver depression, employment disruption, and family burden are substantial. (scheffer2024developmentalandepileptic pages 17-19)

## 4. Genetic and molecular information

| Mechanism class | Representative genes | Typical functional consequence | Causal chain to phenotype | Representative precision-management implication | Evidence type / limitations |
|---|---|---|---|---|---|
| Voltage-gated sodium channelopathy | SCN1A, SCN2A, SCN8A | Variant-specific; can be loss-of-function (LOF) or gain-of-function (GOF), so effect must be interpreted per gene/variant rather than assumed | Altered sodium current changes neuronal excitability during early brain development, contributing to recurrent seizures, epileptiform activity, and downstream developmental slowing/regression; SCN1A-related Dravet syndrome is a key example (scheffer2024developmentalandepileptic pages 1-4, scheffer2024developmentalandepileptic pages 19-21, specchio2024theexpandingfield pages 6-8) | Precision management depends on mechanism: activity-boosting strategies for LOF versus inhibitory strategies for GOF; SCN1A-positive Dravet syndrome has AAV9 transcriptional activation trials (ETX101) designed to increase SCN1A expression in presumed LOF disease (specchio2024theexpandingfield pages 6-8, NCT06112275 chunk 1, NCT06283212 chunk 1) | Human umbrella reviews plus gene-specific trials and mouse studies support this class, but not every variant in these genes behaves identically and treatment generalization across sodium-channel genes is unsafe (scheffer2024developmentalandepileptic pages 1-4, specchio2024theexpandingfield pages 14-17, NCT06112275 chunk 1) |
| Potassium channelopathy | KCNQ2, KCNT1, KCNH5 | Variant-specific GOF or LOF; functional direction is clinically important and should be established where possible | Disordered potassium conductance impairs membrane repolarization and network stability, producing neonatal/infantile seizures and, in severe cases, DEE with developmental impairment (cavirani2024geneticepilepsiesand pages 2-4, specchio2024theexpandingfield pages 6-8) | Mechanism-guided therapy is conceptually important: inhibitor approach for some GOF states versus function-supporting approach for LOF states; emerging gene/RNA strategies are under study broadly in DEE, but robust variant-level treatment rules remain incomplete (specchio2024theexpandingfield pages 6-8, scheffer2024developmentalandepileptic pages 17-19) | Evidence is strong for inclusion of potassium-channel genes among major DEE causes, but the gathered evidence is mostly review-level and does not provide uniform variant-specific response data for all genes in this class (cavirani2024geneticepilepsiesand pages 2-4, specchio2024theexpandingfield pages 6-8) |
| Synaptic vesicle / synaptic signaling dysfunction | STXBP1, SYNGAP1, PCDH19, NBEA | Often reduced or altered synaptic function; exact consequence is gene- and variant-specific | Impaired vesicle release or synaptic signaling disrupts circuit formation and excitatory/inhibitory balance, leading to seizures, developmental delay/intellectual disability, and frequent movement/behavioral comorbidity (cavirani2024geneticepilepsiesand pages 4-6, specchio2024theexpandingfield pages 6-8) | Supportive precision approach is mainly diagnosis-led today; STXBP1 has an early interventional gene-therapy program (CAP-002) in pediatrics, but efficacy is not established (NCT06983158 chunk 2) | Evidence comes from multicenter human cohorts and reviews; STXBP1 trial evidence is preliminary, and mechanistic heterogeneity across synaptic genes limits direct extrapolation from one gene to another (cavirani2024geneticepilepsiesand pages 4-6, NCT06983158 chunk 2) |
| Glutamatergic receptor / excitatory synapse dysfunction | GRIN2A and broader GRIN family | Variant-specific receptor dysfunction, potentially GOF or LOF depending on variant | Abnormal NMDA receptor signaling disturbs synaptic maturation and excitatory circuit development, contributing to epileptiform activity plus language/cognitive impairment characteristic of some DEEs (specchio2024theexpandingfield pages 1-6, specchio2024theexpandingfield pages 6-8) | Precision implication is mechanism-first interpretation rather than syndrome-first treatment; receptor dysfunction supports rationale for targeted pathway modulation, but gene-specific standardized therapies were not established in the gathered clinical evidence (specchio2024theexpandingfield pages 6-8) | Evidence is mainly review-level in the gathered set; mechanistic plausibility is strong, but variant-level therapeutic evidence is comparatively limited here (specchio2024theexpandingfield pages 1-6, specchio2024theexpandingfield pages 6-8) |
| mTOR-pathway dysregulation / cortical developmental pathology | MTOR, TSC1, TSC2 | Typically pathway overactivation in relevant disorders, though exact molecular consequence depends on lesion/gene context | mTOR overactivation in the developing cortex can drive malformations of cortical development, network hyperexcitability, infantile spasms/epilepsy, and developmental impairment (specchio2024theexpandingfield pages 17-21, specchio2024theexpandingfield pages 6-8, specchio2024theexpandingfield pages 14-17) | mTOR is a representative actionable pathway in DEE; pathway-oriented treatment logic is stronger here than in many other classes, although the gathered evidence emphasizes translational rationale more than new 2024 trial outcomes (specchio2024theexpandingfield pages 17-21, specchio2024theexpandingfield pages 14-17) | Supported by authoritative reviews and pathway-oriented discussion; however, not all mTOR-related epilepsies are identical and some evidence cited is translational rather than direct comparative clinical efficacy data (specchio2024theexpandingfield pages 17-21, specchio2024theexpandingfield pages 14-17) |
| Metabolic / vitamin-responsive causes within early-infantile DEE differential | GLDC, SAMHD1; biotinidase deficiency noted in cohort-level metabolic testing | Mechanistically heterogeneous; some are potentially treatable metabolic defects rather than classic ion-channel DEEs | Metabolic dysfunction can produce early seizures and encephalopathy; in early-infantile cohorts, vitamin-responsive etiologies had better seizure control than genetic/unknown groups, showing the importance of separating treatable metabolic causes from monogenic DEE (cavirani2024geneticepilepsiesand pages 4-6) | Precision implication is urgent metabolic evaluation because some early-infantile epilepsies are vitamin responsive and clinically more treatable than most monogenic DEEs () | Strong practical message from prospective human cohort, but this row spans heterogeneous disorders and should not be collapsed into a single molecular DEE mechanism () |
| Chromatin / transcriptional regulation defects | CHD2, KMT2A, HNRNPU, CDKL5 | Often dosage-sensitive or loss-of-function/haploinsufficiency-like effects, but not uniformly so across genes | Disrupted transcriptional or chromatin regulation alters neuronal differentiation and network development, yielding treatment-resistant epilepsy, developmental delay/intellectual disability, autism/behavioral features, and possible regression (cavirani2024geneticepilepsiesand pages 4-6, scheffer2024developmentalandepileptic pages 17-19) | Current precision-management value is highest for diagnosis, prognosis, and trial readiness; CHD2 is highlighted as dosage sensitive with model systems under development, but no established targeted therapy yet (scheffer2024developmentalandepileptic pages 17-19) | Human cohort and roadmap/model evidence support this class; important limitation is that some animal models fail to recapitulate seizures, underscoring translational gaps (scheffer2024developmentalandepileptic pages 17-19) |


*Table: This table summarizes major mechanistic categories represented in genetic developmental and epileptic encephalopathies, linking gene classes to variant effects, disease biology, and current precision-management implications. It is useful as a compact knowledge-base scaffold because DEE is genetically heterogeneous and treatment logic often depends on variant-specific gain- versus loss-of-function.*

The crucial annotation principle is **variant-specific functional direction**. For example, pathogenic variants in sodium-channel genes may cause loss of function, gain of function, or altered gating. The appropriate therapy can therefore be opposite for different variants or genes: suppressing sodium current may help some gain-of-function channelopathies but worsen SCN1A loss-of-function Dravet syndrome. (specchio2024theexpandingfield pages 6-8, scheffer2024developmentalandepileptic pages 19-21)

Most causal variants are constitutional germline changes, but post-zygotic mosaic variants—especially in cortical-development/mTOR genes—may be restricted to brain tissue and missed in blood. Chromosomal abnormalities and CNVs are important: in one 168-person early-onset cohort, 45 pathogenic/likely pathogenic diagnoses were chromosomal/CNV disorders and 104 were monogenic. (cavirani2024geneticepilepsiesand pages 2-4)

Modifier genes and epigenetic state probably help explain variable expressivity, but clinically validated modifier alleles are not available for the umbrella disorder. Epigenetic dysfunction can itself be upstream when causal genes encode chromatin remodelers or transcriptional regulators; a universal DEE methylation signature has not been established.

## 5. Environmental information

Genetic DEE is neither infectious nor occupational and has no zoonotic transmission. Non-genetic insults—hypoxic–ischemic injury, congenital infection, immune encephalitis, trauma, and toxic-metabolic illness—are instead important **differential etiologies** for a child with seizures and developmental impairment. Environmental trigger management is individualized; there is no evidence-based universal lifestyle program that reverses the genetic neurodevelopmental defect.

## 6. Mechanism and pathophysiology

A general causal chain is:

**pathogenic variant/CNV → altered protein dosage or function → abnormal neuronal development, excitability, synaptic release, receptor signaling, metabolism, or cortical architecture → impaired excitation–inhibition balance and epileptic networks → recurrent seizures and epileptiform EEG activity → additional activity-dependent disruption of plasticity and cognition, superimposed on the primary developmental defect → developmental slowing/regression and multimorbidity.** (scheffer2024developmentalandepileptic pages 1-4, specchio2024theexpandingfield pages 6-8)

Upstream mechanisms include channel dysfunction, synaptic-vesicle defects, receptor dysfunction, mTOR overactivation, metabolic deficiency, and altered chromatin regulation. Downstream mechanisms include network hypersynchrony, excitotoxic/metabolic stress, sleep disruption, medication burden, injury from prolonged seizures, and impaired experience-dependent plasticity.

The developing brain is particularly vulnerable because excitatory AMPA/NMDA receptor composition and inhibitory GABAergic circuits change rapidly in infancy; immature GABAergic currents can remain depolarizing, while accelerated excitatory-circuit maturation can create transient hyperexcitability. (specchio2024theexpandingfield pages 6-8)

Suggested ontology mappings include:

- GO biological processes: *regulation of membrane potential* (GO:0042391), *chemical synaptic transmission* (GO:0007268), *synaptic vesicle exocytosis* (GO:0016079), *glutamate receptor signaling pathway*, *GABAergic synaptic transmission*, *TOR signaling* (GO:0031929), *neuron differentiation* (GO:0030182), and *chromatin organization* (GO:0006325).
- Cell Ontology: neuron (CL:0000540), glutamatergic neuron (CL:0000679), GABAergic neuron (CL:0000617), cortical neuron, interneuron, neural progenitor cell, astrocyte, oligodendrocyte, and microglial cell. The principal cell population differs by gene.
- Cellular components: voltage-gated ion-channel complex, presynaptic active zone, synaptic vesicle, postsynaptic density, neuronal plasma membrane, nucleus/chromatin, mitochondrion, lysosome, and mTOR complexes.

Transcriptomic, proteomic, metabolomic, single-cell, and spatial data remain fragmented and gene-specific. Multi-omics is a major research priority, not yet a validated umbrella diagnostic biomarker. (specchio2024theexpandingfield pages 17-21)

## 7. Anatomical structures affected

The primary organ is the **brain**, especially distributed cortical and subcortical networks. Depending on genotype, affected structures can include cerebral cortex, hippocampus, thalamus, basal ganglia, cerebellum, and brainstem autonomic/respiratory networks. Suggested UBERON terms include brain (UBERON:0000955), cerebral cortex (UBERON:0000956), hippocampal formation, thalamus, basal ganglion, cerebellum (UBERON:0002037), and brainstem (UBERON:0002298).

MRI can be normal, show nonspecific atrophy, reveal a malformation of cortical development, or demonstrate a syndrome-specific abnormality. In a prospective early-infantile cohort, MRI was abnormal in 35/80; 16/35 had a malformation and 19/35 had nonspecific findings that did not establish etiology. No consistent lateralization characterizes genetic DEE as a group.

Secondary systems include musculoskeletal tissue through immobility/spasticity, gastrointestinal and feeding systems, respiratory/autonomic systems, vision, and sleep regulation. These are usually complications or pleiotropic manifestations rather than the primary lesion.

## 8. Temporal development

Approximately 75% of DEEs begin before age three, but onset can occur later in childhood. Population-based data show that 27% of DEEs began after age three, warning against restricting testing to infancy. (scheffer2024developmentalandepileptic pages 1-4)

Typical course:

1. **Pre-seizure period:** normal, subtly delayed, or clearly abnormal development depending on genotype.
2. **Seizure onset:** neonatal, infantile, or childhood onset; acute presentation but chronic underlying disease.
3. **Evolution:** multiple seizure types and changing EEG patterns; developmental slowing, plateau, or regression.
4. **Chronic phase:** seizure burden may improve in some syndromes while intellectual, behavioral, motor, and communication disability persists or becomes more apparent.

In a 10-year SCN1A-positive Dravet study, epilepsy severity became less severe while developmental outcome worsened and autistic, behavioral, and motor/mobility comorbidities became more frequent. This illustrates that seizure improvement does not equal neurodevelopmental recovery. Critical intervention windows probably occur before or soon after network dysfunction begins, supporting rapid diagnosis and early treatment, but exact windows remain gene-specific. (scheffer2024developmentalandepileptic pages 17-19)

## 9. Inheritance and population epidemiology

A population-based New Zealand study estimated a DEE point prevalence of **112 per 100,000 children** and cumulative incidence of **169 per 100,000**—approximately **1 in 590 children** by age 16. The broader category of epilepsy plus developmental impairment occurred in approximately 1 in 340 children. These figures include genetically unresolved and non-genetic DEEs, not only molecularly confirmed disease. (scheffer2024developmentalandepileptic pages 1-4, scheffer2024developmentalandepileptic pages 19-21)

Syndrome cumulative incidence per 100,000 children was 58.2 for infantile epileptic spasms syndrome, 16.4 for epilepsy with myoclonic-atonic seizures, 13.2 for Lennox–Gastaut syndrome, and 5.1 for Dravet syndrome. One-third of children with DEE lacked a recognized electroclinical syndrome.

In the Italian molecular survey, diagnoses increased more than tenfold from 2012 to 2022; the mean age at molecular diagnosis was 11.2 years despite typically pediatric onset, demonstrating historical diagnostic delay. Geographic and ethnic differences in reported frequency largely reflect ascertainment, consanguinity, founder variants, access to sequencing, and variant interpretation. There is no established universal ethnic predisposition. Sex ratio depends on gene; X-linked disorders and sex-limited PCDH19-related disease can produce marked differences. One population cohort was 58% male, whereas a 2024 early-onset genetic cohort included 97 females and 71 males, arguing against a universal sex ratio.

## 10. Diagnostics

### Clinical evaluation

Diagnosis integrates detailed prenatal/perinatal and three-generation family history, seizure semiology, serial developmental examination, neurological and dysmorphology assessment, video-EEG, brain MRI using an epilepsy protocol, and targeted metabolic testing. EEG confirms epilepsy type and encephalopathic patterns but is rarely gene-specific. MRI identifies malformations, injuries, or structural mimics.

Urgent treatable investigations in neonatal/infantile onset can include glucose, electrolytes, calcium, magnesium, blood gas/lactate, ammonia, liver studies, plasma amino acids, acylcarnitines, urine organic acids, CSF studies where indicated, and therapeutic trials/testing for pyridoxine-, pyridoxal-phosphate-, folinic-acid-, biotin-, or glucose-transporter-responsive disease. In one prospective cohort, metabolic testing was diagnostic in 3/41 tested children, all with biotinidase deficiency; vitamin-responsive disease was the only factor independently associated with better seizure control. This supports urgent testing even though the yield is lower than sequencing.

### Genetic workflow

A practical workflow is:

1. **Rapid trio genome or exome sequencing** for critically ill neonates/infants where available.
2. Otherwise, **trio exome/genome or a comprehensive epilepsy/DEE panel** with CNV calling.
3. **Chromosomal microarray** when congenital anomalies, dysmorphism, or CNV disease is suspected, or when sequencing does not provide reliable CNV detection.
4. **Mitochondrial genome, repeat-expansion, methylation, RNA, or biochemical testing** when phenotype indicates.
5. **Reanalysis** after 12–24 months and consideration of WGS, long-read sequencing, RNA sequencing, or tissue-specific testing for mosaicism after a nondiagnostic result.
6. Parental testing, segregation, ACMG/AMP classification, and pre/post-test genetic counseling.

A 2024 first-line WES series found pathogenic variants in 35/82 (**43%**); 66% were de novo, and missense variants comprised 75%. A prospective early-infantile cohort achieved a molecular diagnosis in 53/77 (**69%**), with NGS yield 51% and microarray yield 14%. Rapid genome sequencing in infants with early seizures identified genetic etiologies in 46%, produced clinical utility in 56%, and informed prognostic counseling in 86%, with median 37 days to result. (scheffer2024developmentalandepileptic pages 9-11, chang2023genetictestingin pages 4-6)

Testing after a negative exome can still be useful because WGS detects noncoding, structural, and difficult-to-sequence variants. Single-gene testing is appropriate when a phenotype is highly specific, but broad sequencing usually performs better for heterogeneous DEE. Karyotype and FISH have limited first-line roles unless a known rearrangement is suspected.

Differential diagnoses include acquired hypoxic–ischemic injury, infection, immune encephalitis, structural epilepsy, cerebral malformation, metabolic/vitamin-responsive epilepsy, neurodegenerative disease, and developmental disability with coincidental epilepsy. There is no general newborn-screening program for DEE, although individual metabolic causes may be included in national panels.

## 11. Outcome and prognosis

Outcome is strongly genotype-, variant-, and syndrome-dependent. Many affected people have lifelong intellectual and adaptive disability, impaired communication, dependence for daily activities, movement disorder, feeding problems, orthopedic complications, and drug-resistant epilepsy. Seizure freedom does not necessarily reverse the primary developmental encephalopathy.

In 510 people with common genetic DEEs, convulsive status epilepticus occurred in **47%**, nonconvulsive status in **19%**, and 42/510 (**8%**) died. Overall mortality was **6.1 per 1,000 person-years**; 19/42 deaths were SUDEP, giving an estimated SUDEP rate of **2.8 per 1,000 person-years**. CSE occurred in 89% of the Dravet subgroup and was also frequent in KCNT1- and SCN2A-related disease. SUDEP was observed in SCN1A-, SCN2A-, SCN8A-, and STXBP1-associated groups. These data support gene-specific emergency plans and SUDEP counseling. (scheffer2024developmentalandepileptic pages 19-21)

Poor prognostic factors include early and severe epilepsy, recurrent status, profound early developmental impairment, pathogenic mechanisms producing major protein dysfunction, progressive/metabolic disease, and severe feeding or respiratory comorbidity. In Dravet syndrome, poorer baseline language, greater initial epilepsy severity, and a worse SCN1A genetic score predicted poorer ten-year development. More than 90% of caregivers reported adverse effects on their health and career opportunities. (scheffer2024developmentalandepileptic pages 17-19)

No valid umbrella five- or ten-year survival percentage exists. Prognosis should be communicated by gene, variant mechanism, syndrome, and individual trajectory.

## 12. Treatment

### Standard multimodal care

Treatment includes syndrome-appropriate antiseizure medication, emergency rescue medication and status plan, dietary therapy, and—when indicated—epilepsy surgery, vagus-nerve stimulation, or other neuromodulation. Developmental, physical, occupational, speech/augmentative-communication, feeding, sleep, behavioral, orthopedic, visual, and psychosocial care are essential.

Suggested MAXO mappings include antiseizure pharmacotherapy, electroencephalography, brain MRI, molecular genetic testing, ketogenic diet therapy, vagus-nerve stimulation, epilepsy surgery, physical therapy, occupational therapy, speech therapy, gastrostomy, genetic counseling, and seizure-emergency planning. Exact MAXO identifiers should be resolved against the current ontology release.

### Genotype- and syndrome-directed examples

- **SCN1A loss-of-function Dravet syndrome:** valproate, clobazam, stiripentol, cannabidiol, and fenfluramine are commonly used according to jurisdiction and patient profile. Sustained sodium-channel blockers can aggravate seizures in many patients and are generally avoided, although emergency-use decisions remain clinical.
- **KCNQ2/SCN2A/SCN8A channelopathy:** sodium-channel blockers may be beneficial in selected gain-of-function phenotypes but harmful in others; functional direction and age-dependent phenotype matter.
- **TSC1/TSC2 with infantile spasms:** vigabatrin is an important syndrome-specific treatment; mTOR inhibition is relevant for selected tuberous-sclerosis manifestations.
- **SLC2A1 deficiency:** ketogenic diet directly supplies alternative cerebral fuel.
- **Pyridoxine/PLP/folinic acid/biotin-responsive disorders:** prompt vitamin/cofactor therapy can be transformative.
- **Focal structural/mTOR-pathway disease:** resective or ablative surgery can be considered when a localized epileptogenic lesion is demonstrated.

Genetic diagnosis prompted medication changes in nearly half of patients in some reviewed series, but precision benefit is uneven and many interventions remain based on small cohorts or mechanistic inference. (specchio2024theexpandingfield pages 6-8)

### Emerging therapies and trials

- **ETX101, SCN1A-positive Dravet syndrome:** AAV9 delivers a GABAergic regulatory element and engineered transcription factor to increase endogenous *SCN1A* transcription. WAYFINDER, NCT06112275, is Phase 1/2, active but not recruiting, with 4 children enrolled; EXPEDITION, NCT06283212, is Phase 1/2, active but not recruiting, with 5 children. Primary outcomes include safety, monthly seizure-frequency change, prolonged seizures/status, and development. These are early safety/efficacy studies, not evidence of established benefit. URLs: https://clinicaltrials.gov/study/NCT06112275 and https://clinicaltrials.gov/study/NCT06283212. (NCT06112275 chunk 1, NCT06283212 chunk 1)
- **STXBP1 gene therapy:** CAP-002, NCT06983158, entered Phase 1/2 pediatric evaluation but the retrieved record reports termination after enrollment of one participant; no efficacy conclusion is possible. URL: https://clinicaltrials.gov/study/NCT06983158. (NCT06983158 chunk 2)
- **Ataluren for nonsense variants:** NCT02758626 was a completed Phase 2 randomized crossover trial in CDKL5 or Dravet cases with nonsense mutations, enrolling 15 children. It tested premature-stop-codon read-through; the record alone does not establish efficacy. URL: https://clinicaltrials.gov/study/NCT02758626. (NCT02758626 chunk 1, NCT02758626 chunk 2)
- **CDKL5 hyperthermic baths:** NCT06447675 was an eight-person feasibility study of 20-minute daily 40–42°C baths; a 34-person PROBE trial, NCT07602205, is planned. This unconventional intervention lacks established efficacy and should only be considered in a research protocol with safety oversight. URLs: https://clinicaltrials.gov/study/NCT06447675 and https://clinicaltrials.gov/study/NCT07602205. (NCT06447675 chunk 1, NCT07602205 chunk 1)
- **RNA therapeutics:** antisense oligonucleotides have improved phenotypes in preclinical SCN1A, SCN2A, SCN8A, and KCNT1 models. TANGO-type approaches increase productive gene output. Human efficacy and long-term neurodevelopmental effects remain unproven. (scheffer2024developmentalandepileptic pages 17-19)

No curative therapy is currently established for genetic DEE as a group. Authoritative reviews emphasize that trial endpoints should include development, behavior, sleep, motor function, and caregiver burden in addition to seizures. (specchio2024theexpandingfield pages 1-6, specchio2024theexpandingfield pages 17-21)

## 13. Prevention

Primary prevention by lifestyle modification or vaccination is not applicable to a spontaneous pathogenic variant. Relevant preventive strategies are:

- **Reproductive prevention/options:** genetic counseling, parental segregation and mosaicism testing, carrier testing for recessive/X-linked disease, prenatal diagnosis, and preimplantation genetic testing when the familial variant is known.
- **Secondary prevention:** rapid genetic/metabolic diagnosis, early syndrome-specific treatment, developmental intervention, and cascade testing where relatives may carry a pathogenic variant.
- **Tertiary prevention:** individualized status plans, rescue medication, medication adherence, trigger management, drowning and bathing precautions, sleep and respiratory management, feeding/aspiration care, bone health, and explicit SUDEP counseling.

Population newborn genomic screening for DEE is not standard. Some treatable metabolic causes are detected by conventional newborn screening, depending on jurisdiction.

## 14. Other species and natural disease

DEE is not a transmissible disease and has no zoonotic potential. Homologous epilepsy/neurodevelopmental phenotypes can occur naturally in veterinary species, but “genetic DEE” is not a single cross-species veterinary diagnosis. Gene- and breed-specific entries should be sought in OMIA and the Vertebrate Breed Ontology rather than inferred from the human umbrella.

Orthologues of major genes—including *SCN1A, SCN2A, KCNQ2, STXBP1, CDKL5, CHD2,* and *SYNGAP1*—are evolutionarily conserved across mammals and many vertebrates, enabling comparative study of channel, synaptic, and developmental mechanisms. NCBI Taxonomy identifiers commonly used in research include human 9606, mouse 10090, zebrafish 7955, fruit fly 7227, and *C. elegans* 6239.

## 15. Model organisms and experimental systems

Models include knock-out, knock-in, haploinsufficient, conditional, and humanized mice; zebrafish, Drosophila, Xenopus, and *C. elegans*; heterologous electrophysiology systems; patient-derived iPSC neurons; CRISPR-isogenic lines; and cerebral organoids.

**Applications:** variant functional classification, developmental timing, cell-type-specific excitability, seizure-network analysis, transcriptomic/proteomic profiling, drug screening, viral-vector biodistribution, and gene/RNA-therapy proof of concept.

In SCN1A mouse models, viral delivery or transcriptional activation directed toward relevant brain regions or GABAergic neurons reduced hyperthermia-induced seizures; CAV-2 delivery to thalamus and hippocampus improved survival and spontaneous seizures. These are preclinical results and do not establish human safety or efficacy. (specchio2024theexpandingfield pages 14-17)

Patient-derived iPSC neurons preserve the human genetic background and can be paired with CRISPR-corrected controls; organoids permit study of early cortical development and cell-type interactions. Limitations include immature cellular states, variable differentiation, incomplete vascular/immune architecture, and poor modeling of long-range circuits and whole-organism pharmacology.

Animal-model limitations are equally important. Species differences in channel expression, brain development, and genetic background can alter seizure phenotypes. For example, some CHD2 mouse models do not develop seizures despite the human disorder, prompting use of zebrafish, frogs, patient-derived cells, and cortical organoids. (sun2024strategiesfordissecting pages 14-15)

## Current expert assessment and priority gaps

The strongest expert consensus is that DEE care should move from electroclinical labels alone toward **integrated electroclinical–genomic diagnosis**, while retaining syndrome labels where they guide treatment and prognosis. Mechanism must be established at the variant level: the same gene family can contain both gain- and loss-of-function disease, making indiscriminate “gene-based” treatment unsafe. (specchio2024theexpandingfield pages 6-8)

Major gaps are unresolved genetic diagnoses; limited ancestry diversity; uncertain VUS interpretation; scarce longitudinal adult data; weak developmental biomarkers; inadequate natural-history controls; undermeasurement of sleep, movement, communication, and caregiver outcomes; and uncertain durability, immunogenicity, and developmental timing of gene/RNA therapies. International registries, functional assays, multi-omics, and prospective studies beginning before treatment are therefore priorities. (specchio2024theexpandingfield pages 1-6, specchio2024theexpandingfield pages 17-21)

## Key recent sources

1. Scheffer IE et al. **Developmental and epileptic encephalopathies.** *Nature Reviews Disease Primers.* Published September 2024;10:61. DOI/URL: https://doi.org/10.1038/s41572-024-00546-6. Authoritative disease primer. (scheffer2024developmentalandepileptic pages 9-11, scheffer2024developmentalandepileptic pages 1-4)
2. Specchio N et al. **The expanding field of genetic developmental and epileptic encephalopathies: current understanding and future perspectives.** *Lancet Child & Adolescent Health.* Published November 2024;8:821–834. DOI/URL: https://doi.org/10.1016/S2352-4642(24)00196-2. Expert review of mechanisms and emerging therapies. (specchio2024theexpandingfield pages 1-6, specchio2024theexpandingfield pages 17-21)
3. Chang Y-T et al. **Genetic Testing in Children with Developmental and Epileptic Encephalopathies.** *Children.* Published March 2023;10:556. DOI/URL: https://doi.org/10.3390/children10030556. (chang2023genetictestingin pages 4-6)
4. Cavirani B et al. **Genetic Epilepsies and Developmental Epileptic Encephalopathies with Early Onset: A Multicenter Study.** *International Journal of Molecular Sciences.* Published January 2024;25:1248. DOI/URL: https://doi.org/10.3390/ijms25021248. (cavirani2024geneticepilepsiesand pages 2-4, cavirani2024geneticepilepsiesand pages 4-6)
5. Donnan AM et al. **Rates of Status Epilepticus and Sudden Unexplained Death in Epilepsy in People With Genetic DEEs.** *Neurology.* Published April 2023;100:e1712–e1722. DOI/URL: https://doi.org/10.1212/WNL.0000000000207080. (scheffer2024developmentalandepileptic pages 19-21)

### Representative exact abstract wording

Recent abstracts describe DEEs as “**severe neurodevelopmental disorders characterized by recurrent, usually early-onset, epileptic seizures accompanied by developmental impairment**” and emphasize that impairment is “**often related to both underlying genetic etiology and abnormal epileptiform activity**.” A 2024 longitudinal Dravet abstract concluded that the “**negative impact of epilepsy severity at baseline on long-term developmental outcomes highlights the importance of implementing early and focused therapies**.” These quotations support the dual-causation model and early-intervention rationale, but do not imply that seizure suppression alone normalizes development. (scheffer2024developmentalandepileptic pages 1-4, scheffer2024developmentalandepileptic pages 17-19)

**PMID note:** DOI URLs are supplied for reliable record resolution. PMIDs should be imported directly from PubMed during database ingestion rather than inferred where they were not explicitly present in the retrieved source metadata.

References

1. (scheffer2024developmentalandepileptic pages 1-4): Ingrid E. Scheffer, Sameer Zuberi, Heather C. Mefford, Renzo Guerrini, and Amy McTague. Developmental and epileptic encephalopathies. Nature reviews. Disease primers, 10 1:61, Sep 2024. URL: https://doi.org/10.1038/s41572-024-00546-6, doi:10.1038/s41572-024-00546-6. This article has 157 citations.

2. (chang2023genetictestingin pages 4-6): Yu-Tzu Chang, Syuan-Yu Hong, Wei-De Lin, Chien-Heng Lin, Sheng-Shing Lin, Fuu-Jen Tsai, and I-Ching Chou. Genetic testing in children with developmental and epileptic encephalopathies: a review of advances in epilepsy genomics. Children, 10:556, Mar 2023. URL: https://doi.org/10.3390/children10030556, doi:10.3390/children10030556. This article has 31 citations.

3. (specchio2024theexpandingfield pages 1-6): Nicola Specchio, Marina Trivisano, Eleonora Aronica, Simona Balestrini, Alexis Arzimanoglou, Gaia Colasante, J Helen Cross, Sergiusz Jozwiak, Jo M Wilmshurst, Federico Vigevano, Stéphane Auvin, Rima Nabbout, and Paolo Curatolo. The expanding field of genetic developmental and epileptic encephalopathies: current understanding and future perspectives. The Lancet. Child & adolescent health, 8 11:821-834, Nov 2024. URL: https://doi.org/10.1016/s2352-4642(24)00196-2, doi:10.1016/s2352-4642(24)00196-2. This article has 35 citations.

4. (scheffer2024developmentalandepileptic pages 9-11): Ingrid E. Scheffer, Sameer Zuberi, Heather C. Mefford, Renzo Guerrini, and Amy McTague. Developmental and epileptic encephalopathies. Nature reviews. Disease primers, 10 1:61, Sep 2024. URL: https://doi.org/10.1038/s41572-024-00546-6, doi:10.1038/s41572-024-00546-6. This article has 157 citations.

5. (scheffer2024developmentalandepileptic pages 19-21): Ingrid E. Scheffer, Sameer Zuberi, Heather C. Mefford, Renzo Guerrini, and Amy McTague. Developmental and epileptic encephalopathies. Nature reviews. Disease primers, 10 1:61, Sep 2024. URL: https://doi.org/10.1038/s41572-024-00546-6, doi:10.1038/s41572-024-00546-6. This article has 157 citations.

6. (cavirani2024geneticepilepsiesand pages 2-4): Benedetta Cavirani, Carlotta Spagnoli, Stefano Giuseppe Caraffi, Anna Cavalli, Carlo Alberto Cesaroni, Gianni Cutillo, Valentina De Giorgis, Daniele Frattini, Giulia Bruna Marchetti, Silvia Masnada, Angela Peron, Susanna Rizzi, Costanza Varesio, Luigina Spaccini, Aglaia Vignoli, Maria Paola Canevini, Pierangelo Veggiotti, Livia Garavelli, and Carlo Fusco. Genetic epilepsies and developmental epileptic encephalopathies with early onset: a multicenter study. International Journal of Molecular Sciences, 25:1248, Jan 2024. URL: https://doi.org/10.3390/ijms25021248, doi:10.3390/ijms25021248. This article has 24 citations.

7. (cavirani2024geneticepilepsiesand pages 4-6): Benedetta Cavirani, Carlotta Spagnoli, Stefano Giuseppe Caraffi, Anna Cavalli, Carlo Alberto Cesaroni, Gianni Cutillo, Valentina De Giorgis, Daniele Frattini, Giulia Bruna Marchetti, Silvia Masnada, Angela Peron, Susanna Rizzi, Costanza Varesio, Luigina Spaccini, Aglaia Vignoli, Maria Paola Canevini, Pierangelo Veggiotti, Livia Garavelli, and Carlo Fusco. Genetic epilepsies and developmental epileptic encephalopathies with early onset: a multicenter study. International Journal of Molecular Sciences, 25:1248, Jan 2024. URL: https://doi.org/10.3390/ijms25021248, doi:10.3390/ijms25021248. This article has 24 citations.

8. (specchio2024theexpandingfield pages 14-17): Nicola Specchio, Marina Trivisano, Eleonora Aronica, Simona Balestrini, Alexis Arzimanoglou, Gaia Colasante, J Helen Cross, Sergiusz Jozwiak, Jo M Wilmshurst, Federico Vigevano, Stéphane Auvin, Rima Nabbout, and Paolo Curatolo. The expanding field of genetic developmental and epileptic encephalopathies: current understanding and future perspectives. The Lancet. Child & adolescent health, 8 11:821-834, Nov 2024. URL: https://doi.org/10.1016/s2352-4642(24)00196-2, doi:10.1016/s2352-4642(24)00196-2. This article has 35 citations.

9. (sun2024strategiesfordissecting pages 14-15): Jiawan Sun, Serena Noss, Deepro Banerjee, Maitreya Das, and Santhosh Girirajan. Strategies for dissecting the complexity of neurodevelopmental disorders. Trends in Genetics, 40:187-202, Feb 2024. URL: https://doi.org/10.1016/j.tig.2023.10.009, doi:10.1016/j.tig.2023.10.009. This article has 11 citations and is from a domain leading peer-reviewed journal.

10. (scheffer2024developmentalandepileptic pages 17-19): Ingrid E. Scheffer, Sameer Zuberi, Heather C. Mefford, Renzo Guerrini, and Amy McTague. Developmental and epileptic encephalopathies. Nature reviews. Disease primers, 10 1:61, Sep 2024. URL: https://doi.org/10.1038/s41572-024-00546-6, doi:10.1038/s41572-024-00546-6. This article has 157 citations.

11. (specchio2024theexpandingfield pages 6-8): Nicola Specchio, Marina Trivisano, Eleonora Aronica, Simona Balestrini, Alexis Arzimanoglou, Gaia Colasante, J Helen Cross, Sergiusz Jozwiak, Jo M Wilmshurst, Federico Vigevano, Stéphane Auvin, Rima Nabbout, and Paolo Curatolo. The expanding field of genetic developmental and epileptic encephalopathies: current understanding and future perspectives. The Lancet. Child & adolescent health, 8 11:821-834, Nov 2024. URL: https://doi.org/10.1016/s2352-4642(24)00196-2, doi:10.1016/s2352-4642(24)00196-2. This article has 35 citations.

12. (NCT06112275 chunk 1):  A Clinical Study to Evaluate the Safety and Efficacy of ETX101, an AAV9-Delivered Gene Therapy in Children With SCN1A-positive Dravet Syndrome (Australia Only). Encoded Therapeutics. 2024. ClinicalTrials.gov Identifier: NCT06112275

13. (NCT06283212 chunk 1):  A Clinical Study to Evaluate the Safety and Efficacy of ETX101, an AAV9-Delivered Gene Therapy in Children With SCN1A-positive Dravet Syndrome. Encoded Therapeutics. 2024. ClinicalTrials.gov Identifier: NCT06283212

14. (NCT06983158 chunk 2):  A Clinical Trial of CAP-002 Gene Therapy in Pediatric Patients With Syntaxin-Binding Protein 1 (STXBP1) Encephalopathy. Capsida Biotherapeutics, Inc.. 2025. ClinicalTrials.gov Identifier: NCT06983158

15. (specchio2024theexpandingfield pages 17-21): Nicola Specchio, Marina Trivisano, Eleonora Aronica, Simona Balestrini, Alexis Arzimanoglou, Gaia Colasante, J Helen Cross, Sergiusz Jozwiak, Jo M Wilmshurst, Federico Vigevano, Stéphane Auvin, Rima Nabbout, and Paolo Curatolo. The expanding field of genetic developmental and epileptic encephalopathies: current understanding and future perspectives. The Lancet. Child & adolescent health, 8 11:821-834, Nov 2024. URL: https://doi.org/10.1016/s2352-4642(24)00196-2, doi:10.1016/s2352-4642(24)00196-2. This article has 35 citations.

16. (NCT02758626 chunk 1):  Ataluren for Nonsense Mutation in CDKL5 and Dravet Syndrome. NYU Langone Health. 2016. ClinicalTrials.gov Identifier: NCT02758626

17. (NCT02758626 chunk 2):  Ataluren for Nonsense Mutation in CDKL5 and Dravet Syndrome. NYU Langone Health. 2016. ClinicalTrials.gov Identifier: NCT02758626

18. (NCT06447675 chunk 1): Liankun_Ren. Efficacy and Safety Evaluation of Hyperthermic Baths in the Treatment of Seizures in CDKL5 Deficiency Disorder. Xuanwu Hospital, Beijing. 2024. ClinicalTrials.gov Identifier: NCT06447675

19. (NCT07602205 chunk 1): Liankun_Ren. Efficacy and Safety of Daily Home-based Hyperthermic Baths for Reducing Epileptic Seizures in CDKL5 Deficiency Disorder: A PROBE Clinical Trial. Xuanwu Hospital, Beijing. 2026. ClinicalTrials.gov Identifier: NCT07602205

## Artifacts

- [Edison artifact artifact-00](Genetic_Developmental_and_Epileptic_Encephalopathy-deep-research-falcon_artifacts/artifact-00.md)