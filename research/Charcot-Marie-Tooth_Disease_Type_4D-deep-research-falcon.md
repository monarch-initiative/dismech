---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-27T15:36:34.851807'
end_time: '2026-08-27T15:44:20.145011'
duration_seconds: 465.29
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Charcot-Marie-Tooth disease type 4D
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 15
reference_validation:
  total_references: 12
  verified: 11
  not_found: 0
  unverifiable: 1
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 5
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Charcot-Marie-Tooth_Disease_Type_4D-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Charcot-Marie-Tooth disease type 4D
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Charcot-Marie-Tooth disease type 4D** covering all of the
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
- **Disease Name:** Charcot-Marie-Tooth disease type 4D
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Charcot-Marie-Tooth disease type 4D** covering all of the
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


# Charcot–Marie–Tooth disease type 4D (CMT4D/HMSN-Lom): comprehensive disease-characteristics report

## Executive summary and evidence scope

Charcot–Marie–Tooth disease type 4D (CMT4D), historically called **hereditary motor and sensory neuropathy–Lom (HMSN-Lom)**, is a rare, childhood-onset, autosomal-recessive demyelinating neuropathy caused by biallelic pathogenic variants in **NDRG1**. It produces progressive distal weakness and wasting, sensory loss, areflexia, severe slowing of nerve conduction, foot and hand deformities, and frequently later-onset sensorineural hearing loss. The strongest human evidence comes from Romani founder families and small case series; mechanistic evidence comes principally from Ndrg1-null mice and Schwann-cell studies. Open Targets links MONDO:0011085 to NDRG1 using five evidence records, including PMID 10831399, the landmark causal-gene report. (OpenTargets Search: Charcot-Marie-Tooth disease type 4D-NDRG1)

No CMT4D-specific disease-modifying treatment or credible subtype-specific interventional trial was identified. Contemporary implementation therefore consists of genetic diagnosis, multidisciplinary rehabilitation, orthotic/orthopedic management, hearing surveillance and support, and genetic counseling. Because this ultra-rare subtype has few modern cohorts, many requested statistics—incidence, survival, penetrance, carrier frequency outside founder populations, and phenotype percentages—remain unknown rather than zero.

The following table gives a compact knowledge-base summary.

| Domain | Key finding | Evidence type | Disease specificity | Key citations / URLs |
|---|---|---|---|---|
| Identity / identifiers | Charcot-Marie-Tooth disease type 4D (CMT4D) is the same entity as hereditary motor and sensory neuropathy-Lom (HMSN-Lom), an autosomal-recessive demyelinating peripheral neuropathy associated with later hearing loss; Open Targets lists MONDO_0011085 and a disease-target association with **NDRG1**. | Aggregated disease resource + human clinical literature | Subtype-specific | MONDO_0011085; Open Targets disease-target association for NDRG1 (OpenTargets Search: Charcot-Marie-Tooth disease type 4D-NDRG1). Clinical nomenclature and subtype summary in review excerpt (nam2019clinicalandgenetic pages 13-15). |
| Causal gene / inheritance | Causal gene: **NDRG1** (N-myc downstream regulated 1; ENSG00000104419). Inheritance is **autosomal recessive**; affected individuals typically carry homozygous or biallelic pathogenic variants. | Aggregated disease resource + human clinical literature | Subtype-specific | Open Targets evidence links CMT4D to NDRG1 and literature PMIDs 10831399, 20301641, 28776325 (OpenTargets Search: Charcot-Marie-Tooth disease type 4D-NDRG1). Review summary: homozygous NDRG1 variants on 8q24 cause CMT4D (nam2019clinicalandgenetic pages 13-15). |
| Founder variant | The best-known founder allele is the **Lom mutation** in **NDRG1**, historically reported as **p.R148X / p.Arg148Ter** (older protein nomenclature also **P148X** appears in review text), enriched in Romani populations from Bulgaria and other European countries. | Human founder-population genetics + review | Subtype-specific | Refined mapping in Romani families: Chandler et al., *Neuromuscul Disord* 2000, DOI: https://doi.org/10.1016/S0960-8966(00)00148-6 (муртазина2019современныеклиникогенетическиепредставленияa pages 12-13, муртазина2019современныеклиникогенетическиепредставления pages 12-13). Review excerpt notes p.P148X as most common mutation (jiang2022aberrantneuregulin1erbb pages 1-2). |
| Hallmark phenotype / timeline | Typical onset is in the **first decade of life** with distal lower-limb weakness, gait difficulty, foot deformities, distal sensory loss, hyporeflexia/areflexia, and progression to hand/upper-limb involvement; **deafness commonly appears in the 3rd decade**. | Human clinical literature + review | Subtype-specific | “Onset occurs in the first decade of life” and deafness often develops in the third decade (nam2019clinicalandgenetic pages 13-15). 2022 mechanistic paper summarizes early-onset progressive motor and sensory neuropathy with distal weakness, skeletal/foot deformities, and sensorineural hearing loss (jiang2022aberrantneuregulin1erbb pages 1-2). |
| Electrophysiology / pathology | Nerve conduction velocities are **severely reduced** and may become unattainable. Nerve biopsy shows **marked depletion of myelinated fibers**, **thin myelin sheaths**, **segmental demyelination/remyelination**, **axonal loss**, and **onion bulb formations**; abnormal brainstem auditory evoked potentials have been reported. | Human clinical literature + pathology | Subtype-specific | Review excerpt on CMT4D findings (nam2019clinicalandgenetic pages 13-15). 2022 paper summary reports sural nerve biopsy with myelinated fiber loss, thin myelin, and onion bulbs (jiang2022aberrantneuregulin1erbb pages 1-2). |
| Mechanism | Current model centers on **Schwann-cell dysfunction and demyelination**. In Ndrg1 deficiency, total **ErbB2/ErbB3** receptor levels are increased but **phosphorylated ErbB2/3** and downstream signaling are decreased; **neuregulin-1** is increased and **integrin β4** is reduced, supporting impaired **neuregulin-1/ErbB signaling** as a contributor to failed myelination/maintenance. NDRG1 is also linked to membrane/lipid binding and vesicular trafficking in broader literature. | Mouse model + mechanistic molecular study | Subtype-specific core mechanism; trafficking/lipid-binding context is broader NDRG1 biology | Jiang et al., 2022, *Mol Cell Biol* 42(7), DOI: https://doi.org/10.1128/mcb.00559-21 (jiang2022aberrantneuregulin1erbb pages 1-2). Structural/biophysical context: Mustonen et al., 2021, DOI: https://doi.org/10.1111/febs.15660 (paper-search result, not directly citeable here). |
| Model organisms | **Ndrg1-deficient mouse** models develop **early progressive demyelinating neuropathy** and limb muscle weakness, supporting a causal role for NDRG1 loss in peripheral nerve myelin maintenance. | Model organism | Subtype-specific | Mouse phenotype summarized in 2022 mechanistic study (jiang2022aberrantneuregulin1erbb pages 1-2) and in review excerpt citing Ndrg1-deficient mice with progressive demyelinating peripheral nerve disorder (муртазина2019современныеклиникогенетическиепредставленияa pages 12-13). |
| Diagnosis | Diagnosis is based on phenotype (early-onset demyelinating neuropathy with later hearing loss), **electrophysiology**, and **molecular confirmation of NDRG1 variants**. In practice, this is usually achieved through hereditary neuropathy multigene panels, WES, or WGS rather than single-modality testing alone. | Human clinical literature + general CMT diagnostic practice | Subtype-specific phenotype; testing strategy partly general-CMT evidence | Subtype clues and electrophysiology/pathology from CMT4D review excerpt (nam2019clinicalandgenetic pages 13-15). Broader importance of accurate genetic diagnosis in CMT emphasized in general review DOI: https://doi.org/10.23838/pfm.2018.00163 (nam2019clinicalandgenetic pages 13-15). |
| Treatment / management | **No subtype-specific disease-modifying therapy is established** for CMT4D. Management is supportive: physical/occupational therapy, orthoses/AFOs, hearing assessment and aids, pain/symptom control, and orthopedic surgery for severe deformity when needed. Broader CMT trial activity is increasing, but available evidence is largely not CMT4D-specific. | General CMT management / trials literature | Mostly general-CMT evidence; supportive care is applicable to CMT4D | General CMT trial landscape: Nair et al., 2023, DOI: https://doi.org/10.3389/fneur.2023.1251885. General rehabilitation: Coraci et al., 2023, DOI: https://doi.org/10.3390/jcm12185879. These are general-CMT/peripheral-neuropathy rather than subtype-specific evidence. |
| Epidemiology / population | CMT4D is **rare globally** but shows a strong **founder effect in Romani populations**, especially those originally described in Bulgaria and later across several European countries. Robust population prevalence/incidence estimates specific to CMT4D are not well established in accessible sources. | Human population genetics + review | Subtype-specific founder distribution; prevalence gap remains | Chandler et al. founder mapping in Romani families across Europe, DOI: https://doi.org/10.1016/S0960-8966(00)00148-6 (муртазина2019современныеклиникогенетическиепредставленияa pages 12-13, муртазина2019современныеклиникогенетическиепредставления pages 12-13). Review notes first description in Bulgarian Romani population (nam2019clinicalandgenetic pages 13-15). |
| Key evidence gaps | Missing or limited accessible data include: precise **ICD/Orphanet/MeSH/OMIM crosswalks**, validated **population prevalence/incidence**, **carrier frequency** estimates outside founder groups, quantified **phenotype frequencies** from large cohorts, proven **modifier genes**, **gene-environment interactions**, biomarkers, natural-history survival data, and **subtype-specific interventional trials**. | Evidence synthesis | Subtype-specific gaps | Gaps inferred from available disease-specific evidence being limited to founder cohorts, reviews, and mechanistic mouse studies (OpenTargets Search: Charcot-Marie-Tooth disease type 4D-NDRG1, jiang2022aberrantneuregulin1erbb pages 1-2, муртазина2019современныеклиникогенетическиепредставленияa pages 12-13, nam2019clinicalandgenetic pages 13-15, муртазина2019современныеклиникогенетическиепредставления pages 12-13). |


*Table: This table summarizes the most actionable disease-knowledge-base facts for Charcot-Marie-Tooth disease type 4D/HMSN-Lom, distinguishing subtype-specific evidence from broader CMT literature. It is useful for quickly identifying established findings, translational implications, and current data gaps.*

## 1. Disease information

### Definition and classification

CMT4D is a **Mendelian, autosomal-recessive, predominantly demyelinating hereditary motor and sensory neuropathy**. It belongs to the recessive CMT4 group and affects the peripheral motor and sensory nerves; auditory neuropathy/sensorineural hearing impairment is an important syndromic feature. The disease was initially delineated in Bulgarian Romani families and subsequently mapped in Romani families from several European countries. (муртазина2019современныеклиникогенетическиепредставленияa pages 12-13, nam2019clinicalandgenetic pages 13-15)

**Synonyms:**

- Charcot–Marie–Tooth disease type 4D; CMT4D
- Hereditary motor and sensory neuropathy–Lom; HMSN-Lom; HMSNL
- Lom-type hereditary motor and sensory neuropathy
- NDRG1-related demyelinating neuropathy
- Peripheral neuropathy, motor and sensory, with hearing loss, NDRG1-related

**Identifiers and cross-references:**

- **MONDO:** MONDO:0011085, Charcot–Marie–Tooth disease type 4D. (OpenTargets Search: Charcot-Marie-Tooth disease type 4D-NDRG1)
- **OMIM phenotype:** commonly cross-referenced as CMT4D/HMSN-Lom, **OMIM 601455**; **NDRG1 OMIM 605262**. These identifiers should be validated against the live OMIM record before automated ingestion.
- **Gene:** NDRG1; Ensembl ENSG00000104419. (OpenTargets Search: Charcot-Marie-Tooth disease type 4D-NDRG1)
- **Orphanet:** generally represented under rare hereditary motor and sensory neuropathy/CMT4 classifications; a stable subtype-specific ORPHA number was not established from the retrieved primary evidence.
- **ICD-10:** no dedicated CMT4D code; typically coded under G60.0, hereditary motor and sensory neuropathy.
- **ICD-11:** classified under hereditary neuropathies rather than a reliably subtype-specific billable code.
- **MeSH:** Charcot-Marie-Tooth Disease; no separate CMT4D MeSH descriptor was established.

The information summarized here is **aggregated disease-level evidence** from publications and curated resources, not individual-level EHR data. Some original publications describe individual patients or pedigrees, but no patient-level records were accessed.

## 2. Etiology, risk, protection, and environment

### Primary cause

The necessary cause is **biallelic germline pathogenic variation in NDRG1**, usually producing loss of NDRG1 function. Open Targets identifies NDRG1 as the sole associated target in its CMT4D record. (OpenTargets Search: Charcot-Marie-Tooth disease type 4D-NDRG1)

The best-known founder allele is the **Lom nonsense variant**, conventionally reported as **p.Arg148Ter (p.R148X)**. One retrieved review rendered the common allele as “p.P148X”; because that conflicts with the established Arg148Ter notation, the genomic/transcript-level HGVS should be checked against the chosen MANE transcript before database loading. The 2022 review reports ten distinct disease-associated mutations and identifies this early stop allele as the most common. (jiang2022aberrantneuregulin1erbb pages 1-2)

Other reported NDRG1 disease alleles include nonsense, missense, frameshift, and splice-altering variants. A 2023 Iranian 80-gene-panel study reported a novel splice-region variant, **c.205+1delG**, in a patient classified as CMT4D, illustrating that the disorder is not restricted to the Lom founder allele. Classification and population frequency must be assigned variant by variant using current ClinVar/gnomAD and transcript data rather than inferred from the disease label.

### Risk factors

- **Genetic:** two pathogenic NDRG1 alleles; carrier parents; affected siblings; consanguinity; and ancestry from a founder population increase prior probability.
- **Family history:** because inheritance is recessive, family history may be absent, and affected siblings can occur with unaffected parents.
- **Population:** Romani ancestry is an ascertainment clue, not a diagnostic requirement. The founder haplotype has been demonstrated across multiple European Romani populations. (муртазина2019современныеклиникогенетическиепредставленияa pages 12-13, муртазина2019современныеклиникогенетическиепредставления pages 12-13)
- **Sex:** males and females are expected to be affected equally.
- **Age:** age changes clinical expression, not inherited risk; neuropathy usually becomes evident in childhood, while deafness often appears later. (nam2019clinicalandgenetic pages 13-15)

No reproducible environmental cause, infectious trigger, susceptibility locus, modifier gene, or sex-specific risk has been established for CMT4D. No validated genetic or environmental protective factor is known. Data do not support diet, smoking, alcohol, occupation, radiation, pollution, or infection as primary etiologic factors.

### Gene–environment considerations

Clinical practice should distinguish causation from aggravation. Neurotoxic drugs, major immobility, injury, and poorly fitted footwear could plausibly worsen function in an existing neuropathy, as in other CMT forms, but subtype-specific gene–environment studies are absent. Avoiding neurotoxic exposure is therefore prudent supportive practice, not proven CMT4D prevention.

## 3. Phenotypes

Published descriptions consistently support a severe, length-dependent motor-sensory neuropathy, but sufficiently large cohorts for reliable percentages are unavailable.

| Phenotype | Type, timing, course, and impact | Suggested HPO term |
|---|---|---|
| Distal lower-limb weakness | Clinical sign; first decade; progressive; initially feet/legs; causes tripping and impaired walking | Distal muscle weakness, HP:0002460 |
| Distal muscle atrophy | Sign; progressive, lower limbs before hands; reduces endurance and dexterity | Muscle atrophy, HP:0003202 |
| Gait abnormality/foot drop | Sign and functional manifestation; childhood onward; progressive fall risk | Abnormal gait, HP:0001288; Foot drop, HP:0003376 |
| Pes cavus/equinovarus | Musculoskeletal manifestation; develops with muscle imbalance; footwear and mobility burden | Pes cavus, HP:0001761; Talipes equinovarus, HP:0001762 |
| Hand weakness/deformity | Later motor manifestation following lower-limb disease; impairs writing, dressing, and fine motor tasks | Distal upper-limb muscle weakness, HP:0008954 |
| Distal sensory loss | Sign/symptom; progressive; affects touch, vibration, pain, and proprioception; increases unnoticed-injury risk | Distal sensory impairment, HP:0002936; Impaired vibration sensation, HP:0002495 |
| Hyporeflexia/areflexia | Neurologic sign; common and progressive | Areflexia, HP:0001284; Hyporeflexia, HP:0001265 |
| Sensorineural hearing loss/auditory neuropathy | Usually later than motor disease, often becoming evident in the third decade; communication and educational impact | Sensorineural hearing impairment, HP:0000407; Hearing impairment, HP:0000365 |
| Severely reduced nerve-conduction velocity | Electrophysiologic abnormality; may eventually be unrecordable | Reduced motor nerve conduction velocity, HP:0003431 |
| Demyelination/onion bulbs | Pathologic sign; chronic demyelination and remyelination | Segmental peripheral demyelination, HP:0003481 |

The characteristic sequence is lower-limb onset followed by upper-limb involvement; deafness often develops in the third decade. Nerve conduction can become so severely impaired that responses are unobtainable. Sural-nerve pathology includes loss of myelinated fibers, thin myelin, segmental demyelination/remyelination, axonal loss, and onion-bulb formations. Abnormal brainstem auditory evoked responses support auditory pathway involvement. (jiang2022aberrantneuregulin1erbb pages 1-2, nam2019clinicalandgenetic pages 13-15)

Reports of broader central nervous system involvement exist, but the core phenotype is peripheral neuropathy with hearing impairment; CNS findings should not be treated as universally present. (муртазина2019современныеклиникогенетическиепредставленияa pages 12-13)

No CMT4D-specific EQ-5D, SF-36, PROMIS, or validated quality-of-life cohort was retrieved. Nevertheless, progressive mobility loss, falls, deformity, loss of hand function, sensory injury, and hearing impairment predict substantial effects on education, work, communication, independence, and social participation.

## 4. Genetic and molecular information

### Gene and variation

- **Gene:** NDRG1, N-myc downstream regulated 1; chromosome **8q24**; ENSG00000104419. (OpenTargets Search: Charcot-Marie-Tooth disease type 4D-NDRG1, nam2019clinicalandgenetic pages 13-15)
- **Inheritance/origin:** autosomal-recessive, constitutional **germline**; not a somatic cancer disorder.
- **Functional class:** disease is best modeled as **loss of function**, reducing the Schwann-cell functions needed for peripheral myelin development or maintenance.
- **Variant classes:** nonsense, splice-disrupting, frameshift, and missense alleles have been reported; pathogenicity must be assessed under ACMG/AMP criteria using segregation, population frequency, phenotype, predicted molecular consequence, and functional evidence.
- **Population frequency:** severe CMT4D alleles are expected to be rare in global population databases. The Lom allele is enriched by a Romani founder effect, but a defensible universal carrier frequency was not found.

No validated modifier gene, protective allele, disease-specific methylation signature, histone abnormality, repeat expansion, aneuploidy, translocation, or recurrent large chromosomal rearrangement is established. CMA, karyotyping, FISH, mitochondrial sequencing, and repeat-expansion assays are therefore not first-line subtype tests unless the broader phenotype supplies another indication.

## 5. Environmental information

CMT4D is not an infectious, toxic, nutritional, occupational, or lifestyle-mediated disease. No pathogen, zoonotic agent, radiation exposure, pollutant, dietary deficiency, alcohol exposure, or smoking association is established. Exercise and rehabilitation can preserve function but do not prevent inheritance or correct NDRG1 deficiency. Clinicians should apply general hereditary-neuropathy precautions concerning foot injury and potentially neurotoxic medications.

## 6. Mechanism and pathophysiology

### Causal chain

**Biallelic NDRG1 loss** → defective NDRG1-dependent membrane/vesicular and receptor-regulatory functions in myelinating Schwann cells → reduced productive neuregulin-1/ErbB2/ErbB3 signaling despite increased ligand and total receptors → disturbed expression of myelination regulators such as SOX10, OCT6/POU3F1, and EGR2 → inadequate myelin formation or maintenance → repeated demyelination/remyelination, thin myelin and onion bulbs → severe conduction slowing/block → chronic axonal loss → distal weakness, atrophy, sensory loss and deformity. Auditory nerve/pathway involvement produces later hearing impairment. (jiang2022aberrantneuregulin1erbb pages 1-2)

In Ndrg1-deficient sciatic nerve, total ErbB2/ErbB3 and neuregulin-1 are increased, yet phosphorylated ErbB2/3 and downstream signaling are decreased; integrin β4, a positive collaborator of ErbB signaling, is significantly reduced. The authors’ abstract-level conclusion was that the demyelinating phenotype is “at least in part a consequence of molecular defects in neuregulin 1/ErbB signaling.” This is strong model-organism mechanistic evidence but does not establish that this is the only human pathway. (jiang2022aberrantneuregulin1erbb pages 1-2)

### Cellular, tissue, and molecular annotations

- **Primary cell:** myelinating Schwann cell — CL:0002573; broader Schwann cell — CL:0000218.
- **Secondary cell:** peripheral sensory and motor neurons/axons; axonal loss is probably downstream of chronic glial dysfunction.
- **Suggested GO biological processes:** peripheral nervous system myelination (GO:0022011); axon ensheathment (GO:0008366); regulation of receptor tyrosine kinase signaling (GO:0050769); vesicle-mediated transport (GO:0016192); neuron–glial cell signaling.
- **Suggested GO molecular functions/processes:** lipid binding (GO:0008289); protein binding; ErbB signaling pathway (GO:0038127).
- **Suggested GO cellular components:** Schwann-cell plasma membrane, cytoplasm, vesicle, myelin sheath (GO:0043209).
- **Metabolism/immune system:** no validated CMT4D metabolomic, lipidomic, inflammatory, autoimmune, or immunodeficiency signature. NDRG1 has broader stress-response and lipid/membrane biology, but these findings should not be overinterpreted as human clinical biomarkers.

No CMT4D-specific human single-cell atlas, spatial-transcriptomic dataset, multi-omic diagnostic classifier, CRISPR screen, circulating proteomic signature, or metabolomic biomarker was found. The most informative molecular profiling currently consists of targeted expression/signaling analysis in mutant mouse nerve.

## 7. Anatomical structures affected

- **Organ/system:** peripheral nervous system, especially long motor and sensory nerves; auditory nerve/brainstem auditory pathway.
- **Anatomic distribution:** bilateral, length-dependent and usually symmetric; distal legs and feet precede hands and forearms.
- **Tissues:** peripheral nerve, Schwann-cell myelin, axons, and secondarily denervated skeletal muscle.
- **Representative UBERON suggestions:** peripheral nerve, UBERON:0001780; sciatic nerve, UBERON:0001322; sural nerve; skeletal muscle tissue, UBERON:0001134; inner ear, UBERON:0001846.
- **Subcellular structures:** plasma membrane/receptor complexes, vesicular compartments, cytoplasm, and the compact/noncompact myelin apparatus.

The disease is not primarily a muscle disease: muscle wasting is downstream of peripheral denervation. Sural-nerve biopsy findings and the sciatic-nerve mouse phenotype directly support peripheral-nerve localization. (jiang2022aberrantneuregulin1erbb pages 1-2, nam2019clinicalandgenetic pages 13-15)

## 8. Temporal development

Onset is usually **chronic and insidious in the first decade**, beginning with distal leg/foot weakness and gait difficulty. Weakness, sensory impairment, and skeletal deformity progress over years to involve upper limbs. Hearing impairment is frequently delayed until adolescence or the third decade. (jiang2022aberrantneuregulin1erbb pages 1-2, nam2019clinicalandgenetic pages 13-15)

CMT4D is lifelong and progressive, not episodic or relapsing-remitting. There is no recognized spontaneous remission. Childhood—before fixed deformity and major axonal loss—is the logical window for rehabilitation and any future molecular therapy, although a disease-specific therapeutic window has not been empirically defined.

## 9. Inheritance and population

For two carrier parents, each pregnancy has a **25% probability of an affected child, 50% probability of an unaffected carrier, and 25% probability of a child inheriting neither familial allele**. Both sexes are affected.

The disorder has a marked founder history in Romani populations, initially Bulgaria and subsequently several European countries. The multicountry mapping study is Chandler et al., *Neuromuscular Disorders*, December 2000, DOI: https://doi.org/10.1016/S0960-8966(00)00148-6; PMID 11053686. The original clinical delineation, “Hereditary motor and sensory neuropathy-Lom, a novel demyelinating neuropathy associated with deafness in Gypsies,” appeared in *Brain* in March 1998; PMID 9549516. (муртазина2019современныеклиникогенетическиепредставленияa pages 12-13)

No robust CMT4D-specific prevalence per 100,000, annual incidence, global carrier frequency, age distribution, or sex ratio has been established. Penetrance is generally presumed high for biallelic severe loss-of-function alleles, but formal age-dependent penetrance estimates are unavailable. Expressivity is variable, especially the timing/severity of hearing loss. Anticipation is not expected because CMT4D is not a repeat-expansion disease. Germline mosaicism is theoretically possible but not established as a recurring phenomenon. Consanguinity can increase the probability of biallelic disease alleles.

## 10. Diagnostics

### Clinical and neurophysiologic work-up

1. Document a three-generation pedigree, ancestry, age at onset, gait/falls, hearing, and neurotoxic exposures.
2. Neurologic examination: distal strength and wasting, reflexes, sensory modalities, gait, balance, and foot/hand deformity.
3. Nerve-conduction studies and EMG: expected severe demyelinating-range slowing, low amplitudes when axonal loss is advanced, and potentially unobtainable responses. (nam2019clinicalandgenetic pages 13-15)
4. Audiology: pure-tone testing, speech discrimination, otoacoustic emissions as appropriate, and auditory brainstem responses when auditory neuropathy is suspected.
5. Nerve biopsy is rarely required after molecular diagnosis. Historical pathology shows thin myelin, severe myelinated-fiber depletion, onion bulbs, demyelination/remyelination, and axonal loss. (jiang2022aberrantneuregulin1erbb pages 1-2, nam2019clinicalandgenetic pages 13-15)
6. MRI is not diagnostic but may evaluate atypical CNS findings, spine disease, or alternative causes.

### Genetic testing strategy

A hereditary-neuropathy multigene panel that includes **NDRG1** is usually the efficient first molecular test after common CMT causes are considered. Testing should detect single-nucleotide variants, small indels, splice variants, and ideally exon-level copy-number changes. If panel testing is negative, trio WES or WGS can identify rare/novel alleles; RNA analysis from an informative tissue may clarify splice variants. Sanger sequencing is appropriate for familial-variant confirmation, segregation, and cascade testing. Targeted founder-variant testing can be efficient in an appropriate Romani family but should not replace broader sequencing when negative.

Molecular diagnosis requires pathogenic/likely pathogenic variants on both alleles in trans. A single heterozygous NDRG1 variant or a VUS does not confirm CMT4D.

### Differential diagnosis

Important alternatives include PMP22-related CMT1A, GJB1-related CMTX1, MPZ-related neuropathy, and recessive demyelinating neuropathies due to SH3TC2, GDAP1, MTMR2, SBF2, PRX, and FGD4. Hearing loss also raises MPZ, PMP22, NEFL, GJB1 and other syndromic neuropathies. Acquired chronic inflammatory demyelinating polyneuropathy is distinguished by tempo, inflammatory studies, conduction pattern, treatment response, pedigree, and genetic findings. Distal hereditary motor neuropathy, spinal muscular atrophy, Friedreich ataxia, mitochondrial disease, and treatable metabolic neuropathies should be considered when sensory or systemic findings differ.

There is no population newborn-screening program. **Cascade testing** of relatives is the practical screening method. Prenatal diagnosis and preimplantation genetic testing are possible after the familial pathogenic variants are known.

## 11. Outcome and prognosis

CMT4D causes chronic morbidity rather than a defined acute mortality syndrome. Expected burdens include progressive walking difficulty, falls, fixed cavovarus deformity, hand dysfunction, sensory injury, communication impairment from deafness, and possible need for mobility or hearing devices. Recovery of established axonal loss is limited; supportive interventions can improve safety and function but do not reverse the genotype.

No reliable CMT4D-specific five- or ten-year survival, mortality rate, life-expectancy estimate, longitudinal disability curve, or validated prognostic biomarker was identified. Disease-specific prognosis is probably influenced by genotype, childhood severity, degree of axonal loss, deformity, hearing involvement, and access to rehabilitation, but formal prediction models do not exist.

## 12. Treatment and current applications

### Established management

There is **no approved NDRG1-directed pharmacotherapy**. Current care is multidisciplinary:

- physical therapy: low-to-moderate intensity strengthening, stretching, balance, gait and endurance training while avoiding overwork injury;
- occupational therapy and adaptive devices for hand weakness and daily activities;
- custom footwear, insoles, and ankle–foot orthoses for foot drop, instability and energy-efficient gait;
- orthopedic evaluation for progressive cavovarus/equinovarus, tendon imbalance, contracture, or scoliosis; selected patients may need tendon transfer, osteotomy, or fusion;
- pain management directed to neuropathic or musculoskeletal pain;
- regular skin/foot inspection because sensory loss permits unnoticed injury;
- audiology, hearing aids and, in severe cases, assessment for cochlear implantation/auditory rehabilitation;
- school, vocational, psychosocial and communication support.

Suggested NCIt intervention concepts include Physical Therapy (C15302), Occupational Therapy, Orthotic Device, Hearing Aid, Cochlear Implantation, Genetic Counseling (C15241), and orthopedic surgery concepts. NCIt identifiers should be checked in the current release before ingestion.

### Experimental and recent therapeutic context

A 2023 analysis of the broader CMT trial landscape found 286 registered studies by 2022; 86% were therapeutic, including procedures, drugs, devices and physical therapy, while gene-therapy work remained predominantly preclinical. These figures describe **all CMT**, not CMT4D, and should not be represented as CMT4D trial counts. DOI: https://doi.org/10.3389/fneur.2023.1251885 (published September 2023).

The ClinicalTrials.gov search performed for this report returned no verified NDRG1/CMT4D-specific interventional trial; apparent hits were unrelated studies caused by nonspecific text matching. Thus, no NCT identifier can responsibly be assigned to a CMT4D therapy.

Conceptually, recessive NDRG1 loss is amenable to Schwann-cell-directed gene replacement, mRNA delivery, or pathway correction. However, no human efficacy or safety data exist. Manipulating NRG1/ErbB signaling is biologically plausible but complex because signaling dose and timing control myelin thickness and Schwann-cell state.

## 13. Prevention

Primary lifestyle prevention is impossible because the disorder is inherited. Effective reproductive prevention options require informed, nondirective genetic counseling:

- carrier and cascade testing for relatives;
- partner testing when one familial carrier is known;
- preimplantation genetic testing for monogenic disease;
- chorionic-villus sampling or amniocentesis for prenatal diagnosis;
- use of donor gametes or other reproductive choices.

Secondary prevention comprises early molecular diagnosis, childhood audiologic monitoring, early orthotic/rehabilitation intervention, and surveillance for deformity. Tertiary prevention includes fall prevention, contracture management, skin/foot care, hearing support, pain treatment, and timely orthopedic intervention. Vaccination, anti-infective prophylaxis, sanitation, and environmental remediation have no disease-specific role.

## 14. Other species and natural disease

No well-established naturally occurring veterinary homolog of human NDRG1-related CMT4D was identified in the retrieved literature. The disease is not transmissible or zoonotic. Orthologous NDRG1 genes are evolutionarily conserved in mammals and other vertebrates, enabling experimental modeling, but induced knockout phenotypes should not be mislabeled as spontaneous animal disease.

## 15. Model organisms and experimental systems

The principal disease model is the **Ndrg1-deficient mouse** (*Mus musculus*, NCBI Taxon 10090). An early model showed progressive demyelination of peripheral nerves (PMID 15082788). A newer knockout deleting exons 4–5 developed early progressive demyelinating neuropathy and limb weakness and reproduced abnormalities in myelin transcription factors and NRG1/ErbB signaling. (jiang2022aberrantneuregulin1erbb pages 1-2, муртазина2019современныеклиникогенетическиепредставленияa pages 12-13)

**Recapitulated features:** peripheral demyelination, thin/abnormal myelin, progressive weakness, altered Schwann-cell signaling, and myelination-regulator abnormalities.

**Applications:** defining Schwann-cell-autonomous mechanisms; temporal profiling of demyelination and axonal loss; testing NDRG1 replacement; and evaluating whether restoration of integrin β4/ErbB signaling rescues myelination.

**Limitations:** mouse lifespan and peripheral-nerve scale differ from humans; later human hearing loss and disability trajectory may not be fully reproduced; complete knockout may not model every hypomorphic missense/splice allele; and treatment timing or vector biodistribution may not translate directly.

Patient-derived fibroblasts, reprogrammed iPSCs, and differentiated Schwann-cell or sensory-neuron co-cultures would be valuable allele-specific systems, but no mature CMT4D organoid, zebrafish, Drosophila, or CRISPR-screen platform with validated human-phenotype recapitulation was identified.

## Recent developments and expert interpretation

The most disease-specific recent advance remains Jiang et al., published **July 2022**, DOI: https://doi.org/10.1128/mcb.00559-21. Its key contribution was moving CMT4D biology from a generic “myelin-maintenance defect” toward a testable Schwann-cell signaling model: NDRG1 deficiency uncouples abundant NRG1/ErbB components from effective receptor phosphorylation and downstream activity, possibly through reduced integrin β4. (jiang2022aberrantneuregulin1erbb pages 1-2)

No major CMT4D-specific 2023–2024 therapeutic or natural-history study was identified. The relevant 2023 development was broader: inherited-neuropathy panels continued to detect geographically diverse NDRG1 variants, while CMT research increasingly pursued gene-targeted approaches. Expert interpretation should therefore remain conservative: CMT4D is mechanistically promising for gene replacement, but present human care is supportive, and subtype-specific natural-history and biomarker studies are prerequisites for a credible therapeutic trial.

## Key primary literature and authoritative links

1. **Kalaydjieva et al.** Original HMSN-Lom clinical delineation. *Brain*. March 1998;121:399–408. PMID: **9549516**. PubMed: https://pubmed.ncbi.nlm.nih.gov/9549516/ (муртазина2019современныеклиникогенетическиепредставленияa pages 12-13)
2. **Chandler et al.** Refined mapping in European Romani families. *Neuromuscular Disorders*. December 2000;10:584–591. PMID: **11053686**. DOI: https://doi.org/10.1016/S0960-8966(00)00148-6 (муртазина2019современныеклиникогенетическиепредставленияa pages 12-13, муртазина2019современныеклиникогенетическиепредставления pages 12-13)
3. **Kalaydjieva et al.** NDRG1 identified as the causal gene. PMID: **10831399**. PubMed: https://pubmed.ncbi.nlm.nih.gov/10831399/ (OpenTargets Search: Charcot-Marie-Tooth disease type 4D-NDRG1)
4. **Okuda et al.** Ndrg1-deficient mice exhibit progressive peripheral demyelination. *Molecular and Cellular Biology*. 2004;24:3949–3956. PMID: **15082788**. PubMed: https://pubmed.ncbi.nlm.nih.gov/15082788/ (муртазина2019современныеклиникогенетическиепредставленияa pages 12-13)
5. **Jiang et al.** “Aberrant Neuregulin 1/ErbB Signaling in Charcot-Marie-Tooth Type 4D Disease.” *Molecular and Cellular Biology*. July 2022;42(7). DOI: https://doi.org/10.1128/mcb.00559-21 (jiang2022aberrantneuregulin1erbb pages 1-2)
6. **Luigetti et al.** Clinical, electrophysiological and pathological findings with the Lom mutation. *Journal of the Neurological Sciences*. October 2014;345:271–273. PMID: **25108819**. PubMed: https://pubmed.ncbi.nlm.nih.gov/25108819/ (муртазина2019современныеклиникогенетическиепредставленияa pages 12-13)

## Data-quality cautions for knowledge-base ingestion

Phenotype timing and pathology are well supported, but numerical phenotype frequencies cannot be assigned from the retrieved evidence. The MONDO–NDRG1 association is curated and supported by multiple genetic records. (OpenTargets Search: Charcot-Marie-Tooth disease type 4D-NDRG1) Variant HGVS, ClinVar status, gnomAD frequency, HGNC identifier, OMIM/Orphanet cross-references, and ontology identifiers should be programmatically revalidated against current database releases. The p.P148X rendering in one review conflicts with the accepted p.Arg148Ter/p.R148X Lom notation and should not be loaded without transcript-level confirmation. Finally, generalized CMT rehabilitation and trial statistics must be tagged as indirect evidence rather than CMT4D-specific efficacy data.

References

1. (OpenTargets Search: Charcot-Marie-Tooth disease type 4D-NDRG1): Open Targets Query (Charcot-Marie-Tooth disease type 4D-NDRG1, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (nam2019clinicalandgenetic pages 13-15): Soo Hyun Nam and Byung-Ok Choi. Clinical and genetic aspects of charcot-marie-tooth disease subtypes. Jun 2019. URL: https://doi.org/10.23838/pfm.2018.00163, doi:10.23838/pfm.2018.00163. This article has 45 citations.

3. (муртазина2019современныеклиникогенетическиепредставленияa pages 12-13): АФ Муртазина, ОА Щагина, and СС Никитин. Современные клиникогенетические представления об аутосомнорецессивных наследственных периферических нейропатиях. Unknown journal, 2019.

4. (муртазина2019современныеклиникогенетическиепредставления pages 12-13): АФ Муртазина, ОА Щагина, and СС Никитин. Современные клиникогенетические представления об аутосомнорецессивных наследственных периферических нейропатиях. Unknown journal, 2019.

5. (jiang2022aberrantneuregulin1erbb pages 1-2): Li-Ting Jiang, Yu-Hui Chen, Jie-Hong Huang, Wei-Fang Tong, Ling-Jing Jin, and Li-Xi Li. Aberrant neuregulin 1/erbb signaling in charcot-marie-tooth type 4d disease. Jul 2022. URL: https://doi.org/10.1128/mcb.00559-21, doi:10.1128/mcb.00559-21. This article has 7 citations and is from a domain leading peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](Charcot-Marie-Tooth_Disease_Type_4D-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 12 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 1 |
| References weighed for topical relevance | 11 |
| On topic | 5 |
| Off topic | 0 |

11 of 12 references resolved; the rest could not be looked up either way.