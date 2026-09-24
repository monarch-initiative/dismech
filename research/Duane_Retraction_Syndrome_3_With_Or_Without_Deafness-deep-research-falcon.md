---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-27T15:35:42.748183'
end_time: '2026-08-27T15:43:12.608920'
duration_seconds: 449.86
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Duane Retraction Syndrome 3 With Or Without Deafness
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 13
reference_validation:
  total_references: 8
  verified: 7
  not_found: 0
  unverifiable: 1
  confabulation_rate: 0.0
  relevance_assessed: 7
  on_topic: 3
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Duane_Retraction_Syndrome_3_With_Or_Without_Deafness-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Duane Retraction Syndrome 3 With Or Without Deafness
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Duane Retraction Syndrome 3 With Or Without Deafness** covering all of the
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
- **Disease Name:** Duane Retraction Syndrome 3 With Or Without Deafness
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Duane Retraction Syndrome 3 With Or Without Deafness** covering all of the
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


# Duane Retraction Syndrome 3 With or Without Deafness

## Executive summary and evidence boundaries

Duane retraction syndrome 3 with or without deafness (DRS3) is an ultra-rare, congenital, Mendelian congenital cranial dysinnervation disorder (CCDD) caused by monoallelic **MAFB** dysfunction. Its core manifestation is Duane retraction syndrome—an incomitant strabismus caused by abnormal development of the abducens motor system and aberrant innervation of extraocular muscle—with variably present deafness or inner-ear malformation. The pivotal human-and-mouse report is Park et al., published May 12, 2016 online and June 2, 2016 in *American Journal of Human Genetics* (PMID **27181683**; DOI/URL: https://doi.org/10.1016/j.ajhg.2016.03.023). Its title directly summarizes the principal conclusion: “Loss of MAFB Function in Humans and Mice Causes Duane Syndrome, Aberrant Extraocular Muscle Innervation, and Inner-Ear Defects.” (NCT03059420 chunk 1)

The disease-specific literature remains very small. Consequently, exact phenotype frequencies, penetrance, incidence, life expectancy, and treatment-response rates for genetically confirmed MAFB-DRS3 are not established. Where this report uses broader Duane syndrome evidence, it is explicitly labeled **general DRS evidence** and should not be interpreted as a DRS3-specific frequency estimate.

The following table provides a compact knowledge-base summary.

| Domain | Best-supported finding | Evidence scope/limitation |
|---|---|---|
| Disease identifier | Duane retraction syndrome 3 with or without deafness is represented in Open Targets as **MONDO_0014880**. (OpenTargets Search: Duane retraction syndrome 3-MAFB) | MONDO ID supported; avoid adding unsupported OMIM/Orphanet IDs here. |
| Causal gene | The disease is associated with **MAFB** (**ENSG00000204103**), a large MAF bZIP transcription factor. (OpenTargets Search: Duane retraction syndrome 3-MAFB, fujino2023exploringlargemaf pages 7-9) | Association is well supported genetically, but accessible sources here do not provide a full curated variant list. |
| Inheritance | Curated disease-target evidence labels the inheritance pattern as **monoallelic autosomal**. (OpenTargets Search: Duane retraction syndrome 3-MAFB) | Penetrance and expressivity are not fully quantified in the accessible evidence set. |
| Disease class | This is a **congenital cranial dysinnervation disorder (CCDD)** affecting ocular motility development. (NCT03059420 chunk 1, sanchez2023geneticsofstrabismus pages 1-2) | CCDD classification is strong; some broader DRS literature is not specific to MAFB-related DRS3. |
| Core ocular phenotype | General DRS is defined by **abduction limitation**, variable adduction deficit, **globe retraction**, and **palpebral fissure narrowing on adduction**; DRS is an incomitant strabismus. (derespinis1993duanesretractionsyndrome. pages 15-17, derespinis1993duanesretractionsyndrome. pages 10-11, murillocorrea2009clinicalfeaturesassociated pages 1-2) | These signs are well established for DRS overall; exact frequencies in MAFB-related DRS3 are not available here. |
| Auditory phenotype | DRS3 may occur **with or without deafness**; the key 2016 study title specifically cites **inner-ear defects** in humans and mice. (NCT03059420 chunk 1, OpenTargets Search: Duane retraction syndrome 3-MAFB) | Accessible evidence confirms the auditory/inner-ear association, but detailed audiologic frequencies and subtype breakdown are limited. |
| Developmental mechanism | Best-supported mechanism is **loss of MAFB function** disrupting development/survival of **abducens neurons**, causing **aberrant extraocular muscle innervation** and associated inner-ear defects. (NCT03059420 chunk 1, fujino2023exploringlargemafa pages 7-9, fujino2023exploringlargemaf pages 7-9, sanchez2023geneticsofstrabismus pages 1-2) | Mechanistic chain is supported by human genetics plus mouse data; exact embryonic cell/rhombomere details were not directly accessible. |
| Reported variant example | A reported **heterozygous p.Leu239Pro** MAFB variant lies in the **DNA-binding region** and was described as abolishing **MARE** binding; the same patient also had **FSGS**. (fujino2023exploringlargemafa pages 7-9, fujino2023exploringlargemaf pages 7-9) | Important genotype-phenotype example, but may represent overlap with renal phenotype rather than isolated ocular disease. |
| Animal model support | Mouse data support causality: studies cited report that **loss of Mafb function** causes Duane syndrome-like ocular innervation defects and inner-ear abnormalities; mutant mice with p.Leu239Pro show impaired podocyte differentiation. (NCT03059420 chunk 1, fujino2023exploringlargemaf pages 7-9) | Strong biologic support, but not a complete natural-history model for all human phenotypic variability. |
| Diagnosis | Diagnosis is primarily **clinical ophthalmic assessment** of incomitant strabismus/ocular motility pattern; **MRI** can support cranial nerve and extraocular muscle evaluation; **genetic testing** for MAFB is appropriate in syndromic/familial CCDD evaluation. (murillocorrea2009clinicalfeaturesassociated pages 1-2, NCT03059420 chunk 1) | No disease-specific biomarker or standardized MAFB-only diagnostic algorithm was identified. |
| Management | Current care is **supportive/symptom-directed**, using standard DRS approaches such as refractive/amblyopia management, monitoring, and selected strabismus surgery for abnormal head posture or primary-position deviation. (derespinis1993duanesretractionsyndrome. pages 27-28, derespinis1993duanesretractionsyndrome. pages 26-27, derespinis1993duanesretractionsyndrome. pages 15-17) | Evidence is extrapolated from general DRS management; MAFB-specific treatment studies were not found. |
| Disease-modifying therapy | **No disease-modifying or gene-targeted therapy** was identified for MAFB-related DRS3. (NCT03059420 chunk 1, fujino2023exploringlargemaf pages 7-9) | Current research emphasis is genetic discovery and mechanism, not interventional trials. |
| Ongoing research | A large **observational** genetics study of strabismus/CCDDs is recruiting (**NCT03059420**). (NCT03059420 chunk 1) | This is not a therapeutic trial; it supports gene discovery and phenotypic expansion. |


*Table: This table summarizes the most defensible disease-level facts for Duane retraction syndrome 3 with or without deafness using only accessible cited evidence. It is designed as a compact knowledge-base artifact that distinguishes strong findings from current evidence gaps.*

## 1. Disease information

### Definition

DRS3 is a congenital neurodevelopmental disorder of cranial motor innervation. Failure of normal abducens-neuron/nerve development and anomalous innervation of the lateral rectus produce limited horizontal eye movement, globe retraction, and narrowing of the palpebral fissure during attempted adduction. Hearing impairment is variably present, reflecting involvement of inner-ear development. Curated evidence associates only **MAFB** with the named MONDO entity. (OpenTargets Search: Duane retraction syndrome 3-MAFB, NCT03059420 chunk 1)

### Identifiers and synonyms

- **MONDO:** **MONDO:0014880**.
- **Causal target:** MAFB; Ensembl **ENSG00000204103**; approved name *MAF bZIP transcription factor B*.
- **MeSH:** the parent clinical disorder “Duane Retraction Syndrome” is **D004370**; the broader class “Congenital Cranial Dysinnervation Disorders” is **D000093922**. (NCT03059420 chunk 1, NCT03059420 chunk 2)
- **Common names:** Duane retraction syndrome 3; DRS3; MAFB-related Duane syndrome; Duane syndrome with or without deafness; MAFB-related congenital cranial dysinnervation disorder.
- A disease-specific ICD-10/ICD-11 code was not established in the retrieved evidence. In practice, coding generally occurs under Duane syndrome/strabismus, congenital ocular motility disorder, or cranial-nerve disorder rather than a molecularly specific MAFB code.
- A disease-specific OMIM or Orphanet number could not be verified from the retrieved full-text evidence and is therefore not asserted here.

This report synthesizes **aggregated disease-level resources, published pedigrees/cases, and model-organism studies**, not individual EHR records. Open Targets integrates EVA, Gene2Phenotype, UniProt, ClinVar-like variant records, and literature evidence; it reports five to six evidence items depending on the displayed aggregation. (OpenTargets Search: Duane retraction syndrome 3-MAFB)

## 2. Etiology and risk/protective factors

### Causal factor

The primary cause is a rare, germline, heterozygous/monoallelic pathogenic alteration affecting **MAFB** function. Open Targets assigns the MAFB–DRS3 association a score of 0.637 and identifies monoallelic autosomal inheritance; supporting literature includes PMID 27181683 and PMID 29779709. (OpenTargets Search: Duane retraction syndrome 3-MAFB)

MAFB is a large-MAF basic leucine-zipper transcription factor. Disease-associated alterations may truncate the protein or disrupt its DNA-binding function. A 2023 authoritative review states that the 2016 work identified MAFB as causal for Duane syndrome and concludes that MAFB mutations impair the generation or maintenance of abducens neurons and inner-ear structures. (fujino2023exploringlargemafa pages 7-9, fujino2023exploringlargemaf pages 7-9)

### Risk factors

- **Genetic:** carrying a pathogenic monoallelic MAFB variant is the established major risk factor. A positive family history raises prior probability, although de novo disease is biologically plausible and segregation-specific rates remain unquantified.
- **Environmental/lifestyle/infectious:** no toxin, infection, diet, smoking, alcohol, occupation, or other exposure has been demonstrated to cause MAFB-DRS3.
- **Age/sex:** congenital onset means age is not an acquired risk factor. No reliable DRS3-specific sex ratio exists.
- **General DRS only:** approximately 90% of nonsyndromic DRS is sporadic and roughly 10% familial; these figures should not be assigned directly to MAFB-DRS3. (derespinis1993duanesretractionsyndrome. pages 26-27, murillocorrea2009clinicalfeaturesassociated pages 1-2)

### Protective factors and gene–environment interaction

No genetic protective allele, environmental protective exposure, modifier gene, or replicated MAFB-specific gene–environment interaction is known. Environmental associations reported for common/comitant strabismus are not applicable evidence for this monogenic CCDD. There is likewise no evidence that diet, exercise, or avoidance of a particular exposure prevents DRS3 after conception.

## 3. Phenotypes

### Core and associated manifestations

1. **Abduction limitation/ophthalmoplegia** — congenital clinical sign; usually stable but variable in severity. Suggested HPO: **Abnormality of ocular abduction**, **External ophthalmoplegia**.
2. **Variable limitation of adduction** — congenital sign; HPO: **Abnormality of ocular adduction**.
3. **Globe retraction on adduction** and **palpebral-fissure narrowing on adduction** — defining physical signs caused by horizontal rectus co-contraction; HPO suggestions: **Globe retraction**, **Abnormal palpebral fissure**.
4. **Incomitant strabismus**, including primary-position esotropia, orthotropia, or less commonly exotropia; HPO: **Strabismus**, **Esotropia**, **Exotropia**.
5. **Upshoot/downshoot on adduction** — variable sign due to anomalous innervation and/or mechanical leash effects; HPO: **Abnormal extraocular movement**.
6. **Compensatory head turn** — functional adaptation supporting binocular alignment; HPO: **Abnormal head position**.
7. **Sensorineural hearing loss/deafness and inner-ear abnormality** — optional rather than obligatory, as expressed by “with or without deafness”; HPO: **Sensorineural hearing impairment**, **Deafness**, **Abnormal inner-ear morphology**.

General DRS descriptions document severe abduction limitation, variable adduction limitation, retraction, fissure narrowing, and oblique upshoot/downshoot. Infants may initially show only abduction deficiency, with retraction becoming more evident later as the lateral rectus becomes less elastic or fibrotic. (derespinis1993duanesretractionsyndrome. pages 15-17, derespinis1993duanesretractionsyndrome. pages 10-11, murillocorrea2009clinicalfeaturesassociated pages 1-2)

### Frequency and severity

No defensible percentage is available for any phenotype among molecularly confirmed MAFB-DRS3 cases. General DRS data report Huber type I in about 75%, type II around 7%, hypermetropia in approximately 71%, anisometropia greater than 1 diopter in 23%, and amblyopia in about 14%; these historical pooled values characterize DRS broadly, not DRS3. (derespinis1993duanesretractionsyndrome. pages 10-11)

### Quality of life

DRS3-specific EQ-5D, SF-36, PROMIS, or disease-specific quality-of-life data are unavailable. Extrapolating cautiously from strabismus generally, misalignment can impair binocular vision, cause amblyopia, prompt compensatory head posture, and produce social or occupational discrimination and reduced quality of life. A 2023 review states that strabismus “leads to the disruption of binocular vision, amblyopia, social and occupational discrimination, and decreased quality of life.” (sanchez2023geneticsofstrabismus pages 1-2, sanchez2023geneticsofstrabismus pages 4-5)

No behavioral, psychiatric, or characteristic laboratory phenotype is established for DRS3 itself.

## 4. Genetic and molecular information

### Gene and protein

- **Gene:** MAFB.
- **Ensembl:** ENSG00000204103.
- **Protein class:** large-MAF basic leucine-zipper transcription factor.
- **Molecular function:** sequence-specific DNA binding and transcriptional regulation at MAF-recognition elements (MAREs).
- Suggested GO molecular-function terms: **DNA-binding transcription factor activity**; **sequence-specific double-stranded DNA binding**; **protein heterodimerization activity**.
- Suggested GO cellular component: **nucleus**.

### Pathogenic variants

Curated evidence encompasses missense and frameshift variants and absent gene products, but the retrieved material did not expose a complete, transcript-normalized variant roster or all current ACMG/AMP classifications. (OpenTargets Search: Duane retraction syndrome 3-MAFB)

A documented heterozygous example is **MAFB p.Leu239Pro**. This substitution lies in a highly conserved DNA-binding region and renders MAFB unable to bind the MARE sequence. The reported Japanese patient had Duane syndrome plus focal segmental glomerulosclerosis (FSGS), so the variant illustrates broader MAFB pleiotropy rather than a purely ocular phenotype. Mutant neonatal-mouse podocytes showed impaired differentiation. (fujino2023exploringlargemafa pages 7-9, fujino2023exploringlargemaf pages 7-9)

The review also mentions **c.176C>T (p.Pro59Leu)**, but this is primarily associated with multicentric carpotarsal osteolysis, abnormal MAFB phosphorylation/degradation, and renal disease—not the canonical DRS3 phenotype—and should not be entered as a DRS3 variant without case-level evidence. (fujino2023exploringlargemaf pages 7-9)

The variants are presumed **germline** in this Mendelian condition. There is no evidence for a somatic DRS3 mechanism. Exact gnomAD/TOPMed allele frequencies were not available in the retrieved sources; pathogenic alleles are expected to be very rare, but no numerical frequency should be assigned without variant-specific database review.

### Functional consequence

The best-supported disease model is **loss of function or functional insufficiency**, through truncation/absent product or impaired DNA binding. This differs from stabilization/gain-of-function mechanisms described for phosphorylation-site MAFB variants causing MCTO. (NCT03059420 chunk 1, fujino2023exploringlargemaf pages 7-9)

No validated modifier gene, disease-specific methylation signature, histone abnormality, repeat expansion, aneuploidy, recurrent translocation, or inversion is established. Large deletions involving MAFB remain technically detectable and should be considered when sequence testing is negative, but no recurrent DRS3 copy-number lesion was documented here.

## 5. Environmental information

No environmental, lifestyle, occupational, toxic, radiologic, dietary, or infectious cause is known. DRS3 is not infectious, transmissible, or zoonotic. Historical suggestions that general DRS may reflect a developmental insult during gestational weeks 4–8 do not establish a specific environmental cause and should not displace the demonstrated MAFB etiology. (derespinis1993duanesretractionsyndrome. pages 26-27)

## 6. Mechanism and pathophysiology

### Causal chain

**Upstream:** germline monoallelic MAFB loss or impaired DNA binding → altered transcription during embryonic hindbrain and inner-ear development.

**Intermediate:** deficient generation, differentiation, or maintenance of abducens motor neurons/nerve and abnormal axonal targeting → absent or reduced normal sixth-nerve input to the lateral rectus, with aberrant extraocular-muscle innervation. In CCDDs generally, causal genes disturb either cranial motor-neuron differentiation or axon guidance. (NCT03059420 chunk 1, fujino2023exploringlargemaf pages 7-9, sanchez2023geneticsofstrabismus pages 1-2, sanchez2023geneticsofstrabismus pages 4-5)

**Downstream ocular effect:** inappropriate lateral-rectus activation during adduction and co-contraction with medial rectus → restricted abduction/adduction, globe retraction, fissure narrowing, upshoot/downshoot, strabismus, and compensatory head posture. Electromyographic evidence in general DRS demonstrates paradoxical lateral-rectus innervation during adduction. (derespinis1993duanesretractionsyndrome. pages 26-27, derespinis1993duanesretractionsyndrome. pages 15-17)

**Downstream auditory effect:** disturbed inner-ear development → variably present hearing loss/deafness. Park et al. demonstrated convergent human and mouse ocular and inner-ear abnormalities. (NCT03059420 chunk 1)

### Relevant processes, cells, and structures

Suggested GO biological-process annotations include **hindbrain development**, **cranial nerve development**, **motor neuron differentiation**, **axon guidance**, **neuron projection development**, **inner-ear development**, **DNA-templated transcription regulation**, and **extraocular skeletal muscle innervation**. Suggested Cell Ontology concepts include **motor neuron**, more specifically **abducens motor neuron**, **cranial motor neuron**, **inner-ear sensory epithelial cell/hair cell**, and **extraocular skeletal muscle cell**. Some highly specific labels may require local ontology mapping if no exact CL class exists.

MAFB also regulates macrophage, podocyte, pancreas, parathyroid, thymus, epidermal, urethral, and lymphatic biology. These functions explain pleiotropic MAFB disorders but do not imply that immune, metabolic, or renal dysfunction is universal in DRS3. Mafb-null mice die after birth with hindbrain hypoplasia, respiratory and renal failure; thus complete loss has effects much broader than typical human monoallelic DRS3. (fujino2023exploringlargemaf pages 7-9)

No DRS3-specific inflammation, autoimmunity, oxidative stress, ischemia, fibrosis, metabolomic signature, lipidomic profile, proteomic biomarker, single-cell atlas, spatial-transcriptomic dataset, patient multi-omics analysis, organoid, or CRISPR-screen result was identified. The 2023 MAF review emphasizes that careful comparison of patients and mouse models is needed to uncover mechanisms and develop etiology-based therapies. (fujino2023exploringlargemafa pages 7-9, fujino2023exploringlargemaf pages 7-9)

## 7. Anatomical structures affected

### Primary

- **Nervous system:** embryonic hindbrain/brainstem abducens motor system; sixth cranial nerve.
- **Eye/orbit:** lateral and medial rectus extraocular muscles and their innervation; ocular motor apparatus.
- **Auditory system:** inner ear and potentially vestibulocochlear pathways in hearing-impaired cases.

Suggested UBERON annotations: **hindbrain**, **brainstem**, **abducens nerve**, **eye**, **orbit**, **extraocular muscle**, **lateral rectus muscle**, **medial rectus muscle**, **inner ear**, **cochlea**, and **vestibulocochlear nerve**. Suggested GO cellular-component annotations include **nucleus**, **axon**, **growth cone**, **neuromuscular junction**, and **transcription-factor complex**.

### Secondary/variable

Renal podocytes and glomeruli may be involved in broader MAFB phenotypes, illustrated by p.Leu239Pro-associated FSGS, but renal disease is not established as a required feature of the named DRS3 entity. (fujino2023exploringlargemafa pages 7-9, fujino2023exploringlargemaf pages 7-9)

### Lateralization

DRS can be unilateral, bilateral, or asymmetric. General DRS cohorts show a left-eye preference—approximately 72% among unilateral cases—and female predominance, but DRS3-specific lateralization and sex ratios are unknown. (derespinis1993duanesretractionsyndrome. pages 27-28, derespinis1993duanesretractionsyndrome. pages 26-27)

## 8. Temporal development

DRS3 is **congenital**, originating during embryogenesis. Recognition usually occurs in infancy or childhood when ocular motility, strabismus, or hearing is assessed. The disorder is chronic and lifelong rather than acute, episodic, inflammatory, or relapsing-remitting.

The underlying developmental wiring defect is generally stable. Apparent clinical retraction or mechanical restriction may become more obvious with age, while secondary amblyopia, refractive error, binocular-vision loss, or musculoskeletal consequences of persistent head posture can evolve. There are no validated molecular disease stages, remission pattern, or end-stage state. (derespinis1993duanesretractionsyndrome. pages 15-17)

The critical causal window is prenatal cranial-motor and inner-ear development. The main postnatal therapeutic window is early childhood, when refractive correction and amblyopia therapy can preserve visual development; surgery changes alignment and head posture but cannot reconstruct the embryonic wiring defect.

## 9. Inheritance and population

### Inheritance

Curated evidence identifies **monoallelic autosomal** inheritance, clinically interpreted as autosomal dominant. (OpenTargets Search: Duane retraction syndrome 3-MAFB)

Penetrance is not adequately quantified. Variable expressivity is strongly suggested by “with or without deafness,” differences in ocular involvement, and the broader observation that relatives carrying CCDD mutations may show only some associated features without an ocular-motility disorder. (NCT03059420 chunk 1)

No evidence establishes anticipation, repeat instability, a founder mutation, sex-limited transmission, a consanguinity effect, or a population-specific carrier frequency. Germline mosaicism has not been quantified; it remains a general counseling possibility after an apparently de novo variant.

### Epidemiology

No prevalence or incidence estimate exists for molecularly confirmed MAFB-DRS3. It is substantially rarer than DRS overall. General DRS has been estimated at approximately **1 in 1,000** and accounts for up to **4% of strabismus cases**, but these should not be entered as DRS3 prevalence. Approximately 90% of nonsyndromic DRS is sporadic, with only about 10% familial. (murillocorrea2009clinicalfeaturesassociated pages 1-2)

No reliable ethnic, geographic, age-distribution, or sex-ratio enrichment has been demonstrated for MAFB-DRS3.

## 10. Diagnostics

### Clinical diagnosis

Evaluation should include:

1. Pediatric ophthalmic/orthoptic examination: monocular and binocular ductions, primary-position alignment, globe retraction, fissure narrowing, upshoot/downshoot, compensatory head posture, visual acuity, cycloplegic refraction, stereopsis, and amblyopia assessment.
2. Audiologic testing: age-appropriate otoacoustic emissions, auditory brainstem response, and behavioral pure-tone audiometry, because hearing loss is variably present.
3. Focused examination for additional congenital anomalies and renal assessment when phenotype or genotype suggests broader MAFB involvement.

General DRS diagnosis is principally clinical. Huber type I has limited abduction, type II predominantly limited adduction, and type III limitation of both; however, molecular DRS3 should be classified genetically and phenotypically rather than inferred from Huber type alone. (derespinis1993duanesretractionsyndrome. pages 15-17, derespinis1993duanesretractionsyndrome. pages 10-11)

### Imaging and electrophysiology

High-resolution MRI of the brainstem, cisternal cranial nerves, internal auditory canals, inner ear, orbits, and extraocular muscles can document absent/hypoplastic nerves or structural ear abnormalities and exclude acquired lesions. MRI abnormalities in general DRS can include hypoplastic ocular motor nerves or small innervated muscles. Imaging is supportive, not required in every classic uncomplicated case. (derespinis1993duanesretractionsyndrome. pages 27-28, murillocorrea2009clinicalfeaturesassociated pages 1-2)

Electromyography can demonstrate anomalous lateral-rectus activation but is invasive and rarely needed clinically. There is no diagnostic blood chemistry, urine analyte, tissue biopsy, circulating biomarker, proteomic marker, or metabolomic signature.

### Genetic testing strategy

- Use an ocular-motility/CCDD panel including **MAFB**, **CHN1**, **SALL4**, **HOXA1**, **KIF21A**, **TUBB3**, and other phenotype-appropriate genes.
- Alternatively, sequence MAFB directly when DRS plus hearing loss/inner-ear malformation strongly indicates DRS3.
- Ensure copy-number analysis is included; if panel testing is negative, trio WES or preferably WGS can identify coding, splice, structural, or regulatory variants.
- Confirm candidate variants and segregation by orthogonal testing when appropriate.
- CMA is useful when multiple congenital anomalies suggest a genomic imbalance. Karyotyping/FISH is reserved for suspected cytogenetic rearrangement.
- Mitochondrial DNA, repeat-expansion, epigenomic, liquid-biopsy, proteomic, and metabolomic tests have no established role.

### Differential diagnosis

Important alternatives are isolated congenital sixth-nerve palsy; CHN1-related DRS; SALL4-related Duane-radial ray/Okihiro syndrome; HOXA1-related brainstem dysgenesis; Moebius syndrome; congenital fibrosis of extraocular muscles; horizontal gaze palsy with progressive scoliosis; Brown syndrome; restrictive orbital disease; congenital hearing-loss syndromes; and acquired retraction from trauma, thyroid eye disease, inflammation, tumor, or prior surgery. Acquired conditions are distinguished by later onset, diplopia, pain/proptosis, trauma or surgery history, progressive course, or orbital imaging abnormalities. (derespinis1993duanesretractionsyndrome. pages 15-17, NCT03059420 chunk 1)

### Screening

Population or newborn genomic screening is not established. Cascade testing is appropriate after identifying a familial pathogenic variant. Audiologic screening should not be omitted in confirmed or suspected DRS3. Prenatal or preimplantation testing is technically possible once the familial variant is known, following genetic counseling.

## 11. Outcome and prognosis

No DRS3-specific mortality, five- or ten-year survival, or life-expectancy deficit is documented. Isolated ocular/auditory disease is not expected to shorten survival. Complete Mafb loss is lethal in mice, but that is not an appropriate prognosis model for heterozygous human DRS3. (fujino2023exploringlargemaf pages 7-9)

Principal morbidity includes restricted gaze, anomalous head posture, primary-position misalignment, amblyopia, impaired stereopsis/binocular field, hearing-related communication difficulty, and psychosocial burden. General DRS is described as congenital and nonthreatening; most patients preserve useful vision and many maintain normal stereopsis through compensatory head posture. (derespinis1993duanesretractionsyndrome. pages 27-28, derespinis1993duanesretractionsyndrome. pages 15-17)

The neural dysinnervation itself does not recover. Refractive error and amblyopia are treatable, hearing can be rehabilitated, and alignment/head posture may improve after appropriate surgery. Prognosis depends on bilateral involvement, primary-gaze deviation, amblyopia, severity of head posture, hearing impairment, and additional MAFB-associated organ disease. No validated prognostic molecular biomarker exists.

## 12. Treatment and current applications

There is no approved pharmacologic, gene, RNA, cell, CRISPR, immunologic, or other disease-modifying therapy for MAFB-DRS3. Management is multidisciplinary and phenotype-directed.

### Ophthalmic care

- Observation when alignment in primary gaze, binocular function, and head posture are acceptable.
- Spectacle correction of refractive error.
- Standard amblyopia treatment—optical correction, patching, or atropine penalization as clinically indicated.
- Prisms may help selected small primary-position deviations but cannot restore abduction.
- Strabismus surgery is considered for a substantial compensatory head turn, cosmetically/functionally significant primary-position deviation, severe globe retraction, or disfiguring upshoot/downshoot. General DRS procedures include medial or lateral rectus recession, vertical-rectus or superior-rectus transposition, and lateral-rectus Y-splitting for marked up/downshoot. Surgery must be individualized to alignment, forced duction, innervation pattern, and binocular function. Historical review supports surgery for significant head posture or noticeable deviation and describes recession, Y-splitting, adjustable sutures, and botulinum approaches. (derespinis1993duanesretractionsyndrome. pages 27-28, derespinis1993duanesretractionsyndrome. pages 26-27)

Suggested NCIT concepts: **Strabismus Surgery**, **Extraocular Muscle Recession**, **Muscle Transposition Procedure**, **Corrective Lens Therapy**, **Occlusion Therapy**, **Audiologic Rehabilitation**, **Hearing Aid**, and **Cochlear Implantation**. Exact NCIT identifiers should be validated against the current NCI Thesaurus release before database ingestion.

### Hearing management

ENT/audiology surveillance; hearing aids for aidable loss; communication and educational support; and cochlear-implant evaluation for severe/profound sensorineural loss where cochlear and cochlear-nerve anatomy and physiology permit. No DRS3-specific response rate is available.

### Trials and recent implementation

**NCT03059420**, “Genetic Studies of Strabismus, Congenital Cranial Dysinnervation Disorders (CCDDs), and Their Associated Anomalies,” is a recruiting Boston Children’s Hospital observational cohort, started February 1, 2004, with estimated enrollment of 20,000 and estimated completion in 2030. It accepts participants from one day of age onward and retains DNA-containing blood, saliva, or discarded tissue. Its purpose is gene discovery and functional characterization, not treatment. ClinicalTrials.gov: https://clinicaltrials.gov/study/NCT03059420. Status was verified February 2026. (NCT03059420 chunk 1)

No interventional DRS3 trial or genotype-guided pharmacotherapy was identified.

## 13. Prevention

### Primary prevention

No vaccine, medication, lifestyle change, environmental avoidance strategy, or prophylactic procedure prevents a pathogenic MAFB developmental disorder. Immunization and infectious-disease measures are not disease-specific.

### Secondary prevention

Early recognition can prevent avoidable consequences rather than disease occurrence: prompt cycloplegic refraction and amblyopia management; audiologic assessment; surveillance of visual development and head posture; and evaluation for associated anomalies.

### Genetic prevention and counseling

Offer clinical genetics assessment, segregation testing, cascade testing of at-risk relatives, and reproductive counseling. Under autosomal-dominant inheritance, a heterozygous affected individual generally has a 50% transmission probability per pregnancy, although phenotypic severity and deafness cannot be predicted reliably because expressivity is variable. Prenatal diagnosis and preimplantation genetic testing are possible after identification of the familial variant. Apparently de novo cases have low but nonzero recurrence risk because parental germline mosaicism cannot be excluded.

### Tertiary prevention

Treat amblyopia before visual maturation, correct refractive error, rehabilitate hearing early, monitor educational/language development, and address sustained abnormal head posture to limit secondary disability. There is no population screening program specific to DRS3.

## 14. Other species and natural disease

The key comparative species is the laboratory mouse, **Mus musculus** (NCBI Taxonomy **10090**), carrying the ortholog **Mafb**. Human is **Homo sapiens** (Taxonomy **9606**). MAFB’s developmental transcriptional role is evolutionarily conserved sufficiently for mouse loss-of-function to reproduce ocular motor and inner-ear abnormalities relevant to human disease. (NCT03059420 chunk 1, fujino2023exploringlargemaf pages 7-9)

No naturally occurring veterinary DRS3 attributable to Mafb, affected breed, VBO identifier, wildlife reservoir, cross-species transmission, or zoonotic risk was identified. This is an inherited developmental disorder, not a transmissible disease.

## 15. Model organisms and experimental systems

### Mouse models

Park et al. provided the central disease model: loss of Mafb function in mice causes Duane-like abnormal extraocular-muscle innervation and inner-ear defects, offering strong cross-species support for causal inference from the human variants. (NCT03059420 chunk 1)

Broader Mafb knockout and knock-in models demonstrate hindbrain, respiratory, kidney, parathyroid, pancreatic, macrophage, and developmental functions. Homozygous Mafb-GFP knock-in/knockout mice die immediately after birth with hindbrain hypoplasia plus respiratory and renal failure. CRISPR-generated p.Leu239Pro models support loss of DNA-binding function and abnormal podocyte differentiation. (fujino2023exploringlargemaf pages 7-9)

### Recapitulation and limitations

**Strengths:** direct manipulation of the ortholog; replication of ocular-innervation and inner-ear phenotypes; access to embryonic axon trajectories and tissue histology; mechanistic separation of MAFB dosage and domain-specific effects.

**Limitations:** homozygous null lethality and multisystem disease exceed the typical heterozygous human phenotype; mouse eye-movement behavior and hearing anatomy are not identical to humans; penetrance and clinical variability may not map directly; p.Leu239Pro models also emphasize renal effects.

No validated DRS3 zebrafish, Drosophila, C. elegans, rat, patient-iPSC, cranial-motor-neuron organoid, or disease-specific cell-line model was identified in the retrieved evidence. Suitable future applications include lineage-restricted Mafb deletion, human iPSC-derived hindbrain motor neurons and otic organoids, single-cell transcriptomics of affected embryonic lineages, and rescue testing of variant-specific transcriptional activity.

## Recent developments and expert interpretation

The most relevant recent synthesis is Fujino, Ojima, and Takahashi, published September 27, 2023 in *Genes* (14:1883; DOI/URL: https://doi.org/10.3390/genes14101883). It places DRS within the spectrum of domain- and mechanism-specific large-MAF disorders, highlights the p.Leu239Pro DNA-binding defect, and concludes that MAFB mutations compromise abducens neurons, inner ear, and—in broader phenotypes—podocytes. (fujino2023exploringlargemafa pages 7-9, fujino2023exploringlargemaf pages 7-9)

A July 20, 2023 genetics review emphasizes the contemporary framework that CCDDs result from improper cranial motor-neuron differentiation or abnormal axon guidance and that these remain the strabismus forms with established Mendelian causal genes. DOI/URL: https://doi.org/10.3389/fopht.2023.1233866. (sanchez2023geneticsofstrabismus pages 1-2, sanchez2023geneticsofstrabismus pages 4-5)

No 2023–2024 primary study was found that materially expanded the number of molecularly confirmed MAFB-DRS3 families, established population prevalence, or introduced a targeted therapy. Thus, the 2016 human/mouse study remains the disease-defining primary source, while 2023 work mainly consolidates mechanistic understanding.

## Evidence-quality assessment and knowledge gaps

**Strong evidence:** MAFB causality; monoallelic autosomal inheritance; congenital CCDD classification; abducens/extraocular-innervation mechanism; variable inner-ear/hearing involvement; mouse recapitulation.

**Moderate or extrapolated evidence:** diagnostic work-up, natural history, ophthalmic surgery, quality-of-life burden, and general DRS epidemiology. These derive largely from DRS overall rather than genetically confirmed DRS3.

**Currently unavailable:** molecular-case prevalence and incidence; exact penetrance; robust phenotype percentages; DRS3-specific sex/ethnic/geographic distribution; complete contemporary variant table with gnomAD frequencies; validated modifiers; disease-specific transcriptomic/proteomic/metabolomic signatures; standardized diagnostic criteria; survival statistics; treatment-response rates; and disease-modifying clinical trials.

For knowledge-base implementation, each general-DRS datum should therefore carry an evidence qualifier such as **“phenotypic-parent evidence; not MAFB-specific.”** Variant assertions should be transcript-versioned and rechecked directly in ClinVar/gnomAD before ingestion.

References

1. (NCT03059420 chunk 1): Elizabeth Engle. Genetic Studies of Strabismus, Congenital Cranial Dysinnervation Disorders (CCDDs), and Their Associated Anomalies. Boston Children's Hospital. 2004. ClinicalTrials.gov Identifier: NCT03059420

2. (OpenTargets Search: Duane retraction syndrome 3-MAFB): Open Targets Query (Duane retraction syndrome 3-MAFB, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

3. (fujino2023exploringlargemaf pages 7-9): Mitsunori Fujino, Masami Ojima, and Satoru Takahashi. Exploring large maf transcription factors: functions, pathology, and mouse models with point mutations. Genes, 14:1883, Sep 2023. URL: https://doi.org/10.3390/genes14101883, doi:10.3390/genes14101883. This article has 15 citations.

4. (sanchez2023geneticsofstrabismus pages 1-2): Mayra Martinez Sanchez and Mary C. Whitman. Genetics of strabismus. Frontiers in Ophthalmology, Jul 2023. URL: https://doi.org/10.3389/fopht.2023.1233866, doi:10.3389/fopht.2023.1233866. This article has 34 citations.

5. (derespinis1993duanesretractionsyndrome. pages 15-17): Patrick A. DeRespinis, Anthony R. Caputo, Rudolph S. Wagner, and Suqin Guo. Duane's retraction syndrome. Survey of ophthalmology, 38 3:257-88, Nov 1993. URL: https://doi.org/10.1016/0039-6257(93)90077-k, doi:10.1016/0039-6257(93)90077-k. This article has 325 citations and is from a peer-reviewed journal.

6. (derespinis1993duanesretractionsyndrome. pages 10-11): Patrick A. DeRespinis, Anthony R. Caputo, Rudolph S. Wagner, and Suqin Guo. Duane's retraction syndrome. Survey of ophthalmology, 38 3:257-88, Nov 1993. URL: https://doi.org/10.1016/0039-6257(93)90077-k, doi:10.1016/0039-6257(93)90077-k. This article has 325 citations and is from a peer-reviewed journal.

7. (murillocorrea2009clinicalfeaturesassociated pages 1-2): Claudia E. Murillo-Correa, Veronica Kon-Jara, Elizabeth C. Engle, and Juan C. Zenteno. Clinical features associated with an i126m alpha2-chimaerin mutation in a family with autosomal-dominant duane retraction syndrome. Journal of AAPOS : the official publication of the American Association for Pediatric Ophthalmology and Strabismus, 13 3:245-8, Jun 2009. URL: https://doi.org/10.1016/j.jaapos.2009.03.007, doi:10.1016/j.jaapos.2009.03.007. This article has 23 citations.

8. (fujino2023exploringlargemafa pages 7-9): M Fujino, M Ojima, and S Takahashi. Exploring large maf transcription factors: functions, pathology, and mouse models with point mutations. genes 2023, 14, 1883. Unknown journal, 2023.

9. (derespinis1993duanesretractionsyndrome. pages 27-28): Patrick A. DeRespinis, Anthony R. Caputo, Rudolph S. Wagner, and Suqin Guo. Duane's retraction syndrome. Survey of ophthalmology, 38 3:257-88, Nov 1993. URL: https://doi.org/10.1016/0039-6257(93)90077-k, doi:10.1016/0039-6257(93)90077-k. This article has 325 citations and is from a peer-reviewed journal.

10. (derespinis1993duanesretractionsyndrome. pages 26-27): Patrick A. DeRespinis, Anthony R. Caputo, Rudolph S. Wagner, and Suqin Guo. Duane's retraction syndrome. Survey of ophthalmology, 38 3:257-88, Nov 1993. URL: https://doi.org/10.1016/0039-6257(93)90077-k, doi:10.1016/0039-6257(93)90077-k. This article has 325 citations and is from a peer-reviewed journal.

11. (NCT03059420 chunk 2): Elizabeth Engle. Genetic Studies of Strabismus, Congenital Cranial Dysinnervation Disorders (CCDDs), and Their Associated Anomalies. Boston Children's Hospital. 2004. ClinicalTrials.gov Identifier: NCT03059420

12. (sanchez2023geneticsofstrabismus pages 4-5): Mayra Martinez Sanchez and Mary C. Whitman. Genetics of strabismus. Frontiers in Ophthalmology, Jul 2023. URL: https://doi.org/10.3389/fopht.2023.1233866, doi:10.3389/fopht.2023.1233866. This article has 34 citations.

## Artifacts

- [Edison artifact artifact-00](Duane_Retraction_Syndrome_3_With_Or_Without_Deafness-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 1 |
| References weighed for topical relevance | 7 |
| On topic | 3 |
| Off topic | 0 |

7 of 8 references resolved; the rest could not be looked up either way.