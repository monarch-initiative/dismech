---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-18T09:23:29.737483'
end_time: '2026-08-18T09:34:13.447830'
duration_seconds: 643.71
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Noonan Syndrome 6
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 29
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 3
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Noonan_Syndrome_6-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Noonan Syndrome 6
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Noonan Syndrome 6** covering all of the
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
- **Disease Name:** Noonan Syndrome 6
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Noonan Syndrome 6** covering all of the
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


# Noonan Syndrome 6 (NRAS-associated Noonan syndrome): comprehensive disease-characteristics report

## Executive summary and evidence boundaries

**Noonan syndrome 6 (NS6)** is a very rare, congenital **Mendelian RASopathy caused by heterozygous constitutional activating variants in `NRAS`**. It is best regarded as the NRAS-defined molecular subtype of Noonan syndrome, although severe individuals may overlap clinically with cardiofaciocutaneous syndrome (CFCS) or Costello syndrome. The strongest subtype-specific evidence remains a 2017 international series of 19 newly described individuals; consequently, precise prevalence, penetrance, survival, and treatment-response estimates are unavailable. Broader Noonan-syndrome data are useful for care but must not be represented as NRAS-specific evidence. (altmuller2017genotypeandphenotype pages 1-2, altmuller2017genotypeandphenotype pages 3-4, altmuller2017genotypeandphenotype pages 4-5)

The following compact table separates subtype-specific findings from broader Noonan-syndrome evidence.

| Domain | NRAS-specific finding for Noonan syndrome 6 | General Noonan syndrome context | Key citation(s) | Caveats |
|---|---|---|---|---|
| Entity / identifiers | **Noonan syndrome 6** is the **NRAS-associated RASopathy**; Open Targets maps **MONDO:0013186** to **NRAS** with supporting literature including PubMed-linked evidence | General NS is a broader clinical syndrome with multiple RAS/MAPK genes | Open Targets MONDO_0013186→NRAS association (OpenTargets Search: Noonan syndrome 6-NRAS) | MONDO supported here; OMIM/Orphanet identifiers were not directly retrieved in tool context and should be externally verified before KB ingestion |
| Causal gene & inheritance | **NRAS** heterozygous **germline** variants cause NS6; cohort included **de novo** and **familial** cases with segregation in 4 families; variants confirmed in non-hematopoietic tissues, supporting constitutional origin | NS is usually **autosomal dominant**, with rare recessive exceptions for some non-NRAS genes | Altmüller et al., 2017, *Eur J Hum Genet*, DOI:10.1038/ejhg.2017.65 (altmuller2017genotypeandphenotype pages 3-4, altmuller2017genotypeandphenotype pages 4-5); general NS inheritance/prevalence review (perrino2024updateonpediatric pages 6-8) | Penetrance for NRAS-specific NS6 is not precisely quantified; expressivity is clearly variable |
| Strongest NRAS-specific cohort | Largest directly retrieved NRAS cohort: **19 affected individuals from 13 unrelated families** (9 males, 10 females; median age **7.1 y**, range **3 months–50 y**); majority had clinical NS (**15/19**), with some CFCS/CS overlap | Recent broader NS cohorts are much larger but are **not NRAS-specific** | Altmüller et al., 2017 (altmuller2017genotypeandphenotype pages 3-4, altmuller2017genotypeandphenotype pages 4-5) | This remains a small rare-disease cohort; some percentages exclude a complex outlier case from aggregate tables |
| Hallmark phenotype frequencies | Craniofacial/RASopathy-like features in all assessed subjects; **short/webbed neck 94%**, **ocular ptosis 82%**, **cardiac anomalies 59%**, **HCM 35%**, **septal defects 12%**, **pulmonary stenosis 6%**, **motor delay 38%**, **intellectual/learning disabilities 42%**, **prenatal abnormalities 69%** (**polyhydramnios 46%**, **nuchal edema 15%**, **fetal chylothorax/hydrops 23%**), **cryptorchidism 63% of males**, bleeding diathesis **3/15** with one confirmed von Willebrand disease | In broader NS, pulmonary valve stenosis is typically much more common than in NRAS cases; one recent general NS series found cardiac defects **71.5%**, pulmonary valve stenosis **48.3%**, short stature **43.1%** | NRAS cohort frequencies (altmuller2017genotypeandphenotype pages 4-5, altmuller2017genotypeandphenotype pages 8-9); broader NS comparison (reynolds2025updateonthe pages 9-10, reynolds2025updateonthe pages 1-2) | NRAS phenotype can overlap CFCS/Costello-like presentations, especially with Gly12 variants; frequency estimates remain imprecise because of low n |
| Molecular mechanism | Germline activating **NRAS** variants dysregulate **RAS-MAPK** and **PI3K-AKT** signaling. Functional studies showed **NRAS p.Thr58Ile** and **p.Gly12Val** increase **ERK** and **AKT phosphorylation** even without stimulation; p.Thr58Ile shifts protein toward active **GTP-bound** state, though less strongly than oncogenic p.Gly12Val | General NS is a pathway disease of **RAS/MAPK hyperactivation** across multiple genes | Altmüller et al., 2017 mechanistic assays in HEK293T cells (altmuller2017genotypeandphenotype pages 3-4, altmuller2017genotypeandphenotype pages 7-8, altmuller2017genotypeandphenotype pages 5-7) | Mechanistic evidence is strong for selected variants, but not all NS6 variants have equally detailed functional characterization |
| Diagnosis | Best-supported approach is **clinical suspicion of a RASopathy phenotype plus molecular confirmation of an NRAS germline variant**; WES identified at least one atypical/costello-like case, and constitutional status was confirmed in skin fibroblasts, nail keratinocytes, buccal cells, urine, or saliva when needed | General NS diagnosis increasingly relies on multigene **RASopathy panels** / exome sequencing; disease genes include **PTPN11, SOS1, RAF1, RIT1, LZTR1, KRAS, SOS2, NRAS, RRAS, RRAS2, MRAS, SPRED2** | NRAS-specific diagnostic examples (altmuller2017genotypeandphenotype pages 4-5, altmuller2017genotypeandphenotype pages 5-7); general NS gene list and diagnostic framing (perrino2024updateonpediatric pages 6-8) | No NRAS-specific formal clinical criteria were retrieved; differential diagnosis includes other RASopathies, especially CFCS and Costello syndrome |
| Management | No NRAS-specific management guideline was retrieved; current care is extrapolated from **general NS multidisciplinary management** with attention to cardiology, growth, neurodevelopment, feeding, lymphatic issues, and hematologic abnormalities when present | General NS data support genotype-guided care; rGH used in a subset of NS patients and is **not generally contraindicated** when clinically indicated | General NS management summaries (reynolds2025updateonthe pages 18-20, reynolds2025updateonthe pages 9-10, reynolds2025updateonthe pages 1-2) | Evidence for NS6-specific outcome modification is lacking; management remains largely supportive and organ-directed |
| Cancer surveillance | NRAS cohort reported **2 neoplastic/hematologic events**: **JMML-like myeloproliferative disorder** with **p.Gly12Asp** and an uncharacterized **brain tumor/hypothalamic lesion** with **p.Gly12Arg**; authors state more data are needed to define malignancy risk in germline oncogenic NRAS carriers | Updated NS guidance: childhood cancer risk is about **8-fold** above general population, but **routine CBC surveillance is not recommended** for otherwise healthy NS; focus on **clinical exam**, especially hepatosplenomegaly in infancy/early childhood, and family education about tumor symptoms | NRAS-specific tumor observations (altmuller2017genotypeandphenotype pages 1-2, altmuller2017genotypeandphenotype pages 7-8, altmuller2017genotypeandphenotype pages 8-9); general surveillance update 2024 (perrino2024updateonpediatric pages 8-10, perrino2024updateonpediatric pages 6-8) | Surveillance recommendations are **general NS**, not validated specifically for NRAS NS6; absolute cancer risk for NS6 remains undefined |
| Active trials / real-world implementation | No active **NRAS-only** interventional trial was retrieved | General NS trials include **NCT05308927** Norditropin registry (observational, enrolling by invitation, est. n=221), **NCT06668805** vosoritide Phase 2 (recruiting, n=30), **NCT06555237** trametinib/MEK inhibitor for RASopathy HCM Phase 2 (recruiting, n=40), plus completed somatropin studies **NCT01529840**, **NCT00452725**, and post-marketing surveillance **NCT03435627** | Trial records (NCT05308927 chunk 1, NCT06668805 chunk 1, NCT03435627 chunk 1, NCT06555237 chunk 1) | These studies enroll broader NS/RASopathy populations; applicability to NS6 is indirect unless genotype-specific subgroup analyses are reported |


*Table: This table summarizes the highest-yield disease knowledge-base facts for Noonan syndrome 6, emphasizing directly retrieved NRAS-specific evidence and clearly separating it from broader Noonan syndrome data. It is useful as a compact curation aid for identifiers, phenotype, mechanism, surveillance, and currently active clinical studies.*

**Evidence labels used below:** **Human–NRAS** = patients with constitutional NRAS variants; **Human–general NS** = mixed-genotype Noonan syndrome; **in vitro** = transfected-cell functional evidence; **registry** = ClinicalTrials.gov. Ontology identifiers proposed below should be validated against the current ontology release before production ingestion.

---

## 1. Disease information

### Definition and identifiers

* **Preferred name:** Noonan syndrome 6.
* **Synonyms:** NRAS-associated Noonan syndrome; NRAS-related Noonan syndrome; NRAS-associated RASopathy. “NRAS-associated RASopathy” is broader because a few individuals were clinically classified as CFCS- or Costello-like.
* **MONDO:** **MONDO:0013186**. Open Targets maps this disease directly to `NRAS` (Ensembl **ENSG00000213281**) with five supporting association records. (OpenTargets Search: Noonan syndrome 6-NRAS)
* **OMIM:** commonly catalogued as **Noonan syndrome 6, 613224**; the umbrella Noonan syndrome entry is **163950**. The retrieved primary article explicitly identifies general NS as OMIM 163950, but the subtype number should be independently checked against the current OMIM record before automated ingestion. (altmuller2017genotypeandphenotype pages 1-2)
* **MeSH:** **D009634, Noonan Syndrome**; there is no separate MeSH descriptor for NS6. The trial registry maps Noonan syndrome to D009634. (NCT06555237 chunk 1)
* **Orphanet:** generally represented under the umbrella Noonan-syndrome/RASopathy concept rather than a well-supported subtype-specific identifier in the retrieved evidence.
* **ICD-10/ICD-11:** subtype-specific codes were not established in the retrieved sources. NS is generally coded at syndrome level; local coding systems should not infer an NRAS-specific code.

The evidence is principally **aggregated disease-level literature assembled from individually phenotyped patients**, not an EHR-derived population dataset. The principal study included 19 individuals from 13 unrelated families, nine males and ten females, median age 7.1 years (range 3 months–50 years). Fifteen had a clinical NS diagnosis, two CFCS, and one an initially suspected Costello phenotype. (altmuller2017genotypeandphenotype pages 3-4, altmuller2017genotypeandphenotype pages 4-5)

> **Primary-paper abstract quote:** “Here we describe 19 new cases with RASopathy due to disease-causing variants in NRAS.” The authors further state that “the phenotype in our cohort was variable but well within the RASopathy spectrum.” Published online **3 May 2017**, DOI: [10.1038/ejhg.2017.65](https://doi.org/10.1038/ejhg.2017.65). (altmuller2017genotypeandphenotype pages 1-2)

---

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal factor

NS6 is caused by **germline/constitutional heterozygous activating `NRAS` variants**. Both proven **de novo** variants and familial cosegregation occur. Variants were confirmed in nonhematopoietic specimens—including fibroblasts, buccal epithelium, nail keratinocytes, urine, or saliva—to distinguish constitutional disease from somatic NRAS-mutant hematologic neoplasia. (altmuller2017genotypeandphenotype pages 3-4, altmuller2017genotypeandphenotype pages 4-5, altmuller2017genotypeandphenotype pages 5-7)

### Genetic risk factors

Reported pathogenic residues include **Gly12, Ile24, Glu37, Thr50, Thr58, and Gly60**. The 2017 cohort reported `c.34G>C p.(Gly12Arg)`, `c.35G>A p.(Gly12Asp)`, `c.34G>A p.(Gly12Ser)`, `c.35G>T p.(Gly12Val)`, `c.112-1_113dupGGA p.(Glu37dup)`, `c.173C>T p.(Thr58Ile)`, `c.71T>A p.(Ile24Asn)`, `c.149C>T p.(Thr50Ile)`, and `c.179G>A p.(Gly60Glu)`. Four Gly12 substitutions were proven de novo. (altmuller2017genotypeandphenotype pages 3-4)

Genotype may influence severity: p.Gly12Val was associated with progressive fetal hydrops and intrauterine death at 22 weeks; p.Gly12Asp occurred with a JMML-like myeloproliferative disorder; and p.Gly12Arg produced a severe neonatal Costello-like presentation with HCM, feeding/airway problems, and a hypothalamic lesion. These are single-case observations, not validated risk estimates. (altmuller2017genotypeandphenotype pages 7-8, altmuller2017genotypeandphenotype pages 4-5, altmuller2017genotypeandphenotype pages 5-7)

### Environmental and protective factors

No environmental toxin, infection, diet, lifestyle exposure, occupational factor, or protective allele has been shown to cause or prevent NS6. Parental age, sex, ethnicity, and geography are not established modifiers. Environmental care can modify **outcome**, however—for example, timely treatment of cardiac disease, feeding problems, developmental needs, and lymphatic complications—but does not remove the underlying variant.

A possible modifier was observed in one severely affected patient with a second 1.24-Mb 22q11.23 duplication plus hypoxic–ischemic injury; the authors excluded that patient from aggregate statistics because these factors likely increased neurodevelopmental severity. This is evidence for blended genetic/acquired modification, not a reproducible NRAS-specific gene–environment interaction. (altmuller2017genotypeandphenotype pages 5-7)

---

## 3. Phenotypes

### NRAS-specific frequencies

| Phenotype and type | NRAS-specific characterization | Suggested HPO term |
|---|---|---|
| RASopathy facial appearance/sign | Present in all assessed subjects; congenital, age-dependent appearance; variable | **HP:0001999** Abnormal facial shape; more granular terms include hypertelorism and ptosis |
| Short/broad or webbed neck/sign | **94%**; congenital, generally persistent | **HP:0000465** Webbed neck; **HP:0000470** Short neck |
| Ptosis/sign | **82%**; congenital/childhood | **HP:0000508** Ptosis |
| Congenital heart disease/sign | **59% (10/17)**; severity variable | **HP:0001627** Abnormal heart morphology |
| Hypertrophic cardiomyopathy/sign | **35%**; congenital or early childhood; course variable | **HP:0001639** Hypertrophic cardiomyopathy |
| Septal defect/sign | **12%** | **HP:0001631** Atrial septal defect; **HP:0001629** Ventricular septal defect |
| Pulmonary stenosis/sign | **6%**, notably lower than typical mixed-genotype NS | **HP:0001642** Pulmonic stenosis |
| Short stature/sign | **27% (4/15)** in the new cohort; a broader aggregation reported approximately 42% | **HP:0004322** Short stature |
| Motor delay/sign | **38–39%**, usually mild but variable | **HP:0001270** Motor delay |
| Intellectual/learning difficulty | **42%** in the new cohort; often mild; broader aggregation reported learning disability around 27% | **HP:0001249** Intellectual disability; **HP:0001328** Specific learning disability |
| Prenatal abnormality | **69%**; polyhydramnios **46%**, nuchal edema **15%**, fetal chylothorax/hydrops **23%** | **HP:0001561** Polyhydramnios; **HP:0001789** Hydrops fetalis; **HP:0010880** Increased nuchal translucency |
| Cryptorchidism/sign | **63% of affected males** | **HP:0000028** Cryptorchidism |
| Bleeding tendency/laboratory-clinical | **3/15** reported; only one confirmed coagulopathy (von Willebrand disease) | **HP:0001892** Abnormal bleeding; **HP:0005541** von Willebrand disease |
| Feeding difficulty/symptom | Variable; occasionally severe, requiring gastrostomy | **HP:0011968** Feeding difficulties |
| Hypotonia/sign | Variable; sometimes profound in severe/overlap cases | **HP:0001252** Hypotonia |
| Ectodermal findings/sign | Curly or sparse hair, keratosis pilaris, nevi, or café-au-lait macules in some cases | **HP:0002212** Curly hair; **HP:0001007** Hirsutism is not appropriate unless documented; use exact skin/hair terms |
| Renal/urinary anomaly/sign | Hydronephrosis, duplex system, ureteroceles in individual cases | **HP:0000126** Hydronephrosis; **HP:0000072** Hydroureter |
| Tumor/hematologic abnormality | One JMML-like disorder and one brain lesion among 19 new patients | **HP:0004376** Neoplasm; **HP:0012209** Juvenile myelomonocytic leukemia |

These figures derive from small denominators and should be stored with numerator/denominator and study provenance rather than treated as stable population frequencies. (altmuller2017genotypeandphenotype pages 8-8, altmuller2017genotypeandphenotype pages 4-5, altmuller2017genotypeandphenotype pages 8-9)

### Quality of life

No NS6-specific EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life study was retrieved. Expected burdens include cardiac follow-up, short stature, feeding and airway support, learning assistance, surgery, and anxiety regarding malignancy. These are clinically plausible impacts, but quantitative QoL values should not be assigned. The current French Norditropin registry is prospectively collecting HRQoL and educational/rehabilitation information for general NS, potentially improving future evidence. (NCT05308927 chunk 1)

---

## 4. Genetic and molecular information

* **Causal gene:** `NRAS`, NRAS proto-oncogene, GTPase; Ensembl **ENSG00000213281**. Open Targets reports a disease–target association score of 0.8066. (OpenTargets Search: Noonan syndrome 6-NRAS)
* **Variant class:** principally heterozygous **missense gain-of-function** variants; p.Glu37dup is an in-frame duplication affecting the switch-I region.
* **Origin:** constitutional germline; many cases are de novo, while familial autosomal-dominant transmission and parental mosaicism occur. One apparently unaffected father was mosaic for p.Thr58Ile. (altmuller2017genotypeandphenotype pages 3-4, altmuller2017genotypeandphenotype pages 5-7)
* **Functional consequence:** increased active GTP-bound NRAS and excessive signaling through RAF–MEK–ERK and PI3K–AKT. Gly12 substitutions impair intrinsic GTPase activity and confer resistance to GTPase-activating proteins, maintaining NRAS in its active state. (altmuller2017genotypeandphenotype pages 7-8, altmuller2017genotypeandphenotype pages 3-4)
* **Population frequency:** pathogenic constitutional variants are exceptionally rare and are expected to be absent or nearly absent from population databases. Exact contemporary gnomAD frequencies were not retrieved and must be checked variant by variant.
* **Classification:** the cited variants were treated as disease-causing in the primary study, supported by de novo occurrence/cosegregation, conservation, phenotype, hotspot location, and selected functional assays. Current ClinVar assertions and ACMG classifications should be independently retrieved for each HGVS allele; do not automatically classify every somatic oncogenic NRAS variant as a constitutional NS6 allele.
* **Somatic versus germline:** codons 12, 13, and 61 are classic somatic cancer hotspots. A variant detected only in blood during leukemia evaluation must not establish NS6; testing of nonhematopoietic tissue may be required. (altmuller2017genotypeandphenotype pages 7-8, altmuller2017genotypeandphenotype pages 4-5)
* **Chromosomal/epigenetic findings:** no recurrent NS6-causing structural chromosome abnormality or validated NRAS-specific episignature was identified. No established modifier gene exists; the 22q11.23 duplication in one patient is a candidate individual modifier, not a general association. (altmuller2017genotypeandphenotype pages 5-7)

---

## 5. Environmental information

NS6 is not infectious, toxic, nutritional, occupational, or lifestyle-induced. Smoking, alcohol, diet, exercise, pollutants, radiation, and pathogens have no demonstrated etiologic role. Standard healthy-lifestyle counseling remains appropriate for cardiovascular health but is not primary disease prevention. There is no zoonotic or person-to-person transmission.

---

## 6. Mechanism and pathophysiology

### Causal chain

1. A constitutional activating `NRAS` allele alters a highly conserved GTPase residue.
2. Impaired GTP hydrolysis/GAP responsiveness or altered switch-region kinetics increases **GTP-bound NRAS**.
3. Upstream-to-downstream signal flow is enhanced through **RAF–MEK–ERK/MAPK** and, for tested variants, **PI3K–AKT**.
4. Dysregulated proliferation, differentiation, survival, developmental patterning, and possibly metabolism affect multiple embryonic tissues.
5. Developmental consequences include craniofacial dysmorphism, cardiac and lymphatic malformation, altered growth, neurodevelopmental differences, and ectodermal findings; excessive hematopoietic signaling can produce MPD/JMML-like disease. (altmuller2017genotypeandphenotype pages 7-8, altmuller2017genotypeandphenotype pages 1-2, altmuller2017genotypeandphenotype pages 3-4)

In HEK293T transfection experiments, both NRAS-p.Thr58Ile and NRAS-p.Gly12Val increased ERK and AKT phosphorylation **without EGF stimulation**; p.Thr58Ile increased GTP-bound NRAS less strongly than p.Gly12Val. This is direct **in-vitro functional evidence**, not a patient-tissue multi-omics result. (altmuller2017genotypeandphenotype pages 3-4, altmuller2017genotypeandphenotype pages 5-7)

**Suggested GO biological processes:** GO:0000165 MAPK cascade; GO:0007265 Ras protein signal transduction; GO:0043408 regulation of MAPK cascade; GO:0008284 positive regulation of cell population proliferation; GO:0001525 angiogenesis; GO:0001944 vasculature development; GO:0007507 heart development; GO:0060429 epithelium development; GO:0007399 nervous system development. **GO cellular components:** plasma membrane, cytosol, and endomembrane-associated signaling compartments; mature NRAS is membrane-associated.

**Candidate cell types (not proven NS6-specific targets):** cardiomyocyte (**CL:0000746**), endocardial/endothelial cells, lymphatic endothelial cell (**CL:0002138**), neural progenitor, neuron (**CL:0000540**), hematopoietic stem/progenitor cell, monocyte (**CL:0000576**), chondrocyte (**CL:0000138**), and fibroblast (**CL:0000057**).

No NS6-specific patient transcriptomics, proteomics, metabolomics, lipidomics, single-cell sequencing, spatial transcriptomics, CRISPR screen, or integrated multi-omics study was retrieved. Mitochondrial/metabolic effects described for broader RASopathies should not be asserted as established NS6 mechanisms.

---

## 7. Anatomical structures affected

Primary systems are **cardiovascular**, craniofacial/connective-tissue, lymphatic, musculoskeletal/growth, nervous, ocular, skin/hair, genitourinary, and hematopoietic. Relevant structures include myocardium (**UBERON:0002349**), heart valves, cardiac septa, pulmonary artery, lymphatic vasculature (**UBERON:0004537**), brain (**UBERON:0000955**), eye (**UBERON:0000970**), kidney (**UBERON:0002113**), testis (**UBERON:0000473**), skeleton, skin (**UBERON:0002097**), and bone marrow (**UBERON:0002371**). No consistent lateralization is known. (altmuller2017genotypeandphenotype pages 4-5, altmuller2017genotypeandphenotype pages 5-7)

At the subcellular level, dysfunction begins at membrane-associated NRAS signaling and propagates through cytoplasmic kinase cascades to nuclear transcriptional programs. The disease is not primarily a lysosomal, mitochondrial, ER-storage, or ion-channel disorder.

---

## 8. Temporal development

NS6 begins **prenatally/congenitally**. Prenatal presentations range from polyhydramnios or nuchal edema to chylothorax and lethal hydrops. Cardiac defects, facial appearance, neck/chest morphology, feeding difficulty, and cryptorchidism are generally congenital; short stature and learning differences become clearer during childhood. (altmuller2017genotypeandphenotype pages 4-5)

The course is chronic and lifelong but not uniformly progressive. Some neonatal problems improve: one p.Gly12Arg child had tracheostomy removal at 20 months and caught up in motor development. HCM, lymphatic disease, and neurodevelopmental outcomes vary, while a JMML-like MPD may remain stable or potentially resolve; malignant transformation cannot be predicted from the available NRAS cohort. (altmuller2017genotypeandphenotype pages 7-8, altmuller2017genotypeandphenotype pages 5-7, perrino2024updateonpediatric pages 8-10)

Critical periods are prenatal life, infancy for severe cardiac/lymphatic disease and MPD, early childhood for developmental intervention and malignancy awareness, and transition to adult cardiac and reproductive care. No formal NS6 staging or remission classification exists.

---

## 9. Inheritance and population

* **Inheritance:** autosomal dominant.
* **Recurrence:** an affected heterozygous parent ordinarily has a 50% transmission probability per pregnancy. Most sporadic cases arise de novo, but parental mosaicism means recurrence risk is not necessarily zero after apparently de novo disease. (altmuller2017genotypeandphenotype pages 3-4, altmuller2017genotypeandphenotype pages 5-7)
* **Penetrance:** not quantified. Familial cosegregation supports high penetrance for recognizable RASopathy features, but an apparently unaffected mosaic father demonstrates dependence on variant allele fraction and tissue distribution.
* **Expressivity:** markedly variable, from relatively mild NS to severe CFCS/Costello-like disease or fetal lethality. (altmuller2017genotypeandphenotype pages 1-2, altmuller2017genotypeandphenotype pages 4-5)
* **Anticipation:** no evidence.
* **Founder effects, consanguinity, carrier frequency:** none established; consanguinity is not etiologically relevant to this dominant subtype.
* **Sex ratio:** 9 male:10 female in the principal cohort, providing no evidence of sex bias. (altmuller2017genotypeandphenotype pages 3-4)
* **NS6 epidemiology:** prevalence and incidence are unknown. It is far rarer than overall NS.
* **General NS context:** estimated prevalence is **1 in 1,000–2,500 live births**, but this must not be assigned to NS6. (perrino2024updateonpediatric pages 6-8)
* **Ethnic/geographic distribution:** cases are internationally distributed; no population enrichment has been established.

---

## 10. Diagnostics

### Recommended approach

1. **Clinical assessment:** evaluate prenatal lymphatic findings, characteristic face, webbed neck/pectus morphology, growth, cardiac disease, development, cryptorchidism, bleeding, skin/hair, vision/hearing, and renal anomalies.
2. **Baseline tests:** echocardiogram and ECG; growth and feeding assessment; developmental, ophthalmologic, and audiologic evaluation; renal ultrasound when indicated; coagulation evaluation before surgery or for bleeding history; CBC if symptomatic or if hepatosplenomegaly is present.
3. **Molecular confirmation:** a comprehensive RASopathy panel including `NRAS`, `PTPN11`, `SOS1`, `RAF1`, `RIT1`, `LZTR1`, `KRAS`, `SOS2`, `RRAS`, `RRAS2`, `MRAS`, and relevant CFCS/Costello genes. Broader exome or genome sequencing is appropriate after negative panel testing or for atypical/blended phenotypes. (altmuller2017genotypeandphenotype pages 5-7, perrino2024updateonpediatric pages 6-8)
4. **Variant-origin testing:** parental testing for segregation and recurrence counseling. If an oncogenic-hotspot NRAS variant is found in blood in the setting of MPD/leukemia, confirm constitutional status in nonhematopoietic tissue.

WES directly identified p.Gly12Arg in an HRAS-negative Costello-like child. CMA is not expected to diagnose monogenic NS6 but can detect a second diagnosis, as illustrated by the 22q11.23 duplication. Karyotype, FISH, mitochondrial sequencing, repeat-expansion testing, biopsy, and liquid biopsy are not routine NS6 tests. No validated RNA-seq, proteomic, metabolomic, or epigenomic diagnostic assay exists. (altmuller2017genotypeandphenotype pages 5-7)

### Differential diagnosis

The principal differentials are other molecular forms of NS, CFCS, Costello syndrome, Noonan syndrome with multiple lentigines, neurofibromatosis-Noonan syndrome, CBL syndrome, Turner syndrome, 22q11.2-related disorders, and isolated congenital heart/lymphatic disease. Severe feeding, ectodermal, and developmental findings may suggest CFCS; coarse/Costello-like appearance and tumor predisposition may suggest HRAS-related Costello syndrome. Molecular testing is therefore essential.

There is no population newborn screen. Prenatal diagnosis is possible by CVS/amniocentesis for a known familial variant; fetal ultrasound may detect cystic hygroma, hydrops, pleural effusions, or cardiac disease but is not diagnostic. Cascade testing, prenatal testing, and PGT-M are appropriate after identification of a familial pathogenic variant.

---

## 11. Outcome and prognosis

No reliable NS6-specific survival curve, mortality rate, or life-expectancy estimate exists. The observed age range to 50 years demonstrates survival into adulthood in some individuals, but severe fetal hydrops caused intrauterine death in one de novo p.Gly12Val case and first-day death in a familial p.Gly60Glu case. Prognosis is driven mainly by HCM/other cardiac disease, lymphatic complications, feeding/respiratory compromise, neurodevelopmental severity, and possibly MPD/malignancy. (altmuller2017genotypeandphenotype pages 3-4, altmuller2017genotypeandphenotype pages 4-5)

Functional outcomes range from normal cognition or mild learning/attention difficulty to severe disability in complicated or blended cases. Recovery of early motor and airway problems can occur, but congenital genetic susceptibility remains lifelong. No validated prognostic biomarker exists beyond preliminary variant-level observations and organ severity.

General NS data indicate an approximately **eightfold relative childhood-cancer risk**, although absolute risk remains moderate. Because most risk estimates are dominated by PTPN11 and mixed genotypes, the absolute NS6 cancer risk is unknown. (perrino2024updateonpediatric pages 8-10, perrino2024updateonpediatric pages 6-8)

---

## 12. Treatment and current implementation

There is no curative or NRAS-specific approved therapy. Management is multidisciplinary and organ-directed:

* **Cardiac:** standard pediatric/adult cardiology care, including surveillance, beta-blocker/disopyramide where appropriate for HCM, catheter/surgical treatment of obstructive lesions, and individualized arrhythmia management.
* **Growth:** nutrition/endocrine evaluation and recombinant human growth hormone (somatropin) when indicated and not otherwise contraindicated. Completed general-NS trials include Phase III **NCT01529840** (24 participants; 33 versus 66 μg/kg/day, up to ten years) and **NCT00452725** (36 participants). Postmarketing **NCT03435627** enrolled 71 patients. These studies were not NRAS-specific. (NCT01529840 chunk 1, NCT00452725 chunk 1, NCT03435627 chunk 1)
* **Development:** early physical, occupational, speech/language, educational, and behavioral intervention.
* **Feeding/lymphatic:** nutritional support, feeding therapy/tube feeding when needed, and conventional management of chylothorax/effusions.
* **Bleeding:** define the coagulation defect before surgery and use hematology-guided therapy.
* **Surgery:** correction of cardiac, genitourinary, or orthopedic abnormalities as clinically indicated.

The 2024 AACR expert update found no evidence that growth hormone increases tumor occurrence or growth and does not advise against clinically indicated GH; routine brain MRI before GH is not recommended in an asymptomatic child. (perrino2024updateonpediatric pages 8-10)

### Targeted/experimental therapies

* **Trametinib (MEK1/2 inhibitor; NCIt concept: MEK inhibitor/targeted therapy):** Phase II **MEKinRAS, NCT06555237**, began 1 August 2024 and was listed as recruiting. It randomizes approximately 40 patients aged 1 day–18 years with a molecularly confirmed RASopathy and HCM to trametinib **0.025 mg/kg/day plus standard therapy** versus standard therapy, assessing echocardiographic hypertrophy/LVOTO and cardiac biomarkers. An NRAS patient could be eligible if all criteria are met, but no NS6 subgroup outcome exists. [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT06555237). (NCT06555237 chunk 1)
* A 2025 systematic review found 16 published pediatric NS cases plus one new case treated with trametinib for severe cardiac/lymphatic disease; short-term improvement was reported in all, three deaths were considered unrelated, moderate adverse effects occurred in some, and long-term follow-up was absent. This remains off-label and experimental. DOI: [10.3389/fped.2025.1475143](https://doi.org/10.3389/fped.2025.1475143), PMID 40041314. (brouchoven2025trametinibasa pages 12-13, brouchoven2025trametinibasa pages 1-2)
* **Vosoritide:** Phase II **NCT06668805**, recruiting, randomized/triple-masked, estimated n=30, tests three doses in genetically confirmed NS with inadequate growth during/after GH. It monitors annualized growth, HCM, skeletal safety, final height, and QoL for up to 15 years. Applicability is general NS, not proven NS6. [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT06668805). (NCT06668805 chunk 1)
* **Real-world GH registry:** **NCT05308927**, estimated n=221, is collecting six-year Norditropin growth, cardiac, metabolic, safety, educational, and HRQoL data in French children. [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT05308927). (NCT05308927 chunk 1)

No gene replacement, CRISPR, ASO/siRNA, cell therapy, or immunotherapy is clinically available. Direct systemic NRAS inhibition is not an established developmental-disease strategy and could disrupt normal signaling.

---

## 13. Prevention

**Primary prevention:** there is no vaccine, environmental avoidance, diet, or medication that prevents a de novo constitutional NRAS variant. Reproductive options after molecular diagnosis include genetic counseling, parental/mosaicism testing, PGT-M, CVS/amniocentesis, and informed use of donor gametes.

**Secondary prevention:** early recognition and molecular diagnosis permit fetal/neonatal planning, baseline cardiac evaluation, developmental intervention, and cascade testing. Population screening is not justified by current prevalence and evidence.

**Tertiary prevention:** regular multisystem follow-up aims to prevent cardiac decompensation, growth/nutritional morbidity, developmental disability, surgical bleeding, hearing/vision impairment, and delayed recognition of MPD or tumors.

The 2024 AACR update recommends **clinical examination—particularly for hepatosplenomegaly in infancy and early childhood—rather than routine CBCs in otherwise healthy NS children**. Routine radiologic/laboratory screening for solid tumors is not justified by absolute risk; families may be educated about rhabdomyosarcoma, glioma, and neuroblastoma symptoms. Any suspected MPD warrants pediatric hematology/oncology follow-up. These are general NS recommendations, not validated specifically in NS6. (perrino2024updateonpediatric pages 8-10)

---

## 14. Other species and natural disease

`NRAS` orthologues are evolutionarily conserved across vertebrates and many experimental species, but no well-established **naturally occurring veterinary syndrome equivalent to human NS6** was identified. There is no zoonotic potential or cross-species transmission because this is a constitutional genetic disorder. Breed-specific disease, VBO annotation, and animal carrier frequency are unavailable.

---

## 15. Model organisms and experimental systems

The directly retrieved NS6 functional model was **HEK293T cells transiently expressing FLAG-tagged wild-type or mutant NRAS**. ERK1/2 and AKT phosphorylation, together with GTP-bound NRAS assays, demonstrated variant gain of function. This model is useful for biochemical pathogenicity testing but cannot reproduce embryonic development, tissue interactions, dosage throughout life, cardiac architecture, lymphatic flow, cognition, or tumor risk. (altmuller2017genotypeandphenotype pages 3-4, altmuller2017genotypeandphenotype pages 5-7)

No validated NS6-specific knock-in mouse, rat, zebrafish, Drosophila, organoid, or patient-derived iPSC model was identified in the retrieved literature. General RASopathy animal and lymphatic-organoid work supports MEK inhibition conceptually, but extrapolation to a particular NRAS allele requires caution. A priority model would be a conditional heterozygous knock-in reproducing a viable human allele such as p.Thr58Ile, with cardiac, lymphatic, growth, neurodevelopmental, and hematopoietic phenotyping.

---

## Current expert interpretation and critical knowledge gaps

The evidence strongly establishes NS6 as a constitutional **gain-of-function RAS/MAPK disorder**, but disease curation should preserve three distinctions: (1) **NRAS-specific observations versus mixed-genotype NS data**, (2) constitutional variants versus blood-restricted somatic cancer mutations, and (3) individual-case genotype associations versus reproducible prognostic rules. The most urgent research needs are a prospective international NRAS registry, allele-resolved natural history, gnomAD/ClinVar harmonization, penetrance and parental-mosaicism studies, systematic cancer-risk estimation, patient-reported outcomes, and NRAS-specific developmental models. (altmuller2017genotypeandphenotype pages 7-8, altmuller2017genotypeandphenotype pages 8-9, perrino2024updateonpediatric pages 10-11)

### Core references

1. Altmüller F, et al. **Genotype and phenotype spectrum of NRAS germline variants.** *European Journal of Human Genetics.* Published online 3 May 2017;25:823–831. DOI: [10.1038/ejhg.2017.65](https://doi.org/10.1038/ejhg.2017.65). Primary human cohort plus in-vitro functional evidence. (altmuller2017genotypeandphenotype pages 1-2, altmuller2017genotypeandphenotype pages 3-4)
2. Perrino MR, et al. **Update on Pediatric Cancer Surveillance Recommendations…** *Clinical Cancer Research.* Published August 2024;30:4834–4843. DOI: [10.1158/1078-0432.CCR-24-1611](https://doi.org/10.1158/1078-0432.CCR-24-1611). Current expert surveillance guidance; general NS rather than NRAS-specific. (perrino2024updateonpediatric pages 6-8, perrino2024updateonpediatric pages 8-10)
3. Open Targets. **MONDO:0013186—NRAS association.** Disease–target evidence includes PMID 19966803 and PMID 23875798. (OpenTargets Search: Noonan syndrome 6-NRAS)
4. De Brouchoven I, et al. **Trametinib as a targeted treatment in cardiac and lymphatic presentations of Noonan syndrome.** *Frontiers in Pediatrics.* 18 February 2025;13:1475143. DOI: [10.3389/fped.2025.1475143](https://doi.org/10.3389/fped.2025.1475143); PMID 40041314. (brouchoven2025trametinibasa pages 1-2, NCT06555237 chunk 1)

References

1. (altmuller2017genotypeandphenotype pages 1-2): Franziska Altmüller, Christina Lissewski, Debora Bertola, Elisabetta Flex, Zornitza Stark, Stephanie Spranger, Gareth Baynam, Michelle Buscarilli, Sarah Dyack, Jane Gillis, Helger G Yntema, Francesca Pantaleoni, Rosa LE van Loon, Sara MacKay, Kym Mina, Ina Schanze, Tiong Yang Tan, Maie Walsh, Susan M White, Marena R Niewisch, Sixto García-Miñaúr, Diego Plaza, Mohammad Reza Ahmadian, Hélène Cavé, Marco Tartaglia, and Martin Zenker. Genotype and phenotype spectrum of nras germline variants. European Journal of Human Genetics, 25:823-831, May 2017. URL: https://doi.org/10.1038/ejhg.2017.65, doi:10.1038/ejhg.2017.65. This article has 65 citations and is from a domain leading peer-reviewed journal.

2. (altmuller2017genotypeandphenotype pages 3-4): Franziska Altmüller, Christina Lissewski, Debora Bertola, Elisabetta Flex, Zornitza Stark, Stephanie Spranger, Gareth Baynam, Michelle Buscarilli, Sarah Dyack, Jane Gillis, Helger G Yntema, Francesca Pantaleoni, Rosa LE van Loon, Sara MacKay, Kym Mina, Ina Schanze, Tiong Yang Tan, Maie Walsh, Susan M White, Marena R Niewisch, Sixto García-Miñaúr, Diego Plaza, Mohammad Reza Ahmadian, Hélène Cavé, Marco Tartaglia, and Martin Zenker. Genotype and phenotype spectrum of nras germline variants. European Journal of Human Genetics, 25:823-831, May 2017. URL: https://doi.org/10.1038/ejhg.2017.65, doi:10.1038/ejhg.2017.65. This article has 65 citations and is from a domain leading peer-reviewed journal.

3. (altmuller2017genotypeandphenotype pages 4-5): Franziska Altmüller, Christina Lissewski, Debora Bertola, Elisabetta Flex, Zornitza Stark, Stephanie Spranger, Gareth Baynam, Michelle Buscarilli, Sarah Dyack, Jane Gillis, Helger G Yntema, Francesca Pantaleoni, Rosa LE van Loon, Sara MacKay, Kym Mina, Ina Schanze, Tiong Yang Tan, Maie Walsh, Susan M White, Marena R Niewisch, Sixto García-Miñaúr, Diego Plaza, Mohammad Reza Ahmadian, Hélène Cavé, Marco Tartaglia, and Martin Zenker. Genotype and phenotype spectrum of nras germline variants. European Journal of Human Genetics, 25:823-831, May 2017. URL: https://doi.org/10.1038/ejhg.2017.65, doi:10.1038/ejhg.2017.65. This article has 65 citations and is from a domain leading peer-reviewed journal.

4. (OpenTargets Search: Noonan syndrome 6-NRAS): Open Targets Query (Noonan syndrome 6-NRAS, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (perrino2024updateonpediatric pages 6-8): Melissa R. Perrino, Anirban Das, Sarah R. Scollon, Sarah G. Mitchell, Mary-Louise C. Greer, Marielle E. Yohe, Jordan R. Hansford, Jennifer M. Kalish, Kris Ann P. Schultz, Suzanne P. MacFarland, Wendy K. Kohlmann, Philip J. Lupo, Kara N. Maxwell, Stefan M. Pfister, Rosanna Weksberg, Orli Michaeli, Marjolijn C.J. Jongmans, Gail E. Tomlinson, Jack Brzezinski, Uri Tabori, Gina M. Ney, Karen W. Gripp, Andrea M. Gross, Brigitte C. Widemann, Douglas R. Stewart, Emma R. Woodward, and Christian P. Kratz. Update on pediatric cancer surveillance recommendations for patients with neurofibromatosis type 1, noonan syndrome, cbl syndrome, costello syndrome, and related rasopathies. Clinical Cancer Research, 30:4834-4843, Aug 2024. URL: https://doi.org/10.1158/1078-0432.ccr-24-1611, doi:10.1158/1078-0432.ccr-24-1611. This article has 60 citations and is from a highest quality peer-reviewed journal.

6. (altmuller2017genotypeandphenotype pages 8-9): Franziska Altmüller, Christina Lissewski, Debora Bertola, Elisabetta Flex, Zornitza Stark, Stephanie Spranger, Gareth Baynam, Michelle Buscarilli, Sarah Dyack, Jane Gillis, Helger G Yntema, Francesca Pantaleoni, Rosa LE van Loon, Sara MacKay, Kym Mina, Ina Schanze, Tiong Yang Tan, Maie Walsh, Susan M White, Marena R Niewisch, Sixto García-Miñaúr, Diego Plaza, Mohammad Reza Ahmadian, Hélène Cavé, Marco Tartaglia, and Martin Zenker. Genotype and phenotype spectrum of nras germline variants. European Journal of Human Genetics, 25:823-831, May 2017. URL: https://doi.org/10.1038/ejhg.2017.65, doi:10.1038/ejhg.2017.65. This article has 65 citations and is from a domain leading peer-reviewed journal.

7. (reynolds2025updateonthe pages 9-10): Giuseppe Reynolds, Andrea Gazzin, Diana Carli, Stefania Massuras, Simona Cardaropoli, Maria Luca, Beatrice Defilippi, Marco Tartaglia, Giovanni Battista Ferrero, and Alessandro Mussa. Update on the clinical and molecular characterization of noonan syndrome and other rasopathies: a retrospective study and systematic review. International Journal of Molecular Sciences, 26:3515, Apr 2025. URL: https://doi.org/10.3390/ijms26083515, doi:10.3390/ijms26083515. This article has 31 citations.

8. (reynolds2025updateonthe pages 1-2): Giuseppe Reynolds, Andrea Gazzin, Diana Carli, Stefania Massuras, Simona Cardaropoli, Maria Luca, Beatrice Defilippi, Marco Tartaglia, Giovanni Battista Ferrero, and Alessandro Mussa. Update on the clinical and molecular characterization of noonan syndrome and other rasopathies: a retrospective study and systematic review. International Journal of Molecular Sciences, 26:3515, Apr 2025. URL: https://doi.org/10.3390/ijms26083515, doi:10.3390/ijms26083515. This article has 31 citations.

9. (altmuller2017genotypeandphenotype pages 7-8): Franziska Altmüller, Christina Lissewski, Debora Bertola, Elisabetta Flex, Zornitza Stark, Stephanie Spranger, Gareth Baynam, Michelle Buscarilli, Sarah Dyack, Jane Gillis, Helger G Yntema, Francesca Pantaleoni, Rosa LE van Loon, Sara MacKay, Kym Mina, Ina Schanze, Tiong Yang Tan, Maie Walsh, Susan M White, Marena R Niewisch, Sixto García-Miñaúr, Diego Plaza, Mohammad Reza Ahmadian, Hélène Cavé, Marco Tartaglia, and Martin Zenker. Genotype and phenotype spectrum of nras germline variants. European Journal of Human Genetics, 25:823-831, May 2017. URL: https://doi.org/10.1038/ejhg.2017.65, doi:10.1038/ejhg.2017.65. This article has 65 citations and is from a domain leading peer-reviewed journal.

10. (altmuller2017genotypeandphenotype pages 5-7): Franziska Altmüller, Christina Lissewski, Debora Bertola, Elisabetta Flex, Zornitza Stark, Stephanie Spranger, Gareth Baynam, Michelle Buscarilli, Sarah Dyack, Jane Gillis, Helger G Yntema, Francesca Pantaleoni, Rosa LE van Loon, Sara MacKay, Kym Mina, Ina Schanze, Tiong Yang Tan, Maie Walsh, Susan M White, Marena R Niewisch, Sixto García-Miñaúr, Diego Plaza, Mohammad Reza Ahmadian, Hélène Cavé, Marco Tartaglia, and Martin Zenker. Genotype and phenotype spectrum of nras germline variants. European Journal of Human Genetics, 25:823-831, May 2017. URL: https://doi.org/10.1038/ejhg.2017.65, doi:10.1038/ejhg.2017.65. This article has 65 citations and is from a domain leading peer-reviewed journal.

11. (reynolds2025updateonthe pages 18-20): Giuseppe Reynolds, Andrea Gazzin, Diana Carli, Stefania Massuras, Simona Cardaropoli, Maria Luca, Beatrice Defilippi, Marco Tartaglia, Giovanni Battista Ferrero, and Alessandro Mussa. Update on the clinical and molecular characterization of noonan syndrome and other rasopathies: a retrospective study and systematic review. International Journal of Molecular Sciences, 26:3515, Apr 2025. URL: https://doi.org/10.3390/ijms26083515, doi:10.3390/ijms26083515. This article has 31 citations.

12. (perrino2024updateonpediatric pages 8-10): Melissa R. Perrino, Anirban Das, Sarah R. Scollon, Sarah G. Mitchell, Mary-Louise C. Greer, Marielle E. Yohe, Jordan R. Hansford, Jennifer M. Kalish, Kris Ann P. Schultz, Suzanne P. MacFarland, Wendy K. Kohlmann, Philip J. Lupo, Kara N. Maxwell, Stefan M. Pfister, Rosanna Weksberg, Orli Michaeli, Marjolijn C.J. Jongmans, Gail E. Tomlinson, Jack Brzezinski, Uri Tabori, Gina M. Ney, Karen W. Gripp, Andrea M. Gross, Brigitte C. Widemann, Douglas R. Stewart, Emma R. Woodward, and Christian P. Kratz. Update on pediatric cancer surveillance recommendations for patients with neurofibromatosis type 1, noonan syndrome, cbl syndrome, costello syndrome, and related rasopathies. Clinical Cancer Research, 30:4834-4843, Aug 2024. URL: https://doi.org/10.1158/1078-0432.ccr-24-1611, doi:10.1158/1078-0432.ccr-24-1611. This article has 60 citations and is from a highest quality peer-reviewed journal.

13. (NCT05308927 chunk 1):  French Registry of Children Treated With Norditropin® for Short Stature Associated With Noonan Syndrome. Novo Nordisk A/S. 2022. ClinicalTrials.gov Identifier: NCT05308927

14. (NCT06668805 chunk 1):  A Study of Vosoritide in Children With Noonan Syndrome With Inadequate Growth During or After Human Growth Hormone Treatment. BioMarin Pharmaceutical. 2024. ClinicalTrials.gov Identifier: NCT06668805

15. (NCT03435627 chunk 1):  Post Marketing Surveillance on Long-term Use With Norditropin® (Short Stature Due to Noonan Syndrome). Novo Nordisk A/S. 2018. ClinicalTrials.gov Identifier: NCT03435627

16. (NCT06555237 chunk 1):  MEK Inhibitors for the Treatment of Hypertrophic Cardiomyopathy in Patients With RASopathies. Medical University of Warsaw. 2024. ClinicalTrials.gov Identifier: NCT06555237

17. (altmuller2017genotypeandphenotype pages 8-8): Franziska Altmüller, Christina Lissewski, Debora Bertola, Elisabetta Flex, Zornitza Stark, Stephanie Spranger, Gareth Baynam, Michelle Buscarilli, Sarah Dyack, Jane Gillis, Helger G Yntema, Francesca Pantaleoni, Rosa LE van Loon, Sara MacKay, Kym Mina, Ina Schanze, Tiong Yang Tan, Maie Walsh, Susan M White, Marena R Niewisch, Sixto García-Miñaúr, Diego Plaza, Mohammad Reza Ahmadian, Hélène Cavé, Marco Tartaglia, and Martin Zenker. Genotype and phenotype spectrum of nras germline variants. European Journal of Human Genetics, 25:823-831, May 2017. URL: https://doi.org/10.1038/ejhg.2017.65, doi:10.1038/ejhg.2017.65. This article has 65 citations and is from a domain leading peer-reviewed journal.

18. (NCT01529840 chunk 1):  Somatropin Effect on Linear Growth and Final Height in Subjects With Noonan Syndrome. Novo Nordisk A/S. 1990. ClinicalTrials.gov Identifier: NCT01529840

19. (NCT00452725 chunk 1):  Effect of MAXOMAT ® on the Growth of Small Children to NOONAN's Syndrome. Sanofi. 1997. ClinicalTrials.gov Identifier: NCT00452725

20. (brouchoven2025trametinibasa pages 12-13): Isabel De Brouchoven, Juan Lorand, Léon Bofferding, Arthur Sorlin, An Van Damme, and Olivier Danhaive. Trametinib as a targeted treatment in cardiac and lymphatic presentations of noonan syndrome. Frontiers in Pediatrics, Feb 2025. URL: https://doi.org/10.3389/fped.2025.1475143, doi:10.3389/fped.2025.1475143. This article has 10 citations.

21. (brouchoven2025trametinibasa pages 1-2): Isabel De Brouchoven, Juan Lorand, Léon Bofferding, Arthur Sorlin, An Van Damme, and Olivier Danhaive. Trametinib as a targeted treatment in cardiac and lymphatic presentations of noonan syndrome. Frontiers in Pediatrics, Feb 2025. URL: https://doi.org/10.3389/fped.2025.1475143, doi:10.3389/fped.2025.1475143. This article has 10 citations.

22. (perrino2024updateonpediatric pages 10-11): Melissa R. Perrino, Anirban Das, Sarah R. Scollon, Sarah G. Mitchell, Mary-Louise C. Greer, Marielle E. Yohe, Jordan R. Hansford, Jennifer M. Kalish, Kris Ann P. Schultz, Suzanne P. MacFarland, Wendy K. Kohlmann, Philip J. Lupo, Kara N. Maxwell, Stefan M. Pfister, Rosanna Weksberg, Orli Michaeli, Marjolijn C.J. Jongmans, Gail E. Tomlinson, Jack Brzezinski, Uri Tabori, Gina M. Ney, Karen W. Gripp, Andrea M. Gross, Brigitte C. Widemann, Douglas R. Stewart, Emma R. Woodward, and Christian P. Kratz. Update on pediatric cancer surveillance recommendations for patients with neurofibromatosis type 1, noonan syndrome, cbl syndrome, costello syndrome, and related rasopathies. Clinical Cancer Research, 30:4834-4843, Aug 2024. URL: https://doi.org/10.1158/1078-0432.ccr-24-1611, doi:10.1158/1078-0432.ccr-24-1611. This article has 60 citations and is from a highest quality peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Noonan_Syndrome_6-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 3 |
| Off topic | 0 |

All extracted references resolved successfully.