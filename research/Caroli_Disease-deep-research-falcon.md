---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-20T02:49:51.570437'
end_time: '2026-08-20T02:57:18.185581'
duration_seconds: 446.62
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Caroli disease
  mondo_id: MONDO:0010913
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 16
reference_validation:
  total_references: 7
  verified: 4
  not_found: 3
  unverifiable: 0
  confabulation_rate: 0.429
  relevance_assessed: 4
  on_topic: 1
  unresolved_references:
  - DOI:10.14218/JCTH.2024.00119](https://doi.org/10.14218/jcth.2024.00119
  - DOI:10.1186/s13023-024-03187-w](https://doi.org/10.1186/s13023-024-03187-w
  - DOI:10.1016/j.bbadis.2017.06.027](https://doi.org/10.1016/j.bbadis.2017.06.027
  needs_review: true
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Caroli_Disease-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Caroli disease
- **MONDO ID:** MONDO:0010913 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Caroli disease** covering all of the
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
- **Disease Name:** Caroli disease
- **MONDO ID:** MONDO:0010913 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Caroli disease** covering all of the
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


# Caroli Disease: Comprehensive Disease-Characteristics Report

**Target:** Caroli disease (CD)  
**Category:** rare Mendelian cholangiopathy / developmental ciliopathy  
**Core distinction:** CD denotes non-obstructive segmental or diffuse ectasia of the large intrahepatic bile ducts **without congenital hepatic fibrosis**. **Caroli syndrome (CS)** denotes the same duct abnormality plus congenital hepatic fibrosis (CHF), often with portal hypertension and renal manifestations of the autosomal-recessive polycystic kidney disease spectrum. The distinction is clinically important and is sometimes blurred in publications and databases. (tidwell2024heritablechroniccholestatic pages 6-7, tidwell2024heritablechroniccholestatic pages 5-6)

The following table summarizes the principal structured findings; the narrative thereafter addresses all 15 requested domains.

| Domain | Caroli disease (CD) summary | Caroli syndrome (CS) distinction | Ontology suggestions | Evidence |
|---|---|---|---|---|
| Definition / identifiers | Rare congenital malformation characterized by non-obstructive, segmental or diffuse saccular dilatation of the **large intrahepatic bile ducts**; incidence estimated at **~1:1,000,000**. MONDO provided by user: **MONDO:0010913**. Disease-level knowledge here is derived from aggregated literature/review and registry-style summaries, not individual EHRs. | CS = CD features **plus congenital hepatic fibrosis (CHF)** involving interlobular ducts and portal fibrosis. | MONDO:0010913; UBERON: liver / intrahepatic bile duct; HPO: Dilatation of the intrahepatic bile duct | (tidwell2024heritablechroniccholestatic pages 6-7, tidwell2024heritablechroniccholestatic pages 5-6) |
| Inheritance / gene | Reported as **autosomal recessive** in the gathered evidence; associated mainly with **PKHD1** mutations encoding **fibrocystin/polyductin**; Open Targets also lists disease-target evidence for **PKHD1**, with weaker associations for **CYS1** and **DZIP1L**. | CS shares the same AR/PKHD1 association in review evidence and is more often discussed within the ARPKD/CHF spectrum. | HGNC: PKHD1; CL/GO-linked ciliopathy context | (tidwell2024heritablechroniccholestatic pages 5-6, OpenTargets Search: Caroli disease-PKHD1) |
| Hallmark anatomy | Primary lesion localizes to **large intrahepatic bile ducts** with ductal ectasia; imaging may show diffuse involvement (**50%**) or localization to right lobe (**28.6%**) or left lobe (**21.4%**). | CS additionally includes **portal tracts/congenital hepatic fibrosis** and signs of portal hypertension. | UBERON: intrahepatic bile duct, liver; CL: cholangiocyte | (tidwell2024heritablechroniccholestatic pages 5-6) |
| Core phenotypes with frequencies | Acute cholangitis **64%**; intrahepatic cholelithiasis/choledocholithiasis **33%**; right upper quadrant pain **50%**; jaundice **35.7%**; fever **28.6%**; asymptomatic **14.3%**. Lab abnormalities reported: elevated GGT **64.3%**, alkaline phosphatase **35.7%**, bilirubin **28.6%**. Mean diagnosis age **42 years** (range **15–68**); no gender predominance in the cited series. | CS cohorts more often show portal-hypertension phenotypes: abdominal pain, fever, thrombocytopenia, prolonged PT, ascites, varices, splenomegaly. | HPO: Cholangitis, Hepatolithiasis, Abdominal pain, Jaundice, Fever, Elevated gamma-glutamyltransferase, Elevated alkaline phosphatase, Hyperbilirubinemia, Hepatomegaly, Splenomegaly, Ascites, Esophageal varices | (tidwell2024heritablechroniccholestatic pages 6-7, tidwell2024heritablechroniccholestatic pages 5-6) |
| Mechanism / pathophysiology | CD is a **cholangiociliopathy**. PKHD1 loss causes defective fibrocystin, altered ciliary/plasma-membrane signaling, reduced interaction with PC2/calcium signaling, activation of **cAMP**, **β-catenin**, **NF-κB**, **JAK/STAT**, chemokine production, macrophage recruitment, **TGF-β** activation, myofibroblast stimulation, ECM deposition, and fibrogenic remodeling. Review evidence also notes aberrant **NOTCH1-4** expression in biliary epithelial cells in CD. | CS lies further along the fibrocystic/fibrotic spectrum, with CHF/portal fibrosis clinically manifest. | GO: cilium organization; calcium ion signaling; inflammatory response; chemokine production; macrophage chemotaxis; extracellular matrix organization; fibrosis. CL: cholangiocyte, macrophage, portal myofibroblast | (mariotti2018animalmodelsof pages 13-17, tidwell2024heritablechroniccholestatic pages 1-2, mahboobipour2024clinicalmanifestationepidemiology pages 5-7, tidwell2024heritablechroniccholestatic pages 5-6) |
| Diagnosis | Preferred modality: **MRCP**. Pathognomonic imaging sign: **central dot sign** on contrast CT/MRI. Additional modalities: ultrasound, hepatobiliary scintigraphy (beading of intrahepatic ducts). Histology: localized dilated non-obstructive ducts with patent vascular channels/intraluminal wall protrusions; fetal-type markers **CK7**, **MUC-1**, and **β-catenin** support congenital origin. | CS diagnosis additionally evaluates CHF/portal-hypertension features and associated renal disease. | HPO: Abnormality of the biliary tract morphology; UBERON: intrahepatic bile duct; NCIT-imaging terms not confidently assigned from gathered evidence | (tidwell2024heritablechroniccholestatic pages 6-7, NCT04007575 chunk 1) |
| Differential diagnosis | Key differentials in gathered evidence: **primary sclerosing cholangitis** and **recurrent pyogenic cholangitis**; NCT04007575 specifically aimed to distinguish CD from **obstructive benign or malignant bile duct dilatation** by MRCP criteria. | CS may also overlap clinically with other causes of congenital hepatic fibrosis/portal hypertension. | — | (tidwell2024heritablechroniccholestatic pages 6-7, NCT04007575 chunk 1) |
| Complications / cancer risk | Recurrent cholangitis, biliary stones, hepatic abscess, sepsis, poor quality of life from recurrent infections. Cholangiocarcinoma risk elevated: **6.3% CD**, **7.6% CS** in one multicenter dataset; systematic review of **561 CD patients** found **6.6%** cholangiocarcinoma incidence. | CS shares the cancer risk and adds portal-hypertension complications. | HPO: Cholangiocarcinoma, Hepatic abscess, Sepsis, Portal hypertension | (tidwell2024heritablechroniccholestatic pages 6-7) |
| Treatment | Medical/supportive: **antibiotics** for cholangitis; **ursodeoxycholic acid** for intrahepatic cholelithiasis; chronic suppressive antibiotics may be used while awaiting transplant. Procedural/surgical: **hepatectomy/resection** for localized disease; **liver transplantation** for diffuse disease; **simultaneous liver-kidney transplantation** may be required with renal involvement. Reported postoperative complications after hepatectomy include biliary leakage **26%**, surgical revision **16%**, pleural effusion **5.5%**, UTI **5.5%**. | CS often more likely to require transplant because of diffuse hepatobiliary and fibrotic/portal-hypertensive involvement. | NCIT: Antibiotic Therapy; Ursodeoxycholic Acid; Hepatectomy; Liver Transplantation; Kidney and Liver Transplantation | (tidwell2024heritablechroniccholestatic pages 6-7, tidwell2024heritablechroniccholestatic pages 5-6) |
| Prognosis / temporal course | Most patients are asymptomatic until **age 20**; **>80%** become symptomatic by **age 30**. Disease burden is chronic/episodic with recurrent cholangitis. Main mortality drivers reported in review evidence are **sepsis** and **hepatic abscesses**. Reported transplant outcomes are favorable: patient survival **99%**, **96.2%**, **94.6%** at 1, 3, 5 years; graft survival **94.9%**, **91.1%**, **89.6%**. | CS prognosis worsens with portal hypertension, fibrosis, renal disease, and infectious complications. | HPO: Recurrent fever, Recurrent cholangitis, Portal hypertension, Chronic kidney disease | (tidwell2024heritablechroniccholestatic pages 5-6, tidwell2024heritablechroniccholestatic pages 6-7) |
| Models / research applications | **PCK rat** (PKHD1 splicing mutation) shows progressive intrahepatic bile duct dilatation, cyst development, renal collecting-duct cysts, and mild portal fibrosis. **Pkhd1del4/del4 mouse** develops intrahepatic bile duct dysgenesis progressing to cyst-like lesions, peribiliary fibrogenesis after 3 months, and splenomegaly in **>50%** by 6 months. These models are used to study cholangiocyte cilia dysfunction, inflammatory-fibrotic signaling, and portal-fibrosis mechanisms. | Models largely represent the broader ARPKD/CHF/CD-CS spectrum rather than isolated adult CD alone. | CL: cholangiocyte, macrophage; GO: fibrogenesis, chemokine-mediated signaling, epithelial tube morphogenesis | (mariotti2018animalmodelsof pages 13-17) |


*Table: This table provides a compact knowledge-base style summary of Caroli disease, explicitly distinguishing it from Caroli syndrome and organizing the main supported facts across genetics, phenotype, mechanism, diagnosis, treatment, prognosis, and models. It is useful as a structured extraction layer from the gathered evidence.*

## Evidence scope and limitations

The strongest recent sources retrieved were two peer-reviewed 2024 reviews: Tidwell and Wu, published June 2024 ([DOI 10.14218/JCTH.2024.00119](https://doi.org/10.14218/jcth.2024.00119)), and Mahboobipour et al., published April 2024 ([DOI 10.1186/s13023-024-03187-w](https://doi.org/10.1186/s13023-024-03187-w)). Mechanistic model evidence was supplemented by Mariotti et al. ([DOI 10.1016/j.bbadis.2017.06.027](https://doi.org/10.1016/j.bbadis.2017.06.027), published April 2018). Most quantitative clinical estimates come from small retrospective cohorts or systematic reviews assembled from case series; they should not be interpreted as population-level precision estimates. No individual-patient EHR data were used.

## 1. Disease information

### Definition and nomenclature

Caroli disease is a congenital malformation of the large intrahepatic bile ducts characterized by non-obstructive, communicating, saccular or fusiform duct dilatation. It predisposes to bile stasis, hepatolithiasis, recurrent bacterial cholangitis, hepatic abscess, sepsis, and cholangiocarcinoma. Pure CD lacks the portal fibrosis and portal hypertension that define CS. (tidwell2024heritablechroniccholestatic pages 6-7, tidwell2024heritablechroniccholestatic pages 5-6)

**Common names:** Caroli disease; Caroli’s disease; communicating cavernous ectasia of the intrahepatic ducts; simple-type Caroli disease. “Caroli syndrome” is related but not synonymous.

**Identifiers:**

- **MONDO:** MONDO:0010913, as supplied and corroborated by the retrieved Open Targets disease record.
- **Orphanet:** commonly indexed within the Caroli disease/Caroli syndrome spectrum; an exact ORPHA number was not independently verified in the retrieved full text.
- **OMIM:** the molecularly overlapping PKHD1/ARPKD–CHF spectrum is generally represented through PKHD1-associated polycystic kidney disease; an isolated-CD OMIM number was not verified here.
- **MeSH:** Caroli Disease.
- **ICD:** no uniquely validated ICD-10-CM code was established from retrieved evidence; implementations often place it under congenital malformations of bile ducts. ICD coding should therefore be validated against the target jurisdiction and release rather than inferred.

The knowledge represented here is aggregated disease-level evidence from reviews, cohorts, genetic databases, and model studies—not observations extracted from a particular patient record.

## 2. Etiology, risk, and protective factors

### Causal factors

The established causal framework is developmental and genetic. Pathogenic dysfunction in **PKHD1**, encoding fibrocystin/polyductin, disrupts cholangiocyte primary-cilium and epithelial-tubule biology. The resulting ductal-plate/tubular-architecture abnormality produces large-duct ectasia. Open Targets gives PKHD1–CD an association score of 0.514, supported by genetic literature, clinical variation resources, and animal models; weaker database associations with **CYS1** and **DZIP1L** should not be treated as equivalent, clinically established causes of isolated human CD. (OpenTargets Search: Caroli disease-PKHD1)

A whole-exome study in a Chinese twin family identified recessive compound-heterozygous PKHD1 variants (PMID **24710345**). The same report emphasized that PKHD1 variant detection has historically been lower in patients labeled specifically as CD than in severe ARPKD/CHF, consistent with genetic heterogeneity, incomplete testing, or phenotype-classification problems. (OpenTargets Search: Caroli disease-PKHD1)

### Risk factors

- **Genetic:** biallelic pathogenic PKHD1 variants, an affected sibling, parental carrier status, and consanguinity increase risk under an autosomal-recessive model.
- **Clinical modifiers:** duct distribution and bile stasis determine vulnerability to stones and infection. Chronic inflammation is a downstream risk factor for cholangiocarcinoma rather than a primary cause.
- **Environmental/lifestyle:** no reproducible toxin, dietary, occupational, smoking, alcohol, sex, or pollution exposure has been shown to cause the congenital malformation. Infection is a complication facilitated by stasis, not the initiating etiology.

### Protective factors and gene–environment interaction

No validated protective allele, diet, lifestyle exposure, or pharmacologic primary-prevention factor was identified. A practical gene–environment interaction is that genetically abnormal duct anatomy creates bile stasis, after which bacterial exposure and obstruction precipitate cholangitis and inflammatory injury. This is mechanistically plausible and clinically observed, but formal G×E effect estimates are unavailable.

## 3. Phenotypes

The course is highly variable and may remain clinically silent for years. In one 14-patient series summarized in the 2024 review, acute cholangitis occurred in **64%**, intrahepatic stones/choledocholithiasis in **33%**, right-upper-quadrant pain in **50%**, jaundice in **35.7%**, fever in **28.6%**, and asymptomatic disease in **14.3%**. Reported laboratory abnormalities included elevated GGT in **64.3%**, alkaline phosphatase in **35.7%**, and bilirubin in **28.6%**. These percentages are series-specific, not universal frequencies. (tidwell2024heritablechroniccholestatic pages 6-7, tidwell2024heritablechroniccholestatic pages 5-6)

| Phenotype | Type and characteristics | Suggested HPO annotation |
|---|---|---|
| Intrahepatic bile-duct ectasia | Congenital structural sign; localized or diffuse; lifelong | Abnormality/dilatation of intrahepatic bile duct |
| Recurrent cholangitis | Episodic, potentially severe; often adult-recognized | Cholangitis; recurrent fever |
| Hepatolithiasis | Structural/clinical complication from bile stasis; recurrent | Intrahepatic cholelithiasis |
| RUQ abdominal pain | Episodic symptom, often accompanying infection/obstruction | Abdominal pain |
| Fever | Episodic symptom during cholangitis | Fever |
| Jaundice/cholestasis | Fluctuating symptom/laboratory phenotype | Jaundice; hyperbilirubinemia; cholestasis |
| Elevated GGT/ALP | Laboratory abnormality, especially during cholestasis | Elevated gamma-glutamyltransferase; elevated alkaline phosphatase |
| Hepatomegaly | Physical sign, variable | Hepatomegaly |
| Hepatic abscess/sepsis | Severe infectious complications | Hepatic abscess; sepsis |
| Portal hypertension, splenomegaly, ascites, varices | Primarily CS/CHF rather than pure CD | Portal hypertension; splenomegaly; ascites; esophageal varices |
| Renal cystic disease | Primarily PKHD1-associated CS/ARPKD spectrum | Renal cyst; polycystic kidney dysplasia |
| Cholangiocarcinoma | Late malignant complication | Cholangiocarcinoma |

In a 16-patient CS cohort, abdominal pain occurred in eight, fever in six, variceal bleeding in one, and fatigue in one; ten had thrombocytopenia and five prolonged prothrombin time. These findings should not be transferred uncritically to simple CD. (tidwell2024heritablechroniccholestatic pages 6-7)

**Quality of life:** no validated CD-specific EQ-5D, SF-36, or PROMIS dataset was retrieved. Nevertheless, recurrent painful cholangitis, hospitalization, antibiotic exposure, procedures, and fear of sepsis or cancer impose substantial burden; the 2024 review explicitly associates recurrent cholangitis with early quality-of-life loss. (tidwell2024heritablechroniccholestatic pages 6-7)

## 4. Genetic and molecular information

### Causal gene and protein

- **PKHD1**: human gene ENSG00000170927; encodes fibrocystin/polyductin, a large ciliary/plasma-membrane protein involved in epithelial tubulogenesis and duct-lumen architecture.
- **Origin:** disease-causing variants are constitutional/germline, generally biallelic under an autosomal-recessive model—not somatic drivers.
- **Functional direction:** loss or severe reduction of fibrocystin function.
- **Protein interaction:** fibrocystin’s C-terminal region interacts with the N-terminal region of polycystin-2 (PC2); fibrocystin loss reduces PC2 expression and perturbs calcium signaling. (mariotti2018animalmodelsof pages 13-17, mahboobipour2024clinicalmanifestationepidemiology pages 5-7)

### Variant classes and interpretation

PKHD1 disease alleles across the ARPKD/CHF/CD spectrum include missense, nonsense, frameshift, and splice-altering variants. However, no comprehensive CD-specific ClinVar extraction, ACMG classification table, HGVS list, or gnomAD frequency analysis was available in the retrieved evidence. Knowledge-base curation should therefore import variant-level assertions directly from current ClinVar records and retain submitter/date/review-status fields. Pathogenic recessive alleles are expected to be individually rare; a VUS should not be considered diagnostic without segregation, phenotype, population, and functional evidence.

No established recurrent chromosomal abnormality, repeat expansion, mitochondrial variant, somatic mutation mechanism, genetic anticipation, or germline mosaicism pattern was identified. No validated modifier gene or protective allele is known. DZIP1L is biologically relevant to ciliary transition-zone trafficking of PC1/PC2, but its weaker disease association should be labeled emerging/indirect rather than a routine isolated-CD gene. (OpenTargets Search: Caroli disease-PKHD1, mahboobipour2024clinicalmanifestationepidemiology pages 5-7)

### Epigenetics

No disease-specific, replicated DNA-methylation, histone-mark, or chromatin-remodeling signature suitable for clinical annotation was retrieved. Epigenomic testing is not standard diagnosis.

## 5. Environmental information

There is no evidence that toxins, radiation, pollution, occupational exposure, smoking, alcohol, diet, or inactivity cause CD. Ascending bacteria are clinically important in cholangitis, but no single pathogen defines the disease. Common biliary organisms may act opportunistically after stasis or instrumentation. Environmental and lifestyle information should therefore be annotated as **not established**, rather than “absent by proof.”

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream germline defect:** biallelic PKHD1 dysfunction reduces or alters fibrocystin.
2. **Ciliary/tubular defect:** abnormal fibrocystin at the cholangiocyte primary cilium/plasma membrane disrupts PC2-associated calcium sensing, planar-cell-polarity/tubulogenesis, and maintenance of duct-lumen architecture.
3. **Developmental lesion:** malformed large intrahepatic ducts become segmentally or diffusely ectatic and remain connected to the biliary tree.
4. **Biophysical consequence:** ectatic ducts cause sluggish flow and bile stasis, promoting pigment stones, sludge, obstruction, and bacterial colonization.
5. **Clinical consequence:** recurrent cholangitis produces pain, fever, jaundice, abscess, and sepsis.
6. **Inflammatory/fibrotic amplification:** cAMP/β-catenin and NF-κB signaling increases IL-1β, CXCL1, CXCL10, and CXCL12; JAK/STAT and NLRP3/caspase-1 signaling amplify inflammation. Recruited macrophages provide TNF-α and TGF-β; cholangiocyte αvβ6 integrin activates latent TGF-β1, recruiting portal myofibroblasts and extracellular-matrix deposition. This axis is especially important in CS/CHF. (mariotti2018animalmodelsof pages 13-17, tidwell2024heritablechroniccholestatic pages 1-2)
7. **Long-term malignant risk:** prolonged stasis, epithelial turnover, and inflammation create a field favoring cholangiocarcinoma. (tidwell2024heritablechroniccholestatic pages 6-7)

Human biliary epithelium in CD has shown strong NOTCH1–4 expression relative to weak/negative expression in CHF, but whether this is initiating, compensatory, or downstream remains unresolved. (tidwell2024heritablechroniccholestatic pages 5-6)

### Cells, processes, and ontology suggestions

- **Primary cell:** cholangiocyte / biliary epithelial cell — **CL:0000068** may be used after ontology-version validation.
- **Secondary cells:** macrophages, portal fibroblasts/myofibroblasts, hepatic stellate cells, and vascular cells within portal tracts.
- **GO biological processes:** cilium organization; epithelial tube morphogenesis; calcium-ion transmembrane transport/signaling; canonical Wnt/β-catenin signaling; NF-κB signaling; chemokine production; macrophage chemotaxis; TGF-β receptor signaling; extracellular-matrix organization; inflammatory response.
- **GO cellular components:** primary cilium, ciliary membrane, plasma membrane, basal-body/centrosomal region.

### Molecular profiling and advanced technologies

No validated CD-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or multi-omic clinical signature was retrieved. Contemporary ciliopathy organoids can model patient-specific genotype–phenotype relationships and permit drug screening, but this remains a research application rather than a validated CD diagnostic or therapy.

## 7. Anatomical structures affected

- **Primary organ/system:** liver and biliary system; large intrahepatic bile ducts.
- **Distribution:** diffuse in **50%**, right-lobe localized in **28.6%**, and left-lobe localized in **21.4%** in one small cohort. CD is not intrinsically lateralized; it can be segmental, lobar, or bilobar. (tidwell2024heritablechroniccholestatic pages 5-6)
- **Tissue:** biliary epithelium and peribiliary/portal connective tissue.
- **Cell:** cholangiocyte; macrophages and portal myofibroblasts become involved downstream.
- **Subcellular:** primary cilium/ciliary membrane and plasma-membrane fibrocystin–PC2 complex.
- **Secondary structures:** portal venous system and spleen in CS; kidneys and occasionally pancreatic cysts in the broader PKHD1 spectrum. (tidwell2024heritablechroniccholestatic pages 6-7)

Suggested anatomical annotations are **UBERON liver**, **intrahepatic bile duct**, **biliary tree**, **portal tract**, **kidney collecting duct**, and **spleen**; exact numeric UBERON identifiers should be ontology-release validated before ingestion.

## 8. Temporal development

The anatomical defect is congenital, but recognition is often delayed. Most patients reportedly remain asymptomatic until approximately age 20, while more than **80% become symptomatic before age 30**. A small adult CD series had a mean diagnostic age of **42 years** (range 15–68), illustrating ascertainment variability. (tidwell2024heritablechroniccholestatic pages 6-7, tidwell2024heritablechroniccholestatic pages 5-6)

The course is lifelong and commonly episodic: asymptomatic structural disease may progress to recurrent cholangitis and stones, followed by abscess/sepsis, repeated interventions, or malignancy. Pure CD need not progress to cirrhosis; portal-hypertension progression suggests CS/CHF or secondary advanced injury. Spontaneous anatomical remission is not expected. A critical intervention window occurs when disease remains localized enough for curative-intent resection, before diffuse infection or malignant transformation.

## 9. Inheritance and population

- **Incidence/prevalence:** approximately **1 per 1,000,000** is frequently cited, but the retrieved review labels this as incidence and does not establish a rigorous population denominator or annual incidence. Robust registry-based prevalence is lacking. (tidwell2024heritablechroniccholestatic pages 6-7)
- **Inheritance:** autosomal recessive in the PKHD1-associated spectrum. (tidwell2024heritablechroniccholestatic pages 5-6)
- **Penetrance/expressivity:** exact penetrance is unknown; expressivity is clearly variable, spanning isolated duct ectasia, CS/CHF, and renal-predominant ARPKD.
- **Sex:** no sex predominance in the cited 14-patient series. (tidwell2024heritablechroniccholestatic pages 5-6)
- **Ethnicity/geography:** worldwide case reports exist, but no validated high-risk ancestry or geographic endemicity was identified.
- **Founder effects/carrier frequency:** no CD-specific founder allele or carrier-frequency estimate was retrieved.
- **Anticipation:** not expected for a recessive loss-of-function ciliopathy and not reported.
- **Consanguinity:** increases the probability of biallelic recessive disease, but a CD-specific attributable fraction is unknown.

For confirmed biallelic disease, recurrence risk is conventionally 25% for each pregnancy when both parents are heterozygous carriers, subject to confirmation of phase and parentage.

## 10. Diagnostics

### Imaging and clinical evaluation

**MRCP is the preferred non-invasive diagnostic modality.** It maps the morphology and communication of intrahepatic duct ectasia while avoiding diagnostic ERCP risks. Contrast CT or MRI may reveal the **central dot sign**: a portal-vein branch or hepatic-artery branch surrounded by an ectatic duct. Ultrasound can identify duct dilatation and stones; hepatobiliary scintigraphy may show beading. The central dot sign is highly characteristic but its absence does not exclude disease. (tidwell2024heritablechroniccholestatic pages 6-7)

NCT04007575 (IMACA), completed in 2020, retrospectively studied **61 patients** to develop MRCP criteria based on duct shape and distribution, the dot sign, calculi, liver abnormalities, and portal-hypertension signs, with the aim of distinguishing CD from benign or malignant obstructive dilatation. This was an observational diagnostic study, not a therapeutic trial. [ClinicalTrials.gov: NCT04007575](https://clinicaltrials.gov/study/NCT04007575). (NCT04007575 chunk 1)

### Laboratory and pathology

During cholangitis, expected findings include neutrophilic leukocytosis, direct hyperbilirubinemia, and elevated alkaline phosphatase/GGT; blood cultures should be obtained before antibiotics when feasible. Renal function, blood counts, coagulation, and portal-hypertension indices help distinguish broader CS/ARPKD involvement. Histology can show dilated non-obstructed ducts with intraluminal wall protrusions and patent portal vascular channels. CK7, MUC1, and β-catenin expression supports fetal/congenital duct phenotype, although biopsy is not routinely necessary when imaging is diagnostic. (tidwell2024heritablechroniccholestatic pages 6-7)

### Genetic testing

A practical algorithm is:

1. Confirm compatible communicating intrahepatic duct ectasia by MRCP.
2. Assess kidneys, portal hypertension, fibrosis, and family history.
3. Use a **cystic-kidney/cholangiopathy multigene panel** including PKHD1 when phenotype is atypical or syndromic.
4. If suspicion remains high, perform deletion/duplication analysis and WES/WGS with phenotype-driven reanalysis.
5. Confirm candidate recessive variants by segregation and ACMG/AMP classification.

PKHD1 next-generation sequencing is available. CMA, karyotyping, FISH, mitochondrial sequencing, and repeat-expansion testing are not first-line unless an independent indication exists. (tidwell2024heritablechroniccholestatic pages 6-7)

### Differential diagnosis

Principal alternatives include primary sclerosing cholangitis, recurrent pyogenic cholangitis, obstructive stones or strictures, cholangiocarcinoma, choledochal cyst/type V duct disease terminology, polycystic liver disease, primary biliary disorders, and secondary sclerosing cholangitis. PSC tends to show multifocal stricturing and beading rather than congenital saccular ectasia with central vascular dots; recurrent pyogenic cholangitis is usually accompanied by obstructing pigment stones and acquired strictures. (tidwell2024heritablechroniccholestatic pages 6-7, NCT04007575 chunk 1)

There is no population or newborn screening program. Cascade testing is appropriate after a molecular diagnosis.

## 11. Outcome and prognosis

Major morbidity arises from recurrent cholangitis, hepatolithiasis, abscesses, sepsis, hospitalization, and repeated biliary procedures. In CS, portal hypertension, variceal bleeding, hypersplenism, and kidney failure add substantial morbidity. Sepsis and hepatic abscess are reported major causes of death. (tidwell2024heritablechroniccholestatic pages 6-7)

### Cancer risk

A multicenter dataset found cholangiocarcinoma in **6.3% of CD** and **7.6% of CS** patients. A systematic review of **561 CD patients** reported a **6.6%** incidence; among affected cancer cases, one-year survival was **36%** and recurrence **75%**. Heterogeneous referral and surgical ascertainment likely inflate or destabilize these estimates, but the direction of risk is clear. (tidwell2024heritablechroniccholestatic pages 6-7)

### Treatment-associated prognosis

After transplantation, reported patient survival was **99%, 96.2%, and 94.6%** at one, three, and five years; corresponding graft survival was **94.9%, 91.1%, and 89.6%**. These excellent selected-cohort outcomes should not be interpreted as untreated natural-history survival. (tidwell2024heritablechroniccholestatic pages 5-6)

No validated CD-specific prognostic biomarker or risk calculator exists. Clinically adverse indicators include diffuse/bilobar disease, recurrent uncontrolled infection, abscess, portal hypertension, renal failure, and suspected malignancy.

## 12. Treatment and current implementation

No approved drug corrects the congenital duct lesion or PKHD1 defect. Management is anatomy- and complication-directed.

### Medical and interventional care

- **Acute cholangitis:** prompt broad-spectrum antibiotics, cultures, supportive care, and biliary decompression when obstruction or failure of medical therapy is present. Suggested NCIt concept: antibiotic therapy.
- **Hepatolithiasis:** ursodeoxycholic acid may be used for intrahepatic stones, although robust CD-specific response trials are lacking. Suggested chemical annotation: ursodeoxycholic acid; NCIt intervention: pharmacologic treatment.
- **Bridging:** chronic suppressive antibiotics may be used in selected patients with recurrent infection awaiting transplantation. (tidwell2024heritablechroniccholestatic pages 6-7, tidwell2024heritablechroniccholestatic pages 5-6)
- **Endoscopic/percutaneous drainage:** useful for accessible stones, strictures, abscesses, or acute decompression; repeated instrumentation can itself introduce infection.

### Surgery

- **Localized unilobar/segmental CD:** anatomical hepatectomy can remove the diseased reservoir and may be definitive.
- **Diffuse/bilobar disease, recurrent life-threatening cholangitis, portal-hypertensive CS, or unresectable disease:** liver transplantation.
- **Clinically important renal failure/ARPKD:** simultaneous liver–kidney transplantation may be appropriate. (tidwell2024heritablechroniccholestatic pages 5-6)

Reported surgical complications include bile leak **26%**, revision **16%**, pleural effusion **5.5%**, and urinary infection **5.5%**. A reviewed surgical cohort of 21 patients had no deaths over five years, but the sample was small and selected. (tidwell2024heritablechroniccholestatic pages 6-7)

Suggested NCIt intervention concepts: hepatectomy, partial hepatectomy, liver transplantation, combined liver–kidney transplantation, endoscopic biliary drainage, percutaneous drainage, antibiotic therapy, and ursodeoxycholic acid treatment.

### Advanced and experimental treatment

No established gene therapy, CRISPR therapy, ASO/siRNA therapy, cell therapy, or targeted anti-ciliary drug is approved for CD. cAMP, β-catenin, inflammatory, and TGF-β pathways are preclinical targets, but systemic inhibition may be toxic and evidence has not reached disease-specific clinical efficacy. The trial search identified observational natural-history/imaging studies rather than active interventional CD drug trials. NCT01401998 is an observational ARPKD database study, relevant to the broader PKHD1 spectrum but not a CD treatment trial.

No CD-specific pharmacogenomic guideline from CPIC/PharmGKB was identified.

## 13. Prevention

**Primary prevention:** the congenital genetic lesion cannot currently be prevented by lifestyle modification or vaccination. Genetic counseling, carrier testing after familial variants are known, prenatal diagnosis, and preimplantation genetic testing are reproductive-risk options—not treatments of an affected person.

**Secondary prevention:** no population screening is recommended. Family cascade testing and imaging/genetic evaluation of at-risk siblings can enable earlier detection. Periodic clinical, biochemical, and imaging review is reasonable, although an evidence-based surveillance interval was not established.

**Tertiary prevention:** rapid treatment of cholangitis, removal or drainage of obstructing stones, avoidance of unnecessary biliary instrumentation, management of portal hypertension and renal disease, and timely referral for resection/transplantation can reduce complications. Given the increased cholangiocarcinoma risk, expert hepatobiliary follow-up is appropriate, but no screening method or interval has proven mortality benefit. Vaccination according to chronic-liver-disease/transplant schedules may reduce unrelated infectious morbidity; it does not prevent CD.

## 14. Other species and natural disease

No well-established, common naturally occurring veterinary counterpart with validated breed-specific inheritance was retrieved. Caroli-like hepatobiliary lesions can occur in animal disease descriptions, but the principal comparative evidence comes from engineered or spontaneous laboratory models rather than a recognized zoonosis.

There is **no zoonotic potential** and no cross-species transmission: CD is an inherited developmental disorder. PKHD1/fibrocystin function is evolutionarily conserved across vertebrates, enabling rodent modeling.

## 15. Model organisms

### PCK rat

The **PCK rat** carries an orthologous Pkhd1 splicing defect and develops progressive intrahepatic bile-duct dilatation and hepatic cystic lesions, together with renal outer-medullary collecting-duct cysts. With age, some cystic structures disconnect from the biliary system. The model develops mild portal fibrosis but generally lacks the full fibrous septa and portal hypertension of severe human CS. It is useful for studying cholangiocyte cilia, cyst growth, bile-duct remodeling, and candidate antifibrotic/cyst-directed treatments. (mariotti2018animalmodelsof pages 13-17)

### Pkhd1del4/del4 mouse

This mouse develops intrahepatic duct dysgenesis followed by cyst-like configuration and peribiliary fibrosis after approximately three months; more than **50%** show splenomegaly by six months, consistent with clinically relevant portal hypertension. It is especially useful for dissecting macrophage–cholangiocyte–myofibroblast signaling. (mariotti2018animalmodelsof pages 13-17)

### Mechanistic findings and limitations

Fibrocystin-deficient cholangiocytes produce CXCL1, CXCL10, and CXCL12 through overactive β-catenin signaling. Macrophage-derived TNF-α/TGF-β promotes αvβ6-integrin-mediated local activation of TGF-β1 and portal fibrosis; macrophage depletion with clodronate reduces fibrosis in model systems. Pkhd1 knockout also increases cholangiocyte CTGF production. (mariotti2018animalmodelsof pages 13-17, mahboobipour2024clinicalmanifestationepidemiology pages 5-7)

These models recapitulate major features of the **ARPKD–CHF–CS spectrum** better than they reproduce isolated adult simple CD. Species differences, variable renal involvement, and incomplete human phenotypic heterogeneity limit direct translation. Liver/cholangiocyte organoids and patient-derived iPSC systems offer a complementary human platform, but no validated organoid-guided treatment is currently implemented clinically.

## Overall assessment

Caroli disease is best understood as a rare developmental cholangiociliopathy centered on abnormal large intrahepatic ducts. PKHD1/fibrocystin dysfunction is the strongest established genetic mechanism, but variant detection and genotype–phenotype mapping are less complete for isolated CD than for classic ARPKD/CHF. The major real-world priorities are accurate MRCP-based diagnosis, strict separation of CD from CS, rapid management of cholangitis and stones, anatomical resection for localized disease, transplantation for diffuse or life-threatening disease, and long-term expert monitoring for infection and cholangiocarcinoma. Recent 2024 literature primarily refines genetic-cholestasis classification and ciliary mechanisms; it has not yet delivered a disease-modifying molecular therapy. (tidwell2024heritablechroniccholestatic pages 6-7, OpenTargets Search: Caroli disease-PKHD1, tidwell2024heritablechroniccholestatic pages 1-2, tidwell2024heritablechroniccholestatic pages 5-6)

References

1. (tidwell2024heritablechroniccholestatic pages 6-7): Jasmine Tidwell and George Y. Wu. Heritable chronic cholestatic liver diseases: a review. Journal of Clinical and Translational Hepatology, 12:726-738, Jun 2024. URL: https://doi.org/10.14218/jcth.2024.00119, doi:10.14218/jcth.2024.00119. This article has 14 citations.

2. (tidwell2024heritablechroniccholestatic pages 5-6): Jasmine Tidwell and George Y. Wu. Heritable chronic cholestatic liver diseases: a review. Journal of Clinical and Translational Hepatology, 12:726-738, Jun 2024. URL: https://doi.org/10.14218/jcth.2024.00119, doi:10.14218/jcth.2024.00119. This article has 14 citations.

3. (OpenTargets Search: Caroli disease-PKHD1): Open Targets Query (Caroli disease-PKHD1, 4 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

4. (mariotti2018animalmodelsof pages 13-17): Valeria Mariotti, Mario Strazzabosco, Luca Fabris, and Diego F. Calvisi. Animal models of biliary injury and altered bile acid metabolism. Biochimica et Biophysica Acta (BBA) - Molecular Basis of Disease, 1864:1254-1261, Apr 2018. URL: https://doi.org/10.1016/j.bbadis.2017.06.027, doi:10.1016/j.bbadis.2017.06.027. This article has 237 citations and is from a peer-reviewed journal.

5. (tidwell2024heritablechroniccholestatic pages 1-2): Jasmine Tidwell and George Y. Wu. Heritable chronic cholestatic liver diseases: a review. Journal of Clinical and Translational Hepatology, 12:726-738, Jun 2024. URL: https://doi.org/10.14218/jcth.2024.00119, doi:10.14218/jcth.2024.00119. This article has 14 citations.

6. (mahboobipour2024clinicalmanifestationepidemiology pages 5-7): Amir Ali Mahboobipour, Moein Ala, Javad Safdari Lord, and Arash Yaghoobi. Clinical manifestation, epidemiology, genetic basis, potential molecular targets, and current treatment of polycystic liver disease. Orphanet Journal of Rare Diseases, Apr 2024. URL: https://doi.org/10.1186/s13023-024-03187-w, doi:10.1186/s13023-024-03187-w. This article has 23 citations and is from a peer-reviewed journal.

7. (NCT04007575 chunk 1):  Study of New Imaging Criteria for the Diagnosis of Caroli's Disease. Assistance Publique - Hôpitaux de Paris. 2020. ClinicalTrials.gov Identifier: NCT04007575

## Artifacts

- [Edison artifact artifact-00](Caroli_Disease-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 3 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 1 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.14218/JCTH.2024.00119](https://doi.org/10.14218/jcth.2024.00119` (1 mention) - Identifier did not resolve to a record
- `DOI:10.1186/s13023-024-03187-w](https://doi.org/10.1186/s13023-024-03187-w` (1 mention) - Identifier did not resolve to a record
- `DOI:10.1016/j.bbadis.2017.06.027](https://doi.org/10.1016/j.bbadis.2017.06.027` (1 mention) - Identifier did not resolve to a record