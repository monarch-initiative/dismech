---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-17T12:41:28.748785'
end_time: '2026-09-17T12:54:18.609345'
duration_seconds: 769.86
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: GUCA1A-Related Retinopathy
  mondo_id: MONDO:0700376
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 39
reference_validation:
  total_references: 10
  verified: 10
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 10
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 1
  verified: 1
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0700376
    reported_labels:
    - if available
    - GUCA1A-related retinopathy
    ontology_label: GUCA1A-related retinopathy
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: GUCA1A-Related_Retinopathy-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** GUCA1A-Related Retinopathy
- **MONDO ID:** MONDO:0700376 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **GUCA1A-Related Retinopathy** covering all of the
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
- **Disease Name:** GUCA1A-Related Retinopathy
- **MONDO ID:** MONDO:0700376 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **GUCA1A-Related Retinopathy** covering all of the
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


# GUCA1A-Related Retinopathy: Disease Characteristics Research Report

## Executive summary

**GUCA1A-related retinopathy** (MONDO:0700376) is a rare, nonsyndromic, usually autosomal-dominant inherited retinal disease caused by heterozygous missense variants in **GUCA1A**, which encodes guanylate cyclase-activating protein 1 (**GCAP1**). It forms a phenotypic continuum encompassing macular dystrophy, cone dystrophy, cone–rod dystrophy and, rarely, an RP-like generalized degeneration. The core manifestations are progressive, bilateral central visual loss, impaired color discrimination and photophobia, with outer-retinal/macular atrophy and cone-predominant electroretinographic dysfunction. The best quantitative disease-specific natural-history evidence is a 2025 retrospective cohort of 19 patients from 14 families; no comparably comprehensive 2023–2024 clinical cohort was retrieved. (OpenTargets Search: GUCA1A-related retinopathy-GUCA1A, allon2025clinicalgeneticimaging pages 1-2, allon2025clinicalgeneticimaging pages 4-5)

The principal mechanism is not simple haploinsufficiency. Most pathogenic GCAP1 variants impair Ca²⁺ sensing and permit inappropriate activation of retinal guanylate cyclase at Ca²⁺ concentrations that should inhibit it, disturbing cGMP/Ca²⁺ homeostasis and ultimately injuring photoreceptors. There is currently no approved GUCA1A-specific disease-modifying treatment or relevant human interventional trial in the retrieved evidence. AAV-delivered RNA interference has delayed degeneration and improved function in mutant-GCAP1 mice, but remains preclinical. (marino2018anovelp.(glu111val) pages 3-3, kitiratschky2009mutationsinthe pages 1-3, dell’orco2019normalgcapspartly pages 1-2, jiang2013rnaimediatedgenesuppression pages 13-13)

The following compact table is suitable for initial knowledge-base ingestion.

| Knowledge-base field | Evidence-based summary | Suggested ontology mapping | Evidence |
|---|---|---|---|
| Disease identity | Rare inherited retinal dystrophy spanning macular dystrophy, cone dystrophy, cone–rod dystrophy and, less often, an RP-like phenotype; designated **GUCA1A-related retinopathy**. | **MONDO:0700376** | (OpenTargets Search: GUCA1A-related retinopathy-GUCA1A, allon2025clinicalgeneticimaging pages 1-2) |
| Gene/protein | **GUCA1A** encodes guanylate cyclase-activating protein 1 (**GCAP1**), a neuronal calcium sensor expressed in rod and cone photoreceptors and involved in recovery of phototransduction. | Suggested gene/protein annotations: **GUCA1A**, **GCAP1** | (kitiratschky2009mutationsinthe pages 1-3, marino2018anovelp.(glu111val) pages 1-1) |
| Inheritance | Predominantly **autosomal dominant**, caused by heterozygous germline missense variants; multigenerational disease was present in 13 of 14 families in the largest reported cohort. Penetrance is not reliably quantified, and expressivity is highly variable. | Suggested HPO: *Autosomal dominant inheritance* | (allon2025clinicalgeneticimaging pages 4-5, marino2018anovelp.(glu111val) pages 8-9, kitiratschky2009mutationsinthe pages 1-3) |
| Core phenotypes | Progressive bilateral central visual loss, impaired color discrimination and photophobia; central/paracentral scotomas, macular/outer-retinal atrophy and reduced cone ERG responses are typical. Rod dysfunction is usually absent or later/milder, but severe cone–rod disease occurs. | Suggested HPO: *Progressive visual loss*, *Reduced visual acuity*, *Abnormal color vision*, *Photophobia*, *Central scotoma*, *Macular atrophy*, *Cone dystrophy*, *Cone-rod dystrophy*, *Abnormal electroretinogram*, *Nystagmus* | (allon2025clinicalgeneticimaging pages 4-5, allon2025clinicalgeneticimaging pages 5-10, marino2018anovelp.(glu111val) pages 2-3) |
| Mechanism | Missense variants—often affecting GCAP1 EF-hand calcium-sensing regions—reduce calcium sensitivity and permit persistent retinal guanylate-cyclase activation at calcium concentrations that should inhibit it. This dysregulates cGMP and Ca²⁺ homeostasis and leads to photoreceptor dysfunction and degeneration; the final cell-death pathway is supported strongly by models but is not fully resolved in humans. | Suggested GO biological processes: *visual phototransduction*, *phototransduction recovery*, *calcium ion sensing*, *regulation of guanylate cyclase activity*, *cGMP biosynthetic process*, *calcium ion homeostasis*, *photoreceptor cell death* | (marino2018anovelp.(glu111val) pages 3-3, kitiratschky2009mutationsinthe pages 1-3, dell’orco2019normalgcapspartly pages 1-2, payne1998amutationin pages 3-3) |
| Cells/anatomy | Primary targets are macular cone photoreceptors and, variably, rod photoreceptors; abnormalities begin in the outer photoreceptor/ellipsoid-zone region. RPE involvement occurs with advanced human maculopathy and in zebrafish models. Disease is generally bilateral and highly symmetric. | Suggested CL: *cone photoreceptor cell*, *rod photoreceptor cell*, *retinal pigment epithelial cell*. Suggested UBERON: *retina*, *macula*, *neural retina*, *photoreceptor outer segment*, *retinal pigment epithelium* | (allon2025clinicalgeneticimaging pages 10-13, allon2025clinicalgeneticimaging pages 13-13, chen2017guca1amutationcauses pages 7-8) |
| Diagnostics | Clinical assessment should combine visual acuity and color-vision evaluation with fundus examination, fundus autofluorescence, macular SD-OCT, visual fields and ISCEV-standard pattern/full-field ERG. Molecular confirmation can use an inherited-retinal-disease panel, WES or WGS, followed by Sanger/segregation testing and ACMG/AMP interpretation. | Suggested HPO-linked findings: *Ellipsoid-zone disruption*, *Outer retinal atrophy*, *Central scotoma*, *Reduced cone ERG response* | (allon2025clinicalgeneticimaging pages 4-5, marino2018anovelp.(glu111val) pages 2-3, allon2025clinicalgeneticimaging pages 10-13, allon2025clinicalgeneticimaging pages 2-4) |
| Prognosis | Chronic, generally progressive and nonlethal. In 19 patients, mean onset was 23 years (range 5–74), and visual acuity worsened by approximately **0.20 logMAR per decade**, although severity ranged from preserved acuity beyond age 70 to no light perception. Possible variant-specific and sex effects require confirmation. | Suggested HPO: *Variable age at onset*, *Progressive visual impairment*, *Variable expressivity* | (allon2025clinicalgeneticimaging pages 1-2, allon2025clinicalgeneticimaging pages 4-5, allon2025clinicalgeneticimaging pages 10-10) |
| Treatment status | No GUCA1A-specific approved disease-modifying therapy or relevant registered interventional trial was identified in the gathered evidence. Present care is supportive and rehabilitative. AAV8-delivered RNA interference delayed degeneration and improved function in mutant-GCAP1 mice, but remains preclinical and carries normal-allele suppression/off-target concerns. | Suggested NCIT intervention concepts: *Low Vision Rehabilitation*, *Genetic Counseling*, *Gene Silencing Therapy*, *Adeno-Associated Virus Vector Therapy* | (jiang2013rnaimediatedgenesuppression pages 13-13, jiang2013rnaimediatedgenesuppression pages 1-2, jiang2012rnainterferencegene pages 158-159) |
| Experimental models | Engineered mouse models include transgenic **Y99C**, transgenic **L151F** and knock-in **E155G**, which reproduce dominant, progressive photoreceptor dysfunction with cone-predominant degeneration. Zebrafish overexpressing human **R120L** show photoreceptor and RPE disruption. These are induced genetic models, not documented natural veterinary disease. | Suggested model annotations: *Mus musculus genetic disease model*; *Danio rerio overexpression model* | (jiang2013rnaimediatedgenesuppression pages 13-13, dell’orco2019normalgcapspartly pages 1-2, chen2017guca1amutationcauses pages 7-8) |
| Evidence gaps | Disease-specific incidence, population prevalence, penetrance, carrier frequency, founder effects, validated modifier genes, environmental or protective factors, gene–environment interactions, epigenetic signatures, human single-cell/spatial multi-omics, standardized quality-of-life data, natural animal disease and human treatment-response rates are not established in the gathered evidence. | No ontology assignment recommended until evidence is available. | (allon2025clinicalgeneticimaging pages 2-4, avesani2026retinalnetworkdysfunction pages 12-14, allon2025clinicalgeneticimaging pages 1-2) |


*Table: Compact evidence table covering disease identity, genetics, phenotype, mechanism, diagnostic approach, prognosis, treatment status, experimental models and major knowledge gaps. Ontology mappings are explicitly suggested rather than asserted.*

## 1. Disease information

### Definition and scope

GUCA1A-related retinopathy is a **Mendelian photoreceptor degeneration** in which cone dysfunction usually dominates. Clinical labels historically assigned to affected families include:

- GUCA1A-associated/related retinopathy or retinal dystrophy;
- GCAP1-related retinopathy;
- autosomal-dominant cone dystrophy, historically **cone dystrophy 3/COD3**;
- autosomal-dominant cone–rod dystrophy;
- GUCA1A-related macular dystrophy or maculopathy;
- central areolar choroidal dystrophy-like maculopathy;
- rarely, an RP-like phenotype. (allon2025clinicalgeneticimaging pages 1-2, chen2017guca1amutationcauses pages 7-8, georgiou2020retinalimagingin pages 13-15)

The foundational 1998 report identified p.Tyr99Cys in an autosomal-dominant cone-dystrophy pedigree. A later clinical series established that GUCA1A variants can cause “cone, cone-rod, and macular dystrophy” (Michaelides et al., *Ophthalmology*, August 2005; PMID **15953638**). (payne1998amutationin pages 3-3, georgiou2020retinalimagingin pages 13-15)

### Identifiers

- **MONDO:** MONDO:0700376, GUCA1A-related retinopathy; Open Targets maps this entity principally to GUCA1A/ENSG00000048545. (OpenTargets Search: GUCA1A-related retinopathy-GUCA1A)
- **Gene:** GUCA1A; approved name *guanylate cyclase activator 1A*.
- A disease-specific **ICD-10, ICD-11 or MeSH code was not established in the retrieved sources**; implementation should use a broader inherited retinal/cone–rod dystrophy code plus the molecular diagnosis.
- OMIM/Orphanet identifiers should be verified directly against those live resources before database ingestion; the retrieved primary texts did not provide a sufficiently reliable disease-level identifier.

This report synthesizes **aggregated disease-level literature and retrospective cohorts**, not individual EHR records. The 2025 study used molecularly confirmed clinical records from a specialist referral center. (allon2025clinicalgeneticimaging pages 4-5, allon2025clinicalgeneticimaging pages 1-2)

## 2. Etiology, risk and protective factors

### Causal factor

The primary cause is a **heterozygous germline GUCA1A missense variant**, generally producing altered-function GCAP1. Familial segregation and multigenerational transmission support autosomal-dominant causality. All 19 patients in the largest cohort carried pathogenic or likely pathogenic heterozygous missense alleles. (allon2025clinicalgeneticimaging pages 5-10, marino2018anovelp.(glu111val) pages 8-9, kitiratschky2009mutationsinthe pages 1-3)

### Genetic risk factors

Disease risk is dominated by carrying a pathogenic allele. Variants frequently affect or perturb the EF-hand Ca²⁺-sensing regions. Documented alleles include p.Tyr99Cys, p.Asp100Glu, p.Asn104His, p.Ile107Thr, p.Glu111Ala/Val, p.Arg120Leu, p.Leu151Phe, p.Glu155Gly, p.Gly159Val, p.Leu176Phe, p.Leu84Phe and p.Glu89Lys. The 2025 cohort contained five alleles: p.Tyr99Cys in 10 of 14 families, with p.Leu84Phe, p.Ile107Thr, p.Glu111Ala and p.Leu176Phe in one family each. (allon2025clinicalgeneticimaging pages 1-2, allon2025clinicalgeneticimaging pages 2-4, marino2018anovelp.(glu111val) pages 3-3, kitiratschky2009mutationsinthe pages 1-3, chen2017guca1amutationcauses pages 7-8)

Family history is therefore a major risk indicator, but apparently sporadic cases may represent de novo variants or unrecognized reduced penetrance. Penetrance is not robustly quantified. Marked inter- and intrafamilial variability is documented; p.Arg120Leu produced maculopathy ranging from mild photoreceptor degeneration to severe central areolar choroidal dystrophy in one five-generation family. (allon2025clinicalgeneticimaging pages 10-10, chen2017guca1amutationcauses pages 7-8, georgiou2020retinalimagingin pages 13-15)

### Modifiers and protective factors

No validated human modifier gene or protective allele has been established. Wild-type GCAP1 partly attenuated E111V-induced cyclase dysregulation in biochemical experiments. Mouse modeling suggested GCAP2 may add compensation, but human GCAP2 did not activate GC1 over the tested physiological Ca²⁺ range; this is a proposed species-dependent compensatory mechanism, not a proven human modifier. (dell’orco2019normalgcapspartly pages 1-2)

No disease-specific protective diet, lifestyle intervention or medication is established. Environmental toxins, smoking, alcohol, occupation, infection, sex and age are **not primary causes**. A 2025 cohort found worse acuity in males, but this exploratory association requires replication. Age predicts accumulated severity rather than genetic susceptibility. (allon2025clinicalgeneticimaging pages 4-5, allon2025clinicalgeneticimaging pages 10-10)

### Gene–environment interaction

No reproducible GUCA1A-specific gene–environment interaction was found. Ordinary light drives the pathway in which GCAP1 functions, but available evidence does not establish routine light exposure as a modifiable cause or prove that light avoidance changes progression.

## 3. Phenotypes

In the 2025 cohort, mean symptom onset was **23 years** (range **5–74**). Initial complaints were impaired color discrimination in 68.4%, central visual loss in 21.1%, photophobia in 5.3% and unremembered in 5.3%. Across follow-up, central visual deficits occurred in 89.5%, color deficits in 84.2% and photophobia in 78.9%; nyctalopia and metamorphopsia each occurred in 5.3%. (allon2025clinicalgeneticimaging pages 4-5, allon2025clinicalgeneticimaging pages 10-10)

| Phenotype | Type and characteristics | Suggested HPO term |
|---|---|---|
| Reduced central visual acuity | Symptom/sign; bilateral, usually progressive; severity ranges from mild loss to no light perception | Reduced visual acuity; Progressive visual loss |
| Abnormal color vision | Symptom; often the earliest complaint and common during follow-up | Abnormality of color vision |
| Photophobia | Symptom; common once cone dysfunction is established | Photophobia |
| Central/paracentral scotoma | Functional sign; reported on available visual fields | Central scotoma; Paracentral scotoma |
| Cone dystrophy | Electrophysiologic/clinical phenotype; 11/13 tested patients in the 2025 cohort | Cone dystrophy; Abnormal cone ERG |
| Cone–rod dystrophy | More severe branch with later or concurrent rod involvement | Cone-rod dystrophy; Abnormal rod ERG |
| Macular dystrophy/atrophy | Structural sign; OCT maculopathy in all 19 recent patients | Macular dystrophy; Macular atrophy |
| Ellipsoid-zone/outer-retinal loss | Imaging sign; begins as irregularity or optical gap and progresses to outer-nuclear-layer/RPE atrophy | Abnormal retinal morphology; Retinal atrophy |
| Nystagmus | Usually severe congenital/early-onset disease, including E111V | Nystagmus |
| Nyctalopia | Uncommon in cone-predominant disease; may occur with generalized rod involvement | Nyctalopia |
| Peripheral pigmentary degeneration | Uncommon; described with some p.Tyr99Cys and p.Glu111Ala cases | Retinal pigmentary degeneration |

These mappings are suggested labels; exact HPO identifiers should be resolved through the current HPO release. The phenotype is generally highly symmetric between eyes. Rod-specific ERGs are often normal, while severe E111V disease can reduce both cone and rod responses. (allon2025clinicalgeneticimaging pages 10-13, allon2025clinicalgeneticimaging pages 5-10, marino2018anovelp.(glu111val) pages 2-3)

No GUCA1A-specific EQ-5D, SF-36, PROMIS or validated vision-related quality-of-life dataset was found. Nevertheless, progressive loss of central acuity, color discrimination and light tolerance predict substantial effects on reading, facial recognition, driving, education and employment; these functional consequences are clinical inference rather than quantified disease-specific outcomes.

## 4. Genetic and molecular information

### Gene and variant classes

GUCA1A encodes GCAP1, a neuronal calcium-sensor expressed in rods and cones, with stronger cone immunoreactivity. The disease-associated variants in the retrieved human series were overwhelmingly **germline, heterozygous missense variants**. No recurrent pathogenic copy-number alteration, aneuploidy, translocation, repeat expansion, mitochondrial mutation or somatic mechanism was established. (kitiratschky2009mutationsinthe pages 1-3, payne1998amutationin pages 3-3)

Representative HGVS alleles include:

- NM_000409:c.332A>T, p.Glu111Val—absent from public databases available to its discoverers; failed to inhibit cyclase adequately at high Ca²⁺. (marino2018anovelp.(glu111val) pages 3-3)
- c.265G>A, p.Glu89Lys; c.300T>A, p.Asp100Glu; c.476G>T, p.Gly159Val; and c.451C>T, p.Leu151Phe—all altered Ca²⁺-dependent cyclase regulation. The novel alleles were absent from 200 control chromosomes, but precise modern gnomAD frequencies were not supplied. (kitiratschky2009mutationsinthe pages 1-3)
- c.250C>T, p.Leu84Phe and c.320T>C, p.Ile107Thr—reported in autosomal-dominant retinal degeneration; functional mechanism was initially predicted rather than fully demonstrated. (allon2025clinicalgeneticimaging pages 2-4)
- p.Asn104His doubled the reported inhibitory midpoint from 260 nM for wild type to 520 nM and increased GC affinity, consistent with persistent activity at physiological Ca²⁺. This biochemical result was reported in 2021, not in a 2023–2024 human trial.

Variant classification must be performed allele by allele under current ACMG/AMP criteria. A missense change or rare population frequency alone is insufficient; segregation, phenotype match, functional data and independent observations are important. The 2025 cohort used ACMG classification and included only pathogenic/likely pathogenic alleles. (allon2025clinicalgeneticimaging pages 5-10, allon2025clinicalgeneticimaging pages 4-5)

### Modifiers, epigenetics and structural variation

No validated modifier gene, disease-specific methylation signature, histone alteration or chromatin mechanism was identified. Likewise, no recurrent large chromosomal abnormality defines this disorder.

## 5. Environmental information

This is primarily a genetic photoreceptor disorder. No causal toxin, radiation exposure, pollutant, occupation, diet, smoking pattern, alcohol exposure or infectious agent is established. There is no zoonotic or transmissible component. Evidence is insufficient to claim that sunglasses, supplements or dietary manipulation alter the molecular course, although glare control may improve comfort symptomatically.

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A heterozygous **GUCA1A missense lesion** leads to structurally altered GCAP1, commonly affecting Ca²⁺ coordination or conformational switching in EF-hand regions. (marino2018anovelp.(glu111val) pages 8-9, payne1998amutationin pages 3-3)
2. Altered GCAP1 leads to reduced Ca²⁺ sensitivity or stabilization of the Mg²⁺-bound activating conformation. (marino2018anovelp.(glu111val) pages 8-9, marino2018anovelp.(glu111val) pages 3-3)
3. This leads to failure to suppress retinal guanylate cyclase—principally GC1/RetGC1 encoded by **GUCY2D**—when intracellular Ca²⁺ is high, including dark-adapted conditions. (marino2018anovelp.(glu111val) pages 3-3, dell’orco2019normalgcapspartly pages 1-2)
4. Persistent cyclase activity leads to excessive or mistimed cGMP synthesis and impaired recovery/homeostasis of phototransduction. (kitiratschky2009mutationsinthe pages 1-3, dell’orco2019normalgcapspartly pages 1-2)
5. Excess cGMP leads to persistent opening/dysregulation of cGMP-gated channels and increased outer-segment Ca²⁺ load; the exact quantitative chain is demonstrated most strongly in biochemical and animal systems and inferred in human retina. (dell’orco2019normalgcapspartly pages 1-2)
6. **Branch A:** disturbed cGMP/Ca²⁺ homeostasis leads to early cone/rod response abnormalities and synaptic/network dysfunction. **Branch B:** chronic second-messenger toxicity leads to photoreceptor stress and death; downstream death effectors are not fully resolved for human GUCA1A disease. (jiang2013rnaimediatedgenesuppression pages 13-13, avesani2026retinalnetworkdysfunction pages 14-17, avesani2026retinalnetworkdysfunction pages 12-14)
7. Cone-predominant photoreceptor dysfunction and loss lead to color-vision impairment, photophobia, central scotoma and reduced central acuity; broader rod involvement leads to cone–rod or RP-like disease. (allon2025clinicalgeneticimaging pages 4-5, allon2025clinicalgeneticimaging pages 5-10, marino2018anovelp.(glu111val) pages 2-3)
8. Progressive outer-retinal and later RPE atrophy results in chronic, irreversible macular degeneration and severe visual disability. (allon2025clinicalgeneticimaging pages 10-13, chen2017guca1amutationcauses pages 7-8)

### Normal pathway and protein dysfunction

In light, phototransduction lowers cytoplasmic cGMP, closes cyclic-nucleotide-gated channels, hyperpolarizes the photoreceptor and lowers intracellular Ca²⁺. Low-Ca²⁺/Mg²⁺-bound GCAP1 activates RetGC to replenish cGMP; at high dark-state Ca²⁺, Ca²⁺-bound GCAP1 suppresses cyclase. Disease variants uncouple this feedback. (kitiratschky2009mutationsinthe pages 1-3, payne1998amutationin pages 3-3)

The 2018 E111V study found no major secondary/tertiary structural rearrangement but did find stabilization/rigidification of the activating state and residual cyclase activation at high Ca²⁺. Its key conclusion, reflected directly in the title, was that the variant “**leads to impaired calcium sensing and perturbed second messenger homeostasis in photoreceptors**.” (marino2018anovelp.(glu111val) pages 8-9, marino2018anovelp.(glu111val) pages 3-3)

### Cells, processes and ontology suggestions

- **Cell types:** cone photoreceptor cell; rod photoreceptor cell; retinal pigment epithelial cell. Suggested CL concepts should be matched to the current Cell Ontology.
- **GO biological processes:** visual phototransduction; phototransduction recovery; detection of light stimulus; calcium-ion sensing; regulation of guanylate cyclase activity; cGMP biosynthetic process; calcium-ion homeostasis; photoreceptor-cell maintenance; photoreceptor-cell death.
- **GO cellular components:** photoreceptor outer segment; photoreceptor inner segment; plasma membrane; cytosol.

Inflammation is not established as an initiating human mechanism. Early mitochondrial, synaptic and inflammatory alterations were reported only in a 2026 E111V mouse preprint and should be treated as emerging model evidence, not settled human pathophysiology. (avesani2026retinalnetworkdysfunction pages 14-17)

### Molecular profiling and advanced technologies

No disease-specific human single-cell, spatial-transcriptomic, proteomic, metabolomic, lipidomic or epigenomic signature was identified. Biophysical assays, molecular-dynamics simulations and engineered animal studies currently provide more mechanistic resolution than human omics. (marino2018anovelp.(glu111val) pages 8-9, marino2018anovelp.(glu111val) pages 3-3)

## 7. Anatomical structures affected

- **Organ/system:** eye; retina within the visual nervous system. No consistent extraocular syndrome is established.
- **Primary site:** bilateral neural retina, especially central macula and cone-rich outer retina.
- **Cells:** cone photoreceptors first or most severely; rods variably; RPE becomes involved in advanced maculopathy and in zebrafish models.
- **Subcellular site:** GCAP1-mediated signaling at photoreceptor outer-segment membranes in association with retinal guanylate cyclase; OCT abnormalities localize initially to the ellipsoid/outer-photoreceptor zone.
- **Suggested UBERON concepts:** eye, retina, neural retina, macula, retinal pigment epithelium, photoreceptor outer segment.
- **Lateralization:** bilateral, generally highly symmetric; the 2025 interocular acuity correlation was 0.90. (allon2025clinicalgeneticimaging pages 1-2, allon2025clinicalgeneticimaging pages 10-13, chen2017guca1amutationcauses pages 7-8)

## 8. Temporal development

Onset is chronic and usually insidious, ranging from childhood to late adulthood. In the largest cohort, mean onset was 23 years and the range was 5–74. Severe E111V disease may present congenitally with nystagmus, photophobia and marked acuity loss. (allon2025clinicalgeneticimaging pages 4-5, marino2018anovelp.(glu111val) pages 2-3)

A practical staging framework is:

1. **Early functional disease:** color discrimination difficulty and photophobia; FAF may be abnormal before color fundus examination.
2. **Early structural maculopathy:** ellipsoid-zone irregularity or optical gap.
3. **Established cone dystrophy:** reduced photopic ERG, central/paracentral scotoma and progressive acuity loss.
4. **Advanced macular/cone–rod disease:** outer-retinal and outer-nuclear-layer atrophy, RPE atrophy and possible peripheral degeneration.
5. **End-stage visual impairment:** extensive photoreceptor loss and, in rare severe cases, light perception or no light perception. (allon2025clinicalgeneticimaging pages 10-13, allon2025clinicalgeneticimaging pages 5-10)

Visual acuity declined by approximately **0.20 logMAR per decade** in the 2025 cohort, but progression is highly variable and some individuals retain relatively good vision beyond age 70. There is no established remission pattern; the disease is chronic and generally progressive. (allon2025clinicalgeneticimaging pages 4-5, allon2025clinicalgeneticimaging pages 10-10)

## 9. Inheritance and population

Inheritance is predominantly **autosomal dominant**. Thirteen of 14 families in the largest cohort had multiple-generation involvement. Each child of a heterozygous affected individual ordinarily has a 50% transmission probability, although clinical severity cannot be predicted reliably. (allon2025clinicalgeneticimaging pages 4-5)

Penetrance is not accurately quantified. Two apparently sporadic cases could not distinguish de novo variation from reduced penetrance. Expressivity is clearly variable, including within families. No genetic anticipation, recurrent germline mosaicism, consanguinity effect or established founder allele was identified. Because affected heterozygotes are not asymptomatic “carriers” in the recessive sense, carrier-frequency language is generally inappropriate; population pathogenic-allele frequency remains unknown. (allon2025clinicalgeneticimaging pages 10-10, chen2017guca1amutationcauses pages 7-8)

Disease-specific population prevalence and incidence are unavailable. GUCA1A accounted for approximately **0.1%–0.7% of IRD cohorts**, 3% of one autosomal-dominant non-RP subgroup, and 1.2% of a German macular/cone-dystrophy cohort (1.6% among molecularly solved cases). These are referral-cohort proportions, not population prevalence. (allon2025clinicalgeneticimaging pages 2-4)

No reproducible ethnic, geographic or sex ratio has been established. The recent male-severity signal should not be interpreted as male-limited inheritance. (allon2025clinicalgeneticimaging pages 4-5)

## 10. Diagnostics

### Clinical workflow

1. Record onset, progression, family history, photophobia, color impairment, central vision and nyctalopia.
2. Measure best-corrected visual acuity and perform slit-lamp/fundus examination.
3. Test color discrimination and central/peripheral visual fields.
4. Obtain macular spectral-domain OCT, short-wavelength fundus autofluorescence and widefield color/pseudocolor imaging.
5. Use ISCEV-standard pattern ERG to assess macular function and full-field ERG, including photopic on–off responses, to distinguish cone-predominant from cone–rod disease.
6. Confirm molecularly with an inherited-retinal-disease NGS panel, WES or WGS; validate/phase and assess segregation by Sanger sequencing when appropriate; classify under current ACMG/AMP standards. (allon2025clinicalgeneticimaging pages 4-5, marino2018anovelp.(glu111val) pages 2-3, allon2025clinicalgeneticimaging pages 2-4)

FAF may detect maculopathy before conventional fundus abnormalities but is not genotype-specific. OCT typically progresses from ellipsoid-zone irregularity/optical gap to outer-retinal, outer-nuclear-layer and RPE atrophy. PERG P50 is often undetectable with severe macular involvement. Full-field ERG distinguished cone dystrophy in 11/13 tested recent patients from macular dystrophy with normal full-field responses in 2/13. (allon2025clinicalgeneticimaging pages 10-13, allon2025clinicalgeneticimaging pages 5-10)

CMA, karyotyping, FISH, mtDNA analysis and repeat-expansion testing are not first-line for a classic dominant GUCA1A phenotype. They may be used only when the broader presentation suggests another diagnosis. RNA-seq and other omics are research tools, not validated diagnostics.

### Differential diagnosis

The differential includes other inherited cone/cone–rod or macular dystrophies—especially **GUCY2D, PRPH2, ABCA4, CRX, RPGR, PROM1, CDHR1, CNGA3/CNGB3**—and acquired toxic, autoimmune or age-related maculopathy. Distinguishing clues are dominant transmission, cone-predominant ERG dysfunction, symmetric outer-retinal maculopathy and a pathogenic GUCA1A allele. Imaging alone is insufficient because FAF/OCT appearances overlap across genotypes. (allon2025clinicalgeneticimaging pages 10-13, georgiou2020retinalimagingin pages 13-15)

### Screening

Population or newborn screening is not established. **Cascade genetic testing** is appropriate for adult relatives after the familial pathogenic variant is known. Predictive testing of minors requires genetics/ophthalmology counseling and consideration of whether results alter childhood surveillance or management.

## 11. Outcome and prognosis

GUCA1A retinopathy is not known to reduce life expectancy or cause disease-specific mortality. Morbidity is visual. In the 2025 cohort, mean right-eye acuity changed from 0.67 to 0.94 logMAR and left-eye acuity from 0.63 to 0.95 over a mean follow-up of approximately 10 years; the observed range extended from 0.00 logMAR to no light perception. (allon2025clinicalgeneticimaging pages 1-2, allon2025clinicalgeneticimaging pages 4-5)

Prognostic indicators include age, baseline macular structure/function and probably genotype. p.Leu84Phe was associated with earlier loss, p.Glu111Ala with worse vision, and p.Ile107Thr with later/milder disease, but each rare subgroup was very small. Extensive central atrophy and complete photoreceptor-layer loss correlate with worse acuity. (allon2025clinicalgeneticimaging pages 10-13, allon2025clinicalgeneticimaging pages 10-10)

Recovery of lost photoreceptors is not expected with current supportive care. A rare Coats-like reaction with exudative retinal detachment was reported, but this is not a typical complication. No validated circulating or molecular prognostic biomarker exists beyond genotype and retinal structural/functional measures. (allon2025clinicalgeneticimaging pages 4-5)

## 12. Treatment

### Current clinical care

No GUCA1A-specific pharmacotherapy, gene therapy, RNA therapy, cell therapy or approved surgical treatment was identified. Present management is supportive:

- individualized refractive correction;
- tinted lenses/glare control for photophobia;
- low-vision assessment and optical/electronic aids;
- orientation, mobility, educational and occupational accommodations;
- monitoring by an inherited-retinal-disease service using acuity, OCT/FAF and functional testing;
- treatment of unrelated or secondary ocular complications according to standard practice;
- genetic counseling and access to IRD registries/natural-history research.

Suggested NCIT intervention concepts are **Low Vision Rehabilitation**, **Assistive Device**, **Genetic Counseling**, **Gene Silencing Therapy**, and **Adeno-Associated Virus Vector Therapy**; the latter two are experimental for this disease.

### Preclinical advanced therapeutics

A non-allele-specific silencing strategy is mechanistically attractive because many variants are dominant gain-of-function alleles. In L151F mice, scAAV2/8-delivered shRNA suppressed mutant GCAP1 by about 70% and endogenous GCAP1 by about 90%. In a Y99C model, approximately 80% transgene silencing persisted for nearly one year and improved photoreceptor survival, delayed degeneration and improved visual function. Risks include suppression of normal GCAP1, RNAi saturation and off-target effects. (jiang2013rnaimediatedgenesuppression pages 13-13, jiang2013rnaimediatedgenesuppression pages 1-2)

The investigators characterized these results as a “**proof of concept**” for RNAi-based treatment of dominant GCAP1 disease. No human response rate or safety estimate exists. Gene supplementation alone is unlikely to neutralize a dominant toxic allele; silencing-and-replacement, allele-specific RNAi, antisense approaches or editing may ultimately be more appropriate. (jiang2012rnainterferencegene pages 158-159)

No relevant GUCA1A human interventional trial/NCT identifier was found. A search hit for “GCAP” referred to an unrelated bladder-cancer chemotherapy acronym and must not be included as a retinal trial.

## 13. Prevention

Primary lifestyle prevention is unavailable because the initiating cause is inherited. Secondary prevention consists of molecular diagnosis, surveillance and identifying relatives early enough for counseling, visual support and future trial eligibility. Tertiary prevention aims to limit disability through glare control, low-vision rehabilitation, workplace/school accommodation and treatment of secondary ocular complications.

Genetic counseling should explain autosomal-dominant transmission, variable expressivity and uncertain severity. Once a familial pathogenic variant is established, reproductive options may include prenatal diagnosis or preimplantation genetic testing, subject to local regulation and nondirective counseling. Vaccination, antimicrobial prophylaxis and public-health environmental measures are not applicable.

## 14. Other species and natural disease

No naturally occurring GUCA1A-equivalent veterinary disease was identified in companion animals, livestock or wildlife. There is no zoonotic potential or cross-species transmission. Orthologous **Guca1a** genes in mouse and zebrafish support strongly conserved calcium-dependent phototransduction, but the reported diseases are engineered experimental models rather than natural animal cases. Exact NCBI Gene and Taxon identifiers should be resolved directly from current NCBI records before ingestion.

## 15. Model organisms

### Mouse models (*Mus musculus*)

- **Y99C transgenic:** rapid, expression-dose-dependent photoreceptor degeneration and a useful allele-specific RNAi model. (dell’orco2019normalgcapspartly pages 1-2, jiang2012rnainterferencegene pages 158-159)
- **L151F genomic transgenic:** late-onset, slowly progressive cone–rod degeneration resembling human GCAP1-CORD; photopic b-wave was approximately 60% of normal at 12 months. (jiang2013rnaimediatedgenesuppression pages 13-13, jiang2013rnaimediatedgenesuppression pages 1-2)
- **E155G knock-in:** normal early development followed by progressive cone-predominant dysfunction and photoreceptor loss; 12-month photopic b-wave was approximately 42% of normal. cGMP accumulation preceded structural degeneration, supporting its upstream pathogenic role. (jiang2013rnaimediatedgenesuppression pages 13-13)
- **E111V knock-in:** a 2026 non-peer-reviewed preprint reports functional/network abnormalities before major structural loss, with outer-nuclear-layer thinning only later. Acute ex-vivo wild-type GCAP1 partially corrected rod-response kinetics; this is proof of biochemical modifiability, not therapeutic efficacy. (avesani2026retinalnetworkdysfunction pages 14-17, avesani2026retinalnetworkdysfunction pages 12-14)

Mouse limitations include a rod-dominant retina, transgene dosage effects, retention of endogenous normal alleles in some lines and species-specific GCAP2 compensation. These differences can exaggerate or attenuate the human cone-predominant phenotype. (jiang2013rnaimediatedgenesuppression pages 13-13, dell’orco2019normalgcapspartly pages 1-2)

### Zebrafish (*Danio rerio*)

Overexpression of human p.Arg120Leu reduced rod/cone markers, disrupted photoreceptors and RPE, and affected retinal/choriocapillaris-associated vasculature. Wild-type GUCA1A did not fully rescue the phenotype, supporting altered/gain-of-function behavior. p.Asp100Glu also injured photoreceptors and RPE, with a proposed dominant-negative mechanism. These are overexpression models and may not reproduce physiological heterozygous dosage. The corresponding human study was published in *Genetics in Medicine* in August 2017, DOI [10.1038/gim.2016.217](https://doi.org/10.1038/gim.2016.217), PMID **28125083**. (chen2017guca1amutationcauses pages 7-8, georgiou2020retinalimagingin pages 13-15)

No disease-specific human iPSC, retinal-organoid, Drosophila, *C. elegans*, yeast or naturally affected animal model was established in the retrieved evidence.

## Recent developments and evidence gaps

The most important recent advance is the 2025 largest-cohort study, which quantified onset, longitudinal acuity decline, symptom frequencies, bilateral symmetry, OCT sequence and preliminary genotype–phenotype associations. It was published February 19, 2025, DOI [10.1167/iovs.66.2.50](https://doi.org/10.1167/iovs.66.2.50). The strongest 2023 contribution retrieved was a review emphasizing that dominant retinal diseases often require silencing, editing or combined suppression/replacement rather than simple gene augmentation; no GUCA1A human program had entered clinical testing. (allon2025clinicalgeneticimaging pages 1-2, allon2025clinicalgeneticimaging pages 4-5)

Major unresolved fields are population prevalence/incidence, penetrance, founder effects, validated modifiers, gene–environment interaction, standardized quality-of-life outcomes, human retinal omics, biomarkers, prospective natural history and human therapeutic trials. The 2025 cohort’s modest size—19 patients and only one family for four of five alleles—means variant-specific prognostic estimates remain preliminary. (allon2025clinicalgeneticimaging pages 1-2, allon2025clinicalgeneticimaging pages 10-10)

## Key primary references

1. Payne A, et al. *Human Molecular Genetics*. February 1998. “A mutation in guanylate cyclase activator 1A….” DOI: [10.1093/hmg/7.2.273](https://doi.org/10.1093/hmg/7.2.273). Foundational human Y99C pedigree. (payne1998amutationin pages 3-3)
2. Michaelides M, et al. *Ophthalmology*. August 2005;112:1442–1447. PMID **15953638**. Human phenotype spectrum. (georgiou2020retinalimagingin pages 13-15)
3. Kitiratschky VBD, et al. *Human Mutation*. August 2009;30:E782–E796. DOI: [10.1002/humu.21055](https://doi.org/10.1002/humu.21055). Human variants plus biochemical functional testing. (kitiratschky2009mutationsinthe pages 1-3)
4. Jiang L, et al. *PLoS ONE*. March 5, 2013;8:e57676. DOI: [10.1371/journal.pone.0057676](https://doi.org/10.1371/journal.pone.0057676). L151F model and AAV-RNAi. (jiang2013rnaimediatedgenesuppression pages 13-13, jiang2013rnaimediatedgenesuppression pages 1-2)
5. Chen X, et al. *Genetics in Medicine*. August 2017;19:945–954. DOI: [10.1038/gim.2016.217](https://doi.org/10.1038/gim.2016.217); PMID **28125083**. Human R120L family and zebrafish modeling. (chen2017guca1amutationcauses pages 7-8, georgiou2020retinalimagingin pages 13-15)
6. Marino V, et al. *Human Molecular Genetics*. December 2018;27. DOI: [10.1093/hmg/ddy311](https://doi.org/10.1093/hmg/ddy311). Human E111V disease and biochemical mechanism. (marino2018anovelp.(glu111val) pages 2-3, marino2018anovelp.(glu111val) pages 8-9, marino2018anovelp.(glu111val) pages 3-3)
7. Dell’Orco D, Dal Cortivo G. *Scientific Reports*. December 2019;9:20105. DOI: [10.1038/s41598-019-56606-5](https://doi.org/10.1038/s41598-019-56606-5). Wild-type GCAP compensation and species differences. (dell’orco2019normalgcapspartly pages 1-2)
8. Allon G, et al. *Investigative Ophthalmology & Visual Science*. February 19, 2025;66(2):50. DOI: [10.1167/iovs.66.2.50](https://doi.org/10.1167/iovs.66.2.50). Largest GUCA1A clinical cohort and natural-history analysis. (allon2025clinicalgeneticimaging pages 1-2, allon2025clinicalgeneticimaging pages 4-5)

References

1. (OpenTargets Search: GUCA1A-related retinopathy-GUCA1A): Open Targets Query (GUCA1A-related retinopathy-GUCA1A, 3 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (allon2025clinicalgeneticimaging pages 1-2): Gilad Allon, Siying Lin, Anthony G. Robson, Gavin Arno, Magella M. Neveu, Pirro G. Hysi, Michel Michaelides, Andrew R. Webster, and Omar A. Mahroo. Clinical, genetic, imaging and electrophysiological findings in a cohort of patients with <i>guca1a</i>-associated retinopathy. Feb 2025. URL: https://doi.org/10.1167/iovs.66.2.50, doi:10.1167/iovs.66.2.50. This article has 3 citations and is from a domain leading peer-reviewed journal.

3. (allon2025clinicalgeneticimaging pages 4-5): Gilad Allon, Siying Lin, Anthony G. Robson, Gavin Arno, Magella M. Neveu, Pirro G. Hysi, Michel Michaelides, Andrew R. Webster, and Omar A. Mahroo. Clinical, genetic, imaging and electrophysiological findings in a cohort of patients with <i>guca1a</i>-associated retinopathy. Feb 2025. URL: https://doi.org/10.1167/iovs.66.2.50, doi:10.1167/iovs.66.2.50. This article has 3 citations and is from a domain leading peer-reviewed journal.

4. (marino2018anovelp.(glu111val) pages 3-3): Valerio Marino, Giuditta Dal Cortivo, Elisa Oppici, Paolo Enrico Maltese, Fabiana D’Esposito, Elena Manara, Lucia Ziccardi, Benedetto Falsini, Adriano Magli, Matteo Bertelli, and Daniele Dell’Orco. A novel p.(glu111val) missense mutation in guca1a associated with cone-rod dystrophy leads to impaired calcium sensing and perturbed second messenger homeostasis in photoreceptors. Sep 2018. URL: https://doi.org/10.1093/hmg/ddy311, doi:10.1093/hmg/ddy311. This article has 41 citations and is from a domain leading peer-reviewed journal.

5. (kitiratschky2009mutationsinthe pages 1-3): Veronique B.D. Kitiratschky, Petra Behnen, Ulrich Kellner, John R Heckenlively, Eberhart Zrenner, Herbert JÃ¤gle, Susanne Kohl, Bernd Wissinger, and Karl-Wilhelm Koch. Mutations in the guca1a gene involved in hereditary cone dystrophies impair calcium‐mediated regulation of guanylate cyclase. Human Mutation, 30:E782-E796, Aug 2009. URL: https://doi.org/10.1002/humu.21055, doi:10.1002/humu.21055. This article has 89 citations and is from a domain leading peer-reviewed journal.

6. (dell’orco2019normalgcapspartly pages 1-2): Daniele Dell’Orco and Giuditta Dal Cortivo. Normal gcaps partly compensate for altered cgmp signaling in retinal dystrophies associated with mutations in guca1a. Scientific Reports, Dec 2019. URL: https://doi.org/10.1038/s41598-019-56606-5, doi:10.1038/s41598-019-56606-5. This article has 24 citations and is from a peer-reviewed journal.

7. (jiang2013rnaimediatedgenesuppression pages 13-13): Li Jiang, Tansy Z. Li, Shannon E. Boye, William W. Hauswirth, Jeanne M. Frederick, and Wolfgang Baehr. Rnai-mediated gene suppression in a gcap1(l151f) cone-rod dystrophy mouse model. PLoS ONE, 8(3):e57676, Mar 2013. URL: https://doi.org/10.1371/journal.pone.0057676, doi:10.1371/journal.pone.0057676. This article has 19 citations and is from a peer-reviewed journal.

8. (marino2018anovelp.(glu111val) pages 1-1): Valerio Marino, Giuditta Dal Cortivo, Elisa Oppici, Paolo Enrico Maltese, Fabiana D’Esposito, Elena Manara, Lucia Ziccardi, Benedetto Falsini, Adriano Magli, Matteo Bertelli, and Daniele Dell’Orco. A novel p.(glu111val) missense mutation in guca1a associated with cone-rod dystrophy leads to impaired calcium sensing and perturbed second messenger homeostasis in photoreceptors. Sep 2018. URL: https://doi.org/10.1093/hmg/ddy311, doi:10.1093/hmg/ddy311. This article has 41 citations and is from a domain leading peer-reviewed journal.

9. (marino2018anovelp.(glu111val) pages 8-9): Valerio Marino, Giuditta Dal Cortivo, Elisa Oppici, Paolo Enrico Maltese, Fabiana D’Esposito, Elena Manara, Lucia Ziccardi, Benedetto Falsini, Adriano Magli, Matteo Bertelli, and Daniele Dell’Orco. A novel p.(glu111val) missense mutation in guca1a associated with cone-rod dystrophy leads to impaired calcium sensing and perturbed second messenger homeostasis in photoreceptors. Sep 2018. URL: https://doi.org/10.1093/hmg/ddy311, doi:10.1093/hmg/ddy311. This article has 41 citations and is from a domain leading peer-reviewed journal.

10. (allon2025clinicalgeneticimaging pages 5-10): Gilad Allon, Siying Lin, Anthony G. Robson, Gavin Arno, Magella M. Neveu, Pirro G. Hysi, Michel Michaelides, Andrew R. Webster, and Omar A. Mahroo. Clinical, genetic, imaging and electrophysiological findings in a cohort of patients with <i>guca1a</i>-associated retinopathy. Feb 2025. URL: https://doi.org/10.1167/iovs.66.2.50, doi:10.1167/iovs.66.2.50. This article has 3 citations and is from a domain leading peer-reviewed journal.

11. (marino2018anovelp.(glu111val) pages 2-3): Valerio Marino, Giuditta Dal Cortivo, Elisa Oppici, Paolo Enrico Maltese, Fabiana D’Esposito, Elena Manara, Lucia Ziccardi, Benedetto Falsini, Adriano Magli, Matteo Bertelli, and Daniele Dell’Orco. A novel p.(glu111val) missense mutation in guca1a associated with cone-rod dystrophy leads to impaired calcium sensing and perturbed second messenger homeostasis in photoreceptors. Sep 2018. URL: https://doi.org/10.1093/hmg/ddy311, doi:10.1093/hmg/ddy311. This article has 41 citations and is from a domain leading peer-reviewed journal.

12. (payne1998amutationin pages 3-3): A. Payne, S. Downes, D. Bessant, R. Taylor, G. Holder, M. Warren, A. C. Bird, and S. Bhattacharya. A mutation in guanylate cyclase activator 1a (guca1a) in an autosomal dominant cone dystrophy pedigree mapping to a new locus on chromosome 6p21.1. Human Molecular Genetics, 7(2):273-277, Feb 1998. URL: https://doi.org/10.1093/hmg/7.2.273, doi:10.1093/hmg/7.2.273. This article has 273 citations and is from a domain leading peer-reviewed journal.

13. (allon2025clinicalgeneticimaging pages 10-13): Gilad Allon, Siying Lin, Anthony G. Robson, Gavin Arno, Magella M. Neveu, Pirro G. Hysi, Michel Michaelides, Andrew R. Webster, and Omar A. Mahroo. Clinical, genetic, imaging and electrophysiological findings in a cohort of patients with <i>guca1a</i>-associated retinopathy. Feb 2025. URL: https://doi.org/10.1167/iovs.66.2.50, doi:10.1167/iovs.66.2.50. This article has 3 citations and is from a domain leading peer-reviewed journal.

14. (allon2025clinicalgeneticimaging pages 13-13): Gilad Allon, Siying Lin, Anthony G. Robson, Gavin Arno, Magella M. Neveu, Pirro G. Hysi, Michel Michaelides, Andrew R. Webster, and Omar A. Mahroo. Clinical, genetic, imaging and electrophysiological findings in a cohort of patients with <i>guca1a</i>-associated retinopathy. Feb 2025. URL: https://doi.org/10.1167/iovs.66.2.50, doi:10.1167/iovs.66.2.50. This article has 3 citations and is from a domain leading peer-reviewed journal.

15. (chen2017guca1amutationcauses pages 7-8): Xue Chen, X. Sheng, Wenjuan Zhuang, Xiantao Sun, Guohua Liu, Xun Shi, Guofu Huang, Yan-fang Mei, Yingjie Li, Xinyuan Pan, Ya-ni Liu, Zi-li Li, Qingshun Zhao, B. Yan, and Chen Zhao. Guca1a mutation causes maculopathy in a five-generation family with a wide spectrum of severity. Genetics in Medicine, 19:945-954, Aug 2017. URL: https://doi.org/10.1038/gim.2016.217, doi:10.1038/gim.2016.217. This article has 26 citations and is from a highest quality peer-reviewed journal.

16. (allon2025clinicalgeneticimaging pages 2-4): Gilad Allon, Siying Lin, Anthony G. Robson, Gavin Arno, Magella M. Neveu, Pirro G. Hysi, Michel Michaelides, Andrew R. Webster, and Omar A. Mahroo. Clinical, genetic, imaging and electrophysiological findings in a cohort of patients with <i>guca1a</i>-associated retinopathy. Feb 2025. URL: https://doi.org/10.1167/iovs.66.2.50, doi:10.1167/iovs.66.2.50. This article has 3 citations and is from a domain leading peer-reviewed journal.

17. (allon2025clinicalgeneticimaging pages 10-10): Gilad Allon, Siying Lin, Anthony G. Robson, Gavin Arno, Magella M. Neveu, Pirro G. Hysi, Michel Michaelides, Andrew R. Webster, and Omar A. Mahroo. Clinical, genetic, imaging and electrophysiological findings in a cohort of patients with <i>guca1a</i>-associated retinopathy. Feb 2025. URL: https://doi.org/10.1167/iovs.66.2.50, doi:10.1167/iovs.66.2.50. This article has 3 citations and is from a domain leading peer-reviewed journal.

18. (jiang2013rnaimediatedgenesuppression pages 1-2): Li Jiang, Tansy Z. Li, Shannon E. Boye, William W. Hauswirth, Jeanne M. Frederick, and Wolfgang Baehr. Rnai-mediated gene suppression in a gcap1(l151f) cone-rod dystrophy mouse model. PLoS ONE, 8(3):e57676, Mar 2013. URL: https://doi.org/10.1371/journal.pone.0057676, doi:10.1371/journal.pone.0057676. This article has 19 citations and is from a peer-reviewed journal.

19. (jiang2012rnainterferencegene pages 158-159): Li Jiang. Rna interference gene therapy for dominant photoreceptor degeneration disease in mouse models expressing mutant guanylate cyclase-activating protein 1. Text, Jan 2012. URL: https://doi.org/10.26053/0h-j46h-jcg0, doi:10.26053/0h-j46h-jcg0. This article has 0 citations and is from a peer-reviewed journal.

20. (avesani2026retinalnetworkdysfunction pages 12-14): Anna Avesani, Giuditta Dal Cortivo, Sabrina Asteriti, Giorgia Targa, Laura Veschetti, Valerio Marino, Amedeo Biasi, Carmen Longo, Barbara Cisterna, Karolina Saran, Giovanni Malerba, Andrzej T. Foik, Marco Cambiaghi, Lorenzo Cangiano, and Daniele Dell’Orco. Retinal network dysfunction precedes structural degeneration in severe guca1a cone-rod dystrophy. bioRxiv, Jul 2026. URL: https://doi.org/10.64898/2026.06.23.734025, doi:10.64898/2026.06.23.734025. This article has 1 citations.

21. (georgiou2020retinalimagingin pages 13-15): Michalis Georgiou, Kaoru Fujinami, and Michel Michaelides. Retinal imaging in inherited retinal diseases. Sep 2020. URL: https://doi.org/10.21037/aes-20-81, doi:10.21037/aes-20-81. This article has 53 citations.

22. (avesani2026retinalnetworkdysfunction pages 14-17): Anna Avesani, Giuditta Dal Cortivo, Sabrina Asteriti, Giorgia Targa, Laura Veschetti, Valerio Marino, Amedeo Biasi, Carmen Longo, Barbara Cisterna, Karolina Saran, Giovanni Malerba, Andrzej T. Foik, Marco Cambiaghi, Lorenzo Cangiano, and Daniele Dell’Orco. Retinal network dysfunction precedes structural degeneration in severe guca1a cone-rod dystrophy. bioRxiv, Jul 2026. URL: https://doi.org/10.64898/2026.06.23.734025, doi:10.64898/2026.06.23.734025. This article has 1 citations.

## Artifacts

- [Edison artifact artifact-00](GUCA1A-Related_Retinopathy-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 10 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 10 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 1 |
| Resolved | 1 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0700376` (4 mentions) - the report calls it "if available", "GUCA1A-related retinopathy"; MONDO calls it **GUCA1A-related retinopathy**

### Terms named inconsistently

The report gives these identifiers more than one name of its own:

- `MONDO:0700376` - called "if available", "GUCA1A-related retinopathy"