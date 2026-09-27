---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-28T11:30:53.608871'
end_time: '2026-08-28T11:41:47.662726'
duration_seconds: 654.05
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Dominant Nonsyndromic Hearing Loss 7
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 28
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 3
  verified: 3
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Autosomal_Dominant_Nonsyndromic_Hearing_Loss_7-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Dominant Nonsyndromic Hearing Loss 7
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Nonsyndromic Hearing Loss 7** covering all of the
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
- **Disease Name:** Autosomal Dominant Nonsyndromic Hearing Loss 7
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Autosomal Dominant Nonsyndromic Hearing Loss 7** covering all of the
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


# Autosomal Dominant Nonsyndromic Hearing Loss 7 (DFNA7): Disease-Characteristics Report

## Executive summary

Autosomal dominant nonsyndromic hearing loss 7 (DFNA7) is a rare Mendelian sensorineural hearing-loss disorder caused by heterozygous pathogenic variants in **LMX1A**, a LIM-homeodomain transcription-factor gene at **1q23.3**. The best-supported phenotype is bilateral but frequently asymmetric sensorineural hearing loss (SNHL), with congenital through adult onset, usually a downsloping/high-frequency audiogram, variable mild-to-profound severity, and frequent progression. Vestibular dysfunction occurs in a subset and affected individuals otherwise lack a consistent syndromic phenotype. Human functional studies support **haploinsufficiency**, while mouse models establish LMX1A roles in cochlear and vestibular patterning, sensory-epithelium segregation, stria-vascularis differentiation, and generation of the endocochlear potential. No DFNA7-specific disease-modifying therapy or clinical trial was identified; present care consists of surveillance, hearing aids, cochlear implantation when indicated, vestibular management, communication support, and genetic counseling. (wesdorp2018heterozygousmissensevariants pages 8-9, wesdorp2018heterozygousmissensevariants pages 1-2, lee2020novelgenotype–phenotypecorrelation pages 2-4, jo2022geneticloadof pages 8-10)

| Domain | Key findings | Ontology suggestions | Evidence strength/type |
|---|---|---|---|
| Identity / disease class | Autosomal dominant nonsyndromic hearing loss 7 (DFNA7) is a Mendelian, nonsyndromic sensorineural hearing-loss entity associated with **LMX1A**; Open Targets lists **MONDO:0011074** for this disease-target association. Evidence is from aggregated disease resources plus small family-based human studies, not EHR-derived population datasets. (OpenTargets Search: autosomal dominant nonsyndromic hearing loss 7-LMX1A, alde2023autosomaldominantnonsyndromic pages 3-4) | MONDO:0011074; nonsyndromic hearing impairment concept | Moderate; curated disease-resource + human genetic studies |
| Locus / gene | Cytogenetic location reported as **1q23.3**; gene **LMX1A** encodes a LIM-homeobox transcription factor important for inner-ear development and maintenance. (OpenTargets Search: autosomal dominant nonsyndromic hearing loss 7-LMX1A, alde2023autosomaldominantnonsyndromic pages 3-4, lee2020novelgenotype–phenotypecorrelation pages 1-2) | Gene: LMX1A; UBERON: inner ear, cochlea, vestibular system | Strong for gene-disease association; human + model evidence |
| Inheritance | Predominantly **autosomal dominant**; several families show vertical transmission, and **de novo** heterozygous variants have also been reported. (wesdorp2018heterozygousmissensevariants pages 1-2, lee2020novelgenotype–phenotypecorrelation pages 2-4, jo2022geneticloadof pages 8-10) | HP: Autosomal dominant inheritance | Strong; human pedigree/segregation evidence |
| Core phenotype | Core presentation is **sensorineural hearing loss (SNHL)**, usually bilateral but often **asymmetric**, commonly with **downsloping/high-frequency** configuration and variable severity from mild to profound. Suggested HPO terms: hearing impairment, sensorineural hearing impairment, asymmetric hearing impairment, progressive hearing impairment, high-frequency/sloping audiogram. (wesdorp2018heterozygousmissensevariants pages 8-9, jo2022geneticloadof pages 8-10, alde2023autosomaldominantnonsyndromic pages 3-4) | HPO suggestions: sensorineural hearing impairment; progressive hearing impairment; asymmetric hearing impairment; high-frequency hearing impairment | Strong; human clinical cohorts |
| Onset / temporal course | Onset is highly variable: congenital/prelingual cases and postlingual cases are both reported; 2023 review summarizes onset from **1st–6th decade** with progressive course. In the 2018 series, onset ranged from congenital to 35 years and was often in the 2nd–3rd decade. Disease is typically lifelong, not remitting. (alde2023autosomaldominantnonsyndromic pages 3-4, wesdorp2018heterozygousmissensevariants pages 1-2, wesdorp2018heterozygousmissensevariants pages 8-9) | HPO suggestions: congenital onset; childhood onset; adult onset; progressive course | Strong; review + primary human data |
| Vestibular involvement | Vestibular dysfunction is a recurrent but variable feature: the 2018 study states **about half** of affected individuals had vestibular dysfunction/symptoms; abnormalities included absent cVEMPs and caloric abnormalities, with symptoms appearing in adulthood and seeming progressive. In the 2022 cohort, one patient had hearing fluctuation with intermittent vertigo/headache suggestive of Menière-like episodes. (wesdorp2018heterozygousmissensevariants pages 1-2, wesdorp2018heterozygousmissensevariants pages 4-6, jo2022geneticloadof pages 8-10) | HPO suggestions: vestibular dysfunction, vertigo, abnormal caloric test, absent vestibular evoked myogenic potentials | Moderate-strong; small human cohorts with formal vestibular testing |
| Key pathogenic variants | Reported heterozygous disease-associated variants include **c.290G>C (p.Cys97Ser)**, **c.721G>C (p.Val241Leu)**, **c.595A>G (p.Arg199Gly)**, **c.622C>T (p.Arg208*)**, **c.887dup (p.Gln297Thrfs*41)**, **c.719A>G (p.Gln240Arg)**, **c.721G>A (p.Val241Met)**, and **c.331del (p.Gln111Argfs*7)**. Most are ultra-rare/absent in population databases in the cited cohorts. (wesdorp2018heterozygousmissensevariants pages 1-2, lee2020novelgenotype–phenotypecorrelation pages 2-4, jo2022geneticloadof pages 4-5, jo2022geneticloadof pages 8-10, wesdorp2018heterozygousmissensevariants pages 4-6) | Variant classes: missense, nonsense, frameshift; germline heterozygous variants | Strong for listed reported variants; human molecular studies |
| Mechanism / pathophysiology | Human functional data support **haploinsufficiency** rather than dominant-negative effect for dominant LMX1A hearing loss. Reduced transcriptional activity correlates with more severe phenotype; p.Arg199Gly had near-abolished activity and severe congenital SNHL, whereas p.Cys97Ser/p.Val241Leu retained more activity and caused later progressive NSHL. Upstream/downstream developmental links from models include regulation involving **Lmo4**, **Bmp6**, **Atoh1**, **Pax2**, Wnt-related patterning, and strial differentiation markers. (lee2020novelgenotype–phenotypecorrelation pages 2-4, lee2020novelgenotype–phenotypecorrelation pages 1-2, huang2018reciprocalnegativeregulation pages 1-2, iskusnykh2026anlmx1aballelic pages 1-2, renauld2025lmx1aisessential pages 1-2, nichols2008lmx1aisrequired pages 11-12) | GO suggestions: DNA-binding transcription factor activity; inner ear development; sensory epithelium development; stria vascularis development | Strong for transcriptional dysfunction/haploinsufficiency; human in vitro + mouse developmental models |
| Anatomy / tissues / cell types | Primary anatomy: **cochlea**, **organ of Corti**, **stria vascularis**, **Reissner’s membrane**, **endolymphatic duct/sac**, vestibular organs, and spiral ganglion/cerebellar-brainstem auditory circuitry in models. Cell-type suggestions include **hair cells**, **marginal cells**, **intermediate cells**, **spiral ganglion neurons**, and non-sensory epithelial cells. Single-cell evidence identified an **Lmx1a-positive type I spiral ganglion neuron** population in mouse cochlea. (renauld2025lmx1aisessential pages 1-2, chizhikov2021lmx1aandlmx1b pages 1-2, nichols2008lmx1aisrequired pages 11-12, grandi2020singlecellrnaanalysis pages 1-2) | UBERON suggestions: cochlea, organ of Corti, stria vascularis, vestibular labyrinth; CL suggestions: hair cell, marginal cell, intermediate cell, spiral ganglion neuron; GO CC suggestions: nucleus | Moderate-strong; mostly model-organism anatomy/cell evidence |
| Diagnostics | Current diagnosis is based on audiologic phenotyping, serial follow-up for progression/asymmetry, vestibular testing when symptomatic, temporal-bone CT to exclude malformations/other causes, and molecular testing using hearing-loss gene panels or **WES** with segregation/ACMG interpretation; **WGS** is a reasonable escalation in unsolved hearing-loss cases generally, but no DFNA7-specific testing guideline was found. (wesdorp2018heterozygousmissensevariants pages 1-2, wesdorp2018heterozygousmissensevariants pages 4-6, jo2022geneticloadof pages 8-10) | HPO suggestions for workup: abnormal auditory brainstem response; abnormal vestibular testing | Moderate; disease-specific cohort methods + general hearing-loss practice inference |
| Treatment / real-world care | No DFNA7-specific drug or gene therapy was identified. Real-world management is supportive: **hearing aids** for milder/moderate disease and **cochlear implantation (CI)** for advanced loss. In the 2022 LMX1A series, one patient underwent unilateral CI with significant speech-perception improvement at 3 and 6 months post-op; the same paper notes favorable CI outcomes in LMX1A-related cases. (jo2022geneticloadof pages 8-10, jo2022geneticloadof pages 4-5) | NCIT suggestions: hearing aid device; cochlear implantation; vestibular rehabilitation; genetic counseling | Moderate; small human rehabilitation cohort |
| Epidemiology / population | Disease-specific prevalence and incidence are **not available**. Evidence comes from very small reported series: 2018 described **two Dutch families**; 2022 identified **nine patients from six LMX1A-associated families** in two tertiary centers. No robust penetrance, sex ratio, founder mutation, carrier frequency, or geographic prevalence data were found. (wesdorp2018heterozygousmissensevariants pages 1-2, jo2022geneticloadof pages 8-10) | Rare disease; familial autosomal dominant hearing loss | Limited; case-series level |
| Environmental factors / modifiers | No validated DFNA7-specific environmental risk or protective factors were identified. The 2018 study excluded obvious acquired causes of hearing loss in examined subjects, but formal gene-environment interactions remain unproven. General hearing-conservation advice is still clinically sensible but is not DFNA7-specific evidence. (wesdorp2018heterozygousmissensevariants pages 4-6, wesdorp2018heterozygousmissensevariants pages 8-9) | HPO/Exposure suggestions not disease-specific | Limited; absence-of-evidence statement |
| Model organisms | Mouse **Lmx1a** null/dreher models show severe cochlear and vestibular malformations, loss/fusion of sensory epithelia, abnormal stria vascularis formation, absent endocochlear potential, and deafness; these models are mechanistically informative but more severe than human dominant DFNA7. Heterozygous mice may have normal hearing, highlighting translational limitations. (wesdorp2018heterozygousmissensevariants pages 8-9, renauld2025lmx1aisessential pages 1-2, chizhikov2021lmx1aandlmx1b pages 1-2, nichols2008lmx1aisrequired pages 11-12) | NCBI Taxon suggestion: Mus musculus; phenotype suggestions: deafness, vestibular dysfunction | Strong for mechanism; indirect for exact human phenotype |
| Evidence gaps / curation cautions | Gaps include: original historical linkage details not fully retrieved here; no disease-specific epidemiology; no validated penetrance estimates; no confirmed modifier genes, protective factors, omics biomarkers, or epigenetic signatures; no registered DFNA7-specific interventional trial identified; and several ontology IDs beyond MONDO/HPO high-level terms would require manual validation before KB ingestion. (OpenTargets Search: autosomal dominant nonsyndromic hearing loss 7-LMX1A, jo2022geneticloadof pages 8-10, qi2026genetherapyfor pages 4-6) | Manual validation recommended for HPO/GO/CL/UBERON mappings | Strong for identified gaps because evidence is sparse/no direct studies |


*Table: This table summarizes high-yield knowledge-base facts for autosomal dominant nonsyndromic hearing loss 7 associated with LMX1A, including phenotype, mechanism, diagnostics, treatment, and evidence gaps. It is designed as a compact curation aid grounded in the available cited human and model-organism evidence.*

## 1. Disease information

### Definition and identifiers

DFNA7 is an autosomal-dominant, predominantly nonsyndromic cochleovestibular disorder associated with monoallelic **LMX1A** variants. Open Targets records the association as **MONDO:0011074**, with LMX1A/ENSG00000162761 as its associated target. The cytogenetic locus is **1q23.3**. (OpenTargets Search: autosomal dominant nonsyndromic hearing loss 7-LMX1A, alde2023autosomaldominantnonsyndromic pages 3-4)

Recommended identifiers and labels are:

- **Preferred name:** autosomal dominant nonsyndromic hearing loss 7
- **Synonyms:** DFNA7; deafness, autosomal dominant 7; LMX1A-related autosomal dominant nonsyndromic hearing loss; LMX1A-related dominant hearing impairment
- **MONDO:** MONDO:0011074
- **Gene:** LMX1A, *LIM homeobox transcription factor 1 alpha*; Ensembl ENSG00000162761
- **Gene OMIM:** LMX1A, MIM 600298
- **Broad phenotype OMIM concept:** hereditary nonsyndromic hearing impairment, MIM 500008, as used in the foundational study; a disease-specific OMIM number was not independently verified from the retrieved evidence.
- **ICD-10/ICD-11 and MeSH:** no DFNA7-specific billing or subject-heading code was established. Use the applicable broader sensorineural/genetic hearing-loss code, recording MONDO and molecular diagnosis separately.

The evidence is mainly **aggregated disease-resource information and family-level research cohorts**, not individual longitudinal EHR data. Open Targets integrates five disease-target evidence records; the primary human literature comprises small pedigrees and tertiary-center series. (OpenTargets Search: autosomal dominant nonsyndromic hearing loss 7-LMX1A, jo2022geneticloadof pages 8-10)

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal factor

The primary cause is a **germline heterozygous pathogenic or likely pathogenic LMX1A variant**. Familial vertical transmission and de novo variants are both documented. In 2018, whole-exome sequencing identified p.Val241Leu and p.Cys97Ser in two Dutch families; p.Val241Leu was de novo, while p.Cys97Ser segregated with dominant hearing loss. The latter was absent from gnomAD in that study. (PMID: **29754270**; published May 12, 2018; DOI/URL: https://doi.org/10.1007/s00439-018-1880-5). (wesdorp2018heterozygousmissensevariants pages 1-2, wesdorp2018heterozygousmissensevariants pages 4-6)

### Risk factors

- **Genetic:** carrying a pathogenic heterozygous LMX1A allele is the major risk factor. Family history is important but not required because de novo disease occurs.
- **Age:** risk of clinically detectable impairment increases with age for later-onset progressive alleles, although severe congenital presentations also occur.
- **Sex:** no reproducible sex effect is established.
- **Family history:** an affected parent implies an approximately 50% transmission probability for each pregnancy, assuming a constitutional heterozygous variant.
- **Environmental/acquired factors:** no DFNA7-specific toxin, infection, diet, smoking exposure, or occupational risk has been demonstrated.

The 2018 cohort specifically investigated acquired causes and found none sufficient to explain the familial SNHL. One patient also had fenestral otosclerosis, illustrating that genetic and acquired/concurrent disorders can coexist. (wesdorp2018heterozygousmissensevariants pages 4-6)

### Protective factors and gene–environment interaction

No protective LMX1A variants, modifier alleles, diet, medication, or lifestyle intervention has been validated. The marked intrafamilial variability led investigators to propose environmental and/or genetic modifiers, including expression of the remaining wild-type LMX1A allele, but this remains a hypothesis rather than an established interaction. Avoidance of excessive noise and ototoxic exposure is prudent hearing conservation, but it has not been shown specifically to alter DFNA7 penetrance or progression. (wesdorp2018heterozygousmissensevariants pages 8-9)

## 3. Phenotypes

### Core hearing phenotype

The principal manifestation is **sensorineural hearing impairment**, usually bilateral and often asymmetric. The overall audiogram is commonly downsloping, reflecting greater high-frequency impairment. Severity ranges from mild to profound and varies substantially within and between families. Suggested terms include **HP:0000365—hearing impairment**, **HP:0000407—sensorineural hearing impairment**, progressive hearing impairment, high-frequency hearing impairment, and asymmetric hearing impairment; exact subordinate HPO identifiers should be ontology-validated before ingestion. (wesdorp2018heterozygousmissensevariants pages 8-9, alde2023autosomaldominantnonsyndromic pages 3-4, wesdorp2018heterozygousmissensevariants pages 4-6)

A 2023 DFNA review summarized DFNA7 as congenital-to-adult onset across the first through sixth decades, with a sloping, progressive phenotype and possible vertigo. This is a synthesis rather than a disease-specific natural-history cohort (published June 2023; DOI: https://doi.org/10.3390/biomedicines11061616). (alde2023autosomaldominantnonsyndromic pages 3-4)

### Quantitative clinical evidence

In the 2022 two-center series, **nine patients from six LMX1A families** were identified. Five of nine had an interaural difference greater than 15 dB; reported mean asymmetry was **35.75 dB**, range **15–65 dB**. Three of four patients with follow-up audiometry had progressive hearing loss. Individual asymmetries in the clinical table included 18, 36, 45, and 61 dB. (PMID: **36519758**; published August 30, 2022; DOI: https://doi.org/10.3390/biomedicines10092125). (jo2022geneticloadof pages 4-5, jo2022geneticloadof pages 8-10)

The 2018 report found onset from congenital to 35 years, usually in the second or third decade, with mild-to-profound, generally downsloping and progressive impairment. Its abstract states: **“Large variability was observed in the age of onset (a)symmetry, severity and progression rate of HI.”** (wesdorp2018heterozygousmissensevariants pages 1-2, wesdorp2018heterozygousmissensevariants pages 4-6, wesdorp2018heterozygousmissensevariants pages 8-9)

### Vestibular and related manifestations

Approximately half of affected members in the 2018 study displayed vestibular dysfunction and symptoms. Absent cervical vestibular-evoked myogenic potentials up to 100 dBnHL implicated saccular dysfunction; caloric and rotary-chair abnormalities were also observed. Adult onset and greater abnormalities in older individuals suggested progression, although longitudinal vestibular data were unavailable. Suggested HPO concepts are vestibular dysfunction, vertigo, abnormal caloric response, and absent cVEMP. (wesdorp2018heterozygousmissensevariants pages 8-9, wesdorp2018heterozygousmissensevariants pages 1-2, wesdorp2018heterozygousmissensevariants pages 4-6)

One 2022 patient had fluctuating unilateral hearing, intermittent vertigo, and headache considered suggestive of coexisting Ménière disease. This should not be generalized as the canonical DFNA7 phenotype. (jo2022geneticloadof pages 8-10)

### Syndromic exclusions and quality of life

Normal cognition and absence of consistent neurologic, skeletal, pigmentation, reproductive, or cutaneous abnormalities were reported in the Dutch families. The abstract explicitly states: **“Although Lmx1a mouse mutants demonstrate neurological, skeletal, pigmentation and reproductive system abnormalities, no syndromic features were present in the participating subjects of either family.”** (wesdorp2018heterozygousmissensevariants pages 1-2)

Disease-specific EQ-5D, SF-36, PROMIS, employment, educational, or psychosocial statistics are unavailable. Expected morbidity arises from impaired speech perception, communication, localization—especially with asymmetry—and possibly balance; severity depends on onset, progression, rehabilitation, and access to communication accommodations.

## 4. Genetic and molecular information

### Causal gene and protein

**LMX1A** encodes a nuclear LIM-homeodomain transcription factor. The protein contains two cysteine-rich LIM domains that mediate protein–protein interactions and a homeodomain responsible for sequence-specific DNA binding. (lee2020novelgenotype–phenotypecorrelation pages 1-2)

### Reported dominant variants

Reported heterozygous DFNA7-associated variants include:

- **NM_177398.4:c.290G>C, p.(Cys97Ser):** missense; second LIM domain; disrupts a zinc-binding residue; segregated in a Dutch family and was absent from gnomAD in the 2018 analysis.
- **c.721G>C, p.(Val241Leu):** de novo missense; DNA-binding homeodomain.
- **c.595A>G, p.(Arg199Gly):** de novo missense; homeodomain; classified likely pathogenic in the source study; severe congenital asymmetric SNHL.
- **c.622C>T, p.(Arg208Ter):** nonsense.
- **c.887dup, p.(Gln297ThrfsTer41):** frameshift.
- **c.719A>G, p.(Gln240Arg):** missense.
- **c.721G>A, p.(Val241Met):** missense.
- **c.331del, p.(Gln111ArgfsTer7):** frameshift, reported as novel in 2022.

Most variants were absent from the population resources consulted by the reporting laboratories. Current ClinVar assertions, transcript normalization, genome build, read evidence, and gnomAD frequency should nevertheless be rechecked variant by variant before clinical reporting. All are germline; no somatic DFNA7 mechanism is known. (lee2020novelgenotype–phenotypecorrelation pages 2-4, jo2022geneticloadof pages 4-5, jo2022geneticloadof pages 8-10, wesdorp2018heterozygousmissensevariants pages 4-6)

The p.Arg199Gly case was detected after abnormal newborn screening in a three-month-old boy. Reporter assays showed near-abolished transcriptional activity and no dominant-negative effect. The abstract states: **“Further, our dominant LMX1A variant exerted pathogenic effects via haploinsufficiency rather than dominant-negative effect.”** (PMID: **32840933**; published September 2020; DOI: https://doi.org/10.1002/humu.24095). (lee2020novelgenotype–phenotypecorrelation pages 2-4, lee2020novelgenotype–phenotypecorrelation pages 1-2)

### Genotype–phenotype relationship

Residual transcriptional activity appears related to clinical severity: p.Arg199Gly produced the largest functional deficit and congenital severe-to-profound loss, whereas p.Cys97Ser and p.Val241Leu produced moderate reductions and later progressive disease. This relationship is biologically coherent but remains based on very few variants and should not be treated as a validated predictive model. (lee2020novelgenotype–phenotypecorrelation pages 2-4, lee2020novelgenotype–phenotypecorrelation pages 1-2)

### Modifiers, epigenetics, and structural variation

No validated modifier gene, methylation signature, histone alteration, or DFNA7-specific chromatin profile has been reported. A heterozygous 1q23.3–q24.1 deletion encompassing LMX1A in a separate patient supports dosage sensitivity, but large deletions may cause additional manifestations through neighboring genes. No recurrent DFNA7-specific translocation, inversion, aneuploidy, or copy-number syndrome is established. (wesdorp2018heterozygousmissensevariants pages 8-9)

## 5. Environmental and infectious information

DFNA7 is not caused by infection, radiation, pollution, diet, smoking, alcohol, or occupational exposure. No infectious trigger or zoonotic agent applies. Noise, ototoxic medication, aging, otitis, and other common causes may add independent hearing burden and should be assessed clinically, but their interaction with LMX1A has not been quantified. There are no DFNA7-specific CHEBI annotations beyond chemicals used in routine testing or treatment.

## 6. Mechanism and pathophysiology

### Human causal chain

The best-supported chain is:

**heterozygous LMX1A variant → impaired LIM-domain complex formation or homeodomain DNA binding → reduced transcriptional activity/haploinsufficiency → inadequate regulation or maintenance of cochleovestibular epithelial and neural programs → progressive dysfunction or loss of auditory/vestibular cells and ionic homeostasis → downsloping SNHL, asymmetry, and sometimes vestibular dysfunction.** (wesdorp2018heterozygousmissensevariants pages 8-9, lee2020novelgenotype–phenotypecorrelation pages 1-2)

For later-onset alleles, one normal copy appears sufficient for gross embryonic development but insufficient for lifelong cochleovestibular maintenance. For severe alleles such as p.Arg199Gly, transcriptional function may fall below a developmental threshold, producing congenital disease. The 2018 authors summarized this uncertainty directly: **“We propose that a single LMX1A wild-type copy is sufficient for normal development but insufficient for maintenance of cochleovestibular function.”** (wesdorp2018heterozygousmissensevariants pages 1-2)

### Developmental and cellular mechanisms from models

Mouse studies place Lmx1a upstream of sensory versus nonsensory epithelial segregation and vestibular/cochlear morphogenesis. Reciprocal negative regulation between Lmx1a and **Lmo4** patterns sensory cristae, semicircular canals, utricle, endolymphatic duct, and basal cochlear hair cells. Other implicated networks include Wnt/Otx patterning, Delta–Notch-related sensory segregation, and regulation of **Pax2, Fgf8, Sox2, Atoh1, Prox1, Hmx2/3**, and **Bmp6**-dependent progenitors. These are model-derived pathways, not all proven direct targets in human DFNA7. (huang2018reciprocalnegativeregulation pages 1-2, chizhikov2021lmx1aandlmx1b pages 1-2, nichols2008lmx1aisrequired pages 11-12)

Recent mechanistic work showed that Lmx1a-null mice fail to differentiate a normal stria vascularis: marginal-cell proteins **BSND** and **KCNQ1** and intermediate-cell marker **CD44** are lost, pendrin/SLC26A4 expression expands abnormally, intermediate cells disappear, and the normal approximately 80–100 mV endocochlear potential is absent. This provides a plausible downstream ionic-homeostasis mechanism, but the study was published in 2025 and used recessive-null mice rather than human heterozygous DFNA7 tissue (DOI: https://doi.org/10.3389/fcell.2025.1537505). (renauld2025lmx1aisessential pages 1-2)

Suggested GO concepts include DNA-binding transcription-factor activity, transcriptional regulation, inner-ear development, sensory-organ morphogenesis, auditory-receptor-cell development, sensory-epithelium development, cell-fate specification, ion homeostasis, stria-vascularis development, and maintenance of sensory cells. The principal subcellular compartment is the **nucleus**.

### Molecular profiling and advanced technologies

Single-cell qPCR in mouse cochlea identified an **Lmx1a-positive type-I spiral ganglion neuron** population at postnatal days P3, P8, and P12, distinct from Slc4a4- and Mfap4/Fzd2-marked populations. This suggests early molecular specification of auditory-afferent subtypes, but it does not establish that these neurons are the primary lesion in human DFNA7 (DOI: https://doi.org/10.3389/fnmol.2020.00083). (grandi2020singlecellrnaanalysis pages 1-2)

No DFNA7 patient-tissue transcriptome, proteome, metabolome, lipidome, spatial-transcriptomic atlas, CRISPR screen, or integrated patient multi-omics signature was found. There is no established immune, inflammatory, fibrotic, ischemic, or metabolic component.

## 7. Anatomical structures affected

The principal organ is the **inner ear**. Relevant sites are the cochlea and organ of Corti, cochlear sensory and nonsensory epithelia, stria vascularis, Reissner membrane, endolymphatic duct and sac, semicircular canals, utricle, saccule, and spiral ganglion. Human CT generally showed no major cochleovestibular malformation in later-onset heterozygous disease. (wesdorp2018heterozygousmissensevariants pages 1-2, renauld2025lmx1aisessential pages 1-2, nichols2008lmx1aisrequired pages 11-12)

Suggested mappings are:

- **UBERON:** inner ear, cochlea, organ of Corti, stria vascularis, vestibular labyrinth, saccule, utricle, semicircular canal, spiral ganglion.
- **CL:** inner/outer hair cell, sensory epithelial cell, nonsensory epithelial cell, strial marginal cell, strial intermediate cell/melanocyte-lineage cell, spiral ganglion neuron.
- **GO cellular component:** nucleus and transcription-factor complex.

Hearing loss is usually bilateral but can be markedly asymmetric. Major secondary-organ involvement is not expected in human DFNA7.

## 8. Temporal development

Onset ranges from congenital/prelingual disease to childhood, adolescence, or adulthood. The 2023 review gives a first-to-sixth-decade range. Course is chronic and commonly progressive rather than episodic or remitting, although fluctuation was reported in one patient with possible coexisting Ménière disease. (jo2022geneticloadof pages 4-5, jo2022geneticloadof pages 8-10, alde2023autosomaldominantnonsyndromic pages 3-4)

Practical stages are not formally standardized but can be represented as: early high-frequency or asymmetric loss; broader-frequency moderate/severe loss with reduced speech perception; and advanced severe-to-profound loss potentially requiring cochlear implantation. Critical intervention windows include early childhood for congenital disease and any period when serial audiometry documents declining aided speech access. No spontaneous remission has been demonstrated.

## 9. Inheritance and population

Inheritance is autosomal dominant, with de novo disease recognized. Penetrance is likely age- and allele-dependent but has not been measured robustly. Expressivity is clearly variable in onset, symmetry, progression, vestibular involvement, and severity. Anticipation, germline mosaicism, founder effects, consanguinity effects, and carrier frequency have not been established. Consanguinity is not expected to be a major factor in dominant DFNA7, although biallelic LMX1A disease is a separate severe recessive phenotype. (wesdorp2018heterozygousmissensevariants pages 1-2, lee2020novelgenotype–phenotypecorrelation pages 2-4)

No population prevalence, incidence, sex ratio, or reliable ethnic/geographic enrichment is available. Published cases include Dutch and Korean clinical cohorts, but these ascertainment locations do not prove population enrichment. The two-center 2022 study found nine LMX1A patients from six families among a broader molecularly tested referral cohort; this is not a population-prevalence estimate. (jo2022geneticloadof pages 8-10)

## 10. Diagnostics

### Clinical evaluation

Recommended assessment comprises history of onset and progression; three-generation pedigree; otoscopy; pure-tone air/bone audiometry; speech audiometry; tympanometry; otoacoustic emissions and auditory brainstem response when age or reliability warrants; and serial testing of each ear because asymmetry and progression are common. Vestibular history and examination should be followed by vHIT, caloric/rotary-chair testing, and cVEMP when imbalance or vertigo is present. Temporal-bone CT or MRI is used selectively to evaluate marked asymmetry, cochlear-implant anatomy, or alternative pathology, not as a molecular diagnostic test. (wesdorp2018heterozygousmissensevariants pages 1-2, wesdorp2018heterozygousmissensevariants pages 4-6)

There is no blood chemistry, metabolite, circulating protein, biopsy, or histopathologic biomarker for DFNA7.

### Genetic testing strategy

1. Use a comprehensive hereditary-hearing-loss panel that includes **LMX1A**, with copy-number analysis and adequate coverage of relevant exons/splice regions.
2. If negative or the presentation is atypical, use trio/family WES and segregation analysis; WES identified the founding dominant variants.
3. Escalate unresolved cases to WGS to detect cryptic splice, regulatory, mitochondrial, and structural variants, although this is general hearing-loss practice rather than DFNA7-specific evidence.
4. Confirm reportable variants by an orthogonal method when appropriate, review ClinVar/gnomAD, and apply current ACMG/AMP criteria with phenotype and segregation evidence.

Single-gene LMX1A sequencing is reasonable when the phenotype and family variant are known. CMA may detect a deletion encompassing LMX1A but is lower yield for sequence variants. Routine karyotype, FISH, mitochondrial testing, and repeat-expansion testing are not indicated unless another diagnosis is suspected. RNA studies can clarify suspected splice variants but are not routine DFNA7 diagnostics.

### Differential diagnosis and screening

Differentials include other dominant nonsyndromic hearing-loss genes—especially **KCNQ4, TECTA, WFS1, POU4F3, EYA4, ACTG1, MYO6, COCH**, and MYO7A—as well as age/noise-related loss, congenital CMV, ototoxicity, Ménière disease, otosclerosis, and syndromic conditions initially presenting with isolated hearing loss. The combination of frequent asymmetry, progression, occasional vestibular dysfunction, and LMX1A variant is suggestive but not diagnostic by phenotype alone.

Universal newborn hearing screening can detect congenital severe alleles but will miss later-onset DFNA7. Once a familial pathogenic variant is established, offer cascade testing and baseline/serial audiometry to at-risk relatives, including those currently asymptomatic.

## 11. Outcome and prognosis

DFNA7 is not known to reduce survival or life expectancy, and disease-specific mortality is not reported. Morbidity is auditory and sometimes vestibular. Hearing may progress to severe or profound levels, but rate and final severity are allele- and person-dependent. Major prognostic features are age at onset, baseline thresholds, progression, asymmetry, speech discrimination, vestibular involvement, and access to timely amplification or implantation. No validated molecular prognostic biomarker exists beyond preliminary variant-function correlations. (lee2020novelgenotype–phenotypecorrelation pages 2-4, jo2022geneticloadof pages 8-10)

Spontaneous recovery is not expected. Functional outcomes can improve substantially with rehabilitation. In the 2022 series, one patient whose left ear progressed to profound loss underwent unilateral cochlear implantation and had significant speech-perception improvement at three and six months. (jo2022geneticloadof pages 8-10)

## 12. Treatment and applications

### Current standard care

- **Hearing aids:** first-line for aidable mild-to-severe loss; fit each ear according to thresholds and speech needs.
- **Cochlear implantation:** consider for severe-to-profound loss with inadequate aided speech recognition. The available LMX1A evidence is favorable but limited to very small numbers.
- **Vestibular care:** vestibular rehabilitation and disorder-specific management when objective dysfunction or imbalance is present.
- **Communication/rehabilitation:** speech-language therapy where needed, assistive listening devices, classroom/workplace accommodations, captioning, and sign-language access according to patient preference.
- **Surveillance:** long-term audiometry is important because progression and interaural divergence may alter device candidacy.

Suggested NCIT concepts are Hearing Aid, Cochlear Implantation, Audiologic Rehabilitation, Vestibular Rehabilitation, Speech Therapy, and Genetic Counseling; exact NCIT identifiers should be validated before database loading. (jo2022geneticloadof pages 8-10, alde2023autosomaldominantnonsyndromic pages 3-4)

### Pharmacologic and advanced therapies

No drug, pharmacogenomic algorithm, surgery that corrects LMX1A dysfunction, cell therapy, ASO, siRNA, CRISPR treatment, or LMX1A gene therapy is approved or clinically validated. A search specifically for DFNA7/LMX1A trials found no relevant registered interventional study. The widely publicized 2024 hereditary-deafness gene-therapy advances concern **biallelic OTOF/DFNB9**, including seven reported trials, not dominant LMX1A disease; these results should not be extrapolated to DFNA7. (qi2026genetherapyfor pages 4-6)

For dominant haploinsufficiency, future strategies might include allele-agnostic augmentation or enhancement of residual LMX1A function, but developmental expression, nuclear transcriptional targeting, dosage control, delivery to multiple cochleovestibular cell types, and an uncertain treatment window remain substantial barriers.

## 13. Prevention

Primary prevention of a de novo or inherited pathogenic allele is not possible through lifestyle or vaccination. Reproductive options after identifying the family variant include genetic counseling, prenatal diagnosis, and preimplantation genetic testing, governed by patient values and local regulation. Predictive testing of minors can be clinically actionable because surveillance and hearing intervention are beneficial.

Secondary prevention consists of cascade testing, baseline audiology, serial monitoring, and prompt amplification or implantation. Tertiary prevention includes hearing conservation, avoidance of unnecessary ototoxic exposure, management of vestibular fall risk, and communication rehabilitation. These measures prevent additional disability rather than the underlying genotype. No vaccine or chemoprophylaxis applies.

## 14. Other species and natural disease

The principal comparative species is **Mus musculus** (NCBI Taxonomy 10090), with ortholog **Lmx1a**. Naturally occurring and induced mouse alleles include dreher, mutanlallemand, and belly-spot-and-deafness. Homozygous animals are deaf and display vestibular behaviors such as circling and head tossing, with absent endolymphatic ducts/semicircular canals, shortened cochlear ducts, sensory-patch abnormalities, and truncated Lmx1a protein. (DOI: https://doi.org/10.1371/journal.pone.0051065). (huang2018reciprocalnegativeregulation pages 1-2, nichols2008lmx1aisrequired pages 11-12)

These are hereditary laboratory-animal phenotypes, not a recognized contagious veterinary disease; breed-specific natural disease, VBO terms, zoonotic transmission, and cross-species infection are not applicable. Conservation of Lmx1-family auditory-development functions supports comparative utility, but species differ in dosage sensitivity.

## 15. Model organisms

### Mouse genetic models

Recessive-null/dreher, spontaneous splice/deletion alleles, and conditional knockouts model Lmx1a loss. They reproduce deafness and vestibular dysfunction and reveal developmental abnormalities in the cochlea, vestibular labyrinth, stria vascularis, and central auditory structures. Relevant applications include studying sensory-epithelial segregation, ion homeostasis, hair-cell maintenance, vestibular morphogenesis, and interactions with Lmx1b/Lmo4/Wnt/BMP programs. (huang2018reciprocalnegativeregulation pages 1-2, renauld2025lmx1aisessential pages 1-2, chizhikov2021lmx1aandlmx1b pages 1-2, nichols2008lmx1aisrequired pages 11-12)

The major limitation is severity and inheritance mismatch: homozygous mouse nulls have profound multisystem developmental abnormalities, whereas human DFNA7 is heterozygous and usually nonsyndromic. Heterozygous mice had normal hearing through approximately three to four months in cited observations. Therefore, null-mouse anatomy supports biological plausibility but does not fully model human penetrance, progression, or asymmetry. (wesdorp2018heterozygousmissensevariants pages 8-9)

### Cellular and in-vitro models

HEK293T luciferase assays quantify variant-specific LMX1A transcriptional activity and support haploinsufficiency and preliminary genotype–phenotype correlation. They cannot reproduce cochlear architecture, mechanical transduction, or long-term sensory-cell maintenance. Patient-derived iPSC inner-ear organoids, precise heterozygous knock-in animals, and longitudinal single-cell/spatial profiling would be higher-fidelity future models. (lee2020novelgenotype–phenotypecorrelation pages 2-4, lee2020novelgenotype–phenotypecorrelation pages 1-2)

## Recent research and expert interpretation

The most important recent synthesis is the 2023 DFNA review, which places DFNA7 among more than 80 dominant hearing-loss loci and emphasizes long-term audiological follow-up to detect deterioration and trigger hearing-aid or cochlear-implant intervention. For DFNA7 specifically, however, the decisive human evidence remains the 2018 gene-discovery cohort, 2020 functional genotype–phenotype study, and 2022 tertiary-center series. (jo2022geneticloadof pages 8-10, alde2023autosomaldominantnonsyndromic pages 3-4)

A 2024 structural study of LMX1A homeodomain recognition of A/T-rich promoter motifs advances basic understanding of DNA binding but does not yet alter diagnosis or treatment (DOI: https://doi.org/10.1111/febs.17118). The latest mechanistic extension, published in 2025, identifies Lmx1a as essential for strial marginal-cell differentiation and endocochlear-potential generation in mice. Together these results strengthen a dual developmental-and-maintenance model but do not yet provide a therapeutic target validated in human DFNA7 tissue. (renauld2025lmx1aisessential pages 1-2)

## Evidence limitations and curation cautions

DFNA7 evidence remains case-series level: no registry-scale natural-history study, prevalence estimate, prospective penetrance study, randomized treatment trial, patient-derived omics dataset, or validated environmental modifier exists. Several variants reported in research cohorts require current ClinVar and ACMG reassessment before clinical use. Mouse recessive-null findings must be labeled as **model-organism evidence**, and general hearing-loss recommendations must not be represented as DFNA7-specific efficacy data. The strongest directly supported knowledge-base assertions are the LMX1A association, autosomal-dominant/de novo inheritance, variable progressive SNHL with frequent asymmetry, occasional vestibular dysfunction, and haploinsufficiency mechanism. (OpenTargets Search: autosomal dominant nonsyndromic hearing loss 7-LMX1A, wesdorp2018heterozygousmissensevariants pages 1-2, lee2020novelgenotype–phenotypecorrelation pages 2-4, jo2022geneticloadof pages 8-10)

References

1. (wesdorp2018heterozygousmissensevariants pages 8-9): Mieke Wesdorp, P. A. M. de Koning Gans, M. Schraders, J. Oostrik, M. Huynen, H. Venselaar, A. Beynon, J. van Gaalen, Vitória Piai, N. Voermans, M. V. van Rossum, B. Hartel, Stefan H. Lelieveld, L. Wiel, B. Verbist, L. Rotteveel, M. V. van Dooren, P. Lichtner, H. Kunst, I. Feenstra, R. Admiraal, M. F. H. H. W. E. H. M. P. S. G. L. J. C. S. G. M. J. van Dooren de Gier Hoefsloot van der Schroeff Kant, M. V. van Dooren, H. D. de Gier, E. H. Hoefsloot, M. P. van der Schroeff, S. Kant, L. Rotteveel, S. Frints, J. Hof, R. Stokroos, E. Vanhoutte, R. Admiraal, I. Feenstra, H. Kremer, H. Kunst, R. Pennings, H. Yntema, A. V. van Essen, R. Free, J. S. Klein-Wassink, H. Yntema, L. Hoefsloot, R. Pennings, and H. Kremer. Heterozygous missense variants of lmx1a lead to nonsyndromic hearing impairment and vestibular dysfunction. Human Genetics, 137:389-400, May 2018. URL: https://doi.org/10.1007/s00439-018-1880-5, doi:10.1007/s00439-018-1880-5. This article has 43 citations and is from a peer-reviewed journal.

2. (wesdorp2018heterozygousmissensevariants pages 1-2): Mieke Wesdorp, P. A. M. de Koning Gans, M. Schraders, J. Oostrik, M. Huynen, H. Venselaar, A. Beynon, J. van Gaalen, Vitória Piai, N. Voermans, M. V. van Rossum, B. Hartel, Stefan H. Lelieveld, L. Wiel, B. Verbist, L. Rotteveel, M. V. van Dooren, P. Lichtner, H. Kunst, I. Feenstra, R. Admiraal, M. F. H. H. W. E. H. M. P. S. G. L. J. C. S. G. M. J. van Dooren de Gier Hoefsloot van der Schroeff Kant, M. V. van Dooren, H. D. de Gier, E. H. Hoefsloot, M. P. van der Schroeff, S. Kant, L. Rotteveel, S. Frints, J. Hof, R. Stokroos, E. Vanhoutte, R. Admiraal, I. Feenstra, H. Kremer, H. Kunst, R. Pennings, H. Yntema, A. V. van Essen, R. Free, J. S. Klein-Wassink, H. Yntema, L. Hoefsloot, R. Pennings, and H. Kremer. Heterozygous missense variants of lmx1a lead to nonsyndromic hearing impairment and vestibular dysfunction. Human Genetics, 137:389-400, May 2018. URL: https://doi.org/10.1007/s00439-018-1880-5, doi:10.1007/s00439-018-1880-5. This article has 43 citations and is from a peer-reviewed journal.

3. (lee2020novelgenotype–phenotypecorrelation pages 2-4): Sang‐Yeon Lee, Jin Hee Han, Marge Carandang, Min Young Kim, Bonggi Kim, Nayoung Yi, Jinho Kim, Bong Jik Kim, Doo‐Yi Oh, Ja‐Won Koo, Jun Ho Lee, Seung‐Ha Oh, and Byung Yoon Choi. Novel genotype–phenotype correlation of functionally characterized <i>lmx1a</i> variants linked to sensorineural hearing loss. Sep 2020. URL: https://doi.org/10.1002/humu.24095, doi:10.1002/humu.24095. This article has 23 citations and is from a domain leading peer-reviewed journal.

4. (jo2022geneticloadof pages 8-10): Hyung Dong Jo, Jin Hee Han, So Min Lee, Dong Hwa Choi, Sang-Yeon Lee, and Byung Yoon Choi. Genetic load of alternations of transcription factor genes in non-syndromic deafness and the associated clinical phenotypes: experience from two tertiary referral centers. Biomedicines, 10(9):2125, Aug 2022. URL: https://doi.org/10.3390/biomedicines10092125, doi:10.3390/biomedicines10092125. This article has 11 citations.

5. (OpenTargets Search: autosomal dominant nonsyndromic hearing loss 7-LMX1A): Open Targets Query (autosomal dominant nonsyndromic hearing loss 7-LMX1A, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (alde2023autosomaldominantnonsyndromic pages 3-4): Mirko Aldè, Giovanna Cantarella, Diego Zanetti, Lorenzo Pignataro, Ignazio La Mantia, Luigi Maiolino, Salvatore Ferlito, Paola Di Mauro, Salvatore Cocuzza, Jérôme René Lechien, Giannicola Iannella, Francois Simon, and Antonino Maniaci. Autosomal dominant non-syndromic hearing loss (dfna): a comprehensive narrative review. Biomedicines, 11:1616, Jun 2023. URL: https://doi.org/10.3390/biomedicines11061616, doi:10.3390/biomedicines11061616. This article has 65 citations.

7. (lee2020novelgenotype–phenotypecorrelation pages 1-2): Sang‐Yeon Lee, Jin Hee Han, Marge Carandang, Min Young Kim, Bonggi Kim, Nayoung Yi, Jinho Kim, Bong Jik Kim, Doo‐Yi Oh, Ja‐Won Koo, Jun Ho Lee, Seung‐Ha Oh, and Byung Yoon Choi. Novel genotype–phenotype correlation of functionally characterized <i>lmx1a</i> variants linked to sensorineural hearing loss. Sep 2020. URL: https://doi.org/10.1002/humu.24095, doi:10.1002/humu.24095. This article has 23 citations and is from a domain leading peer-reviewed journal.

8. (wesdorp2018heterozygousmissensevariants pages 4-6): Mieke Wesdorp, P. A. M. de Koning Gans, M. Schraders, J. Oostrik, M. Huynen, H. Venselaar, A. Beynon, J. van Gaalen, Vitória Piai, N. Voermans, M. V. van Rossum, B. Hartel, Stefan H. Lelieveld, L. Wiel, B. Verbist, L. Rotteveel, M. V. van Dooren, P. Lichtner, H. Kunst, I. Feenstra, R. Admiraal, M. F. H. H. W. E. H. M. P. S. G. L. J. C. S. G. M. J. van Dooren de Gier Hoefsloot van der Schroeff Kant, M. V. van Dooren, H. D. de Gier, E. H. Hoefsloot, M. P. van der Schroeff, S. Kant, L. Rotteveel, S. Frints, J. Hof, R. Stokroos, E. Vanhoutte, R. Admiraal, I. Feenstra, H. Kremer, H. Kunst, R. Pennings, H. Yntema, A. V. van Essen, R. Free, J. S. Klein-Wassink, H. Yntema, L. Hoefsloot, R. Pennings, and H. Kremer. Heterozygous missense variants of lmx1a lead to nonsyndromic hearing impairment and vestibular dysfunction. Human Genetics, 137:389-400, May 2018. URL: https://doi.org/10.1007/s00439-018-1880-5, doi:10.1007/s00439-018-1880-5. This article has 43 citations and is from a peer-reviewed journal.

9. (jo2022geneticloadof pages 4-5): Hyung Dong Jo, Jin Hee Han, So Min Lee, Dong Hwa Choi, Sang-Yeon Lee, and Byung Yoon Choi. Genetic load of alternations of transcription factor genes in non-syndromic deafness and the associated clinical phenotypes: experience from two tertiary referral centers. Biomedicines, 10(9):2125, Aug 2022. URL: https://doi.org/10.3390/biomedicines10092125, doi:10.3390/biomedicines10092125. This article has 11 citations.

10. (huang2018reciprocalnegativeregulation pages 1-2): Yanhan Huang, Jennifer Hill, Andrew Yatteau, Loksum Wong, Tao Jiang, Jelena Petrovic, Lin Gan, Lijin Dong, and Doris K. Wu. Reciprocal negative regulation between lmx1a and lmo4 is required for inner ear formation. The Journal of Neuroscience, 38:5429-5440, Jun 2018. URL: https://doi.org/10.1523/jneurosci.2484-17.2018, doi:10.1523/jneurosci.2484-17.2018. This article has 23 citations.

11. (iskusnykh2026anlmx1aballelic pages 1-2): Igor Y. Iskusnykh, Bernd Fritzsch, Ebenezer N. Yamoah, Ekaterina Y. Steshina, and Victor V. Chizhikov. An lmx1a/b allelic series reveals the role of lmx1 genes in cochlear nuclei development. Cell and Tissue Research, Apr 2026. URL: https://doi.org/10.1007/s00441-026-04064-7, doi:10.1007/s00441-026-04064-7. This article has 1 citations and is from a peer-reviewed journal.

12. (renauld2025lmx1aisessential pages 1-2): Justine M. Renauld, Igor Y. Iskusnykh, Ebenezer N. Yamoah, Richard J. H. Smith, Corentin Affortit, David Z. He, Huizhan Liu, David Nichols, Judith Bouma, Mahesh K. Nayak, Xin Weng, Tianli Qin, Mai Har Sham, Victor V. Chizhikov, and Bernd Fritzsch. Lmx1a is essential for marginal cell differentiation and stria vascularis formation. Frontiers in Cell and Developmental Biology, Mar 2025. URL: https://doi.org/10.3389/fcell.2025.1537505, doi:10.3389/fcell.2025.1537505. This article has 9 citations.

13. (nichols2008lmx1aisrequired pages 11-12): David H. Nichols, Sarah Pauley, Israt Jahan, Kirk W. Beisel, Kathleen J. Millen, and Bernd Fritzsch. Lmx1a is required for segregation of sensory epithelia and normal ear histogenesis and morphogenesis. Cell and Tissue Research, 334:339-358, Nov 2008. URL: https://doi.org/10.1007/s00441-008-0709-2, doi:10.1007/s00441-008-0709-2. This article has 155 citations and is from a peer-reviewed journal.

14. (chizhikov2021lmx1aandlmx1b pages 1-2): Victor V. Chizhikov, Igor Y. Iskusnykh, Nikolai Fattakhov, and Bernd Fritzsch. Lmx1a and lmx1b are redundantly required for the development of multiple components of the mammalian auditory system. Jan 2021. URL: https://doi.org/10.1016/j.neuroscience.2020.11.013, doi:10.1016/j.neuroscience.2020.11.013. This article has 57 citations and is from a domain leading peer-reviewed journal.

15. (grandi2020singlecellrnaanalysis pages 1-2): Fiorella Carla Grandi, Lara De Tomasi, and Mirna Mustapha. Single-cell rna analysis of type i spiral ganglion neurons reveals a lmx1a population in the cochlea. Frontiers in Molecular Neuroscience, May 2020. URL: https://doi.org/10.3389/fnmol.2020.00083, doi:10.3389/fnmol.2020.00083. This article has 32 citations.

16. (qi2026genetherapyfor pages 4-6): Yu Qi, Fangzhi Tan, Maoli Duan, and Ling Lu. Gene therapy for non-syndromic hearing loss. Head and Neck Diseases Conflux, 2(1):e345, Mar 2026. URL: https://doi.org/10.71321/703b4949, doi:10.71321/703b4949. This article has 0 citations.

## Artifacts

- [Edison artifact artifact-00](Autosomal_Dominant_Nonsyndromic_Hearing_Loss_7-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 3 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |

Every term resolved, and every label the report gave matched.