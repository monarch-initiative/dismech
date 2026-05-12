---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-05-12T14:04:32.112266'
end_time: '2026-05-12T14:20:19.317651'
duration_seconds: 947.21
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Achromatopsia
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
citation_count: 38
artifact_count: 3
artifacts:
- filename: artifact-00.md
  path: Achromatopsia-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Achromatopsia-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
- filename: artifact-02.md
  path: Achromatopsia-deep-research-falcon_artifacts/artifact-02.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-02
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Achromatopsia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Achromatopsia** covering all of the
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
- **Disease Name:** Achromatopsia
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Achromatopsia** covering all of the
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


# Achromatopsia (ACHM) — Comprehensive Disease Characteristics Report (Mendelian)

## Executive summary (current understanding; 2023–2024 emphasis)
Achromatopsia (ACHM) is a rare congenital cone photoreceptor disorder (cone dysfunction syndrome) with onset at birth/early infancy and a characteristic triad of markedly reduced visual acuity, photophobia/photoaversion, and absent/markedly impaired color discrimination, often accompanied by infantile nystagmus. It is most commonly autosomal recessive and caused by biallelic loss-of-function variants in cone phototransduction genes—especially **CNGA3** and **CNGB3**—with additional rarer causes including **GNAT2, PDE6C, PDE6H,** and **ATF6**. The best-supported disease mechanism is failure of cone phototransduction/cGMP-gated ion channel signaling (CNGA3/CNGB3/PDE6*/GNAT2) and, for ATF6-ACHM, a developmental cone deficit linked to ER/UPR biology. Clinical management today is largely supportive (filters, low-vision rehabilitation), but multiple **AAV subretinal gene-replacement trials** are in late phase I/II stages for CNGA3- and CNGB3-ACHM, with early signals of safety and functional benefit in subsets of participants.

---

## 1. Disease information

### 1.1 Concise overview
- **Definition:** Andersen et al. (2023) describe ACHM as “**a rare congenital condition with cone photoreceptor dysfunction causing color blindness, reduced vision, nystagmus and photophobia**” (andersen2023geneticandclinical pages 1-2). Baxter & Borchert (2024) similarly note it is an autosomal recessive cone dysfunction syndrome presenting at birth/early infancy with poor visual acuity, nystagmus, photophobia, and loss of color vision (baxter2024genetherapyfor pages 1-2).
- **Synonyms / alternative names:** “**rod monochromacy**” and “**total color blindness**” are used as alternative names/descriptors (andersen2023geneticandclinical pages 1-2, michalakis2022achromatopsiageneticsand pages 1-2).
- **Evidence type:** The information in this report is derived from **aggregated disease-level resources** (reviews), plus **patient cohort natural history/quality-of-life studies** and **ClinicalTrials.gov trial records** (baxter2024genetherapyfor pages 1-2, andersen2023geneticandclinical pages 1-2, chan2023morphologicalandfunctional pages 1-2, NCT03001310 chunk 1).

### 1.2 Key identifiers (available in retrieved evidence)
- **MONDO:** OpenTargets maps “achromatopsia” to **MONDO_0018852** (OpenTargets Search: Achromatopsia).

**Note (identifier coverage limitation):** OMIM/Orphanet/ICD-10/ICD-11/MeSH identifiers were not retrieved in the available evidence chunks in this run; they should be added from OMIM/Orphanet/ICD/MeSH primary sources in a follow-on extraction.

| Identifier system | ID/value | Notes | Source (include URL/publication year if present) |
|---|---|---|---|
| Disease name | Achromatopsia | Rare congenital cone photoreceptor disorder; commonly presents at birth or early infancy with poor visual acuity, nystagmus, photophobia, and loss of color vision; autosomal recessive | Baxter & Borchert 2024, Int J Mol Sci, https://doi.org/10.3390/ijms25179739 (2024) (baxter2024genetherapyfor pages 1-2) |
| MONDO | MONDO:0018852 | OpenTargets lists achromatopsia under MONDO_0018852 | OpenTargets disease-target association context (OpenTargets Search: Achromatopsia) |
| Synonym | Rod monochromacy | Explicitly listed as an alternative name for achromatopsia | Andersen et al. 2023, Genes, https://doi.org/10.3390/genes14030690 (2023); Michalakis et al. 2022, Mol Diagn Ther, https://doi.org/10.1007/s40291-021-00565-z (2022) (andersen2023geneticandclinical pages 1-2, michalakis2022achromatopsiageneticsand pages 1-2) |
| Synonym | Total color blindness | Used as an alternative disease name/descriptor | Michalakis et al. 2022, Mol Diagn Ther, https://doi.org/10.1007/s40291-021-00565-z (2022) (michalakis2022achromatopsiageneticsand pages 1-2) |
| Inheritance | Autosomal recessive | Consistently reported across reviews and clinical studies | Baxter & Borchert 2024, https://doi.org/10.3390/ijms25179739 (2024); Michalakis et al. 2022, https://doi.org/10.1007/s40291-021-00565-z (2022) (baxter2024genetherapyfor pages 1-2, michalakis2022achromatopsiageneticsand pages 1-2) |
| Prevalence estimate | ~1 in 30,000 | Commonly cited point estimate | Baxter & Borchert 2024, https://doi.org/10.3390/ijms25179739 (2024); Michalakis et al. 2022, https://doi.org/10.1007/s40291-021-00565-z (2022) (baxter2024genetherapyfor pages 1-2, michalakis2022achromatopsiageneticsand pages 1-2) |
| Prevalence estimate | 1 in 30,000–50,000 | Range reported in natural-history/clinical review sources | Andersen et al. 2023, https://doi.org/10.3390/genes14030690 (2023); Asensio-Sánchez 2020 (andersen2023geneticandclinical pages 1-2, asensiosanchez2020genetherapyfor pages 1-2) |
| Major causal genes | CNGA3; CNGB3 | Together account for up to ~90% of cases in recent reviews | Baxter & Borchert 2024, https://doi.org/10.3390/ijms25179739 (2024); Michalakis et al. 2022, https://doi.org/10.1007/s40291-021-00565-z (2022) (baxter2024genetherapyfor pages 1-2, michalakis2022achromatopsiageneticsand pages 1-2) |
| Other established causal genes | GNAT2; PDE6C; PDE6H; ATF6 | Recurrently listed as rarer achromatopsia genes | Baxter & Borchert 2024, https://doi.org/10.3390/ijms25179739 (2024); Michalakis et al. 2022, https://doi.org/10.1007/s40291-021-00565-z (2022) (baxter2024genetherapyfor pages 1-2, michalakis2022achromatopsiageneticsand pages 1-2) |
| OpenTargets associated targets | CNGA3; CNGB3; PDE6C; GNAT2; ATF6; PDE6H | Disease-target evidence also lists OPN1MW, OPN1LW, and CABP4, but the core Mendelian achromatopsia genes in retrieved review/clinical sources are CNGA3, CNGB3, GNAT2, PDE6C, PDE6H, and ATF6 | OpenTargets disease-target association context; corroborated by recent reviews (OpenTargets Search: Achromatopsia, baxter2024genetherapyfor pages 1-2, michalakis2022achromatopsiageneticsand pages 1-2) |


*Table: This table summarizes key disease identifiers, synonyms, inheritance, prevalence, and causal genes for achromatopsia using only retrieved evidence. It is useful as a compact normalization reference for a disease knowledge base entry.*

---

## 2. Etiology

### 2.1 Disease causal factors
- **Primary cause:** Mendelian, typically **autosomal recessive** inherited retinal disease due to biallelic pathogenic variants affecting cone function (baxter2024genetherapyfor pages 1-2, michalakis2022achromatopsiageneticsand pages 1-2).
- **Core causal genes (well-established):** CNGA3, CNGB3, GNAT2, PDE6C, PDE6H, ATF6 (baxter2024genetherapyfor pages 1-2, michalakis2022achromatopsiageneticsand pages 1-2).

### 2.2 Genetic risk factors (causal variants)
- **CNGA3/CNGB3 predominate:** Baxter & Borchert (2024) state: “**Up to 90% of achromatopsia patients harbour mutations in CNGA3 or CNB3**” (CNGB3) (baxter2024genetherapyfor pages 1-2). Michalakis et al. (2022) and Moussawi et al. (2021) also place the majority of cases in these genes (michalakis2022achromatopsiageneticsand pages 1-2, moussawi2021genetherapyin pages 1-3).
- **Relative contributions (approximate; older synthesis):** Asensio-Sánchez (2020) reports CNGB3 ≈50% and CNGA3 ≈25% of autosomal recessive ACHM and lower proportions for GNAT2/PDE6C/PDE6H/ATF6 (asensiosanchez2020genetherapyfor pages 1-2, asensiosanchez2020genetherapyfor pages 7-10). These proportions should be treated as approximate and cohort-dependent.

### 2.3 Environmental risk/protective factors
No specific environmental exposures or protective factors are established as causal for **congenital** achromatopsia in the retrieved evidence; ACHM is primarily genetic (baxter2024genetherapyfor pages 1-2, michalakis2022achromatopsiageneticsand pages 1-2).

### 2.4 Gene–environment interactions
No gene–environment interaction evidence specific to ACHM was present in the retrieved sources.

| Gene (HGNC symbol) | Protein/function in cone | Pathway step (phototransduction/CNG/UPR) | Typical inheritance | Relative contribution/proportion if stated in evidence | Notes on phenotype (complete vs incomplete; progression) | Key sources (with URL/year) |
|---|---|---|---|---|---|---|
| **CNGA3** | Alpha subunit of the cone cyclic nucleotide-gated (CNG) channel; part of the final step converting cGMP changes into cone electrical responses (baxter2024genetherapyfor pages 1-2, baxter2024genetherapyfor pages 2-3, gerhardt2023biologypathobiologyand pages 1-2) | **CNG / cone phototransduction** | Autosomal recessive (baxter2024genetherapyfor pages 1-2, michalakis2022achromatopsiageneticsand pages 1-2) | Together with **CNGB3**, accounts for **up to ~90%** of ACHM; older review gives CNGA3 alone **~25%** (baxter2024genetherapyfor pages 1-2, michalakis2022achromatopsiageneticsand pages 1-2, asensiosanchez2020genetherapyfor pages 1-2) | Can cause complete or incomplete ACHM; incomplete forms reported particularly with some missense variants in CNGA3; no strong genotype-phenotype correlation overall; progression less commonly documented than for CNGB3/PDE6C in Danish cohort (moussawi2021genetherapyin pages 1-3, andersen2023geneticandclinical pages 1-2, baxter2024genetherapyfor pages 1-2, andersen2023geneticandclinical pages 7-9) | Baxter & Borchert 2024, https://doi.org/10.3390/ijms25179739 (2024); Michalakis et al. 2022, https://doi.org/10.1007/s40291-021-00565-z (2022); Gerhardt et al. 2023, https://doi.org/10.3390/biomedicines11020269 (2023) (baxter2024genetherapyfor pages 1-2, michalakis2022achromatopsiageneticsand pages 1-2, gerhardt2023biologypathobiologyand pages 2-5) |
| **CNGB3** | Beta subunit of the cone CNG channel; required with CNGA3 for functional cone CNG channel assembly and normal cone responses (baxter2024genetherapyfor pages 1-2, michalakis2022achromatopsiageneticsand pages 1-2, brotherton2024molecularmechanismsgoverning pages 3-5) | **CNG / cone phototransduction** | Autosomal recessive (baxter2024genetherapyfor pages 1-2, michalakis2022achromatopsiageneticsand pages 1-2) | Together with **CNGA3**, **up to ~90%** of ACHM; older review gives CNGB3 alone **~50%** of autosomal recessive ACHM (baxter2024genetherapyfor pages 1-2, michalakis2022achromatopsiageneticsand pages 1-2, asensiosanchez2020genetherapyfor pages 7-10) | Often associated with **complete achromatopsia** in review evidence; progressive BCVA deterioration attributable to ACHM was observed in some CNGB3 patients in long-term Danish follow-up (moussawi2021genetherapyin pages 1-3, andersen2023geneticandclinical pages 1-2, andersen2023geneticandclinical pages 7-9) | Baxter & Borchert 2024, https://doi.org/10.3390/ijms25179739 (2024); Michalakis et al. 2022, https://doi.org/10.1007/s40291-021-00565-z (2022); Asensio-Sánchez 2020 (baxter2024genetherapyfor pages 1-2, michalakis2022achromatopsiageneticsand pages 1-2, asensiosanchez2020genetherapyfor pages 7-10) |
| **GNAT2** | Cone transducin alpha subunit; couples activated cone opsin to PDE activation in phototransduction (baxter2024genetherapyfor pages 1-2, yang2024dyschromatopsiaacomprehensive pages 4-5, baxter2024genetherapyfor pages 2-3) | **Phototransduction** | Autosomal recessive (disease-level ACHM inheritance) (baxter2024genetherapyfor pages 1-2, michalakis2022achromatopsiageneticsand pages 1-2) | Rare; older review states **<2%** (asensiosanchez2020genetherapyfor pages 1-2) | Missense GNAT2 variants have been associated with **incomplete achromatopsia** and relative preservation of cone structure/function in some reports; Danish cohort suggested myopia may be more frequent with GNAT2 and no BCVA deterioration was reported in that cohort subset (moussawi2021genetherapyin pages 1-3, andersen2023geneticandclinical pages 7-9, yang2024dyschromatopsiaacomprehensive pages 4-5) | Baxter & Borchert 2024, https://doi.org/10.3390/ijms25179739 (2024); Yang et al. 2024, https://doi.org/10.3389/fnins.2024.1265630 (2024); Asensio-Sánchez 2020 (baxter2024genetherapyfor pages 1-2, yang2024dyschromatopsiaacomprehensive pages 4-5, asensiosanchez2020genetherapyfor pages 1-2) |
| **PDE6C** | Cone phosphodiesterase catalytic subunit; hydrolyzes cGMP in response to transducin activation (baxter2024genetherapyfor pages 1-2, yang2024dyschromatopsiaacomprehensive pages 6-8, baxter2024genetherapyfor pages 2-3) | **Phototransduction / cGMP metabolism** | Autosomal recessive (disease-level ACHM inheritance) (baxter2024genetherapyfor pages 1-2, michalakis2022achromatopsiageneticsand pages 1-2) | Rare; older review states **<2%** (asensiosanchez2020genetherapyfor pages 1-2) | Missense PDE6C variants can be associated with **incomplete ACHM** in review evidence, but PDE6C is also linked to more progressive cone disease in some reports; Danish cohort found progression attributable to ACHM in PDE6C and more frequent myopia/severe myopia (moussawi2021genetherapyin pages 1-3, andersen2023geneticandclinical pages 1-2, andersen2023geneticandclinical pages 7-9, yang2024dyschromatopsiaacomprehensive pages 4-5) | Baxter & Borchert 2024, https://doi.org/10.3390/ijms25179739 (2024); Yang et al. 2024, https://doi.org/10.3389/fnins.2024.1265630 (2024); Nouri et al. 2024, https://doi.org/10.1186/s12920-024-01942-3 (2024) (baxter2024genetherapyfor pages 1-2, yang2024dyschromatopsiaacomprehensive pages 6-8) |
| **PDE6H** | Cone phosphodiesterase gamma/inhibitory subunit; regulates cone PDE activity and therefore cGMP levels (baxter2024genetherapyfor pages 1-2, yang2024dyschromatopsiaacomprehensive pages 6-8, yang2024dyschromatopsiaacomprehensive pages 4-5) | **Phototransduction / cGMP metabolism** | Autosomal recessive (disease-level ACHM inheritance) (baxter2024genetherapyfor pages 1-2, michalakis2022achromatopsiageneticsand pages 1-2) | Very rare; older review states **<1%** (asensiosanchez2020genetherapyfor pages 1-2) | Missense PDE6H variants have been associated with **incomplete achromatopsia** in review evidence; Danish cohort found no BCVA deterioration in PDE6H subset but a high proportion with myopia/severe myopia (moussawi2021genetherapyin pages 1-3, andersen2023geneticandclinical pages 7-9, yang2024dyschromatopsiaacomprehensive pages 6-8) | Baxter & Borchert 2024, https://doi.org/10.3390/ijms25179739 (2024); Yang et al. 2024, https://doi.org/10.3389/fnins.2024.1265630 (2024); Asensio-Sánchez 2020 (baxter2024genetherapyfor pages 1-2, yang2024dyschromatopsiaacomprehensive pages 6-8, asensiosanchez2020genetherapyfor pages 1-2) |
| **ATF6** | Activating transcription factor 6; ER membrane transcription factor regulating unfolded protein response and essential for human cone photoreceptor development (michalakis2022achromatopsiageneticsand pages 1-2, yang2024dyschromatopsiaacomprehensive pages 6-8) | **UPR / ER homeostasis / cone development** | Autosomal recessive (disease-level ACHM inheritance) (baxter2024genetherapyfor pages 1-2, michalakis2022achromatopsiageneticsand pages 1-2) | Rare; older review states **~1–2%** (asensiosanchez2020genetherapyfor pages 1-2) | Mechanistically distinct from phototransduction genes; associated with developmental cone defects and foveal hypoplasia/absence of cone structures rather than only signaling failure; may provide fewer residual cone targets for classic gene replacement; pharmacologic ATF6 activation has shown rescue of cone growth/gene expression in patient organoids (yang2024dyschromatopsiaacomprehensive pages 6-8, yang2024dyschromatopsiaacomprehensive pages 4-5) | Kroeger et al. 2021, https://doi.org/10.1073/pnas.2103196118 (2021); Michalakis et al. 2022, https://doi.org/10.1007/s40291-021-00565-z (2022); Yang et al. 2024, https://doi.org/10.3389/fnins.2024.1265630 (2024) (michalakis2022achromatopsiageneticsand pages 1-2, yang2024dyschromatopsiaacomprehensive pages 6-8) |


*Table: This table summarizes the established achromatopsia genes, their functional roles in cone biology, and evidence-based phenotype notes. It is useful for linking genotype to mechanism, inheritance, and expected clinical presentation.*

---

## 3. Phenotypes (with ontology suggestions)

### 3.1 Core phenotype spectrum
Across reviews and cohort studies, ACHM is consistently characterized by:
- **Reduced visual acuity** (HPO suggestion: **HP:0007663 Decreased visual acuity**). Andersen et al. report VA “around **20/200**” in typical cases (andersen2023geneticandclinical pages 1-2), and Baxter & Borchert note similar typical VA and that incomplete forms can have better acuity (20/40–20/120) (baxter2024genetherapyfor pages 1-2).
- **Color vision loss** (HPO: **HP:0000551 Abnormal color vision**; for complete ACHM, **HP:0000618 Achromatopsia**). In a Danish cohort, “**49**” of 57 tested had complete color blindness and “**eight** had residual color vision” (andersen2023geneticandclinical pages 5-7).
- **Photophobia/photoaversion** (HPO: **HP:0000613 Photophobia**). Chan et al. emphasize: “**photoaversion has been described to be one of the more debilitating symptoms of achromatopsia**” (chan2023morphologicalandfunctional pages 1-2).
- **Infantile/childhood nystagmus** (HPO: **HP:0000639 Nystagmus**). In the Danish cohort, “**Most patients (89%, n = 72) had a history of childhood nystagmus**” (andersen2023geneticandclinical pages 5-7). Chan et al. report nystagmus in 88.5% among 61 patients (chan2023morphologicalandfunctional pages 4-6).
- **Refractive error (myopia/hyperopia)** (HPO: **HP:0000545 Myopia**, **HP:0000540 Hyperopia**). In Andersen et al., myopia was more frequent in GNAT2/PDE6C/PDE6H subsets (75–80%) (andersen2023geneticandclinical pages 7-9).

### 3.2 Anatomical structures affected
- **Primary organ/tissue:** Retina, especially macula/fovea with **cone photoreceptors**.
  - UBERON suggestions: **retina (UBERON:0000966)**; **macula lutea (UBERON:0001891)**; **fovea centralis (UBERON:0001866)**.
  - Cell Ontology suggestions: **retinal cone photoreceptor cell (CL:0000210)**.

### 3.3 Natural history / temporal development
- **Onset:** At birth or early infancy (baxter2024genetherapyfor pages 1-2, michalakis2022achromatopsiageneticsand pages 1-2).
- **Course:** Predominantly stationary with respect to visual acuity in many cohorts.
  - Chan et al. (2023) state: “**Visual acuity was stable… over a time of observation from 2008 to 2021**” (chan2023morphologicalandfunctional pages 1-2).
  - Andersen et al. report “**a median follow-up of 22 years** (…range 1–65 years)” and that the first and last VA were within ±0.2 logMAR in “**88% (n = 51)**” (andersen2023geneticandclinical pages 5-7).
  - Progressive BCVA deterioration attributable to ACHM was reported in “**three of 58 patients**” in Andersen et al. (andersen2023geneticandclinical pages 1-2, andersen2023geneticandclinical pages 7-9).

---

## 4. Genetic / molecular information (knowledge base–ready)

### 4.1 Causal genes
Established ACHM genes in the retrieved evidence: **CNGA3, CNGB3, GNAT2, PDE6C, PDE6H, ATF6** (baxter2024genetherapyfor pages 1-2, michalakis2022achromatopsiageneticsand pages 1-2). OpenTargets also links ACHM to these targets and provides supporting PubMed ID lists (e.g., CNGA3/CNGB3 evidence) and the MONDO mapping (OpenTargets Search: Achromatopsia).

### 4.2 Pathogenic variant characteristics
The retrieved evidence primarily provides gene-level rather than variant-level detail. Variant class patterns inferred from the evidence include:
- **Loss-of-function variants** are common drivers (recessive) in CNGA3/CNGB3-related ACHM (gong2024infantilenystagmussyndrome—associated pages 12-13).
- Some reviews note incomplete ACHM may be associated with specific **missense** changes in GNAT2/CNGA3/PDE6C/PDE6H (moussawi2021genetherapyin pages 1-3).

**Note (variant-level limitation):** ClinVar/HGMD/gnomAD allele frequencies, ACMG classifications, and recurrent founder variants were not retrieved in the evidence chunks and thus cannot be reliably populated here.

---

## 5. Environmental information
No infectious, toxic, occupational, or lifestyle exposures were identified as causal contributors for congenital ACHM in the retrieved evidence.

---

## 6. Mechanism / pathophysiology

### 6.1 Cone phototransduction / cGMP / CNG channel failure (CNGA3, CNGB3, GNAT2, PDE6C, PDE6H)
Mechanistically, ACHM (for the phototransduction-gene forms) arises from disruption of the cone phototransduction cascade and/or the CNG channel that converts cGMP signaling into an electrical response:
- Yang et al. (2024) explicitly summarize the cascade: “**Activated PDE begins to hydrolyze cGMP efficiently. As the cGMP concentration decreases, the CNG channel closed**” (yang2024dyschromatopsiaacomprehensive pages 6-8). They further describe a PDE6H mechanism: “**cGMP gated channels are permanently closed**” in a way “**similar to permanent light stimulation**” (yang2024dyschromatopsiaacomprehensive pages 6-8).
- Michalakis et al. (2022) describe the core dark/light physiology: in darkness high cGMP keeps CNG channels open producing Na+/Ca2+ current and depolarization; in light, opsin→transducin→PDE reduces cGMP, closes channels, and hyperpolarizes the cone (michalakis2022achromatopsiageneticsand pages 1-2).
- Downstream consequences include absent cone-mediated ERG components with preserved rod function (diagnostic hallmark) and cone degeneration; Michalakis et al. note early cone degeneration features including **cGMP accumulation** (michalakis2022achromatopsiageneticsand pages 4-5).

**GO term suggestions (biological process):** phototransduction (GO:0007602), cyclic nucleotide-mediated signaling (GO:0019935), cGMP metabolic process (GO:0046068), ion transmembrane transport (GO:0034220).

### 6.2 ATF6-related achromatopsia (developmental / ER/UPR biology)
ATF6-associated ACHM is mechanistically distinct, involving ER homeostasis/UPR signaling and cone development:
- Yang et al. (2024) state: “**ATF6 ... plays a key role in unfolded protein response (UPR) and endoplasmic reticulum homeostasis**” (yang2024dyschromatopsiaacomprehensive pages 6-8).
- Michalakis et al. (2022) likewise describe ATF6 as an ER-localized transcription factor capable of activating the unfolded protein response (michalakis2022achromatopsiageneticsand pages 1-2).

**Therapeutic implication (conceptual):** Phototransduction-gene ACHM is amenable to gene supplementation (recessive loss-of-function), whereas ATF6-associated disease may have fewer intact cone structures to target and may require pathway modulation (yang2024dyschromatopsiaacomprehensive pages 4-5).

---

## 7. Anatomical structures affected (ontology-ready)
- **Primary:** retina (macula/fovea) and cone photoreceptor system.
- **Subcellular / molecular compartments (relevant):** cone outer segment, cGMP signaling microdomain, CNG channels in outer segment membrane; ER/UPR machinery for ATF6.
  - GO Cellular Component suggestions: photoreceptor outer segment (GO:0001750), plasma membrane (GO:0005886), endoplasmic reticulum membrane (GO:0005789).

---

## 8. Temporal development
- **Typical onset:** congenital/infantile (baxter2024genetherapyfor pages 1-2, michalakis2022achromatopsiageneticsand pages 1-2).
- **Progression:** predominantly stable VA over many years for many patients, but with documented minority progression in long follow-up (andersen2023geneticandclinical pages 5-7, andersen2023geneticandclinical pages 7-9).

---

## 9. Inheritance and population

### 9.1 Epidemiology
- **Prevalence:** commonly cited as ~**1 in 30,000** (baxter2024genetherapyfor pages 1-2, michalakis2022achromatopsiageneticsand pages 1-2), and also reported as a range **1 in 30,000–50,000** (andersen2023geneticandclinical pages 1-2, asensiosanchez2020genetherapyfor pages 1-2).

### 9.2 Inheritance
- Typically **autosomal recessive** (baxter2024genetherapyfor pages 1-2, michalakis2022achromatopsiageneticsand pages 1-2).

**Note (population genetics limitation):** No carrier frequencies, founder variants, or geographic variant distributions were retrievable from the evidence in this run.

---

## 10. Diagnostics

### 10.1 Clinical and electrophysiology
- Classic diagnostic confirmation includes demonstration of absent cone function: Andersen et al. refer to “**demonstration of a lack of cone function by electroretinography**” (andersen2023geneticandclinical pages 1-2). Baxter & Borchert note ERGs typically show normal rod/scotopic responses with absence of cone-mediated photopic components (baxter2024genetherapyfor pages 1-2).

### 10.2 Imaging (OCT/FAF) and functional endpoints
- **Fundus autofluorescence (FAF):** Baxter & Borchert classify 4 phenotypes (normal; central increased; central reduced; central decreased with hyperautofluorescent ring) (baxter2024genetherapyfor pages 1-2).
- **OCT:** Baxter & Borchert classify 5 OCT patterns (continuous/disrupted/absent ellipsoid layer; hyporeflective zone; outer retinal atrophy with RPE loss) and note foveal hypoplasia is common (baxter2024genetherapyfor pages 1-2).
- **Microperimetry as structure–function endpoint (2024):** In adolescents, OCT staging correlated with microperimetry sensitivity (central foveal and perifoveal rings) with p-values **0.0286**, **0.0008**, **0.0014**; in contrast, OCT staging did **not** correlate with VA or contrast sensitivity (cosmo2024microperimetrysensitivitycorrelates pages 1-2, cosmo2024microperimetrysensitivitycorrelates pages 4-6).

### 10.3 Recommended testing approach (evidence-based synthesis)
A practical diagnostic workflow supported by the retrieved sources is:
1) Clinical phenotype (infantile onset, photophobia, nystagmus, color vision deficit), 2) ERG documenting absent cone responses with preserved rod responses, 3) OCT/FAF characterization of foveal/outer retinal structure, 4) genetic testing to identify causal gene(s) and determine eligibility for gene therapy trials (baxter2024genetherapyfor pages 1-2, andersen2023geneticandclinical pages 1-2, gong2024infantilenystagmussyndrome—associated pages 12-13).

**Differential diagnosis (limited in retrieved evidence):** The retrieved evidence does not provide a systematic differential diagnosis list; however, the context of inherited retinal diseases presenting with infantile nystagmus includes multiple entities (review context) (gong2024infantilenystagmussyndrome—associated pages 12-13). A dedicated differential diagnosis extraction would require additional sources.

---

## 11. Outcomes / prognosis
- **Visual acuity stability:** Chan et al. report “**Visual acuity was stable…**” in their cohort over 2008–2021 (chan2023morphologicalandfunctional pages 1-2). Andersen et al. report long-term stability in most patients (±0.2 logMAR in **88%**) and rare ACHM-attributable deterioration (**3/58**) (andersen2023geneticandclinical pages 5-7, andersen2023geneticandclinical pages 7-9).
- **Functional and QoL impact:** Photoaversion is described as debilitating (chan2023morphologicalandfunctional pages 1-2). In Chan et al., legal disability ratings ranged widely and **27.9%** were rated 100% (chan2023morphologicalandfunctional pages 6-8).

---

## 12. Treatment

### 12.1 Supportive/rehabilitative (current real-world implementation)
- Optical aids and filters are widely used; Chan et al. report: “**Edge filter glasses were the most used optical aids, while enlarged reading glasses were the most used low vision aids**” (chan2023morphologicalandfunctional pages 1-2).
- In an extended aid inventory (subset), common devices included reading glasses (56.3%), magnifying glasses (55.2%), smartphones (39.1%), tablets (37.9%), monoculars (36.8%), and CCTV (31%) (chan2023morphologicalandfunctional pages 6-8).

**MAXO suggestions:** low vision rehabilitation (MAXO:0000787), prescription of optical filters (filter-lens intervention; MAXO term may need confirmation), assistive device use.

### 12.2 Advanced therapeutics: gene therapy (2023–2024 status)
- Baxter & Borchert (2024) emphasize “**There is no FDA-approved treatment for achromatopsia**” and note “**five gene therapy clinical trials registered**” (phase I/II) for CNGA3/CNGB3 (baxter2024genetherapyfor pages 1-2).

**Key trials and implementation details** (ClinicalTrials.gov plus 2024 expert synthesis):
- **CNGA3 AAV subretinal trials:** NCT02610582 and NCT02935517 (NCT02610582 chunk 1, NCT02935517 chunk 1).
  - NCT02610582 includes subretinal administration and multiple functional endpoints including microperimetry and patient-reported outcomes (NCT02610582 chunk 1).
  - Gong & Hertle (2024) summarize a first CNGA3 trial: treatment “**well tolerated, with no serious adverse events**” and visual acuity/contrast sensitivity improvements persisting “**for at least three years**” (gong2024infantilenystagmussyndrome—associated pages 12-13).
- **CNGB3 AAV subretinal trials:** NCT03001310 and NCT02599922 (NCT03001310 chunk 1, gong2024infantilenystagmussyndrome—associated pages 12-13).
  - NCT03001310 is a completed phase I/II dose-escalation trial using **AAV2/8-hCARp.hCNGB3** with BCVA and retinal sensitivity endpoints at 24 weeks and QoL EQ-VAS measures (NCT03001310 chunk 1).
  - Gong & Hertle (2024) report that in one CNGB3 program, “**rAAV2tYF-PR1.7-hCNGB3 treatment has improved photosensitivity in some patients**” (gong2024infantilenystagmussyndrome—associated pages 12-13).

| NCT ID | Gene | Sponsor | Vector / promoter | Route | Phase | Age eligibility | Enrollment | Status | Primary endpoint(s) | Key secondary endpoints | Reported outcomes / development notes |
|---|---|---|---|---|---|---|---:|---|---|---|---|
| NCT02610582 | CNGA3 | STZ eyetrial | rAAV.hCNGA3; AAV8.hCNGA3 reported in review; promoter not specified in ClinicalTrials.gov chunk | Subretinal injection after pars plana vitrectomy | Phase I/II | 6–12 years and >=18 years; pediatric cohort C n=6 | 13 | Active, not recruiting | Safety at 12 months; adverse events/abnormal labs related to treatment (NCT02610582 chunk 2, NCT02610582 chunk 1) | Contrast sensitivity (Pelli Robson) at 6 months; BCVA (ETDRS), microperimetry (MAIA), chromatic pupil campimetry, VFQ25/CVFQ, A3-PRO; broader efficacy measures of improved visual function (NCT02610582 chunk 2, NCT02610582 chunk 1) | Review reports 9 CNGA3-ACHM patients treated; well tolerated with no serious adverse events; increases in visual acuity and contrast sensitivity persisted for at least 3 years; phase IIb follow-up planned for second eye and children 6–12 years (gong2024infantilenystagmussyndrome—associated pages 12-13) |
| NCT02935517 | CNGA3 | Beacon Therapeutics | AGTC-402 / rAAV2tYF-PR1.7-hCNGA3 | Subretinal, one eye | Phase I/II | Adults >=18 years in groups 1–5; 6–17 years in group 3a; 4–8 years in groups 4a and 6 | 24 | Active, not recruiting | Safety: proportion with grade 3 or greater adverse events over 1 year (NCT02935517 chunk 1) | Change in visual acuity, light discomfort/light aversion, and color vision vs pretreatment over 1 year (NCT02935517 chunk 1) | Gong 2024 describes this as an open-label dose-escalation subretinal AAV2-variant trial using engineered cone opsin promoter; participants assigned to 4 dose groups in review summary; outcomes for CNGA3 arm described as less encouraging than CNGB3 in available review commentary (gong2024infantilenystagmussyndrome—associated pages 12-13, NCT02935517 chunk 1) |
| NCT02599922 | CNGB3 | Beacon Therapeutics | rAAV2tYF-PR1.7-hCNGB3 | Subretinal | Phase I/II | Not stated in retrieved ClinicalTrials.gov chunks; review describes adults and children across achromatopsia programs | 32 | Active, not recruiting | Not fully detailed in retrieved ClinicalTrials.gov chunks; review characterizes trial as phase I/II open-label dose-escalation (gong2024infantilenystagmussyndrome—associated pages 12-13) | Not fully detailed in retrieved ClinicalTrials.gov chunks; review notes visual-function secondary outcomes (gong2024infantilenystagmussyndrome—associated pages 12-13) | Gong 2024 reports sequential assignment to 4 dose groups and that rAAV2tYF-PR1.7-hCNGB3 improved photosensitivity in some patients (gong2024infantilenystagmussyndrome—associated pages 12-13) |
| NCT03758404 | CNGA3 | MeiraGTx UK II Ltd | AAV2/8-hG1.7p.coCNGA3 (review) | Not stated in retrieved ClinicalTrials.gov chunk; review groups these with similar subretinal phase I/II trials | Phase I/II | Adults and children (review) | 11 | Completed | Incidence of treatment-related adverse events at 6 months (review) (gong2024infantilenystagmussyndrome—associated pages 12-13) | Improvements in visual function (review) (gong2024infantilenystagmussyndrome—associated pages 12-13) | Gong 2024 describes this as similar to NCT03001310, evaluating AAV2/8-hG1.7p.coCNGA3 in adults and children (gong2024infantilenystagmussyndrome—associated pages 12-13) |
| NCT03001310 | CNGB3 | MeiraGTx UK II Ltd | AAV2/8-hCARp.hCNGB3 | Subretinal, single administration; low/intermediate/high dose escalation | Phase I/II | >=3 years | 23 | Completed | Composite safety over 6 weeks post administration, including serious ocular/non-ocular events possibly related to ATIMP (NCT03001310 chunk 1) | Week-24 change in BCVA (ETDRS), mean retinal sensitivity by static perimetry, and QoL (EQ-VAS) for children/adults (NCT03001310 chunk 1) | Gong 2024 also describes a similar phase I/II open-label dose-escalation trial in adults and children; primary outcome framed as treatment-related adverse events at 6 months and secondary outcomes as visual-function improvements (gong2024infantilenystagmussyndrome—associated pages 12-13, NCT03001310 chunk 1) |


*Table: This table summarizes the key human CNGA3- and CNGB3-targeted gene therapy trials for achromatopsia using only retrieved ClinicalTrials.gov records and the 2024 Gong review. It is useful for comparing sponsors, vectors, eligibility, endpoints, and the current state of clinical development.*

**Expert opinion / analysis (authoritative source):** Gong & Hertle (2024) frame molecular diagnosis as crucial for access to gene-based therapies and highlight that AAV-based subretinal gene therapy is actively being studied in CNGA3/CNGB3 ACHM with evolving outcome measures (gong2024infantilenystagmussyndrome—associated pages 12-13).

---

## 13. Prevention
- **Primary prevention:** Not applicable in the classic exposure-reduction sense because ACHM is congenital genetic.
- **Genetic counseling / family planning:** Most relevant prevention-like strategy is carrier testing and counseling in at-risk families (inferred from autosomal recessive inheritance; not detailed in retrieved text).
- **Secondary/tertiary:** Early diagnosis and early low-vision rehabilitation (filters/devices) to reduce disability impact (chan2023morphologicalandfunctional pages 1-2).

---

## 14. Other species / natural disease
The retrieved evidence describes naturally occurring large-animal ACHM models used translationally (dogs, sheep) and engineered models (mice), which serve as comparative biology for disease mechanisms and therapies (gerhardt2023biologypathobiologyand pages 10-12, asensiosanchez2020genetherapyfor pages 7-10).

---

## 15. Model organisms (key systems and translational use)

### 15.1 Models used
- **Mouse models:** Cnga3 knockout and other cone dysfunction models; rAAV-Cnga3 can restore cone responses and normalize cGMP (gerhardt2023biologypathobiologyand pages 10-12, michalakis2022achromatopsiageneticsand pages 4-5).
- **Dog (CNGB3-mutant):** Subretinal AAV5-CNGB3 improved cone function; strong age dependence (gerhardt2023biologypathobiologyand pages 10-12).
- **Sheep (Awassi, CNGA3):** Long-duration rescue after AAV-CNGA3 (≥6 years reported in review) (gerhardt2023biologypathobiologyand pages 10-12).

### 15.2 Key translational findings
- **Age-dependence / therapeutic window:** In CNGB3 dogs, “**best treatment results were achieved in 3-week-old-animals, whereas treatment was minimally effective in dogs 1 year of age and older**” (gerhardt2023biologypathobiologyand pages 10-12).
- **Durability:** In sheep, AAV-CNGA3 led to “**Significant long-term improvement… for at least 6 years**” (gerhardt2023biologypathobiologyand pages 10-12).

---

## Recent developments (2023–2024 highlights)
- **Natural history and stability:** Large retrospective cohorts (2023) provide long follow-up supporting largely stationary VA with rare progression (andersen2023geneticandclinical pages 5-7, andersen2023geneticandclinical pages 7-9).
- **Outcome measure refinement:** 2024 evidence suggests microperimetry may be a more sensitive structure–function endpoint than VA/contrast sensitivity for certain age groups (adolescents) (cosmo2024microperimetrysensitivitycorrelates pages 1-2, cosmo2024microperimetrysensitivitycorrelates pages 4-6).
- **Clinical gene therapy maturation:** Detailed trial designs and endpoints are now available publicly via ClinicalTrials.gov for multiple CNGA3/CNGB3 programs, and expert synthesis highlights multi-year persistence of functional gains in at least one CNGA3 study (NCT02610582 chunk 1, NCT02935517 chunk 1, NCT03001310 chunk 1, gong2024infantilenystagmussyndrome—associated pages 12-13).

---

## Data/statistics summary (from recent studies)
- **Prevalence:** ~1:30,000 or 1:30,000–1:50,000 (baxter2024genetherapyfor pages 1-2, andersen2023geneticandclinical pages 1-2).
- **VA stability:** 88% within ±0.2 logMAR over median 22-year follow-up in Danish cohort (andersen2023geneticandclinical pages 5-7).
- **ACHM-attributable progression:** 3/58 in Danish cohort (andersen2023geneticandclinical pages 7-9).
- **QoL/disability:** 27.9% rated 100% disability in one cohort subset (chan2023morphologicalandfunctional pages 6-8).

---

## Key evidence quotes (abstract-supported)
- ACHM definition: “**Achromatopsia is a rare congenital condition with cone photoreceptor dysfunction causing color blindness, reduced vision, nystagmus and photophobia**” (andersen2023geneticandclinical pages 1-2).
- Trial landscape: “**There is no FDA-approved treatment for achromatopsia; however… There are currently five gene therapy clinical trials registered…**” (baxter2024genetherapyfor pages 1-2).
- Microperimetry endpoint: OCT staging correlated with microperimetry sensitivity (p = 0.0286; 0.0008; 0.0014) and not with VA/CS (cosmo2024microperimetrysensitivitycorrelates pages 1-2).

---

## Limitations of this extraction (what is missing and why)
- **OMIM/Orphanet/ICD/MeSH identifiers** were not captured in retrieved evidence chunks.
- **Variant-level information** (ClinVar IDs, exact variant nomenclature, ACMG classes, population allele frequencies, carrier frequencies, founder variants) was not present in the retrieved sources.
- **Systematic differential diagnosis** and **formal clinical guidelines** were not included in retrieved evidence.

These components require additional targeted retrieval from OMIM/Orphanet/ClinVar/gnomAD/GeneReviews and guideline databases.


References

1. (andersen2023geneticandclinical pages 1-2): Mette Kjøbæk Gundestrup Andersen, Mette Bertelsen, Karen Grønskov, Susanne Kohl, and Line Kessel. Genetic and clinical characterization of danish achromatopsia patients. Genes, 14:690, Mar 2023. URL: https://doi.org/10.3390/genes14030690, doi:10.3390/genes14030690. This article has 19 citations.

2. (baxter2024genetherapyfor pages 1-2): Megan F. Baxter and Grace A. Borchert. Gene therapy for achromatopsia. International Journal of Molecular Sciences, 25:9739, Sep 2024. URL: https://doi.org/10.3390/ijms25179739, doi:10.3390/ijms25179739. This article has 17 citations.

3. (michalakis2022achromatopsiageneticsand pages 1-2): Stylianos Michalakis, Maximilian Gerhardt, Günther Rudolph, Siegfried Priglinger, and Claudia Priglinger. Achromatopsia: genetics and gene therapy. Molecular Diagnosis & Therapy, 26:51-59, Dec 2022. URL: https://doi.org/10.1007/s40291-021-00565-z, doi:10.1007/s40291-021-00565-z. This article has 74 citations and is from a peer-reviewed journal.

4. (chan2023morphologicalandfunctional pages 1-2): Caroline Chan, Berthold Seitz, and Barbara Käsmann-Kellner. Morphological and functional aspects and quality of life in patients with achromatopsia. Journal of Personalized Medicine, 13:1106, Jul 2023. URL: https://doi.org/10.3390/jpm13071106, doi:10.3390/jpm13071106. This article has 0 citations.

5. (NCT03001310 chunk 1):  Gene Therapy for Achromatopsia (CNGB3). MeiraGTx UK II Ltd. 2017. ClinicalTrials.gov Identifier: NCT03001310

6. (OpenTargets Search: Achromatopsia): Open Targets Query (Achromatopsia, 15 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

7. (asensiosanchez2020genetherapyfor pages 1-2): VM Asensio-Sánchez. Gene therapy for the treatment of achromatopsia: recent advances. Unknown journal, 2020.

8. (moussawi2021genetherapyin pages 1-3): Zeinab El Moussawi, Marguerita Boueiri, and Christiane Al-Haddad. Gene therapy in color vision deficiency: a review. International Ophthalmology, 41:1917-1927, Feb 2021. URL: https://doi.org/10.1007/s10792-021-01717-0, doi:10.1007/s10792-021-01717-0. This article has 42 citations and is from a peer-reviewed journal.

9. (asensiosanchez2020genetherapyfor pages 7-10): VM Asensio-Sánchez. Gene therapy for the treatment of achromatopsia: recent advances. Unknown journal, 2020.

10. (baxter2024genetherapyfor pages 2-3): Megan F. Baxter and Grace A. Borchert. Gene therapy for achromatopsia. International Journal of Molecular Sciences, 25:9739, Sep 2024. URL: https://doi.org/10.3390/ijms25179739, doi:10.3390/ijms25179739. This article has 17 citations.

11. (gerhardt2023biologypathobiologyand pages 1-2): Maximilian J. Gerhardt, Siegfried G. Priglinger, Martin Biel, and Stylianos Michalakis. Biology, pathobiology and gene therapy of cng channel-related retinopathies. Biomedicines, 11:269, Jan 2023. URL: https://doi.org/10.3390/biomedicines11020269, doi:10.3390/biomedicines11020269. This article has 20 citations.

12. (andersen2023geneticandclinical pages 7-9): Mette Kjøbæk Gundestrup Andersen, Mette Bertelsen, Karen Grønskov, Susanne Kohl, and Line Kessel. Genetic and clinical characterization of danish achromatopsia patients. Genes, 14:690, Mar 2023. URL: https://doi.org/10.3390/genes14030690, doi:10.3390/genes14030690. This article has 19 citations.

13. (gerhardt2023biologypathobiologyand pages 2-5): Maximilian J. Gerhardt, Siegfried G. Priglinger, Martin Biel, and Stylianos Michalakis. Biology, pathobiology and gene therapy of cng channel-related retinopathies. Biomedicines, 11:269, Jan 2023. URL: https://doi.org/10.3390/biomedicines11020269, doi:10.3390/biomedicines11020269. This article has 20 citations.

14. (brotherton2024molecularmechanismsgoverning pages 3-5): Chloe Brotherton and Roly Megaw. Molecular mechanisms governing sight loss in inherited cone disorders. Genes, 15:727, Jun 2024. URL: https://doi.org/10.3390/genes15060727, doi:10.3390/genes15060727. This article has 8 citations.

15. (yang2024dyschromatopsiaacomprehensive pages 4-5): Zihao Yang, Lin Yan, Wenliang Zhang, Jia Qi, Wenjing An, and Kai Yao. Dyschromatopsia: a comprehensive analysis of mechanisms and cutting-edge treatments for color vision deficiency. Frontiers in Neuroscience, Jan 2024. URL: https://doi.org/10.3389/fnins.2024.1265630, doi:10.3389/fnins.2024.1265630. This article has 26 citations and is from a peer-reviewed journal.

16. (yang2024dyschromatopsiaacomprehensive pages 6-8): Zihao Yang, Lin Yan, Wenliang Zhang, Jia Qi, Wenjing An, and Kai Yao. Dyschromatopsia: a comprehensive analysis of mechanisms and cutting-edge treatments for color vision deficiency. Frontiers in Neuroscience, Jan 2024. URL: https://doi.org/10.3389/fnins.2024.1265630, doi:10.3389/fnins.2024.1265630. This article has 26 citations and is from a peer-reviewed journal.

17. (andersen2023geneticandclinical pages 5-7): Mette Kjøbæk Gundestrup Andersen, Mette Bertelsen, Karen Grønskov, Susanne Kohl, and Line Kessel. Genetic and clinical characterization of danish achromatopsia patients. Genes, 14:690, Mar 2023. URL: https://doi.org/10.3390/genes14030690, doi:10.3390/genes14030690. This article has 19 citations.

18. (chan2023morphologicalandfunctional pages 4-6): Caroline Chan, Berthold Seitz, and Barbara Käsmann-Kellner. Morphological and functional aspects and quality of life in patients with achromatopsia. Journal of Personalized Medicine, 13:1106, Jul 2023. URL: https://doi.org/10.3390/jpm13071106, doi:10.3390/jpm13071106. This article has 0 citations.

19. (gong2024infantilenystagmussyndrome—associated pages 12-13): Xiaoming Gong and Richard W. Hertle. Infantile nystagmus syndrome—associated inherited retinal diseases: perspectives from gene therapy clinical trials. Life, 14:1356, Oct 2024. URL: https://doi.org/10.3390/life14111356, doi:10.3390/life14111356. This article has 2 citations.

20. (michalakis2022achromatopsiageneticsand pages 4-5): Stylianos Michalakis, Maximilian Gerhardt, Günther Rudolph, Siegfried Priglinger, and Claudia Priglinger. Achromatopsia: genetics and gene therapy. Molecular Diagnosis & Therapy, 26:51-59, Dec 2022. URL: https://doi.org/10.1007/s40291-021-00565-z, doi:10.1007/s40291-021-00565-z. This article has 74 citations and is from a peer-reviewed journal.

21. (cosmo2024microperimetrysensitivitycorrelates pages 1-2): Eleonora Cosmo, Elisabetta Pilotto, Enrica Convento, Federico Parolini, and Edoardo Midena. Microperimetry sensitivity correlates to structural macular changes in adolescents with achromatopsia unlike other visual function tests. Journal of Clinical Medicine, 13:5968, Oct 2024. URL: https://doi.org/10.3390/jcm13195968, doi:10.3390/jcm13195968. This article has 0 citations.

22. (cosmo2024microperimetrysensitivitycorrelates pages 4-6): Eleonora Cosmo, Elisabetta Pilotto, Enrica Convento, Federico Parolini, and Edoardo Midena. Microperimetry sensitivity correlates to structural macular changes in adolescents with achromatopsia unlike other visual function tests. Journal of Clinical Medicine, 13:5968, Oct 2024. URL: https://doi.org/10.3390/jcm13195968, doi:10.3390/jcm13195968. This article has 0 citations.

23. (chan2023morphologicalandfunctional pages 6-8): Caroline Chan, Berthold Seitz, and Barbara Käsmann-Kellner. Morphological and functional aspects and quality of life in patients with achromatopsia. Journal of Personalized Medicine, 13:1106, Jul 2023. URL: https://doi.org/10.3390/jpm13071106, doi:10.3390/jpm13071106. This article has 0 citations.

24. (NCT02610582 chunk 1):  Safety and Efficacy of rAAV.hCNGA3 Gene Therapy in Patients With CNGA3-linked Achromatopsia. STZ eyetrial. 2015. ClinicalTrials.gov Identifier: NCT02610582

25. (NCT02935517 chunk 1):  Safety and Efficacy Trial of AAV Gene Therapy in Patients With CNGA3 Achromatopsia (A Clarity Clinical Trial). Beacon Therapeutics. 2017. ClinicalTrials.gov Identifier: NCT02935517

26. (NCT02610582 chunk 2):  Safety and Efficacy of rAAV.hCNGA3 Gene Therapy in Patients With CNGA3-linked Achromatopsia. STZ eyetrial. 2015. ClinicalTrials.gov Identifier: NCT02610582

27. (gerhardt2023biologypathobiologyand pages 10-12): Maximilian J. Gerhardt, Siegfried G. Priglinger, Martin Biel, and Stylianos Michalakis. Biology, pathobiology and gene therapy of cng channel-related retinopathies. Biomedicines, 11:269, Jan 2023. URL: https://doi.org/10.3390/biomedicines11020269, doi:10.3390/biomedicines11020269. This article has 20 citations.

## Artifacts

- [Edison artifact artifact-00](Achromatopsia-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Achromatopsia-deep-research-falcon_artifacts/artifact-01.md)
- [Edison artifact artifact-02](Achromatopsia-deep-research-falcon_artifacts/artifact-02.md)