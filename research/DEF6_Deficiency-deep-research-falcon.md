---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-27T16:19:40.320263'
end_time: '2026-08-27T16:33:11.600291'
duration_seconds: 811.28
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: DEF6 Deficiency
  mondo_id: ''
  category: Genetic
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 14
reference_validation:
  total_references: 5
  verified: 5
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 5
  on_topic: 2
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: DEF6_Deficiency-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** DEF6 Deficiency
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **DEF6 Deficiency** covering all of the
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
- **Disease Name:** DEF6 Deficiency
- **MONDO ID:**  (if available)
- **Category:** Genetic

## Research Objectives

Please provide a comprehensive research report on **DEF6 Deficiency** covering all of the
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


# DEF6 Deficiency: Disease-Characteristics Research Report

## Executive summary and evidence limits

DEF6 deficiency is an **ultra-rare, autosomal-recessive inborn error of immunity (IEI)** caused by biallelic loss-of-function/hypomorphic variants in **DEF6**. It combines immunodeficiency with severe, usually infantile immune dysregulation—particularly autoimmune enteropathy, systemic autoimmunity, lymphoproliferation, hypogammaglobulinemia, poor specific-antibody responses, and recurrent infections. The defining human evidence remains the July 2019 *Nature Communications* report of **three patients from two unrelated families**; therefore, percentages below are descriptive fractions of this tiny ascertainment cohort, not population estimates. Recent 2023–2024 literature mainly places the disorder among CTLA-4-pathway Tregopathies and has not supplied a substantially larger DEF6-specific cohort. (serwas2019humandef6deficiency pages 2-3, serwas2019humandef6deficiency pages 9-10, sogkas2021cellularandmolecular pages 4-5)

| Domain | Summary | Evidence type | Key citations |
|---|---|---|---|
| Evidence base | Ultra-rare monogenic inborn error of immunity described in a foundational 2019 report of 3 affected individuals from 2 unrelated families; later literature is mainly review/contextual, with no large dedicated cohort or trial identified. | Direct human cohort + later expert review | (serwas2019humandef6deficiency pages 2-3, serwas2019humandef6deficiency pages 1-2, serwas2019humandef6deficiency pages 15-15) |
| Inheritance / variants | Autosomal recessive pattern supported by biallelic homozygous DEF6 missense variants in consanguineous families: family A c.991G>A p.Glu331Lys (2 siblings), family B c.628T>G p.Tyr210Asp (1 patient). Both were reported as damaging and absent in homozygous state in ExAC/gnomAD/TOPMed in the source paper. | Direct human genetic evidence | (serwas2019humandef6deficiency pages 3-5) |
| Core phenotype | Early-onset systemic autoimmunity with immunodeficiency: severe enteropathy/diarrhea, bowel inflammation, hepatosplenomegaly or hepatomegaly/cholestasis, cardiomyopathy/cardiac malformations, recurrent infections, and autoimmune hematologic disease in one patient. One sibling died in infancy from cardiomyopathy-related multiorgan failure. | Direct human clinical evidence | (serwas2019humandef6deficiency pages 2-3, serwas2019humandef6deficiency pages 10-11, serwas2019humandef6deficiency pages 1-2) |
| Laboratory phenotype | Reported abnormalities included reduced CD8+ T cells, reduced Tregs, few class-switched B cells, decreased mature NK cells, hypogammaglobulinemia with poor vaccine responses, positive autoantibodies/autoimmune markers (ANCA, cardiolipin, beta2-glycoprotein, positive direct Coombs), while neutrophil phagocytosis and oxidative burst were normal. | Direct human immunology/lab evidence | (serwas2019humandef6deficiency pages 2-3, serwas2019humandef6deficiency pages 3-5) |
| Mechanism | DEF6 deficiency impairs CTLA-4 homeostasis in T cells by disrupting DEF6-RAB11 interaction, reducing RAB11+CTLA-4 recycling vesicles, CTLA-4 cycling, ligand uptake/transendocytosis, and functional surface CTLA-4 availability. Variants also reduce DEF6 protein abundance/stability, especially p.Tyr210Asp. | Direct human cellular evidence + engineered cell validation | (serwas2019humandef6deficiency pages 8-9, serwas2019humandef6deficiency pages 9-10, serwas2019humandef6deficiency pages 7-8, serwas2019humandef6deficiency pages 7-7, serwas2019humandef6deficiency pages 6-7) |
| Diagnosis | Supported approach from available evidence: molecular sequencing confirming biallelic DEF6 variants in patients with early immune dysregulation plus functional corroboration using CTLA-4 trafficking/cycling or ligand-uptake assays in T cells when available. No disease-specific formal diagnostic criteria, screening program, or validated biomarker panel was identified. | Direct human evidence + expert extrapolation | (serwas2019humandef6deficiency pages 1-2, serwas2019humandef6deficiency pages 10-11, sogkas2021cellularandmolecular pages 4-5) |
| Treatment | Directly reported care included immunoglobulin replacement, antibiotics/anti-infectives, conventional immunosuppression for autoimmune complications, and targeted CTLA-4-Ig (abatacept). One patient treated from 15 months had marked improvement and sustained remission over ~4 years. No DEF6-specific HSCT, gene therapy, RNA therapy, or trial evidence was identified. | Direct human treatment evidence | (serwas2019humandef6deficiency pages 2-3, serwas2019humandef6deficiency pages 1-2, serwas2019humandef6deficiency pages 10-11) |
| Prognosis | Clinical course appears severe and variable: 1 of 3 known patients died in infancy; another had sustained remission of autoimmunity and stable cardiorespiratory status on abatacept; persistent infection susceptibility remained a concern despite supportive therapy. Long-term survival, penetrance, and natural-history estimates are unknown. | Direct human follow-up evidence | (serwas2019humandef6deficiency pages 2-3, serwas2019humandef6deficiency pages 10-11) |
| Major knowledge gaps | No verified disease-specific population prevalence/incidence, no large natural-history study, no robust genotype-phenotype map, no established penetrance estimate, no DEF6-specific interventional trial, no validated prevention strategy, and no standardized diagnostic or management guideline. Mouse/model work suggests broader roles in T-cell signaling, TFH/TH17 biology, lupus-like disease, arthritis, and osteoclastogenesis, but these are not yet equivalent to proven human disease features. | Explicit gap statement with model/extrapolation boundary | (serwas2019humandef6deficiency pages 9-10, manni2017regulationofsystemic pages 6-7, binder2017def6restrainsosteoclastogenesis pages 6-8, binder2017def6restrainsosteoclastogenesis pages 3-4) |


*Table: This table provides a compact disease knowledge-base summary for DEF6 deficiency, separating direct human evidence from model-based extrapolation. It is useful for quickly identifying what is established, what is clinically actionable, and where major evidence gaps remain.*

## 1. Disease information

### Definition

DEF6 deficiency is a monogenic immune-regulatory disorder in which defective DEF6-dependent vesicular trafficking reduces functional **CTLA-4** availability on activated conventional and regulatory T cells. Loss of this inhibitory checkpoint causes systemic autoimmunity, while broader T- and B-cell abnormalities confer susceptibility to infection. It is best classified as an **IEI with immune dysregulation/systemic autoimmunity** and, mechanistically, a secondary CTLA-4 trafficking disorder or Tregopathy. (serwas2019humandef6deficiency pages 1-2, serwas2019humandef6deficiency pages 9-10, sogkas2021cellularandmolecular pages 4-5)

### Names and identifiers

- Preferred name: **DEF6 deficiency**.
- Descriptive synonym: **immunodeficiency syndrome with systemic autoimmunity and aberrant CTLA-4 homeostasis**.
- Gene/protein aliases: **differentially expressed in FDCP6 homolog**, **SLAT** (“SWAP-70-like adaptor of T cells”), and **IBP** (“IRF4-binding protein”). (serwas2019humandef6deficiency pages 15-15, serwas2019humandef6deficiency pages 1-2)
- Disease-specific **MONDO, Orphanet, MeSH, ICD-10, and ICD-11 identifiers were not verified in the retrieved evidence**. A knowledge base should not substitute a generic immunodeficiency or autoimmunity code as if it were disease-specific.
- The disease appears to correspond to the OMIM phenotype commonly called *immunodeficiency 68 with or without autoimmunity*, but its numerical OMIM identifier was not established by the retrieved primary text and should be verified directly against current OMIM before ingestion.

The primary data are **individual-patient research records**, pathology, immunophenotyping, sequencing, and functional experiments, not EHR-scale or registry-level aggregated data. Later sources are disease-level reviews.

### Foundational citation and abstract quotation

Serwas NK et al., “Human DEF6 deficiency underlies an immunodeficiency syndrome with systemic autoimmunity and aberrant CTLA-4 homeostasis,” *Nature Communications* 10:3106, published July 2019. DOI/URL: https://doi.org/10.1038/s41467-019-10812-x. The PMID was not present in the retrieved full text and should be checked in PubMed rather than guessed. (serwas2019humandef6deficiency pages 15-15, serwas2019humandef6deficiency pages 14-15)

The abstract states: **“Here, we identify biallelic mutations in three patients from two unrelated families … as the molecular cause of an inborn error of immunity with systemic autoimmunity.”** It further reports that **“Patient T cells exhibit impaired regulation of CTLA-4 surface trafficking associated with reduced functional CTLA-4 availability.”** (serwas2019humandef6deficiency pages 1-2)

## 2. Etiology, risk, protection, and gene–environment interaction

### Causal factor

The primary cause is **germline biallelic DEF6 dysfunction**. Two homozygous missense variants were reported:

1. **c.991G>A, p.Glu331Lys (E331K)** in two siblings from family A, affecting the PH–DH region and reducing protein abundance and RAB11 binding.
2. **c.628T>G, p.Tyr210Asp (Y210D)** in one patient from family B, causing marked protein instability; proteasome inhibition restored mutant protein in vitro. (serwas2019humandef6deficiency pages 3-5, serwas2019humandef6deficiency pages 9-10, serwas2019humandef6deficiency pages 5-6)

Both were predicted damaging and were absent in homozygous form from ExAC, gnomAD, and TOPMed in the 2019 analysis. They should be curated as disease-associated, functionally supported biallelic variants; current ClinVar assertions and ACMG classifications require direct database verification. (serwas2019humandef6deficiency pages 3-5)

### Risk factors

- **Genetic:** two pathogenic/hypomorphic alleles; parental consanguinity and an affected sibling are major family-level risk indicators. Family A was Pakistani and consanguineous; family B had consanguineous Iraqi parents. (serwas2019humandef6deficiency pages 2-3, serwas2019humandef6deficiency pages 1-2)
- **Environmental/lifestyle:** no toxins, diet, smoking, alcohol, occupation, radiation, sex-specific exposure, or lifestyle factor has been shown to cause DEF6 deficiency.
- **Infection as trigger:** infection is not the primary cause, but immune challenges may reveal disease. In P3, autoimmune hemolytic anemia appeared during CMV infection; this is compatible with infection-triggered expression of autoimmunity but does not establish a general gene–environment interaction. (serwas2019humandef6deficiency pages 2-3)
- **Modifiers:** no validated modifier genes, protective alleles, environmental protective factors, or epigenetic modifiers have been reported.

## 3. Phenotypes

Frequencies are calculated from the three published patients only and are therefore highly unstable.

### Core clinical and laboratory features

- **Infantile onset:** all three had clinically important disease during infancy (3/3). P1 developed watery diarrhea in the first month; P2 had neonatal/premature multisystem disease; P3 presented at seven months. Suggested HPO: **HP:0003593 Infantile onset**. (serwas2019humandef6deficiency pages 2-3, serwas2019humandef6deficiency pages 10-11)
- **Enteropathy/diarrhea:** severe watery diarrhea, bowel inflammation, villous atrophy, T-cell/eosinophilic infiltration, rectal/perianal lesions, or necrotizing enterocolitis-like intestinal disease occurred in both family-A siblings (2/3). Suggested HPO: **Chronic diarrhea**, **Enteropathy**, **Villous atrophy**, **Abnormality of the gastrointestinal tract**. Course was severe and chronic before targeted therapy. (serwas2019humandef6deficiency pages 2-3, serwas2019humandef6deficiency pages 10-11, serwas2019humandef6deficiency pages 1-2)
- **Recurrent infections:** reported across the cohort, involving bacterial, viral, and fungal organisms. Documented organisms included *Streptococcus pneumoniae*, *Staphylococcus aureus*, *Enterobacter aerogenes*, *Enterococcus faecalis*, rhinovirus, influenza B, RSV, rotavirus, CMV, and *Malassezia furfur*. Suggested HPO: **HP:0002719 Recurrent infections**, **Recurrent respiratory infections**, **Viral infection**, **Fungal infection**. (serwas2019humandef6deficiency pages 3-5)
- **Liver/lymphoid-organ disease:** hepatomegaly or hepatosplenomegaly occurred in the family-A patients; P2 developed cholestasis and liver failure. Suggested HPO: **HP:0002240 Hepatomegaly**, **HP:0001744 Splenomegaly**, **HP:0001396 Cholestasis**, **Liver failure**. (serwas2019humandef6deficiency pages 2-3, serwas2019humandef6deficiency pages 10-11)
- **Cardiac disease:** the siblings had cardiomyopathy and/or congenital structural heart disease; P2 had atrioventricular septal defect, progressive heart failure and pacemaker requirement, while P1 had biventricular hypertrophy and atrial septal defect. Suggested HPO: **HP:0001638 Cardiomyopathy**, **HP:0001631 Atrial septal defect**, **HP:0006695 Atrioventricular septal defect**, **HP:0001635 Congestive heart failure**. Whether congenital heart anomalies are intrinsic DEF6 manifestations remains uncertain because only one family was affected. (serwas2019humandef6deficiency pages 10-11)
- **Autoimmune cytopenia:** P3 developed autoimmune hemolytic anemia during CMV infection (1/3); direct Coombs positivity was also recorded. Suggested HPO: **HP:0001890 Autoimmune hemolytic anemia**, **Positive direct antiglobulin test**. (serwas2019humandef6deficiency pages 2-3, serwas2019humandef6deficiency pages 3-5)
- **Autoantibodies:** ANCA, anticardiolipin, anti-β2-glycoprotein and smooth-muscle antibodies were reported. Suggested HPO: **HP:0002960 Autoimmunity**, **Abnormal circulating autoantibody concentration**. (serwas2019humandef6deficiency pages 2-3, serwas2019humandef6deficiency pages 3-5)
- **Immunologic abnormalities:** T-cell/CD8 lymphopenia, reduced CD25-high/CD127-low/FOXP3-positive Tregs, low class-switched memory B cells, decreased mature NK cells, hypogammaglobulinemia and poor tetanus/pneumococcal antibody responses were found variably. P1 had IgG 1.60 g/L, IgA 0.009 g/L and IgM 0.17 g/L at one assessment; neutrophil phagocytosis and oxidative burst were normal. Suggested HPO: **HP:0005403 T-cell lymphopenia**, **HP:0004313 Decreased circulating antibody level**, **Hypogammaglobulinemia**, **Impaired specific antibody response**, **Decreased switched memory B-cell count**, and **Decreased regulatory T-cell count**. (serwas2019humandef6deficiency pages 2-3, serwas2019humandef6deficiency pages 3-5)

### Severity, progression, and quality of life

Severity ranged from life-threatening infantile multiorgan disease to treatable chronic immune dysregulation. Enteropathy impaired nutrition and required intensive care/parenteral nutrition in P2; recurrent infection and cardiopulmonary disease increased care burden. No EQ-5D, SF-36, PROMIS, developmental, educational, or formal disability measurements have been published. One patient died at 10.5 months; P1 achieved sustained control of autoimmunity with abatacept. (serwas2019humandef6deficiency pages 2-3, serwas2019humandef6deficiency pages 10-11)

## 4. Genetic and molecular information

- **Causal gene:** **DEF6**; HGNC/NCBI Gene/Ensembl/OMIM gene numbers should be imported from their current authoritative records rather than inferred from this literature set.
- **Inheritance:** autosomal recessive; variants are constitutional/germline, not somatic. (serwas2019humandef6deficiency pages 1-2, serwas2019humandef6deficiency pages 3-5)
- **Variant classes:** both known disease alleles are missense variants with partial or severe loss of protein/function. E331K is defective in RAB11 interaction and functional rescue; Y210D is strongly destabilized. Thus, the most defensible functional annotation is **loss of function/hypomorphic loss of function**, not gain of function or dominant negative. (serwas2019humandef6deficiency pages 5-6, serwas2019humandef6deficiency pages 8-9, serwas2019humandef6deficiency pages 9-10)
- **Population frequency:** no homozygotes in the population resources queried in 2019; exact allele frequencies were not available in the retrieved excerpts. (serwas2019humandef6deficiency pages 3-5)
- **Protein architecture:** DEF6 contains an N-terminal EF-hand, ITAM-like sequence, phosphoinositide-binding PH domain and C-terminal DH-like GEF region. Resting DEF6 is autoinhibited; TCR engagement and LCK-mediated phosphorylation open the molecule and recruit it to the immunological synapse. (binder2017def6restrainsosteoclastogenesis pages 3-4, binder2017def6restrainsosteoclastogenesis pages 11-12, manni2017regulationofsystemic pages 12-14)
- **Modifier genes, epigenetics, and chromosomal abnormalities:** none established. There is no evidence that aneuploidy, translocation, inversion, methylation disorder, repeat expansion, or mitochondrial mutation causes this phenotype.

## 5. Environmental and infectious information

There is no evidence for a primary environmental, toxic, dietary, occupational, radiation, or lifestyle etiology. Infectious agents are **complications or possible immune triggers**, not inherited-cause substitutes. CMV coincided with hemolytic anemia in P3, while respiratory, enteric, bacterial and fungal infections reflected immunodeficiency. No zoonotic or transmissible form exists. (serwas2019humandef6deficiency pages 2-3, serwas2019humandef6deficiency pages 3-5)

## 6. Mechanism and pathophysiology

### Principal human causal chain

**Biallelic DEF6 variant → reduced/unstable DEF6 or impaired PH–DH function → defective binding/GEF activity toward RAB11 → loss of RAB11-positive CTLA-4 recycling vesicles → impaired CTLA-4 cycling to the T-cell surface → reduced CD80/CD86 capture and transendocytosis → inadequate inhibition of antigen-presenting-cell/T-cell costimulation → systemic autoimmunity and lymphoproliferation.** Parallel defects in T-cell signaling, lymphocyte composition and antibody responses contribute to infection susceptibility. (serwas2019humandef6deficiency pages 8-9, serwas2019humandef6deficiency pages 9-10, serwas2019humandef6deficiency pages 7-8, serwas2019humandef6deficiency pages 7-7)

The evidence is unusually strong for an ultra-rare disease: patient CD4 T cells and memory Tregs had impaired CTLA-4 cycling; CRISPR DEF6-knockout Jurkat cells phenocopied the defect; wild-type DEF6 rescued it, whereas E331K did not; RAB11 abundance itself was normal; and co-immunoprecipitation established DEF6–RAB11 interaction. (serwas2019humandef6deficiency pages 8-9, serwas2019humandef6deficiency pages 7-8, serwas2019humandef6deficiency pages 6-7, serwas2019humandef6deficiency pages 9-9)

Suggested annotations:

- GO biological processes: **T-cell receptor signaling**, **regulation of immune response**, **vesicle-mediated transport**, **recycling endosome organization**, **regulation of T-cell activation**, **small-GTPase-mediated signal transduction**, **actin cytoskeleton organization**, and **calcium-mediated signaling**.
- GO cellular components: **immunological synapse**, **recycling endosome**, **cytoplasmic vesicle**, **plasma membrane**, **cytosol**, and **nucleus**.
- Cell Ontology: **CL:0000084 T cell**, **CL:0000815 regulatory T cell**, **CL:0000624 CD4-positive alpha-beta T cell**, **CL:0000785 mature B cell**, **CL:0000623 natural killer cell**, **CL:0000235 macrophage**, and **CL:0000092 osteoclast**.

### Additional DEF6 biology—model or contextual evidence

In T cells, DEF6 activates RAC and CDC42, regulates actin dynamics, synapse formation and Ca²⁺/NFAT signaling, sequesters IRF4, limits ROCK2-dependent IRF4 phosphorylation, and restrains TH17/IL-17/IL-21 and TFH programs. It also inhibits assembly of a p62–TRAF6–Raptor complex, thereby regulating mTORC1-dependent translation, including BCL6. These pathways plausibly modify the human phenotype but the RAB11–CTLA-4 defect is the mechanism directly demonstrated in patients. (manni2017regulationofsystemic pages 3-4, manni2017regulationofsystemic pages 12-14)

In myeloid/osteoclast models, DEF6 promotes an autocrine IFN-β brake on the c-FOS–NFATC1–BLIMP1 osteoclastogenic axis. Def6-null precursors are hypersensitive to RANKL and can undergo TNF-driven osteoclastogenesis; mice develop reduced trabecular bone and enhanced inflammatory erosion. These are credible downstream biological roles but osteoporosis or inflammatory arthritis has not yet been established as a recurrent human DEF6-deficiency phenotype. (binder2017def6restrainsosteoclastogenesis pages 9-11, binder2017def6restrainsosteoclastogenesis pages 6-8)

No disease-specific single-cell, spatial-transcriptomic, metabolomic, lipidomic, patient proteomic, organoid, iPSC, or multi-omics signature has been validated. The 2019 work used primary immune cells, conventional immunophenotyping, microscopy, co-immunoprecipitation and engineered cell models rather than clinical multi-omics.

## 7. Anatomical structures affected

Directly observed sites include:

- **Immune/lymphoid system:** circulating T, B and NK cells; spleen and lymphoid compartments. Suggested UBERON: blood, spleen, lymph node, thymus.
- **Gastrointestinal tract:** stomach, duodenum, colon, rectum/perianal region; mucosa and villi were affected. Suggested UBERON: stomach, duodenum, colon, rectum, intestinal mucosa, intestinal villus. (serwas2019humandef6deficiency pages 2-3, serwas2019humandef6deficiency pages 1-2)
- **Liver:** hepatomegaly, cholestasis and liver failure in severe disease. Suggested UBERON: liver, intrahepatic biliary system. (serwas2019humandef6deficiency pages 10-11)
- **Heart:** myocardium and septal structures in family A. Suggested UBERON: heart, myocardium, atrial septum, ventricular septum. (serwas2019humandef6deficiency pages 10-11)
- **Bone in models:** trabecular bone and osteoclast surfaces; human relevance remains unproven. (binder2017def6restrainsosteoclastogenesis pages 6-8)

At the subcellular level, the critical sites are the **recycling endosome, CTLA-4-positive vesicle, immunological synapse, plasma membrane, cytosol and nucleus**. No consistent lateralization is applicable.

## 8. Temporal development and natural history

Typical recognized onset is **congenital/infantile**, often chronic and multisystemic. The course can be progressive, episodic with infections, or treatment-responsive. P1 began with diarrhea during the first month; P3 presented at seven months; P2 had severe neonatal/infantile disease and died at 10.5 months. (serwas2019humandef6deficiency pages 2-3, serwas2019humandef6deficiency pages 10-11)

No validated stages exist. A pragmatic clinical sequence is: early infection/enteropathy or autoimmune cytopenia → evolving lymphoproliferation, antibody deficiency and systemic autoimmunity → organ complications. Remission may be treatment-induced: P1's bowel inflammation improved within approximately one month of abatacept, and no overt autoimmune recurrence was reported over about four years. No spontaneous-remission rate or critical intervention window has been quantified, although the observed infantile severity supports early genomic diagnosis and immune-directed treatment. (serwas2019humandef6deficiency pages 2-3)

## 9. Inheritance and population

- **Pattern:** autosomal recessive.
- **Penetrance:** apparently high among the three biallelic affected individuals, but numerically unknowable; age-dependent and organ-specific penetrance cannot be estimated.
- **Expressivity:** clearly variable, including lethal infantile cardiomyopathy/multiorgan failure, predominant enteropathy, and CMV-associated autoimmune hemolysis.
- **Anticipation, germline mosaicism and founder effect:** not reported.
- **Consanguinity:** present in both discovery families and important for case ascertainment, but not biologically required for autosomal-recessive disease. (serwas2019humandef6deficiency pages 2-3, serwas2019humandef6deficiency pages 1-2)
- **Prevalence/incidence/carrier frequency:** unknown; no cases-per-100,000 estimate or registry-based denominator exists.
- **Demographics:** two girls were siblings in a Pakistani family; P3 came from an Iraqi family. The dataset is too small to infer ethnicity, geography, sex ratio or age distribution. No sex-limited inheritance exists.

## 10. Diagnostics

### Clinical recognition

Consider DEF6 deficiency in an infant or child with a **CTLA-4/LRBA-like syndrome**: autoimmune enteropathy, autoimmune cytopenia, hepatosplenomegaly/lymphoproliferation, hypogammaglobulinemia or impaired vaccine responses, and recurrent infections—especially with consanguinity or similarly affected siblings. DEF6-mutated patients may lack some T-cell activation/exhaustion features described in CTLA4 or LRBA disease, so phenotype alone is insufficient. (serwas2019humandef6deficiency pages 9-10, sogkas2021cellularandmolecular pages 4-5)

### Recommended work-up

1. CBC with differential; lymphocyte subsets and naïve/memory phenotyping.
2. Quantitative IgG/IgA/IgM and vaccine-specific antibodies.
3. Treg enumeration using an age-appropriate CD4/CD25-high/CD127-low/FOXP3 panel.
4. Autoimmune testing guided by presentation: direct antiglobulin test, hemolysis profile, ANCA, antiphospholipid and organ-specific antibodies.
5. Microbiological testing, including CMV/EBV where clinically indicated.
6. Fecal calprotectin, endoscopy and intestinal biopsy for severe diarrhea; biopsy may show villous atrophy and lymphocytic/eosinophilic infiltration.
7. Cardiac echocardiography/ECG where symptoms or family history warrant it; liver chemistry and imaging for hepatobiliary disease. (serwas2019humandef6deficiency pages 2-3, serwas2019humandef6deficiency pages 3-5, serwas2019humandef6deficiency pages 10-11)

### Genetic diagnosis

Use an IEI/immune-dysregulation panel containing **DEF6**, **CTLA4**, **LRBA** and other Tregopathy/autoimmune-lymphoproliferation genes, or trio WES/WGS when the phenotype is broad. Confirm candidate variants by an orthogonal method and test segregation. Single-gene sequencing is efficient when a familial DEF6 variant is known. Copy-number analysis should accompany sequencing where technically possible. CMA, karyotype, FISH, mitochondrial and repeat-expansion testing are not first-line unless another diagnosis is suspected.

Functional confirmation may include DEF6 protein abundance, stimulated CTLA-4 expression/cycling, CD80/CD86 uptake or transendocytosis, and RAB11–CTLA-4 colocalization in specialized laboratories. These are research-supported assays, not standardized diagnostic criteria. (serwas2019humandef6deficiency pages 8-9, serwas2019humandef6deficiency pages 7-8, serwas2019humandef6deficiency pages 7-7, serwas2019humandef6deficiency pages 1-2)

### Differential diagnosis

Major differentials include **CTLA-4 haploinsufficiency**, **LRBA deficiency**, **FOXP3/IPEX**, activated PI3Kδ syndrome, STAT3 gain-of-function disease, autoimmune lymphoproliferative syndrome, common variable immunodeficiency, NBEAL2 deficiency with immune dysregulation, and monogenic inflammatory bowel disease. The strongest mechanistic mimics are CTLA4 and LRBA disorders because all reduce functional CTLA-4 checkpoint activity. (serwas2019humandef6deficiency pages 9-10, sogkas2021cellularandmolecular pages 4-5)

No population or newborn screening program exists. Cascade testing is appropriate after molecular diagnosis.

## 11. Outcome and prognosis

One of the three discovery patients died at 10.5 months from cardiomyopathy-associated multiorgan failure, giving a crude discovery-cohort mortality of **1/3**, which must not be interpreted as a population mortality rate. P1 remained without overt recurrent autoimmunity and had stable cardiorespiratory function approximately four years after starting abatacept. Persistent infection susceptibility can continue despite immunoglobulin replacement and immune control. (serwas2019humandef6deficiency pages 2-3)

No five- or ten-year survival rate, median life expectancy, validated prognostic score, disability scale, or prognostic biomarker exists. Plausible adverse indicators include neonatal onset, severe enteropathy, cardiomyopathy, liver failure, recurrent sepsis, profound lymphopenia and uncontrolled autoimmunity, but none has been validated statistically.

## 12. Treatment and current implementation

Treatment is individualized in an expert pediatric immunology/IEI center.

- **Abatacept (CTLA-4-Ig):** the principal mechanism-directed therapy. P1 began four-weekly abatacept at 15 months. Bowel inflammation improved within about one month, villous atrophy and lymphocytic infiltration resolved, perianal lesions reversed, and remission persisted for approximately four years. This is compelling single-patient precision-medicine evidence, not a response-rate trial. Suggested NCIt term: **Abatacept** / **CTLA-4 immunoglobulin**. (serwas2019humandef6deficiency pages 2-3, serwas2019humandef6deficiency pages 1-2)
- **Immunoglobulin replacement:** used for low immunoglobulins and poor vaccine titers; all reported patients received regular immunoglobulin treatment. Suggested NCIt: **Intravenous Immunoglobulin Therapy** or **Immunoglobulin Replacement Therapy**. (serwas2019humandef6deficiency pages 2-3, serwas2019humandef6deficiency pages 10-11)
- **Anti-infective therapy:** organism-directed antibiotics and antivirals; P3 received ganciclovir/valganciclovir for CMV. Suggested NCIt: **Antibiotic Therapy**, **Antiviral Therapy**, **Ganciclovir**, **Valganciclovir**. (serwas2019humandef6deficiency pages 2-3)
- **Conventional immunosuppression:** corticosteroids and azathioprine were used for autoimmune hemolytic anemia. Suggested NCIt: **Corticosteroid Therapy**, **Azathioprine**. (serwas2019humandef6deficiency pages 2-3)
- **Organ-supportive care:** nutritional therapy, management of heart failure and structural cardiac disease, and liver/critical-care support according to phenotype. P1 received enalapril, atenolol, spironolactone and furosemide for cardiac disease. (serwas2019humandef6deficiency pages 10-11)

No DEF6-specific randomized trial, approved gene therapy, CRISPR therapy, RNA therapy, CAR-T approach, or published DEF6-specific hematopoietic stem-cell transplantation outcome was identified. HSCT may be discussed by analogy with severe immune-dysregulation IEIs, but efficacy and risk in DEF6 deficiency are unknown. Abatacept can itself contribute to infection risk, requiring surveillance. (serwas2019humandef6deficiency pages 9-10)

## 13. Prevention

The genetic defect cannot presently be prevented by lifestyle modification.

- **Primary prevention/family planning:** genetic counseling, parental carrier testing, reproductive options including preimplantation genetic testing and prenatal diagnosis once familial variants are known.
- **Secondary prevention:** cascade testing of siblings and relatives; prompt evaluation of infants at 25% Mendelian recurrence risk; early immune, gastrointestinal, hepatic and cardiac assessment.
- **Tertiary prevention:** immunoglobulin replacement where indicated, rapid treatment of infections, vaccination planning under immunology guidance, monitoring for CMV/other opportunistic infection when immunosuppressed, surveillance for enteropathy, cytopenias, liver disease and cardiac dysfunction, and early control of autoimmunity.

No DEF6-specific vaccine, antimicrobial-prophylaxis regimen, public-health program, newborn screen or evidence-based behavioral intervention exists. Live-vaccine decisions must be individualized to immune competence rather than inferred solely from genotype.

## 14. Other species and natural disease

The human disorder is not infectious or zoonotic. No naturally occurring veterinary DEF6-deficiency syndrome or breed association was identified. The principal comparative species is **mouse (*Mus musculus*, NCBI Taxon 10090)**, which has the ortholog **Def6**. Ortholog-specific NCBI Gene and VBO identifiers require direct database retrieval.

Evolutionary conservation is supported by shared roles in lymphocyte signaling and autoimmunity, but mouse manifestations are highly background-dependent. Consequently, mouse lupus, arthritis and bone phenotypes should be annotated as comparative-model evidence—not natural human manifestations. (biswas2010irf4andits pages 14-15, binder2017def6restrainsosteoclastogenesis pages 3-4)

## 15. Model organisms and experimental systems

### Mouse models

- **Def6-null, mixed 129/B6 background:** approximately 60% of females developed lupus-like disease by five months, including lymphadenopathy, splenomegaly, hypergammaglobulinemia, anti-dsDNA antibodies and glomerulonephritis. (biswas2010irf4andits pages 14-15)
- **Def6-null × DO11.10 TCR-transgenic BALB/c:** RA-like disease began around two months, with symmetric joint swelling, synovitis, pannus, cartilage/subchondral bone destruction, rheumatoid factor and anti-CCP antibodies. (biswas2010irf4andits pages 14-15, biswas2010irf4andits pages 15-16)
- **Def6/Swap70 double knockout:** female-biased systemic autoimmunity, TFH/TH17 expansion, aged/atypical CD11c-positive T-bet-positive B-cell accumulation, anti-DNA/nuclear antibodies and immune-complex glomerulonephritis; IL-21 signaling is important. (manni2017regulationofsystemic pages 6-7, manni2017regulationofsystemic pages 7-9)
- **C57BL/6 Def6-null:** may lack spontaneous autoantibodies/systemic disease, highlighting strain effects. Independently, these mice show excessive RANKL/TNF-driven osteoclastogenesis, osteopenia and inflammatory bone erosion. (binder2017def6restrainsosteoclastogenesis pages 6-8, binder2017def6restrainsosteoclastogenesis pages 3-4)

### Cellular models

Primary patient PBMCs/CD4 T cells, feeder-expanded T cells, CRISPR DEF6-knockout Jurkat cells, reconstitution with wild-type or E331K DEF6, and HEK293T co-immunoprecipitation systems established the RAB11–CTLA-4 trafficking mechanism. Wild-type—but not mutant—DEF6 rescued trafficking, satisfying a strong functional-causality criterion. (serwas2019humandef6deficiency pages 8-9, serwas2019humandef6deficiency pages 9-10, serwas2019humandef6deficiency pages 7-8)

### Model limitations

Mouse disease depends strongly on strain, sex, TCR transgene and concurrent Swap70 loss. Mice prominently model lupus, arthritis and bone loss, whereas the known human syndrome emphasizes infantile enteropathy, infections, antibody deficiency and CTLA-4 trafficking. Jurkat and overexpression systems clarify molecular interactions but cannot reproduce tissue-level disease, development, infection susceptibility or treatment toxicity.

## Current assessment and priority research needs

The most authoritative interpretation is that DEF6 deficiency is a **RAB11-dependent CTLA-4 recycling disorder with broader TCR-signaling effects**. The abatacept response is a notable real-world example of mechanism-guided therapy, but it rests on one treated patient. Priorities are international case aggregation, standardized phenotyping and CTLA-4 functional assays, contemporary ClinVar/gnomAD curation, longitudinal infection and malignancy surveillance, formal HSCT evaluation, and genotype–phenotype studies. Larger cohorts are explicitly required to define the full clinical spectrum. (serwas2019humandef6deficiency pages 2-3, serwas2019humandef6deficiency pages 9-10)

### Evidence-source hierarchy

- **Direct human clinical/genetic:** Serwas et al., July 2019, DOI https://doi.org/10.1038/s41467-019-10812-x. (serwas2019humandef6deficiency pages 2-3, serwas2019humandef6deficiency pages 1-2)
- **Current expert synthesis:** Sogkas et al., published April 2021, DOI https://doi.org/10.1038/s41423-020-00626-z; 2024 Tregopathy reviews support current placement but do not materially enlarge the DEF6 cohort. (sogkas2021cellularandmolecular pages 4-5)
- **Mechanistic/model literature:** Binder et al., May 2017, DOI https://doi.org/10.4049/jimmunol.1601716; Manni et al., November 2017, DOI https://doi.org/10.1016/j.cellimm.2017.05.010. (binder2017def6restrainsosteoclastogenesis pages 3-4, manni2017regulationofsystemic pages 6-7)

References

1. (serwas2019humandef6deficiency pages 2-3): Nina K. Serwas, Birgit Hoeger, Rico C. Ardy, Sigrun V. Stulz, Zhenhua Sui, Nima Memaran, Marie Meeths, Ana Krolo, Özlem Yüce Petronczki, Laurène Pfajfer, Tie Z. Hou, Neil Halliday, Elisangela Santos-Valente, Artem Kalinichenko, Alan Kennedy, Emily M. Mace, Malini Mukherjee, Bianca Tesi, Anna Schrempf, Winfried F. Pickl, Joanna I. Loizou, Renate Kain, Bettina Bidmon-Fliegenschnee, Jean-Nicolas Schickel, Salomé Glauzy, Jakob Huemer, Wojciech Garncarz, Elisabeth Salzer, Iro Pierides, Ivan Bilic, Jens Thiel, Peter Priftakis, Pinaki P. Banerjee, Elisabeth Förster-Waldl, David Medgyesi, Wolf-Dietrich Huber, Jordan S. Orange, Eric Meffre, David M. Sansom, Yenan T. Bryceson, Amnon Altman, and Kaan Boztug. Human def6 deficiency underlies an immunodeficiency syndrome with systemic autoimmunity and aberrant ctla-4 homeostasis. Nature Communications, Jul 2019. URL: https://doi.org/10.1038/s41467-019-10812-x, doi:10.1038/s41467-019-10812-x. This article has 94 citations and is from a highest quality peer-reviewed journal.

2. (serwas2019humandef6deficiency pages 9-10): Nina K. Serwas, Birgit Hoeger, Rico C. Ardy, Sigrun V. Stulz, Zhenhua Sui, Nima Memaran, Marie Meeths, Ana Krolo, Özlem Yüce Petronczki, Laurène Pfajfer, Tie Z. Hou, Neil Halliday, Elisangela Santos-Valente, Artem Kalinichenko, Alan Kennedy, Emily M. Mace, Malini Mukherjee, Bianca Tesi, Anna Schrempf, Winfried F. Pickl, Joanna I. Loizou, Renate Kain, Bettina Bidmon-Fliegenschnee, Jean-Nicolas Schickel, Salomé Glauzy, Jakob Huemer, Wojciech Garncarz, Elisabeth Salzer, Iro Pierides, Ivan Bilic, Jens Thiel, Peter Priftakis, Pinaki P. Banerjee, Elisabeth Förster-Waldl, David Medgyesi, Wolf-Dietrich Huber, Jordan S. Orange, Eric Meffre, David M. Sansom, Yenan T. Bryceson, Amnon Altman, and Kaan Boztug. Human def6 deficiency underlies an immunodeficiency syndrome with systemic autoimmunity and aberrant ctla-4 homeostasis. Nature Communications, Jul 2019. URL: https://doi.org/10.1038/s41467-019-10812-x, doi:10.1038/s41467-019-10812-x. This article has 94 citations and is from a highest quality peer-reviewed journal.

3. (sogkas2021cellularandmolecular pages 4-5): Georgios Sogkas, Faranaz Atschekzei, Ignatius Ryan Adriawan, Natalia Dubrowinskaja, Torsten Witte, and Reinhold Ernst Schmidt. Cellular and molecular mechanisms breaking immune tolerance in inborn errors of immunity. Cellular and Molecular Immunology, 18:1122-1140, Apr 2021. URL: https://doi.org/10.1038/s41423-020-00626-z, doi:10.1038/s41423-020-00626-z. This article has 103 citations and is from a peer-reviewed journal.

4. (serwas2019humandef6deficiency pages 1-2): Nina K. Serwas, Birgit Hoeger, Rico C. Ardy, Sigrun V. Stulz, Zhenhua Sui, Nima Memaran, Marie Meeths, Ana Krolo, Özlem Yüce Petronczki, Laurène Pfajfer, Tie Z. Hou, Neil Halliday, Elisangela Santos-Valente, Artem Kalinichenko, Alan Kennedy, Emily M. Mace, Malini Mukherjee, Bianca Tesi, Anna Schrempf, Winfried F. Pickl, Joanna I. Loizou, Renate Kain, Bettina Bidmon-Fliegenschnee, Jean-Nicolas Schickel, Salomé Glauzy, Jakob Huemer, Wojciech Garncarz, Elisabeth Salzer, Iro Pierides, Ivan Bilic, Jens Thiel, Peter Priftakis, Pinaki P. Banerjee, Elisabeth Förster-Waldl, David Medgyesi, Wolf-Dietrich Huber, Jordan S. Orange, Eric Meffre, David M. Sansom, Yenan T. Bryceson, Amnon Altman, and Kaan Boztug. Human def6 deficiency underlies an immunodeficiency syndrome with systemic autoimmunity and aberrant ctla-4 homeostasis. Nature Communications, Jul 2019. URL: https://doi.org/10.1038/s41467-019-10812-x, doi:10.1038/s41467-019-10812-x. This article has 94 citations and is from a highest quality peer-reviewed journal.

5. (serwas2019humandef6deficiency pages 15-15): Nina K. Serwas, Birgit Hoeger, Rico C. Ardy, Sigrun V. Stulz, Zhenhua Sui, Nima Memaran, Marie Meeths, Ana Krolo, Özlem Yüce Petronczki, Laurène Pfajfer, Tie Z. Hou, Neil Halliday, Elisangela Santos-Valente, Artem Kalinichenko, Alan Kennedy, Emily M. Mace, Malini Mukherjee, Bianca Tesi, Anna Schrempf, Winfried F. Pickl, Joanna I. Loizou, Renate Kain, Bettina Bidmon-Fliegenschnee, Jean-Nicolas Schickel, Salomé Glauzy, Jakob Huemer, Wojciech Garncarz, Elisabeth Salzer, Iro Pierides, Ivan Bilic, Jens Thiel, Peter Priftakis, Pinaki P. Banerjee, Elisabeth Förster-Waldl, David Medgyesi, Wolf-Dietrich Huber, Jordan S. Orange, Eric Meffre, David M. Sansom, Yenan T. Bryceson, Amnon Altman, and Kaan Boztug. Human def6 deficiency underlies an immunodeficiency syndrome with systemic autoimmunity and aberrant ctla-4 homeostasis. Nature Communications, Jul 2019. URL: https://doi.org/10.1038/s41467-019-10812-x, doi:10.1038/s41467-019-10812-x. This article has 94 citations and is from a highest quality peer-reviewed journal.

6. (serwas2019humandef6deficiency pages 3-5): Nina K. Serwas, Birgit Hoeger, Rico C. Ardy, Sigrun V. Stulz, Zhenhua Sui, Nima Memaran, Marie Meeths, Ana Krolo, Özlem Yüce Petronczki, Laurène Pfajfer, Tie Z. Hou, Neil Halliday, Elisangela Santos-Valente, Artem Kalinichenko, Alan Kennedy, Emily M. Mace, Malini Mukherjee, Bianca Tesi, Anna Schrempf, Winfried F. Pickl, Joanna I. Loizou, Renate Kain, Bettina Bidmon-Fliegenschnee, Jean-Nicolas Schickel, Salomé Glauzy, Jakob Huemer, Wojciech Garncarz, Elisabeth Salzer, Iro Pierides, Ivan Bilic, Jens Thiel, Peter Priftakis, Pinaki P. Banerjee, Elisabeth Förster-Waldl, David Medgyesi, Wolf-Dietrich Huber, Jordan S. Orange, Eric Meffre, David M. Sansom, Yenan T. Bryceson, Amnon Altman, and Kaan Boztug. Human def6 deficiency underlies an immunodeficiency syndrome with systemic autoimmunity and aberrant ctla-4 homeostasis. Nature Communications, Jul 2019. URL: https://doi.org/10.1038/s41467-019-10812-x, doi:10.1038/s41467-019-10812-x. This article has 94 citations and is from a highest quality peer-reviewed journal.

7. (serwas2019humandef6deficiency pages 10-11): Nina K. Serwas, Birgit Hoeger, Rico C. Ardy, Sigrun V. Stulz, Zhenhua Sui, Nima Memaran, Marie Meeths, Ana Krolo, Özlem Yüce Petronczki, Laurène Pfajfer, Tie Z. Hou, Neil Halliday, Elisangela Santos-Valente, Artem Kalinichenko, Alan Kennedy, Emily M. Mace, Malini Mukherjee, Bianca Tesi, Anna Schrempf, Winfried F. Pickl, Joanna I. Loizou, Renate Kain, Bettina Bidmon-Fliegenschnee, Jean-Nicolas Schickel, Salomé Glauzy, Jakob Huemer, Wojciech Garncarz, Elisabeth Salzer, Iro Pierides, Ivan Bilic, Jens Thiel, Peter Priftakis, Pinaki P. Banerjee, Elisabeth Förster-Waldl, David Medgyesi, Wolf-Dietrich Huber, Jordan S. Orange, Eric Meffre, David M. Sansom, Yenan T. Bryceson, Amnon Altman, and Kaan Boztug. Human def6 deficiency underlies an immunodeficiency syndrome with systemic autoimmunity and aberrant ctla-4 homeostasis. Nature Communications, Jul 2019. URL: https://doi.org/10.1038/s41467-019-10812-x, doi:10.1038/s41467-019-10812-x. This article has 94 citations and is from a highest quality peer-reviewed journal.

8. (serwas2019humandef6deficiency pages 8-9): Nina K. Serwas, Birgit Hoeger, Rico C. Ardy, Sigrun V. Stulz, Zhenhua Sui, Nima Memaran, Marie Meeths, Ana Krolo, Özlem Yüce Petronczki, Laurène Pfajfer, Tie Z. Hou, Neil Halliday, Elisangela Santos-Valente, Artem Kalinichenko, Alan Kennedy, Emily M. Mace, Malini Mukherjee, Bianca Tesi, Anna Schrempf, Winfried F. Pickl, Joanna I. Loizou, Renate Kain, Bettina Bidmon-Fliegenschnee, Jean-Nicolas Schickel, Salomé Glauzy, Jakob Huemer, Wojciech Garncarz, Elisabeth Salzer, Iro Pierides, Ivan Bilic, Jens Thiel, Peter Priftakis, Pinaki P. Banerjee, Elisabeth Förster-Waldl, David Medgyesi, Wolf-Dietrich Huber, Jordan S. Orange, Eric Meffre, David M. Sansom, Yenan T. Bryceson, Amnon Altman, and Kaan Boztug. Human def6 deficiency underlies an immunodeficiency syndrome with systemic autoimmunity and aberrant ctla-4 homeostasis. Nature Communications, Jul 2019. URL: https://doi.org/10.1038/s41467-019-10812-x, doi:10.1038/s41467-019-10812-x. This article has 94 citations and is from a highest quality peer-reviewed journal.

9. (serwas2019humandef6deficiency pages 7-8): Nina K. Serwas, Birgit Hoeger, Rico C. Ardy, Sigrun V. Stulz, Zhenhua Sui, Nima Memaran, Marie Meeths, Ana Krolo, Özlem Yüce Petronczki, Laurène Pfajfer, Tie Z. Hou, Neil Halliday, Elisangela Santos-Valente, Artem Kalinichenko, Alan Kennedy, Emily M. Mace, Malini Mukherjee, Bianca Tesi, Anna Schrempf, Winfried F. Pickl, Joanna I. Loizou, Renate Kain, Bettina Bidmon-Fliegenschnee, Jean-Nicolas Schickel, Salomé Glauzy, Jakob Huemer, Wojciech Garncarz, Elisabeth Salzer, Iro Pierides, Ivan Bilic, Jens Thiel, Peter Priftakis, Pinaki P. Banerjee, Elisabeth Förster-Waldl, David Medgyesi, Wolf-Dietrich Huber, Jordan S. Orange, Eric Meffre, David M. Sansom, Yenan T. Bryceson, Amnon Altman, and Kaan Boztug. Human def6 deficiency underlies an immunodeficiency syndrome with systemic autoimmunity and aberrant ctla-4 homeostasis. Nature Communications, Jul 2019. URL: https://doi.org/10.1038/s41467-019-10812-x, doi:10.1038/s41467-019-10812-x. This article has 94 citations and is from a highest quality peer-reviewed journal.

10. (serwas2019humandef6deficiency pages 7-7): Nina K. Serwas, Birgit Hoeger, Rico C. Ardy, Sigrun V. Stulz, Zhenhua Sui, Nima Memaran, Marie Meeths, Ana Krolo, Özlem Yüce Petronczki, Laurène Pfajfer, Tie Z. Hou, Neil Halliday, Elisangela Santos-Valente, Artem Kalinichenko, Alan Kennedy, Emily M. Mace, Malini Mukherjee, Bianca Tesi, Anna Schrempf, Winfried F. Pickl, Joanna I. Loizou, Renate Kain, Bettina Bidmon-Fliegenschnee, Jean-Nicolas Schickel, Salomé Glauzy, Jakob Huemer, Wojciech Garncarz, Elisabeth Salzer, Iro Pierides, Ivan Bilic, Jens Thiel, Peter Priftakis, Pinaki P. Banerjee, Elisabeth Förster-Waldl, David Medgyesi, Wolf-Dietrich Huber, Jordan S. Orange, Eric Meffre, David M. Sansom, Yenan T. Bryceson, Amnon Altman, and Kaan Boztug. Human def6 deficiency underlies an immunodeficiency syndrome with systemic autoimmunity and aberrant ctla-4 homeostasis. Nature Communications, Jul 2019. URL: https://doi.org/10.1038/s41467-019-10812-x, doi:10.1038/s41467-019-10812-x. This article has 94 citations and is from a highest quality peer-reviewed journal.

11. (serwas2019humandef6deficiency pages 6-7): Nina K. Serwas, Birgit Hoeger, Rico C. Ardy, Sigrun V. Stulz, Zhenhua Sui, Nima Memaran, Marie Meeths, Ana Krolo, Özlem Yüce Petronczki, Laurène Pfajfer, Tie Z. Hou, Neil Halliday, Elisangela Santos-Valente, Artem Kalinichenko, Alan Kennedy, Emily M. Mace, Malini Mukherjee, Bianca Tesi, Anna Schrempf, Winfried F. Pickl, Joanna I. Loizou, Renate Kain, Bettina Bidmon-Fliegenschnee, Jean-Nicolas Schickel, Salomé Glauzy, Jakob Huemer, Wojciech Garncarz, Elisabeth Salzer, Iro Pierides, Ivan Bilic, Jens Thiel, Peter Priftakis, Pinaki P. Banerjee, Elisabeth Förster-Waldl, David Medgyesi, Wolf-Dietrich Huber, Jordan S. Orange, Eric Meffre, David M. Sansom, Yenan T. Bryceson, Amnon Altman, and Kaan Boztug. Human def6 deficiency underlies an immunodeficiency syndrome with systemic autoimmunity and aberrant ctla-4 homeostasis. Nature Communications, Jul 2019. URL: https://doi.org/10.1038/s41467-019-10812-x, doi:10.1038/s41467-019-10812-x. This article has 94 citations and is from a highest quality peer-reviewed journal.

12. (manni2017regulationofsystemic pages 6-7): Michela Manni, Edd Ricker, and Alessandra B. Pernis. Regulation of systemic autoimmunity and cd11c+ tbet+ b cells by swef proteins. Cellular immunology, 321:46-51, Nov 2017. URL: https://doi.org/10.1016/j.cellimm.2017.05.010, doi:10.1016/j.cellimm.2017.05.010. This article has 30 citations and is from a peer-reviewed journal.

13. (binder2017def6restrainsosteoclastogenesis pages 6-8): N. Binder, Christine H. Miller, Masaki Yoshida, Kazuki Inoue, Shinichi Nakano, Xiaoyu Hu, L. Ivashkiv, L. Ivashkiv, G. Schett, Alessandra B. Pernis, Alessandra B. Pernis, S. Goldring, F. Ross, Baohong Zhao, and Baohong Zhao. Def6 restrains osteoclastogenesis and inflammatory bone resorption. The Journal of Immunology, 198:3436-3447, May 2017. URL: https://doi.org/10.4049/jimmunol.1601716, doi:10.4049/jimmunol.1601716. This article has 27 citations.

14. (binder2017def6restrainsosteoclastogenesis pages 3-4): N. Binder, Christine H. Miller, Masaki Yoshida, Kazuki Inoue, Shinichi Nakano, Xiaoyu Hu, L. Ivashkiv, L. Ivashkiv, G. Schett, Alessandra B. Pernis, Alessandra B. Pernis, S. Goldring, F. Ross, Baohong Zhao, and Baohong Zhao. Def6 restrains osteoclastogenesis and inflammatory bone resorption. The Journal of Immunology, 198:3436-3447, May 2017. URL: https://doi.org/10.4049/jimmunol.1601716, doi:10.4049/jimmunol.1601716. This article has 27 citations.

15. (serwas2019humandef6deficiency pages 14-15): Nina K. Serwas, Birgit Hoeger, Rico C. Ardy, Sigrun V. Stulz, Zhenhua Sui, Nima Memaran, Marie Meeths, Ana Krolo, Özlem Yüce Petronczki, Laurène Pfajfer, Tie Z. Hou, Neil Halliday, Elisangela Santos-Valente, Artem Kalinichenko, Alan Kennedy, Emily M. Mace, Malini Mukherjee, Bianca Tesi, Anna Schrempf, Winfried F. Pickl, Joanna I. Loizou, Renate Kain, Bettina Bidmon-Fliegenschnee, Jean-Nicolas Schickel, Salomé Glauzy, Jakob Huemer, Wojciech Garncarz, Elisabeth Salzer, Iro Pierides, Ivan Bilic, Jens Thiel, Peter Priftakis, Pinaki P. Banerjee, Elisabeth Förster-Waldl, David Medgyesi, Wolf-Dietrich Huber, Jordan S. Orange, Eric Meffre, David M. Sansom, Yenan T. Bryceson, Amnon Altman, and Kaan Boztug. Human def6 deficiency underlies an immunodeficiency syndrome with systemic autoimmunity and aberrant ctla-4 homeostasis. Nature Communications, Jul 2019. URL: https://doi.org/10.1038/s41467-019-10812-x, doi:10.1038/s41467-019-10812-x. This article has 94 citations and is from a highest quality peer-reviewed journal.

16. (serwas2019humandef6deficiency pages 5-6): Nina K. Serwas, Birgit Hoeger, Rico C. Ardy, Sigrun V. Stulz, Zhenhua Sui, Nima Memaran, Marie Meeths, Ana Krolo, Özlem Yüce Petronczki, Laurène Pfajfer, Tie Z. Hou, Neil Halliday, Elisangela Santos-Valente, Artem Kalinichenko, Alan Kennedy, Emily M. Mace, Malini Mukherjee, Bianca Tesi, Anna Schrempf, Winfried F. Pickl, Joanna I. Loizou, Renate Kain, Bettina Bidmon-Fliegenschnee, Jean-Nicolas Schickel, Salomé Glauzy, Jakob Huemer, Wojciech Garncarz, Elisabeth Salzer, Iro Pierides, Ivan Bilic, Jens Thiel, Peter Priftakis, Pinaki P. Banerjee, Elisabeth Förster-Waldl, David Medgyesi, Wolf-Dietrich Huber, Jordan S. Orange, Eric Meffre, David M. Sansom, Yenan T. Bryceson, Amnon Altman, and Kaan Boztug. Human def6 deficiency underlies an immunodeficiency syndrome with systemic autoimmunity and aberrant ctla-4 homeostasis. Nature Communications, Jul 2019. URL: https://doi.org/10.1038/s41467-019-10812-x, doi:10.1038/s41467-019-10812-x. This article has 94 citations and is from a highest quality peer-reviewed journal.

17. (binder2017def6restrainsosteoclastogenesis pages 11-12): N. Binder, Christine H. Miller, Masaki Yoshida, Kazuki Inoue, Shinichi Nakano, Xiaoyu Hu, L. Ivashkiv, L. Ivashkiv, G. Schett, Alessandra B. Pernis, Alessandra B. Pernis, S. Goldring, F. Ross, Baohong Zhao, and Baohong Zhao. Def6 restrains osteoclastogenesis and inflammatory bone resorption. The Journal of Immunology, 198:3436-3447, May 2017. URL: https://doi.org/10.4049/jimmunol.1601716, doi:10.4049/jimmunol.1601716. This article has 27 citations.

18. (manni2017regulationofsystemic pages 12-14): Michela Manni, Edd Ricker, and Alessandra B. Pernis. Regulation of systemic autoimmunity and cd11c+ tbet+ b cells by swef proteins. Cellular immunology, 321:46-51, Nov 2017. URL: https://doi.org/10.1016/j.cellimm.2017.05.010, doi:10.1016/j.cellimm.2017.05.010. This article has 30 citations and is from a peer-reviewed journal.

19. (serwas2019humandef6deficiency pages 9-9): Nina K. Serwas, Birgit Hoeger, Rico C. Ardy, Sigrun V. Stulz, Zhenhua Sui, Nima Memaran, Marie Meeths, Ana Krolo, Özlem Yüce Petronczki, Laurène Pfajfer, Tie Z. Hou, Neil Halliday, Elisangela Santos-Valente, Artem Kalinichenko, Alan Kennedy, Emily M. Mace, Malini Mukherjee, Bianca Tesi, Anna Schrempf, Winfried F. Pickl, Joanna I. Loizou, Renate Kain, Bettina Bidmon-Fliegenschnee, Jean-Nicolas Schickel, Salomé Glauzy, Jakob Huemer, Wojciech Garncarz, Elisabeth Salzer, Iro Pierides, Ivan Bilic, Jens Thiel, Peter Priftakis, Pinaki P. Banerjee, Elisabeth Förster-Waldl, David Medgyesi, Wolf-Dietrich Huber, Jordan S. Orange, Eric Meffre, David M. Sansom, Yenan T. Bryceson, Amnon Altman, and Kaan Boztug. Human def6 deficiency underlies an immunodeficiency syndrome with systemic autoimmunity and aberrant ctla-4 homeostasis. Nature Communications, Jul 2019. URL: https://doi.org/10.1038/s41467-019-10812-x, doi:10.1038/s41467-019-10812-x. This article has 94 citations and is from a highest quality peer-reviewed journal.

20. (manni2017regulationofsystemic pages 3-4): Michela Manni, Edd Ricker, and Alessandra B. Pernis. Regulation of systemic autoimmunity and cd11c+ tbet+ b cells by swef proteins. Cellular immunology, 321:46-51, Nov 2017. URL: https://doi.org/10.1016/j.cellimm.2017.05.010, doi:10.1016/j.cellimm.2017.05.010. This article has 30 citations and is from a peer-reviewed journal.

21. (binder2017def6restrainsosteoclastogenesis pages 9-11): N. Binder, Christine H. Miller, Masaki Yoshida, Kazuki Inoue, Shinichi Nakano, Xiaoyu Hu, L. Ivashkiv, L. Ivashkiv, G. Schett, Alessandra B. Pernis, Alessandra B. Pernis, S. Goldring, F. Ross, Baohong Zhao, and Baohong Zhao. Def6 restrains osteoclastogenesis and inflammatory bone resorption. The Journal of Immunology, 198:3436-3447, May 2017. URL: https://doi.org/10.4049/jimmunol.1601716, doi:10.4049/jimmunol.1601716. This article has 27 citations.

22. (biswas2010irf4andits pages 14-15): Partha S. Biswas, Govind Bhagat, and Alessandra B. Pernis. Irf4 and its regulators: evolving insights into the pathogenesis of inflammatory arthritis? Immunological Reviews, 233:79-96, Jan 2010. URL: https://doi.org/10.1111/j.0105-2896.2009.00864.x, doi:10.1111/j.0105-2896.2009.00864.x. This article has 63 citations and is from a domain leading peer-reviewed journal.

23. (biswas2010irf4andits pages 15-16): Partha S. Biswas, Govind Bhagat, and Alessandra B. Pernis. Irf4 and its regulators: evolving insights into the pathogenesis of inflammatory arthritis? Immunological Reviews, 233:79-96, Jan 2010. URL: https://doi.org/10.1111/j.0105-2896.2009.00864.x, doi:10.1111/j.0105-2896.2009.00864.x. This article has 63 citations and is from a domain leading peer-reviewed journal.

24. (manni2017regulationofsystemic pages 7-9): Michela Manni, Edd Ricker, and Alessandra B. Pernis. Regulation of systemic autoimmunity and cd11c+ tbet+ b cells by swef proteins. Cellular immunology, 321:46-51, Nov 2017. URL: https://doi.org/10.1016/j.cellimm.2017.05.010, doi:10.1016/j.cellimm.2017.05.010. This article has 30 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](DEF6_Deficiency-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 5 |
| Resolved | 5 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 5 |
| On topic | 2 |
| Off topic | 0 |

All extracted references resolved successfully.