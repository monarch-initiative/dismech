---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-07-31T23:35:09.018795'
end_time: '2026-07-31T23:42:02.309401'
duration_seconds: 413.29
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Early-Infantile Developmental and Epileptic Encephalopathy
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 21
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Early-Infantile_Developmental_and_Epileptic_Encephalopathy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Early-Infantile Developmental and Epileptic Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Early-Infantile Developmental and Epileptic Encephalopathy** covering all of the
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
- **Disease Name:** Early-Infantile Developmental and Epileptic Encephalopathy
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Early-Infantile Developmental and Epileptic Encephalopathy** covering all of the
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


# Early-Infantile Developmental and Epileptic Encephalopathy (EIDEE): Research Report

**Evidence cut-off:** emphasis on literature published through 2024. **Scope caution:** EIDEE is an electroclinical syndrome/class, not one Mendelian disorder. Gene-numbered historical “EIEE” OMIM entries are separate gene-defined diseases and should not be conflated with the umbrella syndrome.

## Executive summary

Early-infantile developmental and epileptic encephalopathy is a severe, etiologically heterogeneous epilepsy beginning at or before 3 months of age, accompanied by abnormal EEG activity and impaired development. Contemporary terminology subsumes much of the historical Ohtahara/early-infantile epileptic-encephalopathy spectrum, but not every infant with early seizures has EIDEE: acute provoked neonatal seizures, self-limited genetic neonatal epilepsy, vitamin-responsive epilepsy, structural epilepsy, and infection must be distinguished.

The strongest recent EIDEE-specific dataset is a 2023 prospective cohort of 80 children. Median seizure onset was 28 days; an etiology was established in 83%, comprising genetic 50%, structural 19%, vitamin-responsive metabolic 14%, and unknown 17%. Molecular diagnosis was obtained in 53/77 tested children (69%); 60% remained drug-resistant, 71% had severe developmental delay/intellectual disability, and 14% died during mean 30-month follow-up. These figures are referral-cohort estimates, not population prevalence. (agarwala2023earlyinfantiledevelopmentaland pages 4-6, agarwala2023earlyinfantiledevelopmentaland pages 1-3)

A database-ready synopsis is provided below.

| domain | key findings/values | suggested ontology identifiers | evidence/source |
|---|---|---|---|
| Disease definition/scope | Early-infantile developmental and epileptic encephalopathy (EIDEE) refers to DEEs with seizure onset by **3 months** of age; modern usage encompasses historical early infantile epileptic encephalopathy / Ohtahara-spectrum terminology and emphasizes combined developmental impairment plus epileptic encephalopathy. | MONDO: **requires registry verification**; MeSH: **requires registry verification**; ICD-10/11: **requires registry verification**; HPO candidate terms: Seizure onset in infancy **HP:0002373** (verify), Developmental regression/delay terms **require verification** | (scheffer2024developmentalandepileptic pages 34-39, agarwala2023earlyinfantiledevelopmentaland pages 1-3) |
| Cohort demographics | Prospective EIDEE cohort: **80 children**, male:female **1.5:1**, median seizure onset **28 days** (range **1–90**), mean follow-up **30 months**. | NCIT/phenotype ontology not essential; Age of onset ontology terms **require verification** | (agarwala2023earlyinfantiledevelopmentaland pages 4-6, agarwala2023earlyinfantiledevelopmentaland pages 1-3) |
| Etiologic distribution | Confirmed etiology in **66/80 (83%)**: **genetic 50%**, **structural 19%**, **metabolic 14%** (all vitamin-responsive), **unknown 17%**. | MONDO disease grouping **requires verification**; HPO: Abnormality of metabolism / structural brain abnormality terms **require verification** | (agarwala2023earlyinfantiledevelopmentaland pages 1-3) |
| Seizure/EEG phenotype | Common seizure types included **clonic, tonic, myoclonic**; EEG: **burst-suppression 42%**, **multifocal discharges 30%**, **hypsarrhythmia 13%**. | HPO candidates: Burst suppression on EEG **HP:0010849** (verify); Hypsarrhythmia **HP:0002521** (verify); Myoclonic seizure **HP:0002123** (verify); Tonic seizure **HP:0002069** (verify); Clonic seizure **HP:0002266** (verify) | (agarwala2023earlyinfantiledevelopmentaland pages 4-6) |
| Neurodevelopmental/behavioral phenotype | Genetic/unknown etiologies showed more severe neurodevelopmental burden than vitamin-responsive/structural groups: severe DD/ID **OR 57**, autistic behaviors **OR 37**, tone abnormalities **OR 9**, movement disorder **OR 19**. | HPO candidates: Global developmental delay **HP:0001263** (verify); Intellectual disability **HP:0001249** (verify); Autism **HP:0000717** (verify); Abnormality of muscle tone **HP:0003808** (verify); Movement disorder **HP:0100022** (verify) | (agarwala2023earlyinfantiledevelopmentaland pages 1-3, agarwala2023earlyinfantiledevelopmentaland pages 8-10) |
| MRI/metabolic findings | MRI abnormal in **35/80 (44%)**; among abnormal MRIs, **16/35** had malformations and **19/35** nonspecific changes. Metabolic testing diagnostic in **3/41**, all **biotinidase deficiency** in the prospective cohort summary. | UBERON brain **UBERON:0000955**; HPO candidate: Abnormal brain MRI **HP:0012443** (verify); Biotinidase deficiency disease ontology **requires verification** | (agarwala2023earlyinfantiledevelopmentaland pages 4-6, agarwala2023earlyinfantiledevelopmentaland pages 1-3) |
| Outcomes/prognosis | At follow-up: **71%** had severe developmental delay/intellectual disability, **60%** remained drug-resistant, **14%** died. Vitamin-responsive etiologies had the best probability of seizure control; only vitamin-responsive etiology had significant positive effect on seizure control (**P=0.02**). | HPO candidates: Drug resistant epilepsy **requires verification**; Severe global developmental delay **requires verification**; Mortality not typically HPO-coded | (agarwala2023earlyinfantiledevelopmentaland pages 4-6, agarwala2023earlyinfantiledevelopmentaland pages 1-3) |
| Genetic architecture | DEEs are highly heterogeneous; 2024 review notes **~50%** of DEE patients overall receive a molecular diagnosis, and by 2023 **825 DEE-associated genes** were cataloged among **925 monogenic epilepsy genes**. | HGNC gene symbols as listed; MONDO/GENO mappings **require verification** | (scheffer2024developmentalandepileptic pages 9-11, scheffer2024developmentalandepileptic pages 19-21) |
| Major mechanism class: ion channelopathies | Representative early-infantile DEE genes include **SCN1A, SCN2A, SCN3A, SCN8A, KCNQ2, KCNT1, SCN1B, nicotinic receptor genes**. Functional direction matters: **GOF** variants may benefit from inhibitory/channel-blocking strategies; **LOF** variants may require augmentation approaches. | GO: ion transmembrane transport **GO:0034220**; GO: regulation of membrane potential **GO:0042391**; CL terms for excitatory/inhibitory neurons **require verification** | (specchio2024theexpandingfield pages 8-11, scheffer2024developmentalandepileptic pages 19-21, specchio2024theexpandingfield pages 6-8) |
| Representative gene-mechanism examples | **SCN2A GOF** → neonatal-onset epilepsy, often responsive to sodium-channel blockers; **SCN2A LOF** → later-onset generalized seizures/poorer response. **SCN8A GOF** can cause infantile epilepsies/DEE. **KCNT1 GOF** increases current; quinidine has variable benefit. **KCNQ2** is a key early-infantile potassium-channel DEE gene. | HGNC: SCN2A, SCN8A, KCNT1, KCNQ2; GO annotations above; variant mechanism ontology **requires verification** | (specchio2024theexpandingfield pages 8-11, scheffer2024developmentalandepileptic pages 19-21) |
| Synaptic/synaptopathy mechanisms | Synaptopathies are a major DEE class; **STXBP1** was the most common single-gene diagnosis in the prospective EIDEE cohort (**5 patients**). DEE mechanisms include disrupted **SNARE machinery**, synaptic scaffolds, and post-synaptic receptor dysfunction. | HGNC: STXBP1; GO: synaptic vesicle exocytosis **GO:0016079**; GO: chemical synaptic transmission **GO:0007268** | (agarwala2023earlyinfantiledevelopmentaland pages 1-3, scheffer2024developmentalandepileptic pages 34-39) |
| Other mechanism classes | Additional DEE mechanisms include **mTOR-pathway dysregulation** (e.g., **DEPDC5** negative regulator; second-hit/somatic LOH in focal cortical dysplasia), **ubiquitination/post-translational pathways** (e.g., **UBA5, KLHL20, WWOX**), transporter dysfunction, and transcriptional/epigenetic regulation abnormalities. | GO: TOR signaling **GO:0031929**; GO: protein ubiquitination **GO:0016567**; GO: regulation of transcription **GO:0006355**; CL/UBERON terms **require verification** | (specchio2024theexpandingfield pages 8-11, scheffer2024developmentalandepileptic pages 9-11, scheffer2024developmentalandepileptic pages 34-39) |
| Cell/tissue emphasis | Reviews highlight dysfunction in **cortical/telencephalic parvalbumin-positive inhibitory interneurons** in some sodium-channel DEEs, alongside roles for excitatory neurons and glia. | CL: parvalbumin-positive interneuron **requires verification**; UBERON: cerebral cortex **UBERON:0000956** (verify); GO CC plasma membrane **GO:0005886** | (scheffer2024developmentalandepileptic pages 19-21, specchio2024theexpandingfield pages 6-8) |
| Diagnostic workflow | Recommended workup: **video-EEG**, **3T epilepsy-protocol brain MRI**, early blood/urine metabolic testing, CSF studies when indicated, and rapid genomic testing. Genetic strategy commonly starts with **CMA** for CNVs then **NGS/exome**; **genome sequencing** is entering practice. High-depth methods may be needed for mosaicism. | LOINC/NCIT assay codes **require verification**; HPO/UBERON as above | (scheffer2024developmentalandepileptic pages 11-13, scheffer2024developmentalandepileptic pages 13-15, nguyen2024genotypedriventherapeuticsin pages 9-10, agarwala2023earlyinfantiledevelopmentaland pages 1-3) |
| Diagnostic yield data | In the EIDEE cohort, molecular diagnosis in **53/77 (69%)** tested; **NGS yield 51%**, **microarray yield 14%**. A 2024 review cites pathogenic variants identified in ~**50%** of DEE patients overall. Rapid genome sequencing in infants <1 year with seizures found genetic etiology in **46%** with median **37 days** to diagnosis. | CMA/exome/genome ontology identifiers **require verification** | (agarwala2023earlyinfantiledevelopmentaland pages 1-3, scheffer2024developmentalandepileptic pages 11-13, scheffer2024developmentalandepileptic pages 9-11) |
| Treatable mimics / metabolic-vitamins | Early evaluation should prioritize **treatable and vitamin-responsive epilepsies**. Reported empiric trials include **pyridoxine, pyridoxal 5'-phosphate, folinic acid, biotin**; vitamin-responsive etiologies had the most favorable seizure-control outcomes in the prospective cohort. | CHEBI/DrugBank IDs **require verification**; NCIT intervention terms for pyridoxine/biotin/folinic acid **require verification** | (scheffer2024developmentalandepileptic pages 13-15, agarwala2023earlyinfantiledevelopmentaland pages 1-3) |
| Genotype-guided pharmacotherapy | Sodium-channel blockers may be effective in selected **GOF** channelopathies; cohort examples with benefit included **SCN1A, KCNQ2, FGF12, SCN8A, SCN2A** (6 patients total). **Quinidine** benefited one **KCNT1** patient in the cohort. | NCIT: Carbamazepine/Phenytoin/Lacosamide/Quinidine **require verification**; CHEBI drug IDs **require verification** | (agarwala2023earlyinfantiledevelopmentaland pages 8-10, specchio2024theexpandingfield pages 8-11, scheffer2024developmentalandepileptic pages 13-15) |
| Important cautions | Precision treatment must consider direction of effect. In **Dravet syndrome / SCN1A LOF**, **carbamazepine/oxcarbazepine** can worsen seizures and should be avoided, whereas sodium-channel blockers may help some **SCN2A/SCN8A/KCNQ2 GOF** cases. | NCIT drug terms **require verification**; disease-specific MONDO IDs **require verification** | (scheffer2024developmentalandepileptic pages 9-11, specchio2024theexpandingfield pages 8-11) |
| Diet therapy | **Ketogenic diet** is used for ASM-resistant DEE and was described as an early treatment option in genotype-driven DEE management; one 2024 cohort/review context reported approximately **30% seizure freedom** and **60% >50% seizure reduction** in young patients with EIDEE/related DEEs. | NCIT: Ketogenic Diet **requires verification** | (nguyen2024genotypedriventherapeuticsin pages 9-10) |
| Surgery/interventional care | For **unifocal resectable structural lesions** (e.g., focal cortical dysplasia), epilepsy surgery evaluation is recommended and can be transformational. | NCIT: Epilepsy surgery **requires verification**; UBERON lesion-specific anatomy **requires verification** | (scheffer2024developmentalandepileptic pages 11-13) |
| Supportive/holistic care | Holistic care is necessary because long-term developmental outcomes are often abnormal despite seizure treatment; common needs include management of **motor dysfunction, psychiatric features, speech and sleep problems**, developmental therapies, and family support. | HPO candidates: Sleep disturbance / speech delay / motor delay **require verification**; NCIT rehab/supportive care terms **require verification** | (scheffer2024developmentalandepileptic pages 9-11) |
| Inheritance/counseling | In the EIDEE cohort’s pathogenic variants, **67% autosomal dominant** and **33% autosomal recessive** inheritance were reported. High-depth sequencing detects parental mosaicism; one review reported mosaicism in **8%** of apparently de novo cases, relevant to recurrence-risk counseling and prenatal/IVF options. | GENO inheritance terms **require verification** | (agarwala2023earlyinfantiledevelopmentaland pages 4-6, scheffer2024developmentalandepileptic pages 13-15) |
| Experimental therapies | Emerging precision therapies include **antisense oligonucleotides (ASOs)** and gene-augmentation/activation strategies. Examples from DEE reviews: **STK-001** for SCN1A/Dravet (TANGO strategy), exploratory **SCN2A ASO** approaches, and AAV-mediated gene therapy concepts. | NCIT: Antisense oligonucleotide therapy / Gene therapy **require verification** | (specchio2024theexpandingfield pages 8-11, scheffer2024developmentalandepileptic pages 17-19, specchio2024theexpandingfield pages 27-29) |
| Experimental models | Model systems cited across DEE reviews include **mouse**, **iPSC-derived neurons**, and other preclinical platforms. Dravet/iPSC data show selective impairment of inhibitory neurons; mouse models demonstrated rescue with **AAV-SCN1A**, **CRISPRa/dCas9 activation**, and cell-selective GABAergic targeting. | CL: induced pluripotent stem cell-derived neuron **requires verification**; NCBITaxon mouse **NCBITaxon:10090**; GO/CL interneuron terms **require verification** | (specchio2024theexpandingfield pages 27-29, scheffer2024developmentalandepileptic pages 19-21, specchio2024theexpandingfield pages 14-17) |
| Real-world implementation / trial landscape | Active interventional DEE trials retrieved included **NCT07019922** (elsunersen in pediatric SCN2A-DEE, recruiting), **NCT05737784** (PRAX-222 in early-onset SCN2A-DEE, recruiting), **NCT04639310** / **NCT04912856** (XEN496/ezogabine in KCNQ2-DEE, terminated), **NCT06983158** (CAP-002 gene therapy for STXBP1 encephalopathy, terminated), and broad DEE programs such as **relutrigine NCT07010471** and **LP352 NCT06719141/NCT06908226**. | ClinicalTrials.gov NCT identifiers as listed; NCIT interventions **require verification** | Retrieved clinical trial records in prior tool output; narrative support from (specchio2024theexpandingfield pages 8-11, scheffer2024developmentalandepileptic pages 17-19) |


*Table: This table summarizes core disease-definition, cohort, mechanistic, diagnostic, therapeutic, and translational findings for Early-Infantile Developmental and Epileptic Encephalopathy. It is formatted for direct knowledge-base curation and flags ontology identifiers that require external registry verification.*

## 1. Disease information

### Definition and nomenclature

EIDEE denotes a developmental and epileptic encephalopathy with seizure onset **by 3 months**, developmental impairment attributable both to the underlying cause and potentially to epileptic activity, and a markedly abnormal EEG. Frequent seizures, including tonic, clonic, myoclonic, focal, and epileptic spasms, are typical. Burst suppression is characteristic but not obligatory; multifocal discharges or hypsarrhythmia may occur. (agarwala2023earlyinfantiledevelopmentaland pages 4-6, scheffer2024developmentalandepileptic pages 34-39)

**Synonyms/related terms:** early-infantile DEE; early infantile developmental and epileptic encephalopathy; neonatal-onset DEE; historical early infantile epileptic encephalopathy; Ohtahara syndrome; early myoclonic encephalopathy. The latter historical syndromes overlap the modern category but should remain searchable synonyms rather than exact equivalents in every record.

**Identifiers:** a single stable umbrella MONDO/OMIM/Orphanet identifier could not be verified from the retrieved primary literature. OMIM mainly represents gene-specific EIEE-numbered entities. ICD-10-CM generally codes the manifestations under epilepsy/epileptic encephalopathy rather than providing a sufficiently specific EIDEE code. ICD-11 and current MONDO entries should therefore be validated directly against the release used by the target knowledge base. MeSH indexing generally falls under *Epileptic Encephalopathies*.

The evidence summarized here is **aggregated disease-level evidence** from cohorts and reviews, not individual EHR data. Individual case/trial observations are identified as such.

## 2. Etiology, risk, and protective factors

EIDEE is a final common phenotype rather than a single genetic disease. In the 2023 cohort, causes were genetic in 50%, structural in 19%, vitamin-responsive metabolic in 14%, and unresolved in 17%. Relevant structural causes include malformations of cortical development and acquired neonatal injuries such as hypoxic–ischemic injury, stroke, infection, hypoglycemia, or trauma. (agarwala2023earlyinfantiledevelopmentaland pages 1-3, scheffer2024developmentalandepileptic pages 34-39)

### Genetic risk

Major mechanistic groups include:

- **Ion-channel disorders:** *SCN1A, SCN2A, SCN3A, SCN8A, SCN1B, KCNQ2, KCNB1, KCNT1, KCNA2,* and calcium/receptor-channel genes.
- **Synaptic-vesicle and synaptic-signaling disorders:** *STXBP1, DNM1, SNAP25, NECAP1, NBEA,* and glutamate/GABA-receptor genes.
- **Kinase/transcription/chromatin disorders:** *CDKL5, CSNK2B, ARX, FOXG1, CHD2* and related regulators.
- **mTOR/cortical-malformation disorders:** *TSC1, TSC2, DEPDC5, NPRL2, NPRL3, MTOR* and mosaic PI3K–AKT–mTOR-pathway variants.
- **Transport/metabolic/mitochondrial disorders:** *SLC2A1, SLC6A1, ATP1A3, ALDH7A1, PNPO, BTD, POLG* and mitochondrial genes.
- **Ubiquitination/cellular-homeostasis disorders:** biallelic *UBA5* and *WWOX*, and dominant *KLHL20*. (specchio2024theexpandingfield pages 8-11, scheffer2024developmentalandepileptic pages 9-11, scheffer2024developmentalandepileptic pages 19-21, specchio2024theexpandingfield pages 1-6)

Variants may be missense, nonsense, frameshift, splice-altering, copy-number, structural, or mosaic. Most severe dominant channel/synaptic DEEs arise through germline **de novo** variants, whereas metabolic and several cellular-homeostasis disorders are autosomal recessive. X-linked disorders include *CDKL5* and *ARX*. In the 2023 cohort, 67% of pathogenic findings followed dominant and 33% recessive inheritance. (agarwala2023earlyinfantiledevelopmentaland pages 4-6)

Allele frequency must be assessed per variant in gnomAD and ClinVar; pathogenic dominant EIDEE variants are ordinarily absent or exceptionally rare in population databases. ACMG classification and functional direction must be recorded separately. A VUS is not diagnostic without segregation, phenotype, and/or functional evidence.

### Environmental, lifestyle, infectious, and protective factors

There is no established lifestyle exposure that causes the primary genetic syndrome, and no validated protective allele or diet that prevents it. Fever, infection, sleep deprivation, and metabolic stress can precipitate seizures in an affected child but are generally **triggers**, not causes. Prenatal/perinatal infection and hypoxic–ischemic injury are etiologic alternatives or structural causes. Inflammation may amplify channelopathy phenotypes in experimental systems, but a general human gene–environment model is not established. (specchio2024theexpandingfield pages 14-17)

## 3. Phenotypes and quality-of-life impact

The 80-child prospective cohort reported burst suppression in 42%, multifocal discharges in 30%, and hypsarrhythmia in 13%. Severe DD/ID affected 71% at follow-up. Relative to structural/vitamin-responsive cases, genetic/unknown cases had much higher odds of severe DD/ID (OR 57), autistic behavior (OR 37), tone abnormalities (OR 9), and movement disorder (OR 19). (agarwala2023earlyinfantiledevelopmentaland pages 4-6, agarwala2023earlyinfantiledevelopmentaland pages 1-3, agarwala2023earlyinfantiledevelopmentaland pages 8-10)

Suggested phenotype annotations include:

- early-infantile seizure onset; neonatal seizure; focal, tonic, clonic, myoclonic seizures; epileptic spasms;
- burst-suppression EEG, multifocal epileptiform discharges, hypsarrhythmia;
- global developmental delay (**HP:0001263**), intellectual disability (**HP:0001249**), developmental stagnation/regression;
- hypotonia, hypertonia/spasticity, dystonia, chorea, tremor, or other movement disorder;
- microcephaly, feeding/swallowing dysfunction, growth failure, cortical visual impairment;
- autistic behavior (**HP:0000729** should be registry-checked), sleep disturbance, absent or limited speech.

The burden is typically profound: frequent seizures and rescue-medication use, impaired mobility and communication, feeding/respiratory complications, disrupted sleep, repeated hospitalizations, and lifelong caregiver dependence. Formal EIDEE-specific EQ-5D/SF-36 norms were not found; generic pediatric quality-of-life instruments may underrepresent profound neurodisability.

## 4. Genetic and molecular information

Functional interpretation is essential because the **same gene can require opposite treatment** depending on variant effect:

- *SCN2A* gain-of-function (GOF) variants typically produce neonatal/early-infantile focal epilepsy and may respond to phenytoin, carbamazepine, or lacosamide; loss-of-function (LOF) more often causes later developmental phenotypes and should not automatically be treated the same way.
- *SCN8A* GOF increases Nav1.6-mediated excitability and can cause infantile DEE; LOF is associated with different, often later phenotypes.
- *SCN1A* haploinsufficiency impairs firing of GABAergic inhibitory interneurons in Dravet syndrome; sodium-channel blockers may worsen this LOF disorder. Rare *SCN1A* GOF phenotypes require separate interpretation.
- *KCNQ2* LOF reduces M-current, weakening neuronal repolarization and increasing excitability.
- *KCNT1* GOF increases sodium-activated potassium-channel current and causes severe early epilepsy; quinidine is mechanistically plausible but clinical efficacy and tolerability are inconsistent.
- *STXBP1* haploinsufficiency disrupts SNARE-mediated synaptic-vesicle release; it was the most frequent single-gene finding in the 2023 cohort (5 children).
- *DEPDC5* loss disinhibits mTORC1; a somatic second hit can generate focal cortical dysplasia. (agarwala2023earlyinfantiledevelopmentaland pages 1-3, specchio2024theexpandingfield pages 27-29, specchio2024theexpandingfield pages 8-11, scheffer2024developmentalandepileptic pages 19-21)

No syndrome-wide epigenetic signature is established. Chromatin-regulator genes can cause DEE, and somatic mosaicism is important in cortical malformations. CNVs are clinically relevant: microarray detected diagnoses in 14% of the EIDEE cohort, although broader DEE reviews estimate approximately 4% in less selected populations. (agarwala2023earlyinfantiledevelopmentaland pages 1-3, scheffer2024developmentalandepileptic pages 11-13)

## 5. Mechanism and pathophysiology

A generalized causal chain is:

**pathogenic variant/brain lesion/metabolic deficiency → altered neurodevelopment, synaptic release, receptor signaling, ion conductance, or energy metabolism → excitation–inhibition imbalance in immature cortical networks → recurrent seizures and epileptiform EEG activity → activity-dependent network injury layered upon the primary developmental defect → developmental stagnation/regression and neurological comorbidity.**

Upstream mechanisms include altered cortical progenitor development, neuronal migration, channel biophysics, SNARE release, transcription/chromatin regulation, and mTOR signaling. Downstream mechanisms include network hypersynchrony, excitotoxic/oxidative stress, sleep disruption, neuroinflammation, and impaired activity-dependent circuit maturation. The relative contribution of the primary developmental defect versus seizures differs by genotype. (scheffer2024developmentalandepileptic pages 34-39, specchio2024theexpandingfield pages 6-8, specchio2024theexpandingfield pages 1-6)

Suggested annotations include **GO:0042391 regulation of membrane potential**, **GO:0034220 ion transmembrane transport**, **GO:0007268 chemical synaptic transmission**, **GO:0016079 synaptic-vesicle exocytosis**, **GO:0031929 TOR signaling**, and **GO:0016567 protein ubiquitination**. Relevant cells include glutamatergic neurons, GABAergic interneurons—especially parvalbumin-positive interneurons in selected sodium channelopathies—radial/apical neural progenitors, and glia. Relevant compartments include plasma membrane/axon initial segment, presynaptic active zone and synaptic vesicle, postsynaptic membrane, nucleus/chromatin, mitochondrion, and lysosome. (scheffer2024developmentalandepileptic pages 19-21, specchio2024theexpandingfield pages 6-8)

Disease-wide transcriptomic, proteomic, metabolomic, lipidomic, single-cell, and spatial signatures are not sufficiently replicated for clinical annotation. Such findings are mainly gene-specific and preclinical.

## 6. Anatomy

The primary organ is the central nervous system, especially bilateral cerebral cortex and distributed thalamocortical networks. Structural subgroups may involve focal cortex, hippocampus, basal ganglia, cerebellum, or diffuse malformations. Suggested terms include **UBERON:0000955 brain** and **UBERON:0000956 cerebral cortex**. There is generally no fixed lateralization unless a focal malformation or stroke is causal. Secondary involvement includes musculoskeletal contractures from immobility/spasticity, aspiration-related respiratory disease, gastrointestinal feeding problems, impaired growth, and sleep/autonomic dysfunction.

## 7. Temporal development and natural history

Onset is neonatal or within the first three postnatal months and may be abrupt, with clusters, status epilepticus, or rapidly increasing seizure burden. In the 2023 cohort, 32.5% began within 7 days and median onset was 28 days. Evolution to infantile epileptic spasms syndrome or later multifocal/Lennox–Gastaut-like epilepsy may occur. The course is chronic and often drug-resistant rather than classically relapsing–remitting. Seizure remission does not guarantee developmental recovery because the genetic/structural disorder has independent developmental effects. (agarwala2023earlyinfantiledevelopmentaland pages 4-6)

Early infancy is the critical diagnostic and therapeutic period: treatable metabolic disease, resectable structural lesions, and mechanism-specific channel therapy should be identified before prolonged status epilepticus and disrupted circuit maturation.

## 8. Epidemiology, inheritance, and population

Robust population incidence or prevalence for the **umbrella EIDEE syndrome** is unavailable. A tertiary-center cohort cannot supply population prevalence. Syndrome-specific Scottish estimates cited in a 2024 review include CDKL5-DEE incidence of 2.36 per 100,000 live births and PCDH19 clustering epilepsy of 4.85 per 100,000, but these are not EIDEE-wide estimates. (scheffer2024developmentalandepileptic pages 34-39)

Both sexes are affected; sex ratios vary by gene. The 2023 cohort had a male:female ratio of 1.5:1, but this should not be generalized globally. X-linked disorders create gene-specific sex effects. No consistent ethnic/geographic predisposition is established; ascertainment and access to sequencing strongly affect reported distributions. (agarwala2023earlyinfantiledevelopmentaland pages 4-6)

Penetrance is often high for severe de novo variants but is gene/variant-specific. Expressivity is variable. Anticipation is not a general feature. Parental mosaicism was reported in approximately 8% of apparently de novo DEE cases when sensitive methods were used; recurrence risk can therefore exceed the conventional ~1% germline-mosaicism estimate. Recessive disease risk rises with consanguinity, and founder variants may be population-specific. (scheffer2024developmentalandepileptic pages 13-15)

## 9. Diagnosis

### Recommended workflow

1. **Stabilize and document seizures:** continuous or prolonged video-EEG is essential because neonatal seizures may be electrographic-only. Characterize background, burst suppression, multifocal activity, and spasms.
2. **Identify acquired causes urgently:** glucose, electrolytes, calcium/magnesium, blood gas, CBC/cultures, infection testing, and assessment for hypoxic–ischemic injury, hemorrhage, stroke, or trauma.
3. **MRI:** 3-T epilepsy-protocol MRI, including diffusion and susceptibility sequences, to identify malformation, ischemia, hemorrhage, or focal cortical dysplasia. (scheffer2024developmentalandepileptic pages 11-13)
4. **Treatable metabolic testing:** ammonia, lactate/pyruvate, plasma amino acids, acylcarnitines, urine organic acids, biotinidase, and targeted CSF glucose, lactate, amino acids, and neurotransmitters when indicated. Prioritize *ALDH7A1*, *PNPO*, *BTD*, *SLC2A1*, mitochondrial and *POLG*-related disease. (scheffer2024developmentalandepileptic pages 13-15)
5. **Do not delay monitored vitamin trials** when appropriate: pyridoxine, pyridoxal-5′-phosphate, folinic acid, and biotin, with cardiorespiratory/EEG monitoring because pyridoxine can cause apnea. In the cohort, metabolic testing diagnosed biotinidase deficiency in 3/41 tested children, and all metabolic etiologies were vitamin-responsive. (agarwala2023earlyinfantiledevelopmentaland pages 1-3)
6. **Rapid trio exome or genome sequencing:** increasingly favored early because of high heterogeneity and time-sensitive treatment. Rapid genome sequencing in infants under one year with seizures found an etiology in 46% at median 37 days; overall NGS identifies about half of DEE. (scheffer2024developmentalandepileptic pages 9-11)
7. **CNV and mosaic analysis:** ensure exon-level CNV calling; use CMA if not captured or when dysmorphism/malformation suggests CNV. Consider deep sequencing, affected-tissue sequencing, or droplet-digital PCR for low-level mosaicism. (scheffer2024developmentalandepileptic pages 11-13)
8. **Reanalysis:** periodically reanalyze negative exome/genome data; consider mtDNA, repeat expansion, RNA sequencing, methylation signatures, or functional assays when phenotype directs. Karyotype/FISH is not first-line unless a cytogenetic rearrangement is suspected.

The prospective study’s exact abstract statement was: **“A molecular diagnosis was achieved in 53 out of 77 patients tested (69%). Next-generation sequencing had a yield of 51%, while microarray had a yield of 14%.”** (Publication: 14 September 2023; DOI URL: https://doi.org/10.1093/braincomms/fcad243.) (agarwala2023earlyinfantiledevelopmentaland pages 1-3)

### Differential diagnosis

Exclude acute symptomatic neonatal seizures, self-limited familial neonatal/infantile epilepsy, infantile epileptic spasms syndrome, epilepsy of infancy with migrating focal seizures, Dravet syndrome, glycine encephalopathy, pyridoxine/PNPO/folinic-acid-responsive epilepsy, biotinidase deficiency, GLUT1 deficiency, mitochondrial disease, congenital infection, autoimmune encephalitis, hypoxic–ischemic injury, stroke, and structural malformation. EEG pattern alone is not etiologic.

## 10. Outcomes and prognosis

In the 2023 prospective cohort, 60% remained drug-resistant, 71% had severe DD/ID, and 14% died over mean 30 months. Median time to seizure control was 3 days for vitamin-responsive disease versus 75 days structural, 80 days unknown, and 90 days genetic. Vitamin responsiveness was the only independently significant favorable seizure-control factor (P=0.02). (agarwala2023earlyinfantiledevelopmentaland pages 4-6, agarwala2023earlyinfantiledevelopmentaland pages 8-10)

Mortality mechanisms include status epilepticus, respiratory/aspiration complications, infection, underlying metabolic disease, and sudden unexpected death in epilepsy. There are no reliable syndrome-wide 5- or 10-year survival estimates. Favorable prognostic factors include an immediately treatable metabolic deficiency, a completely resectable lesion, and early mechanism-matched treatment. Severe neonatal EEG background abnormality, persistent status, profound early developmental impairment, and drug resistance generally indicate poorer outcomes.

## 11. Treatment and real-world implementation

### Acute and conventional treatment

Treat status epilepticus according to neonatal/pediatric protocols while pursuing etiology. Phenobarbital, levetiracetam, benzodiazepines, phenytoin/fosphenytoin, and other ASMs are selected according to seizure type, age, organ function, and suspected mechanism. No single ASM treats all EIDEE.

### Genotype/etiology-guided treatment

- **Vitamin-dependent epilepsy:** pyridoxine for *ALDH7A1*; pyridoxal-5′-phosphate for *PNPO*; folinic acid in selected responsive disorders; biotin for biotinidase deficiency.
- **SCN2A/SCN8A GOF and some KCNQ2 early-onset disease:** sodium-channel blockers may be unusually effective. Six genotype-guided responders in the 2023 cohort carried *SCN1A, KCNQ2, FGF12, SCN8A,* or *SCN2A* findings. (agarwala2023earlyinfantiledevelopmentaland pages 8-10, specchio2024theexpandingfield pages 8-11)
- **SCN1A-LOF/Dravet:** avoid maintenance carbamazepine and oxcarbazepine because seizure aggravation can occur; use syndrome-supported regimens such as valproate, clobazam, stiripentol, cannabidiol, and fenfluramine as clinically appropriate. (scheffer2024developmentalandepileptic pages 9-11)
- **KCNT1 GOF:** quinidine is experimental/off-label; one cohort child benefited, but ECG/QT and drug-interaction monitoring is mandatory and responses are variable. (agarwala2023earlyinfantiledevelopmentaland pages 8-10, specchio2024theexpandingfield pages 8-11)
- **mTORopathy:** everolimus has established evidence for tuberous-sclerosis-complex-associated seizures, not for EIDEE indiscriminately.
- **GLUT1 deficiency:** ketogenic diet is disease-targeted therapy.

The ketogenic diet is also used for drug-resistant EIDEE. A 2024 study reported approximately 30% seizure freedom and 60% achieving >50% seizure reduction in the relevant young-patient context, but these uncontrolled results should not be interpreted as a universal EIDEE response rate. (nguyen2024genotypedriventherapeuticsin pages 9-10)

For a unifocal, resectable lesion, early epilepsy-surgery assessment can be transformative. Palliative options for persistent generalized/multifocal disease include vagus-nerve stimulation, corpus callosotomy, and other neuromodulation, although EIDEE-specific comparative evidence is limited. (scheffer2024developmentalandepileptic pages 11-13)

Supportive care requires feeding/swallow assessment, nutrition and gastrostomy when needed, respiratory and sleep management, physiotherapy, occupational/speech/communication therapy, management of tone and movement disorders, vision/hearing services, rescue plans, SUDEP counseling, psychosocial support, and palliative-care involvement where appropriate. Suggested NCIT mappings include Anticonvulsant Therapy, Ketogenic Diet Therapy, Epilepsy Surgery, Vagus Nerve Stimulation, Physical Therapy, Occupational Therapy, Speech Therapy, Genetic Counseling, Antisense Oligonucleotide Therapy, and Gene Therapy; local NCIT concept codes should be release-verified.

## 12. 2023–2024 research developments and trials

The major conceptual advance is movement from gene-name prescribing toward **variant-mechanism prescribing**. The 2024 Lancet review emphasizes that GOF should generally be reduced, whereas LOF/haploinsufficiency may require transcript or gene augmentation. (specchio2024theexpandingfield pages 8-11, specchio2024theexpandingfield pages 6-8)

Emerging approaches include ASOs, AAV gene replacement, CRISPR activation, and stop-codon read-through. In mouse Dravet models, AAV-mediated *SCN1A* augmentation and dCas9/CRISPRa activation improved seizures and survival; cell-selective targeting of inhibitory neurons is particularly relevant. Patient-derived iPSC neurons demonstrate impaired inhibitory-neuron excitability in *SCN1A* disease. These are preclinical findings and do not establish routine efficacy. (specchio2024theexpandingfield pages 27-29, scheffer2024developmentalandepileptic pages 19-21, specchio2024theexpandingfield pages 14-17, scheffer2024developmentalandepileptic pages 17-19)

Retrieved ClinicalTrials.gov records included:

- **NCT05737784:** PRAX-222/elsunersen-like SCN2A-lowering ASO program for early-onset SCN2A-DEE; phase 1/2, 60 planned, recruiting in the retrieved record.
- **NCT07019922:** elsunersen in pediatric SCN2A-DEE; phase 3, 40 planned, recruiting.
- **NCT04639310/NCT04912856:** XEN496 (ezogabine) and extension in KCNQ2-DEE; both terminated, enrollment 8.
- **NCT04937062:** phenylbutyrate for monogenic DEE; early phase 1, 50 planned, active-not-recruiting.
- **NCT04873869/NCT05226780:** NBI-921352 for SCN8A-DEE and extension; terminated, enrollment 8.
- **NCT06983158:** CAP-002 gene therapy for STXBP1 encephalopathy; phase 1/2, terminated after enrollment of 1 in the retrieved record.

Trial statuses are dynamic and must be rechecked at https://clinicaltrials.gov before curation or clinical use.

## 13. Prevention

There is no vaccine, lifestyle modification, or population-screening program that prevents sporadic de novo EIDEE. Primary prevention is therefore reproductive rather than behavioral: molecular diagnosis, parental high-depth testing, counseling about gonadal/somatic mosaicism, preimplantation genetic testing, chorionic-villus sampling, or amniocentesis. (scheffer2024developmentalandepileptic pages 13-15)

Secondary prevention consists of rapid recognition, EEG confirmation, early genomic diagnosis, and immediate treatment of vitamin-responsive/metabolic disease or a resectable lesion. Tertiary prevention includes seizure-rescue plans, aspiration and infection prevention, nutrition, contracture prevention, bone health, SUDEP counseling, and rehabilitation. Cascade/carrier testing applies to inherited dominant, recessive, X-linked, or mitochondrial diagnoses; universal newborn screening for EIDEE is not currently established.

## 14. Other species and natural disease

No unitary, naturally occurring veterinary syndrome equivalent to human EIDEE was established in the retrieved evidence. Orthologous channel, synaptic, and metabolic diseases occur in animals, but annotation should be made at the **gene-specific** level through OMIA rather than assigning the entire human umbrella syndrome. The condition is not infectious or zoonotic and has no cross-species transmission.

## 15. Model organisms

- **Mouse (NCBITaxon:10090):** heterozygous/conditional *Scn1a* models reproduce spontaneous seizures, temperature sensitivity, premature death, and inhibitory-interneuron dysfunction; *Scn2a, Scn8a, Kcnq2, Stxbp1,* and *Cdkl5* models capture selected seizure/developmental phenotypes. Genetic background strongly changes severity.
- **Zebrafish (NCBITaxon:7955):** scalable seizure and drug-screening models exist for several channel/synaptic genes, but brain development and pharmacokinetics limit direct translation.
- **Drosophila/C. elegans:** useful for conserved ion-channel and synaptic pathways, with limited representation of mammalian cortical circuitry.
- **Patient iPSC-derived neurons and cerebral organoids:** enable variant-specific electrophysiology, GOF/LOF assignment, rescue experiments, and study of human progenitor/circuit phenotypes. Limitations include cellular immaturity, line-to-line variation, and absence of whole-organism pharmacology. In *SCN1A* iPSC systems, inhibitory neurons show selective functional impairment. (scheffer2024developmentalandepileptic pages 19-21)

The best-supported applications are mechanism validation, functional classification of VUS, drug screening, therapeutic-window studies, and testing ASO/AAV/CRISPR strategies. Experimental rescue in a model does not itself prove clinical efficacy.

## Evidence limitations and authoritative interpretation

The 2024 Nature Reviews Disease Primers and Lancet Child & Adolescent Health reviews support rapid molecular diagnosis and mechanism-stratified therapy, while emphasizing that DEEs encompass hundreds of genes and that developmental morbidity often persists despite seizure improvement. (scheffer2024developmentalandepileptic pages 34-39, specchio2024theexpandingfield pages 8-11, specchio2024theexpandingfield pages 1-6, scheffer2024developmentalandepileptic pages 9-11)

The most directly applicable abstract conclusion from the 2023 prospective study is: **“Genetic aetiologies are the most common cause of early-infantile developmental and epileptic encephalopathies… Patients with vitamin responsive epilepsies had the best probability of seizure control.”** (Published September 2023; https://doi.org/10.1093/braincomms/fcad243.) (agarwala2023earlyinfantiledevelopmentaland pages 1-3)

Major limitations are small rare-disease cohorts, tertiary-center referral bias, changing terminology, pooling of mechanistically different disorders, sparse long-term adult data, and predominantly observational evidence for precision treatments. Exact OMIM, MONDO, Orphanet, HPO, NCIT, HGNC, and ClinVar identifiers should be validated against current database releases before production ingestion.

References

1. (agarwala2023earlyinfantiledevelopmentaland pages 4-6): Pooja Agarwala, Bhuvandeep Narang, Thenral S. Geetha, Nilesh Kurwale, Praveena L Samson, Tamanna Golani, Udita Mahadevia, Ramprasad Vedam, Sakthivel Murugan, Sagnik Chatterjee, Pradeep Goyal, and Vivek Jain. Early-infantile developmental and epileptic encephalopathy: the aetiologies, phenotypic differences and outcomes—a prospective observational study. Brain Communications, Sep 2023. URL: https://doi.org/10.1093/braincomms/fcad243, doi:10.1093/braincomms/fcad243. This article has 17 citations and is from a peer-reviewed journal.

2. (agarwala2023earlyinfantiledevelopmentaland pages 1-3): Pooja Agarwala, Bhuvandeep Narang, Thenral S. Geetha, Nilesh Kurwale, Praveena L Samson, Tamanna Golani, Udita Mahadevia, Ramprasad Vedam, Sakthivel Murugan, Sagnik Chatterjee, Pradeep Goyal, and Vivek Jain. Early-infantile developmental and epileptic encephalopathy: the aetiologies, phenotypic differences and outcomes—a prospective observational study. Brain Communications, Sep 2023. URL: https://doi.org/10.1093/braincomms/fcad243, doi:10.1093/braincomms/fcad243. This article has 17 citations and is from a peer-reviewed journal.

3. (scheffer2024developmentalandepileptic pages 34-39): Ingrid E. Scheffer, Sameer Zuberi, Heather C. Mefford, Renzo Guerrini, and Amy McTague. Developmental and epileptic encephalopathies. Nature reviews. Disease primers, 10 1:61, Sep 2024. URL: https://doi.org/10.1038/s41572-024-00546-6, doi:10.1038/s41572-024-00546-6. This article has 157 citations.

4. (agarwala2023earlyinfantiledevelopmentaland pages 8-10): Pooja Agarwala, Bhuvandeep Narang, Thenral S. Geetha, Nilesh Kurwale, Praveena L Samson, Tamanna Golani, Udita Mahadevia, Ramprasad Vedam, Sakthivel Murugan, Sagnik Chatterjee, Pradeep Goyal, and Vivek Jain. Early-infantile developmental and epileptic encephalopathy: the aetiologies, phenotypic differences and outcomes—a prospective observational study. Brain Communications, Sep 2023. URL: https://doi.org/10.1093/braincomms/fcad243, doi:10.1093/braincomms/fcad243. This article has 17 citations and is from a peer-reviewed journal.

5. (scheffer2024developmentalandepileptic pages 9-11): Ingrid E. Scheffer, Sameer Zuberi, Heather C. Mefford, Renzo Guerrini, and Amy McTague. Developmental and epileptic encephalopathies. Nature reviews. Disease primers, 10 1:61, Sep 2024. URL: https://doi.org/10.1038/s41572-024-00546-6, doi:10.1038/s41572-024-00546-6. This article has 157 citations.

6. (scheffer2024developmentalandepileptic pages 19-21): Ingrid E. Scheffer, Sameer Zuberi, Heather C. Mefford, Renzo Guerrini, and Amy McTague. Developmental and epileptic encephalopathies. Nature reviews. Disease primers, 10 1:61, Sep 2024. URL: https://doi.org/10.1038/s41572-024-00546-6, doi:10.1038/s41572-024-00546-6. This article has 157 citations.

7. (specchio2024theexpandingfield pages 8-11): Nicola Specchio, Marina Trivisano, Eleonora Aronica, Simona Balestrini, Alexis Arzimanoglou, Gaia Colasante, J Helen Cross, Sergiusz Jozwiak, Jo M Wilmshurst, Federico Vigevano, Stéphane Auvin, Rima Nabbout, and Paolo Curatolo. The expanding field of genetic developmental and epileptic encephalopathies: current understanding and future perspectives. The Lancet. Child & adolescent health, 8 11:821-834, Nov 2024. URL: https://doi.org/10.1016/s2352-4642(24)00196-2, doi:10.1016/s2352-4642(24)00196-2. This article has 35 citations.

8. (specchio2024theexpandingfield pages 6-8): Nicola Specchio, Marina Trivisano, Eleonora Aronica, Simona Balestrini, Alexis Arzimanoglou, Gaia Colasante, J Helen Cross, Sergiusz Jozwiak, Jo M Wilmshurst, Federico Vigevano, Stéphane Auvin, Rima Nabbout, and Paolo Curatolo. The expanding field of genetic developmental and epileptic encephalopathies: current understanding and future perspectives. The Lancet. Child & adolescent health, 8 11:821-834, Nov 2024. URL: https://doi.org/10.1016/s2352-4642(24)00196-2, doi:10.1016/s2352-4642(24)00196-2. This article has 35 citations.

9. (scheffer2024developmentalandepileptic pages 11-13): Ingrid E. Scheffer, Sameer Zuberi, Heather C. Mefford, Renzo Guerrini, and Amy McTague. Developmental and epileptic encephalopathies. Nature reviews. Disease primers, 10 1:61, Sep 2024. URL: https://doi.org/10.1038/s41572-024-00546-6, doi:10.1038/s41572-024-00546-6. This article has 157 citations.

10. (scheffer2024developmentalandepileptic pages 13-15): Ingrid E. Scheffer, Sameer Zuberi, Heather C. Mefford, Renzo Guerrini, and Amy McTague. Developmental and epileptic encephalopathies. Nature reviews. Disease primers, 10 1:61, Sep 2024. URL: https://doi.org/10.1038/s41572-024-00546-6, doi:10.1038/s41572-024-00546-6. This article has 157 citations.

11. (nguyen2024genotypedriventherapeuticsin pages 9-10): Yen Thi My Nguyen, Bao-Quoc Vu, Duy-Khai Nguyen, Ngoc-Vinh Quach, Liem Thanh Bui, Jeonghan Hong, and Chi-Bao Bui. Genotype-driven therapeutics in dee and metabolic epilepsy: navigating treatment efficacy and drug resistance. Scientific Reports, Sep 2024. URL: https://doi.org/10.1038/s41598-024-72683-7, doi:10.1038/s41598-024-72683-7. This article has 5 citations and is from a peer-reviewed journal.

12. (scheffer2024developmentalandepileptic pages 17-19): Ingrid E. Scheffer, Sameer Zuberi, Heather C. Mefford, Renzo Guerrini, and Amy McTague. Developmental and epileptic encephalopathies. Nature reviews. Disease primers, 10 1:61, Sep 2024. URL: https://doi.org/10.1038/s41572-024-00546-6, doi:10.1038/s41572-024-00546-6. This article has 157 citations.

13. (specchio2024theexpandingfield pages 27-29): Nicola Specchio, Marina Trivisano, Eleonora Aronica, Simona Balestrini, Alexis Arzimanoglou, Gaia Colasante, J Helen Cross, Sergiusz Jozwiak, Jo M Wilmshurst, Federico Vigevano, Stéphane Auvin, Rima Nabbout, and Paolo Curatolo. The expanding field of genetic developmental and epileptic encephalopathies: current understanding and future perspectives. The Lancet. Child & adolescent health, 8 11:821-834, Nov 2024. URL: https://doi.org/10.1016/s2352-4642(24)00196-2, doi:10.1016/s2352-4642(24)00196-2. This article has 35 citations.

14. (specchio2024theexpandingfield pages 14-17): Nicola Specchio, Marina Trivisano, Eleonora Aronica, Simona Balestrini, Alexis Arzimanoglou, Gaia Colasante, J Helen Cross, Sergiusz Jozwiak, Jo M Wilmshurst, Federico Vigevano, Stéphane Auvin, Rima Nabbout, and Paolo Curatolo. The expanding field of genetic developmental and epileptic encephalopathies: current understanding and future perspectives. The Lancet. Child & adolescent health, 8 11:821-834, Nov 2024. URL: https://doi.org/10.1016/s2352-4642(24)00196-2, doi:10.1016/s2352-4642(24)00196-2. This article has 35 citations.

15. (specchio2024theexpandingfield pages 1-6): Nicola Specchio, Marina Trivisano, Eleonora Aronica, Simona Balestrini, Alexis Arzimanoglou, Gaia Colasante, J Helen Cross, Sergiusz Jozwiak, Jo M Wilmshurst, Federico Vigevano, Stéphane Auvin, Rima Nabbout, and Paolo Curatolo. The expanding field of genetic developmental and epileptic encephalopathies: current understanding and future perspectives. The Lancet. Child & adolescent health, 8 11:821-834, Nov 2024. URL: https://doi.org/10.1016/s2352-4642(24)00196-2, doi:10.1016/s2352-4642(24)00196-2. This article has 35 citations.

## Artifacts

- [Edison artifact artifact-00](Early-Infantile_Developmental_and_Epileptic_Encephalopathy-deep-research-falcon_artifacts/artifact-00.md)