---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-13T14:14:09.772630'
end_time: '2026-06-13T14:24:05.777258'
duration_seconds: 596.0
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Gaucher Disease Due To Saposin C Deficiency
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 26
artifact_count: 2
artifact_sources:
  edison_answer_artifacts: 2
artifacts:
- filename: artifact-00.md
  path: Gaucher_Disease_Due_To_Saposin_C_Deficiency-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
- filename: artifact-01.md
  path: Gaucher_Disease_Due_To_Saposin_C_Deficiency-deep-research-falcon_artifacts/artifact-01.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-01
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Gaucher Disease Due To Saposin C Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Gaucher Disease Due To Saposin C Deficiency** covering all of the
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
- **Disease Name:** Gaucher Disease Due To Saposin C Deficiency
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Gaucher Disease Due To Saposin C Deficiency** covering all of the
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


# Gaucher Disease Due to Saposin C Deficiency (PSAP/SapC): Comprehensive Disease Characteristics Report

## Target disease
- **Disease name:** Gaucher disease due to saposin C deficiency (PSAP-related “atypical Gaucher disease”) (tamargo2012theroleof pages 1-2, motta2014gaucherdiseasedue pages 1-2)
- **Category:** Mendelian / lysosomal storage disease (autosomal recessive) (tamargo2012theroleof pages 1-2, motta2014gaucherdiseasedue pages 1-2)
- **MONDO ID:** Not identified in the retrieved full-text evidence set (tamargo2012theroleof pages 1-2, motta2014gaucherdiseasedue pages 1-2)

---

## 1. Disease Information

### 1.1 Concise overview (current understanding)
Gaucher disease due to saposin C deficiency is an ultra-rare lysosomal disorder in which biallelic pathogenic variants in **PSAP** (prosaposin) impair production/function of **saposin C (SapC)**, an essential activator/cofactor for lysosomal **glucocerebrosidase (GCase)**. This causes a Gaucher-like phenotype via impaired degradation of **glucosylceramide (GlcCer)** and related sphingolipids, and can clinically resemble non-neuronopathic (type 1-like) or neuronopathic (type 3-like) Gaucher disease—sometimes despite *normal in vitro* GCase activity assays (tamargo2012theroleof pages 1-2, rafi1993mutationalanalysisin pages 1-3, motta2014gaucherdiseasedue pages 1-2).

### 1.2 Key identifiers (as evidenced in retrieved literature)
| Disease/Concept | Identifier type | Identifier/value | Notes (inheritance, subtype, comments) | Source |
|---|---|---|---|---|
| Gaucher disease due to saposin C deficiency | MIM/OMIM disease ID | 610539 | Rare PSAP-related Gaucher-like disorder; autosomal recessive; can phenocopy type 1 or type 3 Gaucher disease; standard Orphanet/MONDO/MeSH/ICD identifiers were not found in the evidence (liaqat2022phenotypeexpansionfor pages 1-2, tamargo2012theroleof pages 1-2) | Genes 2022; Mol Genet Metab 2012 |
| Variant Gaucher disease due to saposin C deficiency | Synonym | variant Gaucher disease due to saposin C deficiency | Historical/alternative phrasing for PSAP saposin C deficiency causing Gaucher-like disease (rafi1993mutationalanalysisin pages 1-3, motta2014gaucherdiseasedue pages 1-2) | Somatic Cell Mol Genet 1993; Hum Mol Genet 2014 |
| Atypical Gaucher disease due to PSAP | Synonym | atypical Gaucher disease due to PSAP | Used for PSAP-associated Gaucher spectrum with phenotypic heterogeneity, including visceral and neurologic manifestations (liaqat2022phenotypeexpansionfor pages 5-7, liaqat2022phenotypeexpansionfor pages 1-2) | Genes 2022 |
| PSAP gene | MIM/OMIM gene ID | 176801 | Encodes prosaposin, precursor of saposins A-D; biallelic pathogenic variants can cause saposin C deficiency or broader prosaposin deficiency (liaqat2022phenotypeexpansionfor pages 1-2, motta2014gaucherdiseasedue pages 1-2) | Genes 2022; Hum Mol Genet 2014 |
| GBA gene | MIM/OMIM gene ID | 606463 | Encodes glucocerebrosidase/GCase; canonical Gaucher disease gene; SapC is its essential activator/cofactor (liaqat2022phenotypeexpansionfor pages 1-2, tamargo2012theroleof pages 1-2, motta2014gaucherdiseasedue pages 1-2) | Genes 2022; Mol Genet Metab 2012; Hum Mol Genet 2014 |
| Gaucher disease type 1 | MIM/OMIM disease ID | 230800 | Non-neuronopathic Gaucher reference subtype; SapC deficiency may clinically resemble type 1 in some patients (tamargo2012theroleof pages 1-2, motta2014gaucherdiseasedue pages 1-2) | Mol Genet Metab 2012; Hum Mol Genet 2014 |
| Gaucher disease type 2 | MIM/OMIM disease ID | 230900 | Acute neuronopathic Gaucher reference subtype; cited in review context for GD classification (pavan2024deficiencyofglucocerebrosidase pages 2-4) | Int J Mol Sci 2024 |
| Gaucher disease type 3 | MIM/OMIM disease ID | 231000 | Chronic neuronopathic Gaucher reference subtype; SapC deficiency often discussed as type 3-like/neuronopathic (tamargo2012theroleof pages 1-2, pavan2024deficiencyofglucocerebrosidase pages 2-4) | Mol Genet Metab 2012; Int J Mol Sci 2024 |
| Prosaposin deficiency | MIM/OMIM disease ID | 611721 | Distinct from isolated SapC deficiency; complete prosaposin deficiency affects all saposins and is typically more severe (tamargo2012theroleof pages 1-2, pavan2024deficiencyofglucocerebrosidase pages 1-2) | Mol Genet Metab 2012; Int J Mol Sci 2024 |
| Saposin C | Molecular concept | Essential activator of GCase | Derived from prosaposin; promotes GCase interaction with anionic lysosomal membranes and stabilizes enzyme activity/protein; deficiency can present despite normal in vitro GCase activity in some assays (tamargo2012theroleof pages 1-2, tamargo2012theroleof pages 5-7, motta2014gaucherdiseasedue pages 1-2) | Mol Genet Metab 2012; Hum Mol Genet 2014 |
| Evidence base | Resource provenance | Aggregated disease literature plus individual case reports | Knowledge derives mainly from case reports/small families and mechanistic studies, not EHR-scale datasets; only a handful of patients have been reported worldwide (liaqat2022phenotypeexpansionfor pages 5-7, tamargo2012theroleof pages 5-7) | Genes 2022; Mol Genet Metab 2012 |
| External identifiers not found in retrieved evidence | Identifier status | Orphanet/MONDO/MeSH/ICD not found | Absence here reflects retrieved evidence only and should not be interpreted as proof that no such identifiers exist in external databases (liaqat2022phenotypeexpansionfor pages 1-2, tamargo2012theroleof pages 1-2, motta2014gaucherdiseasedue pages 1-2) | Genes 2022; Mol Genet Metab 2012; Hum Mol Genet 2014 |


*Table: This table summarizes the key disease and gene identifiers, core synonyms, and classification facts for Gaucher disease due to saposin C deficiency. It is useful for normalizing nomenclature and linking PSAP-related disease concepts to canonical Gaucher disease subtypes.*

**Notes on identifiers:** Orphanet, MeSH, ICD-10/ICD-11, and MONDO identifiers were not present in the retrieved documents and therefore cannot be reliably populated from this evidence set (tamargo2012theroleof pages 1-2, motta2014gaucherdiseasedue pages 1-2).

### 1.3 Synonyms / alternative names
- Gaucher disease due to saposin C deficiency (tamargo2012theroleof pages 1-2, motta2014gaucherdiseasedue pages 1-2)
- Variant Gaucher disease caused by SAP-2 / saposin C (historical terminology) (rafi1993mutationalanalysisin pages 1-3)
- Atypical Gaucher disease due to PSAP (liaqat2022phenotypeexpansionfor pages 5-7, liaqat2022phenotypeexpansionfor pages 1-2)

### 1.4 Evidence provenance
The evidence base is dominated by **single-patient case reports and small families**, plus mechanistic in vitro and animal-model studies; it is not derived from EHR-scale aggregated cohorts (tamargo2012theroleof pages 5-7, liaqat2022phenotypeexpansionfor pages 5-7).

---

## 2. Etiology

### 2.1 Primary causal factors
- **Genetic cause:** biallelic pathogenic variants in **PSAP** affecting the SapC domain (autosomal recessive) (tamargo2012theroleof pages 1-2, motta2014gaucherdiseasedue pages 1-2).
- **Mechanistic cause:** loss of functional SapC reduces/impairs membrane-associated GCase activity and/or stability, leading to lysosomal glycosphingolipid storage (GlcCer ± GlcSph and other sphingolipids) and downstream macrophage and/or CNS pathology (tamargo2012theroleof pages 4-5, motta2014gaucherdiseasedue pages 1-2, pavan2024deficiencyofglucocerebrosidase pages 9-10).

### 2.2 Risk factors
- **Genetic:** consanguinity increases risk by increasing probability of homozygous PSAP variants; a large consanguineous Pakistani family with multiple affected individuals has been reported (liaqat2022phenotypeexpansionfor pages 5-7).
- **Environmental / infectious:** no disease-specific environmental or infectious risk factors were identified in the retrieved evidence.

### 2.3 Protective factors
No protective genetic or environmental factors were reported in the retrieved evidence.

### 2.4 Gene–environment interactions
No PSAP SapC-deficiency-specific gene–environment interaction evidence was found in the retrieved documents.

---

## 3. Phenotypes (clinical features) and ontology mapping

### 3.1 Phenotype spectrum and clinical heterogeneity
Across the limited number of reported patients, SapC deficiency can produce **type 1-like (visceral/hematologic/bone)** disease and/or **type 3-like neuronopathic** disease. A review of six reported patients described presentations ranging from type 1-like to type 3-like, including adult siblings with mild neurologic deterioration (tamargo2012theroleof pages 5-7, tamargo2012theroleof pages 1-2).

### 3.2 Structured phenotype + diagnostic feature table (with HPO suggestions)
| Phenotype/feature | HPO term suggestion | Typical onset/course | Notes/frequency (if available) | Key evidence |
|---|---|---|---|---|
| Hepatosplenomegaly | HP:0001433 Hepatosplenomegaly | Infantile to childhood; progressive or persistent | Commonly reported visceral feature across cases/families | Seen in classic case summaries and recent reports; 4-month-old PSAP case had hepatosplenomegaly; also reported in Pakistani family and Indian infant (tamargo2012theroleof pages 1-2, pavan2024deficiencyofglucocerebrosidase pages 2-4, liaqat2022phenotypeexpansionfor pages 5-7, li2025prosaposinamultifaceted pages 10-11) |
| Anemia | HP:0001903 Anemia | Infantile/childhood; chronic | Reported in Gaucher-like visceral presentations; not quantified for all cases | Listed among typical GD-like findings in SapC deficiency; present in Indian/Chinese summaries (tamargo2012theroleof pages 1-2, li2025prosaposinamultifaceted pages 10-11) |
| Thrombocytopenia | HP:0001873 Thrombocytopenia | Infantile to childhood; chronic | Recurrent hematologic finding | Reported in Pakistani family and in general SapC-deficiency phenotype descriptions (tamargo2012theroleof pages 1-2, liaqat2022phenotypeexpansionfor pages 5-7, li2025prosaposinamultifaceted pages 10-11) |
| Bone lesions / kyphosis | HP:0002650 Scoliosis/Kyphosis; HP:0002758 Osteolysis or HP:0000930 Generalized osteopenia | Childhood to adult; progressive/variable | Bone lesions are part of GD-like spectrum; kyphosis specifically reported in Pakistani family | Bone disease noted in reviews; kyphosis reported with p.Glu359Ala family (tamargo2012theroleof pages 1-2, liaqat2022phenotypeexpansionfor pages 5-7) |
| Pulmonary hypertension | HP:0002092 Pulmonary hypertension | Variable; likely later complication | Mentioned as part of GD clinical spectrum in SapC-deficiency review, not clearly frequency-defined for SapC cases | Listed among clinical features in 2014 mechanistic paper introduction (motta2014gaucherdiseasedue pages 1-2) |
| Seizures / encephalopathy | HP:0001250 Seizure; HP:0001298 Encephalopathy | Early infantile in severe neuronopathic cases; can be rapidly progressive | Indian infant had encephalopathy and refractory seizures; severe neonatal/infantile presentations reported | 2-month-old infant with encephalopathy and resistant tonic-clonic seizures died by 4 months (li2025prosaposinamultifaceted pages 10-11) |
| Hypotonia | HP:0001252 Hypotonia | Early infantile; progressive in severe cases | Present in severe infantile case; also 4-month-old PSAP_PT had hypotonia | Reported in Indian infant and PSAP_PT with severe neurologic disease (li2025prosaposinamultifaceted pages 10-11, pavan2024deficiencyofglucocerebrosidase pages 2-4) |
| Nystagmus | HP:0000639 Nystagmus | Early infantile in severe neuronopathic case | Reported in PSAP_PT suspected as GD2-like | 4-month-old infant had hypotonia, nystagmus, swallowing difficulty (pavan2024deficiencyofglucocerebrosidase pages 2-4) |
| Ataxia | HP:0001251 Ataxia | Childhood to adult; progressive neurologic course | Seen in type 3-like / neuronopathic presentations and mouse models | Included in human clinical spectrum and supported by SapC-deficient mouse phenotype (tamargo2012theroleof pages 1-2, sun2010specificsaposinc pages 1-2) |
| Myoclonic epilepsy | HP:0001336 Myoclonic seizures | Childhood/adolescent; progressive neuronopathic course | Reported in GD-like neurologic spectrum due to SapC deficiency | Included in SapC-deficiency clinical overlap with type 3 GD (tamargo2012theroleof pages 1-2) |
| Abnormal horizontal saccades | HP:0000640 Oculomotor apraxia / HP:0000616 Abnormality of eye movement | Childhood/adolescent; neurologic | Characteristic neuronopathic GD-like feature in some reported cases | Listed in review of six reported patients (tamargo2012theroleof pages 1-2) |
| Hearing impairment | HP:0000365 Hearing impairment | Congenital/prelingual or childhood; non-progressive/progressive uncertain | All affected members in Pakistani family had hearing impairment; prelingual profound SNHL highlighted | Strong feature in p.Glu359Ala family (liaqat2022phenotypeexpansionfor pages 5-7) |
| Vestibular dysfunction | HP:0001751 Vestibular areflexia / HP:0001756 Vestibular dysfunction | Childhood; chronic | Reported with hearing impairment in Pakistani family | Present in all affected family members in phenotype-expansion report (liaqat2022phenotypeexpansionfor pages 5-7) |
| GCase activity may be normal in vitro | HP:0012378 Abnormal enzyme/coenzyme activity | Diagnostic caveat; may obscure diagnosis | Important distinguishing feature: SapC deficiency can present despite normal standard GCase assay results | Human SapC-deficient cases can show normal in vitro GCase activity; one case had normal skin fibroblast GCase despite biomarker abnormalities (tamargo2012theroleof pages 1-2, rafi1993mutationalanalysisin pages 1-3, li2025prosaposinamultifaceted pages 11-13) |
| Tissue glucosylceramide accumulation | HP:0011015 Abnormal sphingolipid concentration | Persistent biochemical hallmark | May be demonstrated in spleen/tissue despite normal enzyme assay | Spleen glucosylceramide accumulation documented in variant Gaucher due to SapC deficiency (rafi1993mutationalanalysisin pages 1-3) |
| Plasma chitotriosidase elevation | HP:0034046 Increased circulating chitotriosidase level | Elevated at diagnosis; reflects macrophage activation | Markedly elevated in severe infantile PSAP case | PSAP_PT chitotriosidase 2951.0 nmol/mL/h (pavan2024deficiencyofglucocerebrosidase pages 2-4) |
| Plasma glucosylsphingosine (GlcSph) elevation | HP:0034383 Increased circulating glucosylsphingosine | Elevated at diagnosis | Useful GD biomarker in PSAP-related GCase deficiency | PSAP_PT plasma GlcSph 19.0 ng/mL (pavan2024deficiencyofglucocerebrosidase pages 2-4) |
| Lyso-Gb3 elevation | HP:0034380 Abnormal globotriaosylsphingosine level | Elevated at diagnosis in reported case | Ancillary lipid biomarker; may assist broader sphingolipid profiling | PSAP_PT Lyso-Gb3 1.98 ng/mL (pavan2024deficiencyofglucocerebrosidase pages 2-4) |
| PPCS elevation | HP:0034385 Abnormal lysosphingolipid profile | Elevated at diagnosis in reported case | Additional plasma biomarker reported in 2024 study | PSAP_PT PPCS 745.9 ng/mL (pavan2024deficiencyofglucocerebrosidase pages 2-4) |
| Genetic testing for PSAP variants | HP:0000007 Autosomal recessive inheritance | Confirmatory test; indicated when GD suspected but GBA1 negative or biochemistry atypical | Reported pathogenic variant classes include missense, nonsense, splice-site, start-loss, and deletions | PSAP sequencing/WES/Sanger used across cases; variants include p.E297*, p.Glu359Ala, p.C382G/F, p.L349P, c.1005+1G>A (liaqat2022phenotypeexpansionfor pages 5-7, motta2014gaucherdiseasedue pages 1-2, pavan2024deficiencyofglucocerebrosidase pages 2-4) |
| Negative GBA1 testing should trigger PSAP evaluation | HP:0000007 Autosomal recessive inheritance | Diagnostic workflow recommendation | Particularly important in infantile GD-like disease with elevated biomarkers and low-normal/normal GCase assays | 2024 PSAP_PT was GBA1-negative then diagnosed by PSAP testing; Indian report explicitly advises considering specific activator deficiency when GD is suspected with partially deficient or near-normal GBA activity (pavan2024deficiencyofglucocerebrosidase pages 2-4, li2025prosaposinamultifaceted pages 10-11) |


*Table: This table summarizes the reported clinical spectrum and key diagnostic findings for Gaucher disease due to saposin C deficiency caused by PSAP variants. It is useful for distinguishing this ultra-rare activator deficiency from canonical GBA1-related Gaucher disease, especially when enzyme activity is normal or only mildly reduced.*

### 3.3 Quality of life impact
Formal QoL instruments (e.g., EQ-5D/SF-36/PROMIS) were not reported in the retrieved evidence. Severe infantile neuronopathic disease is expected to substantially impair functioning (hypotonia, swallowing difficulty, seizures), while chronic neurologic disease (ataxia) and visceral disease (organomegaly, cytopenias) can impair daily activity and endurance (pavan2024deficiencyofglucocerebrosidase pages 2-4, tamargo2012theroleof pages 1-2).

---

## 4. Genetic / Molecular Information

### 4.1 Causal gene(s)
- **PSAP** (prosaposin; SapC derived from prosaposin proteolysis) (tamargo2012theroleof pages 1-2, motta2014gaucherdiseasedue pages 1-2).

### 4.2 Pathogenic variants (examples from primary/review literature)
Evidence-supported PSAP/SapC-domain pathogenic or likely pathogenic variants include:
- **c.1144T>G (p.Cys382Gly)** reported in a variant Gaucher case with glucosylceramide accumulation despite normal measured glucocerebrosidase activity (rafi1993mutationalanalysisin pages 1-3).
- SapC lesions summarized in mechanistic work: **p.C315S, p.342_348FDKMCSKdel, p.L349P, p.C382G, p.C382F** (motta2014gaucherdiseasedue pages 1-2).
- A consanguineous family with likely pathogenic **c.1076A>C (p.Glu359Ala)** in the SapC domain; variant is rare in gnomAD and lies in the SapC GCase-binding region (aa 351–390) (liaqat2022phenotypeexpansionfor pages 5-7).
- Severe infantile case: **c.889G>T (p.E297*)** with nonsense-mediated mRNA decay; GD2-like suspicion clinically (pavan2024deficiencyofglucocerebrosidase pages 2-4).

**Variant classes observed:** missense, in-frame deletion, nonsense, splice-site; many reported variants affect SapC cysteines/disulfide bonds or otherwise destabilize the SapC fold (tamargo2012theroleof pages 5-7, motta2014gaucherdiseasedue pages 1-2).

### 4.3 Functional consequences
- SapC is a small, cysteine-rich activator/cofactor with disulfide bonds that confer acid stability; multiple disease mutants adopt aberrant disulfide arrangements and are **rapidly degraded**, with evidence implicating **autophagy-mediated degradation** as a key pathogenic mechanism in SapC deficiency (motta2014gaucherdiseasedue pages 1-2).
- SapC also protects GCase from proteolysis; absence of SapC can reduce tissue GCase activity and increase degradation, which can be modulated by protease inhibitors in experimental systems (tamargo2012theroleof pages 4-5).

### 4.4 Modifier genes / epigenetics / chromosomal abnormalities
No SapC-deficiency-specific modifier gene, epigenetic, or chromosomal abnormality evidence was found in the retrieved documents.

---

## 5. Environmental Information
No disease-specific environmental, lifestyle, or infectious contributors were identified in the retrieved evidence; the disorder is primarily genetic (tamargo2012theroleof pages 1-2, motta2014gaucherdiseasedue pages 1-2).

---

## 6. Mechanism / Pathophysiology

### 6.1 Causal chain (trigger → molecular defect → cellular dysfunction → clinical phenotype)
1. **Upstream trigger:** biallelic PSAP variants reduce/abolish functional SapC production or stability (including nonsense-mediated decay for truncating variants) (pavan2024deficiencyofglucocerebrosidase pages 2-4, pavan2024deficiencyofglucocerebrosidase pages 9-10).
2. **Primary molecular defect:** SapC normally binds anionic lysosomal membranes and GCase, enabling membrane-associated presentation/access of GlcCer to the enzyme; SapC also stabilizes/protects GCase from proteolysis (tamargo2012theroleof pages 4-5, tamargo2012theroleof pages 5-7).
3. **Biochemical consequence:** reduced effective GCase-mediated degradation causes storage of GlcCer and often **glucosylsphingosine (GlcSph)** (and sometimes other sphingolipids) (tamargo2012theroleof pages 5-7, pavan2024deficiencyofglucocerebrosidase pages 9-10).
4. **Cellular pathology:** lipid-laden macrophages (“Gaucher cells”) drive inflammation and visceral disease; in neuronopathic cases, CNS pathology includes neuronal inclusions, Purkinje cell loss, axonal degeneration, and glial activation/inflammation (sun2010specificsaposinc pages 1-2, tamargo2012theroleof pages 5-7).
5. **Clinical manifestations:** hepatosplenomegaly, cytopenias, bone disease; and/or neurologic impairment (hypotonia, seizures, ataxia, abnormal eye movements, etc.) (tamargo2012theroleof pages 1-2, pavan2024deficiencyofglucocerebrosidase pages 2-4).

### 6.2 Pathways, processes, and suggested GO terms
**Key molecular/cellular processes (GO Biological Process suggestions):**
- Lysosomal glycosphingolipid catabolic process / sphingolipid metabolic process (supported conceptually by impaired GlcCer breakdown) (pavan2024deficiencyofglucocerebrosidase pages 1-2, pavan2024deficiencyofglucocerebrosidase pages 9-10)
- Lysosome organization and membrane-associated catabolism (SapC-mediated membrane interaction/liftase model) (tamargo2012theroleof pages 4-5)
- Autophagy (as a degradation route for mutant SapC proteins) (motta2014gaucherdiseasedue pages 1-2)
- Neuroinflammatory response / glial activation (microglia, astrocytes activated in SapC-deficient mouse CNS) (sun2010specificsaposinc pages 1-2)

### 6.3 Cell types and suggested CL terms
**Cell Ontology (CL) suggestions based on evidence:**
- Macrophage (Gaucher cells; mononuclear phagocyte system involvement) (tamargo2012theroleof pages 1-2, motta2014gaucherdiseasedue pages 1-2)
- Microglial cell (activated microglia in SapC-deficient mouse CNS) (sun2010specificsaposinc pages 1-2)
- Astrocyte (astrocyte activation in SapC-deficient mouse CNS) (sun2010specificsaposinc pages 1-2)
- Purkinje cell (cerebellar Purkinje neuron loss in SapC-deficient mouse model) (sun2010specificsaposinc pages 1-2)

### 6.4 Expert mechanistic analysis (authoritative synthesis)
High-citation expert reviews emphasize that SapC functions as a membrane-active cofactor enabling optimal GCase function and that SapC deficiency can yield a Gaucher phenotype even with apparently normal in vitro enzyme assays, which has important diagnostic implications (tamargo2012theroleof pages 1-2, tamargo2012theroleof pages 4-5).

**Direct abstract quote (animal model; mechanistic):**
- Sun et al. report: “*The few patients with saposin C deficiency develop a Gaucher disease-like central nervous system (CNS) phenotype attributed to diminished glucosylceramide (GC) cleavage activity by acid β-glucosidase (GCase).*” (Human Molecular Genetics; Dec 2010; https://doi.org/10.1093/hmg/ddp531) (sun2010specificsaposinc pages 1-2)

---

## 7. Anatomical Structures Affected

### 7.1 Organ/system level (UBERON suggestions)
- **Liver / spleen (hepatosplenomegaly):** mononuclear phagocyte system storage involvement (UBERON: liver; UBERON: spleen) (tamargo2012theroleof pages 1-2, pavan2024deficiencyofglucocerebrosidase pages 2-4).
- **Bone / skeletal system:** bone lesions and kyphosis reported; osteoarticular involvement is typical of Gaucher-like disease (UBERON: bone of lower limb / vertebral column) (tamargo2012theroleof pages 1-2, liaqat2022phenotypeexpansionfor pages 5-7).
- **Central nervous system:** neuronopathic presentations include seizures, hypotonia, ataxia, eye movement abnormalities; SapC-deficient mice show cerebellar and axonal pathology (UBERON: brain; UBERON: cerebellum; UBERON: spinal cord) (sun2010specificsaposinc pages 1-2, pavan2024deficiencyofglucocerebrosidase pages 2-4).

### 7.2 Tissue/cell level
- Monocyte/macrophage lineage cells with lysosomal lipid storage (motta2014gaucherdiseasedue pages 1-2).
- Cerebellar neuronal populations (Purkinje cells) and glial cells (microglia, astrocytes) in neurologic disease models (sun2010specificsaposinc pages 1-2).

### 7.3 Subcellular level (GO Cellular Component suggestions)
- Lysosome (site of glycosphingolipid catabolism and SapC–GCase function) (pavan2024deficiencyofglucocerebrosidase pages 1-2, tamargo2012theroleof pages 4-5).

---

## 8. Temporal Development

### 8.1 Onset
Onset is variable, ranging from **infantile severe neurologic disease** (including GD2-like presentations) to **childhood/adult-onset neurologic deterioration** or more type 1-like disease without clear CNS signs in some families (pavan2024deficiencyofglucocerebrosidase pages 2-4, tamargo2012theroleof pages 5-7, liaqat2022phenotypeexpansionfor pages 5-7).

### 8.2 Progression
Severe infantile cases may progress rapidly and can be fatal within months (pavan2024deficiencyofglucocerebrosidase pages 2-4). Other cases show chronic neurologic progression (e.g., ataxia) or chronic visceral disease (tamargo2012theroleof pages 5-7, tamargo2012theroleof pages 1-2).

---

## 9. Inheritance and Population

### 9.1 Inheritance
Autosomal recessive inheritance is strongly supported by multiple reports of homozygous/biallelic PSAP variants and occurrence in consanguineous families (tamargo2012theroleof pages 1-2, liaqat2022phenotypeexpansionfor pages 5-7, pavan2024deficiencyofglucocerebrosidase pages 2-4).

### 9.2 Epidemiology
No population-level prevalence or incidence estimates were identified in the retrieved literature. Available synthesis notes only a handful of published patients worldwide (e.g., six described in one review; and ~seven reported cases cited in a later family report), consistent with an ultra-rare condition (tamargo2012theroleof pages 5-7, liaqat2022phenotypeexpansionfor pages 5-7).

### 9.3 Population genetics / allele frequency example
The likely pathogenic **PSAP c.1076A>C (p.Glu359Ala)** variant was reported as rare in gnomAD (overall AF 5.3×10−5; South Asian AF 3.6×10−4; no homozygotes in gnomAD per authors) (liaqat2022phenotypeexpansionfor pages 5-7).

---

## 10. Diagnostics

### 10.1 Clinical suspicion
Consider PSAP/SapC deficiency when a patient has a **Gaucher-like phenotype** (hepatosplenomegaly, cytopenias ± bone disease and/or neurologic disease) but:
- **GBA1 testing is negative**, and/or
- **GCase activity is normal/low-normal** on standard assays (diagnostic pitfall), and/or
- biomarkers suggest Gaucher-like macrophage activation and glycosphingolipid storage (pavan2024deficiencyofglucocerebrosidase pages 2-4, rafi1993mutationalanalysisin pages 1-3, tamargo2012theroleof pages 1-2).

### 10.2 Laboratory biomarkers and statistics from recent study (2024)
A 2024 biochemical profiling study reports markedly elevated Gaucher biomarkers in a PSAP case (PSAP_PT):
- **Chitotriosidase:** **2951.0 nmol/mL/h**
- **Plasma glucosylsphingosine (GlcSph):** **19.0 ng/mL**
- **Lyso-Gb3:** **1.98 ng/mL**
- **PPCS:** **745.9 ng/mL**
with a homozygous truncating PSAP variant (c.889G>T; p.E297*) and severe infantile disease (Jun 2024; https://doi.org/10.3390/ijms25126615) (pavan2024deficiencyofglucocerebrosidase pages 2-4).

### 10.3 Enzyme activity testing caveat
A seminal primary report documented glucosylceramide accumulation in spleen **despite normal measured glucocerebrosidase activity**, supporting “activator deficiency” rather than enzyme deficiency (rafi1993mutationalanalysisin pages 1-3).

### 10.4 Genetic testing approach
- Confirmatory testing is **PSAP sequencing** (single-gene, lysosomal storage disease panels, or exome/genome sequencing) and variant interpretation in the context of phenotype and biochemical findings (liaqat2022phenotypeexpansionfor pages 5-7, pavan2024deficiencyofglucocerebrosidase pages 2-4).

---

## 11. Outcome / Prognosis
Prognosis appears highly variable and genotype/phenotype dependent. A severe infantile PSAP truncating-variant case with GD2-like features died a few months after diagnosis (pavan2024deficiencyofglucocerebrosidase pages 2-4). Milder phenotypes without overt CNS involvement have been reported in families, implying potentially longer survival (liaqat2022phenotypeexpansionfor pages 5-7). Systematic survival statistics are not available in the retrieved evidence.

---

## 12. Treatment

### 12.1 Disease-directed therapies
No controlled clinical trial evidence specific to **SapC deficiency** treatment was identified in the retrieved documents, and the clinical trials search did not return SapC-deficiency-specific interventional trials.

Mechanistically, SapC deficiency is an *activator/cofactor deficiency* rather than a primary GCase catalytic deficiency. Expert reviews discuss that increasing SapC levels or restoring SapC–GCase interactions could be therapeutic in principle, and that chemical chaperones can improve folding/trafficking and SapC–enzyme interactions in experimental contexts, but these are not presented as established clinical therapies for SapC deficiency in the retrieved evidence (tamargo2012theroleof pages 5-7, tamargo2012theroleof pages 7-8).

### 12.2 Supportive care
Supportive management is implied by clinical features (e.g., management of cytopenias, organomegaly complications, seizures, swallowing dysfunction), but specific guidelines were not found in the retrieved evidence.

### 12.3 MAXO term suggestions
- Enzyme activity assay / enzyme replacement-related actions are not directly evidenced as effective here; nevertheless, for knowledge-base normalization:
  - MAXO: enzyme replacement therapy (as a general Gaucher therapy class; disease-specific effectiveness for SapC deficiency not evidenced)
  - MAXO: anticonvulsant therapy (for seizure management in neuronopathic presentations)
  - MAXO: supportive respiratory care / feeding support (for severe infantile neurologic disease)

---

## 13. Prevention

### 13.1 Primary/secondary prevention (genetic)
Given autosomal recessive inheritance, prevention is primarily through **genetic counseling** and **prenatal or preimplantation genetic testing** in families with known PSAP variants. A PSAP-related infantile case report summary indicates prenatal diagnosis in a subsequent pregnancy identified a carrier fetus who was unaffected postnatally (reported as part of the PSAP infantile case summary in a synthesis) (li2025prosaposinamultifaceted pages 10-11).

---

## 14. Other Species / Natural Disease
Natural SapC-deficiency animal disease was not identified in the retrieved evidence.

---

## 15. Model Organisms

### 15.1 Mouse models
A selective SapC-deficient mouse model (knock-in point mutation eliminating SapC) exhibits a CNS-predominant phenotype (hindlimb weakness, progressive ataxia, neurophysiologic impairment, dorsal root ganglion storage cells, Purkinje cell loss, glial activation) with little/no visceral organ storage—highlighting both mechanistic insight and limitations in recapitulating human visceral disease (sun2010specificsaposinc pages 1-2).

**Direct abstract quote (mouse model):**
- “*By 1 year, the C−/− mice exhibited weakness of the hind limbs and progressive ataxia.*” (Human Molecular Genetics; Dec 2010; https://doi.org/10.1093/hmg/ddp531) (sun2010specificsaposinc pages 1-2)

---

## 2023–2024 developments and real-world implementation highlights

1. **2024 biochemical profiling beyond GBA1 Gaucher disease:** A 2024 study explicitly compares GCase-deficiency etiologies (GBA1 vs PSAP vs SCARB2/LIMP-2) and provides quantified biomarker data (chitotriosidase, GlcSph, Lyso-Gb3, PPCS) in a PSAP case, supporting real-world diagnostic workflows for “Gaucher-like” presentations with negative GBA1 testing (Jun 2024; https://doi.org/10.3390/ijms25126615) (pavan2024deficiencyofglucocerebrosidase pages 2-4, pavan2024deficiencyofglucocerebrosidase pages 1-2).
2. **2023 case-based evidence of PSAP-related disease burden:** A 2023 neonatal case report of combined saposin deficiency illustrates severe neurovisceral presentations and reinforces that enzymatic and genetic confirmation plus counseling are implemented in real clinical settings (Mar 2023; https://doi.org/10.1016/j.mjafi.2021.01.024) (bhat2023combinedsaposindeficiency pages 1-2).

---

## Evidence gaps (important for knowledge base curation)
- **Orphanet/MONDO/MeSH/ICD identifiers** were not extractable from the retrieved full text and should be populated via dedicated database lookup rather than inferred here (tamargo2012theroleof pages 1-2, motta2014gaucherdiseasedue pages 1-2).
- **Treatment efficacy evidence** (ERT/SRT/gene therapy) specifically for SapC deficiency was not found in the retrieved documents; mechanistic speculation exists, but clinical outcome evidence is not available in this evidence set (tamargo2012theroleof pages 5-7).
- **Epidemiology** (prevalence/incidence) is not available in the retrieved literature, beyond statements of extreme rarity and small numbers of published cases (tamargo2012theroleof pages 5-7, liaqat2022phenotypeexpansionfor pages 5-7).


References

1. (tamargo2012theroleof pages 1-2): Rafael J. Tamargo, Arash Velayati, Ehud Goldin, and Ellen Sidransky. The role of saposin c in gaucher disease. Molecular genetics and metabolism, 106 3:257-63, Jul 2012. URL: https://doi.org/10.1016/j.ymgme.2012.04.024, doi:10.1016/j.ymgme.2012.04.024. This article has 208 citations and is from a peer-reviewed journal.

2. (motta2014gaucherdiseasedue pages 1-2): Marialetizia Motta, Serena Camerini, Massimo Tatti, Marialuisa Casella, Paola Torreri, Marco Crescenzi, Marco Tartaglia, and Rosa Salvioli. Gaucher disease due to saposin c deficiency is an inherited lysosomal disease caused by rapidly degraded mutant proteins. Human molecular genetics, 23 21:5814-26, Nov 2014. URL: https://doi.org/10.1093/hmg/ddu299, doi:10.1093/hmg/ddu299. This article has 45 citations and is from a domain leading peer-reviewed journal.

3. (rafi1993mutationalanalysisin pages 1-3): Mohammad A. Rafi, Gregory Gala, Xun-ling Zhang, and David A. Wenger. Mutational analysis in a patient with a variant form of gaucher disease caused by sap-2 deficiency. Somatic Cell and Molecular Genetics, 19:1-7, Jan 1993. URL: https://doi.org/10.1007/bf01233949, doi:10.1007/bf01233949. This article has 102 citations.

4. (liaqat2022phenotypeexpansionfor pages 1-2): Khurram Liaqat, Shabir Hussain, Anushree Acharya, Abdul Nasir, Thashi Bharadwaj, Muhammad Ansar, Sulman Basit, Isabelle Schrauwen, Wasim Ahmad, and Suzanne M. Leal. Phenotype expansion for atypical gaucher disease due to homozygous missense psap variant in a large consanguineous pakistani family. Genes, 13:662, Apr 2022. URL: https://doi.org/10.3390/genes13040662, doi:10.3390/genes13040662. This article has 15 citations.

5. (liaqat2022phenotypeexpansionfor pages 5-7): Khurram Liaqat, Shabir Hussain, Anushree Acharya, Abdul Nasir, Thashi Bharadwaj, Muhammad Ansar, Sulman Basit, Isabelle Schrauwen, Wasim Ahmad, and Suzanne M. Leal. Phenotype expansion for atypical gaucher disease due to homozygous missense psap variant in a large consanguineous pakistani family. Genes, 13:662, Apr 2022. URL: https://doi.org/10.3390/genes13040662, doi:10.3390/genes13040662. This article has 15 citations.

6. (pavan2024deficiencyofglucocerebrosidase pages 2-4): Eleonora Pavan, Paolo Peruzzo, Silvia Cattarossi, Natascha Bergamin, Andrea Bordugo, Annalisa Sechi, Maurizio Scarpa, Jessica Biasizzo, Fabiana Colucci, and Andrea Dardis. Deficiency of glucocerebrosidase activity beyond gaucher disease: psap and limp-2 dysfunctions. International Journal of Molecular Sciences, 25:6615, Jun 2024. URL: https://doi.org/10.3390/ijms25126615, doi:10.3390/ijms25126615. This article has 10 citations.

7. (pavan2024deficiencyofglucocerebrosidase pages 1-2): Eleonora Pavan, Paolo Peruzzo, Silvia Cattarossi, Natascha Bergamin, Andrea Bordugo, Annalisa Sechi, Maurizio Scarpa, Jessica Biasizzo, Fabiana Colucci, and Andrea Dardis. Deficiency of glucocerebrosidase activity beyond gaucher disease: psap and limp-2 dysfunctions. International Journal of Molecular Sciences, 25:6615, Jun 2024. URL: https://doi.org/10.3390/ijms25126615, doi:10.3390/ijms25126615. This article has 10 citations.

8. (tamargo2012theroleof pages 5-7): Rafael J. Tamargo, Arash Velayati, Ehud Goldin, and Ellen Sidransky. The role of saposin c in gaucher disease. Molecular genetics and metabolism, 106 3:257-63, Jul 2012. URL: https://doi.org/10.1016/j.ymgme.2012.04.024, doi:10.1016/j.ymgme.2012.04.024. This article has 208 citations and is from a peer-reviewed journal.

9. (tamargo2012theroleof pages 4-5): Rafael J. Tamargo, Arash Velayati, Ehud Goldin, and Ellen Sidransky. The role of saposin c in gaucher disease. Molecular genetics and metabolism, 106 3:257-63, Jul 2012. URL: https://doi.org/10.1016/j.ymgme.2012.04.024, doi:10.1016/j.ymgme.2012.04.024. This article has 208 citations and is from a peer-reviewed journal.

10. (pavan2024deficiencyofglucocerebrosidase pages 9-10): Eleonora Pavan, Paolo Peruzzo, Silvia Cattarossi, Natascha Bergamin, Andrea Bordugo, Annalisa Sechi, Maurizio Scarpa, Jessica Biasizzo, Fabiana Colucci, and Andrea Dardis. Deficiency of glucocerebrosidase activity beyond gaucher disease: psap and limp-2 dysfunctions. International Journal of Molecular Sciences, 25:6615, Jun 2024. URL: https://doi.org/10.3390/ijms25126615, doi:10.3390/ijms25126615. This article has 10 citations.

11. (li2025prosaposinamultifaceted pages 10-11): Xin Li and Liang Guo. Prosaposin: a multifaceted protein orchestrating biological processes and diseases. Cells, 14:1131, Jul 2025. URL: https://doi.org/10.3390/cells14151131, doi:10.3390/cells14151131. This article has 10 citations.

12. (sun2010specificsaposinc pages 1-2): Y. Sun, H. Ran, M. Zamzow, K. Kitatani, M. R. Skelton, M. T. Williams, C. V. Vorhees, D. P. Witte, Y. A. Hannun, and G. A. Grabowski. Specific saposin c deficiency: cns impairment and acid β-glucosidase effects in the mouse. Human Molecular Genetics, 19:634-647, Dec 2010. URL: https://doi.org/10.1093/hmg/ddp531, doi:10.1093/hmg/ddp531. This article has 41 citations and is from a domain leading peer-reviewed journal.

13. (li2025prosaposinamultifaceted pages 11-13): Xin Li and Liang Guo. Prosaposin: a multifaceted protein orchestrating biological processes and diseases. Cells, 14:1131, Jul 2025. URL: https://doi.org/10.3390/cells14151131, doi:10.3390/cells14151131. This article has 10 citations.

14. (tamargo2012theroleof pages 7-8): Rafael J. Tamargo, Arash Velayati, Ehud Goldin, and Ellen Sidransky. The role of saposin c in gaucher disease. Molecular genetics and metabolism, 106 3:257-63, Jul 2012. URL: https://doi.org/10.1016/j.ymgme.2012.04.024, doi:10.1016/j.ymgme.2012.04.024. This article has 208 citations and is from a peer-reviewed journal.

15. (bhat2023combinedsaposindeficiency pages 1-2): Vivek Bhat, R.W. Thergaonkar, Manisha Thakur, and T. Rajkamal. Combined saposin deficiency: a rare occurrence. Medical Journal Armed Forces India, 79:238-240, Mar 2023. URL: https://doi.org/10.1016/j.mjafi.2021.01.024, doi:10.1016/j.mjafi.2021.01.024. This article has 3 citations.

## Artifacts

- [Edison artifact artifact-00](Gaucher_Disease_Due_To_Saposin_C_Deficiency-deep-research-falcon_artifacts/artifact-00.md)
- [Edison artifact artifact-01](Gaucher_Disease_Due_To_Saposin_C_Deficiency-deep-research-falcon_artifacts/artifact-01.md)