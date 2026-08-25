---
provider: falcon
model: Edison Scientific Literature
cached: true
start_time: '2026-08-17T21:36:01.098906'
end_time: '2026-08-17T21:36:01.118017'
duration_seconds: 0.02
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Left Ventricular Noncompaction 8
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 23
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 8
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Left_Ventricular_Noncompaction_8-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Left Ventricular Noncompaction 8
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Left Ventricular Noncompaction 8** covering all of the
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
- **Disease Name:** Left Ventricular Noncompaction 8
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Left Ventricular Noncompaction 8** covering all of the
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


# Left Ventricular Noncompaction 8 (LVNC8): comprehensive disease-characteristics report

**Scope and evidence note.** LVNC8 is an exceptionally rare, genetically defined subtype of left-ventricular noncompaction associated with **PRDM16**. Most clinical evidence consists of individual families and aggregated case series; accordingly, many epidemiologic and management statements below derive from broader LVNC/noncompaction-cardiomyopathy literature and are explicitly labeled as such. This is not an individual-patient/EHR summary.

| Domain | LVNC8-specific finding | Broader LVNC context | Key identifiers / evidence |
|---|---|---|---|
| Identity | Left Ventricular Noncompaction 8 (LVNC8) is the PRDM16-associated monogenic LVNC subtype; disease-level evidence is aggregated from published case series/reviews rather than EHR-derived individual databases. | Broad LVNC / left ventricular noncompaction is recognized as a phenotype/cardiomyopathy spectrum with controversy over whether it is a distinct cardiomyopathy or a morphologic trait shared across disorders. | Broad LVNC MONDO:0018901; PRDM16-associated disease-target evidence in Open Targets (OpenTargets Search: left ventricular noncompaction-PRDM16, wu2022prdm16isa pages 13-14) |
| Causal gene | **PRDM16** (PR/SET domain 16) is the established causal gene for LVNC8; truncating variants are the main LVNC-associated class. | Other LVNC genes exist, but they define other subtypes or broader nonspecific LVNC phenotypes. | PRDM16 / ENSG00000142611; original human causal paper cited via review as Arndt et al. 2013, PMID 23768516 (wu2022prdm16isa pages 13-14) |
| Inheritance | Predominantly **autosomal dominant** with de novo and familial cases reported; penetrance appears incomplete/variable but subtype-specific estimates are not established. | Familial screening is recommended in LVNC more generally when cardiomyopathy is suspected. | Multiple inherited and de novo truncating variants summarized in 2023 review (walsh2023thetroublewith pages 10-11) |
| Strongest human genetic statistic | In a cohort enrichment analysis, PRDM16 variants were found in **1.35% (6/444)** of LVNC cases versus **0.006% (7/120,147)** in gnomAD, **p = 4.0E-12**. | Supports pathogenic enrichment beyond background variation and strengthens subtype validity. | Walsh 2023, DOI: 10.1007/s12265-023-10459-6 (walsh2023thetroublewith pages 10-11) |
| Core phenotype | LVNC8 presents with excessive LV trabeculation/noncompaction, ventricular dysfunction, and can include dilation, heart failure, conduction disease, arrhythmia, or sudden death; severity ranges from fetal/childhood onset to adult disease. | Broader LVNC may occur isolated or alongside DCM/HCM/RCM/ARVC phenotypes and congenital heart disease. | Human variant summaries across countries/populations (walsh2023thetroublewith pages 10-11) |
| Imaging criteria | No PRDM16-specific imaging criteria exist; LVNC8 uses standard LVNC imaging thresholds. | Echo criterion commonly cited: end-systolic noncompacted/compacted ratio **>2.0**; CMR criterion commonly cited: ratio **>2.3**; diagnostic overcall is a known concern. | Arbustini 2014 JACC DOI: 10.1016/j.jacc.2014.08.030 (arbustini2014leftventricularnoncompaction pages 7-8); Walsh 2023 (walsh2023thetroublewith pages 1-2) |
| Major complications | Reported LVNC8 complications include severe biventricular heart failure, ventricular enlargement, conduction abnormalities, arrhythmias, and sudden cardiac death. | In symptomatic broader LVNC cohorts, ventricular tachyarrhythmias up to **47%** and sudden cardiac death **13–18%** have been reported; thromboembolism risk motivates anticoagulation consideration in selected patients. | PRDM16-specific case summaries (walsh2023thetroublewith pages 10-11); broader LVNC management review (arbustini2014leftventricularnoncompaction pages 8-9, arbustini2014leftventricularnoncompaction pages 9-10) |
| Key mechanism | PRDM16 is a compact-myocardium-enriched transcription factor required to maintain **left-ventricular compact cardiomyocyte identity**; loss causes shift toward trabecular, neuronal-like, atrial, and conduction-system programs, with downstream dysfunction. | LVNC pathogenesis broadly implicates disturbed trabeculation/compaction, developmental signaling, and myocardial maturation failure. | Wu 2022 Circulation DOI: 10.1161/CIRCULATIONAHA.121.056666 (wu2022prdm16isa pages 1-3, wu2022prdm16isa pages 9-11); Van Wauwe 2024 DOI: 10.26508/lsa.202402719 (wauwe2024prdm16determinesspecification pages 1-2) |
| Latest 2023–2024 developments | 2023 multi-omics mouse work showed early **metabolic dysregulation**, oxidative stress, sex-specific substrate-use defects, and novel regulators **Pyroxd2/Pbxip1** in PRDM16-associated cardiomyopathy; 2024 single-cell RNA+ATAC work showed PRDM16 suppresses alternative atrial/conduction fates and prevents distal ventricular conduction system hyperplasia. | 2024 cardiomyopathy guidance/commentary continues to frame LV trabeculation as dynamic and emphasizes genetics plus deep phenotyping for interpretation. | Kühnisch 2023 DOI: 10.1093/cvr/cvad154 (kuhnisch2023prdm16mutationdetermines pages 1-2, kuhnisch2023prdm16mutationdetermines pages 4-7, kuhnisch2023prdm16mutationdetermines pages 10-11); Van Wauwe 2024 (wauwe2024prdm16determinesspecification pages 1-2); ESC commentary 2024 DOI: 10.1093/eurheartjsupp/suae002 (context from search, not directly cited here) |
| Management | No PRDM16-targeted therapy exists; management is **phenotype-directed**: standard heart-failure therapy, arrhythmia surveillance, ICD when indicated by conventional risk factors, anticoagulation in selected patients, and family/genetic screening. | Asymptomatic patients with normal LV size/function are generally monitored; symptomatic patients are treated per HF/arrhythmia guidelines; family echocardiographic screening is recommended in familial disease. | Arbustini 2014 (arbustini2014leftventricularnoncompaction pages 8-9, arbustini2014leftventricularnoncompaction pages 9-10) |
| Trials / real-world studies | No PRDM16-specific interventional trial was identified. | Active LVNC observational studies include **NCT06024759** (risk registry, recruiting, n=500), **NCT04265040** (TORCH-Plus registry, recruiting, n=2040), **NCT06607471** (multicenter registry, recruiting), plus prior imaging/risk studies **NCT01470014**, **NCT03572569**, **NCT02568072**. | ClinicalTrials.gov records (NCT06024759 chunk 1, NCT04265040 chunk 1, NCT06607471 chunk 23, NCT01470014 chunk 1, NCT03572569 chunk 1, NCT02568072 chunk 1) |
| Major evidence gaps | Exact LVNC8 OMIM/MONDO subtype identifier, prevalence/incidence, penetrance, carrier frequency, genotype-specific prognosis, pregnancy/exercise guidance, and prospective treatment-response data are not well established. Most evidence is from small families, case series, reviews, and model systems. | Broader LVNC itself remains diagnostically controversial because hypertrabeculation can be physiologic (e.g., athletes, pregnancy) and may not correlate with prognosis in isolation. | Evidence-gap summary supported by genetics review and broader LVNC controversy literature (walsh2023thetroublewith pages 10-11, walsh2023thetroublewith pages 1-2) |


*Table: This compact table summarizes subtype-specific facts for PRDM16-associated Left Ventricular Noncompaction 8 and separates them from broader LVNC evidence. It highlights what is established, what is extrapolated from general LVNC literature, and where important evidence gaps remain.*

## 1. Disease information

### Definition
LVNC8 is a genetic cardiomyopathy characterized by excessive ventricular trabeculation, deep intertrabecular recesses, and a relatively thin compact myocardial layer, caused principally by pathogenic heterozygous variants affecting **PRDM16**. The phenotype can coexist with ventricular dilation or systolic dysfunction and may manifest as heart failure, conduction disease, ventricular arrhythmia, thromboembolism, or sudden cardiac death.

A crucial current distinction is between **pathologic noncompaction cardiomyopathy** and **isolated hypertrabeculation**. Sensitive cardiac MRI may identify marked trabeculation in up to 15% of healthy people; reversible increases also occur during pregnancy and intensive athletic training. Trabeculation burden alone does not reliably correlate with ventricular dysfunction or prognosis. Diagnosis should therefore integrate morphology with ventricular function, ECG findings, fibrosis, symptoms, family history, and genotype (Walsh, published November 2023; DOI: https://doi.org/10.1007/s12265-023-10459-6). (walsh2023thetroublewith pages 1-2)

### Identifiers and nomenclature

- **Preferred name:** Left ventricular noncompaction 8; LVNC8.
- **Causal-gene name:** PRDM16-associated cardiomyopathy/noncompaction cardiomyopathy.
- **Broad disease MONDO:** **MONDO:0018901**, left ventricular noncompaction. Open Targets associates PRDM16/ENSG00000142611 with this entity. A confidently verified subtype-specific MONDO identifier was not recovered. (OpenTargets Search: left ventricular noncompaction-PRDM16)
- **OMIM:** PRDM16 is **MIM 605557**. The original causal report is Arndt et al., 2013, PMID **23768516**. A subtype-specific OMIM number should be verified directly in the current OMIM release before database deposition because it was not independently recovered in the retrieved evidence. (micolonghi2024unveilingthespectrum pages 18-19, wu2022prdm16isa pages 13-14)
- **HPO disease-phenotype concept:** Left ventricular noncompaction cardiomyopathy, **HP:0011664**. (OpenTargets Search: left ventricular noncompaction-PRDM16)
- **ICD:** No dedicated ICD-10-CM code uniquely identifies LVNC8; it is generally coded under cardiomyopathy (e.g., I42.8/I42.9 depending jurisdiction and documentation). ICD-11 likewise does not provide a PRDM16-specific code in the retrieved material.
- **Synonyms:** noncompaction cardiomyopathy, left-ventricular hypertrabeculation/noncompaction, spongy myocardium, PRDM16-related cardiomyopathy. “Isolated LVNC” should be used cautiously because associated DCM, congenital, neuromuscular, and arrhythmic phenotypes are common.

## 2. Etiology, risk, and protective factors

### Primary causal factor
The principal cause is a **germline heterozygous pathogenic PRDM16 variant**, particularly a nonsense or frameshift variant producing protein truncation or loss of function. Contemporary review evidence indicates that truncating variants are preferentially associated with LVNC, whereas missense variants have more often been reported with dilated cardiomyopathy. PRDM16 is predicted to be highly loss-of-function intolerant. (micolonghi2024unveilingthespectrum pages 18-19)

The strongest reported enrichment analysis found PRDM16 variants in **6/444 LVNC cases (1.35%)**, compared with **7/120,147 gnomAD individuals (0.006%)**, *p*=4.0×10⁻¹². Variants occurred in geographically diverse families and included de novo and inherited alleles, supporting a genuine but rare disease association rather than a founder effect. (walsh2023thetroublewith pages 10-11)

### Risk factors and modifiers

- **Established:** a pathogenic PRDM16 allele; a family history of cardiomyopathy, congenital heart disease, arrhythmia, or sudden death.
- **Possible genetic modifiers:** broader cardiomyopathy-variant burden, and interaction with developmental regulators including **TBX5, HAND1, TBX20**, and **SKI**. Modifier effects are mechanistically plausible but not quantitatively validated for human LVNC8. PRDM16 and SKI reduction interacted to lower cardiac output in zebrafish. (theisen2024characterisationofthe pages 17-21)
- **Age/sex:** onset ranges from fetal life through adulthood. Human sex-specific penetrance is unresolved. A 1p36-deletion cardiomyopathy series included 16 females among 18 individuals, while heterozygous mouse disease was more severe in females; neither observation establishes a human female risk ratio. (theisen2024characterisationofthe pages 17-21, kuhnisch2023prdm16mutationdetermines pages 1-2)
- **Environmental/lifestyle risks:** no toxin, infection, diet, smoking, alcohol, or occupational exposure is established as a cause of LVNC8. Pregnancy and endurance training can increase trabeculation and thereby mimic or unmask the morphology, but are not demonstrated causes of PRDM16 disease. (walsh2023thetroublewith pages 1-2, NCT02568072 chunk 1)
- **Protective factors:** no validated genetic or environmental protective factor is known. Early detection, guideline-directed therapy, and avoidance of individually unsafe exertion prevent complications rather than prevent the congenital genetic substrate.

## 3. Phenotypes

Frequencies specific to LVNC8 are unavailable because published patients are too few and ascertainment is nonuniform.

| Phenotype | Type, onset, course, impact | Suggested HPO term |
|---|---|---|
| Left-ventricular noncompaction/hypertrabeculation | Imaging sign; congenital substrate, detectable fetally or later; may remain stable or accompany progressive dysfunction | HP:0011664 |
| Dilated or hypoplastic LV; reduced ejection fraction | Structural/functional sign; severity variable from asymptomatic to biventricular failure | Dilated cardiomyopathy HP:0001644; decreased LV ejection fraction HP:0012664 |
| Heart failure | Symptom/sign; pediatric or adult onset; potentially progressive and transplant-requiring | HP:0001635 |
| Exercise intolerance, dyspnea, fatigue | Symptoms secondary to low output/congestion; impair mobility, school/work, and quality of life | HP:0002875; HP:0002094; HP:0012378 |
| Ventricular arrhythmia/palpitations | Episodic; may cause syncope, ICD therapy, or sudden death | HP:0004308; HP:0001962 |
| Conduction abnormality | ECG sign; mechanistically consistent with altered ventricular-conduction-cell specification | HP:0001678 |
| Sudden cardiac death | Severe outcome, reported in PRDM16 families | HP:0001645 |
| Intracardiac thrombosis/systemic embolism | Complication, especially with dysfunction, atrial fibrillation, or prior thrombus | HP:0031292; HP:0002204 |
| Myocardial fibrosis | CMR/pathologic sign; not universal | HP:0031325 |

PRDM16 case summaries include fetal-to-adult presentation, severe biventricular failure in a 33-year-old man, onset at 12 years in a female, ventricular/atrial enlargement, fibrosis, and sudden death. (walsh2023thetroublewith pages 10-11) Broader historical symptomatic LVNC cohorts reported ventricular tachyarrhythmias in as many as **47%** and sudden death in **13–18%**, but these figures must not be treated as LVNC8-specific. (arbustini2014leftventricularnoncompaction pages 8-9)

## 4. Genetic and molecular information

### Gene and variants

- **Gene:** **PRDM16**, PR/SET domain 16; Ensembl **ENSG00000142611**; protein is a zinc-finger transcriptional/epigenetic regulator. (OpenTargets Search: left ventricular noncompaction-PRDM16, micolonghi2024unveilingthespectrum pages 18-19)
- **Variant spectrum:** principally germline nonsense and frameshift/truncating alleles in LVNC; missense alleles are more frequently associated with DCM. The experimentally examined truncating allele **c.2104A>T (p.Lys702Ter)** impaired zebrafish cardiac function. (micolonghi2024unveilingthespectrum pages 18-19, theisen2024characterisationofthe pages 17-21)
- **Origin:** germline; familial autosomal-dominant and de novo cases occur. No evidence supports a somatic origin.
- **Population frequency:** causal alleles are individually very rare or absent from population databases. Aggregate comparison was 0.006% in gnomAD versus 1.35% in LVNC cases, but each variant requires transcript-aware gnomAD review and ACMG/AMP classification. (walsh2023thetroublewith pages 10-11)
- **Functional effect:** haploinsufficiency/loss of transcriptional regulation is the leading model. Variant-specific dominant-negative or gain-of-function effects are not established universally.

### Chromosomal and epigenetic context
The original mapping arose from **1p36 deletion syndrome**: 18 deletion patients with cardiomyopathy shared a deleted interval containing PRDM16 exons 4–17. Large 1p36 deletions can remove additional genes, so their phenotype is not equivalent to isolated LVNC8. (theisen2024characterisationofthe pages 17-21)

PRDM16 has histone-methyltransferase/chromatin-regulatory activity, but no reproducible disease-specific DNA-methylation signature has been defined. Variant interpretation should not infer LVNC8 from a 1p36 deletion without considering deletion extent and other dosage-sensitive genes.

### Testing interpretation
Apply ACMG/AMP criteria with ClinVar/ClinGen curation, segregation, de novo status, phenotype specificity, functional evidence, and population frequency. A rare PRDM16 missense VUS should not by itself establish LVNC8, especially when trabeculation is isolated.

## 5. Environmental, lifestyle, and infectious information

No infectious agent, toxin, radiation exposure, dietary factor, or occupational exposure is known to cause LVNC8. Physiologic remodeling during pregnancy or high-intensity training can meet morphology-based thresholds, creating a **gene–environment diagnostic interaction** rather than proven PRDM16 penetrance modification. The MARATHON study, NCT02568072, specifically examined exercise-induced trabeculation and reversibility after detraining. (NCT02568072 chunk 1)

For affected individuals, exercise recommendations should be individualized according to ejection fraction, arrhythmia burden, fibrosis, symptoms, and genotype rather than trabeculation alone. Standard cardiovascular risk reduction—no smoking, moderate alcohol, blood-pressure control, and appropriate activity—supports general cardiac health but is not primary prevention of LVNC8.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream trigger:** heterozygous PRDM16 loss of function or deletion reduces effective PRDM16 activity in developing ventricular cardiomyocytes.
2. **Cell-identity defect:** PRDM16 normally activates compact-myocardial genes and represses trabecular, neuronal, atrial, and conduction-system programs, partly with **TBX5** and **HAND1**.
3. **Developmental consequence:** compact-layer cardiomyocytes adopt trabecular/alternative identities; proliferation and ventricular-wall maturation are disturbed, producing excessive trabeculation and a thin compact layer.
4. **Metabolic consequence:** altered mitochondrial substrate use, redox stress, and reduced glycolytic/TCA intermediates impair energy reserve.
5. **Tissue/organ consequence:** ventricular dilation or hypoplasia, systolic/diastolic dysfunction, conduction-system abnormalities, fibrosis in some models/patients, arrhythmia, heart failure, and sudden death.

### Multi-omics and advanced technologies

Cardiomyocyte-specific Prdm16 knockout mice developed LV-specific dilation/dysfunction and biventricular noncompaction. RNA-seq, ChIP-seq, single-cell RNA-seq, and spatial transcriptomics showed that LV compact cardiomyocytes ectopically expressed trabecular genes (**Nppa, Nppb, Cited1, Mest**) and neural genes (**Cttnbp2, Spon1**), while compact-myocardial genes (**Hey2, Mb**) fell. In 7,783 single cardiomyocytes, the dominant changes occurred in LV compact myocardium, whereas right-ventricular compact cells were comparatively preserved. (wu2022prdm16isa pages 9-11, wu2022prdm16isa pages 1-3)

A 2024 combined single-cell RNA+ATAC study found that developmental PRDM16 loss shifted ventricular working cardiomyocytes toward atrial and conduction fates, caused distal ventricular conduction-system hyperplasia, abnormal electrophysiology, contractile dysfunction, and premature death. Direct abstract statement: **“PRDM16 favors ventricular working cardiomyocyte identity, by opposing the activity of master regulators of ventricular conduction and atrial fate.”** (Van Wauwe et al., published September 2024; DOI: https://doi.org/10.26508/lsa.202402719). (wauwe2024prdm16determinesspecification pages 1-2)

The 2023 heterozygous-mouse multi-omics study found hypoplastic hearts and reduced stroke volume, output, and ejection fraction with normal survival through eight months. Cardiac metabolites involved in amino-acid/glycerol metabolism, glycolysis, pentose-phosphate metabolism, and the TCA cycle were reduced; glutathione fell and IMP rose, indicating oxidative and energetic stress. Males accumulated triacylglycerides and showed reduced fatty-acid use; females had a more severe phenotype and prominent glucose/mitochondrial abnormalities. **PYROXD2** and **PBXIP1** emerged as candidate downstream metabolic regulators. (Kühnisch et al., published October 2023; DOI: https://doi.org/10.1093/cvr/cvad154). (kuhnisch2023prdm16mutationdetermines pages 1-2, kuhnisch2023prdm16mutationdetermines pages 4-7, kuhnisch2023prdm16mutationdetermines pages 10-11, kuhnisch2023prdm16mutationdetermines pages 8-10)

In zebrafish, PRDM16 knockdown or p.Lys702Ter expression caused bradycardia, reduced output, diminished cardiomyocyte proliferation, increased apoptosis, and electrical uncoupling. (theisen2024characterisationofthe pages 17-21)

**Suggested ontology annotations:** GO:0007507 heart development; GO:0003208 cardiac ventricle morphogenesis; GO:0060415 muscle-tissue morphogenesis; GO:0006355 regulation of DNA-templated transcription; GO:0007005 mitochondrion organization; GO:0006091 generation of precursor metabolites and energy; GO:0006979 response to oxidative stress. Cell types: ventricular cardiomyocyte (**CL:0000746**, verify current release), cardiac conduction cell, endothelial cell, and cardiac fibroblast.

## 7. Anatomical structures affected

- **Primary organ/system:** heart/cardiovascular system; primarily left ventricle, sometimes biventricular myocardium.
- **Localization:** apical and mid-ventricular segments are commonly emphasized in LVNC imaging; the process is not a lateralized paired-organ disorder.
- **Tissues:** compact and trabecular myocardium, ventricular conduction system, and secondarily interstitium/fibrosis.
- **Cells:** ventricular working cardiomyocytes are primary; conduction cardiomyocytes are secondarily expanded/mis-specified in models. Endocardial/endothelial signaling contributes to normal trabeculation generally, but direct endothelial causality in LVNC8 remains insufficiently established.
- **Subcellular compartments:** nucleus/chromatin—PRDM16 transcriptional regulation; mitochondria—energy/redox abnormalities; sarcomere and intercalated/electrical-coupling structures as downstream functional compartments.

Suggested anatomy terms include UBERON:0000948 heart, UBERON:0002084 heart left ventricle, ventricular myocardium, and interventricular septum; exact accession numbers beyond these should be validated against the production ontology release.

## 8. Temporal development and natural history

The structural susceptibility is developmental, but clinical recognition can be fetal, neonatal, childhood, or adult. PRDM16 expression is ventricular and developmentally prominent, declining postnatally. (wauwe2024prdm16determinesspecification pages 1-2)

Disease course is highly variable: lifelong asymptomatic morphology; stable mild dysfunction; or progressive dilation, heart failure, arrhythmia, and transplantation/death. No validated LVNC8 staging system exists. Practical stages are: genotype-positive/phenotype-negative; hypertrabeculation with preserved function; cardiomyopathy with dysfunction or arrhythmia; and advanced heart failure. Apparent “remission” can reflect reverse remodeling with heart-failure therapy or resolution of physiologic pregnancy/exercise trabeculation, not correction of the germline defect.

## 9. Inheritance and population

- **Inheritance:** predominantly autosomal dominant; de novo cases occur. Expressivity is markedly variable and penetrance is likely incomplete/age-dependent, but no reliable percentage exists. (walsh2023thetroublewith pages 10-11)
- **Anticipation:** not established.
- **Germline mosaicism:** theoretically possible after an apparently de novo event, but no LVNC8-specific frequency is known.
- **Founder effect/consanguinity:** none established; variants have been reported across European, Asian, and Australian populations. (walsh2023thetroublewith pages 10-11)
- **Prevalence/incidence/carrier frequency:** unknown for LVNC8. The 1.35% statistic is the proportion of an ascertained LVNC cohort carrying qualifying PRDM16 variants, not population prevalence. (walsh2023thetroublewith pages 10-11)
- **Sex ratio:** unknown. Mouse sexual dimorphism cannot be directly converted into human epidemiology. (kuhnisch2023prdm16mutationdetermines pages 1-2)

## 10. Diagnostics

### Clinical and imaging work-up

1. History, three-generation pedigree, physical examination, ECG, ambulatory rhythm monitoring, and transthoracic echocardiography.
2. Common echocardiographic criterion: end-systolic noncompacted-to-compacted myocardial ratio **>2.0** with characteristic two-layer morphology and perfused recesses.
3. CMR: commonly cited end-diastolic NC/C ratio **>2.3**; also assesses ventricular volumes/function, regional morphology, thrombus, and late-gadolinium-enhancement fibrosis. Neither threshold is sufficiently specific in isolation. (arbustini2014leftventricularnoncompaction pages 7-8)
4. Biomarkers such as BNP/NT-proBNP and troponin assess heart failure/injury but are not diagnostic of LVNC8. Heterozygous Prdm16 mice showed elevated BNP, supporting stretch/dysfunction rather than a specific biomarker. (kuhnisch2023prdm16mutationdetermines pages 2-3)
5. CT can assess trabeculation when MRI is unavailable or contraindicated; NCT01470014 enrolled 39 patients to investigate CT discrimination of isolated LVNC. (NCT01470014 chunk 1)

### Genetic testing
Use a validated cardiomyopathy panel including PRDM16 plus established sarcomeric, cytoskeletal, nuclear-envelope, ion-channel, mitochondrial, and syndromic LVNC genes. Exome/genome sequencing is appropriate when panel testing is negative, phenotype is syndromic, or structural variants are suspected. Copy-number analysis/CMA is important for developmental abnormalities suggestive of 1p36 deletion. Karyotype/FISH is not routine unless a chromosomal rearrangement is suspected. Mitochondrial-DNA testing is phenotype-driven; repeat-expansion testing has no specific role.

RNA sequencing may clarify splice variants but remains an adjunct. No validated diagnostic proteomic, metabolomic, epigenomic, or liquid-biopsy assay exists.

### Differential diagnosis
Physiologic athletic/pregnancy remodeling; normal prominent trabeculation; DCM/HCM with secondary trabeculation; apical HCM; endocardial fibroelastosis; arrhythmogenic cardiomyopathy; myocarditis; congenital heart disease; endomyocardial fibrosis; cardiac thrombus or tumor; neuromuscular/mitochondrial disorders. Dysfunction, fibrosis, arrhythmia, pathogenic genotype, and familial segregation favor cardiomyopathy over a benign trait.

### Screening
Offer genetic counseling and cascade testing for a pathogenic/likely pathogenic familial PRDM16 variant. First-degree relatives should have baseline ECG and imaging; variant-positive relatives require longitudinal surveillance. Echocardiographic family screening is recommended in familial LVNC. (arbustini2014leftventricularnoncompaction pages 9-10)

## 11. Outcome and prognosis

No LVNC8-specific 5- or 10-year survival estimate exists. Prognosis is driven less by trabeculation extent than by ventricular dysfunction, dilation, fibrosis, sustained ventricular arrhythmia, syncope, conduction disease, thrombus/embolism, and heart-failure severity. (walsh2023thetroublewith pages 1-2)

Broader LVNC morbidity includes heart-failure hospitalization, ICD implantation, stroke/systemic embolism, mechanical circulatory support, transplant, and sudden death. In one small historical ICD series, **37% of 30 patients** received appropriate ICD therapy during **40±34 months**, but this is neither a randomized estimate nor LVNC8-specific. (arbustini2014leftventricularnoncompaction pages 9-10)

Quality-of-life instruments specific to LVNC8 have not been validated. EQ-5D, SF-36, Kansas City Cardiomyopathy Questionnaire, pediatric quality-of-life tools, and PROMIS measures can quantify the impact of dyspnea, fatigue, arrhythmia anxiety, activity restriction, repeated imaging, and familial genetic risk.

## 12. Treatment and current applications

There is **no approved PRDM16-directed, gene, cell, RNA, or epigenetic therapy**. Treatment is phenotype-directed:

- **Heart failure:** guideline-directed therapy appropriate to age and ejection fraction—typically renin–angiotensin-system inhibition/ARNI, evidence-based beta-blocker, mineralocorticoid-receptor antagonist, SGLT2 inhibitor, and diuretic for congestion. Pediatric regimens require specialist dosing.
- **Arrhythmia:** ambulatory monitoring; antiarrhythmic therapy or ablation as clinically indicated. ICD placement follows conventional secondary-prevention or cardiomyopathy primary-prevention criteria rather than trabeculation alone. CRT may be considered with EF ≤35% and qualifying electrical dyssynchrony. (arbustini2014leftventricularnoncompaction pages 8-9)
- **Anticoagulation:** indicated for atrial fibrillation, documented ventricular thrombus, prior systemic embolism, or another standard indication; often considered when substantial LV dysfunction is present. Routine anticoagulation for isolated trabeculation with normal function remains debated. (arbustini2014leftventricularnoncompaction pages 9-10, arbustini2014leftventricularnoncompaction pages 8-9)
- **Advanced disease:** mechanical circulatory support and heart transplantation according to standard advanced-heart-failure criteria.
- **Rehabilitation/support:** individualized cardiac rehabilitation, exercise prescription, vaccination and infection prevention appropriate to heart-failure care, pregnancy counseling, psychosocial support, and genetic counseling.
- **Pharmacogenomics:** no PRDM16-specific drug-response guidance exists.

Suggested NCIt intervention concepts include genetic counseling, echocardiography, cardiac MRI, electrocardiography, Holter monitoring, anticoagulant therapy, beta-blocker therapy, implantable cardioverter-defibrillator, cardiac resynchronization therapy, ventricular assist device, and heart transplantation; exact NCIt accessions should be resolved against the implementation release.

### Trials and real-world implementation
No PRDM16-specific interventional trial was identified. Current implementation is through registries and risk-stratification studies:

- **NCT06024759**, recruiting, observational, target **500**, 10-year LVNC risk registry examining genetics, ventricular dysfunction, arrhythmia, strain, and ICD predictors. https://clinicaltrials.gov/study/NCT06024759 (NCT06024759 chunk 1)
- **NCT04265040**, recruiting, TORCH-Plus cardiomyopathy registry, target **2,040**, with phenotyping, biosampling, genomics, inflammation, and four-year mortality. https://clinicaltrials.gov/study/NCT04265040 (NCT04265040 chunk 1)
- **NCT03572569**, prospective family-based pediatric cardiomyopathy study, target **200**, evaluating death, mechanical support, and transplant over up to eight years. https://clinicaltrials.gov/study/NCT03572569 (NCT03572569 chunk 1)
- **NCT01470014**, completed CT diagnostic study, **39** participants. https://clinicaltrials.gov/study/NCT01470014 (NCT01470014 chunk 1)

## 13. Prevention

**Primary prevention:** the germline disorder cannot currently be prevented by lifestyle or vaccination. Reproductive options after counseling include prenatal diagnosis and preimplantation genetic testing when a familial pathogenic variant is known.

**Secondary prevention:** cascade genetic testing, periodic ECG/imaging, ambulatory rhythm monitoring, and early treatment of dysfunction or arrhythmia. Population or newborn screening is not recommended because prevalence, penetrance, and test performance are insufficiently defined.

**Tertiary prevention:** guideline-directed heart-failure therapy; thrombosis prevention when indicated; ICD/CRT in selected patients; exercise and pregnancy risk assessment; prompt treatment of decompensation; and family education regarding syncope, sustained palpitations, chest pain, and heart-failure warning signs.

## 14. Other species and natural disease

- **Human:** *Homo sapiens*, NCBI Taxon **9606**.
- **Mouse:** *Mus musculus*, Taxon **10090**; ortholog **Prdm16**.
- **Zebrafish:** *Danio rerio*, Taxon **7955**; prdm16 perturbation produces developmental cardiac dysfunction.

Naturally occurring LVNC-like disease has been described in veterinary species and Japanese macaques, but no retrieved evidence established a naturally occurring PRDM16-defined LVNC8 orthologous disease, breed predisposition, or VBO term. The condition is noninfectious and has no zoonotic or cross-species transmission.

## 15. Model organisms and experimental systems

### Zebrafish
Morpholino/antisense knockdown and expression of human p.Lys702Ter produced reduced output, bradycardia, diminished proliferation, apoptosis, and electrical uncoupling. Advantages include rapid developmental and cardiac-function assays; limitations include two-chamber anatomy, gene-duplication differences, and imperfect modeling of human ventricular compaction. (theisen2024characterisationofthe pages 17-21)

### Mouse

- **Cardiomyocyte-specific biallelic Prdm16 knockout:** LV dilation/dysfunction and biventricular noncompaction; strong model for developmental cell-identity mechanisms, but more severe than many heterozygous human cases. (wu2022prdm16isa pages 1-3)
- **Prdm16csp1/wt heterozygote:** viable with mild hypoplastic cardiomyopathy, reduced systolic performance, early metabolic stress, and female-predominant severity. It better models haploinsufficiency but lacks the full human structural/arrhythmic spectrum and showed no fibrosis in one characterization. (kuhnisch2023prdm16mutationdetermines pages 1-2, theisen2024characterisationofthe pages 76-81)
- **Developmental cardiomyocyte knockout with single-cell RNA+ATAC:** demonstrates atrial/conduction fate shift and conduction-system hyperplasia; useful for chromatin and lineage studies, though premature death limits chronic-treatment experiments. (wauwe2024prdm16determinesspecification pages 1-2)

### Human cellular systems
Patient-specific iPSC cardiomyocytes have established the broader LVNC paradigm that abnormal developmental signaling and impaired cardiomyocyte proliferation can be modeled and rescued experimentally. In TBX20-associated LVNC, TGF-β activation reduced proliferation; PRDM16 was identified as a downstream target, and PRDM16 editing itself caused proliferation defects. This supports pathway convergence but is not a direct PRDM16-patient LVNC8 model. Relevant abstract language states that **“inhibition of TGF-β signalling and genome correction of the TBX20 mutation were sufficient to reverse the disease phenotype”** (Kodo et al., 2016; DOI: https://doi.org/10.1038/ncb3411).

## Evidence appraisal and critical gaps

The strongest LVNC8 evidence combines rare-variant enrichment, de novo/familial truncating alleles, 1p36 deletion mapping, and concordant zebrafish/mouse functional studies. Recent 2023–2024 work substantially advances mechanism through multi-omics and single-cell chromatin/transcriptome analysis. However, exact prevalence, penetrance, variant-specific prognosis, human sex effects, environmental modifiers, quality-of-life data, and treatment-response rates remain unknown. Morphology-only diagnosis risks substantial overcalling; expert interpretation should prioritize the integrated **genotype–phenotype–function–family** context rather than the NC/C ratio alone. (walsh2023thetroublewith pages 10-11, wauwe2024prdm16determinesspecification pages 1-2, walsh2023thetroublewith pages 1-2, kuhnisch2023prdm16mutationdetermines pages 1-2)

References

1. (OpenTargets Search: left ventricular noncompaction-PRDM16): Open Targets Query (left ventricular noncompaction-PRDM16, 2 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (wu2022prdm16isa pages 13-14): Tongbin Wu, Zhengyu Liang, Zengming Zhang, Canzhao Liu, Lunfeng Zhang, Yusu Gu, Kirk L. Peterson, Sylvia M. Evans, Xiang-Dong Fu, and Ju Chen. Prdm16 is a compact myocardium-enriched transcription factor required to maintain compact myocardial cardiomyocyte identity in left ventricle. Circulation, 145:586-602, Feb 2022. URL: https://doi.org/10.1161/circulationaha.121.056666, doi:10.1161/circulationaha.121.056666. This article has 106 citations and is from a highest quality peer-reviewed journal.

3. (walsh2023thetroublewith pages 10-11): Roddy Walsh. The trouble with trabeculation: how genetics can help to unravel a complex and controversial phenotype. Journal of cardiovascular translational research, 16:1310-1324, Nov 2023. URL: https://doi.org/10.1007/s12265-023-10459-6, doi:10.1007/s12265-023-10459-6. This article has 11 citations and is from a peer-reviewed journal.

4. (arbustini2014leftventricularnoncompaction pages 7-8): Eloisa Arbustini, Frank Weidemann, and Jennifer L. Hall. Left ventricular noncompaction: a distinct cardiomyopathy or a trait shared by different cardiac diseases? Journal of the American College of Cardiology, 64 17:1840-50, Oct 2014. URL: https://doi.org/10.1016/j.jacc.2014.08.030, doi:10.1016/j.jacc.2014.08.030. This article has 324 citations and is from a highest quality peer-reviewed journal.

5. (walsh2023thetroublewith pages 1-2): Roddy Walsh. The trouble with trabeculation: how genetics can help to unravel a complex and controversial phenotype. Journal of cardiovascular translational research, 16:1310-1324, Nov 2023. URL: https://doi.org/10.1007/s12265-023-10459-6, doi:10.1007/s12265-023-10459-6. This article has 11 citations and is from a peer-reviewed journal.

6. (arbustini2014leftventricularnoncompaction pages 8-9): Eloisa Arbustini, Frank Weidemann, and Jennifer L. Hall. Left ventricular noncompaction: a distinct cardiomyopathy or a trait shared by different cardiac diseases? Journal of the American College of Cardiology, 64 17:1840-50, Oct 2014. URL: https://doi.org/10.1016/j.jacc.2014.08.030, doi:10.1016/j.jacc.2014.08.030. This article has 324 citations and is from a highest quality peer-reviewed journal.

7. (arbustini2014leftventricularnoncompaction pages 9-10): Eloisa Arbustini, Frank Weidemann, and Jennifer L. Hall. Left ventricular noncompaction: a distinct cardiomyopathy or a trait shared by different cardiac diseases? Journal of the American College of Cardiology, 64 17:1840-50, Oct 2014. URL: https://doi.org/10.1016/j.jacc.2014.08.030, doi:10.1016/j.jacc.2014.08.030. This article has 324 citations and is from a highest quality peer-reviewed journal.

8. (wu2022prdm16isa pages 1-3): Tongbin Wu, Zhengyu Liang, Zengming Zhang, Canzhao Liu, Lunfeng Zhang, Yusu Gu, Kirk L. Peterson, Sylvia M. Evans, Xiang-Dong Fu, and Ju Chen. Prdm16 is a compact myocardium-enriched transcription factor required to maintain compact myocardial cardiomyocyte identity in left ventricle. Circulation, 145:586-602, Feb 2022. URL: https://doi.org/10.1161/circulationaha.121.056666, doi:10.1161/circulationaha.121.056666. This article has 106 citations and is from a highest quality peer-reviewed journal.

9. (wu2022prdm16isa pages 9-11): Tongbin Wu, Zhengyu Liang, Zengming Zhang, Canzhao Liu, Lunfeng Zhang, Yusu Gu, Kirk L. Peterson, Sylvia M. Evans, Xiang-Dong Fu, and Ju Chen. Prdm16 is a compact myocardium-enriched transcription factor required to maintain compact myocardial cardiomyocyte identity in left ventricle. Circulation, 145:586-602, Feb 2022. URL: https://doi.org/10.1161/circulationaha.121.056666, doi:10.1161/circulationaha.121.056666. This article has 106 citations and is from a highest quality peer-reviewed journal.

10. (wauwe2024prdm16determinesspecification pages 1-2): Jore Van Wauwe, Alexia Mahy, Sander Craps, Samaneh Ekhteraei-Tousi, Pieter Vrancaert, Hannelore Kemps, Wouter Dheedene, Rosa Doñate Puertas, Sander Trenson, H. Llewelyn Roderick, Manu Beerens, and Aernout Luttun. Prdm16 determines specification of ventricular cardiomyocytes by suppressing alternative cell fates. Life Science Alliance, 7:e202402719, Sep 2024. URL: https://doi.org/10.26508/lsa.202402719, doi:10.26508/lsa.202402719. This article has 8 citations and is from a peer-reviewed journal.

11. (kuhnisch2023prdm16mutationdetermines pages 1-2): Jirko Kühnisch, Simon Theisen, Josephine Dartsch, Raphaela Fritsche-Guenther, Marieluise Kirchner, Benedikt Obermayer, Anna Bauer, Anne-Karin Kahlert, Michael Rothe, Dieter Beule, Arnd Heuser, Philipp Mertins, Jennifer A Kirwan, Nikolaus Berndt, Calum A MacRae, Norbert Hubner, and Sabine Klaassen. <i>prdm16</i> mutation determines sex-specific cardiac metabolism and identifies two novel cardiac metabolic regulators. Cardiovascular Research, 119:2902-2916, Oct 2023. URL: https://doi.org/10.1093/cvr/cvad154, doi:10.1093/cvr/cvad154. This article has 16 citations and is from a domain leading peer-reviewed journal.

12. (kuhnisch2023prdm16mutationdetermines pages 4-7): Jirko Kühnisch, Simon Theisen, Josephine Dartsch, Raphaela Fritsche-Guenther, Marieluise Kirchner, Benedikt Obermayer, Anna Bauer, Anne-Karin Kahlert, Michael Rothe, Dieter Beule, Arnd Heuser, Philipp Mertins, Jennifer A Kirwan, Nikolaus Berndt, Calum A MacRae, Norbert Hubner, and Sabine Klaassen. <i>prdm16</i> mutation determines sex-specific cardiac metabolism and identifies two novel cardiac metabolic regulators. Cardiovascular Research, 119:2902-2916, Oct 2023. URL: https://doi.org/10.1093/cvr/cvad154, doi:10.1093/cvr/cvad154. This article has 16 citations and is from a domain leading peer-reviewed journal.

13. (kuhnisch2023prdm16mutationdetermines pages 10-11): Jirko Kühnisch, Simon Theisen, Josephine Dartsch, Raphaela Fritsche-Guenther, Marieluise Kirchner, Benedikt Obermayer, Anna Bauer, Anne-Karin Kahlert, Michael Rothe, Dieter Beule, Arnd Heuser, Philipp Mertins, Jennifer A Kirwan, Nikolaus Berndt, Calum A MacRae, Norbert Hubner, and Sabine Klaassen. <i>prdm16</i> mutation determines sex-specific cardiac metabolism and identifies two novel cardiac metabolic regulators. Cardiovascular Research, 119:2902-2916, Oct 2023. URL: https://doi.org/10.1093/cvr/cvad154, doi:10.1093/cvr/cvad154. This article has 16 citations and is from a domain leading peer-reviewed journal.

14. (NCT06024759 chunk 1):  Predictors of Risk in Left Ventricular Non-Compaction. London Health Sciences Centre Research Institute OR Lawson Research Institute of St. Joseph's. 2023. ClinicalTrials.gov Identifier: NCT06024759

15. (NCT04265040 chunk 1): Benjamin Meder. DZHK TORCH-Plus is a Registry for Patients With Cardiomyopathies and Serves as Source for Cardiovascular Research Studies. University Hospital Heidelberg. 2020. ClinicalTrials.gov Identifier: NCT04265040

16. (NCT06607471 chunk 23): Giovanni Peretto. Multimodal and Multidisciplinary Approach to Optimize Diagnostic, Prognostic, and Therapeutic Management of Patients with Non-ischemic Cardiomyopathies and Arrhythmogenic-inflammatory Phenotypes: a Multicenter, Observational, Retrospective and Prospective Registry Study.. Scientific Institute San Raffaele. 2018. ClinicalTrials.gov Identifier: NCT06607471

17. (NCT01470014 chunk 1):  Cardiac Computed Tomography: Characteristics of Isolated Left Ventricular Non-compaction. University of Zurich. 2011. ClinicalTrials.gov Identifier: NCT01470014

18. (NCT03572569 chunk 1):  Risk Stratification in Children and Adolescents With Primary Cardiomyopathy. German Heart Institute. 2013. ClinicalTrials.gov Identifier: NCT03572569

19. (NCT02568072 chunk 1):  Training-induced Increased Left Ventricular Trabeculation. St George's, University of London. 2015. ClinicalTrials.gov Identifier: NCT02568072

20. (micolonghi2024unveilingthespectrum pages 18-19): Caterina Micolonghi, Federica Perrone, Marco Fabiani, Silvia Caroselli, Camilla Savio, Antonio Pizzuti, Aldo Germani, Vincenzo Visco, Simona Petrucci, Speranza Rubattu, and Maria Piane. Unveiling the spectrum of minor genes in cardiomyopathies: a narrative review. International Journal of Molecular Sciences, 25:9787, Sep 2024. URL: https://doi.org/10.3390/ijms25189787, doi:10.3390/ijms25189787. This article has 11 citations.

21. (theisen2024characterisationofthe pages 17-21): Simon Theisen. Characterisation of the prdm16csp1/wt mouse as a model for the prdm16 associated cardiomyopathy. Text, Jan 2024. URL: https://doi.org/10.17169/refubium-41680, doi:10.17169/refubium-41680. This article has 0 citations and is from a peer-reviewed journal.

22. (kuhnisch2023prdm16mutationdetermines pages 8-10): Jirko Kühnisch, Simon Theisen, Josephine Dartsch, Raphaela Fritsche-Guenther, Marieluise Kirchner, Benedikt Obermayer, Anna Bauer, Anne-Karin Kahlert, Michael Rothe, Dieter Beule, Arnd Heuser, Philipp Mertins, Jennifer A Kirwan, Nikolaus Berndt, Calum A MacRae, Norbert Hubner, and Sabine Klaassen. <i>prdm16</i> mutation determines sex-specific cardiac metabolism and identifies two novel cardiac metabolic regulators. Cardiovascular Research, 119:2902-2916, Oct 2023. URL: https://doi.org/10.1093/cvr/cvad154, doi:10.1093/cvr/cvad154. This article has 16 citations and is from a domain leading peer-reviewed journal.

23. (kuhnisch2023prdm16mutationdetermines pages 2-3): Jirko Kühnisch, Simon Theisen, Josephine Dartsch, Raphaela Fritsche-Guenther, Marieluise Kirchner, Benedikt Obermayer, Anna Bauer, Anne-Karin Kahlert, Michael Rothe, Dieter Beule, Arnd Heuser, Philipp Mertins, Jennifer A Kirwan, Nikolaus Berndt, Calum A MacRae, Norbert Hubner, and Sabine Klaassen. <i>prdm16</i> mutation determines sex-specific cardiac metabolism and identifies two novel cardiac metabolic regulators. Cardiovascular Research, 119:2902-2916, Oct 2023. URL: https://doi.org/10.1093/cvr/cvad154, doi:10.1093/cvr/cvad154. This article has 16 citations and is from a domain leading peer-reviewed journal.

24. (theisen2024characterisationofthe pages 76-81): Simon Theisen. Characterisation of the prdm16csp1/wt mouse as a model for the prdm16 associated cardiomyopathy. Text, Jan 2024. URL: https://doi.org/10.17169/refubium-41680, doi:10.17169/refubium-41680. This article has 0 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Left_Ventricular_Noncompaction_8-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 8 |
| Off topic | 0 |

All extracted references resolved successfully.