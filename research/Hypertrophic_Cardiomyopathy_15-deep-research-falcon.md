---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-08T11:06:15.835824'
end_time: '2026-09-08T11:22:37.042774'
duration_seconds: 981.21
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Hypertrophic Cardiomyopathy 15
  mondo_id: MONDO:0013200
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 30
reference_validation:
  total_references: 6
  verified: 6
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 6
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 48
  verified: 48
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0013200
    reported_labels:
    - if available
    ontology_label: hypertrophic cardiomyopathy 15
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Hypertrophic_Cardiomyopathy_15-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypertrophic Cardiomyopathy 15
- **MONDO ID:** MONDO:0013200 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypertrophic Cardiomyopathy 15** covering all of the
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
- **Disease Name:** Hypertrophic Cardiomyopathy 15
- **MONDO ID:** MONDO:0013200 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Hypertrophic Cardiomyopathy 15** covering all of the
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


# Hypertrophic Cardiomyopathy 15 (HCM15): Comprehensive Disease-Characteristics Report

## Executive summary and evidence boundary

Hypertrophic cardiomyopathy 15 (HCM15) is a historically catalogued, extremely rare Mendelian hypertrophic-cardiomyopathy subtype attributed to heterozygous germline variants in **VCL**, which encodes vinculin and its muscle-specific splice isoform metavinculin. The supplied disease identifier is **MONDO:0013200**. Because disease numbering and gene–disease assertions can change between ontology releases, this identifier and the HCM15–VCL relationship should be checked against the current MONDO, OMIM, ClinGen, and ClinVar releases before production use. Open Targets supports a VCL–HCM association and points to human literature including PMIDs **16712796, 20052757, 21779496, 22826437, and 24937142**, but this is gene-level evidence rather than proof that every rare VCL variant causes HCM15. (OpenTargets Search: hypertrophic cardiomyopathy-VCL)

The central limitation is that published HCM15-specific human data are too sparse to estimate penetrance, age-specific onset, phenotype frequencies, incidence, prognosis, or treatment response. Consequently, this report distinguishes:

* **Subtype-specific evidence:** human VCL association and experimental Vcl biology.
* **Parent-disease evidence:** contemporary phenotype-defined HCM criteria, surveillance, prognosis, and treatment, which guide management but must not be encoded as VCL-specific outcomes.

| Domain | HCM15/VCL-specific evidence | General HCM evidence used for clinical context | Confidence / knowledge-base handling |
|---|---|---|---|
| Identity/genetics | HCM15 is catalogued as a rare Mendelian HCM subtype associated with heterozygous germline **VCL** variants; Open Targets links VCL to HCM using human genetic literature including PMIDs 16712796, 20052757, 21779496, 22826437, and 24937142. The submitted identifier is **MONDO:0013200**, but identifier/version consistency should be checked against the live MONDO and OMIM releases. (OpenTargets Search: hypertrophic cardiomyopathy-VCL) | Monogenic HCM is usually autosomal dominant, with variable penetrance and expressivity; identifiable pathogenic variants occur in roughly 30–60% of unselected HCM, predominantly in established sarcomeric genes. (verheyen2024austrianconsensusstatement pages 11-12, verheyen2024austrianconsensusstatement pages 9-11) | **Low–moderate subtype confidence.** Record VCL as the reported causal gene and inheritance as autosomal dominant, but retain provenance and current ClinGen/ClinVar classification. Do not infer penetrance, pathogenicity, or phenotype from gene-level association alone; distinguish P/LP variants from VUS explicitly. |
| Phenotype | Published VCL-associated human observations support a cardiomyopathy spectrum, but available evidence is too sparse to estimate HCM15-specific frequencies, typical onset, severity, obstruction rate, or extracardiac manifestations. (OpenTargets Search: hypertrophic cardiomyopathy-VCL) | HCM ranges from asymptomatic hypertrophy to dyspnea, chest pain, syncope, atrial or ventricular arrhythmia, heart failure, and sudden cardiac death. LV hypertrophy may be asymmetric, reverse-curvature, sigmoid, concentric, or apical; LVOTO/SAM can occur at rest or with provocation. (verheyen2024austrianconsensusstatement pages 11-12, verheyen2024austrianconsensusstatement pages 6-7) | **Low subtype confidence; high general-HCM confidence.** Encode observed features patient by patient when primary VCL case data are available. General HCM manifestations may define the diagnostic phenotype but **must not be stored as VCL-specific frequencies, onset distributions, or obligate features**. |
| Mechanism | Vinculin localizes to cardiomyocyte costameres and intercalated discs, linking actin to cell–matrix and cell–cell adhesion systems. Direct human variant-specific mechanisms remain incompletely established; disruption of force transmission, junctional stability, and mechanosensing is biologically plausible. (zemljicharpf2007cardiacmyocytespecificexcisionof pages 1-2, zemljicharpf2007cardiacmyocytespecificexcisionof pages 2-3) | Focal-adhesion mechanotransduction involves integrins, vinculin, FAK/Src, PI3K–AKT, and Wnt/β-catenin signaling; mechanical-load responses can promote hypertrophic growth. These pathways provide context, not proof of the causal route in HCM15. | **Moderate protein-function, low variant-mechanism confidence.** Annotate adhesion/mechanotransduction as supported VCL biology; label the route from a particular VCL allele to human hypertrophy as **inferred** unless demonstrated by segregation and variant-specific functional assays. |
| Epidemiology | No reliable HCM15-specific prevalence, incidence, carrier-frequency, founder-effect, sex-ratio, or geographic-distribution estimate was identified. | Phenotype-defined unexplained LV thickening affects approximately 0.16–0.23% of adults; including genotype-positive/phenotype-negative individuals may raise estimated HCM prevalence to about 0.6%. (verheyen2024austrianconsensusstatement pages 1-2) | **HCM15 epidemiology unavailable.** Store general HCM prevalence only at the parent-disease level. Never attribute the 0.16–0.23% or 0.6% estimates to VCL-associated HCM15. |
| Diagnosis | Molecular confirmation requires a **VCL** variant classified as pathogenic/likely pathogenic with appropriate phenotype, inheritance, segregation, and exclusion of alternative causes; a VCL VUS does not establish HCM15. | HCM is generally diagnosed by otherwise unexplained maximal LV wall thickness ≥15 mm, or ≥13 mm in a relative of an affected person or a carrier of a confirmed disease-causing variant. Evaluation uses pedigree, ECG, echocardiography, ambulatory ECG, CMR, exercise testing, and exclusion of hypertension, valvular disease, athlete’s heart, amyloidosis, and metabolic/storage phenocopies. (verheyen2024austrianconsensusstatement pages 11-12, verheyen2024austrianconsensusstatement pages 6-7, verheyen2024austrianconsensusstatement pages 1-2) | **High general diagnostic confidence; moderate subtype confidence.** Encode HCM phenotype and molecular diagnosis as separate assertions. Reassess VCL variants periodically; panel, exome, or genome findings require ACMG/AMP interpretation and phenotype correlation. |
| Treatment | No VCL-specific drug, gene therapy, RNA therapy, editing strategy, or genotype-guided treatment has demonstrated clinical efficacy. | Phenotype-directed HCM care includes β-blockers or non-dihydropyridine calcium-channel blockers, disopyramide in selected obstructive disease, myosin inhibition, septal reduction for refractory obstruction, AF anticoagulation, ICD-based SCD prevention, and advanced-heart-failure therapy. In EXPLORER-HCM, mavacamten achieved the primary endpoint in 37% versus 17% with placebo; in VALOR-HCM, 17.9% versus 76.8% met criteria for or underwent septal reduction at 16 weeks. (pagel2025advancesincardiovascular pages 5-6, seferovic2023stateoftheartdocumenton pages 11-12) | **High general-HCM, no subtype-specific efficacy evidence.** Treatments should be attached to the patient’s obstruction, arrhythmia, SCD-risk, or heart-failure phenotype—not to VCL genotype. Do not encode mavacamten response or procedural outcomes as HCM15-specific. |
| Prognosis | HCM15-specific survival, SCD rate, heart-failure progression, transplant risk, and quality-of-life trajectories are unknown; limited VCL reports cannot define penetrance or outcome distributions. | General HCM prognosis is heterogeneous. Risk assessment considers wall thickness, LVOT gradient, family history, unexplained syncope, nonsustained VT, LVEF, apical aneurysm, and fibrosis; LGE ≥15% of LV mass is an additional risk marker. A 2024 cohort found genotype-positive status alone did not independently predict mortality, heart-failure progression, or SCD. (verheyen2024austrianconsensusstatement pages 9-11, seferovic2023stateoftheartdocumenton pages 13-13) | **Insufficient subtype evidence.** Use validated clinical risk markers and longitudinal patient data. General HCM event rates, genotype-outcome estimates, and survival figures **must not be encoded as VCL/HCM15-specific prognosis**. |
| Models | Cardiomyocyte-specific **Vcl** knockout mice directly demonstrate loss-of-function consequences: abnormal intercalated discs, myofibril detachment, reduced cadherin/β1D-integrin, connexin-43 redistribution, conduction slowing, ventricular tachycardia, and sudden death; 49% died before about 3 months, while survivors developed DCM and died before 6 months. (zemljicharpf2007cardiacmyocytespecificexcisionof pages 8-11, zemljicharpf2007cardiacmyocytespecificexcisionof pages 11-12, zemljicharpf2007cardiacmyocytespecificexcisionof pages 1-2) | The model supports vinculin’s necessity for cardiac mechanical and electrical integrity but models near-complete cardiomyocyte loss and predominantly arrhythmic/DCM outcomes, not a specific heterozygous human HCM15 allele. | **High confidence for Vcl-loss biology; limited disease fidelity.** Record as a mechanistic VCL model, not a complete HCM15 phenocopy. Do not transfer mouse lethality, timing, sex effects, or DCM frequency to affected humans. |


*Table: This table separates VCL/HCM15-specific findings from parent-level HCM evidence used only for clinical context. It highlights which claims can be encoded directly and which must not be represented as VCL-specific frequencies, treatment responses, or outcomes.*

---

## 1. Disease information

### Definition

HCM15 is a proposed **autosomal-dominant, VCL-associated form of familial hypertrophic cardiomyopathy**. At the parent-disease level, HCM is defined by increased left-ventricular wall thickness that is not explained solely by loading conditions or another cardiac, systemic, metabolic, infiltrative, or storage disorder. Contemporary adult criteria are maximal end-diastolic LV wall thickness **≥15 mm**, or **≥13 mm** in a first-degree relative of an affected person or in a carrier of a confirmed disease-causing variant. (verheyen2024austrianconsensusstatement pages 6-7, verheyen2024austrianconsensusstatement pages 1-2)

### Identifiers and terminology

* **MONDO:** MONDO:0013200, as supplied; verify against the live release.
* **Preferred name:** hypertrophic cardiomyopathy 15.
* **Synonyms:** HCM15; familial hypertrophic cardiomyopathy 15; VCL-related hypertrophic cardiomyopathy; vinculin-related cardiomyopathy.
* **Parent disease:** hypertrophic cardiomyopathy, MONDO:0005045 in Open Targets. (OpenTargets Search: hypertrophic cardiomyopathy-VCL)
* **OMIM:** the subtype has historically been associated with the VCL locus; the exact current phenotype record should be confirmed directly in OMIM because numbered HCM assignments are periodically revised.
* **ICD-10-CM:** I42.1, obstructive HCM; I42.2, other HCM. These codes do not distinguish HCM15.
* **ICD-11:** cardiomyopathy hierarchy, hypertrophic-cardiomyopathy category; no VCL-specific code.
* **MeSH:** Cardiomyopathy, Hypertrophic.

This is an **aggregated disease-level synthesis**, not an individual EHR record. The foundational subtype evidence derives from small human genetic observations; modern diagnostic and therapeutic statements derive predominantly from aggregated HCM cohorts, trials, and guidelines.

---

## 2. Etiology

### Causal factor

The initiating lesion is a **heterozygous germline VCL variant** with sufficient pathogenic evidence. Vinculin is an actin-binding adhesion protein concentrated at cardiomyocyte costameres and intercalated discs; metavinculin is a muscle-enriched alternatively spliced isoform. VCL links the actin cytoskeleton and contractile apparatus to cell–matrix and cell–cell adhesion systems. Complete cardiomyocyte loss in mice demonstrates that this function is essential for junctional and electrical integrity. (zemljicharpf2007cardiacmyocytespecificexcisionof pages 1-2, zemljicharpf2007cardiacmyocytespecificexcisionof pages 2-3)

A rare VCL variant should not automatically be considered causal. A defensible molecular diagnosis requires ACMG/AMP classification, phenotype concordance, segregation, population rarity, and ideally variant-specific functional evidence. A **VUS does not establish HCM15**.

### Risk factors

**Genetic:**

* A pathogenic/likely pathogenic VCL allele is the principal proposed risk factor.
* Autosomal-dominant transmission implies a **50% probability of allele transmission**, not 50% certainty of clinical disease, because penetrance is likely incomplete and age dependent.
* Family history of HCM or sudden cardiac death increases clinical suspicion, but absence of family history does not exclude disease because of reduced penetrance or a de novo variant. General monogenic HCM shows variable penetrance and expressivity. (verheyen2024austrianconsensusstatement pages 11-12, verheyen2024austrianconsensusstatement pages 9-11)
* No validated HCM15-specific modifier gene, polygenic score, founder allele, carrier frequency, or ancestry-specific susceptibility estimate is available.

**Environmental and physiologic modifiers:**

Hypertension, obesity, valvular disease, ischemia, pregnancy-related hemodynamic loading, and intense exercise may alter hypertrophy, symptoms, or arrhythmic burden in HCM generally, but none is established as a cause of VCL-HCM15. Hypertension and athlete’s heart are especially important diagnostic confounders. In mild-to-moderate hypertension, LV thickness ≥15 mm is uncommon, reported in under 5% in the cited consensus. (verheyen2024austrianconsensusstatement pages 11-12)

### Protective factors and gene–environment interaction

No replicated **VCL-specific protective allele**, diet, medication, or exposure is known to prevent disease penetrance. Control of hypertension and other cardiovascular comorbidities, avoidance of dehydration in obstructive physiology, and individualized exercise are prudent tertiary-risk measures rather than primary prevention of the mutation.

Vinculin is load responsive: mechanical stress alters adhesion-complex recruitment. Therefore, a VCL defect plausibly interacts with hemodynamic load through impaired mechanotransduction, but a quantitative human VCL × environment interaction has not been demonstrated. (zemljicharpf2007cardiacmyocytespecificexcisionof pages 2-3)

---

## 3. Phenotypes

Published evidence does not support HCM15-specific percentages. The following are expected **HCM phenotypes**, to be recorded as observed rather than assumed in a VCL carrier.

| Phenotype | Type/course and impact | Suggested HPO term |
|---|---|---|
| Unexplained LV hypertrophy, often asymmetric septal but potentially concentric or apical | Clinical/imaging sign; may be absent early and develop with age; severity variable | **HP:0001712** Left ventricular hypertrophy; **HP:0001670** Asymmetric septal hypertrophy |
| LV outflow-tract obstruction and systolic anterior motion | Dynamic sign, resting or provoked; obstruction/SAM can occur in up to 75% of general HCM but is not HCM15-specific | **HP:0001685** Dynamic LV outflow obstruction; **HP:0004382** Mitral-valve systolic anterior motion |
| Diastolic dysfunction and left-atrial enlargement | Progressive or load dependent; contributes to exertional dyspnea and AF | **HP:0005117** Elevated LV filling pressure; **HP:0031640** Left-atrial enlargement |
| Exertional dyspnea, exercise intolerance, fatigue | Symptoms ranging from mild to disabling; reduce work, sport, and daily activity | **HP:0002094** Dyspnea; **HP:0003546** Exercise intolerance; **HP:0012378** Fatigue |
| Chest pain/ischemia | Episodic; may reflect microvascular ischemia rather than epicardial coronary disease | **HP:0100749** Chest pain; **HP:0001677** Coronary microvascular dysfunction where supported |
| Palpitations, AF, nonsustained or sustained VT | Episodic; AF can worsen filling and thromboembolic risk; ventricular arrhythmia can cause SCD | **HP:0001962** Palpitations; **HP:0005110** Atrial fibrillation; **HP:0004756** Ventricular tachycardia |
| Presyncope/syncope | Episodic; exertional or unexplained syncope is prognostically important | **HP:0001279** Syncope |
| Myocardial fibrosis/disarray | Histologic/CMR abnormality; LGE is present in roughly 50–60% of general HCM | **HP:0031294** Myocardial fibrosis |
| Heart failure, rarely end-stage systolic dysfunction | Chronic progressive phenotype; may remain preserved-EF or evolve to LVEF <50% | **HP:0001635** Congestive heart failure; **HP:0001723** Restrictive cardiomyopathy phenotype when documented |
| Sudden cardiac death/cardiac arrest | Rare but severe outcome, particularly relevant in younger patients | **HP:0001645** Sudden cardiac death; **HP:0001695** Cardiac arrest |

HCM quality-of-life impairment is driven by dyspnea, fatigue, exercise limitation, anxiety about SCD, medication effects, and activity restrictions. The 2024 Austrian consensus states that HCM can cause a “substantial reduction in quality of life,” but no HCM15-specific EQ-5D, SF-36, KCCQ, or HCMSQ data exist. (verheyen2024austrianconsensusstatement pages 1-2)

---

## 4. Genetic and molecular information

### Causal gene

* **Gene:** VCL, vinculin.
* **Ensembl:** ENSG00000035403. (OpenTargets Search: hypertrophic cardiomyopathy-VCL)
* **Gene product:** ubiquitous vinculin and muscle-specific metavinculin.
* **Origin:** germline for inherited HCM15; somatic VCL mutation is not an established cause.
* **Inheritance:** proposed autosomal dominant.

### Pathogenic variants

The accessible evidence did not provide a sufficiently verified, current list of HCM15 variants with transcript, HGVS expression, ClinVar assertion, gnomAD frequency, segregation, and functional status. A knowledge-base implementation should therefore import variants directly from current ClinVar/ClinGen and retain:

1. reference transcript and genome build;
2. genomic, coding, and protein HGVS;
3. submitter/date and review status;
4. ACMG/AMP class;
5. gnomAD ancestry-specific frequency;
6. segregation and phenotype;
7. functional-assay type;
8. whether vinculin, metavinculin, or both are affected.

Reported VCL cardiomyopathy alleles have included missense and splice/isoform-affecting variants, but the disease spectrum includes both hypertrophic and dilated cardiomyopathy. Thus, variant-specific evidence is essential. Open Targets’ supporting literature includes PMIDs 16712796, 20052757, 21779496, 22826437, and 24937142. (OpenTargets Search: hypertrophic cardiomyopathy-VCL)

### Functional consequence

Possible mechanisms include loss of function, altered actin binding, disturbed head–tail autoinhibition, defective recruitment to costameres/intercalated discs, or altered mechanosensing. Complete Vcl deletion is clearly loss of function, but it must not be assumed that every human heterozygous missense allele acts identically.

### Modifiers, epigenetics, and chromosomal abnormalities

* **Modifier genes:** none validated specifically for HCM15.
* **Epigenetics:** no reproducible VCL-HCM15 methylation, chromatin, or histone signature identified.
* **Structural variants:** no recurrent HCM15-associated deletion, duplication, inversion, or translocation established.
* **Anticipation:** not established; VCL disease is not a repeat-expansion disorder.
* **Mosaicism:** theoretically possible but not quantified.

---

## 5. Environmental information

No toxin, pollutant, radiation exposure, occupation, or infectious agent is known to cause HCM15. Viral myocarditis and other acquired myocardial diseases can mimic or aggravate cardiomyopathy but are not defining etiologies. Smoking, excess alcohol, obesity, hypertension, sleep apnea, and sedentary behavior should be managed for overall cardiovascular health; none has demonstrated VCL-specific penetrance modification.

Lifestyle advice should be phenotype based. Low-to-moderate recreational exercise is generally safe and beneficial. High-intensity sport should be assessed through shared decision-making, particularly when there is prior cardiac arrest, unexplained syncope, exercise-induced arrhythmia, significant LVOTO, or elevated SCD risk. (verheyen2024austrianconsensusstatement pages 19-21)

---

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A pathogenic heterozygous **VCL** lesion **leads to** deficient or abnormal vinculin/metavinculin localization or function at cardiomyocyte costameres and intercalated discs; this first step is established for Vcl loss but remains variant-specific in humans.
2. Abnormal vinculin **leads to** impaired linkage of actin/myofibrils to integrin-containing cell–matrix adhesions and cadherin-containing cell–cell junctions.
3. Impaired adhesion **results in** defective force transmission, mechanosensing, and intercalated-disc stability; conditional Vcl-null mouse hearts show reduced cadherin and β1D-integrin, myofibril detachment, and abnormal discs. (zemljicharpf2007cardiacmyocytespecificexcisionof pages 8-11, zemljicharpf2007cardiacmyocytespecificexcisionof pages 11-12)
4. Junctional disruption **leads to** connexin-43 redistribution, heterogeneous coupling, local conduction slowing, ventricular ectopy, polymorphic VT, and sudden death in the knockout model. (zemljicharpf2007cardiacmyocytespecificexcisionof pages 8-11, zemljicharpf2007cardiacmyocytespecificexcisionof pages 12-14)
5. **Mechanical branch—partly inferred for human HCM15:** chronic force-transmission inefficiency and load-responsive focal-adhesion signaling **lead to** compensatory cardiomyocyte hypertrophy, energetic stress, and maladaptive remodeling.
6. **Structural branch:** repeated mechanical injury **results in** myocyte loss, replacement fibrosis, and altered ventricular compliance.
7. Hypertrophy, disarray, fibrosis, and small-vessel/energetic dysfunction **lead to** diastolic dysfunction, microvascular ischemia, dynamic LVOTO, atrial enlargement, and heart-failure symptoms.
8. Fibrosis plus electrical uncoupling **results in** atrial and ventricular arrhythmia and creates the substrate for SCD.
9. In advanced disease, progressive myocyte loss and remodeling **may lead to** systolic dysfunction, dilation, or a restrictive end-stage phenotype; the direct Vcl-null model predominantly evolves toward DCM rather than faithfully reproducing heterozygous HCM15.

### Molecular and cellular detail

Vinculin occupies **costameres**, which align with Z-discs and transmit sarcomeric force to extracellular matrix, and **intercalated discs**, which provide end-to-end mechanical and electrical coupling. Relevant signaling context includes integrin–FAK/Src, PI3K–AKT, Wnt/β-catenin, cytoskeletal tension, and hypertrophic gene programs. These pathways are biologically relevant to focal-adhesion mechanotransduction but have not been demonstrated as a complete allele-to-phenotype chain in HCM15.

In conditional cardiomyocyte Vcl-knockout mice, structural abnormalities preceded overt dysfunction: serrated, less electron-dense intercalated discs, separation of myofibrils, disorganized mitochondria, reduced cadherin/β1D-integrin, and lateralized connexin-43 were observed. Telemetry showed heart block and polymorphic VT; 86% of isolated knockout hearts had spontaneous ventricular ectopy. (zemljicharpf2007cardiacmyocytespecificexcisionof pages 8-11, zemljicharpf2007cardiacmyocytespecificexcisionof pages 11-12)

**Suggested GO biological processes:**

* GO:0007155 cell adhesion
* GO:0007160 cell–matrix adhesion
* GO:0007156 homophilic cell adhesion
* GO:0055002 striated-muscle-cell development
* GO:0007512 adult heart development
* GO:0006936 muscle contraction
* GO:0003015 heart process
* GO:0006979 response to oxidative stress
* GO:0060048 cardiac muscle contraction
* GO:0007507 heart development
* GO:0035994 response to muscle stretch

**Suggested GO cellular components:** focal adhesion (GO:0005925), cell–substrate junction (GO:0030055), adherens junction (GO:0005912), intercalated disc (GO:0014704), costamere (GO:0043034), actin cytoskeleton (GO:0015629), Z disc (GO:0030018), mitochondrion (GO:0005739).

**Suggested Cell Ontology terms:** cardiomyocyte (**CL:0000746**), ventricular cardiomyocyte (**CL:0002129**), cardiac fibroblast, vascular endothelial cell (**CL:0000115**), vascular smooth-muscle cell (**CL:0000359**), cardiac conduction cell where appropriate.

### Molecular profiling and advanced technologies

No HCM15-specific bulk transcriptomic, single-cell, spatial, proteomic, metabolomic, lipidomic, methylomic, or CRISPR-screen signature was identified. A 2023 spatial multiomic atlas mapped cellular niches across eight normal human heart regions, and a 2024 review emphasized that single-cell/spatial technologies now resolve cardiac cellular diversity, but these resources do not establish a VCL-HCM15 molecular signature. Therefore, such evidence should be treated as enabling context, not disease-specific annotation.

---

## 7. Anatomical structures affected

**Primary organ:** heart, principally the left-ventricular myocardium and interventricular septum.

**Structures:**

* left ventricle — **UBERON:0002084**;
* interventricular septum — **UBERON:0002094**;
* myocardium — **UBERON:0002349**;
* papillary muscles and mitral-valve apparatus when SAM/LVOTO is present;
* left atrium secondarily from elevated filling pressure;
* right ventricle occasionally through hypertrophy, loading, or advanced disease.

**Tissue/cell level:** striated cardiac muscle, ventricular cardiomyocytes, interstitial fibroblasts, intramural coronary microvasculature, conduction-system cells.

**Subcellular level:** intercalated discs, fascia adherens, costameres, focal adhesions, actin cytoskeleton, sarcomere/Z-disc interfaces, gap junctions, and secondarily mitochondria. The Vcl-knockout study directly showed abnormal intercalated discs, myofibril detachment, connexin-43 redistribution, and mitochondrial disorganization. (zemljicharpf2007cardiacmyocytespecificexcisionof pages 8-11, zemljicharpf2007cardiacmyocytespecificexcisionof pages 11-12)

HCM is usually diffuse or regionally asymmetric rather than unilateral; lateralization is not applicable.

---

## 8. Temporal development

HCM15-specific onset is unknown. General inherited HCM may be detectable in childhood, adolescence, adulthood, or late life; onset is often insidious and penetrance is age dependent. A genotype-positive person may remain phenotype negative for years.

A practical temporal model is:

1. **Preclinical:** pathogenic-variant carrier, normal wall thickness; subtle ECG, strain, crypt, or CMR abnormalities may occur.
2. **Early phenotype:** localized or mild LV hypertrophy, preserved LVEF, few symptoms.
3. **Established HCM:** greater hypertrophy with diastolic dysfunction, possible LVOTO/SAM, symptoms, AF or ventricular ectopy.
4. **Advanced disease:** fibrosis, atrial enlargement, recurrent arrhythmia, heart failure, apical aneurysm, or LVEF <50%.
5. **End stage:** restrictive or dilated/systolic phenotype, transplantation consideration.

The course is chronic and lifelong but highly variable, not classically relapsing–remitting. There is no established spontaneous molecular remission. Obstruction and symptoms can improve with treatment.

Genotype-positive/phenotype-negative children and adolescents should generally undergo ECG and imaging every **1–2 years**, and adults every **3–5 years**. Stable phenotype-positive patients generally receive clinical review, ECG/Holter, and echocardiography every **1–2 years**, with earlier reassessment after symptom change. (verheyen2024austrianconsensusstatement pages 21-22, verheyen2024austrianconsensusstatement pages 19-21)

---

## 9. Inheritance and population

### Inheritance

* **Pattern:** autosomal dominant.
* **Transmission risk:** 50% per pregnancy from a heterozygous parent.
* **Penetrance:** insufficiently characterized for VCL; likely incomplete and age dependent by analogy with inherited HCM.
* **Expressivity:** variable; VCL variation has been associated with a cardiomyopathy spectrum rather than one invariant morphology.
* **Anticipation:** not established.
* **Germline mosaicism:** possible in principle, unquantified.
* **Consanguinity:** not expected to be a principal factor in dominant HCM15.
* **Founder effects/carrier frequency:** unknown.

### Epidemiology

No HCM15-specific prevalence or incidence estimate exists. Parent-level phenotype-defined unexplained LV thickening affects approximately **0.16–0.23%** of adults; inclusion of genotype-positive/phenotype-negative people may raise general HCM prevalence toward **0.6%**. These values must not be assigned to HCM15. (verheyen2024austrianconsensusstatement pages 1-2)

No reliable HCM15-specific sex ratio, age distribution, ancestry enrichment, or geographic clustering is known. General cohorts can show referral-related male predominance, which should not be interpreted as Mendelian sex limitation.

---

## 10. Diagnostics

### Clinical diagnostic pathway

1. Obtain symptoms, blood pressure, loading conditions, medications, and a **three-generation pedigree** including HCM, heart failure, unexplained death, and SCD.
2. Perform 12-lead ECG, transthoracic echocardiography, and 24–48-hour ambulatory ECG. Longer monitoring is appropriate for intermittent palpitations, presyncope, or suspected AF/VT. (verheyen2024austrianconsensusstatement pages 6-7)
3. Measure maximal LV thickness in all segments and assess systolic/diastolic function, left-atrial size, mitral anatomy, SAM, and resting/provoked LVOT gradient.
4. Use Valsalva, standing, squat-to-stand, or exercise provocation when resting obstruction is absent; dobutamine stress is not recommended for this purpose. (verheyen2024austrianconsensusstatement pages 6-7)
5. Obtain CMR when echocardiography is incomplete or to define morphology, apical disease/aneurysm, crypts, LVEF, and fibrosis by LGE/T1/ECV.
6. Conduct exercise testing or cardiopulmonary exercise testing for latent obstruction, symptoms, blood-pressure response, functional capacity, and advanced-heart-failure assessment.
7. Exclude phenocopies and alternative loading causes.
8. Offer genetic counselling and a curated cardiomyopathy panel. Molecular HCM15 requires a P/LP **VCL** variant plus a compatible phenotype or robust familial evidence.

CMR detects focal fibrosis; LGE is reported in approximately 50–60% of general HCM, and involvement of **≥15% of LV mass** is an additional SCD-risk marker. CMR can be repeated every **3–5 years** when useful for risk reassessment. (verheyen2024austrianconsensusstatement pages 9-11, verheyen2024austrianconsensusstatement pages 21-22)

### Laboratory and biomarkers

No diagnostic enzyme assay or VCL-specific circulating biomarker exists. Useful phenotype/severity biomarkers include NT-proBNP/BNP and high-sensitivity troponin, but neither establishes HCM15. Baseline renal, liver, thyroid, iron, CK, and metabolic testing is selected according to differential diagnosis and treatment.

### Genetic testing

* **Preferred first line:** phenotype-focused multigene cardiomyopathy panel containing validated HCM genes, phenocopy genes, and VCL with deletion/duplication analysis where validated.
* **Single-gene VCL testing:** reasonable when a familial P/LP VCL variant is already known.
* **WES/WGS:** useful after a negative panel in strongly familial disease, for structural/noncoding variants, blended phenotypes, or research reanalysis; interpretation remains the limiting step.
* **CMA/karyotype/FISH:** not routine for isolated HCM; use when syndromic features suggest a chromosomal disorder.
* **mtDNA/repeat-expansion tests:** not routine unless the phenotype suggests mitochondrial or repeat-expansion disease.
* **RNA sequencing:** potentially resolves splice variants but is not a standard HCM15 diagnostic and cardiac tissue is rarely available.

Cascade testing should target the known familial P/LP variant. Genotype-negative relatives can usually be released from serial familial surveillance when the familial variant is definitively causal; VUS-based predictive testing should not be used for reassurance or irreversible decisions.

### Differential diagnosis

Hypertensive remodeling, aortic stenosis, athlete’s heart, transthyretin or AL amyloidosis, Fabry disease, Danon disease, Pompe disease, PRKAG2 glycogenosis, mitochondrial disease, Noonan/RASopathy, Friedreich ataxia, and cardiac tumors or subaortic membrane should be considered. Morphology, extracardiac features, ECG voltage, strain, CMR, biomarkers, and molecular testing distinguish these entities. (verheyen2024austrianconsensusstatement pages 11-12, verheyen2024austrianconsensusstatement pages 6-7)

---

## 11. Outcome and prognosis

There are no valid HCM15-specific 5- or 10-year survival estimates, annual SCD rate, transplant rate, or life-expectancy figures. Prognosis must be individualized from phenotype rather than VCL status alone.

General adverse outcomes include AF and stroke, ventricular arrhythmia/SCD, progressive heart failure, apical aneurysm/thrombus, end-stage systolic dysfunction, and need for septal reduction or transplantation. Apical aneurysm occurs in approximately 2% of general HCM and was associated in cited data with annual SCD and thromboembolism rates of **4.7%** and **1.1%**, respectively. (verheyen2024austrianconsensusstatement pages 9-11)

SCD assessment includes age, maximal wall thickness, LVOT gradient, left-atrial diameter, family history, unexplained syncope, and nonsustained VT. Additional markers include LVEF <50%, apical aneurysm, extensive LGE, and selected pathogenic sarcomeric variants. The ESC framework considers an ICD at a 5-year risk **≥6%** and may consider it at **4–<6%**; the AHA/ACC approach emphasizes major risk markers such as prior arrest/sustained VT, early familial SCD, wall thickness ≥30 mm, recent unexplained syncope, apical aneurysm, and LVEF <50%. (seferovic2023stateoftheartdocumenton pages 13-13)

A 2024 German cohort of 283 adults observed 14 SCD-equivalent events over median 5.77 years; adding genetic status improved model AUC to 0.76, but this was not VCL specific. Conversely, a separate 2024 international cohort of 1,468 patients found genotype-positive status was not independently predictive of mortality, heart-failure progression, or SCD. Genotype alone should therefore not dictate prognosis.

---

## 12. Treatment

No VCL-specific approved therapy or validated pharmacogenomic algorithm exists. Management is driven by obstruction, symptoms, arrhythmia, heart-failure state, and SCD risk.

### Pharmacotherapy

* **Nonvasodilating β-blocker:** first-line symptom/gradient control in obstructive HCM; NCIT concept: beta-adrenergic blocker therapy.
* **Verapamil or diltiazem:** alternatives when β-blockers are ineffective or not tolerated, with caution in severe obstruction/hypotension; NCIT: calcium-channel-blocker therapy.
* **Disopyramide:** negative inotrope added in selected symptomatic obstruction, with QT and anticholinergic monitoring; NCIT: antiarrhythmic-agent therapy.
* **Mavacamten:** selective allosteric cardiac-myosin ATPase inhibitor for eligible symptomatic obstructive HCM; reduces excessive actin–myosin cross-bridging. NCIT: cardiac myosin inhibitor therapy.
* **AF:** rate/rhythm management and anticoagulation because HCM-associated AF has clinically important embolic risk; NCIT: anticoagulant therapy/catheter ablation as applicable.
* **Advanced LVEF <50%:** guideline-directed reduced-EF heart-failure therapy; discontinue negative inotropes when inappropriate and assess for CRT/transplantation.

In EXPLORER-HCM, **37%** receiving mavacamten versus **17%** receiving placebo met the primary functional endpoint; 65% versus 31% improved at least one NYHA class, and postexercise LVOT gradient fell by 36 mmHg. Transient LVEF <50% occurred in 6% and resolved after withdrawal. (seferovic2023stateoftheartdocumenton pages 11-12)

In VALOR-HCM, **17.9%** of mavacamten-treated versus **76.8%** of placebo-treated patients met criteria for or underwent septal reduction at 16 weeks. These are general obstructive-HCM data, not evidence of VCL-specific response. (pagel2025advancesincardiovascular pages 5-6)

Mavacamten requires serial echocardiographic LVEF/gradient surveillance and careful review of CYP2C19/CYP3A4 interactions because excessive myosin inhibition can cause systolic dysfunction.

### Surgical and interventional treatment

* **Surgical septal myectomy:** preferred at experienced centers for severe, drug-refractory symptomatic LVOTO, especially with complex mitral/subvalvular anatomy; NCIT: ventricular septal myectomy.
* **Alcohol septal ablation:** catheter alternative in selected adults with suitable septal-perforator anatomy or elevated surgical risk; NCIT: alcohol septal ablation.
* **ICD:** secondary prevention after arrest/sustained VT and primary prevention after individualized risk assessment; NCIT: implantable cardioverter-defibrillator placement.
* **Pacemaker/CRT, AF ablation, transplantation:** phenotype-specific indications.

### Exercise and rehabilitation

A 2023 randomized trial enrolled 15 completers. Five months of moderate- or progressive high-intensity training improved peak VO₂ by **1.3 mL/kg/min** overall (P=0.009), without serious arrhythmia or adverse cardiac events, although it was underpowered for safety. A 2024 systematic review of five studies and 235 participants reported functional-capacity improvements up to 46% and no sustained tachyarrhythmia, ICD discharge, or SCD during the studied programs. These data support supervised, individualized rehabilitation rather than universal inactivity.

### Experimental therapy and trials

Gene replacement, allele-specific silencing, base/prime editing, and RNA therapies are preclinical concepts for inherited HCM; none has demonstrated benefit for VCL-HCM15. Current HCM implementation studies include the multinational real-world **COLLIGO-HCM, NCT06372457** (331 participants) and phase-3 mavacamten studies such as **NCT05414175**. Aficamten trials are active across obstructive and nonobstructive phenotypes. Trial eligibility is phenotype based, not VCL specific.

---

## 13. Prevention

### Primary prevention

The germline variant cannot currently be prevented pharmacologically. Reproductive options after identification of a familial P/LP variant include genetic counselling, prenatal diagnosis, and preimplantation genetic testing for monogenic disease. These require discussion of uncertain penetrance and variable severity.

### Secondary prevention

* Cascade genetic testing and clinical screening of first-degree relatives.
* ECG and imaging every 1–2 years in genotype-positive children/adolescents and every 3–5 years in genotype-positive adults without phenotype. (verheyen2024austrianconsensusstatement pages 21-22)
* Prompt assessment of exertional syncope, palpitations, chest pain, or family SCD.
* Periodic Holter monitoring, exercise testing, and CMR-based fibrosis/morphology assessment.

### Tertiary prevention

* Treat obstruction, AF, hypertension, and heart failure.
* Anticoagulate clinically documented AF according to HCM recommendations.
* Use an ICD for secondary prevention and selected high-risk primary prevention.
* Maintain hydration and avoid unmonitored drugs that markedly reduce preload/afterload in severe obstruction.
* Encourage individualized low-to-moderate exercise and shared decisions regarding vigorous sport. (verheyen2024austrianconsensusstatement pages 19-21)

Vaccination has no disease-specific preventive role, although routine immunization reduces general infectious risk. Population newborn screening is not recommended because HCM15 is exceptionally rare and no validated biochemical marker exists.

---

## 14. Other species and natural disease

* **Human:** *Homo sapiens*, NCBI Taxonomy **9606**.
* **Mouse model species:** *Mus musculus*, NCBI Taxonomy **10090**; orthologue **Vcl**.

Naturally occurring HCM is recognized in cats and occurs in other animals, but no well-established naturally occurring veterinary disease was identified that is specifically caused by an orthologous VCL allele and faithfully corresponds to human HCM15. Accordingly, cat HCM should not be annotated automatically as VCL-HCM15. No zoonotic or transmissible potential exists.

Vinculin’s adhesion and mechanotransduction functions are evolutionarily conserved, supporting comparative study. Species differences in heart rate, loading, isoform expression, and remodeling limit direct translation.

---

## 15. Model organisms and experimental systems

### Conditional cardiomyocyte Vcl-knockout mouse

The strongest direct model is the ventricular-cardiomyocyte-specific **Vcl** knockout created by Cre-mediated exon-3 excision. Vinculin/metavinculin were lost from cardiomyocytes while remaining in nonmyocytes and vessels. Before overt physiological dysfunction, animals developed abnormal intercalated discs, detachment of myofibrils, mitochondrial disorganization, reduced cadherin and β1D-integrin, and connexin-43 redistribution. Electrical mapping showed irregular wavefronts and local conduction slowing; telemetry documented heart block and polymorphic VT. (zemljicharpf2007cardiacmyocytespecificexcisionof pages 8-11, zemljicharpf2007cardiacmyocytespecificexcisionof pages 11-12, zemljicharpf2007cardiacmyocytespecificexcisionof pages 3-4)

The abstract-level result is especially informative: **“49% died suddenly before 3 months, despite preserved contractile function”**; surviving animals subsequently developed DCM and died before six months. At 14 weeks, male survival was 51% and female survival 71%; no males survived beyond 32 weeks. (zemljicharpf2007cardiacmyocytespecificexcisionof pages 1-2, zemljicharpf2007cardiacmyocytespecificexcisionof pages 7-8)

**Recapitulated features:** cardiomyocyte junctional disease, conduction defects, ventricular arrhythmia, sudden death, early mild hypertrophy, fibrosis, and progressive cardiomyopathy.

**Limitations:** near-complete cardiomyocyte knockout is more severe than a heterozygous human missense allele; the dominant late phenotype is DCM, not isolated HCM; mouse timing and lethality cannot be transferred to humans.

**Citation:** Zemljic-Harpf et al., *Molecular and Cellular Biology*, November 2007; DOI: [10.1128/MCB.00728-07](https://doi.org/10.1128/mcb.00728-07). (zemljicharpf2007cardiacmyocytespecificexcisionof pages 8-11, zemljicharpf2007cardiacmyocytespecificexcisionof pages 1-2)

### Other model systems

Human iPSC-derived cardiomyocytes carrying rigorously classified VCL variants, engineered heart tissues, and isogenic CRISPR-corrected controls would be the most informative future systems for variant-specific contractility, adhesion, conduction, and mechanoload studies. No sufficiently validated HCM15-specific iPSC, organoid, zebrafish, Drosophila, or large-animal model was identified in the retrieved evidence.

---

## Knowledge-base recommendations

1. Store **HCM15–VCL** as a historically reported gene–disease assertion with provenance and periodic re-evaluation, not as an unconditional fact for every VCL variant.
2. Separate `genotype`, `HCM phenotype`, and `molecular diagnosis` fields.
3. Do not assign general-HCM phenotype frequencies, prevalence, prognosis, or mavacamten response to HCM15.
4. Encode mechanistic steps as **demonstrated in Vcl-loss mouse** versus **inferred in heterozygous human HCM15**.
5. Require P/LP status for cascade testing; retain VUS as non-diagnostic.
6. Mark HCM15-specific penetrance, incidence, sex ratio, carrier frequency, protective factors, omics signatures, natural veterinary disease, and treatment response as **not currently available**.

## Key recent and foundational sources

* Verheyen N, et al. “Austrian consensus statement on the diagnosis and management of hypertrophic cardiomyopathy.” Published October 2024. DOI/URL: [10.1007/s00508-024-02442-1](https://doi.org/10.1007/s00508-024-02442-1). (verheyen2024austrianconsensusstatement pages 11-12, verheyen2024austrianconsensusstatement pages 6-7, verheyen2024austrianconsensusstatement pages 1-2)
* Seferović PM, et al. “State-of-the-Art Document on Optimal Contemporary Management of Cardiomyopathies.” Published September 2023. DOI/URL: [10.1002/ejhf.2979](https://doi.org/10.1002/ejhf.2979). (seferovic2023stateoftheartdocumenton pages 11-12, seferovic2023stateoftheartdocumenton pages 13-13)
* MacNamara JP, et al. Randomized moderate- versus high-intensity exercise trial in HCM. Published October 2023. DOI/URL: [10.1161/JAHA.123.031399](https://doi.org/10.1161/JAHA.123.031399).
* Braunwald E, et al. “Mavacamten: a first-in-class myosin inhibitor for obstructive hypertrophic cardiomyopathy.” Published October 2023. DOI/URL: [10.1093/eurheartj/ehad637](https://doi.org/10.1093/eurheartj/ehad637).
* Zemljic-Harpf AE, et al. “Cardiac-Myocyte-Specific Excision of the Vinculin Gene Disrupts Cellular Junctions, Causing Sudden Death or Dilated Cardiomyopathy.” Published November 2007. DOI/URL: [10.1128/MCB.00728-07](https://doi.org/10.1128/mcb.00728-07). (zemljicharpf2007cardiacmyocytespecificexcisionof pages 8-11, zemljicharpf2007cardiacmyocytespecificexcisionof pages 1-2)

Overall, HCM15 is best treated as a **rare, incompletely validated VCL-associated HCM entity** embedded within the broader clinical HCM framework. The most secure biology concerns vinculin’s role in cardiomyocyte adhesion, force transmission, intercalated-disc integrity, and conduction; the least secure domains are variant-level causality, penetrance, epidemiology, and genotype-specific therapeutic response.

References

1. (OpenTargets Search: hypertrophic cardiomyopathy-VCL): Open Targets Query (hypertrophic cardiomyopathy-VCL, 7 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (verheyen2024austrianconsensusstatement pages 11-12): Nicolas Verheyen, Johannes Auer, Nikolaos Bonaros, Tamara Buchacher, Daniel Dalos, Michael Grimm, Agnes Mayr, Anna Rab, Sebastian Reinstadler, Daniel Scherr, Gabor G Toth, Thomas Weber, David K. Zach, Marc-Michael Zaruba, Daniel Zimpfer, Peter P Rainer, and Gerhard Pölzl. Austrian consensus statement on the diagnosis and management of hypertrophic cardiomyopathy. Wiener Klinische Wochenschrift, 136:571-597, Oct 2024. URL: https://doi.org/10.1007/s00508-024-02442-1, doi:10.1007/s00508-024-02442-1. This article has 6 citations and is from a peer-reviewed journal.

3. (verheyen2024austrianconsensusstatement pages 9-11): Nicolas Verheyen, Johannes Auer, Nikolaos Bonaros, Tamara Buchacher, Daniel Dalos, Michael Grimm, Agnes Mayr, Anna Rab, Sebastian Reinstadler, Daniel Scherr, Gabor G Toth, Thomas Weber, David K. Zach, Marc-Michael Zaruba, Daniel Zimpfer, Peter P Rainer, and Gerhard Pölzl. Austrian consensus statement on the diagnosis and management of hypertrophic cardiomyopathy. Wiener Klinische Wochenschrift, 136:571-597, Oct 2024. URL: https://doi.org/10.1007/s00508-024-02442-1, doi:10.1007/s00508-024-02442-1. This article has 6 citations and is from a peer-reviewed journal.

4. (verheyen2024austrianconsensusstatement pages 6-7): Nicolas Verheyen, Johannes Auer, Nikolaos Bonaros, Tamara Buchacher, Daniel Dalos, Michael Grimm, Agnes Mayr, Anna Rab, Sebastian Reinstadler, Daniel Scherr, Gabor G Toth, Thomas Weber, David K. Zach, Marc-Michael Zaruba, Daniel Zimpfer, Peter P Rainer, and Gerhard Pölzl. Austrian consensus statement on the diagnosis and management of hypertrophic cardiomyopathy. Wiener Klinische Wochenschrift, 136:571-597, Oct 2024. URL: https://doi.org/10.1007/s00508-024-02442-1, doi:10.1007/s00508-024-02442-1. This article has 6 citations and is from a peer-reviewed journal.

5. (zemljicharpf2007cardiacmyocytespecificexcisionof pages 1-2): Alice E. Zemljic-Harpf, Joel C. Miller, Scott A. Henderson, Adam T. Wright, Ana Maria Manso, Laila Elsherif, Nancy D. Dalton, Andrea K. Thor, Guy A. Perkins, Andrew D. McCulloch, and Robert S. Ross. Cardiac-myocyte-specific excision of the vinculin gene disrupts cellular junctions, causing sudden death or dilated cardiomyopathy. Molecular and Cellular Biology, 27:7522-7537, Nov 2007. URL: https://doi.org/10.1128/mcb.00728-07, doi:10.1128/mcb.00728-07. This article has 245 citations and is from a domain leading peer-reviewed journal.

6. (zemljicharpf2007cardiacmyocytespecificexcisionof pages 2-3): Alice E. Zemljic-Harpf, Joel C. Miller, Scott A. Henderson, Adam T. Wright, Ana Maria Manso, Laila Elsherif, Nancy D. Dalton, Andrea K. Thor, Guy A. Perkins, Andrew D. McCulloch, and Robert S. Ross. Cardiac-myocyte-specific excision of the vinculin gene disrupts cellular junctions, causing sudden death or dilated cardiomyopathy. Molecular and Cellular Biology, 27:7522-7537, Nov 2007. URL: https://doi.org/10.1128/mcb.00728-07, doi:10.1128/mcb.00728-07. This article has 245 citations and is from a domain leading peer-reviewed journal.

7. (verheyen2024austrianconsensusstatement pages 1-2): Nicolas Verheyen, Johannes Auer, Nikolaos Bonaros, Tamara Buchacher, Daniel Dalos, Michael Grimm, Agnes Mayr, Anna Rab, Sebastian Reinstadler, Daniel Scherr, Gabor G Toth, Thomas Weber, David K. Zach, Marc-Michael Zaruba, Daniel Zimpfer, Peter P Rainer, and Gerhard Pölzl. Austrian consensus statement on the diagnosis and management of hypertrophic cardiomyopathy. Wiener Klinische Wochenschrift, 136:571-597, Oct 2024. URL: https://doi.org/10.1007/s00508-024-02442-1, doi:10.1007/s00508-024-02442-1. This article has 6 citations and is from a peer-reviewed journal.

8. (pagel2025advancesincardiovascular pages 5-6): Paul S. Pagel, Dustin Hang, Julie K. Freed, and George J. Crystal. Advances in cardiovascular pharmacotherapy. i. cardiac myosin inhibitors. Journal of cardiothoracic and vascular anesthesia, Feb 2025. URL: https://doi.org/10.1053/j.jvca.2025.02.009, doi:10.1053/j.jvca.2025.02.009. This article has 3 citations and is from a peer-reviewed journal.

9. (seferovic2023stateoftheartdocumenton pages 11-12): Petar M. Seferović, Marija Polovina, Giuseppe Rosano, Biykem Bozkurt, Marco Metra, Stephane Heymans, Wilfried Mullens, Johann Bauersachs, Karen Sliwa, Rudolf A. de Boer, Dimitrios Farmakis, Thomas Thum, Iacopo Olivotto, Claudio Rapezzi, Aleš Linhart, Domenico Corrado, Carsten Tschöpe, Ivan Milinković, Antoni Bayes Genis, Gerasimos Filippatos, Andre Keren, Milika Ašanin, Gordana Krljanac, Ružica Maksimović, Hadi Skouri, Tuvia Ben Gal, Brenda Moura, Maurizio Volterrani, Magdy Abdelhamid, Yuri Lopatin, Ovidiu Chioncel, and Andrew J.S. Coats. State-of-the-art document on optimal contemporary management of cardiomyopathies. Sep 2023. URL: https://doi.org/10.1002/ejhf.2979, doi:10.1002/ejhf.2979. This article has 18 citations and is from a highest quality peer-reviewed journal.

10. (seferovic2023stateoftheartdocumenton pages 13-13): Petar M. Seferović, Marija Polovina, Giuseppe Rosano, Biykem Bozkurt, Marco Metra, Stephane Heymans, Wilfried Mullens, Johann Bauersachs, Karen Sliwa, Rudolf A. de Boer, Dimitrios Farmakis, Thomas Thum, Iacopo Olivotto, Claudio Rapezzi, Aleš Linhart, Domenico Corrado, Carsten Tschöpe, Ivan Milinković, Antoni Bayes Genis, Gerasimos Filippatos, Andre Keren, Milika Ašanin, Gordana Krljanac, Ružica Maksimović, Hadi Skouri, Tuvia Ben Gal, Brenda Moura, Maurizio Volterrani, Magdy Abdelhamid, Yuri Lopatin, Ovidiu Chioncel, and Andrew J.S. Coats. State-of-the-art document on optimal contemporary management of cardiomyopathies. Sep 2023. URL: https://doi.org/10.1002/ejhf.2979, doi:10.1002/ejhf.2979. This article has 18 citations and is from a highest quality peer-reviewed journal.

11. (zemljicharpf2007cardiacmyocytespecificexcisionof pages 8-11): Alice E. Zemljic-Harpf, Joel C. Miller, Scott A. Henderson, Adam T. Wright, Ana Maria Manso, Laila Elsherif, Nancy D. Dalton, Andrea K. Thor, Guy A. Perkins, Andrew D. McCulloch, and Robert S. Ross. Cardiac-myocyte-specific excision of the vinculin gene disrupts cellular junctions, causing sudden death or dilated cardiomyopathy. Molecular and Cellular Biology, 27:7522-7537, Nov 2007. URL: https://doi.org/10.1128/mcb.00728-07, doi:10.1128/mcb.00728-07. This article has 245 citations and is from a domain leading peer-reviewed journal.

12. (zemljicharpf2007cardiacmyocytespecificexcisionof pages 11-12): Alice E. Zemljic-Harpf, Joel C. Miller, Scott A. Henderson, Adam T. Wright, Ana Maria Manso, Laila Elsherif, Nancy D. Dalton, Andrea K. Thor, Guy A. Perkins, Andrew D. McCulloch, and Robert S. Ross. Cardiac-myocyte-specific excision of the vinculin gene disrupts cellular junctions, causing sudden death or dilated cardiomyopathy. Molecular and Cellular Biology, 27:7522-7537, Nov 2007. URL: https://doi.org/10.1128/mcb.00728-07, doi:10.1128/mcb.00728-07. This article has 245 citations and is from a domain leading peer-reviewed journal.

13. (verheyen2024austrianconsensusstatement pages 19-21): Nicolas Verheyen, Johannes Auer, Nikolaos Bonaros, Tamara Buchacher, Daniel Dalos, Michael Grimm, Agnes Mayr, Anna Rab, Sebastian Reinstadler, Daniel Scherr, Gabor G Toth, Thomas Weber, David K. Zach, Marc-Michael Zaruba, Daniel Zimpfer, Peter P Rainer, and Gerhard Pölzl. Austrian consensus statement on the diagnosis and management of hypertrophic cardiomyopathy. Wiener Klinische Wochenschrift, 136:571-597, Oct 2024. URL: https://doi.org/10.1007/s00508-024-02442-1, doi:10.1007/s00508-024-02442-1. This article has 6 citations and is from a peer-reviewed journal.

14. (zemljicharpf2007cardiacmyocytespecificexcisionof pages 12-14): Alice E. Zemljic-Harpf, Joel C. Miller, Scott A. Henderson, Adam T. Wright, Ana Maria Manso, Laila Elsherif, Nancy D. Dalton, Andrea K. Thor, Guy A. Perkins, Andrew D. McCulloch, and Robert S. Ross. Cardiac-myocyte-specific excision of the vinculin gene disrupts cellular junctions, causing sudden death or dilated cardiomyopathy. Molecular and Cellular Biology, 27:7522-7537, Nov 2007. URL: https://doi.org/10.1128/mcb.00728-07, doi:10.1128/mcb.00728-07. This article has 245 citations and is from a domain leading peer-reviewed journal.

15. (verheyen2024austrianconsensusstatement pages 21-22): Nicolas Verheyen, Johannes Auer, Nikolaos Bonaros, Tamara Buchacher, Daniel Dalos, Michael Grimm, Agnes Mayr, Anna Rab, Sebastian Reinstadler, Daniel Scherr, Gabor G Toth, Thomas Weber, David K. Zach, Marc-Michael Zaruba, Daniel Zimpfer, Peter P Rainer, and Gerhard Pölzl. Austrian consensus statement on the diagnosis and management of hypertrophic cardiomyopathy. Wiener Klinische Wochenschrift, 136:571-597, Oct 2024. URL: https://doi.org/10.1007/s00508-024-02442-1, doi:10.1007/s00508-024-02442-1. This article has 6 citations and is from a peer-reviewed journal.

16. (zemljicharpf2007cardiacmyocytespecificexcisionof pages 3-4): Alice E. Zemljic-Harpf, Joel C. Miller, Scott A. Henderson, Adam T. Wright, Ana Maria Manso, Laila Elsherif, Nancy D. Dalton, Andrea K. Thor, Guy A. Perkins, Andrew D. McCulloch, and Robert S. Ross. Cardiac-myocyte-specific excision of the vinculin gene disrupts cellular junctions, causing sudden death or dilated cardiomyopathy. Molecular and Cellular Biology, 27:7522-7537, Nov 2007. URL: https://doi.org/10.1128/mcb.00728-07, doi:10.1128/mcb.00728-07. This article has 245 citations and is from a domain leading peer-reviewed journal.

17. (zemljicharpf2007cardiacmyocytespecificexcisionof pages 7-8): Alice E. Zemljic-Harpf, Joel C. Miller, Scott A. Henderson, Adam T. Wright, Ana Maria Manso, Laila Elsherif, Nancy D. Dalton, Andrea K. Thor, Guy A. Perkins, Andrew D. McCulloch, and Robert S. Ross. Cardiac-myocyte-specific excision of the vinculin gene disrupts cellular junctions, causing sudden death or dilated cardiomyopathy. Molecular and Cellular Biology, 27:7522-7537, Nov 2007. URL: https://doi.org/10.1128/mcb.00728-07, doi:10.1128/mcb.00728-07. This article has 245 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Hypertrophic_Cardiomyopathy_15-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 6 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 6 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 48 |
| Resolved | 48 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013200` (4 mentions) - the report calls it "if available"; MONDO calls it **hypertrophic cardiomyopathy 15**
