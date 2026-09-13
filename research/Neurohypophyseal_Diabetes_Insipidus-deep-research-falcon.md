---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-05T17:57:22.239586'
end_time: '2026-09-05T18:09:10.806994'
duration_seconds: 708.57
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Neurohypophyseal Diabetes Insipidus
  mondo_id: MONDO:0007450
  category: ''
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 52
reference_validation:
  total_references: 20
  verified: 18
  not_found: 0
  unverifiable: 2
  confabulation_rate: 0.0
  relevance_assessed: 18
  on_topic: 3
  off_topic: 1
  off_topic_references:
  - DOI:10.1055/a-2198-7207
  needs_review: true
  validator_version: 0.2.1
term_validation:
  total_terms: 3
  verified: 2
  not_found: 0
  obsolete: 0
  unverifiable: 1
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0007450
    reported_labels:
    - if available
    ontology_label: neurohypophyseal diabetes insipidus
  unresolvable_prefixes:
  - ORPHA
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Neurohypophyseal_Diabetes_Insipidus-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurohypophyseal Diabetes Insipidus
- **MONDO ID:** MONDO:0007450 (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Neurohypophyseal Diabetes Insipidus** covering all of the
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
- **Disease Name:** Neurohypophyseal Diabetes Insipidus
- **MONDO ID:** MONDO:0007450 (if available)
- **Category:** 

## Research Objectives

Please provide a comprehensive research report on **Neurohypophyseal Diabetes Insipidus** covering all of the
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


# Neurohypophyseal Diabetes Insipidus: Disease-Characteristics Research Report

**Target entity:** Neurohypophyseal diabetes insipidus  
**Preferred current clinical name:** **arginine vasopressin deficiency (AVP-D)**  
**MONDO:** **MONDO:0007450**  
**Category:** rare neuroendocrine disorder of water homeostasis; hereditary and acquired forms  
**Scope note:** “Neurohypophyseal diabetes insipidus” is sometimes used narrowly for hereditary **AVP**-related disease and sometimes broadly for central diabetes insipidus. This report covers the broad AVP-deficiency phenotype while explicitly distinguishing inherited AVP-related disease.

The following table summarizes the principal knowledge-base fields; detailed evidence and limitations follow.

| Knowledge-base field | Compact finding | High-value data / suggested ontology terms | Evidence type and citation |
|---|---|---|---|
| Definition and nomenclature | Neurohypophyseal diabetes insipidus is deficient hypothalamic production or neurohypophyseal release of arginine vasopressin, causing hypotonic polyuria and compensatory polydipsia. The preferred name is **arginine vasopressin deficiency (AVP-D)**; distinguish it from AVP resistance and primary polydipsia. | **MONDO:0007450**; synonym: central diabetes insipidus. Suggested HPO: Central diabetes insipidus (**HP:0000863**, present in evidence). | Clinical reviews and patient survey (atila2022centraldiabetesinsipidus pages 1-5, onwuka2025physiologicalbasisof pages 1-3, OpenTargets Search: neurohypophyseal diabetes insipidus-AVP) |
| Epidemiology | AVP-D is rare, and population-level incidence data are limited. Acquired disease greatly exceeds congenital disease in adult clinical cohorts. | Approximate prevalence: **1 in 25,000**. Hereditary DI has been estimated at **<10%** of DI cases. | Reviews (tomkins2026bestpractice&a pages 5-6, jasmeen2024diabetesinsipidustypes pages 1-3) |
| Major etiologies | Acquired causes include hypothalamic–pituitary surgery, sellar or suprasellar tumors and cysts, trauma, hemorrhage or ischemia, autoimmune or inflammatory hypophysitis, Langerhans-cell histiocytosis, germinoma, sarcoidosis, infection, congenital CNS malformations, and idiopathic disease. | In a 1,034-person survey: idiopathic **30%**, presurgical tumor/cyst **21%**, and postsurgical tumor/cyst **25%**. In 23 children with pituitary-stalk thickening, **73.9%** had germinoma and three had LCH. Adult stalk-lesion series averaged **24% neoplastic, 28% inflammatory, 11% congenital, and 37% unknown**. | Human survey, pediatric cohort, and imaging review (atila2022centraldiabetesinsipidus pages 1-5, hana2020pituitarystalkenlargement pages 2-4, moszczynska2022pituitarystalkthickening pages 1-2) |
| Hallmark phenotypes | Large-volume dilute urine, excessive thirst, nocturia, dehydration, fatigue, weight loss, and hyperosmolality or hypernatremia when water access or thirst is impaired; partial AVP-D can be milder. | Survey frequencies: polyuria **90%**, polydipsia **88%**, and nocturia **78%**. Suggested HPO terms: **Polyuria**, **Polydipsia**, **Nocturia**, **Dehydration**, **Hypernatremia**, **Fatigue**, **Weight loss**, and Central diabetes insipidus (**HP:0000863**); other IDs require ontology validation. | International patient survey and clinical review (atila2022centraldiabetesinsipidus pages 9-13, jasmeen2024diabetesinsipidustypes pages 1-3) |
| Associated endocrine phenotypes | Acquired stalk or hypothalamic disease often produces combined anterior and posterior pituitary dysfunction rather than isolated AVP-D. | Survey: isolated posterior dysfunction **47%** and combined anterior/posterior dysfunction **53%**. In pediatric stalk thickening: growth-hormone deficiency **56.5%**, hyperprolactinemia **39%**, central hypothyroidism **34.8%**, and adrenal insufficiency **9%**. Suggested HPO terms require ID validation. | Human survey and pediatric cohort (atila2022centraldiabetesinsipidus pages 9-13, moszczynska2022pituitarystalkthickening pages 1-2) |
| Causal gene and inheritance | Familial neurohypophyseal DI is primarily caused by heterozygous pathogenic **AVP** variants and usually follows fully penetrant autosomal-dominant inheritance; rare autosomal-recessive disease results from biallelic variants or a large deletion. | **AVP**, Ensembl **ENSG00000101200**; more than **70 variants** reported by 2020. Classes include missense, nonsense, frameshift, deletion, and signal-peptide defects, predominantly affecting neurophysin II. Example: **NM_000490.4:c.61T>C (p.Tyr21His; rs121964893)**. | Genetic reviews, family sequencing, and Open Targets aggregation (spiess2020roleofprotein pages 1-5, koufaris2015identificationofan pages 3-4, OpenTargets Search: neurohypophyseal diabetes insipidus-AVP) |
| Core familial mechanism | Mutant prepro-AVP misfolds and remains in the endoplasmic reticulum, heterodimerizes with and traps wild-type precursor, undergoes ER-associated proteasomal degradation or forms disulfide-linked fibrillar aggregates, and reduces regulated AVP secretion. Chronic ER stress, unfolded-protein response, and autophagy are implicated in progressive neuronal dysfunction; neuron loss occurs in some models but is not required for early disease. | Precursor components: 19-aa signal peptide, AVP nonapeptide, 93-aa neurophysin II, and copeptin. Suggested GO processes: protein folding, ER-associated degradation, unfolded-protein response, autophagy, regulated secretion, AVP secretion, and renal water reabsorption; IDs require validation. | In-vitro experiments and knock-in/transgenic mouse studies (spiess2020roleofprotein pages 1-5, arima2014endoplasmicreticulumstress pages 2-3, spiess2020roleofprotein pages 8-10, spiess2020roleofprotein pages 5-8) |
| Downstream renal mechanism | Reduced circulating AVP decreases collecting-duct V2-receptor activation and aquaporin-2 membrane recruitment, reducing water reabsorption and producing dilute urine; intact thirst often prevents marked hypernatremia. | Suggested cell types: hypothalamic magnocellular AVP neuron and renal collecting-duct principal cell; CL IDs require validation. Suggested processes: AVPR2 signaling, AQP2 trafficking, and water homeostasis. | Physiological review (onwuka2025physiologicalbasisof pages 1-3) |
| Initial diagnostic confirmation | Confirm true hypotonic polyuria, exclude osmotic diuresis and electrolyte or renal causes, and measure serum sodium, plasma osmolality, and urine osmolality. | Polyuria: **>50 mL/kg/day or >3 L/day**. With hypernatremia, urine osmolality **<300 mOsm/kg** supports an AVP disorder, whereas **>700 mOsm/kg** indicates preserved AVP action. Acute postoperative criteria include polyuria, urine osmolality **<300 mOsm/kg**, and plasma osmolality **>300 mOsm/kg** or sodium **>145 mmol/L**. | Clinical guidance and review (tomkins2026bestpractice& pages 5-6, tomkins2026bestpractice&a pages 5-6) |
| Dynamic testing | Water deprivation followed by desmopressin distinguishes AVP-D from AVP resistance, but performs poorly in partial disease or chronic primary polydipsia and can cause dehydration. Stimulated copeptin is the preferred modern discriminator where expertise is available. | Traditional water-deprivation accuracy approximately **70% overall** and **41% for primary polydipsia**. Baseline copeptin **>21.4 pmol/L** supports AVP resistance. Arginine-stimulated thresholds under the predefined protocol: **<2.4 pmol/L** complete AVP-D, **2.4–3.8 pmol/L** partial AVP-D, and **>3.8 pmol/L** primary polydipsia. | Diagnostic reviews and prospective-test protocol evidence (jasmeen2024diabetesinsipidustypes pages 1-3, indirli2024copeptinasa pages 23-27) |
| Imaging and etiologic work-up | Contrast-enhanced hypothalamic–pituitary MRI evaluates the posterior-pituitary bright spot, stalk thickness, hypothalamus, and sellar or suprasellar masses. Isolated stalk thickening requires serial endocrine and MRI surveillance because germinoma or LCH can emerge later. | Pediatric CDI study: etiologic diagnosis at presentation **28.2%**, an additional **13% within 2.5 years**, and permanent anterior deficits **53%**. Suggested surveillance: MRI every six months for two years and again during year three or annually according to risk; pituitary testing every six months for 2–3 years, then annually. | Prospective pediatric cohort and imaging reviews (iorgi2014centraldiabetesinsipidus pages 1-2, hana2020pituitarystalkenlargement pages 11-12) |
| Standard treatment | **Desmopressin (dDAVP)**, a selective V2-receptor agonist, replaces AVP's antidiuretic action; oral formulations generally have the best tolerability and safety profile. Ensure free access to water and treat the underlying lesion where possible. | Suggested intervention term: desmopressin therapy; NCIT identifier requires validation. | Recent treatment reviews (atila2022centraldiabetesinsipidus pages 1-5, christcrain2021diabetesinsipidus pages 9-9) |
| Treatment safety | Continuous antidiuresis plus excess fluid intake can cause dilutional hyponatremia; missed or delayed dDAVP, fasting, or restricted water can cause severe hypernatremic dehydration. Planned intermittent aquaresis reduces risk. | Survey: outpatient hyponatremia **22%**, dysnatraemia requiring admission **35%**, and hypernatremia requiring admission **15%**; desmopressin escape was associated with lower hyponatremia (**OR 0.55, 95% CI 0.39–0.77; p=0.0006**). NHS England recorded **471** incidents, including **76 dose omissions** and **four deaths** from severe dehydration. | Human survey and safety-event data (atila2022centraldiabetesinsipidus pages 9-13, atila2022centraldiabetesinsipidus pages 16-19) |
| Prognosis and quality of life | Isolated hereditary AVP-D is generally compatible with long-term survival when water and dDAVP are reliably available. Morbidity and mortality in acquired disease are driven chiefly by the underlying lesion, hypothalamic injury, associated pituitary deficits, and dysnatraemia. | In the international survey, **64%** reported reduced quality of life and **36%** psychological or recognized psychological changes. In craniopharyngioma, DI and hypopituitarism were negative prognostic factors; childhood-onset standardized mortality ratio was **17 (95% CI 6.3–37)**. | Human survey and population-based craniopharyngioma cohort (atila2022centraldiabetesinsipidus pages 9-13, olsson2015excessmortalityand pages 1-2) |
| Models and experimental therapy | Brattleboro rats carry an Avp defect and reproduce polyuria and polydipsia; AVP-mutant knock-in mice model ER retention, progressive hormone deficiency, and variable neuronal loss. Viral AVP replacement in magnocellular neurons provides preclinical proof of concept but is not an established human therapy. | Suggested model annotations: Brattleboro rat, AVP-mutant knock-in mouse, neuronal cell-expression model, and ERAD-deficient mouse. Human gene, cell, RNA, or CRISPR therapy is not established. | Rodent and cellular mechanistic evidence (arima2014endoplasmicreticulumstress pages 2-3, spiess2020roleofprotein pages 8-10, arima2014endoplasmicreticulumstress pages 1-2) |
| Current trials and emerging research | Current research emphasizes easier copeptin stimulation and whether concomitant oxytocin deficiency contributes to psychological, social, and sexual morbidity after hypothalamic–pituitary injury. | Examples: **NCT05890690**, oral-urea/copeptin, completed, 48 participants; **NCT06036004**, oxytocin substitution, phase 2, recruiting, 112 participants; **NCT04789148**, intranasal oxytocin, phase 1, recruiting, 40 participants; **NCT03572166**, arginine-stimulated copeptin, completed, 177 participants. | Clinical-trial registry records and recent diagnostic evidence (indirli2024copeptinasa pages 23-27) |


*Table: Compact evidence table covering neurohypophyseal diabetes insipidus nomenclature, causes, phenotypes, genetics, mechanisms, diagnosis, treatment, prognosis, models, and emerging trials. Statistics are labeled by evidence type, while ontology terms lacking verified identifiers are explicitly marked for validation.*

## 1. Disease information

Neurohypophyseal DI is deficient synthesis, axonal transport, storage, or release of arginine vasopressin from the hypothalamic–neurohypophyseal system. Insufficient circulating AVP prevents appropriate renal concentration of urine, causing high-volume hypotonic urine, compensatory thirst, and polydipsia. Marked hypernatremia is usually avoided when thirst and access to water remain intact. AVP-D must be distinguished from **AVP resistance** (formerly nephrogenic DI), in which AVP secretion is preserved but the kidney does not respond, and from primary polydipsia. (tomkins2026bestpractice& pages 5-6, onwuka2025physiologicalbasisof pages 1-3)

**Identifiers and terminology**

- MONDO: **MONDO:0007450**, neurohypophyseal diabetes insipidus.
- HPO disease phenotype: **HP:0000863**, central diabetes insipidus.
- Orphanet: **ORPHA:30925**, hereditary central diabetes insipidus, as represented in the Open Targets aggregation.
- Common names: central diabetes insipidus, cranial DI, neurogenic DI, hypothalamic DI, vasopressin-sensitive DI, familial neurohypophyseal DI, familial central DI, autosomal-dominant neurohypophyseal DI, and AVP deficiency. (OpenTargets Search: neurohypophyseal diabetes insipidus-AVP)
- ICD-10-CM generally groups DI under **E23.2**; ICD-11 and MeSH mappings should be checked directly against the release used by the knowledge base because these identifiers were not independently retrieved in this review.
- OMIM commonly separates neurohypophyseal DI from syndromic and nephrogenic forms; a release-verified OMIM identifier was not available in the retrieved evidence and should not be inferred.

The 2022 international patient survey found that 80% of respondents encountered confusion with diabetes mellitus and 85% supported renaming, especially to “vasopressin deficiency” or “arginine vasopressin deficiency.” This patient-safety rationale drove current terminology. (atila2022centraldiabetesinsipidus pages 9-13, atila2022centraldiabetesinsipidus pages 16-19)

**Evidence provenance:** Most information here is aggregated disease-level evidence from reviews, ontologies, registries, and cohorts—not individual EHR records. The major patient-level source was an anonymous international survey of 1,034 people, while genetic reports include individual pedigrees. (atila2022centraldiabetesinsipidus pages 9-13, koufaris2015identificationofan pages 3-4)

## 2. Etiology

### 2.1 Causal factors

**Hereditary isolated AVP-D.** Heterozygous pathogenic **AVP** variants are the major cause of familial neurohypophyseal DI. Rare recessive disease results from biallelic variants or large deletions. Syndromic central DI can also occur in Wolfram syndrome/DIDMOAD and congenital hypothalamic–pituitary malformations, but these are etiologically distinct from isolated AVP-related disease. (spiess2020roleofprotein pages 1-5)

**Acquired AVP-D.** Causes include hypothalamic or pituitary surgery, craniocerebral trauma, hemorrhage or ischemia, germinoma, craniopharyngioma, other sellar/suprasellar tumors or metastases, Langerhans-cell histiocytosis (LCH), Erdheim–Chester disease, lymphocytic or IgG4-related hypophysitis, neurosarcoidosis, tuberculosis and other infections, infiltrative disease, pregnancy-associated hypophysitis, and congenital CNS abnormalities. Some cases remain idiopathic, with autoimmune neurohypophyseal destruction suspected in a subset. (tomkins2026bestpractice& pages 5-6, christcrain2021diabetesinsipidus pages 9-9, hana2020pituitarystalkenlargement pages 2-4)

In the international survey, reported causes were idiopathic in 30%, a tumor/cyst before surgery in 21%, and a tumor/cyst after surgery in 25%. These are self-reported proportions rather than population incidence estimates. (atila2022centraldiabetesinsipidus pages 1-5)

### 2.2 Risk factors

- **Genetic:** an affected parent or familial polyuria–polydipsia; a heterozygous pathogenic AVP allele; biallelic AVP variants in rare recessive families. Dominant variants are usually highly penetrant. (spiess2020roleofprotein pages 1-5)
- **Clinical/anatomical:** hypothalamic–pituitary surgery, stalk transection, trauma, sellar/suprasellar neoplasm, infiltrative disease, and radiologic stalk enlargement. In children with stalk thickening, male sex, younger age, a larger or enlarging lesion, hyperprolactinemia, and multiple anterior pituitary deficits increase concern for neoplasia. (moszczynska2022pituitarystalkthickening pages 6-9)
- **Disease-specific:** in children with LCH or germ-cell tumors, hypothalamic–pituitary involvement confers risk. Among 23 children with pituitary-stalk thickening, 17 (73.9%) had germinoma and three had LCH, illustrating the high-risk referral population rather than general prevalence. (moszczynska2022pituitarystalkthickening pages 1-2)
- **Drug-related:** immune-checkpoint inhibitors can cause hypophysitis, although posterior-pituitary involvement is uncommon. (christcrain2021diabetesinsipidus pages 9-9, iglesias2024anupdateon pages 26-27)

### 2.3 Protective factors and gene–environment interaction

No reproducible protective human allele, dietary factor, exercise pattern, or lifestyle exposure has been shown to prevent AVP-D. Reliable water access protects against hypernatremia but does not prevent the disease. Avoidance of unnecessary hypothalamic/stalk injury and hypothalamus-sparing tumor surgery may reduce iatrogenic risk, although treatment of the underlying lesion takes priority.

A plausible genetic–physiological interaction occurs in dominant AVP disease: dehydration increases demand for AVP synthesis and may intensify ER stress in mutant neurons. In mice, water deprivation was associated with autophagy and neuronal injury, but a corresponding quantified human gene–environment effect has not been demonstrated. (spiess2020roleofprotein pages 8-10, arima2014endoplasmicreticulumstress pages 1-2)

## 3. Phenotypes

| Phenotype | Type and characteristics | Frequency/course | Suggested HPO term |
|---|---|---|---|
| Hypotonic polyuria | Symptom/sign; often continuous, severe in complete deficiency | 90% in the 1,034-person survey | Polyuria |
| Polydipsia/thirst | Symptom; compensatory and usually continuous | 88% | Polydipsia |
| Nocturia/sleep interruption | Symptom; chronic without adequate replacement | 78% | Nocturia |
| Dilute urine/low urine osmolality | Laboratory abnormality | Defining biochemical phenotype | Hyposthenuria / decreased urine osmolality |
| Hypernatremia/hyperosmolality | Laboratory abnormality; episodic or acute when thirst/water access fails | 15% reported admission for hypernatremia | Hypernatremia |
| Dehydration/hypovolemia | Clinical sign; potentially severe | Especially with adipsia, fasting, vomiting, or missed dDAVP | Dehydration |
| Fatigue, weight loss | Symptoms, severity variable | Qualitatively reported | Fatigue; Weight loss |
| Adipsia or impaired thirst | Neurological/endocrine sign; uncommon but high risk | Usually extensive hypothalamic disease | Adipsia |
| Anterior pituitary deficits | Laboratory/clinical; cause-dependent | 53% combined anterior/posterior dysfunction in survey | Hypopituitarism and hormone-specific terms |

Survey frequencies and admission outcomes derive from selected respondents and should not be treated as population prevalence. (atila2022centraldiabetesinsipidus pages 9-13)

In a pediatric stalk-thickening cohort, presenting polyuria/polydipsia/nocturia occurred in 82.6%; decreased growth velocity in 56.5%; CDI in 91.3%; growth-hormone deficiency in 56.5%; hyperprolactinemia in 39%; central hypothyroidism in 34.8%; adrenal insufficiency in 9%; and precocious puberty in 8.7%. (moszczynska2022pituitarystalkthickening pages 1-2)

**Onset and severity:** dominant familial disease usually begins insidiously in infancy or early childhood and progresses as AVP secretory capacity declines. Acquired disease may be abrupt after surgery/trauma or insidious with infiltrative, autoimmune, or neoplastic stalk disease. Partial AVP-D is milder and diagnostically difficult. (spiess2020roleofprotein pages 1-5, iorgi2014centraldiabetesinsipidus pages 1-2)

**Quality of life:** 64% of surveyed patients reported reduced quality of life and 36% psychological or recognized psychological changes. Nocturia, constant treatment planning, fear of dysnatremia, hospital access problems, and associated hypothalamic/pituitary disease affect school, work, recreation, sleep, and mental health. (atila2022centraldiabetesinsipidus pages 9-13)

## 4. Genetic and molecular information

### 4.1 Causal gene

**AVP** encodes prepro-arginine vasopressin. Open Targets identifies AVP (Ensembl **ENSG00000101200**) as the strongest associated target for MONDO:0007450, supported by human literature including PMID **40281371**, **8554046**, **10677561**, **14673472**, and **12012274**. AVPR2 and AQP2 cause renal AVP resistance, not primary neurohypophyseal AVP deficiency. (OpenTargets Search: neurohypophyseal diabetes insipidus-AVP)

The precursor contains a 19-amino-acid signal peptide, the AVP nonapeptide, approximately 93-amino-acid neurophysin II carrier, and C-terminal copeptin/glycopeptide. Neurophysin II contains most precursor disulfide bonds and is the most frequent location of dominant pathogenic variants. (spiess2020roleofprotein pages 10-13, arima2014endoplasmicreticulumstress pages 1-2)

### 4.2 Variants

More than 70 AVP variants were reported by 2020, and the spectrum includes missense, nonsense, frameshift, splice-region, signal-peptide, and deletion variants. Most dominant variants affect the signal peptide or neurophysin-II region; variants in the mature AVP peptide are less common. (spiess2020roleofprotein pages 1-5, spiess2020roleofprotein pages 10-13)

A well-characterized example is **NM_000490.4:c.61T>C, p.(Tyr21His), rs121964893**, affecting position 2 of mature AVP. It cosegregated with disease in Cypriot and Turkish pedigrees; affected individuals had over 80% deficient AVP secretion and absent posterior-pituitary bright spot. (koufaris2015identificationofan pages 3-4)

The retrieved 2025 Japanese report identified heterozygous **c.308T>A, p.(Val103Asp)** in neurophysin II in a family affected for more than five generations. The evidence comprised segregation, computational prediction, and modeled structural change; without validated functional assays, classification should remain according to the submitting laboratory’s ACMG/AMP assessment rather than automatically “pathogenic.”

Dominant variants are germline and generally act through toxic misfolding/dominant-negative mechanisms. Somatic AVP variants are not an established cause. Population allele frequencies are expected to be extremely low for highly penetrant variants, but variant-specific gnomAD frequencies were not retrieved and must be populated directly from the current gnomAD release.

### 4.3 Modifiers, epigenetics, and chromosomes

No clinically validated modifier genes, protective alleles, epigenetic signature, anticipation, or recurrent chromosomal rearrangement specific to isolated AVP-related FNDI has been established. Rare large deletions and biallelic AVP defects exist. Germline mosaicism is theoretically possible but not quantified. Founder mutations have been described in individual pedigrees, but no robust carrier-frequency estimate exists. (spiess2020roleofprotein pages 1-5)

## 5. Environmental information

No toxin, pollutant, smoking behavior, diet, alcohol exposure, or occupation is an established primary cause of isolated neurohypophyseal DI. Relevant non-genetic insults are chiefly anatomical or medical: surgery, trauma, vascular injury, radiation, neoplasia, autoimmunity, and infiltrative or infectious disease. Pregnancy can be associated with hypophysitis; gestational vasopressinase excess causes gestational DI and is a separate mechanism. (tomkins2026bestpractice& pages 5-6, hana2020pituitarystalkenlargement pages 2-4)

Potential infectious causes of stalk inflammation include tuberculosis and rarer CNS infections. AVP-D is not communicable, and no vaccination or pathogen-specific prevention applies to the disease as a whole. (moszczynska2022pituitarystalkthickening pages 6-9, hana2020pituitarystalkenlargement pages 2-4)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **An AVP mutation, hypothalamic–stalk lesion, inflammation, infiltration, vascular injury, trauma, or surgery leads to impaired AVP synthesis, transport, storage, or release.** (tomkins2026bestpractice& pages 5-6, spiess2020roleofprotein pages 1-5)
2. **In dominant familial disease, mutant prepro-AVP misfolding leads to ER retention and heterodimerization with wild-type precursor, which results in dominant-negative trapping and reduced forward trafficking.** (spiess2020roleofprotein pages 8-10, spiess2020roleofprotein pages 5-8)
3. **ER-retained precursor leads to ER-associated degradation or disulfide-linked fibrillar aggregation, which activates the unfolded-protein response and autophagy.** (spiess2020roleofprotein pages 13-18, arima2014endoplasmicreticulumstress pages 1-2)
4. **Chronic proteostatic stress leads to reduced AVP mRNA stability/shortened poly(A) tails and progressive secretory dysfunction; in some models it results in AVP-neuron loss, although neuronal death is not required for early disease.** (arima2014endoplasmicreticulumstress pages 2-3, spiess2020roleofprotein pages 8-10)
5. **Reduced circulating AVP leads to insufficient AVPR2 activation on collecting-duct principal cells.** (onwuka2025physiologicalbasisof pages 1-3)
6. **Reduced AVPR2–Gs–cAMP–PKA signaling leads to diminished apical aquaporin-2 recruitment and water permeability, resulting in reduced collecting-duct water reabsorption.** This downstream renal step is established physiology, while its precise quantitative contribution in each partial-AVP-D genotype is inferred.
7. **Reduced water reabsorption leads to high-volume dilute urine, which results in increased plasma osmolality and activation of thirst.** (onwuka2025physiologicalbasisof pages 1-3)
8. **Branch A—intact thirst and water access lead to compensatory polydipsia, usually preserving sodium. Branch B—adipsia, impaired consciousness, restricted water, vomiting, or omitted desmopressin leads to dehydration and potentially life-threatening hypernatremia.** (tomkins2026bestpractice& pages 5-6, atila2022centraldiabetesinsipidus pages 16-19)

### Mechanistic detail

Mutant precursors remain chaperone-associated in the ER. IRE1, PERK, and ATF6-mediated unfolded-protein responses increase folding capacity and reduce translation; severe unresolved stress can activate CHOP-linked death pathways. ERAD uses SEL1L–HRD1, Derlin, p97/CDC48, ubiquitination, and the proteasome. Sel1L-deficient mice accumulate even wild-type AVP in amyloid-like ER aggregates and develop DI, demonstrating that physiological ER quality control is essential. (spiess2020roleofprotein pages 13-18, spiess2020roleofprotein pages 5-8)

In Cys98stop/C67X-related mouse models, mutant neurophysin accumulated in SON/PVN neurons, axonal transport decreased, AVP production progressively declined, and polyuria developed. Some models showed late neuron loss, whereas others showed persistent AVP-mRNA-positive neurons and progressive disease without apoptosis; therefore “toxic neurodegeneration” is supported but not universal. (arima2014endoplasmicreticulumstress pages 2-3, spiess2020roleofprotein pages 8-10)

**Suggested GO processes:** response to ER stress; unfolded-protein response; ER-associated ubiquitin-dependent protein catabolism; protein folding; autophagy; regulated secretory pathway; hormone secretion; vasopressin secretion; renal water homeostasis; aquaporin-mediated transport.  
**Suggested cellular components:** endoplasmic-reticulum lumen, Golgi apparatus, dense-core secretory granule, neurosecretory axon, plasma membrane, apical collecting-duct membrane.  
**Suggested CL concepts:** magnocellular neurosecretory neuron/vasopressinergic neuron; renal collecting-duct principal cell. Exact GO/CL identifiers require ontology-release validation.

**Omics:** targeted transcript evidence includes AVP mRNA reduction and poly(A)-tail shortening in FNDI mice. No disease-defining human single-cell, spatial-transcriptomic, proteomic, metabolomic, lipidomic, or integrated multi-omic signature is established. (arima2014endoplasmicreticulumstress pages 2-3, arima2014endoplasmicreticulumstress pages 1-2)

## 7. Anatomical structures affected

**Primary sites:** supraoptic nucleus, paraventricular nucleus, hypothalamo-neurohypophyseal axons, median eminence/infundibulum, pituitary stalk, and posterior pituitary. The stalk connects the hypothalamic median eminence to the gland and normally tapers inferiorly. (onwuka2025physiologicalbasisof pages 1-3, hana2020pituitarystalkenlargement pages 2-4)

**Secondary effector organ:** kidney, especially collecting-duct principal cells expressing AVPR2 and AQP2. Secondary complications affect total-body water, extracellular fluid, CNS function during dysnatremia, and—after longstanding massive polyuria—the urinary tract.

Suggested anatomical terms include hypothalamus, supraoptic nucleus, paraventricular nucleus, pituitary stalk, neurohypophysis, kidney collecting duct, and renal medulla. UBERON identifiers should be release-validated. Disease is midline/bilateral rather than meaningfully lateralized.

MRI assesses stalk thickness, posterior-pituitary T1 bright spot, hypothalamus, and sellar/suprasellar structures. Normal stalk measurements reported in one pediatric review were 3.25 ± 0.56 mm at the optic chiasm and 1.91 ± 0.40 mm at pituitary insertion; proposed thickening categories were mild 3–3.9 mm, moderate 4–6.5 mm, and severe >6.5 mm. (moszczynska2022pituitarystalkthickening pages 6-9)

## 8. Temporal development

Dominant familial AVP-D usually has childhood onset and gradual progression; rare recessive defects may present earlier. Acquired postoperative or traumatic AVP-D can begin acutely and may be transient, permanent, or triphasic after stalk injury. Tumor, LCH, and autoimmune disease may initially appear “idiopathic” and declare themselves months or years later. (spiess2020roleofprotein pages 1-5, iorgi2014centraldiabetesinsipidus pages 1-2)

In 85 children/young adults, 28.2% received an etiologic diagnosis at presentation and another 13% within 2.5 years, including seven germinomas and four LCH cases. Serial MRI was performed every six months for two years and annually for three years; permanent anterior pituitary deficits occurred in 53%. (iorgi2014centraldiabetesinsipidus pages 1-2)

Hereditary AVP-D is lifelong but controllable. Acquired disease may remit if postoperative or inflammatory injury is transient; permanent axonal loss or genetic disease does not spontaneously remit. Critical windows include immediate postoperative fluid monitoring and the first several years after unexplained pediatric AVP-D/stalk thickening, when occult germinoma or LCH may emerge. (hana2020pituitarystalkenlargement pages 11-12)

## 9. Inheritance and population

AVP-D has an approximate prevalence of **1 in 25,000**, although robust population-based incidence data are sparse. A 2024 review estimated hereditary DI at <10% of all DI. In a Danish adult clinical cohort, 7/222 (3.2%) cases were congenital and 215/222 (96.8%) acquired, illustrating referral practice rather than population prevalence. (tomkins2026bestpractice&a pages 5-6, jasmeen2024diabetesinsipidustypes pages 1-3)

Isolated AVP-related FNDI is usually **autosomal dominant**, with high/complete penetrance reported for many pedigrees and variable age-dependent expressivity. Rare autosomal-recessive disease follows biallelic inheritance. No convincing anticipation is known. Both sexes are affected in autosomal disease; broad clinical reviews report no major sex disparity. (jasmeen2024diabetesinsipidustypes pages 1-3, spiess2020roleofprotein pages 1-5)

No reliable global carrier frequency, ethnic prevalence gradient, or geographic endemicity is established. Particular variants may cluster in individual extended families. Consanguinity is relevant mainly to rare recessive disease.

## 10. Diagnostics

### 10.1 Clinical and biochemical approach

1. Confirm polyuria: **>50 mL/kg/day or >3 L/day** in adults.
2. Demonstrate hypotonic urine and exclude uncontrolled diabetes mellitus, hypercalcemia, hypokalemia, renal impairment, diuretics, and other osmotic diureses.
3. Measure paired serum sodium/plasma osmolality and urine osmolality. With hypernatremia, urine osmolality <300 mOsm/kg supports an AVP disorder, whereas >700 mOsm/kg indicates preserved antidiuresis.
4. Distinguish AVP-D from AVP resistance and primary polydipsia with stimulated copeptin or, where unavailable, supervised water deprivation plus desmopressin.
5. Once AVP-D is established, perform contrast-enhanced hypothalamic–pituitary MRI and assess all anterior pituitary axes. (tomkins2026bestpractice& pages 5-6, tomkins2026bestpractice&a pages 5-6)

Traditional water deprivation has approximately 70% overall accuracy and only 41% accuracy for primary polydipsia in the cited review; chronic polyuria blunts the renal concentrating gradient, making partial disease difficult. The test can cause severe dehydration and should not be performed unsupervised or in an already hypernatremic patient. (jasmeen2024diabetesinsipidustypes pages 1-3)

**Copeptin:** copeptin is the stable C-terminal prepro-AVP fragment. Baseline copeptin >21.4 pmol/L strongly supports AVP resistance. Hypertonic-saline-stimulated copeptin is the most accurate modern test but requires frequent sodium measurement and specialist supervision. (tomkins2026bestpractice& pages 5-6, christcrain2021diabetesinsipidus pages 9-9)

The 2023 multicenter head-to-head trial used arginine 0.5 g/kg (maximum 40 g) over 30 minutes and compared it with 3% saline stimulation. Prespecified 60-minute arginine thresholds were <2.4 pmol/L for complete AVP-D, 2.4–3.8 pmol/L for partial AVP-D, and >3.8 pmol/L for primary polydipsia. The definitive report is Refardt et al., *New England Journal of Medicine*, published November 2023, DOI [10.1056/NEJMoa2306263](https://doi.org/10.1056/NEJMoa2306263), NCT03572166. Hypertonic saline remained more accurate; arginine is simpler but should not be treated as equivalent in indeterminate cases. (indirli2024copeptinasa pages 23-27, blocher2024posttraumatichypopituitarism pages 11-12)

### 10.2 Imaging, pathology, and differential diagnosis

MRI loss of the posterior bright spot is supportive but neither necessary nor specific. Stalk thickening requires evaluation for germinoma, LCH, hypophysitis, neurosarcoidosis, tuberculosis, metastasis, lymphoma, congenital lesions, and adjacent tumors. Adult stalk-lesion series averaged 24% neoplastic, 28% inflammatory, 11% congenital, and 37% unknown. Whole-body CT/PET, tumor markers, ACE, IgG4, and biopsy of a safer extracranial lesion may identify the cause. (hana2020pituitarystalkenlargement pages 2-4)

If isolated stalk enlargement remains unexplained, repeat clinical, hormonal, and MRI assessment at 3–12 months. Pediatric guidance supports pituitary testing every six months for 2–3 years and MRI every six months for two years, with subsequent risk-based surveillance. Stalk biopsy is reserved for progression or strong tumor suspicion because it can cause permanent deficits. (hana2020pituitarystalkenlargement pages 11-12)

### 10.3 Genetic testing

Offer testing when onset is familial, early, progressive without a structural cause, or syndromic. Sequence **AVP** first for isolated familial central DI; a broader panel/WES should include genes for congenital hypothalamic–pituitary disorders and syndromes such as Wolfram disease. Copy-number analysis is appropriate if sequencing is negative and recessive/deletion disease is suspected. WGS may detect structural or noncoding variants after negative panel/WES. CMA, karyotype, FISH, mitochondrial testing, and repeat-expansion testing are not routine for isolated FNDI unless another phenotype indicates them. Cascade testing and genetic counseling are appropriate after identifying a familial variant. (christcrain2021diabetesinsipidus pages 9-9, spiess2020roleofprotein pages 1-5)

No validated RNA-seq, proteomic, metabolomic, epigenomic, or liquid-biopsy diagnostic is currently used.

## 11. Outcome and prognosis

With reliable water access, intact thirst, desmopressin, education, and monitoring, isolated hereditary AVP-D is compatible with long survival; disease-specific 5- or 10-year survival estimates are not available. Prognosis in acquired AVP-D is dominated by the underlying tumor, infiltrative disorder, hypothalamic injury, anterior pituitary deficits, and dysnatremia.

The patient survey documented outpatient hyponatremia in 22%, dysnatremia requiring admission in 35%, hypernatremia requiring admission in 15%, reduced quality of life in 64%, and psychological changes in 36%. (atila2022centraldiabetesinsipidus pages 9-13)

In Swedish craniopharyngioma data, DI and hypopituitarism were negative prognostic factors. Childhood-onset craniopharyngioma had an SMR of 17 (95% CI 6.3–37), versus 3.5 (2.6–4.6) for adult onset, but these risks cannot be attributed to AVP-D alone. (olsson2015excessmortalityand pages 1-2)

Complications include hypo- or hypernatremic encephalopathy, seizures/coma, dehydration, hypovolemia, thromboembolism in severely dehydrated perioperative patients, sleep disruption, psychological burden, and dilatation of the urinary tract after longstanding massive urine flow. Prognostic factors include preserved thirst, treatment access/adherence, cognitive capacity, lesion type, anterior-pituitary involvement, and quality of inpatient fluid management. (atila2022centraldiabetesinsipidus pages 16-19, tomkins2026bestpractice& pages 7-9)

## 12. Treatment

### 12.1 Standard pharmacotherapy

**Desmopressin (dDAVP)** is first-line treatment. It is a synthetic AVP analogue with predominantly V2-receptor antidiuretic activity and can be given orally, sublingually, intranasally, or parenterally. Oral formulations generally provide the best safety/tolerability profile; dose and schedule must be individualized to symptom control while allowing intermittent aquaresis. Suggested NCIt concept: *Desmopressin* and *Hormone Replacement Therapy*; identifiers require NCIt-release validation. (atila2022centraldiabetesinsipidus pages 1-5, christcrain2021diabetesinsipidus pages 9-9)

Acute hypernatremic dehydration requires calculated fluid replacement, careful sodium correction, and desmopressin. Underlying tumors, infection, inflammation, or infiltrative disease require cause-specific therapy. Adipsic AVP-D requires scheduled fluids, daily weight/sodium-guided plans, and caregiver support.

A 2024 Danish registry study of 222 adults found a median oral-equivalent daily dose of 600 µg in congenital versus 200 µg in acquired disease (p=0.005). Among acquired cases, 30.7% had sodium <136 mmol/L and 9.3% <131 mmol/L in the preceding year; administration route and BMI did not significantly affect hyponatremia risk. These observational findings do not define a universal dose. DOI: [10.1055/a-2198-7207](https://doi.org/10.1055/a-2198-7207), published 2024.

### 12.2 Safety and implementation

The main chronic adverse effect is dilutional hyponatremia from continuous antidiuresis plus excess drinking. Delaying or omitting a scheduled dose until aquaresis occurs lowers risk. In the survey, this strategy was associated with less hyponatremia (OR 0.55, 95% CI 0.39–0.77; p=0.0006). (atila2022centraldiabetesinsipidus pages 1-5)

Conversely, missed dDAVP or restricted water can be fatal. NHS England recorded 471 incidents in 2009–2015, including 76 dose omissions; four omissions caused death from severe dehydration. Hospitals should treat dDAVP as time-critical, ensure 24-hour availability, prescribe fluids explicitly, monitor sodium/urine balance, and involve endocrinology. (atila2022centraldiabetesinsipidus pages 16-19, tomkins2026bestpractice& pages 7-9)

There is no established pharmacogenomic dosing guideline, gene therapy, cell therapy, ASO, siRNA, or CRISPR treatment for human FNDI. Surgery treats the causal mass—not AVP-D itself—and can worsen or create permanent deficiency.

### 12.3 Experimental research

Current studies emphasize better copeptin stimulation and possible coexisting oxytocin deficiency. Examples include NCT03572166 (arginine-stimulated copeptin; completed, 177), NCT05890690 (oral urea/copeptin; completed, 48), NCT06036004 (oxytocin substitution; phase 2, recruiting, 112), and NCT04789148 (intranasal oxytocin; phase 1, recruiting, 40). These oxytocin studies target psychological/social sequelae and do not replace desmopressin.

A 2024 randomized crossover analysis found glucagon did not significantly stimulate oxytocin or distinguish ten AVP-D patients from ten controls, illustrating that oxytocin deficiency remains investigational rather than an established diagnostic entity. DOI: [10.1007/s12020-024-03920-2](https://doi.org/10.1007/s12020-024-03920-2), published June 2024.

## 13. Prevention

**Primary prevention:** genetic AVP-D cannot be prevented after conception. Risk-reducing measures include hypothalamus/stalk-sparing surgery where oncologically feasible and appropriate prevention/treatment of trauma or infection. No vaccine or lifestyle prophylaxis is specific to AVP-D.

**Secondary prevention:** prompt evaluation of persistent polyuria after neurosurgery, trauma, pregnancy-associated pituitary disease, or cancer therapy; family cascade testing; and longitudinal MRI/endocrine surveillance for unexplained pediatric AVP-D. Prenatal or preimplantation testing is technically possible after identifying a familial pathogenic variant and should be offered non-directively through genetic counseling. (iorgi2014centraldiabetesinsipidus pages 1-2, hana2020pituitarystalkenlargement pages 11-12)

**Tertiary prevention:** uninterrupted access to water and dDAVP; medical-alert identification; written sick-day and fasting plans; planned intermittent aquaresis; sodium checks after dose/formulation changes; caregiver education for children or cognitively impaired patients; and hospital alerts against omitted desmopressin. These measures prevent dysnatremia rather than the underlying disease. (atila2022centraldiabetesinsipidus pages 16-19, tomkins2026bestpractice& pages 7-9)

## 14. Other species and natural disease

Central DI occurs naturally in companion animals, especially dogs and cats, from idiopathic, traumatic, neoplastic, or congenital neurohypophyseal disease, and generally responds to desmopressin. However, the retrieved literature did not establish a well-curated naturally occurring breed-specific AVP mutation equivalent to common human dominant FNDI. Breed ontology identifiers and OMIA entries should therefore be populated only after direct veterinary-database verification.

Relevant taxonomy suggestions are *Homo sapiens* (NCBI Taxon 9606), *Mus musculus* (10090), *Rattus norvegicus* (10116), *Canis lupus familiaris* (9615), and *Felis catus* (9685). AVP sequence, neurophysin-dependent processing, AVPR2 signaling, and AQP2-mediated collecting-duct water transport are strongly conserved. The disease is noninfectious and has no zoonotic or cross-species transmission potential.

## 15. Model organisms

**Brattleboro rat:** a naturally occurring recessive *Avp* defect causes absent circulating AVP, marked polyuria, and polydipsia. It is useful for renal water-balance physiology and replacement/gene-transfer studies, but it does not reproduce dominant human precursor proteotoxicity.

**AVP-mutant knock-in/transgenic mice:** Cys98stop/C67X and related models reproduce ER retention, aggregate formation, progressive decline in AVP production, and polyuria. Neuron loss is sex-, age-, and model-dependent; some animals develop progressive polyuria without frank neuron death, limiting simple neurodegeneration interpretations. (arima2014endoplasmicreticulumstress pages 2-3, spiess2020roleofprotein pages 8-10)

**ERAD-deficient mice:** neuronal Sel1L/HRD1 disruption causes wild-type AVP aggregation and DI, demonstrating the importance of ER quality control. (spiess2020roleofprotein pages 13-18, spiess2020roleofprotein pages 8-10)

**Cell systems:** COS-1, Neuro2A, fibroblast, and neuronal expression systems demonstrate failed ER exit, mutant/wild-type heterodimerization, proteasomal degradation, disulfide-linked fibrils, autophagy, and reduced viability. They are mechanistically useful but lack the long axonal transport and systemic osmotic feedback of magnocellular neurons in vivo. (spiess2020roleofprotein pages 13-18, spiess2020roleofprotein pages 8-10)

Viral AVP rescue in magnocellular neurons of Brattleboro rats reduced water intake and improved DI, providing preclinical proof of concept. It did not normalize all behavioral phenotypes, and no human AVP gene therapy is established.

## Recent developments and expert interpretation

The most consequential 2023–2024 developments are: (1) adoption of **AVP deficiency** terminology to reduce confusion and improve safety; (2) confirmation that hypertonic-saline-stimulated copeptin is more accurate than arginine stimulation, although arginine is operationally simpler; (3) increased emphasis on intermittent aquaresis and prevention of inpatient dDAVP omission; and (4) investigation of concomitant oxytocin deficiency as a contributor to psychosocial morbidity. (atila2022centraldiabetesinsipidus pages 9-13, christcrain2021diabetesinsipidus pages 9-9, indirli2024copeptinasa pages 23-27)

A concise expert conclusion is that AVP-D is usually straightforward to replace hormonally but remains difficult in three domains: correctly distinguishing partial AVP-D from primary polydipsia, establishing the cause of apparently idiopathic stalk disease, and preventing treatment-related dysnatremia. The evidence also cautions against attributing all psychological morbidity directly to AVP or oxytocin deficiency, because hypothalamic injury, associated hormone deficits, sleep disruption, and selection bias remain important confounders. (atila2022centraldiabetesinsipidus pages 9-13, iorgi2014centraldiabetesinsipidus pages 1-2)

## Selected sources with dates and URLs

- Refardt J, Atila C, Christ-Crain M. “New insights on diagnosis and treatment of AVP deficiency.” *Reviews in Endocrine and Metabolic Disorders*. 2024;25:639–649. [https://doi.org/10.1007/s11154-023-09862-w](https://doi.org/10.1007/s11154-023-09862-w).
- Refardt J et al. “Arginine or Hypertonic Saline–Stimulated Copeptin to Diagnose AVP Deficiency.” *New England Journal of Medicine*. November 2023;389:1877–1887. [https://doi.org/10.1056/NEJMoa2306263](https://doi.org/10.1056/NEJMoa2306263). (blocher2024posttraumatichypopituitarism pages 11-12)
- Atila C et al. “Central diabetes insipidus from a patient’s perspective.” *Lancet Diabetes & Endocrinology*. October 2022;10:700–709. [https://doi.org/10.1016/S2213-8587(22)00219-4](https://doi.org/10.1016/S2213-8587(22)00219-4). Direct abstract-level conclusion: the study documented “management, psychological co-morbidities, and renaming” concerns across an international patient cohort. (atila2022centraldiabetesinsipidus pages 9-13)
- Pedersen AN et al. “Desmopressin Dose Requirements in Adults with Congenital and Acquired Central Diabetes Insipidus.” *Hormone and Metabolic Research*. 2024;56:206–213. [https://doi.org/10.1055/a-2198-7207](https://doi.org/10.1055/a-2198-7207).
- Spiess M et al. “Role of protein aggregation and degradation in autosomal dominant neurohypophyseal diabetes insipidus.” *Molecular and Cellular Endocrinology*. February 2020;501:110653. [https://doi.org/10.1016/j.mce.2019.110653](https://doi.org/10.1016/j.mce.2019.110653). (spiess2020roleofprotein pages 1-5)
- Di Iorgi N et al. “Central diabetes insipidus in children and young adults.” *Journal of Clinical Endocrinology & Metabolism*. April 2014;99:1264–1272. [https://doi.org/10.1210/jc.2013-3724](https://doi.org/10.1210/jc.2013-3724). (iorgi2014centraldiabetesinsipidus pages 1-2)

**Evidence limitation:** PMID values were included only where explicitly recovered from Open Targets. DOI links are supplied for other publications rather than risking incorrect PMID assignment. Exact ontology, ICD-11, OMIM, ClinVar-classification, gnomAD-frequency, NCIt, GO, CL, and UBERON identifiers should be release-validated before database ingestion.

References

1. (atila2022centraldiabetesinsipidus pages 1-5): Cihan Atila, Paul Benjamin Loughrey, Aoife Garrahy, Bettina Winzeler, Julie Refardt, Patricia Gildroy, Malak Hamza, Aparna Pal, Joseph G Verbalis, Christopher J Thompson, Lars G Hemkens, Steven J Hunter, Mark Sherlock, Miles J Levy, Niki Karavitaki, John Newell-Price, John A H Wass, and Mirjam Christ-Crain. Central diabetes insipidus from a patient's perspective: management, psychological co-morbidities, and renaming of the condition: results from an international web-based survey. The Lancet Diabetes &amp; Endocrinology, 10(10):700-709, Oct 2022. URL: https://doi.org/10.1016/s2213-8587(22)00219-4, doi:10.1016/s2213-8587(22)00219-4. This article has 104 citations and is from a highest quality peer-reviewed journal.

2. (onwuka2025physiologicalbasisof pages 1-3): Osah Martins Onwuka. Physiological basis of arginine vasopressin deficiency (avp-d, formerly central diabetes insipidus) and avp-resistance (avp-r, formerly nephrogenic diabetes insipidus). Exploration of Medicine, Feb 2025. URL: https://doi.org/10.37349/emed.2025.1001289, doi:10.37349/emed.2025.1001289. This article has 5 citations.

3. (OpenTargets Search: neurohypophyseal diabetes insipidus-AVP): Open Targets Query (neurohypophyseal diabetes insipidus-AVP, 17 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

4. (tomkins2026bestpractice&a pages 5-6): M Tomkins, D Mc Donald, and D Green. Best practice & research clinical endocrinology & metabolism. Unknown journal, 2026.

5. (jasmeen2024diabetesinsipidustypes pages 1-3): Jasmeen, Phoebe Vitubisgho Nyirenda, Navneet Khurana, Rakhi Mishra, Jasmine Chaudhary, and Navneet Duggal. Diabetes insipidus: types, diagnosis and management. BIO Web of Conferences, 86:01016, Jan 2024. URL: https://doi.org/10.1051/bioconf/20248601016, doi:10.1051/bioconf/20248601016. This article has 2 citations.

6. (hana2020pituitarystalkenlargement pages 2-4): Václav Hána, Sylvie Salenave, and Philippe Chanson. Pituitary stalk enlargement in adults. Neuroendocrinology, 110:809-821, Feb 2020. URL: https://doi.org/10.1159/000506641, doi:10.1159/000506641. This article has 16 citations and is from a peer-reviewed journal.

7. (moszczynska2022pituitarystalkthickening pages 1-2): Elżbieta Moszczyńska, Karolina Kunecka, Marta Baszyńska-Wilk, Marta Perek-Polnik, Dorota Majak, and `Wiesława Grajkowska. Pituitary stalk thickening: causes and consequences. the children’s memorial health institute experience and literature review. Frontiers in Endocrinology, May 2022. URL: https://doi.org/10.3389/fendo.2022.868558, doi:10.3389/fendo.2022.868558. This article has 30 citations.

8. (atila2022centraldiabetesinsipidus pages 9-13): Cihan Atila, Paul Benjamin Loughrey, Aoife Garrahy, Bettina Winzeler, Julie Refardt, Patricia Gildroy, Malak Hamza, Aparna Pal, Joseph G Verbalis, Christopher J Thompson, Lars G Hemkens, Steven J Hunter, Mark Sherlock, Miles J Levy, Niki Karavitaki, John Newell-Price, John A H Wass, and Mirjam Christ-Crain. Central diabetes insipidus from a patient's perspective: management, psychological co-morbidities, and renaming of the condition: results from an international web-based survey. The Lancet Diabetes &amp; Endocrinology, 10(10):700-709, Oct 2022. URL: https://doi.org/10.1016/s2213-8587(22)00219-4, doi:10.1016/s2213-8587(22)00219-4. This article has 104 citations and is from a highest quality peer-reviewed journal.

9. (spiess2020roleofprotein pages 1-5): Martin Spiess, Michael Friberg, Nicole Beuret, Cristina Prescianotto-Baschong, and Jonas Rutishauser. Role of protein aggregation and degradation in autosomal dominant neurohypophyseal diabetes insipidus. Feb 2020. URL: https://doi.org/10.1016/j.mce.2019.110653, doi:10.1016/j.mce.2019.110653. This article has 15 citations and is from a peer-reviewed journal.

10. (koufaris2015identificationofan pages 3-4): Costas Koufaris, Angelos Alexandrou, Carolina Sismani, and Nicos Skordis. Identification of an avp-npii mutation within the avp moiety in a family with neurohypophyseal diabetes insipidus: review of the literature. Hormones, 14:442-446, Jul 2015. URL: https://doi.org/10.14310/horm.2002.1604, doi:10.14310/horm.2002.1604. This article has 10 citations and is from a peer-reviewed journal.

11. (arima2014endoplasmicreticulumstress pages 2-3): Hiroshi Arima, Yoshiaki Morishita, Daisuke Hagiwara, Masayuki Hayashi, and Yutaka Oiso. Endoplasmic reticulum stress in vasopressin neurons of familial diabetes insipidus model mice: aggregate formation and mrna poly(a) tail shortening. Experimental Physiology, 99:66-71, Jan 2014. URL: https://doi.org/10.1113/expphysiol.2013.072553, doi:10.1113/expphysiol.2013.072553. This article has 13 citations and is from a peer-reviewed journal.

12. (spiess2020roleofprotein pages 8-10): Martin Spiess, Michael Friberg, Nicole Beuret, Cristina Prescianotto-Baschong, and Jonas Rutishauser. Role of protein aggregation and degradation in autosomal dominant neurohypophyseal diabetes insipidus. Feb 2020. URL: https://doi.org/10.1016/j.mce.2019.110653, doi:10.1016/j.mce.2019.110653. This article has 15 citations and is from a peer-reviewed journal.

13. (spiess2020roleofprotein pages 5-8): Martin Spiess, Michael Friberg, Nicole Beuret, Cristina Prescianotto-Baschong, and Jonas Rutishauser. Role of protein aggregation and degradation in autosomal dominant neurohypophyseal diabetes insipidus. Feb 2020. URL: https://doi.org/10.1016/j.mce.2019.110653, doi:10.1016/j.mce.2019.110653. This article has 15 citations and is from a peer-reviewed journal.

14. (tomkins2026bestpractice& pages 5-6): M Tomkins, D Mc Donald, and D Green. Best practice & research clinical endocrinology & metabolism. Unknown journal, 2026.

15. (indirli2024copeptinasa pages 23-27): R Indirli. Copeptin as a surrogate marker of arginine vasopressin: clinical diagnostic and prognostic applications in endocrine and non-endocrine diseases. Unknown journal, 2024.

16. (iorgi2014centraldiabetesinsipidus pages 1-2): Natascia Di Iorgi, Anna Elsa Maria Allegri, Flavia Napoli, Annalisa Calcagno, Erika Calandra, Nadia Fratangeli, Marianna Vannati, Andrea Rossi, Francesca Bagnasco, Riccardo Haupt, and Mohamad Maghnie. Central diabetes insipidus in children and young adults: etiological diagnosis and long-term outcome of idiopathic cases. The Journal of clinical endocrinology and metabolism, 99 4:1264-72, Apr 2014. URL: https://doi.org/10.1210/jc.2013-3724, doi:10.1210/jc.2013-3724. This article has 134 citations.

17. (hana2020pituitarystalkenlargement pages 11-12): Václav Hána, Sylvie Salenave, and Philippe Chanson. Pituitary stalk enlargement in adults. Neuroendocrinology, 110:809-821, Feb 2020. URL: https://doi.org/10.1159/000506641, doi:10.1159/000506641. This article has 16 citations and is from a peer-reviewed journal.

18. (christcrain2021diabetesinsipidus pages 9-9): M Christ-Crain, DG Bichet, and WK Fenske. Diabetes insipidus. Dec 2021. URL: https://doi.org/10.1016/j.lpm.2021.104093, doi:10.1016/j.lpm.2021.104093. This article has 368 citations.

19. (atila2022centraldiabetesinsipidus pages 16-19): Cihan Atila, Paul Benjamin Loughrey, Aoife Garrahy, Bettina Winzeler, Julie Refardt, Patricia Gildroy, Malak Hamza, Aparna Pal, Joseph G Verbalis, Christopher J Thompson, Lars G Hemkens, Steven J Hunter, Mark Sherlock, Miles J Levy, Niki Karavitaki, John Newell-Price, John A H Wass, and Mirjam Christ-Crain. Central diabetes insipidus from a patient's perspective: management, psychological co-morbidities, and renaming of the condition: results from an international web-based survey. The Lancet Diabetes &amp; Endocrinology, 10(10):700-709, Oct 2022. URL: https://doi.org/10.1016/s2213-8587(22)00219-4, doi:10.1016/s2213-8587(22)00219-4. This article has 104 citations and is from a highest quality peer-reviewed journal.

20. (olsson2015excessmortalityand pages 1-2): Daniel S. Olsson, Eva Andersson, Ing-Liss Bryngelsson, Anna G. Nilsson, and Gudmundur Johannsson. Excess mortality and morbidity in patients with craniopharyngioma, especially in patients with childhood onset: a population-based study in sweden. The Journal of clinical endocrinology and metabolism, 100 2:467-74, Feb 2015. URL: https://doi.org/10.1210/jc.2014-3525, doi:10.1210/jc.2014-3525. This article has 235 citations.

21. (arima2014endoplasmicreticulumstress pages 1-2): Hiroshi Arima, Yoshiaki Morishita, Daisuke Hagiwara, Masayuki Hayashi, and Yutaka Oiso. Endoplasmic reticulum stress in vasopressin neurons of familial diabetes insipidus model mice: aggregate formation and mrna poly(a) tail shortening. Experimental Physiology, 99:66-71, Jan 2014. URL: https://doi.org/10.1113/expphysiol.2013.072553, doi:10.1113/expphysiol.2013.072553. This article has 13 citations and is from a peer-reviewed journal.

22. (moszczynska2022pituitarystalkthickening pages 6-9): Elżbieta Moszczyńska, Karolina Kunecka, Marta Baszyńska-Wilk, Marta Perek-Polnik, Dorota Majak, and `Wiesława Grajkowska. Pituitary stalk thickening: causes and consequences. the children’s memorial health institute experience and literature review. Frontiers in Endocrinology, May 2022. URL: https://doi.org/10.3389/fendo.2022.868558, doi:10.3389/fendo.2022.868558. This article has 30 citations.

23. (iglesias2024anupdateon pages 26-27): Pedro Iglesias. An update on advances in hypopituitarism: etiology, diagnosis, and current management. Oct 2024. URL: https://doi.org/10.3390/jcm13206161, doi:10.3390/jcm13206161. This article has 44 citations.

24. (spiess2020roleofprotein pages 10-13): Martin Spiess, Michael Friberg, Nicole Beuret, Cristina Prescianotto-Baschong, and Jonas Rutishauser. Role of protein aggregation and degradation in autosomal dominant neurohypophyseal diabetes insipidus. Feb 2020. URL: https://doi.org/10.1016/j.mce.2019.110653, doi:10.1016/j.mce.2019.110653. This article has 15 citations and is from a peer-reviewed journal.

25. (spiess2020roleofprotein pages 13-18): Martin Spiess, Michael Friberg, Nicole Beuret, Cristina Prescianotto-Baschong, and Jonas Rutishauser. Role of protein aggregation and degradation in autosomal dominant neurohypophyseal diabetes insipidus. Feb 2020. URL: https://doi.org/10.1016/j.mce.2019.110653, doi:10.1016/j.mce.2019.110653. This article has 15 citations and is from a peer-reviewed journal.

26. (blocher2024posttraumatichypopituitarism pages 11-12): Nissa Blocher. Post-traumatic hypopituitarism. Current Physical Medicine and Rehabilitation Reports, 12:405-416, Sep 2024. URL: https://doi.org/10.1007/s40141-024-00468-0, doi:10.1007/s40141-024-00468-0. This article has 5 citations.

27. (tomkins2026bestpractice& pages 7-9): M Tomkins, D Mc Donald, and D Green. Best practice & research clinical endocrinology & metabolism. Unknown journal, 2026.

## Artifacts

- [Edison artifact artifact-00](Neurohypophyseal_Diabetes_Insipidus-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 20 |
| Resolved | 18 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 2 |
| References weighed for topical relevance | 18 |
| On topic | 3 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `DOI:10.1055/a-2198-7207` (6 mentions) - Desmopressin Dose Requirements in Adults with Congenital and Acquired
                    Central Diabetes Insipidus
  - shared terms: primary, type

Weighed against this report's own most characteristic terms: `disease`, `avp`, `clinical`, `avp-d`, `gene`, `genetic`, `treatment`, `cause`, `variant`, `water`, `include`, `pituitary`, `primary`, `human`, `hypothalamic`, `model`, `dominant`, `type`, `stalk`, `cell`.

18 of 20 references resolved; the rest could not be looked up either way.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 3 |
| Resolved | 2 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 1 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0007450` (5 mentions) - the report calls it "if available"; MONDO calls it **neurohypophyseal diabetes insipidus**

### Prefixes with no resolver

Terms carrying these prefixes were not checked either way, because no configured ontology covers them. An unrecognised prefix may name an ontology this run could not reach as easily as one that does not exist, so nothing here is evidence of fabrication: `ORPHA`.