---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-30T09:05:13.671441'
end_time: '2026-06-30T09:25:08.950023'
duration_seconds: 1195.28
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Elsahy-Waters Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 13
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: Elsahy-Waters_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Elsahy-Waters_Syndrome-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Elsahy-Waters Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Elsahy-Waters Syndrome** covering all of the
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
- **Disease Name:** Elsahy-Waters Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Elsahy-Waters Syndrome** covering all of the
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


# Comprehensive Research Report: Elsahy-Waters Syndrome

## 1. Disease Information

### Overview
Elsahy-Waters syndrome (EWS), also known as branchioskeletogenital syndrome (BSGS), is an ultra-rare autosomal recessive multiple congenital anomaly/intellectual disability (MCA/MR) syndrome characterized by distinctive craniofacial features, premature loss of teeth with radicular dentin dysplasia, vertebral and genital anomalies, and intellectual disability (castori2018anovelmutation pages 1-2, castori2010elsahy–waterssyndromeevidence pages 1-2). The condition was first described in 1971 by Elsahy and Waters in three affected brothers (castori2010elsahy–waterssyndromeevidence pages 4-6). CDH11 was identified as the causal gene in 2017–2018 through exome sequencing studies (castori2018anovelmutation pages 1-2, castori2018anovelmutation pages 2-4).

### Key Identifiers
The following table summarizes the disease identifiers, nomenclature, and core genetic information:

| Category | Identifier/Detail | Source |
|---|---|---|
| Disease name | Elsahy-Waters syndrome | (castori2010elsahy–waterssyndromeevidence pages 1-2, castori2018anovelmutation pages 1-2) |
| OMIM disease ID | OMIM: 211380 | (li2021pathogenicvariantsin pages 9-11) |
| MONDO ID | MONDO:0008885 | (OpenTargets Search: Elsahy-Waters syndrome) |
| Synonyms | Branchioskeletogenital syndrome; branchio-skeleto-genital syndrome; BSG syndrome; BSGS | (castori2010elsahy–waterssyndromeevidence pages 1-2, castori2018anovelmutation pages 1-2) |
| Causal gene | CDH11 | (castori2018anovelmutation pages 1-2, OpenTargets Search: Elsahy-Waters syndrome) |
| Gene OMIM ID | OMIM: 600023 | (castori2018anovelmutation pages 1-2) |
| Chromosomal location | 16q21 | (li2021pathogenicvariantsin pages 14-16) |
| Protein | Cadherin-11; OB-cadherin; osteoblast-cadherin | (castori2018anovelmutation pages 1-2, castori2018anovelmutation pages 4-5) |
| Inheritance | Autosomal recessive | (castori2010elsahy–waterssyndromeevidence pages 1-2, castori2010elsahy–waterssyndromeevidence pages 4-6, castori2018anovelmutation pages 2-4) |
| Molecular mechanism | Biallelic loss-of-function variants in CDH11 causing prematurely truncated protein and impaired adhesion | (castori2018anovelmutation pages 1-2, castori2018anovelmutation pages 2-4, li2021pathogenicvariantsin pages 1-3) |
| Reported variant classes | Homozygous nonsense and other truncating variants | (castori2018anovelmutation pages 1-2, li2021pathogenicvariantsin pages 9-11, li2021pathogenicvariantsin pages 1-3) |
| Example pathogenic variant | CDH11 c.127A>T (p.Lys43*) homozygous nonsense variant | (castori2018anovelmutation pages 2-4) |
| Functional consequence | Impaired Ca2+-dependent cell adhesion / reduced cell-substrate adhesion; delayed osteogenic differentiation proposed | (li2021pathogenicvariantsin pages 1-3, pan2023theodontoblasticdifferentiation pages 15-16) |
| Relationship to Teebi hypertelorism syndrome | Distinct allelic disorder: heterozygous CDH11 variants cause Teebi hypertelorism syndrome, while biallelic truncating variants cause Elsahy-Waters syndrome | (li2021pathogenicvariantsin pages 9-11, li2021pathogenicvariantsin pages 1-3) |
| Distinguishing clinical-genetic note | Global developmental delay/intellectual disability is emphasized in Elsahy-Waters syndrome and helps distinguish it from many Teebi hypertelorism syndrome cases | (li2021pathogenicvariantsin pages 9-11) |
| Open Targets association | CDH11 is the sole associated target listed for Elsahy-Waters syndrome; association score 0.713 | (OpenTargets Search: Elsahy-Waters syndrome) |
| Reported patients/families through 2018 | Approximately 6 patients from 4 families reported as of 2018 | (castori2018anovelmutation pages 2-4) |
| Additional case after 2018 | First East Asian patient reported in 2021, expanding geographic representation | (OpenTargets Search: Elsahy-Waters syndrome) |


*Table: This table summarizes the core disease identifiers, nomenclature, inheritance, and CDH11-related molecular genetics for Elsahy-Waters syndrome. It is useful as a compact reference for knowledge-base curation and for distinguishing this recessive CDH11 disorder from dominant CDH11-related Teebi hypertelorism syndrome.*

### Synonyms
- Branchioskeletogenital syndrome (BSGS)
- Branchio-skeleto-genital syndrome
- BSG syndrome

### Data Sources
Information for this entry is derived from aggregated disease-level resources including OMIM (211380), OpenTargets (MONDO:0008885), and published case reports in the primary literature rather than individual patient EHR data (OpenTargets Search: Elsahy-Waters syndrome, castori2010elsahy–waterssyndromeevidence pages 1-2).

---

## 2. Etiology

### Disease Causal Factors
Elsahy-Waters syndrome is a monogenic Mendelian disorder caused by biallelic loss-of-function mutations in the *CDH11* gene (OMIM 600023) located on chromosome 16q21 (castori2018anovelmutation pages 1-2, castori2018anovelmutation pages 2-4). Cadherins are Ca²⁺-dependent cell-adhesion molecules that control morphogenesis, cell migration, and cell shape changes during multiple developmental processes (castori2018anovelmutation pages 1-2). The identified pathogenic variants include homozygous nonsense mutations resulting in prematurely truncated forms of the cadherin-11 protein, such as c.127A>T (p.Lys43*) (castori2018anovelmutation pages 2-4). There are no known environmental, infectious, or lifestyle risk factors for this genetic condition.

### Risk Factors
- **Genetic risk factors**: Biallelic pathogenic variants in CDH11 are the sole known cause. All reported families have demonstrated parental consanguinity, which greatly increases the risk of autosomal recessive disease (castori2010elsahy–waterssyndromeevidence pages 4-6, castori2010elsahy–waterssyndromeevidence pages 1-2).
- **Environmental risk factors**: Not applicable for this Mendelian disorder.
- **Gene-environment interactions**: None documented.

### Protective Factors
No genetic or environmental protective factors have been identified for this condition. The partial redundancy of cadherin-11 with N-cadherin (CDH2) in bone tissue may mitigate the severity of the skeletal phenotype, as evidenced by the relatively mild skeletal phenotype in Cdh11 null mice compared to compound Cdh2 heterozygous/Cdh11 null mice (castori2018anovelmutation pages 4-5).

---

## 3. Phenotypes

The clinical phenotype of EWS is distinctive, multisystemic, and shows both intra-familial and inter-familial variability (castori2010elsahy–waterssyndromeevidence pages 4-6). The facial phenotype evolves with age, initially resembling craniosynostosis syndromes but becoming more characteristic in adulthood (castori2010elsahy–waterssyndromeevidence pages 4-6). The following table provides a comprehensive listing of all reported phenotypic features with suggested HPO terms:

| Organ system | Phenotype/Feature | Description | Frequency (if known) | HPO term | Reference/PMID |
|---|---|---|---|---|---|
| Craniofacial | Brachycephaly / turribrachycephaly | Shortened anteroposterior skull shape; in some reports described as turri-brachycephaly with small skull circumference | Reported in multiple families; exact percentage not available | HP:0000248 Brachycephaly | Castori 2010, Am J Med Genet A 152A:2810-2815 (castori2010elsahy–waterssyndromeevidence pages 2-4, castori2010elsahy–waterssyndromeevidence pages 4-6, castori2010elsahy–waterssyndromeevidence pages 1-2) |
| Craniofacial | Facial asymmetry | Persistent asymmetry of facial contour, sometimes with head tilting | Reported in multiple patients | HP:0000324 Facial asymmetry | Castori 2010; Castori 2018 (castori2010elsahy–waterssyndromeevidence pages 2-4, castori2010elsahy–waterssyndromeevidence pages 1-2, castori2018anovelmutation pages 2-4) |
| Craniofacial | Hypertelorism / telecanthus | Markedly increased interorbital distance; a core recognizable feature | Present in essentially all reported patients described in available case series | HP:0000316 Hypertelorism | Castori 2010; Li 2021 (castori2010elsahy–waterssyndromeevidence pages 2-4, castori2010elsahy–waterssyndromeevidence pages 4-6, castori2010elsahy–waterssyndromeevidence pages 1-2, li2021pathogenicvariantsin pages 9-11) |
| Craniofacial | Proptosis | Prominent globes/orbital protrusion | Reported in several patients | HP:0000520 Proptosis | Castori 2010; Castori 2018 (castori2010elsahy–waterssyndromeevidence pages 2-4, castori2018anovelmutation pages 2-4) |
| Craniofacial | Blepharochalasis | Redundant or lax eyelid tissue | Reported in several patients | HP:0000613 Blepharochalasis | Castori 2010; Castori 2018 (castori2010elsahy–waterssyndromeevidence pages 4-6, castori2018anovelmutation pages 2-4) |
| Craniofacial | Midface hypoplasia | Underdeveloped midface/maxillary region contributing to characteristic profile | Common in reported cases | HP:0000340 Midface retrusion | Castori 2010; Castori 2018 (castori2010elsahy–waterssyndromeevidence pages 2-4, castori2010elsahy–waterssyndromeevidence pages 4-6, castori2010elsahy–waterssyndromeevidence pages 1-2, castori2018anovelmutation pages 2-4) |
| Craniofacial | Broad nose with concave ridge / bulbous or bifid tip | Broad nasal bridge and tip, sometimes with concave nasal ridge or bifid tip | Common in reported cases | HP:0000445 Broad nose; HP:0011120 Concave nasal ridge; HP:0000455 Broad nasal tip | Castori 2010; Castori 2018 (castori2010elsahy–waterssyndromeevidence pages 2-4, castori2010elsahy–waterssyndromeevidence pages 4-6, castori2010elsahy–waterssyndromeevidence pages 1-2, castori2018anovelmutation pages 2-4) |
| Craniofacial | Prognathism / prominent mandible | Forward projection of mandible with characteristic lower-face prominence | Reported in multiple patients | HP:0000303 Prognathism | Castori 2010; Castori 2018 (castori2010elsahy–waterssyndromeevidence pages 2-4, castori2010elsahy–waterssyndromeevidence pages 4-6, castori2010elsahy–waterssyndromeevidence pages 1-2, castori2018anovelmutation pages 2-4) |
| Craniofacial | High forehead / bitemporal narrowing | Tall forehead and narrowing of temporal regions | Reported in some patients | HP:0000348 High forehead | Castori 2018 (castori2018anovelmutation pages 2-4) |
| Craniofacial | Strabismus / exotropia | Divergent strabismus/exotropia reported in some individuals | Variable | HP:0000486 Strabismus; HP:0000567 Exotropia | Castori 2010 (castori2010elsahy–waterssyndromeevidence pages 4-6, castori2010elsahy–waterssyndromeevidence pages 1-2) |
| Craniofacial / Oropharyngeal | Bifid uvula | Midline split of uvula | Reported in at least one patient/family | HP:0000193 Bifid uvula | Castori 2010 (castori2010elsahy–waterssyndromeevidence pages 4-6) |
| Craniofacial / Perioral | Short philtrum and thin upper vermilion | Mild perioral dysmorphism contributing to facial gestalt | Variable | HP:0000322 Short philtrum; HP:0000219 Thin upper lip vermilion | Castori 2010 (castori2010elsahy–waterssyndromeevidence pages 4-6) |
| Dental | Radicular dentin dysplasia | Severe root malformation with shortened roots and obliterated pulp chambers; hallmark dental feature | Core feature in reported patients | HP:0006312 Dentin dysplasia | Castori 2010; Castori 2018 (castori2010elsahy–waterssyndromeevidence pages 2-4, castori2010elsahy–waterssyndromeevidence pages 1-2, castori2018anovelmutation pages 2-4) |
| Dental | Dentigerous / apical cysts | Recurrent cysts associated with teeth or apices | Variable; present in some but not all reported patients | HP:0011072 Dentigerous cyst | Castori 2010; Castori 2018 (castori2010elsahy–waterssyndromeevidence pages 2-4, castori2010elsahy–waterssyndromeevidence pages 4-6, castori2018anovelmutation pages 2-4) |
| Dental | Premature tooth loss / early exfoliation | Progressive early loss of teeth, often severe enough to impair chewing | Common and clinically significant | HP:0006480 Premature loss of teeth | Castori 2010; Castori 2018 (castori2010elsahy–waterssyndromeevidence pages 2-4, castori2010elsahy–waterssyndromeevidence pages 4-6, castori2018anovelmutation pages 2-4) |
| Dental | Unerupted or malformed teeth / dysodontiasis | Abnormal tooth eruption and morphology | Variable | HP:0000670 Delayed eruption of teeth; HP:0000684 Abnormality of tooth morphology | Castori 2010; Castori 2018 (castori2010elsahy–waterssyndromeevidence pages 2-4, castori2018anovelmutation pages 2-4) |
| Dental / Jaw | Alveolar bone resorption | Marked alveolar bone loss accompanying dental pathology | Reported in multiple patients | HP:0100259 Abnormal alveolar ridge morphology | Castori 2010; Castori 2018 (castori2010elsahy–waterssyndromeevidence pages 2-4, castori2010elsahy–waterssyndromeevidence pages 1-2, castori2018anovelmutation pages 2-4) |
| Functional impact | Difficulty chewing solid foods | Severe dental disease can prevent normal mastication and compromise oral intake | Reported in affected siblings followed long term | HP:0012537 Dysphagia for solids (closest related term) | Castori 2018 (castori2018anovelmutation pages 2-4) |
| Skeletal | Cervical vertebral fusion (e.g., C2-C3) | Congenital vertebral synostosis, especially in cervical spine | Recurrent feature | HP:0002949 Vertebral fusion | Castori 2010; Castori 2018 (castori2010elsahy–waterssyndromeevidence pages 2-4, castori2010elsahy–waterssyndromeevidence pages 4-6, castori2010elsahy–waterssyndromeevidence pages 1-2, castori2018anovelmutation pages 2-4) |
| Skeletal | Lumbar vertebral fusion / posterior arch fusion | Fusion involving lumbar vertebrae or posterior arches | Variable | HP:0002949 Vertebral fusion | Castori 2010; Castori 2018 (castori2010elsahy–waterssyndromeevidence pages 4-6, castori2018anovelmutation pages 2-4) |
| Skeletal | Scoliosis | Thoracolumbar spinal curvature abnormality | Variable | HP:0002650 Scoliosis | Castori 2010 (castori2010elsahy–waterssyndromeevidence pages 2-4, castori2010elsahy–waterssyndromeevidence pages 4-6) |
| Skeletal | Thick calvaria / cranial bone abnormality | Increased calvarial thickness reported radiographically | Reported in some cases | HP:0000244 Calvarial thickening | Castori 2010 (castori2010elsahy–waterssyndromeevidence pages 1-2) |
| Skeletal / Mandible | Thinning of mandible | Radiographic mandibular thinning | Reported in at least one family | HP:0000278 Retrognathia/mandibular anomaly (closest broad term) | Castori 2010 (castori2010elsahy–waterssyndromeevidence pages 2-4) |
| Genital | Hypospadias | Urethral opening on ventral penis; recurrent male genital anomaly | Present in affected males reported to date | HP:0000047 Hypospadias | Castori 2010; Castori 2018; Li 2021 (castori2010elsahy–waterssyndromeevidence pages 1-2, castori2010elsahy–waterssyndromeevidence pages 4-6, castori2018anovelmutation pages 2-4, li2021pathogenicvariantsin pages 9-11) |
| Genital | Small penis / hypogenitalism | Underdevelopment of external genitalia | Variable among male cases | HP:0000054 Micropenis | Castori 2010 (castori2010elsahy–waterssyndromeevidence pages 2-4, castori2010elsahy–waterssyndromeevidence pages 1-2) |
| Genitourinary | Ureteral stenosis | Structural urinary tract anomaly reported in one case | Rare/isolated report | HP:0012839 Ureter stenosis | Castori 2010 (castori2010elsahy–waterssyndromeevidence pages 4-6) |
| Neurological / Developmental | Intellectual disability / developmental delay | Typically mild-to-moderate cognitive impairment with delayed psychomotor development; considered a key distinguishing feature from dominant CDH11-related Teebi syndrome | Reported in all EWS patients summarized by Li 2021 | HP:0001249 Intellectual disability; HP:0001263 Global developmental delay | Castori 2010; Castori 2018; Li 2021 (castori2010elsahy–waterssyndromeevidence pages 1-2, castori2010elsahy–waterssyndromeevidence pages 4-6, castori2018anovelmutation pages 2-4, li2021pathogenicvariantsin pages 9-11) |
| Neurological | Microcephaly | Small head circumference reported in some affected individuals | Variable | HP:0000252 Microcephaly | Castori 2018 (castori2018anovelmutation pages 2-4) |
| Neurological | Seizures | Seizure disorder reported in at least one patient | Rare/variable | HP:0001250 Seizure | Castori 2010 (castori2010elsahy–waterssyndromeevidence pages 4-6) |
| Auditory | Mixed hearing loss / progressive bilateral hearing loss | Sensorineural-conductive mixed loss, in some cases progressive and bilateral | Variable | HP:0000408 Hearing impairment; HP:0004789 Mixed hearing impairment | Castori 2010; Castori 2018 (castori2010elsahy–waterssyndromeevidence pages 2-4, castori2010elsahy–waterssyndromeevidence pages 4-6, castori2018anovelmutation pages 2-4) |
| Dermatological | Pachydermia / thick furrowed skin | Thickened furrowed facial skin, especially glabellar region | Reported in some patients | HP:0000974 Hyperkeratosis / HP:0007430 Thickened skin (closest broad term) | Castori 2018; Castori 2010 (castori2018anovelmutation pages 2-4, castori2010elsahy–waterssyndromeevidence pages 4-6) |
| Dermatological | Glabellar skin wrinkling/furrows | Wrinkling or furrows over glabella contributing to facial appearance | Variable but recurrent | HP:0000997 Abnormality of skin texture | Castori 2010 (castori2010elsahy–waterssyndromeevidence pages 2-4, castori2010elsahy–waterssyndromeevidence pages 4-6) |
| Dermatological | Progressive alopecia | Progressive scalp hair loss reported in long-term follow-up of siblings | Reported in some patients | HP:0008070 Alopecia | Castori 2018 (castori2018anovelmutation pages 2-4) |
| Functional / Social | Dependence in adult life | Reported lack of occupational activity and reliance on parental support in adulthood | Observed in 2 adult siblings with long-term follow-up | HP:0033676 Impaired activities of daily living (closest related term) | Castori 2018 (castori2018anovelmutation pages 2-4) |


*Table: This table summarizes the reported clinical phenotype spectrum of Elsahy-Waters syndrome across major organ systems, with suggested HPO mappings and supporting citations from the gathered evidence. It is useful for disease knowledge base curation, phenotype annotation, and differential diagnosis.*

### Summary of Key Phenotype Characteristics

**Age of Onset**: Congenital/childhood. The craniofacial gestalt and dental anomalies become more recognizable with age, and cognitive impairment becomes clearer during childhood (castori2010elsahy–waterssyndromeevidence pages 4-6).

**Severity**: Moderate. Intellectual disability is typically mild to moderate. The dental phenotype, however, is severe and significantly impacts daily functioning, preventing solid food consumption in some patients (castori2018anovelmutation pages 2-4).

**Progression**: Progressive features include worsening dental pathology (progressive tooth loss, dentigerous cysts), progressive alopecia, and progressive hearing loss in some patients (castori2010elsahy–waterssyndromeevidence pages 2-4, castori2018anovelmutation pages 2-4). The characteristic facial phenotype becomes more pronounced with age (castori2010elsahy–waterssyndromeevidence pages 4-6).

**Quality of Life Impact**: Severely impacted. Both affected siblings in the study by Castori et al. (2018) were dependent on their parents without occupational activity. The dental complications represent a major clinical burden, impairing mastication and nutritional intake (castori2018anovelmutation pages 2-4).

---

## 4. Genetic/Molecular Information

### Causal Gene
**CDH11** (Cadherin-11; HGNC:1750; OMIM: 600023; Ensembl: ENSG00000140937) on chromosome 16q21 is the sole gene known to cause EWS when mutated in a biallelic fashion (OpenTargets Search: Elsahy-Waters syndrome, castori2018anovelmutation pages 1-2).

### Pathogenic Variants
- **Variant type**: Homozygous nonsense and other truncating variants (castori2018anovelmutation pages 1-2, li2021pathogenicvariantsin pages 9-11).
- **Classification**: Pathogenic (per ClinGen Syndromic Disorders Gene Curation Expert Panel evaluation) (OpenTargets Search: Elsahy-Waters syndrome).
- **Example variant**: c.127A>T (p.Lys43*) — a nonsense variant in exon 1 creating a premature stop codon that severely truncates the cadherin-11 protein (castori2018anovelmutation pages 2-4).
- **Functional consequence**: Loss of function. The variants truncate the transmembrane and intracellular domains, abolishing cell-adhesion capability (li2021pathogenicvariantsin pages 9-11, li2021pathogenicvariantsin pages 1-3).
- **Origin**: Germline.
- **Allele frequency**: Not reported in population databases given the ultra-rare nature of the condition. All reported families have demonstrated consanguinity (castori2010elsahy–waterssyndromeevidence pages 4-6).

### Allelic Disorder: Teebi Hypertelorism Syndrome
Notably, heterozygous missense variants in CDH11 cause a distinct allelic disorder — Teebi hypertelorism syndrome (THS; OMIM 145420) — which presents with hypertelorism but generally normal or only mildly delayed development and minimal skeletal findings, contrasting with the biallelic loss-of-function mechanism in EWS (li2021pathogenicvariantsin pages 9-11, li2021pathogenicvariantsin pages 1-3). This genotype-phenotype correlation distinguishes dominant (haploinsufficiency or dominant-negative) from recessive (complete loss-of-function) CDH11-related conditions.

### Modifier Genes
No specific modifier genes have been identified. However, partial redundancy between CDH11 and CDH2 (N-cadherin) in bone tissue has been demonstrated in mouse models, where compound Cdh2 heterozygous/Cdh11 null mice display more pronounced bone phenotypes than single Cdh11 null mice, suggesting CDH2 may modify disease expression (castori2018anovelmutation pages 4-5).

### Epigenetic Information
CDH11 is known to undergo promoter methylation inactivation in certain cancer contexts (Chen et al. 2021, J Cancer 12:1190-1199), but no specific epigenetic findings have been reported in EWS.

---

## 5. Environmental Information

No environmental factors, lifestyle factors, or infectious agents have been implicated in the etiology or modification of Elsahy-Waters syndrome. This is consistent with its classification as a Mendelian genetic disorder.

---

## 6. Mechanism / Pathophysiology

### Molecular Pathways
CDH11 encodes cadherin-11 (also termed OB-cadherin or osteoblast-cadherin), a type II classical cadherin that mediates Ca²⁺-dependent homophilic cell-cell adhesion (castori2018anovelmutation pages 1-2, li2021pathogenicvariantsin pages 1-3). Key pathways and molecular mechanisms include:

1. **Cell adhesion and migration**: CDH11 localizes to focal adhesions and promotes cell-substrate adhesion. Pathogenic variants reduce cell-to-substrate transadhesion activity and alter fibroblast morphology, with delayed lamellipodia formation and abnormal membrane dynamics observed in patient-derived fibroblasts (li2021pathogenicvariantsin pages 14-16, li2021pathogenicvariantsin pages 17-24, li2021pathogenicvariantsin pages 8-9). CDH11 regulates protrusive activity in cranial neural crest cells through interactions with Trio and small GTPases (GO:0007155 cell adhesion; GO:0016477 cell migration) (li2021pathogenicvariantsin pages 14-16).

2. **TGFβ1/Smad signaling**: Cadherin-11 regulates extracellular matrix (ECM) production via the TGFβ1 pathway. Cells lacking cadherin-11 show increased TGFβ1 expression and subsequent translocation of phosphorylated SMAD2/3 into the nucleus, with changes in ECM composition including decreased type VI collagen and increased fibronectin (Passanha et al. 2022, Stem Cells 40:669-677).

3. **RhoA/ROCK signaling**: CDH11 modulates RhoA/ROCK pathway activity, which is involved in cytoskeletal organization and fibrosis (Franzè et al. 2020, J Crohn's Colitis 14:406-417).

4. **Smad2/3, ERK1/2, and JNK pathways**: RNA-seq of CDH11-null atrial fibroblasts showed significant decreases in transcripts associated with Smad2/3, ERK1/2, and JNK pathways (Cao et al. 2021, J Inflamm Res 14:2897-2911).

### Cellular Processes
- **Osteoblast differentiation**: CDH11 shows prevalent expression in osteoblastic cell lines with upregulation during differentiation, suggesting a specific function in bone formation and development (castori2018anovelmutation pages 1-2). Loss-of-function CDH11 mutations delay osteogenic differentiation, which may underlie craniofacial defects in EWS patients (pan2023theodontoblasticdifferentiation pages 15-16).
- **Mesenchymal stem cell differentiation**: CDH11 is required for mesenchymal stem cell commitment to multiple lineages, regulating the balance between osteogenic and adipogenic differentiation (Passanha et al. 2022, Stem Cells 40:669-677).
- **Cranial neural crest cell migration**: CDH11 is expressed in cranial neural crest cells and plays critical roles in their migration and morphogenetic processes during craniofacial development (li2021pathogenicvariantsin pages 14-16, li2021pathogenicvariantsin pages 17-24).

### Causal Chain
The pathophysiological sequence from molecular defect to clinical manifestation proceeds as follows:
1. **Initial trigger**: Biallelic loss-of-function CDH11 mutations → absence/severe truncation of functional cadherin-11 protein
2. **Upstream mechanism**: Loss of Ca²⁺-dependent cell-cell adhesion and impaired cell-substrate interactions in mesenchymal tissues
3. **Intermediate processes**: Disrupted cranial neural crest cell migration, impaired osteoblast differentiation, altered ECM production, and dysregulated TGFβ1/Smad signaling
4. **Downstream effects**: Abnormal craniofacial morphogenesis, defective bone formation (vertebral fusions, calvarial abnormalities), defective dentin formation (radicular dentin dysplasia), and impaired neurodevelopment
5. **Clinical manifestation**: The distinctive craniofacial gestalt, dental anomalies, skeletal malformations, genital anomalies, and intellectual disability characteristic of EWS

### Cell Types Involved
- Cranial neural crest cells (CL:0000008)
- Osteoblasts (CL:0000062)
- Dental mesenchymal stem cells / odontoblasts (CL:0000060)
- Mesenchymal stem cells (CL:0000134)
- Fibroblasts (CL:0000057)

### Protein Dysfunction
Cadherin-11 normally contains five extracellular cadherin (EC) repeat domains, a transmembrane domain, and an intracellular domain. The truncating variants identified in EWS eliminate the transmembrane and intracellular domains entirely, preventing membrane anchoring and intracellular signaling (li2021pathogenicvariantsin pages 9-11, li2021pathogenicvariantsin pages 1-3). The Ca²⁺-binding regions between EC domains are critical for cadherin stability, and disruption of these regions impairs the protein's adhesive function (li2021pathogenicvariantsin pages 1-3).

---

## 7. Anatomical Structures Affected

### Organ Level
- **Primary**: Craniofacial skeleton (UBERON:0003128), teeth/dentin (UBERON:0001751), vertebral column (UBERON:0001130)
- **Secondary**: External genitalia (UBERON:0004176), brain (UBERON:0000955), ear/auditory system (UBERON:0002105), skin (UBERON:0002097)
- **Body systems**: Skeletal, nervous, genitourinary, integumentary, special senses

### Tissue and Cell Level
- Bone tissue — osteoblasts (CL:0000062) — defective bone formation
- Dental tissues — odontoblasts (CL:0000060) — radicular dentin dysplasia
- Neural tissue — neurons — intellectual disability, seizures
- Mesenchyme — mesenchymal stem cells (CL:0000134) — impaired differentiation
- Skin — dermal fibroblasts — pachydermia, alopecia

### Localization
- Craniofacial: bilateral involvement with facial asymmetry
- Vertebral: cervical (particularly C2-C3) and lumbar spine (castori2010elsahy–waterssyndromeevidence pages 2-4, castori2018anovelmutation pages 2-4)
- Genital: ventral penile (hypospadias)
- Auditory: bilateral hearing loss (castori2010elsahy–waterssyndromeevidence pages 2-4)

---

## 8. Temporal Development

### Onset
- **Typical age of onset**: Congenital. Craniofacial dysmorphism is present at birth, though it becomes more recognizable with age (castori2010elsahy–waterssyndromeevidence pages 4-6).
- **Onset pattern**: Congenital with progressive features.

### Progression
- The dental phenotype is progressive, with early tooth loss and recurrent dentigerous cysts (castori2010elsahy–waterssyndromeevidence pages 2-4, castori2018anovelmutation pages 2-4).
- Hearing loss may be progressive and bilateral (castori2010elsahy–waterssyndromeevidence pages 2-4).
- Alopecia is progressive (castori2018anovelmutation pages 2-4).
- The facial gestalt evolves with age, becoming more characteristic in adulthood (castori2010elsahy–waterssyndromeevidence pages 4-6).
- Disease course: Chronic lifelong condition.

### Critical Periods
Early dental intervention could potentially improve quality of life, though dental implants have not been feasible in reported cases due to alveolar bone resorption (castori2018anovelmutation pages 2-4).

---

## 9. Inheritance and Population

### Epidemiology
- **Prevalence**: Unknown; estimated fewer than 1 in 1,000,000 given the ultra-rare nature. As of 2018, only approximately 6 patients from 4 families had been documented in the medical literature (castori2018anovelmutation pages 2-4).
- **Incidence**: Not calculable from available data.

### Inheritance Pattern
- **Autosomal recessive** (castori2010elsahy–waterssyndromeevidence pages 1-2, castori2010elsahy–waterssyndromeevidence pages 4-6).
- Parental consanguinity has been documented in all reported families, consistent with a rare autosomal recessive condition (castori2010elsahy–waterssyndromeevidence pages 4-6).
- Both sexes are affected; an affected female was first reported by Castori et al. in 2010, refuting earlier hypotheses of X-linked inheritance based on the original report of three affected brothers (castori2010elsahy–waterssyndromeevidence pages 1-2, castori2010elsahy–waterssyndromeevidence pages 4-6).

### Penetrance and Expressivity
- **Penetrance**: Appears to be complete in individuals with biallelic loss-of-function CDH11 variants.
- **Expressivity**: Variable. Intra-familial and inter-familial variability has been noted, particularly in vertebral fusions, hearing loss, and dentigerous cysts (castori2010elsahy–waterssyndromeevidence pages 4-6).

### Population Demographics
- **Geographic distribution**: Cases have been reported from the Middle East, Italy, Turkey, and East Asia (first East Asian patient reported in 2021) (castori2018anovelmutation pages 2-4).
- **Sex ratio**: Both males and females affected, approximately equal (castori2010elsahy–waterssyndromeevidence pages 1-2).

---

## 10. Diagnostics

### Clinical Diagnosis
Diagnosis of EWS is based on recognition of the characteristic clinical phenotype: distinctive craniofacial features (hypertelorism, brachycephaly, midface hypoplasia, facial asymmetry), radicular dentin dysplasia with premature tooth loss, vertebral fusions, hypospadias in males, and intellectual disability (castori2018anovelmutation pages 1-2, castori2010elsahy–waterssyndromeevidence pages 1-2).

### Diagnostic Imaging
- **Craniofacial imaging**: Radiography or CT demonstrating brachycephaly, increased interorbital distance, thick calvaria (castori2010elsahy–waterssyndromeevidence pages 1-2).
- **Dental imaging**: Panoramic radiographs revealing radicular dentin dysplasia with shortened roots, obliterated pulp chambers, and dentigerous cysts (castori2010elsahy–waterssyndromeevidence pages 2-4, castori2010elsahy–waterssyndromeevidence pages 1-2).
- **Spinal imaging**: Radiography or MRI of the spine demonstrating vertebral fusions (particularly C2-C3) and scoliosis (castori2010elsahy–waterssyndromeevidence pages 2-4, castori2018anovelmutation pages 2-4).

### Genetic Testing
- **Whole exome sequencing (WES)**: The primary modality through which CDH11 mutations were identified as the cause of EWS. WES is the recommended first-tier genetic testing approach (castori2018anovelmutation pages 1-2, castori2018anovelmutation pages 2-4).
- **Whole genome sequencing (WGS)**: May also identify CDH11 variants.
- **Single gene testing**: Targeted sequencing of CDH11 can confirm a clinical diagnosis.
- **Gene panels**: CDH11 should be included in panels for syndromic intellectual disability, craniofacial disorders, and skeletal dysplasias.

### Differential Diagnosis
- **Teebi hypertelorism syndrome** (OMIM 145420): Caused by heterozygous CDH11 missense variants; distinguished by generally normal development and minimal skeletal findings (li2021pathogenicvariantsin pages 9-11).
- **Craniosynostosis syndromes**: The facial phenotype in childhood may resemble craniosynostosis (castori2010elsahy–waterssyndromeevidence pages 4-6).
- **Other conditions with hypertelorism and intellectual disability**.

---

## 11. Outcome/Prognosis

### Life Expectancy and Survival
No specific mortality data are available for EWS. The condition is not known to be life-limiting, but longitudinal data are extremely limited given the ultra-rarity of the disorder.

### Morbidity and Function
- Affected individuals may have significant morbidity from dental complications, which can prevent solid food consumption (castori2018anovelmutation pages 2-4).
- Both siblings followed long-term by Castori et al. (2018) were dependent on their parents without occupational activity, indicating significant functional impairment in adulthood (castori2018anovelmutation pages 2-4).
- Mild-to-moderate intellectual disability limits academic and vocational achievement (li2021pathogenicvariantsin pages 9-11, castori2018anovelmutation pages 2-4).

### Complications
- Recurrent dentigerous cysts (castori2010elsahy–waterssyndromeevidence pages 4-6, castori2018anovelmutation pages 2-4)
- Progressive tooth loss and alveolar bone resorption (castori2010elsahy–waterssyndromeevidence pages 2-4)
- Progressive hearing loss (castori2010elsahy–waterssyndromeevidence pages 2-4)

---

## 12. Treatment

### Pharmacotherapy
No disease-specific pharmacotherapy exists for EWS. Management is entirely symptomatic and supportive (MAXO:0000009 — supportive care).

### Surgical and Interventional
- **Dental management**: Dental complications represent the major clinical challenge. Surgical evaluation for dental implants was performed in reported cases but determined not to be feasible due to severe alveolar bone resorption (castori2018anovelmutation pages 2-4). Dentigerous cyst excision may be required (MAXO:0000004 — surgical procedure).
- **Craniofacial surgery**: May be considered for specific features, though no reports detail craniofacial surgical outcomes in EWS.
- **Hypospadias repair**: Standard urological surgical approaches may be applied in affected males (MAXO:0000004).

### Supportive and Rehabilitative
- Nutritional support for patients unable to consume solid foods (castori2018anovelmutation pages 2-4)
- Speech therapy and hearing aids for hearing loss (MAXO:0000930 — hearing aid fitting)
- Special education and developmental support for intellectual disability (MAXO:0000950 — educational intervention)
- Occupational therapy
- Genetic counseling for affected families (MAXO:0000079 — genetic counseling)

### Experimental Treatments
No clinical trials are registered for EWS on ClinicalTrials.gov. No gene therapy, cell therapy, or targeted therapeutic approaches have been reported or are in development for this condition.

---

## 13. Prevention

### Primary Prevention
Not applicable as a Mendelian genetic disorder.

### Genetic Screening and Counseling
- **Carrier screening**: CDH11 sequencing in consanguineous couples from families with known EWS may identify carriers (MAXO:0000079).
- **Prenatal diagnosis**: Possible through targeted genetic testing (chorionic villus sampling or amniocentesis) if the familial variant is known.
- **Preimplantation genetic diagnosis (PGD)**: Theoretically available for families with identified CDH11 pathogenic variants.
- **Cascade screening**: Recommended in families with affected members, particularly in consanguineous populations (castori2010elsahy–waterssyndromeevidence pages 4-6).

---

## 14. Other Species / Natural Disease

No naturally occurring animal model of Elsahy-Waters syndrome has been reported. The disease has not been documented in companion animals or livestock.

---

## 15. Model Organisms

### Mouse Models
- **Cdh11 knockout (Cdh11⁻/⁻) mice**: Global Cdh11 null mice have been generated and studied extensively. These mice exhibit phenotypic features relevant to EWS, though the skeletal phenotype is milder than expected due to partial redundancy with N-cadherin (Cdh2) (castori2018anovelmutation pages 4-5). Key findings include:
  - Altered behavioral responses, consistent with the neurodevelopmental aspect of EWS, linked to high CDH11 expression in developing mouse brains with differential expression in hippocampal synaptic junctions (castori2018anovelmutation pages 4-5).
  - Reduced bone phenotype compared to compound Cdh2 heterozygous/Cdh11 null mice, demonstrating functional redundancy (castori2018anovelmutation pages 4-5).
  - Decreased collagen and elastin synthesis, reduced tissue contractile function (Row et al. 2016, J Cell Sci 129:2950-2961).
  - Protection from fibrosis in various organ models including cardiac (Schroer et al. 2019, JCI Insight 4), intestinal (Franzè et al. 2020, J Crohn's Colitis 14:406-417), and hepatic (Wu et al. 2022, Pediatr Invest 6:100-110) fibrosis models.

### Model Characteristics
- **Phenotype recapitulation**: Partial. Cdh11 null mice recapitulate the skeletal and behavioral aspects of EWS but with milder severity. Dental phenotypes have not been well characterized in mouse models.
- **Limitations**: The partial redundancy of CDH11 with CDH2 in mouse bone tissue limits the severity of the skeletal phenotype relative to the human disease (castori2018anovelmutation pages 4-5). Mouse dental biology also differs substantially from human dental development.

### Zebrafish Models
CDH11 expression has been documented during zebrafish skull development, and zebrafish models may be useful for studying craniofacial aspects of the syndrome, though no specific EWS zebrafish model has been reported.

---

## 16. Open Targets Disease-Target Associations

OpenTargets (MONDO:0008885) identifies CDH11 (ENSG00000140937) as the sole molecular target associated with Elsahy-Waters syndrome, with an association score of 0.71 based on 5 evidence items from multiple curation sources including ClinGen and the Developmental Disorders Gene Curation Expert Panel (OpenTargets Search: Elsahy-Waters syndrome). Key supporting PMIDs include 28988429, 33811546, 29271567, 27431290, 30194892, and 34278706 (OpenTargets Search: Elsahy-Waters syndrome).

---

## 17. Ontology Term Summary

**Disease Ontology**:
- MONDO:0008885 (Elsahy-Waters syndrome)
- OMIM:211380

**Gene Ontology (Biological Process)**:
- GO:0007155 (cell adhesion)
- GO:0016477 (cell migration)
- GO:0001649 (osteoblast differentiation)
- GO:0060349 (bone morphogenesis)
- GO:0007275 (multicellular organism development)

**Gene Ontology (Cellular Component)**:
- GO:0005913 (cell-cell adherens junction)
- GO:0005925 (focal adhesion)
- GO:0016020 (membrane)

**Gene Ontology (Molecular Function)**:
- GO:0005509 (calcium ion binding)
- GO:0045296 (cadherin binding)

**Cell Ontology**:
- CL:0000062 (osteoblast)
- CL:0000060 (odontoblast)
- CL:0000134 (mesenchymal stem cell)
- CL:0000008 (cranial neural crest cell)

**UBERON**:
- UBERON:0003128 (craniofacial skeleton)
- UBERON:0001751 (dentin)
- UBERON:0001130 (vertebral column)
- UBERON:0000955 (brain)

**CHEBI**:
- CHEBI:29108 (calcium(2+)) — required for CDH11 function

---

## Summary

Elsahy-Waters syndrome is an ultra-rare autosomal recessive Mendelian disorder caused by biallelic loss-of-function mutations in *CDH11*, the gene encoding cadherin-11 (OB-cadherin). As of 2018, approximately 6 patients from 4 families had been reported worldwide, with all families demonstrating consanguinity (castori2018anovelmutation pages 2-4, castori2010elsahy–waterssyndromeevidence pages 4-6). The clinical phenotype encompasses distinctive craniofacial dysmorphism (hypertelorism, brachycephaly, midface hypoplasia), severe dental anomalies (radicular dentin dysplasia, dentigerous cysts, premature tooth loss), skeletal malformations (vertebral fusions), genital anomalies (hypospadias in males), and mild-to-moderate intellectual disability (castori2018anovelmutation pages 1-2, castori2010elsahy–waterssyndromeevidence pages 2-4, castori2018anovelmutation pages 2-4). The molecular pathophysiology involves impaired Ca²⁺-dependent cell adhesion, disrupted cranial neural crest cell migration, and delayed osteogenic differentiation (li2021pathogenicvariantsin pages 14-16, castori2018anovelmutation pages 1-2, pan2023theodontoblasticdifferentiation pages 15-16). No disease-specific therapies exist; management is supportive with particular challenges in dental rehabilitation (castori2018anovelmutation pages 2-4). CDH11 heterozygous variants cause the allelic but phenotypically distinct Teebi hypertelorism syndrome (li2021pathogenicvariantsin pages 9-11). Cdh11 knockout mice provide a partial animal model but exhibit a milder phenotype due to functional redundancy with N-cadherin (castori2018anovelmutation pages 4-5).

References

1. (castori2018anovelmutation pages 1-2): Marco Castori, Claus‐Eric Ott, Luigi Bisceglia, Maria Pia Leone, Tommaso Mazza, Stefano Castellana, Jurgen Tomassi, Silvia Lanciotti, Stefan Mundlos, Raoul C. Hennekam, Uwe Kornak, and Francesco Brancati. A novel mutation in cdh11, encoding cadherin‐11, cause branchioskeletogenital (elsahy‐waters) syndrome. American Journal of Medical Genetics Part A, 176:2028-2033, Sep 2018. URL: https://doi.org/10.1002/ajmg.a.40379, doi:10.1002/ajmg.a.40379. This article has 8 citations.

2. (castori2010elsahy–waterssyndromeevidence pages 1-2): Marco Castori, Piero Cascone, Michele Valiante, Luigi Laino, Giorgio Iannetti, Raoul C.M. Hennekam, and Paola Grammatico. Elsahy–waters syndrome: evidence for autosomal recessive inheritance. American Journal of Medical Genetics Part A, 152A:2810-2815, Nov 2010. URL: https://doi.org/10.1002/ajmg.a.33634, doi:10.1002/ajmg.a.33634. This article has 16 citations.

3. (castori2010elsahy–waterssyndromeevidence pages 4-6): Marco Castori, Piero Cascone, Michele Valiante, Luigi Laino, Giorgio Iannetti, Raoul C.M. Hennekam, and Paola Grammatico. Elsahy–waters syndrome: evidence for autosomal recessive inheritance. American Journal of Medical Genetics Part A, 152A:2810-2815, Nov 2010. URL: https://doi.org/10.1002/ajmg.a.33634, doi:10.1002/ajmg.a.33634. This article has 16 citations.

4. (castori2018anovelmutation pages 2-4): Marco Castori, Claus‐Eric Ott, Luigi Bisceglia, Maria Pia Leone, Tommaso Mazza, Stefano Castellana, Jurgen Tomassi, Silvia Lanciotti, Stefan Mundlos, Raoul C. Hennekam, Uwe Kornak, and Francesco Brancati. A novel mutation in cdh11, encoding cadherin‐11, cause branchioskeletogenital (elsahy‐waters) syndrome. American Journal of Medical Genetics Part A, 176:2028-2033, Sep 2018. URL: https://doi.org/10.1002/ajmg.a.40379, doi:10.1002/ajmg.a.40379. This article has 8 citations.

5. (li2021pathogenicvariantsin pages 9-11): Dong Li, Michael E. March, Paola Fortugno, Liza L. Cox, Leticia S. Matsuoka, Rosanna Monetta, Christoph Seiler, Louise C. Pyle, Emma C. Bedoukian, María José Sánchez-Soler, Oana Caluseriu, Katheryn Grand, Allison Tam, Alicia R. P. Aycinena, Letizia Camerota, Yiran Guo, Patrick Sleiman, Bert Callewaert, Candy Kumps, Annelies Dheedene, Michael Buckley, Edwin P. Kirk, Anne Turner, Benjamin Kamien, Chirag Patel, Meredith Wilson, Tony Roscioli, John Christodoulou, Timothy C. Cox, Elaine H. Zackai, Francesco Brancati, Hakon Hakonarson, and Elizabeth J. Bhoj. Pathogenic variants in cdh11 impair cell adhesion and cause teebi hypertelorism syndrome. Human Genetics, 140:1061-1076, Apr 2021. URL: https://doi.org/10.1007/s00439-021-02274-3, doi:10.1007/s00439-021-02274-3. This article has 12 citations and is from a peer-reviewed journal.

6. (OpenTargets Search: Elsahy-Waters syndrome): Open Targets Query (Elsahy-Waters syndrome, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

7. (li2021pathogenicvariantsin pages 14-16): Dong Li, Michael E. March, Paola Fortugno, Liza L. Cox, Leticia S. Matsuoka, Rosanna Monetta, Christoph Seiler, Louise C. Pyle, Emma C. Bedoukian, María José Sánchez-Soler, Oana Caluseriu, Katheryn Grand, Allison Tam, Alicia R. P. Aycinena, Letizia Camerota, Yiran Guo, Patrick Sleiman, Bert Callewaert, Candy Kumps, Annelies Dheedene, Michael Buckley, Edwin P. Kirk, Anne Turner, Benjamin Kamien, Chirag Patel, Meredith Wilson, Tony Roscioli, John Christodoulou, Timothy C. Cox, Elaine H. Zackai, Francesco Brancati, Hakon Hakonarson, and Elizabeth J. Bhoj. Pathogenic variants in cdh11 impair cell adhesion and cause teebi hypertelorism syndrome. Human Genetics, 140:1061-1076, Apr 2021. URL: https://doi.org/10.1007/s00439-021-02274-3, doi:10.1007/s00439-021-02274-3. This article has 12 citations and is from a peer-reviewed journal.

8. (castori2018anovelmutation pages 4-5): Marco Castori, Claus‐Eric Ott, Luigi Bisceglia, Maria Pia Leone, Tommaso Mazza, Stefano Castellana, Jurgen Tomassi, Silvia Lanciotti, Stefan Mundlos, Raoul C. Hennekam, Uwe Kornak, and Francesco Brancati. A novel mutation in cdh11, encoding cadherin‐11, cause branchioskeletogenital (elsahy‐waters) syndrome. American Journal of Medical Genetics Part A, 176:2028-2033, Sep 2018. URL: https://doi.org/10.1002/ajmg.a.40379, doi:10.1002/ajmg.a.40379. This article has 8 citations.

9. (li2021pathogenicvariantsin pages 1-3): Dong Li, Michael E. March, Paola Fortugno, Liza L. Cox, Leticia S. Matsuoka, Rosanna Monetta, Christoph Seiler, Louise C. Pyle, Emma C. Bedoukian, María José Sánchez-Soler, Oana Caluseriu, Katheryn Grand, Allison Tam, Alicia R. P. Aycinena, Letizia Camerota, Yiran Guo, Patrick Sleiman, Bert Callewaert, Candy Kumps, Annelies Dheedene, Michael Buckley, Edwin P. Kirk, Anne Turner, Benjamin Kamien, Chirag Patel, Meredith Wilson, Tony Roscioli, John Christodoulou, Timothy C. Cox, Elaine H. Zackai, Francesco Brancati, Hakon Hakonarson, and Elizabeth J. Bhoj. Pathogenic variants in cdh11 impair cell adhesion and cause teebi hypertelorism syndrome. Human Genetics, 140:1061-1076, Apr 2021. URL: https://doi.org/10.1007/s00439-021-02274-3, doi:10.1007/s00439-021-02274-3. This article has 12 citations and is from a peer-reviewed journal.

10. (pan2023theodontoblasticdifferentiation pages 15-16): Houwen Pan, Yiling Yang, Hongyuan Xu, Anting Jin, Xiangru Huang, Xin Gao, Siyuan Sun, Yuanqi Liu, Jingyi Liu, Tingwei Lu, Xinyu Wang, Yanfei Zhu, and Lingyong Jiang. The odontoblastic differentiation of dental mesenchymal stem cells: molecular regulation mechanism and related genetic syndromes. Frontiers in Cell and Developmental Biology, Sep 2023. URL: https://doi.org/10.3389/fcell.2023.1174579, doi:10.3389/fcell.2023.1174579. This article has 35 citations.

11. (castori2010elsahy–waterssyndromeevidence pages 2-4): Marco Castori, Piero Cascone, Michele Valiante, Luigi Laino, Giorgio Iannetti, Raoul C.M. Hennekam, and Paola Grammatico. Elsahy–waters syndrome: evidence for autosomal recessive inheritance. American Journal of Medical Genetics Part A, 152A:2810-2815, Nov 2010. URL: https://doi.org/10.1002/ajmg.a.33634, doi:10.1002/ajmg.a.33634. This article has 16 citations.

12. (li2021pathogenicvariantsin pages 17-24): Dong Li, Michael E. March, Paola Fortugno, Liza L. Cox, Leticia S. Matsuoka, Rosanna Monetta, Christoph Seiler, Louise C. Pyle, Emma C. Bedoukian, María José Sánchez-Soler, Oana Caluseriu, Katheryn Grand, Allison Tam, Alicia R. P. Aycinena, Letizia Camerota, Yiran Guo, Patrick Sleiman, Bert Callewaert, Candy Kumps, Annelies Dheedene, Michael Buckley, Edwin P. Kirk, Anne Turner, Benjamin Kamien, Chirag Patel, Meredith Wilson, Tony Roscioli, John Christodoulou, Timothy C. Cox, Elaine H. Zackai, Francesco Brancati, Hakon Hakonarson, and Elizabeth J. Bhoj. Pathogenic variants in cdh11 impair cell adhesion and cause teebi hypertelorism syndrome. Human Genetics, 140:1061-1076, Apr 2021. URL: https://doi.org/10.1007/s00439-021-02274-3, doi:10.1007/s00439-021-02274-3. This article has 12 citations and is from a peer-reviewed journal.

13. (li2021pathogenicvariantsin pages 8-9): Dong Li, Michael E. March, Paola Fortugno, Liza L. Cox, Leticia S. Matsuoka, Rosanna Monetta, Christoph Seiler, Louise C. Pyle, Emma C. Bedoukian, María José Sánchez-Soler, Oana Caluseriu, Katheryn Grand, Allison Tam, Alicia R. P. Aycinena, Letizia Camerota, Yiran Guo, Patrick Sleiman, Bert Callewaert, Candy Kumps, Annelies Dheedene, Michael Buckley, Edwin P. Kirk, Anne Turner, Benjamin Kamien, Chirag Patel, Meredith Wilson, Tony Roscioli, John Christodoulou, Timothy C. Cox, Elaine H. Zackai, Francesco Brancati, Hakon Hakonarson, and Elizabeth J. Bhoj. Pathogenic variants in cdh11 impair cell adhesion and cause teebi hypertelorism syndrome. Human Genetics, 140:1061-1076, Apr 2021. URL: https://doi.org/10.1007/s00439-021-02274-3, doi:10.1007/s00439-021-02274-3. This article has 12 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Elsahy-Waters_Syndrome-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Elsahy-Waters_Syndrome-deep-research-falcon_artifacts/artifact-01.md)