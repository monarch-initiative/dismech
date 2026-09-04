---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-25T20:45:35.222650'
end_time: '2026-08-25T20:57:40.733089'
duration_seconds: 725.51
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Immunodeficiency 61
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 10
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 1
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Immunodeficiency_61-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Immunodeficiency 61
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 61** covering all of the
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
- **Disease Name:** Immunodeficiency 61
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Immunodeficiency 61** covering all of the
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


# Immunodeficiency 61 (SH3KBP1/CIN85 deficiency): comprehensive disease-characteristics report

**Evidence cutoff and interpretation.** Immunodeficiency 61 is an ultra-rare, X-linked, predominantly antibody deficiency caused by loss of **SH3KBP1**, encoding the adaptor CIN85. The disease-specific human literature remains essentially one 2018 family with two affected brothers. Consequently, frequencies below are “2/2” or “1/2” observations, not population estimates, and many management recommendations must be extrapolated from primary antibody-deficiency practice rather than regarded as proven specifically for this disorder. The defining article was published online **10 April 2018**: Keller et al., *Journal of Experimental Medicine* 215:1327–1336, DOI/URL: https://doi.org/10.1084/jem.20170534. (kellerUnknownyeargövip18prof.dr. pages 1-4, kellerUnknownyeargövip18prof.dr. pages 4-5)

## Executive evidence summary

| domain | established finding | quantitative detail | evidence type/strength |
|---|---|---|---|
| Disease definition | Immunodeficiency 61 corresponds to SH3KBP1/CIN85 deficiency, an X-linked primary antibody deficiency caused by germline loss of CIN85/SH3KBP1 | Human evidence currently centers on 1 family with 2 affected male siblings and an asymptomatic carrier mother (kellerUnknownyeargövip18prof.dr. pages 1-4, kellerUnknownyeargövip18prof.dr. pages 4-5) | Human primary disease report; strong for gene-disease link but very limited case count (kellerUnknownyeargövip18prof.dr. pages 1-4, kellerUnknownyeargövip18prof.dr. pages 4-5) |
| Causal gene/locus | SH3KBP1 (CIN85) deletion on chromosome Xp22.12 abolishes prevalent CIN85 transcript/protein expression | 247.5-kbp deletion, exons 2-6, GRCh37 position 19,667,630-19,886,572; adjacent genes unaffected (kellerUnknownyeargövip18prof.dr. pages 4-5) | Human genomic + protein evidence; strong (kellerUnknownyeargövip18prof.dr. pages 4-5) |
| Inheritance | X-linked transmission | 2 affected hemizygous males; mother hemizygous carrier without clinical symptoms; healthy half-brother negative for deletion (kellerUnknownyeargövip18prof.dr. pages 4-5) | Human pedigree evidence; strong within single family (kellerUnknownyeargövip18prof.dr. pages 4-5) |
| Patient 1 demographics | Surviving index case | Male, age 12 years at report; diagnosed genetically after evaluation of antibody deficiency (kellerUnknownyeargövip18prof.dr. pages 4-5) | Human case report; strong (kellerUnknownyeargövip18prof.dr. pages 4-5) |
| Patient 2 demographics/outcome | More severe affected brother | Male; died at age 15 years, 3 years before report (kellerUnknownyeargövip18prof.dr. pages 4-5) | Human family history/archived DNA; moderate-strong (kellerUnknownyeargövip18prof.dr. pages 4-5) |
| Immunoglobulins: patient 1 | Selective hypogammaglobulinemia affecting IgM and IgG subclasses with preserved total IgG/IgA | IgM 16 mg/dL (ref 48-228); IgG2 55 mg/dL (110-485); IgG4 <0.8 mg/dL (5.2-196); IgG3 60 mg/dL (24-116); IgG1 595 mg/dL (370-910); IgA 79 mg/dL (40-238); total IgG 918 mg/dL (672-1,536) (kellerUnknownyeargövip18prof.dr. pages 5-7) | Human laboratory evidence; strong (kellerUnknownyeargövip18prof.dr. pages 5-7) |
| Immunoglobulins: patient 2 | More profound pan-hypogammaglobulinemia than patient 1 | Serum IgM and IgG2/4 diminished; total IgG and IgA below detection limits (kellerUnknownyeargövip18prof.dr. pages 4-5) | Human retrospective clinical data; moderate (kellerUnknownyeargövip18prof.dr. pages 4-5) |
| Vaccine response | Defective polysaccharide antibody responses with preserved peptide response | Pneumococcal IgG response insufficient against 8/9 serotypes; serotype-specific IgM reached suggested cutoff for only 8/10 serotypes; anti-tetanus-toxoid response normal (kellerUnknownyeargövip18prof.dr. pages 4-5, kellerUnknownyeargövip18prof.dr. pages 5-7) | Human functional clinical immunology; strong (kellerUnknownyeargövip18prof.dr. pages 4-5, kellerUnknownyeargövip18prof.dr. pages 5-7) |
| Infections/clinical course: patient 1 | Early-childhood severe bacterial infections, then partial clinical improvement | Severe infections especially in winter months until age 4; no obvious compromised immune reactions thereafter, despite persistent laboratory defect (kellerUnknownyeargövip18prof.dr. pages 4-5) | Human longitudinal case history; moderate-strong (kellerUnknownyeargövip18prof.dr. pages 4-5) |
| Infections/clinical course: patient 2 | Persistent susceptibility to recurrent sinopulmonary infection with fatal outcome | Repetitive sinusitis, otitis media, and pneumonia; died of septic shock and multiorgan failure subsequent to bilateral pneumonia at age 15 (kellerUnknownyeargövip18prof.dr. pages 4-5) | Human case history; strong for severe phenotype (kellerUnknownyeargövip18prof.dr. pages 4-5) |
| Additional reported features | Possible neurobehavioral/constitutional features, uncertain causality | Both brothers reportedly had moderate ADHD, mildly impaired adaptive skills, and obesity at age 11; causal relation to CIN85 deficiency not established (kellerUnknownyeargövip18prof.dr. pages 5-7) | Human observational note; weak/uncertain disease attribution (kellerUnknownyeargövip18prof.dr. pages 5-7) |
| B-cell numbers/phenotype | Peripheral B-cell development largely preserved despite antibody deficiency | B cells 5.3% and 165/µL (ref 7.8-23.7%, 119-578/µL); transitional B cells 5.9%/10 µL; naive B cells 83.6%/138 µL; IgM/IgD memory 4.6%/8 µL; IgM-only memory 0.1%/1 µL; IgG-switched memory 2.5%/4 µL; IgA-switched memory 1.1%/2 µL; plasmablasts 0.3%; CD21low 1.7%; kappa/lambda 1.2 (kellerUnknownyeargövip18prof.dr. pages 5-7, kellerUnknownyeargövip18prof.dr. pages 7-9) | Human flow-cytometry evidence; strong (kellerUnknownyeargövip18prof.dr. pages 5-7, kellerUnknownyeargövip18prof.dr. pages 7-9) |
| T/NK-cell phenotype | T-cell and NK-cell compartments grossly intact | CD4 40%/1,245 µL; CD8 26.2%/815 µL; NK 8.7%; normal CD4 subpopulations including recent thymic emigrants and Tregs; terminally differentiated CD8 cells slightly reduced at 3.7%/30 µL (ref 9-65%, 35-420/µL) (kellerUnknownyeargövip18prof.dr. pages 5-7, kellerUnknownyeargövip18prof.dr. pages 9-10) | Human flow-cytometry evidence; strong (kellerUnknownyeargövip18prof.dr. pages 5-7, kellerUnknownyeargövip18prof.dr. pages 9-10) |
| BCR proximal signaling | CIN85-negative primary B cells show reduced BCR-driven calcium signaling but preserved ERK and PI3K-S6 signaling | Ca2+ flux consistently moderately reduced; inducible ERK phosphorylation normal; robust S6 phosphorylation preserved (kellerUnknownyeargövip18prof.dr. pages 7-9) | Human ex vivo signaling assays; strong (kellerUnknownyeargövip18prof.dr. pages 7-9) |
| NF-kB signaling in B cells | Key disease mechanism is selective failure to couple BCR signaling to canonical NF-kB activation | Very few patient B cells degraded IκBα after 40 min of BCR ligation vs majority of controls; reduced p65 phosphorylation; prolonged BCR stimulation did not substantially improve IκBα degradation; BclXL induction after BCR stimulation compromised (kellerUnknownyeargövip18prof.dr. pages 7-9) | Human ex vivo mechanistic evidence; strong (kellerUnknownyeargövip18prof.dr. pages 7-9) |
| Stimulus specificity | Defect is selective for BCR pathway rather than global B-cell activation failure | NF-kB activation after TLR9 ligation, CD40 stimulation, or PMA treatment was intact; TLR9/CD40 also preserved for plasmablast differentiation, class switching, and proliferation in vitro (kellerUnknownyeargövip18prof.dr. pages 7-9, kellerUnknownyeargövip18prof.dr. pages 9-10) | Human ex vivo functional evidence; strong (kellerUnknownyeargövip18prof.dr. pages 7-9, kellerUnknownyeargövip18prof.dr. pages 9-10) |
| B-cell activation markers | Surface activation responses downstream of BCR are selectively impaired | BCR-induced CD86 and ICAM-1 up-regulation diminished; CD69 and CD25 only moderately affected; TLR9/CD40 responses similar to controls (kellerUnknownyeargövip18prof.dr. pages 7-9) | Human ex vivo functional evidence; strong (kellerUnknownyeargövip18prof.dr. pages 7-9) |
| T-cell function | No obvious intrinsic T-cell activation defect demonstrated | Naive and memory CD4 T cells showed normal Ca2+ flux and NF-kB activation after TCR/CD28 stimulation; CD69, CD25, ICOS up-regulation normal; IL-4, IFN-γ, IL-17 production and CD4/CD8 proliferation preserved (kellerUnknownyeargövip18prof.dr. pages 9-10) | Human ex vivo functional evidence; strong (kellerUnknownyeargövip18prof.dr. pages 9-10) |
| Mechanistic interpretation | Humoral deficiency is attributed mainly to B-cell intrinsic signaling defects rather than defective T-cell help | Authors conclude poor antigen reactivity of B cells underlies antibody deficiency; hypogammaglobulinemia unlikely due to insufficient T-cell help (kellerUnknownyeargövip18prof.dr. pages 9-10) | Human mechanistic synthesis; moderate-strong (kellerUnknownyeargövip18prof.dr. pages 9-10) |
| Supporting pre-disease mechanistic study | Independent human B-cell work established CIN85 as regulator of Cbl-mediated BCR signaling | CIN85 overexpression inhibited BCR-induced calcium flux and phosphorylation of Syk/PLCγ2; CIN85 knockdown enhanced BCR-induced survival/growth and affected differentiation-associated molecules in human B cells (niiro2012cin85isrequired pages 1-2, niiro2012cin85isrequired pages 2-3, niiro2012cin85isrequired pages 3-4) | Human cell-line and primary-cell mechanistic evidence; supportive but not disease-specific (niiro2012cin85isrequired pages 1-2, niiro2012cin85isrequired pages 2-3, niiro2012cin85isrequired pages 3-4) |
| Mouse B-cell model | Conditional murine B-cell loss of CIN85 recapitulates selective humoral defects | IgM and IgG3 responses to Ficoll-coupled hapten almost blunted; peritoneal B1-cell subset reduced ~7.5-fold; splenic B2 development grossly normal; T-dependent responses had little impact (kellerUnknownyeargövip18prof.dr. pages 4-5, kellerUnknownyeargövip18prof.dr. pages 5-7, kellerUnknownyeargövip18prof.dr. pages 11-12) | In vivo model evidence; strong supportive translational evidence (kellerUnknownyeargövip18prof.dr. pages 4-5, kellerUnknownyeargövip18prof.dr. pages 5-7, kellerUnknownyeargövip18prof.dr. pages 11-12) |
| Human engineered cell model | Gene editing confirms nonredundant role of CIN85 in human BCR signaling | CRISPR/Cas9 CIN85 knockout DG75 cells showed strongly compromised BCR-induced Ca2+ mobilization; signaling-incompetent C-terminal deletion mutant failed to rescue; similar result also seen with independent TALEN approach (kellerUnknownyeargövip18prof.dr. pages 7-9, kellerUnknownyeargövip18prof.dr. pages 10-11) | Human cell model; strong mechanistic validation (kellerUnknownyeargövip18prof.dr. pages 7-9, kellerUnknownyeargövip18prof.dr. pages 10-11) |
| Brain model/comparative biology | Nonimmune CIN85 functions are supported by mouse brain isoform data | Brain-specific CIN85 loss impaired dopamine receptor endocytosis and caused hyperactive behavior in mice, relevant only as indirect support for possible ADHD-like observations (kellerUnknownyeargövip18prof.dr. pages 4-5, kellerUnknownyeargövip18prof.dr. pages 11-12) | Mouse model; indirect/weak for human disease phenotype (kellerUnknownyeargövip18prof.dr. pages 4-5, kellerUnknownyeargövip18prof.dr. pages 11-12) |
| Diagnosis | Diagnosis in reported family required genomic copy-number testing plus immunologic workup | aCGH identified deletion; qPCR verification used; whole-exome sequencing excluded phenotypically relevant variants in 395 primary immunodeficiency genes; immunoblot confirmed loss of CIN85 with normal CD2AP (kellerUnknownyeargövip18prof.dr. pages 4-5, kellerUnknownyeargövip18prof.dr. pages 10-11) | Human diagnostic evidence; strong for this family (kellerUnknownyeargövip18prof.dr. pages 4-5, kellerUnknownyeargövip18prof.dr. pages 10-11) |
| Current clinical implementation | Disease has entered at least some specialized immunology workflows | CIN85 marker reportedly incorporated into routine immune diagnostics in Freiburg and Hannover after publication (kellerUnknownyeargövip18prof.dr. pages 1-4) | Institutional implementation statement; moderate (kellerUnknownyeargövip18prof.dr. pages 1-4) |
| Treatment evidence | No disease-specific treatment study was identified in the retrieved evidence | No disease-specific interventional trial or gene-targeted therapy identified; artifact intentionally avoids extrapolating unproven treatment recommendations (OpenTargets Search: Immunodeficiency 61-SH3KBP1) | Evidence gap; strong as negative finding within retrieved sources (OpenTargets Search: Immunodeficiency 61-SH3KBP1) |
| Epidemiology | Extremely rare; prevalence/incidence cannot be estimated | Only 1 reported family and 2 affected males in retrieved primary literature (kellerUnknownyeargövip18prof.dr. pages 4-5) | Evidence gap with minimal published denominator (kellerUnknownyeargövip18prof.dr. pages 4-5) |
| Major evidence gaps | Natural history, penetrance, female-carrier phenotype, full variant spectrum, long-term complications, and optimal management remain undefined | No additional well-characterized families, no disease-specific cohort statistics, no formal genotype-phenotype series, no dedicated trials, and no robust evidence on malignancy/autoimmunity risk specific to SH3KBP1 deficiency (kellerUnknownyeargövip18prof.dr. pages 4-5, OpenTargets Search: Immunodeficiency 61-SH3KBP1) | Overall literature limitation; strong caution warranted (kellerUnknownyeargövip18prof.dr. pages 4-5, OpenTargets Search: Immunodeficiency 61-SH3KBP1) |


*Table: This table compiles the core disease-specific evidence for Immunodeficiency 61 / SH3KBP1 (CIN85) deficiency, emphasizing the two reported brothers, their deletion, phenotype, immune findings, mechanism, and supporting models. It is designed to give a concise view of what is established versus what remains unknown.*

## 1. Disease information

### Definition and identifiers
Immunodeficiency 61 is a **Mendelian, X-linked primary antibody deficiency** in which germline loss of SH3KBP1/CIN85 impairs B-cell antigen-receptor signaling and production of IgM, selected IgG subclasses, and antipolysaccharide antibodies. Peripheral B- and T-cell development can remain nearly normal, distinguishing it from classic BTK-related X-linked agammaglobulinemia. (kellerUnknownyeargövip18prof.dr. pages 1-4, kellerUnknownyeargövip18prof.dr. pages 4-5, kellerUnknownyeargövip18prof.dr. pages 5-7)

Recommended names and synonyms are **Immunodeficiency 61**, **SH3KBP1 deficiency**, **CIN85 deficiency**, **X-linked antibody deficiency due to CIN85 deficiency**, and **germline deletion of CIN85**. SH3KBP1 is also called *SH3-domain kinase-binding protein 1*; its protein is **Cbl-interacting protein of 85 kDa (CIN85)**, also known experimentally as Ruk or SETA. (niiro2012cin85isrequired pages 1-2, kellerUnknownyeargövip18prof.dr. pages 1-4)

A reliable disease-specific MONDO, Orphanet, ICD-10/11, or MeSH identifier was not exposed by the retrieved authoritative literature and should not be inferred. The Open Targets query did not return an SH3KBP1–Immunodeficiency 61 association, illustrating incomplete coverage rather than disproving the primary human evidence. Use of the literal label “Immunodeficiency 61” should therefore be accompanied by SH3KBP1/CIN85 in database records. (OpenTargets Search: Immunodeficiency 61-SH3KBP1)

The evidence is **aggregated disease-level literature derived from individual patients**, not EHR-scale data: one pedigree, two affected males, one clinically unaffected carrier mother, and one unaffected half-brother. (kellerUnknownyeargövip18prof.dr. pages 4-5)

## 2. Etiology, risk, protection, and gene–environment interaction

The established cause is a **germline loss-of-function copy-number deletion** involving SH3KBP1. In the reported family, a 247.5-kb Xp22.12 deletion removed exons 2–6 at GRCh37 chrX:19,667,630–19,886,572, abolished expression of the prevalent NM_031892 transcript/CIN85 protein, and spared adjacent genes. Whole-exome analysis found no phenotypically relevant variant among 395 primary-immunodeficiency genes, while expression of the related adaptor CD2AP remained normal. (kellerUnknownyeargövip18prof.dr. pages 4-5, kellerUnknownyeargövip18prof.dr. pages 10-11)

The principal genetic risk factor is therefore inheritance of a pathogenic hemizygous SH3KBP1 loss-of-function allele in a male. The mother carried the deletion without reported immunodeficiency, consistent with X-linked transmission and likely protection through a functional allele/X-chromosome mosaicism, although X-inactivation was not established. Penetrance in hemizygous males cannot be quantified from two brothers; expression was markedly variable. (kellerUnknownyeargövip18prof.dr. pages 4-5)

No susceptibility loci, validated modifier genes, protective variants, founder effect, carrier frequency, germline mosaicism, anticipation, or environmental cause has been established. The authors explicitly considered additional genetic, epigenetic, and environmental modifiers because the brothers carrying the same deletion differed dramatically: one improved after early childhood, whereas the other developed persistent infections and fatal sepsis. Specific gene–environment interactions remain unknown; pathogen exposure likely reveals the antibody defect but does not cause it. (kellerUnknownyeargövip18prof.dr. pages 5-7, kellerUnknownyeargövip18prof.dr. pages 9-10)

## 3. Phenotypes

### Core infectious and laboratory phenotypes

* **Recurrent/severe bacterial infection**—observed in both brothers. Patient 1 had severe, winter-predominant infections through age four and subsequently became clinically well; patient 2 had recurrent sinusitis, otitis media, and pneumonia. Suggested HPO mappings: *Recurrent bacterial infections*, **HP:0002783 Recurrent lower respiratory tract infections**, **HP:0011107 Recurrent respiratory infections**, **HP:0000246 Sinusitis**, **HP:0000403 Recurrent otitis media**, and **HP:0002090 Pneumonia**. Severity and course were highly variable. (kellerUnknownyeargövip18prof.dr. pages 4-5)
* **Hypogammaglobulinemia/Ig-subclass deficiency.** Patient 1 had IgM 16 mg/dL (reference 48–228), IgG2 55 mg/dL (110–485), and IgG4 <0.8 mg/dL (5.2–196), with preserved total IgG 918 mg/dL, IgA 79 mg/dL, IgG1 595 mg/dL, and IgG3 60 mg/dL. Patient 2 had reduced IgM and IgG2/4 plus undetectable total IgG and IgA. Suggested HPO: **HP:0004313 Hypogammaglobulinemia**, *Decreased serum IgM*, *IgG2 deficiency*, *IgG4 deficiency*, and *Agammaglobulinemia* for the severe brother. (kellerUnknownyeargövip18prof.dr. pages 4-5, kellerUnknownyeargövip18prof.dr. pages 5-7)
* **Impaired antipolysaccharide antibody response.** Patient 1 failed adequate pneumococcal IgG responses against eight of nine evaluated serotypes; serotype-specific IgM met the proposed cutoff for only eight of ten serotypes, whereas anti-tetanus-toxoid peptide response was normal. Suggested HPO: **HP:0002845 Abnormality of humoral immunity** and *Impaired antibody response to vaccination*. (kellerUnknownyeargövip18prof.dr. pages 4-5, kellerUnknownyeargövip18prof.dr. pages 5-7)
* **Fatal invasive infection/organ failure.** Patient 2 died at 15 years from septic shock and multiorgan failure after bilateral pneumonia. Suggested HPO: **HP:0100806 Sepsis**, *Septic shock*, and *Multiple organ dysfunction syndrome*. (kellerUnknownyeargövip18prof.dr. pages 4-5)
* **Possible nonimmune features.** Both brothers were diagnosed at age 11 with moderate ADHD, mildly impaired adaptive skills, and obesity. Causality is uncertain; these should be entered as provisional, not definitive disease phenotypes. Suggested HPO: **HP:0007018 Attention deficit hyperactivity disorder**, **HP:0000729 Autistic behavior/behavioral abnormality only if clinically documented**, and **HP:0001513 Obesity**. (kellerUnknownyeargövip18prof.dr. pages 5-7)

No disease-specific EQ-5D, SF-36, PROMIS, disability, or quality-of-life measurements exist. Recurrent infections plausibly disrupt schooling, daily activity, and family life, while the fatal case establishes potentially profound morbidity; quantitative QoL claims are unsupported.

## 4. Genetic and molecular information

**Causal gene:** **SH3KBP1**, Xp22.12; protein CIN85. The reported deletion is germline, hemizygous in affected males, and functionally null. It is a multiexon structural deletion rather than a missense, nonsense, or small indel. The original study demonstrated absent protein, segregation with disease, and a matching B-cell functional defect, strongly supporting pathogenicity for this family. (kellerUnknownyeargövip18prof.dr. pages 4-5)

No additional confidently disease-causing allelic series, ClinVar classification set, HGMD series, population allele frequency, or genotype–phenotype correlation was established in the retrieved literature. A large deletion of this kind is expected to be extremely rare; an exact gnomAD/TOPMed frequency should not be stated without direct database interrogation. Somatic SH3KBP1 variants are not the cause of this disorder.

No validated modifier genes or disease-specific epigenetic signature have been reported. CD2AP is a biologically plausible redundant adaptor because it remained normally expressed and may compensate in T cells and some B-cell responses, but it is not a proven clinical modifier. No aneuploidy, translocation, inversion, or recurrent cytogenetic syndrome beyond the focal Xp22.12 deletion is established. (kellerUnknownyeargövip18prof.dr. pages 4-5, kellerUnknownyeargövip18prof.dr. pages 9-10)

## 5. Environmental and infectious information

There is no evidence that toxins, radiation, air pollution, occupation, smoking, diet, alcohol, or physical activity alter disease occurrence. Infectious exposure is a **clinical trigger**, not an etiology. Reported syndromes were bacterial sinopulmonary infections; individual organisms were not specified. Encapsulated bacteria are biologically important because IgM/IgG2 and pneumococcal-polysaccharide responses are defective, but organism-specific susceptibility cannot be quantified from this family. (kellerUnknownyeargövip18prof.dr. pages 4-5, kellerUnknownyeargövip18prof.dr. pages 5-7)

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic lesion:** germline SH3KBP1 deletion → absent CIN85 adaptor protein. (kellerUnknownyeargövip18prof.dr. pages 4-5)
2. **Signal-complex defect:** CIN85 normally cooperates with SLP65/BLNK and signaling proteins downstream of the B-cell receptor. Its absence reduces BCR-triggered Ca²⁺ mobilization and diacylglycerol/PKC-β-dependent coupling to canonical NF-κB. (kellerUnknownyeargövip18prof.dr. pages 7-9, kellerUnknownyeargövip18prof.dr. pages 9-10)
3. **Selective pathway failure:** patient B cells showed markedly impaired IκBα degradation and p65 phosphorylation after BCR ligation, with reduced induction of Bcl-xL, CD86, and ICAM-1. ERK phosphorylation and PI3K–Akt–mTOR readout S6 phosphorylation remained intact; CD40-, TLR9-, and PMA-driven NF-κB activation also remained intact. (kellerUnknownyeargövip18prof.dr. pages 7-9)
4. **Cellular consequence:** circulating B-cell development is largely preserved, but antigen-driven B-cell activation and differentiation into effective antibody-secreting responses—especially T-independent antipolysaccharide responses—are inadequate. T-cell signaling, cytokine production, and proliferation were overtly normal, arguing for a predominantly B-cell-intrinsic disorder. (kellerUnknownyeargövip18prof.dr. pages 7-9, kellerUnknownyeargövip18prof.dr. pages 9-10)
5. **Clinical consequence:** reduced IgM/IgG-subclass production and defective pneumococcal antibodies → recurrent respiratory bacterial infection → in severe expression, pneumonia, septic shock, multiorgan failure, and death. (kellerUnknownyeargövip18prof.dr. pages 4-5, kellerUnknownyeargövip18prof.dr. pages 5-7)

An earlier human-cell study found that CIN85 associates with c-Cbl, Cbl-b, and BLNK and affects Syk ubiquitination/degradation, calcium flux, PLCγ2, survival, growth, and differentiation. Its in-vitro negative-regulatory observations did not fully predict the positive, nonredundant role demonstrated in patient B cells, emphasizing the primacy of the human loss-of-function phenotype. Published **8 March 2012**, DOI: https://doi.org/10.1182/blood-2011-04-351965. (niiro2012cin85isrequired pages 1-2, niiro2012cin85isrequired pages 2-3, kellerUnknownyeargövip18prof.dr. pages 7-9)

Suggested GO biological processes include **B-cell receptor signaling pathway (GO:0050853)**, **B-cell activation (GO:0042113)**, **canonical NF-kappaB signal transduction**, **calcium-mediated signaling**, **immunoglobulin production**, and **response to bacterium**. Relevant cells are **B lymphocyte (CL:0000236)**, naïve B cell, memory B cell, plasmablast, plasma cell, and possibly B-1 B cell; T lymphocytes and NK cells are evaluated comparators rather than primary targets. Relevant cellular components include cytosol, plasma membrane/BCR signalosome, and protein-containing signaling complex. (kellerUnknownyeargövip18prof.dr. pages 5-7, kellerUnknownyeargövip18prof.dr. pages 7-9, kellerUnknownyeargövip18prof.dr. pages 9-10)

No disease-specific patient transcriptome, proteome, metabolome, lipidome, single-cell atlas, spatial transcriptome, or integrated multi-omics dataset was identified. Functional genomics evidence consists of CRISPR/Cas9 and independently targeted TALEN deletion in human DG75 B cells: knockout impaired BCR-induced Ca²⁺ mobilization, and a C-terminally truncated signaling-incompetent CIN85 did not rescue it. (kellerUnknownyeargövip18prof.dr. pages 7-9, kellerUnknownyeargövip18prof.dr. pages 10-11)

## 7. Anatomical structures affected

The primary biological compartment is the **hematolymphoid/immune system**, especially circulating and lymphoid-organ B cells. Suggested anatomical terms include **UBERON:0000178 blood**, **UBERON:0002106 spleen**, **UBERON:0002371 bone marrow**, and lymph node; direct human tissue pathology in spleen, marrow, or nodes has not been reported. Secondary clinical sites are the upper and lower respiratory tract: paranasal sinus, middle ear, and bilateral lungs. Suggested terms include **UBERON:0002048 lung**, paranasal sinus, and middle ear. Infections were not described as lateralized except bilateral pneumonia in the fatal case. (kellerUnknownyeargövip18prof.dr. pages 4-5)

At subcellular level, the defect concerns a cytosolic adaptor assembled near the plasma-membrane BCR, rather than a primary mitochondrial, lysosomal, nuclear, or endoplasmic-reticulum disorder. (niiro2012cin85isrequired pages 1-2, kellerUnknownyeargövip18prof.dr. pages 7-9)

## 8. Temporal development and natural history

Onset was pediatric and likely in early childhood. Patient 1 had severe infections through age four and then a clinically quiescent period despite persistent abnormal immunology. Patient 2 never outgrew the juvenile infection period, developed recurrent sinopulmonary disease, and died at 15. Both were diagnosed with antibody deficiency/genetic disease around later childhood; the index was 12 at molecular investigation. (kellerUnknownyeargövip18prof.dr. pages 4-5, kellerUnknownyeargövip18prof.dr. pages 5-7)

The course is therefore **chronic lifelong at the molecular level but clinically variable**, ranging from early-childhood infections followed by apparent remission to persistent, progressive infectious morbidity. There is no validated staging system, progression rate, critical treatment window, or spontaneous-remission rate. Early identification before irreversible lung disease or sepsis is the most defensible intervention window, but this is clinical inference rather than disease-specific trial evidence.

## 9. Inheritance and population

Inheritance is **X-linked recessive/hemizygous loss of function**. Two males were affected; their carrier mother was clinically asymptomatic, and a healthy half-brother lacked the deletion. Penetrance among carrier females, skewed X-inactivation, and reproductive fitness are unknown. Expressivity among affected males is demonstrably variable. There is no evidence of anticipation. (kellerUnknownyeargövip18prof.dr. pages 4-5)

Prevalence and incidence cannot be calculated: the disease-specific evidence comprises one family and two affected males. No ethnicity, founder population, geographic enrichment, carrier frequency, sex ratio beyond X-linked expectation, or consanguinity effect is established. The original family was evaluated in German centers, which indicates ascertainment location rather than ancestry or geographic risk. (kellerUnknownyeargövip18prof.dr. pages 1-4, kellerUnknownyeargövip18prof.dr. pages 4-5)

## 10. Diagnostics

### Clinical and immunologic workup

Suspect the disorder in a boy with recurrent bacterial sinopulmonary infections, low IgM and IgG2/IgG4 or broader hypogammaglobulinemia, impaired pneumococcal-polysaccharide responses, and relatively preserved circulating B cells. Initial tests should include complete blood count/differential; quantitative IgG, IgA, IgM; IgG subclasses; lymphocyte subsets; B-cell maturation subsets; baseline and post-vaccination antigen-specific antibodies; and assessment for secondary causes of hypogammaglobulinemia. Disease-specific functional support includes BCR-induced Ca²⁺ flux, IκBα degradation/p65 phosphorylation, and CIN85 immunoblotting in a specialist laboratory. (kellerUnknownyeargövip18prof.dr. pages 5-7, kellerUnknownyeargövip18prof.dr. pages 7-9, edwards2021beyondmonogeneticrare pages 8-9)

### Genetic testing

The defining deletion was detected by **array comparative genomic hybridization**, verified by quantitative PCR, and confirmed functionally by absent CIN85 protein. Because ordinary WES may miss multiexon CNVs, a practical strategy is an inborn-error-of-immunity/antibody-deficiency panel that includes SH3KBP1 and validated CNV calling, followed by deletion/duplication analysis, CMA, or genome sequencing if negative. WGS is attractive for breakpoint resolution; single-gene sequencing alone is insufficient if it lacks dosage analysis. Karyotyping and FISH are generally low-yield for a 247.5-kb lesion unless a targeted probe is specifically designed. Mitochondrial and repeat-expansion testing are not relevant. (kellerUnknownyeargövip18prof.dr. pages 4-5, kellerUnknownyeargövip18prof.dr. pages 10-11)

RNA sequencing could establish transcript loss or aberrant splicing for novel variants, while protein and stimulated-pathway assays can help satisfy functional pathogenicity criteria. No validated liquid-biopsy, metabolomic, proteomic, or epigenomic diagnostic exists.

Differential diagnoses include BTK-related X-linked agammaglobulinemia, CD19/CD81/CD21 deficiency, NFKB1/NFKB2 deficiency, TACI/BAFF-R defects, CARD11/BLNK defects, ARHGEF1 deficiency, and nonmonogenic CVID. Preserved B-cell numbers, selective IgM/IgG2/4 and polysaccharide-response deficiency, and the characteristic BCR→NF-κB defect favor SH3KBP1 deficiency over BTK-related XLA. Recent antibody-deficiency reviews continue to list SH3KBP1 deficiency as IgM/IgG deficiency with severe bacterial infection, but no standardized disease-specific diagnostic criteria exist. (amirifar2021knownandpotential pages 9-10, szaflarska2024clinicalandexperimental pages 4-5)

Family testing should include the mother and at-risk maternal relatives; prenatal or preimplantation testing is technically possible once the familial deletion is defined. Newborn TREC screening would likely miss this predominantly humoral defect because T-cell development is intact; no population newborn screen exists. (kellerUnknownyeargövip18prof.dr. pages 9-10)

## 11. Outcome and prognosis

Observed survival ranged from survival with clinical improvement at age 12 to death at 15. A 5- or 10-year survival rate, life expectancy, mortality rate, and disease-specific disability burden cannot be estimated. The fatal pathway was bilateral pneumonia → septic shock → multiorgan failure. Potential long-term bronchiectasis is biologically and review-supported for SH3KBP1 deficiency, but the defining family report did not provide imaging-based bronchiectasis details. (kellerUnknownyeargövip18prof.dr. pages 4-5, amirifar2021knownandpotential pages 9-10)

Likely prognostic factors are depth of immunoglobulin loss, frequency/severity of infections, vaccine-response failure, and established lung damage; none is validated in a cohort. Patient 2’s undetectable IgG/IgA and persistent infection suggest that broader antibody loss may mark worse prognosis, but this is an n=1 comparison. No prognostic biomarker or QoL instrument has been validated.

## 12. Treatment and applications

No controlled or disease-specific treatment study, response rate, pharmacogenomic guidance, HSCT series, gene therapy, RNA therapy, or SH3KBP1-targeted clinical trial was identified. A 2024 review accordingly listed treatment for SH3KBP1/CIN85 deficiency as **not available**, meaning no disorder-specific evidence—not that supportive antibody-deficiency care should be withheld. (szaflarska2024clinicalandexperimental pages 4-5)

A rational clinical approach, extrapolated from predominantly antibody deficiencies, is:

1. Prompt culture-directed antimicrobial therapy for infections and consideration of antibacterial prophylaxis if infections recur.
2. **Immunoglobulin replacement therapy (IgRT)** when clinically significant infections coexist with substantial IgG deficiency or impaired specific-antibody production. Contemporary humoral-immunodeficiency practice uses approximately 0.4–0.5 g/kg every four weeks IV or 0.1 g/kg weekly SC, individualized to infection control and trough IgG. Across CVID—not specifically SH3KBP1 deficiency—pneumonia incidence fell about 27% for each 100-mg/dL increase in trough IgG. (szaflarska2024clinicalandexperimental pages 5-6)
3. Pulmonary surveillance, including spirometry and chest imaging when indicated, plus ENT care and airway-clearance therapy if chronic suppurative disease/bronchiectasis develops.
4. Avoid empirical immunosuppression unless a documented inflammatory/autoimmune indication exists; none was disease-specific in the reported family.

Suggested NCIt intervention concepts are **Immunoglobulin Replacement Therapy**, **Intravenous Immunoglobulin**, **Subcutaneous Immunoglobulin**, **Antibiotic Therapy**, **Antimicrobial Prophylaxis**, and **Genetic Counseling**. Exact NCIt codes should be resolved against the current release. HSCT is not established and is difficult to justify for an isolated B-cell signaling defect manageable with supportive care; gene replacement/editing remains preclinical. No relevant NCT identifier was found.

## 13. Prevention

The genotype cannot be prevented through lifestyle modification. **Primary prevention** consists of reproductive genetic counseling, carrier testing, and optional prenatal/preimplantation diagnosis. **Secondary prevention** consists of cascade testing and early immunologic assessment of at-risk male infants before severe infection. **Tertiary prevention** includes IgRT when indicated, prompt antibiotics, prophylaxis in selected patients, respiratory surveillance, airway clearance, and avoidance of delayed pneumonia treatment.

Vaccination should be individualized by an immunologist. Inactivated vaccines are generally useful and anti-tetanus response was preserved, but pneumococcal-polysaccharide responses may be inadequate and should be measured. The literature does not define live-vaccine safety specifically; preserved T cells are reassuring, but decisions should reflect the complete immune phenotype rather than the disease label alone. Household vaccination and routine infection-control practices are sensible but untested specifically. (kellerUnknownyeargövip18prof.dr. pages 4-5, kellerUnknownyeargövip18prof.dr. pages 9-10)

## 14. Other species and natural disease

No naturally occurring veterinary counterpart, breed predisposition, zoonotic transmission, or cross-species infectious transmission of this genetic disorder was identified. The orthologous murine gene is commonly styled **Sh3kbp1/Cin85**; mouse is **NCBI Taxon 10090**, human **Taxon 9606**. Exact ortholog Gene IDs and VBO terms should be obtained directly from NCBI/Alliance before database loading.

The mechanism is evolutionarily conserved sufficiently for murine B-cell deletion to reproduce impaired T-independent antibody responses, but species differences are important: murine work emphasizes IgM/IgG3 and peritoneal B-1 cells, whereas human disease showed IgM/IgG2/IgG4 and antipneumococcal abnormalities. (kellerUnknownyeargövip18prof.dr. pages 4-5, kellerUnknownyeargövip18prof.dr. pages 5-7)

## 15. Model organisms and experimental systems

The principal in-vivo model is a **conditional B-cell-specific CIN85-deficient mouse**. It had almost absent IgM/IgG3 responses to Ficoll-coupled hapten, an approximately 7.5-fold reduction of peritoneal B-1 cells, and largely preserved splenic B-2 development and T-dependent responses. This model strongly recapitulates selective T-independent humoral failure but does not reproduce the full human severity spectrum or prove the existence of an equivalent human B-1-cell defect. Constitutively active IKK-β rescued the mouse T-independent antibody response, placing impaired canonical NF-κB downstream of the CIN85 lesion. (kellerUnknownyeargövip18prof.dr. pages 4-5, kellerUnknownyeargövip18prof.dr. pages 5-7, kellerUnknownyeargövip18prof.dr. pages 9-10, kellerUnknownyeargövip18prof.dr. pages 11-12)

Human experimental models include primary patient B cells and CRISPR/Cas9- or TALEN-edited DG75 B-cell lines. Knockout compromised BCR-induced Ca²⁺ flux, and wild-type—but not C-terminally truncated—CIN85 restored signaling, providing orthogonal functional validation. Earlier BJAB/primary B-cell knockdown and overexpression studies mapped interactions with Cbl/BLNK, Syk/PLCγ2 signaling, survival, and differentiation. (niiro2012cin85isrequired pages 1-2, niiro2012cin85isrequired pages 2-3, kellerUnknownyeargövip18prof.dr. pages 7-9, kellerUnknownyeargövip18prof.dr. pages 10-11)

A brain-isoform conditional mouse showed impaired dopamine-receptor endocytosis and hyperactivity. This is only indirect support for the brothers’ ADHD-like phenotype and should not be treated as definitive neurobehavioral disease recapitulation. No rat, zebrafish, Drosophila, organoid, or patient-derived iPSC model was identified. (kellerUnknownyeargövip18prof.dr. pages 4-5, kellerUnknownyeargövip18prof.dr. pages 11-12)

## Current understanding and priority knowledge gaps

The most authoritative conclusion is that CIN85 has a **nonredundant role in human humoral immunity**, selectively connecting BCR engagement to Ca²⁺/PKC-β/canonical NF-κB activation while leaving much of T-cell function and CD40/TLR9 signaling intact. Recent reviews through 2024 continue to recognize SH3KBP1 deficiency, but they have not supplied a larger clinical series or disease-specific therapy. (amirifar2021knownandpotential pages 9-10, szaflarska2024clinicalandexperimental pages 4-5)

High-priority research needs are independent families and variants; ClinGen-level gene curation; penetrance and female-carrier studies; longitudinal infection, lung, autoimmune, malignancy, and QoL outcomes; direct treatment-response data; single-cell characterization of B-cell subsets; and development of patient-derived iPSC or primary B-cell rescue systems. Until these data exist, exact prevalence, phenotype frequencies, prognosis, and optimal therapy must be labeled **unknown**, not extrapolated from the two reported brothers.

References

1. (kellerUnknownyeargövip18prof.dr. pages 1-4): B Keller, M Shoukier, K Schulz, A Bhatt, and I Heine. Gö-vip-18: prof. dr. jürgen wienands. Unknown journal, Unknown year.

2. (kellerUnknownyeargövip18prof.dr. pages 4-5): B Keller, M Shoukier, K Schulz, A Bhatt, and I Heine. Gö-vip-18: prof. dr. jürgen wienands. Unknown journal, Unknown year.

3. (kellerUnknownyeargövip18prof.dr. pages 5-7): B Keller, M Shoukier, K Schulz, A Bhatt, and I Heine. Gö-vip-18: prof. dr. jürgen wienands. Unknown journal, Unknown year.

4. (kellerUnknownyeargövip18prof.dr. pages 7-9): B Keller, M Shoukier, K Schulz, A Bhatt, and I Heine. Gö-vip-18: prof. dr. jürgen wienands. Unknown journal, Unknown year.

5. (kellerUnknownyeargövip18prof.dr. pages 9-10): B Keller, M Shoukier, K Schulz, A Bhatt, and I Heine. Gö-vip-18: prof. dr. jürgen wienands. Unknown journal, Unknown year.

6. (niiro2012cin85isrequired pages 1-2): Hiroaki Niiro, Siamak Jabbarzadeh-Tabrizi, Yoshikane Kikushige, Takahiro Shima, Kumiko Noda, Shun-ichiro Ota, Hirofumi Tsuzuki, Yasushi Inoue, Yojiro Arinobu, Hiromi Iwasaki, Shinji Shimoda, Eishi Baba, Hiroshi Tsukamoto, Takahiko Horiuchi, Tadayoshi Taniyama, and Koichi Akashi. Cin85 is required for cbl-mediated regulation of antigen receptor signaling in human b cells. Blood, 119 10:2263-73, Mar 2012. URL: https://doi.org/10.1182/blood-2011-04-351965, doi:10.1182/blood-2011-04-351965. This article has 20 citations and is from a highest quality peer-reviewed journal.

7. (niiro2012cin85isrequired pages 2-3): Hiroaki Niiro, Siamak Jabbarzadeh-Tabrizi, Yoshikane Kikushige, Takahiro Shima, Kumiko Noda, Shun-ichiro Ota, Hirofumi Tsuzuki, Yasushi Inoue, Yojiro Arinobu, Hiromi Iwasaki, Shinji Shimoda, Eishi Baba, Hiroshi Tsukamoto, Takahiko Horiuchi, Tadayoshi Taniyama, and Koichi Akashi. Cin85 is required for cbl-mediated regulation of antigen receptor signaling in human b cells. Blood, 119 10:2263-73, Mar 2012. URL: https://doi.org/10.1182/blood-2011-04-351965, doi:10.1182/blood-2011-04-351965. This article has 20 citations and is from a highest quality peer-reviewed journal.

8. (niiro2012cin85isrequired pages 3-4): Hiroaki Niiro, Siamak Jabbarzadeh-Tabrizi, Yoshikane Kikushige, Takahiro Shima, Kumiko Noda, Shun-ichiro Ota, Hirofumi Tsuzuki, Yasushi Inoue, Yojiro Arinobu, Hiromi Iwasaki, Shinji Shimoda, Eishi Baba, Hiroshi Tsukamoto, Takahiko Horiuchi, Tadayoshi Taniyama, and Koichi Akashi. Cin85 is required for cbl-mediated regulation of antigen receptor signaling in human b cells. Blood, 119 10:2263-73, Mar 2012. URL: https://doi.org/10.1182/blood-2011-04-351965, doi:10.1182/blood-2011-04-351965. This article has 20 citations and is from a highest quality peer-reviewed journal.

9. (kellerUnknownyeargövip18prof.dr. pages 11-12): B Keller, M Shoukier, K Schulz, A Bhatt, and I Heine. Gö-vip-18: prof. dr. jürgen wienands. Unknown journal, Unknown year.

10. (kellerUnknownyeargövip18prof.dr. pages 10-11): B Keller, M Shoukier, K Schulz, A Bhatt, and I Heine. Gö-vip-18: prof. dr. jürgen wienands. Unknown journal, Unknown year.

11. (OpenTargets Search: Immunodeficiency 61-SH3KBP1): Open Targets Query (Immunodeficiency 61-SH3KBP1, 0 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

12. (edwards2021beyondmonogeneticrare pages 8-9): Emily S. J. Edwards, Julian J. Bosco, Samar Ojaimi, Robyn E. O’Hehir, and Menno C. van Zelm. Beyond monogenetic rare variants: tackling the low rate of genetic diagnoses in predominantly antibody deficiency. Cellular & Molecular Immunology, 18:588-603, Aug 2021. URL: https://doi.org/10.1038/s41423-020-00520-8, doi:10.1038/s41423-020-00520-8. This article has 46 citations and is from a peer-reviewed journal.

13. (amirifar2021knownandpotential pages 9-10): Parisa Amirifar, Reza Yazdani, Gholamreza Azizi, Mohammad Reza Ranjouri, Anne Durandy, Alessandro Plebani, Vassilios Lougaris, Lennart Hammarstrom, Asghar Aghamohammadi, and Hassan Abolhassani. Known and potential molecules associated with altered b cell development leading to predominantly antibody deficiencies. Pediatric Allergy and Immunology, 32:1601-1615, Jul 2021. URL: https://doi.org/10.1111/pai.13589, doi:10.1111/pai.13589. This article has 22 citations and is from a domain leading peer-reviewed journal.

14. (szaflarska2024clinicalandexperimental pages 4-5): Anna Szaflarska, Marzena Lenart, Magdalena Rutkowska-Zapała, and Maciej Siedlar. Clinical and experimental treatment of primary humoral immunodeficiencies. Clinical and Experimental Immunology, 216:120-131, Feb 2024. URL: https://doi.org/10.1093/cei/uxae008, doi:10.1093/cei/uxae008. This article has 8 citations and is from a peer-reviewed journal.

15. (szaflarska2024clinicalandexperimental pages 5-6): Anna Szaflarska, Marzena Lenart, Magdalena Rutkowska-Zapała, and Maciej Siedlar. Clinical and experimental treatment of primary humoral immunodeficiencies. Clinical and Experimental Immunology, 216:120-131, Feb 2024. URL: https://doi.org/10.1093/cei/uxae008, doi:10.1093/cei/uxae008. This article has 8 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Immunodeficiency_61-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 1 |
| Off topic | 0 |

All extracted references resolved successfully.