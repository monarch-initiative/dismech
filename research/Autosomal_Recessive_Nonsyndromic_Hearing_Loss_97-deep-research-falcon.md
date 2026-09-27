---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-28T19:01:28.256571'
end_time: '2026-08-28T19:11:28.646658'
duration_seconds: 600.39
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Recessive Nonsyndromic Hearing Loss 97 (DFNB97, MET-related)
  mondo_id: MONDO:0014739
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 18
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 6
  validator_version: 0.2.1
term_validation:
  total_terms: 6
  verified: 6
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0014739
    reported_labels:
    - if available
    ontology_label: autosomal recessive nonsyndromic hearing loss 97
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Autosomal_Recessive_Nonsyndromic_Hearing_Loss_97-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Recessive Nonsyndromic Hearing Loss 97 (DFNB97, MET-related)
- **MONDO ID:** MONDO:0014739 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Nonsyndromic Hearing Loss 97 (DFNB97, MET-related)** covering all of the
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
- **Disease Name:** Autosomal Recessive Nonsyndromic Hearing Loss 97 (DFNB97, MET-related)
- **MONDO ID:** MONDO:0014739 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Nonsyndromic Hearing Loss 97 (DFNB97, MET-related)** covering all of the
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


# Autosomal Recessive Nonsyndromic Hearing Loss 97 (DFNB97; MET-related)

## Executive summary

DFNB97 is an **ultra-rare, autosomal-recessive, nonsyndromic sensorineural hearing loss** caused by biallelic variants in **MET**, which encodes the hepatocyte growth factor receptor, a receptor tyrosine kinase. The direct human evidence remains small: a large Pakistani pedigree containing nine affected people and a Moroccan family with one affected child. The characteristic presentation is bilateral, prelingual or early-childhood, severe-to-profound sensorineural hearing loss without established vestibular, structural inner-ear, or systemic abnormalities. The best-supported pathogenic model is impaired HGF–MET signaling during cochlear development, particularly defective incorporation or function of neural-crest-derived intermediate cells in the stria vascularis, followed by failure to maintain the endocochlear electrochemical environment required for hair-cell transduction. However, that chain is partly extrapolated from HGF and conditional animal models; no patient-variant knock-in model or patient-derived cochlear tissue has yet demonstrated it directly. (mujtaba2015amutationof pages 1-3, bousfiha2020furtherevidencefor pages 1-2, naz2020growthfactorand pages 7-8)

No MET-specific drug, gene therapy, validated biomarker, natural-history cohort, or DFNB97 clinical trial was identified. Current care therefore follows standard pediatric sensorineural-hearing-loss practice: early audiologic confirmation, hearing technology or cochlear implantation as appropriate, speech/language habilitation, educational support, and genetic counseling. A 2024 review records rapid progress in gene therapy for other hereditary deafness genes—especially **OTOF/DFNB9**—but this should not be represented as a treatment for DFNB97. (bousfiha2020furtherevidencefor pages 2-2, zhang2024aav‐mediatedgenetherapy pages 1-2)

| Domain | Established finding | Evidence level/source | Suggested ontology identifiers/terms | Key caveat |
|---|---|---|---|---|
| Disease identity | Autosomal recessive nonsyndromic hearing loss 97 (DFNB97) is a rare genetic form of bilateral sensorineural hearing loss linked to biallelic MET variants; MONDO association is available as MONDO:0014739. (OpenTargets Search: autosomal recessive nonsyndromic hearing loss 97-MET, mujtaba2015amutationof pages 1-3, bousfiha2020furtherevidencefor pages 1-2) | Disease database association plus primary human family reports | MONDO:0014739; term: autosomal recessive nonsyndromic hearing loss 97; term: nonsyndromic hearing loss | Disease-level prevalence and natural-history data remain sparse. |
| Causal gene/protein | Causal gene: MET (ENSG00000105976), encoding MET proto-oncogene, receptor tyrosine kinase / hepatocyte growth factor receptor (HGFR). (OpenTargets Search: autosomal recessive nonsyndromic hearing loss 97-MET, mujtaba2015amutationof pages 1-3, bousfiha2020furtherevidencefor pages 1-2) | Primary human genetics; curated disease-target association | ENSG00000105976; term: MET proto-oncogene, receptor tyrosine kinase; term: hepatocyte growth factor receptor | HGNC/NCBI Gene/UniProt IDs should be verified separately if needed. |
| Inheritance | Inheritance is autosomal recessive; reported cases occurred in consanguineous families with homozygous missense variants and unaffected heterozygous relatives. (mujtaba2015amutationof pages 1-3, bousfiha2020furtherevidencefor pages 1-2, bousfiha2020furtherevidencefor pages 2-2) | Primary human pedigree/segregation evidence | HPO term label: Autosomal recessive inheritance (ID verification required) | Penetrance cannot be estimated robustly from two reported families. |
| Human family 1 / variant | Pakistani family HLGM17: 9 affected individuals, severe sensorineural hearing loss, homozygous MET c.2521T>G, p.(Phe841Val) / p.F841V; mapped to 7q31.2 with maximum LOD 4.8. (mujtaba2015amutationof pages 1-3, mujtaba2015amutationof pages 3-4, mujtaba2015amutationof pages 8-10) | Strong primary human linkage + exome + segregation | term: MET c.2521T>G; term: p.Phe841Val; term: chromosome 7q31.2; HPO term label: Sensorineural hearing impairment | Transcript/isoform numbering should be normalized before KB ingestion. |
| Human family 2 / variant | Moroccan family SF190: one affected girl with total bilateral nonsyndromic hearing impairment; homozygous MET c.948A>G, p.(Ile316Met); heterozygous parents and brother had normal hearing. (bousfiha2020furtherevidencefor pages 1-2, bousfiha2020furtherevidencefor pages 2-4, bousfiha2020furtherevidencefor pages 2-2) | Primary human exome + segregation evidence | term: MET c.948A>G; term: p.Ile316Met; HPO term label: Bilateral hearing impairment | Single-patient family report; broader phenotypic spectrum unknown. |
| Core phenotype | Reported phenotype is early-onset/prelingual, bilateral, nonsyndromic sensorineural hearing loss, severe to profound, with speech delay and intrafamilial threshold variability. Vestibular bedside testing was normal in the Pakistani family. (mujtaba2015amutationof pages 1-3, mujtaba2015amutationof pages 3-4, bousfiha2020furtherevidencefor pages 2-2) | Primary human clinical/audiometric evidence | HPO term labels: Sensorineural hearing impairment; Severe hearing impairment; Profound hearing impairment; Prelingual hearing impairment; Delayed speech and language development; Bilateral hearing impairment | Percent frequencies for individual phenotypes are unavailable beyond the reported families. |
| Onset/course | Pakistani family: hearing loss noted at or before age 2 years; Moroccan case diagnosed in early childhood by BAEP/ABR. Available reports support congenital/early-childhood onset and lifelong course. (mujtaba2015amutationof pages 1-3, bousfiha2020furtherevidencefor pages 2-2) | Primary human case evidence | HPO term labels: Congenital or childhood onset hearing impairment (ID verification required) | Progression is not well defined specifically for DFNB97. |
| Syndromic exclusion | Reported DFNB97 cases lacked obvious extra-auditory disease; Pakistani cases had normal liver/kidney/heart history and normal selected laboratory/ophthalmic assessments; Moroccan imaging showed no inner-ear or cochleovestibular nerve malformation. (mujtaba2015amutationof pages 1-3, bousfiha2020furtherevidencefor pages 2-2) | Primary human clinical evaluation | term: nonsyndromic hearing loss; term: normal inner ear imaging | Small numbers do not exclude subtle or age-dependent extra-auditory manifestations. |
| Anatomy/organs | Primary affected organ is the inner ear, especially the cochlea; broader pathway evidence implicates the stria vascularis in maintaining endocochlear potential needed for sound transduction. (naz2020growthfactorand pages 7-8, shadab2024autosomalrecessivenon‐syndromic pages 8-9, zhang2024aav‐mediatedgenetherapy pages 1-2) | Mechanistic synthesis from pathway/review and model evidence | UBERON term labels: inner ear; cochlea; stria vascularis | Direct human histopathology for DFNB97 is not available. |
| Cell types | Most implicated cell populations are strial intermediate cells (neural crest-derived melanocyte-like cells) and possibly other cochlear nonsensory cells; MET/HGF expression has also been described in spiral ganglion cells and hair cells in embryonic rat cochlea. (bousfiha2020furtherevidencefor pages 5-6, naz2020growthfactorand pages 7-8) | Indirect model/expression evidence | CL term labels: intermediate cell of stria vascularis; melanocyte; hair cell; spiral ganglion neuron | Exact causally affected human cell type in DFNB97 remains inferred, not proven. |
| Molecular mechanism | Best-supported mechanism: deleterious MET variants impair HGF-MET receptor function. The IPT3/IPT4 region forms a high-affinity HGF-binding surface, while the SEMA domain is important for dimerization/activation; altered signaling is predicted to disrupt development of neural crest-derived intermediate cells in the stria vascularis, reducing endocochlear potential and causing hearing loss. (bousfiha2020furtherevidencefor pages 5-6, mujtaba2015amutationof pages 4-6, naz2020growthfactorand pages 7-8, shadab2024autosomalrecessivenon‐syndromic pages 8-9) | Variant/domain interpretation plus pathway/model inference | GO term labels: receptor tyrosine kinase signaling; epithelial to mesenchymal transition; neural crest cell migration; inner ear development; potassium ion homeostasis (ID verification required) | No variant-specific functional assay directly demonstrated loss of MET signaling in patient tissue. |
| Variant functional evidence | p.Phe841Val: conserved residue, predicted damaging by multiple tools, possible splicing effect in exon-trap assay, absent from large control/public datasets in 2015 study. p.Ile316Met: conserved residue, in silico pathogenicity support and molecular dynamics predicted loss of flexibility affecting receptor conformation/binding site. (mujtaba2015amutationof pages 3-4, bousfiha2020furtherevidencefor pages 1-2, bousfiha2020furtherevidencefor pages 2-4, mujtaba2015amutationof pages 4-6) | Primary human variant interpretation with in vitro/in silico support | ACMG term labels: pathogenic / likely pathogenic (case-specific review required) | ClinVar/ACMG status should be checked live because classifications may change. |
| Diagnostics | Recommended workup is standard hereditary hearing-loss evaluation: audiometry/ABR, clinical exam to exclude syndromic causes, and molecular testing via multigene hearing-loss panel or exome/genome sequencing with segregation testing. MET should be included in comprehensive hearing-loss analysis rather than isolated first-line testing. (mujtaba2015amutationof pages 1-3, bousfiha2020furtherevidencefor pages 1-2, zhang2024aav‐mediatedgenetherapy pages 1-2) | Primary case reports plus 2024 field review | term: pure-tone audiometry; term: auditory brainstem response; term: exome sequencing; term: segregation analysis | No DFNB97-specific biomarker, pathology assay, or imaging signature is established. |
| Treatment / management | No MET-specific disease-modifying therapy is established. Current real-world management is supportive/rehabilitative hearing-loss care, including hearing aids where useful, cochlear implantation when indicated, and speech/language habilitation; the Moroccan child underwent cochlear implantation at age 4. (bousfiha2020furtherevidencefor pages 2-2, zhang2024aav‐mediatedgenetherapy pages 1-2) | Primary case implementation plus contemporary hereditary-deafness review | NCIT term labels: Cochlear Implantation; Hearing Aid Device; Speech Therapy / Auditory rehabilitation (ID verification required) | Published DFNB97-specific post-implant auditory outcomes were not reported in the retrieved evidence. |
| Experimental therapeutics | No registered DFNB97- or MET-hearing-loss-specific interventional trial was identified. 2024 hearing-loss gene therapy advances are real but currently center on other genes such as OTOF, not MET. (zhang2024aav‐mediatedgenetherapy pages 1-2) | 2024 field review; trial search context | term: gene therapy for hereditary deafness; DFNB9/OTOF as field comparator | MET pathway manipulation may have safety/oncology implications and is not a validated DFNB97 strategy. |
| Epidemiology | DFNB97 appears ultra-rare: only two reported families were identified in the retrieved literature (Pakistan and Morocco). Screening of 100 unrelated Pakistani nonsyndromic hearing-loss families found no additional MET cases in the 2015 report. (mujtaba2015amutationof pages 3-4, bousfiha2020furtherevidencefor pages 1-2) | Primary human evidence | term: rare disease; term: ultra-rare genetic hearing loss | No population prevalence, incidence, or carrier-frequency estimate is established for DFNB97 specifically. |
| Population/genetic context | Reported families were consanguineous, consistent with recessive inheritance and enrichment of rare homozygous variants in some populations. Pakistan has high ARNSHL gene discovery yield, but MET contributes a very small fraction relative to major genes. (bousfiha2020furtherevidencefor pages 1-2, shadab2024autosomalrecessivenon‐syndromic pages 8-9, mujtaba2015amutationof pages 1-3) | Primary cases plus 2024 population review | term: consanguinity; term: founder effect evaluation | There is no confirmed MET founder variant for DFNB97 at present. |
| Models | Direct DFNB97 model is lacking. Relevant comparative evidence includes embryonic lethality of complete Met loss in mouse, reduced neuromast-derived hair cells in zebrafish met morphants, and HGF-pathway mouse data showing failure of neural crest/intermediate-cell incorporation into stria vascularis with reduced endocochlear potential and deafness. (mujtaba2015amutationof pages 4-6, naz2020growthfactorand pages 7-8, shadab2024autosomalrecessivenon‐syndromic pages 8-9) | Model-organism/pathway evidence | NCBI Taxon labels: Mus musculus; Danio rerio | Mechanistic extrapolation from HGF or global Met perturbation may not fully mimic human missense DFNB97. |
| 2023-2024 research status | Recent literature mainly provides broader ARNSHL synthesis, stria-vascularis biology, and rapid progress in gene therapy for other deafness genes. No new 2023-2024 DFNB97 patient series, natural-history cohort, variant-specific functional animal model, or MET-targeted therapy was found in the retrieved evidence. (shadab2024autosomalrecessivenon‐syndromic pages 8-9, zhang2024aav‐mediatedgenetherapy pages 1-2) | Recent expert synthesis/review | term: precision medicine; term: stria vascularis biology | Knowledge gaps remain large despite strong gene-disease validity. |


*Table: This table summarizes the most knowledge-base-ready findings for MET-related autosomal recessive nonsyndromic hearing loss 97, separating well-supported human evidence from pathway-based inference. It is useful for quickly populating core disease, gene, phenotype, mechanism, diagnosis, and treatment fields while flagging major gaps.*

## Evidence framework

* **Direct human DFNB97 evidence:** Mujtaba et al., *Journal of Medical Genetics*, final publication August 2015, DOI [10.1136/jmedgenet-2015-103023](https://doi.org/10.1136/jmedgenet-2015-103023), PMID **25941349**; and Bousfiha et al., *Human Heredity*, published online December 4, 2019 and in volume 84 (2020), DOI [10.1159/000503450](https://doi.org/10.1159/000503450). (mujtaba2015amutationof pages 1-3, bousfiha2020furtherevidencefor pages 1-2)
* **Mechanistic evidence:** structural prediction, an exon-trap experiment, expression studies, and HGF/MET-pathway mouse or zebrafish studies. This is biologically persuasive but not equivalent to functional proof for each human allele. (mujtaba2015amutationof pages 3-4, mujtaba2015amutationof pages 4-6, naz2020growthfactorand pages 7-8)
* **Recent context:** 2024 literature concerns the broader Pakistani recessive-hearing-loss landscape, stria-vascularis biology, and gene therapy for other genotypes; no new 2023–2024 DFNB97 cohort or MET-directed treatment was found. (shadab2024autosomalrecessivenon‐syndromic pages 8-9, zhang2024aav‐mediatedgenetherapy pages 1-2)

## 1. Disease information

### Definition and identifiers

DFNB97 is a monogenic form of isolated, recessively inherited hearing impairment associated with biallelic **MET** variants. Open Targets maps the disease to **MONDO:0014739**, MET Ensembl **ENSG00000105976**, and cites four disease-target evidence records, including PMID 25941349 and ClinVar record RCV000202585. (OpenTargets Search: autosomal recessive nonsyndromic hearing loss 97-MET)

Recommended database labels are:

* **Preferred name:** autosomal recessive nonsyndromic hearing loss 97.
* **Synonyms:** DFNB97; nonsyndromic autosomal recessive deafness 97; MET-related nonsyndromic hearing loss; MET-related deafness.
* **MONDO:** MONDO:0014739.
* **Causal-gene OMIM identifier:** **MET, OMIM 164860**. The disease-specific OMIM phenotype number should be verified directly in the current OMIM record before ingestion because it was not exposed reliably in the retrieved sources. (bousfiha2020furtherevidencefor pages 2-2)
* **ICD-10/ICD-11 and MeSH:** there is no known DFNB97-specific billing or MeSH code. Use the appropriate bilateral sensorineural/congenital hearing-loss code plus a molecular diagnosis; do not treat a generic code as uniquely identifying DFNB97.

The evidence is **aggregated disease-level literature and family-based research**, not an EHR-derived patient series. The two primary reports nevertheless contain individual-level pedigree, audiometric, imaging, and laboratory observations. (mujtaba2015amutationof pages 1-3, bousfiha2020furtherevidencefor pages 1-2)

### Landmark abstract quotation

The discovery paper states: **“Homozygosity mapping with a dense array of one million SNP markers allowed us to map the gene for recessively inherited severe hearing loss to chromosome 7q31.2, defining a new deafness locus designated DFNB97 (maximum LOD score of 4.8).”** It concludes: **“We identified a missense mutation of MET, encoding the hepatocyte growth factor receptor, as a likely cause of hearing loss in humans.”** (mujtaba2015amutationof pages 1-3)

## 2. Etiology, risks, protective factors, and gene–environment interaction

### Causal factor

The established cause is **germline biallelic MET variation**. Both reported families were consanguineous and carried homozygous missense variants. Heterozygous relatives in the Moroccan family had normal hearing, supporting recessive inheritance. (bousfiha2020furtherevidencefor pages 1-2, bousfiha2020furtherevidencefor pages 2-4)

### Risk factors

* **Primary genetic risk:** two pathogenic or likely pathogenic MET alleles in trans—or a homozygous allele inherited through parental relatedness.
* **Family history/consanguinity:** increases the probability that both parents carry the same rare allele; it is not itself a biological cause.
* **Sex:** no sex-specific effect is established.
* **Age:** age determines when hearing impairment becomes detectable but is not a causal risk factor.
* **Environmental risks:** noise, congenital infection, and ototoxic drugs can independently cause or worsen hearing loss generally, but no DFNB97-specific interaction has been demonstrated.

### Protective factors and modifiers

No protective MET allele, environmental protective factor, penetrance modifier, or confirmed DFNB97 modifier gene is known. **GAB1, SPRY2, and METTL13/EEF1AKNMT** provide relevant pathway biology: GAB1 is a MET-associated scaffold; SPRY2 down-regulates receptor-tyrosine-kinase signaling; and a METTL13 allele has been proposed to suppress GAB1-related DFNB26 deafness. These are not proven modifiers of MET-related DFNB97. (naz2020growthfactorand pages 7-8)

No DFNB97-specific gene–environment interaction has been reported. Ordinary hearing conservation and avoidance of unnecessary ototoxic exposure remain prudent tertiary measures, but they cannot prevent genetically programmed congenital cochlear dysfunction.

## 3. Phenotypes

### Core auditory phenotype

In Pakistani family HLGM17, all nine affected relatives, aged 5–60 years, had hearing loss recognized at or before age two because of delayed speech. Pure-tone averages from 500–4,000 Hz were **74–89 dB HL**, indicating severe sensorineural impairment with intrafamilial threshold variation. The original paper describes nine of nine evaluated affected relatives with the defining phenotype, but this is a pedigree-specific proportion, not a population frequency. (mujtaba2015amutationof pages 1-3)

The Moroccan proband was a seven-year-old girl with **total bilateral** nonsyndromic impairment, detected by brainstem auditory-evoked testing at age 3 years 9 months. She received a cochlear implant at age four. CT and MRI showed no inner-ear or cochleovestibular-nerve abnormality. (bousfiha2020furtherevidencefor pages 2-2)

Suggested HPO annotations include:

* **Sensorineural hearing impairment** — HP:0000407.
* **Bilateral sensorineural hearing impairment** — use the current HPO bilateral child term or combine HP:0000407 with a bilateral qualifier.
* **Severe hearing impairment** and **profound hearing impairment** — verify current severity-specific HPO identifiers.
* **Prelingual hearing impairment** — HP:0000399.
* **Delayed speech and language development** — HP:0000750.
* **Normal vestibular function** and normal inner-ear imaging are important negative observations but should not be encoded as universal defining features.

### Vestibular and extra-auditory findings

Pakistani participants walked independently at 12–13 months and had normal Romberg and tandem-gait tests, suggesting intact or residual peripheral vestibular function. No liver, kidney, cardiac disease, or cancer history was reported; two affected adolescents had normal blood counts, serum chemistry, urinalysis, liver tests, and funduscopy. These observations support the designation “nonsyndromic,” but ten known patients are insufficient to exclude subtle, late-onset, or allele-specific systemic effects. (mujtaba2015amutationof pages 1-3)

### Course and quality of life

Published DFNB97 data do not establish whether hearing thresholds are stable or progressive. The Pakistani pedigree spans ages 5–60 and shows variable thresholds, but no longitudinal audiometry was reported. Hearing loss of this degree can compromise spoken-language acquisition, education, communication, social participation, and psychosocial well-being. The Moroccan report emphasizes early intervention for speech, intellectual, cognitive, and social development, but no DFNB97-specific EQ-5D, SF-36, PROMIS, or hearing-related quality-of-life measurements exist. (bousfiha2020furtherevidencefor pages 1-2)

## 4. Genetic and molecular information

### Gene

**MET** encodes the MET proto-oncogene receptor tyrosine kinase, also called hepatocyte growth factor receptor/HGFR. It lies at chromosome **7q31.2**. HGF is its ligand; pathogenic noncoding HGF variants cause the distinct recessive locus DFNB39, making HGF–MET a ligand–receptor pair in which disruption of either partner can cause nonsyndromic hearing loss. (mujtaba2015amutationof pages 4-6, naz2020growthfactorand pages 7-8)

### Reported DFNB97 variants

1. **c.2521T>G, p.(Phe841Val), commonly abbreviated p.F841V.** This was homozygous in the nine affected Pakistani relatives and co-segregated perfectly. It was absent from 800 ethnically matched control chromosomes and 136,602 public-database chromosomes available in 2015; no additional case was found among 100 unrelated Pakistani families. The residue is evolutionarily conserved. PROVEAN, PolyPhen-2, MutationTaster, and Human Splicing Finder supported deleteriousness, whereas SIFT was tolerant. CUPSAT/I-Mutant predicted reduced stability, and an exon-trap assay suggested possible alternative intron retention. It lies in extracellular IPT4, part of the high-affinity HGF-binding region. (mujtaba2015amutationof pages 3-4, mujtaba2015amutationof pages 8-10, mujtaba2015amutationof pages 4-6)

2. **c.948A>G, p.(Ile316Met).** This was homozygous in the Moroccan child and heterozygous in her unaffected parents and older brother. It affects a conserved residue in the extracellular SEMA domain, important for HGF binding, receptor dimerization, and activation. Computational scores supported damage, and molecular-dynamics simulation predicted loss of flexibility with altered receptor conformation and binding-site function. Reported database frequency was low but not absent, including one homozygote among 9,790 African individuals in the dataset used by the authors; this, the singleton phenotype, and absence of a direct signaling assay warrant contemporary ClinVar/ACMG re-evaluation rather than uncritical acceptance of the paper’s “pathogenic” label. (bousfiha2020furtherevidencefor pages 1-2, bousfiha2020furtherevidencefor pages 2-4)

An apparent **p.Phe859Val/c.2575T>G** label in the later paper likely reflects alternative transcript/isoform numbering for the Pakistani allele. A knowledge base should retain the publication-specific representation but normalize all alleles against a declared MANE transcript and genome build before merging records. (bousfiha2020furtherevidencefor pages 5-6)

Both are constitutional/germline missense variants, not somatic cancer alterations. Current gnomAD frequencies, ClinVar review status, HGNC ID, MANE transcript, and genomic coordinates should be refreshed through live database queries before clinical reporting.

### Other molecular categories

No DFNB97-associated copy-number variant, translocation, inversion, repeat expansion, mitochondrial variant, epigenetic signature, methylation defect, somatic mosaicism, or validated modifier is known. No patient-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or multi-omic profile has been published.

## 5. Environmental information

DFNB97 is genetic; no toxin, radiation exposure, pollutant, lifestyle behavior, diet, infection, smoking, alcohol use, or occupational exposure is established as a cause or trigger. Congenital CMV, meningitis, noise, and ototoxic agents remain important **differential or additive causes of hearing loss**, not demonstrated components of DFNB97 pathogenesis. Vaccination and avoidance of excessive noise or unnecessary ototoxic medication protect general auditory health but do not correct MET deficiency.

## 6. Mechanism and pathophysiology

### Proposed causal chain

1. **Upstream lesion:** biallelic MET missense variation changes the extracellular SEMA or IPT4 domain.
2. **Receptor defect:** impaired folding, stability, HGF binding, dimerization, activation, or—specifically for p.Phe841Val—possibly transcript splicing reduces effective HGF–MET signaling.
3. **Developmental cellular defect:** pathway evidence indicates that HGF–MET signaling is required for proper migration/incorporation of neural-crest-derived melanocytic intermediate cells into the middle layer of the developing stria vascularis.
4. **Tissue dysfunction:** abnormal or thinned stria vascularis cannot adequately establish cochlear ionic homeostasis and the endocochlear potential.
5. **Physiologic failure:** the normal stria supports approximately **+80 to +120 mV** and potassium near **154 mM** in endolymph, conditions needed for sensory-hair-cell mechanotransduction.
6. **Clinical outcome:** reduced cochlear transduction produces bilateral severe-to-profound sensorineural hearing loss and secondary delay in spoken-language development. (naz2020growthfactorand pages 7-8, shadab2024autosomalrecessivenon‐syndromic pages 8-9)

The downstream HGF-stimulated MET network has numerous branches and includes GAB1 scaffolding and SPRY2 negative regulation. Canonical MET signaling can engage RAS–MAPK, PI3K–AKT, PLCγ, STAT, survival, proliferation, motility, and epithelial–mesenchymal programs, but the precise branch responsible for DFNB97 has not been isolated experimentally. (naz2020growthfactorand pages 7-8)

### Suggested ontology annotations

* **GO biological processes:** hepatocyte growth factor receptor signaling pathway; transmembrane receptor protein tyrosine kinase signaling; neural crest cell migration; melanocyte migration/differentiation; inner-ear morphogenesis; stria-vascularis development; potassium-ion homeostasis; sensory perception of sound.
* **GO molecular function:** HGF receptor activity; transmembrane receptor protein tyrosine kinase activity; ATP binding; protein-tyrosine-kinase activity.
* **GO cellular component:** plasma membrane; receptor complex; basolateral plasma membrane, where supported by cell-specific evidence.
* **Cell Ontology labels:** melanocyte; neural-crest-derived cell; strial intermediate cell; cochlear hair cell; spiral ganglion neuron. Exact CL identifiers should be validated because “strial intermediate cell” may not have a dedicated current class.

There is no demonstrated primary metabolic enzyme defect, immune-mediated process, autoinflammation, fibrosis, ischemia, or systemic biochemical abnormality. Hair cells and spiral ganglion cells express HGF/MET in embryonic rat cochlea, but whether they are primary cellular targets in human DFNB97 is unresolved. (bousfiha2020furtherevidencefor pages 5-6)

## 7. Anatomical structures affected

The primary organ is the **inner ear**, specifically the auditory cochlea. The strongest mechanistic localization is the **stria vascularis** along the lateral cochlear wall, particularly its neural-crest-derived intermediate-cell layer. Hair cells, spiral ganglion neurons, and nonsensory cochlear structures are biologically relevant but not proven primary sites of human disease. No secondary organ involvement is established. (bousfiha2020furtherevidencefor pages 5-6, naz2020growthfactorand pages 7-8)

Suggested anatomy terms are **UBERON:0001846 inner ear**, **UBERON:0001851 cochlea**, organ of Corti, cochlear duct, cochlear lateral wall, and stria vascularis; the latter identifiers should be checked in the current UBERON release. The clinical impairment is bilateral. CT/MRI can be anatomically normal, as in the Moroccan child. (bousfiha2020furtherevidencefor pages 2-2)

## 8. Temporal development and natural history

Available evidence supports congenital or very early childhood onset, usually recognized during the prelingual period. The Pakistani family’s onset was reported by age two; the Moroccan case was objectively identified in early childhood. The condition is chronic and lifelong without auditory rehabilitation. There are no validated clinical stages, remission pattern, spontaneous recovery rate, or quantified progression rate. (mujtaba2015amutationof pages 1-3, bousfiha2020furtherevidencefor pages 2-2)

The major intervention window is early childhood, when access to sound is important for spoken-language and educational development. This is a developmental and rehabilitative principle, not evidence that MET molecular pathology itself is reversible after a defined age.

## 9. Inheritance, penetrance, and population epidemiology

Inheritance is autosomal recessive. For two confirmed carrier parents, each pregnancy conventionally has a 25% probability of an affected child, 50% probability of an unaffected carrier, and 25% probability of inheriting neither familial allele, subject to confirmation that the allele is truly pathogenic.

Penetrance appears high in the Pakistani pedigree, where the homozygous allele tracked with hearing loss, but it cannot be estimated population-wide. Expressivity is variable in audiometric threshold. Anticipation is not expected; germline mosaicism has not been reported. No confirmed founder allele or sex bias is known. (mujtaba2015amutationof pages 1-3, mujtaba2015amutationof pages 3-4)

Only two families were documented in the retrieved direct literature. Screening 100 additional Pakistani nonsyndromic-hearing-loss families found no case, and a 2024 review indicates that uncommon Pakistani ARNSHL genes each account for under 2%, whereas 13 much more prevalent genes collectively explain over half of profound cases. Consequently, **DFNB97-specific prevalence, incidence, carrier frequency, geographic distribution, and sex ratio are unknown**; extrapolation from generic hearing-loss statistics would be misleading. (mujtaba2015amutationof pages 3-4, shadab2024autosomalrecessivenon‐syndromic pages 8-9)

## 10. Diagnostics

### Clinical evaluation

1. Confirm hearing status with newborn screening followed by diagnostic **auditory brainstem response/BAEP**, otoacoustic emissions where informative, tympanometry, and age-appropriate pure-tone and speech audiometry.
2. Establish sensorineural rather than conductive loss and document laterality, frequency configuration, severity, and longitudinal change.
3. Examine for syndromic findings; assess vestibular function and development. Consider ophthalmology, renal, cardiac, infectious, or other testing only when history or examination indicates it.
4. CT or MRI is useful for cochlear-implant planning or suspected structural/nerve abnormality, but normal imaging does not exclude DFNB97. (bousfiha2020furtherevidencefor pages 2-2, mujtaba2015amutationof pages 1-3)

### Molecular testing

A comprehensive hearing-loss **multigene panel** that includes MET is generally preferable to first-line MET-only sequencing because hereditary hearing loss is highly heterogeneous. Exome sequencing was decisive in both reported families; genome sequencing may improve detection of noncoding and structural alleles when panel/exome testing is negative. Candidate variants require read-quality review, population-frequency assessment, phenotype fit, ACMG/AMP interpretation, and parental/family segregation. (mujtaba2015amutationof pages 1-3, bousfiha2020furtherevidencefor pages 1-2)

CMA, karyotyping, FISH, mitochondrial sequencing, and repeat-expansion testing are not DFNB97-specific; use them only when phenotype or first-line results suggest another diagnosis. No blood chemistry, circulating protein, metabolite, biopsy, histopathology, RNA, proteomic, or liquid-biopsy marker diagnoses DFNB97.

### Differential diagnosis

The differential includes common nonsyndromic genes such as GJB2, SLC26A4, OTOF, MYO15A, CDH23, TMC1, and TMPRSS3; HGF-related DFNB39; congenital CMV; auditory neuropathy; ototoxicity; structural malformations; and syndromes such as Usher or Pendred syndrome. Normal vestibular testing and imaging can support but do not uniquely identify DFNB97.

### Screening

Universal newborn hearing screening detects impairment, not genotype. Once a familial MET diagnosis is established, targeted cascade testing can identify carriers and affected relatives. Population carrier screening is not currently supported by prevalence or clinical-utility data.

## 11. Outcome and prognosis

DFNB97 is not known to reduce survival or life expectancy; no disease-specific mortality has been reported. Prognosis primarily concerns auditory communication. Untreated severe-to-profound prelingual loss can produce persistent speech/language, educational, vocational, and social disability. Early, effective access to communication—spoken, signed, or multimodal—can substantially mitigate secondary developmental consequences, but DFNB97-specific response rates are unavailable. (bousfiha2020furtherevidencefor pages 1-2)

The Moroccan child’s cochlear implantation demonstrates real-world implementation, but the retrieved report did not provide postoperative speech-perception or threshold outcomes. No molecular prognostic biomarker predicts progression, hearing-aid benefit, or implant response. Cochleovestibular-nerve integrity, age at intervention, residual hearing, rehabilitation access, and communication environment are likely to matter as in other congenital hearing losses, but these have not been tested specifically in DFNB97. (bousfiha2020furtherevidencefor pages 2-2, zhang2024aav‐mediatedgenetherapy pages 1-2)

## 12. Treatment and current applications

### Standard management

There is no approved pharmacotherapy that restores MET function. Management is individualized and may include:

* hearing aids for aidable residual hearing;
* cochlear implantation for severe/profound impairment with insufficient hearing-aid benefit;
* auditory-verbal, speech/language, and listening therapy where spoken language is a family goal;
* sign-language and multimodal communication access;
* educational accommodations, assistive listening systems, and psychosocial support;
* periodic audiologic and device monitoring.

Suggested NCIt intervention labels are **Hearing Aid**, **Cochlear Implantation**, **Speech Therapy**, **Auditory Rehabilitation**, and **Genetic Counseling**; exact current NCIt codes should be validated before database loading.

### Advanced and experimental therapy

No MET replacement, gene editing, antisense RNA, cell therapy, HGF agonist, or small-molecule treatment has demonstrated efficacy in DFNB97. A 2024 authoritative review states that current hereditary-deafness options remain largely hearing aids and cochlear implants and that AAV therapy has restored hearing in more than 20 genetic mouse models. It also stresses that different deafness genes and target-cell transduction efficiencies require genotype- and cell-specific precision approaches. (zhang2024aav‐mediatedgenetherapy pages 1-2)

OTOF gene therapy restored hearing in early DFNB9 trials, making it an important translational proof of concept, **not evidence of efficacy for MET-related disease**. MET is broadly expressed and is also an oncogenic receptor; indiscriminate systemic HGF/MET activation would therefore require particularly careful safety evaluation. The clinical-trial search found no relevant DFNB97/MET-hearing-loss trial; oncology trials targeting MET and a middle-ear implant named “MET V” are unrelated and must not be linked to this disease.

## 13. Prevention

The inherited molecular lesion cannot be prevented by vaccination, diet, exercise, or medication.

* **Primary genetic prevention/family planning:** genetic counseling, carrier testing of relatives, partner testing, prenatal diagnosis, or preimplantation genetic testing when a familial pathogenic variant is established. These are optional reproductive choices, not directives.
* **Secondary prevention:** universal newborn hearing screening, rapid diagnostic ABR, early molecular testing, and prompt communication intervention can prevent or reduce secondary language deprivation.
* **Tertiary prevention:** optimize hearing devices, educational access, and rehabilitation; avoid excessive noise and unnecessary ototoxic exposure; monitor residual hearing.

No vaccine or chemoprophylaxis is relevant specifically to DFNB97.

## 14. Other species and natural disease

No naturally occurring veterinary DFNB97 equivalent, breed predisposition, zoonotic potential, or cross-species transmission is established. Orthologous **Met** exists in common vertebrate models, including **Mus musculus** (NCBI Taxon 10090) and **Danio rerio** (Taxon 7955). MET’s developmental functions are evolutionarily conserved, but global Met deficiency in mice is embryonically lethal, whereas zebrafish met morphants have reduced neuromast-derived hair cells. Neither exactly reproduces the residual-function human missense disorder. (mujtaba2015amutationof pages 4-6, naz2020growthfactorand pages 7-8)

## 15. Model organisms and research models

No published p.Phe841Val or p.Ile316Met knock-in mouse, patient-derived iPSC cochlear model, organoid, or CRISPR model was identified.

Relevant indirect models include:

* **Mouse:** complete Met loss is embryonically lethal, limiting conventional knockout analysis. Hgf overexpression and inner-ear Hgf deficiency both cause deafness, showing that HGF dosage must be tightly regulated. HGF-pathway models exhibit failed neural-crest-cell incorporation into the strial intermediate layer and reduced endocochlear potential. (mujtaba2015amutationof pages 4-6, naz2020growthfactorand pages 7-8, shadab2024autosomalrecessivenon‐syndromic pages 8-9)
* **Zebrafish:** met morphants show fewer neuromast-derived hair cells. Neuromasts are experimentally accessible but are not anatomically equivalent to the mammalian stria vascularis. (naz2020growthfactorand pages 7-8)
* **Rat expression studies:** HGF and MET have been detected in embryonic cochlear hair cells and spiral ganglion cells; expression alone does not establish the causal cell type. (bousfiha2020furtherevidencefor pages 5-6)
* **Future models:** inner-ear-specific conditional Met loss, human-variant knock-in mice, patient iPSCs, and vascularized cochlear/strial organoids would allow direct measurement of MET phosphorylation, neural-crest migration, intermediate-cell differentiation, endocochlear potential, and therapeutic rescue.

## 2023–2024 developments and expert assessment

The principal recent conclusion is the persistence of a major evidence gap. A 2024 review of Pakistani ARNSHL emphasizes extreme heterogeneity and identifies 13 genes responsible for more than half of profound cases; MET is not among those common contributors. The same review supports the HGF–MET–stria-vascularis mechanism but does not report new DFNB97 families. (shadab2024autosomalrecessivenon‐syndromic pages 8-9)

The broader 2024 gene-therapy field has moved from numerous successful mouse models to human hearing restoration in OTOF deficiency. Expert analysis nevertheless emphasizes the complex cochlear anatomy, different target-cell requirements, and need for precision vectors for each genotype. For DFNB97, the immediate research priorities are therefore: (1) international case ascertainment and standardized longitudinal audiometry; (2) contemporary variant curation; (3) variant-specific functional assays; (4) definition of the critical human cochlear cell population; and (5) development of conditional or knock-in models before contemplating MET-directed therapy. (zhang2024aav‐mediatedgenetherapy pages 1-2)

## Knowledge gaps and curation cautions

1. The disease is supported by only two reported families; phenotype frequencies should not be generalized beyond them.
2. Progression, penetrance, carrier frequency, prevalence, and implant outcomes are unknown.
3. The mechanistic link to strial intermediate cells is strong pathway inference, not direct human histopathology.
4. Transcript-dependent variant-number discrepancies require MANE normalization.
5. Published pathogenicity labels—especially for p.Ile316Met—should be reconciled with current gnomAD, ClinVar, ClinGen, and ACMG/AMP evidence.
6. HGF-related DFNB39, GAB1-related DFNB26, MET-related syndromic presentations, somatic oncogenic MET alterations, and DFNB97 must remain separate knowledge-base entities.

Overall, DFNB97 is a credible but exceptionally rare MET-associated cochlear developmental disorder. Its human phenotype is reasonably defined as early bilateral severe-to-profound nonsyndromic sensorineural hearing loss, whereas its detailed cellular mechanism, natural history, population burden, and disease-modifying treatment remain unresolved.

References

1. (mujtaba2015amutationof pages 1-3): Ghulam Mujtaba, Julie M Schultz, Ayesha Imtiaz, Robert J Morell, Thomas B Friedman, and Sadaf Naz. A mutation of met, encoding hepatocyte growth factor receptor, is associated with human dfnb97 hearing loss. Journal of Medical Genetics, 52:548-552, May 2015. URL: https://doi.org/10.1136/jmedgenet-2015-103023, doi:10.1136/jmedgenet-2015-103023. This article has 49 citations and is from a domain leading peer-reviewed journal.

2. (bousfiha2020furtherevidencefor pages 1-2): Amale Bousfiha, Zied Riahi, Lamiae Elkhattabi, Amina Bakhchane, Hicham Charoute, Khalid Snoussi, Crystel Bonnet, Christine Petit, and Abdelhamid Barakat. Further evidence for the implication of the met gene in non-syndromic autosomal recessive deafness. Human Heredity, 84:109-116, Dec 2020. URL: https://doi.org/10.1159/000503450, doi:10.1159/000503450. This article has 7 citations and is from a peer-reviewed journal.

3. (naz2020growthfactorand pages 7-8): Sadaf Naz and Thomas B. Friedman. Growth factor and receptor malfunctions associated with human genetic deafness. Clinical Genetics, 97:138-155, Oct 2020. URL: https://doi.org/10.1111/cge.13641, doi:10.1111/cge.13641. This article has 17 citations and is from a peer-reviewed journal.

4. (bousfiha2020furtherevidencefor pages 2-2): Amale Bousfiha, Zied Riahi, Lamiae Elkhattabi, Amina Bakhchane, Hicham Charoute, Khalid Snoussi, Crystel Bonnet, Christine Petit, and Abdelhamid Barakat. Further evidence for the implication of the met gene in non-syndromic autosomal recessive deafness. Human Heredity, 84:109-116, Dec 2020. URL: https://doi.org/10.1159/000503450, doi:10.1159/000503450. This article has 7 citations and is from a peer-reviewed journal.

5. (zhang2024aav‐mediatedgenetherapy pages 1-2): Liyan Zhang, Fangzhi Tan, Jieyu Qi, Yicheng Lu, Xiaohan Wang, Xuehan Yang, Xiangyan Chen, Xinru Zhang, Jinyi Fan, Yinyi Zhou, Li Peng, Nianci Li, Lei Xu, Shiming Yang, and Renjie Chai. Aav‐mediated gene therapy for hereditary deafness: progress and perspectives. Advanced Science, Nov 2024. URL: https://doi.org/10.1002/advs.202402166, doi:10.1002/advs.202402166. This article has 41 citations and is from a peer-reviewed journal.

6. (OpenTargets Search: autosomal recessive nonsyndromic hearing loss 97-MET): Open Targets Query (autosomal recessive nonsyndromic hearing loss 97-MET, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

7. (mujtaba2015amutationof pages 3-4): Ghulam Mujtaba, Julie M Schultz, Ayesha Imtiaz, Robert J Morell, Thomas B Friedman, and Sadaf Naz. A mutation of met, encoding hepatocyte growth factor receptor, is associated with human dfnb97 hearing loss. Journal of Medical Genetics, 52:548-552, May 2015. URL: https://doi.org/10.1136/jmedgenet-2015-103023, doi:10.1136/jmedgenet-2015-103023. This article has 49 citations and is from a domain leading peer-reviewed journal.

8. (mujtaba2015amutationof pages 8-10): Ghulam Mujtaba, Julie M Schultz, Ayesha Imtiaz, Robert J Morell, Thomas B Friedman, and Sadaf Naz. A mutation of met, encoding hepatocyte growth factor receptor, is associated with human dfnb97 hearing loss. Journal of Medical Genetics, 52:548-552, May 2015. URL: https://doi.org/10.1136/jmedgenet-2015-103023, doi:10.1136/jmedgenet-2015-103023. This article has 49 citations and is from a domain leading peer-reviewed journal.

9. (bousfiha2020furtherevidencefor pages 2-4): Amale Bousfiha, Zied Riahi, Lamiae Elkhattabi, Amina Bakhchane, Hicham Charoute, Khalid Snoussi, Crystel Bonnet, Christine Petit, and Abdelhamid Barakat. Further evidence for the implication of the met gene in non-syndromic autosomal recessive deafness. Human Heredity, 84:109-116, Dec 2020. URL: https://doi.org/10.1159/000503450, doi:10.1159/000503450. This article has 7 citations and is from a peer-reviewed journal.

10. (shadab2024autosomalrecessivenon‐syndromic pages 8-9): Madiha Shadab, Ansar Ahmed Abbasi, Ahsan Ejaz, Afif Ben‐Mahmoud, Vijay Gupta, Hyung‐Goo Kim, and Barbara Vona. Autosomal recessive non‐syndromic hearing loss genes in pakistan during the previous three decades. Journal of Cellular and Molecular Medicine, Mar 2024. URL: https://doi.org/10.1111/jcmm.18119, doi:10.1111/jcmm.18119. This article has 9 citations and is from a peer-reviewed journal.

11. (bousfiha2020furtherevidencefor pages 5-6): Amale Bousfiha, Zied Riahi, Lamiae Elkhattabi, Amina Bakhchane, Hicham Charoute, Khalid Snoussi, Crystel Bonnet, Christine Petit, and Abdelhamid Barakat. Further evidence for the implication of the met gene in non-syndromic autosomal recessive deafness. Human Heredity, 84:109-116, Dec 2020. URL: https://doi.org/10.1159/000503450, doi:10.1159/000503450. This article has 7 citations and is from a peer-reviewed journal.

12. (mujtaba2015amutationof pages 4-6): Ghulam Mujtaba, Julie M Schultz, Ayesha Imtiaz, Robert J Morell, Thomas B Friedman, and Sadaf Naz. A mutation of met, encoding hepatocyte growth factor receptor, is associated with human dfnb97 hearing loss. Journal of Medical Genetics, 52:548-552, May 2015. URL: https://doi.org/10.1136/jmedgenet-2015-103023, doi:10.1136/jmedgenet-2015-103023. This article has 49 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Autosomal_Recessive_Nonsyndromic_Hearing_Loss_97-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014739` (5 mentions) - the report calls it "if available"; MONDO calls it **autosomal recessive nonsyndromic hearing loss 97**