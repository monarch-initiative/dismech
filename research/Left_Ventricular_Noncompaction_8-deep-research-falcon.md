---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-06T14:29:00.546455'
end_time: '2026-09-06T14:40:25.374206'
duration_seconds: 684.83
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Left Ventricular Noncompaction 8
  mondo_id: MONDO:0014152
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 36
reference_validation:
  total_references: 13
  verified: 13
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 13
  on_topic: 10
  validator_version: 0.2.1
term_validation:
  total_terms: 23
  verified: 23
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 3
  labels_matching: 2
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0014152
    reported_labels:
    - if available
    ontology_label: left ventricular noncompaction 8
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Left_Ventricular_Noncompaction_8-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Left Ventricular Noncompaction 8
- **MONDO ID:** MONDO:0014152 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Left Ventricular Noncompaction 8** covering all of the
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
- **Disease Name:** Left Ventricular Noncompaction 8
- **MONDO ID:** MONDO:0014152 (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Left Ventricular Noncompaction 8** covering all of the
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


# Left Ventricular Noncompaction 8 (LVNC8): Comprehensive Disease Report

## Executive summary and evidence boundaries

Left ventricular noncompaction 8 (LVNC8; **MONDO:0014152**) is the **PRDM16-associated genetic subtype** of left ventricular noncompaction. It is principally caused by heterozygous germline loss-of-function variants or deletions involving **PRDM16**, with haploinsufficiency as the best-supported mechanism. The cardiac phenotype ranges from isolated excessive left-ventricular trabeculation to noncompaction cardiomyopathy with dilation, systolic failure, fibrosis, arrhythmia, or conduction disease. Penetrance is incomplete and expression is highly variable.

A critical distinction is necessary: most epidemiologic, diagnostic, prognostic, and treatment evidence concerns **LVNC of all genetic causes**, not LVNC8 specifically. Imaging-defined hypertrabeculation alone is neither specific for PRDM16 disease nor necessarily pathological. A defensible LVNC8 diagnosis therefore requires a compatible phenotype plus a pathogenic/likely pathogenic PRDM16 variant or PRDM16-containing deletion.

| Domain | PRDM16/LVNC8-specific finding | Evidence type | Knowledge-base annotation |
|---|---|---|---|
| Identity | **LVNC8** is the PRDM16-associated form of left ventricular noncompaction; heterozygous loss-of-function and deletion evidence supports **PRDM16 haploinsufficiency**, although LVNC can also overlap dilated cardiomyopathy (DCM). (arndt2013finemappingof pages 4-5, mazzarotto2020thegeneticarchitecture pages 1-3, boudina2023prdm16deletionis pages 1-3) | Human genetic association; segregation; translational models | MONDO:0014152; gene: **PRDM16**; genetic disease; distinguish subtype-specific disease from broad LVNC morphology |
| Representative variants | Reported LVNC-associated variants include **c.1573dupC (p.Arg525Profs*79)**, **c.2104A>T (p.Lys702Ter)**, and **p.Gln187Ter/Q187X**; these are germline protein-truncating variants expected to cause loss of function. (sun2023nonsensevariantprdm16q187x pages 1-3, arndt2013finemappingof pages 4-5) | Human cases; patient-derived iPSC cardiomyocytes; knock-in mouse | Variant classes: frameshift, nonsense; consequence: loss of function/haploinsufficiency; verify transcript and ClinVar classification before variant-level ingestion |
| Chromosomal lesion | Heterozygous **1p36 deletions encompassing PRDM16** increase cardiomyopathy risk, but neighboring deleted genes may modify the syndromic phenotype. In a combined cohort, cardiomyopathy occurred in 29.1% with versus 10.8% without PRDM16 deletion. (boudina2023prdm16deletionis pages 1-3) | Human retrospective cohort plus systematic review, n=134 | Structural variant/CNV; 1p36 deletion syndrome; record PRDM16-containing deletions separately from isolated sequence variants |
| Inheritance | Sequence-variant LVNC8 is principally described as **autosomal dominant with incomplete, age-dependent penetrance and variable expressivity**; phenotypes include LVNC, DCM, or overlapping LVNC/DCM. (sun2023nonsensevariantprdm16q187x pages 10-11, arndt2013finemappingof pages 4-5, mazzarotto2020thegeneticarchitecture pages 1-3) | Human pedigrees and case series | AD inheritance; germline; variable expressivity; no established anticipation or founder effect |
| Key phenotypes | Excessive LV trabeculation/deep intertrabecular recesses, thin compact myocardium, LV systolic dysfunction or dilation, heart failure, fibrosis, arrhythmia, and conduction abnormalities; onset ranges from fetal/infantile to adult and severity is variable. (sun2023nonsensevariantprdm16q187x pages 1-3, arndt2013finemappingof pages 4-5, nam2020cardiacspecificinactivationof pages 1-5) | PRDM16-specific human cases and models | Suggested HPO: **HP:0030682** left ventricular noncompaction; HP:0001635 congestive heart failure; HP:0001644 dilated cardiomyopathy; HP:0011675 arrhythmia; HP:0031546 myocardial fibrosis |
| Upstream mechanism | PRDM16 loss disrupts its transcriptional/chromatin-regulatory function, reducing specification and proliferation of compact-myocardial cardiomyocytes and permitting trabecular, atrial, neuronal-like, or conduction-cell transcriptional programs. (wu2022prdm16isa pages 11-13, wauwe2024prdm16determinesspecification pages 1-2) | Conditional mouse genetics; scRNA-seq; spatial transcriptomics; single-cell RNA+ATAC sequencing | GO suggestions: regulation of transcription, chromatin organization, cardiac muscle-cell differentiation, ventricular cardiac muscle development; CL: ventricular cardiomyocyte, cardiac conduction cell |
| TGF-β and tissue injury | PRDM16 binds TGFB2/TGFB3 regulatory regions and alters H3K4 methylation. Loss produces developmentally dependent TGF-β dysregulation, impaired proliferation, increased apoptosis, fibrosis, and hypertrophy; some causal links remain model-derived. (sun2023nonsensevariantprdm16q187x pages 1-3, sun2023nonsensevariantprdm16q187x pages 10-11, sun2023nonsensevariantprdm16q187x pages 11-13, nam2020cardiacspecificinactivationof pages 1-5) | Patient iPSC cardiomyocytes; knock-in/conditional mice; cardiomyoblast assays | GO: TGF-β receptor signaling, cardiomyocyte proliferation, apoptotic process, extracellular-matrix organization; cells: cardiomyocyte and cardiac fibroblast |
| Electrophysiology | Prdm16-null mouse hearts have prolonged QRS/QTc, fibrosis, and dysregulated **KCNE1, SCN5A, CACNA1H, CACNA2D2**, suggesting impaired Na+, K+, and Ca2+ homeostasis; TGF-β-receptor inhibition did not rescue conduction defects. (nam2020cardiacspecificinactivationof pages 1-5) | Mouse ECG, histology, qPCR, RNA-seq | GO: cardiac conduction, membrane depolarization, ion transmembrane transport; classify as mechanistic model evidence, not a proven universal human pathway |
| 2023–2024 developments | The 2023 Q187X study linked human pediatric LVNC to impaired proliferation, apoptosis, and TGF-β dysregulation. A 2023 multi-omics study identified early sex-specific energetic abnormalities. In 2024, single-cell RNA+ATAC analysis showed loss of ventricular working-cardiomyocyte identity and distal conduction-system hyperplasia. (sun2023nonsensevariantprdm16q187x pages 1-3, wauwe2024prdm16determinesspecification pages 1-2, kuhnisch2023prdm16mutationdetermines pages 1-2) | Human/iPSC and mouse translational studies; transcriptomics, proteomics, metabolomics, scRNA+ATAC | Recent evidence strengthens developmental cell-identity and metabolic mechanisms but does not yet establish a targeted therapy |
| Metabolism | Monoallelic Prdm16-mutant mice showed reduced amino-acid, glycerol, glycolytic and TCA-cycle metabolites, low glutathione, increased IMP, male-specific triacylglyceride accumulation, reduced male fatty-acid use, and reduced female glucose use. (kuhnisch2023prdm16mutationdetermines pages 1-2) | Mouse multi-omics and computational metabolic modeling | GO: cellular respiration, glycolysis, TCA cycle, fatty-acid oxidation, glutathione metabolism, response to oxidative stress; model-only evidence |
| Diagnosis | **Broad-LVNC fact:** diagnosis integrates clinical context with echocardiography and CMR rather than morphology alone. Common thresholds include echocardiographic NC/C >2 and CMR NC/C ≥2.3; hypertrabeculation may be physiological in athletes or pregnancy. (martineztittonel2025leftventricularnoncompaction pages 5-7, NCT03572569 chunk 1, aung2020prognosticsignificanceof pages 1-2) | Imaging cohorts, reviews, registry criteria | Imaging phenotype plus function, ECG, family history, and genetics; use a cardiomyopathy panel including PRDM16, with CNV analysis; consider CMA for syndromic 1p36 deletion |
| Prognosis | **Broad-LVNC fact:** outcomes are driven more by LVEF than trabeculation burden. Across 2,501 patients, cardiovascular mortality was 1.92 and ventricular arrhythmia 2.17 per 100 person-years. **PRDM16-specific:** deletion was associated with death, transplant, or VAD (p=0.04). (boudina2023prdm16deletionis pages 1-3, aung2020prognosticsignificanceof pages 1-2) | Meta-analysis of observational cohorts; PRDM16 deletion cohort | Adverse markers: reduced LVEF, advanced NYHA class, ventricular tachycardia, fibrosis/LGE; subtype-specific survival estimates remain unavailable |
| Treatment | No PRDM16- or LVNC8-specific disease-modifying therapy exists. **Broad-LVNC practice:** phenotype-directed guideline therapy for heart failure and arrhythmia; anticoagulation for standard indications or documented thrombus/embolism; ICD according to systolic-function/arrhythmic risk; LVAD or transplantation for end-stage disease. | Extrapolated cardiomyopathy/heart-failure management; no subtype-specific randomized trial | NCIT suggestions: Pharmacotherapy, Anticoagulation Therapy, Implantable Cardioverter-Defibrillator, Ventricular Assist Device, Heart Transplantation |
| Models | Available systems include PRDM16-Q187X patient-derived iPSC cardiomyocytes, Q187X knock-in mice, cardiomyocyte-specific Prdm16 knockout mice, monoallelic Prdm16csp1/wt mice, and zebrafish knockdown. They reproduce impaired proliferation, apoptosis, noncompaction/compact-layer defects, dysfunction, fibrosis, conduction changes, and metabolic abnormalities to varying degrees. (sun2023nonsensevariantprdm16q187x pages 1-3, wu2022prdm16isa pages 11-13, nam2020cardiacspecificinactivationof pages 1-5, kuhnisch2023prdm16mutationdetermines pages 1-2) | In vitro human cells; mouse and zebrafish genetic models | Taxa: Homo sapiens, Mus musculus, Danio rerio; model limitations include dosage-, Cre-, developmental-stage-, and sex-dependent phenotypes |
| Uncertainty | PRDM16 truncating variants are enriched in LVNC, but penetrance, subtype prevalence, complete phenotype frequencies, modifiers, environmental interactions, protective factors, and variant-specific prognosis are not established. Morphologic LVNC alone is neither specific for LVNC8 nor necessarily pathological. (sun2023nonsensevariantprdm16q187x pages 11-13, mazzarotto2020thegeneticarchitecture pages 1-3, aung2020prognosticsignificanceof pages 1-2) | Genetic association and expert synthesis | Do not infer LVNC8 from imaging alone; require pathogenic/likely pathogenic PRDM16 evidence and phenotype correlation; retain VUS separately |


*Table: Concise evidence map for PRDM16-associated left ventricular noncompaction, separating subtype-specific findings from broader LVNC evidence. It summarizes genetics, mechanisms, phenotypes, diagnostics, prognosis, treatment, models, and ontology-ready annotations.*

## 1. Disease information

### Definition

LVNC is a ventricular myocardial phenotype characterized by excessive trabeculae, deep intertrabecular recesses communicating with the ventricular cavity, and a relatively thin compact epicardial layer. LVNC8 denotes the subset attributable to **PRDM16 dysfunction**. Large-scale genetic analysis found that many LVNC cases overlap genetically with dilated or hypertrophic cardiomyopathy, whereas protein-truncating variants in PRDM16, MYH7, and ACTN2 showed enrichment more specific to noncompaction. Thus, LVNC8 is best treated as a molecularly defined developmental cardiomyopathy rather than an imaging label alone. (mazzarotto2020thegeneticarchitecture pages 1-3)

### Identifiers and synonyms

- **MONDO:** MONDO:0014152, Left ventricular noncompaction 8.
- **Gene:** PRDM16, PR/SET domain 16; chromosomal location **1p36.32**.
- **Suggested OMIM mapping:** the numbered phenotype is commonly represented as *Left ventricular noncompaction 8*; database release-specific OMIM numbers should be verified directly before production ingestion.
- **MeSH:** no retrieved evidence established a dedicated LVNC8 MeSH descriptor; broader indexing commonly falls under cardiomyopathies.
- **ICD-10/ICD-11:** no gene-specific LVNC8 code was identified. Coding generally uses an appropriate cardiomyopathy code, supplemented by a genetic diagnosis where supported.
- **Synonyms:** PRDM16-related cardiomyopathy; PRDM16-associated noncompaction cardiomyopathy; PRDM16-associated LVNC; noncompaction cardiomyopathy due to PRDM16 haploinsufficiency; left ventricular hypertrabeculation/noncompaction, PRDM16-related.

This report synthesizes **aggregated disease-level resources and published cohorts**, not individual EHR records. Patient-level observations are used only where reported in primary case or family studies.

## 2. Etiology

### Causal factors and genetic risk

The primary cause is a heterozygous germline loss-of-function variant in PRDM16 or a chromosome 1p36 deletion encompassing PRDM16. Foundational human variants included **c.1573dupC (p.Arg525ProfsTer79)**, **c.2104A>T (p.Lys702Ter)**, and **c.2447A>G (p.Asn816Ser)**. These variants affected conserved residues or truncated the protein and were absent from 1000 Genomes and more than 6,400 Exome Sequencing Project controls. The study found greater than fourfold enrichment of novel nonsynonymous variants over expectation, with *p*=0.006. Published July 2013; DOI: [10.1016/j.ajhg.2013.05.015](https://doi.org/10.1016/j.ajhg.2013.05.015). (arndt2013finemappingof pages 4-5)

A large analysis of **840 LVNC cases and 125,748 gnomAD controls** independently found PRDM16 truncating variants among the classes uniquely enriched in LVNC, supporting haploinsufficiency rather than a generic association with all cardiomyopathies. (mazzarotto2020thegeneticarchitecture pages 1-3)

The 2023 Q187X study reported two pediatric probands with PRDM16 loss-of-function variants; one had **PRDM16 p.Gln187Ter (Q187X)** and infant-onset heart failure. Its abstract states: “Novel loss-of-function PRDM16 variant impairs myocardial development resulting in noncompaction cardiomyopathy in humans and mice associated with altered TGF-β signaling.” Published December 2023; DOI: [10.1161/CIRCHEARTFAILURE.122.010351](https://doi.org/10.1161/circheartfailure.122.010351). (sun2023nonsensevariantprdm16q187x pages 1-3)

### Chromosome 1p36 deletion

In a four-hospital retrospective cohort of 71 people with 1p36 deletion syndrome, cardiomyopathy occurred in **34.5%** of individuals whose deletion included PRDM16 versus **7.7%** when PRDM16 was retained, although this comparison did not reach significance (*p*=0.1). In the combined clinical and systematic-review cohort (**n=134**), the corresponding rates were **29.1% versus 10.8%** (*p*=0.03). PRDM16 deletion was also associated with death, transplantation, or ventricular-assist-device support (*p*=0.04). Published August 2023; DOI: [10.1161/CIRCGEN.122.003912](https://doi.org/10.1161/CIRCGEN.122.003912). (boudina2023prdm16deletionis pages 1-3)

Because 1p36 deletions can remove multiple genes, their syndromic manifestations cannot be attributed wholly to PRDM16. Sequence-variant LVNC8 and PRDM16-containing 1p36 deletion syndrome should therefore be represented as related but distinct knowledge-base entities.

### Environmental, lifestyle, infectious, and protective factors

No toxin, infection, diet, smoking exposure, or occupational factor is known to cause molecularly defined LVNC8. Hemodynamic loading, pregnancy, and intensive exercise can produce **acquired or physiological hypertrabeculation**, creating an imaging phenocopy rather than PRDM16 disease. (mazzarotto2020thegeneticarchitecture pages 1-3, aung2020prognosticsignificanceof pages 1-2)

No validated protective PRDM16 allele, diet, medication, or lifestyle exposure has been demonstrated. A 2024 exploratory study proposed a potentially protective MYH7 SNV for broad LVNC, but this is neither replicated nor relevant enough to annotate as protective for LVNC8.

### Gene–environment interaction

A formal PRDM16-by-environment interaction has not been established. It is plausible—but unproved—that pregnancy, athletic loading, hypertension, myocarditis, alcohol, or cardiotoxic exposure could unmask dysfunction in a genetically susceptible myocardium. Such factors should be documented clinically as possible modifiers, not recorded as established LVNC8 causes.

## 3. Phenotypes

Subtype-specific frequencies are unavailable because published PRDM16 cohorts are small. The following phenotype spectrum combines PRDM16 cases with clearly labeled broad-LVNC estimates.

- **Left ventricular noncompaction/hypertrabeculation** — structural sign; congenital substrate, detectable prenatally through adulthood; severity variable. Suggested HPO: **HP:0030682, Left ventricular noncompaction**.
- **Thin or underdeveloped compact myocardium** — imaging/pathologic sign; developmental and potentially progressive in functional consequence. Suggested HPO: HP:0030682, with a local morphology annotation if no more specific HPO term is available.
- **Dilated cardiomyopathy/LV dilation** — sign; childhood or adult onset; may progress. Suggested HPO: **HP:0001644, Dilated cardiomyopathy**.
- **Reduced LV systolic function/heart failure** — sign and symptom complex; ranges from absent to severe infantile or adult failure. Suggested HPO: **HP:0001635, Congestive heart failure**; HP:0012664, reduced ejection fraction.
- **Arrhythmia and conduction disease** — palpitations, bradycardia, AV block, ventricular or supraventricular arrhythmia, and occasionally pre-excitation. Suggested HPO: **HP:0011675, Arrhythmia**; HP:0001662, bradycardia; HP:0001678, atrioventricular block; HP:0004308, ventricular arrhythmia.
- **Myocardial fibrosis** — CMR or histologic sign, generally associated with worse function. Suggested HPO: myocardial fibrosis where available; GO:0030198 extracellular matrix organization.
- **Thromboembolism/stroke** — downstream complication, especially with reduced function, atrial fibrillation, or intracardiac thrombus. Suggested HPO: HP:0002140 ischemic stroke; HP:0001907 thromboembolism.
- **Sudden cardiac arrest/death** — uncommon but clinically important complication of malignant arrhythmia or severe cardiomyopathy.

For context, a pediatric LVNC cohort of 31 children—not restricted to PRDM16—reported heart-failure symptoms in **10/31 (32%)**, arrhythmia or AV-conduction abnormalities in **15/31 (48%)**, elevated NT-proBNP in **5/31 (16%)**, thromboembolism in **2/31 (6%)**, and death in **2/31 (6%)**. Sixteen children (52%) had an identified molecular variant, including two with PRDM16 variants. These rates must not be assigned directly to LVNC8. (piekutowskaabramczuk2022geneticprofileof pages 3-5)

Quality of life has not been quantified specifically for LVNC8 using EQ-5D, SF-36, or PROMIS. Symptomatic heart failure can impair exercise tolerance, schooling/employment, and activities of daily living; arrhythmic risk and inherited-disease surveillance add psychosocial burden.

## 4. Genetic and molecular information

### Causal gene and protein

- **Gene:** PRDM16; HGNC identifier should be verified against the current HGNC release before ingestion.
- **Protein:** a nuclear zinc-finger transcriptional regulator containing a PR/SET domain, two zinc-finger DNA-binding regions, and transcriptional activation/repression domains. It also influences chromatin state and histone H3K4 methylation. (nam2020cardiacspecificinactivationof pages 1-5)
- **Disease mechanism:** predominantly **loss of function/haploinsufficiency**.
- **Origin:** germline. No evidence supports a recurrent somatic LVNC8 mechanism.

### Variant classes and interpretation

Documented classes include nonsense, frameshift, splice-disrupting, missense, and multigene copy-number deletions. Protein-truncating variants provide the strongest class-level evidence. Each variant nevertheless requires current ACMG/AMP classification, transcript normalization, segregation review, and population-frequency assessment. A VUS must not establish LVNC8.

Population frequencies are variant-specific. The foundational truncating variants were absent from the cited historical controls. One later PRDM16 variant associated with LVNC/Wolff–Parkinson–White syndrome, rs201814961/ClinVar Variation ID 487607, was reported at approximately **0.03%** in gnomAD, illustrating why rarity alone does not establish pathogenicity. (umapathi2025…geneticvariant pages 1-2, umapathi2025araregenetic pages 1-2)

### Modifiers, epigenetics, and structural variation

No validated human modifier gene is established. Variable 1p36 deletion boundaries, additional cardiomyopathy variants, sex, and genetic background are plausible modifiers. PRDM16 itself changes chromatin accessibility and H3K4 methylation at target loci, but no diagnostic DNA-methylation signature has been validated. Large PRDM16-containing **1p36 deletions** are the principal structural abnormality; no recurrent LVNC8-specific translocation, inversion, aneuploidy, or repeat expansion is known.

## 5. Environmental information

LVNC8 is not infectious or toxicologic, and it has no zoonotic transmission. Athletic remodeling, pregnancy, anemia/sickle-cell disease, and other loading states can mimic LVNC morphology and should be treated as differential-context variables. Smoking, alcohol excess, obesity, uncontrolled hypertension, and cardiotoxic drugs may worsen general myocardial health, but LVNC8-specific effect sizes are unavailable. (martineztittonel2025leftventricularnoncompaction pages 5-7, aung2020prognosticsignificanceof pages 1-2)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **A heterozygous PRDM16 loss-of-function variant or deletion leads to reduced PRDM16 dosage and transcriptional/chromatin-regulatory activity.**
2. **Reduced PRDM16 activity leads to impaired ventricular working/compact-cardiomyocyte specification and permits inappropriate trabecular, atrial, neuronal-like, or conduction-cell programs.** This is demonstrated primarily in mouse single-cell studies and inferred in humans. (wu2022prdm16isa pages 11-13, wauwe2024prdm16determinesspecification pages 1-2)
3. **Abnormal cell identity leads to reduced compact-layer cardiomyocyte proliferation and, in some models, increased apoptosis**, producing an underdeveloped compact myocardium. (sun2023nonsensevariantprdm16q187x pages 1-3, wu2022prdm16isa pages 11-13)
4. **PRDM16 loss also leads to developmentally abnormal TGF-β regulation** through TGFB2/TGFB3 promoter occupancy and altered H3K4 methylation; the direction depends on developmental stage. (sun2023nonsensevariantprdm16q187x pages 10-11, sun2023nonsensevariantprdm16q187x pages 11-13)
5. **These developmental defects lead to persistent trabeculation/noncompaction and ventricular wall abnormality.**
6. **Branch A:** altered myocardial structure and energetics lead to hypoplasia or dilation, systolic dysfunction, remodeling, fibrosis, and heart failure. (boudina2023prdm16deletionis pages 1-3, kuhnisch2023prdm16mutationdetermines pages 1-2)
7. **Branch B:** conduction-system fate expansion, ion-channel dysregulation, and fibrosis lead to slowed conduction, prolonged QRS/QTc, arrhythmia, and possible sudden death. The detailed ion mechanism is demonstrated in mice and remains inferential in human LVNC8. (nam2020cardiacspecificinactivationof pages 1-5, wauwe2024prdm16determinesspecification pages 1-2)
8. **Branch C:** ventricular dysfunction, recess-associated stasis, and atrial arrhythmia may lead to intracardiac thrombosis and systemic embolism; this is broad-LVNC inference rather than a PRDM16-specific demonstration.

### Cellular identity and advanced profiling

A 2022 cardiomyocyte-specific knockout study combined scRNA-seq with spatial transcriptomics. LV compact cardiomyocytes lost compact-layer markers and acquired trabecular or even neuronal-like signatures. PRDM16 appeared to cooperate with LV-enriched **TBX5** and **HAND1**. Importantly, noncompaction and dilation were separable: both ventricles could show noncompaction, while dilation and proliferative defects were LV-predominant. (wu2022prdm16isa pages 11-13)

A study published online **20 September 2024** used combined single-cell RNA and ATAC sequencing. PRDM16 loss opposed ventricular working-cardiomyocyte identity, permitted atrial and conduction fates, and produced distal ventricular-conduction-system hyperplasia, abnormal electrophysiology, contractile dysfunction, and premature death. DOI: [10.26508/lsa.202402719](https://doi.org/10.26508/lsa.202402719). (wauwe2024prdm16determinesspecification pages 1-2)

Suggested cell terms: **CL:0000746 cardiac muscle cell/cardiomyocyte**, ventricular working cardiomyocyte, trabecular cardiomyocyte, Purkinje/conduction-system cell, cardiac fibroblast, coronary arterial endothelial cell, and vascular smooth-muscle cell. Suggested processes: GO:0055008 cardiac muscle tissue development; GO:0007507 heart development; GO:0048738 cardiac muscle tissue development; GO:0006355 regulation of transcription; GO:0006338 chromatin remodeling; GO:0060048 cardiac muscle contraction; GO:0061337 cardiac conduction.

### TGF-β, apoptosis, fibrosis, and ion homeostasis

Patient-derived Q187X iPSC cardiomyocytes showed significantly impaired proliferation and increased apoptosis with dysregulation of cardiac-maturation and TGF-β-associated transcripts. Homozygous Q187X mice had underdeveloped compact myocardium and embryonic lethality; heterozygotes had smaller ventricles, fibrosis, and age-dependent loss of TGF-β expression. (sun2023nonsensevariantprdm16q187x pages 1-3)

Cardiac-specific Prdm16-null mice had prolonged QRS and QTc, cardiomyocyte hypertrophy, and fibrosis, with increased **Ctgf, Timp1, Acta2, Tgfb1–3**, and phosphorylated SMAD2. RNA-seq identified dysregulated **Kcne1, Scn5a, Cacna1h**, and **Cacna2d2**, implicating Na+, K+, and Ca2+ homeostasis. TGF-β-receptor inhibition did not rescue conduction, suggesting a parallel electrophysiologic pathway rather than conduction disease being merely secondary to TGF-β activation. (nam2020cardiacspecificinactivationof pages 1-5)

### Metabolic multi-omics

A 2023 transcriptomic, proteomic, metabolomic, lipidomic, and computational study of heterozygous Prdm16 mice found hypoplastic hearts and reduced systolic performance, worse in females. Mutant hearts had reduced amino-acid, glycerol, glycolytic, and tricarboxylic-acid-cycle metabolites; reduced glutathione and increased inosine monophosphate suggested oxidative stress and disturbed energetics. Male hearts accumulated triacylglycerides and showed reduced modeled fatty-acid use, whereas females showed lower glucose use. **PYROXD2** and **PBXIP1** were upregulated. The authors concluded that “metabolic dysregulation is an early event in the PRDM16 associated cardiac pathology.” Published online 16 October 2023; DOI: [10.1093/cvr/cvad154](https://doi.org/10.1093/cvr/cvad154). These are model findings, not validated human biomarkers. (kuhnisch2023prdm16mutationdetermines pages 1-2)

Immune or autoimmune mechanisms, reproducible human proteomic biomarkers, and subtype-specific circulating metabolomic signatures have not been established.

## 7. Anatomical structures affected

The principal organ is the **heart** (UBERON:0000948), particularly the **left ventricle** (UBERON:0002084) and its myocardium. The apical and mid-inferolateral segments are commonly involved in broad LVNC, although distribution is variable. Biventricular noncompaction can occur, so the label “left ventricular” does not exclude right-ventricular trabecular abnormalities. (wu2022prdm16isa pages 11-13, aung2020prognosticsignificanceof pages 1-2)

Affected tissues and cells include compact and trabecular myocardium, ventricular cardiomyocytes, conduction-system cardiomyocytes, cardiac fibroblasts, and potentially coronary vascular cells. Relevant subcellular compartments are the nucleus/chromatin, sarcomeric/contractile apparatus, plasma membrane ion-channel complexes, and mitochondria. PRDM16 is predominantly nuclear in cardiomyocytes and cardiac interstitial cells. (arndt2013finemappingof pages 4-5, nam2020cardiacspecificinactivationof pages 1-5)

Secondary organs may be affected by heart-failure hypoperfusion or thromboembolism, especially brain, kidney, liver, and lung. There is no meaningful left-right body lateralization beyond predominant involvement of the left cardiac ventricle.

## 8. Temporal development

The initiating lesion is germline and the developmental substrate is congenital, but clinical onset ranges from fetal or infantile disease to asymptomatic adulthood. Severe biallelic disruption is embryonically lethal in mouse models; heterozygous human disease can cause infant-onset heart failure or remain mild for decades. (sun2023nonsensevariantprdm16q187x pages 1-3, sun2023nonsensevariantprdm16q187x pages 10-11)

The course is chronic and lifelong but highly variable: stable morphology with preserved function, progressive ventricular dysfunction, episodic arrhythmia, or advanced heart failure may occur. Critical periods include embryonic compact-myocardium specification, infancy/childhood in severe disease, puberty and growth, pregnancy, and periods of high hemodynamic demand. True remission of the causal genotype does not occur; ventricular function may improve with heart-failure therapy, and loading-related hypertrabeculation can regress when it is a phenocopy rather than LVNC8.

## 9. Inheritance and population

### Inheritance

The usual pattern is **autosomal dominant**, with incomplete, age-dependent penetrance and variable expressivity. Reported expressions include isolated LVNC, DCM, mixed LVNC/DCM, preserved-function hypertrabeculation, and conduction disease. No evidence supports genetic anticipation. Germline mosaicism is theoretically possible but not quantified. No reproducible founder variant or consanguinity effect is established. Carrier frequency cannot be estimated because variant pathogenicity and penetrance remain uncertain.

Sex may modify severity. In PRDM16-deleted 1p36 cases, cardiomyopathy occurred in **34.5% of females versus 16.7% of males**, but the difference was not significant (*p*=0.2). Female knockout mice had more severe dysfunction, fibrosis, and mortality (*p*=0.0003), providing biological support but not a definitive human sex-risk estimate. (boudina2023prdm16deletionis pages 1-3)

### Epidemiology

No prevalence or incidence estimate exists for molecularly confirmed LVNC8. For **adult LVNC of all causes**, a 2024 systematic review/meta-analysis reported pooled prevalence of **0.5%**, with CMR detection of **1.3%**; estimates across studies ranged from 0.014% to 14.79%, illustrating major ascertainment and criteria effects. Mortality was 12% and transplantation 7%. Published online 16 September 2024; DOI: [10.14740/cr1673](https://doi.org/10.14740/cr1673). (llerenavelastegui2024prevalenceclinicalmanifestations pages 1-2)

In an earlier meta-analysis of 2,501 LVNC patients, mean age was 46 years and the male:female ratio was **1.7:1**. These figures cannot be assumed for LVNC8. (aung2020prognosticsignificanceof pages 1-2)

1p36 deletion syndrome occurs in approximately **1 in 5,000 newborns**, but only a subset of deletions includes PRDM16 and only a subset of those individuals develops cardiomyopathy. (boudina2023prdm16deletionis pages 1-3)

No validated ethnic or geographic enrichment of isolated PRDM16-LVNC8 has been established.

## 10. Diagnostics

### Clinical evaluation

Evaluation should include three-generation pedigree, symptoms, examination, 12-lead ECG, ambulatory ECG, echocardiography, and CMR when feasible. Exercise testing is useful for functional capacity and exertional arrhythmia. NT-proBNP/troponin can characterize heart failure or injury but are not diagnostic for LVNC8. Biopsy is not routinely required.

Common morphology thresholds include:

- **Chin echocardiographic criterion:** X/Y ≤0.5 in diastole.
- **Jenni criterion:** noncompacted/compacted (**NC/C**) ratio >2 in systole, with a two-layer structure and perfused recesses.
- **Stöllberger criterion:** at least three prominent trabeculae apical to papillary muscles, perfused recesses, and often NC/C >2.
- **Petersen CMR criterion:** NC/C ≥2.3 in end-diastole.
- **Jacquier CMR criterion:** trabeculated mass >20% of total LV mass. (martineztittonel2025leftventricularnoncompaction pages 5-7)

These are not interchangeable and can overdiagnose healthy athletes, pregnancy-related remodeling, and some ancestries. The contemporary expert position is to integrate morphology with ventricular size/function, fibrosis, ECG abnormalities, symptoms, family history, congenital/syndromic features, and genotype. In a pediatric cohort, median echocardiographic NC/C was 2.80 and median CMR NC/C 3.09; CMR confirmed all 25 evaluable echocardiographic cases. (piekutowskaabramczuk2022geneticprofileof pages 3-5)

### Genetic testing strategy

1. Perform a validated cardiomyopathy panel containing **PRDM16** plus established LVNC/DCM/HCM and arrhythmia genes, with deletion/duplication analysis.
2. Use exome or genome sequencing when panel testing is negative and suspicion remains high, particularly for pediatric, syndromic, or familial disease.
3. Use chromosomal microarray when developmental delay, dysmorphism, seizures, congenital anomalies, or growth abnormalities suggest **1p36 deletion syndrome**.
4. Confirm reportable variants and test parents/relatives for segregation.
5. RNA analysis may clarify suspected splice variants, but it is not yet routine.
6. Karyotype/FISH may characterize a known structural rearrangement but are less sensitive than CMA for small 1p36 deletions.
7. Mitochondrial DNA and repeat-expansion testing are not specifically indicated unless the broader phenotype suggests those disorders.

### Differential diagnosis

Rule out physiological athlete’s heart, pregnancy-associated hypertrabeculation, sickle-cell/anemia-associated remodeling, DCM/HCM with secondary trabeculation, myocarditis, ischemic or hypertensive remodeling, apical hypertrophic cardiomyopathy, endocardial fibroelastosis, endomyocardial fibrosis, cardiac tumors or thrombus, congenital heart disease, Barth syndrome/TAZ disease, mitochondrial disease, neuromuscular disorders, and HCN4/RYR2-associated arrhythmic LVNC. (martineztittonel2025leftventricularnoncompaction pages 5-7, aung2020prognosticsignificanceof pages 1-2)

### Screening

Cascade screening of first-degree relatives should combine genetic testing for the familial pathogenic variant with ECG and cardiac imaging. Genotype-positive/phenotype-negative relatives require longitudinal surveillance because penetrance may be age-dependent. There is no population or newborn LVNC8 screening program.

## 11. Outcome and prognosis

LVNC8-specific survival curves are unavailable. In the broad-LVNC meta-analysis of 28 studies and 2,501 patients followed for a median 2.9 years, event rates per 100 person-years were:

- cardiovascular mortality **1.92** (95% CI 1.54–2.30);
- all-cause mortality **2.16**;
- stroke/systemic embolism **1.54**;
- heart-failure admission **3.53**;
- transplantation **1.24**;
- ventricular arrhythmia **2.17**;
- cardiac-device implantation **2.66**. (aung2020prognosticsignificanceof pages 1-2)

Cardiovascular mortality was similar to DCM (OR 1.10, 95% CI 0.18–6.67). The strongest conclusion was that **LVEF, not trabeculation burden, drove adverse outcomes**. Reduced LVEF, NYHA III/IV symptoms, ventricular tachycardia, dilation, and CMR late gadolinium enhancement/fibrosis are therefore more useful prognostic markers than NC/C ratio alone. (llerenavelastegui2024prevalenceclinicalmanifestations pages 1-2, aung2020prognosticsignificanceof pages 1-2)

PRDM16 deletion conferred increased risk of death, transplantation, or VAD in the 2023 cohort. Severe pediatric onset, marked systolic dysfunction, malignant arrhythmia, and fibrosis should be regarded as adverse indicators, although no validated PRDM16-specific risk calculator exists. (boudina2023prdm16deletionis pages 1-3)

## 12. Treatment

No approved PRDM16-restoring, gene-editing, RNA, cell, or TGF-β-targeted therapy exists. Management is phenotype-directed and extrapolated from heart-failure and arrhythmia guidelines.

- **Heart failure:** guideline-directed therapy according to age and phenotype, generally including an ACE inhibitor/ARB or ARNI, evidence-based beta-blocker, mineralocorticoid-receptor antagonist, SGLT2 inhibitor in eligible patients, and diuretics for congestion.
- **Arrhythmia:** beta-blocker or other antiarrhythmic therapy selected by rhythm and ventricular function; catheter ablation when appropriate.
- **ICD:** standard primary- or secondary-prevention indications based on LVEF, sustained VT/VF, prior arrest, and individualized genetic/fibrotic risk—not trabeculation alone.
- **Anticoagulation:** indicated for atrial fibrillation, intracardiac thrombus, previous systemic embolism, or other conventional high-risk contexts. Routine anticoagulation solely for morphology is not supported.
- **Advanced failure:** cardiac resynchronization when standard criteria are met; LVAD or heart transplantation for refractory end-stage disease.
- **Supportive care:** individualized exercise advice, vaccination and infection prevention as for other cardiomyopathies, pregnancy counseling, psychosocial support, and cardiac rehabilitation when stable.

Suggested NCIt intervention concepts: Pharmacotherapy; Angiotensin-Converting Enzyme Inhibitor; Beta-Adrenergic Blocker; Anticoagulation Therapy; Catheter Ablation; Implantable Cardioverter-Defibrillator; Cardiac Resynchronization Therapy; Ventricular Assist Device; Heart Transplantation.

### Current research implementation

No retrieved interventional trial tested an LVNC8-specific treatment. Active work is registry-based:

- **NCT06024759**, recruiting, estimated **500 adults**, follows LVNC for 10 years to identify genetic, strain, PVC/NSVT, dysfunction, and ICD-risk predictors; start 1 September 2023, estimated completion 2033. [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT06024759). (NCT06024759 chunk 1)
- **NCT04265040 (TORCH-Plus)**, recruiting, estimated **2,040 participants**, integrates deep phenotyping, genomics, inflammation, fibrosis, biomarkers, and outcomes across cardiomyopathies including rare LVNC; estimated completion December 2027. [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT04265040). (NCT04265040 chunk 1)
- **NCT03572569 (RIKADA)** is a prospective family-based pediatric cardiomyopathy study, estimated **200 participants**, incorporating ECG/Holter, exercise testing, echo, CMR, laboratory testing, and genetics. Registry status is currently “unknown,” with last known status recruiting. [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT03572569). (NCT03572569 chunk 1)

## 13. Prevention

Primary prevention of a de novo or inherited PRDM16 variant is not available. Reproductive options after genetic counseling include prenatal diagnosis and preimplantation genetic testing when a familial pathogenic variant is known; counseling must emphasize incomplete penetrance and variable expressivity.

Secondary prevention consists of cascade genetic testing, baseline ECG/echo, periodic surveillance of genotype-positive relatives, ambulatory rhythm monitoring when indicated, and early treatment of ventricular dysfunction or arrhythmia. Tertiary prevention includes guideline-directed heart-failure therapy, embolic-risk management, ICD use under conventional criteria, avoidance of cardiotoxic exposures, and timely referral for advanced-heart-failure care.

No vaccine or infectious prophylaxis prevents LVNC8. General vaccination and prompt treatment of infections may reduce cardiovascular decompensation but are not disease-specific.

## 14. Other species and natural disease

- **Human:** *Homo sapiens*, NCBI Taxonomy **9606**; naturally occurring PRDM16 variants and deletions cause LVNC/DCM.
- **Mouse:** *Mus musculus*, Taxonomy **10090**; engineered Prdm16 loss produces noncompaction, compact-layer defects, conduction abnormalities, fibrosis, metabolic dysfunction, and sex-biased severity.
- **Zebrafish:** *Danio rerio*, Taxonomy **7955**; experimental prdm16 knockdown reduces heart rate and cardiac output and impairs cardiomyocyte proliferation. (nam2020cardiacspecificinactivationof pages 1-5)

No well-established naturally occurring veterinary LVNC8 syndrome or breed predisposition was identified. There is no transmission or zoonotic potential. The conserved cardiac expression and phenotype across vertebrates support evolutionary conservation of PRDM16-dependent myocardial development, although zebrafish cardiac anatomy and regenerative capacity limit direct clinical extrapolation.

## 15. Model organisms and experimental systems

### Available models

- **Patient-derived PRDM16-Q187X iPSC cardiomyocytes:** impaired proliferation, increased apoptosis, and TGF-β/cardiac-maturation transcriptional abnormalities. Strength: human genetic background. Limitation: immature in-vitro cardiomyocytes and absent organ-level loading. (sun2023nonsensevariantprdm16q187x pages 1-3)
- **Prdm16-Q187X knock-in mouse:** homozygotes show compact-layer underdevelopment and embryonic lethality; heterozygotes show milder underdevelopment, fibrosis, and age-dependent signaling changes. Strength: allelic fidelity; limitation: mouse dosage effects differ from humans. (sun2023nonsensevariantprdm16q187x pages 1-3, sun2023nonsensevariantprdm16q187x pages 10-11)
- **Cardiomyocyte-specific Prdm16 knockout mouse:** recapitulates LV-predominant dilation/dysfunction, noncompaction, identity switching, conduction abnormalities, hypertrophy, and fibrosis. Useful for developmental timing and cell-autonomous effects; results depend on Cre driver and deletion timing. (wu2022prdm16isa pages 11-13, nam2020cardiacspecificinactivationof pages 1-5)
- **Prdm16csp1/wt systemic heterozygous mouse:** models monoallelic human loss and early sex-specific metabolic dysfunction; useful for multi-omics and preclinical metabolism studies. (kuhnisch2023prdm16mutationdetermines pages 1-2)
- **Zebrafish morpholino/knockdown:** suitable for rapid developmental and cardiac-output assays but incompletely models mammalian ventricular compaction.
- **H9c2 cardiomyoblasts:** demonstrated PRDM16 occupancy/regulation at TGFB promoters and H3K4 effects; limited by their rat, nonadult-cardiomyocyte identity. (sun2023nonsensevariantprdm16q187x pages 11-13)

No validated human cardiac organoid, large-animal, or natural veterinary PRDM16-LVNC8 model was identified in the retrieved literature.

## Evidence gaps and knowledge-base cautions

1. Molecularly confirmed LVNC8 prevalence, incidence, penetrance, and age-specific natural history remain unknown.
2. Human phenotype frequencies cannot be inferred from broad LVNC cohorts.
3. Variant-specific risks require current ClinVar/ClinGen and population-database review; historical “mutation” labels should not automatically be converted to pathogenic.
4. Imaging hypertrabeculation alone must not be equated with cardiomyopathy or LVNC8.
5. TGF-β, metabolic, and conduction mechanisms are compelling but predominantly model-derived; none yet supports targeted clinical therapy.
6. No validated protective factor, pharmacogenomic rule, molecular biomarker, epigenetic diagnostic, or disease-modifying treatment exists.

Overall, the strongest current model is that **PRDM16 haploinsufficiency disrupts ventricular/compact-cardiomyocyte identity, proliferation, chromatin regulation, developmental TGF-β signaling, electrophysiology, and energy metabolism**, producing a variably penetrant spectrum from isolated hypertrabeculation to severe noncompaction/dilated cardiomyopathy.

References

1. (arndt2013finemappingof pages 4-5): Anne-Karin Arndt, Sebastian Schafer, Jorg-Detlef Drenckhahn, M. Khaled Sabeh, Eva R. Plovie, Almuth Caliebe, Eva Klopocki, Gabriel Musso, Andreas A. Werdich, Hermann Kalwa, Matthias Heinig, Robert F. Padera, Katharina Wassilew, Julia Bluhm, Christine Harnack, Janine Martitz, Paul J. Barton, Matthias Greutmann, Felix Berger, Norbert Hubner, Reiner Siebert, Hans-Heiner Kramer, Stuart A. Cook, Calum A. MacRae, and Sabine Klaassen. Fine mapping of the 1p36 deletion syndrome identifies mutation of prdm16 as a cause of cardiomyopathy. American journal of human genetics, 93 1:67-77, Jul 2013. URL: https://doi.org/10.1016/j.ajhg.2013.05.015, doi:10.1016/j.ajhg.2013.05.015. This article has 242 citations and is from a highest quality peer-reviewed journal.

2. (mazzarotto2020thegeneticarchitecture pages 1-3): Francesco Mazzarotto, Megan H. Hawley, Matteo Beltrami, Leander Beekman, Antonio de Marvao, Kathryn A. McGurk, Ben Statton, Beatrice Boschi, Francesca Girolami, Angharad M. Roberts, Elisabeth M. Lodder, Mona Allouba, Soha Romeih, Yasmine Aguib, A. John Baksi, Antonis Pantazis, Sanjay K. Prasad, Elisabetta Cerbai, Magdi H. Yacoub, Declan P. O’Regan, Stuart A. Cook, James S. Ware, Birgit Funke, Iacopo Olivotto, Connie R. Bezzina, Paul J.R. Barton, and Roddy Walsh. The genetic architecture of left ventricular non-compaction reveals both substantial overlap with other cardiomyopathies and a distinct aetiology in a subset of cases. European Heart Journal, Jan 2020. URL: https://doi.org/10.1101/2020.01.03.19015602, doi:10.1101/2020.01.03.19015602. This article has 4 citations and is from a highest quality peer-reviewed journal.

3. (boudina2023prdm16deletionis pages 1-3): PhD Sihem Boudina, MD Andrew Landstrom, MD Ruth McPherson, BA Ryan J. Kramer, Amir, BS Nima Fatahian, MD Alice Chan, MD Jeffery Mortenson, BA Jennifer Osher, Bo Sun, BS Lauren E. Parker, M. M. Michael B. Rosamilia, BS Kyra B. Potter, BS Kaila Moore, BS Sage L. Atkins, MS Jill A. Rosenfeld, MD Alona Birjiniuk, PhD Edward Jones, MD Taylor S. Howard, MD Jeffrey J. Kim, MD Daryl A. Scott, PhD Seema Lalani Md, Msc Omid M.T. Rouzbehani, PhD Samantha Kaplan, Marissa A. Hathaway, MD Jennifer L. Cohen, MD S. Yukiko Asaki, and MD Hugo R. Martinez. <i>prdm16</i> deletion is associated with sex-dependent cardiomyopathy and cardiac mortality: a translational, multi-institutional cohort study. Aug 2023. URL: https://doi.org/10.1161/circgen.122.003912, doi:10.1161/circgen.122.003912. This article has 17 citations.

4. (sun2023nonsensevariantprdm16q187x pages 1-3): Bo Sun, Omid M.T. Rouzbehani, Ryan J. Kramer, Rajeshwary Ghosh, Robin M. Perelli, Sage Atkins, Amir Nima Fatahian, Kathryn Davis, Marta W. Szulik, Michael A. Goodman, Marissa A. Hathaway, Ellenor Chi, Tarah A. Word, Hari Tunuguntla, Susan W. Denfield, Xander H.T. Wehrens, Kevin J. Whitehead, Hala Y. Abdelnasser, Junco S. Warren, Mingfu Wu, Sarah Franklin, Sihem Boudina, and Andrew P. Landstrom. Nonsense variant prdm16-q187x causes impaired myocardial development and tgf-β signaling resulting in noncompaction cardiomyopathy in humans and mice. Circulation: Heart Failure, 16:e010351, Dec 2023. URL: https://doi.org/10.1161/circheartfailure.122.010351, doi:10.1161/circheartfailure.122.010351. This article has 26 citations and is from a domain leading peer-reviewed journal.

5. (sun2023nonsensevariantprdm16q187x pages 10-11): Bo Sun, Omid M.T. Rouzbehani, Ryan J. Kramer, Rajeshwary Ghosh, Robin M. Perelli, Sage Atkins, Amir Nima Fatahian, Kathryn Davis, Marta W. Szulik, Michael A. Goodman, Marissa A. Hathaway, Ellenor Chi, Tarah A. Word, Hari Tunuguntla, Susan W. Denfield, Xander H.T. Wehrens, Kevin J. Whitehead, Hala Y. Abdelnasser, Junco S. Warren, Mingfu Wu, Sarah Franklin, Sihem Boudina, and Andrew P. Landstrom. Nonsense variant prdm16-q187x causes impaired myocardial development and tgf-β signaling resulting in noncompaction cardiomyopathy in humans and mice. Circulation: Heart Failure, 16:e010351, Dec 2023. URL: https://doi.org/10.1161/circheartfailure.122.010351, doi:10.1161/circheartfailure.122.010351. This article has 26 citations and is from a domain leading peer-reviewed journal.

6. (nam2020cardiacspecificinactivationof pages 1-5): Jeong Min Nam, Ji Eun Lim, Tae Woong Ha, Bermseok Oh, and Ji-One Kang. Cardiac-specific inactivation of <i>prdm16</i> effects cardiac conduction abnormalities and cardiomyopathy-associated phenotypes. Apr 2020. URL: https://doi.org/10.1152/ajpheart.00647.2019, doi:10.1152/ajpheart.00647.2019. This article has 42 citations.

7. (wu2022prdm16isa pages 11-13): Tongbin Wu, Zhengyu Liang, Zengming Zhang, Canzhao Liu, Lunfeng Zhang, Yusu Gu, Kirk L. Peterson, Sylvia M. Evans, Xiang-Dong Fu, and Ju Chen. Prdm16 is a compact myocardium-enriched transcription factor required to maintain compact myocardial cardiomyocyte identity in left ventricle. Feb 2022. URL: https://doi.org/10.1161/circulationaha.121.056666, doi:10.1161/circulationaha.121.056666. This article has 106 citations and is from a highest quality peer-reviewed journal.

8. (wauwe2024prdm16determinesspecification pages 1-2): Jore Van Wauwe, Alexia Mahy, Sander Craps, Samaneh Ekhteraei-Tousi, Pieter Vrancaert, Hannelore Kemps, Wouter Dheedene, Rosa Doñate Puertas, Sander Trenson, H. Llewelyn Roderick, Manu Beerens, and Aernout Luttun. Prdm16 determines specification of ventricular cardiomyocytes by suppressing alternative cell fates. Life Science Alliance, 7:e202402719, Sep 2024. URL: https://doi.org/10.26508/lsa.202402719, doi:10.26508/lsa.202402719. This article has 8 citations and is from a peer-reviewed journal.

9. (sun2023nonsensevariantprdm16q187x pages 11-13): Bo Sun, Omid M.T. Rouzbehani, Ryan J. Kramer, Rajeshwary Ghosh, Robin M. Perelli, Sage Atkins, Amir Nima Fatahian, Kathryn Davis, Marta W. Szulik, Michael A. Goodman, Marissa A. Hathaway, Ellenor Chi, Tarah A. Word, Hari Tunuguntla, Susan W. Denfield, Xander H.T. Wehrens, Kevin J. Whitehead, Hala Y. Abdelnasser, Junco S. Warren, Mingfu Wu, Sarah Franklin, Sihem Boudina, and Andrew P. Landstrom. Nonsense variant prdm16-q187x causes impaired myocardial development and tgf-β signaling resulting in noncompaction cardiomyopathy in humans and mice. Circulation: Heart Failure, 16:e010351, Dec 2023. URL: https://doi.org/10.1161/circheartfailure.122.010351, doi:10.1161/circheartfailure.122.010351. This article has 26 citations and is from a domain leading peer-reviewed journal.

10. (kuhnisch2023prdm16mutationdetermines pages 1-2): Jirko Kühnisch, Simon Theisen, Josephine Dartsch, Raphaela Fritsche-Guenther, Marieluise Kirchner, Benedikt Obermayer, Anna Bauer, Anne-Karin Kahlert, Michael Rothe, Dieter Beule, Arnd Heuser, Philipp Mertins, Jennifer A Kirwan, Nikolaus Berndt, Calum A MacRae, Norbert Hubner, and Sabine Klaassen. <i>prdm16</i> mutation determines sex-specific cardiac metabolism and identifies two novel cardiac metabolic regulators. Oct 2023. URL: https://doi.org/10.1093/cvr/cvad154, doi:10.1093/cvr/cvad154. This article has 16 citations and is from a domain leading peer-reviewed journal.

11. (martineztittonel2025leftventricularnoncompaction pages 5-7): Luis Elias Martínez-Tittonel, Florin Ciorba, Xavier Bayona-Huguet, and Edgardo Kaplinsky. Left ventricular non-compaction cardiomyopathy: a review of the pathophysiology, epidemiology, diagnosis, genetics, and clinical management. Jul 2025. URL: https://doi.org/10.20944/preprints202507.1652.v1, doi:10.20944/preprints202507.1652.v1.

12. (NCT03572569 chunk 1):  Risk Stratification in Children and Adolescents With Primary Cardiomyopathy. German Heart Institute. 2013. ClinicalTrials.gov Identifier: NCT03572569

13. (aung2020prognosticsignificanceof pages 1-2): Nay Aung, Sara Doimo, Fabrizio Ricci, Mihir M. Sanghvi, Cesar Pedrosa, Simon P. Woodbridge, Amer Al-Balah, Filip Zemrak, Mohammed Y. Khanji, Patricia B. Munroe, Huseyin Naci, and Steffen E. Petersen. Prognostic significance of left ventricular noncompaction. Circulation. Cardiovascular Imaging, 13:e009712-e009712, Jan 2020. URL: https://doi.org/10.1161/circimaging.119.009712, doi:10.1161/circimaging.119.009712. This article has 143 citations.

14. (piekutowskaabramczuk2022geneticprofileof pages 3-5): Dorota Piekutowska-Abramczuk, Agata Paszkowska, Elżbieta Ciara, Kamila Frączak, Alicja Mirecka-Rola, Dorota Wicher, Agnieszka Pollak, Karolina Rutkowska, Jędrzej Sarnecki, and Lidia Ziółkowska. Genetic profile of left ventricular noncompaction cardiomyopathy in children—a single reference center experience. Genes, 13:1334, Jul 2022. URL: https://doi.org/10.3390/genes13081334, doi:10.3390/genes13081334. This article has 20 citations.

15. (umapathi2025…geneticvariant pages 1-2): KK Umapathi, SB Schmidt, and U Kohli. … genetic variant in prdm16 is associated with wolff–parkinson–white syndrome with complex accessory pathway characteristics and left ventricular non-compaction …. Unknown journal, 2025.

16. (umapathi2025araregenetic pages 1-2): KK Umapathi, SB Schmidt, and U Kohli. A rare genetic variant in prdm16 is associated with wolff–parkinson–white syndrome with complex accessory pathway characteristics and left ventricular non …. Unknown journal, 2025.

17. (llerenavelastegui2024prevalenceclinicalmanifestations pages 1-2): Jordan Llerena-Velastegui, Almendra Lopez-Usina, and Camila Mantilla-Cisneros. Prevalence, clinical manifestations, and adverse outcomes of left ventricular noncompaction in adults: a systematic review and meta-analysis. Oct 2024. URL: https://doi.org/10.14740/cr1673, doi:10.14740/cr1673. This article has 6 citations.

18. (NCT06024759 chunk 1):  Predictors of Risk in Left Ventricular Non-Compaction. London Health Sciences Centre Research Institute OR Lawson Research Institute of St. Joseph's. 2023. ClinicalTrials.gov Identifier: NCT06024759

19. (NCT04265040 chunk 1): Benjamin Meder. DZHK TORCH-Plus is a Registry for Patients With Cardiomyopathies and Serves as Source for Cardiovascular Research Studies. University Hospital Heidelberg. 2020. ClinicalTrials.gov Identifier: NCT04265040

## Artifacts

- [Edison artifact artifact-00](Left_Ventricular_Noncompaction_8-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 13 |
| On topic | 10 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 23 |
| Resolved | 23 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 3 |
| Terms named correctly | 2 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014152` (4 mentions) - the report calls it "if available"; MONDO calls it **left ventricular noncompaction 8**