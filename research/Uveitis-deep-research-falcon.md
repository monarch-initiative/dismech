---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-26T22:12:04.043455'
end_time: '2026-08-26T22:20:20.095600'
duration_seconds: 496.05
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Uveitis
  mondo_id: ''
  category: Complex
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 46
reference_validation:
  total_references: 16
  verified: 16
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 16
  on_topic: 6
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Uveitis-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Uveitis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Uveitis** covering all of the
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
- **Disease Name:** Uveitis
- **MONDO ID:**  (if available)
- **Category:** Complex

## Research Objectives

Please provide a comprehensive research report on **Uveitis** covering all of the
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


# Uveitis: comprehensive disease-characteristics report

## Executive summary

Uveitis is not one molecular disease but a heterogeneous group of more than 25 intraocular inflammatory disorders. It is classified anatomically as anterior, intermediate, posterior, or panuveitis and etiologically as infectious, noninfectious immune-mediated, idiopathic, drug/trauma/surgery-associated, or masquerade disease. The umbrella concept is therefore **complex and usually multifactorial**, not a single-gene Mendelian condition. Uveitis disproportionately affects working-age people, can recur for decades, and causes vision loss through both direct inflammatory injury and complications such as macular edema, cataract, glaucoma, retinal ischemia, and retinal detachment. Reported prevalence is approximately 36.2–730 per 100,000 and incidence 17–52.4 per 100,000 person-years, with large geographic and methodological variation. (asghar2024“infectiousuveitisa pages 1-2, trivedi2019theuseof pages 3-5, rosenbaum2018theeyeshave pages 1-3, delatorre2024epidemiologyclinicalfeatures pages 1-2)

The most important 2023–2024 advances are: evidence connecting HLA-B27 uveitis to enteric antigen exposure and mucosally differentiated CD8 T cells; single-cell resolution of Th17/Treg and PIM1–CXCR4 biology; aqueous and tear proteomic biomarker discovery; highly accurate deep-learning detection of acute retinal necrosis; quantification of immune-checkpoint-inhibitor-associated risk; and late-stage trials of oral pathway-directed therapy and optimized local corticosteroid delivery. These findings remain heterogeneous in readiness: imaging AI has human external validation, proteomic panels require larger validation, and TIGIT, dimethyl fumarate, progesterone, and CD28/ICOS blockade remain preclinical for uveitis. (wu2024comprehensiveproteomicprofiling pages 1-2, peters2024tigitstimulationsuppresses pages 1-2, kuo2024associationbetweenimmune pages 1-2, rodriguezmartinez2024potentialprognosticprotein pages 1-2, liu2023progesteroneattenuatesth17cell pages 1-2, zhu2024beneficialmechanismsof pages 1-2, paley2024mucosalsignaturesof pages 1-2, wang2024automatedearlydetection pages 1-2, NCT06431373 chunk 1, wilson2023systemicadministrationof pages 1-2)

The following table provides a compact ontology-ready representation; the narrative below adds qualification and evidence interpretation.

| Domain | Core finding | Suggested ontology terms/identifiers | Evidence type |
|---|---|---|---|
| Definition / disease entity | Uveitis is intraocular inflammation affecting the uveal tract and adjacent ocular structures; major anatomic classes are anterior, intermediate, posterior, and panuveitis (rosenbaum2018theeyeshave pages 1-3, rosenbaum2018theeyeshave pages 10-14, delatorre2024epidemiologyclinicalfeatures pages 1-2) | MONDO:0020283 uveitis; label-only: anterior uveitis, intermediate uveitis, posterior uveitis, panuveitis; MeSH/ICD/SUN classification labels | Human review + multicenter clinical cohort |
| Classification / disease-level resource | SUN criteria are used for uveitis definition and anterior chamber grading; National Eye Institute system used for vitreous haze grading (delatorre2024epidemiologyclinicalfeatures pages 1-2, wang2024automatedearlydetection pages 1-2) | label-only: SUN Working Group criteria; NEI vitreous haze scale | Human clinical standards |
| Epidemiology | Reported prevalence ranges about 36.2–730 per 100,000 and incidence 17–52.4 per 100,000; uveitis causes substantial visual impairment and often affects working-age adults (delatorre2024epidemiologyclinicalfeatures pages 1-2, trivedi2019theuseof pages 3-5, rosenbaum2018theeyeshave pages 1-3) | label-only: epidemiologic measure, visual impairment | Human epidemiology / reviews |
| Demographics / regional pattern | In a Colombian multicenter cohort of 3,404 patients, mean age at diagnosis was 41.1 years, 54.2% were female, 66.7% unilateral, 48.3% acute, and 83% non-granulomatous (delatorre2024epidemiologyclinicalfeatures pages 1-2) | label-only: unilateral disease, acute onset, non-granulomatous inflammation | Human multicenter cohort |
| Major phenotype / ocular symptoms-signs | Common phenotype spectrum includes anterior chamber cells/flare, vitreous haze, retinal vasculitis, chorioretinal inflammation, optic disc edema, and reduced visual acuity; anatomy-specific manifestations differ by subtype (rosenbaum2018theeyeshave pages 10-14, wang2024automatedearlydetection pages 1-2, delatorre2024epidemiologyclinicalfeatures pages 1-2) | HPO label-only: decreased visual acuity, photophobia, ocular pain, eye redness, floaters, vitreous haze, retinal vasculitis, macular edema | Human clinical + imaging |
| Major phenotype / pediatric disease | Pediatric uveitis can be asymptomatic, especially JIA-associated chronic anterior uveitis; childhood incidence ~4.3/100,000 and prevalence ~27.9/100,000 (chang2021uveitisinchildren pages 1-3) | HPO label-only: asymptomatic anterior uveitis, cataract, glaucoma | Human pediatric review |
| Quality-of-life / functional burden | Uveitis is sight-threatening and associated with physical, economic, and visual-function burden; VFQ-25 is used as an outcome in current trials (zhu2024beneficialmechanismsof pages 1-2, NCT06310837 chunk 1) | label-only: NEI VFQ-25; visual function impairment | Human review + interventional trial design |
| Anatomy affected / organ level | Primary structures include iris, ciliary body, choroid, retina, vitreous, anterior chamber, and posterior segment (rosenbaum2018theeyeshave pages 10-14, wu2024comprehensiveproteomicprofiling pages 1-2, wang2024automatedearlydetection pages 1-2) | UBERON label-only: iris, ciliary body, choroid, retina, vitreous humor, anterior chamber of eyeball, posterior segment of eyeball | Human review + proteomics |
| Cell types involved | Pathogenic and regulatory immune cells implicated include Th17 cells, Th1 cells, Treg cells, CD8+ T cells, dendritic cells, granulocytes/neutrophils, plasma cells/B cells, NK cells, and retinal/endothelial cells (peters2024tigitstimulationsuppresses pages 1-2, liu2023progesteroneattenuatesth17cell pages 1-2, zhu2024beneficialmechanismsof pages 1-2, paley2024mucosalsignaturesof pages 1-2, hoffmann2022preactivatedgranulocytesfrom pages 1-3, chang2021uveitisinchildren pages 1-3) | CL label-only: T helper 17 cell, T-helper 1 cell, regulatory T cell, CD8-positive alpha-beta T cell, dendritic cell, neutrophil, plasma cell, natural killer cell, endothelial cell | Human + animal + in vitro |
| Molecular pathways | Recurrently implicated pathways include cytokine-cytokine receptor interaction, JAK-STAT signaling, IL-23/Th17/GM-CSF signaling, PIM1-AKT-FOXO1, CXCR4-mediated trafficking, complement activation, ROS/TXNIP/HIF-1α, NF-κB, and STAT3 (asghar2024“infectiousuveitisa pages 1-2, liu2023progesteroneattenuatesth17cell pages 1-2, zhu2024beneficialmechanismsof pages 1-2, wu2024comprehensiveproteomicprofiling pages 1-2, hoffmann2022preactivatedgranulocytesfrom pages 1-3) | GO/Reactome label-only: inflammatory response, T cell activation, leukocyte migration, cytokine-mediated signaling pathway, complement activation, oxidative stress response | Human omics + animal mechanistic + in vitro |
| Etiology / broad categories | Uveitis can be infectious, noninfectious immune-mediated, drug-induced, traumatic, post-surgical, idiopathic, or masquerade syndrome (delatorre2024epidemiologyclinicalfeatures pages 1-2, trivedi2019theuseof pages 1-3, kuo2024associationbetweenimmune pages 1-2) | MONDO:0020283; label-only: infectious uveitis, noninfectious uveitis, drug-induced uveitis, masquerade syndrome | Human cohort + reviews |
| Etiology / infectious | Infectious uveitis is caused by viruses, bacteria, fungi, and parasites; a 2024 review found viruses 39% and bacteria 17% among infectious etiologies reviewed, and Colombian data identified toxoplasmosis as a leading cause (25.3%) (asghar2024“infectiousuveitisa pages 1-2, delatorre2024epidemiologyclinicalfeatures pages 1-2) | label-only: ocular toxoplasmosis, viral uveitis, tuberculous uveitis, herpetic uveitis | Human systematic review + cohort |
| Etiology / immune-mediated systemic associations | Important associated systemic diseases include spondyloarthritis/HLA-B27 disease, juvenile idiopathic arthritis, Behçet disease, sarcoidosis, Vogt–Koyanagi–Harada syndrome, inflammatory bowel disease, and TINU syndrome (trivedi2019theuseof pages 1-3, rosenbaum2018theeyeshave pages 1-3, chang2021uveitisinchildren pages 1-3) | label-only: HLA-B27-associated acute anterior uveitis, JIA-associated uveitis, Behçet uveitis, ocular sarcoidosis, VKH, TINU syndrome | Human reviews |
| Genetic risk | HLA-B27 is a major risk allele for acute anterior uveitis; Open Targets links uveitis/anterior uveitis to ERAP1, IL23R, TNF, IL17A, and IL1B, supporting polygenic immune susceptibility (paley2024mucosalsignaturesof pages 1-2, OpenTargets Search: uveitis, chang2021uveitisinchildren pages 1-3) | label-only: HLA-B27, ERAP1, IL23R, TNF, IL17A, IL1B | Human genetic + database evidence |
| Gene-environment / microbiome | HLA-B27-associated disease may involve enteric antigen exposure and molecular mimicry; YeiH-specific CD8+ T cells in B27-associated anterior uveitis show mucosal signatures (CD161, integrin α4β7, CCR6), supporting a gut-eye axis (paley2024mucosalsignaturesof pages 1-2) | GO label-only: antigen processing and presentation, mucosal immune response; CL label-only: CD8+ T cell | Human translational immunology |
| Environmental / drug trigger | Immune checkpoint inhibitors are a clinically important trigger of drug-induced uveitis; in TriNetX, ICI exposure was associated with HR 2.39 for incident uveitis over 144 months (kuo2024associationbetweenimmune pages 1-2) | NCIT label-only: immune checkpoint inhibitor therapy; HPO label-only: uveitis adverse event | Human population-based EHR cohort |
| Diagnostics / clinical workup | Standard workup includes ophthalmic examination by slit lamp, intraocular pressure measurement, dilated fundus examination, visual acuity, and evaluation for systemic/infectious disease in multidisciplinary care (delatorre2024epidemiologyclinicalfeatures pages 1-2, rodriguezmartinez2024potentialprognosticprotein pages 1-2) | LOINC/SNOMED label-only: visual acuity testing, slit lamp exam, tonometry, dilated fundus exam | Human clinical practice |
| Diagnostics / imaging | Imaging and grading include OCT, fluorescein angiography, ultra-widefield color fundus photography, and OCT/OCTA in trials and biomarker workups (wang2024automatedearlydetection pages 1-2, NCT06310837 chunk 1, NCT02595398 chunk 1) | label-only: optical coherence tomography, fluorescein angiography, OCT angiography, ultra-widefield fundus photography | Human imaging studies + trials |
| Diagnostics / biomarkers | Aqueous humor proteomics in idiopathic uveitis/VKH identified complement activation and suggested transferrin plus complement factor B as a biomarker panel; tear proteomics in anti-TNF nonresponders highlighted DEF-1,3, biotinidase, ABCA1, neutrophil effector functions, and redox imbalance (wu2024comprehensiveproteomicprofiling pages 1-2, rodriguezmartinez2024potentialprognosticprotein pages 1-2) | label-only: transferrin, complement factor B, defensin-1/3, biotinidase, ABCA1, S100 proteins, cytokines/chemokines | Human proteomics |
| Diagnostics / AI implementation | Deep learning on ultra-widefield fundus images achieved AUROC 0.996 internal and 0.973 external for uveitis screening, and AUROC 0.960/0.971 for ARN discrimination, with performance comparable to ophthalmologists (wang2024automatedearlydetection pages 1-2) | NCIT label-only: artificial intelligence-assisted diagnosis; label-only: acute retinal necrosis | Human computational / imaging validation |
| Complications | Important complications include cataract, glaucoma/ocular hypertension, cystoid macular edema, retinal detachment, epiretinal membrane, vitreous hemorrhage, retinal neovascularization, ischemia, and blindness/vision loss (trivedi2019theuseof pages 3-5, delatorre2024epidemiologyclinicalfeatures pages 1-2, wang2024automatedearlydetection pages 1-2, chang2021uveitisinchildren pages 1-3) | HPO label-only: cataract, glaucoma, cystoid macular edema, retinal detachment, vitreous hemorrhage, blindness | Human cohort + reviews |
| Prognosis / disease course | Disease course may be acute, chronic, recurrent, unilateral or bilateral; recurrent or undertreated inflammation leads to structural damage and visual loss; ARN treatment delay is linked to worse vision outcomes (delatorre2024epidemiologyclinicalfeatures pages 1-2, wang2024automatedearlydetection pages 1-2, chang2021uveitisinchildren pages 1-3) | HPO label-only: recurrent uveitis, chronic inflammation, severe visual loss | Human cohort + disease-specific study |
| Established treatment / corticosteroids | Corticosteroids remain mainstay therapy (topical, local, systemic); glucocorticoid target association is reflected by NR3C1 linkage in Open Targets (trivedi2019theuseof pages 1-3, OpenTargets Search: uveitis) | NCIT label-only: corticosteroid therapy, triamcinolone acetonide, fluocinolone acetonide implant | Human reviews + database |
| Established treatment / conventional immunomodulators | Steroid-sparing systemic agents include methotrexate, azathioprine, mycophenolate mofetil, and cyclosporine (trivedi2019theuseof pages 1-3) | NCIT label-only: methotrexate, azathioprine, mycophenolate mofetil, cyclosporine | Human review |
| Established treatment / biologics | Adalimumab is the only systemic biologic specifically noted as FDA/EMA approved for noninfectious intermediate, posterior, and panuveitis; nonresponse may occur in up to 40% (rodriguezmartinez2024potentialprognosticprotein pages 1-2, trivedi2019theuseof pages 1-3) | NCIT label-only: adalimumab, TNF inhibitor | Human review + clinical proteomics cohort |
| Local interventional therapy | Intravitreal/suprachoroidal corticosteroid delivery is established in practice and trials; PEACHTREE tested suprachoroidal triamcinolone acetonide for uveitic macular edema, and TYNI is evaluating two YUTIQ implants versus sham (NCT02595398 chunk 1, NCT05486468 chunk 1) | NCIT label-only: suprachoroidal injection, intravitreal implant, triamcinolone acetonide, fluocinolone acetonide | Human phase 3 trials |
| Emerging systemic therapy / current trials | Active 2024-era trials include brepocitinib phase 3 CLARITY in active noninfectious non-anterior uveitis and a randomized trial of adalimumab biosimilar + mycophenolate versus corticosteroids + mycophenolate; izokibep phase 2b was terminated after endpoints were not met (NCT06431373 chunk 1, NCT06310837 chunk 1, NCT05384249 chunk 1) | NCIT label-only: brepocitinib, adalimumab biosimilar, mycophenolate mofetil, izokibep, JAK/TYK2 pathway inhibition, IL-17A inhibition | Human clinical trials |
| Emerging therapeutic targets | Candidate targets/mechanisms from recent work include TIGIT agonism, PIM1/CXCR4 inhibition, IL-6/JAK/complement targeting in anti-TNF-refractory disease, and dual CD28/ICOS blockade with acazicolcept (peters2024tigitstimulationsuppresses pages 1-2, zhu2024beneficialmechanismsof pages 1-2, rodriguezmartinez2024potentialprognosticprotein pages 1-2, wilson2023systemicadministrationof pages 1-2) | NCIT label-only: TIGIT agonist, acazicolcept, IL-6 inhibitor, JAK inhibitor, complement inhibitor, CXCR4 inhibitor, PIM1 inhibitor | Animal mechanistic + human proteomics + preclinical translational |
| Prevention / secondary-tertiary | Practical prevention centers on early detection, prompt treatment, multidisciplinary screening in at-risk groups such as JIA, and avoidance/exclusion of infectious etiologies before immunosuppression (chang2021uveitisinchildren pages 1-3, delatorre2024epidemiologyclinicalfeatures pages 1-2, NCT06431373 chunk 1) | label-only: ophthalmic screening, tertiary prevention, tuberculosis screening before biologics | Human guidelines/review + trial eligibility |
| Natural disease in other species | Equine recurrent uveitis is a spontaneous remitting-relapsing autoimmune uveitis and a leading cause of blindness in horses; it shares clinical and immunopathologic features with human recurrent panuveitis (hoffmann2022preactivatedgranulocytesfrom pages 1-3) | label-only: equine recurrent uveitis; NCBI Taxon label-only: Equus caballus | Veterinary natural disease + comparative pathology |
| Model organisms / experimental models | Experimental autoimmune uveitis (EAU) in mice and rats is the principal model for autoimmune/noninfectious uveitis; useful for studying Th1/Th17 disease, Treg biology, ocular infiltration, and testing therapies, but does not fully capture all human subtypes (peters2024tigitstimulationsuppresses pages 1-2, liu2023progesteroneattenuatesth17cell pages 1-2, zhu2024beneficialmechanismsof pages 1-2, wilson2023systemicadministrationof pages 1-2, chang2021uveitisinchildren pages 1-3) | label-only: experimental autoimmune uveitis, Lewis rat model, C57BL/6 mouse model | Animal model review + mechanistic studies |


*Table: This table summarizes ontology-ready disease facts for uveitis across clinical, mechanistic, diagnostic, therapeutic, and translational domains. It is designed to support structured knowledge-base curation using only evidence already gathered.*

## 1. Disease information

**Definition and classification.** Uveitis means intraocular inflammation involving the uveal tract—iris, ciliary body, and choroid—and often adjacent retina, vitreous, retinal vessels, and optic nerve. Under Standardization of Uveitis Nomenclature (SUN), anterior uveitis has anterior-chamber inflammation as the principal site; intermediate uveitis predominantly affects vitreous; posterior uveitis affects retina and/or choroid; and panuveitis involves anterior chamber, vitreous, and retina/choroid without one predominant site. Descriptors also include onset, duration, course, laterality, granulomatous morphology, activity, and structural damage. (asghar2024“infectiousuveitisa pages 1-2, rosenbaum2018theeyeshave pages 10-14, rosenbaum2018theeyeshave pages 1-3, delatorre2024epidemiologyclinicalfeatures pages 1-2)

**Identifiers and synonyms.** The current umbrella identifier retrieved from Open Targets/MONDO is **MONDO:0020283**. More specific entities include anterior uveitis **MONDO:0006651**, posterior uveitis **MONDO:0006918**, and autoimmune uveitis **MONDO:0031012**. Common terms include intraocular inflammation, iritis, iridocyclitis, choroiditis, chorioretinitis/retinochoroiditis, pars planitis, and panuveitis, although these are not fully interchangeable. ICD-10-CM distributes disease across H20–H22 and H30–H32 rather than providing one etiologically precise umbrella code; subtype coding should be preferred. No single OMIM or Orphanet entry appropriately represents all uveitis because the umbrella is not a unitary Mendelian or rare disease. (OpenTargets Search: uveitis, rosenbaum2018theeyeshave pages 10-14, rosenbaum2018theeyeshave pages 1-3)

**Data provenance.** Most facts here are aggregated disease-level evidence from reviews, cohorts, databases, and trials. The 2024 Colombian study aggregated clinical records from 3,404 patients; the immune-checkpoint study used propensity-matched EHR data; aqueous/tear studies used patient biospecimens; and experimental autoimmune uveitis (EAU) findings come from animals rather than individual-patient EHRs. (wu2024comprehensiveproteomicprofiling pages 1-2, kuo2024associationbetweenimmune pages 1-2, rodriguezmartinez2024potentialprognosticprotein pages 1-2, delatorre2024epidemiologyclinicalfeatures pages 1-2)

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal categories

1. **Infectious:** herpesviruses including HSV/VZV/CMV, *Toxoplasma gondii*, *Mycobacterium tuberculosis*, *Treponema pallidum*, and regionally important bacterial, fungal, and parasitic infections. A 2024 systematic review of 97 studies reported viruses in 39% and bacteria in 17% of its infectious-uveitis etiologic distribution, emphasizing that proportions vary geographically. In Colombia, toxoplasmosis accounted for 25.3% of all cases and virus-associated disease for 6.4%. (asghar2024“infectiousuveitisa pages 1-2, asghar2024“infectiousuveitisa pages 14-15, delatorre2024epidemiologyclinicalfeatures pages 1-2)
2. **Noninfectious immune-mediated:** isolated idiopathic uveitis or ocular manifestations of HLA-B27 spondyloarthritis, JIA, Behçet disease, sarcoidosis, inflammatory bowel disease, Vogt–Koyanagi–Harada disease, and tubulointerstitial nephritis–uveitis. (trivedi2019theuseof pages 1-3, rosenbaum2018theeyeshave pages 1-3, chang2021uveitisinchildren pages 1-3)
3. **Other:** trauma, surgery, lens-related inflammation, drugs, and masquerade syndromes such as intraocular lymphoma. The Colombian investigators explicitly included autoimmune, autoinflammatory, traumatic, postsurgical, drug-induced, and idiopathic categories. (kuo2024associationbetweenimmune pages 1-2, delatorre2024epidemiologyclinicalfeatures pages 1-2)

### Genetic susceptibility

Uveitis overall has **multifactorial/polygenic inheritance**. HLA-B27 is the strongest established risk factor for acute anterior uveitis; approximately 50% of acute anterior uveitis patients in a recent translational report were HLA-B27-positive. HLA-DR2/DR15 has been associated with pars planitis, and syndrome-specific associations include HLA-B51 in Behçet disease and melanocyte-directed HLA backgrounds in VKH. Open Targets supports associations involving **ERAP1, IL23R, TNF, IL17A, IL1B**, and other loci, but these are susceptibility/therapeutic associations, not deterministic “causal genes” for umbrella uveitis. (OpenTargets Search: uveitis, trivedi2019theuseof pages 3-5, paley2024mucosalsignaturesof pages 1-2, chang2021uveitisinchildren pages 1-3)

Accordingly, routine claims about pathogenic variants, penetrance, carrier frequency, anticipation, germline mosaicism, or founder variants are **not applicable to nonsyndromic umbrella uveitis**. Germline panel/WES/WGS testing is not routine; it is reserved for unusual pediatric, familial, syndromic, autoinflammatory, immunodeficiency, or retinal-dystrophy phenotypes. No recurrent somatic mutation or chromosomal abnormality defines ordinary uveitis.

### Environmental and iatrogenic factors

Geography, pathogen prevalence, sanitation, food exposure, immune status, migration, and access to molecular diagnostics shape infectious disease. Smoking and microbiome alterations are plausible modifiers in associated systemic disease, but no universal lifestyle exposure has a sufficiently consistent effect to be considered causal across all uveitis. Drug triggers include immune checkpoint inhibitors. In a 2024 matched TriNetX cohort of 71,931 exposed and 71,931 unexposed cancer patients, ICI use was associated with uveitis HR 2.39 (95% CI 2.07–2.75); anti-PD-1 monotherapy HR was 1.98, anti-CTLA-4 5.86, and combined anti-PD-1/CTLA-4 5.04. The article’s conclusion states: “A significantly increased risk for uveitis diseases was found among the ICI group from the first year of follow-up.” (kuo2024associationbetweenimmune pages 1-2)

### Protective factors and gene–environment interaction

No genetic or dietary factor is validated for primary prevention of all uveitis. Immune tolerance, intact blood–ocular barriers, regulatory T-cell activity, prompt infection control, and—in JIA—regular asymptomatic screening are practically protective against onset or damage. Hormonal observations, including pregnancy-associated remission, are hypothesis-generating rather than preventive recommendations. (liu2023progesteroneattenuatesth17cell pages 1-2, chang2021uveitisinchildren pages 1-3)

The clearest recent gene–environment model concerns HLA-B27. A 2024 human study found that YeiH-specific CD8 T cells in HLA-B27 acute anterior uveitis and axial spondyloarthritis expressed CD161, integrin α4β7, and CCR6, compatible with intestinal differentiation. Because YeiH occurs in enteric microbes and can be presented by HLA-B27 to ocular/joint-enriched public T-cell receptors, the proposed chain is: **HLA-B27 antigen presentation + enteric microbial exposure → cross-reactive mucosal CD8 T-cell expansion → trafficking to eye → acute anterior inflammation**. The authors cautiously conclude that early antigen exposure and differentiation “may occur in enteric organs”; this is strong translational evidence but not proof that one organism causes disease. Published July 18, 2024; DOI: https://doi.org/10.1172/jci.insight.174776. (paley2024mucosalsignaturesof pages 1-2)

## 3. Phenotypes

**Anterior disease** commonly produces acute pain, redness, photophobia, tearing, blurred vision, ciliary injection, keratic precipitates, anterior-chamber cells/flare, and sometimes posterior synechiae. HLA-B27 disease is typically sudden, unilateral, symptomatic, and recurrent. JIA-associated anterior uveitis is often bilateral, chronic, relapsing, and initially asymptomatic, making screening essential. Suggested HPO labels: ocular pain, photophobia, red eye, decreased visual acuity, anterior uveitis, posterior synechiae. (paley2024mucosalsignaturesof pages 1-2, chang2021uveitisinchildren pages 1-3)

**Intermediate disease** often causes floaters and blurred vision with vitreous cells/haze, snowballs/snowbanking, peripheral vasculitis, and macular edema. Pars planitis has a reported pediatric mean onset near 7.8 years. Suggested HPO labels: vitreous floaters, vitreous haze, retinal vasculitis, cystoid macular edema. (rosenbaum2018theeyeshave pages 10-14, chang2021uveitisinchildren pages 1-3)

**Posterior/panuveitis** causes floaters, visual-field defects, metamorphopsia or reduced acuity; signs include retinitis/choroiditis, retinal vasculitis, hemorrhage, optic-disc edema, macular edema, necrosis, and exudative or rhegmatogenous detachment. Severity ranges from mild self-limited episodes to rapidly blinding disease. Acute retinal necrosis is a particularly destructive herpetic phenotype. (asghar2024“infectiousuveitisa pages 1-2, wang2024automatedearlydetection pages 1-2)

**Frequency and laterality vary by setting.** In the 3,404-patient Colombian cohort, anterior uveitis was 49.5%, posterior 22.9%, panuveitis 22.3%, and intermediate 5.2%; 66.7% were unilateral, 48.3% acute, and 83% nongranulomatous. Mean diagnostic age was 41.1 years, 54.2% were female, and ages 30–50 were most frequent. These are referral-cohort—not universal population—frequencies. Published March 6, 2024; DOI: https://doi.org/10.1007/s00417-024-06422-z. (delatorre2024epidemiologyclinicalfeatures pages 1-2)

**Pediatric phenotype.** Estimated childhood incidence is 4.3/100,000 and prevalence 27.9/100,000. Approximate diagnostic proportions reported in a pediatric review were idiopathic anterior uveitis 29%, JIA-associated 21%, pars planitis 17%, and infectious 6%. Up to 45% of children with JIA-associated uveitis already have complications such as cataract or glaucoma at first ophthalmology assessment. (chang2021uveitisinchildren pages 1-3)

**Quality of life.** Pain and photophobia impair work/school during active anterior episodes; floaters, contrast loss, macular edema, field loss, treatment burden, and fear of recurrence impair daily function in chronic disease. NEI VFQ-25 is used in contemporary trials, but phenotype-specific utility/frequency values are not standardized across the heterogeneous umbrella. (zhu2024beneficialmechanismsof pages 1-2, NCT06310837 chunk 1, NCT05384249 chunk 1)

## 4. Genetic, molecular, and epigenetic information

There is no single causal gene for generic uveitis. Relevant molecular categories are: antigen presentation (**HLA-B27, HLA-B51, ERAP1**); Th17 biology (**IL23R, IL17A, STAT3, RORC**); inflammatory effectors (**TNF, IL1B, IL6, IFNG**); trafficking (**CXCR4, integrins**); and regulation (**FOXP3/Treg, TIGIT, PIM1**). Open Targets also highlights glucocorticoid receptor **NR3C1** and DHFR, reflecting therapeutic biology. These should be annotated as susceptibility genes/targets rather than pathogenic monogenic variants. (OpenTargets Search: uveitis, asghar2024“infectiousuveitisa pages 1-2, liu2023progesteroneattenuatesth17cell pages 1-2, zhu2024beneficialmechanismsof pages 1-2)

Human pediatric literature reports uveitis-associated DNA methylation and microRNA differences, but no epigenetic signature is yet clinically validated. Likewise, current evidence does not support routine variant-level ClinVar interpretation, population allele-frequency reporting, CMA, karyotype, FISH, mtDNA, or repeat-expansion testing for typical uveitis. (chang2021uveitisinchildren pages 1-3)

## 5. Environmental and infectious information

The principal non-genetic determinants are infection exposure, immune status, regional endemicity, drugs, surgery/trauma, and systemic inflammatory disease activity. Infectious uveitis can be viral, bacterial, fungal, or parasitic and frequently differs by geography; developing/high-TB/HIV settings carry larger infectious fractions than many high-income settings. Targeted history should cover travel/residence, animal and undercooked-meat exposure, TB and syphilis risk, immunosuppression, recent ocular surgery/trauma, and medications. (asghar2024“infectiousuveitisa pages 1-2, trivedi2019theuseof pages 3-5, asghar2024“infectiousuveitisa pages 14-15)

No robust evidence supports alcohol, exercise, or a specific diet as universal risk/protective factors. Microbiome associations are an active research area, but clinical manipulation cannot yet be recommended. ICI-associated uveitis is the strongest quantified recent iatrogenic signal. (kuo2024associationbetweenimmune pages 1-2, paley2024mucosalsignaturesof pages 1-2)

## 6. Mechanism and pathophysiology

### Integrated causal chain

**Upstream events** are ocular infection or immune recognition of retinal/uveal antigens in a genetically susceptible host. Pathogen-derived danger signals or antigen-presenting dendritic cells activate innate immunity and prime Th1, Th17, and cytotoxic T cells in draining lymphoid/mucosal compartments. Loss of Treg-mediated tolerance and molecular mimicry can sustain autoreactivity. **Intermediate events** include cytokine amplification through IL-23/IL-17/GM-CSF, IFN-γ, TNF, IL-6 and JAK–STAT; CXCR4/integrin-mediated leukocyte trafficking; complement activation; endothelial activation; and disruption of blood–aqueous/blood–retinal barriers. **Downstream events** are leukocyte entry, microglial/innate-cell activation, oxidative stress, edema, vasculitis, ECM disruption and photoreceptor/retinal injury, producing pain, floaters, reduced acuity, ischemia and irreversible scarring. (asghar2024“infectiousuveitisa pages 1-2, wu2024comprehensiveproteomicprofiling pages 1-2, liu2023progesteroneattenuatesth17cell pages 1-2, zhu2024beneficialmechanismsof pages 1-2, chang2021uveitisinchildren pages 1-3, hoffmann2022preactivatedgranulocytesfrom pages 1-3)

Suggested GO processes include inflammatory response, adaptive immune response, antigen processing and presentation, T-cell activation/differentiation, leukocyte migration, cytokine-mediated signaling, complement activation, response to oxidative stress, regulation of vascular permeability, and apoptotic cell death. Suggested CL terms include Th1 cell, Th17 cell, regulatory T cell, CD8-positive alpha-beta T cell, dendritic cell, neutrophil, monocyte/macrophage, plasma cell, NK cell, microglial cell, vascular endothelial cell, retinal pigment epithelial cell, and photoreceptor cell.

### Recent molecular profiling

* **Human aqueous proteomics (2024):** 44 samples—12 idiopathic uveitis, 16 VKH, 16 controls—yielded 557 proteins. IU and VKH shared ECM disruption, reduced retinal-cell proteins, complement activation, and innate-cell-marker enrichment; transferrin plus complement factor B formed a machine-learning-selected candidate panel validated by targeted mass spectrometry. Quote: “innate immunity played an important role, as indicated by complement cascade activation.” Published April 15, 2024; DOI: https://doi.org/10.1021/acsomega.3c10257. Small sample size makes this discovery evidence, not a diagnostic standard. (wu2024comprehensiveproteomicprofiling pages 1-2)
* **Human tear proteomics (2024):** adalimumab nonresponders had 29 differential proteins—14 upregulated, 15 downregulated—linked to neutrophil effectors and redox imbalance. DEF-1/3, biotinidase, and ABCA1 were candidate response biomarkers. Up to 40% may have primary/secondary adalimumab nonresponse. Published November 14, 2024; DOI: https://doi.org/10.1167/iovs.65.13.29. (rodriguezmartinez2024potentialprognosticprotein pages 1-2)
* **Mouse single-cell studies:** progesterone reversed AP-1/S100/Cxcr4 inflammatory programs, Th17/Treg imbalance, Id2/Pim1 and IL-23/Th17/GM-CSF signaling. Dimethyl fumarate suppressed PIM1/CXCR4, restored Teff/Treg balance through PIM1–AKT–FOXO1, and reduced ocular Teff infiltration. These support mechanisms but not human efficacy. DOI: https://doi.org/10.1186/s12974-023-02829-3 and https://doi.org/10.1186/s12974-024-03096-6. (liu2023progesteroneattenuatesth17cell pages 1-2, zhu2024beneficialmechanismsof pages 1-2)
* **Animal TIGIT work (2024):** agonism at symptom onset reduced EAU severity and Th17 infiltration; transferred Tregs suppressed disease in recipients. Quote: stimulation “allows for induction of regulatory immunity that provides resistance to uveitis.” DOI: https://doi.org/10.1093/jleuko/qiae116. (peters2024tigitstimulationsuppresses pages 1-2)

Spatial transcriptomics, validated human single-cell atlases, CRISPR screens, and integrated clinical multi-omics remain limited; no such assay is standard of care.

## 7. Anatomical structures

The primary organ is the eye. Sites include iris and anterior chamber, ciliary body, pars plana, vitreous, choroid/choriocapillaris, retina and retinal vessels, retinal pigment epithelium, macula, and optic disc/nerve head. Secondary involvement includes lens (cataract), trabecular meshwork/optic nerve (uveitic glaucoma), epiretinal interface, and sclera. Suggested UBERON labels: eye, uvea, iris, ciliary body, choroid, retina, vitreous body, anterior chamber, retinal blood vessel, and optic nerve. (rosenbaum2018theeyeshave pages 10-14, wu2024comprehensiveproteomicprofiling pages 1-2, delatorre2024epidemiologyclinicalfeatures pages 1-2, wang2024automatedearlydetection pages 1-2)

Relevant subcellular compartments depend on mechanism: nucleus/chromatin for transcriptional programs, plasma membrane for HLA/TCR/cytokine receptors and adhesion, ER for antigen processing, mitochondria for redox metabolism, and inflammasome/cytosolic signaling complexes. These are mechanistic annotations rather than diagnostic lesions.

Laterality is subtype-dependent: HLA-B27 attacks often alternate unilaterally; JIA/VKH/Behçet and other systemic entities are commonly bilateral or become bilateral. In Colombia, all-subtype disease was unilateral in 66.7%. (paley2024mucosalsignaturesof pages 1-2, delatorre2024epidemiologyclinicalfeatures pages 1-2, chang2021uveitisinchildren pages 1-3)

## 8. Temporal development

Onset can occur from childhood through late adulthood. Acute disease develops suddenly; insidious JIA-associated disease may be asymptomatic. SUN course descriptors include acute, recurrent, and chronic. In the Colombian cohort, 48.3% were acute. HLA-B27 episodes generally resolve over weeks but recur; chronic intermediate/posterior/panuveitis can persist or relapse for years. (paley2024mucosalsignaturesof pages 1-2, delatorre2024epidemiologyclinicalfeatures pages 1-2, chang2021uveitisinchildren pages 1-3)

There is no universal stage system. Clinically useful states are active inflammation, improvement/inactivity, remission off therapy, recurrence, and accumulated damage. Critical windows include immediate treatment of destructive infection and early control of posterior inflammation or macular edema. In ARN, a mean treatment delay of 5.2 days was associated with a 2.3-fold higher likelihood of severe visual loss than treatment within one day. (wang2024automatedearlydetection pages 1-2)

Remission may be spontaneous in self-limited anterior attacks or treatment-induced. Durable remission is less predictable in chronic NIU. Continued surveillance remains important because structural damage can progress independently of current symptom intensity.

## 9. Inheritance and population

Prevalence estimates span approximately 36.2–730/100,000 and incidence 17–52.4/100,000/year. Older reviews estimate prevalence near 1/1,000. Uveitis accounts for approximately 5–10% of global visual impairment; up to 35% of affected patients may experience significant vision loss. Differences reflect case definitions, referral patterns, geography and infection prevalence. (trivedi2019theuseof pages 1-3, trivedi2019theuseof pages 3-5, rosenbaum2018theeyeshave pages 1-3, delatorre2024epidemiologyclinicalfeatures pages 1-2)

Adults of working age carry a large burden. The Colombian cohort’s peak was age 30–50, with modest female predominance, but there is no universal sex ratio: HLA-B27/spondyloarthritis-associated disease often tracks male-enriched systemic disease, while JIA-associated patterns differ. Infectious disease predominates in some lower-resource/endemic regions; immune-mediated anterior disease is proportionally more common in many developed settings. (asghar2024“infectiousuveitisa pages 1-2, trivedi2019theuseof pages 3-5, delatorre2024epidemiologyclinicalfeatures pages 1-2, chang2021uveitisinchildren pages 1-3)

Inheritance is generally complex/polygenic with variable, incomplete penetrance. Anticipation, carrier frequency and germline mosaicism are not meaningful umbrella-disease attributes. Population-specific HLA frequencies contribute to geographic variation, but do not determine disease by themselves.

## 10. Diagnostics

Diagnosis is clinical and etiologic. Minimum examination includes history, best-corrected visual acuity, pupils, slit-lamp examination with SUN anterior-cell grading, intraocular pressure, and dilated fundus examination with vitreous-haze grading. OCT quantifies macular edema/retinal structure; fluorescein angiography detects vascular leakage, ischemia and inflammatory lesions; indocyanine-green angiography supports choroidal disease; fundus photography/ultra-widefield imaging documents peripheral lesions; ultrasonography is useful when media are opaque. (delatorre2024epidemiologyclinicalfeatures pages 1-2, wang2024automatedearlydetection pages 1-2, NCT06310837 chunk 1, NCT02595398 chunk 1)

Laboratory investigation should be **phenotype- and exposure-directed**, not an indiscriminate panel. Commonly considered tests include syphilis serology and TB testing/chest imaging; HLA-B27 for recurrent acute anterior disease; ACE/chest imaging where sarcoidosis is plausible; ANA-based JIA risk assessment in children; renal studies for TINU; and ocular-fluid PCR for HSV/VZV/CMV or toxoplasma in selected atypical/severe cases. Aqueous/vitreous culture, PCR, or metagenomic testing is especially important before escalating immunosuppression when infection remains plausible. Biopsy/cytology/flow studies are reserved for suspected lymphoma or other masquerades.

**Differential diagnoses** include conjunctivitis, keratitis, scleritis, acute angle closure, endophthalmitis, retinal vascular occlusion, retinal detachment, intraocular lymphoma/leukemia, pigment dispersion, postoperative inflammation, and retinal degeneration. Distinguishing infection from sterile inflammation is the highest-stakes decision.

**Recent implementation:** DeepDrARN used 11,508 ultra-widefield images from 1,112 participants. Uveitis-screening AUROC was 0.996 internally and 0.973 externally; ARN discrimination AUROC was 0.960 and 0.971. External sensitivity/specificity for three-way classification were 78.7%/89.1%. Performance exceeded the average accuracy of seven ophthalmologists by 6.57% for screening and 11.14% for ARN identification. This is impressive retrospective validation, not yet autonomous diagnosis. DOI: https://doi.org/10.1186/s40662-024-00396-z. (wang2024automatedearlydetection pages 1-2)

Genetic testing, RNA-seq, proteomics, metabolomics, epigenomics and “liquid biopsy” are not standard diagnostics for generic uveitis. Aqueous/tear proteomics and microRNAs remain investigational. (golubenco2024biomarkersofuveitis pages 1-3, golubenco2024biomarkersofuveitis pages 10-10, wu2024comprehensiveproteomicprofiling pages 1-2, rodriguezmartinez2024potentialprognosticprotein pages 1-2)

## 11. Outcomes and prognosis

Uveitis usually does not independently shorten life expectancy; mortality is driven by associated infection/systemic disease or treatment complications. Therefore, conventional 5- or 10-year survival rates are not useful umbrella outcomes.

The main morbidity is visual disability. Reported complications include cataract (24%), retinal neovascularization (16%) and cystoid macular edema (8.6%) in one summarized evidence base, alongside glaucoma, epiretinal membrane, vitreous hemorrhage, ischemia and retinal detachment. In ARN, 20–73% of treated eyes may still develop rhegmatogenous retinal detachment. Prognosis is better with prompt etiologic diagnosis and inflammation control, and worse with posterior involvement, macular/optic-nerve damage, chronicity, frequent relapse, delayed treatment, infection, glaucoma, or poor therapeutic response. (trivedi2019theuseof pages 3-5, rodriguezmartinez2024potentialprognosticprotein pages 1-2, wang2024automatedearlydetection pages 1-2, chang2021uveitisinchildren pages 1-3)

Visual recovery is possible when loss reflects reversible cells/haze or edema, but limited after photoreceptor loss, macular ischemia, optic atrophy, glaucoma or detachment. No molecular prognostic biomarker is currently validated for routine care; S100 proteins, complement factor B/transferrin, and tear DEF-1/3–biotinidase–ABCA1 panels are candidates. (golubenco2024biomarkersofuveitis pages 1-3, wu2024comprehensiveproteomicprofiling pages 1-2, rodriguezmartinez2024potentialprognosticprotein pages 1-2)

## 12. Treatment and current implementation

Treatment requires first deciding whether disease is infectious. **Infectious uveitis** receives pathogen-directed antimicrobial therapy—often with carefully timed adjunctive anti-inflammatory treatment. Immunosuppression without antimicrobial coverage can worsen infection. (asghar2024“infectiousuveitisa pages 1-2)

**Noninfectious anterior uveitis:** topical corticosteroid plus cycloplegic/mydriatic is typical initial care; periocular/systemic therapy is used when severe or refractory. **Intermediate/posterior/panuveitis:** local corticosteroid injection/implant or systemic corticosteroid may induce control, followed by steroid-sparing therapy for chronic, bilateral, sight-threatening or relapsing disease. Conventional agents include methotrexate, mycophenolate mofetil, azathioprine and cyclosporine. Major toxicities include cataract/glaucoma from ocular steroids and metabolic, bone, infection and organ toxicities from systemic therapy. (trivedi2019theuseof pages 1-3, wilson2023systemicadministrationof pages 1-2)

**Biologics:** adalimumab, a TNF inhibitor, is the established systemic biologic for noninfectious intermediate, posterior and panuveitis; infliximab is widely used off-label, particularly in severe Behçet disease. Etanercept is not considered equivalently effective for uveitis. Tocilizumab, rituximab, abatacept and other pathway agents are used selectively/off-label. Up to 40% of patients may fail adalimumab primarily or secondarily, underscoring the need for response biomarkers and alternatives. (trivedi2019theuseof pages 1-3, rodriguezmartinez2024potentialprognosticprotein pages 1-2)

**Local therapy:** fluocinolone implants and intravitreal dexamethasone/triamcinolone can reduce systemic exposure but increase ocular hypertension and cataract risk. PEACHTREE was a phase 3, 160-person, randomized quadruple-masked study of two 4-mg suprachoroidal triamcinolone injections for uveitic macular edema; the primary endpoint was a ≥15-letter BCVA gain at week 24. (NCT02595398 chunk 1)

**Current/recent trials:** 

* **CLARITY, NCT06431373:** phase 3, randomized quadruple-masked oral brepocitinib versus placebo in 371 adults with active noninfectious intermediate/posterior/panuveitis; primary endpoint is time to treatment failure through 48 weeks. Started September 11, 2024; active, not recruiting in the retrieved record. https://clinicaltrials.gov/study/NCT06431373 (NCT06431373 chunk 1)
* **NCT06310837:** 128-person randomized comparison of adalimumab biosimilar + mycophenolate versus corticosteroid + mycophenolate; primary endpoint is 24-week ETDRS BCVA change, with VFQ-25, imaging and steroid-toxicity outcomes. https://clinicaltrials.gov/study/NCT06310837 (NCT06310837 chunk 1)
* **TYNI, NCT05486468:** recruiting phase 3 trial of two 0.18-mg YUTIQ fluocinolone implants versus sham, target n=30, with six-month recurrence as primary endpoint. https://clinicaltrials.gov/study/NCT05486468 (NCT05486468 chunk 1)
* **Izokibep, NCT05384249:** 96-person phase 2b IL-17A-inhibitor trial was terminated because primary and secondary endpoints did not reach statistical significance. This negative result warns against inferring clinical efficacy directly from Th17 biology. https://clinicaltrials.gov/study/NCT05384249 (NCT05384249 chunk 1)

Gene, RNA and approved cell therapies are not current standard treatments. Acazicolcept, TIGIT agonism, dimethyl fumarate and progesterone remain experimental. In 57 Lewis rats, systemic acazicolcept reduced clinical score, histology, ocular CD45 cells, and IL-17A/IFN-γ-expressing T cells, without steroid-associated weight loss; human studies are still required. (peters2024tigitstimulationsuppresses pages 1-2, liu2023progesteroneattenuatesth17cell pages 1-2, zhu2024beneficialmechanismsof pages 1-2, wilson2023systemicadministrationof pages 1-2)

Suggested NCIT intervention labels include corticosteroid therapy, cycloplegic therapy, antimicrobial therapy, methotrexate, mycophenolate mofetil, azathioprine, cyclosporine, adalimumab, infliximab, intravitreal injection, suprachoroidal injection and fluocinolone implant. No broadly accepted pharmacogenomic dosing guideline currently directs uveitis therapy.

## 13. Prevention

**Primary prevention** is etiology-specific rather than universal: vaccination and infection control where relevant; TB/syphilis/HIV prevention and treatment; food hygiene to reduce toxoplasmosis risk; vector control for endemic infections; and avoidance or surveillance of causative drugs when alternatives exist. No vaccine prevents autoimmune uveitis generally. (asghar2024“infectiousuveitisa pages 1-2, asghar2024“infectiousuveitisa pages 14-15)

**Secondary prevention** is early detection. Children with high-risk JIA—young onset, ANA-positive, oligoarticular/RF-negative polyarticular/psoriatic/undifferentiated categories—may require slit-lamp screening every three months because disease can be silent. Prompt specialist review is also warranted for recurrent painful red eye, new floaters, or visual loss and for ICI-treated patients with ocular symptoms. (kuo2024associationbetweenimmune pages 1-2, chang2021uveitisinchildren pages 1-3)

**Tertiary prevention** comprises rapid suppression of inflammation, steroid-sparing control of recurrence, OCT/pressure surveillance, antimicrobial prophylaxis where immunosuppression warrants it, vaccination before major immunosuppression, and timely cataract/glaucoma/macular-edema management. TB and infection screening before biologic/JAK-pathway therapy is integral. (NCT06431373 chunk 1, NCT06310837 chunk 1)

Genetic counseling is not ordinarily indicated for isolated uveitis, but may be appropriate where a defined inherited syndrome or autoinflammatory disorder is suspected.

## 14. Other species and natural disease

Naturally occurring uveitis affects companion and agricultural species, notably dogs, cats and horses; infectious etiologies vary by species. **Equine recurrent uveitis (ERU)** in *Equus caballus* (NCBI Taxonomy 9796) is a spontaneous painful remitting–relapsing disease and a major cause of equine blindness. Warmblood horses often develop posterior or panuveitis involving choroid, retina and vitreous. ERU shares retinal autoantigens including CRALBP, IRBP and S-antigen and T-cell/granulocyte biology with human recurrent NIU, making it a valuable comparative model. (hoffmann2022preactivatedgranulocytesfrom pages 1-3)

ERU granulocyte proteomics found 170 differentially abundant proteins after IL-8 stimulation, with PKA, PTEN and leukocyte-extravasation pathways and increased MMP25 implicated in blood–retinal-barrier dysfunction. This is veterinary/in-vitro evidence, not a validated human biomarker. Published August 23, 2022; DOI: https://doi.org/10.3390/ijms23179555; ProteomeXchange PXD013648. (hoffmann2022preactivatedgranulocytesfrom pages 1-3)

Uveitis itself is not zoonotically transmitted, but pathogens capable of causing it—such as *Toxoplasma* and some vector-borne organisms—can cross species or have animal reservoirs.

## 15. Model organisms

**EAU in mouse and rat** is the dominant induced model. Immunization with retinal antigens such as IRBP/S-antigen plus adjuvant breaks tolerance and produces T-cell-mediated chorioretinal inflammation. C57BL/6 reporter/knockout systems enable Th17/Treg tracking and genetic dissection; Lewis rats develop robust disease useful for pharmacology, OCT and histology. Readouts include fundus/clinical scores, OCT, histopathology, flow cytometry and aqueous cytokines. (peters2024tigitstimulationsuppresses pages 1-2, liu2023progesteroneattenuatesth17cell pages 1-2, zhu2024beneficialmechanismsof pages 1-2, wilson2023systemicadministrationof pages 1-2)

EAU recapitulates antigen-specific Th1/Th17 activation, leukocyte trafficking, blood–retinal-barrier failure, retinal inflammation and treatment response. It is useful for testing costimulation blockade, checkpoint agonism, cellular therapy and pathway inhibitors. Limitations are artificial antigen/adjuvant induction, strain dependence, compressed time course, predominantly posterior pathology, and incomplete modeling of human anterior, infectious, granulomatous, JIA-associated and spontaneous relapsing disease. Critically, no model has shown that B cells/autoantibodies alone reproduce human uveitis. (chang2021uveitisinchildren pages 1-3, wilson2023systemicadministrationof pages 1-2)

ERU complements EAU by providing spontaneous relapsing disease in a large eye, but cost, genetics, husbandry and species-specific immunology constrain experiments. Cell cultures, retinal explants, organoids and blood–retinal-barrier systems can isolate endothelial, RPE or immune mechanisms but cannot reproduce whole-organism immune trafficking.

## Evidence assessment and knowledge gaps

The most authoritative clinical conclusions are that uveitis is a syndrome requiring anatomic and etiologic classification; infection must be excluded before immunosuppression; early control prevents much visual loss; and chronic NIU often needs steroid-sparing multidisciplinary care. Epidemiologic estimates should always retain geography and referral context. Recent human HLA-B27/mucosal and proteomic studies provide biologically coherent mechanisms but need replication in larger, diverse cohorts. Animal single-cell findings identify promising PIM1, CXCR4, TIGIT and costimulation targets, yet the terminated izokibep trial demonstrates why mechanistic plausibility cannot substitute for randomized human efficacy. (rodriguezmartinez2024potentialprognosticprotein pages 1-2, paley2024mucosalsignaturesof pages 1-2, NCT06431373 chunk 1, wilson2023systemicadministrationof pages 1-2, NCT05384249 chunk 1)

Major gaps are validated noninvasive biomarkers, head-to-head treatment algorithms after anti-TNF failure, representative global incidence/DALY estimates, longitudinal pediatric risk prediction, prospective validation and bias auditing of diagnostic AI, human single-cell/spatial atlases, and precision selection among local, conventional systemic and targeted therapies.

References

1. (asghar2024“infectiousuveitisa pages 1-2): Muhammad Arif Asghar, Shixin Tang, Li Ping Wong, Peizeng Yang, and Qinjian Zhao. “infectious uveitis: a comprehensive systematic review of emerging trends and molecular pathogenesis using network analysis”. Journal of Ophthalmic Inflammation and Infection, Nov 2024. URL: https://doi.org/10.1186/s12348-024-00444-8, doi:10.1186/s12348-024-00444-8. This article has 24 citations and is from a peer-reviewed journal.

2. (trivedi2019theuseof pages 3-5): Amruta Trivedi and Constance Katelaris. The use of biologic agents in the management of uveitis. Internal Medicine Journal, 49:1352-1363, Nov 2019. URL: https://doi.org/10.1111/imj.14215, doi:10.1111/imj.14215. This article has 46 citations and is from a peer-reviewed journal.

3. (rosenbaum2018theeyeshave pages 1-3): James T. Rosenbaum and Andrew D. Dick. The eyes have it. Arthritis & Rheumatology, 70:1533-1543, Aug 2018. URL: https://doi.org/10.1002/art.40568, doi:10.1002/art.40568. This article has 67 citations and is from a highest quality peer-reviewed journal.

4. (delatorre2024epidemiologyclinicalfeatures pages 1-2): Alejandra de-la-Torre, Germán Mejía-Salgado, Carlos Cifuentes-González, William Rojas-Carabali, Miguel Cuevas, Sandra García, Carlos M. Rangel, Claudia Durán, Diana Isabel Pachón-Suárez, and Andrés Bustamante-Arias. Epidemiology, clinical features, and classification of 3,404 patients with uveitis: colombian uveitis multicenter study (col-uvea). Graefe's Archive for Clinical and Experimental Ophthalmology, 262:2601-2615, Mar 2024. URL: https://doi.org/10.1007/s00417-024-06422-z, doi:10.1007/s00417-024-06422-z. This article has 24 citations.

5. (wu2024comprehensiveproteomicprofiling pages 1-2): Lingzi Wu, Jinying An, Xueru Li, Qingqin Tao, Zheng Liu, Kai Zhang, Lei Zhou, and Xiaomin Zhang. Comprehensive proteomic profiling of aqueous humor in idiopathic uveitis and vogt–koyanagi–harada syndrome. ACS Omega, 9:18643-18653, Apr 2024. URL: https://doi.org/10.1021/acsomega.3c10257, doi:10.1021/acsomega.3c10257. This article has 5 citations and is from a peer-reviewed journal.

6. (peters2024tigitstimulationsuppresses pages 1-2): Kayleigh Peters, Trisha McDonald, Fauziyya Muhammad, Adrien Brady, John Dostal, and Darren J Lee. Tigit stimulation suppresses autoimmune uveitis by inhibiting th17 cell infiltration. Journal of leukocyte biology, 116:1054-1060, May 2024. URL: https://doi.org/10.1093/jleuko/qiae116, doi:10.1093/jleuko/qiae116. This article has 10 citations and is from a peer-reviewed journal.

7. (kuo2024associationbetweenimmune pages 1-2): Hou-Ting Kuo, Chia-Yun Chen, Alan Y. Hsu, Yu-Hsun Wang, Chun-Ju Lin, Ning-Yi Hsia, Yi-Yu Tsai, and James Cheng-Chung Wei. Association between immune checkpoint inhibitor medication and uveitis: a population-based cohort study utilizing trinetx database. Frontiers in Immunology, Jan 2024. URL: https://doi.org/10.3389/fimmu.2023.1302293, doi:10.3389/fimmu.2023.1302293. This article has 21 citations and is from a peer-reviewed journal.

8. (rodriguezmartinez2024potentialprognosticprotein pages 1-2): Lorena Rodríguez-Martínez, Carmen Antía Rodríguez-Fernández, Olalla Rodríguez Lemos, Begoña de Domingo, Pere García Bru, Jesús Mateos, and Anxo Fernández-Ferreiro. Potential prognostic protein biomarkers in tears from noninfectious uveitis patients under biologic treatment as a prelude to personalized medicine. Investigative Ophthalmology &amp; Visual Science, 65:29, Nov 2024. URL: https://doi.org/10.1167/iovs.65.13.29, doi:10.1167/iovs.65.13.29. This article has 4 citations and is from a domain leading peer-reviewed journal.

9. (liu2023progesteroneattenuatesth17cell pages 1-2): Xiuxing Liu, Chenyang Gu, Jianjie Lv, Qi Jiang, Wen Ding, Zhaohao Huang, Yidan Liu, Yuhan Su, Chun Zhang, Zhuping Xu, Xianggui Wang, and Wenru Su. Progesterone attenuates th17-cell pathogenicity in autoimmune uveitis via id2/pim1 axis. Journal of Neuroinflammation, Jun 2023. URL: https://doi.org/10.1186/s12974-023-02829-3, doi:10.1186/s12974-023-02829-3. This article has 34 citations and is from a peer-reviewed journal.

10. (zhu2024beneficialmechanismsof pages 1-2): Lei Zhu, He Li, Xuening Peng, Zhaohuai Li, Sichen Zhao, Dongting Wu, Jialing Chen, Si Li, Renbing Jia, Zuohong Li, and Wenru Su. Beneficial mechanisms of dimethyl fumarate in autoimmune uveitis: insights from single-cell rna sequencing. Journal of Neuroinflammation, 21:1-18, Apr 2024. URL: https://doi.org/10.1186/s12974-024-03096-6, doi:10.1186/s12974-024-03096-6. This article has 14 citations and is from a peer-reviewed journal.

11. (paley2024mucosalsignaturesof pages 1-2): Michael A. Paley, Xinbo Yang, Lynn M. Hassman, Frank Penkava, Lee I. Garner, Grace L. Paley, Nicole Linskey, Ryan Agnew, Paulo Henrique Arantes de Faria, Annie Feng, Sophia Y. Li, Davide Simone, Elisha D.O. Roberson, Philip A. Ruzycki, Ekaterina Esaulova, Jennifer Laurent, Lacey Feigl-Lenzen, Luke E. Springer, Chang Liu, Geraldine M. Gillespie, Paul Bowness, K. Christopher Garcia, and Wayne M. Yokoyama. Mucosal signatures of pathogenic t cells in hla-b*27+ anterior uveitis and axial spondyloarthritis. Jul 2024. URL: https://doi.org/10.1172/jci.insight.174776, doi:10.1172/jci.insight.174776. This article has 30 citations and is from a domain leading peer-reviewed journal.

12. (wang2024automatedearlydetection pages 1-2): Yuqin Wang, Zijian Yang, Xingneng Guo, Wang Jin, Dan Lin, Anying Chen, and Meng Zhou. Automated early detection of acute retinal necrosis from ultra-widefield color fundus photography using deep learning. Eye and Vision, Aug 2024. URL: https://doi.org/10.1186/s40662-024-00396-z, doi:10.1186/s40662-024-00396-z. This article has 9 citations and is from a peer-reviewed journal.

13. (NCT06431373 chunk 1):  A Study of Brepocitinib in Adults With Active, Non-Infectious, Non-Anterior Uveitis. Priovant Therapeutics, Inc.. 2024. ClinicalTrials.gov Identifier: NCT06431373

14. (wilson2023systemicadministrationof pages 1-2): Leslie Wilson, Katherine E. Lewis, Lawrence S. Evans, Stacey R. Dillon, and Kathryn L. Pepple. Systemic administration of acazicolcept, a dual cd28 and inducible t cell costimulator inhibitor, ameliorates experimental autoimmune uveitis. Mar 2023. URL: https://doi.org/10.1167/tvst.12.3.27, doi:10.1167/tvst.12.3.27. This article has 4 citations and is from a peer-reviewed journal.

15. (rosenbaum2018theeyeshave pages 10-14): James T. Rosenbaum and Andrew D. Dick. The eyes have it. Arthritis & Rheumatology, 70:1533-1543, Aug 2018. URL: https://doi.org/10.1002/art.40568, doi:10.1002/art.40568. This article has 67 citations and is from a highest quality peer-reviewed journal.

16. (chang2021uveitisinchildren pages 1-3): Margaret H. Chang, Jessica G. Shantha, Jacob J. Fondriest, Mindy S. Lo, and Sheila T. Angeles-Han. Uveitis in children and adolescents. Rheumatic diseases clinics of North America, 47 4:619-641, Nov 2021. URL: https://doi.org/10.1016/j.rdc.2021.07.005, doi:10.1016/j.rdc.2021.07.005. This article has 57 citations.

17. (NCT06310837 chunk 1):  Effect of Immunosuppressants With Adalimumab Biosimilars vs Corticosteroids on Noninfectious Uveitis. Zhongshan Ophthalmic Center, Sun Yat-sen University. 2024. ClinicalTrials.gov Identifier: NCT06310837

18. (hoffmann2022preactivatedgranulocytesfrom pages 1-3): Anne L. C. Hoffmann, Stefanie M. Hauck, Cornelia A. Deeg, and Roxane L. Degroote. Pre-activated granulocytes from an autoimmune uveitis model show divergent pathway activation profiles upon il8 stimulation in vitro. International Journal of Molecular Sciences, 23:9555, Aug 2022. URL: https://doi.org/10.3390/ijms23179555, doi:10.3390/ijms23179555. This article has 9 citations.

19. (trivedi2019theuseof pages 1-3): Amruta Trivedi and Constance Katelaris. The use of biologic agents in the management of uveitis. Internal Medicine Journal, 49:1352-1363, Nov 2019. URL: https://doi.org/10.1111/imj.14215, doi:10.1111/imj.14215. This article has 46 citations and is from a peer-reviewed journal.

20. (OpenTargets Search: uveitis): Open Targets Query (uveitis, 18 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

21. (NCT02595398 chunk 1):  Suprachoroidal Injection of CLS-TA in Subjects With Macular Edema Associated With Non-infectious Uveitis. Clearside Biomedical, Inc.. 2015. ClinicalTrials.gov Identifier: NCT02595398

22. (NCT05486468 chunk 1):  The Use of Two YUTIQ Versus Sham for Treatment of Chronic Non Infectious Intraocular Inflammation Affecting the Posterior Segment. Texas Retina Associates. 2022. ClinicalTrials.gov Identifier: NCT05486468

23. (NCT05384249 chunk 1):  Phase 2b Pivotal Study of Izokibep in Non-infectious, Intermediate-, Posterior- or Pan-uveitis. ACELYRIN Inc.. 2022. ClinicalTrials.gov Identifier: NCT05384249

24. (asghar2024“infectiousuveitisa pages 14-15): Muhammad Arif Asghar, Shixin Tang, Li Ping Wong, Peizeng Yang, and Qinjian Zhao. “infectious uveitis: a comprehensive systematic review of emerging trends and molecular pathogenesis using network analysis”. Journal of Ophthalmic Inflammation and Infection, Nov 2024. URL: https://doi.org/10.1186/s12348-024-00444-8, doi:10.1186/s12348-024-00444-8. This article has 24 citations and is from a peer-reviewed journal.

25. (golubenco2024biomarkersofuveitis pages 1-3): Elena GOLUBENCO, Elena DOLAPCIU, Olga GAIDARJI, Lucia MAZUR-NICORICI, and Ninel REVENCO. Biomarkers of uveitis in juvenile idiopathic arthritis: a systematic review. Archives of the Balkan Medical Union, 59(4):415-424, Dec 2024. URL: https://doi.org/10.31688/abmu.2024.59.4.12, doi:10.31688/abmu.2024.59.4.12. This article has 1 citations.

26. (golubenco2024biomarkersofuveitis pages 10-10): Elena GOLUBENCO, Elena DOLAPCIU, Olga GAIDARJI, Lucia MAZUR-NICORICI, and Ninel REVENCO. Biomarkers of uveitis in juvenile idiopathic arthritis: a systematic review. Archives of the Balkan Medical Union, 59(4):415-424, Dec 2024. URL: https://doi.org/10.31688/abmu.2024.59.4.12, doi:10.31688/abmu.2024.59.4.12. This article has 1 citations.

## Artifacts

- [Edison artifact artifact-00](Uveitis-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 16 |
| Resolved | 16 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 16 |
| On topic | 6 |
| Off topic | 0 |

All extracted references resolved successfully.