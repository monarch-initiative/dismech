---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-30T15:24:41.317028'
end_time: '2026-07-30T15:41:44.883734'
duration_seconds: 1023.57
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Global Developmental Delay, Progressive Ataxia, and Elevated Glutamine
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
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Global_Developmental_Delay_Progressive_Ataxia_and_Elevated_Glutamine-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Global Developmental Delay, Progressive Ataxia, and Elevated Glutamine
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Global Developmental Delay, Progressive Ataxia, and Elevated Glutamine** covering all of the
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
- **Disease Name:** Global Developmental Delay, Progressive Ataxia, and Elevated Glutamine
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Global Developmental Delay, Progressive Ataxia, and Elevated Glutamine** covering all of the
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


# Global developmental delay, progressive ataxia, and elevated glutamine (GDPAG)

## Executive summary

GDPAG is an ultra-rare autosomal-recessive inborn error of glutamate–glutamine metabolism caused by biallelic loss of **GLS**, the gene encoding mitochondrial kidney-type glutaminase. Its defining triad is early global developmental delay, progressive ataxia, and elevated plasma glutamine with reportedly normal plasma glutamate. The best-characterized molecular cause is a large **GCA repeat expansion in the GLS 5′ untranslated region (5′UTR)**, either homozygous or in trans with a damaging coding allele. The expansion creates repressive chromatin and reduces GLS transcription rather than causing promoter DNA hypermethylation. Published disease-specific evidence remains exceptionally small—principally three unrelated probands—so prevalence, complete phenotypic frequencies, prognosis, and treatment efficacy cannot yet be estimated reliably. (rumping2020inbornerrorsof pages 3-4, richmond2020expandingtheutility pages 72-78, richmond2020expandingtheutility pages 78-83)

| domain | established finding | evidence type/sample | confidence or limitation |
|---|---|---|---|
| Disease identity | Global developmental delay, progressive ataxia, and elevated glutamine corresponds to GDPAG; OMIM 618412 is explicitly linked in retrieved literature, and Open Targets maps the disease to EFO_0010257 with GLS as the associated target (shu2023thepowerof pages 7-8, OpenTargets Search: Global developmental delay, progressive ataxia, and elevated glutamine) | Disease database / review context | High for OMIM and EFO mapping; MONDO and other identifiers were not established from retrieved evidence |
| Gene and inheritance | Causal gene is **GLS** (glutaminase); the disorder is autosomal recessive, with biallelic pathogenic alleles including coding variants and/or 5′UTR GCA repeat expansions (shu2023thepowerof pages 7-8, richmond2020expandingtheutility pages 72-78) | Human genetic evidence from 3 unrelated probands/families | High for GLS and AR inheritance |
| Case count | Three unrelated affected index cases/families were reported for the GLS 5′UTR GCA-repeat form of GDPAG (rumping2020inbornerrorsof pages 3-4, richmond2020expandingtheutility pages 72-78) | Human case series | Moderate; retrieved text summarizes the study but does not provide full demographic detail |
| Genotype: Family 1 | Compound heterozygous: paternally inherited **c.938C>T (p.Pro313Leu)** plus maternally inherited 5′UTR **GCA repeat expansion**; expansion estimated as >90 by ExpansionHunter, rising to 246 with off-target reads; repeat PCR showed a major expansion product of ~680 repeats (richmond2020expandingtheutility pages 72-78) | Human molecular genetics in 1 proband/family | Moderate; different assays yielded different size estimates, reflecting technical uncertainty for large repeats |
| Genotype: Family 2 | Homozygous 5′UTR **GCA repeat expansion** alleles inherited from both parents; repeat PCR showed a major expansion product of ~900 repeats (richmond2020expandingtheutility pages 72-78) | Human molecular genetics in 1 proband/family | Moderate; exact allele-by-allele repeat lengths were not fully resolved |
| Genotype: Family 3 | Compound heterozygous: maternally inherited **c.923dupA (p.Tyr308\*)** plus paternally inherited 5′UTR **GCA repeat expansion**; repeat PCR showed a major expansion product of ~1500 repeats (richmond2020expandingtheutility pages 72-78) | Human molecular genetics in 1 proband/family | Moderate; expansion size is approximate |
| Population repeat data | In 8,295 genomes, the GLS GCA repeat had median size **14 repeats**, bimodal peaks at **8** and **16**; 1 person was heterozygous for an allele with >90 repeats, implying allele frequency **6.03×10^-5** for such large expanded alleles (richmond2020expandingtheutility pages 72-78) | Population genome screening | Moderate; based on short-read genome analysis at a difficult repeat locus |
| Core phenotype | The GLS repeat-expansion phenotype was reported as **early-onset/global developmental delay**, **progressive ataxia**, and **elevated plasma glutamine**; plasma glutamate was unaltered (rumping2020inbornerrorsof pages 3-4, richmond2020expandingtheutility pages 72-78) | Human clinical/biochemical evidence | High for these core features; many additional phenotype details were not available in retrieved text |
| Biochemical marker | Elevated **plasma glutamine** with **normal plasma glutamate** is the main reported disease biomarker; biochemical and flux assays supported glutaminase deficiency in patient cells (rumping2020inbornerrorsof pages 3-4, richmond2020expandingtheutility pages 72-78) | Human plasma biochemistry plus fibroblast/PBM functional assays | High for qualitative direction; quantitative metabolite values were not available |
| Enzyme deficiency | Patient fibroblasts and peripheral-blood mononuclear cells showed **reduced GLS activity** and decreased GLS protein/expression; residual activity was present, which was proposed to explain a milder phenotype than complete ablation (richmond2020expandingtheutility pages 72-78, richmond2020expandingtheutility pages 78-83) | Human patient-derived cells | High for reduced activity/expression; exact activity values not extracted |
| Molecular mechanism | The 5′UTR GCA repeat expansion did **not** show increased DNA methylation, but was associated with reduced **H3 acetylation** and **H3K4me3** and increased **H3K9me3**, consistent with repressive chromatin and decreased GLS transcription (richmond2020expandingtheutility pages 78-83) | Patient fibroblast chromatin studies | High for chromatin-silencing mechanism in tested cells |
| Diagnostic methods | Detection required methods beyond exome sequencing: **singleton WGS/manual inspection**, **ExpansionHunter**, **triplet repeat–primed PCR**, **repeat-flanking PCR/agarose sizing**, **Sanger sequencing** for coding variants/non-expanded alleles, plus **qPCR/cDNA allelic expression** and **enzyme assays** (richmond2020expandingtheutility pages 72-78, shu2023thepowerof pages 7-8) | Human diagnostic workflow evidence | High that standard ES can miss this lesion; exact clinical sensitivity/specificity not available |
| Distinction from other GLS disorders | Retrieved literature distinguishes GDPAG from a **de novo hypermorphic GLS** disorder and from other severe **GLS loss-of-function** epileptic/neonatal phenotypes; GDPAG specifically refers here to the AR GLS deficiency with developmental delay, progressive ataxia, and elevated glutamine (rumping2020inbornerrorsof pages 3-4, rumping2020metabolicfingerprintingreveals pages 1-6) | Review synthesis across GLS-associated phenotypes | Moderate; distinction is clear, but retrieved sources did not fully harmonize modern nosology |
| Model organisms | **Zebrafish** knockdown of GLS orthologues (**glsa, glsl**) caused **smaller body size, curved body, and cardiac edema**; prior **mouse** data cited in the retrieved text indicate GLS ablation impairs glutamatergic synaptic transmission and causes early death from respiratory problems, with heterozygotes showing hippocampal hypoactivity (richmond2020expandingtheutility pages 72-78, richmond2020expandingtheutility pages 78-83) | Animal models | Moderate; model findings support biology but do not fully recapitulate the human GDPAG phenotype |
| Treatment | No disease-specific pharmacologic, gene, RNA, or dietary therapy for GDPAG was established in the retrieved evidence (rumping2020inbornerrorsof pages 3-4, richmond2020expandingtheutility pages 72-78) | Evidence-gap assessment | Low therapeutic certainty because of absence of direct interventional studies |
| Clinical trials | No relevant interventional trials for GDPAG/glutaminase deficiency were identified; retrieved GLS trials were oncology **GLS inhibitor** studies and are not applicable to an enzyme-deficiency disorder (OpenTargets Search: Global developmental delay, progressive ataxia, and elevated glutamine) | Clinical-trial search context | High as a current evidence gap |
| Epidemiology | No prevalence or incidence estimate for GDPAG was identified in retrieved disease-specific evidence; currently evidence is limited to a very small number of families/cases (rumping2020inbornerrorsof pages 3-4, richmond2020expandingtheutility pages 72-78) | Evidence-gap assessment from case literature | High as a gap; rarity is evident but not quantifiable from retrieved sources |


*Table: This table condenses the strongest retrieved evidence for GLS-associated GDPAG, emphasizing what is established versus what remains uncertain. It is useful for a knowledge-base entry because it separates core disease facts from important evidence gaps.*

## 1. Disease information

**Definition.** GDPAG is a Mendelian neurometabolic/neurodevelopmental disorder of glutaminase deficiency. GLS normally hydrolyzes glutamine to glutamate and ammonia; therefore, reduced GLS function impairs the first step of glutamine catabolism. GLS is expressed especially in brain and kidney, whereas the paralog **GLS2** is predominantly hepatic. (rumping2020inbornerrorsof pages 3-4)

**Identifiers and synonyms**

- **Preferred name:** Global developmental delay, progressive ataxia, and elevated glutamine.
- **Abbreviation:** GDPAG.
- **OMIM:** **#618412**.
- **Open Targets/EFO:** **EFO_0010257**; Open Targets associates the entity with **GLS/ENSG00000115419**. (OpenTargets Search: Global developmental delay, progressive ataxia, and elevated glutamine, shu2023thepowerof pages 7-8)
- **Synonyms:** *GLS deficiency*, *glutaminase deficiency*, and *GLS-related GDPAG* are useful descriptive alternatives.
- **MONDO, Orphanet, MeSH, ICD-10 and ICD-11:** no disease-specific identifiers were established in the retrieved evidence. A knowledge base should not assign a generic ataxia, developmental-disorder, or amino-acid-metabolism code as though it were disease-specific.

**Evidence granularity.** The clinical evidence is patient-level data from three unrelated probands/families, subsequently summarized in disease-level reviews and databases. It is not an EHR-derived population cohort. (rumping2020inbornerrorsof pages 3-4, richmond2020expandingtheutility pages 72-78)

**Nosologic caution.** GDPAG should not be conflated with other allelic GLS disorders: severe neonatal/developmental and epileptic encephalopathy from other biallelic loss-of-function alleles, an optic-atrophy/ataxia phenotype associated with a homozygous exon-1 duplication, or the distinct de novo **p.Ser482Cys hypermorphic** disorder with glutamate excess, cataract, profound developmental delay, hypotonia, and behavioral abnormalities. (rumping2020inbornerrorsof pages 3-4, rumping2020metabolicfingerprintingreveals pages 1-6)

## 2. Etiology, risk, and protective factors

### Primary cause

The disease is caused by **germline biallelic GLS loss of function**. In the three foundational families:

1. **Family 1:** paternal **c.938C>T (p.Pro313Leu)** plus a maternal 5′UTR GCA expansion.
2. **Family 2:** GCA expansions inherited from both parents.
3. **Family 3:** maternal **c.923dupA (p.Tyr308\*)** plus a paternal GCA expansion. (richmond2020expandingtheutility pages 72-78)

The repeat alleles were transmitted by clinically unaffected heterozygous parents, supporting recessive inheritance. Variants are constitutional/germline; no somatic driver has been reported. (richmond2020expandingtheutility pages 72-78)

### Risk factors

- **Established genetic risk:** two pathogenic GLS alleles in trans.
- **Family history/consanguinity:** recurrence risk follows autosomal-recessive inheritance, but consanguinity was not documented in the retrieved case evidence.
- **Environmental, infectious, occupational, lifestyle, age, or sex risk factors:** none established.
- **Modifier genes, founder effects, anticipation, or germline mosaicism:** not established.

### Protective factors and gene–environment interaction

No protective allele, diet, exposure, or lifestyle factor has been demonstrated. Glutamine supplementation should **not** be extrapolated from glutamine-synthetase deficiency: GDPAG already features glutamine accumulation, and whether that accumulation is directly neurotoxic remains unresolved. The primary study explicitly noted that the contribution of elevated glutamine to the phenotype was unclear. (richmond2020expandingtheutility pages 78-83)

## 3. Phenotypes

Because only three index patients define the repeat-expansion syndrome, apparent “3/3” observations describe ascertainment-defining features and should not be interpreted as stable population frequencies.

| Phenotype | Type and course | Reported frequency | Suggested HPO term |
|---|---|---:|---|
| Global developmental delay | Neurodevelopmental sign; early onset | 3/3 in the defining series | **HP:0001263** Global developmental delay |
| Progressive ataxia | Neurologic sign; progressive/neurodegenerative course | 3/3 | **HP:0001251** Ataxia; additionally annotate progressive course in narrative |
| Elevated plasma glutamine | Laboratory abnormality | 3/3 | **HP:0003217** Hyperglutaminemia |
| Normal plasma glutamate | Relevant negative biochemical finding | Reported across the defining cases | Record as a negative observation rather than an HPO disease feature |

The review describes “early-onset delay in overall development, progressive ataxia and elevated glutamine plasma levels,” with unaltered plasma glutamate. (rumping2020inbornerrorsof pages 3-4)

**Severity and quality of life.** Progressive ataxia and developmental impairment are expected to compromise mobility, coordination, learning, communication, and independence, but no GDPAG-specific EQ-5D, SF-36, PROMIS, caregiver-burden, or activities-of-daily-living study has been published in the retrieved literature. Seizure frequency, behavior, speech, tone, ophthalmologic findings, hearing, dysmorphism, and growth cannot be assigned reliable frequencies from the available evidence.

## 4. Genetic and molecular information

### Gene/protein

- **Gene:** **GLS**; approved name *glutaminase*.
- **Ensembl:** **ENSG00000115419**. (OpenTargets Search: Global developmental delay, progressive ataxia, and elevated glutamine)
- **Protein/function:** phosphate-activated mitochondrial glutaminase; EC **3.5.1.2**.
- **Isoforms:** alternative splicing produces glutaminase C and kidney-type glutaminase; both are mitochondrial, with strong kidney-type glutaminase expression in cerebral cortex and kidney. (richmond2020expandingtheutility pages 78-83)

### Pathogenic alleles

The disease-associated expansion lies in the **5′UTR**, not in the protein-coding sequence. Repeat PCR estimated major expanded products of approximately **680**, **900**, and **1,500 GCA repeats** in the three probands. For Family 1, short-read analysis estimated >90 repeats without off-target reads and 246 with them, illustrating that short-read estimates substantially underresolve very large expansions. (richmond2020expandingtheutility pages 72-78)

The coding alleles were:

- **c.938C>T (p.Pro313Leu):** missense; experimentally associated with reduced enzyme function in the disease workflow.
- **c.923dupA (p.Tyr308\*):** frameshift/premature-termination allele as reported in the study text. (richmond2020expandingtheutility pages 72-78)

Clinical databases should retain the authors’ reported nomenclature while independently checking the transcript accession before importing HGVS strings. ClinVar accessions and current ACMG/AMP assertion statuses were not established by the retrieved evidence.

### Population frequency

Among **8,295 genomes/16,590 alleles**, the median repeat length was **14**, with modes at **8 and 16**. One individual carried an allele estimated at >90 repeats, corresponding to an expanded-allele frequency of **6.03×10⁻⁵** in that dataset. This is a locus-specific research estimate, not a validated carrier-frequency estimate, because short reads under-size large repetitive alleles. (richmond2020expandingtheutility pages 72-78)

### Functional consequence and epigenetics

Patient fibroblasts and peripheral-blood mononuclear cells showed reduced GLS activity/protein, reduced GLS mRNA, and allelic-expression imbalance. Residual activity remained and was proposed to explain the milder course relative to complete GLS ablation. (richmond2020expandingtheutility pages 78-83, richmond2020expandingtheutility pages 72-78)

The expansion produced an epigenetic **loss-of-expression** mechanism:

- no increased DNA methylation upstream or downstream of the repeat;
- reduced activating **H3 acetylation** and **H3K4me3**;
- enrichment of repressive **H3K9me3**;
- strongest chromatin effect in the proband with two expanded alleles. (richmond2020expandingtheutility pages 78-83)

Reporter constructs containing 13, 104, or approximately 240 repeats did not reproduce a direct inhibitory effect outside the native chromosomal context. This supports chromatin-mediated silencing rather than simple repeat-dependent blockade of transcription or translation. (richmond2020expandingtheutility pages 78-83)

No disease-specific modifier gene, methylation episignature, large chromosomal abnormality, or structural rearrangement beyond the separately reported GLS exon-1 duplication phenotype has been established.

## 5. Environmental information

GDPAG is a constitutional genetic disease. No toxin, radiation, pollution, occupation, smoking, alcohol, exercise, infection, or microbiome contribution is known. Environmental factors could influence general health or rehabilitation but are not established causes or modifiers. There is no zoonotic or transmissible component.

## 6. Mechanism and pathophysiology

### Causal chain

**Biallelic GLS pathogenic alleles** → 5′UTR expansion-associated repressive chromatin and/or coding-allele dysfunction → reduced mitochondrial GLS transcript, protein, and activity → impaired conversion of glutamine to glutamate plus ammonia → systemic glutamine accumulation and likely altered neuronal glutamate–glutamine cycling → impaired glutamatergic synaptic function and broader amino-acid/energy/redox metabolism → abnormal neurodevelopment and progressive cerebellar motor dysfunction. The steps through reduced activity and elevated plasma glutamine are directly supported; the exact causal contribution of brain glutamine accumulation versus local glutamate deficiency remains unresolved. (rumping2020inbornerrorsof pages 3-4, richmond2020expandingtheutility pages 78-83, richmond2020expandingtheutility pages 72-78)

### Biological processes and pathways

Relevant pathway annotations include glutamine catabolism, glutamate biosynthesis, glutaminolysis, neurotransmitter metabolism, the glutamate–glutamine cycle, nitrogen metabolism, TCA-cycle anaplerosis, GABA synthesis, glutathione metabolism, proline/ornithine metabolism, and nucleotide synthesis. GLS links glutamine to glutamate, which can feed α-ketoglutarate/TCA metabolism and serves as a precursor of GABA and glutathione. (rumping2020metabolicfingerprintingreveals pages 1-6)

**Suggested GO terms**

- **GO:0006543** glutamine catabolic process
- **GO:0006537** glutamate biosynthetic process
- **GO:0006536** glutamate metabolic process
- **GO:0006099** tricarboxylic acid cycle
- **GO:0006749** glutathione metabolic process
- **GO:0007268** chemical synaptic transmission
- **GO:0043209** myelin sheath, as an anatomical cellular component of interest rather than a demonstrated GDPAG lesion

**Subcellular localization:** mitochondrion/mitochondrial matrix are the key compartments; suggested GO cellular-component annotation is **GO:0005739 mitochondrion**. (richmond2020expandingtheutility pages 78-83)

### Cells and tissues

The most plausible vulnerable populations are glutamatergic neurons, cerebellar neurons including Purkinje cells, astrocytes participating in the glutamate–glutamine cycle, and neural progenitors. However, patient-specific single-cell or histopathologic evidence identifying one selectively affected cell type is unavailable. Suggested CL terms include **CL:0000540 neuron**, **CL:0000127 astrocyte**, **CL:0000121 Purkinje cell**, and **CL:0000679 glutamatergic neuron**; these should be labeled mechanistically suggested, not proven by patient tissue.

### Molecular profiling

The disease study used targeted expression, enzyme, stable-isotope flux, immunoblotting, and chromatin assays. No GDPAG-specific single-cell RNA-seq, spatial transcriptomics, broad patient proteomics, lipidomics, or integrated multi-omics dataset was identified. A separate hypermorphic-GLS HEK293 metabolomics model found **109 of 12,437** mass-spectral features corresponding to endogenous metabolites significantly affected by high GLS activity, but that experiment models the opposite biochemical direction and should not be imported as a GDPAG signature. (rumping2020metabolicfingerprintingreveals pages 1-6)

## 7. Anatomical structures affected

**Primary system:** central nervous system, particularly developmental and cerebellar motor networks.

**Suggested anatomy annotations:**

- brain — **UBERON:0000955**;
- cerebellum — **UBERON:0002037**;
- cerebral cortex — **UBERON:0000956**;
- kidney — biologically relevant because of GLS expression, but not established as clinically diseased in GDPAG;
- mitochondrion — principal subcellular compartment.

No consistent patient MRI pattern, pathology series, lateralization, peripheral-nerve lesion, or renal structural phenotype was available in the retrieved GDPAG evidence. Separate GLS-deficiency phenotypes have included cerebral edema/white-matter disease or cerebellar atrophy, but these should not be assigned automatically to GDPAG. (rumping2020inbornerrorsof pages 3-4)

## 8. Temporal development

Onset is pediatric/early developmental and apparently insidious rather than acute. Developmental delay is followed or accompanied by progressive ataxia, producing a chronic, lifelong neurodevelopmental-neurodegenerative course. Remission, episodic crises, stage boundaries, median progression rate, and critical therapeutic windows have not been defined. (rumping2020inbornerrorsof pages 3-4, richmond2020expandingtheutility pages 78-83)

A practical, nonvalidated staging description is:

1. **Early:** delayed acquisition of developmental milestones.
2. **Intermediate:** emergence of coordination/gait impairment.
3. **Advanced:** progressive motor disability.

This framework is inferential and should not be represented as an accepted clinical staging system.

## 9. Inheritance and population

Inheritance is **autosomal recessive**. For two carrier parents, standard Mendelian counseling gives a 25% affected, 50% carrier, and 25% non-carrier probability per pregnancy, assuming both parental alleles are correctly characterized.

Penetrance for biallelic pathogenic genotypes appears high in the reported families but cannot be quantified. Expressivity, anticipation, repeat instability across generations, sex ratio, age distribution, founder effects, geographic clustering, prevalence, and incidence are unknown. The reported expanded-allele frequency of 6.03×10⁻⁵ is not equivalent to disease prevalence or carrier frequency. (richmond2020expandingtheutility pages 72-78)

## 10. Diagnostics

### Clinical suspicion and biochemical testing

Consider GDPAG in a child with developmental delay plus progressive ataxia, particularly when plasma amino-acid analysis shows elevated glutamine without elevated glutamate. Recommended research-informed evaluation includes:

1. quantitative plasma amino acids, especially glutamine and glutamate;
2. ammonia, acid–base status, liver function, lactate, and broader metabolic screening to exclude common causes of hyperglutaminemia;
3. neurologic examination and standardized developmental assessment;
4. brain MRI, although no GDPAG-specific radiologic criterion exists;
5. GLS activity/flux and protein/expression assays in fibroblasts or PBMCs where available. (rumping2020inbornerrorsof pages 3-4, richmond2020expandingtheutility pages 72-78)

### Genetic testing algorithm

1. **Sequence GLS coding exons and splice junctions**, preferably as part of trio exome/genome analysis.
2. If one or no GLS coding allele is found despite the biochemical phenotype, perform **GLS 5′UTR GCA-repeat testing**.
3. Suitable methods include repeat-primed PCR, repeat-flanking PCR with gel/capillary sizing, Southern blot or validated long-read sequencing for very large alleles.
4. Short-read WGS with ExpansionHunter or comparable software can flag the expansion, but exact sizing may be unreliable; the original workflow required manual read inspection and off-target-read analysis.
5. Confirm parental phase to demonstrate biallelic inheritance. (shu2023thepowerof pages 7-8, richmond2020expandingtheutility pages 72-78)

Standard exome sequencing can miss the noncoding expansion. The 2023 review states: “Initial ES only uncovered one heterozygous and damaging variant in GLS in two probands,” whereas short-read genome sequencing identified the 5′UTR expansions. (shu2023thepowerof pages 7-8)

CMA, karyotyping, FISH, mtDNA sequencing, and generic repeat-expansion panels are not first-line confirmatory tests unless needed for the broader differential. RNA/cDNA allelic-expression analysis and chromatin assays are useful research-level functional tests, not standardized clinical criteria.

### Differential diagnosis

Key alternatives include urea-cycle disorders and hepatic hyperammonemia; glutamine synthetase deficiency; SLC38A3-related developmental and epileptic encephalopathy; other GLS-associated encephalopathies; mitochondrial disease; treatable metabolic ataxias; and nonmetabolic hereditary ataxias. Distinguishing GDPAG features are the GLS genotype, reduced glutaminase function, persistent hyperglutaminemia, and progressive ataxia.

There are no validated clinical diagnostic criteria, newborn-screening program, or established population-screening assay.

## 11. Outcome and prognosis

No Kaplan–Meier survival analysis, life-expectancy estimate, mortality rate, or 5-/10-year outcome data exist for GDPAG. Residual enzyme activity was proposed to account for a milder phenotype than complete GLS ablation, but no validated genotype–prognosis relationship is available. (richmond2020expandingtheutility pages 78-83)

Expected morbidity centers on developmental disability and progressive loss of coordination/mobility. Published GDPAG-specific evidence does not quantify wheelchair dependence, feeding support, respiratory complications, educational attainment, adult independence, or caregiver burden. Recovery has not been documented; stabilization with supportive therapy has not been systematically studied. Candidate monitoring biomarkers are plasma glutamine and cell-based GLS activity, but neither is validated as a prognostic surrogate.

## 12. Treatment and current applications

There is **no approved disease-modifying therapy** and no relevant GDPAG clinical trial identified. Oncology trials of GLS inhibitors are mechanistically inappropriate for a GLS-deficiency disorder and must not be misclassified as therapeutic GDPAG studies. (OpenTargets Search: Global developmental delay, progressive ataxia, and elevated glutamine)

### Present clinical management

Management is supportive and individualized:

- developmental pediatrics and neurology follow-up;
- physical therapy for balance, gait, strength, contracture prevention, and assistive-device assessment;
- occupational therapy for activities of daily living;
- speech/language therapy and augmentative communication where needed;
- nutritional assessment and safe-swallow evaluation if indicated;
- treatment of seizures, spasticity, pain, sleep problems, or orthopedic complications if they occur;
- periodic plasma amino-acid monitoring, recognizing that no treatment target is validated.

Suggested MAXO annotations include **MAXO:0000011 physical therapy**, **MAXO:0000010 occupational therapy**, speech-language therapy, developmental assessment, genetic counseling, biochemical surveillance, and assistive-device use; local ontology versions should be checked before production import.

### Experimental concepts

Potential future strategies include GLS gene replacement, activation of the silenced expanded allele, epigenome editing, or repeat-targeted approaches. None has reached a GDPAG preclinical efficacy study or human trial. Because GLS participates in neurotransmission, redox balance, and systemic metabolism, both under-correction and overactivation could be harmful; the distinct hypermorphic GLS syndrome demonstrates this dosage sensitivity. (rumping2020inbornerrorsof pages 3-4, rumping2020metabolicfingerprintingreveals pages 1-6, richmond2020expandingtheutility pages 78-83)

## 13. Prevention

The disease is not preventable through vaccination, diet, or lifestyle. Evidence-based prevention is reproductive/genetic rather than environmental:

- cascade testing of relatives after defining the familial alleles;
- carrier testing that includes the 5′UTR repeat, not coding sequencing alone;
- prenatal diagnosis using chorionic-villus or amniotic-fluid DNA;
- preimplantation genetic testing for monogenic disease;
- counseling regarding autosomal-recessive recurrence.

Secondary/tertiary prevention consists of early diagnosis, developmental intervention, fall prevention, mobility support, and surveillance for complications. No newborn-screening recommendation or prophylactic medication exists.

## 14. Other species and natural disease

No naturally occurring GLS-related GDPAG has been established in companion animals, livestock, or wildlife, and no breed/VBO association is known. The disorder is noninfectious and has no zoonotic potential. Orthologous GLS biology is conserved in vertebrates, supporting comparative modeling, but induced models should not be represented as natural veterinary disease.

## 15. Model organisms

### Zebrafish

Knockdown of **glsa**, **glsl**, or both caused smaller body size, body curvature, and cardiac edema. This supports developmental dependence on GLS but does not specifically reproduce the human triad or the 5′UTR chromatin lesion. (richmond2020expandingtheutility pages 72-78)

### Mouse

Cited mouse studies indicate that complete Gls ablation partially impairs glutamatergic synaptic transmission and causes early death from respiratory dysfunction, whereas heterozygous deficiency produces hippocampal hypoactivity. These findings support a dosage-sensitive role in neuronal transmission and respiration but model more severe or carrier states rather than the residual-activity human GDPAG genotype. (richmond2020expandingtheutility pages 78-83)

### Human cells

Patient fibroblasts and PBMCs reproduce reduced mRNA/protein/activity, altered glutamine-to-glutamate flux, allelic imbalance, and expansion-associated chromatin repression. Attempts to generate neuronal cells from patient fibroblasts were unsuccessful, limiting direct study of human neuronal pathophysiology. (richmond2020expandingtheutility pages 78-83, richmond2020expandingtheutility pages 72-78)

Useful future models include isogenic repeat-expanded iPSCs, induced glutamatergic neurons, cerebellar/Purkinje organoids, repeat-length knock-in mice, and CRISPR-corrected rescue lines.

## Recent developments and evidence appraisal

The most relevant 2023–2024 development is diagnostic rather than therapeutic. A 2023 review used GDPAG as a paradigm showing that phenotype-plus-biochemistry can direct genome analysis toward pathogenic noncoding variants missed by exome sequencing. (shu2023thepowerof pages 7-8)

Recent GLS literature has also broadened the allelic spectrum, including 2024 reports of coding-variant developmental/epileptic encephalopathy and mechanistically distinct de novo GLUL/GLS-pathway disorders; these developments reinforce the need to classify disease by **variant mechanism and biochemical direction**, rather than treating all glutamine-pathway phenotypes as interchangeable. However, no 2023–2024 publication retrieved here materially expanded the GDPAG repeat-expansion cohort, established prevalence, or tested treatment.

## Key source notes, dates, URLs, and quotations

1. **Rumping et al., “Inborn errors of enzymes in glutamate metabolism,” Journal of Inherited Metabolic Disease, published November 2020.** DOI/URL: https://doi.org/10.1002/jimd.12180. Disease-specific review statement: “Three other unrelated patients with GLS deficiency, as a consequence of tandem repeat expansion in GLS, presented with early-onset delay in overall development, progressive ataxia and elevated glutamine plasma levels.” It further reports that plasma glutamate was unaltered. PMID was not available in the retrieved record. (rumping2020inbornerrorsof pages 3-4)

2. **Shu, Maroilley & Tarailo-Graovac, “The Power of Clinical Diagnosis for Deciphering Complex Genetic Mechanisms in Rare Diseases,” Genes, published January 2023.** DOI/URL: https://doi.org/10.3390/genes14010196. Exact retrieved text: “Kuilenburg et al. identified GCA-REs in the 5′UTR region of the GLS by SR-GS. Initial ES only uncovered one heterozygous and damaging variant in GLS in two probands who presented with global developmental delay, progressive ataxia, and elevated glutamine (GDPAG; OMIM #618412).” PMID was not present in the retrieved record. (shu2023thepowerof pages 7-8)

3. **Richmond, “Expanding the utility of whole genome sequencing in the diagnosis of rare genetic disorders,” University of British Columbia thesis/ArXiv, January 2020.** DOI/URL: https://doi.org/10.14288/1.0394775. This retrieved full text supplied the detailed repeat sizes, population analysis, functional assays, and chromatin mechanism. Its conclusion states: “The expansion in the 5′ untranslated region of GLS, which encodes glutaminase, results in reduced expression and glutaminase deficiency.” This is not a peer-reviewed primary journal article and has no PMID; it is therefore best treated as detailed supporting primary-study documentation. (richmond2020expandingtheutility pages 78-83, richmond2020expandingtheutility pages 72-78)

4. **Rumping et al., “Metabolic fingerprinting reveals extensive consequences of GLS hyperactivity,” BBA—General Subjects, accepted November 4, 2019 and published in the 2020 volume.** DOI/URL: https://doi.org/10.1016/j.bbagen.2019.129484. This is mechanistically informative but models GLS hyperactivity, not GDPAG deficiency. (rumping2020metabolicfingerprintingreveals pages 1-6)

## Knowledge-base conclusions

The high-confidence entry is: **GDPAG (OMIM 618412) is an autosomal-recessive GLS loss-of-function disorder characterized by early developmental delay, progressive ataxia, and hyperglutaminemia. Large 5′UTR GCA expansions silence GLS through repressive histone remodeling and can occur homozygously or in trans with a coding pathogenic allele.** Diagnosis requires biochemical phenotyping plus explicit repeat-expansion analysis because standard exome sequencing may miss the causal allele. All broader phenotype frequencies, natural-history estimates, imaging signatures, epidemiology, prognosis, and disease-modifying treatments remain insufficiently characterized.

References

1. (rumping2020inbornerrorsof pages 3-4): Lynne Rumping, Esmee Vringer, Roderick H. J. Houwen, Peter M. van Hasselt, Judith J. M. Jans, and Nanda M. Verhoeven‐Duif. Inborn errors of enzymes in glutamate metabolism. Journal of Inherited Metabolic Disease, 43:200-215, Nov 2020. URL: https://doi.org/10.1002/jimd.12180, doi:10.1002/jimd.12180. This article has 33 citations and is from a peer-reviewed journal.

2. (richmond2020expandingtheutility pages 72-78): Phillip Andrew Richmond. Expanding the utility of whole genome sequencing in the diagnosis of rare genetic disorders. ArXiv, Jan 2020. URL: https://doi.org/10.14288/1.0394775, doi:10.14288/1.0394775. This article has 0 citations.

3. (richmond2020expandingtheutility pages 78-83): Phillip Andrew Richmond. Expanding the utility of whole genome sequencing in the diagnosis of rare genetic disorders. ArXiv, Jan 2020. URL: https://doi.org/10.14288/1.0394775, doi:10.14288/1.0394775. This article has 0 citations.

4. (shu2023thepowerof pages 7-8): Li Shu, Tatiana Maroilley, and Maja Tarailo-Graovac. The power of clinical diagnosis for deciphering complex genetic mechanisms in rare diseases. Genes, 14:196, Jan 2023. URL: https://doi.org/10.3390/genes14010196, doi:10.3390/genes14010196. This article has 9 citations.

5. (OpenTargets Search: Global developmental delay, progressive ataxia, and elevated glutamine): Open Targets Query (Global developmental delay, progressive ataxia, and elevated glutamine, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (rumping2020metabolicfingerprintingreveals pages 1-6): Lynne Rumping, Mia L. Pras-Raves, Johan Gerrits, Yuen Fung Tang, Marcel A. Willemsen, Roderick H.J. Houwen, Gijs van Haaften, Peter M. van Hasselt, Nanda M. Verhoeven-Duif, and Judith J.M. Jans. Metabolic fingerprinting reveals extensive consequences of gls hyperactivity. Mar 2020. URL: https://doi.org/10.1016/j.bbagen.2019.129484, doi:10.1016/j.bbagen.2019.129484. This article has 10 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Global_Developmental_Delay_Progressive_Ataxia_and_Elevated_Glutamine-deep-research-falcon_artifacts/artifact-00.md)