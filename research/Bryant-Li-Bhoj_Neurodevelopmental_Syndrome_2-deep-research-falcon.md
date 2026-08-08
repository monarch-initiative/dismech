---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T17:13:50.202452'
end_time: '2026-08-01T17:21:37.790227'
duration_seconds: 467.59
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Bryant-Li-Bhoj Neurodevelopmental Syndrome 2
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 12
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Bryant-Li-Bhoj_Neurodevelopmental_Syndrome_2-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Bryant-Li-Bhoj Neurodevelopmental Syndrome 2
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Bryant-Li-Bhoj Neurodevelopmental Syndrome 2** covering all of the
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

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
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
- Treatment annotations (NCIT terms)
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
- **Disease Name:** Bryant-Li-Bhoj Neurodevelopmental Syndrome 2
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Bryant-Li-Bhoj Neurodevelopmental Syndrome 2** covering all of the
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

For each treatment, suggest NCIT (NCI Thesaurus) clinical-intervention terms where applicable.

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
- Ontology term suggestions (HPO, GO, CL, UBERON, CHEBI, NCIT, MONDO) where applicable
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
- Treatment annotations (NCIT terms)
- Evidence items with PMIDs and exact abstract quotes
- Epidemiology, prognosis, diagnostic, and prevention information
- Animal model descriptions with phenotype recapitulation details


# Bryant-Li-Bhoj Neurodevelopmental Syndrome 2: Disease-Characteristics Report

## Executive summary

Bryant-Li-Bhoj neurodevelopmental syndrome 2 (BLBNS2) is an ultra-rare Mendelian chromatin disorder caused by heterozygous germline variants in **H3F3B** (current symbol **H3-3B**), one of two genes encoding the replication-independent histone H3.3 protein. It is the H3-3B-associated subtype of Bryant-Li-Bhoj syndrome (BLBS); the corresponding H3-3A-associated disorder is type 1. The best-supported phenotype comprises developmental delay/intellectual disability, motor and speech delay, tone abnormalities, dysmorphic craniofacial features, abnormal growth, visual impairment, and variably abnormal brain MRI. Some patients develop regression, progressive ataxia, white-matter disease, or cerebral atrophy, but progression is neither universal nor adequately quantified for type 2 alone. Most cases arise from de novo dominant variants, although inherited H3-3B disease has now been documented. No disease-modifying therapy, validated biomarker, formal diagnostic criteria, prevalence estimate, or BLBNS2-specific clinical trial is available.

A central evidence limitation is that most clinical publications pool H3-3A and H3-3B cases. This report therefore labels findings as **H3-3B-specific** or **combined BLBS** and does not treat pooled percentages as type-2-specific rates.

| domain | best-supported finding | evidence scope (H3F3B-specific versus combined BLBS) | ontology/identifier suggestion | evidence limitation |
|---|---|---|---|---|
| Disease identity | Bryant-Li-Bhoj neurodevelopmental syndrome 2 is the H3F3B-associated subtype of Bryant-Li-Bhoj syndrome; OMIM-classified in 2022 and mapped in Open Targets to MONDO:0030607 (layocarris2024expandedphenotypicspectrum pages 3-4, OpenTargets Search: Bryant-Li-Bhoj neurodevelopmental syndrome 2-H3F3B) | H3F3B-specific disease label supported by database mapping; phenotype literature often combines H3F3A and H3F3B | MONDO:0030607; OMIM: 619721; gene: H3F3B / H3-3B | Many publications discuss combined BLBS rather than isolated type 2 |
| Synonyms/nomenclature | Names in current use include Bryant-Li-Bhoj syndrome (BLBS) for the combined disorder and Bryant-Li-Bhoj neurodevelopmental syndrome 2 for the H3F3B form (layocarris2024expandedphenotypicspectrum pages 3-4, OpenTargets Search: Bryant-Li-Bhoj neurodevelopmental syndrome 2-H3F3B) | Mixed | Bryant-Li-Bhoj neurodevelopmental syndrome 2; BLBS | No stable broad synonym set beyond OMIM/database naming located in the retrieved evidence |
| Causal gene | Causal gene is H3F3B (also written H3-3B), encoding histone H3.3 histone B (layocarris2024expandedphenotypicspectrum pages 3-4, OpenTargets Search: Bryant-Li-Bhoj neurodevelopmental syndrome 2-H3F3B, okur2021denovovariants pages 2-3) | H3F3B-specific | H3F3B; H3-3B | Some papers use H3-3B and H3F3B interchangeably |
| Inheritance | Most reported cases are heterozygous germline de novo variants; inheritance pattern is best described as autosomal dominant, with newer evidence showing that not all cases are strictly de novo because maternally inherited p.N108S has been reported in the expanded cohort (layocarris2024expandedphenotypicspectrum pages 3-4, bryant2020histoneh3.3beyond pages 3-4, layocarris2024expandedphenotypicspectrum pages 8-9) | H3F3B-specific and combined | Autosomal dominant; de novo germline | Penetrance and recurrence risk are not well quantified; inherited cases appear rare |
| Variant spectrum | H3F3B cases include missense and stop-loss/stop-altering variants; Bryant 2020 reported 13 H3F3B patients with 12 unique H3F3B variants, and Okur 2021 added 6 H3F3B individuals including a stop-loss variant (bryant2020histoneh3.3beyond pages 3-4, okur2021denovovariants pages 2-3) | H3F3B-specific | Missense variant; stop-loss variant; heterozygous germline variant | Full variant catalog and ClinVar classifications were not extracted here |
| Population frequency | Variants were absent from 138,632 gnomAD controls in the foundational cohort, supporting rarity (bryant2020histoneh3.3beyond pages 3-4) | Combined BLBS with included H3F3B variants | Ultra-rare Mendelian disorder | No prevalence or incidence estimates available |
| Core neurodevelopmental phenotype | Developmental delay/intellectual disability is a leading feature; in Okur 2021 all detailed individuals had global developmental delay with motor and speech delay (okur2021denovovariants pages 2-3), and 2024 authors identify developmental delay/intellectual disability as one of the four most common BLBS features (layocarris2024expandedphenotypicspectrum pages 8-9) | Combined BLBS; includes H3F3B individuals | HPO term suggestion: developmental delay; intellectual disability; motor delay; speech delay | Exact H3F3B-only frequencies not available in retrieved excerpts |
| Tone/motor phenotype | Hypotonia and broader tonal abnormalities are common; gait difficulty/ataxia and progressive gait ataxia have been described (okur2021denovovariants pages 2-3, layocarris2024expandedphenotypicspectrum pages 8-9) | Combined BLBS with H3F3B representation | HPO term suggestion: hypotonia; hypertonia; gait ataxia; gait disturbance | Progression appears variable and is not quantified specifically for type 2 |
| Craniofacial phenotype | Craniofacial anomalies are a major syndrome component; in the expanded cohort, craniofacial anomalies were reported in 86% of individuals with H3-3B variants versus 95% with H3-3A variants (layocarris2024expandedphenotypicspectrum pages 3-4) | H3F3B-specific comparison available | HPO term suggestion: abnormal facial shape; dysmorphic facies; midface hypoplasia | Specific facial feature frequencies for type 2 were not fully extracted |
| Growth phenotype | Short stature/failure to thrive/abnormal growth are common; Okur 2021 found short stature with failure to thrive in 80%, while the expanded cohort noted 31% undergrowth/overgrowth trajectories for H3-3B variants (okur2021denovovariants pages 2-3, layocarris2024expandedphenotypicspectrum pages 3-4) | Mixed, partly H3F3B-specific | HPO term suggestion: short stature; failure to thrive; abnormality of head size | Growth direction and severity vary by cohort and variant |
| Brain and imaging phenotype | Structural brain abnormalities are common, including diminished white matter, hypomyelination, cortical dysplasia, leukoencephalopathy, cortical atrophy, and other MRI anomalies (bryant2020histoneh3.3beyond pages 3-4, okur2021denovovariants pages 2-3, layocarris2024expandedphenotypicspectrum pages 8-9) | Combined BLBS with H3F3B representation | HPO term suggestion: abnormal brain MRI; white matter abnormality; hypomyelination; cortical dysplasia; cerebral atrophy | H3F3B-only imaging frequencies were not provided in the retrieved excerpts |
| Vision/hearing/other systems | Visual impairment and ophthalmologic problems are repeatedly reported; hearing, cardiac, endocrine, and GU anomalies are less consistently supported in later aggregate phenotyping (lubin2025couplingdeepphenotypic pages 9-11, okur2021denovovariants pages 2-3) | Combined BLBS | HPO term suggestion: visual impairment; hearing impairment; congenital hypothyroidism | Some features may reflect ascertainment or incomplete response rates rather than robust syndrome associations |
| Natural history | Disease course spans neurodevelopmental impairment with possible neurodegenerative progression in a subset; Bryant 2020 reported neurologic degeneration in 21% overall and 3 deaths in a 46-person mixed cohort, while Layo-Carris 2024 emphasizes phenotypic heterogeneity and uncertainty about progression (bryant2020histoneh3.3beyond pages 3-4, layocarris2024expandedphenotypicspectrum pages 8-9) | Combined BLBS | Neurodevelopmental disorder; neurodegenerative course in subset | Type-2-specific mortality, survival, and longitudinal staging remain undefined |
| Mechanism: chromatin/protein | Germline H3.3 mutations disrupt DNA, histone, and chaperone interactions; modeling mapped many variants to nucleosome interfaces or regulator-binding regions, supporting altered chromatin function distinct from oncogenic somatic histone mutations (bryant2020histoneh3.3beyond pages 3-4, bryant2020histoneh3.3beyond pages 7-8) | Combined BLBS with H3F3B mutant lines included | GO term suggestion: chromatin organization; nucleosome assembly; protein-DNA complex assembly | Most mechanistic work is across mixed H3F3A/H3F3B variants rather than isolated H3F3B/type 2 |
| Mechanism: epigenetic/transcriptional | Patient PTM analysis showed aberrant local mutant-histone PTM patterns, RNA-seq showed upregulated mitosis/cell-division programs, and fibroblasts showed increased proliferation with altered S/G2 phases (bryant2020histoneh3.3beyond pages 7-8) | Combined BLBS with H3F3B patient fibroblasts included | GO term suggestion: regulation of cell cycle; mitotic cell cycle; histone modification; transcriptional regulation by chromatin | Direct causal links from these molecular findings to each clinical phenotype remain incomplete |
| Cell/tissue involvement | Evidence points especially to nervous system development, neural crest-derived tissues, and glial biology; zebrafish studies showed craniofacial anomalies and Foxd3-derived glial defects (bryant2020histoneh3.3beyond pages 7-8) | Model-organism evidence for mixed H3.3 biology relevant to BLBS | CL term suggestion: glial cell; neural crest cell; UBERON term suggestion: brain; craniofacial skeleton | No dedicated H3F3B-only animal model was identified in retrieved evidence |
| Diagnostic approach | Diagnosis is currently gene-first: exome/genome sequencing or neurodevelopmental disorder panels detecting heterozygous H3F3B variants, interpreted with phenotype correlation and often brain MRI (okur2021denovovariants pages 2-3, layocarris2024expandedphenotypicspectrum pages 8-9) | H3F3B-specific gene, general rare-disease workflow | Molecular genetic testing; H3F3B sequencing; exome sequencing; genome sequencing | No formal consensus diagnostic criteria or biomarker assays were identified |
| Differential diagnosis | Authors note phenotypic overlap with leukodystrophy and other neurodevelopmental disorders with structural brain abnormalities, making genomic testing important for distinction (layocarris2024expandedphenotypicspectrum pages 8-9, okur2021denovovariants pages 2-3) | Combined BLBS | Differential term suggestion: leukodystrophy; syndromic neurodevelopmental disorder | Differential diagnosis list is not standardized in the retrieved sources |
| Management | No disease-modifying therapy identified; management is supportive and multidisciplinary, focused on developmental therapies, neurology follow-up, feeding/growth support, ophthalmology, and surveillance guided by symptoms and imaging (layocarris2024expandedphenotypicspectrum pages 8-9, okur2021denovovariants pages 2-3) | Combined BLBS applied to type 2 | NCIT/clinical intervention term suggestion: supportive care; physical therapy; occupational therapy; speech therapy; genetic counseling | Published treatment-outcome data are extremely sparse |
| Prevention/counseling | Primary prevention is not established; useful measures are genetic counseling, trio testing to confirm de novo status, recurrence-risk discussion, and consideration of prenatal/preimplantation testing once a familial variant is known (layocarris2024expandedphenotypicspectrum pages 3-4, layocarris2024expandedphenotypicspectrum pages 8-9) | H3F3B-relevant Mendelian counseling principles | Genetic counseling; prenatal diagnosis; preimplantation genetic testing | Empiric recurrence risk and mosaicism data are not well defined |
| Epidemiology | Ultra-rare disorder with no population incidence/prevalence estimate located; evidence comes from aggregated case series and matchmaker-style ascertainment rather than registries (bryant2020histoneh3.3beyond pages 3-4, okur2021denovovariants pages 2-3, layocarris2024expandedphenotypicspectrum pages 8-9) | Combined BLBS | Rare disease; case-series evidence | Strong ascertainment bias; no denominator-based epidemiology |
| Prognosis | Prognosis is variable and incompletely defined, ranging from severe developmental disability to later-onset progressive neurologic manifestations; survival data are inadequate for type 2 specifically (bryant2020histoneh3.3beyond pages 3-4, layocarris2024expandedphenotypicspectrum pages 8-9) | Combined BLBS | Variable expressivity | No validated prognostic biomarkers or genotype-specific outcome models |
| Model systems | Functional evidence includes patient fibroblasts and zebrafish; fibroblasts showed cell-cycle/proliferation abnormalities, and zebrafish showed craniofacial and glial phenotypes (bryant2020histoneh3.3beyond pages 7-8) | Combined BLBS/mechanistic | Patient-derived fibroblast model; zebrafish model | No dedicated mammalian H3F3B BLBNS2 model identified in retrieved evidence |


*Table: This table summarizes the best-supported current knowledge for Bryant-Li-Bhoj neurodevelopmental syndrome 2, emphasizing what is specific to H3F3B versus what is only available from combined BLBS cohorts. It is useful as a compact knowledge-base scaffold and highlights key evidence gaps.*

## 1. Disease information

### Definition and identifiers

BLBNS2 is a congenital/pediatric-onset neurodevelopmental disorder—a Mendelian “histonopathy”—caused by germline variation in **H3-3B/H3F3B**, which encodes histone H3.3. Open Targets maps the disease to **MONDO:0030607**, **OMIM 619721**, and Ensembl target **ENSG00000132475**. The disease became OMIM-classified in 2022. The broader BLBS designation covers both OMIM 619720 and 619721. (layocarris2024expandedphenotypicspectrum pages 3-4, OpenTargets Search: Bryant-Li-Bhoj neurodevelopmental syndrome 2-H3F3B)

**Preferred name:** Bryant-Li-Bhoj neurodevelopmental syndrome 2.  
**Synonyms/related labels:** BLBNS2; H3F3B-related Bryant-Li-Bhoj syndrome; H3-3B-related neurodevelopmental disorder; histone H3.3-related chromatinopathy, H3-3B subtype. “Bryant-Li-Bhoj syndrome” or “BLBS” is broader and should not be used as an exact synonym when gene-specific precision is required.

No dedicated ICD-10, ICD-11, or MeSH code was identified. In clinical coding, nonspecific codes for intellectual disability, developmental disorder, hypotonia, ataxia, or congenital malformations may therefore be used, but these are not disease identifiers.

### Evidence provenance

Knowledge derives primarily from aggregated, investigator-assembled cohorts identified through clinical exome sequencing, Matchmaker Exchange/GeneMatcher-like networks, and literature review—not from population registries or routine EHR-derived epidemiology. The foundational 2020 study included 46 individuals with H3-3A/H3-3B disease, including **13 H3-3B patients carrying 12 unique H3-3B variants**. A 2021 cohort added six H3-3B individuals, while the 2024 expanded BLBS analysis reached 96 combined cases. (bryant2020histoneh3.3beyond pages 3-4, okur2021denovovariants pages 2-3, layocarris2024expandedphenotypicspectrum pages 8-9)

## 2. Etiology, risk, protection, and gene–environment relationships

### Causal factor

The primary cause is a **heterozygous germline H3-3B variant** that alters histone H3.3 sequence, abundance, nucleosome interactions, chaperone binding, or post-translational regulation. Most established variants are missense; stop-loss and transcript-dependent stop-gain consequences have also been reported. The original variants were absent from 138,632 gnomAD controls, consistent with strong rarity and pathogenic constraint. (layocarris2024expandedphenotypicspectrum pages 3-4, bryant2020histoneh3.3beyond pages 3-4)

The original paper’s abstract states: **“Germ line mutations in H3F3A and H3F3B cause a previously unidentified neurodevelopmental syndrome.”** It further describes **“46 patients bearing de novo germline mutations … with progressive neurologic dysfunction and congenital anomalies without malignancies.”** This is human cohort evidence, not merely computational inference. Bryant et al., *Science Advances*, 4 December 2020, PMID **33268356**, DOI/URL: https://doi.org/10.1126/sciadv.abc9207. (bryant2020histoneh3.3beyond pages 3-4, bryant2020histoneh3.3beyond pages 2-3)

### Risk factors

* **Genetic:** a pathogenic/likely pathogenic H3-3B allele is the dominant risk factor. Most cases are de novo, but a maternally inherited **p.Asn108Ser (p.N108S)** allele demonstrates that transmission can occur. Variant position and whether H3-3A or H3-3B is affected appear to influence phenotype more than sex, but robust genotype–phenotype rules have not been established. (layocarris2024expandedphenotypicspectrum pages 3-4, layocarris2024expandedphenotypicspectrum pages 8-9)
* **Environmental, lifestyle, infectious, occupational, age, or sex-related risk:** none established.
* **Family history:** usually absent because most variants are de novo; a positive family history is possible in inherited disease or parental mosaicism.
* **Modifier genes:** none validated. The striking variability among people with the same allele implies additional genetic, epigenetic, developmental, or environmental modifiers, but these remain hypotheses. (layocarris2024expandedphenotypicspectrum pages 3-4)

### Protective factors and gene–environment interaction

No protective allele, diet, behavior, exposure, medication, or environmental intervention has been shown to prevent or attenuate BLBNS2. Histone H3.3 lies at the genetics–epigenetics interface, so gene–environment interactions are biologically plausible, but no reproducible interaction has been demonstrated in patients. The 2024 authors explicitly concluded that unmeasured factors likely modify expressivity and highlighted gene–environment research as a future priority. (layocarris2024expandedphenotypicspectrum pages 3-4)

## 3. Phenotypes

### Core clinical spectrum

| Phenotype | Type and usual timing/course | Best available frequency | Suggested HPO annotation |
|---|---|---:|---|
| Developmental delay/intellectual disability | Sign; infancy/early childhood; mild to severe, generally chronic | All 10 deeply phenotyped H3-3A/H3-3B patients in Okur et al. had global motor and speech delay; exact type-2 rate unavailable | Global developmental delay; Intellectual disability; Delayed motor development; Speech delay |
| Hypotonia/hypertonia | Sign; often infancy; variable and sometimes mixed over time | Hypotonia 80% in the 10-person pooled 2021 cohort; tone abnormality is one of the four leading features in the 2024 cohort | Hypotonia; Hypertonia; Abnormal muscle tone |
| Gait impairment/ataxia | Sign; childhood onward; may be progressive | Gait difficulty 70% in the pooled 2021 cohort; progressive gait ataxia reported in later BLBS cases | Gait disturbance; Gait ataxia; Progressive ataxia |
| Craniofacial dysmorphism | Physical manifestation; congenital/stable | **86% in H3-3B** versus 95% in H3-3A in the expanded cohort | Abnormal facial shape; Facial asymmetry; Midface hypoplasia; Thin upper lip vermilion |
| Abnormal growth/failure to thrive | Sign; infancy/childhood; variable under- or overgrowth | Short stature/failure to thrive 80% in pooled 2021 cases; **31% of H3-3B cases** had undergrowth/overgrowth trajectories in the expanded analysis | Failure to thrive; Short stature; Abnormal body height; Abnormal head size |
| Microcephaly | Physical sign; congenital or acquired | 26% in the original 46-person combined cohort; 60% in the 2021 ten-person cohort | Microcephaly; Acquired microcephaly |
| Brain MRI abnormality | Imaging sign; may evolve | Cortical atrophy 26% in the original combined cohort; structural abnormalities 57% among evaluable 2021 cases | Abnormal brain MRI; Cerebral atrophy; White matter abnormality; Hypomyelination; Cortical dysplasia |
| Visual impairment | Symptom/sign; pediatric | Recurrent feature; exact H3-3B rate unavailable | Visual impairment; Abnormality of the eye |
| Skeletal/extremity anomalies | Physical manifestation; usually congenital | Reported recurrently but incompletely quantified | Abnormality of the musculoskeletal system; Abnormality of the hand/foot |
| Regression/neurodegeneration | Sign/course; childhood through adulthood; subset only | Neurologic degeneration 21% in the original combined cohort | Developmental regression; Neurodegeneration |

The quantitative values above must not be interpreted as population prevalence estimates. H3-3B-specific data are available for craniofacial findings and growth trajectory, whereas most other percentages pool both genes. (layocarris2024expandedphenotypicspectrum pages 3-4, bryant2020histoneh3.3beyond pages 3-4, okur2021denovovariants pages 2-3, layocarris2024expandedphenotypicspectrum pages 8-9)

Brain abnormalities reported across BLBS include diminished white matter, hypomyelination, leukodystrophy-like change, cortical dysplasia, leukoencephalopathy, and cerebral/cortical atrophy. Repeat MRI may help distinguish static developmental anomalies from progressive white-matter or volume loss. (bryant2020histoneh3.3beyond pages 3-4, okur2021denovovariants pages 2-3, layocarris2024expandedphenotypicspectrum pages 8-9)

### Variability, function, and quality of life

Severity ranges from mild delay to profound disability with inability to attain independent ambulation. In the original combined cohort, 73% attained independent sitting; recurrent variants could nevertheless produce markedly different milestones, regression, seizures, and tone findings. Such variability argues against deterministic prognosis based only on variant identity. (bryant2020histoneh3.3beyond pages 3-4, bryant2020histoneh3.3beyond pages 2-3)

No BLBNS2-specific EQ-5D, SF-36, PROMIS, caregiver-burden, or other quality-of-life study was found. Expected effects include impaired communication, mobility, feeding, education, self-care, and independent living, but quantitative utility weights are unavailable.

Seizures, hearing abnormalities, cardiac/circulatory findings, genitourinary findings, and endocrine abnormalities occur in some reports, but a 2025 deep-phenotyping analysis did not support them as consistently associated BLBS features. They should be recorded and treated when present without being considered obligatory manifestations. (lubin2025couplingdeepphenotypic pages 9-11)

## 4. Genetic and molecular information

### Gene and variant classes

**Causal gene:** H3-3B/H3F3B, encoding histone H3.3B. The original 46-person study found 13 H3-3B cases and 12 unique H3-3B variants; a recurrent H3-3B allele was **p.Pro121Arg**. More recent examples include **p.Gly34Arg**, **p.Gly34Val**, **p.Asn108Ser**, **p.Val117Val/p.Ser147Ter** (transcript-dependent consequence), and a two-base stop-loss deletion reported as **p.*137Cext*9** or **p.Cys136*ext9**, depending on transcript/notation. (layocarris2024expandedphenotypicspectrum pages 3-4, bryant2020histoneh3.3beyond pages 3-4, okur2021denovovariants pages 2-3, layocarris2024expandedphenotypicspectrum pages 8-9)

**Variant classes:** predominantly missense, but synonymous variants with noncanonical-transcript stop consequences and stop-loss/extension variants establish a broader allelic spectrum. Most are germline and heterozygous. No evidence supports a somatic mosaic tumor mechanism as the usual cause of BLBNS2.

**Classification:** pathogenicity requires ACMG/AMP assessment integrating de novo occurrence, population absence, phenotype consistency, recurrence, structural location, and functional data. A variant should not be labeled pathogenic solely because it alters H3-3B; variant-level ClinVar assertions may differ and require current review.

**Population frequency:** established cohort variants were absent from 138,632 gnomAD controls. Exact per-variant gnomAD v4, TOPMed, and ancestry-stratified frequencies were not available in the retrieved evidence. (bryant2020histoneh3.3beyond pages 3-4)

### Functional effects

Variant consequences are heterogeneous rather than a single simple null mechanism. Structural modeling of 37 variants at 25 H3.3 residues predicted disruption of DNA contacts, histone-octamer stability, intramolecular contacts, or binding to histone chaperones and epigenetic regulators. Experimental constructs showed reduced abundance for p.Arg129His, p.Met121Ile, and p.Ile52Asn, increased abundance for p.Arg41Cys, and approximately wild-type abundance for an elongated stop-loss protein. p.Arg129His increased interaction with the chaperone DAXX in one assay. These observations support altered-function, stability, and interaction mechanisms rather than uniform haploinsufficiency. (bryant2020histoneh3.3beyond pages 3-4, okur2021denovovariants pages 2-3)

No validated modifier gene, disease-specific DNA-methylation episignature, large chromosomal rearrangement, recurrent CNV, or parent-of-origin effect is established. Conventional aneuploidy, translocation, and repeat-expansion mechanisms are not characteristic.

## 5. Environmental information

No toxin, radiation exposure, pollutant, occupation, smoking, alcohol use, diet, physical activity pattern, infection, or microbiome state has been shown to cause or trigger BLBNS2. It is not infectious or contagious. Environmental history remains clinically useful for excluding phenocopies and managing general health, but it does not presently alter molecular diagnosis.

## 6. Mechanism and pathophysiology

### Proposed causal chain

1. **Upstream trigger:** a heterozygous germline H3-3B sequence variant produces an altered H3.3 molecule.
2. **Nucleosome-level dysfunction:** the mutant histone changes DNA contacts, nucleosome stability, or interaction with chaperones such as DAXX/UBN1 and chromatin readers.
3. **Epigenetic disturbance:** post-translational modifications are altered locally **in cis** on mutant H3.3 rather than globally on all histones, distinguishing these germline alleles from canonical somatic “oncohistone” mechanisms.
4. **Transcription/cell-cycle disturbance:** patient-cell RNA sequencing shows upregulation of mitosis and cell-division programs; fibroblasts demonstrate increased proliferation and altered S/G2 distribution without a major viability defect.
5. **Developmental tissue effects:** disturbed chromatin regulation affects neural development, glial/neural-crest derivatives, craniofacial development, and potentially white-matter maintenance.
6. **Clinical outcome:** developmental delay, intellectual disability, tone and gait abnormalities, dysmorphism, growth disturbance, and—in a subset—progressive neurologic dysfunction or atrophy. (bryant2020histoneh3.3beyond pages 3-4, bryant2020histoneh3.3beyond pages 7-8)

In five patient fibroblast lines, including lines with H3-3B p.Gly34Val, p.Val117Val, and p.Ser146Ter-related variants, proliferation was increased relative to six controls, with significant S- and G2-phase changes. This is direct patient-derived in-vitro evidence but does not prove that excess proliferation is the sole neuronal disease mechanism. (bryant2020histoneh3.3beyond pages 7-8)

The foundational abstract reports: **“Patient histone posttranslational modifications analysis revealed notably aberrant local PTM patterns”** and **“RNA sequencing on patient cells demonstrated up-regulated gene expression related to mitosis and cell division.”** It concludes that germline and cancer-associated mutations are mechanistically distinct but may converge on proliferation control. (bryant2020histoneh3.3beyond pages 7-8)

### Relevant ontology suggestions

* **GO biological process:** chromatin organization; nucleosome assembly; regulation of transcription by chromatin organization; histone modification; mitotic cell cycle; regulation of cell proliferation; nervous-system development; glial-cell development; neural-crest-cell development.
* **GO cellular component:** nucleosome; chromatin; nucleus; chromosome.
* **CL cell types:** neuron; glial cell; neural crest cell; oligodendrocyte lineage cell; fibroblast for patient-cell assays.
* **Molecular profiling:** disease-relevant bulk RNA sequencing, histone PTM proteomics, interaction proteomics, and cell-cycle profiling exist. No validated patient single-cell, spatial transcriptomic, metabolomic, lipidomic, or integrated clinical multi-omic signature was identified.
* **Immune/metabolic/tissue-injury mechanisms:** no primary immunodeficiency, autoimmunity, enzyme deficiency, mitochondrial metabolic defect, fibrosis, ischemia, or inflammatory tissue-injury pathway is established.

## 7. Anatomical structures affected

**Primary system:** central nervous system, particularly brain development and white matter. Suggested terms include **UBERON:brain**, cerebral cortex, cerebral white matter, cerebellum, and central nervous system. MRI abnormalities are generally bilateral/diffuse rather than a consistently lateralized lesion. (bryant2020histoneh3.3beyond pages 3-4, okur2021denovovariants pages 2-3)

**Secondary structures:** craniofacial skeleton and soft tissues, eyes/visual system, skeletal/extremity structures, and gastrointestinal/feeding systems. Cardiac, endocrine, auditory, and genitourinary abnormalities may occur but are not firmly established as core type-2 manifestations. (lubin2025couplingdeepphenotypic pages 9-11, okur2021denovovariants pages 2-3)

**Cellular/subcellular localization:** neurons and glia are clinically implicated; neural-crest derivatives are supported by zebrafish data. The fundamental subcellular site is nuclear chromatin/nucleosomes rather than mitochondria, lysosome, or endoplasmic reticulum. Suggested GO cellular-component terms are nucleus, chromatin, chromosome, and nucleosome.

## 8. Temporal development and natural history

BLBNS2 is usually congenital or early pediatric in onset, although the molecular lesion is present from conception. Developmental delay, hypotonia, feeding/growth concerns, or dysmorphism commonly become evident in infancy or early childhood. The course is lifelong and highly variable.

The original mixed cohort, aged 2 months to 32 years, documented neurologic degeneration in 9/46 (21%), cortical atrophy in 26%, and three deaths. These figures demonstrate that progression and mortality can occur but do **not** establish H3-3B-specific survival risks. Later work emphasizes a mixed neurodevelopmental–neurodegenerative spectrum, including progressive gait ataxia, rather than universal degeneration. (bryant2020histoneh3.3beyond pages 3-4, layocarris2024expandedphenotypicspectrum pages 8-9)

There are no validated stages, median progression rate, remission pattern, or critical therapeutic window. Developmental surveillance and early habilitation are rational because infancy and early childhood are periods of high neuroplasticity, but no study has quantified a disease-specific window of reversibility.

## 9. Inheritance and population

### Inheritance

The best model is **autosomal dominant**, usually due to a **de novo** heterozygous germline allele. One maternally inherited p.Asn108Ser variant expands the spectrum beyond strictly de novo disease. (bryant2020histoneh3.3beyond pages 3-4, layocarris2024expandedphenotypicspectrum pages 8-9)

Penetrance is unknown; expressivity is clearly variable, including among individuals with the same allele. No anticipation, founder effect, consanguinity association, carrier frequency, or population-specific enrichment has been established. Parental germline or low-level somatic mosaicism has not been quantified and remains relevant to recurrence counseling.

### Epidemiology

No incidence, prevalence, sex ratio, ethnic predisposition, or geographic distribution can be estimated reliably. Published cases span multiple countries and ancestries, supporting worldwide occurrence rather than endemicity. Case discovery depends heavily on access to exome/genome sequencing. The original combined cohort contained 27 males and 19 females, but this ascertainment ratio is not evidence of sex-biased risk. (bryant2020histoneh3.3beyond pages 3-4)

## 10. Diagnostics

### Recommended approach

1. **Clinical recognition:** unexplained developmental/intellectual disability with tone abnormality, gait disorder, growth disturbance, dysmorphism, visual problems, or abnormal brain MRI.
2. **First-line molecular testing:** trio whole-exome or whole-genome sequencing is preferred for a genetically heterogeneous neurodevelopmental presentation. A comprehensive neurodevelopmental/chromatinopathy panel should include **H3-3B/H3F3B** and **H3-3A/H3F3A**.
3. **Variant confirmation:** orthogonal confirmation as appropriate, parental testing, transcript-aware HGVS annotation, population-database review, and ACMG/AMP classification.
4. **Phenotypic assessment:** developmental evaluation; neurologic examination; growth and feeding assessment; ophthalmology; hearing testing; and brain MRI. EEG is indicated for suspected seizures or episodic movements, not universally as a diagnostic biomarker.
5. **Longitudinal evaluation:** repeat neurologic, gait, vision, growth, and developmental assessment; repeat MRI when progression, regression, ataxia, or new focal findings emerge. (okur2021denovovariants pages 2-3, layocarris2024expandedphenotypicspectrum pages 8-9)

The 2021 abstract states that detailed phenotyping of H3-3A and H3-3B cases showed **“global developmental delay, short stature, failure to thrive, dysmorphic facial features, structural brain abnormalities, hypotonia, and visual impairment.”** Okur et al., *npj Genomic Medicine*, December 2021, PMID **34876591**, DOI/URL: https://doi.org/10.1038/s41525-021-00268-8. (okur2021denovovariants pages 2-3)

### Role of other tests

* **CMA:** useful when first-tier testing for developmental disability or to find an alternative CNV, but cannot reliably detect most causative H3-3B single-nucleotide variants.
* **Karyotype/FISH:** not routinely informative unless another chromosomal diagnosis is suspected.
* **Single-gene sequencing:** reasonable for a highly suggestive phenotype or familial variant, but exome/genome testing usually offers better differential coverage.
* **RNA sequencing:** potentially useful for transcript-dependent splice/stop consequences or uncertain variants, but not a validated routine assay.
* **Methylation/proteomics/metabolomics:** no clinically validated BLBNS2 signature.
* **Mitochondrial DNA and repeat-expansion tests:** not disease-specific; use only when the differential warrants them.

### Differential diagnosis

Important alternatives include H3-3A-related BLBNS1, other germline histonopathies/chromatinopathies, leukodystrophies and hypomyelinating disorders, cerebral-palsy phenocopies, mitochondrial disease, congenital disorders of glycosylation, syndromic intellectual disability with growth failure, and genetic ataxia or movement disorders. Leukodystrophy overlap is especially relevant when progressive gait ataxia or white-matter abnormalities dominate. (okur2021denovovariants pages 2-3, layocarris2024expandedphenotypicspectrum pages 8-9)

There are no standardized clinical diagnostic criteria, prenatal ultrasound signature, newborn biochemical screen, or population screening program.

## 11. Outcome and prognosis

Prognosis is variable. Developmental impairment is generally lifelong; functional outcomes range from delayed but achieved milestones to severe dependence. Regression, progressive ataxia, and cerebral atrophy occur in a subset. Three deaths were reported in the original 46-person combined cohort, but causes, age-specific mortality, and H3-3B-specific contribution are insufficient to estimate life expectancy or survival curves. (bryant2020histoneh3.3beyond pages 3-4)

No validated prognostic biomarker exists. Variant location and affected paralog may influence particular phenotypes, but neither currently supports an individual outcome calculator. Sex was less explanatory than gene and protein position in the expanded analysis, while substantial residual variability remained. (layocarris2024expandedphenotypicspectrum pages 3-4)

Potential complications include feeding/growth failure, immobility, contracture or orthopedic problems, communication impairment, falls from ataxia, visual disability, seizures in a minority, and caregiver burden. No formal recovery rate or treatment-response rate has been published.

## 12. Treatment and current applications

### Current clinical implementation

There is no FDA/EMA-approved disease-modifying or genotype-targeted treatment. Care is multidisciplinary and phenotype-directed:

* developmental pediatrics and neurology follow-up;
* early physical, occupational, speech/language, communication, and feeding therapy;
* nutritional support and swallowing assessment when indicated;
* mobility aids, orthotics, and orthopedic management for gait or skeletal problems;
* standard antiseizure medication when epilepsy is documented;
* ophthalmologic correction or low-vision support;
* audiology and endocrine/cardiac evaluation when clinically indicated;
* educational planning, augmentative communication, psychosocial support, respite care, and genetic counseling.

Suggested NCIT intervention concepts include **Supportive Care**, **Physical Therapy**, **Occupational Therapy**, **Speech Therapy**, **Nutritional Support**, **Genetic Counseling**, and **Anticonvulsant Therapy**. These are ontology suggestions, not BLBNS2-specific efficacy claims.

No BLBNS2 interventional clinical trial was identified. Trials retrieved through broad H3F3A/H3F3B searches concerned somatic H3-mutant gliomas and must not be extrapolated to germline BLBNS2. Gene replacement, CRISPR editing, allele-selective silencing, ASOs, cell therapy, immunotherapy, and chromatin-targeted drugs remain preclinical concepts without demonstrated patient benefit.

## 13. Prevention

**Primary prevention:** no lifestyle, vaccine, environmental, or pharmacologic intervention prevents a de novo germline H3-3B variant.

**Secondary prevention/early detection:** prompt genomic testing can shorten the diagnostic odyssey and initiate developmental, feeding, vision, mobility, and educational support. There is no newborn screening assay or evidence supporting population screening.

**Tertiary prevention:** monitor growth, swallowing, mobility, contractures, vision, neurologic regression, and seizures to reduce avoidable complications.

**Reproductive options:** genetic counseling; parental testing; assessment for parental mosaicism when technically feasible; prenatal diagnosis by CVS/amniocentesis; or preimplantation genetic testing once a familial pathogenic variant is established. For an affected heterozygous individual, theoretical transmission risk is 50% per pregnancy, subject to penetrance and reproductive fitness. After an apparently de novo case, recurrence risk is low but not zero because germline mosaicism cannot be excluded. No disease-specific empirical mosaicism estimate is available.

## 14. Other species and natural disease

No naturally occurring veterinary counterpart, affected breed, zoonotic reservoir, or cross-species transmission phenomenon was identified. BLBNS2 is genetic and noncommunicable. H3.3 biology is evolutionarily conserved, making animal orthologs useful experimentally, but conservation does not establish spontaneous animal disease.

Relevant experimental taxa include **Homo sapiens** (NCBI Taxon 9606), **Danio rerio** (zebrafish; Taxon 7955), and potentially **Mus musculus** (mouse; Taxon 10090). Exact ortholog NCBI Gene identifiers should be verified directly before database ingestion.

## 15. Model organisms and experimental systems

### Patient-derived cells

Patient fibroblasts are the strongest disease-proximal in-vitro model. They demonstrate variant-specific PTM changes, altered transcriptional programs, increased proliferation, and S/G2 cell-cycle changes. Their limitation is that fibroblasts do not reproduce neuronal/glial maturation, circuitry, myelination, or neurodegeneration. (bryant2020histoneh3.3beyond pages 7-8)

### Zebrafish

H3.3 perturbation in zebrafish produced craniofacial anomalies and defects in Foxd3-derived glia and other neural-crest derivatives, providing organism-level support for craniofacial and glial mechanisms. The original abstract states: **“A zebrafish model showed craniofacial anomalies and a defect in Foxd3-derived glia.”** However, this is not a fully validated H3-3B-variant-specific model of every human phenotype. (bryant2020histoneh3.3beyond pages 7-8)

### Other models and applications

Structural modeling and transfected variant constructs have been used to examine nucleosome interfaces, protein abundance, and chaperone binding. No dedicated mammalian knock-in model, patient iPSC-derived neural model, cerebral organoid, or H3-3B-specific longitudinal vertebrate model was identified in the retrieved evidence. Priority applications include testing allele-specific mechanisms, defining neuronal versus oligodendroglial vulnerability, studying myelination and regression, and evaluating allele-selective therapeutic strategies.

## Recent developments and expert interpretation

The major 2024 advance was expansion from an initially narrow “de novo missense neurodegenerative syndrome” to a **96-person, phenotypically heterogeneous neurodevelopmental–neurodegenerative spectrum** encompassing missense, synonymous/transcript-dependent, stop-loss, and inherited alleles. The authors found no conclusive simple genotype–phenotype correlation; gene and protein location appeared more informative than sex, but substantial variability remained. Layo-Carris et al., *European Journal of Human Genetics* 32:928–937, published April 2024, DOI/URL: https://doi.org/10.1038/s41431-024-01610-1. (layocarris2024expandedphenotypicspectrum pages 3-4, layocarris2024expandedphenotypicspectrum pages 8-9)

The paper’s abstract summarizes the current expert position: **“phenotypic heterogeneity was present even amongst individuals harboring the same variant”** and **“additional factors may play a role in modifying the phenotypes.”** This supports cautious individualized prognosis and continued longitudinal study rather than rigid variant-based prediction. (layocarris2024expandedphenotypicspectrum pages 3-4)

A 2025 deep-phenotyping study of 192 individuals with germline histonopathies further reinforced developmental delay/intellectual disability, motor and speech delay, MRI abnormalities, hypotonia, vision abnormalities, head-size abnormalities, and skeletal findings as central BLBS domains, while finding weaker support for seizures and several non-neurologic systems as consistent syndrome associations. It also reported an adult H3-3B p.Lys23Arg carrier with an atypical pulmonary carcinoid at age 33; this isolated observation is insufficient to establish cancer predisposition or justify routine tumor surveillance. Lubin et al., *Human Genetics and Genomics Advances* 6:100440, July 2025, https://doi.org/10.1016/j.xhgg.2025.100440. (lubin2025couplingdeepphenotypic pages 9-11)

## Principal knowledge gaps

1. H3-3B-specific phenotype denominators and longitudinal natural history.
2. Incidence, prevalence, penetrance, sex ratio, mortality, and life expectancy.
3. Systematic parental-mosaicism and reproductive-risk data.
4. Variant-level functional classification and reproducible genotype–phenotype relationships.
5. Neuron-, oligodendrocyte-, and brain-organoid models specific to H3-3B alleles.
6. Validated epigenomic, transcriptomic, imaging, or fluid biomarkers.
7. Controlled evidence for surveillance and supportive interventions.
8. Disease-modifying therapies and BLBNS2-specific clinical trials.

Accordingly, BLBNS2 should currently be represented in a knowledge base as a **de novo-dominant, variably expressive H3-3B histonopathy with developmental and possible progressive neurologic manifestations**, while marking most frequency, prognosis, and treatment fields as incomplete rather than absent.

References

1. (layocarris2024expandedphenotypicspectrum pages 3-4): Dana E. Layo-Carris, Emily E. Lubin, Annabel K. Sangree, Kelly J. Clark, Emily L. Durham, Elizabeth M. Gonzalez, Sarina Smith, Rajesh Angireddy, Xiao Min Wang, Erin Weiss, Annick Toutain, Roberto Mendoza-Londono, Lucie Dupuis, Nadirah Damseh, Danita Velasco, Irene Valenzuela, Marta Codina-Solà, Catherine Ziats, Jaclyn Have, Katie Clarkson, Dora Steel, Manju Kurian, Katy Barwick, Diana Carrasco, Aditi I. Dagli, M. J. M. Nowaczyk, Miroslava Hančárová, Šárka Bendová, Darina Prchalova, Zdeněk Sedláček, Alica Baxová, Catherine Bearce Nowak, Jessica Douglas, Wendy K. Chung, Nicola Longo, Konrad Platzer, Chiara Klöckner, Luisa Averdunk, Dagmar Wieczorek, Ilona Krey, Christiane Zweier, Andre Reis, Tugce Balci, Marleen Simon, Hester Y. Kroes, Antje Wiesener, Georgia Vasileiou, Nikolaos M. Marinakis, Danai Veltra, Christalena Sofocleous, Konstantina Kosma, Joanne Traeger Synodinos, Konstantinos A. Voudris, Marie-Laure Vuillaume, Paul Gueguen, Nicolas Derive, Estelle Colin, Clarisse Battault, Billie Au, Martin Delatycki, Mathew Wallis, Lyndon Gallacher, Fatma Majdoub, Noor Smal, Sarah Weckhuysen, An-Sofie Schoonjans, R. Frank Kooy, Marije Meuwissen, Benjamin T. Cocanougher, Kathryn Taylor, Carolyn E. Pizoli, Marie T. McDonald, Philip James, Elizabeth R. Roeder, Rebecca Littlejohn, Nicholas A. Borja, Willa Thorson, Kristine King, Radka Stoeva, Manon Suerink, Esther Nibbeling, Stephanie Baskin, Gwenaël L. E. Guyader, Julie Kaplan, Candace Muss, Deanna Alexis Carere, Elizabeth J. K. Bhoj, and Laura M. Bryant. Expanded phenotypic spectrum of neurodevelopmental and neurodegenerative disorder bryant-li-bhoj syndrome with 38 additional individuals. European Journal of Human Genetics, 32:928-937, Apr 2024. URL: https://doi.org/10.1038/s41431-024-01610-1, doi:10.1038/s41431-024-01610-1. This article has 12 citations and is from a domain leading peer-reviewed journal.

2. (OpenTargets Search: Bryant-Li-Bhoj neurodevelopmental syndrome 2-H3F3B): Open Targets Query (Bryant-Li-Bhoj neurodevelopmental syndrome 2-H3F3B, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

3. (okur2021denovovariants pages 2-3): Volkan Okur, Zefu Chen, Liesbeth Vossaert, Sandra Peacock, Jill Rosenfeld, Lina Zhao, Haowei Du, Emily Calamaro, Amanda Gerard, Sen Zhao, Jill Kelsay, Ashley Lahr, Chloe Mighton, Hillary M. Porter, Amy Siemon, Josh Silver, Shayna Svihovec, Chin-To Fong, Christina L. Grant, Jordan Lerner-Ellis, Kandamurugu Manickam, Suneeta Madan-Khetarpal, Shawn E. McCandless, Chantal F. Morel, G. Bradley Schaefer, Elizabeth M. Berry-Kravis, Ryan Gates, Natalia Gomez-Ospina, Guixing Qiu, Terry Jianguo Zhang, Zhihong Wu, Linyan Meng, Pengfei Liu, Daryl A. Scott, James R. Lupski, Christine M. Eng, Nan Wu, and Bo Yuan. De novo variants in h3-3a and h3-3b are associated with neurodevelopmental delay, dysmorphic features, and structural brain abnormalities. npj Genomic Medicine, Dec 2021. URL: https://doi.org/10.1038/s41525-021-00268-8, doi:10.1038/s41525-021-00268-8. This article has 32 citations and is from a peer-reviewed journal.

4. (bryant2020histoneh3.3beyond pages 3-4): Laura Bryant, Dong Li, Samuel G. Cox, Dylan Marchione, Evan F. Joiner, Khadija Wilson, Kevin Janssen, Pearl Lee, Michael E. March, Divya Nair, Elliott Sherr, Brieana Fregeau, Klaas J. Wierenga, Alexandrea Wadley, Grazia M. S. Mancini, Nina Powell-Hamilton, Jiddeke van de Kamp, Theresa Grebe, John Dean, Alison Ross, Heather P. Crawford, Zoe Powis, Megan T. Cho, Marcia C. Willing, Linda Manwaring, Rachel Schot, Caroline Nava, Alexandra Afenjar, Davor Lessel, Matias Wagner, Thomas Klopstock, Juliane Winkelmann, Claudia B. Catarino, Kyle Retterer, Jane L. Schuette, Jeffrey W. Innis, Amy Pizzino, Sabine Lüttgen, Jonas Denecke, Tim M. Strom, Kristin G. Monaghan, Zuo-Fei Yuan, Holly Dubbs, Renee Bend, Jennifer A. Lee, Michael J. Lyons, Julia Hoefele, Roman Günthner, Heiko Reutter, Boris Keren, Kelly Radtke, Omar Sherbini, Cameron Mrokse, Katherine L. Helbig, Sylvie Odent, Benjamin Cogne, Sandra Mercier, Stephane Bezieau, Thomas Besnard, Sebastien Kury, Richard Redon, Karit Reinson, Monica H. Wojcik, Katrin Õunap, Pilvi Ilves, A. Micheil Innes, Kristin D. Kernohan, Gregory Costain, M. Stephen Meyn, David Chitayat, Elaine Zackai, Anna Lehman, Hilary Kitson, Martin G. Martin, Julian A. Martinez-Agosto, Stan F. Nelson, Christina G. S. Palmer, Jeanette C. Papp, Neil H. Parker, Janet S. Sinsheimer, Eric Vilain, Jijun Wan, Amanda J. Yoon, Allison Zheng, Elise Brimble, Giovanni Battista Ferrero, Francesca Clementina Radio, Diana Carli, Sabina Barresi, Alfredo Brusco, Marco Tartaglia, Jennifer Muncy Thomas, Luis Umana, Marjan M. Weiss, Garrett Gotway, K. E. Stuurman, Michelle L. Thompson, Kirsty McWalter, Constance T. R. M. Stumpel, Servi J. C. Stevens, Alexander P. A. Stegmann, Kristian Tveten, Arve Vøllo, Trine Prescott, Christina Fagerberg, Lone Walentin Laulund, Martin J. Larsen, Melissa Byler, Robert Roger Lebel, Anna C. Hurst, Joy Dean, Samantha A. Schrier Vergano, Jennifer Norman, Saadet Mercimek-Andrews, Juanita Neira, Margot I. Van Allen, Nicola Longo, Elizabeth Sellars, Raymond J. Louie, Sara S. Cathey, Elly Brokamp, Delphine Heron, Molly Snyder, Adeline Vanderver, Celeste Simon, Xavier de la Cruz, Natália Padilla, J. Gage Crump, Wendy Chung, Benjamin Garcia, Hakon H. Hakonarson, and Elizabeth J. Bhoj. Histone h3.3 beyond cancer: germline mutations in <i>histone 3 family 3a and 3b</i> cause a previously unidentified neurodegenerative disorder in 46 patients. Science Advances, Dec 2020. URL: https://doi.org/10.1126/sciadv.abc9207, doi:10.1126/sciadv.abc9207. This article has 92 citations and is from a highest quality peer-reviewed journal.

5. (layocarris2024expandedphenotypicspectrum pages 8-9): Dana E. Layo-Carris, Emily E. Lubin, Annabel K. Sangree, Kelly J. Clark, Emily L. Durham, Elizabeth M. Gonzalez, Sarina Smith, Rajesh Angireddy, Xiao Min Wang, Erin Weiss, Annick Toutain, Roberto Mendoza-Londono, Lucie Dupuis, Nadirah Damseh, Danita Velasco, Irene Valenzuela, Marta Codina-Solà, Catherine Ziats, Jaclyn Have, Katie Clarkson, Dora Steel, Manju Kurian, Katy Barwick, Diana Carrasco, Aditi I. Dagli, M. J. M. Nowaczyk, Miroslava Hančárová, Šárka Bendová, Darina Prchalova, Zdeněk Sedláček, Alica Baxová, Catherine Bearce Nowak, Jessica Douglas, Wendy K. Chung, Nicola Longo, Konrad Platzer, Chiara Klöckner, Luisa Averdunk, Dagmar Wieczorek, Ilona Krey, Christiane Zweier, Andre Reis, Tugce Balci, Marleen Simon, Hester Y. Kroes, Antje Wiesener, Georgia Vasileiou, Nikolaos M. Marinakis, Danai Veltra, Christalena Sofocleous, Konstantina Kosma, Joanne Traeger Synodinos, Konstantinos A. Voudris, Marie-Laure Vuillaume, Paul Gueguen, Nicolas Derive, Estelle Colin, Clarisse Battault, Billie Au, Martin Delatycki, Mathew Wallis, Lyndon Gallacher, Fatma Majdoub, Noor Smal, Sarah Weckhuysen, An-Sofie Schoonjans, R. Frank Kooy, Marije Meuwissen, Benjamin T. Cocanougher, Kathryn Taylor, Carolyn E. Pizoli, Marie T. McDonald, Philip James, Elizabeth R. Roeder, Rebecca Littlejohn, Nicholas A. Borja, Willa Thorson, Kristine King, Radka Stoeva, Manon Suerink, Esther Nibbeling, Stephanie Baskin, Gwenaël L. E. Guyader, Julie Kaplan, Candace Muss, Deanna Alexis Carere, Elizabeth J. K. Bhoj, and Laura M. Bryant. Expanded phenotypic spectrum of neurodevelopmental and neurodegenerative disorder bryant-li-bhoj syndrome with 38 additional individuals. European Journal of Human Genetics, 32:928-937, Apr 2024. URL: https://doi.org/10.1038/s41431-024-01610-1, doi:10.1038/s41431-024-01610-1. This article has 12 citations and is from a domain leading peer-reviewed journal.

6. (lubin2025couplingdeepphenotypic pages 9-11): Emily E. Lubin, Elizabeth M. Gonzalez, Annabel K. Sangree, Emily L. Durham, Hannah Klinkhammer, Jing-Mei Li, Sarina M. Smith, Dana E. Layo-Carris, Kelly J. Clark, Ashley J. Melendez-Perez, Xiao Min Wang, Rajesh Angireddy, Erin E. Weiss, Tahsin Stefan Barakat, Sandra Mercier, Benjamin Cogné, Saskia Koene, Yvonne Hilhorst-Hofstee, Malgorzata Rydzanicz, Rafal Ploski, María de los Ángeles Gómez Cano, María Palomares-Bralo, Tania Barragán Arévalo, Tiong Yang Tan, Lyndon Gallacher, Suzanne P. MacFarland, Rebecca C. Ahrens-Nicklas, Tomoki T. Nomakuchi, and Elizabeth J.K. Bhoj. Coupling deep phenotypic quantification with next-generation phenotyping for 192 individuals with germline histonopathies. Jul 2025. URL: https://doi.org/10.1016/j.xhgg.2025.100440, doi:10.1016/j.xhgg.2025.100440. This article has 5 citations and is from a peer-reviewed journal.

7. (bryant2020histoneh3.3beyond pages 7-8): Laura Bryant, Dong Li, Samuel G. Cox, Dylan Marchione, Evan F. Joiner, Khadija Wilson, Kevin Janssen, Pearl Lee, Michael E. March, Divya Nair, Elliott Sherr, Brieana Fregeau, Klaas J. Wierenga, Alexandrea Wadley, Grazia M. S. Mancini, Nina Powell-Hamilton, Jiddeke van de Kamp, Theresa Grebe, John Dean, Alison Ross, Heather P. Crawford, Zoe Powis, Megan T. Cho, Marcia C. Willing, Linda Manwaring, Rachel Schot, Caroline Nava, Alexandra Afenjar, Davor Lessel, Matias Wagner, Thomas Klopstock, Juliane Winkelmann, Claudia B. Catarino, Kyle Retterer, Jane L. Schuette, Jeffrey W. Innis, Amy Pizzino, Sabine Lüttgen, Jonas Denecke, Tim M. Strom, Kristin G. Monaghan, Zuo-Fei Yuan, Holly Dubbs, Renee Bend, Jennifer A. Lee, Michael J. Lyons, Julia Hoefele, Roman Günthner, Heiko Reutter, Boris Keren, Kelly Radtke, Omar Sherbini, Cameron Mrokse, Katherine L. Helbig, Sylvie Odent, Benjamin Cogne, Sandra Mercier, Stephane Bezieau, Thomas Besnard, Sebastien Kury, Richard Redon, Karit Reinson, Monica H. Wojcik, Katrin Õunap, Pilvi Ilves, A. Micheil Innes, Kristin D. Kernohan, Gregory Costain, M. Stephen Meyn, David Chitayat, Elaine Zackai, Anna Lehman, Hilary Kitson, Martin G. Martin, Julian A. Martinez-Agosto, Stan F. Nelson, Christina G. S. Palmer, Jeanette C. Papp, Neil H. Parker, Janet S. Sinsheimer, Eric Vilain, Jijun Wan, Amanda J. Yoon, Allison Zheng, Elise Brimble, Giovanni Battista Ferrero, Francesca Clementina Radio, Diana Carli, Sabina Barresi, Alfredo Brusco, Marco Tartaglia, Jennifer Muncy Thomas, Luis Umana, Marjan M. Weiss, Garrett Gotway, K. E. Stuurman, Michelle L. Thompson, Kirsty McWalter, Constance T. R. M. Stumpel, Servi J. C. Stevens, Alexander P. A. Stegmann, Kristian Tveten, Arve Vøllo, Trine Prescott, Christina Fagerberg, Lone Walentin Laulund, Martin J. Larsen, Melissa Byler, Robert Roger Lebel, Anna C. Hurst, Joy Dean, Samantha A. Schrier Vergano, Jennifer Norman, Saadet Mercimek-Andrews, Juanita Neira, Margot I. Van Allen, Nicola Longo, Elizabeth Sellars, Raymond J. Louie, Sara S. Cathey, Elly Brokamp, Delphine Heron, Molly Snyder, Adeline Vanderver, Celeste Simon, Xavier de la Cruz, Natália Padilla, J. Gage Crump, Wendy Chung, Benjamin Garcia, Hakon H. Hakonarson, and Elizabeth J. Bhoj. Histone h3.3 beyond cancer: germline mutations in <i>histone 3 family 3a and 3b</i> cause a previously unidentified neurodegenerative disorder in 46 patients. Science Advances, Dec 2020. URL: https://doi.org/10.1126/sciadv.abc9207, doi:10.1126/sciadv.abc9207. This article has 92 citations and is from a highest quality peer-reviewed journal.

8. (bryant2020histoneh3.3beyond pages 2-3): Laura Bryant, Dong Li, Samuel G. Cox, Dylan Marchione, Evan F. Joiner, Khadija Wilson, Kevin Janssen, Pearl Lee, Michael E. March, Divya Nair, Elliott Sherr, Brieana Fregeau, Klaas J. Wierenga, Alexandrea Wadley, Grazia M. S. Mancini, Nina Powell-Hamilton, Jiddeke van de Kamp, Theresa Grebe, John Dean, Alison Ross, Heather P. Crawford, Zoe Powis, Megan T. Cho, Marcia C. Willing, Linda Manwaring, Rachel Schot, Caroline Nava, Alexandra Afenjar, Davor Lessel, Matias Wagner, Thomas Klopstock, Juliane Winkelmann, Claudia B. Catarino, Kyle Retterer, Jane L. Schuette, Jeffrey W. Innis, Amy Pizzino, Sabine Lüttgen, Jonas Denecke, Tim M. Strom, Kristin G. Monaghan, Zuo-Fei Yuan, Holly Dubbs, Renee Bend, Jennifer A. Lee, Michael J. Lyons, Julia Hoefele, Roman Günthner, Heiko Reutter, Boris Keren, Kelly Radtke, Omar Sherbini, Cameron Mrokse, Katherine L. Helbig, Sylvie Odent, Benjamin Cogne, Sandra Mercier, Stephane Bezieau, Thomas Besnard, Sebastien Kury, Richard Redon, Karit Reinson, Monica H. Wojcik, Katrin Õunap, Pilvi Ilves, A. Micheil Innes, Kristin D. Kernohan, Gregory Costain, M. Stephen Meyn, David Chitayat, Elaine Zackai, Anna Lehman, Hilary Kitson, Martin G. Martin, Julian A. Martinez-Agosto, Stan F. Nelson, Christina G. S. Palmer, Jeanette C. Papp, Neil H. Parker, Janet S. Sinsheimer, Eric Vilain, Jijun Wan, Amanda J. Yoon, Allison Zheng, Elise Brimble, Giovanni Battista Ferrero, Francesca Clementina Radio, Diana Carli, Sabina Barresi, Alfredo Brusco, Marco Tartaglia, Jennifer Muncy Thomas, Luis Umana, Marjan M. Weiss, Garrett Gotway, K. E. Stuurman, Michelle L. Thompson, Kirsty McWalter, Constance T. R. M. Stumpel, Servi J. C. Stevens, Alexander P. A. Stegmann, Kristian Tveten, Arve Vøllo, Trine Prescott, Christina Fagerberg, Lone Walentin Laulund, Martin J. Larsen, Melissa Byler, Robert Roger Lebel, Anna C. Hurst, Joy Dean, Samantha A. Schrier Vergano, Jennifer Norman, Saadet Mercimek-Andrews, Juanita Neira, Margot I. Van Allen, Nicola Longo, Elizabeth Sellars, Raymond J. Louie, Sara S. Cathey, Elly Brokamp, Delphine Heron, Molly Snyder, Adeline Vanderver, Celeste Simon, Xavier de la Cruz, Natália Padilla, J. Gage Crump, Wendy Chung, Benjamin Garcia, Hakon H. Hakonarson, and Elizabeth J. Bhoj. Histone h3.3 beyond cancer: germline mutations in <i>histone 3 family 3a and 3b</i> cause a previously unidentified neurodegenerative disorder in 46 patients. Science Advances, Dec 2020. URL: https://doi.org/10.1126/sciadv.abc9207, doi:10.1126/sciadv.abc9207. This article has 92 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Bryant-Li-Bhoj_Neurodevelopmental_Syndrome_2-deep-research-falcon_artifacts/artifact-00.md)