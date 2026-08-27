---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-26T16:36:08.559049'
end_time: '2026-08-26T16:48:56.985226'
duration_seconds: 768.43
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Adamantinoma
  mondo_id: ''
  category: Neoplastic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 25
reference_validation:
  total_references: 8
  verified: 5
  not_found: 1
  unverifiable: 2
  confabulation_rate: 0.167
  relevance_assessed: 5
  on_topic: 1
  unresolved_references:
  - DOI:10.14670/hh-18-950
  needs_review: true
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Adamantinoma-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Adamantinoma
- **MONDO ID:**  (if available)
- **Category:** Neoplastic

## Research Objectives

Please provide a comprehensive research report on **Adamantinoma** covering all of the
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
- **Disease Name:** Adamantinoma
- **MONDO ID:**  (if available)
- **Category:** Neoplastic

## Research Objectives

Please provide a comprehensive research report on **Adamantinoma** covering all of the
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


# Adamantinoma of Long Bones: Disease-Characteristics Research Report

## Scope and evidence note

This report concerns **adamantinoma of long bones**, not ameloblastoma of the jaw, adamantinomatous craniopharyngioma, or adamantinoma-like Ewing sarcoma (ALES). Those are biologically distinct entities whose similar names commonly produce database-search false positives. Evidence for adamantinoma is limited by extreme rarity; much of the quantitative literature consists of retrospective referral-center series, pathology cohorts, case reports, and narrative reviews rather than prospective trials.

The most useful recent sources retrieved were Węgrzyniak *et al.*, published **30 August 2023** (DOI: [10.12775/JEHS.2023.47.01.003](https://doi.org/10.12775/JEHS.2023.47.01.003)), and Monteiro *et al.*, accepted **9 February 2024**. The major primary clinical benchmark remains Keeney *et al.*’s 85-case series, published **1 August 1989** (DOI: [10.1002/1097-0142(19890801)64:3%3C730::AID-CNCR2820640327%3E3.0.CO;2-P](https://doi.org/10.1002/1097-0142(19890801)64:3%3C730::AID-CNCR2820640327%3E3.0.CO;2-P)).

| Domain | Evidence-based entry | Suggested ontology |
|---|---|---|
| Definition/classification | Adamantinoma of long bone is a rare primary low-grade malignant bone tumor with biphasic epithelial and osteofibrous components, most often arising in the tibial diaphysis. WHO 2020 places it among “other mesenchymal tumours of bone” and recognizes classic adamantinoma, OFD-like adamantinoma, and dedifferentiated adamantinoma. It is distinct from adamantinoma-like Ewing sarcoma, which is a separate EWSR1/FET-ETS–rearranged round-cell sarcoma mimic rather than true adamantinoma. (wegrzyniak2023currentclinicopathologicalcharacterisation pages 1-5, wegrzyniak2023currentclinicopathologicalcharacterisation pages 5-9, jain2008adamantinomaaclinicopathological pages 1-2, rekhi2025osteofibrousdysplasia(ofd) pages 8-10) | MONDO: adamantinoma (MONDO_0002422); NCIT: Adamantinoma; MeSH: Adamantinoma; UBERON: tibia, fibula; NCIT/WHO class: other mesenchymal tumours of bone |
| Epidemiology | Reported frequency is ~0.1–0.5% of primary bone tumors. Landmark 85-case series: 70/85 tibial, 11 of those with fibular involvement; age range 3–72 years, average 25.9 years; slight male excess (45 male, 39 female, 1 unknown). Reviews summarize typical presentation at 20–40 years, often 25–35 years. (wegrzyniak2023currentclinicopathologicalcharacterisation pages 5-9, keeney1989adamantinomaoflong pages 1-2, jain2008adamantinomaaclinicopathological pages 1-2) | NCIT: Rare Neoplasm; HPO onset terms: Adult onset, Adolescent onset |
| Anatomy/localization | Strong predilection for long bones (reported 97%), especially tibia (80–85%), usually anterior cortex/diaphysis; ipsilateral fibular involvement in ~10–15%. Rare sites include femur, ulna, humerus, radius, ribs, spine, and pretibial soft tissue. Lesions are often intracortical but may extend into medulla and soft tissue. (jain2008adamantinomaaclinicopathological pages 1-2, jain2008adamantinomaaclinicopathological pages 2-4, keeney1989adamantinomaoflong pages 1-2, keeney1989adamantinomaoflong pages 2-3) | UBERON: tibia, fibula, cortical bone, bone marrow, soft tissue; CL: epithelial cell, fibroblast |
| Phenotype/natural history | Presentation is indolent and nonspecific: pain, swelling, stiffness, deformity/bowing, impaired weight-bearing; pathologic fracture reported up to ~23–25%. Course is slow and progressive, with symptoms sometimes present for years before diagnosis; recurrence/metastasis may appear many years later. (jain2008adamantinomaaclinicopathological pages 1-2, wegrzyniak2023currentclinicopathologicalcharacterisation pages 5-9, keeney1989adamantinomaoflong pages 1-2, kumar2021anunusualcase pages 6-7) | HPO: HP:0012531 Pain; HP:0001382 Joint stiffness; HP:0009826 Limb swelling; HP:0000927 Abnormality of the skeletal system; HP:0002757 Pathological fracture |
| Distinguishing subtypes | Classic adamantinoma: usually >20 years, overt epithelial nests in fibrous stroma, more aggressive malignant behavior. OFD-like adamantinoma: usually younger patients/teens, intracortical lesion with sparse keratin-positive epithelial nests often requiring IHC, better prognosis but long follow-up needed; possible progression to classic tumor reported. Dedifferentiated adamantinoma: classic areas plus high-grade sarcomatous component, more aggressive. Adamantinoma-like Ewing sarcoma differs by molecular fusion status and immunophenotype. (wegrzyniak2023currentclinicopathologicalcharacterisation pages 5-9, wegrzyniak2023currentclinicopathologicalcharacterisation pages 9-13, jain2008adamantinomaaclinicopathological pages 2-4, rekhi2025osteofibrousdysplasia(ofd) pages 8-10) | NCIT: Classic Adamantinoma; NCIT: Dedifferentiated Adamantinoma; NCIT/WHO: Osteofibrous dysplasia-like adamantinoma; NCIT: Ewing Sarcoma |
| Molecular findings | Evidence supports epithelial differentiation with cytokeratin expression. Recurrent cytogenetic copy-number abnormalities/gains involving chromosomes 7, 8, 12, 19, and 21 have been reported. Candidate/nonvalidated tumor findings summarized in recent reviews include KMT2D mutation and increased DLK1 expression; these are research-level, not established clinical drivers. Increased epithelial-cell proliferation markers and EGFR expression relative to stromal component have been proposed. No validated germline causal gene, hereditary syndrome, or standard actionable target is established. (wegrzyniak2023currentclinicopathologicalcharacterisation pages 5-9, jain2008adamantinomaaclinicopathological pages 6-8, amr2026managementoftibial pages 4-6) | HGNC: KMT2D, DLK1, EGFR, TP53; GO: keratinization/epithelial cell differentiation, cell proliferation; CL: epithelial cell, fibroblast |
| Pathophysiology | Current model is a biphasic neoplasm of epithelial cells embedded in osteofibrous stroma. Reviews propose that the epithelial component is the primary neoplastic population, potentially stimulating stromal proliferation; relation to osteofibrous dysplasia remains debated, with some evidence for a spectrum/continuum in a subset. Mechanistic evidence remains limited and largely histologic/cytogenetic rather than pathway-resolved. (wegrzyniak2023currentclinicopathologicalcharacterisation pages 5-9, jain2008adamantinomaaclinicopathological pages 4-5, jain2008adamantinomaaclinicopathological pages 6-8) | GO: epithelial cell proliferation, extracellular matrix organization; CL: epithelial cell, fibroblast; UBERON: cortical bone |
| Diagnosis | Diagnosis integrates radiology, biopsy, histology, and IHC. Radiographs typically show multilocular osteolytic lesion with sclerosis and “soap-bubble” appearance; CT defines cortex and pulmonary metastases; MRI is best for intramedullary, cortical, multifocal, and soft-tissue extent. Histology shows epithelial islands/nests/cords in fibrous stroma with tubular, basaloid, squamous, spindle-cell, or OFD-like patterns. Extensive sampling is important, especially for OFD-like lesions. (jain2008adamantinomaaclinicopathological pages 2-4, wegrzyniak2023currentclinicopathologicalcharacterisation pages 9-13, amr2026managementoftibial pages 4-6, monteiro2024adamantinomadetíbia pages 4-6, jain2008adamantinomaaclinicopathological pages 9-10) | NCIT: Magnetic Resonance Imaging, Computed Tomography, Radiography, Biopsy; HPO: HP:0031837 Osteolytic lesion |
| Diagnostic immunophenotype | Typical tumor epithelial cells are positive for broad cytokeratins, especially CK5/CK14/CK19, and often p63; EMA may be positive in classic lesions but can be variable. IHC is particularly valuable for detecting sparse epithelial nests in OFD-like lesions and excluding mimics. (jain2008adamantinomaaclinicopathological pages 1-2, wegrzyniak2023currentclinicopathologicalcharacterisation pages 5-9, amr2026managementoftibial pages 4-6, monteiro2024adamantinomadetíbia pages 4-6) | HGNC/Protein markers: KRT5, KRT14, KRT19, TP63, EPCAM/EMA |
| Differential diagnosis | Key differentials: osteofibrous dysplasia, fibrous dysplasia, Ewing sarcoma/adamantinoma-like Ewing sarcoma, osteosarcoma, metastatic carcinoma, vascular tumors, osteomyelitis. OFD is typically strictly intracortical and benign; adamantinoma-like Ewing sarcoma is separated by fusion testing and a different IHC/genetic profile. (jain2008adamantinomaaclinicopathological pages 2-4, jain2008adamantinomaaclinicopathological pages 8-9, wegrzyniak2023currentclinicopathologicalcharacterisation pages 9-13, rekhi2025osteofibrousdysplasia(ofd) pages 8-10) | NCIT: Osteofibrous Dysplasia, Fibrous Dysplasia of Bone, Ewing Sarcoma, Osteosarcoma, Carcinoma Metastatic in Bone |
| Prognosis | Landmark series reported local recurrence in 26/85 (31%), lung metastasis in 13/85 (15%), lymph-node metastasis in 6/85 (7%), and disease-specific death in 11 patients. Reviews summarize recurrence ~18–32% and metastasis ~12–30%, often to lung and regional lymph nodes, with very late events possible. Poorer outcomes are associated with male sex, pain, shorter symptom duration, inadequate/intralesional treatment, and lack of squamous differentiation; margin status is a major predictor. (keeney1989adamantinomaoflong pages 1-2, keeney1989adamantinomaoflong pages 6-7, jain2008adamantinomaaclinicopathological pages 6-8, amr2026managementoftibial pages 6-7, kumar2021anunusualcase pages 6-7) | NCIT: Local Recurrence, Lung Metastasis, Lymph Node Metastasis, Prognostic Factor |
| Treatment/current practice | Standard treatment is wide en-bloc resection with negative margins, usually with limb-salvage reconstruction when feasible. Amputation is reserved for unresectable recurrence, extensive disease, or reconstructive failure. Chemotherapy and radiotherapy have no established routine benefit in conventional adamantinoma. Reconstruction options reported include allograft, vascularized fibular graft, endoprosthetic approaches, and other limb-salvage methods. (jain2008adamantinomaaclinicopathological pages 6-8, kumar2021anunusualcase pages 6-7, amr2026managementoftibial pages 8-9, monteiro2024adamantinomadetíbia pages 4-6) | NCIT: Surgical Resection, Limb Salvage Procedure, Bone Grafting, Amputation |
| Follow-up/prevention | No validated primary-prevention strategy, screening program, or hereditary-risk testing framework is established. Because recurrence and metastasis may occur after long latency, prolonged or lifelong imaging surveillance is recommended after definitive surgery. (keeney1989adamantinomaoflong pages 1-2, amr2026managementoftibial pages 6-7, amr2026managementoftibial pages 8-9) | NCIT: Surveillance, Follow-Up Care |
| Evidence gaps | No robust evidence for infectious cause, environmental cause, protective factors, gene-environment interaction, validated circulating biomarkers, disease-specific staging system, standard targeted therapy, immunotherapy, liquid biopsy, single-cell or spatial transcriptomics atlas, animal model, or natural nonhuman disease counterpart was established in the retrieved evidence. Clinical-trial search did not identify relevant interventional trials for this disease; false-positive hits referred to ameloblastoma/craniopharyngioma. (OpenTargets Search: adamantinoma, wegrzyniak2023currentclinicopathologicalcharacterisation pages 1-5, wegrzyniak2023currentclinicopathologicalcharacterisation pages 5-9, wegrzyniak2023currentclinicopathologicalcharacterisation pages 9-13) | Evidence gap annotation; NCIT: Not Available / Unknown |


*Table: This compact table summarizes the most evidence-supported knowledge-base fields for adamantinoma of long bones, emphasizing distinctions among classic, OFD-like, and adamantinoma-like Ewing entities. It is useful for rapid curation because it combines clinical facts, molecular caveats, and suggested ontology mappings in one place.*

## 1. Disease information

### Definition and classification

Adamantinoma is an **exceedingly rare, primary, usually low-grade malignant bone neoplasm** characterized by epithelial tumor cells embedded in an osteofibrous or fibroblastic stroma. Its canonical location is the anterior cortex and diaphysis of the tibia. The 2020 WHO classification uses the name **“adamantinoma of long bones”**, places it among “other mesenchymal tumours of bone,” and recognizes classic, osteofibrous-dysplasia-like (OFD-like), and dedifferentiated forms. OFD-like adamantinoma is classified as intermediate/locally aggressive, whereas classic and dedifferentiated forms are malignant. The 2008 review’s abstract states directly: “Adamantinoma is a primary low-grade, malignant bone tumor that is predominantly located in the mid-portion of the tibia.” (jain2008adamantinomaaclinicopathological pages 1-2, wegrzyniak2023currentclinicopathologicalcharacterisation pages 1-5, wegrzyniak2023currentclinicopathologicalcharacterisation pages 5-9)

### Identifiers and synonyms

- **MONDO:** **MONDO:0002422**, adamantinoma. Open Targets returned this disease record but no established associated therapeutic target. (OpenTargets Search: adamantinoma)
- **Common names:** adamantinoma; adamantinoma of long bones; long-bone adamantinoma; tibial adamantinoma.
- **Subtype synonyms:** differentiated adamantinoma, juvenile adamantinoma, intracortical adamantinoma, regressive adamantinoma, and OFD-like adamantinoma have historically overlapped, although current WHO terminology favors **OFD-like adamantinoma**.
- **MeSH:** Adamantinoma is an indexed disease concept; curators should verify the current identifier in the target terminology release.
- **ICD:** There is no sufficiently specific ICD-10-CM code for adamantinoma. Coding generally uses the malignant bone-neoplasm code selected by anatomical site; ICD-O morphology coding should be checked against the applicable registry edition.
- **OMIM/Orphanet:** No hereditary Mendelian disease entry or causal-gene record was established in the retrieved evidence. A specific Orphanet identifier should not be asserted without direct registry verification.

The evidence summarized here is **aggregated disease-level literature**, not individual EHR-derived data. The 2024 report is an individual clinical case and is identified as such. (monteiro2024adamantinomadetíbia pages 1-4, monteiro2024adamantinomadetíbia pages 4-6)

## 2. Etiology and risk factors

The cause remains unknown. Epithelial differentiation is strongly supported by broad cytokeratin staining and ultrastructural features including basal lamina and desmosomes. Historical hypotheses—embryonic displacement of basal epidermal cells, traumatic implantation, synovial, vascular, or mesenchymal origin—have not yielded a proven initiating cause. The embryonic-displacement hypothesis was motivated by the tumor’s anterior tibial predilection, where skin lies close to developing bone. (jain2008adamantinomaaclinicopathological pages 1-2)

### Risk, protective, and gene–environment factors

- **Germline risk:** No validated causal germline variant, susceptibility locus, familial syndrome, founder mutation, carrier state, or Mendelian inheritance pattern is established.
- **Age/sex:** Typical presentation is in the second through fifth decades, especially ages 20–40. A slight male excess is repeatedly reported. These are demographic associations, not demonstrated causal factors. (keeney1989adamantinomaoflong pages 1-2, jain2008adamantinomaaclinicopathological pages 1-2, wegrzyniak2023currentclinicopathologicalcharacterisation pages 5-9)
- **Trauma:** Trauma has often been reported, but evidence is inconsistent. In the 85-case series, only 12 patients had a trauma history and the authors could not infer causality; an older literature review reported trauma in approximately 60%. Trauma may simply draw attention to a pre-existing lesion. (keeney1989adamantinomaoflong pages 1-2, keeney1989adamantinomaoflong pages 2-3, keeney1989adamantinomaoflong pages 6-7, jain2008adamantinomaaclinicopathological pages 1-2)
- **Environmental/lifestyle/occupational exposures:** No reproducible association with smoking, alcohol, diet, radiation, toxins, pollution, occupation, or physical inactivity is established.
- **Infection:** No bacterial, viral, fungal, or parasitic cause is known.
- **Protective factors and gene–environment interactions:** None validated.

## 3. Phenotypes

Presentation is typically **insidious, chronic, and progressive**. In the 85-case series, among 65 patients with known symptoms, 34 had pain plus swelling, 14 painless swelling, 14 pain alone, and three pathological fracture. Symptom duration ranged from two weeks to 50 years; 41/64 patients had symptoms for less than five years and 23 for at least five years. (keeney1989adamantinomaoflong pages 1-2)

| Phenotype | Type and characteristics | Suggested HPO term |
|---|---|---|
| Localized limb/bone pain | Common symptom; variable severity; chronic progressive course | **HP:0012531 Pain**; more specific bone-pain term if available |
| Local swelling/mass | Common clinical sign; usually firm, sometimes warm | **HP:0009826 Limb swelling** |
| Progressive tibial deformity/bowing | Less frequent; reflects anterior cortical remodeling | **HP:0000927 Abnormality of the skeletal system**; tibial bowing term where supported |
| Pathological fracture | Reported in approximately 10% radiographically in the 85-case study and up to 23% in reviews | **HP:0002757 Pathological fracture** |
| Stiffness/impaired weight-bearing | Functional manifestation in larger lesions | **HP:0001382 Joint stiffness**, gait-abnormality term if documented |
| Osteolytic lesion | Imaging phenotype, often multilocular with peripheral sclerosis | **HP:0031837 Osteolytic lesion** |
| Neurologic deficit | Rare, restricted to spinal disease | Site-specific neurologic HPO term |
| Hypercalcemia | Very rare paraneoplastic finding reported with pulmonary metastases | **HP:0003072 Hypercalcemia** |

There are no robust disease-specific EQ-5D, SF-36, PROMIS, or utility estimates. Quality of life may be impaired by pain, reduced weight-bearing, deformity, fracture, major resection, graft or prosthetic complications, limb-length discrepancy, repeated reconstruction, or amputation. The 2024 pediatric case explicitly reported limitation of daily activities. (monteiro2024adamantinomadetíbia pages 4-6)

## 4. Genetic and molecular information

### Tumor genetics

Adamantinoma is not presently a hereditary single-gene disorder. Reported abnormalities are **tumor-level/somatic research findings**, not clinically validated constitutional pathogenic variants.

- Aneuploidy and recurrent extra copies of chromosomes **7, 8, 12, 19, and 21** have been reported. (jain2008adamantinomaaclinicopathological pages 6-8, wegrzyniak2023currentclinicopathologicalcharacterisation pages 5-9)
- A 2019 molecular study summarized by the 2023 review proposed **KMT2D mutation** and increased **DLK1** expression as potential markers. These are candidate findings—not sufficient to define a causal gene, ACMG pathogenic germline variant, or approved treatment target. (wegrzyniak2023currentclinicopathologicalcharacterisation pages 5-9)
- Open Targets listed **zero established target associations** for MONDO:0002422. This is important negative evidence against importing BRAF/SMO findings from ameloblastoma or CTNNB1 findings from adamantinomatous craniopharyngioma. (OpenTargets Search: adamantinoma)
- No validated modifier gene, allele frequency, penetrance estimate, pharmacogenomic marker, or standard ClinVar-classified disease variant is established.

### Protein and immunophenotypic findings

The epithelial tumor cells express broad cytokeratins, particularly **KRT5, KRT14, and KRT19**, and commonly p63; EMA is often reported but may be variable. Older studies found p53 immunoreactivity in epithelial cells. The osteofibrous stroma is vimentin-positive. Keratin expression and epithelial ultrastructure support true epithelial differentiation. (amr2026managementoftibial pages 4-6, jain2008adamantinomaaclinicopathological pages 1-2, wegrzyniak2023currentclinicopathologicalcharacterisation pages 5-9)

A 2024 classic-tumor case was AE1/AE3-positive in the epithelial component and p63-positive, but EMA, CK19, CD34, and the reported CK99 stain were negative, illustrating that a panel plus morphology is more reliable than any single marker. (monteiro2024adamantinomadetíbia pages 4-6)

### Epigenetics and structural abnormalities

No reproducible disease-defining methylation class, histone-mark signature, enhancer alteration, or chromosomal translocation is established for true adamantinoma. This differs critically from ALES, which usually has a FET–ETS fusion such as **EWSR1::FLI1**. Molecular testing is particularly appropriate in a small-round-cell, head-and-neck, or otherwise atypical “adamantinoma-like” lesion. (rekhi2025osteofibrousdysplasia(ofd) pages 8-10)

## 5. Environmental information

No causal toxin, radiation exposure, pollutant, occupational exposure, lifestyle behavior, or infectious agent has been demonstrated. Trauma is best treated as an uncertain historical association rather than an environmental cause. Consequently, there are no evidence-based dietary, exercise, exposure-avoidance, antimicrobial, or vaccination recommendations specific to disease prevention.

## 6. Mechanism and pathophysiology

### Current causal model

1. An unidentified initiating event produces an epithelial neoplastic clone in cortical bone.
2. Tumor epithelial cells proliferate as nests, cords, tubules, basaloid islands, squamous areas, or spindle-shaped cells.
3. Epithelial–stromal signaling promotes a prominent fibro-osseous response, yielding the characteristic biphasic lesion.
4. Slow longitudinal growth causes cortical osteolysis, sclerosis, expansion, medullary extension, deformity, pain, and sometimes fracture.
5. Cortical breakthrough permits soft-tissue extension; lymphovascular dissemination produces regional-node and pulmonary metastases.
6. In rare cases, dedifferentiation generates a high-grade pleomorphic sarcomatous component and more aggressive behavior. (jain2008adamantinomaaclinicopathological pages 2-4, wegrzyniak2023currentclinicopathologicalcharacterisation pages 5-9, wegrzyniak2023currentclinicopathologicalcharacterisation pages 9-13)

The epithelial component has greater Ki-67 and growth-factor/receptor expression than the stroma in older studies, supporting the interpretation that epithelial cells are the neoplastic driver and that osteofibrous tissue is at least partly reactive. Nevertheless, whether OFD, OFD-like adamantinoma, and classic adamantinoma form a universal biological continuum remains disputed. Documented progression supports a continuum in some patients, but older clinicopathologic work did not establish that ordinary OFD is invariably a precursor. (jain2008adamantinomaaclinicopathological pages 4-5, wegrzyniak2023currentclinicopathologicalcharacterisation pages 5-9)

Suggested annotations include **GO epithelial cell proliferation**, **GO extracellular matrix organization**, **GO cell population proliferation**, and **GO epithelial cell differentiation**; cell types include **CL epithelial cell** and **CL fibroblast**. There is no established disease-specific metabolic, autophagic, immune-checkpoint, inflammatory, mitochondrial, or ion-channel mechanism.

### Molecular profiling and advanced technologies

Small genomic/cytogenetic studies exist, but no validated transcriptomic classifier, clinical proteomic or metabolomic signature, lipidomic profile, single-cell atlas, spatial-transcriptomic map, integrated multi-omics cohort, or CRISPR/RNAi dependency screen was identified. These are major research gaps.

## 7. Anatomical structures affected

- **Primary organ/system:** skeleton, especially long bones of the lower limb.
- **Canonical site:** anterior cortex of the tibial diaphysis; suggested terms: **UBERON tibia**, **UBERON cortical bone**, **UBERON diaphysis**.
- **Secondary local structures:** medullary cavity/bone marrow, periosteum, adjacent fibula, subcutaneous tissue, and other soft tissues.
- **Frequency:** Reviews estimate 97% occur in long bones and 80–85% in the tibia. In the primary 85-case series, 70/85 involved the tibia; 11 of those also involved the fibula. Six arose in femur, three ulna, two humerus, two fibula, one radius, and one pretibial soft tissue. Approximately 90% were diaphyseal. (keeney1989adamantinomaoflong pages 1-2, keeney1989adamantinomaoflong pages 2-3, jain2008adamantinomaaclinicopathological pages 1-2)
- **Distant sites:** lung and regional lymph nodes predominate; bone, vertebral column, brain, and other sites are rare.
- **Lateralization:** no meaningful biological laterality is established; the 85-case series had 34 right and 32 left lesions among cases with known side. (keeney1989adamantinomaoflong pages 2-3)
- **Subcellular compartments:** diagnostic keratins are cytoplasmic/cytoskeletal; p63/p53 are nuclear. No organelle-specific pathogenic defect is known.

## 8. Temporal development

Classic adamantinoma most often presents from adolescence through middle adulthood, with a median/typical age around 25–35 years; OFD-like disease is enriched in children and adolescents, generally under 20. The 85-case series had an age range of 3–72 years and mean age 25.9 years. (keeney1989adamantinomaoflong pages 1-2, jain2008adamantinomaaclinicopathological pages 1-2, jain2008adamantinomaaclinicopathological pages 2-4)

The course is chronic and slowly progressive rather than episodic. Local recurrence in the 85-case series occurred after a mean 4.7 years, range 3 months–19.4 years; lymph-node metastasis occurred after a mean 5.8 years, and lung metastasis after a mean 8.2 years, range 1.1–17.9 years. Events several decades after treatment have also been reported, supporting prolonged—often lifelong—surveillance. Spontaneous remission is not expected for classic adamantinoma; apparent regression is discussed principally in OFD/OFD-like lesions. (amr2026managementoftibial pages 6-7, keeney1989adamantinomaoflong pages 3-6)

## 9. Inheritance and population

Adamantinoma is **sporadic**, with no established autosomal dominant, autosomal recessive, X-linked, mitochondrial, polygenic, or anticipation pattern. Penetrance, carrier frequency, germline mosaicism, founder effects, consanguinity, and prenatal risk are therefore not applicable.

It accounts for approximately **0.1–0.5% of primary bone tumors**, but reliable population incidence and point-prevalence estimates per 100,000 are not well established. No consistent ethnic, geographic, or endemic pattern is known. The 85-case cohort included 45 males, 39 females, and one patient of unknown sex; reviews summarize the sex ratio as approximately 5:4 male:female. (keeney1989adamantinomaoflong pages 1-2, jain2008adamantinomaaclinicopathological pages 1-2, wegrzyniak2023currentclinicopathologicalcharacterisation pages 5-9)

## 10. Diagnostics

### Recommended work-up

1. **Plain radiography:** typically central or eccentric, longitudinal, multilocular osteolysis with septation, peripheral sclerosis, cortical expansion/thinning, and a “soap-bubble” appearance.
2. **MRI of the entire involved bone:** best for skip/satellite foci, medullary extent, cortical breakthrough, soft-tissue involvement, and surgical margins. Typical signal is low/intermediate on T1 and high on T2/STIR, with enhancement. Two patterns are described: a solitary lobulated focus or multiple small nodules in one or more foci.
3. **CT:** clarifies cortical destruction and mineralization; chest CT is important for pulmonary staging.
4. **Biopsy planned with the definitive sarcoma surgeon:** central and extensive sampling is crucial because peripheral OFD-like areas may lack obvious epithelial nests.
5. **Histology and IHC:** establish biphasic architecture and epithelial differentiation.
6. **Molecular testing where morphology is atypical:** fusion testing helps exclude ALES and synovial sarcoma. (monteiro2024adamantinomadetíbia pages 4-6, jain2008adamantinomaaclinicopathological pages 2-4, jain2008adamantinomaaclinicopathological pages 9-10, wegrzyniak2023currentclinicopathologicalcharacterisation pages 9-13)

### Pathology

Classic tumors contain bland epithelial nests within fibrous stroma. Patterns include tubular, basaloid, squamous, spindle-cell, and OFD-like forms. Mitoses are usually sparse—historically 0–2 per 10 high-power fields—and marked atypia is unusual outside dedifferentiated disease. OFD-like tumors are predominantly fibro-osseous and may contain only tiny keratin-positive epithelial clusters. (keeney1989adamantinomaoflong pages 2-3, jain2008adamantinomaaclinicopathological pages 2-4, wegrzyniak2023currentclinicopathologicalcharacterisation pages 9-13)

### Differential diagnosis

The principal differentials are OFD, fibrous dysplasia, OFD-like adamantinoma, osteosarcoma, Ewing/ALES, intraosseous synovial sarcoma, metastatic carcinoma, epithelioid vascular tumors, nonossifying fibroma, and osteomyelitis. OFD is generally benign and strictly intracortical; true adamantinoma more often extends toward marrow and contains demonstrable epithelial tumor cells. ALES commonly arises in head/neck soft tissue or bone, expresses CD99/NKX2.2 and keratins, and is defined by a FET–ETS fusion. (rekhi2025osteofibrousdysplasia(ofd) pages 8-10, jain2008adamantinomaaclinicopathological pages 2-4, jain2008adamantinomaaclinicopathological pages 8-9)

No diagnostic blood/urine test, circulating biomarker, liquid biopsy, validated WES/WGS panel, CMA, mitochondrial assay, or repeat-expansion test is recommended routinely. There is no population screening or cascade testing.

## 11. Outcome and prognosis

In the 85-case primary series, **26/85 (31%)** developed local recurrence, **13/85 (15%)** lung metastases, **6/85 (7%)** lymph-node metastases, and 11 died from disease. Nine of 13 patients with lung metastasis had preceding local recurrence, and recurrence significantly increased pulmonary-metastasis risk. (keeney1989adamantinomaoflong pages 1-2, keeney1989adamantinomaoflong pages 3-6, keeney1989adamantinomaoflong pages 6-7)

Broader reviews report local recurrence around **18–32%**, metastasis approximately **12–30%**, and mortality around **13–18%**, but these estimates mix eras and treatments. A modern synthesis cited 5- and 10-year recurrence estimates of 8.6% and 18.6%, 10-year disease-specific survival of 92%, and recurrence-free survival of 72%; interpretation requires caution because source populations and subtype composition differ. (jain2008adamantinomaaclinicopathological pages 6-8, amr2026managementoftibial pages 6-7, amr2026managementoftibial pages 8-9, kumar2021anunusualcase pages 6-7)

Adverse factors reported across retrospective studies include inadequate/intralesional surgery or positive margins, male sex, pain, symptom duration under five years, local recurrence, pathological fracture, skip lesions/periosteal involvement, younger age, and absence of squamous differentiation. Margin status is the most actionable and consistent factor. These associations should not be treated as validated individual-risk calculators. (jain2008adamantinomaaclinicopathological pages 6-8, amr2026managementoftibial pages 8-9, keeney1989adamantinomaoflong pages 1-2, keeney1989adamantinomaoflong pages 6-7)

## 12. Treatment

### Standard treatment

**Wide en-bloc resection with histologically negative margins** is the treatment of choice. Limb salvage is preferred when adequate margins and useful function are achievable. Reconstruction may use intercalary allograft, vascularized fibular autograft, bone transport/distraction osteogenesis, endoprosthetic reconstruction, or combinations selected by tumor length, joint involvement, age, and remaining growth. Suggested NCIT terms include **Surgical Resection**, **Wide Excision**, **Limb Salvage Procedure**, **Bone Grafting**, **Reconstructive Surgical Procedure**, and **Amputation**. (jain2008adamantinomaaclinicopathological pages 6-8, amr2026managementoftibial pages 8-9, kumar2021anunusualcase pages 6-7, wegrzyniak2023currentclinicopathologicalcharacterisation pages 5-9)

Amputation is reserved for unresectable or repeatedly recurrent disease, inability to obtain margins, major neurovascular involvement, infection, or failed reconstruction; it has not shown an inherent survival advantage over adequate wide resection. Curettage and other intralesional procedures are inappropriate for classic adamantinoma because of high recurrence risk. (amr2026managementoftibial pages 6-7, wegrzyniak2023currentclinicopathologicalcharacterisation pages 5-9)

### Systemic and radiation treatment

Conventional chemotherapy and radiotherapy have no established routine efficacy. Anecdotal use of tyrosine-kinase inhibitors such as pazopanib or sunitinib has been discussed for unresectable/metastatic disease, but there is no validated response rate, approved adamantinoma-specific target, or standard regimen. Genotype-guided therapy, checkpoint inhibition, CAR-T therapy, gene therapy, ASOs/siRNA, and mRNA therapy are investigational or unsupported. (jain2008adamantinomaaclinicopathological pages 6-8, amr2026managementoftibial pages 8-9, kumar2021anunusualcase pages 6-7)

A ClinicalTrials.gov search did **not** identify a relevant adamantinoma interventional study; retrieved hits concerned similarly named ameloblastoma or craniopharyngioma and must not be assigned to this disease.

### Supportive care

Management includes analgesia, fracture precautions, physical and occupational therapy, gait training, orthotics/prosthetics when appropriate, surveillance of graft union and hardware, and psychosocial support. Reconstruction can require repeated revision because of nonunion, graft fracture, infection, limb-length discrepancy, or prosthetic failure. No adamantinoma-specific pharmacogenomic guidance exists.

## 13. Prevention

There is no known primary prevention because no modifiable cause is established. There is no population, newborn, carrier, prenatal, or germline screening program and no vaccine or prophylactic drug.

Secondary prevention consists of prompt specialist assessment of persistent tibial pain, swelling, deformity, or a characteristic cortical lesion and avoiding unplanned curettage. Tertiary prevention includes complete initial resection, fracture prevention, rehabilitation, and very long-term local and chest surveillance. Genetic counseling is not routinely indicated for familial risk, although counseling about the absence of demonstrated heritability may be useful.

## 14. Other species and natural disease

No well-validated naturally occurring veterinary counterpart, breed predisposition, orthologous causal gene, cross-species susceptibility, or comparative spontaneous-disease cohort was identified. Adamantinoma is not infectious and has no zoonotic or cross-species transmission potential. Reports using “adamantinoma” in veterinary or older pathology sources require careful review because the term has historically been applied to odontogenic tumors.

## 15. Model organisms and experimental systems

No standardized mouse, rat, zebrafish, invertebrate, genetically engineered, humanized, patient-derived xenograft, organoid, iPSC, or validated cell-line model was identified. Consequently, no model has been shown to reproduce the human tibial cortical localization, biphasic epithelial–osteofibrous architecture, prolonged latency, or late metastatic behavior. Development of authenticated patient-derived cultures, organoids, xenografts, and spatial/single-cell datasets is a major unmet research need.

## Recent developments and expert interpretation

The 2023 review emphasizes three practical developments: adoption of the 2020 WHO three-part classification, increasing use of combined immunohistochemical and genetic assessment, and MRI-based definition of full tumor extent before wide-margin surgery. Its abstract concludes that “confirmation of the immunohistochemical profile, as well as the genetic profile…is essential for diagnosis” and that the best treatment remains resection with large margins. (wegrzyniak2023currentclinicopathologicalcharacterisation pages 1-5)

The 2024 tibial case illustrates current real-world implementation: serial radiography, CT and MRI; centrally sampled biopsy; morphology plus p63/AE1-AE3 IHC; and limb-preserving resection/reconstruction. It also demonstrates the risk of misleading early imaging labels and postoperative functional complications in young patients. (monteiro2024adamantinomadetíbia pages 1-4, monteiro2024adamantinomadetíbia pages 4-6)

The central expert conclusion is that adamantinoma remains a **surgically curable but deceptively persistent malignancy**. Accurate subtype assignment, exclusion of molecular mimics, complete initial resection, and decades-long surveillance are more clinically consequential than presently available molecular-targeting strategies.

References

1. (wegrzyniak2023currentclinicopathologicalcharacterisation pages 1-5): A Węgrzyniak, W Wokurka, and D Drobek. Current clinicopathological characterisation of adamantinoma-a review of the literature. Unknown journal, 2023.

2. (wegrzyniak2023currentclinicopathologicalcharacterisation pages 5-9): A Węgrzyniak, W Wokurka, and D Drobek. Current clinicopathological characterisation of adamantinoma-a review of the literature. Unknown journal, 2023.

3. (jain2008adamantinomaaclinicopathological pages 1-2): Deepali Jain, Vijay K Jain, Rakesh K Vasishta, Prabhat Ranjan, and Yashwant Kumar. Adamantinoma: a clinicopathological review and update. Diagnostic Pathology, 3:8-8, Feb 2008. URL: https://doi.org/10.1186/1746-1596-3-8, doi:10.1186/1746-1596-3-8. This article has 130 citations and is from a peer-reviewed journal.

4. (rekhi2025osteofibrousdysplasia(ofd) pages 8-10): B Rekhi, R Jayan, R Jayan, and B Rekhi. Osteofibrous dysplasia (ofd) and adamantinoma: a comprehensive review and updates. Histology and histopathology, pages 18950, Jun 2025. URL: https://doi.org/10.14670/hh-18-950, doi:10.14670/hh-18-950. This article has 3 citations and is from a peer-reviewed journal.

5. (keeney1989adamantinomaoflong pages 1-2): Gary L. Keeney, K. Krishnan Unni, John W. Beabout, and Douglas J. Pritchard. Adamantinoma of long bones. a clinicopathologic study of 85 cases. Cancer, 64:730-737, Aug 1989. URL: https://doi.org/10.1002/1097-0142(19890801)64:3<730::aid-cncr2820640327>3.0.co;2-p, doi:10.1002/1097-0142(19890801)64:3<730::aid-cncr2820640327>3.0.co;2-p. This article has 218 citations and is from a domain leading peer-reviewed journal.

6. (jain2008adamantinomaaclinicopathological pages 2-4): Deepali Jain, Vijay K Jain, Rakesh K Vasishta, Prabhat Ranjan, and Yashwant Kumar. Adamantinoma: a clinicopathological review and update. Diagnostic Pathology, 3:8-8, Feb 2008. URL: https://doi.org/10.1186/1746-1596-3-8, doi:10.1186/1746-1596-3-8. This article has 130 citations and is from a peer-reviewed journal.

7. (keeney1989adamantinomaoflong pages 2-3): Gary L. Keeney, K. Krishnan Unni, John W. Beabout, and Douglas J. Pritchard. Adamantinoma of long bones. a clinicopathologic study of 85 cases. Cancer, 64:730-737, Aug 1989. URL: https://doi.org/10.1002/1097-0142(19890801)64:3<730::aid-cncr2820640327>3.0.co;2-p, doi:10.1002/1097-0142(19890801)64:3<730::aid-cncr2820640327>3.0.co;2-p. This article has 218 citations and is from a domain leading peer-reviewed journal.

8. (kumar2021anunusualcase pages 6-7): Arvind Kumar, Ruchi Sharma, Anil Kumar Verma, Abhijeet Tiwari, and Jyoti Mishra. An unusual case of adamantinoma of long bone. Autopsy & Case Reports, 11:e2021276, May 2021. URL: https://doi.org/10.4322/acr.2021.276, doi:10.4322/acr.2021.276. This article has 7 citations.

9. (wegrzyniak2023currentclinicopathologicalcharacterisation pages 9-13): A Węgrzyniak, W Wokurka, and D Drobek. Current clinicopathological characterisation of adamantinoma-a review of the literature. Unknown journal, 2023.

10. (jain2008adamantinomaaclinicopathological pages 6-8): Deepali Jain, Vijay K Jain, Rakesh K Vasishta, Prabhat Ranjan, and Yashwant Kumar. Adamantinoma: a clinicopathological review and update. Diagnostic Pathology, 3:8-8, Feb 2008. URL: https://doi.org/10.1186/1746-1596-3-8, doi:10.1186/1746-1596-3-8. This article has 130 citations and is from a peer-reviewed journal.

11. (amr2026managementoftibial pages 4-6): Yasser Amr, Aye Htun, and Simerjit Singh. Management of tibial adamantinoma: balancing oncologic cure and reconstructive longevity. Cureus, Aug 2026. URL: https://doi.org/10.7759/cureus.113794, doi:10.7759/cureus.113794. This article has 0 citations.

12. (jain2008adamantinomaaclinicopathological pages 4-5): Deepali Jain, Vijay K Jain, Rakesh K Vasishta, Prabhat Ranjan, and Yashwant Kumar. Adamantinoma: a clinicopathological review and update. Diagnostic Pathology, 3:8-8, Feb 2008. URL: https://doi.org/10.1186/1746-1596-3-8, doi:10.1186/1746-1596-3-8. This article has 130 citations and is from a peer-reviewed journal.

13. (monteiro2024adamantinomadetíbia pages 4-6): LS de Sousa Monteiro and LF Vitule. Adamantinoma de tíbia: adamantinoma of the tibia. Unknown journal, 2024.

14. (jain2008adamantinomaaclinicopathological pages 9-10): Deepali Jain, Vijay K Jain, Rakesh K Vasishta, Prabhat Ranjan, and Yashwant Kumar. Adamantinoma: a clinicopathological review and update. Diagnostic Pathology, 3:8-8, Feb 2008. URL: https://doi.org/10.1186/1746-1596-3-8, doi:10.1186/1746-1596-3-8. This article has 130 citations and is from a peer-reviewed journal.

15. (jain2008adamantinomaaclinicopathological pages 8-9): Deepali Jain, Vijay K Jain, Rakesh K Vasishta, Prabhat Ranjan, and Yashwant Kumar. Adamantinoma: a clinicopathological review and update. Diagnostic Pathology, 3:8-8, Feb 2008. URL: https://doi.org/10.1186/1746-1596-3-8, doi:10.1186/1746-1596-3-8. This article has 130 citations and is from a peer-reviewed journal.

16. (keeney1989adamantinomaoflong pages 6-7): Gary L. Keeney, K. Krishnan Unni, John W. Beabout, and Douglas J. Pritchard. Adamantinoma of long bones. a clinicopathologic study of 85 cases. Cancer, 64:730-737, Aug 1989. URL: https://doi.org/10.1002/1097-0142(19890801)64:3<730::aid-cncr2820640327>3.0.co;2-p, doi:10.1002/1097-0142(19890801)64:3<730::aid-cncr2820640327>3.0.co;2-p. This article has 218 citations and is from a domain leading peer-reviewed journal.

17. (amr2026managementoftibial pages 6-7): Yasser Amr, Aye Htun, and Simerjit Singh. Management of tibial adamantinoma: balancing oncologic cure and reconstructive longevity. Cureus, Aug 2026. URL: https://doi.org/10.7759/cureus.113794, doi:10.7759/cureus.113794. This article has 0 citations.

18. (amr2026managementoftibial pages 8-9): Yasser Amr, Aye Htun, and Simerjit Singh. Management of tibial adamantinoma: balancing oncologic cure and reconstructive longevity. Cureus, Aug 2026. URL: https://doi.org/10.7759/cureus.113794, doi:10.7759/cureus.113794. This article has 0 citations.

19. (OpenTargets Search: adamantinoma): Open Targets Query (adamantinoma, 6 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

20. (monteiro2024adamantinomadetíbia pages 1-4): LS de Sousa Monteiro and LF Vitule. Adamantinoma de tíbia: adamantinoma of the tibia. Unknown journal, 2024.

21. (keeney1989adamantinomaoflong pages 3-6): Gary L. Keeney, K. Krishnan Unni, John W. Beabout, and Douglas J. Pritchard. Adamantinoma of long bones. a clinicopathologic study of 85 cases. Cancer, 64:730-737, Aug 1989. URL: https://doi.org/10.1002/1097-0142(19890801)64:3<730::aid-cncr2820640327>3.0.co;2-p, doi:10.1002/1097-0142(19890801)64:3<730::aid-cncr2820640327>3.0.co;2-p. This article has 218 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Adamantinoma-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 1 |
| Unverifiable | 2 |
| References weighed for topical relevance | 5 |
| On topic | 1 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.14670/hh-18-950` (3 mentions) - Identifier did not resolve to a record