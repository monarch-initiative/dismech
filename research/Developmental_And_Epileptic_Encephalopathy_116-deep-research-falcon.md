---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-27T02:47:53.605777'
end_time: '2026-08-27T02:58:53.739862'
duration_seconds: 660.13
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Developmental and Epileptic Encephalopathy 116
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 20
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 3
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Developmental_And_Epileptic_Encephalopathy_116-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Developmental and Epileptic Encephalopathy 116
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Developmental and Epileptic Encephalopathy 116** covering all of the
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
- **Disease Name:** Developmental and Epileptic Encephalopathy 116
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Developmental and Epileptic Encephalopathy 116** covering all of the
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


# Developmental and Epileptic Encephalopathy 116 (DEE116): Disease-Characteristics Report

## Executive summary and evidence limits

Developmental and epileptic encephalopathy 116 (DEE116) is a newly delineated, ultra-rare, autosomal-dominant neurodevelopmental disorder caused by heterozygous variants that abolish the canonical translation start of **GLUL**, the gene encoding glutamine synthetase (GS; glutamate-ammonia ligase). The authors of the foundational 2024 report proposed the mechanistic name **glutamine synthetase stabilization disorder (GSSD)**. Unlike recessive glutamine-synthetase deficiency, DEE116 is a **gain-of-stabilization** disorder: translation reinitiates at Met18, removing an N-terminal degradation signal while retaining catalytic function. The resulting GS protein evades glutamine-induced proteasomal degradation. (jones2024clustereddenovo pages 1-3, jones2024clustereddenovo pages 11-12, jones2024clustereddenovo pages 3-4)

The evidence base remains extremely small: nine females reported in the foundational 2024 cohort and one 25-year-old male reported in 2025. Consequently, phenotype percentages below are descriptive case-series frequencies—not population estimates—and penetrance, survival, genotype-response relationships, and treatment response rates cannot yet be estimated reliably. (carbonell2025maleprobandwith pages 1-2, jones2024clustereddenovo pages 5-6, carbonell2025maleprobandwith pages 3-5)

| Topic | Summary | Evidence type | Key source(s) |
|---|---|---|---|
| Identity / identifier | Developmental and epileptic encephalopathy 116 (DEE116); MONDO:0970945; also proposed as “glutamine synthetase stabilization disorder (GSSD)”. Disease-target association links DEE116 to **GLUL**. (jones2024clustereddenovo pages 11-12, OpenTargets Search: Developmental and epileptic encephalopathy 116-GLUL) | Human cohort; database | Jones et al., *Am J Hum Genet* 2024, PMID: 38579670, DOI: https://doi.org/10.1016/j.ajhg.2024.03.005; OpenTargets disease-target association (OpenTargets Search: Developmental and epileptic encephalopathy 116-GLUL) |
| Causal gene / inheritance | Caused by heterozygous **GLUL** start-codon-disrupting variants or 5′UTR splice variants causing start loss; de novo in all evaluated families; mechanism is autosomal dominant by protein stabilization rather than deficiency. GLUL OMIM: 138290; DEE116 gene listed as GLUL MIM: 620806 in follow-up case report. (carbonell2025maleprobandwith pages 1-2, jones2024clustereddenovo pages 4-5, jones2024clustereddenovo pages 3-4) | Human cohort; case report | Jones et al. 2024 PMID: 38579670; Carbonell et al. 2025 PMID: 39985170, DOI: https://doi.org/10.1016/j.xhgg.2025.100419 |
| Reported cohort size / sex / ages | Foundational cohort: **9 probands**, all **female**, ages **16 months–16 years**; follow-up report adds **1 adult male**, age **25 years**, making **10 reported individuals** total in current literature. (carbonell2025maleprobandwith pages 1-2, jones2024clustereddenovo pages 5-6, carbonell2025maleprobandwith pages 3-5) | Human cohort; case report | Jones et al. 2024 PMID: 38579670; Carbonell et al. 2025 PMID: 39985170 |
| Core phenotype frequencies | In Jones cohort: seizures **8/8**, global developmental delay **9/9**, hypotonia **9/9**; severe/profound developmental impairment was typical. Male case: non-verbal, cortical visual impairment, limb contractures, scoliosis, feeding difficulties, growth delay, total-care dependent. (jones2024clustereddenovo pages 5-6, carbonell2025maleprobandwith pages 3-5) | Human cohort; case report | Jones et al. 2024 PMID: 38579670; Carbonell et al. 2025 PMID: 39985170 |
| Seizure onset / types | Jones cohort seizure onset **10 weeks–22 months**; generalized onset **7/8**, focal onset **4/8**; tonic-clonic **6/8**, tonic **2/8**, clonic **2/8**, myoclonic **4/8**, atonic **1/8**, absence **1/8**, epileptic spasms **1/8**; seizure frequency ranged **sporadic to daily**; treatment refractory **6/7**. Male case onset at **24 months**, weekly focal and generalized seizures, including myoclonic and generalized tonic-clonic seizures, compatible with Lennox-Gastaut syndrome. (carbonell2025maleprobandwith pages 2-3, carbonell2025maleprobandwith pages 3-5) | Human cohort; case report | Jones et al. 2024 PMID: 38579670; Carbonell et al. 2025 PMID: 39985170 |
| MRI findings | Jones cohort MRI abnormal in **7/7**; enlarged perivascular spaces **5/7**, thinning corpus callosum **7/7**, hypomyelination **7/7**; one patient had periventricular nodular heterotopia. Male case had **normal brain MRI** at ages 1 and 3 years. (jones2024clustereddenovo pages 1-3, carbonell2025maleprobandwith pages 3-5) | Human cohort; case report | Jones et al. 2024 PMID: 38579670; Carbonell et al. 2025 PMID: 39985170 |
| Biochemistry | Despite GLUL involvement, Jones cohort showed **normal plasma glutamine** in **6/8**, **normal CSF glutamine** in **5/7** (abstract says normal CSF biochemistry; evidence summary notes normal CSF glutamine n=4 in available excerpt), and **normal serum ammonia** in **3** tested; male case had **no plasma/CSF glutamine or ammonia measured**. (carbonell2025maleprobandwith pages 2-3, jones2024clustereddenovo pages 5-6, jones2024clustereddenovo pages 11-12) | Human cohort; case report | Jones et al. 2024 PMID: 38579670; Carbonell et al. 2025 PMID: 39985170 |
| Variant spectrum | Seven/9 original probands had start-loss variants in the initiation codon: **c.3G>A**, **c.1A>T**, **c.1A>C**, **c.1A>G** (recurrent **c.1A>G** in **4** individuals). Two had 5′UTR splice-disrupting variants upstream of exon 2: **c.-13-1G>A** and **c.-13-2A>G** (format normalized from article excerpt). Male case carried recurrent **c.-13-2A>G**; variant absent from gnomAD v4 in that report and diagnostic submission was ClinVar **SCV005619927**. Jones ClinVar series: **SCV004177219–SCV004177224**. (carbonell2025maleprobandwith pages 2-3, carbonell2025maleprobandwith pages 5-6, jones2024clustereddenovo pages 4-5, jones2024clustereddenovo pages 11-12) | Human cohort; case report; database-linked | Jones et al. 2024 PMID: 38579670; Carbonell et al. 2025 PMID: 39985170 |
| Molecular mechanism | Variants abolish canonical start codon usage; translation reinitiates at **Met18**, removing the N-terminal **degron**. Resulting GS is **stable and enzymatically competent but insensitive to glutamine-mediated degradation/negative feedback** (“gain-of-stabilization”). (carbonell2025maleprobandwith pages 1-2, jones2024clustereddenovo pages 1-3, jones2024clustereddenovo pages 3-4, jones2024clustereddenovo pages 7-8, jones2024clustereddenovo pages 8-10) | Human cohort; in vitro | Jones et al. 2024 PMID: 38579670; Carbonell et al. 2025 PMID: 39985170 |
| Functional evidence | Patient fibroblasts and HEK293 **GLUL**-KO transfection studies showed a smaller GS band; mass spectrometry aligned mutant protein with **Met18** initiation; cycloheximide/high-glutamine assays showed truncated GS resists degradation; enzyme assay showed **GS_met18 activity ~0.99 of full-length**, while known recessive deficiency controls had reduced activity (**0.64–0.65**). (jones2024clustereddenovo pages 6-7, jones2024clustereddenovo pages 7-8, jones2024clustereddenovo pages 8-10) | In vitro | Jones et al. 2024 PMID: 38579670 |
| Cell-type localization | Single-cell / single-nucleus transcriptomics of human cortex showed **GLUL** expression in neuro- and glial-progenitor populations and mature glial cells, especially **astrocytes**, but not post-mitotic neurons. (jones2024clustereddenovo pages 1-3, jones2024clustereddenovo pages 10-11) | Computational single-cell | Jones et al. 2024 PMID: 38579670 |
| Mouse evidence | In utero electroporation in embryonic mouse neocortex overexpressing stabilized GS did **not** show significant effects on neural progenitor abundance, gliogenic progenitors, or neuronal migration, arguing against a simple migration-defect explanation for the single heterotopia case. (jones2024clustereddenovo pages 1-3, jones2024clustereddenovo pages 10-11, jones2024clustereddenovo pages 8-10) | Mouse | Jones et al. 2024 PMID: 38579670 |
| Current treatment evidence | No disease-specific standard therapy established. Human evidence is limited to symptomatic antiseizure management. In the adult male case, **zonisamide and brivaracetam** were reported as most effective for seizure reduction after long-standing refractory epilepsy. (carbonell2025maleprobandwith pages 2-3) | Case report | Carbonell et al. 2025 PMID: 39985170 |
| Experimental therapy status | No DEE116-specific interventional trial identified. Proposed but unproven approaches include **methionine sulfoximine (MSO)**, an irreversible GS inhibitor extrapolated from hyperammonemic animal models, and **antisense oligonucleotides (ASOs)** for splice correction or allele-specific silencing; both remain speculative and require major safety/validation work. (carbonell2025maleprobandwith pages 5-6, jones2024clustereddenovo pages 11-12) | In vitro / translational hypothesis; no disease-specific trial | Jones et al. 2024 PMID: 38579670; Carbonell et al. 2025 PMID: 39985170; no relevant ClinicalTrials.gov hit found in prior search |


*Table: This table condenses the currently available disease-specific evidence for GLUL-related DEE116 across human, experimental, and database sources. It is useful as a quick reference for identifiers, phenotype frequencies, mechanism, and the present absence of validated targeted therapy.*

## 1. Disease information

### Definition

DEE116 is a severe, usually infantile-onset developmental and epileptic encephalopathy characterized by global developmental impairment, hypotonia, multiple seizure types that are commonly drug resistant, and frequent cerebral white-matter abnormalities. The causal metabolic disturbance is believed to arise principally in neurodevelopmental progenitors and astroglial cells rather than post-mitotic neurons. (jones2024clustereddenovo pages 5-6, jones2024clustereddenovo pages 1-3, jones2024clustereddenovo pages 10-11)

### Identifiers and synonyms

- **MONDO:** **MONDO:0970945**.
- **Disease OMIM/MIM:** **620806**, as cited in the 2025 follow-up report.
- **Causal gene:** **GLUL**; gene OMIM **138290**; Ensembl **ENSG00000135821**.
- **Preferred name:** developmental and epileptic encephalopathy 116.
- **Synonyms:** DEE116; developmental and epileptic encephalopathy-116; **glutamine synthetase stabilization disorder (GSSD)**; GLUL-related developmental and epileptic encephalopathy.
- **Distinct allelic disorder:** autosomal-recessive glutamine synthetase deficiency, OMIM **610015**, caused by biallelic hypomorphic variants and associated with low glutamine. It should not be merged with dominant DEE116. (jones2024clustereddenovo pages 11-12, jones2024clustereddenovo pages 3-4, OpenTargets Search: Developmental and epileptic encephalopathy 116-GLUL)
- **Orphanet, MeSH, ICD-10/ICD-11:** no disease-specific entries or dedicated codes were established in the retrieved evidence. Operational coding would therefore use broader developmental/epileptic encephalopathy or genetic epilepsy categories.

OpenTargets associates MONDO:0970945 specifically with GLUL and reports five underlying evidence records. (OpenTargets Search: Developmental and epileptic encephalopathy 116-GLUL)

### Evidence provenance

The disease definition is aggregated from a research cohort assembled through GeneMatcher, functional laboratory studies, and a subsequent single-patient case report—not from an EHR-derived population dataset. The male case incorporated longitudinal clinical records, genome sequencing, annual reanalysis, RNA sequencing, and ClinVar deposition. (jones2024clustereddenovo pages 5-6, carbonell2025maleprobandwith pages 5-6, carbonell2025maleprobandwith pages 3-5, jones2024clustereddenovo pages 3-4)

**Key primary sources**

1. Jones AG et al. “Clustered de novo start-loss variants in GLUL result in a developmental and epileptic encephalopathy via stabilization of glutamine synthetase.” *American Journal of Human Genetics*. Published **April 4, 2024**; 111:729–741. **PMID: 38579670**. DOI: https://doi.org/10.1016/j.ajhg.2024.03.005. (jones2024clustereddenovo pages 5-6, jones2024clustereddenovo pages 12-13)
2. Carbonell E et al. “Male proband with intractable seizures and a de novo start-codon-disrupting variant in GLUL.” *Human Genetics and Genomics Advances*. Published **April 10, 2025**; 6:100419. **PMID: 39985170**. DOI: https://doi.org/10.1016/j.xhgg.2025.100419. (carbonell2025maleprobandwith pages 2-3, carbonell2025maleprobandwith pages 5-6)

**Exact abstract statement from the foundational study:** “We ascertained nine individuals with severe developmental delay, seizures, and white matter abnormalities but normal plasma and cerebrospinal fluid biochemistry with de novo variants in GLUL.” (jones2024clustereddenovo pages 1-3)

## 2. Etiology, risk, and protective factors

### Causal factors

The established cause is a heterozygous, usually demonstrably **de novo**, germline GLUL variant that directly disrupts the start codon or alters 5′-UTR splicing so that the canonical initiation codon is excluded. Parental testing was completed in eight foundational families, and the variant was de novo in all eight; de novo status was unavailable for the ninth. The later male case was also de novo. (carbonell2025maleprobandwith pages 2-3, jones2024clustereddenovo pages 4-5)

### Genetic risk factors

The known pathogenic region is unusually constrained mechanistically:

- Start-loss variants: **NM_001033044.4:c.3G>A, c.1A>T, c.1A>C, and c.1A>G**, all annotated p.Met1?.
- The recurrent **c.1A>G** occurred in four of nine foundational cases.
- 5′-UTR splice variants: **c.-13-1G>A** and **c.-13-2A>G**; the latter recurred in the adult male.
- All foundational variants were absent from gnomAD v3.1.2; the male’s c.-13-2A>G variant was also absent from gnomAD v4. (carbonell2025maleprobandwith pages 2-3, jones2024clustereddenovo pages 5-6, jones2024clustereddenovo pages 4-5)

The c.-13-2A>G variant was classified as **likely pathogenic**, using PS2_Moderate, PM1, PS3_Supporting, and PM2_Supporting. Relevant submissions include ClinVar **SCV004177219–SCV004177224** for the foundational series and **SCV005619927** for the male case. (carbonell2025maleprobandwith pages 2-3, carbonell2025maleprobandwith pages 5-6, jones2024clustereddenovo pages 11-12)

### Environmental, lifestyle, infectious, and demographic risk

No toxin, infection, diet, occupation, parental age, lifestyle exposure, or other environmental cause has been established. No susceptibility loci or validated modifier genes are known. An initial all-female cohort prompted speculation about sex-dependent glutamine metabolism, but the affected male establishes that disease is not female limited; the apparent sex imbalance may reflect ascertainment in a cohort of only ten people. (carbonell2025maleprobandwith pages 3-5, jones2024clustereddenovo pages 10-11)

### Protective factors and gene–environment interaction

No genetic or environmental protective factor has been demonstrated. Glutamine concentration regulates degradation of normal GS in vitro, but there is no clinical evidence that dietary glutamine manipulation is beneficial or safe. This biochemical substrate-response relationship must not be interpreted as an established dietary gene–environment interaction. (jones2024clustereddenovo pages 7-8, jones2024clustereddenovo pages 8-10)

## 3. Phenotypes

### Neurologic and developmental phenotype

| Phenotype | Frequency/current evidence | Onset/course and impact | Suggested HPO term |
|---|---:|---|---|
| Seizures | 8/8 with data in the original cohort; present in male | 10 weeks–22 months in cohort; 24 months in male; sporadic-to-daily or weekly; often chronic and refractory | Seizure, **HP:0001250** |
| Drug-resistant epilepsy | 6/7 evaluable foundational cases; male also refractory | Persistent despite multiple antiseizure medicines; major care burden | Drug-resistant epilepsy, **HP:0100543** |
| Generalized seizure onset | 7/8; male also had generalized seizures | Infantile/early childhood; episodic | Generalized-onset seizure, **HP:0002197** |
| Focal seizure onset | 4/8; male also affected | Episodic; evolved to multifocal/generalized EEG abnormalities in male | Focal-onset seizure, **HP:0007359** |
| Tonic-clonic seizures | 6/8; male affected | Variable frequency and severity | **HP:0002069** |
| Myoclonic seizures | 4/8; male affected | Episodic | **HP:0032794** |
| Tonic seizures | 2/8 | Episodic | **HP:0032792** |
| Clonic seizures | 2/8 | Episodic | **HP:0020221** |
| Atonic/absence/spasms | Each 1/8 | Rare in current series | **HP:0010819**, **HP:0011147**, **HP:0011097** |
| Global developmental delay | 9/9; male affected | Severe-to-profound; chronic, with adult dependence | **HP:0001263** |
| Hypotonia | 9/9; male affected | Early and persistent | **HP:0001252** |
| Absent speech/non-verbal | Documented in male; incompletely reported in cohort | Lifelong communication limitation | **HP:0001344** |
| Cortical visual impairment | Documented in male, recognized at 5 months | Chronic visual disability | **HP:0100704** |
| Feeding difficulty/G-tube dependence | Documented in male | Chronic; affected nutrition and growth | **HP:0011968**; gastrostomy status may be separately encoded |
| Contractures, hip dysplasia, neuromuscular scoliosis | Documented in adult male | Progressive secondary motor complications | **HP:0003121**, **HP:0001385**, **HP:0002650** |
| Growth delay/short stature | Documented in male: 40.8 kg, 152 cm at 25 years | Chronic | **HP:0001510**, **HP:0004322** |

Frequencies and HPO mappings are derived from the published comparison table; denominators vary because not all variables were recorded in every patient. (carbonell2025maleprobandwith pages 3-5)

The adult male was non-verbal, unable to ambulate independently, G-tube dependent, and required total care in a group home. Nonetheless, caregivers reported enjoyment of social contact, music, outdoor activity, adaptive skiing/swimming, and vestibular activities. This is the only disease-specific qualitative quality-of-life information; no EQ-5D, SF-36, PROMIS, or validated caregiver-burden study has been reported. (carbonell2025maleprobandwith pages 3-5)

### Neuroimaging and electrophysiology

MRI was abnormal in **7/7** evaluable foundational cases: hypomyelination **7/7**, thin corpus callosum **7/7**, and enlarged perivascular spaces **5/7**. One individual had periventricular nodular heterotopia. In contrast, the adult male had normal MRIs at ages 1 and 3 years, demonstrating that normal early MRI does not exclude DEE116. Suggested HPO terms are **HP:0006808**, **HP:0033725**, **HP:0012520**, and **HP:0007165**. (jones2024clustereddenovo pages 1-3, carbonell2025maleprobandwith pages 3-5)

The male’s serial EEGs from infancy to age 24 evolved from central-parietal spike-wave discharges to multifocal and generalized abnormalities. His combined seizure phenotype was considered consistent with Lennox–Gastaut syndrome. Detailed aggregate EEG frequencies were not available for the nine-person cohort. (carbonell2025maleprobandwith pages 2-3)

### Laboratory phenotype

Routine biochemical markers can be normal: plasma glutamine was normal in **6/8** and CSF glutamine in **5/7** in the later published comparison; serum ammonia was normal in the three reported as tested. The adult male had not undergone plasma/CSF glutamine or ammonia measurement. Thus, normal glutamine or ammonia does not exclude the diagnosis. (carbonell2025maleprobandwith pages 2-3, jones2024clustereddenovo pages 5-6, carbonell2025maleprobandwith pages 3-5, jones2024clustereddenovo pages 11-12)

## 4. Genetic and molecular information

### Gene and protein

- **Gene:** GLUL; approved protein name glutamate-ammonia ligase/glutamine synthetase.
- **Ensembl:** ENSG00000135821.
- **Gene OMIM:** 138290.
- **Protein:** cytoplasmic GS; approximately 42 kDa per subunit; active protein is a cylindrical decamer.
- **Reaction:** glutamate + ammonia + ATP → glutamine; relevant chemical annotations include **CHEBI:29985** (L-glutamate), **CHEBI:58359** (L-glutamine zwitterion), **CHEBI:16134** (ammonia), and **CHEBI:30616** (ATP), subject to local ontology-version verification. (jones2024clustereddenovo pages 3-4, OpenTargets Search: Developmental and epileptic encephalopathy 116-GLUL)

### Variant class and functional consequence

All currently established dominant DEE116 variants are germline SNVs producing start loss either directly or through abnormal 5′-UTR splicing. No causal frameshift, nonsense, copy-number, chromosomal, repeat-expansion, mitochondrial, or somatic variant class has been established for DEE116. The c.-13-2A>G allele generated an aberrant splice junction in 44% of blood RNA reads, deleting 26 bases including the canonical start. (carbonell2025maleprobandwith pages 5-6)

Translation reinitiates at **Met18**, deleting the first 17 residues, including degron lysines 11 and 14. The mutant protein is catalytically competent but insensitive to glutamine-triggered negative feedback. Incorporation of truncated subunits may stabilize the entire heteromeric GS decamer, including full-length subunits. This is neither conventional haploinsufficiency nor dominant-negative loss of activity. (jones2024clustereddenovo pages 7-8, jones2024clustereddenovo pages 8-10)

### Allele frequencies, modifiers, epigenetics, and chromosomal findings

All reported variants were absent from the cited gnomAD versions. Carrier frequency cannot be estimated and is expected to be extremely low because known cases are predominantly de novo. No modifier gene, founder allele, disease-specific methylation signature, histone abnormality, chromatin signature, or recurrent chromosomal abnormality has been reported. (carbonell2025maleprobandwith pages 2-3, jones2024clustereddenovo pages 5-6)

## 5. Environmental information

DEE116 is a Mendelian disorder without an established environmental, infectious, toxic, radiation, pollution, occupational, smoking, alcohol, exercise, or dietary etiology. Environmental exposures could still influence seizure threshold—as in epilepsy generally—but no DEE116-specific interaction has been studied. There is no zoonotic or transmissible component.

## 6. Mechanism and pathophysiology

### Supported upstream causal chain

1. A de novo heterozygous GLUL start-loss or 5′-UTR splice variant removes the canonical translation initiation site.
2. Translation reinitiates at Met18.
3. The first 17 amino acids—including the glutamine-sensitive N-terminal degron—are lost.
4. Mutant GS retains approximately full catalytic activity but becomes resistant to glutamine-induced ubiquitin/proteasome degradation.
5. GS abundance/activity is therefore inadequately downregulated, producing a gain-of-stabilization metabolic disorder during brain development.
6. Dysregulated glutamate–glutamine, ammonia/nitrogen, and ATP homeostasis plausibly disrupts neural progenitor and astrocyte support of neuronal networks, contributing to developmental impairment, hypomyelination, and epilepsy. Steps 1–5 are experimentally supported; the precise links in step 6 remain mechanistic hypotheses. (jones2024clustereddenovo pages 1-3, jones2024clustereddenovo pages 6-7, jones2024clustereddenovo pages 11-12, jones2024clustereddenovo pages 7-8, jones2024clustereddenovo pages 8-10)

**Exact abstract statement:** the variants produce “a protein that is stable and enzymatically competent but insensitive to negative feedback by glutamine.” (jones2024clustereddenovo pages 1-3)

### Human-cell and in-vitro evidence

Patient fibroblasts showed both full-length and smaller GS isoforms. Mass spectrometry aligned the start-loss product with Met18 initiation. In GLUL-knockout HEK293 cells, full-length GS underwent significantly more degradation in high than low glutamine, whereas Met18 GS did not. Met18 enzyme activity was **0.99 relative to full-length**, while recessive-deficiency controls p.Arg324Cys and p.Arg341Cys were approximately **0.64–0.65** in the study assay. (jones2024clustereddenovo pages 6-7, jones2024clustereddenovo pages 7-8, jones2024clustereddenovo pages 8-10)

Suggested GO annotations include:

- glutamine biosynthetic process, **GO:0006542**;
- glutamate metabolic process, **GO:0006536**;
- cellular nitrogen-compound metabolic process, **GO:0034641**;
- protein ubiquitination, **GO:0016567**;
- proteasomal protein catabolic process, **GO:0010498**;
- regulation of neurotransmitter levels, **GO:0001505**;
- gliogenesis, **GO:0042063**;
- central nervous system myelination, **GO:0022010**.

### Cell types and downstream hypotheses

Human single-cell/single-nucleus datasets showed GLUL expression in neuro- and glial-progenitor cells and, later, principally mature astrocytes; expression was low/absent in post-mitotic neurons. Suggested Cell Ontology terms are **astrocyte (CL:0000127)**, **neural progenitor cell (CL:0011020)**, **radial glial cell (CL:0000681)**, **oligodendrocyte precursor cell (CL:0002453)**, and **neuron (CL:0000540)** as a downstream affected rather than primary GLUL-expressing population. (jones2024clustereddenovo pages 1-3, jones2024clustereddenovo pages 10-11, jones2024clustereddenovo pages 8-10)

Proposed downstream mechanisms include:

- excessive conversion of glutamate/ammonia to glutamine and disturbed neurotransmitter precursor homeostasis;
- altered nitrogen flux and pH;
- astrocytic osmotic stress/swelling;
- suppression of glutaminolysis and altered neural-progenitor energetics;
- excessive ATP consumption by stabilized GS;
- reduced astrocytic ATP release, potentially weakening inhibition and myelination;
- possible non-canonical effects through RHOJ, angiogenesis, and cytoskeletal remodeling.

These mechanisms are biologically plausible but have not been demonstrated directly in DEE116 brains. Systemic glutamine and ammonia may remain normal because liver and other tissues possess compensatory pathways. (jones2024clustereddenovo pages 11-12, jones2024clustereddenovo pages 12-13)

No disease-specific immune, inflammatory, oxidative-stress, apoptosis, autophagy, lipidomic, proteomic-biomarker, metabolomic-signature, spatial-transcriptomic, or integrated multi-omic dataset has been reported.

## 7. Anatomical structures affected

### Organ and tissue levels

The primary organ is the **central nervous system**, particularly the developing cerebral cortex and cerebral white matter. Suggested UBERON terms include **brain (UBERON:0000955)**, **cerebral cortex (UBERON:0000956)**, **prefrontal cortex (UBERON:0000451)**, **cerebral white matter (UBERON:0002437)**, and **corpus callosum (UBERON:0002336)**, with local identifier validation recommended. Imaging suggests bilateral/diffuse rather than consistently lateralized disease. (jones2024clustereddenovo pages 5-6, jones2024clustereddenovo pages 1-3, jones2024clustereddenovo pages 10-11)

Secondary musculoskeletal involvement—contractures, hip dysplasia, and neuromuscular scoliosis—was documented in the adult male and is probably downstream of severe chronic motor impairment. Feeding/growth complications may require gastrointestinal nutritional support. (carbonell2025maleprobandwith pages 3-5)

### Subcellular level

GS is a cytosolic enzyme, making **cytosol (GO:0005829)** and **cytoplasm (GO:0005737)** appropriate primary compartments. The dysregulated control process involves ubiquitin-mediated proteasomal degradation; **proteasome complex (GO:0000502)** is mechanistically relevant but is not the principal steady-state localization of GS. (jones2024clustereddenovo pages 3-4, jones2024clustereddenovo pages 7-8)

## 8. Temporal development

DEE116 is pediatric-onset and likely neurodevelopmental from prenatal brain development onward, although seizures began postnatally between 10 weeks and 24 months in known patients. Developmental impairment and hypotonia are chronic. Epilepsy is episodic but usually persistent and frequently drug resistant. (jones2024clustereddenovo pages 5-6, carbonell2025maleprobandwith pages 3-5)

No validated staging system exists. The adult male showed progressive motor complications and required total care, but whether neurodegeneration is intrinsic to DEE116 or these changes are secondary to severe static encephalopathy, epilepsy, immobility, and orthopedic complications remains uncertain. No spontaneous remission pattern or critical therapeutic window has been established. Because the causal disturbance acts during neurodevelopment, early molecular diagnosis is a rational—but not yet proven—intervention priority. (carbonell2025maleprobandwith pages 3-5)

## 9. Inheritance and population

### Inheritance

The inheritance model is **autosomal dominant**, currently almost always de novo. Penetrance appears high among identified variant carriers, but unbiased penetrance cannot be calculated. Expressivity is variable, as illustrated by abnormal versus normal early MRI and variable seizure types. There is no evidence of anticipation, a founder effect, or a role for consanguinity. Parental germline mosaicism has not been documented but cannot be excluded after an apparently de novo result. (carbonell2025maleprobandwith pages 2-3, jones2024clustereddenovo pages 5-6, carbonell2025maleprobandwith pages 3-5)

### Epidemiology

Only ten affected individuals were documented in the retrieved disease-specific literature: nine females aged approximately 16 months–16 years in 2024 and one 25-year-old male in 2025. Prevalence, incidence, carrier frequency, ethnic differences, geographic gradients, and a reliable sex ratio are unavailable. Cases in the original international cohort came from New Zealand, North America, Europe, and South Africa, providing no evidence for geographic restriction. (carbonell2025maleprobandwith pages 1-2, jones2024clustereddenovo pages 5-6)

## 10. Diagnostics

### Clinical recognition

Consider DEE116 in an infant or child with severe developmental delay, hypotonia, early multiple seizure types or drug-resistant epilepsy, and hypomyelination/thin corpus callosum—especially when standard metabolic tests are normal. A normal early MRI does not exclude it. No society-endorsed disease-specific diagnostic criteria currently exist. (jones2024clustereddenovo pages 5-6, carbonell2025maleprobandwith pages 3-5)

### Recommended investigations

1. **EEG:** baseline and longitudinal video-EEG to classify focal/generalized seizures, epileptic spasms, and encephalopathic patterns.
2. **MRI brain:** include high-quality myelin-sensitive sequences; assess corpus callosum, perivascular spaces, migration abnormalities, and longitudinal change.
3. **Biochemistry:** plasma amino acids including glutamine, ammonia, blood gas/pH, metabolic panel; consider CSF amino acids where clinically justified. Normal results do not rule out DEE116.
4. **MR spectroscopy:** investigationally useful for in-vivo cerebral glutamine because plasma and CSF may not represent brain interstitial metabolism; it is not a validated diagnostic biomarker. (carbonell2025maleprobandwith pages 3-5, jones2024clustereddenovo pages 10-11)

### Genetic-testing strategy

- **First line:** trio WES or WGS, or a comprehensive DEE/epilepsy panel that includes **GLUL** and covers non-coding exon/5′-UTR splice boundaries.
- **Variant interpretation:** prioritize de novo variants affecting c.1–c.3 and 5′-UTR splice acceptors; do not restrict interpretation to recessive GLUL deficiency.
- **RNA sequencing:** highly valuable for suspected 5′-UTR splice variants; blood RNA confirmed the 26-bp deletion and 44% aberrant junction in the male.
- **Reanalysis:** essential when prior testing was negative. The male’s earlier 13- and 40-gene panels were negative, genome sequencing was initially inconclusive because GLUL was then associated only with recessive disease, and annual reanalysis ultimately enabled diagnosis.
- **CMA/karyotype/FISH:** useful for broader developmental-delay workup but not targeted tests for the known SNV mechanism.
- **Mitochondrial or repeat-expansion testing:** phenotype-driven only; neither is a known DEE116 mechanism. (carbonell2025maleprobandwith pages 5-6, carbonell2025maleprobandwith pages 3-5)

### Differential diagnosis

Key differentials include recessive glutamine-synthetase deficiency, other monogenic DEEs, hypomyelinating leukodystrophies, neuronal-migration disorders, Lennox–Gastaut syndrome of another cause, structural epilepsies, and treatable metabolic epileptic encephalopathies. Recessive GS deficiency is distinguished by biallelic active-site variants, enzyme deficiency, and characteristically low plasma/CSF glutamine rather than dominant degron-loss stabilization. (carbonell2025maleprobandwith pages 3-5, jones2024clustereddenovo pages 3-4)

There is no population newborn screen, validated biochemical screen, or routine carrier-screening program. Cascade testing should confirm parental status and can inform reproductive counseling.

## 11. Outcome and prognosis

All nine foundational patients were reported alive at ages up to 16 years; the additional male was alive at 25 years. These observations demonstrate survival into adulthood but do not support survival-rate or life-expectancy estimates. No disease-specific mortality rate or sudden-unexpected-death-in-epilepsy estimate is available. (carbonell2025maleprobandwith pages 1-2, carbonell2025maleprobandwith pages 3-5)

Long-term morbidity is substantial: severe/profound developmental disability, persistent epilepsy, impaired communication and mobility, feeding dependence, and secondary orthopedic complications. Complete developmental recovery has not been reported. Prognostic biomarkers are unknown. Potential factors requiring future study include seizure burden, degree of white-matter abnormality, cerebral glutamine measured by MR spectroscopy, and residual ratio of normal to aberrant transcript. None is currently validated. (carbonell2025maleprobandwith pages 3-5, jones2024clustereddenovo pages 10-11)

## 12. Treatment

### Current clinical implementation

There is no approved disease-modifying or DEE116-specific therapy. Management is individualized and symptomatic:

- antiseizure pharmacotherapy selected by seizure type and EEG syndrome;
- rescue plans for prolonged seizures/status epilepticus;
- physical, occupational, speech/augmentative-communication, and visual therapy;
- nutritional assessment, swallowing evaluation, and gastrostomy when necessary;
- orthopedic surveillance for hip displacement, contractures, and scoliosis;
- sleep, respiratory, bone-health, and caregiver-support assessment.

The adult male experienced the best reported seizure reduction with **zonisamide plus brivaracetam**, but this is a single uncontrolled observation and cannot establish comparative efficacy. Suggested NCIt concepts include **Anticonvulsant Agent (NCIT:C264)**, **Physical Therapy (NCIT:C15303)**, **Occupational Therapy**, **Speech Therapy**, and **Gastrostomy**, with exact local NCIt identifiers verified before ingestion. (carbonell2025maleprobandwith pages 2-3, carbonell2025maleprobandwith pages 3-5)

No DEE116 pharmacogenomic association or genotype-specific antiseizure algorithm has been reported.

### Experimental precision approaches

1. **Methionine sulfoximine (MSO):** an irreversible GS inhibitor proposed because the mutant enzyme remains active and over-stable. MSO attenuated some pathology in hyperammonemic rat models at subconvulsant doses, but toxicity, off-target effects, interspecies potency differences, and its own seizure-inducing potential are major barriers. It has not been tested as DEE116 therapy in humans. (jones2024clustereddenovo pages 11-12)
2. **Antisense oligonucleotides:** the recurrent c.-13-2A>G splice defect creates a theoretical opportunity for splice correction or allele-specific knockdown. This proposal has no disease-model efficacy, dosing, biodistribution, or safety validation. (carbonell2025maleprobandwith pages 5-6)
3. **Gene replacement/editing:** not currently supported. Unregulated replacement could worsen a gain-of-stabilization disorder, and an allele-selective approach would be required.

No disease-specific interventional trial or NCT identifier was identified in the ClinicalTrials.gov search. Treatment-response percentages and disease-specific adverse-event rates are unavailable.

## 13. Prevention

No vaccine, lifestyle modification, environmental intervention, diet, or prophylactic drug can prevent a de novo GLUL variant. Primary prevention is therefore limited to informed reproductive options after molecular diagnosis:

- genetic counseling;
- parental testing, with explanation of residual recurrence risk from possible germline mosaicism;
- prenatal diagnosis or preimplantation genetic testing for a known familial variant;
- donor-gamete or other reproductive options according to patient preferences.

Secondary/tertiary prevention consists of early genomic diagnosis, prompt seizure treatment, developmental intervention, aspiration/nutrition management, orthopedic surveillance, and injury/SUDEP risk counseling. Population newborn or carrier screening is not currently justified by prevalence data or an established presymptomatic intervention.

## 14. Other species and natural disease

No naturally occurring veterinary equivalent, breed predisposition, or zoonotic transmission has been reported. GLUL is evolutionarily conserved and its essential biology is illustrated by embryonic lethality of complete **Glul** knockout in mice at approximately embryonic day 3.5, but that loss-of-function state is not homologous to human dominant gain-of-stabilization DEE116. (jones2024clustereddenovo pages 3-4)

Relevant taxonomy suggestions are **Homo sapiens, NCBI Taxon:9606** and **Mus musculus, NCBI Taxon:10090**. No VBO breed annotation applies.

## 15. Model organisms and experimental models

### Available models

- **Patient dermal fibroblasts:** reproduce full-length plus truncated GS isoforms and abnormal glutamine-dependent stability.
- **HEK293 GLUL-knockout complementation system:** supports controlled expression, mass-spectrometric identification of Met18 initiation, stability assays, and catalytic assays.
- **Embryonic mouse in-utero electroporation:** overexpression of full-length or start-loss GS in C57BL/6JRj neocortex at E13.5/E16.5.
- **Human single-cell computational models:** reanalysis of fetal-to-adult cortical datasets localized GLUL expression to progenitors and astroglia. (jones2024clustereddenovo pages 4-5, jones2024clustereddenovo pages 7-8, jones2024clustereddenovo pages 8-10)

### Recapitulation and limitations

The cell systems robustly reproduce the proximal molecular defect but do not model seizures, network development, or white-matter disease. Mouse electroporation found no significant change in Pax6-positive progenitors, Tbr2-positive lineage commitment, Olig2-positive gliogenic progenitors, or neuronal migration. It therefore did not reproduce the human heterotopia observation or broader DEE phenotype. Species differences may be particularly important because human fetal cortical progenitors have distinctive glutaminolysis biology. (jones2024clustereddenovo pages 1-3, jones2024clustereddenovo pages 10-11, jones2024clustereddenovo pages 8-10)

A rigorous future model would require heterozygous knock-in of a human-equivalent start-loss or splice variant, assessment across neural progenitors and astrocytes, EEG/seizure monitoring, myelination, metabolite flux, and rescue with allele-selective suppression. Patient-derived iPSC astrocytes, neuron–astrocyte co-cultures, and cerebral organoids would be valuable but were not reported in the retrieved literature.

## Knowledge-base conclusions

DEE116 should be represented as a **GLUL gain-of-stabilization disorder**, not as generic GLUL deficiency. The most defensible disease graph is: de novo start-codon disruption → Met18 reinitiation → N-terminal degron loss → failure of glutamine-induced GS degradation → dysregulated astroglial/progenitor glutamine and energy homeostasis → altered neuronal-network development, myelination, and seizure susceptibility. The first five nodes are experimentally supported; downstream cellular and clinical links remain provisional. Current care is symptomatic, and neither MSO nor ASO therapy is ready for clinical implementation. (jones2024clustereddenovo pages 1-3, jones2024clustereddenovo pages 11-12, jones2024clustereddenovo pages 7-8, jones2024clustereddenovo pages 8-10)

References

1. (jones2024clustereddenovo pages 1-3): Amy G. Jones, Matilde Aquilino, Rory J. Tinker, Laura Duncan, Zandra Jenkins, Gemma L. Carvill, Stephanie J. DeWard, Dorothy K. Grange, MJ Hajianpour, Benjamin J. Halliday, Muriel Holder-Espinasse, Judit Horvath, Silvia Maitz, Vincenzo Nigro, Manuela Morleo, Victoria Paul, Careni Spencer, Alina I. Esterhuizen, Tilman Polster, Alice Spano, Inés Gómez-Lozano, Abhishek Kumar, Gemma Poke, John A. Phillips, Hunter R. Underhill, Gregory Gimenez, Takashi Namba, and Stephen P. Robertson. Clustered de novo start-loss variants in glul result in a developmental and epileptic encephalopathy via stabilization of glutamine synthetase. American journal of human genetics, 111 4:729-741, Apr 2024. URL: https://doi.org/10.1016/j.ajhg.2024.03.005, doi:10.1016/j.ajhg.2024.03.005. This article has 19 citations and is from a highest quality peer-reviewed journal.

2. (jones2024clustereddenovo pages 11-12): Amy G. Jones, Matilde Aquilino, Rory J. Tinker, Laura Duncan, Zandra Jenkins, Gemma L. Carvill, Stephanie J. DeWard, Dorothy K. Grange, MJ Hajianpour, Benjamin J. Halliday, Muriel Holder-Espinasse, Judit Horvath, Silvia Maitz, Vincenzo Nigro, Manuela Morleo, Victoria Paul, Careni Spencer, Alina I. Esterhuizen, Tilman Polster, Alice Spano, Inés Gómez-Lozano, Abhishek Kumar, Gemma Poke, John A. Phillips, Hunter R. Underhill, Gregory Gimenez, Takashi Namba, and Stephen P. Robertson. Clustered de novo start-loss variants in glul result in a developmental and epileptic encephalopathy via stabilization of glutamine synthetase. American journal of human genetics, 111 4:729-741, Apr 2024. URL: https://doi.org/10.1016/j.ajhg.2024.03.005, doi:10.1016/j.ajhg.2024.03.005. This article has 19 citations and is from a highest quality peer-reviewed journal.

3. (jones2024clustereddenovo pages 3-4): Amy G. Jones, Matilde Aquilino, Rory J. Tinker, Laura Duncan, Zandra Jenkins, Gemma L. Carvill, Stephanie J. DeWard, Dorothy K. Grange, MJ Hajianpour, Benjamin J. Halliday, Muriel Holder-Espinasse, Judit Horvath, Silvia Maitz, Vincenzo Nigro, Manuela Morleo, Victoria Paul, Careni Spencer, Alina I. Esterhuizen, Tilman Polster, Alice Spano, Inés Gómez-Lozano, Abhishek Kumar, Gemma Poke, John A. Phillips, Hunter R. Underhill, Gregory Gimenez, Takashi Namba, and Stephen P. Robertson. Clustered de novo start-loss variants in glul result in a developmental and epileptic encephalopathy via stabilization of glutamine synthetase. American journal of human genetics, 111 4:729-741, Apr 2024. URL: https://doi.org/10.1016/j.ajhg.2024.03.005, doi:10.1016/j.ajhg.2024.03.005. This article has 19 citations and is from a highest quality peer-reviewed journal.

4. (carbonell2025maleprobandwith pages 1-2): Elizabeth Carbonell, Sarah L. Stenton, Vijay S. Ganesh, Jialan Ma, Grace E. VanNoy, Lynn Pais, John N. Gaitanis, Melanie C. O’Leary, Heidi L. Rehm, and Anne O’Donnell-Luria. Male proband with intractable seizures and a de novo start-codon-disrupting variant in glul. Apr 2025. URL: https://doi.org/10.1016/j.xhgg.2025.100419, doi:10.1016/j.xhgg.2025.100419. This article has 3 citations and is from a peer-reviewed journal.

5. (jones2024clustereddenovo pages 5-6): Amy G. Jones, Matilde Aquilino, Rory J. Tinker, Laura Duncan, Zandra Jenkins, Gemma L. Carvill, Stephanie J. DeWard, Dorothy K. Grange, MJ Hajianpour, Benjamin J. Halliday, Muriel Holder-Espinasse, Judit Horvath, Silvia Maitz, Vincenzo Nigro, Manuela Morleo, Victoria Paul, Careni Spencer, Alina I. Esterhuizen, Tilman Polster, Alice Spano, Inés Gómez-Lozano, Abhishek Kumar, Gemma Poke, John A. Phillips, Hunter R. Underhill, Gregory Gimenez, Takashi Namba, and Stephen P. Robertson. Clustered de novo start-loss variants in glul result in a developmental and epileptic encephalopathy via stabilization of glutamine synthetase. American journal of human genetics, 111 4:729-741, Apr 2024. URL: https://doi.org/10.1016/j.ajhg.2024.03.005, doi:10.1016/j.ajhg.2024.03.005. This article has 19 citations and is from a highest quality peer-reviewed journal.

6. (carbonell2025maleprobandwith pages 3-5): Elizabeth Carbonell, Sarah L. Stenton, Vijay S. Ganesh, Jialan Ma, Grace E. VanNoy, Lynn Pais, John N. Gaitanis, Melanie C. O’Leary, Heidi L. Rehm, and Anne O’Donnell-Luria. Male proband with intractable seizures and a de novo start-codon-disrupting variant in glul. Apr 2025. URL: https://doi.org/10.1016/j.xhgg.2025.100419, doi:10.1016/j.xhgg.2025.100419. This article has 3 citations and is from a peer-reviewed journal.

7. (OpenTargets Search: Developmental and epileptic encephalopathy 116-GLUL): Open Targets Query (Developmental and epileptic encephalopathy 116-GLUL, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

8. (jones2024clustereddenovo pages 4-5): Amy G. Jones, Matilde Aquilino, Rory J. Tinker, Laura Duncan, Zandra Jenkins, Gemma L. Carvill, Stephanie J. DeWard, Dorothy K. Grange, MJ Hajianpour, Benjamin J. Halliday, Muriel Holder-Espinasse, Judit Horvath, Silvia Maitz, Vincenzo Nigro, Manuela Morleo, Victoria Paul, Careni Spencer, Alina I. Esterhuizen, Tilman Polster, Alice Spano, Inés Gómez-Lozano, Abhishek Kumar, Gemma Poke, John A. Phillips, Hunter R. Underhill, Gregory Gimenez, Takashi Namba, and Stephen P. Robertson. Clustered de novo start-loss variants in glul result in a developmental and epileptic encephalopathy via stabilization of glutamine synthetase. American journal of human genetics, 111 4:729-741, Apr 2024. URL: https://doi.org/10.1016/j.ajhg.2024.03.005, doi:10.1016/j.ajhg.2024.03.005. This article has 19 citations and is from a highest quality peer-reviewed journal.

9. (carbonell2025maleprobandwith pages 2-3): Elizabeth Carbonell, Sarah L. Stenton, Vijay S. Ganesh, Jialan Ma, Grace E. VanNoy, Lynn Pais, John N. Gaitanis, Melanie C. O’Leary, Heidi L. Rehm, and Anne O’Donnell-Luria. Male proband with intractable seizures and a de novo start-codon-disrupting variant in glul. Apr 2025. URL: https://doi.org/10.1016/j.xhgg.2025.100419, doi:10.1016/j.xhgg.2025.100419. This article has 3 citations and is from a peer-reviewed journal.

10. (carbonell2025maleprobandwith pages 5-6): Elizabeth Carbonell, Sarah L. Stenton, Vijay S. Ganesh, Jialan Ma, Grace E. VanNoy, Lynn Pais, John N. Gaitanis, Melanie C. O’Leary, Heidi L. Rehm, and Anne O’Donnell-Luria. Male proband with intractable seizures and a de novo start-codon-disrupting variant in glul. Apr 2025. URL: https://doi.org/10.1016/j.xhgg.2025.100419, doi:10.1016/j.xhgg.2025.100419. This article has 3 citations and is from a peer-reviewed journal.

11. (jones2024clustereddenovo pages 7-8): Amy G. Jones, Matilde Aquilino, Rory J. Tinker, Laura Duncan, Zandra Jenkins, Gemma L. Carvill, Stephanie J. DeWard, Dorothy K. Grange, MJ Hajianpour, Benjamin J. Halliday, Muriel Holder-Espinasse, Judit Horvath, Silvia Maitz, Vincenzo Nigro, Manuela Morleo, Victoria Paul, Careni Spencer, Alina I. Esterhuizen, Tilman Polster, Alice Spano, Inés Gómez-Lozano, Abhishek Kumar, Gemma Poke, John A. Phillips, Hunter R. Underhill, Gregory Gimenez, Takashi Namba, and Stephen P. Robertson. Clustered de novo start-loss variants in glul result in a developmental and epileptic encephalopathy via stabilization of glutamine synthetase. American journal of human genetics, 111 4:729-741, Apr 2024. URL: https://doi.org/10.1016/j.ajhg.2024.03.005, doi:10.1016/j.ajhg.2024.03.005. This article has 19 citations and is from a highest quality peer-reviewed journal.

12. (jones2024clustereddenovo pages 8-10): Amy G. Jones, Matilde Aquilino, Rory J. Tinker, Laura Duncan, Zandra Jenkins, Gemma L. Carvill, Stephanie J. DeWard, Dorothy K. Grange, MJ Hajianpour, Benjamin J. Halliday, Muriel Holder-Espinasse, Judit Horvath, Silvia Maitz, Vincenzo Nigro, Manuela Morleo, Victoria Paul, Careni Spencer, Alina I. Esterhuizen, Tilman Polster, Alice Spano, Inés Gómez-Lozano, Abhishek Kumar, Gemma Poke, John A. Phillips, Hunter R. Underhill, Gregory Gimenez, Takashi Namba, and Stephen P. Robertson. Clustered de novo start-loss variants in glul result in a developmental and epileptic encephalopathy via stabilization of glutamine synthetase. American journal of human genetics, 111 4:729-741, Apr 2024. URL: https://doi.org/10.1016/j.ajhg.2024.03.005, doi:10.1016/j.ajhg.2024.03.005. This article has 19 citations and is from a highest quality peer-reviewed journal.

13. (jones2024clustereddenovo pages 6-7): Amy G. Jones, Matilde Aquilino, Rory J. Tinker, Laura Duncan, Zandra Jenkins, Gemma L. Carvill, Stephanie J. DeWard, Dorothy K. Grange, MJ Hajianpour, Benjamin J. Halliday, Muriel Holder-Espinasse, Judit Horvath, Silvia Maitz, Vincenzo Nigro, Manuela Morleo, Victoria Paul, Careni Spencer, Alina I. Esterhuizen, Tilman Polster, Alice Spano, Inés Gómez-Lozano, Abhishek Kumar, Gemma Poke, John A. Phillips, Hunter R. Underhill, Gregory Gimenez, Takashi Namba, and Stephen P. Robertson. Clustered de novo start-loss variants in glul result in a developmental and epileptic encephalopathy via stabilization of glutamine synthetase. American journal of human genetics, 111 4:729-741, Apr 2024. URL: https://doi.org/10.1016/j.ajhg.2024.03.005, doi:10.1016/j.ajhg.2024.03.005. This article has 19 citations and is from a highest quality peer-reviewed journal.

14. (jones2024clustereddenovo pages 10-11): Amy G. Jones, Matilde Aquilino, Rory J. Tinker, Laura Duncan, Zandra Jenkins, Gemma L. Carvill, Stephanie J. DeWard, Dorothy K. Grange, MJ Hajianpour, Benjamin J. Halliday, Muriel Holder-Espinasse, Judit Horvath, Silvia Maitz, Vincenzo Nigro, Manuela Morleo, Victoria Paul, Careni Spencer, Alina I. Esterhuizen, Tilman Polster, Alice Spano, Inés Gómez-Lozano, Abhishek Kumar, Gemma Poke, John A. Phillips, Hunter R. Underhill, Gregory Gimenez, Takashi Namba, and Stephen P. Robertson. Clustered de novo start-loss variants in glul result in a developmental and epileptic encephalopathy via stabilization of glutamine synthetase. American journal of human genetics, 111 4:729-741, Apr 2024. URL: https://doi.org/10.1016/j.ajhg.2024.03.005, doi:10.1016/j.ajhg.2024.03.005. This article has 19 citations and is from a highest quality peer-reviewed journal.

15. (jones2024clustereddenovo pages 12-13): Amy G. Jones, Matilde Aquilino, Rory J. Tinker, Laura Duncan, Zandra Jenkins, Gemma L. Carvill, Stephanie J. DeWard, Dorothy K. Grange, MJ Hajianpour, Benjamin J. Halliday, Muriel Holder-Espinasse, Judit Horvath, Silvia Maitz, Vincenzo Nigro, Manuela Morleo, Victoria Paul, Careni Spencer, Alina I. Esterhuizen, Tilman Polster, Alice Spano, Inés Gómez-Lozano, Abhishek Kumar, Gemma Poke, John A. Phillips, Hunter R. Underhill, Gregory Gimenez, Takashi Namba, and Stephen P. Robertson. Clustered de novo start-loss variants in glul result in a developmental and epileptic encephalopathy via stabilization of glutamine synthetase. American journal of human genetics, 111 4:729-741, Apr 2024. URL: https://doi.org/10.1016/j.ajhg.2024.03.005, doi:10.1016/j.ajhg.2024.03.005. This article has 19 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Developmental_And_Epileptic_Encephalopathy_116-deep-research-falcon_artifacts/artifact-00.md)

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