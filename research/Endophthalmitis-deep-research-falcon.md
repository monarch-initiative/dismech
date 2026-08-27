---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-26T16:34:44.108060'
end_time: '2026-08-26T16:44:08.705735'
duration_seconds: 564.6
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Endophthalmitis
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 34
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 2
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Endophthalmitis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Endophthalmitis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Endophthalmitis** covering all of the
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
- **Disease Name:** Endophthalmitis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Endophthalmitis** covering all of the
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


# Endophthalmitis: comprehensive disease-characteristics report

## Executive summary

Endophthalmitis is a sight-threatening inflammatory syndrome caused most often by microbial infection of the aqueous, vitreous, retina, or adjacent intraocular tissues. **Exogenous endophthalmitis** follows surgery, intravitreal injection, penetrating trauma, keratitis, or filtering-bleb infection; **endogenous endophthalmitis** results from hematogenous seeding during bacteremia or fungemia. It is an ophthalmic emergency because pathogen proliferation, toxins, and an intense host inflammatory response can destroy retinal architecture within hours to days.

Modern series remain dominated by exogenous disease and Gram-positive organisms, especially coagulase-negative staphylococci. In an Australian 18-year cohort, 87.1% of cases were exogenous, post-cataract and post-injection cases each represented approximately 38%, organisms were recovered in 56%, and 52.5% of treated eyes improved visually. A German 2019–2023 series identified a pathogen in 58.7%; *Staphylococcus epidermidis* represented 58.1% of identified organisms. These figures are center- and procedure-dependent rather than population prevalence estimates. (englisch2026microbiologicaletiologyof pages 1-2, maher2026epidemiologymicrobiologymanagement pages 1-2, maher2026epidemiologymicrobiologymanagement pages 2-5)

The disease is not a Mendelian disorder: no causal germline gene, inheritance pattern, disease-defining variant, or routine genetic test is established. Recent mechanistic research instead concerns host-response genes and pathways—AMPKα1, NLRP3, cytokine signaling, macrophage polarization, and fungal-response transcriptomes—which may eventually support host-directed adjuncts but are not current clinical genetic biomarkers. (singh2024myeloidcellspecificdeletion pages 1-6, khapuinamai2024unveilingtheinnate pages 1-2)

## 1. Disease information

### Definition and classification

Infectious endophthalmitis is microbial invasion of intraocular fluids or tissues producing severe inflammation. Panophthalmitis denotes extension through all ocular coats and often periocular tissue. Classification is clinically useful along four axes:

1. **Route:** exogenous versus endogenous.
2. **Setting:** postoperative, post-intravitreal injection, post-traumatic/foreign body, keratitis-associated, bleb-associated, or hematogenous.
3. **Timing:** acute—usually days—or delayed/chronic, often weeks to months.
4. **Organism:** bacterial, fungal, or rarely parasitic.

Endogenous endophthalmitis accounts for approximately 2–8% in reviews, although referral cohorts vary; recent series reported 7.9–12.9%. It is defined by bloodstream dissemination without preceding direct ocular inoculation. (alshehri2024endogenousendophthalmitisassociated pages 1-2, englisch2026microbiologicaletiologyof pages 1-2, maher2026epidemiologymicrobiologymanagement pages 1-2)

### Identifiers and synonyms

- **Preferred name:** Endophthalmitis.
- **Synonyms:** infectious endophthalmitis, purulent endophthalmitis, intraocular infection; subtype terms include postoperative, post-injection, post-traumatic, endogenous, metastatic, bacterial, and fungal endophthalmitis.
- **ICD-10-CM:** H44.0, purulent endophthalmitis; H44.1, other endophthalmitis. More specific child codes are jurisdiction/version dependent.
- **MeSH:** Endophthalmitis.
- **MONDO:** a MONDO concept exists for endophthalmitis, but the exact identifier should be verified against the current MONDO release before database ingestion rather than inferred here.
- **OMIM/Orphanet:** not generally applicable as a primary inherited or rare Mendelian disease entity.
- **ICD-11:** use the current browser’s endophthalmitis concept under disorders of the eye; release-specific code verification is required.

The evidence summarized here is predominantly **aggregated disease-level information** from cohorts, reviews, clinical studies, and model systems. Individual case reports are used only to illustrate rare organisms or presentations; it is not an EHR-derived patient profile.

## 2. Etiology, risk, and protective factors

### Causal factors and infectious agents

**Exogenous inoculation:** Cataract surgery and intravitreal injection are now major causes in high-income settings. Other routes include pars plana vitrectomy, glaucoma surgery, penetrating trauma, retained intraocular foreign body, corneal ulcer, and infected filtering bleb. In a German series of 126 cases, antecedents were injection in 55.6%, cataract surgery in 23.8%, vitrectomy in 5.6%, and glaucoma surgery in 4.8%. (englisch2026microbiologicaletiologyof pages 1-2)

**Endogenous seeding:** Bloodstream organisms cross the blood–ocular barriers during bacteremia or fungemia. Common systemic sources include endocarditis, liver abscess, urinary infection, indwelling vascular access, gastrointestinal or hepatobiliary infection, and injection-drug use. COVID-era reports suggested increased fungal endogenous disease in critically ill, immunosuppressed patients, particularly involving *Candida* and *Aspergillus*. (alshehri2024endogenousendophthalmitisassociated pages 1-2, shah2025riskfactorsfor pages 1-2)

**Organisms:** Exogenous disease is usually Gram-positive: coagulase-negative staphylococci, *S. aureus*, streptococci, *Enterococcus*, and delayed *Cutibacterium acnes*. Virulent Gram-negative organisms include *Pseudomonas aeruginosa*, *Klebsiella pneumoniae*, and *Escherichia coli*. Trauma—especially soil-contaminated injury—is associated with *Bacillus cereus*. Endogenous fungi are commonly *Candida* or *Aspergillus*; rare molds can produce relapsing infection. In the German series, all Gram-positive isolates were vancomycin susceptible, but this should not substitute for local surveillance. (englisch2026microbiologicaletiologyof pages 1-2, saeed2024auniquecase pages 1-3, braga2024endogenousendophthalmitisdue pages 1-2)

### Risk factors

- **Procedural:** wound leak or poor wound construction, posterior-capsule rupture/vitreous loss, prolonged or complicated surgery, contaminated instruments/medications, inadequate antisepsis, repeated intravitreal injections, and filtering blebs.
- **Traumatic:** delayed wound closure, dirty rural injury, lens disruption, and retained IOFB. In 218 cases, IOFB independently predicted poor postoperative vision in traumatic disease (OR 2.215; p=0.016). A 2024 metallic-injury cohort found IOFB associated with faster onset, greater WBC/neutrophil/CRP responses, and poorer control (R=0.39; p<0.05). (li2025clinicalretrospectiveanalysis pages 1-2, wu2024systematicinflammatoryindicators pages 1-2)
- **Endogenous:** diabetes, malignancy, neutropenia, HIV/AIDS, transplantation, systemic corticosteroids or other immunosuppression, recent major surgery, indwelling catheter, parenteral nutrition, intravenous drug use, and endocarditis. Among 769,472 inpatients with infective endocarditis, 2,248 had coded endogenous endophthalmitis; diabetes with complications conferred OR 2.043, alcohol-use disorder OR 1.795, and cirrhosis OR 1.452. (shah2025riskfactorsfor pages 1-2)
- **Age/sex/geography:** Exogenous cohorts skew older because cataract surgery and anti-VEGF treatment increase with age. In one cohort, median age was 76.8 years for exogenous versus 60.5 for endogenous disease. Trauma cohorts are often predominantly working-age men; a 2024 metallic-injury study was 86.2% male. Organism distributions vary geographically—hypervirulent *Klebsiella* endogenous infection is especially important in East and Southeast Asia. (maher2026epidemiologymicrobiologymanagement pages 2-5, wu2024systematicinflammatoryindicators pages 1-2)

### Protective factors and gene–environment interactions

Strongly supported protective interventions are procedural rather than genetic: povidone–iodine antisepsis, sterile technique, prompt wound repair/foreign-body removal, and intracameral antibiotic prophylaxis during cataract surgery where adopted. No validated protective germline variant or modifier allele is known. Apparent host-genetic effects such as myeloid AMPKα1 activity are preclinical mechanistic observations, not population susceptibility loci. Thus, “gene–environment interaction” is best conceptualized as host immune/metabolic state interacting with pathogen virulence and inoculation route, rather than a validated clinical G×E association. (singh2024myeloidcellspecificdeletion pages 1-6)

## 3. Phenotypes

Typical disease is unilateral after a local procedure or injury; endogenous disease can be bilateral. Severity and progression range from indolent chronic inflammation to fulminant retinal destruction.

- **Reduced or rapidly declining vision:** core symptom, variable from mild blur to hand-motion/light-perception vision. Suggested HPO: decreased visual acuity; blindness. Presenting acuity is among the strongest outcome predictors. (nowosielski2026visualacuityinfluences pages 1-2, braga2024endogenousendophthalmitisdue pages 1-2)
- **Eye pain and photophobia:** common but not universal; pain can be absent in indolent or immunocompromised disease. Suggested HPO: eye pain; photophobia. (saeed2024auniquecase pages 1-3, braga2024endogenousendophthalmitisdue pages 1-2)
- **Red eye/conjunctival injection and eyelid edema:** inflammatory signs. Suggested HPO: conjunctival hyperemia; periorbital edema. (saeed2024auniquecase pages 1-3, krohn2024endogenousfungalendophthalmitis pages 1-2)
- **Anterior chamber cells/flare, fibrin, hypopyon:** signs of severe anterior inflammation. Suggested HPO: anterior uveitis; hypopyon. The 2024 *E. coli* case had a 3+/4+ anterior chamber reaction. (braga2024endogenousendophthalmitisdue pages 1-2)
- **Vitritis/vitreous haze, absent red reflex, poor fundus view:** defining posterior-segment manifestations. Suggested HPO: vitritis; vitreous opacity. The same *E. coli* case had 4+/4+ vitritis. (braga2024endogenousendophthalmitisdue pages 1-2)
- **Floaters:** common early posterior symptom. Suggested HPO: vitreous floaters. (braga2024endogenousendophthalmitisdue pages 1-2)
- **Retinal/choroidal infiltrates or abscesses:** particularly endogenous bacterial or fungal disease. Suggested HPO: chorioretinal inflammation; retinal lesion. A hypervirulent *Klebsiella* case showed retinochoroidal abscesses by ultrasonography. (saeed2024auniquecase pages 1-3)
- **Laboratory abnormalities:** ocular-fluid Gram stain/culture/PCR positivity; endogenous cases may have positive blood cultures, leukocytosis, elevated CRP, or systemic organ infection. No single blood biomarker is diagnostic.

**Onset:** Acute postoperative/post-injection disease often develops within approximately 3–7 days; an 18-year cohort reported a median of 5 days after procedure, whereas trabeculectomy-associated cases presented at a median 28 days. Chronic *C. acnes* or fungal disease can evolve over weeks or recur months after treatment withdrawal. (maher2026epidemiologymicrobiologymanagement pages 2-5, krohn2024endogenousfungalendophthalmitis pages 1-2)

**Quality of life:** Permanent monocular or bilateral visual loss affects reading, driving, employment, mobility, falls risk, and independence. Eye pain, repeated injections/surgery, prolonged antifungal treatment, and fear of losing the fellow eye add substantial burden. Endophthalmitis-specific EQ-5D/SF-36 reference values are limited; visual acuity and vision-related instruments such as NEI-VFQ are more disease-proximal.

## 4. Genetic and molecular information

No established **causal genes, pathogenic germline variants, chromosomal abnormalities, inheritance pattern, penetrance, anticipation, founder effect, or carrier frequency** applies to infectious endophthalmitis. ClinVar-style variant classification and routine WES/WGS, panel, CMA, karyotype, FISH, mtDNA, or repeat-expansion testing are therefore not indicated for diagnosis.

Host-response genes are research targets rather than disease-causing genes:

- **PRKAA1/AMPKα1:** Myeloid-specific deletion in mice worsened *S. aureus* infection, elevated IL-1β, TNF-α, IL-6 and CXCL2, shifted macrophages toward inflammatory M1 states, and impaired phagocytosis. Wild-type marrow transfer preserved retinal function. The abstract states that deletion “skewed macrophage polarization toward the inflammatory M1 phenotype and impaired the phagocytic clearance of *S. aureus*.” This is model-organism causality, not evidence for pathogenic human PRKAA1 variants. Published October 2024; DOI/URL: https://doi.org/10.4049/jimmunol.2400282. (singh2024myeloidcellspecificdeletion pages 1-6)
- **NLRP3/miR-223-3p:** Emerging translational work links extracellular-vesicle miR-223-3p with NLRP3 inflammasome modulation; potential diagnostic or therapeutic use remains experimental.
- **Fungal-response genes:** Murine *Candida* RNA sequencing highlighted CD3-associated signaling, CAMP, LCK, C-type lectin, NOD-like receptor, T-cell, and NK-cell pathways. These represent infection-induced expression changes rather than inherited pathogenic variants. (khapuinamai2024unveilingtheinnate pages 1-2)

No reproducible disease-specific epigenetic signature, somatic mutation, structural genomic lesion, or clinical pharmacogenomic algorithm is established.

## 5. Environmental and lifestyle information

Relevant non-genetic exposures are primarily iatrogenic or traumatic: intraocular surgery, repeated injection, penetrating metal/organic injury, soil contamination, contact with contaminated compounded products, and healthcare-associated bloodstream infection. Hot/humid environments and regional microbiology may alter organism distributions, but no universal environmental exposure–response estimate is available.

Smoking, diet, alcohol, and exercise are not established direct causes of exogenous disease. Alcohol-use disorder was associated with endogenous disease among endocarditis inpatients, plausibly through liver disease, immune dysfunction, and infection risk rather than a direct ocular toxic effect. Diabetes and immunosuppressive therapy are clinically important host-environment modifiers. (shah2025riskfactorsfor pages 1-2)

There is no contagious person-to-person ocular transmission in ordinary endophthalmitis. The underlying systemic infection may itself be transmissible depending on the organism, but endophthalmitis is generally a complication rather than an independently transmitted disease.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream trigger:** Direct inoculation breaches the cornea/sclera or introduces organisms during surgery/injection; alternatively, bloodstream organisms cross retinal/choroidal vascular barriers.
2. **Early microbial phase:** Organisms proliferate in immune-privileged, nutrient-rich aqueous/vitreous. Capsules, adhesins, biofilm, proteases, cytolysins, and toxins influence virulence. *Bacillus*, streptococci, *Pseudomonas*, *Klebsiella*, and molds can cause especially rapid damage.
3. **Innate recognition:** Retinal Müller glia, resident microglia/macrophages, vascular cells, and infiltrating myeloid cells detect pathogen-associated molecules through TLR, C-type lectin, and NOD-like receptor pathways.
4. **Inflammatory amplification:** NF-κB/inflammasome signaling and cytokines/chemokines—including IL-1β, TNF-α, IL-6 and CXCL2—recruit neutrophils and monocytes. These cells clear organisms but release proteases, reactive oxygen species, and inflammatory mediators that damage the blood-retinal barrier and neurons.
5. **Downstream tissue injury:** Vitreous opacification, fibrin, edema, photoreceptor/inner-retinal dysfunction, ischemia, necrosis, retinal detachment, and fibrosis/PVR produce vision loss. Delayed therapy allows both microbial burden and immunopathology to become irreversible. (singh2024myeloidcellspecificdeletion pages 1-6)

Suggested terms include GO: inflammatory response, response to bacterium/fungus, neutrophil migration, macrophage activation, phagocytosis, cytokine-mediated signaling, NOD-like receptor signaling, inflammasome complex assembly, reactive oxygen species metabolic process, and apoptotic process. Suggested CL terms: neutrophil, monocyte, macrophage, microglial cell, retinal Müller glial cell, T cell, NK cell, retinal ganglion cell, and photoreceptor cell.

### Recent molecular profiling

A 2024 C57BL/6 murine *Candida albicans* study found 27,717 differentially expressed transcripts overall and 1,493 significant DEGs—924 upregulated and 569 downregulated. Upregulated pathways included T-cell signaling, NK-cell cytotoxicity, C-type lectin and NOD-like receptor signaling; MAPK, cAMP, and metabolic pathways were downregulated. The model used intravitreal *Candida* and sampled at 24 and 72 hours, so it depicts early experimental disease rather than the full human course. Published September 2024; DOI/URL: https://doi.org/10.1021/acsomega.4c05081. (khapuinamai2024unveilingtheinnate pages 1-2)

The 2024 AMPK study integrated retinal transcriptomic/metabolic findings implicating immune signaling, antimicrobial defense, ER stress, trafficking, NAD+ metabolism, and lipid biosynthesis. These data support immunometabolic regulation of resolution but do not yet justify AMPK-targeted human treatment. (singh2024myeloidcellspecificdeletion pages 1-6)

Human single-cell, spatial-transcriptomic, lipidomic, and validated multi-omic diagnostic signatures remain sparse. This is an important evidence gap.

## 7. Anatomical structures affected

The primary organ is the **eye**, especially:

- Vitreous body and vitreous chamber—major inflammatory compartment.
- Aqueous humor/anterior chamber—cells, flare, fibrin, and hypopyon.
- Retina, retinal pigment epithelium, and choroid—neuronal injury, infiltrates, abscesses, ischemia, edema.
- Ciliary body, lens capsule, and intraocular lens surfaces—potential microbial reservoirs in chronic disease.
- Cornea and sclera—entry routes or contiguous sources; extensive infection may progress to panophthalmitis.
- Optic nerve—secondary injury in destructive disease.

Suggested UBERON terms: eye, vitreous humor, anterior chamber of eyeball, retina, retinal pigment epithelium, choroid, ciliary body, lens, cornea, sclera, and optic nerve. Suggested GO cellular components include inflammasome complex, extracellular vesicle, lysosome/phagolysosome, plasma membrane, and extracellular space. Disease is usually unilateral after local inoculation but can be bilateral in endogenous fungemia.

A recurrent 2024 dematiaceous fungal case demonstrated persistent organisms at the ciliary processes and posterior lens surface, illustrating protected anatomical reservoirs. Despite local/systemic therapy, recurrence led to painful glaucoma and enucleation. Published June 2024; DOI/URL: https://doi.org/10.1186/s12348-024-00408-y. (krohn2024endogenousfungalendophthalmitis pages 1-2)

## 8. Temporal development

Acute bacterial disease generally progresses over hours to days. The key therapeutic window is before irreversible retinal damage: one 2024 trauma series found intervention within two hours of symptom exacerbation associated with fewer complications (AUC 0.708, 95% CI 0.547–0.838; p=0.047). This small retrospective result supports urgency but is not a universally validated cutoff. (wu2024systematicinflammatoryindicators pages 1-2)

A practical course is:

- **Early:** pain/blur, anterior reaction, small retinal infiltrate or mild vitritis.
- **Intermediate:** dense vitritis, hypopyon, marked acuity loss, retinal/choroidal lesions.
- **Advanced:** no fundus view, retinal necrosis/ischemia or detachment, panophthalmitis.
- **Recovery/sequelae:** clearing inflammation with variable visual recovery, or macular edema, epiretinal membrane, PVR, retinal detachment, glaucoma, hypotony, phthisis, or enucleation.

Fungal and *C. acnes* disease may be indolent or relapsing. The *Cladophialophora* case recurred three months after treatment discontinuations despite prolonged antifungals, illustrating that apparent remission may not equal eradication. (krohn2024endogenousfungalendophthalmitis pages 1-2)

## 9. Epidemiology, inheritance, and population

No universal prevalence per 100,000 is meaningful because endophthalmitis is usually reported per procedure or among bloodstream infections. Historical post-cataract rates were approximately 0.13–0.15%; contemporary rates are often lower with small-incision surgery, antisepsis, and intracameral prophylaxis. Post-injection risk in one Australian cohort was 0.035%, approximately 1 per 2,857 injections, with cumulative risk rising as injections accumulate. (maher2026epidemiologymicrobiologymanagement pages 8-9)

In 232 Australian cases from 2006–2024, exogenous disease accounted for 87.1%, endogenous 12.9%, and annual cases declined (slope −0.17/year; p=0.005), driven by declining post-cataract disease while injection-associated cases rose. Organisms were predominantly Gram-positive cocci. These are referral-center distributions, not national incidence estimates. (maher2026epidemiologymicrobiologymanagement pages 1-2, maher2026epidemiologymicrobiologymanagement pages 2-5)

Sex and age patterns reflect exposure: older adults dominate postoperative/injection disease, whereas traumatic cases often affect younger men. Endogenous disease varies with regional bloodstream pathogens; hypervirulent *Klebsiella* and diabetes are particularly relevant in Asian populations. There is no AD, AR, X-linked, mitochondrial, polygenic-inheritance, carrier, consanguinity, anticipation, or mosaicism framework for the disease.

## 10. Diagnostics

### Emergency clinical work-up

Diagnosis is clinical and treatment should not await laboratory confirmation. Assess visual acuity, pupils, intraocular pressure, slit-lamp inflammation/hypopyon, wound/bleb/cornea, and dilated fundus. If media opacity prevents retinal examination, **B-scan ultrasound** evaluates vitreous echoes, membranes, retinal detachment, choroidal thickening, or abscess. OCT/OCTA can characterize macular or chorioretinal sequelae once imaging is possible. (saeed2024auniquecase pages 1-3)

Obtain aqueous and preferably vitreous samples for microscopy, aerobic/anaerobic bacterial and fungal culture, susceptibility testing, and targeted or broad-range PCR. In endogenous disease, obtain multiple blood cultures before systemic antimicrobials when feasible and investigate endocarditis, liver/renal/urinary infection, catheter infection, or other source.

Culture sensitivity is limited: positivity was 44.04% in a 218-case Chinese series and 53.2% in a German series; in the latter, overall organism detection was 58.7%, while PCR detected 43.5%. The authors concluded that no single method identified every infection, supporting combined culture and molecular testing. (englisch2026microbiologicaletiologyof pages 1-2, li2025clinicalretrospectiveanalysis pages 1-2)

### Emerging diagnostics

Broad-range 16S/18S/ITS PCR and metagenomic next-generation sequencing can detect nonviable, unculturable, unexpected, or antibiotic-exposed organisms. A 2024 infectious-uveitis pilot tested aqueous from 20 eyes; MGS found candidate pathogens in seven and conventional ELISA/qPCR verified five. Its abstract states that MGS “cannot completely replace the traditional diagnostic techniques,” accurately reflecting current limitations: contamination, low biomass, background reads, cost, turnaround time, and uncertain causal interpretation. Molecular sequencing is therefore an adjunct, especially for culture-negative, atypical, fungal, or chronic cases, not a replacement for culture and susceptibility testing. (asao2025overviewofmicroorganisms pages 26-28)

### Differential diagnosis

Rule out toxic anterior-segment syndrome—usually earlier, often painless, and initially anterior-predominant—sterile post-injection inflammation, severe noninfectious uveitis, retained lens material, lens-induced inflammation, suprachoroidal hemorrhage, retinal necrosis, intraocular foreign-body inflammation, and vitreoretinal lymphoma. Vitreoretinal lymphoma is especially important in chronic, steroid-responsive/recurrent “uveitis.”

No asymptomatic population screening or genetic testing is recommended. Targeted ophthalmic examination may be appropriate in candidemia or high-risk bacteremia according to local infectious-disease/ophthalmology guidance and symptoms.

## 11. Outcome and prognosis

Endophthalmitis rarely determines long-term survival directly, except as a marker of severe systemic sepsis; conventional 5- or 10-year survival measures are not useful. Ocular morbidity is substantial.

In the Australian cohort, 52.5% improved by at least one visual category. In the 218-case Chinese study, acuity >0.02 increased from 12.39% at admission to 27.98% at discharge (p<0.001). A later cohort reported improvement from median 2.3 logMAR at diagnosis to 1.0 at six months. (maher2026epidemiologymicrobiologymanagement pages 5-8, li2025clinicalretrospectiveanalysis pages 1-2, nowosielski2026visualacuityinfluences pages 1-2)

Poor prognostic factors include light-perception/no-light-perception presentation, treatment delay, virulent streptococci, *Bacillus*, Gram-negative rods or molds, endogenous route, corneal source, retinal/choroidal involvement, IOFB, retinal detachment, immunosuppression, and inadequate source control. Presenting visual acuity is consistently a major predictor. In one exogenous cohort, delayed surgery increased the re-intervention hazard (HR 5.7, 95% CI 2.9–11.1; p<0.001), although retrospective confounding limits causal interpretation. (nowosielski2026visualacuityinfluences pages 1-2)

Complications include macular edema, epiretinal membrane, retinal detachment/PVR, optic atrophy, secondary glaucoma, hypotony/phthisis, cataract, recurrent infection, evisceration/enucleation, and permanent blindness. Fungal cases may also reflect life-threatening disseminated infection. (krohn2024endogenousfungalendophthalmitis pages 1-2)

## 12. Treatment

### Emergency algorithm

1. Treat suspected infectious endophthalmitis as a same-day emergency.
2. Obtain vitreous/aqueous samples without materially delaying treatment.
3. Give empiric **intravitreal vancomycin plus ceftazidime** for broad Gram-positive and Gram-negative coverage; local protocols and allergy/resistance patterns govern alternatives.
4. Consider early pars plana vitrectomy for light-perception vision, dense vitreous disease, severe/rapidly progressive infection, IOFB, retinal complications, fungal infection, inadequate response, or need for better diagnostic/source control.
5. Add systemic antimicrobials for endogenous disease and eradicate the systemic source. Routine systemic antibiotics add limited value in uncomplicated acute post-cataract disease, consistent with landmark EVS evidence.
6. Use cycloplegia, analgesia, careful pressure control, and topical corticosteroid only under antimicrobial coverage and specialist direction. The role of intravitreal corticosteroid remains controversial.

Intravitreal therapy was used in 97.3% and vitrectomy in 41.5% of the Australian cohort. The vitrectomy win ratio was 1.31 overall but 2.28 in the light-perception subgroup; neither estimate reached conventional significance in that retrospective analysis, but the direction aligns with the landmark Endophthalmitis Vitrectomy Study. (maher2026epidemiologymicrobiologymanagement pages 5-8, maher2026epidemiologymicrobiologymanagement pages 1-2)

Suggested NCIT terms: Intravitreal Injection; Vancomycin; Ceftazidime; Pars Plana Vitrectomy/Vitrectomy; Antibiotic Therapy; Antifungal Therapy; Cycloplegic Agent; Corticosteroid Therapy.

### Organism-specific considerations

- **Bacteria:** tailor to ocular-fluid susceptibilities; repeat intravitreal treatment or vitrectomy if worsening.
- **Yeasts:** intravitreal amphotericin B or voriconazole plus systemic fluconazole/voriconazole when susceptible, with vitrectomy for significant vitritis.
- **Molds:** intravitreal and systemic voriconazole are commonly used; amphotericin or other azoles depend on species/susceptibility. Surgical source control is frequently required.
- **Rare fungi:** prolonged therapy and repeated sampling may be necessary. A 2024 *Cladophialophora* case required amphotericin, itraconazole, repeated intravitreal voriconazole, posaconazole, and isavuconazole yet ultimately underwent enucleation. (krohn2024endogenousfungalendophthalmitis pages 1-2)

There is no approved gene, cell, RNA, or immune-checkpoint therapy. AMPK activation, inflammasome modulation, EV-miRNA biomarkers, antimicrobial nanoparticles, and phage/host-directed approaches remain experimental.

### Trials and implementation

Relevant ClinicalTrials.gov records found include the completed phase-3 EVS (NCT00000130), ESCRS cataract prophylaxis study (NCT00136344; approximately 35,000), intracameral moxifloxacin prevention trial (NCT02595359; phase 2, 1,000), early vitrectomy studies NCT04192994 and NCT05249413, recruiting nanopore-sequencing study NCT05372861, and recruiting vascular-change observational study NCT07175311. These records should be checked directly for current status and posted results before structured ingestion.

## 13. Prevention

**Primary prevention:** preoperative ocular-surface assessment; treatment of active lid/corneal infection when surgery is elective; povidone–iodine preparation of conjunctival sac and periocular skin; sterile lid speculum, instruments and medication handling; secure wounds; and intracameral antibiotic prophylaxis for cataract surgery where supported by policy. Intracameral agents prevent rather than treat infection; drug choice, formulation, dilution safety, allergy, and stewardship matter.

**Injection prevention:** povidone–iodine remains central; minimize talking or use masks according to protocol, avoid needle contact with lids/lashes, use sterile single-use equipment, and educate patients about pain, redness, or vision decline. Routine peri-injection topical antibiotics are generally not favored because they do not clearly reduce risk and select resistance.

**Trauma prevention:** occupational eye protection; urgent closure of open globe; prompt IOFB removal and antimicrobial prophylaxis based on injury contamination. The 2024 metallic-trauma data reinforce rapid escalation when symptoms worsen. (wu2024systematicinflammatoryindicators pages 1-2)

**Secondary/tertiary prevention:** rapid recognition, immediate intravitreal therapy, culture-guided adjustment, systemic-source control, serial retinal imaging, and management of retinal detachment, edema, glaucoma, and low-vision needs. No vaccine, genetic screening, carrier testing, prenatal testing, or population screening program applies.

## 14. Other species and natural disease

Naturally occurring endophthalmitis occurs in companion and production animals after trauma, surgery, corneal ulceration, or hematogenous infection. Reported host species include dog (*Canis lupus familiaris*, NCBI Taxon 9615), cat (*Felis catus*, 9685), horse (*Equus caballus*, 9796), cattle (*Bos taurus*, 9913), and birds. Organisms and anatomy overlap with humans, but exposure patterns, veterinary access, and likelihood of enucleation differ. Breed-specific Mendelian predisposition and VBO mappings are not established as general features.

The condition itself is not ordinarily zoonotic. Shared environmental organisms may infect different species, and animal-associated trauma could introduce pathogens, but cross-species transmission is not a defining mechanism.

## 15. Model organisms

**Mouse:** C57BL/6 intravitreal inoculation with *S. aureus*, *Pseudomonas*, *Bacillus*, *Candida*, or *Aspergillus* is the dominant mammalian model. It reproduces microbial growth, neutrophil influx, cytokine induction, retinal dysfunction, and histologic damage, and supports knockout, bone-marrow chimera, transcriptomic, metabolomic, and treatment experiments. The 2024 AMPKα1 model demonstrated myeloid-cell control of macrophage phenotype and bacterial clearance; the *Candida* model resolved early innate/adaptive transcriptional programs. (singh2024myeloidcellspecificdeletion pages 1-6, khapuinamai2024unveilingtheinnate pages 1-2)

**Rabbit:** Larger eyes facilitate surgery, pharmacokinetics, intravitreal dosing, implant testing, and serial sampling, although immunological reagents/genetic tools are less extensive than in mice.

**Zebrafish (*Danio rerio*, NCBI Taxon 7955):** Intravitreal *S. aureus* did not reproduce destructive murine/human disease. Fish maintained retinal architecture and rapidly cleared bacteria via retinal vessels/optic nerve with a monocyte/macrophage response. It is therefore a model of protective innate clearance rather than a faithful severe-endophthalmitis model.

**In vitro/ex vivo:** Retinal Müller glia, microglia/macrophages, retinal pigment epithelium, organotypic retinal explants, and ocular-fluid pathogen assays support receptor, cytokine, biofilm, toxicity, and antimicrobial studies. Human retinal organoids and eye-on-chip systems are promising but not yet validated replacements for in vivo disease.

Principal limitations are artificial high-dose intravitreal inoculation, compressed time course, species-specific immunity, lack of cataract hardware or human comorbidities, and imperfect modeling of vision. Model findings should be annotated as preclinical rather than human causal evidence.

## Recent 2023–2024 research highlights and expert interpretation

1. **Immunometabolic regulation:** The October 2024 AMPKα1 study gives causal model evidence that macrophage metabolism can determine bacterial clearance versus destructive inflammation. It identifies a plausible adjunctive-treatment direction, but human dosing and the risk of suppressing antimicrobial defense require study. (singh2024myeloidcellspecificdeletion pages 1-6)
2. **Fungal systems biology:** The September 2024 *Candida* transcriptome demonstrated coordinated innate and adaptive activation rather than purely neutrophil-driven disease. The enormous DEG count and intravitreal challenge design demand cautious translation. (khapuinamai2024unveilingtheinnate pages 1-2)
3. **Precision microbiology:** Molecular sequencing can rescue selected culture-negative diagnoses, but the most defensible current implementation is culture plus targeted PCR/mNGS—not sequencing alone—because only culture yields routine phenotypic susceptibility. (englisch2026microbiologicaletiologyof pages 1-2, asao2025overviewofmicroorganisms pages 26-28)
4. **Urgency in trauma:** The December 2024 metallic-IOFB cohort links delayed treatment and systemic inflammatory patterns with difficult control. Its small sample supports, but does not independently establish, a universal two-hour threshold. (wu2024systematicinflammatoryindicators pages 1-2)
5. **Changing epidemiology:** Better cataract prophylaxis has reduced post-cataract disease in some systems, while repeated anti-VEGF injections shift absolute case burden toward post-injection infection. Prevention programs should therefore monitor both procedure volume and infection per procedure. (maher2026epidemiologymicrobiologymanagement pages 8-9, maher2026epidemiologymicrobiologymanagement pages 2-5)

## Selected exact abstract quotations

- “Endogenous endophthalmitis (EE) is a rare but severe intraocular infection resulting from hematogenous dissemination of microorganisms.” Alshehri, September 2024; https://doi.org/10.7759/cureus.70523. (alshehri2024endogenousendophthalmitisassociated pages 1-2)
- “Endophthalmitis is a severe form of purulent inflammation caused by the infection of the intraocular tissues or fluids.” Braga et al., March 2024; https://doi.org/10.5935/0004-2749.2023-0066. (braga2024endogenousendophthalmitisdue pages 1-2)
- “The deletion of AMPKα1 in myeloid cells skewed macrophage polarization toward the inflammatory M1 phenotype and impaired the phagocytic clearance of *S. aureus* by macrophages.” Singh et al., October 2024; https://doi.org/10.4049/jimmunol.2400282. (singh2024myeloidcellspecificdeletion pages 1-6)
- The rare-fungal report concluded that, “Despite early diagnosis and prolonged local and systemic antifungal therapy, it was not possible to achieve long-term control of the fungal infection.” Krohn et al., June 2024; https://doi.org/10.1186/s12348-024-00408-y. (krohn2024endogenousfungalendophthalmitis pages 1-2)

PMIDs were not consistently available in the retrieved full-text metadata; DOI URLs are therefore supplied and should be resolved against PubMed during final database curation.

## Ontology-ready summary

The following table consolidates phenotype, anatomical, mechanistic, diagnostic, treatment, and model annotations. Exact ontology identifiers marked uncertain should be validated against current releases before production ingestion.

| domain | knowledge-base statement | suggested ontology terms/IDs | evidence type |
|---|---|---|---|
| Disease definition | Endophthalmitis is a severe intraocular infection/inflammation involving ocular fluids and tissues; major clinical forms are exogenous (postoperative, post-injection, post-traumatic) and endogenous (hematogenous spread). (maher2026epidemiologymicrobiologymanagement pages 1-2, alshehri2024endogenousendophthalmitisassociated pages 1-2) | MONDO: term-name-only suggestion `endophthalmitis` (exact MONDO ID uncertain); MeSH: `Endophthalmitis` (term-name-only); ICD-10: H44.0 `Purulent endophthalmitis`, H44.1 `Other endophthalmitis` | Human clinical cohorts; systematic review |
| Resource provenance | Most knowledge here is aggregated disease-level evidence from cohorts, systematic reviews, guidelines, and model-organism studies rather than individual-patient EHR alone. (maher2026epidemiologymicrobiologymanagement pages 5-8, alshehri2024endogenousendophthalmitisassociated pages 1-2, singh2024myeloidcellspecificdeletion pages 1-6) | Evidence provenance annotation: aggregated disease-level resource | Mixed evidence synthesis |
| Classification | Exogenous disease predominates overall; endogenous disease is a minority but clinically important subtype. In a German state study, only 7.9% were endogenous; in an Australian cohort, 87.1% were exogenous. (englisch2026microbiologicaletiologyof pages 1-2, maher2026epidemiologymicrobiologymanagement pages 1-2) | Disease subtypes: `exogenous endophthalmitis` (term-name-only), `endogenous endophthalmitis` (term-name-only) | Human epidemiology |
| Disease timing | Presentation is usually acute/subacute after ocular procedures; median time to presentation was 5 days post-procedure in one 18-year cohort. (maher2026epidemiologymicrobiologymanagement pages 2-5) | HPO term-name-only suggestions: `Acute onset`, `Abnormality of vision`; temporal annotation: acute/subacute | Human cohort |
| Phenotype | Reduced visual acuity is a core presenting feature and major prognostic marker. (nowosielski2026visualacuityinfluences pages 1-2, braga2024endogenousendophthalmitisdue pages 1-2) | HPO: `Decreased visual acuity` (exact ID not asserted) | Human cohort; case report |
| Phenotype | Ocular pain is common, especially in endogenous fungal or bacterial presentations. (saeed2024auniquecase pages 1-3, krohn2024endogenousfungalendophthalmitis pages 1-2) | HPO term-name-only: `Eye pain` | Human case reports |
| Phenotype | Red eye/conjunctival injection is a typical inflammatory manifestation. (saeed2024auniquecase pages 1-3, krohn2024endogenousfungalendophthalmitis pages 1-2) | HPO term-name-only: `Red eye` | Human case reports |
| Phenotype | Vitritis/vitreous opacity is a hallmark sign and often limits retinal visualization. (krohn2024endogenousfungalendophthalmitis pages 1-2, braga2024endogenousendophthalmitisdue pages 1-2) | HPO term-name-only: `Vitritis`, `Vitreous haze` | Human case reports |
| Phenotype | Hypopyon/anterior chamber reaction occurs in severe bacterial cases. (saeed2024auniquecase pages 1-3, braga2024endogenousendophthalmitisdue pages 1-2) | HPO term-name-only: `Hypopyon`, `Anterior chamber inflammation` | Human case reports |
| Phenotype | Floaters and photophobia may occur in endogenous disease. (braga2024endogenousendophthalmitisdue pages 1-2) | HPO term-name-only: `Floaters`, `Photophobia` | Human case report |
| Complications | Severe outcomes include retinal damage, retinal detachment/PVR after surgery, secondary glaucoma, enucleation, and permanent vision loss. (krohn2024endogenousfungalendophthalmitis pages 1-2, nowosielski2026visualacuityinfluences pages 1-2) | HPO term-name-only: `Retinal detachment`, `Secondary glaucoma`, `Blindness` | Human case report; cohort |
| Anatomy | Primary affected compartments are vitreous body and aqueous/anterior chamber, with spread to retina and choroid; fungal disease may persist at ciliary processes and posterior lens surface. (krohn2024endogenousfungalendophthalmitis pages 1-2, braga2024endogenousendophthalmitisdue pages 1-2) | UBERON term-name-only: `vitreous humor`, `anterior chamber of eyeball`, `retina`, `choroid`, `ciliary body`, `lens` | Human pathology/case reports |
| Localization | Endogenous cases may show retinochoroidal abscess/chorioretinal involvement. (saeed2024auniquecase pages 1-3) | UBERON/HPO term-name-only: `retinochoroidal abscess`, `chorioretinal lesion` | Human imaging/case report |
| Etiology | Exogenous causes include cataract surgery, intravitreal injection, vitrectomy, glaucoma surgery, and penetrating trauma/IOFB. (englisch2026microbiologicaletiologyof pages 1-2, wu2024systematicinflammatoryindicators pages 1-2) | Exposure annotations: `cataract surgery`, `intravitreal injection`, `penetrating eye injury`, `intraocular foreign body` | Human cohort |
| Etiology | Endogenous disease results from hematogenous dissemination during systemic infection; associated settings include bacteremia, infective endocarditis, urinary tract infection, diabetes, immunosuppression, and indwelling catheters. (alshehri2024endogenousendophthalmitisassociated pages 1-2, shah2025riskfactorsfor pages 1-2, braga2024endogenousendophthalmitisdue pages 1-2) | Disease/exposure term-name-only: `bacteremia`, `infective endocarditis`, `urinary tract infection`, `immunosuppression`, `diabetes mellitus` | Systematic review; cohort; case report |
| Pathogens | Gram-positive cocci predominate overall; `Staphylococcus epidermidis` is the most common organism in multiple cohorts. (englisch2026microbiologicaletiologyof pages 1-2, li2025clinicalretrospectiveanalysis pages 1-2) | NCBI Taxonomy term-name-only: `Staphylococcus epidermidis`, `Staphylococcus aureus`, `Enterococcus faecalis` | Human microbiology cohorts |
| Pathogens | Other important bacteria include streptococci, `Pseudomonas aeruginosa`, `Escherichia coli`, and hypervirulent `Klebsiella pneumoniae`. (maher2026epidemiologymicrobiologymanagement pages 5-8, saeed2024auniquecase pages 1-3, braga2024endogenousendophthalmitisdue pages 1-2) | NCBI Taxonomy term-name-only: `Streptococcus spp.`, `Pseudomonas aeruginosa`, `Escherichia coli`, `Klebsiella pneumoniae` | Human cohort; case reports |
| Pathogens | Fungal causes include `Candida albicans`, `Aspergillus spp.`, and rare dematiaceous fungi such as `Cladophialophora devriesii`; fungi are relatively more important in endogenous disease. (alshehri2024endogenousendophthalmitisassociated pages 1-2, krohn2024endogenousfungalendophthalmitis pages 1-2, englisch2026microbiologicaletiologyof pages 1-2) | NCBI Taxonomy term-name-only: `Candida albicans`, `Aspergillus spp.`, `Cladophialophora devriesii` | Systematic review; case report; cohort |
| Epidemiology | Post-cataract and post-injection disease are currently dominant exogenous forms; one Australian cohort found both accounted for 38.1% each among all cases. (maher2026epidemiologymicrobiologymanagement pages 2-5) | Epidemiology annotation only | Human cohort |
| Epidemiology | Post-injection endophthalmitis risk in one anti-VEGF era cohort was approximately 0.035% (about 1 in 2,857 injections). (maher2026epidemiologymicrobiologymanagement pages 8-9) | Epidemiology annotation only | Human cohort |
| Risk factor | Metallic intraocular foreign body correlates with faster symptom onset and poorer control after vitrectomy. (wu2024systematicinflammatoryindicators pages 1-2, li2025clinicalretrospectiveanalysis pages 1-2) | Exposure term-name-only: `intraocular foreign body` | Human cohort |
| Risk factor | In infective endocarditis patients, diabetes, alcohol use disorder, cirrhosis, and older age increased endogenous endophthalmitis risk. (shah2025riskfactorsfor pages 1-2) | Disease/exposure term-name-only: `diabetes mellitus`, `alcohol use disorder`, `cirrhosis`, `advanced age` | Human database study |
| Protective factor | In a national post-injection study, non-smoking was protective. (maher2026epidemiologymicrobiologymanagement pages 8-9) | Exposure term-name-only: `non-smoker status` | Human epidemiology |
| Immune mechanism | Disease pathogenesis involves rapid innate immune activation with neutrophil infiltration, inflammatory cytokines, and retinal tissue injury. (singh2024myeloidcellspecificdeletion pages 1-6, khapuinamai2024unveilingtheinnate pages 1-2) | GO term-name-only: `neutrophil migration`, `inflammatory response`, `cytokine-mediated signaling pathway`; CL term-name-only: `neutrophil` | Murine model; translational |
| Immune mechanism | Key inflammatory mediators elevated in bacterial endophthalmitis include IL-1β, TNF-α, IL-6, and CXCL2. (singh2024myeloidcellspecificdeletion pages 1-6) | GO term-name-only: `interleukin-1 production`, `tumor necrosis factor production`, `interleukin-6 production`, `chemokine production` | Murine model |
| Immune mechanism | Macrophage phenotype influences outcome; myeloid AMPKα1 supports infection resolution, whereas deletion skews toward inflammatory M1 macrophages and impairs phagocytic clearance. (singh2024myeloidcellspecificdeletion pages 1-6) | GO term-name-only: `macrophage activation`, `phagocytosis`, `response to bacterium`; CL term-name-only: `macrophage`, `monocyte` | Murine model |
| Immune mechanism | Fungal endophthalmitis transcriptomics showed enriched T-cell signaling, NK-cell mediated cytotoxicity, C-type lectin receptor signaling, and NOD-like receptor signaling. (khapuinamai2024unveilingtheinnate pages 1-2) | GO/Pathway term-name-only: `T cell activation`, `natural killer cell mediated immunity`, `pattern recognition receptor signaling pathway`, `NOD-like receptor signaling pathway` | Murine transcriptomics |
| Molecular profiling | In murine `Candida albicans` endophthalmitis, 1,493 significant DEGs were reported (924 upregulated, 569 downregulated). (khapuinamai2024unveilingtheinnate pages 1-2) | Omics annotation only | Murine RNA-seq |
| Molecular profiling | Extracellular-vesicle miR-223-3p is linked to modulation of the NLRP3 inflammasome and may have biomarker potential in culture-negative bacterial disease. (singh2024myeloidcellspecificdeletion pages 1-6) | GO term-name-only: `inflammasome complex assembly`; molecular entities: `miR-223-3p`, `NLRP3` | Murine + human vitreous translational study |
| Cell types | Major involved cells include neutrophils, monocytes/macrophages, retinal immune cells, T cells, and NK cells. (singh2024myeloidcellspecificdeletion pages 1-6, khapuinamai2024unveilingtheinnate pages 1-2) | CL term-name-only: `neutrophil`, `monocyte`, `macrophage`, `T cell`, `natural killer cell`, `retinal Müller glial cell` (supportive literature context) | Murine model |
| Diagnostics | Core microbiology remains vitreous/aqueous sampling with Gram stain/culture plus molecular testing; no single method detects all cases. (englisch2026microbiologicaletiologyof pages 1-2) | Diagnostic procedure term-name-only: `vitreous tap`, `aqueous tap`, `microbial culture`, `broad-range PCR` | Human cohort |
| Diagnostics | Culture positivity is incomplete: 58.7% in one German series and 44.0% in one Chinese series. (englisch2026microbiologicaletiologyof pages 1-2, li2025clinicalretrospectiveanalysis pages 1-2) | Laboratory finding annotation only | Human cohorts |
| Diagnostics | Metagenomic sequencing is an emerging adjunct for infectious uveitis/endophthalmitis workups, especially when culture/PCR are negative or limited. (asao2025overviewofmicroorganisms pages 26-28) | Diagnostic procedure term-name-only: `metagenomic sequencing`, `mNGS` | Review/technology assessment |
| Imaging | B-scan ultrasonography can identify vitritis and retinochoroidal abscess when the fundus view is obscured. (saeed2024auniquecase pages 1-3, braga2024endogenousendophthalmitisdue pages 1-2) | Imaging term-name-only: `B-scan ultrasonography` | Human case reports |
| Differential diagnosis | Important mimics include noninfectious uveitis and vitreoretinal lymphoma; distinguishing infection is clinically critical. (asao2025overviewofmicroorganisms pages 26-28) | Disease term-name-only: `uveitis`, `vitreoretinal lymphoma` | Review/contextual expert synthesis |
| Treatment | Standard empiric bacterial therapy remains intravitreal vancomycin plus ceftazidime; intravitreal antibiotics were used in 97.3% of cases in one large cohort. (nowosielski2026visualacuityinfluences pages 1-2, maher2026epidemiologymicrobiologymanagement pages 1-2) | NCIT term-name-only: `Intravitreal Injection`, `Vancomycin`, `Ceftazidime` | Human cohort; expert-standard practice |
| Treatment | Pars plana vitrectomy is frequently used for severe disease, diagnostic sampling, or poor initial vision; one cohort reported vitrectomy in 41.5% of cases, and benefit appears greatest in light-perception presentations. (maher2026epidemiologymicrobiologymanagement pages 5-8, maher2026epidemiologymicrobiologymanagement pages 1-2) | NCIT term-name-only: `Vitrectomy`, `Pars Plana Vitrectomy` | Human cohort; EVS-aligned expert practice |
| Treatment | Fungal disease often requires combined local and systemic antifungal therapy, with cases using amphotericin B, voriconazole, posaconazole, itraconazole, or isavuconazole. (krohn2024endogenousfungalendophthalmitis pages 1-2) | NCIT term-name-only: `Amphotericin B`, `Voriconazole`, `Posaconazole`, `Itraconazole`, `Isavuconazole` | Human case report |
| Treatment outcomes | Visual improvement is common but incomplete; one cohort found 52.5% improved, while presenting BCVA strongly predicts final outcome. (maher2026epidemiologymicrobiologymanagement pages 5-8, nowosielski2026visualacuityinfluences pages 1-2) | Outcome annotation only | Human cohorts |
| Prevention | Intracameral antibiotic prophylaxis after cataract surgery is a major preventive strategy; modern post-cataract rates are substantially lower than historical ~0.13%–0.15%. (li2025clinicalretrospectiveanalysis pages 1-2) | NCIT term-name-only: `Antibiotic Prophylaxis`, `Intracameral Administration` | Editorial/surveillance synthesis |
| Prevention | Peri-procedural sterile protocols and microbiological surveillance are central to prevention, especially as post-injection cases rise with anti-VEGF use. (maher2026epidemiologymicrobiologymanagement pages 8-9, maher2026epidemiologymicrobiologymanagement pages 1-2) | Public health/clinical process annotation only | Human cohort |
| Genetics | No established Mendelian causal gene defines infectious endophthalmitis as a disease entity. | N/A for causal Mendelian genes | Not applicable |
| Inheritance | No Mendelian inheritance pattern applies; susceptibility is primarily infectious/procedural/systemic-risk based rather than inherited as a monogenic disorder. | N/A for AD/AR/X-linked inheritance | Not applicable |
| Pathogenic variants | No disease-defining germline pathogenic variant set is established for endophthalmitis. | N/A for variant annotation | Not applicable |
| Genetic testing | Routine clinical genetic testing (single-gene, panel, WES/WGS, CMA, FISH, mtDNA, repeat expansion) is not standard for diagnosis of infectious endophthalmitis. | N/A for genetic testing workflow | Not applicable |
| Model organisms | Mouse intravitreal infection models are widely used for bacterial and fungal pathogenesis and treatment studies. (singh2024myeloidcellspecificdeletion pages 1-6, khapuinamai2024unveilingtheinnate pages 1-2) | Model annotation only | Model organism |
| Model organisms | Zebrafish are comparatively resistant to `Staphylococcus aureus` endophthalmitis and may model protective innate responses rather than full human disease severity. (maher2026epidemiologymicrobiologymanagement pages 2-5) | Model annotation only | Model organism |
| Comparative limitation | Animal models reproduce inflammatory and microbiological features but may not fully capture human procedure-related heterogeneity, chronicity, or visual outcome trajectories. (singh2024myeloidcellspecificdeletion pages 1-6, khapuinamai2024unveilingtheinnate pages 1-2) | Evidence limitation annotation | Model-based inference |


*Table: This table condenses clinically and biologically relevant endophthalmitis facts into ontology-ready statements with suggested term mappings and evidence types. It is designed to help populate a disease knowledge base while clearly marking uncertain IDs and non-applicable Mendelian genetics fields.*

## Evidence limitations

Much of contemporary management still rests on the 1995 EVS, observational cohorts, organism-specific case series, and expert practice because randomized trials are difficult for a rare emergency. Incidence, organisms, resistance, and outcomes vary by procedure, geography, referral pattern, and prophylaxis. Recent 2024 mechanistic results are mainly murine and should not be represented as validated human biomarkers or therapies. Likewise, rare-organism case reports demonstrate biological possibility and diagnostic strategy, not frequency or comparative efficacy.

References

1. (englisch2026microbiologicaletiologyof pages 1-2): Colya N. Englisch, Tim Berger, Fabian N. Fries, Alexander Halfmann, Markus Bischoff, Philip Wakili, Annekatrin Rickmann, Boris V. Stanzel, Eugen Reifschneider, Marc A. Macek, Alaa Din Abdin, Shady Suffo, Loay Daas, Karl T. Boden, Peter Szurman, Berthold Seitz, Sören L. Becker, Clara E. Englisch, and Núria Pérez Guerra. Microbiological etiology of endogenous and exogenous postprocedural endophthalmitis: a 5-year german federal state study. Infection, 54(3):1383-1388, Mar 2026. URL: https://doi.org/10.1007/s15010-026-02763-5, doi:10.1007/s15010-026-02763-5. This article has 0 citations and is from a peer-reviewed journal.

2. (maher2026epidemiologymicrobiologymanagement pages 1-2): Clare Maher, Brad Guo, Benjamin Sim, Mark Loewenthal, Donna Gillies, and Anthony Hall. Epidemiology, microbiology, management and outcomes of endophthalmitis: an 18 year retrospective observational study at a tertiary referral center in australia. Clinical Ophthalmology, Volume 20:1-11, Feb 2026. URL: https://doi.org/10.2147/opth.s583832, doi:10.2147/opth.s583832. This article has 0 citations and is from a peer-reviewed journal.

3. (maher2026epidemiologymicrobiologymanagement pages 2-5): Clare Maher, Brad Guo, Benjamin Sim, Mark Loewenthal, Donna Gillies, and Anthony Hall. Epidemiology, microbiology, management and outcomes of endophthalmitis: an 18 year retrospective observational study at a tertiary referral center in australia. Clinical Ophthalmology, Volume 20:1-11, Feb 2026. URL: https://doi.org/10.2147/opth.s583832, doi:10.2147/opth.s583832. This article has 0 citations and is from a peer-reviewed journal.

4. (singh2024myeloidcellspecificdeletion pages 1-6): Sukhvinder Singh, Pawan Kumar Singh, Zeeshan Ahmad, Susmita Das, Marc Foretz, Benoit Viollet, Shailendra Giri, and Ashok Kumar. Myeloid cell-specific deletion of ampkα1 worsens ocular bacterial infection by skewing macrophage phenotypes. Journal of immunology, 213:1656-1665, Oct 2024. URL: https://doi.org/10.4049/jimmunol.2400282, doi:10.4049/jimmunol.2400282. This article has 3 citations and is from a domain leading peer-reviewed journal.

5. (khapuinamai2024unveilingtheinnate pages 1-2): Agimanailiu Khapuinamai, Dhanwini Rudraprasad, Suchita Pandey, Dilip Kumar Mishra, and Joveeta Joseph. Unveiling the innate and adaptive immunity interplay: global transcriptomic profiling of the host immune response in <i>candida albicans</i> endophthalmitis in a murine model. Sep 2024. URL: https://doi.org/10.1021/acsomega.4c05081, doi:10.1021/acsomega.4c05081. This article has 4 citations and is from a peer-reviewed journal.

6. (alshehri2024endogenousendophthalmitisassociated pages 1-2): Abdulaziz M Alshehri. Endogenous endophthalmitis associated with covid-19: a systematic review on its incidence, risk factors, causative organisms, and prognosis. Sep 2024. URL: https://doi.org/10.7759/cureus.70523, doi:10.7759/cureus.70523. This article has 5 citations.

7. (shah2025riskfactorsfor pages 1-2): Megh K. Shah, Aretha Zhu, Aditya Uppuluri, Roger K. Henry, Marco A. Zarbin, and Neelakshi Bhagat. Risk factors for endogenous endophthalmitis in infectious endocarditis patients. Eye, 39:125-132, Oct 2025. URL: https://doi.org/10.1038/s41433-024-03390-w, doi:10.1038/s41433-024-03390-w. This article has 5 citations and is from a peer-reviewed journal.

8. (saeed2024auniquecase pages 1-3): Ghazal Talal Saeed, Montaser Nabeeh Al Smady, Gunjan Awatramani, Hessa Alqasimi, Mohammed Amaan Khokar, Mohamed Awad, and Khadija Hafidh. A unique case of hypervirulent klebsiella pneumoniae invasive syndrome with endogenous endophthalmitis and left renal vein thrombosis without liver abscess. European Journal of Case Reports in Internal Medicine, Oct 2024. URL: https://doi.org/10.12890/2024\_004927, doi:10.12890/2024\_004927. This article has 5 citations.

9. (braga2024endogenousendophthalmitisdue pages 1-2): João Pedro Romero Braga, Victor C. F. Bellanda, Moises Moura de Lucena, Francyne Veiga Reis, and Rodrigo Jorge. Endogenous endophthalmitis due to escherichia coli: a case report. Arquivos Brasileiros de Oftalmologia, Mar 2024. URL: https://doi.org/10.5935/0004-2749.2023-0066, doi:10.5935/0004-2749.2023-0066. This article has 3 citations and is from a peer-reviewed journal.

10. (li2025clinicalretrospectiveanalysis pages 1-2): Chunhui Li, Zheyi Yan, Guohong Zhou, Yan Gao, and Peini Cheng. Clinical retrospective analysis of 218 cases of infectious endophthalmitis. BMC Ophthalmology, Jun 2025. URL: https://doi.org/10.1186/s12886-025-04142-4, doi:10.1186/s12886-025-04142-4. This article has 4 citations and is from a peer-reviewed journal.

11. (wu2024systematicinflammatoryindicators pages 1-2): Donghai Wu, Yuan Lin, Huping Wu, and Jinhong Cai. Systematic inflammatory indicators and clinical management of exogenous endophthalmitis due to metal penetrating injury of eyeball. Frontiers in Medicine, Dec 2024. URL: https://doi.org/10.3389/fmed.2024.1466530, doi:10.3389/fmed.2024.1466530. This article has 3 citations.

12. (nowosielski2026visualacuityinfluences pages 1-2): Yvonne Nowosielski, Charlotte Erlacher, Sarah Maier, Teresa Rauchegger, Alexander Franchi, and Matus Rehak. Visual acuity influences visual outcome in endophthalmitis: a 10-year retrospective observational cohort analysis. Ophthalmology and Therapy, Aug 2026. URL: https://doi.org/10.1007/s40123-026-01468-0, doi:10.1007/s40123-026-01468-0. This article has 0 citations and is from a peer-reviewed journal.

13. (krohn2024endogenousfungalendophthalmitis pages 1-2): Jørgen Krohn, Øystein A. Power, Haima Mylvaganam, Andreas J. Askim, Jarle B. Arnes, and Bjørn Blomberg. Endogenous fungal endophthalmitis caused by cladophialophora devriesii: report of a case and literature review. Journal of Ophthalmic Inflammation and Infection, Jun 2024. URL: https://doi.org/10.1186/s12348-024-00408-y, doi:10.1186/s12348-024-00408-y. This article has 1 citations and is from a peer-reviewed journal.

14. (maher2026epidemiologymicrobiologymanagement pages 8-9): Clare Maher, Brad Guo, Benjamin Sim, Mark Loewenthal, Donna Gillies, and Anthony Hall. Epidemiology, microbiology, management and outcomes of endophthalmitis: an 18 year retrospective observational study at a tertiary referral center in australia. Clinical Ophthalmology, Volume 20:1-11, Feb 2026. URL: https://doi.org/10.2147/opth.s583832, doi:10.2147/opth.s583832. This article has 0 citations and is from a peer-reviewed journal.

15. (asao2025overviewofmicroorganisms pages 26-28): Kazunobu Asao and Noriyasu Hashida. Overview of microorganisms: bacterial microbiome, mycobiome, virome identified using next-generation sequencing, and their application to ophthalmic diseases. Jun 2025. URL: https://doi.org/10.3390/microorganisms13061300, doi:10.3390/microorganisms13061300. This article has 6 citations.

16. (maher2026epidemiologymicrobiologymanagement pages 5-8): Clare Maher, Brad Guo, Benjamin Sim, Mark Loewenthal, Donna Gillies, and Anthony Hall. Epidemiology, microbiology, management and outcomes of endophthalmitis: an 18 year retrospective observational study at a tertiary referral center in australia. Clinical Ophthalmology, Volume 20:1-11, Feb 2026. URL: https://doi.org/10.2147/opth.s583832, doi:10.2147/opth.s583832. This article has 0 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Endophthalmitis-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.