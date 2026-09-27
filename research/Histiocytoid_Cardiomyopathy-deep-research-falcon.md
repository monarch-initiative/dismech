---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-01T17:04:28.375253'
end_time: '2026-08-01T17:13:54.489920'
duration_seconds: 566.11
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Histiocytoid Cardiomyopathy
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 18
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Histiocytoid_Cardiomyopathy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Histiocytoid Cardiomyopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Histiocytoid Cardiomyopathy** covering all of the
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
- **Disease Name:** Histiocytoid Cardiomyopathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Histiocytoid Cardiomyopathy** covering all of the
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


# Histiocytoid Cardiomyopathy: Comprehensive Disease-Characteristics Report

## Executive summary

Histiocytoid cardiomyopathy (HC) is an exceptionally rare, usually infantile myocardial/conduction-system disorder characterized by multifocal aggregates of enlarged, pale, mitochondria-rich cardiomyocytes with Purkinje/conduction-cell-like features. Although historically classified as a hamartoma or cardiac tumor, current molecular and ultrastructural evidence more strongly supports a **mitochondrial cardiomyopathy with marked arrhythmogenicity**. Fewer than 150 cases had been reported in the literature by the 2015 WHO-era review; consequently, nearly all quantitative evidence comes from aggregated case reports and small retrospective series rather than population registries or electronic-health-record cohorts. Most recognized patients present in the first year of life with ventricular tachyarrhythmia, heart failure, cardiac arrest, or sudden death. More than one-third reportedly have additional cardiac or extracardiac anomalies. (burke2016the2015who pages 2-3)

The strongest established molecular association is with **NDUFB11**, an X-chromosomal nuclear gene encoding an accessory subunit of mitochondrial respiratory-chain complex I. Patient-tissue studies show that pathogenic NDUFB11 variants can disrupt RNA splicing, eliminate or reduce NDUFB11 protein, impair complex-I assembly and activity, and alter respiratory supercomplexes. However, HC remains genetically heterogeneous or unsolved in many historical cases; an NDUFB11 result should therefore not be treated as necessary for diagnosis. (OpenTargets Search: histiocytoid cardiomyopathy-NDUFB11, amategarcia2023anovelmutation pages 6-8, amategarcia2023anovelmutation pages 5-6)

| domain | evidence-based finding | suggested ontology identifiers/terms | evidence strength or limitation |
|---|---|---|---|
| Disease identity | Histiocytoid cardiomyopathy is a rare pediatric cardiac disease/tumor-like lesion characterized by conduction-system-like altered cardiomyocytes; historical literature notes fewer than 150 reported cases and current disease mapping includes MONDO:0010771. Historical synonyms include oncocytic cardiomyopathy, Purkinje cell hamartoma, and cardiac hamartoma (burke2016the2015who pages 2-3, OpenTargets Search: histiocytoid cardiomyopathy-NDUFB11) | MONDO:0010771; term-only: histiocytoid cardiomyopathy; term-only synonyms: oncocytic cardiomyopathy, Purkinje cell hamartoma, cardiac hamartoma | Moderate evidence from reviews/database mapping; rarity means estimates are literature-derived, not registry-based (burke2016the2015who pages 2-3, OpenTargets Search: histiocytoid cardiomyopathy-NDUFB11) |
| Core demographics / epidemiology | Predominantly affects infants, especially in the first year of life; many presentations are ventricular tachyarrhythmia or sudden cardiac death (burke2016the2015who pages 2-3, adorisio2025mitochondrialcardiomyopathiesnavigating pages 3-4) | HPO term-only: Infantile onset; Ventricular tachycardia; Sudden cardiac death | Moderate evidence; no robust population incidence/prevalence study identified (burke2016the2015who pages 2-3) |
| Phenotype: arrhythmia / sudden death | The hallmark presentation is malignant ventricular arrhythmia, often with sudden death or near-fatal events in infancy (burke2016the2015who pages 2-3, adorisio2025mitochondrialcardiomyopathiesnavigating pages 3-4) | HPO term-only: Ventricular tachycardia; Arrhythmia; Sudden cardiac death | Strong clinical pattern across case literature/reviews, but frequency estimates remain imprecise (burke2016the2015who pages 2-3) |
| Phenotype: hypertrophic cardiomyopathy | Hypertrophic cardiomyopathy is a major phenotype in NDUFB11-related disease and may overlap the histiocytoid spectrum; severe neonatal obstructive HCM was reported in a 2024 female case (tariq2024casereportsevere pages 1-2, tariq2024casereportsevere pages 2-3) | HPO term-only: Hypertrophic cardiomyopathy | Strong for NDUFB11-associated mitochondrial cardiomyopathy; exact fraction specifically within histiocytoid cardiomyopathy is uncertain (tariq2024casereportsevere pages 1-2, tariq2024casereportsevere pages 2-3) |
| Phenotype: ventricular noncompaction | Ventricular noncompaction/LV noncompaction is reported in the broader NDUFB11/mitochondrial cardiomyopathy spectrum and historical histiocytoid literature (adorisio2025mitochondrialcardiomyopathiesnavigating pages 3-4, tariq2024casereportsevere pages 2-3) | HPO term-only: Left ventricular noncompaction | Limited disease-specific evidence; association appears real but uncommon and based largely on case reports/reviews (adorisio2025mitochondrialcardiomyopathiesnavigating pages 3-4, tariq2024casereportsevere pages 2-3) |
| Phenotype: heart failure | Progressive heart failure can occur rapidly in neonatal-onset NDUFB11-associated disease; death by 48 hours to 3 months has been documented in recent reports (amategarcia2023anovelmutation pages 2-5, tariq2024casereportsevere pages 1-2) | HPO term-only: Heart failure | Strong for severe neonatal mitochondrial presentations; not all histiocytoid cases have the same course (amategarcia2023anovelmutation pages 2-5, tariq2024casereportsevere pages 1-2) |
| Phenotype: lactic acidosis | Lactic acidosis supports mitochondrial respiratory-chain dysfunction and was documented in recent NDUFB11 neonatal cases (amategarcia2023anovelmutation pages 2-5, tariq2024casereportsevere pages 2-3) | HPO term-only: Lactic acidosis; Elevated serum lactate | Strong in molecularly solved NDUFB11 cases; not universal across all historical histiocytoid reports (amategarcia2023anovelmutation pages 2-5, tariq2024casereportsevere pages 2-3) |
| Congenital anomalies / syndromic overlap | More than one-third of affected children have additional cardiac or extracardiac anomalies; overlap with microphthalmia with linear skin defects syndrome (MLS) has been reported in NDUFB11-related females (burke2016the2015who pages 2-3, amategarcia2023anovelmutation pages 6-8) | HPO term-only: Multiple congenital anomalies; Microphthalmia; Linear skin defects | Moderate evidence; anomaly spectrum is heterogeneous and incompletely standardized (burke2016the2015who pages 2-3, amategarcia2023anovelmutation pages 6-8) |
| Causal gene | NDUFB11 is the principal established disease gene linked to histiocytoid cardiomyopathy in current evidence resources and human studies (OpenTargets Search: histiocytoid cardiomyopathy-NDUFB11, amategarcia2023anovelmutation pages 6-8) | HGNC symbol: NDUFB11; term-only: NADH:ubiquinone oxidoreductase subunit B11 | Strongest currently available gene-level evidence; other reported genes/variants remain secondary or candidate-level for this phenotype (OpenTargets Search: histiocytoid cardiomyopathy-NDUFB11, amategarcia2023anovelmutation pages 6-8) |
| Inheritance | Inheritance is X-linked; affected males may present with severe neonatal disease, while heterozygous females may be asymptomatic or variably affected depending on X-inactivation (amategarcia2023anovelmutation pages 6-8, amategarcia2023anovelmutation pages 5-6, tariq2024casereportsevere pages 2-3) | term-only: X-linked inheritance | Strong human genetic evidence from segregation and de novo case reports (amategarcia2023anovelmutation pages 6-8, amategarcia2023anovelmutation pages 5-6, tariq2024casereportsevere pages 2-3) |
| Variable expressivity / X-inactivation | Skewed X-chromosome inactivation appears to modify penetrance and severity in females; recent work documented skewing ratios around 78:22 and 80:20 in carriers (amategarcia2023anovelmutation pages 5-6, amategarcia2023anovelmutation pages 8-9) | term-only: Skewed X-inactivation | Strong mechanistic modifier evidence in families studied, but based on small numbers (amategarcia2023anovelmutation pages 5-6, amategarcia2023anovelmutation pages 8-9) |
| Molecular mechanism | NDUFB11 encodes a mitochondrial respiratory-chain Complex I subunit; pathogenic variants impair canonical transcript/protein production, causing defective Complex I assembly/activity and mitochondrial cardiomyopathy (amategarcia2023anovelmutation pages 6-8, amategarcia2023anovelmutation pages 5-6, amategarcia2023anovelmutation pages 2-5) | GO term-only: mitochondrial respiratory chain complex I assembly; oxidative phosphorylation; mitochondrial electron transport, NADH to ubiquinone | Strong functional evidence from patient heart/skeletal muscle assays; pathway assignment is well supported (amategarcia2023anovelmutation pages 6-8, amategarcia2023anovelmutation pages 5-6, amategarcia2023anovelmutation pages 2-5) |
| Transcript/protein dysfunction | A 2023 NDUFB11 variant at the last nucleotide of exon 2 caused loss of the canonical short transcript, upregulation of a longer alternative transcript, absent/reduced NDUFB11 protein, and isolated Complex I deficiency (amategarcia2023anovelmutation pages 6-8, amategarcia2023anovelmutation pages 5-6, amategarcia2023anovelmutation pages 2-5) | Sequence Ontology term-only: splice-region/splice-altering variant; GO term-only: RNA splicing; protein-containing complex assembly | Strong disease-mechanism evidence, but derived from one deeply characterized family/proband (amategarcia2023anovelmutation pages 6-8, amategarcia2023anovelmutation pages 5-6, amategarcia2023anovelmutation pages 2-5) |
| Anatomy: organ / tissue | Primary sites are myocardium and endocardium, especially ventricles and atrioventricular/sinoatrial nodal regions, with conduction-system involvement central to pathobiology (burke2016the2015who pages 2-3) | UBERON term-only: heart; cardiac ventricle myocardium; atrioventricular node; sinoatrial node; endocardium; myocardium | Moderate evidence from pathology reviews; exact lesion distribution varies case to case (burke2016the2015who pages 2-3) |
| Cell type involvement | Lesional cells resemble modified myocytes of the cardiac conduction system / Purkinje-like cardiomyocytes (burke2016the2015who pages 2-3) | CL term-only: cardiac muscle cell; Purkinje myocyte / conduction cardiomyocyte | Moderate evidence; precise modern cell-ontology mapping remains uncertain because historical pathology predates single-cell classification (burke2016the2015who pages 2-3) |
| Subcellular localization | Mitochondria are central affected organelles; older pathology and modern mitochondrial genetics support abnormal mitochondrial accumulation/dysfunction in lesional cardiomyocytes (burke2016the2015who pages 2-3, amategarcia2023anovelmutation pages 6-8) | GO Cellular Component term-only: mitochondrion; mitochondrial inner membrane; respiratory chain complex I | Moderate-to-strong evidence; ultrastructural detail is not uniformly available in recent accessible sources (burke2016the2015who pages 2-3, amategarcia2023anovelmutation pages 6-8) |
| Diagnostic approach | Diagnosis is multimodal: ECG/rhythm monitoring for ventricular arrhythmia, echocardiography/cardiac MRI for cardiomyopathy morphology, metabolic testing for lactate/mitochondrial clues, and broad genomic testing (preferably WGS/WES or mitochondrial/cardiomyopathy panels that include NDUFB11); pathology remains definitive in some cases (tariq2024casereportsevere pages 1-2, tariq2024casereportsevere pages 2-3, amategarcia2023anovelmutation pages 6-8, amategarcia2023anovelmutation pages 2-5) | NCIT term-only: Electrocardiography; Echocardiography; Cardiac Magnetic Resonance Imaging; Whole Genome Sequencing; Whole Exome Sequencing; Gene Panel Sequencing; Pathologic Examination | Strong practical inference from recent case reports; no disease-specific consensus guideline identified (tariq2024casereportsevere pages 1-2, tariq2024casereportsevere pages 2-3, amategarcia2023anovelmutation pages 6-8, amategarcia2023anovelmutation pages 2-5) |
| Genetic testing implication | Recent evidence shows NDUFB11 may be missed by some commercial cardiomyopathy panels; rapid WGS can be critical in infantile cases (tariq2024casereportsevere pages 1-2) | NCIT term-only: Whole Genome Sequencing; Molecular Genetic Testing | Strong for at least some current panels; panel content is lab-dependent and changes over time (tariq2024casereportsevere pages 1-2) |
| Treatment categories | No approved disease-specific therapy exists. Management is case-based and may include antiarrhythmics/beta-blockade, catheter ablation or surgical lesion-directed treatment in selected arrhythmic cases, intensive heart-failure support, ECMO/VAD bridge, and heart transplantation; supportive mitochondrial care is empirical (recent disease-specific trials not found) (adorisio2025mitochondrialcardiomyopathiesnavigating pages 3-4, tariq2024casereportsevere pages 1-2) | NCIT term-only: Antiarrhythmic Therapy; Beta Adrenergic Receptor Blocking Agent Therapy; Catheter Ablation; Surgical Excision; Extracorporeal Membrane Oxygenation; Ventricular Assist Device; Heart Transplantation; Supportive Care | Weak-to-moderate evidence because treatment data are almost entirely case reports/series and extrapolation from pediatric mitochondrial cardiomyopathy practice (adorisio2025mitochondrialcardiomyopathiesnavigating pages 3-4, tariq2024casereportsevere pages 1-2) |
| Prognosis | Prognosis is often poor with highest mortality in infancy, particularly first-year presentations and severe neonatal mitochondrial disease (adorisio2025mitochondrialcardiomyopathiesnavigating pages 3-4, amategarcia2023anovelmutation pages 2-5, tariq2024casereportsevere pages 1-2) | HPO term-only: Sudden cardiac death; Infantile onset; Heart failure | Moderate evidence; no prospective natural-history cohort specific to histiocytoid cardiomyopathy identified (adorisio2025mitochondrialcardiomyopathiesnavigating pages 3-4, amategarcia2023anovelmutation pages 2-5, tariq2024casereportsevere pages 1-2) |
| Environmental / infectious factors | No reproducible environmental, lifestyle, occupational, or infectious causes are established; current evidence supports a primarily genetic/mitochondrial mechanism (amategarcia2023anovelmutation pages 6-8, amategarcia2023anovelmutation pages 1-2) | term-only: not established / no ontology assignment | Evidence gap rather than negative proof; rarity limits epidemiologic inference (amategarcia2023anovelmutation pages 6-8, amategarcia2023anovelmutation pages 1-2) |
| Major evidence gaps | No disease-specific clinical trials were found; limited epidemiology, no standardized diagnostic criteria, sparse quality-of-life data, no validated biomarkers beyond mitochondrial testing, and little disease-specific single-cell/spatial omics or model-organism work (adorisio2025mitochondrialcardiomyopathiesnavigating pages 3-4, OpenTargets Search: histiocytoid cardiomyopathy-NDUFB11, amategarcia2023anovelmutation pages 6-8) | term-only: evidence gap; natural history study needed; biomarker development needed | Strong confidence that evidence is sparse because multiple searches yielded little disease-specific prospective/experimental literature (adorisio2025mitochondrialcardiomyopathiesnavigating pages 3-4, OpenTargets Search: histiocytoid cardiomyopathy-NDUFB11, amategarcia2023anovelmutation pages 6-8) |


*Table: This table condenses the main evidence-based facts for histiocytoid cardiomyopathy, including core phenotype, genetics, mechanism, anatomy, diagnostics, treatment categories, and evidence limitations. It is designed for rapid knowledge-base curation with ontology term suggestions and citation-backed confidence notes.*

## 1. Disease information

### Definition and classification

HC is a rare pediatric cardiomyopathy in which abnormal myocardial cells resemble histiocytes by light microscopy but are actually modified cardiomyocytes, often interpreted as conduction-system/Purkinje-like cells. Lesions are usually multifocal and occur in myocardium and endocardium, particularly the ventricles and atrioventricular or sinoatrial nodal regions. This localization explains the disproportionate burden of malignant ventricular arrhythmia. (burke2016the2015who pages 2-3)

The designation “tumor” is historical and potentially misleading: lesions are non-metastatic, and genetic, biochemical, and ultrastructural findings support a developmental/mitochondrial cardiomyopathy rather than a conventional neoplasm.

### Identifiers and synonyms

* **MONDO:** **MONDO:0010771**.
* **Open Targets disease–target association:** MONDO:0010771–NDUFB11 (ENSG00000147123), based on five underlying evidence records in the retrieved database result. (OpenTargets Search: histiocytoid cardiomyopathy-NDUFB11)
* **Common names:** histiocytoid cardiomyopathy; infantile histiocytoid cardiomyopathy; oncocytic cardiomyopathy; infantile xanthomatous cardiomyopathy; arachnocytosis of the myocardium; Purkinje-cell hamartoma/dysplasia; conduction-system hamartoma; cardiac hamartoma.
* **OMIM/Orphanet/MeSH/ICD:** No disease-specific OMIM, Orphanet, MeSH, ICD-10, or ICD-11 identifier was verified in the retrieved evidence. Coding generally falls under broader cardiomyopathy, cardiac-arrhythmia, congenital-heart-disease, or cardiac-tumor categories; such mappings should be labeled approximate rather than equivalent.

### Evidence granularity

The disease description is an **aggregated disease-level synthesis** assembled predominantly from published individual cases, autopsy material, small pathology series, and a historical HC registry. It is not based on a large EHR-derived cohort. This distinction matters because ascertainment is strongly biased toward lethal, surgically treated, or pathologically confirmed cases.

## 2. Etiology, risk, and protective factors

### Causal factors

The leading cause is genetic mitochondrial respiratory-chain dysfunction. **NDUFB11** is the principal established nuclear gene. Pathogenic variants cause deficient complex-I assembly/function and can produce HC, hypertrophic cardiomyopathy, left-ventricular noncompaction, sideroblastic anemia, or microphthalmia with linear skin defects syndrome. Open Targets identifies NDUFB11 as the sole associated target returned for MONDO:0010771. (OpenTargets Search: histiocytoid cardiomyopathy-NDUFB11, amategarcia2023anovelmutation pages 1-2)

A sporadic mitochondrial-DNA **m.8344A>G** MERRF-associated case has also been published, but this is isolated evidence and does not establish a common cause. Reports involving other genes, including possible ion-channel modifiers, should presently be regarded as candidate or case-level associations rather than validated HC genes.

### Risk factors and modifiers

* **Sex and X chromosome:** Historical HC has a strong female predominance, while severe hemizygous NDUFB11 loss can be lethal in males. This apparently paradoxical distribution likely reflects variant-specific viability, X-linked biology, and ascertainment.
* **X-chromosome inactivation:** Female penetrance is modified by tissue-specific X-inactivation. In one 2023 family, clinically protected carrier women had skewing of **78:22 and 80:20**, preferentially inactivating the variant-bearing chromosome. Conversely, unfavorable skewing was proposed to explain severe disease in a female neonate. (amategarcia2023anovelmutation pages 5-6, amategarcia2023anovelmutation pages 8-9, tariq2024casereportsevere pages 1-2)
* **Family history:** X-linked recurrence is possible, but de novo variants and apparently sporadic disease occur.
* **Congenital anomalies:** More than one-third of reported children had additional cardiac or extracardiac anomalies, but these are associated manifestations, not demonstrated causal exposures. (burke2016the2015who pages 2-3)

No reproducible environmental, dietary, toxic, occupational, infectious, lifestyle, or maternal exposure has been established. No validated genetic or environmental protective factor exists apart from the inferred protection conferred by favorable X-inactivation in some heterozygous women. No gene–environment interaction has been demonstrated.

## 3. Phenotypes

### Core cardiac manifestations

1. **Ventricular tachyarrhythmia**—often severe, episodic, treatment-resistant, and capable of causing cardiac arrest or sudden death. Suggested HPO: *Ventricular tachycardia*, *Ventricular arrhythmia*, *Cardiac arrest*.
2. **Sudden cardiac death**, frequently during infancy and occasionally the first recognized manifestation. Suggested HPO: *Sudden cardiac death*.
3. **Cardiomyopathy morphology**—hypertrophic, dilated, or noncompaction phenotypes can accompany the histiocytoid lesion. Mitochondrial cardiomyopathy literature describes reduced fractional shortening and relatively concentric hypertrophy, with the worst mortality among patients diagnosed during the first year. Suggested HPO: *Hypertrophic cardiomyopathy*, *Dilated cardiomyopathy*, *Left ventricular noncompaction*, *Reduced left ventricular systolic function*. (adorisio2025mitochondrialcardiomyopathiesnavigating pages 3-4)
4. **Heart failure**—severity ranges from absent/asymptomatic childhood disease to rapidly progressive neonatal failure. Suggested HPO: *Heart failure*, *Cardiomegaly*, *Poor cardiac output*. (adorisio2025mitochondrialcardiomyopathiesnavigating pages 3-4, tariq2024casereportsevere pages 1-2)
5. **Conduction/pre-excitation abnormalities**—conduction-system localization makes bradyarrhythmia, conduction block, ectopy, and Wolff–Parkinson–White-like presentations biologically plausible and reported in case literature. Suggested HPO: *Cardiac conduction abnormality*, *Ventricular premature beat*, *Pre-excitation syndrome*.

### Metabolic and syndromic manifestations

Lactic acidosis, elevated lactate/pyruvate ratio, failure to thrive, hypotonia/myopathy, epilepsy, sideroblastic anemia, microphthalmia, and linear skin defects occur in parts of the broader NDUFB11 spectrum but are not universal features of pathology-defined HC. A 2024 female neonate had a lactate/pyruvate ratio of **67.5**. (amategarcia2023anovelmutation pages 1-2, tariq2024casereportsevere pages 2-3)

Suggested HPO terms include *Lactic acidosis*, *Elevated circulating lactate concentration*, *Failure to thrive*, *Muscular hypotonia*, *Seizure*, *Sideroblastic anemia*, *Microphthalmia*, and *Aplasia cutis/linear skin defect* as phenotype-appropriate.

### Frequency, progression, and quality of life

Reliable phenotype percentages are unavailable. The most defensible qualitative frequencies are: infantile onset—common; ventricular arrhythmia/sudden death—common and characteristic; extracardiac or additional cardiac anomalies—**>33%** in the WHO review; cardiomyopathy morphology and heart failure—variable. (burke2016the2015who pages 2-3)

No HC-specific EQ-5D, SF-36, PROMIS, neurobehavioral, or caregiver-burden studies were found. Survivors may face recurrent hospitalization, medication burden, implanted devices, ablation or transplantation, and substantial restrictions related to arrhythmic risk.

## 4. Genetic and molecular information

### Principal causal gene

**NDUFB11**—NADH:ubiquinone oxidoreductase subunit B11; Xp11.23; Ensembl **ENSG00000147123**. It encodes an approximately 17.3-kDa accessory component of the membrane/P module of mitochondrial complex I. (OpenTargets Search: histiocytoid cardiomyopathy-NDUFB11, amategarcia2023anovelmutation pages 6-8, tariq2024casereportsevere pages 2-3)

### Documented recent variants

* **c.338G>A**, initially predicted **p.(Arg113Lys)**: hemizygous, inherited from the mother, and classified likely pathogenic under ACMG/AMP criteria. Because it affects the last nucleotide of exon 2, its principal consequence is abnormal splicing rather than a simple missense substitution. The affected male died at 48 hours. (amategarcia2023anovelmutation pages 5-6, amategarcia2023anovelmutation pages 2-5)
* **c.391G>A, p.Glu131Lys:** de novo variant found by whole-genome sequencing in a female neonate with obstructive hypertrophic cardiomyopathy, lactic acidosis, progressive heart failure, and death by three months. (tariq2024casereportsevere pages 1-2)
* Previously summarized pathogenic alleles include nonsense/frameshift variants such as **p.Trp85\***, **p.Arg88\***, **p.Tyr108\***, and **p.Arg134Serfs\*3**, particularly among symptomatic females. (amategarcia2023anovelmutation pages 8-9)

The 2023 report counted **eight pathogenic NDUFB11 variants among 15 previously reported patients**, with cardiomyopathy in approximately **67%**. This statistic describes the reported NDUFB11 disease spectrum, not the proportion of all HC attributable to NDUFB11. (amategarcia2023anovelmutation pages 6-8)

Population allele frequencies were not available in the retrieved evidence. Given severe early-onset disease and ACMG classifications, causal alleles are expected to be absent or extremely rare in reference populations, but each variant requires direct gnomAD/ClinVar verification before database deposition. Variants are germline; no recurrent somatic mechanism is established.

### Functional consequence

For c.338G>A, the normal **462-bp canonical transcript** (NM_001135998; 153 amino acids) was lost, while a **492-bp alternative transcript** retaining 30 additional bases increased. The longer RNA did not generate stable functional protein. NDUFB11 protein was undetectable in heart and severely reduced in skeletal muscle; skeletal-muscle complex-I activity was **22.7% of control**. Respiratory supercomplex analysis showed reduced complex I within the respirasome and I+III₂ assemblies, with compensatory accumulation of III₂+IV and dimeric IV species. (amategarcia2023anovelmutation pages 6-8, amategarcia2023anovelmutation pages 5-6, amategarcia2023anovelmutation pages 2-5)

Direct abstract-level statement from the 2023 study: **“the canonical ‘short’ transcript is required for the proper NDUFB11 protein synthesis, which is essential for optimal CI assembly and activity.”** (amategarcia2023anovelmutation pages 6-8)

No validated modifier gene, recurrent chromosomal rearrangement, disease-specific DNA-methylation signature, or pathogenic somatic clone is established. X-inactivation is the best-supported epigenetic modifier.

## 5. Environmental information

There is no established role for smoking, diet, exercise, alcohol, pollution, radiation, occupational toxins, medication exposure, or infection in initiating HC. Acute illness may unmask mitochondrial energy failure or precipitate arrhythmia, but this is a physiologic stress response rather than a proven etiologic gene–environment interaction. No pathogen, zoonotic agent, vaccine relationship, or transmissible mechanism applies.

## 6. Mechanism and pathophysiology

### Causal chain

**Upstream germline variant** → altered NDUFB11 transcript or protein → defective assembly/stability of mitochondrial respiratory-chain complex I → impaired NADH-to-ubiquinone electron transfer and oxidative phosphorylation → deficient ATP production, disturbed redox balance, and compensatory mitochondrial proliferation in energy-intensive cardiomyocytes → swollen/oncocytic “histiocytoid” cells, preferentially involving conduction-system-rich myocardial regions → abnormal impulse formation/conduction and myocardial dysfunction → ventricular tachyarrhythmia, heart failure, cardiac arrest, or sudden death. Patient heart and skeletal-muscle studies directly support the transcript-to-complex-I portion of this chain. (amategarcia2023anovelmutation pages 6-8, amategarcia2023anovelmutation pages 5-6, amategarcia2023anovelmutation pages 2-5)

### Cells, anatomy, and ontology suggestions

* **Cell types:** working cardiomyocyte; cardiac conduction/Purkinje-like myocyte. Suggested CL terms: *cardiac muscle cell* and *cardiac Purkinje cell*; exact current identifiers should be ontology-validated.
* **Processes:** GO term suggestions—*mitochondrial respiratory chain complex I assembly*, *mitochondrial electron transport, NADH to ubiquinone*, *oxidative phosphorylation*, *ATP metabolic process*, *mitochondrial organization*, and *cardiac muscle contraction*.
* **Compartments:** GO suggestions—*mitochondrion*, *mitochondrial inner membrane*, *respiratory-chain complex I*, and *mitochondrial respirasome*.
* **Downstream damage:** energy failure, electrical instability, myocardial hypertrophy/remodeling, and terminal low-output/multiorgan failure. Chronic inflammation, autoimmunity, and primary fibrosis are not established initiating mechanisms.

### Molecular profiling and advanced technologies

A historical whole-genome-expression study proposed candidate pathways, but no replicated diagnostic expression signature exists. The most informative recent profiling used RT-qPCR, Western blotting, blue-native PAGE, two-dimensional BN/SDS-PAGE, and enzyme assays in patient heart and muscle. (amategarcia2023anovelmutation pages 9-11)

No disease-specific single-cell RNA-seq, spatial transcriptomic atlas, proteomic cohort, metabolomic/lipidomic signature, CRISPR screen, or integrated multi-omics study was identified. Lactic acidosis is a nonspecific marker of respiratory-chain dysfunction, not an HC-specific metabolomic biomarker.

## 7. Anatomical structures affected

The primary organ is the **heart**, especially ventricular myocardium and endocardium, with frequent involvement of atrioventricular and sinoatrial nodal/conduction regions. Lesions are often multiple rather than lateralized. Suggested UBERON terms are *heart*, *myocardium*, *endocardium*, *cardiac ventricle*, *interventricular septum*, *sinoatrial node*, and *atrioventricular node*. (burke2016the2015who pages 2-3)

At tissue level, cardiac muscle and specialized conducting myocardium are affected. At subcellular level, the mitochondrial inner membrane and respiratory-chain complex I are central. Secondary organs may become involved through low cardiac output/multiorgan failure or as part of a syndromic NDUFB11 disorder; they are not necessarily sites of histiocytoid lesions.

## 8. Temporal development

HC is generally congenital or infantile. Most recognized patients present during the first year; severe NDUFB11 disease may manifest prenatally with hypertrophy/growth restriction or within hours after birth with lactic acidosis and heart failure. Nonetheless, asymptomatic childhood cases occur. (burke2016the2015who pages 2-3, adorisio2025mitochondrialcardiomyopathiesnavigating pages 3-4, tariq2024casereportsevere pages 1-2)

The course is highly variable:

* **Hyperacute:** neonatal metabolic decompensation, refractory heart failure, or fatal arrhythmia within hours or days.
* **Episodic:** recurrent ventricular tachycardia between periods of relative stability.
* **Progressive:** increasing hypertrophy, obstruction, systolic dysfunction, and heart failure.
* **Occult:** sudden death without a prior diagnosis.

There are no validated stages or remission criteria. The neonatal period and first year are the highest-risk windows; mortality is greatest among those diagnosed before one year. (adorisio2025mitochondrialcardiomyopathiesnavigating pages 3-4)

## 9. Inheritance and population

No population-based prevalence or incidence has been established. “Fewer than 150 reported cases” is a publication count, not prevalence. HC is therefore appropriately classified as ultra-rare. (burke2016the2015who pages 2-3)

NDUFB11-associated disease is **X-linked**, with variable penetrance and expressivity determined partly by variant class and X-inactivation. Males may have severe hemizygous neonatal disease; heterozygous females range from unaffected to lethal disease. De novo variants occur. Genetic anticipation, founder effects, consanguinity effects, carrier frequency, and germline mosaicism rates have not been established. (amategarcia2023anovelmutation pages 6-8, amategarcia2023anovelmutation pages 5-6, tariq2024casereportsevere pages 1-2)

No robust ethnic or geographic enrichment is known. Historical female predominance should not be converted into a precise sex ratio because of small samples, male prenatal/neonatal lethality, and case-selection bias.

## 10. Diagnostics

### Clinical workflow

1. **Recognize the phenotype:** infant with unexplained ventricular ectopy/tachycardia, cardiac arrest, hypertrophic or noncompaction cardiomyopathy, or syndromic features.
2. **Electrophysiology:** 12-lead ECG, continuous telemetry, Holter/event monitoring, and electrophysiology study when ablation is contemplated.
3. **Imaging:** echocardiography for hypertrophy, obstruction, ventricular function, and noncompaction; cardiac MRI for anatomy, multifocal lesions, tissue characterization, and scar when feasible.
4. **Metabolic evaluation:** serum lactate, pyruvate and ratio, blood gas, glucose, creatine kinase, acylcarnitines, amino/organic acids, complete blood count for sideroblastic anemia, and broader mitochondrial assessment. Normal values do not exclude HC.
5. **Genetics:** rapid trio WGS or WES with copy-number and mitochondrial-genome analysis is preferred in critically ill infants. At minimum, panels must include **NDUFB11** and relevant nuclear/mtDNA mitochondrial cardiomyopathy genes. A 2024 pathogenic NDUFB11 variant was missed by commercial cardiomyopathy panels and detected by WGS. (tariq2024casereportsevere pages 1-2)
6. **Tissue studies:** myocardial biopsy or explanted/autopsy heart can establish morphology. When available, electron microscopy, mitochondrial immunohistochemistry, respiratory-chain enzyme testing, RNA studies, and BN-PAGE can confirm mechanism. Skeletal muscle may show biochemical complex-I deficiency despite bland histology. (amategarcia2023anovelmutation pages 5-6)

### Pathology

Expected findings include multifocal nodules or sheets of large polygonal cells with pale, foamy/eosinophilic granular cytoplasm, reduced contractile apparatus, and abundant abnormal mitochondria. Immunophenotyping supports myocardial/conduction-cell rather than macrophage origin. Definitive interpretation requires correlation with lesion distribution and ultrastructure because “histiocytoid” describes appearance, not lineage.

### Differential diagnosis

Important alternatives are rhabdomyoma, fibroma, Purkinje-cell/conduction-system lesions, glycogen-storage cardiomyopathy, fatty or vacuolated myocardial change, myocarditis, mitochondrial cytopathy without histiocytoid morphology, sarcomeric HCM, left-ventricular noncompaction, arrhythmogenic cardiomyopathy, channelopathy/long-QT syndrome, and tachycardia-induced cardiomyopathy. Distinguishing features include multifocal mitochondria-rich histiocytoid myocytes, conduction-system distribution, mitochondrial biochemical/genetic findings, and absence of a conventional neoplastic architecture.

There are no universally accepted disease-specific clinical diagnostic criteria. Prenatal or cascade testing is possible only after a familial pathogenic variant has been established. HC is not part of routine newborn screening.

## 11. Outcome and prognosis

The prognosis is guarded, especially with neonatal or first-year presentation, complex-I deficiency, persistent ventricular arrhythmia, or progressive ventricular dysfunction. Recent molecularly solved severe cases ended in death at **48 hours** and **three months**, respectively. (amategarcia2023anovelmutation pages 2-5, tariq2024casereportsevere pages 1-2)

No reliable 5- or 10-year survival rate, life-expectancy estimate, disability-adjusted burden, or validated prognostic model exists. Major complications are recurrent ventricular tachycardia, torsades/ventricular fibrillation, sudden death, heart failure, thromboembolic or device complications, and multiorgan failure. Earlier diagnosis, localized resectable disease, rhythm control, and access to mechanical support/transplant may improve individual outcomes, but comparative effectiveness has not been established.

## 12. Treatment and current implementation

No medication, gene therapy, RNA therapy, or mitochondrial therapy is approved specifically for HC. Management is individualized in a pediatric electrophysiology, heart-failure, mitochondrial-genetics, and cardiac-surgery center.

* **Acute arrhythmia care:** resuscitation, cardioversion/defibrillation, correction of electrolyte and acid–base disturbances, and intravenous antiarrhythmics according to rhythm and pediatric protocols.
* **Chronic rhythm control:** beta-blockers, amiodarone, sodium-channel blockers, or combinations have been used. A 2023 case report proposed high-dose carvedilol, but a single case cannot establish efficacy. In the 2024 NDUFB11 female case, beta-blockade did not prevent progressive failure. (tariq2024casereportsevere pages 1-2)
* **Catheter ablation:** may control a dominant premature-ventricular-complex or ventricular-tachycardia focus, including reported infant torsades triggers; multifocal myocardial disease limits durability.
* **Surgical excision:** considered when a discrete arrhythmogenic lesion can be safely localized and removed.
* **Device therapy:** pacemaker or implantable cardioverter-defibrillator decisions are individualized; small infant size and rapidly progressive disease complicate implantation.
* **Heart-failure support:** diuretics, afterload reduction, inotropes, ventilation, and nutritional/metabolic support as clinically indicated.
* **Advanced support:** ECMO or biventricular assist devices have been used as rescue/bridge strategies; orthotopic heart transplantation has been reported.
* **Mitochondrial supplements:** coenzyme Q10, riboflavin, thiamine, or related “mitochondrial cocktails” may be considered for broader mitochondrial disease but have no demonstrated HC-specific response rate.

Suggested NCIT intervention terms include *Antiarrhythmic Therapy*, *Beta-Blocker Therapy*, *Electrical Cardioversion*, *Catheter Ablation*, *Surgical Resection*, *Implantable Cardioverter Defibrillator*, *Extracorporeal Membrane Oxygenation*, *Ventricular Assist Device*, and *Heart Transplantation*. No disease-specific interventional ClinicalTrials.gov study was identified in the tool search.

## 13. Prevention

Primary prevention through lifestyle or immunization is not applicable. For a family with a pathogenic variant, prevention and early detection consist of genetic counseling, cascade testing, reproductive options such as prenatal or preimplantation genetic testing, and fetal echocardiography/rhythm assessment. Because X-inactivation makes female phenotype prediction unreliable, genotype alone cannot precisely predict severity.

Secondary prevention includes early ECG/echo surveillance of at-risk relatives and rapid evaluation of unexplained infantile arrhythmia. Tertiary prevention focuses on suppressing recurrent arrhythmia, preventing heart-failure decompensation, providing emergency-action planning, and considering ablation/device/advanced-heart-failure therapy before irreversible deterioration. There is no population screening program or prophylactic medication supported by disease-specific trials.

## 14. Other species and natural disease

A naturally occurring analogous lesion—Purkinje-fiber dysplasia/histiocytoid cardiomyopathy with ventricular noncompaction—has been described in a Savannah kitten. This supports comparative conservation of specialized conduction cardiomyocytes and mitochondrial pathology, but one veterinary case does not establish breed predisposition or a homologous NDUFB11 cause. Suggested taxonomy: *Felis catus*, NCBI Taxonomy **9685**. No zoonotic or cross-species transmission exists.

## 15. Model organisms

No validated engineered animal model was identified that reproduces the complete human combination of histiocytoid myocardial lesions, infantile malignant arrhythmia, sex bias, and NDUFB11-associated complex-I deficiency. The naturally affected feline case is a comparative-pathology model rather than a standardized experimental system.

Mechanistic work has instead used patient heart/skeletal muscle and NDUFB11 knockdown cell systems. The 2023 human-tissue study combined transcript analysis, respiratory-chain enzyme measurement, immunoblotting, and supercomplex analysis; this directly models biochemical disease but cannot reproduce whole-heart electrophysiology. (amategarcia2023anovelmutation pages 5-6, amategarcia2023anovelmutation pages 9-11)

Useful future systems include conditional cardiomyocyte- or conduction-cell-specific Ndufb11 mouse models, zebrafish rhythm models, CRISPR-engineered human iPSC cardiomyocytes, and cardiac/conduction-system organoids. Essential readouts would be complex-I assembly, oxygen consumption, ATP/redox state, mitochondrial ultrastructure, action potentials, triggered activity, conduction velocity, and arrhythmia susceptibility.

## Recent developments, 2023–2024

* **January 2023:** Amate-García and colleagues functionally characterized NDUFB11 c.338G>A in affected human tissues. Their work showed that a nominal “missense” change was actually splice-disrupting, eliminated the functional short transcript, altered respiratory supercomplexes, and reduced skeletal-muscle complex-I activity to 22.7% of control. DOI: https://doi.org/10.3390/ijms24021743. (amategarcia2023anovelmutation pages 6-8, amategarcia2023anovelmutation pages 2-5)
* **November 2023:** A case report described high-dose carvedilol as a potential antiarrhythmic strategy; this remains anecdotal and should not be generalized without comparative data. DOI: https://doi.org/10.1093/ehjcr/ytad588.
* **July 2024:** Tariq and colleagues reported the first female neonate with severe obstructive HCM attributed to de novo NDUFB11 c.391G>A (p.Glu131Lys). Rapid WGS succeeded where commercial cardiomyopathy panels did not; the infant died by three months despite beta-blockade. DOI: https://doi.org/10.1093/ehjcr/ytae377. (tariq2024casereportsevere pages 1-2, tariq2024casereportsevere pages 2-3)

These developments reinforce two expert conclusions: NDUFB11 disease is broader than classical histiocytoid morphology, and broad rapid genomic testing plus functional RNA/protein studies may be necessary to establish pathogenicity.

## Evidence-quality assessment and priority gaps

Evidence is strongest for the infantile arrhythmic phenotype, conduction-system-like mitochondrial pathology, and NDUFB11/complex-I mechanism. It is weakest for epidemiologic rates, penetrance, treatment effectiveness, long-term quality of life, and genotype-specific prognosis. There are no prospective natural-history studies, standardized criteria, validated circulating biomarkers, disease-specific trials, or replicated advanced-omics datasets. Reported-case totals and phenotype percentages are especially vulnerable to publication and survivor bias. Accordingly, treatment claims should remain labeled **case-report/series evidence**, while NDUFB11 functional findings can be labeled **human tissue molecular evidence**.

### Key source links and dates

1. Burke A, Tavora F. *The 2015 WHO Classification of Tumors of the Heart and Pericardium.* Published April 2016. https://doi.org/10.1016/j.jtho.2015.11.009. (burke2016the2015who pages 2-3)
2. Amate-García G, et al. *A Novel Mutation Associated with Neonatal Lethal Cardiomyopathy Leads to an Alternative Transcript Expression in the X-Linked Complex I NDUFB11 Gene.* Published January 2023. https://doi.org/10.3390/ijms24021743. (amategarcia2023anovelmutation pages 6-8, amategarcia2023anovelmutation pages 5-6)
3. Tariq J, et al. *Severe hypertrophic cardiomyopathy in a female neonate caused by de novo variant in NDUFB11.* Published July 2024. https://doi.org/10.1093/ehjcr/ytae377. (tariq2024casereportsevere pages 1-2)
4. Open Targets Platform, disease–target record for MONDO:0010771 and NDUFB11, accessed through the current tool query. (OpenTargets Search: histiocytoid cardiomyopathy-NDUFB11)
5. Adorisio R, et al. *Mitochondrial cardiomyopathies: navigating through different clinical and management pictures between adult and paediatric forms.* Published July 2025; used only as a current contextual review where 2023–2024 HC-specific evidence was sparse. https://doi.org/10.3389/fcvm.2025.1621096. (adorisio2025mitochondrialcardiomyopathiesnavigating pages 3-4)

References

1. (burke2016the2015who pages 2-3): Allen Burke and Fabio Tavora. The 2015 who classification of tumors of the heart and pericardium. Journal of thoracic oncology : official publication of the International Association for the Study of Lung Cancer, 11 4:441-52, Apr 2016. URL: https://doi.org/10.1016/j.jtho.2015.11.009, doi:10.1016/j.jtho.2015.11.009. This article has 342 citations.

2. (OpenTargets Search: histiocytoid cardiomyopathy-NDUFB11): Open Targets Query (histiocytoid cardiomyopathy-NDUFB11, 3 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

3. (amategarcia2023anovelmutation pages 6-8): Guillermo Amate-García, María Juliana Ballesta-Martínez, Pablo Serrano-Lorenzo, Rocío Garrido-Moraga, Adrián González-Quintana, Alberto Blázquez, Juan C. Rubio, Inés García-Consuegra, Joaquín Arenas, Cristina Ugalde, María Morán, Encarnación Guillén-Navarro, and Miguel A. Martín. A novel mutation associated with neonatal lethal cardiomyopathy leads to an alternative transcript expression in the x-linked complex i ndufb11 gene. International Journal of Molecular Sciences, 24:1743, Jan 2023. URL: https://doi.org/10.3390/ijms24021743, doi:10.3390/ijms24021743. This article has 16 citations.

4. (amategarcia2023anovelmutation pages 5-6): Guillermo Amate-García, María Juliana Ballesta-Martínez, Pablo Serrano-Lorenzo, Rocío Garrido-Moraga, Adrián González-Quintana, Alberto Blázquez, Juan C. Rubio, Inés García-Consuegra, Joaquín Arenas, Cristina Ugalde, María Morán, Encarnación Guillén-Navarro, and Miguel A. Martín. A novel mutation associated with neonatal lethal cardiomyopathy leads to an alternative transcript expression in the x-linked complex i ndufb11 gene. International Journal of Molecular Sciences, 24:1743, Jan 2023. URL: https://doi.org/10.3390/ijms24021743, doi:10.3390/ijms24021743. This article has 16 citations.

5. (adorisio2025mitochondrialcardiomyopathiesnavigating pages 3-4): Rachele Adorisio, Nicoletta Cantarutti, Barbara Siri, Elisa Bellettini, Gessica Ingrasciotta, Erica Mencarelli, Francesca Graziani, Rosa Lillo, Sara Di Marzio, Corrado Di Mambro, Fabrizio Drago, Antonio Amodeo, and Diego Martinelli. Mitochondrial cardiomyopathies: navigating through different clinical and management pictures between adult and paediatric forms. Frontiers in Cardiovascular Medicine, Jul 2025. URL: https://doi.org/10.3389/fcvm.2025.1621096, doi:10.3389/fcvm.2025.1621096. This article has 3 citations and is from a peer-reviewed journal.

6. (tariq2024casereportsevere pages 1-2): Javeria Tariq, Madeleine Townsend, Sumit Parikh, and Jeffrey Bennett. Case report: severe hypertrophic cardiomyopathy in a female neonate caused by de novo variant in ndufb11. European Heart Journal. Case Reports, Jul 2024. URL: https://doi.org/10.1093/ehjcr/ytae377, doi:10.1093/ehjcr/ytae377. This article has 3 citations.

7. (tariq2024casereportsevere pages 2-3): Javeria Tariq, Madeleine Townsend, Sumit Parikh, and Jeffrey Bennett. Case report: severe hypertrophic cardiomyopathy in a female neonate caused by de novo variant in ndufb11. European Heart Journal. Case Reports, Jul 2024. URL: https://doi.org/10.1093/ehjcr/ytae377, doi:10.1093/ehjcr/ytae377. This article has 3 citations.

8. (amategarcia2023anovelmutation pages 2-5): Guillermo Amate-García, María Juliana Ballesta-Martínez, Pablo Serrano-Lorenzo, Rocío Garrido-Moraga, Adrián González-Quintana, Alberto Blázquez, Juan C. Rubio, Inés García-Consuegra, Joaquín Arenas, Cristina Ugalde, María Morán, Encarnación Guillén-Navarro, and Miguel A. Martín. A novel mutation associated with neonatal lethal cardiomyopathy leads to an alternative transcript expression in the x-linked complex i ndufb11 gene. International Journal of Molecular Sciences, 24:1743, Jan 2023. URL: https://doi.org/10.3390/ijms24021743, doi:10.3390/ijms24021743. This article has 16 citations.

9. (amategarcia2023anovelmutation pages 8-9): Guillermo Amate-García, María Juliana Ballesta-Martínez, Pablo Serrano-Lorenzo, Rocío Garrido-Moraga, Adrián González-Quintana, Alberto Blázquez, Juan C. Rubio, Inés García-Consuegra, Joaquín Arenas, Cristina Ugalde, María Morán, Encarnación Guillén-Navarro, and Miguel A. Martín. A novel mutation associated with neonatal lethal cardiomyopathy leads to an alternative transcript expression in the x-linked complex i ndufb11 gene. International Journal of Molecular Sciences, 24:1743, Jan 2023. URL: https://doi.org/10.3390/ijms24021743, doi:10.3390/ijms24021743. This article has 16 citations.

10. (amategarcia2023anovelmutation pages 1-2): Guillermo Amate-García, María Juliana Ballesta-Martínez, Pablo Serrano-Lorenzo, Rocío Garrido-Moraga, Adrián González-Quintana, Alberto Blázquez, Juan C. Rubio, Inés García-Consuegra, Joaquín Arenas, Cristina Ugalde, María Morán, Encarnación Guillén-Navarro, and Miguel A. Martín. A novel mutation associated with neonatal lethal cardiomyopathy leads to an alternative transcript expression in the x-linked complex i ndufb11 gene. International Journal of Molecular Sciences, 24:1743, Jan 2023. URL: https://doi.org/10.3390/ijms24021743, doi:10.3390/ijms24021743. This article has 16 citations.

11. (amategarcia2023anovelmutation pages 9-11): Guillermo Amate-García, María Juliana Ballesta-Martínez, Pablo Serrano-Lorenzo, Rocío Garrido-Moraga, Adrián González-Quintana, Alberto Blázquez, Juan C. Rubio, Inés García-Consuegra, Joaquín Arenas, Cristina Ugalde, María Morán, Encarnación Guillén-Navarro, and Miguel A. Martín. A novel mutation associated with neonatal lethal cardiomyopathy leads to an alternative transcript expression in the x-linked complex i ndufb11 gene. International Journal of Molecular Sciences, 24:1743, Jan 2023. URL: https://doi.org/10.3390/ijms24021743, doi:10.3390/ijms24021743. This article has 16 citations.

## Artifacts

- [Edison artifact artifact-00](Histiocytoid_Cardiomyopathy-deep-research-falcon_artifacts/artifact-00.md)