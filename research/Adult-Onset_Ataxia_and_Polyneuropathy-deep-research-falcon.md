---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-19T21:01:55.732361'
end_time: '2026-08-19T21:11:49.054617'
duration_seconds: 593.32
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Adult-Onset Ataxia and Polyneuropathy
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
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 4
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Adult-Onset_Ataxia_and_Polyneuropathy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Adult-Onset Ataxia and Polyneuropathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Adult-Onset Ataxia and Polyneuropathy** covering all of the
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
- **Disease Name:** Adult-Onset Ataxia and Polyneuropathy
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Adult-Onset Ataxia and Polyneuropathy** covering all of the
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


# Adult-Onset Ataxia and Polyneuropathy: Comprehensive Disease Report

## Scope and disease mapping

The requested label is not a consistently maintained standalone disease name. In a Mendelian context, it maps most closely to **RFC1 spectrum disorder**, especially **cerebellar ataxia with neuropathy and bilateral vestibular areflexia syndrome (CANVAS)**. Open Targets identifies this entity as **MONDO:0044720** and links it specifically to **RFC1** (ENSG00000035928), supported by human genetic evidence including PMID **30926972**, PMID **31230722**, and ClinGen/ClinVar records. “Adult-onset ataxia and polyneuropathy” can also describe genetically heterogeneous disorders; therefore, a knowledge-base entry should state explicitly that this report concerns **RFC1-related disease**, not every disorder producing that phenotype. (OpenTargets Search: CANVAS)

The evidence summarized below is aggregated disease-level evidence from cohorts, case series, molecular studies, and ClinicalTrials.gov—not individual EHR data.

| Domain | Core finding | Quantitative details | Ontology suggestions | Evidence |
|---|---|---:|---|---|
| Disease identity | Adult-onset ataxia and polyneuropathy in this Mendelian context maps best to **RFC1 spectrum disorder / CANVAS** = **cerebellar ataxia with neuropathy and bilateral vestibular areflexia syndrome**; **MONDO:0044720** | Open Targets links MONDO:0044720 to **RFC1** with literature support | MONDO:0044720; HPO: HP:0001251 Ataxia, HP:0009830 Peripheral neuropathy, HP:0007646 Bilateral vestibular hypofunction | (OpenTargets Search: CANVAS, traschutz2021naturalhistoryphenotypic pages 1-2) |
| Inheritance / causal gene | Usually **autosomal recessive**; primary cause is **biallelic intronic RFC1 pentanucleotide repeat expansion** in intron 2 | Typical pathogenic motif **AAGGG**; reported pathogenic spectrum also includes population-specific **ACAGG** and Māori-associated configurations; compound heterozygosity with truncating RFC1 variants also reported | Gene: RFC1; HPO: HP:0000007 Autosomal recessive inheritance | (cortese2019biallelicexpansionof pages 4-6, ronco2023truncatingvariantsin pages 1-2, scriba2023rfc1inan pages 3-4) |
| Variant / molecular lesion | Pathogenic alleles are large nonreference intronic repeat expansions; truncating coding variants can act in trans with one expansion in rare cases | Expansion size about **~400–2,000 repeats** (median ~1,000) in early discovery work; 2024 data show repeat size modifies onset/severity | SO: tandem repeat expansion; intron variant | (cortese2019biallelicexpansionof pages 4-6, curro2024roleofthe pages 10-12, curro2024roleofthe pages 15-17) |
| Typical onset / course | **Adult onset**, usually insidious and slowly progressive multisystem neurodegeneration | Mean onset **54±9 y** (range **35–73**) in 2019 series; median onset **54 y** (range **25–80**) in 2024 cohort; progression about **1.3 SARA points/year** | HPO: HP:0003581 Adult onset, HP:0003676 Progressive neurologic deterioration | (cortese2019biallelicexpansionof pages 4-6, curro2024roleofthe pages 10-12, traschutz2021naturalhistoryphenotypic pages 1-2) |
| Core phenotype: sensory neuropathy / neuronopathy | Hallmark feature; often presents as sensory ataxic neuropathy and may precede full CANVAS | **All tested/examined cases** had sensory neuropathy in major cohorts; in 2024 cohort **24%** had isolated sensory neuropathy and **38%** complex neuropathy | HPO: HP:0009830 Peripheral neuropathy, HP:0002355 Difficulty walking; UBERON: dorsal root ganglion | (cortese2019biallelicexpansionof pages 4-6, curro2024roleofthe pages 10-12, curro2024roleofthe pages 4-7) |
| Core phenotype: cerebellar ataxia | Cerebellar dysfunction is common but not universal early; often evolves over time | Cerebellar involvement **80%** in 2019 series; cerebellar signs **72%** at first assessment and **84%** at follow-up in 2024 cohort | HPO: HP:0001251 Ataxia, HP:0002060 Cerebellar atrophy; UBERON: cerebellum | (cortese2019biallelicexpansionof pages 4-6, curro2024roleofthe pages 10-12) |
| Core phenotype: vestibular dysfunction | Bilateral vestibular areflexia/hypofunction is a defining axis of CANVAS but may be incomplete early | Bilateral vestibular areflexia **54%** in 2019 series; **75%** in 2024 cohort | HPO: HP:0007993 Vestibular dysfunction, HP:0007646 Bilateral vestibular hypofunction; UBERON: vestibular labyrinth | (cortese2019biallelicexpansionof pages 4-6, curro2024roleofthe pages 10-12, gisatulin2020clinicalspectrumof pages 5-9) |
| Core phenotype: chronic cough | Highly discriminative associated symptom and may precede neurologic signs | **37%** in 2019 series; **75% overall** and initial symptom in **50%** in 2024 cohort; ACC phenotype can be highly suggestive | HPO: HP:0012735 Chronic cough | (cortese2019biallelicexpansionof pages 4-6, curro2024roleofthe pages 10-12, traschutz2021naturalhistoryphenotypic pages 1-2) |
| Core phenotype: dysautonomia / small-fiber involvement | Autonomic and small-fiber involvement are common in multisystem disease | Autonomic involvement **23%** in 2019 series; dysautonomia **62%** in 2021 natural history study; 2023 Portuguese cohort: multisystem features beyond CANVAS in **82%**, dysautonomia **43%**, severe epidermal denervation in all biopsied patients | HPO: HP:0000789 Autonomic dysfunction; CL: sensory neuron; UBERON: skin, peripheral nerve | (cortese2019biallelicexpansionof pages 4-6, traschutz2021naturalhistoryphenotypic pages 1-2) |
| Other multisystem phenotypes | Can overlap with parkinsonism/MSA-C, movement disorder, cranial or motor neuron features | Bradykinesia **28%**, postural instability **49%**, slow vertical saccades **17%**, chorea/dystonia **11%** in 2021 study; motor neuron/motor neuropathy **18%** in 2023 Portuguese cohort | HPO: HP:0002067 Bradykinesia, HP:0002136 Dysphagia, HP:0001260 Dysarthria | (traschutz2021naturalhistoryphenotypic pages 1-2) |
| Diagnostics | Diagnosis relies on targeted **RFC1 repeat testing** plus phenotype-specific neurologic workup | Methods reported: flanking PCR, **repeat-primed PCR**, duplex PCR, **Southern blot**, fragment analysis, Sanger sequencing, short-read screening, targeted **long-read sequencing**; MRI/CT showed cerebellar atrophy in **83%** of 42 cases | HPO: HP:0003401 Cerebellar MRI abnormality; UBERON: cerebellar vermis | (cortese2019biallelicexpansionof pages 4-6, gisatulin2020clinicalspectrumof pages 1-5, scriba2023rfc1inan pages 3-4) |
| Diagnostic yield / testing strategy | RFC1 testing should be prioritized in adult-onset ataxia with sensory neuropathy, vestibular failure, or chronic cough | Prevalence in enriched cohorts: **67%** in suspected cohort, **68%** in clinical CANVAS, **100%** in ataxia with chronic cough, **14%** in unselected late-onset ataxia; Australasian cohort found pathogenic expansions in **15.3% (37/242)** | HPO-guided testing: ataxia + neuropathy + cough + vestibular dysfunction | (traschutz2021naturalhistoryphenotypic pages 1-2, scriba2023rfc1inan pages 3-4) |
| Key 2024 mechanism | Patient iPSC-derived neurons support **repeat-dependent, RFC1-protein-independent synaptic dysfunction** | 2024 Science Advances study found normal RFC1 splicing/expression and intact DNA repair, no consistent RNA foci/peptide toxicity in iNeurons, but reduced neuronal development/synaptic connectivity; **CRISPR deletion of one expanded allele rescued deficits**, RFC1 knockdown did not phenocopy, and RFC1 re-expression did not rescue | GO: synapse organization, chemical synaptic transmission; CL: glutamatergic neuron; UBERON: cerebellum/peripheral nervous system | (maltby2024aagggrepeatexpansions pages 1-2, maltby2024aagggrepeatexpansions pages 13-14, maltby2024aagggrepeatexpansions pages 11-13) |
| Genotype–phenotype modifier (2024) | Repeat size is a prognostic modifier | Larger smaller allele HR **2.06** and larger allele HR **1.53** for earlier neurologic onset; loss of independent walking HR **2.78** (smaller allele) and **1.60** (larger allele); dysarthria/dysphagia HR **3.40** and **1.71**; larger expansions associated with more severe vermian atrophy | HPO: HP:0001260 Dysarthria, HP:0002015 Dysphagia; UBERON: cerebellar vermis | (curro2024roleofthe pages 10-12, curro2024roleofthe pages 15-17) |
| Prognosis | Chronic progressive disability; some premature mortality in advanced disease | In 2024 cohort **54%** required walking aids after median **10 y**, **17%** wheelchairs after **14 y**; mortality **8%**, with disease-related deaths including aspiration pneumonia/immobility complications | HPO: HP:0002829 Wheelchair dependence, HP:0040296 Aspiration pneumonia | (curro2024roleofthe pages 10-12, traschutz2021naturalhistoryphenotypic pages 1-2) |
| Current treatment / trial status | **No established disease-modifying therapy**; care is supportive and multidisciplinary; RFC1-specific biomarker/natural-history trial is recruiting | Trial planning estimate: **330** total patients for 1-year or **132** for 2-year study to detect 50% slowing; **NCT07156214** recruiting from **2024-10-14**, primary completion **2026-06-30**, evaluating scales, NfL/oxidative stress biomarkers, imaging, and patient-derived cells | NCIT: supportive care; physical therapy/rehabilitation; biomarker study | (traschutz2021naturalhistoryphenotypic pages 1-2, NCT07156214 chunk 1) |


*Table: This table summarizes the core knowledge-base fields for RFC1 spectrum disorder/CANVAS, the main Mendelian interpretation of adult-onset ataxia and polyneuropathy. It highlights identifiers, causal genetics, phenotype frequencies, diagnostics, 2024 mechanistic insights, prognosis, and current trial status with ontology suggestions and evidence IDs.*

## 1. Disease information

RFC1 disease is an autosomal-recessive, usually late-onset neurodegenerative disorder whose manifestations form a continuum from isolated sensory neuronopathy/neuropathy to combined sensory, cerebellar, and bilateral vestibular dysfunction. The complete triad is termed **CANVAS**. Other common labels are **RFC1 spectrum disorder**, **RFC1-related disorder**, **RFC1-associated disease**, **CANVAS syndrome**, and **ataxia with chronic cough**.

**Identifiers and classifications**

- **MONDO:** MONDO:0044720, cerebellar ataxia with neuropathy and bilateral vestibular areflexia syndrome.
- **OMIM:** CANVAS is commonly indexed as **614575**; RFC1 is **102579**. Database versions should be checked before ingestion.
- **Gene:** RFC1, replication factor C subunit 1; Ensembl ENSG00000035928.
- **MeSH:** no uniquely specific RFC1-CANVAS descriptor was established in the retrieved evidence; broader terms include cerebellar ataxia and peripheral nervous system disease.
- **ICD-10/ICD-11:** no uniquely disease-specific code was established. Coding generally combines hereditary/degenerative ataxia, polyneuropathy, and vestibular dysfunction. A knowledge base should not assign a single exact ICD code without jurisdictional validation.

The landmark discovery study described a mean onset of **54±9 years** (range 35–73) and mean observed disease duration of **11±7 years**. Its defining molecular lesion was a biallelic, large intronic RFC1 repeat expansion. (cortese2019biallelicexpansionof pages 4-6)

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal factor

The principal cause is a **germline biallelic nonreference pentanucleotide-repeat expansion in intron 2 of RFC1**, usually `(AAGGG)n`. Typical pathogenic alleles contain approximately **400–2,000 repeats**, often near 800–1,000, whereas the reference motif is `(AAAAG)n`. The expansion lies in the poly-A tail of an AluSx3 element. (cortese2019biallelicexpansionof pages 4-6, gisatulin2020clinicalspectrumof pages 5-9, gisatulin2020clinicalspectrumof pages 1-5)

Pathogenic configurations are population dependent. Besides AAGGG, disease-associated **ACAGG** and complex Māori-associated `(AAAGG)exp(AAGGG)exp` alleles have been reported. Consequently, an AAGGG-only assay can miss disease in non-European populations. (curro2024roleofthe pages 4-7, scriba2023rfc1inan pages 3-4)

Rare patients have one expanded allele and a truncating RFC1 variant in trans. Reported variants include **c.1267C>T (p.Arg423Ter), c.1739_1740del (p.Lys580SerfsTer9), c.2191del (p.Gly731GlufsTer6), and c.2876del (p.Pro959GlnfsTer24)**. Fibroblasts carrying two tested truncating alleles showed nonsense-mediated decay and reduced RFC1 RNA and protein. Full RFC1 sequencing is therefore appropriate when classic CANVAS accompanies only one detected expansion. (ronco2023truncatingvariantsin pages 1-2)

### Risk and modifying factors

- **Genetic risk:** two pathogenic RFC1 alleles are causal; heterozygous carriers are generally unaffected.
- **Repeat size:** the strongest established modifier. In 553 expansion carriers, with size measured in 392, larger alleles predicted earlier onset and more severe disease. Earlier neurologic onset had HR **2.06** for the smaller allele and **1.53** for the larger allele; earlier dysarthria/dysphagia had HR **3.40** and **1.71**; earlier loss of independent walking had HR **2.78** and **1.60**, respectively. Larger repeats were also associated with complex neuropathy, complete CANVAS, and greater vermian atrophy. Repeat size explained only about **6%** of onset variability, implying additional modifiers. (curro2024roleofthe pages 10-12, curro2024roleofthe pages 15-17)
- **Age:** manifestations are age dependent, explaining apparently sporadic presentations and unaffected younger siblings.
- **Family history:** its absence does not argue strongly against disease because inheritance is recessive and onset is late.

No reproducible sex, lifestyle, occupational, dietary, infectious, or toxic risk factor has been established for genetically confirmed RFC1 disease. No validated protective allele, diet, drug, or environmental exposure is known. Environmental or epigenetic modifiers are plausible because repeat size explains little phenotypic variance, but specific gene–environment interactions remain unproven. The 2024 repeat study found no major meiotic or tissue-specific somatic instability, arguing against marked anticipation driven by unstable expansion growth. (curro2024roleofthe pages 15-17)

## 3. Phenotypes

The disease is chronic and progressive, but component systems emerge at different times. Sensory neuropathy often precedes cerebellar and vestibular signs; chronic spasmodic cough can precede neurologic disability by years.

- **Sensory neuronopathy/neuropathy:** hallmark phenotype, generally non-length-dependent, affecting large fibers and proprioception; motor conduction is often preserved. Suggested terms: **HP:0009830 peripheral neuropathy**, HP:0000763 sensory neuropathy, HP:0003477 impaired vibration sense, HP:0010871 sensory ataxia. It was found in all examined patients in major cohorts. (cortese2019biallelicexpansionof pages 4-6, curro2024roleofthe pages 10-12)
- **Cerebellar ataxia:** gait and limb ataxia, dysarthria, impaired pursuit, and cerebellar atrophy; **HP:0001251**, HP:0002072 chorea only where present, HP:0001260 dysarthria, HP:0002060 cerebellar atrophy. Cerebellar involvement was 80% in the discovery cohort and rose from 72% at first assessment to 84% at follow-up in a later large cohort. (cortese2019biallelicexpansionof pages 4-6, curro2024roleofthe pages 10-12)
- **Bilateral vestibulopathy:** oscillopsia, impaired vestibulo-ocular reflex, and imbalance worsened in darkness; **HP:0007993 vestibular dysfunction**, HP:0007646 bilateral vestibular hypofunction, HP:0010544 oscillopsia. Reported prevalence was 54–75%, depending on cohort and disease stage. (cortese2019biallelicexpansionof pages 4-6, curro2024roleofthe pages 10-12, gisatulin2020clinicalspectrumof pages 5-9)
- **Chronic cough:** dry, spasmodic cough, frequently prodromal; **HP:0012735**. Frequencies ranged from 37% in the initial series to 75% in a 2024 cohort; in the latter it was the initial symptom in 50%. (cortese2019biallelicexpansionof pages 4-6, curro2024roleofthe pages 10-12)
- **Dysautonomia and small-fiber disease:** urinary, bowel, cardiovascular, cardiovagal, and sudomotor dysfunction; **HP:0000789 autonomic dysfunction**, HP:0000020 urinary incontinence where applicable. Dysautonomia occurred in 23% of the discovery series and 62% in a deeply phenotyped natural-history cohort. (cortese2019biallelicexpansionof pages 4-6, traschutz2021naturalhistoryphenotypic pages 1-2)
- **Other manifestations:** bradykinesia 28%, postural instability 49%, slow vertical saccades 17%, and chorea/dystonia 11% in one cohort. Motor-neuron/motor-neuropathy phenotypes, sleep disorders, cranial neuropathy, and cognitive impairment have been reported but are less securely quantified and may represent spectrum extremes. (traschutz2021naturalhistoryphenotypic pages 1-2)
- **Advanced disability:** dysarthria/dysphagia increased from 6% to 51% during follow-up. Suggested terms include **HP:0002015 dysphagia**, HP:0002829 wheelchair dependence, and HP:0040296 aspiration pneumonia. (curro2024roleofthe pages 10-12)

Quality-of-life effects include impaired walking in darkness or on uneven surfaces, falls, oscillopsia, chronic cough, pain or sensory discomfort, loss of driving and employment, dysphagia, and eventual dependence for mobility. RFC1-specific EQ-5D, SF-36, or PROMIS population estimates were not found.

## 4. Genetic and molecular information

**RFC1** encodes the large subunit of replication factor C, a clamp-loader complex involved in DNA replication and repair. The conventional disease genotype is homozygous or compound-heterozygous pathogenic repeat expansion. Variants are germline, not somatic cancer alterations.

Population screening in the discovery study found expanded AAGGG alleles on approximately **0.7% of chromosomes**; subsequent estimates range from 0.7% to 4%, depending on ancestry, motif definition, and ascertainment. These figures are allele frequencies, not disease prevalence. (cortese2019biallelicexpansionof pages 4-6, traschutz2021naturalhistoryphenotypic pages 1-2)

Large repeat expansions are not represented reliably by standard SNV/indel nomenclature, and their frequencies are poorly captured by conventional gnomAD short-read variant tables. For knowledge-base purposes, pathogenicity should be assigned at the **repeat-configuration level**, with motif, size, zygosity, and assay recorded. Benign or uncertain expansions, including AAAAG/AAAGG or interrupted configurations, must not be automatically classified as pathogenic. (gisatulin2020clinicalspectrumof pages 1-5, scriba2023rfc1inan pages 3-4)

No validated modifier gene, disease-specific methylation signature, recurrent chromosomal rearrangement, or pathogenic epigenetic lesion has been established. Rare RFC1 deletions and truncating alleles broaden the allelic spectrum but do not define a recurrent chromosomal syndrome. (ronco2023truncatingvariantsin pages 1-2)

## 5. Environmental and lifestyle information

RFC1 disease is not known to be caused by infection, radiation, pollution, alcohol, smoking, diet, or occupational exposure. Such factors remain relevant in the **differential diagnosis** of adult-onset ataxia/polyneuropathy—particularly alcohol, neurotoxic medications, vitamin deficiencies, immune disease, and paraneoplastic processes—but are not demonstrated causal cofactors for biallelic RFC1 disease. No vaccine or pathogen-specific intervention applies.

## 6. Mechanism and pathophysiology

### Causal chain

**Biallelic pathogenic RFC1 repeat configuration → repeat-dependent neuronal dysfunction → impaired synaptic development/signaling and selective vulnerability of sensory ganglia, cerebellar circuits, and vestibular pathways → sensory ataxia, cerebellar ataxia, and vestibular areflexia.** Downstream degeneration includes Purkinje-cell loss, dorsal-root-ganglionopathy, peripheral small/large-fiber loss, and cerebellar atrophy. Severe Purkinje-cell depletion with Bergmann gliosis has been documented neuropathologically. (cortese2019biallelicexpansionof pages 4-6)

Earlier studies found unchanged RFC1/WDR19 expression and no RFC1 intron retention, leaving mechanism uncertain. (gisatulin2020clinicalspectrumof pages 1-5)

The key 2024 mechanistic development used patient-derived iPSCs and glutamatergic iNeurons. RFC1 expression, splicing, DNA-repair function, DNA-damage accumulation, and UV-repair recovery were not materially abnormal. Reporter constructs permitted pentapeptide-repeat translation, but repeat peptides and convincing RNA-foci toxicity were not consistently demonstrated in patient iNeurons. Conversely, patient neurons had abnormal neuronal-development and synaptic-gene programs, reduced burst rate, burst strength, and firing correlation, and impaired connectivity. Deleting one expanded allele with CRISPR rescued molecular and functional defects; RFC1 knockdown did not reproduce them, and RFC1 replacement did not rescue them. The authors’ abstract conclusion was: **“These findings support a repeat-dependent but RFC1 protein–independent cause of neuronal dysfunction in CANVAS.”** (maltby2024aagggrepeatexpansions pages 1-2, maltby2024aagggrepeatexpansions pages 13-14, maltby2024aagggrepeatexpansions pages 11-13)

This creates tension with truncating-variant evidence supporting partial RFC1 loss of function. The most defensible current interpretation is that more than one mechanism may operate: repeat-sequence/configuration toxicity is strongly supported in neurons, while RFC1 haploinsufficiency or reduced dosage can contribute in rare compound genotypes. (ronco2023truncatingvariantsin pages 1-2, maltby2024aagggrepeatexpansions pages 1-2)

**Suggested annotations:** GO:0050808 synapse organization; GO:0007268 chemical synaptic transmission; GO:0006281 DNA repair, with a qualifier that canonical repair dysfunction was not demonstrated; GO:0006950 response to stress; CL:0000540 neuron, CL:0000121 Purkinje cell, CL:0000101 sensory neuron, CL:0000709 retinal?—the latter should not be used without phenotype evidence. Relevant compartments include nucleus, cytoplasm, synapse, and axon.

No validated disease-level epigenomic, proteomic, metabolomic, lipidomic, single-cell, or spatial-transcriptomic signature is yet available. INSIDE-CANVAS is investigating oxidative stress, neurofilament light, mitochondrial function, and patient-derived cells. (NCT07156214 chunk 1)

## 7. Anatomical structures affected

Primary systems are the peripheral sensory nervous system, cerebellum, and vestibular system.

- **Dorsal-root ganglia and sensory peripheral nerves:** neuronopathy with large- and small-fiber loss; UBERON:0000044 dorsal root ganglion, UBERON:0001021 nerve, CL:0000101 sensory neuron.
- **Cerebellum:** Purkinje cells, vermis, and hemispheric circuits; UBERON:0002037 cerebellum, UBERON:0004729 cerebellar vermis, CL:0000121 Purkinje cell.
- **Vestibular apparatus/pathways:** bilateral vestibular hypofunction; UBERON:0001843 vestibular labyrinth and vestibular nerve/pathway terms.
- **Spinal proprioceptive pathways and brainstem oculomotor networks** may contribute secondarily.
- **Autonomic and cutaneous small fibers** are involved in a subset.

MRI showed cerebellar atrophy in **83% of 42** imaged cases in the discovery series. Larger repeats, especially the smaller expanded allele, correlated with greater atrophy of vermian lobules I–V and VI–VII. Disease is generally bilateral/systemic rather than lateralized. (cortese2019biallelicexpansionof pages 4-6, curro2024roleofthe pages 10-12)

## 8. Temporal development

Onset is usually insidious in the fifth or sixth decade, but observed onset spans approximately 25–80 years. Cough or sensory symptoms may be the first manifestation; cerebellar and vestibular components accumulate later. (cortese2019biallelicexpansionof pages 4-6, curro2024roleofthe pages 10-12)

A practical staging model is:

1. **Prodromal/early:** chronic cough, distal or patchy sensory symptoms, imbalance in darkness.
2. **Intermediate:** sensory ataxia plus cerebellar or vestibular dysfunction; falls and oscillopsia.
3. **Established CANVAS:** all three systems affected, with dysarthria and reduced independent mobility.
4. **Advanced:** walking aids or wheelchair use, dysphagia, aspiration risk, and multisystem/autonomic complications.

Mean ataxia progression was approximately **1.3 SARA points/year**, although nonlinear MSA-C-like phases of 2.5–5.5 points/year occurred. No spontaneous remission pattern is recognized. (traschutz2021naturalhistoryphenotypic pages 1-2)

## 9. Inheritance and population

Inheritance is **autosomal recessive**, with variable expressivity and strongly age-dependent penetrance. Precise lifetime penetrance for each repeat motif and size is not established. Repeat-size correlation supports dose-dependent expressivity. Unlike many repeat diseases, marked meiotic/somatic instability and classic genetic anticipation were not observed. (curro2024roleofthe pages 10-12, curro2024roleofthe pages 15-17)

RFC1 expansions were found in **14% of unselected late-onset ataxia**, **67% of an enriched suspected cohort**, **68% of clinical CANVAS**, and **100% of ataxia-with-chronic-cough cases** in one study. These are diagnostic yields, not population prevalence. (traschutz2021naturalhistoryphenotypic pages 1-2)

An Australasian study found pathogenic biallelic expansions in **37/242 (15.3%)** neurologic cases, including AAGGG, ACAGG, and Māori-associated configurations. A Japanese hereditary sensory/autonomic neuropathy cohort found biallelic RFC1 expansions in **20/79 (25.3%)** cases. These findings demonstrate ancestry-specific motif distributions. (scriba2023rfc1inan pages 3-4)

Population incidence, point prevalence, sex ratio, carrier frequency by ancestry, and survival-adjusted prevalence remain inadequately measured. Consanguinity can increase recessive disease probability but is not required, given relatively common carrier alleles.

## 10. Diagnostics

### Clinical and physiologic evaluation

Evaluate cerebellar signs, sensory modalities, reflexes, gait in darkness, eye movements, autonomic symptoms, chronic cough, and family history. Recommended investigations include:

- Nerve-conduction studies: typically absent/reduced sensory responses with relatively preserved motor conduction.
- Vestibular testing: video head-impulse testing, calorics, rotational chair, vestibular-evoked myogenic potentials, and visually enhanced vestibulo-ocular reflex where available.
- Brain MRI: cerebellar and vermian atrophy; spinal imaging when alternative diagnoses are suspected.
- SARA or ICARS for ataxia, vestibular disability scales, swallowing assessment, and autonomic testing.
- Laboratory exclusion of acquired ataxia/neuropathy: vitamin E/B12/copper, thyroid, diabetes, paraprotein, immune/paraneoplastic studies, toxins, infections, and medication review as clinically indicated.

### Genetic testing algorithm

1. Order **RFC1 flanking PCR plus motif-specific repeat-primed PCR** in adult-onset sensory neuronopathy, CANVAS, bilateral vestibulopathy with neuropathy, or ataxia with chronic cough.
2. Confirm and size large alleles with **Southern blot, optical genome mapping, or validated long-read sequencing**.
3. If the phenotype is compelling but only one expansion is found, sequence the complete RFC1 coding region and assess deletion/CNV alleles. (ronco2023truncatingvariantsin pages 1-2)
4. If PCR patterns are atypical or ancestry suggests non-AAGGG motifs, use targeted long-read sequencing to resolve motif, interruptions, orientation, and size. The 2023 Australasian study recommended a multistep short-/long-read workflow. (scriba2023rfc1inan pages 3-4)
5. If negative, test other repeat disorders and conventional ataxia/neuropathy genes with a repeat-expansion panel plus WES/WGS. Standard WES alone can miss RFC1 expansions.

The 2024 adult-onset ataxia review summarized the diagnostic challenge: targeted repeat testing remains necessary even when exome or short-read genome sequencing is performed, while long-read sequencing may eventually unify detection. (scriba2023rfc1inan pages 3-4)

Important differentials include Friedreich ataxia, SCA3 and other dominant SCAs, **FGF14-GAA/SCA27B**, FXTAS, POLG and other mitochondrial disease, spinocerebellar ataxia with axonal neuropathy, hereditary sensory/autonomic neuropathies, immune/paraneoplastic ataxia, superficial siderosis, multiple-system atrophy–cerebellar type, alcohol/toxin-associated disease, and vitamin deficiencies.

Cascade testing is appropriate after molecular confirmation. Population or newborn screening is not recommended; predictive testing of adult relatives requires genetic counseling.

## 11. Outcome and prognosis

Disease is lifelong and progressive; recovery is not expected, although rehabilitation can improve function and safety. In a large cohort, **54%** required a walking aid after a median of **10 years**, and **17%** required a wheelchair after **14 years**. Mortality was **8%**; attributed deaths included aspiration pneumonia and complications of immobility. (curro2024roleofthe pages 10-12)

Repeat size is the best current molecular prognostic marker, but it is not deterministic. Baseline multisystem involvement, dysphagia, falls, and rapid SARA progression likely indicate poorer functional prognosis. No validated individual survival calculator exists.

## 12. Treatment and current applications

There is **no approved disease-modifying therapy**. Current real-world care is genotype-informed but symptomatic:

- physiotherapy, balance and gait training, vestibular rehabilitation, fall prevention, and mobility aids;
- occupational therapy and home adaptation;
- speech therapy, swallow evaluation, texture modification, and aspiration prevention;
- treatment of neuropathic pain using standard agents when present;
- management of orthostatic, urinary, bowel, and sudomotor symptoms;
- cough assessment and symptomatic management after excluding pulmonary causes;
- nutritional, respiratory, psychological, and social support;
- hearing/vision compensation and driving-safety review;
- genetic counseling and cascade testing.

Suggested NCIT concepts include **Physical Therapy**, **Occupational Therapy**, **Speech Therapy**, **Vestibular Rehabilitation**, **Supportive Care**, and **Genetic Counseling**. No RFC1-specific pharmacogenomic guideline, surgery, cell therapy, ASO, siRNA, or gene-replacement therapy is established.

The 2024 iNeuron result argues that simply restoring RFC1 protein may be insufficient; excision, silencing, or sequence-specific targeting of the expanded repeat is a more mechanistically supported direction, although CRISPR rescue remains preclinical. (maltby2024aagggrepeatexpansions pages 1-2, maltby2024aagggrepeatexpansions pages 11-13)

**Clinical research:** INSIDE-CANVAS (**NCT07156214**) began October 14, 2024 and is recruiting. It targets 25 RFC1 patients plus matched controls, with one-year clinical scales, neurophysiology, vestibular testing, brain/spinal MRI, NfL and oxidative-stress biomarkers, fibroblasts, and iPSCs; estimated primary completion is June 30, 2026. It is a biomarker/pathogenesis study, not a proven therapeutic trial. (NCT07156214 chunk 1)

Natural-history modeling estimated that a trial detecting 50% slowing would require approximately **330 participants for one year** or **132 for two years**. (traschutz2021naturalhistoryphenotypic pages 1-2)

## 13. Prevention

Primary prevention through lifestyle modification is not available. For families with a known genotype, options include genetic counseling, adult cascade testing, prenatal diagnosis, and preimplantation genetic testing, subject to local ethics and regulation. Because penetrance is age dependent and genotype–phenotype prediction is incomplete, predictive counseling must address uncertainty.

Secondary prevention consists of early molecular diagnosis and surveillance for falls, vestibular failure, autonomic dysfunction, dysphagia, and aspiration. Tertiary prevention includes rehabilitation, mobility aids, home-safety modification, vaccination and respiratory care according to general standards, and prompt treatment of aspiration or immobility complications. No RFC1-specific vaccine or chemoprophylaxis applies.

## 14. Other species and natural disease

No well-established naturally occurring veterinary counterpart caused by orthologous RFC1 intronic pentanucleotide expansions was identified. RFC1 is evolutionarily conserved, but the human disease depends on a specific repeat architecture that may not be conserved across species. Zoonotic transmission is not applicable. A knowledge base should mark affected nonhuman species, breed associations, and natural transmission as **not established** rather than infer them from RFC1 conservation.

## 15. Model organisms and experimental systems

The most informative current model is the **human patient-derived iPSC/iNeuron system**. The 2024 study used four patient and three control lines and an isogenic CRISPR-corrected line. It reproduced neuronal-development, transcriptomic, calcium-signaling, and synaptic-connectivity abnormalities and demonstrated rescue after deletion of one expanded allele. (maltby2024aagggrepeatexpansions pages 13-14, maltby2024aagggrepeatexpansions pages 2-3)

Limitations are important: the neurons were predominantly glutamatergic rather than dorsal-root-ganglion sensory neurons, vestibular neurons, or mature Purkinje cells; the number of lines and isogenic controls was small; and early developmental phenotypes may not reproduce decades-long human degeneration. Pentapeptide products were detected in three of four postmortem cerebella but not convincingly in iNeurons, illustrating model dependence. (maltby2024aagggrepeatexpansions pages 13-14)

No validated mouse, rat, zebrafish, Drosophila, or C. elegans model was established in the retrieved evidence as recapitulating the complete human triad. Priority models include repeat knock-in animals, sensory-neuron and Purkinje-cell differentiation, cerebellar organoids, and isogenic long-repeat systems.

## Key recent expert conclusions and exact abstract quotations

- Currò et al., *Brain* 2024, DOI [10.1093/brain/awad436](https://doi.org/10.1093/brain/awad436): **“RFC1 repeat size, particularly of the smaller allele, is one of the determinants of variability in RFC1 disease and represents a key prognostic factor to predict disease onset, phenotype, and severity.”** (curro2024roleofthe pages 10-12)
- Maltby et al., *Science Advances*, September 2024, DOI [10.1126/sciadv.adn2321](https://doi.org/10.1126/sciadv.adn2321): **“These findings support a repeat-dependent but RFC1 protein–independent cause of neuronal dysfunction in CANVAS, with implications for therapeutic development in this currently untreatable condition.”** (maltby2024aagggrepeatexpansions pages 1-2)
- Scriba et al., *Brain Communications*, July 2023, DOI [10.1093/braincomms/fcad208](https://doi.org/10.1093/braincomms/fcad208): the authors found pathogenic expansions in 15.3% of their neurological cohort and concluded that RFC1 expansions make a substantial contribution to Australasian neurological disease, supporting combined short- and long-read diagnostic workflows. (scriba2023rfc1inan pages 3-4)
- Ronco et al., *Neurology*, January 2023, DOI [10.1212/WNL.0000000000201486](https://doi.org/10.1212/WNL.0000000000201486), PMID **36478048**: **“Full RFC1 sequencing is recommended in cases affected by typical CANVAS and carrying monoallelic (AAGGG)n expansions.”** (ronco2023truncatingvariantsin pages 1-2)

## Evidence gaps

Reliable population incidence and prevalence, motif-specific penetrance, sex ratios, validated quality-of-life norms, environmental modifiers, fluid biomarkers, single-cell/spatial atlases, natural animal disease, robust whole-animal models, and disease-modifying treatment data remain unavailable. Frequencies vary substantially with ascertainment and disease stage; cohort percentages should therefore not be treated as universal penetrance estimates.

References

1. (OpenTargets Search: CANVAS): Open Targets Query (CANVAS, 17 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (traschutz2021naturalhistoryphenotypic pages 1-2): Andreas Traschütz, Andrea Cortese, Selina Reich, Natalia Dominik, Jennifer Faber, Heike Jacobi, Annette M. Hartmann, Dan Rujescu, Solveig Montaut, Andoni Echaniz-Laguna, Sevda Erer, Valerie Cornelia Schütz, Alexander A. Tarnutzer, Marc Sturm, Tobias B. Haack, Nadège Vaucamps-Diedhiou, Helene Puccio, Ludger Schöls, Thomas Klockgether, Bart P. van de Warrenburg, Martin Paucar, Dagmar Timmann, Ralf-Dieter Hilgers, Jose Gazulla, Michael Strupp, German Moris, Alessandro Filla, Henry Houlden, Mathieu Anheim, Jon Infante, A. Nazli Basak, Matthis Synofzik, Banu Özen Barut, Basar Bilgic, Cavit Boz, Cécile Cauquil, Natalie Deininger, Claudia Dufke, Bülent Elibol, Furkan Erbas, Sibel Ertan, Fatma Genc, Ina Giegling, Yesim Parman, Salvatore Rossi, Celal Salcin, Meliha Tan, Hilal Taştekin, Christine Tranchant, Günes Uygun, and Özge Yagcioglu Yassa. Natural history, phenotypic spectrum, and discriminative features of multisystemic rfc1 disease. Neurology, Mar 2021. URL: https://doi.org/10.1212/wnl.0000000000011528, doi:10.1212/wnl.0000000000011528. This article has 193 citations and is from a highest quality peer-reviewed journal.

3. (cortese2019biallelicexpansionof pages 4-6): Andrea Cortese, Roberto Simone, Roisin Sullivan, Jana Vandrovcova, Huma Tariq, Wai Yan Yau, Jack Humphrey, Zane Jaunmuktane, Prasanth Sivakumar, James Polke, Muhammad Ilyas, Eloise Tribollet, Pedro J. Tomaselli, Grazia Devigili, Ilaria Callegari, Maurizio Versino, Vincenzo Salpietro, Stephanie Efthymiou, Diego Kaski, Nick W. Wood, Nadja S. Andrade, Elena Buglo, Adriana Rebelo, Alexander M. Rossor, Adolfo Bronstein, Pietro Fratta, Wilson J. Marques, Stephan Züchner, Mary M. Reilly, and Henry Houlden. Biallelic expansion of an intronic repeat in rfc1 is a common cause of late-onset ataxia. Nature Genetics, 51(4):649-658, Mar 2019. URL: https://doi.org/10.1038/s41588-019-0372-4, doi:10.1038/s41588-019-0372-4. This article has 650 citations and is from a highest quality peer-reviewed journal.

4. (ronco2023truncatingvariantsin pages 1-2): Riccardo Ronco, Cecilia Perini, Riccardo Currò, Natalia Dominik, Stefano Facchini, Alice Gennari, Roberto Simone, Skye Stuart, Sara Nagy, Elisa Vegezzi, Ilaria Quartesan, Amar El-Saddig, Timothy Lavin, Arianna Tucci, Agnieszka Szymura, Luiz Eduardo Novis De Farias, Alexander Gary, Megan Delfeld, Priscilla Kandikatla, Nifang Niu, Sanjukta Tawde, Joseph Shaw, James Polke, Mary M. Reilly, Nick W. Wood, Emmanuele Crespan, Christopher Gomez, Jin Yun Helen Chen, Jeremy Dan Schmahmann, David Gosal, Henry Houlden, Soma Das, and Andrea Cortese. Truncating variants in <i>rfc1</i> in cerebellar ataxia, neuropathy, and vestibular areflexia syndrome. Jan 2023. URL: https://doi.org/10.1212/wnl.0000000000201486, doi:10.1212/wnl.0000000000201486. This article has 69 citations and is from a highest quality peer-reviewed journal.

5. (scriba2023rfc1inan pages 3-4): Carolin K Scriba, Igor Stevanovski, Sanjog R Chintalaphani, Hasindu Gamaarachchi, Roula Ghaoui, Darshan Ghia, Robert D Henderson, Nerissa Jordan, Antony Winkel, Phillipa J Lamont, Miriam J Rodrigues, Richard H Roxburgh, Ben Weisburd, Nigel G Laing, Ira W Deveson, Mark R Davis, and Gianina Ravenscroft. Rfc1 in an australasian neurological disease cohort: extending the genetic heterogeneity and implications for diagnostics. Brain Communications, Jul 2023. URL: https://doi.org/10.1093/braincomms/fcad208, doi:10.1093/braincomms/fcad208. This article has 20 citations and is from a peer-reviewed journal.

6. (curro2024roleofthe pages 10-12): Riccardo Currò, Natalia Dominik, Stefano Facchini, Elisa Vegezzi, Roisin Sullivan, Valentina Galassi Deforie, Gorka Fernández-Eulate, Andreas Traschütz, Salvatore Rossi, Matteo Garibaldi, Mariusz Kwarciany, Franco Taroni, Alfredo Brusco, Jean-Marc Good, Francesca Cavalcanti, Simon Hammans, Gianina Ravenscroft, Richard H Roxburgh, Ricardo Parolin Schnekenberg, Bianca Rugginini, Elena Abati, Arianna Manini, Ilaria Quartesan, Arianna Ghia, Adolfo Lòpez de Munaìn, Fiore Manganelli, Marina Kennerson, Filippo Maria Santorelli, Jon Infante, Wilson Marques, Manu Jokela, Sinéad M Murphy, Paola Mandich, Gian Maria Fabrizi, Chiara Briani, David Gosal, Davide Pareyson, Alberto Ferrari, Ferran Prados, Tarek Yousry, Vikram Khurana, Sheng-Han Kuo, James Miller, Claire Troakes, Zane Jaunmuktane, Paola Giunti, Annette Hartmann, Nazli Basak, Matthis Synofzik, Tanya Stojkovic, Marios Hadjivassiliou, Mary M Reilly, Henry Houlden, and Andrea Cortese. Role of the repeat expansion size in predicting age of onset and severity in rfc1 disease. MedRxiv, 147:1887-1898, Oct 2024. URL: https://doi.org/10.1101/2023.10.15.23297048, doi:10.1101/2023.10.15.23297048. This article has 42 citations.

7. (curro2024roleofthe pages 15-17): Riccardo Currò, Natalia Dominik, Stefano Facchini, Elisa Vegezzi, Roisin Sullivan, Valentina Galassi Deforie, Gorka Fernández-Eulate, Andreas Traschütz, Salvatore Rossi, Matteo Garibaldi, Mariusz Kwarciany, Franco Taroni, Alfredo Brusco, Jean-Marc Good, Francesca Cavalcanti, Simon Hammans, Gianina Ravenscroft, Richard H Roxburgh, Ricardo Parolin Schnekenberg, Bianca Rugginini, Elena Abati, Arianna Manini, Ilaria Quartesan, Arianna Ghia, Adolfo Lòpez de Munaìn, Fiore Manganelli, Marina Kennerson, Filippo Maria Santorelli, Jon Infante, Wilson Marques, Manu Jokela, Sinéad M Murphy, Paola Mandich, Gian Maria Fabrizi, Chiara Briani, David Gosal, Davide Pareyson, Alberto Ferrari, Ferran Prados, Tarek Yousry, Vikram Khurana, Sheng-Han Kuo, James Miller, Claire Troakes, Zane Jaunmuktane, Paola Giunti, Annette Hartmann, Nazli Basak, Matthis Synofzik, Tanya Stojkovic, Marios Hadjivassiliou, Mary M Reilly, Henry Houlden, and Andrea Cortese. Role of the repeat expansion size in predicting age of onset and severity in rfc1 disease. MedRxiv, 147:1887-1898, Oct 2024. URL: https://doi.org/10.1101/2023.10.15.23297048, doi:10.1101/2023.10.15.23297048. This article has 42 citations.

8. (curro2024roleofthe pages 4-7): Riccardo Currò, Natalia Dominik, Stefano Facchini, Elisa Vegezzi, Roisin Sullivan, Valentina Galassi Deforie, Gorka Fernández-Eulate, Andreas Traschütz, Salvatore Rossi, Matteo Garibaldi, Mariusz Kwarciany, Franco Taroni, Alfredo Brusco, Jean-Marc Good, Francesca Cavalcanti, Simon Hammans, Gianina Ravenscroft, Richard H Roxburgh, Ricardo Parolin Schnekenberg, Bianca Rugginini, Elena Abati, Arianna Manini, Ilaria Quartesan, Arianna Ghia, Adolfo Lòpez de Munaìn, Fiore Manganelli, Marina Kennerson, Filippo Maria Santorelli, Jon Infante, Wilson Marques, Manu Jokela, Sinéad M Murphy, Paola Mandich, Gian Maria Fabrizi, Chiara Briani, David Gosal, Davide Pareyson, Alberto Ferrari, Ferran Prados, Tarek Yousry, Vikram Khurana, Sheng-Han Kuo, James Miller, Claire Troakes, Zane Jaunmuktane, Paola Giunti, Annette Hartmann, Nazli Basak, Matthis Synofzik, Tanya Stojkovic, Marios Hadjivassiliou, Mary M Reilly, Henry Houlden, and Andrea Cortese. Role of the repeat expansion size in predicting age of onset and severity in rfc1 disease. MedRxiv, 147:1887-1898, Oct 2024. URL: https://doi.org/10.1101/2023.10.15.23297048, doi:10.1101/2023.10.15.23297048. This article has 42 citations.

9. (gisatulin2020clinicalspectrumof pages 5-9): Maria Gisatulin, Valerija Dobricic, Christine Zühlke, Yorck Hellenbroich, Vera Tadic, Alexander Münchau, Klaus Isenhardt, Katrin Bürk, Melanie Bahlo, Paul J. Lockhart, Katja Lohmann, Christoph Helmchen, and Norbert Brüggemann. Clinical spectrum of the pentanucleotide repeat expansion in the <i>rfc1</i> gene in ataxia syndromes. Nov 2020. URL: https://doi.org/10.1212/wnl.0000000000010744, doi:10.1212/wnl.0000000000010744. This article has 64 citations and is from a highest quality peer-reviewed journal.

10. (gisatulin2020clinicalspectrumof pages 1-5): Maria Gisatulin, Valerija Dobricic, Christine Zühlke, Yorck Hellenbroich, Vera Tadic, Alexander Münchau, Klaus Isenhardt, Katrin Bürk, Melanie Bahlo, Paul J. Lockhart, Katja Lohmann, Christoph Helmchen, and Norbert Brüggemann. Clinical spectrum of the pentanucleotide repeat expansion in the <i>rfc1</i> gene in ataxia syndromes. Nov 2020. URL: https://doi.org/10.1212/wnl.0000000000010744, doi:10.1212/wnl.0000000000010744. This article has 64 citations and is from a highest quality peer-reviewed journal.

11. (maltby2024aagggrepeatexpansions pages 1-2): Connor J. Maltby, Amy Krans, Samantha J. Grudzien, Yomira Palacios, Jessica Muiños, Andrea Suárez, Melissa Asher, Sydney Willey, Kinsey Van Deynze, Camille Mumm, Alan P. Boyle, Andrea Cortese, Alain Ndayisaba, Vikram Khurana, Sami J. Barmada, Anke A. Dijkstra, and Peter K. Todd. Aaggg repeat expansions trigger<i>rfc1</i>-independent synaptic dysregulation in human canvas neurons. Sep 2024. URL: https://doi.org/10.1126/sciadv.adn2321, doi:10.1126/sciadv.adn2321. This article has 26 citations and is from a highest quality peer-reviewed journal.

12. (maltby2024aagggrepeatexpansions pages 13-14): Connor J. Maltby, Amy Krans, Samantha J. Grudzien, Yomira Palacios, Jessica Muiños, Andrea Suárez, Melissa Asher, Sydney Willey, Kinsey Van Deynze, Camille Mumm, Alan P. Boyle, Andrea Cortese, Alain Ndayisaba, Vikram Khurana, Sami J. Barmada, Anke A. Dijkstra, and Peter K. Todd. Aaggg repeat expansions trigger<i>rfc1</i>-independent synaptic dysregulation in human canvas neurons. Sep 2024. URL: https://doi.org/10.1126/sciadv.adn2321, doi:10.1126/sciadv.adn2321. This article has 26 citations and is from a highest quality peer-reviewed journal.

13. (maltby2024aagggrepeatexpansions pages 11-13): Connor J. Maltby, Amy Krans, Samantha J. Grudzien, Yomira Palacios, Jessica Muiños, Andrea Suárez, Melissa Asher, Sydney Willey, Kinsey Van Deynze, Camille Mumm, Alan P. Boyle, Andrea Cortese, Alain Ndayisaba, Vikram Khurana, Sami J. Barmada, Anke A. Dijkstra, and Peter K. Todd. Aaggg repeat expansions trigger<i>rfc1</i>-independent synaptic dysregulation in human canvas neurons. Sep 2024. URL: https://doi.org/10.1126/sciadv.adn2321, doi:10.1126/sciadv.adn2321. This article has 26 citations and is from a highest quality peer-reviewed journal.

14. (NCT07156214 chunk 1):  Pathogenic Insights and Search for Biomarkers in RFC1-ataxia/CANVAS. Catholic University of the Sacred Heart. 2024. ClinicalTrials.gov Identifier: NCT07156214

15. (maltby2024aagggrepeatexpansions pages 2-3): Connor J. Maltby, Amy Krans, Samantha J. Grudzien, Yomira Palacios, Jessica Muiños, Andrea Suárez, Melissa Asher, Sydney Willey, Kinsey Van Deynze, Camille Mumm, Alan P. Boyle, Andrea Cortese, Alain Ndayisaba, Vikram Khurana, Sami J. Barmada, Anke A. Dijkstra, and Peter K. Todd. Aaggg repeat expansions trigger<i>rfc1</i>-independent synaptic dysregulation in human canvas neurons. Sep 2024. URL: https://doi.org/10.1126/sciadv.adn2321, doi:10.1126/sciadv.adn2321. This article has 26 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Adult-Onset_Ataxia_and_Polyneuropathy-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 4 |
| Off topic | 0 |

All extracted references resolved successfully.