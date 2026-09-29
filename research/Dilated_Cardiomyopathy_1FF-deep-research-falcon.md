---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-09-02T17:32:29.246347'
end_time: '2026-09-02T17:45:18.254439'
duration_seconds: 769.01
template_file: templates/disease_pathophysiology_research.md
template_sha: "1e7ea4ee817acfe1dda5f77fafe6f2e8b5927666"
template_variables:
  disease_name: Dilated Cardiomyopathy 1FF
  mondo_id: ''
  category: Cardiovascular
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 11
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 3
  validator_version: 0.2.1
term_validation:
  total_terms: 38
  verified: 38
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  labels_checked: 1
  labels_matching: 0
  labels_variant: 1
  needs_review: true
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Dilated_Cardiomyopathy_1FF-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Dilated Cardiomyopathy 1FF
- **MONDO ID:**  (if available)
- **Category:** Cardiovascular

## Research Objectives

Please provide a comprehensive research report on **Dilated Cardiomyopathy 1FF** covering all of the
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
- **Disease Name:** Dilated Cardiomyopathy 1FF
- **MONDO ID:**  (if available)
- **Category:** Cardiovascular

## Research Objectives

Please provide a comprehensive research report on **Dilated Cardiomyopathy 1FF** covering all of the
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


# Dilated Cardiomyopathy 1FF: comprehensive disease-characteristics report

## Executive summary and scope

**Dilated cardiomyopathy 1FF (DCM1FF) is the autosomal-dominant TNNI3-associated dilated-cardiomyopathy phenotype, OMIM #613286.** It must not be conflated with **DCM2A (OMIM #611880)**, the increasingly well-supported, usually severe neonatal/infantile cardiomyopathy caused by **biallelic TNNI3 loss-of-function (LoF)** variants. It must also be separated from TNNI3-associated hypertrophic cardiomyopathy (HCM), restrictive cardiomyopathy (RCM), and left-ventricular noncompaction (LVNC). This distinction is clinically important because variant mechanism, inheritance, penetrance, onset, and recurrence risk differ. Heterozygous TNNI3 variants can act through haploinsufficiency, altered thin-filament regulation, or dominant-negative/gain-of-function effects; biallelic null variants can nearly abolish cardiac troponin-I expression. (sorrentino2023homozygoustnni3mutations pages 1-2, sorrentino2023homozygoustnni3mutations pages 5-8, sorrentino2023homozygoustnni3mutations pages 2-4, bollen2017genotype‐specificpathogeniceffects pages 1-4)

The evidence base for narrowly defined DCM1FF remains small. Consequently, exact disease-specific prevalence, penetrance, sex ratio, survival, phenotype frequencies, environmental modifiers, and treatment-response rates are not established. Where necessary, this report identifies evidence as **DCM1FF-specific**, **TNNI3-spectrum**, or **general genetic DCM** rather than extrapolating silently.

| Entity | Inheritance / variant mechanism | Typical onset / phenotype | Key example variants | Evidence caveat |
|---|---|---|---|---|
| **DCM1FF (OMIM 613286)** | Autosomal dominant; heterozygous **TNNI3** variants, including function-altering missense variants and reported truncation-associated haploinsufficiency | Variable-onset dilated cardiomyopathy with ventricular dilation and systolic dysfunction; penetrance and expressivity can vary within and between families | p.Arg98Ter (p.98trunc); p.Glu182Lys and p.Glu184Lys have also been listed with DCM | Very rare, with uneven variant-level evidence. Pathogenicity requires ACMG/AMP assessment using population frequency, segregation, and functional evidence. Must not be conflated with recessive infantile DCM. |
| **DCM2A (OMIM 611880)** | Autosomal recessive; biallelic **TNNI3** loss-of-function variants causing markedly reduced or absent cardiac troponin I | Severe neonatal or infantile DCM, often presenting in the first year with ventricular dilation, very low LVEF, rapidly progressive heart failure, transplantation, or death | Homozygous c.292C>T (p.Arg98Ter); c.204del (p.Arg69AlafsTer8); c.150G>A (p.Lys50=), causing abnormal splicing; contiguous deletion involving **TNNI3** | Strongest loss-of-function evidence concerns biallelic disease. Heterozygous carrier parents may be unaffected; recessive cases must not be classified as autosomal-dominant DCM1FF. |
| **Other TNNI3 cardiomyopathies: HCM, RCM, and LVNC** | Usually autosomal-dominant missense disease in HCM or RCM through gain-of-function or dominant-negative effects; recessive missense and splice variants also occur; mechanism is variant-dependent | HCM and RCM may begin in childhood or adulthood; pediatric RCM can progress rapidly and have poor prognosis. LVNC has been reported with biallelic splice variation. Intermediate and overlapping phenotypes occur. | HCM: p.Arg21Cys and p.Arg79Cys; RCM: p.Arg192Cys and homozygous p.Asp196His; LVNC: homozygous c.24+2T>A | The same gene can cause distinct phenotypes. HCM, RCM, or LVNC evidence does not automatically establish DCM1FF causality; some reported alleles remain VUS or show low penetrance. |


*Table: This table separates autosomal-dominant DCM1FF from biallelic TNNI3 loss-of-function DCM2A and other TNNI3-associated cardiomyopathies. Evidence comes from human cases, myocardial functional studies, and reviews. (sorrentino2023homozygoustnni3mutations pages 1-2, sorrentino2023homozygoustnni3mutations pages 4-5, sorrentino2023homozygoustnni3mutations pages 5-8, sorrentino2023homozygoustnni3mutations pages 2-4, bollen2017genotype‐specificpathogeniceffects pages 1-4, bollen2017genotype‐specificpathogeniceffects pages 14-18, han2025troponini– pages 7-8)*

## 1. Disease information

### Definition

DCM is conventionally defined by left-ventricular or biventricular dilation and systolic dysfunction that cannot be explained solely by coronary artery disease, hypertension, valvular disease, congenital heart disease, or other abnormal loading conditions. DCM1FF is the subset attributed to a pathogenic heterozygous variant in **TNNI3**, which encodes cardiac troponin I (cTnI), an inhibitory component of the sarcomeric thin-filament troponin complex. (sorrentino2023homozygoustnni3mutations pages 2-4, scolari2024geneticsofthe pages 3-3, sorella2025diagnosisandmanagement pages 1-2)

### Identifiers and synonyms

- **Preferred name:** Dilated cardiomyopathy 1FF
- **OMIM phenotype:** **613286**
- **Gene:** **TNNI3**, cardiac troponin I; chromosome **19q13.4**. (sorrentino2023homozygoustnni3mutations pages 2-4)
- **Synonyms:** DCM1FF; TNNI3-related autosomal-dominant dilated cardiomyopathy; cardiac troponin-I–related DCM; familial dilated cardiomyopathy due to TNNI3.
- **MONDO:** A distinct DCM1FF MONDO identifier was not established from the retrieved sources. Parent concepts appropriate for mapping are **dilated cardiomyopathy, MONDO:0005021**, and **familial dilated cardiomyopathy, MONDO:0016333**. The retrieved Open Targets result supports those parent disease records but should not be used as proof of a DCM1FF-specific MONDO mapping. (OpenTargets Search: dilated cardiomyopathy-FLNC)
- **ICD-10:** No genotype-specific code; use the jurisdiction-appropriate DCM code, commonly **I42.0**.
- **ICD-11:** No TNNI3/DCM1FF-specific code was identified; map to the dilated-cardiomyopathy category.
- **MeSH:** Cardiomyopathy, Dilated.
- **Orphanet:** No disease-specific ORPHA identifier was verified in the retrieved evidence; do not assign one without direct ORDO/Orphanet confirmation.

This report uses aggregated disease resources, published families, case reports, explanted myocardial tissue, and cohort studies—not individual EHR data. Recent HPO work supports standardized rare-disease phenotyping and EHR integration, but it does not itself supply DCM1FF phenotype frequencies. 

### Critical nomenclature correction

OMIM **#617047 is not DCM1FF**; retrieved current literature uses it for FLNC-associated familial restrictive cardiomyopathy 5. DCM1FF is **#613286 and TNNI3-associated**. This correction prevents erroneous attribution of FLNC’s high arrhythmic-risk phenotype to DCM1FF.

## 2. Etiology

### Causal factors and genetic risk

The primary lesion is a **germline TNNI3 variant** affecting cTnI quantity or function. Heterozygous missense variants can alter interactions with troponin C, troponin T, tropomyosin, or actin and may exert dominant-negative or gain-of-function effects. A heterozygous p.Arg98Ter/p.98truncation allele has been studied as haploinsufficiency in human myocardium. (sorrentino2023homozygoustnni3mutations pages 2-4, bollen2017genotype‐specificpathogeniceffects pages 1-4)

Variant interpretation must be phenotype- and mechanism-specific. The same gene causes DCM, HCM, RCM, LVNC, and intermediate phenotypes; therefore, a TNNI3 variant reported in HCM or RCM does not automatically establish DCM1FF. Variants should be assessed under ACMG/AMP principles using rarity, segregation, allelic state, functional evidence, phenotype match, and competing causes. (han2025troponini– pages 7-8, mestre2025predictionandprognostic pages 9-9, scolari2024geneticsofthe pages 3-3)

### Environmental and clinical risk modifiers

No DCM1FF-specific environmental-risk study was identified. In genetic DCM generally, pregnancy/peripartum stress, alcohol, cardiotoxic chemotherapy, and myocarditis can reveal or amplify disease in genetically predisposed people. These are plausible “second hits,” not demonstrated TNNI3-specific causal modifiers. (scolari2024geneticsofthe pages 3-3)

Other clinically relevant stressors include uncontrolled hypertension, tachyarrhythmia, ischemia, endocrine/metabolic disease, nutritional deficiency, and cardiotoxic drugs. They should be excluded as alternative or additive causes rather than assumed to be part of DCM1FF.

### Protective factors

No reproducible **genetic protective variant**, diet, supplement, medication, or exposure has been demonstrated specifically for DCM1FF. Potentially protective clinical practices are avoidance of cardiotoxins and excessive alcohol, control of blood pressure and arrhythmias, timely heart-failure therapy, and surveillance of genotype-positive relatives. These reduce acquired cardiac stress or identify disease earlier; they do not prevent inheritance.

### Gene–environment interaction

A biologically reasonable model is that impaired sarcomeric reserve reduces tolerance to hemodynamic, inflammatory, toxic, or pregnancy-associated stress, accelerating remodeling. This remains **inferred for DCM1FF**. A neonatal case was initially suspected to have myocarditis, illustrating diagnostic overlap rather than proving infection-triggered TNNI3 disease. (sorrentino2023homozygoustnni3mutations pages 4-5)

## 3. Phenotypes

Because no large DCM1FF natural-history cohort was found, frequencies below are qualitative unless otherwise stated.

- **Ventricular dilation**—clinical sign/imaging abnormality; usually left ventricular and potentially biventricular; variable onset and progressive in symptomatic disease. Suggested HPO: **Dilated cardiomyopathy (HP:0001644)**, **Left ventricular dilatation (HP:0001712)**.
- **Reduced systolic function/LVEF**—imaging/functional abnormality; mild to severe. General DCM descriptions use LVEF below approximately 40–50% as impaired, depending on diagnostic framework. Suggested HPO: **Decreased left ventricular ejection fraction (HP:0012664)**, **Left ventricular systolic dysfunction (HP:0025169)**. (sorrentino2023homozygoustnni3mutations pages 1-2)
- **Heart failure**—syndrome/signs and symptoms; exertional dyspnea, fatigue, exercise intolerance, orthopnea, edema, feeding difficulty or tachypnea in infants. Suggested HPO: **Congestive heart failure (HP:0001635)**, **Dyspnea (HP:0002094)**, **Exercise intolerance (HP:0003546)**, **Peripheral edema (HP:0012398)**.
- **Arrhythmia or conduction disease**—possible DCM complication, but DCM1FF-specific frequency and arrhythmic risk are not defined. Suggested HPO: **Cardiac arrhythmia (HP:0011675)**, **Ventricular arrhythmia (HP:0031677)**, **Palpitations (HP:0001962)**, **Syncope (HP:0001279)**. (sorrentino2023homozygoustnni3mutations pages 1-2)
- **Functional mitral/tricuspid regurgitation**—secondary to chamber/annular dilation; HPO: **Mitral regurgitation (HP:0001653)** and **Tricuspid regurgitation (HP:0005180)**. Both occurred in severe biallelic infantile cases but are not quantified in DCM1FF. (sorrentino2023homozygoustnni3mutations pages 4-5)
- **Thromboembolism/stroke**—advanced HF/device-associated complication rather than a defining phenotype. One biallelic infantile case developed ischemic stroke during mechanical support. HPO: **Thromboembolism (HP:0001907)** and **Ischemic stroke (HP:0002140)**. (sorrentino2023homozygoustnni3mutations pages 4-5)
- **Sudden cardiac death**—recognized in DCM generally, but a TNNI3-DCM1FF-specific rate is unavailable. HPO: **Sudden cardiac death (HP:0001645)**.

### Age, severity, and progression

AD DCM1FF may have variable onset and penetrance. In contrast, biallelic TNNI3-null DCM commonly presents in the first year and can progress rapidly to transplant or death. Recent examples presented at six to seven months with LVEF 25%; both required transplantation, while a separate de novo p.Glu182Lys neonatal case died shortly after discharge. (sorrentino2023homozygoustnni3mutations pages 1-2, sorrentino2023homozygoustnni3mutations pages 4-5, han2025troponini– pages 7-8)

### Quality of life

No DCM1FF-specific EQ-5D, SF-36, Kansas City Cardiomyopathy Questionnaire, or pediatric quality-of-life dataset was found. Expected burdens follow symptomatic DCM: restricted exercise and employment/school activity, recurrent hospitalization, medication and device burden, anxiety about sudden death and relatives, and transplant-related morbidity. These should be captured with validated HF instruments rather than entered as measured DCM1FF effects.

## 4. Genetic and molecular information

### Causal gene

- **TNNI3**; cardiac troponin I.
- **Protein role:** approximately 24-kDa inhibitory troponin subunit that suppresses actin–myosin interaction at low cytosolic calcium and participates in calcium-dependent activation/relaxation. (sorrentino2023homozygoustnni3mutations pages 2-4)
- **HGNC/NCBI/UniProt identifiers:** should be populated by direct database import in a production knowledge base; they were not independently verified in the retrieved excerpts.

### Variant classes and consequences

1. **Heterozygous missense:** may alter thin-filament protein interactions, calcium sensitivity, or phosphorylation-dependent regulation; mechanism can be dominant-negative or gain-of-function. Penetrance may be incomplete and variable. (sorrentino2023homozygoustnni3mutations pages 2-4)
2. **Heterozygous truncating p.Arg98Ter/p.98truncation:** human myocardium supports haploinsufficiency with reduced troponin-complex abundance and abnormal myofilament physiology. (bollen2017genotype‐specificpathogeniceffects pages 1-4, bollen2017genotype‐specificpathogeniceffects pages 14-18)
3. **Biallelic LoF:** causes a separate recessive, severe early-onset disease. Homozygous c.204del, p.Arg69AlafsTer8 produced markedly reduced TNNI3 RNA and absent protein, supporting nonsense-mediated decay. (sorrentino2023homozygoustnni3mutations pages 5-8)
4. **Splice/synonymous LoF:** biallelic splice-disrupting or intron-retaining variants can cause pediatric DCM or LVNC. (sorrentino2023homozygoustnni3mutations pages 5-8, sorrentino2023homozygoustnni3mutations pages 10-11)

Reported DCM-associated alleles in retrieved sources include p.Arg98Ter/p.98truncation, p.Glu182Lys, and p.Glu184Lys. The latter two were listed in a review-derived table, and p.Glu182Lys was reported de novo in a neonate; each requires transcript-specific HGVS normalization and ClinVar reassessment before clinical use. (bollen2017genotype‐specificpathogeniceffects pages 1-4, han2025troponini– pages 7-8)

For recessive infantile DCM, examples include **NM_000363.5:c.292C>T, p.Arg98Ter**; **c.204del, p.Arg69AlafsTer8**; **c.150G>A, p.Lys50=** with splice effect; and a contiguous deletion involving TNNI3. (sorrentino2023homozygoustnni3mutations pages 4-5, sorrentino2023homozygoustnni3mutations pages 5-8)

### Allele frequency and origin

Pathogenic Mendelian DCM alleles should generally be absent or extremely rare in ancestry-matched population databases. Exact gnomAD/TOPMed frequencies were not supplied by the retrieved evidence and should be imported variant by variant. DCM1FF variants are constitutional **germline**, not somatic cancer mutations. Both inherited and de novo TNNI3 variants occur across the broader spectrum.

### Modifier, epigenetic, and chromosomal information

No validated DCM1FF modifier gene or disease-specific DNA-methylation, histone, or chromatin signature was identified. The contiguous TNNT1/TNNI3 deletion is relevant to recessive syndromic infantile disease, not typical AD DCM1FF. Large structural variants remain possible and may require copy-number/WGS analysis when panel testing is negative.

## 5. Environmental information

No toxin, pathogen, radiation exposure, occupation, smoking pattern, diet, or lifestyle factor is sufficient to cause genetically defined DCM1FF. General DCM evaluation should nevertheless assess:

- alcohol and stimulants;
- anthracyclines and other cardiotoxic therapies;
- pregnancy/peripartum timing;
- viral or immune-mediated myocarditis;
- sustained tachyarrhythmia;
- endocrine, nutritional, metabolic, and autoimmune causes;
- hypertension and coronary disease.

Myocarditis-like episodes or infections can mimic inherited DCM, and genetic susceptibility can coexist with acquired injury. Evidence for a TNNI3-specific infectious trigger is unavailable. (sorrentino2023homozygoustnni3mutations pages 4-5, scolari2024geneticsofthe pages 3-3)

## 6. Mechanism and pathophysiology

### Ordered causal chain

1. A pathogenic germline **TNNI3** variant **leads to** reduced cTnI abundance or altered cTnI structure/function.
2. Abnormal cTnI **leads to** disturbed interaction among troponin I, troponin C, troponin T, actin, tropomyosin, and the thin filament.
3. Disturbed troponin regulation **results in** abnormal calcium sensitivity, phosphorylation response, and/or inhibitory control of actomyosin cycling.
4. These myofilament defects **lead to** inefficient contraction/relaxation and impaired length-dependent activation; the exact balance is variant-specific.
5. Chronic cardiomyocyte mechanical and energetic inefficiency **is inferred to cause** cellular stress and reduced contractile reserve.
6. This stress **leads to** adverse myocardial remodeling—myocyte dysfunction/loss, extracellular-matrix remodeling and fibrosis, and ventricular wall stress. The fibrosis branch is general DCM biology rather than directly demonstrated for every DCM1FF allele.
7. Remodeling **results in** ventricular dilation and reduced LVEF.
8. Dilation and systolic failure **lead to** neurohormonal activation, functional valve regurgitation, congestion, and clinical heart failure.
9. **Branch:** structural/electrical remodeling and calcium-handling abnormalities **may lead to** atrial or ventricular arrhythmia, syncope, thromboembolism, and sudden death; DCM1FF-specific event rates remain unknown.
10. **Biallelic branch:** two TNNI3 LoF alleles **lead to** nonsense-mediated decay or severely reduced/absent cTnI, **resulting in** much earlier, often infantile, severe DCM. (sorrentino2023homozygoustnni3mutations pages 4-5, sorrentino2023homozygoustnni3mutations pages 5-8, bollen2017genotype‐specificpathogeniceffects pages 1-4)

### Direct mechanistic evidence

**Human explanted-myocardium evidence:** in p.98trunc cardiomyocytes, troponin I, T, and C abundance was approximately **39%, 64%, and 73% of control**, respectively. Skinned cardiomyocytes had increased Ca²⁺ sensitivity and impaired length-dependent activation. Exogenous PKA did not normalize the defect, whereas exchange with recombinant wild-type troponin partly restored protein levels and normalized functional abnormalities. This supports a direct, genotype-specific troponin-complex mechanism rather than secondary end-stage remodeling alone. (bollen2017genotype‐specificpathogeniceffects pages 1-4, bollen2017genotype‐specificpathogeniceffects pages 14-18)

**Human biopsy evidence, recessive disease:** homozygous p.Arg69AlafsTer8 was associated with markedly reduced transcript and complete absence of cTnI protein, with increased fetal TNNI1 expression—consistent with nonsense-mediated decay and incomplete isoform compensation. (sorrentino2023homozygoustnni3mutations pages 5-8)

A useful short quotation from the 2017 study abstract is: **“different gene mutations induce dilated cardiomyopathy via diverse cellular pathways.”** (bollen2017genotype‐specificpathogeniceffects pages 1-4)

### Pathways, processes, cells, and ontology suggestions

- Thin-filament contraction and calcium regulation: **GO:0006941 striated muscle contraction**, **GO:0055008 cardiac muscle contraction**, **GO:0006936 muscle contraction**, **GO:0003009 skeletal muscle contraction** only if skeletal involvement is documented.
- Calcium regulation/excitation–contraction coupling: **GO:0006874 cellular calcium ion homeostasis**, **GO:0010880 regulation of release of sequestered calcium ion into cytosol by sarcoplasmic reticulum**, **GO:0086001 cardiac muscle cell action potential**.
- Sarcomere organization/remodeling: **GO:0045214 sarcomere organization**, **GO:0060048 cardiac muscle contraction**, **GO:0048738 cardiac muscle tissue development**.
- Downstream remodeling: hypertrophy, apoptosis, autophagy, oxidative stress, fibrosis, and inflammatory signaling are plausible general DCM processes but were not directly resolved in DCM1FF-specific single-cell data.
- Principal cell: **cardiac muscle cell/cardiomyocyte (CL:0000746)**. Secondary cells include cardiac fibroblasts, vascular endothelial cells, smooth-muscle cells, macrophages, and conduction-system cardiomyocytes; involvement is inferred from remodeling.

No DCM1FF-specific Wnt, MAPK, mTOR, or PI3K–AKT initiating pathway has been demonstrated. These may be downstream remodeling pathways, not the primary biochemical lesion.

### Molecular profiling and advanced technologies

Available disease-specific profiling is limited to myocardial RNA/protein abundance and contractile physiology. No validated DCM1FF-specific plasma metabolomic, lipidomic, proteomic, epigenomic, single-cell, spatial-transcriptomic, or integrated multi-omic signature was identified. Thus, such profiles should not be entered as established disease features.

## 7. Anatomical structures affected

- **Primary organ:** heart, particularly ventricular myocardium; **UBERON:0000948 heart**, **UBERON:0002084 heart left ventricle**, **UBERON:0002080 heart right ventricle**, **UBERON:0002349 myocardium**.
- **Tissue:** cardiac muscle tissue, ventricular wall, sarcomeres and thin filaments.
- **Cells:** cardiomyocytes, especially ventricular working myocytes (**CL:0000746**).
- **Subcellular:** sarcomere (**GO:0030017**), myofibril (**GO:0030016**), actin cytoskeleton (**GO:0015629**), troponin complex (**GO:0005861**), thin filament.
- **Secondary organs:** lungs in pulmonary congestion; liver, kidneys, and peripheral tissues in advanced low-output/congestive HF; brain after embolic stroke. These are complications, not primary TNNI3 targets.
- **Lateralization:** not applicable. Disease is not unilateral; left ventricular predominance is anatomical rather than body-side lateralization.

## 8. Temporal development

AD DCM1FF appears **chronic and variably penetrant**, with onset potentially from childhood to adulthood, but robust gene-specific age distributions are lacking. Disease may pass through a genotype-positive/phenotype-negative phase, subtle strain or ECG abnormalities, overt LV systolic dysfunction/dilation, symptomatic HF, and advanced HF/transplantation.

The biallelic form is different: most reported severe cases present in infancy, sometimes after apparently normal birth. In the 2023 report, symptoms began at six or seven months, followed by LVEF 25%, rapid deterioration, mechanical support, and transplant by eight months or within four months of presentation. (sorrentino2023homozygoustnni3mutations pages 4-5)

Recovery is possible through reverse remodeling under HF therapy in DCM generally, but no DCM1FF-specific remission rate exists. Even after normalized LVEF, genetic substrate persists; surveillance and usually continued therapy are prudent. Critical intervention windows are (1) presymptomatic familial surveillance, (2) early asymptomatic LV dysfunction, and (3) rapid referral for advanced HF when severe pediatric or adult deterioration occurs.

## 9. Inheritance and population

### Inheritance

- **DCM1FF:** autosomal dominant; recurrence risk is nominally 50% for each child of a heterozygous carrier, before accounting for penetrance and variant classification.
- **Biallelic TNNI3-null DCM/DCM2A:** autosomal recessive; when both parents are carriers, each pregnancy has 25% affected, 50% carrier, and 25% noncarrier risk.
- **Penetrance:** incomplete/variable and likely age-dependent for heterozygous TNNI3 variants; precise DCM1FF penetrance is unknown. (sorrentino2023homozygoustnni3mutations pages 2-4)
- **Expressivity:** variable, spanning asymptomatic carriage, DCM, HCM, RCM, or overlapping phenotypes depending on allele and mechanism.
- **Anticipation:** not established.
- **Germline mosaicism:** theoretically possible after an apparently de novo finding but not quantified.
- **Consanguinity:** relevant mainly to biallelic recessive disease. (sorrentino2023homozygoustnni3mutations pages 4-5, sorrentino2023homozygoustnni3mutations pages 5-8)

### Epidemiology

No population prevalence or incidence is available for DCM1FF itself. In genetic DCM generally, plausible genetic causes are found in approximately **10–40%** of cases; guideline synthesis estimates familial DCM at **30–50%**, with an identifiable cause in roughly **30–40% of familial cases**. Estimates vary with ascertainment and gene curation. (scolari2024geneticsofthe pages 3-3, sorella2025diagnosisandmanagement pages 1-2)

A recent Polish genetic DCM cohort attributed about **1%** of identified gene findings to TNNI3, compared with TTN 38%, MYH7 7%, FLNC and DMD 5% each, and TNNT2 3%. This is cohort composition—not TNNI3 prevalence in the general population. (chmielewski2025geneticarchitectureof pages 2-2)

No reliable DCM1FF sex ratio, ethnic disparity, geographic distribution, or carrier frequency was identified. Founder effects are established for certain TNNI3 HCM/RCM alleles, but not for DCM1FF in the reviewed evidence.

## 10. Diagnostics

### Clinical diagnostic pathway

1. **History and pedigree:** three-generation cardiac history, sudden death, transplant, HF, arrhythmia, neuromuscular disease, alcohol/toxin exposure, pregnancy, infection, and cardiotoxic treatment.
2. **Examination:** congestion, murmurs of functional regurgitation, low output, edema, hepatomegaly, growth/feeding assessment in children.
3. **ECG and ambulatory monitoring:** conduction disease, ectopy, atrial fibrillation, nonsustained ventricular tachycardia.
4. **Echocardiography:** LV and RV size/function, LVEF, global longitudinal strain, valve regurgitation, filling pressures.
5. **Cardiac MRI:** volumes, function, edema and late gadolinium enhancement/fibrosis; useful for phenotyping, differential diagnosis, and risk assessment.
6. **Laboratory tests:** BNP/NT-proBNP and high-sensitivity troponin are guideline-consensus biomarkers; CBC, electrolytes, renal/liver function, thyroid, iron, and cause-directed metabolic/infectious testing. (sorella2025diagnosisandmanagement pages 1-2)
7. **Coronary and loading-condition exclusion:** based on age/risk and clinical context.
8. **Endomyocardial biopsy:** not routine; reserve for suspected myocarditis, infiltrative/storage disease, or rapidly progressive unexplained HF when results would change management.

A 2024 ESC-guideline commentary quotes cardiomyopathies as myocardial disorders structurally and functionally abnormal **“in the absence of coronary artery disease, hypertension, valvular disease, and congenital heart disease sufficient to cause the observed myocardial abnormality.”**

### Genetic testing

Use a curated cardiomyopathy multigene panel including **TNNI3**, with deletion/duplication analysis and appropriate coverage. Trio testing is valuable in severe pediatric disease. WES/WGS is appropriate when panel testing is negative, onset is very early, the presentation is syndromic, structural/deep-intronic variants are suspected, or recessive disease is possible. Confirm clinically actionable variants by an orthogonal method and perform segregation testing. (sorrentino2023homozygoustnni3mutations pages 2-4, scolari2024geneticsofthe pages 3-3)

Do not use a VUS for predictive testing, irreversible treatment, or reproductive decisions. Reanalyze periodically as ClinVar, gnomAD, functional data, and gene-specific curation evolve. RNA studies can establish splice effects; myocardial or iPSC functional studies remain research tools.

CMA/karyotype/FISH are not first-line for isolated DCM1FF but may be appropriate for congenital anomalies, developmental delay, or suspected copy-number/chromosomal disease. Mitochondrial and repeat-expansion testing are phenotype-driven, not routine TNNI3 tests.

### Family screening

Offer genetic counseling and targeted testing to first-degree relatives after a pathogenic/likely pathogenic familial variant is established. Genotype-positive relatives require serial ECG and imaging even when asymptomatic; Holter monitoring and strain imaging can add predictive information. Genotype-negative relatives in a well-characterized P/LP family can often be released from serial genetic-family surveillance, subject to clinical judgment. A recent Dutch program found DCM in **9% at baseline** and another **10% of reevaluated relatives** over a median five years; none of 128 relatives lacking the familial P/LP variant developed DCM. These are general DCM data, not TNNI3-specific. 

### Differential diagnosis

Exclude ischemic cardiomyopathy, hypertensive or valvular remodeling, myocarditis, tachycardia-induced cardiomyopathy, peripartum cardiomyopathy, alcohol/toxin/chemotherapy injury, endocrine/metabolic/mitochondrial disease, neuromuscular disease, arrhythmogenic cardiomyopathy, LVNC, and TNNI3-related HCM/RCM. Distinguishing the latter requires imaging phenotype, diastolic physiology, allelic state, and variant-level evidence.

## 11. Outcome and prognosis

No valid DCM1FF-specific five- or ten-year survival curve exists in the retrieved literature. Prognosis should therefore be estimated from phenotype: LVEF/RV function, NYHA/Ross class, congestion, fibrosis, ventricular arrhythmia, syncope, biomarkers, treatment response, and need for mechanical support.

General pediatric cardiomyopathy data provide context only: one 2024 cohort reported DCM survival of **75.5% at five years** and **60.1% at ten years**, with NYHA/Ross III–IV predicting mortality. These figures cannot be assigned specifically to TNNI3 disease.

The recessive infantile form is often severe. In two 2023 cases, both had LVEF 25% and required transplant in infancy; one suffered stroke during support. In another neonatal p.Glu182Lys case, the child died after discharge. (sorrentino2023homozygoustnni3mutations pages 4-5, han2025troponini– pages 7-8)

Prognostic complications include progressive HF, ventricular and atrial arrhythmias, sudden death, functional regurgitation, intracardiac thrombosis/embolism, multiorgan congestion, mechanical support, and transplantation. Improvement under treatment is possible, but genetic status remains lifelong.

## 12. Treatment

### Current standard care

There is **no approved TNNI3- or DCM1FF-specific drug, RNA therapy, gene therapy, or cell therapy**. Treatment follows age-appropriate DCM/HFrEF guidelines:

- ARNI or ACE inhibitor/ARB;
- evidence-based beta blocker;
- mineralocorticoid-receptor antagonist;
- SGLT2 inhibitor in eligible HFrEF patients;
- loop diuretic for congestion;
- iron replacement for documented iron deficiency;
- anticoagulation only for standard indications such as atrial fibrillation, intracardiac thrombus, or prior embolism;
- ivabradine, hydralazine/isosorbide dinitrate, vericiguat, or digoxin in selected patients.

Suggested NCIt intervention mappings include **Pharmacologic Therapy (C15986)**, **Angiotensin Receptor–Neprilysin Inhibitor**, **Beta Adrenergic Blocker**, **Mineralocorticoid Receptor Antagonist**, **Sodium-Glucose Cotransporter 2 Inhibitor**, and **Diuretic Therapy**; production IDs should be verified against the current NCIt release.

### Devices and advanced care

- ICD for secondary prevention and phenotype-based primary prevention after individualized assessment; TNNI3 alone currently lacks a validated gene-specific ICD threshold.
- CRT for standard electrical/mechanical criteria.
- LVAD/ECMO for refractory shock or bridge to transplant/recovery.
- Heart transplantation for end-stage HF; the 2023 biallelic cases illustrate successful real-world use. (sorrentino2023homozygoustnni3mutations pages 4-5)
- Suggested NCIt terms: **Implantable Cardioverter-Defibrillator**, **Cardiac Resynchronization Therapy**, **Ventricular Assist Device**, **Extracorporeal Membrane Oxygenation**, **Heart Transplantation**.

### Rehabilitation and supportive care

Multidisciplinary HF/cardiogenetics care, sodium/fluid advice individualized to congestion, vaccination, supervised exercise/cardiac rehabilitation when stable, psychosocial care, school/work accommodations, and reproductive counseling are appropriate. Competitive/intense exercise advice should be individualized by phenotype and arrhythmia burden rather than genotype alone.

### Experimental therapy and trials

Troponin-complex replacement normalized contractile abnormalities in an ex-vivo human cardiomyocyte experiment, providing proof of mechanism—not a deliverable therapy. (bollen2017genotype‐specificpathogeniceffects pages 1-4, bollen2017genotype‐specificpathogeniceffects pages 14-18)

A ClinicalTrials.gov search retrieved no relevant TNNI3/DCM1FF-directed interventional trial. The one gene-therapy trial returned concerned Friedreich-ataxia cardiomyopathy and is not applicable. Gene replacement, allele-specific silencing, editing, and sarcomere/calcium modulators remain preclinical concepts. For dominant missense disease, the correct strategy would depend on whether the allele acts by haploinsufficiency, dominant-negative effect, or gain of function.

## 13. Prevention

### Primary prevention

The inherited allele cannot presently be prevented after conception. Reduce avoidable myocardial stress: avoid cocaine/amphetamines and cardiotoxic supplements, minimize excessive alcohol, control blood pressure and metabolic disease, review cardiotoxic chemotherapy risk, and seek early assessment for pregnancy-associated or infectious cardiac symptoms. Evidence is general DCM prevention, not DCM1FF-specific.

### Secondary prevention

- Cascade genetic testing after identification of a familial P/LP variant.
- Serial ECG, echocardiography/strain, and rhythm monitoring in carriers.
- Prompt therapy for asymptomatic LV dysfunction or overt HF.
- Consider CMR for uncertain or evolving phenotype.

Family-screening evidence indicates earlier detected LV dysfunction has better outcomes than disease detected outside screening programs, supporting surveillance as a clinically meaningful preventive implementation. (mestre2025predictionandprognostic pages 9-9)

### Tertiary prevention

Continue guideline-directed therapy, prevent decompensation, treat arrhythmias and thromboembolic risk, vaccinate against respiratory infections, provide rehabilitation, and refer early for device or advanced-HF evaluation when indicated.

### Reproductive prevention/counseling

Offer preconception counseling, prenatal diagnosis, or PGT-M after a familial pathogenic variant is established. Counseling must distinguish the 50% transmission risk of AD DCM1FF from the 25% affected risk when both parents carry a recessive TNNI3 LoF allele. A VUS is inadequate for PGT-M or predictive testing.

## 14. Other species and natural disease

- **Human:** *Homo sapiens*, NCBI Taxon **9606**.
- Common research ortholog systems include mouse (*Mus musculus*, **10090**), rat (*Rattus norvegicus*, **10116**), and zebrafish (*Danio rerio*, **7955**).

TNNI3/cardiac troponin-I function is evolutionarily conserved across vertebrates, supporting mechanistic models. However, no well-validated naturally occurring companion-animal or livestock disease specifically homologous to human DCM1FF was identified. Accordingly, no breed/VBO association should be assigned. The disorder is not infectious, transmissible, or zoonotic.

## 15. Model organisms and experimental systems

### Human myocardial models

The strongest DCM1FF mechanism evidence comes from explanted human LV tissue and membrane-permeabilized cardiomyocytes carrying p.98trunc. Strengths are native adult sarcomere context and direct contractile measurement; limitations include end-stage remodeling, small sample size, and inability to model presymptomatic progression. Recombinant wild-type troponin exchange supplied a causal rescue experiment. (bollen2017genotype‐specificpathogeniceffects pages 1-4, bollen2017genotype‐specificpathogeniceffects pages 14-18)

### Human biopsy models of recessive disease

RNA and protein studies in p.Arg69AlafsTer8 myocardium showed reduced transcript and absent cTnI, directly demonstrating LoF. This models DCM2A, not AD DCM1FF. (sorrentino2023homozygoustnni3mutations pages 5-8)

### iPSC-derived cardiomyocytes and engineered tissue

TNNI3-mutant iPSC-cardiomyocytes and engineered heart tissues can examine calcium sensitivity, relaxation, contractile force, sarcomere organization, drug response, and gene correction. Advantages include human genetic background and isogenic CRISPR controls. Limitations include fetal-like maturation, altered TNNI isoform expression, lack of adult loading and multicellular architecture, and incomplete modeling of fibrosis, immunity, and long-term arrhythmia.

### Mouse and zebrafish models

Transgenic/knock-in mice and zebrafish are used across the TNNI3/troponin cardiomyopathy spectrum. They permit in-vivo hemodynamic, arrhythmic, developmental, and survival studies, but phenotype direction can differ by variant, species, dosage, developmental stage, and background. No single model retrieved here fully recapitulates human AD DCM1FF natural history. (han2025troponini– pages 7-8)

### Omics/model gaps

No DCM1FF-specific organoid, single-cell atlas, spatial transcriptomic map, systematic CRISPR screen, or validated multi-omic biomarker panel was identified. These are high-priority research gaps, along with prospective registries that separate heterozygous DCM1FF from biallelic DCM2A and other TNNI3 phenotypes.

## Evidence appraisal and current research priorities

The most persuasive disease-specific evidence is human myocardial physiology demonstrating p.98trunc-associated haploinsufficiency and functional rescue. Recent 2023 literature substantially strengthens a **different** relationship—biallelic TNNI3 LoF with lethal or transplant-requiring infantile DCM. (sorrentino2023homozygoustnni3mutations pages 4-5, sorrentino2023homozygoustnni3mutations pages 5-8, bollen2017genotype‐specificpathogeniceffects pages 1-4)

Priority needs are: a curated transcript-specific variant registry; segregation and penetrance studies; ancestry-diverse population controls; longitudinal ECG/CMR/strain phenotyping; direct comparison of AD missense, AD truncating, and biallelic LoF mechanisms; mature isogenic engineered-heart-tissue models; and genotype-specific therapeutic studies. Until those data exist, diagnosis should be variant-level and phenotype-led, and management should follow contemporary inherited-DCM and HF guidance rather than assuming a uniform “TNNI3 cardiomyopathy” prognosis.

References

1. (sorrentino2023homozygoustnni3mutations pages 1-2): Ugo Sorrentino, Ilaria Gabbiato, Chiara Canciani, Davide Calosci, Chiara Rigon, Daniela Zuccarello, and Matteo Cassina. Homozygous tnni3 mutations and severe early onset dilated cardiomyopathy: patient report and review of the literature. Mar 2023. URL: https://doi.org/10.3390/genes14030748, doi:10.3390/genes14030748. This article has 19 citations.

2. (sorrentino2023homozygoustnni3mutations pages 5-8): Ugo Sorrentino, Ilaria Gabbiato, Chiara Canciani, Davide Calosci, Chiara Rigon, Daniela Zuccarello, and Matteo Cassina. Homozygous tnni3 mutations and severe early onset dilated cardiomyopathy: patient report and review of the literature. Mar 2023. URL: https://doi.org/10.3390/genes14030748, doi:10.3390/genes14030748. This article has 19 citations.

3. (sorrentino2023homozygoustnni3mutations pages 2-4): Ugo Sorrentino, Ilaria Gabbiato, Chiara Canciani, Davide Calosci, Chiara Rigon, Daniela Zuccarello, and Matteo Cassina. Homozygous tnni3 mutations and severe early onset dilated cardiomyopathy: patient report and review of the literature. Mar 2023. URL: https://doi.org/10.3390/genes14030748, doi:10.3390/genes14030748. This article has 19 citations.

4. (bollen2017genotype‐specificpathogeniceffects pages 1-4): Ilse A. E. Bollen, Maike Schuldt, Magdalena Harakalova, Aryan Vink, Folkert W. Asselbergs, Jose R. Pinto, Martina Krüger, Diederik W. D. Kuster, and Jolanda van der Velden. Genotype‐specific pathogenic effects in human dilated cardiomyopathy. The Journal of Physiology, 595:4677-4693, Jun 2017. URL: https://doi.org/10.1113/jp274145, doi:10.1113/jp274145. This article has 50 citations.

5. (sorrentino2023homozygoustnni3mutations pages 4-5): Ugo Sorrentino, Ilaria Gabbiato, Chiara Canciani, Davide Calosci, Chiara Rigon, Daniela Zuccarello, and Matteo Cassina. Homozygous tnni3 mutations and severe early onset dilated cardiomyopathy: patient report and review of the literature. Mar 2023. URL: https://doi.org/10.3390/genes14030748, doi:10.3390/genes14030748. This article has 19 citations.

6. (bollen2017genotype‐specificpathogeniceffects pages 14-18): Ilse A. E. Bollen, Maike Schuldt, Magdalena Harakalova, Aryan Vink, Folkert W. Asselbergs, Jose R. Pinto, Martina Krüger, Diederik W. D. Kuster, and Jolanda van der Velden. Genotype‐specific pathogenic effects in human dilated cardiomyopathy. The Journal of Physiology, 595:4677-4693, Jun 2017. URL: https://doi.org/10.1113/jp274145, doi:10.1113/jp274145. This article has 50 citations.

7. (han2025troponini– pages 7-8): Dongju Han, Younghyun Lim, Soah Lee, and Seong-il Eyun. Troponin i – a comprehensive review of its function, structure, evolution, and role in muscle diseases. Animal Cells and Systems, 29:446-468, Jul 2025. URL: https://doi.org/10.1080/19768354.2025.2533821, doi:10.1080/19768354.2025.2533821. This article has 9 citations and is from a peer-reviewed journal.

8. (scolari2024geneticsofthe pages 3-3): Fernando Luis Scolari, Henrique Iahnke Garbin, Thais Mariel Andara Beuren, Felipe Cerqueira Matheus, Ricardo Mourilhe-Rocha, and Marcelo Imbroinise Bittencourt. Genetics of the cardiomyopathies: a review for the cardiologist. ABC Heart Fail Cardiomyop, Oct 2024. URL: https://doi.org/10.36660/abchf.20240047i, doi:10.36660/abchf.20240047i. This article has 3 citations.

9. (sorella2025diagnosisandmanagement pages 1-2): Anna Sorella, Kristian Galanti, Lorena Iezzi, Sabina Gallina, Selma F Mohammed, Neha Sekhri, Mohammed Majid Akhtar, Sanjay K Prasad, Choudhary Anwar Ahmed Chahal, Fabrizio Ricci, and Mohammed Yunus Khanji. Diagnosis and management of dilated cardiomyopathy: a systematic review of clinical practice guidelines and recommendations. European Heart Journal. Quality of Care & Clinical Outcomes, 11:206-222, Dec 2025. URL: https://doi.org/10.1093/ehjqcco/qcae109, doi:10.1093/ehjqcco/qcae109. This article has 45 citations.

10. (OpenTargets Search: dilated cardiomyopathy-FLNC): Open Targets Query (dilated cardiomyopathy-FLNC, 7 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

11. (mestre2025predictionandprognostic pages 9-9): Eva Del Mestre, Alessia Paldino, Carola Pio Loco Detto Gava, Ilaria Gandin, Marta Gigli, Davide Stolfo, Martina Setti, Giovanni Maria Severini, Beatrice Spedicati, Stefania Lenarduzzi, Giorgia Girotto, Alessandro Folgheraiter, Jacopo Giulio Rizzi, Renata Korcova, Luisa Mestroni, Marco Merlo, Matteo Dal Ferro, and Gianfranco Sinagra. Prediction and prognostic role of left ventricular systolic dysfunction in family screening for dilated cardiomyopathy and non-dilated left ventricular cardiomyopathy. European journal of heart failure, Apr 2025. URL: https://doi.org/10.1002/ejhf.3657, doi:10.1002/ejhf.3657. This article has 6 citations and is from a highest quality peer-reviewed journal.

12. (sorrentino2023homozygoustnni3mutations pages 10-11): Ugo Sorrentino, Ilaria Gabbiato, Chiara Canciani, Davide Calosci, Chiara Rigon, Daniela Zuccarello, and Matteo Cassina. Homozygous tnni3 mutations and severe early onset dilated cardiomyopathy: patient report and review of the literature. Mar 2023. URL: https://doi.org/10.3390/genes14030748, doi:10.3390/genes14030748. This article has 19 citations.

13. (chmielewski2025geneticarchitectureof pages 2-2): P. Chmielewski, G. Truszkowska, G. Kostrzewa, Ewa Michalak, P. Stawiński, Ilona Kowalik, Ilona Minota, Przemysław Leszek, Łukasz Mazurkiewicz, Jolanta Krzysztoń-Russjan, Rafał Płoski, and Z. Bilińska. Genetic architecture of dilated cardiomyopathy in poland: variant distribution, clinical characteristics and prognosis. Polish archives of internal medicine, Aug 2025. URL: https://doi.org/10.20452/pamw.17083, doi:10.20452/pamw.17083. This article has 4 citations.

## Artifacts

- [Edison artifact artifact-00](Dilated_Cardiomyopathy_1FF-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

Checked with `linkml-term-validator` 0.4.5, through the `ols:` adapter.

| Outcome | Count |
| --- | --- |
| Terms checked | 38 |
| Resolved | 38 |
| Unresolved (possible confabulation) | 0 |
| Obsolete | 0 |
| Unverifiable | 0 |
| Terms whose name was checked | 1 |
| Terms named correctly | 0 |
| Terms named as a **different** term | 0 |
| Terms whose name is worth a second look | 1 |

### Terms whose name is worth a second look

The report's name for these is recognisably related to the term's own name without being one of them. A loose paraphrase reads the same way as a citation of the wrong sibling term - and so does a *related* synonym, which the ontology records precisely because it names something adjacent rather than the same thing - so these are listed rather than judged:

- `CL:0000746` (2 mentions) - the report calls it "Principal cell: **cardiac muscle cell/cardiomyocyte"; CL calls it **cardiac muscle cell**

Every term resolved, and every label the report gave matched.