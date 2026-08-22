---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-19T09:06:31.315141'
end_time: '2026-08-19T09:17:45.991557'
duration_seconds: 674.68
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Congenital Heart Disease
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 21
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 6
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Congenital_Heart_Disease-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Congenital Heart Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Congenital Heart Disease** covering all of the
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
- **Disease Name:** Congenital Heart Disease
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Congenital Heart Disease** covering all of the
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


# Congenital Heart Disease: Comprehensive Disease-Characteristics Report

## Executive summary

Congenital heart disease (CHD) is an umbrella term for structurally or functionally important cardiovascular malformations arising during embryonic development and present at birth, although mild lesions may not be recognized until childhood or adulthood. It is not one molecular disease: lesions range from small septal defects to tetralogy of Fallot (TOF), transposition of the great arteries (TGA), hypoplastic left-heart syndrome (HLHS), and heterotaxy. Contemporary studies generally place prevalence near 1% of live births; broader definitions that include bicuspid aortic valve and very small defects produce estimates approaching 1–2%. Genetic or recognized environmental causes are found in only a minority of all cases, but diagnostic yield rises markedly in severe, syndromic, or extracardiac-malformation cohorts. In a 2024 neonatal intensive-care cohort, a molecular/cytogenetic diagnosis was established in 17% (32/188) of infants. (helm2021geneticevaluationof pages 1-2, peterlin2024thegeneticarchitecture pages 10-12)

CHD begins prenatally but is usually a lifelong condition rather than a lesion “cured” by surgery. Improved fetal diagnosis, neonatal surgery, catheter intervention, and longitudinal care have shifted much of the burden toward adult heart failure, arrhythmia, pulmonary vascular disease, reintervention, neurodevelopmental disability, and psychosocial morbidity. Sudden cardiac death (SCD) is reported at 0.28–2.7% per year in CHD cohorts and 0.9–1.5% per year after TOF in the reviewed literature, accounting for as many as 25% of CHD deaths in some populations. (salzillo2024cardiovasculardiseasesin pages 10-11)

The following table provides an ontology-oriented synopsis.

| domain | core facts | suggested ontology terms/IDs | key evidence/statistics |
|---|---|---|---|
| Disease definition/identifier | Congenital heart disease (CHD) is a heterogeneous group of structural heart defects present at birth; it is the most commonly detected congenital anomaly. Use disease-level aggregated resources rather than individual EHR-derived evidence for core definition. | MONDO:0005453 congenital heart disease; MeSH: Congenital Heart Defects | Affects up to ~1% of live-born neonates; global prevalence often cited as 1–2% of infants (peterlin2024thegeneticarchitecture pages 10-12, helm2021geneticevaluationof pages 1-2) |
| Major lesion phenotypes | Representative major lesions include ventricular septal defect, tetralogy of Fallot, hypoplastic left heart syndrome, transposition of the great arteries, left ventricular outflow tract obstruction, and single-ventricle disease. | HP:0001629 Ventricular septal defect; HP:0001636 Tetralogy of Fallot; HP:0004383 Hypoplastic left heart; HP:0001651 Transposition of the great arteries; HP:0005105 Abnormality of left ventricular outflow tract; HP:0004762 Single ventricle | TOF and HLHS were specifically analyzed in recent single-cell/machine-learning work; LVOTO had relatively high diagnostic genetic yield in isolated CHD cohorts (ma2024machinelearningin pages 2-3, helm2021geneticevaluationof pages 1-2) |
| Genetics: causal/susceptibility genes | Recurrently implicated CHD genes include NKX2-5, GATA4, GATA6, TBX20, TBX1, GDF1, MYH6, TNNT2, TFAP2B, TAB2, GJA1; BMP4 has recent evidence as a causative/predisposing gene. | HGNC: NKX2-5, GATA4, GATA6, TBX20, TBX1, GDF1, MYH6, TNNT2, TFAP2B, TAB2, GJA1, BMP4; MONDO:0800441 NKX2.5-related congenital, conduction and myopathic heart disease | Open Targets lists strongest CHD associations for NKX2-5 and GATA4; 2024 familial study identified BMP4 p.Tyr106* segregating with CHD and loss of induction of NKX2-5/TBX20 targets (OpenTargets Search: congenital heart disease, salzillo2024cardiovasculardiseasesin pages 13-15) |
| Chromosomal/syndromic contributors | Important chromosomal or syndromic causes include trisomy 21, trisomy 18, trisomy 13, Turner syndrome, 22q11.2 deletion/DiGeorge syndrome, Williams syndrome, CHARGE syndrome, and Noonan syndrome. | 22q11.2 deletion syndrome; trisomy 21; trisomy 18; trisomy 13; Turner syndrome; Williams syndrome; CHARGE syndrome; Noonan syndrome | In a 2024 NICU cohort, 17% received a genetic diagnosis; most frequent diagnoses were 22q11.2 deletion and CHARGE, followed by Noonan and Williams syndromes (peterlin2024thegeneticarchitecture pages 10-12, salzillo2024cardiovasculardiseasesin pages 13-15) |
| Genetic testing/diagnostic yield | Current evidence supports chromosomal microarray (CMA) and next-generation sequencing (NGS/WGS/WES) in severe or syndromic CHD; isolated CHD can still yield diagnoses. | CMA; WES; WGS; copy-number variant analysis | CMA diagnostic yield: 14.6% in 440 infants and 10.1% in 188 NICU neonates; overall genetic diagnosis 17% in the NICU cohort; isolated CHD still had diagnostic findings (6.5% CMA-positive in one cohort; ~3% diagnosed in another cohort) (helm2021geneticevaluationof pages 1-2, peterlin2024thegeneticarchitecture pages 10-12) |
| Environmental/non-genetic risk factors | CHD risk is influenced by maternal and environmental exposures, including maternal diabetes, obesity, gestational hypertension, harmful chemicals, noise, antidepressant exposure, and family genetic history. | CHEBI terms not resolved here; exposure concepts: maternal diabetes, maternal obesity, SSRI/SNRI exposure | Updated umbrella review found convincing/highly suggestive evidence for maternal DM, obesity, folic acid supplementation, antidepressants, gestational hypertension, decoration materials, harmful chemicals, and noise exposure associations (zubrzycki2024cardiacdevelopmentand pages 25-26) |
| Protective factors | Maternal folic acid supplementation is repeatedly discussed as a modifiable factor associated with reduced CHD risk, although evidence varies by lesion and study design. | folic acid supplementation | Umbrella review identified folic acid supplementation among the strongest non-genetic factors evaluated for CHD prevention relevance (zubrzycki2024cardiacdevelopmentand pages 25-26) |
| Developmental pathways/mechanisms | CHD arises from disruption of cardiac morphogenesis involving second heart field, neural crest, epicardial progenitors, and pathways such as BMP, Notch, Wnt, TGF-beta/Smad, laterality/NODAL signaling, and transcriptional programs controlling septation and outflow tract development. | GO:0007507 heart development; GO:0060916 cardiac septum morphogenesis; GO:0001947 heart looping; GO:0007220 Notch signaling pathway; GO:0030509 BMP signaling pathway; GO:0016055 Wnt signaling pathway; GO:0007179 TGF-beta receptor signaling pathway | Recent reviews emphasize genetic plus environmental regulation of fetal heart development; single-cell/machine-learning studies also point to pathway disruption across CHD subtypes (zubrzycki2024cardiacdevelopmentand pages 25-26, ma2024machinelearningin pages 2-3) |
| Cell types involved | Key implicated cardiac cell populations include cardiomyocytes, endothelial cells, cardiac fibroblasts, neural crest-derived cells, second heart field progenitors, and epicardial progenitor cells. | CL:0000746 cardiac muscle cell; CL:0000115 endothelial cell; CL:0000057 fibroblast; CL:0000349 neural crest cell; CL:0002494 epicardial cell | 2024 single-cell analysis examined 73,296 cardiomyocytes, 35,673 endothelial cells, and 21,034 fibroblasts across CHD-related conditions (ma2024machinelearningin pages 2-3, ma2024machinelearningin pages 21-23) |
| Anatomy/localization | Primary structures affected include cardiac septa, ventricular chambers, atria, outflow tract, great arteries, valves, coronary arteries, aorta, and conduction system. | UBERON:0000948 heart; UBERON:0002084 cardiac ventricle; UBERON:0002079 atrium; UBERON:0001981 cardiac septum; UBERON:0003129 outflow tract; UBERON:0000947 aorta | Reviews of chromosomal CHD and imaging emphasize abnormalities across chambers, valves, coronary arteries, aorta, and conduction tissue (salzillo2024cardiovasculardiseasesin pages 13-15) |
| Imaging/clinical diagnostics | Core diagnostics include echocardiography, fetal echocardiography, genetic testing, and cardiovascular magnetic resonance (CMR) for detailed anatomy, hemodynamics, and postoperative follow-up. | fetal echocardiography; cardiac MRI/CMR | CMR provides high-detail anatomy, chamber volumes, flow, tissue characterization, and postoperative assessment without ionizing radiation; prenatal diagnosis relies heavily on fetal echocardiography (salzillo2024cardiovasculardiseasesin pages 13-15) |
| Treatment/interventions | Management includes surgical repair/palliation, catheter-based intervention, balloon valvuloplasty, staged Norwood/Glenn/Fontan procedures for HLHS, medications for heart failure/arrhythmia/hemodynamics, implantable defibrillators in selected cases, and heart transplantation for severe disease. | NCIT: Cardiac Surgical Procedure; NCIT: Catheterization; NCIT: Balloon Valvuloplasty; NCIT: Fontan Procedure; NCIT: Norwood Procedure; NCIT: Glenn Procedure; NCIT: Heart Transplantation; NCIT: Implantable Cardioverter Defibrillator | Recent summaries note surgery as highest-risk/highest-cost, catheter procedures as resource-intensive, and lifelong medication burden; severe cases may need transplant or ICDs (ma2024machinelearningin pages 2-3, salzillo2024cardiovasculardiseasesin pages 13-15) |
| Outcomes/prognosis | Mortality and complication burden remain substantial despite improved survival. SCD is a major late complication, especially in complex lesions and repaired TOF. | HP:0001644 Sudden cardiac death; HP:0011675 Arrhythmia | SCD incidence in CHD cohorts reported at 0.28–2.7% annually; TOF 0.9–1.5% annually; SCD may account for up to 25% of deaths in CHD populations (salzillo2024cardiovasculardiseasesin pages 10-11) |
| Omics and advanced models | Emerging CHD research uses single-cell transcriptomics, RNA-seq, metabolomics, machine learning, iPSC-derived cardiomyocytes, CRISPR rescue experiments, and organoid systems. | single-cell RNA-seq; metabolomics; iPSC-CM disease model; CRISPR/Cas9 | iPSC-CM models identified mitochondrial dysfunction/oxidative stress in HLHS and showed rescue of MYH6-R443P dysfunction by gene editing; metabolomics studies linked perioperative metabolites to mortality, AKI, and neurologic outcomes (pushpan2024ipscderivedcardiomyocytesas pages 10-11, meggiolaro2024metabolomicprofilingof pages 4-5, ma2024machinelearningin pages 21-23) |
| Current real-world studies/trials | Active real-world implementation includes national/regional registries, transition programs, arrhythmia imaging studies, prenatal multi-omics studies, device studies, and lifecycle CHD registries. | ClinicalTrials.gov: NCT02258724, NCT06611787, NCT06705543, NCT07425132, NCT07559253 | Beijing Anzhen lifecycle registry plans 100,000 patients with long-term follow-up; other active studies include adult CHD registry and fetal complex CHD multi-omics investigation (NCT06611787 chunk 1) |
| Evidence caveats | CHD is highly heterogeneous; many estimates pool diverse lesions, ages, and syndromic/isolated cases. Diagnostic yields vary by cohort selection and testing strategy; some cited evidence comes from reviews or registry descriptions rather than lesion-specific randomized trials. | Evidence annotation recommended: human clinical, registry, review, model organism, in vitro | Several excerpts note limited access due to socioeconomic disparities, small sample sizes in omics studies, and imperfect sensitivity of dysmorphology-based screening (salzillo2024cardiovasculardiseasesin pages 13-15, meggiolaro2024metabolomicprofilingof pages 4-5, helm2021geneticevaluationof pages 1-2) |


*Table: This table condenses the conversation’s established congenital heart disease facts into ontology-ready domains for a knowledge base. It highlights identifiers, phenotypes, genes, pathways, anatomy, diagnostics, treatments, and key evidence caveats with citeable context IDs.*

## 1. Disease information

### Definition and classification

CHD comprises abnormalities of cardiac chambers, septa, valves, coronary arteries, aorta, great arteries, venous connections, and/or conduction-related anatomy caused by abnormal cardiovascular morphogenesis. Clinically useful groupings include:

* **Septal lesions:** ventricular septal defect (VSD), atrial septal defect, atrioventricular septal defect.
* **Left-sided obstruction:** bicuspid aortic valve, valvar/subvalvar aortic stenosis, coarctation, interrupted aortic arch, HLHS.
* **Right-sided obstruction:** pulmonary stenosis/atresia and tricuspid atresia.
* **Conotruncal defects:** TOF, truncus arteriosus, TGA, double-outlet right ventricle.
* **Anomalous connections:** total/partial anomalous pulmonary venous connection.
* **Single-ventricle and laterality disorders:** unbalanced atrioventricular canal, heterotaxy, and other functionally univentricular hearts.

### Identifiers and synonyms

* **MONDO:** MONDO:0005453, congenital heart disease. Related umbrella term: MONDO:0019512, congenital heart malformation; syndromic CHD: MONDO:0100614.
* **MeSH:** *Heart Defects, Congenital*.
* **ICD-10-CM:** principally Q20–Q28; Q20–Q26 cover congenital malformations of cardiac chambers/connections, septa, valves, great arteries, and great veins.
* **ICD-11:** lesion-specific entities reside under congenital anomalies of the circulatory system; a single code should not replace lesion-level coding.
* **OMIM/Orphanet:** no single OMIM entry adequately represents all CHD. OMIM and Orphanet are most appropriately attached to the causal syndrome or lesion–gene disorder, such as 22q11.2 deletion syndrome, Holt–Oram syndrome, or NKX2-5-related disease.
* **Synonyms:** congenital heart defect, congenital cardiac defect, congenital cardiovascular malformation, congenital heart anomaly, congenital cardiac malformation.

The definition, ontology identifiers, and pooled epidemiology are **aggregated disease-level knowledge**. Patient-specific lesion, imaging, procedure, and genotype data are ordinarily derived from EHRs, registries, or cohorts and should remain provenance-linked rather than being treated as universal disease facts.

## 2. Etiology, risk, protection, and gene–environment interaction

### Genetic causal factors

CHD has a mixed architecture: aneuploidies and pathogenic copy-number variants (CNVs), highly penetrant single-gene variants, incompletely penetrant inherited variants, de novo variants, oligogenic combinations, and common polygenic susceptibility all occur. Earlier severe-infant cohorts attributed approximately 8–10% to aneuploidy, 3–5% to single-gene disease, and a variable 3–25% to pathogenic CNVs, depending strongly on ascertainment and technology. (helm2021geneticevaluationof pages 1-2)

Major chromosomal/syndromic contributors include trisomies 21, 18, and 13; monosomy X; 22q11.2 deletion; Williams–Beuren syndrome; CHARGE; and RASopathies such as Noonan syndrome. Trisomy 21 is especially associated with atrioventricular septal defects; 22q11.2 deletion/TBX1 with conotruncal and aortic-arch defects; Turner syndrome with bicuspid aortic valve and coarctation; and Williams syndrome with supravalvar aortic stenosis. A 2024 NICU study found 22q11.2 deletion and CHARGE most often, followed by Noonan and Williams syndromes. (salzillo2024cardiovasculardiseasesin pages 13-15, peterlin2024thegeneticarchitecture pages 10-12)

High-priority developmental genes include **NKX2-5, GATA4, GATA6, TBX1, TBX5, TBX20, NOTCH1, JAG1, KMT2D, CHD7, ELN, PTPN11, RAF1, ZIC3, NODAL, GDF1, MMP21, MYH6, ACTC1, TAB2, TFAP2B**, and **GJA1**. Open Targets ranks NKX2-5 and GATA4 among the strongest general CHD associations and also supports TBX20, GDF1, MYH6, TFAP2B, TAB2, NODAL, MMP21, GJA1, and TBX1. These associations are lesion- and syndrome-dependent and should not be interpreted as a validated universal “CHD panel.” (OpenTargets Search: congenital heart disease)

**Variant classes** include germline missense, nonsense, frameshift, splice, regulatory, and structural variants. Pathogenic alleles are usually rare or absent in population databases; no meaningful single carrier frequency exists for heterogeneous CHD. Classification should follow ACMG/AMP criteria using segregation, de novo status, population frequency, functional evidence, and phenotype specificity. A 2024 familial study reported heterozygous **BMP4 NM_001202.6:c.318T>G, p.(Tyr106*)**, cosegregating with CHD; mutant BMP4 failed to activate NKX2-5 and TBX20 reporter expression. This is promising single-family evidence, not justification for treating all rare BMP4 variants as pathogenic. (salzillo2024cardiovasculardiseasesin pages 13-15)

### Environmental and maternal factors

An umbrella review covering 56 systematic reviews, 369 meta-analyses, and 949 component studies found the strongest reported non-genetic associations for maternal pregestational/gestational diabetes, obesity—particularly moderate or severe obesity—gestational hypertension, antidepressant exposure including SSRIs/SNRIs, harmful chemicals, renovation materials, noise exposure, and reproductive/family-history variables. Only 16% of the included systematic reviews were rated “moderate” by AMSTAR2, so association does not necessarily establish causation. (zubrzycki2024cardiacdevelopmentand pages 25-26)

Other recognized or suspected risks include maternal phenylketonuria, rubella infection, retinoic acid, valproate, lithium for selected lesions, smoking, alcohol, air pollution, fever, advanced parental age, assisted reproduction, and occupational solvent/pesticide exposure. Absolute risk generally remains low for any single exposure, and confounding by indication is important for medication studies.

### Protective factors and prevention-relevant modifiers

Periconceptional folic acid/multivitamin use is associated with lower risk in several observational syntheses, but effect size varies by lesion and study design. The evidence supports adequate folate for general congenital-anomaly prevention, not a guarantee against CHD. Glycemic optimization before conception and during early pregnancy is one of the clearest modifiable strategies for women with diabetes. Avoidance of rubella through pre-pregnancy immunization, teratogen review, smoking/alcohol avoidance, healthy weight, and treatment of maternal phenylketonuria are also rational primary-prevention measures. (zubrzycki2024cardiacdevelopmentand pages 25-26)

No reproducible “protective CHD allele” is established for routine clinical use. Modifier alleles and background polygenic burden probably influence penetrance and severity, but remain research-level.

### Gene–environment interaction

The biologically plausible model is that maternal metabolic or toxic exposures alter oxidative stress, one-carbon metabolism, chromatin state, signaling, or neural-crest/second-heart-field development in an embryo whose genetic background changes susceptibility. Folate-pathway variants and maternal folate are a frequently studied example, but robust lesion-specific G×E estimates are limited. Thus, exposure history and molecular diagnosis should be represented as interacting evidence rather than mutually exclusive causes.

## 3. Phenotypes

| Phenotype | Type, onset, course, and impact | Suggested HPO term |
|---|---|---|
| VSD | Structural sign; prenatal/neonatal. Small lesions may close spontaneously; large lesions cause early heart failure, poor feeding, and growth failure. | HP:0001629 |
| Atrial septal defect | Structural sign; often asymptomatic in childhood, with later right-heart dilation, exercise limitation, or atrial arrhythmia. | HP:0001631 |
| Atrioventricular septal defect | Structural sign; neonatal/infant heart failure and pulmonary overcirculation; severity variable and often syndromic. | HP:0006695 |
| TOF | Cyanotic structural defect; neonatal-to-infant onset depending on obstruction; episodic hypercyanotic spells may occur before repair. | HP:0001636; cyanosis HP:0000961 |
| TGA | Critical neonatal cyanosis, generally severe and rapidly progressive without mixing and intervention. | HP:0001651 |
| Coarctation/aortic obstruction | May present after ductal closure with shock, weak femoral pulses, differential blood pressure, or later hypertension. | HP:0001680; hypertension HP:0000822 |
| HLHS | Critical neonatal duct-dependent systemic circulation; severe, staged-palliation or transplant pathway. | HP:0004383 |
| Single-ventricle physiology | Structural/physiological state leading to chronic cyanosis before palliation and lifelong Fontan-associated morbidity after palliation. | HP:0004762 |
| Heart failure | Symptom/sign complex: tachypnea, feeding difficulty, diaphoresis, hepatomegaly, poor growth; may recur in adulthood. | HP:0001635 |
| Arrhythmia/conduction disease | Episodic or progressive; postoperative scars, chamber dilation, and specific genotypes contribute. | HP:0011675; conduction abnormality HP:0031546 |
| Pulmonary hypertension | Progressive vascular complication of unrepaired shunts, late repair, or complex physiology. | HP:0002092 |
| Exercise intolerance/fatigue | Common functional phenotype in moderate/complex CHD; affects school, work, participation, and quality of life. | HP:0003546; fatigue HP:0012378 |
| Growth failure | Most evident in infants with heart failure/cyanosis; nutritional and perioperative contributors coexist. | HP:0001508 |
| Neurodevelopmental impairment | Variable deficits in motor, language, attention, executive function, and academic achievement, particularly after critical neonatal CHD. | HP:0012758; HP:0001263 |

Frequencies cannot be assigned across “CHD” as a whole because each lesion defines a different denominator. Severity ranges from clinically silent to lethal without neonatal intervention. Quality-of-life impact reflects not only anatomy but also surgeries, exercise capacity, neurodevelopment, mental health, socioeconomic access, and transition to adult care.

## 4. Genetic and molecular information

### Inheritance and penetrance

Inheritance may be autosomal dominant, autosomal recessive, X-linked, chromosomal, or multifactorial. Dominant developmental-gene disorders often show incomplete penetrance and variable expressivity; recessive laterality/cilia disorders are enriched in consanguineous populations; **ZIC3** causes X-linked heterotaxy in some families. De novo variants are important in severe sporadic/syndromic CHD. Parental and germline mosaicism can produce recurrence despite negative parental blood testing. Anticipation is not a general feature. Founder variants exist for particular syndromes/populations, but there is no single CHD founder allele or carrier frequency.

### Functional mechanisms

* **Transcription-factor haploinsufficiency:** NKX2-5, GATA4/6, TBX5/20, and TBX1 disturb specification, chamber formation, septation, or conduction-system development.
* **Signaling defects:** NOTCH/JAG1, BMP/TGF-β, WNT, RAS–MAPK, and NODAL pathways alter progenitor fate, endocardial cushion formation, outflow tract patterning, valve development, or left–right asymmetry.
* **Chromatin/epigenetic regulation:** CHD7, KMT2D, and other chromatin regulators change developmental gene accessibility; pathogenic mechanisms are usually germline and developmental rather than somatic.
* **Contractile/cytoskeletal dysfunction:** MYH6, ACTC1, MYH7, MYBPC3, and TNNT2 can connect structural malformation with myocardial dysfunction.
* **Cilia/laterality:** ZIC3, NODAL, GDF1, MMP21, and ciliary genes disrupt left–right organizer function and produce heterotaxy.

Routine databases may label variants pathogenic, likely pathogenic, VUS, likely benign, or benign. VUS should not guide irreversible surgery, prenatal decision-making, or predictive testing. Somatic variants are not a principal established cause of ordinary CHD, although somatic mosaicism is biologically plausible and increasingly detectable with deep sequencing.

### Chromosomal abnormalities

Clinically important abnormalities include whole-chromosome aneuploidies and recurrent CNVs such as 22q11.2 deletion and 7q11.23 deletion. Structural rearrangements, mosaic aneuploidy, and nonrecurrent CNVs also occur. CMA therefore remains valuable even when examination suggests isolated CHD: one infant cohort found diagnostic CMA in 6.5% of apparently isolated cases. (helm2021geneticevaluationof pages 1-2)

## 5. Environmental information

The most consequential exposure window is early organogenesis, approximately gestational weeks 3–8. Maternal diabetes can expose the embryo to hyperglycemia, oxidative stress, and altered signaling; retinoids and antiepileptics can perturb transcriptional programs; rubella can produce a congenital infection syndrome with patent ductus arteriosus and pulmonary-artery stenosis. Air pollution, solvents, pesticides, smoking, and alcohol have epidemiologic associations of varying consistency. (zubrzycki2024cardiacdevelopmentand pages 25-26)

CHD is **not infectious or transmissible**. Rubella is an upstream teratogenic infection, not an infection acquired from the affected infant. Exercise by the mother is not established as a lesion-specific protective intervention, although general preconception health is beneficial.

## 6. Mechanism and pathophysiology

### Upstream developmental chain

1. **Trigger:** pathogenic variant/CNV/aneuploidy, maternal exposure, or combined susceptibility.
2. **Developmental perturbation:** altered chromatin, transcription-factor dosage, WNT/BMP/NOTCH/TGF-β/RAS–MAPK/NODAL signaling, metabolism, or ciliary left–right patterning.
3. **Cellular effect:** abnormal proliferation, migration, differentiation, epithelial-to-mesenchymal transition, neural-crest contribution, myocardialization, or apoptosis.
4. **Morphogenetic failure:** defective looping, septation, endocardial cushions, valves, outflow tract, arch, venous return, or ventricular growth.
5. **Clinical physiology:** left-to-right shunt, obstruction, mixing/cyanosis, regurgitation, or single-ventricle circulation.
6. **Downstream remodeling:** pressure/volume load, hypoxemia, neurohormonal activation, endothelial dysfunction, pulmonary vascular remodeling, hypertrophy, fibrosis, arrhythmia, and heart failure.

Suggested GO terms include **heart development GO:0007507**, **heart looping GO:0001947**, **cardiac septum morphogenesis GO:0060916**, **Notch signaling GO:0007219**, **BMP signaling GO:0030509**, **Wnt signaling GO:0016055**, **epithelial-to-mesenchymal transition GO:0001837**, **neural-crest-cell migration GO:0001755**, **mitochondrial respiratory-chain complex assembly GO:0033108**, and **response to oxidative stress GO:0006979**.

Relevant Cell Ontology concepts include cardiomyocyte **CL:0000746**, endothelial cell **CL:0000115**, fibroblast **CL:0000057**, neural crest cell **CL:0000333/ontology release-dependent**, endocardial cell, epicardial cell **CL:0002494**, and cardiac progenitor cell.

### Molecular profiling and advanced technologies

A 2024 single-cell/machine-learning analysis used 21,034 fibroblasts, 73,296 cardiomyocytes, and 35,673 endothelial cells. Candidate cell-type signatures included FOXO3 in fibroblasts; TMTC1, ART3, ARHGAP24, SHROOM3, and XIST in cardiomyocyte analyses; and COL25A1, NFIB, and KLF7 in endothelial analyses. These are computational biomarkers requiring independent biological and prospective clinical validation. (ma2024machinelearningin pages 2-3, ma2024machinelearningin pages 21-23)

Patient-specific iPSC cardiomyocytes are being used to model TOF, single-ventricle disease, and HLHS. HLHS models have shown mitochondrial dysfunction, oxidative stress, abnormal unfolded-protein responses, sarcomere defects, and impaired contractility. CRISPR correction of **MYH6-R443P** rescued sarcomeric and contractile phenotypes in vitro; sildenafil and tauroursodeoxycholic acid emerged as experimental pathway-directed candidates, not established HLHS treatments. (pushpan2024ipscderivedcardiomyocytesas pages 10-11)

Perioperative metabolomics is another emerging application. A 2024 systematic review included seven studies and 509 children and found associations of amino-acid/fatty-acid-related profiles with mortality, acute kidney injury, and neurologic outcomes, but heterogeneity and small samples preclude clinical biomarker adoption. One included neonatal dataset sampled 149 infants around cardiopulmonary bypass. (meggiolaro2024metabolomicprofilingof pages 4-5)

## 7. Anatomical structures affected

The primary organ is the **heart (UBERON:0000948)**, including atria, ventricles, interatrial/interventricular septa, endocardial cushions, valves, myocardium, endocardium, epicardium, and conduction system. Great-vessel sites include the aorta **UBERON:0000947**, pulmonary trunk/arteries, arterial duct, aortic arch, systemic veins, and pulmonary veins. Laterality can be normal, mirror-imaged, or discordant/asymmetric in heterotaxy.

Secondary organ injury involves lungs/pulmonary vasculature, liver and lymphatics after Fontan circulation, kidneys after low output or bypass, brain through fetal dysmaturation/hypoxemia/embolism, and intestine through low perfusion. Subcellular compartments include nucleus/chromatin, primary cilia, mitochondria, sarcomere, intercellular junctions, and endoplasmic reticulum. Chromosomal disease can additionally involve immune, endocrine, craniofacial, renal, skeletal, auditory, and neurodevelopmental systems. (salzillo2024cardiovasculardiseasesin pages 13-15, pushpan2024ipscderivedcardiomyocytesas pages 10-11)

## 8. Temporal development and natural history

CHD originates in embryogenesis and is therefore congenital, even when diagnosis is delayed. Critical duct-dependent lesions often deteriorate acutely when the ductus arteriosus closes during the first days of life. Large shunts tend to produce heart failure over weeks as pulmonary vascular resistance falls. Small septal defects may remain stable or close spontaneously.

Surgery usually repairs or palliates anatomy but does not remove lifelong risk. Intermediate and late stages may include residual shunts/obstruction, valve dysfunction, ventricular failure, aortopathy, pulmonary hypertension, arrhythmia, endocarditis, thrombosis, protein-losing enteropathy, plastic bronchitis, Fontan-associated liver disease, and transplant consideration. There is no general spontaneous remission category; lesion-specific closure of small defects is the main exception. Critical intervention windows include prenatal recognition, delivery planning, prostaglandin initiation before ductal closure, neonatal repair/palliation, and structured adolescent transition.

## 9. Inheritance and population epidemiology

CHD affects approximately 1% of live-born infants in commonly used definitions; ascertainment, inclusion of mild defects, prenatal loss, and access to echocardiography drive geographic differences. (helm2021geneticevaluationof pages 1-2, peterlin2024thegeneticarchitecture pages 10-12)

Sex distribution is lesion-specific rather than uniformly male or female: left-sided obstructive lesions and TGA are more common in males, while atrial septal defects and patent ductus arteriosus are often more common in females. Ethnic/racial differences partly reflect genetic background but also maternal risk, prenatal detection, termination practices, socioeconomic conditions, referral, and registry completeness. Resource-limited regions experience disproportionate preventable mortality because fetal diagnosis, pediatric surgery, catheter care, and lifelong specialist follow-up are less available. (salzillo2024cardiovasculardiseasesin pages 15-16, salzillo2024cardiovasculardiseasesin pages 13-15)

Empiric recurrence after an isolated nonsyndromic CHD is usually a few percent but varies by lesion and family history; a known Mendelian or chromosomal diagnosis replaces the empirical estimate with disorder-specific counseling. Incomplete penetrance and variable expressivity are common. Consanguinity increases recessive forms, particularly laterality/cilia disorders.

## 10. Diagnostics

### Clinical and imaging approach

* **Prenatal:** screening obstetric ultrasound with outflow-tract views; fetal echocardiography for abnormal screening, family history, maternal diabetes/teratogen exposure, increased nuchal translucency, fetal genetic abnormality, or extracardiac malformation. Prenatal CMA and sequencing are considered when CHD is detected, particularly with extracardiac findings.
* **Newborn:** physical examination, pre-/postductal oxygen saturation, pulse assessment, blood pressure when indicated, and universal pulse-oximetry screening for critical CHD where implemented. A normal screen does not exclude coarctation or noncyanotic disease.
* **Definitive anatomy:** transthoracic echocardiography is first line; transesophageal/intracardiac echo supports interventions.
* **CMR:** quantifies chamber volumes, ventricular function, flow, shunts, fibrosis, edema, and complex postoperative anatomy without ionizing radiation. Limitations include expertise, scan time, device compatibility, breath holding, and anesthesia in younger children.
* **CT/catheterization:** CT offers rapid high-resolution vascular/coronary anatomy at the cost of radiation/contrast; catheterization supplies invasive hemodynamics and permits intervention.
* **Functional surveillance:** ECG, ambulatory monitoring, exercise testing, cardiopulmonary exercise testing, and laboratory markers such as BNP/NT-proBNP in selected heart-failure contexts.

Prenatal screening, fetal echocardiography, genomic testing, postoperative monitoring, and molecular autopsy are emphasized for chromosomal/sudden-death-risk CHD. (salzillo2024cardiovasculardiseasesin pages 13-15)

### Genetic testing

A practical sequence is: detailed three-generation pedigree and dysmorphology/extracardiac assessment; rapid aneuploidy testing or karyotype when suspected; **CMA** for severe/syndromic CHD; then phenotype-guided panel or preferably trio WES/WGS when CMA is nondiagnostic. FISH remains useful for targeted confirmation/family studies but should not substitute for genome-wide CNV testing. Mitochondrial testing is indicated only where phenotype supports it; repeat-expansion testing is not routine CHD testing.

In 440 infants, CMA yield was 14.6% and combined testing yield 17%; LV outflow-tract obstruction had 15.8% yield among apparently isolated cases. In a 2024 cohort of 188 neonates, 17% received one of 22 genetic diagnoses, CMA yield was 10.1%, and VUS were found in 4.8%. Reported WGS yield reached 27% in a cited implementation, with management changed in 62% of diagnosed cases. (helm2021geneticevaluationof pages 1-2, peterlin2024thegeneticarchitecture pages 10-12)

RNA-seq, methylation episignatures, optical genome mapping, long-read sequencing, proteomics, and metabolomics remain second-line or research tools. They are useful for splice confirmation, cryptic structural variation, syndrome resolution, and biomarker discovery, but are not substitutes for anatomic diagnosis.

### Differential diagnosis

Important alternatives include persistent pulmonary hypertension of the newborn, neonatal sepsis, respiratory disease, cardiomyopathy, arrhythmia/channelopathy without malformation, innocent murmur, acquired valvular disease, and extracardiac causes of cyanosis or failure to thrive. Echocardiographic anatomy distinguishes these from structural CHD.

## 11. Outcomes and prognosis

Prognosis is lesion-, era-, center-, genotype-, comorbidity-, and access-dependent; one pooled “five-year survival” is misleading. Small isolated defects can confer normal lifespan. Critical/single-ventricle disease has substantial neonatal risk and chronic morbidity despite successful palliation. Trisomies 13 and 18 generally carry worse early prognosis than trisomy 21, while outcomes within every genetic category remain heterogeneous. (salzillo2024cardiovasculardiseasesin pages 15-16)

Important adverse prognostic factors include complex anatomy, single-ventricle physiology, ventricular dysfunction, pulmonary hypertension, cyanosis, arrhythmia, residual hemodynamic lesions, multiple sternotomies, extracardiac/genetic disease, prematurity/low birth weight, renal injury, socioeconomic disadvantage, and interrupted specialist care. In CHD cohorts, SCD incidence of 0.28–2.7% annually and TOF estimates of 0.9–1.5% annually underscore the need for lifelong rhythm and hemodynamic surveillance. (salzillo2024cardiovasculardiseasesin pages 10-11)

Morbidity includes exercise limitation, heart failure, stroke/thromboembolism, endocarditis, repeat procedures, pregnancy risk, neurodevelopmental disability, anxiety/depression, educational/employment effects, and caregiver burden. Quality of life can remain good despite complex anatomy but is generally worse with functional limitation, repeated intervention, pain/trauma, and poor access. Lesion-specific PROMIS, PedsQL, SF-36, EQ-5D, and disease-specific adult-CHD instruments should be stored with age and anatomy rather than pooled indiscriminately.

## 12. Treatment

### Lesion-directed intervention

* **Septal defects/ductus:** observation when small; transcatheter closure or surgical repair for significant shunt, chamber dilation, symptoms, or selected endocarditis risk.
* **Valve/outflow obstruction:** balloon valvuloplasty, catheter stenting, surgical valvotomy/reconstruction, or valve replacement depending on anatomy.
* **Coarctation:** surgery or catheter stent, with lifelong hypertension/aortic surveillance.
* **TGA:** prostaglandin E1 to maintain ductal patency, balloon atrial septostomy when mixing is inadequate, and neonatal arterial-switch operation.
* **TOF:** complete repair, later pulmonary-valve replacement when indicated, and rhythm surveillance.
* **HLHS/single ventricle:** prostaglandin stabilization followed by staged Norwood, bidirectional Glenn, and Fontan palliation, hybrid strategies, transplant, or individualized comfort care.

Suggested NCIt concepts include **Cardiac Surgical Procedure**, **Cardiac Catheterization**, **Balloon Valvuloplasty**, **Norwood Procedure**, **Glenn Procedure**, **Fontan Procedure**, **Heart Transplantation**, and **Implantable Cardioverter Defibrillator**. Current modalities span open surgery, catheterization, balloon valvuloplasty, staged single-ventricle operations, drug therapy, ICDs, and transplant. (salzillo2024cardiovasculardiseasesin pages 13-15, ma2024machinelearningin pages 2-3)

### Pharmacotherapy and supportive care

Drugs generally manage physiology or complications rather than correcting the malformation: prostaglandin E1 for duct-dependent circulation; diuretics and selected ACE inhibitors/beta blockers for heart failure; pulmonary vasodilators for carefully characterized pulmonary vascular disease; antiarrhythmics and anticoagulants/antiplatelets for indicated rhythm/thrombotic risks; antibiotics for established infection and narrowly defined endocarditis prophylaxis. No universal CHD pharmacogenomic algorithm exists.

Nutritional support, developmental surveillance, neuropsychology, exercise prescription/cardiac rehabilitation, dental care, reproductive counseling, pregnancy management, and structured transition to adult congenital cardiology are integral. Physical activity should be individualized; blanket restriction is often harmful.

### Experimental and precision approaches

CRISPR correction, gene replacement, RNA therapeutics, regenerative cell therapy, engineered valves, and tissue-engineered conduits remain experimental for most CHD. iPSC rescue of MYH6-associated dysfunction is proof of mechanism, not clinical gene therapy. (pushpan2024ipscderivedcardiomyocytesas pages 10-11)

Examples of current real-world research include the recruiting lifecycle registry **NCT06611787**, designed for approximately 100,000 patients across more than 20 hospitals with fetal-to-adult data, biospecimens, reoperation, and long-term survival outcomes; the Swiss adult registry **NCT02258724**; fetal complex-CHD multi-omics **NCT06705543**; and personalized non-invasive electrocardiographic imaging **NCT07425132**. The Beijing registry began recruitment in February 2024 and plans extended longitudinal follow-up. (NCT06611787 chunk 1)

## 13. Prevention

* **Primary:** preconception diabetes and phenylketonuria control; healthy maternal weight; folic acid according to public-health guidance; rubella vaccination before pregnancy; medication/teratogen review; avoidance of smoking, alcohol, and illicit drugs; occupational/environmental protection. These measures reduce risk but cannot prevent most CHD. (zubrzycki2024cardiacdevelopmentand pages 25-26)
* **Secondary:** prenatal ultrasound/fetal echocardiography, prenatal genetics, planned delivery at an appropriate center, newborn examination and pulse oximetry, prompt echocardiography, and cascade testing when a familial diagnosis is found.
* **Tertiary:** timely repair/palliation, residual-lesion and arrhythmia surveillance, vaccination, dental hygiene, selective endocarditis prophylaxis, exercise/weight management, neurodevelopmental services, contraception/pregnancy counseling, and uninterrupted congenital-cardiology follow-up.

Preimplantation or prenatal genetic testing is feasible when a pathogenic familial variant or chromosomal rearrangement is known. It is much less informative for unexplained multifactorial CHD. Genetic counseling must discuss variable expressivity, incomplete penetrance, residual risk, and the difference between detecting a genotype and predicting lesion severity.

## 14. Other species and natural disease

Naturally occurring septal defects, patent ductus arteriosus, pulmonic stenosis, subaortic stenosis, TOF, valve dysplasia, and vascular-ring anomalies occur in dogs, cats, horses, cattle, and other vertebrates. Domestic dog (**NCBI Taxon 9615**) and cat (**9685**) are the principal companion-animal contexts; breed predispositions suggest heritable susceptibility, but breed–variant claims should be taken from OMIA/VBO records for the precise lesion rather than generalized to CHD.

Veterinary CHD is non-zoonotic and not cross-species transmissible. Comparative relevance derives from conserved cardiac development, hemodynamics, and orthologs—not infection. Spontaneous animal cases can better model anatomical scale and catheter/surgical procedures than rodents, although breed structure and incomplete genotyping limit direct human inference.

## 15. Model organisms and experimental systems

* **Mouse, Mus musculus (Taxon 10090):** knockout/knock-in, conditional, and chromosomal-synteny models reproduce septation, valve, outflow-tract, arch, and laterality defects. A 2024 Down-syndrome model showed that three copies of **Dyrk1a** impaired cardiomyocyte proliferation and mitochondrial respiration; restoring two copies rescued septation, and prenatal DYRK1A inhibition partially reversed transcriptional abnormalities. This is strong model-organism mechanistic evidence but not yet a safe prenatal human therapy.
* **Zebrafish, Danio rerio (Taxon 7955):** rapid, transparent embryos and efficient CRISPR permit high-throughput assessment of looping, chamber patterning, contractility, and laterality. Limitations include a two-chamber heart and important differences in septation and placental/maternal physiology.
* **Human iPSC cardiomyocytes:** preserve patient genotype and permit isogenic CRISPR controls, functional phenotyping, and drug screening. They incompletely reproduce mature myocardium, multicellular anatomy, loading, circulation, and whole-organ morphogenesis. Recent CHD models have combined WES, RNA-seq, and single-cell transcriptomics. (pushpan2024ipscderivedcardiomyocytesas pages 10-11)
* **Cardiac organoids and engineered tissues:** model interactions among myocardium, endocardium, epicardium, vascular cells, and foregut-like tissues. They are promising for developmental toxicology and spatial multi-omics but currently lack complete four-chamber anatomy, mature conduction, physiologic perfusion, and maternal–placental context.
* **Chick and Xenopus:** valuable for neural-crest migration, looping, microsurgery, and lineage tracing; translation is constrained by species-specific anatomy.

## Recent developments and expert interpretation, 2023–2024

1. **Broader genomic testing:** recent neonatal data support CMA plus sequencing rather than restricting testing to obviously dysmorphic infants. Expert interpretation is that phenotypic examination alone lacks sufficient sensitivity; nevertheless, the lower yield in isolated CHD means counseling should anticipate nondiagnostic and VUS results. (helm2021geneticevaluationof pages 1-2, peterlin2024thegeneticarchitecture pages 10-12)
2. **Cell-resolved molecular maps:** single-cell sequencing and machine learning now resolve cardiomyocyte, endothelial, and fibroblast signatures, but retrospective classification performance is not equivalent to a clinically validated biomarker. (ma2024machinelearningin pages 2-3, ma2024machinelearningin pages 21-23)
3. **Patient-specific disease modeling:** iPSC/CRISPR systems can test causality and rescue individual cellular defects. Their immediate application is mechanism and drug prioritization rather than clinical genome editing. (pushpan2024ipscderivedcardiomyocytesas pages 10-11)
4. **Metabolomic risk stratification:** perioperative signatures may help forecast kidney, neurologic, and mortality outcomes, but current evidence is too heterogeneous and small for routine use. (meggiolaro2024metabolomicprofilingof pages 4-5)
5. **Lifecycle registries and digital surveillance:** very large registries, wearables, and non-invasive electrical imaging aim to connect fetal anatomy, genotype, operations, adult complications, and patient-reported outcomes. Equity and international standardization remain major implementation challenges. (salzillo2024cardiovasculardiseasesin pages 15-16, NCT06611787 chunk 1)

## Selected exact abstract statements and source metadata

* Helm et al., *Genes*, published August 2021, DOI: https://doi.org/10.3390/genes12081244: “Cumulative evidence provides a rationale for comprehensive, standardized genetic evaluation in infants with severe CHDs regardless of lesion or extracardiac anomalies.” The study reported CMA yield of 14.6% and overall genetic-testing yield of 17%. (helm2021geneticevaluationof pages 1-2)
* Peterlin et al., *Life*, published September 2024, DOI: https://doi.org/10.3390/life14091118: “We established the genetic diagnosis of 22 distinct syndromes in 17% (32/188) of neonates.” (peterlin2024thegeneticarchitecture pages 10-12)
* Ma et al., *Life*, published August 2024, DOI: https://doi.org/10.3390/life14081032: the study states that it analyzed “21,034 cardiac fibroblasts, 73,296 cardiomyocytes, and 35,673 endothelial cells,” illustrating the scale of emerging cell-resolved CHD profiling. (ma2024machinelearningin pages 2-3, ma2024machinelearningin pages 21-23)
* Meggiolaro et al., *Frontiers in Cardiovascular Medicine*, published November 2024, DOI: https://doi.org/10.3389/fcvm.2024.1491046: “Seven studies involving 509 children … were included,” and the authors judged the findings promising but limited by heterogeneous designs and small samples. (meggiolaro2024metabolomicprofilingof pages 4-5)

PMIDs were not consistently exposed in the retrieved records; DOI URLs are therefore supplied for the principal recent sources rather than risking incorrect PMID assignment. Evidence labels should distinguish human cohorts/registries, systematic reviews, computational single-cell analyses, in-vitro iPSC experiments, and model-organism studies. The principal knowledge-base caveat is that CHD is a heterogeneous umbrella category: lesion-, genotype-, age-, and procedure-specific facts should be stored separately whenever possible.

References

1. (helm2021geneticevaluationof pages 1-2): Benjamin M. Helm, Benjamin J. Landis, and Stephanie M. Ware. Genetic evaluation of inpatient neonatal and infantile congenital heart defects: new findings and review of the literature. Genes, 12:1244, Aug 2021. URL: https://doi.org/10.3390/genes12081244, doi:10.3390/genes12081244. This article has 35 citations.

2. (peterlin2024thegeneticarchitecture pages 10-12): Ana Peterlin, Sara Bertok, Karin Writzl, Luca Lovrečić, Aleš Maver, Borut Peterlin, Maruša Debeljak, and Gregor Nosan. The genetic architecture of congenital heart disease in neonatal intensive care unit patients—the experience of university medical centre, ljubljana. Life, 14:1118, Sep 2024. URL: https://doi.org/10.3390/life14091118, doi:10.3390/life14091118. This article has 3 citations.

3. (salzillo2024cardiovasculardiseasesin pages 10-11): Cecilia Salzillo, Marco La Verde, Amalia Imparato, Rossella Molitierno, Stefano Lucà, Francesca Pagliuca, and Andrea Marzullo. Cardiovascular diseases in public health: chromosomal abnormalities in congenital heart disease causing sudden cardiac death in children. Medicina, 60:1976, Dec 2024. URL: https://doi.org/10.3390/medicina60121976, doi:10.3390/medicina60121976. This article has 15 citations.

4. (ma2024machinelearningin pages 2-3): Qinglan Ma, Yu-Hang Zhang, Wei Guo, Kaiyan Feng, Tao Huang, and Yu-Dong Cai. Machine learning in identifying marker genes for congenital heart diseases of different cardiac cell types. Life, 14:1032, Aug 2024. URL: https://doi.org/10.3390/life14081032, doi:10.3390/life14081032. This article has 9 citations.

5. (OpenTargets Search: congenital heart disease): Open Targets Query (congenital heart disease, 33 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

6. (salzillo2024cardiovasculardiseasesin pages 13-15): Cecilia Salzillo, Marco La Verde, Amalia Imparato, Rossella Molitierno, Stefano Lucà, Francesca Pagliuca, and Andrea Marzullo. Cardiovascular diseases in public health: chromosomal abnormalities in congenital heart disease causing sudden cardiac death in children. Medicina, 60:1976, Dec 2024. URL: https://doi.org/10.3390/medicina60121976, doi:10.3390/medicina60121976. This article has 15 citations.

7. (zubrzycki2024cardiacdevelopmentand pages 25-26): Marek Zubrzycki, Rene Schramm, Angelika Costard-Jäckle, Jochen Grohmann, Jan F. Gummert, and Maria Zubrzycka. Cardiac development and factors influencing the development of congenital heart defects (chds): part i. International Journal of Molecular Sciences, 25:7117, Jun 2024. URL: https://doi.org/10.3390/ijms25137117, doi:10.3390/ijms25137117. This article has 42 citations.

8. (ma2024machinelearningin pages 21-23): Qinglan Ma, Yu-Hang Zhang, Wei Guo, Kaiyan Feng, Tao Huang, and Yu-Dong Cai. Machine learning in identifying marker genes for congenital heart diseases of different cardiac cell types. Life, 14:1032, Aug 2024. URL: https://doi.org/10.3390/life14081032, doi:10.3390/life14081032. This article has 9 citations.

9. (pushpan2024ipscderivedcardiomyocytesas pages 10-11): Chithra K. Pushpan and Subramanyan Ram Kumar. Ipsc-derived cardiomyocytes as a disease model to understand the biology of congenital heart defects. Cells, 13:1430, Aug 2024. URL: https://doi.org/10.3390/cells13171430, doi:10.3390/cells13171430. This article has 4 citations.

10. (meggiolaro2024metabolomicprofilingof pages 4-5): Leonardo Meggiolaro, Laura Moschino, Matteo Stocchero, Giuseppe Giordano, Vladimiro Vida, Giovanni Di Salvo, and Eugenio Baraldi. Metabolomic profiling of infants undergoing cardiopulmonary bypass and association with clinical outcomes: a systematic review. Frontiers in Cardiovascular Medicine, Nov 2024. URL: https://doi.org/10.3389/fcvm.2024.1491046, doi:10.3389/fcvm.2024.1491046. This article has 4 citations and is from a peer-reviewed journal.

11. (NCT06611787 chunk 1):  A Comprehensive Registry Study of the Whole Life Cycle of Patients With CHD. Beijing Anzhen Hospital. 2024. ClinicalTrials.gov Identifier: NCT06611787

12. (salzillo2024cardiovasculardiseasesin pages 15-16): Cecilia Salzillo, Marco La Verde, Amalia Imparato, Rossella Molitierno, Stefano Lucà, Francesca Pagliuca, and Andrea Marzullo. Cardiovascular diseases in public health: chromosomal abnormalities in congenital heart disease causing sudden cardiac death in children. Medicina, 60:1976, Dec 2024. URL: https://doi.org/10.3390/medicina60121976, doi:10.3390/medicina60121976. This article has 15 citations.

## Artifacts

- [Edison artifact artifact-00](Congenital_Heart_Disease-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 7 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.