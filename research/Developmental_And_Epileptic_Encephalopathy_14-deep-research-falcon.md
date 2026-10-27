---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-07T02:50:19.046252'
end_time: '2026-09-07T03:03:28.816758'
duration_seconds: 789.77
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Developmental and Epileptic Encephalopathy 14
  mondo_id: MONDO:0013989
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 34
reference_validation:
  total_references: 15
  verified: 15
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 15
  on_topic: 11
  validator_version: 0.2.1
term_validation:
  total_terms: 33
  verified: 32
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0013989
    reported_labels:
    - if available
    ontology_label: developmental and epileptic encephalopathy, 14
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Developmental_And_Epileptic_Encephalopathy_14-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Developmental and Epileptic Encephalopathy 14
- **MONDO ID:** MONDO:0013989 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Developmental and Epileptic Encephalopathy 14** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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
- **Disease Name:** Developmental and Epileptic Encephalopathy 14
- **MONDO ID:** MONDO:0013989 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Developmental and Epileptic Encephalopathy 14** covering all of the
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

**Present this section as an ordered causal chain first, then the detail below.**
Open with a numbered sequence of mechanistic steps running from the initiating
lesion (mutation, exposure, infection) to the clinical manifestation, one step per
line, each naming what it causes next. State the causal verb explicitly ("leads
to", "results in") and say where a step is inferred rather than demonstrated.
Where the mechanism branches, show the branch. The categories below are a
checklist of what to cover within those steps, not the organizing structure —
a step may draw on several of them, and a category may contribute to several
steps.

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


# Developmental and Epileptic Encephalopathy 14 (DEE14): Research Report

## Executive summary and evidence scope

Developmental and epileptic encephalopathy 14 (DEE14) is a rare, usually severe, monogenic potassium-channel disorder caused predominantly by heterozygous gain-of-function variants in **KCNT1**. Its characteristic presentation is epilepsy of infancy with migrating focal seizures (EIMFS), although KCNT1 variants also cause non-EIMFS DEE and milder focal epilepsies. These categories overlap genetically but should not be treated as clinically interchangeable. Open Targets links MONDO:0013989 specifically to KCNT1 (ENSG00000107147), supported by human genetic literature including PMID 23086397, 26993267, and 27864847. (OpenTargets Search: developmental and epileptic encephalopathy 14-KCNT1)

The evidence base remains limited by rarity, retrospective ascertainment, phenotype mixing, and small treatment cohorts. The best quantitative sources are a 27-child multicentre cohort, a 248-person KCNT1-spectrum study, a 2023 genetic-DEE status-epilepticus study, and a 2024 treatment systematic review. The compact evidence summary below distinguishes disease-specific evidence from broader KCNT1-spectrum observations.

| Domain | Best-supported finding | Quantitative evidence | Evidence type/limitations |
|---|---|---|---|
| Identity/genetics | DEE14 is an autosomal-dominant **KCNT1** channelopathy (MONDO:0013989; OMIM 614959), usually caused by heterozygous gain-of-function variants; most severe infantile cases are de novo. | In a 27-child cohort, 23/24 tested variants (96%) were de novo. A 248-person series comprised 152 EIMFS, 37 other DEE, 53 sleep-related hypermotor epilepsy, and 6 other phenotypes; all reported variants were missense except one in-frame deletion. | Curated disease-target evidence plus clinical cohorts. The broader KCNT1 spectrum is not synonymous with DEE14, and recurrent variants show variable expressivity. (OpenTargets Search: developmental and epileptic encephalopathy 14-KCNT1, borlot2020kcnt1‐relatedepilepsyan pages 1-2, carvill1993kcnt1relatedepilepsy pages 10-13) |
| Phenotype/onset | The characteristic presentation is epilepsy of infancy with migrating focal seizures (EIMFS): neonatal or early-infantile focal seizures that migrate between regions, become frequent or nearly continuous, resist medication, and accompany developmental plateau, regression, hypotonia, and profound impairment. | Onset ranged from day 1 to 6 months in the 27-child cohort; 48.1% plateaued developmentally at seizure onset, approximately two-thirds had EIMFS, and 48.1% had focal tonic seizures. | Multicenter pediatric cohort and curated clinical review. Frequencies vary by referral setting and phenotype definition. (borlot2020kcnt1‐relatedepilepsyan pages 1-2, carvill1993kcnt1relatedepilepsy pages 3-6, carvill1993kcnt1relatedepilepsy pages 1-3) |
| EEG/MRI | EEG typically demonstrates multifocal ictal discharges that migrate between hemispheres or cortical regions. MRI may initially be normal, but delayed myelination, thin corpus callosum, cerebral or cerebellar atrophy, and other volume-loss patterns occur. | MRI was abnormal in 60% of the 27-child cohort. A 2023 single case had left frontal-central interictal and left temporal ictal activity with posterior periventricular or parietal volume loss and myelin injury. | Cohort imaging plus a confounded single case carrying pathogenic variants in three genes; the latter cannot isolate KCNT1 effects. (borlot2020kcnt1‐relatedepilepsyan pages 1-2, carvill1993kcnt1relatedepilepsy pages 3-6, zeka2023casereportdiagnosis pages 1-2) |
| Mechanism | Pathogenic gain of KNa1.1 current increases resting or subthreshold potassium conductance, particularly in inhibitory neurons, reducing interneuron firing and producing circuit disinhibition, network hyperexcitability, and seizures. | Y796H increased KNa current 3–11-fold in heterologous systems. Among 14 variants tested in another study, all except T314A increased current; resting open probability correlated with neurological severity. | Electrophysiology and knock-in mouse evidence strongly support gain of function and interneuron vulnerability; some downstream links remain mechanistic inference and may differ by variant or cell maturity. (rychkov2022functionaleffectsof pages 1-2, shore2020reducedgabaergicneuron pages 1-4, scheffer2024developmentalandepileptic pages 4-6) |
| Prognosis/burden | Disease is generally lifelong and highly disabling; seizures may improve with age in some patients, but profound developmental impairment often persists. Status epilepticus and premature death are important risks. | Four of 27 children died (15%; none classified as SUDEP). In a separate genetic-DEE study, 6/10 KCNT1 participants had convulsive status epilepticus (60%; 95% CI 26–88). Caregiver interviews reported impaired self-care in 12/12 families and schooling effects in 10/12. | Small retrospective cohorts and 12 caregiver interviews. No reliable disease-specific survival curve, life expectancy, or KCNT1-specific SUDEP rate is available. (donnan2023ratesofstatus pages 1-2, lafferty2024adiseaseconceptual pages 1-8, borlot2020kcnt1‐relatedepilepsyan pages 1-2) |
| Treatment | No approved disease-modifying therapy was established in the gathered 2023–2024 literature. Conventional antiseizure medications often have limited benefit; ketogenic diet, cannabidiol, and quinidine can help subsets. Quinidine requires ECG and QT monitoring because responses are unpredictable and arrhythmia risk can be serious. | A 2024 review of 43 studies and 197 patients found, in its other-DEE subgroup, benefit with ketogenic diet in 4/7, cannabidiol in 1/2, and quinidine in 6/9. In broader retrospective data, at least 50% seizure-reduction rates were 26.0% for quinidine and 43.5% for ketogenic therapy. | Systematic review dominated by case reports or series and heterogeneous response definitions, polytherapy, and short follow-up; estimates are low certainty and not exclusively DEE14. (gras2024efficacyofanti‐seizure pages 1-2, lin2022efficacyofantiseizure pages 1-2, gras2024efficacyofanti‐seizure pages 12-13) |
| Diagnostics | Diagnosis requires compatible epilepsy and developmental findings plus a pathogenic or likely pathogenic **KCNT1** variant; phenotype or EEG alone is insufficient, and a VUS is non-diagnostic. Early multigene-panel, trio-exome, or genome testing is appropriate because EIMFS and DEE are genetically heterogeneous. | In one 400-patient early-onset epilepsy or severe-delay panel study, 71/400 (18%) received a molecular diagnosis; yield was 39% when seizures began in the first two months, and KCNT1 variants were found in 3 patients. | Clinical genomic cohort and curated guidance. These are general early-onset epilepsy yields, not KCNT1-specific test sensitivity; sequence testing has historically detected nearly all reported KCNT1 cases, whereas large deletions are not established as a common mechanism. (carvill1993kcnt1relatedepilepsy pages 1-3, carvill1993kcnt1relatedepilepsy pages 6-8, carvill1993kcnt1relatedepilepsy pages 10-13) |
| Trials | Prospective natural-history data collection has been implemented; targeted molecular therapies entered clinical development only after 2024 in the retrieved registry records. | NCT04924153 was a completed prospective observational study with 35 participants and 12-month seizure, adaptive-function, sleep, and quality-of-life outcomes. Post-2024 records include intrathecal S230815 (NCT07227857; phase Ib/II; target n=20; start 24 Nov 2025) and oral ABS-1230 (NCT07600736; phase 1b/2; target n=55; start 18 May 2026). | Registry data, not efficacy results. The two interventional trials began after the requested 2023–2024 priority window and were recruiting as of the retrieved records. (NCT04924153 chunk 1, NCT07600736 chunk 1, NCT07227857 chunk 1) |


*Table: Compact evidence-grade synthesis of the best-supported genetic, clinical, mechanistic, diagnostic, therapeutic, and trial findings for KCNT1-related DEE14. Quantitative findings are paired with limitations to prevent broader KCNT1 or general-DEE evidence from being misclassified as disease-specific.*

## 1. Disease information

### Definition and identifiers

DEE14 is an early-onset developmental and epileptic encephalopathy in which a pathogenic **KCNT1** variant contributes directly to neuronal dysfunction, while recurrent epileptic activity may add further developmental impairment. The classic electroclinical syndrome is EIMFS: focal seizures arise independently in different cortical regions and migrate sequentially or simultaneously between hemispheres, typically with developmental plateau or regression and marked drug resistance. The older terms “malignant migrating partial seizures of infancy” and “migrating partial epilepsy of infancy” were replaced by EIMFS terminology. (carvill1993kcnt1relatedepilepsy pages 3-6, carvill1993kcnt1relatedepilepsy pages 1-3, carvill1993kcnt1relatedepilepsy pages 6-8)

Key identifiers and names are:

- **MONDO:** MONDO:0013989.
- **OMIM phenotype:** 614959.
- **Causal gene:** **KCNT1**, OMIM 608167; chromosome 9q34.3.
- **Synonyms:** developmental and epileptic encephalopathy 14; DEE14; early infantile epileptic encephalopathy 14; EIEE14; KCNT1-related developmental and epileptic encephalopathy; KCNT1 encephalopathy. EIMFS and its historical names describe the common syndrome, not every DEE14 patient.
- **Orphanet:** disease-specific mapping should be verified against the current Orphanet release; EIMFS has an Orphanet concept, but a separate DEE14 code was not established in the retrieved evidence.
- **ICD-10/ICD-11 and MeSH:** no uniquely specific DEE14 code was identified. Coding generally uses developmental/epileptic encephalopathy, intractable epilepsy, or focal-seizure categories plus the molecular diagnosis.

Most information summarized here is **aggregated disease-level evidence** from curated resources and cohorts. The 2023 Zeka report is an individual-patient observation confounded by pathogenic variants in **KCNT1, ACADM**, and **CHD4**, and therefore cannot define isolated DEE14. (zeka2023casereportdiagnosis pages 1-2)

## 2. Etiology

### Causal factor

The primary cause is a germline pathogenic or likely pathogenic **KCNT1** variant. Most severe infantile cases are heterozygous and de novo. In one international cohort, 23/24 tested cases (96%) were de novo. Rare inherited cases, parental somatic/germline mosaicism, and unusual homozygous presentations have been reported. (borlot2020kcnt1‐relatedepilepsyan pages 1-2, carvill1993kcnt1relatedepilepsy pages 10-13)

Most pathogenic variants are missense substitutions that increase KNa1.1 current. In the largest spectrum analysis, 248 affected individuals included 152 EIMFS, 37 non-EIMFS DEE, 53 sleep-related hypermotor epilepsy (SHE), and six other phenotypes; variants were missense except for one in-frame deletion. Recurrent variants can produce markedly different phenotypes, demonstrating variable expressivity and limiting simple genotype–phenotype prediction. (rychkov2022functionaleffectsof pages 1-2, carvill1993kcnt1relatedepilepsy pages 13-16)

### Risk factors

- **Genetic:** a pathogenic KCNT1 allele is the decisive risk factor. Recurrent examples include p.Gly288Ser, p.Arg398Gln, p.Arg474His/Gln, p.Tyr796His, p.Met896Ile, p.Arg928Cys, p.Pro924Leu, and p.Ala934Thr. Variant location alone does not reliably predict severity, although SHE variants show relative enrichment around RCK2. (borlot2020kcnt1‐relatedepilepsyan pages 1-2, milligan2014kcnt1gainof pages 1-3, cole2021functionandpharmacological pages 36-39)
- **Family history:** often absent because variants are de novo. A mildly affected or mosaic parent remains possible.
- **Environmental/lifestyle/infectious:** no toxin, diet, infection, sex, or lifestyle exposure is established as a primary risk factor for DEE14.
- **Modifiers:** recurrent variants yielding different syndromes imply genetic-background, developmental, cell-type, or stochastic modifiers, but no validated human modifier gene is currently available for clinical prediction.

### Protective factors and gene–environment interaction

No validated protective human allele, environmental protective exposure, or reproducible KCNT1-specific gene–environment interaction has been demonstrated. Avoiding sleep deprivation, illness-related treatment interruption, and missed medication may reduce seizures generally, but this is seizure management rather than prevention of the Mendelian disorder. The ketogenic diet is therapeutic in some patients, not an established etiologic protective factor. (gras2024efficacyofanti‐seizure pages 13-14, lin2022efficacyofantiseizure pages 1-2)

## 3. Phenotypes

### Core neurological phenotypes

- **Migrating focal seizures** — clinical/electrophysiological sign; usually neonatal or early infantile, often escalating toward nearly continuous seizures by 6–9 months; severe and typically drug-resistant. Suggested HPO: **Seizure (HP:0001250)**, **Focal-onset seizure (HP:0007359)**, and an EIMFS-specific term if supported by the current HPO release. (carvill1993kcnt1relatedepilepsy pages 3-6, carvill1993kcnt1relatedepilepsy pages 1-3)
- **Multiple seizure types** — focal motor, tonic, clonic, myoclonic, generalized tonic-clonic, epileptic spasms, and autonomic seizures may coexist. Focal tonic seizures occurred in 48.1% of the 27-child cohort. Suggested HPO: **Tonic seizure (HP:0032792)**, **Clonic seizure**, **Myoclonic seizure (HP:0002123)**, **Epileptic spasms (HP:0011097)**. (borlot2020kcnt1‐relatedepilepsyan pages 1-2, carvill1993kcnt1relatedepilepsy pages 3-6)
- **Developmental plateau/regression and global developmental delay** — typically begins with or after seizure onset; often profound and persistent. Development plateaued at seizure onset in 48.1% of the 27-child cohort. Suggested HPO: **Global developmental delay (HP:0001263)**, **Developmental regression (HP:0002376)**, **Profound global developmental delay**. (borlot2020kcnt1‐relatedepilepsyan pages 1-2)
- **Intellectual disability and absent/minimal speech** — commonly severe to profound; substantially impairs education, communication, autonomy, and caregiver well-being. Suggested HPO: **Intellectual disability (HP:0001249)**, **Absent speech (HP:0001344)**.
- **Hypotonia evolving to motor impairment** — common in severe EIMFS; spasticity, dyskinesia, dystonia, or other movement disorders can develop. Suggested HPO: **Hypotonia (HP:0001252)**, **Spasticity (HP:0001257)**, **Dystonia (HP:0001332)**, **Abnormality of movement (HP:0100022)**. (carvill1993kcnt1relatedepilepsy pages 3-6, carvill1993kcnt1relatedepilepsy pages 1-3)
- **Acquired microcephaly** — may become evident during infancy rather than being congenital. Suggested HPO: **Postnatal microcephaly (HP:0005484)**. (carvill1993kcnt1relatedepilepsy pages 3-6)
- **Behavioral, psychiatric, and sleep abnormalities** — more prominent and better characterized in KCNT1-SHE than classic EIMFS. These include disturbed sleep, autistic or behavioral features, and cognitive regression. They should be annotated as broader KCNT1-spectrum features unless observed in a specific DEE14 patient. (rychkov2022functionaleffectsof pages 1-2, lafferty2024adiseaseconceptual pages 1-8)

### EEG, imaging, and laboratory phenotypes

EEG classically demonstrates multifocal ictal discharges migrating between cortical regions; background slowing, multifocal spikes, hypsarrhythmia, or burst suppression may occur depending on age and syndrome. Suggested HPO: **EEG with focal epileptiform discharges (HP:0011185)**, **Hypsarrhythmia (HP:0002521)**, **Burst suppression (HP:0010851)**. (carvill1993kcnt1relatedepilepsy pages 3-6)

MRI can be normal initially. Later abnormalities include delayed myelination, thin corpus callosum, cerebral/hippocampal/cerebellar atrophy, and nonspecific volume loss. MRI was abnormal in 60% of the 27-child cohort. Suggested HPO: **Delayed CNS myelination (HP:0002188)**, **Thin corpus callosum (HP:0033725)**, **Cerebral atrophy (HP:0002059)**, **Cerebellar atrophy (HP:0001272)**. (borlot2020kcnt1‐relatedepilepsyan pages 1-2, carvill1993kcnt1relatedepilepsy pages 3-6)

No diagnostic blood, urine, CSF, metabolomic, or protein biomarker is established. Routine biochemical studies are mainly used to exclude treatable mimics.

### Quality-of-life burden

A 2024 interview study of 12 caregivers—nine EIMFS and three SHE—found effects on self-care/daily living in 12/12, schooling in 10/12, hospitalization in 9/12, and socialization in 8/12. All caregivers described effort, emotional, and social burdens; 11/12 reported financial impact and 10/12 effects on caregiver health. This small qualitative sample did not reach concept saturation and was not demographically representative. (lafferty2024adiseaseconceptual pages 1-8, lafferty2024adiseaseconceptual pages 49-53)

## 4. Genetic and molecular information

**KCNT1** encodes potassium sodium-activated channel subfamily T member 1, commonly called KNa1.1, Slack, Slo2.2, or KCa4.1. The long Slack-B isoform has 31 exons and 1,235 amino acids. The tetrameric channel contains six transmembrane segments, an ion-selective pore, intracellular RCK1/RCK2 regulatory domains, and a distal NAD-related regulatory region. (carvill1993kcnt1relatedepilepsy pages 13-16, carvill1993kcnt1relatedepilepsy pages 10-13)

### Variant architecture

- **Typical class:** heterozygous germline missense, usually pathogenic/likely pathogenic and de novo.
- **Less common:** an in-frame deletion; parental mosaicism; rare inherited variants; exceptional homozygous variants.
- **Functional effect:** predominantly gain of function through increased current amplitude, increased open probability near resting potential, altered sodium sensitivity, or shifted voltage dependence. One reported p.Phe932Ile variant showed loss of function, so functional direction should not be assumed for every new variant. (rychkov2022functionaleffectsof pages 1-2, carvill1993kcnt1relatedepilepsy pages 13-16)
- **ACMG interpretation:** pathogenic or likely pathogenic variants support diagnosis; a VUS does not. De novo status, absence or extreme rarity in population databases, phenotype concordance, functional assays, and prior observations are particularly important. (carvill1993kcnt1relatedepilepsy pages 1-3)
- **Population frequency:** pathogenic severe-DEE alleles are expected to be absent or extremely rare in gnomAD. Variant-specific current gnomAD frequencies must be retrieved at annotation time rather than inferred from the syndrome.
- **Somatic versus germline:** disease-causing variants are usually germline; parental somatic/gonadal mosaicism is clinically relevant. Brain-limited somatic KCNT1 mosaicism is not established as a common mechanism.
- **Structural variants/chromosomal abnormalities:** no recurrent KCNT1 deletion, duplication, translocation, inversion, or aneuploidy defines DEE14. Large-deletion testing has lower expected yield than sequence analysis.
- **Epigenetics:** no validated DEE14 methylation episignature or disease-defining chromatin abnormality was found.

Suggested gene identifiers include **HGNC:18865** and NCBI/Ensembl stable identifiers should be verified against current releases before database ingestion.

## 5. Environmental information

DEE14 is not an environmental, lifestyle, occupational, toxic, radiation-associated, or infectious disease. Fever, intercurrent infection, sleep disruption, or medication changes may precipitate seizures in an affected person, but they do not cause the channelopathy. Smoking, alcohol, exercise, and diet have no demonstrated effect on penetrance. No zoonotic or communicable component exists.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A pathogenic **KCNT1** variant **leads to** altered gating of the neuronal sodium-activated potassium channel KNa1.1, usually gain of function.
2. Gain of function **results in** excessive outward K+ current, increased resting/subthreshold conductance, altered afterhyperpolarization, or excessive channel opening near resting membrane potential. This is demonstrated in heterologous cells, patient-derived neurons, and knock-in mice. (shore2020reducedgabaergicneuron pages 1-4, golinski2024genetherapyfor pages 1-2, cole2021functionandpharmacological pages 36-39)
3. Excess current in inhibitory cortical neurons **leads to** increased rheobase and reduced action-potential firing. This is demonstrated in KCNT1 gain-of-function mouse models; relative human cell-type selectivity remains partly inferred. (shore2020reducedgabaergicneuron pages 1-4, scheffer2024developmentalandepileptic pages 4-6)
4. Reduced GABAergic interneuron output **results in** circuit disinhibition and excitation–inhibition imbalance. The reduced interneuron firing is demonstrated; the complete causal bridge to human seizures is strongly supported but partly inferred.
5. Disinhibition and altered synaptic connectivity **lead to** network hyperexcitability, hypersynchrony, migrating multifocal epileptiform activity, and recurrent seizures. (shore2020reducedgabaergicneuron pages 1-4)
6. **Branch A:** recurrent seizures and epileptiform activity **lead to** additional developmental slowing/regression and neurological disability.
7. **Branch B:** primary KCNT1 dysfunction during prenatal and early postnatal neuronal development **likely leads to** developmental impairment independently of seizure burden; this branch is supported by prenatal channel expression, patient-derived neuronal abnormalities, and persistent disability but remains less completely demonstrated in humans. (golinski2024genetherapyfor pages 1-2)
8. Chronic network dysfunction and severe epilepsy **result in** drug resistance, status epilepticus risk, cerebral volume/myelination abnormalities in some patients, and premature mortality.

### Pathway, process, and cell annotations

This is principally an **ion-channel gating and neuronal-circuit disorder**, not a canonical Wnt, MAPK, mTOR, PI3K–AKT, inflammatory, fibrotic, or metabolic-enzyme disease. Relevant GO suggestions are **sodium-activated potassium channel activity**, **potassium ion transmembrane transport**, **regulation of membrane potential**, **action potential**, **neuronal action-potential repolarization**, **synaptic transmission, GABAergic**, and **regulation of neuronal excitability**. Suggested cellular components include **plasma membrane**, **integral component of membrane**, **axon**, and **somatodendritic compartment**.

The principal cell types are neurons, especially cortical GABAergic interneurons and excitatory projection neurons. Suggested Cell Ontology terms include **neuron (CL:0000540)**, **GABAergic neuron (CL:0000617)**, **interneuron (CL:0000099)**, and **glutamatergic neuron (CL:0000679)**.

### Molecular profiling and advanced technologies

A 2024 mouse cortical proteomic study found increased inner-mitochondrial-membrane proteins and increased mitochondrial-crista density primarily in Kcnt1-null mice; Kcnt1 ASO treatment partially corrected proteomic dysregulation in a gain-of-function model. These observations are exploratory and do not establish a human DEE14 metabolic biomarker. No reproducible human transcriptomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or integrated multi-omic signature is established. (burbano2022antisenseoligonucleotidetherapy pages 1-2)

Patient-derived p.Arg474His neurons showed abnormal excitability and afterhyperpolarization; ASO exposure normalized spiking/burst properties in a 2024 preprint. The reported medium afterhyperpolarization changed from −18.2 ± 0.9 mV to −25.1 ± 1.4 mV after ASO treatment (P=0.001). As a preprint, this requires peer-reviewed confirmation. (golinski2024genetherapyfor pages 1-2)

## 7. Anatomical structures affected

- **Primary organ/system:** central nervous system; nervous system.
- **Primary regions:** cerebral cortex and distributed bilateral cortical networks, with seizure onset migrating among regions rather than showing fixed lateralization.
- **Secondary structures:** corpus callosum, cerebral white matter/myelin, hippocampus, and cerebellum may show secondary or developmental abnormalities.
- **Suggested UBERON:** brain (**UBERON:0000955**), cerebral cortex (**UBERON:0000956**), white matter (**UBERON:0002316**), corpus callosum (**UBERON:0002336**), hippocampal formation (**UBERON:0002421**), and cerebellum (**UBERON:0002037**).
- **Subcellular site:** neuronal plasma membrane and membrane-embedded KNa1.1 channel complexes.
- **Lateralization:** generally bilateral/multifocal and migrating. A fixed unilateral abnormality should prompt evaluation for a structural lesion or additional diagnosis.

Rare cardiac conduction abnormalities and pulmonary vascular complications have been reported in the wider KCNT1 spectrum, but they are not defining DEE14 manifestations. (carvill1993kcnt1relatedepilepsy pages 3-6, carvill1993kcnt1relatedepilepsy pages 13-16)

## 8. Temporal development

Onset is congenital in genetic origin but usually **neonatal or early infantile in clinical expression**. In the 27-child cohort, seizures began between day 1 and six months. Seizure frequency often rises rapidly over weeks or months and may become nearly continuous by 6–9 months. Development may be initially normal, already delayed, or plateau/regress around seizure onset. (borlot2020kcnt1‐relatedepilepsyan pages 1-2, carvill1993kcnt1relatedepilepsy pages 3-6)

The course is chronic and lifelong. Some individuals experience declining seizure frequency with age, but this does not reliably reverse profound developmental impairment. There is no validated formal staging system. A practical natural-history framework is: early seizure emergence; escalation/migrating multifocal phase; established drug-resistant encephalopathy; and chronic phase with variable seizure improvement but persistent disability. Early infancy is probably the most important therapeutic window because both channel dysfunction and seizure burden act during rapid brain development. Prenatal and neonatal channel-expression data strengthen this hypothesis, but prenatal treatment remains experimental. (golinski2024genetherapyfor pages 1-2)

## 9. Inheritance and population

DEE14 is generally **autosomal dominant**. Most EIMFS/DEE14 cases are simplex and de novo; if a parent carries the variant, each pregnancy has a 50% transmission probability. A clinically unaffected parent may be mosaic, so recurrence risk is above population baseline even when parental blood testing is negative. Prenatal and preimplantation genetic testing are possible once the familial variant is known. (carvill1993kcnt1relatedepilepsy pages 1-3, carvill1993kcnt1relatedepilepsy pages 10-13)

Penetrance appears high or complete for classic EIMFS, whereas reduced penetrance occurs in milder KCNT1 phenotypes. Expressivity is highly variable, including within families. Anticipation is not established. No robust founder effect, population-specific carrier frequency, ethnic enrichment, geographic concentration, or consanguinity dependence is established. Both sexes are affected; one cohort included 15 males among 27 children, and a separate 10-person KCNT1-DEE subgroup was 50% female. (borlot2020kcnt1‐relatedepilepsyan pages 1-2, donnan2023ratesofstatus pages 3-4)

Disease-specific incidence and prevalence are unknown. Broad childhood DEE epidemiology must not be substituted for DEE14 prevalence. The rarity, evolving nomenclature, and underdiagnosis preclude a defensible cases-per-100,000 estimate.

## 10. Diagnostics

### Clinical and electrophysiological assessment

Evaluation should include detailed seizure semiology, developmental history, three-generation pedigree, prolonged video-EEG, brain MRI with epilepsy protocol, and assessment of feeding, respiratory, sleep, tone, movement, vision, hearing, and development. EEG identifies migrating focal ictal patterns but is not independently diagnostic. MRI excludes structural causes and establishes baseline cerebral volume and myelination. (carvill1993kcnt1relatedepilepsy pages 3-6, carvill1993kcnt1relatedepilepsy pages 1-3)

Laboratory testing—glucose, electrolytes, calcium/magnesium, liver/renal indices, lactate, ammonia, amino acids, acylcarnitines, urine organic acids, and infection/CSF studies when indicated—is directed at treatable mimics. There is no KCNT1 enzyme assay, circulating biomarker, biopsy signature, or liquid-biopsy test.

### Genetic testing strategy

1. **First line:** rapid trio genome or exome sequencing, or a comprehensive neonatal/infantile epilepsy/DEE panel including **KCNT1**, **SCN1A, SCN2A, SCN8A, KCNQ2, STXBP1, CDKL5, SLC12A5, SLC25A22, TBC1D24, PLCB1**, and metabolic epilepsy genes.
2. Confirm clinically significant variants and parental origin; assess low-level parental mosaicism when recurrence counseling is important.
3. Ensure copy-number calling or add chromosomal microarray when congenital anomalies, dysmorphism, or unexplained negative sequencing warrants it.
4. Use WGS after negative panel/WES when noncoding, structural, mosaic, or technically difficult variants remain possible.
5. Karyotyping/FISH, mitochondrial sequencing, and repeat-expansion testing are not routine for a classic KCNT1 presentation unless another diagnosis is suspected.

A 400-patient panel study found causative variants in 71/400 (18%), rising to 39% when seizures began in the first two months; KCNT1 variants were found in three patients. These are general early-onset epilepsy yields, not KCNT1 test sensitivity. (carvill1993kcnt1relatedepilepsy pages 6-8)

### Diagnostic rule and differential diagnosis

A compatible phenotype plus a pathogenic/likely pathogenic KCNT1 variant establishes the molecular diagnosis. A VUS does not. No universally accepted DEE14 clinical criteria exist. (carvill1993kcnt1relatedepilepsy pages 1-3)

Differentials include structural epilepsy, hypoxic–ischemic injury, CNS infection, pyridoxine-dependent epilepsy, pyridoxal-phosphate-responsive epilepsy, glucose-transporter deficiency, mitochondrial disease, and genetic EIMFS/DEE caused by **SCN2A, SCN8A, SCN1A, SLC12A5, SLC25A22, TBC1D24, KCNQ2**, and **STXBP1**. Treatable metabolic and infectious conditions require urgent exclusion. (carvill1993kcnt1relatedepilepsy pages 6-8)

Population newborn screening is unavailable. Cascade testing is appropriate for a known familial variant but has limited reach because most cases are de novo.

## 11. Outcome and prognosis

DEE14 generally causes severe lifelong morbidity: drug-resistant epilepsy, profound cognitive/communication impairment, motor disability, feeding dependence, sleep disruption, recurrent hospitalizations, and complete or near-complete dependence for daily activities. Seizure improvement does not guarantee developmental recovery. Quantitative EQ-5D, SF-36, or PROMIS norms specific to DEE14 are unavailable; caregiver studies document major family-health, social, and financial burdens. (lafferty2024adiseaseconceptual pages 1-8, lafferty2024adiseaseconceptual pages 49-53)

In the 27-child cohort, four children died (15%); none was classified as SUDEP. In a 2023 retrospective study, convulsive status epilepticus occurred in 6/10 individuals with KCNT1-related DEE (60%; 95% CI 26–88). That study identified no KCNT1 SUDEP cases, but its subgroup was too small to demonstrate absence of risk. Overall genetic-DEE mortality and SUDEP rates must not be attributed specifically to KCNT1. (donnan2023ratesofstatus pages 1-2, donnan2023ratesofstatus pages 2-3, borlot2020kcnt1‐relatedepilepsyan pages 1-2)

No validated five- or ten-year survival rate, life expectancy, prognostic calculator, or molecular prognostic biomarker exists. Potential adverse indicators include neonatal onset, very high seizure burden, status epilepticus, burst suppression/hypsarrhythmia, abnormal MRI, profound early developmental impairment, and variants producing high resting open probability, but these require prospective validation. (rychkov2022functionaleffectsof pages 1-2)

## 12. Treatment

### Current strategy

No disease-modifying treatment had established regulatory approval in the 2023–2024 evidence. Management is multidisciplinary and individualized:

1. Treat seizures/status epilepticus according to pediatric epilepsy protocols.
2. Trial conventional antiseizure medicines using seizure diaries and EEG where appropriate.
3. Consider ketogenic diet early in drug-resistant disease.
4. Consider cannabidiol or carefully monitored off-label quinidine at specialist centers after genotype and cardiac review.
5. Provide feeding/nutrition, respiratory, sleep, orthopedic, physical, occupational, speech/augmentative-communication, and palliative-support services.
6. Consider VNS only case by case; evidence is anecdotal.

Suggested NCIt intervention concepts include **Anticonvulsant Therapy**, **Ketogenic Diet**, **Cannabidiol**, **Quinidine**, **Vagus Nerve Stimulation**, **Physical Therapy**, **Occupational Therapy**, **Speech and Language Therapy**, and **Genetic Counseling**; exact NCIt codes should be verified in the current release.

### Evidence for specific therapies

Conventional antiseizure medications have no consistently superior agent. Polytherapy commonly includes phenobarbital, benzodiazepines, levetiracetam, valproate, topiramate, sodium-channel blockers, and others. A multicentre cohort used a mean 7.4 medications per patient without a consistently effective drug. (borlot2020kcnt1‐relatedepilepsyan pages 1-2)

The 2024 systematic review included 43 studies and 197 KCNT1-spectrum patients. Within the small non-EIMFS DEE subgroup, benefit was reported for ketogenic diet in 4/7, cannabidiol in 1/2, and quinidine in 6/9. In EIMFS, benefit occurred in 25/40 for diet, 6/12 for CBD, and 25/56 for quinidine. Definitions included seizure-frequency, intensity, or quality-of-life improvement and were not standardized, making these low-certainty estimates. (gras2024efficacyofanti‐seizure pages 13-14, gras2024efficacyofanti‐seizure pages 1-2, gras2024efficacyofanti‐seizure pages 2-4)

A separate retrospective analysis defining response as ≥50% seizure reduction found overall efficacy of 26.0% for quinidine and 43.5% for ketogenic therapy; among functional-domain variants, rates were 20.6% versus 53.8%, respectively (P=0.037). (lin2022efficacyofantiseizure pages 4-5, lin2022efficacyofantiseizure pages 1-2)

Quinidine blocks KCNT1 current in vitro and is mechanistically attractive, but clinical exposure, CNS penetration, variant sensitivity, and safety are problematic. QT prolongation was reported in 7/9 quantified responders in one dataset, and gastrointestinal and energy/feeding adverse effects also occurred. Use requires baseline cardiology review, serial ECG/QTc and electrolytes, interaction review, and usually therapeutic drug monitoring. A single case associated seizure control with plasma concentrations >1.5 µg/mL, while >4.0 µg/mL increased arrhythmia risk; quinidine alone failed and topiramate was retained. This is not a validated universal therapeutic range. (kravetz2021casereportof pages 1-2, gras2024efficacyofanti‐seizure pages 12-13)

One non-EIMFS case reported substantial seizure and EEG improvement after VNS, but a single uncontrolled observation cannot establish efficacy. Surgery is generally unsuitable because seizures are multifocal and migrating; focal resection is considered only if an independent, stable epileptogenic lesion is proven.

### Advanced and experimental therapy

A Kcnt1-targeting gapmer ASO reduced seizures, improved behavior, and prolonged survival in symptomatic p.Pro924Leu mice after intracerebroventricular administration; neonatal treatment was also tolerated and effective in that model. This is compelling preclinical proof of concept, not clinical efficacy. (burbano2022antisenseoligonucleotidetherapy pages 1-2)

A 2024 bioRxiv preprint reported marked seizure reductions in two p.Arg474His individuals treated with a first-in-human ASO and normalization of patient-neuron electrophysiology. Because the source was a preprint and detailed controlled clinical data were unavailable, it should be recorded as preliminary. (golinski2024genetherapyfor pages 1-2)

**Clinical studies:** NCT04924153 was a completed, non-interventional 35-person natural-history study with 12-month seizure, adaptive-behavior, sleep, and quality-of-life outcomes. (NCT04924153 chunk 1, NCT04924153 chunk 2)

Two retrieved interventional records began **after 2024** and are latest-current rather than 2023–2024 evidence: intrathecal S230815, Phase Ib/II, approximately 20 participants aged 2–12 years, NCT07227857; and oral ABS-1230, Phase 1b/2, approximately 55 participants aged one month to <22 years, NCT07600736. Registry entries provide no efficacy conclusion. (NCT07600736 chunk 1, NCT07227857 chunk 1)

## 13. Prevention

Primary prevention through lifestyle change, vaccination, environmental control, or medication is not applicable to a usually de novo Mendelian disorder. No vaccine or chemoprophylaxis exists.

Secondary prevention consists of rapid recognition of neonatal/infantile focal seizures, early EEG, and expedited genomic diagnosis so treatable mimics and precision options are not delayed. Population newborn screening is not established.

For families with a known variant, genetic counseling should address autosomal-dominant transmission, parental mosaicism, recurrence uncertainty after an apparently de novo finding, prenatal diagnosis, and preimplantation genetic testing. Tertiary prevention includes seizure-rescue planning, status-epilepticus protocols, aspiration and nutrition management, nocturnal supervision when appropriate, SUDEP counseling, vaccination and infection prevention, bone-health monitoring, rehabilitation, and caregiver support. (carvill1993kcnt1relatedepilepsy pages 1-3, carvill1993kcnt1relatedepilepsy pages 10-13)

## 14. Other species and natural disease

No well-established naturally occurring veterinary syndrome directly equivalent to human KCNT1-DEE14 was identified. Therefore, breed associations, VBO terms, animal prevalence, and veterinary carrier frequencies are unavailable. The disorder is noninfectious and has no zoonotic or cross-species transmission.

Relevant orthologues include mouse **Kcnt1** in *Mus musculus* (NCBI Taxonomy 10090), rat **Kcnt1** in *Rattus norvegicus* (10116), zebrafish orthologues in *Danio rerio* (7955), and the conserved channel system studied in *Drosophila melanogaster* (7227). Exact NCBI Gene identifiers should be verified through the current orthology release before ingestion. Conservation of sodium-activated potassium conductance supports comparative modeling, but species differences in channel expression, development, and dosage limit direct clinical extrapolation.

## 15. Model organisms

### Mouse

A heterozygous Kcnt1 p.Arg455His mouse, homologous to human p.Arg474His, develops persistent interictal spikes, spontaneous seizures, and increased pentylenetetrazole susceptibility. Homozygous animals are embryonic lethal, limiting direct dosage comparison with heterozygous human disease. Another p.Tyr777His model, homologous to human p.Tyr796His, shows early seizures, cortical hyperexcitability, cognitive impairment, reduced inhibitory-neuron excitability, and altered connectivity. Human Y796H increased KNa current 3–11-fold in heterologous assays. (shore2020reducedgabaergicneuron pages 1-4, cole2021functionandpharmacological pages 32-36)

A homozygous p.Pro924Leu mouse recapitulates frequent seizures, developmental compromise, and premature death and has supported ASO proof-of-concept. Its homozygous genotype is a major limitation because human disease is usually heterozygous. (burbano2022antisenseoligonucleotidetherapy pages 1-2)

Kcnt1-null mice have no spontaneous epilepsy and normal lifespan but show exploratory and motor/procedural-learning deficits, cautioning that excessive therapeutic knockdown could have consequences not predicted by seizure outcomes alone. (cole2021functionandpharmacological pages 39-43)

### Cellular and in-vitro systems

HEK293T cells, Xenopus oocytes, primary neurons, and patient-derived or engineered iPSC neurons quantify current amplitude, gating, sodium sensitivity, afterhyperpolarization, firing, and pharmacological block. Across 14 tested variants, all except T314A increased current amplitude; resting open probability correlated with clinical severity. Quinidine reduced variant-channel gain of function in vitro, but this did not reliably predict human response. (rychkov2022functionaleffectsof pages 1-2, milligan2014kcnt1gainof pages 1-3)

### Drosophila

Transgenic flies expressing human G288S, R398Q, or R928C in GABAergic neurons developed seizure phenotypes and variant-dependent responses to five commonly used antiseizure drugs. Cannabidiol produced the greatest reduction in that platform. This 2024 model is useful for whole-animal drug screening but cannot reproduce human cortical development, pharmacokinetics, communication disability, or SUDEP. 

### Resources and model applications

Models can be sought through MGI, IMSR, MMRRC, IMPC, ZFIN, FlyBase, and relevant iPSC repositories. Major uses are variant functional classification, cell-type mechanism, developmental-window analysis, KCNT1 inhibitor screening, and ASO dose/safety optimization. No model fully recapitulates the heterogeneous human syndrome.

## Current understanding and principal knowledge gaps

Authoritative 2024 DEE reviews recognize heterozygous de novo KCNT1 gain of function and inhibitory-neuron disinhibition as a leading mechanistic explanation, while stressing that developmental impairment can reflect both primary genetic dysfunction and epileptic activity. (scheffer2024developmentalandepileptic pages 4-6)

The highest-priority gaps are a disease-specific incidence estimate; prospective untreated natural history; standardized seizure and developmental endpoints; variant-resolved functional interpretation; validated prognostic biomarkers; long-term mortality/SUDEP estimates; controlled evidence for ketogenic diet, CBD, and quinidine; and peer-reviewed clinical evidence for KCNT1-lowering therapies. Existing treatment percentages should be considered hypothesis-generating, not comparative-effectiveness estimates.

### Selected direct abstract statements

- Rychkov et al. concluded that reduced inhibitory-neuron firing “**leads to disinhibition of neural circuits, hyperexcitability and seizures**,” summarizing the principal circuit hypothesis. (rychkov2022functionaleffectsof pages 1-2)
- The ASO mouse study reported that treatment “**significantly reduced**” seizure frequency, improved behavioral abnormalities, and extended survival, explicitly describing the work as proof of concept. (burbano2022antisenseoligonucleotidetherapy pages 1-2)
- The 2024 treatment review states that KCNT1-related epilepsy commonly involves “**drug-resistant seizures and global developmental delays**,” but its efficacy estimates derive mainly from uncontrolled reports. (gras2024efficacyofanti‐seizure pages 1-2)

**URL note:** DOI links supplied above resolve to publisher records. Key recent sources include Gras et al., published June 2024, https://doi.org/10.1002/epi4.12975; Scheffer et al., September 2024, https://doi.org/10.1038/s41572-024-00546-6; Donnan et al., April 18, 2023, https://doi.org/10.1212/WNL.0000000000207080; and the preliminary Golinski et al. preprint, October 24, 2024, https://doi.org/10.1101/2024.10.24.620125.

References

1. (OpenTargets Search: developmental and epileptic encephalopathy 14-KCNT1): Open Targets Query (developmental and epileptic encephalopathy 14-KCNT1, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (borlot2020kcnt1‐relatedepilepsyan pages 1-2): Felippe Borlot, Ahmed Abushama, Nadine Morrison‐Levy, Puneet Jain, Kollencheri Puthenveettil Vinayan, Musaad Abukhalid, Hesham M. Aldhalaan, Hanin S. Almuzaini, Sheffali Gulati, Tova Hershkovitz, Ramesh Konanki, Lokesh Lingappa, Aimee F. Luat, Shatha Shafi, Brahim Tabarki, Maya Thomas, Sangeetha Yoganathan, Majid Alfadhel, Ravindra Arya, Elizabeth J. Donner, Salleh N. Ehaideb, Vykuntaraju K. Gowda, Vivek Jain, Priyanka Madaan, Kenneth A. Myers, Hiroshi Otsubo, Prateek Panda, Jitendra K. Sahu, Letícia P. B. Sampaio, Suvasini Sharma, Elisabeth Simard‐Tremblay, Maria Zak, and Robyn Whitney. Kcnt1‐related epilepsy: an international multicenter cohort of 27 pediatric cases. Epilepsia, 61:679-692, Mar 2020. URL: https://doi.org/10.1111/epi.16480, doi:10.1111/epi.16480. This article has 93 citations and is from a domain leading peer-reviewed journal.

3. (carvill1993kcnt1relatedepilepsy pages 10-13): G Carvill. Kcnt1-related epilepsy. Unknown journal, 1993.

4. (carvill1993kcnt1relatedepilepsy pages 3-6): G Carvill. Kcnt1-related epilepsy. Unknown journal, 1993.

5. (carvill1993kcnt1relatedepilepsy pages 1-3): G Carvill. Kcnt1-related epilepsy. Unknown journal, 1993.

6. (zeka2023casereportdiagnosis pages 1-2): Naim Zeka, Eris Zeka, Esra Zhubi, and Ilir Hoxha. Case report: diagnosis of a patient with sifrim–hitz–weiss syndrome, development and epileptic encephalopathy-14, and medium chain acyl-coa dehydrogenase deficiency. Frontiers in Pediatrics, Sep 2023. URL: https://doi.org/10.3389/fped.2023.1230056, doi:10.3389/fped.2023.1230056. This article has 4 citations.

7. (rychkov2022functionaleffectsof pages 1-2): Grigori Y. Rychkov, Zeeshan Shaukat, Chiao Xin Lim, Rashid Hussain, Ben J. Roberts, Claudia M. Bonardi, Guido Rubboli, Brandon F. Meaney, Robyn Whitney, Rikke S. Møller, Michael G. Ricos, and Leanne M. Dibbens. Functional effects of epilepsy associated kcnt1 mutations suggest pathogenesis via aberrant inhibitory neuronal activity. International Journal of Molecular Sciences, 23:15133, Dec 2022. URL: https://doi.org/10.3390/ijms232315133, doi:10.3390/ijms232315133. This article has 23 citations.

8. (shore2020reducedgabaergicneuron pages 1-4): Amy N. Shore, Sophie Colombo, William F. Tobin, Sabrina Petri, Erin R. Cullen, Soledad Dominguez, Christopher D. Bostick, Michael A. Beaumont, Damian Williams, Dion Khodagholy, Mu Yang, Cathleen M. Lutz, Yueqing Peng, Jennifer N. Gelinas, David B. Goldstein, Michael J. Boland, Wayne N. Frankel, and Matthew C. Weston. Reduced gabaergic neuron excitability, altered synaptic connectivity, and seizures in a kcnt1 gain-of-function mouse model of childhood epilepsy. Cell reports, 33:108303-108303, Oct 2020. URL: https://doi.org/10.1016/j.celrep.2020.108303, doi:10.1016/j.celrep.2020.108303. This article has 96 citations and is from a highest quality peer-reviewed journal.

9. (scheffer2024developmentalandepileptic pages 4-6): Ingrid E. Scheffer, Sameer Zuberi, Heather C. Mefford, Renzo Guerrini, and Amy McTague. Developmental and epileptic encephalopathies. Nature Reviews Disease Primers, Sep 2024. URL: https://doi.org/10.1038/s41572-024-00546-6, doi:10.1038/s41572-024-00546-6. This article has 175 citations.

10. (donnan2023ratesofstatus pages 1-2): Alice M. Donnan, Amy L. Schneider, Sophie Russ-Hall, Leonid Churilov, and Ingrid E. Scheffer. Rates of status epilepticus and sudden unexplained death in epilepsy in people with genetic developmental and epileptic encephalopathies. Neurology, Apr 2023. URL: https://doi.org/10.1212/wnl.0000000000207080, doi:10.1212/wnl.0000000000207080. This article has 109 citations and is from a highest quality peer-reviewed journal.

11. (lafferty2024adiseaseconceptual pages 1-8): Jasmine M. Lafferty. A disease conceptual model of kcnt1-related epilepsy. Text, Jan 2024. URL: https://doi.org/10.7282/t3-pb2n-dj92, doi:10.7282/t3-pb2n-dj92. This article has 0 citations and is from a peer-reviewed journal.

12. (gras2024efficacyofanti‐seizure pages 1-2): Mathilde Gras, David Bearden, Justin West, and Rima Nabbout. Efficacy of anti‐seizure medications and alternative therapies (ketogenic diet, cbd, and quinidine) in kcnt1‐related epilepsy: a systematic review. Epilepsia Open, 9:1176-1191, Jun 2024. URL: https://doi.org/10.1002/epi4.12975, doi:10.1002/epi4.12975. This article has 23 citations and is from a peer-reviewed journal.

13. (lin2022efficacyofantiseizure pages 1-2): Zehong Lin, Tian Sang, Ying Yang, Yuan Wu, Yan Dong, Taoyun Ji, Yuehua Zhang, Ye Wu, Kai Gao, and Yuwu Jiang. Efficacy of anti-seizure medications, quinidine, and ketogenic diet therapy for kcnt1-related epilepsy and genotype-efficacy correlation analysis. Frontiers in Neurology, Jan 2022. URL: https://doi.org/10.3389/fneur.2021.834971, doi:10.3389/fneur.2021.834971. This article has 17 citations and is from a peer-reviewed journal.

14. (gras2024efficacyofanti‐seizure pages 12-13): Mathilde Gras, David Bearden, Justin West, and Rima Nabbout. Efficacy of anti‐seizure medications and alternative therapies (ketogenic diet, cbd, and quinidine) in kcnt1‐related epilepsy: a systematic review. Epilepsia Open, 9:1176-1191, Jun 2024. URL: https://doi.org/10.1002/epi4.12975, doi:10.1002/epi4.12975. This article has 23 citations and is from a peer-reviewed journal.

15. (carvill1993kcnt1relatedepilepsy pages 6-8): G Carvill. Kcnt1-related epilepsy. Unknown journal, 1993.

16. (NCT04924153 chunk 1):  A Natural History Study of Participants With Potassium Sodium-Activated Channel Subfamily T Member 1 (KCNT1)-Related Epilepsy. Biogen. 2021. ClinicalTrials.gov Identifier: NCT04924153

17. (NCT07600736 chunk 1):  A Study to Investigate the Safety, Tolerability, Pharmacokinetics, and Clinical Activity of ABS-1230 in Pediatric and Young Adult Participants With KCNT1-related Epilepsy. Actio Biosciences, Inc.. 2026. ClinicalTrials.gov Identifier: NCT07600736

18. (NCT07227857 chunk 1):  A First-in-human Study of S230815 in Pediatric Participants With KCNT1-related Developmental and Epileptic Encephalopathy. Institut de Recherches Internationales Servier. 2025. ClinicalTrials.gov Identifier: NCT07227857

19. (carvill1993kcnt1relatedepilepsy pages 13-16): G Carvill. Kcnt1-related epilepsy. Unknown journal, 1993.

20. (milligan2014kcnt1gainof pages 1-3): Carol J. Milligan, Melody Li, Elena V. Gazina, Sarah E. Heron, Umesh Nair, Chantel Trager, Christopher A. Reid, Anu Venkat, Donald P. Younkin, Dennis J. Dlugos, Slavé Petrovski, David B. Goldstein, Leanne M. Dibbens, Ingrid E. Scheffer, Samuel F. Berkovic, and Steven Petrou. Kcnt1 gain of function in 2 epilepsy phenotypes is reversed by quinidine. Annals of Neurology, 75:581-590, Apr 2014. URL: https://doi.org/10.1002/ana.24128, doi:10.1002/ana.24128. This article has 341 citations and is from a highest quality peer-reviewed journal.

21. (cole2021functionandpharmacological pages 36-39): BA Cole. Function and pharmacological modulation of the epilepsy-associated kna1. 1 (kcnt1) potassium channel. Unknown journal, 2021.

22. (gras2024efficacyofanti‐seizure pages 13-14): Mathilde Gras, David Bearden, Justin West, and Rima Nabbout. Efficacy of anti‐seizure medications and alternative therapies (ketogenic diet, cbd, and quinidine) in kcnt1‐related epilepsy: a systematic review. Epilepsia Open, 9:1176-1191, Jun 2024. URL: https://doi.org/10.1002/epi4.12975, doi:10.1002/epi4.12975. This article has 23 citations and is from a peer-reviewed journal.

23. (lafferty2024adiseaseconceptual pages 49-53): Jasmine M. Lafferty. A disease conceptual model of kcnt1-related epilepsy. Text, Jan 2024. URL: https://doi.org/10.7282/t3-pb2n-dj92, doi:10.7282/t3-pb2n-dj92. This article has 0 citations and is from a peer-reviewed journal.

24. (golinski2024genetherapyfor pages 1-2): Sean R. Golinski, Karla Soriano, Alex C. Briegel, Madeline C. Burke, Timothy W. Yu, Tojo Nakayama, Ruilong Hu, and Richard S. Smith. Gene therapy for targeting a prenatally enriched potassium channel associated with severe childhood epilepsy and premature death. bioRxiv, Oct 2024. URL: https://doi.org/10.1101/2024.10.24.620125, doi:10.1101/2024.10.24.620125. This article has 2 citations.

25. (burbano2022antisenseoligonucleotidetherapy pages 1-2): Lisseth Estefania Burbano, Melody Li, Nikola Jancovski, Paymaan Jafar-Nejad, Kay Richards, Alicia Sedo, Armand Soriano, Ben Rollo, Linghan Jia, Elena V. Gazina, Sandra Piltz, Fatwa Adikusuma, Paul Q. Thomas, Helen Kopsidas, Frank Rigo, Christopher A. Reid, Snezana Maljevic, and Steven Petrou. Antisense oligonucleotide therapy for kcnt1 encephalopathy. Dec 2022. URL: https://doi.org/10.1172/jci.insight.146090, doi:10.1172/jci.insight.146090. This article has 77 citations and is from a domain leading peer-reviewed journal.

26. (donnan2023ratesofstatus pages 3-4): Alice M. Donnan, Amy L. Schneider, Sophie Russ-Hall, Leonid Churilov, and Ingrid E. Scheffer. Rates of status epilepticus and sudden unexplained death in epilepsy in people with genetic developmental and epileptic encephalopathies. Neurology, Apr 2023. URL: https://doi.org/10.1212/wnl.0000000000207080, doi:10.1212/wnl.0000000000207080. This article has 109 citations and is from a highest quality peer-reviewed journal.

27. (donnan2023ratesofstatus pages 2-3): Alice M. Donnan, Amy L. Schneider, Sophie Russ-Hall, Leonid Churilov, and Ingrid E. Scheffer. Rates of status epilepticus and sudden unexplained death in epilepsy in people with genetic developmental and epileptic encephalopathies. Neurology, Apr 2023. URL: https://doi.org/10.1212/wnl.0000000000207080, doi:10.1212/wnl.0000000000207080. This article has 109 citations and is from a highest quality peer-reviewed journal.

28. (gras2024efficacyofanti‐seizure pages 2-4): Mathilde Gras, David Bearden, Justin West, and Rima Nabbout. Efficacy of anti‐seizure medications and alternative therapies (ketogenic diet, cbd, and quinidine) in kcnt1‐related epilepsy: a systematic review. Epilepsia Open, 9:1176-1191, Jun 2024. URL: https://doi.org/10.1002/epi4.12975, doi:10.1002/epi4.12975. This article has 23 citations and is from a peer-reviewed journal.

29. (lin2022efficacyofantiseizure pages 4-5): Zehong Lin, Tian Sang, Ying Yang, Yuan Wu, Yan Dong, Taoyun Ji, Yuehua Zhang, Ye Wu, Kai Gao, and Yuwu Jiang. Efficacy of anti-seizure medications, quinidine, and ketogenic diet therapy for kcnt1-related epilepsy and genotype-efficacy correlation analysis. Frontiers in Neurology, Jan 2022. URL: https://doi.org/10.3389/fneur.2021.834971, doi:10.3389/fneur.2021.834971. This article has 17 citations and is from a peer-reviewed journal.

30. (kravetz2021casereportof pages 1-2): M. C. Kravetz, M. S. Viola, J. Prenz, M. Curi, G. F. Bramuglia, and S. Tenembaum. Case report of novel genetic variant in kcnt1 channel and pharmacological treatment with quinidine. precision medicine in refractory epilepsy. Frontiers in Pharmacology, May 2021. URL: https://doi.org/10.3389/fphar.2021.648519, doi:10.3389/fphar.2021.648519. This article has 14 citations.

31. (NCT04924153 chunk 2):  A Natural History Study of Participants With Potassium Sodium-Activated Channel Subfamily T Member 1 (KCNT1)-Related Epilepsy. Biogen. 2021. ClinicalTrials.gov Identifier: NCT04924153

32. (cole2021functionandpharmacological pages 32-36): BA Cole. Function and pharmacological modulation of the epilepsy-associated kna1. 1 (kcnt1) potassium channel. Unknown journal, 2021.

33. (cole2021functionandpharmacological pages 39-43): BA Cole. Function and pharmacological modulation of the epilepsy-associated kna1. 1 (kcnt1) potassium channel. Unknown journal, 2021.

## Artifacts

- [Edison artifact artifact-00](Developmental_And_Epileptic_Encephalopathy_14-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 15 |
| Resolved | 15 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 15 |
| On topic | 11 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 33 |
| Resolved | 32 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013989` (4 mentions) - the report calls it "if available"; MONDO calls it **developmental and epileptic encephalopathy, 14**