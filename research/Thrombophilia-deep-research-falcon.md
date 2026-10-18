---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-26T16:31:58.202128'
end_time: '2026-08-26T16:42:34.581106'
duration_seconds: 636.38
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Thrombophilia
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 15
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  quotes_checked: 3
  quotes_valid: 3
  quotes_not_checkable: 1
  relevance_assessed: 9
  on_topic: 4
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Thrombophilia-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Thrombophilia
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Thrombophilia** covering all of the
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
- **Disease Name:** Thrombophilia
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Thrombophilia** covering all of the
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


# Thrombophilia: comprehensive disease-characteristics report

**Scope and evidence note.** Thrombophilia is a heterogeneous predisposition, not one anatomically localized disease. The clinically meaningful outcome is usually venous thromboembolism (VTE), while arterial thrombosis is much less consistently related to inherited thrombophilia. Evidence below is labeled as human clinical/cohort, guideline, model-organism, or exploratory. URLs are DOI links unless otherwise stated.

## Executive summary

Thrombophilia denotes an inherited or acquired shift of hemostasis toward thrombosis. The five classic inherited forms are factor V Leiden, prothrombin G20210A, and deficiencies of antithrombin, protein C, or protein S. Antiphospholipid syndrome (APS) is the principal acquired thrombophilia. Open Targets links the umbrella entity to **MONDO:0002305**, inherited thrombophilia to **MONDO:0100240**, and the strongest established targets to **F5, F2, SERPINC1, PROC**, and **PROS1**. These associations are supported by clinical and genetic evidence rather than by a single causal gene for the umbrella disorder (OpenTargets Search: thrombophilia).

The central causal chain is: inherited/acquired defect plus a transient exposure—surgery, immobility, cancer, pregnancy, estrogen, inflammation, or infection—causes inadequate control of factor Xa/thrombin, excessive fibrin formation, venous obstruction, embolization, ischemia, and chronic post-thrombotic injury. Penetrance is incomplete and strongly exposure-dependent.

The dominant contemporary expert view is **selective, action-oriented testing**, not broad panels. ASH 2023 generally recommends against testing after unprovoked VTE if standard management is indefinite anticoagulation, but conditionally supports testing in selected hormone-associated or major transient-risk VTE and selected cerebral/splanchnic thrombosis when the result would determine whether anticoagulation is stopped. BSH similarly discourages routine testing after clearly provoked VTE and routine screening of asymptomatic relatives; APS testing is more actionable because triple positivity affects both duration and choice of anticoagulant (miceli2025fromcirculatingbiomarkers pages 8-9, miceli2025fromcirculatingbiomarkers pages 6-8, miceli2025fromcirculatingbiomarkers pages 5-6).

## 1. Disease information

### Definition and classification

Thrombophilia—also called a **hypercoagulable state**, **prothrombotic state**, or, for genetic forms, **hereditary/inherited thrombophilia**—is an increased tendency to form clinically inappropriate thrombi. It may be:

* **Inherited:** factor V Leiden/APC resistance; F2 G20210A; antithrombin, protein C, or protein S deficiency; much rarer defects affecting thrombomodulin, heparin cofactor II, fibrinogen, or other regulators.
* **Acquired:** APS; cancer; myeloproliferative neoplasms; paroxysmal nocturnal hemoglobinuria; pregnancy/postpartum state; estrogen exposure; surgery, trauma, immobilization; inflammatory/infectious disease; nephrotic syndrome; and heparin-induced thrombocytopenia. These acquired illnesses are etiologies or provoking conditions, not interchangeable diagnoses.
* **Complex/multifactorial:** most clinical events reflect gene–gene and gene–environment interaction rather than a genotype acting alone.

### Identifiers

* **MONDO:** thrombophilia **MONDO:0002305**; inherited thrombophilia **MONDO:0100240**; AD protein-S-deficiency thrombophilia **MONDO:0012868**; X-linked thrombophilia due to factor IX defect **MONDO:0010432**; congenital HRG-deficiency thrombophilia **MONDO:0013143** (OpenTargets Search: thrombophilia).
* **MeSH:** *Thrombophilia*; *Venous Thromboembolism* is a separate outcome concept.
* **ICD-10-CM:** **D68.5 Primary thrombophilia** and **D68.6 Other thrombophilia** are commonly used; APS and individual thrombotic events also have distinct codes. ICD-11 should be mapped to the relevant thrombophilic disorder and separately to the thrombotic manifestation rather than treating the umbrella term as a single lesion.
* **OMIM/Orphanet:** use subtype records rather than one umbrella record—e.g., factor V Leiden, prothrombin thrombophilia, antithrombin deficiency, protein C deficiency, and protein S deficiency.

The report is synthesized from aggregated resources, cohorts, guidelines, and primary studies. It is **not individual-patient/EHR evidence** unless a cited cohort explicitly used medical records.

## 2. Etiology and risk/protective factors

### Genetic causal factors

The classic mechanisms are gain of coagulation function (**F5**, **F2**) or loss of endogenous anticoagulant function (**SERPINC1, PROC, PROS1**). In a population cohort of 29,387 middle-aged/older adults, pathogenic **PROC/PROS1/SERPINC1** variants occurred in 908 participants (3.1%) and conferred HR 1.6 for incident VTE; heterozygous factor V Leiden and F2 G20210A conferred HR 1.8 and 1.6. One classic variant gave HR 1.7, whereas two or more gave HR 3.9, demonstrating a dose-graded genetic effect. The study abstract states: “**The 5 classic thrombophilias are associated with a dose-graded risk of VTE**” (human population cohort; Manderstedt et al., 2022, DOI: https://doi.org/10.1161/JAHA.121.023018).

Factor V Leiden prevalence is approximately 1–5% in European-ancestry populations and 10–20% among VTE patients; heterozygotes have about sevenfold and homozygotes about 20-fold higher lifetime thrombosis risk in summarized evidence. F2 G20210A occurs in roughly 1–3% of the general population and 6–10% of VTE patients, with a two- to threefold risk increase in heterozygotes (miceli2025fromcirculatingbiomarkers pages 14-15). These frequencies vary markedly by ancestry and should not be extrapolated universally.

Rare candidate genes include **THBD, SERPIND1, HRG, ADAMTS13, F8, F9, F11**, fibrinolysis genes, and regulators of VWF. However, evidence is weaker than for the classic five. Approximately one-third of familial/recurrent thrombosis remains molecularly unexplained, and known variants explain only part of estimated VTE heritability—about 30% in general-population analyses and 50% in twins (d’andrea2021raredefectslooking pages 2-3, d’andrea2021raredefectslooking pages 7-9).

### Acquired and environmental factors

Major risk factors are advancing age, previous VTE, active cancer, surgery/trauma, hospitalization, immobilization or paralysis, central venous catheters, pregnancy/puerperium, estrogen-containing contraception or hormone therapy, obesity, smoking, long travel, nephrotic syndrome, inflammatory bowel disease, severe infection/COVID-19, and autoimmune disease. Acquired inflammation activates endothelium, monocytes, neutrophils and platelets, increases tissue factor and NET formation, and suppresses anticoagulant/fibrinolytic pathways.

### Gene–environment interaction

Factor V Leiden or an anticoagulant deficiency may remain silent until estrogen exposure, pregnancy, surgery, immobility, or cancer supplies the second “hit.” APC resistance itself can also be acquired through pregnancy, postpartum physiology, exogenous hormones, high factor VIII, or protein S deficiency (miceli2025fromcirculatingbiomarkers pages 6-8). This interaction explains incomplete penetrance and why exposure avoidance/prophylaxis is often more useful than lifelong treatment of an asymptomatic genotype.

### Protective factors

No protective allele is sufficiently validated for clinical use. Some variants affecting coagulation factors may reduce thrombosis but increase bleeding, precluding simple classification as beneficial. Practical protective factors are mobility, weight management, smoking cessation, hydration/movement during prolonged travel, avoiding estrogen in high-risk carriers, and appropriate perioperative/pregnancy thromboprophylaxis. These reduce exposure-mediated risk but do not erase inherited susceptibility.

## 3. Phenotypes

Thrombophilia is often asymptomatic until thrombosis. Frequency and onset depend on subtype, zygosity, age, and exposures.

* **Deep-vein thrombosis:** unilateral limb pain, swelling, warmth and erythema; usually acute/episodic, most often adult-onset. Suggested HPO: **HP:0002625 Deep venous thrombosis**, **HP:0009763 Limb pain**, **HP:0000988 Skin edema**.
* **Pulmonary embolism:** acute dyspnea, pleuritic pain, tachycardia, hypoxemia, syncope or shock; severity ranges from incidental to fatal. HPO: **HP:0002204 Pulmonary embolism**, **HP:0002094 Dyspnea**, **HP:0001649 Tachycardia**, **HP:0012418 Hypoxemia**.
* **Cerebral venous thrombosis:** headache, papilledema, focal deficits, seizures, altered consciousness; often affects younger adults and women with hormonal/pregnancy risk. HPO: **HP:0002140 Cerebral venous thrombosis**, **HP:0002315 Headache**, **HP:0001250 Seizure**.
* **Splanchnic thrombosis:** abdominal pain, portal hypertension, bowel ischemia, splenomegaly or incidental thrombosis. HPO: **HP:0002626 Venous thrombosis**, **HP:0002027 Abdominal pain**, **HP:0001409 Portal hypertension**.
* **Recurrent VTE/unusual-site thrombosis:** suggests stronger or combined thrombophilia but is not diagnostic. HPO: **HP:0004420 Recurrent thrombophlebitis** where applicable.
* **Severe biallelic PROC/PROS1 deficiency:** neonatal purpura fulminans with dermal microvascular thrombosis, necrosis and disseminated thrombosis. HPO: **HP:0001019 Erythema**, **HP:0000961 Cyanosis**, **HP:0002639 Abnormality of coagulation**; add a specific purpura-fulminans term where supported by the current HPO release.
* **Pregnancy morbidity:** most strongly established for APS. Associations between inherited thrombophilia and recurrent loss are heterogeneous. A 2024 synthesis reported OR 2.44 for factor V Leiden, 2.08 for F2 G20210A, and 3.45 for protein S deficiency across cited pregnancy-loss evidence, but selection bias and treatment uncertainty remain substantial (borsi2024riskfactorsof pages 12-13).
* **Laboratory phenotype:** APC resistance; reduced antithrombin/protein C/free protein S activity or antigen; persistent lupus anticoagulant/anticardiolipin/anti-β2GPI in APS; elevated thrombin-generation potential. D-dimer identifies fibrin turnover in suspected acute VTE but does **not** diagnose inherited thrombophilia.

Quality-of-life impairment derives from the event: pain, breathlessness, anticoagulant burden, bleeding anxiety, post-thrombotic syndrome, chronic thromboembolic pulmonary hypertension, work loss, and fear of recurrence. A 2023 network meta-analysis explicitly states that post-thrombotic syndrome “**has a major impact on the quality of life after deep venous thrombosis**” (Shao et al., published 29 November 2023, DOI: https://doi.org/10.3390/jcm12237450).

## 4. Genetic and molecular information

| Entity/subtype | Molecular defect | Inheritance/acquired status | Typical phenotype/risk | Recommended laboratory confirmation | Ontology/gene identifiers |
|---|---|---|---|---|---|
| Factor V Leiden thrombophilia | **F5** c.1601G>A, p.Arg534Gln (legacy R506Q; historically 1691G>A); causes activated protein C resistance | Autosomal dominant thrombophilia susceptibility; incomplete penetrance | Common inherited thrombophilia; increased risk of first and recurrent venous thromboembolism, especially with estrogen exposure, pregnancy, surgery, or immobility (miceli2025fromcirculatingbiomarkers pages 14-15, miceli2025fromcirculatingbiomarkers pages 6-8) | APC resistance assay as screen, followed by targeted **F5** genotyping (miceli2025fromcirculatingbiomarkers pages 14-15) | **F5**; thrombophilia **MONDO:0002305**; inherited thrombophilia **MONDO:0100240** (OpenTargets Search: thrombophilia) |
| Prothrombin thrombophilia | **F2** c.*97G>A (legacy G20210A) in 3' UTR; associated with higher prothrombin levels | Autosomal dominant thrombophilia susceptibility; incomplete penetrance | Increased venous thromboembolism risk; risk may be amplified by coexisting provoking factors or additional thrombophilia variants (miceli2025fromcirculatingbiomarkers pages 14-15, miceli2025fromcirculatingbiomarkers pages 6-8) | Targeted **F2** genotyping for c.*97G>A | **F2**; thrombophilia **MONDO:0002305**; inherited thrombophilia **MONDO:0100240** (OpenTargets Search: thrombophilia) |
| Antithrombin deficiency | Loss-of-function or reduced-activity variants in **SERPINC1** causing quantitative or qualitative antithrombin deficiency | Usually autosomal dominant inherited thrombophilia | High-risk hereditary thrombophilia with strong VTE predisposition; events often occur at younger age and may recur (d’andrea2021raredefectslooking pages 2-3, miceli2025fromcirculatingbiomarkers pages 5-6) | Initial antithrombin **activity** assay; if low, antigen assay and activity:antigen interpretation; consider molecular testing; test outside anticoagulant interference/acquired deficiency states (miceli2025fromcirculatingbiomarkers pages 6-8) | **SERPINC1**; thrombophilia **MONDO:0002305**; inherited thrombophilia **MONDO:0100240** (OpenTargets Search: thrombophilia) |
| Protein C deficiency | Pathogenic variants in **PROC** with reduced protein C anticoagulant activity | Usually autosomal dominant inherited thrombophilia; severe biallelic disease can present neonatally | Increased VTE risk; severe deficiency may cause neonatal purpura fulminans (human and model evidence) (OpenTargets Search: thrombophilia) | Protein C activity with confirmatory antigen/genetic testing as appropriate; avoid testing during acute thrombosis or anticoagulant interference when possible (miceli2025fromcirculatingbiomarkers pages 6-8) | **PROC**; thrombophilia **MONDO:0002305**; inherited thrombophilia **MONDO:0100240** (OpenTargets Search: thrombophilia) |
| Protein S deficiency | Pathogenic variants in **PROS1** causing reduced free/functional protein S | Usually autosomal dominant inherited thrombophilia | Increased VTE risk; severe deficiency can contribute to purpura fulminans; platelet and plasma protein S both modulate venous thrombosis biology (OpenTargets Search: thrombophilia) | Free protein S antigen and/or functional assay with careful interpretation; confirm genetically when indicated; avoid confounding by pregnancy, estrogen use, and anticoagulants (miceli2025fromcirculatingbiomarkers pages 6-8) | **PROS1**; thrombophilia due to protein S deficiency **MONDO:0012868**; inherited thrombophilia **MONDO:0100240** (OpenTargets Search: thrombophilia) |
| Antiphospholipid syndrome (APS) | Autoantibody-mediated thrombophilia: lupus anticoagulant, anticardiolipin, and anti-β2-glycoprotein I antibodies | Acquired | Venous and arterial thrombosis and pregnancy morbidity; triple-positive profile confers higher recurrence risk and often changes anticoagulant choice (miceli2025fromcirculatingbiomarkers pages 8-9, miceli2025fromcirculatingbiomarkers pages 5-6) | Persistent antiphospholipid antibody positivity on repeat testing per APS criteria; include lupus anticoagulant, anticardiolipin, anti-β2GPI; interpret carefully with anticoagulants present (miceli2025fromcirculatingbiomarkers pages 8-9, miceli2025fromcirculatingbiomarkers pages 6-8) | APS is an acquired thrombophilia; broader thrombophilia **MONDO:0002305** |
| Not recommended marker set | Common **MTHFR** polymorphisms (e.g., C677T, A1298C) | Genetic variants of low/uncertain thrombosis relevance | **Not recommended** as routine thrombophilia markers because evidence does not support meaningful VTE risk stratification in most settings (miceli2025fromcirculatingbiomarkers pages 6-8) | Do **not** include in standard thrombophilia panels unless a separate indication exists (miceli2025fromcirculatingbiomarkers pages 6-8) | **MTHFR**; not a core recommended thrombophilia marker (miceli2025fromcirculatingbiomarkers pages 6-8) |


*Table: Compact reference table of the principal inherited and acquired thrombophilia entities, their molecular basis, clinical significance, and laboratory confirmation. It is useful for report standardization and for distinguishing core markers from tests such as MTHFR polymorphisms that are not routinely recommended.*

### Variant interpretation

* **F5 Leiden:** germline missense, **NM_000130.5:c.1601G>A, p.Arg534Gln**; legacy p.Arg506Gln/1691G>A reflects older numbering. It produces resistance to APC-mediated factor Va inactivation—a gain of procoagulant persistence.
* **F2 G20210A:** germline 3′-UTR variant **c.*97G>A**, increasing prothrombin expression.
* **SERPINC1, PROC, PROS1:** heterogeneous germline missense, nonsense, splice, frameshift, deletion/duplication, and regulatory variants. Quantitative type-I deficiencies reduce antigen and activity; qualitative type-II deficiencies preferentially reduce activity.
* **Origin:** classic inherited variants are germline. Somatic **JAK2/CALR/MPL** mutations indicate an acquired clonal myeloproliferative thrombophilia rather than inherited disease.
* **Classification:** assign pathogenic/likely pathogenic/VUS using ACMG/AMP criteria plus phenotype, activity/antigen measurements, segregation, population frequency, and functional evidence. A VUS alone should not establish thrombophilia or dictate lifelong anticoagulation.

Allele frequency must be recorded from the current ancestry-specific gnomAD release for the exact transcript/build. Factor V Leiden and F2 G20210A are common low-penetrance susceptibility alleles; most severe natural-anticoagulant-deficiency variants are rare. Broad sequencing may detect VUS without improving management.

Modifier effects include multiple thrombophilia variants, ABO/VWF/factor VIII levels, age, sex-specific hormone exposure, obesity, inflammatory disease, and cancer. Epigenetic signals and DNA methylation changes in endothelium/immune cells are biologically plausible but not validated diagnostic criteria. No recurrent chromosomal abnormality defines primary thrombophilia; karyotype/CMA/FISH are therefore not routine.

## 5. Environmental, lifestyle, and infectious information

Thrombosis follows Virchow’s triad: **stasis**, **vascular/endothelial injury**, and **hypercoagulability**. Environmental implementations include hospital VTE-risk assessment, mechanical and pharmacologic prophylaxis, catheter stewardship, early postoperative mobilization, and targeted pregnancy prophylaxis.

Smoking, obesity and inactivity increase risk; alcohol and specific diets are not accepted stand-alone thrombophilia causes. Occupational risk chiefly reflects prolonged immobility—e.g., long-haul travel or sedentary work—not a unique toxin. Severe infections, including SARS-CoV-2, can trigger endothelial injury, cytokine signaling, platelet activation and NET-mediated immunothrombosis. VITT is an acquired anti-PF4 antibody disorder following particular adenoviral-vector vaccines, not hereditary thrombophilia.

## 6. Mechanism/pathophysiology

### Upstream-to-downstream causal chain

1. **Upstream trigger:** F5/F2 susceptibility, loss of antithrombin/protein C/protein S, antiphospholipid antibodies, cancer/inflammation, estrogen, endothelial injury, or venous stasis.
2. **Regulatory failure:** factor Xa/thrombin escape inhibition; factor Va/VIIIa persist; tissue-factor initiation and platelet phospholipid assembly amplify coagulation.
3. **Thrombin burst:** fibrinogen becomes cross-linked fibrin; platelets activate; fibrinolysis is relatively inadequate.
4. **Thrombus propagation:** low-flow venous environments permit erythrocyte/fibrin-rich clot growth, supported by endothelial cells, monocytes, neutrophils/NETs, and platelets.
5. **Clinical injury:** venous obstruction causes edema/pain; embolization causes pulmonary vascular obstruction and right-heart strain; unusual-site thrombosis causes cerebral edema/hemorrhage or bowel/liver injury; chronic organization causes venous hypertension, PTS or chronic thromboembolic pulmonary hypertension.

### Specific pathways and ontology suggestions

* Protein C activation occurs on thrombin–thrombomodulin/EPCR-bearing endothelium; APC with protein S proteolyzes factors Va and VIIIa. Relevant GO: **GO:0007596 blood coagulation**, **GO:0050818 regulation of coagulation**, **GO:0030195 negative regulation of blood coagulation**, **GO:0072378 blood coagulation, fibrin clot formation**.
* Antithrombin inhibits thrombin and factor Xa. Protein S supports APC and TFPI. A platelet-specific **Pros1** knockout increased venous but not arterial thrombosis in mice by increasing factor X activation and thrombin within low-shear thrombi, showing cell- and flow-context specificity (model-organism evidence; Calzavarini et al., 2020, DOI: https://doi.org/10.1182/blood.2019003630).
* Immunothrombosis involves neutrophils, cfDNA/NETs, platelets and endothelium. A family-based multi-omics study of 935 GAIT-2 participants estimated cfDNA heritability at 0.26 and identified rs1687391 near **ORM1** at p=3.55×10⁻¹⁰; this remains exploratory, not a clinical biomarker (d’andrea2021raredefectslooking pages 7-9).
* Suggested cell ontology: **CL:0000115 endothelial cell**, **CL:0000233 platelet**, **CL:0000775 neutrophil**, **CL:0000576 monocyte**, **CL:0000232 erythrocyte**, **CL:0000182 hepatocyte**.
* Suggested subcellular/process terms: platelet alpha granule, secretory granule, plasma membrane, extracellular space, endoplasmic reticulum/Golgi for hepatic synthesis; NET formation and leukocyte activation where inflammatory thrombosis is documented.

No validated thrombophilia-specific single-cell, spatial-transcriptomic, proteomic, metabolomic, lipidomic, or epigenomic classifier is in routine care. Such platforms currently illuminate thromboinflammation rather than replace conventional testing.

## 7. Anatomical structures affected

The primary compartment is the **vascular system**, especially deep veins of the lower limbs and pelvis. Secondary sites include pulmonary arteries, cerebral venous sinuses, portal/mesenteric/splenic/hepatic veins, upper-extremity veins and catheter-associated veins. Severe deficiencies can affect dermal microvasculature.

Suggested anatomy terms include **UBERON:0001638 vein**, **UBERON:0002018 blood vasculature**, **UBERON:0002048 lung**, **UBERON:0000955 brain**, **UBERON:0002107 liver**, **UBERON:0000948 heart**, and site-specific vein terms from the current Uberon release. DVT is commonly unilateral; PE may be unilateral or bilateral; purpura fulminans is multifocal/symmetric.

## 8. Temporal development

Inherited predisposition is present from conception but typically manifests as an **acute, episodic event in adulthood**. Risk increases with age and cumulative exposures. Severe biallelic PROC/PROS1 defects present neonatally. Pediatric carriers can remain asymptomatic but become vulnerable during risk periods: in a prospective cohort, six VTEs occurred among 70 carriers over 287 observation-years—2.09% per patient-year—versus none among 64 noncarriers; 4/14 carriers exposed to a risk period developed VTE (human prospective cohort; Tormene et al., 2020, DOI: https://doi.org/10.1182/bloodadvances.2020002781).

There is no conventional staging system. A useful temporal model is: predisposition → provoking period → acute thrombosis → 3–6-month treatment phase → resolution, recurrence, or chronic sequelae. Genetic susceptibility is lifelong; the clot itself may resolve or organize. Critical intervention windows are prophylaxis before surgery/immobility and pregnancy/postpartum exposure, rapid anticoagulation after acute VTE, and reassessment before stopping therapy.

## 9. Inheritance and population

Most heterozygous F5, F2, SERPINC1, PROC and PROS1 thrombophilias behave as **autosomal-dominant susceptibility traits with incomplete, age- and exposure-dependent penetrance and variable expressivity**. Severe biallelic PROC/PROS1 disease is recessive and can cause neonatal purpura fulminans. Rare **F9** gain-of-function thrombophilia is X-linked. Anticipation is not expected; germline mosaicism is not a prominent established feature.

Factor V Leiden has a founder distribution concentrated in European-derived populations and is uncommon in many East Asian and sub-Saharan African populations. F2 G20210A is also enriched in European/Mediterranean ancestry. Protein-deficiency variants are individually rare and geographically heterogeneous. Sex differences are dominated by pregnancy and estrogen exposure rather than simple Mendelian sex ratios.

“Prevalence of thrombophilia” cannot be represented by one valid global number because the umbrella includes common susceptibility alleles, rare high-risk deficiencies, and acquired conditions. Likewise, incidence applies more meaningfully to VTE—roughly 1–2 per 1,000 person-years in many adult populations, rising steeply with age—than to a lifelong genotype. Population ascertainment and ancestry must accompany every estimate.

## 10. Diagnostics

### Distinguish acute-event diagnosis from thrombophilia testing

Suspected DVT/PE is evaluated with clinical pretest probability, D-dimer where appropriate, and objective imaging—compression ultrasonography for DVT and CT pulmonary angiography or V/Q scanning for PE. D-dimer is a fibrin-degradation marker and cannot define the underlying inherited state.

### Core thrombophilia evaluation

* **F5 Leiden:** APC-resistance assay followed by targeted genotyping; DNA testing is unaffected by anticoagulation.
* **F2 G20210A:** targeted genotyping.
* **Antithrombin:** activity first; if low, antigen and activity:antigen ratio, then genetics where actionable. Exclude liver dysfunction, proteinuria, DIC, acute thrombosis, surgery and heparin. The ISTH communication states: “**Hereditary deficiency of antithrombin…causes a thrombophilia with a high risk for venous thromboembolism**” (Van Cott et al., 2020, DOI: https://doi.org/10.1111/jth.14648).
* **Protein C:** functional activity ± antigen; repeat when stable and off interfering vitamin-K antagonism.
* **Protein S:** free protein-S antigen ± activity; interpret using sex/age/pregnancy-specific ranges and repeat outside pregnancy, estrogen exposure, acute illness and vitamin-K antagonism.
* **APS:** lupus anticoagulant plus IgG/IgM anticardiolipin and anti-β2GPI; persistence must be demonstrated according to APS criteria. Anticoagulants can produce false lupus-anticoagulant results.

Do not measure natural anticoagulants during the acute phase if the result will be distorted; guidance summarized in the retrieved literature recommends testing after approximately three months of anticoagulation/clinical stabilization (miceli2025fromcirculatingbiomarkers pages 6-8). DOACs, heparins and warfarin interfere with multiple clot-based assays. DOAC-Stop/DOAC-Remove/filtration can reduce interference but may be incomplete and require local validation.

### Who should be tested?

Testing should answer a management question. Higher-yield situations include young/recurrent VTE, strong first-degree family history, unusual sites, suspected severe natural-anticoagulant deficiency, neonatal purpura fulminans, or suspected APS—particularly if results change anticoagulant choice/duration, pregnancy prophylaxis, estrogen decisions, or family counseling.

ASH 2023 advises against routine testing after unprovoked VTE when the default is continuing anticoagulation; conditionally supports selected testing after hormonal or major transient provoking factors and in cerebral/splanchnic thrombosis if clinicians otherwise intend to stop anticoagulation. It recommends against universal testing before combined oral contraception but supports selective testing in families with known antithrombin, protein C or protein S deficiency (miceli2025fromcirculatingbiomarkers pages 8-9, miceli2025fromcirculatingbiomarkers pages 6-8). BSH 2022 discourages routine inherited testing after clearly provoked VTE, arterial thrombosis, unusual-site thrombosis without a management implication, and indiscriminate asymptomatic-relative screening (miceli2025fromcirculatingbiomarkers pages 5-6).

**Not recommended routinely:** MTHFR C677T/A1298C, PAI-1 polymorphisms, broad “thrombophilia panels,” WES/WGS, RNA-seq, CMA, karyotype, FISH, mitochondrial or repeat-expansion testing. WES/WGS may be considered in severe unexplained familial disease through specialist/research pathways but generates VUS and is not first-line.

Differentials include local compression, cancer-associated thrombosis, APS, HIT/VITT, myeloproliferative neoplasm, PNH, nephrotic/liver disease, DIC, severe infection, and medication-associated thrombosis.

## 11. Outcome and prognosis

Thrombophilia alone does not supply a meaningful five-year survival statistic. Prognosis is determined by thrombus location/severity, recurrence, cancer/cardiopulmonary comorbidity, bleeding risk, and treatment. Acute PE can be fatal; DVT may lead to PTS; recurrent emboli may lead to chronic thromboembolic pulmonary hypertension. Long-term anticoagulation reduces recurrence but increases bleeding.

Active cancer and an unprovoked first event are stronger recurrence predictors than most common inherited variants. Triple-positive APS is a high-recurrence acquired state and generally warrants long-term VKA rather than a DOAC (miceli2025fromcirculatingbiomarkers pages 8-9). Common thrombophilia has at most modest association with arterial disease; indiscriminate arterial-thrombosis testing is therefore low value.

QoL should be measured with **VEINES-QOL/Sym** for chronic venous disease/PTS, **PEmb-QoL** after PE, and generic **EQ-5D/SF-36/PROMIS**. Recovery after uncomplicated treated DVT/PE is often good, but persistent edema, pain, exercise limitation and recurrence anxiety can be substantial.

## 12. Treatment

Thrombophilia without thrombosis is generally **not** an indication for continuous anticoagulation. Treat the event and provoking context.

* **Acute VTE:** therapeutic anticoagulation with a DOAC (apixaban, rivaroxaban, edoxaban or dabigatran), LMWH, unfractionated heparin, or warfarin according to renal/hepatic function, pregnancy, cancer, APS, interactions, bleeding risk and anatomy. Suggested NCIt terms: **Anticoagulant Therapy**, **Direct Factor Xa Inhibitor**, **Low Molecular Weight Heparin**, **Vitamin K Antagonist**.
* **Duration:** usually at least three months; extend for unprovoked/recurrent VTE, persistent risk, APS, active cancer or high-risk thrombophilia when recurrence risk exceeds bleeding risk. Genotype alone rarely decides duration.
* **APS:** warfarin/VKA is preferred for high-risk triple-positive APS; DOAC protection is inferior in this group (miceli2025fromcirculatingbiomarkers pages 8-9).
* **Pregnancy:** LMWH is preferred because it does not cross the placenta; warfarin is teratogenic and DOACs are generally avoided. Prophylaxis depends on prior VTE, thrombophilia severity and family history—not genotype alone.
* **Severe protein C deficiency/purpura fulminans:** protein C concentrate, anticoagulation and intensive supportive care; severe antithrombin deficiency may require antithrombin concentrate in selected high-risk situations.
* **Interventions:** thrombolysis, thrombectomy, catheter-directed therapy, IVC filter or surgical embolectomy are reserved for selected life-/limb-threatening situations or contraindication/failure, not for thrombophilia itself.

For CVT, a 2024 meta-analysis of four RCTs/270 participants found similar recanalization with DOACs versus standard therapy (78.2% vs 83.2%) and no significant difference in major bleeding (1.2% vs 2.4%). The authors concluded: “**DOACs and standard of care showed similar efficacy and safety profiles**” (Chen et al., published 2024, DOI: https://doi.org/10.1177/10760296241256360). Applicability to triple-positive APS and pregnancy is limited.

No approved gene, cell, CRISPR, or RNA therapy treats common thrombophilia. Reducing antithrombin or protein S is being explored to rebalance **bleeding disorders**, but that strategy can itself create thrombosis and is not therapy for thrombophilia.

## 13. Prevention

* **Primary:** avoid smoking and obesity; maintain mobility; manage cancer/inflammation; use perioperative/hospital VTE-risk assessment; avoid estrogen-containing contraception/HRT in high-risk carriers or women with prior estrogen-related VTE; provide LMWH prophylaxis during defined high-risk periods when indicated.
* **Secondary:** recognize VTE promptly and ensure adequate anticoagulant dose/duration/adherence. Thrombophilia testing is secondary prevention only when it changes management.
* **Tertiary:** manage PTS with activity, compression for symptom relief where appropriate, venous-ulcer care, rehabilitation and CTEPH referral; prevent recurrence while minimizing bleeding.
* **Screening:** no population or newborn screening. Selective cascade testing is reasonable for a known severe **SERPINC1/PROC/PROS1** familial defect when results will alter prophylaxis, pregnancy or estrogen decisions. APS is acquired, so relatives should not be screened merely because of family membership (miceli2025fromcirculatingbiomarkers pages 8-9).
* **Reproductive counseling:** explain incomplete penetrance, 50% transmission risk for many heterozygous AD variants, and the distinction between carrying a susceptibility allele and having had VTE. Prenatal/PGT is technically possible for severe familial variants but rarely appropriate for common low-penetrance F5/F2 alleles.
* **Immunization:** no vaccine prevents inherited thrombophilia. Routine vaccination benefits generally outweigh rare VITT risk; VITT requires its own diagnostic pathway.

## 14. Other species and natural disease

Naturally occurring thrombosis and inherited anticoagulant deficiencies occur in dogs, cats and horses, but veterinary evidence is fragmented and breed-specific. Candidate orthologs include canine/feline/equine **F5, F2, SERPINC1, PROC** and **PROS1**. Veterinary database confirmation through OMIA and current NCBI Taxonomy/Gene records is required before assigning a VBO breed term. Thrombophilia is not infectious or zoonotic; there is no cross-species transmission.

Comparative value lies in conserved coagulation biology, not identical epidemiology. Species differences in platelets, coagulation-factor levels, vessel size and experimental injury mean that animal thrombosis phenotypes do not directly estimate human penetrance.

## 15. Model organisms

* **Mouse (NCBI Taxon 10090):** F5 Leiden knock-in, **Serpinc1/Proc/Pros1** loss-of-function and conditional endothelial/platelet models. Complete protein C/S pathway disruption may cause embryonic/neonatal lethality or widespread thrombosis, whereas conditional models isolate cell-specific mechanisms. Endothelial thrombomodulin loss causes juvenile-onset thrombosis; platelet-specific Pros1 loss selectively augments low-shear venous thrombosis.
* **Zebrafish (Taxon 7955):** transparent embryos and scalable genetics permit live thrombosis imaging and modifier screens. Complete protein C versus protein S loss can yield different phenotypes, illustrating that nominally linked anticoagulant pathways are not biologically interchangeable.
* **Rat/rabbit/pig:** stasis, stenosis, endothelial injury and catheter models support pharmacology/device studies but model an induced thrombus more than lifelong inherited susceptibility.
* **In vitro:** calibrated thrombin generation, endothelial–platelet flow systems, plasma reconstitution, hepatocyte models, and patient-derived iPSC endothelium/hepatocytes can test variant function.

Limitations include severe knockout lethality, supraphysiologic injury, interspecies hemostatic differences, and weak modeling of aging, cancer, pregnancy, obesity and polygenic background. Resources include MGI, IMPC, IMSR/MMRRC, ZFIN and the Alliance of Genome Resources.

## Recent developments and active implementation

1. **Guideline shift (2023):** ASH formalized decision-model-based selective testing. The major implication is that a positive result has little value if anticoagulation management will not change (miceli2025fromcirculatingbiomarkers pages 8-9, miceli2025fromcirculatingbiomarkers pages 6-8).
2. **CVT management (2024):** German consensus guidance does not recommend general thrombophilia screening; it considers testing in young, spontaneous/recurrent CVT or positive family history when therapy would change. It increasingly accepts DOACs after the acute phase, while pregnancy prophylaxis remains LMWH-based.
3. **Laboratory implementation:** adsorbent/filtration products can remove DOACs before clot-based assays, but incomplete removal and assay-specific validation remain concerns.
4. **Risk prediction:** polygenic scores, thrombin generation, extracellular vesicles, NET/cfDNA markers and machine learning are research tools—not replacements for clinical risk assessment.
5. **Trials/registries:** active examples include **NCT04537416 FREYA** (fertility, hypercoagulability and inflammation; observational; 1,000), **NCT03206372** (VTE risk during hormonal exposure; observational; 2,640), **NCT03910933 KIDCLOT** (pediatric thrombosis/thrombophilia education; 248), and **NCT06153394** (post-hepatectomy hypercoagulability; planned phase 3; 50). These study risk assessment/implementation rather than curative therapy.

## Expert interpretation and evidence gaps

The most authoritative interpretation is that thrombophilia testing is a **decision aid, not a diagnosis-generating fishing expedition**. High-value results identify severe natural-anticoagulant deficiency or APS that changes pregnancy prophylaxis, estrogen counseling, family testing, anticoagulant duration, or—in APS—drug class. Low-value testing during acute thrombosis or anticoagulation creates false diagnoses, anxiety, insurance/employment concerns, unnecessary lifelong anticoagulation and avoidable bleeding.

Pregnancy-loss evidence needs particular caution. The 2024 Romanian cohort and earlier meta-analyses report associations, but selected referral populations, multiple-comparison testing, disputed markers such as MTHFR/PAI-1, and uncertain LMWH benefit prevent universal screening or genotype-directed treatment. ESHRE guidance conditionally recommends against LMWH for inherited-thrombophilia-associated recurrent loss because certainty is low (borsi2024riskfactorsof pages 12-13, borsi2024riskfactorsof pages 2-3).

The largest knowledge gaps are ancestry-diverse penetrance estimates, standardized functional interpretation of rare variants, prospective proof that testing improves outcomes, integration of polygenic/environmental risk, and validated omics markers. Until these are resolved, the appropriate knowledge-base representation is a hierarchy of molecular subtypes plus acquired causes and event phenotypes—not one monolithic disease with a single prevalence, prognosis, or treatment.

References

1. (OpenTargets Search: thrombophilia): Open Targets Query (thrombophilia, 23 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (miceli2025fromcirculatingbiomarkers pages 8-9): Giuseppe Miceli, Anna Maria Ciaccio, and Antonino Tuttolomondo. From circulating biomarkers to polymorphic variants: a narrative review of challenges in thrombophilia evaluation. May 2025. URL: https://doi.org/10.3390/jcm14103448, doi:10.3390/jcm14103448. This article has 17 citations.

3. (miceli2025fromcirculatingbiomarkers pages 6-8): Giuseppe Miceli, Anna Maria Ciaccio, and Antonino Tuttolomondo. From circulating biomarkers to polymorphic variants: a narrative review of challenges in thrombophilia evaluation. May 2025. URL: https://doi.org/10.3390/jcm14103448, doi:10.3390/jcm14103448. This article has 17 citations.

4. (miceli2025fromcirculatingbiomarkers pages 5-6): Giuseppe Miceli, Anna Maria Ciaccio, and Antonino Tuttolomondo. From circulating biomarkers to polymorphic variants: a narrative review of challenges in thrombophilia evaluation. May 2025. URL: https://doi.org/10.3390/jcm14103448, doi:10.3390/jcm14103448. This article has 17 citations.

5. (miceli2025fromcirculatingbiomarkers pages 14-15): Giuseppe Miceli, Anna Maria Ciaccio, and Antonino Tuttolomondo. From circulating biomarkers to polymorphic variants: a narrative review of challenges in thrombophilia evaluation. May 2025. URL: https://doi.org/10.3390/jcm14103448, doi:10.3390/jcm14103448. This article has 17 citations.

6. (d’andrea2021raredefectslooking pages 2-3): Giovanna D’Andrea and Maurizio Margaglione. Rare defects: looking at the dark face of the thrombosis. International Journal of Environmental Research and Public Health, 18(17):9146, Aug 2021. URL: https://doi.org/10.3390/ijerph18179146, doi:10.3390/ijerph18179146. This article has 5 citations.

7. (d’andrea2021raredefectslooking pages 7-9): Giovanna D’Andrea and Maurizio Margaglione. Rare defects: looking at the dark face of the thrombosis. International Journal of Environmental Research and Public Health, 18(17):9146, Aug 2021. URL: https://doi.org/10.3390/ijerph18179146, doi:10.3390/ijerph18179146. This article has 5 citations.

8. (borsi2024riskfactorsof pages 12-13): Ema Borsi, Ovidiu Potre, Ioana Ionita, Miruna Samfireag, Cristina Secosan, and Cristina Potre. Risk factors of thrombophilia-related mutations for early and late pregnancy loss. Medicina, 60:521, Mar 2024. URL: https://doi.org/10.3390/medicina60040521, doi:10.3390/medicina60040521. This article has 19 citations.

9. (borsi2024riskfactorsof pages 2-3): Ema Borsi, Ovidiu Potre, Ioana Ionita, Miruna Samfireag, Cristina Secosan, and Cristina Potre. Risk factors of thrombophilia-related mutations for early and late pregnancy loss. Medicina, 60:521, Mar 2024. URL: https://doi.org/10.3390/medicina60040521, doi:10.3390/medicina60040521. This article has 19 citations.

## Artifacts

- [Edison artifact artifact-00](Thrombophilia-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| Quoted claims checked | 3 |
| Quoted claims found in source | 3 |
| Quoted claims **not** found in source | 0 |
| Quoted claims with nothing to check against | 1 |
| References weighed for topical relevance | 9 |
| On topic | 4 |
| Off topic | 0 |

### Quotes that could not be checked

There was no text to compare these against, so they are neither confirmed nor contradicted:

- `DOI:10.1111/jth.14648`: "**Hereditary deficiency of antithrombin…causes a thrombophilia with a high risk for venous thromboembolism**"
  - Reference resolved but exposes no abstract or full text to search

All extracted references resolved successfully.