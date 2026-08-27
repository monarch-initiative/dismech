---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-27T11:45:20.885123'
end_time: '2026-08-27T11:56:46.077864'
duration_seconds: 685.19
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Myiasis
  mondo_id: ''
  category: Infectious Disease
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 32
reference_validation:
  total_references: 10
  verified: 8
  not_found: 2
  unverifiable: 0
  confabulation_rate: 0.2
  relevance_assessed: 8
  on_topic: 3
  unresolved_references:
  - DOI:10.1590/S1984-29612024020
  - DOI:10.1590/s1984-29612024020
  needs_review: true
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Myiasis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Myiasis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Myiasis** covering all of the
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
- **Disease Name:** Myiasis
- **MONDO ID:**  (if available)
- **Category:** Infectious Disease

## Research Objectives

Please provide a comprehensive research report on **Myiasis** covering all of the
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


# Myiasis: Comprehensive Disease-Characteristics Report

## Executive summary

Myiasis is an infectious–parasitic infestation in which larvae of flies (order **Diptera**) develop in or on a living vertebrate. It is not one etiologically uniform disease: clinical behavior depends on the fly species, whether it is an obligate or facultative parasite, and the involved anatomical site. Human disease is concentrated in tropical/subtropical settings, travelers, people exposed to livestock, and vulnerable patients with wounds, impaired self-care, or intensive-care devices. Skin and wounds are most often involved, but ocular, oral, nasal, aural, gastrointestinal, and urogenital disease occurs.

The evidence base remains dominated by case reports and small series rather than population surveillance or randomized trials. Consequently, global incidence, prevalence, mortality, and phenotype frequencies cannot be estimated reliably. The most consistent management is complete mechanical removal, irrigation and wound care; invasive obligate myiasis additionally requires debridement, while ivermectin and antibiotics are selected adjuncts rather than universal therapy. Recent research emphasizes molecular identification, hospital infection prevention, climate-sensitive geographic expansion, and One Health connections among human disease, livestock infestation, fly microbiota, and emerging bacterial sepsis.

| Domain | Evidence-based summary | Suggested ontology terms (approximate mappings where needed) | Evidence type and key source/year/DOI |
|---|---|---|---|
| Definition / classification | Myiasis is infestation of living human or animal tissue by dipteran larvae. It is classified anatomically (cutaneous/furuncular, wound, ocular, nasal, aural, urogenital, gastrointestinal/cavitary) and ecologically as obligate, facultative, or accidental/pseudomyiasis. Major implicated human families include Oestridae, Calliphoridae, Sarcophagidae, and Muscidae. Lucilia sericata is typically facultative; Cochliomyia hominivorax, Chrysomya bezziana, Oestrus ovis, and Wohlfahrtia magnifica are important obligate agents (monney2025myiasisinthe pages 1-2, monney2025myiasisinthe pages 3-5, tuygun2009furuncularmyiasisin pages 1-2). | MONDO: myiasis (ID uncertain; do not assign without ontology lookup). MeSH/ICD likely available but not verified here. Approx. HPO/clinical descriptors: cutaneous lesion, wound infestation, ocular infestation. | Human clinical review/case + taxonomy review: Swiss Med Wkly 2025 doi:10.57187/s.3827; Turk J Pediatr 2009; Microorganisms 2024 doi:10.3390/microorganisms12020233 |
| Major clinical phenotypes | Clinical forms include furuncular lesions, wound myiasis, conjunctival/ophthalmomyiasis, nasopharyngeal/oropharyngeal, aural, and genital involvement. Furuncular disease may present as swelling and furuncle-like lesion; inflammatory lesions can be accompanied by eosinophilia. O. ovis in animals causes sneezing/nasal discharge and is zoonotic for ophthalmic/nasopharyngeal human disease (zhou2025machinelearningbasedtext pages 1-2, tuygun2009furuncularmyiasisin pages 1-2, garijo‐toledo2023prevalenceofoestrus pages 1-3, silva2024prevalenceandseasonal pages 1-3). | Approx. HPO: Skin nodule, Furuncle, Wound infection, Edema, Pain, Bleeding, Eosinophilia, Conjunctivitis, Nasal discharge, Dyspnea. UBERON approx.: skin, oral cavity, eye, nasal cavity, pharynx, genitalia. | Human case reports/review + veterinary epidemiology: Front Cell Infect Microbiol 2025 doi:10.3389/fcimb.2025.1568563; Turk J Pediatr 2009; Med Vet Entomol 2023 doi:10.1111/mve.12634; Braz J Vet Parasitol 2024 doi:10.1590/S1984-29612024020 |
| Risk factors | Recurrent risk factors include wounds, necrosis, bacterial contamination, poor hygiene, advanced age, severe underlying illness, immobilization, diabetes, alcoholism, vascular disease, mental impairment, mechanical ventilation, nasogastric tube use, periodontal disease, mouth breathing/lip incompetence, hot seasons, rural/livestock exposure, and tropical travel. Some patients lack obvious predisposing factors (monney2025myiasisinthe pages 2-3, monney2025myiasisinthe pages 3-5, tuygun2009furuncularmyiasisin pages 1-2). | Approx. HPO/social-clinical descriptors: Impaired wound healing, Periodontitis, Immobility, Diabetes mellitus. UBERON approx.: oral cavity, skin wound. | Human clinical review/case: Swiss Med Wkly 2025 doi:10.57187/s.3827; Turk J Pediatr 2009 |
| Pathophysiology | Causal chain: adult fly deposits eggs/larvae on wounds, body orifices, or intact skin (species-dependent) → larvae feed on living tissue, secretions, or necrotic material → mechanical/proteolytic injury and burrowing produce pain, bleeding, edema, ulceration, necrosis, and local inflammation → secondary bacterial infection may occur, rarely progressing to sepsis. Histologic inflammatory response can include lymphocytes, giant cells, neutrophils, eosinophils, and plasma cells; eosinophilia can occur in furuncular myiasis. In obligate species such as W. magnifica and C. bezziana, tissue destruction can be extensive (hou2025extensivepalatalnecrosis pages 5-6, tuygun2009furuncularmyiasisin pages 1-2, simin2024longtimeno pages 1-2, malekiravasan2020newinsightsinto pages 1-2). | GO approx.: inflammatory response; response to wounding; proteolysis; leukocyte migration. CL approx.: neutrophil, eosinophil, plasma cell, giant cell/macrophage. UBERON approx.: skin, mucosa, hoof/nasal cavities in veterinary disease. | Human case/pathobiology + veterinary review + fly microbiome study: Turk J Pediatr 2009; Microorganisms 2024 doi:10.3390/microorganisms12020233; Front Microbiol 2020 doi:10.3389/fmicb.2020.00505; Archives of Orofacial Sciences 2025 doi:10.21315/aos2025.2001.cr03 |
| Diagnosis | Primary diagnosis is clinical visualization/removal of larvae, supported by species identification. Morphology of larval stages remains standard; molecular confirmation commonly uses mitochondrial COI barcoding. In ICU-associated cases, developmental stage and temperature can help estimate timing of infestation. For O. ovis and W. magnifica, detailed larval morphology and anatomic localization are used in veterinary/human investigations (monney2025myiasisinthe pages 1-2, simin2024longtimeno pages 1-2, simin2024longtimeno pages 2-3, simin2024longtimeno pages 3-5). | NCIT approx.: Clinical examination; Specimen collection; DNA barcoding; Polymerase chain reaction. UBERON approx.: lesion site-specific sampling. | Human/veterinary diagnostic reports: Swiss Med Wkly 2025 doi:10.57187/s.3827; Microorganisms 2024 doi:10.3390/microorganisms12020233 |
| Treatment | Core management is prompt mechanical larval extraction plus cleansing/irrigation and local wound care. Debridement is important for invasive obligate wound myiasis. Antibiotics are used when secondary bacterial infection is suspected; systemic antiparasitic therapy such as ivermectin may be used in selected cutaneous/orbital/wound cases, but facultative ICU myiasis may derive limited added benefit once larvae are removed. Veterinary treatment includes antiseptics/insecticides, local antibiotic spray, macrocyclic lactones, and supportive care (monney2025myiasisinthe pages 2-3, monney2025myiasisinthe pages 3-5, simin2024longtimeno pages 2-3, zhou2025machinelearningbasedtext pages 2-5). | NCIT approx.: Debridement; Wound irrigation; Anti-infective therapy; Ivermectin therapy; Supportive care. CHEBI: ivermectin; diazinon (veterinary/environmental use). | Human review + veterinary case management + bibliometric synthesis: Swiss Med Wkly 2025 doi:10.57187/s.3827; Microorganisms 2024 doi:10.3390/microorganisms12020233; Front Cell Infect Microbiol 2025 doi:10.3389/fcimb.2025.1568563 |
| Prevention | Prevention is mainly environmental and behavioral: fly control, sanitation, wound hygiene and coverage, oral care in debilitated/intubated patients, screening/windows/fumigation in healthcare settings, and traveler/livestock exposure education. ICU prevention emphasizes barriers against fly entry and better oral care for ventilated patients. Climate warming may expand risk windows/regions for some fly species (monney2025myiasisinthe pages 13-15, monney2025myiasisinthe pages 3-5, garijo‐toledo2023prevalenceofoestrus pages 1-3). | NCIT/Public health approx.: Infection prevention; Environmental control; Health education. GO not central. | Human infection-control review + veterinary climate-linked epidemiology: Swiss Med Wkly 2025 doi:10.57187/s.3827; Med Vet Entomol 2023 doi:10.1111/mve.12634 |
| Epidemiology | Robust global incidence/prevalence in humans is not available; literature is dominated by case reports. Country-level review from Italy found 703 autochthonous human cases, 98.1% due to O. ovis; imported cases were mainly Cordylobia spp. (59.5%) and Dermatobia hominis (40.5%). ICU-acquired myiasis review identified 38 worldwide cases, 92% oro-/nasopharyngeal and 45% due to L. sericata. Seasonality and heat are recurrent epidemiologic themes (zammarchi2014humanoestriasisacquired pages 2-4, monney2025myiasisinthe pages 2-3, monney2025myiasisinthe pages 1-2). | MONDO approx.: myiasis. UBERON approx.: nasopharynx/oral cavity/eye/skin. | Human literature review: Parasitology Research 2014 doi:10.1007/s00436-014-3906-9; Swiss Med Wkly 2025 doi:10.57187/s.3827 |
| Veterinary / One Health | Veterinary burden is substantial and supports One Health relevance. W. magnifica causes painful traumatic myiasis in sheep and other warm-blooded vertebrates and is associated with emerging bacterium Wohlfahrtiimonas chitiniclastica. Recent animal prevalence data: O. ovis prevalence 56.3% in 3476 small-ruminant heads from eastern Spain, with temperature association; 45.77% (319/697) in sheep from Mato Grosso, Brazil, with year-round infestation. Veterinary lesions include lameness, depression, inappetence, blindness, reproductive problems, and death if untreated (simin2024longtimeno pages 1-2, garijo‐toledo2023prevalenceofoestrus pages 1-3, silva2024prevalenceandseasonal pages 1-3). | CL approx.: epithelial cells, neutrophils/eosinophils in inflamed tissue. UBERON approx.: nasal cavity, sinuses, skin, hoof, genitalia. CHEBI: ivermectin/doramectin (control). | Veterinary field studies and One Health review: Microorganisms 2024 doi:10.3390/microorganisms12020233; Med Vet Entomol 2023 doi:10.1111/mve.12634; Braz J Vet Parasitol 2024 doi:10.1590/S1984-29612024020 |
| Non-applicable genetics / omics | Myiasis is an infectious/parasitic infestation rather than a monogenic human disease. No established human causal genes, pathogenic variants, inheritance pattern, penetrance, or chromosomal abnormalities are known to define “myiasis.” Omics are mostly applied to the fly, not the host: COI sequencing for species ID and 16S/metagenetic studies of L. sericata microbiota. Experimental work on suspected intestinal myiasis suggests some reported cases may be pseudomyiasis rather than true colonization (malekiravasan2020newinsightsinto pages 1-2, zhan2026clogmiaalbipunctatafails pages 13-15, zhan2026clogmiaalbipunctatafails pages 1-2). | Mark as not applicable for OMIM-style causal gene fields. GO/CL/UBERON only for host response, not disease inheritance. NCIT approx.: DNA barcoding; microbiome analysis. | Insect microbiome and experimental model evidence: Front Microbiol 2020 doi:10.3389/fmicb.2020.00505; PLOS One 2026 doi:10.1371/journal.pone.0356742 |


*Table: This table summarizes evidence-based disease characteristics of myiasis and maps them to cautious ontology suggestions where reliable. It is useful for populating a disease knowledge base while explicitly separating well-supported clinical/parasitologic facts from non-applicable human genetics fields.*

## 1. Disease information

### Definition and classification

Myiasis is infestation of living human or animal tissues by dipteran larvae (“maggots”). Important causative families are **Calliphoridae**, **Sarcophagidae**, **Oestridae**, and **Muscidae**. Ecologically, agents are:

* **Obligate parasites**, which require a living host and may invade viable tissue—examples include *Cochliomyia hominivorax*, *Chrysomya bezziana*, *Wohlfahrtia magnifica*, and *Oestrus ovis*.
* **Facultative parasites**, normally associated with carrion or decaying matter but able to colonize necrotic wounds—most notably *Lucilia sericata*.
* **Accidental myiasis/pseudomyiasis**, in which ingested or contaminating larvae pass through a specimen or body compartment without sustained tissue infestation.

Anatomical categories are cutaneous (furuncular, migratory/creeping, and wound or traumatic), ocular, nasal/nasopharyngeal, oral/oropharyngeal, aural, gastrointestinal, and urogenital myiasis. Cutaneous myiasis itself comprises three major clinical patterns: furuncular, migratory, and traumatic/wound disease. (monney2025myiasisinthe pages 1-2, monney2025myiasisinthe pages 3-5, zhou2025machinelearningbasedtext pages 1-2, tuygun2009furuncularmyiasisin pages 1-2)

### Identifiers and synonyms

* **ICD-10-CM:** **B87 — Myiasis**, with anatomical subcodes such as B87.0 cutaneous, B87.1 wound, B87.2 ocular, B87.3 nasopharyngeal, B87.4 aural, B87.8 other, and B87.9 unspecified. Local ICD modifications should be checked before production use.
* **MeSH:** *Myiasis*; commonly indexed under parasitic diseases/arthropod infestations.
* **ICD-11:** represented within infestations by arthropods; the exact current browser code should be validated against the release used by the knowledge base.
* **MONDO:** a myiasis concept is available, but its numerical identifier was not independently verified in the retrieved corpus and should not be populated without a direct MONDO release lookup.
* **OMIM:** not applicable as a primary entry because myiasis is not a Mendelian disorder.
* **Orphanet:** generally not applicable; it is not a defined rare genetic disease.
* Synonyms include **maggot infestation**, **fly-larval infestation**, **cutaneous myiasis**, **wound myiasis**, **traumatic myiasis**, and species-specific terms such as **oestriasis/oestrosis**, **wohlfahrtiosis**, **dermatobiosis**, and **screwworm myiasis**.

This report synthesizes **aggregated disease-level literature**, including reviews, surveillance studies, and case reports. It is not derived from an individual EHR, although many primary evidence items describe individual patients.

## 2. Etiology, risk factors, and protective factors

### Causal agents and exposure

The direct cause is deposition of eggs or larvae by a competent fly on intact skin, wounds, necrotic tissue, mucosa, or natural orifices; some larvae may instead be ingested. *W. magnifica* is larviparous and can deposit larvae in eyes, ears, mouth, genital openings, wounds, or occasionally intact skin. Larvae feed on tissue and body fluids until they leave the host to pupate. Its Palearctic distribution extends from Mediterranean Europe and North Africa through the Middle East and Eurasian steppe into Central and East Asia. (simin2024longtimeno pages 1-2)

### Established or plausible risk factors

Human risk factors include:

* open wounds, ulcers, necrosis, malignant wounds, infected dermatitis, and bacterial contamination;
* poor wound or oral hygiene, periodontal disease, exposed body orifices, and inadequate fly barriers;
* older age, frailty, impaired consciousness, immobility, neurologic disability, or inability to perform self-care;
* diabetes, vascular occlusive disease, alcoholism, malignancy, malnutrition, and severe systemic illness;
* mechanical ventilation, endotracheal or nasogastric tubes, mouth breathing, and lip incompetence;
* homelessness or poor housing/sanitation, though disease also occurs in high-income settings without social neglect;
* tropical/subtropical residence or travel, outdoor sleeping, livestock contact, shepherding, and warm seasons.

In a review of ICU-acquired disease, 92% of 38 cases were oro- or nasopharyngeal; ventilation, nasogastric tubes, and periodontal disease were recurring factors. Nevertheless, healthy people can develop furuncular or ocular disease, and an eight-year-old with *W. magnifica* furuncular myiasis had no identified risk factor beyond likely environmental exposure. (monney2025myiasisinthe pages 2-3, monney2025myiasisinthe pages 3-5, tuygun2009furuncularmyiasisin pages 1-2)

### Protective factors

Protective factors are environmental rather than genetic: prompt wound cleaning and coverage, oral hygiene, protective clothing and repellents in fly-active areas, screened buildings, sanitation, fly control, early treatment of necrotic wounds, and regular inspection of dependent patients and livestock. No validated human protective allele, diet, supplement, or preventive medication is known.

### Genetics and gene–environment interaction

No causal human gene, susceptibility locus, protective variant, modifier gene, or replicated gene–environment interaction has been established. Host comorbidities alter exposure and tissue vulnerability, but this is not evidence of genetic inheritance. There is no established role for penetrance, anticipation, mosaicism, founder variants, carrier status, or consanguinity.

## 3. Phenotypes

Phenotype expression depends strongly on anatomy and species; formal population frequencies are generally unavailable.

* **Furuncular cutaneous disease:** one or several painful/pruritic papules or nodules with a central punctum, serous drainage, movement sensation, and intermittent lancinating pain. Onset follows larval inoculation and evolves over days to weeks. Suggested HPO mappings: *Skin nodule*, *Papule*, *Pruritus*, *Pain*, *Abnormality of skin physiology*.
* **Migratory/creeping disease:** serpiginous or moving subcutaneous/epidermal lesions. Usually progressive over days until removal or larval exit. Suggested HPO: *Abnormal skin morphology*, *Pruritus*.
* **Wound/traumatic myiasis:** visible larvae in an ulcer or wound, malodor, bleeding, serosanguineous or purulent drainage, edema, pain, friable tissue, and necrosis. Severity ranges from superficial facultative colonization to rapid destruction by obligate species. Suggested HPO: *Skin ulcer*, *Necrosis*, *Edema*, *Bleeding*, *Pain*.
* **Ocular disease:** foreign-body sensation, acute conjunctivitis, lacrimation, photophobia, and visible motile larvae; internal or orbital invasion can threaten vision. Suggested HPO: *Conjunctivitis*, *Photophobia*, *Visual impairment*, *Lacrimation*.
* **Nasal/nasopharyngeal disease:** nasal irritation, sneezing, obstruction, epistaxis, discharge, facial discomfort, and occasionally tissue destruction. Suggested HPO: *Nasal discharge*, *Epistaxis*, *Nasal obstruction*.
* **Oral/oropharyngeal disease:** oral larvae, ulceration, bleeding, halitosis, swelling, dysphagia, and tissue necrosis. ICU disease often has little tissue injury when caused by facultative *L. sericata*. Suggested HPO: *Oral ulcer*, *Dysphagia*, *Bleeding*, *Abnormal oral cavity morphology*.
* **Aural disease:** otalgia, discharge, tinnitus, hearing disturbance, and canal or middle-ear injury. Suggested HPO: *Otalgia*, *Hearing impairment*, *Otorrhea*.
* **Urogenital disease:** vulvar, vaginal, urethral, or urinary symptoms, discharge, pain, ulceration, or larvae in urine; contamination must be distinguished from true infestation.
* **Laboratory abnormalities:** peripheral eosinophilia and elevated IgE can occur but are neither common nor diagnostic. An eight-year-old had an absolute eosinophil count of 5,160/mm³ and IgE 667 IU/mL; both declined after removal of one larva. Tissue reactions may contain lymphocytes, macrophage-derived giant cells, neutrophils, eosinophils, and plasma cells. (tuygun2009furuncularmyiasisin pages 1-2)

Quality-of-life data using EQ-5D, SF-36, or PROMIS were not found. Pain, odor, social stigma, sleep disruption, impaired mobility, vision/hearing risk, and wound-care burden can substantially impair functioning. Veterinary disease similarly causes severe pain, lameness, impaired feeding, reproductive problems, and production loss. (simin2024longtimeno pages 1-2)

## 4. Genetic and molecular information

There are **no recognized human causal genes, HGNC disease genes, pathogenic germline or somatic variants, chromosomal abnormalities, modifier genes, or disease-defining epigenetic changes**. WES, WGS, gene panels, CMA, karyotyping, FISH, mitochondrial testing, and repeat-expansion testing therefore have no routine diagnostic role.

Molecular testing is directed at the **parasite**, not inherited host susceptibility. Mitochondrial cytochrome-c oxidase subunit I (**COI**) barcoding can confirm morphological identification. A 2024 *W. magnifica* investigation amplified a 710-bp COI barcode with LCO1490/HCO2198 primers, sequenced it bidirectionally, and compared it with GenBank using BLAST; sequences were deposited as MT027108–MT027114. (simin2024longtimeno pages 1-2, simin2024longtimeno pages 3-5)

## 5. Environmental, lifestyle, and infectious-agent information

Temperature, humidity, season, fly ecology, livestock density, sanitation, housing, and wound exposure determine risk. *W. magnifica* activity is greatest during hot summer months, although climatic conditions may permit a March–November season. A Spanish long-term veterinary study found temperature, but not rainfall, associated with *O. ovis* prevalence, supporting concern that warming may alter fly abundance and geographic risk. (simin2024longtimeno pages 1-2, garijo‐toledo2023prevalenceofoestrus pages 1-3)

Smoking and alcohol are not direct causes; alcohol use may act through neglect, impaired consciousness, or chronic wounds. Diet is not etiologic, although malnutrition may impair wound integrity and care.

Major infectious agents are Diptera larvae, especially *Dermatobia hominis*, *Cordylobia anthropophaga*, *Cochliomyia hominivorax*, *C. macellaria*, *Chrysomya bezziana*, *Lucilia sericata*, *Wohlfahrtia magnifica*, *Oestrus ovis*, *Musca domestica*, and several Sarcophagidae and Psychodidae. Larvae can carry bacteria. *W. magnifica* is associated with the emerging Gram-negative organism *Wohlfahrtiimonas chitiniclastica*, capable of local infection and sepsis. (simin2024longtimeno pages 1-2)

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream exposure:** an adult fly reaches exposed skin, wound, necrotic tissue, or mucosal opening and deposits eggs or larvae.
2. **Establishment:** larvae anchor by mouth hooks and body spines. Facultative species preferentially consume necrotic tissue; obligate species can invade viable tissue.
3. **Tissue injury:** movement and feeding cause mechanical disruption. Extracorporeal digestion releases salivary digestive enzymes that liquefy substrate before ingestion, providing a mechanistic basis for progressive tissue breakdown. (malekiravasan2020newinsightsinto pages 1-2)
4. **Host response:** epithelial injury induces acute and chronic inflammation, edema, bleeding, pain, and sometimes systemic eosinophilia. Relevant processes include inflammatory response, response to wounding, proteolysis, leukocyte migration, and tissue remodeling; relevant cell types include keratinocytes/epithelial cells, neutrophils, eosinophils, macrophages/giant cells, lymphocytes, and plasma cells. (tuygun2009furuncularmyiasisin pages 1-2)
5. **Downstream complications:** continuing invasion can cause ulceration, necrosis, destruction of cartilage or bone, secondary bacterial infection, bacteremia/sepsis, and—in anatomically dangerous sites—intracranial, orbital, or airway complications. *C. bezziana* larvae can penetrate wounds within approximately 24 hours after hatching and produce progressive bleeding, purulent discharge, and extensive soft-tissue or bone injury. (hou2025extensivepalatalnecrosis pages 5-6)

Suggested GO terms include **inflammatory response**, **response to wounding**, **proteolysis**, **leukocyte migration**, **innate immune response**, and **tissue remodeling**. Suggested Cell Ontology concepts include **neutrophil**, **eosinophil**, **macrophage**, **lymphocyte**, **plasma cell**, and site-specific **epithelial cell**. Exact ontology identifiers should be validated before ingestion.

### Molecular profiling

Human transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or multi-omic signatures have not been clinically validated. Fly-associated metagenetics is more developed: a 2020 *L. sericata* study identified 265 bacterial records spanning 20 families, 28 genera, and 40 species; Gammaproteobacteria dominated, while *Enterococcus faecalis*, *Proteus*, *Providencia vermicola*, and *Serratia marcescens* showed transstadial transmission. These data concern insect ecology and maggot-debridement safety, not a human diagnostic biomarker. (malekiravasan2020newinsightsinto pages 1-2)

## 7. Anatomical structures affected

Primary sites include:

* **Skin and subcutis**—suggested UBERON: skin, subcutaneous tissue;
* **open wounds, ulcers, malignant tissue**, and exposed connective tissue;
* **eye**, conjunctiva, eyelids, orbit;
* **external auditory canal**, middle ear;
* **nasal cavity**, turbinates, paranasal sinuses, nasopharynx;
* **oral cavity**, gingiva, palate, tongue, pharynx;
* **urogenital tract**, including vulva, vagina, urethra, bladder;
* rarely gastrointestinal tract.

In animals, hoof/interdigital tissue, genital openings, nasal passages, ethmoid region, and frontal/maxillary sinuses are prominent. In *O. ovis*, first instars are concentrated in septum, meatus, and ventral conchae, whereas later stages occur in the nasopharynx, ethmoid labyrinth, dorsal conchae, and sinuses. (garijo‐toledo2023prevalenceofoestrus pages 1-3)

Disease may be unilateral, bilateral, focal, or multisite; no fixed lateralization exists. At subcellular level there is no disease-specific organelle lesion—the pathology is tissue-level mechanical, enzymatic, inflammatory, and microbial injury.

## 8. Temporal development

Myiasis can occur at any age and is acquired rather than congenital. Furuncular lesions usually evolve over days to weeks; wound and cavitary disease may appear acutely and progress rapidly when produced by obligate tissue-feeding species. In an ICU case, 13 third-instar *L. sericata* larvae were found 60 hours after intubation; developmental modeling indicated at least 30 hours to reach third instar at approximately 34°C, illustrating how temperature and stage can help estimate acquisition. (monney2025myiasisinthe pages 1-2)

There is no universal staging system. A pragmatic sequence is inoculation, larval establishment, progressive local injury, possible secondary infection/deep invasion, and either removal, spontaneous exit/pupation, or complications. Facultative superficial disease is often self-limited after complete extraction. Obligate myiasis can progress until every larva is removed and devitalized tissue is treated. Recurrence generally indicates retained larvae, continued exposure, or inadequately managed wounds rather than biological relapse.

## 9. Inheritance, epidemiology, and population

Myiasis is **not inherited**. Penetrance, expressivity, anticipation, germline mosaicism, carrier frequency, and founder effects are not applicable.

No reliable global incidence or prevalence per 100,000 exists. A bibliometric analysis recovered only 211 PubMed publications on cutaneous myiasis from 2001–2021 and found that case reports remained a defining feature, underscoring surveillance limitations. (zhou2025machinelearningbasedtext pages 2-5, zhou2025machinelearningbasedtext pages 1-2)

Available quantitative observations include:

* An Italian review documented **703 autochthonous cases**, of which **690 (98.1%)** were attributed to *O. ovis*. Among 42 imported cases, **59.5%** involved *Cordylobia* species and **40.5%** *D. hominis*. Historically, 77% of recognized Italian *O. ovis* cases were in shepherds; old occupational surveys reported lifetime histories of approximately 80–87%, but these figures should not be extrapolated to modern populations. (zammarchi2014humanoestriasisacquired pages 2-4)
* A worldwide ICU review identified **38 cases**; **92%** were oro-/nasopharyngeal and **45%** involved *L. sericata*. Fourteen occurred in high-income countries and eight in Europe. (monney2025myiasisinthe pages 2-3)
* Human cases occur in both sexes and all ages. No robust global sex ratio is available. Older, disabled, or critically ill people predominate in wound/nosocomial series, while travelers and otherwise healthy adults commonly develop furuncular disease.

Geography follows fly species: *D. hominis* in tropical America; *Cordylobia* in sub-Saharan Africa; New World screwworm in the Americas where not eradicated; *C. bezziana* across parts of Africa and Asia; and *W. magnifica* across the Palearctic. Imported disease occurs worldwide through travel.

## 10. Diagnostics

### Clinical and laboratory diagnosis

Diagnosis is usually made by seeing or extracting larvae. Examination should determine lesion depth, larval number, necrosis, vascular or neurologic involvement, and proximity to the eye, airway, ear, skull, or major vessels. CBC may show eosinophilia, but no blood biomarker is sufficiently sensitive or specific. Culture blood or tissue when fever, cellulitis, sepsis, or bacteremia is suspected.

### Species identification

Larvae should be preserved appropriately and referred to medical entomology or parasitology. Morphological diagnosis uses size and instar, posterior peritremes/spiracles, anterior spiracles, cephalopharyngeal skeleton, body spines, and anal division. Molecular COI barcoding is valuable when specimens are damaged, morphology is ambiguous, or epidemiological confirmation is important. (simin2024longtimeno pages 2-3, simin2024longtimeno pages 3-5)

### Imaging and pathology

Ultrasound can demonstrate movement in furuncular lesions. CT or MRI is indicated for orbital, sinonasal, aural, intracranial, deep-tissue, or bone involvement. Endoscopy may assist nasal, oral, aural, or urogenital inspection. Histology is not usually required but may show mixed inflammatory infiltrates, necrosis, and larval structures.

### Differential diagnosis

Differentials include bacterial furuncle/abscess, epidermoid cyst, arthropod bite, cutaneous larva migrans, tungiasis, leishmaniasis, pyoderma, foreign-body granuloma, cellulitis, malignancy, mucormycosis, allergic or bacterial conjunctivitis, rhinitis/sinusitis, otitis externa, and delusional infestation. True intestinal or urinary infestation must be distinguished from specimen contamination and pseudomyiasis.

No routine asymptomatic screening, newborn screening, carrier screening, genetic testing, or population screening is warranted.

## 11. Outcome and prognosis

Complete removal in uncomplicated furuncular or superficial facultative disease is usually curative. In the eosinophilic pediatric case, lymphadenopathy and swelling regressed rapidly without additional treatment, and the eosinophil count normalized after larval extraction. (tuygun2009furuncularmyiasisin pages 1-2)

Adverse outcomes include persistent ulceration, bleeding, pain, disfigurement, secondary bacterial infection, cellulitis, osteomyelitis, bacteremia/sepsis, airway compromise, visual loss, hearing injury, intracranial extension, and death. Risk is greatest with obligate tissue-feeding species, large burdens, delayed presentation, deep craniofacial or orbital location, severe comorbidity, and inadequate debridement. In veterinary *W. magnifica* disease, untreated infestation can produce lethargy, depression, inappetence, blindness, lameness, reproductive loss, wasting, and death. (simin2024longtimeno pages 1-2)

There are no validated survival curves, 5- or 10-year survival estimates, prognostic scores, or molecular prognostic biomarkers. Death usually reflects deep invasion, sepsis, or underlying illness rather than a chronic post-myiasis state.

## 12. Treatment and current applications

### Clinical algorithm

1. Stabilize airway, bleeding, sepsis, and ocular or neurologic emergencies.
2. Mechanically remove all visible larvae with forceps and adequate analgesia/anesthesia.
3. Irrigate thoroughly; repeat inspection because deeply embedded larvae may be missed.
4. Debride necrotic tissue, particularly in obligate wound myiasis.
5. Obtain larvae for identification and cultures when infection is suspected.
6. Treat bacterial infection based on clinical findings and cultures—not simply because larvae are present.
7. Consider ivermectin for extensive, inaccessible, orbital, or invasive disease under specialist supervision.
8. Correct the predisposing wound, malignancy, hygiene deficit, or hospital fly-control breach.

Mechanical extraction is the primary intervention. Reviews suggest that antibiotics or antiparasitic agents add little after complete removal of uncomplicated facultative ICU myiasis, whereas obligate myiasis requires aggressive extraction and debridement. (monney2025myiasisinthe pages 2-3, monney2025myiasisinthe pages 3-5)

### Pharmacotherapy and interventions

* **Ivermectin:** a macrocyclic lactone used off-label in selected human myiasis cases; evidence is primarily case-based, and no universal dose or regimen is established across anatomical forms.
* **Antibiotics:** indicated for cellulitis, bacteremia, osteomyelitis, or other secondary infection; they do not remove larvae.
* **Occlusive agents:** petroleum jelly or similar occlusion may force air-breathing furuncular larvae toward the surface. Care is needed because larval rupture or death in situ may intensify inflammation.
* **Surgical/endoscopic extraction and debridement:** required for deep, cavitary, orbital, sinonasal, or destructive lesions.
* **Supportive care:** analgesia, antiseptic wound care, dressings, nutrition, and rehabilitation for functional injury.

Suggested NCIt intervention concepts are **foreign-body removal**, **surgical debridement**, **wound irrigation**, **antibiotic therapy**, **antiparasitic therapy**, **ivermectin**, and **supportive care**. Suggested chemical mappings include ivermectin and antiseptic/irrigation agents; exact CHEBI identifiers require release validation.

The ClinicalTrials.gov search retrieved no relevant interventional myiasis trial. Gene, cell, RNA, immune-checkpoint, or precision-genotype therapies have no role. Pharmacogenomic guidance specific to myiasis is unavailable.

### Important distinction from maggot debridement therapy

Uncontrolled myiasis is not equivalent to regulated maggot debridement therapy (MDT). MDT uses sterile, laboratory-reared facultative larvae—commonly *L. sericata*—to remove necrotic tissue. A 2025 computational/bibliometric study proposed possible benefit in infected diabetic wounds, but this does not justify retaining wild larvae, whose species, burden, and microbiota are uncontrolled. (zhou2025machinelearningbasedtext pages 2-5, malekiravasan2020newinsightsinto pages 1-2)

## 13. Prevention

### Primary prevention

* cover and regularly inspect wounds; promptly remove necrotic tissue;
* maintain personal, oral, household, and livestock hygiene;
* use screens, bed nets, protective clothing, and repellents where flies are active;
* manage garbage, carrion, manure, and animal wounds;
* educate travelers, caregivers, livestock workers, and shepherds;
* implement veterinary surveillance and coordinated screwworm control.

### Secondary and tertiary prevention

Early recognition and complete extraction prevent deep invasion. Patients with malignant wounds, diabetes, vascular ulcers, immobility, tracheostomy/intubation, or impaired consciousness need scheduled skin, mouth, device-site, and wound examinations. Following treatment, repeat inspection and continued wound coverage reduce retained-larva complications and reinfestation.

Hospitals should use window/door screens, air barriers where feasible, pest surveillance, prompt waste removal, environmental fumigation when an outbreak is confirmed, and meticulous oral care for mechanically ventilated patients. Recent ICU reports document fumigation and window screening as practical outbreak responses. (monney2025myiasisinthe pages 13-15, monney2025myiasisinthe pages 3-5)

There is no human vaccine, chemoprophylaxis program, genetic screening, or validated population screening test.

## 14. Other species and natural disease

Myiasis is naturally widespread among mammals and birds. Important hosts include sheep, goats, cattle, horses, pigs, camels, dogs, cats, wildlife, and humans. Taxonomic identifiers should be linked at the causative-species level—for example, *Oestrus ovis*, *W. magnifica*, *L. sericata*, *C. hominivorax*, and *C. bezziana*—rather than treating “maggot” as one organism.

Recent veterinary data show substantial burden:

* In eastern Spain, 3,476 culled sheep/goat heads examined from 2009–2019 yielded **56.3% overall *O. ovis* prevalence**, higher in sheep (**61.2%**) than goats (**43%**). Mean intensity was **12.8 larvae/head**; temperature was significantly associated with prevalence. The abstract concluded that results showed “the trend increasing in recent years in association with higher mean temperatures.” (garijo‐toledo2023prevalenceofoestrus pages 1-3)
* In Mato Grosso, Brazil, **319/697 sheep (45.77%)** were infested; 2,412 larvae were recovered, **96.89%** identified as *O. ovis*. Seasonal prevalence ranged from **41% in spring to 56% in summer**, but larvae occurred year-round. The authors state: “It is also reported as a zoonosis causing ophthalmomyiasis and nasopharyngeal myiasis.” (silva2024prevalenceandseasonal pages 1-3)
* A 2024 Serbian study documented the first reported Western Balkan *W. magnifica* cases in 80 years. Four sheep had severe hoof, genital, or interdigital disease; two hoof wounds contained 400 and 354 larvae, with deep bleeding foci, horn destruction, inflammation, arthritis, lameness, and poor condition. (simin2024longtimeno pages 1-2, simin2024longtimeno pages 3-5)

Animal disease is both an economic/welfare problem and an exposure reservoir, but ordinary human-to-human or animal-to-human transmission does not occur directly: adult flies mediate infestation. The One Health significance includes shared fly ecology, livestock amplification, climate sensitivity, and fly-associated bacteria such as *W. chitiniclastica*.

## 15. Model organisms and research systems

There is no standard genetic knockout, transgenic, zebrafish, organoid, or iPSC model of human myiasis. Natural infestation in sheep, goats, cattle, and other livestock is the most informative comparative system because it reproduces larval colonization, inflammation, pain, tissue destruction, and seasonal ecology. Its limitation is species-specific anatomy and fly–host adaptation.

Experimental models are sparse. A 2026 study—outside the requested 2023–2024 priority window but mechanistically informative—used INFOGEST-like simulated digestive fluids and BALB/c mouse gavage to test *Clogmia albipunctata*. Gastric exposure reduced egg hatchability from **76.80% to 0%** and produced **99.17% larval mortality**; mice showed no shedding, mucosal injury, or colonization. The study supports pseudomyiasis or sample contamination as explanations for many purported intestinal cases, but healthy mice do not model hypochlorhydria, dysmotility, altered microbiota, or immunosuppression. (zhan2026clogmiaalbipunctatafails pages 13-15, zhan2026clogmiaalbipunctatafails pages 1-2)

Other useful platforms include fly-rearing systems, larval feeding assays, wound models, microbiome/metagenetic profiling, COI phylogenetics, and insecticide susceptibility studies. These primarily investigate parasite biology, species identification, MDT, veterinary control, and forensic timing rather than inherited human disease.

## Evidence appraisal and current research priorities

The strongest current evidence concerns clinical recognition, species morphology/molecular identification, and veterinary epidemiology. Human evidence is weak for comparative drug efficacy, standardized ivermectin regimens, global burden, long-term quality of life, and prognostic biomarkers. A 2025 literature analysis found persistent emphasis on uncommon species, nasal disease, travel, and case reports—an expert signal that the field needs prospective surveillance and standardized reporting rather than additional isolated descriptions. (zhou2025machinelearningbasedtext pages 2-5, zhou2025machinelearningbasedtext pages 1-2)

Priority research needs are: mandatory or sentinel reporting in endemic regions; standardized case definitions separating true myiasis from pseudomyiasis; prospective treatment comparisons; validated protocols for orbital, craniofacial, and malignant-wound disease; genomic surveillance of fly populations; systematic characterization of larval microbiota and bacteremia risk; and integrated veterinary–human–environmental surveillance under a One Health framework.

## Key recent sources and publication details

1. Simin S, et al. **Long Time No Hear, Magnificent Wohlfahrtia!** *Microorganisms*. Published **23 January 2024**. DOI/URL: https://doi.org/10.3390/microorganisms12020233. The abstract calls *W. magnifica* “a potentially deadly agent of obligate traumatic myiasis in humans and animals.” (simin2024longtimeno pages 1-2)
2. Silva VLB, et al. **Prevalence and seasonal aspects of parasitism by Oestrus ovis in sheep from Mato Grosso State, Brazil.** *Brazilian Journal of Veterinary Parasitology*. Received **12 December 2023**, accepted **11 March 2024**. DOI/URL: https://doi.org/10.1590/S1984-29612024020. (silva2024prevalenceandseasonal pages 1-3)
3. Garijo-Toledo MM, et al. **Prevalence of Oestrus ovis in small ruminants from the eastern Iberian Peninsula.** *Medical and Veterinary Entomology*. Published **2023**. DOI/URL: https://doi.org/10.1111/mve.12634. (garijo‐toledo2023prevalenceofoestrus pages 1-3)
4. Monney M, et al. **Myiasis in the intensive care unit: report from Switzerland and review of worldwide cases.** *Swiss Medical Weekly*. Published **July 2025**. DOI/URL: https://doi.org/10.57187/s.3827. This post-2024 review supplies the most current aggregated ICU evidence. (monney2025myiasisinthe pages 1-2, monney2025myiasisinthe pages 2-3)
5. Zhou Z, et al. **Machine learning-based text mining for cutaneous myiasis.** *Frontiers in Cellular and Infection Microbiology*. Published **May 2025**. DOI/URL: https://doi.org/10.3389/fcimb.2025.1568563. (zhou2025machinelearningbasedtext pages 2-5)
6. Maleki-Ravasan N, et al. **New Insights Into Culturable and Unculturable Bacteria Across the Life History of Medicinal Maggots Lucilia sericata.** *Frontiers in Microbiology*. Published **8 April 2020**. DOI/URL: https://doi.org/10.3389/fmicb.2020.00505. (malekiravasan2020newinsightsinto pages 1-2)
7. Zammarchi L, et al. **Human oestriasis acquired in Florence and review on human myiasis in Italy.** *Parasitology Research*. Published **May 2014**. DOI/URL: https://doi.org/10.1007/s00436-014-3906-9. (zammarchi2014humanoestriasisacquired pages 2-4)
8. Tuygun N, et al. **Furuncular myiasis in a child caused by Wohlfahrtia magnifica associated with eosinophilia.** *Turkish Journal of Pediatrics*. Published **2009;51:279–281**. Its abstract states: “Following removal of the larva, the clinical and hematological manifestations returned to normal.” (tuygun2009furuncularmyiasisin pages 1-2)

**Database limitation:** PMIDs were not exposed in the retrieved full-text metadata, so DOI URLs are supplied rather than risking incorrect PMID assignment. Likewise, exact MONDO, HPO, GO, CL, UBERON, CHEBI, and NCIt numerical identifiers should be resolved against the knowledge base’s pinned ontology releases before production ingestion.

References

1. (monney2025myiasisinthe pages 1-2): Marine Monney, Jiri Hodecek, Jean-Marc Schwob, N. Buetti, Jacques Schrenzel, and Viviane Donner. Myiasis in the intensive care unit: report from switzerland and review of worldwide cases. Swiss medical weekly, 155:3827, Jul 2025. URL: https://doi.org/10.57187/s.3827, doi:10.57187/s.3827. This article has 1 citations and is from a peer-reviewed journal.

2. (monney2025myiasisinthe pages 3-5): Marine Monney, Jiri Hodecek, Jean-Marc Schwob, N. Buetti, Jacques Schrenzel, and Viviane Donner. Myiasis in the intensive care unit: report from switzerland and review of worldwide cases. Swiss medical weekly, 155:3827, Jul 2025. URL: https://doi.org/10.57187/s.3827, doi:10.57187/s.3827. This article has 1 citations and is from a peer-reviewed journal.

3. (tuygun2009furuncularmyiasisin pages 1-2): N Tuygun, A Taylan-Ozkan, and G Tanir. Furuncular myiasis in a child caused by wohlfahrtia magnifica (diptera: sarcophagidae) associated with eosinophilia. Unknown journal, 2009.

4. (zhou2025machinelearningbasedtext pages 1-2): Zhiyuan Zhou, Chaoran Yu, Danhua Yao, Zhen Wang, Yuhua Huang, Pengfei Wang, Weimin Wang, and Yousheng Li. Machine learning-based text mining for cutaneous myiasis and potential value of an accidental maggot therapy for complicated skin and soft tissue infection with sepsis. Frontiers in Cellular and Infection Microbiology, May 2025. URL: https://doi.org/10.3389/fcimb.2025.1568563, doi:10.3389/fcimb.2025.1568563. This article has 3 citations.

5. (garijo‐toledo2023prevalenceofoestrus pages 1-3): María Magdalena Garijo‐Toledo, José Sansano‐Maestre, Ana Elena Ahuir‐Baraja, Carlos Martínez‐Carrasco, Francisco Domingo Alonso de Vega, Lola Llobat, and María Rocío Ruiz de Ybáñez‐Carnero. Prevalence of oestrus ovis in small ruminants from the eastern iberian peninsula. a long‐term study. Medical and Veterinary Entomology, 37:330-338, Jan 2023. URL: https://doi.org/10.1111/mve.12634, doi:10.1111/mve.12634. This article has 7 citations and is from a peer-reviewed journal.

6. (silva2024prevalenceandseasonal pages 1-3): V. L. Silva, D. G. S. Ramos, R. C. Pacheco, Diego Montagner Schenkel, Nilton Pereira Dias Junior, Artur Kanadani Campos, and Fernando H. Furlan. Prevalence and seasonal aspects of parasitism by oestrus ovis (diptera: oestridae) in sheep from mato grosso state, brazil. Revista Brasileira de Parasitologia Veterinária / Brazilian Journal of Veterinary Parasitology, Apr 2024. URL: https://doi.org/10.1590/s1984-29612024020, doi:10.1590/s1984-29612024020. This article has 2 citations.

7. (monney2025myiasisinthe pages 2-3): Marine Monney, Jiri Hodecek, Jean-Marc Schwob, N. Buetti, Jacques Schrenzel, and Viviane Donner. Myiasis in the intensive care unit: report from switzerland and review of worldwide cases. Swiss medical weekly, 155:3827, Jul 2025. URL: https://doi.org/10.57187/s.3827, doi:10.57187/s.3827. This article has 1 citations and is from a peer-reviewed journal.

8. (hou2025extensivepalatalnecrosis pages 5-6): Ken Wong Siong Hou, Syamsa Rizal Abdullah, Mohd Rafizul Mohd Yusof, Ahmad Firdaus Mohd Salleh, and Syed Nabil. Extensive palatal necrosis secondary to chrysomya bezziana myiasis: a case report. Archives of Orofacial Sciences, 20:59-68, Jun 2025. URL: https://doi.org/10.21315/aos2025.2001.cr03, doi:10.21315/aos2025.2001.cr03. This article has 0 citations.

9. (simin2024longtimeno pages 1-2): Stanislav Simin, Snežana Tomanović, Ratko Sukara, Marijana Stefanov, Milan Savović, Bojan Gajić, and Vesna Lalošević. Long time no hear, magnificent wohlfahrtia! morphological and molecular evidence of almost forgotten flesh fly in serbia and western balkans. Microorganisms, 12:233, Jan 2024. URL: https://doi.org/10.3390/microorganisms12020233, doi:10.3390/microorganisms12020233. This article has 2 citations.

10. (malekiravasan2020newinsightsinto pages 1-2): Naseh Maleki-Ravasan, Nahid Ahmadi, Zahra Soroushzadeh, Abbas Ali Raz, Sedigheh Zakeri, and Navid Dinparast Djadid. New insights into culturable and unculturable bacteria across the life history of medicinal maggots lucilia sericata (meigen) (diptera: calliphoridae). Frontiers in Microbiology, Apr 2020. URL: https://doi.org/10.3389/fmicb.2020.00505, doi:10.3389/fmicb.2020.00505. This article has 46 citations and is from a peer-reviewed journal.

11. (simin2024longtimeno pages 2-3): Stanislav Simin, Snežana Tomanović, Ratko Sukara, Marijana Stefanov, Milan Savović, Bojan Gajić, and Vesna Lalošević. Long time no hear, magnificent wohlfahrtia! morphological and molecular evidence of almost forgotten flesh fly in serbia and western balkans. Microorganisms, 12:233, Jan 2024. URL: https://doi.org/10.3390/microorganisms12020233, doi:10.3390/microorganisms12020233. This article has 2 citations.

12. (simin2024longtimeno pages 3-5): Stanislav Simin, Snežana Tomanović, Ratko Sukara, Marijana Stefanov, Milan Savović, Bojan Gajić, and Vesna Lalošević. Long time no hear, magnificent wohlfahrtia! morphological and molecular evidence of almost forgotten flesh fly in serbia and western balkans. Microorganisms, 12:233, Jan 2024. URL: https://doi.org/10.3390/microorganisms12020233, doi:10.3390/microorganisms12020233. This article has 2 citations.

13. (zhou2025machinelearningbasedtext pages 2-5): Zhiyuan Zhou, Chaoran Yu, Danhua Yao, Zhen Wang, Yuhua Huang, Pengfei Wang, Weimin Wang, and Yousheng Li. Machine learning-based text mining for cutaneous myiasis and potential value of an accidental maggot therapy for complicated skin and soft tissue infection with sepsis. Frontiers in Cellular and Infection Microbiology, May 2025. URL: https://doi.org/10.3389/fcimb.2025.1568563, doi:10.3389/fcimb.2025.1568563. This article has 3 citations.

14. (monney2025myiasisinthe pages 13-15): Marine Monney, Jiri Hodecek, Jean-Marc Schwob, N. Buetti, Jacques Schrenzel, and Viviane Donner. Myiasis in the intensive care unit: report from switzerland and review of worldwide cases. Swiss medical weekly, 155:3827, Jul 2025. URL: https://doi.org/10.57187/s.3827, doi:10.57187/s.3827. This article has 1 citations and is from a peer-reviewed journal.

15. (zammarchi2014humanoestriasisacquired pages 2-4): Lorenzo Zammarchi, Andrea Giorni, Simona Gabrielli, Marianne Strohmeyer, Gabriella Cancrini, and Alessandro Bartoloni. Human oestriasis acquired in florence and review on human myiasis in italy. Parasitology Research, 113:2379-2385, May 2014. URL: https://doi.org/10.1007/s00436-014-3906-9, doi:10.1007/s00436-014-3906-9. This article has 40 citations and is from a peer-reviewed journal.

16. (zhan2026clogmiaalbipunctatafails pages 13-15): Huahan Zhan, Linghong Zhang, Lu Ge, Yanli Chen, Peiyi Zhang, Yumeng Jiao, Xiaocheng Luo, Hui Xia, Qiang Fang, and Zhiyong Tao. Clogmia albipunctata fails to induce true intestinal myiasis: evidence from in vitro and in vivo digestive models. PLOS One, 21(8):e0356742, Aug 2026. URL: https://doi.org/10.1371/journal.pone.0356742, doi:10.1371/journal.pone.0356742. This article has 0 citations and is from a peer-reviewed journal.

17. (zhan2026clogmiaalbipunctatafails pages 1-2): Huahan Zhan, Linghong Zhang, Lu Ge, Yanli Chen, Peiyi Zhang, Yumeng Jiao, Xiaocheng Luo, Hui Xia, Qiang Fang, and Zhiyong Tao. Clogmia albipunctata fails to induce true intestinal myiasis: evidence from in vitro and in vivo digestive models. PLOS One, 21(8):e0356742, Aug 2026. URL: https://doi.org/10.1371/journal.pone.0356742, doi:10.1371/journal.pone.0356742. This article has 0 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Myiasis-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 10 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 2 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 3 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.1590/S1984-29612024020` (4 mentions) - Identifier did not resolve to a record
- `DOI:10.1590/s1984-29612024020` (3 mentions) - Identifier did not resolve to a record