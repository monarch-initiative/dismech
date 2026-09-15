---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-18T21:02:13.419441'
end_time: '2026-08-18T21:10:37.983834'
duration_seconds: 504.57
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Familial Defective Apolipoprotein B-100
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 21
reference_validation:
  total_references: 9
  verified: 8
  not_found: 1
  unverifiable: 0
  confabulation_rate: 0.111
  quotes_checked: 1
  quotes_valid: 1
  relevance_assessed: 8
  on_topic: 6
  unresolved_references:
  - DOI:10.5551/jat.CR005](https://doi.org/10.5551/jat.CR005
  needs_review: true
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Familial_Defective_Apolipoprotein_B-100-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Familial Defective Apolipoprotein B-100
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Familial Defective Apolipoprotein B-100** covering all of the
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
- **Disease Name:** Familial Defective Apolipoprotein B-100
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Familial Defective Apolipoprotein B-100** covering all of the
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


# Familial Defective Apolipoprotein B-100: Disease-Characteristics Report

## Executive summary and evidence boundaries

Familial defective apolipoprotein B-100 (FDB) is a Mendelian, usually autosomal-dominant/codominant hypercholesterolemia caused by **ligand-defective APOB**. The prototypic allele is **APOB c.10580G>A, p.Arg3527Gln**, historically called **R3500Q**; p.Arg3527Trp/R3500W is another established allele. Defective apoB-100 binding to hepatic LDL receptor (LDLR) reduces LDL clearance, causing lifelong elevation of LDL cholesterol (LDL-C) and cumulative atherosclerotic cardiovascular risk. FDB is now commonly classified as **APOB-related familial hypercholesterolemia (FH)** rather than managed as a separate clinical syndrome. On average it is milder and less penetrant than LDLR-related FH, but coronary disease and myocardial infarction can still occur prematurely. (kounatidis2024apob100andatherosclerosis pages 13-14, kounatidis2024apob100andatherosclerosis pages 11-13)

Evidence below is labeled implicitly by scope: statements about the apoB-binding defect and comparative FDB cohorts are **FDB-specific human evidence**; management targets, diagnostic criteria, and many risk modifiers are **general FH evidence extrapolated to molecularly confirmed FDB**. Recent disease-specific evidence is limited; the most directly relevant recent synthesis is Kounatidis et al., published February 2024, DOI [10.3390/metabo14020123](https://doi.org/10.3390/metabo14020123). (kounatidis2024apob100andatherosclerosis pages 13-14)

The following compact table summarizes knowledge-base-ready assertions and their principal caveats.

| domain | curated finding | suggested ontology/identifier | evidence scope/caveat |
|---|---|---|---|
| Disease identity | Familial defective apolipoprotein B-100 (FDB) is an inherited ligand-defective APOB disorder characterized by hypercholesterolemia and premature atherosclerosis; often treated clinically within the APOB-related familial hypercholesterolemia spectrum. | Disease label: Familial defective apolipoprotein B-100; consider MONDO/Orphanet/OMIM cross-map, verify current release | Disease-specific review supports identity, but many modern sources subsume FDB under broader familial hypercholesterolemia (FH) rather than list it separately (kounatidis2024apob100andatherosclerosis pages 11-13, kounatidis2024apob100andatherosclerosis pages 13-14, haradashiba2023guidelinesforthe pages 2-4) |
| Synonyms / naming | Common names include FDB, familial defective apoB-100, APOB-related familial hypercholesterolemia, ligand-defective apoB hypercholesterolemia. Legacy residue numbering uses R3500Q/R3500W; current full-length APOB numbering uses p.Arg3527Gln / p.Arg3527Trp. | APOB gene (HGNC: APOB label; verify HGNC ID/current transcript) | Important curation issue: legacy codon 3500 and current codon 3527 refer to the same canonical disease hotspot under different numbering systems (siddiqi2026familialhypercholesterolemiastateoftheart pages 3-4, haradashiba2023guidelinesforthe pages 24-25) |
| Causal gene / variant hotspot | Core causal gene is APOB; the best-established pathogenic variant is p.Arg3527Gln (legacy R3500Q). p.Arg3527Trp (legacy R3500W) is the second most common FDB mutation; additional nearby APOB exon 26 variants are reported. | Gene: APOB; variant labels: p.Arg3527Gln, p.Arg3527Trp; ClinVar/ClinGen/HGVS mapping recommended | Disease-specific review reports ~35 FH-causing APOB variants overall; exact pathogenicity for rarer nearby variants should be checked in ClinVar/ClinGen (kounatidis2024apob100andatherosclerosis pages 13-14, siddiqi2026familialhypercholesterolemiastateoftheart pages 3-4) |
| Inheritance | Usually autosomal codominant / autosomal dominant in clinical practice, with dose effect between heterozygous and rare homozygous states. | HPO inheritance term: Autosomal dominant inheritance / codominant qualifier, verify preferred ontology usage | Source wording varies: recent apoB review uses “autosomal codominant,” while FH guidelines often simplify dominant FH inheritance (kounatidis2024apob100andatherosclerosis pages 11-13, haradashiba2023guidelinesforthe pages 2-4) |
| Core laboratory phenotype | Lifelong elevation of LDL-C is the hallmark; the R3500Q variant increases serum LDL-C by about 60–70 mg/dL. ApoB-containing LDL particles accumulate because hepatic clearance is impaired. | HPO labels: Hypercholesterolemia, Increased LDL cholesterol level; LOINC/NCIT lipid panel terms, verify current release | Quantitative increase is variant-specific and may be modified by background genetics and environment (kounatidis2024apob100andatherosclerosis pages 13-14, kounatidis2024apob100andatherosclerosis pages 11-13, siddiqi2026familialhypercholesterolemiastateoftheart pages 3-4) |
| Clinical phenotype | May present with hyper-LDL cholesterolemia, premature coronary disease, and sometimes xanthomas/coronary artery calcification, but phenotype is often milder than classic LDLR-mediated FH. | HPO labels: Premature coronary artery disease, Coronary artery calcification, Tendon xanthoma, Myocardial infarction | Much of the visible-xanthoma literature comes from broader FH cohorts; FDB-specific severity is generally lower/variable (kounatidis2024apob100andatherosclerosis pages 13-14, haradashiba2023guidelinesforthe pages 8-11) |
| Complications | FDB is associated with coronary artery disease, ischemic heart disease, myocardial infarction, and coronary artery calcification. Comparative data suggest lower CHD prevalence and later onset than classic FH: 5.6% CHD at median age 52 in FDB vs 40% at mean age 41 in FH; carotid stenosis 4% vs 15%. | HPO labels: Coronary artery disease, Myocardial infarction, Carotid artery stenosis | These comparative risk figures are disease-informative but derive from FDB-vs-FH comparison rather than population prevalence estimates (kounatidis2024apob100andatherosclerosis pages 13-14) |
| Molecular mechanism | ApoB100 normally serves as an LDL receptor ligand. Pathogenic APOB hotspot variants reduce apoB100 binding affinity to LDLR, lowering LDL uptake/clearance by hepatocytes and increasing circulating LDL; excess LDL is retained/oxidized in arterial intima, triggering foam-cell inflammation and plaque formation. | GO labels: low-density lipoprotein particle receptor binding, receptor-mediated endocytosis, cholesterol homeostasis, foam cell differentiation, inflammatory response; Reactome/KEGG LDL metabolism pathways, verify current release | Upstream defect is FDB-specific (apoB-LDLR binding); downstream atherogenesis steps are general apoB/LDL biology extrapolated from atherosclerosis literature (kounatidis2024apob100andatherosclerosis pages 11-13, kounatidis2024apob100andatherosclerosis pages 4-5, kounatidis2024apob100andatherosclerosis pages 5-7) |
| Anatomy / cells | Primary organs/systems: liver and arterial vasculature; target tissues include arterial intima and atherosclerotic plaque. Key cells: hepatocytes, endothelial cells, monocytes/macrophages, vascular smooth muscle cells, CD4+ T cells. | UBERON labels: liver, blood vessel, carotid artery, coronary artery; CL labels: hepatocyte, endothelial cell, macrophage, smooth muscle cell, CD4-positive T cell; GO cellular components/pathways verify current release | Cell-level cascade is derived mainly from apoB atherosclerosis biology rather than FDB-only experiments (kounatidis2024apob100andatherosclerosis pages 4-5, kounatidis2024apob100andatherosclerosis pages 5-7) |
| Diagnosis | Suspect in patients with elevated untreated LDL-C and family history of premature CAD/FH; distinguish from LDLR-mediated FH and secondary dyslipidemia. Genetic testing for APOB variants is confirmatory. FH diagnostic frameworks use untreated LDL-C thresholds (e.g., ≥180 mg/dL in Japanese adult criteria) plus xanthomas/family history, and recommend cascade screening. | Disease/gene testing: APOB sequencing or FH multigene panel (APOB, LDLR, PCSK9, LDLRAP1); clinical criteria labels: Dutch Lipid Clinic Network, Simon Broome, MEDPED, JAS adult FH criteria | No FDB-specific modern standalone diagnostic criteria were identified; current practice usually diagnoses under FH algorithms and then subtypes genetically (haradashiba2023guidelinesforthe pages 8-11, haradashiba2023guidelinesforthe pages 2-4, haradashiba2023guidelinesforthe pages 24-25) |
| Differential diagnosis | Main differential diagnoses are LDLR-related FH, PCSK9-related FH, LDLRAP1-related hypercholesterolemia, polygenic hypercholesterolemia, elevated Lp(a)-driven LDL-C signal, and secondary dyslipidemias. | Disease labels as above; consider Lp(a), sitosterolemia, hypothyroidism, nephrotic syndrome, cholestatic liver disease, verify coding system | Differential structure comes mostly from general FH guidance, not FDB-specific cohorts (siddiqi2026familialhypercholesterolemiastateoftheart pages 1-2, faiz2012molecularpathologyof pages 4-5, haradashiba2023guidelinesforthe pages 8-11) |
| Treatment | Managed similarly to heterozygous FH: lifestyle intervention, high-intensity statin first line, usually plus ezetimibe; consider PCSK9 inhibitors, inclisiran, bempedoic acid, and lipoprotein apheresis if targets are not reached. General FH targets include ≥50% LDL-C reduction and LDL-C <70 mg/dL for primary prevention or <55 mg/dL for very-high-risk patients. | NCIT labels: statin therapy, ezetimibe, PCSK9 inhibitor therapy, inclisiran, bempedoic acid, lipoprotein apheresis; CHEBI/DrugBank mapping verify current release | Evidence is mostly general FH guidance; a caveat for FDB is that LDLR is structurally normal, so response patterns may differ from LDLR-negative FH, but modern management still follows FH algorithms (fularski2024unveilingfamilialhypercholesterolemia—review pages 7-9, siddiqi2026familialhypercholesterolemiastateoftheart pages 1-2, kounatidis2024apob100andatherosclerosis pages 13-14) |
| Prevention / screening | Cascade screening of relatives is recommended after identifying an index case; early diagnosis reduces cumulative LDL exposure and premature CAD risk. Lifestyle measures include Mediterranean-style diet and aerobic exercise, which can lower apoB-related risk markers. | Public health labels: cascade screening; HPO/family history terms; behavioral intervention terms verify current release | Screening and prevention evidence is mainly general FH implementation evidence, applicable to APOB-FDB because of shared inherited LDL burden (haradashiba2023guidelinesforthe pages 2-4, kounatidis2024apob100andatherosclerosis pages 13-14) |
| Prognosis | Untreated FDB increases atherosclerotic risk, but available comparative evidence suggests lower severity than classic FH on average. Expressivity is variable and can be worsened by additional genetic hits or conventional cardiovascular risk factors. | Prognostic feature labels: premature CAD risk, variable expressivity, incomplete penetrance | Specific long-term survival estimates for pure FDB were not identified in retrieved recent sources (kounatidis2024apob100andatherosclerosis pages 13-14, siddiqi2026familialhypercholesterolemiastateoftheart pages 3-4, kamar2021thedigeniccausality pages 14-15) |
| Modifiers | Phenotype may be modified by smoking, diabetes, hypertension, low HDL-C, high TG, obesity/insulin resistance, and other lipid genes or digenic states. | HPO/ExO/environmental exposure labels; modifier genes to verify per case | Most modifier evidence is from broader FH rather than FDB-only cohorts; use cautiously when curating disease-specific assertions (haradashiba2023guidelinesforthe pages 8-11, kamar2021thedigeniccausality pages 14-15) |
| Models / other species | Relevant experimental systems include human APOB100 transgenic or knock-in atherosclerosis models and pathway models such as Ldlr-/- or Apoe-based mice, but these are not exact allele-faithful FDB models. No naturally occurring veterinary FDB equivalent was identified in retrieved sources. | Model labels: human APOB100 transgenic mouse; LDLR knockout mouse; APOE-related atherosclerosis mouse, verify model database accession | Useful for mechanism and drug testing, but limited for direct genotype-phenotype recapitulation of APOB p.Arg3527Gln FDB (zadelaar2007mousemodelsfor pages 3-4) |
| Evidence gaps | Uncertain/needs verification: exact MONDO/Orphanet/OMIM mapping for FDB as a distinct entity, current ClinVar classifications for all rare APOB hotspot-adjacent variants, precise prevalence/incidence of pure FDB by ancestry, penetrance estimates, QoL data, and disease-specific animal models. | Use ontology labels only and verify current release before database loading | Modern literature often collapses FDB into APOB-related FH, so separate disease-level curation requires careful source labeling (kounatidis2024apob100andatherosclerosis pages 13-14, siddiqi2026familialhypercholesterolemiastateoftheart pages 1-2, haradashiba2023guidelinesforthe pages 24-25) |


*Table: This table provides a compact curation-oriented summary of Familial Defective Apolipoprotein B-100, covering disease identity, variant hotspot, phenotype, mechanism, diagnosis, treatment, anatomy, and key evidence gaps. It is designed to support structured knowledge-base entry building while flagging where broader FH evidence is being extrapolated to FDB.*

## 1. Disease information

### Definition

FDB is an inherited disorder in which apoB-100 on LDL has reduced affinity for LDLR. The resulting under-clearance of LDL produces hypercholesterolemia and premature atherosclerosis. A recent review defines it as an “**inherited autosomal codominant disorder characterized by hypercholesterolemia and premature atherosclerosis**.” (kounatidis2024apob100andatherosclerosis pages 11-13)

### Identifiers and synonyms

- **Preferred name:** familial defective apolipoprotein B-100.
- **Synonyms:** familial defective apoB-100; FDB; ligand-defective apolipoprotein B; APOB-related familial hypercholesterolemia; familial hypercholesterolemia type 2 due to APOB.
- **OMIM:** commonly mapped to **144010, Hypercholesterolemia, familial, 2 (FHCL2)**; **APOB gene OMIM 107730**. Database release should be verified before ingestion.
- **Orphanet:** commonly represented within familial hypercholesterolemia rather than consistently as a separate current disorder; verify the live Orphanet release.
- **MONDO:** use the current MONDO entry for *familial hypercholesterolemia due to ligand-defective apolipoprotein B* if present; exact live identifier could not be independently verified from the retrieved corpus.
- **ICD-10-CM:** **E78.01 Familial hypercholesterolemia**; no FDB-specific code.
- **ICD-11:** use the familial hypercholesterolaemia entity under disorders of lipoprotein metabolism; no allele-specific FDB code was established here.
- **MeSH:** *Hyperlipoproteinemia Type II* and *Familial Hypercholesterolemia* are appropriate indexing concepts; no reliably verified standalone current FDB MeSH descriptor was found.

These are aggregated disease-level assertions from reviews and guidelines, not individual EHR observations. Patient-level values cited below come from published cohorts; no identifiable patient records were accessed.

## 2. Etiology, risk, protection, and gene–environment interaction

### Primary cause

The causal lesion is a **germline APOB variant affecting the LDLR-binding region of apoB-100**. The best-established variants are p.Arg3527Gln and p.Arg3527Trp. Older papers number these as Arg3500 because of historical protein-numbering conventions. The 2024 review reports that R3500Q raises LDL-C by approximately **60–70 mg/dL** and that approximately 35 FH-associated APOB variants had been described, although every rare APOB missense variant requires contemporary classification and preferably functional validation. (kounatidis2024apob100andatherosclerosis pages 13-14)

### Genetic risk and modifiers

Risk is greatest with biallelic/dose-enhanced disease, additional pathogenic variants in LDL-pathway genes, and a high polygenic LDL-C burden. Candidate modifiers include **LDLR, PCSK9, APOE, LDLRAP1, ABCG5, and ABCG8**. Digenic FH literature shows substantial intrafamilial variability and warns that computational prediction alone is insufficient; cosegregation, population frequency, and functional LDLR-binding/uptake evidence remain important. (haradashiba2023guidelinesforthe pages 8-11, kamar2021thedigeniccausality pages 14-15)

Possible protective modifiers include LDL-lowering **PCSK9 loss-of-function** alleles and APOB truncating alleles, but an APOB truncation causes a biologically distinct hypobetalipoproteinemia phenotype and should not be treated as a protective FDB allele. PCSK9 knockout mice showed an approximately 80% LDL-C decrease, illustrating the pathway rather than proving an FDB-specific human modifier effect. (kamar2021thedigeniccausality pages 14-15)

### Environmental and lifestyle modifiers

The pathogenic variant is sufficient to predispose to disease, but cumulative LDL exposure and clinical events are modified by diet, smoking, physical activity, obesity/visceral adiposity, diabetes, hypertension, high triglycerides, and low HDL-C. These associations are best established in broader FH cohorts. A Western diet rich in saturated fat can impede LDL apoB-100 clearance; Mediterranean-style eating enhances LDL catabolism, while aerobic training modestly lowers apoB. In a meta-analysis of 57 trials involving 3,194 participants, aerobic exercise lowered apoB-100 by about **2.073 mg/dL**; this was not an FDB-only analysis. (kounatidis2024apob100andatherosclerosis pages 13-14, haradashiba2023guidelinesforthe pages 8-11)

There is no infectious, toxic, occupational, or radiation cause. Such exposures may affect background cardiovascular risk but do not cause the Mendelian disorder.

## 3. Phenotypes

| Phenotype | Type, onset/course, frequency and severity | Suggested HPO annotation |
|---|---|---|
| Elevated LDL-C/hypercholesterolemia | Laboratory abnormality present from early life; chronic and lifelong without treatment. R3500Q adds roughly 60–70 mg/dL, with variable penetrance. | **Hypercholesterolemia; Increased LDL cholesterol level**—verify current HPO IDs |
| Premature atherosclerosis/CAD | Progressive complication of cumulative LDL exposure; adult-onset is usual in heterozygous FDB, but timing varies. | **Premature coronary artery disease; Atherosclerosis** |
| Coronary calcification | Imaging sign; both mild and severe calcification are reported. | **Coronary artery calcification** |
| Myocardial infarction/ischemic heart disease | Episodic acute complication of chronic plaque disease; potentially fatal. | **Myocardial infarction; Ischemic heart disease** |
| Tendon or cutaneous xanthomas | Physical sign caused by cholesterol deposition; possible but apparently less frequent than in severe LDLR-FH. | **Tendon xanthoma; Xanthoma** |
| Corneal arcus/xanthelasma | Physical signs recognized in FH; FDB-specific frequencies are unavailable. | **Corneal arcus; Xanthelasma** |
| Carotid stenosis | Vascular imaging sign. One comparison found 4% in FDB versus 15% in classic FH. | **Carotid artery stenosis** |

In one comparative study summarized in 2024, CHD was present in **5.6% of FDB subjects at median age 52**, versus nearly **40% of FH patients at mean age 41**; carotid stenosis occurred in 4% versus 15%. These figures should not be interpreted as lifetime penetrance because age distributions and ascertainment differed. (kounatidis2024apob100andatherosclerosis pages 13-14)

Hyper-LDL-cholesterolemia itself is generally asymptomatic. Quality-of-life loss arises mainly from diagnostic burden, lifelong medication, cardiovascular procedures, angina, infarction, and anxiety about relatives. No validated FDB-specific EQ-5D, SF-36, or PROMIS estimates were identified.

## 4. Genetic and molecular information

- **Gene:** **APOB**, chromosome 2p24.1; protein apolipoprotein B-100. HGNC and transcript identifiers should be pulled from the current HGNC/NCBI release during production curation.
- **Primary variant:** **NM_000384.3:c.10580G>A, p.Arg3527Gln**, legacy **R3500Q**.
- **Additional established allele:** p.Arg3527Trp, legacy R3500W.
- **Other reported ligand-defective alleles:** nearby residues such as p.Arg3558Cys/legacy R3531C and other APOB missense variants have been reported, but pathogenicity is not uniform and must be checked variant by variant.
- **Origin/type:** germline, usually heterozygous missense; rare homozygotes occur. This is not a somatic cancer disorder.
- **Functional class:** partial loss of ligand function—reduced LDLR binding—rather than loss of apoB production. It is neither a classical null allele nor a demonstrated dominant-negative protein in the usual sense.
- **Classification:** p.Arg3527Gln is an established pathogenic FH allele. Current ClinVar assertions, review status, gnomAD frequency, and ancestry-stratified counts should be imported directly from live databases; exact values were not available in the retrieved papers.
- **Structural abnormalities:** no recurrent aneuploidy, translocation, inversion, or copy-number lesion defines FDB. CMA, karyotyping, and FISH therefore have no routine role.
- **Epigenetics:** no reproducible disease-defining methylation, histone, or chromatin signature has been established. Epigenetic studies of atherosclerosis are downstream and not diagnostic of FDB.

APOB variants were estimated in the retrieved reviews to account for approximately **5–12% of autosomal-dominant FH**, depending strongly on population and ascertainment. This is not the prevalence of FDB in the general population. (kounatidis2024apob100andatherosclerosis pages 13-14, siddiqi2026familialhypercholesterolemiastateoftheart pages 3-4)

## 5. Environmental information

No environmental exposure is necessary or sufficient to produce FDB. Environment modifies biochemical expression and ASCVD progression:

- **Adverse:** saturated/trans-fat-rich diet, smoking, inactivity, obesity, insulin resistance/diabetes, and hypertension.
- **Protective:** Mediterranean-style dietary pattern, replacement of saturated with unsaturated fats, regular aerobic activity, avoidance of tobacco, and control of blood pressure, weight, and diabetes.
- **Alcohol:** no FDB-specific protective effect should be inferred; alcohol is not recommended for prevention.
- **Infection:** not etiologic. Inflammation contributes to downstream plaque biology, but FDB is not infectious.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic trigger:** ligand-region APOB missense variant.
2. **Protein dysfunction:** apoB-100 on LDL binds LDLR with reduced affinity.
3. **Cellular defect:** receptor-mediated uptake by hepatocytes falls despite a generally intact LDLR.
4. **Metabolic abnormality:** LDL residence time and plasma LDL particle concentration rise.
5. **Arterial initiation:** apoB-containing particles cross and are retained in arterial intima, then undergo oxidation and other modifications.
6. **Inflammatory amplification:** endothelial VCAM1/ICAM1/E-selectin expression recruits monocytes; macrophage scavenger receptors such as CD36 and LOX-1 internalize oxidized LDL, generating foam cells. TLR, NF-κB, p38-MAPK/JAK-STAT, ROS, and NLRP3–IL-1 signaling contribute.
7. **Tissue injury:** foam-cell death, defective efferocytosis, smooth-muscle activation, extracellular-matrix deposition, necrotic core formation, calcification, and fibrous-cap remodeling produce stenotic or rupture-prone plaque.
8. **Clinical endpoints:** stable angina, coronary calcification/stenosis, plaque rupture, thrombosis, acute myocardial infarction, and premature death. (kounatidis2024apob100andatherosclerosis pages 4-5, kounatidis2024apob100andatherosclerosis pages 5-7, kounatidis2024apob100andatherosclerosis pages 11-13)

ApoB-100 is the LDLR ligand, and each VLDL, IDL, LDL, and Lp(a) particle contains one apoB molecule; thus apoB concentration approximates atherogenic particle number. More than 90% of circulating apoB-containing particles are LDL in many settings. (kounatidis2024apob100andatherosclerosis pages 5-7)

**Suggested GO biological processes:** LDL particle receptor binding; receptor-mediated endocytosis; plasma lipoprotein clearance; cholesterol homeostasis; lipid transport; response to oxidized LDL; macrophage-derived foam-cell differentiation; leukocyte adhesion; inflammatory response; regulation of NLRP3 inflammasome complex assembly.

**Suggested GO cellular components:** LDL particle; VLDL particle; plasma membrane; clathrin-coated pit; endosome; extracellular space.

**Suggested CL terms:** hepatocyte; vascular endothelial cell; classical monocyte; macrophage; foam cell; vascular smooth-muscle cell; dendritic cell; CD4-positive T cell; regulatory T cell. Exact IDs should be verified against current GO/CL releases.

No FDB-specific single-cell atlas, spatial transcriptomic map, diagnostic transcriptomic/proteomic signature, or integrated multi-omics classifier was identified. Modern single-cell atherosclerosis studies describe downstream plaque heterogeneity, not an FDB-specific state.

## 7. Anatomical structures affected

- **Primary metabolic organ:** liver—especially hepatocytes responsible for LDLR-mediated clearance. Suggested **UBERON: liver; liver lobule**.
- **Primary injured system:** arterial vasculature, particularly coronary arteries and aorta; carotid and peripheral arteries can also be involved. Suggested **UBERON: artery; coronary artery; aorta; carotid artery; arterial wall/tunica intima**.
- **Secondary tissues:** Achilles and extensor tendons, skin, and corneal periphery when lipid deposits form.
- **Subcellular sites:** hepatocyte plasma membrane, clathrin-coated pits and endosomes for LDLR uptake; extracellular/subendothelial matrix for LDL retention; macrophage lysosomal/lipid-droplet compartments during foam-cell formation.
- **Lateralization:** not applicable; vascular disease can be diffuse, bilateral, or anatomically asymmetric according to plaque burden.

## 8. Temporal development

The genotype is congenital and LDL-C elevation begins early, although clinical symptoms are usually absent for years. Disease is **chronic, lifelong, and insidiously progressive**. A useful staging model is:

1. biochemical hypercholesterolemia;
2. subclinical arterial retention, increased intima-media thickness, or coronary calcium;
3. clinically stable atherosclerotic disease;
4. acute plaque complication—ACS/MI—or diffuse advanced vascular disease.

There is no spontaneous genetic remission. LDL-C can normalize or substantially improve with treatment, but established plaque may persist. Earlier statin initiation is associated with less carotid intima-media thickening in pediatric FH, supporting childhood as a critical prevention window. (haradashiba2023guidelinesforthe pages 2-4, haradashiba2023guidelinesforthe pages 24-25)

## 9. Inheritance and population

### Inheritance

FDB is generally **autosomal dominant/codominant**. Each child of a heterozygous affected individual has a 50% transmission risk. Penetrance for the biochemical phenotype is incomplete/variable and age-dependent for clinical ASCVD. Expressivity varies with allele dosage, polygenic background, lifestyle, sex, and conventional risk factors. Genetic anticipation is not established; consanguinity is not required, although it raises the chance of biallelic disease. Germline mosaicism is not a recognized major feature.

### Epidemiology

A reliable global prevalence or incidence for molecularly pure FDB is unavailable. Historical European estimates vary because of founder effects and because modern FH cohorts combine APOB and LDLR disease. APOB alleles account for approximately 5–12% of genetically defined autosomal-dominant FH in some series. General heterozygous FH prevalence is about 1:300 in the 2023 Japanese guideline, but applying that figure directly to FDB would be incorrect. (haradashiba2023guidelinesforthe pages 2-4)

p.Arg3527Gln is enriched in populations of northwestern/central European ancestry and in founder-derived groups. p.Arg3527Trp has been described more often in East Asian families. Both sexes inherit the allele equally; observed event rates may be earlier in men because ASCVD penetrance is sex- and age-dependent. Precise carrier frequencies should be sourced from live gnomAD ancestry data.

## 10. Diagnostics

### Clinical and laboratory assessment

Obtain a fasting or nonfasting lipid profile, apoB, non-HDL-C, triglycerides, HDL-C, and Lp(a), and document the **highest untreated LDL-C**. Examine Achilles/extensor tendons and skin; obtain a three-generation history of hypercholesterolemia and premature CAD. The 2023 Japanese guideline diagnoses adult FH using at least two of: untreated LDL-C ≥180 mg/dL; tendon/cutaneous nodular xanthoma; first-degree family history of FH or premature CAD. Premature CAD is <55 years in men and <65 years in women. These are general FH, not FDB-specific, criteria. (haradashiba2023guidelinesforthe pages 8-11)

Imaging is for phenotype/risk assessment, not molecular diagnosis: Achilles tendon radiograph or ultrasound, coronary calcium CT in selected adults, carotid ultrasound, and stress testing or coronary imaging when ischemia is suspected. Japanese thresholds for Achilles thickening are radiographic ≥8.0 mm in men/≥7.5 mm in women or ultrasound ≥6.0/≥5.5 mm. (haradashiba2023guidelinesforthe pages 8-11)

### Genetic testing

Preferred testing is an FH multigene panel including **LDLR, APOB, PCSK9, and LDLRAP1**, with deletion/duplication analysis where appropriate. If a familial APOB allele is known, targeted testing is efficient. WES/WGS is useful for panel-negative severe or atypical families and possible digenic disease, but incidental APOB missense variants require rigorous ACMG/AMP interpretation and functional evidence. CMA, karyotype, FISH, mitochondrial sequencing, and repeat-expansion testing are not routinely indicated.

### Differential diagnosis

Exclude hypothyroidism, nephrotic syndrome, cholestatic liver disease, uncontrolled diabetes, medication-related dyslipidemia, familial combined hyperlipidemia, polygenic hypercholesterolemia, sitosterolemia, lysosomal acid lipase deficiency, elevated Lp(a), LDLR-related FH, PCSK9 gain-of-function FH, and LDLRAP1-related recessive hypercholesterolemia. FDB often has a milder LDL-C elevation and normal receptor structure/function but cannot be reliably distinguished from LDLR-FH by lipid profile alone. (kounatidis2024apob100andatherosclerosis pages 13-14, faiz2012molecularpathologyof pages 4-5)

No validated omics-based diagnostic beyond DNA testing and conventional lipoprotein biomarkers is established.

## 11. Outcome and prognosis

FDB increases lifelong ASCVD morbidity, particularly coronary calcification, ischemic heart disease, and MI. Average severity appears lower than LDLR-FH, but individual prognosis is heterogeneous. General FH data show CAD odds approximately 10–20 times and peripheral arterial disease odds 5–10 times those of non-FH populations; these effect sizes should not be assigned directly to FDB. (haradashiba2023guidelinesforthe pages 2-4)

Prognostic factors are untreated and on-treatment LDL-C/apoB, duration of exposure, existing ASCVD or coronary calcium, smoking, diabetes, hypertension, low HDL-C, high triglycerides, Lp(a), male sex/older age, family history, allele dosage, and additional LDL-pathway variants. No FDB-specific 5- or 10-year survival, disability, mortality, or quality-of-life model was identified. Recovery from the genotype is impossible, but LDL normalization can markedly reduce future risk.

## 12. Treatment

FDB is treated according to heterozygous FH algorithms, with response monitored by LDL-C, non-HDL-C, and apoB.

1. **Lifestyle foundation:** Mediterranean-style diet; reduced saturated/trans fats; regular aerobic exercise; weight, diabetes, and blood-pressure control; no tobacco. These measures are adjunctive and rarely sufficient alone. Suggested NCIt concepts: dietary intervention, exercise therapy, smoking cessation.
2. **High-intensity statin:** atorvastatin or rosuvastatin; reduces hepatic cholesterol synthesis and upregulates LDLR. Suggested NCIt: HMG-CoA reductase inhibitor therapy. Statins are the best-supported first-line class in FH and earlier pediatric use limits IMT progression. (haradashiba2023guidelinesforthe pages 2-4)
3. **Ezetimibe:** blocks NPC1L1-mediated intestinal cholesterol absorption; add when targets are not achieved. Suggested NCIt: ezetimibe therapy.
4. **PCSK9 monoclonal antibody:** evolocumab or alirocumab increases recycled hepatic LDLR. General HeFH trials report about **59–61%** and **51–58%** LDL-C reductions, respectively; intact LDLR in FDB provides a strong mechanistic rationale, but these are not FDB-only response estimates. (siddiqi2026familialhypercholesterolemiastateoftheart pages 1-2)
5. **Inclisiran:** hepatic PCSK9 siRNA; general FH evidence reports about **48%** LDL-C lowering. Suggested NCIt: small interfering RNA therapy/inclisiran.
6. **Bempedoic acid:** oral ATP-citrate lyase inhibitor, useful when further lowering is needed or statin intolerance occurs. Suggested NCIt: ATP citrate lyase inhibitor therapy.
7. **Bile-acid sequestrant:** an option, including selected pregnancy contexts; gastrointestinal adverse effects and pill burden limit use.
8. **Lipoprotein apheresis:** reserved for exceptionally severe, refractory disease or advanced ASCVD; acutely lowers LDL-C approximately **50–75% per session** in general FH. (siddiqi2026familialhypercholesterolemiastateoftheart pages 1-2)

Common adverse effects include statin-associated muscle symptoms and transaminase elevations, ezetimibe gastrointestinal symptoms, PCSK9/inclisiran injection-site reactions, bempedoic-acid-associated hyperuricemia/gout and tendon concerns, and apheresis-related vascular-access burden and hypotension. Pregnancy planning requires specialist management; many systemic lipid-lowering drugs are stopped, while bile-acid sequestrants and, in severe disease, apheresis may be considered. (haradashiba2023guidelinesforthe pages 19-21)

Targets used in contemporary FH practice are ≥50% LDL-C reduction and LDL-C <70 mg/dL for high-risk primary prevention, or <55 mg/dL for very-high-risk/established ASCVD; pediatric targets are commonly <135 mg/dL after age 10. (siddiqi2026familialhypercholesterolemiastateoftheart pages 1-2, fularski2024unveilingfamilialhypercholesterolemia—review pages 7-9)

No approved therapy edits APOB p.Arg3527Gln. APOB-silencing therapies are unattractive as a routine FDB correction because excessive apoB suppression can impair hepatic lipid export. No retrieved ClinicalTrials.gov study specifically enrolled FDB as a distinct molecular cohort.

## 13. Prevention

- **Primary prevention of genotype:** impossible after conception. Reproductive options include genetic counseling, prenatal diagnosis, and preimplantation genetic testing when the familial pathogenic variant is known.
- **Secondary prevention:** opportunistic/universal cholesterol screening according to national policy, molecular confirmation, and **cascade testing** of first-degree relatives. Each identified heterozygous relative has a 50% prior risk in an autosomal-dominant pedigree.
- **Tertiary prevention:** early and sustained LDL/apoB lowering, smoking avoidance, and management of blood pressure, diabetes, obesity, and Lp(a)-related residual risk.
- **Vaccination/immunization:** not applicable.
- **Newborn screening:** not universally established for FDB. Pediatric lipid screening or reverse-cascade screening can identify affected families before events.

The World Heart Federation emphasizes that adverse exposure to LDL/apoB particles is cumulative and preventable through earlier screening and treatment. (haradashiba2023guidelinesforthe pages 2-4)

## 14. Other species and natural disease

- **Human:** *Homo sapiens*, NCBI Taxonomy **9606**; disease gene **APOB**.
- **Orthologues:** ApoB is evolutionarily conserved in mammals, including mouse (*Mus musculus*, Taxon 10090), rat (*Rattus norvegicus*, 10116), rabbit (*Oryctolagus cuniculus*, 9986), pig (*Sus scrofa*, 9823), and dog (*Canis lupus familiaris*, 9615). Current NCBI Gene IDs should be imported directly.
- **Natural veterinary disease:** no well-established naturally occurring animal disorder orthologous specifically to human APOB p.Arg3527Gln FDB was identified. Breed-specific VBO annotation is therefore not justified.
- **Transmission:** inherited vertically within a species; not contagious or zoonotic.

## 15. Model organisms and experimental systems

Relevant models include human apoB-100 transgenic mice, APOB variant-expression systems, primary or immortalized hepatocyte uptake assays, fibroblast/lymphocyte LDLR assays, and general atherosclerosis models such as **Ldlr-null** and **Apoe-null** mice. Human apoB-100-expressing mice can develop complex atherosclerotic lesions and are useful for lipoprotein metabolism and pharmacology. (zadelaar2007mousemodelsfor pages 3-4)

An allele-faithful APOB p.Arg3527Gln knock-in or transgenic system is conceptually the most specific model: expected readouts are reduced LDLR binding/uptake, prolonged LDL residence, hypercholesterolemia, and diet-dependent plaque. However, mice normally package much cholesterol in HDL and edit ApoB RNA differently from humans; background strain and diet strongly influence plaque, limiting direct quantitative translation. Ldlr−/− and Apoe−/− mice reproduce hypercholesterolemia and atherogenesis but not the defining apoB ligand defect. Cell-based LDLR-binding and uptake assays may therefore be more specific for variant classification than generic knockout models.

## Recent developments and expert interpretation

The major 2023–2024 development is not a new FDB-specific therapy but **integration of APOB-FDB into genotype-defined FH care**: multigene panels/cascade screening, earlier combination treatment, apoB and non-HDL-C as particle-burden measures, and wider use of PCSK9-directed agents. The February 2024 apoB review emphasizes that apoB is both an atherogenic-particle biomarker and a participant in arterial inflammation; its abstract states that apoB-100 “**has been suggested to play a crucial role in the formation of the atherogenic plaque**.” [Published February 2024; DOI 10.3390/metabo14020123.] (kounatidis2024apob100andatherosclerosis pages 13-14, kounatidis2024apob100andatherosclerosis pages 5-7)

The 2023 Japanese guideline’s clinically important conclusion is that FH causes persistent LDL elevation from birth and therefore requires “**early diagnosis and appropriate treatment**” plus cascade screening. [Published May 2023; DOI 10.5551/jat.CR005](https://doi.org/10.5551/jat.CR005). This guidance is applicable to FDB, while its risk estimates and examination thresholds derive from mixed-genotype FH. (haradashiba2023guidelinesforthe pages 2-4, haradashiba2023guidelinesforthe pages 8-11)

## Key curation cautions

1. Do not confuse ligand-defective APOB hypercholesterolemia with **APOB-related familial hypobetalipoproteinemia**, which is usually caused by truncating/loss-of-production variants and produces low LDL-C and hepatic steatosis.
2. Store both modern and legacy residue nomenclature: **p.Arg3527Gln = R3500Q**.
3. Do not assign every rare APOB missense variant as pathogenic; require current ClinVar/ClinGen assessment, population frequency, segregation, and ideally functional evidence.
4. Do not copy general FH prevalence, mortality, or treatment-response estimates into FDB-specific fields without an “extrapolated from mixed-genotype FH” qualifier.
5. Exact live MONDO, Orphanet, HGNC, HPO, GO, CL, UBERON, NCIt, ClinVar, and gnomAD identifiers should be validated against their current releases before production loading.

References

1. (kounatidis2024apob100andatherosclerosis pages 13-14): Dimitris Kounatidis, Natalia G. Vallianou, Aikaterini Poulaki, Angelos Evangelopoulos, Fotis Panagopoulos, Theodora Stratigou, Eleni Geladari, Irene Karampela, and Maria Dalamaga. Apob100 and atherosclerosis: what’s new in the 21st century? Metabolites, 14:123, Feb 2024. URL: https://doi.org/10.3390/metabo14020123, doi:10.3390/metabo14020123. This article has 64 citations.

2. (kounatidis2024apob100andatherosclerosis pages 11-13): Dimitris Kounatidis, Natalia G. Vallianou, Aikaterini Poulaki, Angelos Evangelopoulos, Fotis Panagopoulos, Theodora Stratigou, Eleni Geladari, Irene Karampela, and Maria Dalamaga. Apob100 and atherosclerosis: what’s new in the 21st century? Metabolites, 14:123, Feb 2024. URL: https://doi.org/10.3390/metabo14020123, doi:10.3390/metabo14020123. This article has 64 citations.

3. (haradashiba2023guidelinesforthe pages 2-4): Mariko Harada-Shiba, Hidenori Arai, Hirotoshi Ohmura, Hiroaki Okazaki, Daisuke Sugiyama, Hayato Tada, Kazushige Dobashi, Kota Matsuki, Tetsuo Minamino, Shizuya Yamashita, and Koutaro Yokote. Guidelines for the diagnosis and treatment of adult familial hypercholesterolemia 2022. Journal of Atherosclerosis and Thrombosis, 30:558-586, May 2023. URL: https://doi.org/10.5551/jat.cr005, doi:10.5551/jat.cr005. This article has 108 citations and is from a peer-reviewed journal.

4. (siddiqi2026familialhypercholesterolemiastateoftheart pages 3-4): Ahmed Kamal Siddiqi, Kumail Mustafa Ali, Rameen Shahid, Shamna Haris, Anandita Kulkarni, Iliyan Mithani, Wilhelm Haverkamp, and Muhammad Shahzeb Khan. Familial hypercholesterolemia: state-of-the-art. Jun 2026. URL: https://doi.org/10.4081/cardio.2026.102, doi:10.4081/cardio.2026.102. This article has 0 citations.

5. (haradashiba2023guidelinesforthe pages 24-25): Mariko Harada-Shiba, Hidenori Arai, Hirotoshi Ohmura, Hiroaki Okazaki, Daisuke Sugiyama, Hayato Tada, Kazushige Dobashi, Kota Matsuki, Tetsuo Minamino, Shizuya Yamashita, and Koutaro Yokote. Guidelines for the diagnosis and treatment of adult familial hypercholesterolemia 2022. Journal of Atherosclerosis and Thrombosis, 30:558-586, May 2023. URL: https://doi.org/10.5551/jat.cr005, doi:10.5551/jat.cr005. This article has 108 citations and is from a peer-reviewed journal.

6. (haradashiba2023guidelinesforthe pages 8-11): Mariko Harada-Shiba, Hidenori Arai, Hirotoshi Ohmura, Hiroaki Okazaki, Daisuke Sugiyama, Hayato Tada, Kazushige Dobashi, Kota Matsuki, Tetsuo Minamino, Shizuya Yamashita, and Koutaro Yokote. Guidelines for the diagnosis and treatment of adult familial hypercholesterolemia 2022. Journal of Atherosclerosis and Thrombosis, 30:558-586, May 2023. URL: https://doi.org/10.5551/jat.cr005, doi:10.5551/jat.cr005. This article has 108 citations and is from a peer-reviewed journal.

7. (kounatidis2024apob100andatherosclerosis pages 4-5): Dimitris Kounatidis, Natalia G. Vallianou, Aikaterini Poulaki, Angelos Evangelopoulos, Fotis Panagopoulos, Theodora Stratigou, Eleni Geladari, Irene Karampela, and Maria Dalamaga. Apob100 and atherosclerosis: what’s new in the 21st century? Metabolites, 14:123, Feb 2024. URL: https://doi.org/10.3390/metabo14020123, doi:10.3390/metabo14020123. This article has 64 citations.

8. (kounatidis2024apob100andatherosclerosis pages 5-7): Dimitris Kounatidis, Natalia G. Vallianou, Aikaterini Poulaki, Angelos Evangelopoulos, Fotis Panagopoulos, Theodora Stratigou, Eleni Geladari, Irene Karampela, and Maria Dalamaga. Apob100 and atherosclerosis: what’s new in the 21st century? Metabolites, 14:123, Feb 2024. URL: https://doi.org/10.3390/metabo14020123, doi:10.3390/metabo14020123. This article has 64 citations.

9. (siddiqi2026familialhypercholesterolemiastateoftheart pages 1-2): Ahmed Kamal Siddiqi, Kumail Mustafa Ali, Rameen Shahid, Shamna Haris, Anandita Kulkarni, Iliyan Mithani, Wilhelm Haverkamp, and Muhammad Shahzeb Khan. Familial hypercholesterolemia: state-of-the-art. Jun 2026. URL: https://doi.org/10.4081/cardio.2026.102, doi:10.4081/cardio.2026.102. This article has 0 citations.

10. (faiz2012molecularpathologyof pages 4-5): Fathimath Faiz, Amanda J. Hooper, and Frank M. van Bockxmeer. Molecular pathology of familial hypercholesterolemia, related dyslipidemias and therapies beyond the statins. Critical Reviews in Clinical Laboratory Sciences, 49:1-17, Feb 2012. URL: https://doi.org/10.3109/10408363.2011.646942, doi:10.3109/10408363.2011.646942. This article has 38 citations and is from a peer-reviewed journal.

11. (fularski2024unveilingfamilialhypercholesterolemia—review pages 7-9): Piotr Fularski, Joanna Hajdys, Gabriela Majchrowicz, Magdalena Stabrawa, Ewelina Młynarska, Jacek Rysz, and Beata Franczyk. Unveiling familial hypercholesterolemia—review, cardiovascular complications, lipid-lowering treatment and its efficacy. International Journal of Molecular Sciences, 25:1637, Jan 2024. URL: https://doi.org/10.3390/ijms25031637, doi:10.3390/ijms25031637. This article has 30 citations.

12. (kamar2021thedigeniccausality pages 14-15): Amina Kamar, Athar Khalil, and Georges Nemer. The digenic causality in familial hypercholesterolemia: revising the genotype–phenotype correlations of the disease. Frontiers in Genetics, Jan 2021. URL: https://doi.org/10.3389/fgene.2020.572045, doi:10.3389/fgene.2020.572045. This article has 31 citations and is from a peer-reviewed journal.

13. (zadelaar2007mousemodelsfor pages 3-4): Susanne Zadelaar, Robert Kleemann, Lars Verschuren, Jitske de Vries-Van der Weij, José van der Hoorn, Hans M. Princen, and Teake Kooistra. Mouse models for atherosclerosis and pharmaceutical modifiers. Arteriosclerosis, thrombosis, and vascular biology, 27 8:1706-21, Aug 2007. URL: https://doi.org/10.1161/atvbaha.107.142570, doi:10.1161/atvbaha.107.142570. This article has 758 citations and is from a domain leading peer-reviewed journal.

14. (haradashiba2023guidelinesforthe pages 19-21): Mariko Harada-Shiba, Hidenori Arai, Hirotoshi Ohmura, Hiroaki Okazaki, Daisuke Sugiyama, Hayato Tada, Kazushige Dobashi, Kota Matsuki, Tetsuo Minamino, Shizuya Yamashita, and Koutaro Yokote. Guidelines for the diagnosis and treatment of adult familial hypercholesterolemia 2022. Journal of Atherosclerosis and Thrombosis, 30:558-586, May 2023. URL: https://doi.org/10.5551/jat.cr005, doi:10.5551/jat.cr005. This article has 108 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Familial_Defective_Apolipoprotein_B-100-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 0 |
| Quoted claims checked | 1 |
| Quoted claims found in source | 1 |
| Quoted claims **not** found in source | 0 |
| References weighed for topical relevance | 8 |
| On topic | 6 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.5551/jat.CR005](https://doi.org/10.5551/jat.CR005` (1 mention) - Identifier did not resolve to a record