---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-27T02:49:34.130924'
end_time: '2026-08-27T02:56:25.482695'
duration_seconds: 411.35
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Intellectual Disability Autosomal Dominant 52
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 16
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 1
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Intellectual_Disability_Autosomal_Dominant_52-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Intellectual Disability Autosomal Dominant 52
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Intellectual Disability Autosomal Dominant 52** covering all of the
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
- **Disease Name:** Intellectual Disability Autosomal Dominant 52
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Intellectual Disability Autosomal Dominant 52** covering all of the
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


# Intellectual Disability, Autosomal Dominant 52 (MRD52): Research Report

## Executive summary

Intellectual disability, autosomal dominant 52 (MRD52) is an ultra-rare, congenital neurodevelopmental chromatinopathy caused principally by heterozygous pathogenic variants in **ASH1L**, usually through loss of function or haploinsufficiency. The phenotype is variable but centers on developmental delay/intellectual disability, severe speech-language impairment, autism or other behavioral abnormalities, and sometimes hypotonia, dysmorphism, and epilepsy. ASH1L is a Trithorax-family histone lysine methyltransferase that promotes transcriptionally permissive chromatin, principally through H3K36 methylation and associated H3K4 methylation, while opposing Polycomb repression. No disease-specific therapy, validated biomarker, prevalence estimate, or dedicated clinical trial was identified. The most important 2024 advances are mechanistic: a peer-reviewed Ash1l-haploinsufficient mouse study implicated excessive prefrontal cortical excitability, while a December 2024 bioRxiv study found impaired neurite growth, transcription, and chromatin regulation in engineered human neurons. Both remain preclinical. (ma2024chemogeneticinhibitionof pages 12-13, wilson2022reprogrammingofthe pages 14-15, jhanji2024dynamicregulationof pages 4-7)

The following compact table summarizes the knowledge-base-level conclusions.

| Domain | Key facts | Ontology / controlled-term suggestions | Evidence |
|---|---|---|---|
| Disease identity / identifiers | Intellectual disability, autosomal dominant 52 (MRD52); ASH1L-related neurodevelopmental disorder; OMIM **617796**; MONDO **MONDO:0030918**. Disease-level knowledge is aggregated from published case reports/cohorts, reviews, and curated disease-target resources rather than EHR-only evidence. | MONDO:0030918 | (OpenTargets Search: Intellectual disability, autosomal dominant 52, wilson2022reprogrammingofthe pages 14-15) |
| Synonyms | ASH1L-related intellectual developmental disorder; ASH1L-related neurodevelopmental disorder; MRD52; intellectual developmental disorder with speech delay/autism features due to **ASH1L**. | MeSH/ICD-specific synonym mapping not established in retrieved evidence | (wilson2022reprogrammingofthe pages 14-15) |
| Inheritance | **Autosomal dominant**; most reported pathogenic events are interpreted as **heterozygous loss-of-function / haploinsufficiency**, often de novo in sequencing cohorts. Penetrance and recurrence risk are not well quantified; parental testing is important to assess de novo status and mosaicism. | HP:0000006 Autosomal dominant inheritance | (OpenTargets Search: Intellectual disability, autosomal dominant 52, wilson2022reprogrammingofthe pages 14-15, jhanji2024dynamicregulationof pages 1-4) |
| Causal gene / protein | **ASH1L** (also called **KMT2H**), encoding ASH1-like histone lysine methyltransferase, a Trithorax-family chromatin regulator expressed in brain and involved in transcriptional activation. | HGNC:19208 ASH1L; UniProt ASH1L protein | (wilson2022reprogrammingofthe pages 14-15, jhanji2024dynamicregulationof pages 1-4) |
| Pathogenic mechanism | Predominant mechanism is **germline monoallelic loss of function / haploinsufficiency** disrupting chromatin-mediated transcription. ASH1L catalyzes **H3K36me2** and contributes to **H3K4me3**, opposing **PRC2/H3K27me3** repression; downstream effects include altered neuronal gene expression, neurite growth, synaptic programs, and cortical excitability. The 2024 human-neuron study is a **bioRxiv preprint**. | GO:0046975 histone methyltransferase activity; GO:0018024 histone H3-K36 methylation; GO:0046968 H3-K4 methylation; GO:0006357 regulation of transcription by RNA polymerase II; GO:0030154 cell differentiation | (ma2024chemogeneticinhibitionof pages 12-13, wilson2022reprogrammingofthe pages 14-15, jhanji2024dynamicregulationof pages 4-7, jhanji2024dynamicregulationof pages 1-4, jhanji2024dynamicregulationof pages 10-12) |
| Core phenotypes | Developmental delay and **intellectual disability** (mild to severe reported), marked **speech/language delay**, **autism spectrum disorder / autistic behaviors**, dysmorphic facial features, and behavioral abnormalities; some patients have seizures/epilepsy or broader neuropsychiatric manifestations. Precise phenotype frequencies are not robustly established in retrieved evidence. | HP:0001263 Global developmental delay; HP:0001249 Intellectual disability; HP:0000750 Delayed speech and language development; HP:0000729 Autism; HP:0001250 Seizure; HP:0000717 Autism spectrum disorder; HP:0001252 Hypotonia; HP:0001999 Facial dysmorphism | (wilson2022reprogrammingofthe pages 14-15, jhanji2024dynamicregulationof pages 1-4, jhanji2024dynamicregulationof pages 39-41) |
| Principal anatomy / cell types | Primary system affected is the **central nervous system**, especially cortical circuits. Experimental data implicate **prefrontal cortex** and **cortical excitatory pyramidal neurons**; neuronal projections, axons, synapses, and nuclei are enriched among dysregulated compartments/features. | UBERON:0000955 brain; UBERON:0001870 cerebral cortex; UBERON:0000451 prefrontal cortex; CL:0000540 neuron; CL:0002608 pyramidal neuron; GO:0030424 axon; GO:0045202 synapse; GO:0005634 nucleus | (ma2024chemogeneticinhibitionof pages 12-13, jhanji2024dynamicregulationof pages 4-7, jhanji2024dynamicregulationof pages 10-12) |
| Diagnosis | Molecular diagnosis relies on **exome/genome sequencing** or neurodevelopmental disorder/intellectual disability panels that include **ASH1L**; trio-based testing is particularly valuable to establish de novo occurrence. No disease-specific biochemical biomarker or imaging signature was established in retrieved evidence. | NCIT:C101294 Whole Exome Sequencing; NCIT:C84351 Whole Genome Sequencing; NCIT:C157640 Molecular Genetic Testing | (OpenTargets Search: Intellectual disability, autosomal dominant 52, wilson2022reprogrammingofthe pages 14-15) |
| Treatment / management | No **approved disease-specific therapy** identified. Current care is **supportive and multidisciplinary**: developmental pediatrics, neurology, speech-language therapy, occupational/physical therapy, behavioral/educational interventions, and seizure management when present. **Preclinical only:** in Ash1l mouse or edited human-neuron systems, chemogenetic PFC inhibition and epigenetic drugs (**tazemetostat**, **vorinostat**) rescued selected phenotypes; these are not established patient treatments. | NCIT:C51909 Supportive Care; NCIT:C17556 Speech Therapy; NCIT:C15635 Occupational Therapy; NCIT:C15313 Physical Therapy; NCIT:C146712 Behavioral Intervention; NCIT:C15246 Tazemetostat; NCIT:C1820 Vorinostat | (ma2024chemogeneticinhibitionof pages 12-13, jhanji2024dynamicregulationof pages 34-39, jhanji2024dynamicregulationof pages 39-41) |
| Epidemiology / prognosis | Appears to be an **ultra-rare Mendelian disorder**; no reliable prevalence or incidence estimates were identified in retrieved evidence. Natural history is incompletely defined; morbidity is dominated by lifelong neurodevelopmental impairment, communication disability, behavioral challenges, and possible epilepsy. Disease-specific survival, life expectancy, and mortality rates are unavailable. | Orphan/rare disease category; chronic neurodevelopmental disorder | (wilson2022reprogrammingofthe pages 14-15) |
| Model systems | **Mouse:** Ash1l haploinsufficiency/gene-trap models show social deficits, repetitive grooming, cognitive impairment, EEG epileptiform activity/absence-like seizures, and increased PFC excitability. **Human neuronal models:** CRISPR-engineered iPSC/ESC-derived cortical excitatory neurons (including **E2148*** catalytic-domain variant) show reduced neurite length/arborization and altered histone marks/transcriptomes; this 2024 study is a **bioRxiv preprint**. **Zebrafish:** ash1a knockdown reduces neuron numbers in pineal gland. | NCBITaxon:10090 Mus musculus; NCBITaxon:7955 Danio rerio; CL:0000540 neuron; CL:0002608 pyramidal neuron | (ma2024chemogeneticinhibitionof pages 12-13, wilson2022reprogrammingofthe pages 14-15, jhanji2024dynamicregulationof pages 4-7, jhanji2024dynamicregulationof pages 26-29) |
| Key evidence gaps | Major gaps include: small patient numbers; limited validated phenotype frequencies; scarce longitudinal natural-history data; poor estimates of penetrance/expressivity; no established episignature/clinical biomarker in retrieved evidence; no disease-specific interventional trials found; limited patient-cell functional studies in peer-reviewed literature; 2024 human-neuron rescue work remains **preprint/preclinical**. | Evidence-gap annotation | (wilson2022reprogrammingofthe pages 14-15, jhanji2024dynamicregulationof pages 1-4, jhanji2024dynamicregulationof pages 39-41) |


*Table: Compact knowledge-base table summarizing identifiers, genetics, phenotypes, mechanism, diagnosis, management, models, and current evidence gaps for Intellectual disability, autosomal dominant 52 / ASH1L-related disorder. It separates established disease knowledge from preclinical and preprint findings.*

## 1. Disease information

**Definition.** MRD52 is a monogenic developmental disorder in which deficient ASH1L dosage disrupts chromatin-dependent neuronal development. It belongs to the Mendelian intellectual-developmental disorders and more broadly to the “chromatinopathies.” Reported severity ranges from mild to severe intellectual disability, with developmental and speech delay, autism-spectrum manifestations, and variable dysmorphism. (wilson2022reprogrammingofthe pages 14-15)

**Identifiers and names**

- **MONDO:** MONDO:0030918.
- **OMIM phenotype:** **617796**, Intellectual disability, autosomal dominant 52.
- **Common abbreviations/synonyms:** MRD52; ASH1L-related intellectual developmental disorder; ASH1L-related neurodevelopmental disorder.
- **Gene:** ASH1L, also called KMT2H; Ensembl ENSG00000116539.
- A unique disease-specific ICD-10, ICD-11, or MeSH code was not established in the retrieved evidence; patients are ordinarily coded under intellectual disability, developmental disorder, autism, or epilepsy as appropriate.

Open Targets associates ASH1L with MONDO:0030918 and links the association to, among other studies, **PMID 28394464**, **23033978**, and **28191889**. It also returned a weaker LMAN2L association, but the present phenotype’s established molecular definition is ASH1L-related; the weaker result should not be used as an alternative causal assignment without re-curation. (OpenTargets Search: Intellectual disability, autosomal dominant 52)

The evidence is **aggregated disease-level evidence** from sequencing cohorts, case reports, curated databases, reviews, and experimental studies—not an analysis of an individual patient’s EHR.

## 2. Etiology, risk, protection, and environment

### Causal factor

The primary cause is a **germline heterozygous pathogenic ASH1L variant**. Protein-truncating nonsense, frameshift, and splice-disrupting alleles are consistent with loss of function and haploinsufficiency; damaging catalytic-domain alleles can similarly impair histone methyltransferase activity. The experimentally modeled **p.Glu2148Ter (E2148\*)** allele is a catalytic-domain truncation associated with ASD, ID, and epilepsy. (jhanji2024dynamicregulationof pages 4-7, jhanji2024dynamicregulationof pages 1-4)

### Risk factors

- **Genetic:** carrying a pathogenic ASH1L allele is the principal risk factor. Most recognized cases appear sporadic/de novo, although autosomal-dominant transmission is biologically possible.
- **Family history:** an affected heterozygous parent would imply a 50% transmission probability per pregnancy, subject to variable expressivity. If apparently de novo, recurrence is low but not zero because parental germline mosaicism cannot be excluded.
- **Modifiers:** no validated modifier gene, founder allele, ancestry-specific risk, sex-specific penetrance, or polygenic modifier has been established.

No reliable disease-specific environmental, lifestyle, occupational, infectious, maternal-age, or sex risk factor has been demonstrated. Prenatal exposures associated with neurodevelopmental disorders generally should not be represented as causes or modifiers of molecularly confirmed MRD52 without direct evidence.

### Protective factors and gene–environment interaction

No protective ASH1L allele, diet, drug, lifestyle exposure, or reproducible gene–environment interaction is known. Ordinary developmental supports may improve function but do not prevent the genotype. Infectious and zoonotic causation are not applicable.

## 3. Phenotypes

Because published cohorts are small and ascertainment differs, **robust percentages are unavailable**. Qualitative frequencies should therefore be encoded as “common,” “variable,” or “reported,” not as inferred percentages.

- **Global developmental delay — HP:0001263:** typically evident in infancy or early childhood; variable severity; chronic rather than episodic. It affects acquisition of communication, learning, self-care, and adaptive skills.
- **Intellectual disability — HP:0001249:** mild through severe; generally lifelong and non-remitting. Formal severity may become clearer during childhood as cognitive demands increase. (wilson2022reprogrammingofthe pages 14-15)
- **Delayed speech and language development — HP:0000750; absent speech, if applicable — HP:0001344:** often especially prominent. Childhood apraxia of speech has also been discussed within the expanding genetic spectrum of ASH1L-associated speech disorders, but should be assigned only after specialist motor-speech assessment.
- **Autism/autistic behavior — HP:0000729 or HP:0000717:** social-communication impairment, restricted interests, repetitive behavior, or formal ASD may occur. Behavioral consequences can substantially affect education, family participation, and independent living. (wilson2022reprogrammingofthe pages 14-15, jhanji2024dynamicregulationof pages 1-4)
- **Seizures/epilepsy — HP:0001250 / HP:0001251:** variably reported rather than obligatory. The experimental literature particularly supports susceptibility to absence-like and convulsive seizures, but mouse seizure type should not automatically be assigned to every patient. (ma2024chemogeneticinhibitionof pages 12-13)
- **Hypotonia — HP:0001252:** reported in the clinical spectrum and may contribute to delayed motor milestones, poor coordination, feeding difficulty, or need for physical therapy.
- **Facial dysmorphism — HP:0001999:** variable and generally nonspecific; it is not sufficiently distinctive to diagnose the disorder clinically. (wilson2022reprogrammingofthe pages 14-15)
- **Other neuropsychiatric associations:** ASH1L variation has been reported across ADHD, Tourette syndrome, schizophrenia, ASD, ID, and epilepsy. These broader associations demonstrate pleiotropy but are not all defining manifestations of MRD52. The 2024 preprint catalogued 136 disease-associated ASH1L variants across these phenotypes. (jhanji2024dynamicregulationof pages 1-4)

No disease-specific laboratory abnormality, metabolite signature, immune phenotype, or pathognomonic MRI pattern is established. Quality-of-life studies using EQ-5D, SF-36, PROMIS, or a disease-specific instrument were not found; impact must presently be inferred from communication, cognitive, behavioral, and seizure burden.

## 4. Genetic and molecular information

**ASH1L** encodes a large nuclear chromatin regulator and histone lysine methyltransferase. The dominant disease mechanism is best represented as **haploinsufficiency/loss of function**, although individual missense variants require case-specific functional and ACMG/AMP assessment. Disease-associated classes include nonsense, frameshift, splice, and damaging missense/catalytic-domain variants. (wilson2022reprogrammingofthe pages 14-15, jhanji2024dynamicregulationof pages 4-7)

For a knowledge base, each variant should retain transcript-specific HGVS nomenclature, genome build, inheritance, ClinVar assertion and review status, and gnomAD frequency. Pathogenic truncating alleles are expected to be absent or extremely rare in population databases, but no universal allele frequency can be assigned without variant-level lookup. The variants are **germline**, not a recognized somatic cancer mechanism in this disease.

No validated modifier genes or MRD52-specific diagnostic DNA-methylation episignature were identified. ASH1L can be affected within larger copy-number alterations, but a broad deletion involving neighboring genes should not be assumed phenotypically equivalent to an intragenic ASH1L loss-of-function allele.

## 5. Environmental, lifestyle, and infectious information

MRD52 is not known to be caused by toxins, radiation, pollution, occupation, smoking, alcohol, diet, inactivity, or infection. Such exposures can independently influence development or pregnancy outcome but have no demonstrated disease-specific causal interaction with ASH1L. There is no vaccine, antimicrobial prophylaxis, or environmental remediation specific to MRD52.

## 6. Mechanism and pathophysiology

### Upstream molecular defect

ASH1L promotes active chromatin through **H3K36me2** and associated **H3K4me3** and counteracts PRC2-mediated H3K27me3 repression. It is expressed in embryonic and adult brain and participates in developmental gene activation, including HOX regulation. Suggested terms include GO:0018024, histone H3-K36 methylation; GO:0046968, histone H3-K4 methylation; GO:0006357, regulation of transcription by RNA polymerase II; and GO:0046975, histone methyltransferase activity. (wilson2022reprogrammingofthe pages 14-15, jhanji2024dynamicregulationof pages 1-4)

### Causal chain

**Pathogenic heterozygous ASH1L variant → reduced functional methyltransferase dosage/activity → altered H3K36/H3K4 and Polycomb-related chromatin states → inefficient transcription and altered isoform use of long neuronal, axonal, ion-channel, and synaptic genes → impaired neurite growth, neuronal connectivity, and excitation/inhibition balance → developmental delay, ID, autism-related behavior, speech impairment, and seizure susceptibility.** Human patient-level genotype–mechanism correspondence remains less mature than the experimental evidence. (jhanji2024dynamicregulationof pages 4-7, jhanji2024dynamicregulationof pages 7-10, jhanji2024dynamicregulationof pages 10-12)

### 2024 human-neuron findings—preprint evidence

CRISPR-engineered human cortical excitatory neurons carrying E2148* showed mean neurite length of **47.47 ± 1.99 μm** versus **56.9 ± 2.41 μm** in controls (P<0.004), total neurite length of **139.3 ± 4.66 μm** versus **182.7 ± 6.39 μm** (P<0.0001), and a lower complexity index, **228.8 ± 13.42** versus **289.5 ± 18.21** (P<0.0099). (jhanji2024dynamicregulationof pages 26-29)

The same system showed H3K36me2 at **67%**, H3K4me3 at **68%**, and H3K36me3 at **78%** of control. Nascent-transcription signal fell from **1.017 ± 0.029** to **0.817 ± 0.027** (P<0.0001). Transcriptomic analysis identified **2,475 differentially expressed genes** in one analysis, with enrichment for axon guidance, axonogenesis, nervous-system development, transcription, and synaptic function; 263 dysregulated genes overlapped SFARI ASD genes. Long genes above 100 kb were preferentially downregulated, and 57 genes showed differential transcript usage, including **SMARCA4, AFF2, and TARDBP**. These findings are important but came from a December 2, 2024 bioRxiv preprint and require independent peer-reviewed replication. URL: https://doi.org/10.1101/2024.12.02.625500. (jhanji2024dynamicregulationof pages 4-7, jhanji2024dynamicregulationof pages 7-10, jhanji2024dynamicregulationof pages 10-12, jhanji2024dynamicregulationof pages 29-34)

### Cellular systems

Relevant processes include axonogenesis (GO:0007409), neuron projection development (GO:0031175), synapse organization (GO:0050808), regulation of membrane potential (GO:0042391), and nervous-system development (GO:0007399). Principal suggested cell terms are neuron (CL:0000540), glutamatergic neuron (CL:0000679), and pyramidal neuron (CL:0002608). No convincing primary metabolic, immune, inflammatory, fibrotic, ischemic, or degenerative mechanism has been demonstrated.

## 7. Anatomical structures affected

The principal organ is the **brain** (UBERON:0000955), particularly the **cerebral cortex** (UBERON:0001870). Mouse electrophysiology implicates the **prefrontal cortex** (UBERON:0000451), where Ash1l haploinsufficiency increases pyramidal-neuron excitability through enhanced glutamatergic transmission, reduced GABAergic inhibition, and altered intrinsic properties. Relevant subcellular compartments include nucleus (GO:0005634), chromatin (GO:0000785), axon (GO:0030424), dendrite (GO:0030425), and synapse (GO:0045202). (ma2024chemogeneticinhibitionof pages 12-13)

No consistent lateralization is known. Dysmorphic or skeletal findings may occur, but nervous-system dysfunction is primary.

## 8. Temporal development and natural history

The molecular defect is present from conception and acts during prenatal and postnatal neurodevelopment. Clinical recognition is usually pediatric and insidious—through delayed milestones, language delay, hypotonia, behavior, or seizures—rather than an acute onset. MRD52 is chronic and lifelong; there is no established staging system, remission pattern, or end-stage phase. Developmental gains may occur with maturation and therapy, but underlying intellectual and adaptive impairment generally persists. Longitudinal studies are insufficient to determine whether epilepsy, behavior, or cognition systematically improves or worsens with age.

Early childhood is likely the most important intervention window because language, motor, and social circuits are developing, although no ASH1L-specific critical-period trial has established an optimal time.

## 9. Inheritance and population

Inheritance is **autosomal dominant** (HP:0000006), with many diagnoses arising from de novo variants. Expressivity is variable; penetrance has not been accurately quantified. Anticipation, repeat expansion, consanguinity, a founder effect, and a carrier frequency are not established features. Germline mosaicism remains a counseling consideration after an apparently de novo result.

The disease is ultra-rare, but no defensible incidence per 100,000, prevalence, geographic concentration, ethnic enrichment, age distribution, or sex ratio was found. Absence of epidemiologic estimates reflects limited ascertainment rather than proof of equal distribution.

## 10. Diagnostics

### Recommended approach

1. Perform clinical developmental, neurologic, behavioral, speech-language, hearing, vision, growth, and dysmorphology assessment.
2. Use **trio exome sequencing or genome sequencing**, or a comprehensive developmental-delay/ID/epilepsy panel containing ASH1L. Trio analysis helps establish de novo status and reduces uncertainty.
3. Confirm reportable variants by an orthogonal method where required and test both parents. Apply ACMG/AMP criteria, including predicted loss of function, population absence, segregation, phenotype fit, and functional evidence.
4. Use chromosomal microarray when copy-number disease remains possible; genome sequencing may detect both sequence and structural variants. Karyotype or FISH is indicated only when a larger rearrangement is suspected.
5. Consider RNA sequencing for a suspected splice variant or unresolved case, but it is not a routine validated MRD52 diagnostic biomarker.

No enzyme assay, blood biomarker, metabolomic test, biopsy, liquid biopsy, or established epigenomic signature diagnoses MRD52. MRI and EEG are **phenotype-directed**: MRI for focal neurologic signs, abnormal head growth, regression, or seizures; EEG for suspected seizures or developmental regression. Mitochondrial and repeat-expansion testing are not disease-specific.

### Differential diagnosis

The differential includes other chromatinopathies and monogenic NDDs—SETD5-, KMT2A-, KMT2D-, KDM5B-, CHD8-, ARID1B-, ASXL3-, TCF4-, and FOXP-related disorders—as well as Fragile X syndrome, pathogenic CNVs, metabolic disease when clinically indicated, cerebral palsy, nonsyndromic ASD/ID, and epilepsy-associated developmental encephalopathies. Clinical overlap is substantial, making genome-wide testing preferable to phenotype-only diagnosis.

## 11. Outcome and prognosis

No disease-specific five- or ten-year survival, mortality rate, or life-expectancy estimate is available. Available evidence does not establish MRD52 as intrinsically life-limiting, but severe epilepsy, feeding problems, accidents, or unrelated congenital disease could influence individual prognosis.

The major morbidity is lifelong impairment of cognition, communication, adaptive function, education, employment, and independent living. Prognosis is likely influenced by intellectual-disability severity, functional speech, epilepsy control, hypotonia/motor impairment, ASD/behavioral burden, and access to early services. No validated molecular prognostic biomarker exists.

## 12. Treatment and current applications

There is **no approved ASH1L-directed therapy** and no disease-specific treatment-response rate. Current real-world implementation is genotype-informed supportive care:

- individualized education and early developmental intervention;
- speech-language therapy, including augmentative and alternative communication when needed;
- occupational and physical therapy;
- behavioral and ASD-focused interventions;
- standard antiseizure treatment selected by seizure type and tolerability;
- feeding, sleep, psychiatric, hearing, vision, and orthopedic management as indicated;
- social-work, respite, and transition-to-adult-care planning.

Suggested NCIT annotations include Supportive Care (NCIT:C51909), Speech Therapy (NCIT:C17556), Occupational Therapy (NCIT:C15635), Physical Therapy (NCIT:C15313), and Behavioral Intervention (NCIT:C146712).

### Experimental therapy

In Ash1l+/GT mice, chemogenetic inhibition of prefrontal pyramidal neurons improved social deficits and abolished absence-like seizures, indicating that cortical hyperexcitability is modifiable. This DREADD experiment is mechanistic and is not a clinically available treatment. URL and publication date: *Genes*, December 2024, https://doi.org/10.3390/genes15121619. (ma2024chemogeneticinhibitionof pages 12-13)

In engineered human neurons, **tazemetostat** (EZH2 inhibitor, 0.5 μM) and **vorinostat** (HDAC inhibitor, 0.1 μM) improved selected neurite/chromatin readouts. Vorinostat increased total neurite length from **163.3 ± 4.83 μm** under vehicle to **225.2 ± 8.38 μm** and markedly increased H4K16ac; tazemetostat reduced H3K27me3. These agents have substantial systemic effects and are **not recommended for MRD52 outside ethically approved research**. (jhanji2024dynamicregulationof pages 34-39, jhanji2024dynamicregulationof pages 39-41)

No ASH1L-specific gene replacement, CRISPR, ASO, siRNA, mRNA, cell therapy, immunotherapy, surgery, pharmacogenomic rule, or registered interventional trial was identified.

## 13. Prevention

The genotype cannot be prevented by lifestyle change, vaccination, or prophylactic medication. Appropriate measures are:

- **Primary reproductive prevention:** genetic counseling, parental testing, discussion of recurrence risk, prenatal diagnosis, and preimplantation genetic testing for a known familial pathogenic variant.
- **Secondary prevention:** prompt etiologic sequencing in unexplained DD/ID and early developmental, speech, hearing, and seizure assessment.
- **Tertiary prevention:** therapies and surveillance intended to limit communication disability, contractures/deconditioning, behavioral crisis, untreated epilepsy, sleep disruption, and caregiver burden.
- **Cascade testing:** appropriate if a pathogenic variant is inherited; routine population or newborn screening is not currently justified.

## 14. Other species and natural disease

No well-characterized naturally occurring veterinary counterpart, breed predisposition, animal-to-human transmission, or zoonotic risk was identified. Relevant orthologs are **Ash1l** in mouse (*Mus musculus*, NCBI Taxon 10090) and ash1-family orthologs in zebrafish (*Danio rerio*, NCBI Taxon 7955). Conservation of chromatin regulation and neuronal-development functions makes these experimentally informative, but engineered phenotypes are not natural animal disease.

## 15. Model organisms and experimental systems

**Mouse, gene-trap haploinsufficiency.** Ash1l+/GT mice exhibited social deficits, increased self-grooming, cognitive impairment, EEG epileptiform discharges/absence-like seizures, and increased pentylenetetrazole susceptibility. Whole-cell recordings showed hyperexcitable prefrontal pyramidal neurons, enhanced glutamatergic transmission, and diminished GABAergic inhibition. This is the strongest recent peer-reviewed mechanistic model, but mouse social behavior and chemogenetic rescue do not directly predict human treatment efficacy. (ma2024chemogeneticinhibitionof pages 12-13)

**Human cellular model.** Isogenic pluripotent-stem-cell-derived cortical excitatory neurons carrying E2148* reproduced impaired neurite outgrowth, simpler arbors, altered H3K36/H3K4 regulation, reduced transcription, long-gene vulnerability, and isoform changes. Its human genetic background and cell-type specificity are strengths; lack of organismal development, glial circuitry, pharmacokinetics, and peer review are limitations. (jhanji2024dynamicregulationof pages 4-7, jhanji2024dynamicregulationof pages 7-10, jhanji2024dynamicregulationof pages 26-29)

**Zebrafish and other mouse alleles.** Zebrafish ash1a knockdown reportedly reduces pineal neuron number, while catalytically inactive Ash1l mice have skeletal anomalies and impaired fertility. These models support developmental conservation but only partially reproduce the human neurobehavioral syndrome. (wilson2022reprogrammingofthe pages 14-15)

## Authoritative interpretation and evidence gaps

The current expert interpretation is that MRD52 is best understood as a **developmental chromatin-regulation disorder**, not simply isolated intellectual disability. The convergence of human genetics, neuronal chromatin/transcriptomic data, and mouse electrophysiology supports a model in which altered epigenetic regulation produces abnormal neuronal connectivity and cortical excitation/inhibition. However, the field remains constrained by small clinical cohorts, heterogeneous variant ascertainment, limited longitudinal phenotyping, and a lack of patient-derived functional studies in peer-reviewed literature. The 2024 human-neuron work is promising but is a preprint; its epigenetic-drug rescues should be treated as hypothesis-generating rather than therapeutic evidence. (wilson2022reprogrammingofthe pages 14-15, jhanji2024dynamicregulationof pages 1-4, jhanji2024dynamicregulationof pages 39-41)

Two concise source statements capture the current evidence:

> “Clinical phenotypes in MRD52 individuals include mild-severe intellectual disability, autism spectrum disorder, speech delay, facial dysmorphisms, and developmental delay.” — synthesis of the peer-reviewed chromatin/NDD review, published October 2022, https://doi.org/10.1080/10409238.2021.1979457. (wilson2022reprogrammingofthe pages 14-15)

> “Chemogenetic inhibition of pyramidal neurons in the PFC of Ash1l+/GT mice ameliorated autism-like social deficits and abolished absence-like seizures.” — Ma et al., published December 2024, https://doi.org/10.3390/genes15121619. (ma2024chemogeneticinhibitionof pages 12-13)

Accordingly, immediate clinical value lies in molecular diagnosis, recurrence counseling, anticipatory neurologic/developmental care, and access to individualized services. Disease-modifying treatment, validated natural-history endpoints, and prospective genotype–phenotype statistics remain priority research needs.

References

1. (ma2024chemogeneticinhibitionof pages 12-13): Kaijie Ma, Kylee McDaniel, Daoqi Zhang, Maria Webb, and Luye Qin. Chemogenetic inhibition of prefrontal cortex ameliorates autism-like social deficits and absence-like seizures in a gene-trap ash1l haploinsufficiency mouse model. Genes, 15(12):1619, Dec 2024. URL: https://doi.org/10.3390/genes15121619, doi:10.3390/genes15121619. This article has 2 citations.

2. (wilson2022reprogrammingofthe pages 14-15): Khadija D. Wilson, Elizabeth G. Porter, and Benjamin A. Garcia. Reprogramming of the epigenome in neurodevelopmental disorders. Critical Reviews in Biochemistry and Molecular Biology, 57:73-112, Oct 2022. URL: https://doi.org/10.1080/10409238.2021.1979457, doi:10.1080/10409238.2021.1979457. This article has 33 citations and is from a peer-reviewed journal.

3. (jhanji2024dynamicregulationof pages 4-7): Megha Jhanji, Joseph A. Ward, Calvin S. Leung, Colleen L. Krall, Foster D. Ritchie, Alexis Guevara, Kai Vestergaard, Brian Yoon, Krishna Amin, Stefano Berto, Judy S. Liu, and Sofia B. Lizarraga. Dynamic regulation of the chromatin environment by ash1l modulates human neuronal structure and function. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.02.625500, doi:10.1101/2024.12.02.625500. This article has 0 citations.

4. (OpenTargets Search: Intellectual disability, autosomal dominant 52): Open Targets Query (Intellectual disability, autosomal dominant 52, 3 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (jhanji2024dynamicregulationof pages 1-4): Megha Jhanji, Joseph A. Ward, Calvin S. Leung, Colleen L. Krall, Foster D. Ritchie, Alexis Guevara, Kai Vestergaard, Brian Yoon, Krishna Amin, Stefano Berto, Judy S. Liu, and Sofia B. Lizarraga. Dynamic regulation of the chromatin environment by ash1l modulates human neuronal structure and function. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.02.625500, doi:10.1101/2024.12.02.625500. This article has 0 citations.

6. (jhanji2024dynamicregulationof pages 10-12): Megha Jhanji, Joseph A. Ward, Calvin S. Leung, Colleen L. Krall, Foster D. Ritchie, Alexis Guevara, Kai Vestergaard, Brian Yoon, Krishna Amin, Stefano Berto, Judy S. Liu, and Sofia B. Lizarraga. Dynamic regulation of the chromatin environment by ash1l modulates human neuronal structure and function. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.02.625500, doi:10.1101/2024.12.02.625500. This article has 0 citations.

7. (jhanji2024dynamicregulationof pages 39-41): Megha Jhanji, Joseph A. Ward, Calvin S. Leung, Colleen L. Krall, Foster D. Ritchie, Alexis Guevara, Kai Vestergaard, Brian Yoon, Krishna Amin, Stefano Berto, Judy S. Liu, and Sofia B. Lizarraga. Dynamic regulation of the chromatin environment by ash1l modulates human neuronal structure and function. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.02.625500, doi:10.1101/2024.12.02.625500. This article has 0 citations.

8. (jhanji2024dynamicregulationof pages 34-39): Megha Jhanji, Joseph A. Ward, Calvin S. Leung, Colleen L. Krall, Foster D. Ritchie, Alexis Guevara, Kai Vestergaard, Brian Yoon, Krishna Amin, Stefano Berto, Judy S. Liu, and Sofia B. Lizarraga. Dynamic regulation of the chromatin environment by ash1l modulates human neuronal structure and function. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.02.625500, doi:10.1101/2024.12.02.625500. This article has 0 citations.

9. (jhanji2024dynamicregulationof pages 26-29): Megha Jhanji, Joseph A. Ward, Calvin S. Leung, Colleen L. Krall, Foster D. Ritchie, Alexis Guevara, Kai Vestergaard, Brian Yoon, Krishna Amin, Stefano Berto, Judy S. Liu, and Sofia B. Lizarraga. Dynamic regulation of the chromatin environment by ash1l modulates human neuronal structure and function. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.02.625500, doi:10.1101/2024.12.02.625500. This article has 0 citations.

10. (jhanji2024dynamicregulationof pages 7-10): Megha Jhanji, Joseph A. Ward, Calvin S. Leung, Colleen L. Krall, Foster D. Ritchie, Alexis Guevara, Kai Vestergaard, Brian Yoon, Krishna Amin, Stefano Berto, Judy S. Liu, and Sofia B. Lizarraga. Dynamic regulation of the chromatin environment by ash1l modulates human neuronal structure and function. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.02.625500, doi:10.1101/2024.12.02.625500. This article has 0 citations.

11. (jhanji2024dynamicregulationof pages 29-34): Megha Jhanji, Joseph A. Ward, Calvin S. Leung, Colleen L. Krall, Foster D. Ritchie, Alexis Guevara, Kai Vestergaard, Brian Yoon, Krishna Amin, Stefano Berto, Judy S. Liu, and Sofia B. Lizarraga. Dynamic regulation of the chromatin environment by ash1l modulates human neuronal structure and function. bioRxiv, Dec 2024. URL: https://doi.org/10.1101/2024.12.02.625500, doi:10.1101/2024.12.02.625500. This article has 0 citations.

## Artifacts

- [Edison artifact artifact-00](Intellectual_Disability_Autosomal_Dominant_52-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 1 |
| Off topic | 0 |

All extracted references resolved successfully.