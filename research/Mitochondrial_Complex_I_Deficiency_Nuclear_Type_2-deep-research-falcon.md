---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-08-25T19:37:10.733723'
end_time: '2026-08-25T19:49:07.686536'
duration_seconds: 716.95
template_file: templates/disease_pathophysiology_research.md
template_variables:
  disease_name: Mitochondrial Complex I Deficiency, Nuclear Type 2
  mondo_id: ''
  category: Mendelian
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 28
reference_validation:
  total_references: 8
  verified: 8
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 8
  on_topic: 5
  validator_version: 0.2.1
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: Mitochondrial_Complex_I_Deficiency_Nuclear_Type_2-deep-research-falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Disease Characteristics Research Template

## Target Disease
- **Disease Name:** Mitochondrial Complex I Deficiency, Nuclear Type 2
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial Complex I Deficiency, Nuclear Type 2** covering all of the
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
- **Disease Name:** Mitochondrial Complex I Deficiency, Nuclear Type 2
- **MONDO ID:**  (if available)
- **Category:** Mendelian

## Research Objectives

Please provide a comprehensive research report on **Mitochondrial Complex I Deficiency, Nuclear Type 2** covering all of the
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


# Mitochondrial Complex I Deficiency, Nuclear Type 2: Research Report

## Executive summary and evidence boundaries

Mitochondrial complex I deficiency, nuclear type 2 (MC1DN2) is an ultra-rare, autosomal-recessive mitochondrial disorder caused by biallelic pathogenic variants in **NDUFS8**, which encodes a nuclear-derived iron–sulfur core subunit of respiratory-chain complex I. The usual presentation lies within the **Leigh syndrome spectrum**, but reported disease ranges from neonatal cardiorespiratory failure and death at 11 weeks to a slowly progressive childhood “progressive external ophthalmoplegia-plus” encephalomyopathy. Open Targets maps the entity **MONDO:0032606** specifically to **NDUFS8** (Ensembl ENSG00000110717). (OpenTargets Search: Mitochondrial complex I deficiency, nuclear type 2)

The evidence base is extremely small. A 2022 review found only **16 reported patients with Leigh syndrome and one with encephalomyopathy** carrying NDUFS8 variants. Consequently, phenotype frequencies, penetrance, prevalence, survival curves, treatment-response rates, and formal genotype–phenotype correlations cannot presently be estimated reliably. Claims below are labelled implicitly by context as **NDUFS8-specific human**, **experimental**, or **general Leigh/primary mitochondrial disease** evidence; general Leigh statistics must not be treated as MC1DN2-specific. (wang2022emergingrolesof pages 4-5)

| Category | Summary | Evidence basis |
|---|---|---|
| Entity / identifier | **Mitochondrial complex I deficiency, nuclear type 2**; MONDO **MONDO:0032606**. Disease-target mapping supports **NDUFS8** as the causal gene. Do **not** infer unsupported OMIM/Orphanet/ICD identifiers without direct source confirmation. | Disease-specific (OpenTargets Search: Mitochondrial complex I deficiency, nuclear type 2) |
| Causal gene / inheritance | **NDUFS8** (NADH:ubiquinone oxidoreductase core subunit S8); inheritance is **autosomal recessive** with reported **compound heterozygous** and **homozygous** missense variants. | Disease-specific (loeffen1998thefirstnuclearencoded pages 2-3, loeffen1998thefirstnuclearencoded pages 1-2, wang2022emergingrolesof pages 4-5, marina2013ndufs8relatedcomplexi pages 2-4) |
| Protein / molecular mechanism | NDUFS8 is a **core complex I Fe-S subunit** in the **Q module**, containing **two 4Fe-4S ferredoxin consensus motifs** and participating in **electron transfer** and **complex I assembly/stability**. Reported pathogenic mechanisms include **misfolding**, impaired interaction with **NDUFA12/NDUFS7/NDUFS2**, and disruption of **N5/N6a-related electron transfer**. | Disease-specific (loeffen1998thefirstnuclearencoded pages 1-2, wang2022emergingrolesof pages 4-5, wang2022emergingrolesof pages 2-4, wang2022emergingrolesof pages 5-6) |
| Reported human evidence size | Literature summary identified **16 patients with Leigh syndrome** and **1 patient with encephalomyopathy** carrying NDUFS8 mutations by 2022 review; primary detailed reports include the 1998 index infant and a 2013 consanguineous Afghan sibship with 3 affected children. | Disease-specific (wang2022emergingrolesof pages 4-5, marina2013ndufs8relatedcomplexi pages 1-2, marina2013ndufs8relatedcomplexi pages 2-4) |
| Variant spectrum | Reported variants are almost exclusively **missense**: e.g., **c.236C>T (p.Pro79Leu), c.305G>A (p.Arg102His), c.160C>T (p.Arg54Trp), c.187G>C (p.Glu63Gln), c.254C>T (p.Pro85Leu), c.413G>A (p.Arg138His), c.229C>T (p.Arg77Trp), c.476C>A (p.Ala159Asp), c.460G>A (p.Gly154Ser), c.52C>T (p.Arg18Cys), c.484G>A/T (p.Val162Met), c.281C>T (p.Arg94Cys), c.457T>C (p.Cys153Arg)**. Reviews note absence of reported nonsense variants, hypothesizing complete loss may be embryonically lethal. | Disease-specific (wang2022emergingrolesof pages 4-5, wang2022emergingrolesof pages 5-6, marina2013ndufs8relatedcomplexi pages 2-4) |
| Onset / course | **Variable but usually early-onset.** Severe neonatal/infantile disease can begin **from day 1 of life** or in the first weeks with rapid progression to cardiorespiratory failure; milder forms may show **infant hypotonia**, then **slowly progressive childhood neuromuscular disease** with dysarthria/ataxia/ophthalmoplegia. | Disease-specific (loeffen1998thefirstnuclearencoded pages 1-2, loeffen1998thefirstnuclearencoded pages 2-3, marina2013ndufs8relatedcomplexi pages 1-2, marina2013ndufs8relatedcomplexi pages 2-4) |
| Prognosis | Prognosis is **highly variable**. Severe infantile presentations may result in **death within weeks to 3 months**; milder childhood forms can survive into later childhood/adolescence with progressive disability, wheelchair need, or special schooling. | Disease-specific (loeffen1998thefirstnuclearencoded pages 2-3, wang2022emergingrolesof pages 4-5, marina2013ndufs8relatedcomplexi pages 1-2, marina2013ndufs8relatedcomplexi pages 2-4) |
| Hallmark phenotypes | Common disease-specific phenotypes reported across cases: **Leigh syndrome**, **lactic acidosis**, **hypotonia**, **developmental delay/regression**, **muscle weakness/exercise intolerance**, **dysarthria**, **ataxia**, **ptosis/external ophthalmoplegia**, **nystagmus**, **seizures**, **hypertrophic cardiomyopathy or LV dysfunction**, **feeding difficulty**, **respiratory failure/apnea**, **myopia**, **contractures/scoliosis**. | Disease-specific (loeffen1998thefirstnuclearencoded pages 1-2, loeffen1998thefirstnuclearencoded pages 2-3, marina2013ndufs8relatedcomplexi pages 1-2, marina2013ndufs8relatedcomplexi pages 2-4) |
| HPO suggestions | Suggested HPO terms: **Leigh syndrome phenotype** HP:0000007-context not specific; **Lactic acidosis** HP:0003128; **Hypotonia** HP:0001252; **Seizure** HP:0001250; **Apnea** HP:0002104; **Respiratory failure** HP:0002878; **Feeding difficulties** HP:0011968; **Hypertrophic cardiomyopathy** HP:0001639; **Developmental delay** HP:0001263; **Muscle weakness** HP:0001324; **Exercise intolerance** HP:0003546; **Ataxic gait** HP:0002066; **Dysarthria** HP:0001260; **Ptosis** HP:0000508; **External ophthalmoplegia** HP:0000602; **Nystagmus** HP:0000639; **Myopia** HP:0000545; **Scoliosis** HP:0002650; **Joint contracture** HP:0001371. | Disease-specific synthesis from reported cases (loeffen1998thefirstnuclearencoded pages 1-2, loeffen1998thefirstnuclearencoded pages 2-3, marina2013ndufs8relatedcomplexi pages 1-2, marina2013ndufs8relatedcomplexi pages 2-4) |
| Anatomy affected | **Primary:** brain (especially **putamen/basal ganglia**, mesencephalon/brainstem, caudate, white matter), skeletal muscle, heart. **Secondary/systemic:** respiratory control pathways, peripheral neuromuscular system, occasionally liver. | Disease-specific (loeffen1998thefirstnuclearencoded pages 2-3, marina2013ndufs8relatedcomplexi pages 1-2, marina2013ndufs8relatedcomplexi pages 2-4) |
| Diagnostic anchors | Key anchors are: **(1)** characteristic neuroimaging with **bilateral symmetric basal ganglia/brainstem lesions**; **(2)** elevated **blood/CSF lactate and pyruvate**; **(3)** **isolated complex I deficiency** in fibroblasts/muscle and sometimes heart/brain; **(4)** **biallelic NDUFS8 variants** by targeted sequencing/WES. In the index case, complex I residual activity was **39% in muscle, 69% in fibroblasts, ~0% in heart, 3% in brain**. | Disease-specific (loeffen1998thefirstnuclearencoded pages 2-3, marina2013ndufs8relatedcomplexi pages 2-4) |
| Disease-specific imaging / pathology | Disease-specific MRI/CT findings include **putaminal lesions**, **mesencephalic lesions**, **white-matter hypodensity**, and in one family **putamen, caudate, and frontal subcortical abnormalities**. Neuropathology in the infant index case showed **bilateral symmetrical degeneration**, **spongiform change**, **capillary proliferation**, **demyelinization**, and **gliosis**. | Disease-specific (loeffen1998thefirstnuclearencoded pages 2-3, marina2013ndufs8relatedcomplexi pages 2-4) |
| Triggers / modifiers | **Infections/febrile illness** were repeatedly reported to precipitate worsening; the 1998 infant worsened during **acute gastroenteritis**, and the 2013 sibship had symptom exacerbation during **febrile infections**. Broader mitochondrial-disease literature suggests modifiers may include nuclear-mitochondrial background, but this is not established specifically for NDUFS8 disease. | Disease-specific + cautious generalization (loeffen1998thefirstnuclearencoded pages 1-2, marina2013ndufs8relatedcomplexi pages 1-2, conti2023redflagsin pages 1-2) |
| Treatment status | **No approved NDUFS8-specific disease-modifying therapy identified.** Clinical care is largely **supportive/symptomatic**. Supplements such as **riboflavin/creatine** have been used empirically in individual patients without clear demonstrable effect in one family. | Disease-specific (marina2013ndufs8relatedcomplexi pages 1-2, wang2022emergingrolesof pages 4-5) |
| Experimental / emerging therapy | A **TAT-mediated NDUFS8 protein transduction** approach reportedly improved complex I assembly and partially rescued function in an NDUFS8-deficient cell line; this remains **preclinical**. | Disease-specific (wang2022emergingrolesof pages 4-5) |
| Leigh-spectrum-general therapies / trials | Not NDUFS8-specific but relevant to real-world management landscape: **vatiquinone/EPI-743** Phase 2 Leigh studies (**NCT01721733**, **NCT02352896**) and **elamipretide** Phase 3 nuclear-DNA PMD trial (**NCT05162768**) include Leigh or complex I deficiency populations broadly, not proven NDUFS8 subsets. | Leigh-spectrum-general / PMD-general (NCT02352896 chunk 1, NCT05162768 chunk 1) |
| Registries / natural history resources | **International Registry for Leigh Syndrome** (**NCT03137355**) and **GENOMIT global mitochondrial registry** (**NCT05554835**) are active infrastructure for natural history, phenotyping, and trial readiness; these are not NDUFS8-specific but may capture such cases. | Leigh-spectrum-general / PMD-general (NCT03137355 chunk 1, NCT05554835 chunk 1) |
| Model systems | **Yarrowia lipolytica** models reconstructed **p.P79L** and **p.R102H**, showing roughly **50% Vmax reduction** and altered inhibitor sensitivity; useful for mechanistic study of electron transfer/assembly. A 2024 endothelial **shRNA/CRISPR** study showed NDUFS8 depletion lowers OCR/complex I activity/ATP and increases ROS, impairing angiogenesis; this is mechanistic but **not a patient disease model**. | Disease-specific mechanism models (henke2024diseasemodelsof pages 5-6, xiong2024therequirementof pages 1-2) |
| Recent developments (2023-2024) | Recent high-value additions are mainly **general Leigh/mitochondrial disease infrastructure and modeling**, not large new NDUFS8 patient cohorts: 2024 review of **Leigh disease models from yeast to organoids**, 2024 functional paper linking **NDUFS8 to angiogenesis/Akt-mTOR signaling**, and active registry/trial ecosystems. | Mixed: disease-specific mechanism + Leigh-spectrum-general (henke2024diseasemodelsof pages 1-2, xiong2024therequirementof pages 1-2, NCT03137355 chunk 1, NCT05554835 chunk 1) |
| Major evidence gaps | Major gaps include **very small NDUFS8-specific case numbers**, lack of **prospective natural history**, no robust **prevalence/incidence** estimates for this subtype, limited **genotype-phenotype penetrance** data, sparse **quality-of-life** measures, minimal **omics** data, no established **animal model specific to NDUFS8 patient variants**, and no proven **targeted therapy** beyond preclinical rescue. | Evidence-gap synthesis from available disease-specific and registry sources (wang2022emergingrolesof pages 4-5, henke2024diseasemodelsof pages 1-2, NCT03137355 chunk 1, NCT05554835 chunk 1) |


*Table: This table condenses the most actionable disease-knowledge-base facts for mitochondrial complex I deficiency, nuclear type 2, emphasizing which findings are NDUFS8-specific versus broader Leigh-spectrum evidence. It is useful as a compact reference for curation, phenotype annotation, and evidence-gap tracking.*

## 1. Disease information

### Definition and classification

MC1DN2 is a **Mendelian oxidative-phosphorylation disorder** in which biallelic NDUFS8 dysfunction reduces NADH:ubiquinone oxidoreductase activity. It is generally expressed clinically as Leigh syndrome/Leigh syndrome spectrum, mitochondrial encephalopathy, or a PEO-plus neuromuscular syndrome. The original report described it as the first molecular link between a nuclear-encoded complex-I subunit and Leigh syndrome. (loeffen1998thefirstnuclearencoded pages 1-2)

### Identifiers and synonyms

- **MONDO:** MONDO:0032606.
- **Causal target:** NDUFS8, approved name *NADH:ubiquinone oxidoreductase core subunit S8*; Ensembl **ENSG00000110717**. (OpenTargets Search: Mitochondrial complex I deficiency, nuclear type 2)
- **Leigh disease MeSH:** **D007888**; this identifies the broader clinical syndrome, not the gene-specific subtype. (NCT02352896 chunk 1)
- **Relevant broader OMIM phenotypes reported in the literature:** Leigh syndrome **MIM 256000** and mitochondrial complex-I deficiency **MIM 252010**. These should not be substituted automatically for a subtype-specific OMIM entry. (loeffen1998thefirstnuclearencoded pages 1-2)
- **Common names:** NDUFS8-related complex-I deficiency; NDUFS8-related Leigh syndrome; mitochondrial complex-I deficiency due to NDUFS8; TYKY-subunit deficiency; nuclear type-2 mitochondrial complex-I deficiency.
- **Orphanet and subtype-specific ICD-10/ICD-11 codes:** not directly verified in the retrieved evidence. Clinically, coding normally falls under broader mitochondrial metabolism or Leigh-disease categories; a gene-specific ICD code is not established here.

The information summarized is predominantly **aggregated disease-level literature**, supplemented by individual case reports and case-series records—not EHR-derived patient-level data.

## 2. Etiology, risk, protection, and gene–environment interaction

### Primary cause

The necessary cause is **germline biallelic NDUFS8 variation**. Both homozygous and compound-heterozygous missense genotypes have been reported. The 1998 index patient carried c.236C>T (p.Pro79Leu) and c.305G>A (p.Arg102His), absent from 70 control alleles and segregating in the family. Three affected siblings of consanguineous Afghan parents were homozygous for c.160C>T (p.Arg54Trp), while both parents were heterozygous. (loeffen1998thefirstnuclearencoded pages 1-2, marina2013ndufs8relatedcomplexi pages 2-4)

### Risk factors

- **Genetic:** having two pathogenic NDUFS8 alleles; parental consanguinity increases the probability of homozygosity. Family history may nevertheless be negative, as in the index case.
- **Family recurrence:** for confirmed autosomal-recessive disease, each conception between two carriers has a theoretical 25% affected, 50% carrier, and 25% unaffected/non-carrier probability.
- **Environmental:** no environmental exposure causes MC1DN2. Infections and catabolic illness can unmask or exacerbate energy failure. The index infant deteriorated during gastroenteritis, while affected siblings worsened during febrile infections. (loeffen1998thefirstnuclearencoded pages 1-2, marina2013ndufs8relatedcomplexi pages 1-2)
- **Sex and ancestry:** no evidence supports sex-specific risk or a population-wide ancestry effect. Both sexes and Dutch/Afghan families are represented.

### Protective factors and modifiers

No validated protective allele, diet, lifestyle factor, or modifier gene is established. The absence of reported nonsense variants led authors to hypothesize that complete NDUFS8 loss could be incompatible with fetal survival, but this is an inference rather than proof. Nuclear–mitochondrial background and metabolic compensation are plausible modifiers; broader PMD literature identifies mitochondrial haplotype, other variants, tissue-specific expression, and environmental factors as possible modifiers, but none has been validated specifically in MC1DN2. (wang2022emergingrolesof pages 4-5, conti2023redflagsin pages 1-2)

## 3. Phenotypes

The disorder has a severe infantile and a milder childhood continuum. Because published case counts are very small, most frequencies are **unknown** rather than “rare” or “common.”

### Severe neonatal/infantile presentation

The original male infant developed poor feeding, apnea, and cyanosis from the first day of life and presented at five weeks with hypercarbia, drowsiness, severe hypotonia, brisk reflexes, ankle clonus, eye flutter, seizures, and hypertrophic obstructive cardiomyopathy. He died from cardiorespiratory failure at 11 weeks. Suggested HPO terms include **Feeding difficulties HP:0011968, Apnea HP:0002104, Cyanosis HP:0000961, Hypotonia HP:0001252, Seizure HP:0001250, Hyperreflexia HP:0001347, Hypertrophic cardiomyopathy HP:0001639**, and **Respiratory failure HP:0002878**. (loeffen1998thefirstnuclearencoded pages 1-2, loeffen1998thefirstnuclearencoded pages 2-3)

Biochemical abnormalities included blood lactate 3.4 mmol/L, CSF lactate 5.6 mmol/L, blood pyruvate 167 µmol/L, CSF pyruvate 193 µmol/L, and CSF lactate:pyruvate ratio 29.0. Suggested terms are **Lactic acidosis HP:0003128** and **Increased circulating pyruvate concentration HP:0004352**. (loeffen1998thefirstnuclearencoded pages 2-3)

### Childhood PEO-plus/Leigh presentation

In the Afghan sibship, the oldest child had infantile hypotonia, sat at 16 months and walked at 24 months, then developed progressive weakness, dysarthria, ataxia, ophthalmoplegia, swallowing difficulty, dystonic posturing, scoliosis, contractures, and major walking limitation. At 13 years he could walk only a few steps and otherwise used a wheelchair; IQ was 61. His brother developed dysarthria at five, severe myopia at six, weakness, falls, exercise intolerance, ptosis, ophthalmoplegia, nystagmus, and mild cognitive impairment (IQ 73). Their sister had milder hypotonia, scapular winging, contractures, myopia, nystagmus, and dysmetria, with IQ 84 at age nine. (marina2013ndufs8relatedcomplexi pages 1-2, marina2013ndufs8relatedcomplexi pages 2-4)

Suggested terms include **Global developmental delay HP:0001263, Muscle weakness HP:0001324, Exercise intolerance HP:0003546, Dysarthria HP:0001260, Ataxic gait HP:0002066, Dystonia HP:0001332, Ptosis HP:0000508, External ophthalmoplegia HP:0000602, Nystagmus HP:0000639, Myopia HP:0000545, Dysphagia HP:0002015, Scoliosis HP:0002650, Joint contracture HP:0001371, Intellectual disability HP:0001249**, and **Abnormality of the putamen HP:0012751**.

### Imaging and pathology

CT in the index infant showed extensive white-matter hypodensity followed by symmetric putaminal and mesencephalic lesions. Autopsy showed bilateral degeneration involving rostral/caudal brainstem, diencephalon, central nuclei, spinal cord, and centrum semiovale, with spongiform degeneration, capillary proliferation, endothelial swelling, demyelination, and gliosis. (loeffen1998thefirstnuclearencoded pages 2-3)

MRI in the milder family showed bilateral putaminal abnormalities; the oldest child later had putamen, caudate, and frontal subcortical lesions. Cerebellum and brainstem were structurally normal in those scans despite ataxia. (marina2013ndufs8relatedcomplexi pages 2-4, marina2013ndufs8relatedcomplexi pages 4-5)

### Functional and quality-of-life effect

No MC1DN2-specific EQ-5D, SF-36, PROMIS, or validated quality-of-life study exists. Case descriptions nevertheless demonstrate substantial effects: loss of independent mobility, wheelchair use, special education, impaired communication, feeding/swallowing difficulty, pain and fatigue after exercise, and recurrent deterioration during illness. General mitochondrial registries use the Newcastle Pediatric Mitochondrial Disease Scale, including a QoL section scored 0–25. (marina2013ndufs8relatedcomplexi pages 1-2, NCT05554835 chunk 1)

## 4. Genetic and molecular information

### Gene and protein

**NDUFS8** encodes a roughly 23-kDa, 210-amino-acid core subunit of mitochondrial complex I. It contains two [4Fe–4S] ferredoxin consensus motifs and resides in the ubiquinone-binding/Q region, where it supports electron transfer, ubiquinone reduction, and complex-I assembly/stability. Suggested annotations include **GO:0005747 mitochondrial respiratory-chain complex I**, **GO:0005743 mitochondrial inner membrane**, **GO:0006120 mitochondrial electron transport, NADH to ubiquinone**, **GO:0008137 NADH dehydrogenase (ubiquinone) activity**, **GO:0051539 4 iron, 4 sulfur cluster binding**, and **GO:0006091 generation of precursor metabolites and energy**. (wang2022emergingrolesof pages 2-4, loeffen1998thefirstnuclearencoded pages 1-2)

### Reported pathogenic variant spectrum

Published variants include p.Pro79Leu, p.Arg102His, p.Arg54Trp, p.Glu63Gln, p.Pro85Leu, p.Arg138His, p.Arg77Trp, p.Ala159Asp, p.Gly154Ser, p.Arg18Cys, p.Arg94Cys, p.Val162Met, and p.Cys153Arg. Reported mechanisms include NDUFS8 misfolding, loss of interactions with NDUFA12/NDUFS7/NDUFS2, and perturbation of electron transfer near N5/N6a-associated structural regions. (wang2022emergingrolesof pages 5-6, wang2022emergingrolesof pages 4-5)

All variants summarized in the 2022 review were missense. Variant-level ClinVar classifications and current gnomAD/TOPMed allele frequencies were not directly retrieved and should be curated individually against current genome build and transcript **before** knowledge-base import. The disease is germline, not somatic. Large chromosomal rearrangements, repeat expansions, and a recurrent pathogenic CNV have not been established.

### Modifier, epigenetic, and digenic evidence

No confirmed MC1DN2 modifier gene or disease-specific methylation/chromatin signature exists. Recent literature discusses heterozygous NDUFS8 alleles occurring with biallelic DNAJC30 variants in possible digenic mitochondrial disease, but this does not replace the established biallelic NDUFS8 model and requires further validation. No anticipation is expected because this is not a repeat-expansion disorder.

## 5. Environmental and lifestyle information

No toxin, radiation exposure, pollutant, occupational exposure, infection, smoking behavior, alcohol use, or dietary pattern is known to cause the disease. The clinically important interaction is between constitutive genetic energy-production failure and **catabolic stress**. Fever, infection, fasting, dehydration, surgery, and anesthesia may increase ATP demand or substrate deficiency and precipitate decompensation; direct MC1DN2 evidence exists for gastroenteritis and febrile infections. (loeffen1998thefirstnuclearencoded pages 1-2, marina2013ndufs8relatedcomplexi pages 1-2)

There is no infectious agent intrinsic to pathogenesis and no zoonotic or communicable component. Routine immunization is not etiologic; preventing vaccine-preventable infections is generally desirable in mitochondrial disease, subject to individualized clinical advice.

## 6. Mechanism and pathophysiology

### Causal chain

1. **Upstream genetic trigger:** biallelic NDUFS8 missense variants alter a conserved Fe–S/Q-module core subunit.
2. **Protein/complex defect:** misfolding or impaired subunit interfaces destabilize complex-I assembly and/or electron transfer toward ubiquinone.
3. **Biochemical defect:** NADH oxidation, proton pumping, membrane polarization, and respiratory ATP production fall; NADH/NAD+ homeostasis is disturbed.
4. **Compensation/injury:** glycolytic flux rises, producing lactate; electron leakage can increase ROS; energetic stress perturbs ion gradients, neurotransmission, contractility, and cell survival.
5. **Tissue selectivity:** high-demand neurons, skeletal myofibers, cardiomyocytes, and respiratory-control networks cross an energetic threshold first.
6. **Clinical outcome:** symmetric basal-ganglia/brainstem lesions, psychomotor or motor dysfunction, hypotonia/weakness, seizures, cardiomyopathy, apnea, and potentially cardiorespiratory death.

In the index patient, residual complex-I activity was 39% of the lower reference limit in muscle, 69% in fibroblasts, approximately 0% in heart, 53% in liver, and 3% in brain, illustrating marked tissue dependence. Other respiratory complexes were normal. (loeffen1998thefirstnuclearencoded pages 2-3)

### Recent mechanistic development, 2024

NDUFS8 knockdown or CRISPR knockout in human endothelial cells reduced oxygen consumption, complex-I activity, ATP, and membrane potential, while increasing ROS, lipid oxidation, and modest apoptosis. It inhibited proliferation, migration, tube formation, and Akt–mTOR activation; ATP supplementation or constitutively active AKT1 rescued portions of the phenotype. Endothelial-directed shRNA also inhibited retinal angiogenesis in mice. This establishes an NDUFS8-dependent ATP–Akt/mTOR–angiogenesis axis experimentally, but vascular maldevelopment has **not** yet been demonstrated as a core MC1DN2 patient phenotype. Suggested terms include **GO:0001525 angiogenesis, GO:0006979 response to oxidative stress, GO:0006915 apoptotic process, GO:0045765 regulation of angiogenesis**, and endothelial cell **CL:0000115**. Published April 2024, DOI: https://doi.org/10.1038/s41419-024-06636-3. (xiong2024therequirementof pages 1-2)

### Molecular profiling

No disease-specific human single-cell, spatial-transcriptomic, lipidomic, metabolomic, or integrated multi-omic cohort was identified. The principal molecular readouts remain respiratory-chain enzymology, oxygen consumption, complex assembly, ATP, lactate/pyruvate, membrane potential, and ROS. Thus, claims about immune activation, autophagy, epigenetic remodeling, or specific metabolomic signatures should be regarded as unestablished for MC1DN2.

## 7. Anatomical structures affected

- **Central nervous system:** bilateral putamen/basal ganglia (**UBERON:0001874/UBERON:0002420**), caudate nucleus (**UBERON:0001873**), midbrain/mesencephalon (**UBERON:0001891**), brainstem (**UBERON:0002298**), cerebral white matter (**UBERON:0002437**), diencephalon (**UBERON:0001894**), and spinal cord (**UBERON:0002240**). Lesions are typically bilateral and symmetric.
- **Skeletal muscle:** generalized neuromuscular involvement; **UBERON:0001134**. Relevant cells are skeletal muscle fibers/myocytes (**CL:0000188**).
- **Heart:** hypertrophic cardiomyopathy or borderline ventricular dysfunction; **UBERON:0000948** and cardiomyocyte **CL:0000746**.
- **Eye/oculomotor system:** extraocular muscles and ocular motor pathways, producing ptosis, ophthalmoplegia, nystagmus, and myopia.
- **Subcellular:** mitochondrial inner membrane (**GO:0005743**) and respiratory-chain complex I (**GO:0005747**), with nuclear DNA as the mutation site but mitochondria as the functional lesion.

## 8. Temporal development

Onset ranges from **day one of life** to later childhood. Severe disease may progress over weeks to fatal cardiorespiratory failure. Milder disease can begin with infantile hypotonia or apparently normal early milestones, followed at approximately five to seven years by dysarthria, weakness, ophthalmoplegia, ataxia, and cognitive impairment. (loeffen1998thefirstnuclearencoded pages 1-2, marina2013ndufs8relatedcomplexi pages 1-2)

The course is usually chronic and progressive, with superimposed metabolic/neurologic worsening during infection. There is no established staging system or spontaneous remission pattern. Critical periods include infancy, intercurrent illness, fasting, surgery/anesthesia, and periods of rapid growth. Early molecular diagnosis creates opportunities for anticipatory cardiac/respiratory surveillance, nutritional support, emergency illness planning, and reproductive counseling, although it does not yet enable a proven disease-modifying therapy.

For the broader Leigh spectrum, a 2024 review reports typical onset around seven months and median death at 2.4 years, with outcome influenced by onset age, genotype, and severity. These figures are **not MC1DN2-specific**, and the surviving adolescent sibship demonstrates why applying them directly would be misleading. DOI: https://doi.org/10.1002/jimd.12804, received April and accepted September 2024. (henke2024diseasemodelsof pages 1-2)

## 9. Inheritance and population

Inheritance is **autosomal recessive**. Penetrance appears high for clearly pathogenic biallelic genotypes in reported families, but precise penetrance and age dependence cannot be calculated. Expressivity is markedly variable, including within one family. There is no evidence of anticipation. Germline mosaicism has not been documented but cannot be excluded for counseling purposes.

No MC1DN2-specific prevalence, incidence, carrier frequency, sex ratio, founder effect, or geographic distribution estimate is available. The literature estimate of approximately **1 Leigh case per 40,000 births** applies to all genetic causes of Leigh syndrome, not NDUFS8 disease. Primary mitochondrial diseases collectively have been estimated at approximately 1 in 4,300, again not this subtype. (loeffen1998thefirstnuclearencoded pages 1-2, henke2024diseasemodelsof pages 1-2, conti2023redflagsin pages 1-2)

Consanguinity was important in the Afghan family but is not required, as shown by the nonconsanguineous Dutch family. No ethnic group should be considered intrinsically high-risk on current evidence.

## 10. Diagnostics

### Clinical and biochemical evaluation

Diagnostic suspicion should arise from infantile or childhood neuroregression/developmental delay, hypotonia, movement disorder, ophthalmoplegia, unexplained cardiomyopathy, respiratory episodes, elevated lactate, and bilateral symmetric basal-ganglia/brainstem lesions.

Recommended evaluation includes:

1. Blood lactate, pyruvate, glucose, electrolytes/bicarbonate, liver function, CK, plasma amino acids, acylcarnitines, and urine organic acids; CSF lactate/pyruvate when clinically justified.
2. Brain MRI with T1/T2/FLAIR and diffusion sequences; MR spectroscopy may demonstrate lactate but is not obligatory.
3. ECG and echocardiography; respiratory/sleep assessment; EEG for seizures; audiology, ophthalmology, and formal developmental/motor assessment.
4. Complex-I enzyme assay and respiratory studies in fibroblasts or muscle when genetics is uncertain or a variant requires functional validation. Normal CK, absent ragged-red fibers, or a nondiagnostic muscle biopsy does not exclude disease. In the mild family, histology was nonspecific and lacked ragged-red fibers despite isolated complex-I activity of 0.05 U/U citrate synthase versus a 0.17–0.56 reference range. (marina2013ndufs8relatedcomplexi pages 2-4)

### Genetic testing hierarchy

A practical first-line test is a comprehensive mitochondrial-disease/Leigh panel or **trio WES/WGS**, analyzing nuclear genes and mtDNA concurrently. WGS offers improved coverage of noncoding and structural variants; RNA sequencing can clarify suspected splice defects, although no NDUFS8-specific RNA diagnostic series exists. Biallelic variants should be confirmed and phased by parental testing. The mild family illustrates WES utility: 62 shared novel homozygous changes were filtered to the homozygous NDUFS8 p.Arg54Trp variant, absent from 222 control chromosomes and segregating with disease. (marina2013ndufs8relatedcomplexi pages 2-4)

Single-gene NDUFS8 sequencing is reasonable where biochemical/imaging findings and family segregation strongly implicate MC1DN2. CMA, karyotyping, FISH, and repeat-expansion testing are not primary tests unless another diagnosis is suspected. mtDNA sequencing remains essential in the differential because Leigh syndrome has extensive nuclear and mitochondrial heterogeneity. General expert reviews recommend integrating clinical, biochemical, imaging, and molecular data rather than relying on a single nonspecific marker. (maack2025mitochondrialcardiomyopathiespathogenesis pages 6-7, maack2025mitochondrialcardiomyopathiespathogenesis pages 8-8, maack2025mitochondrialcardiomyopathiespathogenesis pages 1-2)

### Differential diagnosis

The differential includes other nuclear complex-I deficiencies (e.g., NDUFS4, NDUFS7, NDUFS2, NDUFAF genes), mtDNA complex-I disorders, SURF1-related complex-IV deficiency, MT-ATP6 disease, pyruvate-dehydrogenase deficiency, biotin-thiamine-responsive basal ganglia disease, organic acidemias, toxic/metabolic basal-ganglia injury, POLG disease, and other causes of PEO-plus syndromes. Genetic confirmation distinguishes these overlapping entities.

### Screening

There is no population or newborn screening program specific to NDUFS8. After a molecular diagnosis, offer parental carrier confirmation and targeted cascade testing to adult relatives. Prenatal testing and preimplantation genetic testing for the known familial variants are technically feasible.

## 11. Outcome and prognosis

Prognosis is genotype- and phenotype-dependent. The severe index patient died at 11 weeks from cardiorespiratory failure; literature review noted other patients dying within three months. Conversely, p.Arg54Trp homozygotes survived to ages 9–13, albeit with progressive weakness, ophthalmoplegia, ataxia, cognitive impairment, and, in the oldest sibling, wheelchair dependence. (loeffen1998thefirstnuclearencoded pages 2-3, wang2022emergingrolesof pages 4-5, marina2013ndufs8relatedcomplexi pages 1-2)

No subtype-specific 5-year/10-year survival rate, life expectancy, mortality rate, disability-adjusted life-year estimate, or validated prognostic model exists. Adverse clinical indicators likely include neonatal onset, very low residual complex-I activity in brain/heart, cardiomyopathy, central apnea/respiratory failure, refractory seizures, feeding failure, and recurrent metabolic decompensation, but these have not been statistically validated in MC1DN2.

Recovery of established neurodegeneration is generally limited; supportive intervention can preserve function and prevent avoidable complications. Longitudinal endpoints suitable for registries include NPMDS/NMDAS, Gross Motor Function Measure, Barry–Albright Dystonia Scale, respiratory support days, hospitalization, cardiac function, mobility, swallowing, and caregiver-reported QoL. (NCT02352896 chunk 1, NCT05554835 chunk 1)

## 12. Treatment and current applications

### Standard clinical management

There is **no approved NDUFS8-specific curative or disease-modifying therapy**. Management should be multidisciplinary and individualized:

- Prompt treatment of infection, dehydration, hypoglycemia, and acidosis; avoid prolonged fasting and establish an emergency illness plan.
- Nutrition/swallow evaluation, calorie support, reflux/constipation management, and gastrostomy when needed.
- Respiratory monitoring and noninvasive/invasive ventilation when indicated.
- Standard antiseizure treatment selected with mitochondrial expertise; avoid unnecessary mitochondrial-toxic exposure.
- Cardiac surveillance and guideline-based treatment of cardiomyopathy/heart failure.
- Physical, occupational, speech, feeding, and respiratory therapy; mobility/orthotic aids and contracture/scoliosis management.
- Ophthalmology and low-vision support; educational and neuropsychological services.

Riboflavin, thiamine, coenzyme Q10, creatine, and other “mitochondrial cocktails” are often tried empirically, but efficacy evidence is weak. In the reported p.Arg54Trp family, creatine plus riboflavin produced “no clearly demonstrable effect.” (marina2013ndufs8relatedcomplexi pages 1-2, li2024newinsightsinto pages 12-13)

Suggested NCIt intervention concepts include **Supportive Care**, **Physical Therapy**, **Occupational Therapy**, **Speech Therapy**, **Nutritional Support**, **Mechanical Ventilation**, **Anticonvulsant Therapy**, and **Genetic Counseling**. Exact NCIt codes should be validated during ontology curation.

### NDUFS8-directed experimental therapy

A TAT cell-penetrating peptide–NDUFS8 fusion improved complex-I assembly and partially rescued in-gel activity and oxygen consumption in an NDUFS8-deficient cell line. This is proof-of-concept protein replacement only; delivery, tissue targeting, durability, immunogenicity, and clinical efficacy remain unresolved. (wang2022emergingrolesof pages 4-5)

No NDUFS8 gene-replacement, CRISPR, ASO, siRNA, mRNA, stem-cell, or mitochondrial-transplantation therapy has demonstrated clinical efficacy. Because the causal gene is nuclear, AAV-mediated gene addition is conceptually possible, but simultaneous delivery to brain, muscle, heart, and respiratory tissues and regulated mitochondrial import are major barriers.

### Trials and registries

- **Vatiquinone/EPI-743, NCT02352896:** completed Phase 2 long-term study in 30 children with genetically confirmed Leigh syndrome; 15 mg/kg up to 200 mg three times daily, with NPMDS, safety, neurodevelopment, respiratory outcomes, hospitalization, mortality, QoL, and glutathione biomarkers assessed. It was not NDUFS8-specific and does not establish efficacy for MC1DN2. ClinicalTrials.gov: https://clinicaltrials.gov/study/NCT02352896. (NCT02352896 chunk 1)
- **Elamipretide, NCT05162768:** completed 48-week randomized, quadruple-masked Phase 3 trial in 102 adults with nuclear-DNA primary mitochondrial myopathy; 60 mg subcutaneously daily versus placebo, with six-minute walk distance as the primary endpoint. Although “mitochondrial complex I deficiency” was listed, the phenotype requirement favored adult myopathy/PEO and results cannot be extrapolated to pediatric NDUFS8 Leigh disease. https://clinicaltrials.gov/study/NCT05162768. (NCT05162768 chunk 1)
- **International Registry for Leigh Syndrome, NCT03137355:** recruiting, estimated 200 participants, with ten-year longitudinal phenotype collection. https://clinicaltrials.gov/study/NCT03137355. (NCT03137355 chunk 1)
- **GENOMIT, NCT05554835:** recruiting global registry targeting 6,000 mitochondrial-disease participants, with annual HPO-coded phenotyping and NPMDS/NMDAS outcomes. https://clinicaltrials.gov/study/NCT05554835. (NCT05554835 chunk 1)

## 13. Prevention

The genetic defect cannot currently be prevented after conception by lifestyle modification. Prevention therefore has three levels:

- **Primary/reproductive:** genetic counseling, carrier testing of relatives, preimplantation genetic testing, chorionic-villus sampling or amniocentesis for known familial variants, and use of donor gametes if desired. Mitochondrial replacement therapy is not relevant because NDUFS8 is nuclear, not mtDNA-encoded.
- **Secondary:** early recognition and molecular diagnosis in symptomatic infants/siblings; targeted testing of at-risk relatives. No validated population newborn screen exists.
- **Tertiary:** prevent catabolic decompensation, aspiration, malnutrition, contractures, respiratory failure, avoidable anesthetic risk, and untreated cardiomyopathy through surveillance and emergency planning.

Vaccination is not a disease-specific prophylaxis but can reduce infection-triggered metabolic stress. No preventive medication has proven efficacy.

## 14. Other species and natural disease

NDUFS8 orthologs are evolutionarily conserved across eukaryotes and prokaryotes, reflecting the conserved complex-I core. No naturally occurring veterinary disorder caused specifically by an NDUFS8 ortholog was identified in the retrieved evidence. Thus, no species, breed, or VBO term can be assigned confidently for a natural NDUFS8 disease.

A 2024 canine Leigh syndrome report involved **NDUFS7**, not NDUFS8; it should not be annotated as an MC1DN2 natural model. There is no zoonotic potential, transmission, or cross-species infectious susceptibility.

## 15. Model organisms and experimental systems

### NDUFS8-specific models

The best validated model is the obligately aerobic yeast **Yarrowia lipolytica**, in which human-equivalent p.Pro79Leu and p.Arg102His variants were reconstructed. Each reduced complex-I Vmax by approximately 50%; p.Pro79Leu altered rotenone sensitivity and p.Arg102His caused mild hypersensitivity to DQA. This model directly tests catalytic/structural effects but cannot reproduce mammalian brain development, cardiomyopathy, or multisystem natural history. (henke2024diseasemodelsof pages 5-6)

Cellular models include patient fibroblasts, lymphoblasts, and NDUFS8-deficient engineered cells. The 2024 HUVEC/endothelial shRNA and CRISPR models reveal ATP/ROS/Akt–mTOR and angiogenic consequences, while the TAT-NDUFS8 system provides a platform for protein-replacement screening. (wang2022emergingrolesof pages 4-5, xiong2024therequirementof pages 1-2)

### Broader Leigh models—not genotype-equivalent

The Ndufs4-knockout mouse is the dominant mammalian complex-I Leigh model, while Drosophila, zebrafish, *C. elegans*, patient iPSCs, neurons, cardiomyocytes, and organoids model other Leigh genotypes. A 2024 expert review emphasizes that iPSCs and organoids enable cell-type-specific phenotyping and high-throughput drug screening, but each model captures only selected aspects of heterogeneous Leigh disease. DOI: https://doi.org/10.1002/jimd.12804; published online following acceptance on September 18, 2024. (henke2024diseasemodelsof pages 1-2)

These models are useful for pathway-level hypotheses but should not be labeled NDUFS8 models unless the NDUFS8 genotype is engineered directly.

## Direct supporting quotations

The 1998 landmark abstract states: **“Cycle sequencing of amplified NDUFS8 cDNA of 20 patients with isolated enzymatic complex I deficiency revealed two compound heterozygous transitions in a patient with neuropathologically proven Leigh syndrome.”** It further reports: **“The first mutation was a C236T (P79L), and the second mutation was a G305A (R102H).”** (loeffen1998thefirstnuclearencoded pages 1-2)

The later case-series abstract states: **“Here we report the unusual clinical presentation of ‘Progressive External Ophthalmoplegia (PEO) plus’ Leigh syndrome in three children from a consanguineous family where exome sequencing identified mutations in NDUFS8.”** It emphasizes that the patients had **“a later onset, milder and a clinically distinct phenotype.”** (marina2013ndufs8relatedcomplexi pages 1-2)

The 2024 modeling review concludes that iPSCs permit study in **“neurons, cardiomyocytes, and even three-dimensional organoids”** and that complementary models may be instrumental in finding treatments for this **“currently untreatable disease.”** This is an authoritative Leigh-spectrum opinion, not evidence that those models or therapies have already been validated for NDUFS8. (henke2024diseasemodelsof pages 1-2)

## Knowledge-base conclusions and gaps

The most defensible knowledge-base representation is: **MONDO:0032606 → biallelic germline NDUFS8 missense dysfunction → impaired complex-I assembly/electron transfer → reduced oxidative phosphorylation and ATP with lactate/ROS stress → preferential injury to bilateral basal ganglia/brainstem, skeletal muscle, heart, and respiratory-control systems → variable Leigh-spectrum disease.** (OpenTargets Search: Mitochondrial complex I deficiency, nuclear type 2, loeffen1998thefirstnuclearencoded pages 2-3, wang2022emergingrolesof pages 4-5)

Priority gaps are a curated ClinVar/gnomAD variant table, prospective NDUFS8 natural history, standardized phenotype frequencies, formal QoL data, tissue-resolved omics, a mammalian NDUFS8 knock-in model, clinically relevant neuronal/cardiac organoids, and genotype-specific therapeutic trials. The 2023–2024 advances are principally stronger Leigh modeling, registries, and mechanistic NDUFS8 cell biology—not a new targeted therapy or a large NDUFS8 clinical cohort. (henke2024diseasemodelsof pages 1-2, xiong2024therequirementof pages 1-2, NCT03137355 chunk 1, NCT05554835 chunk 1)

References

1. (OpenTargets Search: Mitochondrial complex I deficiency, nuclear type 2): Open Targets Query (Mitochondrial complex I deficiency, nuclear type 2, 1 results). Buniello, A. et al. (2025). Open Targets Platform: facilitating therapeutic hypotheses building in drug discovery. Nucleic Acids Research.

2. (wang2022emergingrolesof pages 4-5): Sifan Wang, Yuanbo Kang, Ruifeng Wang, Ju-feng Deng, Yupei Yu, Jun Yu, and Junpu Wang. Emerging roles of ndufs8 located in mitochondrial complex i in different diseases. Molecules, 27:8754, Dec 2022. URL: https://doi.org/10.3390/molecules27248754, doi:10.3390/molecules27248754. This article has 30 citations.

3. (loeffen1998thefirstnuclearencoded pages 2-3): Jan Loeffen, Jan Smeitink, Ralf Triepels, Roel Smeets, Markus Schuelke, Rob Sengers, Frans Trijbels, Ben Hamel, Renier Mullaart, and Lambert van den Heuvel. The first nuclear-encoded complex i mutation in a patient with leigh syndrome. American journal of human genetics, 63 6:1598-608, Dec 1998. URL: https://doi.org/10.1086/302154, doi:10.1086/302154. This article has 386 citations and is from a highest quality peer-reviewed journal.

4. (loeffen1998thefirstnuclearencoded pages 1-2): Jan Loeffen, Jan Smeitink, Ralf Triepels, Roel Smeets, Markus Schuelke, Rob Sengers, Frans Trijbels, Ben Hamel, Renier Mullaart, and Lambert van den Heuvel. The first nuclear-encoded complex i mutation in a patient with leigh syndrome. American journal of human genetics, 63 6:1598-608, Dec 1998. URL: https://doi.org/10.1086/302154, doi:10.1086/302154. This article has 386 citations and is from a highest quality peer-reviewed journal.

5. (marina2013ndufs8relatedcomplexi pages 2-4): Adela Della Marina, Ulrike Schara, Angela Pyle, Claudia Möller-Hartmann, Elke Holinski-Feder, Angela Abicht, Birgit Czermin, Hanns Lochmüller, Helen Griffin, Mauro Santibanez-Koref, Patrick F. Chinnery, and Rita Horvath. Ndufs8-related complex i deficiency extends phenotype from "peo plus" to leigh syndrome. JIMD reports, 10:17-22, Jan 2013. URL: https://doi.org/10.1007/8904\_2012\_195, doi:10.1007/8904\_2012\_195. This article has 24 citations and is from a peer-reviewed journal.

6. (wang2022emergingrolesof pages 2-4): Sifan Wang, Yuanbo Kang, Ruifeng Wang, Ju-feng Deng, Yupei Yu, Jun Yu, and Junpu Wang. Emerging roles of ndufs8 located in mitochondrial complex i in different diseases. Molecules, 27:8754, Dec 2022. URL: https://doi.org/10.3390/molecules27248754, doi:10.3390/molecules27248754. This article has 30 citations.

7. (wang2022emergingrolesof pages 5-6): Sifan Wang, Yuanbo Kang, Ruifeng Wang, Ju-feng Deng, Yupei Yu, Jun Yu, and Junpu Wang. Emerging roles of ndufs8 located in mitochondrial complex i in different diseases. Molecules, 27:8754, Dec 2022. URL: https://doi.org/10.3390/molecules27248754, doi:10.3390/molecules27248754. This article has 30 citations.

8. (marina2013ndufs8relatedcomplexi pages 1-2): Adela Della Marina, Ulrike Schara, Angela Pyle, Claudia Möller-Hartmann, Elke Holinski-Feder, Angela Abicht, Birgit Czermin, Hanns Lochmüller, Helen Griffin, Mauro Santibanez-Koref, Patrick F. Chinnery, and Rita Horvath. Ndufs8-related complex i deficiency extends phenotype from "peo plus" to leigh syndrome. JIMD reports, 10:17-22, Jan 2013. URL: https://doi.org/10.1007/8904\_2012\_195, doi:10.1007/8904\_2012\_195. This article has 24 citations and is from a peer-reviewed journal.

9. (conti2023redflagsin pages 1-2): Federica Conti, Serena Di Martino, Filippo Drago, Claudio Bucolo, Vincenzo Micale, Vincenzo Montano, Gabriele Siciliano, Michelangelo Mancuso, and Piervito Lopriore. Red flags in primary mitochondrial diseases: what should we recognize? International Journal of Molecular Sciences, 24:16746, Nov 2023. URL: https://doi.org/10.3390/ijms242316746, doi:10.3390/ijms242316746. This article has 18 citations.

10. (NCT02352896 chunk 1):  Long-Term Safety and Efficacy Evaluation of EPI-743 in Children With Leigh Syndrome. PTC Therapeutics. 2014. ClinicalTrials.gov Identifier: NCT02352896

11. (NCT05162768 chunk 1):  Study to Evaluate Efficacy and Safety of Elamipretide in Subjects With Primary Mitochondrial Disease From Nuclear DNA Mutations (nPMD). Stealth BioTherapeutics Inc.. 2022. ClinicalTrials.gov Identifier: NCT05162768

12. (NCT03137355 chunk 1): Mary Kay Koenig. The International Registry for Leigh Syndrome. The University of Texas Health Science Center, Houston. 2015. ClinicalTrials.gov Identifier: NCT03137355

13. (NCT05554835 chunk 1): Prof. Thomas Klopstock. Global Registry and Natural History Study for Mitochondrial Disorders. LMU Klinikum. 2009. ClinicalTrials.gov Identifier: NCT05554835

14. (henke2024diseasemodelsof pages 5-6): Marie‐Thérèse Henke, Alessandro Prigione, and Markus Schuelke. Disease models of leigh syndrome: from yeast to organoids. Journal of Inherited Metabolic Disease, 47:1292-1321, Oct 2024. URL: https://doi.org/10.1002/jimd.12804, doi:10.1002/jimd.12804. This article has 19 citations and is from a peer-reviewed journal.

15. (xiong2024therequirementof pages 1-2): Qian-wei Xiong, Kun Jiang, Xiao-wei Shen, Zhou-rui Ma, Xiang-ming Yan, Hao Xia, and Xu Cao. The requirement of the mitochondrial protein ndufs8 for angiogenesis. Cell Death &amp; Disease, Apr 2024. URL: https://doi.org/10.1038/s41419-024-06636-3, doi:10.1038/s41419-024-06636-3. This article has 22 citations and is from a peer-reviewed journal.

16. (henke2024diseasemodelsof pages 1-2): Marie‐Thérèse Henke, Alessandro Prigione, and Markus Schuelke. Disease models of leigh syndrome: from yeast to organoids. Journal of Inherited Metabolic Disease, 47:1292-1321, Oct 2024. URL: https://doi.org/10.1002/jimd.12804, doi:10.1002/jimd.12804. This article has 19 citations and is from a peer-reviewed journal.

17. (marina2013ndufs8relatedcomplexi pages 4-5): Adela Della Marina, Ulrike Schara, Angela Pyle, Claudia Möller-Hartmann, Elke Holinski-Feder, Angela Abicht, Birgit Czermin, Hanns Lochmüller, Helen Griffin, Mauro Santibanez-Koref, Patrick F. Chinnery, and Rita Horvath. Ndufs8-related complex i deficiency extends phenotype from "peo plus" to leigh syndrome. JIMD reports, 10:17-22, Jan 2013. URL: https://doi.org/10.1007/8904\_2012\_195, doi:10.1007/8904\_2012\_195. This article has 24 citations and is from a peer-reviewed journal.

18. (maack2025mitochondrialcardiomyopathiespathogenesis pages 6-7): Christoph Maack, Jan Dudek, Edoardo Bertero, Emmanouil Tampakakis, and Hilary J Vernon. Mitochondrial cardiomyopathies: pathogenesis, diagnosis, and treatment. European heart journal, Jul 2025. URL: https://doi.org/10.1093/eurheartj/ehaf491, doi:10.1093/eurheartj/ehaf491. This article has 9 citations and is from a highest quality peer-reviewed journal.

19. (maack2025mitochondrialcardiomyopathiespathogenesis pages 8-8): Christoph Maack, Jan Dudek, Edoardo Bertero, Emmanouil Tampakakis, and Hilary J Vernon. Mitochondrial cardiomyopathies: pathogenesis, diagnosis, and treatment. European heart journal, Jul 2025. URL: https://doi.org/10.1093/eurheartj/ehaf491, doi:10.1093/eurheartj/ehaf491. This article has 9 citations and is from a highest quality peer-reviewed journal.

20. (maack2025mitochondrialcardiomyopathiespathogenesis pages 1-2): Christoph Maack, Jan Dudek, Edoardo Bertero, Emmanouil Tampakakis, and Hilary J Vernon. Mitochondrial cardiomyopathies: pathogenesis, diagnosis, and treatment. European heart journal, Jul 2025. URL: https://doi.org/10.1093/eurheartj/ehaf491, doi:10.1093/eurheartj/ehaf491. This article has 9 citations and is from a highest quality peer-reviewed journal.

21. (li2024newinsightsinto pages 12-13): Ya Li, Huhu Zhang, Chunjuan Yu, Xiaolei Dong, Fanghao Yang, Mengjun Wang, Ziyuan Wen, Mohan Su, Bing Li, and Lina Yang. New insights into mitochondria in health and diseases. International Journal of Molecular Sciences, 25:9975, Sep 2024. URL: https://doi.org/10.3390/ijms25189975, doi:10.3390/ijms25189975. This article has 65 citations.

## Artifacts

- [Edison artifact artifact-00](Mitochondrial_Complex_I_Deficiency_Nuclear_Type_2-deep-research-falcon_artifacts/artifact-00.md)

## Reference Validation

Checked with `linkml-reference-validator` 0.2.1.

| Outcome | Count |
| --- | --- |
| References checked | 8 |
| Resolved | 8 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 8 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.