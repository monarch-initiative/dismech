---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-26T22:06:42.201539'
end_time: '2026-08-26T22:17:43.732832'
duration_seconds: 661.53
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Keratosis Pilaris Atrophicans
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 25
reference_validation:
  total_references: 9
  verified: 9
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 9
  on_topic: 3
  off_topic: 1
  off_topic_references:
  - DOI:10.66344/jpad.v13i4.765
  needs_review: true
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Keratosis_Pilaris_Atrophicans-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Keratosis Pilaris Atrophicans
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Keratosis Pilaris Atrophicans** covering all of the
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
- **Disease Name:** Keratosis Pilaris Atrophicans
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Keratosis Pilaris Atrophicans** covering all of the
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


# Keratosis Pilaris Atrophicans: Comprehensive Disease-Characteristics Report

## Executive summary and evidence limits

Keratosis pilaris atrophicans (KPA) is best treated as a **clinically defined, genetically heterogeneous spectrum**, not as one molecular disease. Its shared sequence is follicular keratin plugging and perifollicular erythema/inflammation followed by follicular destruction, atrophy, scarring, and permanent hair loss. The conventional forms are (1) keratosis pilaris atrophicans faciei (KPAF), often equated with **ulerythema ophryogenes** (UO); (2) **atrophoderma vermiculatum/vermiculata** (AV); and (3) **keratosis follicularis spinulosa decalvans** (KFSD). Boundaries overlap, and some classifications distinguish KPAF from UO more narrowly by facial distribution. (stojanovic2015overlapbetweenulerythema pages 3-5, stojanovic2015overlapbetweenulerythema pages 1-3, alessandrini2021theroleof pages 4-5)

Only X-linked KFSD has a well-supported recurrent molecular cause, **MBTPS2**. UO is strongly enriched in RAS/MAPK disorders but an isolated UO diagnosis does not imply that a RASopathy gene is causal. AV remains largely a clinicopathologic diagnosis with uncertain genetic architecture. Most therapeutic evidence consists of case reports or small uncontrolled series; no KPA-specific randomized trial was identified.

| Entity | Defining phenotype / distribution | Onset / course | Inheritance / genetic evidence | Suggested HPO terms | Key diagnostics | Evidence-supported treatment | Evidence limitations |
|---|---|---|---|---|---|---|---|
| Umbrella keratosis pilaris atrophicans (KPA) | Follicular keratotic papules with perifollicular erythema progressing to fibrosis/atrophy, scarring, and permanent hair loss; umbrella grouping that includes UO/KPA faciei, atrophoderma vermiculatum, and KFSD (stojanovic2015overlapbetweenulerythema pages 3-5, stojanovic2015overlapbetweenulerythema pages 1-3) | Usually begins in infancy or childhood; several reports note progression until puberty then relative stabilization, with permanent residual alopecia/scarring possible (stojanovic2015overlapbetweenulerythema pages 1-3, stojanovic2015overlapbetweenulerythema pages 5-7) | Disease-group term rather than a single molecular entity; genetic architecture heterogeneous. Established monogenic cause exists for KFSD via MBTPS2, but isolated KPA umbrella diagnosis does not map to one confirmed causal gene in the retrieved evidence (stojanovic2015overlapbetweenulerythema pages 5-7, bornholdt2013genotype–phenotypecorrelationsemerging pages 1-2) | Follicular hyperkeratosis; Alopecia; Eyebrow alopecia; Cicatricial alopecia; Facial erythema; Cutaneous atrophy | Primarily clinical pattern recognition plus subtype-specific histopathology when scarring alopecia or overlap is present; biopsy may show dilated keratin-plugged follicles, perifollicular inflammation, and fibrosis (stojanovic2015overlapbetweenulerythema pages 1-3, stojanovic2015overlapbetweenulerythema pages 5-7) | Symptomatic and subtype-directed: keratolytics, topical retinoids, topical corticosteroids, oral retinoids in selected inflammatory disease, and laser procedures in case reports/small series (stojanovic2015overlapbetweenulerythema pages 5-7, nimgaonkar2022ulerythemaophryogenesin pages 3-4, bari2017atrophodermavermiculataa pages 1-3) | No unified diagnostic criteria, no prevalence estimates, and no umbrella-level randomized trials identified; evidence dominated by case reports/series (stojanovic2015overlapbetweenulerythema pages 1-3, bari2017atrophodermavermiculataa pages 1-3) |
| KPA faciei / ulerythema ophryogenes (UO) | Inflammatory keratotic papules and erythema beginning in the lateral eyebrows, spreading medially; may extend to cheeks and less often forehead/scalp; leads to eyebrow alopecia/scarring (stojanovic2015overlapbetweenulerythema pages 3-5, jansen2003atrophodermiavermiculatacase pages 1-3, nimgaonkar2022ulerythemaophryogenesin pages 1-3) | Begins at birth or soon after / early infancy; often progresses through childhood and may improve after puberty, but scarring can leave permanent hair loss (stojanovic2015overlapbetweenulerythema pages 3-5, stojanovic2015overlapbetweenulerythema pages 1-3, nimgaonkar2022ulerythemaophryogenesin pages 1-3) | Familial cases reported, often described as autosomal dominant with variable penetrance; strong syndromic association with RAS/MAPK disorders (Noonan, CFC, related syndromes), but retrieved evidence supports association rather than a single established cause for isolated UO. In CFC, UO occurred in 90% (55/61) of mutation-positive individuals; MAP3K1-associated Swyer syndrome case also reported (stojanovic2015overlapbetweenulerythema pages 1-3, siegel2011dermatologicalfindingsin pages 1-3, nimgaonkar2022ulerythemaophryogenesin pages 1-3) | HP:0000204 Eyebrow sparse; keratosis pilaris; facial erythema; scarring alopecia; madarosis | Clinical diagnosis; consider evaluation for syndromic features/RASopathy if dysmorphism, cardiac disease, developmental findings, or widespread ectodermal findings are present. Histology in overlap disease shows keratin plugging, infundibular atrophy, lymphocytic perifollicular infiltrates, fibrosis (stojanovic2015overlapbetweenulerythema pages 1-3, siegel2011dermatologicalfindingsin pages 1-3) | Topical retinoids, keratolytics (urea/lactic acid/salicylic acid), low-potency topical steroids used symptomatically; limited response reported in a MAP3K1 case. For erythematous disease, a cited 595-nm pulsed-dye laser series (n=10) achieved complete resolution in 3 and >75% improvement in 7, mainly reducing erythema (nimgaonkar2022ulerythemaophryogenesin pages 3-4, nimgaonkar2022ulerythemaophryogenesin pages 1-3) | Evidence mainly case reports and small uncontrolled laser series; effect on restoring eyebrow hair appears limited once scarring is established; causation for isolated UO remains uncertain in retrieved sources (nimgaonkar2022ulerythemaophryogenesin pages 3-4, nimgaonkar2022ulerythemaophryogenesin pages 1-3) |
| Atrophoderma vermiculatum / atrophoderma vermiculata | Symmetric follicular erythematous papules of cheeks, often preauricular, evolving into pitted reticulated “worm-eaten” / “honey-combed” atrophy and scarring (stojanovic2015overlapbetweenulerythema pages 3-5, bari2017atrophodermavermiculataa pages 1-3) | Usually childhood onset; generally slow progressive worsening (bari2017atrophodermavermiculataa pages 1-3) | Considered within KPA spectrum, but isolated AV causal genetics remain uncertain in retrieved evidence. Older reports mention possible chromosomal associations (e.g., 18p deletion), but no firmly established recurrent monogenic cause was retrieved here (jansen2003atrophodermiavermiculatacase pages 1-3, bari2017atrophodermavermiculataa pages 1-3) | Cutaneous atrophy; Facial scar; Follicular hyperkeratosis; Cheek lesion | Clinical morphology plus histopathology when needed: early keratotic follicular plugging/perifollicular inflammation; later follicular and sebaceous gland atrophy with dermal fibrosis (bari2017atrophodermavermiculataa pages 1-3) | Case-report support only for topical tretinoin and 35% trichloroacetic acid chemical peeling with partial response; literature cited in review/case reports also mentions CO2 laser, 585-nm pulsed-dye laser, dermabrasion, cryotherapy, and isotretinoin for inflammatory activity (bari2017atrophodermavermiculataa pages 1-3) | No curative therapy identified; very sparse evidence base, almost entirely single-patient reports; long-term benefit of cosmetic procedures hard to judge (bari2017atrophodermavermiculataa pages 1-3) |
| Keratosis follicularis spinulosa decalvans (KFSD) | Diffuse follicular hyperkeratosis with progressive cicatricial alopecia of scalp, eyebrows, and eyelashes; may include facial erythema, keratosis pilaris on trunk/extremities, photophobia, and ocular inflammation (alessandrini2021theroleof pages 3-4, alessandrini2021theroleof pages 4-5, alessandrini2021theroleof pages 1-2) | Infancy or childhood onset; scalp alopecia typically progresses through childhood/early adolescence; some reports note progression until puberty with permanent scarring alopecia (stojanovic2015overlapbetweenulerythema pages 1-3, alessandrini2021theroleof pages 4-5, alessandrini2021theroleof pages 1-2) | Established MBTPS2-related disorder with X-linked inheritance; study of 15 affected males from 13 unrelated families identified 11 missense mutations and genotype-phenotype correlations. Variant c.1523A>G p.(Asn508Ser) caused mild KFSDX in three unrelated families (bornholdt2013genotype–phenotypecorrelationsemerging pages 1-2, bornholdt2013genotype–phenotypecorrelationsemerging pages 7-8, bornholdt2013genotype–phenotypecorrelationsemerging pages 2-3) | HP:0002556 Scarring alopecia; HP:0002209 Keratosis pilaris; HP:0000656 Eyelash alopecia; HP:0000204 Eyebrow sparse; photophobia | Diagnosis is clinical plus pathology; trichoscopy can show perifollicular hyperkeratosis, absent follicular ostia, tufted folliculitis/elongated vessels, yellow dots with dystrophic hairs. Histopathology shows decreased sebaceous glands and follicular units with diffuse fibrosis (alessandrini2021theroleof pages 3-4, alessandrini2021theroleof pages 4-5) | Best evidence is low-level but more specific than other KPA forms: keratolytics plus isotretinoin 0.3 mg/kg/day for 6 months produced complete facial resolution and scalp improvement in one report; subsequent minoxidil 5% twice daily increased hair density. Acitretin improved follicular ichthyosis/eyelash regrowth in related MBTPS2 disease but not established alopecia (alessandrini2021theroleof pages 3-4, ming2009ichthyosisfollicularisalopecia pages 1-3) | Despite established gene causation, treatment evidence remains limited to case reports/reviews; no disease-specific controlled trials identified; irreversible scarring limits hair recovery even with treatment (alessandrini2021theroleof pages 3-4, alessandrini2021theroleof pages 4-5) |


*Table: This compact table summarizes the keratosis pilaris atrophicans spectrum and separates clinically defined entities from the genetically established MBTPS2-associated KFSD subtype. It is useful for disease knowledge-base curation because it aligns phenotype, course, genetics, diagnostics, treatment evidence, and uncertainty in one place.*

## 1. Disease information

### Definition and subtypes

* **KPAF/UO:** inflammatory keratotic papules begin chiefly in the lateral eyebrows, extend medially, and may involve cheeks, temples, forehead, or rarely scalp. Progressive scarring causes lateral-eyebrow loss and sometimes complete eyebrow alopecia; eyelashes are generally spared in classical UO. (stojanovic2015overlapbetweenulerythema pages 3-5, stojanovic2015overlapbetweenulerythema pages 1-3, jansen2003atrophodermiavermiculatacase pages 1-3)
* **AV:** symmetric preauricular/cheek follicular papules evolve into reticulated, pitted “worm-eaten” or “honey-combed” atrophy. Synonyms include *atrophoderma reticulatum* and *folliculitis erythematosa reticulata*. (stojanovic2015overlapbetweenulerythema pages 3-5, bari2017atrophodermavermiculataa pages 1-3)
* **KFSD:** the most extensive form, with generalized follicular hyperkeratosis and progressive cicatricial alopecia of scalp, eyebrows, and eyelashes; facial erythema, photophobia, ocular inflammation, palmoplantar keratoderma, xerosis, atopy, nail dystrophy, or dental abnormalities may coexist. (stojanovic2015overlapbetweenulerythema pages 3-5, alessandrini2021theroleof pages 4-5, alessandrini2021theroleof pages 1-2)

### Identifiers and coding

* **OMIM:** X-linked KFSD is **MIM 308800**. (bornholdt2013genotype–phenotypecorrelationsemerging pages 2-3)
* **MONDO:** a precise umbrella-level MONDO identifier was not verified in the retrieved primary literature and should be resolved directly against the current MONDO release before ingestion. Do not substitute the code for ordinary keratosis pilaris.
* **ICD:** no dedicated ICD-10-CM or ICD-11 code was established from the retrieved sources. In practice, coding may fall under “other specified epidermal thickening/disorder of keratinization” and/or cicatricial alopecia, but jurisdiction-specific verification is required.
* **MeSH:** dedicated indexing for the umbrella disorder was not established; publications are commonly indexed through keratosis pilaris, keratinization disorders, atrophy, or cicatricial alopecia.

This report synthesizes **aggregated disease-level literature**, including family studies, case reports, reviews, and a mutation-positive syndromic cohort. It is not derived from individual EHR records.

## 2. Etiology, risk, protection, and gene–environment interaction

KPA is a congenital/developmental follicular keratinization spectrum. The proximal lesion is abnormal keratinization in and around the pilosebaceous follicle, followed by plugging, inflammation, follicular atrophy, and fibrosis. (stojanovic2015overlapbetweenulerythema pages 1-3, jansen2003atrophodermiavermiculatacase pages 1-3)

### Genetic causes and susceptibility

* **KFSD:** hemizygous germline missense variants in **MBTPS2**, an X-chromosomal gene encoding site-2 protease, are established causes of X-linked KFSD. A study of 15 affected males from 13 unrelated families found 11 missense variants, seven novel. Variant **NM_015884:c.1523A>G, p.(Asn508Ser)** caused a comparatively mild KFSD phenotype in three unrelated families. Other reported substitutions across the MBTPS2 phenotypic spectrum include p.Met87Ile, p.Phe475Ser, p.Leu476Ser, p.Asp477Val, p.Gly500Asp, and p.Asn508Ser. (bornholdt2013genotype–phenotypecorrelationsemerging pages 1-2, bornholdt2013genotype–phenotypecorrelationsemerging pages 7-8, bornholdt2013genotype–phenotypecorrelationsemerging pages 2-3, bornholdt2013genotype–phenotypecorrelationsemerging pages 3-4)
* **UO/KPAF:** familial autosomal-dominant transmission with variable penetrance has been described, but no single recurrent causal gene for isolated UO was established in the retrieved evidence. UO is a strong cutaneous marker of RAS/MAPK dysregulation: in a cohort of 61 molecularly confirmed cardio-facio-cutaneous syndrome patients with **BRAF, MAP2K1, MAP2K2, or KRAS** variants, 55/61 (90%) had UO. (stojanovic2015overlapbetweenulerythema pages 1-3, siegel2011dermatologicalfindingsin pages 1-3)
* A 17-year-old with 46,XY gonadal dysgenesis and **MAP3K1 c.1016G>A, p.Arg339Gln** also had UO. This single case establishes an association, not proof that MAP3K1 generally causes isolated UO. (nimgaonkar2022ulerythemaophryogenesin pages 1-3)
* **AV:** proposed chromosomal associations, including 18p deletion, are historical and not sufficient to define a recurrent AV locus. Its isolated genetic cause remains unresolved. (bari2017atrophodermavermiculataa pages 1-3)

No reproducible modifier genes, protective variants, founder alleles, carrier frequency, or population allele-frequency estimates were identified. Reported MBTPS2 variants should be checked individually in current ClinVar and gnomAD releases; the source studies do not supply ACMG/AMP classifications or population frequencies. The disease variants described are constitutional/germline, not somatic.

### Environmental and protective factors

No toxin, infection, radiation exposure, occupation, diet, smoking, alcohol, exercise pattern, or lifestyle behavior is established as causal. No validated genetic or environmental protective factor exists. Dryness or irritation may plausibly accentuate follicular roughness, but evidence that these alter the scarring natural history is lacking. Accordingly, a formal gene–environment interaction has not been demonstrated.

## 3. Phenotypes

### Core manifestations and suggested HPO annotations

* **Follicular hyperkeratosis/keratosis pilaris** — physical sign; onset in infancy or childhood; often widespread in KFSD. Suggested HPO: **Keratosis pilaris, HP:0002209**.
* **Perifollicular/facial erythema** — inflammatory sign; prominent in active UO and KFSD; may diminish after puberty.
* **Sparse or absent eyebrows/madarosis** — early lateral eyebrow loss in UO, broader involvement in KFSD. Suggested HPO: **Sparse eyebrow, HP:0000535** or the current HPO child term for eyebrow alopecia after release verification.
* **Cicatricial alopecia** — progressive and irreversible once follicles are replaced by fibrosis; chiefly scalp in KFSD. Suggested HPO: **Scarring alopecia, HP:0004552**, subject to current-release verification.
* **Eyelash alopecia** — supports KFSD rather than classical UO. Suggested HPO: *Sparse eyelashes/eyelash alopecia*.
* **Cutaneous facial atrophy and pitted scars** — dominant AV phenotype; slowly progressive. Suggested HPO: *Cutaneous atrophy* and *Abnormality of facial skin*.
* **Photophobia and keratoconjunctival inflammation** — variable KFSD-associated manifestations. Suggested HPO: **Photophobia, HP:0000613** and *Keratitis/Conjunctivitis*.
* **Palmoplantar keratoderma, ichthyosiform xerosis, nail dystrophy, dental abnormalities, and atopic dermatitis** — uncommon/variable KFSD-associated findings. (stojanovic2015overlapbetweenulerythema pages 3-5, alessandrini2021theroleof pages 1-2)

UO commonly begins at birth or soon afterward; KFSD begins in infancy or childhood, with scalp disease becoming conspicuous in childhood or early adolescence; AV generally begins in childhood. Severity is variable. UO and KFSD often progress until puberty and then stabilize or become less inflammatory, but alopecia and atrophy remain. (stojanovic2015overlapbetweenulerythema pages 1-3, alessandrini2021theroleof pages 4-5, nimgaonkar2022ulerythemaophryogenesin pages 1-3, bari2017atrophodermavermiculataa pages 1-3)

Reliable frequencies for isolated KPA manifestations are unavailable. The strongest quantitative datum is syndromic: UO in 90% (55/61) of mutation-positive CFC patients, which must not be generalized to isolated KPA. (siegel2011dermatologicalfindingsin pages 1-3)

### Quality of life

No validated KPA-specific EQ-5D, SF-36, PROMIS, or dermatology-quality-of-life cohort was identified. The principal expected burden is visible facial/scalp scarring, eyebrow/eyelash loss, cosmetic disfigurement, and—in KFSD with ocular disease—photophobia. AV has explicitly been described as a rare “disfiguring” condition, but this is descriptive rather than instrument-based evidence. (bari2017atrophodermavermiculataa pages 1-3)

## 4. Genetic and molecular information

### MBTPS2 and pathogenic mechanism

**MBTPS2** encodes an endoplasmic-reticulum/Golgi membrane zinc metalloprotease, site-2 protease (S2P), required for regulated intramembrane proteolysis. After site-1 cleavage, S2P releases membrane-bound transcription factors controlling sterol homeostasis, lipid metabolism, ER-stress responses, and differentiation, including SREBP, ATF6, and OASIS-family proteins. (bornholdt2013genotype–phenotypecorrelationsemerging pages 1-2, lim2021omicsprofilingof pages 2-4)

Pathogenic substitutions cluster in transmembrane domains. Changes near the catalytic site reduce activity most severely; residual activity correlates with phenotype. N- or C-terminal variants retaining more activity tend to produce milder disease, whereas transmembrane-domain 6–8 hotspots can eliminate approximately two-thirds of catalytic activity and cause severe developmental/ichthyotic phenotypes. p.Asn508Ser is associated with mild KFSD and progressive alopecia. Female expression is influenced by X-chromosome inactivation. (bornholdt2013genotype–phenotypecorrelationsemerging pages 7-8)

No dominant-negative mechanism is established; the evidence supports **partial loss of catalytic function/hypomorphic dysfunction**. Whole-gene deletions, recurrent splice variants, repeat expansions, mitochondrial variants, and disease-specific epigenetic abnormalities were not established.

## 5. Environmental information

KPA is not infectious or transmissible, and no microbial trigger is recognized. There is no evidence for pollution, toxins, ultraviolet exposure, occupational exposure, diet, smoking, alcohol, or exercise as causal factors. Standard skin care may reduce roughness and irritation but is supportive rather than disease-preventing. CTD-style chemical associations, validated gene–environment effects, and exposure-response data are absent.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream inherited defect:** an MBTPS2 missense variant in X-linked KFSD reduces S2P activity; in syndromic UO, upstream germline RAS/MAPK activation is associated with abnormal ectodermal development, although the direct follicular chain is unresolved. (bornholdt2013genotype–phenotypecorrelationsemerging pages 1-2, siegel2011dermatologicalfindingsin pages 1-3)
2. **Molecular dysfunction:** defective regulated intramembrane proteolysis impairs activation of SREBP/ATF6/OASIS-related transcriptional programs, disturbing lipid/sterol homeostasis, ER-stress adaptation, and epidermal differentiation. Patient fibroblasts carrying p.Arg429His or p.Asn508Ser showed impaired OASIS cleavage and diminished induced ATF6/SREBP activities. (lim2021omicsprofilingof pages 2-4)
3. **Cellular/tissue lesion:** abnormal follicular keratinization plugs the infundibulum, producing dilated keratin-filled follicles and perifollicular lymphocytic inflammation. (stojanovic2015overlapbetweenulerythema pages 1-3)
4. **Downstream irreversible damage:** chronic folliculocentric inflammation causes infundibular atrophy, sebaceous-gland and follicular-unit loss, and perifollicular/diffuse dermal fibrosis. (stojanovic2015overlapbetweenulerythema pages 5-7, alessandrini2021theroleof pages 4-5, bari2017atrophodermavermiculataa pages 1-3)
5. **Clinical manifestation:** rough keratotic papules and erythema evolve into eyebrow/eyelash/scalp alopecia or reticulated facial atrophy, depending on anatomical distribution and disease subtype.

### Suggested annotations

* **GO biological process:** regulated intramembrane proteolysis; cholesterol homeostasis; lipid metabolic process; response to endoplasmic-reticulum stress; epidermal-cell differentiation; keratinization; inflammatory response; wound healing/fibrosis.
* **GO molecular function:** metalloendopeptidase activity; zinc-ion binding.
* **GO cellular component:** endoplasmic-reticulum membrane; Golgi membrane; integral component of membrane.
* **Cell Ontology:** **keratinocyte**, hair-follicle keratinocyte, dermal fibroblast, sebocyte, and perifollicular lymphocyte. Exact CL identifiers should be release-verified.

### Molecular profiling and advanced technologies

The principal profiling study used primary skin fibroblasts from four controls, three MBTPS2-osteogenesis-imperfecta patients, and two MBTPS2-IFAP/KFSD patients, with RNA sequencing, lipid analysis, electron microscopy, and immunofluorescence. The dermatologic group included p.Arg429His and p.Asn508Ser. This establishes pathway-level dysfunction but is underpowered for a KFSD-specific molecular signature. No KPA-specific single-cell atlas, spatial transcriptomic dataset, proteomic signature, metabolomic biomarker, organoid, or CRISPR screen was identified. (lim2021omicsprofilingof pages 2-4)

## 7. Anatomical structures affected

The primary organ is **skin**, specifically the pilosebaceous unit and hair follicles.

* **UO:** bilateral lateral eyebrows, then medial eyebrows, cheeks, temples, and occasionally forehead/scalp.
* **AV:** bilateral preauricular and malar cheek skin.
* **KFSD:** scalp, eyebrows, eyelashes, face, and variably trunk/extensor limbs; cornea and conjunctiva may be secondarily involved.
* **Tissue/cell level:** follicular epithelium/infundibulum, sebaceous glands, perifollicular dermis, keratinocytes, sebocytes, fibroblasts, and inflammatory lymphocytes.
* **Subcellular level:** ER and Golgi membranes are central to MBTPS2/S2P biology.

Suggested UBERON labels are skin of face, cheek, eyebrow, eyelid/eyelash region, scalp, hair follicle, sebaceous gland, cornea, and conjunctiva. Disease is generally bilateral and symmetric in UO/AV; focal or patchy scalp alopecia can occur in KFSD. (stojanovic2015overlapbetweenulerythema pages 3-5, stojanovic2015overlapbetweenulerythema pages 1-3)

## 8. Temporal development

Onset is congenital, neonatal, or early pediatric rather than adult-acquired. The onset is insidious and chronic. Active stages feature follicular papules and erythema; intermediate disease adds follicular atrophy and hair loss; advanced disease contains established fibrosis, absent follicular ostia, and irreversible scarring. UO/KFSD often progress until puberty and subsequently stabilize, while AV usually worsens slowly. Inflammation can remit spontaneously or with treatment, but destroyed follicles do not regenerate. (stojanovic2015overlapbetweenulerythema pages 1-3, stojanovic2015overlapbetweenulerythema pages 5-7, nimgaonkar2022ulerythemaophryogenesin pages 1-3, bari2017atrophodermavermiculataa pages 1-3)

The critical therapeutic window is therefore the **active inflammatory stage before fibrosis**, although this inference has not been tested prospectively.

## 9. Inheritance and population

* **KFSD:** usually X-linked, often described as X-linked dominant or X-linked with sex-modified expression. Hemizygous males are typically more severely affected; heterozygous females can be asymptomatic or mildly affected because of lyonization. Autosomal-dominant and sporadic KFSD-like cases have also been reported. (alessandrini2021theroleof pages 3-4, alessandrini2021theroleof pages 1-2, bornholdt2013genotype–phenotypecorrelationsemerging pages 1-2)
* **UO:** sporadic and autosomal-dominant families with variable penetrance occur. Syndromic UO follows the inheritance of the causal syndrome, commonly autosomal-dominant/de novo RASopathy inheritance. (stojanovic2015overlapbetweenulerythema pages 1-3, siegel2011dermatologicalfindingsin pages 1-3)
* **AV:** familial cases support a genodermatosis, but the mode and locus remain uncertain.

No robust prevalence, incidence, geographic distribution, ethnicity effect, carrier frequency, founder effect, anticipation, germline-mosaicism rate, or consanguinity association was found. “Rare” or “exceedingly rare” is currently more defensible than a cases-per-100,000 estimate. There is no established sex imbalance for the umbrella spectrum; male predominance/severity applies chiefly to X-linked KFSD.

## 10. Diagnostics

### Clinical assessment

Diagnosis starts with age of onset, distribution, inflammatory activity, scarring, family history, and associated ocular or syndromic findings. There are no validated standardized criteria or circulating biomarkers. Routine blood/urine tests and radiologic imaging are not diagnostic.

**Trichoscopy in KFSD** can show diffuse perifollicular hyperkeratosis, absent follicular ostia, tufting, elongated vessels, yellow dots, and dystrophic eyebrow/eyelash hairs. Evidence is very limited—the 2021 report described itself as the first trichoscopic evaluation. (alessandrini2021theroleof pages 3-4, alessandrini2021theroleof pages 4-5)

**Histopathology:** early lesions show dilated keratin-filled follicles and perifollicular lymphocytes. Progressive lesions show infundibular atrophy, reduced sebaceous glands and follicular units, and perifollicular or diffuse fibrosis. AV similarly progresses from follicular plugging/inflammation to pilosebaceous atrophy and dermal fibrosis. (stojanovic2015overlapbetweenulerythema pages 1-3, alessandrini2021theroleof pages 4-5, bari2017atrophodermavermiculataa pages 1-3)

### Genetic testing

* In a male with KFSD, test **MBTPS2** by sequencing with deletion/duplication analysis. A genodermatosis/cicatricial-alopecia panel or WES is appropriate for atypical/negative cases because phenocopies and overlapping MBTPS2 disorders exist.
* In UO with congenital heart disease, short stature, dysmorphism, developmental disability, lymphatic disease, or widespread ectodermal findings, use a **RASopathy panel** including BRAF, KRAS, MAP2K1, MAP2K2, SOS1, SOS2, and other current genes. UO alone is insufficient evidence for such a molecular diagnosis. The 90% frequency in CFC makes it a useful syndromic clue. (siegel2011dermatologicalfindingsin pages 1-3)
* CMA is reasonable when developmental anomalies suggest a copy-number disorder. Karyotype/FISH, mitochondrial sequencing, and repeat-expansion testing are not routine KPA tests. WGS may be considered after nondiagnostic panel/WES but has no established incremental KPA yield.
* Confirm the variant with an accredited laboratory, perform segregation analysis where possible, and interpret under ACMG/AMP standards.

### Differential diagnosis

Differentials include ordinary nonatrophic keratosis pilaris; keratosis pilaris rubra; folliculitis decalvans; lichen planopilaris; frontal fibrosing alopecia; IFAP syndrome; keratitis–ichthyosis–deafness syndrome; atrichia with papular lesions; hereditary mucoepithelial dystrophy; acne or varicella scars; focal dermal hypoplasia; and other varioliform atrophodermas. Loss of follicular ostia and fibrosis distinguish cicatricial disease; eyelash/scalp scarring favors KFSD, whereas lateral eyebrow-predominant disease favors UO and reticulated cheek pits favor AV. (alessandrini2021theroleof pages 4-5)

No population, newborn, or carrier-screening program exists. Cascade testing is appropriate only after a familial pathogenic variant is established.

## 11. Outcome and prognosis

KPA is not known to reduce survival or life expectancy; disease-specific mortality has not been reported. Morbidity is dermatologic and cosmetic, with photophobia/ocular inflammation adding functional burden in KFSD. The active inflammatory component may improve after puberty or treatment, but established alopecia and pitted atrophy are generally permanent. (stojanovic2015overlapbetweenulerythema pages 5-7, nimgaonkar2022ulerythemaophryogenesin pages 1-3)

Poorer outcome is expected with extensive scalp involvement, eyelash loss, prolonged inflammation, or delayed control before fibrosis. These are clinically plausible prognostic features, not validated predictors. No prognostic molecular biomarker or survival model exists.

## 12. Treatment

There is no curative or regulatory-approved disease-modifying therapy. Management aims to reduce plugging and inflammation before scarring, treat ocular disease, and improve appearance.

### Practical strategy

1. **Baseline care:** gentle cleanser, regular emollient, and avoidance of abrasive manipulation.
2. **Follicular plugging:** topical urea, lactic/glycolic acid, salicylic acid, or topical retinoid. Suggested CHEBI concepts include urea, lactic acid, salicylic acid, and tretinoin; NCIT intervention concepts: topical therapy, keratolytic therapy.
3. **Active inflammation:** brief low-potency topical corticosteroid on facial disease; tetracycline-class anti-inflammatory therapy has been reported but lacks controlled evidence. A UO case used adapalene plus desonide and hydroxy-acid emollient without significant change at three months, complicated by poor adherence. (nimgaonkar2022ulerythemaophryogenesin pages 3-4, nimgaonkar2022ulerythemaophryogenesin pages 1-3)
4. **Progressive KFSD/AV:** consider a systemic retinoid under specialist monitoring. In one KFSD case, **isotretinoin 0.3 mg/kg/day for six months** plus keratolytic cream produced complete facial resolution and scalp improvement; subsequent **5% minoxidil twice daily** increased hair density. No adverse effects were reported, but this is one patient. (alessandrini2021theroleof pages 3-4)
5. **Vascular erythema:** 595-nm pulsed-dye laser has the best small-series signal: among ten UO patients, three achieved complete resolution and seven had >75% improvement, primarily in erythema. This does not establish reversal of scarring or hair regrowth. (nimgaonkar2022ulerythemaophryogenesin pages 3-4)
6. **Established texture/atrophy:** AV case literature describes partial response to 35% trichloroacetic-acid peels plus 0.05% tretinoin and reports use of CO2 or 585-nm PDL, dermabrasion, cryotherapy, and isotretinoin for active inflammation. Long-term efficacy is unknown. (bari2017atrophodermavermiculataa pages 1-3)
7. **Residual alopecia:** camouflage, cosmetic eyebrow techniques, minoxidil where viable follicles remain, and selected hair transplantation only after prolonged disease inactivity. Ophthalmology should manage photophobia, keratitis, or conjunctivitis.

Potential adverse effects include irritant dermatitis from acids/retinoids, steroid atrophy, retinoid teratogenicity and mucocutaneous/laboratory toxicity, minoxidil irritation/hypertrichosis, and laser-associated pain, pigment alteration, or scarring. No KPA pharmacogenomic guidance exists. There is no gene, cell, RNA, CRISPR, targeted kinase, or immunotherapy in clinical use.

ClinicalTrials.gov searching retrieved studies for **ordinary keratosis pilaris**—including diode/Nd:YAG/thulium laser, emollient, and cosmetic interventions—but none was established as enrolling KPA/UO/AV/KFSD specifically. These should not be represented as disease-specific KPA trials.

## 13. Prevention

Primary prevention is unavailable because the disease is inherited/developmental; vaccines, prophylactic drugs, and public-health/environmental interventions are not applicable. Secondary/tertiary prevention consists of early recognition, minimizing follicular inflammation before fibrosis, ophthalmologic surveillance when indicated, and screening syndromic UO patients for associated RASopathy manifestations. A report specifically advocated improved UO recognition in RASopathy patients to permit intervention before permanent scarring. (nimgaonkar2022ulerythemaophryogenesin pages 3-4)

For molecularly confirmed families, genetic counseling should cover subtype-specific inheritance, variable expression, recurrence risk, cascade testing, and reproductive options, including prenatal or preimplantation testing when desired. Females carrying an MBTPS2 variant may be mildly affected or nonpenetrant. (bornholdt2013genotype–phenotypecorrelationsemerging pages 1-2)

## 14. Other species and natural disease

No verified naturally occurring KPA, UO, AV, or KFSD orthologous syndrome was identified in companion animals, livestock, or wildlife. Consequently, no breed/VBO annotation, veterinary prevalence, zoonotic potential, or cross-species transmission applies. MBTPS2 is evolutionarily conserved, but conservation alone is not evidence of a natural veterinary counterpart.

## 15. Model organisms and experimental models

No validated mouse, rat, zebrafish, Drosophila, or other organismal model was found that demonstrably reproduces the human combination of follicular keratosis and progressive cicatricial alopecia. The most directly relevant experimental systems are patient-derived dermal fibroblasts carrying MBTPS2 variants. These support defective S2P-dependent transcription-factor activation and permit transcriptomic/lipid/ER-stress assays, but fibroblasts do not reproduce hair-follicle architecture, keratin plugging, immune–epithelial interactions, or scarring alopecia. (lim2021omicsprofilingof pages 2-4)

Future models should use variant-specific knock-in animals, human hair-follicle organoids, or isogenic iPSC-derived keratinocyte–sebocyte–fibroblast systems. Applications would include mapping SREBP/ATF6/OASIS defects to follicular differentiation, defining inflammatory-to-fibrotic transitions, and testing whether early pathway correction prevents permanent follicular loss.

## Recent developments and authoritative interpretation

The 2023–2024 literature did not materially change KPA-specific molecular diagnosis or treatment. The most informative contemporary evidence remains: patient-fibroblast molecular profiling (2021), trichoscopy plus a dose-specific KFSD treatment report (2021), and the MAP3K1-associated UO case with a summary of laser evidence (2022). The major current interpretation is therefore conservative: **MBTPS2 testing is justified for KFSD; UO should trigger assessment for a RASopathy when systemic clues are present; and early anti-keratinizing/anti-inflammatory therapy is rational but unproven to prevent scarring.** (lim2021omicsprofilingof pages 2-4, siegel2011dermatologicalfindingsin pages 1-3, alessandrini2021theroleof pages 3-4, nimgaonkar2022ulerythemaophryogenesin pages 3-4)

## Selected exact source language

* Stojanović et al. describe KPA lesions as follicular keratotic papules that “eventually result in fibrosis, atrophy, progressive scarring and permanent hair loss.” Publication: September 2015; https://doi.org/10.1515/sjdv-2015-0012. (stojanovic2015overlapbetweenulerythema pages 3-5, stojanovic2015overlapbetweenulerythema pages 1-3)
* The 2021 KFSD report defines the disorder as a rare hereditary keratinization disease with “progressive scarring alopecia of scalp, eyebrows, and eyelashes.” Publication: October 2021; https://doi.org/10.1159/000510525. (alessandrini2021theroleof pages 1-2)
* The AV abstract describes a “rare genodermatosis with usual onset in childhood” and “honey-combed” cheek atrophy, with a “generally slow” progressive course. Publication: January 2017; https://doi.org/10.66344/jpad.v13i4.765. (bari2017atrophodermavermiculataa pages 1-3)

PMIDs were not consistently exposed in the retrieved records; DOI URLs and publication dates are therefore supplied rather than inventing unverified PMID values. Before production ingestion, identifiers—including MONDO, HPO IDs, HGNC ID for MBTPS2, current ClinVar assertions, and ICD mappings—should be programmatically validated against their current releases.

References

1. (stojanovic2015overlapbetweenulerythema pages 3-5): Slobodan Stojanović, Nada Vučković, and Marina Jovanović. Overlap between ulerythema ophryogenes and keratosis follicularis spinulosa decalvans: a case report. Serbian Journal of Dermatology and Venereology, 7:129-138, Sep 2015. URL: https://doi.org/10.1515/sjdv-2015-0012, doi:10.1515/sjdv-2015-0012. This article has 1 citations.

2. (stojanovic2015overlapbetweenulerythema pages 1-3): Slobodan Stojanović, Nada Vučković, and Marina Jovanović. Overlap between ulerythema ophryogenes and keratosis follicularis spinulosa decalvans: a case report. Serbian Journal of Dermatology and Venereology, 7:129-138, Sep 2015. URL: https://doi.org/10.1515/sjdv-2015-0012, doi:10.1515/sjdv-2015-0012. This article has 1 citations.

3. (alessandrini2021theroleof pages 4-5): Aurora Alessandrini, Giancarlo Brattoli, Bianca Maria Piraccini, Ambra Di Altobrando, and Michela Starace. The role of trichoscopy in keratosis follicularis spinulosa decalvans: case report and review of the literature. Skin Appendage Disorders, 7:29-35, Oct 2021. URL: https://doi.org/10.1159/000510525, doi:10.1159/000510525. This article has 11 citations and is from a peer-reviewed journal.

4. (stojanovic2015overlapbetweenulerythema pages 5-7): Slobodan Stojanović, Nada Vučković, and Marina Jovanović. Overlap between ulerythema ophryogenes and keratosis follicularis spinulosa decalvans: a case report. Serbian Journal of Dermatology and Venereology, 7:129-138, Sep 2015. URL: https://doi.org/10.1515/sjdv-2015-0012, doi:10.1515/sjdv-2015-0012. This article has 1 citations.

5. (bornholdt2013genotype–phenotypecorrelationsemerging pages 1-2): Dorothea Bornholdt, T. Prescott Atkinson, Bakar Bouadjar, Benoit Catteau, Helen Cox, Deepthi De Silva, Judith Fischer, Chalukya N. Gunasekera, Smaïl Hadj-Rabia, Rudolf Happle, Muriel Holder-Espinasse, Elke Kaminski, Arne König, André Mégarbané, Hala Mégarbané, Ulrike Neidel, Frank Oeffner, Vinzenz Oji, Amy Theos, Heiko Traupe, Anders Vahlquist, Bregje W. van Bon, Marie Virtanen, and Karl-Heinz Grzeschik. Genotype–phenotype correlations emerging from the identification of missense mutations in mbtps2. Human Mutation, 34:n/a-n/a, Apr 2013. URL: https://doi.org/10.1002/humu.22275, doi:10.1002/humu.22275. This article has 48 citations and is from a domain leading peer-reviewed journal.

6. (nimgaonkar2022ulerythemaophryogenesin pages 3-4): Ila Nimgaonkar, Marielle Jamgochian, David M. Milgraum, Amy S. Pappert, and Sandy S. Milgraum. Ulerythema ophryogenes in association with map3k1-mutated swyer syndrome. Jul 2022. URL: https://doi.org/10.1016/j.jdcr.2022.05.008, doi:10.1016/j.jdcr.2022.05.008. This article has 2 citations.

7. (bari2017atrophodermavermiculataa pages 1-3): Arfan ul Bari. Atrophoderma vermiculata: a rare disfiguring condition. Journal of Pakistan Association of Dermatologists, 13(4):208-210, Jan 2017. URL: https://doi.org/10.66344/jpad.v13i4.765, doi:10.66344/jpad.v13i4.765. This article has 1 citations.

8. (jansen2003atrophodermiavermiculatacase pages 1-3): T. Jansen, C. Sander, and P. Altmeyer. Atrophodermia vermiculata: case report and review of the literature. Journal of the European Academy of Dermatology and Venereology, 17:70-72, Jan 2003. URL: https://doi.org/10.1046/j.1468-3083.2003.00517.x, doi:10.1046/j.1468-3083.2003.00517.x. This article has 15 citations and is from a domain leading peer-reviewed journal.

9. (nimgaonkar2022ulerythemaophryogenesin pages 1-3): Ila Nimgaonkar, Marielle Jamgochian, David M. Milgraum, Amy S. Pappert, and Sandy S. Milgraum. Ulerythema ophryogenes in association with map3k1-mutated swyer syndrome. Jul 2022. URL: https://doi.org/10.1016/j.jdcr.2022.05.008, doi:10.1016/j.jdcr.2022.05.008. This article has 2 citations.

10. (siegel2011dermatologicalfindingsin pages 1-3): D.H. Siegel, J. McKenzie, I.J. Frieden, and K.A. Rauen. Dermatological findings in 61 mutation‐positive individuals with cardiofaciocutaneous syndrome. British Journal of Dermatology, 164:no-no, Jan 2011. URL: https://doi.org/10.1111/j.1365-2133.2010.10122.x, doi:10.1111/j.1365-2133.2010.10122.x. This article has 123 citations and is from a highest quality peer-reviewed journal.

11. (alessandrini2021theroleof pages 3-4): Aurora Alessandrini, Giancarlo Brattoli, Bianca Maria Piraccini, Ambra Di Altobrando, and Michela Starace. The role of trichoscopy in keratosis follicularis spinulosa decalvans: case report and review of the literature. Skin Appendage Disorders, 7:29-35, Oct 2021. URL: https://doi.org/10.1159/000510525, doi:10.1159/000510525. This article has 11 citations and is from a peer-reviewed journal.

12. (alessandrini2021theroleof pages 1-2): Aurora Alessandrini, Giancarlo Brattoli, Bianca Maria Piraccini, Ambra Di Altobrando, and Michela Starace. The role of trichoscopy in keratosis follicularis spinulosa decalvans: case report and review of the literature. Skin Appendage Disorders, 7:29-35, Oct 2021. URL: https://doi.org/10.1159/000510525, doi:10.1159/000510525. This article has 11 citations and is from a peer-reviewed journal.

13. (bornholdt2013genotype–phenotypecorrelationsemerging pages 7-8): Dorothea Bornholdt, T. Prescott Atkinson, Bakar Bouadjar, Benoit Catteau, Helen Cox, Deepthi De Silva, Judith Fischer, Chalukya N. Gunasekera, Smaïl Hadj-Rabia, Rudolf Happle, Muriel Holder-Espinasse, Elke Kaminski, Arne König, André Mégarbané, Hala Mégarbané, Ulrike Neidel, Frank Oeffner, Vinzenz Oji, Amy Theos, Heiko Traupe, Anders Vahlquist, Bregje W. van Bon, Marie Virtanen, and Karl-Heinz Grzeschik. Genotype–phenotype correlations emerging from the identification of missense mutations in mbtps2. Human Mutation, 34:n/a-n/a, Apr 2013. URL: https://doi.org/10.1002/humu.22275, doi:10.1002/humu.22275. This article has 48 citations and is from a domain leading peer-reviewed journal.

14. (bornholdt2013genotype–phenotypecorrelationsemerging pages 2-3): Dorothea Bornholdt, T. Prescott Atkinson, Bakar Bouadjar, Benoit Catteau, Helen Cox, Deepthi De Silva, Judith Fischer, Chalukya N. Gunasekera, Smaïl Hadj-Rabia, Rudolf Happle, Muriel Holder-Espinasse, Elke Kaminski, Arne König, André Mégarbané, Hala Mégarbané, Ulrike Neidel, Frank Oeffner, Vinzenz Oji, Amy Theos, Heiko Traupe, Anders Vahlquist, Bregje W. van Bon, Marie Virtanen, and Karl-Heinz Grzeschik. Genotype–phenotype correlations emerging from the identification of missense mutations in mbtps2. Human Mutation, 34:n/a-n/a, Apr 2013. URL: https://doi.org/10.1002/humu.22275, doi:10.1002/humu.22275. This article has 48 citations and is from a domain leading peer-reviewed journal.

15. (ming2009ichthyosisfollicularisalopecia pages 1-3): Andrew Ming, Rudolf Happle, Karl‐Heinz Grzeschik, and Gayle Fischer. Ichthyosis follicularis, alopecia, and photophobia (ifap) syndrome due to mutation of the gene mbtps2 in a large australian kindred. Pediatric Dermatology, 26:427-431, Jul 2009. URL: https://doi.org/10.1111/j.1525-1470.2009.00946.x, doi:10.1111/j.1525-1470.2009.00946.x. This article has 22 citations and is from a peer-reviewed journal.

16. (bornholdt2013genotype–phenotypecorrelationsemerging pages 3-4): Dorothea Bornholdt, T. Prescott Atkinson, Bakar Bouadjar, Benoit Catteau, Helen Cox, Deepthi De Silva, Judith Fischer, Chalukya N. Gunasekera, Smaïl Hadj-Rabia, Rudolf Happle, Muriel Holder-Espinasse, Elke Kaminski, Arne König, André Mégarbané, Hala Mégarbané, Ulrike Neidel, Frank Oeffner, Vinzenz Oji, Amy Theos, Heiko Traupe, Anders Vahlquist, Bregje W. van Bon, Marie Virtanen, and Karl-Heinz Grzeschik. Genotype–phenotype correlations emerging from the identification of missense mutations in mbtps2. Human Mutation, 34:n/a-n/a, Apr 2013. URL: https://doi.org/10.1002/humu.22275, doi:10.1002/humu.22275. This article has 48 citations and is from a domain leading peer-reviewed journal.

17. (lim2021omicsprofilingof pages 2-4): Pei Jin Lim, Severin Marfurt, Uschi Lindert, Lennart Opitz, Timothée Ndarugendamwo, Pakeerathan Srikanthan, Martin Poms, Martin Hersberger, Claus-Dieter Langhans, Dorothea Haas, Marianne Rohrbach, and Cecilia Giunta. Omics profiling of s2p mutant fibroblasts as a mean to unravel the pathomechanism and molecular signatures of x-linked mbtps2 osteogenesis imperfecta. Frontiers in Genetics, May 2021. URL: https://doi.org/10.3389/fgene.2021.662751, doi:10.3389/fgene.2021.662751. This article has 7 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Keratosis_Pilaris_Atrophicans-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 9 |
| Resolved | 9 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 9 |
| On topic | 3 |
| Off topic | 1 |

### References that may not be about this subject

These identifiers resolve, so they are not fabrications, but the records they resolve to share almost none of this report's vocabulary. That is a clue and not a verdict - a paper can be relevant in ways its title and abstract do not spell out - so read them before deciding:

- `DOI:10.66344/jpad.v13i4.765` (5 mentions) - Atrophoderma vermiculata: A rare disfiguring condition
  - shared terms: atrophy

Weighed against this report's own most characteristic terms: `disease`, `kfsd`, `gene`, `clinical`, `follicular`, `genetic`, `scarring`, `variant`, `alopecia`, `molecular`, `loss`, `inflammation`, `fibrosis`, `atrophy`, `mbtps2`, `established`, `keratosis`, `treatment`, `scalp`, `eyelash`.

All extracted references resolved successfully.
Resolving is not the same as being relevant, though - see the references listed above as possibly off topic.