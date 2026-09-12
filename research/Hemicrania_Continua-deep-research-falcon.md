---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-16T20:28:00.141885'
end_time: '2026-08-16T20:36:43.605982'
duration_seconds: 523.46
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Hemicrania Continua
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 12
reference_validation:
  total_references: 7
  verified: 7
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Hemicrania_Continua-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Hemicrania Continua
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Hemicrania Continua** covering all of the
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
- **Disease Name:** Hemicrania Continua
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Hemicrania Continua** covering all of the
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


# Hemicrania Continua: Disease-Characteristics Research Report

## Executive summary

Hemicrania continua (HC) is an uncommon primary headache disorder characterized by continuous, strictly unilateral headache, superimposed exacerbations, and ipsilateral cranial autonomic symptoms and/or agitation during exacerbations. An absolute therapeutic response to indomethacin is part of the International Classification of Headache Disorders, third edition (ICHD-3) case definition. HC belongs to the trigeminal autonomic cephalalgia (TAC) group, although migrainous symptoms are frequent.

The evidence base is small. Most data come from specialist-clinic cohorts, case series, functional imaging studies, and expert reviews rather than population cohorts or randomized trials. No causal gene, validated molecular biomarker, disease-specific omics signature, or accepted animal model has been established. The most important recent clinical development is recognition that structural disorders can closely mimic HC, supporting brain MRI—with contrast and targeted vascular or pituitary imaging when indicated—before labeling a case primary. Experimental treatment development remains difficult: a Phase 2 erenumab study enrolled only two participants and was terminated for recruitment difficulty (NCT04303845 chunk 1).

| Domain | Established finding | Evidence strength/type | Suggested ontology terms |
|---|---|---|---|
| Definition / phenotype | Hemicrania continua is a primary headache disorder characterized by persistent strictly unilateral head pain with superimposed exacerbations and cranial autonomic features; it is classically defined by complete response to indomethacin. The broader headache review notes HC is “more complex” but retains the “rapid and absolute response to indomethacin in almost all cases” property within indomethacin-responsive headaches (lane2024primaryheadachesare pages 7-9, lane2024primaryheadachesare pages 9-11). | Established clinical classification; review-level synthesis; disease-defining therapeutic response | headache; unilateral headache; lacrimation; conjunctival injection; ptosis; miosis; photophobia; phonophobia; nausea |
| Anatomy | Primary structures implicated are the trigeminal system and trigeminocervical complex, with involvement of brainstem and sometimes hypothalamic regions in functional imaging models of TAC-like disorders; disease localizes to the nervous system and is typically unilateral (lane2024primaryheadachesare pages 9-11, lane2024primaryheadachesare pages 11-12). | Established systems-neuroscience model; indirect for HC-specific localization | trigeminal nerve; trigeminocervical complex; brainstem; hypothalamus; nervous system |
| Mechanism / pathophysiology | Best-supported model is network dysfunction involving trigeminal nociceptive afferents and cranial parasympathetic outflow. The review states nociceptive inputs from cranial and upper cervical structures converge in the TCC, which is “fundamental to transmission” of head/neck nociceptive information (lane2024primaryheadachesare pages 9-11, lane2024primaryheadachesare pages 11-12). | Moderate evidence; human neuroanatomical/pathophysiologic inference rather than molecular proof | trigeminal autonomic reflex; trigeminocervical complex; parasympathetic nervous system; brainstem |
| Genetics / molecular / omics gaps | No validated causal gene, inheritance pattern, pathogenic variant, disease-specific biomarker, or established transcriptomic/proteomic/metabolomic signature was identified from the available evidence. | Evidence gap / negative finding | no established causal gene; no established biomarker |
| Diagnostics | Diagnosis is clinical, anchored to ICHD-3 phenotype plus confirmation of complete indomethacin responsiveness; neuroimaging is important to exclude secondary mimics because structural lesions can present as HC-like syndromes. | Strong clinical consensus; supportive review-level evidence | headache disorder diagnosis; magnetic resonance imaging; differential diagnosis; indomethacin test |
| First-line treatment | Indomethacin is the defining and first-line therapy; complete response is central to diagnosis. The recent review explicitly highlights “rapid and absolute response to indomethacin in almost all cases” (lane2024primaryheadachesare pages 7-9). | Strongest treatment evidence; long-standing clinical standard | indomethacin; nonsteroidal anti-inflammatory drug |
| Alternatives / refractory disease | When indomethacin is not tolerated, evidence for alternatives is limited and lower quality; reported options include melatonin, topiramate, gabapentin, COX-2 inhibitors, nerve blocks, botulinum toxin, vagus nerve stimulation, and occipital nerve stimulation. | Low-quality evidence; case series/refractory-care practice | melatonin; topiramate; gabapentin; occipital nerve stimulation; vagus nerve stimulation; botulinum toxin |
| Epidemiology | HC is uncommon/rare in practice; current estimates are mainly from clinic-based studies rather than population-based surveillance, so prevalence is uncertain and likely under-recognized. | Limited epidemiology; clinic-based meta-analytic literature exists but population certainty is low | rare disease; headache disorder epidemiology |
| Prognosis | Disorder is usually chronic but treatment-responsive when true HC is present; major morbidity is pain burden, disability, and medication toxicity from long-term indomethacin rather than mortality. | Moderate clinical experience; limited longitudinal natural-history data | chronic pain; disability; adverse drug effect |
| Clinical trials | Registered interventional trial NCT04303845 evaluated erenumab 140 mg for HC, Phase 2, but was terminated after enrolling 2 participants; eligibility required ≥12 months of unremitting HC by ICHD-3 and prior/current complete indomethacin response (NCT04303845 chunk 1). | Direct registry evidence | NCT04303845; erenumab; monoclonal antibody therapy |
| Real-world implementation / registry | NCT01842763 is an active-not-recruiting French observational database of occipital nerve stimulation in refractory chronic headache disorders including HC; planned data include efficacy, safety, and potential predictors of response, with total enrollment 246 across headache subtypes (NCT01842763 chunk 1, NCT01842763 chunk 2). | Direct registry evidence; mixed-disorder observational dataset | NCT01842763; occipital nerve stimulation; patient registry |
| Animal / model systems | No validated naturally occurring animal disease, species-specific model, or HC-specific genetic/cellular model was identified in the available evidence. | Evidence gap / negative finding | no established animal model; no established cellular model |


*Table: This compact table summarizes the most actionable disease-knowledge-base facts for hemicrania continua, emphasizing what is established versus where evidence is absent. It is useful for rapid curation of phenotype, mechanism, diagnosis, treatment, and trial annotations.*

## 1. Disease information

### Definition and classification

HC is a persistent unilateral headache syndrome first described by Sjaastad and Spierings in 1984. The ICHD-3 definition requires:

1. Unilateral headache present for more than three months, with exacerbations of moderate or greater intensity.
2. During exacerbations, at least one ipsilateral cranial autonomic feature—conjunctival injection or lacrimation, nasal congestion or rhinorrhea, eyelid edema, forehead/facial sweating, miosis or ptosis—or restlessness/agitation or aggravation by movement.
3. An absolute response to therapeutic doses of indomethacin.
4. No better alternative diagnosis.

ICHD-3 recognizes **remitting HC**, with spontaneous remissions lasting at least 24 hours, and **unremitting HC**, which is continuously present for at least one year without a remission of 24 hours or longer. Contemporary headache literature continues to emphasize the disorder’s rapid and essentially absolute indomethacin response (lane2024primaryheadachesare pages 7-9).

### Identifiers and synonyms

- **Preferred name:** Hemicrania continua
- **Synonyms:** continuous hemicrania; HC; chronic continuous unilateral headache responsive to indomethacin
- **MeSH:** *Hemicrania Continua*; broader hierarchy includes Headache Disorders/Brain Diseases.
- **ICD-10-CM:** G44.51, Hemicrania continua.
- **ICD-11:** classified among trigeminal autonomic cephalalgias; local implementations should verify the current extension code rather than mapping solely from ICD-10-CM.
- **Orphanet:** ORPHA:157835 is commonly used for hemicrania continua.
- **MONDO:** a dedicated MONDO concept exists in current ontology releases, but the exact release-specific identifier should be verified during ingestion rather than inferred from name matching.
- **OMIM:** no established Mendelian disease entry or phenotype-gene relationship.

These are aggregated disease-level classifications, not individual EHR observations. Clinical records constitute patient-level evidence only when documenting laterality, duration, autonomic manifestations, exclusionary investigations, and indomethacin response.

## 2. Etiology, risk, and protective factors

### Primary and secondary HC

**Primary HC** has no established external or genetic cause. **Secondary HC-like headache** can accompany pituitary lesions, intracranial tumors, vascular lesions or dissection, venous thrombosis, inflammatory orbital disease, infection, trauma, cervical pathology, and other structural disorders. A clinically perfect indomethacin response does not by itself exclude a secondary cause.

No reproducible causal variant, susceptibility locus, modifier gene, family-based inheritance pattern, founder effect, or gene–environment interaction has been established. Consequently, penetrance, carrier frequency, anticipation, germline mosaicism, and consanguinity are not applicable disease characteristics at present.

Reported temporal associations include head or neck trauma, surgery, and occasionally infection, but these are case-level triggers rather than validated population risk factors. Adult onset is usual, but pediatric and late-life onset occur. Women appear somewhat more frequently represented in many series, although HC lacks the striking female predominance originally presumed. No ethnicity, occupation, toxin, smoking pattern, diet, alcohol exposure, or infectious agent has been shown to alter incidence.

### Protective factors

No validated genetic or environmental protective factor exists. Avoiding an individual patient’s exacerbation triggers may reduce symptom burden but is not primary prevention. Indomethacin prevents pain while taken; it does not establish that the underlying tendency has been removed.

## 3. Phenotypes

The defining phenotype is a continuous side-locked headache, commonly temporal, orbital, supraorbital, frontal, or hemicranial, with exacerbations lasting minutes to days. Pain may extend to the occiput, neck, face, oral cavity, or shoulder. A prospective headache-clinic study cited in a 2024 synthesis found facial pain in 21% of HC cases, demonstrating that pain is not necessarily confined to the orbital or temporal region (lane2024primaryheadachesare pages 9-11).

| Phenotype | Character and course | Suggested HPO annotation |
|---|---|---|
| Continuous headache | Daily and continuous for >3 months; background often mild–moderate, exacerbations moderate–severe | Headache; Chronic daily headache |
| Strict unilateral localization | Usually side-locked; side-shifting is exceptional and should prompt reassessment | Unilateral headache |
| Lacrimation/conjunctival injection | Ipsilateral during exacerbations; variable frequency | Increased lacrimation; Conjunctival injection |
| Nasal congestion/rhinorrhea | Ipsilateral autonomic activation | Nasal congestion; Rhinorrhea |
| Ptosis/miosis/eyelid edema | Partial Horner-like or eyelid manifestations during exacerbations | Ptosis; Miosis; Periorbital edema |
| Restlessness/agitation | May occur during severe exacerbations; movement can worsen pain | Agitation |
| Photophobia/phonophobia | Common migrainous accompaniments, often unilateral or maximal ipsilateral to pain | Photophobia; Phonophobia |
| Nausea/vomiting | May accompany severe exacerbations | Nausea; Vomiting |
| Allodynia/tenderness | Cranial or cervical in some patients | Allodynia; Hyperalgesia |
| Sleep disturbance, anxiety, impaired concentration | Downstream effects of persistent pain; not diagnostic | Insomnia; Anxiety; Impaired concentration |

There is no characteristic blood, urine, CSF, endocrine, or histopathologic abnormality. Quality-of-life impairment arises from continuous pain, unpredictable severe exacerbations, sleep disruption, occupational and social disability, and adverse effects of long-term NSAID therapy. HC-specific EQ-5D, SF-36, or PROMIS reference norms remain poorly developed.

## 4. Genetic and molecular information

No causal gene, HGNC identifier, OMIM gene association, pathogenic or likely pathogenic variant, recurrent copy-number change, chromosomal abnormality, or recognized somatic mutation is established for HC. Accordingly, there are no disease-specific allele frequencies, ACMG classifications, loss-/gain-of-function mechanisms, modifier genes, or pharmacogenomic recommendations.

No reproducible HC-specific DNA-methylation, histone, chromatin, transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or multi-omic signature was identified. Routine WES, WGS, gene panels, CMA, karyotyping, FISH, mitochondrial sequencing, and repeat-expansion testing are therefore **not indicated for typical isolated HC**. Genetic testing should be driven by an alternative syndromic phenotype or family history.

## 5. Environmental and lifestyle information

HC is not a toxic, radiation-induced, occupational, nutritional, infectious, or communicable disease. Individual exacerbations may be provoked by physical activity, movement, alcohol, sleep disruption, stress, or other migraine-like triggers, but evidence is observational and inconsistent. There is no validated dose–response relationship and no specific pathogen. Secondary headache following trauma or a structural lesion should be coded as secondary rather than assumed to represent idiopathic HC.

## 6. Mechanism and pathophysiology

### Current systems-neuroscience model

The best-supported model is dysfunction of a distributed trigeminal–autonomic pain network rather than a single molecular defect:

1. Nociceptive afferents from cranial dura, trigeminal territories, and upper cervical roots converge in the **trigeminocervical complex (TCC)**.
2. Ascending pathways project to thalamic, brainstem, periaqueductal gray, and hypothalamic regions, generating persistent unilateral pain and altered descending pain control.
3. Trigeminal activation recruits the superior salivatory nucleus and facial-nerve parasympathetic pathways through the sphenopalatine ganglion, producing lacrimation, conjunctival injection, rhinorrhea, and congestion.
4. Sympathetic dysfunction can generate ptosis or miosis.
5. Superimposed network activation produces painful exacerbations and migrainous symptoms.

A recent neuroanatomical synthesis describes the TCC as fundamental to transmission of nociceptive information from the head and neck and notes its convergence of trigeminal, lower-cranial-nerve, and upper-cervical inputs (lane2024primaryheadachesare pages 9-11, lane2024primaryheadachesare pages 11-12). HC-specific PET studies have reported activation involving the contralateral posterior hypothalamus and ipsilateral dorsal rostral pons/ventrolateral midbrain during pain, with normalization after indomethacin. These findings are associative systems-level observations, not evidence that a single region is the initiating lesion.

### Molecular interpretation and limitations

Indomethacin inhibits cyclooxygenase-1 and -2 and prostaglandin synthesis, but ordinary NSAID potency does not explain HC’s uniquely complete response. Proposed actions include modulation of nitric-oxide signaling, cerebral blood flow, and trigeminovascular transmission. No specific receptor, ion channel, enzyme deficiency, protein misfolding, immune mechanism, metabolic defect, neurodegenerative process, or epigenetic lesion has been demonstrated.

Suggested terms include **GO:0007218 neuropeptide signaling pathway**, **GO:0007204 positive regulation of cytosolic calcium ion concentration**, **GO:0006954 inflammatory response** only as broad mechanistic hypotheses, and nociception/pain-perception terms as stronger annotations. Relevant cell labels include trigeminal sensory neuron, parasympathetic neuron, sympathetic neuron, thalamic neuron, hypothalamic neuron, and brainstem neuron. These cell assignments are anatomical inferences, not single-cell evidence.

## 7. Anatomical structures affected

HC is a functional disorder of the nervous system, not a destructive lesion of the painful scalp, orbit, or face.

- **Primary system:** central and peripheral nervous system.
- **Pain pathways:** trigeminal nerve, trigeminal ganglion, spinal trigeminal nucleus, TCC, upper cervical afferents, thalamus, periaqueductal gray, dorsal pons, and hypothalamus.
- **Autonomic pathway:** superior salivatory nucleus, facial nerve parasympathetic fibers, sphenopalatine ganglion, lacrimal and nasal targets; cervical sympathetic pathways.
- **Localization:** unilateral orbital, supraorbital, temporal, frontal, facial, parietal, or occipital pain; radiation into neck is possible.
- **Lateralization:** strict unilateral persistence is diagnostically central.

Suggested UBERON labels are brain, brainstem, pons, midbrain, hypothalamus, thalamus, trigeminal nerve, cervical spinal cord, eye region, face, and scalp. No disease-specific mitochondrion, nucleus, ER, lysosome, or other subcellular compartment is established.

## 8. Temporal development

Onset is usually in adulthood but ranges from childhood to advanced age. It may be abrupt—with the patient recalling the precise day—or insidious. HC can arise de novo as an unremitting disorder or evolve from a remitting pattern. Remissions may be spontaneous or treatment-associated; relapse commonly follows indomethacin withdrawal, sometimes rapidly.

HC is chronic but not known to be neurodegenerative or biologically progressive. There are no accepted early, intermediate, advanced, or end-stage categories. A marked change in pattern, new neurologic deficit, systemic symptom, onset after age 50, pregnancy/postpartum onset, or new Horner syndrome is a critical window for renewed secondary-cause evaluation.

## 9. Epidemiology, inheritance, and population

Population prevalence and incidence remain uncertain because few community-based studies exist and diagnosis requires an indomethacin trial. A 2023 systematic review and meta-analysis specifically evaluated clinic-based prevalence and clinical features, underscoring that available estimates are referral-based rather than general-population rates (Al-Khazali et al., *Cephalalgia*, published January 2023, DOI: https://doi.org/10.1177/03331024221131343).

Across headache-clinic studies, HC generally represents well below 1% to approximately 2% of referred patients, depending on case ascertainment and whether indomethacin response is required. These figures must not be interpreted as population prevalence per 100,000. Incidence per 100,000 person-years is unknown. Both sexes and all reported ethnic groups can be affected; clinic series commonly show a modest female predominance. There is no established geographic endemicity.

HC is sporadic and non-Mendelian based on current evidence. Penetrance, expressivity, carrier frequency, anticipation, founder effects, and prenatal or preimplantation testing are therefore not applicable.

## 10. Diagnostics

### Clinical diagnosis and indomethacin test

The practical diagnostic sequence is:

1. Confirm continuous baseline headache for more than three months.
2. Confirm fixed unilateral localization and exacerbations.
3. Document ipsilateral autonomic manifestations or movement-related agitation.
4. Record migrainous features without misclassifying the continuous baseline as chronic migraine.
5. Exclude structural and vascular causes.
6. Demonstrate complete response to an adequate indomethacin trial.

Oral indomethacin is often begun at 25 mg three times daily and increased every several days to 50 mg three times daily if necessary and medically safe. ICHD-3 notes that adults may initially require at least 150 mg/day and occasionally up to 225 mg/day; lower maintenance doses should be sought after response. Parenteral indomethacin—the historical “indotest”—can provide rapid confirmation where available.

A partial response, intolerance before reaching an adequate dose, poor adherence, or concurrent analgesic overuse does not establish ICHD-3 HC. Conversely, an apparently complete response should not override red flags or abnormal imaging.

### Imaging and other tests

Brain MRI with and without gadolinium is recommended at least once in a suspected new HC case. Imaging should scrutinize the pituitary/sellar region, cavernous sinus, orbit, posterior fossa, trigeminal pathway, and upper cervical region. MRA/CTA or venous imaging is added when dissection, aneurysm, fistula, reversible vasoconstriction, or venous thrombosis is plausible. Pituitary hormones, inflammatory markers, lumbar puncture, ophthalmologic examination, or cervical imaging are indication-driven rather than routine.

There is no diagnostic EEG, EMG, biopsy, histopathology, blood biomarker, CSF biomarker, liquid biopsy, or omics test.

### Differential diagnosis

- **Chronic migraine:** may be unilateral and autonomic, but is not usually continuously side-locked and does not respond absolutely to indomethacin.
- **New daily persistent headache:** abrupt remembered onset and continuous course; phenotype is usually migrainous or tension-type rather than indomethacin-defined.
- **Paroxysmal hemicrania:** short, frequent attacks with pain-free intervals rather than continuous baseline pain.
- **Cluster headache:** attacks lasting 15–180 minutes with attack-free intervals, often with circadian/bout periodicity.
- **SUNCT/SUNA:** seconds-to-minutes neuralgiform attacks.
- **Cervicogenic headache/occipital neuralgia:** cervical provocation, restricted movement, or neuralgiform occipital distribution.
- **Trigeminal neuralgia:** brief electric-shock pain in trigeminal distributions.
- **Medication-overuse headache:** usually bilateral or variable and linked to excessive acute medication.
- **Secondary mimics:** pituitary/cavernous-sinus disease, tumor, dissection, venous thrombosis, orbital inflammation, infection, and traumatic or cervical lesions.

There is no screening program for asymptomatic people, newborns, carriers, or relatives.

## 11. Outcome and prognosis

HC is painful and disabling but is not known to shorten life expectancy or cause disease-specific mortality. Five- and ten-year survival metrics are therefore not clinically relevant. When indomethacin is effective and tolerated, pain freedom and restoration of function can be dramatic. Without effective treatment, continuous pain can cause persistent disability, impaired sleep and employment, anxiety/depression, medication overuse, and repeated healthcare utilization.

Long-term morbidity often reflects treatment toxicity: dyspepsia, peptic ulceration or bleeding, renal impairment, fluid retention, hypertension, and cardiovascular risk. Prognosis depends more on accurate diagnosis, exclusion of a secondary lesion, and ability to sustain effective therapy than on age or a molecular biomarker. No validated prognostic biomarker or risk calculator exists.

## 12. Treatment

### Indomethacin

**First-line and diagnostic treatment:** indomethacin, a nonselective cyclooxygenase inhibitor. Complete response is expected in ICHD-defined disease. Use the lowest effective maintenance dose after control is obtained. Gastroprotection with a proton-pump inhibitor is commonly used when not contraindicated; monitor blood pressure, renal function, blood count where appropriate, gastrointestinal symptoms, edema, and cardiovascular risk.

Suggested annotations: CHEBI/DrugBank concept for indomethacin; NCIt concepts **Indomethacin**, **Cyclooxygenase Inhibitor**, and **Nonsteroidal Anti-inflammatory Drug**.

### Alternatives when indomethacin is contraindicated or intolerable

Evidence is chiefly case reports or small open-label series, and none is an equivalent diagnostic substitute:

- COX-2-selective inhibitors such as celecoxib—possible benefit but cardiovascular/renal risks.
- Topiramate or gabapentin—occasionally useful; monitor cognitive, metabolic, teratogenic, or sedating effects as relevant.
- Melatonin—may provide full or partial response or permit dose reduction in selected patients. A treatment-focused report was published in March 2024: Cheung, Oliveira, and Goadsby, *Cephalalgia*, DOI https://doi.org/10.1177/03331024231226196.
- OnabotulinumtoxinA—reported in small series, especially indomethacin-intolerant cases.
- Greater occipital, supraorbital, or trochlear-region blocks—variable and generally temporary benefit.
- Non-invasive vagus nerve stimulation—limited case-level evidence.
- Occipital nerve stimulation—reserved for highly refractory, specialist-confirmed disease because implantation carries infection, lead migration, revision, and hardware risks.

The French NCT01842763 database collects longitudinal efficacy, quality-of-life, technical, and safety information for occipital nerve stimulation in refractory headache disorders including HC. It is observational, active but not recruiting, and has 246 participants across multiple headache diagnoses; therefore, 246 must not be reported as the HC sample size or as proof of HC-specific efficacy (NCT01842763 chunk 1, NCT01842763 chunk 2).

### CGRP-targeted treatment and trials

NCT04303845 evaluated a single 140-mg subcutaneous dose of erenumab in unremitting HC previously or currently completely responsive to indomethacin. The Phase 2 study enrolled only two participants and was terminated because of recruitment difficulty; it cannot support an efficacy estimate (NCT04303845 chunk 1). No gene, cell, RNA, CRISPR, or disease-specific immunotherapy is indicated.

No CPIC or PharmGKB genotype-guided strategy exists for HC treatment.

## 13. Prevention

There is no established primary prevention because causal risk factors are unknown. Vaccination, environmental remediation, carrier screening, prenatal testing, or public-health screening has no HC-specific role.

Secondary prevention consists of prompt recognition, an adequate indomethacin trial, and appropriate imaging to avoid prolonged misdiagnosis or delayed identification of a structural mimic. Tertiary prevention includes maintaining the lowest effective dose, gastroprotection and toxicity monitoring, controlling medication overuse, treating sleep or mood comorbidity, and reassessing patients whose pattern changes. Lifestyle regularity and avoidance of reproducible personal triggers may reduce exacerbations but do not prevent disease onset.

## 14. Other species and natural disease

No naturally occurring veterinary counterpart meeting human HC criteria has been validated in dogs, cats, livestock, wildlife, or other species. There is no associated NCBI Taxon, VBO breed term, orthologous causal gene, cross-species susceptibility, transmission, or zoonotic potential. Human HC is neither infectious nor transmissible.

## 15. Model organisms and experimental systems

No disease-specific knockout, knock-in, transgenic, humanized, chemically induced, iPSC, organoid, or cellular HC model is established. General rodent trigeminovascular, dural stimulation, superior-salivatory-nucleus, and TCC models can investigate nociception or trigeminal–autonomic reflexes, but they do not reproduce the defining clinical combination of continuous unilateral pain and absolute indomethacin responsiveness. There are no HC-specific CRISPR/RNAi screens or validated single-cell reference datasets.

## Evidence appraisal and curation cautions

1. **Diagnostic evidence is strongest:** the characteristic phenotype plus absolute indomethacin response is established by international classification and repeated clinical observation.
2. **Epidemiologic certainty is low:** specialist-clinic proportions should not be converted into population prevalence or incidence.
3. **Mechanistic evidence is intermediate and associative:** functional imaging and neuroanatomy support trigeminal–autonomic, brainstem, and hypothalamic network involvement, but no initiating molecular lesion is known. The TCC’s anatomical convergence and ascending nociceptive role are well described, although much of this evidence applies across primary headache disorders rather than uniquely to HC (lane2024primaryheadachesare pages 9-11, lane2024primaryheadachesare pages 11-12).
4. **Alternative-treatment evidence is low:** most reports are uncontrolled and vulnerable to diagnostic heterogeneity, placebo effects, spontaneous remission, and publication bias.
5. **Trial evidence remains insufficient:** the erenumab trial’s two-person enrollment cannot establish response rates, while the occipital-stimulation registry combines several headache diagnoses (NCT04303845 chunk 1, NCT01842763 chunk 1).

## Selected authoritative references and exact source statements

- Lane R, Davies P. “Primary headaches are a continuum driven by a common process.” *Discover Medicine*. Published October 2024. DOI: https://doi.org/10.1007/s44337-024-00068-w. The review characterizes the TCC as “fundamental to transmission” of nociceptive information from head and neck structures and discusses the rapid, absolute indomethacin response associated with HC (lane2024primaryheadachesare pages 7-9, lane2024primaryheadachesare pages 11-12).
- Al-Khazali HM et al. “Prevalence and clinical features of hemicrania continua in clinic-based studies: a systematic review and meta-analysis.” *Cephalalgia*. Published January 2023. DOI: https://doi.org/10.1177/03331024221131343.
- Bahra A. “Paroxysmal hemicrania and hemicrania continua: review on pathophysiology, clinical features and treatment.” *Cephalalgia*. Published November 2023. DOI: https://doi.org/10.1177/03331024231214239.
- Yildiz Goksel H et al. “The critical role of neuroimaging in hemicrania continua: a systematic review and case series.” *Headache*. Published May 2024;64:674–684. DOI: https://doi.org/10.1111/head.14728.
- Cittadini E, Goadsby PJ. “Hemicrania continua: a clinical study of 39 patients with diagnostic implications.” *Brain*. Published July 2010;133:1973–1986. DOI: https://doi.org/10.1093/brain/awq137.
- Prakash S, Patel P. “Hemicrania continua: clinical review, diagnosis and management.” *Journal of Pain Research*. Published June 2017;10:1493–1509. DOI: https://doi.org/10.2147/JPR.S128472.
- ClinicalTrials.gov. **NCT04303845**, “Erenumab for Treatment of Hemicrania Continua,” Mayo Clinic; study period August 2021–April 2022; terminated, n=2 (NCT04303845 chunk 1).
- ClinicalTrials.gov. **NCT01842763**, “French Database of Occipital Nerves Stimulation in the Treatment of Refractory Chronic Headache Disorders”; first posted April 30, 2013; registry status active, not recruiting; mixed-diagnosis enrollment n=246 (NCT01842763 chunk 1).

**Important limitation:** exact abstract quotations could be supplied only where retrievable source text was available. Several key 2023–2024 articles were identifiable by bibliographic metadata but their full abstracts were not available through the retrieval corpus; wording from those articles has therefore not been presented as a direct quotation.

References

1. (NCT04303845 chunk 1): Rashmi B. Halker Singh MD. Erenumab For Treatment of Hemicrania Continua. Mayo Clinic. 2021. ClinicalTrials.gov Identifier: NCT04303845

2. (lane2024primaryheadachesare pages 7-9): Russell Lane and Paul Davies. Primary headaches are a continuum driven by a common process. Discover Medicine, Oct 2024. URL: https://doi.org/10.1007/s44337-024-00068-w, doi:10.1007/s44337-024-00068-w. This article has 3 citations.

3. (lane2024primaryheadachesare pages 9-11): Russell Lane and Paul Davies. Primary headaches are a continuum driven by a common process. Discover Medicine, Oct 2024. URL: https://doi.org/10.1007/s44337-024-00068-w, doi:10.1007/s44337-024-00068-w. This article has 3 citations.

4. (lane2024primaryheadachesare pages 11-12): Russell Lane and Paul Davies. Primary headaches are a continuum driven by a common process. Discover Medicine, Oct 2024. URL: https://doi.org/10.1007/s44337-024-00068-w, doi:10.1007/s44337-024-00068-w. This article has 3 citations.

5. (NCT01842763 chunk 1):  French Database of Occipital Nerves Stimulation in the Treatment of Refractory Chronic Headache Disorders. Centre Hospitalier Universitaire de Nice. 2013. ClinicalTrials.gov Identifier: NCT01842763

6. (NCT01842763 chunk 2):  French Database of Occipital Nerves Stimulation in the Treatment of Refractory Chronic Headache Disorders. Centre Hospitalier Universitaire de Nice. 2013. ClinicalTrials.gov Identifier: NCT01842763

## Artifacts

- [Edison artifact artifact-00](Hemicrania_Continua-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 7 |
| Resolved | 7 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |

All extracted references resolved successfully.