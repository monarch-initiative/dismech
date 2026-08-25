---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-17T21:10:22.919000'
end_time: '2026-08-17T21:18:40.900844'
duration_seconds: 497.98
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Jervell and Lange-Nielsen Syndrome 2
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 18
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
  path: Jervell_and_Lange-Nielsen_Syndrome_2-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Jervell and Lange-Nielsen Syndrome 2
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Jervell and Lange-Nielsen Syndrome 2** covering all of the
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
- **Disease Name:** Jervell and Lange-Nielsen Syndrome 2
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Jervell and Lange-Nielsen Syndrome 2** covering all of the
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


# Jervell and Lange-Nielsen syndrome 2: disease-characteristics report

## Executive summary and evidence scope

Jervell and Lange-Nielsen syndrome 2 (JLNS2) is an exceptionally rare, severe, autosomal-recessive cardio-auditory channelopathy caused by **biallelic pathogenic loss-of-function variants in *KCNE1***. Its defining combination is **congenital, usually profound bilateral sensorineural hearing loss** and **long-QT syndrome (LQTS)**, which predisposes to torsades de pointes, ventricular fibrillation, syncope, seizure-like episodes, cardiac arrest, and sudden death. It must be distinguished from **JLNS1**, caused by biallelic *KCNQ1* variants, and from autosomal-dominant *KCNE1*-related Romano-Ward syndrome/LQT5, which lacks congenital deafness. The strongest JLNS2-specific clinical evidence remains small family series rather than large cohorts; therefore, numerical prognosis and most treatment recommendations necessarily derive from JLNS overall or congenital LQTS guidance and are labeled accordingly. (faridi2019mutationalandphenotypic pages 9-11, faridi2019mutationalandphenotypic pages 8-9, faridi2019mutationalandphenotypic pages 1-3)

| Domain | Database-ready summary | Key ontology / identifiers | Evidence type | Key citations |
|---|---|---|---|---|
| Identity | Jervell and Lange-Nielsen syndrome 2 (JLNS2) is a rare cardio-auditory channelopathy defined by congenital profound bilateral sensorineural hearing loss plus long-QT syndrome with risk of ventricular arrhythmia and sudden death; it is distinct from JLNS1, which is caused by biallelic KCNQ1 variants. | OMIM: 612347; MONDO: disease-level JLNS available as MONDO_0002441; HPO candidates: congenital sensorineural hearing impairment, long QT interval | Human clinical families; disease-gene curation | (faridi2019mutationalandphenotypic pages 1-3, OpenTargets Search: Jervell and Lange-Nielsen syndrome-KCNE1) |
| Causal gene / inheritance | Cause: biallelic loss-of-function variants in KCNE1, encoding the potassium voltage-gated channel subfamily E regulatory subunit 1, an accessory subunit for KCNQ1/Kv7.1. Inheritance is autosomal recessive; heterozygous loss-of-function carriers may have normal hearing and normal QT, while some heterozygous missense alleles can cause Romano-Ward syndrome via dominant-negative effects. | Gene: KCNE1; HGNC-approved symbol: KCNE1; HPO candidate: autosomal recessive inheritance | Human clinical genetics; mechanistic interpretation | (faridi2019mutationalandphenotypic pages 1-3, faridi2019mutationalandphenotypic pages 8-9, faridi2019mutationalandphenotypic pages 9-11) |
| Cardinal phenotypes | Core phenotype is congenital, severe-to-profound, bilateral sensorineural deafness with prolonged QTc. Reported JLNS2 families had QTcF about 487-495 ms and QTcB about 503-518 ms; syncopal events may be absent in some genetically confirmed cases, so hearing-loss-first presentation is possible. | HPO candidates: profound sensorineural hearing impairment; bilateral hearing impairment; long QT interval; syncope; sudden cardiac death | Human clinical families | (faridi2019mutationalandphenotypic pages 8-9, faridi2019mutationalandphenotypic pages 1-3) |
| Mechanism / pathophysiology | Upstream defect: KCNE1 deficiency impairs the IKs channel complex with KCNQ1. In heart, reduced repolarizing current delays ventricular repolarization, prolonging QT and increasing torsades/ventricular arrhythmia risk. In inner ear stria vascularis, KCNE1/KCNQ1 dysfunction disrupts K+ secretion into endolymph and collapses the endocochlear potential required for hair-cell depolarization, causing deafness; paralog compensation appears insufficient in inner ear. | GO candidates: potassium ion transmembrane transport; regulation of cardiac action potential repolarization; sensory perception of sound; CL candidate: strial marginal cell; UBERON candidate: stria vascularis, cochlea, heart ventricle | Human molecular genetics; animal model; auditory cell biology | (faridi2019mutationalandphenotypic pages 9-11, faridi2019mutationalandphenotypic pages 3-4) |
| Diagnostic anchors | Diagnostic confirmation rests on syndromic phenotype plus ECG and molecular testing. Contemporary congenital LQTS anchors: QTc ≥480 ms, or modified Schwartz score >3; in symptomatic patients, QTc ≥460 ms can suffice. Because a proportion of gene-confirmed LQTS can have normal-range resting QTc, KCNE1-inclusive NGS panels/exome testing are important in deaf children or families with cardio-auditory findings. | HPO candidates: abnormal electrocardiogram, long QT interval; test concepts: ECG, molecular genetic testing | Human clinical guidelines/review; human genetic diagnosis | (balestra2024congenitallongqt pages 4-5, balestra2024congenitallongqt pages 5-8, qiu2020jervellandlangenielsen pages 1-2) |
| Standard management | Management is largely extrapolated from congenital LQTS/JLNS practice: nonselective beta-blockers (nadolol or propranolol) are first-line; avoidance of QT-prolonging drugs and trigger management are standard. ICD is recommended after cardiac arrest and considered for persistent symptoms despite beta-blockers; left cardiac sympathetic denervation is used when events recur or ICD is unsuitable. Cochlear implantation can improve hearing, but peri-anesthetic arrhythmia risk requires careful planning and monitoring. | NCIT candidates: Beta Adrenergic Receptor Blocking Agent Therapy; Implantable Cardioverter Defibrillator; Sympathectomy; Cochlear Implantation | Guidelines/review; case report real-world implementation | (balestra2024congenitallongqt pages 5-8, balestra2024congenitallongqt pages 8-9, qiu2020jervellandlangenielsen pages 5-7) |
| Emerging research / latest developments | Recent work emphasizes precision medicine in congenital LQTS using patient-specific iPSC-derived cardiomyocytes, CRISPR-enabled variant validation, and high-throughput drug testing. A completed 2024 phase 4 JLNS trial tested acute IV diltiazem effects on QT interval in 1 genetically confirmed adult participant; results were submitted for publication after trial completion. | Research concepts: iPSC disease modeling; CRISPR genome editing; ClinicalTrials.gov NCT06534671 | In vitro precision-medicine review; clinical trial | (yu2023precisionmedicinefor pages 1-2, yu2023precisionmedicinefor pages 7-8, NCT06534671 chunk 1) |
| Major evidence gaps | JLNS2-specific epidemiology, penetrance, carrier frequency, founder-variant frequencies, longitudinal survival, quality-of-life metrics, and genotype-specific treatment outcomes remain sparse because published evidence is limited to few families/case-based data. No confident JLNS2-specific epigenomic, transcriptomic, proteomic, metabolomic, or large natural-history datasets were identified in the retrieved evidence. | No supported disease-specific ontology additions beyond above | Evidence-gap synthesis | (faridi2019mutationalandphenotypic pages 1-3, faridi2019mutationalandphenotypic pages 8-9, NCT06534671 chunk 1) |


*Table: This table summarizes the most actionable database-ready facts for Jervell and Lange-Nielsen syndrome 2, including identity, gene, mechanism, diagnosis, management, recent research, and explicit evidence gaps. It is designed to support structured knowledge-base entry creation while avoiding unsupported identifiers.*

## 1. Disease information

### Definition and identifiers

* **Preferred name:** Jervell and Lange-Nielsen syndrome 2
* **Synonyms:** JLNS2; Jervell and Lange-Nielsen syndrome type 2; *KCNE1*-related Jervell–Lange-Nielsen syndrome; autosomal-recessive long-QT syndrome with deafness caused by *KCNE1*.
* **OMIM:** **612347**.
* **MONDO:** The retrieved disease-level record is **MONDO:0002441, Jervell and Lange-Nielsen syndrome**. A securely verified subtype-specific MONDO identifier for JLNS2 was not recovered; the knowledge base should not substitute the JLNS1 record MONDO:0024540.
* **Orphanet:** JLNS is represented as a rare syndromic long-QT disorder, but a securely verified type-2-specific ORPHA identifier was not recovered in this search.
* **ICD-10/ICD-11:** No dedicated JLNS2 code was identified. Coding generally combines congenital long-QT syndrome/cardiac arrhythmia and sensorineural hearing-loss concepts.
* **MeSH:** No securely verified JLNS2-specific descriptor was identified; “Long QT Syndrome” and “Hearing Loss, Sensorineural” are appropriate indexing concepts.

Open Targets identifies *KCNE1* (ENSG00000180509) as the principal evidence-supported target for the general JLNS record, with an association score of 0.804 and supporting literature including PMID **30461122**. Low-scoring neighboring-gene associations in that resource should not be interpreted as additional causal JLNS2 genes. (OpenTargets Search: Jervell and Lange-Nielsen syndrome-KCNE1)

The information here is **aggregated disease-level evidence** from literature, disease resources, and trial registries. Individual-patient evidence appears only in published family/case reports and is not derived from an accessible EHR cohort.

## 2. Etiology, risk, and protective factors

### Primary cause

JLNS2 results from **germline biallelic *KCNE1* pathogenic variants**, usually homozygous in consanguineous families or compound heterozygous. *KCNE1* encodes the minK regulatory β-subunit of the KCNQ1/Kv7.1 potassium channel complex. Biallelic loss reduces the slow delayed-rectifier potassium current, **I(Ks)**. (faridi2019mutationalandphenotypic pages 9-11, faridi2019mutationalandphenotypic pages 1-3)

The key publication states directly: “**Both KCNE1 and KCNQ1 are necessary for normal hearing and cardiac ventricular repolarization**” and that “**biallelic null alleles are associated with JLNS2**.” This is human clinical-genetic evidence from Faridi et al., *Human Mutation*, published December 2019, PMID **30461122**, DOI: https://doi.org/10.1002/humu.23689. (faridi2019mutationalandphenotypic pages 1-3)

### Genetic risk factors

* Two pathogenic/likely pathogenic alleles in trans are the defining risk factor.
* Published homozygous nonsense alleles include **NM_000219:c.50G>A (p.Trp17Ter), c.51G>A (p.Trp17Ter), and c.138C>A (p.Tyr46Ter)**. These are predicted null alleles producing severe N-terminal truncation. (faridi2019mutationalandphenotypic pages 8-9, faridi2019mutationalandphenotypic pages 1-3)
* Missense, splice, frameshift, and other truncating variants can be disease-causing, but each should be classified under current ACMG/AMP and ClinGen specifications rather than assumed pathogenic solely because it occurs in *KCNE1*.
* Heterozygous relatives carrying a null allele may have normal hearing and normal QT. Conversely, some heterozygous missense variants produce autosomal-dominant LQTS/Romano-Ward syndrome through a dominant-negative effect. Thus, dosage, variant mechanism, and functional evidence matter. (faridi2019mutationalandphenotypic pages 8-9, faridi2019mutationalandphenotypic pages 1-3)
* The common *KCNE1* p.Asp85Asn allele can modify repolarization in broader LQTS populations, but it is not by itself an established cause of recessive JLNS2 in the evidence reviewed.

Population allele frequencies must be retrieved variant-by-variant from the current gnomAD release. A single JLNS2-wide carrier frequency cannot be assigned from the available evidence. Causal alleles are expected to be individually rare; variants too common for a severe recessive cardio-auditory disorder require reassessment.

### Modifiers, environment, and protection

No JLNS2-specific modifier gene has been validated. Variability among individuals with *KCNE1* deficiency implies additional genetic, physiologic, treatment, or exposure modifiers, but the evidence is insufficient for a curated modifier annotation. The apparent capacity of other KCNE paralogs to compensate partially in heart—but not in inner ear—is a mechanistic hypothesis, not a clinically validated protective genotype. (faridi2019mutationalandphenotypic pages 8-9, faridi2019mutationalandphenotypic pages 3-4)

Environmental factors do **not cause** JLNS2, but can expose its arrhythmia substrate. Relevant triggers include exertion, swimming, emotional stress, sudden auditory stimuli, fever, electrolyte depletion, anesthesia, and QT-prolonging medication. Maintaining normal potassium and magnesium, avoiding QT-prolonging drugs, adherence to β-blockade, and trigger-specific precautions reduce event risk but do not prevent congenital deafness or remove the genotype. (balestra2024congenitallongqt pages 5-8, balestra2024congenitallongqt pages 4-5, qiu2020jervellandlangenielsen pages 5-7)

Smoking, diet, alcohol, infection, pollution, radiation, and occupational exposure have no established etiologic role. Infection matters only indirectly through fever, dehydration, electrolyte disturbance, or exposure to QT-prolonging antimicrobials.

## 3. Phenotypes

### Cardinal manifestations

| Phenotype | Type and course | Frequency/evidence | Suggested HPO term |
|---|---|---|---|
| Congenital bilateral sensorineural deafness | Physical/functional; present at birth, severe-to-profound and generally permanent | Defining feature in reported JLNS2; homozygous null families had severe-to-profound deafness | Congenital sensorineural hearing impairment; profound sensorineural hearing impairment; bilateral hearing impairment |
| Long QT interval | ECG abnormality; congenital substrate, magnitude can vary over time and with rate/exposure | Defining cardiac feature; reported QTcF 487–495 ms and QTcB 503–518 ms | **HP:0001657 Long QT interval** |
| Ventricular tachyarrhythmia/torsades | Episodic, potentially fatal | Recognized disease risk; sparse JLNS2-specific frequency data | Ventricular tachycardia; torsade de pointes |
| Syncope | Episodic, often triggered; may begin in childhood | Variable; absent in some molecularly confirmed null-allele individuals | **HP:0001279 Syncope** |
| Seizure-like episodes | Symptom, usually cerebral hypoperfusion rather than primary epilepsy | Reported in JLNS and frequently causes diagnostic delay | Seizure; episodic loss of consciousness |
| Cardiac arrest/sudden cardiac death | Acute complication | Major untreated risk, but no reliable JLNS2-only percentage | Cardiac arrest; sudden cardiac death |
| Vestibular dysfunction | Clinical sign; variable | Supported in JLNS and Kcne1-null animals, but JLNS2 human frequency is unknown | Vestibular dysfunction |

The Faridi families show why symptoms cannot be used to exclude disease: individuals with profound deafness and QTcB **503–518 ms** reported no syncope. (faridi2019mutationalandphenotypic pages 8-9)

### Quality of life

Profound prelingual deafness affects language acquisition, education, communication, social participation, and caregiver burden. Cardiac risk imposes medication, exercise, medication-screening, emergency-planning, and procedural-anesthesia burdens. ICD shocks and activity restriction may add psychological morbidity. No JLNS2-specific EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life dataset was found.

## 4. Genetic and molecular information

* **Gene:** *KCNE1*; approved name potassium voltage-gated channel subfamily E regulatory subunit 1; Ensembl **ENSG00000180509**.
* **Disease locus:** chromosome 21q22 region.
* **Origin:** germline; somatic variation is not a recognized cause.
* **Inheritance:** autosomal recessive.
* **Functional class:** predominantly loss of function; null alleles produce absence or severe deficiency of functional KCNE1. Some heterozygous missense alleles have a distinct dominant-negative mechanism and should be annotated as Romano-Ward/LQT5 rather than JLNS2 unless a second pathogenic allele is present. (faridi2019mutationalandphenotypic pages 9-11, faridi2019mutationalandphenotypic pages 8-9)
* **Chromosomal abnormalities:** no recurrent aneuploidy, translocation, inversion, or copy-number syndrome was established as a typical cause. Exon-level deletion/duplication analysis remains relevant when sequence analysis finds one or no allele.
* **Epigenetics:** no reproducible JLNS2-specific DNA methylation, histone, or chromatin signature was found.
* **Anticipation:** not expected and not reported.
* **Mosaicism:** no characteristic germline-mosaic pattern is established; low residual recurrence from parental germline mosaicism is theoretically possible in apparently de novo cases.

Penetrance for congenital deafness appears high with biallelic null variants, whereas cardiac severity and events show variable expressivity. Precise age-dependent penetrance estimates are unavailable.

## 5. Environmental and lifestyle information

JLNS2 is not infectious, toxic, nutritional, occupational, or lifestyle-caused. Clinically important interactions are mainly **arrhythmia triggers**:

1. adrenergic surges from vigorous exercise or emotional stress;
2. swimming, especially unsupervised;
3. fever, vomiting, diarrhea, fasting, or other causes of electrolyte disturbance;
4. medications listed as QT-prolonging or torsadogenic;
5. perioperative stress and anesthetic drugs/interactions.

A published cochlear-implant case with biallelic *KCNQ1*—therefore **JLNS1, not JLNS2**—developed life-threatening arrhythmia around anesthesia. It demonstrates a clinically plausible JLNS-wide procedural hazard but cannot establish a JLNS2-specific event rate. Defibrillation capability, continuous monitoring, electrolyte optimization, continuation/planning of cardiac medication, and coordination among electrophysiology, anesthesia, and otology teams are prudent. (qiu2020jervellandlangenielsen pages 5-7, qiu2020jervellandlangenielsen pages 1-2)

## 6. Mechanism and pathophysiology

### Causal chain in heart

**Biallelic *KCNE1* loss → deficient KCNE1–KCNQ1 channel complex → reduced/altered I(Ks) → impaired phase-3 ventricular repolarization and reduced repolarization reserve → prolonged action potential and QTc → early afterdepolarizations and spatial dispersion → torsades de pointes/ventricular fibrillation → syncope, hypoxic convulsion, cardiac arrest, or sudden death.**

Relevant cells are ventricular cardiomyocytes. Suggested terms include **CL:0000746 cardiac muscle cell/cardiomyocyte**, GO “potassium ion transmembrane transport,” “regulation of cardiac muscle cell action potential,” “cardiac muscle cell action potential involved in contraction,” and “membrane repolarization during cardiac action potential.” The relevant subcellular compartment is the **plasma membrane** and voltage-gated potassium-channel complex.

### Causal chain in inner ear

**Biallelic *KCNE1* loss → defective apical KCNQ1/KCNE1 current in strial marginal cells → impaired potassium secretion into scala-media endolymph → loss of the positive endocochlear potential and potassium homeostasis → failure of hair-cell depolarization plus secondary Reissner-membrane collapse/hair-cell degeneration → congenital profound sensorineural deafness.** KCNE paralogs apparently do not compensate adequately in the inner ear. (faridi2019mutationalandphenotypic pages 9-11, faridi2019mutationalandphenotypic pages 3-4)

Suggested annotations are GO “potassium ion transport,” “sensory perception of sound,” and “inner ear development”; CL “strial marginal cell,” “inner hair cell,” and “outer hair cell”; and UBERON “cochlea,” “stria vascularis,” “scala media,” “endolymph,” “organ of Corti,” and “Reissner membrane.”

There is no established primary immune, inflammatory, fibrotic, neoplastic, or metabolic mechanism. Tissue injury in the cochlea is downstream of ionic failure rather than autoimmunity or infection.

### Molecular profiling and advanced technologies

No disease-defining JLNS2 transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or multi-omic signature was identified. Current LQTS precision research uses patient-specific induced pluripotent stem cell-derived cardiomyocytes, whole-genome sequencing, CRISPR correction/engineering, machine learning, and high-throughput drug testing. These platforms can test causality and variant-specific responses, but they are research tools rather than validated JLNS2 diagnostics or treatments. The 2023 review’s abstract states that “**Deep phenotyping and high-throughput drug testing using LQTS patient-specific cardiomyocytes herald the upcoming precision medicine in LQTS**.” Publication: January 2023; DOI: https://doi.org/10.1017/erm.2022.43. (yu2023precisionmedicinefor pages 1-2, yu2023precisionmedicinefor pages 7-8)

## 7. Anatomical structures affected

* **Primary organ systems:** cardiovascular and auditory/vestibular systems.
* **Heart:** ventricular myocardium/electrical conduction at the cardiomyocyte-membrane level; the heart is generally structurally normal.
* **Inner ear:** bilateral cochleae, especially stria vascularis and scala-media ionic environment; secondary organ-of-Corti hair-cell degeneration may occur.
* **Vestibular labyrinth:** possible involvement through analogous potassium-secreting dark cells.
* **Secondary brain effects:** transient cerebral hypoperfusion during arrhythmia can cause syncope or convulsive movements; primary epilepsy is not intrinsic to JLNS2.
* **Lateralization:** auditory involvement is typically bilateral, not unilateral or asymmetric.

Suggested UBERON terms: heart, cardiac ventricle, ventricular myocardium, inner ear, cochlea, cochlear duct, stria vascularis, organ of Corti, and vestibular labyrinth. Suggested GO cellular components: plasma membrane, voltage-gated potassium-channel complex, and KCNQ1–KCNE1 complex where supported.

## 8. Temporal development

The molecular defect is present from conception. Hearing loss is congenital and lifelong. QT prolongation is congenital or detectable in infancy/childhood, although resting QTc and clinical expression can fluctuate. Arrhythmic events are episodic and trigger-dependent rather than steadily progressive. The disorder itself is lifelong; there is no spontaneous remission of the genotype or deafness.

Critical windows are:

* newborn/early-childhood hearing assessment, before language delay;
* the first ECG after detection of congenital profound deafness;
* initiation and adherence to β-blockade before a sentinel arrhythmia;
* illness, electrolyte disturbance, swimming/exertion, and perioperative periods;
* cascade testing after identification of a proband.

QTc above **500 ms** is generally high risk and above **600 ms** extremely high risk in congenital LQTS. Syncope before age seven predicts recurrent events despite β-blockade in broader LQTS data. (balestra2024congenitallongqt pages 4-5)

## 9. Inheritance and population

JLNS2 is autosomal recessive: for two carrier parents, each pregnancy has a 25% probability of an affected child, 50% probability of a heterozygous child, and 25% probability of inheriting neither familial allele. Both sexes should be affected equally.

JLNS overall has been estimated at roughly **1 per 200,000 to 1 per 1,000,000**, but this range is not JLNS2-specific and likely varies with consanguinity and founder effects. Approximately 90% of JLNS in some series is attributed to *KCNQ1*, making *KCNE1*-related JLNS2 the minority subtype. (faridi2019mutationalandphenotypic pages 1-3, qiu2020jervellandlangenielsen pages 1-2)

Consanguinity increases the probability that two relatives carry the same rare allele; the reported p.Trp17Ter and p.Tyr46Ter homozygotes were found in consanguineous Pakistani families. This is ascertainment evidence, not proof of restriction to any ancestry. (faridi2019mutationalandphenotypic pages 8-9)

No robust JLNS2-specific incidence, prevalence, sex ratio, carrier frequency, geographic distribution, or founder-allele frequency was identified. Such fields should be recorded as **unknown**, not populated using all-JLNS or all-LQTS estimates.

## 10. Diagnostics

### Clinical work-up

1. **History:** congenital deafness, exertional/emotional/sudden-noise syncope, apparent seizures, resuscitated arrest, unexplained drowning, sudden death, medication exposure, and three-generation pedigree.
2. **ECG:** manual QT measurement and heart-rate correction, preferably serial studies. Contemporary congenital LQTS criteria include QTc **≥480 ms** or modified Schwartz score **>3**; QTc **≥460 ms** can support diagnosis in a patient with arrhythmic syncope or cardiac arrest. (balestra2024congenitallongqt pages 4-5)
3. **Additional electrophysiology:** Holter/event monitoring and exercise/recovery ECG can reveal dynamic abnormalities. Echocardiography helps exclude structural disease but is usually not diagnostic.
4. **Audiology:** newborn auditory brainstem response, otoacoustic emissions, pure-tone audiometry when developmentally appropriate, speech/language assessment, and cochlear-implant evaluation.
5. **Laboratory testing:** potassium, magnesium, calcium, renal function, and thyroid studies identify acquired contributors; there is no diagnostic serum biomarker or enzyme assay.

A normal resting QTc does not exclude inherited LQTS: recent reviews estimate **20–25%**, and in some selected genetically confirmed series up to approximately **40%**, may have normal-range resting QTc. These differing figures reflect study populations and should not be treated as a JLNS2-specific frequency. (balestra2024congenitallongqt pages 5-8, yu2023precisionmedicinefor pages 1-2, yu2023precisionmedicinefor pages 2-2)

### Genetic testing

The preferred approach is a validated hereditary arrhythmia or combined hearing-loss/cardio-auditory panel including at minimum ***KCNE1* and *KCNQ1***, with deletion/duplication analysis. A broad hearing-loss panel that omits arrhythmia genes can miss the life-threatening diagnosis. If panel testing is negative or the phenotype is atypical, exome or genome sequencing with copy-number and splice-aware analysis is appropriate. Sanger sequencing is useful for confirmation and segregation.

CMA, karyotype, FISH, mitochondrial sequencing, and repeat-expansion testing are not first-line unless other clinical findings suggest an alternative disorder. RNA analysis may clarify suspected splice variants but is not routine. Variant interpretation must incorporate allele frequency, segregation, phenotype, functional data, and ACMG/AMP criteria; a VUS does not independently confirm JLNS2.

### Differential diagnosis

* **JLNS1:** identical cardinal phenotype, but biallelic *KCNQ1* variants.
* **Romano-Ward/LQT5:** heterozygous *KCNE1* variant, long QT without congenital profound deafness.
* Other congenital LQTS subtypes plus unrelated genetic deafness.
* Acquired QT prolongation from medication, hypokalemia, hypomagnesemia, hypocalcemia, or bradycardia.
* Nonsyndromic hearing loss, including *GJB2*, *STRC*, or other causes, without intrinsic long QT.
* Pendred syndrome, Usher syndrome, mitochondrial deafness, and congenital infection.
* Epilepsy when convulsive syncope is the true mechanism.

### Screening

All infants with severe/profound congenital hearing loss should receive an ECG or prompt cardiac assessment where JLNS is plausible. Once familial variants are known, targeted cascade testing is more efficient than repeated broad sequencing. At-risk relatives need ECG assessment even when hearing is normal because heterozygous missense effects and incomplete cardiac expression can complicate segregation. Prenatal diagnosis and preimplantation genetic testing are technically possible for known familial pathogenic variants.

## 11. Outcome and prognosis

Untreated JLNS is one of the highest-risk congenital LQTS presentations, but **JLNS2-only survival and mortality curves are unavailable**. Profound deafness does not spontaneously recover. Arrhythmia risk is lifelong but can be substantially reduced by early recognition, trigger avoidance, nonselective β-blockade, and escalation to device or surgical therapy when indicated.

In broader symptomatic congenital LQTS, β-blockers reportedly reduced annual mortality from approximately **60% to below 2% over the ten years after an arrhythmic event**; this historical statistic is not a JLNS2-specific response rate. (balestra2024congenitallongqt pages 5-8)

Adverse prognostic features include prior cardiac arrest, recurrent syncope on therapy, very prolonged QTc, early-childhood events, poor adherence, electrolyte disturbance, QT-prolonging medication, and potentially a second arrhythmia-associated variant. Absence of previous syncope is not reassuring enough to omit treatment because molecularly confirmed JLNS2 can be asymptomatic despite QTc above 500 ms. (faridi2019mutationalandphenotypic pages 8-9, balestra2024congenitallongqt pages 4-5)

## 12. Treatment and current implementation

### Cardiac treatment

* **Nonselective β-blockers:** first-line, usually **nadolol** or **propranolol**. A recent pediatric LQTS review gives propranolol **2–3 mg/kg/day** or nadolol **1–1.5 mg/kg/day**, divided according to regimen. Dosing is individualized by electrophysiology specialists. β1-selective agents are generally less favored for congenital LQTS. Suggested NCIt concept: beta-adrenergic receptor blocking-agent therapy. (balestra2024congenitallongqt pages 5-8)
* **ICD:** recommended after resuscitated cardiac arrest and considered for recurrent arrhythmic syncope or ventricular arrhythmia despite optimized therapy. In small children, device complications and inappropriate shocks require careful balancing. NCIt: implantable cardioverter-defibrillator procedure/device. (balestra2024congenitallongqt pages 8-9)
* **Left cardiac sympathetic denervation:** appropriate when events recur despite medication, when an ICD is contraindicated/not feasible, or to reduce recurrent shocks. NCIt: sympathectomy/left cardiac sympathetic denervation. (balestra2024congenitallongqt pages 8-9, yu2023precisionmedicinefor pages 7-8)
* **Pacing:** may be considered in selected patients with severe bradycardia, pause-dependent events, or as part of an individualized high-risk strategy; it is not universal JLNS2 therapy.
* **Electrolytes:** promptly correct potassium and magnesium depletion. Routine potassium supplementation requires clinical supervision.
* **Avoidance:** use a current QT-risk resource when prescribing; avoid unsupervised swimming and individualize exercise participation through specialist shared decision-making.

Mexiletine is genotype-directed mainly for sodium-channel LQTS3 and is not established targeted treatment for *KCNE1*-JLNS2. No validated pharmacogenomic dosing rule specific to *KCNE1* was found.

### Hearing and supportive care

Hearing aids may provide limited benefit when loss is profound. **Cochlear implantation** can provide useful auditory access, coupled with early speech-language therapy, educational support, and Deaf-community/family-centered communication planning. Surgery requires a JLNS-aware anesthesia protocol and continuous postoperative monitoring. The strongest retrieved procedural case was *KCNQ1*-related JLNS1, so efficacy and anesthesia precautions are extrapolated to JLNS2 on syndrome-wide grounds. (qiu2020jervellandlangenielsen pages 5-7)

### Experimental treatment and 2023–2024 developments

No approved gene, RNA, cell, or CRISPR therapy corrects JLNS2. Patient-specific iPSC cardiomyocytes and CRISPR-based isogenic controls are being developed for functional variant adjudication and individualized drug testing, but remain preclinical. (yu2023precisionmedicinefor pages 1-2, yu2023precisionmedicinefor pages 7-8)

**NCT06534671, “Diltiazem in Jervell and Lange-Nielsen Syndrome,”** was a completed Phase 4 Vanderbilt study in 2024. One genetically confirmed adult received IV diltiazem 0.25 mg/kg, with a possible 0.35 mg/kg second dose, and ECG/telemetry assessment for acute QT shortening. Enrollment was **one**, completion was October 23, 2024, and no efficacy conclusion should be drawn without posted peer-reviewed results. Diltiazem is therefore experimental, not standard JLNS2 treatment. (NCT06534671 chunk 1)

## 13. Prevention

Primary prevention of the genotype is possible only through informed reproductive choices: carrier testing in at-risk relatives, genetic counseling, prenatal diagnosis, donor gametes, or preimplantation genetic testing. There is no vaccine or environmental primary prevention.

Secondary prevention consists of newborn hearing screening followed by ECG/genetic evaluation, cascade testing, early β-blockade, and identification of concealed disease. Tertiary prevention includes medication adherence, QT-drug avoidance, electrolyte management, emergency action plans, supervised exercise decisions, ICD/LCSD where indicated, and safe anesthesia planning.

Families should be counseled about autosomal-recessive recurrence, variable cardiac expression, CPR/AED access, recognition of arrhythmic syncope, and informing schools, dentists, surgeons, and anesthesiologists. Public-health sanitation or infectious-disease control is not relevant.

## 14. Other species and natural disease

No well-established naturally occurring veterinary syndrome equivalent to human JLNS2 was identified. There is no zoonotic potential or cross-species transmission because this is an inherited channelopathy.

Orthologous *Kcne1* is conserved in laboratory mouse, **Mus musculus, NCBI Taxonomy 10090**. The relevant comparative biology is experimental rather than a common spontaneous veterinary disease. A spontaneous mouse nonsense allele, *Kcne1*^pkr (“punk rocker,” p.Arg67Ter), produces an auditory/vestibular phenotype. (faridi2019mutationalandphenotypic pages 9-11)

## 15. Model organisms

Three *Kcne1*-null mouse alleles are reported: two engineered coding-exon deletions and the spontaneous p.Arg67Ter punk-rocker allele. Homozygous animals are deaf; heterozygotes have normal hearing. Cochlear findings include collapsed Reissner membrane and hair-cell degeneration, and punk-rocker mice display head tossing consistent with vestibular dysfunction. These findings strongly recapitulate the recessive inner-ear component of human JLNS2. (faridi2019mutationalandphenotypic pages 9-11)

Cardiac recapitulation is inconsistent: one line showed longer QT at slow rates and shorter QT at fast rates, another increased inducible arrhythmia, and another no ECG difference. A major limitation is the mouse resting heart rate of approximately **500–700 beats/minute**, which complicates QT measurement and makes the model less faithful for human ventricular repolarization. Mouse inner-ear architecture is much more suitable for studying the auditory mechanism. (faridi2019mutationalandphenotypic pages 9-11)

Suggested model annotations include mammalian genetic knockout, homozygous null, nonsense knock-in/spontaneous mutant, auditory brainstem response, ECG/telemetry, cochlear histopathology, strial marginal cell, hair cell, and vestibular dark cell. Patient-derived iPSC cardiomyocytes are the leading human cellular model for variant causality and drug testing, although a large JLNS2-specific iPSC dataset was not identified. (yu2023precisionmedicinefor pages 1-2)

## Evidence limitations and curation cautions

1. JLNS2 is much rarer than *KCNQ1*-related JLNS1; disease-wide JLNS numbers must not be assigned automatically to JLNS2.
2. Much treatment evidence comes from congenital LQTS or JLNS overall rather than randomized JLNS2 trials.
3. Individual variants require current ClinVar/gnomAD review; literature-level pathogenicity should not replace laboratory reclassification.
4. No reliable JLNS2-specific incidence, carrier frequency, survival curve, quality-of-life scale, molecular-omics signature, protective allele, or approved precision therapy was found.
5. A retrieved 2020 cochlear-implant report is **JLNS1 because its patient carried biallelic *KCNQ1***; it supports syndrome-wide procedural practice but must not be mislabeled as genotype-confirmed JLNS2. (qiu2020jervellandlangenielsen pages 5-7, qiu2020jervellandlangenielsen pages 1-2)

References

1. (faridi2019mutationalandphenotypic pages 9-11): Rabia Faridi, Risa Tona, Alessandra Brofferio, Michael Hoa, Rafal Olszewski, Isabelle Schrauwen, Muhammad Z.K. Assir, Akhtar A. Bandesha, Asma A. Khan, Atteeq U. Rehman, Carmen Brewer, Wasim Ahmed, Suzanne M. Leal, Sheikh Riazuddin, Steven E. Boyden, and Thomas B. Friedman. Mutational and phenotypic spectra of kcne1 deficiency in jervell and lange‐nielsen syndrome and romano‐ward syndrome. Human Mutation, 40:162-176, Dec 2019. URL: https://doi.org/10.1002/humu.23689, doi:10.1002/humu.23689. This article has 47 citations and is from a domain leading peer-reviewed journal.

2. (faridi2019mutationalandphenotypic pages 8-9): Rabia Faridi, Risa Tona, Alessandra Brofferio, Michael Hoa, Rafal Olszewski, Isabelle Schrauwen, Muhammad Z.K. Assir, Akhtar A. Bandesha, Asma A. Khan, Atteeq U. Rehman, Carmen Brewer, Wasim Ahmed, Suzanne M. Leal, Sheikh Riazuddin, Steven E. Boyden, and Thomas B. Friedman. Mutational and phenotypic spectra of kcne1 deficiency in jervell and lange‐nielsen syndrome and romano‐ward syndrome. Human Mutation, 40:162-176, Dec 2019. URL: https://doi.org/10.1002/humu.23689, doi:10.1002/humu.23689. This article has 47 citations and is from a domain leading peer-reviewed journal.

3. (faridi2019mutationalandphenotypic pages 1-3): Rabia Faridi, Risa Tona, Alessandra Brofferio, Michael Hoa, Rafal Olszewski, Isabelle Schrauwen, Muhammad Z.K. Assir, Akhtar A. Bandesha, Asma A. Khan, Atteeq U. Rehman, Carmen Brewer, Wasim Ahmed, Suzanne M. Leal, Sheikh Riazuddin, Steven E. Boyden, and Thomas B. Friedman. Mutational and phenotypic spectra of kcne1 deficiency in jervell and lange‐nielsen syndrome and romano‐ward syndrome. Human Mutation, 40:162-176, Dec 2019. URL: https://doi.org/10.1002/humu.23689, doi:10.1002/humu.23689. This article has 47 citations and is from a domain leading peer-reviewed journal.

4. (OpenTargets Search: Jervell and Lange-Nielsen syndrome-KCNE1): Open Targets Query (Jervell and Lange-Nielsen syndrome-KCNE1, 8 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

5. (faridi2019mutationalandphenotypic pages 3-4): Rabia Faridi, Risa Tona, Alessandra Brofferio, Michael Hoa, Rafal Olszewski, Isabelle Schrauwen, Muhammad Z.K. Assir, Akhtar A. Bandesha, Asma A. Khan, Atteeq U. Rehman, Carmen Brewer, Wasim Ahmed, Suzanne M. Leal, Sheikh Riazuddin, Steven E. Boyden, and Thomas B. Friedman. Mutational and phenotypic spectra of kcne1 deficiency in jervell and lange‐nielsen syndrome and romano‐ward syndrome. Human Mutation, 40:162-176, Dec 2019. URL: https://doi.org/10.1002/humu.23689, doi:10.1002/humu.23689. This article has 47 citations and is from a domain leading peer-reviewed journal.

6. (balestra2024congenitallongqt pages 4-5): Elia Balestra, Marco Bobbo, Marco Cittar, Daniela Chicco, Biancamaria D’Agata Mottolese, Egidio Barbi, and Thomas Caiffa. Congenital long qt syndrome in children and adolescents: a general overview. Children, 11:582, May 2024. URL: https://doi.org/10.3390/children11050582, doi:10.3390/children11050582. This article has 20 citations.

7. (balestra2024congenitallongqt pages 5-8): Elia Balestra, Marco Bobbo, Marco Cittar, Daniela Chicco, Biancamaria D’Agata Mottolese, Egidio Barbi, and Thomas Caiffa. Congenital long qt syndrome in children and adolescents: a general overview. Children, 11:582, May 2024. URL: https://doi.org/10.3390/children11050582, doi:10.3390/children11050582. This article has 20 citations.

8. (qiu2020jervellandlangenielsen pages 1-2): Yue Qiu, Sen Chen, Xia Wu, Wen-Juan Zhang, Wen Xie, Yuan Jin, Le Xie, Kai Xu, Xue Bai, Hui-Min Zhang, Xiao-Zhou Liu, Xiao-Hui Wang, Yu Sun, and Wei-Jia Kong. Jervell and lange-nielsen syndrome due to a novel compound heterozygous kcnq1 mutation in a chinese family. Neural Plasticity, 2020:1-8, May 2020. URL: https://doi.org/10.1155/2020/3569359, doi:10.1155/2020/3569359. This article has 14 citations and is from a peer-reviewed journal.

9. (balestra2024congenitallongqt pages 8-9): Elia Balestra, Marco Bobbo, Marco Cittar, Daniela Chicco, Biancamaria D’Agata Mottolese, Egidio Barbi, and Thomas Caiffa. Congenital long qt syndrome in children and adolescents: a general overview. Children, 11:582, May 2024. URL: https://doi.org/10.3390/children11050582, doi:10.3390/children11050582. This article has 20 citations.

10. (qiu2020jervellandlangenielsen pages 5-7): Yue Qiu, Sen Chen, Xia Wu, Wen-Juan Zhang, Wen Xie, Yuan Jin, Le Xie, Kai Xu, Xue Bai, Hui-Min Zhang, Xiao-Zhou Liu, Xiao-Hui Wang, Yu Sun, and Wei-Jia Kong. Jervell and lange-nielsen syndrome due to a novel compound heterozygous kcnq1 mutation in a chinese family. Neural Plasticity, 2020:1-8, May 2020. URL: https://doi.org/10.1155/2020/3569359, doi:10.1155/2020/3569359. This article has 14 citations and is from a peer-reviewed journal.

11. (yu2023precisionmedicinefor pages 1-2): Yang Yu, Isabelle Deschenes, and Ming-Tao Zhao. Precision medicine for long qt syndrome: patient-specific ipscs take the lead. Expert Reviews in Molecular Medicine, Jan 2023. URL: https://doi.org/10.1017/erm.2022.43, doi:10.1017/erm.2022.43. This article has 23 citations and is from a peer-reviewed journal.

12. (yu2023precisionmedicinefor pages 7-8): Yang Yu, Isabelle Deschenes, and Ming-Tao Zhao. Precision medicine for long qt syndrome: patient-specific ipscs take the lead. Expert Reviews in Molecular Medicine, Jan 2023. URL: https://doi.org/10.1017/erm.2022.43, doi:10.1017/erm.2022.43. This article has 23 citations and is from a peer-reviewed journal.

13. (NCT06534671 chunk 1): Prince Joseph Kannankeril. Diltiazem in Jervell and Lange-Nielsen Syndrome. Vanderbilt University Medical Center. 2024. ClinicalTrials.gov Identifier: NCT06534671

14. (yu2023precisionmedicinefor pages 2-2): Yang Yu, Isabelle Deschenes, and Ming-Tao Zhao. Precision medicine for long qt syndrome: patient-specific ipscs take the lead. Expert Reviews in Molecular Medicine, Jan 2023. URL: https://doi.org/10.1017/erm.2022.43, doi:10.1017/erm.2022.43. This article has 23 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Jervell_and_Lange-Nielsen_Syndrome_2-deep-research-falcon_artifacts/artifact-00.md)

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