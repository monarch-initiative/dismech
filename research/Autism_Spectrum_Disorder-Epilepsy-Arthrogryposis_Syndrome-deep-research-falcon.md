---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-30T23:48:36.074617'
end_time: '2026-07-30T23:56:24.539557'
duration_seconds: 468.47
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autism Spectrum Disorder-Epilepsy-Arthrogryposis Syndrome
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 11
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Autism_Spectrum_Disorder-Epilepsy-Arthrogryposis_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autism Spectrum Disorder-Epilepsy-Arthrogryposis Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autism Spectrum Disorder-Epilepsy-Arthrogryposis Syndrome** covering all of the
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
- **Disease Name:** Autism Spectrum Disorder-Epilepsy-Arthrogryposis Syndrome
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autism Spectrum Disorder-Epilepsy-Arthrogryposis Syndrome** covering all of the
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


# Autism Spectrum Disorder–Epilepsy–Arthrogryposis Syndrome

## Executive summary

Autism spectrum disorder–epilepsy–arthrogryposis syndrome is an ultra-rare, autosomal-recessive congenital disorder of glycosylation caused by biallelic pathogenic variants in **SLC35A3**. It is also called **SLC35A3-CDG**. The disorder combines congenital joint and skeletal abnormalities—particularly arthrogryposis—with developmental impairment/autistic features and epilepsy. The best current case synthesis identifies only **12 reported patients**, so phenotype frequencies, penetrance, prognosis, and genotype–phenotype relationships remain poorly quantified. Two reported patients died at 21 days and 9 years, but severity ranges from mild to profound. (OpenTargets Search: Autism spectrum disorder-epilepsy-arthrogryposis syndrome, kamiyama2024solutecarrierfamily pages 11-12, quelhas2026cdgdueto pages 5-6)

The disease mechanism is impaired transport of UDP-N-acetylglucosamine (UDP-GlcNAc) into the Golgi apparatus, disturbing glycan and proteoglycan biosynthesis needed for neural, cartilage, vertebral, and joint development. Patient fibroblasts have shown reduced Golgi UDP-GlcNAc transport and reduced highly branched cell-surface N-glycans. Mouse and cattle findings provide strong orthogonal support for the skeletal mechanism. No disease-modifying treatment or syndrome-specific clinical trial was identified; management is multidisciplinary and symptomatic. (kamiyama2024solutecarrierfamily pages 11-12, szulc2020biosynthesisofglcnacrich pages 1-2, quelhas2026cdgdueto pages 5-6)

| domain | established finding | evidence type/strength | ontology/database annotation |
|---|---|---|---|
| Disease identity | Ultra-rare Mendelian syndrome characterized by autism/neurodevelopmental impairment, epilepsy/seizures, and congenital arthrogryposis with skeletal abnormalities; represented in Orphanet as Autism spectrum disorder-epilepsy-arthrogryposis syndrome (Orphanet 370943) and linked to SLC35A3 (OpenTargets Search: Autism spectrum disorder-epilepsy-arthrogryposis syndrome, kamiyama2024solutecarrierfamily pages 11-12, quelhas2026cdgdueto pages 5-6) | Curated disease database association plus review synthesis of primary case reports; moderate | Orphanet: 370943; disease label: SLC35A3-CDG / autism spectrum disorder-epilepsy-arthrogryposis syndrome |
| Causal gene | Causal gene is SLC35A3, encoding a Golgi nucleotide-sugar transporter with UDP-GlcNAc transport activity (OpenTargets Search: Autism spectrum disorder-epilepsy-arthrogryposis syndrome, kamiyama2024solutecarrierfamily pages 11-12) | Strong molecular and disease-association evidence; human disease and transporter biology | Gene: SLC35A3; protein class: solute carrier family 35; pathway theme: Golgi glycosylation |
| Inheritance | Reported human disease is autosomal recessive due to biallelic pathogenic variants in SLC35A3 (kamiyama2024solutecarrierfamily pages 11-12, quelhas2026cdgdueto pages 5-6) | Human case-based evidence summarized in reviews; moderate | Inheritance: autosomal recessive |
| Epidemiology | Twelve patients have been reported, including a large kindred with eight patients and two siblings; no reliable population prevalence or incidence estimate is available (quelhas2026cdgdueto pages 5-6) | Review summary of published human cases; moderate for case count, weak for epidemiology | Evidence note: ultra-rare disorder; no population registry estimate |
| Core congenital musculoskeletal phenotype | Predominant problems involve skeleton and joints, especially congenital arthrogryposis mainly affecting hands and feet, short long bones, and broader skeletal defects including vertebral anomalies/CMV-like changes (kamiyama2024solutecarrierfamily pages 11-12, quelhas2026cdgdueto pages 5-6) | Human clinical evidence with supportive animal/model concordance; moderate-strong | HPO suggestions: Arthrogryposis multiplex congenita; Congenital joint contractures; Short long bones; Vertebral anomaly |
| Craniofacial and growth phenotype | Reported associated features include microcephaly and facial dysmorphism, including retromicrognathy and cleft palate (quelhas2026cdgdueto pages 5-6) | Human clinical evidence; moderate | HPO suggestions: Microcephaly; Facial dysmorphism; Retrognathia/micrognathia; Cleft palate |
| Neurodevelopmental phenotype | Patients show impaired intellectual/neurodevelopmental development; syndrome name and original disease entity include autism spectrum disorder (kamiyama2024solutecarrierfamily pages 11-12, OpenTargets Search: Autism spectrum disorder-epilepsy-arthrogryposis syndrome) | Human disease reports summarized in reviews and curated database label; moderate | HPO suggestions: Global developmental delay; Intellectual disability; Autism spectrum disorder / autistic behavior |
| Seizure phenotype | Seizures/epilepsy are a recurring core feature; disease severity ranges from mild to profound (kamiyama2024solutecarrierfamily pages 11-12, quelhas2026cdgdueto pages 5-6) | Human case evidence; moderate | HPO suggestions: Seizure; Epilepsy |
| Natural history / prognosis | Clinical severity ranges from mild to profound; 2 reported deaths occurred at 21 days and 9 years, indicating that severe early-life and childhood mortality can occur (quelhas2026cdgdueto pages 5-6) | Small-case natural history evidence; limited-moderate | Outcome annotation: variable severity; possible early mortality |
| Molecular mechanism | SLC35A3 is a Golgi UDP-GlcNAc transporter; disease mechanism is impaired Golgi UDP-GlcNAc transport causing abnormal glycosylation, including reduced highly branched N-glycans and likely broader effects on proteoglycans/GAG-related development (kamiyama2024solutecarrierfamily pages 11-12) | Strong mechanistic evidence from transporter biology, patient cells, and models | GO/pathway suggestions: UDP-N-acetylglucosamine transport; Golgi apparatus; protein glycosylation; glycosaminoglycan biosynthesis |
| Patient-cell functional evidence | Golgi vesicles isolated from patient fibroblasts showed significantly reduced UDP-GlcNAc transport activity; patient fibroblasts supported a glycosylation defect with reduced highly branched N-glycans on the cell surface (kamiyama2024solutecarrierfamily pages 11-12) | Direct human functional evidence; strong | Cell type: fibroblast; assay class: Golgi vesicle transport / glycosylation profiling |
| Comparative / animal evidence | Bovine SLC35A3 missense variation causes complex vertebral malformation with vertebral defects, arthrogryposis, craniofacial anomalies, and perinatal lethality; Slc35a3-null mice show chondrodysplasia, CMV-like vertebral anomalies, reduced cartilage ECM/proteoglycans, and perinatal lethality (kamiyama2024solutecarrierfamily pages 11-12) | Strong comparative/model support for skeletal-development mechanism | Species/model annotation: cattle natural disease; mouse knockout; phenotype theme: vertebral malformation / chondrodysplasia |
| Cellular models | CRISPR SLC35A3-knockout mammalian cell lines show context-dependent glycosylation effects, supporting a role in Golgi UDP-GlcNAc handling while also suggesting compensatory/alternative transport mechanisms (szulc2020biosynthesisofglcnacrich pages 18-20, szulc2020biosynthesisofglcnacrich pages 1-2) | In vitro mechanistic evidence; moderate | Model annotation: CRISPR knockout cell lines (CHO, HEK293T, HepG2) |
| Diagnosis | Recommended diagnosis is direct gene or exome sequencing demonstrating biallelic SLC35A3 variants in a compatible phenotype; functional studies in fibroblasts can support pathogenicity where available (quelhas2026cdgdueto pages 5-6, kamiyama2024solutecarrierfamily pages 11-12) | Review/guideline-style recommendation supported by human functional evidence; moderate | Diagnostic annotation: exome sequencing; genome/gene sequencing; functional fibroblast testing |
| Treatment | No disease-specific therapy is established; treatment is reported as purely symptomatic/supportive (quelhas2026cdgdueto pages 5-6) | Review summary; moderate | MAXO-style suggestions: symptomatic treatment; seizure management; orthopedic management; developmental therapies |
| Major evidence gaps | Very small number of published patients, sparse variant-level public detail in available sources, no validated biomarkers or disease-specific therapy, no clinical trials found, and no robust prevalence, penetrance, QoL, or longitudinal natural-history datasets (quelhas2026cdgdueto pages 5-6, kamiyama2024solutecarrierfamily pages 11-12) | High-confidence gap assessment based on absence/scarcity of evidence; strong for gap statement | Knowledge-base flags: evidence sparse; ultra-rare; natural history unknown; no interventional trials identified |


*Table: This table summarizes the most actionable disease facts for Autism spectrum disorder-epilepsy-arthrogryposis syndrome, focusing on established human findings, mechanism, diagnosis, models, and current evidence gaps. It is designed as a compact knowledge-base artifact with ontology and database mapping cues.*

## 1. Disease information

### Definition and classification

This is a **Mendelian neurodevelopmental–skeletal syndrome** within the congenital disorders of glycosylation. Its defining clinical triad is neurodevelopmental impairment/autism, epilepsy or seizures, and congenital arthrogryposis. Skeletal dysplasia and craniofacial abnormalities broaden the recognized phenotype. The disease-level association with **SLC35A3** is independently represented in Open Targets. (OpenTargets Search: Autism spectrum disorder-epilepsy-arthrogryposis syndrome, kamiyama2024solutecarrierfamily pages 11-12)

### Identifiers and synonyms

- **Preferred name:** Autism spectrum disorder–epilepsy–arthrogryposis syndrome.
- **Established synonyms:** SLC35A3-CDG; SLC35A3-related congenital disorder of glycosylation; SLC35A3-related arthrogryposis–neurodevelopmental syndrome.
- **Orphanet:** **ORPHA:370943**. (OpenTargets Search: Autism spectrum disorder-epilepsy-arthrogryposis syndrome)
- **Gene:** **SLC35A3**, Ensembl **ENSG00000117620**, approved name “solute carrier family 35 member A3.” (OpenTargets Search: Autism spectrum disorder-epilepsy-arthrogryposis syndrome)
- **OMIM/MONDO:** The exact current record numbers were not independently returned by the available tools and should be verified directly before database ingestion. The label is present in disease-ontology aggregation, but an unverified identifier should not be asserted.
- **ICD-10/ICD-11 and MeSH:** No syndrome-specific code was identified. Clinical coding ordinarily requires component or broader rare-genetic-disease codes for congenital arthrogryposis, developmental disorder, epilepsy, and congenital disorder of glycosylation.

The evidence is primarily **aggregated disease-level evidence derived from published individual cases and families**, not an EHR-derived population cohort. The 2026 synthesis reports 12 patients, including eight members of a large kindred and a separate sibling pair. (quelhas2026cdgdueto pages 5-6)

## 2. Etiology

### Causal factor

The primary cause is **biallelic germline loss-of-function or function-impairing variation in SLC35A3**, inherited in an autosomal-recessive pattern. SLC35A3 encodes a multi-pass Golgi nucleotide-sugar transporter associated with UDP-GlcNAc delivery for glycosylation. (kamiyama2024solutecarrierfamily pages 11-12)

A concise statement from the 2024 transporter review is: **“In 2013, Edvardson et al. identified deleterious mutations in SLC35A3 in patients with arthrogryposis, impaired intellectual development, and seizures.”** (kamiyama2024solutecarrierfamily pages 11-12)

### Genetic risk factors

The decisive risk factor is inheritance of two pathogenic SLC35A3 alleles. Consanguinity is relevant because recessive alleles can become homozygous in related parents, and the original literature included a large kindred; however, a quantitative consanguinity-associated risk estimate is unavailable. No validated susceptibility loci, modifier genes, founder effect, or carrier-frequency estimate has been established. (quelhas2026cdgdueto pages 5-6)

Variant-level assertions should be taken from the original reports or current ClinVar records during curation. The retrieved evidence supports deleterious biallelic variants and subsequent missense/splice-related reports, but did not provide a complete, consistently transcript-normalized list suitable for clinical annotation.

### Environmental, infectious, and lifestyle factors

No toxin, infection, diet, parental behavior, occupational exposure, or lifestyle factor is known to cause this syndrome. It is a constitutional genetic disorder. Environment can affect general health, seizure threshold, contracture complications, and access to rehabilitation, but these are modifiers of clinical status rather than causes of SLC35A3-CDG.

### Protective factors and gene–environment interaction

No protective allele, diet, supplement, drug, or environmental intervention has been validated. No disease-specific gene–environment interaction has been demonstrated. Avoid extrapolating galactose supplementation used experimentally in some other transporter CDGs to SLC35A3-CDG; no corresponding therapeutic evidence was identified here.

## 3. Phenotypes

Because only 12 patients are summarized in the current literature, most frequencies cannot be estimated reliably. Terms below should therefore be annotated as **reported**, not universally present. (quelhas2026cdgdueto pages 5-6)

### Congenital musculoskeletal phenotype

- **Arthrogryposis/congenital multiple-joint contractures:** predominantly hands and feet; congenital, non-progressive as a malformation, although functional consequences can evolve with growth.
- **Short long bones and skeletal dysplasia:** variable severity.
- **Vertebral abnormalities:** may resemble complex vertebral malformation.
- **Potential associated joint limitation and orthopedic disability:** likely to impair positioning, mobility, dressing, hygiene, and activities of daily living.

Suggested HPO terms include **Arthrogryposis multiplex congenita**, **Congenital joint contracture**, **Abnormality of the hand**, **Abnormality of the foot**, **Short long bones**, **Skeletal dysplasia**, and **Abnormal vertebral morphology**. Exact HPO identifiers should be validated against the current HPO release. (kamiyama2024solutecarrierfamily pages 11-12, quelhas2026cdgdueto pages 5-6)

### Neurologic and behavioral phenotype

- **Global developmental delay/intellectual disability:** severity ranges from mild to profound.
- **Autistic behavior/autism spectrum disorder:** part of the original syndrome designation; detailed standardized DSM assessments are not consistently reported.
- **Epilepsy/seizures:** recurrent core manifestation; available evidence does not support a reliable syndrome-specific seizure-type distribution, onset median, or treatment-response rate.
- **Microcephaly:** reported in the current clinical synthesis.

Suggested HPO terms are **Global developmental delay**, **Intellectual disability**, **Autistic behavior**, **Seizure**, **Epilepsy**, and **Microcephaly**. Neurodevelopmental disability and epilepsy can substantially affect communication, education, independence, caregiver burden, and safety, but no EQ-5D, PROMIS, SF-36, or syndrome-specific quality-of-life study was found. (kamiyama2024solutecarrierfamily pages 11-12, quelhas2026cdgdueto pages 5-6)

### Craniofacial phenotype

Reported abnormalities include facial dysmorphism, retromicrognathia, and cleft palate. Suggested HPO terms include **Abnormal facial shape**, **Micrognathia/retrognathia**, and **Cleft palate**. Feeding, airway, speech, and dental effects should be assessed individually. (quelhas2026cdgdueto pages 5-6)

### Laboratory and biochemical phenotype

The most informative reported abnormality is functional rather than a routine serum result: Golgi vesicles from patient fibroblasts showed significantly reduced UDP-GlcNAc transport and markedly reduced highly branched N-glycans at the cell surface. A normal routine metabolic panel or even a nondiagnostic generic CDG screen would therefore not exclude the condition. (kamiyama2024solutecarrierfamily pages 11-12)

## 4. Genetic and molecular information

### Gene and protein

**SLC35A3** encodes a ubiquitously expressed Golgi membrane protein originally termed UGT-related protein 2. It was identified as a UDP-GlcNAc transporter through complementation experiments in *Kluyveromyces lactis* and subsequent mammalian studies. SLC35A3 shares sequence identity with other SLC35 nucleotide-sugar transporters, including SLC35A2 and SLC35A1. (kamiyama2024solutecarrierfamily pages 11-12)

### Pathogenic variants

Human disease results from **germline biallelic variants**. Reported classes across the SLC35A3 disease literature include function-impairing missense and splice variants; however, the retrieved material did not provide a complete ClinVar-grade list with HGVS transcript, ACMG classification, segregation, and gnomAD frequency. Those fields should be populated only after direct review of the original reports and current ClinVar/gnomAD entries.

There is no evidence that this is a somatic disorder. No recurrent chromosomal rearrangement, aneuploidy, repeat expansion, mitochondrial variant, or epigenetic lesion defines the syndrome. Modifier genes and disease-specific episignatures have not been established.

### Functional consequence

Patient fibroblast evidence supports reduced transporter activity and abnormal glycan branching. Nevertheless, modern CRISPR knockout experiments complicate a simplistic “sole UDP-GlcNAc transporter” model. In CHO cells, SLC35A3 knockout did not decrease vesicular UDP-GlcNAc transport and caused only subtle N-glycan effects; in HEK293T cells, transport decreased but was not abolished, while N-glycan branching could remain intact. These findings imply cell-type-dependent compensation, alternative transport routes, or transporter complexes. (szulc2020biosynthesisofglcnacrich pages 18-20, szulc2020biosynthesisofglcnacrich pages 1-2)

Thus, the best current interpretation is **partial failure of a Golgi nucleotide-sugar transport network**, with particularly important consequences in developing neural and skeletal tissues, rather than universal elimination of all GlcNAc-containing glycans.

## 5. Environmental information

No environmental contributor or infectious trigger has been demonstrated. Smoking, alcohol, exercise, diet, pollution, and radiation have no established etiologic role. Standard avoidance of seizure triggers and prevention of immobility-related complications are clinically sensible but do not constitute primary prevention of the genetic disorder.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic defect:** biallelic SLC35A3 variants impair the abundance, localization, stability, or transport function of the Golgi membrane protein.
2. **Transport defect:** insufficient or dysregulated UDP-GlcNAc entry into specific Golgi compartments reduces substrate availability to selected glycosyltransferases.
3. **Glycosylation defect:** abnormal N-glycan branching and likely disturbed proteoglycan/glycosaminoglycan production alter cell-surface and extracellular-matrix molecules.
4. **Skeletal-development consequences:** reduced or abnormal cartilage extracellular matrix disrupts chondrocyte organization, growth-plate architecture, vertebral segmentation, and joint development, producing skeletal dysplasia and arthrogryposis.
5. **Neural consequences:** altered glycosylation of molecules needed for neural development, synaptic organization, excitability, and cell–matrix interactions plausibly produces developmental impairment, autism-related behavior, and epilepsy. The exact neuronal glycoproteins responsible remain unidentified. (kamiyama2024solutecarrierfamily pages 11-12)

### Pathways and ontology suggestions

Suggested GO biological-process concepts include **nucleotide-sugar transmembrane transport**, **UDP-N-acetylglucosamine transport**, **protein N-linked glycosylation**, **glycosaminoglycan biosynthetic process**, **proteoglycan biosynthetic process**, **cartilage development**, **skeletal-system development**, and **nervous-system development**. Suggested GO cellular components are **Golgi membrane**, **Golgi apparatus**, and **Golgi lumen**. Relevant chemical concepts include UDP-N-acetyl-D-glucosamine and N-acetyl-D-glucosamine; CHEBI identifiers should be checked against the current release before ingestion.

Suggested cell types include **chondrocyte** (CL mapping), proliferative growth-plate chondrocyte, fibroblast, neuron, and neural progenitor cell. Of these, direct patient evidence is strongest for fibroblasts; chondrocyte involvement is strongly supported by the knockout mouse. (kamiyama2024solutecarrierfamily pages 11-12)

### Immune, metabolic, and omics findings

No syndrome-specific chronic inflammation, autoimmunity, immunodeficiency, oxidative injury, mitochondrial defect, or characteristic small-molecule metabolomic signature has been established. No disease-specific patient single-cell, spatial-transcriptomic, proteomic, lipidomic, or integrated multi-omic study was identified. The available molecular profiling is principally glycan analysis and targeted transport assays.

## 7. Anatomical structures affected

The primary systems are:

- **Central nervous system:** brain development and neuronal function; suggested UBERON concepts include brain and central nervous system.
- **Musculoskeletal system:** joints of hands and feet, vertebral column, long bones, cartilage, and growth plates.
- **Craniofacial structures:** mandible and palate.
- **Tissue level:** nervous tissue, cartilage, connective tissue, extracellular matrix, and skeletal tissues.
- **Subcellular level:** Golgi membrane/lumen.

No consistent unilateral or lateralized pattern is established. Skeletal involvement is generally multiple and often bilateral. Mouse evidence specifically demonstrates altered growth-plate cartilage extracellular matrix and abnormal proliferative chondrocyte morphology. (kamiyama2024solutecarrierfamily pages 11-12, quelhas2026cdgdueto pages 5-6)

## 8. Temporal development and natural history

Arthrogryposis and structural skeletal abnormalities are **prenatal/congenital**, indicating a critical developmental window before birth. Neurodevelopmental impairment becomes evident in infancy or childhood, while seizures may occur early, but the available case synthesis does not establish a reliable median age at seizure onset. The disorder is lifelong; congenital contractures are not intrinsically degenerative, although orthopedic consequences can change during growth. (kamiyama2024solutecarrierfamily pages 11-12, quelhas2026cdgdueto pages 5-6)

There is no validated stage system, remission pattern, or longitudinal natural-history model. Neurodevelopmental gains may occur with therapy, and epilepsy may respond variably to standard antiseizure treatment, but reversal of the underlying developmental abnormalities has not been shown.

## 9. Inheritance and population

### Epidemiology

Only **12 patients** were summarized in the latest retrieved review. This is a published-case count, not prevalence. No incidence per 100,000, geographic distribution, sex ratio, ethnic enrichment, carrier frequency, or population-registry estimate is available. Publication and ascertainment bias are substantial. (quelhas2026cdgdueto pages 5-6)

### Inheritance and counseling

Inheritance is autosomal recessive. For two confirmed heterozygous parents, each pregnancy conventionally carries a 25% probability of an affected child, a 50% probability of an unaffected carrier, and a 25% probability of inheriting neither familial variant. Penetrance among individuals with clearly pathogenic biallelic genotypes appears high, but expressivity is markedly variable. No anticipation is expected. Germline mosaicism has not been specifically quantified and is less central than parental carrier status.

## 10. Diagnostics

### Clinical recognition

Consider SLC35A3-CDG when congenital arthrogryposis or vertebral/skeletal dysplasia co-occurs with developmental delay, autistic features, microcephaly, or epilepsy. Craniofacial findings such as micrognathia or cleft palate increase suspicion but are not required. (kamiyama2024solutecarrierfamily pages 11-12, quelhas2026cdgdueto pages 5-6)

### Recommended genetic approach

1. **Trio whole-exome or whole-genome sequencing** is the most efficient approach for an unsolved syndromic presentation.
2. A comprehensive **developmental epileptic encephalopathy, arthrogryposis, skeletal-dysplasia, or CDG panel** should include SLC35A3 and provide deletion/duplication analysis.
3. Confirm candidate variants by orthogonal testing and parental segregation.
4. Use **RNA analysis** for suspected splice variants when feasible.
5. Patient-fibroblast UDP-GlcNAc transport and glycan-branching studies can supply functional evidence for uncertain variants, although these are specialized research assays. (kamiyama2024solutecarrierfamily pages 11-12, quelhas2026cdgdueto pages 5-6)

CMA can detect an alternative pathogenic copy-number disorder but will generally miss small biallelic SLC35A3 variants. Routine karyotyping, FISH, mitochondrial sequencing, and repeat-expansion testing are not first-line disease-specific tests.

### Phenotype assessment

Recommended baseline evaluations include neurologic examination, EEG for suspected seizures, brain MRI when clinically indicated, developmental/autism assessment, orthopedic examination, spine and limb radiography, feeding/swallowing and airway assessment when micrognathia or cleft palate is present, and hearing/vision assessment as part of comprehensive neurodevelopmental care.

### Differential diagnosis

Important alternatives include other congenital disorders of glycosylation; SCYL2-related arthrogryposis multiplex congenita 4; NALCN-related CLIFAHDD; MAGEL2-related Schaaf–Yang syndrome; CNTNAP1-related lethal congenital contracture syndrome; PIEZO2-, ECEL1-, MYH3-, TPM2-, and ZC4H2-related arthrogryposis disorders; and other developmental epileptic encephalopathies with congenital contractures. The distinguishing feature is demonstration of pathogenic biallelic SLC35A3 variants, ideally with functional support.

## 11. Outcome and prognosis

Severity is highly variable, from mild to profound. In the 12-patient synthesis, two deaths occurred—at **21 days** and **9 years**—but this cannot be converted into a valid mortality rate because of tiny sample size, incomplete follow-up, and ascertainment bias. No median survival or life-expectancy estimate exists. (quelhas2026cdgdueto pages 5-6)

Likely long-term morbidity includes intellectual and communication disability, epilepsy, impaired mobility and self-care from contractures or skeletal deformity, orthopedic pain, feeding/speech issues in patients with palatal or mandibular abnormalities, and substantial caregiver burden. No validated disease-specific prognostic biomarker or quality-of-life instrument has been studied.

## 12. Treatment

No approved molecular, gene, RNA, cell, or substrate-replacement therapy exists. The recent transporter-CDG review characterizes treatment as **“purely symptomatic.”** (quelhas2026cdgdueto pages 5-6)

A practical multidisciplinary strategy is:

- **Epilepsy:** standard seizure-type-directed antiseizure medication; rescue plan; consider ketogenic diet, vagus-nerve stimulation, or epilepsy surgery only under usual drug-resistant-epilepsy criteria—not as syndrome-specific therapy.
- **Musculoskeletal disease:** early physiotherapy, stretching and positioning, occupational therapy, splinting/orthoses, mobility equipment, surveillance for spine/hip/limb deformity, and individualized orthopedic surgery.
- **Development and autism-related disability:** early-intervention services, speech/language therapy, augmentative communication, behavioral and educational support.
- **Cleft palate/micrognathia:** craniofacial, ENT, dental, feeding, speech, and airway management.
- **Nutrition and safety:** swallowing assessment, nutrition support, bone-health monitoring, and prevention of aspiration, pressure injury, and contracture complications.

Suggested MAXO concepts include genetic counseling, exome sequencing, electroencephalography, brain MRI, radiography, antiseizure pharmacotherapy, physical therapy, occupational therapy, speech therapy, orthotic treatment, orthopedic surgery, nutritional support, and developmental intervention. Exact MAXO identifiers should be validated before entry.

No disease-specific ClinicalTrials.gov study was found. There are no SLC35A3-specific response rates or pharmacogenomic recommendations.

## 13. Prevention

Primary lifestyle prevention is not possible. Reproductive prevention options for a family with known pathogenic variants include carrier testing of relatives, cascade screening, prenatal diagnosis, and preimplantation genetic testing for monogenic disease. Secondary prevention consists of early molecular diagnosis, seizure recognition, developmental intervention, and orthopedic surveillance. Tertiary prevention targets contracture progression, aspiration, injury from seizures, immobility, and loss of function.

There is no relevant vaccine or antimicrobial prophylaxis. Genetic counseling is the principal preventive intervention.

## 14. Other species and natural disease

A naturally occurring SLC35A3 disorder is well established in **Holstein Friesian cattle**. Homozygosity for bovine **p.Val180Phe** causes autosomal-recessive complex vertebral malformation, with cervical/thoracic vertebral defects, malformed ribs, craniofacial dysmorphism, lower-limb arthrogryposis, cardiac anomalies, and frequent intrauterine or perinatal death; heterozygotes are asymptomatic. This is a close comparative model of the human skeletal phenotype, although autism and epilepsy cannot be considered equivalently modeled. (kamiyama2024solutecarrierfamily pages 11-12)

The disease is not infectious and has no zoonotic or cross-species transmission risk.

## 15. Model organisms and experimental systems

### Mouse

CRISPR-generated **Slc35a3-null mice** display chondrodysplasia, complex-vertebral-malformation-like anomalies, and perinatal lethality. Growth-plate cartilage has markedly reduced extracellular matrix, altered proliferative chondrocyte morphology, and reduced heparan sulfate, keratan sulfate, and chondroitin/dermatan sulfate proteoglycans. This provides strong causal evidence linking SLC35A3 loss to defective cartilage matrix and skeletal development. The model is limited by perinatal lethality and does not establish the human behavioral or epilepsy phenotype. (kamiyama2024solutecarrierfamily pages 11-12)

### Cellular and yeast systems

Canine SLC35A3 complemented a *K. lactis* mutant lacking terminal GlcNAc, establishing transporter function. Mammalian CRISPR knockout models in CHO, HEK293T, and HepG2 cells demonstrate cell-context-dependent effects and suggest compensatory UDP-GlcNAc transport. These systems are useful for variant complementation, transport assays, glycomic analysis, and screening strategies, but they do not reproduce organism-level neurodevelopment. (kamiyama2024solutecarrierfamily pages 11-12, szulc2020biosynthesisofglcnacrich pages 18-20, szulc2020biosynthesisofglcnacrich pages 1-2)

## Recent developments and expert interpretation

The most important recent source is Kamiyama and Sone’s **August 2024** review, *Solute Carrier Family 35 (SLC35)—An Overview and Recent Progress*, DOI: https://doi.org/10.3390/biologics4030017. It integrates human fibroblast, cattle, and knockout-mouse evidence and concludes that SLC35A3 is essential for glycosylation of molecules involved in neural and skeletal development. (kamiyama2024solutecarrierfamily pages 11-12)

A key conceptual advance is that SLC35A3 is not necessarily the only route for mammalian Golgi UDP-GlcNAc delivery. The 2020 JBC knockout study found substantial cell-type dependence and residual transport, supporting redundancy or transporter cooperation: https://doi.org/10.1074/jbc.RA119.012362, published online September 16, 2020. (szulc2020biosynthesisofglcnacrich pages 18-20, szulc2020biosynthesisofglcnacrich pages 1-2)

The January 2026 membrane-transporter CDG update, DOI: https://doi.org/10.1002/jimd.70133, provides the latest retrieved clinical tally—12 patients—and emphasizes the wide severity range and absence of disease-specific treatment. Although later than the requested 2023–2024 priority window, it is currently the most useful consolidated clinical update. (quelhas2026cdgdueto pages 5-6)

## Evidence limitations and curation cautions

This knowledge base entry should be marked **low-count/high-uncertainty**. Most clinical claims derive from case reports and related families rather than independent population cohorts. Percentages should not be assigned to individual phenotypes unless extracted patient-by-patient from the primary reports. The two deaths among 12 published patients are observations, not a 16.7% disease mortality estimate. Similarly, the syndrome name should not be interpreted to mean that every molecularly confirmed patient necessarily has formally diagnosed autism, epilepsy, and arthrogryposis.

Primary landmark citation: Edvardson S, et al. *Mutations in SLC35A3 cause autism spectrum disorder, epilepsy and arthrogryposis.* **Journal of Medical Genetics**, September 2013;50:733–739. DOI: https://doi.org/10.1136/jmedgenet-2013-101753. Subsequent key human citation: Marini C, et al. *Recessive mutations in SLC35A3 cause early onset epileptic encephalopathy with skeletal defects.* **American Journal of Medical Genetics Part A**, April 2017;173:1119–1123. DOI: https://doi.org/10.1002/ajmg.a.38112. These primary papers should be consulted directly for final HGVS variant, patient-level frequency, segregation, and PMID fields before production database release.

References

1. (OpenTargets Search: Autism spectrum disorder-epilepsy-arthrogryposis syndrome): Open Targets Query (Autism spectrum disorder-epilepsy-arthrogryposis syndrome, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (kamiyama2024solutecarrierfamily pages 11-12): Shin Kamiyama and Hideyuki Sone. Solute carrier family 35 (slc35)—an overview and recent progress. Biologics, 4:242-279, Aug 2024. URL: https://doi.org/10.3390/biologics4030017, doi:10.3390/biologics4030017. This article has 14 citations and is from a peer-reviewed journal.

3. (quelhas2026cdgdueto pages 5-6): D. Quelhas, C. R. Ferreira, and J. Jaeken. <scp>cdg</scp> due to defective membrane transporters: update. Journal of Inherited Metabolic Disease, Jan 2026. URL: https://doi.org/10.1002/jimd.70133, doi:10.1002/jimd.70133. This article has 0 citations and is from a peer-reviewed journal.

4. (szulc2020biosynthesisofglcnacrich pages 1-2): Bozena Szulc, Paulina Sosicka, Dorota Maszczak-Seneczko, Edyta Skurska, Auhen Shauchuk, Teresa Olczak, Hudson H. Freeze, and Mariusz Olczak. Biosynthesis of glcnac-rich n- and o-glycans in the golgi apparatus does not require the nucleotide sugar transporter slc35a3. Journal of Biological Chemistry, 295:16445-16463, Nov 2020. URL: https://doi.org/10.1074/jbc.ra119.012362, doi:10.1074/jbc.ra119.012362. This article has 32 citations and is from a domain leading peer-reviewed journal.

5. (szulc2020biosynthesisofglcnacrich pages 18-20): Bozena Szulc, Paulina Sosicka, Dorota Maszczak-Seneczko, Edyta Skurska, Auhen Shauchuk, Teresa Olczak, Hudson H. Freeze, and Mariusz Olczak. Biosynthesis of glcnac-rich n- and o-glycans in the golgi apparatus does not require the nucleotide sugar transporter slc35a3. Journal of Biological Chemistry, 295:16445-16463, Nov 2020. URL: https://doi.org/10.1074/jbc.ra119.012362, doi:10.1074/jbc.ra119.012362. This article has 32 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Autism_Spectrum_Disorder-Epilepsy-Arthrogryposis_Syndrome-deep-research-falcon_artifacts/artifact-00.md)