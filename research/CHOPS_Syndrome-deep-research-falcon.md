---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-19T09:06:16.887711'
end_time: '2026-08-19T09:16:41.477218'
duration_seconds: 624.59
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: CHOPS Syndrome
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 30
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 2
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: CHOPS_Syndrome-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** CHOPS Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **CHOPS Syndrome** covering all of the
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
- **Disease Name:** CHOPS Syndrome
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **CHOPS Syndrome** covering all of the
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


# CHOPS Syndrome: Comprehensive Disease-Characteristics Report

**Evidence cutoff:** literature and database searches emphasized 2023–2024 research, while retaining the foundational 2015 disease-discovery study. CHOPS syndrome is exceptionally rare: most disease-specific conclusions still rest on three deeply characterized index patients. Accordingly, fractions such as 3/3 describe that discovery cohort and must not be interpreted as population prevalence.

## Executive summary

CHOPS syndrome is a congenital, multisystem disorder of developmental transcription caused by heterozygous gain-of-function missense variants in the degron region of **AFF4**, a scaffold of the super elongation complex (SEC). The defining phenotype comprises **c**ognitive impairment and **c**oarse facies, **h**eart defects, **o**besity, **p**ulmonary involvement, and **s**hort stature with skeletal dysplasia. The three original variants—**NM_014423.4:c.760A>G (p.Thr254Ala), c.761C>G (p.Thr254Ser), and c.772C>T (p.Arg258Trp)**—were de novo in three unrelated individuals. Mutant AFF4 resists SIAH1-mediated proteasomal degradation, accumulates on chromatin, and dysregulates SEC-dependent RNA-polymerase-II (Pol II) pause release and transcriptional elongation. Altered AFF4, cohesin, and Pol II occupancy provides a mechanistic explanation for overlap with Cornelia de Lange syndrome (CdLS). (izumi2015germlinegainoffunctionmutations pages 3-4, izumi2015germlinegainoffunctionmutations pages 4-6, izumi2015germlinegainoffunctionmutations pages 8-10)

No CHOPS-specific natural-history cohort, prevalence estimate, formal diagnostic criteria, disease-modifying treatment, or interventional trial was identified. Diagnosis is molecular, generally through exome/genome sequencing or targeted **AFF4** analysis, and care is supportive and organ-directed.

The following structured summary is suitable for knowledge-base ingestion.

| Domain | Established finding | Evidence/quantity | Suggested ontology |
|---|---|---|---|
| Disease name/definition | CHOPS syndrome is a multisystem developmental disorder named for cognitive impairment/coarse facies, heart defects, obesity, pulmonary involvement, short stature, and skeletal dysplasia | Initially delineated in 3 unrelated probands; phenotype overlaps Cornelia de Lange syndrome spectrum but is molecularly distinct via AFF4 gain-of-function (izumi2015germlinegainoffunctionmutations pages 3-4, izumi2015germlinegainoffunctionmutations pages 1-3) | OMIM:616368; EFO:0009031; MONDO: unavailable/unverified |
| Synonyms | Cognitive impairment–coarse facies–heart defects–obesity–pulmonary involvement–short stature–skeletal dysplasia syndrome; CHOPS syndrome | Acronym-based syndrome name used in primary literature and disease-target resources (izumi2015germlinegainoffunctionmutations pages 3-4, OpenTargets Search: CHOPS syndrome-AFF4) | Exact synonym mapping to disease record |
| Evidence source type | Knowledge is derived primarily from aggregated disease-level literature plus deep molecular analysis of patient-derived fibroblasts; not from large registry or trial datasets | 3 published probands in landmark study; fibroblast transcriptomics/ChIP-seq/cell-line functional assays (izumi2015germlinegainoffunctionmutations pages 3-4, izumi2015germlinegainoffunctionmutations pages 4-6, izumi2015germlinegainoffunctionmutations pages 10-11, izumi2015germlinegainoffunctionmutations pages 11-13) | ECO: human clinical evidence; in vitro functional evidence |
| Causal gene | AFF4 (ALF transcription elongation factor 4), core scaffold component of the super elongation complex (SEC) | Single established causal gene for classic CHOPS syndrome in available evidence (izumi2015germlinegainoffunctionmutations pages 3-4, izumi2015germlinegainoffunctionmutations pages 1-3) | HGNC: AFF4; NCBI Gene/Ensembl gene record |
| Pathogenic variants | Recurrent de novo missense variants in the degron/ALF homology region: c.760A>G (p.Thr254Ala), c.761C>G (p.Thr254Ser), c.772C>T (p.Arg258Trp) | 3/3 probands had heterozygous de novo missense variants; all affected highly conserved residues (izumi2015germlinegainoffunctionmutations pages 3-4) | Sequence Ontology: missense_variant |
| Inheritance | Autosomal dominant disorder usually arising de novo | Variants absent in all 6 biological parents in the discovery cohort; no inherited multigeneration pedigree established (izumi2015germlinegainoffunctionmutations pages 3-4, izumi2015germlinegainoffunctionmutations pages 15-18) | HP:0000006 Autosomal dominant inheritance; HP:0025352 De novo mutation |
| Molecular class/mechanism | Gain-of-function caused by impaired SIAH1-mediated ubiquitin/proteasome degradation of AFF4 | Mutant AFF4 resists degradation and behaves opposite to AFF4 knockdown/LoF models (izumi2015germlinegainoffunctionmutations pages 4-6, izumi2015germlinegainoffunctionmutations pages 6-8, izumi2015germlinegainoffunctionmutations pages 3-4) | GO: positive regulation of transcription by RNA polymerase II; GO: protein ubiquitination |
| Causal chain | Degron-region AFF4 missense mutation → reduced SIAH1 binding/degradation → chromatin-associated AFF4 accumulation → altered SEC activity and RNAP2 pause-release/elongation → altered cohesin/RNAP2 genome-wide binding → developmental transcriptional dysregulation → multisystem phenotype | Supported by patient fibroblasts, overexpression systems, transcriptomics, and ChIP-seq (izumi2015germlinegainoffunctionmutations pages 4-6, izumi2015germlinegainoffunctionmutations pages 8-10, izumi2015germlinegainoffunctionmutations pages 6-8, izumi2016disordersoftranscriptional pages 9-10, tei2024cohesinregulatespromoterproximal pages 1-3) | GO: protein stabilization; GO: chromatin binding; GO: transcription elongation by RNA polymerase II |
| Core phenotype: cognitive/developmental | Cognitive impairment/intellectual disability/developmental delay | Present across all 3 index cases as core naming feature (izumi2015germlinegainoffunctionmutations pages 3-4, izumi2015germlinegainoffunctionmutations pages 15-18) | HP:0100543 Cognitive impairment; HP:0001249 Intellectual disability |
| Core phenotype: facial | Coarse facies/dysmorphic facial features | Core naming feature; dysmorphic/coarse facial appearance reported in all 3 probands (izumi2015germlinegainoffunctionmutations pages 3-4, izumi2015germlinegainoffunctionmutations pages 15-18) | HP:0000280 Coarse facial features |
| Core phenotype: cardiac | Congenital heart disease, especially PDA and/or VSD | Cardiac defects in all 3 probands; PDA reported in 3/3, VSD in 2/3 from available case descriptions (izumi2015germlinegainoffunctionmutations pages 15-18) | HP:0001644 Congenital heart defect; HP:0001643 Patent ductus arteriosus; HP:0001629 Ventricular septal defect |
| Core phenotype: obesity | Obesity/abnormal weight gain | Common syndrome-defining feature; described in all 3 probands and considered a core component of the acronym (izumi2015germlinegainoffunctionmutations pages 3-4, izumi2015germlinegainoffunctionmutations pages 15-18, izumi2015germlinegainoffunctionmutations pages 8-10) | HP:0001513 Obesity |
| Core phenotype: pulmonary/airway | Chronic lung disease/airway involvement including tracheomalacia, laryngomalacia, subglottic-tracheal stenosis | Pulmonary involvement in 3/3 probands; chronic lung disease noted as universal in initial cohort (izumi2015germlinegainoffunctionmutations pages 15-18, izumi2015germlinegainoffunctionmutations pages 8-10) | HP:0002093 Respiratory insufficiency; HP:0002783 Tracheomalacia; HP:0001600 Laryngomalacia |
| Core phenotype: growth/skeletal | Short stature and skeletal dysplasia with vertebral anomalies, kyphoscoliosis, brachydactyly | Short stature and brachydactyly in all 3; vertebral/skeletal anomalies in multiple probands (izumi2015germlinegainoffunctionmutations pages 15-18) | HP:0004322 Short stature; HP:0001156 Brachydactyly; HP:0002650 Scoliosis; HP:0000929 Abnormality of the vertebral column |
| Additional phenotypes | Gastroesophageal reflux, constipation, hearing loss, horseshoe kidney, cryptorchidism, cataracts | Present in subsets rather than all cases; evidence remains case-based (izumi2015germlinegainoffunctionmutations pages 15-18, piche2019theexpandingphenotypes pages 7-9) | HP:0002020 Gastroesophageal reflux; HP:0002019 Constipation; HP:0000084 Horseshoe kidney; HP:0000028 Cryptorchidism; HP:0000518 Cataract |
| Age/onset/course | Congenital or early-childhood onset developmental disorder with chronic multisystem manifestations | Discovery cases were pediatric/developmental presentations; no formal staging system or long-term natural history study identified (izumi2015germlinegainoffunctionmutations pages 3-4, izumi2015germlinegainoffunctionmutations pages 15-18) | HP:0003577 Congenital onset |
| Key cell/tissue systems | Brain/neurodevelopment, craniofacial tissues, heart, airway/lung, skeleton, gastrointestinal tract, kidney, gonads, eye | Multisystem developmental syndrome inferred from human phenotype distribution; mechanistic studies mainly in dermal fibroblasts (izumi2015germlinegainoffunctionmutations pages 15-18, izumi2015germlinegainoffunctionmutations pages 10-11, izumi2015germlinegainoffunctionmutations pages 11-13) | UBERON: brain, heart, lung, vertebral column; CL: fibroblast |
| Omics evidence | Patient fibroblast transcriptomics showed 288 downregulated and 445 upregulated genes in one analysis; RNA-seq identified 519 differentially expressed genes in CHOPS samples | Disease-relevant direct targets include MYC, JUN, TMEM100, ZNF711, FAM13C; direct AFF4 targets upregulated by 9–127% (mean 48.9%) (izumi2015germlinegainoffunctionmutations pages 4-6, izumi2015germlinegainoffunctionmutations pages 11-13) | GO: embryonic organ development; GO: skeletal system development |
| Chromatin evidence | ChIP-seq showed altered genome-wide binding of AFF4, cohesin, and RNAP2 with AFF4 accumulation around TSS/gene regions and excess chromatin-associated AFF4 | Mechanistic link to SEC–cohesin–RNAP2 dysregulation supported in patient cells (izumi2015germlinegainoffunctionmutations pages 8-10, izumi2015germlinegainoffunctionmutations pages 18-22, izumi2016disordersoftranscriptional pages 9-10) | GO: chromatin organization; GO: RNA polymerase II CTD phosphorylation |
| Differential diagnosis | Cornelia de Lange syndrome and related disorders of transcriptional regulation/cohesinopathy spectrum | Overlapping phenotype and partially shared transcriptomic signature, but CHOPS is distinguished by AFF4 GOF rather than classic cohesin-gene LoF (izumi2015germlinegainoffunctionmutations pages 3-4, izumi2015germlinegainoffunctionmutations pages 1-3, tei2024cohesinregulatespromoterproximal pages 1-3) | MONDO/CdLS spectrum cross-reference |
| Diagnosis | Molecular diagnosis is best established by exome/genome sequencing or targeted AFF4 analysis in a patient with CdLS-like features plus obesity/pulmonary involvement/short stature-skeletal findings | Discovery was by exome sequencing; no disease-specific biochemical biomarker or formal consensus criteria identified (izumi2015germlinegainoffunctionmutations pages 3-4, izumi2015germlinegainoffunctionmutations pages 15-18) | NCIT: Whole Exome Sequencing; NCIT: Molecular Genetic Testing |
| Treatment status | No disease-modifying or targeted CHOPS therapy established; management is supportive and organ-specific | No relevant CHOPS interventional trials identified; care inferred from phenotype burden rather than syndrome-specific evidence (piche2019theexpandingphenotypes pages 7-9) | NCIT: Supportive Care; NCIT: Physical Therapy; NCIT: Cardiology Referral; NCIT: Pulmonology Referral |
| Prevention/genetic counseling | Primary prevention not established; recurrence risk generally low when variant is de novo, but standard counseling should address possible germline mosaicism uncertainty | No CHOPS-specific recurrence studies or prevention trials found (izumi2015germlinegainoffunctionmutations pages 3-4) | NCIT: Genetic Counseling |
| Epidemiology | Extremely rare; prevalence and incidence not established | Only a handful of published patients identified in available literature; no population-based estimate (izumi2015germlinegainoffunctionmutations pages 3-4) | Orphan disease epidemiology field: unknown |
| Prognosis | Long-term survival, life expectancy, and prognostic factors are unknown | No longitudinal cohort, survival analysis, or validated prognostic biomarker identified (izumi2015germlinegainoffunctionmutations pages 3-4, izumi2015germlinegainoffunctionmutations pages 15-18) | Prognosis field: unknown |
| Environment/risk modifiers | No established environmental, lifestyle, infectious, or protective factors | Current evidence supports primary monogenic etiology without defined gene-environment interaction data (izumi2015germlinegainoffunctionmutations pages 3-4) | Exposure ontology: not established |
| Model/functional systems | Main disease models are patient-derived fibroblasts and transfected cell lines; Aff4 knockout differs phenotypically from CHOPS, supporting GOF; an ENU Aff1 mouse with related degron mechanism is supportive but indirect | Functional evidence is strong for cellular mechanism, limited for organismal CHOPS-specific modeling (izumi2015germlinegainoffunctionmutations pages 6-8, izumi2015germlinegainoffunctionmutations pages 3-4) | CL: fibroblast; model type: in vitro human cell model |
| Recent developments (2023–2024) | Recent work strengthens the SEC/cohesin pause-release framework relevant to CHOPS: AFF4 shown to have distinct TSS-proximal elongation roles, and cohesin depletion increases SEC recruitment and reduces RNAP2 pausing | Mechanistic context from 2023 AFF1/AFF4 SEC study and 2024 cohesin/SEC preprint supports the CHOPS pathogenic model, though not CHOPS-patient cohorts directly (che2023distinctrolesof pages 2-3, che2023distinctrolesof pages 1-2, tei2024cohesinregulatespromoterproximal pages 1-3) | GO: promoter-proximal RNA polymerase II pausing; GO: transcription elongation |
| Evidence gaps | No validated MONDO ID confirmed here, no syndrome-specific trials, no robust prevalence, no natural-history registry, no single-cell/spatial/proteomic/metabolomic datasets, and no known natural disease in other species | Important for knowledge-base curation to mark as unavailable rather than absent disease biology (izumi2015germlinegainoffunctionmutations pages 3-4, tei2024cohesinregulatespromoterproximal pages 1-3) | Evidence status annotation: not available/unverified |


*Table: This table condenses the highest-confidence knowledge-base fields for CHOPS syndrome, including identifiers, causal AFF4 variants, mechanism, key phenotypes, diagnostic approach, and major evidence gaps. It is designed for rapid downstream curation into a structured rare-disease entry.*

## 1. Disease information

### Definition and identifiers

* **Preferred name:** CHOPS syndrome.
* **Expanded name/synonym:** Cognitive impairment–coarse facies–heart defects–obesity–pulmonary involvement–short stature–skeletal dysplasia syndrome.
* **OMIM:** **616368**.
* **EFO/Open Targets:** **EFO_0009031**; Open Targets associates this entity with one established target, **AFF4** (ENSG00000072364), supported principally by PMID **25730767**. (OpenTargets Search: CHOPS syndrome-AFF4)
* **MONDO:** A definitive current MONDO identifier was not established by the retrieved evidence; it should be marked **unverified**, not guessed. Open Targets separately displays “Cornelia de Lange syndrome 6” as MONDO_0957921, but that label should not automatically be substituted for CHOPS without ontology-level verification. (OpenTargets Search: CHOPS syndrome-AFF4)
* **Orphanet, MeSH, ICD-10/ICD-11:** No disease-specific identifiers were verified. Clinical coding will usually require broader congenital-malformation, neurodevelopmental, or genetic-syndrome codes.

The landmark report was Izumi et al., *Nature Genetics*, online March 2015, volume 47:338–344; PMID **25730767**, DOI [10.1038/ng.3229](https://doi.org/10.1038/ng.3229). Its abstract states: **“Using exome sequencing, we discovered missense mutations in AFF4…in three unrelated probands with a new syndrome…that we have named CHOPS syndrome.”** The evidence is aggregated disease-level literature derived from individually phenotyped patients and patient-derived cells, not population EHR statistics. (izumi2015germlinegainoffunctionmutations pages 3-4, izumi2015germlinegainoffunctionmutations pages 1-3)

## 2. Etiology, risk, and protective factors

The necessary and currently established cause is a **germline heterozygous gain-of-function AFF4 variant** affecting a narrow, highly conserved degron/ALF-homology region. All three original variants were absent from all six tested biological parents, establishing de novo occurrence in that cohort. (izumi2015germlinegainoffunctionmutations pages 3-4)

* **Genetic risk:** A pathogenic activating/degradation-resistant AFF4 allele. No susceptibility loci, modifier genes, founder variants, or polygenic risk scores are established.
* **Environmental, lifestyle, occupational, or infectious risk:** None established. These factors are not considered primary causes.
* **Protective factors:** No genetic or environmental protective factors have been reported.
* **Gene–environment interaction:** Unknown. Obesity may be modified by food intake and activity, but no CHOPS-specific interaction study supports such an effect.
* **Family history:** Usually negative because known cases arose de novo. A negative family history does not reduce suspicion.

## 3. Phenotypes

The phenotype begins prenatally or in early childhood and is chronic. Frequencies below are descriptive of the three index cases.

* **Neurodevelopment:** Cognitive impairment/intellectual disability and developmental delay were shared features (3/3). Severity was clinically meaningful but not quantified by standardized IQ or adaptive-function scales. Suggested terms: **HP:0100543 Cognitive impairment**, **HP:0001249 Intellectual disability**, **HP:0001263 Global developmental delay**. (izumi2015germlinegainoffunctionmutations pages 15-18)
* **Craniofacial:** Coarse/dysmorphic facial appearance occurred in all index patients. Suggested term: **HP:0000280 Coarse facial features**. (izumi2015germlinegainoffunctionmutations pages 3-4, izumi2015germlinegainoffunctionmutations pages 15-18)
* **Growth/metabolic:** Short stature, obesity, and brachydactyly were shared findings (3/3). Obesity may emerge during childhood; the original authors proposed altered appetite regulation because AFF4 is expressed in hypothalamus, but this remains a hypothesis rather than a demonstrated metabolic pathway. Suggested terms: **HP:0004322 Short stature**, **HP:0001513 Obesity**, **HP:0001156 Brachydactyly**. (izumi2015germlinegainoffunctionmutations pages 15-18, izumi2015germlinegainoffunctionmutations pages 8-10)
* **Cardiac:** Patent ductus arteriosus was reported in 3/3 and ventricular septal defect in 2/3. Suggested terms: **HP:0001643 Patent ductus arteriosus**, **HP:0001629 Ventricular septal defect**, **HP:0001627 Abnormal heart morphology**. (izumi2015germlinegainoffunctionmutations pages 15-18, piche2019theexpandingphenotypes pages 7-9)
* **Pulmonary/upper airway:** Pulmonary involvement or chronic lung disease affected all three. Individual manifestations included tracheomalacia, laryngomalacia, narrow oropharynx, and subglottic/tracheal stenosis. Suggested terms: **HP:0002783 Tracheomalacia**, **HP:0001600 Laryngomalacia**, **HP:0002093 Respiratory insufficiency**, and the appropriate HPO stenosis term after clinical confirmation. (izumi2015germlinegainoffunctionmutations pages 15-18, izumi2015germlinegainoffunctionmutations pages 8-10)
* **Skeletal:** Vertebral abnormalities, kyphoscoliosis, and brachydactyly were reported; severity varies. Suggested terms: **HP:0000929 Abnormality of the vertebral column**, **HP:0002751 Kyphoscoliosis**, **HP:0002650 Scoliosis**, **HP:0001156 Brachydactyly**. (izumi2015germlinegainoffunctionmutations pages 15-18)
* **Gastrointestinal:** Gastroesophageal reflux and constipation are reported manifestations. Suggested terms: **HP:0002020 Gastroesophageal reflux**, **HP:0002019 Constipation**. (piche2019theexpandingphenotypes pages 7-9)
* **Other variable findings:** Horseshoe kidney (**HP:0000085**), cryptorchidism (**HP:0000028**), hearing loss (**HP:0000365**), and cataracts (**HP:0000518**) occurred in individual patients. (izumi2015germlinegainoffunctionmutations pages 15-18)

No CHOPS-specific EQ-5D, SF-36, PROMIS, or caregiver-burden study exists. Nevertheless, developmental disability, respiratory disease, congenital heart disease, skeletal restriction, and communication/motor limitations plausibly impose substantial lifelong effects on schooling, independence, mobility, and caregiver burden; these are clinical inferences rather than measured syndrome-specific outcomes.

## 4. Genetic and molecular information

**AFF4**—ALF transcription elongation factor 4, Ensembl **ENSG00000072364**—is the only established causal gene. The original variants are heterozygous missense substitutions: c.760A>G/p.Thr254Ala, c.761C>G/p.Thr254Ser, and c.772C>T/p.Arg258Trp. They affect highly conserved residues and were germline/de novo, not somatic. (izumi2015germlinegainoffunctionmutations pages 3-4, OpenTargets Search: CHOPS syndrome-AFF4)

The functional classification is **gain of function through protein stabilization**, not haploinsufficiency. Mutants resist SIAH1-dependent ubiquitination/proteasomal turnover and accumulate particularly in chromatin fractions. Phenotypic differences between CHOPS patients, AFF4 genomic deletions, and Aff4-knockout mice further argue against simple loss of function. (izumi2015germlinegainoffunctionmutations pages 6-8, OpenTargets Search: CHOPS syndrome-AFF4)

Population frequencies were not supplied in the retrieved primary text. For clinical curation, current gnomAD absence or extreme rarity should be checked against the exact transcript/build at interpretation time; absence alone is insufficient because the mechanism and tight positional clustering are critical. ClinVar classifications should likewise be retrieved contemporaneously. No validated modifier gene, disease-specific DNA-methylation episignature, pathogenic structural variant, repeat expansion, mitochondrial variant, or somatic mosaic mechanism has been established.

## 5. Environmental information

No toxin, radiation, pollution, occupation, diet, smoking, alcohol exposure, exercise pattern, or pathogen has been shown to cause or trigger CHOPS syndrome. Environmental management may influence secondary obesity, cardiopulmonary fitness, reflux, and constipation, but it cannot reverse the congenital AFF4 variant. There is no infectious or zoonotic component.

## 6. Mechanism and pathophysiology

### Causal chain

1. A missense change alters the AFF4 degron/ALF-homology region.
2. Mutant AFF4 interacts inadequately with the SIAH1 degradation machinery and becomes resistant to ubiquitin-dependent proteasomal clearance.
3. Stabilized AFF4 accumulates on chromatin as part of the SEC, whose other components include ELL/ELL2 and P-TEFb (**CDK9–cyclin T1**).
4. Excess SEC perturbs promoter-proximal Pol II pause release and productive elongation, including altered Ser2-phosphorylated Pol II distribution.
5. Genome-wide AFF4, cohesin/RAD21, SPT5, and Pol II occupancy changes produce developmental transcriptional dysregulation.
6. Misexpression of developmental, skeletal, extracellular-matrix, and immediate-early genes leads to the multisystem phenotype. (izumi2015germlinegainoffunctionmutations pages 4-6, izumi2015germlinegainoffunctionmutations pages 6-8, izumi2016disordersoftranscriptional pages 9-10, izumi2015germlinegainoffunctionmutations pages 1-3)

In patient fibroblasts, one analysis identified **288 downregulated and 445 upregulated genes**. Direct AFF4 targets increased **9–127% (mean 48.9%)**, including **MYC, JUN, TMEM100, ZNF711, and FAM13C**. Upregulated sets were enriched for homeobox proteins, skeletal-system development, anterior–posterior patterning, and embryonic-organ development; downregulated sets included actin-binding and extracellular-matrix genes. A separately described RNA-seq analysis reported **519 differentially expressed genes**. (izumi2015germlinegainoffunctionmutations pages 4-6, izumi2015germlinegainoffunctionmutations pages 11-13)

The primary experimental systems were patient dermal fibroblasts, hTERT-immortalized fibroblasts, HEK293T overexpression assays, and HeLa lysates. Methods included microarray, RNA-seq, qRT-PCR, western blotting, protein interaction assays, and ChIP-seq. This is strong cellular functional evidence, but it does not identify a single affected embryonic cell lineage. (izumi2015germlinegainoffunctionmutations pages 18-22, izumi2015germlinegainoffunctionmutations pages 10-11, izumi2015germlinegainoffunctionmutations pages 11-13)

### Recent mechanistic developments

A peer-reviewed 2023 study showed that AFF1 and AFF4 are not interchangeable SEC scaffolds: approximately **74% of AFF4 peaks** localized at Pol-II-bound transcription start sites, with AFF4 enriched downstream of the TSS and traveling into highly transcribed gene bodies. AFF4 depletion caused slow elongation/early termination in a subset of bound genes, refining why stabilized AFF4 can distort developmental transcription. Che et al., accepted July 31, 2023, DOI [10.1093/jmcb/mjad049](https://doi.org/10.1093/jmcb/mjad049). This was general cell-line biology, not a CHOPS patient cohort. (che2023distinctrolesof pages 2-3, che2023distinctrolesof pages 1-2)

A March 16, 2024 bioRxiv preprint found that acute cohesin depletion reduced promoter Pol II binding and pausing while increasing SEC recruitment; SEC inhibition abolished the pausing reduction. This supports a model in which cohesin normally limits SEC access to promoters. The study used RAD21/SMC1A degron-engineered HCT116 cells, nascent-RNA sequencing, ChIP-seq, and the experimental SEC inhibitor KL-1; it is mechanistically relevant but was **not peer reviewed in the retrieved 2024 version and is not therapeutic evidence for CHOPS**. DOI [10.1101/2024.03.15.584908](https://doi.org/10.1101/2024.03.15.584908). (tei2024cohesinregulatespromoterproximal pages 1-3, tei2024cohesinregulatespromoterproximal pages 14-17)

Suggested annotations include **GO:0006368 transcription elongation by RNA polymerase II**, **GO:0006357 regulation of transcription by RNA polymerase II**, protein ubiquitination/proteasomal catabolism, chromatin binding, embryonic organ development, skeletal-system development, and anterior–posterior pattern specification. Relevant cellular compartments are **nucleus/chromatin**; suggested cell term for the directly assayed human system is **CL:0000057 fibroblast**. No CHOPS-specific immune, metabolic, lipidomic, metabolomic, single-cell, spatial-transcriptomic, or multi-omic signature has been reported.

## 7. Anatomical structures affected

Primary systems include the developing central nervous system, craniofacial complex, heart, upper airway/lung, axial and appendicular skeleton, and growth-regulatory tissues. Variable secondary involvement includes gastrointestinal tract, kidney, testes, ear, and lens. Suggested UBERON mappings include **brain (UBERON:0000955), heart (UBERON:0000948), lung (UBERON:0002048), trachea (UBERON:0003126), vertebral column (UBERON:0001130), kidney (UBERON:0002113), and eye (UBERON:0000970)**. Mechanistic localization is nuclear/chromatin-associated rather than mitochondrial, lysosomal, or extracellular. No consistent lateralization has been reported. (izumi2015germlinegainoffunctionmutations pages 15-18, izumi2015germlinegainoffunctionmutations pages 8-10)

## 8. Temporal development

CHOPS is a congenital/early-childhood developmental disorder with chronic, lifelong manifestations. Heart defects, dysmorphism, airway malacia/stenosis, vertebral anomalies, and growth disturbance may be evident at birth or infancy; developmental impairment becomes clearer with age, and obesity may emerge later. No validated early/intermediate/advanced staging system, remission pattern, progression rate, or critical therapeutic window exists. Early infancy is nevertheless clinically important for detecting airway obstruction, chronic lung disease, feeding/reflux problems, and congenital heart lesions.

## 9. Inheritance and population

Inheritance is best described as **autosomal dominant, usually de novo**. Both sexes were affected in the original cohort—two females and one male. Penetrance appears high for proven degron-region activating variants, but the sample is too small to estimate penetrance statistically. Expressivity is variable, particularly for cardiac, airway, renal, genital, auditory, and ocular findings. Anticipation, founder effects, consanguinity effects, carrier frequency, and ethnic/geographic enrichment are unknown. Germline mosaicism has not been demonstrated but cannot be excluded in counseling. (izumi2015germlinegainoffunctionmutations pages 3-4, izumi2015germlinegainoffunctionmutations pages 15-18)

Neither incidence nor prevalence per 100,000 is known. Published case counts cannot yield a defensible prevalence because ascertainment and molecular testing are incomplete. The condition should be classified as ultra-rare.

## 10. Diagnostics

There are no consensus clinical criteria or diagnostic biochemical biomarkers. Suspicion should arise in a child with developmental impairment/coarse facies plus the combination of obesity, short stature, skeletal/vertebral abnormalities, congenital heart disease, and chronic pulmonary or structural airway disease—especially when CdLS testing is negative.

**Recommended molecular workflow:**

1. Trio whole-exome or genome sequencing with phenotype-driven analysis of **AFF4**, including careful review of missense variants near residues Thr254–Arg258.
2. Confirm by an orthogonal method and test both parents to establish de novo status.
3. If sequencing is nondiagnostic, consider CNV analysis, genome reanalysis, mosaic calling, and broader developmental-disorder/CdLS-like panels. CMA detects large CNVs but will miss the known single-nucleotide variants; karyotype/FISH are not first-line tests.
4. Functional testing—protein stability, chromatin fractionation, or transcriptomic/ChIP-seq studies—remains research-level rather than routine.

Baseline clinical evaluation should include echocardiography/ECG, pulmonology and ENT airway assessment, oxygenation and sleep evaluation as indicated, spine/limb radiographs, hearing and ophthalmic examinations, renal ultrasound, growth/BMI and nutrition assessment, and developmental, speech, motor, feeding, and behavioral evaluation. These recommendations are phenotype-directed expert practice rather than a validated CHOPS guideline.

Principal differentials include classic/nonclassic CdLS (**NIPBL, SMC1A, SMC3, RAD21, HDAC8**) and other disorders of transcriptional regulation involving **AFF3, BRD4, ANKRD11, EP300, TAF1**, and related chromatin genes. CHOPS is distinguished molecularly by an activating AFF4 degron variant; clinically, obesity and prominent pulmonary/airway disease may be useful clues. Shared AFF4/cohesin/Pol-II dysregulation explains the overlap rather than making the diseases identical. (izumi2015germlinegainoffunctionmutations pages 1-3, tei2024cohesinregulatespromoterproximal pages 1-3, piche2019theexpandingphenotypes pages 7-9)

Population newborn screening, biochemical carrier screening, repeat-expansion testing, mitochondrial testing, liquid biopsy, and prenatal ultrasound criteria are not established.

## 11. Outcome and prognosis

There are no survival curves, mortality rates, life-expectancy estimates, validated prognostic scores, or prognostic biomarkers. Morbidity is likely driven by developmental disability, chronic airway/lung disease, congenital heart disease, orthopedic deformity, obesity, reflux/constipation, and sensory deficits. Recovery from the underlying developmental syndrome is not expected, although individual complications may improve with treatment. The small literature does not justify claims about normal or shortened lifespan.

## 12. Treatment and current applications

No approved disease-modifying pharmacotherapy, AFF4-directed treatment, gene therapy, ASO/siRNA therapy, cell therapy, or genotype-specific clinical pathway exists. ClinicalTrials.gov searches identified no relevant CHOPS interventional trial. Management is therefore multidisciplinary and symptom-directed:

* cardiology surveillance and repair/intervention for hemodynamically significant PDA/VSD;
* pulmonology, ENT, sleep medicine, airway-clearance support, oxygen/ventilatory support, or airway surgery according to anatomy and physiology;
* nutrition and feeding therapy, reflux and constipation treatment, and individualized obesity management;
* physical and occupational therapy, speech/language and augmentative-communication services, educational supports, and developmental pediatrics;
* orthopedic monitoring for vertebral deformity/kyphoscoliosis and mobility impairment;
* audiology, ophthalmology, nephrology/urology, and endocrinology referrals when indicated.

Suggested NCIt concepts include **Supportive Care**, **Physical Therapy**, **Occupational Therapy**, **Speech Therapy**, **Genetic Counseling**, **Cardiac Surgery**, and **Airway Management**, with exact codes verified against the current NCIt release.

SEC inhibitors such as KL-1 can alter SEC activity experimentally, but global transcriptional elongation is fundamental to normal cells. The available data neither establish a safe therapeutic window nor support off-label use in CHOPS. (tei2024cohesinregulatespromoterproximal pages 14-17, che2023distinctrolesof pages 2-3)

## 13. Prevention

Primary prevention through lifestyle modification, vaccination, or exposure avoidance is not applicable to a usually de novo monogenic disorder. Secondary prevention consists of prompt molecular diagnosis and early surveillance for airway, pulmonary, cardiac, feeding, developmental, orthopedic, and sensory complications. Tertiary prevention includes respiratory and cardiac management, obesity prevention, reflux/constipation care, therapy services, mobility support, and educational accommodations.

Genetic counseling should explain autosomal-dominant causation, usually de novo occurrence, uncertainty from possible parental germline mosaicism, and a **50% transmission risk for an affected individual’s future pregnancies** if reproductive fitness permits. When the familial variant is known, prenatal diagnosis and preimplantation genetic testing are technically possible. CHOPS is not part of routine newborn or population carrier screening.

## 14. Other species and natural disease

No naturally occurring CHOPS-equivalent veterinary disease, affected breed, zoonotic transmission, or cross-species infectious susceptibility was identified. Orthologous AFF-family proteins and the SEC/proteasomal mechanism are evolutionarily conserved, but conservation should not be conflated with a naturally occurring animal syndrome.

## 15. Model organisms and experimental systems

The best disease-relevant models are **human patient-derived dermal fibroblasts** carrying p.Thr254Ala, p.Thr254Ser, or p.Arg258Trp and engineered HEK293T/HeLa systems. These reproduce AFF4 stabilization, chromatin accumulation, downstream target activation, and altered AFF4/cohesin/Pol-II occupancy. (izumi2015germlinegainoffunctionmutations pages 18-22, izumi2015germlinegainoffunctionmutations pages 10-11, izumi2015germlinegainoffunctionmutations pages 11-13)

Aff4-knockout mice have phenotypes unlike CHOPS, an important limitation that supports gain-of-function rather than loss-of-function pathogenesis. An ENU-induced mouse mutation in the homologous degron mechanism of **Aff1** provides indirect evidence that altered degradation of AF4/FMR2-family proteins is pathogenic, but it is not a CHOPS knock-in model. (izumi2015germlinegainoffunctionmutations pages 6-8, izumi2015germlinegainoffunctionmutations pages 3-4)

No validated AFF4-CHOPS knock-in mouse, rat, zebrafish, Drosophila, organoid, or patient-derived iPSC model was identified. Priorities for the field are precise p.Thr254/p.Arg258 knock-in models, neural-crest/cardiopulmonary/skeletal organoids, longitudinal registries, and single-cell or spatial profiling during differentiation.

## Evidence assessment and research priorities

The causal inference is strong despite the tiny cohort because three unrelated patients had clustered de novo variants and concordant cellular gain-of-function effects. The major weakness is external validity: penetrance, full phenotypic range, variant-specific severity, survival, and treatment outcomes remain unresolved. The most consequential next steps are international case aggregation, standardized HPO phenotyping, natural-history follow-up, contemporary ClinVar/gnomAD reconciliation, development of precise knock-in models, and testing whether AFF4 normalization can be achieved without broadly suppressing essential SEC-dependent transcription.

### Principal references

1. Izumi K, et al. **Germline Gain-of-Function Mutations in AFF4 Cause a Developmental Syndrome Functionally Linking the Super Elongation Complex and Cohesin.** *Nature Genetics*. Published March 2015;47:338–344. PMID: **25730767**. DOI: [10.1038/ng.3229](https://doi.org/10.1038/ng.3229). (izumi2015germlinegainoffunctionmutations pages 3-4)
2. Izumi K. **Disorders of Transcriptional Regulation: An Emerging Category of Multiple Malformation Syndromes.** *Molecular Syndromology*. Published September 2016;7:262–273. DOI: [10.1159/000448747](https://doi.org/10.1159/000448747). (izumi2016disordersoftranscriptional pages 9-10)
3. Piché J, et al. **The expanding phenotypes of cohesinopathies: one ring to rule them all!** *Cell Cycle*. Published September 2019;18:2828–2848. DOI: [10.1080/15384101.2019.1658476](https://doi.org/10.1080/15384101.2019.1658476). (piche2019theexpandingphenotypes pages 7-9)
4. Che Z, et al. **Distinct roles of two SEC scaffold proteins, AFF1 and AFF4, in regulating RNA polymerase II transcription elongation.** *Journal of Molecular Cell Biology*. Accepted July 31, 2023;15(8):mjad049. DOI: [10.1093/jmcb/mjad049](https://doi.org/10.1093/jmcb/mjad049). (che2023distinctrolesof pages 1-2)
5. Tei S, et al. **Cohesin regulates promoter-proximal pausing of RNA Polymerase II by limiting recruitment of super elongation complex.** bioRxiv preprint posted March 16, 2024. DOI: [10.1101/2024.03.15.584908](https://doi.org/10.1101/2024.03.15.584908). (tei2024cohesinregulatespromoterproximal pages 1-3)

References

1. (izumi2015germlinegainoffunctionmutations pages 3-4): Kosuke Izumi, Ryuichiro Nakato, Zhe Zhang, Andrew C Edmondson, Sarah Noon, Matthew C Dulik, Ramakrishnan Rajagopalan, Charles P Venditti, Karen Gripp, Joy Samanich, Elaine H Zackai, Matthew A Deardorff, Dinah Clark, Julian L Allen, Dale Dorsett, Ziva Misulovin, Makiko Komata, Masashige Bando, Maninder Kaur, Yuki Katou, Katsuhiko Shirahige, and Ian D Krantz. Germline gain-of-function mutations in aff4 cause a developmental syndrome functionally linking the super elongation complex and cohesin. Nature genetics, 47:338-344, Mar 2015. URL: https://doi.org/10.1038/ng.3229, doi:10.1038/ng.3229. This article has 173 citations and is from a highest quality peer-reviewed journal.

2. (izumi2015germlinegainoffunctionmutations pages 4-6): Kosuke Izumi, Ryuichiro Nakato, Zhe Zhang, Andrew C Edmondson, Sarah Noon, Matthew C Dulik, Ramakrishnan Rajagopalan, Charles P Venditti, Karen Gripp, Joy Samanich, Elaine H Zackai, Matthew A Deardorff, Dinah Clark, Julian L Allen, Dale Dorsett, Ziva Misulovin, Makiko Komata, Masashige Bando, Maninder Kaur, Yuki Katou, Katsuhiko Shirahige, and Ian D Krantz. Germline gain-of-function mutations in aff4 cause a developmental syndrome functionally linking the super elongation complex and cohesin. Nature genetics, 47:338-344, Mar 2015. URL: https://doi.org/10.1038/ng.3229, doi:10.1038/ng.3229. This article has 173 citations and is from a highest quality peer-reviewed journal.

3. (izumi2015germlinegainoffunctionmutations pages 8-10): Kosuke Izumi, Ryuichiro Nakato, Zhe Zhang, Andrew C Edmondson, Sarah Noon, Matthew C Dulik, Ramakrishnan Rajagopalan, Charles P Venditti, Karen Gripp, Joy Samanich, Elaine H Zackai, Matthew A Deardorff, Dinah Clark, Julian L Allen, Dale Dorsett, Ziva Misulovin, Makiko Komata, Masashige Bando, Maninder Kaur, Yuki Katou, Katsuhiko Shirahige, and Ian D Krantz. Germline gain-of-function mutations in aff4 cause a developmental syndrome functionally linking the super elongation complex and cohesin. Nature genetics, 47:338-344, Mar 2015. URL: https://doi.org/10.1038/ng.3229, doi:10.1038/ng.3229. This article has 173 citations and is from a highest quality peer-reviewed journal.

4. (izumi2015germlinegainoffunctionmutations pages 1-3): Kosuke Izumi, Ryuichiro Nakato, Zhe Zhang, Andrew C Edmondson, Sarah Noon, Matthew C Dulik, Ramakrishnan Rajagopalan, Charles P Venditti, Karen Gripp, Joy Samanich, Elaine H Zackai, Matthew A Deardorff, Dinah Clark, Julian L Allen, Dale Dorsett, Ziva Misulovin, Makiko Komata, Masashige Bando, Maninder Kaur, Yuki Katou, Katsuhiko Shirahige, and Ian D Krantz. Germline gain-of-function mutations in aff4 cause a developmental syndrome functionally linking the super elongation complex and cohesin. Nature genetics, 47:338-344, Mar 2015. URL: https://doi.org/10.1038/ng.3229, doi:10.1038/ng.3229. This article has 173 citations and is from a highest quality peer-reviewed journal.

5. (OpenTargets Search: CHOPS syndrome-AFF4): Open Targets Query (CHOPS syndrome-AFF4, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (izumi2015germlinegainoffunctionmutations pages 10-11): Kosuke Izumi, Ryuichiro Nakato, Zhe Zhang, Andrew C Edmondson, Sarah Noon, Matthew C Dulik, Ramakrishnan Rajagopalan, Charles P Venditti, Karen Gripp, Joy Samanich, Elaine H Zackai, Matthew A Deardorff, Dinah Clark, Julian L Allen, Dale Dorsett, Ziva Misulovin, Makiko Komata, Masashige Bando, Maninder Kaur, Yuki Katou, Katsuhiko Shirahige, and Ian D Krantz. Germline gain-of-function mutations in aff4 cause a developmental syndrome functionally linking the super elongation complex and cohesin. Nature genetics, 47:338-344, Mar 2015. URL: https://doi.org/10.1038/ng.3229, doi:10.1038/ng.3229. This article has 173 citations and is from a highest quality peer-reviewed journal.

7. (izumi2015germlinegainoffunctionmutations pages 11-13): Kosuke Izumi, Ryuichiro Nakato, Zhe Zhang, Andrew C Edmondson, Sarah Noon, Matthew C Dulik, Ramakrishnan Rajagopalan, Charles P Venditti, Karen Gripp, Joy Samanich, Elaine H Zackai, Matthew A Deardorff, Dinah Clark, Julian L Allen, Dale Dorsett, Ziva Misulovin, Makiko Komata, Masashige Bando, Maninder Kaur, Yuki Katou, Katsuhiko Shirahige, and Ian D Krantz. Germline gain-of-function mutations in aff4 cause a developmental syndrome functionally linking the super elongation complex and cohesin. Nature genetics, 47:338-344, Mar 2015. URL: https://doi.org/10.1038/ng.3229, doi:10.1038/ng.3229. This article has 173 citations and is from a highest quality peer-reviewed journal.

8. (izumi2015germlinegainoffunctionmutations pages 15-18): Kosuke Izumi, Ryuichiro Nakato, Zhe Zhang, Andrew C Edmondson, Sarah Noon, Matthew C Dulik, Ramakrishnan Rajagopalan, Charles P Venditti, Karen Gripp, Joy Samanich, Elaine H Zackai, Matthew A Deardorff, Dinah Clark, Julian L Allen, Dale Dorsett, Ziva Misulovin, Makiko Komata, Masashige Bando, Maninder Kaur, Yuki Katou, Katsuhiko Shirahige, and Ian D Krantz. Germline gain-of-function mutations in aff4 cause a developmental syndrome functionally linking the super elongation complex and cohesin. Nature genetics, 47:338-344, Mar 2015. URL: https://doi.org/10.1038/ng.3229, doi:10.1038/ng.3229. This article has 173 citations and is from a highest quality peer-reviewed journal.

9. (izumi2015germlinegainoffunctionmutations pages 6-8): Kosuke Izumi, Ryuichiro Nakato, Zhe Zhang, Andrew C Edmondson, Sarah Noon, Matthew C Dulik, Ramakrishnan Rajagopalan, Charles P Venditti, Karen Gripp, Joy Samanich, Elaine H Zackai, Matthew A Deardorff, Dinah Clark, Julian L Allen, Dale Dorsett, Ziva Misulovin, Makiko Komata, Masashige Bando, Maninder Kaur, Yuki Katou, Katsuhiko Shirahige, and Ian D Krantz. Germline gain-of-function mutations in aff4 cause a developmental syndrome functionally linking the super elongation complex and cohesin. Nature genetics, 47:338-344, Mar 2015. URL: https://doi.org/10.1038/ng.3229, doi:10.1038/ng.3229. This article has 173 citations and is from a highest quality peer-reviewed journal.

10. (izumi2016disordersoftranscriptional pages 9-10): Kosuke Izumi. Disorders of transcriptional regulation: an emerging category of multiple malformation syndromes. Molecular Syndromology, 7:262-273, Sep 2016. URL: https://doi.org/10.1159/000448747, doi:10.1159/000448747. This article has 69 citations and is from a peer-reviewed journal.

11. (tei2024cohesinregulatespromoterproximal pages 1-3): Shoin Tei, Toyonori Sakata, Atsunori Yoshimura, Toyoaki Natsume, Masato T Kanemaki, Masashige Bando, and Katsuhiko Shirahige. Cohesin regulates promoter-proximal pausing of rna polymerase ii by limiting recruitment of super elongation complex. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.15.584908, doi:10.1101/2024.03.15.584908. This article has 3 citations.

12. (piche2019theexpandingphenotypes pages 7-9): Jessica Piché, Patrick Piet Van Vliet, Michel Pucéat, and Gregor Andelfinger. The expanding phenotypes of cohesinopathies: one ring to rule them all! Cell Cycle, 18:2828-2848, Sep 2019. URL: https://doi.org/10.1080/15384101.2019.1658476, doi:10.1080/15384101.2019.1658476. This article has 121 citations and is from a peer-reviewed journal.

13. (izumi2015germlinegainoffunctionmutations pages 18-22): Kosuke Izumi, Ryuichiro Nakato, Zhe Zhang, Andrew C Edmondson, Sarah Noon, Matthew C Dulik, Ramakrishnan Rajagopalan, Charles P Venditti, Karen Gripp, Joy Samanich, Elaine H Zackai, Matthew A Deardorff, Dinah Clark, Julian L Allen, Dale Dorsett, Ziva Misulovin, Makiko Komata, Masashige Bando, Maninder Kaur, Yuki Katou, Katsuhiko Shirahige, and Ian D Krantz. Germline gain-of-function mutations in aff4 cause a developmental syndrome functionally linking the super elongation complex and cohesin. Nature genetics, 47:338-344, Mar 2015. URL: https://doi.org/10.1038/ng.3229, doi:10.1038/ng.3229. This article has 173 citations and is from a highest quality peer-reviewed journal.

14. (che2023distinctrolesof pages 2-3): Zhuanzhuan Che, Xiaoxu Liu, Qian Dai, Ke Fang, Chenghao Guo, Junjie Yue, Haitong Fang, Peng Xie, Zhuojuan Luo, and Chengqi Lin. Distinct roles of two sec scaffold proteins, aff1 and aff4, in regulating rna polymerase ii transcription elongation. Journal of Molecular Cell Biology, Aug 2023. URL: https://doi.org/10.1093/jmcb/mjad049, doi:10.1093/jmcb/mjad049. This article has 8 citations and is from a peer-reviewed journal.

15. (che2023distinctrolesof pages 1-2): Zhuanzhuan Che, Xiaoxu Liu, Qian Dai, Ke Fang, Chenghao Guo, Junjie Yue, Haitong Fang, Peng Xie, Zhuojuan Luo, and Chengqi Lin. Distinct roles of two sec scaffold proteins, aff1 and aff4, in regulating rna polymerase ii transcription elongation. Journal of Molecular Cell Biology, Aug 2023. URL: https://doi.org/10.1093/jmcb/mjad049, doi:10.1093/jmcb/mjad049. This article has 8 citations and is from a peer-reviewed journal.

16. (tei2024cohesinregulatespromoterproximal pages 14-17): Shoin Tei, Toyonori Sakata, Atsunori Yoshimura, Toyoaki Natsume, Masato T Kanemaki, Masashige Bando, and Katsuhiko Shirahige. Cohesin regulates promoter-proximal pausing of rna polymerase ii by limiting recruitment of super elongation complex. bioRxiv, Mar 2024. URL: https://doi.org/10.1101/2024.03.15.584908, doi:10.1101/2024.03.15.584908. This article has 3 citations.

## Artifacts

- [Edison artifact artifact-00](CHOPS_Syndrome-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.