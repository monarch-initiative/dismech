---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T00:41:51.735305'
end_time: '2026-07-31T00:49:27.935731'
duration_seconds: 456.2
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Bryant-Li-Bhoj Neurodevelopmental Syndrome 1
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 27
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Bryant-Li-Bhoj_Neurodevelopmental_Syndrome_1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bryant-Li-Bhoj Neurodevelopmental Syndrome 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Bryant-Li-Bhoj Neurodevelopmental Syndrome 1** covering all of the
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
- **Disease Name:** Bryant-Li-Bhoj Neurodevelopmental Syndrome 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Bryant-Li-Bhoj Neurodevelopmental Syndrome 1** covering all of the
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


# Bryant-Li-Bhoj Neurodevelopmental Syndrome 1: Disease Characteristics Report

**Scope and evidence date.** This report focuses on **Bryant-Li-Bhoj neurodevelopmental syndrome 1 (BLBS1)**, while using combined H3-3A/H3-3B cohorts where BLBS1-specific stratification was unavailable. The strongest clinical source is the 2024 international cohort of 96 affected individuals; mechanistic evidence comes principally from the 2020 discovery study and a 2023 H3.3-G34 mouse/cellular study. Because this is an ultra-rare, recently delineated disorder, many requested epidemiologic, prognostic, and therapeutic fields remain unknown.

| Domain | High-confidence summary | Ontology suggestions | Key citations |
|---|---|---|---|
| Disease / identifiers | Bryant-Li-Bhoj neurodevelopmental syndrome 1 (BLBS1) is a Mendelian neurodevelopmental/neurodegenerative disorder caused by germline H3-3A/H3F3A variants. MONDO:0030606. OMIM: 619720. Related entity: BLBS2/OMIM 619721 for H3-3B/H3F3B. Evidence is disease-level, aggregated from published case series/cohorts plus individual case reports. | MONDO:0030606 | (OpenTargets Search: Bryant-Li-Bhoj neurodevelopmental syndrome 1, layocarris2024expandedphenotypicspectrum pages 1-2) |
| Causal gene / inheritance | Causal gene for BLBS1: H3-3A / H3F3A (H3.3 histone A). Most reported BLBS1 variants are heterozygous, germline, and de novo; missense variants predominate. One inherited event has been reported in the broader BLBS literature, but de novo inheritance remains the rule. | Gene: H3-3A/H3F3A; inheritance term: autosomal dominant | (layocarris2024expandedphenotypicspectrum pages 8-9, layocarris2024expandedphenotypicspectrum pages 3-4, layocarris2024expandedphenotypicspectrum pages 1-2) |
| Foundational cohorts | Foundational human cohort: 46 patients in 2020. Expanded cohort: 96 individuals total in 2024 (47 male, 49 female; age range about 10 weeks/2 months to 39 years), including 65 with H3-3A variants and 31 with H3-3B variants. |  | (bryant2020histoneh3.3beyond pages 1-2, layocarris2024expandedphenotypicspectrum pages 3-4, layocarris2024expandedphenotypicspectrum pages 2-3) |
| Core phenotype frequencies | Developmental delay/intellectual disability 94/95 (99%); craniofacial anomalies 86/93 (92%); hypotonia 57/92 (62%); seizures 45/91 (49%); microcephaly 30/95 (32%); height ≤5th percentile 32/91 (35%); abnormal neuroimaging 44/76 (58%); corpus callosum malformation 37% (reported cohort frequency); oculomotor dysfunction 49/90 (54%); strabismus 32/90 (36%); musculoskeletal findings ~58-60%; dermal findings ~52-53%; cardiac abnormalities ~13-14%; genital abnormalities 20%. | HPO suggestions: developmental delay; intellectual disability; hypotonia; seizure; microcephaly; abnormality of head or neck; abnormal facial shape; strabismus; abnormality of the musculoskeletal system; corpus callosum abnormality | (hojo2024neonatalmyoclonusin pages 2-3, layocarris2024expandedphenotypicspectrum pages 4-6, layocarris2024expandedphenotypicspectrum pages 3-4) |
| Development / natural history | Usually congenital or infantile/early-childhood onset. Motor milestones are frequently delayed: delayed/no walking >20 months 59/75 (79%), delayed/no sitting >12 months 33/65 (51%). Language delay is common; only 50/84 were reported to speak words by >20 months. Phenotype is variable, and the syndrome is now framed as both neurodevelopmental and neurodegenerative. Some individuals show severe neonatal presentations (feeding difficulty, convulsions/myoclonus). | HPO suggestions: delayed ability to sit; delayed ability to walk; delayed speech and language development; feeding difficulties in infancy | (hojo2024neonatalmyoclonusin pages 2-3, layocarris2024expandedphenotypicspectrum pages 8-9, wei2024bryantlibhojneurodevelopmentalsyndrome pages 1-4) |
| Anatomy affected | Primary system: central nervous system, especially cerebrum/white matter and corpus callosum. Reported MRI abnormalities include delayed myelination/hypomyelination, corpus callosum dysgenesis/thinning, dilated ventricles, and hemispheric asymmetry. Secondary multisystem involvement includes craniofacial structures, eye/oculomotor system, musculoskeletal system, skin, heart, and genitalia. | UBERON suggestions: brain; corpus callosum; eye; skin; heart; musculoskeletal system. CL suggestion: neuron; microglial cell. | (layocarris2024expandedphenotypicspectrum pages 4-6, layocarris2024expandedphenotypicspectrum pages 8-9, khazaei2023singlesubstitutionin pages 1-3) |
| Molecular mechanism | H3.3 germline mutations disrupt histone-DNA, histone-histone, and histone-chaperone interactions and alter local histone PTM patterns. Patient-cell studies showed RNA-seq upregulation of mitosis/cell-cycle genes and increased proliferative capacity. For H3.3 G34 substitutions, a 2023 Cell study showed reduced H3K36me2 on mutant tails, impaired DNMT3A recruitment, redistribution of DNA methylation, and progressive neurodegeneration with neuronal loss and abnormal microglial accumulation. | GO suggestions: chromatin organization; nucleosome assembly; regulation of transcription by chromatin organization; histone H3-K36 methylation; DNA methylation. CL suggestion: neuron; microglial cell. | (bryant2020histoneh3.3beyond pages 1-2, bryant2020histoneh3.3beyond pages 7-8, khazaei2023singlesubstitutionin pages 1-3, wilson2022reprogrammingofthe pages 27-29) |
| Upstream/downstream pathophysiology | Upstream: pathogenic H3.3 amino-acid substitution in germline chromatin protein. Intermediate: altered chaperone binding/PTMs/H3K36 methylation and DNMT3A chromatin recruitment. Downstream: transcriptional dysregulation, abnormal proliferation programs, impaired neurodevelopment, and in some variants progressive neurodegeneration/neuroinflammation. | GO suggestions: protein-DNA complex assembly; histone modification; DNA methylation; regulation of cell cycle; neuroinflammatory response | (bryant2020histoneh3.3beyond pages 1-2, khazaei2023singlesubstitutionin pages 1-3) |
| Diagnostics | No syndrome-specific biochemical biomarker is established. Diagnosis currently relies on genomic testing, especially exome/genome sequencing in neurodevelopmental disorder workups; disease was repeatedly identified by WES/WGS in case series and clinical sequencing studies. Brain MRI is useful for supportive phenotyping; EEG may assist in seizure characterization. | Diagnostic ontology suggestions: MRI brain; exome sequencing; genome sequencing; EEG | (wei2024bryantlibhojneurodevelopmentalsyndrome pages 1-4, wei2024bryantlibhojneurodevelopmentalsyndrome pages 4-6, wei2024bryantlibhojneurodevelopmentalsyndrome pages 6-9, bryant2020histoneh3.3beyond pages 1-2) |
| Variant landscape | Reported pathogenic variants are mainly heterozygous germline missense substitutions, with additional synonymous and stop-loss variants described in the expanded cohort. Variants occur across the H3.3 protein; location within tail versus core appears to influence severity and growth/phenotypic pattern more than sex. |  | (layocarris2024expandedphenotypicspectrum pages 1-2, layocarris2024expandedphenotypicspectrum pages 3-4, layocarris2024expandedphenotypicspectrum pages 8-9) |
| Treatment / current care | No disease-modifying therapy is established. Real-world care is symptomatic and supportive: anti-seizure medications for epilepsy/myoclonus/convulsions (e.g., phenobarbital, levetiracetam, valproate in case reports), feeding support, developmental therapies, and multidisciplinary neurologic/rehabilitative management. | MAXO suggestions: anticonvulsant therapy; feeding support; physical therapy; occupational therapy; speech therapy; genetic counseling | (wei2024bryantlibhojneurodevelopmentalsyndrome pages 1-4, hojo2024neonatalmyoclonusin pages 2-3, wei2024bryantlibhojneurodevelopmentalsyndrome pages 6-9) |
| Prognosis | Prognosis is incompletely defined and likely variable. Severe disability is common; many patients have major motor and language delay. Progressive neurologic dysfunction/neurodegeneration has been reported in subsets, but longitudinal natural-history data remain sparse. A severe neonatal case reported death from aspiration at 39 days. | HPO suggestions: global developmental delay; neurodegeneration | (layocarris2024expandedphenotypicspectrum pages 8-9, wei2024bryantlibhojneurodevelopmentalsyndrome pages 4-6, wei2024bryantlibhojneurodevelopmentalsyndrome pages 6-9) |
| Epidemiology / population | Extremely rare; no robust prevalence or incidence estimates were identified. Current evidence derives from aggregated international case collections and individual case reports rather than population registries. No clear sex bias was observed in the 96-person cohort. |  | (layocarris2024expandedphenotypicspectrum pages 3-4, layocarris2024expandedphenotypicspectrum pages 2-3) |
| Models | Zebrafish h3f3a models showed craniofacial anomalies and defects in Foxd3-derived glia/neural crest-derived tissues. Mouse H3.3 G34R knock-in models showed progressive microcephaly/neurodegeneration with neuronal depletion and abnormal microglial accumulation. Patient-derived fibroblasts/lymphoblasts supported PTM, transcriptomic, and proliferation studies. | GO/CL suggestions: neural crest cell; glial cell; neuron; microglial cell | (bryant2020histoneh3.3beyond pages 7-8, bryant2020histoneh3.3beyond pages 1-2, khazaei2023singlesubstitutionin pages 1-3, wilson2022reprogrammingofthe pages 27-29) |
| Environmental factors / prevention | No validated environmental, lifestyle, toxin, or infectious causal factors have been established for BLBS1. No proven protective factors or gene-environment interactions are yet defined, though recent authors highlight them as an area for future study. Prevention currently centers on reproductive/genetic counseling rather than exposure modification. | MAXO suggestion: genetic counseling | (layocarris2024expandedphenotypicspectrum pages 1-2, layocarris2024expandedphenotypicspectrum pages 8-9) |
| Key evidence gaps | Major gaps include: no prevalence/incidence data; limited penetrance estimates; sparse long-term survival and QoL data; no validated prognostic biomarkers; no standard diagnostic criteria beyond molecular confirmation; no disease-modifying or targeted therapy; little evidence for epigenomic/transcriptomic diagnostics in practice; limited understanding of modifier genes and gene-environment interaction. |  | (layocarris2024expandedphenotypicspectrum pages 8-9, layocarris2024expandedphenotypicspectrum pages 1-2, layocarris2024expandedphenotypicspectrum pages 4-6) |


*Table: This table summarizes high-confidence, citable facts for Bryant-Li-Bhoj neurodevelopmental syndrome 1, including identifiers, genetics, phenotype frequencies, mechanism, diagnostics, treatment, prognosis, and evidence gaps. It is designed as a compact artifact for disease knowledge-base population.*

## 1. Disease information

BLBS1 is a rare **autosomal-dominant Mendelian chromatin disorder** caused by heterozygous germline variants in **H3-3A**, historically named **H3F3A**, which encodes histone H3.3. It is characterized chiefly by developmental delay/intellectual disability (DD/ID), abnormal muscle tone, craniofacial dysmorphism, epilepsy, growth abnormalities, and structural or maturational brain abnormalities. Although initially described as a progressive neurodegenerative condition, current understanding is that BLBS spans a heterogeneous **neurodevelopmental–neurodegenerative continuum**. The related BLBS2 phenotype is caused by H3-3B/H3F3B variants and is clinically overlapping. (layocarris2024expandedphenotypicspectrum pages 8-9, layocarris2024expandedphenotypicspectrum pages 1-2)

**Identifiers and synonyms**

- **MONDO:** MONDO:0030606.
- **OMIM:** **619720** for BLBS1; **619721** for BLBS2.
- **Causal target:** H3-3A/H3F3A, Ensembl ENSG00000163041; Open Targets reports a strong disease–target association supported by the foundational literature, including PMID **33268356**. (OpenTargets Search: Bryant-Li-Bhoj neurodevelopmental syndrome 1)
- **Synonyms:** Bryant-Li-Bhoj syndrome; BLBS; BRYLIB1; Bryant-Li-Bhoj neurodevelopmental syndrome type 1; H3F3A-related neurodevelopmental disorder; H3.3-related chromatinopathy.
- **Orphanet, MeSH, ICD-10/ICD-11:** no confidently disease-specific entries were identified. Clinically, nonspecific codes for developmental/intellectual disability, epilepsy, hypotonia, or congenital anomalies may be used, but these are not equivalent to a dedicated BLBS1 identifier.

The evidence is predominantly **aggregated disease-level information** assembled from international research cohorts and published case reports—not longitudinal EHR-derived population data. The 2024 cohort combined 58 previously published and 38 newly characterized unrelated individuals. (layocarris2024expandedphenotypicspectrum pages 1-2, layocarris2024expandedphenotypicspectrum pages 2-3)

**Key primary sources and abstract quotations**

- Bryant et al., *Science Advances*, published **4 December 2020**, DOI [10.1126/sciadv.abc9207](https://doi.org/10.1126/sciadv.abc9207), PMID **33268356**: “**Germ line mutations in H3F3A and H3F3B cause a previously unidentified neurodevelopmental syndrome.**” The study analyzed 46 affected individuals. (bryant2020histoneh3.3beyond pages 1-2)
- Layo-Carris et al., *European Journal of Human Genetics*, online **8 April 2024**, DOI [10.1038/s41431-024-01610-1](https://doi.org/10.1038/s41431-024-01610-1): “**In this larger cohort of 96 people, we identify causative missense, synonymous, and stop-loss variants.**” (layocarris2024expandedphenotypicspectrum pages 1-2)

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal factor

The primary cause is a **heterozygous germline H3-3A/H3F3A variant** affecting histone H3.3. Most established variants are de novo missense substitutions, although the broader BLBS cohort also contains synonymous and stop-loss variants. This is not an infectious, toxic, nutritional, or lifestyle-mediated disease. (layocarris2024expandedphenotypicspectrum pages 3-4, layocarris2024expandedphenotypicspectrum pages 1-2)

### Risk factors

- **Genetic:** the pathogenic H3-3A allele is the principal risk factor. Variants occur throughout the H3.3 tail and histone-fold core rather than at one hotspot. Protein position and affected paralog appear to influence severity, but robust variant-specific prediction is not yet possible. (layocarris2024expandedphenotypicspectrum pages 1-2)
- **Family history:** usually absent because variants are predominantly de novo. A maternally inherited H3-3B p.Asn108Ser variant has been reported in the broader syndrome, proving that inheritance is possible, but this does not establish BLBS1 penetrance. (layocarris2024expandedphenotypicspectrum pages 8-9)
- **Sex:** not a major risk factor. The expanded cohort was nearly balanced—47 male and 49 female—and gene/protein location appeared more influential than sex. (layocarris2024expandedphenotypicspectrum pages 3-4, layocarris2024expandedphenotypicspectrum pages 2-3)
- **Environmental, maternal-age, paternal-age, ethnic, occupational, or lifestyle risks:** none established.

### Protective factors and modifiers

No validated protective allele, modifier gene, diet, drug, or exposure has been demonstrated. Marked variability among individuals carrying the same variant implies unidentified genetic, epigenetic, developmental, stochastic, or environmental modifiers. The 2024 investigators explicitly proposed gene–environment interaction as a future research area, not as an established causal relationship. (layocarris2024expandedphenotypicspectrum pages 1-2)

## 3. Phenotypes

Frequencies below are primarily for the combined 96-person BLBS cohort; denominators differ because data were unavailable or participants were too young for particular milestones.

| Phenotype and type | Frequency/current characterization | Suggested HPO term |
|---|---:|---|
| DD/ID—developmental/behavioral | 94/95, **99%**; mild to profound, usually evident in infancy/childhood | Global developmental delay, **HP:0001263**; intellectual disability, **HP:0001249** |
| Delayed walking—motor sign | 59/75, **79%**, delayed beyond 20 months or absent | Delayed walking, **HP:0002062** |
| Delayed sitting—motor sign | 33/65, **51%**, beyond 12 months or absent | Delayed ability to sit, **HP:0025336** |
| Speech/language delay | Only 50/84 had words after the applicable age; approximately **60% delayed/no words** | Delayed speech and language development, **HP:0000750** |
| Hypotonia—neurologic sign | 57/92, **62%**; hypertonia or mixed tone can also occur | Muscular hypotonia, **HP:0001252**; hypertonia, **HP:0001276** |
| Seizures/epilepsy | 45/91, **49%**; focal, tonic, myoclonic, and tonic-clonic types | Seizure, **HP:0001250** |
| Abnormal MRI | 44/76, **58%**; delayed/hypomyelination, callosal dysgenesis/thinning, ventriculomegaly, asymmetry | Abnormal brain morphology, **HP:0012443**; abnormal corpus callosum morphology, **HP:0001273** |
| Corpus-callosum malformation | Approximately **37%** | Hypoplasia of corpus callosum, **HP:0002079** |
| Craniofacial anomalies | 86/93, **92%**; broad or narrow forehead, broad nasal bridge, hypertelorism, thin upper lip, micrognathia, ear/dental findings | Abnormal facial shape, **HP:0001999**; micrognathia, **HP:0000347** |
| Microcephaly | 30/95, **32%**; macrocephaly occurs in a smaller subgroup (~15%) | Microcephaly, **HP:0000252** |
| Short stature/undergrowth | 32/91, **35%** at or below fifth percentile | Short stature, **HP:0004322**; failure to thrive, **HP:0001508** |
| Oculomotor abnormality | 49/90, **54%**; strabismus 32/90, **36%** | Strabismus, **HP:0000486**; abnormal eye movement, **HP:0012372** |
| Musculoskeletal anomalies | Approximately **58–60%**; scoliosis, clubfoot, hip dysplasia, hypermobility | Abnormality of musculoskeletal system, **HP:0033127** |
| Dermal findings | Approximately **52–53%**; eczema, persistent fetal finger pads, nipple anomalies | Abnormality of skin, **HP:0000951** |
| Cardiac anomalies | Approximately **13–14%** | Congenital heart defect, **HP:0001627** |
| Genital anomalies | Approximately **20%** | Abnormality of genital system, **HP:0000119** |
| Feeding difficulty | Recurrent, including tube-feeding dependence in severe cases; cohort-wide frequency not securely extracted | Feeding difficulties, **HP:0011968** |
| Neonatal myoclonus | Newly expanded feature; may lack an ictal EEG correlate | Myoclonus, **HP:0001336** |

These frequencies and developmental outcomes are supported by the 2024 cohort and subsequent Japanese report. (hojo2024neonatalmyoclonusin pages 2-3, layocarris2024expandedphenotypicspectrum pages 4-6, layocarris2024expandedphenotypicspectrum pages 3-4)

A December 2024 Japanese case with H3F3A p.Ala48Gly broadened the phenotype to neonatal myoclonus; video-EEG did not establish that the neonatal movements were epileptic. At age 20 years, that individual could walk independently and speak simple words, demonstrating that profound motor impairment is not universal. The paper’s abstract states that BLBS is “**characterized by mild to severe developmental delay, intellectual disability, failure to thrive, muscle tone abnormalities, and dysmorphic facial features.**” DOI [10.1038/s41439-024-00303-x](https://doi.org/10.1038/s41439-024-00303-x), published **December 2024**. (hojo2024neonatalmyoclonusin pages 2-3, hojo2024neonatalmyoclonusin pages 3-4)

**Quality of life:** no BLBS-specific EQ-5D, SF-36, PROMIS, caregiver-burden, or utility study was identified. Nevertheless, absent/delayed walking, limited communication, epilepsy, feeding dependence, visual/hearing impairment, and orthopedic disease plausibly produce major lifelong effects on independence and caregiver needs. This is a clinical inference, not a quantified BLBS QoL result.

## 4. Genetic and molecular information

### Causal gene and variants

- **Gene:** H3-3A, approved symbol replacing historical **H3F3A**; protein: histone H3.3.
- **Disease relationship:** heterozygous germline H3-3A variants cause BLBS1. H3-3B/H3F3B causes BLBS2. (OpenTargets Search: Bryant-Li-Bhoj neurodevelopmental syndrome 1)
- **Variant spectrum:** mainly missense; synonymous and stop-loss alleles have also been assigned causality in the expanded BLBS cohort. Among 96 combined cases, 65 carried H3-3A and 31 H3-3B variants, representing 70 unique causative alleles. (layocarris2024expandedphenotypicspectrum pages 1-2, layocarris2024expandedphenotypicspectrum pages 2-3)
- **Examples:** p.Ala48Gly in a Japanese case; c.365C>G, reported as p.Pro122Arg in a Chinese preprint; germline G34R/V alleles occur in a mechanistically distinctive subgroup. Transcript/protein numbering should always be checked because historical reports contain nomenclature discrepancies. (wei2024bryantlibhojneurodevelopmentalsyndrome pages 1-4, hojo2024neonatalmyoclonusin pages 2-3, layocarris2024expandedphenotypicspectrum pages 8-9)
- **Origin:** germline, usually de novo. This sharply distinguishes BLBS1 from **somatic H3F3A oncohistone variants** causing gliomas or bone tumors. No concurrent malignancy was reported in the 2024 BLBS cohort. (layocarris2024expandedphenotypicspectrum pages 8-9)
- **Population frequency:** pathogenic variants are expected to be absent or extremely rare in population databases; variant-by-variant gnomAD counts were not available in the retrieved evidence and should be verified at ingestion time.
- **ACMG classification:** individual alleles require transcript-specific assessment using de novo status, absence from population databases, constrained gene/protein regions, phenotype match, and functional evidence. It is unsafe to assign one blanket ACMG category to every reported allele.

### Functional consequences and modifiers

BLBS is not a simple haploinsufficiency syndrome. Missense alleles alter nucleosomal contacts, H3.3-specific chaperone interactions, or post-translational modification states. Variant-specific dominant-negative or neomorphic effects are plausible, but no single mechanism explains every allele. Protein-tail variants were associated with more undergrowth, while gene and protein location contributed more to phenotype than sex; these remain trends rather than deterministic correlations. (layocarris2024expandedphenotypicspectrum pages 3-4, layocarris2024expandedphenotypicspectrum pages 1-2)

No validated modifier genes, recurrent chromosomal rearrangements, or syndrome-specific constitutional copy-number abnormalities are established. Epigenetic dysfunction is central to pathogenesis, but no validated diagnostic “episignature” was identified.

## 5. Environmental information

No toxin, radiation exposure, pollution source, occupation, diet, smoking, alcohol use, exercise pattern, or infectious agent is known to cause or trigger BLBS1. Such factors should not be represented as established disease risks. Similarly, no environmental protective factor or prophylactic exposure modification has evidence. The disorder is genetic and constitutional.

## 6. Mechanism and pathophysiology

### General H3.3 mechanism

H3.3 is a replication-independent histone variant deposited into active chromatin by **HIRA** and into repetitive/telomeric regions by **ATRX–DAXX**. It accumulates in post-mitotic neurons and supports chromatin architecture, transcription, genome stability, and cellular memory. Germline substitutions can disturb contacts with DNA, adjacent histones, or chaperone proteins such as DAXX, UBN1, and ZMYND11. (morcos2025h3.3denovo pages 1-4, bryant2020histoneh3.3beyond pages 7-8)

**General causal chain:** germline H3-3A substitution → abnormal H3.3 nucleosome/chaperone interaction or local PTM state → altered chromatin accessibility and transcriptional regulation → disturbed cell-cycle/neural-crest/glial/neuronal development → congenital anomalies and DD/ID; for selected alleles, postnatal methylome disruption and neuroinflammation add progressive neurodegeneration. (bryant2020histoneh3.3beyond pages 7-8, bryant2020histoneh3.3beyond pages 1-2)

### Human-cell molecular profiling

The 2020 study modeled 37 variants and found disruptions of DNA, histone, and chaperone interactions. Patient histone analyses showed aberrant **local, cis PTM patterns**, unlike the broad trans effects associated with classic somatic oncohistones. RNA sequencing of patient-derived fibroblasts identified 323 upregulated genes enriched for mitosis/cell-cycle functions, and cellular assays demonstrated increased proliferation and altered S/G2 phases. (bryant2020histoneh3.3beyond pages 7-8, bryant2020histoneh3.3beyond pages 1-2, wilson2022reprogrammingofthe pages 27-29)

The abstract’s mechanistic summary is: “**RNA sequencing on patient cells demonstrated up-regulated gene expression related to mitosis and cell division, and cellular assays confirmed an increased proliferative capacity.**” (bryant2020histoneh3.3beyond pages 1-2)

### G34R/V-specific mechanism

The 2023 *Cell* study, DOI [10.1016/j.cell.2023.02.023](https://doi.org/10.1016/j.cell.2023.02.023), showed that H3.3-G34R markedly reduces H3K36me2 on the mutant tail, impairing recruitment and genomic localization of **DNMT3A**. Consequences include loss of neuronal non-CG/CH methylation, aberrant CG methylation including neuronal-promoter silencing, sustained complement/innate-immune transcription, abnormal microglial accumulation, neuronal depletion, progressive microcephaly, and neurodegeneration. G34V had a milder effect. This mechanism is compelling for G34 substitutions but should not be generalized to all H3-3A alleles. (khazaei2023singlesubstitutionin pages 1-3)

### Mechanism annotations

- **GO biological processes:** chromatin organization (GO:0006325); nucleosome assembly (GO:0006334); covalent chromatin modification (GO:0016569); DNA methylation (GO:0006306); histone H3-K36 methylation (GO:0010452); regulation of cell cycle (GO:0051726); neuroinflammatory response (GO:0150076).
- **GO cellular components:** nucleus (GO:0005634); nucleosome (GO:0000786); chromatin (GO:0000785).
- **Cell Ontology:** neuron (CL:0000540), microglial cell (CL:0000129), glial cell (CL:0000125), neural crest cell (CL:0000333), fibroblast (CL:0000057).
- **Metabolomics/lipidomics/proteomics:** no clinically validated disease signatures. Proteomic/PTM studies are research-grade.
- **Single-cell/spatial/multi-omics:** no BLBS1 patient single-cell or spatial atlas was identified. Mouse tissue and bulk patient-cell analyses currently dominate.
- **Immune involvement:** demonstrated principally for G34R model neuroinflammation; there is no evidence that BLBS1 is an autoimmune or primary immunodeficiency disorder. (khazaei2023singlesubstitutionin pages 1-3)

## 7. Anatomical structures affected

The **central nervous system** is primary, with involvement of cerebral white matter/myelination, corpus callosum, ventricles, and cerebral hemispheres. Neurons and glia are mechanistically implicated; microglia participate in G34R-associated degeneration. Craniofacial structures and neural-crest derivatives are also important, with secondary involvement of eyes/oculomotor pathways, skeleton/joints, skin, heart, and genital tract. (khazaei2023singlesubstitutionin pages 1-3, bryant2020histoneh3.3beyond pages 7-8, layocarris2024expandedphenotypicspectrum pages 4-6)

Suggested anatomy annotations include brain (**UBERON:0000955**), corpus callosum (**UBERON:0002336**), cerebral white matter (**UBERON:0002437**), eye (**UBERON:0000970**), skin (**UBERON:0002097**), and heart (**UBERON:0000948**). No consistent lateralization is established; hemispheric asymmetry can occur, but disease is generally systemic/bilateral.

## 8. Temporal development

Onset is typically congenital, neonatal, or early childhood and usually insidious as developmental milestones are missed. Feeding difficulty, hypotonia, dysmorphism, myoclonus, or seizures may be apparent neonatally. Ages in the 2024 cohort ranged from approximately 10 weeks to 39 years. (wei2024bryantlibhojneurodevelopmentalsyndrome pages 1-4, hojo2024neonatalmyoclonusin pages 2-3, layocarris2024expandedphenotypicspectrum pages 2-3)

The course is **chronic and lifelong**, but not uniformly progressive. Developmental impairment may remain relatively stable in some individuals, whereas regression/progressive neurologic dysfunction, microcephaly, or neurodegeneration occurs in subsets. Longitudinal data are too sparse to define stages, median progression rate, remission patterns, or critical treatment windows. Repeat developmental, neurologic, ophthalmologic, growth, and MRI assessment is reasonable because phenotype may evolve. (layocarris2024expandedphenotypicspectrum pages 8-9)

## 9. Inheritance and population

BLBS1 is autosomal dominant and usually caused by a de novo heterozygous allele. Penetrance appears high for neurodevelopmental manifestations among ascertained carriers, but ascertainment bias prevents a numerical penetrance estimate. Expressivity is markedly variable, including among people with the same variant. Anticipation, founder effects, carrier frequency, and a role for consanguinity are not established. Parental germline mosaicism has not been quantified but remains a general possibility after an apparently de novo result.

No prevalence or incidence per 100,000 is known. The condition is best described as **ultra-rare**, with 96 combined BLBS1/2 individuals in the largest 2024 cohort, not as a population prevalence estimate. The cohort’s 47:49 male:female distribution argues against sex bias. No ancestry or geographic enrichment is established. (layocarris2024expandedphenotypicspectrum pages 3-4, layocarris2024expandedphenotypicspectrum pages 2-3)

## 10. Diagnostics

### Recommended approach

1. Recognize unexplained DD/ID with hypotonia or mixed tone, craniofacial dysmorphism, epilepsy, growth abnormality, and/or atypical brain MRI.
2. Perform trio **exome or genome sequencing**, including de novo analysis and adequate coverage of H3-3A/H3F3A and H3-3B/H3F3B. WES identified the Chinese c.365C>G allele and has been central to cohort ascertainment. (wei2024bryantlibhojneurodevelopmentalsyndrome pages 1-4, wei2024bryantlibhojneurodevelopmentalsyndrome pages 4-6)
3. Confirm the variant by an orthogonal method when required and test both parents to establish de novo status or inheritance.
4. Interpret using current ACMG/AMP criteria, ClinVar submissions, phenotype fit, population frequency, and allele-specific functional evidence.

A neurodevelopmental/epilepsy/chromatinopathy panel containing **H3-3A and H3-3B** is appropriate when rapid panel testing is preferred. Single-gene sequencing can confirm a known familial allele but is less efficient for a genetically heterogeneous NDD. WGS can detect poorly covered exonic, intronic, mosaic, and structural variants, although demonstrated incremental BLBS1 yield is unknown.

CMA remains useful for unexplained DD/congenital anomalies but will ordinarily not detect a single-nucleotide H3-3A allele. Karyotype, FISH, mitochondrial sequencing, and repeat-expansion testing are not BLBS1-specific tests unless another differential diagnosis warrants them. No routine enzyme assay, metabolite, blood protein, biopsy, liquid biopsy, or validated methylation episignature exists.

### Clinical evaluation after diagnosis

- Brain MRI, ideally including myelination and corpus-callosum assessment.
- EEG for suspected seizures; prolonged video-EEG can distinguish nonepileptic neonatal myoclonus. (hojo2024neonatalmyoclonusin pages 2-3, hojo2024neonatalmyoclonusin pages 3-4)
- Developmental, speech/language, feeding/swallowing, hearing, ophthalmologic, growth, orthopedic, skin, cardiac, and genital examinations guided by symptoms.

### Differential diagnosis

Consider other chromatinopathies/histonopathies, cerebral palsy, leukodystrophies, Rett-spectrum disorders, epileptic encephalopathies, HIVEP2- and BCL11A-related NDDs, and other syndromic causes of callosal abnormality. Molecular confirmation is important because no pathognomonic clinical criterion exists.

Population newborn screening is unavailable. Cascade testing is indicated if a parental variant is found. Prenatal and preimplantation testing are technically possible once the familial pathogenic variant is established.

## 11. Outcome and prognosis

No 5- or 10-year survival estimate, life expectancy, mortality rate, or validated prognostic score exists. The oldest participant in the 2024 cohort was 39 years, showing survival into adulthood, but this cannot define average longevity. Severe motor and communication disability is common: 79% of evaluable individuals walked late or not at all, and substantial language impairment was present. (hojo2024neonatalmyoclonusin pages 2-3)

Potential complications include epilepsy, aspiration and feeding-related morbidity, impaired mobility, scoliosis/hip disease, visual or hearing impairment, and evolving neurologic dysfunction. One severe neonatal case reportedly died from aspiration at 39 days; this is a single case and should not be used to estimate syndrome-wide mortality. (wei2024bryantlibhojneurodevelopmentalsyndrome pages 4-6, wei2024bryantlibhojneurodevelopmentalsyndrome pages 6-9)

Variant position, affected paralog, initial neurologic severity, feeding safety, seizure burden, and progressive MRI changes may ultimately prove prognostic, but none is validated. No prognostic biomarker or standardized QoL instrument has been studied.

## 12. Treatment and current applications

There is **no approved disease-modifying, gene, cell, RNA, or epigenetic therapy** for BLBS1. No relevant BLBS-specific interventional clinical trial was identified in the ClinicalTrials.gov search.

Current real-world implementation is individualized supportive care:

- **Epilepsy:** standard antiseizure therapy selected by seizure type. Phenobarbital, levetiracetam, valproate, and pyridoxine were used in published cases; one adult’s seizures were well controlled with valproate or levetiracetam. These reports do not establish comparative efficacy. (wei2024bryantlibhojneurodevelopmentalsyndrome pages 1-4, hojo2024neonatalmyoclonusin pages 2-3)
- **Feeding/aspiration:** swallow evaluation, nutritional intervention, feeding therapy, thickening or enteral support when needed.
- **Development:** early physical, occupational, speech/language, augmentative-communication, educational, and behavioral services.
- **Motor/orthopedic:** tone management, mobility aids, orthotics, scoliosis and hip surveillance.
- **Vision/hearing:** correction and specialist management.
- **Genetic counseling:** recurrence-risk assessment and reproductive options.

Suggested MAXO annotations include genetic counseling (**MAXO:0001004**), exome sequencing, brain MRI, EEG, anticonvulsant therapy, physical therapy, occupational therapy, speech therapy, nutritional support, and gastrostomy where clinically necessary. Exact MAXO identifiers should be validated against the current ontology release before database ingestion.

No established pharmacogenomic recommendation exists. ASO therapy has been discussed broadly for nano-rare variants, including H3F3A submissions, but there is no published BLBS1 efficacy evidence and no basis for clinical use outside a regulated individualized program.

## 13. Prevention

Primary lifestyle or environmental prevention is not possible because most cases arise from de novo germline variation. Vaccination and antimicrobial prophylaxis have no disease-specific role.

- **Primary/reproductive prevention:** nondirective genetic counseling; parental testing; prenatal diagnosis or preimplantation genetic testing for a known familial pathogenic allele.
- **Secondary prevention:** early genomic diagnosis and early developmental intervention; there is no population newborn screen.
- **Tertiary prevention:** seizure control, aspiration prevention, nutrition optimization, mobility/contracture management, and surveillance for evolving neurologic, ophthalmologic, hearing, cardiac, and orthopedic complications.

After a confirmed de novo variant, recurrence risk is low but not zero because parental germline mosaicism cannot be excluded. If a parent is heterozygous, each pregnancy has a theoretical 50% transmission probability, with uncertain severity because expressivity is variable.

## 14. Other species and natural disease

No well-established naturally occurring BLBS-equivalent veterinary disease, affected breed, zoonotic potential, or cross-species transmission exists. BLBS1 is noninfectious. Orthologous H3.3 genes are deeply conserved across vertebrates, enabling experimentally induced models, but these should not be mislabeled as spontaneous animal disease.

Relevant taxa include human (*Homo sapiens*, NCBI Taxon **9606**), mouse (*Mus musculus*, **10090**), and zebrafish (*Danio rerio*, **7955**). Exact ortholog NCBI Gene identifiers should be retrieved from current NCBI/Alliance records during database normalization.

## 15. Model organisms

### Zebrafish

Experimental h3f3a perturbation reproduced craniofacial abnormalities, including severe jaw-cartilage loss, and reduced melanocytes, xanthophores, and Foxd3-derived glia. This supports disruption of neural-crest-derived craniofacial tissue and glial development. Its limitation is that severe embryonic perturbation may not reproduce the allele-specific heterozygous human spectrum. (bryant2020histoneh3.3beyond pages 7-8, bryant2020histoneh3.3beyond pages 1-2)

### Mouse

H3.3-G34R knock-in mice developed fully penetrant progressive microcephaly/neurodegeneration, neuronal depletion, abnormal microglial accumulation, methylome disruption, and innate-immune/complement activation; G34V was milder. This model is powerful for G34-specific DNMT3A/H3K36me2 mechanisms but cannot represent all dispersed BLBS1 variants. (khazaei2023singlesubstitutionin pages 1-3)

### Cellular models

Patient fibroblasts and lymphoblastoid cells revealed local histone-PTM abnormalities, increased proliferation, altered cell-cycle distribution, and mitosis/cell-division transcriptional upregulation. They are experimentally accessible but do not fully model post-mitotic human neurons. Patient-derived iPSC neurons or cerebral organoids would be valuable, but no mature BLBS1 iPSC/organoid natural-history platform was identified. (bryant2020histoneh3.3beyond pages 7-8, wilson2022reprogrammingofthe pages 27-29)

## Evidence appraisal and priority gaps

**High-confidence:** H3-3A causality; predominantly de novo dominant inheritance; DD/ID, dysmorphism, tone abnormalities, seizures, motor/language delay, and MRI abnormalities; local chromatin/PTM disruption; G34R-specific DNMT3A/methylome mechanism.

**Moderate-confidence:** variant-location genotype–phenotype trends, progressive neurodegeneration outside G34 alleles, and multisystem frequency estimates, because missing data and mixed BLBS1/BLBS2 analyses limit inference.

**Unknown/not established:** prevalence, penetrance, carrier frequency, environmental modifiers, standardized diagnostic criteria, methylation biomarker, QoL burden, life expectancy, prognostic biomarkers, natural animal disease, and disease-modifying treatment.

The highest priorities are prospective longitudinal natural-history studies, allele-stratified neuroimaging and developmental assessments, patient-derived neuronal models, systematic methylome/transcriptome profiling, modifier-gene studies, feeding/aspiration outcome research, and trial-ready outcome measures.

References

1. (OpenTargets Search: Bryant-Li-Bhoj neurodevelopmental syndrome 1): Open Targets Query (Bryant-Li-Bhoj neurodevelopmental syndrome 1, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (layocarris2024expandedphenotypicspectrum pages 1-2): Dana E. Layo-Carris, Emily E. Lubin, Annabel K. Sangree, Kelly J. Clark, Emily L. Durham, Elizabeth M. Gonzalez, Sarina Smith, Rajesh Angireddy, Xiao Min Wang, Erin Weiss, Annick Toutain, Roberto Mendoza-Londono, Lucie Dupuis, Nadirah Damseh, Danita Velasco, Irene Valenzuela, Marta Codina-Solà, Catherine Ziats, Jaclyn Have, Katie Clarkson, Dora Steel, Manju Kurian, Katy Barwick, Diana Carrasco, Aditi I. Dagli, M. J. M. Nowaczyk, Miroslava Hančárová, Šárka Bendová, Darina Prchalova, Zdeněk Sedláček, Alica Baxová, Catherine Bearce Nowak, Jessica Douglas, Wendy K. Chung, Nicola Longo, Konrad Platzer, Chiara Klöckner, Luisa Averdunk, Dagmar Wieczorek, Ilona Krey, Christiane Zweier, Andre Reis, Tugce Balci, Marleen Simon, Hester Y. Kroes, Antje Wiesener, Georgia Vasileiou, Nikolaos M. Marinakis, Danai Veltra, Christalena Sofocleous, Konstantina Kosma, Joanne Traeger Synodinos, Konstantinos A. Voudris, Marie-Laure Vuillaume, Paul Gueguen, Nicolas Derive, Estelle Colin, Clarisse Battault, Billie Au, Martin Delatycki, Mathew Wallis, Lyndon Gallacher, Fatma Majdoub, Noor Smal, Sarah Weckhuysen, An-Sofie Schoonjans, R. Frank Kooy, Marije Meuwissen, Benjamin T. Cocanougher, Kathryn Taylor, Carolyn E. Pizoli, Marie T. McDonald, Philip James, Elizabeth R. Roeder, Rebecca Littlejohn, Nicholas A. Borja, Willa Thorson, Kristine King, Radka Stoeva, Manon Suerink, Esther Nibbeling, Stephanie Baskin, Gwenaël L. E. Guyader, Julie Kaplan, Candace Muss, Deanna Alexis Carere, Elizabeth J. K. Bhoj, and Laura M. Bryant. Expanded phenotypic spectrum of neurodevelopmental and neurodegenerative disorder bryant-li-bhoj syndrome with 38 additional individuals. European Journal of Human Genetics, 32:928-937, Apr 2024. URL: https://doi.org/10.1038/s41431-024-01610-1, doi:10.1038/s41431-024-01610-1. This article has 12 citations and is from a domain leading peer-reviewed journal.

3. (layocarris2024expandedphenotypicspectrum pages 8-9): Dana E. Layo-Carris, Emily E. Lubin, Annabel K. Sangree, Kelly J. Clark, Emily L. Durham, Elizabeth M. Gonzalez, Sarina Smith, Rajesh Angireddy, Xiao Min Wang, Erin Weiss, Annick Toutain, Roberto Mendoza-Londono, Lucie Dupuis, Nadirah Damseh, Danita Velasco, Irene Valenzuela, Marta Codina-Solà, Catherine Ziats, Jaclyn Have, Katie Clarkson, Dora Steel, Manju Kurian, Katy Barwick, Diana Carrasco, Aditi I. Dagli, M. J. M. Nowaczyk, Miroslava Hančárová, Šárka Bendová, Darina Prchalova, Zdeněk Sedláček, Alica Baxová, Catherine Bearce Nowak, Jessica Douglas, Wendy K. Chung, Nicola Longo, Konrad Platzer, Chiara Klöckner, Luisa Averdunk, Dagmar Wieczorek, Ilona Krey, Christiane Zweier, Andre Reis, Tugce Balci, Marleen Simon, Hester Y. Kroes, Antje Wiesener, Georgia Vasileiou, Nikolaos M. Marinakis, Danai Veltra, Christalena Sofocleous, Konstantina Kosma, Joanne Traeger Synodinos, Konstantinos A. Voudris, Marie-Laure Vuillaume, Paul Gueguen, Nicolas Derive, Estelle Colin, Clarisse Battault, Billie Au, Martin Delatycki, Mathew Wallis, Lyndon Gallacher, Fatma Majdoub, Noor Smal, Sarah Weckhuysen, An-Sofie Schoonjans, R. Frank Kooy, Marije Meuwissen, Benjamin T. Cocanougher, Kathryn Taylor, Carolyn E. Pizoli, Marie T. McDonald, Philip James, Elizabeth R. Roeder, Rebecca Littlejohn, Nicholas A. Borja, Willa Thorson, Kristine King, Radka Stoeva, Manon Suerink, Esther Nibbeling, Stephanie Baskin, Gwenaël L. E. Guyader, Julie Kaplan, Candace Muss, Deanna Alexis Carere, Elizabeth J. K. Bhoj, and Laura M. Bryant. Expanded phenotypic spectrum of neurodevelopmental and neurodegenerative disorder bryant-li-bhoj syndrome with 38 additional individuals. European Journal of Human Genetics, 32:928-937, Apr 2024. URL: https://doi.org/10.1038/s41431-024-01610-1, doi:10.1038/s41431-024-01610-1. This article has 12 citations and is from a domain leading peer-reviewed journal.

4. (layocarris2024expandedphenotypicspectrum pages 3-4): Dana E. Layo-Carris, Emily E. Lubin, Annabel K. Sangree, Kelly J. Clark, Emily L. Durham, Elizabeth M. Gonzalez, Sarina Smith, Rajesh Angireddy, Xiao Min Wang, Erin Weiss, Annick Toutain, Roberto Mendoza-Londono, Lucie Dupuis, Nadirah Damseh, Danita Velasco, Irene Valenzuela, Marta Codina-Solà, Catherine Ziats, Jaclyn Have, Katie Clarkson, Dora Steel, Manju Kurian, Katy Barwick, Diana Carrasco, Aditi I. Dagli, M. J. M. Nowaczyk, Miroslava Hančárová, Šárka Bendová, Darina Prchalova, Zdeněk Sedláček, Alica Baxová, Catherine Bearce Nowak, Jessica Douglas, Wendy K. Chung, Nicola Longo, Konrad Platzer, Chiara Klöckner, Luisa Averdunk, Dagmar Wieczorek, Ilona Krey, Christiane Zweier, Andre Reis, Tugce Balci, Marleen Simon, Hester Y. Kroes, Antje Wiesener, Georgia Vasileiou, Nikolaos M. Marinakis, Danai Veltra, Christalena Sofocleous, Konstantina Kosma, Joanne Traeger Synodinos, Konstantinos A. Voudris, Marie-Laure Vuillaume, Paul Gueguen, Nicolas Derive, Estelle Colin, Clarisse Battault, Billie Au, Martin Delatycki, Mathew Wallis, Lyndon Gallacher, Fatma Majdoub, Noor Smal, Sarah Weckhuysen, An-Sofie Schoonjans, R. Frank Kooy, Marije Meuwissen, Benjamin T. Cocanougher, Kathryn Taylor, Carolyn E. Pizoli, Marie T. McDonald, Philip James, Elizabeth R. Roeder, Rebecca Littlejohn, Nicholas A. Borja, Willa Thorson, Kristine King, Radka Stoeva, Manon Suerink, Esther Nibbeling, Stephanie Baskin, Gwenaël L. E. Guyader, Julie Kaplan, Candace Muss, Deanna Alexis Carere, Elizabeth J. K. Bhoj, and Laura M. Bryant. Expanded phenotypic spectrum of neurodevelopmental and neurodegenerative disorder bryant-li-bhoj syndrome with 38 additional individuals. European Journal of Human Genetics, 32:928-937, Apr 2024. URL: https://doi.org/10.1038/s41431-024-01610-1, doi:10.1038/s41431-024-01610-1. This article has 12 citations and is from a domain leading peer-reviewed journal.

5. (bryant2020histoneh3.3beyond pages 1-2): Laura Bryant, Dong Li, Samuel G. Cox, Dylan Marchione, Evan F. Joiner, Khadija Wilson, Kevin Janssen, Pearl Lee, Michael E. March, Divya Nair, Elliott Sherr, Brieana Fregeau, Klaas J. Wierenga, Alexandrea Wadley, Grazia M. S. Mancini, Nina Powell-Hamilton, Jiddeke van de Kamp, Theresa Grebe, John Dean, Alison Ross, Heather P. Crawford, Zoe Powis, Megan T. Cho, Marcia C. Willing, Linda Manwaring, Rachel Schot, Caroline Nava, Alexandra Afenjar, Davor Lessel, Matias Wagner, Thomas Klopstock, Juliane Winkelmann, Claudia B. Catarino, Kyle Retterer, Jane L. Schuette, Jeffrey W. Innis, Amy Pizzino, Sabine Lüttgen, Jonas Denecke, Tim M. Strom, Kristin G. Monaghan, Zuo-Fei Yuan, Holly Dubbs, Renee Bend, Jennifer A. Lee, Michael J. Lyons, Julia Hoefele, Roman Günthner, Heiko Reutter, Boris Keren, Kelly Radtke, Omar Sherbini, Cameron Mrokse, Katherine L. Helbig, Sylvie Odent, Benjamin Cogne, Sandra Mercier, Stephane Bezieau, Thomas Besnard, Sebastien Kury, Richard Redon, Karit Reinson, Monica H. Wojcik, Katrin Õunap, Pilvi Ilves, A. Micheil Innes, Kristin D. Kernohan, Gregory Costain, M. Stephen Meyn, David Chitayat, Elaine Zackai, Anna Lehman, Hilary Kitson, Martin G. Martin, Julian A. Martinez-Agosto, Stan F. Nelson, Christina G. S. Palmer, Jeanette C. Papp, Neil H. Parker, Janet S. Sinsheimer, Eric Vilain, Jijun Wan, Amanda J. Yoon, Allison Zheng, Elise Brimble, Giovanni Battista Ferrero, Francesca Clementina Radio, Diana Carli, Sabina Barresi, Alfredo Brusco, Marco Tartaglia, Jennifer Muncy Thomas, Luis Umana, Marjan M. Weiss, Garrett Gotway, K. E. Stuurman, Michelle L. Thompson, Kirsty McWalter, Constance T. R. M. Stumpel, Servi J. C. Stevens, Alexander P. A. Stegmann, Kristian Tveten, Arve Vøllo, Trine Prescott, Christina Fagerberg, Lone Walentin Laulund, Martin J. Larsen, Melissa Byler, Robert Roger Lebel, Anna C. Hurst, Joy Dean, Samantha A. Schrier Vergano, Jennifer Norman, Saadet Mercimek-Andrews, Juanita Neira, Margot I. Van Allen, Nicola Longo, Elizabeth Sellars, Raymond J. Louie, Sara S. Cathey, Elly Brokamp, Delphine Heron, Molly Snyder, Adeline Vanderver, Celeste Simon, Xavier de la Cruz, Natália Padilla, J. Gage Crump, Wendy Chung, Benjamin Garcia, Hakon H. Hakonarson, and Elizabeth J. Bhoj. Histone h3.3 beyond cancer: germline mutations in <i>histone 3 family 3a and 3b</i> cause a previously unidentified neurodegenerative disorder in 46 patients. Science Advances, Dec 2020. URL: https://doi.org/10.1126/sciadv.abc9207, doi:10.1126/sciadv.abc9207. This article has 92 citations and is from a highest quality peer-reviewed journal.

6. (layocarris2024expandedphenotypicspectrum pages 2-3): Dana E. Layo-Carris, Emily E. Lubin, Annabel K. Sangree, Kelly J. Clark, Emily L. Durham, Elizabeth M. Gonzalez, Sarina Smith, Rajesh Angireddy, Xiao Min Wang, Erin Weiss, Annick Toutain, Roberto Mendoza-Londono, Lucie Dupuis, Nadirah Damseh, Danita Velasco, Irene Valenzuela, Marta Codina-Solà, Catherine Ziats, Jaclyn Have, Katie Clarkson, Dora Steel, Manju Kurian, Katy Barwick, Diana Carrasco, Aditi I. Dagli, M. J. M. Nowaczyk, Miroslava Hančárová, Šárka Bendová, Darina Prchalova, Zdeněk Sedláček, Alica Baxová, Catherine Bearce Nowak, Jessica Douglas, Wendy K. Chung, Nicola Longo, Konrad Platzer, Chiara Klöckner, Luisa Averdunk, Dagmar Wieczorek, Ilona Krey, Christiane Zweier, Andre Reis, Tugce Balci, Marleen Simon, Hester Y. Kroes, Antje Wiesener, Georgia Vasileiou, Nikolaos M. Marinakis, Danai Veltra, Christalena Sofocleous, Konstantina Kosma, Joanne Traeger Synodinos, Konstantinos A. Voudris, Marie-Laure Vuillaume, Paul Gueguen, Nicolas Derive, Estelle Colin, Clarisse Battault, Billie Au, Martin Delatycki, Mathew Wallis, Lyndon Gallacher, Fatma Majdoub, Noor Smal, Sarah Weckhuysen, An-Sofie Schoonjans, R. Frank Kooy, Marije Meuwissen, Benjamin T. Cocanougher, Kathryn Taylor, Carolyn E. Pizoli, Marie T. McDonald, Philip James, Elizabeth R. Roeder, Rebecca Littlejohn, Nicholas A. Borja, Willa Thorson, Kristine King, Radka Stoeva, Manon Suerink, Esther Nibbeling, Stephanie Baskin, Gwenaël L. E. Guyader, Julie Kaplan, Candace Muss, Deanna Alexis Carere, Elizabeth J. K. Bhoj, and Laura M. Bryant. Expanded phenotypic spectrum of neurodevelopmental and neurodegenerative disorder bryant-li-bhoj syndrome with 38 additional individuals. European Journal of Human Genetics, 32:928-937, Apr 2024. URL: https://doi.org/10.1038/s41431-024-01610-1, doi:10.1038/s41431-024-01610-1. This article has 12 citations and is from a domain leading peer-reviewed journal.

7. (hojo2024neonatalmyoclonusin pages 2-3): Moemi Hojo, Noriko Soma, Kei Yamada, Yu Kobayashi, Masaki Miura, Hitomi Fujii, Hiromi Nyuzuki, Yosuke Nishio, Taichi Oso, Tomoo Ogi, Takeshi Ikeuchi, and Jun Tohyama. Neonatal myoclonus in bryant-li-bhoj syndrome associated with a novel h3f3a variant. Human Genome Variation, Dec 2024. URL: https://doi.org/10.1038/s41439-024-00303-x, doi:10.1038/s41439-024-00303-x. This article has 4 citations.

8. (layocarris2024expandedphenotypicspectrum pages 4-6): Dana E. Layo-Carris, Emily E. Lubin, Annabel K. Sangree, Kelly J. Clark, Emily L. Durham, Elizabeth M. Gonzalez, Sarina Smith, Rajesh Angireddy, Xiao Min Wang, Erin Weiss, Annick Toutain, Roberto Mendoza-Londono, Lucie Dupuis, Nadirah Damseh, Danita Velasco, Irene Valenzuela, Marta Codina-Solà, Catherine Ziats, Jaclyn Have, Katie Clarkson, Dora Steel, Manju Kurian, Katy Barwick, Diana Carrasco, Aditi I. Dagli, M. J. M. Nowaczyk, Miroslava Hančárová, Šárka Bendová, Darina Prchalova, Zdeněk Sedláček, Alica Baxová, Catherine Bearce Nowak, Jessica Douglas, Wendy K. Chung, Nicola Longo, Konrad Platzer, Chiara Klöckner, Luisa Averdunk, Dagmar Wieczorek, Ilona Krey, Christiane Zweier, Andre Reis, Tugce Balci, Marleen Simon, Hester Y. Kroes, Antje Wiesener, Georgia Vasileiou, Nikolaos M. Marinakis, Danai Veltra, Christalena Sofocleous, Konstantina Kosma, Joanne Traeger Synodinos, Konstantinos A. Voudris, Marie-Laure Vuillaume, Paul Gueguen, Nicolas Derive, Estelle Colin, Clarisse Battault, Billie Au, Martin Delatycki, Mathew Wallis, Lyndon Gallacher, Fatma Majdoub, Noor Smal, Sarah Weckhuysen, An-Sofie Schoonjans, R. Frank Kooy, Marije Meuwissen, Benjamin T. Cocanougher, Kathryn Taylor, Carolyn E. Pizoli, Marie T. McDonald, Philip James, Elizabeth R. Roeder, Rebecca Littlejohn, Nicholas A. Borja, Willa Thorson, Kristine King, Radka Stoeva, Manon Suerink, Esther Nibbeling, Stephanie Baskin, Gwenaël L. E. Guyader, Julie Kaplan, Candace Muss, Deanna Alexis Carere, Elizabeth J. K. Bhoj, and Laura M. Bryant. Expanded phenotypic spectrum of neurodevelopmental and neurodegenerative disorder bryant-li-bhoj syndrome with 38 additional individuals. European Journal of Human Genetics, 32:928-937, Apr 2024. URL: https://doi.org/10.1038/s41431-024-01610-1, doi:10.1038/s41431-024-01610-1. This article has 12 citations and is from a domain leading peer-reviewed journal.

9. (wei2024bryantlibhojneurodevelopmentalsyndrome pages 1-4): Ying Wei, Kun Dai, Jinzhi Gao, Ling Chen, and Zhihui Rong. Bryant-li-bhoj neurodevelopmental syndrome: a case report in china and literature review. Unknown journal, May 2024. URL: https://doi.org/10.21203/rs.3.rs-4393513/v1, doi:10.21203/rs.3.rs-4393513/v1.

10. (khazaei2023singlesubstitutionin pages 1-3): Sima Khazaei, Carol C.L. Chen, Augusto Faria Andrade, Nisha Kabir, Pariya Azarafshar, Shahir M. Morcos, Josiane Alves França, Mariana Lopes, Peder J. Lund, Geoffroy Danieau, Samantha Worme, Lata Adnani, Nadine Nzirorera, Xiao Chen, Gayathri Yogarajah, Caterina Russo, Michele Zeinieh, Cassandra J. Wong, Laura Bryant, Steven Hébert, Bethany Tong, Tianna S. Sihota, Damien Faury, Evan Puligandla, Wajih Jawhar, Veronica Sandy, Mitra Cowan, Emily M. Nakada, Loydie A. Jerome-Majewska, Benjamin Ellezam, Carolina Cavalieri Gomes, Jonas Denecke, Davor Lessel, Marie T. McDonald, Carolyn E. Pizoli, Kathryn Taylor, Benjamin T. Cocanougher, Elizabeth J. Bhoj, Anne-Claude Gingras, Benjamin A. Garcia, Chao Lu, Eric I. Campos, Claudia L. Kleinman, Livia Garzia, and Nada Jabado. Single substitution in h3.3g34 alters dnmt3a recruitment to cause progressive neurodegeneration. Cell, 186:1162-1178.e20, Mar 2023. URL: https://doi.org/10.1016/j.cell.2023.02.023, doi:10.1016/j.cell.2023.02.023. This article has 76 citations and is from a highest quality peer-reviewed journal.

11. (bryant2020histoneh3.3beyond pages 7-8): Laura Bryant, Dong Li, Samuel G. Cox, Dylan Marchione, Evan F. Joiner, Khadija Wilson, Kevin Janssen, Pearl Lee, Michael E. March, Divya Nair, Elliott Sherr, Brieana Fregeau, Klaas J. Wierenga, Alexandrea Wadley, Grazia M. S. Mancini, Nina Powell-Hamilton, Jiddeke van de Kamp, Theresa Grebe, John Dean, Alison Ross, Heather P. Crawford, Zoe Powis, Megan T. Cho, Marcia C. Willing, Linda Manwaring, Rachel Schot, Caroline Nava, Alexandra Afenjar, Davor Lessel, Matias Wagner, Thomas Klopstock, Juliane Winkelmann, Claudia B. Catarino, Kyle Retterer, Jane L. Schuette, Jeffrey W. Innis, Amy Pizzino, Sabine Lüttgen, Jonas Denecke, Tim M. Strom, Kristin G. Monaghan, Zuo-Fei Yuan, Holly Dubbs, Renee Bend, Jennifer A. Lee, Michael J. Lyons, Julia Hoefele, Roman Günthner, Heiko Reutter, Boris Keren, Kelly Radtke, Omar Sherbini, Cameron Mrokse, Katherine L. Helbig, Sylvie Odent, Benjamin Cogne, Sandra Mercier, Stephane Bezieau, Thomas Besnard, Sebastien Kury, Richard Redon, Karit Reinson, Monica H. Wojcik, Katrin Õunap, Pilvi Ilves, A. Micheil Innes, Kristin D. Kernohan, Gregory Costain, M. Stephen Meyn, David Chitayat, Elaine Zackai, Anna Lehman, Hilary Kitson, Martin G. Martin, Julian A. Martinez-Agosto, Stan F. Nelson, Christina G. S. Palmer, Jeanette C. Papp, Neil H. Parker, Janet S. Sinsheimer, Eric Vilain, Jijun Wan, Amanda J. Yoon, Allison Zheng, Elise Brimble, Giovanni Battista Ferrero, Francesca Clementina Radio, Diana Carli, Sabina Barresi, Alfredo Brusco, Marco Tartaglia, Jennifer Muncy Thomas, Luis Umana, Marjan M. Weiss, Garrett Gotway, K. E. Stuurman, Michelle L. Thompson, Kirsty McWalter, Constance T. R. M. Stumpel, Servi J. C. Stevens, Alexander P. A. Stegmann, Kristian Tveten, Arve Vøllo, Trine Prescott, Christina Fagerberg, Lone Walentin Laulund, Martin J. Larsen, Melissa Byler, Robert Roger Lebel, Anna C. Hurst, Joy Dean, Samantha A. Schrier Vergano, Jennifer Norman, Saadet Mercimek-Andrews, Juanita Neira, Margot I. Van Allen, Nicola Longo, Elizabeth Sellars, Raymond J. Louie, Sara S. Cathey, Elly Brokamp, Delphine Heron, Molly Snyder, Adeline Vanderver, Celeste Simon, Xavier de la Cruz, Natália Padilla, J. Gage Crump, Wendy Chung, Benjamin Garcia, Hakon H. Hakonarson, and Elizabeth J. Bhoj. Histone h3.3 beyond cancer: germline mutations in <i>histone 3 family 3a and 3b</i> cause a previously unidentified neurodegenerative disorder in 46 patients. Science Advances, Dec 2020. URL: https://doi.org/10.1126/sciadv.abc9207, doi:10.1126/sciadv.abc9207. This article has 92 citations and is from a highest quality peer-reviewed journal.

12. (wilson2022reprogrammingofthe pages 27-29): Khadija D. Wilson, Elizabeth G. Porter, and Benjamin A. Garcia. Reprogramming of the epigenome in neurodevelopmental disorders. Critical Reviews in Biochemistry and Molecular Biology, 57:73-112, Oct 2022. URL: https://doi.org/10.1080/10409238.2021.1979457, doi:10.1080/10409238.2021.1979457. This article has 31 citations and is from a peer-reviewed journal.

13. (wei2024bryantlibhojneurodevelopmentalsyndrome pages 4-6): Ying Wei, Kun Dai, Jinzhi Gao, Ling Chen, and Zhihui Rong. Bryant-li-bhoj neurodevelopmental syndrome: a case report in china and literature review. Unknown journal, May 2024. URL: https://doi.org/10.21203/rs.3.rs-4393513/v1, doi:10.21203/rs.3.rs-4393513/v1.

14. (wei2024bryantlibhojneurodevelopmentalsyndrome pages 6-9): Ying Wei, Kun Dai, Jinzhi Gao, Ling Chen, and Zhihui Rong. Bryant-li-bhoj neurodevelopmental syndrome: a case report in china and literature review. Unknown journal, May 2024. URL: https://doi.org/10.21203/rs.3.rs-4393513/v1, doi:10.21203/rs.3.rs-4393513/v1.

15. (hojo2024neonatalmyoclonusin pages 3-4): Moemi Hojo, Noriko Soma, Kei Yamada, Yu Kobayashi, Masaki Miura, Hitomi Fujii, Hiromi Nyuzuki, Yosuke Nishio, Taichi Oso, Tomoo Ogi, Takeshi Ikeuchi, and Jun Tohyama. Neonatal myoclonus in bryant-li-bhoj syndrome associated with a novel h3f3a variant. Human Genome Variation, Dec 2024. URL: https://doi.org/10.1038/s41439-024-00303-x, doi:10.1038/s41439-024-00303-x. This article has 4 citations.

16. (morcos2025h3.3denovo pages 1-4): Shahir M. Morcos, Sabina Sarvan, Alejandro Saettone, Cassandra J. Wong, Samuel Chau Duy Tam Vo, Ayala Milo, Omar H. Bayoumy, Rajesh Angireddy, Giovanni L. Burke, Jack F. Greenblatt, Nada Jabado, Carol C.L. Chen, Elizabeth J. Bhoj, Anne-Claude Gingras, Jean-François Couture, and Eric I. Campos. H3.3 de novo mutations alter lysine 36 methylation via distinct mechanisms. BioRxiv, Sep 2025. URL: https://doi.org/10.1101/2025.09.09.674984, doi:10.1101/2025.09.09.674984. This article has 1 citations.

## Artifacts

- [Edison artifact artifact-00](Bryant-Li-Bhoj_Neurodevelopmental_Syndrome_1-deep-research-falcon_artifacts/artifact-00.md)