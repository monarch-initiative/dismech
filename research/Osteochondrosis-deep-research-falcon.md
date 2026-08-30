---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-26T22:17:42.844007'
end_time: '2026-08-26T22:24:54.236095'
duration_seconds: 431.39
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Osteochondrosis
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 14
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
  path: Osteochondrosis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Osteochondrosis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Osteochondrosis** covering all of the
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
- **Disease Name:** Osteochondrosis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Osteochondrosis** covering all of the
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


# Osteochondrosis: comprehensive disease-characteristics report

## Executive summary and scope

**Osteochondrosis is not one homogeneous disease.** In its strict developmental-articular sense, it is a focal disturbance of endochondral ossification in the growing skeleton. Failure of blood supply to epiphyseal cartilage produces chondronecrosis and arrested ossification; mechanical loading may then cause clefting, collapse, an unstable osteochondral fragment, and clinically recognized **osteochondritis dissecans (OCD)**. The term is also applied to anatomically distinct juvenile disorders—such as Legg–Calvé–Perthes, Osgood–Schlatter, Sever, Freiberg, Köhler, and Scheuermann diseases—and, especially in Europe, to adult degenerative spinal disease. These should not be merged into one knowledge-base record. This report therefore focuses on **developmental articular osteochondrosis/OCD**, with other named osteochondroses treated as related but separate entities. (mccoy2013articularosteochondrosisa pages 7-8, mccoy2013articularosteochondrosisa pages 2-4, mccoy2013articularosteochondrosisa pages 1-2)

| Entity/scope | Defining biology | Typical age/sites | KB handling |
|---|---|---|---|
| Developmental articular osteochondrosis (latent/manifesta stages) | Focal disturbance/failure of endochondral ossification in growing epiphyseal or articular-epiphyseal cartilage, linked to cartilage-canal vascular failure and localized chondronecrosis; latent/manifesta represent pre-fracture stages before instability or dissection becomes clinically obvious (mccoy2013articularosteochondrosisa pages 7-8, mccoy2013articularosteochondrosisa pages 2-4, mccoy2013articularosteochondrosisa pages 5-7, mccoy2013articularosteochondrosisa pages 1-2, edmonds2023evaluatingtheetiology pages 1-3) | Usually children/adolescents; classic sites include knee, elbow/capitellum, ankle/talus and other developing joints (konarski2024understandingosteochondritisdissecans pages 1-2, konarski2024understandingosteochondritisdissecans pages 2-3) | Use as the core disease-family concept for developmental articular lesions; record latent/manifesta as upstream pathobiology or stage terms rather than separate unrelated diseases |
| Osteochondritis dissecans (OCD) | Fissured/unstable or fragmenting stage of articular osteochondrosis in which the osteochondral surface becomes unstable, may cleave/dissect, and causes pain, swelling, catching, or locking; often the stage recognized clinically in humans (konarski2024understandingosteochondritisdissecans pages 1-2, mccoy2013articularosteochondrosisa pages 7-8, mccoy2013articularosteochondrosisa pages 2-4, konarski2024understandingosteochondritisdissecans pages 12-13) | Predominantly children/adolescents; most often knee, then elbow and ankle; juvenile form has open physes and better healing potential than adult form (konarski2024understandingosteochondritisdissecans pages 1-2, konarski2024understandingosteochondritisdissecans pages 2-3, konarski2024understandingosteochondritisdissecans pages 12-13) | Represent as a child concept or advanced-stage concept under articular osteochondrosis, with site-specific subrecords (knee OCD, capitellar OCD, talar OCD) when anatomy-specific details differ |
| Named juvenile osteochondroses (e.g., Legg-Calvé-Perthes, Osgood-Schlatter, Sever, Freiberg, Köhler, Scheuermann) | Site-specific pediatric osteochondrosis labels used for distinct anatomic syndromes; they should not be automatically merged with articular osteochondrosis/OCD because biology, anatomy, imaging, natural history, and management differ by entity | Childhood/adolescence; hip/femoral head, tibial tubercle, calcaneal apophysis, metatarsal head, navicular, vertebral endplates depending on syndrome | Curate as separate disease records linked by broader “juvenile osteochondrosis/osteochondrosis” family membership; avoid pooling epidemiology or genetics across these entities without direct evidence |
| Adult spinal “osteochondrosis” terminology | Commonly used degenerative spine terminology rather than the pediatric developmental articular-osteochondrosis process; usage may refer to vertebral endplate/disc degeneration or historical naming conventions rather than OCD biology | Mainly adolescents/adults in the spine, especially thoracic/lumbar vertebral endplates/discs in clinical radiology/orthopedics usage | Keep separate from developmental articular osteochondrosis/OCD in the knowledge base unless a source explicitly addresses Scheuermann-type juvenile vertebral osteochondrosis; do not merge adult degenerative spine usage with pediatric OCD biology |


*Table: This table clarifies how “osteochondrosis” should be scoped in a knowledge base to avoid conflating developmental articular osteochondrosis/OCD with named juvenile osteochondroses or adult degenerative spinal terminology. It is useful for deciding when to create a parent concept versus separate site-specific disease records.*

**Evidence base.** The strongest recent sources retrieved were a 2024 clinical review, a 2023 longitudinal MRI study of lesion development, and the registry record/publication metadata for a 2023 prospective multicenter randomized drilling trial. Mechanistic evidence also relies on a highly cited 2013 comparative pathology review because early human tissue is rarely available. PMID values were not exposed in the retrieved records; DOI links are supplied rather than inventing PMIDs.

---

## 1. Disease information

### Definition

Articular osteochondrosis is a **developmental disorder of epiphyseal growth cartilage** in which focal failure of endochondral ossification creates an abnormally retained, often necrotic cartilage region. Veterinary pathology recognizes a continuum:

1. **Osteochondrosis latens:** microscopic cartilage necrosis, not radiographically visible.
2. **Osteochondrosis manifesta:** retained cartilage or an ossification defect visible radiographically.
3. **Osteochondrosis dissecans/osteochondritis dissecans:** fissuring through cartilage, instability, or separation of an osteochondral fragment.

Human patients are commonly recognized only at the symptomatic OCD stage. “Osteochondritis” is historically entrenched but potentially misleading because primary inflammation is not established; “osteochondrosis dissecans” better reflects the developmental-necrotic process. (mccoy2013articularosteochondrosisa pages 7-8, mccoy2013articularosteochondrosisa pages 2-4, mccoy2013articularosteochondrosisa pages 5-7)

A current clinical definition describes OCD as a focal idiopathic subchondral-bone alteration that threatens articular-surface stability and can culminate in premature osteoarthritis. It primarily affects the knee, elbow, and ankle of children and adolescents. (konarski2024understandingosteochondritisdissecans pages 1-2)

### Identifiers and terminology

- **OMIM 165800:** familial osteochondritis dissecans, associated with **ACAN**. This is a rare Mendelian subtype, not an identifier for all sporadic osteochondrosis. (mccoy2013articularosteochondrosisa pages 5-7)
- **MONDO:** the exact current MONDO accession was not verified in the retrieved evidence and should be resolved directly against the current MONDO release. Do not assign the osteochondritis-dissecans concept to every named juvenile osteochondrosis.
- **MeSH:** Osteochondritis Dissecans is the appropriate literature-indexing concept for clinically dissecting lesions; site-specific juvenile osteochondroses have separate concepts where available.
- **ICD-10-CM:** OCD is generally coded within **M93.2-** (“osteochondritis dissecans”), with site/laterality extensions; other juvenile osteochondroses fall within M91–M93. Exact national extensions must be validated against the implementation in use.
- **ICD-11, SNOMED CT, Orphanet:** use current terminology-service lookups at ingestion. A single Orphanet/OMIM record does not encompass common multifactorial articular OCD.
- **Synonyms:** articular osteochondrosis; osteochondritis dissecans; osteochondrosis dissecans; juvenile OCD/JOCD; adult OCD/AOCD; dissecting osteochondritis.

The evidence summarized here is **aggregated disease-level literature**, not individual-patient EHR data. The 2023 etiologic study is a small patient-level imaging cohort subsequently aggregated for analysis. (edmonds2023evaluatingtheetiology pages 1-3)

> **Exact abstract quotation—2024 review:** “OCD is a joint disorder predominantly affecting the knee, elbow, and ankle of children and adolescents.” (konarski2024understandingosteochondritisdissecans pages 1-2)

---

## 2. Etiology

### Causal and susceptibility factors

Osteochondrosis/OCD is usually **multifactorial**. The best-supported causal model combines developmental vascular vulnerability with mechanical loading:

- **Developmental vascular failure:** interruption of cartilage-canal blood supply causes focal chondrocyte death and failed ossification.
- **Repetitive microtrauma/overuse:** particularly jumping, pivoting, and repetitive throwing. Contemporary clinical literature regards sports-associated repetitive microtrauma as the commonest precipitating exposure.
- **Local ischemia:** predilection sites have vulnerable vascular anatomy.
- **Growth and skeletal immaturity:** lesions arise during active epiphyseal ossification.
- **Obesity:** extreme childhood obesity was associated with an **86% higher risk** in the epidemiologic evidence summarized by the 2024 review.
- **Genetic predisposition:** familial aggregation, concordance in identical twins, rare monogenic ACAN disease, and candidate associations on chromosomes 7 and 13 support inherited susceptibility. Evidence for common sporadic variants remains limited. (konarski2024understandingosteochondritisdissecans pages 2-3, mccoy2013articularosteochondrosisa pages 5-7)

Trauma should be interpreted carefully. Comparative pathology suggests that loading may provoke symptoms or convert a pre-existing necrotic lesion into a fissure, rather than always initiating the earliest lesion. Thus, **vascular injury is upstream**, while repetitive stress often acts as a lesion-progressing factor. (mccoy2013articularosteochondrosisa pages 5-7)

### Protective factors

No validated protective human allele or disease-specific protective diet is established. Plausible environmental protection consists of avoiding excessive repetitive joint loading during vulnerable growth periods, maintaining healthy body mass, varying youth sports, and responding promptly to persistent activity-related joint pain. These are risk-reduction principles, not interventions proven to abolish disease. Animal evidence implicates copper deficiency, excess phosphorus, and excessive dietary energy, but comparable human nutrition studies were not identified. (mccoy2013articularosteochondrosisa pages 5-7)

### Gene–environment interaction

The working model is that genetically influenced matrix quality, vascular anatomy, growth velocity, or endochondral-ossification resilience modifies the effect of mechanical load. In rare ACAN-related disease, abnormal aggrecan weakens cartilage-matrix function; in common sporadic disease, polygenic susceptibility may determine why only some heavily exposed young athletes develop lesions. Definitive human G×E effect estimates are unavailable. (mccoy2013articularosteochondrosisa pages 5-7)

---

## 3. Phenotypes

| Phenotype | Type and characteristics | Suggested HPO term |
|---|---|---|
| Activity-related joint pain | Earliest common symptom; vague and poorly localized, initially intermittent and later persistent | **HP:0002829 Arthralgia** |
| Joint swelling/effusion | Usually activity-associated; may become recurrent | **HP:0001373 Joint swelling** |
| Joint stiffness/restricted movement | More evident with progression | **HP:0001387 Joint stiffness**, **HP:0001376 Limitation of joint mobility** |
| Catching or locking | Mechanical symptom suggesting flap/fragment instability | **HP:0011743 Joint locking** if accepted in local HPO release |
| Reduced function/limp | Site dependent; lower-extremity lesions impair walking, running, and sport | **HP:0002355 Difficulty walking**, **HP:0002750 Delayed skeletal maturation** only when documented |
| Osteochondral defect/subchondral lesion | Imaging/structural phenotype | **HP:0033126 Osteochondritis dissecans** if available in the deployed HPO release |
| Early secondary osteoarthritis | Late complication of persistent or unstable disease | **HP:0002758 Osteoarthritis** |

Onset is usually in childhood or adolescence and peaks around early-to-mid adolescence. Severity ranges from asymptomatic radiographic lesions to severe pain, recurrent effusion, locking, and disability. Bilateral disease occurs but is usually asymmetric. No characteristic behavioral, hematologic, biochemical, or systemic laboratory phenotype exists in isolated disease. (konarski2024understandingosteochondritisdissecans pages 1-2, mccoy2013articularosteochondrosisa pages 2-4)

**Quality of life:** pain interferes with physical function, school sports, competitive participation, and sometimes ordinary walking. Long-term cartilage loss can create chronic pain and early osteoarthritis. Disease-specific EQ-5D or SF-36 population estimates were not identified; orthopedic studies commonly use IKDC, KOOS, Lysholm, activity scales, and site-specific scores. (konarski2024understandingosteochondritisdissecans pages 12-13)

---

## 4. Genetic and molecular information

### Established and candidate genes

- **ACAN** encodes aggrecan, a major cartilage extracellular-matrix proteoglycan. Heterozygous germline pathogenic variants can cause autosomal-dominant familial OCD (OMIM 165800), often with disproportionate short stature and early osteoarthritis. Variant-specific HGVS, ClinVar classification, and gnomAD frequency must be curated from the individual family report; there is no single common causal ACAN allele. The inferred mechanism is altered aggrecan matrix organization/function. (mccoy2013articularosteochondrosisa pages 5-7)
- **COMP:** a 2024 clinical report expanded the phenotype of COMP-related multiple epiphyseal dysplasia to include multiple OCD lesions. This establishes OCD as a possible manifestation of a broader skeletal dysplasia, not COMP as a common cause of isolated sporadic OCD.
- **COL9A2**, and more broadly **COL9A1/COL9A2/COL9A3**, are relevant when OCD co-occurs with multiple epiphyseal dysplasia; knee-predominant disease has been described in collagen-IX-associated MED.
- Common sporadic OCD appears **polygenic**. Candidate signals on chromosomes 7 and 13 are hypothesis-generating and are not diagnostic loci. (konarski2024understandingosteochondritisdissecans pages 2-3, mccoy2013articularosteochondrosisa pages 5-7)

### Variant interpretation

For a patient with isolated, unilateral, sports-associated OCD, routine molecular testing has low expected yield. Testing becomes appropriate for **multifocal or bilateral disease, short stature, epiphyseal dysplasia, premature generalized osteoarthritis, or a strong family history**. A skeletal-dysplasia panel should include ACAN, COMP, COL9A1, COL9A2, and COL9A3, with phenotype-driven expansion. WES/WGS may be considered after negative panel testing in strongly familial disease. CMA, karyotype, FISH, mitochondrial testing, and repeat-expansion testing are not routine without additional syndromic evidence.

No recurrent chromosomal abnormality, somatic mutation, pharmacogenomic marker, proven modifier gene, or clinically validated epigenetic signature is established for common articular osteochondrosis. Allele frequency and ACMG status are **variant-specific** and should never be assigned at gene level.

---

## 5. Environmental information

Relevant exposures are biomechanical rather than toxic or infectious:

- intensive repetitive sport during growth;
- overhead throwing for capitellar lesions;
- basketball and soccer participation for knee lesions;
- high body mass/mechanical loading;
- possible malalignment or site-specific biomechanics.

Smoking, alcohol, pollution, ionizing radiation, occupational toxins, and infectious agents are not established primary causes of developmental articular osteochondrosis. The disorder is not contagious, vaccine-preventable, or zoonotic. Nutritional abnormalities are supported mainly in livestock models and should not be extrapolated directly to children. (konarski2024understandingosteochondritisdissecans pages 2-3, mccoy2013articularosteochondrosisa pages 5-7)

---

## 6. Mechanism and pathophysiology

### Causal chain

1. **Growing epiphyseal cartilage depends on cartilage-canal vessels.** During development, blood supply transitions from perichondrial vessels toward medullary vessels.
2. **Vascular interruption or failed vascular transition** produces focal ischemia.
3. **Chondronecrosis** develops around affected canals.
4. Necrotic cartilage **fails to undergo normal endochondral ossification**, creating retained cartilage and an irregular subchondral-bone front.
5. Continued growth and mechanical loading cause **resorption, collapse, clefting, and sequestrum formation**.
6. A stable lesion may heal through revascularization; a narrow, avascular attachment is prone to instability and dissection.
7. Fragmentation damages the articular surface, producing pain, effusion, mechanical locking, and ultimately **secondary osteoarthritis**. (mccoy2013articularosteochondrosisa pages 7-8, mccoy2013articularosteochondrosisa pages 9-11, mccoy2013articularosteochondrosisa pages 5-7)

The 2023 longitudinal MRI study provides recent human support for a lesion arising at the articular–epiphyseal cartilage complex. Six children with seven knees had pre-OCD MRI at a median age of **11.6 years** and follow-up about **1.9 years** later. Every lesion increased in depth; depth changed significantly in coronal and sagittal planes (**p=0.029** and **p=0.026**). Variable patterns—continued ossification, arrested progression, or regression near the lesion—support heterogeneous responses or multiple etiologic routes. (edmonds2023evaluatingtheetiology pages 1-3)

### Cells, processes, and ontology suggestions

- **Cells:** epiphyseal/articular chondrocytes (**CL:0000138 chondrocyte**), vascular endothelial cells (**CL:0000115 endothelial cell**), osteoblast-lineage cells (**CL:0000062 osteoblast**), osteoclasts (**CL:0000092 osteoclast**).
- **GO biological processes:** endochondral ossification (**GO:0001958**), cartilage development (**GO:0051216**), blood-vessel development (**GO:0001568**), chondrocyte differentiation (**GO:0002062**), response to hypoxia (**GO:0001666**), cell death (**GO:0008219**), extracellular-matrix organization (**GO:0030198**), bone remodeling (**GO:0046849**).
- **Cellular compartments:** extracellular matrix (**GO:0031012**), collagen-containing extracellular matrix (**GO:0062023**), aggrecan-rich cartilage matrix, and cell–matrix interfaces.

Primary immune autoimmunity is not established. Inflammation may occur downstream after fissuring or synovial irritation. No disease-specific metabolic, proteomic, lipidomic, single-cell, spatial-transcriptomic, CRISPR-screen, or multi-omic diagnostic signature has entered practice.

---

## 7. Anatomical structures affected

The principal structures are **articular cartilage, epiphyseal growth cartilage, subchondral bone, and the osteochondral junction**. Common sites are:

- **Knee:** classically the lateral aspect of the medial femoral condyle; the medial femoral condyle accounts for approximately **66.2%** of knee lesions.
- **Elbow:** capitellum, particularly in throwing athletes.
- **Ankle:** talar dome.
- Less commonly: patella, trochlea, femoral head, shoulder, and multifocal sites. (konarski2024understandingosteochondritisdissecans pages 1-2, konarski2024understandingosteochondritisdissecans pages 2-3)

Suggested UBERON mappings include **knee joint (UBERON:0001465)**, **elbow joint (UBERON:0001461)**, **ankle joint**, **articular cartilage (UBERON:0001997)**, **epiphysis**, **subchondral bone**, **femoral condyle**, **capitulum of humerus**, and **talus**; identifiers should be validated against the deployed UBERON release. Disease may be unilateral or bilateral, but bilateral lesions are often asymmetric. (mccoy2013articularosteochondrosisa pages 2-4)

---

## 8. Temporal development

Onset is insidious during skeletal growth. Early lesions may be asymptomatic and invisible on radiographs. Symptomatic progression typically moves from activity-related pain to recurrent swelling and stiffness, then catching/locking as instability develops. (konarski2024understandingosteochondritisdissecans pages 1-2, mccoy2013articularosteochondrosisa pages 2-4)

The practical stages are latent → manifesta → stable OCD → unstable/displaced OCD → secondary osteoarthritis. Skeletally immature patients with open physes have greater healing potential than adults. Animal and comparative evidence indicates a species-specific **critical age** after which persistent lesions are unlikely to resolve; in humans this corresponds broadly to diminishing healing potential as physeal closure approaches. Stable, broadly attached, vascularized lesions may heal, whereas narrow, avascular, unstable fragments seldom heal completely. (mccoy2013articularosteochondrosisa pages 9-11)

The principal intervention window is **before physeal closure and before cartilage breach or fragment displacement**. There is no relapsing-remitting systemic course; apparent remission generally reflects lesion healing or successful treatment.

---

## 9. Inheritance and population epidemiology

### Epidemiology

Recent synthesis reports:

- Knee OCD prevalence/incidence estimates vary substantially, approximately **2.3–31.6 per million** in some datasets.
- Peak frequency is at **12–16 years**, approximately **11.2 per 100,000**.
- Males have about **3.8-fold** greater risk than females.
- Capitellar OCD incidence is approximately **6.0 per 100,000** overall—**9.5 per 100,000 males** and **2.6 per 100,000 females**.
- Ankle OCD incidence is approximately **4.6 per 100,000** among persons aged 6–19 years.
- Across human series, females comprise roughly **20–40%** of cases. (mccoy2013articularosteochondrosisa pages 9-11, konarski2024understandingosteochondritisdissecans pages 2-3)

Differences in case definitions, joint site, age window, imaging intensity, and athlete enrichment explain much of the heterogeneity. Population-wide prevalence of the broader “osteochondrosis” family cannot be calculated meaningfully by pooling all named juvenile disorders.

### Inheritance

Most isolated disease is multifactorial/polygenic with incomplete penetrance and variable expressivity. Rare ACAN-associated familial OCD is autosomal dominant. Genetic anticipation, germline mosaicism, founder mutations, consanguinity effects, and general-population carrier frequencies are not established features. Strong family history or multifocal disease should prompt evaluation for skeletal dysplasia. (mccoy2013articularosteochondrosisa pages 5-7)

---

## 10. Diagnostics

### Clinical assessment

Suspect OCD in a growing child or adolescent with persistent, activity-related joint pain, recurrent effusion, loss of motion, or mechanical catching/locking—particularly an athlete. Examination may show tenderness, swelling, reduced range of motion, gait alteration, or pain at terminal flexion/extension, but no finding is sufficiently sensitive to exclude disease. (konarski2024understandingosteochondritisdissecans pages 1-2, mccoy2013articularosteochondrosisa pages 2-4)

### Imaging

1. **Plain radiography:** first-line; use site-appropriate orthogonal and specialized views. It detects manifesta lesions, sclerosis, lucency, and fragments but can miss early disease.
2. **MRI:** preferred for early detection and assessment of lesion size, cartilage integrity, marrow/subchondral changes, fluid undermining the fragment, and stability. MRI is more sensitive than radiography for early lesions.
3. **CT:** useful for osseous architecture, fragments, cysts, and operative planning, but exposes the child to radiation.
4. **Ultrasound:** limited adjunct for superficial lesions/effusion; not a definitive staging test.
5. **Arthroscopy:** direct assessment and treatment; often the definitive stability assessment when imaging is equivocal. (konarski2024understandingosteochondritisdissecans pages 1-2, mccoy2013articularosteochondrosisa pages 2-4)

There is no diagnostic blood test, enzyme assay, circulating biomarker, liquid biopsy, or validated omics assay. Biopsy is not routinely required; histology, when available, shows retained/necrotic cartilage, failed ossification, clefts, fibrous repair, and variable subchondral remodeling.

### Differential diagnosis

Differentials include acute osteochondral fracture, osteonecrosis, stress injury, normal ossification variants, infection, inflammatory arthritis, meniscal pathology, plica, loose body, chondral tumor, and site-specific conditions such as talar osteochondral lesions. Clinical context, lesion location, cartilage integrity, marrow reaction, and trauma history distinguish these.

### Genetic diagnosis and screening

No population, newborn, or routine athlete-screening program is recommended. Contralateral-joint imaging may be considered when symptoms, multifocal disease, or familial disease suggest bilateral involvement. Genetic testing is phenotype-driven rather than routine.

---

## 11. Outcomes and prognosis

Osteochondrosis is generally **not life-limiting**; disease-specific mortality, reduced life expectancy, and survival rates are not meaningful endpoints. Morbidity arises from pain, sports restriction, stiffness, mechanical symptoms, surgery, and premature osteoarthritis.

Favorable prognostic factors include young skeletal age, open physes, early diagnosis, small stable lesion, intact cartilage, broad vascular attachment, and adherence to unloading. Unfavorable factors include physeal closure, large or atypically located lesions, cysts/sclerosis, instability, displacement, long symptom duration, and failed conservative care. Early detection is emphasized because fragmentation produces permanent cartilage injury and joint degeneration. (mccoy2013articularosteochondrosisa pages 9-11, konarski2024understandingosteochondritisdissecans pages 12-13)

Recovery is common for stable juvenile lesions, but exact healing rates depend heavily on joint, MRI definition, follow-up duration, and treatment. Unstable lesions are less likely to heal without fixation or restoration. No validated molecular prognostic biomarker exists.

---

## 12. Treatment

### Treatment algorithm

**Stable lesion, open physis, mild symptoms:**

- cessation of impact/throwing exposure;
- protected weight bearing or immobilization when indicated;
- analgesia/short-term NSAIDs for symptoms;
- progressive physical therapy emphasizing range of motion, strength, and biomechanics;
- serial clinical and radiographic/MRI assessment;
- gradual return only after pain resolution and evidence of healing. The 2024 review recommends that return to sport occur only after symptoms resolve and at least **six months** have elapsed. (konarski2024understandingosteochondritisdissecans pages 1-2)

**Persistent stable lesion:** arthroscopic or image-guided **retroarticular/retrograde or transarticular drilling** to stimulate revascularization and healing.

**Unstable but salvageable lesion:** reduction, debridement of nonviable interface, drilling/bone grafting as needed, and fixation with screws, pins, or anchors.

**Unsavable defect:** fragment excision plus cartilage-restoration strategy selected by size, depth, site, and age—microfracture/marrow stimulation, osteochondral autograft or allograft, autologous chondrocyte implantation, scaffold-assisted repair, or combined bone/cartilage reconstruction. (konarski2024understandingosteochondritisdissecans pages 1-2, konarski2024understandingosteochondritisdissecans pages 12-13)

### Evidence and clinical trials

The multicenter ROCK trial, **NCT01754298**, enrolled 91 participants and compared transarticular with retroarticular drilling for stable juvenile knee OCD. It was published in May 2023 in *The American Journal of Sports Medicine*, 51:1392–1402, DOI [10.1177/03635465231165290](https://doi.org/10.1177/03635465231165290). The retrieved registry excerpt confirms the randomized comparison but did not expose arm-specific numerical outcomes; these should be abstracted from the full publication before entering response rates. (NCT01754298 chunk 2)

Other registered studies retrieved included platelet-rich plasma for juvenile knee OCD (**NCT02397278**, completed, 15 participants) and withdrawn demineralized bone matrix work (**NCT01283737**, 0 enrolled). These remain investigational and do not establish standard efficacy.

No approved disease-modifying drug, gene therapy, RNA therapy, immunotherapy, or genotype-guided pharmacotherapy exists. Cell/scaffold and orthobiologic procedures are cartilage-repair technologies rather than corrections of the initiating developmental vascular defect.

Suggested NCIt intervention mappings: **Activity Modification**, **Physical Therapy**, **Immobilization**, **Arthroscopy**, **Internal Fixation Procedure**, **Bone Grafting**, **Microfracture**, **Osteochondral Autograft Transplantation**, **Osteochondral Allograft Transplantation**, and **Autologous Chondrocyte Implantation**; codes should be resolved in the current NCIt release.

---

## 13. Prevention

### Primary prevention

No intervention completely prevents multifactorial disease. Reasonable measures include healthy body weight, diversified age-appropriate activity, limits on repetitive throwing/jumping load, scheduled rest, progressive training, attention to alignment and technique, and avoidance of premature single-sport overuse. Evidence is risk-factor based rather than derived from definitive prevention trials. (konarski2024understandingosteochondritisdissecans pages 2-3)

### Secondary prevention

Prompt evaluation of persistent activity-related pain or recurrent swelling, low threshold for MRI when radiographs are normal but suspicion remains, and early unloading of stable lesions may prevent progression to instability. There is no justified general-population imaging screen. (mccoy2013articularosteochondrosisa pages 2-4, konarski2024understandingosteochondritisdissecans pages 12-13)

### Tertiary prevention

Protect healing lesions, monitor radiographic resolution, rehabilitate strength and motion, correct modifiable biomechanics, and delay return to high-impact sport until clinical and imaging recovery. The goal is prevention of fragmentation and secondary osteoarthritis. Genetic counseling is appropriate for ACAN-associated or skeletal-dysplasia-associated familial disease.

Vaccination, antimicrobial prophylaxis, environmental decontamination, and infectious-disease public-health measures are not applicable.

---

## 14. Other species and natural disease

Naturally occurring articular osteochondrosis is important in **horses (*Equus caballus*, NCBI Taxon 9796)**, **domestic pigs (*Sus scrofa domesticus*; parent taxon *Sus scrofa*, 9823)**, and dogs; analogous lesions also occur in production animals. Veterinary consequences include pain/lameness, reduced athletic performance, welfare problems, and economic loss.

Human, equine, and porcine disease share predilection sites, imaging and histologic features, focal cartilage avascular necrosis, failed endochondral ossification, and progression to cartilage fissure. Females are less frequently affected in humans and pigs, whereas equine disease shows no consistent sex difference. Estimated heritability in horses and pigs ranges from **0.14 to 0.52**; reports indicate up to **70% of foals from affected sires** may develop lesions and affected offspring may be approximately twice as likely as unaffected offspring. These values are population- and phenotype-dependent and should not be transferred to humans. (mccoy2013articularosteochondrosisa pages 7-8, mccoy2013articularosteochondrosisa pages 9-11, mccoy2013articularosteochondrosisa pages 5-7)

There is no transmission or zoonotic potential: cross-species similarity reflects conserved endochondral ossification, not infection. Breed-specific VBO identifiers and animal ortholog NCBI Gene IDs should be attached only after breed- and gene-specific database verification.

---

## 15. Model organisms and experimental systems

### Natural and induced models

- **Pig and horse natural disease:** best models of early lesion formation because large epiphyses and cartilage canals permit serial imaging and histopathology before clinical end-stage disease.
- **Surgical vascular-interruption models:** transection of epiphyseal cartilage vessels reproduces focal ischemic chondronecrosis and delayed ossification, strongly supporting vascular failure as an upstream mechanism.
- **Large-animal drilling/cartilage-repair models:** sheep, pigs, goats, and horses are used to test revascularization, fixation, scaffolds, and osteochondral repair.
- **Rodents:** convenient for molecular manipulation but less faithful because epiphyseal scale, loading, and cartilage-canal biology differ.
- **In vitro chondrocytes, osteochondral explants, and organoids:** useful for matrix, hypoxia, and mechanobiology, but cannot fully reproduce joint vascular transition and growth-related loading. (mccoy2013articularosteochondrosisa pages 7-8, mccoy2013articularosteochondrosisa pages 1-2)

### Strengths and limitations

Natural large-animal disease reproduces the temporal sequence from latent vascular lesions to dissection and permits study of tissue unavailable from presymptomatic children. Limitations include species-specific growth rates, joint loading, predilection sites, husbandry, nutrition, and genetic architecture. Surgically induced vessel injury tests the ischemic mechanism but may over-simplify multifactorial human disease. (mccoy2013articularosteochondrosisa pages 9-11, mccoy2013articularosteochondrosisa pages 1-2)

---

## Recent developments and expert interpretation

1. **Developmental-complex model strengthened (2023):** serial human MRI demonstrated increasing lesion depth and heterogeneous changes at the articular–epiphyseal cartilage complex, favoring a dynamic developmental lesion rather than a single acute traumatic event. (edmonds2023evaluatingtheetiology pages 1-3)
2. **Comparative mechanism remains influential:** vascular failure and chondronecrosis provide the most coherent upstream mechanism; repetitive load explains why lesions at mechanically vulnerable sites become symptomatic or unstable. (mccoy2013articularosteochondrosisa pages 7-8, mccoy2013articularosteochondrosisa pages 5-7)
3. **Treatment evidence improved:** the 2023 multicenter randomized drilling trial directly compared two accepted approaches, although full numerical outcomes require extraction from the paper rather than the registry excerpt. (NCT01754298 chunk 2)
4. **Genetic phenotypic expansion (2024):** reports of multiple OCD in COMP-associated multiple epiphyseal dysplasia reinforce that multifocal disease should trigger skeletal-dysplasia assessment.
5. **Clinical consensus (2024):** age, physeal status, lesion stability, cartilage integrity, size, and location—not the label alone—should drive treatment. Stable juvenile lesions merit conservative care; unstable or displaced lesions require restoration of surface congruity and fixation when salvageable. (konarski2024understandingosteochondritisdissecans pages 1-2, konarski2024understandingosteochondritisdissecans pages 12-13)

## Principal knowledge gaps

Major gaps include validated sporadic-risk loci, prospective gene–environment studies, standardized incidence estimates, biomarkers of instability, direct early-stage human histology, harmonized MRI criteria, long-term comparative effectiveness of cartilage-restoration methods, disease-specific quality-of-life data, and preventive trials in high-risk youth athletes. Evidence is particularly sparse for protective genetics, epigenomics, single-cell/spatial profiling, and genotype-guided therapy.

References

1. (mccoy2013articularosteochondrosisa pages 7-8): A.M. McCoy, F. Toth, N.I. Dolvik, S. Ekman, J. Ellermann, K. Olstad, B. Ytrehus, and C.S. Carlson. Articular osteochondrosis: a comparison of naturally-occurring human and animal disease. Osteoarthritis and cartilage, 21 11:1638-47, Nov 2013. URL: https://doi.org/10.1016/j.joca.2013.08.011, doi:10.1016/j.joca.2013.08.011. This article has 161 citations and is from a domain leading peer-reviewed journal.

2. (mccoy2013articularosteochondrosisa pages 2-4): A.M. McCoy, F. Toth, N.I. Dolvik, S. Ekman, J. Ellermann, K. Olstad, B. Ytrehus, and C.S. Carlson. Articular osteochondrosis: a comparison of naturally-occurring human and animal disease. Osteoarthritis and cartilage, 21 11:1638-47, Nov 2013. URL: https://doi.org/10.1016/j.joca.2013.08.011, doi:10.1016/j.joca.2013.08.011. This article has 161 citations and is from a domain leading peer-reviewed journal.

3. (mccoy2013articularosteochondrosisa pages 1-2): A.M. McCoy, F. Toth, N.I. Dolvik, S. Ekman, J. Ellermann, K. Olstad, B. Ytrehus, and C.S. Carlson. Articular osteochondrosis: a comparison of naturally-occurring human and animal disease. Osteoarthritis and cartilage, 21 11:1638-47, Nov 2013. URL: https://doi.org/10.1016/j.joca.2013.08.011, doi:10.1016/j.joca.2013.08.011. This article has 161 citations and is from a domain leading peer-reviewed journal.

4. (mccoy2013articularosteochondrosisa pages 5-7): A.M. McCoy, F. Toth, N.I. Dolvik, S. Ekman, J. Ellermann, K. Olstad, B. Ytrehus, and C.S. Carlson. Articular osteochondrosis: a comparison of naturally-occurring human and animal disease. Osteoarthritis and cartilage, 21 11:1638-47, Nov 2013. URL: https://doi.org/10.1016/j.joca.2013.08.011, doi:10.1016/j.joca.2013.08.011. This article has 161 citations and is from a domain leading peer-reviewed journal.

5. (edmonds2023evaluatingtheetiology pages 1-3): Eric W. Edmonds, Marc Tompkins, James D. Bomar, and Andrew T. Pennock. Evaluating the etiology of osteochondritis dissecans of the knee: the role of the articular-epiphyseal cartilage complex. Journal of the Pediatric Orthopaedic Society of North America, 5(4):677, Nov 2023. URL: https://doi.org/10.55275/jposna-2023-677, doi:10.55275/jposna-2023-677. This article has 2 citations.

6. (konarski2024understandingosteochondritisdissecans pages 1-2): Wojciech Konarski, Tomasz Poboży, Klaudia Konarska, Michał Derczyński, and Ireneusz Kotela. Understanding osteochondritis dissecans: a narrative review of the disease commonly affecting children and adolescents. Apr 2024. URL: https://doi.org/10.3390/children11040498, doi:10.3390/children11040498. This article has 15 citations.

7. (konarski2024understandingosteochondritisdissecans pages 2-3): Wojciech Konarski, Tomasz Poboży, Klaudia Konarska, Michał Derczyński, and Ireneusz Kotela. Understanding osteochondritis dissecans: a narrative review of the disease commonly affecting children and adolescents. Apr 2024. URL: https://doi.org/10.3390/children11040498, doi:10.3390/children11040498. This article has 15 citations.

8. (konarski2024understandingosteochondritisdissecans pages 12-13): Wojciech Konarski, Tomasz Poboży, Klaudia Konarska, Michał Derczyński, and Ireneusz Kotela. Understanding osteochondritis dissecans: a narrative review of the disease commonly affecting children and adolescents. Apr 2024. URL: https://doi.org/10.3390/children11040498, doi:10.3390/children11040498. This article has 15 citations.

9. (mccoy2013articularosteochondrosisa pages 9-11): A.M. McCoy, F. Toth, N.I. Dolvik, S. Ekman, J. Ellermann, K. Olstad, B. Ytrehus, and C.S. Carlson. Articular osteochondrosis: a comparison of naturally-occurring human and animal disease. Osteoarthritis and cartilage, 21 11:1638-47, Nov 2013. URL: https://doi.org/10.1016/j.joca.2013.08.011, doi:10.1016/j.joca.2013.08.011. This article has 161 citations and is from a domain leading peer-reviewed journal.

10. (NCT01754298 chunk 2): Benton Heyworth. Study of Two Surgical Drilling Techniques to Treat Juvenile Osteochondritis Dissecans of the Knee. Boston Children's Hospital. 2013. ClinicalTrials.gov Identifier: NCT01754298

## Artifacts

- [Edison artifact artifact-00](Osteochondrosis-deep-research-falcon_artifacts/artifact-00.md)

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