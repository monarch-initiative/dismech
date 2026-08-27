---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-26T22:31:52.636322'
end_time: '2026-08-26T22:47:34.142392'
duration_seconds: 941.51
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Generalized Resistance to Thyroid Hormone
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 20
reference_validation:
  total_references: 4
  verified: 4
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 4
  on_topic: 2
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Generalized_Resistance_to_Thyroid_Hormone-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Generalized Resistance to Thyroid Hormone
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Generalized Resistance to Thyroid Hormone** covering all of the
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
- **Disease Name:** Generalized Resistance to Thyroid Hormone
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Generalized Resistance to Thyroid Hormone** covering all of the
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


# Generalized Resistance to Thyroid Hormone: Disease Characteristics Report

## Scope and terminology

**Generalized resistance to thyroid hormone (GRTH)** is the historical name for reduced tissue responsiveness to thyroid hormone affecting the hypothalamic–pituitary–thyroid axis and peripheral tissues. Most molecularly confirmed cases are now termed **resistance to thyroid hormone beta (RTHβ)**. This distinction matters: RTHα, defects of hormone transport such as MCT8 deficiency, and defects of hormone metabolism are separate disorders. “Generalized,” “pituitary,” and “peripheral” RTH were originally clinical subdivisions, but they overlap and are less useful than molecular classification.

The strongest current authority is the **2024 European Thyroid Association (ETA) guideline**, published July 2024 (DOI [10.1530/ETJ-24-0125](https://doi.org/10.1530/etj-24-0125)). Its abstract states: “Impaired sensitivity to thyroid hormones encompasses disorders with defective transport of hormones into cells, reduced hormone metabolism, and resistance to hormone action,” and emphasizes that diagnosis combines clinical features with pathogenic variants while management rests on a limited evidence base. (persani20242024europeanthyroid pages 10-11, persani20242024europeanthyroid pages 9-10)

| domain | core finding/statistic | evidence type | source/date/DOI or NCT |
|---|---|---|---|
| Disease identifiers | Generalized resistance to thyroid hormone; MONDO:0009043; OMIM:188570; disease-level aggregated rare-disease/gene-disease resources link generalized RTH to **THRB** (OpenTargets Search: resistance to thyroid hormone-THRB, persani20242024europeanthyroid pages 9-10) | Ontology/database + guideline | Open Targets disease-target association context; ETA Guideline, Jul 2024, https://doi.org/10.1530/etj-24-0125 |
| Core definition | RTHβ is characterized by elevated thyroid hormones with non-suppressed TSH and variable multisystem phenotype from asymptomatic to thyrotoxic (persani20242024europeanthyroid pages 9-10, persani20242024europeanthyroid pages 2-3) | Guideline/reviewed clinical evidence | ETA Guideline, Jul 2024, DOI:10.1530/etj-24-0125 |
| Causal gene / inheritance | Causal gene: **THRB**; typically **autosomal dominant**; mutant TRβ acts in a **dominant-negative** manner via reduced hormone binding and/or impaired corepressor release/coactivator recruitment (persani20242024europeanthyroid pages 9-10) | Mechanistic human/genetic guideline evidence | ETA Guideline, Jul 2024, DOI:10.1530/etj-24-0125 |
| Prevalence | Reported prevalence range **~1:18,750 to 1:40,000** (buyukyılmaz2024clinicalcharacteristicsand pages 1-1, belal20247684resistanceto pages 1-2) | Human cohort + case report summary | Büyükyılmaz et al., Dec 2024, DOI:10.4274/jcrpe.galenos.2024.2024-8-14; Belal et al., Oct 2024, DOI:10.1210/jendso/bvae163.2063 |
| Variant spectrum | Turkish series found **8 heterozygous pathogenic/likely pathogenic missense variants** in 30 genetically confirmed patients from 8 unrelated families, including **3 novel variants** (buyukyılmaz2024clinicalcharacteristicsand pages 1-1, buyukyılmaz2024clinicalcharacteristicsand pages 2-3) | Human cohort | Büyükyılmaz et al., Dec 2024, DOI:10.4274/jcrpe.galenos.2024.2024-8-14 |
| Variant-negative fraction | About **10–15%** of clinically suspected/phenotypic RTHβ cases may lack an identifiable **THRB** variant; possible explanations include mosaicism or noncoding/deep intronic defects (persani20242024europeanthyroid pages 9-10, buyukyılmaz2024clinicalcharacteristicsand pages 3-3, belal20247684resistanceto pages 1-2) | Guideline + cohort + case summary | ETA Guideline, Jul 2024, DOI:10.1530/etj-24-0125; Büyükyılmaz et al., Dec 2024, DOI:10.4274/jcrpe.galenos.2024.2024-8-14 |
| Biochemical hallmark | Typical diagnostic pattern: **elevated free/total T4**, **elevated free/total T3**, and **non-suppressed or inappropriately normal/elevated TSH** (persani20242024europeanthyroid pages 9-10, persani20242024europeanthyroid pages 2-3) | Guideline | ETA Guideline, Jul 2024, DOI:10.1530/etj-24-0125 |
| Differential diagnosis | Important differentials include **assay interference** and **TSH-secreting pituitary adenoma (TSHoma)**; in the Turkish suspected cohort, **1/20** variant-negative patients had TSHoma (buyukyılmaz2024clinicalcharacteristicsand pages 2-3, belal20247684resistanceto pages 1-2) | Cohort + case-based clinical evidence | Büyükyılmaz et al., Dec 2024, DOI:10.4274/jcrpe.galenos.2024.2024-8-14; Belal et al., Oct 2024, DOI:10.1210/jendso/bvae163.2063 |
| Pediatric/adult phenotype frequencies | In the 2024 Turkish genetically confirmed cohort (**n=30**): **56%** of children had goiter; **23%** had positive thyroid autoantibodies; **7 adults** had thyroid nodules; **2 adults** had papillary thyroid carcinoma (buyukyılmaz2024clinicalcharacteristicsand pages 1-1, buyukyılmaz2024clinicalcharacteristicsand pages 3-3) | Human cohort | Büyükyılmaz et al., Dec 2024, DOI:10.4274/jcrpe.galenos.2024.2024-8-14 |
| Clinical phenotype spectrum | Many patients are asymptomatic, but reported manifestations include goiter, tachycardia/tachyarrhythmia, anxiety, sleep disturbance, ADHD/learning issues, hearing loss, color vision impairment, dyslipidemia, and increased liver fat (persani20242024europeanthyroid pages 9-10, buyukyılmaz2024clinicalcharacteristicsand pages 2-3, belal20247684resistanceto pages 1-2) | Guideline + cohort + case summary | ETA Guideline, Jul 2024, DOI:10.1530/etj-24-0125; Büyükyılmaz et al., Dec 2024, DOI:10.4274/jcrpe.galenos.2024.2024-8-14 |
| Cardiovascular prognosis | Guideline-level evidence notes increased risks of **atrial fibrillation, myocardial infarction, heart failure, and earlier mortality** in RTHβ, likely reflecting excess hormone action in TRα-expressing tissues such as myocardium (persani20242024europeanthyroid pages 9-10) | Guideline/expert synthesis | ETA Guideline, Jul 2024, DOI:10.1530/etj-24-0125 |
| Management principles | Many patients require **no disease-specific therapy**; avoid antithyroid drugs or thyroid ablation unless significant comorbidity/misdiagnosis issues; treatment is individualized and symptom-directed (buyukyılmaz2024clinicalcharacteristicsand pages 2-3, persani20242024europeanthyroid pages 3-5) | Guideline + cohort | ETA Guideline, Jul 2024, DOI:10.1530/etj-24-0125; Büyükyılmaz et al., Dec 2024, DOI:10.4274/jcrpe.galenos.2024.2024-8-14 |
| TRIAC therapy | **TRIAC (triiodothyroacetic acid)** is recommended/used to control thyrotoxic signs and symptoms; guideline dosing reported as **1.4–2.8 mg twice or three times daily**, preferably with expert-center input (persani20242024europeanthyroid pages 10-11, persani20242024europeanthyroid pages 3-5) | Guideline/expert consensus | ETA Guideline, Jul 2024, DOI:10.1530/etj-24-0125 |
| Other symptomatic therapy | **Beta-blockade** can be used for adrenergic symptoms; selected reports note benefit of **alternate-day supraphysiologic liothyronine (D-T3)** for goiter/ADHD phenotypes (persani20242024europeanthyroid pages 9-10, belal20247684resistanceto pages 1-2) | Guideline + case summary | ETA Guideline, Jul 2024, DOI:10.1530/etj-24-0125; Belal et al., Oct 2024, DOI:10.1210/jendso/bvae163.2063 |
| Surveillance | Recommended follow-up includes **thyroid ultrasound**, **anti-thyroid antibodies**, cardiovascular assessment (BP, ECG ± echo, especially >30 y or symptomatic), **fasting lipids/glucose**, adult **bone density**, and pediatric growth/development/hearing/neuropsychological assessment (persani20242024europeanthyroid pages 3-5, persani20242024europeanthyroid pages 2-3) | Guideline | ETA Guideline, Jul 2024, DOI:10.1530/etj-24-0125 |
| Pregnancy | Women with RTHβ should receive **multidisciplinary endocrine-obstetric care**; monitoring should include fetal growth and heart rate; guideline notes increased **miscarriage** and **small-for-gestational-age** risk in affected mothers (persani20242024europeanthyroid pages 10-11, persani20242024europeanthyroid pages 3-5) | Guideline/expert synthesis | ETA Guideline, Jul 2024, DOI:10.1530/etj-24-0125 |
| Active observational study | **Understanding, Diagnosis and Monitoring of Thyroid Hormone Action Defects**; recruiting observational study; planned enrollment **150** (RTH and related thyroid hormone action defects) | Clinical study registry | **NCT06307990**, Istituto Auxologico Italiano, https://clinicaltrials.gov/study/NCT06307990 |
| Active registry | **Register for Patients With Thyroid Hormone Resistance**; recruiting observational registry; planned enrollment **200** | Clinical study registry | **NCT06566066**, Charité University Berlin, https://clinicaltrials.gov/study/NCT06566066 |
| Natural history platform | **Natural History of Thyroid Function Disorders**; recruiting observational study; planned enrollment **2500** | Clinical study registry | **NCT00001159**, NIH Clinical Center, https://clinicaltrials.gov/study/NCT00001159 |
| Mouse model evidence | TRβ mouse models show that **pituitary-thyroid negative feedback depends on TRβ DNA binding**; **severe hearing loss** occurs in TRβKO and TRβGS mice; retinal thickness/visual phenotypes support sensory-system involvement of TRβ (hones2024comparativephenotypingof pages 5-9) | Animal model | Hönes et al., bioRxiv, Nov 2024, DOI:10.1101/2023.11.26.568063 |
| Translational interpretation | Mouse data support human tissue selectivity: impaired central feedback and sensory phenotypes help explain unsuppressed TSH plus hearing/vision abnormalities seen clinically in RTHβ (persani20242024europeanthyroid pages 9-10, hones2024comparativephenotypingof pages 5-9) | Cross-species synthesis | ETA Guideline, Jul 2024, DOI:10.1530/etj-24-0125; Hönes et al., Nov 2024, DOI:10.1101/2023.11.26.568063 |


*Table: This compact table summarizes high-value evidence for generalized resistance to thyroid hormone (RTHβ), emphasizing identifiers, genetics, biochemical diagnosis, recent cohort data, management, surveillance, ongoing studies, and translational animal findings.*

## 1. Disease information

### Definition

RTHβ is a rare, usually Mendelian disorder in which tissues show reduced sensitivity to triiodothyronine (T3), producing the characteristic biochemical combination of **high free/total T4 and usually high free/total T3 with a non-suppressed TSH**. Compensatory elevation of thyroid hormones maintains near-normal signaling in resistant tissues but can over-stimulate tissues in which TRα predominates, explaining simultaneous hypo-, eu-, and hyperthyroid features. The phenotype ranges from clinically asymptomatic to significant thyrotoxicosis. (persani20242024europeanthyroid pages 9-10, persani20242024europeanthyroid pages 2-3)

### Identifiers and synonyms

- **MONDO:** **MONDO:0009043**, generalized resistance to thyroid hormone.
- **Related molecular MONDO entry:** **MONDO:0700478**, resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta.
- **OMIM:** **188570**, generalized resistance to thyroid hormone. The ETA guideline separately lists **145650** for pituitary resistance.
- **MeSH concept:** thyroid hormone resistance syndrome; the exact current descriptor identifier should be validated directly against the production MeSH release before database ingestion.
- **Common names:** generalized thyroid hormone resistance; generalized RTH; resistance to thyroid hormone; thyroid hormone resistance syndrome; Refetoff syndrome; RTHβ/RTH-beta; impaired sensitivity to thyroid hormone due to THRB mutation.
- **ICD:** no highly specific, universally used ICD-10 code cleanly captures molecular RTHβ; it is commonly mapped under other specified endocrine/thyroid dysfunction. ICD-11 implementation should likewise be verified locally rather than inferring a molecularly specific code.

Open Targets links **THRB** with generalized RTH, molecular RTHβ, pituitary RTH, peripheral RTH, and the broader thyroid-hormone-resistance syndrome. These are aggregated disease–gene resources, not individual electronic health records. The Turkish study discussed below is aggregated retrospective patient-level clinical data. (OpenTargets Search: resistance to thyroid hormone-THRB)

## 2. Etiology, risk, and protective factors

### Primary cause

The principal cause is a **germline heterozygous pathogenic variant in THRB**, encoding nuclear thyroid hormone receptor β. Approximately 75% of cases are familial/autosomal dominant, while the remainder include de novo disease. Mutant TRβ generally exerts a **dominant-negative** effect over wild-type receptor by reducing ligand binding, preventing corepressor release, impairing coactivator recruitment, or otherwise disrupting transcription at thyroid-hormone-response elements. (persani20242024europeanthyroid pages 9-10, buyukyılmaz2024clinicalcharacteristicsand pages 1-1)

About **10–15% of clinically convincing RTHβ phenotypes lack a detectable coding THRB variant**. Proposed explanations include somatic mosaicism and deep intronic or other regulatory defects; this group should not automatically be assumed to have RTHβ until assay interference and alternative diagnoses are rigorously excluded. (persani20242024europeanthyroid pages 9-10, buyukyılmaz2024clinicalcharacteristicsand pages 3-3, belal20247684resistanceto pages 1-2)

### Risk and protective factors

- **Genetic risk:** an affected parent, a de novo pathogenic THRB allele, or parental mosaicism. No established common susceptibility locus is used clinically.
- **Family history:** confers an approximately 50% transmission probability for a heterozygous affected individual, subject to variant interpretation and mosaicism.
- **Environmental, infectious, occupational, dietary, smoking, alcohol, or lifestyle causes:** none is established as a cause of Mendelian RTHβ.
- **Protective alleles or environmental protective factors:** none validated.
- **Gene–environment interaction:** not established for disease occurrence. Iodine exposure, intercurrent thyroid autoimmunity, pregnancy, medication, and thyroid ablation can alter hormone burden and clinical expression without causing the inherited receptor defect.
- **Epigenetic causation:** no validated disease-defining methylation or chromatin signature.

## 3. Phenotypes

Clinical expression is highly variable within and between families and is not reliably predicted by serum hormone concentration alone. Most manifestations can begin in childhood, while nodules, arrhythmia, metabolic complications, and cardiovascular events become more relevant during adulthood. The disorder is generally chronic and lifelong rather than episodic.

### Major phenotype groups and suggested HPO terms

| Phenotype | Type and characteristics | Frequency/evidence | Suggested HPO annotation |
|---|---|---|---|
| Elevated T4/T3 with non-suppressed TSH | Laboratory hallmark; persistent unless modified by treatment or another thyroid disorder | Defining pattern | **Abnormal circulating thyroxine concentration**, **abnormal circulating triiodothyronine concentration**, **abnormal TSH level**; validate exact HPO IDs in the current release |
| Goiter | Sign; diffuse initially, potentially nodular; variable severity | **56% of variant-positive children** in the 2024 Turkish cohort | **HP:0000853, Goiter** |
| Thyroid nodules | Structural manifestation, mainly adult surveillance concern | 7 adults in the Turkish cohort | **HP:0100646, Thyroid nodule** |
| Tachycardia/palpitations | Cardiovascular sign/symptom; reflects excess T3 action in TRα-predominant myocardium | Common qualitative feature; exact universal frequency unavailable | **HP:0001649, Tachycardia**; palpitations term |
| Atrial fibrillation/heart failure | Adult complication; potentially severe | Increased-risk signal in contemporary clinical evidence, but absolute penetrance is unavailable | **HP:0005110, Atrial fibrillation**; **HP:0001635, Congestive heart failure** |
| ADHD, attention or learning difficulty | Behavioral/neurodevelopmental; usually recognized in childhood | One child had attention-deficit disorder and learning disability in the Turkish cohort; broader association recognized by ETA | **HP:0007018, Attention deficit hyperactivity disorder**; **HP:0001328, Specific learning disability** |
| Anxiety and sleep disturbance | Symptoms; variable and potentially fluctuating | Qualitative guideline association | **HP:0000739, Anxiety**; sleep-abnormality term |
| Hearing impairment | Sensory sign; developmental or later recognized | Qualitative human association; strong mechanistic mouse support | **HP:0000365, Hearing impairment** |
| Impaired color vision/macular disease | Ophthalmic manifestation; color perception can be altered in heterozygous RTHβ; selected splice variants cause a distinct macular dystrophy phenotype | Rare/variant-specific | **HP:0000551, Abnormality of color vision**; macular dystrophy term |
| Dyslipidemia and hepatic steatosis | Laboratory/metabolic manifestations reflecting hepatic TRβ resistance | Qualitative guideline association | **HP:0003124, Hypercholesterolemia**; **HP:0001397, Hepatic steatosis** |
| Reduced bone density | Potential chronic complication of hormone excess/tissue-selective action | Frequency uncertain; surveillance recommended | **HP:0000938, Osteopenia** |
| Thyroid autoimmunity | Comorbidity rather than the receptor defect itself | **23%** antibody positivity in the Turkish variant-positive group, reported only in females | Autoimmune thyroiditis/thyroid-antibody HPO concepts |

The December 2024 Turkish multicenter study examined 50 suspected/familial cases and molecularly confirmed RTHβ in 30 people from eight families. Its abstract reports: “Although most patients with RTHβ were asymptomatic, seven patients exhibited various symptoms.” It found eight heterozygous pathogenic/likely pathogenic missense variants, including three novel variants; 56% of affected children had goiter, seven adults had nodules, and two adults had papillary thyroid cancer. These cancer observations are important for surveillance but do **not** establish a population-level cancer penetrance from this small, selected cohort. DOI [10.4274/jcrpe.galenos.2024.2024-8-14](https://doi.org/10.4274/jcrpe.galenos.2024.2024-8-14), published December 2024. (buyukyılmaz2024clinicalcharacteristicsand pages 1-1, buyukyılmaz2024clinicalcharacteristicsand pages 2-3, buyukyılmaz2024clinicalcharacteristicsand pages 3-3)

### Quality of life

Palpitations, anxiety, sleep problems, hearing impairment, goiter, and neurocognitive symptoms can impair school, work, and social functioning. However, no validated RTHβ-specific patient-reported outcome instrument, EQ-5D norm, or robust SF-36 cohort estimate was identified. QoL effects should therefore be recorded at the individual-patient level rather than assigned a population percentage.

## 4. Genetic and molecular information

### Causal gene and protein

- **Gene:** **THRB**, thyroid hormone receptor beta.
- **HGNC:** **HGNC:11799**.
- **Ensembl:** **ENSG00000151090**.
- **Protein:** nuclear thyroid hormone receptor β; major isoforms TRβ1 and TRβ2.
- **Origin:** ordinarily germline; postzygotic/somatic mosaicism is a proposed explanation for some variant-negative cases. This is not a cancer-associated somatic disorder.

Pathogenic variants cluster predominantly in the ligand-binding domain and are commonly missense substitutions. Insertions, deletions, frameshifts, and truncating alleles can occur and may produce more severe receptor dysfunction. The Turkish cohort's eight variants were all heterozygous missense changes; because the retrieved evidence did not expose every HGVS expression and ClinVar accession, these should be imported directly from ClinVar/the primary article rather than reconstructed. (buyukyılmaz2024clinicalcharacteristicsand pages 1-1, buyukyılmaz2024clinicalcharacteristicsand pages 2-3)

### Functional consequence and classification

Disease-causing missense alleles are generally loss-of-function at the mutant receptor level but produce **dominant-negative gain of interference** at the cellular level. A receptor may retain DNA binding while failing to respond appropriately to T3, thereby maintaining corepressor complexes or failing to recruit coactivators and suppressing normal-receptor signaling. (persani20242024europeanthyroid pages 9-10)

For clinical reporting, each variant requires ACMG/AMP classification using segregation, population frequency, functional evidence, location/domain, computational evidence, and prior observations. Pathogenic RTHβ variants are expected to be rare or absent from gnomAD, but no single allele-frequency value applies to the disease. VUS findings must not be treated as diagnostic without segregation or functional support.

### Modifiers, epigenetics, and chromosomes

Marked intrafamilial variability implies modifiers, including receptor-isoform distribution, hormone transporters, deiodinases, coregulators, age, and coincident thyroid disease. No specific modifier gene is validated for routine prognostication. No recurrent aneuploidy, translocation, inversion, methylation defect, or chromosomal syndrome defines RTHβ. CMA, karyotyping, and FISH are therefore not first-line tests.

## 5. Environmental information

RTHβ is not caused by toxin, radiation, pollution, occupation, lifestyle, or infection. Exogenous levothyroxine, liothyronine, amiodarone, biotin-related assay artifacts, antithyroid therapy, iodine status, and thyroid surgery can confound diagnosis or amplify manifestations but do not create the germline disorder. A 2024 case illustrates prolonged misclassification as hypothyroidism and escalation of levothyroxine despite elevated FT4/FT3 and non-suppressed TSH. DOI [10.1210/jendso/bvae163.2063](https://doi.org/10.1210/jendso/bvae163.2063), October 2024. (belal20247684resistanceto pages 1-2)

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream trigger:** heterozygous pathogenic **THRB** variant.
2. **Protein defect:** altered TRβ ligand binding or transcriptional-coregulator exchange.
3. **Cellular effect:** mutant receptor occupies or perturbs thyroid-hormone-response-element complexes and inhibits wild-type signaling.
4. **Central endocrine consequence:** pituitary/hypothalamic resistance weakens T3-mediated negative feedback.
5. **Biochemical compensation:** TSH remains inappropriately normal or rises, stimulating thyroid growth and increased T4/T3 synthesis.
6. **Tissue-selective consequences:** TRβ-rich tissues remain relatively resistant, while TRα-rich heart, skeletal muscle, brain, and bone are exposed to high circulating hormone and may become hyperthyroid.
7. **Clinical outcome:** mixed goitrous, metabolic, neurobehavioral, sensory, skeletal, and cardiovascular phenotypes. (persani20242024europeanthyroid pages 9-10)

### Pathways and ontology suggestions

- **Canonical pathway:** nuclear-receptor-mediated thyroid hormone signaling and transcriptional regulation.
- **Noncanonical signaling:** TRs can influence PI3K–AKT and MAPK–ERK signaling, but their contribution to individual human RTHβ phenotypes remains incompletely resolved.
- **Suggested GO biological processes:** thyroid hormone receptor signaling pathway; cellular response to thyroid hormone stimulus; regulation of transcription by RNA polymerase II; negative regulation of thyroid-stimulating hormone secretion; sensory perception of sound; cone photoreceptor differentiation; lipid metabolic process.
- **Suggested GO cellular components:** **GO:0005634 nucleus**, chromatin, transcription-regulator complex.
- **Suggested molecular functions:** nuclear thyroid hormone receptor activity; ligand-activated transcription-factor activity; DNA-binding transcription-factor activity.
- **Suggested cell types:** pituitary thyrotroph (**CL:0000476**), hepatocyte (**CL:0000182**), cardiomyocyte (**CL:0000746**), retinal cone photoreceptor (**CL:0000573**), cochlear sensory hair cell, thyroid follicular cell, neuron, and osteoblast. Exact CL mappings should be version-validated.

### Metabolic, immune, and tissue effects

Hepatic TRβ resistance can contribute to dyslipidemia and increased liver fat. Cardiac injury is principally downstream of chronic high hormone exposure in relatively TRα-sensitive myocardium, manifesting as tachyarrhythmia or failure rather than a primary inflammatory cardiomyopathy. Autoimmune thyroid disease may coexist, but autoimmunity is not the primary mechanism. No established disease-specific transcriptomic, proteomic, metabolomic, lipidomic, single-cell, spatial-transcriptomic, or multi-omic diagnostic signature currently exists. (persani20242024europeanthyroid pages 10-11, persani20242024europeanthyroid pages 9-10)

## 7. Anatomical structures affected

- **Primary endocrine axis:** hypothalamus, pituitary, and thyroid gland.
- **TRβ-rich targets:** liver, kidney, cochlea, and retina.
- **Secondary systems:** cardiovascular system, CNS/behavioral circuits, skeleton, skeletal muscle, and metabolic tissues.
- **Suggested UBERON terms:** thyroid gland (**UBERON:0002046**), pituitary gland (**UBERON:0000007**), hypothalamus (**UBERON:0001898**), liver (**UBERON:0002107**), kidney (**UBERON:0002113**), heart (**UBERON:0000948**), retina (**UBERON:0000966**), and cochlea (**UBERON:0001844**).
- **Subcellular localization:** primarily nuclear/chromatin-associated receptor complexes; noncanonical cytoplasmic signaling is also biologically plausible.
- **Lateralization:** not characteristic; systemic and generally bilateral sensory involvement is expected.

The expression statement in one 2024 case abstract uses “TSH receptor beta/alpha”; biologically, this should be interpreted as **thyroid hormone receptor β/α**, not the TSH receptor. (belal20247684resistanceto pages 1-2)

## 8. Temporal development

The molecular defect is congenital and lifelong. Biochemical abnormalities may be evident neonatally or discovered incidentally in childhood/adulthood. Goiter and neurodevelopmental manifestations often emerge during childhood; nodular thyroid disease, hepatic fat, dyslipidemia, arrhythmia, and cardiovascular complications may accumulate with age. There is no accepted stage system. Course and severity are variable rather than predictably progressive, and spontaneous molecular remission is not expected. Pregnancy is a critical period because fetal genotype determines whether maternal high thyroid hormone levels are compensatory or excessive for the fetus. (persani20242024europeanthyroid pages 10-11, persani20242024europeanthyroid pages 3-5)

## 9. Inheritance and population

Reported prevalence is approximately **1 in 18,750–40,000**, equivalent to roughly **2.5–5.3 per 100,000**. Reliable annual incidence estimates are unavailable. RTHβ affects all sexes and ancestries; no consistent sex ratio, geographic endemicity, or broadly applicable founder effect is established. (buyukyılmaz2024clinicalcharacteristicsand pages 1-1, belal20247684resistanceto pages 1-2)

Inheritance is usually **autosomal dominant**, with variable expressivity and clinically incomplete recognition. Biochemical penetrance is generally high for established dominant-negative variants, but clinical penetrance is variable. Anticipation is not recognized. Germline/parental mosaicism is possible but not quantified. Consanguinity is not a characteristic risk factor for dominant RTHβ, and population carrier-frequency estimates are not robust enough for general screening.

## 10. Diagnostics

### Clinical biochemical workflow

1. Confirm elevated FT4/FT3 with non-suppressed TSH on a repeat sample.
2. Review medications and supplements, especially levothyroxine/liothyronine, amiodarone, heparin-related artifacts, and high-dose biotin.
3. Exclude analytical interference using another assay platform, dilution/blocking studies, equilibrium dialysis or ultrafiltration where needed; assess binding-protein abnormalities.
4. Evaluate family thyroid-function tests. Similar biochemical results in a first-degree relative strongly support inherited RTH.
5. Exclude **TSH-secreting pituitary tumor (TSHoma)** using clinical context, pituitary hormones/α-subunit where informative, sex-hormone-binding globulin, pituitary MRI, and specialist dynamic testing when uncertainty remains.
6. Sequence **THRB** and test segregation. The ETA recommends THRB sequencing when genuinely elevated thyroid hormones coexist with non-suppressed TSH. (belal20247684resistanceto pages 1-2, persani20242024europeanthyroid pages 2-3)

In the Turkish suspected cohort, one of 20 people without a THRB variant was found to have a TSHoma, demonstrating why a negative genetic test does not itself prove “non-THRB RTH.” (buyukyılmaz2024clinicalcharacteristicsand pages 2-3)

### Genetic testing strategy

- **First line:** sequence THRB coding exons and splice boundaries, with deletion/duplication analysis if the platform does not provide it.
- **Panel:** a discordant-thyroid-function/thyroid-hormone-action panel may include **THRB, THRA, SLC16A2, SECISBP2, DIO1/DIO2-related candidates**, binding-protein genes, and genes relevant to familial dysalbuminemic hyperthyroxinemia, tailored to the biochemical phenotype.
- **WES/WGS:** appropriate when targeted testing is negative and the phenotype remains convincing. WGS is better suited to deep intronic/regulatory and structural variants; mosaic-aware analysis may be needed.
- **RNA sequencing:** potentially useful to prove abnormal splicing but not routine.
- **CMA, karyotype, FISH, mitochondrial, and repeat-expansion testing:** not routinely indicated.

### Imaging and monitoring

Thyroid ultrasound evaluates goiter and nodules. In adults—especially after age 30 or when symptomatic—assess blood pressure, ECG, and, when indicated, echocardiography and cardiac biomarkers. Check fasting lipids/glucose and adult bone density. In children, monitor growth, development, hearing, cognition, and ADHD symptoms. (persani20242024europeanthyroid pages 3-5, persani20242024europeanthyroid pages 2-3)

### Screening

RTHβ is not part of routine population or newborn genetic screening. Newborn TSH/T4 screening may identify unusual profiles but is not optimized for RTHβ. **Cascade biochemical and variant testing** of first-degree relatives is recommended after identifying a familial pathogenic variant. Prenatal diagnosis and PGT-M are technically possible following counseling.

## 11. Outcome and prognosis

Many affected people remain asymptomatic or mildly symptomatic and live independently. Nevertheless, contemporary guideline synthesis associates RTHβ with greater risks of atrial fibrillation, myocardial infarction, heart failure, and earlier mortality, supporting proactive cardiovascular surveillance. No reliable disease-specific 5-year/10-year survival percentage or treated-versus-untreated life-expectancy estimate is available in the retrieved evidence. (persani20242024europeanthyroid pages 9-10)

Potential morbidity includes persistent goiter/nodules, avoidable thyroidectomy after misdiagnosis, arrhythmia, cardiac failure, dyslipidemia, liver fat, low bone density, hearing/vision abnormalities, and educational or behavioral impairment. Prognosis is influenced by genotype, degree of hormone elevation, age, cardiovascular phenotype, thyroid structural disease, and—critically—iatrogenic treatment. Genotype correlates with FT4, resting energy expenditure, and LDL cholesterol, but individual prediction remains limited. (persani20242024europeanthyroid pages 10-11)

## 12. Treatment and current implementation

### General principle

Treatment is **phenotype-directed, not laboratory-normalization-directed**. An asymptomatic patient with compensated high thyroid hormones generally does not require therapy. Routine antithyroid drugs, radioiodine, or thyroidectomy can destroy compensation and create difficult-to-treat hypothyroidism; the ETA recommends avoiding these approaches absent compelling comorbidity. (buyukyılmaz2024clinicalcharacteristicsand pages 2-3, persani20242024europeanthyroid pages 3-5)

### Interventions

- **Observation and surveillance:** first-line for asymptomatic/mild disease.
- **Beta-blocker:** for tachycardia, tremor, or palpitations; suggested NCIt concept: beta-adrenergic blocking-agent therapy.
- **TRIAC/tiratricol (3,5,3′-triiodothyroacetic acid):** a thyroid-hormone analogue with relatively strong pituitary action that lowers TSH and circulating T4/T3. The ETA reports **1.4–2.8 mg two or three times daily**, titrated to symptoms and FT4, and recommends expert-center supervision. It can be combined with beta-blockade; selected severe cardiomyopathy cases have used antithyroid medication plus TRIAC to control hormone production without allowing marked TSH-driven goiter. (persani20242024europeanthyroid pages 10-11, persani20242024europeanthyroid pages 3-5)
- **Supraphysiologic intermittent liothyronine:** alternate-day T3 has reduced goiter and helped selected ADHD phenotypes in case-based experience. It is not standardized therapy and requires specialist monitoring. (persani20242024europeanthyroid pages 9-10, belal20247684resistanceto pages 1-2)
- **Antithyroid drugs/ablation/surgery:** reserve for exceptional, severe situations or independent thyroid pathology such as suspicious cancer; replacement afterward can be challenging.
- **ADHD or psychiatric therapy:** treat according to standard clinical criteria while accounting for cardiovascular risk.
- **Rehabilitation/support:** educational accommodations, audiology support, and psychological care as indicated.

No approved gene therapy, CRISPR therapy, ASO/siRNA therapy, cell therapy, immunotherapy, or RTHβ-specific pharmacogenomic guideline exists. Evidence for TRIAC and intermittent T3 is largely observational/case-based, not derived from large randomized RTHβ trials.

### Pregnancy

All affected pregnancies warrant joint endocrine–maternal-fetal-medicine care. Maternal RTHβ has been associated with miscarriage and small-for-gestational-age birth. Monitor fetal growth and heart rate; fetal tachycardia or growth restriction may justify carefully selected maternal antithyroid treatment. Management must consider whether the fetus inherited RTHβ: hormone levels compensatory for an affected mother/fetus can be excessive for an unaffected fetus. (persani20242024europeanthyroid pages 10-11, persani20242024europeanthyroid pages 3-5)

### Trials and registries

Current real-world research is primarily observational:

- **NCT06307990**, *Understanding, Diagnosis and Monitoring of Thyroid Hormone Action Defects*: recruiting, target **150**, Istituto Auxologico Italiano; [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT06307990).
- **NCT06566066**, *Register for Patients With Thyroid Hormone Resistance*: recruiting, target **200**, Charité Berlin; [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT06566066).
- **NCT00001159**, *Natural History of Thyroid Function Disorders*: recruiting NIH observational platform, target **2,500**; [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT00001159).

No active late-phase disease-modifying RTHβ interventional trial was identified. Trials of tiratricol in **MCT8 deficiency** or resmetirom in steatotic liver disease should not be misclassified as RTHβ trials.

## 13. Prevention

Primary prevention of a de novo or inherited receptor variant by lifestyle or vaccination is not possible. Applicable measures are:

- **Genetic counseling:** autosomal-dominant recurrence risk, variable expressivity, prenatal diagnosis, and PGT-M.
- **Secondary prevention:** cascade testing, early recognition of discordant thyroid tests, and avoiding misdiagnosis as Graves disease, hypothyroidism, or TSHoma.
- **Tertiary prevention:** cardiac surveillance, thyroid examination/ultrasound, metabolic and bone monitoring, hearing and neurodevelopmental assessment, and avoidance of unnecessary ablation.
- **Public-health prophylaxis, vaccination, sanitation, environmental remediation, and preventive medication:** not applicable.

## 14. Other species and natural disease

No well-established, clinically important naturally occurring companion-animal or wildlife counterpart of human THRB-associated generalized RTH was identified. There is no zoonotic potential or cross-species transmission because the condition is genetic. Orthologues include mouse **Thrb** and corresponding vertebrate THRB genes; mechanisms of receptor-mediated transcription and feedback are evolutionarily conserved. Before assigning OMIA, NCBI Gene, or VBO identifiers, they should be verified directly in the relevant live database.

## 15. Model organisms

### Mouse models

Available systems include global **Thrb knockout**, DNA-binding-deficient **TRβGS knock-in**, and dominant-negative ligand-binding-domain knock-in models such as **ThrbPV**. These permit separation of receptor absence, impaired canonical DNA binding, and dominant-negative mutant-receptor effects.

A November 2024 comparative phenotyping preprint found that pituitary–thyroid negative feedback requires TRβ DNA binding; both TRβKO and TRβGS mice had severe hearing loss, while retinal thickness, visual acuity, cone maturation, and opsin expression showed TRβ-dependent abnormalities. It also suggested roles for noncanonical TRβ signaling in liver triglycerides and glucose control. DOI [10.1101/2023.11.26.568063](https://doi.org/10.1101/2023.11.26.568063). (hones2024comparativephenotypingof pages 5-9)

### Recapitulation and limitations

These mice reproduce central resistance, sensory-system defects, and selected metabolic manifestations and are useful for dissecting canonical versus noncanonical signaling. Some dominant-negative Thrb models develop thyroid hyperplasia/carcinoma under sustained TSH drive, offering a mechanistic tumor model; however, tumor severity in such homozygous or engineered mice must not be directly translated into human cancer penetrance. Species differences, allele dosage, global versus tissue-specific disruption, and controlled genetic backgrounds limit clinical extrapolation.

Cellular reporter assays remain useful for measuring T3 binding, transcriptional activation, dominant-negative activity, corepressor release, and coactivator recruitment. Patient-derived iPSC/organoid, CRISPR-screen, single-cell, and spatial-transcriptomic models are not yet established routine platforms for RTHβ.

## Current expert interpretation and evidence gaps

The 2024 ETA panel's central expert position is that discordant thyroid tests must be verified before genetic diagnosis, and management should target clinically important tissue effects rather than force T4/T3 into reference ranges. This is particularly important because inappropriate treatment is common: **41.7%** of historically managed patients in the Turkish series had received interventions before diagnosis, including antithyroid therapy or thyroidectomy. (buyukyılmaz2024clinicalcharacteristicsand pages 2-3, persani20242024europeanthyroid pages 3-5)

Major remaining gaps are prospective natural-history data, standardized phenotype frequencies, validated QoL measures, variant-specific penetrance, controlled RTHβ treatment trials, disease-specific mortality estimates, molecular biomarkers beyond thyroid-function tests and genotype, and human single-cell/multi-omic characterization. The newly recruiting registries are therefore clinically relevant recent developments rather than merely administrative studies.

References

1. (persani20242024europeanthyroid pages 10-11): Luca Persani, Patrice Rodien, Carla Moran, W Edward Visser, Stefan Groeneweg, Robin Peeters, Samuel Refetoff, Mark Gurnell, Paolo Beck-Peccoz, and Krishna Chatterjee. 2024 european thyroid association guidelines on diagnosis and management of genetic disorders of thyroid hormone transport, metabolism and action. Jul 2024. URL: https://doi.org/10.1530/etj-24-0125, doi:10.1530/etj-24-0125. This article has 58 citations and is from a peer-reviewed journal.

2. (persani20242024europeanthyroid pages 9-10): Luca Persani, Patrice Rodien, Carla Moran, W Edward Visser, Stefan Groeneweg, Robin Peeters, Samuel Refetoff, Mark Gurnell, Paolo Beck-Peccoz, and Krishna Chatterjee. 2024 european thyroid association guidelines on diagnosis and management of genetic disorders of thyroid hormone transport, metabolism and action. Jul 2024. URL: https://doi.org/10.1530/etj-24-0125, doi:10.1530/etj-24-0125. This article has 58 citations and is from a peer-reviewed journal.

3. (OpenTargets Search: resistance to thyroid hormone-THRB): Open Targets Query (resistance to thyroid hormone-THRB, 5 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

4. (persani20242024europeanthyroid pages 2-3): Luca Persani, Patrice Rodien, Carla Moran, W Edward Visser, Stefan Groeneweg, Robin Peeters, Samuel Refetoff, Mark Gurnell, Paolo Beck-Peccoz, and Krishna Chatterjee. 2024 european thyroid association guidelines on diagnosis and management of genetic disorders of thyroid hormone transport, metabolism and action. Jul 2024. URL: https://doi.org/10.1530/etj-24-0125, doi:10.1530/etj-24-0125. This article has 58 citations and is from a peer-reviewed journal.

5. (buyukyılmaz2024clinicalcharacteristicsand pages 1-1): Gönül Büyükyılmaz, Büşranur Çavdarlı, Serkan Bilge Koca, Keziban Toksoy Adıgüzel, Oya Topaloğlu, Cevdet Aydın, Sema Hepsen, Erman Çakal, Nur Semerci Gündüz, Mehmet Boyraz, Fatih Gürbüz, and Hüseyin Demirbilek. Clinical characteristics and genotype-phenotype correlation in turkish patients with a diagnosis of resistance to thyroid hormone beta. Journal of Clinical Research in Pediatric Endocrinology, 17:191-201, Dec 2024. URL: https://doi.org/10.4274/jcrpe.galenos.2024.2024-8-14, doi:10.4274/jcrpe.galenos.2024.2024-8-14. This article has 0 citations.

6. (belal20247684resistanceto pages 1-2): H. Belal, A. N. Mukhtar, and J. M. Chehade. 7684 resistance to thyroid hormone beta mistaken as primary hypothyroidism: variable phenotypes and diagnostic dilemmas. Journal of the Endocrine Society, Oct 2024. URL: https://doi.org/10.1210/jendso/bvae163.2063, doi:10.1210/jendso/bvae163.2063. This article has 0 citations and is from a peer-reviewed journal.

7. (buyukyılmaz2024clinicalcharacteristicsand pages 2-3): Gönül Büyükyılmaz, Büşranur Çavdarlı, Serkan Bilge Koca, Keziban Toksoy Adıgüzel, Oya Topaloğlu, Cevdet Aydın, Sema Hepsen, Erman Çakal, Nur Semerci Gündüz, Mehmet Boyraz, Fatih Gürbüz, and Hüseyin Demirbilek. Clinical characteristics and genotype-phenotype correlation in turkish patients with a diagnosis of resistance to thyroid hormone beta. Journal of Clinical Research in Pediatric Endocrinology, 17:191-201, Dec 2024. URL: https://doi.org/10.4274/jcrpe.galenos.2024.2024-8-14, doi:10.4274/jcrpe.galenos.2024.2024-8-14. This article has 0 citations.

8. (buyukyılmaz2024clinicalcharacteristicsand pages 3-3): Gönül Büyükyılmaz, Büşranur Çavdarlı, Serkan Bilge Koca, Keziban Toksoy Adıgüzel, Oya Topaloğlu, Cevdet Aydın, Sema Hepsen, Erman Çakal, Nur Semerci Gündüz, Mehmet Boyraz, Fatih Gürbüz, and Hüseyin Demirbilek. Clinical characteristics and genotype-phenotype correlation in turkish patients with a diagnosis of resistance to thyroid hormone beta. Journal of Clinical Research in Pediatric Endocrinology, 17:191-201, Dec 2024. URL: https://doi.org/10.4274/jcrpe.galenos.2024.2024-8-14, doi:10.4274/jcrpe.galenos.2024.2024-8-14. This article has 0 citations.

9. (persani20242024europeanthyroid pages 3-5): Luca Persani, Patrice Rodien, Carla Moran, W Edward Visser, Stefan Groeneweg, Robin Peeters, Samuel Refetoff, Mark Gurnell, Paolo Beck-Peccoz, and Krishna Chatterjee. 2024 european thyroid association guidelines on diagnosis and management of genetic disorders of thyroid hormone transport, metabolism and action. Jul 2024. URL: https://doi.org/10.1530/etj-24-0125, doi:10.1530/etj-24-0125. This article has 58 citations and is from a peer-reviewed journal.

10. (hones2024comparativephenotypingof pages 5-9): G. S. Hönes, Daniela Geist, Christina Wenzek, Paul T. Pfluger, T. Müller, J. A. Aguilar-Pimentel, O. Amarie, L. Becker, Natalia Dragano, Lillian Garrett, S. Hölter, B. Rathkolb, J. Rozman, N. Spielmann, Irina Treise, Eckhard Wolf, Wolfgang Wurst, H. Fuchs, V. Gailus-Durner, M. Hrabě de Angelis, Dagmar Führer, and L. C. Moeller. Comparative phenotyping of mice reveals canonical and noncanonical physiological functions of trα and trβ. bioRxiv, Nov 2024. URL: https://doi.org/10.1101/2023.11.26.568063, doi:10.1101/2023.11.26.568063. This article has 8 citations.

## Artifacts

- [Edison artifact artifact-00](Generalized_Resistance_to_Thyroid_Hormone-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 4 |
| Resolved | 4 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 4 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.