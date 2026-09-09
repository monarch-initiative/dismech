---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-28T19:01:28.891063'
end_time: '2026-08-28T19:14:02.445148'
duration_seconds: 753.55
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Autosomal Recessive Nonsyndromic Hearing Loss 93 (DFNB93, CABP2-related)
  mondo_id: MONDO:0013963
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 26
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 6
  validator_version: 0.2.1
term_validation:
  total_terms: 12
  verified: 12
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0013963
    reported_labels:
    - if available
    ontology_label: autosomal recessive nonsyndromic hearing loss 93
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Autosomal_Recessive_Nonsyndromic_Hearing_Loss_93-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Autosomal Recessive Nonsyndromic Hearing Loss 93 (DFNB93, CABP2-related)
- **MONDO ID:** MONDO:0013963 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Nonsyndromic Hearing Loss 93 (DFNB93, CABP2-related)** covering all of the
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
- **Disease Name:** Autosomal Recessive Nonsyndromic Hearing Loss 93 (DFNB93, CABP2-related)
- **MONDO ID:** MONDO:0013963 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Autosomal Recessive Nonsyndromic Hearing Loss 93 (DFNB93, CABP2-related)** covering all of the
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


# Autosomal-recessive nonsyndromic hearing loss 93 (DFNB93; CABP2-related)

## Executive summary

DFNB93 is an exceptionally rare, autosomal-recessive, usually prelingual sensorineural hearing disorder caused by biallelic pathogenic variants in **CABP2**, encoding calcium-binding protein 2 (CaBP2). The best-supported phenotype is bilateral, symmetric, moderate-to-severe hearing loss, often greatest at middle frequencies; severe loss also occurs. Physiologically, DFNB93 is best classified as a **presynaptic auditory synaptopathy**: outer-hair-cell amplification and cochlear architecture can remain relatively preserved, while excessive inactivation of inner-hair-cell (IHC) CaV1.3 calcium channels limits sustained glutamate release to spiral-ganglion neurons (SGNs). Human evidence remains limited to a small number of families, so prevalence, penetrance, progression, and genotype–phenotype relationships are not yet quantified reliably. (picher2017ca2+bindingprotein2 pages 1-2, schrauwen2012amutationin pages 1-2, picher2017ca2+bindingprotein2 pages 2-3)

The principal recent advance is the December 24, 2024 eLife study showing that CaBP1 and CaBP2 cooperate to suppress voltage- and calcium-dependent CaV1.3 inactivation and sustain IHC exocytosis. A dedicated CABP2 registry, **NCT06680934**, began August 16, 2024 and is recruiting, representing the first disease-specific real-world natural-history infrastructure. AAV-mediated Cabp2 augmentation has improved hearing in mice, but no CABP2-directed human interventional trial or approved molecular therapy was identified. (NCT06680934 chunk 1, oestreicher2024cabp1and2 pages 1-2, oestreicher2024cabp1and2 pages 11-12)

The key human, model, and translational evidence is summarized below.

| Evidence/source and date | Cohort/model | Variant/intervention | Phenotype or quantitative outcome | Interpretation/evidence type |
|---|---|---|---|---|
| Schrauwen et al., *Am J Hum Genet* (2012-10-05) | 3 consanguineous Iranian families (Sh10, Sh11, He) | **CABP2 c.637+1G>T**, predicted exon 6 skipping; **p.Phe164Serfs*4** | Moderate-to-severe **sensorineural** hearing impairment; founder effect supported by shared **0.52 Mb haplotype**; variant absent in **100 Iranian controls**; truncated protein showed altered Ca²⁺ binding and less potent **CaV1.3** regulation (schrauwen2012amutationin pages 1-2, schrauwen2012amutationin pages 7-8, schrauwen2012amutationin pages 3-4) | Primary human genetics + functional in vitro evidence establishing DFNB93 mechanism via hypofunctional CaBP2 |
| Picher et al., *PNAS* (2017-02) | 2 affected siblings from Northern Italy + family segregation | **CABP2 c.466G>T (p.Glu156Ter / p.E156X)** | Prelingual, bilateral, symmetric **moderate-to-severe** hearing impairment with characteristic **U-shaped/mid-frequency** emphasis affecting communication; no syndromic features on clinical exam; variant absent in **225 white controls** and not reported in ExAC in cited study context (picher2017ca2+bindingprotein2 pages 1-2) | Primary human clinical-genetic evidence for an independent CABP2 loss-of-function DFNB93 family |
| Koohiyan et al., *Audiol Neurotol* (2019-10) | Consanguineous Iranian family; 2 affected relatives/siblings in multigenerational pedigree | **CABP2 c.311G>A (p.Gly104Asp)** | **Prelingual bilateral severe** sensorineural hearing loss; segregated homozygously in affected relatives; absent in **50 normal-hearing controls** from same population; study states zero frequency in **1000 Genomes** and **ExAC** (koohiyan2019anovelpathogenic pages 4-5, koohiyan2019anovelpathogenic pages 3-4, koohiyan2019anovelpathogenic pages 1-2) | Primary human genetics showing phenotypic heterogeneity, extending CABP2 from moderate/severe to severe DFNB93 |
| Nawaz et al., *Heliyon* (available online 2023-12-14; 2024 issue) | Egyptian family A; 2 affected siblings with DASS background due to separate **LTBP3** defect | **CABP2 c.590T>C (p.Ile197Thr)** | Hearing impairment in Egyptian siblings was reported as having a **separate transmission mechanism independent of LTBP3**; both siblings homozygous for CABP2 missense variant while mother heterozygous (nawaz2024brachyolmiadentalanomalies pages 1-2) | Recent blended-phenotype report; supports CABP2 as contributor to hearing loss but not isolated DFNB93-only family ascertainment |
| Picher et al., *PNAS* (2017-02) | **Cabp2** knockout mouse (**Cabp2LacZ/LacZ**) | Genetic disruption of **Cabp2** | Elevated **ABR thresholds** and reduced amplitudes at **6–24 kHz**; **DPOAE** thresholds/amplitudes comparable to controls; reduced and more jittered SGN firing; preserved IHC/OHC anatomy and normal synapses with SGNs; expression stronger in **IHCs** than OHCs, also vestibular hair cells/outer retina (picher2017ca2+bindingprotein2 pages 2-3, picher2017ca2+bindingprotein2 pages 1-2, picher2017ca2+bindingprotein2 pages 7-8) | Primary model-organism evidence for **auditory synaptopathy** with preserved outer hair cell/cochlear amplification |
| Oestreicher et al., *Front Mol Neurosci* (2021-08) | Postnatal **Cabp2−/−** mice treated at **P5–P7** | **AAV2/1-Cabp2** or **AAV-PHP.eB-Cabp2** round-window gene therapy | Hearing improved in **16/24 (67%)** treated animals with **≥20 dB SPL** improvement at tested frequencies (**p<0.0001**); **ABR wave I** amplitude increased from **0.8±0.1 µV** to **1.3±0.2 µV** at 80 dB SPL (**p<0.001**); PHP.eB achieved about **98% IHC transduction**; DPOAEs largely unaffected in mutants (oestreicher2021cabp2genetherapyrestores pages 2-4, oestreicher2021cabp2genetherapyrestores pages 5-7, oestreicher2021cabp2genetherapyrestores pages 7-8, oestreicher2021cabp2genetherapyrestores pages 1-2) | Preclinical translational proof-of-concept that CABP2 deficiency is at least partially reversible by inner-ear gene augmentation |
| Oestreicher et al., *eLife* Version of Record (2024-12-24) | **Cabp1/2 double-knockout** mice | Loss of **CaBP1 + CaBP2**; rescue by transgenic/AAV-mediated CaBP2 re-expression | Severe auditory dysfunction: click **ABR threshold 59±2 dB SPL vs 30±2 WT** at 3–4 weeks (**N=8–9**), worsening to **68±5 dB SPL vs 30±1 WT** by 7–13 weeks (**N=7**); preserved ribbon density **12.9±0.2 WT vs 12.8±0.8 DKO synapses/cell**; SGN adaptation ratio **12.5±3.0 vs 3.4±0.2 WT, p<0.00001**; sound-responsive neuron yield **0.3/h vs 2.5/h WT**; rescue substantially recovered IHC synaptic function, **ABR wave I** amplitudes, and thresholds (oestreicher2024cabp1and2 pages 1-2, oestreicher2024cabp1and2 pages 11-12, oestreicher2024cabp1and2 pages 7-9, oestreicher2024cabp1and2 pages 13-14) | Latest mechanistic refinement: CaBP1 and CaBP2 cooperatively suppress CaV1.3 inactivation needed for sustained exocytosis and sound encoding |
| ClinicalTrials.gov **NCT06680934** (first posted 2024-11-08; recruiting) | Human registry/natural history study; **estimated n=100**; University Medical Center Goettingen | **CABP2 Patient Registry and Natural History Study** | Observational **case-only** patient registry for individuals with biallelic CABP2 variants; actual start **2024-08-16**; primary outcomes include **pure-tone audiometry** and **speech audiometry**; secondary outcomes **otoacoustic emissions** and **auditory brainstem response**; estimated completion **2049-08-16** (NCT06680934 chunk 1) | Current real-world implementation creating disease-specific natural-history infrastructure for diagnostics, phenotyping, and future trial readiness |


*Table: This table summarizes the main human, model-organism, translational, and registry evidence for CABP2-related DFNB93. It highlights reported variants, core phenotypes, quantitative rescue/model findings, and the distinction between isolated DFNB93 evidence and broader/blended presentations.*

## 1. Disease information

### Definition and identifiers

* **Preferred name:** autosomal-recessive nonsyndromic hearing loss 93.
* **Synonyms:** DFNB93; deafness, autosomal recessive 93; CABP2-related hearing loss; CABP2-associated hearing impairment; CABP2-related auditory synaptopathy.
* **Disease OMIM:** **614899** (DFNB93). **Gene OMIM/MIM:** **CABP2, 607314**. The locus was mapped to chromosome **11q13.3**. (schrauwen2012amutationin pages 1-2, koohiyan2019anovelpathogenic pages 1-2)
* **MONDO:** the supplied identifier **MONDO:0013963** should be retained, but its current label/cross-references should be verified directly in the live MONDO release before production ingestion.
* **Gene:** CABP2, seven exons in the transcript used by the original reports, encoding a 220-amino-acid Ca²⁺-binding protein. The 2012 HGVS descriptions used **NM_016366.2/NP_057450.2**. (schrauwen2012amutationin pages 1-2, koohiyan2019anovelpathogenic pages 2-3)
* **MeSH:** no disease-specific MeSH term was identified. Use the broader **Hearing Loss, Sensorineural** where appropriate; ClinicalTrials.gov maps the registry to **Hearing Loss, D034381**. (NCT06680934 chunk 1)
* **ICD-10/ICD-11:** there is no CABP2-specific billing code. Code the clinical hearing phenotype under the applicable bilateral sensorineural hearing-loss category and retain the molecular diagnosis separately. Exact national ICD-10-CM/ICD-11 coding should be jurisdictionally validated.
* **Orphanet:** no confidently verified disease-specific Orphanet identifier was recovered; do not assign one without checking the current Orphanet release.

This report is based on **aggregated disease-level literature and registry resources**, not individual EHR data. Nevertheless, the human evidence itself consists largely of family-level case ascertainment, pedigrees, audiograms, and molecular testing rather than population cohorts.

## 2. Etiology, risk, protection, and environment

### Causal factor

The necessary cause is **biallelic germline CABP2 dysfunction**. Established disease mechanisms include nonsense-mediated decay, splice-induced truncation, defective Ca²⁺ binding, reduced protein abundance, and impaired modulation of CaV1.3 channels. Heterozygous relatives and heterozygous mice were reported as hearing-normal, supporting recessive inheritance. (schrauwen2012amutationin pages 1-2, picher2017ca2+bindingprotein2 pages 1-2, schrauwen2012amutationin pages 6-7)

### Genetic risk factors

Reported variants with primary evidence include:

1. **c.637+1G>T; p.Phe164Serfs*4**: splice-donor disruption, predicted exon 6 skipping and loss of EF hands 3–4; found in three consanguineous Iranian families on a shared 0.52-Mb haplotype, consistent with a founder allele. It was absent from 100 Iranian controls. The truncated protein had approximately tenfold lower expression and less effective CaV1.3 regulation in experimental assays. (schrauwen2012amutationin pages 7-8, schrauwen2012amutationin pages 6-7, schrauwen2012amutationin pages 3-4)
2. **c.466G>T; p.Glu156Ter** (reported as p.E156X): homozygous in two Northern Italian siblings; likely nonsense-mediated decay. It was absent from 225 White controls and was not represented in ExAC at the time. (picher2017ca2+bindingprotein2 pages 1-2)
3. **c.311G>A; p.Gly104Asp**: homozygous in two affected relatives from a consanguineous Iranian family; classified as pathogenic by the reporting authors under ACMG/AMP criteria, absent from 50 local controls, 1000 Genomes, and ExAC. It affects a conserved EF-hand region, but the retrieved evidence is primarily segregation, rarity, prediction, and structural modeling rather than a direct electrophysiological assay. (koohiyan2019anovelpathogenic pages 4-5, koohiyan2019anovelpathogenic pages 3-4, koohiyan2019anovelpathogenic pages 1-2)
4. **c.590T>C; p.Ile197Thr**: reported in two Egyptian siblings with hearing impairment. Their skeletal/dental DASS phenotype was independently caused by biallelic **LTBP3** variation; the authors described the CABP2-associated hearing phenotype as having a separate transmission mechanism. This is a blended diagnosis, not evidence that CABP2 causes DASS. (nawaz2024brachyolmiadentalanomalies pages 1-2)

Current ClinVar classifications and present-day gnomAD frequencies were not directly retrieved and should be checked variant-by-variant against the current databases before clinical interpretation. No somatic mechanism is implicated.

### Other factors

* **Family history, consanguinity, and founder ancestry** increase the probability of biallelic inheritance; they are ascertainment/risk factors rather than biological triggers.
* No validated susceptibility loci, protective CABP2 alleles, environmental protective factors, modifier genes, epigenetic determinants, or human gene–environment interactions have been established.
* Noise, ototoxic drugs, infection, smoking, diet, alcohol, occupation, age, and sex are not demonstrated causes of DFNB93. Avoiding ordinary acquired auditory injury remains prudent but cannot prevent a congenital CABP2 defect.
* CaBP1 provides partial functional redundancy in mice and is therefore a plausible biological modifier, but no human **CABP1** modifier association has been demonstrated. (oestreicher2024cabp1and2 pages 1-2, oestreicher2024cabp1and2 pages 11-12)

## 3. Phenotypes

### Core auditory phenotype

| Phenotype | Characteristics and evidence | Suggested HPO |
|---|---|---|
| Bilateral sensorineural hearing impairment | Symmetric, prelingual, generally moderate-to-severe; severe loss occurred with p.Gly104Asp | **HP:0000407** Sensorineural hearing impairment; **HP:0000365** Hearing impairment; **HP:0012715** Bilateral hearing impairment |
| Mid-frequency-predominant/U-shaped audiogram | Especially clear in the Italian siblings; hearing was impaired across frequencies but preferentially in the middle range | **HP:0000408** Progressive sensorineural hearing impairment is *not* appropriate unless progression is documented; use an audiogram-shape annotation if available locally |
| Prelingual onset | Reported in Italian and Iranian patients and affected communication | **HP:0011592** Selective mutism is inappropriate; use **HP:0003623** Neonatal onset or **HP:0011463** Childhood onset only when patient-specific age is known; otherwise encode “prelingual onset” textually |
| Auditory synaptopathy physiology | Reduced/abnormal neural responses with potentially preserved otoacoustic emissions, localizing dysfunction downstream of outer-hair-cell amplification | **HP:0012718** Auditory neuropathy spectrum disorder, if supported by the individual’s electrophysiology |
| Speech/communication difficulty | Explicitly reported in the Italian family; expected functional consequence of prelingual hearing loss | **HP:0002167** Speech articulation difficulties or **HP:0000750** Delayed speech and language development only when clinically documented |

The 2017 primary report states that affected siblings had “**prelingual hearing impairment affecting their communication**” and “**symmetrical moderate-to-severe hearing impairment across all frequencies, preferentially affecting the middle-frequency range (‘U shape’).**” (picher2017ca2+bindingprotein2 pages 1-2)

### Frequency, progression, and extra-auditory findings

Reliable percentages cannot be calculated: published families are too few, ascertainment differs, and case reports are not a denominator-based cohort. Bilaterality and prelingual onset appear recurrent, but their penetrance should not be represented as 100% in a knowledge base. Longitudinal progression is unresolved. The mouse double knockout worsened with age, but this must not be translated directly into a human progression rate. (oestreicher2024cabp1and2 pages 7-9)

Comprehensive examinations in the Italian family excluded syndromic features. The original Iranian study performed ophthalmologic and cardiovascular evaluations; CABP2 expression in retina and vestibular hair cells has not translated into a reproducible human retinal, cardiac, or vestibular syndrome. The Egyptian DASS findings belong to the separate LTBP3 diagnosis. (picher2017ca2+bindingprotein2 pages 1-2, schrauwen2012amutationin pages 1-2, nawaz2024brachyolmiadentalanomalies pages 1-2)

### Quality of life

No DFNB93-specific EQ-5D, SF-36, PROMIS, educational, employment, or caregiver-burden study was identified. Likely effects concern speech perception, communication, language acquisition, education, and social participation, but disease-specific effect sizes are unavailable.

## 4. Genetic and molecular information

**CABP2** encodes a calmodulin-related EF-hand Ca²⁺-binding protein. CaBP2 binds/modulates presynaptic L-type **CaV1.3**, whose pore-forming subunit is encoded by **CACNA1D**. CaBP2-alt is the predominant murine cochlear isoform, although rescue studies also used the conventional long isoform. (koohiyan2019anovelpathogenic pages 4-5, oestreicher2024cabp1and2 pages 11-12)

Variant consequences should be represented as follows:

* c.637+1G>T: germline splice loss → frameshift/truncation → loss of C-terminal EF hands, altered Ca²⁺ binding, reduced protein expression, hypomorphic/functional loss.
* c.466G>T: germline nonsense → anticipated NMD → loss of function.
* c.311G>A and c.590T>C: germline missense; likely impaired protein structure/function, but direct variant-specific electrophysiology was not recovered, so “loss of function” should be qualified rather than asserted as experimentally proven.

No validated dominant-negative or gain-of-function CABP2 mechanism, large recurrent deletion, translocation, aneuploidy, repeat expansion, mitochondrial mechanism, somatic mosaicism, germline mosaicism, or disease-specific methylation/chromatin abnormality has been reported. No robust transcriptomic, human single-cell, spatial-transcriptomic, proteomic, metabolomic, or lipidomic disease signature is established.

## 5. Environmental information

DFNB93 is genetic, not infectious, toxic, nutritional, occupational, or lifestyle-mediated. No pathogen, toxin, radiation exposure, pollutant, smoking behavior, diet, exercise pattern, or alcohol exposure is known to trigger it. General hearing conservation and avoidance of ototoxic exposure may preserve residual hearing but are tertiary risk-reduction measures, not disease-specific prevention.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic lesion:** biallelic CABP2 loss or dysfunction reduces effective CaBP2 in cochlear hair cells.
2. **Channel dysregulation:** CaBP2 normally restrains voltage- and/or calcium-dependent inactivation of IHC CaV1.3 channels. Its absence leaves fewer channels available during sustained or repeated depolarization.
3. **Presynaptic failure:** reduced sustained Ca²⁺ entry impairs ribbon-synapse vesicle exocytosis and glutamate release.
4. **Neural coding defect:** SGNs fire less, adapt excessively, and show poorer temporal precision/jitter.
5. **Systems phenotype:** ABR thresholds rise and wave amplitudes fall despite relatively preserved DPOAEs and cochlear mechanics, producing bilateral sensorineural hearing impairment/auditory synaptopathy. (picher2017ca2+bindingprotein2 pages 1-2, brotto2024autosomalrecessivenonsyndromic pages 8-9, picher2017ca2+bindingprotein2 pages 7-8)

The 2012 abstract described the mutant protein as “**a hypofunctional CaBP2 defective in Ca²⁺ sensing and effector regulation in the inner ear**.” (schrauwen2012amutationin pages 1-2)

The latest mechanistic refinement comes from the 2024 eLife Version of Record: CaBP1/2 double-null IHCs exhibited “**strongly enhanced CaV1.3 inactivation, slowed recovery from inactivation and impaired sustained exocytosis**”; the authors concluded that both proteins support “**fast, temporally precise and indefatigable sound encoding**.” (oestreicher2024cabp1and2 pages 1-2)

### Ontology-ready annotations

* **GO biological processes:** calcium ion transmembrane transport; regulation of voltage-gated calcium-channel activity; regulation of membrane depolarization; synaptic vesicle exocytosis; chemical synaptic transmission; sensory perception of sound; calcium-ion homeostasis.
* **GO molecular functions:** calcium-ion binding; voltage-gated calcium-channel regulator activity; protein binding.
* **GO cellular components:** cytosol; presynaptic active zone; ribbon synapse; plasma membrane/voltage-gated calcium-channel complex. Exact GO accessions should be validated in the live GO release.
* **Cell Ontology suggestions:** inner hair cell (**CL term to be release-validated**), outer hair cell, spiral-ganglion neuron/auditory neuron, vestibular hair cell.
* **CHEBI:** calcium(2+) (**CHEBI:29108**) and glutamate should be annotated only as mechanistic entities, not treatments.

No primary metabolic, immune, inflammatory, fibrotic, ischemic, lysosomal, mitochondrial, or apoptotic disease mechanism is established. The major lesion is channel regulation and synaptic transmission, not early hair-cell death.

## 7. Anatomical structures affected

* **Organ/system:** inner ear, specifically the cochlear auditory system; no established secondary-organ involvement.
* **Primary cells:** cochlear IHCs, where CaBP2 strongly regulates CaV1.3; OHC expression occurs but amplification is comparatively preserved. SGN abnormalities are downstream of impaired IHC output. (picher2017ca2+bindingprotein2 pages 2-3)
* **Subcellular site:** presynaptic ribbon active zone, CaV1.3 channel complex, cytosolic Ca²⁺-buffering/modulatory environment, and synaptic-vesicle release machinery.
* **Suggested UBERON:** inner ear; cochlea; organ of Corti/spiral organ; cochlear hair cell layer; spiral ganglion. Validate exact accessions against the current UBERON release.
* **Laterality:** typically bilateral and symmetric in documented patients. (picher2017ca2+bindingprotein2 pages 1-2)

Mouse expression also occurs in vestibular hair cells and retinal cells, but scotopic electroretinography was intact and consistent human vestibular/retinal disease has not been established. (picher2017ca2+bindingprotein2 pages 2-3)

## 8. Temporal development

The best-supported onset is congenital or prelingual, with a chronic, lifelong course. Available reports do not define discrete stages, remission, episodic attacks, or spontaneous recovery. Human longitudinal data are insufficient to label DFNB93 uniformly stable or progressive.

The clinically important intervention window is inferred from preserved early cochlear morphology in mice: development, stereocilia, ribbons, and SGNs remain initially intact, potentially permitting functional rescue before secondary damage. This is a translational hypothesis, not a validated human treatment window. (oestreicher2021cabp2genetherapyrestores pages 7-8, oestreicher2021cabp2genetherapyrestores pages 1-2)

## 9. Inheritance and population

Inheritance is autosomal recessive. If both parents carry the same pathogenic CABP2 allele, each pregnancy has an expected **25% affected, 50% carrier, and 25% non-carrier/unaffected** probability under standard Mendelian assumptions. Male and female siblings have been affected; no sex bias is known.

Evidence supports a founder effect for c.637+1G>T in southern/southwestern Iranian families and identity-by-descent for c.466G>T in the Italian pedigree. Consanguinity was prominent in Iranian and Egyptian reports. (schrauwen2012amutationin pages 1-2, picher2017ca2+bindingprotein2 pages 2-3, nawaz2024brachyolmiadentalanomalies pages 1-2)

There is no defensible prevalence, annual incidence, carrier frequency, geographic prevalence, sex ratio, penetrance estimate, or age distribution. The published families demonstrate occurrence in Iranian, Northern Italian, and Egyptian ancestry but do not establish ethnic restriction. Apparent geographic clustering is heavily affected by consanguinity and ascertainment.

## 10. Diagnostics

### Clinical evaluation

Recommended phenotype definition includes:

1. Age-appropriate pure-tone or visual-reinforcement audiometry, with air and bone conduction.
2. Speech audiometry, including speech-in-noise where feasible.
3. Tympanometry to exclude conductive middle-ear disease.
4. OAEs to evaluate OHC function.
5. ABR, including wave-I amplitude/latency where technically available, to assess auditory-neural transmission.
6. Otologic, vestibular, ophthalmologic, and syndromic review guided by presentation. The dedicated registry uses pure-tone and speech audiometry as primary outcomes and OAEs and ABR as secondary outcomes. (NCT06680934 chunk 1, schrauwen2012amutationin pages 1-2)

A characteristic clue is bilateral symmetric mid-frequency loss with preserved OAEs or unexpectedly abnormal ABR, but neither feature is diagnostic in isolation.

### Molecular diagnosis

A practical sequence is:

* comprehensive hearing-loss multigene panel including **CABP2**, with copy-number analysis;
* exome or genome sequencing if panel testing is negative or the phenotype is blended/atypical;
* confirm candidate variants and phase them by parental/segregation testing;
* interpret under current ACMG/AMP specifications, ClinVar, ClinGen, gnomAD, and phenotype concordance;
* consider RNA analysis for uncertain splice variants where clinically accessible.

WES discovered p.Gly104Asp after GJB2 and several common ARNSHL genes were excluded; exome sequencing also resolved the dual LTBP3/CABP2 diagnosis in the Egyptian family. (koohiyan2019anovelpathogenic pages 2-3, nawaz2024brachyolmiadentalanomalies pages 1-2)

Single-gene CABP2 sequencing is reasonable in a known family or highly characteristic phenotype. WGS may detect noncoding or structural variants missed by exome/panels, but no CABP2-specific diagnostic-yield comparison exists. CMA, conventional karyotyping, FISH, mtDNA sequencing, and repeat-expansion assays are not first-line for isolated suspected DFNB93 unless another clinical indication exists. No blood biomarker, enzyme assay, biopsy, imaging signature, proteomic, metabolomic, epigenomic, or liquid-biopsy test diagnoses DFNB93.

### Differential diagnosis and screening

Differentials include other nonsyndromic hearing-loss genes producing mid-frequency loss (**TECTA**, **STRC**) and auditory synaptopathy genes such as **OTOF**, as well as broader congenital genetic, infectious, structural, and acquired causes. TECTA and CABP2 were specifically considered in the Italian U-shaped-audiogram family. (picher2017ca2+bindingprotein2 pages 1-2)

Universal newborn hearing screening can detect hearing impairment but does not establish CABP2 etiology. Cascade testing should be offered after a familial variant is established. The current natural-history study requires a molecular diagnosis involving biallelic CABP2 variants and audiometry. (NCT06680934 chunk 1)

## 11. Outcome and prognosis

DFNB93 is not known to reduce survival or life expectancy, and no disease-specific mortality has been reported. Five- or ten-year survival statistics are therefore not meaningful. Morbidity is principally auditory and communicative.

Residual hearing may remain in the moderate-to-severe range, but severe hearing loss is documented. Prognostic factors are not validated; plausible candidates—variant class, residual CaBP2 activity, audiometric severity, OAEs, ABR wave I, age, and CaBP1 compensation—remain unproven in humans. No prognostic biomarker or validated risk calculator exists.

Recovery without hearing technology is not documented. Because early anatomy is preserved in mice, functional restoration may be biologically feasible, but human durability and therapeutic window remain unknown. (oestreicher2021cabp2genetherapyrestores pages 7-8, oestreicher2021cabp2genetherapyrestores pages 1-2)

## 12. Treatment and real-world implementation

### Current standard care

There is no approved CABP2-specific pharmacotherapy. Management follows individualized pediatric/adult sensorineural hearing-loss care:

* appropriately fitted hearing aids when audibility and speech benefit are adequate;
* cochlear-implant assessment when severe loss or poor aided speech understanding meets local criteria;
* early speech-language/auditory habilitation, educational accommodations, assistive listening technology, and communication support;
* serial audiology to track thresholds, speech performance, OAEs, and ABR as indicated.

The primary preclinical paper notes that present management of auditory synaptopathies is limited to hearing aids or cochlear implants, but it provides no CABP2-specific response rate. (oestreicher2021cabp2genetherapyrestores pages 1-2)

Suggested NCIT concepts, with identifiers to be release-validated, include **Hearing Aid**, **Cochlear Implantation**, **Speech Therapy**, **Audiologic Rehabilitation**, **Genetic Counseling**, and **Gene Therapy**.

### Experimental gene therapy

In Cabp2-null mice, round-window delivery at postnatal days 5–7 of **AAV2/1-Cabp2** or **AAV-PHP.eB-Cabp2** restored IHC CaV1.3 function and partially improved hearing. Sixteen of 24 treated mice met a reported ≥20-dB improvement criterion at tested frequencies; wave-I amplitude rose from 0.8±0.1 to 1.3±0.2 µV at 80 dB SPL, and PHP.eB produced approximately 98% IHC transduction. (oestreicher2021cabp2genetherapyrestores pages 2-4)

Limitations include partial rather than complete rescue, cross-ear transduction, possible toxicity or physiological disruption from vector/eGFP overexpression, imperfect promoter/dose matching, postnatal mouse delivery, and uncertain human translation. Some treated wild-type mice developed modest threshold/DPOAE abnormalities, emphasizing the importance of cell-specific, physiological expression. (oestreicher2021cabp2genetherapyrestores pages 5-7, oestreicher2021cabp2genetherapyrestores pages 7-8)

No CABP2-directed drug, ASO, siRNA, CRISPR/editing, cell therapy, immunotherapy, or human gene-therapy trial was identified. **NCT06680934 is observational, not therapeutic.**

### Registry implementation

NCT06680934, sponsored by University Medical Center Göttingen, is a recruiting, case-only, non-probability registry targeting 100 participants of any sex and age with biallelic CABP2 variants. It began August 16, 2024, was first posted November 8, 2024, and has an estimated 25-year duration. Registry URL: https://clinicaltrials.gov/study/NCT06680934; study site: http://www.auditory-neuroscience.uni-goettingen.de/cabp2_registry_en.html. (NCT06680934 chunk 1)

## 13. Prevention

Primary prevention by lifestyle, vaccine, or medication is not possible for an inherited biallelic disorder. Reproductive prevention options after identifying familial variants include carrier testing, cascade screening, prenatal diagnosis, and preimplantation genetic testing, following nondirective genetic counseling and local ethical/legal standards.

Secondary prevention consists of newborn hearing screening, prompt diagnostic audiology, early molecular diagnosis, and rapid habilitation during language-development windows. Tertiary prevention includes hearing conservation, avoidance of unnecessary ototoxins, optimized hearing technology, speech-language services, and educational support. No immunization or pharmacologic prophylaxis specifically prevents DFNB93.

## 14. Other species and natural disease

The principal comparative species is **Mus musculus** (NCBI Taxonomy **10090**) with ortholog **Cabp2**. CaBP2’s cochlear expression and calcium-channel regulatory role are conserved sufficiently for mouse models to reproduce the human synaptopathy mechanism. No naturally occurring companion-animal, livestock, or wildlife CABP2-associated hearing disorder, breed predisposition, VBO term, cross-species transmission, or zoonotic potential was identified. DFNB93 is noninfectious and cannot be transmitted between animals or humans.

## 15. Model organisms and experimental systems

### Cabp2-null mouse

The KOMP-derived **Cabp2LacZ/LacZ** model replaces/disrupts Cabp2 exons and shows elevated ABR thresholds, reduced amplitudes, prolonged latencies, and reduced/jittered SGN firing, with normal DPOAEs and preserved IHC/OHC and synaptic anatomy. It is suited to studying IHC CaV1.3 gating, ribbon-synapse transmission, neural temporal coding, and gene replacement. (picher2017ca2+bindingprotein2 pages 7-8, picher2017ca2+bindingprotein2 pages 2-3)

### Cabp1/Cabp2 double knockout

This model exposes functional redundancy. At 3–4 weeks, click thresholds were **59±2 versus 30±2 dB SPL** in controls; by 7–13 weeks they were **68±5 versus 30±1 dB SPL**. Ribbon number remained essentially unchanged (**12.8±0.8 versus 12.9±0.2 synapses/IHC**), while SGN adaptation increased markedly (**12.5±3.0 versus 3.4±0.2**). These data localize failure to synaptic physiology rather than synapse loss. (oestreicher2024cabp1and2 pages 11-12, oestreicher2024cabp1and2 pages 7-9)

### Cellular/in-vitro systems

HEK293-derived heterologous expression, calcium-binding calorimetry, cochlear explants, perforated-patch electrophysiology, exocytosis measurements, immunohistochemistry, ABR/DPOAE, and in-vivo SGN recordings have been used. Such systems isolate channel effects but cannot reproduce the complete human tonotopic, developmental, and perceptual phenotype.

### Limitations

The Cabp2 single knockout has a milder SGN phenotype than many affected humans; mice have different audible-frequency ranges, developmental timing, and CaBP redundancy. The double knockout models combined CABP1/CABP2 deficiency rather than human DFNB93 itself and may exaggerate severity. AAV rescue in neonatal mice does not establish safety, dose, surgical route, durability, or efficacy in humans. (oestreicher2024cabp1and2 pages 13-14)

## Evidence gaps and expert interpretation

The authoritative interpretation emerging from the primary studies is that DFNB93 is a **function-first, structurally preserved presynaptic disorder**, making it unusually attractive for gene augmentation. That conclusion is supported by preserved OAEs/anatomy, reversible CaV1.3 inactivation, and successful mouse rescue—not by human therapeutic data. (brotto2024autosomalrecessivenonsyndromic pages 8-9, oestreicher2021cabp2genetherapyrestores pages 1-2)

Major knowledge-base fields should presently be marked **unknown** rather than negative: population prevalence and incidence; age-dependent penetrance; longitudinal progression; carrier frequency; validated modifier genes; environmental interaction; disease-specific quality-of-life scores; hearing-aid/cochlear-implant outcomes; human therapeutic window; and variant-specific treatment response. The dedicated registry is designed to close several of these gaps by collecting molecular diagnoses, pure-tone and speech audiometry, OAEs, and ABRs. (NCT06680934 chunk 1)

## Principal sources and publication dates

* Schrauwen I, et al. “A Mutation in CABP2, Expressed in Cochlear Hair Cells, Causes Autosomal-Recessive Hearing Impairment.” *American Journal of Human Genetics*. **October 5, 2012**. DOI/URL: https://doi.org/10.1016/j.ajhg.2012.08.018. (schrauwen2012amutationin pages 1-2)
* Picher MM, et al. “Ca²⁺-binding protein 2 inhibits Ca²⁺-channel inactivation in mouse inner hair cells.” *PNAS*. **February 2017**. DOI/URL: https://doi.org/10.1073/pnas.1617533114. (picher2017ca2+bindingprotein2 pages 2-3)
* Koohiyan M, et al. “A Novel Pathogenic Variant in the CABP2 Gene Causes Severe Nonsyndromic Hearing Loss in a Consanguineous Iranian Family.” *Audiology and Neurotology*. **October 2019**. DOI/URL: https://doi.org/10.1159/000502251. (koohiyan2019anovelpathogenic pages 4-5)
* Oestreicher D, et al. “Cabp2-Gene Therapy Restores Inner Hair Cell Calcium Currents and Improves Hearing in a DFNB93 Mouse Model.” *Frontiers in Molecular Neuroscience*. **August 2021**. DOI/URL: https://doi.org/10.3389/fnmol.2021.689415. (oestreicher2021cabp2genetherapyrestores pages 1-2)
* Nawaz H, et al. “Brachyolmia, dental anomalies and short stature (DASS): Phenotype and genotype analyses of Egyptian and Pakistani patients.” *Heliyon* 10:e23688; available online **December 14, 2023**, 2024 issue. DOI/URL: https://doi.org/10.1016/j.heliyon.2023.e23688. (nawaz2024brachyolmiadentalanomalies pages 1-2)
* Oestreicher D, et al. “CaBP1 and 2 enable sustained CaV1.3 calcium currents and synaptic transmission in inner hair cells.” *eLife* 13:RP93646, Version of Record **December 24, 2024**. DOI/URL: https://doi.org/10.7554/eLife.93646. (oestreicher2024cabp1and2 pages 1-2)
* ClinicalTrials.gov. “CABP2 Patient Registry and Natural History Study.” **NCT06680934**, first posted **November 8, 2024**: https://clinicaltrials.gov/study/NCT06680934. The registry record also links a 2025 review, PMID **40927552**. (NCT06680934 chunk 1)

References

1. (picher2017ca2+bindingprotein2 pages 1-2): Maria Magdalena Picher, Anna Gehrt, Sandra Meese, Aleksandra Ivanovic, Friederike Predoehl, SangYong Jung, Isabelle Schrauwen, Alberto Giulio Dragonetti, Roberto Colombo, Guy Van Camp, Nicola Strenzke, and Tobias Moser. Ca2+-binding protein 2 inhibits ca2+-channel inactivation in mouse inner hair cells. Proceedings of the National Academy of Sciences, 114:E1717-E1726, Feb 2017. URL: https://doi.org/10.1073/pnas.1617533114, doi:10.1073/pnas.1617533114. This article has 74 citations and is from a highest quality peer-reviewed journal.

2. (schrauwen2012amutationin pages 1-2): Isabelle Schrauwen, Sarah Helfmann, Akira Inagaki, Friederike Predoehl, Mohammad Amin Tabatabaiefar, Maria Magdalena Picher, Manou Sommen, Celia Zazo Seco, Jaap Oostrik, Hannie Kremer, Annelies Dheedene, Charlotte Claes, Erik Fransen, Morteza Hashemzadeh Chaleshtori, Paul Coucke, Amy Lee, Tobias Moser, and Guy Van Camp. A mutation in cabp2, expressed in cochlear hair cells, causes autosomal-recessive hearing impairment. American journal of human genetics, 91 4:636-45, Oct 2012. URL: https://doi.org/10.1016/j.ajhg.2012.08.018, doi:10.1016/j.ajhg.2012.08.018. This article has 154 citations and is from a highest quality peer-reviewed journal.

3. (picher2017ca2+bindingprotein2 pages 2-3): Maria Magdalena Picher, Anna Gehrt, Sandra Meese, Aleksandra Ivanovic, Friederike Predoehl, SangYong Jung, Isabelle Schrauwen, Alberto Giulio Dragonetti, Roberto Colombo, Guy Van Camp, Nicola Strenzke, and Tobias Moser. Ca2+-binding protein 2 inhibits ca2+-channel inactivation in mouse inner hair cells. Proceedings of the National Academy of Sciences, 114:E1717-E1726, Feb 2017. URL: https://doi.org/10.1073/pnas.1617533114, doi:10.1073/pnas.1617533114. This article has 74 citations and is from a highest quality peer-reviewed journal.

4. (NCT06680934 chunk 1): Tobias Moser. CABP2 Patient Registry and Natural History Study. University Medical Center Goettingen. 2024. ClinicalTrials.gov Identifier: NCT06680934

5. (oestreicher2024cabp1and2 pages 1-2): David Oestreicher, Shashank Chepurwar, Kathrin Kusch, Vladan Rankovic, Sangyong Jung, Nicola Strenzke, and Tina Pangrsic. Cabp1 and 2 enable sustained cav1.3 calcium currents and synaptic transmission in inner hair cells. Aug 2024. URL: https://doi.org/10.7554/elife.93646.2, doi:10.7554/elife.93646.2. This article has 12 citations.

6. (oestreicher2024cabp1and2 pages 11-12): David Oestreicher, Shashank Chepurwar, Kathrin Kusch, Vladan Rankovic, Sangyong Jung, Nicola Strenzke, and Tina Pangrsic. Cabp1 and 2 enable sustained cav1.3 calcium currents and synaptic transmission in inner hair cells. Aug 2024. URL: https://doi.org/10.7554/elife.93646.2, doi:10.7554/elife.93646.2. This article has 12 citations.

7. (schrauwen2012amutationin pages 7-8): Isabelle Schrauwen, Sarah Helfmann, Akira Inagaki, Friederike Predoehl, Mohammad Amin Tabatabaiefar, Maria Magdalena Picher, Manou Sommen, Celia Zazo Seco, Jaap Oostrik, Hannie Kremer, Annelies Dheedene, Charlotte Claes, Erik Fransen, Morteza Hashemzadeh Chaleshtori, Paul Coucke, Amy Lee, Tobias Moser, and Guy Van Camp. A mutation in cabp2, expressed in cochlear hair cells, causes autosomal-recessive hearing impairment. American journal of human genetics, 91 4:636-45, Oct 2012. URL: https://doi.org/10.1016/j.ajhg.2012.08.018, doi:10.1016/j.ajhg.2012.08.018. This article has 154 citations and is from a highest quality peer-reviewed journal.

8. (schrauwen2012amutationin pages 3-4): Isabelle Schrauwen, Sarah Helfmann, Akira Inagaki, Friederike Predoehl, Mohammad Amin Tabatabaiefar, Maria Magdalena Picher, Manou Sommen, Celia Zazo Seco, Jaap Oostrik, Hannie Kremer, Annelies Dheedene, Charlotte Claes, Erik Fransen, Morteza Hashemzadeh Chaleshtori, Paul Coucke, Amy Lee, Tobias Moser, and Guy Van Camp. A mutation in cabp2, expressed in cochlear hair cells, causes autosomal-recessive hearing impairment. American journal of human genetics, 91 4:636-45, Oct 2012. URL: https://doi.org/10.1016/j.ajhg.2012.08.018, doi:10.1016/j.ajhg.2012.08.018. This article has 154 citations and is from a highest quality peer-reviewed journal.

9. (koohiyan2019anovelpathogenic pages 4-5): Mahbobeh Koohiyan, Mohammad Reza Noori-Daloii, Morteza Hashemzadeh-Chaleshtori, Mansoor Salehi, Hamidreza Abtahi, and Mohammad Amin Tabatabaiefar. A novel pathogenic variant in the cabp2 gene causes severe nonsyndromic hearing loss in a consanguineous iranian family. Audiology and Neurotology, 24:258-263, Oct 2019. URL: https://doi.org/10.1159/000502251, doi:10.1159/000502251. This article has 18 citations.

10. (koohiyan2019anovelpathogenic pages 3-4): Mahbobeh Koohiyan, Mohammad Reza Noori-Daloii, Morteza Hashemzadeh-Chaleshtori, Mansoor Salehi, Hamidreza Abtahi, and Mohammad Amin Tabatabaiefar. A novel pathogenic variant in the cabp2 gene causes severe nonsyndromic hearing loss in a consanguineous iranian family. Audiology and Neurotology, 24:258-263, Oct 2019. URL: https://doi.org/10.1159/000502251, doi:10.1159/000502251. This article has 18 citations.

11. (koohiyan2019anovelpathogenic pages 1-2): Mahbobeh Koohiyan, Mohammad Reza Noori-Daloii, Morteza Hashemzadeh-Chaleshtori, Mansoor Salehi, Hamidreza Abtahi, and Mohammad Amin Tabatabaiefar. A novel pathogenic variant in the cabp2 gene causes severe nonsyndromic hearing loss in a consanguineous iranian family. Audiology and Neurotology, 24:258-263, Oct 2019. URL: https://doi.org/10.1159/000502251, doi:10.1159/000502251. This article has 18 citations.

12. (nawaz2024brachyolmiadentalanomalies pages 1-2): Hamed Nawaz, Asia Parveen, Sher Alam Khan, Abul Khair Zalan, Muhammad Adnan Khan, Noor Muhammad, Nehal F. Hassib, Mostafa I. Mostafa, Rasha M. Elhossini, Nehal Nabil Roshdy, Asmat Ullah, Amina Arif, Saadullah Khan, Ole Ammerpohl, and Naveed Wasif. Brachyolmia, dental anomalies and short stature (dass): phenotype and genotype analyses of egyptian and pakistani patients. Jan 2024. URL: https://doi.org/10.1016/j.heliyon.2023.e23688, doi:10.1016/j.heliyon.2023.e23688. This article has 4 citations.

13. (picher2017ca2+bindingprotein2 pages 7-8): Maria Magdalena Picher, Anna Gehrt, Sandra Meese, Aleksandra Ivanovic, Friederike Predoehl, SangYong Jung, Isabelle Schrauwen, Alberto Giulio Dragonetti, Roberto Colombo, Guy Van Camp, Nicola Strenzke, and Tobias Moser. Ca2+-binding protein 2 inhibits ca2+-channel inactivation in mouse inner hair cells. Proceedings of the National Academy of Sciences, 114:E1717-E1726, Feb 2017. URL: https://doi.org/10.1073/pnas.1617533114, doi:10.1073/pnas.1617533114. This article has 74 citations and is from a highest quality peer-reviewed journal.

14. (oestreicher2021cabp2genetherapyrestores pages 2-4): David Oestreicher, Maria Magdalena Picher, Vladan Rankovic, Tobias Moser, and Tina Pangrsic. Cabp2-gene therapy restores inner hair cell calcium currents and improves hearing in a dfnb93 mouse model. Frontiers in Molecular Neuroscience, Aug 2021. URL: https://doi.org/10.3389/fnmol.2021.689415, doi:10.3389/fnmol.2021.689415. This article has 28 citations.

15. (oestreicher2021cabp2genetherapyrestores pages 5-7): David Oestreicher, Maria Magdalena Picher, Vladan Rankovic, Tobias Moser, and Tina Pangrsic. Cabp2-gene therapy restores inner hair cell calcium currents and improves hearing in a dfnb93 mouse model. Frontiers in Molecular Neuroscience, Aug 2021. URL: https://doi.org/10.3389/fnmol.2021.689415, doi:10.3389/fnmol.2021.689415. This article has 28 citations.

16. (oestreicher2021cabp2genetherapyrestores pages 7-8): David Oestreicher, Maria Magdalena Picher, Vladan Rankovic, Tobias Moser, and Tina Pangrsic. Cabp2-gene therapy restores inner hair cell calcium currents and improves hearing in a dfnb93 mouse model. Frontiers in Molecular Neuroscience, Aug 2021. URL: https://doi.org/10.3389/fnmol.2021.689415, doi:10.3389/fnmol.2021.689415. This article has 28 citations.

17. (oestreicher2021cabp2genetherapyrestores pages 1-2): David Oestreicher, Maria Magdalena Picher, Vladan Rankovic, Tobias Moser, and Tina Pangrsic. Cabp2-gene therapy restores inner hair cell calcium currents and improves hearing in a dfnb93 mouse model. Frontiers in Molecular Neuroscience, Aug 2021. URL: https://doi.org/10.3389/fnmol.2021.689415, doi:10.3389/fnmol.2021.689415. This article has 28 citations.

18. (oestreicher2024cabp1and2 pages 7-9): David Oestreicher, Shashank Chepurwar, Kathrin Kusch, Vladan Rankovic, Sangyong Jung, Nicola Strenzke, and Tina Pangrsic. Cabp1 and 2 enable sustained cav1.3 calcium currents and synaptic transmission in inner hair cells. Aug 2024. URL: https://doi.org/10.7554/elife.93646.2, doi:10.7554/elife.93646.2. This article has 12 citations.

19. (oestreicher2024cabp1and2 pages 13-14): David Oestreicher, Shashank Chepurwar, Kathrin Kusch, Vladan Rankovic, Sangyong Jung, Nicola Strenzke, and Tina Pangrsic. Cabp1 and 2 enable sustained cav1.3 calcium currents and synaptic transmission in inner hair cells. Aug 2024. URL: https://doi.org/10.7554/elife.93646.2, doi:10.7554/elife.93646.2. This article has 12 citations.

20. (koohiyan2019anovelpathogenic pages 2-3): Mahbobeh Koohiyan, Mohammad Reza Noori-Daloii, Morteza Hashemzadeh-Chaleshtori, Mansoor Salehi, Hamidreza Abtahi, and Mohammad Amin Tabatabaiefar. A novel pathogenic variant in the cabp2 gene causes severe nonsyndromic hearing loss in a consanguineous iranian family. Audiology and Neurotology, 24:258-263, Oct 2019. URL: https://doi.org/10.1159/000502251, doi:10.1159/000502251. This article has 18 citations.

21. (schrauwen2012amutationin pages 6-7): Isabelle Schrauwen, Sarah Helfmann, Akira Inagaki, Friederike Predoehl, Mohammad Amin Tabatabaiefar, Maria Magdalena Picher, Manou Sommen, Celia Zazo Seco, Jaap Oostrik, Hannie Kremer, Annelies Dheedene, Charlotte Claes, Erik Fransen, Morteza Hashemzadeh Chaleshtori, Paul Coucke, Amy Lee, Tobias Moser, and Guy Van Camp. A mutation in cabp2, expressed in cochlear hair cells, causes autosomal-recessive hearing impairment. American journal of human genetics, 91 4:636-45, Oct 2012. URL: https://doi.org/10.1016/j.ajhg.2012.08.018, doi:10.1016/j.ajhg.2012.08.018. This article has 154 citations and is from a highest quality peer-reviewed journal.

22. (brotto2024autosomalrecessivenonsyndromic pages 8-9): Davide Brotto, Marco Greggio, Cosimo De Filippis, and Patrizia Trevisi. Autosomal recessive non-syndromic deafness: is aav gene therapy a real chance? Audiology Research, 14:239-253, Feb 2024. URL: https://doi.org/10.3390/audiolres14020022, doi:10.3390/audiolres14020022. This article has 8 citations.

## Artifacts

- [Edison artifact artifact-00](Autosomal_Recessive_Nonsyndromic_Hearing_Loss_93-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 12 |
| Resolved | 12 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013963` (2 mentions) - the report calls it "if available"; MONDO calls it **autosomal recessive nonsyndromic hearing loss 93**