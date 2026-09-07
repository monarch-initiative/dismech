---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-26T08:38:38.060595'
end_time: '2026-08-26T08:48:51.216269'
duration_seconds: 613.16
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Alopecia-Intellectual Disability Syndrome 1
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 19
reference_validation:
  total_references: 6
  verified: 3
  not_found: 3
  unverifiable: 0
  confabulation_rate: 0.5
  relevance_assessed: 3
  on_topic: 1
  unresolved_references:
  - DOI:10.1007/s00439-016-1756-5](https://doi.org/10.1007/s00439-016-1756-5
  - DOI:10.3389/fnins.2024.1301865](https://doi.org/10.3389/fnins.2024.1301865
  - DOI:10.1038/s41390-019-0499-0](https://doi.org/10.1038/s41390-019-0499-0
  needs_review: true
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Alopecia-Intellectual_Disability_Syndrome_1-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Alopecia-Intellectual Disability Syndrome 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Alopecia-Intellectual Disability Syndrome 1** covering all of the
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
- **Disease Name:** Alopecia-Intellectual Disability Syndrome 1
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Alopecia-Intellectual Disability Syndrome 1** covering all of the
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


# Alopecia–Intellectual Disability Syndrome 1 (APMR1): comprehensive disease-characteristics report

## Executive summary and evidence limits

Alopecia–intellectual disability syndrome 1 (APMR1; historically *alopecia–mental retardation syndrome 1*) is an exceptionally rare autosomal-recessive neurocutaneous disorder characterized principally by partial or complete alopecia and intellectual disability. The molecular evidence currently rests mainly on one large consanguineous Iranian family: seven affected relatives were homozygous for **AHSG c.950G>A (p.Arg317His; rs201849460)**, whereas seven unaffected relatives carried either one variant allele or the reference genotype. The association is compelling but not yet supported by numerous unrelated families or a disease-recapitulating experimental model. Accordingly, **AHSG should be treated as the reported/proposed APMR1 causal gene, with limited replication**, rather than as a comprehensively validated gene–disease relationship. (sailani2017associationofahsg pages 4-7, sailani2017associationofahsg pages 1-3, sailani2017associationofahsg pages 3-4)

The most important recent disease-family update is a 2024 comparative APMR study. It continues to distinguish APMR1 from LSS-related APMR4 and describes APMR1 as generally involving mild-to-moderate intellectual disability; however, it adds little new APMR1-specific molecular evidence. (kang2024clinicalandgenetic pages 1-2)

| Domain | Key findings | Quantitative details | Evidence level | Citation |
|---|---|---|---|---|
| Identity / identifier | Disease resolved as **alopecia-mental retardation syndrome 1 (APMR1)**, a very rare autosomal recessive condition mapped to **chromosome 3q26.33-q27.3**; characterized by alopecia with intellectual disability. OMIM given as **203650**. | Single disease entity discussed in one primary molecular report; linkage region reported as **17 Mb** on chr3. | Human clinical / gene-mapping | (sailani2017associationofahsg pages 1-3, sailani2017associationofahsg pages 4-7) |
| Gene and variant | Candidate causal gene is **AHSG** (*alpha-2-HS-glycoprotein*; fetuin-A; OMIM **138680**). Reported disease-associated variant: **c.950G>A (p.Arg317His)** in **exon 7**; dbSNP **rs201849460**. | Variant genomic position reported as **chr3:186338565**; rarity in ExAC reported as **MAF 0.0008%**. In silico scores: MutationTaster **0.95**, PolyPhen **0.99**, SIFT **0.0**. | Human segregation + computational | (sailani2017associationofahsg pages 1-3, sailani2017associationofahsg pages 3-4) |
| Inheritance / family | Inheritance is consistent with **autosomal recessive** transmission in a **large consanguineous Iranian family**. Variant segregated with disease. | **7 affected homozygous** individuals; **7 unaffected** relatives were heterozygous or homozygous reference; segregation significance reported as **chi-square P=0.01**. | Human segregation | (sailani2017associationofahsg pages 1-3, sailani2017associationofahsg pages 4-7, sailani2017associationofahsg pages 3-4) |
| Phenotype and patient counts | Core phenotype is **alopecia** plus **intellectual disability**. Hair loss may be **complete or partial**. APMR1 is described in 2024 context as having **mild-to-moderate ID**; developmental delay and epilepsy have been noted in APMR1 generally, but were not individually detailed in the extracted 2017 family table. | **7 affected** relatives total; ages explicitly visible for 7 individuals: **3Y, 4Y, 14Y, 17Y, 21Y, 23Y, 24Y**; sexes: **4 male, 3 female**; alopecia pattern among listed individuals: **3 complete, 4 partial**; IQ range **40-54**. | Human clinical observation | (sailani2017associationofahsg pages 3-4, kang2024clinicalandgenetic pages 1-2) |
| Functional evidence | AHSG/fetuin-A is implicated in **protein processing/post-translational modification**, **BMP/TGF-beta antagonism**, **keratinocyte migration**, and possible **brain developmental** roles. The APMR1 variant lies in the protein processing region and is predicted to disrupt a phosphorylation motif near **Thr319**; patient serum AHSG showed altered migration on SDS-PAGE. | Predicted loss/change of kinase recognition around **p.Thr319** with probabilities reported in one analysis as **0.96-0.74** for **PKA/DMPK/AUR** kinases; western blot showed **two bands in affected** versus **single bands in unaffected** controls. | In vitro / biochemical + computational | (sailani2017associationofahsg pages 4-7, sailani2017associationofahsg pages 3-4, sailani2017associationofahsg pages 7-8, sailani2017associationofahsg pages 8-9) |
| Diagnosis | No disease-specific standardized diagnostic criteria were identified. Current practical diagnosis depends on recognizing the phenotype and confirming **biallelic AHSG variation**, typically via **whole-exome sequencing** or other molecular testing. Broader ichthyosis/alopecia-neurodevelopmental literature supports NGS for rare syndromic differential diagnosis. | In a syndromic/non-syndromic ichthyosis cohort, NGS achieved a molecular diagnosis in **53/64 patients (82.8%)**, illustrating utility of panel/WES approaches for overlapping phenotypes. | Human diagnostic practice / extrapolated rare-disease genomics | (sailani2017associationofahsg pages 1-3, kang2024clinicalandgenetic pages 1-2) |
| Treatment / trials | **No disease-specific therapy** or management guideline for APMR1 was found in the retrieved evidence. Management is therefore presumed **supportive and multidisciplinary** (developmental, neurologic, dermatologic, rehabilitation, genetic counseling) rather than disease-modifying. **No relevant interventional clinical trials** were retrieved. | **0 relevant trials found** in the searched trial results. | Evidence gap / no active trial evidence retrieved | (sailani2017associationofahsg pages 3-4) |
| Major evidence gaps | Evidence base is extremely limited: one genetically resolved family, sparse natural-history data, no prevalence/incidence estimates, no penetrance estimates, no standardized diagnostic criteria, no biomarker validation, no disease-specific therapy, and no direct APMR1 animal model identified. Existing animal evidence for **AHSG** is indirect and comes from other phenotypes involving fetuin-A deficiency. | Human molecular evidence currently rests mainly on **1 family / 7 affected individuals**; indirect AHSG biology from knockout animals links fetuin-A deficiency to mineralization and bone phenotypes rather than a fully recapitulated APMR1 syndrome. | Animal indirect + evidence gap | (sailani2017associationofahsg pages 1-3, merdlerrabinowicz2019fetuinadeficiencyis pages 3-4, merdlerrabinowicz2019fetuinadeficiencyis pages 4-5) |


*Table: This table summarizes the strongest currently available evidence for alopecia-mental retardation syndrome 1 (APMR1), including identifiers, AHSG variant data, family segregation, phenotype counts, functional findings, and the major unresolved gaps. It is useful for rapidly distinguishing established human evidence from indirect mechanistic or animal evidence.*

## 1. Disease information

### Definition and identifiers

* **Preferred name:** Alopecia–intellectual disability syndrome 1.
* **Historical names/synonyms:** alopecia–mental retardation syndrome 1; APMR1; alopecia with mental retardation syndrome; AHSG-associated alopecia–intellectual disability syndrome.
* **OMIM phenotype:** **203650**.
* **Mapped locus:** chromosome **3q26.33–q27.3**, originally a roughly 17-Mb linkage interval.
* **Gene entry:** **AHSG**, OMIM **138680**; protein alpha-2-HS-glycoprotein/fetuin-A.
* **MONDO, Orphanet, MeSH, ICD-10 and ICD-11:** a disease-specific identifier/code was not established in the retrieved evidence. For coding, a combination of alopecia, intellectual disability, and genetic-syndrome categories may be necessary; these are not equivalent to a dedicated APMR1 code and should not be entered as exact mappings.
* **Category:** Mendelian, autosomal recessive, neurocutaneous/neuroectodermal syndrome. (sailani2017associationofahsg pages 1-3)

The evidence is **aggregated family-level research data**, not EHR-derived population data. Individual-level details were reported for seven affected relatives, but no registry or population cohort exists in the retrieved literature. (sailani2017associationofahsg pages 3-4)

**Primary source:** Sailani et al., *Human Genetics*, published January 2017, DOI [10.1007/s00439-016-1756-5](https://doi.org/10.1007/s00439-016-1756-5). A PMID was not available in the retrieved record and should be verified directly in PubMed before database deposition. (sailani2017associationofahsg pages 1-3)

## 2. Etiology

### Causal and genetic factors

The reported molecular cause is homozygosity for **AHSG c.950G>A, p.Arg317His**, an exon-7 missense variant. It lay both within the prior linkage interval and a run of homozygosity, segregated with disease, and was extremely rare in ExAC (**MAF 0.0008%**). Reported predictions were MutationTaster 0.95, PolyPhen 0.99, and SIFT 0.0. The variant affects a conserved residue in a protein-processing region. (sailani2017associationofahsg pages 4-7, sailani2017associationofahsg pages 1-3)

The variant was homozygous in all seven affected relatives. Seven unaffected relatives were heterozygous or reference homozygotes; reported segregation was χ² **P=0.01**. This supports recessive inheritance, but one pedigree cannot establish population-wide penetrance or the full allelic spectrum. (sailani2017associationofahsg pages 4-7, sailani2017associationofahsg pages 3-4)

### Other risk, protective, and gene–environment factors

* **Established risk:** biallelic inheritance of the familial AHSG allele; parental consanguinity increases the probability that descendants inherit the same rare allele from both parents.
* **Environmental or infectious risk factors:** none demonstrated.
* **Lifestyle risks:** none demonstrated.
* **Protective alleles, modifier genes, or protective exposures:** none reported.
* **Gene–environment interaction:** not studied.
* **Somatic contribution:** unsupported; this is presumed a germline disorder.

These absences reflect lack of evidence, not proof that modifiers cannot exist.

## 3. Phenotypes

### Core observed phenotype

All seven molecularly described relatives had alopecia and intellectual disability. Ages were 3, 4, 14, 17, 21, 23, and 24 years; there were four males and three females. Three were described as having complete alopecia and four partial alopecia. All had reported Stanford–Binet IQ values in the **40–54** range. Thus, within this selected family, both major manifestations occurred in **7/7 (100%)**, although this cannot be generalized to all future AHSG genotypes. (sailani2017associationofahsg pages 7-8, sailani2017associationofahsg pages 3-4)

The disease-level description includes loss of scalp hair and absence of eyebrows and eyelashes. Recent comparative literature classifies APMR1 intellectual disability as usually mild-to-moderate and states that developmental delay and epilepsy can occur in APMR1, but the retrieved primary family text did not provide patient-by-patient seizure histories, onset ages, EEG results, or developmental milestones. (sailani2017associationofahsg pages 1-3, kang2024clinicalandgenetic pages 1-2)

### Ontology-ready phenotype suggestions

| Manifestation | Type/course | Suggested HPO annotation |
|---|---|---|
| Partial or complete scalp alopecia | Physical sign; pediatric presentation documented; persistence likely, but formal longitudinal data absent | **Alopecia (HP:0001596)**; consider partial/total alopecia child terms after HPO verification |
| Absent/sparse eyebrows | Physical sign; disease-level description | **Sparse eyebrow (HP:0045075)** or absent eyebrow term after ontology verification |
| Absent/sparse eyelashes | Physical sign | **Sparse eyelashes (HP:0000653)** or absent eyelashes term after verification |
| Intellectual disability, IQ 40–54 | Neurodevelopmental/behavioral phenotype; mild-to-moderate in recent comparison | **Intellectual disability (HP:0001249)**; moderate ID **HP:0002342** where supported individually |
| Developmental delay | Reported at syndrome-comparison level, not quantified in the foundational family | **Global developmental delay (HP:0001263)** |
| Epilepsy/seizures | Reported as possible in APMR1 comparison; individual frequencies unavailable | **Seizure (HP:0001250)** / **Epilepsy (HP:0001250 family of terms)** |

### Quality of life

No EQ-5D, SF-36, PROMIS, caregiver-burden, educational-attainment, or adaptive-function data exist in the retrieved literature. Intellectual disability is expected to affect learning and independent function; alopecia may affect appearance and psychosocial well-being, but APMR1-specific quantitative effects have not been measured.

## 4. Genetic and molecular information

### Gene and variant annotation

* **Gene:** **AHSG** (alpha-2-HS-glycoprotein), encoding secreted fetuin-A.
* **Variant:** **c.950G>A (p.Arg317His)**; exon 7; **rs201849460**; reported genomic coordinate chr3:186338565 in the source assembly.
* **Variant class:** missense, germline, homozygous in affected relatives.
* **Population frequency:** ExAC MAF 0.0008% in the 2017 report; current gnomAD frequency and ancestry-specific counts require direct contemporary database verification.
* **ClinVar/ACMG status:** no current ClinVar assertion was established from retrieved evidence. “Pathogenic” should not be imported solely from prediction scores; a contemporary ACMG/AMP assessment should incorporate segregation, rarity, phenotype specificity, functional data, and any newer submissions.
* **Functional direction:** probably altered protein maturation/post-translational regulation rather than complete null function. The exact mechanism—loss of function, hypomorph, neomorph, or altered phosphorylation—remains unresolved. (sailani2017associationofahsg pages 4-7, sailani2017associationofahsg pages 1-3, sailani2017associationofahsg pages 3-4)

No APMR1-associated copy-number variant, translocation, repeat expansion, mitochondrial variant, modifier gene, methylation signature, or other epigenetic abnormality has been reported.

## 5. Environmental information

No toxins, radiation, pollution, occupation, diet, smoking, alcohol, physical activity, medication, or infectious agent has been causally associated with APMR1. Because the disorder segregates as a rare Mendelian trait, environmental exposure is not considered the primary cause. Environmental influences on hair retention, seizures, cognition, or AHSG biology have not been tested specifically in affected people.

## 6. Mechanism and pathophysiology

### Normal protein biology

Fetuin-A is an approximately **52-kDa**, negatively charged, secreted glycoprotein produced principally by hepatocytes. It is also produced by osteocytes and, to a lesser extent, osteoblasts. It binds calcium phosphate, forms soluble protein–mineral complexes, and inhibits ectopic calcification. Fetuin-A can mimic a TGF-β type-II receptor and antagonize TGF-β/BMP-family ligands, with reported binding to TGF-β1/2 and BMP-2, BMP-4, and BMP-6. (merdlerrabinowicz2019fetuinadeficiencyis pages 3-4, merdlerrabinowicz2019fetuinadeficiencyis pages 5-5)

Relevant to APMR1, AHSG is strongly expressed during development: the protein has high fetal plasma and CSF concentrations, is synthesized by early developing neurons in immature neocortex, and is expressed in developing hair follicles where basal keratinocytes reorganize into follicular placodes. The 2017 work also reported promotion of primary keratinocyte migration and greater expression in fetal than postnatal skin. These observations provide biological plausibility for combined hair and neurodevelopmental phenotypes. (sailani2017associationofahsg pages 7-8, sailani2017associationofahsg pages 8-9)

### Proposed causal chain

1. **Upstream genetic event:** homozygous AHSG p.Arg317His.
2. **Molecular consequence:** disruption of a recognition motif near Thr319; computational analyses predicted altered PKA/DMPK/AUR-family kinase recognition, with reported probabilities around 0.74–0.96.
3. **Protein consequence:** altered maturation or post-translational modification. Patient-serum Western blot showed two AHSG bands in affected people versus a single band in unaffected controls.
4. **Cellular/tissue consequences, still hypothetical:** disturbed fetuin-A signaling or extracellular availability may impair keratinocyte migration/hair-follicle placode development and alter developmental BMP/TGF-β regulation in the immature neocortex.
5. **Clinical outcome:** alopecia plus intellectual/developmental impairment, with possible epilepsy. (sailani2017associationofahsg pages 4-7, sailani2017associationofahsg pages 3-4)

Steps 1 and segregation are human genetic observations; step 3 is human biochemical evidence; the links from altered bands/phosphorylation to follicular and neural dysfunction remain mechanistic hypotheses rather than demonstrated causal experiments.

### Suggested ontology annotations

* **GO biological processes:** protein phosphorylation (**GO:0006468**), protein processing (**GO:0016485**), BMP signaling pathway (**GO:0030509**), TGF-β receptor signaling (**GO:0007179**), keratinocyte migration, hair-follicle development (**GO:0001942**), nervous-system development (**GO:0007399**), biomineralization (**GO:0110148**).
* **GO cellular components:** extracellular region (**GO:0005576**), extracellular space (**GO:0005615**), blood microparticle/serum-associated compartment where appropriate.
* **Cell Ontology candidates:** hepatocyte (**CL:0000182**), keratinocyte (**CL:0000312**), neuron (**CL:0000540**), osteocyte (**CL:0000137**), osteoblast (**CL:0000062**). Hair-follicle placode/basal keratinocyte terms should be checked against the current CL release.

### Immune, metabolic, and omics evidence

There is no demonstrated autoimmune alopecia, immunodeficiency, chronic inflammation, specific metabolomic signature, lipidomic profile, transcriptomic signature, proteomic panel, single-cell dataset, spatial-transcriptomic study, multi-omics integration, or CRISPR/RNAi screen for APMR1. Fetuin-A’s mineral metabolism functions are established generally, but no mineral or skeletal abnormality was quantified in the APMR1 family.

## 7. Anatomical structures affected

The directly observed organ systems are:

* **Integumentary:** scalp hair follicles; eyebrows and eyelashes. Suggested UBERON terms include **hair follicle (UBERON:0002073)**, scalp, eyebrow, and eyelash structures after current-release verification.
* **Nervous system:** developmental brain/cognitive function; the neocortex is biologically plausible from fetal AHSG localization, but no APMR1-specific neuropathology or imaging lesion was established. Suggested terms: brain (**UBERON:0000955**) and cerebral cortex (**UBERON:0000956**).
* **Cell/tissue:** follicular keratinocytes and developing neurons are candidate affected populations.
* **Subcellular level:** the evidence points to a secreted extracellular protein and altered post-translational processing; no disease-specific organelle lesion is known. (sailani2017associationofahsg pages 7-8, sailani2017associationofahsg pages 8-9)

Alopecia is not described as unilateral; involvement appears generalized/bilateral. Formal lateralization data are absent.

## 8. Temporal development

Affected children were documented as young as age 3, supporting early childhood expression. The disease is frequently described within the broader APMR family as congenital or early-onset alopecia, but exact onset dates were not available for the APMR1 relatives. Intellectual impairment is developmental rather than an adult neurodegenerative presentation. (sailani2017associationofahsg pages 3-4)

No validated disease stages, progression rate, remission pattern, critical therapeutic window, or longitudinal natural-history series exists. Persistence into ages 21–24 indicates a chronic/lifelong phenotype, but whether partial alopecia predictably progresses to complete alopecia is unproven.

## 9. Inheritance and population

* **Inheritance:** autosomal recessive.
* **Pedigree:** consanguineous Iranian family.
* **Observed sex distribution:** 4 male and 3 female affected relatives, consistent with an autosomal condition but too small for a meaningful sex ratio.
* **Penetrance:** appeared complete among seven homozygotes in this family; population-level penetrance is unknown.
* **Expressivity:** variable alopecia severity—3/7 complete and 4/7 partial—despite the same familial genotype.
* **Anticipation:** not reported and not mechanistically expected for a missense allele.
* **Germline mosaicism:** not reported.
* **Founder effect:** not established beyond one consanguineous kindred.
* **Carrier frequency:** unknown.
* **Prevalence/incidence:** no reliable cases-per-100,000 estimate. The evidence base of one molecularly resolved family implies an ultra-rare disorder but does not permit a numerical prevalence calculation. (sailani2017associationofahsg pages 1-3, sailani2017associationofahsg pages 3-4)

## 10. Diagnostics

### Recommended practical workflow

1. **Clinical assessment:** document distribution and onset of scalp/eyebrow/eyelash alopecia; complete dermatologic and hair-shaft examination; developmental, neurologic, seizure, hearing, vision, growth, and dysmorphology assessment.
2. **Phenotyping:** standardized cognitive/developmental testing and three-generation pedigree, including consanguinity.
3. **Genomic testing:** a neurodevelopmental-disorder/alopecia panel that includes **AHSG**, or preferably trio/parent–child **WES** because of extensive differential diagnosis. Confirm candidate variants by Sanger sequencing and segregation analysis.
4. **If sequencing is negative:** CNV-aware exome analysis or genome sequencing; CMA is appropriate when syndromic intellectual disability suggests a chromosomal imbalance. Karyotype/FISH are not first-line for this single-nucleotide disorder unless cytogenetic findings are suspected.
5. **Variant interpretation:** verify transcript, phase, population frequency in current gnomAD, ClinVar assertions, and phenotype concordance. Functional serum fetuin-A electrophoresis is research-level, not a validated clinical diagnostic assay. (sailani2017associationofahsg pages 1-3, sailani2017associationofahsg pages 3-4)

No validated blood biomarker, enzyme assay, imaging pattern, EEG signature, biopsy criterion, prenatal ultrasound sign, or formal diagnostic score exists.

### Differential diagnosis

Important genetic alternatives include **APMR2**, **APMR3**, and **LSS-related APMR4**; IFAP/BRESHECK syndrome; Menkes disease; Woodhouse–Sakati syndrome; Coffin–Siris spectrum; ectodermal dysplasias; and other syndromic alopecias/neurodevelopmental disorders. APMR4 can include congenital alopecia, variable ID, developmental delay, and epilepsy and is caused by biallelic **LSS** variants. Recent comparison reports mild-to-moderate ID in APMR1/2, severe ID in APMR3, and mild-to-severe ID in APMR4. (kang2024clinicalandgenetic pages 1-2)

Molecular testing is particularly important because phenotype overlap is substantial. In a broader 64-person ichthyosis cohort—not an APMR1 cohort—NGS identified pathogenic variants in 53 patients (**82.8%**), illustrating the diagnostic value of broad sequencing but not an APMR1-specific sensitivity. 

### Screening

No population or newborn screening is indicated. Once a familial pathogenic/likely pathogenic genotype is confirmed, targeted **cascade carrier testing**, prenatal diagnosis, and preimplantation genetic testing are technically feasible. These require genetic counseling and careful acknowledgment that the AHSG–APMR1 relationship has limited independent replication.

## 11. Outcome and prognosis

No survival curves, mortality rate, life-expectancy estimate, hospitalization rate, or prognostic biomarker has been published. Survival into the mid-20s was documented in the family, and there is no evidence that alopecia itself is life limiting. The principal known morbidity is neurodevelopmental disability, with potential seizure-related morbidity where epilepsy occurs. (sailani2017associationofahsg pages 3-4)

Recovery of established intellectual disability or spontaneous durable hair regrowth has not been documented. No quantitative adaptive-function or quality-of-life outcome is available. Prognostic correlations with alopecia extent, IQ, serum fetuin-A, or genotype are unknown.

## 12. Treatment and real-world implementation

There is **no approved disease-modifying pharmacotherapy**, gene therapy, RNA therapy, cell therapy, surgery, or genotype-guided drug regimen for APMR1. No relevant interventional trial was retrieved from ClinicalTrials.gov searches.

Current real-world management is therefore individualized and supportive:

* early developmental intervention and special education;
* speech/language, occupational, and physical therapy according to functional need;
* neurology assessment and standard antiseizure treatment if epilepsy is confirmed;
* dermatology evaluation, scalp care, cosmetic camouflage, wigs/prostheses, and psychological support;
* periodic hearing, vision, growth, nutrition, and behavioral assessment based on clinical findings;
* genetic counseling and family cascade testing.

Suggested NCIt intervention concepts include **Genetic Counseling**, **Occupational Therapy**, **Physical Therapy**, **Speech and Language Therapy**, **Supportive Care**, and **Anticonvulsant Therapy**; exact NCIt codes should be resolved against the current thesaurus. There are no APMR1-specific response rates, adverse-event datasets, pharmacogenomic recommendations, or treatment algorithms.

## 13. Prevention

The phenotype cannot currently be prevented after an affected genotype is established. Primary prevention is reproductive rather than environmental: carrier identification in the family, informed partner testing, prenatal diagnosis, or preimplantation genetic testing. Secondary prevention consists of early recognition of developmental delay or seizures and prompt intervention. Tertiary prevention includes educational/rehabilitative services, seizure control, psychosocial support, and surveillance tailored to identified complications.

Vaccination, infection prophylaxis, diet, exercise, toxin avoidance, or public-health environmental measures have no disease-specific preventive role beyond standard care.

## 14. Other species and natural disease

No naturally occurring veterinary counterpart of AHSG-associated APMR1 was identified; no breed association, zoonotic transmission, or cross-species infectious susceptibility applies. AHSG/fetuin-A is evolutionarily conserved, permitting comparative functional study, but conservation alone does not establish an animal disease homolog.

A separate human phenotype—infantile cortical hyperostosis—has been associated with a homozygous AHSG nonsense allele and complete fetuin-A deficiency. This demonstrates allelic/functional relevance of AHSG but should **not** be merged with APMR1 because its reported phenotype and molecular consequence differ. (merdlerrabinowicz2019fetuinadeficiencyis pages 3-4, merdlerrabinowicz2019fetuinadeficiencyis pages 4-5)

## 15. Model organisms

### Available evidence

**Ahsg-null mice** are an indirect mechanistic model, not a validated APMR1 model. Reported phenotypes include severe extra-osseous renal calcification, accelerated growth-plate mineralization, increased femoral cortical thickness, a greater than twofold increase in cortical-to-cancellous bone ratio, immature bone islands, growth-plate defects, and shortened proximal limb bones. These findings support fetuin-A’s role in mineral chaperoning and BMP/TGF-β-regulated osteogenesis but do not reproduce the defining human alopecia–intellectual-disability combination. (merdlerrabinowicz2019fetuinadeficiencyis pages 3-4, merdlerrabinowicz2019fetuinadeficiencyis pages 5-5)

No p.Arg317His knock-in mouse, zebrafish, Drosophila, *C. elegans*, patient-derived iPSC, neural organoid, hair-follicle organoid, or humanized model was identified. The most informative future model would be a homozygous p.Arg317His knock-in system coupled with fetal cortical-neuron and hair-follicle-placode assays; key readouts should include fetuin-A processing/phosphorylation, secretion, BMP/TGF-β signaling, keratinocyte migration, folliculogenesis, neurodevelopment, cognition, and seizure susceptibility.

## Expert assessment and research priorities

The strongest evidence is the internally consistent combination of linkage, homozygosity, rarity, segregation in 14 relatives, evolutionary conservation, and altered patient-protein electrophoretic behavior. Nevertheless, the absence of unrelated replicated families and direct variant-specific disease models limits certainty. The altered Western-blot migration shows a biochemical effect but does not prove that loss of Thr319 phosphorylation causes alopecia or intellectual disability. (sailani2017associationofahsg pages 4-7, sailani2017associationofahsg pages 3-4)

Priorities are: (1) identify independent biallelic AHSG cases through GeneMatcher/rare-disease genome programs; (2) perform formal ClinGen gene–disease curation; (3) measure secretion, glycosylation, phosphorylation, BMP/TGF-β antagonism, and migration in variant-engineered keratinocytes and neurons; (4) develop knock-in or patient-derived organoid models; and (5) establish prospective natural-history and patient-reported-outcome data.

## Source and quotation note

The key primary report is Sailani et al., published January 2017: [https://doi.org/10.1007/s00439-016-1756-5](https://doi.org/10.1007/s00439-016-1756-5). The recent comparative source is Kang et al., published May 2024: [https://doi.org/10.3389/fnins.2024.1301865](https://doi.org/10.3389/fnins.2024.1301865). The indirect fetuin-A-deficiency/model source is Merdler-Rabinowicz et al., published July 2019: [https://doi.org/10.1038/s41390-019-0499-0](https://doi.org/10.1038/s41390-019-0499-0). (sailani2017associationofahsg pages 1-3, kang2024clinicalandgenetic pages 1-2, merdlerrabinowicz2019fetuinadeficiencyis pages 3-4)

A verbatim abstract for the foundational APMR1 article was not present in the retrieved full-text evidence. To avoid fabricating quotations, its findings have been accurately paraphrased rather than placed in quotation marks. The available 2024 abstract describes APMR disorders as involving congenital alopecia and variable intellectual disability, but that article concerns APMR4 and should not be used as direct evidence for AHSG causality. (kang2024clinicalandgenetic pages 1-2)

References

1. (sailani2017associationofahsg pages 4-7): M. Reza Sailani, Fereshteh Jahanbani, Jafar Nasiri, Mahdiyeh Behnam, Mansoor Salehi, Maryam Sedghi, Majid Hoseinzadeh, Shinichi Takahashi, Amin Zia, Joshua Gruber, Janet Linnea Lynch, Daniel Lam, Juliane Winkelmann, Semira Amirkiai, Baoxu Pang, Shannon Rego, Safoura Mazroui, Jonathan A. Bernstein, and Michael P. Snyder. Association of ahsg with alopecia and mental retardation (apmr) syndrome. Human Genetics, 136:287-296, Jan 2017. URL: https://doi.org/10.1007/s00439-016-1756-5, doi:10.1007/s00439-016-1756-5. This article has 16 citations and is from a peer-reviewed journal.

2. (sailani2017associationofahsg pages 1-3): M. Reza Sailani, Fereshteh Jahanbani, Jafar Nasiri, Mahdiyeh Behnam, Mansoor Salehi, Maryam Sedghi, Majid Hoseinzadeh, Shinichi Takahashi, Amin Zia, Joshua Gruber, Janet Linnea Lynch, Daniel Lam, Juliane Winkelmann, Semira Amirkiai, Baoxu Pang, Shannon Rego, Safoura Mazroui, Jonathan A. Bernstein, and Michael P. Snyder. Association of ahsg with alopecia and mental retardation (apmr) syndrome. Human Genetics, 136:287-296, Jan 2017. URL: https://doi.org/10.1007/s00439-016-1756-5, doi:10.1007/s00439-016-1756-5. This article has 16 citations and is from a peer-reviewed journal.

3. (sailani2017associationofahsg pages 3-4): M. Reza Sailani, Fereshteh Jahanbani, Jafar Nasiri, Mahdiyeh Behnam, Mansoor Salehi, Maryam Sedghi, Majid Hoseinzadeh, Shinichi Takahashi, Amin Zia, Joshua Gruber, Janet Linnea Lynch, Daniel Lam, Juliane Winkelmann, Semira Amirkiai, Baoxu Pang, Shannon Rego, Safoura Mazroui, Jonathan A. Bernstein, and Michael P. Snyder. Association of ahsg with alopecia and mental retardation (apmr) syndrome. Human Genetics, 136:287-296, Jan 2017. URL: https://doi.org/10.1007/s00439-016-1756-5, doi:10.1007/s00439-016-1756-5. This article has 16 citations and is from a peer-reviewed journal.

4. (kang2024clinicalandgenetic pages 1-2): Qingyun Kang, Hui Kang, Jingwen Tang, Miao Wang, Haojiang Jiang, Ze-shu Ning, and Liwen Wu. Clinical and genetic analyses of apmr4 syndrome caused by novel biallelic lss variants. Frontiers in Neuroscience, May 2024. URL: https://doi.org/10.3389/fnins.2024.1301865, doi:10.3389/fnins.2024.1301865. This article has 3 citations and is from a peer-reviewed journal.

5. (sailani2017associationofahsg pages 7-8): M. Reza Sailani, Fereshteh Jahanbani, Jafar Nasiri, Mahdiyeh Behnam, Mansoor Salehi, Maryam Sedghi, Majid Hoseinzadeh, Shinichi Takahashi, Amin Zia, Joshua Gruber, Janet Linnea Lynch, Daniel Lam, Juliane Winkelmann, Semira Amirkiai, Baoxu Pang, Shannon Rego, Safoura Mazroui, Jonathan A. Bernstein, and Michael P. Snyder. Association of ahsg with alopecia and mental retardation (apmr) syndrome. Human Genetics, 136:287-296, Jan 2017. URL: https://doi.org/10.1007/s00439-016-1756-5, doi:10.1007/s00439-016-1756-5. This article has 16 citations and is from a peer-reviewed journal.

6. (sailani2017associationofahsg pages 8-9): M. Reza Sailani, Fereshteh Jahanbani, Jafar Nasiri, Mahdiyeh Behnam, Mansoor Salehi, Maryam Sedghi, Majid Hoseinzadeh, Shinichi Takahashi, Amin Zia, Joshua Gruber, Janet Linnea Lynch, Daniel Lam, Juliane Winkelmann, Semira Amirkiai, Baoxu Pang, Shannon Rego, Safoura Mazroui, Jonathan A. Bernstein, and Michael P. Snyder. Association of ahsg with alopecia and mental retardation (apmr) syndrome. Human Genetics, 136:287-296, Jan 2017. URL: https://doi.org/10.1007/s00439-016-1756-5, doi:10.1007/s00439-016-1756-5. This article has 16 citations and is from a peer-reviewed journal.

7. (merdlerrabinowicz2019fetuinadeficiencyis pages 3-4): Rona Merdler-Rabinowicz, Anna Grinberg, Jeffrey M. Jacobson, Ido Somekh, Christoph Klein, Atar Lev, Salama Ihsan, Adib Habib, Raz Somech, and Amos J. Simon. Fetuin-a deficiency is associated with infantile cortical hyperostosis (caffey disease). Pediatric Research, 86:603-607, Jul 2019. URL: https://doi.org/10.1038/s41390-019-0499-0, doi:10.1038/s41390-019-0499-0. This article has 21 citations and is from a domain leading peer-reviewed journal.

8. (merdlerrabinowicz2019fetuinadeficiencyis pages 4-5): Rona Merdler-Rabinowicz, Anna Grinberg, Jeffrey M. Jacobson, Ido Somekh, Christoph Klein, Atar Lev, Salama Ihsan, Adib Habib, Raz Somech, and Amos J. Simon. Fetuin-a deficiency is associated with infantile cortical hyperostosis (caffey disease). Pediatric Research, 86:603-607, Jul 2019. URL: https://doi.org/10.1038/s41390-019-0499-0, doi:10.1038/s41390-019-0499-0. This article has 21 citations and is from a domain leading peer-reviewed journal.

9. (merdlerrabinowicz2019fetuinadeficiencyis pages 5-5): Rona Merdler-Rabinowicz, Anna Grinberg, Jeffrey M. Jacobson, Ido Somekh, Christoph Klein, Atar Lev, Salama Ihsan, Adib Habib, Raz Somech, and Amos J. Simon. Fetuin-a deficiency is associated with infantile cortical hyperostosis (caffey disease). Pediatric Research, 86:603-607, Jul 2019. URL: https://doi.org/10.1038/s41390-019-0499-0, doi:10.1038/s41390-019-0499-0. This article has 21 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Alopecia-Intellectual_Disability_Syndrome_1-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 6 |
| Resolved | 3 |
| Unresolved (possible confabulation) | 3 |
| Unverifiable | 0 |
| References weighed for topical relevance | 3 |
| On topic | 1 |
| Off topic | 0 |

### Unresolved references

These identifiers did not resolve to a record and may be fabricated. A lookup that failed for transport reasons is indistinguishable from one that failed because the record does not exist, so spot-check before acting on them:

- `DOI:10.1007/s00439-016-1756-5](https://doi.org/10.1007/s00439-016-1756-5` (2 mentions) - Identifier did not resolve to a record
- `DOI:10.3389/fnins.2024.1301865](https://doi.org/10.3389/fnins.2024.1301865` (2 mentions) - Identifier did not resolve to a record
- `DOI:10.1038/s41390-019-0499-0](https://doi.org/10.1038/s41390-019-0499-0` (2 mentions) - Identifier did not resolve to a record