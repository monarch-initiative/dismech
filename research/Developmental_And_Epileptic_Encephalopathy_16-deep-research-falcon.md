---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-07T02:49:46.534245'
end_time: '2026-09-07T03:01:58.290315'
duration_seconds: 731.76
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Developmental And Epileptic Encephalopathy 16
  mondo_id: MONDO:0014133
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
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 2
  validator_version: 0.2.1
term_validation:
  total_terms: 28
  verified: 28
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 1
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0014133
    reported_labels:
    - if available
    ontology_label: developmental and epileptic encephalopathy, 16
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Developmental_And_Epileptic_Encephalopathy_16-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Developmental And Epileptic Encephalopathy 16
- **MONDO ID:** MONDO:0014133 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Developmental And Epileptic Encephalopathy 16** covering all of the
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
- **Disease Name:** Developmental And Epileptic Encephalopathy 16
- **MONDO ID:** MONDO:0014133 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Developmental And Epileptic Encephalopathy 16** covering all of the
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


# Developmental and Epileptic Encephalopathy 16: Disease-Characteristics Report

## Executive summary and evidence boundaries

Developmental and epileptic encephalopathy 16 (DEE16), formerly early-infantile epileptic encephalopathy 16 (EIEE16), is an ultrarare, usually autosomal-recessive neurodevelopmental disorder caused by biallelic pathogenic variants in **TBC1D24**. It is characterized by neonatal or early-infantile seizures—often multiple, prolonged, fever-sensitive, and drug-resistant—together with severe developmental impairment. DEE16 is the severe end of a much broader allelic spectrum that also includes familial infantile myoclonic epilepsy, focal epilepsy, progressive myoclonus phenotypes, DOORS syndrome, and dominant or recessive nonsyndromic hearing loss. Findings from those other phenotypes should not automatically be assigned to DEE16. (tona2019thephenotypiclandscape pages 2-3, spoto2022synaptopathiesindevelopmental pages 11-13, balestrini2016tbc1d24genotype–phenotypecorrelation pages 1-2)

The evidence base is small and consists predominantly of individual cases, literature-assembled cohorts, patient-derived neurons, and animal models. Consequently, many quoted frequencies below are from a **48-person pan-TBC1D24 epilepsy cohort**, not a population-based DEE16 cohort. Disease-specific prevalence, survival curves, treatment-response rates, and quality-of-life scores are unavailable. The retrieval system supplied DOI records but generally did not expose PubMed identifiers; PMIDs are therefore not invented or inferred.

| Domain | Curated finding | Ontology or identifier suggestions | Evidence scope and limitations |
|---|---|---|---|
| Identity | Developmental and epileptic encephalopathy 16, or DEE16, was formerly called early-infantile epileptic encephalopathy 16, or EIEE16. It is a severe early-onset epilepsy and neurodevelopmental disorder within the TBC1D24-related disorder spectrum. | OMIM: 615338; MONDO: MONDO:0014133, supplied by user; synonyms: DEE16, EIEE16, TBC1D24-associated early-infantile epileptic encephalopathy | DEE16 must not be conflated with milder TBC1D24 epilepsies, dominant or recessive nonsyndromic deafness, or DOORS syndrome. (tona2019thephenotypiclandscape pages 2-3, tona2019thephenotypiclandscape pages 1-2) |
| Etiology and inheritance | Classic DEE16 is caused by germline biallelic pathogenic variants in TBC1D24, usually homozygous or compound heterozygous, and follows autosomal-recessive inheritance. | Gene: TBC1D24; NCBI Gene: 57465; inheritance: autosomal recessive | A broad 48-person epilepsy cohort was almost entirely biallelic. Isolated heterozygous variants and multigene 16p13.3 deletions have been associated with other epilepsy phenotypes but do not establish classic DEE16. (finelli2019theepilepsyassociatedprotein pages 5-6, balestrini2016tbc1d24genotype–phenotypecorrelation pages 3-4) |
| Onset and seizures | DEE-focused literature reports onset from approximately 20 minutes after birth to 8 months, with 28 of 30 reported DEE cases beginning by 3 months. Seizures may be myoclonic, clonic, tonic, focal, multifocal, migrating focal, generalized tonic-clonic, epileptic spasms, or prolonged status episodes. | HPO: HP:0001250 Seizure; HP:0002123 Generalized myoclonic seizure; HP:0002069 Bilateral tonic-clonic seizure; HP:0012469 Infantile spasms; HP:0002133 Status epilepticus | The 30-case figures derive from a literature-compiled TBC1D24-DEE table, not a prospective DEE16 registry. In the broader 48-person TBC1D24 epilepsy cohort, onset averaged 7 months, range less than 1 hour to 8 years; 60% had myoclonic or clonic seizures and 79% had prolonged seizures or status epilepticus. (spoto2022synaptopathiesindevelopmental pages 11-13, balestrini2016tbc1d24genotype–phenotypecorrelation pages 1-2, balestrini2016tbc1d24genotype–phenotypecorrelation pages 2-3) |
| Triggers and EEG | Fever or infection may precipitate seizures or status. Fatigue, repetitive movement, feeding, sensory stimulation, drowsiness, constipation, and delayed medication have also been reported as triggers. EEG may show background slowing, multifocal or generalized epileptiform discharges, or hypsarrhythmia. | HPO: HP:0002373 Febrile seizures; HP:0011182 EEG abnormality; HP:0010841 Multifocal epileptiform discharges; HP:0002521 Hypsarrhythmia | Evidence largely comes from the broader TBC1D24 epilepsy spectrum: fever or infection precipitated episodes in 19 of 48 patients, whereas 13 of 48 had a normal interictal EEG. Clinical photosensitivity was absent in that cohort. (spoto2022synaptopathiesindevelopmental pages 11-13, balestrini2016tbc1d24genotype–phenotypecorrelation pages 2-3, balestrini2016tbc1d24genotype–phenotypecorrelation pages 3-4) |
| Neurodevelopment and neurologic phenotype | Severe or profound global developmental delay or intellectual disability, psychomotor stagnation or regression, hypotonia, impaired speech, and major motor disability are characteristic. Ataxia, dystonia or other extrapyramidal signs, visual impairment, and sensorineural hearing loss occur variably. | HPO: HP:0001263 Global developmental delay; HP:0001249 Intellectual disability; HP:0001252 Hypotonia; HP:0001251 Ataxia; HP:0001332 Dystonia; HP:0000407 Sensorineural hearing impairment; HP:0000505 Visual impairment | In the broader cohort, 39 of 48 had developmental delay or intellectual disability, but eight relatives with benign familial infantile myoclonic epilepsy had normal development. Spectrum-level frequencies therefore should not be treated as DEE16-specific estimates. (balestrini2016tbc1d24genotype–phenotypecorrelation pages 2-3, spoto2022synaptopathiesindevelopmental pages 11-13, balestrini2016tbc1d24genotype–phenotypecorrelation pages 3-4) |
| Neuroimaging and anatomy | Imaging may initially be normal or may show cerebral or cerebellar atrophy, delayed myelination, cerebellar signal abnormalities or hypoplasia, and occasionally hippocampal sclerosis. The central nervous system is primarily affected, particularly the cerebral cortex, hippocampus, cerebellum, axons, and synapses. | HPO: HP:0002059 Cerebral atrophy; HP:0001272 Cerebellar atrophy; HP:0012448 Delayed myelination; HP:0001321 Cerebellar hypoplasia; UBERON suggestions: cerebral cortex, hippocampus, cerebellum | In the broader 48-person cohort, 16 had cerebral or cerebellar atrophy, five had delayed myelination, three had hippocampal sclerosis, and 11 had cerebellar abnormalities. No imaging feature consistently predicted phenotype or prognosis. (balestrini2016tbc1d24genotype–phenotypecorrelation pages 2-3, balestrini2016tbc1d24genotype–phenotypecorrelation pages 3-4) |
| Molecular mechanism | Pathogenic variants generally reduce or disrupt TBC1D24 function. Defects involving its TBC lipid-binding and TLDc domains disturb ARF6- and Rab-related membrane trafficking, growth-cone endocytosis, synaptic-vesicle recycling, neuronal migration, axon formation, dendritic-spine maintenance, and oxidative-stress resistance. These defects alter neuronal connectivity and excitability, leading to seizures and developmental impairment. | GO suggestions: synaptic vesicle endocytosis; endosomal transport; regulation of ARF protein signal transduction; axon development; neuron migration; dendritic spine maintenance; response to oxidative stress. CL suggestions: neuron; cortical neuron; hippocampal neuron | ARF6, axonal, and synaptic findings are demonstrated in rodent neurons, patient-derived induced pluripotent stem-cell neurons, and mice. The complete causal chain to human DEE16 remains partly inferred. Severe patient-derived neurons showed axon-formation defects absent from a milder epilepsy line. (pepe2023arolein pages 14-17, finelli2019theepilepsyassociatedprotein pages 13-14, lin2020theepilepsyand pages 1-2, aprile2019tbc1d24regulatesaxonal pages 1-2) |
| 2024 mechanistic development | The TBC1D24 TLDc domain specifically binds the C2 domain of KIBRA, encoded by WWC1. Recessive epilepsy-associated variants p.Gly511Arg and p.Ala515Val abolished or weakened this interaction, linking TBC1D24 dysfunction to a synaptic and cognition-related scaffold pathway. | Genes and proteins: TBC1D24 and WWC1 or KIBRA; candidate pathways: Hippo signaling, scaffold organization, and synaptic signaling | Demonstrated using yeast two-hybrid and nanoscale pull-down assays, with hippocampal co-expression supporting biological plausibility. Necessity of the interaction in human DEE16 and its therapeutic tractability remain unproven. Published online 28 August 2024. (tona2024interactionbetweenthe pages 13-14, tona2024interactionbetweenthe pages 1-2) |
| Diagnosis | Diagnosis combines seizure and developmental history, video EEG, brain MRI, hearing, vision, and neurologic assessments, plus molecular confirmation of pathogenic or likely pathogenic variants on opposite TBC1D24 alleles. Trio whole-exome or whole-genome sequencing, or a comprehensive epilepsy panel with deletion and duplication analysis, is preferred. Parental segregation is essential. | Suggested tests: trio WES; trio WGS; epilepsy multigene panel; copy-number analysis; ACMG and AMP variant classification | A 2024 general DEE cohort found pathogenic variants in 35 of 82 WES tests, a 43% diagnostic yield, supporting first-line WES; this is not a DEE16-specific yield. Chromosomal microarray is useful when a copy-number variant is suspected. (vetri2024wholeexomesequencing pages 1-2, scheffer2024developmentalandepileptic pages 1-4) |
| Treatment status | No approved TBC1D24- or DEE16-specific disease-modifying treatment exists. Management is individualized with antiseizure polytherapy and rescue treatment for prolonged seizures, plus feeding, respiratory, hearing, vision, physical, occupational, speech, developmental, and psychosocial support. | NCIT suggestions: Anticonvulsant Therapy; Electroencephalography; Physical Therapy; Occupational Therapy; Speech Therapy; Genetic Counseling | In the broader cohort, 30 of 48 had drug-resistant epilepsy and 18 responded well. Benefits were reported with valproate, phenobarbital, phenytoin plus clobazam, zonisamide, topiramate, and other combinations, but uncontrolled observations do not establish a preferred DEE16 regimen. (balestrini2016tbc1d24genotype–phenotypecorrelation pages 1-2, balestrini2016tbc1d24genotype–phenotypecorrelation pages 2-3) |
| Experimental treatment | N-acetylcysteine amide and alpha-tocopherol restored vesicle trafficking and sustained activity in a humanized TBC1D24 p.Gly501Arg fly model, suggesting oxidative-stress modulation as a research direction. | CHEBI suggestions: N-acetylcysteine amide; alpha-tocopherol; antioxidant | Rescue was demonstrated in Drosophila modeling a milder TLDc-associated epilepsy and dystonia phenotype, not in humans or a DEE16 clinical trial. No relevant interventional DEE16 trial was identified in the search. (luthy2019tbc1d24tldcrelatedepilepsyexerciseinduced pages 1-2) |
| Prognosis | DEE16 is chronic and may cause profound lifelong disability, persistent drug-resistant seizures, and childhood death. Respiratory failure, infection-associated status epilepticus, and sudden unexpected death in epilepsy are recognized risks across severe TBC1D24 epilepsies. | HPO: HP:0001250 Seizure; HP:0001263 Global developmental delay; HP:0003811 Lethal infantile encephalopathy | In the broader cohort, 9 of 48 patients, or 19%, were deceased; mean age at death was 37 months, range 6 to 96 months, including one probable SUDEP. Among 17 individuals with a truncating or splice variant, 15 had drug-resistant epilepsy and eight died by age seven. These are retrospective spectrum-level data, not DEE16 survival estimates. (balestrini2016tbc1d24genotype–phenotypecorrelation pages 2-3, balestrini2016tbc1d24genotype–phenotypecorrelation pages 3-4) |
| Models | Models include patient-derived induced pluripotent stem-cell neurons, TBC1D24-silenced rodent cortical neurons, Drosophila skywalker mutants and humanized flies, and several mice. Homozygous S324Tfs*3 mice develop abrupt spontaneous seizures at postnatal day 15; homozygous F251L mice show hyperexcitability, spontaneous seizures, and premature death. | Taxa: Homo sapiens NCBITaxon:9606; Mus musculus NCBITaxon:10090; Rattus norvegicus NCBITaxon:10116; Drosophila melanogaster NCBITaxon:7227. Model types: knock-in; knockdown; humanized transgenic; induced pluripotent stem-cell-derived neuron | S324Tfs*3 seizure onset coincides with a developmentally regulated micro-exon switch. F251L destabilizes TBC1D24 and impairs excitatory-synapse maintenance. Models reproduce selected seizure, survival, trafficking, axonal, or cognitive features, but not the full human multisystem phenotype. (tona2019thephenotypiclandscape pages 1-2, lin2020theepilepsyand pages 1-2, aprile2019tbc1d24regulatesaxonal pages 1-2) |
| Epidemiologic evidence gap | DEE16 is ultrarare, but no reliable disease-specific prevalence, incidence, carrier frequency, ethnic enrichment, founder effect, or sex ratio has been established. | MONDO: MONDO:0014133, supplied by user | The 48-person spectrum cohort included 28 males and 20 females, but non-population-based ascertainment precludes estimation of a sex ratio. General DEE incidence estimates must not be assigned to DEE16. (balestrini2016tbc1d24genotype–phenotypecorrelation pages 1-2, scheffer2024developmentalandepileptic pages 1-4) |


*Table: Concise curation of DEE16 identity, genetics, phenotype, mechanism, diagnosis, management, prognosis, and experimental models. Evidence boundaries distinguish DEE16-specific observations from broader TBC1D24-spectrum findings.*

## 1. Disease information

**Definition.** DEE16 is a genetic developmental and epileptic encephalopathy in which the underlying TBC1D24 defect impairs neurodevelopment and synaptic function, while recurrent seizures and epileptiform activity may add further developmental burden. This conforms to the modern ILAE concept of DEE, which recognizes contributions from both the primary etiology and epileptic activity. (vetri2024wholeexomesequencing pages 1-2, scheffer2024developmentalandepileptic pages 1-4)

**Identifiers and synonyms.** The principal identifiers are **OMIM 615338** and the user-specified **MONDO:0014133**. Common names are “developmental and epileptic encephalopathy 16,” “DEE16,” “early-infantile epileptic encephalopathy 16,” “EIEE16,” and “TBC1D24-associated early-infantile epileptic encephalopathy.” No dedicated MeSH, ICD-10, or ICD-11 code was verified; clinically it is ordinarily represented under broader epilepsy/epileptic-encephalopathy and developmental-disability codes. EIEE16 can occur with or without hearing loss. (tona2019thephenotypiclandscape pages 2-3, tona2019thephenotypiclandscape pages 1-2)

**Data provenance.** Available knowledge is aggregated from published patients and families rather than EHR-derived population surveillance. The largest detailed source examined assembled 11 newly characterized and 37 previously published individuals with TBC1D24-related epilepsy. Its abstract states: “TBC1D24-related epilepsy syndromes show marked phenotypic pleiotropy,” ranging from benign epilepsy to early-onset encephalopathy with severe delay and early death. (balestrini2016tbc1d24genotype–phenotypecorrelation pages 1-2)

## 2. Etiology, risk, protection, and environment

Classic DEE16 results from **germline biallelic TBC1D24 pathogenic variants**, either homozygous or compound heterozygous. Consanguinity increases the probability that both parents carry the same rare allele, but affected children also occur in nonconsanguineous families. Segmental uniparental isodisomy is a rare alternative route to biallelic disease. Heterozygous TBC1D24 variants and multigene 16p13.3 deletions can produce other epilepsy phenotypes, but these do not define classic recessive DEE16. (finelli2019theepilepsyassociatedprotein pages 5-6, balestrini2016tbc1d24genotype–phenotypecorrelation pages 2-3, balestrini2016tbc1d24genotype–phenotypecorrelation pages 3-4)

No validated environmental cause, lifestyle risk factor, infectious cause, genetic protective allele, or human protective exposure is known. Fever and infection can **trigger seizures/status epilepticus** in an affected individual but do not cause the Mendelian disease: 19 of 48 individuals in the broad cohort had fever- or infection-precipitated episodes. Fatigue, drowsiness, repetitive movement, feeding, sensory stimulation, constipation, and delayed medication were additional reported seizure precipitants. (balestrini2016tbc1d24genotype–phenotypecorrelation pages 1-2, balestrini2016tbc1d24genotype–phenotypecorrelation pages 2-3)

A plausible gene–environment interaction is reduced cellular tolerance of activity-associated reactive oxygen species: TLDc-domain dysfunction increased oxidative-stress sensitivity in a fly model. This is mechanistic/preclinical evidence, not proof that environmental oxidants alter human penetrance. (luthy2019tbc1d24tldcrelatedepilepsyexerciseinduced pages 1-2)

## 3. Phenotypes

### Core neurologic phenotype

A DEE-focused literature compilation identified seizure onset from approximately **20 minutes after birth to 8 months**, with **28/30 cases beginning by 3 months**. Reported seizure types include myoclonic and clonic seizures, tonic seizures, focal and multifocal seizures, migrating focal seizures, generalized tonic–clonic seizures, epileptic spasms, absence seizures, and convulsive or nonconvulsive status epilepticus. Suggested terms include **HP:0001250 Seizure**, **HP:0002123 generalized myoclonic seizure**, **HP:0012469 infantile spasms**, **HP:0002069 bilateral tonic-clonic seizure**, and **HP:0002133 status epilepticus**. (spoto2022synaptopathiesindevelopmental pages 11-13)

In the broader cohort, onset averaged 7 months but ranged from under 1 hour to 8 years; 29/48 (60%) had myoclonic or clonic seizures and 38/48 (79%) had status epilepticus or seizures lasting over five minutes. Myoclonus could be segmental or generalized, unilateral or bilateral, migrating, alternating, rhythmic or pseudorhythmic, and could persist in clusters for days. These spectrum-wide figures likely underestimate the severity and earlier onset of DEE16. (balestrini2016tbc1d24genotype–phenotypecorrelation pages 1-2, balestrini2016tbc1d24genotype–phenotypecorrelation pages 2-3)

**EEG.** Findings include slow background, multifocal or generalized epileptiform abnormalities, focal discharges, and hypsarrhythmia; suggested terms are **HP:0011182 EEG abnormality**, **HP:0010841 multifocal epileptiform discharges**, and **HP:0002521 hypsarrhythmia**. Thirteen of 48 spectrum patients had a normal interictal recording, illustrating that a normal single EEG does not exclude a TBC1D24 disorder. Only two had a photoparoxysmal response, and none showed clinical photosensitivity. (spoto2022synaptopathiesindevelopmental pages 11-13, balestrini2016tbc1d24genotype–phenotypecorrelation pages 3-4)

### Development, motor function, behavior, and sensory findings

Severe global developmental delay or intellectual disability, psychomotor stagnation/regression, hypotonia, absent or very limited speech, and marked motor disability are typical of DEE16. Relevant terms include **HP:0001263 global developmental delay**, **HP:0001249 intellectual disability**, **HP:0001252 hypotonia**, and **HP:0001344 absent speech**. Across the broader cohort, 39/48 had developmental delay or intellectual disability, whereas eight relatives with benign familial infantile myoclonic epilepsy had normal development—an important demonstration of allelic pleiotropy. (spoto2022synaptopathiesindevelopmental pages 11-13, balestrini2016tbc1d24genotype–phenotypecorrelation pages 3-4)

Variable associated findings include ataxia (**HP:0001251**), dystonia (**HP:0001332**), other extrapyramidal signs, visual impairment (**HP:0000505**), and sensorineural hearing impairment (**HP:0000407**). In the spectrum cohort, seven had ataxia, eight had extrapyramidal signs, 13/48 (27%) had visual impairment, and three non-DOORS patients had bilateral sensorineural deafness. Acral, nail, and bone abnormalities instead suggest overlapping **DOORS syndrome** and should not be considered obligatory DEE16 manifestations. (balestrini2016tbc1d24genotype–phenotypecorrelation pages 2-3, balestrini2016tbc1d24genotype–phenotypecorrelation pages 3-4)

**Quality of life.** No DEE16-specific EQ-5D, SF-36, PROMIS, or caregiver-burden study was found. Severe epilepsy, nonverbal status, dependence for mobility and activities of daily living, sensory impairment, feeding/respiratory risks, and repeated emergency care imply profound patient and caregiver burden. Contemporary experts emphasize that DEEs require substantial lifelong support and impose high psychosocial burden on families and communities. (scheffer2024developmentalandepileptic pages 1-4)

## 4. Genetic and molecular information

**Gene.** **TBC1D24** encodes a 559-amino-acid protein in its longest cited isoform, containing an N-terminal TBC region and C-terminal TLDc domain. TBC1D24 is expressed broadly but is particularly relevant in neurons and is found at the trans-Golgi network, clathrin-coated vesicles, growth cones, and pre- and postsynaptic sites. Suggested identifiers are HGNC symbol **TBC1D24** and NCBI Gene **57465**. (pepe2023arolein pages 14-17, tona2024interactionbetweenthe pages 1-2, aprile2019tbc1d24regulatesaxonal pages 1-2)

**Variant classes and interpretation.** Reported disease alleles include missense, nonsense, frameshift, splice-site, small insertion/deletion, and larger copy-number variants. Examples in DEE-focused compilations include p.Ser45Arg, p.Gly139Val, p.Pro144Leu, p.Lys206Glu, p.Arg237Trp, p.Arg266Cys, p.Gly346Val, p.Gly359Arg, and p.Glu373Lys. Classification should follow current ACMG/AMP criteria and require phenotype concordance, population rarity, segregation, phase confirmation, predicted loss of function where applicable, and functional evidence. No single list should be treated as permanently pathogenic without checking the current ClinVar record and transcript. (spoto2022synaptopathiesindevelopmental pages 11-13)

All well-supported patients in the 2016 epilepsy cohort had biallelic mutations except one clinically typical DOORS case in whom only one variant was detected. Frameshift, nonsense, or splice variants generally predicted worse outcome: among 17 carriers of at least one such allele, 15 had drug-resistant epilepsy and eight died by age seven. Nevertheless, missense effects are heterogeneous, and no reliable position-only genotype–phenotype rule exists. Variants associated with the severest disease were not always the most disruptive in neurite-outgrowth assays. (balestrini2016tbc1d24genotype–phenotypecorrelation pages 1-2, balestrini2016tbc1d24genotype–phenotypecorrelation pages 3-4)

DEE16 alleles are expected to be absent or extremely rare in population databases; an exact gnomAD frequency must be reported variant by variant. They are germline, not recognized somatic cancer drivers. No validated modifier gene, disease-specific episignature, methylation abnormality, repeat expansion, aneuploidy, or recurrent balanced rearrangement is established. Multigene 16p13.3 deletions involving TBC1D24 can cause epilepsy, microcephaly, and developmental delay but represent a contiguous-gene disorder rather than canonical DEE16. (finelli2019theepilepsyassociatedprotein pages 5-6)

## 5. Environmental information

DEE16 is not caused by toxins, radiation, pollution, diet, smoking, alcohol, occupation, or an infectious agent. Fever/infection may lower seizure threshold and precipitate prolonged episodes. Accordingly, rapid treatment of intercurrent illness, hydration, avoidance of missed antiseizure doses, and an individualized rescue plan are clinically relevant, although they do not alter the inherited lesion. No disease-specific dietary or exercise intervention has proven preventive efficacy. (balestrini2016tbc1d24genotype–phenotypecorrelation pages 2-3)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Biallelic pathogenic TBC1D24 variants lead to** reduced protein abundance, stability, or domain function; this is demonstrated for several alleles but inferred for variants lacking functional assays. (finelli2019theepilepsyassociatedprotein pages 13-14, lin2020theepilepsyand pages 1-2)
2. **TBC/TLDc dysfunction leads to** disturbed phosphoinositide-membrane association, ARF6/Rab-related signaling, oxidative-stress handling, and—in two 2024-tested alleles—loss or weakening of TBC1D24–KIBRA binding. (tona2024interactionbetweenthe pages 1-2, aprile2019tbc1d24regulatesaxonal pages 1-2, luthy2019tbc1d24tldcrelatedepilepsyexerciseinduced pages 1-2)
3. **Abnormal small-GTPase and membrane regulation leads to** defective growth-cone endocytosis, enlarged endosomal compartments, and impaired synaptic-vesicle sorting/recycling. (pepe2023arolein pages 14-17, finelli2019theepilepsyassociatedprotein pages 13-14, aprile2019tbc1d24regulatesaxonal pages 1-2)
4. **Defective trafficking leads to** impaired neuronal migration, axonal specification/callosal projection, neurite growth, dendritic-spine maintenance, and pre- and postsynaptic dysfunction. (lin2020theepilepsyand pages 1-2, aprile2019tbc1d24regulatesaxonal pages 1-2)
5. **Altered neuronal connectivity and vesicle cycling lead to** abnormal neurotransmission and increased network excitability; direct links are demonstrated in models and inferred in human cortex. (tona2019thephenotypiclandscape pages 1-2, lin2020theepilepsyand pages 1-2)
6. **Network hyperexcitability results in** neonatal/infantile multifocal seizures, spasms, and status epilepticus. **In parallel**, primary developmental wiring defects result in developmental encephalopathy; recurrent epileptic activity may further worsen development. (spoto2022synaptopathiesindevelopmental pages 11-13, vetri2024wholeexomesequencing pages 1-2, scheffer2024developmentalandepileptic pages 1-4)
7. **Severe, prolonged epilepsy plus neurologic dysfunction leads to** profound disability and risks of aspiration/respiratory failure, infection-associated status, and premature death. (balestrini2016tbc1d24genotype–phenotypecorrelation pages 2-3, balestrini2016tbc1d24genotype–phenotypecorrelation pages 3-4)

### Mechanistic detail and annotations

TBC1D24 binds ARF6 through its TBC region and appears to restrain active ARF6-GTP, although it lacks canonical residues expected of a conventional GAP. Knockdown causes migration, neurite, axonal-specification, action-potential, and dendritic-spine defects; dominant-negative ARF6 rescues several model phenotypes. Patient iPSC-derived neurons from a severe developmental encephalopathy showed axon-formation defects that were absent in neurons from a milder epilepsy case. (pepe2023arolein pages 14-17, aprile2019tbc1d24regulatesaxonal pages 1-2)

Presynaptically, reduced TBC1D24 slows vesicle endocytosis and produces enlarged endosomal accumulations; postsynaptically, TBC1D24 inhibits ARF6 and maintains excitatory dendritic spines. Suggested GO terms include **synaptic vesicle endocytosis**, **endosomal transport**, **regulation of ARF protein signal transduction**, **neuron migration**, **axon development**, **dendritic spine maintenance**, **chemical synaptic transmission**, and **response to oxidative stress**. Suggested cell types include **CL:0000540 neuron**, cortical projection neurons, hippocampal neurons, and excitatory neurons. (pepe2023arolein pages 14-17, finelli2019theepilepsyassociatedprotein pages 13-14, lin2020theepilepsyand pages 1-2)

The TLDc domain has a neuroprotective/oxidative-stress role. In a humanized p.Gly501Arg fly, activity-induced locomotor and vesicle-trafficking defects were associated with oxidative-stress sensitivity and rescued by N-acetylcysteine amide or alpha-tocopherol. This supports a redox-sensitive synaptic mechanism but derives from a milder epilepsy/dystonia allele, not DEE16 patients. (luthy2019tbc1d24tldcrelatedepilepsyexerciseinduced pages 1-2)

**Latest mechanistic development, 2024.** Tona et al., published online **28 August 2024**, identified a specific interaction between the TBC1D24 TLDc domain and the C2 domain of KIBRA/WWC1. Recessive epilepsy-associated p.Gly511Arg and p.Ala515Val disrupted the human interaction. The abstract states that this finding “reveals a pathogenic mechanism of TBC1D24-associated epilepsy, linking the TBC1D24 and KIBRA pathways.” Hippocampal coexpression supports in-vivo plausibility, but necessity in human DEE16 and therapeutic tractability remain unproven. DOI: https://doi.org/10.1016/j.jbc.2024.107725. (tona2024interactionbetweenthe pages 13-14, tona2024interactionbetweenthe pages 1-2)

No replicated DEE16-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or integrated multi-omics signature was identified. Available “omics” primarily consist of genomic sequencing and patient-derived neuronal modeling.

## 7. Anatomical structures affected

The nervous system is primary. Relevant sites are the cerebral cortex and developing corticocortical projections, hippocampus, cerebellum, and synapses. Suggested UBERON concepts include **cerebral cortex**, **hippocampus**, **cerebellum**, **corpus callosum**, and **central nervous system**; relevant subcellular GO components include **synapse**, **presynaptic active zone**, **postsynaptic density**, **dendritic spine**, **growth cone**, **clathrin-coated vesicle**, **endosome**, and **trans-Golgi network**. (tona2019thephenotypiclandscape pages 1-2, tona2024interactionbetweenthe pages 1-2, lin2020theepilepsyand pages 1-2, aprile2019tbc1d24regulatesaxonal pages 1-2)

MRI may be initially nonspecific or normal. In the broader cohort, 16/48 had cerebral or cerebellar atrophy, five delayed myelination, three hippocampal sclerosis, and 11 cerebellar signal, atrophy, or hypoplasia abnormalities. No consistent relationship linked imaging to prognosis. Abnormalities are generally bilateral/diffuse rather than characteristically lateralized. The cochlea/auditory pathway can be secondarily relevant in patients with hearing loss. (balestrini2016tbc1d24genotype–phenotypecorrelation pages 3-4)

## 8. Temporal development

Onset is congenital-developmental at the molecular level and usually neonatal or early infantile clinically. Seizures may begin abruptly in the first hours or weeks and evolve into multiple seizure types, prolonged clusters, or status. Development may already be abnormal because of the genetic lesion and may plateau or regress with severe epileptic activity. (spoto2022synaptopathiesindevelopmental pages 11-13, scheffer2024developmentalandepileptic pages 1-4)

The course is chronic and highly variable. Severe DEE16 commonly remains drug-resistant with profound disability; milder TBC1D24 epilepsies can remit, so remission data from those disorders cannot be generalized. The period from fetal cortical development through the first postnatal years is probably the principal window of vulnerability. A mouse S324Tfs*3 model illustrates temporal biology: seizures appeared abruptly at postnatal day 15 as use of a conserved alternatively spliced micro-exon increased. (tona2019thephenotypiclandscape pages 1-2)

## 9. Inheritance and population

Inheritance is predominantly **autosomal recessive**. For two confirmed carrier parents, each pregnancy has a 25% probability of an affected child, 50% probability of an unaffected carrier, and 25% probability of inheriting neither familial allele, subject to confirmation of phase and parental status. Penetrance for two severe pathogenic alleles appears high, but expressivity is broad across the TBC1D24 spectrum. No anticipation mechanism is known. Parental germline mosaicism is theoretically possible but not quantified; uniparental isodisomy is documented as an unusual mechanism.

DEE16-specific incidence, prevalence, carrier frequency, founder effects, ethnic enrichment, and sex ratio are unknown. The 48-person cohort contained 28 males and 20 females, but referral ascertainment makes this unsuitable for estimating sex bias. General DEEs have cumulative childhood incidence estimates around 169/100,000 in one New Zealand study, but that statistic must not be assigned to DEE16. (balestrini2016tbc1d24genotype–phenotypecorrelation pages 1-2, scheffer2024developmentalandepileptic pages 1-4)

## 10. Diagnostics

**Clinical evaluation.** Obtain pregnancy/birth and three-generation family history, precise seizure semiology and triggers, serial video-EEG including sleep, brain MRI with epilepsy protocol, developmental and neurologic assessment, growth measurements, audiology, ophthalmology, feeding/swallowing and respiratory evaluation, and screening for movement disorder. Basic metabolic testing is useful when presentation is undiagnosed because treatable metabolic epilepsies can mimic DEE16, but no enzyme, metabolite, blood, urine, biopsy, or liquid-biopsy marker diagnoses TBC1D24 disease.

**Molecular testing.** Trio WES or WGS is preferred for an unexplained neonatal/infantile DEE; a comprehensive epilepsy/DEE panel including TBC1D24 with copy-number analysis is also appropriate. Confirm candidate variants by orthogonal testing where required, establish that biallelic variants are in trans, and test parents. WGS can detect noncoding, structural, and copy-number lesions missed by WES. CMA is useful when microcephaly, dysmorphism, congenital anomalies, or a contiguous-gene deletion is suspected. Karyotype/FISH, mitochondrial sequencing, and repeat-expansion assays are not routine DEE16 tests unless another diagnosis is suspected.

A 2024 first-line WES study of 82 unselected DEE cases found 35 pathogenic variants, a **43% yield**; 66% were de novo. This supports early genomic testing but is not a TBC1D24-specific yield. DOI: https://doi.org/10.3390/ijms25021146; published **17 January 2024**. (vetri2024wholeexomesequencing pages 1-2)

**Differential diagnosis.** Consider other neonatal/infantile DEEs—including STXBP1-, KCNQ2-, SCN2A-, SCN8A-, KCNT1-, CDKL5-, PCDH19-, GNAO1-, TUBA1A-, and metabolic/vitamin-responsive epilepsies—plus epilepsy of infancy with migrating focal seizures, infantile epileptic spasms syndrome, progressive myoclonus epilepsies, mitochondrial disorders, and structural cortical malformations. Within TBC1D24 disease, distinguish DEE16 from DOORS syndrome and milder epilepsy/hearing-loss phenotypes.

No population newborn screen is available. Targeted familial testing, cascade carrier testing, prenatal diagnosis, and preimplantation genetic testing are feasible after both causal alleles are established.

## 11. Outcome and prognosis

No valid DEE16-specific five- or ten-year survival rate or life-expectancy estimate exists. In the broader cohort, **9/48 (19%)** had died at a mean 37 months (range 6–96 months). Causes included infection, respiratory failure, infection-associated status epilepticus, unknown causes, and one probable SUDEP at 18 months. These retrospective spectrum-wide observations should not be interpreted as a DEE16 mortality rate. (balestrini2016tbc1d24genotype–phenotypecorrelation pages 2-3)

Poor prognostic indicators include neonatal onset, frequent prolonged seizures/status, drug resistance, profound early developmental impairment, respiratory/feeding complications, and truncating or splice-disrupting alleles. Among 17 cohort members with at least one frameshift, nonsense, or splice variant, 15 had drug-resistant epilepsy and eight died by age seven. Recovery to typical development is unlikely in severe DEE16, although seizure burden may improve. No validated molecular or circulating prognostic biomarker exists. (balestrini2016tbc1d24genotype–phenotypecorrelation pages 3-4)

## 12. Treatment and applications

There is **no approved TBC1D24-directed or disease-modifying therapy**. Treatment is individualized by seizure type and EEG syndrome, with prompt management of prolonged seizures and intercurrent illness. The 2016 spectrum cohort reported 30/48 with drug-resistant epilepsy and 18 with good treatment response. Observational benefits occurred with valproate or phenobarbital, phenytoin plus clobazam, zonisamide, topiramate, and other combinations; these uncontrolled data do not establish a preferred DEE16 algorithm. (balestrini2016tbc1d24genotype–phenotypecorrelation pages 1-2, balestrini2016tbc1d24genotype–phenotypecorrelation pages 2-3)

A practical strategy is: (1) classify seizure types and EEG syndrome; (2) select standard antiseizure therapy accordingly; (3) provide a home rescue plan and status protocol; (4) monitor sedation, respiration, feeding, hepatic/hematologic toxicity, and drug interactions; (5) reassess polytherapy regularly; and (6) integrate developmental, physical, occupational, speech/augmentative-communication, nutritional, hearing, vision, orthopedic, sleep, respiratory, and palliative-care expertise as needed. Suggested NCIT concepts include **Anticonvulsant Therapy**, **Electroencephalography**, **Physical Therapy**, **Occupational Therapy**, **Speech Therapy**, and **Genetic Counseling**.

No relevant interventional ClinicalTrials.gov study for DEE16/TBC1D24 was identified. Antioxidant rescue with N-acetylcysteine amide and alpha-tocopherol is preclinical and must not be used as evidence of human efficacy. Likewise, the 2024 KIBRA result identifies a possible target network but not a treatment. No gene replacement, editing, ASO, siRNA, mRNA, cell therapy, immunotherapy, or validated pharmacogenomic regimen is currently established. (tona2024interactionbetweenthe pages 1-2, luthy2019tbc1d24tldcrelatedepilepsyexerciseinduced pages 1-2)

## 13. Prevention

The de novo occurrence of symptoms cannot be prevented by vaccination, lifestyle, or environmental modification once a child has biallelic pathogenic variants. **Primary reproductive prevention** consists of genetic counseling, parental carrier confirmation, cascade testing, preimplantation genetic testing, or prenatal diagnosis. **Secondary prevention** consists of early genomic diagnosis, seizure recognition, EEG monitoring, and rapid initiation of appropriate therapy to reduce avoidable epileptic burden. **Tertiary prevention** includes rescue medication, fever/illness plans, aspiration and respiratory precautions, nutrition and bone-health support, injury prevention, SUDEP counseling, and rehabilitation.

Routine immunization remains appropriate unless an individual clinical contraindication exists; vaccines do not cause DEE16. Because fever can trigger seizures, vaccination planning and fever management should be individualized without withholding the protection against infections that can themselves provoke status.

## 14. Other species and natural disease

No well-established naturally occurring veterinary disease equivalent to human DEE16 was identified. There is no zoonotic transmission or cross-species infectious susceptibility because this is a germline Mendelian disorder. Relevant orthologous systems include **Mus musculus** (NCBITaxon:10090), **Rattus norvegicus** (10116), and **Drosophila melanogaster** (7227; ortholog *skywalker/sky*). Conservation of the TBC and TLDc functions supports comparative modeling, but species-specific isoforms and auditory biology limit direct extrapolation. (tona2019thephenotypiclandscape pages 2-3, tona2024interactionbetweenthe pages 1-2)

## 15. Model organisms and experimental systems

**Mouse S324Tfs*3.** Homozygous mice have abrupt spontaneous seizures beginning at postnatal day 15, coincident with a developmental switch that incorporates a conserved six-amino-acid micro-exon. Hippocampal TBC1D24 localizes to synapses and clathrin-coated vesicles. Auditory and vestibular function were normal, demonstrating incomplete recapitulation of human multisystem disease. DOI: https://doi.org/10.1093/hmg/ddy445; published online **2 January 2019**. (tona2019thephenotypiclandscape pages 1-2)

**Mouse F251L.** This missense allele destabilizes TBC1D24. Homozygous knock-in mice develop neuronal hyperexcitability, spontaneous seizures, and premature death; heterozygotes survive but exhibit dendritic-spine and memory defects. Hippocampal knockdown similarly causes spine loss, impaired contextual fear memory, hyperactivity, and anxiety. DOI: https://doi.org/10.1371/journal.pgen.1008587; published **31 January 2020**. (lin2020theepilepsyand pages 1-2)

**Rodent and human neurons.** TBC1D24-silenced rat cortical neurons show impaired axonal specification, growth-cone endocytosis, axon-initial-segment maturation, action-potential firing, and callosal projection. Patient iPSC-derived neurons from severe developmental encephalopathy reproduced axon-formation defects, whereas a milder epilepsy line did not. DOI: https://doi.org/10.1038/s41418-019-0313-x; published online **11 March 2019**. (aprile2019tbc1d24regulatesaxonal pages 1-2)

**Drosophila.** *skywalker* models are efficient for synaptic-vesicle trafficking and oxidative-stress experiments. Humanized p.Gly501Arg flies showed activity-induced behavioral and vesicle-transport abnormalities rescued by antioxidants. Limitations include invertebrate circuitry, variant-specific phenotypes, and uncertain human dosing or safety. DOI: https://doi.org/10.1093/brain/awz175; advance publication **29 June 2019**. (luthy2019tbc1d24tldcrelatedepilepsyexerciseinduced pages 1-2)

## Overall assessment

Current expert understanding places DEE16 among presynaptic/postsynaptic trafficking disorders rather than a primary ion-channel disorder. The strongest disease model is biallelic TBC1D24 loss or dysfunction producing convergent defects in neuronal development, ARF6/Rab-associated membrane trafficking, synaptic-vesicle recycling, dendritic-spine maintenance, and cellular stress resistance. The 2024 discovery of variant-sensitive TBC1D24–KIBRA binding adds a specific molecular interaction to this framework, but clinical care remains symptomatic. Priorities are a disease-specific natural-history registry, standardized variant curation, longitudinal EEG/developmental outcomes, quantitative patient/caregiver measures, human-neuron validation of KIBRA and redox mechanisms, and carefully designed genotype-stratified therapeutic studies. (tona2024interactionbetweenthe pages 13-14, tona2024interactionbetweenthe pages 1-2, scheffer2024developmentalandepileptic pages 1-4)

References

1. (tona2019thephenotypiclandscape pages 2-3): Risa Tona, Wenqian Chen, Yoko Nakano, Laura D Reyes, Ronald S Petralia, Ya-Xian Wang, Matthew F Starost, Talah T Wafa, Robert J Morell, Kevin D Cravedi, Johann du Hoffmann, Takushi Miyoshi, Jeeva P Munasinghe, Tracy S Fitzgerald, Yogita Chudasama, Koichi Omori, Carlo Pierpaoli, Botond Banfi, Lijin Dong, Inna A Belyantseva, and Thomas B Friedman. The phenotypic landscape of a tbc1d24 mutant mouse includes convulsive seizures resembling human early infantile epileptic encephalopathy. Human Molecular Genetics, 28:1530–1547, Jan 2019. URL: https://doi.org/10.1093/hmg/ddy445, doi:10.1093/hmg/ddy445. This article has 41 citations and is from a domain leading peer-reviewed journal.

2. (spoto2022synaptopathiesindevelopmental pages 11-13): Giulia Spoto, Giulia Valentini, Maria Concetta Saia, Ambra Butera, Greta Amore, Vincenzo Salpietro, Antonio Gennaro Nicotera, and Gabriella Di Rosa. Synaptopathies in developmental and epileptic encephalopathies: a focus on pre-synaptic dysfunction. Frontiers in Neurology, Mar 2022. URL: https://doi.org/10.3389/fneur.2022.826211, doi:10.3389/fneur.2022.826211. This article has 46 citations and is from a peer-reviewed journal.

3. (balestrini2016tbc1d24genotype–phenotypecorrelation pages 1-2): Simona Balestrini, Mathieu Milh, Claudia Castiglioni, Kevin Lüthy, Mattea J. Finelli, Patrik Verstreken, Aaron Cardon, Barbara Gnidovec Stražišar, J. Lloyd Holder, Gaetan Lesca, Maria M. Mancardi, Anne L. Poulat, Gabriela M. Repetto, Siddharth Banka, Leonilda Bilo, Laura E. Birkeland, Friedrich Bosch, Knut Brockmann, J. Helen Cross, Diane Doummar, Temis M. Félix, Fabienne Giuliano, Mutsuki Hori, Irina Hüning, Hulia Kayserili, Usha Kini, Melissa M. Lees, Girish Meenakshi, Leena Mewasingh, Alistair T. Pagnamenta, Silvio Peluso, Antje Mey, Gregory M. Rice, Jill A. Rosenfeld, Jenny C. Taylor, Matthew M. Troester, Christine M. Stanley, Dorothee Ville, Magdalena Walkiewicz, Antonio Falace, Anna Fassio, Johannes R. Lemke, Saskia Biskup, Jessica Tardif, Norbert F. Ajeawung, Aslihan Tolun, Mark Corbett, Jozef Gecz, Zaid Afawi, Katherine B. Howell, Karen L. Oliver, Samuel F. Berkovic, Ingrid E. Scheffer, Fabrizio A. de Falco, Peter L. Oliver, Pasquale Striano, Federico Zara, Phillipe M. Campeau, and S.M. Sisodiya. Tbc1d24 genotype–phenotype correlation. Neurology, 87:77-85, Jul 2016. URL: https://doi.org/10.1212/wnl.0000000000002807, doi:10.1212/wnl.0000000000002807. This article has 163 citations and is from a highest quality peer-reviewed journal.

4. (tona2019thephenotypiclandscape pages 1-2): Risa Tona, Wenqian Chen, Yoko Nakano, Laura D Reyes, Ronald S Petralia, Ya-Xian Wang, Matthew F Starost, Talah T Wafa, Robert J Morell, Kevin D Cravedi, Johann du Hoffmann, Takushi Miyoshi, Jeeva P Munasinghe, Tracy S Fitzgerald, Yogita Chudasama, Koichi Omori, Carlo Pierpaoli, Botond Banfi, Lijin Dong, Inna A Belyantseva, and Thomas B Friedman. The phenotypic landscape of a tbc1d24 mutant mouse includes convulsive seizures resembling human early infantile epileptic encephalopathy. Human Molecular Genetics, 28:1530–1547, Jan 2019. URL: https://doi.org/10.1093/hmg/ddy445, doi:10.1093/hmg/ddy445. This article has 41 citations and is from a domain leading peer-reviewed journal.

5. (finelli2019theepilepsyassociatedprotein pages 5-6): Mattéa J Finelli, Davide Aprile, Enrico Castroflorio, Alexander Jeans, Matteo Moschetta, Lauren Chessum, Matteo T Degiacomi, Julia Grasegger, Alexis Lupien-Meilleur, Andrew Bassett, Elsa Rossignol, Philippe M Campeau, Michael R Bowl, Fabio Benfenati, Anna Fassio, and Peter L Oliver. The epilepsy-associated protein tbc1d24 is required for normal development, survival and vesicle trafficking in mammalian neurons. Human Molecular Genetics, 28:584-597, Oct 2019. URL: https://doi.org/10.1093/hmg/ddy370, doi:10.1093/hmg/ddy370. This article has 73 citations and is from a domain leading peer-reviewed journal.

6. (balestrini2016tbc1d24genotype–phenotypecorrelation pages 3-4): Simona Balestrini, Mathieu Milh, Claudia Castiglioni, Kevin Lüthy, Mattea J. Finelli, Patrik Verstreken, Aaron Cardon, Barbara Gnidovec Stražišar, J. Lloyd Holder, Gaetan Lesca, Maria M. Mancardi, Anne L. Poulat, Gabriela M. Repetto, Siddharth Banka, Leonilda Bilo, Laura E. Birkeland, Friedrich Bosch, Knut Brockmann, J. Helen Cross, Diane Doummar, Temis M. Félix, Fabienne Giuliano, Mutsuki Hori, Irina Hüning, Hulia Kayserili, Usha Kini, Melissa M. Lees, Girish Meenakshi, Leena Mewasingh, Alistair T. Pagnamenta, Silvio Peluso, Antje Mey, Gregory M. Rice, Jill A. Rosenfeld, Jenny C. Taylor, Matthew M. Troester, Christine M. Stanley, Dorothee Ville, Magdalena Walkiewicz, Antonio Falace, Anna Fassio, Johannes R. Lemke, Saskia Biskup, Jessica Tardif, Norbert F. Ajeawung, Aslihan Tolun, Mark Corbett, Jozef Gecz, Zaid Afawi, Katherine B. Howell, Karen L. Oliver, Samuel F. Berkovic, Ingrid E. Scheffer, Fabrizio A. de Falco, Peter L. Oliver, Pasquale Striano, Federico Zara, Phillipe M. Campeau, and S.M. Sisodiya. Tbc1d24 genotype–phenotype correlation. Neurology, 87:77-85, Jul 2016. URL: https://doi.org/10.1212/wnl.0000000000002807, doi:10.1212/wnl.0000000000002807. This article has 163 citations and is from a highest quality peer-reviewed journal.

7. (balestrini2016tbc1d24genotype–phenotypecorrelation pages 2-3): Simona Balestrini, Mathieu Milh, Claudia Castiglioni, Kevin Lüthy, Mattea J. Finelli, Patrik Verstreken, Aaron Cardon, Barbara Gnidovec Stražišar, J. Lloyd Holder, Gaetan Lesca, Maria M. Mancardi, Anne L. Poulat, Gabriela M. Repetto, Siddharth Banka, Leonilda Bilo, Laura E. Birkeland, Friedrich Bosch, Knut Brockmann, J. Helen Cross, Diane Doummar, Temis M. Félix, Fabienne Giuliano, Mutsuki Hori, Irina Hüning, Hulia Kayserili, Usha Kini, Melissa M. Lees, Girish Meenakshi, Leena Mewasingh, Alistair T. Pagnamenta, Silvio Peluso, Antje Mey, Gregory M. Rice, Jill A. Rosenfeld, Jenny C. Taylor, Matthew M. Troester, Christine M. Stanley, Dorothee Ville, Magdalena Walkiewicz, Antonio Falace, Anna Fassio, Johannes R. Lemke, Saskia Biskup, Jessica Tardif, Norbert F. Ajeawung, Aslihan Tolun, Mark Corbett, Jozef Gecz, Zaid Afawi, Katherine B. Howell, Karen L. Oliver, Samuel F. Berkovic, Ingrid E. Scheffer, Fabrizio A. de Falco, Peter L. Oliver, Pasquale Striano, Federico Zara, Phillipe M. Campeau, and S.M. Sisodiya. Tbc1d24 genotype–phenotype correlation. Neurology, 87:77-85, Jul 2016. URL: https://doi.org/10.1212/wnl.0000000000002807, doi:10.1212/wnl.0000000000002807. This article has 163 citations and is from a highest quality peer-reviewed journal.

8. (pepe2023arolein pages 14-17): SARA PEPE. A role in ph homeostasis regulation by genes related to neurodevelopmental disorders: tbc1d24 and atp6v1a. May 2023. URL: https://doi.org/10.15167/pepe-sara\_phd2023-05-15, doi:10.15167/pepe-sara\_phd2023-05-15. This article has 0 citations.

9. (finelli2019theepilepsyassociatedprotein pages 13-14): Mattéa J Finelli, Davide Aprile, Enrico Castroflorio, Alexander Jeans, Matteo Moschetta, Lauren Chessum, Matteo T Degiacomi, Julia Grasegger, Alexis Lupien-Meilleur, Andrew Bassett, Elsa Rossignol, Philippe M Campeau, Michael R Bowl, Fabio Benfenati, Anna Fassio, and Peter L Oliver. The epilepsy-associated protein tbc1d24 is required for normal development, survival and vesicle trafficking in mammalian neurons. Human Molecular Genetics, 28:584-597, Oct 2019. URL: https://doi.org/10.1093/hmg/ddy370, doi:10.1093/hmg/ddy370. This article has 73 citations and is from a domain leading peer-reviewed journal.

10. (lin2020theepilepsyand pages 1-2): Lianfeng Lin, Quanwei Lyu, Pui-Yi Kwan, Junjun Zhao, Ruolin Fan, Anping Chai, Cora Sau Wan Lai, Ying-Shing Chan, Xuting Shen, and Kwok-On Lai. The epilepsy and intellectual disability-associated protein tbc1d24 regulates the maintenance of excitatory synapses and animal behaviors. PLOS Genetics, 16:e1008587, Jan 2020. URL: https://doi.org/10.1371/journal.pgen.1008587, doi:10.1371/journal.pgen.1008587. This article has 28 citations and is from a domain leading peer-reviewed journal.

11. (aprile2019tbc1d24regulatesaxonal pages 1-2): Davide Aprile, Floriana Fruscione, Simona Baldassari, Manuela Fadda, Daniele Ferrante, Antonio Falace, Emmanuelle Buhler, Jacopo Sartorelli, Alfonso Represa, Pietro Baldelli, Fabio Benfenati, Federico Zara, and Anna Fassio. Tbc1d24 regulates axonal outgrowth and membrane trafficking at the growth cone in rodent and human neurons. Cell Death & Differentiation, 26:2464-2478, Mar 2019. URL: https://doi.org/10.1038/s41418-019-0313-x, doi:10.1038/s41418-019-0313-x. This article has 57 citations and is from a domain leading peer-reviewed journal.

12. (tona2024interactionbetweenthe pages 13-14): Risa Tona, Sayaka Inagaki, Yasuko Ishibashi, Rabia Faridi, Rizwan Yousaf, Isabelle Roux, Elizabeth Wilson, Cristina Fenollar-Ferrer, Wade W. Chien, Inna A. Belyantseva, and Thomas B. Friedman. Interaction between the tbc1d24 tldc domain and the kibra c2 domain is disrupted by two epilepsy-associated tbc1d24 missense variants. Journal of Biological Chemistry, 300:107725, Sep 2024. URL: https://doi.org/10.1016/j.jbc.2024.107725, doi:10.1016/j.jbc.2024.107725. This article has 8 citations and is from a domain leading peer-reviewed journal.

13. (tona2024interactionbetweenthe pages 1-2): Risa Tona, Sayaka Inagaki, Yasuko Ishibashi, Rabia Faridi, Rizwan Yousaf, Isabelle Roux, Elizabeth Wilson, Cristina Fenollar-Ferrer, Wade W. Chien, Inna A. Belyantseva, and Thomas B. Friedman. Interaction between the tbc1d24 tldc domain and the kibra c2 domain is disrupted by two epilepsy-associated tbc1d24 missense variants. Journal of Biological Chemistry, 300:107725, Sep 2024. URL: https://doi.org/10.1016/j.jbc.2024.107725, doi:10.1016/j.jbc.2024.107725. This article has 8 citations and is from a domain leading peer-reviewed journal.

14. (vetri2024wholeexomesequencing pages 1-2): Luigi Vetri, Francesco Calì, Salvatore Saccone, Mirella Vinci, Natalia Valeria Chiavetta, Marco Carotenuto, Michele Roccella, Carola Costanza, and Maurizio Elia. Whole exome sequencing as a first-line molecular genetic test in developmental and epileptic encephalopathies. International Journal of Molecular Sciences, 25:1146, Jan 2024. URL: https://doi.org/10.3390/ijms25021146, doi:10.3390/ijms25021146. This article has 25 citations.

15. (scheffer2024developmentalandepileptic pages 1-4): Ingrid E. Scheffer, Sameer Zuberi, Heather C. Mefford, Renzo Guerrini, and Amy McTague. Developmental and epileptic encephalopathies. Nature Reviews Disease Primers, Sep 2024. URL: https://doi.org/10.1038/s41572-024-00546-6, doi:10.1038/s41572-024-00546-6. This article has 175 citations.

16. (luthy2019tbc1d24tldcrelatedepilepsyexerciseinduced pages 1-2): Kevin Lüthy, Davide Mei, Baptiste Fischer, Maurizio De Fusco, Jef Swerts, Jone Paesmans, Elena Parrini, Naomi Lubarr, Inge A Meijer, Katherine M Mackenzie, Wang-Tso Lee, Davide Cittaro, Paolo Aridon, Nils Schoovaerts, Wim Versées, Patrik Verstreken, Giorgio Casari, and Renzo Guerrini. Tbc1d24-tldc-related epilepsy exercise-induced dystonia: rescue by antioxidants in a disease model. Brain : a journal of neurology, 142:2319-2335, Jun 2019. URL: https://doi.org/10.1093/brain/awz175, doi:10.1093/brain/awz175. This article has 73 citations.

## Artifacts

- [Edison artifact artifact-00](Developmental_And_Epileptic_Encephalopathy_16-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 28 |
| Resolved | 28 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 2 |
| Terms named correctly | 1 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0014133` (4 mentions) - the report calls it "if available"; MONDO calls it **developmental and epileptic encephalopathy, 16**