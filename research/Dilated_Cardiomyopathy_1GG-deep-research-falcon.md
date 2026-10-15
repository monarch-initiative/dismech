---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-31T10:10:09.213596'
end_time: '2026-08-31T10:21:40.372367'
duration_seconds: 691.16
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Dilated Cardiomyopathy 1GG
  mondo_id: MONDO:0013339
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 15
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 1
  quotes_valid: 1
  quotes_not_checkable: 1
  relevance_assessed: 4
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 13
  verified: 13
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 2
  labels_matching: 0
  labels_mismatched: 1
  mislabelled_terms:
  - term_id: MONDO:0013339
    reported_labels:
    - if available
    ontology_label: dilated cardiomyopathy 1GG
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Dilated_Cardiomyopathy_1GG-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dilated Cardiomyopathy 1GG
- **MONDO ID:** MONDO:0013339 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dilated Cardiomyopathy 1GG** covering all of the
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
- **Disease Name:** Dilated Cardiomyopathy 1GG
- **MONDO ID:** MONDO:0013339 (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Dilated Cardiomyopathy 1GG** covering all of the
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


# Dilated Cardiomyopathy 1GG (DCM1GG): disease-characteristics report

## Executive summary and evidence limits

Dilated cardiomyopathy 1GG is an exceptionally rare, predominantly neonatal/infantile, autosomal-recessive cardiomyopathy attributed to biallelic **SDHA** dysfunction. The defining evidence remains a 2010 study of 15 affected members of consanguineous Bedouin kindreds carrying homozygous **SDHA c.1664G>A (p.Gly555Glu; G555E)**. Thus, most subtype-specific frequency and outcome estimates derive from one founder cohort and should not be generalized to every biallelic SDHA genotype. Open Targets independently associates SDHA with dilated, familial, and familial-isolated DCM, but this is aggregated secondary evidence rather than a new cohort (OpenTargets Search: Dilated cardiomyopathy-SDHA, levitas2010familialneonatalisolated pages 1-2).

The evidence can be summarized as follows:

| domain | finding | evidence type/strength | key source |
|---|---|---|---|
| Disease identity | Dilated Cardiomyopathy 1GG is a Mendelian DCM subtype linked to **SDHA**; foundational reported causal variant is **c.1664G>A (p.Gly555Glu / G555E)** in homozygosity | Human primary family study; strong for variant-disease association in reported kindreds | Levitas et al., 2010 (levitas2010familialneonatalisolated pages 1-2, levitas2010familialneonatalisolated pages 2-3, levitas2010familialneonatalisolated pages 5-6) |
| Inheritance | **Autosomal recessive** inheritance in consanguineous families; affected individuals homozygous, available parents typically heterozygous | Human segregation evidence; strong within families | Levitas et al., 2010 (levitas2010familialneonatalisolated pages 1-2, levitas2010familialneonatalisolated pages 2-3, levitas2010familialneonatalisolated pages 4-5) |
| Cohort/founder context | **15 Bedouin patients** from **two large consanguineous families** of one tribe; authors infer a common founder | Human cohort description; moderate-strong | Levitas et al., 2010 (levitas2010familialneonatalisolated pages 1-2, levitas2010familialneonatalisolated pages 2-3) |
| Onset/clinical spectrum | Onset ranged from **32 weeks gestation to 10 years**; prominent pediatric/neonatal isolated cardiomyopathy with LV dilation and systolic dysfunction | Human case-series evidence; strong descriptive | Levitas et al., 2010 (levitas2010familialneonatalisolated pages 1-2, levitas2010familialneonatalisolated pages 2-3, levitas2010familialneonatalisolated pages 3-4) |
| Core phenotype | Frequent features included **respiratory distress, congestive heart failure, cardiogenic shock, cardiomegaly, LV dilation, reduced fractional shortening**, and **LV noncompaction in 8 infants** | Human phenotype evidence; strong descriptive | Levitas et al., 2010 (levitas2010familialneonatalisolated pages 2-3, levitas2010familialneonatalisolated pages 3-4) |
| Mortality/course | Condition showed **high mortality**, with **about two-thirds** succumbing to cardiac failure; rapid deterioration resembles mitochondrial cardiomyopathy burden | Human case-series evidence; moderate-strong | Levitas et al., 2010 (levitas2010familialneonatalisolated pages 5-6) |
| Cardiac testing | ECG reportedly showed **sinus rhythm, LV hypertrophy, normal QTc**; lactate was usually normal except **mild elevation to 3.7 mmol/L**; two brain MRIs lacked Leigh-syndrome lesions | Human clinical testing evidence; moderate | Levitas et al., 2010 (levitas2010familialneonatalisolated pages 2-3) |
| Biochemical defect | Respiratory-chain testing showed **tissue-specific complex II deficiency**: skeletal muscle residual activity about **50-60%**, versus myocardium about **15-18%** for succinate dehydrogenase/complex II; succinate oxidation in muscle **26%** in one assay | Human biochemical evidence; strong | Levitas et al., 2010 (levitas2010familialneonatalisolated pages 2-3, levitas2010familialneonatalisolated pages 4-5, levitas2010familialneonatalisolated pages 5-6) |
| Specificity/variability | Partial complex I decrease occurred in one patient, but normal aconitase argued against generalized iron-sulfur metabolism failure; phenotype showed marked intrafamilial variability | Human biochemical/clinical evidence; moderate | Levitas et al., 2010 (levitas2010familialneonatalisolated pages 2-3, levitas2010familialneonatalisolated pages 5-6) |
| Reduced penetrance | One adult father was **homozygous** for the variant yet clinically unaffected on exam, ECG, and echocardiography despite reduced lymphoblast complex II activity, indicating **nonpenetrance/reduced penetrance** | Human observation; important but based on single individual | Levitas et al., 2010 (levitas2010familialneonatalisolated pages 4-5, levitas2010familialneonatalisolated pages 5-6) |
| Mechanistic interpretation | Authors concluded disease is “**presumably caused by the significant tissue-specific reduction in SDH enzymatic activity in the heart muscle**,” while retaining more activity in skeletal muscle and lymphoblastoid cells | Human mechanistic inference anchored by enzyme assays; moderate | Levitas et al., 2010 (levitas2010familialneonatalisolated pages 1-2, levitas2010familialneonatalisolated pages 5-6) |
| Supporting disease-gene mapping | Independent target-disease aggregation resources also map **SDHA** to dilated/familial isolated DCM | Aggregated database evidence; supportive but secondary | Open Targets association (OpenTargets Search: Dilated cardiomyopathy-SDHA) |
| Experimental mechanism relevance | In mice, **cardiac Sdhaf4 loss** impaired complex II assembly, promoted **SDHA/SDHB degradation**, metabolic impairment, **DRP1-mediated mitochondrial fission/mitophagy**, and progressive **dilated cardiomyopathy/lethal heart failure** | Mouse mechanistic study; strong for complex-II-to-DCM biology, indirect for DCM1GG | Wang et al., 2022 (wang2022cardiacdisruptionof pages 1-2, wang2022cardiacdisruptionof pages 10-12) |
| Experimental rescue relevance | In the Sdhaf4 mouse model, **fumarate supplementation** or **mitochondrial fission inhibition** partially restored cardiac function and prolonged lifespan | Mouse interventional evidence; hypothesis-generating, not subtype-specific clinical proof | Wang et al., 2022 (wang2022cardiacdisruptionof pages 1-2, wang2022cardiacdisruptionof pages 10-12) |
| Current diagnosis | Contemporary cardiomyopathy guidance emphasizes **deep phenotyping, ECG, biomarkers, echocardiography/CMR, and genetic workup** for hereditary cardiomyopathy | Recent guideline/review evidence; strong for general DCM practice | ESC-guideline summary 2024; guideline review 2025 (grasso2024thenew2023 pages 1-2, sorella2025diagnosisandmanagement pages 12-13) |
| Current family management | **Genetic counselling and cascade screening** of at-risk relatives are recommended when a pathogenic variant is identified; advanced HF care may require transplant/device evaluation | Recent guideline/review evidence; strong for general DCM practice | Guideline review 2025 (sorella2025diagnosisandmanagement pages 12-13) |
| Subtype-specific treatment evidence | No **approved therapy**, no validated **SDHA/DCM1GG-specific treatment algorithm**, and no clearly identified **clinical trial dedicated to this subtype** were found in the available evidence | Evidence gap / negative finding from searched literature and trials; moderate confidence | Available evidence corpus and trial searches (sorella2025diagnosisandmanagement pages 12-13, grasso2024thenew2023 pages 1-2) |


*Table: This table compacts the strongest available evidence for Dilated Cardiomyopathy 1GG, separating direct human subtype evidence from indirect mechanistic and guideline evidence. It is useful for quickly identifying what is established, what is inferred, and where current evidence gaps remain.*

**Evidence notation used below:** *human-direct* means observations in DCM1GG patients; *human-indirect* means findings in broader DCM or other SDHA disease; *model* means animal/cellular evidence not yet demonstrated in DCM1GG patients.

---

## 1. Disease information

### Definition

DCM1GG is a Mendelian mitochondrial-energy cardiomyopathy in which left or both ventricles become dilated and systolic function is impaired. In the defining families it was usually an isolated cardiac disorder, often beginning prenatally or in infancy, rather than the encephalomyopathic/Leigh phenotype also produced by biallelic SDHA variants. The paper’s exact abstract statement was: **“we present the association of a mutation in the SDHA gene with recessive neonatal isolated DCM in 15 patients of two large consanguineous Bedouin families.”** It further called the phenotype a “severe form of neonatal cardiomyopathy” with “extreme phenotypic variability” (published online **16 June 2010**; PMID **20551992**; DOI: https://doi.org/10.1038/ejhg.2010.83) (levitas2010familialneonatalisolated pages 1-2).

### Identifiers and terminology

- **MONDO:** MONDO:0013339, as supplied in the query; this should be retained as the knowledge-base primary identifier.
- **Disease name/synonyms:** dilated cardiomyopathy 1GG; DCM1GG; SDHA-related dilated cardiomyopathy; SDHA-related recessive neonatal isolated cardiomyopathy; familial neonatal isolated cardiomyopathy caused by SDHA mutation.
- **Causal-gene identifier:** **SDHA**, succinate dehydrogenase complex flavoprotein subunit A; Ensembl **ENSG00000073578** (OpenTargets Search: Dilated cardiomyopathy-SDHA).
- **Parent/general disease:** dilated cardiomyopathy, historically MIM 115200 in the primary paper (levitas2010familialneonatalisolated pages 1-2).
- **OMIM subtype number:** not independently recoverable from the searched full text; it should be verified directly in OMIM before database ingestion rather than inferred from the suffix “1GG.”
- **Orphanet:** no subtype-specific Orphanet identifier was established in the retrieved evidence.
- **ICD-10/ICD-11 and MeSH:** coding is at the general DCM/cardiomyopathy level, not an SDHA-specific clinical code. Appropriate broad terms are ICD-10-CM **I42.0** and MeSH **Cardiomyopathy, Dilated**; these should not be represented as uniquely identifying DCM1GG.

The foundational information is aggregated at disease/family level from deliberately recruited patients and medical-record review—not a population EHR analysis. The investigators reviewed growth, development, hospitalizations, laboratory studies, serial ECG and echocardiography, family examinations, and molecular/biochemical testing (levitas2010familialneonatalisolated pages 2-3).

---

## 2. Etiology

### Causal factor and genetic risk

The demonstrated initiating lesion is germline homozygosity for **SDHA c.1664G>A, p.Gly555Glu**. All tested affected individuals were homozygous; healthy siblings were heterozygous or homozygous reference, and almost all available parents were heterozygous. Linkage/autozygosity mapping identified a 5.6-cM segment containing SDHA, followed by cDNA and genomic sequencing (levitas2010familialneonatalisolated pages 2-3, levitas2010familialneonatalisolated pages 4-5).

The variant had previously been associated with lethal infantile multisystem disease and Leigh syndrome. Previous functional work cited by the family study showed destabilization/assembly failure of mitochondrial complex II and approximately halved activity in muscle or fibroblasts; it was absent from 186 historical control chromosomes. A modern global allele frequency and current ClinVar ACMG classification were not established by the retrieved evidence and must be checked directly against the current ClinVar/gnomAD release before curation (levitas2010familialneonatalisolated pages 4-5, levitas2010familialneonatalisolated pages 5-6).

### Risk, protective, and modifying factors

- **Established risk factors:** biallelic pathogenic SDHA genotype, consanguinity, and family history. The reported families belonged to one Bedouin tribe and were considered to share a founder allele (levitas2010familialneonatalisolated pages 2-3).
- **Reduced penetrance/modification:** one homozygous adult father had normal examination, ECG, and LV size/function despite lymphoblast complex-II activity similar to affected patients. This is direct evidence of reduced penetrance, although based on one person. SDHB, SDHD, and SDHAF1 sequencing did not explain the difference; unidentified genetic, epigenetic, or environmental modifiers remain plausible (levitas2010familialneonatalisolated pages 4-5, levitas2010familialneonatalisolated pages 5-6).
- **Environmental risks/protective factors:** none were demonstrated specifically for DCM1GG. General myocardial stressors—viral myocarditis, cardiotoxic agents, ischemia, alcohol, pregnancy, metabolic stress—may worsen DCM, but extrapolation to this founder disorder is untested.
- **Gene–environment interaction:** the historical G555E infant with lethal multisystem disease deteriorated following respiratory infection and severe hypoglycemia, suggesting that catabolic stress may unmask limited mitochondrial reserve; this was not proven in the isolated-DCM cohort (levitas2010familialneonatalisolated pages 1-2, levitas2010familialneonatalisolated pages 4-5).
- **Protective alleles/dietary protection:** none established. The unaffected homozygous father strongly suggests modification, but no protective allele was identified (levitas2010familialneonatalisolated pages 5-6).

---

## 3. Phenotypes

The following frequencies are from the 15-person founder cohort unless otherwise stated.

- **Dilated left ventricle / cardiomegaly** — structural sign; present across the reported affected series. LV end-diastolic diameters in the table ranged approximately **33–50 mm**, with age-inappropriate dilation. Suggested HPO: **Dilated cardiomyopathy (HP:0001644)** and **Cardiomegaly (HP:0001640)** (levitas2010familialneonatalisolated pages 2-3, levitas2010familialneonatalisolated pages 3-4).
- **LV systolic dysfunction** — functional sign; fractional shortening ranged from **<10% to 26%**, frequently severe. Suggested HPO: decreased left-ventricular systolic function and reduced ejection/fractional shortening; verify current HPO identifiers before ingestion (levitas2010familialneonatalisolated pages 3-4).
- **Congestive heart failure** — clinical syndrome with respiratory distress, repeated admissions, feeding/exercise limitations, and sometimes cardiogenic shock. Suggested HPO: **Congestive heart failure (HP:0001635)** and **Respiratory distress (HP:0002098)** (levitas2010familialneonatalisolated pages 3-4).
- **Left-ventricular noncompaction/trabeculation** — reported in **8 infants (8/15; 53%)**. Suggested HPO: **Left ventricular noncompaction (HP:0031689)**. Contemporary ESC interpretation treats LV noncompaction as a morphologic trait that can occur in several settings, so it should be recorded alongside—not substituted for—the causal DCM diagnosis (levitas2010familialneonatalisolated pages 2-3, grasso2024thenew2023 pages 1-2).
- **LV hypertrophy and mitral insufficiency** — usually mild/moderate and accompanying dilation in survivors. Suggested HPO: **Left ventricular hypertrophy (HP:0001712)** and **Mitral regurgitation (HP:0001653)** (levitas2010familialneonatalisolated pages 3-4).
- **ECG abnormality** — sinus rhythm with LV hypertrophy and normal QTc in all assessed patients; no defining conduction phenotype was reported (levitas2010familialneonatalisolated pages 2-3).
- **Mild hyperlactatemia** — lactate **3.7 mmol/L**; otherwise routine indices were largely normal. Suggested HPO: **Increased serum lactate (HP:0002151)** (levitas2010familialneonatalisolated pages 2-3).
- **Neurologic/skeletal-muscle sparing in this phenotype** — normal growth, age-appropriate development, muscle bulk/strength, reflexes, and gait; no seizures during follow-up. Two brain MRIs lacked basal-ganglia, cortex, gray-matter, or brainstem lesions, arguing against Leigh syndrome in those patients (levitas2010familialneonatalisolated pages 2-3).
- **Exercise intolerance** — documented in several longer-term survivors. Suggested HPO: **Exercise intolerance (HP:0003546)** (levitas2010familialneonatalisolated pages 3-4).

### Onset, severity, progression, and quality of life

The reported enrollment/presentation spectrum extended from **32 weeks’ gestation to 10 years**, but most tabulated symptomatic onsets were prenatal or at **1–8 months**. Severity ranged from asymptomatic cardiomegaly/mild dysfunction to shock and death. Progression was generally chronic and often rapidly progressive in infancy, with recurrent heart-failure admissions; some survivors attended normal school into ages 7–11 years but experienced exercise intolerance (levitas2010familialneonatalisolated pages 2-3, levitas2010familialneonatalisolated pages 3-4).

No DCM1GG-specific EQ-5D, SF-36, PROMIS, or pediatric quality-of-life data exist in the retrieved literature. Respiratory distress, frequent hospitalization, exercise intolerance, and early mortality imply major family and functional burden, but a quantitative utility estimate would be unsupported.

---

## 4. Genetic and molecular information

### Gene and variant

- **Gene:** **SDHA**, nuclear encoded, chromosome 5; protein is the FAD-containing flavoprotein catalytic subunit of succinate dehydrogenase/respiratory complex II.
- **Variant:** **c.1664G>A (p.Gly555Glu; G555E)**, exon 13 in the transcript used by the original investigators.
- **Origin:** constitutional/germline.
- **Zygosity/inheritance:** homozygous disease state; autosomal recessive.
- **Class:** missense. Historical evidence supports pathogenicity through segregation, linkage, rarity in controls, recurrent disease association, complex-II instability, and deficient enzyme activity (levitas2010familialneonatalisolated pages 2-3, levitas2010familialneonatalisolated pages 4-5, levitas2010familialneonatalisolated pages 5-6).
- **Functional consequence:** partial loss of complex-II stability/activity rather than complete null function. Cardiac SDH activity was only **15–18%** of control, compared with **50–60%** residual activity in skeletal muscle and approximately **60–63%** in selected lymphoblast assays. Complex II+III activity in myocardium was **8–21%** of control; succinate oxidation was **26%** in one skeletal-muscle assay (levitas2010familialneonatalisolated pages 2-3, levitas2010familialneonatalisolated pages 4-5).

All four SDH subunits are nuclear encoded: soluble SDHA and SDHB are anchored to the inner mitochondrial membrane by SDHC and SDHD. SDHA oxidizes succinate to fumarate while passing electrons into the respiratory chain through ubiquinone, linking the tricarboxylic-acid cycle and oxidative phosphorylation (levitas2010familialneonatalisolated pages 1-2, wang2022cardiacdisruptionof pages 1-2).

### Modifiers, epigenetics, and structural variation

No validated modifier gene, methylation signature, chromatin lesion, pathogenic copy-number change, translocation, inversion, or aneuploidy has been established for DCM1GG. SDHAF1 was investigated but did not account for intrafamilial variability. CMA/karyotype/FISH are therefore not first-line tests for this single-nucleotide founder disorder unless the patient has additional congenital anomalies or sequencing is unrevealing (levitas2010familialneonatalisolated pages 4-5, levitas2010familialneonatalisolated pages 5-6).

Heterozygous germline SDHA loss-of-function variants can confer tumor predisposition in other contexts, whereas DCM1GG is a recessive mitochondrial phenotype. These should not be conflated; cancer surveillance decisions require variant-specific genetics expertise and are not established from the G555E DCM cohort.

---

## 5. Environmental information

No toxin, radiation, pollutant, occupational exposure, smoking pattern, alcohol exposure, dietary factor, or infectious agent was shown to cause DCM1GG. The disease is genetic. Nevertheless, prudent mitochondrial/heart-failure care includes avoiding smoking, binge alcohol, illicit stimulants, unprescribed mitochondrial-toxic drugs, dehydration, prolonged fasting, and delayed treatment of infection. These are risk-management principles, not demonstrated primary prevention of the genotype.

Because the heart has high energy demand and patients have limited complex-II reserve, fever, fasting, hypoglycemia, major surgery, or infection are biologically plausible “second hits.” Evidence remains indirect; no controlled DCM1GG gene–environment study exists.

---

## 6. Mechanism/pathophysiology

### Ordered causal chain

1. **Biallelic SDHA p.Gly555Glu leads to** impaired stability/assembly and catalytic function of mitochondrial respiratory complex II in affected tissues. This is supported by prior functional observations and direct patient enzyme assays (levitas2010familialneonatalisolated pages 4-5, levitas2010familialneonatalisolated pages 5-6).
2. **Complex-II dysfunction leads to** markedly reduced cardiac succinate-dehydrogenase and succinate-to-respiratory-chain flux; myocardium retains only 15–18% SDH activity, much less than skeletal muscle or lymphoblasts (levitas2010familialneonatalisolated pages 2-3, levitas2010familialneonatalisolated pages 4-5).
3. **Reduced succinate oxidation/electron transfer is inferred to lead to** impaired TCA-cycle/oxidative-phosphorylation coupling and inadequate ATP-generating reserve in energy-intensive cardiomyocytes. ATP depletion was not directly measured in DCM1GG hearts.
4. **Complex-II metabolic failure is inferred to branch:**  
   **4a.** energetic insufficiency **leads to** impaired excitation–contraction and systolic function;  
   **4b.** redox/TCA imbalance **may lead to** ROS injury, succinate accumulation, fumarate depletion, and mitochondrial damage. This branch is supported mainly by complex-II mouse models, not demonstrated in DCM1GG patients (wang2022cardiacdisruptionof pages 10-12, wang2022cardiacdisruptionof pages 1-2).
5. **Mitochondrial damage is inferred to lead to** DRP1 activation, excess mitochondrial fission and mitophagy, reducing functional mitochondrial mass. This was demonstrated after cardiac Sdhaf4 loss in mice, not after human SDHA G555E (wang2022cardiacdisruptionof pages 1-2).
6. **Cardiomyocyte energetic and organelle failure leads to** reduced contractility and maladaptive ventricular remodeling, producing LV dilation, reduced fractional shortening, noncompaction morphology, mitral insufficiency, and sometimes hypertrophy (levitas2010familialneonatalisolated pages 2-3, levitas2010familialneonatalisolated pages 3-4).
7. **Progressive pump dysfunction leads to** pulmonary congestion/respiratory distress, recurrent CHF, cardiogenic shock, exercise intolerance, and early cardiac death (levitas2010familialneonatalisolated pages 3-4, levitas2010familialneonatalisolated pages 5-6).

### Detailed pathways and evidence grading

**Human-direct:** the decisive biochemical abnormality is tissue-selective complex-II deficiency. Complexes III and IV were largely preserved; one patient had partial complex-I reduction, while normal aconitase argued against a generalized iron–sulfur assembly defect. Why the heart is much more affected than other tissues remains unresolved (levitas2010familialneonatalisolated pages 2-3, levitas2010familialneonatalisolated pages 4-5).

**Mouse supporting mechanism:** cardiac/muscle Sdhaf4 deletion suppresses SDHA–SDHB assembly, accelerates subunit degradation, increases ROS/protein oxidation, raises succinate, lowers fumarate, activates DRP1-dependent fission/mitophagy, and causes progressive DCM and lethal heart failure. Importantly, metabolic abnormalities precede gross remodeling, supporting complex-II failure as upstream rather than merely a consequence of heart failure. Fumarate supplementation or fission inhibition partially rescued function and survival in mice. The authors’ exact abstract wording was that loss of Sdhaf4 causes “globally impaired metabolic capacity and activation of dynamin-related protein 1, which induces excess mitochondrial fission and mitophagy, thereby causing progressive dilated cardiomyopathy and lethal heart failure in animals” (published **July 2022**; DOI: https://doi.org/10.1038/s41467-022-31548-1) (wang2022cardiacdisruptionof pages 1-2, wang2022cardiacdisruptionof pages 10-12).

**Omics:** no DCM1GG patient-specific transcriptome, proteome, metabolome, lipidome, single-cell, spatial-transcriptomic, or integrated multi-omic dataset was found. Public human DCM expression data show reduced SDHAF4, but this is general DCM and does not establish the mechanism of SDHA G555E (wang2022cardiacdisruptionof pages 1-2).

**Suggested ontology annotations:**

- GO: **succinate dehydrogenase activity**; **tricarboxylic acid cycle**; **mitochondrial electron transport, succinate to ubiquinone**; **oxidative phosphorylation**; **ATP metabolic process**; **reactive oxygen species metabolic process**; **mitochondrial fission**; **mitophagy**; **cardiac muscle contraction**; **ventricular cardiac muscle tissue morphogenesis**. Exact IDs should be resolved against the current GO release.
- Cell Ontology: **cardiomyocyte (CL:0000746)**, ventricular cardiomyocyte, cardiac fibroblast, vascular endothelial cell, and cardiac macrophage. Only cardiomyocytes have direct mechanistic priority; fibrosis/immune-cell involvement is plausible downstream biology, not subtype-demonstrated.
- Cellular component: **mitochondrial matrix**, **mitochondrial inner membrane**, **succinate dehydrogenase complex**, **respiratory-chain complex II**.

---

## 7. Anatomical structures affected

The primary organ is the **heart**, especially the **left ventricular myocardium**; both ventricles can be involved under the broader DCM definition. Suggested anatomy terms include UBERON **heart (UBERON:0000948)**, **left ventricle (UBERON:0002084)**, myocardium, interventricular septum, papillary/mitral apparatus, and cardiac muscle tissue. Exact ontology IDs beyond the first two should be release-validated.

At tissue/cell level, ventricular cardiomyocytes are the primary affected population; secondary remodeling may involve cardiac fibroblasts, vascular cells, and inflammatory cells. Subcellular involvement is mitochondrial—matrix-facing catalytic complex II associated with the inner mitochondrial membrane. There is no lateralization; “left” denotes ventricular anatomy, not unilateral disease.

Secondary organ effects arise from low cardiac output and congestion: lungs/respiratory system, liver, kidneys, and systemic circulation may be affected in advanced failure. Neurologic and skeletal-muscle disease were notably absent in the defining isolated-cardiomyopathy cohort, although other biallelic SDHA phenotypes can involve brain and muscle (levitas2010familialneonatalisolated pages 2-3).

---

## 8. Temporal development

- **Typical onset:** prenatal, neonatal, or infantile; outliers may be detected later in childhood.
- **Pattern:** usually insidious structural dysfunction followed by acute decompensation, respiratory distress, or shock. Three patients were recognized at 32–33 gestational weeks (levitas2010familialneonatalisolated pages 3-4).
- **Early stage:** cardiomegaly/LV dilation, sometimes asymptomatic; mildly reduced function.
- **Intermediate stage:** declining shortening, noncompaction morphology, mitral insufficiency, exercise intolerance, recurrent CHF admissions.
- **Advanced stage:** severe noncontractile LV, cardiogenic shock, refractory failure, or sudden death.
- **Course:** chronic lifelong genetic vulnerability with highly variable progression. Several deaths occurred at 1–11 months, while survivors reached 7–11 years with normal school performance but sometimes exercise limitation (levitas2010familialneonatalisolated pages 3-4).
- **Remission/recovery:** no robust spontaneous-remission rate or treatment-induced reverse-remodeling statistic is available. The clinically normal homozygous adult represents nonpenetrance rather than documented recovery (levitas2010familialneonatalisolated pages 4-5, levitas2010familialneonatalisolated pages 5-6).
- **Critical window:** fetal life and the first year are the principal vulnerability period in the known cohort, supporting immediate evaluation after prenatal cardiomegaly, neonatal distress, or identification of an at-risk genotype.

---

## 9. Inheritance and population

### Inheritance

Inheritance is **autosomal recessive**. For two confirmed heterozygous parents, each pregnancy has a 25% probability of an affected biallelic child, 50% of a heterozygous carrier, and 25% of a child inheriting neither familial allele. Expressivity is markedly variable and penetrance is incomplete, demonstrated by one clinically normal homozygous adult (levitas2010familialneonatalisolated pages 4-5, levitas2010familialneonatalisolated pages 5-6).

There is no evidence of anticipation. Germline mosaicism was not reported. Consanguinity was central to the reported pedigrees, and the shared tribal/family context supports a founder effect. Carrier frequency in the tribe and in global populations remains unknown. No reliable sex ratio can be estimated from 15 founder cases; both sexes were affected (levitas2010familialneonatalisolated pages 2-3, levitas2010familialneonatalisolated pages 3-4).

### Epidemiology

No population prevalence or incidence exists for DCM1GG. Only 15 cases in the defining report were characterized, so any cases-per-100,000 estimate would be misleading. SDH deficiency broadly was described as approximately **2% of mitochondrial respiratory-chain disorders**, but that is not the prevalence of DCM1GG (levitas2010familialneonatalisolated pages 1-2).

Geographic/ancestry evidence is limited to the reported consanguineous Bedouin tribe in Israel. The disease should not be characterized as exclusive to this population; rather, this particular founder variant and phenotype were discovered there.

---

## 10. Diagnostics

### Clinical diagnosis

Current cardiomyopathy practice begins with a three-generation pedigree, physical examination, ECG, echocardiography, laboratory evaluation, and exclusion of coronary, hypertensive, valvular, congenital, toxic, infectious, and loading causes sufficient to explain the phenotype. The 2023 ESC definition describes cardiomyopathies as myocardial disorders with structural/functional abnormality absent those alternative causes. The 2024 ESC commentary emphasizes ECG, first-/second-level biomarkers, multimodality imaging, and a genetics pathway (published **April 2024**; DOI: https://doi.org/10.1093/eurheartjsupp/suae002) (grasso2024thenew2023 pages 1-2).

**Recommended tests:**

1. **Echocardiography:** LV dimensions indexed to age/body size, shortening/ejection fraction, global/regional function, trabeculation/noncompaction, mitral regurgitation, RV involvement.
2. **ECG and rhythm monitoring:** standard ECG, Holter/event monitoring where symptomatic or with ventricular dysfunction; DCM1GG has no established signature beyond LVH in the founder cohort.
3. **CMR:** ventricular volumes/function, fibrosis by late gadolinium enhancement, edema/inflammation, and alternative diagnoses; sedation/instability may limit neonatal use.
4. **Laboratory studies:** BNP/NT-proBNP and troponin for heart-failure/injury assessment; electrolytes, renal/liver function, CBC, thyroid studies, CK; lactate, pyruvate, glucose, amino/organic acids, acylcarnitines, and carnitine when mitochondrial/metabolic DCM is suspected. Biomarkers are supportive, not diagnostic. Recent guideline synthesis identifies natriuretic peptides and high-sensitivity troponin as consensus tests (sorella2025diagnosisandmanagement pages 12-13).
5. **Respiratory-chain testing:** complex-II assays in muscle or myocardium can support causality. A normal/mild lymphoblast or skeletal-muscle result does not exclude severe cardiac deficiency because tissue specificity was profound (levitas2010familialneonatalisolated pages 2-3, levitas2010familialneonatalisolated pages 4-5).
6. **Biopsy:** not routinely required solely to diagnose DCM1GG; consider when myocarditis, infiltrative disease, storage disease, or unresolved mitochondrial disease would change management. ESC commentary notes that biopsy remains reserved for selected indications (grasso2024thenew2023 pages 1-2).

### Genetic testing

A cardiomyopathy/mitochondrial panel that includes **SDHA**, or trio exome/genome sequencing with CNV analysis, is appropriate for severe neonatal DCM, especially with consanguinity. If the familial variant is known, targeted testing for c.1664G>A is fastest and least expensive. Confirm in an accredited laboratory with segregation testing. WES/WGS is especially useful for phenotypic expansion, locus heterogeneity, deep intronic/structural variants, or a negative panel. RNA sequencing may resolve splice variants but has no established routine DCM1GG biomarker role.

CMA, karyotyping, and FISH have low expected yield for an isolated known SNV but may be used for syndromic congenital anomalies. mtDNA sequencing can be included in unexplained mitochondrial cardiomyopathy, although SDHA itself is nuclear encoded. Repeat-expansion testing is not relevant unless another phenotype indicates it.

### Diagnostic criteria and differential diagnosis

A defensible molecular diagnosis requires (i) DCM phenotype, (ii) biallelic pathogenic/likely pathogenic SDHA variants with appropriate segregation, and (iii) exclusion of stronger alternative causes; complex-II biochemical deficiency strengthens the diagnosis. A VUS alone is insufficient.

Important differentials include viral/immune myocarditis, anomalous coronary origin or ischemia, congenital heart disease, tachycardia-induced cardiomyopathy, endocrine/nutritional causes, Barth syndrome (**TAZ**), mitochondrial translation/OXPHOS defects, fatty-acid oxidation disorders, CoQ deficiency, glycogen/storage disease, and other recessive DCM genes. Leigh syndrome should be evaluated if developmental regression, seizures, hypotonia, movement disorder, or characteristic MRI lesions occur. The founder cohort’s normal neuromuscular examinations and two negative brain MRIs support an isolated cardiac presentation, not exclusion of neurologic SDHA disease in every genotype (levitas2010familialneonatalisolated pages 2-3).

### Family screening

Once a pathogenic familial genotype is established, offer genetic counseling and cascade testing. Biallelic relatives require cardiac evaluation even if asymptomatic because penetrance is variable; heterozygous relatives need reproductive counseling and individualized assessment. Contemporary ESC/AHA guidance strongly supports cascade screening after identification of a pathogenic variant (sorella2025diagnosisandmanagement pages 12-13).

---

## 11. Outcome and prognosis

The defining report states exactly that the condition was **“marked by high mortality, with two-thirds succumbing to cardiac failure.”** Given 15 cases, this corresponds to approximately ten deaths, although follow-up duration varied. Deaths in the table clustered in early infancy, including cardiogenic shock and one sudden death at home. Several children survived to 7–11 years with normal schooling, showing substantial within-genotype variability (levitas2010familialneonatalisolated pages 3-4, levitas2010familialneonatalisolated pages 5-6).

No reliable 5- or 10-year survival curve, median life expectancy, disability-adjusted life-year estimate, or validated subtype-specific prognostic score exists. Prognosis is likely worse with prenatal onset, severe LV dilation, fractional shortening <10%, recurrent CHF, cardiogenic shock, and failure to improve with therapy, but these have not been formally modeled.

Major complications are chronic/refractory heart failure, pulmonary congestion, mitral regurgitation, arrhythmia/sudden death, thromboembolism in severe ventricular dysfunction, end-organ hypoperfusion, mechanical-support requirement, and transplantation. Quality-of-life morbidity includes repeated hospitalization and exercise limitation; formal patient-reported outcomes are absent.

---

## 12. Treatment

### Current clinical strategy

There is **no approved SDHA- or DCM1GG-specific therapy**. Treatment follows age-appropriate DCM and heart-failure guidance in a pediatric cardiomyopathy/mitochondrial center:

- diuretics for congestion;
- guideline-directed systolic-heart-failure therapy as age, blood pressure, renal function, and pediatric evidence permit—ACE inhibitor/ARB or ARNI, evidence-based beta blocker, mineralocorticoid-receptor antagonist, and in suitable older patients an SGLT2 inhibitor;
- inotropes/vasoactive support for cardiogenic shock;
- anticoagulation only for standard indications such as intracardiac thrombus, embolism, atrial arrhythmia, or severe dysfunction with additional risk;
- rhythm surveillance and treatment; ICD/CRT decisions are individualized because no DCM1GG-specific threshold exists;
- mechanical circulatory support as bridge to recovery/transplant and cardiac transplantation for refractory advanced disease. Guideline synthesis recommends transplantation for refractory NYHA III–IV disease and consideration of mechanical support as bridge therapy (sorella2025diagnosisandmanagement pages 12-13).

Suggested NCIt intervention concepts include **heart-failure therapy**, **diuretic therapy**, **ACE-inhibitor therapy**, **beta-blocker therapy**, **implantable cardioverter-defibrillator**, **ventricular assist device**, and **heart transplantation**; exact NCIt codes should be resolved in the current thesaurus.

### Mitochondrial supplements and pharmacogenomics

Riboflavin, coenzyme Q10, carnitine, antioxidants, or other “mitochondrial cocktails” are sometimes used empirically in respiratory-chain disease, but no controlled efficacy evidence exists for SDHA G555E cardiomyopathy. They should not replace heart-failure therapy. No DCM1GG pharmacogenomic dosing rule is established.

### Experimental therapies

Fumarate supplementation and DRP1/mitochondrial-fission inhibition improved function and survival in **Sdhaf4-deficient mice**, not DCM1GG patients. These findings are hypothesis-generating and do not justify clinical fumarate or fission-inhibitor use outside a protocol (wang2022cardiacdisruptionof pages 1-2, wang2022cardiacdisruptionof pages 10-12).

No dedicated DCM1GG clinical trial, approved gene replacement/editing therapy, ASO/siRNA therapy, or cell therapy was identified. ClinicalTrials.gov searches returned SDH-deficient oncology studies and a broad mitochondrial registry, not therapeutic DCM1GG trials; the oncology studies are not applicable to cardiomyopathy.

---

## 13. Prevention

**Primary prevention of the genotype:** carrier identification in the founder family/population, genetic counseling, partner testing, preimplantation genetic testing, prenatal diagnosis, and use of donor gametes where desired. There is no vaccine or medication preventing inheritance.

**Secondary prevention:** cascade testing followed by baseline and longitudinal ECG/echocardiography, with CMR and rhythm monitoring as appropriate. Prenatal/fetal echocardiography is reasonable in at-risk pregnancies because onset occurred as early as 32 weeks (levitas2010familialneonatalisolated pages 3-4).

**Tertiary prevention:** early treatment of ventricular dysfunction and congestion; vaccination according to routine schedules; prompt infection management; avoidance of smoking, cardiotoxic exposures, illicit stimulants, excessive alcohol, prolonged fasting/dehydration, and unsupervised intense exercise; and individualized arrhythmic/thromboembolic risk management.

Population-wide newborn screening is not established. Targeted founder/carrier screening may be reasonable only after local validation of variant frequency, analytical performance, counseling infrastructure, and community engagement.

---

## 14. Other species and natural disease

No naturally occurring animal disease specifically caused by the orthologous SDHA Gly555Glu variant was identified. Therefore, no validated breed association, VBO term, veterinary prevalence, zoonotic potential, or cross-species transmission exists. This is a noninfectious inherited disorder and is not zoonotic.

SDHA and complex-II biology are evolutionarily conserved across mammals and other eukaryotes. Comparative relevance lies in conserved succinate oxidation, electron transfer, mitochondrial energetics, and redox regulation—not in a documented naturally occurring veterinary DCM1GG syndrome.

---

## 15. Model organisms

### Available models

- **Mouse, conditional Sdhaf4 loss:** the strongest cardiac model of complex-II assembly failure. It reproduces complex-II deficiency, metabolic deterioration, excessive fission/mitophagy, progressive LV dilation/heart failure, and lethality. It enabled rescue experiments with fumarate and mitochondrial-fission inhibition (wang2022cardiacdisruptionof pages 1-2, wang2022cardiacdisruptionof pages 10-12).
- **Cellular/biochemical systems:** patient lymphoblasts, skeletal-muscle mitochondria, and postmortem myocardium demonstrate tissue-specific enzyme loss, but they are assays rather than renewable cardiomyocyte disease models (levitas2010familialneonatalisolated pages 2-3, levitas2010familialneonatalisolated pages 4-5).
- **General SDH models:** SDH-subunit knockout cell and zebrafish systems can study succinate accumulation and respiratory deficiency, but they do not reproduce the specific G555E cardiac phenotype and should be annotated as indirect.

### Limitations and priority models

The Sdhaf4 mouse disrupts an assembly factor, not SDHA Gly555Glu, and deletion may be more severe or mechanistically different from a hypomorphic missense allele. No retrieved model reproduced the human tissue-selective penetrance or the unaffected homozygous adult.

High-priority future resources are: (1) CRISPR knock-in **Sdha p.Gly555Glu** mice; (2) patient-derived iPSC ventricular cardiomyocytes and engineered heart tissues; (3) isogenic corrected controls; (4) stress challenges such as pacing, hypoxia, fever-like temperature, or nutrient limitation; and (5) single-cell/spatial multi-omics to distinguish cardiomyocyte-autonomous failure from fibroblast, vascular, and immune remodeling.

---

## Current understanding and 2023–2024 developments

The major 2023–2024 advance relevant to implementation is not a new DCM1GG cohort but the 2023 ESC cardiomyopathy framework, summarized in 2024, which makes **advanced imaging, deep phenotyping, and genetics central to family-based care** and cautions that LV noncompaction is a morphologic trait rather than necessarily a separate disease (grasso2024thenew2023 pages 1-2). The mechanistic field has advanced through cardiac complex-II models demonstrating that metabolic injury can precede structural DCM and may be partly reversible experimentally, but translation to SDHA G555E patients remains untested (wang2022cardiacdisruptionof pages 1-2, wang2022cardiacdisruptionof pages 10-12).

The key knowledge gaps are consequently substantial: modern ClinVar/gnomAD characterization of the founder allele; incidence and carrier frequency; prospective penetrance; long-term survival; arrhythmic risk; patient-derived cardiomyocyte models; direct ATP/redox/metabolomic measurements; modifier discovery; and genotype-directed therapy. Until these are addressed, authoritative interpretation should treat DCM1GG as a well-supported but extremely rare SDHA-associated founder cardiomyopathy whose numerical natural-history estimates are provisional.

References

1. (OpenTargets Search: Dilated cardiomyopathy-SDHA): Open Targets Query (Dilated cardiomyopathy-SDHA, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (levitas2010familialneonatalisolated pages 1-2): Aviva Levitas, Emad Muhammad, Gali Harel, Ann Saada, Vered Chalifa Caspi, Esther Manor, John C Beck, Val Sheffield, and Ruti Parvari. Familial neonatal isolated cardiomyopathy caused by a mutation in the flavoprotein subunit of succinate dehydrogenase. European Journal of Human Genetics, 18:1160-1165, Jun 2010. URL: https://doi.org/10.1038/ejhg.2010.83, doi:10.1038/ejhg.2010.83. This article has 142 citations and is from a domain leading peer-reviewed journal.

3. (levitas2010familialneonatalisolated pages 2-3): Aviva Levitas, Emad Muhammad, Gali Harel, Ann Saada, Vered Chalifa Caspi, Esther Manor, John C Beck, Val Sheffield, and Ruti Parvari. Familial neonatal isolated cardiomyopathy caused by a mutation in the flavoprotein subunit of succinate dehydrogenase. European Journal of Human Genetics, 18:1160-1165, Jun 2010. URL: https://doi.org/10.1038/ejhg.2010.83, doi:10.1038/ejhg.2010.83. This article has 142 citations and is from a domain leading peer-reviewed journal.

4. (levitas2010familialneonatalisolated pages 5-6): Aviva Levitas, Emad Muhammad, Gali Harel, Ann Saada, Vered Chalifa Caspi, Esther Manor, John C Beck, Val Sheffield, and Ruti Parvari. Familial neonatal isolated cardiomyopathy caused by a mutation in the flavoprotein subunit of succinate dehydrogenase. European Journal of Human Genetics, 18:1160-1165, Jun 2010. URL: https://doi.org/10.1038/ejhg.2010.83, doi:10.1038/ejhg.2010.83. This article has 142 citations and is from a domain leading peer-reviewed journal.

5. (levitas2010familialneonatalisolated pages 4-5): Aviva Levitas, Emad Muhammad, Gali Harel, Ann Saada, Vered Chalifa Caspi, Esther Manor, John C Beck, Val Sheffield, and Ruti Parvari. Familial neonatal isolated cardiomyopathy caused by a mutation in the flavoprotein subunit of succinate dehydrogenase. European Journal of Human Genetics, 18:1160-1165, Jun 2010. URL: https://doi.org/10.1038/ejhg.2010.83, doi:10.1038/ejhg.2010.83. This article has 142 citations and is from a domain leading peer-reviewed journal.

6. (levitas2010familialneonatalisolated pages 3-4): Aviva Levitas, Emad Muhammad, Gali Harel, Ann Saada, Vered Chalifa Caspi, Esther Manor, John C Beck, Val Sheffield, and Ruti Parvari. Familial neonatal isolated cardiomyopathy caused by a mutation in the flavoprotein subunit of succinate dehydrogenase. European Journal of Human Genetics, 18:1160-1165, Jun 2010. URL: https://doi.org/10.1038/ejhg.2010.83, doi:10.1038/ejhg.2010.83. This article has 142 citations and is from a domain leading peer-reviewed journal.

7. (wang2022cardiacdisruptionof pages 1-2): Xueqiang Wang, Xing Zhang, Ke Cao, Mengqi Zeng, Xuyang Fu, Adi Zheng, Feng Zhang, Feng Gao, Xuan Zou, Hao Li, Min Li, Weiqiang Lv, Jie Xu, Jiangang Long, Weijin Zang, Jinghai Chen, Feng Gao, Jian Ding, Jiankang Liu, and Zhihui Feng. Cardiac disruption of sdhaf4-mediated mitochondrial complex ii assembly promotes dilated cardiomyopathy. Nature Communications, Jul 2022. URL: https://doi.org/10.1038/s41467-022-31548-1, doi:10.1038/s41467-022-31548-1. This article has 67 citations and is from a highest quality peer-reviewed journal.

8. (wang2022cardiacdisruptionof pages 10-12): Xueqiang Wang, Xing Zhang, Ke Cao, Mengqi Zeng, Xuyang Fu, Adi Zheng, Feng Zhang, Feng Gao, Xuan Zou, Hao Li, Min Li, Weiqiang Lv, Jie Xu, Jiangang Long, Weijin Zang, Jinghai Chen, Feng Gao, Jian Ding, Jiankang Liu, and Zhihui Feng. Cardiac disruption of sdhaf4-mediated mitochondrial complex ii assembly promotes dilated cardiomyopathy. Nature Communications, Jul 2022. URL: https://doi.org/10.1038/s41467-022-31548-1, doi:10.1038/s41467-022-31548-1. This article has 67 citations and is from a highest quality peer-reviewed journal.

9. (grasso2024thenew2023 pages 1-2): Maurizia Grasso, Davide Bondavalli, Viviana Vilardo, Claudia Cavaliere, Ilaria Gatti, Alessandro Di Toro, Lorenzo Giuliani, Mario Urtis, Michela Ferrari, Barbara Cattadori, Alessandra Serio, Carlo Pellegrini, and Eloisa Arbustini. The new 2023 esc guidelines for the management of cardiomyopathies: a guiding path for cardiologist decisions. European Heart Journal Supplements : Journal of the European Society of Cardiology, 26:i1-i5, Apr 2024. URL: https://doi.org/10.1093/eurheartjsupp/suae002, doi:10.1093/eurheartjsupp/suae002. This article has 18 citations.

10. (sorella2025diagnosisandmanagement pages 12-13): Anna Sorella, Kristian Galanti, Lorena Iezzi, Sabina Gallina, Selma F Mohammed, Neha Sekhri, Mohammed Majid Akhtar, Sanjay K Prasad, Choudhary Anwar Ahmed Chahal, Fabrizio Ricci, and Mohammed Yunus Khanji. Diagnosis and management of dilated cardiomyopathy: a systematic review of clinical practice guidelines and recommendations. European Heart Journal. Quality of Care & Clinical Outcomes, 11:206-222, Dec 2025. URL: https://doi.org/10.1093/ehjqcco/qcae109, doi:10.1093/ehjqcco/qcae109. This article has 45 citations.

## Artifacts

- [Edison artifact artifact-00](Dilated_Cardiomyopathy_1GG-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| Quoted claims with nothing to check against | 1 |
| References weighed for topical relevance | 4 |
| On topic | 3 |
| Off topic | 0 |

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `DOI:10.1038/ejhg.2010.83`: "extreme phenotypic variability"
  - Reference resolved but exposes no abstract or full text to search

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 13 |
| Resolved | 13 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 2 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 1 |
| Terms whose name is worth a second look | 1 |

### Terms the report names something else

These identifiers resolve, so nothing about them looks wrong, and the ontology calls them something unrelated to what the report calls them. That usually means the identifier is not the one the sentence needs:

- `MONDO:0013339` (2 mentions) - the report calls it "if available"; MONDO calls it **dilated cardiomyopathy 1GG**

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000746` (1 mention) - the report calls it "Cell Ontology: **cardiomyocyte"; CL calls it **cardiac muscle cell**, and lists "cardiomyocyte" among its other names