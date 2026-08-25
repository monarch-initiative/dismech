---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-17T21:04:00.001713'
end_time: '2026-08-17T21:13:22.491062'
duration_seconds: 562.49
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hypertrophic Cardiomyopathy 2
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 24
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 7
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Hypertrophic_Cardiomyopathy_2-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hypertrophic Cardiomyopathy 2
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Hypertrophic Cardiomyopathy 2** covering all of the
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
- **Disease Name:** Hypertrophic Cardiomyopathy 2
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **Hypertrophic Cardiomyopathy 2** covering all of the
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


# Hypertrophic Cardiomyopathy 2 (TNNT2-related HCM): Disease Characteristics Report

## Executive scope and evidence note

**Hypertrophic cardiomyopathy 2 (HCM2)** is the historical gene-numbered form of familial hypertrophic cardiomyopathy caused by heterozygous pathogenic variants in **TNNT2**, encoding cardiac troponin T. It should not be confused with generic hypertrophic cardiomyopathy (HCM), nor with other TNNT2-associated phenotypes such as dilated cardiomyopathy or left-ventricular noncompaction. Open Targets supports a literature-backed association between TNNT2 (ENSG00000118194) and HCM/familial HCM, including primary reports indexed by PMIDs 8989109, 10525521, 12707239, 27532257, 28369730, and 30681346. (OpenTargets Search: hypertrophic cardiomyopathy-TNNT2)

Because contemporary guidelines generally manage disease according to the **HCM phenotype**, rather than its historical numbered subtype, this report labels evidence as either **TNNT2-specific** or **general-HCM extrapolation**. The source base is aggregated disease-level literature rather than individual-patient EHR data.

| Domain | HCM2-specific fact | Suggested ontology IDs/terms | Evidence/qualification |
|---|---|---|---|
| Identity | Historical disease entity is **Hypertrophic cardiomyopathy 2 (HCM2)**, a **TNNT2-related familial hypertrophic cardiomyopathy** subtype; use disease-level resources with caution because many current sources collapse numbered subtypes into generic HCM. | **OMIM: 115195** (if using historical subtype mapping); **TNNT2 / HGNC:11949**; **MONDO caveat:** use generic **hypertrophic cardiomyopathy MONDO:0005045** when subtype MONDO is not confidently established | TNNT2 is an established HCM target/disease association; numbering/scope caveat because recent resources emphasize gene-defined sarcomeric HCM rather than historic subtype labels (OpenTargets Search: hypertrophic cardiomyopathy-TNNT2) |
| Synonyms | Suggested labels: **TNNT2-related hypertrophic cardiomyopathy**, **cardiac troponin T-associated hypertrophic cardiomyopathy**, **familial hypertrophic cardiomyopathy due to TNNT2** | MeSH/ICD not confidently subtype-specific here; retain free-text synonyms | Modern literature usually discusses TNNT2-positive HCM rather than “HCM2” as a primary label (OpenTargets Search: hypertrophic cardiomyopathy-TNNT2, topriceanu2024metaanalysisofpenetrance pages 1-2) |
| Etiology | Primary cause is **heterozygous germline pathogenic/likely pathogenic variants in TNNT2**, encoding cardiac troponin T, a thin-filament sarcomeric protein | **TNNT2 / HGNC:11949**; sarcomere/thin filament terms as annotations | Supported by disease-target evidence and TNNT2-specific primary studies/models (OpenTargets Search: hypertrophic cardiomyopathy-TNNT2, kondo2022humaninducedpluripotentstem pages 1-2, shafaattalab2021mechanismsofarrhythmogenicity pages 1-2, cai2020establishinganew pages 21-25) |
| Inheritance | Typically **autosomal dominant** with **age-dependent, incomplete penetrance** and variable expressivity | HPO inheritance term may be added locally if needed; no ID asserted here | General genetic HCM evidence; applies to TNNT2-positive families, with gene-specific penetrance estimates available (shafaattalab2021mechanismsofarrhythmogenicity pages 1-2, topriceanu2024metaanalysisofpenetrance pages 1-2) |
| Penetrance / natural history | Meta-analysis estimate for **TNNT2 penetrance ~60%** in nonproband relatives identified by cascade screening; mean age at HCM diagnosis ~**38 years**; phenotypic conversion across sarcomeric HCM about **15% over ~8 years** from subclinical state | Phenotype conversion / age-dependent penetrance annotations | Best recent quantitative estimate; this is family/clinical-context penetrance, not incidental population penetrance (topriceanu2024metaanalysisofpenetrance pages 1-2) |
| Variant classes | Reported pathogenic TNNT2 variants in HCM include **missense** and **small in-frame deletion** variants; notable research variants include **R92Q**, **I79N**, **Δ160E** | Sequence Ontology terms can be added locally (missense_variant, inframe_deletion) | Variant examples are from mechanistic/model papers; not an exhaustive clinical variant catalog (kondo2022humaninducedpluripotentstem pages 1-2, shafaattalab2021mechanismsofarrhythmogenicity pages 1-2, cai2020establishinganew pages 21-25) |
| Core phenotype | Unexplained **left ventricular hypertrophy** with familial sarcomeric cardiomyopathy features | **HP:0001712 Left ventricular hypertrophy** | TNNT2-specific and general HCM-defining feature; subtype-specific frequency not precisely quantified in retrieved evidence (cai2020establishinganew pages 21-25, nakamura2025cardiacmyosininhibitors pages 2-4) |
| Arrhythmic phenotype | TNNT2 variants can confer **high arrhythmic risk and sudden death risk**, sometimes **despite mild hypertrophy** | **HP:0001645 Arrhythmia**; **HP:0001680 Ventricular arrhythmia**; **HP:0001644 Syncope**; **HP:0001699 Sudden cardiac death** | Strongly emphasized for TNNT2 variants, especially I79N and thin-filament HCM literature (shafaattalab2021mechanismsofarrhythmogenicity pages 1-2) |
| Diastolic/relaxation phenotype | Relaxation impairment and diastolic dysfunction are prominent early phenotypes linked to increased myofilament Ca2+ sensitivity | **HP:0005157 Abnormal left ventricular diastolic function** | Directly shown in TNNT2 Δ160E and zebrafish TNNT2 models (kondo2022humaninducedpluripotentstem pages 1-2, kamel2021aheterozygousmutation pages 1-2) |
| Cellular hypertrophy | Mutant cardiomyocytes show increased cell size and hypertrophic signaling | **HP:0001639 Cardiomyocyte hypertrophy** if locally mapped; **HP:0000822?** not asserted if uncertain | Derived mainly from hESC/iPSC cardiomyocyte models; keep as experimental phenotype annotation (kondo2022humaninducedpluripotentstem pages 1-2, cai2020establishinganew pages 21-25) |
| Sarcomere disarray | TNNT2-HCM models show **myofilament/myofibrillar disarray** | **HP:0005179 Myocardial fiber disarray** (suggested if local ontology supports exact term) | Strong experimental support in TNNT2 R92Q and I79N models (shafaattalab2021mechanismsofarrhythmogenicity pages 1-2, cai2020establishinganew pages 21-25) |
| Biomarker phenotype | Natriuretic peptide and injury biomarker elevation may occur in HCM; TNNT2 I79N model showed **NPPA/NPPB upregulation** | **HP:0031185 Elevated circulating NT-proBNP level** (general-HCM extrapolation); transcript markers **NPPA/NPPB** | Direct TNNT2 evidence is transcriptomic/model-based; circulating biomarker use is broader HCM extrapolation (shafaattalab2021mechanismsofarrhythmogenicity pages 1-2, nakamura2025cardiacmyosininhibitors pages 13-14, ottaviani2023revisitingdiagnosisand pages 23-24) |
| Mechanism: primary biophysical defect | Upstream mechanism is **increased myofilament Ca2+ sensitivity** and **slower Ca2+ dissociation/off-rate** from thin filament regulation | **GO:0051592 response to calcium ion**; **GO:0006936 muscle contraction**; **GO:0030049 muscle filament sliding** | Core TNNT2 mechanism shown for I79N, Δ160E, and R92Q models (kondo2022humaninducedpluripotentstem pages 1-2, shafaattalab2021mechanismsofarrhythmogenicity pages 1-2, cai2020establishinganew pages 21-25) |
| Mechanism: calcium handling | Mutations drive **prolonged calcium decay**, intracellular Ca2+ retention/buffering abnormalities, and impaired relaxation | **GO:0051480 regulation of cytosolic calcium ion concentration**; **GO:1903779 regulation of cardiac conduction?** not asserted if uncertain | Strong TNNT2-specific model evidence (kondo2022humaninducedpluripotentstem pages 1-2, shafaattalab2021mechanismsofarrhythmogenicity pages 1-2, kamel2021aheterozygousmutation pages 1-2) |
| Mechanism: hypertrophic signaling | Downstream signaling includes **NFATc1 nuclear translocation** and **increased CaMKIIδ / phospholamban phosphorylation** | **GO:0006468 protein phosphorylation**; **GO:0007205 protein kinase C-activating GPCR signaling?** not asserted; **GO:0006950 response to stress** if needed | Direct TNNT2 Δ160E evidence; useful for pathway annotation but not yet routine clinical biomarker use (kondo2022humaninducedpluripotentstem pages 1-2) |
| Mechanism: electrophysiology | Ca2+ dysregulation promotes **beat-to-beat instability**, **action-potential triangulation**, and **alternans**, creating an arrhythmic substrate/trigger | **GO:0086001 cardiac muscle cell action potential**; **GO:1903779 regulation of cardiac conduction** | Strong TNNT2 I79N hiPSC-CM evidence (shafaattalab2021mechanismsofarrhythmogenicity pages 1-2) |
| Mechanism: energetics / oxidative stress | Recent HCM work supports a broader sarcomeric-HCM mechanism in which increased Ca2+ sensitivity causes **bioenergetic mismatch**, **mitochondrial ROS**, spontaneous Ca2+ release, and arrhythmias | **GO:0006979 response to oxidative stress**; **GO:0042775 mitochondrial ATP synthesis coupled electron transport** | General-HCM extrapolation from HCM mouse models including TNNT2-I79N; promising but partly preprint-stage for 2024 evidence (dolder2025experimentalmodelsof pages 36-36) |
| Tissue remodeling | Fibrosis/ECM-remodeling programs are downstream disease features; TNNT2 I79N transcriptomics showed ECM-remodeling signatures | **GO:0030198 extracellular matrix organization**; **GO:0061448 connective tissue development?** not asserted; **HP:0005680 Myocardial fibrosis** (suggested) | Direct transcriptomic/model support; clinical fibrosis imaging is often inferred from general HCM practice (shafaattalab2021mechanismsofarrhythmogenicity pages 1-2, sanghvi2025hypertrophiccardiomyopathymanagement pages 11-12) |
| Cell types | Primary affected cell type is **cardiomyocyte**; fibroblasts and endothelial/immune compartments are likely secondary participants in remodeling/fibrosis | **CL:0002494 cardiomyocyte**; **CL:0000057 fibroblast**; endothelial cell term may be added locally if needed | Cardiomyocyte involvement is direct; fibroblast/endothelial participation is mainly general-HCM extrapolation from fibrosis literature (kondo2022humaninducedpluripotentstem pages 1-2, shafaattalab2021mechanismsofarrhythmogenicity pages 1-2, dolder2025experimentalmodelsof pages 36-36) |
| Anatomy | Primary organ/site is **heart**, especially **left ventricular myocardium**; obstruction may involve **left ventricular outflow tract** in obstructive phenotypes | **UBERON:0000948 heart**; **UBERON:0002084 myocardium**; **UBERON:0002080 cardiac ventricle**; LVOT term add locally if curated | HCM-anatomy statements are partly generic HCM criteria because TNNT2-specific anatomy is not uniquely distinct (cai2020establishinganew pages 21-25, sanghvi2025hypertrophiccardiomyopathymanagement pages 11-12, nakamura2025cardiacmyosininhibitors pages 2-4) |
| Subcellular localization | Disease-relevant compartment is the **sarcomeric thin filament / myofilament complex** | GO cellular-component terms can be added locally, e.g. sarcomere/thin filament if curated from external ontology | Strong mechanistic fit, but specific GO CC IDs were not verified in retrieved context, so not asserted numerically |
| Diagnostics: clinical definition | HCM diagnosis in adults generally requires **unexplained LV wall thickness ≥15 mm**; **≥13 mm** in first-degree relatives can support diagnosis | Diagnostic threshold annotation; **HP:0001712** | **General-HCM extrapolation** from current diagnostic practice, applied to TNNT2-HCM when subtype-specific criteria are absent (nakamura2025cardiacmyosininhibitors pages 2-4) |
| Diagnostics: imaging | **Transthoracic echocardiography** is first-line; **CMR** is recommended for morphology clarification, apical disease, aneurysm/thrombus detection, and fibrosis/LGE assessment; provocation/exercise testing is used when obstruction is suspected but absent at rest | NCIT-style labels: Echocardiography, Cardiac MRI, Exercise Testing | Guideline-review level evidence, largely generic HCM but clinically applicable to TNNT2-HCM (sanghvi2025hypertrophiccardiomyopathymanagement pages 11-12, nakamura2025cardiacmyosininhibitors pages 2-4) |
| Diagnostics: genetic testing | Multigene cardiomyopathy testing including **TNNT2** is recommended to support diagnosis, cascade screening, and phenocopy distinction | **TNNT2 / HGNC:11949**; NCIT-style labels: Molecular Genetic Testing, Cascade Screening | Strongly supported in guideline reviews; phenotype-negative relatives are not genetically “diagnosed” without a known familial variant (sanghvi2025hypertrophiccardiomyopathymanagement pages 11-12, nakamura2025cardiacmyosininhibitors pages 2-4) |
| Differential diagnosis | Exclude **HCM phenocopies** and secondary hypertrophy causes: amyloidosis, Fabry disease, glycogen storage disease, mitochondrial disease, RASopathy, valvular/loading conditions, athlete’s heart | Use generic phenocopy/differential labels locally | Mostly general-HCM evidence, important because numbered HCM subtype labels can obscure phenocopies (sanghvi2025hypertrophiccardiomyopathymanagement pages 11-12, nakamura2025cardiacmyosininhibitors pages 2-4) |
| Epidemiology | HCM prevalence broadly is about **1 in 500** in classic estimates; TNNT2-specific disease is a minority sarcomeric subset; one review/meta-analysis found TNNT2 penetrance around 60% in family screening context | Population prevalence annotation; gene-specific subset flag | **General-HCM extrapolation** for overall prevalence; TNNT2-specific frequency not robustly quantified in retrieved evidence (shafaattalab2021mechanismsofarrhythmogenicity pages 1-2, topriceanu2024metaanalysisofpenetrance pages 1-2) |
| Prognosis | Prognosis is variable; TNNT2 variants are notable for **arrhythmia/sudden death risk** and in some variants for adverse remodeling or systolic dysfunction | Sudden-death risk annotation; heart-failure progression annotation | Subtype-specific risk is variant-dependent; avoid overgeneralizing all TNNT2 variants as uniformly high risk (kondo2022humaninducedpluripotentstem pages 1-2, shafaattalab2021mechanismsofarrhythmogenicity pages 1-2) |
| Prevention / family management | **Cascade screening** of relatives is central; exercise should generally be encouraged at mild-moderate intensity, while high-risk/high-intensity activity decisions are individualized; pregnancy medication review is needed and **mavacamten is contraindicated in pregnancy** | NCIT-style labels: Genetic Counseling, Family Screening, Exercise Counseling, Pregnancy Counseling | Mostly general-HCM guideline extrapolation but directly useful in TNNT2-HCM care pathways (sanghvi2025hypertrophiccardiomyopathymanagement pages 11-12) |
| Standard pharmacotherapy | First-line symptomatic therapy for obstructive HCM: **beta-blocker**; alternatives include **verapamil/diltiazem**; **disopyramide** can be added in selected obstructive cases | NCIT-style labels: **Beta Adrenergic Receptor Blockade**, **Verapamil Therapy**, **Diltiazem Therapy**, **Disopyramide Therapy** | General-HCM treatment extrapolation; no TNNT2-specific drug-response biomarker established in retrieved evidence (nakamura2025cardiacmyosininhibitors pages 11-13, nakamura2025cardiacmyosininhibitors pages 2-4) |
| Targeted therapy | **Mavacamten** is a cardiac myosin inhibitor for symptomatic obstructive HCM; EXPLORER-HCM primary endpoint achieved in **37% vs 17%** placebo; VALOR-HCM reduced SRT eligibility to **17.9% vs 76.8%** after 16 weeks | NCIT-style labels: **Mavacamten Therapy**, **Cardiac Myosin Inhibitor Therapy** | High-quality general-HCM evidence; not TNNT2-specific, but directly relevant to sarcomeric obstructive HCM clinical implementation (nakamura2025cardiacmyosininhibitors pages 13-14, nakamura2025cardiacmyosininhibitors pages 16-18, ottaviani2023revisitingdiagnosisand pages 23-24) |
| Emerging targeted therapy | **Aficamten** is a next-generation cardiac myosin inhibitor with shorter half-life and favorable trial results in obstructive HCM | NCIT-style labels: **Aficamten Therapy**, **Cardiac Myosin Inhibitor Therapy** | General-HCM extrapolation; regulatory/implementation status continues to evolve (nakamura2025cardiacmyosininhibitors pages 13-14, hou2025cardiacmyosininhibitors pages 12-13) |
| Procedures | If severe obstructive symptoms persist despite drug therapy, **septal reduction therapy** (surgical myectomy or alcohol septal ablation) is standard | NCIT-style labels: **Surgical Septal Myectomy**, **Alcohol Septal Ablation**, **Septal Reduction Therapy** | General-HCM standard of care; not gene-specific (nakamura2025cardiacmyosininhibitors pages 16-18, nakamura2025cardiacmyosininhibitors pages 11-13) |
| Device therapy | **ICD** used for primary/secondary prevention based on sudden-death risk stratification; one guideline approach recommends ICD for **5-year SCD risk ≥6%** and consideration at **4–6%** | NCIT-style labels: **Implantable Cardioverter Defibrillator** | General-HCM extrapolation from guideline review; TNNT2 genotype may inform concern but ICD decisions remain phenotype/risk-marker led (sanghvi2025hypertrophiccardiomyopathymanagement pages 11-12) |
| Advanced HF therapy | End-stage disease may require advanced heart-failure care, including transplant in rare progressed cases | NCIT-style labels: **Heart Transplantation** | General-HCM extrapolation; relevant because some TNNT2 variants can progress to systolic dysfunction (kondo2022humaninducedpluripotentstem pages 1-2) |
| Experimental / mechanism-based therapy | **Calcium desensitization** is mechanistically attractive in TNNT2-HCM; **epigallocatechin-3-gallate** improved calcium decay/relaxation in Δ160E iPSC-CMs | CHEBI/compound IDs not asserted here; experimental therapy label locally | Preclinical only in retrieved evidence (kondo2022humaninducedpluripotentstem pages 1-2) |
| Models: human cellular | Human **hiPSC-CM** and **hESC-CM** TNNT2 models recapitulate hypertrophy, calcium dysregulation, disarray, and pro-arrhythmic phenotypes; examples: **Δ160E**, **I79N**, **R92Q** | Model labels: hiPSC-derived cardiomyocyte, hESC-derived cardiomyocyte, engineered heart tissue | Strong direct disease-model evidence and useful for assay/drug screening annotation (kondo2022humaninducedpluripotentstem pages 1-2, shafaattalab2021mechanismsofarrhythmogenicity pages 1-2, cai2020establishinganew pages 21-25) |
| Models: animal | **Mouse** TNNT2 models (e.g., I79N, R92Q) and **zebrafish tnnt2a RK94del** model reproduce Ca2+ dysregulation, remodeling, fibrosis, and arrhythmogenic traits | Organism labels locally; NCBI Taxon IDs not asserted to avoid invention | Strong comparative evidence; supports mechanism and therapeutic screening (kamel2021aheterozygousmutation pages 1-2, dolder2025experimentalmodelsof pages 36-36) |
| Data provenance | This entry should be populated primarily from **aggregated disease-level resources and primary literature**, not solely EHR-derived observations | Evidence-source annotation | Important because subtype identity is historical and modern datasets often aggregate into generic HCM (OpenTargets Search: hypertrophic cardiomyopathy-TNNT2, topriceanu2024metaanalysisofpenetrance pages 1-2) |


*Table: This compact table summarizes key facts for Hypertrophic Cardiomyopathy 2 as TNNT2-related HCM, with ontology suggestions and evidence qualifiers for direct knowledge-base ingestion. It distinguishes TNNT2-specific findings from general-HCM extrapolations and flags uncertain identifiers to avoid over-assertion.*

## 1. Disease information

HCM2 is a primary sarcomeric myocardial disorder characterized by otherwise unexplained left-ventricular hypertrophy (LVH), cardiomyocyte disarray, diastolic dysfunction, and variable susceptibility to ventricular arrhythmia, heart failure, and sudden cardiac death. TNNT2 disease is notable because substantial arrhythmic risk may occur with relatively modest hypertrophy. (shafaattalab2021mechanismsofarrhythmogenicity pages 1-2, cai2020establishinganew pages 21-25)

**Identifiers and nomenclature**

- Historical identifier: **OMIM 115195, Cardiomyopathy, familial hypertrophic, 2**.
- Gene: **TNNT2**, HGNC:11949; Ensembl ENSG00000118194; cardiac troponin T.
- Broad phenotype: **MONDO:0005045, hypertrophic cardiomyopathy**; **MONDO:0024573, familial hypertrophic cardiomyopathy**. A confidently verified HCM2-specific MONDO identifier was not recovered, so the broad MONDO term plus TNNT2 genotype is preferable. (OpenTargets Search: hypertrophic cardiomyopathy-TNNT2)
- Common synonyms: *TNNT2-related hypertrophic cardiomyopathy*, *cardiac troponin T-associated HCM*, *familial hypertrophic cardiomyopathy due to TNNT2*, and *HCM2*.
- ICD-10/ICD-11 and MeSH generally encode HCM or obstructive HCM, not the TNNT2 subtype; genotype should therefore be recorded separately.

## 2. Etiology, risk, protection, and gene–environment interaction

### Primary cause

The causal lesion is usually a **heterozygous germline TNNT2 pathogenic or likely pathogenic variant**. TNNT2 is a component of the troponin complex on the sarcomeric thin filament and couples cytosolic calcium signals to actin–myosin contraction. Reported HCM-associated classes include missense substitutions and small in-frame deletions, including **p.Ile79Asn (I79N), p.Arg92Gln (R92Q), and p.Glu160del (Δ160E; c.478_480del)**. (kondo2022humaninducedpluripotentstem pages 1-2, shafaattalab2021mechanismsofarrhythmogenicity pages 1-2, cai2020establishinganew pages 21-25)

### Risk modifiers

Risk is shaped by variant-specific biophysics, age, family history, polygenic background, sex, loading conditions, and lifestyle, but robust TNNT2-specific effect sizes are limited. The best recent synthesis concludes that penetrance is “highly variable” and influenced by still-undefined, context-dependent genetic and environmental factors. In family-based cascade screening, TNNT2 penetrance was approximately **60%**, whereas penetrance of incidentally discovered sarcomeric variants in population cohorts was much lower, approximately **11%** overall. (topriceanu2024metaanalysisofpenetrance pages 1-2)

Hypertension, obesity, intense adrenergic stress, dehydration, and extreme exertion can worsen the expressed HCM phenotype or provoke obstruction/arrhythmia, but they do not cause monogenic HCM2. Family history of premature sudden death is clinically important. No infectious cause is recognized.

### Protective factors

No validated **TNNT2-specific protective allele** is established. Potentially protective management includes blood-pressure control, avoidance of dehydration and stimulant misuse, individualized exercise counseling, and surveillance of genotype-positive relatives. Experimental calcium desensitization improved abnormal calcium decay and relaxation in TNNT2-Δ160E cardiomyocytes, but this is not established preventive therapy. (kondo2022humaninducedpluripotentstem pages 1-2, sanghvi2025hypertrophiccardiomyopathymanagement pages 11-12)

## 3. Phenotypes

Clinical expression is age-dependent and highly variable, ranging from lifelong genotype-positive/phenotype-negative status to childhood or adult disease, severe arrhythmia, heart failure, or sudden death. Mean age at diagnosis among nonproband sarcomeric-variant relatives was **38 years** (95% CI 36–40); this is not a TNNT2-only age estimate. (topriceanu2024metaanalysisofpenetrance pages 1-2)

Major phenotypes and suggested HPO annotations include:

- **Left-ventricular hypertrophy — HP:0001712:** usually asymmetric septal, but apical or concentric patterns may occur. Severity is variable; TNNT2 carriers may have mild hypertrophy despite clinically important arrhythmic risk. (shafaattalab2021mechanismsofarrhythmogenicity pages 1-2, nakamura2025cardiacmyosininhibitors pages 2-4)
- **Abnormal LV diastolic function — HP:0005157:** impaired relaxation is mechanistically early and may precede overt hypertrophy. TNNT2-Δ160E cells showed prolonged calcium decay and relaxation impairment. (kondo2022humaninducedpluripotentstem pages 1-2)
- **Ventricular arrhythmia — HP:0001680; arrhythmia — HP:0001645:** palpitations, nonsustained or sustained ventricular tachycardia, and fibrillation may occur. I79N cardiomyocytes developed action-potential and calcium alternans above 75 beats/min in vitro. (shafaattalab2021mechanismsofarrhythmogenicity pages 1-2)
- **Syncope — HP:0001279/HP:0001644 depending local mapping:** may reflect obstruction or arrhythmia and is a sudden-death risk marker.
- **Sudden cardiac death — HP:0001699:** a major but incompletely predictable complication, sometimes disproportionate to wall thickness in TNNT2 disease. (shafaattalab2021mechanismsofarrhythmogenicity pages 1-2)
- **Dyspnea, chest pain, fatigue, reduced exercise tolerance:** generally progressive with obstruction, diastolic dysfunction, microvascular ischemia, or heart failure; subtype-specific frequencies were not recovered.
- **Dynamic LV outflow-tract obstruction:** provoked or resting obstruction may produce exertional symptoms; it is not universal and is not uniquely TNNT2-associated. (nakamura2025cardiacmyosininhibitors pages 2-4)
- **Atrial enlargement/atrial fibrillation:** downstream of chronic filling-pressure elevation; carries thromboembolic risk.
- **Myocardial fibrosis and myofiber disarray:** pathological substrates for stiffness and electrical instability. TNNT2 I79N models upregulated extracellular-matrix programs, while R92Q models showed altered sarcomere organization. (shafaattalab2021mechanismsofarrhythmogenicity pages 1-2, cai2020establishinganew pages 21-25)
- **Systolic dysfunction/end-stage remodeling:** uncommon but important; Δ160E was identified in familial HCM progressing to advanced heart failure. (kondo2022humaninducedpluripotentstem pages 1-2)

Quality of life is chiefly impaired through exercise limitation, symptoms, anxiety concerning sudden death, activity restrictions, repeated surveillance, and family implications. In obstructive HCM, mavacamten improved the Kansas City Cardiomyopathy Questionnaire overall score by **14.9 versus 5.4 points** with placebo; 36% achieved a ≥20-point improvement, corresponding to an NNT of approximately 5. These data are HCM-wide, not TNNT2-specific. (nakamura2025cardiacmyosininhibitors pages 13-14)

## 4. Genetic and molecular information

**Causal gene:** TNNT2 encodes cardiac troponin T, a sarcomeric thin-filament protein. Pathogenic HCM variants are predominantly heterozygous germline missense or in-frame changes and commonly exert altered-function/“poison-peptide” effects rather than simple whole-gene haploinsufficiency. Variant interpretation must follow ACMG/AMP criteria using segregation, population frequency, computational, functional, and case-enrichment evidence.

Illustrative variants include:

- **p.Ile79Asn:** increases myofilament Ca²⁺ sensitivity, slows Ca²⁺ dissociation, and creates pro-arrhythmic electrophysiology. (shafaattalab2021mechanismsofarrhythmogenicity pages 1-2)
- **p.Arg92Gln:** produces calcium dysregulation, increased adrenergic sensitivity, hypertrophic-marker induction, and sarcomere disorganization in engineered human cardiomyocytes. (cai2020establishinganew pages 21-25)
- **p.Glu160del/Δ160E:** causes calcium retention, impaired relaxation, hypertrophic NFAT signaling, and in some families progressive systolic dysfunction. It was reported in 1/112 Japanese familial cases, 1/197 French cases, and 3/552 UK cases in the cited study’s background. (kondo2022humaninducedpluripotentstem pages 1-2)

Pathogenic HCM alleles should generally be absent or extremely rare in gnomAD; however, no universal allele-frequency value applies. Exact ClinVar classification and gnomAD frequency must be recorded per HGVS allele and transcript. VUSs are **not** suitable for predictive cascade testing or irreversible management decisions.

No recurrent chromosomal abnormality, repeat expansion, mitochondrial mutation, or somatic mechanism defines HCM2. Modifier genes and polygenic background likely contribute to penetrance, but no modifier is currently sufficiently validated for routine HCM2 risk prediction. Epigenetic abnormalities are biologically plausible downstream responses, but no diagnostic HCM2 methylation signature is established.

## 5. Environmental and lifestyle information

HCM2 is not caused by pollution, radiation, toxins, occupation, diet, or infection. Environmental/loading factors instead modify expression. Hypertension and obesity add hypertrophic and hemodynamic stress; dehydration and vasodilation may worsen LV outflow obstruction; intense adrenergic activation may reveal arrhythmia susceptibility. Mild-to-moderate recreational exercise is generally encouraged, while high-intensity or competitive exercise requires shared decision-making and is discouraged in individuals with major risk markers or significant obstruction. (sanghvi2025hypertrophiccardiomyopathymanagement pages 11-12)

Smoking cessation, moderation of alcohol, maintenance of healthy weight, treatment of sleep apnea and hypertension, and avoidance of illicit stimulants are prudent cardiovascular measures, although none has proven TNNT2-specific disease-preventing efficacy.

## 6. Mechanism and pathophysiology

### Causal chain

**TNNT2 variant → altered troponin–tropomyosin/actin regulation → increased thin-filament calcium sensitivity and slower calcium release → hypercontractility and impaired lusitropy → energetic demand–supply mismatch and calcium-handling instability → hypertrophic signaling, cardiomyocyte enlargement, disarray, extracellular-matrix remodeling and fibrosis → diastolic dysfunction, obstruction, ischemia, arrhythmia, and occasionally systolic failure.**

The I79N study directly found increased calcium sensitivity and reduced Ca²⁺ off-rate. Its abstract reports that these changes caused “beat-to-beat instability and triangulation of the cardiac action potential,” while NPPA, NPPB, Notch, and ECM-remodeling genes were upregulated. (shafaattalab2021mechanismsofarrhythmogenicity pages 1-2)

In Δ160E cardiomyocytes, calcium retention and delayed relaxation activated **CaMKIIδ**, phospholamban phosphorylation, and dose-dependent **NFATc1 nuclear translocation**, linking the biophysical lesion to hypertrophic gene expression. Calcium desensitization with epigallocatechin-3-gallate partially rescued relaxation in vitro. (kondo2022humaninducedpluripotentstem pages 1-2)

### Biological annotations

- Processes: sarcomere organization; cardiac muscle contraction (**GO:0060048**); muscle filament sliding (**GO:0030049**); regulation of cytosolic Ca²⁺ (**GO:0051480**); cardiac action potential (**GO:0086001**); protein phosphorylation (**GO:0006468**); response to oxidative stress (**GO:0006979**); ECM organization (**GO:0030198**).
- Cells: cardiomyocyte (**CL:0002494**) is primary; cardiac fibroblasts (**CL:0000057**, broad fibroblast) and endothelial/immune cells participate secondarily in remodeling.
- Compartments: sarcomere (**GO:0030017**), myofilament/thin filament, cytosol, sarcoplasmic reticulum, mitochondrion, and nucleus.

Recent model work also implicates mitochondrial redox imbalance: increased myofilament calcium sensitivity can uncouple workload from mitochondrial calcium signaling, consume NADPH-dependent antioxidant reserve, increase mitochondrial ROS, trigger spontaneous sarcoplasmic-reticulum calcium release, and slow conduction. This provides both trigger and substrate for arrhythmia, but the 2024 report was preprint-stage and is not yet a clinical biomarker or therapy. (dolder2025experimentalmodelsof pages 36-36)

Single-cell, spatial-transcriptomic, proteomic, metabolomic, or lipidomic signatures specific to **TNNT2-HCM2** remain insufficiently validated for clinical use. Current omics findings are largely experimental and variant/model dependent.

## 7. Anatomical structures affected

The primary organ is the **heart (UBERON:0000948)**, especially **left-ventricular myocardium (UBERON:0002084, myocardium; UBERON:0002080, cardiac ventricle)**. Hypertrophy may involve the interventricular septum, apex, free wall, papillary muscles, and mitral–septal apparatus; dynamic obstruction localizes to the LV outflow tract. Secondary involvement includes left-atrial enlargement, pulmonary venous hypertension, and systemic thromboembolism from atrial fibrillation.

At tissue level, cardiac muscle shows cardiomyocyte hypertrophy, sarcomere/myofiber disarray, small-vessel disease, and interstitial or replacement fibrosis. At subcellular level, the thin filament, calcium-handling apparatus, mitochondria, and hypertrophic-signaling nucleus are implicated. Disease is not lateralized; ventricular distribution may be asymmetric. (kondo2022humaninducedpluripotentstem pages 1-2, shafaattalab2021mechanismsofarrhythmogenicity pages 1-2, cai2020establishinganew pages 21-25)

## 8. Temporal development

HCM2 is a chronic lifelong genetic predisposition, often clinically silent for years. Onset can occur in childhood, adolescence, or adulthood; penetrance is age-dependent rather than congenital in every carrier. In the 2024 meta-analysis, mean HCM diagnosis age among nonproband carriers was 38 years, and longitudinal family cohorts showed approximately **15% phenotypic conversion over eight years**, beginning from a mean age near 16 years. TNNT2 penetrance was approximately 60% in family-screened relatives. (topriceanu2024metaanalysisofpenetrance pages 1-2)

A useful stage model is:

1. **Genotype-positive/phenotype-negative:** normal wall thickness; subtle ECG, strain, diastolic, or biomarker abnormalities may occur.
2. **Early phenotype:** focal hypertrophy and impaired relaxation.
3. **Established HCM:** symptomatic or asymptomatic hypertrophy, with or without LVOTO.
4. **Complicated HCM:** atrial fibrillation, ventricular arrhythmia, progressive fibrosis, stroke, or heart failure.
5. **End-stage disease:** systolic dysfunction, restrictive physiology, or transplant-level failure in a minority.

There is no spontaneous genetic remission. Obstruction and symptoms can improve with treatment, but pathogenic-variant status persists. Childhood growth, athletic exposure, pregnancy, hypertension, and aging are clinically important surveillance periods.

## 9. Inheritance and population

Inheritance is usually **autosomal dominant**, with a 50% transmission probability from a heterozygous affected parent. Penetrance is incomplete and age-dependent, and expressivity is highly variable—even within a family. Genetic anticipation is not established. Germline mosaicism is possible in principle but is not a defining feature; consanguinity is not generally relevant to dominant HCM2. (topriceanu2024metaanalysisofpenetrance pages 1-2)

The classic clinical prevalence of all HCM is approximately **1 in 500**, but contemporary genotype/imaging estimates vary. HCM-associated P/LP variants may be more common than clinically expressed disease. HCM2-specific prevalence and incidence per 100,000 are not robustly established, and TNNT2 is a minority cause compared with MYBPC3 and MYH7. (shafaattalab2021mechanismsofarrhythmogenicity pages 1-2, topriceanu2024metaanalysisofpenetrance pages 1-2)

No consistent ethnicity-specific or geographic distribution applies to TNNT2-HCM as a whole. Individual founder alleles may be enriched locally and should be assessed variant by variant. Both sexes inherit variants equally, although clinical expression and outcomes may differ by sex; no reliable HCM2-specific male:female ratio was recovered.

## 10. Diagnostics

### Clinical and imaging criteria

In adults, HCM is generally diagnosed by otherwise unexplained maximum LV wall thickness **≥15 mm**; **≥13 mm** may support diagnosis in a first-degree relative or known pathogenic-variant carrier. Echocardiography is first-line. Valsalva, standing, or exercise provocation is used to detect latent obstruction when the resting gradient is absent. Cardiac MRI clarifies apical or focal hypertrophy and identifies aneurysm, thrombus, and late-gadolinium-enhancement fibrosis. (sanghvi2025hypertrophiccardiomyopathymanagement pages 11-12, nakamura2025cardiacmyosininhibitors pages 2-4)

Baseline evaluation includes history and pedigree, physical examination, 12-lead ECG, ambulatory ECG, echocardiography, exercise testing when appropriate, and CMR. NT-proBNP and cardiac troponin reflect hemodynamic stress/injury and prognosis but are not HCM2-specific diagnostic tests.

Histology, usually available only after myectomy, transplant, or autopsy, may show cardiomyocyte hypertrophy, nuclear enlargement, myofiber disarray, and fibrosis. Biopsy is not routinely needed for typical sarcomeric HCM.

### Genetic testing

Recommended testing uses a **validated cardiomyopathy panel** containing definitive HCM genes, including TNNT2, MYBPC3, MYH7, TNNI3, TPM1, ACTC1, MYL2, and MYL3, with phenocopy genes selected by clinical context. Sequencing plus deletion/duplication analysis is preferred. WES/WGS can be useful when panel testing is negative or the phenotype is atypical, but interpretation of deep-intronic, structural, and incidental variants remains challenging. CMA, karyotyping, FISH, mitochondrial DNA, and repeat-expansion testing are not first-line for isolated HCM2 unless syndromic features suggest another diagnosis.

Once a familial TNNT2 P/LP variant is identified, targeted cascade testing is appropriate. Relatives who test negative for that variant can usually be released from serial HCM surveillance; genotype-positive relatives require longitudinal ECG/imaging. A VUS should not be used for predictive testing. Genetic testing supports family screening and phenocopy discrimination but does not replace phenotype-led sudden-death assessment. (sanghvi2025hypertrophiccardiomyopathymanagement pages 11-12, nakamura2025cardiacmyosininhibitors pages 2-4)

### Differential diagnosis

Exclude hypertensive heart disease, aortic stenosis, athletic remodeling, transthyretin or light-chain amyloidosis, Fabry disease, glycogen-storage disease including PRKAG2 and LAMP2 disorders, mitochondrial disease, RASopathies, and infiltrative/storage disease. Red flags include multisystem disease, conduction disease, pre-excitation, neuropathy, renal dysfunction, low-voltage ECG despite thick walls, and atypical CMR enhancement.

## 11. Outcome and prognosis

Many patients have normal or near-normal longevity with contemporary surveillance and treatment, but individual risk varies. Major morbid outcomes are ventricular arrhythmia/sudden death, atrial fibrillation and stroke, progressive heart failure, LV apical aneurysm, and end-stage systolic dysfunction.

TNNT2 should not be treated as uniformly malignant: risk is **variant- and phenotype-dependent**. Nevertheless, thin-filament TNNT2 variants have been associated with sudden death despite mild LVH, and Δ160E has been associated with adverse remodeling and advanced heart failure. (kondo2022humaninducedpluripotentstem pages 1-2, shafaattalab2021mechanismsofarrhythmogenicity pages 1-2)

Prognostic assessment integrates prior cardiac arrest or sustained VT, unexplained syncope, family history of HCM-related sudden death, maximal wall thickness, LV apical aneurysm, LVEF, nonsustained VT, LVOT gradient, left-atrial size, fibrosis/LGE, and age. The ESC HCM Risk-SCD framework considers an ICD at a five-year risk of **4–6%** and recommends it at **≥6%**, while US guidance uses major risk markers and shared decision-making. (sanghvi2025hypertrophiccardiomyopathymanagement pages 11-12)

No TNNT2-specific circulating prognostic biomarker is clinically validated. Genotype is useful context but should not be the sole basis for ICD implantation.

## 12. Treatment

Treatment is phenotype-directed; no approved therapy corrects the TNNT2 allele.

### Pharmacotherapy

- **Non-vasodilating beta-blockers** are first-line for symptomatic obstructive HCM; **verapamil or diltiazem** are alternatives when appropriate. **Disopyramide** may be added for persistent obstruction. Suggested NCIT-style concepts: Beta-Blocker Therapy, Calcium Channel Blocker Therapy, Disopyramide Therapy. (nakamura2025cardiacmyosininhibitors pages 11-13, nakamura2025cardiacmyosininhibitors pages 2-4)
- Diuretics may be used cautiously for congestion. Atrial fibrillation generally warrants anticoagulation irrespective of conventional CHA₂DS₂-VASc thresholds.
- Standard heart-failure therapy is used when systolic dysfunction develops, with specialist oversight.

### Cardiac myosin inhibitors

**Mavacamten** directly reduces cardiac myosin ATPase activity and excessive actin–myosin cross-bridging. In EXPLORER-HCM, **37% versus 17%** achieved the primary exercise/NYHA endpoint; post-exercise LVOT gradient fell approximately 36 mmHg more than placebo. In VALOR-HCM, only **17.9% versus 76.8%** remained eligible for septal reduction after 16 weeks. (nakamura2025cardiacmyosininhibitors pages 13-14, ottaviani2023revisitingdiagnosisand pages 23-24)

Long-term MAVA-LTE data over a median 166.1 weeks found 77.9% improved by at least one NYHA class, LVOT gradients declined 40.3–55.3 mmHg, and 82.7% reached a Valsalva gradient <30 mmHg. Transient LVEF <50% occurred in 8.7% and resolved after interruption; this necessitates protocolized echocardiographic monitoring and drug-interaction review. (nakamura2025cardiacmyosininhibitors pages 16-18)

**Aficamten**, a shorter-half-life myosin inhibitor, reduced LVOT gradients by approximately 27–53 mmHg in REDWOOD/FOREST studies and improved exercise capacity and symptoms in obstructive HCM. These agents treat the HCM physiology, not specifically TNNT2-HCM, and are not curative. (hou2025cardiacmyosininhibitors pages 12-13, ottaviani2023revisitingdiagnosisand pages 23-24)

Mavacamten is teratogenic and contraindicated in pregnancy; reproductive counseling and effective contraception are required. (sanghvi2025hypertrophiccardiomyopathymanagement pages 11-12)

### Procedures and devices

Severe drug-refractory symptomatic LVOTO is treated with **surgical septal myectomy** or, in selected adults, **alcohol septal ablation**. A contemporary synthesis reported obstruction control in approximately 88% after myectomy and 79% after alcohol ablation; center expertise is crucial. (nakamura2025cardiacmyosininhibitors pages 11-13)

An **implantable cardioverter-defibrillator** is indicated after cardiac arrest/sustained VT and considered for primary prevention according to risk markers. Heart transplantation is reserved for refractory end-stage disease.

### Experimental therapy

Calcium desensitizers, allele-specific silencing, RNA therapy, gene editing, and gene replacement remain preclinical for TNNT2-HCM. Epigallocatechin-3-gallate rescued calcium-decay abnormalities in Δ160E iPSC cardiomyocytes, but there is no clinical efficacy evidence. (kondo2022humaninducedpluripotentstem pages 1-2)

## 13. Prevention

**Primary prevention of the inherited allele** is not possible after conception. Reproductive options include genetic counseling, prenatal diagnosis, and preimplantation genetic testing when a familial P/LP variant is known.

**Secondary prevention** centers on cascade genetic testing, serial ECG/echo surveillance of genotype-positive relatives, early recognition of obstruction/arrhythmia, ambulatory rhythm monitoring, and periodic CMR when clinically indicated. Population or newborn screening is not standard.

**Tertiary prevention** includes sudden-death risk assessment and ICD placement, anticoagulation for atrial fibrillation, management of obstruction and heart failure, avoidance of dehydration and stimulants, and individualized exercise plans. Mild-to-moderate exercise is generally beneficial; blanket inactivity is not recommended. (sanghvi2025hypertrophiccardiomyopathymanagement pages 11-12)

Vaccination has no disease-specific role beyond routine cardiovascular health. There is no infectious prophylaxis or environmental-control program specific to HCM2.

## 14. Other species and naturally occurring disease

Naturally occurring cardiomyopathies occur in cats and other animals, but a well-established, breed-specific naturally occurring **TNNT2-HCM2 orthologous disease** was not identified in the retrieved evidence. Therefore no VBO breed annotation should be asserted without OMIA-level verification. The disease is noninfectious and nonzoonotic.

Orthologous troponin-T biology is highly conserved. A CRISPR-generated **zebrafish tnnt2a RK94del** heterozygote developed early diastolic dysfunction and abnormal calcium dynamics by five days postfertilization; adults showed atrial enlargement, reduced ventricular size, myocardial stress, fibrosis, and progressive heart failure. This experimentally induced model supports cross-species conservation of thin-filament calcium dysregulation. (kamel2021aheterozygousmutation pages 1-2)

## 15. Model organisms and experimental systems

- **Human iPSC cardiomyocytes, TNNT2 I79N:** CRISPR isogenic cells reproduce increased calcium sensitivity, slowed calcium off-rate, action-potential triangulation, alternans, disarray, and NPPA/NPPB/ECM transcriptional activation. Strength: human genetic background and electrophysiology. Limitation: immature cardiomyocyte phenotype. (shafaattalab2021mechanismsofarrhythmogenicity pages 1-2)
- **Human iPSC cardiomyocytes, Δ160E:** heterozygous and homozygous isogenic lines show dose-dependent calcium-decay prolongation, relaxation impairment, NFATc1 activation, hypertrophy, and CaMKII/phospholamban signaling. Useful for calcium-desensitizer screening. (kondo2022humaninducedpluripotentstem pages 1-2)
- **Human embryonic-stem-cell cardiomyocytes and engineered tissue, R92Q:** reproduce calcium dysregulation, hypertrophic-marker expression, adrenergic hypersensitivity, altered contractility, and myofilament disorganization; useful for drug efficacy and cardiotoxicity studies. (cai2020establishinganew pages 21-25)
- **Mouse Tnnt2 models:** I79N, R92Q, and related transgenic/knock-in models reproduce arrhythmogenicity, calcium sensitization, hypertrophy, and remodeling. Advantages are intact physiology and longitudinal testing; limitations include species-specific heart rate, calcium handling, and transgene dosage. (dolder2025experimentalmodelsof pages 36-36)
- **Zebrafish tnnt2a RK94del:** offers rapid in-vivo imaging and compound screening but differs substantially from human chamber anatomy and electrophysiology. (kamel2021aheterozygousmutation pages 1-2)

## Recent developments and expert assessment

The most important 2023–2024 advance is recognition that genetic HCM penetrance depends strongly on ascertainment. The January 2024 Circulation meta-analysis reviewed 455 manuscripts and estimated TNNT2 penetrance near 60% in cascade-screened relatives, but only about 11% penetrance for incidentally identified sarcomeric P/LP variants in population studies. This supports expert recommendations that genotype be interpreted alongside pedigree and longitudinal phenotype rather than deterministically. DOI: https://doi.org/10.1161/CIRCULATIONAHA.123.065987, published January 2024. (topriceanu2024metaanalysisofpenetrance pages 1-2)

The 2023–2024 guideline era also normalized moderate exercise, emphasized shared ICD decisions and CMR fibrosis assessment, and incorporated cardiac myosin inhibition for symptomatic obstructive HCM. However, these advances are **not genotype-specific**, and no evidence yet shows that TNNT2 carriers respond differently from other sarcomeric-HCM patients. (nakamura2025cardiacmyosininhibitors pages 13-14, sanghvi2025hypertrophiccardiomyopathymanagement pages 11-12)

The central expert interpretation is therefore: **TNNT2 genotype establishes cause and enables cascade screening, but surveillance, prognosis, and treatment remain phenotype-led.** Variant-level functional data can be highly informative, yet should not be generalized across all TNNT2 alleles. The largest unresolved needs are variant-specific natural-history cohorts, validated polygenic/environmental modifiers, mature human myocardial models, and trials of causal RNA or gene therapies.

References

1. (OpenTargets Search: hypertrophic cardiomyopathy-TNNT2): Open Targets Query (hypertrophic cardiomyopathy-TNNT2, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (topriceanu2024metaanalysisofpenetrance pages 1-2): Constantin-Cristian Topriceanu, Alexandre C. Pereira, James C. Moon, Gabriella Captur, and Carolyn Y. Ho. Meta-analysis of penetrance and systematic review on transition to disease in genetic hypertrophic cardiomyopathy. Circulation, 149:107-123, Jan 2024. URL: https://doi.org/10.1161/circulationaha.123.065987, doi:10.1161/circulationaha.123.065987. This article has 105 citations and is from a highest quality peer-reviewed journal.

3. (kondo2022humaninducedpluripotentstem pages 1-2): Takumi Kondo, Shuichiro Higo, Mikio Shiba, Yasuaki Kohama, Satoshi Kameda, Tomoka Tabata, Hiroyuki Inoue, Shota Okuno, Shou Ogawa, Satoki Nakamura, Maki Takeda, Emiko Ito, Junjun Li, Li Liu, Yuki Kuramoto, Jong-Kook Lee, Seiji Takashima, Shigeru Miyagawa, Yoshiki Sawa, Shungo Hikoso, and Yasushi Sakata. Human-induced pluripotent stem cell–derived cardiomyocyte model for <i>tnnt2</i> δ160e-induced cardiomyopathy. Circulation: Genomic and Precision Medicine, Oct 2022. URL: https://doi.org/10.1161/circgen.121.003522, doi:10.1161/circgen.121.003522. This article has 20 citations.

4. (shafaattalab2021mechanismsofarrhythmogenicity pages 1-2): Sanam Shafaattalab, Alison Y Li, Marvin G Gunawan, BaRun Kim, Farah Jayousi, Yasaman Maaref, Zhen Song, James N Weiss, R. John Solaro, Zhilin Qu, and Glen F Tibbits. Mechanisms of arrhythmogenicity of hypertrophic cardiomyopathy-associated troponin t (tnnt2) variant i79n. Frontiers in Cell and Developmental Biology, Dec 2021. URL: https://doi.org/10.3389/fcell.2021.787581, doi:10.3389/fcell.2021.787581. This article has 38 citations.

5. (cai2020establishinganew pages 21-25): Huanhuan Cai, Bin Li, Aobing Bai, Jie Huang, Yongkun Zhan, Ning Sun, Qianqian Liang, and Chen Xu. Establishing a new human hypertrophic cardiomyopathy-specific model using human embryonic stem cells. Feb 2020. URL: https://doi.org/10.1016/j.yexcr.2019.111736, doi:10.1016/j.yexcr.2019.111736. This article has 9 citations and is from a peer-reviewed journal.

6. (nakamura2025cardiacmyosininhibitors pages 2-4): Kazufumi Nakamura, Takahiro Okumura, Seiya Kato, Kenji Onoue, Toru Kubo, Hidemichi Kouzu, Toshiyuki Yano, and Takayuki Inomata. Cardiac myosin inhibitors in hypertrophic cardiomyopathy: from sarcomere to clinic. International Journal of Molecular Sciences, 26:9347, Sep 2025. URL: https://doi.org/10.3390/ijms26199347, doi:10.3390/ijms26199347. This article has 6 citations.

7. (kamel2021aheterozygousmutation pages 1-2): Sarah M. Kamel, Charlotte D. Koopman, Fabian Kruse, Sven Willekers, Sonja Chocron, and Jeroen Bakkers. A heterozygous mutation in cardiac troponin t promotes ca2+ dysregulation and adult cardiomyopathy in zebrafish. Journal of Cardiovascular Development and Disease, 8:46, Apr 2021. URL: https://doi.org/10.3390/jcdd8040046, doi:10.3390/jcdd8040046. This article has 18 citations.

8. (nakamura2025cardiacmyosininhibitors pages 13-14): Kazufumi Nakamura, Takahiro Okumura, Seiya Kato, Kenji Onoue, Toru Kubo, Hidemichi Kouzu, Toshiyuki Yano, and Takayuki Inomata. Cardiac myosin inhibitors in hypertrophic cardiomyopathy: from sarcomere to clinic. International Journal of Molecular Sciences, 26:9347, Sep 2025. URL: https://doi.org/10.3390/ijms26199347, doi:10.3390/ijms26199347. This article has 6 citations.

9. (ottaviani2023revisitingdiagnosisand pages 23-24): Andrea Ottaviani, Davide Mansour, Lorenzo V. Molinari, Kristian Galanti, Cesare Mantini, Mohammed Y. Khanji, Anwar A. Chahal, Marco Zimarino, Giulia Renda, Luigi Sciarra, Francesco Pelliccia, Sabina Gallina, and Fabrizio Ricci. Revisiting diagnosis and treatment of hypertrophic cardiomyopathy: current practice and novel perspectives. Journal of Clinical Medicine, 12:5710, Sep 2023. URL: https://doi.org/10.3390/jcm12175710, doi:10.3390/jcm12175710. This article has 43 citations.

10. (dolder2025experimentalmodelsof pages 36-36): Floor W. van den Dolder, Rafeeh Dinani, Vincent A.J. Warnaar, Sofija Vučković, Adriana S. Passadouro, Ali A. Nassar, Azhaar X. Ramsaroep, George B. Burchell, Linda J. Schoonmade, Jolanda van der Velden, and Birgit Goversen. Experimental models of hypertrophic cardiomyopathy. JACC: Basic to Translational Science, 10:511-546, Jan 2025. URL: https://doi.org/10.1016/j.jacbts.2024.10.017, doi:10.1016/j.jacbts.2024.10.017. This article has 12 citations.

11. (sanghvi2025hypertrophiccardiomyopathymanagement pages 11-12): Mihir M Sanghvi, Eamon Dhall, C Anwar A. Chahal, Constantinos O'Mahony, Saidi A Mohiddin, Konstantinos Savvatis, Fabrizio Ricci, Patricia B Munroe, Steffen E Petersen, Nay Aung, and Mohammed Y Khanji. Hypertrophic cardiomyopathy management: a systematic review of the clinical practice guidelines and recommendations. European heart journal. Quality of care & clinical outcomes, Jan 2025. URL: https://doi.org/10.1093/ehjqcco/qcae117, doi:10.1093/ehjqcco/qcae117. This article has 15 citations.

12. (nakamura2025cardiacmyosininhibitors pages 11-13): Kazufumi Nakamura, Takahiro Okumura, Seiya Kato, Kenji Onoue, Toru Kubo, Hidemichi Kouzu, Toshiyuki Yano, and Takayuki Inomata. Cardiac myosin inhibitors in hypertrophic cardiomyopathy: from sarcomere to clinic. International Journal of Molecular Sciences, 26:9347, Sep 2025. URL: https://doi.org/10.3390/ijms26199347, doi:10.3390/ijms26199347. This article has 6 citations.

13. (nakamura2025cardiacmyosininhibitors pages 16-18): Kazufumi Nakamura, Takahiro Okumura, Seiya Kato, Kenji Onoue, Toru Kubo, Hidemichi Kouzu, Toshiyuki Yano, and Takayuki Inomata. Cardiac myosin inhibitors in hypertrophic cardiomyopathy: from sarcomere to clinic. International Journal of Molecular Sciences, 26:9347, Sep 2025. URL: https://doi.org/10.3390/ijms26199347, doi:10.3390/ijms26199347. This article has 6 citations.

14. (hou2025cardiacmyosininhibitors pages 12-13): Lianglei Hou, Bin Lin, Xiaojun Ji, and Anwu Huang. Cardiac myosin inhibitors in hypertrophic cardiomyopathy: clinical advances and therapeutic prospects. Drug Design, Development and Therapy, Volume 19:9367-9385, Oct 2025. URL: https://doi.org/10.2147/dddt.s555335, doi:10.2147/dddt.s555335. This article has 7 citations.

## Artifacts

- [Edison artifact artifact-00](Hypertrophic_Cardiomyopathy_2-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 7 |
| Off topic | 0 |

All extracted references resolved successfully.