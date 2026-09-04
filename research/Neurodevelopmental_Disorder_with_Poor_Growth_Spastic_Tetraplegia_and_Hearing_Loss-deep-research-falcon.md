---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-04T12:10:27.629303'
end_time: '2026-09-04T12:20:23.541210'
duration_seconds: 595.91
template_file: templates/disease_pathophysiology_research.md
template_sha: 1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666
template_variables:
  disease_name: Neurodevelopmental Disorder with Poor Growth, Spastic Tetraplegia,
    and Hearing Loss
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 7
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 40
  verified: 40
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 8
  labels_matching: 7
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Neurodevelopmental_Disorder_with_Poor_Growth_Spastic_Tetraplegia_and_Hearing_Loss-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Neurodevelopmental Disorder with Poor Growth, Spastic Tetraplegia, and Hearing Loss
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder with Poor Growth, Spastic Tetraplegia, and Hearing Loss** covering all of the
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
- **Disease Name:** Neurodevelopmental Disorder with Poor Growth, Spastic Tetraplegia, and Hearing Loss
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Neurodevelopmental Disorder with Poor Growth, Spastic Tetraplegia, and Hearing Loss** covering all of the
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


# Neurodevelopmental Disorder with Poor Growth, Spastic Tetraplegia, and Hearing Loss

## Executive summary and evidence limits

This is an ultra-rare autosomal-recessive **PSMC1-related neurodevelopmental proteasomopathy**, currently supported by one peer-reviewed family study: three affected male siblings from a consanguineous Bedouin Israeli family. The defining lesion is homozygous **PSMC1 NM_002802.3:c.983T>C, p.(Ile328Thr)**, also numbered **NM_001330212.1:c.764T>C, p.(Ile255Thr)** on an alternative transcript. All three individuals had profound developmental impairment, absent speech and ambulation, poor growth, spastic tetraplegia with central hypotonia, hearing loss, micropenis, and cryptorchidism. Accordingly, percentages below describe **3 related individuals, not population frequencies**, and should not be interpreted as stable estimates of penetrance or the full phenotypic spectrum. The primary paper was received April 28, accepted July 18, and published in 2022; PMID **35861243**, DOI [10.1111/cge.14195](https://doi.org/10.1111/cge.14195). (OpenTargets Search: Neurodevelopmental disorder with poor growth, spastic tetraplegia, and hearing loss-PSMC1, aharoni2022psmc1variantcauses pages 4-6, aharoni2022psmc1variantcauses pages 1-2)

> **Exact abstract quotation:** “We now delineate an autosomal recessive syndrome of failure to thrive, severe developmental delay and intellectual disability, spastic tetraplegia with central hypotonia, chorea, hearing loss, micropenis and undescended testes, as well as mild elevation of liver enzymes.” (aharoni2022psmc1variantcauses pages 1-2)

The following table distinguishes direct observations from model-based inference.

| Domain | Established finding | Evidence level | Ontology/database annotation |
|---|---|---|---|
| Disease identity | Neurodevelopmental disorder with poor growth, spastic tetraplegia, and hearing loss | Curated disease-level association supported by one primary family report | **MONDO:0859296**; PMID: **35861243** (OpenTargets Search: Neurodevelopmental disorder with poor growth, spastic tetraplegia, and hearing loss-PSMC1) |
| Causal gene | **PSMC1**, encoding proteasome 26S subunit ATPase 1/Rpt2, a 19S regulatory-particle AAA+ ATPase | Human genetic association plus in-vivo functional evidence | **PSMC1**; Ensembl: **ENSG00000100764** (OpenTargets Search: Neurodevelopmental disorder with poor growth, spastic tetraplegia, and hearing loss-PSMC1, aharoni2022psmc1variantcauses pages 1-2) |
| Inheritance | Autosomal recessive; variant segregated with disease in a consanguineous Bedouin Israeli family, while obligate heterozygous carriers were unaffected | Direct human pedigree, linkage, and segregation evidence | Suggested HPO: **HP:0000007** (aharoni2022psmc1variantcauses pages 7-8, aharoni2022psmc1variantcauses pages 6-7) |
| Reported population | Three affected male siblings among ten offspring of healthy consanguineous parents; ages at last examination were **3, 8, and 20 years** | Direct human case-series evidence; **n=3**, one family | Bedouin Israeli ancestry; the male-only report does not establish sex limitation (aharoni2022psmc1variantcauses pages 4-6) |
| Pathogenic variant | Homozygous **NM_002802.3:c.983T>C (p.Ile328Thr)**; alternate transcript **NM_001330212.1:c.764T>C (p.Ile255Thr)** | Direct sequencing and segregation evidence, damaging computational predictions, and in-vivo functional support | Germline missense variant; ClinVar study **RCV002291329** (OpenTargets Search: Neurodevelopmental disorder with poor growth, spastic tetraplegia, and hearing loss-PSMC1, aharoni2022psmc1variantcauses pages 6-7, aharoni2022psmc1variantcauses pages 4-6) |
| Population frequency | Variant absent from 1000 Genomes, gnomAD, AFC, an internal 553-exome database, and 84 unaffected ethnically matched tribal controls | Direct database and control screening reported in 2022; no population carrier-frequency estimate | Reported allele count **0** in the queried datasets (aharoni2022psmc1variantcauses pages 6-7, aharoni2022psmc1variantcauses pages 4-6) |
| Neurodevelopment | Severe developmental delay and intellectual disability in **3/3**; none achieved verbal communication, sitting, standing, or ambulation | Direct human evidence | Suggested HPO: **HP:0001263**, **HP:0001249**, **HP:0001344**, **HP:0000750** (aharoni2022psmc1variantcauses pages 4-6, aharoni2022psmc1variantcauses pages 1-2) |
| Motor phenotype | Spastic tetraplegia with central hypotonia in **3/3**; chorea in **2/2 assessed**, with data unavailable for the eldest sibling | Direct human evidence | Suggested HPO: **HP:0002510**, **HP:0001257**, **HP:0001290**, **HP:0002072** (aharoni2022psmc1variantcauses pages 4-6) |
| Growth and feeding | Failure to thrive or poor growth in **3/3**; PEG feeding in **2/3**. At age 20, the eldest weighed **13 kg** | Direct human evidence | Suggested HPO: **HP:0001508**, **HP:0008872**, **HP:0011968** (aharoni2022psmc1variantcauses pages 4-6) |
| Hearing | Hearing loss in **3/3**; subtype, severity, onset, laterality, and hearing-device use were not specified | Direct human evidence | Suggested HPO: **HP:0000365**; sensorineural hearing loss should not be asserted (aharoni2022psmc1variantcauses pages 4-6, aharoni2022psmc1variantcauses pages 1-2) |
| Genital/endocrine | Micropenis and undescended testes in **3/3**; low testosterone and gonadotropins in one toddler, with other anterior-pituitary axes normal | Direct human evidence | Suggested HPO: **HP:0000054**, **HP:0000028**, **HP:0000823** (aharoni2022psmc1variantcauses pages 4-6) |
| Dysmorphism | Mild dysmorphism in **3/3**, including borderline dolichocephaly or microcephaly, bushy eyebrows, flat midface, long nasal bridge, and micrognathia | Direct human evidence | Suggested HPO: **HP:0000252**, **HP:0000256**, **HP:0000574**, **HP:0011800**, **HP:0000347** (aharoni2022psmc1variantcauses pages 4-6) |
| Neuroimaging | Mild-to-moderate global ventriculomegaly and broadened extra-axial spaces in **2/2 imaged** patients; pituitary structure was normal | Direct human MRI evidence | Suggested HPO: **HP:0002119**, **HP:0012704**; brain **UBERON:0000955** (aharoni2022psmc1variantcauses pages 4-6) |
| Laboratory findings | Mild-to-moderate macrocytic anemia in **3/3** despite normal B12, folate, and TSH; neonatal cholestatic jaundice with persistent mild liver-enzyme elevation in **2/3** | Direct human laboratory evidence | Suggested HPO: **HP:0001972**, **HP:0006579**, **HP:0002910** (aharoni2022psmc1variantcauses pages 4-6) |
| Other findings | One patient had a duplicated renal collecting system and muscular ventricular septal defect; the authors cautioned that these might be unrelated | Direct observation; causal attribution **uncertain** | Suggested HPO: **HP:0000071**, **HP:0001629** (aharoni2022psmc1variantcauses pages 4-6) |
| Protein consequence | Ile328 lies in the conserved AAA+ ATPase and putative ATP-binding/hydrolysis region; modeling predicts disruption of a hydrophobic core | Structural-modeling evidence; ATPase and proteasome activity were not directly measured in patient cells | Suggested GO: **GO:0000502**, **GO:0016887**, **GO:0006511** (aharoni2022psmc1variantcauses pages 6-7, aharoni2022psmc1variantcauses pages 1-2) |
| Functional validation | Eye-specific fly **Rpt2** knockdown caused degeneration and ommatidial abnormalities; human wild-type PSMC1 nearly fully rescued these defects, whereas mutant PSMC1 rescued only partially | Direct in-vivo Drosophila evidence; the model does not reproduce the full human syndrome | **NCBITaxon:7227**; fly Rpt2 has **91.36%** protein identity to human PSMC1 (aharoni2022psmc1variantcauses pages 6-7) |
| Mechanistic inference | Partial PSMC1 dysfunction probably impairs 26S-proteasome substrate unfolding and translocation, disrupting proteostasis and neuronal development; aggregation, mitophagy, interferon, synaptic, and lipid effects remain **inferred** | Core proteasome function is established; downstream disease mechanisms derive mainly from other proteasome disorders and models | Suggested GO: **GO:0016567**, **GO:0010498**, **GO:0048666** (aharoni2022psmc1variantcauses pages 1-2, ebstein2023psmc3proteasomesubunit pages 10-12, kury2024unveilingthecrucial pages 5-8) |
| Treatment and trials | No disease-modifying therapy, approved targeted treatment, response study, or disease-specific clinical trial was identified; PEG feeding was the only documented supportive intervention | Negative trial search plus direct supportive-care observation; other multidisciplinary care is **inferred standard practice** | Suggested NCIT concepts: supportive care, gastrostomy, physical therapy, occupational therapy, and hearing rehabilitation (aharoni2022psmc1variantcauses pages 4-6, aharoni2022psmc1variantcauses pages 1-2) |


*Table: Compact summary of the genetic, clinical, mechanistic, and therapeutic evidence for PSMC1-related neurodevelopmental disorder. Direct human findings are distinguished from model-based inference and unresolved associations.*

## 1. Disease information

### Definition

The disorder is a severe, congenital/early-childhood Mendelian neurodevelopmental syndrome caused by biallelic PSMC1 dysfunction. It combines profound global developmental and motor disability with poor growth, pyramidal motor disease, central hypotonia, movement disorder, hearing loss, genital/endocrine abnormalities, and mild multisystem findings. It belongs conceptually to the emerging group of **neurodevelopmental proteasomopathies**—disorders caused by impaired proteasome-subunit function. (aharoni2022psmc1variantcauses pages 1-2, kury2024unveilingthecrucial pages 5-8)

### Identifiers and names

- **MONDO:** **MONDO:0859296**.
- **Causal target:** PSMC1; Ensembl **ENSG00000100764**; approved name *proteasome 26S subunit, ATPase 1*. OpenTargets links this disease–gene association to PMID 35861243 and ClinVar record RCV002291329. (OpenTargets Search: Neurodevelopmental disorder with poor growth, spastic tetraplegia, and hearing loss-PSMC1)
- **PMID:** **35861243**.
- **OMIM/Orphanet:** no disease-specific number was established in the retrieved evidence; do not infer one from neighboring PSMC-related disorders.
- **ICD-10/ICD-11 and MeSH:** no unique disease-specific code or heading identified. Broad coding would require component manifestations or a generic genetic/neurodevelopmental-disorder category.
- **Synonyms:** *PSMC1-related neurodevelopmental disorder*; *PSMC1-related neurological syndrome*; *autosomal-recessive PSMC1 neurodevelopmental proteasomopathy*. The publication title is “PSMC1 variant causes a novel neurological syndrome.” (aharoni2022psmc1variantcauses pages 1-2)

The evidence is aggregated at disease level from a published pedigree, but the underlying source consists of individual clinical examinations and laboratory/genetic data from one family—not EHR-derived population data. (aharoni2022psmc1variantcauses pages 4-6)

## 2. Etiology and risk/protective factors

### Causal factor

The demonstrated cause is a **germline homozygous missense PSMC1 variant**. It segregated with disease under an autosomal-recessive model in a 1.14-Mb homozygous chromosome-14 interval; the maximum multipoint LOD score was 1.95. Obligatory heterozygous relatives were clinically unaffected. (aharoni2022psmc1variantcauses pages 6-7, aharoni2022psmc1variantcauses pages 4-6)

### Genetic risk

- Two carrier parents have a 25% theoretical recurrence probability for each pregnancy, 50% carrier probability, and 25% probability of inheriting neither familial allele, assuming standard autosomal-recessive segregation.
- Consanguinity increased the probability that both parents carried the same rare ancestral allele; it is a family-level reproductive risk factor, not a cause independent of the variant.
- No susceptibility loci, modifier genes, anticipation, germline mosaicism, or protective alleles have been reported.
- The three known patients were male, but the sample provides no evidence of sex-limited biology; genital findings may simply be observable only in males. (aharoni2022psmc1variantcauses pages 7-8, aharoni2022psmc1variantcauses pages 4-6)

### Environmental and protective factors

No toxin, infection, maternal exposure, diet, lifestyle factor, occupational exposure, or gene–environment interaction has been implicated. No environmental or genetic protective factor is known. An earlier report of heterozygous 14q32.11 deletions involving PSMC1 was confounded by multiple deleted genes and, in one family, maternal heroin/tobacco exposure; it does **not** establish an environmental cause or the same disorder. (aharoni2022psmc1variantcauses pages 7-8)

## 3. Phenotypes

The principal human frequencies are:

- **Severe developmental delay/intellectual disability:** 3/3; no individual acquired verbal communication, sitting, standing, or ambulation. Suggested HPO: HP:0001263, HP:0001249, HP:0001344, HP:0000750. (aharoni2022psmc1variantcauses pages 4-6, aharoni2022psmc1variantcauses pages 1-2)
- **Spastic tetraplegia with central hypotonia:** 3/3, severe and chronic. Suggested HPO: HP:0002510, HP:0001257, HP:0001290. (aharoni2022psmc1variantcauses pages 4-6)
- **Poor growth/failure to thrive:** 3/3. The 20-year-old weighed 13 kg and required gastrostomy feeding; PEG was documented in 2/3. Suggested HPO: HP:0001508, HP:0008872, HP:0011968. (aharoni2022psmc1variantcauses pages 4-6)
- **Hearing loss:** 3/3. Onset, severity, laterality, conductive versus sensorineural type, audiometry, and device use were not reported. Suggested HPO: HP:0000365; a more specific hearing-loss term is not justified. (aharoni2022psmc1variantcauses pages 4-6)
- **Chorea:** present in both assessed younger patients; unavailable for the eldest. Suggested HPO: HP:0002072. (aharoni2022psmc1variantcauses pages 4-6)
- **Micropenis and undescended testes:** 3/3. One toddler had low testosterone and gonadotropins, with otherwise normal anterior-pituitary axes and normal pituitary structure. Suggested HPO: HP:0000054, HP:0000028, HP:0000823. (aharoni2022psmc1variantcauses pages 4-6)
- **Mild dysmorphism:** 3/3—borderline dolichocephaly/microcephaly, prominent bushy eyebrows, flat midface, long nasal bridge, and micrognathia. Suggested terms include HP:0000252/HP:0000256, HP:0000574, HP:0011800, and HP:0000347. (aharoni2022psmc1variantcauses pages 4-6)
- **Macrocytic anemia:** 3/3, mild-to-moderate, despite normal B12, folate, and TSH. Suggested HPO: HP:0001972. (aharoni2022psmc1variantcauses pages 4-6)
- **Neonatal cholestatic jaundice and residual liver-enzyme elevation:** 2/3; jaundice resolved within months. Suggested HPO: HP:0006579 and HP:0002910. (aharoni2022psmc1variantcauses pages 4-6)
- **MRI:** mild-to-moderate global ventriculomegaly and broadened extra-axial spaces in 2/2 imaged. EEG in the reported evaluation was normal. Suggested HPO: HP:0002119 and HP:0012704. (aharoni2022psmc1variantcauses pages 4-6)
- **Uncertain singleton findings:** duplicated renal collecting system and muscular ventricular septal defect in one patient; the authors cautioned these might be unrelated. (aharoni2022psmc1variantcauses pages 4-6)

No validated disease-specific quality-of-life instrument was administered. Nevertheless, absent communication and mobility, severe growth failure, PEG dependence, hearing impairment, and tetraplegia imply profound effects on self-care, participation, caregiver burden, and health-related quality of life. This functional interpretation is clinically reasonable but was not quantified in the study. (aharoni2022psmc1variantcauses pages 4-6)

## 4. Genetic and molecular information

### Gene and variant

**PSMC1** encodes a 440-amino-acid AAA+ ATPase subunit, PSMC1/Rpt2, in the base of the 19S regulatory particle of the 26S proteasome. Relevant protein accession: **NP_002793.2**. (aharoni2022psmc1variantcauses pages 6-7, aharoni2022psmc1variantcauses pages 1-2)

The pathogenic candidate is:

- **NM_002802.3:c.983T>C, p.(Ile328Thr)**;
- alternative transcript **NM_001330212.1:c.764T>C, p.(Ile255Thr)**;
- variant type: germline, homozygous missense;
- predicted damaging by SIFT and possibly damaging by PolyPhen-2;
- absent from 1000 Genomes, gnomAD, AFC, an internal 553-exome database, and 84 unaffected ethnically matched tribal controls;
- fully segregated with the phenotype by RFLP and Sanger sequencing. (aharoni2022psmc1variantcauses pages 6-7, aharoni2022psmc1variantcauses pages 4-6)

PSMC1 is highly constrained: the report gives missense Z=3.95, observed/expected missense ratio 0.28, and pLI=1; only five loss-of-function variants, none homozygous, were then present in gnomAD for ENST00000261303.8. These are gene-level constraint metrics, not variant-specific frequencies. (aharoni2022psmc1variantcauses pages 6-7)

The variant lies in the conserved AAA+ motor/putative ATP-binding and hydrolysis region. Modeling with PDB 6MSB predicts that replacing hydrophobic isoleucine with hydrophilic threonine disrupts a buried hydrophobic core. Direct ATPase activity, proteasome assembly, substrate translocation, and patient-cell proteomics were **not** measured; “hypomorphic loss of function” is therefore the best functional interpretation, not a fully demonstrated biochemical classification. (aharoni2022psmc1variantcauses pages 2-4, aharoni2022psmc1variantcauses pages 6-7)

No confirmed modifier gene, disease-associated methylation signature, somatic contribution, pathogenic CNV, translocation, inversion, or aneuploidy has been reported. Proband karyotype, chromosomal microarray, and SRY sequencing were normal. (aharoni2022psmc1variantcauses pages 4-6)

## 5. Environmental information

This is a genetic proteasomopathy. No disease-specific environmental, lifestyle, nutritional, infectious, radiation, pollution, or occupational contributor is known. Poor nutrition may worsen growth after disease onset, but it has not been shown to initiate or modify the molecular disorder. There is no zoonotic or transmissible component. (aharoni2022psmc1variantcauses pages 4-6, aharoni2022psmc1variantcauses pages 1-2)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. **Homozygous PSMC1 p.Ile328Thr leads to** substitution of a conserved hydrophobic residue within the AAA+ motor domain. (aharoni2022psmc1variantcauses pages 6-7)
2. **The substitution is predicted to lead to** destabilization of the PSMC1 hydrophobic core; this structural effect is modeled, not directly measured. (aharoni2022psmc1variantcauses pages 6-7)
3. **Altered PSMC1 likely leads to** reduced function of the 19S AAA+ ATPase ring during ATP-dependent substrate engagement, unfolding, and translocation into the 20S catalytic core; this step is mechanistically inferred for the patient allele. (aharoni2022psmc1variantcauses pages 2-4, aharoni2022psmc1variantcauses pages 1-2)
4. **Reduced 26S proteasome throughput is inferred to lead to** impaired ubiquitin-dependent proteolysis and proteostatic stress. Direct patient-cell proteasome assays are unavailable. (aharoni2022psmc1variantcauses pages 1-2, kury2024unveilingthecrucial pages 5-8)
5. **Proteostasis failure is inferred to lead to** abnormal neuronal development and/or survival, producing severe intellectual disability, central hypotonia, pyramidal dysfunction, chorea, and ventriculomegaly. PSMC1 loss causes neuronal degeneration in model systems, but the precise vulnerable human cell populations remain unknown. (aharoni2022psmc1variantcauses pages 7-8, aharoni2022psmc1variantcauses pages 6-7)
6. **The same developmental proteostasis defect probably branches to:**
   - auditory-system dysfunction → hearing loss;
   - hypothalamic–pituitary–gonadal or gonadal dysfunction → low gonadotropins/testosterone, micropenis, and cryptorchidism;
   - feeding/growth and possibly hepatic/hematopoietic dysfunction → failure to thrive, transient cholestasis, liver-enzyme elevation, and macrocytic anemia. These tissue-specific links remain inferred. (aharoni2022psmc1variantcauses pages 4-6)

### Functional evidence and current research

In flies, eye-specific Rpt2 silencing caused depigmentation, necrosis, ommatidial disorganization/fusion, abnormal ommatidial size/shape, and bristle loss. Wild-type human PSMC1 nearly fully rescued structural defects, whereas mutant PSMC1 only partially rescued them. This is strong in-vivo evidence that p.Ile328Thr impairs function, although a fly eye is not a model of the full human syndrome. (aharoni2022psmc1variantcauses pages 6-7)

Human PSMC1 and fly Rpt2 share 91.36% protein identity. Complete Psmc1 loss is embryonic lethal in mice; neuron-restricted depletion causes 26S-proteasome loss, ubiquitin/α-synuclein-positive Lewy-like inclusions, and extensive neurodegeneration, demonstrating neuronal dependence on PSMC1-mediated proteostasis. Heterozygous knockout did not produce discernible mouse-brain pathology, consistent with unaffected human carriers. (aharoni2022psmc1variantcauses pages 7-8, aharoni2022psmc1variantcauses pages 6-7)

Recent 2023–2024 work on **other** proteasomal ATPases—not the PSMC1 family—supports a broader mechanistic framework involving protein aggregation, altered dendrite/neurite development, synaptic imbalance, mitophagy, lipid metabolism, integrated stress responses, and type-I-interferon signaling. These findings are authoritative mechanistic leads but must not be entered as demonstrated PSMC1-p.Ile328Thr phenotypes. (ebstein2023psmc3proteasomesubunit pages 10-12, kury2024unveilingthecrucial pages 29-31, kury2024unveilingthecrucial pages 5-8)

Suggested annotations include GO:0000502 (proteasome complex), GO:0016887 (ATP hydrolysis activity), GO:0006511 (ubiquitin-dependent protein catabolic process), GO:0010498 (proteasomal protein catabolic process), and GO:0048666 (neuron development). Candidate cell classes—not yet directly demonstrated—include neurons (CL:0000540), upper motor neurons, neural progenitor cells, auditory sensory cells, hepatocytes, and pituitary/gonadal endocrine cells.

No disease-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, epigenomic, patient-iPSC, organoid, or CRISPR-screen dataset was identified.

## 7. Anatomical structures affected

- **Primary:** central nervous system—brain (UBERON:0000955), corticospinal/pyramidal motor systems, and motor-control circuits; MRI shows ventricular/extra-axial-space abnormalities. (aharoni2022psmc1variantcauses pages 4-6)
- **Auditory system:** hearing is affected, but the lesion was not localized to cochlea, auditory nerve, brainstem, or auditory cortex; bilateral involvement was not specified.
- **Musculoskeletal:** all four limbs are functionally affected through spastic tetraplegia; primary muscle pathology was not demonstrated.
- **Endocrine/reproductive:** penis and testes; possible hypothalamic–pituitary–gonadal involvement, although pituitary anatomy and other anterior axes were normal. (aharoni2022psmc1variantcauses pages 4-6)
- **Digestive/nutritional and liver:** severe feeding/growth impairment, PEG use, transient neonatal cholestasis, and persistent mild enzyme elevation.
- **Hematopoietic:** macrocytic anemia.
- **Renal/cardiac:** abnormalities occurred in one patient and remain of uncertain attribution. (aharoni2022psmc1variantcauses pages 4-6)

At subcellular level, the implicated structure is the cytosolic/nuclear 26S proteasome, especially its 19S regulatory-particle AAA+ ring. No patient-tissue histopathology or subcellular localization study was reported. (aharoni2022psmc1variantcauses pages 1-2)

## 8. Temporal development

The syndrome presents in infancy or early childhood, with failure to thrive and developmental impairment; two patients had neonatal cholestatic jaundice. Available ages at last examination were 3, 8, and 20 years. None acquired major motor or language milestones at any age, and the eldest remained profoundly impaired, nonambulatory, gastrostomy-fed, and severely underweight at 20 years. This establishes a chronic lifelong and severe course through early adulthood, but not whether the neurologic phenotype is primarily static, slowly progressive, or neurodegenerative. No remission, episodic pattern, formal staging system, or critical therapeutic window is known. (aharoni2022psmc1variantcauses pages 4-6)

## 9. Inheritance and population

Inheritance is autosomal recessive. Three of ten offspring of healthy consanguineous parents were affected, compatible with recessive segregation but too small a pedigree for precise penetrance estimation. Expressivity appeared broadly consistent for core features, with variation in chorea, PEG requirement, jaundice, and singleton anomalies. No anticipation or founder effect has been proven. (aharoni2022psmc1variantcauses pages 6-7, aharoni2022psmc1variantcauses pages 4-6)

No incidence, prevalence, birth prevalence, carrier frequency, geographic distribution, or reliable sex ratio is available. Only one Bedouin Israeli kindred has been documented in the disease-specific evidence. Absence of the allele from 84 tribal controls argues against a common tribal allele but does not exclude a very rare founder variant. (aharoni2022psmc1variantcauses pages 6-7, aharoni2022psmc1variantcauses pages 4-6)

## 10. Diagnostics

### Clinical recognition

The diagnostic constellation is severe early neurodevelopmental impairment, absent speech/ambulation, mixed spastic tetraplegia and central hypotonia, poor growth/feeding difficulty, hearing loss, chorea, ventriculomegaly, male genital anomalies, macrocytic anemia, and mild hepatic abnormalities—especially in siblings or a consanguineous pedigree. There are no formal clinical criteria. (aharoni2022psmc1variantcauses pages 4-6, aharoni2022psmc1variantcauses pages 1-2)

### Recommended evaluation

1. Detailed neurologic/developmental examination and three-generation pedigree.
2. Growth and nutritional assessment; swallowing/feeding evaluation.
3. Formal audiology, because the original report did not subtype hearing loss.
4. Brain MRI; EEG when seizures or episodic events are suspected, although the reported EEG was normal.
5. CBC with indices; B12, folate, thyroid testing; liver enzymes, bilirubin, and general chemistry.
6. In males, genital examination and testosterone, LH/FSH, with endocrine assessment.
7. Consider renal ultrasound and echocardiography because singleton anomalies were observed, while documenting their uncertain disease relationship. (aharoni2022psmc1variantcauses pages 4-6)

### Genetic confirmation

Trio **WES or WGS** is preferred for an undiagnosed severe syndromic neurodevelopmental disorder; analysis should include PSMC1 and other proteasome/neurodevelopmental genes, homozygosity regions, CNVs, and recessive inheritance. A neurodevelopmental, hereditary-spasticity, cerebral-palsy mimic, or hearing-loss-plus-neurodevelopmental panel containing PSMC1 is an alternative. Familial-variant Sanger testing is appropriate after diagnosis. (aharoni2022psmc1variantcauses pages 2-4, aharoni2022psmc1variantcauses pages 6-7)

CMA and karyotype can exclude competing chromosomal diagnoses but were normal in the proband and cannot detect most single-nucleotide PSMC1 variants. FISH, mitochondrial DNA, and repeat-expansion testing are not first-line for this molecular diagnosis unless the phenotype suggests an alternative. No validated RNA-seq, proteomic, metabolomic, methylation, enzyme, or circulating biomarker assay exists.

### Differential diagnosis

Important alternatives include complicated hereditary spastic paraplegias; AP-4 deficiency disorders; cerebral-palsy mimics; PSMC3-, PSMC5-, PSMD12-, PSMD11-, and PSMB1-related proteasomopathies; TRAPPC4 and SPATA5L1 disorders; mitochondrial encephalopathy; congenital disorders with deafness and severe motor impairment; and acquired perinatal brain injury. Hearing loss, genital anomalies, macrocytosis/cholestasis, recessive segregation, and the exact PSMC1 genotype help distinguish this entity. Phenotypic overlap among proteasome disorders is recognized, but the PSMC1 genital phenotype was considered unusual. (aharoni2022psmc1variantcauses pages 7-8, aharoni2022psmc1variantcauses pages 6-7, aharoni2022psmc1variantcauses pages 1-2)

## 11. Outcome and prognosis

No survival curve, mortality rate, life expectancy, hospitalization rate, or standardized quality-of-life outcome is available. Survival to age 20 was documented. Functional prognosis in the reported genotype was poor: 0/3 developed verbal communication or sitting/standing/ambulation, 2/3 required PEG feeding, and the eldest remained profoundly disabled and weighed 13 kg at age 20. Recovery or treatment-response probabilities are unknown. (aharoni2022psmc1variantcauses pages 4-6)

Likely morbidity includes severe lifelong motor and communication disability, contracture/orthopedic risk from tetraplegia, nutritional/aspiration risk, hearing-related communication barriers, and caregiver dependence. These complications are clinically plausible but were not systematically measured. No prognostic biomarker or validated genotype–phenotype model exists.

## 12. Treatment and real-world implementation

There is no approved disease-modifying, gene, RNA, cell, immune, or targeted therapy, and no disease-specific clinical trial was identified. No pharmacogenomic guidance exists. PEG feeding in two patients is the only specifically documented intervention. (aharoni2022psmc1variantcauses pages 4-6, aharoni2022psmc1variantcauses pages 1-2)

Management should therefore be individualized and multidisciplinary, explicitly recognized as extrapolated supportive care:

- nutritional and swallowing management, high-calorie support, aspiration surveillance, and gastrostomy when indicated;
- physical and occupational therapy, positioning, range-of-motion work, orthoses, mobility/seating equipment, and orthopedic surveillance;
- standard spasticity treatment where appropriate, such as oral antispastic agents, focal botulinum toxin, or specialist procedural management;
- audiologic rehabilitation, hearing aids or cochlear-implant assessment according to lesion type;
- augmentative/alternative communication and special education;
- movement-disorder review for troublesome chorea;
- endocrine/urologic management of cryptorchidism, micropenis, and hypogonadotropic findings;
- monitoring CBC and liver biochemistry.

Suggested NCIT intervention concepts include Supportive Care, Gastrostomy, Physical Therapy, Occupational Therapy, Speech/Communication Therapy, Hearing Aid, Cochlear Implantation, and Genetic Counseling. These are intervention annotations, not evidence of PSMC1-specific efficacy.

Recent paralog studies have proposed integrated-stress-response/PKR–GCN2 modulation for proteasome-associated interferon dysregulation, but this remains experimental and has not been tested in PSMC1 patients. Proteasome inhibitors would be mechanistically concerning rather than rational because they further reduce proteasome activity. (ebstein2023psmc3proteasomesubunit pages 10-12, kury2024unveilingthecrucial pages 5-8)

## 13. Prevention

The pathogenic genotype cannot presently be prevented through lifestyle or vaccination. Primary reproductive prevention options after identifying the familial variant include carrier testing of relatives, partner testing, prenatal diagnosis, and IVF with preimplantation genetic testing for monogenic disease. Secondary prevention consists of early molecular diagnosis, audiology, nutritional intervention, and developmental therapy. Tertiary prevention targets aspiration, malnutrition, contractures, pressure injury, communication deprivation, and untreated hearing/endocrine problems. These are standard genetic and disability-care strategies; none has been tested in a PSMC1-specific trial.

Genetic counseling should explain autosomal-recessive recurrence, the severe phenotype observed with the familial allele, uncertainty about the broader spectrum, and limitations of predictions for variants other than p.Ile328Thr. Cascade screening is appropriate. Population or newborn screening is not currently justified because prevalence, test performance, and disease-modifying presymptomatic treatment are unknown.

## 14. Other species and natural disease

No naturally occurring veterinary counterpart was identified, and there is no zoonotic transmission. Relevant orthologues are strongly conserved across *Mus musculus* (NCBITaxon:10090), *Drosophila melanogaster* (NCBITaxon:7227; Rpt2), *Caenorhabditis elegans* (NCBITaxon:6239), plants, and yeast. Human and fly proteins share 91.36% identity, supporting conserved proteasome function. (aharoni2022psmc1variantcauses pages 2-4, aharoni2022psmc1variantcauses pages 6-7)

Complete loss is incompatible with normal development in several organisms: mouse knockout is embryonic lethal, pan-neuronal fly knockdown prevents completion of pupation, and C. elegans Rpt2 knockdown causes lethality. These represent induced genetic models, not natural animal disease. (aharoni2022psmc1variantcauses pages 6-7)

## 15. Model organisms

- **Drosophila knockdown/rescue:** Rpt2 RNAi in the eye gives a robust degenerative morphology. Rescue by wild-type but only partial rescue by mutant human PSMC1 provides allele-level functional evidence. Limitations include tissue specificity, RNAi residual expression, overexpression of human transgenes, and absence of human growth, hearing, motor, endocrine, or hepatic phenotypes. (aharoni2022psmc1variantcauses pages 6-7)
- **Mouse complete/conditional knockout:** complete knockout is embryonic lethal. Conditional neuronal loss depletes 26S proteasomes and causes inclusions and extensive neurodegeneration; heterozygotes lack overt brain pathology. These models establish dosage-sensitive neuronal necessity but are more severe than the human hypomorphic missense state. (aharoni2022psmc1variantcauses pages 7-8, aharoni2022psmc1variantcauses pages 6-7)
- **C. elegans RNAi:** developmental and adult lethality demonstrates essential conserved function but has limited syndrome-level face validity. (aharoni2022psmc1variantcauses pages 6-7)
- **Unavailable models:** no patient-derived fibroblast proteasome study, iPSC neuron, cerebral organoid, knock-in p.Ile328Thr mouse, zebrafish allele model, or humanized model was identified.

High-priority research applications are biochemical measurement of mutant ATPase/proteasome activity, patient-derived iPSC neuronal and auditory models, p.Ile328Thr knock-in animals, longitudinal natural-history recruitment, and testing whether proteotoxic stress, mitochondrial dysfunction, synaptic imbalance, or interferon activation observed in other proteasomopathies also occurs in PSMC1 disease.

## Overall assessment

The gene–disease relationship is supported by recessive segregation, extreme rarity, evolutionary conservation, structural modeling, and an allele-sensitive in-vivo rescue assay. The clinical association is nevertheless based on one family and one homozygous allele. Core phenotype entries can be populated with relatively high confidence for that family, but epidemiology, penetrance, broader allelic spectrum, progression, hearing subtype, biochemical mechanism in human cells, prognosis, and treatment remain major knowledge gaps. Recent 2023–2024 proteasomopathy research strengthens the general proteostasis framework but should be encoded as indirect mechanistic evidence rather than as established characteristics of MONDO:0859296. (OpenTargets Search: Neurodevelopmental disorder with poor growth, spastic tetraplegia, and hearing loss-PSMC1, aharoni2022psmc1variantcauses pages 6-7, ebstein2023psmc3proteasomesubunit pages 10-12, kury2024unveilingthecrucial pages 5-8)

References

1. (OpenTargets Search: Neurodevelopmental disorder with poor growth, spastic tetraplegia, and hearing loss-PSMC1): Open Targets Query (Neurodevelopmental disorder with poor growth, spastic tetraplegia, and hearing loss-PSMC1, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (aharoni2022psmc1variantcauses pages 4-6): Sarit Aharoni, Regina Proskorovski‐Ohayon, Ramesh Kumar Krishnan, Yuval Yogev, Ohad Wormser, Noam Hadar, Anna Bakhrat, Ismael Alshafee, Maya Gombosh, Nadav Agam, Libe Gradstein, Zamir Shorer, Raz Zarivach, Marina Eskin‐Schwartz, Uri Abdu, and Ohad S. Birk. <scp><i>psmc1</i></scp> variant causes a novel neurological syndrome. Aug 2022. URL: https://doi.org/10.1111/cge.14195, doi:10.1111/cge.14195. This article has 16 citations and is from a peer-reviewed journal.

3. (aharoni2022psmc1variantcauses pages 1-2): Sarit Aharoni, Regina Proskorovski‐Ohayon, Ramesh Kumar Krishnan, Yuval Yogev, Ohad Wormser, Noam Hadar, Anna Bakhrat, Ismael Alshafee, Maya Gombosh, Nadav Agam, Libe Gradstein, Zamir Shorer, Raz Zarivach, Marina Eskin‐Schwartz, Uri Abdu, and Ohad S. Birk. <scp><i>psmc1</i></scp> variant causes a novel neurological syndrome. Aug 2022. URL: https://doi.org/10.1111/cge.14195, doi:10.1111/cge.14195. This article has 16 citations and is from a peer-reviewed journal.

4. (aharoni2022psmc1variantcauses pages 7-8): Sarit Aharoni, Regina Proskorovski‐Ohayon, Ramesh Kumar Krishnan, Yuval Yogev, Ohad Wormser, Noam Hadar, Anna Bakhrat, Ismael Alshafee, Maya Gombosh, Nadav Agam, Libe Gradstein, Zamir Shorer, Raz Zarivach, Marina Eskin‐Schwartz, Uri Abdu, and Ohad S. Birk. <scp><i>psmc1</i></scp> variant causes a novel neurological syndrome. Aug 2022. URL: https://doi.org/10.1111/cge.14195, doi:10.1111/cge.14195. This article has 16 citations and is from a peer-reviewed journal.

5. (aharoni2022psmc1variantcauses pages 6-7): Sarit Aharoni, Regina Proskorovski‐Ohayon, Ramesh Kumar Krishnan, Yuval Yogev, Ohad Wormser, Noam Hadar, Anna Bakhrat, Ismael Alshafee, Maya Gombosh, Nadav Agam, Libe Gradstein, Zamir Shorer, Raz Zarivach, Marina Eskin‐Schwartz, Uri Abdu, and Ohad S. Birk. <scp><i>psmc1</i></scp> variant causes a novel neurological syndrome. Aug 2022. URL: https://doi.org/10.1111/cge.14195, doi:10.1111/cge.14195. This article has 16 citations and is from a peer-reviewed journal.

6. (ebstein2023psmc3proteasomesubunit pages 10-12): Frédéric Ebstein, Sébastien Küry, Victoria Most, Cory Rosenfelt, Marie-Pier Scott-Boyer, Geeske M. van Woerden, Thomas Besnard, Jonas Johannes Papendorf, Maja Studencka-Turski, Tianyun Wang, Tzung-Chien Hsieh, Richard Golnik, Dustin Baldridge, Cara Forster, Charlotte de Konink, Selina M.W. Teurlings, Virginie Vignard, Richard H. van Jaarsveld, Lesley Ades, Benjamin Cogné, Cyril Mignot, Wallid Deb, Marjolijn C.J. Jongmans, F. Sessions Cole, Marie-José H. van den Boogaard, Jennifer A. Wambach, Daniel J. Wegner, Sandra Yang, Vickie Hannig, Jennifer Ann Brault, Neda Zadeh, Bruce Bennetts, Boris Keren, Anne-Claire Gélineau, Zöe Powis, Meghan Towne, Kristine Bachman, Andrea Seeley, Anita E. Beck, Jennifer Morrison, Rachel Westman, Kelly Averill, Theresa Brunet, Judith Haasters, Melissa T. Carter, Matthew Osmond, Patricia G. Wheeler, Francesca Forzano, Shehla Mohammed, Yannis Trakadis, Andrea Accogli, Rachel Harrison, Yiran Guo, Hakon Hakonarson, Sophie Rondeau, Geneviève Baujat, Giulia Barcia, René Günther Feichtinger, Johannes Adalbert Mayr, Martin Preisel, Frédéric Laumonnier, Tilmann Kallinich, Alexej Knaus, Bertrand Isidor, Peter Krawitz, Uwe Völker, Elke Hammer, Arnaud Droit, Evan E. Eichler, Ype Elgersma, Peter W. Hildebrand, François Bolduc, Elke Krüger, and Stéphane Bézieau. Psmc3 proteasome subunit variants are associated with neurodevelopmental delay and type i interferon production. Science Translational Medicine, May 2023. URL: https://doi.org/10.1126/scitranslmed.abo3189, doi:10.1126/scitranslmed.abo3189. This article has 43 citations and is from a highest quality peer-reviewed journal.

7. (kury2024unveilingthecrucial pages 5-8): Sébastien Küry, Janelle E. Stanton, Geeske van Woerden, Tzung-Chien Hsieh, Cory Rosenfelt, Marie Pier Scott-Boyer, Victoria Most, Tianyun Wang, Jonas Johannes Papendorf, Charlotte de Konink, Wallid Deb, Virginie Vignard, Maja Studencka-Turski, Thomas Besnard, Anna Marta Hajdukowicz, Franziska Thiel, Sophie Möller, Laëtitia Florenceau, Silvestre Cuinat, Sylvain Marsac, Ingrid Wentzensen, Annabelle Tuttle, Cara Forster, Johanna Striesow, Richard Golnik, Damara Ortiz, Laura Jenkins, Jill A. Rosenfeld, Alban Ziegler, Clara Houdayer, Dominique Bonneau, Erin Torti, Amber Begtrup, Kristin G. Monaghan, Sureni V. Mullegama, C.M.L. (Nienke) Volker-Touw, Koen L. I. van Gassen, Renske Oegema, Mirjam de Pagter, Katharina Steindl, Anita Rauch, Ivan Ivanovski, Kimberly McDonald, Emily Boothe, Andrew Dauber, Janice Baker, Noelle Andrea V Fabie, Raphael A. Bernier, Tychele N. Turner, Siddharth Srivastava, Kira A. Dies, Lindsay Swanson, Carrie Costin, Rebekah K. Jobling, John Pappas, Rachel Rabin, Dmitriy Niyazov, Anne Chun-Hui Tsai, Karen Kovak, David B. Beck, MCV Malicdan, David R. Adams, Lynne Wolfe, Rebecca D. Ganetzky, Colleen Muraresku, Davit Babikyan, Zdeněk Sedláček, Miroslava Hančárová, Andrew T. Timberlake, Hind Al Saif, Berkley Nestler, Kayla King, MJ Hajianpour, Gregory Costain, D’Arcy Prendergast, Chumei Li, David Geneviève, Antonio Vitobello, Arthur Sorlin, Christophe Philippe, Tamar Harel, Ori Toker, Ataf Sabir, Derek Lim, Mark Hamilton, Lisa Bryson, Elaine Cleary, Sacha Weber, Trevor L. Hoffman, Anna Maria Cueto-González, Eduardo Fidel Tizzano, David Gómez-Andrés, Marta Codina-Solà, Athina Ververi, Efterpi Pavlidou, Alexandros Lambropoulos, Kyriakos Garganis, Marlène Rio, Jonathan Levy, Sarah Jurgensmeyer, Anne M. McRae, Mathieu Kent Lessard, Maria Daniela D’Agostino, Isabelle De Bie, Meret Wegler, Rami Abou Jamra, Susanne B. Kamphausen, Viktoria Bothe, Larissa M. Busch, Uwe Völker, Elke Hammer, Kristian Wende, Benjamin Cogné, Bertrand Isidor, Jens Meiler, Amélie Bosc-Rosati, Julien Marcoux, Marie-Pierre Bousquet, Jeremie Poschmann, Frédéric Laumonnier, Peter W. Hildebrand, Evan E. Eichler, Kirsty McWalter, Peter M. Krawitz, Arnaud Droit, Ype Elgersma, Andreas M. Grabrucker, Francois V. Bolduc, Stéphane Bézieau, Frédéric Ebstein, and Elke Krüger. Unveiling the crucial neuronal role of the proteasomal atpase subunit gene psmc5 in neurodevelopmental proteasomopathies. medRxiv : the preprint server for health sciences, Jan 2024. URL: https://doi.org/10.1101/2024.01.13.24301174, doi:10.1101/2024.01.13.24301174. This article has 11 citations.

8. (aharoni2022psmc1variantcauses pages 2-4): Sarit Aharoni, Regina Proskorovski‐Ohayon, Ramesh Kumar Krishnan, Yuval Yogev, Ohad Wormser, Noam Hadar, Anna Bakhrat, Ismael Alshafee, Maya Gombosh, Nadav Agam, Libe Gradstein, Zamir Shorer, Raz Zarivach, Marina Eskin‐Schwartz, Uri Abdu, and Ohad S. Birk. <scp><i>psmc1</i></scp> variant causes a novel neurological syndrome. Aug 2022. URL: https://doi.org/10.1111/cge.14195, doi:10.1111/cge.14195. This article has 16 citations and is from a peer-reviewed journal.

9. (kury2024unveilingthecrucial pages 29-31): Sébastien Küry, Janelle E. Stanton, Geeske van Woerden, Tzung-Chien Hsieh, Cory Rosenfelt, Marie Pier Scott-Boyer, Victoria Most, Tianyun Wang, Jonas Johannes Papendorf, Charlotte de Konink, Wallid Deb, Virginie Vignard, Maja Studencka-Turski, Thomas Besnard, Anna Marta Hajdukowicz, Franziska Thiel, Sophie Möller, Laëtitia Florenceau, Silvestre Cuinat, Sylvain Marsac, Ingrid Wentzensen, Annabelle Tuttle, Cara Forster, Johanna Striesow, Richard Golnik, Damara Ortiz, Laura Jenkins, Jill A. Rosenfeld, Alban Ziegler, Clara Houdayer, Dominique Bonneau, Erin Torti, Amber Begtrup, Kristin G. Monaghan, Sureni V. Mullegama, C.M.L. (Nienke) Volker-Touw, Koen L. I. van Gassen, Renske Oegema, Mirjam de Pagter, Katharina Steindl, Anita Rauch, Ivan Ivanovski, Kimberly McDonald, Emily Boothe, Andrew Dauber, Janice Baker, Noelle Andrea V Fabie, Raphael A. Bernier, Tychele N. Turner, Siddharth Srivastava, Kira A. Dies, Lindsay Swanson, Carrie Costin, Rebekah K. Jobling, John Pappas, Rachel Rabin, Dmitriy Niyazov, Anne Chun-Hui Tsai, Karen Kovak, David B. Beck, MCV Malicdan, David R. Adams, Lynne Wolfe, Rebecca D. Ganetzky, Colleen Muraresku, Davit Babikyan, Zdeněk Sedláček, Miroslava Hančárová, Andrew T. Timberlake, Hind Al Saif, Berkley Nestler, Kayla King, MJ Hajianpour, Gregory Costain, D’Arcy Prendergast, Chumei Li, David Geneviève, Antonio Vitobello, Arthur Sorlin, Christophe Philippe, Tamar Harel, Ori Toker, Ataf Sabir, Derek Lim, Mark Hamilton, Lisa Bryson, Elaine Cleary, Sacha Weber, Trevor L. Hoffman, Anna Maria Cueto-González, Eduardo Fidel Tizzano, David Gómez-Andrés, Marta Codina-Solà, Athina Ververi, Efterpi Pavlidou, Alexandros Lambropoulos, Kyriakos Garganis, Marlène Rio, Jonathan Levy, Sarah Jurgensmeyer, Anne M. McRae, Mathieu Kent Lessard, Maria Daniela D’Agostino, Isabelle De Bie, Meret Wegler, Rami Abou Jamra, Susanne B. Kamphausen, Viktoria Bothe, Larissa M. Busch, Uwe Völker, Elke Hammer, Kristian Wende, Benjamin Cogné, Bertrand Isidor, Jens Meiler, Amélie Bosc-Rosati, Julien Marcoux, Marie-Pierre Bousquet, Jeremie Poschmann, Frédéric Laumonnier, Peter W. Hildebrand, Evan E. Eichler, Kirsty McWalter, Peter M. Krawitz, Arnaud Droit, Ype Elgersma, Andreas M. Grabrucker, Francois V. Bolduc, Stéphane Bézieau, Frédéric Ebstein, and Elke Krüger. Unveiling the crucial neuronal role of the proteasomal atpase subunit gene psmc5 in neurodevelopmental proteasomopathies. medRxiv : the preprint server for health sciences, Jan 2024. URL: https://doi.org/10.1101/2024.01.13.24301174, doi:10.1101/2024.01.13.24301174. This article has 11 citations.

## Artifacts

- [Edison artifact artifact-00](Neurodevelopmental_Disorder_with_Poor_Growth_Spastic_Tetraplegia_and_Hearing_Loss-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 40 |
| Resolved | 40 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 8 |
| Terms named correctly | 7 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `UBERON:0000955` (2 mentions) - the report calls it "Primary:** central nervous system—brain"; UBERON calls it **brain**, and lists "suprasegmental levels of nervous system" among its other names

Every term resolved, and every label the report gave matched.
