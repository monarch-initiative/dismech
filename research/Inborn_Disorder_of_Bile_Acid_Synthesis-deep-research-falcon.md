---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-17T21:55:01.283239'
end_time: '2026-06-17T22:05:56.896950'
duration_seconds: 655.61
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Inborn Disorder of Bile Acid Synthesis
  mondo_id: ''
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 30
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Inborn_Disorder_of_Bile_Acid_Synthesis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Inborn Disorder of Bile Acid Synthesis
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Inborn Disorder of Bile Acid Synthesis** covering all of the
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
- **Disease Name:** Inborn Disorder of Bile Acid Synthesis
- **MONDO ID:**  (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Inborn Disorder of Bile Acid Synthesis** covering all of the
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


# Disease Characteristics Research Report: Inborn Disorder of Bile Acid Synthesis (IEBAS/IEBAM/BASD)

## Target Disease
- **Disease name (aggregate category):** Inborn disorder of bile acid synthesis / **Inborn errors of bile acid metabolism**
- **Common acronyms/synonyms in recent literature:**
  - **IEBAM/IEBAM** (“inborn errors of bile acid metabolism”) (nittono2024navigatingcholestasisidentifying pages 1-2)
  - **IEBAS** (“inborn errors of bile acid synthesis”) (obuz2019pathwaysandinborn pages 4-6)
  - **BASD/BASD** (“bile acid synthesis disorders”) (kimura2021bileacidsynthesis pages 1-5)
  - “inborn errors of bile acid synthesis and metabolism” (clinical trial terminology) (NCT00007020 chunk 1)
- **MONDO ID:** Not identified in the retrieved primary/secondary sources in this run (will require direct MONDO lookup outside the provided documents).
- **Category:** Rare inborn errors of metabolism (IEM) affecting hepatic bile acid synthesis/conjugation and, in some subtypes, peroxisomal bile-acid side-chain processing.

**Note on citation/PMID availability:** The retrieved full-text evidence provided DOIs and ClinicalTrials.gov NCT identifiers but did not reliably expose PubMed IDs (PMIDs) within the accessible text chunks; therefore, citations below use the provided context IDs and include URLs/dates when present.

---

## 1. Disease Information

### 1.1 Concise overview (current understanding)
“Inborn errors of bile acid metabolism” (IEBAM) are congenital genetic defects of enzymes required to synthesize the primary bile acids **cholic acid (CA)** and **chenodeoxycholic acid (CDCA)**, leading to cholestasis and/or systemic toxicity from accumulating atypical C27 bile acid intermediates (nittono2024navigatingcholestasisidentifying pages 1-2, nittono2024navigatingcholestasisidentifying pages 3-4). A major diagnostic pitfall is that patients can have **cholestasis despite normal/low serum total bile acids (STBA) and normal γ-glutamyltransferase (GGT)**, which can resemble or be confused with other neonatal cholestasis etiologies (nittono2024navigatingcholestasisidentifying pages 1-2, nittono2024navigatingcholestasisidentifying pages 3-4).

Nittono et al. (Frontiers in Pediatrics; **Apr 2024**; https://doi.org/10.3389/fped.2024.1385970) explicitly emphasizes that IEBAM causes neonatal cholestasis and “**accounts for approximately 2% of cases of cholestasis of unknown cause**” (nittono2024navigatingcholestasisidentifying pages 1-2).

### 1.2 Key identifiers and terminologies
**OMIM identifiers for key defect types and genes were available in the retrieved literature (but not ICD/Orphanet/MONDO):**
- **HSD3B7 deficiency** (3β-hydroxy-Δ5-C27-steroid dehydrogenase/isomerase deficiency): **OMIM 607765** (nittono2024navigatingcholestasisidentifying pages 1-2, kimura2021bileacidsynthesis pages 1-5)
- **SRD5B1 / AKR1D1 deficiency** (Δ4-3-oxosteroid 5β-reductase deficiency): **OMIM 235555** (nittono2024navigatingcholestasisidentifying pages 1-2, kimura2021bileacidsynthesis pages 1-5)
- **CYP7B1 deficiency** (oxysterol 7α-hydroxylase deficiency): **OMIM 603711** (nittono2024navigatingcholestasisidentifying pages 1-2, kimura2021bileacidsynthesis pages 1-5)
- **CYP27A1 (CTX)** sterol 27-hydroxylase deficiency: **OMIM 213700** (nittono2024navigatingcholestasisidentifying pages 1-2)
- Additional gene OMIMs available from a review table (Obuz & Lay 2019; Dec 2019; https://doi.org/10.32552/2019.actamedica.404): **AKR1D1 604741; CYP7A1 118455; SLC27A5 603314; BAAT 602938; AMACR 604489** (obuz2019pathwaysandinborn pages 4-6).

**MeSH terms (as represented in ClinicalTrials.gov metadata):** ClinicalTrials.gov record for compassionate CA treatment lists condition mappings including “Metabolism, Inborn Errors” and related peroxisomal disorder terms (NCT00007020 chunk 1).

**ICD-10/ICD-11 / Orphanet:** Not present in the retrieved evidence; would require dedicated lookup.

### 1.3 Synonyms/alternative names in practice
- “Congenital bile acid synthesis defect type 3” for CYP7B1 deficiency is used in case literature (Tang et al., BMC Gastroenterology; **Apr 2021**; https://doi.org/10.1186/s12876-021-01749-x) (chen2020akr1d1andcyp7b1 pages 1-2).
- “BASD type 4” used for **AMACR** deficiency in a recent case report (Cureus; **Jul 2023**; https://doi.org/10.7759/cureus.41720) (isa2023autoantibodypositivityin pages 1-2).

### 1.4 Evidence sources (patient-level vs aggregated)
- Much of the evidence base remains **case reports/series** and retrospective cohorts (e.g., Japanese cohort of 7 patients over 21 years; and AKR1D1 cohort of 16 patients) (kimura2021bileacidsynthesis pages 1-5, gardin2023∆43oxo5βreductasedeficiencyfavorable pages 1-2).
- A 2024 systematic review concluded that CA evidence is predominantly case reports/series with substantial bias risk (polak2024theclinicaland pages 5-6).

---

## 2. Etiology

### 2.1 Disease causal factors
Primary causal factors are **germline genetic variants** causing enzyme deficiencies in bile acid synthesis, conjugation/amidation, or peroxisomal side-chain processing pathways (nittono2024navigatingcholestasisidentifying pages 1-2, obuz2019pathwaysandinborn pages 4-6).

Representative genes explicitly listed for IEBAM include **HSD3B7, SRD5B1, CYP27A1, CYP7B1, BAAT, SLC27A5, AMACR, CYP7A1** (nittono2024navigatingcholestasisidentifying pages 1-2).

### 2.2 Risk factors
- **Genetic (causal):** autosomal recessive inheritance is explicitly stated for BASD (kimura2021bileacidsynthesis pages 1-5). Cohorts and case reports include homozygous/compound heterozygous variants (kimura2021bileacidsynthesis pages 1-5, chen2020akr1d1andcyp7b1 pages 1-2).
- **Environmental:** Not well characterized as “risk factors” for the monogenic disorders themselves in the retrieved sources; however, misdiagnosis risk is influenced by routine bile acid assays that only detect 3α-hydroxylated bile acids (nittono2024navigatingcholestasisidentifying pages 3-4).

### 2.3 Protective factors
Not established in the retrieved evidence. Some phenotypic variability is described (e.g., AKR1D1 mutation carriers without severe neonatal cholestasis) but protective variants or modifiers are not identified (kimura2023healthypatientswith pages 1-2).

### 2.4 Gene–environment interactions
Not directly addressed in the retrieved evidence for IEBAS/IEBAM.

---

## 3. Phenotypes

### 3.1 Core phenotype domain: neonatal/infantile cholestasis
Across IEBAM, hallmark lab patterns include:
- **Cholestasis** with **normal or low STBA** and **normal GGT** in many types (nittono2024navigatingcholestasisidentifying pages 1-2, nittono2024navigatingcholestasisidentifying pages 3-4).
- **Absence of pruritus** is highlighted as a clue in BASD (kimura2021bileacidsynthesis pages 1-5, gardin2023∆43oxo5βreductasedeficiencyfavorable pages 1-2).

Nittono et al. (Apr 2024) explicitly states: “Laboratory tests in IEBAM are characterized by **normal γ-glutamyltransferase (GGT) and serum total bile acid (STBA) levels despite the presence of cholestasis**” and that measuring STBA and GGT is essential for distinguishing biliary atresia from IEBAM (nittono2024navigatingcholestasisidentifying pages 3-4, nittono2024navigatingcholestasisidentifying pages 1-2).

**Example quantitative baseline (Japan cohort, n=7):** median direct bilirubin 4.5 mg/dL with median total bile acids 3.4 μmol/L (kimura2021bileacidsynthesis pages 16-19).

### 3.2 Nutritional/malabsorption phenotypes
Fat-soluble vitamin malabsorption/deficiency is emphasized as a clinical feature in BASD, and bleeding can occur:
- In AKR1D1 deficiency cohort (Δ4-3-oxo-R), **3/16** had severe bleeding as early manifestations (gardin2023∆43oxo5βreductasedeficiencyfavorable pages 1-2).

### 3.3 Neurologic and multi-system phenotypes (defect-dependent)
- **AMACR deficiency**: a 2024 cohort described adult-onset neurologic disease: “All adult patients subsequently developed neurological signs and symptoms after the age of 40 years; most frequently neuropathy, ataxia and cognitive decline…” (Orphanet J Rare Dis; **Sep 2024**; https://doi.org/10.1186/s13023-024-03358-9) (polak2024theclinicaland pages 5-6).
- **CYP7B1 deficiency**: phenotype can vary within siblings, with infantile liver disease in one and adolescent spastic paraplegia features in another (chen2020akr1d1andcyp7b1 pages 1-2).

### 3.4 Suggested HPO terms (examples)
(These are ontology suggestions; not all are explicitly asserted in the retrieved texts.)
- Cholestasis (**HP:0001396**)
- Neonatal jaundice (**HP:0006579**)
- Conjugated hyperbilirubinemia (**HP:0002904**)
- Elevated hepatic transaminases (**HP:0002910**)
- Fat malabsorption / steatorrhea (**HP:0002570**)
- Fat-soluble vitamin deficiency (**HP:0031034**; consider also vitamin K deficiency bleeding)
- Failure to thrive (**HP:0001508**)
- Normal gamma-glutamyltransferase in cholestasis (no single HPO term; can encode as “Cholestasis” + lab observation)
- Ataxia (**HP:0001251**), Peripheral neuropathy (**HP:0009830**), Cognitive decline (**HP:0001268**), Retinitis pigmentosa (**HP:0000510**) for AMACR deficiency.

### 3.5 Phenotype frequencies
Robust frequencies across the entire IEBAS category are not available in the retrieved evidence; however, subtype cohorts include:
- Δ4-3-oxo-R/AKR1D1 deficiency: 14/16 cholestatic jaundice; 3/16 bleeding; 4 had liver failure at CA start (gardin2023∆43oxo5βreductasedeficiencyfavorable pages 1-2).
- AMACR deficiency: retinitis pigmentosa in 5/9 adults (polak2024theclinicaland pages 5-6).

---

## 4. Genetic / Molecular Information

### 4.1 Causal genes (human germline)
Genes repeatedly identified across IEBAM/BASD include:
- **HSD3B7** (3β-HSD deficiency) (nittono2024navigatingcholestasisidentifying pages 1-2, kimura2021bileacidsynthesis pages 1-5)
- **SRD5B1 and/or AKR1D1** (Δ4-3-oxo-5β-reductase deficiency) (nittono2024navigatingcholestasisidentifying pages 1-2, gardin2023∆43oxo5βreductasedeficiencyfavorable pages 1-2)
- **CYP7B1** (oxysterol 7α-hydroxylase deficiency) (nittono2024navigatingcholestasisidentifying pages 1-2, chen2020akr1d1andcyp7b1 pages 1-2)
- **CYP27A1** (CTX) (nittono2024navigatingcholestasisidentifying pages 1-2)
- **BAAT (BACD1)** (bile acid conjugation defect-1) (nittono2024navigatingcholestasisidentifying pages 2-3)
- **SLC27A5** (bile acid-CoA ligase deficiency is listed as an IEBAM type) (nittono2024navigatingcholestasisidentifying pages 1-2)
- **AMACR** (BASD type 4) (isa2023autoantibodypositivityin pages 1-2)
- **CYP7A1** (cholesterol 7α-hydroxylase deficiency is listed as a type) (nittono2024navigatingcholestasisidentifying pages 1-2)

### 4.2 Variant types and examples
- In Japan BASD cohort, patients had “homozygous or compound heterozygous mutations” in **HSD3B7, SRD5B1, CYP7B1** (kimura2021bileacidsynthesis pages 1-5).
- A CYP7B1 case reported compound heterozygous nonsense mutations **p.R63X / p.R112X** (chen2020akr1d1andcyp7b1 pages 1-2).
- The Japan cohort tables include multiple variant notations across HSD3B7/SRD5B1/CYP7B1 (e.g., splice site, deletions, missense) (kimura2021bileacidsynthesis pages 16-19).

### 4.3 Functional consequences (mechanistic framing)
The core biochemical consequence is impaired formation of CA/CDCA, leading to:
1) reduced bile flow and fat absorption, and
2) accumulation of atypical “unusual” bile acids/intermediates (often C27 intermediates), some described as hepatotoxic (nittono2024navigatingcholestasisidentifying pages 3-4, kimura2021bileacidsynthesis pages 7-11).

---

## 5. Environmental Information
IEBAS/IEBAM are primarily monogenic disorders; specific environmental toxins/lifestyle factors are not established causes in the retrieved sources. However, **pre-analytical handling of samples** (cooling and rapid processing) is highlighted as important to avoid oxidation artifacts that could confound diagnosis (nittono2024navigatingcholestasisidentifying pages 3-4).

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (general)
A synthesized mechanistic chain supported by retrieved sources is:
- **Inherited enzyme deficiency** in bile acid synthesis/conjugation → **low/absent primary bile acids (CA/CDCA)** and **accumulation of unusual bile acids (including non-3αOH bile acids)** → impaired bile formation/flow and fat-soluble vitamin absorption + direct hepatotoxic effects of intermediates → **cholestasis**, progressive liver injury/fibrosis, and (in some subtypes) neurologic sequelae from systemic metabolite accumulation (nittono2024navigatingcholestasisidentifying pages 3-4, gardin2023∆43oxo5βreductasedeficiencyfavorable pages 1-2, polak2024theclinicaland pages 5-6).

Nittono et al. emphasize that routine STBA assays measure only 3αOH bile acids and can miss IEBAM, underscoring the biochemical distinctiveness of the accumulated metabolites (nittono2024navigatingcholestasisidentifying pages 3-4).

### 6.2 Upstream vs downstream mechanisms
- **Upstream:** enzyme deficits in steroid/bile acid biosynthetic pathway (HSD3B7, AKR1D1/SRD5B1, CYP7B1, etc.) (nittono2024navigatingcholestasisidentifying pages 1-2).
- **Downstream:** cholestasis with “normal GGT and normal STBA despite cholestasis,” fat-soluble vitamin deficiency and bleeding, fibrosis (nittono2024navigatingcholestasisidentifying pages 1-2, gardin2023∆43oxo5βreductasedeficiencyfavorable pages 1-2).

### 6.3 Suggested pathway and ontology terms
- **GO Biological Process (suggested):** bile acid biosynthetic process (GO:0006699); cholesterol metabolic process (GO:0008203); lipid digestion/absorption-related processes.
- **Cell types (CL; suggested):** hepatocyte (CL:0000182); cholangiocyte (CL:0000068).

---

## 7. Anatomical Structures Affected

### 7.1 Primary organs
- **Liver** (primary; cholestasis, fibrosis, liver failure) (gardin2023∆43oxo5βreductasedeficiencyfavorable pages 1-2, nittono2024navigatingcholestasisidentifying pages 3-4).
- **Intestine** (secondary; fat absorption and enterohepatic circulation disruption; vitamin malabsorption) (NCT01115582 chunk 1, NCT01589523 chunk 1).

### 7.2 Secondary organ involvement (defect-dependent)
- **Central/peripheral nervous system** in certain defects (e.g., AMACR neurologic phenotype; CYP7B1 spastic paraplegia association) (polak2024theclinicaland pages 5-6, chen2020akr1d1andcyp7b1 pages 1-2).
- **Eye/retina** in AMACR deficiency (retinitis pigmentosa) (polak2024theclinicaland pages 5-6).

### 7.3 UBERON suggestions
- Liver (**UBERON:0002107**)
- Intrahepatic bile duct (**UBERON:0003704**)
- Small intestine (**UBERON:0002108**)
- Retina (**UBERON:0000966**) (AMACR)

---

## 8. Temporal Development

### 8.1 Onset
- Many IEBAM present in the **neonatal/early infancy period** (nittono2024navigatingcholestasisidentifying pages 1-2, gardin2023∆43oxo5βreductasedeficiencyfavorable pages 1-2).
- Δ4-3-oxo-R deficiency cohort: median first symptoms **2 months** (gardin2023∆43oxo5βreductasedeficiencyfavorable pages 1-2).

### 8.2 Progression
Without appropriate bile acid replacement, disorders may progress to cirrhosis/liver failure; case series highlight need for timely therapy and/or transplantation in severe infantile phenotypes (NCT01115582 chunk 1, chen2020akr1d1andcyp7b1 pages 1-2).

AMACR deficiency can have **adult slowly progressive** neurologic course with late diagnosis (median 56 years in one cohort) (polak2024theclinicaland pages 5-6).

---

## 9. Inheritance and Population

### 9.1 Inheritance
Autosomal recessive inheritance is described for BASD (kimura2021bileacidsynthesis pages 1-5).

### 9.2 Epidemiology and underdiagnosis
- **IEBAM proportion among unexplained cholestasis:** approximately **2%** (nittono2024navigatingcholestasisidentifying pages 1-2).
- **Japan cohort screening-based estimate:** among **1010 infants with unexplained cholestasis (1996–2017)**, BASD prevalence was **0.7%** (kimura2021bileacidsynthesis pages 5-7).
- **Underdiagnosis evidence:** a Taiwanese cohort notes possible underdiagnosis and provides a control allele frequency for a CYP7B1 variant (p.R112X) of **0.16% (2/1216 alleles)** in 608 controls (chen2020akr1d1andcyp7b1 pages 1-2).

### 9.3 Demographics
The retrieved evidence includes regional observations (Japan: only 10 identified IEBAM cases in one clinic’s experience, supporting rarity and diagnostic challenge) (nittono2024navigatingcholestasisidentifying pages 1-2, nittono2024navigatingcholestasisidentifying pages 2-3).

---

## 10. Diagnostics

### 10.1 Core diagnostic strategy
A recurring recommended workflow in the retrieved sources:
1) In neonatal/infantile cholestasis, check **direct bilirubin, GGT, and STBA** early; normal GGT and normal/low STBA raise suspicion for IEBAM and may help avoid unnecessary invasive procedures intended for biliary atresia (nittono2024navigatingcholestasisidentifying pages 1-2, nittono2024navigatingcholestasisidentifying pages 2-3).
2) Perform **urinary bile acid profiling by LC–MS or GC–MS**, as routine enzymatic STBA assays may miss non-3αOH bile acids (nittono2024navigatingcholestasisidentifying pages 3-4).
3) Confirm with **genetic testing** (targeted sequencing/NGS panels/WES) (nittono2024navigatingcholestasisidentifying pages 3-4, chen2020akr1d1andcyp7b1 pages 1-2).

**Direct quote (abstract-level, Frontiers in Pediatrics 2024):** “With suspected IEBAM, **liquid chromatography–mass spectrometry (LC/MS) analysis of urinary bile acids is needed**…” (nittono2024navigatingcholestasisidentifying pages 1-2).

### 10.2 Diagnostic tests and biomarkers
- **Urinary bile acid profiling (LC–MS / GC–MS):** key test; detects unusual bile acids and supports subtype inference (nittono2024navigatingcholestasisidentifying pages 3-4, nittono2024navigatingcholestasisidentifying pages 2-3).
- **Serum/urine ‘unusual bile acid’ fractions:** in Japan cohort, unusual bile acids often comprised the majority of measured bile acids at baseline in certain defects (e.g., 87.5–100% in 3β-HSD deficiency) (kimura2021bileacidsynthesis pages 5-7).
- **Impact of UDCA on profiles:** UDCA can markedly alter bile-acid profiles; recommendation to measure STBA after stopping UDCA (nittono2024navigatingcholestasisidentifying pages 4-5, nittono2024navigatingcholestasisidentifying pages 3-4).

### 10.3 Differential diagnosis
- **Biliary atresia** is specifically discussed as a key differential; BA typically has elevated STBA/GGT and requires prompt surgery (nittono2024navigatingcholestasisidentifying pages 2-3).

### 10.4 Screening
Newborn screening is described as “emerging” via dried blood spot bile acid metabolite detection (nittono2024navigatingcholestasisidentifying pages 5-6).

---

## 11. Outcome / Prognosis

### 11.1 Prognosis with treatment
- **Δ4-3-oxo-R (AKR1D1/SRD5B1) treated with CA (n=16):** all were alive with native liver after median 4.5 years; liver tests normalized within 6–12 months; fibrosis stabilized/improved (gardin2023∆43oxo5βreductasedeficiencyfavorable pages 1-2).
- **Japan cohort (n=7) treated largely with long-term CDCA (because CA unavailable):** “All 7 patients… are currently in good health without liver dysfunction.” (Digestive Diseases and Sciences; **Jan 2021**; https://doi.org/10.1007/s10620-020-06722-4) (kimura2021bileacidsynthesis pages 1-5).

### 11.2 Prognosis without treatment / severe disease
The ClinicalTrials.gov description notes that inborn errors “are progressive and potentially lead to cirrhosis and liver failure if untreated” (NCT01115582 chunk 1).

### 11.3 Quality of life
The AKR1D1/SRD5B1 cohort explicitly reports “normal growth and quality of life” on CA (gardin2023∆43oxo5βreductasedeficiencyfavorable pages 1-2).

---

## 12. Treatment

### 12.1 Standard disease-modifying approach: primary bile acid replacement
**Cholic acid (CA)** and **chenodeoxycholic acid (CDCA)** are the primary replacement therapies used to restore bile acid pool, promote bile flow, suppress endogenous synthesis of toxic intermediates, and improve fat-soluble vitamin absorption (NCT01115582 chunk 1, nittono2024navigatingcholestasisidentifying pages 3-4).

**Direct quote (ClinicalTrials.gov NCT01115582):** patients “lack the enzymes needed to synthesize the primary bile acids cholic acid and chenodeoxycholic acid (CDCA)” and CA monotherapy “inhibits endogenous production and accumulation of potentially hepatotoxic and cholestatic bile acid precursors” (NCT01115582 chunk 1).

#### Evidence-based dosing and outcomes
- **CA dosing in Phase 3 bridge trial:** **10–15 mg/kg/day** oral, divided doses (NCT01115582; completed; enrollment 16) (NCT01115582 chunk 1).
- **CA outcomes in Δ4-3-oxo-R deficiency (n=16; Orphanet J Rare Dis; Dec 2023; https://doi.org/10.1186/s13023-023-02984-z):**
  - liver tests normalized in all within **6–12 months**
  - median CA at last follow-up **8.3 mg/kg/day**
  - all alive with native liver after median **4.5 years**
  - **12-fold** decrease of urinary 3-oxo-Δ4 derivatives (gardin2023∆43oxo5βreductasedeficiencyfavorable pages 1-2)

- **CDCA dosing in Japan cohort (n=5 treated):** “low-dose (5 to 10 mg/kg/day)” with improved hepatic function and “No adverse effects were noted” (kimura2021bileacidsynthesis pages 1-5).

- **Systematic review of CA (Orphanet J Rare Dis; Dec 2024; https://doi.org/10.1186/s13023-024-03449-7):** 14 publications, **162 total patients**, but concluded “More controlled studies are required” and highlights heterogeneity/bias (polak2024theclinicaland pages 5-6).

### 12.2 Conjugated bile acids for amidation/conjugation defects
- **Glycocholic acid** trial (NCT01589523; completed; enrollment 5) used **10–15 mg/kg/day** in bile acid conjugation/amidation defects and collected liver tests, bile acid profiles, vitamin absorption, growth and histology endpoints (NCT01589523 chunk 1).

### 12.3 Alternative bile acids (emerging/experimental)
- A 2024 case report (Frontiers in Pediatrics; Jun 2024; https://doi.org/10.3389/fped.2024.1418963) described glycine-conjugated deoxycholic acid (gDCA) as “alternative treatment” in HSD3B7 deficiency with improved weight and restored bile acid levels (kimura2021bileacidsynthesis pages 1-5).

### 12.4 Liver transplantation
Used for severe progressive infantile liver failure (e.g., oxysterol 7α-hydroxylase deficiency in Japan cohort; post-transplant bile acids normalized) (kimura2021bileacidsynthesis pages 1-5, kimura2021bileacidsynthesis pages 16-19).

### 12.5 Real-world implementation considerations
- Misdiagnosis avoidance: STBA/GGT plus urinary LC–MS testing can prevent unnecessary invasive cholangiography intended for biliary atresia (nittono2024navigatingcholestasisidentifying pages 2-3).
- Medication access: Japan cohort highlights lack of CA availability and pragmatic reliance on CDCA (kimura2021bileacidsynthesis pages 1-5).

### 12.6 MAXO (suggested) terms
- Primary bile acid replacement therapy (e.g., **MAXO: bile acid replacement therapy**; terminology may vary)
- Cholic acid therapy
- Chenodeoxycholic acid therapy
- Liver transplantation
- Fat-soluble vitamin supplementation

---

## 13. Prevention
Primary prevention of the monogenic disorders is not addressed directly in the retrieved sources. Secondary/tertiary prevention is implicitly supported by:
- early biochemical suspicion (STBA/GGT) and confirmatory bile acid profiling (nittono2024navigatingcholestasisidentifying pages 1-2, nittono2024navigatingcholestasisidentifying pages 3-4)
- early initiation of bile acid replacement to prevent progression to liver failure and long-term complications (NCT01115582 chunk 1, gardin2023∆43oxo5βreductasedeficiencyfavorable pages 1-2).

---

## 14. Other Species / Natural Disease
Not established for this disease category in the retrieved evidence.

---

## 15. Model Organisms
Model organism evidence for these specific disorders was not retrieved in a form that directly supports disease-mechanism statements in this run; therefore, no curated model-organism summary is provided here.

---

# Summary Tables

| Defect / type | Gene | OMIM in evidence | Typical presentation notes | Key diagnostic test | Typical treatment | Key quantitative outcomes / doses |
|---|---|---|---|---|---|---|
| Aggregate concept: inborn disorders of bile acid synthesis/metabolism; synonyms include IEBAM, IEBAS, BASD (nittono2024navigatingcholestasisidentifying pages 1-2, kimura2021bileacidsynthesis pages 1-5, NCT00007020 chunk 1) | Multiple: HSD3B7, SRD5B1/AKR1D1, CYP7B1, CYP27A1, BAAT, SLC27A5, AMACR, CYP7A1 (nittono2024navigatingcholestasisidentifying pages 1-2, obuz2019pathwaysandinborn pages 4-6) | HSD3B7 607765; SRD5B1 235555; CYP27A1 213700; CYP7B1 603711; BAAT/BACD1 619232; AMACR 604489; additional gene OMIMs in evidence include AKR1D1 604741, CYP7A1 118455, SLC27A5 603314 (nittono2024navigatingcholestasisidentifying pages 1-2, obuz2019pathwaysandinborn pages 4-6, nittono2024navigatingcholestasisidentifying pages 2-3) | Usually neonatal/infantile cholestasis with normal or low GGT and normal/low serum total bile acids; often absent pruritus; fat-soluble vitamin deficiency/bleeding; some defects later show neurologic disease (nittono2024navigatingcholestasisidentifying pages 3-4, kimura2023healthypatientswith pages 1-2, gardin2023∆43oxo5βreductasedeficiencyfavorable pages 1-2) | Urinary bile acid profiling by LC-MS or GC-MS plus confirmatory genetic testing; STBA and GGT help distinguish from biliary atresia; newborn dried-blood-spot metabolite screening is emerging (nittono2024navigatingcholestasisidentifying pages 3-4, nittono2024navigatingcholestasisidentifying pages 5-6, nittono2024navigatingcholestasisidentifying pages 2-3) | Primary bile acid replacement, mainly cholic acid or chenodeoxycholic acid; defect-specific exceptions apply; liver transplantation for severe failure (nittono2024navigatingcholestasisidentifying pages 3-4, NCT01115582 chunk 1, gardin2023∆43oxo5βreductasedeficiencyfavorable pages 1-2) | IEBAM may account for ~2% of cholestasis of unknown cause; open-label cholic acid trials used 10–15 mg/kg/day; Japanese BASD prevalence among 1010 unexplained cholestasis cases was 0.7% (nittono2024navigatingcholestasisidentifying pages 1-2, NCT01115582 chunk 1, kimura2021bileacidsynthesis pages 5-7) |
| 3β-hydroxy-Δ5-C27-steroid dehydrogenase/isomerase deficiency (3β-HSD deficiency) (nittono2024navigatingcholestasisidentifying pages 1-2, kimura2021bileacidsynthesis pages 1-5) | HSD3B7 (nittono2024navigatingcholestasisidentifying pages 1-2, kimura2021bileacidsynthesis pages 16-19) | 607765 in evidence (nittono2024navigatingcholestasisidentifying pages 1-2, kimura2021bileacidsynthesis pages 1-5) | Cholestatic jaundice, acholic/fatty stools, failure to thrive, fat-soluble vitamin deficiency; often low/normal GGT and low/normal STBA (nittono2024navigatingcholestasisidentifying pages 2-3, nittono2024navigatingcholestasisidentifying pages 3-4, gardin2023∆43oxo5βreductasedeficiencyfavorable pages 1-2) | Urine/serum bile acid profiling showing high atypical 3β-hydroxy-Δ5 bile acids; sequencing of HSD3B7 (nittono2024navigatingcholestasisidentifying pages 2-3, nittono2024navigatingcholestasisidentifying pages 3-4) | Cholic acid standard; alternative bile acid approaches reported when needed, including glycodeoxycholic acid case use (NCT01115582 chunk 1, NCT01589523 chunk 1, gardin2023∆43oxo5βreductasedeficiencyfavorable pages 1-2) | In long-term CA cohort including 13 HSD3B7 patients, mean daily CA dose 6.9 mg/kg/day and fibrosis improved/disappeared after 10–24 years; gDCA case restored normal bile acid levels and improved weight without liver toxicity (gardin2023∆43oxo5βreductasedeficiencyfavorable pages 1-2, kimura2021bileacidsynthesis pages 1-5) |
| Δ4-3-oxosteroid 5β-reductase deficiency (5β-reductase deficiency; Δ4-3-oxo-R) (gardin2023∆43oxo5βreductasedeficiencyfavorable pages 1-2, kimura2021bileacidsynthesis pages 1-5) | SRD5B1 / AKR1D1 (nittono2024navigatingcholestasisidentifying pages 1-2, kimura2021bileacidsynthesis pages 1-5, kimura2021bileacidsynthesis pages 16-19) | 235555 for disorder; AKR1D1 gene OMIM 604741 in evidence set (nittono2024navigatingcholestasisidentifying pages 1-2, obuz2019pathwaysandinborn pages 4-6) | Usually severe neonatal cholestasis, sometimes severe bleeding and liver failure; can be variable, including minimally symptomatic mutation carriers; pruritus often absent; GGT/TBA often normal or slightly raised (kimura2023healthypatientswith pages 1-2, gardin2023∆43oxo5βreductasedeficiencyfavorable pages 1-2) | Urinary bile acid LC-MS/GC-MS showing 3-oxo-Δ4 derivatives and allo-bile acids; AKR1D1/SRD5B1 sequencing (kimura2023healthypatientswith pages 1-2, gardin2023∆43oxo5βreductasedeficiencyfavorable pages 1-2) | Cholic acid preferred; UDCA may partially improve before diagnosis; some Japanese patients treated long-term with CDCA where CA unavailable (gardin2023∆43oxo5βreductasedeficiencyfavorable pages 1-2, kimura2021bileacidsynthesis pages 5-7) | In 16 CA-treated patients: median onset 2 months, CA started median 8.1 months, liver tests normalized in all within 6–12 months, median last dose 8.3 mg/kg/day, 12-fold urinary metabolite decrease, all alive with native liver after median 4.5 years; 15/16 had prior UDCA with partial improvement in 8 (gardin2023∆43oxo5βreductasedeficiencyfavorable pages 1-2) |
| Oxysterol 7α-hydroxylase deficiency / congenital bile acid synthesis defect type 3 (nittono2024navigatingcholestasisidentifying pages 1-2, kimura2021bileacidsynthesis pages 1-5) | CYP7B1 (nittono2024navigatingcholestasisidentifying pages 1-2, kimura2021bileacidsynthesis pages 16-19) | 603711 in evidence (nittono2024navigatingcholestasisidentifying pages 1-2, kimura2021bileacidsynthesis pages 1-5) | Severe infantile progressive cholestasis/liver failure in infancy; can also present later with hereditary spastic paraplegia phenotype, even within the same family (chen2020akr1d1andcyp7b1 pages 1-2) | Urinary bile acid analysis showing atypical hepatotoxic 3β-hydroxy-Δ5 bile acids; CYP7B1 genetic testing (chen2020akr1d1andcyp7b1 pages 1-2, nittono2024navigatingcholestasisidentifying pages 2-3) | Chenodeoxycholic acid; liver transplantation when progressive failure is advanced (chen2020akr1d1andcyp7b1 pages 1-2, kimura2021bileacidsynthesis pages 16-19) | Case evidence: CDCA begun while awaiting transplant led to rapid liver improvement and normalized urine atypical bile acids by follow-up at 23 months; in Japanese cohort 1 patient required liver transplantation and later recovered (chen2020akr1d1andcyp7b1 pages 1-2, kimura2021bileacidsynthesis pages 16-19) |
| α-Methylacyl-CoA racemase deficiency / BASD type 4 (isa2023autoantibodypositivityin pages 1-2) | AMACR (isa2023autoantibodypositivityin pages 1-2) | 604489 in evidence (nittono2024navigatingcholestasisidentifying pages 2-3) | Neonatal cholestasis or later slowly progressive adult neurologic disease with retinitis pigmentosa, neuropathy, ataxia, cognitive decline; risk of liver fibrosis/cirrhosis/HCC (isa2023autoantibodypositivityin pages 1-2, polak2024theclinicaland pages 5-6) | Urine metabolite testing and/or serum C27 bile acid intermediates with genetic confirmation; MRI may support adult diagnosis (isa2023autoantibodypositivityin pages 1-2, polak2024theclinicaland pages 5-6) | Oral cholic acid plus diet modification reported; CA also represented in systematic review data (isa2023autoantibodypositivityin pages 1-2, polak2024theclinicaland pages 5-6) | Fewer than 20 cases in prior literature; 2024 cohort described 12 genetically confirmed patients, median diagnosis age 56 years, mean follow-up 6 years, retinitis pigmentosa in 5/9 adults, neurologic symptoms in all adults after age 40 (polak2024theclinicaland pages 5-6) |
| Sterol 27-hydroxylase deficiency / cerebrotendinous xanthomatosis (CTX) (nittono2024navigatingcholestasisidentifying pages 1-2, obuz2019pathwaysandinborn pages 4-6) | CYP27A1 (nittono2024navigatingcholestasisidentifying pages 1-2) | 213700 in evidence (nittono2024navigatingcholestasisidentifying pages 1-2) | Systemic disease with bile acid deficiency and cholestanol/bile alcohol accumulation; neurologic sequelae dominate, rather than neonatal cholestasis in most cases (nittono2024navigatingcholestasisidentifying pages 1-2, polak2024theclinicaland pages 5-6) | Biochemical profiling of cholestanol/bile alcohols and genetic testing (polak2024theclinicaland pages 5-6) | Chenodeoxycholic acid standard in CTX; CA represented in systematic review but defect-specific standard remains CDCA (polak2024theclinicaland pages 5-6) | CA systematic review included 22 CTX patients; separate cohort evidence for CDCA shows long-term biochemical and clinical improvement in many patients (polak2024theclinicaland pages 5-6) |
| Bile acid amidation / conjugation defects (bile acid conjugation defect-1) (nittono2024navigatingcholestasisidentifying pages 2-3, obuz2019pathwaysandinborn pages 4-6) | BAAT; related ligase defect SLC27A5 (nittono2024navigatingcholestasisidentifying pages 2-3, obuz2019pathwaysandinborn pages 4-6) | BACD1/BAAT 619232; SLC27A5 gene OMIM 603314 in evidence (nittono2024navigatingcholestasisidentifying pages 2-3, obuz2019pathwaysandinborn pages 4-6) | Neonatal cholestasis with fat-soluble vitamin malabsorption; unconjugated bile acids and compensatory urinary sulfate/glucuronide conjugates; GGT may remain normal (nittono2024navigatingcholestasisidentifying pages 4-5, nittono2024navigatingcholestasisidentifying pages 2-3) | Specialized bile acid profiling showing unamidated bile acids; confirmatory sequencing (obuz2019pathwaysandinborn pages 4-6, nittono2024navigatingcholestasisidentifying pages 2-3) | Glycocholic acid/conjugated cholic acid; UDCA may be considered in some related defects (NCT01589523 chunk 1, nittono2024navigatingcholestasisidentifying pages 3-4) | Phase 3 glycocholic acid study enrolled 5 patients and used 10–15 mg/kg/day, with outcomes including liver tests, bile acid profiles, vitamin absorption, growth, and histology (NCT01589523 chunk 1) |


*Table: This table summarizes the main inborn bile acid synthesis/metabolism defects represented in the retrieved evidence, including genes, OMIM identifiers, presentations, diagnostics, treatments, and key quantitative outcomes. It is useful as a compact reference for comparing subtype-specific clinical and management features.*

---

# Recent developments (2023–2024) highlighted
1) **Precision diagnosis emphasis**: 2024 perspective stresses STBA/GGT patterns and urinary LC–MS bile acid profiling to distinguish IEBAM from biliary atresia and to avoid invasive procedures (nittono2024navigatingcholestasisidentifying pages 3-4, nittono2024navigatingcholestasisidentifying pages 2-3).
2) **Larger contemporary single-defect cohort**: 2023 Orphanet J Rare Dis cohort (n=16) provides quantitative CA effectiveness/safety for Δ4-3-oxo-R deficiency (gardin2023∆43oxo5βreductasedeficiencyfavorable pages 1-2).
3) **Evidence synthesis and evidence gaps**: 2024 systematic review (162 patients, mostly case series) concludes controlled studies and an independent international registry are needed (polak2024theclinicaland pages 5-6).
4) **Phenotype expansion**: 2024 AMACR cohort “redefining phenotype” indicates adult slowly progressive neuro-ophthalmologic pattern and liver cancer risk requiring monitoring (polak2024theclinicaland pages 5-6).



References

1. (nittono2024navigatingcholestasisidentifying pages 1-2): Hiroshi Nittono, Mitsuyoshi Suzuki, Hiromi Suzuki, Satoru Sugimoto, Jun Mori, Rieko Sakamoto, Yugo Takaki, Hisamitsu Hayashi, Hajime Takei, and Akihiko Kimura. Navigating cholestasis: identifying inborn errors of bile acid metabolism for precision diagnosis. Frontiers in Pediatrics, Apr 2024. URL: https://doi.org/10.3389/fped.2024.1385970, doi:10.3389/fped.2024.1385970. This article has 5 citations.

2. (obuz2019pathwaysandinborn pages 4-6): Ufuk Bozkurt Obuz and Incilay Lay. Pathways and inborn errors of bile acid synthesis. Acta Medica, 50:48-56, Dec 2019. URL: https://doi.org/10.32552/2019.actamedica.404, doi:10.32552/2019.actamedica.404. This article has 0 citations.

3. (kimura2021bileacidsynthesis pages 1-5): Akihiko Kimura, Tatsuki Mizuochi, Hajime Takei, Akira Ohtake, Jun Mori, Kunihiro Shinoda, Takuji Hashimoto, Mureo Kasahara, Takao Togawa, Tsuyoshi Murai, Takashi Iida, and Hiroshi Nittono. Bile acid synthesis disorders in japan: long-term outcome and chenodeoxycholic acid treatment. Jan 2021. URL: https://doi.org/10.1007/s10620-020-06722-4, doi:10.1007/s10620-020-06722-4. This article has 20 citations and is from a peer-reviewed journal.

4. (NCT00007020 chunk 1):  Compassionate Treatment of Patients With Inborn Errors of Bile Acid Metabolism With Cholic Acid. Mirum Pharmaceuticals, Inc.. 1992. ClinicalTrials.gov Identifier: NCT00007020

5. (nittono2024navigatingcholestasisidentifying pages 3-4): Hiroshi Nittono, Mitsuyoshi Suzuki, Hiromi Suzuki, Satoru Sugimoto, Jun Mori, Rieko Sakamoto, Yugo Takaki, Hisamitsu Hayashi, Hajime Takei, and Akihiko Kimura. Navigating cholestasis: identifying inborn errors of bile acid metabolism for precision diagnosis. Frontiers in Pediatrics, Apr 2024. URL: https://doi.org/10.3389/fped.2024.1385970, doi:10.3389/fped.2024.1385970. This article has 5 citations.

6. (chen2020akr1d1andcyp7b1 pages 1-2): Ju-Yin Chen, Jia-Feng Wu, Akihiko Kimura, Hiroshi Nittono, Bang-Yu Liou, Chee-Seng Lee, Ho-Sheng Chen, Yu-Chun Chiu, Yen-Hsuan Ni, Steven Shinn-Forng Peng, Wang-Tso Lee, I-Jung Tsai, Mei-Hwei Chang, and Huey-Ling Chen. Akr1d1 and cyp7b1 mutations in patients with inborn errors of bile acid metabolism: possibly underdiagnosed diseases. Pediatrics and neonatology, 61:75-83, Feb 2020. URL: https://doi.org/10.1016/j.pedneo.2019.06.009, doi:10.1016/j.pedneo.2019.06.009. This article has 31 citations and is from a peer-reviewed journal.

7. (isa2023autoantibodypositivityin pages 1-2): Hasan M Isa, Ahmed D Khudair, Rachel A Marshall, Aiman D Khudair, Thuraiya H Al-Rawahia, and Maryam Y Busehail. Autoantibody positivity in two bahraini siblings with a novel alpha-methylacyl-coa racemase mutation. Cureus, Jul 2023. URL: https://doi.org/10.7759/cureus.41720, doi:10.7759/cureus.41720. This article has 1 citations.

8. (gardin2023∆43oxo5βreductasedeficiencyfavorable pages 1-2): Antoine Gardin, Mathias Ruiz, Jan Beime, Mara Cananzi, Margarete Rathert, Barbara Rohmer, Enke Grabhorn, Marion Almes, Veena Logarajah, Luis Peña-Quintana, Thomas Casswall, Amaria Darmellah-Remil, Ana Reyes-Domínguez, Emna Barkaoui, Loreto Hierro, Carolina Baquero-Montoya, Ulrich Baumann, Björn Fischler, Emmanuel Gonzales, Anne Davit-Spraul, Sophie Laplanche, and Emmanuel Jacquemin. ∆4-3-oxo-5β-reductase deficiency: favorable outcome in 16 patients treated with cholic acid. Orphanet Journal of Rare Diseases, Dec 2023. URL: https://doi.org/10.1186/s13023-023-02984-z, doi:10.1186/s13023-023-02984-z. This article has 9 citations and is from a peer-reviewed journal.

9. (polak2024theclinicaland pages 5-6): Yasmin Polak, Laura van Dussen, E. Marleen Kemper, Frédéric M. Vaz, Femke C. C. Klouwer, Marc Engelen, and Carla E. M. Hollak. The clinical and biochemical effectiveness and safety of cholic acid treatment for bile acid synthesis defects: a systematic review. Orphanet Journal of Rare Diseases, Dec 2024. URL: https://doi.org/10.1186/s13023-024-03449-7, doi:10.1186/s13023-024-03449-7. This article has 8 citations and is from a peer-reviewed journal.

10. (kimura2023healthypatientswith pages 1-2): Akihiko Kimura, Jun Mori, Anh-Hoa Nguyen Pham, Kim-Oanh Bui Thi, Hajime Takei, Tsuyoshi Murai, Hisamitsu Hayashi, and Hiroshi Nittono. Healthy patients with akr1d1 mutation not requiring primary bile acid therapy: a case series. JPGN Reports, 4:e372-e372, Oct 2023. URL: https://doi.org/10.1097/pg9.0000000000000372, doi:10.1097/pg9.0000000000000372. This article has 5 citations.

11. (kimura2021bileacidsynthesis pages 16-19): Akihiko Kimura, Tatsuki Mizuochi, Hajime Takei, Akira Ohtake, Jun Mori, Kunihiro Shinoda, Takuji Hashimoto, Mureo Kasahara, Takao Togawa, Tsuyoshi Murai, Takashi Iida, and Hiroshi Nittono. Bile acid synthesis disorders in japan: long-term outcome and chenodeoxycholic acid treatment. Jan 2021. URL: https://doi.org/10.1007/s10620-020-06722-4, doi:10.1007/s10620-020-06722-4. This article has 20 citations and is from a peer-reviewed journal.

12. (nittono2024navigatingcholestasisidentifying pages 2-3): Hiroshi Nittono, Mitsuyoshi Suzuki, Hiromi Suzuki, Satoru Sugimoto, Jun Mori, Rieko Sakamoto, Yugo Takaki, Hisamitsu Hayashi, Hajime Takei, and Akihiko Kimura. Navigating cholestasis: identifying inborn errors of bile acid metabolism for precision diagnosis. Frontiers in Pediatrics, Apr 2024. URL: https://doi.org/10.3389/fped.2024.1385970, doi:10.3389/fped.2024.1385970. This article has 5 citations.

13. (kimura2021bileacidsynthesis pages 7-11): Akihiko Kimura, Tatsuki Mizuochi, Hajime Takei, Akira Ohtake, Jun Mori, Kunihiro Shinoda, Takuji Hashimoto, Mureo Kasahara, Takao Togawa, Tsuyoshi Murai, Takashi Iida, and Hiroshi Nittono. Bile acid synthesis disorders in japan: long-term outcome and chenodeoxycholic acid treatment. Jan 2021. URL: https://doi.org/10.1007/s10620-020-06722-4, doi:10.1007/s10620-020-06722-4. This article has 20 citations and is from a peer-reviewed journal.

14. (NCT01115582 chunk 1):  Efficacy of To Be Marketed (TBM) Cholic Acid Capsules Used to Treat Children With Inborn Errors of Bile Acid Synthesis. Mirum Pharmaceuticals, Inc.. 2010. ClinicalTrials.gov Identifier: NCT01115582

15. (NCT01589523 chunk 1):  GlycoCholic Acid Treatment for Patients With Inborn Errors in Bile Acid Synthesis. Children's Hospital Medical Center, Cincinnati. 2006. ClinicalTrials.gov Identifier: NCT01589523

16. (kimura2021bileacidsynthesis pages 5-7): Akihiko Kimura, Tatsuki Mizuochi, Hajime Takei, Akira Ohtake, Jun Mori, Kunihiro Shinoda, Takuji Hashimoto, Mureo Kasahara, Takao Togawa, Tsuyoshi Murai, Takashi Iida, and Hiroshi Nittono. Bile acid synthesis disorders in japan: long-term outcome and chenodeoxycholic acid treatment. Jan 2021. URL: https://doi.org/10.1007/s10620-020-06722-4, doi:10.1007/s10620-020-06722-4. This article has 20 citations and is from a peer-reviewed journal.

17. (nittono2024navigatingcholestasisidentifying pages 4-5): Hiroshi Nittono, Mitsuyoshi Suzuki, Hiromi Suzuki, Satoru Sugimoto, Jun Mori, Rieko Sakamoto, Yugo Takaki, Hisamitsu Hayashi, Hajime Takei, and Akihiko Kimura. Navigating cholestasis: identifying inborn errors of bile acid metabolism for precision diagnosis. Frontiers in Pediatrics, Apr 2024. URL: https://doi.org/10.3389/fped.2024.1385970, doi:10.3389/fped.2024.1385970. This article has 5 citations.

18. (nittono2024navigatingcholestasisidentifying pages 5-6): Hiroshi Nittono, Mitsuyoshi Suzuki, Hiromi Suzuki, Satoru Sugimoto, Jun Mori, Rieko Sakamoto, Yugo Takaki, Hisamitsu Hayashi, Hajime Takei, and Akihiko Kimura. Navigating cholestasis: identifying inborn errors of bile acid metabolism for precision diagnosis. Frontiers in Pediatrics, Apr 2024. URL: https://doi.org/10.3389/fped.2024.1385970, doi:10.3389/fped.2024.1385970. This article has 5 citations.

## Artifacts

- [Edison artifact artifact-00](Inborn_Disorder_of_Bile_Acid_Synthesis-deep-research-falcon_artifacts/artifact-00.md)