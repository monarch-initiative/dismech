---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-26T22:05:56.186841'
end_time: '2026-08-26T22:15:38.463835'
duration_seconds: 582.28
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Spina Bifida Cystica
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 35
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 3
  off_topic: 3
  off_topic_references:
  - DOI:10.1542/peds.2019-1544
  - DOI:10.1590/2526-8910.ctoAR291837922
  - DOI:10.1590/2526-8910.ctoar291837922
  needs_review: true
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Spina_Bifida_Cystica-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Spina Bifida Cystica
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Spina Bifida Cystica** covering all of the
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
- **Disease Name:** Spina Bifida Cystica
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Spina Bifida Cystica** covering all of the
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


# Spina Bifida Cystica: Comprehensive Disease-Characteristics Report

## Executive summary

Spina bifida cystica is a congenital open or sac-forming spinal dysraphism caused by failed closure of the caudal neural tube during the first four embryonic weeks. Its principal forms are **myelomeningocele/meningomyelocele**, in which neural tissue and meninges protrude through a vertebral defect, and **meningocele**, in which the sac contains meninges and cerebrospinal fluid without exposed spinal cord. Myelomeningocele (MMC) is the clinically dominant and most severe survivable form. It produces lesion-level-dependent paralysis and sensory loss, neurogenic bladder and bowel, orthopedic deformity, Chiari II malformation, hydrocephalus, and variable neurocognitive and psychosocial disability. It is congenital and lifelong rather than degenerative, although hydrocephalus, shunt failure, tethered cord, renal injury, skin breakdown, pain, and musculoskeletal problems can cause secondary deterioration.

Current understanding is that most nonsyndromic disease is **complex, multifactorial, polygenic, and incompletely penetrant**. The strongest recent genetic result is the 2024 identification of the recurrent **22q11.2 deletion**, with **CRKL haploinsufficiency** as a major candidate mechanism and maternal folate status modifying penetrance in mice. Preventive folic acid, prenatal ultrasound/MRI, multidisciplinary lifelong care, and—in selected pregnancies—prenatal repair are established real-world interventions. Prenatal repair improves motor and hydrocephalus-related outcomes but is not curative and carries maternal and prematurity risks. Placental mesenchymal-stromal-cell augmentation of fetal repair remains investigational.

| Domain | Key finding | Evidence type/sample | Quantitative result | Source/date/URL |
|---|---|---|---|---|
| Genetics / structural variation | Common 22q11.2 deletion is a strong risk factor for meningomyelocele; CRKL prioritized as key deleted gene, with folate-sensitive effect in mouse follow-up | Human trio exome/genome sequencing; 715 parent-offspring trios in Spina Bifida Sequencing Consortium, plus independent 22q11.2 deletion cohort of 1,522 individuals (vong2024riskofmeningomyelocele pages 2-4, vong2024riskofmeningomyelocele pages 1-2) | 6/715 cases had 22q11.2del (0.839%); OR vs gnomAD 22.98 (95% CI 6.47–81.61; P=9.16×10^-6); independent 22q11.2del cohort: 8/1522 with MM (0.526%), OR 12.28–15.54 depending on comparator (vong2024riskofmeningomyelocele pages 2-4, vong2024riskofmeningomyelocele pages 1-2) | Vong et al., *Science* 2024-05-03, DOI: 10.1126/science.adl1624, https://doi.org/10.1126/science.adl1624 (vong2024riskofmeningomyelocele pages 2-4, vong2024riskofmeningomyelocele pages 1-2) |
| Genetics / GWAS | Novel exonic loci identified in Bangladeshi spina bifida case-control/trio study | Human genotyping study; 112 case children, 121 control children, 272 mothers, 128 trios (tindula2024genome‐wideanalysisof pages 1-3) | Trio TDT hits: rs140199800 (*SULT1C2*) P=1.9×10^-7; rs45580033 (*ASB2*) P=4.2×10^-10; rs75426652 (*LHPP*) P=7.2×10^-14; no genome-wide significant variants in case-control models (tindula2024genome‐wideanalysisof pages 1-3) | Tindula et al., *Birth Defects Research* 2024-03, DOI: 10.1002/bdr2.2331, https://doi.org/10.1002/bdr2.2331 (tindula2024genome‐wideanalysisof pages 1-3) |
| Genetics / systems biology WGS | Rare likely gene-disrupting variants implicate pathway-level risk rather than single-gene hits; enriched pathways include carbon metabolism, inflammation, innate immunity, cytoskeletal regulation, transcription | Human ancestry-matched whole-genome case-control analysis; 149 cases + 149 controls after QC/matching (aguiarpulido2021systemsbiologyanalysis pages 1-3) | 41,005,720 cohort-level variants initially; 22,502,019 rare variants retained; RF model AUROC 0.78; 439 discriminatory genes highlighted for enrichment analysis (aguiarpulido2021systemsbiologyanalysis pages 1-3) | Aguiar-Pulido et al., *PNAS* 2021-12-16, DOI: 10.1073/pnas.2106844118, https://doi.org/10.1073/pnas.2106844118 (aguiarpulido2021systemsbiologyanalysis pages 1-3) |
| Surgery / long-term outcomes | Prenatal repair improves mobility and reduces hydrocephalus-related surgery burden at school age, but not overall adaptive behavior | Human follow-up cohort from randomized MOMS trial; 161 children assessed at age 5.9–10.3 years (houtrow2020prenatalrepairof pages 1-2) | Vineland composite 89.0 vs 87.5 (P=.35); walking without orthotics/devices 29% vs 11% (P=.06); FRESNO 92±9 vs 85±18 (P<.001); hindbrain herniation 60% vs 87% (P<.001); shunt placement 49% vs 85% (P<.001); shunt revisions 47% vs 70% (P=.02) (houtrow2020prenatalrepairof pages 1-2) | Houtrow et al., *Pediatrics* 2020-02, DOI: 10.1542/peds.2019-1544, https://doi.org/10.1542/peds.2019-1544 (houtrow2020prenatalrepairof pages 1-2) |
| Epidemiology / mortality | Long-term Swedish registry shows falling prevalence and major first-year survival gains; adult deaths emphasize psychosocial and urinary/bladder risks | Population-based registry study in Sweden; 1,735 people with spina bifida, 1973–2021 (andersson2024mortalityratescause pages 1-2) | Prevalence fell from 5.2 to 1.2 per 10,000 births; first-year survival rose from 75% to 94%; childhood causes of death: congenital abnormalities, hydrocephalus, infections; adult excesses included self-inflicted injuries/substance abuse and bladder malignancy (andersson2024mortalityratescause pages 1-2) | Andersson et al., *Acta Paediatrica* 2024-05, DOI: 10.1111/apa.17275, https://doi.org/10.1111/apa.17275 (andersson2024mortalityratescause pages 1-2) |
| Epidemiology / mortality synthesis | Infant and neonatal mortality have declined over time; prematurity and low birthweight are the strongest infant mortality predictors | Systematic review/meta-analysis of 20 population-based studies; >30 million live births and ~12,000 spina bifida-affected infants (ho2021neonatalandinfant pages 1-2, ho2021neonatalandinfant pages 13-15) | IMR decreased 4.76% per 100,000 live births per year; infant case fatality decreased 2.70% per year; preterm birth RR 4.45 (2.30–8.60); low birthweight RR 4.77 (2.67–8.55) (ho2021neonatalandinfant pages 1-2, ho2021neonatalandinfant pages 13-15) | Ho et al., *PLOS ONE* 2021-05-12, DOI: 10.1371/journal.pone.0250098, https://doi.org/10.1371/journal.pone.0250098 (ho2021neonatalandinfant pages 1-2, ho2021neonatalandinfant pages 13-15) |
| Prevention / folate | Folic acid remains the most established preventive intervention for neural tube defects; mechanism linked to one-carbon metabolism and DNA methylation | Narrative review focused on Visegrad countries and broader NTD prevention literature (risova2024preconceptionalandpericonceptional pages 1-3) | FA supplementation during preconception/periconception reduces NTD incidence by nearly 80%; recommended dose 400 µg/day; folate deficiency may exceed 20% in many lower-income countries and is typically <5% in higher-income countries (risova2024preconceptionalandpericonceptional pages 1-3) | Rísová et al., *Nutrients* published 2024-12-31, DOI: 10.3390/nu17010126, https://doi.org/10.3390/nu17010126 (risova2024preconceptionalandpericonceptional pages 1-3) |
| Rehabilitation / function | Independence-focused rehabilitation evidence supports camp-based, CO-OP, occupation-based, self-catheterization, wheelchair, and assistive-tech interventions | Integrative review; 523 records screened, 19 met criteria, 18 intervention studies analyzed (ferreira2024interventionstoimprove pages 1-3) | 18 intervention studies synthesized; strongest support reported for camp-based interventions, CO-OP, and occupation-based therapy to improve ADLs/IADLs independence (ferreira2024interventionstoimprove pages 1-3) | Ferreira & Alves, *Cadernos Brasileiros de Terapia Ocupacional* 2024, DOI: 10.1590/2526-8910.ctoAR291837922, https://doi.org/10.1590/2526-8910.ctoAR291837922 (ferreira2024interventionstoimprove pages 1-3) |
| Experimental therapy / trial | CuRe tests placenta-derived mesenchymal stem cells added to fetal repair to improve motor and autonomic outcomes beyond standard fetal surgery | Interventional Phase 1/2a clinical trial; estimated enrollment 55, recruiting; 35 treated + 20 contemporaneous non-PMSC cohort (NCT04652908 chunk 1, NCT04652908 chunk 2) | Primary endpoint: safety at birth (CSF leak, infection, wound healing failure, unexpected growth/tumor); secondary efficacy at 30 months includes motor improvement ≥2 levels over expected and independent walking, plus bowel/urologic outcomes (NCT04652908 chunk 1, NCT04652908 chunk 2) | ClinicalTrials.gov NCT04652908, first posted 2020-12-03; recruiting update verified 2026-01, https://clinicaltrials.gov/study/NCT04652908 (NCT04652908 chunk 1, NCT04652908 chunk 2) |


*Table: This compact evidence matrix summarizes high-value recent and foundational studies across genetics, prevention, surgery, prognosis, rehabilitation, and experimental therapy for spina bifida cystica/myelomeningocele. It is useful for rapidly mapping claims to quantitative evidence and source URLs.*

## 1. Disease information

### Definition and classification

Spina bifida cystica denotes a visible cystic/open defect produced by incomplete formation of the posterior vertebral arches and neural-tube coverings. In MMC, spinal cord/neural placode and meninges protrude through the defect; in meningocele, only meninges and cerebrospinal fluid protrude. “Open spina bifida,” “spina bifida aperta,” “myelomeningocele,” “meningomyelocele,” “myeloschisis,” and “open neural-tube defect” are common overlapping terms, although myeloschisis specifically describes a flat, open neural placode without a well-formed sac. MMC is described in recent primary literature as “one of the most severe forms of neural tube defects” and “the most frequent structural birth defect of the central nervous system.” (vong2024riskofmeningomyelocele pages 1-2)

This entity must be distinguished from **spina bifida occulta/closed spinal dysraphism**, in which skin covers the defect and the phenotype may involve lipoma, dermal sinus, split cord, or tethering rather than an exposed placode.

### Identifiers

* **MONDO:** MONDO:0017069, spina bifida cystica. The broader parent is MONDO:0008449, spina bifida.
* **MeSH:** D008591, Meningomyelocele; parent D009436, Neural Tube Defects. ClinicalTrials.gov uses D008591 for the open MMC phenotype. (NCT04027374 chunk 2)
* **ICD-10:** Q05.-, spina bifida; subcodes specify cervical, thoracic, lumbar, or sacral level and presence/absence of hydrocephalus.
* **ICD-11:** LA02, spina bifida, with extension coding for anatomy and associated manifestations.
* **OMIM:** MMC/spina bifida is genetically heterogeneous and generally does not have one definitive monogenic OMIM disease entry. Gene-specific or syndromic NTD entries should be represented separately rather than assigning one causal OMIM number to all cystic spina bifida.
* **SNOMED CT:** concepts include myelomeningocele and meningocele; local terminology-server verification is recommended before production ingestion.

The evidence summarized here is predominantly **aggregated disease-level evidence** from registries, cohorts, trials, and genomic studies—not an individual EHR. Individual-patient sequencing and clinical observations contribute to those aggregated studies.

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal framework

The upstream developmental event is failed neurulation, normally completed approximately **21–28 days after fertilization**. Failure of caudal neuropore closure leaves neural tissue exposed. A widely accepted **two-hit model** proposes: (1) primary failure of closure and abnormal cord development; then (2) progressive chemical and mechanical injury from amniotic fluid and fetal movement. A fetal-surgery protocol states that without protective coverage, “secondary destruction of the exposed neural tissue by trauma or amniotic fluid may occur throughout gestation.” (risova2024preconceptionalandpericonceptional pages 1-3, NCT04027374 chunk 1)

### Genetic susceptibility

Most isolated MMC is non-Mendelian. Heritability has been estimated as high as **70%**, but this does not imply that 70% of patients carry one identifiable pathogenic variant. Rare variants, polygenic background, maternal and fetal genotypes, epigenetic state, and exposures interact. (vong2024riskofmeningomyelocele pages 1-2, aguiarpulido2021systemsbiologyanalysis pages 1-3)

Important susceptibility pathways and genes include:

* **Noncanonical WNT/planar-cell-polarity and convergent extension:** *VANGL1, VANGL2, CELSR1, SCRIB, DACT1, PARD3* and related genes. Rare/ultrarare WNT-pathway variants occur in an estimated 1–3% of patients, but many are susceptibility alleles rather than fully penetrant monogenic causes. (vong2024riskofmeningomyelocele pages 1-2)
* **Apical constriction/cytoskeletal morphogenesis:** *SHROOM3*.
* **Folate/one-carbon metabolism:** *MTHFR, MTR, MTRR, MTHFD1, SLC25A32*.
* **Developmental transcription and epithelial regulation:** *TBXT, GRHL2, GRHL3*.
* **Structural variation:** 22q11.2 deletion, discussed below.

Open Targets lists associations for *MTRR, MTHFR, VANGL1, SLC25A32, MTR, VANGL2, PARD3, SCRIB, DACT1, SHROOM3, MTHFD1,* and *TBXT*. These are association-level targets and should not all be labelled clinically proven causal genes. (OpenTargets Search: spina bifida,myelomeningocele)

### Environmental and maternal risks

Established or repeatedly supported risks include insufficient periconceptional folate, low vitamin B12, pregestational diabetes, maternal obesity, hyperthermia/fever during neurulation, and folate-antagonist or antiseizure drugs—especially **valproate**. Smoking, pesticides, arsenic, polycyclic aromatic hydrocarbons, selected infections, and **fumonisin** mycotoxin exposure have varying, generally less definitive evidence. Recent literature explicitly identifies maternal diabetes, valproate, and fumonisin as risk-enhancing exposures. (risova2024preconceptionalandpericonceptional pages 1-3, vong2024riskofmeningomyelocele pages 1-2)

There is no established infectious organism that directly causes spina bifida cystica; infection is a possible maternal exposure or a downstream complication, not a transmissible etiology. Alcohol and smoking avoidance is prudent for general fetal health, but their spina-bifida-specific effect is weaker than folate, diabetes, obesity, hyperthermia, and valproate evidence.

### Protective factors

The principal proven environmental protection is adequate **periconceptional folate**. Randomized trials summarized in a review published 31 December 2024 found nearly **80% reduction in NTD incidence**, supporting **400 µg folic acid daily** for women capable of pregnancy. High-risk regimens commonly use 4–5 mg/day under clinician supervision, beginning before conception, because closure occurs before many pregnancies are recognized. Food fortification reduces population prevalence and addresses unplanned pregnancy. (risova2024preconceptionalandpericonceptional pages 1-3)

No reproducible “protective allele” is ready for clinical use. Likewise, no exercise, vaccine, or postconception lifestyle intervention can reverse a closure defect once formed.

### Direct gene–environment evidence: 22q11.2–CRKL–folate

In 715 parent–offspring trios, six patients had 22q11.2 deletions: four de novo and two inherited. Frequency was 0.839% versus 0.0368% in gnomAD controls, **OR 22.98** (95% CI 6.47–81.61). An independent cohort of 1,522 deletion carriers contained eight MMC cases, implying **12.28- to 15.54-fold** excess risk. *CRKL* was strongly expressed in developing neural tube; Crkl loss reproduced NTDs in mice, and folate deficiency worsened penetrance and expressivity, while supplementation partly alleviated risk. The authors’ exact conclusion was: “the common 22q11.2 deletion confers substantial meningomyelocele risk, which is partially alleviated by folate supplementation.” This is unusually strong evidence linking human structural variation, developmental expression, animal function, and environmental modification. (vong2024riskofmeningomyelocele pages 2-4, vong2024riskofmeningomyelocele pages 1-2)

## 3. Phenotypes

Phenotypes are present at birth, although prenatal imaging can identify them earlier. Severity is highly variable and is driven mainly by anatomical/functional lesion level, preservation of neural tissue, hydrocephalus/Chiari II, and complications.

* **Open/cystic spinal lesion**—congenital, usually lumbosacral; severity ranges from isolated meningocele to exposed MMC/myeloschisis. Suggested HPO: **Myelomeningocele (HP:0002475)**; Meningocele; Spina bifida.
* **Lower-limb weakness or paralysis and sensory loss**—congenital, generally stable at baseline but may worsen with tethering, shunt dysfunction, syrinx, or orthopedic complications. HPO: Paraparesis, Paraplegia, Lower-limb muscle weakness, Hyporeflexia, Impaired pain sensation.
* **Neurogenic bladder**—very common in MMC; may cause retention, incontinence, vesicoureteral reflux, recurrent UTI, hydronephrosis, renal scarring, and chronic kidney disease. HPO: **Neurogenic bladder (HP:0000011)**, Urinary incontinence, Recurrent UTI, Hydronephrosis.
* **Neurogenic bowel/constipation and fecal incontinence**—reported in approximately 90% in one clinical synthesis, although frequency depends on definition. HPO: Neurogenic bowel, Constipation, Fecal incontinence. (mathew2018antenataldiagnosismaternal pages 14-17)
* **Chiari II malformation and hydrocephalus**—most severe MMC cases have Chiari II; hindbrain herniation was reported in >80% in one synthesis. Consequences include shunt dependence, brainstem dysfunction, swallowing/respiratory problems, and cognitive effects. HPO: **Chiari malformation type II (HP:0002308)**, Hydrocephalus (HP:0000238), Ventriculomegaly.
* **Orthopedic manifestations**—clubfoot, hip dislocation/subluxation, scoliosis/kyphosis, contractures, reduced bone density and fractures. HPO: Talipes equinovarus, Scoliosis, Kyphosis, Hip dislocation, Joint contracture.
* **Tethered cord**—often secondary to repair; clinically relevant when accompanied by new pain, weakness, deformity, gait or bladder deterioration. HPO: Tethered cord.
* **Skin and mobility complications**—pressure injury, neuropathic ulceration, obesity, reduced fitness, and wheelchair dependence. HPO: Pressure ulcer, Abnormality of gait, Inability to walk.
* **Neurocognitive/behavioral phenotype**—learning difficulties, executive dysfunction, impaired attention and visuospatial/mathematical skills can occur, especially with hydrocephalus and intracranial anomalies. Global intellectual disability is not obligatory. (houtrow2020prenatalrepairof pages 1-2)
* **Pain, depression, anxiety, social isolation, and sexual dysfunction** contribute substantially to adult burden. A claims cohort combining adults with cerebral palsy or spina bifida found pain disorders in 55.9% versus 35.2% of controls; this estimate is not MMC-specific and should not be used as an isolated-MMC frequency.

Quality-of-life effects include dependence in bathing, dressing, toileting, catheterization, mobility, transportation, meal preparation, and financial management. Dependence is greater with hydrocephalus and lesions above L2. A 2024 review found that camp-based interventions, Cognitive Orientation to Daily Occupational Performance, and occupation-based therapy improved independence, but the intervention literature remains heterogeneous. (ferreira2024interventionstoimprove pages 1-3)

## 4. Genetic and molecular information

### Variant interpretation

There is no universal diagnostic “spina bifida gene panel” with high yield for isolated MMC. Most reported variants are germline susceptibility alleles, rare variants, or copy-number changes with incomplete penetrance. Somatic mutation is not an established mechanism.

* **22q11.2 deletion:** pathogenic structural germline variant; inherited or de novo. In the 2024 cohort, 4/6 were de novo and 2/6 inherited from clinically unrecognized carriers, demonstrating incomplete penetrance. The minimal consensus interval contained ten protein-coding genes, with *CRKL* prioritized. (vong2024riskofmeningomyelocele pages 2-4)
* **PCP variants:** predominantly rare missense or loss-of-function susceptibility variants; classification may range from pathogenic in a defined syndrome to VUS/risk allele in isolated MMC. Each variant requires ClinVar/ClinGen and segregation review.
* **MTHFR C677T and A1298C:** common functional polymorphisms, not deterministic pathogenic variants. Approximately 60–70% of the general population carries at least one of these variants; around 10% is homozygous or compound heterozygous. These figures must not be interpreted as carrier frequencies for spina bifida. (risova2024preconceptionalandpericonceptional pages 1-3)
* **Bangladesh study:** among 112 affected children, 121 controls, 272 mothers, and 128 trios, transmission disequilibrium identified rs140199800 in *SULT1C2* (P=1.9×10⁻⁷), rs45580033 in *ASB2* (P=4.2×10⁻¹⁰), and rs75426652 in *LHPP* (P=7.2×10⁻¹⁴). Case–control models found no genome-wide-significant variants; replication is required. (tindula2024genome‐wideanalysisof pages 1-3)
* **Regulatory variation:** a 2023 mouse study identified an approximately 4-kb LTR insertion about 300 bp upstream of *Grhl2*, causing overexpression and spina bifida/encephalocele. Rare human upstream variants were found in only a small number of cases and remain candidates rather than proven clinical variants. (cranesmith2023anoncodinginsertional pages 1-2)

A WGS systems-biology study of 149 cases and 149 ancestry-matched controls found no single definitive gene after multiple-testing correction. Machine learning identified 439 discriminatory genes and pathway enrichment in carbon metabolism, inflammation/innate immunity, cytoskeletal regulation, and transcription; hold-out AUROC was 0.78. This is computational association evidence, not a validated diagnostic classifier. (aguiarpulido2021systemsbiologyanalysis pages 1-3)

### Epigenetics and molecular profiling

Folate participates in one-carbon transfer, nucleotide synthesis, DNA repair, and methylation. Deficiency may cause DNA hypomethylation, impaired thymidylate synthesis, uracil misincorporation, and genomic instability. The exact folate-protective mechanism nevertheless remains unresolved. (risova2024preconceptionalandpericonceptional pages 1-3)

RNA-seq of five fibroblast lines from 22q11.2-deletion/MMC patients showed reduced expression largely within the deleted interval. Murine spatial transcriptomics and human embryonic single-nucleus RNA-seq demonstrated *CRKL, PI4KA,* and *LZTR1* expression in neural-tube progenitors, neurons, and neural crest. These data prioritize mechanisms but do not constitute a clinical biomarker. (vong2024riskofmeningomyelocele pages 2-4)

NCT04027374 prospectively examined neonatal saliva DNA/RNA after fetal repair, measuring methylation of stress-regulation genes **NR3C1** and **FKBP5**. It completed with 70 participants, but the retrieved registry did not provide definitive posted results; it should be cited as exploratory procedural-stress epigenomics, not disease-causal evidence. (NCT04027374 chunk 1, NCT04027374 chunk 2)

No validated diagnostic proteomic, metabolomic, lipidomic, single-cell, spatial, or liquid-biopsy signature is currently used in routine MMC care.

## 5. Environmental information

The critical exposure window is preconception through approximately day 28 after fertilization. Relevant chemical entities include folic acid (**CHEBI:27470**), folate, vitamin B12/cobalamin, valproic acid (**CHEBI:39867**), and fumonisin B1. Maternal glycemic control, healthy preconception weight, medication review, avoidance of hyperthermia, and adequate nutrition are actionable. Occupational/toxicant associations are plausible but generally lack the causal strength of folate deficiency, diabetes, obesity, and valproate. There is no zoonotic, contagious, or vaccine-preventable cause.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream susceptibility:** fetal and maternal variants/CNVs, altered PCP-WNT, epithelial polarity, cytoskeletal/apical constriction, transcription, folate/one-carbon metabolism, and relevant exposures.
2. **Failed neurulation:** defective convergent extension and dorsolateral bending/apical constriction prevent caudal neural-fold fusion during weeks 3–4.
3. **Open neural placode:** vertebral arches, meninges, muscle, and skin fail to cover the cord.
4. **Secondary fetal injury:** exposed neural tissue undergoes chemical and mechanical injury, neuronal loss, gliosis, and progressive loss of motor/sensory function.
5. **CSF/hindbrain consequences:** leakage and altered craniospinal dynamics contribute to Chiari II hindbrain herniation, impaired CSF flow, ventriculomegaly, and hydrocephalus.
6. **Clinical manifestations:** segmental paralysis/sensory loss; autonomic denervation causes neurogenic bladder and bowel; muscle imbalance causes clubfoot, hip deformity, scoliosis and contractures; hydrocephalus and cerebral anomalies contribute to learning/executive deficits.
7. **Downstream lifelong injury:** shunt failure/infection, tethering, recurrent UTI and high bladder pressure, renal damage, pressure injury, pain, obesity and psychosocial stress.

### Suggested mechanism ontologies

* GO biological process: neural tube closure; neural fold formation; convergent extension involved in neural plate elongation; planar cell polarity pathway; Wnt signaling; actin-cytoskeleton organization; epithelial-cell apical constriction; folic-acid metabolic process; one-carbon metabolic process; DNA methylation; neurogenesis; inflammatory response.
* Cell Ontology: neuroepithelial cell/neural progenitor cell; neuron; neural crest cell; radial glial cell; astrocyte; oligodendrocyte-lineage cell; ependymal cell; choroid-plexus epithelial cell; skeletal myocyte; urothelial cell.
* GO cellular component: adherens junction, apical plasma membrane, actin cytoskeleton, nucleus/chromatin, mitochondrion. These are pathway-relevant compartments; no single organelle defect defines MMC.

The immune system is not the primary cause, although inflammation appears in systems-level genomic enrichment and contributes downstream to exposed-tissue injury, shunt infection, UTI, and chronic wounds. (aguiarpulido2021systemsbiologyanalysis pages 1-3)

## 7. Anatomical structures affected

The primary site is the caudal neural tube and posterior vertebral column, most often lumbar/lumbosacral. Affected structures include spinal cord/neural placode, spinal nerve roots, meninges, vertebral arches, paraspinal muscle and skin. Suggested terms include **UBERON:0002240 spinal cord**, vertebral column, lumbar spinal cord, sacral spinal cord, meninges, skin of back, and skeletal muscle tissue.

Secondary structures include cerebellum and hindbrain/brainstem in Chiari II, cerebral ventricles and CSF pathways, lower-limb peripheral nerves and muscle, hips/knees/feet/spine, urinary bladder, ureters and kidneys, colon/rectum and pelvic floor. Lesions are midline, not meaningfully unilateral; neurological effects are commonly bilateral but may be asymmetric.

## 8. Temporal development

The initiating defect is embryonic and acute within the neurulation window, but the phenotype evolves through gestation because exposed neural tissue can sustain progressive injury. Prenatal diagnosis usually occurs during first- or second-trimester screening. After birth, the disease course is chronic and lifelong.

There is no spontaneous remission of the anatomical defect. Repair closes/protects tissue but does not regenerate all lost neural function. Critical windows are: preconception to day 28 for prevention; midgestation for fetal-repair evaluation; the first 24–48 hours after birth for closure when prenatal repair was not performed; infancy for hydrocephalus surveillance; growth periods for tethering and orthopedic progression; and adolescence for transition to adult self-management.

## 9. Inheritance and population

### Inheritance

Most isolated disease follows **multifactorial/polygenic inheritance with incomplete penetrance and variable expressivity**. Classic dominant, recessive, X-linked, mitochondrial inheritance, anticipation, and a single carrier frequency are not generally applicable. Mendelian or chromosomal syndromes form a minority and should be coded separately. Consanguinity may increase risk of rare recessive syndromic NTDs but is not the main mechanism of nonsyndromic MMC. Familial recurrence is higher than population risk and warrants genetic counseling.

### Epidemiology

Rates vary substantially by geography, ancestry, ascertainment, prenatal diagnosis/termination, folate policy, and whether stillbirths are counted. A 2024 Swedish registry study of 1,735 people found prevalence declined from **5.2 to 1.2 per 10,000 births** between 1973 and 2021. A Brazilian review cited **2.67 per 10,000 births** in 2017–2019. A U.S. MOMS follow-up paper described MMC as affecting approximately **1 in 1,500 births**, whereas the 2024 Science study noted historical prevalence greater than 1 in 2,500 before fortification. These estimates are not contradictory because definitions, periods, and populations differ. (ferreira2024interventionstoimprove pages 1-3, vong2024riskofmeningomyelocele pages 1-2, houtrow2020prenatalrepairof pages 1-2, andersson2024mortalityratescause pages 1-2)

Female excess is often reported for NTDs, but sex ratios vary and no universal cystica-specific ratio should be assigned without a defined registry. Higher historical rates occur in regions without fortification and in some Hispanic/Latino, Celtic, northern Chinese, South Asian, Middle Eastern, and African populations; social disadvantage and access to prevention, prenatal diagnosis, and surgery strongly influence observed burden.

## 10. Diagnostics

### Prenatal screening and confirmation

* **Maternal serum alpha-fetoprotein:** elevated with open NTDs, typically assessed around 15–20 weeks; it is a screening marker, not a definitive diagnosis.
* **Ultrasound:** identifies the spinal defect/sac and cranial signs such as ventriculomegaly, “lemon” and “banana” signs, and hindbrain herniation. One synthesis reported 85–90% accuracy for maternal AFP at 16 weeks or fetal ultrasound at 18–20 weeks, but performance depends on operator and protocol. (mathew2018antenataldiagnosismaternal pages 14-17)
* **Fetal MRI:** refines lesion level, hindbrain anatomy, ventriculomegaly, associated anomalies, and fetal-surgery planning.
* **Amniocentesis/CMA:** offered when anomalies or fetal surgery are being considered; karyotype/CMA assess aneuploidy and pathogenic CNVs, including 22q11.2 deletion.

Postnatally, examination defines sac integrity and functional neurological level. Cranial/spinal ultrasound and MRI assess hydrocephalus, Chiari II, cord anatomy and tethering. Renal/bladder ultrasound, serum creatinine interpreted cautiously, catheterization assessment, and urodynamics characterize neurogenic bladder. Orthopedic, developmental, vision/hearing, sleep/respiratory, and skin assessments are individualized. Biopsy is not diagnostic; EEG/EMG are not routine unless indicated.

### Genetic testing strategy

For isolated MMC, start with careful dysmorphology/family/exposure history and **chromosomal microarray**, especially when additional anomalies are present. The 2024 22q11.2 result strengthens the rationale for CNV detection. Karyotype detects large rearrangements but misses many submicroscopic CNVs; FISH is useful for targeted confirmation/family testing but not genome-wide screening. WES/WGS may be considered for syndromic, recurrent, familial, or unexplained cases, preferably as a trio. Panels may include PCP/neurulation genes but have limited validated yield. Mitochondrial and repeat-expansion testing are not routine.

Differential diagnoses include meningocele versus MMC, closed lipomyelomeningocele, myeloschisis, dermal sinus, sacrococcygeal teratoma, spinal hemangioma, caudal regression/sacral agenesis, split-cord malformation, cloacal exstrophy/OEIS, encephalocele, and amniotic-band disruption.

There is no conventional newborn biochemical screen, asymptomatic carrier screen, or validated liquid biopsy for nonsyndromic MMC.

## 11. Outcome and prognosis

Prognosis depends on lesion level, functional motor level, hydrocephalus/brainstem dysfunction, prematurity, associated anomalies, renal preservation, infection, access to multidisciplinary care, and socioeconomic context. Approximately **85%** of people with spina bifida are estimated to survive into adulthood. (andersson2024mortalityratescause pages 1-2)

In a 2021 meta-analysis of 20 population-based studies, encompassing more than 30 million births and about 12,000 affected infants, infant mortality and case-fatality declined over time. Preterm birth carried **RR 4.45** and low birthweight **RR 4.77** for infant case-fatality. Higher lesion level, hydrocephalus, multiple anomalies and social/demographic factors also increased risk. (ho2021neonatalandinfant pages 13-15, ho2021neonatalandinfant pages 1-2)

A Finnish national cohort of 181 live-born cases found **7.2% early neonatal mortality**; prematurity had uOR 6.96, syndromic status uOR 125.67, and maternal age ≥35 years uOR 5.33, although estimates were unadjusted and imprecise. (kancherla2023earlyneonatalmortality pages 1-6)

The 2024 Swedish study found first-year survival improved from **75% to 94%**. Childhood deaths were associated mainly with congenital anomalies, hydrocephalus and infection. Adult concerns included infection, kidney failure, bladder malignancy, self-inflicted injury and substance abuse, supporting proactive urological and mental-health surveillance. (andersson2024mortalityratescause pages 1-2)

Recovery of established paralysis is limited. Preservation of ambulation is more likely with lower lesions, better prenatal motor function, absence of severe deformity and selected prenatal repair. Independence and quality of life are modifiable through rehabilitation, assistive technology, bowel/bladder programs, educational support, accessible environments and effective transition care.

## 12. Treatment and real-world implementation

### Repair

For infants without prenatal repair, the lesion is covered with sterile nonadherent dressings, latex exposure is minimized, and closure is generally performed within **24–48 hours** to protect tissue and reduce infection risk. Closure does not reverse the primary developmental lesion. (mathew2018antenataldiagnosismaternal pages 14-17)

Selected fetuses with T1–S1 MMC, hindbrain herniation, suitable gestational age and no major contraindication may undergo open or fetoscopic prenatal repair at expert centers. MOMS demonstrated reduced hindbrain herniation/shunt need and improved motor outcomes, balanced against maternal hysterotomy risks and prematurity.

At school age, 161 MOMS children showed no difference in Vineland adaptive behavior (89.0 versus 87.5; P=.35), but prenatal repair yielded better FRESNO motor-function scores (92 versus 85; P<.001), less hindbrain herniation (60% versus 87%), fewer shunts (49% versus 85%), and fewer shunt revisions among shunted children (47% versus 70%). Walking without orthotics/devices was 29% versus 11% (P=.06), and parent-reported quality of life/family impact favored prenatal repair. The authors concluded there was “no strong evidence of improved cognitive functioning.” (houtrow2020prenatalrepairof pages 1-2)

### Lifelong complication management

* Hydrocephalus: ventriculoperitoneal shunt or selected endoscopic procedures; urgent evaluation of headache, vomiting, lethargy, cognitive change, swallowing/respiratory symptoms, or neurological decline.
* Bladder: clean intermittent catheterization, antimuscarinic or β3-agonist therapy when appropriate, urodynamic surveillance, antibiotic treatment for symptomatic UTI, botulinum toxin, and reconstructive surgery in selected high-pressure bladders. There is no disease-specific pharmacogenomic algorithm.
* Bowel: timed toileting, fiber/fluid optimization, osmotic or stimulant laxatives, suppositories/enemas, transanal irrigation, or antegrade continence enema.
* Orthopedics/mobility: physical therapy, orthoses, standing/walking programs, wheelchairs, contracture management and indicated orthopedic surgery.
* Skin/bone: daily inspection, pressure relief, nutrition, weight management, vitamin D/bone-health evaluation and fracture prevention.
* Tethered cord: surgery is reserved for concordant progressive neurological, urological, pain, or orthopedic deterioration—not MRI appearance alone.
* Neurodevelopment/participation: neuropsychology, school accommodations, occupational and physical therapy, self-management training, vocational planning, sexual/reproductive health, mental-health care and structured transition to adult services. A 2024 rehabilitation review retained 18 intervention studies and found increased independence with camp-based, CO-OP and occupation-based approaches. (ferreira2024interventionstoimprove pages 1-3)

Suggested NCIt intervention mappings include surgical repair procedure, fetal surgery, neurosurgical procedure, ventriculoperitoneal shunt, physical therapy, occupational therapy, rehabilitation therapy, intermittent urinary catheterization, botulinum toxin therapy, and mesenchymal stromal cell therapy. Exact NCIt identifiers should be validated against the current NCIt release.

### Experimental therapy

**CuRe, NCT04652908:** recruiting Phase 1/2a, estimated n=55; 35 participants receive placental mesenchymal stem cells seeded on extracellular-matrix dural graft during open fetal repair, with 20 contemporaneous untreated controls. Safety at birth is primary; 30-month endpoints include motor level at least two segments better than anatomical expectation, independent walking, bowel function and urodynamics. This is FDA-regulated and investigational, not standard therapy. (NCT04652908 chunk 1, NCT04652908 chunk 2)

Other recent studies include completed NCT04027374 on stress-associated neonatal epigenetic changes after fetal surgery (actual n=70); recruiting NCT06796972 on parental decision-making and psychological impact (estimated n=44); and NCT07048691, a small active observational ultrasound-outcome study (n=20). The latter records were posted in 2025 and should not be represented as 2023–2024 evidence. (NCT04027374 chunk 1, NCT04027374 chunk 2, NCT07048691 chunk 1, NCT06796972 chunk 1)

No approved gene therapy, CRISPR therapy, RNA therapy, or immune-targeted therapy exists for MMC.

## 13. Prevention

### Primary prevention

* Provide **400 µg folic acid daily** to all who may become pregnant, beginning before conception and continuing through early pregnancy; use clinician-directed high-dose folate after a prior NTD pregnancy or other high-risk circumstances.
* Implement mandatory staple-food fortification and monitor red-cell folate at population level.
* Optimize diabetes control and preconception weight.
* Review antiseizure and folate-antagonist drugs before pregnancy; do not abruptly stop essential medication. Avoid valproate where an effective safer alternative exists.
* Avoid hyperthermia and correct B12 deficiency.

Fortification has reduced prevalence and may reduce severity. Infants born in the postfortification period were reported as almost one-third less likely to die in infancy than those in the prefortification period, although concurrent improvements in diagnosis and care contribute. (ho2021neonatalandinfant pages 13-15)

### Secondary and tertiary prevention

Secondary prevention comprises maternal-serum screening, high-quality prenatal ultrasound, confirmatory MRI/genetic assessment, nondirective counseling and timely referral to fetal/pediatric neurosurgery. Prenatal repair prevents some secondary cord injury but does not prevent the initial malformation.

Tertiary prevention includes prompt closure, hydrocephalus and renal surveillance, catheterization/bowel programs, skin and orthopedic prevention, immunization according to standard schedules, rehabilitation, mental-health care, and transition planning. There is no MMC-specific vaccine or antimicrobial prophylaxis for the general population.

## 14. Other species and naturally occurring disease

Comparable congenital spinal dysraphism occurs sporadically in domestic animals, including dogs, cats, calves, lambs and foals, but robust breed-level epidemiology and validated VBO mappings are sparse. It is noninfectious and has no zoonotic or cross-species transmission. Veterinary lesions resemble human meningocele/MMC anatomically, but hydrocephalus/Chiari II and long-term multidisciplinary survival are less consistently represented. Species identifiers include human **NCBITaxon:9606**, mouse **10090**, sheep **9940**, zebrafish **7955**, chicken **9031**, dog **9615**, and cat **9685**.

## 15. Model organisms and advanced technologies

### Mouse

More than 400 mouse genes can produce NTDs, illustrating genetic heterogeneity. **Crkl** loss is a particularly strong translational model because it functionally validates the human 22q11.2 association and demonstrates folate-modified penetrance. Strengths are mechanistic genetics and controlled diet; limitations include species-specific neurulation, allele effects, and folate exposure. (vong2024riskofmeningomyelocele pages 1-2, aguiarpulido2021systemsbiologyanalysis pages 1-3)

The **Grhl2 Axial defects** model contains a noncoding LTR insertion causing excess *Grhl2* expression and spinal NTDs plus craniofacial defects. It demonstrates that regulatory gain of expression—not only protein loss—can disrupt neurulation. Human upstream variants remain unvalidated. (cranesmith2023anoncodinginsertional pages 1-2)

Other models include curly-tail/*Grhl3*, loop-tail/*Vangl2*, *Scrib*, *Celsr1*, *Shroom3* and folate-antagonist/valproate-induced models. They recapitulate closure failure but not always the human open-lesion secondary injury and Chiari II phenotype.

### Sheep and other models

Surgically created fetal sheep MMC models reproduce exposed-cord secondary injury and permit human-scale fetal repair. In-utero closure has produced near-normal motor function, intact sensation and improved bowel/bladder outcomes in preclinical studies. The limitation is that the lesion is induced surgically rather than arising through primary neurulation failure. (mathew2018antenataldiagnosismaternal pages 14-17)

Chick and zebrafish models permit live imaging and pathway manipulation but differ anatomically from human spinal neurulation. Human pluripotent-stem-cell neural tube organoids model neuroepithelial patterning, morphogenesis and toxicant response, but currently do not reproduce the complete vertebral, meningeal, amniotic-fluid, hindbrain and lifelong-organ phenotype.

## Evidence interpretation and knowledge gaps

The highest-confidence evidence consists of randomized or longitudinal MOMS outcomes, population registries/meta-analysis, randomized folate-prevention evidence, and the replicated human 22q11.2 association with mouse functional validation. Candidate-gene associations, small ancestry-specific GWAS findings, systems-biology classifiers, epigenetic observations, and stem-cell augmentation remain exploratory.

Important gaps include ancestry-diverse genomic cohorts; standardized lesion-specific phenotype frequencies; validated functional interpretation of noncoding variants; maternal–fetal genotype/exposure models; kidney, pain and mental-health outcomes across adulthood; direct comparison of open versus fetoscopic repair; and long-term safety/efficacy of cell-enhanced fetal surgery. Variant-level allele frequencies and ACMG classifications must be obtained from the current ClinVar/gnomAD record for each exact variant and should not be inferred from gene-level association.

### Selected exact source statements

* Vong et al., *Science*, 3 May 2024: “Exome and genome sequencing of 715 parent-offspring trios identified six patients with chromosomal 22q11.2 deletions, suggesting a 23-fold increased risk compared with the general population.” DOI: https://doi.org/10.1126/science.adl1624. (vong2024riskofmeningomyelocele pages 1-2)
* Houtrow et al., *Pediatrics*, February 2020: “Long-term benefits of prenatal surgery included improved mobility and independent functioning and fewer surgeries for shunt placement and revision, with no strong evidence of improved cognitive functioning.” DOI: https://doi.org/10.1542/peds.2019-1544. (houtrow2020prenatalrepairof pages 1-2)
* Ho et al., *PLOS ONE*, 12 May 2021: “Preterm birth … and low birthweight … are the strongest risk factors associated with increased spina bifida infant case fatality.” DOI: https://doi.org/10.1371/journal.pone.0250098. (ho2021neonatalandinfant pages 1-2)
* Rísová et al., published 31 December 2024: “Randomized trials have shown that FA supplementation during preconceptional and periconceptional periods reduces the incidence of NTDs by nearly 80%.” DOI: https://doi.org/10.3390/nu17010126. (risova2024preconceptionalandpericonceptional pages 1-3)

**PMID note:** The retrieved full texts did not consistently display PMIDs. To avoid false identifiers, DOI and ClinicalTrials.gov URLs are provided where verified; PubMed IDs should be added only after direct NCBI record validation.

References

1. (vong2024riskofmeningomyelocele pages 2-4): Keng Ioi Vong, Sangmoon Lee, Kit Sing Au, T. Blaine Crowley, Valeria Capra, Jeremiah Martino, Meade Haller, Camila Araújo, Hélio R. Machado, Renee George, Bryn Gerding, Kiely N. James, Valentina Stanley, Nan Jiang, Kameron Alu, Naomi Meave, Anna S. Nidhiry, Fiza Jiwani, Isaac Tang, Ashna Nisal, Ishani Jhamb, Arzoo Patel, Aakash Patel, Jennifer McEvoy-Venneri, Chelsea Barrows, Celina Shen, Yoo-Jin Ha, Robyn Howarth, Madison Strain, Allison Elizabeth Ashley-Koch, Matloob Azam, Sara Mumtaz, Gyang Markus Bot, Richard H. Finnell, Zoha Kibar, Ahmed I. Marwan, Gia Melikishvili, Hal S. Meltzer, Osvaldo M. Mutchinick, David A. Stevenson, Henry J. Mroczkowski, Betsy Ostrander, Erica Schindewolf, Julie Moldenhauer, Elaine H. Zackai, Beverly S. Emanuel, Sixto Garcia-Minaur, Beata A. Nowakowska, Roger E. Stevenson, Maha S. Zaki, Hope Northrup, Hanna K. McNamara, Kimberly A. Aldinger, Ian G. Phelps, Mei Deng, Ian A. Glass, Bernice Morrow, Donna M. McDonald-McGinn, Simone Sanna-Cherchi, Dolores J. Lamb, Joseph G. Gleeson, Allison Elizabeth Ashley Koch, Hal S. Meltzer, Joan Le, Kit Sing Au, Hope Northrup, Gyang Markus Bot, Valeria Capra, Richard H. Finnell, Zoha Kibar, Philip J. Lupo, Helio R. Machado, Camila Araújo, Tony Magana, Ahmed I. Marwan, Gia Melikishvili, Osvaldo M. Mutchinick, Roger E. Stevenson, Anna Yurrita, Maha S. Zaki, Sara Mumtaz, José Ramón Medina-Bereciartu, Caroline M. Kolvenbach, Shirlee Shril, Friedhelm Hildebrandt, Mahmoud M. Noureldeen, Aida MS. Salem, Yukitoshi Takahashi, Hormos Salimi-Dafsari, H. Westley Phillips, Brian Hanak, Bülent Kara, Ayfer Sakarya Güneş, David D. Gonda, Salman Kirmani, Tinatin Tkemaladze, and Joseph G. Gleeson. Risk of meningomyelocele mediated by the common 22q11.2 deletion. Science, 384:584-590, May 2024. URL: https://doi.org/10.1126/science.adl1624, doi:10.1126/science.adl1624. This article has 20 citations and is from a highest quality peer-reviewed journal.

2. (vong2024riskofmeningomyelocele pages 1-2): Keng Ioi Vong, Sangmoon Lee, Kit Sing Au, T. Blaine Crowley, Valeria Capra, Jeremiah Martino, Meade Haller, Camila Araújo, Hélio R. Machado, Renee George, Bryn Gerding, Kiely N. James, Valentina Stanley, Nan Jiang, Kameron Alu, Naomi Meave, Anna S. Nidhiry, Fiza Jiwani, Isaac Tang, Ashna Nisal, Ishani Jhamb, Arzoo Patel, Aakash Patel, Jennifer McEvoy-Venneri, Chelsea Barrows, Celina Shen, Yoo-Jin Ha, Robyn Howarth, Madison Strain, Allison Elizabeth Ashley-Koch, Matloob Azam, Sara Mumtaz, Gyang Markus Bot, Richard H. Finnell, Zoha Kibar, Ahmed I. Marwan, Gia Melikishvili, Hal S. Meltzer, Osvaldo M. Mutchinick, David A. Stevenson, Henry J. Mroczkowski, Betsy Ostrander, Erica Schindewolf, Julie Moldenhauer, Elaine H. Zackai, Beverly S. Emanuel, Sixto Garcia-Minaur, Beata A. Nowakowska, Roger E. Stevenson, Maha S. Zaki, Hope Northrup, Hanna K. McNamara, Kimberly A. Aldinger, Ian G. Phelps, Mei Deng, Ian A. Glass, Bernice Morrow, Donna M. McDonald-McGinn, Simone Sanna-Cherchi, Dolores J. Lamb, Joseph G. Gleeson, Allison Elizabeth Ashley Koch, Hal S. Meltzer, Joan Le, Kit Sing Au, Hope Northrup, Gyang Markus Bot, Valeria Capra, Richard H. Finnell, Zoha Kibar, Philip J. Lupo, Helio R. Machado, Camila Araújo, Tony Magana, Ahmed I. Marwan, Gia Melikishvili, Osvaldo M. Mutchinick, Roger E. Stevenson, Anna Yurrita, Maha S. Zaki, Sara Mumtaz, José Ramón Medina-Bereciartu, Caroline M. Kolvenbach, Shirlee Shril, Friedhelm Hildebrandt, Mahmoud M. Noureldeen, Aida MS. Salem, Yukitoshi Takahashi, Hormos Salimi-Dafsari, H. Westley Phillips, Brian Hanak, Bülent Kara, Ayfer Sakarya Güneş, David D. Gonda, Salman Kirmani, Tinatin Tkemaladze, and Joseph G. Gleeson. Risk of meningomyelocele mediated by the common 22q11.2 deletion. Science, 384:584-590, May 2024. URL: https://doi.org/10.1126/science.adl1624, doi:10.1126/science.adl1624. This article has 20 citations and is from a highest quality peer-reviewed journal.

3. (tindula2024genome‐wideanalysisof pages 1-3): Gwen Tindula, Biju Issac, Sudipta Kumer Mukherjee, Sheikh Muhammad Ekramullah, D. M. Arman, Joynul Islam, Hafiza Sultana Suchanda, Liang Sun, Shira Rockowitz, David C. Christiani, Benjamin C. Warf, and Maitreyi Mazumdar. Genome‐wide analysis of spina bifida risk variants in a case–control study from bangladesh. Birth Defects Research, Mar 2024. URL: https://doi.org/10.1002/bdr2.2331, doi:10.1002/bdr2.2331. This article has 5 citations and is from a peer-reviewed journal.

4. (aguiarpulido2021systemsbiologyanalysis pages 1-3): Vanessa Aguiar-Pulido, Paul Wolujewicz, Alexander Martinez-Fundichely, Eran Elhaik, Gaurav Thareja, Alice Abdel Aleem, Nader Chalhoub, Tawny Cuykendall, Jamel Al-Zamer, Yunping Lei, Haitham El-Bashir, James M. Musser, Abdulla Al-Kaabi, Gary M. Shaw, Ekta Khurana, Karsten Suhre, Christopher E. Mason, Olivier Elemento, Richard H. Finnell, and M. Elizabeth Ross. Systems biology analysis of human genomes points to key pathways conferring spina bifida risk. Dec 2021. URL: https://doi.org/10.1073/pnas.2106844118, doi:10.1073/pnas.2106844118. This article has 25 citations and is from a highest quality peer-reviewed journal.

5. (houtrow2020prenatalrepairof pages 1-2): Amy J. Houtrow, Elizabeth A. Thom, Jack M. Fletcher, Pamela K. Burrows, N. Scott Adzick, Nina H. Thomas, John W. Brock, Timothy Cooper, Hanmin Lee, Larissa Bilaniuk, Orit A. Glenn, Sumit Pruthi, Cora MacPherson, Diana L. Farmer, Mark P. Johnson, Lori J. Howell, Nalin Gupta, and William O. Walker. Prenatal repair of myelomeningocele and school-age functional outcomes. Feb 2020. URL: https://doi.org/10.1542/peds.2019-1544, doi:10.1542/peds.2019-1544. This article has 185 citations and is from a highest quality peer-reviewed journal.

6. (andersson2024mortalityratescause pages 1-2): Marie Andersson, Lana Hadi, Michaela Dellenmark Blom, Ulla Sillen, Sofia Sjöström, Magdalena Vu Minh Arnell, and Kate Abrahamsson. Mortality rates, cause and risk factors in people with spina bifida, register‐based study over five decades. Acta Paediatrica, 113:1916-1926, May 2024. URL: https://doi.org/10.1111/apa.17275, doi:10.1111/apa.17275. This article has 10 citations and is from a peer-reviewed journal.

7. (ho2021neonatalandinfant pages 1-2): Peter Ho, Maria A. Quigley, Dharamveer Tatwavedi, Carl Britto, and Jennifer J. Kurinczuk. Neonatal and infant mortality associated with spina bifida: a systematic review and meta-analysis. PLoS ONE, 16:e0250098, May 2021. URL: https://doi.org/10.1371/journal.pone.0250098, doi:10.1371/journal.pone.0250098. This article has 52 citations and is from a peer-reviewed journal.

8. (ho2021neonatalandinfant pages 13-15): Peter Ho, Maria A. Quigley, Dharamveer Tatwavedi, Carl Britto, and Jennifer J. Kurinczuk. Neonatal and infant mortality associated with spina bifida: a systematic review and meta-analysis. PLoS ONE, 16:e0250098, May 2021. URL: https://doi.org/10.1371/journal.pone.0250098, doi:10.1371/journal.pone.0250098. This article has 52 citations and is from a peer-reviewed journal.

9. (risova2024preconceptionalandpericonceptional pages 1-3): Vanda Rísová, Rami Saade, Vladimír Jakuš, Lívia Gajdošová, Ivan Varga, and Jozef Záhumenský. Preconceptional and periconceptional folic acid supplementation in the visegrad group countries for the prevention of neural tube defects. Nutrients, 17:126, Dec 2024. URL: https://doi.org/10.3390/nu17010126, doi:10.3390/nu17010126. This article has 17 citations.

10. (ferreira2024interventionstoimprove pages 1-3): Rafaela Fernandes Alvarenga Ferreira and Ana Cristina de Jesus Alves. Interventions to improve independence in basic and instrumental activities of daily living in individuals with myelomeningocele: an integrative literature review. Cadernos Brasileiros de Terapia Ocupacional, Jan 2024. URL: https://doi.org/10.1590/2526-8910.ctoar291837922, doi:10.1590/2526-8910.ctoar291837922. This article has 0 citations.

11. (NCT04652908 chunk 1):  Cellular Therapy for In Utero Repair of Myelomeningocele - The CuRe Trial. University of California, Davis. 2021. ClinicalTrials.gov Identifier: NCT04652908

12. (NCT04652908 chunk 2):  Cellular Therapy for In Utero Repair of Myelomeningocele - The CuRe Trial. University of California, Davis. 2021. ClinicalTrials.gov Identifier: NCT04652908

13. (NCT04027374 chunk 2):  Stress-associated Epigenetic Alterations in Newborns After Fetal Surgery. University Children's Hospital, Zurich. 2019. ClinicalTrials.gov Identifier: NCT04027374

14. (NCT04027374 chunk 1):  Stress-associated Epigenetic Alterations in Newborns After Fetal Surgery. University Children's Hospital, Zurich. 2019. ClinicalTrials.gov Identifier: NCT04027374

15. (OpenTargets Search: spina bifida,myelomeningocele): Open Targets Query (spina bifida,myelomeningocele, 15 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

16. (mathew2018antenataldiagnosismaternal pages 14-17): ME Mathew. Antenatal diagnosis, maternal and neonatal outcome analysis of myelomeningocele, spina bifida at the lithuanian university of health sciences hospital (2016-2017 …. Unknown journal, 2018.

17. (cranesmith2023anoncodinginsertional pages 1-2): Zoe Crane-Smith, Sandra C P De Castro, Evanthia Nikolopoulou, Paul Wolujewicz, Damian Smedley, Yunping Lei, Emma Mather, Chloe Santos, Mark Hopkinson, Andrew A Pitsillides, Richard H Finnell, M Elisabeth Ross, Andrew J Copp, and Nicholas D E Greene. A non-coding insertional mutation of grhl2 causes gene over-expression and multiple structural anomalies including cleft palate, spina bifida and encephalocele. Human Molecular Genetics, 32:2681-2692, Jun 2023. URL: https://doi.org/10.1093/hmg/ddad094, doi:10.1093/hmg/ddad094. This article has 12 citations and is from a domain leading peer-reviewed journal.

18. (kancherla2023earlyneonatalmortality pages 1-6): Vijaya Kancherla, Sanjida Mowla, Sari Räisänen, and Mika Gissler. Early neonatal mortality among babies born with spina bifida in finland (2000–2014). American Journal of Perinatology, 40:1208-1216, Aug 2023. URL: https://doi.org/10.1055/s-0041-1733957, doi:10.1055/s-0041-1733957. This article has 5 citations and is from a peer-reviewed journal.

19. (NCT07048691 chunk 1): Muhammad Naveed Babur. Prenatal and Postnatal Ultrasonographic Evaluation of Myelomeningocele to Predict Post-Surgical Outcomes. Superior University. 2025. ClinicalTrials.gov Identifier: NCT07048691

20. (NCT06796972 chunk 1):  In Utero Surgery for Fetal Myelomeningocele: Decision-making Mechanisms and Psychological Impact of Prenatal Therapy. Assistance Publique - Hôpitaux de Paris. 2024. ClinicalTrials.gov Identifier: NCT06796972

## Artifacts

- [Edison artifact artifact-00](Spina_Bifida_Cystica-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 3 |
| Off topic | 3 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `DOI:10.1542/peds.2019-1544` (8 mentions) - Prenatal Repair of Myelomeningocele and School-age Functional Outcomes
  - shared terms: repair, prenatal
- `DOI:10.1590/2526-8910.ctoAR291837922` (3 mentions) - Interventions to improve independence in basic and instrumental activities of daily living in individuals with myelomeningocele: an integrative literature review
  - shared terms: mmc
- `DOI:10.1590/2526-8910.ctoar291837922` (3 mentions) - Interventions to improve independence in basic and instrumental activities of daily living in individuals with myelomeningocele: an integrative literature review
  - shared terms: mmc

Weighed against this report's own most characteristic terms: `disease`, `gene`, `clinical`, `mmc`, `genetic`, `include`, `human`, `model`, `neural`, `spina`, `bifida`, `fetal`, `variant`, `primary`, `repair`, `risk`, `folate`, `open`, `secondary`, `prenatal`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.